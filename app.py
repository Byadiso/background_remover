import io
from pathlib import Path

import numpy as np
import streamlit as st
from PIL import Image, ImageOps

st.set_page_config(page_title="Background Remover Studio", page_icon="✂️", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""<style>
.stApp {background: #f7f8fc; color: #182238;}
/* Keep native Streamlit controls readable regardless of the OS/browser theme. */
[data-testid="stAppViewContainer"], [data-testid="stMain"], [data-testid="stMainBlockContainer"] {color: #182238;}
[data-testid="stWidgetLabel"] p, [data-testid="stRadio"] label p, [data-testid="stCheckbox"] label p, [data-testid="stSlider"] label p {color: #182238 !important;}
[data-testid="stFileUploader"] section {background: #ffffff; border: 1px dashed #9baecc;}
[data-testid="stFileUploader"] section *, [data-testid="stFileUploader"] small {color: #182238 !important;}
[data-testid="stFileUploader"] button {color: #1b3769 !important; background: #eef3ff !important; border: 1px solid #c5d4ed !important;}
[data-testid="stTabs"] button {color: #344158;}
[data-testid="stTabs"] button[aria-selected="true"] {color: #1d4ed8;}
.block-container {max-width: 1220px; padding-top: 2.2rem; padding-bottom: 3rem;}
#MainMenu, footer {visibility: hidden;}
h1, h2, h3 {letter-spacing: -.035em;}
.hero {padding: 1.65rem 1.9rem; border-radius: 22px; background: linear-gradient(115deg,#192c52,#304e86); color: white; margin-bottom: 1.3rem;}
.hero h1 {color: white; font-size: 2.35rem; margin: .2rem 0 .35rem;}
.hero p {color: #dbe6ff; margin: 0; font-size: 1.02rem;}
.eyebrow {font-size: .75rem; font-weight: 750; letter-spacing: .13em; color: #b8cafa;}
.panel-title {font-size: 1.12rem; font-weight: 750; margin-bottom: .3rem; color: #182238;}
.panel-note {color: #66748b; font-size: .88rem; margin-bottom: .7rem;}
.info-strip {background: white; border: 1px solid #e4e8f0; border-radius: 12px; padding: .75rem 1rem; margin: .8rem 0 1.1rem; color: #344158;}
.stButton > button[kind="primary"], .stDownloadButton > button[kind="primary"] {border-radius: 11px; font-weight: 700;}
[data-testid="stFileUploader"] {border-radius: 15px;}
[data-testid="stImage"] img {border-radius: 12px;}
[data-testid="stVerticalBlockBorderWrapper"] {background: white; border-radius: 17px;}
</style>""", unsafe_allow_html=True)

st.markdown('''<div class="hero"><div class="eyebrow">IMAGE TOOLS · LOCAL WORKFLOW</div>
<h1>✂️ Background Remover Studio</h1>
<p>Remove backgrounds or preserve existing transparency. Keep every original pixel dimension.</p></div>''', unsafe_allow_html=True)

with st.container(border=True):
    st.markdown('<div class="panel-title">01 · Choose your image</div><div class="panel-note">PNG, JPG, JPEG, or WebP · Processed in your current Streamlit session</div>', unsafe_allow_html=True)
    uploaded = st.file_uploader("Drop an image here or browse files", type=["png", "jpg", "jpeg", "webp"], label_visibility="collapsed")

left, right = st.columns([1, 1.55], gap="large")
with left:
    with st.container(border=True):
        st.markdown('<div class="panel-title">02 · Processing settings</div><div class="panel-note">Choose the same methods as the previous version.</div>', unsafe_allow_html=True)
        mode = st.radio("Background method", ["Preserve existing transparency (best for transparent PNGs)", "Remove solid-color background"], index=0, help="Preserve leaves existing transparency and colors untouched. Solid-color removal uses the top-left pixel as its background sample.")
        tolerance, feather, remove_inside = 20, 8, True
        if mode.startswith("Remove"):
            st.info("The background color is sampled from the top-left pixel. This method works best on uniform backgrounds.")
            tolerance = st.slider("Background color tolerance", 0, 100, 20, help="Higher values remove more colors similar to the sampled background.")
            feather = st.slider("Soft edge width (color distance)", 0, 40, 8, help="Higher values create a softer transition at edges.")
            remove_inside = st.checkbox("Remove matching background inside enclosed areas", True, help="When disabled, only connected background regions touching the image border are removed.")
        else:
            st.success("Existing alpha transparency and RGB colors are preserved exactly.", icon="✅")
    with st.container(border=True):
        st.markdown('<div class="panel-title">Export guarantees</div>', unsafe_allow_html=True)
        st.markdown("✅ Original width and height  \n✅ Real PNG alpha transparency  \n✅ No forced resizing  \n✅ No AI recoloring")

with right:
    with st.container(border=True):
        st.markdown('<div class="panel-title">03 · Preview & download</div><div class="panel-note">Review the result before saving the full-resolution PNG.</div>', unsafe_allow_html=True)
        if uploaded is None:
            st.info("Upload an image above to see your original and processed result here.", icon="🖼️")
        else:
            try:
                src = ImageOps.exif_transpose(Image.open(uploaded)).convert("RGBA")
                arr = np.asarray(src).copy()
                if mode.startswith("Remove"):
                    bg = arr[0, 0, :3].astype(np.float32)
                    dist = np.max(np.abs(arr[:, :, :3].astype(np.float32) - bg), axis=2)
                    if remove_inside:
                        alpha = (np.clip((dist - tolerance) / max(feather, 1) * 255, 0, 255).astype(np.uint8)
                                 if feather else np.where(dist > tolerance, 255, 0).astype(np.uint8))
                    else:
                        import cv2
                        candidate = (dist <= tolerance).astype(np.uint8)
                        n, labels = cv2.connectedComponents(candidate, connectivity=4)
                        border = np.unique(np.concatenate([labels[0, :], labels[-1, :], labels[:, 0], labels[:, -1]]))
                        region = np.isin(labels, border) & (candidate > 0)
                        alpha = np.where(region, 0, 255).astype(np.uint8)
                    arr[:, :, 3] = np.minimum(arr[:, :, 3], alpha)
                result = Image.fromarray(arr, "RGBA")
                st.markdown(f'<div class="info-strip">📐 <b>{src.width:,} × {src.height:,} px</b> &nbsp;·&nbsp; PNG output &nbsp;·&nbsp; RGBA transparency</div>', unsafe_allow_html=True)
                tab_original, tab_result, tab_side = st.tabs(["Original", "Transparent result", "Compare side by side"])
                with tab_original:
                    st.image(src, caption="Original upload", use_container_width=True)
                with tab_result:
                    st.image(result, caption="Transparent PNG (viewer may show black or checkerboard behind transparent pixels)", use_container_width=True)
                with tab_side:
                    a, b = st.columns(2)
                    with a:
                        st.image(src, caption="Before", use_container_width=True)
                    with b:
                        st.image(result, caption="After", use_container_width=True)
                buffer = io.BytesIO()
                result.save(buffer, format="PNG")
                name = Path(uploaded.name).stem + "_transparent.png"
                st.download_button("⬇ Download transparent PNG · original size", buffer.getvalue(), file_name=name, mime="image/png", type="primary", use_container_width=True)
                st.caption("The preview is scaled to fit the page. The downloaded file is not resized.")
            except Exception as exc:
                st.error(f"Couldn't process this image: {exc}")

st.caption("Background Remover Studio · Processing methods preserved from the previous version · No external AI model downloads")

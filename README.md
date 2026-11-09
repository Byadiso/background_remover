# Background Remover Studio

A cleaner Streamlit interface for preserving existing transparency and removing solid-color backgrounds. **The image-processing methods and default settings are unchanged** from the previous graphics background remover.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8503
```

Open http://127.0.0.1:8503/ . If port 8503 is in use, change to 8504.

## Features

- PNG, JPG, JPEG and WebP upload
- Preserve existing transparency (default; does not alter RGB or alpha)
- Remove a solid-color background using the top-left pixel, with tolerance and feather controls
- Optionally remove matching colors inside enclosed areas
- Before/after preview and original-size RGBA PNG download
- No automatic image resizing

**Note:** Solid-color removal is intended for relatively uniform backgrounds; it is not a general-purpose photo segmentation model. Previews are displayed at browser-friendly sizes, but downloads preserve pixel dimensions. Large files can require substantial memory on a hosted Streamlit instance.

## GitHub and Streamlit Community Cloud (when you're ready)

1. Create a GitHub repository and add `app.py`, `requirements.txt`, and `README.md` to the repository root.
2. Push the repository to GitHub.
3. Sign in at https://share.streamlit.io/ with GitHub, choose **Create app**, select your repository/branch and `app.py`, then deploy.
4. Streamlit will give you a public `*.streamlit.app` URL that you can share.

Note that a publicly deployed app processes uploaded images on the hosted server, not your local computer. Consider privacy and hosting limits before using sensitive or very large files.


### Display theme
The included `.streamlit/config.toml` forces a readable light theme for Streamlit widgets. Run the app from this project folder so Streamlit picks up the configuration. Restart the server after replacing the files.

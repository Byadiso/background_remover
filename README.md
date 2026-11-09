# Background Remover Studio

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/Source-GitHub-181717?logo=github&logoColor=white)](https://github.com/Byadiso/background_remover)
[![License](https://img.shields.io/badge/License-Not%20Specified-lightgrey)](https://github.com/Byadiso/background_remover)

A lightweight, user-friendly background removal application built with **Python and Streamlit**.

Background Remover Studio allows users to remove solid-color backgrounds, preserve existing transparency, and export high-quality PNG images while maintaining their original dimensions.

Designed for product images, logos, illustrations, digital artwork, and other graphics.

## Features

- **Background Removal** — Remove solid-color backgrounds with adjustable color tolerance.
- **Transparent PNG Export** — Export images with genuine alpha transparency.
- **Full-Resolution Output** — Preserve original image dimensions without automatic resizing.
- **Transparency Preservation** — Maintain existing RGB colors and alpha values.
- **Edge Refinement** — Adjustable feathering for smoother edges.
- **Interior Background Removal** — Optionally remove matching colors inside enclosed areas.
- **Before & After Preview** — Compare original and processed images.
- **Multiple Image Formats** — Supports PNG, JPG, JPEG, and WebP.
- **Modern Interface** — Clean, intuitive, browser-based experience.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| Pillow (PIL) | Image manipulation and export |
| NumPy | Pixel-level image processing |

## Getting Started

### Prerequisites

- Python 3.12 or a compatible version
- pip package manager
- Git (optional)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Byadiso/background_remover.git
cd background_remover
```

**2. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**3. Run the application**

```bash
python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8503
```

**4. Open in your browser**

Visit [http://127.0.0.1:8503](http://127.0.0.1:8503).

If port `8503` is unavailable, use another port such as `8504`.

## How to Use

1. **Upload an image** — Select a PNG, JPG, JPEG, or WebP file.
2. **Choose a processing method** — Preserve existing transparency or remove a solid-color background.
3. **Adjust settings** — Fine-tune tolerance, feathering, and interior background removal when applicable.
4. **Preview the result** — Compare the original image with the processed output.
5. **Download** — Save the final image as a full-resolution transparent PNG.

## Image Quality

Background Remover Studio prioritizes maintaining image quality and original dimensions.

| Property | Description |
|---|---|
| Output format | PNG |
| Color mode | RGBA |
| Background | Transparent when successfully removed |
| Resolution | Original dimensions preserved |
| Automatic resizing | Disabled |
| Existing transparency | Preserved in transparency-preservation mode |

Previews may be scaled for browser display, but exported images retain their original pixel dimensions.

## Limitations

The application uses color-based background removal rather than AI-powered segmentation.

Results are most reliable with relatively uniform backgrounds. Complex backgrounds or colors similar to the foreground may require additional refinement.

Processing large images may require substantial system memory.

## Contributing

Contributions, suggestions, and bug reports are welcome.

To contribute, open an [issue](https://github.com/Byadiso/background_remover/issues) or submit a pull request through the GitHub repository.

## Author

**Byamungu Desire**

Creator and maintainer of Background Remover Studio.

- **GitHub:** [@Byadiso](https://github.com/Byadiso)
- **Repository:** [Background Remover Studio](https://github.com/Byadiso/background_remover)

---

**Background Remover Studio** — Simple background removal. Real transparency. Original resolution.

Developed and maintained by **Byamungu Desire**.
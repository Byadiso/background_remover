# Background Remover Studio

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](https://github.com/Byadiso/background_remover/pulls)

A lightweight, open-source background removal application built with **Python and Streamlit**.

Background Remover Studio makes it easy to remove solid-color backgrounds, preserve existing transparency, and export high-quality PNG images without changing their original dimensions.

Designed for product images, logos, illustrations, digital artwork, and other graphics.

## Features

- **Background Removal** — Remove solid-color backgrounds with adjustable color tolerance.
- **Transparent PNG Export** — Export images with genuine alpha transparency.
- **Full-Resolution Output** — Preserve original image dimensions without resizing.
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

If port `8503` is unavailable, use another available port.

## How to Use

1. **Upload an image** — Select a PNG, JPG, JPEG, or WebP file.
2. **Choose a processing method** — Preserve existing transparency or remove a solid-color background.
3. **Adjust settings** — Fine-tune tolerance, feathering, and interior background removal when applicable.
4. **Preview the result** — Compare the original image with the processed output.
5. **Download** — Save the final image as a full-resolution transparent PNG.

## Image Quality

Background Remover Studio prioritizes maintaining original image dimensions and transparency.

| Property | Description |
|---|---|
| Output format | PNG |
| Color mode | RGBA |
| Background | Transparent where successfully removed |
| Resolution | Original dimensions preserved |
| Automatic resizing | Disabled |
| Existing transparency | Preserved in transparency-preservation mode |

Image previews may be scaled for browser display, but exported files retain their original pixel dimensions.

## Limitations

The application uses color-based background removal rather than AI-powered segmentation.

Results are most reliable with relatively uniform backgrounds. Complex backgrounds or colors similar to the foreground may require additional refinement.

Processing large images may require substantial system memory.

## Contributing

**Contributions are welcome!**

Background Remover Studio is an open-source project. Developers are encouraged to improve the application, report issues, suggest features, and contribute code.

To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them.
4. Push your branch to GitHub.
5. Open a pull request with a description of your changes.

For bugs or feature requests, please [open an issue](https://github.com/Byadiso/background_remover/issues).

## License

This project is licensed under the **MIT License**.

You are free to use, copy, modify, distribute, and contribute to the software, including for commercial purposes, provided the original copyright and license notice are retained.

See the [LICENSE](LICENSE) file for full details.

## Author

**Byamungu Desire**

Creator and maintainer of Background Remover Studio.

- **GitHub:** [@Byadiso](https://github.com/Byadiso)
- **Repository:** [Background Remover Studio](https://github.com/Byadiso/background_remover)

---

**Background Remover Studio** — Simple background removal. Real transparency. Original resolution.

Copyright © 2026 Byamungu Desire. Licensed under MIT.
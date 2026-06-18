# AI-Powered Optical Character Recognition (OCR)

This project uses PaddleOCR to extract text from image files and scanned PDFs. It writes the result to TXT by default and can also export DOCX and JSON.

## Supported Inputs

- Image files: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tif`, `.tiff`, `.webp`
- Scanned PDF documents

## Outputs

- TXT: always generated
- DOCX: optional with `--docx`
- JSON: optional with `--json`

## Installation

Install the dependencies listed in [requirement.txt](requirement.txt). This project uses the headless OpenCV build to avoid `libGL.so.1` import issues. For PDF support, `pdf2image` also needs Poppler installed on your system.

## Usage

Run the CLI with either `main.py` or `ocr.py`:

```bash
python main.py path/to/file.pdf
python ocr.py path/to/image.jpg --docx --json
```

By default, output files are written to the `output/` directory using the input filename as the base name.

## Example Output

For `invoice.jpg`, the tool writes:

- `output/invoice.txt`
- `output/invoice.docx` when `--docx` is used
- `output/invoice.json` when `--json` is used

## Notes

- The OCR engine is loaded lazily, so importing the module does not immediately download or initialize the model.
- DOCX export is optional and requires `python-docx`.

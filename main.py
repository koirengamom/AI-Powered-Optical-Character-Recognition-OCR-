import os
from paddleocr import PaddleOCR
from pdf2image import convert_from_path

# Initialize OCR model

ocr = PaddleOCR(
use_angle_cls=True,
lang='en'
)

IMAGE_EXTENSIONS = (
'.jpg', '.jpeg', '.png',
'.bmp', '.tiff', '.webp'
)

OUTPUT_DIR = "output"

def extract_text_from_image(image_path):
result = ocr.ocr(image_path, cls=True)

```
extracted_text = []

for line in result:
    for word_info in line:
        text = word_info[1][0]
        confidence = word_info[1][1]

        extracted_text.append(
            f"{text} (Confidence: {confidence:.2f})"
        )

return "\n".join(extracted_text)
```

def extract_text_from_pdf(pdf_path):
pages = convert_from_path(pdf_path)

```
complete_text = []

for page_number, page in enumerate(pages, start=1):

    temp_image = f"temp_page_{page_number}.jpg"
    page.save(temp_image, "JPEG")

    page_text = extract_text_from_image(temp_image)

    complete_text.append(
        f"\n========== PAGE {page_number} ==========\n"
    )
    complete_text.append(page_text)

    os.remove(temp_image)

return "\n".join(complete_text)
```

def save_text(text, input_file):
os.makedirs(OUTPUT_DIR, exist_ok=True)

```
filename = os.path.splitext(
    os.path.basename(input_file)
)[0]

output_file = os.path.join(
    OUTPUT_DIR,
    filename + ".txt"
)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

return output_file
```

def main():

```
print("=" * 40)
print(" AI-Powered OCR using PaddleOCR ")
print("=" * 40)

file_path = input(
    "\nEnter image or PDF path: "
).strip()

if not os.path.exists(file_path):
    print("Error: File not found.")
    return

extension = os.path.splitext(
    file_path
)[1].lower()

try:

    if extension in IMAGE_EXTENSIONS:

        print("\nImage detected...")
        text = extract_text_from_image(
            file_path
        )

    elif extension == ".pdf":

        print("\nPDF detected...")
        text = extract_text_from_pdf(
            file_path
        )

    else:
        print(
            "Unsupported file format."
        )
        return

    print("\nExtracted Text:\n")
    print(text)

    output_file = save_text(
        text,
        file_path
    )

    print(
        f"\nText saved successfully to:\n{output_file}"
    )

except Exception as e:
    print(
        f"\nError occurred: {e}"
    )
```

if **name** == "**main**":
main()

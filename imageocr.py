#python
import os
from paddleocr import PaddleOCR

# Initialize PaddleOCR
ocr = PaddleOCR(
    use_textline_orientation=True,
    lang="en"
)

# Supported image formats
IMAGE_EXTENSIONS = (
    ".jpg", ".jpeg", ".png",
    ".bmp", ".tiff", ".webp"
)

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def extract_text_from_image(image_path):

    # Check file exists
    if not os.path.exists(image_path):
        print("Error: File not found!")
        return

    # Check extension
    if not image_path.lower().endswith(IMAGE_EXTENSIONS):
        print("Error: Unsupported image format!")
        return

    print("\nProcessing image...\n")

    try:
        results = ocr.predict(image_path)

        extracted_text = []

        print("----- OCR RESULT -----\n")

        for result in results:

            # Print complete result for debugging
            print(result)

            # Try extracting recognized text
            if hasattr(result, "rec_texts"):

                texts = result.rec_texts
                scores = result.rec_scores

                for text, score in zip(texts, scores):

                    extracted_text.append(text)

                    print(
                        f"Text: {text} | "
                        f"Confidence: {score:.2f}"
                    )

        final_text = "\n".join(extracted_text)

        print("\n----- EXTRACTED TEXT -----\n")
        print(final_text)

        # Save output
        filename = os.path.splitext(
            os.path.basename(image_path)
        )[0]

        output_file = os.path.join(
            OUTPUT_DIR,
            f"{filename}.txt"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(final_text)

        print(f"\nText saved to: {output_file}")

    except Exception as e:
        print(f"\nOCR Error: {e}")


if __name__ == "__main__":

    image_path = input(
        "Enter image path: "
    ).strip()

    extract_text_from_image(image_path)

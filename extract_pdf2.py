import sys
import os

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Installing PyMuPDF...")
    os.system("pip install PyMuPDF")
    import fitz

def extract_text(pdf_path, output_txt):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text() + "\n---PAGE BREAK---\n"
        
        with open(output_txt, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Successfully extracted text to {output_txt}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_pdf2.py <pdf_path> <output_txt>")
        sys.exit(1)
    
    extract_text(sys.argv[1], sys.argv[2])

import sys
import os

try:
    import PyPDF2
except ImportError:
    print("Installing PyPDF2...")
    os.system("pip install PyPDF2")
    import PyPDF2

def extract_text(pdf_path, output_txt):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n---PAGE BREAK---\n"
        
        with open(output_txt, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Successfully extracted text to {output_txt}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_pdf.py <pdf_path> <output_txt>")
        sys.exit(1)
    
    extract_text(sys.argv[1], sys.argv[2])

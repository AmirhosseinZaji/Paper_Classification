import os
import re
from PyPDF2 import PdfReader

def clean_text(text):
    # Remove non-printable characters
    text = ''.join(char for char in text if char.isprintable())
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove isolated single characters
    text = re.sub(r'\s+(\S)\s+', ' ', text)
    
    return text

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def process_pdfs(input_folder, output_folder):

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            raw_text = extract_text_from_pdf(pdf_path)
            cleaned_text = clean_text(raw_text)
            
            # Save the cleaned text to a new file with the same name in the output folder
            output_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(output_folder, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_text)
            
            print(f"Processed: {filename} -> {output_filename}")

if __name__ == "__main__":
    input_folder = "papers/pdfs"
    output_folder = "papers/txts"
    process_pdfs(input_folder, output_folder)
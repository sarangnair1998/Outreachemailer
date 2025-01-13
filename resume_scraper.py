import fitz
import os
print("PyMuPDF is installed and working!")

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    :param pdf_path: Path to the PDF file
    :return: Extracted text as a string
    """
    text = ""
    
    try:
        doc = fitz.open(pdf_path)  
        for page in doc:
            text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

    return text.strip() 


home_dir = os.path.expanduser("~")  
pdf_path = os.path.join(home_dir, "Documents", "Resume for work", "Robotics Resume 2025.pdf")


resume_text = extract_text_from_pdf(pdf_path)

output_text_path = os.path.join(home_dir, "Documents", "Resume for work", "extracted_resume.txt")
with open(output_text_path, "w") as f:
    f.write(resume_text)

print("Extracted Resume Content:\n", resume_text)
print(f"Resume text saved to: {output_text_path}")

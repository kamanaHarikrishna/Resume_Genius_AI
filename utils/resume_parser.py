import pdfplumber
import docx2txt

def extract_resume_text(file):
    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        return docx2txt.process(file)
    else:
        return "Unsupported file type"
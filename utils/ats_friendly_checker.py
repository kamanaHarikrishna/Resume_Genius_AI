from PyPDF2 import PdfReader

def check_ats_friendly(resume_file):
    issues = []
    if resume_file.type != "application/pdf":
        issues.append("Resume is not in PDF format")

    try:
        pdf = PdfReader(resume_file)
        for page in pdf.pages:
            if '/Annots' in page:
                issues.append("Embedded annotations may affect parsing")
    except:
        issues.append("PDF parsing failed")

    return {"issues_found": issues or ["No major ATS issues detected"]}

from pypdf import PdfReader

def read_pdf(path: str):
    """
    Reads text from a PDF file.
    """
    reader = PdfReader(path)
    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    return full_text

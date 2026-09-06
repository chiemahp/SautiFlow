import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from all pages of a PDF file.

    Args:
        pdf_path (str): Path to the uploaded PDF file.

    Returns:
        str: Combined text from all pages.
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"

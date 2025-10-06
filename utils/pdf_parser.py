import PyPDF2
import os
from datetime import datetime
#file_path = "./data/uploads/sample.pdf"
def parse_pdf(file_path):
    text = ""
    with open(file_path,"rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    metadata = {
        "file_name": os.path.basename(file_path),
        "file_size": os.path.getsize(file_path),
        "date_parsed": datetime.now().isoformat()
    }
    return text, metadata

#text , metadata = parse_pdf(file_path=file_path)
#print(text)
#print(metadata)
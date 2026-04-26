import pdfplumber
from pathlib import Path

pdfs_dir = Path("pdfs")
markdown_dir = Path("markdown")
markdown_dir.mkdir(exist_ok=True)

for pdf_path in pdfs_dir.glob("*.pdf"):
    text_pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_pages.append(text)

    md_content = "\n\n---\n\n".join(text_pages)
    md_path = markdown_dir / (pdf_path.stem + ".md")
    md_path.write_text(md_content, encoding="utf-8")
    print(f"Converti : {pdf_path.name} -> {md_path.name}")

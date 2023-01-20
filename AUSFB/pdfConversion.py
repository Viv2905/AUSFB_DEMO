from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
    Path.home()
    / "Downloads"
    / "Data Elements.pdf"
    # / "Virtual CreditCard - API"
    # / "Django"
    # / "AUSFB"
    # / "api_app"
    # / "test.pdf"
)
# print(pdf_path)
pdf_reader = PdfFileReader(str(pdf_path))
last_page = pdf_reader.pages[-1]    # Reading Last-page

pdf_writer = PdfFileWriter()
pdf_writer.addPage(last_page)

output_path = Path.home() / "Downloads" / "last_page.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)

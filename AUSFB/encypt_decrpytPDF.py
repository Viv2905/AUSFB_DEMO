from PyPDF2 import PdfFileWriter, PdfFileReader
import os

out = PdfFileWriter()
file = PdfFileReader("ADMIN_test.pdf")
num = file.numPages

for i in range(num):
    page = file.getPage(i)
    out.addPage(page)

password = "password"
out.encrypt(password)

with open("adm_temp.pdf", "wb") as file:
    out.write(file)

# if os.path.exists("ADMIN_test.pdf"):
#     os.remove("ADMIN_test.pdf")
# else:
#     print("File doesn't exist")
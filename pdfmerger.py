from pypdf import PdfMerger
import os
target_path = r"C:/pdf_to_merge/"
os.chdir(target_path)
print('Current working direcory is: '+ os.getcwd())
pdfs = ['Birth_certificate.pdf','eads.pdf', 'passports_and_stamps.pdf', 'highest degree for upload.pdf']
merger = PdfMerger()
for i in pdfs:
    merger.append(i)

merger.write('merged_output.pdf')
merger.close()
import os
from pdf2image import convert_from_path

# Directory containing PDFs
pdf_dir = './figs'

# Output directory for PNGs (can be the same or different)
output_dir = './figs/pngs'
os.makedirs(output_dir, exist_ok=True)

# DPI for image quality
dpi = 300

# Iterate over all PDF files in the directory
for filename in os.listdir(pdf_dir):
    if filename.lower().endswith('.pdf'):
        pdf_path = os.path.join(pdf_dir, filename)
        # Convert PDF pages to images
        pages = convert_from_path(pdf_path, dpi)
        base_name = os.path.splitext(filename)[0]
        # Save each page as a PNG file
        for i, page in enumerate(pages, start=1):
            output_path = os.path.join(output_dir, f"{base_name}-page{i}.png")
            page.save(output_path, 'PNG')
            print(f"Saved {output_path}")

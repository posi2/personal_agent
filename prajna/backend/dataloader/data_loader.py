import PyPDF2
import json

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file and store it in a list by page number."""
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Extract text from each page and store it in a list
        pages_text = []
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            pages_text.append(page_text)
    
    return pages_text

def save_text_to_json(pages_text, json_path):
    """Save the extracted text (by page) into a JSON file."""
    data = {"pages": pages_text}
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Example usage
pdf_path = 'src/backend/dataloader/data/cricket.pdf'  # Replace with the path to your PDF file
json_path = 'src/backend/dataloader/data/cricket.json'     # Replace with the desired JSON output file name

# Extract text from PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Save the extracted text as a list of paragraphs to a JSON file
save_text_to_json(extracted_text, json_path)



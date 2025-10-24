import subprocess
import os
import json
from datetime import datetime
import pdfplumber                             # For Reading Text fron Each Pages.
from datetime import datetime




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_scrapy_spider(url: str) -> dict:
    try:
        if not url:
            return {"status": "fail", "message": "No URL provided"}
        cmd = f"scrapy crawl generic -a url={url}"
        subprocess.run(cmd, shell=True, cwd=os.path.join(BASE_DIR, "Tmy_scrapper"))
        return {"status": "success", "message": f"Data scraped from {url}"}

    except Exception as e:
        return {"status": "fail", "message": str(e)}





def extract_data_from_pdf(pdf_file):
    """
    Extracts text from each page of a PDF and returns structured JSON data.
    """

    try:
        # Create folder for extracted PDF data if not exists
        output_dir = os.path.join(os.getcwd(), "pdf_extracted_data")
        os.makedirs(output_dir, exist_ok=True)

        # Generate unique JSON file name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(output_dir, f"extracted_{timestamp}.json")

        extracted_pages = []

        # Open and read PDF file
        with pdfplumber.open(pdf_file) as pdf:
            for i, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if text:
                    extracted_pages.append({
                        "page": i,
                        "content": text.strip()
                    })

        # Save data to JSON file
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(extracted_pages, f, ensure_ascii=False, indent=4)

        # Return data directly to frontend
        return extracted_pages

    except Exception as e:
        raise Exception(f"Error extracting PDF data: {str(e)}")
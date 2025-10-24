from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import run_scrapy_spider  
from .utils import extract_data_from_pdf  



def index(request):
    return render(request, "index.html")


@csrf_exempt
def scrape_url(request):                                           # WebScrapping
    if request.method == "POST":
        data = json.loads(request.body)
        url = data.get("url")
        result = run_scrapy_spider(url)
        return JsonResponse(result, status=200 if result["status"] == "success" else 500)

    return JsonResponse({"status": "fail", "message": "Invalid request method"}, status=405)




@csrf_exempt 
def extract_pdf(request):                                           # Pdf Extractrion.
    if request.method == "POST" and request.FILES.get("pdf"):
        try:
            pdf_file = request.FILES["pdf"]
            import pdfplumber, json

            # ✅ Read PDF content
            with pdfplumber.open(pdf_file) as pdf:
                text_data = [page.extract_text() for page in pdf.pages if page.extract_text()]

            # ✅ Save extracted data into JSON file
            import os, datetime
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            folder = os.path.join(BASE_DIR, "Tmy_scrapper")
            os.makedirs(folder, exist_ok=True)
            filename = f"pdf_data_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json"
            filepath = os.path.join(folder, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(text_data, f, ensure_ascii=False, indent=4)

            return JsonResponse({
                "status": "success",
                "message": "PDF data extracted successfully",
                "data": text_data
            })

        except Exception as e:
            return JsonResponse({"status": "fail", "message": str(e)})

    return JsonResponse({"status": "fail", "message": "No PDF file received"}, status=400)
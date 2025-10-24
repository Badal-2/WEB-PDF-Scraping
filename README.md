⚙️ Features

✅ Web scraping using Scrapy
✅ PDF text extraction using pdfplumber
✅ Automatic JSON export
✅ Django backend API endpoints
✅ Simple UI (index.html) for uploads & scraping

🧩 Folder Structure
smart-data-extractor/
│
├── manage.py
├── requirements.txt
├── Tmy_scrapper/                 # Scrapy spider folder
│   ├── spiders/
│   │   └── generic.py            # Main spider for URL scraping
│   └── __init__.py
│
├── main_app/                     # Django app folder
│   ├── views.py                  # Handles requests & API routes
│   ├── utils.py                  # Core scraping + PDF functions
│   ├── templates/
│   │   └── index.html            # Frontend UI
│   └── __init__.py
│
├── pdf_extracted_data/           # Auto-created for storing PDF JSON files
└── scrapy_output/                # Auto-created for scraped data

💻 How to Run It
1️⃣ Clone the repo
git clone https://github.com/YOUR_USERNAME/smart-data-extractor.git
cd smart-data-extractor

2️⃣ Create & activate virtual environment
python -m venv env
source env/bin/activate     # (Linux/Mac)
env\Scripts\activate        # (Windows)

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations & start Django server
python manage.py runserver

5️⃣ Access the UI

Open: http://127.0.0.1:8000/

🌐 API Endpoints
▶️ Web Scraping

POST /scrape_url/



🧠 Tech Stack

Python 3.10+
Django 5+
Scrapy
pdfplumber
HTML + JS (Frontend)

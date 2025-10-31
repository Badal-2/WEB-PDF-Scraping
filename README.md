
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


3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations & start Django server
python manage.py runserver

5️⃣ Access the UI

Open: http://127.0.0.1:8000/

🌐 API Endpoints
▶️ Web Scraping


🧠 Tech Stack

Python 3.10+
Django 5+
Scrapy
pdfplumber
HTML + JS (Frontend)

<img width="1919" height="1016" alt="image" src="https://github.com/user-attachments/assets/37b1dda1-20d2-47a6-8840-99beceb06c75" />
<img width="1919" height="1076" alt="image" src="https://github.com/user-attachments/assets/38b7c3c8-5a16-4862-8229-db3d7084db90" />
<img width="1919" height="953" alt="image" src="https://github.com/user-attachments/assets/a9f04cb6-6e70-4c60-a20d-9faa574b9397" />




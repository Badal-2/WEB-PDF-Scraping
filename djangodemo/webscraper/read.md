__Tmy_scrapper/__       ← Scrapy project (actual scraper)



__utils.py__

Ye file kabel logic aur helper functions ke liye hoti hai.
Matlab: jo kaam backend me core logic ke liye hota hai  Generate a Response. 

LLM call (Gemini)
Text-to-speech (gTTS)
Speech-to-text (VOSK)




__views.py__

Ye  file kabel request/response handle karne ke liye hoti hai.
whatever response will come from backend then views.py file will share response
Matlab: frontend se jo data aata hai (POST/GET), usko receive karna, utils ke functions call karna, aur jo response return hota hai __Utils.py__ file she use user ko show karna.


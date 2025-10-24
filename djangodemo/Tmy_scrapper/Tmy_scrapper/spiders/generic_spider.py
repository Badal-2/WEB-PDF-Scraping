import scrapy
import json
import os
import datetime

class GenericSpider(scrapy.Spider):
    name = "generic"

    # We'll pass URL dynamically from Django
    start_urls = []
    allowed_domains = []

    def __init__(self, url=None, **kwargs):
        super().__init__(**kwargs)
        if url:
            self.start_urls = [url]
            self.allowed_domains = [url.split("/")[2]]  # extract domain
        # Unique JSON filename per scrape
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.output_file = os.path.join("Tmy_scrapper", f"scraped_data_{timestamp}.json")
        self.items_list = []

    def parse(self, response):
        # Extract main text content
        for sel in response.css("p, h1, h2, h3, h4, h5, h6, span, div"):
            text = " ".join(sel.css("::text").getall()).strip()
            if text:
                self.items_list.append(text)

        # Optional: follow all absolute links (pagination)
        for next_page in response.css("a::attr(href)").getall():
            if next_page.startswith("http"):
                yield response.follow(next_page, self.parse)

    def closed(self, reason):
        # Save scraped data to JSON file
        os.makedirs("Tmy_scrapper", exist_ok=True)
        with open(self.output_file, "w", encoding="utf-8") as f:
            json.dump(self.items_list, f, ensure_ascii=False, indent=4)

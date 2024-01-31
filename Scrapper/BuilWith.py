import requests; from bs4 import BeautifulSoup
from typing import List, Dict, Tuple

class Model():
    def __init__(self, url) -> None:
        self.url = url

    def runParse(self, objectRequest: requests) -> Tuple[bool, str]:
        """Initial parse of the website."""
        soup = BeautifulSoup(objectRequest.text, 'html.parser')
        findMain = soup.find("form", attrs={"method": "post", "id": "mainForm", "novalidate": ""})
        findCardBody = findMain.find("div", attrs={"class": "col-md-8 pr-1 pl-4"})
        return findCardBody

    def getContent(self, content: str) -> List[Dict[str, str]]:
        """Extract the content of the page from the soup object."""
        nSoup = BeautifulSoup(content.prettify(), 'html.parser')
        listContents = nSoup.find_all("div", attrs={"class": "card-body pb-0"})
        return listContents

    def formatContents(self, contents: List[str]) -> Dict[str, str]:
        for content in contents:
            nSoup = BeautifulSoup(content.prettify(), 'html.parser')
            _title = nSoup.find("h6", attrs={"class": "card-title text-secondary"})
            _title = _title.get_text(strip=True)
            self.content[_title] = {}
            listOfContents = [a.get_text(strip=True) for a in nSoup.find_all("a", attrs={"class": "text-dark"})]
            self.content[_title] = listOfContents

    def run(self) -> Dict[str, str or bool]:
        """Run the scraper."""
        r1 = requests.get(f"https://builtwith.com/?{self.url}")
        if r1.ok:
            self.content = dict()
            parse = self.runParse(r1)
            gContent = self.getContent(parse)
            self.formatContents(gContent)
            return {"sucess": True, "content": self.content}
        else:
            return {"sucess": False, "content": "Error: (The remote name could not be resolved)"}
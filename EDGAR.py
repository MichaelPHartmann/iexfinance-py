import requests
import BeautifulSoup as bs
https://www.sec.gov/Archives/edgar/data/0000320193/index.json
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320193&type=10-K&dateb=&owner=exclude&count=40&output=atom
https://www.sec.gov/Archives/edgar/data/0000320193/000032019319000119/index.json


EDGAR_BASE_TXT = 'https://www.sec.gov/Archives/edgar/data/{CIK}/{ACCESSION}.txt'
EDGAR_BASE_JSON? = 'https://www.sec.gov/Archives/edgar/data/{CIK}/{ACCESSION}/index.json'

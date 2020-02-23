import os
import re
from bs4 import BeautifulSoup, SoupStrainer

def egdar_find_html(string):
    ## Finds html tags and returns whether it is the start or end of the block
    if re.search('<HTML>', string) or re.search('<html>', string):
        return 'Start'
    if re.search('</HTML>', string) or re.search('</html>', string):
        return 'End'

def edgar_strip_to_html(file, newfile):
    ## Strips a document to just the html elements
    with open(file, 'r+') as f, open(newfile, 'a') as nf:
        transfer = False
        lines = f.readlines()
        for line in lines:
            status = egdar_find_html(line)
            if status == 'Start':
                transfer = True
            elif status == 'End':
                transfer = False
                nf.write(line)

            if transfer == True:
                nf.write(line)

def raw_to_text(self):
    ## Converts a raw txt SEC submission to a text-only document
    filein = self.file
    # Open the original file and soupify it
    with open(filein, 'r') as f:
        filein = filein.strip('.txt')
        soup = BeautifulSoup(f, features="html.parser")
        result = soup.get_text()
    # Open the temporary file and writeout the pretty soup
    tempfile = f"{filein}_temp.txt"
    with open(tempfile, 'w+') as tf:
        tf.write(result)
    # Open the temporary file after it has been written to
    with open(tempfile, 'r') as tf:
        lines = tf.readlines()
        # Open the final file and writeout nonblank lines
        newfile = f"{filein}_textonly.txt"
        with open(newfile, "a") as nf:
            for line in lines:
                if line.strip():
                    nf.write(line)
    # Remove the temporary file
    os.remove(tempfile)
    return newfile

def download_report_file(accessions):
    for accession in accessions:
        fixed_accession = accession.replace("-","")
        URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/{accession}.txt"
        # Stream site to local file
        response = requests.get(URL, stream=True)
        filename = f'{self.ticker}_{accession}.txt'
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=512):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

def document_type_parse(document):
    ## Allows one to pass in a miss-typed document tag and rectifies it
    ten_K = ["10-K","10-k","10K","10k"]
    ten_Q = ["10-Q","10-q","10Q","10q"]
    if document in ten_K:
        pass
    if document in ten_Q:
        pass

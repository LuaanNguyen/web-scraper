# Modal run scrape.py --url http://example.com
# Modal automatically parse the url parameter into main(url)
import re 
import sys 
import urllib.request 
import modal 

app = modal.App(name="link-scraper") #create an app called link-scrapper

@app.function()
def get_links(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf8")
    
    links = [] 
    
    for match in re.finditer('href="(.*?)"', html): # find all strings that match the HTML hypterlink pattern
        links.append(match.group(1))
        
    return links 


@app.local_entrypoint()
def main(url):
    links = get_links.remote(url)
    print(links)


   
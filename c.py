from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.nate.com/')
source = response.text
#print(source)

soup = BeautifulSoup(source, 'html.parser')
#results = soup.select("#olLiveIssueKeyword > li:nth-child(1)") #1 or 6번
results = soup.select("#olLiveIssueKeyword > li") #<li>의 list객체
#print(results)

for li in results:
    span = li.select_one('.txt_rank')
    #print(span)

    if span:
        print(span.get_text(strip=True))
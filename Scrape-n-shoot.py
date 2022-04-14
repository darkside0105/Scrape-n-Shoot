import requests, argparse, time, random, os, tldextract, re
from bs4 import BeautifulSoup

def domain_search():
    file = open('./data/beautify-companies.txt','r')
    param_list = []
    param_list = file.readlines()
    file.close()
    for i in param_list:
        param = i.strip("\n")
        resp1 = requests.get("https://www.google.com/search",\
            params = {"q":param}, \
            headers= {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}\
            )
        html = BeautifulSoup(resp1.text, 'html.parser')
        out = html.find('cite',attrs={'role':'text'}).text
        url = re.sub(r"\s+.*$","",out)
        domain = tldextract.extract(f'{url}')
        file = open('./Results/linkedin-domains.txt','a+')
        file.write(".".join(domain[1:])+"\n")
        file.close()


def beautify_text():    
    cmd2 = 'awk "NF" ./data/extracted-companies.txt | sed -r s/\^\\\s+//g | sort -u |tee ./data/beautify-companies.txt'
    os.system(cmd2)


def linkedin_resp_parse(html_resp):
    html = BeautifulSoup(html_resp, 'html.parser')
    comp_tags = html.find_all('a', attrs={'class':'hidden-nested-link'})
    file = open(f'./data/extracted-companies.txt','a+')
    for i in comp_tags:
        comp_name = i.text.strip(" ")
        # print(comp_name)
        file.write(comp_name)
    file.close()
    

def get_response(keyword,country):
    user_agents = ["Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15", \
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.3; rv:99.0) Gecko/20100101 Firefox/99.0", \
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.24) Gecko/20111109 CentOS/3.6.24-3.el6.centos Firefox/47.0", \
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        ]
    head={"User-Agent": random.choice(user_agents)}
    req = requests.Session()
    resp = req.get("https://www.linkedin.com/jobs/search", \
        params = {"keywords":keyword,"location":country,"geoId":"","trk":"homepage-jobseeker_jobs-search-bar_search-submit"},\
        headers=head\
        )
    req.cookies.update(resp.cookies)
    # file = open(f'./data/Home-RESP.html','w+')
    # file.write(resp.text)
    # file.close()
    linkedin_resp_parse(resp.text)
    print(resp.status_code,resp.headers['Content-Length'])

    for i in range(25,1000,25):
        resp = req.get("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search", \
            params = {"keywords":keyword,"location":country,"geoId":"","trk":"homepage-jobseeker_jobs-search-bar_search-submit","start":i},\
            headers=head\
            )
        # file = open(f'./data/{i}-RESP.html','w+')
        # file.write(resp.text)
        # file.close()
        linkedin_resp_parse(resp.text)
        time.sleep(2)
    beautify_text()
    domain_search()
    
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keyword",  help="Specify any Job Keyword to search", required=True)
    parser.add_argument("-c", "--country",  help="Specify any Country to search for Job", required=True)
    args = parser.parse_args()
    get_response(f"{args.keyword}",f"{args.country}")

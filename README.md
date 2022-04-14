# Scrape-n-Shoot
A Repo for scraping Social media for the Job profiles.

### Install/Build Dependencies:
1. Make sure Your system is running python3 with below command.
```sh
python -V
```

2. Install Project dependencies using pip using below command.
```sh
pip3 install -r requirements.txt
```

3. Run Scrape-n-shoot.py file.
---
### Usage
```sh
python3 Scrape-n-shoot.py -k JOB-DESIGNATION -c JOB-LOCATION
```
**Help**

```sh
python3 Scrape-n-shoot.py [-h|--help]
```

**output**

```yaml
usage: Scrape-n-shoot.py [-h] -k KEYWORD -c COUNTRY
optional arguments:
 -h, --help            show this help message and exit
 -k KEYWORD, --keyword KEYWORD
                        Specify any Job Keyword to search
   -c COUNTRY, --country COUNTRY
                        Specify any Country to search for Job
```
#### Examples:
```sh 
python3 Scrape-n-shoot.py -k "Data Scientist" -c "Hydrabad, Telangana, India"
```
---
### Results
-  Check data folder for Company Names collected from Linkedin.
-  Check Results folder for domains scraped from google using the company names.

**Note:** Linux System is must for the program to run
---
### TODO's:

- [x] Scrape single domains from google using company name
- [ ] Scrape Multiple domains from google with different tlds.
- [ ] Verify the Scraped domain belongs to that respective company/organization.
- [ ] Find a way to extract domains with all tld's which belongs to company/organization.

   

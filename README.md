# google-scholar-report
<center><img src="https://raw.githubusercontent.com/colav/colav.github.io/master/img/Logo.png"/></center>

# google-scholar-report
Google scholar Automation report Tool

# Description
Package allows to download data from google scholar profiles

# Installation

## Package
`pip install google-scholar-report`

# Usage
## commanline 
From comman line, this tool have three main forms of use: generic, authenticated and admin; which difer in amount and cuality of metadata results.

For the firts option of use (generic), issue: 

```bash
python3 main.py "url_for_the_google_scholar_profile"
```
The above option return one xlsx file report in the current working directory with the following metadata:

'title', 'author', 'journal', 'volume', 'number','pages', 'year', 'cite_id', 'cites', 'TitleU'.

If you want the output in csv or json format agregate the bellow flag and the desire ouput format, for instance:

```bash
python3 main.py "url_for_the_google_scholar_profile" --output csv
```

For the second option of use (user authenticate):

```bash
python3 main.py "url_for_the_google_scholar_profile" --email <email> --password <password>
```

This return one xlsx file report in the current working directory with the following metadata:

'cite_id', 'cites', 'publisher', 'year', 'pages', 'number', 'volume', 'journal', 'author', 'title','ENTRYTYPE', 'ID', 'school', 'booktitle', 'organization', 'note','month', 'institution'
 
 Finally, for admin mode, issue: 
 
 ```bash
python3 main.py "url_for_the_google_scholar_profile" --email <email> --password <password> --admin
```

This return by default an xlsx file with the same metadata that option two plus one fiedl 'bibtex'.

In general this commanline tool have the following form:

```bash
python3 main.py "url_for_the_google_scholar_profile" --email <user_email> --password <password> --output <format> --admin
```

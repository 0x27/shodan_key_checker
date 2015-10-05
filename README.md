# Shodan API Key Checker
This is a quick script written for sorting and categorizing Shodan API keys acquired via scraping the internet.  
I wrote it because I kept finding people leaving their API keys unprotected all over the shop, and frankly, sometimes I need a Shodan API key quickly and can't be arsed finding my own one.

Anyways, this script breaks it down into "paid accounts" and "non paid accounts" after its done checking for validity of keys. You could also check which have telnet enabled or whatnot depending on your usecase.

You can find peoples API keys... All over the net, yo.

## Use
Just give it a text file of possible API keys, one API key per line, and let her rip.

## Requirements
You will require the [shodan](https://github.com/achillean/shodan-python) module for this.  
```
pip install shodan
```

## Licence
[Licenced under the WTFPL](http://wtfpl.net)

## Beer
All beer donations can go to 1F3sPdKSEL9mM8LBnymGG8Dv3QCPDSRYeh ;)

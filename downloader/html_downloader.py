__author__ = 'cshao'


import urllib.request


def download_sample_html():
    with urllib.request.urlopen("http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=chapel-hill&r=D&s=scolaber&useShortTitles=true") as response:
        html = response.read()
    return html


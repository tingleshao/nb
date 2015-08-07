__author__ = 'cshao'


def extract_time(html):
    html = html.decode('utf-8')
    for item in html.split('''</direction>'''):
        if '''<direction title="To Eastowne">''' in item:
            if (item[item.find('''<direction title="To Eastowne">''')+len('''<direction title="To Eastowne">'''):]).strip():
                return (item[item.find('''<direction title="To Eastowne">''')+len('''<direction title="To Eastowne">'''):])

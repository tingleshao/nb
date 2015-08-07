__author__ = 'cshao'


def format(xml):
    xml_rows = [row for row in xml.split("\n") if row.strip()]
    time_list = []
    for row in xml_rows:
        time_list.append(row.split(" ")[5].split('="')[1][:-1] + " mins")
    return time_list




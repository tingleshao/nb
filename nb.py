__author__ = 'cshao'


from downloader.html_downloader import download_sample_html
from parser.extractor import extract_time
from parser.formatter import format


def main():
    html = download_sample_html()
    values = extract_time(html)
    with open("test_html", 'w') as html_file:
        html_file.write(html.decode('utf-8'))
    print("Chapel Hill Transit, Route D \nAT S Columbia @ Fraternity Court, To Smith Level and BPW Club")
    for row in format(values):
        print(row)


if __name__ == "__main__":
    main()




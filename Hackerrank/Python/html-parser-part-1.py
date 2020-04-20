# from parser import HTMLParser
# import parser
from html.parser import HTMLParser

n = 2
samples = ["<html><head><title>HTML Parser - I</title></head>",
           "<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>"]

# for i in range(n):
#     print(samples[i])


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)

    def handle_endtag(self, tag):
        print("End :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


parser = MyHTMLParser()

code = ''
for sample in samples:
    code += sample
parser.feed(code)

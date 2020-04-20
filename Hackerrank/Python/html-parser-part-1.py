# https://docs.python.org/3.8/library/html.parser.html?highlight=htmlparser#html.parser.HTMLParser

# n = 2
# samples = ["<html><head><title>HTML Parser - I</title></head>",
#            "<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>"]

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    # qingchen's solution
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for ele in attrs:
            print('->', ele[0], '>', ele[1])

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for ele in attrs:
            print('->', ele[0], '>', ele[1])


parser = MyHTMLParser()

for i in range(int(input())):
    parser.feed(input())


# for sample in samples:
#     parser.feed(sample)

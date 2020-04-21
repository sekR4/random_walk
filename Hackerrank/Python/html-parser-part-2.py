from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print("Data:", data)

    def handle_comment(self, data):
        print("Comment:", data)


html = ""
# for i in range(int(input())):
#     html += input().rstrip()
#     html += '\n'

lines = ["<!--[if IE 9]>IE9-specific content",
         "<![endif]-->",
         "<div> Welcome to HackerRank</div>",
         "<!--[if IE 9]>IE9-specific content<![endif]-->"]

for line in lines:
    html += line.rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

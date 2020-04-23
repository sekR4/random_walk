from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if len(data) > 1:
            print(">>> Data", data, sep='\n')

    def handle_comment(self, data):
        if data.count('\n') > 0:
            print(">>> Multi-line Comment", data, sep='\n')
        if data.count('\n') == 0:
            print(">>> Single-line Comment", data, sep='\n')


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

# print(html.replace('\n', ''))

parser = MyHTMLParser()
parser.feed(html)
parser.close()

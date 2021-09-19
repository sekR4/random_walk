from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        # print("some attributes:", attrs)
        if len(attrs) > 0:
            for i in attrs:
                # print(i)
                print(f"-> {i[0]} > {i[1]}")


lines = [
    '<head>',
    '<title>HTML</title>',
    '</head>',
    '<object type="application/x-flash" ',
    ' data="your-file.swf" ',
    ' width="0" height="0">',
    ' <!-- <param name="movie" value="your-file.swf" /> -->',
    ' <param name="quality" value="high"/>',
    '</object>']


html = ''
# testing
for line in lines:
    html += line.rstrip()
    html += '\n'

# submisson
# for line in range(int(input())):
#     html += input().rstrip()
#     html += '\n'

# print('Input :', html, sep='\n')

# parser = MyHTMLParser()
#
# parser.feed(html)

MyHTMLParser().feed(html)

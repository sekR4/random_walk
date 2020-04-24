# https://docs.python.org/3/library/xml.etree.elementtree.html
import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    # score = 0
    # score += len(node.attrib)
    # for child in node:
    #     score += len(child.attrib)
    # return score

    # thx to asakurajano
    return sum([len(elem.items()) for elem in node.iter()])
    # return etree.tostring(node).count(b'=')


if __name__ == '__main__':
    # submission
    # sys.stdin.readline()
    # xml = sys.stdin.read()

    # testcase 0 (passed)
    # lines = [
    #     "<feed xml:lang='en'>",
    #     "    <title>HackerRank</title>",
    #     "    <subtitle lang='en'>Programming challenges</subtitle>",
    #     "    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>",
    #     "    <updated>2013-12-25T12:00:00</updated>",
    #     "</feed>"]

    # testcase 1
    lines = [
        "<feed xml:lang='en'>",
        "  <title>HackerRank</title>",
        "  <subtitle lang='en'>Programming challenges</subtitle>",
        "  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>",
        "  <updated>2013-12-25T12:00:00</updated>",
        "  <entry>",
        "  	<author gender='male'>Harsh</author>",
        "    <question type='hard'>XML 1</question>",
        "    <description type='text'>This is related to XML parsing</description>",
        "  </entry>",
        "</feed>"
    ]

    xml = ''
    for line in lines:
        xml += line.rstrip()
        xml += '\n'

    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

import qlogger as ql
ql.start_logging(__file__)


import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    txt = ''
    for element in word_list:
        print(element)
    return txt

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


def wrap(string, max_width):
    return "\n".join([string[i:i + max_width] for i in range(0, len(string), max_width)])

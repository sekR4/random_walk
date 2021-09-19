import email.utils
import re


# cases = [
#     'dheeraj <dheeraj-234@gmail.com>',
#     'harsh <harsh_1234@rediff.in>',
#     'kumal <kunal_shin@iop.az>',
#     'mattp <matt23@@india.in>',
#     'harsh <.harsh_1234@rediff.in>',
#     'harsh <-harsh_1234@rediff.in>']


# for i in range(len(cases)):
for i in range(int(input())):
    usr, mail = email.utils.parseaddr(input())
    m = re.match(r'[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$', mail)
    if m:
        print(email.utils.formataddr((usr, mail)))
# 	^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
# print('@'.isalnum())

# https://emailregex.com/
# oracle:
# SELECT email
# FROM table_name
# WHERE REGEXP_LIKE (email, '[A-Z0-9._%-]+@[A-Z0-9._%-]+\.[A-Z]{2,4}');

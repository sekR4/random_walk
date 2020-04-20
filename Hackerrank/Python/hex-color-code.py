import re, sys
print(*re.findall("(?<!\n)#(?i:[\\da-f]{3}){1,2}", sys.stdin.read()), sep='\n')

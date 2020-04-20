import re
regex_pattern = r"\.|\,"  # Do not delete 'r'.

print("\n".join(re.split(regex_pattern, '100,000,000.000')))

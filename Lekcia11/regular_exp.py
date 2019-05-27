import re

data = "17, 98%,A Hard Day's Night (1964),102"

najdene = re.match(
    r"^(\d+),(\s\d+)%,(.*)\s\((\d+)\),(\d+)$",
    data
)

print(najdene.group(1))

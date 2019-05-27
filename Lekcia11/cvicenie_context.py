import re


class Splitter:
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        return self.text

    def __exit__(self, *args):
        res = re.match(
            r"^([\w\s]*)--(.*)--([\w\s]*).$",
            self.text
        )
        print(
            [
                res.group(1).strip(),
                res.group(2).strip(),
                res.group(3).strip()
            ]
        )


text = "There should be one-- and preferably only one --obvious way to do it."
# vytvor objekt splitter, a do premennej za AS
# vloz hodnotu, ktoru vrati metoda __enter__()
#
# with Splitter(text) as lopata:
#     print(f"XY: {lopata}")


lopata = Splitter(text)
print(lopata.__exit__())
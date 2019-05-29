import re


class MovieContext():
    def __init__(self, movies_file):
        self.fh = open(movies_file, "r")

    def __enter__(self):
        next(self.fh)  # ignore header (zavolame next() na iterable object, cim dostaneme dalsi prvok)
        re_ = re.compile(r"^(\d+),\s(\d+)%,(.*)\s\((\d+)\),(\d+)$")
        result = []
        for line in self.fh:
            res = re.match(re_, line)
            result.append(
                (
                    res.group(1),
                    res.group(2),
                    res.group(3),
                    res.group(4),
                    res.group(5)
                )
            )
        self.newest = max(result, key=lambda x: int(x[3]))
        self.oldest = min(result, key=lambda x: int(x[3]))
        self.reviews = max(result, key=lambda x: int(x[4]))
        return self.newest, self.oldest, self.reviews

    def __exit__(self, *args):
        with open("stats.csv", "w") as fp:
            fp.write("typ,nazov,rok,reviews\n")
            fp.write(f"najstarsi,{self.oldest[2]},{self.oldest[3]},{self.oldest[4]}\n")
            fp.write(f"najnovsi,{self.newest[2]},{self.newest[3]},{self.newest[4]}\n")
            fp.write(
                f"najrecenzovanejsi,{self.reviews[2]},{self.reviews[3]},{self.reviews[4]}"
            )
            fp.close()
        self.fh.close()


with MovieContext("movies.csv") as movies:
    print(f"Najstarsi film: {' '.join(movies[1][2:-1])}")
    print(f"Najnovsi film: {' '.join(movies[0][2:-1])}")
    print(f"Najviac recenzovany film: {' '.join(movies[2][2:])}")



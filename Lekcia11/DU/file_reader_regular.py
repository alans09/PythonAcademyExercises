import re

class MovieContext():
    def __init__(self, movies_file):
        self.fh = open(movies_file, "r")

    def __enter__(self):
        next(self.fh) #  ignore header
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
        return result

    def __exit__(self, *args):
        fp = open("stats.csv", "w")
        fp.write("typ,nazov,rok,reviews\n")
        fp.write(f"Najstarsi,{movies[oldest[0]][2]},{movies[oldest[0]][3]},{movies[oldest[0]][4]}\n")
        fp.write(f"Najnovsi,{movies[newest[0]][2]},{movies[newest[0]][3]},{movies[newest[0]][4]}\n")
        fp.write(
            f"Najrecenzovanejsi,{movies[most_reviews[0]][2]},{movies[most_reviews[0]][3]},{movies[most_reviews[0]][4]}"
        )
        fp.close()


# format   <premenna> = [<id>, <rok>]
oldest = [0, 3000]      # definoval som si oldest ako pole, kde 0 prvok je ID filmu, 1 prvok je rok
# format   <premenna> = [<id>, <rok>]
newest = [0, 1111]      # detdo pre newest, iba preto, aby som nemal zbytocne viac premennych
# format   <premenna> = [<id>, <reviews>]
most_reviews = [0, 0]   # detto pre reviews, da sa pouzit aj dictionary


with MovieContext("movies.csv") as movies:
    for k, movie in enumerate(movies):
        if int(movie[3]) < int(oldest[1]):
            oldest[1] = int(movie[3])
            oldest[0] = k
        if int(movie[3]) > int(newest[1]):
            newest[1] = int(movie[3])
            newest[0] = k
        if int(movie[4]) > most_reviews[1]:
            most_reviews[1] = int(movie[4])
            most_reviews[0] = k
    print(f"Najstarsi film: {' '.join(movies[oldest[0]][2:-1])}")
    print(f"Najnovsi film: {' '.join(movies[newest[0]][2:-1])}")
    print(f"Najviac recenzovany film: {' '.join(movies[most_reviews[0]][2:-1])}")

# fp = open("stats.csv", "w")
# fp.write("typ,nazov,rok,reviews\n")
# fp.write(f"Najstarsi,{movies[oldest[0]][2]},{movies[oldest[0]][3]},{movies[oldest[0]][4]}\n")
# fp.write(f"Najnovsi,{movies[newest[0]][2]},{movies[newest[0]][3]},{movies[newest[0]][4]}\n")
# fp.write(f"Najrecenzovanejsi,{movies[most_reviews[0]][2]},{movies[most_reviews[0]][3]},{movies[most_reviews[0]][4]}")
# fp.close()
#


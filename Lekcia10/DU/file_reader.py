import re


fp = open("movies.csv", "r")
line_nr_oldest = 1
line_nr_newest = 1
year_oldest = 3000
year_newest = 1111
line_nr_reviews_count = 1
most_reviews = None
movie_name_oldest = None
movie_name_newest = None
movie_name_reviews = None
reviews_oldest = 1
reviews_newest = 1
newest = None
oldest = None

re_ = re.compile(r"^(\d+,)(\s\d+%,)(.*)(\s\(\d+\))(,\d+)$")

for line in fp:
    data = line.split(',')
    # ak splitneme na , tak predposledny stlpec vzdy bude rok
    # ideme robit obe veci naraz
    # [-2] je koniec nazvu s rokom
    # [0] je poradove cislo co nas zaujma, ak najdeme najstarsi a najnovsi
    # [-2][-5:-1] je rok bez ()
    # [-1] je pocet recenzii
    try:
        help = re.match(re_, line)
        year = int(data[-2][-5:-1])
        if int(data[-2][-5:-1]) > year_newest:
            year_newest = year
            newest = line
            movie_name_newest = help.group(3)
            line_nr_newest = int(data[0])
            reviews_newest = data[-1]
        if int(data[-2][-5:-1]) < year_oldest:
            year_oldest = year
            oldest = line
            movie_name_oldest = help.group(3)
            line_nr_oldest = int(data[0])
            reviews_oldest = data[-1]
        if int(data[-1]) > line_nr_reviews_count:
            line_nr_reviews_count = int(data[-1])
            movie_name_reviews = help.group(3)
            most_reviews = line
    except ValueError:
        # prvy riadok je hlavicka, tu nechceme.. odrezeme ju.. tj. ak dostaneme Value error
        # value error nam padne na riadku year = int(data[-2][-5:-1]) (lebo text nema int() )
        # proste len preskocime chybu
        pass
fp.close()

fp = open("stats.csv", "w")
fp.write("typ,nazov,rok,reviews\n")
fp.write(f"Najstarsi,{movie_name_oldest},{year_oldest},{reviews_oldest}")
fp.write(f"Najnovsi,{movie_name_newest},{year_newest},{reviews_newest}")
fp.write(f"Najviac reviews,{movie_name_reviews},{year_newest},{line_nr_reviews_count}")
fp.close()


print(f"Najstarsi film:\t\t{oldest.strip()}\nNajmladsi film:\t\t{newest.strip()}")
print(f"Najviac recenzii:\t{most_reviews.strip()}")




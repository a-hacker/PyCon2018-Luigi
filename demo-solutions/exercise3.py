import luigi

class SubDicts:
    substitutions1288 = {
        "witnesses": "these dudes I know",
        "allegedly": "kinda probably",
        "new study": "tumblr post",
        "rebuild": "avenge",
        "space": "spaaace",
        "google glass": "virtual boy",
        "smartphone": "pokedex",
        "electric": "atomic",
        "senator": "elf-lord",
        "car": "cat",
        "election": "eating contest",
        "congressional leaders": "river spirits",
        "homeland security": "homestar runner",
        "could not be reached for comment": "is guilty and everyone knows it"
    }

    substitutions1625 = {
        "debate": "dance-off",
        "self driving": "uncontrollably swerving",
        "poll": "psychic reading",
        "candidate": "airbender",
        "drone": "dog",
        "vows to": "probably won't",
        "at large": "very large",
        "successfully": "suddenly",
        "expands": "physically expands",
        "first-degree": "friggin' awful",
        "second-degree": "friggin' awful",
        "third-degree": "friggin' awful",
        "an unknown number": "like hundreds",
        "front runner": "blade runner",
        "global": "spherical",
        "years": "minutes",
        "minutes": "years",
        "no indication": "lots of signs",
        "urged restraint by": "drunkenly egged on",
        "horsepower": "tons of horsemeat"
    }


def get_input_file():
    return "/usr/local/luigi/datafiles/example1.txt"


class ArticleText(luigi.ExternalTask):
    def output(self):
        return get_input_file()


class SubstitutionTask(luigi.Task):

    subs = luigi.IntParameter(default=1288)

    def requires(self):
        return ArticleText()

    def get_substitution_dict(self):
        return getattr(SubDicts(), "substitutions{}".format(self.subs))

    def run(self):
        with self.input().open('r') as infile, self.output().open('w') as outfile:
            text = infile.read()
            for key, val in self.get_substitution_dict().items():
                text = text.replace(key, val)
            outfile.write(text)

    def output(self):
        return luigi.LocalTarget("/usr/local/luigi/output/subbed_example.txt")


if __name__ == '__main__':
    luigi.run()

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


def get_input_files():
    return ["/usr/local/luigi/datafiles/example{}.txt".format(i) for i in range(1, 3)]


class ArticleText(luigi.ExternalTask):
    file_name = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(str(self.file_name))


class SubstitutionTask(luigi.Task):
    subs = luigi.IntParameter(default=1288)

    def requires(self):
        return [ArticleText(fname) for fname in get_input_files()]

    def get_substitution_dict(self):
        return getattr(SubDicts(), "substitutions{}".format(self.subs))

    def run(self):
        out_text = ""
        for f in self.input():
            with f.open('r') as infile:
                text = infile.read()
                for key, val in self.get_substitution_dict().items():
                    text = text.replace(key, val)
                out_text += text
        with self.output().open('w') as outfile:
            outfile.write(out_text)

    def output(self):
        return luigi.LocalTarget("/usr/local/luigi/output/subbed_example.txt")


if __name__ == '__main__':
    luigi.run()

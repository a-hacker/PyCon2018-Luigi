import os

import luigi

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


def get_input_files():
    return ["/usr/local/luigi/datafiles/example{}.txt".format(i) for i in range(1, 4)]


def add_read_permission(file_path):
    os.chmod(file_path, 0o644)

# One of the files does not have the right permissions! Add an event handler to fix it.
# luigi Target classes have a path attribute to get the file location
#
# Tip: Remember to re-enable a failed task in the central scheduler


if __name__ == "__main__":
    luigi.run()
import random as _random

_adjectives = [
    "ace",
    "aloof",
    "amazing",
    "antsy",
    "astonishing",
    "astounding",
    "awesome",
    "badass",
    "bashful",
    "beautiful",
    "bossy",
    "breathtaking",
    "brilliant",
    "busy",
    ("candid", "k"),
    ("captivating", "k"),
    ("careless", "k"),
    ("cautious", "k"),
    ("charming", "ch"),
    ("cheeky", "ch"),
    ("chic", "sh"),
    ("churlish", "ch"),
    ("classy", "cl"),
    ("clever", "cl"),
    ("clumsy", "cl"),
    ("cool", "k"),
    ("crabby", "cr"),
    ("cranky", "cr"),
    ("creepy", "cr"),
    ("crucial", "cr"),
    ("cryptic", "cr"),
    "dandy",
    "dazzling",
    "defiant",
    "delightful",
    "delinquent",
    "devious",
    "digressive",
    "dire",
    "distracted",
    "distraught",
    "divine",
    "dogmatic",
    "droll",
    "dressy",
    "epic",
    "excellent",
    "exceptional",
    "exquisite",
    "extraordinary",
    "fabulous",
    "fantastic",
    "fine",
    "finest",
    "first-rate",
    ("flaky", "fl"),
    ("flamboyant", "fl"),
    ("flawless", "fl"),
    "foolish",
    "funkadelic",
    "galloping",
    ("geometric", "j"),
    "glorious",
    ("gnarly", "n"),
    "good",
    ("grand", "gr"),
    ("great", "gr"),
    ("groovy", "gr"),
    ("groundbreaking", "gr"),
    "handy",
    "harebrained",
    "heroic",
    "hungry",
    "hunky-dory",
    "impeccable",
    "impressive",
    "incredible",
    "jaded",
    "jaunty",
    "jealous",
    "kickass",
    "kooky",
    "klutzy",
    "kind-hearted",
    "kinetic",
    "laudable",
    "lazy",
    "learned",
    "legendary",
    "limber",
    "listless",
    "litigious",
    "livid",
    "long-winded",
    "lovely",
    "luminous",
    "magnificent",
    "majestic",
    "marvelous",
    "mathematical",
    "mind-blowing",
    "neat",
    "noisy",
    "oafish",
    "obligatory",
    "oblivious",
    "obvious",
    "off-putting",
    "oracular",
    "outstanding",
    "peachy",
    "pensive",
    "perfect",
    ("phenomenal", "f"),
    "pioneering",
    "polished",
    "posh",
    "premium",
    "priceless",
    "prime",
    "primo",
    ("quality", "kw"),
    ("queasy", "kw"),
    ("quirky", "kw"),
    ("quixotic", "kw"),
    ("quizzical", "kw"),
    ("quotable", "kw"),
    "radical",
    "rebellious",
    "remarkable",
    "riveting",
    "salty",
    "sassy",
    "saucy",
    ("scrappy", "sk"),
    "sensational",
    ("shabby", "sh"),
    ("shady", "sh"),
    ("shaven", "sh"),
    ("sheepish", "sh"),
    ("shining", "sh"),
    ("sketchy", "sk"),
    ("skeptical", "sk"),
    ("skittish", "sk"),
    ("snarky", "sn"),
    ("snazzy", "sn"),
    ("sneaky", "sn"),
    ("snide", "sn"),
    ("snobby", "sn"),
    ("snooty", "sn"),
    "solid",
    ("spacy", "sp"),
    ("spectacular", "sp"),
    ("splendid", "sp"),
    ("spooky", "sp"),
    ("stellar", "st"),
    ("stingy", "st"),
    ("striking", "st"),
    ("stubborn", "st"),
    ("stunning", "st"),
    ("stupendous", "st"),
    ("stylish", "st"),
    "sublime",
    "super",
    "super-duper",
    "superb",
    "superior",
    "supreme",
    ("swanky", "sw"),
    ("sweet", "sw"),
    ("swell", "sw"),
    ("swift", "sw"),
    "terrific",
    "testy",
    "tiptop",
    "top-notch",
    "transcendent",
    "tremendous",
    "ultimate",
    "unreal",
    "valiant",
    "versatile",
    "wacky",
    "wicked",
    "witty",
    "wonderful",
    "wondrous",
    "world-class",
    "yearnful",
    "yonder",
    "youthful",
    "zany",
    "zazzy",
    "zealous",
    "zesty",
]

_animals = [
    "aardvark",
    "albatross",
    "alligator",
    "alpaca",
    "ant",
    "anteater",
    "antelope",
    "ape",
    "armadillo",
    "baboon",
    "badger",
    "barracuda",
    "bat",
    "bear",
    "bee",
    "bison",
    "boar",
    "buffalo",
    "butterfly",
    ("camel", "k"),
    ("capybara", "k"),
    ("caribou", "k"),
    ("cassowary", "k"),
    ("cat", "k"),
    ("caterpillar", "k"),
    ("chameleon", "k"),
    ("cheetah", "ch"),
    ("chicken", "ch"),
    ("chimpanzee", "ch"),
    ("chinchilla", "ch"),
    ("chipmunk", "ch"),
    ("clam", "cl"),
    ("cobra", "k"),
    ("cockroach", "k"),
    ("cod", "k"),
    ("cormorant", "k"),
    ("coyote", "k"),
    ("crab", "cr"),
    ("crane", "cr"),
    ("crocodile", "cr"),
    ("crow", "cr"),
    "deer",
    "dinosaur",
    "dog",
    "dolphin",
    "donkey",
    "dove",
    "dragonfly",
    "duck",
    "eagle",
    "echidna",
    "eel",
    "elephant",
    "elk",
    "emu",
    "falcon",
    "ferret",
    "finch",
    "fish",
    ("flamingo", "fl"),
    ("fly", "fl"),
    "fox",
    "frog",
    "gazelle",
    ("gerbil", "j"),
    ("giraffe", "j"),
    ("gnat", "n"),
    "gnu",
    "goat",
    "goose",
    "goldfinch",
    "goldfish",
    "gorilla",
    ("grasshopper", "gr"),
    ("grouse", "gr"),
    "guinea-fowl",
    "guinea-pig",
    "gull",
    "hamster",
    "hare",
    "hawk",
    "hedgehog",
    "heron",
    "herring",
    "hippopotamus",
    "hornet",
    "horse",
    "human",
    "hummingbird",
    "hyena",
    "ibex",
    "ibis",
    "jackal",
    "jaguar",
    "jay",
    "jellyfish",
    "kangaroo",
    "kingfisher",
    "koala",
    "lark",
    "lemur",
    "leopard",
    "lion",
    "llama",
    "lobster",
    "locust",
    "louse",
    "magpie",
    "mallard",
    "manatee",
    "mantis",
    "marten",
    "meerkat",
    "mink",
    "mole",
    "mongoose",
    "monkey",
    "moose",
    "mouse",
    "mosquito",
    "mule",
    "narwhal",
    "newt",
    "nightingale",
    "octopus",
    "opossum",
    "ostrich",
    "otter",
    "owl",
    "ox",
    "oyster",
    "panther",
    "parrot",
    "partridge",
    "peafowl",
    "pelican",
    "penguin",
    ("pheasant", "f"),
    "pig",
    "pigeon",
    "polar-bear",
    "pony",
    "porcupine",
    "porpoise",
    "prairie-dog",
    ("quail", "kw"),
    "rabbit",
    "raccoon",
    "ram",
    "rat",
    "raven",
    "reindeer",
    "rhinoceros",
    "rook",
    "salamander",
    "salmon",
    "sand-dollar",
    "sandpiper",
    "sardine",
    ("scorpion", "sk"),
    "sea-lion",
    "sea-urchin",
    "seahorse",
    "seal",
    ("shark", "sh"),
    ("sheep", "sh"),
    ("shrew", "sh"),
    ("shrimp", "sh"),
    ("skunk", "sk"),
    ("snail", "sn"),
    ("snake", "sn"),
    ("sparrow", "sp"),
    ("spider", "sp"),
    ("spoonbill", "sp"),
    ("squid", "sk"),
    ("squirrel", "sk"),
    ("starling", "st"),
    ("stingray", "st"),
    ("stinkbug", "st"),
    ("stork", "st"),
    ("swallow", "sw"),
    ("swan", "sw"),
    "termite",
    "tiger",
    "toad",
    "trout",
    "turkey",
    "turtle",
    "viper",
    "vulture",
    "wallaby",
    "walrus",
    "wasp",
    "water-buffalo",
    "weasel",
    "whale",
    "wolf",
    "wolverine",
    "wombat",
    "woodcock",
    "woodpecker",
    "worm",
    ("wren", "r"),
    "yak",
    "zebra"
]

def generate_animal_id():
    _random.seed()

    animal = _random.choice(_animals)

    if type(animal) is tuple:
        animal, animal_initial = animal
    else:
        animal_initial = animal[0]

    def match(adjective):
        if type(adjective) is tuple:
            adjective, adjective_initial = adjective
        else:
            adjective_initial = adjective[0]

        return adjective_initial == animal_initial

    try:
        adjective = _random.choice([x for x in _adjectives if match(x)])
    except IndexError:
        adjective = _random.choice(_adjectives)

    if type(adjective) is tuple:
        adjective, _ = adjective

    return "-".join((adjective, animal))

if __name__ == "__main__":
    for i in range(100):
        print(generate_animal_id())

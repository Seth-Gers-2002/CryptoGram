## Name: Seth Gersbach
## Student id: 14045002
##
## Coded_text = iyseivnryuvvkwqanliyilplvqigvwalhrghuklwcqmgxsjxsbhwnydlrvqqkstiyijiqhgatgvavfmctarylprvbyiyivmfpnkpkmgvrjvgsvtwvgiavtaixnhvfhcjzaalsaydieemumptxegdcgiqtcrkjiumnghfgamwcothvhgvwlrigzruqsprldwpajhvgrpehkmojthkvvfuhrgatzwuzhhvmtuaabkhbnqcmfowlrlxqignwlrnczxwlvxnmtjxzzrytaiyidwxmfbpeehcuguthvazqflneafawliseptjxoiuhrqerrkqrrwxuwijarrnehfgziptvhcvhlphmzidixsvfibytuyuiwmbgpehoivmaliiyemqxnexejgcqhvgvklwcqmixgjmlgrjibgxmfqdauxgvlwarytaiksuzhegxpdsvmossaxxlwzoinkczrybkegxbglsalwrwgvekwqeawxehwxhrqxckxzwxkumwfawdhvubhciyifcvlpcwgudvxxsscuwqxetszglqrrfmwfyypkinwkfgsbhhshgwvwmgsztcuiicdpvmnaixnhvfhcnekivpnotfafmueawwzwnqhafhcjpsdhvlapmitmhrjbsvpqlhfnmtulaasvrlxuifkbanlryejifxrkxjivjbephbdmluhrgmdiihcepvvpemkudrqtazqabhhehavjgzwlrytuijiokbotiremqxwxuwijarrfetxeugdwnlirxwapeaiwzpgartuxgrrvdlwvhcrvqkrrgbclikbrwuteveemumptcgsdqwmptaklgcjlgmdueq
##
##

## JCU academic word list https://www.jcu.edu.au/__data/assets/pdf_file/0004/1015348/Academic-Word-List.pdf
Coded_text = "iyseivnryuvvkwqanliyilplvqigvwalhrghuklwcqmgxsjxsbhwnydlrvqqkstiyijiqhgatgvavfmctarylprvbyiyivmfpnkpkmgvrjvgsvtwvgiavtaixnhvfhcjzaalsaydieemumptxegdcgiqtcrkjiumnghfgamwcothvhgvwlrigzruqsprldwpajhvgrpehkmojthkvvfuhrgatzwuzhhvmtuaabkhbnqcmfowlrlxqignwlrnczxwlvxnmtjxzzrytaiyidwxmfbpeehcuguthvazqflneafawliseptjxoiuhrqerrkqrrwxuwijarrnehfgziptvhcvhlphmzidixsvfibytuyuiwmbgpehoivmaliiyemqxnexejgcqhvgvklwcqmixgjmlgrjibgxmfqdauxgvlwarytaiksuzhegxpdsvmossaxxlwzoinkczrybkegxbglsalwrwgvekwqeawxehwxhrqxckxzwxkumwfawdhvubhciyifcvlpcwgudvxxsscuwqxetszglqrrfmwfyypkinwkfgsbhhshgwvwmgsztcuiicdpvmnaixnhvfhcnekivpnotfafmueawwzwnqhafhcjpsdhvlapmitmhrjbsvpqlhfnmtulaasvrlxuifkbanlryejifxrkxjivjbephbdmluhrgmdiihcepvvpemkudrqtazqabhhehavjgzwlrytuijiokbotiremqxwxuwijarrfetxeugdwnlirxwapeaiwzpgartuxgrrvdlwvhcrvqkrrgbclikbrwuteveemumptcgsdqwmptaklgcjlgmdueq"

# attempts to find common Bigrams

decypher_words1 = ["analysis", 'approach', "area", "assessment", "assume", 'authority', 'available', 'benefit',
                   'concept',
                   'consistent', 'constitutional', 'context', 'contract', 'create', 'data', 'definition', 'derived',
                   'distribution', 'economic', 'environment', 'established', 'estimate', 'evidence', 'export',
                   'factors',
                   'financial', 'formula', 'function', 'identified', 'income', 'indicate', 'individual',
                   'interpretation',
                   'involved', 'issues', 'labour', 'legal', 'legislation', 'major', 'method', 'occur', 'percent',
                   'period',
                   'policy', 'principle', 'procedure', 'process', 'required', 'research', 'response', 'role', 'section',
                   'sector',
                   'significant', 'similar', 'source', 'specific', 'structure', 'theory', 'variables']

decypher_words2 = ["achieve", 'acquisition', 'administration', 'affect', 'appropriate', 'aspects', 'assistance',
                   'categories', 'chapter',
                   'commission', 'community', 'complex', 'computer', 'conclusion', 'conduct', 'consequences',
                   'construction', 'consumer', 'credit', 'cultural',
                   'design', 'distinction', 'elements', 'equation', 'evaluation', 'features',
                   'final', 'focus', 'impact', 'injury', 'institute', 'investment', 'items', 'journal',
                   'maintenance', 'normal', 'obtained', 'participation', 'perceived', 'positive', 'potential',
                   'previous', 'primary', 'purchase', 'range', 'region', 'regulations', 'relevant',
                   'resident', 'resources', 'restricted', 'security', 'sought', 'select', 'site', 'strategies',
                   'survey', 'text', 'traditional', 'transfer']

decypher_words3 = ['alternative', 'circumstances', 'comments', 'compensation', 'components', 'consent', 'considerable',
                   'constant', 'constraints', 'contribution', 'convention', 'coordination', 'core', 'corporate',
                   'corresponding', 'criteria', 'deduction', 'demonstrate', 'document', 'dominant', 'emphasis',
                   'ensure', 'excluded', 'framework', 'funds', 'illustrated', 'immigration', 'implies',
                   'initial', 'instance', 'interaction', 'justification', 'layer', 'link', 'location', 'maximum',
                   'minorities', 'negative',
                   'outcomes', 'partnership', 'philosophy', 'physical', 'proportion', 'published', 'reaction',
                   'registered', 'reliance', 'removed', 'scheme', 'sequence', 'sex', 'shift', 'specified', 'sufficient',
                   'task',
                   'technical', 'techniques', 'technology', 'validity', 'volume']

decypher_words4 = ['access', 'adequate', 'annual', 'apparent', 'approximated', 'attitudes', 'attributed', 'civil',
                   'code', 'commitment', 'communication',
                   'concentration', 'conference', 'contrast', 'cycle', 'debate', 'despite', 'dimensions', 'domestic',
                   'emerged', 'error', 'ethnic', 'goals', 'granted', 'hence',
                   'hypothesis', 'implementation', 'implications', 'imposed', 'integration', 'internal',
                   'investigation', 'job',
                   'label', 'mechanism', 'obvious', 'occupational', 'option', 'output', 'overall', 'parallel',
                   'parameters', 'phase',
                   'predicted', 'principal', 'prior', 'professional', 'project', 'promote', 'regime', 'resolution',
                   'retained', 'series', 'statistics', 'status', 'stress', 'subsequent', 'sum', 'summary', 'undertaken']

common_sentence_starters = ["The", "It", "He", "She", "They", "We", "I", "There", "This", "That", "In", "On", "When",
                            "While",
                            "After", "Before", "Because", "Since", "Although", "As", "If", "So", "But", "And", "Then",
                            "Once", "At", "With", "From"]

common_sentence_openings = [
    "Inconclusion",
    "Forexample",
    "Asaresult",
    "Ontheotherhand",
    "Inaddition",
    "However",
    "Therefore",
    "Tobeginwith",
    "Firstofall",
    "Itisimportanttonotethat",
    "Accordingto",
    "Thereis",
    "Thereare",
    "Thepurposeofthis",
    "Thismeansthat",
    "Onereasonis",
    "Anotherpointis",
    "Infact",
    "Interestingly",
    "Overtime",
    "Duringthe",
    "Whileitmayseem",
    "Despitethis",
    "Although",
    "Becauseofthis"
]

meaningful_words = [
    "freedom", "courage", "knowledge", "justice", "truth", "honesty", "friendship", "creativity", "innovation",
    "adventure", "wisdom", "hope", "change", "growth", "balance",
    "focus", "passion", "respect", "gratitude", "integrity", "compassion", "strength", "vision", "confidence",
    "discipline",
    "empathy", "leadership", "resilience", "imagination", "curiosity"
]

testing = [
    "apple", "banana", "computer", "dream", "elephant",
    "freedom", "garden", "happy", "internet", "jungle",
    "knowledge", "love", "mountain", "nature", "ocean",
    "peace", "question", "river", "sunshine", "tree",
    "universe", "victory", "wisdom", "xylophone", "youth", "zebra"
]

there_words = [
    "there",
    "thereabout",
    "thereabouts",
    "thereafter",
    "thereagainst",
    "thereamong",
    "thereamongst",
    "thereat",
    "therebefore",
    "therebetween",
    "thereby",
    "therefrom",
    "therein",
    "thereinside",
    "thereinto",
    "thereof",
    "thereon",
    "thereto",
    "thereunder",
    "thereuntil",
    "thereupon",
    "therewith",
    "therewithin",
    "thereout",
    "thereafterward",
    "thereafterwards"
]

over_words = [
    "over",
    "overact",
    "overachieve",
    "overactive",
    "overanalyze",
    "overbearing",
    "overboard",
    "overcast",
    "overcharge",
    "overcome",
    "overcompensate",
    "overconfident",
    "overcook",
    "overcrowded",
    "overdo",
    "overdose",
    "overdraft",
    "overeat",
    "overestimate",
    "overexert",
    "overexpose",
    "overflow",
    "overgrown",
    "overhaul",
    "overhead",
    "overheat",
    "overjoyed",
    "overkill",
    "overload",
    "overlook",
    "overnight",
    "overpower",
    "overprotective",
    "overqualified",
    "override",
    "overrule",
    "oversee",
    "overshadow",
    "overshoot",
    "oversight",
    "oversleep",
    "overspend",
    "overstate",
    "overstep",
    "overtake",
    "overtax",
    "overthink",
    "overthrow",
    "overtime",
    "overtired",
    "overtly",
    "overtone",
    "overturn",
    "overuse",
    "overwhelm",
    "overwork",
    "overwrite"
]

pro_words = [
    "pro",
    "proactive",
    "probability",
    "probable",
    "probably",
    "probe",
    "problem",
    "procedure",
    "process",
    "processing",
    "processor",
    "proclaim",
    "proclamation",
    "procrastinate",
    "produce",
    "producer",
    "product",
    "production",
    "productive",
    "productivity",
    "profession",
    "professional",
    "professor",
    "profile",
    "profit",
    "profitable",
    "profound",
    "program",
    "progress",
    "progressive",
    "prohibit",
    "project",
    "projection",
    "promise",
    "promote",
    "promotion",
    "prompt",
    "proof",
    "propaganda",
    "propel",
    "proper",
    "property",
    "proposal",
    "propose",
    "prospect",
    "prosper",
    "prosperity",
    "protect",
    "protection",
    "protein",
    "protest",
    "protocol",
    "prove",
    "provide",
    "provider",
    "province",
    "provision",
    "provoke"
]

at_words = [
    "at",
    "ate",
    "atlas",
    "atom",
    "atone",
    "attract",
    "attraction",
    "attractive",
    "attribute",
    "attend",
    "attention",
    "attentive",
    "attic",
    "attain",
    "attempt",
    "attest",
    "attitude",
    "attorney",
    "attack",
    "attach",
    "attachment",
    "attire",
    "attendance",
    "attendant",
    "atmosphere",
    "atmospheric",
    "atrocity",
    "atrophy",
    "atypical"
]

qu_words = [
    "quadratic",
    "qualities",
    "quantized",
    "quickstep",
    "questions",
    "quivering",
    "quenchers",
    "qualified",
    "quickened",
    "quietness",
    "quickfire",
    "quickdraw",
    "quarreled",
    "quittable",
    "quizzical",
    "quaintest",
    "quadruped",
    "quintuplet",
]

se_words = [
    "searching",
    "seriously",
    "seedlings",
    "seemingly",
    "separator",
    "secretive",
    "sensation",
    "sentencey",
    "seclusion",
    "sectarian",
    "selection",
    "semantics",
    "seminated",
    "sergeanty",
    "seriously",
    "selfishly",
    "separator",
    "semesterly",
    "settlement",
    "severable",
    "seafaring",
    "searchers",
    "sensitize",
]

fun_words = [
    "functions",
    "funerally",
    "furnishes",
    "funiculars",
    "fundamenta",
    "furnished",
    "fundraise",
    "funneling",
    "funloving",
    "fungiforms",
    "funniness",
    "funhouses",
    "fundatory",
]

# Attempts to decode by finding the keyword

nine_letter_words = [
    "advantage", "appliance", "attention", "beautiful", "benchmark",
    "breathing", "chocolate", "committed", "conscious", "delighted",
    "education", "fantastic", "generally", "happiness", "important",
    "injection", "knowledge", "marketing", "notorious", "operation",
    "permanent", "recording", "strategic", "treatment", "treasury",
    "volunteer", "wonderful", "adventure", "agreement", "alignment",
    "alliances", "animating", "authority", "awakening", "beginning",
    "belonging", "blessings", "blueprint", "brilliant", "candidate",
    "celebrate", "certainty", "chivalric", "classroom", "cleverest",
    "colorless", "commodity", "companion", "complaint", "conqueror",
    "creatures", "creatives", "cultivate", "dedicated", "democracy",
    "dependent", "directing", "discovery", "efficacy", "education",
    "emotional", "empowered", "endeavors", "energized", "engineers",
    "exploring", "fairytale", "favorable", "fertility", "finishing",
    "fireplace", "flourish", "foolproof", "fortunate", "framework",
    "friendship", "generates", "generous", "gentleman", "governors",
    "happiness", "heartfelt", "highlight", "honeymoon", "hospitals",
    "illustrate", "imaginary", "important", "informed", "injustice",
    "inspired", "intellect", "inventing", "invincible", "knowledge"
]

nine_letter_the_words = [
    "theatrics",
    "theocracy",
    "theorists",
    "theoremic",
    "therapies",
    "therefore",
    "thereunto",
    "therewith",
    "thermally",
    "thermions",
    "thesaurus",
    "theorized",
    "theorizes",
    "theologue",
    "thermobar"
]

nine_letter_ch_words = [
    "challenge",
    "chronicle",
    "checklist",
    "chipmaker",
    "childhood",
    "chivalric",
    "chromatic",
    "chubbiest",
    "chintzily",
    "chequings"
]

nine_letter_gr_words = [
    "grapefruit",
    "greenback",
    "graphical",
    "grassland",
    "greyhound",
    "grumbling",
    "grounding",
    "grandiose",
    "graceless",
    "gratified",
    "gradually",
    "gravitate",
    "greenroom",
    "grappling",
    "grievance",
    "greenwood",
    "greyliest",
    "grandeurs",
    "griddlers",
    "grizzlies",
    "granitize",
    "groundhog",
    "grubstake",
]

nine_letter_pr_words = [
    "practical",
    "procedure",
    "precision",
    "presuming",
    "prisoners",
    "prankster",
    "preachers",
    "president",
    "priceless",
    "primality",
    "prevented",
    "prejudice",
    "prophetic",
    "prototype",
    "proximity",
    "prismatic",
    "privately",
    "prospects",
    "preflight",
    "prickling",
]

import numpy as np


def main():
    ###
    ###Decode by brute forcing the code word
    ###

    # Display message
    print('message to decrypt')
    print(Coded_text)
    # finding length
    print("converted to numbers")
    pattern_finder = decypher(Coded_text)
    print(pattern_finder)
    # coincidences
    patterns(pattern_finder)

    # go though a list of keywords and decode them againts the encode text
    Coded_Num_text = decypher(Coded_text)
    for i in nine_letter_pr_words:
        print(i)
        Output = decode(Coded_Num_text, i)
        decoded(Output)

    # decode with a single keyword
    word = "president"
    result = decode(Coded_Num_text, word)
    answer = decoded(result)
    print(''.join(answer))

    Coded_Num_text = decypher(["v", "i", "t", "k", 'c', 'o', 'w', 's', "v", "i", "t", "k"])
    result = decode(Coded_Num_text, 'dead')
    print(decoded(result))

    # used to find repeating word combinations in case

    # repeats = find_repeated_patterns(''.join(answer))
    # for pattern, positions in repeats.items():
    #     print(f"Pattern: {pattern} at positions {positions}")
    #     distances = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]
    #     print(f"  Distances between repetitions: {distances}")

    ### KEYWORD HAS SOMETHING TO DO WITH PRONE


# thereby = prone up
# thereupon = prone by
# over = udon
# husk=beau

# pr =th
# heal = bust
# he = bu
# at = if
# def=fun
# tr =ph
# te=pu
# hp=bad
# im=am

# starting word cant be
# probaly doesnt start with the
# kn = yl
# gr=ch
# pros = them
# prog = they
# prome = these
# prone = there
# produc = the bot
# prostra =  the pen
# se=qu


###
###Decode by brute forcing the starting word
###

##menu() complex running

# def menu():
#     print("D: Decypher letters to numbers")
#     user_command = input("please enter a command word:")
#     while True:
#         if user_command == "D":
#             Coded_Num_text = decypher(Coded_text)
#         if user_command == "E":
#             break
#         if user_command == "B":
#             decoder_word = 'list'
#             decode(Coded_Num_text, decoder_word)
#         print("D: Decypher letters to numbers, E: escape")
#         user_command = input("please enter a command word:")

def decypher(input_text):
    Coded_Num_text = []
    for i in input_text:
        i = i.lower()
        z = ord(i)
        z = int(z) - 97
        Coded_Num_text.append(z)
    return Coded_Num_text


def decode(input_text, input_word):
    word_coded = decypher(input_word)
    counter = 0
    end = len(word_coded)
    return_word = []
    for i in input_text:
        if counter == end:
            counter = 0

        subtract = int(word_coded[counter])
        z = i - subtract

        counter += 1

        if z < 0:
            z = z + 26
        return_word.append(z)

    ##print(return_word)
    return return_word


def decoded(input_text):
    Decoded_Num_text = []
    for i in input_text:
        z = int(i) + 97
        z = chr(z)
        Decoded_Num_text.append(z)
    print(Decoded_Num_text)
    return Decoded_Num_text


def patterns(pattern_finder):
    displaced_text = pattern_finder.copy()
    max_length = len(displaced_text)
    matching_counter = 0
    coincidences_counter = []
    while max_length > 0:
        displaced_text.pop()
        displaced_text.insert(0, " ")
        max_length = max_length - 1

        for x, y in zip(pattern_finder, displaced_text):
            if (x or y) == " ":
                pass
            elif x == y:
                matching_counter += 1

        coincidences_counter.insert(-1, matching_counter)
        matching_counter = 0
    print("number of coincidences")
    print(coincidences_counter)


from collections import defaultdict


def find_repeated_patterns(text, min_len=3, max_len=6):
    patterns = defaultdict(list)

    for length in range(min_len, max_len + 1):
        for i in range(len(text) - length + 1):
            pattern = text[i:i + length]
            patterns[pattern].append(i)

    # Only keep patterns that occur more than once
    repeated = {pat: pos for pat, pos in patterns.items() if len(pos) > 1}
    return repeated


main()

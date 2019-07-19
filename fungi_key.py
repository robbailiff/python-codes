"""
I have created a basic key for British Fungi.
I have added the main fungi groups in their English names as suggested and their more up-to-date latin names. 
I have listed a bibliography at the very end of the script. 
Hopefully, it should work correctly, but there are always exceptions to the rule, and by their nature fungi are very variable and change rapidly. 
I don't know anything about fungi outside of the UK so it may not work for any specimens found outside of it. 

"""

#################
# Fungi Functions
#################

def bracket_key():
    while True:
        print("""
        What are the features of the crust, shelf or bracket?
        Choose one of the following numbers:
        1. Gills on the underside
        2. Crust or smooth underside (no pores or gills)
        3. Pores and a short stipe
        4. Pores and no stipe
        """)

        bracket_choice = int(input("Enter a number (1-4): "))

        if bracket_choice == 1:
            print("""
            \nEnglish name: Oysters\nMain genus: Pleurotus
            """)

        elif bracket_choice == 2:
            print("""
            \nEnglish name: Crusts\nMain genus: Stereum
            """)

        elif bracket_choice == 3:
            print("""
            \nEnglish name: Polypores\nMain genus: Polyporus
            """)

        elif bracket_choice == 4:
            print("""
            \nEnglish name: Brackets\nMain genera: Ganoderma and Trametes
            """)

        else:
            print("That was not a valid input")
            continue

        break


def coral_key():
    while True:
        print("""
        What are the features of the finger, club or coral?
        Choose one of the following numbers:
        1. Jelly-like texture
        2. Hard texture
        3. Foul-smelling finger with a fleshy texture
        4. Unbranched finger or club with brittle texture
        5. Branched finger or club with a brittle texture
        """)

        coral_choice = int(input("Enter a number (1-5): "))

        if coral_choice == 1:
            print("""
            \nEnglish name: Stagshorns\nMain genus: Calocera
            """)

        elif coral_choice == 2:
            print("""
            \nEnglish name: Candlesnuff and Fingers\nMain genus: Xylaria
            """)

        elif coral_choice == 3:
            print("""
            \nEnglish name: Stinkhorns\nMain genus: Phallus
            """)

        elif coral_choice == 4:
            print("""
            \nEnglish name: Clubs\nMain genus: Clavulinopsis
            """)

        elif coral_choice == 5:
            print("""
            \nEnglish name: Corals\nMain genera: Clavulina and Ramaria
            """)

        else:
            print("That was not a valid input")
            continue

        break


def sphere_key():
    while True:
        print("""
        What are the features of the Spherical, star-shaped or nest-like fruitbody?
        Choose one of the following numbers:
        1. Skin peeling back in a star like pattern
        2. Nest-like with tiny 'eggs' inside
        3. Spherical with thin skin and white flesh
        4. Spherical with thick skin and dark flesh
        5. Spherical with jelly layer below skin
        6. Spherical with underground fruitbody
        """)

        sphere_choice = int(input("Enter a number (1-6): "))

        if sphere_choice == 1:
            print("""
            \nEnglish name: Earthstars\nMain genus: Geastrum
            """)

        elif sphere_choice == 2:
            print("""
            \nEnglish name: Bird's Nest\nMain genus: Cyathus
            """)

        elif sphere_choice == 3:
            print("""
            \nEnglish name: Puffballs\nMain genus: Lycoperdon
            """)

        elif sphere_choice == 4:
            print("""
            \nEnglish name: Earthballs\nMain genus: Scleroderma
            """)

        elif sphere_choice == 5:
            print("""
            \nEnglish name: Stinkhorns\nMain genus: Phallus
            """)

        elif sphere_choice == 6:
            print("""
            \nEnglish name: Truffles\nMain genus: Tuber
            """)

        else:
            print("That was not a valid input")
            continue

        break


def cup_key():
    while True:
        print("""
        What are the features of the cup, ear, saddle, or brain?
        Choose one of the following numbers:
        1. Cup-shaped
        2. Ear-shaped with jelly-like texture
        3. Saddle-shaped with a dry texture
        4. Brain-shaped with a jelly-like texture
        5. Brain-shaped with a dry texture
        """)

        cup_choice = int(input("Enter a number (1-5): "))

        if cup_choice == 1:
            print("""
            \nEnglish name: Cups\nMain genus: Peziza
            """)

        elif cup_choice == 2:
            print("""
            \nEnglish name: Jelly Ears\nMain genus: Auricularia
            """)

        elif cup_choice == 3:
            print("""
            \nEnglish name: Saddles\nMain genus: Helvella
            """)

        elif cup_choice == 4:
            print("""
            \nEnglish name: Jelly Fungi\nMain genera: Exidia and Tremella
            """)

        elif cup_choice == 5:
            print("""
            \nEnglish name: Morels and False Morels\nMain genera: Morchella and Gyromitra
            """)

        else:
            print("That was not a valid input")
            continue

        break


def mushroom_key():
    while True:
        print("""
        What are the features of the mushroom?
        Choose one of the following numbers:
        1. Teeth on the underside
        2. Pores on the underside
        3. Smooth or wrinkled on the underside
        4. Gills with pale-coloured spores (white, cream or pale yellow spores)
        5. Gills with dark-coloured spores (pink, purple, rust, brown or black spores)
        """)

        mush_choice = int(input("Enter a number (1-5): "))

        if mush_choice == 1:
            print("""
            \nEnglish name: Toothed Fungi\nMain genus: Hydnum
            """)

        elif mush_choice == 2:
            print("""
            \nEnglish name: Boletes\nMain genus: Boletus
            """)

        elif mush_choice == 3:
            print("""
            \nEnglish name: Chanterelles\nMain genus: Cantharellus
            """)

        elif mush_choice == 4:
            pale_gills()

        elif mush_choice == 5:
            dark_gills()

        else:
            print("That was not a valid input")
            continue

        break


######################
# Pale Spore Functions
######################

def pale_gills():
    while True:
        print("""
        What are the features of the gilled mushroom with pale spores?
        Choose one of the following numbers:
        1. Gills mostly (Adnate) or partially (Adnexed) attached to the stem
        2. Gills running down the stem (Decurrent)
        3. Gills notched before attaching to stem (Emarginate)
        4. Gills not attached to the stem (Free)
        """)

        palegill_choice = int(input("Enter a number (1-4): "))

        if palegill_choice == 1:
            adnate_gills()

        elif palegill_choice == 2:
            decurrent_gills()

        elif palegill_choice == 3:
            emarginate_gills()

        elif palegill_choice == 4:
            free_gills()

        else:
            print("That was not a valid input")
            continue

        break


def adnate_gills():
    while True:
        print("""
        What are the features of the mushroom with adnate or adnexed gills?
        Choose one of the following numbers:
        1. Gills thick, waxy, mostly in grass
        2. Fruitbody easily crumbled, in woodland, damaged gills secrete milk-like fluid
        3. Fruitbody easily crumbled, in woodland, no fluid from damaged gills
        4. Ring present on stem, in woodland, cap has a granular texture
        5. Ring present on stem, growing on living or dead wood, scaly cap
        6. Bell-shaped cap, slender stem
        7. Small convex cap (<1.5cm), on twigs, leaves or needles
        8. Growing on decaying wood, stem is tough and fibrous
        9. In woodland, cap convex to flattened, thick gills
        """)

        adnate_choice = int(input("Enter a number (1-9): "))

        if adnate_choice == 1:
            print("""
            \nEnglish name: Waxcaps\nMain genus: Hygrocybe
            """)

        elif adnate_choice == 2:
            print("""
            \nEnglish name: Milkcaps\nMain genus: Lactarius
            """)

        elif adnate_choice == 3:
            print("""
            \nEnglish name: Brittlegills\nMain genus: Russula
            """)

        elif adnate_choice == 4:
            print("""
            \nEnglish name: Powdercaps\nMain genus: Cystoderma
            """)

        elif adnate_choice == 5:
            print("""
            \nEnglish name: Honey Fungus\nMain genus: Armillaria
            """)

        elif adnate_choice == 6:
            print("""
            \nEnglish name: Bonnets\nMain genus: Mycena
            """)

        elif adnate_choice == 7:
            print("""
            \nEnglish name: Parachutes\nMain genus: Marasmius
            """)

        elif adnate_choice == 8:
            print("""
            \nEnglish name: Toughshanks\nMain genus: Collybia
            """)

        elif adnate_choice == 9:
            print("""
            \nEnglish name: Deceivers\nMain genus: Laccaria
            """)

        else:
            print("That was not a valid input")
            continue

        break


def decurrent_gills():
    while True:
        print("""
        What are the features of the mushroom with decurrent gills?
        Choose one of the following numbers:
        1. Fruitbody easily crumbled, in woodland, damaged gills secrete milk-like fluid
        2. Fruitbody easily crumbled, in woodland, no fluid from damaged gills
        3. Ring present on stem, growing on living or dead wood, scaly cap
        4. Small, growing on moss, funnel-shaped cap and slender stem
        5. Small, growing on heaths or moorland, funnel-shaped cap
        6. Near conifers in woodland or heath, funnel-shaped cap, thick, waxy gills
        7. In woodland or grassland, funnel-shaped cap and inrolled margin
        8. In woodland, cap convex to flattened, tough stem, thick gills
        """)

        decurrent_choice = int(input("Enter a number (1-8): "))

        if decurrent_choice == 1:
            print("""
            \nEnglish name: Milkcaps\nMain genus: Lactarius
            """)

        elif decurrent_choice == 2:
            print("""
            \nEnglish name: Brittlegills\nMain genus: Russula
            """)

        elif decurrent_choice == 3:
            print("""
            \nEnglish name: Honey Fungus\nMain genus: Armillaria
            """)

        elif decurrent_choice == 4:
            print("""
            \nEnglish name: Mosscaps\nMain genus: Rickenella
            """)

        elif decurrent_choice == 5:
            print("""
            \nEnglish name: Navels\nMain genus: Lichenomphalia
            """)

        elif decurrent_choice == 6:
            print("""
            \nEnglish name: False Chanterelle\nMain genus: Hygrophoropsis
            """)

        elif decurrent_choice == 7:
            print("""
            \nEnglish name: Funnels\nMain genus: Clitocybe
            """)

        elif decurrent_choice == 8:
            print("""
            \nEnglish name: Deceivers\nMain genus: Laccaria
            """)

        else:
            print("That was not a valid input")
            continue

        break


def emarginate_gills():
    while True:
        print("""
        What are the features of the mushroom with emarginate gills?
        Choose one of the following numbers:
        1. Stocky, medium to large, broad convex cap with a prominent umbo, gills broad
        2. Medium to large, broad caps that are flattened with an umbo, gills crowded
        3. Stems fusing, clustered fruitbodies
        4. Growing on decaying wood, stem is tough and fibrous
        """)

        emarginate_choice = int(input("Enter a number (1-4): "))

        if emarginate_choice == 1:
            print("""
            \nEnglish name: Knights\nMain genus: Tricholoma
            """)

        elif emarginate_choice == 2:
            print("""
            \nEnglish name: Cavaliers\nMain genus: Melanoleuca
            """)

        elif emarginate_choice == 3:
            print("""
            \nEnglish name: Domecaps\nMain genus: Calocybe
            """)

        elif emarginate_choice == 4:
            print("""
            \nEnglish name: Toughshanks\nMain genus: Collybia
            """)

        else:
            print("That was not a valid input")
            continue

        break


def free_gills():
    while True:
        print("""
        What are the features of the mushroom with free gills?
        Choose one of the following numbers:
        1. Volva at stem base, ring on stem
        2. No volva, ring on stem, large sized
        3. No volva, ring on stem, small to medium sized
        4. No volva or stem ring, gills thick, waxy, mostly in grass
        """)

        free_choice = int(input("Enter a number (1-4): "))

        if free_choice == 1:
            print("""
            \nEnglish name: Amanitas\nMain genus: Amanita
            """)

        elif free_choice == 2:
            print("""
            \nEnglish name: Parasols\nMain genus: Macrolepiota
            """)

        elif free_choice == 3:
            print("""
            \nEnglish name: Dapperlings\nMain genus: Lepiota
            """)

        elif free_choice == 4:
            print("""
            \nEnglish name: Waxcaps\nMain genus: Hygrocybe
            """)

        else:
            print("That was not a valid input")
            continue

        break



######################
# Dark Spore Functions
######################

def dark_gills():
    while True:
        print("""
        What are the features of the gilled mushroom with dark spores?
        Choose one of the following numbers:
        1. Pink coloured spores
        2. Rusty-brown coloured spores
        3. Mid-brown coloured spores
        4. Purple-brown coloured spores
        5. Chocolate brown coloured spores
        6. Black coloured spores
        """)

        darkgill_choice = int(input("Enter a number (1-6): "))

        if darkgill_choice == 1:
            pink_spore()

        elif darkgill_choice == 2:
            rust_spore()

        elif darkgill_choice == 3:
            brown_spore()

        elif darkgill_choice == 4:
            purple_spore()

        elif darkgill_choice == 5:
            print("""
            \nEnglish name: Mushrooms\nMain genus: Agaricus
            """)

        elif darkgill_choice == 6:
            black_spore()

        else:
            print("That was not a valid input")
            continue

        break


def pink_spore():
    while True:
        print("""
        What are the features of the gilled mushroom with pink spores?
        Choose one of the following numbers:
        1. Present on rotting wood, gills free from stem
        2. Present on grassland, gills pink and not free from stem
        3. Stocky mushroom with lilac, brown or grey-pink gills, not free from stem
        """)

        pinksp_choice = int(input("Enter a number (1-3): "))

        if pinksp_choice == 1:
            print("""
            \nEnglish name: Shields\nMain genus: Pluteus
            """)

        elif pinksp_choice == 2:
            print("""
            \nEnglish name: Pinkgills\nMain genus: Entoloma
            """)

        elif pinksp_choice == 3:
            print("""
            \nEnglish name: Blewits\nMain genus: Lepista
            """)

        else:
            print("That was not a valid input")
            continue

        break


def rust_spore():
    while True:
        print("""
        What are the features of the gilled mushroom with rust-brown spores?
        Choose one of the following numbers:
        1. Present in grass or woody debris, small and fragile
        2. Present in woodland with a cobweb-like veil on cap
        3. Growing on wood, medium to large sized, tiny scales on cap
        4. Growing on wood, small to medium sized, gills yellow, stained rust-brown on maturity
        5. Growing on or near wood, small and usually trooping, cap feel felted or rough
        6. Present on soil or wood, cap velvet or downy feel, cap margin tightly inrolled
        """)

        rustsp_choice = int(input("Enter a number (1-6): "))

        if rustsp_choice == 1:
            print("""
            \nEnglish name: Conecaps\nMain genus: Conocybe
            """)

        elif rustsp_choice == 2:
            print("""
            \nEnglish name: Webcaps\nMain genus: Cortinarius
            """)

        elif rustsp_choice == 3:
            print("""
            \nEnglish name: Scalycaps\nMain genus: Pholiota
            """)

        elif rustsp_choice == 4:
            print("""
            \nEnglish name: Rustgills\nMain genus: Gymnopilus
            """)

        elif rustsp_choice == 5:
            print("""
            \nEnglish name: Twiglets\nMain genus: Tubaria
            """)

        elif rustsp_choice == 6:
            print("""
            \nEnglish name: Rollrims\nMain genus: Paxillus
            """)

        else:
            print("That was not a valid input")
            continue

        break


def brown_spore():
    while True:
        print("""
        What are the features of the gilled mushroom with mid-brown spores?
        Choose one of the following numbers:
        1. Present in grass, small and fragile, rounded cap
        2. Present in grass, moss, on wood, small and fragile, bell- or helmet-shaped cap
        3. Present in woodlands, small to medium sized, conical fibrous cap
        4. Present in woodlands, small to medium sized, convex to flat sticky or greasy cap
        """)

        brownsp_choice = int(input("Enter a number (1-4): "))

        if brownsp_choice == 1:
            print("""
            \nEnglish name: Fieldcaps\nMain genus: Agrocybe
            """)

        elif brownsp_choice == 2:
            print("""
            \nEnglish name: Bells\nMain genus: Galerina
            """)

        elif brownsp_choice == 3:
            print("""
            \nEnglish name: Fibrecaps\nMain genus: Inocybe
            """)

        elif brownsp_choice == 4:
            print("""
            \nEnglish name: Poisonpies\nMain genus: Hebeloma
            """)

        else:
            print("That was not a valid input")
            continue

        break


def purple_spore():
    while True:
        print("""
        What are the features of the gilled mushroom with purple-brown spores?
        Choose one of the following numbers:
        1. Growing on dead or decaying wood, small and robust
        2. Growing on grass or dung, small to medium sized, rounded cap
        """)

        purplesp_choice = int(input("Enter a number (1-2): "))

        if purplesp_choice == 1:
            print("""
            \nEnglish name: Tufts\nMain genus: Hypholoma
            """)

        elif purplesp_choice == 2:
            print("""
            \nEnglish name: Roundheads\nMain genus: Stropharia
            """)

        else:
            print("That was not a valid input")
            continue

        break


def black_spore():
    while True:
        print("""
        What are the features of the gilled mushroom with black spores?
        Choose one of the following numbers:
        1. Inky fluid from mature gills
        2. No inky fluid, mottled gills
        3. No inky fluid, plain gills and brittle stem
        """)

        blacksp_choice = int(input("Enter a number (1-3): "))

        if blacksp_choice == 1:
            print("""
            \nEnglish name: Inkcaps\nMain genus: Coprinopsis
            """)

        elif blacksp_choice == 2:
            print("""
            \nEnglish name: Mottlegills\nMain genus: Panaeolus
            """)

        elif blacksp_choice == 3:
            print("""
            \nEnglish name: Brittlestems\nMain genus: Psathyrella
            """)

        else:
            print("That was not a valid input")
            continue

        break


###############
# Main Program
###############

while True:
    print("""
    What is the shape of the fruit body?
    Choose one of the following numbers:
    1. Crust, shelf or bracket shape growing on wood
    2. Finger, club or coral shape
    3. Spherical, star-shaped or nest-like
    4. Cup, ear, saddle, or brain-shaped
    5. Mushroom with a cap and central stem
    """)
    q1_choice = int(input("Enter a number (1-6): "))

    if q1_choice == 1:
        bracket_key()

    elif q1_choice == 2:
        coral_key()

    elif q1_choice == 3:
        sphere_key()

    elif q1_choice == 4:
        cup_key()

    elif q1_choice == 5:
        mushroom_key()

    else:
        print("That was not a valid input")
        continue

    break

##############
# Bibliography
##############
"""
* Collins Gem: Mushrooms by Patrick Harding & Alan Outen
* Collins Complete Guide to British Mushrooms and Toadstools By Paul Sterry & Barry Hughes
* Collins Fungi Guide by Stefan Buczacki, Chris Shields & Denys Ovenden
* Bloomsbury Pocket Guide to Mushrooms by John C. Harris
* Mushrooms: A Comprehensive Guide by Roger Phillips
* Fascinated by Fungi by Pat O'Reilly
* Collins Nature Guide – Mushrooms and Toadstools of Britain and Europe by Edmund Garnweidner (Outdated)
* Fungi of Britain app by NatureBritain
* Mushroomexpert.com
* First-Nature.com
"""

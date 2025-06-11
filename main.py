from lookup.database import SayingDatabase, Saying
# To run the tests, uncomment one case function and comment out the others to run them

# 20 Sayings, alphabetical order for convenience
s1 = Saying(
    "ʻAia akula nō i Ki'ilau.",
    "He is gone to Ki'ilau.",
    "He ʻōlelo no ka kamaʻilio lapuwale a me ka ʻōlelo ʻole loa.",
    "Said of senseless chatter, aimless talk. A play on ki'i (fetch) and lau (many), meaning to fetch much; that is, to fetch a lot to talk about. Ki'ilau is a place in 'Ewa, O'ahu."
)

s2 = Saying(
    "ʻĀina koi 'ula i ka lepo.",
    "Land reddened by the rising dust.",
    "He ʻōlelo no ka ʻāina o ʻEwa, Oʻahu, i ka wā e ʻulaʻula ai ka lepo i ka makani.",
    "Said of 'Ewa, O'ahu, when the dust turns red in the wind."
    )

s3 = Saying(
    "ʻAu ana ka Lae 'o Maunauna i ka 'ino.",
    "Point Manauna swims in the storm.",
    "He ʻōlelo no ke kanaka kūpaʻa i nā pilikia o ke ola e like me ka Lae ʻo Maunauna.",
    "Said of a courageous person who withstands the storms of life like Point Maunauna."
)

s4 = Saying(
    "E hoʻi ka uʻi o Mānoa, ua ahiahi.",
    "Let the youth of Mānoa go home, for it is evening.",
    "He ʻōlelo no ka poʻe ʻōpio o Mānoa e haʻalele i ka hana a hoʻi i ka hale i ka wā ahiahi.",
    "Refers to the youth of Mānoa who used to ride the surf and leave early to avoid work."
)

s5 = Saying(
    "Hāhā pōʻele ka pāpaʻi o Kou.",
    "The crabs of Kou are groped for in the dark.",
    "He ʻōlelo no ka mea e ʻimi ana i nā pāpaʻi ma ka pōʻeleʻele me ka mākaukau ʻole.",
    "Applied to one who goes groping in the dark for crabs."
)

s6 = Saying(
    "He kai ʻāhiu ko Kahana.",
    "A wild sea has Kahana.",
    "He ʻōlelo no ke kai ʻino o Kahana, Oʻahu, i kona ʻano ʻino loa.",
    "Refers to Kahana, O'ahu, and its wild sea."
)

s7 = Saying(
    "He lāʻau kū hoʻokahi, he lehua no Kaʻala.",
    "A lone tree, a lehua of Ka'ala.",
    "He ʻōlelo mahalo no ke kanaka kū hoʻokahi i ka nani, ke akamai, a me ke akamai.",
    "An expression of admiration for an outstanding person, unequaled in beauty, wisdom, or skill."
)

s8 = Saying(
    "Ka hilu pani wai o Hauʻula.",
    "The water-damming hilu fish of Hau'ula.",
    "He ʻōlelo no ka iʻa hilu o Hauʻula, Oʻahu, i kona hana e pani i ka wai.",
    "Refers to Hau'ula, O'ahu, where hilu fish dammed water in ancient tales."
)

s9 = Saying(
    "Ka makani Hoʻeo o Moanalua.",
    "The Ho'eo, whistling wind of Moanalua.",
    "He ʻōlelo no ka makani kani o Moanalua, Oʻahu, i kona leo kani.",
    "Refers to the whistling wind of Moanalua, O'ahu."
)

s10 = Saying(
    "Ka ua kīkē hala o Punaluʻu.",
    "The hala-pelting rain of Punalu'u.",
    "He ʻōlelo no ka ua e kuʻi i nā hala ma Punaluʻu, Oʻahu.",
    "Refers to the rain at Punalu'u, O'ahu, that pelts hala."
)

s11 = Saying(
    "Ke one kuilima laulā o ʻEwa.",
    "The sand on which there was a linking of arms on the breadth of 'Ewa.",
    "He ʻōlelo no ka one o ʻEwa, Oʻahu, kahi i hui ai nā lima o nā kānaka.",
    "Refers to 'Ewa, O'ahu, where people linked arms in battle."
)

s12 = Saying(
    "Kū aʻe ʻEwa; noho iho ʻEwa.",
    "Stand-up 'Ewa; sit-down 'Ewa.",
    "He ʻōlelo no nā pōhaku o ʻEwa, Oʻahu, e mākaukau ai nā kānaka i ka wā e kū a noho ai.",
    "The names of two stones marking the boundary between chiefs' and commoners' land in 'Ewa, O'ahu."
)

s13 = Saying(
    "Lāʻie i ka ʻēheu o nā manu.",
    "Lā'ie, borne on the wings of birds.",
    "He ʻōlelo no Lāʻie, Oʻahu, kahi i lawe ʻia ai e nā manu.",
    "Lā'ie is a gathering place where people were borne on birds' wings."
)

s14 = Saying(
    "Make ʻo Mikololou a ola i ke alelo.",
    "Mikololou died and lived again through his tongue.",
    "He ʻōlelo no Mikololou, ke akua manō, i ola hou ma kāna alelo.",
    "Said of one who talks himself out of a predicament like Mikololou."
)

s15 = Saying(
    "Nā ʻale hānupaupa o Pailolo.",
    "The choppy billows of Pailolo.",
    "He ʻōlelo no nā nalu ʻino o Pailolo ma waena o Oʻahu a me Molokaʻi.",
    "Refers to the choppy billows of the Pailolo channel between O'ahu and Moloka'i."
)

s16 = Saying(
    "Oʻahu a Lua.",
    "O'ahu, island of Lua.",
    "He ʻōlelo no Oʻahu, ka mokupuni a Lua i hoʻokumu ai.",
    "According to legend, O'ahu is the island of Lua, its father."
)

s17 = Saying(
    "Pā kōlea i ka wai o Punahou.",
    "The plover splashes in the water of Punahou.",
    "He ʻōlelo no ka kōlea e lele ana a pā i ka wai o Punahou, Oʻahu.",
    "Refers to the plover bird splashing in Punahou's water, O'ahu."
    )

s18 = Saying(
    "Piʻipiʻi hahai moa.",
    "Curly head followed by chickens.",
    "He ʻōlelo no ke kanaka lauoho wili e hahai ʻia e nā moa.",
    "Said of any curly-haired man who attracts women, like Kahahana."
)

s19 = Saying(
    "Uē ʻo Kānepūniu i ka wale a ka lā.",
    "Kānepūniu complains of the heat of the sun.",
    "He ʻōlelo no ke kanaka e uē ana i ka wela o ka lā ma Kānepūniu, Oʻahu.",
    "Said when someone complains of the heat, from a chant by Hi'iaka."
)

s20 = Saying(
    "Wai peʻepeʻe palai o Waiakekua.",
    "The water of Waiakekua that plays hide-and-seek among the ferns.",
    "He ʻōlelo no ka wai o Waiakekua, Mānoa, e pāʻani ana me nā palai.",
    "Refers to the water of Waiakekua in Mānoa playing among the ferns."
)

# Test Functions
def test_standard_case():
    db = SayingDatabase()
    print("\n--------------------------- Test 1: Standard Case (5 Sayings) ---------------------------")
    sayings = [s1, s4, s7, s10, s13]  # select s1, s4, s7, s10, s13
    for saying in sayings:
        db.insert_saying(saying)
    print()
    for saying in sayings:
        db.member(saying.hawaiian)  # member check for each saying
    print("\nFirst Saying in Hawaiian order:")  
    print(f"- {db.first()}")    # displays s1 "ʻAia..."
    print("\nLast Saying in Hawaiian order:")   
    print(f"- {db.last()}") # displays s13 "Lāʻie..."
    print("\nPredecessor of s7:")
    print(f"- {db.predecessor(s7.hawaiian)}")   # displays s4 "E hoʻi..."
    print("\nSuccessor of s4:")
    print(f"- {db.successor(s4.hawaiian)}")    # displays s7 "He lāʻau..."
    print("\nMeHua search for 'nā':")
    for saying in db.mehua("nā"):
        print(f"- {saying}")
    print("\nWithWord search for 'tree':")
    for saying in db.withword("tree"):
        print(f"- {saying}")

def test_duplicate_case(): # updates existing key but with modified values
    db = SayingDatabase()
    print("\n--------------------------- Test 2: Duplicates ---------------------------")
    db.insert_saying(s1) # shows same key but different translation and 
    s1_modified = Saying(
        s1.hawaiian,
        "He has gone ahead and went to Ki'ilau (modified)",
        s1.explanation_haw,
        "Said of meaningless chatter... (modified explanation)."
    )
    db.insert_saying(s1_modified)
    is_member = db.member(s1.hawaiian)
    print(f"Member check ({s1.hawaiian}): - {is_member}")
    retrieved_saying = db.tree.search_saying(s1.hawaiian).saying
    print("\nUpdated saying:")
    print(f"- {retrieved_saying}")


def test_unicode_validity():
    db = SayingDatabase()
    print("\n--------------------------- Test 3: Unicode Validity ---------------------------")
    db.insert_saying(s5) # as is, normal
    ascii_s5 = Saying("Haha po ele ka papa i o Kou", s5.english, s5.explanation_haw, s5.explanation_eng)
    db.insert_saying(ascii_s5)
    print()
    db.member(s5.hawaiian)
    db.member(ascii_s5.hawaiian)  # member check for ascii, have same explanations
    print("\nRetrieved unicode saying:")
    print(f"- {db.tree.search_saying(s5.hawaiian).saying}")
    print("\nRetrieved ascii saying:")
    print(f"- {db.tree.search_saying(ascii_s5.hawaiian).saying}")

def test_empty_tree(): # all negatives
    db = SayingDatabase()
    print("\n--------------------------- Test 4: Empty Tree ---------------------------")
    db.member(s1.hawaiian)
    print("\nFirst Saying in Hawaiian order:")
    print(f"- {db.first()}")
    print("\nLast Saying in Hawaiian order:")
    print(f"- {db.last()}")
    print("\nPredecessor of s5:")
    print(f"- {db.predecessor(s1.hawaiian)}")
    print("\nSuccessor of s15:")
    print(f"- {db.successor(s1.hawaiian)}")
    print("\nMeHua search for 'makani':")   # exists in list but no inserts
    for saying in db.mehua("makani"):
        print(f"- {saying}")
    print("\nWithWord search for 'mountain':")
    for saying in db.withword("mountain"):
        print(f"- {saying}")

def test_large_quantity():  # all 20 sayings
    db = SayingDatabase()
    print("\n--------------------------- Test 5: Large Quantity (20 Sayings) ---------------------------")
    for i in range(1, 21):
        db.insert_saying(globals()[f"s{i}"])
    print()
    for i in range(1, 21):
        db.member(globals()[f"s{i}"].hawaiian) 
    print("\nFirst Saying in Hawaiian order:")
    print(f"- {db.first()}")
    print("\nLast Saying in Hawaiian order:")
    print(f"- {db.last()}")
    print("\nPredecessor of s10:")
    print(f"- {db.predecessor(s10.hawaiian)}")
    print("\nSuccessor of s5:")
    print(f"- {db.successor(s5.hawaiian)}")
    print("\nMeHua search for 'ka':")
    for saying in db.mehua("ka"):
        print(f"- {saying}")
    print("\nWithWord search for 'storm':")
    for saying in db.withword("storm"):
        print(f"- {saying}")

if __name__ == "__main__":
    test_standard_case()
    #test_duplicate_case()
    #test_unicode_validity()
    #test_empty_tree()
    #test_large_quantity()
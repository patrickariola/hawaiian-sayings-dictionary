from lookup.database import SayingDatabase, Saying

# Initialize the database
db = SayingDatabase()

# ------------------------ REQUIRED TEST CASES ------------------------
# Insert 3 sayings
s1 = Saying(
    "ʻAʻohe hana nui ke alu ʻia",
    "No task is too big when done together",
    "ʻO ka hana nui, hiki ke hoʻopau ʻia me ka hui pū ʻana.",
    "Big tasks are possible when people work together."
)

s2 = Saying(
    "He aliʻi ka ʻāina",
    "The land is a chief",
    "He manaʻo e mahalo i ka ʻāina.",
    "Respect the land, for we serve it."
)

s3 = Saying(
    "E ʻai i kekahi, e kāpī i kekahi",
    "Eat one, salt the other",
    "E hoʻomākaukau no ka wā e hiki mai ana.",
    "Be prepared for the future."
)

db.insert_saying(s1)
db.insert_saying(s2)
db.insert_saying(s3)

# Ordered Set Operations
print("Member check (He aliʻi ka ʻāina):")
print(f"- {db.member('He aliʻi ka ʻāina')}")

print("\nFirst Saying in Hawaiian order:")
print(f"- {db.first()}")

print("\nLast Saying in Hawaiian order:")
print(f"- {db.last()}")

print("\nPredecessor of ʻAʻohe hana nui ke alu ʻia:")
print(f"- {db.predecessor('ʻAʻohe hana nui ke alu ʻia')}")

print("\nSuccessor of ʻAʻohe hana nui ke alu ʻia:")
print(f"- {db.successor('ʻAʻohe hana nui ke alu ʻia')}")

# Word Search Operations
print("\nMeHua search for 'hana':")
for saying in db.mehua("hana"):
    print(f"- {saying}")

print("\nWithWord search for 'land':")
for saying in db.withword("land"):
    print(f"- {saying}")
    
# ------------------------ EXTRA TEST CASES ------------------------

# ---------- Extra Test #1 ----------
print("\n--- Extra Test 1: Insert 2 more sayings (standard case of 5 total) ---")
s4 = Saying(
    "He pūkoʻa kani ʻāina",
    "A coral reef that grows into an island",
    "E ulu ana ka ʻike a me ka ikaika i ka manawa.",
    "Strength and knowledge grow over time."
)

s5 = Saying(
    "Kūlia i ka nuʻu",
    "Strive for the summit",
    "E hana me ka haʻahaʻa a me ka wiwoʻole.",
    "Strive with humility and courage."
)

db.insert_saying(s4)
db.insert_saying(s5)
print("- Inserted sayings 4 and 5")

# ---------- Extra Test #2 ----------
print("\n--- Extra Test 2: Duplicate insert (should overwrite old) ---")
duplicate = Saying(
    "He aliʻi ka ʻāina",
    "UPDATED translation of the land saying",
    "UPDATED Hawaiian explanation",
    "UPDATED English explanation"
)
db.insert_saying(duplicate)
print("- Duplicate inserted. Here's the updated version:")
print(f"- {db.member('He aliʻi ka ʻāina')}")
print(f"- {db.tree.search_saying('He aliʻi ka ʻāina').saying}")  # show updated saying

# ---------- Extra Test #3 ----------
print("\n--- Extra Test 3: Unicode validity test ---")
unicode_saying = Saying(
    "Aloha ʻoe",
    "Farewell to you",
    "He mele aloha e haʻi ana i ke aloha hope.",
    "A love song expressing farewell."
)
ascii_saying = Saying(
    "Aloha oe",
    "Goodbye (ASCII version)",
    "Plain version without diacritics.",
    "Simplified ASCII explanation."
)
db.insert_saying(unicode_saying)
db.insert_saying(ascii_saying)
print("- Inserted versions with and without ʻokina/macrons:")
print(f"- {db.member('Aloha ʻoe')}")
print(f"- {db.member('Aloha oe')}")

# ---------- Extra Test #4 ----------
print("\n--- Extra Test 4: Empty tree test ---")
empty_db = SayingDatabase()
print("- First (empty):", empty_db.first())
print("- Member (ʻAʻohe hana nui ke alu ʻia):", empty_db.member("ʻAʻohe hana nui ke alu ʻia"))
print("- MeHua (hana):", empty_db.mehua("hana"))

# ---------- Extra Test #5 ----------
print("\n--- Extra Test 5: Insert 20 sayings (scalability test) ---")
for i in range(1, 21):
    saying = Saying(
        f"Hawaiian Saying {i}",
        f"English Saying {i}",
        f"Explanation HAW {i}",
        f"Explanation ENG {i}"
    )
    db.insert_saying(saying)
print("- Inserted 20 additional sayings. Total should now exceed 25.")
print("- New first saying:", db.first())
print("- New last saying:", db.last())

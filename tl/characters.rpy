# Script for all characters.
# Defaulting player as not an imposter/not suspicious to 0,
# Find all the clues to win the case
default correct = 0

# Give the info and colour for each character

define GameDev = Character("Narrator") # Narrator for breaking the fourth wall

# Main Character, Nairda Nun
define nun = Character("Nairda Nun", color="#99C68E") #nun, frog green

# Husband of Nun
define hubby = Character("Strudle", color="#FF0000")#Red

# Late Police Detective Partner of Nun
define np = Character("Nun's Partner", color="#99C55E")
# Apartment neighbours
define t = Character("Tony", color="#FF0000")#Red
define e = Character("Ezekiel", color="#FFE4E1")#MistRose

# Misc characters
define a = Character("Alice", color="#33FFCC")#light blue
define d = Character("Detective", color="#FFCC33")#yellow
define po = Character("Police Officer", color="#800000")#maroon
define r = Character("Receptionist", color="AABBCC")
define drk = Character("Dr Krieger", color="FFCCAA")
define ch = Character("Chief", color="FFFFFF")

# images for characters and facial expressions
# General expressions:
# - neutral face
# - sad/crying
# - happy
# - angry
# - confused
# - embarrassed/shy

# Nun (Main Character)
image nun n:
    "nunneutral"
image nun sad:
    "nunsad"
    zoom 0.5
image nun happy:
    "nunhappy"
    zoom 0.5
image nun angry:
    "nunangry"
    zoom 0.5
image nun confused:
    "nunconfused"
    zoom 0.5
image nun shy:
    "nunshy"
    zoom 0.5

# Strudle Nun (Nairda's husband) PLACEHOLDERS REPLACEMENT NEEDED
image snun n:
    "snunneutral"
    zoom 0.2
image snun sad:
    "snunsad"
    zoom 0.2
image snun happy:
    "snunhappy"
    zoom 0.2
image snun angry:
    "snunangry"
    zoom 0.2
image snun confused:
    "snunconfused"
    zoom 0.2
image snun shy:
    "snunshy"
    zoom 0.2

# Dr Krieger (Therapist) PLACEHOLDERS REPLACEMENT NEEDED
image drk n:
    "drkn"
    zoom 0.5
image drk sad:
    "drksad"
    zoom 0.5
image drk happy:
    "drkhappy"
    zoom 0.5
image drk angry:
    "drkangry"
    zoom 0.5
image drk confused:
    "drkconfused"
    zoom 0.5
image drk shy:
    "drkshy"
    zoom 0.5

# Therapy Receptionist PLACEHOLDERS REPLACEMENTS NEEDED
image rec n:
    "receptionistn"
image rec sad:
    "receptionistsad"
    zoom 0.5
image rec happy:
    "receptionisthappy"
    zoom 0.5
image rec angry:
    "receptionistangry"
    zoom 0.5
image rec confused:
    "receptionistconfused"
    zoom 0.5
image rec shy:
    "receptionistshy"
    zoom 0.5

# Tony (apartment neighbour)
image tony n:
    "tonyneutral"
image tony sad:
    "tonysad"
image tony happy: #NEEDED
    "tonyshy"
image tony angry:
    "tonyangry"
image tony confused: #NEEDED
    "tonyshy"
image tony shy:
    "tonyshy"

# Ezekiel (Tony's nemesis and vice versa at apartments) PLACEHOLDERS REPLACEMENTS NEEDED
image ez n:
    "tonyneutral"
    zoom 0.5
image ez sad:
    "nunsad"
    zoom 0.5
image ez happy:
    "nunhappy"
    zoom 0.5
image ez angry:
    "nunangry"
    zoom 0.5
image ez confused:
    "nunneutral"
    zoom 0.5
image ez shy:
    "nunshy"
    zoom 0.5

# Dr Wolfe (Mortician)
image drwolfe n:
    "drwolfeneutral"
    zoom 0.5
image drwolfe sad:
    "drwolfesad"
    zoom 0.5
image drwolfe happy:
    "doctorwolfehappy"
    zoom 0.5
image drwolfe angry:
    "drwolfeangry"
    zoom 0.5
image drwolfe confused:
    "drwolfeconfused"
    zoom 0.5
image drwolfe shy:
    "drwolfeshy"
    zoom 0.5

# Chief (Police chief) placeholder, might be entirely unneeded, might not show chief
image chief n:
    "policeman"
image chief sad:
    "policeman"
    zoom 0.5
image chief happy:
    "policeman"
    zoom 0.5
image chief angry:
    "policeman"
    zoom 0.5
image chief confused:
    "policeman"
    zoom 0.5
image chief shy:
    "policeman"
    zoom 0.5

# Harry Hare (arrogant police detective) PLACEHOLDER NEEDS REPLACING
image hare n:
    "nunsad"
image hare sad:
    "nunsad"
    zoom 0.5
image hare happy:
    "nunhappy"
    zoom 0.5
image hare angry:
    "nunangry"
    zoom 0.5
image hare confused:
    "nunneutral"
    zoom 0.5
image hare shy:
    "nunshy"
    zoom 0.5

# Bruce (Nairda's nemesis at therapy) placeholder, might be entirely unneeded, might not show Bruce
image bruce n:
    "nunsad"
image bruce sad:
    "nunsad"
    zoom 0.5
image bruce happy:
    "nunhappy"
    zoom 0.5
image bruce angry:
    "nunangry"
    zoom 0.5
image bruce confused:
    "nunneutral"
    zoom 0.5
image bruce shy:
    "nunshy"
    zoom 0.5

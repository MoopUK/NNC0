# Script for all characters.
# Defaulting player as not an imposter/not suspicious to 0,
# Find all the clues to win the case
default correct = 0

# Give the info and colour for each character

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
    "nunneutral"
    zoom 0.5
image nun shy:
    "nunshy"
    zoom 0.5

# Strudle Nun (Nairda's husband) PLACEHOLDERS REPLACEMENT NEEDED
image snun n:
    "nunneutral"
image snun sad:
    "nunsad"
    zoom 0.5
image snun happy:
    "nunhappy"
    zoom 0.5
image snun angry:
    "nunangry"
    zoom 0.5
image snun confused:
    "nunneutral"
    zoom 0.5
image snun shy:
    "nunshy"
    zoom 0.5

# Dr Krieger (Therapist) PLACEHOLDERS REPLACEMENT NEEDED
image drk n:
    "nunshy"
image drk sad:
    "nunsad"
    zoom 0.5
image drk happy:
    "nunhappy"
    zoom 0.5
image drk angry:
    "nunangry"
    zoom 0.5
image drk confused:
    "nunneutral"
    zoom 0.5
image drk shy:
    "nunshy"
    zoom 0.5

# Therapy Receptionist PLACEHOLDERS REPLACEMENTS NEEDED
image rec n:
    "nunshy"
image rec sad:
    "nunsad"
    zoom 0.5
image rec happy:
    "nunhappy"
    zoom 0.5
image rec angry:
    "nunangry"
    zoom 0.5
image rec confused: #NEEDED
    "nunneutral"
    zoom 0.5
image rec shy:
    "nunshy"
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
    "doctorwolfneutral"
    zoom 0.7
image drwolfe sad:
    "drwolfsad"
    zoom 0.8
image drwolfe happy:
    "doctorwolfhappy"
    zoom 0.8
image drwolfe angry:
    "drwolfangry"
    zoom 0.8
image drwolfe confused: #NEEDED
    "nunneutral"
    zoom 0.5
image drwolfe shy:
    "drwolfshy"
    zoom 0.8

# Chief (Police chief) placeholder, might be entirely unneeded, might not show chief
image chief n:
    "doctorwolfhappy"
image chief sad:
    "nunsad"
    zoom 0.5
image chief happy:
    "nunhappy"
    zoom 0.5
image chief angry:
    "nunangry"
    zoom 0.5
image chief confused:
    "nunneutral"
    zoom 0.5
image chief shy:
    "nunshy"
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

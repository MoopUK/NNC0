# Script for all characters.
# Defaulting player as not an imposter/not suspicious to 0,
# Find all the clues to win the case
default correct = 0

# Give the info and colour for each character

# Main Character, Nairda Nun
define nun = Character("Nairda Nun", color="#99C68E") #nun, frog green

# Husband of Nun
define hubby = Character("Partner", color="#FF0000")#Red

# Apartment neighbours
define t = Character("Tony", color="#FF0000")#Red
define e = Character("Ezekiel", color="#FFE4E1")#MistRose

# Misc characters
define a = Character("Alice", color="#33FFCC")#light blue
define d = Character("Detective", color="#FFCC33")#yellow
define po = Character("Police Officer", color="#800000")#maroon
define r = Character("Receptionist", color="AABBCC")
define drk = Character("Dr Krieger", color="FFCCAA")

#images for characters

# Nun (Main Character)
image nun n:
    "nunneutral"
image nun sad:
    "nunsad"
    zoom 0.5
image nun angry:
    "nunangry"
    zoom 0.5
image nun happy:
    "nunhappy"
    zoom 0.5
image nun shy:
    "nunshy"
    zoom 0.5

# Tony (apartment neighbour)
image tony n:
    "tonyneutral"
image tony shy:
    "tonyshy"
image tony angry:
    "tonyangry"
image tony sad:
    "tonysad"

# Tony (apartment neighbour)
image drwolfe n:
    "doctorwolfneutral"
    zoom 0.7
image drwolfe shy:
    "drwolfshy"
    zoom 0.8
image drwolfe angry:
    "drwolfangry"
    zoom 0.8
image drwolfe sad:
    "drwolfsad"
    zoom 0.8
image drwolfe happy:
    "doctorwolfhappy"
    zoom 0.8

# Game by: Moop Open-source Games
# Nairda Nun - Chapter Zero (Demo)

# Game Demo summary: Introduction to Nairda Nun, the private detective.
# Based in the 90's, general crime type genre,
# all characters are animal-based, proportions and style similar to Sylvanian
# Families.

# -----------------------------------------------------------------------------
# Game Contents:

# SCENE 00 - Introduction
# 1. Shows Nairda Nun the frog solving a case
# 2. Shows Nairda Nun return home, introduces Tony the Beaver
# 3. Very mild introduction of Ezekiel and a feud between them and Tony

# SCENE 01 - Therapy and backstory told at Therapy
# 1. NN goes to the Therapist and talks about how their police detective partner
# who died when NN took their first day off work sick in over 30 years.
# 2. Therapist in current time explaining NN's OCD

# SCENE 02 - Murder Scene
# 1. Call to go to crime scene
# 2. Murder crime scene and investigation
# 3. Win / Fail the investigation

# Scene 03 - Ending/s
# 1. Win/Lose ending scene
# Demo End.

# -----------------------------------------------------------------------------

# The game/script starts here

# SCENE 00 - Introduction
# 1. Shows Nairda Nun the frog solving a case
# 2. Shows Nairda Nun return home, introduces Tony the Beaver
# 3. Very mild introduction of Ezekiel and a feud between them and Tony
label start:
    scene screenstart
    "Any similarities to real events are purely coincidental."
    "No real animals were dressed in tiny suits and forced to solve crimes in the making of this videogame."
    # PHOTO OF THE MODELS IN A CRIME SCENE SETTING
    scene screenstart1
    "Only fake ones."
    scene apartmenthalls
    play music "audio/cafe.mp3"
    show nun n at left with dissolve

    "(Looking at the dead body, Nairda whispers to themself)"
    nun "I think I left my oven on..."
    "(Their partner sighs deeply)"
    show snun angry at right with dissolve
    hubby "No no... I turned everything off before we left"
    "(Nairda looks around the room, then turns back to their partner)"
    show nun sad at left with dissolve
    nun "Are you sure?"
    show snun happy at right with dissolve
    hubby "Yes, I'm sure. I even disconnected the gas for you so you don't have to worry about anything"
    show nun n at left with dissolve
    nun "Well, in that case..."
    scene apartmenthalls
    "(A deep pause entered the apartment, everyone stopped talking to watch Nairda solve the case...)"
    show nun n at left with dissolve
    nun "The murderer wore slippers to not leave paw prints...
    They were waiting for her for at least an hour, and smoked! Horribly cheap cigarettes, terrible stuff..."
    "(They continue)"
    scene computerroom
    nun "After they killed Jane Doe, they checked her computer. Look at the chair,
    it's way too tall for a cat! The killer has to be at least 2ft 4... very tall, not a frog..."
    scene apartmenthalls
    show nun n at left with dissolve
    show drwolfe confused at right with dissolve
    mor "This is her apartment, isn't it? Why are we calling her a Jane Doe? Don't we have an ID?"
    nun "Yes, we do."
    play sound "audio/paper.mp3"
    "(Nairda passes her passport and several opened letter off to table to the mortician)"
    nun "It's Jane Doe"
    show drwolfe sad at right with dissolve
    "(The mortician looks at the victim's passport and opened letters)"
    mor "Damn, imagine calling you child the general term used for when we can't ID someone...
    They must have hated her"
    nun "Can I finish? I think I left my oven on, so I want to make this quick"
    show drwolfe shy at right with dissolve
    mor "Oh, yeah... sorry... How do you know they used the laptop?"
    show snun angry at right
    hubby "It isn't on! And I turned off the gas, remember?"
    "(Everyone looks at Nairda confused)"
    scene apartmenthalls
    show nun n at left
    "(Nairda Continues)"
    nun "The computer is wiped down clean, and the murderer is tall! At least 2 ft 4! Look at the computer chair!"
    nun "Who'd be able to use that? A giant, that's who!"
    "(Nairda smelled the air again)"
    nun "A dog. The murderer is a dog."
    "(Looking at the floor next to the window, Nairda tilts their head)"
    nun "Irish Wolfhound."
    show drwolfe n at right with dissolve
    mor "Her ex was an Irish Wolfhound!"
    show snun confused
    hubby "Jane Doe the cat was dating a dog? How odd!"
    mor "It's more common that you'd think actually..."
    scene apartmenthalls
    "(Pointing to dirt on the floor, and a clump of freshly shed fur, Nairda knew they found the murderer)"
    show nun n at left with dissolve
    nun "That fur belongs to an Irish Wolfhound, and it was raining earlier. There's a faint smell of wet
    dog on the computer chair. He must have needed something from the computer but..."
    show drwolfe n at right with dissolve
    mor "We can call the computer guys, see if there's a motive on there... Would you like to wait and.."
    "(Nairda interrupted the mortician)"
    nun "No, no no no I can't! I left the oven on! I can smell the gas from here!"
    "(Nairda quickly leaves the apartment whiles their partner follows behind)"
    scene apartmenthalls
    show snun angry
    hubby "You can NOT smell gas! We live across town! And I TURNED OFF YOUR GAS SUPPLY BEFORE WE
    LEFT! YOU'RE INSUFFERABLE!"
    scene apartmenthalls
    "(The police officers, detectives, and mortician in the apartment look in shock and awe)"
    show drwolfe shy at right
    mor "So that's Nairda huh?"
    show hare n at left
    d "Yeah, both impressive and kind of pathetic when you think about it"
    mor "I mean, he solved the case for us, you shouldn't be so harsh."
    scene apartmenthalls
    show drwolfe shy at right
    show hare angry at left
    d "I don't know what it is but he just rubs me the wrong way"

    "(Another Case Closed)"

    scene apartmentdoor
    "(Nairda Nun returns to his apartment building and see's his neighbour outside)"
    show nun happy
    nun "Hello, Tony!"
    show tony shy at left
    t "Hello, Mr Nairda!"
    "(Tony always loves seeing Nairda return home, probably one of the most exciting parts of his day)"
    show tony n at left
    "How was work, Mr Nairda? Did you solve any cases?"
    show nun happy at right
    nun "I did actually! But I needed to return home, I think I left the oven on..."
    play sound "audio/toiletnoise.mp3"
    "(Tony's head suddenly snaps upwards)"
    "(the noise from the pipes after someone flushing their toilet caused them to make the sound of running water)"
    show tony angry
    t "ARGH! WATER! That DAMN EZEKIEL! I've got to go Nairda! I have to stop the water!"
    scene apartmentdoor
    show nun n
    "(Looking into Tony's apartment, you see a makeshift dam covering the walls and ceiling)"
    "(As the door slams shut you hear a banging on the ceiling and murmuring, along with a faint 'fuck you, Tony!' coming from above)"
    show nun sad
    nun "And I thought I had issues..."
    "(Naida's partner comes running up behind them)"
    scene apartmentdoor
    show nun happy at right
    show snun n at left
    hubby "How did you get home before me? I drove and you RAN!?!"
    nun "I just... need to check if the oven is on"
    show snun angry at left
    hubby "Insufferable!"

# SCENE 01 - Therapy and backstory told at Therapy
# 1. NN goes to the Therapist and talks about how their police detective partner
# who died when NN took their first day off work sick in over 30 years.
# 2. Therapist in current time explaining NN's OCD

    # NEED THERAPIST OFFICE SCENE IMAGE RECEPTION && OFFICE ITSELF
    scene emptygym
    "(The next morning, at 9am on the dot, Nairda gets anxious)"
    show nun angry at left
    nun "Excuse me?"
    show rec happy at right
    "(The receptionist looks up)"
    nun "It's 9 o'clock."
    "(The receptionist gives a known look and sighs quietly)"
    show rec sad at right
    r "Yes, Mr Nun. I'm sure they'll be ready for you in a minute"
    nun "But my appointment starts at 9am, and it's 9 o'clock."
    "(She puts one of her paws over her face)"
    r "Shall we call your husband? He'll know what to do, whiles we wait for Dr Krieger"
    "(Nairda looks perplexed)"
    show nun sad at left
    nun "You're right, they will know what to do. Can you call them?"
    show rec n at right
    r "Of course, let's call your husband"
    "(She dials Nairda's husband on the landline, she doesn't need to look it up anymore, this
    happens so often that it's commited to her memory)"
    play sound "audio/ring.mp3"
    "(The phone rings)"
    hubby "Hello? Is everything alright?"
    r "Mr Nun's therapist is running a little late..."
    scene emptygym
    show nun angry at left
    nun "THREE MINUTES AND COUNTING!"
    show rec happy at right
    r "Yes, 3 minutes late, so we thought we'd call you!"
    "(She hands the phone over to Nairda)"
    scene emptygym
    show nun sad at left
    nun "Hello Strudel, my appointment starts at 9am, Dr Krieger knows it starts at 9am,
    I'm not sure what they could be doing but she knows it's 9am..."
    nun "I bet it's Bruce!"
    "(Nairda looks at the receptionist)"
    nun "Is it? Is it Bruce?"
    show rec angry at right
    "(She looks away)"
    r "You know I'm not allowed to discuss other patients with you, Mr Nun."
    "(Nairda looks at the receptionist, and then towards the therapist door, then
    talks down the phone in a hushed wisper)"
    scene emptygym
    show nun angry at left
    nun "It's definately Bruce!!!"
    scene emptygym
    show nun n at left
    "(As nun continues his conversation, being reassured by hubby, the door opens and the therapist
    peaks around the corner locking eyes with Nairda)"
    show drk n at right
    drk "I'm terribly sorry, Nairda. I had an emergency appointment over the phone."
    "(Nairda looks disgruntled as he hangs up the call)"
    nun "Bruce?"
    drk "You know I can't discuss other patients with you Nairda... Now come on in and let's get
    started!"
    "(They both enter the therapy office and take a seat)"

    # THERAPY START
    scene messhall
    show nun n at right
    show drk n at left
    drk "So, how's things?"
    nun "Things have been good! Very goo..."
    scene messhall
    show nun angry at right
    show drk n at left
    "(Nairda notices a cushion tilted to the side, whiles the other cushions on the sofa across
    the room are straight and evenly spaced apart)"
    nun "Is that on purpose?"
    "(Dr Krieger doesn't clock the sofa cushion until she turns to see it)"
    drk "It wasn't on purpose, no. Would you like me to fix it?"
    nun "No no, it's fine. It doesn't bother me, it's fine..."
    "(Nairda tries to look away but the compusion to correct the sofa is killing him)"
    nun "It's just... it doesn't bother me but it looks untidy..."
    "(Nairda goes over to the sofa and straightens the cushions)"
    nun "It doesn't bother me, it just looks untidy, you don't want people to think your
    therapy office is untidy... It'll look unprofessional..."
    scene messhall
    show nun n at right
    show drk n at left
    "(Now that Nairda has justified his compulsion the therapy continues)"

    # BACK STORY START
    drk "Let's talk about your partner"
    nun "My partner's fine, he'll be picking me up after this appointment"
    drk "No, I meant your partner when you were a detective on the force"
    "(Nairda looks perplexed, and remembers the case he never was never able to solve...)"

    # BACK STORY PARTNER DEATH
    scene apartmentlongshot
    "(One year ago)"
    "(Nairda looks as bad as he feels, slumped over the side of the bed he tries to
    pick the telephone up off the landline)"
    nun "I'm sorry, friend. I just can't join you at work today"
    np "Don't worry about it, you haven't taken a day off sick in over 30 years,
    you are allowed to take a break every once in a while, you know!"
    np "I'll come down and grab the keys, I can't be bothered dealing with public transport
    with all the horror stories I hear about the metro"
    "(Nairda's detective partner laughs softly)"
    np "Do you need anything bringing down whiles I'm here?"
    "(Nairda tries to look around groggily, then remembers he's out of milk and cereal)"
    nun "Not really, but could you bring down some milk and cereal? I might try to have breakfast later"
    "(His detective partner laughs again)"
    np "You and your cereal..."
    np "You'll look like a bowl of cereal if you keep this up!"
    np "I'll bring some cereal and milk down, and a few tins of soup too! Soup will do you good
    when you're sick."
    "(Nairda is too weak to argue his hatred of eating soup)"
    nun "Thanks, I appreciate this."
    "(They both hang up the phone and what felt like moments later Nairda's door opens and his
    partner walks inside with a goodie bag of ailments)"
    "(Along with some beloved milk and cereal for Nairda)"
    np "Here you go... oh WOW! You look awful! You really are sick!"
    "(Nairda is not sure whether to classify that reaction as a concern or an insult)"
    nun "..."
    np "I'll leave it over here for you, and don't get up. The milk will last a few hours out of the fridge.
    So I might as well leave it next to you with a bowl for when you're ready to try to eat something."
    "(They grab a bowl and spoon out of the kitchen and place it by Nairda's sofa where he currently resides)"
    "(Nairda weakly responds)"
    nun "Thanks, I appreciate this..."
    np "You're welcome, now where are the car keyssssssss? There!"
    "(They pick up the keys and head towards the door, waving the keys behind them as they walk away)"
    np "Get well soon, Bestie! I love you!"
    "(Nairda starts to have a coughing fit as the door closes)"
    nun "I lo... love you too.. aha..."
    "..."
    "(That was the last time they ever saw each other)"
    # Flashback end

    scene emptygym
    show nun sad at right
    show drk sad at left
    "(Nairda stops recalling the story, scratching at his hands to clean them)"
    drk "I think that's enough for today"
    scene emptygym
    show nun sad at right
    show drk happy at left
    drk "You've done good! I think we're making some real progress. I know it's hard but
    recalling these things can help you to move on and get over.."
    "(Nairda cuts them off)"
    scene emptygym
    show nun angry at right
    show drk happy at left
    nun "I can't get over it!"
    "(Dr Kreiger regrets her words, knowing it wasn't the best way to put it)"
    scene emptygym
    show nun sad at right
    show drk sad at left
    drk "No, I'm sorry... I shouldn't have worded it like that it was insensitive"
    drk "I'm just so used to working on the five stages of grief and it's been a year since the
    accident"
    drk "I'm just concerned that we never discuss it and, you might still be at stage one..."
    "(The town hall clock dings in the distance)"
    scene emptygym
    show nun sad at right
    show drk n at left
    drk "Ah, that time already? Well, I look forward to seeing you again soon. Try to take it easy
    and we'll pick up where we left off on Wednesday."
    "(Nairda leaves the office, and gets into his husband's car)"
    scene stairs
    show nun sad at left
    show snun n at right
    hubby "How did therapy go?"
    "(Nairda looks down to towards the car mat)"
    nun "Can we go home?"
    "(His husband can see it was a hard session)"
    scene stairs
    show nun sad at left
    show snun sad at right
    hubby "Of course! Let's go home."
    "(The Next Day)"
# Therapy End


# SCENE 02 - Murder Scene
# 1. Call to go to crime scene
# 2. Murder crime scene and investigation
# -- Stolen diamond/crystal opal, mace used to break the glass, opal had significant
# historical backstory.
# 3. Win / Fail the investigation
    scene apartmentdoor
    "(The phone rings)"
    d "There's been a murder robbery at the museum of Frogs and Fancies. The chief wants you to come over."
    show nun happy at left
    nun "We'll be right there!"

# Start of correct and incorrect answers in investigation

    scene messhall
    show nun n at left
    nun "So what was stolen?"
    show drwolfe  n at right
    mor "A giant opal. It's not that an opal was stolen though, this opal has historical significance!"
    "(They look around the room to check nobody is listening)"
    mor "It was the opal paid to the Frog King to end Frog War VI"
    "(Nairda remembers the history of Frog War VI, his father fought and died in Frog War VI when he was just a tadpole)"
    nun "How much was it worth?"
    mor "At least 12"
    "(Nairda twitches at the thought of having that much money, enough for a private pond at the Toadstool!)"

# CRIME SCENE: Look around
    show hare n
    d "Hurry up, the crime scene is just in here"
    mor "Ah, yes yes. Let's go in."
    scene library
    "(Once inside, there's several forensic owls and several areas of interest)"
    show nun n at right
# CRIME SCENE: First choice of investigation
    "Where do you want to look first?"
    menu:
        "Broken glass cabinet":
            $ correct = correct +1  #GOOD choice!
            play sound "audio/yes.mp3"
            jump BrokenGlassCabinet
        "Go outside the building":
            $ correct = correct -1  #BAD choice!
            play sound "audio/no.mp3"
            show hare  angry at right
            d "Why are you going outside? The crime scene is in here!"
            "(Nairda is taken back inside and approaches the broken glass cabinet)"
            jump BrokenGlassCabinet

# CRIME SCENE: Broken cabinet
label BrokenGlassCabinet:
    scene library
    show nun happy at left with dissolve
    show drwolfe  n at right
    nun "What was the glass was broken with?"
    mor "Well at first they tried their guns, but it's bullet proof glass so..."
    "(The mortician shrugs)"
    nun "At first? How did you figure out they used guns?"
    mor "There's small imprints on the glass, oh, and they left the guns behind"
    show gun gun
    "(The mortician points to the discarded guns next to the cabinet)"
    nun "Interesting..."
    scene library
    show nun happy at left
    show drwolfe  n at right
    mor "Oh, and one more thing, they also used those guns to kill the security guard"
    show body body
    "(The mortician points to a dead body in the corner that had clearly been shot)"
    scene library
    show nun confused at left
    show drwolfe n at right
    show body body
    nun "Shouldn't you be dealing with that instead of the robbery bit?"
    show drwolfe shy at right
    mor "I just... like watching you work. It's like a TV show!"
    show drwolfe happy at right
    mor "Besides, it's not like he's going anywhere"
    "(Nairda isn't sure what to think of this, and decides to just concentrate on the investigation at hand)"
    jump BackToTheCrimeScene

# CRIME SCENE: NEXT PART
label BackToTheCrimeScene:
    scene library
    "Where do you want to look next?"
    #Q1
    menu:
        "Open cabinet across the room":
            $ correct = correct +1  #GOOD choice!
            play sound "audio/yes.mp3"
            "Nairda looks at the open cabinet across the room"
            show nun confused at left
            nun "The cabinet is missing an object..."
            show drwolfe  n at right
            mor "So it is! Good eye!"
            show mace mace
            "(Nairda stares at the dust around the clean spot where the item used to be housed)"
            show nun n at left
            nun "Was it a mace?"
            mor "Well, this is where they kept the ye olde Frog War VI weapons, maces were a popular weapon
            back in the day."
            scene library
            menu:
                "Check the lock":
                    $ correct = correct +1  #GOOD choice!
                    show nun n at left
                    show drwolfe  n at right
                    play sound "audio/yes.mp3"
                    show opencab opencab
                    nun "It looks like it wasn't forced open..."
                    jump KeysUsed
                "Go back to the scene":
                    $ correct = correct -1 #BAD choice!
                    play sound "audio/no.mp3"
                    "(Nairda feel like you might have missed out on some evidence)"
                    "(It was probably nothing...)"
                    jump BackToTheCrimeScene2

        "Boot print on the floor":
            $ correct = correct +1  #GOOD choice!
            play sound "audio/yes.mp3"
            show boot boot
            "Looks like a boot print"
            show nun confused at left
            nun "Who wears boots?"
            nun "Unless they wanted to disgise what kind of feet they have!"
            show drwolfe angry at right
            mor "That's a good point! Only criminals use footwear!"
            jump BackToTheCrimeScene2
        "Wet Floor Sign":
            $ correct = correct -1 #BAD choice!
            play sound "audio/no.mp3"
            "(It's just a wet floor sign, with a comical rabbit falling on their butt)"
            "(Nairda feel like you might have missed out on some evidence)"
            "(It was probably nothing...)"

label KeysUsed:
    menu:
        "They used a key to get inside?":
            $ correct = correct +1 #GOOD Choice!
            play sound "audio/yes.mp3"
            show nun happy at left
            nun "They had the key to the weapon display? The culprit works here!"
            show drwolfe happy at right
            mor "You're right! I'll go check who has a copy of the keys"
            jump BackToTheCrimeScene2
        "Was it left unlocked?":
            show nun confused at left
            nun "Do you think this would be left unlocked?"
            show drwolfe n at right
            mor "It'd never be left unlocked! Everything here is a historical artifact, someone must have used a key!"
            jump BackToTheCrimeScene2

# CRIME SCENE: NEXT PART
label BackToTheCrimeScene2:
    scene library
    "Where do you want to look next?"
    menu:
        "CCTV Cameras":
            $ correct = correct +1 #Good Answer!
            play sound "audio/yes.mp3"
            show nun confused at left
            nun "Wait, there's CCTV?"
            show drwolfe sad at right
            mor "The tapes have been deleted, we can't look at them"
            nun "Hmmmm...... How do you get into the CCTV room?"
            mor "We had to call a security guard in, they're one of the only people with keys and access"
            nun "Who else has access?"
            show drwolfe n at right
            show nun n at left
            mor "Security and the two caretakers"
            jump caretakers
            label caretakers:
                menu:
                    "Hmm... probably wasn't the caretakers?":
                        scene library
                        $ correct = correct -1 #BAD Answer!
                        play sound "audio/no.mp3"
                        show hare angry with dissolve
                        d "Why not? They didn't show up to work today"
                    "Where are the caretakers?":
                        $ correct = correct +1 #Good Answer!
                        play sound "audio/yes.mp3"
                        show drwolfe shy with dissolve
                        mor "Of course!"
                        mor "They didn't even show up to work today!"
        "Shelf of dusty books":
            $ correct = correct -1 #BAD Answer!
            play sound "audio/no.mp3"
            "(The dusty books have nothing to do with the investigation.)"
            "(Nairda feel like you might have missed out on some evidence)"
            "(It was probably nothing...)"

    scene library
    "Where do you want to look next?"
    menu:
        "Ask about the Front Door lock":
            $ correct = correct +1 # GOOD Choice
            show doorlock doorlock
            show nun n at left
            show drwolfe happy at right
            play sound "audio/yes.mp3"
            nun "Do you know if the front door lock was messed with?"
            mor "It was open when we got here, but it doesn't look like anybody messed with it..."
            nun "Interesting..."

        "Ask about the light switches":
            $ correct = correct -1 # BAD Choice
            play sound "audio/no.mp3"
            nun "Does this place have a light switch?"
            show hare n with dissolve
            d "They're automatic lights, why?"
            nun "hmm... I dunno... fingerprints maybe..."
            "(Nairda feel like you might have missed out on some evidence)"
            "(It was probably nothing...)"

    "(Everyone gathers back at the lab to share what they've learned during the investigation...)"


#ENDINGS: This checks if Nairda gets the good ending solving the crime or the bad ending
    label which_end:
        if correct >= 3:
            jump good_end
        elif correct < 3:
            jump bad_end


# Scene 03 - Ending/s
# 1. Win/Lose ending scene
# Demo End.

# GOOD ENDING
label good_end:
    scene lab
    show nun happy at left with dissolve
    nun "The criminals were the caretakers at the Museum of Frogs and Fancies!"
    nun "Here's what happ..."
    GameDev "Shhh! Do you want me to get sued? Say something else!"
    scene lab
    show nun confused at left
    "(Nairda feels like they just heard the wrath of a... god? Actually, come to think of it, it sounded more like a sleep deprived games developer)"
    nun "(gulp)"
    scene lab
    show nun n at left
    nun "Here's... a summary of the crime?"
    "(Nairda looks around, seemingly safe to continue)"
    show boot boot
    nun "The caretakers snuck in after hours, wearing shoes to hide their foot prints"
    scene lab
    show nun n at left
    show gun gun
    nun "but they couldn't shoot open the case with their guns due to the bullet-proof glass"
    scene lab
    show nun n at left
    show mace mace
    nun "they needed to use something sturdier, like the maces kept in the weapons display!"
    scene lab
    show nun n at left
    show opencab opencab
    nun "With no forced entry, no CCTV footage, no locks broken on the cabinets... it was obvious they must work here!"
    nun "If they'd shot the weapon display open, or any of the locks! We probably wouldn't have clicked that the people worked here"
    scene lab
    show nun n at left
    "(The case was solved, shortly after giving in your report the two caretakers were found making a run for the hills)"
    "(Literally! The police have no jurisdiction on hills, nobody is sure why hills are a safe haven for crimes, probably a stupid old law, but thankfully they were caught before they made it to one)"
    scene lab
    show nun happy
    "(Well done, Nairda.)"
    return

# BAD ENDING
label bad_end:
    scene apartmenthalls
    show nun sad at right with dissolve
    nun "I feel like there were some clues I missed out on..."
    show hare angry at left
    d "You failed to catch the criminals"
    d "I always knew you were an idiot"
    "(The case was left unsolved, and the giant opal was never found)"
    return

# DEMO END
    # This is the end of the game.
    return

### NOTES FOR EXPANSION ON GAME:

## FUTURE THERAPY SESSION:
#    # Nairda is to wake up several hours later with banging on the door and dozens of missed calls from everyone
#    # their partner didn't die immediately, but in hospital, whiles Nun was still sleeping off their illness
#    # They were surrounded by everyone except Nairda. So heavy guilt encompasses him and the phobia of being ill
#    # is so extreme his OCD goes into overdrive.

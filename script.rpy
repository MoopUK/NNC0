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
    scene apartmenthalls
    play music "audio/cafe.mp3"
    ##play sound "audio/Narrator1.mp3"
    show nun n at left with dissolve
    show drwolfe n at right with dissolve

    "Looking at the dead body, Nairda whispers to themself"
    nun "I think I left my oven on..."
    "Their partner sighs deeply"
    hubby "No no... I turned everything off before we left"
    "Nairda looks around the room, then turns back to their partner"
    nun "Are you sure?"
    hubby "Yes, I'm sure. I even disconnected the gas for you so you don't have to worry about anything"
    nun "Well, in that case..."
    "A deep pause entered the apartment, everyone stopped talking to watch Nairda solve the case..."
    nun "The murderer wore slippers to not leave paw prints...
    They were waiting for her for at least an hour, and smoked! Horribly cheap cigarettes, terrible stuff..."
    "They continue"
    scene computerroom
    nun "After they killed Jane Doe, they checked her computer. Look at the chair,
    it's way too tall for a cat! The killer has to be at least 2ft 4... very tall, not a frog..."
    scene apartmenthalls
    show nun n at left with dissolve
    po "This is her apartment, isn't it? Why are we calling her a Jane Doe? Don't we have an ID?"
    nun "Yes, we do."
    "Nairda passes her passport and several opened letter off to table to the police officer"
    nun "It's Jane Doe"
    "The officer looks at the victim's passport and opened letters"
    po "Damn, imagine calling you child the general term used for when we can't ID someone...
    They must have hated her"
    nun "Can I finish? I think I left my oven on, so I want to make this quick"
    po "Oh, yeah... sorry... How do you know they used the laptop?"
    hubby "It isn't on! And I turned off the gas, remember?"
    "Everyone looks at Nairda confused"
    "Nairda Continues"
    nun "The computer is wiped down clean, and the murderer is tall! At least 2 ft 4! Look at the computer chair!"
    nun "Who'd be able to use that? A giant, that's who!"
    "Nairda smelled the air again"
    nun "A dog. The murderer is a dog."
    "Looking at the floor next to the window, Monknt tilts their head"
    nun "Irish Wolfhound."
    po "Her ex was an Irish Wolfhound!"
    hubby "Jane Doe the cat was dating a dog? How odd!"
    po "It's more common that you'd think actually..."
    "Pointing to dirt on the floor, and a clump of freshly shed fur, Nairda knew they found the murderer"
    nun "That fur belongs to an Irish Wolfhound, and it was raining earlier. There's a faint smell of wet
    dog on the computer chair. He must have needed something from the computer but..."
    po "We can call the computer guys, see if there's a motive on there... Would you like to wait and.."
    "Nairda interrupted the police officer"
    nun "No, no no no I can't! I left the oven on! I can smell the gas from here!"
    "Nairda quickly leaves the apartment whiles their partner follows behind"
    hubby "You can NOT smell gas! We live across town! And I TURNED OFF YOUR GAS SUPPLY BEFORE WE
    LEFT! YOU'RE INSUFFERABLE!"
    "The police officers and detectives in the apartment look in shock and awe"
    d "So that's Nairda huh?"
    po "Yeah, both impressive and kind of pathetic when you think about it"
    d "I mean, he solved the case for us, you shouldn't be so harsh."
    po "I don't know what it is but he just rubs me the wrong way"

    "Case Closed"

    scene workhalls
    "Nairda Nun returns to his apartment building and see's his neighbour outside"
    show nun happy
    nun "Hello, Tony!"
    show tony shy at left
    t "Hello, Mr Nairda!"
    "Tony always loves seeing Nairda return home, probably one of the most exciting parts of his day"
    show tony n at left
    "How was work, Mr Nairda? Did you solve any cases?"
    show nun happy at right
    nun "I did actually! But I needed to return home, I think I left the oven on..."
    "Tony's head suddenly snaps upwards, the noise from the pipes after someone flushed their toilet caused them to make the sound of running water"
    show tony angry
    t "ARGH! WATER! That DAMN EZEKIEL! I've got to go Nairda! I have to stop the water!"
    scene workhalls
    show nun n
    "Looking into Tony's apartment, you see a makeshift dam covering the walls and ceiling"
    "As the door slams shut you hear a banging on the cieling and murmuring, along with a faint 'fuck you, Tony!' coming from above"
    show nun sad
    nun "And I thought I had issues..."
    "Naida's partner comes running up behind them"
    scene workhalls
    show nun happy at right
    show tony angry at left
    hubby "How did you get home before me? I drove and you RAN!?!"
    nun "I just... need to check if the oven is on"
    hubby "Insufferable!"

# SCENE 01 - Therapy and backstory told at Therapy
# 1. NN goes to the Therapist and talks about how their police detective partner
# who died when NN took their first day off work sick in over 30 years.
# 2. Therapist in current time explaining NN's OCD

    # NEED THERAPIST OFFICE SCENE IMAGE RECEPTION && OFFICE ITSELF
    scene emptygym
    "The next morning, at 9am on the dot, Nairda gets anxious"
    show nun angry at left
    nun "Excuse me?"
    "The receptionist looks up"
    nun "It's 9 o'clock."
    "The receptionist gives a known look and sighs quietly"
    r "Yes, Mr Nun. I'm sure he'll be ready for you in a minute"
    nun "But my appointment starts at 9am, and it's 9 o'clock."
    "She puts one of her hands over her face"
    r "Shall we call your husband? He'll know what to do, whiles we wait for Dr Krieger"
    "Nairda looks perplexed"
    show nun sad at left
    nun "You're right, they will know what to do. Can you call them?"
    r "Of course, let's call your husband"
    "She dials Nairda's husband on the landline, she doesn't need to look it up anymore, this
    happens so often that it's commited to her memory"
    "The phone rings"
    hubby "Hello? Is everything alright?"
    r "Mr Nun's therapist is running a little late..."
    nun "THREE MINUTES AND COUNTING!"
    r "Yes, 3 minutes late, so we thought we'd call you!"
    "She hands the phone over to Nairda"
    nun "Hello hubby, my appointment starts at 9am, Dr Krieger knows it starts at 9am,
    I'm not sure what he could be doing but he knows it's 9am..."
    nun "I bet it's Bruce!"
    "Nairda looks ar the receptionist"
    nun "Is it? Is it Bruce?"
    "She looks away"
    r "You know I'm not allowed to discuss other patients with you, Mr Nun."
    "Nairda looks at the receptionist, and then towards the therapist door, then
    talks down the phone in a hushed wisper"
    nun "It's definately Bruce!!!"
    "As nun continues his conversation, being reassured by hubby, the door opens and the therapist
    peaks around the corner locking eyes with Nairda"
    drk "I'm terribly sorry, Nairda. I had an emergency appointment over the phone."
    "Nairda looks disgruntled as he hangs up the call"
    nun "Bruce?"
    drk "You know I can't discuss other patients with you Nairda... Now come on in and let's get
    started!"

    # THERAPY START
    drk "So, how's things?"
    nun "Things have been good! Very goo..."
    "Nairda notices a cushion tilted to the side, whiles the other cushions on the sofa across
    the room are straight and evenly spaced apart"
    nun "Is that on purpose?"
    "Dr Krieger doesn't clock the sofa cushion until he turns to see it"
    drk "It wasn't on purpose no. Would you like me to fix it?"
    nun "No no, it's fine. It doesn't bother me, it's fine..."
    "Nairda tries to look away but the compusion to correct the sofa is killing him"
    nun "It's just... it doesn't bother me but it looks untidy..."
    "Nairda goes over to the sofa and straightens the cushions"
    nun "It doesn't bother me, it just looks untidy, you don't want people to think your
    therapy office is untidy... It'll look unprofessional..."
    "Now that Nairda has justified his compulsion the therapy continues"
    # BACK STORY START
    drk "Let's talk about your partner"
    nun "My partner's fine, he'll be picking me up after this appointment"
    drk "No, I meant your partner when you were a detective on the force"
    "Nairda looks perplexed, and remembers the case he never was never able to solve..."
    # BACK STORY PARTNER DEATH
    "One year ago"
    "Nairda looks as bad as he feels, slumped over the side of the bed he tries to
    pick the telephone up off the landline"
    nun ""

# SCENE 02 - Murder Scene
# 1. Call to go to crime scene
# 2. Murder crime scene and investigation
# 3. Win / Fail the investigation
    scene messhall
# Start of correct and incorrect answers in investigation
    "next scene time"
    #play sound "audio/bell.mp3"
# ONE: ALICE
    "QUESTION"
    show tony n with dissolve
    a "ALICE TEXT"
    #INTRO
    menu:
        "ANSWER 1":
            ##play sound "audio/Narrator17.mp3"
            t "TONY NOISES"
        "...":
            show tony n with dissolve
            ##play sound "audio/Narrator18.mp3"
            t "TONY NOISES 2"


    show tony n with dissolve
    a "QUESTION TWO?"
    #Q1
    menu:
        "BEEP BOOP LETTUCE ANSWER BAD":
            $ correct = correct -1  #BAD Answer!
            show tony n with dissolve
            a "heh"
        "BAD ANSWER TWO!":
            $ correct = correct -1  #BAD Answer!
            show tony n with dissolve
            a "hmm...?"
        "GOOD ANSWER ONE":
            $ correct = correct +1 #Good Answer!
            show tony n with dissolve
            a "Good answer noises!"

    show tony n
    #Q2
    a "QYUESTION AGAIN?"
    menu:
        "GOOD ANSWER!":
            $ correct = correct +1 #Good Answer!
            jump answer1
            label answer1:
                a "EXTRA Q?"
                menu:
                    "Bad answer":
                        $ correct = correct -1 #BAD Answer!
                        show tony n with dissolve
                        a "Hm.."
                    "GOOD ANSWER":
                        $ correct = correct +1 #Good Answer!
                        show tony n with dissolve
                        a "Of course!"
        "HALF GOOD ANSWER":
            a "Half good answer reply"

    #Q3
    a "QUESTION QUESTION"
    menu:
        "NEUTRAL REPLY.":
            a "!"
            show tony n with dissolve
            "..."
        "NEUTRAL ANS":
            a "!"
            show tony n with dissolve
            "NEUTRAL"

    "Case solved?"
#Checking for if good or bad end
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
    nun "Good End"
    return

# BAD ENDING
label bad_end:
    scene apartmenthalls
    show nun happy at right with dissolve
    show nun happy at left with dissolve
    nun "Bad end"
    ##play sound "audio/badEnd2.mp3"
    return

# DEMO END
    # This is the end of the game.
    return

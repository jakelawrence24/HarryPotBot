import random
import threading
import smtplib

# content
punList = ["Why does voldemort only use twitter not facebook? \n\nBecause he only has followers not friends.",
           "On a scale from one to ten, how obsessed with Harry Potter are you? \n\nAbout nine and three quarters."
           "Why did Professor Snape stand in the middle of the road?\n\nSo you'll never know which side he's on.",
           "What do you call a Hufflepuff with one brain cell?\n\nGifted.\n\nWhat do you call a Hufflepuff with two brain cells?\n\nPregnant.",
           "How many Muggles does it take to screw in a lightbulb?\n\nOne. It is the only thing they are good for.",
           "How can you tell which Harry Potter movie you are watching\n\nBy the size of Hermione Granger's breasts!",
           "You don't get my Harry Potter jokes?\n\nThere must be some thing RON with you.",
           "Why was Harry Potter sent to the office?\n\nBecause he was cursing in class!",
           "Why doesn't Voldemort have glasses?\n\nNobody nose.",
           "What do you call a Persian who smokes pot?\n\nHarry Potter",
           "How does Harry Potter get rid of a rash?\n\nWith quit-itch.",
           "How do you know if someone's a pureblood?\n\nDon't worry they'll let you know.",
           "What did the comedian say to Harry Potter?\n\nWhy so Sirius?",
           "What did the golden snitch say when Harry Potter was itchy?\n\nQuidditching!",
           "How many Hufflepuffs does it take to screw in a lightbulb?\n\nAll of them.",
           "Why does Sirius Black have so many girlfriends?\n\nOnce you go black you siriusly dont go back! ",
           "Why did Harry Potter cross the road?\n\nNo reason, but someone will write fan fiction about it.",
           "Have you heard about the new X rated Harry Potter movie?\n\nHairy Cooter and the Sorcerer's Bone",
           "Why did Death Eaters cross the road?\n\nThe Dark Lord ordered it.",
           "What does Harry Potter have that Voldemort doesn't?\n\nA nose.",
           "How do Death Eaters freshen their breath?\n\nWith Dementos.",
           "What do you call a movie about Daniel Radcliffe getting high?\n\nHarry Pothead.",
           "What do you call a potterhead on a horse?\n\nHarry Trotter.",
           "Did you survive Avada Kedavra?\n\nCause your drop dead gorgeous.",
           "A hufflepuff, ravenclaw, and a gryffindor girl are first years; which one is the sexiest?\n\nThe hufflepuff, because she is the only one that's 17.",
           "I named my lizard 'Harry' just so I can say 'Your a lizard Harry!'",
           "If your boyfriend looks like Oliver Wood, he's probably a keeper.",
           "Knock Knock\n\nWho's there?\n\nYou Know!\n\nYou Know Who?\n\nExactly",
           "Roses are red\n\nViolets are blue\n\nI thought voldemort was ugly\n\nBut then I saw you.",
           "Voldemort: Why so sirius?\n\nSirius Black: Why so nosy?",
           "Luna Lovegood: 'I slept with a Brazilian....'\n\nHufflepuff: 'Oh my God! You slut! How many is a brazilian?'",
           "Yo momma's so fat the sorting hat put her in all of the houses.",
           "Yo momma's so fat her patronus is a milkshake.",
           "Yo mama's a whore-crux.",
           "I heard you're a Gryffinwhore (Why?) \n\nBecause you let every wizard Slytherin!",
           "My name might not be Luna, but I sure can Lovegood",
           "I wanna stick my Sorcerer's Stone in your Chamber of Secrets and release The Prisoner of Azkaban into your Goblet of Fire giving the Order of the Phoenix making my Half Blood Prince rise and give you the Deathly Hallows",
           "I'd like to get my basilisk into your chamber of secrets",
           "My wand has chosen you!",
           "Save a broom; ride a Quidditch player",
           "Hey, baby; I must be in the Room of Requirement, because I require YOU!",
           "Want to learn to speak troll? Don't worry I can get you grunting in no time.",
           "I'll remember to protect my wand when entering your chamber of secrets!",
           "Lets practice Alohomora...you can be the door so I can slam you all I want!",
           "Would you like to whomp my willow?",
           "Let me Slytherin your Griffendoor.",
           "I'm not wearing an invisibility cloak, but do you think I could still visit your restricted section tonight?",
           "I wanna be your Dumblewhore",
           "My love for you burns like a dying phoenix.",
           "Why did Barty Crouch Jr. quit drinking?\n\nBecause it was making him Moody.",
           "So, Harry Potter and the Order of the Phoenix.\n\n I guess that's when the books started getting Dead Sirius",
           "One day Lupin decides to come clean with Harry. He sits him down and tells him 'Harry, I'm a werewolf'. Harry jumps up and starts shouting 'WHAT!? ARE YOU FUCKING SERIOUS!?' Lupin sighs, hangs his head and mumbles 'Ah yes, that too'",
           "How many Harry Potters does it take to screw in a lightbulb?\n\n1 - he holds it and the world revolves around him.",
           "How many wizards does it take to screw in a lightbulb?\n\nTwo. One to hold the bulb. One to rotate the room.",
           "How many Purebloods does it take to screw in a lightbulb?\n\nWhat's a lightbulb?",
           "How many Gryffindors does it take to screw in a lightbulb?\n\nThree. And you know who they are.",
           "A blind wizard walks into a bar, finds his way to a stool and sits down. He says rather loudly to the bartender, 'Hey, how would you like to hear a Hufflepuff joke?' The bar goes silent and the barkeep replies, 'Sir, I will not lie to you, you are speaking to a Hufflepuff, the man behind you is an Auror from Hufflepuff, the woman to your right is a Hufflepuff dueling champion and we all have our wands drawn. Do you really want to continue?' The blind wizard goes silent for a moment before curtly replying, 'No I don't. Not if Im going to have to explain it 3 times.'",
           "How do the Malfoys enter a building?\n\nThey Slytherin.\n\nAlternatively, how do they get into bed? ;)",
           "A joke?\n\nThe Weasley's bank account. :'(",
           "What did Voldemort tell Wormtail when they went bowling?\n\nKill the spare.",
           "Yo momma is so ugly, even the whomping willow wouldn't hit that.",
           "Harry Potter is sliding down a hill.\n\nJ.K. Rowling.",
           "What do you call a toilet with fur?\n\nA Harry Potter",
           "How do you get a mythical creature into your house? \n\nThrough the Gryffindor!",
           "I haven't been to platform 9 and 3/4 but I know something else with that measurement.",
           "What do you call a Hufflepuff that works out?\n\nHufflebuff",
           "What is born with eight legs, has four after the first year of its life, and then only two after twenty years?\n\nThe Weasley twins.",
           "I don't see why people are just now saying Emma Watson is hot when I've been saying it for 15 years.",
           "Yo mamma's so fat, her boggart is a treadmill.",
           "Ron: Period! \n\nHermione: I thought your catchphrase was Bloody Hell?\n\nRon: Same Thing",
           "Why did Harry cross the road?\n\nHe needed too, but somebody is gonna write a book about it.",
           "Why did Crabbe and Goyle cross the road?\n\nBecause Draco did.",
           "How do you keep a Hufflepuff in suspense?\n\n*walks away*",
           "Professor Hooch: Now once you've got a hold of your broom, I want you to mount it. Grip it tight. You don't want to fall off the end.\n\nMichael Scott: That's what she said.",
           "If you're having quidditch problems I feel bad for you son,\n\nI've got 99 problems but a snitch ain't one",
           "Snape: Headmaster, The dark lord has returned\n\nDumbledore: Are you serious?\n\nSnape: No, I'm Severus",
           "Voldemort: So I just have to lie?\n\nPinocchio: Yup!",
           "Ron: Hermione, how many bones do you have in your body?\n\nHermione: Um, 206.\n\nRon: You want one more?",
           "The Dursleys went to Penn State"
           ]
# subjects
subList = ["Surprise it's HarryPotBot!",
           "HarryPotBot Strikes again!",
           "It's HarryPotBot...Bitch.",
           "The Bot who Lived!",
           "Hogwarts School of Trollcraft and Bottery!",
           "HarryPotBot is the greatest HufflePuff of all time.",
           "HarryPotBot knows who did Harambe; It was Penn State",
           "Will the real HarryPotBot please stand up?",
           "HarryPotBot has the biggest wand.",
           "HarryPotBot has a Hairy bot",
           "HarryPotBot has a nose, smd voldemort",
           "HarryPotBot can Lovegood",
           "HarryPotBot knows who did JFK; It was Penn State",
           ]
# signatures
sigList = ["Long live Hufflepuff",
           "Love",
           "+1 Hufflepuff",
           "Slytherin sucks",
           "Gryffindor has gonnorrhea",
           "Ravenclaw has rabies",
           "Yours truly",
           "Expecto Patronum",
           "Avada Kedavra",
           "Lumos",
           "Never trust a Malfoy",
           "RIP Harambe",
           "Screw Voldemort"
           ]
contentList = ['']

def g():
    # randomizing variables
    r = random.randint(0, len(punList) - 1)
    s = random.randint(0, len(subList) - 1)
    f = random.randint(0, len(sigList) - 1)
    # length of the interval for which the function repeats
    t = 86400

    # the email address of the account of which the email is being sent from
    senderEmail = ""
    # the password of the account of which the email is being sent from
    senderPass = ""
    # the email address of the account of which the email is being sent to
    recieverEmail = ""
    # stylistic break within the email
    lineBreak = "-----------------\n"
    # formatting of the content within the email
    content = punList[r] + "\n" "-------------------------------"+ lineBreak + sigList[f] + "," + "\nHarryPotBot\n" + lineBreak + "Total Points earned for Hufflepuff by HarryPotBot: %s" % (len(contentList) + 1)
    # adds the most recent email to the list of sent emails to log sent data
    contentList.append(content)
    # initialization of email server
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    # initialization of the mail driver
    mail.ehlo()
    mail.starttls()
    # complete formatting of message
    message = 'Subject: %s\n\n%s' % (subList[s] + " -- HPB #%s" %(len(contentList)), content)
    # mail sender info
    mail.login('senderEmail', 'senderPass')
    # sending mail to specified parameters
    mail.sendmail('senderEmail', 'recieverEmail', message)
    # drags out the end of the function for t seconds
    threading.Timer(t, g).start()

# start calling f now and every t sec thereafter
g()

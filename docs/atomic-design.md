# Atomic Design... and You!

I first discovered the concept of the atomic design pattern in 2018.  I thought it was rather novel and an interesting approach to questions about how to structure modules and packages hierarchically.

I liked it a lot so I decided to play with it a bit.  It managed to stick.

The question now is, "How is the concept of "atomic design" used within Automancy?"

## It's Simple
Answer: Barely...

Jokes aside, unless you're just a super documentation nerd (like me), you're probably not reading this doc right now.  But since you are reading this doc right now, that's right, you guessed it, NERD ALERT!!!

Ok, so I guess that last line wasn't really "jokes aside", so sue me.  It's 12:24am, I'm deep into my second Honey Jack and Ginger, it's my documentation, I'll joke if I want to!

Alright alright, here's how it works.

There are three rules for three classifications

1. Atoms are unitary Elementals which can't have children (so sad).  They are objects like Buttons, TextInputs, etc.  They're about as simple as you can get.
2. Molecules are simple Elementals which tend to contain two or three Atoms.  A Form will likely only have a handful of Atom objects as children.
3. Organisms are complex Elementals which can be comprised of many Molecules with children of their own and/or Atoms, and tend to allow for Options Objects (more on those later)

## Motivation
There are many levels of cognitive complexity when it comes to modeling an entire web application.

While from a top level perspective, most users might not ever know that there is an Atomic Design hierarchy of modules within this framework, for those potentially interested in making modifications this is useful knowledge.

My aim was to structure modules within packages in a way that makes sense within a system objects of increasing complexity.

## OptionsObjects (A Brief Overview)
The topic of OptionsObjects will be covered more fully in a different document, but I felt it's worth mentioning here as an aside because of the nature of the "Organism" class of objects.

There are a few objects in Automancy which are so complex, they warrant their own special object meant to store optinos which can be injected upon instantiation.

Only Molecules have the level of complexity as an interface to real world DOM constructs.

As an example, think of a generic Clock or Calendar picker on any given website you've visited.

Think of all the little buttons and sub features of a Calendar or Clock.  The further you consider, the more obviously complex a Calendar or Clock becomes; there are many relationships between elements.

Rather than require a billion input arguments to the Calendar or Clock classes during instantiation, "OptionsObjects" (where appropriate) are available for these Organisms.

These OptionsObjects are just storage for additional locators (mostly), ready to be used for the instantiation of an Organism type object. (Gotta catchem' all!)

That's it, I just wanted to point out nothing less complex than an organism object will have an OptionsObject which is an important distinguishing factor for graduation to a higher tier type within Atomic Design (as I see fit MWAHAHAHAHAHA!!!!!!)
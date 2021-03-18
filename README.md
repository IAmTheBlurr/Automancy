# Automancy
A UI Automation toolset for Python designed to greatly simply the functionality and features of Selenium.

## Motivation
Selenium sucks to work with, we all know it.  It's cumbersome to write, abstract in the not-so-fun way, difficult to read (thus to maintain), and rather fragile.

Automancy was designed to resolve all of these annoyances, regardless of if you're intent is to scrape web pages, automate actions on a web portal, or create automated UI tests.

The sad part is most people don't realize how easy these things can be.  They just put up with suffering through these ailments, claiming "that's just the way it is".

It's just not true, it can be a different way.  To prove it, let me show you a world.  Shining, shimmering, splendid, on an Automancy carpet ride...

Yes, I went there!

## Pre-requisites
You'll need to have your favorite 

## Installation

    pip install automancy

_(What?  You thought they would be more?)_

## First Example
There are many ways Automancy can be used, various styles of implementation supported, it all depends on the needs of your context.

In this example scenario, we're going to automate a few actions for Wikipedia because we want to see if anyone has written a page for Automancy yet.

Only a few Elementals are used, and we're going to use the `.add(...)` method of the `Page` class to automatically associate each of our Elementals with an instance of `Page` called `wikipedia`.

We'll discuss other strategies for associating Elements with one another in other documentation later on.  It's pretty cool stuff.

A special thing to note.  You'll notice there is no passing of the `driver` object to any further object in the scope.  You might be wondering how it's possible that any of the Automancy Elemental objects are able to control the driver instance.  Automancy includes some special sauce which detects for an instance of a driver object within the scope of the script/environment it's objects run in.  This will be discussed in greater detail elsewhere.

_Note: The current version of Automancy still requires the manual instantiation of a Selenium WebDriver object but this will not be true for much longer._

    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    from automancy import Button, Label, Page, TextInput

    # Instantiate a Chrome WebDriver
    driver = webdriver.Chrome(options=webdriver.ChromeOptions(), desired_capabilities=DesiredCapabilities.CHROME)

    # Instantiate a Page object with the wikipedia main url
    wikipedia = Page(url='https://en.wikipedia.org/wiki/Main_Page')

    # Add the necessary Elementals to the wikipedia page.
    wikipedia.add(Button('//input[@id="searchButton"]', 'Search Button', 'search_button'))
    wikipedia.add(TextInput('//input[@id="searchInput"]', 'Search Input', 'search_input'))
    wikipedia.add(Label('//p[@class="mw-search-nonefound"]', 'Not Found Text', 'not_found_text'))

    # Go to the wikipedia main page
    wikipedia.visit()
    
    # Input the search text
    wikipedia.search_input.write('Automancy')
    
    # Click the search button
    wikipedia.search_button.click()
    
    # Check to see if the "not found" text still exists
    if wikipedia.not_found_text.exists
        print('Forever alone...')

## Project Structure
This section outlines the high level thinking about the design of the modules, and the directory structure employed.

Deeper descriptions of each module will be found further down below this section

### Core
The core modules are in many ways the beating heart of Automancy.  The modules in this directory are fundamental to the operations of every module which is meant for humans to interact and write code with.

Some core modules are exposed to be easily accessed from the top level of Automancy while others are not.  Those which are not easily importable are simply accessed by other modules directly, not really being meant for direct user access.

More details about this later.

### Ecosystems
Think of the term "ecosystem" in the natural sciences.  What is an ecosystem?  It's a domain of life generally speaking, a domain of complex entities interacting with each other, usually with some sort of hierarchical relationship between everything within the domain.

This analogy is used here in Automancy.  A single web page can be thought of as an ecosystem.

Simple ecosystems might only contain some text, a picture, and a button to interact with, while complex ecosystem might have animations, triggered DOM changes, modals, toast messages, video playback, etc.

The practice of Automancy is the practice of defining what exists in an ecosystem as a "model" of reality (or at least as close to it as you might need).

We'll cover more about the subject of constructing models of reality as "ecosystems" a bit later on.

### Elementals
If a web page is a complex ecosystem as in nature, you can think of what lives on a web page, the unique constituents of a DOM, as complex organisms, molecular structures, and atomic elements, embedded within each other as complexity decreases.

For this reason, Automancy considers this hierarchical structure for its module and directory path conventions.

#### Atoms
These are the least complex modules.  Each represent a single web element DOM object; a `<button`, or an `<a>`, but also including simple things like a checkbox, radio selector, or a text input field.  "Atom" modules are the smallest objects in Automancy

#### Molecules
Molecules are the second smallest objects in Automancy.  These modules are meant to be used when constructing models of DOM structures such as `<form>`, a modal, a dialogbox.

Molecule objects tend to be made up of Atomic objects which are bounded by some kind of containing web element.

#### Organisms
Some Elementals you'll use to build UI models are complex enough to have their own internal object models to represent what you'd expect to see in the real world.

The `Table` and `Grid` `HTML5VideoPlayer` Elementals are two such "Organism" type objects.

Organism modules usually contain methods for constructing xpath selectors for their children DOM elements, so you don't have to do the work of arduously defining the nitty-gritty details of each `<tr>` and `<td>`, the organism modules do that work for you with the least amount of effort on your part.  

## Examples
Alright, on to the fun bits!

### Elementals
Something

### Browser
Something

### Model
Something

### Tactical Asserts
Something

### External Javascript
Dark Side
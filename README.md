# Automancy
A UI Automation toolset for Python designed to greatly simply the functionality and features of Selenium.

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
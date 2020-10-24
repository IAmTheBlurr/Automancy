# Ecosystem Pattern
## Definitions
An "Ecosystem" in this context is a complex, self-contained, model based representation of the 'thing' you want to interact with.

What does this mean exactly?

Let's say you have a web app to test.  There are many pages, components, features, etc.  There is naturally a hierarchy of objects, inputs within forms within menus within pages, etc.

For each unique component, you create a model in code to match what the component looks like, how it functions, and what elements the component contains as children.

You are building meta-models to mirror what you intend to interact with.

There is more.

An ecosystem is more than just models, it contains other non-model "living parts".  In the context of Automancy, an ecosystem contains it's own webdriver instance, it's own desired capabilities, etc.

An ecosystem must contain everything it needs to act against the system it models with no further outside additional instantiations.

An ecosystem must be a single instantiatable object which builds its internal objects only upon instantiation and where it's internal properties (recursively) cannot be modified after instantiation.

An analogy would be the input parameters of the ecosystem being like people entering a bio-dome for an isolation experiment, you can't just swap them out without tearing down the whole thing and starting from scratch.

## Inside an Ecosystem
There may be internal properties regarding state or conditions inside the ecosystem which can be viewed from the outside but only modifiable from the inside.

Ecosystems must not allow external actors to enter an instance after instantiation.  Raw data as primitives can sometimes be acceptable but not if those values are stored.

Ecosystems can have unified state actions or "reports" which can be triggered through definable protocols passed in upon instantiation.  Protocols cannot be modified after however.

## Model Constructs
Models must be constructed programmatically through the use of an `.dd(...)` or `.include(...)` method which takes at least three parameters
1. The object type (instance) being added (e.g., Button, TextInput, etc)
2. A locator string (i.e., xpath) for the object
3. A human-readable name for the object

Optionally, a fourth parameter of a system-readable name string can be implemented, however, it is sufficient to uniformly transform and store the human readable name into a system-friendly name string.

Models must be constructed hierarchically such that a model object only contains definitions for it's children (and by extension it's grandchildren), never to it's siblings or ancestors.

The motivation for this is for the automatic concatenation of hierarchically structured xpath strings as sophisticated and increasingly accurate node selectors.

The mechanism prepends the locator of the parent object to the child object(s) and acts recursively so the order of when models are instantiated doesn't affect the true xpath locator hierarchy.

There must be additional rules to govern hierarchy structure which is based on complexity for model object types.  Objects of greater complexity must not be added as children to objects of lower complexity (I.E., Buttons can be added to a Form but a Form cannot be added to a Button).

## Options Objects
Some objects of significant complexity may require or allow for an Options Object to be provided during instantiation which contain additional properties specifically important to the operation of the complex object.

Examples of these are:
- Clock
- Grid
- Table
- Calendar

An Options Object usually provides additional locators for elements commonly expected to exist.  Specific examples will be covered in How-Tos to come.
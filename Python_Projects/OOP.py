class Animal:
    def __init__(self, name="default", size="default", color="default"):
        self.name = name
        self.size = size
        self.color = color

    def action(self, animal_action):
        return animal_action


class Dog(Animal):
    def __init__(
        self, name="default", size="default", color="default", breed="Unknown"
    ):
        super().__init__(name, size, color)
        self.breed = breed

    def bark(self):
        barking = super().action("WOOF!")
        return barking


# What was Inherited?
# I inherited the parameters from the Animal class in the Dog class. I also inherited the action
# method from the Animal class.

# What was Overrriden?
# I overriden the method __init__ from the Animal class when I added a fourth parameter in
# the Dog class.

# Where super() was used and why?
# I used it in the __init__ from Dog to avoid rewriting the logic created in the Animal class. And
# as I explained in my notebook, this makes the Animal class execute its own code before the Dog class
# so that it stays updated if we add a new name for example.
#
# I also used it in the method bark from the Dog class. This was made for us to reuse the way
# we create actions for diferent purposes. In this specific case I wanted the dog to bark, that's
# an action, so we just use the code that we already created for that purpose. super() acts as a way
# to communicate between classes.

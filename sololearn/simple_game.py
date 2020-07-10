

def get_input():
    """
    функция развбивает предложения на слова по пробелам
    потом сверяет со словарем verb_dict и вызывает
     функцию из словаря при наличии более двух слов 
    """
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))

def say(noun):
    return 'You said "{}"'.format(noun)

# dict_verb moved down

"""
The code above takes input from the user,
and tries to match the first word with a command in 
verb_dict. If a match is found, the corresponding function is called.
"""



# The next step is to use classes to represent game objects.

class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc

class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)

    @ property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wount on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health == 0:
            health_line = "It is dead."
        elif self.health < 0:
            health_line = "You so furious"
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        """
        Сеттер свойства desc вызывается при изменении значения
        """
        self._desc = value

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name)
    else:
        msg = "There is no {} here".format(noun)
    return msg

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here".format(noun)

goblin = Goblin("Gobbly")

verb_dict = {
  "say": say,
  "examine": examine,
  "hit": hit,
}

"""
We created a Goblin class, which inherits from the GameObjects class.
We also created a new function examine, which returns the objects description.
Now we can add a new "examine" verb to our dictionary and try it out!
"""


while True:
    get_input()

import random

class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):
        self.rare = rare
        self.heads = heads
        self.clean = clean

        for key, value in kwargs.items():
            setattr(self,key,value)

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rust_color

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

    def rust(self):
        self.rust = self.rust_color 

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print "Coin Spent"

    def flip(self):
        heads_option = [True, False]
        choice = random.choice(heads_option)
        self.heads = choice

    def __str__(self):
        if self.value < 1:
            return "{}p coin {} color () diameter".format(self.value,self.color,self.diameter)
        else"
            return "{} Pound coin {} color () diameter".format(self.value,self.color,self.diameter)

class Pound(Coin, object):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9
            }
        super(Pound, self).__init__(**data)
        

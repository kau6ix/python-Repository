import random

class Coin:
    def __init__(self, rust=False, clean=True, heads=True,**kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)
        
        self.is_rust=rust
        self.is_clean=clean
        self.is_heads=heads
        if self.is_rust:
            self.value=self.original_value*1.25
        else:
            self.value=self.original_value
        if self.is_clean:
            self.color=self.clean_color
        else:
            self.color=self.rust_color
    def rust(self):
            self.color=self.rust_color
    def clean(self):
            self.color=self.clean_color
    def flip(self):
        heads_option=[True, False]
        choice=random.choice(heads_option)
        self.heads=choice

class Pound(Coin):
    def __init__(self):
        data={"original_value":0.01,
              "clean_color":"gold",
              "rust_color":"brown",
              }
        super().__init__(**data)

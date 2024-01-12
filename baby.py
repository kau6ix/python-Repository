from random import choice
#answer=input("Why is the sky blue ?").lower()
questions=["why is the sky blue ?","why there are 12 house for a clock ? ", "why there are face in the moon"]
question=choice(questions)
answer=input(question).strip().lower()
while answer!="just because":
    answer=input("why ?...").strip().lower()
    
    

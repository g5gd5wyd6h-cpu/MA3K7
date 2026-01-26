def step(a,b):
    return b, (a + b) % 10

def encode_state(a,b):
    return 10*a + b

canonical_states = []

for a in range(0,10):
    for b in range(0,10):

        #re-initialize collisions for each (a,b)
        collisions = []

        while True:
            state = encode_state(a,b)
            if state in collisions:
                canonical_states.append(min(collisions))
                break
            else:
                collisions.append(state)
                a,b = step(a,b) 
            
print("Number of distinct canonical states:", sorted(set(canonical_states)))

#OUTPUT: Number of distinct canonical states: [0, 1, 2, 5, 13, 26]
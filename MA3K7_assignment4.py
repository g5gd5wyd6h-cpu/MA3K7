#number path heuristic estimate
import random
def estimate_probability_reaching_25(iterations):
    count25 = 0
    for i in range(iterations):
        currentPosition = 1
        while currentPosition <= 25:
            flip = random.randint(1,2)
            currentPosition += flip
            if currentPosition == 25:
                count25 += 1
                break
    print(f"Total iterations: {iterations}")
    print(f"Count of reaching 25: {count25}")
    print(f"Estimated probability of reaching 25: {count25 / iterations}")

#back propagation
def back_propagation(numberTarget):
    old = 1 #probability of reaching 25 from 25, which is 1.0.
    new = 1/2 # probability of reaching 25 from 24, which is 0.5.
    currentCalculation = numberTarget - 2
    while currentCalculation >= 1:
        temp = new
        new = (old + new)/2
        old = temp
        currentCalculation -= 1
    print(f"Probability of reaching {numberTarget} from 1: {new} bar computive epsilon error")

def main():
    #estimate_probability_reaching_25(1000000)
    back_propagation(25)
    back_propagation(24)
    back_propagation(23)
    back_propagation(22)
    back_propagation(21)
    back_propagation(20)
    back_propagation(2)
    back_propagation(1)
    back_propagation(3)  
    back_propagation(5)  
    back_propagation(99999)

main()
# Resources Used: Flap.js, Sipser: Introduction to the Theory of Computation
# Author: Ethan Han - e7han@ucsd.edu

import collections


# process input
def main():
    states = []
    alphabet = []
    transitions = []
    startState = ""
    acceptStates = []

    print("Input number of states: ")
    numStates = int(input())
    for i in range(0,numStates):
        states.append(input())

    print("Input number of characters in alphabet: ")
    numChars = int(input())
    for i in range(0,numChars):
        alphabet.append(input())
    
    print("Input number of transitions:")
    numTransitions = int(input())
    print("Input transitions in the following format: {start} {end} {symbol}")
    for i in range(0,numTransitions):
        strings = input().split(' ')
        transitions.append(strings)

    print("Input start state: ")
    startState = input()
    
    print("Input number of accept states: ")
    numAccept = int(input())
    for i in range(0,numAccept):
        acceptStates.append(input())

    convert(states, alphabet, transitions, startState, acceptStates)


# returns the set of states reachable from the current set of states with a symbol.
def explore(currStates, symbol, matrix):
    reachableStates = []
    for start in currStates:
        for end in matrix[start][symbol]:
            reachableStates.append(end)
    return reachableStates

def createMatrix(states, alphabet,transitions):
    matrix = collections.defaultdict(dict)
    for s in states:
        for sym in alphabet:
            matrix[s][sym] = []

    for t in transitions:
        matrix[t[0]][t[2]].append(t[1])

    return matrix


def convert(states, alphabet, transitions, startState, acceptStates):
    newStates = []
    newTransitions = []
    newStart = [startState]
    newAccept = []

    reachableStates = []

    matrix = createMatrix(states, alphabet, transitions)
    queue = [newStart]

    #BFS
    while len(queue) > 0:
        currStates = queue[0]
        queue.pop(0)

        for sym in alphabet:
            reachableStates = explore(currStates, sym, matrix)

            if reachableStates != []:
                if [currStates, reachableStates, sym] not in newTransitions:
                    newTransitions.append([currStates, reachableStates, sym])
                if reachableStates not in newStates:
                    newStates.append(reachableStates)
                    queue.append(reachableStates)
                    for reachable in reachableStates:
                        if reachable in acceptStates:
                            newAccept.append(reachableStates)
            else:
                if [currStates,"q_trap",sym] not in newTransitions:
                    newTransitions.append([currStates,"q_trap",sym])
                            
    newStates.append(["q_trap"])

    for sym in alphabet:
        newTransitions.append(["q_trap", "q_trap", sym])

    

    print("Set of States: ", *newStates, sep='\n- ')
    print("Alphabet: ", *alphabet, sep='\n- ')
    print("Set of Transitions: ", *newTransitions, sep='\n- ')
    print("Start State: ", newStart)
    print("Set of Accept States: ", *newAccept, sep='\n- ')

main()



# test: https://flapjs.web.app/#NFAq0:425:683:40:0:1;q1:327:1068:40:0:0;q2:740:963:40:0:2;0:1:a%CE%B5%CE%B50R:5:0:1:29~0:2:a%CE%B5%CE%B50R:5:19:7:2~1:2:a%CE%B5%CE%B50R:5:0:19:-9~2:0:b%CE%B5%CE%B50R:5:10:-28:-31~
# 3
# q0
# q1
# q2
# 2
# a
# b
# 4
# q0 q1 a
# q0 q2 a
# q1 q2 a
# q2 q0 b
# q0
# 1
# q2
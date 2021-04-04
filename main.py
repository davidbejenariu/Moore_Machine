from dataclasses import dataclass


@dataclass()
class Moore:
    Sigma: set
    States: set
    Cost: list
    StartState: int
    FinalStates: set
    Transitions: dict


def parseInputFile(A, words):
    with open("input.in", "r") as f:
        input = f.readlines()

    n = int(input[0].split()[0])
    m = int(input[0].split()[1])

    cost = input[1].split()
    A.Cost = []

    for i in range(n):
        A.States.add(i)
        A.Cost.append(cost[i])

    for i in range(2, m + 2):
        transition = input[i].split()
        stateX, stateY, wordZ = int(transition[0]), int(transition[1]), transition[2]

        A.Transitions[(stateX, wordZ)] = stateY

    A.StartState = int(input[m + 2])

    for f in input[m + 3].split()[1:]:
        A.FinalStates.add(int(f))

    n = int(input[m + 4])

    for i in range(m + 5, m + 5 + n):
        words.append(input[i].replace('\n', ''))


if __name__ == '__main__':
    A = Moore(set(), set(), [], -1, set(), {})
    words = []

    parseInputFile(A, words)

    for word in words:
        index = 0
        currentState = A.StartState
        cost = A.Cost[A.StartState]
        path = [A.StartState]
        found = True

        while index < len(word) and found:
            if (currentState, word[index]) not in A.Transitions:
                found = False
                currentState = -1
            else:
                currentState = A.Transitions[(currentState, word[index])]
                path.append(currentState)
                cost += A.Cost[currentState]
                index += 1

        if currentState in A.FinalStates:
            print("DA")
            print(cost)
            print("Traseu:", end=" ")

            for state in path:
                print(state, end=" ")

            print()
        else:
            print("NU")
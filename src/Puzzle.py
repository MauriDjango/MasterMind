# Possible colors for combinations
colors = {
    "Yellow": "#ffff00",
    "Black": "#000000",
    "Green": "#00ff00",
    "Red": "#ff0000",
    "Cyan": "#00ffff",
    "White": "#ffffff",
    "Purple": "#ff00ff",
    "Blue": "#0000ff"
}


# Generates a new secret combination
def newPuzzle(colors):
    puzzle = []
    for i in range(4):
        puzzle.append(random.choice(list(colors.values())))
    return puzzle


# Calculates the results of a guess
def calculateResult(attempt, puzzle):
    misplaced = 0
    incorrect = 0
    correct = 0
    correctPosition = [None, None, None, None]
    misplacedPositions = [None, None, None, None]
    puzzleCopy = puzzle.copy()

    for i in range(4):
        if attempt[i] == puzzleCopy[i]:
            correct+= 1
            correctPosition[i] = attempt[i]
            puzzleCopy[i] = None

        elif attempt[i] in puzzleCopy:
            misplaced += 1
            puzzleCopy[puzzleCopy.index(attempt[i])] = None

        elif attempt[i] not in puzzleCopy[i]:
            incorrect += 1

    result = {
        "incorrect": incorrect,
        "misplaced": misplaced,
        "correct": correct,
        "correctPosition": correctPosition,
    }

    session["intentos"].append({"intento": attempt, "result": result})

    # If there are more than five attempts, remove the oldest one
    if len(session["intentos"]) > 5:
        session["intentos"].pop(0)

    return result


# Generates the next machine guess
def botAttempt(lastAttempt, lastResult, colors):
    nextAttempt = [None, None, None, None]

    # If no previous correct, select four random colors
    if lastResult["correct"] == 0:
        for i in range(4):
            nextAttempt[i] = (random.choice(list(colors.values())))

    # If previous correct, choose new colors randomly
    for i in lastResult:
        if lastResult[i]:
            nextAttempt[i] = lastAttempt[i]
        else:
            nextAttempt[i] = random.choice(list(colors.values()))

    return nextAttempt
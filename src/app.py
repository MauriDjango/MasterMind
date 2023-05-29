from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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

@app.route('/', methods=['GET', 'POST'])
def play_game():
    if 'tries' not in session:
        session['tries'] = []

    if 'puzzle' not in session:
        puzzle = newPuzzle(colors)
        session['puzzle'] = puzzle.copy()

    puzzle = session['puzzle']

    if request.method == 'POST':

        if session['attempts'] == 1:
            botAttempt = []
            for _ in range(4):
                botAttempt.append(random.choice(list(colores.values())))
        else:
            previousAttempt = session['attempts'][-2]
            botAttempt = botAttempt(previousAttempt['attempt'], previousAttempt['result'], colores)
        botResult = calculateResult(botAttempt, puzzle)
        session['attempts'].append({'attempt': botAttempt, 'result': botResult})

        if botResult['incorrect'] == 4:
            return render_template('index.html', mensaje=f'¡La máquina ha acertado en {len(session["attempts"])} attempts!')

        else:
            intento = [request.form.get(f'attempt[{i}]') for i in range(4)]
            resultado = calculateResult(intento, puzzle)
            session['attempts'].append({'attempt': intento, 'result': resultado})

    return render_template('index.html', colores=colores, intentos=session.get('attempts', []), secreto=puzzle)

@app.route('/reiniciar', methods=['POST'])
def restart_game():
    session.clear()
    return render_template('index.html', colores=colores)


if __name__ == '__main__':
    app.run()

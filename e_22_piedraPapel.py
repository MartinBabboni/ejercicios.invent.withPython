def rpsWinner(jugador1, jugador2):
    if jugador1 == jugador2:
        return 'tie'
    if jugador1 =='rock' and jugador2=='paper':
        return 'player two'
    if jugador1 =='paper' and jugador2=='scissors':
        return 'player two'
    if jugador1 =='scissors' and jugador2=='rock':
        return 'player two'
    if jugador1 =='rock' and jugador2=='scissors':
        return 'player one'
    if jugador1 =='paper' and jugador2=='rock':
        return 'player one'
    if jugador1 =='scissors' and jugador2=='paper':
        return 'player one'

assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'

from random import randint

sum = wins = 0

print('=-' * 20)
print('LETS PLAY EVEN OR ODD!')
while True:
    num_bot = randint(1,10)
    sum = 0

    print('=-' * 20)
    num_usr = int(input('Choose a number: '))
    type = str(input('Even or Odd? [E/O] ')).strip().upper()

    sum += (num_usr + num_bot)

    if sum % 2 == 0 and type == 'E':
        print(f'You rolled {num_usr} and the computer rolled {num_bot}. The total of {sum} is EVEN')
        wins += 1
        print('YOU WON!')
    if sum % 2 != 0 and type == 'E':
        print(f'You rolled {num_usr} and the computer rolled {num_bot}. The total of {sum} is ODD')
        print('YOU LOSE!')
        break

    if sum % 2 != 0 and type == 'O':
        print(f'You rolled {num_usr} and the computer rolled {num_bot}. The total of {sum} is ODD')
        wins += 1
        print('YOU WON!')
    if sum % 2 == 0 and type == 'O':
        print(f'You rolled {num_usr} and the computer rolled {num_bot}. The total of {sum} is EVEN')
        print('YOU LOSE!')
        break

print('=-' * 20)
print(f'GAME OVER! You won {wins} times.')

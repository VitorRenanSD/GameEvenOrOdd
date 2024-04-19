from random import randint

soma = wins = 0

print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    num_bot = randint(1,10)
    soma = 0

    print('=-' * 20)
    num_usr = int(input('Diga um número: '))
    tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()

    soma += (num_usr + num_bot)

    if soma % 2 == 0 and tipo == 'P':
        print(f'Você jogou {num_usr} e o computador {num_bot}. Total de {soma} é PAR')
        wins += 1
        print('VOCÊ VENCEU!')
    if soma % 2 != 0 and tipo == 'P':
        print(f'Você jogou {num_usr} e o computador {num_bot}. Total de {soma} é IMPAR')
        print('VOCÊ PERDEU!')
        break

    if soma % 2 != 0 and tipo == 'I':
        print(f'Você jogou {num_usr} e o computador {num_bot}. Total de {soma} é IMPAR')
        wins += 1
        print('VOCÊ VENCEU!')
    if soma % 2 == 0 and tipo == 'I':
        print(f'Você jogou {num_usr} e o computador {num_bot}. Total de {soma} é PAR')
        print('VOCÊ PERDEU!')
        break

print('=-' * 20)
print(f'GAME OVER! Você venceu {wins} vezes.')

# UI inicial
print('=' * 30, 'CALCULADORA DE GASTO CALÓRICO DIÁRIO', 30 * '=')
input('                                   Pressione <enter> continuar')
print(' ')
print(' ')


# Fornecimento de informações
p = float(input('Insira seu peso em kg: '))
print(' ')
a = int( input('Agora insira sua altura em cm: ') )
print(' ')
i = int( input('Insira sua idade em anos: ') )
print(' ')
s = input('E por fim, insira sua sexualidade (M para masculino e F para feminino): ')


# Cálculo BMR
if s == 'M' or s == 'm':
    bmr = 66.47 + (13.75 * p) + (5.003 * a) - (6.775 * i)
elif s == 'F' or s == 'f':
    bmr = 655.1 + (9.563 * p) + (1.850 * a) - (4.676 * i)
    

# Seleção de valores para o cálculo de AMR:
print('1 - Sedentário (pouco ou nenhuma atividade física)')# * 1.2
print('2 - Ligeiramente ativo (atividade física 1-3 vezes na semana)')# * 1.375
print('3 - Moderadamente ativo (Atividade física 3-5 vezes na semana)')# * 1.55
print('4 - Ativo (Atividade física 6-7 vezes na semana)')# * 1.725
print('5 - Extremamente ativo (Atividade física de alta itensidade 6-7 vezes na semana)\n')# * 1.9
f = int( input('Selecione o valor que corresponda a sua frequencia de atividade física: ') )
print(' ')
print(' ')
print(' ')


# Cálculo AMR
if f == 1:
    amr = bmr * 1.2
elif f == 2:
    amr = bmr * 1.375
elif f == 3:
    amr = bmr * 1.55
elif f == 4:
    amr = bmr * 1.725
elif f == 5:
    amr = bmr * 1.9


# Resultados
print('~ Resultados: ')
print(f'º Seu gasto calórico para se manter vivo e acordado é {round(bmr, 2)} por dia')
print(' ')
print(f'º Já o seu gasto calórico somados a sua frequencia/itensidade de atividade física é {round(amr, 2)}')
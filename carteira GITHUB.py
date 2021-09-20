n = str(input('Digite seu nome: ')).strip()
nome = n.title()
cores = {'vermelho':'\033[1;31m', 'limpa':'\033[m'}
print('Olá {}{}{} Prazer te conhecer !!!'.format(cores['vermelho'], nome, cores['limpa']))
print('Vou te auxiliar na sua gestão financeira  vamos começar !!!')


# EM CONSTRUÇÃO ...
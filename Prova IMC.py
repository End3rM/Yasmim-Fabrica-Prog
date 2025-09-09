# A nutricionista Dra. Clara Souza atende dezenas de pacientes por semana e precisa de um
# sistema simples para calcular rapidamente o IMC (Índice de Massa Corporal) de cada
# pessoa. Ela pediu sua ajuda para desenvolver um pequeno programa que receba o peso e
# a altura do paciente e retorne o valor do IMC e a classificação de acordo com a tabela
# oficial da OMS.
# Sua tarefa é desenvolver esse sistema. Ele pode ser feito em linguagem Python,
# JavaScript, C, Java ou outra que você esteja aprendendo na disciplina.

print('Sistema Padrão para Cálculo de IMC.')
nome=input('Seja bem-vindo paciente. Prossiga para a identificação.\nQual é seu nome?\n')
altura=float(input(f'Olá, {nome}. Atualmente, qual é sua altura?\n')) 
peso=float(input(f'Sua altura atual é {altura}. Quanto você está pesando?\n'))

imc=peso/(altura*altura)
diagnostico=imc

print('----------- FICHA TÉCNICA -----------')
print(f'Nome do Paciente: {nome}')
print(f'Altura do Paciente: {altura}')
print(f'Peso do Paciente: {peso}')
print(f'IMC: {diagnostico}')
print('...')
print('[FINALIZAÇÃO]')
print(f'{nome}, seu IMC(Índice de Massa Corporal) atual é {imc}.\nO diagnóstico será exibido abaixo:')



print('----------- RESULTADO -----------')
if diagnostico < 18.5:
    print('Você está [Abaixo do seu peso ideal]. Retornando resultado para Dra. Clara Souza.')
elif diagnostico > 18.5 and diagnostico <= 24.9:
    print(' está no seu [Peso ideal]. Retornando resultado para Dra. Clara Souza.')
elif diagnostico > 25.0 and diagnostico <= 29.9:
    print('Você está [Sobrepeso]. Retornando resultado para Dra. Clara Souza.')
elif diagnostico > 30.0 and diagnostico <= 34.9:
    print('Você está com [Obesidade Grau 1]. Retornando resultado para Dra. Clara Souza.')
elif diagnostico > 35.0 and diagnostico <= 39.9:
    print('Você está com [Obesidade Grau 2]. Retornando resultado para Dra. Clara Souza.')
else:
    print('Você está com [Obesidade Grau 3]. Retornando resultado para Dra. Clara Souza.')






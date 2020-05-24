'''
PyLogThon é um gerenciador de log baseado no everton3x/logman escrito em PHP e que considera a especificação PSR-3
daquela linguagem.

Ele funciona com base em três elementos:

- logman: gerencia o ambiente de log e suas configurações.
- messenger: o mensageiro, responsável pelo envio dos dados para um ou mais loggers.
- logger: componente responsável por receber as mensagens do mensageiro e gravá-las ou exibi-las ao usuário.
'''
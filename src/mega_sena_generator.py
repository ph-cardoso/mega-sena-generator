#!/usr/bin/env python
"""Mega Sena game generator
This program generates a list of random numbers for the Mega Sena game.
The program can generate a list of games with a given number of numbers
and a given number of games.
The program can also save the generated games in a file.

Usage:
  python mega_sena_generator.py -q <quantidade> -t <tamanho> -o <output>

Options:
  -q, --quantidade:  quantidade de jogos.                                   [default: 1]
  -t, --tamanho:     tamanho do jogo [6, 7, 8, 9, 10, 11, 12, 13, 14, 15].  [default: 6]
  -o, --output:      nome do arquivo de saída.                              [default: output-current_date.txt]

Example:
  python mega_sena_generator.py -q 10 -t 6 -o output.txt
  python mega_sena_generator.py -q 10 -t 6
  python mega_sena_generator.py -q 10
  python mega_sena_generator.py
  python mega_sena_generator.py -h

Author:   Pedro Henrique Lima Cardoso
Version:  1.0.0
Date:     2022-12-18
Repo:     https://github.com/ph-cardoso/mega-sena-generator
"""

import datetime as dt
import sys
import getopt

def getArgs(argv: list) -> dict:
  """Verifica se os argumentos foram passados corretamente e retorna um dicionário com os argumentos
  :param argv: lista de argumentos passados para o programa
  :return: dicionário com os argumentos

  :Example:

  >>> getArgs(["mega_sena_generator.py", "-q", "10", "-t", "6", "-o", "output.txt"])
  {'quantidade': '10', 'tamanho': '6', 'output': 'output.txt'}
  >>> getArgs(["mega_sena_generator.py", "-q", "10", "-t", "6"])
  {'quantidade': '10', 'tamanho': '6'}
  >>> getArgs(["mega_sena_generator.py", "-q", "10"])
  {'quantidade': '10'}
  >>> getArgs(["mega_sena_generator.py"])
  {}
  >>> getArgs(["mega_sena_generator.py", "-h"])
  {}
  """
  arg_help = "\
    \nUso:\n\
    \n  python {0} -q <quantidade> -t <tamanho> -o <output>\
    \n\nOpções:\n\
    \n  -q, --quantidade:\t quantidade de jogos.\
    \t\t\t\t\t[default: 1]\
    \n  -t, --tamanho:\t tamanho do jogo [6, 7, 8, 9, 10, 11, 12, 13, 14, 15].\
    \t[default: 6]\
    \n  -o, --output:\t\t nome do arquivo de saída.\
    \t\t\t\t\t[default: output-{1}.txt]\
  ".format(argv[0] , dt.datetime.now().strftime("%d-%m-%Y"))

  try:
    opts, args = getopt.getopt(argv[1:], "hq:t:o:", ["help", "quantidade=", "tamanho=", "output="])
  except getopt.GetoptError as err:
    print(err)
    print(arg_help)
    sys.exit(2)

  args_dict = {}

  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print(arg_help)
      sys.exit()
    elif opt in ("-q", "--quantidade"):
      args_dict["quantidade"] = arg
    elif opt in ("-t", "--tamanho"):
      args_dict["tamanho"] = arg
    elif opt in ("-o", "--output"):
      args_dict["output"] = arg

  return args_dict


def generateGames(quantidade: int, tamanho: int) -> list:
  """Gera uma lista de jogos aleatórios com a quantidade e tamanho especificado
  :param quantidade: quantidade de jogos
  :param tamanho: tamanho do jogo
  :return: lista de jogos

  :Example:

  >>> generateGames(1, 6)
  [['01', '02', '03', '04', '05', '06']]
  >>> generateGames(2, 6)
  [['01', '02', '03', '04', '05', '06'], ['01', '02', '03', '04', '05', '06']]
  >>> generateGames(1, 7)
  [['01', '02', '03', '04', '05', '06', '07']]
  """
  games = []
  for i in range(quantidade):
    game = []

    for j in range(tamanho):
      number = random.randint(1, 60)

      while number in game:
        number = random.randint(1, 60)

      game.append(number)

    game.sort()
    games.append(game)

  returnGames = []
  for game in games:
    returnGames.append(["{:02d}".format(number) for number in game])

  return returnGames


def saveGames(games: list, arquivo_output: str) -> None:
  """Salva os jogos em um arquivo de texto com o nome especificado no parâmetro arquivo_output
  :param games: lista de jogos
  :param arquivo_output: nome do arquivo de saída

  :Example:

  >>> saveGames([['01', '02', '03', '04', '05', '06']], "output.txt")
  Arquivo output.txt salvo com sucesso!
  """
  path = os.path.dirname(os.path.abspath(__file__))
  path = os.path.dirname(path)
  path = os.path.join(path, "output")
  arquivo_output_with_path = os.path.join(path, arquivo_output)

  with open(arquivo_output_with_path, "w") as file:
    for game in games:
      file.write(" - ".join(game) + "\n")

  print("\n\nArquivo {} salvo com sucesso!".format(arquivo_output))


def printGames(games: list) -> None:
  """Imprime os jogos na tela
  :param games: lista de jogos

  :Example:

  >>> printGames([['01', '02', '03', '04', '05', '06'], ['01', '02', '03', '04', '05', '06']])

  Jogos gerados:

    01 - 02 - 03 - 04 - 05 - 06
    01 - 02 - 03 - 04 - 05 - 06

  """

  print("\nJogos gerados:\n")
  for game in games:
    print(" - ".join(game))


def main():
  """Função principal do programa"""
  arg_quantidade = "1"
  arg_tamanho = "6"
  arg_arquivo_output = "output-{}.txt".format(dt.datetime.now().strftime("%d-%m-%Y"))

  args = getArgs(sys.argv)

  if "quantidade" in args:
    arg_quantidade = args["quantidade"]
  if "tamanho" in args:
    arg_tamanho = args["tamanho"]
  if "output" in args:
    arg_arquivo_output = args["output"]

  games = generateGames(int(arg_quantidade), int(arg_tamanho))
  saveGames(games, arg_arquivo_output)

if __name__ == '__main__':
  main()

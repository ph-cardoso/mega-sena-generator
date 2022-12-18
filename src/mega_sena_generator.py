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
  -o, --output:      nome do arquivo de saída.                              [default: output-{1}.txt]

Example:
  python mega_sena_generator.py -q 10 -t 6 -o output.txt
  python mega_sena_generator.py -q 10 -t 6
  python mega_sena_generator.py -q 10
  python mega_sena_generator.py
  python mega_sena_generator.py -h

Author:  Pedro Henrique Lima Cardoso
Version: 1.0.0
Date:    2022-12-18
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
  ".format(argv[0] , dt.datetime.now().strftime("%d/%m/%Y"))

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



def main():
  """Função principal do programa"""
  arg_quantidade = "1"
  arg_tamanho = "6"
  arg_arquivo_output = "output-{}.txt".format(dt.datetime.now().strftime("%d/%m/%Y"))

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

import sys

pyfiglet_path = sys.path[0] + '/lib/'
sys.path.append(pyfiglet_path)

from pyfiglet import figlet_format

print(figlet_format('INFOLIXO', font='big'))

###
#
# Nao terminado
#
###

###############################################################################################################################
#Nome: pyfileinden.py
#
#Desenvolvido por Plinio
#Este Script utiliza parte do codigo do script [reabin.py - <http://code.activestate.com/recipes/65257/history/1/>]
#para leitura binaria dos arquivos.
#O script <reabin.py> foi escrito originalmente por Tony Dycks
#
#Sobre:
#Este script for codificado de forma rudimentar, ele tem a intencao de 
#ler os binarios de um arquivo passado como parametro, pegar os dois primeiro valores hexdecimais
#deste arquivo, e tentar encontrar em um arquivo de texto local algo que possa ser este arquivo.
#
#Pode ainda conter resultados fora do contexto, pois o arquivo que uso para fazer a comparacao
#nao esta completo e nem organizado. Espero pela compreensao.
#
#Basicamente ele tenta encontrar a indentidade do arquivo
#Ele ainda e muito instavel, contudo conforme eu for aprendendo Python, pretendo melhorar ele.
#
#
#
#Modo de Uso:
#python pyfileinde.py (Filepath/NomedoArquivo.ext) <Enter>
#
#Obeservacao:
#Este script precisa do arquivo Compare.txt
#

#Caso que voce queira salvar os resultados do script.
#Usar o seguinte comando:
#python pyfileinde.py (Filepath/NomedoArquivo.ext) >> (ResultadosPyFileInden.log) <Enter>
#
###############################################################################################################################

# Importando Bibliotecas
import sys  
import os   
		
# Limpando o console		
if sys.platform == 'linux-i386' or sys.platform == 'linux2':
	os.system('clear')

elif sys.platform == 'win32' or sys.platform == 'dos' or sys.platform[0:5] == 'ms-dos':
	os.system('cls')

else:
	SysCls = 'unknown'
	

print ' '
print 'Open Source Contribution Under The GNU Public License'
print 'Parte do script foi escrito originalmente por Tony Dycks '
print 'Adapatado por Plinio '
print ' '
print """
	 ____ ___  _ _____ _  _     _____ _  _      ____  _____ _     
/  __\\  \///    // \/ \   /  __// \/ \  /|/  _ \/  __// \  /|
|  \/| \  / |  __\| || |   |  \  | || |\ ||| | \||  \  | |\ ||
|  __/ / /  | |   | || |_/\|  /_ | || | \||| |_/||  /_ | | \||
\_/   /_/   \_/   \_/\____/\____\\_/\_/  \|\____/\____\\_/  \|
"""
print 'Press <Enter> Key To Continue ... \n',

# Declarando variaveis
response = sys.stdin.readline()
hexln = ''  
charval = 0
charcnt = 0

# *******************************************************************
# 			Abrindo arquivo via linha de comandos
# *******************************************************************
try:
	file = open(sys.argv[1], 'r')  
	#print 'File: ', file
	while 1:  # ==> Leia ate o final do arquivo um caractere de cada vez <==
		inchar = file.read(1)
		if not inchar:
			break
		charcnt = charcnt + 1
		charval = ord(inchar)
		hexval = hex(charval)
		hexstrlen = len(hexval)
		startpos = hexstrlen - 2
		if hexval[startpos] == 'x':
			startpos = startpos + 1
			hexval = '0'+hexval[startpos]
		else:
			hexval = hexval[startpos:hexstrlen]
		hexln = hexln+' '+hexval
		# *******************************************************************
		#				Imprime so os primeiros caracteres 
		# *******************************************************************
		if charcnt == 16:
			print hexln
			hexln = str(hexln)
			
except:
	print 'Error ao processar o arquivo:', sys.argv[1]
	print 'Programa Encerrado, Reveja as instrucoes'
	print ' '
	sys.exit()

# *******************************************************************
# 					Selecionando o Cabecalho  	
# *******************************************************************

print ' '
header = hexln[:6]
print "Cabecalho selecionado: "+header
print ''

# *******************************************************************
# 	==> Fazendo a Comparacao do cabecalho com nosso arquivo   <==
# *******************************************************************

compare = open('Compare.txt', 'r') #Abrindo o arquivo que sers usado para comparar os formatos.
data = header.upper() #Convetendo Toda a String para maiusculo
data = data[1:]  #Retirando o espaco em branco antes da String

for line in compare.readlines():
	if data in line:
		print "[+] Este arquivo pode ser: \n"
		print line
		print "[-]"
	else:
		continue
		
compare.close()



#
#Imprimir menssagem final
#
print ' '
print '>>> Programa Encerrado <<<'
print ' '
sys.exit()

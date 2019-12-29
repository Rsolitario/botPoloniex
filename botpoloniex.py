#!usr/bin/env python
import time, os, datetime
import os.path as path
from poloniex import poloniex
poloniex = poloniex()

directorio 	= "/home/end/workspace/py.botTrading/"
namefile 	= "USDT_BTC_2018.csv"
moneda 		= 'USDT_BTC'
intervalo	= 1800
Id = ""

def now():
	time_st = time.localtime()
	hora = time_st.tm_hour
	minutos= time_st.tm_min
	if minutos < 10:
		minutos = "0"+str(minutos)
	elif minutos >= 10: 
		minutos = str(minutos)
	hora = str(hora)	
	return ""+hora+":"+minutos+""

def consulta(moneda):
	dic = {}
	info_mercados = poloniex.returnTicker()
	parm = ["last", "high24hr", "low24hr", "percentChange", "quoteVolume"]
	for a in parm:
		dic[a] = info_mercados[moneda][a]
	return dic
	
def identificador(direc, nfile):
		if not (path.exists(direc+nfile)):
			print "falta el archivo: "+direc+nfile
		else:
			archivo = open(direc+nfile)
			i = 1
			for linea in archivo:
				res = linea.rstrip("\\n")
				i+=1
			archivo.close()
			return i

def connectPoloniex(ndir, nfile, cryptomoneda):
	if not path.exists(ndir+nfile):
		try:
			a = open(ndir+nfile, "a")
			a.close()
		except OSError:
			print 'El Archivo: '+nfile+' en el Directorio: '+ndir+' no se pudo crear!'
			return False
	Id = identificador(ndir, nfile)
	archivo = open(ndir+nfile, "a")
	dic = {}
	dic = consulta(cryptomoneda)
	diames = datetime.datetime.now()
	archivo.write(str(Id)+','+dic['last']+','+dic['high24hr']+','+dic['low24hr']+','+dic['percentChange']+','+dic['quoteVolume']+','+now()+','+str(diames.day)+','+str(diames.month)+'\n')
	archivo.close()

while True:
	print 'DATA: '+moneda+' hora: '+now()
	connectPoloniex(directorio, namefile, moneda)
	time.sleep(intervalo)


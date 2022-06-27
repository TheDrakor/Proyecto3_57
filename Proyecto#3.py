#Proyecto #3
#-----------------------
arr = [1,1,2,3,5,8,13,4]
datos = []
print(arr)
#su
suma = 0
#
try:
	#-------------------------------------------
	suma_a_buscar = input("\nQue suma buscas: ")
	#-------------------------------------------
	i = 0
	f = 1
	i2 = 0
	f2 = 1
	resultados = 0
	#-------------------------------------------
	while i != len(arr):
		#---------------------------------------
		for a in arr[i:f]:
			#-----------------------------------
			for r in arr[i2:f2]:
				if arr.index(a,i,f) == arr.index(r,i2,f2):
					if i2 ==len(arr)-1:
						i+=1
						f+=1
						i2 = 0
						f2 = 0
					else:
						i2+=1
						f2+=1
				else:
					#-------------------------------------------
					suma = int(a)+int(r)
					#print(f"Suma: {a} + {r} = {suma}")
					resDatos = str(arr.index(a,i,f))+str(arr.index(r,i2,f2))
					resDatosInv = resDatos[::-1]
					#---------------------------------------------------------------------------------------------------------------
					if suma == int(suma_a_buscar) and resDatosInv not in datos:
							
						print(f"\nLa suma de los indices: [{arr.index(a,i,f)}] + [{arr.index(r,i2,f2)}] dan como resultado {suma}")
						datos.append(str(arr.index(a,i,f))+str(arr.index(r,i2,f2)))
						resultados +=1
					#---------------------------------------------------------------------------------------------------------------
					if i2==len(arr)-1 and f2==len(arr):
						i+=1
						f+=1
						i2=0
						f2=1
					else:
						i2+=1
						f2+=1
					#----------------------------------
	if resultados == 0:
		print(f"\nNinguna suma de 2 digitos da ese resultado...")

except ValueError:
	print("\nSolo se aceptan numeros enteros")

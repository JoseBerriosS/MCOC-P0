# MCOC2020-P0
# Mi Computador Principal

* Marca/modelo: Apple MacBook Pro 15-inch (2018)
* Tipo: Notebook
* Año adquisición: 2019
* Procesador:
  * Marca/Modelo: Intel Core i7
  * Velocidad Base: 2,2 GHz
  * Velocidad Máxima: 4.1 GHz
  * Numero de núcleos: 6
  * Numero de subprocesos: 12
* Tamaño de las cachés del procesador:
  * L1: 64KB
  * L2: 256KB
  * L3: 9 MB
* Memoria:
  * Total: 16 GB
  * Tipo memoria: DDR4
  * Velocidad 2400 MHz
  * Numero de DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: AMD Radeon Pro 555X
  * Memoria: 4 GB
  * Resolución: 2880 x 1800
* Disco: 
  * Marca: Apple
  * Tipo: SSD
  * Tamaño: 256 GB
  * Sistema de archivos: APFS


* Dirección MAC de la tarjeta wifi: F0:18:98:64:F0:D6
* Dirección IP: 190.163.2.88
* Proveedor internet: VTR Banda Ancha S.A.


# Desempeño MATMUL

<img width="421" alt="Graficos Rendimiento A@B" src="https://user-images.githubusercontent.com/69157278/89681236-867fd100-d8c2-11ea-828d-4a925a662f22.png">

* ¿Como difiere del gráfico del profesor/ayudante? 
  * Difiere en el principio, ya que mi equipo tarda más en resolver la primera matriz. Luego se ve una tendencia a la alza, muy aproximada a la del profesor/ayudante.
  
* ¿A qué se pueden deber las diferencias? 
  * Tener más procesos simultáneos, una mayor utilización de recursos al momento de correr el programa.

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser? 
  * La memoria utilizada es la misma, ya que la forma de escribir el archivo es la misma. El tiempo, sin embargo, no lo es, depende de las características del equipo.

* ¿Qué versión de python está usando?
  * Estoy utilizando la versión 3.7 de Python.

* ¿Qué versión de numpy está usando?
  * Estoy utilizando la versión 1.16.2 de Numpy.

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.
  * No sabría decir si más de un procesador es utilizado, pero por lo que se aprecia en la imagen tiene un peak de %CPU = 646,06.
  <img width="779" alt="Captura de Pantalla 2020-08-07 a la(s) 15 53 34" src="https://user-images.githubusercontent.com/69157278/89684490-926e9180-d8c8-11ea-91ce-f1f5ca023c70.png">
  
# Desempeño MIMATMUL
  
  ![rendimiento mimatmul](https://user-images.githubusercontent.com/69157278/89847600-6a925e80-db52-11ea-8c5b-34bf869c6cba.png)
  

  
* En esta ocasión el gráfico se muestra de una forma más lineal, se demora más tiempo en realizar esta operación. Tal es la lentitud, que se toma como máximo la matriz de 500x500 (20 minutos aprox. en realizar todo el código). Sin embargo, no hay cambios en la memoria utilizada, ya que sigue siendo el mismo cálculo utilizado para la entrega anterior.
El gráfico del ayudante también tiene un aspecto lineal, difieren únicamente al principio, y esto puede ser por diferencias en los procesadores. 
  
# Desempeño de INV
![rendimiento numpy](https://user-images.githubusercontent.com/69157278/90082637-4b283c80-dcde-11ea-9b55-b49e49dcd4ec.png)
![rendimiento scipy false](https://user-images.githubusercontent.com/69157278/90082706-7e6acb80-dcde-11ea-9dd3-f22f8681ef5a.png)
![rendimiento scipy true](https://user-images.githubusercontent.com/69157278/90082819-c7bb1b00-dcde-11ea-81f1-49892196bb93.png)

No se alcanza a apreciar un cambio significativo al emplear la opción "overwrite_a=True".

* np.half = float16
* np.single = float32
* np.double = float64
* np.longdouble = float128

* ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)?

* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? El paralelismo básicamente es realizar varios procesos en simultáneo. El procesador divide los problemas más grandes y los convierte en problemas más pequeños, asi logra utilizar mejor los distintos tipos de memoria (L1, L2, L3)

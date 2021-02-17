# Modelado de epidemias

Fecha límite: jueves 25 de febrero a las 11:59 pm

Las epidemias y el contagio son fenómenos increíblemente complejos que involucran factores biológicos y sociales. Los modelos informáticos, aunque imperfectos, pueden ofrecer información sobre la propagación de enfermedades y pueden representar infecciones con diversos grados de complejidad.
SIR es un modelo simple, pero comúnmente utilizado, para epidemias. En el modelo SIR, una persona puede estar en uno de tres estados: susceptible a la enfermedad, infectada con la enfermedad o recuperada de la enfermedad después de la infección (el modelo lleva el nombre de estos tres estados: S-I-R). En este modelo, nos enfocamos en una red de personas, como una comunidad que podría estar experimentando una epidemia. Aunque simple, el modelo SIR captura tanto los factores sociales (como la forma de la red, por ejemplo, la frecuencia con la que las personas en la red interactúan entre sí) como los factores biológicos (como la duración de la infección) que median la propagación de la enfermedad.
En esta tarea, escribirás código para simular una versión simplificada del modelo epidémico SIR. Su código modelará cómo se propaga la infección a través de una ciudad desde los residentes hasta sus vecinos. En un nivel alto, su código calculará de manera iterativa los estados de enfermedad en una ciudad día a día, realizando un seguimiento del estado de cada persona hasta el final de la simulación. Además, verá cómo utilizar funciones que se complementan entre sí para simplificar un proceso de modelado complejo.


## El modelo
Para comenzar a construir nuestro modelo SIR, debemos especificar los detalles del modelo:

- Estados de enfermedad: las formas de describir la salud de cada persona en la simulación.
- Estructura de una ciudad: cómo se representa una ciudad y los vecinos de cada individuo en la ciudad.
- Reglas de transmisión para la propagación de enfermedades dentro de la ciudad,
- Reglas de contagio: las reglas para recuperarse y adquirir inmunidad a las enfermedades, y
- Condiciones de alto: cuándo detener la simulación.

Especificamos cada uno de estos detalles a continuación.

**Estados de enfermedad**: todas las personas en la simulación pueden existir en uno de los tres estados, susceptible, infectado o recuperado.

- Susceptible: el individuo está sano pero puede infectarse en el futuro. Usaremos ```'S'``` para representar individuos susceptibles.
- Infectado: el individuo tiene una infección actualmente. Representaremos a estas personas con ```'I0', 'I1', 'I2'```, etc. El número después de la I representa la cantidad de días que la persona ha estado infectada (consulte las “Reglas de contagio” a continuación).
- Recuperado: el individuo se ha recuperado de una infección y será inmune a la infección durante el resto de la simulación. Representamos a estas personas con ```'R'```. (Algunas versiones del modelo SIR eliminan a las personas recuperadas del modelo. En nuestro modelo, las personas recuperadas permanecerán en la ciudad).

Ten en cuenta que, en las tareas 6 y 7 de la tarea, introduciremos un estado adicional: Vacunado (representado con una ```'V'```). No necesita preocuparse por este estado, o cualquier referencia a las vacunas, hasta que llegue a esas tareas finales.

**Estructura de una ciudad**: una ciudad en esta simulación se representa como una lista de personas, cada una representada por un estado de enfermedad. Por ejemplo, una ciudad de ```['S', 'I1', 'R']``` está compuesta por tres personas, la primera de las cuales es susceptible, la segunda de las cuales está infectada (y específicamente, está un día después de la infección), y el tercero de los cuales se recupera.

Puedes asumir que cada ciudad tiene al menos una persona.

Una persona en nuestro modelo simplificado tiene hasta dos vecinos, la persona inmediatamente antes de ellos en la lista (conocida como su vecino izquierdo) y la persona inmediatamente después de ellos en la lista (conocida como su vecino derecho). La primera persona de la lista no tiene un vecino de la izquierda y la última persona de la lista no tiene un vecino de la derecha. Por ejemplo, considere la siguiente lista de personas: ['Juan', 'Sara', 'Laura', 'Marco']:

Juan tiene una vecina: Sara.

Sara tiene dos vecinos: Juan y Laura.

Laura tiene dos vecinos: Sara y Marco.

Marco tiene una vecina: Laura.

**Reglas de transmisión**: la infección siempre se transmite de personas infectadas ('I0', 'I1', etc.) a personas susceptibles ('S'). En otras palabras, una persona susceptible con al menos un vecino infectado siempre se infectará al día siguiente.

**Reglas de contagio**: el número de días que una persona está infectada y permanece contagiosa es un parámetro de la simulación. Realizaremos un seguimiento del número de días que una persona ha estado infectada como parte de su estado. Las personas que se infectan comienzan en el estado '10'. Por cada día que una persona está infectada, incrementamos el contador en uno: 'I0' se convierte en 'I1', 'I1' se convierte en 'I2', etc. Cuando el contador alcanza el número especificado de días contagiosos, los declararemos contagiosos recuperado ('R') y ya no es contagioso. En ese momento, son inmunes a la enfermedad y no pueden volver a infectarse. Por ejemplo, si estamos simulando una infección en la que las personas son contagiosas durante tres días, una persona recién infectada comenzará en el estado 'I0', pasará a 'I1' después de un día, a 'I2' después de dos días, y declarará 'R', donde permanecerán durante el resto de la simulación, después de tres días.

**Condiciones de alto**: la simulación debe detenerse cuando no haya más personas infectadas en la ciudad

## Tus tareas
Para esta tarea, especificaremos un conjunto de funciones que debes implementar.
Comenzarás con funciones básicas y avanzará hasta tareas más complejas. También proporcionaremos un extenso código de prueba. 

### Paso 1: Contar el número de personas infectadas en una ciudad

En Python, es común escribir funciones auxiliares que encapsulan definiciones de clave y solo tienen unas pocas líneas. Su primera tarea es completar una de estas funciones: ```count_infected```.

Aquí está el código que verá en el archivo sir.py:

```
def count_infected(city):
    '''
    Cuenta el número de infectados

    Inputs:
      city (list of strings): El estado de una ciudad en un momento determinado
    Returns (int): Conteo de cuánta gente está infecta
      currently infected
    '''

    # TÚ CODIGO VA AQUÍ

```

El docstring de la función especifica los *inputs* de la función. Es suficiente asumir que la variable ```city```  contendrá el valor especificado de contagio, más específicamente, una lista de  strings con el estado de todas las personas en la simulación al comienzo del día.

Luego, debe escribir un código que tome esta variable de ciudad y cuente el número de vecinos infectados.

Por ejemplo, dada la ciudad ```['I0', 'I0', 'I2', 'S', 'R']```, la función devolvería ```3``` (observe cómo tenemos que tener en cuenta el hecho de que hay varios estados infectados). Dada una ciudad como ```['S', 'S', 'S', 'S']```, la función devolvería ```0```.

Aquí hay algunas ciudades y el resultado esperado

| Ciudad                 | Resultado esperado |
|------------------------|--------------------|
| [‘I0’]                 | 1                  |
| [‘I2000’]              | 1                  |
| [‘R’]                  | 0                  |
| [‘S’]                  | 0                  |
| [‘S’, ‘S’, ‘S’, ‘S’]   | 0                  |
| [‘R’, ‘R’, ‘R’, ‘R’]   | 0                  |
| [‘I1’, ‘S’, ‘S’, ‘S’]  | 1                  |
| [‘S’, ‘I1’, ‘S’, ‘S’]  | 1                  |
| [‘S’, ‘S’, ‘I1’, ‘S’]  | 1                  |
| [‘S’, ‘S’, ‘S’, ‘I1’]  | 1                  |
| [‘I1’, ‘R’, ‘R’, ‘R’]  | 1                  |
| [‘I0’, ‘S’, ‘I1’, ‘R’] | 2                  |

Es importe mencionar que para esta tarea hemos generado tests que uno debe correr para asegurar que la función cumple con los requisitos. Por favor abre el archivo ```tarea_2.ipynb``` para consultar estos tests

### Paso 2: ¿Está infectado un vecino?
A continuación, escribirá una función llamada ```has_an_infected_neighbor``` que determinará si una persona susceptible en una posición determinada en una lista tiene al menos un vecino infectado.

Más específicamente, dada la ciudad y la posición de la persona, su código computará las posiciones de los vecinos izquierdo y derecho de la persona especificada en la ciudad, si existen, y determinará si alguno de ellos está en un estado infectado.

Recuerde que la primera persona en la ciudad tiene un vecino de la derecha, pero no un vecino de la izquierda y la última persona en la ciudad tiene un vecino de la izquierda, pero no un vecino de la derecha. Su código deberá manejar estos casos especiales.

Solo tiene sentido llamar a esta función en una posición que contenga una persona susceptible, así que asegurate que esta función solo sirva para personas con estado susceptible.

Algunos casos de uso de la función

```
In [8]: has_an_infected_neighbor(['I1', 'S', 'S'], 1)
Out[8]: True

In [9]: has_an_infected_neighbor(['S', 'I1', 'IO'], 0)
Out[9]: True

In [9]: has_an_infected_neighbor(['S', 'R', 'IO'], 0)
Out[9]: False

In [10]: has_an_infected_neighbor(['S', 'I0', 'S'], 2)
Out[10]: True

In [10]: has_an_infected_neighbor(['S'], 0)
Out[10]: False
```

En la primera lllamada, comprobamos si la persona susceptible en la posición 1 tiene un vecino infectado. Dado que su vecino izquierdo (en la posición 0) está infectado, el resultado debería ser Verdadero.

La siguiente llamada comprueba si la persona susceptible en la posición 0 tiene un vecino infectado. Esta persona no tiene vecino abandonado. Sin embargo, su vecino derecho, en la posición 1, está infectado y, por lo tanto, el resultado debería ser Verdadero.

La tercera llamada también comprueba a la persona en la posición 0. En este caso, la persona en la posición 1 no está infectada, por lo que el resultado esperado es Falso.

La cuarta llamada comprueba a la persona en la posición 2. Esta persona no tiene un vecino adecuado. Sin embargo, su vecino izquierdo, en la posición 1, está infectado, por lo que el resultado esperado es Verdadero.

Finalmente, la última llamada devolverá ```False```. ¿Por qué? Porque, la única persona en esta ciudad no tiene vecinos y, por lo tanto, por definición no tiene vecinos infectados. Tenga en cuenta que una solución correcta no necesita incluir una condición que verifique “si esta ciudad tiene una sola persona”. El código debería funcionar para ciudades de todos los tamaños, incluidas las ciudades con una sola persona. Pista: la persona en esta ciudad unipersonal es tanto el primer como el último elemento de la lista.

Tests a la función:

| Ciudad                   | Posición | Resultado esperado |
|-------------------------|----------|--------------------|
| [‘I0’, ‘S’, ‘S’]        | 1        | True               |
| [‘I1000’, ‘S’, ‘S’]     | 1        | True               |
| [‘R’, ‘S’, ‘I0’]        | 1        | True               |
| [‘R’, ‘S’, ‘I1000’]     | 1        | True               |
| [‘I1’, ‘S’, ‘I0’]       | 1        | True               |
| [‘S’, ‘S’, ‘R’]         | 1        | False              |
| [‘R’, ‘S’, ‘S’, ‘I1’]   | 2        | True               |
| [‘R’, ‘I200’, ‘S’, ‘R’] | 2        | True               |
| [‘I0’, ‘S’, ‘S’, ‘R’]   | 2        | False              |
| [‘S’, ‘S’, ‘S’, ‘I1’]   | 0        | False              |
| [‘S’, ‘I1’, ‘S’, ‘I1’]  | 0        | True               |
| [‘I0’, ‘S’, ‘S’, ‘S’]   | 3        | False              |
| [‘I0’, ‘S’, ‘I10’, ‘S’] | 3        | True               |
| [‘S’]                   | 0        | False              |


### Paso 3: Avanzar estado de persona
Su tercerp paso es completar la función ```advance_person_at_position```. El objetivo de esta función es avanzar el estado de enfermedad de una persona de un día para otro. Dada una ciudad, la ubicación de una persona dentro de esa ciudad y la cantidad de días c la infección es contagiosa, su función debe determinar el próximo estado de la persona. Específicamente, si la persona es:

Susceptible ('S'): debe determinar si tiene un vecino infectado (utilizando la función has_an_infected_neighbor) y, de ser así, cambiarlo al primer estado infectado ('I0'). De lo contrario, permanecen en el estado Susceptible ('S').

Infectado ('I', seguido de un número entero; nos referiremos a ese número entero como x): determine si la persona permanece infectada (es decir, ```x + 1 < c``` ) y pasa al siguiente estado infectado (por ejemplo, 'I0' se convierte en 'I1', ' I1 'se convierte en' I2 ', etc.) o cambia al estado recuperado (' R '). Para calcular el nuevo estado de una persona infectada, deberá extraer el número de días infectados del estado como una cadena, convertirlo en un número entero y luego compararlo con el número de días contagiosos c. Si determinó que la persona seguirá infectada, deberá construir una nueva cadena a partir de 'I' y ```c```.

Recuperado ('R'): no debe hacer nada. Las personas recuperadas permanecen en ese estado.

Como ejemplo, considere las siguientes llamadas a ```advance_person_at_position```:

```
In [22]: advance_person_at_position(['I0', 'I1', 'R'], 0, 2)
Out[22]: "I1"

In [22]: advance_person_at_position(['I0', 'I1', 'R'], 1, 2)
Out[22]: "R"

In [22]: advance_person_at_position(['I0', 'I1', 'R'], 2, 2)
Out[22]: "R"
```

Tests a la función:
| Ciudad                  | Posición| Días Contagiado | Resultado |
|-----------------------|----------|-----------------|--------|
| [‘I1’, ‘S’, ‘S’]      | 1        | 3               | I0     |
| [‘S’, ‘S’, ‘I0’]      | 1        | 3               | I0     |
| [‘I20’, ‘S’, ‘I0’]    | 1        | 3               | I0     |
| [‘R’, ‘S’, ‘R’]       | 1        | 3               | S      |
| [‘I1’, ‘S’, ‘S’, ‘S’] | 2        | 3               | S      |
| [‘S’, ‘S’, ‘I0’]      | 0        | 3               | S      |
| [‘S’, ‘I1500’, ‘I0’]  | 0        | 3               | I0     |
| [‘I1’, ‘R’, ‘S’]      | 2        | 3               | S      |
| [‘I1’, ‘I1500’, ‘S’]  | 2        | 3               | I0     |
| [‘I1’, ‘I1500’, ‘S’]  | 0        | 3               | I2     |
| [‘I2’, ‘I1500’, ‘S’]  | 0        | 3               | R      |
| [‘I2’, ‘I1500’, ‘S’]  | 1        | 2000            | I1501  |
| [‘I2’, ‘I1500’, ‘S’]  | 1        | 1501            | R      |
| [‘I2’, ‘I1500’, ‘R’]  | 2        | 2000            | R      |


### Paso 4: Avanzar la simulación un solo día
Su cuarto paso es completar la función ```simulate_one_day```. Esta función modelará un día en una simulación y actuará como una función auxiliar para ```run_simulation```. Más concretamente, ```simulate_one_day``` debe tomar el estado de la ciudad al comienzo del día y el número de días que una persona es contagiosa y devolver una nueva lista de estados de enfermedad (es decir, el estado de la ciudad después de un día).

Su implementación para esta función debe usar ```advance_person_at_position``` para determinar el nuevo estado de cada persona en la ciudad.

Por ejemplo:

```
In [24]: simulate_one_day(['S', 'I0', 'S'], 2)
Out[24]: ['I0', 'I1', 'I0']
```

Nota cómo las personas susceptibles en las posiciones 0 y 2 se infectan (ambas tienen un vecino infectado) y la persona en la posición 1 avanza al siguiente estado de su infección ('I0' a 'I1').

Tests

| Ciudad               | Días contagio | Resultado esperado   |
|----------------------|---------------|----------------------|
| [‘I0’, ‘I1’, ‘I100’] | 200           | [‘I1’, ‘I2’, ‘I101’] |
| [‘I2’, ‘I2’, ‘I2’]   | 3             | [‘R’, ‘R’, ‘R’]      |
| [‘R’, ‘R’, ‘R’]      | 3             | [‘R’, ‘R’, ‘R’]      |
| [‘I1’, ‘S’, ‘I1’]    | 3             | [‘I2’, ‘I0’, ‘I2’]   |
| [‘I1’, ‘S’, ‘I1’]    | 2             | [‘R’, ‘I0’, ‘R’]     |
| [‘S’, ‘I0’, ‘S’]     | 2             | [‘I0’, ‘I1’, ‘I0’]   |
| [‘S’, ‘S’, ‘S’]      | 2             | [‘S’, ‘S’, ‘S’]      |


### Paso 5: Correr la simulación
Su quinto paso es completar la función ```run_simulation```, que toma el estado inicial de la ciudad y el número de días que una persona es contagiosa, y devuelve tanto el estado final de la ciudad como el número de días simulados como una tupla. Notará que esta función también toma dos parámetros opcionales adicionales (random_seed y vaccionation_effectiveness); puede ignorar estos parámetros ya que no los utilizaremos hasta la siguiente tarea.

La función debe ejecutar una simulación completa, llamando repetidamente a ```simulate_one_day``` hasta que llegue a la condición de parada de la simulación: cuando la ciudad no tenga personas infectadas. Al hacer esto, la función también debe contar el número de días simulados.

Tenga en cuenta que, si la condición de parada es verdadera al inicio de la simulación, entonces el número de días simulados será cero.

Aquí hay dos usos de esta función:

```
In [32]: run_simulation(['S', 'S', 'I0'], 3)
Out[32]: (['R', 'R', 'R'], 5)

In [33]: run_simulation(['S', 'R', 'I0'], 3)
Out[33]: (['S', 'R', 'R'], 3
```

Tests

| Ciudad al inicio                      | Días contagiado | Resultado esperado: ciudad y días         |
|---------------------------------------|-----------------|-------------------------------------------|
| [‘S’, ‘S’, ‘I0’]                      | 3               | ([‘R’, ‘R’, ‘R’], 5)                      |
| [‘S’, ‘R’, ‘I0’]                      | 3               | ([‘S’, ‘R’, ‘R’], 3)                      |
| [‘R’, ‘S’, ‘S’]                       | 2               | ([‘R’, ‘S’, ‘S’], 0)                      |
| [‘R’, ‘I0’, ‘S’, ‘I1’, ‘S’, ‘R’, ‘S’] | 10              | ([‘R’, ‘R’, ‘R’, ‘R’,‘R’, ‘R’, ‘S’], 11) |


### Paso 6: Vacunar una ciudad
Su próximo paso es modificar las funciones para un nuevo estado: vacunado ('V'). Esto implicará implementar la función ```vaccinate_city``` y actualizar la función ```run_simulation```.

El estado 'V' en realidad se comporta exactamente como el estado 'R': una persona vacunada es inmune a la enfermedad y no puede infectarse. Sin embargo, mientras que el estado 'R' se alcanza durante la simulación después de que una persona atraviesa una infección, el estado 'V' se alcanza antes de que comience la simulación, cuando vacunaremos a todas las personas susceptibles de la ciudad.

Sin embargo, ninguna vacuna es 100% efectiva, lo que significa que administrar una vacuna a una persona susceptible no la cambia incondicionalmente al estado 'V'. En cambio, nuestra simulación tendrá un parámetro adicional: una tasa de efectividad de la vacuna v entre 0.0 y 1.0.

En el contexto de este ejercicio, puede pensar que la efectividad de la vacuna es similar a lanzar una moneda ponderada. Esto significa que, si v es 0.8, la moneda caerá en “cara” el 80% de las veces y en “cruz” el 20% de las veces. Ahora, imagine que la moneda tiene "la vacuna confiere inmunidad" en lugar de "cara", y "la vacuna NO confiere inmunidad" en lugar de "cruz".

Entonces, por cada persona susceptible que recibe una vacuna, lanzamos esta moneda ponderada para determinar si la vacuna funciona (la persona cambia al estado 'V') o no funciona (la persona permanece en el estado 'S').

Para "lanzar una moneda" en Python, usaremos un generador de números aleatorios y, más específicamente, llamaremos random.random (), una función que devuelve un número de punto flotante aleatorio entre 0.0 y 1.0. Interpretaremos el valor devuelto de la siguiente manera:

- Si el número aleatorio es estrictamente menor que v, la vacuna funciona.

- Si el número aleatorio es mayor o igual av, la vacuna no funciona.

Entonces, ```vaccinate_city``` tomará una ciudad y una tasa de efectividad de la vacuna, y devolverá una nueva ciudad donde cada persona susceptible ha sido vacunada de acuerdo con la regla anterior. Una vez que haya implementado ```vaccinate_city```, deberá modificar ```run_simulation``` para llamar a vaccinate_city una vez antes de simular cualquier día. Notará que todas nuestras pruebas anteriores llamadas ```run_simulation``` con la efectividad de la vacuna establecida en 0.0, lo que significa que, una vez que complete esta tarea, las pruebas anteriores no se interrumpirán porque continuarán comportándose como antes: sin que nadie en la ciudad esté vacunado .

También deberá asegurarse de que ```advance_person_at_position``` funcione correctamente con el estado 'V'. En particular, alguien en el estado 'V' debe permanecer en ese estado. Puede probar si su función está funcionando como se esperaba de esta manera:

```
In [3]: sir.advance_person_at_position(['S', 'V', 'S'], 1, 2)
Out[3]: 'V'
```

Si la llamada anterior devuelve algo que no sea 'V', asegúrese de estar manejando correctamente el estado 'V' en advance_person_at_position.

Ahora, hay un pequeño truco en el uso de números aleatorios. Intentemos random.random (); para hacerlo, primero tendrá que importar el módulo aleatorio:

```
In [1]: import random
```

Ahora, intente llamar la función

```
In [2]: random.random()
Out[2]: 0.595299247755262

In [3]: random.random()
Out[3]: 0.8159606343474648

In [4]: random.random()
Out[4]: 0.30061626031208444
```

Aquí está lo complicado de los números aleatorios en Python: es casi seguro que verá números diferentes cuando pruebe random.random () (lo cual tiene sentido: ¡la función está destinada a devolver un número aleatorio!) Esto puede complicar la depuración y las pruebas, porque puede llamar a una función que se base en random.random () (como vaccinate_city) y obtenga resultados diferentes cada vez.

Afortunadamente, podemos asegurarnos de que random.random () devuelva la misma secuencia de números cuando se llama al inicializarlo con un valor semilla. Es común establecer el valor inicial para un generador de números aleatorios durante la depuración. Si no establecemos activamente la semilla, los generadores de números aleatorios generalmente derivarán uno del sistema

Dado que muchas de nuestras pruebas usan la misma semilla (20170217), hemos definido una constante, TEST_SEED, con este valor en sir.py para su conveniencia. Este valor debe usarse solo para pruebas; no debería aparecer en ninguna parte del código que escriba.

Probemos a establecer la semilla usando el valor de TEST_SEED y luego hagamos algunas llamadas al generador de números aleatorios en ipython3:


```
In [11]: sir.TEST_SEED
Out[11]: 20170217

In [12]: random.seed(sir.TEST_SEED)

In [13]: random.random()
Out[13]: 0.48971492504609215

In [14]: random.random()
Out[14]: 0.23010566619210782

In [15]: random.seed(sir.TEST_SEED)

In [16]: random.random()
Out[16]: 0.48971492504609215

In [17]: random.random()
Out[17]: 0.23010566619210782

```

Observe que la tercera y cuarta llamadas a random.random () generan exactamente los mismos valores que las dos primeras llamadas. ¿Por qué? Porque establecemos la semilla exactamente en el mismo valor antes de la primera y tercera llamadas.

Este comportamiento aleatorio tiene otra implicación: es **crucial** que ```vaccinate_city``` llame a random.random () solo cuando se encuentre con una persona susceptible. Si llama al generador de números aleatorios para cada persona (incluidas las personas que no están en el estado 'S'), su código puede generar respuestas diferentes a las nuestras en pasos posteriores.

Tests

A diferencia de los pasos anteriores, debe tener cuidado de inicializar la semilla aleatoria antes de llamar a ```vaccinate_city```, para asegurarse de obtener los resultados esperados. Por ejemplo:

```
In [22]: random.seed(sir.TEST_SEED)

In [23]: sir.vaccinate_city(['S', 'S', 'S', 'S', 'S', 'I0', 'S'], 0.8)
Out[23]: ['V', 'V', 'V', 'V', 'S', 'I0', 'V']

In [24]: random.seed(sir.TEST_SEED)

In [25]: sir.vaccinate_city(['S', 'S', 'S', 'S', 'S', 'I0', 'S'], 0.3)
Out[25]: ['S', 'V', 'S', 'S', 'S', 'I0', 'S']
```

Sin embargo, cuando pruebe su ```run_simulation``` actualizado, tenga en cuenta que la función toma la semilla aleatoria como parámetro, lo que significa que debe llamar a random.seed dentro de ```run_simulation```. A continuación, se muestran algunos usos de ejemplo:

```
In [34]: sir.run_simulation(['S', 'S', 'S', 'S', 'S', 'I0', 'S'], 2, sir.TEST_SEED, 0.0)
Out[34]: (['R', 'R', 'R', 'R', 'R', 'R', 'R'], 7)

In [35]: sir.run_simulation(['S', 'S', 'S', 'S', 'S', 'I0', 'S'], 2, sir.TEST_SEED, 0.3)
Out[35]: (['S', 'V', 'R', 'R', 'R', 'R', 'R'], 5)

In [36]: sir.run_simulation(['S', 'S', 'S', 'S', 'S', 'I0', 'S'], 2, sir.TEST_SEED, 0.8)
Out[36]: (['V', 'V', 'V', 'V', 'R', 'R', 'V'], 3)
```


Observe cómo estos resultados tienen sentido: a medida que aumenta la efectividad de la vacuna, la duración de la epidemia disminuye.

La siguiente tabla proporciona información sobre las pruebas automatizadas para ```vaccinate_city```. Cada fila contiene la semilla utilizada para inicializar el generador de números aleatorios, los valores que se pasarán para la ciudad y los argumentos de efectividad de la vacuna para esa prueba, y el resultado esperado. La última columna describe brevemente la prueba.

Tests para ```vaccinate_city```
| Semilla  | Ciudad                               | Efectividad vacuna | Resultado                            |
|----------|--------------------------------------|--------------------|--------------------------------------|
| 20170217 | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] | 0.0                | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] |
| 20170217 | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] | 1.0                | [‘V’, ‘V’, ‘V’, ‘V’, ‘V’, ‘I0’, ‘V’] |
| 20170217 | [‘I0’, ‘I1’, ‘I2’, ‘R’]              | 1.0                | [‘I0’, ‘I1’, ‘I2’, ‘R’]              |
| 20170217 | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] | 0.3                | [‘S’, ‘V’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] |
| 20170217 | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] | 0.8                | [‘V’, ‘V’, ‘V’, ‘V’, ‘S’, ‘I0’, ‘V’] |
| 20170218 | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] | 0.8                | [‘V’, ‘V’, ‘V’, ‘V’, ‘V’, ‘I0’, ‘V’] |

Tests para ```run_simulation``` (con vacunas)
| Semilla  | Ciudad                               | Días contagio | Efectividad vacuna | Resultado esperado                                      |
|----------|--------------------------------------|---------------|--------------------|---------------------------------------------------------|
| 20170217 | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] | 2             | 0.0                | [[‘R’, ‘R’, ‘R’, ‘R’, ‘R’, ‘R’, ‘R’], 7]                |
| 20170217 | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] | 2             | 0.3                | [[‘S’, ‘V’, ‘R’, ‘R’, ‘R’, ‘R’, ‘R’], 5]                |
| 20170218 | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] | 2             | 0.3                | [[‘S’, ‘S’, ‘S’, ‘V’, ‘V’, ‘R’, ‘R’], 3]                |
| 20170217 | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] | 2             | 0.8                | [[‘V’, ‘V’, ‘V’, ‘V’, ‘R’, ‘R’, ‘V’], 3]                |
| 20170218 | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] | 2             | 0.8                | [[‘V’, ‘V’, ‘V’, ‘V’, ‘V’, ‘R’, ‘V’], 2]                |
| 20170217 | [‘S’, ‘S’, ‘S’, ‘S’, ‘S’, ‘I0’, ‘S’] | 2             | 1.0                | [[‘V’, ‘V’, ‘V’, ‘V’, ‘V’, ‘R’, ‘V’], 2]                |


Paso 7: Determinación del tiempo promedio hasta cero infecciones
Este paso consiste en completar la función ```calc_avg_days_to_zero_infections```, que calcula el número promedio de días que le toma a una ciudad alcanzar cero infecciones. Esta función toma el estado inicial de la ciudad, la cantidad de días contagiosos, la semilla aleatoria, la tasa de efectividad de la vacuna y la cantidad de ensayos que se ejecutarán como argumentos y devuelve el número promedio de días hasta que una ciudad alcanza cero infecciones durante el número de ensayos. diferentes ejecuciones de prueba. El número de días hasta que una ciudad alcanza cero infecciones es simplemente el número de días devueltos por run_simulation.

Cada vez que ejecute una simulación de prueba, debe aumentar la semilla aleatoria en 1. Es importante que incremente su semilla aleatoria. Si olvida incrementar su semilla, todas las pruebas serán idénticas, y si incrementa su semilla de una manera diferente a la especificada, su código puede producir un resultado diferente (y por lo tanto, no pasar nuestras pruebas).

Su implementación debe llamar a run_simulation, que establece la semilla, por lo que a diferencia de la tarea anterior, no necesita llamar a random.seed antes de ejecutar esta función en ipython3.

A continuación, se muestra un ejemplo de uso de esta función:

```
In [52]: sir.calc_avg_days_to_zero_infections(['S', 'S', 'S', 'S', 'S', 'I0', 'S'],
    ...:                                      2, sir.TEST_SEED, 0.65, 5)
Out[52]: 2.6
```

Tests
| Semilla  | Ciudad                                        | Días Contagio | Efectividad vacuna | Número de prueba | Resultado esperado |
|----------|-----------------------------------------------|---------------|--------------------|------------------|--------------------|
| 20170217 | [‘S’, ‘I1’, ‘S’, ‘I0’]                        | 2             | 0.8                | 5                | 2.2                |
| 20170217 | [‘S’, ‘I1’, ‘S’, ‘I0’]                        | 2             | 0.3                | 5                | 2.8                |
| 20170219 | [‘S’, ‘I1’, ‘S’, ‘I0’]                        | 2             | 0.8                | 5                | 2.4                |
| 20170217 | [‘S’, ‘I1’, ‘S’, ‘I0’]                        | 2             | 0.8                | 100              | 2.31               |
| 20170218 | [‘S’, ‘I1’, ‘S’, ‘I0’]                        | 2             | 0.8                | 100              | 2.31               |
             | 100              | 5.48               |
| 20170217 | [‘S’, ‘S’, ‘I1’, ‘I1’, ‘I1’, ‘I1’, ‘I1’, ‘S’] | 2             | 0.5                | 1                | 3.0                |
| 20170217 | [‘S’, ‘S’, ‘I1’, ‘I1’, ‘I1’, ‘I1’, ‘I1’, ‘S’] | 2             | 1.0                | 10               | 1.0                |
| 20170217 | [‘R’, ‘R’, ‘R’, ‘R’]                          | 2             | 0.5                | 10               | 0.0                |


### Paso 8: Probabilidad y gravedad de contagio

Hasta ahora hemos asumido que tomo mundo con un vecino se contagia y que la gravedad de la enfermedad (cuántos días dura) es la misma para todos, pero ahora jugaremos con esos supuestos. Modifica las funciones correspondientes para parametrizar la variable ```propensity``` que da una probabilidad de contagio de una persona con base en cuántos vecinos enfermos tiene. La probabilidad de contagio será

- 100% - Si tiene dos vecinos contagiado
- 75% - Si tiene un vecino contagiado

Al mismo tiempo, modifica el parámetro días contagiados ```d``` para que en lugar de ser un número constante sea un techo de contagio, es decir, el máximo de días contagiado será ese número pero es posible que las personas se enfermen menos tiempo, para determinar eso se usará una función random que asigne un número de días contagios entre 1 y ```d```. Vuelve a correr la simulación completa con estas dos modificaciones.

No hemos proporcionado tests para este código, por favor crea 5 tests que prueben que la función funciona



### Paso 9: La gente se mueve

Ahora vamos a asumir que la gente se mueve en su día e interactua con otra gente. Crea una función ```advance_person_at_position_move``` que modifique la función ```advance_person_at_position``` para que acepte como un parámetro adicional una lista de personas con las que se encontró en su día.

Una persona se va a contagiar con probabilidad 100% si se cumple cualquiera de las siguientes condiciones:

- Si tiene dos vecinos contagiado
- Si toda la gente con la que se encontró estába contagiada

Se contagia con probabilidad 75% si se cumple cualquiera de las siguientes condiciones:
- Si tiene un vecino contagiado
- Si 75% o más de la gente con la que se encontró estaba contagiada 

Se contagia con probabilidad 50% si se cumplen las siguientes condiciones:
- Sin vecinos contagiado
- Si 50% o más de la gente con la que se encontró estaba contagiada 

Se contagia con probabilidad 25% si se cumplen las siguientes condiciones:
- Sin vecinos contagiado
- Si 25% o más de la gente con la que se encontró estaba contagiada 

Sólo modifica esta función, un ejemplo sería

```
In [53]: advance_person_at_position_move(['S', 'V', 'S'], 0, 2, ["I0", "I1", "I2"])
Out [53]: 'I0'

```
En este caso, aunque la persona no tenía vecinos enfermos, toda la gente con la que se encontró afuera estaba enferma y por eso se contagió

### Paso 10: La ciudad se complejiza

Finalmente, modifica la función ```has_an_infected_neighbor``` para asegurarse que funciona con una matriz. En esta caso, crea una función ```has_an_infected_neighbor_matrix``` que debe revisar si la persona de arriba y abajo está contagiada (no hay contagios diagonales). 

Para representar una matriz usaremos una lista de listas de modo que la matriz
|    	|   	|    	|
|----	|---	|----	|
| I0 	| S 	| I0 	|
| S  	| S 	| R  	|
| S  	| S 	| I2 	|

Está representada por la lista:
```
city_matrix = [["I0", "R", "I0"],["S", "S", "R"],["S", "S", "I2"]]
```

En este llamar a la función has_an_infected_neighbor debería llamar a una coordenada x, y y regresar el valor

```
In [54]: has_an_infected_neighbor_matriz(city_matriz, (1,2))
Out [54]: True

```
En este caso se evaluar si el caso R en la segunda fila y tercera columna tiene un vecino infectado, su vecino de al lado no está infectado pero el de arriba y abajo sí, y por eso marca infectado. 


## Entregar la tarea
Por favor entrega la tarea con las funciones completadas del archivo .py que mandamos. Recuerda documentar muy bien las funciones y probarlas en el notebook. 
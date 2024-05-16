#pip install scikit-fuzzy
#pip install numpy scikit-fuzzy matplotlib

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

"""#Definir las Variables Difusas"""

servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'Servicio')
comida = ctrl.Antecedent(np.arange(0, 11, 1), 'Comida')
propina = ctrl.Consequent(np.arange(0, 21, 1), 'Propina')

"""#Definir los conjuntos difusos para las variables de servicio y comida.

Entendido, si deseas utilizar cuatro elementos en lugar de tres, puedes utilizar la función trapmf en lugar de trimf. La función trapmf permite definir un conjunto difuso trapezoidal con cuatro parámetros. Aquí está cómo puedes ajustar la línea para 'Pesimo':
"""

# Definir los conjuntos difusos para las variables de servicio y comida.
# Corregidos valores **** servicio['Pesimo'] = fuzz.trimf(servicio.universe, [1, 1, 3, 4])

servicio['Pesimo'] = fuzz.trapmf(servicio.universe, [1, 1, 3, 4])
servicio['Promedio'] = fuzz.trapmf(servicio.universe, [3, 4, 7, 8])
servicio['Excelente'] = fuzz.trapmf(servicio.universe, [7, 8, 10, 10])

comida['Desagradable'] = fuzz.trimf(comida.universe, [0, 3, 5])
comida['Aceptable'] = fuzz.trimf(comida.universe, [4, 7, 8])
comida['Deliciosa'] = fuzz.trimf(comida.universe, [8, 10, 10])

"""#Definir los conjuntos difusos para la variable propina"""

# Definir los conjuntos difusos para la variable propina
propina['Nada'] = fuzz.trimf(propina.universe, [0, 0, 0])
propina['Poca'] = fuzz.trimf(propina.universe, [2, 5, 8])
propina['Normal'] = fuzz.trimf(propina.universe, [7, 10, 14.07])
propina['Generosa'] = fuzz.trapmf(propina.universe, [12.7, 18, 20.1, 20.1])

"""#Definir las reglas"""

# Definir las reglas
rule1 = ctrl.Rule(comida['Desagradable'] & servicio['Pesimo'], propina['Nada'])
rule2 = ctrl.Rule(comida['Desagradable'] & servicio['Promedio'], propina['Nada'])
rule3 = ctrl.Rule(comida['Desagradable'] & servicio['Excelente'], propina['Poca'])

rule4 = ctrl.Rule(comida['Aceptable'] & servicio['Pesimo'], propina['Nada'])
rule5 = ctrl.Rule(comida['Aceptable'] & servicio['Promedio'], propina['Normal'])
rule6 = ctrl.Rule(comida['Aceptable'] & servicio['Excelente'], propina['Normal'])

rule7 = ctrl.Rule(comida['Deliciosa'] & servicio['Pesimo'], propina['Nada'])
rule8 = ctrl.Rule(comida['Deliciosa'] & servicio['Promedio'], propina['Normal'])
rule9 = ctrl.Rule(comida['Deliciosa'] & servicio['Excelente'], propina['Generosa'])

"""Crear el sistema de control difuso

"""

# Crear el sistema de control difuso
control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

"""#Crear una simulación del sistema de control difuso."""

# Crear una simulación del sistema de control difuso.
fuzzy_system = ctrl.ControlSystemSimulation(control_system)

"""# Establecer los insumos de calidad del servicio y calidad de los alimentos.

"""

# Establecer los insumos de calidad del servicio y calidad de los alimentos.
fuzzy_system.input['Servicio'] = 8.5
fuzzy_system.input['Comida'] = 2.4

"""# Calcular la salida del sistema de control difuso"""

# Calcular la salida del sistema de control difuso
fuzzy_system.compute()

"""# Obtener el monto de la propina"""

# Obtener el monto de la propina
tip_amount = fuzzy_system.output['Propina']

"""# Imprimir el monto de la propina"""

# Imprimir el monto de la propina
print(tip_amount)
print(round(tip_amount, 2))
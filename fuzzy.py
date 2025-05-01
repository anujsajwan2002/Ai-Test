import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Input variables
dirt = ctrl.Antecedent(np.arange(0, 11, 1), 'dirt')
grease = ctrl.Antecedent(np.arange(0, 11, 1), 'grease')

# Output variable
wash_time = ctrl.Consequent(np.arange(0, 31, 1), 'wash_time')

# Auto-membership functions (Low, Medium, High)
dirt.automf(3)
grease.automf(3)

# Custom membership functions for wash time
wash_time['short'] = fuzz.trimf(wash_time.universe, [0, 5, 10])
wash_time['medium'] = fuzz.trimf(wash_time.universe, [10, 15, 20])
wash_time['long'] = fuzz.trimf(wash_time.universe, [20, 25, 30])

# Fuzzy rules
rule1 = ctrl.Rule(dirt['poor'] | grease['poor'], wash_time['short'])
rule2 = ctrl.Rule(dirt['average'] | grease['average'], wash_time['medium'])
rule3 = ctrl.Rule(dirt['good'] | grease['good'], wash_time['long'])

# Create control system
washing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
washing_sim = ctrl.ControlSystemSimulation(washing_ctrl)

# Example: Set dirt and grease levels
washing_sim.input['dirt'] = 4  # High dirt
washing_sim.input['grease'] = 2  # High grease

# Compute result
washing_sim.compute()
print(f"Recommended Wash Time: {washing_sim.output['wash_time']:.2f} minutes")

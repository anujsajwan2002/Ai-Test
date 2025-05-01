import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Inputs
hard_work = ctrl.Antecedent(np.arange(0, 11, 1), 'hard_work')
physics = ctrl.Antecedent(np.arange(0, 101, 1), 'physics')
maths = ctrl.Antecedent(np.arange(0, 101, 1), 'maths')
chemistry = ctrl.Antecedent(np.arange(0, 101, 1), 'chemistry')

# Output
risk = ctrl.Consequent(np.arange(0, 11, 1), 'risk')

# Memberships for hard work
hard_work['low'] = fuzz.trimf(hard_work.universe, [0, 0, 4])
hard_work['medium'] = fuzz.trimf(hard_work.universe, [3, 5, 7])
hard_work['high'] = fuzz.trimf(hard_work.universe, [6, 10, 10])

# Memberships for marks
for subj in [physics, maths, chemistry]:
    subj['low'] = fuzz.trimf(subj.universe, [0, 0, 50])
    subj['average'] = fuzz.trimf(subj.universe, [40, 60, 80])
    subj['high'] = fuzz.trimf(subj.universe, [70, 100, 100])

# Memberships for risk
risk['low'] = fuzz.trimf(risk.universe, [0, 0, 4])
risk['medium'] = fuzz.trimf(risk.universe, [3, 5, 7])
risk['high'] = fuzz.trimf(risk.universe, [6, 10, 10])

# Rules
rules = [
    ctrl.Rule(hard_work['low'] & physics['low'], risk['high']),
    ctrl.Rule(hard_work['low'] & maths['low'], risk['high']),
    ctrl.Rule(hard_work['low'] & chemistry['low'], risk['high']),
    ctrl.Rule(hard_work['medium'] & physics['average'] & maths['average'], risk['medium']),
    ctrl.Rule(hard_work['medium'] & chemistry['low'], risk['medium']),
    ctrl.Rule(hard_work['high'] & physics['high'] & maths['high'] & chemistry['high'], risk['low']),
    ctrl.Rule(hard_work['high'] & physics['average'], risk['medium']),
    ctrl.Rule(hard_work['medium'] & maths['high'] & chemistry['high'], risk['low']),
    ctrl.Rule(hard_work['medium'] & physics['high'] & maths['low'], risk['medium']),
    ctrl.Rule(hard_work['high'] & physics['low'], risk['medium']),
    ctrl.Rule(hard_work['high'] & physics['low'] & maths['low'] & chemistry['low'], risk['medium']),  # fallback
]

# Control system
risk_ctrl = ctrl.ControlSystem(rules)
risk_sim = ctrl.ControlSystemSimulation(risk_ctrl)

# Set input values
risk_sim.input['hard_work'] = 6
risk_sim.input['physics'] = 70
risk_sim.input['maths'] = 65
risk_sim.input['chemistry'] = 50

# Compute result with error handling
try:
    risk_sim.compute()
    print(f"Calculated risk level: {risk_sim.output['risk']:.2f}")
    risk.view(sim=risk_sim)  # optional
except KeyError:
    print("Error: Unable to compute risk level. Check input values or rule coverage.")
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Inputs
hard_work = ctrl.Antecedent(np.arange(0, 11, 1), 'hard_work')
physics = ctrl.Antecedent(np.arange(0, 101, 1), 'physics')
maths = ctrl.Antecedent(np.arange(0, 101, 1), 'maths')
chemistry = ctrl.Antecedent(np.arange(0, 101, 1), 'chemistry')

# Output
risk = ctrl.Consequent(np.arange(0, 11, 1), 'risk')

# Memberships for hard work
hard_work['low'] = fuzz.trimf(hard_work.universe, [0, 0, 4])
hard_work['medium'] = fuzz.trimf(hard_work.universe, [3, 5, 7])
hard_work['high'] = fuzz.trimf(hard_work.universe, [6, 10, 10])

# Memberships for marks
for subj in [physics, maths, chemistry]:
    subj['low'] = fuzz.trimf(subj.universe, [0, 0, 50])
    subj['average'] = fuzz.trimf(subj.universe, [40, 60, 80])
    subj['high'] = fuzz.trimf(subj.universe, [70, 100, 100])

# Memberships for risk
risk['low'] = fuzz.trimf(risk.universe, [0, 0, 4])
risk['medium'] = fuzz.trimf(risk.universe, [3, 5, 7])
risk['high'] = fuzz.trimf(risk.universe, [6, 10, 10])

# Rules
rules = [
    ctrl.Rule(hard_work['low'] & physics['low'], risk['high']),
    ctrl.Rule(hard_work['low'] & maths['low'], risk['high']),
    ctrl.Rule(hard_work['low'] & chemistry['low'], risk['high']),
    ctrl.Rule(hard_work['medium'] & physics['average'] & maths['average'], risk['medium']),
    ctrl.Rule(hard_work['medium'] & chemistry['low'], risk['medium']),
    ctrl.Rule(hard_work['high'] & physics['high'] & maths['high'] & chemistry['high'], risk['low']),
    ctrl.Rule(hard_work['high'] & physics['average'], risk['medium']),
    ctrl.Rule(hard_work['medium'] & maths['high'] & chemistry['high'], risk['low']),
    ctrl.Rule(hard_work['medium'] & physics['high'] & maths['low'], risk['medium']),
    ctrl.Rule(hard_work['high'] & physics['low'], risk['medium']),
    ctrl.Rule(hard_work['high'] & physics['low'] & maths['low'] & chemistry['low'], risk['medium']),  # fallback
]

# Control system
risk_ctrl = ctrl.ControlSystem(rules)
risk_sim = ctrl.ControlSystemSimulation(risk_ctrl)

# Set input values
risk_sim.input['hard_work'] = 6
risk_sim.input['physics'] = 70
risk_sim.input['maths'] = 65
risk_sim.input['chemistry'] = 50

# Compute result with error handling
try:
    risk_sim.compute()
    print(f"Calculated risk level: {risk_sim.output['risk']:.2f}")
    risk.view(sim=risk_sim)  # optional
except KeyError:
    print("Error: Unable to compute risk level. Check input values or rule coverage.")

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Inputs and Outputs (Antecedents & Consequent)
volatility = ctrl.Antecedent(np.arange(0, 101, 1), 'volatility')
sentiment = ctrl.Antecedent(np.arange(-1, 1.1, 0.1), 'sentiment')
risk = ctrl.Consequent(np.arange(0, 101, 1), 'risk')

# 2. Membership Functions
volatility.automf(3, names=['low', 'medium', 'high'])

sentiment['negative'] = fuzz.trimf(sentiment.universe, [-1, -1, 0])
sentiment['neutral'] = fuzz.trimf(sentiment.universe, [-0.5, 0, 0.5])
sentiment['positive'] = fuzz.trimf(sentiment.universe, [0, 1, 1])

risk['low'] = fuzz.trimf(risk.universe, [0, 0, 50])
risk['medium'] = fuzz.trimf(risk.universe, [25, 50, 75])
risk['high'] = fuzz.trimf(risk.universe, [50, 100, 100])

# 3. Fuzzy Logic Rules
rule1 = ctrl.Rule(volatility['high'] | sentiment['negative'], risk['high'])
rule2 = ctrl.Rule(volatility['medium'] & sentiment['neutral'], risk['medium'])
rule3 = ctrl.Rule(volatility['low'] & sentiment['positive'], risk['low'])

risk_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
risk_simulator = ctrl.ControlSystemSimulation(risk_ctrl)

# 4. Providing Data and Testing
risk_simulator.input['volatility'] = 65
risk_simulator.input['sentiment'] = -0.2

# 5. Calculation (Defuzzification)
risk_simulator.compute()

# Print the Result
print(f"Calculated Current Risk Score: {risk_simulator.output['risk']:.2f}/100")

# 6. Plotting the Graph
risk.view(sim=risk_simulator)
plt.title("Fuzzy Logic Risk Score Distribution")
plt.show() # Required to keep the plot window open
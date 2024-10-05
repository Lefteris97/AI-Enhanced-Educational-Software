import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class FuzzyLogicSystem:
    def __init__(self):
        # Define Fuzzy Variables
        self.exercises_scores = ctrl.Antecedent(np.arange(0, 101, 1), 'exercises_scores')
        self.speaking_scores = ctrl.Antecedent(np.arange(0, 101, 1), 'speaking_scores')
        self.listening_scores = ctrl.Antecedent(np.arange(0, 101, 1), 'listening_scores')
        self.class_behaviour = ctrl.Antecedent(np.arange(0, 11, 1), 'class_behaviour')
        self.consistency = ctrl.Antecedent(np.arange(0, 11, 1), 'consistency')
        self.forum_usage = ctrl.Antecedent(np.arange(0, 11, 1), 'forum_usage')

        self.performance = ctrl.Consequent(np.arange(0, 101, 1), 'performance')

        self.exercises_scores['F'] = fuzz.trapmf(self.exercises_scores.universe, [0, 0, 45, 50])
        self.exercises_scores['D'] = fuzz.trimf(self.exercises_scores.universe, [48, 55, 62])
        self.exercises_scores['C'] = fuzz.trimf(self.exercises_scores.universe, [60, 68, 76])
        self.exercises_scores['B'] = fuzz.trimf(self.exercises_scores.universe, [74, 82, 90])
        self.exercises_scores['A'] = fuzz.trapmf(self.exercises_scores.universe, [88, 93, 100, 100])

        self.speaking_scores['F'] = fuzz.trapmf(self.speaking_scores.universe, [0, 0, 45, 50])
        self.speaking_scores['D'] = fuzz.trimf(self.speaking_scores.universe, [48, 55, 62])
        self.speaking_scores['C'] = fuzz.trimf(self.speaking_scores.universe, [60, 68, 76])
        self.speaking_scores['B'] = fuzz.trimf(self.speaking_scores.universe, [74, 82, 90])
        self.speaking_scores['A'] = fuzz.trapmf(self.speaking_scores.universe, [88, 93, 100, 100])

        self.listening_scores['F'] = fuzz.trapmf(self.listening_scores.universe, [0, 0, 45, 50])
        self.listening_scores['D'] = fuzz.trimf(self.listening_scores.universe, [48, 55, 62])
        self.listening_scores['C'] = fuzz.trimf(self.listening_scores.universe, [60, 68, 76])
        self.listening_scores['B'] = fuzz.trimf(self.listening_scores.universe, [74, 82, 90])
        self.listening_scores['A'] = fuzz.trapmf(self.listening_scores.universe, [88, 93, 100, 100])

        self.class_behaviour['Very_Poor'] = fuzz.trimf(self.class_behaviour.universe, [0, 0, 2])
        self.class_behaviour['Poor'] = fuzz.trimf(self.class_behaviour.universe, [1, 3, 4])
        self.class_behaviour['Average'] = fuzz.trimf(self.class_behaviour.universe, [3, 5, 7])
        self.class_behaviour['Good'] = fuzz.trimf(self.class_behaviour.universe, [6, 8, 9])
        self.class_behaviour['Excellent'] = fuzz.trimf(self.class_behaviour.universe, [8, 10, 10])

        self.consistency['Very_Inconsistent'] = fuzz.trimf(self.consistency.universe, [0, 0, 2])
        self.consistency['Inconsistent'] = fuzz.trimf(self.consistency.universe, [1, 3, 4])
        self.consistency['Moderate'] = fuzz.trimf(self.consistency.universe, [3, 5, 7])
        self.consistency['Consistent'] = fuzz.trimf(self.consistency.universe, [6, 8, 9])
        self.consistency['Very_Consistent'] = fuzz.trimf(self.consistency.universe, [8, 10, 10])

        self.forum_usage['Low'] = fuzz.trimf(self.forum_usage.universe, [0, 0, 3])
        self.forum_usage['Moderate'] = fuzz.trimf(self.forum_usage.universe, [2, 5, 8])
        self.forum_usage['High'] = fuzz.trimf(self.forum_usage.universe, [7, 10, 10])

        self.performance['Very_Poor'] = fuzz.trimf(self.performance.universe, [0, 0, 25])
        self.performance['Poor'] = fuzz.trimf(self.performance.universe, [20, 35, 50])
        self.performance['Average'] = fuzz.trimf(self.performance.universe, [45, 60, 75])
        self.performance['Good'] = fuzz.trimf(self.performance.universe, [70, 85, 95])
        self.performance['Excellent'] = fuzz.trimf(self.performance.universe, [90, 100, 100])

        # Define Fuzzy Rules
        rules = [
            # Excellent Performance
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent']) &
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Excellent']),

            # Good Performance

            # good grades and good attitude
            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Good']),

            # one strong subject and good attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Good']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Good']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Good']),

            # 2A - 1B, good attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Good']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Good']),

            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Good']),

            # weakness in speaking and good attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Good']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Good']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Good']),

            # excellent grades and bad attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) &
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Good']),

            # Average Performance

            # average grades and good attitude
            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            # one good subject and good attitude
            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),
            
            # one excellent subject and good attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            # overall good grades, but poor speaking and good attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            # 'Good' Performance rules, but Inconsistent

            # good grades and good attitude
            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            # one strong subject and good attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            # 2A - 1B, good attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            # weakness in speaking and good attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            # 'Good' Performance rules but Bad Behaviour

            # good grades and good attitude
            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            # one strong subject and bad attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            # 2A - 1B, bad attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            # weakness in speaking and bad attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Average']),


            # Poor Performance rules with good attitude and trying to improve
            # poor grades - good attitude
            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Average']),

            # mixed average-poor grades and good attitude
            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Average']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Average']),

            # Poor Performance

            # poor grades - good attitude
            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      self.forum_usage['Low'],
                      self.performance['Poor']),

            # mixed average-poor grades and good attitude
            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      self.forum_usage['Low'],
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      self.forum_usage['Low'],
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      self.forum_usage['Low'],
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      self.forum_usage['Low'],
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      self.forum_usage['Low'],
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      self.forum_usage['Low'],
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      self.forum_usage['Low'],
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      self.forum_usage['Low'],
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      self.forum_usage['Low'],
                      self.performance['Poor']),

            # 'Good' Performance rules, but Inconsistent and Bad Behaviour

            # good grades and good attitude
            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            # one strong subject 
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            # 2A - 1B, bad attitude and inconsistent
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            # weakness in speaking 
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            # Average Performance rules but Inconsistent

            # average grades and good attitude
            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            # one good subject and good attitude
            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),
            
            # one excellent subject and good attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            # overall good grades, but poor speaking and good attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            # Average Performance rules but Bad Behaviour

            # average grades
            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            # one good subject
            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),
            
            # one excellent subject
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            # overall good grades, but poor speaking and good attitude
            ctrl.Rule(self.exercises_scores['A'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Poor']),

            # Very Poor Performance Rules but trying to improve
            # poor grades - good attitude
            ctrl.Rule(self.exercises_scores['F'] &
                      self.speaking_scores['F'] &
                      self.listening_scores['F'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Poor']),

            # mixed grades and good attitude
            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['F'] &
                      self.listening_scores['F'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['F'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['F'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['F'] &
                      self.speaking_scores['F'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['F'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['F'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['F'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['F'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['F'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Poor']),

            ctrl.Rule(self.exercises_scores['F'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate']),
                      self.performance['Poor']),

            # Very Poor Performance

            # poor grades
            ctrl.Rule(self.exercises_scores['F'] &
                      self.speaking_scores['F'] &
                      self.listening_scores['F'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average'] | self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate'] | self.consistency['Inconsistent'] | self.consistency['Very_Inconsistent']) & 
                      self.forum_usage['Low'],
                      self.performance['Very_Poor']),

            # mixed grades and good attitude
            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['F'] &
                      self.listening_scores['F'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average'] | self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate'] | self.consistency['Inconsistent'] | self.consistency['Very_Inconsistent']) & 
                      self.forum_usage['Low'],
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['F'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['F'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average'] | self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate'] | self.consistency['Inconsistent'] | self.consistency['Very_Inconsistent']) & 
                      self.forum_usage['Low'],
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['F'] &
                      self.speaking_scores['F'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average'] | self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate'] | self.consistency['Inconsistent'] | self.consistency['Very_Inconsistent']) & 
                      self.forum_usage['Low'],
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['F'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average'] | self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate'] | self.consistency['Inconsistent'] | self.consistency['Very_Inconsistent']) & 
                      self.forum_usage['Low'],
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['F'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average'] | self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate'] | self.consistency['Inconsistent'] | self.consistency['Very_Inconsistent']) & 
                      self.forum_usage['Low'],
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['F'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average'] | self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate'] | self.consistency['Inconsistent'] | self.consistency['Very_Inconsistent']) & 
                      self.forum_usage['Low'],
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['F'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average'] | self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate'] | self.consistency['Inconsistent'] | self.consistency['Very_Inconsistent']) & 
                      self.forum_usage['Low'],
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['F'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average'] | self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate'] | self.consistency['Inconsistent'] | self.consistency['Very_Inconsistent']) & 
                      self.forum_usage['Low'],
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['F'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Excellent'] | self.class_behaviour['Good'] | self.class_behaviour['Average'] | self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Consistent'] | self.consistency['Consistent'] | self.consistency['Moderate'] | self.consistency['Inconsistent'] | self.consistency['Very_Inconsistent']) & 
                      self.forum_usage['Low'],
                      self.performance['Very_Poor']),

            # Average Performance rules, but inconsistent and bad behaviour
            # average grades 
            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            # one good subject
            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),
            
            # one excellent subject 
            ctrl.Rule(self.exercises_scores['A'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['A'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            # overall good grades, but poor speaking 
            ctrl.Rule(self.exercises_scores['A'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['A'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) &  
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      (self.speaking_scores['D'] | self.speaking_scores['F']) &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            # Poor Performance + Inconsistent / Bad Behaviour

            # poor grades
            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            # mixed average-poor grades
            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['B'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['D'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['C'] &
                      self.speaking_scores['D'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['C'] &
                      self.listening_scores['B'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor']),

            ctrl.Rule(self.exercises_scores['D'] &
                      self.speaking_scores['B'] &
                      self.listening_scores['C'] &
                      (self.class_behaviour['Poor'] | self.class_behaviour['Very_Poor']) &
                      (self.consistency['Very_Inconsistent'] | self.consistency['Inconsistent']) & 
                      (self.forum_usage['High'] | self.forum_usage['Moderate'] | self.forum_usage['Low']),
                      self.performance['Very_Poor'])

        ]

        # Add control system and simulation
        self.control_system = ctrl.ControlSystem(rules)
        self.simulation = ctrl.ControlSystemSimulation(self.control_system)

    def calculate_performance(self, exercises_scores, speaking_scores, listening_scores, class_behaviour, consistency, forum_usage):
        try:
            # Fuzzify inputs
            self.simulation.input['exercises_scores'] = exercises_scores
            self.simulation.input['speaking_scores'] = speaking_scores
            self.simulation.input['listening_scores'] = listening_scores
            self.simulation.input['class_behaviour'] = class_behaviour
            self.simulation.input['consistency'] = consistency
            self.simulation.input['forum_usage'] = forum_usage

            # Compute the result
            self.simulation.compute()

            performance_result = self.simulation.output['performance']

            return round(performance_result, 2)
        except:
            return None

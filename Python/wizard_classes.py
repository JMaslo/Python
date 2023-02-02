class WizardPlayer:
    """Mladí kouzelníci"""

    def __init__(self, name="anonym", age=0):
        self.name = name
        self.age = age

    def attack(self):
        return '''
            Zaútočili jsme, ale nepříteli jsme nezpůsobili skoro žádné zranění, musíme povolat někoho silnějšího!
        '''


class HeadWizard(WizardPlayer):
    """Velcí kouzelníci"""
    def attack_2(self):
        return '''
        Z tohohle se nepřítel už nevzpamatuje! '''

class BadWizard(WizardPlayer):
    """Voldemort a spol."""

    def expeliarmus(self):
        return "Expeliarmus!"

    def avada_kedavra(self):
        return "Avada Kedavra!"  

    def crucio(self):
        return "Crucio!"

    def imperio(self):
        return "Imperio!"  

    def speak_to_voldemort(self):
        return "My Lord, we killed all people."
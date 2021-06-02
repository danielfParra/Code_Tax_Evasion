from otree.api import *

c = Currency

doc = """
Welcome page Tax Evasion
"""

class Constants(BaseConstants):
    name_in_url = 'exp_welc'
    players_per_group = None
    num_rounds = 1

    completion_fee = cu(1.1)

    # treatments = ['baseline', 'noavoid', 'noext','simult']


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

#PAGES
class Inst1_Welcome(Page):
    pass


page_sequence = [Inst1_Welcome]
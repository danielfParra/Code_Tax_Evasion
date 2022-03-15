from otree.api import *
import numpy as np

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'example_program'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

# PAGES
class MyPage(Page):
    pass


page_sequence = [MyPage]

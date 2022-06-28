from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Daniel Parra '

doc = """
Avoiding the cost of lying - Welcome Page
"""


class Constants(BaseConstants):
    name_in_url = 'expwzb_welc'
    players_per_group = None
    num_rounds = 1

    payoff_win = c(2.5)
    payoff_lose = c(0.3)
    completion_fee = c(1.15)
    beliefs_payoff = c(0.3)

    treatments = ['baseline', 'noavoid', 'noext','simult']


class Subsession(BaseSubsession):
    def creating_session(self):

        if 'treat' in self.session.config:
            treat = self.session.config['treat']
        else:
            import itertools
            treat = itertools.cycle(['baseline', 'baseline', 'noavoid', 'noavoid', 'simult','simult', 'noext', 'noext',
                                     'baseline', 'baseline', 'noavoid', 'noavoid', 'noext', 'noext'])
            for p in self.get_players():
                p.treat = next(treat)

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    treat = models.StringField()

    # Prolific_ID = models.StringField(
    #     label='Your Prolific ID',
    # )




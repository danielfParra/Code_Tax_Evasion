from otree.api import *

doc = """
Payment information and redirect Prolific
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1

    completion_fee = cu(1.1)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class PaymentInfo(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        payoff = player.participant.payoff
        Prolific_fixed_payoff = Constants.completion_fee
        return dict(
            redemption_code=participant.label,
            Prolific_fixed_payoff=Prolific_fixed_payoff,
            payoff=payoff,
        )


class RedirectProlific(Page):
    pass


page_sequence = [PaymentInfo, RedirectProlific]

from otree.api import *

doc = """
Payment information and redirect Prolific
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1

    completion_fee = cu(1.1)
    payoff_trial = cu(0.6)


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
        Prolific_fixed_payoff = Constants.completion_fee + Constants.payoff_trial
        trial_payoff = Constants.payoff_trial
        return dict(
            redemption_code=participant.label,
            Prolific_fixed_payoff=Prolific_fixed_payoff,
            payoff=payoff,
            trial_payoff=trial_payoff,
        )


class RedirectProlific(Page):
    pass


page_sequence = [PaymentInfo, RedirectProlific]

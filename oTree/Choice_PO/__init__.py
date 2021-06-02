from otree.api import *

c = Currency

doc = """
Choice Public officials - Tax Evasion Game
"""


class Constants(BaseConstants):
    name_in_url = 'Choice_PO'
    players_per_group = None
    num_rounds = 1

    payoff_trial = cu(0.3)
    piece_rate = cu(0.05)
    money_to_take = cu(0.63)
    tax_rate = 35

    wrong_value_controlQa = cu(0.35)
    wrong_value_controlQb = cu(0.4)
    payoff_not_take = cu(0)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    embezzle = models.BooleanField()

    q1PO = models.IntegerField(
        choices=[
            [1, 'You would get {}'.format(Constants.wrong_value_controlQa)],
            [2, 'You would get {}.'.format(Constants.money_to_take)],
            [3, 'You would get {}.'.format(Constants.wrong_value_controlQb)],
        ],
        widget=widgets.RadioSelect,
    )

    q2PO = models.IntegerField(
        choices=[
            [1, 'You would get {}'.format(Constants.payoff_not_take)],
            [2, 'You would get {}.'.format(Constants.money_to_take)],
            [3, 'You would get {}.'.format(Constants.wrong_value_controlQb)],
        ],
        widget=widgets.RadioSelect,
    )

    q3PO = models.IntegerField(
        choices=[
            [1, 'Your decision affects Players B\'s earnings'],
            [2, 'You performed a encoding task in Part 1.'],
            [3, 'The {} that you can take come from the collected taxes that '
                'Players B pay for sure.'.format(Constants.money_to_take)],
        ],
        widget=widgets.RadioSelect,
    )


def q1PO_error_message(player, value):
    print('value is', value)
    if value != 2:
        return 'Recall: The money you can take is a fixed amount of {}.'.format(Constants.money_to_take)

def q2PO_error_message(player, value):
    print('value is', value)
    if value != 1:
      return 'Recall: If you decide not to take your will not receive any additional payment.'

def q3PO_error_message(player, value):
    print('value is', value)
    if not value == 1:
        return 'Recall: You do not affect Players B’s earnings because they have to pay taxes regardless of your ' \
               'decision. '


# FUNCTIONS

# PAGES
class Inst_Choice(Page):
    pass


class Control_Q(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player):
        return ['q1PO', 'q2PO', 'q3PO']

    # @staticmethod
    # def error_message(player, values):
    #     print('values is', values)
    #     if values['q1PO'] != 2 and values['q2PO'] != 1 and values['q3PO'] != 1:
    #         return 'You have something wrong'


class Decision(Page):
    form_model = "player"
    form_fields = ["embezzle"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        income = player.participant.earnings
        embezzle = player.embezzle
        player.payoff = income + (embezzle * Constants.money_to_take)


class Feedback(Page):
    @staticmethod
    def vars_for_template(player: Player):
        decision = player.embezzle
        payoff_task1 = player.participant.earnings
        payoff = player.payoff
        return dict(
            decision=decision,
            payoff_task1=payoff_task1,
            payoff=payoff
        )


page_sequence = [Inst_Choice,
                 Control_Q,
                 Decision,
                 Feedback
                 ]

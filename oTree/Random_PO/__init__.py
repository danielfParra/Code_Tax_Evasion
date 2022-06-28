from otree.api import *

c = Currency

doc = """
Random Public officials - Tax Evasion Game
"""


class Constants(BaseConstants):
    name_in_url = 'Random_PO'
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

def creating_session(subsession: Subsession):
    import csv

    f = open(__name__ + '/Choice_decisions.csv', encoding='utf-8-sig')

    rows = list(csv.DictReader(f))
    players = subsession.get_players()
    for i in range(len(players)):
        row = rows[i]
        player = players[i]
        player.embezzle = bool(int(row['embezzle']))


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    embezzle = models.BooleanField()
    CHOICE = models.BooleanField()

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
            [1, 'Winning the prize will affect Players B\'s earnings'],
            [2, 'You performed an encoding task in Part 1.'],
            [3, 'The {} that you can win come from the collected taxes that '
                'Players B pay for sure.'.format(Constants.money_to_take)],
        ],
        widget=widgets.RadioSelect,
    )


def q1PO_error_message(player, value):
    print('value is', value)
    if value != 2:
        return 'Recall: The money you can win is a fixed amount of {}.'.format(Constants.money_to_take)

def q2PO_error_message(player, value):
    print('value is', value)
    if value != 1:
      return 'Recall: If you do not win the prize, you will not receive any additional payment.'

def q3PO_error_message(player, value):
    print('value is', value)
    if not value == 1:
        return 'Recall: The lottery\'s result do not affect Players B’s earnings because they have to pay taxes ' \
               'regardless of your decision. '


# FUNCTIONS

# PAGES
class Inst_Random(Page):
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


class Lottery(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.CHOICE = 0
        income = player.participant.earnings
        player.payoff = income + (player.embezzle * Constants.money_to_take)

    @staticmethod
    def vars_for_template(player: Player):
        embezzle = player.embezzle
        return dict(
            embezzle=embezzle
        )

class Feedback(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.payoff > Constants.payoff_trial:
            player.payoff = player.payoff - Constants.payoff_trial
        else:
            player.payoff = cu(0)
        player.participant.CHOICE = player.CHOICE

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


page_sequence = [Inst_Random,
                 Control_Q,
                 Lottery,
                 Feedback
                 ]

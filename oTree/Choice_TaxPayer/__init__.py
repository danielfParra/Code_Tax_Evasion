from otree.api import *

c = Currency

doc = """
Choice Taxpayers - Tax Evasion Game
"""


class Constants(BaseConstants):
    name_in_url = 'Choice_TP'
    players_per_group = None
    num_rounds = 1

    payoff_trial = cu(0.6)
    piece_rate = cu(0.13)
    money_to_take = cu(0.63)
    tax_rate = 35
    corruptPO_high = 9  # Number of participants that embezzle in high
    no_corruptPO_high = 1  # Number of participants that embezzle in high
    corruptPO_low = 2  # Number of participants that embezzle in low
    no_corruptPO_low = 8  # Number of participants that embezzle in high

    wrong_value_controlQa = cu(0.5)
    right_value_Qa = cu(0.35)
    wrong_value_controlQb = cu(0.85)
    income_Q1 = cu(1)
    payoff_not_take = cu(0)


class Subsession(BaseSubsession):
    pass


# def creating_session(subsession: Subsession):
#     import csv
#
#     f = open(__name__ + '/pilot1_decisions.csv', encoding='utf-8-sig')
#
#     rows = list(csv.DictReader(f))
#     players = subsession.get_players()
#     for i in range(len(players)):
#         row = rows[i]
#         player = players[i]
#         player.participant_label_exp1 = row['participant_label_exp1']
#         player.embezzle = bool(int(row['embezzle']))
#         player.corruption_level = bool(int(row['corruption_level']))
#         player.cluster_number = row['cluster_number']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    reportedIncome = models.FloatField()
    embezzle = models.BooleanField()
    corruption_level = models.BooleanField()

    q1TP = models.IntegerField(
        choices=[
            [1, 'You would pay {}.'.format(Constants.wrong_value_controlQa)],
            [2, 'You would pay {}.'.format(Constants.right_value_Qa)],
            [3, 'You would pay {}.'.format(Constants.wrong_value_controlQb)],
        ],
        widget=widgets.RadioSelect,
    )

    q2TP = models.IntegerField(
        choices=[
            [1, 'All the members of your group (Players B).'],
            [2, 'The Player A matched with your group.'],
            [3, 'Only you.'],
        ],
        widget=widgets.RadioSelect,
    )

    q3TP = models.IntegerField(
        choices=[
            [1, 'Your decision affects Players A\'s earnings'],
            [2, 'You performed a encoding task in Part 1.'],
            [3, 'The {} that Player A can take correspond to the collected taxes coming '
                'from your group\'s earnings in the practice round in Part 1.'.format(Constants.money_to_take)],
        ],
        widget=widgets.RadioSelect,
    )



def q1TP_error_message(player, value):
    print('value is', value)
    if value != 2:
        return 'Recall: The tax rate is {}%.'.format(Constants.tax_rate)


def q2TP_error_message(player, value):
    print('value is', value)
    if value != 3:
        return 'Recall: You are the only one knowing your actual income. That is the reason why you need to report it ' \
               'to be taxed. '


def q3TP_error_message(player, value):
    print('value is', value)
    if not value == 1:
        return 'Recall: You do not affect Players A’s earnings because the money they can take  ' \
               'comes from the earnings in the practice round and not from your reported income. '


# PAGES

class Inst_ChoiceTP(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            red_high=Constants.corruptPO_high,
        )


class Control_Q_TP(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player):
        return ['q1TP', 'q2TP', 'q3TP']

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.embezzle = player.participant.embezzle
        player.corruption_level = player.participant.corruption_level


class Decision_TP(Page):
    form_model = "player"
    form_fields = ["reportedIncome"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        income = player.participant.earnings
        reportedIncome = player.reportedIncome
        player.payoff = income - (reportedIncome * (Constants.tax_rate / 100))

    @staticmethod
    def js_vars(player: Player):
        return dict(
            tax_rate=Constants.tax_rate / 100,
            max_report=player.participant.earnings / (Constants.tax_rate / 100),
            min_report=Constants.payoff_trial
        )

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            payoff_trial=Constants.payoff_trial,
            corruption_level=player.corruption_level,
            max_report=player.participant.earnings*100 / Constants.tax_rate,
            red_high=Constants.corruptPO_high
        )

class Takeweel(Page):
    @staticmethod
    def vars_for_template(player: Player):
        decision_PO = player.participant.embezzle
        return dict(
            decision_PO=decision_PO
        )


class Feedback_TP(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.payoff > Constants.payoff_trial:
            player.payoff = player.payoff - Constants.payoff_trial
        else:
            player.payoff = cu(0)

    @staticmethod
    def vars_for_template(player: Player):
        decision_PO = player.participant.embezzle
        payoff_task1 = player.participant.earnings
        payoff = player.payoff
        paid_taxes = round(player.reportedIncome * (Constants.tax_rate / 100), 2)
        return dict(
            decision_PO=decision_PO,
            payoff_task1=payoff_task1,
            payoff=payoff,
            paid_taxes=paid_taxes
        )


page_sequence = [Inst_ChoiceTP, Control_Q_TP, Decision_TP, Takeweel, Feedback_TP]

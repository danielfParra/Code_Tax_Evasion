from otree.api import *

c = Currency

doc = """
Welcome page Tax Evasion
"""


class Constants(BaseConstants):
    name_in_url = 'exp_welc_PO'
    players_per_group = None
    num_rounds = 1

    completion_fee = cu(1.1)


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    import csv

    f = open(__name__ + '/pilot1_decisions.csv', encoding='utf-8-sig')

    rows = list(csv.DictReader(f))
    players = subsession.get_players()
    for i in range(len(players)):
        row = rows[i]
        player = players[i]
        player.participant_label_exp1 = row['participant_label_exp1']
        player.embezzle = bool(int(row['embezzle']))
        player.corruption_level = bool(int(row['corruption_level']))
        player.cluster_number = int(row['cluster_number'])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    embezzle = models.BooleanField()
    cluster_number = models.IntegerField()
    corruption_level = models.BooleanField()
    participant_label_exp1 = models.StringField()


# PAGES
class Inst1_Welcome(Page):

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.embezzle = player.embezzle
        player.participant.cluster_number = player.cluster_number
        player.participant.corruption_level = player.corruption_level
        player.participant.participant_label_exp1 = player.participant_label_exp1


page_sequence = [Inst1_Welcome]

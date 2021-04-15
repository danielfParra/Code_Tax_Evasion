import json
import random
import string

from otree.api import *

doc = """

"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = 'encrypt_js'

    letters_per_word = 3
    use_timeout = True
    seconds_per_period = 60
    trial_words = 1

    payoff_trial = cu(0.5)
    piece_rate = cu(3)


class Subsession(BaseSubsession):
    dictionary = models.StringField()

    def creating_session(subsession):
        # Create dictionary
        letters = list(string.ascii_uppercase)
        random.shuffle(letters)
        numbers = []
        N = list(range(100, 1000))
        for i in range(27):
            choice = random.choice(N)
            N.remove(choice)
            numbers.append(choice)
        d = [letters, numbers]
        dictionary = dict([(d[0][i], d[1][i]) for i in range(26)])
        subsession.dictionary = json.dumps(dictionary)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    performance_trial = models.IntegerField(initial=0, blank=False, min=Constants.trial_words)
    mistakes_trial = models.IntegerField(initial=0, blank=True)

    performance = models.IntegerField(initial=0, blank=True)
    mistakes = models.IntegerField(initial=0, blank=True)


# Pages
class instructions1(Page):
    pass

class instructions2(Page):
    pass

class Trial(Page):
    form_model = 'player'
    form_fields = ['performance_trial', 'mistakes_trial']

    @staticmethod
    def vars_for_template(player: Player):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return dict(
            legend_list=legend_list,
            task_list=task_list,
            task_width=task_width
        )


class Task(Page):
    form_model = 'player'
    form_fields = ['performance', 'mistakes']
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    timer_text = 'Time left:'

    @staticmethod
    def vars_for_template(player: Player):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return dict(
            legend_list=legend_list,
            task_list=task_list,
            task_width=task_width
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        trial_fee = Constants.payoff_trial
        piece_rate = Constants.piece_rate
        player.payoff = trial_fee + (piece_rate * player.performance)

class Results(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.performance = player.performance
        player.participant.earnings = player.payoff
        player.payoff = 0

page_sequence = [instructions1,
                 instructions2,
                 Trial,
                 Task,
                 Results]

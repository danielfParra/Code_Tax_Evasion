from otree.api import Currency as c, currency_range
from . import pages
from otree.api import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Inst1_Welcome

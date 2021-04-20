from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Inst1_Welcome(Page):

    # form_model = 'player'
    # form_fields = ['Prolific_ID']

    def app_after_this_page(self, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if self.player.treat == 'baseline':
           return "inst_baseline"
        elif self.player.treat == 'noavoid':
            return "inst_noavoid"
        elif self.player.treat == 'simult':
            return "inst_simult"
        else:
            return "inst_noext"

    def before_next_page(self):
        self.participant.vars['treat'] = self.player.treat


page_sequence = [Inst1_Welcome]


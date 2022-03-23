from otree.api import *

c = Currency  # old name for currency; you can delete this.


def make_field(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=label,
        widget=widgets.RadioSelect,
    )


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    payoff_trial = cu(0.6)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Demographics
    age = models.IntegerField(label='What is your age?', min=18, max=100)

    gender = models.IntegerField(
        label='What is your gender?',
        choices=[[0, 'Male'], [1, 'Female'], [2, 'Rather not say'], [3, 'Other']]
    )

    education = models.IntegerField(
        choices=[[0, 'Less than High School'],
                 [1, 'High School'],
                 [2, 'Some College'],
                 [3, 'Associate Degree'],
                 [4, 'Bachelor\'s Degree'],
                 [5, 'Advanced or Professional Degree']
                 ],
        label='What is your highest level of education?'
    )
    student = models.IntegerField(
        label='Are you currently enrolled in college?',
        choices=[[0, 'No'], [1, 'Yes']]
    )
    experiments = models.IntegerField(
        label='Please give a rough estimate about the number of experiments you have participated in before',
        blank=True
    )

    reasoning = models.LongStringField(
        label='Please give a concise explanation of how you took your decisions in the experiment',
        blank=True
    )

    religion = models.IntegerField(
        choices=[[1, 'Baha\'i'],
                 [2, 'Buddhism'],
                 [3, 'Candomble'],
                 [4,
                  'Christianity (e.g. Baptist, Church of England, Roman Catholic, Methodist, Jehovah Witness, etc.)'],
                 [5, 'Hinduism'],
                 [6, 'Islam'],
                 [7, 'Jainism'],
                 [8, 'Judaism'],
                 [9, 'Non Religious (e.g. Agnostic, Atheist, No Religion)'],
                 [10, 'Paganism'],
                 [11, 'Rastafari'],
                 [12, 'Santeria'],
                 [13, 'Shinto'],
                 [14, 'Sikhism'],
                 [15, 'Spiritualism'],
                 [16, 'Taoism'],
                 [17, 'Unitarianism'],
                 [18, 'Zorastrianism'],
                 [19, 'Other'],
                 [0, 'Do Not Wish to Answer'],
                 ],
        label='What is your religious affiliation (If any)?'
    )

    q1_GASP = make_field('After realizing you have received too much change at a store, you decide to keep it because '
                         'the salesclerk doesn\'t notice. What is the likelihood that you would feel uncomfortable '
                         'about keeping the money?')
    q2_GASP = make_field('You are privately informed that you are the only one in your group that did not make the '
                         'honor society because you skipped too many days of school. What is the likelihood that this '
                         'would lead you to become more responsible about attending school?')
    q3_GASP = make_field('You rip an article out of a journal in the library and take it with you. Your teacher '
                         'discovers what you did and tells the librarian and your entire class. What is the '
                         'likelihood that this would make you would feel like a bad person?')
    q4_GASP = make_field('After making a big mistake on an important project at work in which people were depending '
                         'on you, your boss criticizes you in front of your coworkers. What is the likelihood that '
                         'you would feign sickness and leave work?')
    q5_GASP = make_field('You reveal a friend’s secret, though your friend never finds out. What is the likelihood '
                         'that your failure to keep the secret would lead you to exert extra effort to keep secrets '
                         'in the future?')
    q6_GASP = make_field('You give a bad presentation at work. Afterwards your boss tells your coworkers it was your '
                         'fault that your company lost the contract. What is the likelihood that you would feel '
                         'incompetent?')
    q7_GASP = make_field('A friend tells you that you boast a great deal. What is the likelihood that you would stop '
                         'spending time with that friend?')
    q8_GASP = make_field('Your home is very messy and unexpected guests knock on your door and invite themselves in. '
                         'What is the likelihood that you would avoid the guests until they leave?')
    q9_GASP = make_field('You secretly commit a felony. What is the likelihood that you would feel remorse about '
                         'breaking the law?')
    q10_GASP = make_field('You successfully exaggerate your damages in a lawsuit. Months later, your lies are '
                          'discovered and you are charged with perjury. What is the likelihood that you would think '
                          'you are a despicable human being?')
    q11_GASP = make_field('You strongly defend a point of view in a discussion, and though nobody was aware of it, '
                          'you realize that you were wrong. What is the likelihood that this would make you think '
                          'more carefully before you speak?')
    q12_GASP = make_field('You take office supplies home for personal use and are caught by your boss. What is the '
                          'likelihood that this would lead you to quit your job?')
    q13_GASP = make_field('You make a mistake at work and find out a coworker is blamed for the error. Later, '
                          'your coworker confronts you about your mistake. What is the likelihood that you would feel'
                          ' like a coward?')
    q14_GASP = make_field('At a coworker’s housewarming party, you spill red wine on their new creamcolored carpet. '
                          'You cover the stain with a chair so that nobody notices your mess. What is the likelihood '
                          'that you would feel that the way you acted was pathetic?')
    q15_GASP = make_field('While discussing a heated subject with friends, you suddenly realize you are shouting '
                          'though nobody seems to notice. What is the likelihood that you would try to act more '
                          'considerately toward your friends?')
    q16_GASP = make_field('You lie to people but they never find out about it. What is the likelihood that you would '
                          'feel terrible about the lies you told?')


# FUNCTIONS


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'student', 'experiments', 'reasoning', 'religion']


class GASP(Page):
    form_model = 'player'
    form_fields = ['q1_GASP', 'q2_GASP', 'q3_GASP', 'q4_GASP', 'q5_GASP',
                   'q6_GASP', 'q7_GASP', 'q8_GASP', 'q9_GASP', 'q10_GASP',
                   'q11_GASP', 'q12_GASP', 'q13_GASP', 'q14_GASP', 'q15_GASP', 'q16_GASP']


page_sequence = [Demographics]

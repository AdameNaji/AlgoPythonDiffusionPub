import random

MAX_ITERATE = 100


class Pub:
    def __init__(self, name, prob_clic_th):
        self.name = name
        self.probClicEff = 1
        self.clic = 0
        self.display = 0
        self.probClicTh = prob_clic_th


pubs = []
for i in range(1, 10):
    pubs.append(Pub("pub" + str(i), random.random()))


def display(pub):
    pub.display += 1
    pub.probClicEff = pub.clic / pub.display


def clic(pub):
    pub.clic += 1
    pub.probClicEff = pub.clic / pub.display


def full_random_choice(list_pub):
    nbr_clic = 0

    for i in range(1, MAX_ITERATE):

        rand_pub = random.choice(list_pub)
        display(rand_pub)

        if random.random() < rand_pub.probClicTh:
            clic(rand_pub)
            nbr_clic += 1

    list_pub = sorted(list_pub, key=lambda x: x.probClicEff)

    print("========== SELECTION ALÉATOIRE ==========\n")

    for pub in list_pub:
        print(pub.name + ' : ' + str(pub.probClicEff) + ' clic effectif pour une proba de clic théorique de ' +
              str(pub.probClicTh) + ' - ' + str(pub.clic) + ' realisés')

    print('Nombre de clic total : ' + str(nbr_clic))
    print('\n')


def upper_min_theorical_choice(list_pub):
    nbr_clic = 0

    for i in range(1, MAX_ITERATE):

        rand_pub = random.choice(list_pub)
        display(rand_pub)

        if random.random() < rand_pub.probClicTh:
            clic(rand_pub)
            nbr_clic += 1

        list_pub = list(filter(lambda x: x.probClicEff >= 0.5, list_pub))

    list_pub = sorted(list_pub, key=lambda x: x.probClicEff)

    print("========== SELECTION PAR MINIMUM PROBABLE ==========\n")

    for pub in list_pub:
        print(pub.name + ' : ' + str(pub.probClicEff) + ' clic effectif pour une proba de clic théorique de ' +
              str(pub.probClicTh) + ' - ' + str(pub.clic) + ' realisés')

    print('Nombre de clic total : ' + str(nbr_clic))
    print('\n')


full_random_choice(pubs)
upper_min_theorical_choice(pubs)

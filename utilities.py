import numpy as np

def invitations_split(candidates, number_of_invitations):
    """
    Random choice of volunteers who registered to get invitations to specific game
    :param candidates: (list) Names of the volunteers who registered to the game
    :param number_of_invitations: (int) Number of invitations
    :return: None
    """
    print('Registered Volunteers: {}\n'.format(candidates))
    print('Number of Invitations: {}\n'.format(number_of_invitations))
    if len(candidates)<=number_of_invitations:
        print('Enough invitations for everyone :)\n')
    else:
        print('Not enough invitations for everyone :(\n\n ***Assigning Invitations Randomly***\n')
        winners = np.random.choice(candidates, size=number_of_invitations, replace=False)
        print('Winners:\n')
        for i in range(number_of_invitations):
            print('{}\n'.format(winners[i]))
    return

if __name__ == '__main__':
    invitations_split(['Noam', 'Nimrod', 'Adam', 'Rosi', 'Assaf', 'Ido'], 3)
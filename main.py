import json
import random
import sys
import time
from os import path
from easyAI.AI.Negamax import inf
from easyAI import TwoPlayersGame, AI_Player

class DonePlayer:
    def __init__(self):
        self.t0 = time.time()

    def ask_move(self, game):
        self.t1 = time.time()
        print '[BOT]\tFinished in ' + str(round(self.t1 * 1000) - round(self.t0 * 1000)) + ' ms.'
        exit()


class RandomMoveAi:
    def __init__(self, scoring=None, win_score=+inf, tt=None):
        self.scoring = scoring
        self.tt = tt
        self.win_score = win_score

    def __call__(self, game):
        return random.choice(game.possible_moves())


class SpaceInvaders(TwoPlayersGame):
    def __init__(self, players, outputPath):
        self.players = players
        self.outputPath = outputPath
        self.score = 0
        self.nplayer = 2  # bot player starts

    def possible_moves(self):
        return [
            'Nothing',
            'MoveLeft',
            'MoveRight',
            'Shoot',
            'BuildAlienFactory',
            'BuildMissileController',
            'BuildShield'
        ]

    def make_move(self, move):
        move_file = open(path.join(self.outputPath, 'move.txt'), 'w')
        move_file.write(move + '\r\n')
        move_file.close()

        self.show()
        print '[BOT]\tMove: ' + move

    def win(self):
        return self.score >= 100  # some winning condition

    def is_over(self):
        return self.win()

    def show(self):
        # read game map to string
        with open(path.join(self.outputPath, 'map.txt'), "r") as mapFile:
            game_map = mapFile.read()

        # read game json state to dictionary
        with open(path.join(self.outputPath, 'state.json'), "r") as stateFile:
            game_state = json.loads(stateFile.read())

        # print player number
        print '[BOT]\tRound: ' + str(game_state['RoundNumber'])

        self.showPlayer(game_state['Players'][0])
        self.showPlayer(game_state['Players'][1])

        # print map
        print '[BOT]\tMap:\n' + game_map

    def showPlayer(self, player):
        playerDetails = '[BOT]\t\tPlayer ' + str(player['PlayerNumber']) + ' (' + player['PlayerName'] + ')'
        print playerDetails + '\tKills: ' + str(player['Kills'])
        print playerDetails + '\tLives: ' + str(player['Lives'])
        print playerDetails + '\tMissiles: ' + str(len(player['Missiles'])) + '/' + str(player['MissileLimit'])

    def scoring(self):
        return 0

def printUsage():
    print 'Python Sample Bot usage:'
    print
    print 'python main.py <outputPath>'
    print
    print '\toutputPath\t relative path to the folder where the engine will read & write files (eg. output)'

def main(outputPath):
    doneBot = DonePlayer()
    ai = RandomMoveAi()
    game = SpaceInvaders([doneBot, AI_Player(ai)], outputPath)
    game.play(verbose=False)

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        printUsage()
        exit(-1)

    outputPath = sys.argv[1]
    if (path.exists(outputPath) == False):
        printUsage()
        print
        print 'Error: Output folder "' + sys.argv[1] + '" does not exist.'
        exit(-1)

    main(outputPath)
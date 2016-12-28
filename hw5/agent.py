"""
### NOTICE ###
You need to upload this file.
You can add any function you want in this file.
"""
import numpy as np
import argparse
import random
import dqn
from state import State

class Agent(object):
    def __init__(self, sess, min_action_set):
        self.set_args()
        self.min_action_set = min_action_set
        self.build_dqn()
        self.state = None

    def set_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-epoch-steps", type=int, default=250000, help="how many steps (=4 frames) to run during a training epoch (approx -- will finish current game)")
        parser.add_argument("--eval-epoch-steps", type=int, default=125000, help="how many steps (=4 frames) to run during an eval epoch (approx -- will finish current game)")
        parser.add_argument("--replay-capacity", type=int, default=1000000, help="how many states to store for future training")
        parser.add_argument("--prioritized-replay", action='store_true', help="Prioritize interesting states when training (e.g. terminal or non zero rewards)")
        parser.add_argument("--compress-replay", action='store_true', help="if set replay memory will be compressed with blosc, allowing much larger replay capacity")
        parser.add_argument("--normalize-weights", action='store_true', default=True, help="if set weights/biases are normalized like torch, with std scaled by fan in to the node")
        parser.add_argument("--screen-capture-freq", type=int, default=250, help="record screens for a game this often")
        parser.add_argument("--save-model-freq", type=int, default=10000, help="save the model once per 10000 training sessions")
        parser.add_argument("--observation-steps", type=int, default=50000, help="train only after this many stesp (=4 frames)")
        parser.add_argument("--learning-rate", type=float, default=0.00025, help="learning rate (step size for optimization algo)")
        parser.add_argument("--target-model-update-freq", type=int, default=10000, help="how often (in steps) to update the target model.  Note nature paper says this is in 'number of parameter updates' but their code says steps. see tinyurl.com/hokp4y8")
        parser.add_argument("--model",default="./best_model.ckpt", help="tensorflow model checkpoint file to initialize from")
        parser.add_argument("a")
        parser.add_argument("b")
        self.args = parser.parse_args()

    def build_dqn(self):
        """
        # TODO
            You need to build your DQN here.
            And load the pre-trained model named as './best_model.ckpt'.
            For example, 
                saver.restore(self.sess, './best_model.ckpt')
        """
        self.dqn = dqn.DeepQNetwork(len(self.min_action_set), "./", self.args)


    def getSetting(self):
        """
        # TODO
            You can only modify these three parameters.
            Adding any other parameters are not allowed.
            1. action_repeat: number of time for repeating the same action 
            2. screen_type: return 0 for RGB; return 1 for GrayScale
        """
        action_repeat = 4
        screen_type = 0
        return action_repeat, screen_type

    def play(self, screen):
        """
        # TODO
            The "action" is your DQN argmax ouput.
            The "min_action_set" is used to transform DQN argmax ouput into real action number.
            For example,
                 DQN output = [0.1, 0.2, 0.1, 0.6]
                 argmax = 3
                 min_action_set = [0, 1, 3, 4]
                 real action number = 4
        """
        if self.state is None:
            self.state = State().stateByAddingScreen(screen, 0)
        else:
            self.state = self.state.stateByAddingScreen(screen, 0)
        self.screens = np.reshape(self.state.getScreens(), (1, 84, 84, 4))
        action = self.dqn.inference(self.screens)

        return self.min_action_set[action]

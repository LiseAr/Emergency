from sys import argv

from Emergency import Emergency

class Simulation:

    def __init__(self, args):
        self.run(args)

    def run(self,config):
        runs = int(config[1]) if len(config) > 1 else 50
        for _ in range(runs):
            Emergency('docs/config.txt')

if __name__ == '__main__':
    Simulation(argv)

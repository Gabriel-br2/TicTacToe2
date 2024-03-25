import os
import yaml
from datetime import datetime

# Do the main Config of the aplication
class mainConfig():
    # Begin class with parameters
    def __init__(self):
        self.config =   {'screen': {
                            'tam_x': 1000,
                            'tam_y': 650,
                            'caption': "TicTacToe"},
                         'game': {
                            'base_path': 'resource/base.png'}
                        }

    # Read the config for the aplication
    def read_config(self):
        if not os.path.exists('config'):
            os.makedirs('config')
        if os.path.isfile('config/config.yaml'):
            with open('config/config.yaml','r') as yfile:
                data = yaml.load(yfile, Loader=yaml.loader.SafeLoader)
            
            self.config = data
        else:
            print('No config file. Loading default.')
            with open('config/config.yaml','w') as yfile:
                yaml.dump(self.config,yfile) 

    # change a config in code
    def update_config(self):
        timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        os.rename('config/config.yaml','config/config_%s.yaml'%timestamp)
        with open('config/config.yaml','w') as yfile:
                yaml.dump(self.config,yfile)


if __name__ == "__main__":
    a = mainConfig()
    a.read_config()

    print(a.config)
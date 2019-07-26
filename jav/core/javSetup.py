from jav.core.javConfig import Config
from jav.core.javLogConfig import LogConfig

from os import listdir
from os.path import isfile, join 
from os.path import expanduser


class Setup(object):
    """
        Used to setup the script (fill configuration settings)
    """

    def __init__(self, log, app_config):
        mypath = expanduser('~') + '/.jav/'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        only_ymls = [f for f in onlyfiles if f.startswith('config_') and f.endswith('.yml')]

        for single_config in only_ymls:
            self.log = log
            self.config = Config(self.log, config_filename = single_config)
            self.log_config = LogConfig(self.log, app_config, self.config.config_path + 'setup.log')

    def main(self):
        self.log.info('Initiating App Setup')

        # If conf init was called when Config class was initialized, then we don't call it again
        # This would happen if setup is called before a config file was created
        if self.config.config_init is False:
            self.config.init_config()

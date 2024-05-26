import configparser
import logging
from dash_builder import logger
from  .util import Util, Env


class ConfigManager:
    def __init__(self):
        pass

    def read_config(self):
        """
        Read the configuration
        Returns:

        """
        self.config = self.read_config_file()
        # NOTE: add yaml, DB

    def get_config(self):
        """
        Get the configuration
        Returns:

        """
        return self.config

    def read_config_file(self, config_file_name=None):
        """
        Read the configuration file
        Args:
            config_file_name:

        Returns:

        """
        config = configparser.ConfigParser()

        if config_file_name is None:
            env = Util.get_env_string()
            if env == Env.DEV:
                config_file_name = "config.ini.dev"
            elif env == Env.UAT:
                config_file_name = "config.ini.staging"
            elif env == Env.PROD:
                config_file_name = "config.ini.prod"
            else:
                config_file_name = "config.ini.dev"
                # raise ValueError("Invalid environment")
        logger.info(f"Reading config file: {config_file_name}")
        config.read(config_file_name)
        logger.info(f"[DONE] Reading config file: {config_file_name}")
        return config

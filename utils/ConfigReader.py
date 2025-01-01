import configparser
import os


class ConfigReader:
    config = configparser.ConfigParser()
    config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'configuration', 'config.ini')
    config.read(config_file_path)

    @staticmethod
    def get_property(section, key):
        try:
            return ConfigReader.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Configreader error: {e}")
            return None
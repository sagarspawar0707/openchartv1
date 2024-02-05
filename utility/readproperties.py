import configparser

def getconfig():
    try:
        # Load configuration here
        config = configparser.ConfigParser()
        config.read('C:/Users/Admin/PycharmProjects/pythonSelenium/Framework2/configuration/config.ini')
        return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return None



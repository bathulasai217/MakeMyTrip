import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getDepartLocation():
        departLocation = config.get('traveller details','depatureLocation')
        return departLocation

    @staticmethod
    def getDestinyLocation():
        destinyLocation = config.get("traveller details", "destinyLocation")
        return destinyLocation

    @staticmethod
    def getMonthYear():
        monthYear = config.get("traveller details", "month_year")
        return monthYear

    @staticmethod
    def getDate():
        Date = config.get("traveller details", "date")
        return Date
    @staticmethod
    def getTitle():
        title = config.get("title", "titleflight")
        return title

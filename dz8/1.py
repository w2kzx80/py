
class Date:
    datestr="01-01-0001"
    def __init__(self, datestr):
        self.datestr = datestr

    def getInts(self):
        return [int(s) for s in self.datestr.split('-')]

    @staticmethod
    def validate(datestr):
        '''
        Я по упрощённой схеме, полной проверки не делал
        :param datestr:
        :return:
        '''
        try:
            day, month, year = [int(s) for s in datestr.split('-')]
            if month<1 or month>12:
                return False
            if day<1 or day>30:
                return False
            return True
        except:
            return False

dt1 = Date("20-03-2020")
dt2 = Date("11-02-2019")

print(dt1.getInts())
print(dt2.getInts())
print()

print(Date.validate("01-12-2020"))
print(Date.validate("01-22-2020"))
print(Date.validate("asdf-22-2020"))

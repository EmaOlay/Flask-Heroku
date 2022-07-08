from utils.DateFormat import DateFormat

class Manga():
    def __init__(self,id=None,log_date=None,name=None,last_read=None):
        self.id=id
        self.log_date=log_date
        self.name=name
        self.last_read=last_read
    def to_JSON(self):
        return{
            'id':self.id,
            'log_date':DateFormat.convert_date(self.log_date),
            'name':self.name,
            'last_read':self.last_read
        }
    

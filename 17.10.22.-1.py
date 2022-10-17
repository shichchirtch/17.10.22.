class DateString:
    def __init__(self, date_string:str):
        if not date_string.count(".") == 2:
            raise DateError ("Неверный формат даты")

        arr = date_string.split(".")
        if  0 < int(arr[0].zfill(2)) < 32:
            self.day = arr[0].zfill(2)
        else:
            raise DateError ("Неверный формат даты")
        if 0 < int(arr[1].zfill(2))<13:
            self.month = arr[1].zfill(2)
        else:
            raise DateError("Неверный формат даты")
        if 0 < int(arr[2])<3000:
            self.year = arr[2]
        else:
            raise DateError("Неверный формат даты")
        self.date_string = f'{self.day}.{self.month}.{self.year}'

    def __str__(self):
        return self.date_string

class DateError(Exception):
    pass

date_string = input()

try:
    d = DateString(date_string)
    print(d)
except DateError as e:
    print(e)

#"17.10.2022"

# s = "ddjj"
# if len(s)<5:
#     print(s.zfill(5))
# else:
#     print(s)

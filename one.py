import datetime


def get_birthdays_per_week(users):
    day_now = datetime.datetime.now().day
    month_now = datetime.datetime.now().month
    lst= {"Monday":[], "Tuesday":[], 'Wednesday':[], 'Thursday':[], "Friday":[]}
    days_spec = (datetime.datetime.now() + datetime.timedelta(days=7)).day
    for key, val in users.items():
        mark = val.strftime("%A")
        if val.month == month_now and day_now<=val.day<=days_spec:
            if mark in lst.keys():
                lst[mark].append(key)
            else:
                lst["Monday"].append(key)
    result = ''
    for key, val in lst.items():
        if len(val) >= 1:
            names = ', '.join(val)
            result += f'{key}: {names}\n'
    print(result)
    return result





if __name__=='__main__':
    user = {"Bill": datetime.date(year = 1999, month = 3, day=12),
           "Steve":datetime.date(year = 2002, month = 3, day=18),
           'Victor':datetime.date(year = 1987, month = 3, day=15)}
    get_birthdays_per_week(user)

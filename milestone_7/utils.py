def month_to_num(monthname: str):
    MonthNums = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
    month_num = MonthNums[monthname]

    return month_num

def count_by_id(database, key_date, month, key_event, dep):
    for i in database:
        di = i
        di_by_key = {}
        date = (di[key_date])
        m_n = month_to_num(month)
        if di['department'] != dep:
            pass
        elif di['department'] == dep and int(date[5:7]) == m_n:
            di_by_key['employees'] = {'name': di['Name'], f'{key_event}': f"{month.title()} {date[8:10]}"}
            di_by_key['total'] = len(di_by_key)
            return di_by_key
            
    return di_by_key     


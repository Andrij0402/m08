from datetime import datetime, timedelta

users = [
    {'name': 'aaa', 'birthday': '12.06.2001'},
    {'name': 'bbb', 'birthday': '13.06.2002'},
    {'name': 'ccc', 'birthday': '14.06.2003'},
    {'name': 'ddd', 'birthday': '15.06.2000'},
    {'name': 'eee', 'birthday': '16.06.2004'},
    {'name': 'fff', 'birthday': '17.06.1999'},
    {'name': 'ggg', 'birthday': '18.06.1998'},
    {'name': 'hhh', 'birthday': '11.06.2010'}
]

def get_birthdays_per_week():
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []

    result = {
        'Monday': monday,
        'Tuesday': tuesday,
        'Wednesday': wednesday,
        'Thursday': thursday,
        'Friday': friday
    }

    current_data = datetime.now()
    week_now = current_data.strftime('%W')
    y = current_data.year

    for i in users:
        birthday = i.get('birthday')
        m_b = datetime.strptime(birthday, '%d.%m.%Y')
        m_b = m_b.replace(year=y)
        day = m_b.strftime('%w')
        if day == '0':
            m_b = m_b + timedelta(days=1)
        if day == '6':
            m_b = m_b + timedelta(days=2)
        week = m_b.strftime('%W')

        if week == week_now:
            if day == '1' or day == '6' or day == '0':
                monday.append(i.get('name'))

            elif day == '2':
                tuesday.append(i.get('name'))

            elif day == '3':
                wednesday.append(i.get('name'))

            elif day == '4':
                thursday.append(i.get('name'))

            elif day == '5':
                friday.append(i.get('name'))

    for k, v in result.items():
        print(f'{k}: {", ".join(v)}')

    return
get_birthdays_per_week()

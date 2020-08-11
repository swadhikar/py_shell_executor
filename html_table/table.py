import pandas as pd

data = {
    'Title': ['Ticket', 'Team', 'Raised', 'Severity', 'Cause', 'Status'],
    'ticket1': [1, 'TeamA', '12-Aug-2020 01:00:00', 'major', 'server unreachable', 'closed '],
    'ticket2': [2, 'TeamB', '13-Aug-2020 06:00:00', 'minor', '/tmp/ space filled', 'started'],
    'ticket3': [3, 'TeamC', '11-Aug-2020 03:00:00', 'major', 'server unreachable', 'closed '],
    'ticket4': [4, 'TeamD', '10-Aug-2020 02:00:00', 'minor', '/tmp/ space filled', 'started'],
    'ticket5': [5, 'TeamE', '11-Aug-2020 05:00:00', 'major', 'server unreachable', 'closed '],
    'ticket6': [6, 'TeamF', '13-Aug-2020 06:00:00', 'minor', '/tmp/ space filled', 'started'],
    'ticket7': [7, 'TeamG', '13-Aug-2020 06:00:00', 'minor', '/tmp/ space filled', 'started'],
    'ticket8': [8, 'TeamH', '13-Aug-2020 06:00:00', 'minor', '/tmp/ space filled', 'started'],
    'ticket9': [9, 'TeamI', '13-Aug-2020 06:00:00', 'minor', '/tmp/ space filled', 'started']
}

html_string = '''
<html>
<head>
    <title>
        Service Now | Tickets
    </title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<h1><span class="blue">&lt;</span>Table<span class="blue">&gt;</span> <span class="yellow">Responsive</span></h1>
<h2>Tabular view of <a href="#" target="_blank">Service Now Tickets</a></h2>
<div>
{table}
</div>
</body>
</html>
'''

df = pd.DataFrame(data)
df1 = df.set_index('Title').transpose()
html_table = df1.to_html(classes=["container"], index=False)

with open('table.html', 'w') as f:
    f.write(html_string.format(table=html_table))

import pandas as pd

data = {
    'Name': ['Ticket', 'Raised', 'Severity', 'Cause', 'Status'],
    'TeamA': [1, '12-Aug-2020 01:00:00', 'major', 'server unreachable', 'closed '],
    'TeamB': [2, '13-Aug-2020 06:00:00', 'minor', '/tmp/ space filled', 'started'],
    'TeamC': [3, '11-Aug-2020 03:00:00', 'major', 'server unreachable', 'closed '],
    'TeamD': [4, '10-Aug-2020 02:00:00', 'minor', '/tmp/ space filled', 'started'],
    'TeamE': [5, '11-Aug-2020 05:00:00', 'major', 'server unreachable', 'closed ']
}

html_string = '''
<html>
<head>
    <title>HTML Pandas Dataframe with CSS</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<link rel="stylesheet" type="text/css" href="df_style.css"/>
<body>
    
    {table}

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
            integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
            crossorigin="anonymous"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
            integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
            crossorigin="anonymous"></script>

    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
            integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
            crossorigin="anonymous"></script>

    <script type='text/javascript'>
      window.onload = function() {{
        const thead = document.querySelectorAll('.table > thead');
        thead.forEach(e => e.classList.add('thead-light'));
      }}
    </script>

</body>
</html>
'''

df = pd.DataFrame(data)
html_table = df.to_html(classes=["table", "table-dark"], index=False)

with open('table.html', 'w') as f:
    f.write(html_string.format(table=html_table))

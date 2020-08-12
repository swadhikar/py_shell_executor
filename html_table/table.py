import pandas as pd

from html_table.html_util import write_html

df = pd.read_csv("tickets.csv")
df.set_index('Ticket', inplace=True)
df.index.name = None
print(df.head(3))

write_html(df.to_html(classes=['table', 'table-hover', 'table-dark', 'table-striped']))

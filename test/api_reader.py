import pandas as pd
import requests
import json

csv = 'employee.csv'


# csv = 'example.csv'

def generate_html():
    # Convert csv file into html
    df = pd.read_csv(csv)
    html_table = df.to_html(justify='center', index=False,
                            classes='table table-dark table-striped table-bordered table-hover')

    # Construct html page from table output from pandas
    html_format = '''\
    <!DOCTYPE html>
    <html>

    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
              integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>

    <body class="bg-dark">
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
    </body>
    </html>'''

    # Write html to a file
    with open('employee.html', 'w') as f:
        html_code = html_format.format(table=html_table)
        f.write(html_code)
    print('HTML file written successfully: employee.html')


def get_http_response():
    # Dummy URL
    rest_url = 'http://dummy.restapiexample.com/api/v1/employees'
    response = requests.get(rest_url)

    # # With user session
    # session = requests.Session(url_1, auth=())
    # session.get(table_url)
    # session.close()

    # With authentication
    # response = requests.get(url, auth=('user', 'pass'))

    # print(type(response.json()))
    # formatted_json = json.dumps(response.json(), indent=2)
    # print(formatted_json)

    # status = response.json()['status']
    # print(f'API status: {status}')

    data_list = response.json()['data']
    # print(type(data_list))

    # Select required parameters from JSON response

    with open(csv, 'w') as f:
        f.write('Employee ID,Name,Salary\n')
        for data in data_list:
            emp_id = data['id']
            emp_name = data['employee_name']
            emp_salary = data['employee_salary']
            f.write(f'{emp_id},{emp_name},{emp_salary}\n')

        print('CSV file written successfully!')


get_http_response()
generate_html()

# generate_html()

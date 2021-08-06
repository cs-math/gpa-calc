from bs4 import BeautifulSoup
import os

def main():
    GRADES = {'A+': 4, 'A': 3.7, 'B+': 3.3, 'B': 3, 'C+': 2.7, 'C': 2.4, 'D+': 2.2, 'D': 2, 'F': 0}

    file_name = [file for file in os.listdir() if file.endswith('.html')]
    if not file_name:
        print('Couldn\'t find an HTML file')
        return
    file_name = file_name[0]
    file = open(file_name, 'r')
    html = file.read()
    file.close()

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'class': 'table table-striped col-md-12'})
    table_rows = table.find_all('tr')
    total_hours = 0
    total_points = 0
    for table_row in table_rows:
        td = table_row.find_all('td')
        if not td:
            continue
        name = td[1].decode_contents()
        hours = int(td[3].find('p').decode_contents())
        gpa = td[6].find('p').decode_contents()
        if gpa == '':
            gpa = input(f'What is your expected grade for {name} (A+, A, B+, ...)? ').upper()
        if gpa not in GRADES.keys():
            print(f'Invalid GPA for {name}')
            return
        total_hours += hours
        total_points += hours * GRADES[gpa]
    print('Your GPA is: ' + str(round(total_points / total_hours, 3)))

if __name__ == '__main__':
    main()

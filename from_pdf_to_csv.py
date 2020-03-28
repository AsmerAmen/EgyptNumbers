import csv
import pandas as pd


def clean_from_pdf():
    new_lines = []
    with open('text_data.txt', 'r') as file:
        lines = file.readlines()
        new_lines = [l.replace('\u202b', '').replace('\u202a', '')
                         .replace('\u202c\u202c', '').replace('\u202c', '') for l in lines]
    print(new_lines)

    with open('text_data.txt', 'a') as file:
        file.writelines(new_lines)
    # line = [file.readline()]
    # print(line)
    # l2 = line[0].replace('\u202c\u202c', '')
    # print(l2)

# Male /Female
def step_1():
    lines = []
    gov = []
    with open('text_data.txt', 'r') as file:
        lines = file.readlines()

    for x in range(int(len(lines) / 5)):
        y = x * 5
        gov.append([lines[y].strip(), lines[y + 4].strip(), lines[y + 1].strip(),
                    lines[y + 2].strip(), lines[y + 3].strip()])
    for g in gov:
        print(g)

    with open('population.csv', 'w') as file:
        csv_writer = csv.writer(file, )
        for g in gov:
            g.insert(2, 2019)
            csv_writer.writerow(g)


# Urban / Rural
def step_2():
    lines = []
    urban = []
    rural = []
    urban_percent = []
    with open('text_data.txt', 'r') as file:
        lines = file.readlines()
    for i in range(27):
        urban.append(lines[i].strip())
        rural.append(lines[i+27].strip())
        urban_percent.append(lines[i+(3*27)].strip())
    # print(gov)

    df = pd.read_csv('population.csv')
    # df.drop('gov_ar', axis=1, inplace=True)
    # print(df.head())
    # df['urban'] = urban
    # df['rural'] = rural
    df['urban_per'] = urban_percent

    df.to_csv('population.csv', index=False)


def sex_age_file():

    df = pd.read_csv('text_data.txt',)
    print(df.head())
    df.drop('age_2', axis=1, inplace=True)
    df.to_csv('population_sex_age.csv', index=False)


def population_mid_year():
    years = []
    values = []
    lines = None
    with open('text_data.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        raw_line = line.strip().split()
        if len(raw_line) == 1:
            years.append(raw_line[0])
        if len(raw_line) == 3:
            values.append(raw_line)

    print(years)
    print(values)

    with open('population_over_years.csv', 'w') as file:
        csv_writer = csv.writer(file)
        for i in range(len(years)):
            csv_writer.writerow([
                years[i],
                values[i][0], values[i][1], values[i][2]
            ])


if __name__ == '__main__':
    # clean_from_pdf()
    # pass
    # step_1()
    # step_2()

    # sex_age_file()
    population_mid_year()


import requests

with open("C:/Users/tanze/Documents/Python/datten/dataset_24476_3.txt") as f:
    f_lines = f.read().splitlines() #прочитали и разделили на линии
    for line in f_lines:
        i = line
        res = requests.get(f'http://numbersapi.com/{i}/math?json=true')
        data = res.json()
        template = 'Число {} {}'
        if data['found'] == True:
            print(template.format(line, 'Interesting'))
        else:
            print(template.format(line, 'Boring')) 

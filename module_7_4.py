# Использование %:

team1_num = '%s' % '5'
team2_num = '%s' % '6'

print('В команде Мастера кода участников: ' + team1_num + ' !')
print('В команде Волшебники данных участников: ' + team2_num + ' !')
print('Итого сегодня в командах участников: ' + team1_num + ' и ' + team2_num + ' !')

# Использование format():

print('Команда Волшебники данных решила задач: {score_2} !'.format(score_2=42))
print('Волшебники данных решили задачи за {team2_time} с !'.format(team2_time=18015.2))

# Использование f-строк:

score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

challenge_result = result
print(f'Результат битвы: {challenge_result}')

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!')

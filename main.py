import time
import datetime
import pytz

fuso_horario = pytz.timezone('America/New_York')

start_challenge = "00:00"
challenge_completed = False

def desafio_diario():
    global challenge_completed
    global start_challenge_obj

    print('Desafio Diário!!')
    print('Faça 10 flexões e digite "ok" para concluir o desafio.')
    flexoes = input('10 flexões:')

    if flexoes == "ok":
        challenge_completed = True

    if challenge_completed:
        print('Parabéns!! Você Concluiu o Desafio Diário em:', datetime.datetime.now(fuso_horario).strftime("%H:%M:%S"))
    else:
        print('Você não concluiu o Desafio Diário.')
    
    start_challenge_obj += datetime.timedelta(days=1)

while True:
    now = datetime.datetime.now(fuso_horario)
    start_hour = int(start_challenge.split(":")[0])
    start_minute = int(start_challenge.split(":")[1])
    start_challenge_obj = now.replace(hour=start_hour,minute=start_minute, second=0, microsecond=0)


    if now >= start_challenge_obj:
        desafio_diario()
    
    tempo_espera = (start_challenge_obj - now).total_seconds()
    print(f"Reinicia em: {tempo_espera:.2f} segundos até {start_challenge}...")

    time.sleep(tempo_espera)
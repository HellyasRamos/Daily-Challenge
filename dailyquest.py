import time
import datetime
import pytz

fuso_horario = pytz.timezone('America/New_York')

def desafio_diario():
    print('Desafio Diário!!')
    print('Faça 10 flexões e digite "ok" para concluir o desafio.')
    while True:
        flexoes = input('10 flexões: ')
        if flexoes.lower() == "ok":
            print('Parabéns!! Você Concluiu o Desafio Diário em:', datetime.datetime.now(fuso_horario).strftime("%H:%M:%S"))
            break
        else:
            print('Por favor, faça as 10 flexões e digite "ok".')

def main():
    start_challenge = "00:00"
    while True:
        now = datetime.datetime.now(fuso_horario)
        start_hour, start_minute = map(int, start_challenge.split(":"))
        start_challenge_obj = now.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)

        if now >= start_challenge_obj:
            desafio_diario()
            start_challenge_obj += datetime.timedelta(days=1)

        tempo_espera = (start_challenge_obj - now).total_seconds()
        print(f"Reinicia em: {tempo_espera:.2f} segundos até {start_challenge}...")
        time.sleep(min(tempo_espera, 86400))  # Espera no máximo 24 horas

if __name__ == "__main__":
    main()

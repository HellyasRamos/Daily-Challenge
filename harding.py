n_flexoes = 10
    
print("Desafio Diário!!")
print(f"Faça {n_flexoes} flexões e digite 'ok' para conclui-la.")
while n_flexoes >=10:
    check = input(f"{n_flexoes} flexoes:")
    if check == "ok":
        n_flexoes += 1
        print("Parabéns!! Você concluiu o Desafio Diário em:")
    else:
        print("Por favor, faça as 10 flexões e digite 'ok'.")
        
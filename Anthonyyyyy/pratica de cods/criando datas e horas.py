from datetime import datetime, date, time

def calendario():
#data de agora com hora
    agora= datetime.now()
    print(agora)

#data de hoje
    hoje= date.today()
    print(hoje)

#data escolhida
    data_exemplo= date(2024, 3, 7)
    print(data_exemplo)

#hora escolhida
    hora_exemplo= time(14, 35, 50)
    print(hora_exemplo)
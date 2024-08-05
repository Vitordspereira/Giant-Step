from datetime import datetime, timedelta

def calc_jc(cap, tx_j, n_p):
    return cap * (1 + tx_j) ** n_p

def enc_pml(cap_in, dt_ini, dt_fim, dur_p, tx_j):
    dt_ini = datetime.strptime(dt_ini, "%d/%m/%Y")
    dt_fim = datetime.strptime(dt_fim, "%d/%m/%Y")
    
    max_luc = 0
    mel_p = (None, None)
    
    p = timedelta(days=dur_p)
    dt_at = dt_ini
    
    while dt_at + p <= dt_fim:
        dt_fim_p = dt_at + p
        n_p = dur_p
        luc = calc_jc(cap_in, tx_j, n_p)
        
        if luc > max_luc:
            max_luc = luc
            mel_p = (dt_at.strftime("%d/%m/%Y"), dt_fim_p.strftime("%d/%m/%Y"))
        
        # Avançar um dia 
        dt_at += timedelta(days=1)  
    
    return mel_p, max_luc

# Parâmetros do problema
cap_in = 10000.0  
tx_j = 0.05 / 100    
dt_ini = "01/01/2000"
dt_fim = "31/03/2022"
dur_p = 500  

mel_p, max_luc = enc_pml(cap_in, dt_ini, dt_fim, dur_p, tx_j)

print(f"Periodo mais lucrativo de {dur_p} dias:")
print(f"Inicio: {mel_p[0]}")
print(f"Termino: {mel_p[1]}")
print(f"Lucro total: R$ {max_luc:.2f}")
import streamlit as st
import json

def allenamento():
    st.markdown("# Allenamento")

    allenamenti=[]

    with open('allenamento.json', 'r') as file:
        data = json.load(file)

    for i in data['allenamento']['giorni']:
        allenamenti.append(i)


    giorni_di_allenamento=[]

    for i in allenamenti:
        giorni_di_allenamento.append(i['giorno'])

    giorno_di_allenamento = st.selectbox("Seleziona il giorno di allenamento", giorni_di_allenamento)

    for i in allenamenti:
        if i['giorno'] == giorno_di_allenamento:
            for j in i['esercizi']:
                if j.get('per_gamba'):
                    st.checkbox(f"{j['nome']} - {j['serie']}x{j['ripetizioni']} per gamba")
                elif j.get("durata"):
                    st.checkbox(f"{j['nome']} - {j['serie']}x{j['durata']}")
                else:
                    st.checkbox(f"{j['nome']} - {j['serie']}x{j['ripetizioni']}")

if __name__ == "__main__":
    allenamento() 
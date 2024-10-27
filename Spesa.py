import streamlit as st
import json
import pandas as pd

def spesa():
    st.markdown("# Spesa")

    with open('dieta.json', 'r') as file:
        data = json.load(file)['dieta']['lista_della_spesa']

    for i in data.keys():
        with st.expander(f"# {i.capitalize().replace('_',' ')}"):
            for j in data[i]:
                st.checkbox(f"{j['nome']} - {j['quantità']}")

if __name__ == "__main__":
    spesa()
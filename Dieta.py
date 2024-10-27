import streamlit as st
import json
import pandas as pd
st.markdown("# Dieta")


def dieta():
    with open('dieta.json', 'r') as file:
        data = json.load(file)['dieta']['piano_alimentare']

    for i in data.keys():
        with st.expander(f"# {i.capitalize().replace('_',' ')}"):
            for j in data[i]:
                if isinstance(j,dict):
                    st.markdown(f"### {j['nome']}")
                    df=pd.DataFrame(j['alimenti'])
                    df.insert(0, 'Fatto', False)
                    st.data_editor(df,hide_index=True)
                else:
                    df=pd.DataFrame(data[i][j])
                    df.insert(0, 'Fatto', False)
                    st.data_editor(df,hide_index=True)
    
if __name__ == "__main__":
    dieta() 
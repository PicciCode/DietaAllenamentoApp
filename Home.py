import streamlit as st
from Dieta import dieta
from Allenamento import allenamento

if "page_name" not in st.session_state:
    st.session_state["page_name"]="Dieta"


def set_sidebar():
    with st.sidebar:    
        st.title("Menu")
        opzioni=["Dieta","Allenamento"]
        opzione=st.selectbox("Seleziona un'opzione",opzioni)
        st.session_state["page_name"]=opzione


def main():
    set_sidebar()
    if st.session_state["page_name"]=="Dieta":
        dieta()
    else:
        allenamento()

if __name__ == "__main__":
    main()
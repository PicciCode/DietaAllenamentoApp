import streamlit as st
from Dieta import dieta
from Allenamento import allenamento
from Spesa import spesa

if "page_name" not in st.session_state:
    st.session_state["page_name"]="Dieta"


def set_sidebar():
    with st.sidebar:    
        st.title("Menu")
        opzioni=["Dieta","Allenamento","Spesa"]
        opzione=st.selectbox("Seleziona un'opzione",opzioni)
        st.session_state["page_name"]=opzione


def main():
    set_sidebar()
    if st.session_state["page_name"]=="Dieta":
        dieta()
    elif st.session_state["page_name"]=="Allenamento":
        allenamento()
    elif st.session_state["page_name"]=="Spesa":
        spesa()

if __name__ == "__main__":
    main()
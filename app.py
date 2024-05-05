import streamlit as st
from eda import eda_st


def main():
    menu = ['eda']

    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == menu[0]:
        eda_st()



if __name__ == '__main__':
    main()

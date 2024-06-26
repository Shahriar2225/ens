import streamlit as st
import pandas as pd
import time

st.set_page_config(layout='wide')


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown(f'<div class="main_title">OCPP Simulator</div>', unsafe_allow_html=True)


df = pd.read_csv('charge_2.csv')
last_index = len(df) - 1  

if 'index' not in st.session_state:
    st.session_state.index = 0
if 'authorized' not in st.session_state:
    st.session_state.authorized = False
    

CORRECT_PASSWORD = "kmu2024"

def update_data():
    if st.session_state.index < last_index:
        st.session_state.index += 1  
    else:
        st.session_state.index = 0  

def display_data():
    index = st.session_state.index
    data = df.iloc[[index]]

    if index == -1:
        st.stop()
        return
    
    st.markdown('<div class="sub_title">Charger 01</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    
    
    with col1:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Voltage', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["Voltage"].values[0]} V</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Current', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["Current"].values[0]} A</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('SoC', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["SoC"].values[0]} %</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col4:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Temperature', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["Temperature"].values[0]} C</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col5:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Cost', anchor=None)
        st.markdown(f'<div class="subheader-style">${data["cost"].values[0]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col6:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Status', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["Status"].values[0]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    # Charger 02 Section
    st.markdown('<div class="sub_title">Charger 02</div>', unsafe_allow_html=True)
    col7, col8, col9, col10, col11, col12 = st.columns(6)
    with col7:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Voltage')
        st.markdown(f'<div class="subheader-style">{data["Voltage"].values[0]} V</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col8:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Current')
        st.markdown(f'<div class="subheader-style">{data["Current"].values[0]} A</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col9:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('SoC')
        st.markdown(f'<div class="subheader-style">{data["SoC"].values[0]} %</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col10:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Temperature')
        st.markdown(f'<div class="subheader-style">{data["Temperature"].values[0]} C</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col11:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Cost')
        st.markdown(f'<div class="subheader-style">${data["cost"].values[0]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col12:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Status')
        st.markdown(f'<div class="subheader-style">{data["Status"].values[0]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


if not st.session_state.authorized:
    password = st.text_input("Enter password", type="password")
    if st.button("Authorize"):
        if password == CORRECT_PASSWORD:
            st.session_state.authorized = True
            st.success("Authorization successful")
            st.experimental_rerun()
        else:
            st.error("Invalid password")
else:
    
    while st.session_state.index != -1:
        update_data()
        display_data()
        time.sleep(1.25)  
        st.experimental_rerun()
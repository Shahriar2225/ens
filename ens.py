import streamlit as st
import pandas as pd
import time

st.set_page_config(layout='wide')


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown(f'<div class="main_title">Grid connected PV battry system</div>', unsafe_allow_html=True)


df = pd.read_csv('pv_bat_grid_v1.csv')
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
    
    st.markdown('<div class="sub_title">Ansan Plant</div>', unsafe_allow_html=True)
    
    col2, col3, col4, col5,col1 = st.columns(5)

    with col2:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Grid Unit price', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["grid_unit_price"].values[0]} ₩/Kwh</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Generation', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["pv_power_generation"].values[0]} KW</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col4:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('SoC', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["SoC"].values[0]} %</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col5:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Status', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["battery_charge_discharge_action"].values[0]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col1:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Profit', anchor=None)
        st.markdown(f'<div class="subheader-style">₩ {data["cost"].values[0]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    # Charger 02 Section
    #st.markdown('<div class="sub_title"></div>', unsafe_allow_html=True)
    col6, col7, col8, col9,col10 = st.columns(5)

    with col6:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Grid Unit price', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["grid_unit_price"].values[0]} ₩/Kwh</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col7:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Generation', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["pv_power_generation"].values[0]} KW</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col8:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('SoC', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["SoC_m"].values[0]} %</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col9:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Status', anchor=None)
        st.markdown(f'<div class="subheader-style">{data["battery_charge_discharge_action_m"].values[0]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col10:
        st.markdown('<div class="column-style">', unsafe_allow_html=True)
        st.subheader('Profit', anchor=None)
        st.markdown(f'<div class="subheader-style">₩ {data["cost_m"].values[0]}</div>', unsafe_allow_html=True)
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
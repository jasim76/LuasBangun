import streamlit as st
from streamlit_option_menu import option_menu

#Judul WEB
st.title('created by : mhj.jasim@gmail.com')
#Navigasi sidebar
with st.sidebar:
    selected = option_menu ('APLIKASI',
    ['Hitung Luas Persegi Panjang','Hitung Luas Segitiga','Kalulator'],
    default_index=0)

#Persegi Panjang
if (selected == 'Hitung Luas Persegi Panjang') :
    st.title ('Hitung Luas Persegi Panjang')

    panjang = st.number_input ('Masukan Nilai Panjang',0)
    lebar = st.number_input ('Masukan Nilai Lebar',0)
    hitungpp = st.button ('Hitung Luas')

    if hitungpp :
        luaspp = panjang * lebar
        st.write ('Luas Persegi Panjang adalah : ', luaspp)
        st.success (f'Luas Persegi Panjang adalah = {luaspp}')

#Segitiga
if (selected == 'Hitung Luas Segitiga') :
    st.title ('Hitung Luas Segitiga')

    alas = st.number_input ('Masukan Nilai Alas',0)
    tinggi = st.number_input ('Masukan Nilai Tinggi',0)
    hitungsgt = st.button ('Hitung Luas')

    if hitungsgt :
        luassgt = 1/2*(alas*tinggi)
        st.write ('Luas Segitiga adalah : ', luassgt)
        st.success (f'Luas Segitiga adalah = {luassgt}')

#Kalkulator
if (selected == 'Kalkulator') :
    st.title ('Kalkulator')
    result = eval(input("Enter an expression: "))
print(result)


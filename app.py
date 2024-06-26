import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Eğitim verilerini yükle
train = pd.read_csv('train.csv')

# Modeli eğit
model = LinearRegression()
X_train = train[['allelectrons_Total', 'density_Total', 'allelectrons_Average',
                 'val_e_Average', 'atomicweight_Average', 'ionenergy_Average',
                 'el_neg_chi_Average', 'R_vdw_element_Average', 'R_cov_element_Average',
                 'zaratio_Average', 'density_Average']]
y_train = train['Hardness']
model.fit(X_train, y_train)

# Streamlit başlığı
st.title("Mohs Sertliği Tahmin Uygulaması")

# Kullanıcıdan girdi alma
st.header("Mineral Özelliklerini Girin:")
allelectrons_Total = st.number_input('Toplam Elektron Sayısı')
density_Total = st.number_input('Yoğunluk (Total)')
allelectrons_Average = st.number_input('Ortalama Elektron Sayısı')
val_e_Average = st.number_input('Ortalama Değerlik Elektron Sayısı')
atomicweight_Average = st.number_input('Ortalama Atom Ağırlığı')
ionenergy_Average = st.number_input('Ortalama İyonizasyon Enerjisi')
el_neg_chi_Average = st.number_input('Ortalama Elektron Negatifliği')
R_vdw_element_Average = st.number_input('Ortalama Van der Waals Yarıçapı')
R_cov_element_Average = st.number_input('Ortalama Kovalent Yarıçap')
zaratio_Average = st.number_input('Ortalama Z/A Oranı')
density_Average = st.number_input('Ortalama Yoğunluk')

# Tahmin butonu
if st.button('Sertliği Tahmin Et'):
    input_data = np.array([[allelectrons_Total, density_Total, allelectrons_Average,
                            val_e_Average, atomicweight_Average, ionenergy_Average,
                            el_neg_chi_Average, R_vdw_element_Average, R_cov_element_Average,
                            zaratio_Average, density_Average]])
    prediction = model.predict(input_data)
    st.subheader(f"Tahmin Edilen Mohs Sertliği: {prediction[0]:.2f}")

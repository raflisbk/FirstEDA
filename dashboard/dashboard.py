import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
import streamlit as st
from streamlit.components.v1 import html

year_avg=pd.read_csv("dashboard/year_avg_data.csv")
station_avg=pd.read_csv("dashboard/station_avg_data.csv")

# Mengatur konfigurasi halaman untuk lebar yang lebih besar
st.set_page_config(page_title="Dicoding Submission", layout="wide")

st.header("Dicoding Submission")
with st.sidebar:
    st.header("Dicoding Submission")
    st.subheader("Nama \t\t: Mohamad Rafli Agung Subekti")
    st.subheader("Email \t\t: raflisbk@gmail.com")
    st.subheader("ID Dicoding \t: raflisbk")
    st.subheader("Studi case\t: Air Quality")

st.title("Distrik mana di Beijing yang memiliki tingkat konsentrasi tertinggi untuk setiap parameter kualitas udara (PM2.5, PM10, NO2, SO2, dan CO) pada periode 2013-2017?")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["PM2.5", "PM10", "NO2","SO2","CO"])
 
with tab1:
    st.header("PM2.5")
    col1,col2 = st.columns([3,2.7])
    with col1 :
        
        # Membuat peta dengan di Beijing
        mymap = folium.Map(location=[40.1002, 116.4074], zoom_start=9.38)


        heat_data = [
            [row['latitude'], row['longitude'], row['PM2.5']]
            for index, row in station_avg.iterrows()
        ]

        HeatMap(heat_data, radius=30, blur=10, max_zoom=1).add_to(mymap)


        # Menambahkan marker untuk setiap stasiun
        for index, row in station_avg.iterrows():
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=folium.Popup(f"{row['station']}", max_width=300),
                icon=folium.Icon(color='blue')
            ).add_to(mymap)


        mymap_html = mymap._repr_html_()
        html(mymap_html, height=500, width=700)


    with col2:
        sns.set_theme(style="dark")
        station_ranked = station_avg.sort_values(by="PM2.5", ascending=False)
        
        plt.figure(figsize=(12, 7.3))
        sns.barplot(
            data=station_ranked,
            x="PM2.5",
            y="station",
            hue="station",
            palette="Reds_r"
        )

        plt.title("Ranking Tingkat Konsentrasi PM2.5 di Distrik Beijing", fontsize=16)
        plt.xlabel("Konsentrasi PM2.5", fontsize=12)
        plt.ylabel("Stasiun", fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)
    

    with st.expander("Lihat Penjelasan"):
        st.write(
            """
                PM2.5 (Particulate Matter 2.5) adalah partikel udara yang memiliki diameter lebih kecil dari 2.5 mikrometer. Partikel ini sangat kecil sehingga dapat masuk ke dalam saluran pernapasan manusia, bahkan hingga ke dalam paru-paru dan sistem peredaran darah. PM2.5 terdiri dari berbagai zat kimia, termasuk debu, asap, gas, dan cairan yang berasal dari berbagai sumber, seperti kendaraan bermotor, pembakaran bahan bakar fosil, industri, pembakaran sampah, serta proses alam seperti kebakaran hutan.\n
                Distrik Dongsi di Beijing merupakan  distrik yang memiliki tingkat konsentrasi PM2.5 paling tinggi.
                Hal ini dapat dipengaruhi oleh beberapa faktor, antara lain:
                Kepadatan lalu lintas: Sebagai kawasan yang padat penduduk dan komersial, banyak kendaraan bermotor yang menyebabkan polusi udara.
                Aktivitas industri: Sektor industri di sekitar Beijing dapat menghasilkan polutan udara, termasuk PM2.5, yang terperangkap dalam atmosfer kota.
                Kondisi meteorologi: Faktor cuaca seperti angin dan hujan yang tidak cukup untuk membersihkan udara dapat menyebabkan akumulasi PM2.5 di daerah tersebut.
                Konsentrasi PM2.5 yang tinggi di Dongsi menjadi perhatian karena dapat membahayakan kesehatan masyarakat setempat, terutama bagi kelompok yang rentan. Upaya pengurangan polusi udara, seperti pengendalian emisi dari kendaraan dan pabrik, serta kebijakan untuk mengurangi pembakaran bahan bakar fosil, sangat penting untuk meningkatkan kualitas udara di kawasan ini.
            """
        )



 
with tab2:
    st.header("PM10")
    col1,col2 = st.columns([3,2.7])
    with col1 :
        
            # Membuat peta dengan pusat di Beijing
        mymap = folium.Map(location=[40.1002, 116.4074], zoom_start=9.38)

        heat_data = [
            [row['latitude'], row['longitude'], row['PM10']] 
            for index, row in station_avg.iterrows()
        ]
        HeatMap(heat_data, radius=30, blur=10, max_zoom=1).add_to(mymap)

        # Menambahkan marker untuk setiap stasiun
        for index, row in station_avg.iterrows():
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=folium.Popup(f"{row['station']}", max_width=300),
                icon=folium.Icon(color='blue')
            ).add_to(mymap)
    
        mymap_html = mymap._repr_html_()
        html(mymap_html, height=500, width=700)


    with col2:
        sns.set_theme(style="dark")
        station_ranked = station_avg.sort_values(by="PM10", ascending=False)
        
        plt.figure(figsize=(12, 7.3))
        sns.barplot(
            data=station_ranked,
            x="PM10",
            y="station",
            hue="station",
            palette="Reds_r"
        )

        plt.title("Ranking Tingkat Konsentrasi PM10 di Distrik Beijing", fontsize=16)
        plt.xlabel("Konsentrasi PM10", fontsize=12)
        plt.ylabel("Stasiun", fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)
    

    with st.expander("Lihat Penjelasan"):
        st.write(
            """
                PM10 (Particulate Matter 10) adalah partikel udara yang memiliki diameter lebih kecil dari 10 mikrometer. Meskipun lebih besar dibandingkan dengan PM2.5, partikel ini masih cukup kecil untuk dapat terhirup melalui saluran pernapasan atas manusia dan mencapai paru-paru, bahkan dapat menyebabkan masalah kesehatan serius seperti gangguan pernapasan, asma, dan penyakit jantung. PM10 terdiri dari berbagai zat kimia, termasuk debu, kotoran kendaraan, asap dari pembakaran, dan partikel yang dihasilkan oleh aktivitas industri dan alam seperti kebakaran hutan dan erosi tanah.
                            Konsentrasi PM10 yang tinggi di Gucheng menjadi perhatian serius karena dapat berdampak buruk pada kesehatan, terutama pada anak-anak, lansia, dan mereka yang memiliki masalah pernapasan atau jantung. Untuk mengurangi dampak negatif polusi udara ini, penting untuk menerapkan kebijakan pengurangan emisi kendaraan, memperketat regulasi industri, serta meningkatkan kesadaran akan pentingnya pengelolaan lingkungan yang lebih baik di kawasan tersebut.
                                                    """
        )
 
with tab3:
    st.header("N02")
    col1,col2 = st.columns([3,2.7])
    with col1 :
        
            # Membuat peta dengan pusat di Beijing
        mymap = folium.Map(location=[40.1002, 116.4074], zoom_start=9.38)

        heat_data = [
            [row['latitude'], row['longitude'], row['NO2']] 
            for index, row in station_avg.iterrows()
        ]
        HeatMap(heat_data, radius=30, blur=10, max_zoom=1).add_to(mymap)

        # Menambahkan marker untuk setiap stasiun
        for index, row in station_avg.iterrows():
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=folium.Popup(f"{row['station']}", max_width=300),
                icon=folium.Icon(color='blue')
            ).add_to(mymap)
    
        mymap_html = mymap._repr_html_()
        html(mymap_html, height=500, width=700)


    with col2:
        sns.set_theme(style="dark")
        station_ranked = station_avg.sort_values(by="NO2", ascending=False)
        
        plt.figure(figsize=(12, 7.3))
        sns.barplot(
            data=station_ranked,
            x="NO2",
            y="station",
            hue="station",
            palette="Reds_r"
        )

        plt.title("Ranking Tingkat Konsentrasi NO2 di Distrik Beijing", fontsize=16)
        plt.xlabel("Konsentrasi PM10", fontsize=12)
        plt.ylabel("Stasiun", fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)
    

    with st.expander("Lihat Penjelasan"):
        st.write(
            """
                NO2 (Nitrogen Dioxide) adalah gas beracun yang dihasilkan oleh pembakaran bahan bakar fosil, seperti kendaraan bermotor, pembangkit listrik, dan industri. Gas ini dapat menyebabkan gangguan pernapasan, memperburuk kondisi penyakit paru-paru seperti asma dan bronkitis, serta meningkatkan risiko infeksi saluran pernapasan. NO2 juga dapat bereaksi dengan senyawa lain di atmosfer untuk membentuk ozon dan partikel halus yang dapat merusak kualitas udara. Paparan jangka panjang terhadap NO2 dapat meningkatkan risiko penyakit jantung dan stroke.
                Tingginya konsentrasi NO2 di Wanliu sangat berisiko bagi kesehatan masyarakat setempat, terutama bagi individu dengan masalah pernapasan atau jantung. Oleh karena itu, pengendalian emisi kendaraan, peningkatan kualitas bahan bakar, serta pengawasan ketat terhadap industri yang berpotensi mencemari udara sangat penting untuk mengurangi tingkat polusi udara dan meningkatkan kualitas hidup di distrik ini.
            """
        )

with tab4:
    st.header("SO2")
    col1,col2 = st.columns([3,2.7])
    with col1 :
        
            # Membuat peta dengan pusat di Beijing
        mymap = folium.Map(location=[40.1002, 116.4074], zoom_start=9.38)

        heat_data = [
            [row['latitude'], row['longitude'], row['SO2']] 
            for index, row in station_avg.iterrows()
        ]
        HeatMap(heat_data, radius=30, blur=10, max_zoom=1).add_to(mymap)

        # Menambahkan marker untuk setiap stasiun
        for index, row in station_avg.iterrows():
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=folium.Popup(f"{row['station']}", max_width=300),
                icon=folium.Icon(color='blue')
            ).add_to(mymap)
    
        mymap_html = mymap._repr_html_()
        html(mymap_html, height=500, width=700)


    with col2:
        sns.set_theme(style="dark")
        station_ranked = station_avg.sort_values(by="SO2", ascending=False)
        
        plt.figure(figsize=(12, 7.3))
        sns.barplot(
            data=station_ranked,
            x="SO2",
            y="station",
            hue="station",
            palette="Reds_r"
        )

        plt.title("Ranking Tingkat Konsentrasi SO2 di Distrik Beijing", fontsize=16)
        plt.xlabel("Konsentrasi PM10", fontsize=12)
        plt.ylabel("Stasiun", fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)
    

    with st.expander("Lihat Penjelasan"):
        st.write(
            """
                SO2 (Sulfur Dioxide) adalah gas beracun yang dihasilkan terutama dari pembakaran bahan bakar fosil yang mengandung belerang, seperti batu bara dan minyak bumi, serta dari beberapa proses industri, seperti pengolahan logam. SO2 dapat bereaksi dengan udara dan air untuk membentuk asam sulfat, yang dapat menyebabkan hujan asam dan merusak lingkungan. Paparan SO2 dalam jumlah tinggi dapat menyebabkan iritasi saluran pernapasan, memperburuk asma, serta meningkatkan risiko infeksi saluran pernapasan atas dan bawah. Paparan jangka panjang terhadap SO2 juga dapat berdampak buruk bagi sistem peredaran darah dan jantung.
                Tingginya konsentrasi SO2 di Dongsi menimbulkan kekhawatiran serius bagi kesehatan masyarakat, terutama bagi individu dengan masalah pernapasan atau gangguan jantung. Oleh karena itu, upaya untuk mengurangi emisi SO2 melalui pengendalian sumber emisi industri, pembangkit listrik yang lebih ramah lingkungan, serta pengaturan ketat terhadap emisi kendaraan sangat penting untuk meningkatkan kualitas udara dan kesehatan masyarakat di daerah tersebut.
            """
        )

with tab5:
    st.header("CO")
    col1,col2 = st.columns([3,2.7])
    with col1 :
        
            # Membuat peta dengan pusat di Beijing
        mymap = folium.Map(location=[40.1002, 116.4074], zoom_start=9.38)

        heat_data = [
            [row['latitude'], row['longitude'], row['CO']] 
            for index, row in station_avg.iterrows()
        ]
        HeatMap(heat_data, radius=30, blur=10, max_zoom=1).add_to(mymap)

        # Menambahkan marker untuk setiap stasiun
        for index, row in station_avg.iterrows():
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=folium.Popup(f"{row['station']}", max_width=300),
                icon=folium.Icon(color='blue')
            ).add_to(mymap)
    
        mymap_html = mymap._repr_html_()
        html(mymap_html, height=500, width=700)


    with col2:
        sns.set_theme(style="dark")
        station_ranked = station_avg.sort_values(by="CO", ascending=False)
        
        plt.figure(figsize=(12, 7.3))
        sns.barplot(
            data=station_ranked,
            x="CO",
            y="station",
            hue="station",
            palette="Reds_r"
        )

        plt.title("Ranking Tingkat Konsentrasi CO di Distrik Beijing", fontsize=16)
        plt.xlabel("Konsentrasi PM10", fontsize=12)
        plt.ylabel("Stasiun", fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)
    

    with st.expander("Lihat Penjelasan"):
        st.write(
            """
                CO (Carbon Monoxide) adalah gas beracun yang tidak berwarna, tidak berbau, dan tidak berasa. CO terbentuk terutama dari proses pembakaran tidak sempurna bahan bakar fosil, seperti dalam kendaraan bermotor, pembangkit listrik, dan perangkat pemanas rumah tangga yang menggunakan bahan bakar seperti gas, minyak, atau batu bara. Gas ini dapat mengikat hemoglobin dalam darah dengan lebih mudah daripada oksigen, mengurangi kemampuan darah untuk mengangkut oksigen ke seluruh tubuh. Paparan CO dalam konsentrasi tinggi dapat menyebabkan gejala seperti sakit kepala, pusing, mual, kebingungan, dan bahkan kehilangan kesadaran. Dalam kasus yang lebih parah, paparan CO dapat berakibat fatal.
                Konsentrasi CO yang tinggi di Wanshouxigong menimbulkan ancaman bagi kesehatan masyarakat, terutama bagi orang-orang yang rentan, seperti anak-anak, orang tua, dan individu dengan gangguan pernapasan atau jantung. Oleh karena itu, penting untuk mengurangi emisi CO dengan meningkatkan efisiensi pembakaran pada kendaraan dan industri, serta mempromosikan penggunaan energi yang lebih bersih dan ramah lingkungan di daerah ini.
            """
        )
with st.expander("Kesimpulan"):
     st.write(
          """
             Berdasarkan analisis data kualitas udara di Beijing pada periode 2013-2017, ditemukan bahwa:
Konsentrasi Tertinggi Berdasarkan Parameter Polutan:
Distrik Dongsi menunjukkan tingkat konsentrasi tertinggi untuk parameter PM2.5 dan SO2.
Distrik Gucheng memiliki konsentrasi tertinggi untuk parameter PM10.
Distrik Wanliu mencatat konsentrasi tertinggi untuk parameter NO2.
Distrik Wanshouxigong menunjukkan konsentrasi tertinggi untuk parameter CO.
Hal ini menunjukkan bahwa kualitas udara bervariasi secara spasial di setiap distrik, dengan beberapa distrik mengalami tekanan polutan tertentu lebih tinggi dibanding lainnya.""")

st.title("Apakah kualitas udara di distrik - distrik beijing membaik atau memburuk selama periode 2013-2017?")
tab11, tab22, tab33, tab44, tab55 = st.tabs(["PM2.5", "PM10", "NO2","SO2","CO"])

# membuat dictionary untuk Batas maksimal konsentrasi polutan menurut WHO
# sumber : google
who_limits = {
    'PM2.5': 10,  
    'PM10': 20,   
    'NO2': 40,    
    'SO2': 20,    
    'CO': 9,      
    'O3': 100     
}
with tab11:
    st.header("PM2.5")
    year_avg_melted = year_avg.melt(id_vars='year', 
                                var_name='Polutan', 
                                value_name='Rata - rata konsentrasi')
   
    pm25_data = year_avg_melted[year_avg_melted['Polutan'] == 'PM2.5']

    # menggunakan batas maksimal berdasarkan dictionary yang sebelumnya dibuat
    pm25_limit = who_limits['PM2.5']


    plt.figure(figsize=(15, 5))
    heatmap_data = pm25_data.pivot(index="year", columns="Polutan", values="Rata - rata konsentrasi")


    sns.heatmap(heatmap_data, annot=True, cmap="Reds", fmt=".2f", linewidths=.5, vmin=0, vmax=pm25_limit)


    plt.title(f'Konsentrasi PM2.5 per tahun', fontsize=12)
    plt.xlabel('Polutan', fontsize=10)
    plt.ylabel('Tahun', fontsize=10)


    plt.gca().invert_yaxis()


    plt.tight_layout()
    st.pyplot(plt)

    with st.expander("Lihat Penjelasan"):
            st.write(
                """
                    Walaupun terjadi penurunan yang signifikan dalam konsentrasi PM2.5 dari tahun 2013 hingga 2017, nilai-nilai tersebut masih jauh melebihi standar WHO, yang hanya 10 µg/m³ untuk konsentrasi tahunan PM2.5. Ini menunjukkan bahwa meskipun ada upaya untuk mengurangi polusi udara, masih banyak pekerjaan yang harus dilakukan untuk mencapai kualitas udara yang aman sesuai dengan standar internasional. Kebijakan yang lebih tegas dan penerapan teknologi ramah lingkungan, serta pengurangan emisi dari sektor transportasi dan industri, menjadi kunci untuk mencapai standar kualitas udara yang lebih baik dan lebih sehat bagi masyarakat.
                """
            )

with tab22:
    year_avg_melted = year_avg.melt(id_vars='year', 
                                    var_name='Polutan', 
                                    value_name='Rata - rata konsentrasi')
 
    pm10_data = year_avg_melted[year_avg_melted['Polutan'] == 'PM10']

    # menggunakan batas maksimal berdasarkan dictionary yang sebelumnya dibuat
    pm10_limit = who_limits['PM10']


    plt.figure(figsize=(15, 5))
    heatmap_data = pm10_data.pivot(index="year", columns="Polutan", values="Rata - rata konsentrasi")


    sns.heatmap(heatmap_data, annot=True, cmap="Reds", fmt=".2f", linewidths=.5, vmin=0, vmax=pm10_limit)


    plt.title(f'Konsentrasi PM10 per tahun', fontsize=12)
    plt.xlabel('Polutan', fontsize=10)
    plt.ylabel('Tahun', fontsize=10)


    plt.gca().invert_yaxis()


    plt.tight_layout()
    st.pyplot(plt)

    with st.expander("Lihat Penjelasan"):
            st.write(
                """
                   Secara keseluruhan, data menunjukkan adanya penurunan yang cukup signifikan dalam konsentrasi PM10 dari tahun 2013 hingga 2017. Meskipun penurunan ini dapat dilihat sebagai perbaikan dalam kualitas udara, angka PM10 yang tercatat tetap lebih tinggi dari standar aman yang direkomendasikan oleh WHO (yang menetapkan batas konsentrasi tahunan PM10 sebesar 20 µg/m³). Oleh karena itu, meskipun ada kemajuan dalam mengurangi polusi udara, masih diperlukan upaya yang lebih besar untuk mengurangi emisi polutan dan mencapai kualitas udara yang lebih sehat bagi masyarakat.
                """
            )
with tab33:
    year_avg_melted = year_avg.melt(id_vars='year', 
                                var_name='Polutan', 
                                value_name='Rata - rata konsentrasi')
    no2_data = year_avg_melted[year_avg_melted['Polutan'] == 'NO2']

    # menggunakan batas maksimal berdasarkan dictionary yang sebelumnya dibuat
    no2_limit = who_limits['PM10']


    plt.figure(figsize=(15, 5))
    heatmap_data = no2_data.pivot(index="year", columns="Polutan", values="Rata - rata konsentrasi")


    sns.heatmap(heatmap_data, annot=True, cmap="Reds", fmt=".2f", linewidths=.5, vmin=0, vmax=no2_limit)


    plt.title(f'Konsentrasi NO2 per tahun', fontsize=12)
    plt.xlabel('Polutan', fontsize=10)
    plt.ylabel('Tahun', fontsize=10)


    plt.gca().invert_yaxis()


    plt.tight_layout()
    st.pyplot(plt)
    with st.expander("Lihat Penjelasan"):
            st.write(
                """
                   Secara keseluruhan, meskipun terjadi penurunan pada tahun 2015, konsentrasi NO2 dari tahun 2013 hingga 2017 menunjukkan fluktuasi yang cukup kecil. Angka-angka yang tercatat selama periode ini masih menunjukkan bahwa konsentrasi NO2 belum mencapai level yang aman menurut standar yang ditetapkan oleh WHO (yang merekomendasikan konsentrasi tahunan NO2 di bawah 40 µg/m³). Oleh karena itu, meskipun ada usaha untuk menurunkan emisi polutan ini, kualitas udara masih terpengaruh oleh emisi NO2 yang tinggi, yang berpotensi membahayakan kesehatan, terutama bagi sistem pernapasan.
                """
            )
with tab44:
    year_avg_melted = year_avg.melt(id_vars='year', 
                                var_name='Polutan', 
                                value_name='Rata - rata konsentrasi')
    
    so2_data = year_avg_melted[year_avg_melted['Polutan'] == 'SO2']

    # menggunakan batas maksimal berdasarkan dictionary yang sebelumnya dibuat
    so2_limit = who_limits['SO2']


    plt.figure(figsize=(15, 5))
    heatmap_data = so2_data.pivot(index="year", columns="Polutan", values="Rata - rata konsentrasi")


    sns.heatmap(heatmap_data, annot=True, cmap="Reds", fmt=".2f", linewidths=.5, vmin=0, vmax=so2_limit)


    plt.title(f'Konsentrasi SO2 per tahun', fontsize=12)
    plt.xlabel('Polutan', fontsize=10)
    plt.ylabel('Tahun', fontsize=10)


    plt.gca().invert_yaxis()


    plt.tight_layout()
    st.pyplot(plt)
    with st.expander("Lihat Penjelasan"):
            st.write(
                """
                   Secara keseluruhan, konsentrasi SO₂ menunjukkan tren penurunan dari tahun 2013 hingga 2016, mencerminkan keberhasilan upaya pengurangan emisi. Namun, peningkatan signifikan pada tahun 2017 menunjukkan adanya tantangan baru, seperti peningkatan penggunaan bahan bakar fosil atau kurangnya kepatuhan terhadap kebijakan lingkungan.

                Walaupun tingkat SO₂ di sebagian besar periode ini mungkin masih berada dalam batas aman, peningkatan yang tajam pada tahun 2017 mengindikasikan perlunya pengawasan yang lebih ketat dan kebijakan mitigasi yang konsisten untuk menjaga kualitas udara dan melindungi kesehatan masyarakat.
                """
            )
with tab55:
    year_avg_melted = year_avg.melt(id_vars='year', 
                                var_name='Polutan', 
                                value_name='Rata - rata konsentrasi')
    co_data = year_avg_melted[year_avg_melted['Polutan'] == 'CO']

    # menggunakan batas maksimal berdasarkan dictionary yang sebelumnya dibuat
    co_limit = who_limits['CO']


    plt.figure(figsize=(15, 5))
    heatmap_data = co_data.pivot(index="year", columns="Polutan", values="Rata - rata konsentrasi")


    sns.heatmap(heatmap_data, annot=True, cmap="Reds", fmt=".2f", linewidths=.5, vmin=0, vmax=co_limit)


    plt.title(f'Konsentrasi CO per tahun', fontsize=12)
    plt.xlabel('Polutan', fontsize=10)
    plt.ylabel('Tahun', fontsize=10)


    plt.gca().invert_yaxis()


    plt.tight_layout()
    st.pyplot(plt)
    with st.expander("Lihat Penjelasan"):
            st.write(
                """
                   SSecara keseluruhan, konsentrasi SO₂ menunjukkan tren penurunan awal dari tahun 2013 ke 2014, tetapi mulai mengalami fluktuasi dan peningkatan pada tahun-tahun berikutnya.
Peningkatan tajam pada tahun 2017 menunjukkan adanya tantangan baru dalam pengendalian emisi, seperti peningkatan konsumsi energi dari bahan bakar fosil atau kurangnya pengawasan yang memadai.

                """
            )
with st.expander("Kesimpulan"):
     st.write("""
Secara keseluruhan, terdapat tren penurunan konsentrasi PM2.5, PM10, NO2, dan CO selama lima tahun tersebut, mengindikasikan upaya perbaikan kualitas udara yang membuahkan hasil.
Namun, tingkat konsentrasi polutan masih berada di atas ambang batas aman yang direkomendasikan oleh WHO, sehingga potensi risiko kesehatan tetap tinggi."""
              )

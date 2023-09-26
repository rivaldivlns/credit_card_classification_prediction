import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    # Disable deprecation warning for pyplot
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Read the cleaned data from 'data_raw.csv'
    data_clean = pd.read_csv('data_raw.csv')

    # Application Title
    st.title("Data Visualization")

    # Sidebar to select a plot
    plot_selection = st.sidebar.selectbox("Please select a plot", ("Education Level", "Age", "Marital Status"))

    # Function to create Plot 1
    def create_plot_1():
        st.subheader('Education Level Distribution')
        plt.figure(figsize=(8, 6))
        data_clean['education_level'] = data_clean['education_level'].map({1: 'Graduate', 2: 'University', 3: 'Highschool', 4: 'Others', 5: 'Unknown', 6: 'Unknown'})
        data_clean['count'] = 1
        data_clean['education_level'].value_counts().plot(kind='bar', ax=plt.gca(), color='royalblue')
        plt.xlabel('Education Level')
        plt.ylabel('Amount')
        st.pyplot()

        # Expander for Explanation Plot 1
        with st.expander("Explanation Plot Education Level"):
            st.caption("Terlihat bahwa pada kelas University pada Education Level merupakan kelas nasabah yang paling banyak terlibat kasus gagal bayar.")

    # Function to create Plot 2
    def create_plot_2():
        st.subheader('Age Distribution')
        plt.figure(figsize=(10, 6))
        plt.hist(data_clean['age'], bins=20, edgecolor='k')
        plt.xlabel('Age')
        plt.ylabel('Amount')
        st.pyplot()

        # Expander for Explanation Plot 2
        with st.expander("Explanation Plot Age"):
            st.caption("Terlihat bahwa usia sekitar umur 25-30 merupakan usia mayoritas nasabah yang mengalami kasus gagal bayar")

    # Function to create Plot 3
    def create_plot_3():
        st.subheader('Marital Status Distribution')
        plt.figure(figsize=(8, 6))
        data_clean['marital_status'] = data_clean['marital_status'].map({1: 'Belum Menikah', 2: 'Sudah Menikah', 3: 'Bercerai'})
        data_clean['count'] = 1
        data_clean['marital_status'].value_counts().plot(kind='bar', ax=plt.gca(), color='mediumseagreen')
        plt.xlabel('Status Perkawinan')
        plt.ylabel('Amount')
        plt.xticks(rotation=0)
        st.pyplot()

        # Expander for Explanation Plot 3
        with st.expander("Explanation Plot Marital Status"):
            st.caption("Nasabah yang belum menikah merupakan nasabah yang banyak mengalami kasus gagal bayar")


    # Display the selected plot based on user choice
    if plot_selection == "Education Level":
        create_plot_1()
    elif plot_selection == "Age":
        create_plot_2()
    elif plot_selection == "Marital Status":
        create_plot_3()

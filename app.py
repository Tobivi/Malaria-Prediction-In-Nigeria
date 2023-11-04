import streamlit as st
import pickle
from PIL import Image
import matplotlib.pyplot as plt

st.title("Malaria Prediction in Nigeria")

image = Image.open('Medicine-Higher-Life-Foundation.jpg')
st.image(image, caption='Malaria Prediction')

# Load the classifier
pickle_in = open('Multinomial1.pkl', 'rb')
classifier = pickle.load(pickle_in)

options_doc_to_pat = ['High', 'Low']
options_Lab_equip = ['Not Adequate', 'Adequate']
options_avail_treated_net = ['No', 'Yes']
option_env = ['Yes', 'No']
option_Location = ['Urban','Rural']
option_diagnosis = ['Uncomplicated','Complicated']

with st.sidebar:
        st.write("Here are some of the parameters that would be inputed to give the desired result")
        st.write("Pregnancies: This to know the amount of times the individual got pregnant")
        st.write("Treated net: Was it available?(This is a yes or No answer)")
        st.write("Knowing if the environment was sanitised or not(Yes or no answer)")
        st.write("Laboratory Equipments: Are they adequate or not Adequate?")
        st.write("Location: Do you reside in the Rural or Urban area?")
        st.write("Laboratory Equipments: Are they adequate or not Adequate?")
        st.write("Lab Diagnosis: Complicated or Uncomlicated?. This works on the Mal Parasite Percentage")
        st.write("While the rest of the inputs such as Malaria Parasite Density fever,Complaints of the individual,Rate of malaria infection,age of the individual are all number inputs due to the fact they have a whole lot of categorical unique values in their columns hence they were encoded to number input")
        st.write("Availability of electricity: value of 1(stating yes) while value of 0(stating No)?")

Name = st.text_input("Name")
Pregnancies = st.number_input("The amount of times the individual got pregnant:")
Availaibility_of_treated_net = st.selectbox("Were treated net available?", options_avail_treated_net)
Season_Level_of_Rainfall_Stagnant_water_breeding = st.number_input("The level of rainfall")
High_Rate_of_Mal_Infection_Lab_Diagnosis = st.number_input("The high rate of malaria infection (Lab diagnosis)")
Malaria_Parasite_Density_Fever_Rapid_Diagnostic_TestStrip = st.number_input(
    "The malaria Parasite Density fever rapid diagnostic")
Complaints_Symptoms = st.number_input("The complaints or symptoms of the individual")
Age = st.number_input("The age of the individual")
Electricity = st.number_input('Was there availability of electricity?')
Environment_Sanitised_or_not = st.selectbox("Is the environment sanitized or not", option_env)
Doctor_to_Patient = st.selectbox("Doctor to patient", options_doc_to_pat)
Laboratory_Equipments = st.selectbox("Laboratory Equipments", options_Lab_equip)
Location = st.selectbox("Location(Urban or Rural)",option_Location)
Complicated_Uncomplicated_Lab_Diagnosis = st.selectbox("Lab Diagnosis (can either be complicated or uncomplicated)",option_diagnosis)
submit = st.button("Predict")

if submit:
    # Prepare the input data as a list with the correct order of features
    input_data = [Pregnancies, Availaibility_of_treated_net, Season_Level_of_Rainfall_Stagnant_water_breeding,
                  High_Rate_of_Mal_Infection_Lab_Diagnosis, Complaints_Symptoms, Age, Electricity,
                  Environment_Sanitised_or_not, Doctor_to_Patient, Laboratory_Equipments,
                  Malaria_Parasite_Density_Fever_Rapid_Diagnostic_TestStrip,Location,Complicated_Uncomplicated_Lab_Diagnosis]

    # Convert user inputs to the correct format
    if Availaibility_of_treated_net == 'Yes':
        input_data[1] = 1
    else:
        input_data[1] = 0

    if Doctor_to_Patient == 'High':
        input_data[8] = 1
    else:
        input_data[8] = 0

    if Laboratory_Equipments == 'Adequate':
        input_data[9] = 1
    else:
        input_data[9] = 0

    if Environment_Sanitised_or_not == "No":
        input_data[7] = 0
    else:
        input_data[7] = 1
        
    if Location == "Urban":
        input_data[11] = 1 
    else:
        input_data[11] = 0
    if Complicated_Uncomplicated_Lab_Diagnosis == "Complicated":
        input_data[-1] = 1
    else:
        input_data[-1] = 0

    # Make the prediction
    prediction = classifier.predict([input_data])

    if prediction == 0:
        st.write('Congratulations,', Name, 'you do not have malaria.')
        st.write("Hence the Lab Diagnosis states that the malaria you have is Uncomplicated stating its less than 70%")

        # Plot a bar chart to visualize the prediction
        fig, ax = plt.subplots()
        ax.bar(["Malaria Negative", "Malaria Positive"], [1, 0])
        ax.set_ylabel('Prediction')
        ax.set_title('Malaria Prediction Result')
        st.pyplot(fig)

    else:
        st.write(Name, "we are really sorry to say, but it seems like you have malaria.")
        st.write("Hence the Lab Diagnosis states that the malaria you have is Complicated stating its greater than 70%")

        # Plot a bar chart to visualize the prediction
        fig, ax = plt.subplots()
        ax.bar(["Malaria Negative", "Malaria Positive"], [0, 1])
        ax.set_ylabel('Prediction')
        ax.set_title('Malaria Prediction Result')
        st.pyplot(fig)

st.write("Developed by: Temitope Atoyebi")

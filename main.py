import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Load disease information
disease_info = pd.read_csv("disease_info.csv")
# Load doctor data
doctor_data = pd.read_csv("Disease_Doctor_Data.csv")

# Train the model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(disease_info['Information'], disease_info['Disease'])

joblib.dump(model, 'disease_prediction.pkl')[0]


# Function to detect diseases
def get_disease_detection(symptoms):
    predicted_disease = model.predict([symptoms])[0]
    return predicted_disease


# Function to get doctor suggestion and disease information
def get_doctor_suggestion(disease):
    matching_doctors = doctor_data.loc[doctor_data['Disease'] == disease]
    if not matching_doctors.empty:
        doctor_info = matching_doctors.sample(1)  # Randomly select one doctor from matching list
        specialist = doctor_info['Specialist'].values[0]
        doctor_name = doctor_info['Doctor_Name'].values[0]
    else:
        specialist = "General Physician"
        doctor_name = "Dr. Thomas Jerry Ciolino"

    # Get disease information
    disease_info_row = disease_info[disease_info['Disease'] == disease]
    information = disease_info_row['Information'].values[0]

    return specialist, doctor_name, information


# Function to interact with the user






































































































def chat():
    print(".............Welcome To Disease Detection Chatbot!.............")
    print("Chatbot: Hi there! What's your name?")
    name = input("You: ")

    print("Chatbot: Hello, " + name + "! How can I assist you today? (Enter symptoms that you have)")

    symptoms = ""
    while True:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit', 'bye', 'thank you', 'no']:
            print("Chatbot: Goodbye!")
            break
        elif user_input.strip() == '':
            print("Chatbot: It seems like you have no query. Goodbye!")
            break
        else:
            if symptoms == "":
                symptoms = user_input
            else:
                symptoms += ", " + user_input

            print("Chatbot: How many days have you been experiencing these symptoms?")
            days = input("You: ")

            print("Chatbot: Do you have any other symptoms or concerns you'd like to share? (yes/no)")
            response = input("You: ")

            if response.lower() == 'no':
                predicted_output = get_disease_detection(symptoms)

                # Check if predicted output is a disease name
                if predicted_output in disease_info['Disease'].values:
                    print("Chatbot: It seems like you might have", predicted_output)

                    specialist, doctor_name, information = get_doctor_suggestion(predicted_output)
                    print(f"Chatbot: I recommend you to consult a {specialist}. You can consult {doctor_name}.")
                    print("Chatbot: Here is some information about your disease:\n", information)
                else:
                    print("Chatbot: It seems like you might have", predicted_output)
                    print(
                        "Chatbot: For more information about this condition, please consult a healthcare professional.")

                print("Chatbot: Okay, if you have any more questions or concerns, feel free to ask!")
                break

            elif response.lower() == 'yes':
                continue
            else:

                print("Chatbot: I'm sorry, I didn't understand that. Please respond with 'yes' or 'no'.")


chat()

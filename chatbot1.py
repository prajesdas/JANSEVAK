import json

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load disease information
disease_info = pd.read_csv("disease_info.csv")
# Load doctor data
doctor_data = pd.read_csv("Disease_Doctor_Data.csv")

# Load the trained model
model = joblib.load('disease_prediction.pkl')

questions = [
    "Hi there! What's your name?",
    "Hello, {}! How can I assist you today? (Enter symptoms that you have)",
    "How many days have you been experiencing these symptoms?",
    "Do you have any other symptoms or concerns you'd like to share? (yes/no)"
]

answers = {'symptoms': [], 'days': ''}
current_question = 0

@app.route('/chat', methods=['POST'])
def chat():
    global current_question
    print(current_question)
    data = request.get_data()
    user_input = json.loads(data)['input']

    if current_question == 0:
        name = user_input
        current_question += 1
        response = questions[current_question].format(name)
    elif current_question == 1:
        symptoms = user_input
        answers['symptoms'].append(symptoms)
        current_question += 1
        response = questions[current_question]
    elif current_question == 2:
        days = user_input
        answers['days'] = days
        current_question += 1
        response = questions[current_question]
    elif current_question == 3:
        if user_input.lower() == 'yes':
            response = "Enter another symptom:"
            current_question = 1  # Ask for another symptom
        else:
            print(answers)
            response = "Goodbye!"
            current_question = 0  # Reset the conversation for the next interaction
            # Process the collected answers
            all_symptoms = ", ".join(answers['symptoms'])
            predicted_output = model.predict([all_symptoms])[0]

            if predicted_output in disease_info['Disease'].values:
                specialist, doctor_name, information = get_doctor_suggestion(predicted_output)
                response += f" It seems like you might have {predicted_output}. I recommend you to consult a {specialist}. You can consult {doctor_name}. Here is some information about your disease:\n {information}"
            else:
                response += f" It seems like you might have {predicted_output}. For more information about this condition, please consult a healthcare professional."

            answers.clear()  # Clear the answers for the next conversation\
            answers['symptoms'] = []
    else:
        response = "I'm sorry, I didn't understand that. Please respond with 'yes' or 'no'."

    return jsonify({"response": response})

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

if __name__ == '__main__':
    app.run(debug=True)

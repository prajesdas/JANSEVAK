#IMPORT LIBRARIES
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#LOAD DATASETS
data = pd.read_csv("Symptom2Disease.csv")
disease_info = pd.read_csv("disease_info.csv")

doctor_data = pd.read_csv("Disease_Doctor_Data.csv")

recovery_steps = pd.read_csv("health_conditions.csv")

# TRAIN MODEL USING NAIVE BAYES ALGORITHM

X = data['text']
Y = data['label']

model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X, Y)


# Function to detect diseases
def get_disease_detection(symptoms):
    predicted_disease = model.predict([symptoms])[0]
    return predicted_disease


# FUNCTION TO GET DOCTOR SUGGESTION
def get_doctor_suggestion(disease):
    matching_doctors = doctor_data.loc[doctor_data['Disease'] == disease]
    if not matching_doctors.empty:
        doctor_info = matching_doctors.sample(1)  # Randomly select one doctor from matching list
        specialist = doctor_info['Specialist'].values[0]
        doctor_name = doctor_info['Doctor_Name'].values[0]
    else:
        specialist = "General Physician"
        doctor_name = "Dr. Ashutosh Shukla"

    disease_info_row = disease_info[disease_info['Disease'] == disease]
    information = disease_info_row['Information'].values[0]

    recovery_steps_row = recovery_steps[recovery_steps['Condition'] == disease]
    recovery_steps_info = recovery_steps_row['Recovery Steps'].values[0]

    return specialist, doctor_name, information, recovery_steps_info


# FUNCTION FOR health_insurance
def health_insurance_info():
    print("A health insurance plan is a contract between the insurance provider and policyholder.")
    print("It provides financial coverage against hospitalisation expenses, prescription fees, medical bills, etc.")
    print(
        "You can get either reimbursement for medical expenses or cashless treatment from a network of hospitals associated with the insurance provider.")
    print("Here are some of the main benefits of a health insurance policy:")
    print("- Easy cashless claims")
    print("- Helps you manage rising medical costs")
    print("- Provides critical illness cover")
    print("- Tax benefits under section 80D up to Rs. 1 lakh")
    print("Health insurance policy covers the following hospitalisation expenses:")
    print("- Pre hospitalisation expenses")
    print("- Post hospitalisation expenses")
    print("- Hospital room rent")
    print("- Ambulance cost")
    print("- Surgery cost")
    print("- Critical illness cover")
    print("- Doctor’s consultancy fees")
    print("- Medicines")
    print("- ICU rent")
    print("- Daycare cost")


def insurance_plan_types():
    print("There are 5 major types of health insurance plans available in India:")
    print("1. Individual Health Insurance")
    print("2. Family Floater Health Insurance")
    print("3. Senior Citizens Health Insurance")
    print("4. Critical Illness Insurance")
    print("5. Group Health Insurance Plan")
    print("6. Maternity Health Insurance")


def apply_for_insurance():
    print("Please provide the following details to proceed with your health insurance application:")
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (DD/MM/YYYY): ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")

    print("\nSelect the type of health insurance plan you are interested in:")
    insurance_plan_types()
    plan_choice = input("Enter your choice (1-6): ")

    if plan_choice == "1":
        link = "https://www.hdfcergo.com/campaigns/health-insurance-detail-new?&utm_source=google_search&utm_medium=cpc&utm_campaign=Health_Search_Core_Neev-Phrase&utm_adgroup=Individual-Insurance&adid=632971424547&utm_term=individual%20health%20insurance%20schemes&utm_network=g&utm_matchtype=p&utm_device=c&utm_location=9061800&utm_sitelink={sitelink}&utm_placement=&ci=googlesearch&SEM=1&gad_source=1&gclid=Cj0KCQjwltKxBhDMARIsAG8KnqVU3TbNruBXZjgxjSSZA1MpVrq2z7tdLsHHTtRPxUPqV_l41ZYiIlUaAkUUEALw_wcB"
    elif plan_choice == "2":
        link = "https://www.careinsurance.com/health-insurance/cr/family-medical-insurance-plan-new.html?agentId=20024747&utm_source=google&utm_medium=cpc&utm_campaign=ht_ind_family-103_AD_CR_DTTWO&utm_content=rta&utm_keyword=medical%20insurance%20family%20floater&s_kwcid=AL!10397!3!594005504055!e!!g!!medical%20insurance%20family%20floater&utm_term=11806780756&utm_adgroup=140965531132&gad_source=1&gclid=Cj0KCQjwltKxBhDMARIsAG8KnqVtaTHtvoAOPR7bCzkNVyXE9Ke4sKpKaqWao_AzZ0dIQwMxb0vVWqQaAuYJEALw_wcB"
    elif plan_choice == "3":
        link = "https://www.policybazaar.com/health-insurance/senior-citizen-health-insurance/"
    elif plan_choice == "4":
        link = "https://www.policybazaar.com/health-insurance/critical-illness-insurance/"
    elif plan_choice == "5":
        link = "https://sme.icicilombard.com/employee-benefit-insurance/group-health-insurance?utm_source=google&utm_medium=cpc&utm_campaign=IL_GHI_Generic_Exact_HC_11Apr24&utm_adgroup={adgroup}&utm_term=health%20insurance%20for%20groups&utm_matchtype=e&utm_device=c&utm_content={getquote}&gad_source=1&gclid=Cj0KCQjwltKxBhDMARIsAG8KnqWKKMrFeOiV49f-dQ41DhvSG_3oCyEaxa4wBEvicKUJyNwIorJAYFIaAskaEALw_wcB"
    elif plan_choice == "6":
        link = "https://www.sbigeneral.in/health-insurance/health-edge-insurance?utm_source=google&utm_medium=cpc&utm_campaign=pt-google-sbig-healthedge-gs-lead-core-women-em-in-all-25-April-23&utm_content=women-plan&gad_source=5&gclid=EAIaIQobChMI8O2a75fyhQMV_sg8Ah0FDw6gEAAYAiAAEgLR4vD_BwE"
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
        return

    print("\nHere is the link to apply for your selected health insurance plan:")
    print(link)


def individual_health_insurance_info():
    print(
        "Individual health insurance is a type of insurance plan that provides medical coverage to individuals based on their specific sum insured.")
    print(
        "Unlike group or family health insurance plans, individual health insurance requires separate purchases for each family member.")
    print(
        "This allows for personalized coverage based on individual health needs, rather than covering the entire family.")
    print(
        "Individual health insurance plans typically offer extensive coverage for emergency medical expenses, including hospitalization costs, day care procedures, road ambulance services, alternative treatments, organ donor expenses, and more.")
    print(
        "However, it's important to note that the premium and coverage of an individual health policy cannot be shared among family members.")


def family_floater_health_insurance_info():
    print(
        "If you have a dependent family with parents, spouse, children, and siblings, it is important to buy a health insurance policy for all your family members.")
    print(
        "A family floater health insurance plan is an affordable option to obtain health insurance coverage for the complete family in a single policy.")
    print("In this type of plan, the sum insured will be shared by all the family members.")
    print(
        "In fact, it is an economical insurance plan which means a single floater policy in which the policyholder pays a single premium amount to get coverage for all family members.")


# FUNCTION FOR CHAT CONVERSATION DISEASE DETECTION AND DOCTOR SUGGESTION


def chat():
    print(".............Welcome To Disease Detection ALLY!.............")
    print("ALLY: Hi there! What's your name?")
    name = input("You: ")

    print(f"ALLY: Hello, {name}! How can I assist you today? (Enter symptoms that you have)")

    symptoms = ""
    while True:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit', 'bye', 'thank you', 'no']:
            print("ALLY: Goodbye!")
            break
        elif user_input.strip() == '':
            print("ALLY: It seems like you have no query. Goodbye!")
            break
        else:
            if symptoms == "":
                symptoms = user_input
            else:
                symptoms += ", " + user_input

            print("ALLY: How many days have you been experiencing these symptoms?")
            days = input("You: ")

            print("ALLY: Do you have any other symptoms or concerns you'd like to share? (yes/no)")
            response = input("You: ")

            if response.lower() == 'no':
                predicted_output = get_disease_detection(symptoms)

                if predicted_output in disease_info['Disease'].values:
                    print("\nALLY: It seems like you might have", predicted_output)

                    specialist, doctor_name, information, recovery_steps_info = get_doctor_suggestion(predicted_output)
                    print(f"ALLY: I recommend you to consult a {specialist}. You can consult {doctor_name}.")
                    print("\nALLY: Here is some information about your disease:\n", information)
                    print("\nALLY: Recovery Steps:\n", recovery_steps_info)
                else:
                    print("\nALLY: It seems like you might have", predicted_output)
                    print("ALLY: For more information about this condition, please consult a healthcare professional.")

                print("\nALLY: Would you like to explore health insurance options? (yes/no)")
                response = input("You: ")
                if response.lower() == 'yes':
                    healthcare_options()
                elif response.lower() == 'no':
                    print("ALLY: Okay, if you have any more questions or concerns, feel free to ask!")
                else:
                    print("ALLY: I'm sorry, I didn't understand that. Please respond with 'yes' or 'no'.")
                break

            elif response.lower() == 'yes':
                continue
            else:
                print("\nALLY: I'm sorry, I didn't understand that. Please respond with 'yes' or 'no'.")


## FUNCTION FOR CONVERSATION healthcare_options

def healthcare_options():
    print("ALLY: Do you have any questions or concerns related to health insurance? (yes/no)")
    response = input("You: ")

    if response.lower() == 'yes':
        print("ALLY: Here are some options:")
        health_insurance_info()
        print("ALLY: Would you like to know about different types of health insurance plans? (yes/no)")
        response = input("You: ")

        if response.lower() == 'yes':
            insurance_plan_types()
            print("ALLY: Would you like to apply for a health insurance plan now? (yes/no)")
            response = input("You: ")
            if response.lower() == 'yes':
                apply_for_insurance()
            elif response.lower() == 'no':
                print("ALLY: Okay, let me know if you need further assistance!")
            else:
                print("ALLY: I'm sorry, I didn't understand that. Please respond with 'yes' or 'no'.")
        elif response.lower() == 'no':
            print("ALLY: Okay, let me know if you need further assistance!")
        else:
            print("ALLY: I'm sorry, I didn't understand that. Please respond with 'yes' or 'no'.")
    elif response.lower() == 'no':
        print("ALLY: Okay, let me know if you need further assistance!")
    else:
        print("ALLY: I'm sorry, I didn't understand that. Please respond with 'yes' or 'no'.")


# Start the chat
chat()
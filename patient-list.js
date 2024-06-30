document.addEventListener("DOMContentLoaded", function() {
    const patientsData = [
        { name: "John Doe", age: 35, gender: "Male", condition: "Hypertension" },
        { name: "Jane Smith", age: 45, gender: "Female", condition: "Diabetes" },
        { name: "Robert Johnson", age: 50, gender: "Male", condition: "Arthritis" },
        { name: "Emily Davis", age: 40, gender: "Female", condition: "Asthma" },
        { name: "Michael Miller", age: 60, gender: "Male", condition: "Heart Disease" },
        { name: "Sarah Wilson", age: 55, gender: "Female", condition: "Osteoporosis" },
        // Add more patient data as needed
    ];

    const patientList = document.getElementById("patientList");

    patientsData.forEach(patient => {
        const patientItem = document.createElement("div");
        patientItem.classList.add("patient-item");
        patientItem.innerHTML = `
      <h3>${patient.name}</h3>
      <p>Age: ${patient.age}</p>
      <p>Gender: ${patient.gender}</p>
      <p>Condition: ${patient.condition}</p>
    `;
        patientList.appendChild(patientItem);
    });
});
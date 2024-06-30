document.addEventListener("DOMContentLoaded", function () {
    const addDoctorForm = document.getElementById("addDoctorForm");

    addDoctorForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const doctorName = document.getElementById("doctorName").value;
        const specialization = document.getElementById("specialization").value;
        const consultancyFee = document.getElementById("consultancyFee").value;
        const email = document.getElementById("email").value;
        const mobile = document.getElementById("mobileNumber").value;

        const doctor = {
            name: doctorName,
            specialization: specialization,
            consultancyFee: consultancyFee,
            email: email,
            mobile: mobile
        };

        fetch("/admin/add-doctor", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(doctor)
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Doctor added successfully");
                } else {
                    alert("Failed to add doctor");
                }
            });


        addDoctorForm.reset();
    });
});

fetch("/admin/doctors")
    .then(response => response.json())
    .then(data => {
        const doctorTableBody = document.querySelector("#doctorTable tbody");

        doctorTableBody.innerHTML = "";

        data.forEach(doctor => {
            const row = doctorTableBody.insertRow();

            const nameCell = row.insertCell();
            nameCell.textContent = doctor.name;

            const emailCell = row.insertCell();
            emailCell.textContent = doctor.email;

            const specializationCell = row.insertCell();
            specializationCell.textContent = doctor.specialization;

            const mobileCell = row.insertCell();
            mobileCell.textContent = doctor.mobile;

            const feeCell = row.insertCell();
            feeCell.textContent = doctor.consultancyFee;

            const actionsCell = row.insertCell();
            actionsCell.innerHTML = `
        <button onclick="openEditModal('${doctor.id}')">Edit</button>
        <button onclick="deleteDoctor('${doctor.id}')">Delete</button>
      `;
        });
    })
    .catch(error => {
        console.error("Error fetching doctor list:", error);
    });

function openEditModal(doctorId) {
    const modal = document.getElementById('editDoctorModal');
    modal.style.display = 'block';

    fetch(`/admin/doctors/${doctorId}`)
        .then(response => response.json())
        .then(doctor => {
            document.getElementById('editDoctorId').value = doctor.id;
            document.getElementById('editDoctorName').value = doctor.name;
            document.getElementById('editSpecialization').value = doctor.specialization;
            document.getElementById('editConsultancyFee').value = doctor.consultancyFee;
            document.getElementById('editMobileNumber').value = doctor.mobile;
            document.getElementById('editEmail').value = doctor.email;
        })
        .catch(error => {
            console.error('Error fetching doctor details:', error);
            closeModal();
        });
}

function closeModal() {
    const modal = document.getElementById('editDoctorModal');
    modal.style.display = 'none';
}

function updateDoctor() {
    const doctorId = document.getElementById('editDoctorId').value;
    const doctorName = document.getElementById('editDoctorName').value;
    const specialization = document.getElementById('editSpecialization').value;
    const consultancyFee = document.getElementById('editConsultancyFee').value;
    const email = document.getElementById('editEmail').value;
    const mobile = document.getElementById('editMobileNumber').value;

    const doctor = {
        id: doctorId,
        name: doctorName,
        specialization: specialization,
        consultancyFee: consultancyFee,
        email: email,
        mobile: mobile
    };

    fetch(`/admin/doctors/${doctorId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(doctor)
    })
        .then(response => response.json())
        .then(data => {

            if (data.success) {
                alert('Doctor updated successfully');
                location.reload();
            } else {
                alert('Failed to update doctor');
            }
        })
        .catch(error => {
            console.error('Error updating doctor:', error);
        });

}



function deleteDoctor(doctorId) {
    fetch(`/admin/doctors/${doctorId}`, {
        method: "DELETE"
    })
        .then(response => {
            if (response.ok) {
                // Reload the page
                location.reload();
            } else {
                console.error("Failed to delete doctor");
            }
        })
        .catch(error => {
            console.error("Error deleting doctor:", error);
        });
}

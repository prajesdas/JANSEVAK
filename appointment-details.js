document.addEventListener("DOMContentLoaded", function () {
    fetch('/admin/appointments')
        .then(response => response.json())
        .then(appointments => {
            const table = document.querySelector('.appointments-list');

            appointments.forEach(appointment => {
                const tr = document.createElement('tr');

                // Create a table data cell for each required property
                const properties = ['patientName', 'doctorName', 'email', 'mobile', 'appointmentDate', 'symptoms', 'appointmentTime'];
                properties.forEach(property => {
                    const td = document.createElement('td');
                    td.textContent = appointment[property];
                    tr.appendChild(td);
                });

                table.appendChild(tr);
            });
        })
        .catch(error => {
            console.error("Error fetching appointment list:", error);
        });
});
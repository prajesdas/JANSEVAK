document.addEventListener("DOMContentLoaded", function() {
    const sidebarLinks = document.querySelectorAll('.sidebar a');

    sidebarLinks.forEach(link => {
        link.addEventListener('click', () => {
            const activeLink = document.querySelector('.sidebar a.active');
            if (activeLink) {
                activeLink.classList.remove('active');
            }
            link.classList.add('active');
        });
    });
});

function logout() {
    window.location.href = '/logout';
}

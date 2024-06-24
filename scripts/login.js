function login() {
    const email = document.getElementById("emailDashboard").value.trim();
    const password = document.getElementById("passwordDashboard").value.trim();

    if (workers[email] && workers[email].password === password) {
        sessionStorage.setItem("user", JSON.stringify(workers[email]));
        window.location.href = "dashboard.html";
    } else {
        document.getElementById("error-message").textContent = "Invalid email or password. Please try again.";
    }
}

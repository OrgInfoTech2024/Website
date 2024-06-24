function login() {
    const email = document.getElementById("emailDashboard").value;
    const password = document.getElementById("passwordDashboard").value;

    if (workers[email] && workers[email].password === password) {
        sessionStorage.setItem("user", JSON.stringify(workers[email]));
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid email or password. Please try again.");
    }
}
document.addEventListener("DOMContentLoaded", function() {
    const user = JSON.parse(sessionStorage.getItem("user"));
    if (user) {
        document.getElementById("lastname").textContent = user.lastname;
        document.getElementById("firstname").textContent = user.firstname;
        document.getElementById("patronimic").textContent = user.patronimic;
        document.getElementById("email").textContent = user.email;
        document.getElementById("password").textContent = user.password;
        document.getElementById("job").textContent = user.job;
        document.getElementById("workplace").textContent = user.workplace;
        document.getElementById("cabinet").textContent = user.cabinet;
        document.getElementById("wage").textContent = user.wage;
        document.getElementById("create").textContent = user.create;
        document.getElementById("study").textContent = user.study;
        document.getElementById("yourchief").textContent = user.yourchief;
        document.getElementById("yourcolleagues").textContent = user.yourcolleagues;
        document.getElementById("curatorfor").textContent = user.curatorfor;
    } else {
        window.location.href = "login.html";
    }
});
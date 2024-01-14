$(document).ready(() => {
    $("#enter-Account").click(() => {
        let error = false;

        if ($("#userEmail").val() == "") {
            document.getElementById("emailError").innerText = "Write something";
            document.getElementById("emailError").classList.remove("hide");
            error = true;
        } else {
            document.getElementById("emailError").classList.add("hide");
        }

        if ($("#userPassword").val() == "") {
            document.getElementById("passwordError").innerText = "Write something";
            document.getElementById("passwordError").classList.remove("hide");
            error = true;
        } else {
            document.getElementById("passwordError").classList.add("hide");
        }

        if (!error) {
            criptLogin($("#userEmail").val(), $("#userPassword").val(), (message) => {
                if (message == "successo") {
                    localStorage.setItem("sessionUn", body.username);
                    localStorage.setItem("sessionPwd", body.password);
                } else if (message == 'utente non trovato') {
                    document.getElementById("emailError").innerText = "We didn't find anything, try to sing up";
                    document.getElementById("trysignup").href = "/auth/register";
                    document.getElementById("emailError").classList.remove("hide");
                } else if (message == "password errata") {
                    document.getElementById("passwordError").innerText = "Wrong one, nice try";
                    document.getElementById("passwordError").classList.remove("hide");
                }
            });
        }
    });
});
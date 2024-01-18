$(document).ready(() => {
    $("#enter-Account").click(() => {
        let error = false;

        if ($("#userEmail").val() == "") {
            document.getElementById("emailError").classList.remove("hide");
            error = true;
        } else {
            document.getElementById("emailError").classList.add("hide");
        }

        if ($("#userPassword").val() == "") {
            document.getElementById("passwordError").classList.remove("hide");
            error = true;
        } else {
            document.getElementById("passwordError").classList.add("hide");
        }

        if (!error) {
            startLoaderAnimation();
            criptLogin($("#userEmail").val(), $("#userPassword").val(), (result) => {

                if (result.message == "successo") {
                    localStorage.setItem("sessionUn", body.username);
                    localStorage.setItem("sessionPwd", body.password);
                    stopLoaderAnimation();

                } else if (result.message == 'utente non trovato') {
                    document.getElementById("emailErrorSpan").innerText = "We didn't find anything, try to sing up";
                    document.getElementById("trysignup").href = "/auth/register";
                    document.getElementById("emailError").classList.remove("hide");
                    stopLoaderAnimation();

                } else if (result.message == "password errata") {
                    document.getElementById("passwordErrorSpan").innerText = "Wrong one, nice try";
                    document.getElementById("passwordError").classList.remove("hide");
                    stopLoaderAnimation();
                }
            });
        }
    });
});
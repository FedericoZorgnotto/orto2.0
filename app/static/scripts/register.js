$(document).ready(() => {
    $("#create-Account").click(() => {
        let error = false;

        if ($("#userName").val() == "") {
            document.getElementById("nameError").classList.remove("hide");
            error = true;
        } else {
            document.getElementById("nameError").classList.add("hide");
        }

        if ($("#userSurname").val() == "") {
            document.getElementById("surnameError").classList.remove("hide");
            error = true;
        } else {
            document.getElementById("surnameError").classList.add("hide");
        }

        if ($("#userUsername").val() == "") {
            document.getElementById("usernameErrorSpan").innerText = "Add your Username";
            document.getElementById("usernameError").classList.remove("hide");
            error = true;
        } else {
            document.getElementById("usernameError").classList.add("hide");
        }

        let email = $("#userEmail").val();
        let emailRegex = new RegExp("^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$");
        if (email == "") {
            document.getElementById("emailErrorSpan").innerText = "Add your Email";
            document.getElementById("emailError").classList.remove("hide");
            error = true;
        } else if (!emailRegex.test(email)) {
            document.getElementById("emailErrorSpan").innerText = "Add a valid Email";
            document.getElementById("emailError").classList.remove("hide");
            error = true;
        } else {
            document.getElementById("emailError").classList.add("hide");
        }

        if (($("#userPassword").val()).length < 8) {
            document.getElementById("passwordError").classList.remove("hide");
            error = true
        } else {
            document.getElementById("passwordError").classList.add("hide");
        }

        if (!error) {
            let body = ({
                email: $("#userEmail").val(),
                password: sha1($("#userPassword").val()),
                username: $("#userUsername").val(),
                name: $("#userName").val(),
                surname: $("#userSurname").val(),
            })
            startLoaderAnimation();

            sendReq("post", null, body, (result => {
                stopLoaderAnimation();
                if (result.message == "successo") {
                    location.href = result.url;
                } else if (result.message == "username già esistente") {
                    document.getElementById("handleErrorSpan").innerText = "Already in use, sorry";
                    document.getElementById("handleError").classList.remove("hide");
                } else if (result.message == "email già esistente") {
                    document.getElementById("emailErrorSpan").innerText = "An account is already connected, try to sign up";
                    document.getElementById("trylogin").href = "/auth/login";
                    document.getElementById("emailError").classList.remove("hide");
                } else alert("Something went wrong, try again later");
            }));
        }
    });
})
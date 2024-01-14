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
        if ($("#userHandle").val() == "") {
            document.getElementById("handleError").classList.remove("hide");
            error = true;
        } else {
            document.getElementById("handleError").classList.add("hide");
        }
        if ($("#userEmail").val() == "") {
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
                username: $("#userHandle").val(),
                name: $("#userName").val(),
                surname: $("#userSurname").val(),
            })
            startLoaderAnimation();
            sendReq("post", null, body, (result => {
                console.log(result);




                /*
                if (result == "successo") {
                    location.href = result.url;
                    stopLoaderAnimation();
                } else if (result == "utente già esistente") {
                    document.getElementById("handleErrorSpan").innerText = "Already in use, sorry";
                    document.getElementById("handleError").classList.remove("hide");
                    stopLoaderAnimation();
                } else (result == "email già esistente")
                {
                    document.getElementById("emaiErrorSpan").innerText = "An account is already connected, try to sign up";
                    document.getElementById("trylogin").href = "/auth/login";
                    document.getElementById("emailError").classList.remove("hide");
                    stopLoaderAnimation();
                }

                 */
            }));
        }
    });
})
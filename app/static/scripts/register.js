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
            document.getElementById("usernameError").classList.remove("hide");
            error = true;
        } else {
            document.getElementById("usernameError").classList.add("hide");
        }
        let email = $("#userEmail").val();

        if (email == "") {
            document.getElementById("emaiErrorSpan").innerText = "Add your Email";
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

                if (result.message == "successo") {
                    location.href = result.url;
                    stopLoaderAnimation();
                } else if (result.message == "utente già esistente") {
                    document.getElementById("handleErrorSpan").innerText = "Already in use, sorry";
                    document.getElementById("handleError").classList.remove("hide");
                    stopLoaderAnimation();
                } else if(result.message == "email già esistente")
                {
                    document.getElementById("emaiErrorSpan").innerText = "An account is already connected, try to sign up";
                    document.getElementById("trylogin").href = "/auth/login";
                    document.getElementById("emailError").classList.remove("hide");
                    stopLoaderAnimation();
                }else{
                    stopLoaderAnimation();
                    //TODO: gestire errore
                }


            }));
        }
    });
})
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
        console.log("tutto corretto")
        let body = ({
            email: $("#userEmail").val(),
            password: sha1($("#userPassword").val()),
            username: $("#userHandle").val(),
            name: $("#userName").val(),
            surname: $("#userSurname").val(),
        })
        sendReq("post", null, body, (result => {
            console.log(result);
            if (result.message == "successo") {
                location.href = result.url;
            } else if (result.message == "utente già esistente") {
                document.getElementById("handleError").innerText = "Already in use, sorry";
            } else if (result.message == "mail già in uso") {
                document.getElementById("emailError").innerText = "There is an other account connected";
            }
        }));
    }

});

function a() {
}

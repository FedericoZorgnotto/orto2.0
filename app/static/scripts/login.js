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
        document.getElementById("emailError").innerText = "Write something";
        document.getElementById("emailError").classList.remove("hide");
        error = true;
    } else {
        document.getElementById("passwordError").classList.add("hide");
    }

    if (!error) {
        criptLogin($("#userEmail").val(), $("#userPassword").val(), (result) => {
            console.log(result);
        });
    }
});
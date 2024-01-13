$("#enter-Account").click(() => {
    alert("ciao");

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
        criptLogin($("#userEmail").val(), $("#userPassword").val(), (result) => {
            if (result.message == "successo") {
                localStorage.setItem("sessionUn", body.username);
                localStorage.setItem("sessionPwd", body.password);
            } else if (result.message == "password errata") {
                document.getElementById("passwordError").classList.remove("hide");
            } else if (result.message == "utente non trovato") {
                document.getElementById("emailError").classList.remove("hide");
            }
        });
    }
});


/*
    implementare l'add per riempire il database, fare richesta impost allo stesso indirizzo come request form, forse no risposte
    add picture non va
    passare id, name, description, price, quantity l'id è quello dell' id_vendor

 */
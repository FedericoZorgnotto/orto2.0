window.onload = () => {
    autoLogin();
    //stopLoaderAnimation();
}

function autoLogin() {
    if (localStorage.getItem("sessionPwd") != "null" && localStorage.getItem("sessionUn") != "null") {
        login(localStorage.getItem("sessionUn"), localStorage.getItem("sessionPwd"), (result) => {
            if (result.message == "successo") {
                localStorage.setItem("sessionUn", body.username);
                localStorage.setItem("sessionPwd", body.password);
            } else if (result.message == "password errata") {

            } else if (result.message == "utente non trovato") {

            } else logout();

        });
    }
    //da rimuovere con aggiustamento risposte server
    else {
        $("#profileMenu").hide();
        $("#loginBtn").show();
    }
}

function logout() {
    localStorage.setItem("sessionUn", null);
    localStorage.setItem("sessionPwd", null);
    location.reload();
}

function criptLogin(username, password, callback) {
    login(username, sha1(password), callback);
}

function login(username, password, callback) {
    body = {
        username: username, password: password
    }
    sendReq("post", "https://" + location.host + "/auth/login", body, (result) => {
        callback(result);
    });
}

function sendReq(method, url, body, callback) {
    switch (method) {
        case "get":
            $.get((url == null) ? location.href : url, (result) => {
                callback(result)
            });
            break;
        case "post":
            $.post((url == null) ? location.href : url, body, (result) => {
                console.log(result);
                (callback != null) ? callback(result) : {}
            });
            break;
        default:
            return "UNKNOWN METHOD";
    }
}

function startLoaderAnimation(){
    let main = document.getElementsByTagName("main")[0];
    let div = document.createElement("div");
    div.id = "loader";
    let img = document.createElement("img");
    img.src = "https://"+location.host+"/static/img/logo.png";
    div.appendChild(img);
    main.appendChild(div);
}

function stopLoaderAnimation(){
    document.getElementById("loader").remove();
}
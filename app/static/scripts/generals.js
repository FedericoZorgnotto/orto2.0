window.onload = () =>{
    if(typeof jQuery === 'undefined')
        location.reload();
    else{
        autoLogin();
        console.log("load");
    }
}
function autoLogin(){
    if(localStorage.getItem("sessionPwd")!="null" && localStorage.getItem("sessionUn")!="null"){
        login(localStorage.getItem("sessionUn"), localStorage.getItem("sessionPwd"));
    }
    //da rimuovere con aggiustamento risposte server
    else{
        $("#profileMenu").hide();
        $("#loginBtn").show();
    }
}

function logout(){
    if(localStorage.getItem("sessionUn")==null){
        $("#profileMenu").hide();
        $("#loginBtn").show();
    }else {
        localStorage.setItem("sessionUn", null);
        localStorage.setItem("sessionPwd", null);
        location.reload();
    }
}

function criptLogin(username, password, callback){
    login(username, sha1(password), callback);
}
function login(username, password, callback){
    body = {
        username: username,
        password: password
    }
    sendReq("post", "https://" + location.host + "/auth/login", body, (result)=>{
        console.log(result);
        if(result.message == "successo"){
            localStorage.setItem("sessionUn", body.username);
            localStorage.setItem("sessionPwd", body.password);
            $("#loginBtn").hide();
            $("#profileMenu").show();
            $("#username").text(body.username);
        }else //aggiungere stampa errore
            logout();
        if(callback != null)
            callback();
    });
}

function sendReq(method ,url, body, callback){
    console.log(url);
    switch (method){
        case "get":
            $.get((url == null) ? location.href : url,(result)=>{callback(result)});
            break;
        case "post":
            $.post((url == null) ? location.href : url, body, (result)=>{(callback != null)?callback(result):{}});
            break;
        default:
            return "UNKNOWN METHOD";
    }
}
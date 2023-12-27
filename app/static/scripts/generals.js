$(window).on("load",function (){
    autoLogin();
    console.log("load");
});
function autoLogin(){
    console.log(localStorage.getItem("sessionPwd")!="null");
    if(localStorage.getItem("sessionPwd")!="null" && localStorage.getItem("sessionUn")!="null"){
        login(localStorage.getItem("sessionUn"), localStorage.getItem("sessionPwd"), ()=>{
            console.log("logged in");
            if(document.getElementById("loggedWith") != null)
                document.getElementById("loggedWith").innerText = body.username;
        });
    }
}

function logout(){
    localStorage.setItem("sessionUn", null);
    localStorage.setItem("sessionPwd", null);
    document.getElementById("loggedWith").innerText = "non loggato";
}
function login(username, password, callback){
    body = {
        username: username,
        password: password
    }
    sendReq("post", "https://" + location.host + "/auth/login", body, (result)=>{
        console.log(result);
        if(result.message == "errore interno"){
            localStorage.setItem("sessionUn", body.username);
            localStorage.setItem("sessionPwd", body.password);
        }
        if(callback != null)
            callback();
    });
}

function sendReq(method ,url, body, callback){
    console.log(url);
    let ret = "METHOD NOT FOUND";
    switch (method){
        case "get":
            $.get((url == null) ? location.href : url,(result)=>{callback(result)});
            break;
        case "post":
            $.post((url == null) ? location.href : url, body, (result)=>{(callback != null)?callback(result):{}});
            break;
    }
}
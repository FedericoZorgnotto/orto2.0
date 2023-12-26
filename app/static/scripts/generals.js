$(window).on("load",function (){
    autoLogin();
    console.log("load");
});
function autoLogin(){
    /*if(localStorage.getItem("sessionPwd")!=null && localStorage.getItem("sessionUn")!=null){
        let body = JSON.stringify({
            username: localStorage.getItem("sessionUn"),
            password: localStorage.getItem("sessionPwd")
        })
        $.post(location.host + "/auth/login", body, function(result){
            console.log(result);
        },"json");
    }*/
}
function sendReq(method ,url, body){
    let ret = "METHOD NOT FOUND";
    switch (method){
        case "get":
            $.get((url == null) ? location.href : url,(result)=>{ret =  result});
            break;
        case "post":
            $.post((url == null) ? location.href : url, body, (result)=>{console.log(result)});
            break;
    }
}
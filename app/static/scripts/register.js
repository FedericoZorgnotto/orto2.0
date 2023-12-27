document.getElementById("sendRegister").onclick = function (){
  console.log("dsd");
  let body = ({
    email: $("#email").val(),
    password: sha1($("#password").val()),
    username: $("#username").val()
  })
    sendReq("post", null, body, (result => {
      console.log(result);
      if(result.message == "utente già esistente"){
        login(body.username, body.password);
      }
    }));
};

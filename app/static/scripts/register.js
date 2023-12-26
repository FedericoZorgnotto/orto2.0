document.getElementById("sendRegister").onclick = function (){
  console.log("dsd");
  let body = ({
    email: $("#email").val(),
    password: sha1($("#password").val()),
    username: $("#username").val()
  })
    console.log(sendReq("post", null, body));
};

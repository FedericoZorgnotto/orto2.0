
$("#sendRegister").click(()=> {
  console.log("dsd");
  let body = ({
    email: $("#email").val(),
    password: sha1($("#password").val()),
    username: $("#username").val()
  })
  sendReq("post", null, body, (result => {
    console.log(result);
    if (result.message == "successo") {
      login(body.username, body.password);
    } else if (result.message == "utente già esistente") {
      location.href = location.href;
      alert("nome utente già registrato");
      console.warn("utente già esistente");
    }
  }));
});

function a(){}

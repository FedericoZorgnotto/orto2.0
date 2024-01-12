
$("#create-Account").click(()=> {
  console.log("dsd");
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
      login(body.username, body.password);
    } else if (result.message == "utente già esistente") {
      location.href = location.href;
      alert("nome utente già registrato");
      console.warn("utente già esistente");
    }
  }));
});

function a(){}

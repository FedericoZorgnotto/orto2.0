$(document).ready(() => {

  let img = false;
  let previewImage = document.getElementById("previewImage");

  $("#add-photos").click(function(e) {
    e.preventDefault();
    $("#addImage").trigger('click');
  });

  $("#addImage").change(function() {
    let fileInput = document.getElementById("addImage");

    let file = fileInput.files[0];
    if (file) {
      let reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = function(e) {
        console.log(e.target.result);
        previewImage.src = e.target.result;
        previewImage.classList.remove("invisible");
        img = true;
      }
    }
  });

  $("#create-Post").click(function() {
    let error = false;

    if ($("#postTitle").val() == "") {
      document.getElementById("postTitle").placeholder = "WRITE SOMETHING"
      error = true;
    } else {
      document.getElementById("postTitle").placeholder = "POST TITLE"
    }

    if ($("#address").val() == "") {
      document.getElementById("addressError").classList.remove("hide");
      error = true;
    } else {
      document.getElementById("addressError").classList.add("hide");
    }

    if ($("#quantity").val() == "") {
      document.getElementById("quantityError").classList.remove("hide");
      error = true;
    } else {
      document.getElementById("quantityError").classList.add("hide");
    }

    if ($("#price").val() == "") {
      document.getElementById("priceError").classList.remove("hide");
      error = true;
    } else {
      document.getElementById("priceError").classList.add("hide");
    }

    if ($("#postContent").val() == "") {
      document.getElementById("postContentError").classList.remove("hide");
      error = true;
    } else {
      document.getElementById("postContentError").classList.add("hide");
    }

    if (!error && img) {
      addElement($("#postTitle").val(), $("#postContent").val(), $("#price").val(), $("#quantity").val());
    }
  });
});

function addElement(title, description, price, amount) {
  getId(localStorage.getItem("sessionUn"), (result) => {
    let date = new Date();
    let body = ({
      id_vendor: result,
      name: title,
      description: description,
      price: price,
      quantity: amount,
      publication_date: date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate().toString().padStart(2, '0')
    })
    console.log(body);
    sendReq("post", "https://" + host + "products/add", body, (result) => {
      console.log(result.message)
      let bodyImage = ({
        id_product: result.message,
        base64: previewImage.src,
        main: true,
      })
      sendReq("post", "https://" + host + "products/addImage", bodyImage, (resultImg) => {
        console.log(resultImg.message)
      })
    })
  })
}

function getId(username, callback) {
  sendReq("get", "https://" + host + "/auth/getId/" + username, undefined, callback);
}
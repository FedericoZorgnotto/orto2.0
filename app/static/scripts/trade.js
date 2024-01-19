function addSomething() {
  location.href = "login.html";
}

function contact(name, product, streat, quantity, stars, image) {
  location.href = "contact.html?name=" + name +
    "&product=" + product +
    "&streat=" + streat +
    "&quantity=" + quantity +
    "&stars=" + stars +
    "&image=" + image;
}

function contact(url, name, product, streat, quantity, stars, image) {
  location.href = url+"?name=" + name +
    "&product=" + product +
    "&streat=" + streat +
    "&quantity=" + quantity +
    "&stars=" + stars +
    "&image=" + image;
}
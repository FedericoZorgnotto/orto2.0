const sentences = [
  "I've consistently dedicated my time to nurturing my plants. Eager to exchange resources and expertise, I've made the decision to join this community.",
  "My life has been consistently filled with the care and cultivation of my garden. With an openness to share the fruits of my labor and the knowledge I've acquired, I've signed up on this platform.",
  "For years, my days have been devoted to the tending of my garden. In an effort to share the yield and understanding I've gained, I've decided to become a member of this network.",
  "I've always invested my days in the growth and nourishment of my garden. Desiring to exchange both produce and wisdom, I've chosen to join this site.",
  "My routine has consistently involved nurturing my garden. In order to share the bounty and insights I've gained, I've taken the step of registering on this platform.",
  "Continually, I've committed my days to the cultivation of my garden. Wishing to share my garden's abundance and my learned knowledge, I decided to sign up for this online community.",
  "I've always spent my time wisely, cultivating my garden. With an aim to share my garden's riches and accumulated wisdom, I've opted to participate in this network.",
  "My days have always been devoted to the nurturing of my garden. Keen on sharing the fruits and knowledge I've gathered, I've chosen to register on this platform.",
  "I have perpetually invested my time in the care and growth of my garden. I'm keen to share my garden's yields and my experience, which is why I've registered on this platform.",
  "I've consistently spent my days in the cultivation of my garden. Ready to share my garden's wealth and the knowledge I've accumulated, I've decided to sign up for this platform."
];

window.addEventListener("load", function() {

  let urlParams = new URLSearchParams(window.location.search);
  let name = urlParams.get('name');
  let product = urlParams.get('product');
  let streat = urlParams.get('streat');
  let quantity = urlParams.get('quantity');
  let stars = urlParams.get('stars');
  let image = urlParams.get('image');

  if (name != null && product != null && streat != null && quantity != null && stars != null && image != null) {
    document.getElementById("image").src = "img/pfp/Profilo" + image + ".png";

    let starsList = document.getElementsByClassName("star");
    for (let i = 0; i < starsList.length; i++) {
      if (i > stars - 1)
        starsList[i].classList.add("gray");
    }

    document.getElementById("name").innerText = name;
    document.getElementById("productName").innerText = product;
    document.getElementById("streat").innerText = streat;
    document.getElementById("quantity").innerText = quantity;

    document.getElementById("user-Bio").innerText = sentences[Math.floor(Math.random() * (sentences.length))];

  }
  else {
    alert("Error, no data");
    console.error("no data in query parameters");
  }
});
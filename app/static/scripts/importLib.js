let scrps = new Array("https://code.jquery.com/jquery-3.6.3.min.js",
    "https://"+ location.host + "/static/scripts/generals.js",
    "https://cdnjs.cloudflare.com/ajax/libs/js-sha1/0.6.0/sha1.min.js");
let stl = new Array("https://cdn.jsdelivr.net/npm/bootstrap@5.2/dist/css/bootstrap.min.css");

let head = document.getElementsByTagName("head")[0];

for(let i = 0; i<stl.length; i++){
    let style = document.createElement('script');
    style.src = stl[i];
    style.type = "text/css";
    style.rel = "stylesheet";
    head.appendChild(style);
}


for(let i = 0; i<scrps.length; i++){
    let script = document.createElement('script');
    script.src = scrps[i];
    script.type = "text/javascript";
    head.appendChild(script);
}

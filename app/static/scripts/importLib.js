let scrps = new Array("https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.3/jquery.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/js-sha1/0.6.0/sha1.min.js",
    "https://"+ location.host + "/static/scripts/generals.js",
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js");

let stl = new Array("https://cdn.jsdelivr.net/npm/bootstrap@5.2/dist/css/bootstrap.min.css",
    "https://"+ location.host + "/static/css/generals.css");

let head = document.getElementsByTagName("head")[0];


for(let i = 0; i<stl.length; i++){
    let style = document.createElement('link');
    console.log(stl[i]);
    style.href = stl[i];
    style.type = "text/css";
    style.rel = "stylesheet";
    head.appendChild(style);
}

let scpS = document.getElementsByClassName("ttt");
for (let i = 0; i<scpS.length; i++){
    scrps.push(scpS[i].src);
    scpS[i].remove();
    console.log("aaa");
}

console.log(scrps);
for (let i = 0; i < scrps.length; i++) {
    let script = document.createElement('script');
    script.src = scrps[i];
    script.type = "text/javascript";
    head.append(script);
}


let libs = new Array("https://code.jquery.com/jquery-3.6.3.min.js", "https://"+ location.host + "/static/scripts/generals.js");

let head = document.getElementsByTagName("head")[0];
for(let i = 0; i<libs.length; i++){
    let script = document.createElement('script');
    script.src = libs[i];
    head.appendChild(script);
}

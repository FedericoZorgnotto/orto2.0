function addElement(title, description, price, amount){
    getId(localStorage.getItem("sessionUn"), (result)=>{
        let date = new Date();
        let body = ({
            id_vendor: result,
            name: title,
            description: description,
            price: price,
            quantity: amount,
            publication_date: date.getFullYear()+"-"+(date.getMonth()+1)+"-"+date.getDate().toString().padStart(2, '0')
        })
        console.log(body);
        sendReq("post","https://"+location.host+"products/add", body, (result)=>{console.log(result.message)})
    })
}

function getId(username, callback){
    sendReq("get", "https://"+location.host+"/auth/getId/"+username, undefined, callback);
}
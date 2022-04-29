const btn = document.querySelector('input');

btn.addEventListener('click', updateBtn);

function updateBtn() {
    if (btn.value === 'PT, BR'){
        btn.value = 'ES, AR';
    } else if (btn.value === 'ES, AR'){
        btn.value = 'EN, US';
    }else {
        btn.value = 'PT, BR'
    }
}


function vermais(){
    var pontos = document.getElementById("pontos");
    var maistexto = document.getElementById("mais");
    var btnvermais = document.getElementById("btn-vermais");

    if(pontos.style.display === "none"){
        pontos.style.display = "inline";
        maistexto.style.display = "none";
        btnvermais.innerHTML = "ver mais";
        document.getElementById("rodape").style.marginBottom = "-16%";
    }else{
        pontos.style.display = "none";
        maistexto.style.display = "inline";
        btnvermais.innerHTML = "ocultar";
        document.getElementById("rodape").style.marginBottom = "-15.5%";

    }
}

function trocadiv1() {
    var discussoes1 = document.getElementById("discussoes1");
    var coment1 = document.getElementById("coment1");
    var btncriar1 = document.getElementById("btn-criar1");
    var btnenviar1 = document.getElementById("enviar");
    var poscoment = document.getElementById("pos-coment");
    

    btncriar1.addEventListener("click", function() {
    discussoes1.style.display = "none";
    coment1.style.display = "inline";
    poscoment.style.display = "none";
    document.getElementById("ce1").style.transform = "translate(6.5%, -240%)";
    document.getElementById("ce2").style.transform = "translate(6.5%, -220%)";
    document.getElementById("rodape").style.marginBottom = "-16%";
    })

    btnenviar1.addEventListener("click", function() {
    discussoes1.style.display = "inline";
    coment1.style.display = "none";
    poscoment.style.display = "inline";
    })

}


function text_options() {
    var btnI = document.getElementById("i");
    var btnIvalor = 0;
    var btnB = document.getElementById("b");

    btnI.addEventListener("click", function(){
        if(btnIvalor === 0){
        document.querySelector("textarea").style.fontStyle = "italic";
        btnIvalor = 1;}
        else{
            document.querySelector("textarea").style.fontStyle = "normal";
            btnIvalor = 0;
        }

    })

    btnB.addEventListener("click", function(){
        document.querySelector("textarea").style.fontWeight = "bold";
    })
  
    
  }


  function trocalike() {
        var cont1 = 1;
        var cont2 = 1;
        var btnlike1 = document.getElementById("btn-like1");
        var btnlike2 = document.getElementById("btn-like2");
        

        btnlike1.addEventListener("click", function(){document.getElementById("likeP1").innerHTML= (cont1 + 1) + " likes";});
        btnlike2.addEventListener("click", function(){document.getElementById("likeP2").innerHTML= (cont2 + 1) + " likes";}); 


        
  }
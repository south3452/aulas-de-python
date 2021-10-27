//SECTION 
// 1 - consultar a API 
// 2 - tratar dados do retorno
// 3 - escrever no HTML
//!SECTION   
const bodytb = document.getElementById('corpotabelaimages')

var i = 0
document.body.onload = setInterval(()=>{
    console.log(`olá${i+1}`)
    i++
}, 10000)


//NOTE Cria elementos no HTML
function criaElem(){
    const linha = document.createElement('tr')

    function criarelementos(qntd,elemento){
        for(var i = 0; i < qntd; i++){
            let elem = document.createElement(elemento)
            linha.appendChild(elem)
        }
        bodytb.appendChild(linha)
    }

    criarelementos(2,'td')
}

function imagem(){

//NOTE PASSO 1
let options= {
    method: 'GET'
}


fetch('/images', options).then(response => {
    response.json().then(json => {
        json.forEach(element => {
            criaElem()
            
            //NOTE PASSO 2 && PASSO 3
            bodytb.lastChild.childNodes[0].innerText = element['image']
            var valor = element['id'].indexOf(":")+1 
            bodytb.lastChild.childNodes[1].innerText = element['id'].substring(valor, valor + 12)
        });
        
    })
})
}








//console.log(`corpo.lastChild.childNodes[${i}].innerText = '${conteudo}'`)
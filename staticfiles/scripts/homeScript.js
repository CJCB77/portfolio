const nameText = document.querySelector(".home__subheading");
const strName = nameText.textContent;
const splitName = strName.split("");
nameText.textContent = "";


for(let i = 0; i < splitName.length; i++){
    nameText.innerHTML += "<span class='char'>" + splitName[i] + "</span>";
}

char = 0;
setTimeout(function delay(){
    timer = setInterval(onTick,50);
},2000);
setTimeout(function btnAppear(){
    const btn = document.getElementById("btn");
    btn.style.visibility = "visible";
    btn.style.animation = " 1s appear ease-in, 1s slide-up";
}, 4000);

function onTick(){
    const letters = nameText.querySelectorAll(".char")[char]
    letters.classList.add("fade");
    char++;
    if (char === splitName.length){
        complete();
        return;
    }
}

function complete(){
    clearInterval(timer);
    timer = null;
}
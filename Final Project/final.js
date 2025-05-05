function show(){
    document.getElementById("extinfo").style.display = "block";
    document.getElementById("infbtn").style.display = "none";
    document.getElementById("lesbtn").style.visibility = "visible";
    document.getElementById("lesbtn").style.display = "inline";
}

function hide(){
    document.getElementById("extinfo").style.display = "none";
    document.getElementById("infbtn").style.display = "inline";
    document.getElementById("lesbtn").style.display = "none";
}

function swap1(){
    document.getElementById("altpark-img").style.visibility = "visible";
    document.getElementById("altpark-img").style.display = "inline";
    document.getElementById("park-img").style.visibility = "hidden";
    document.getElementById("park-img").style.display = "none";
}

function swap2(){
    document.getElementById("altpark-img").style.visibility = "hidden";
    document.getElementById("altpark-img").style.display = "none";
    document.getElementById("park-img").style.visibility = "visible";
    document.getElementById("park-img").style.display = "inline";
}
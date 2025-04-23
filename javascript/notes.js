let images = ["https://www.avma.org/sites/default/files/media/pet-selection-budgie-with-girl-sm.jpg", "https://www.thesprucepets.com/thmb/SteTDxnKFImt2SYP1-CY_0HVv8s=/5184x0/filters:no_upscale():strip_icc()/close-up-of-bird-724290655-5abc25c604d1cf0036e0fd9d.jpg", "https://i0.wp.com/puppiesareprozac.com/wp-content/uploads/2011/01/Draco-Budgie-294x300.jpg?resize=294%2C300"]
function hello(){
    document.getElementById("title").innerHTML = "Hello World!"
}
count = 0
function change(){
    document.getElementById("img").src = images[count]
    if (count === 2){
        count = 0
    }else{
        count += 1
    }
}

function highlight(){
    document.getElementById("btn").style.backgroundColor = "orange"
    document.getElementById("btn").style.backgroundColor = "white"
}

function normal(){
    document.getElementById("btn").style.backgroundColor = "grey"
    document.getElementById("btn").style.backgroundColor = "black"
}

function show(){
    document.getElementById("hidden").style.display = "block"
}

function pop(){
    window.alert("For real. Don't click this!")
}
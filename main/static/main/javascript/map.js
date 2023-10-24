const bar__content1 = document.getElementById("bar__content1");
const bar__content2 = document.getElementById("bar__content2");
const bar__content3 = document.getElementById("bar__content3");

const img1 = document.getElementById("img1")
const img2 = document.getElementById("img2")
const img3 = document.getElementById("img3")


bar__content1.addEventListener("click",function(){
    bar__content1.classList.remove("bar__content-active");
    bar__content2.classList.remove("bar__content-active");
    bar__content3.classList.remove("bar__content-active");
    
    img1.classList.remove("img-active");
    img2.classList.remove("img-active");
    img3.classList.remove("img-active");

    bar__content1.classList.add("bar__content-active");
    img1.classList.add("img-active");

})
bar__content2.addEventListener("click",function(){
    bar__content1.classList.remove("bar__content-active");
    bar__content2.classList.remove("bar__content-active");
    bar__content3.classList.remove("bar__content-active");
    
    img1.classList.remove("img-active");
    img2.classList.remove("img-active");
    img3.classList.remove("img-active");
    
    bar__content2.classList.add("bar__content-active");
    img2.classList.add("img-active");
})
bar__content3.addEventListener("click",function(){
    bar__content1.classList.remove("bar__content-active");
    bar__content2.classList.remove("bar__content-active");
    bar__content3.classList.remove("bar__content-active");
    
    img1.classList.remove("img-active");
    img2.classList.remove("img-active");
    img3.classList.remove("img-active");
    
    bar__content3.classList.add("bar__content-active");
    img3.classList.add("img-active");
})

const menu = document.getElementById("hamburgermenu");
const toggleIcon = document.getElementById("menu-toggle");

// アイコンがクリックされるとメニューのアクティブ・非アクティブを切り替える。
toggleIcon.addEventListener("click", function (ev) {
    menu.classList.toggle("active");
});

const mask = document.getElementById("mask");
mask.addEventListener("click",function(){
    menu.classList.remove("active");
})


let menu = document.getElementById("hamburgermenu");
const toggleIcon = document.getElementById("menu-toggle");

// アイコンがクリックされるとメニューのアクティブ・非アクティブを切り替える。
toggleIcon.addEventListener("click", function (ev) {
    menu.classList.toggle("active");
});

const mask = document.getElementById("mask");
mask.addEventListener("click",function(){
    menu.classList.remove("active");
})

function countdown(due) {
    const now = new Date();

    const rest = due.getTime() - now.getTime();
    const sec = Math.floor(rest / 1000) % 60;
    const min = Math.floor(rest / 1000 / 60) % 60;
    const hours = Math.floor(rest / 1000 / 60 / 60) % 24;
    const days = Math.floor(rest / 1000 / 60 / 60 / 24);
    const count = [days, hours, min, sec];
    
    console.log(now)
    console.log(due)
    console.log(rest)
    return count;
}

const goal = new Date(2023, 11-1, 3);

function recalc() {
    const counter = countdown(goal);
    document.getElementById('day').textContent = counter[0];
    document.getElementById('hour').textContent = counter[1];
    document.getElementById('min').textContent = String(counter[2]).padStart(2, '0');
    document.getElementById('sec').textContent = String(counter[3]).padStart(2, '0');
    refresh();  
}

function refresh() {
    setTimeout(recalc, 1000);
}
recalc();


var slideConts = document.querySelectorAll('.slideConts'); // スライドで表示させる要素の取得
var slideContsRect = []; // 要素の位置を入れるための配列
var slideContsTop = []; // 要素の位置を入れるための配列
var windowY = window.pageYOffset; // ウィンドウのスクロール位置を取得
var windowH = window.innerHeight; // ウィンドウの高さを取得
var remainder = 100; // ちょっとはみ出させる部分

// 要素の位置を取得
for (var i = 0; i < slideConts.length; i++) {
  slideContsRect.push(slideConts[i].getBoundingClientRect());
}
for (var i = 0; i < slideContsRect.length; i++) {
  slideContsTop.push(slideContsRect[i].top + windowY);
}

// ウィンドウがリサイズされたら、ウィンドウの高さを再取得
window.addEventListener('resize', function () {
  windowH = window.innerHeight;
});

// スクロールされたら
window.addEventListener('scroll', function () {
  // スクロール位置を取得
  windowY = window.pageYOffset;
  
  for (var i = 0; i < slideConts.length; i++) {
    // 要素が画面の下端にかかったら
    if(windowY > slideContsTop[i] - windowH + remainder) {
      // .showを付与
      slideConts[i].classList.add('show');
    } else {
      // 逆に.showを削除
      slideConts[i].classList.remove('show');
    }
  }
});

// ページネーション swiper.js

var swiper = new Swiper(".mySwiper", {
  spaceBetween: 30,
  effect: "fade",
  loop: true,
  autoplay: {
  delay: 3500,
  disableOnInteraction: false
  },
  pagination: {
      el: ".swiper-pagination",
      clickable: true,
  },
  });
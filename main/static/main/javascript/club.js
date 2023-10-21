let modal = document.getElementById("club_info__modal");
let frameName = document.getElementById("club_name");
let frameExplanation = document.getElementById("club_explanation");
let frameLeader = document.getElementById("club_leader");
let frameImage = document.getElementById("club_image");
let imageList = document.querySelectorAll(".club_info__modal__image__list img");
let clubList = document.querySelectorAll(".club_info__content");

clubList.forEach((element) => {
  element.addEventListener("click", () => {
    // modal.style.display = "flex";
    modal.classList.add("modal-active");

    setTimeout(function () {
      let clubNum = parseInt(element.getAttribute("id").split("-")[1]);
      frameName.innerText = dataList[clubNum][0];
      frameExplanation.innerText = dataList[clubNum][1];
      frameLeader.setAttribute("href", dataList[clubNum][5]);
      frameImage.setAttribute("src", dataList[clubNum][6]);
      for (let i = 6; i < 13; i++) {
        if (dataList[clubNum][i]) {
          imageList[i - 6].setAttribute("src", dataList[clubNum][i]);
          imageList[i - 6].style.display = "block";
        } else {
          imageList[i - 6].style.display = "none";
        }
      }
      modal.style.opacity = 1;
    }, 10);
  });
});

document.getElementById("club_info__modal__close").addEventListener("click", () => {
  modal.style.opacity = 0;
  setTimeout(function () {
    // modal.style.display = "none";
    modal.classList.remove("modal-active");
  }, 500);
});

imageList.forEach((element) => {
  element.addEventListener("click", () => {
    frameImage.style.opacity = 0;
    setTimeout(function () {
      frameImage.setAttribute("src", element.getAttribute("src"));
    }, 200);
    setTimeout(function () {
      frameImage.style.opacity = 1;
    }, 200);
  });
});

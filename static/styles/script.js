// 네비게이션 언더바 관련
let horizontalBar = document.getElementById("nav-underline");
let horizontalMenus = document.querySelectorAll(".nav ul li");

function horizontalIndicator(e) {
  horizontalBar.style.left = e.offsetLeft + "px";
  horizontalBar.style.width = e.offsetWidth + "px";
  horizontalBar.style.top = e.offsetTop + e.offsetHeight + "px";
}

function horizontalMouseout(e) {
  horizontalBar.style.width = 0 + "px";
}

horizontalMenus.forEach((menu) =>
  menu.addEventListener("mouseover", (e) =>
    horizontalIndicator(e.currentTarget)
  )
);

horizontalMenus.forEach((menu) =>
  menu.addEventListener("mouseout", (e) =>
  horizontalMouseout(e.currentTarget)
  )
);



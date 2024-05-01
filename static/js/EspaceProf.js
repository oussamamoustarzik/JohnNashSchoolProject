const body = document.querySelector("body"),
    sidebar = body.querySelector(".sidebar"),
    toogle = body.querySelector(".toggle"),
    modeSwitch = body.querySelector(".toggle-switch"),
    modetext = body.querySelector(".mode-text");


    toogle.addEventListener("click" , () => {


        sidebar.classList.toggle("close");
    });
    modeSwitch.addEventListener("click",() => {
          body.classList.toggle("dark");
if(body.classList.contains("dark")){
        modetext.innerText = "light Mode"
    }
    else{
        modetext.innerText = "dark Mode"
    }
    });
    


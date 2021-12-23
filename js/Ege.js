
/*Калькулятор ЕГЭ*/
const tabs_ege = document.getElementsByClassName('ege__filter');

for (let i = 0; i < tabs_ege.length; i++) {
    tabs_ege[i].addEventListener("click", () => {
        let qua_exam=0;
        for (let i = 0; i < tabs_ege.length; i++)
            if (tabs_ege[i].classList.contains("activated"))
                qua_exam++;
        if (tabs_ege[i].classList.contains("activated") ) {
            tabs_ege[i].classList.remove("activated");
            qua_exam--;
        } else {
            if (qua_exam < 3) {
                tabs_ege[i].classList.add("activated");
                qua_exam++;
            }
        }
    });
}

function ege__input__js() {
    let ege_balls = document.getElementById('ege__input').value;
    if (ege_balls > 300) {
        ege_balls=300;
    }
    if ((ege_balls < 0) || (ege_balls=='')) {
        ege_balls=0;
    }
    document.getElementById('ege__input').value=ege_balls;
}





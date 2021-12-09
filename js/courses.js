


const courses = [
    {name: "Нука Врач", institute: "Мед"},
    {name: "Геймдев", institute: "Пи"},
    {name: "ПИ", institute: "Пи"},
    {name: "ИСИТ", institute: "Пи"},
    {name: "Математика", institute: "Пи"},
    {name: "Физика", institute: "Пи"},
];

const tabs = document.getElementsByClassName('institute');

for (let i = 0; i < tabs.length; i++) {
    tabs[i].addEventListener("click", () => {
        menuUpdate(courses);

        for (let j = 0; j < tabs.length; j++) 
            tabs[j].classList.remove("activated");

        tabs[i].classList.add("activated");
    });
}

function menuUnmarkAll() {
    courseNodes = document.getElementsByClassName('direction');
    for (let j = 0; j < courseNodes.length; j++)
        courseNodes[j].classList.remove("activated");
}

function menuUpdate(courses) {
    const menu = document.querySelector("#courses_list");
    menu.innerHTML = "";

    for (let i = 0; i < courses.length; i++) {
        const node = document.createElement("div");
        node.className = "direction";
        node.innerHTML =  courses[i]?.institute + " | " + courses[i]?.name;

        menu.appendChild(node);

        node.addEventListener("click", () => {
            menuUnmarkAll();
            node.classList.add("activated");
        });
    }
}

menuUpdate(courses);
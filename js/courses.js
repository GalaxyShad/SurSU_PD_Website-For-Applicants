


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

function cardUpdate(card) {
    const nHeader = document.querySelector("#card_header");
    const nDescription = document.querySelector("#card_description");
    const nPoints = document.querySelector("#card_points");
    const nSubjects = document.querySelector("#card_subjects");
    const nPlaceCount = document.querySelector("#card_place");
    const nMoneyType = document.querySelector("#card_money_type");
    const nPeriod = document.querySelector("#card_period");
    const nCost = document.querySelector("#card_cost");

    nHeader.innerHTML = card.title;
    nDescription.innerHTML = card.desc;
    nPoints.innerHTML = card.points;
    nSubjects.innerHTML = "";
    for (let i = 0; i < card.subjects.length; i++) {
        const node = document.createElement("p");
        node.innerHTML = card.subjects[i];
        nSubjects.appendChild(node);
    }
    nPlaceCount.innerHTML = card.placeCount;
    nMoneyType.innerHTML = card.moneyType;
    nPeriod.innerHTML = card.period;
    nCost.innerHTML = card.cost;
}

cardRender( 
    {
        title: "Программная инженерия",
        desc: "Вы будете учить физику :).",
        points: 100.98,
        subjects: ["Просто Физика", "Продвинутая Физика", "Классная Физика"],
        placeCount: "20/5",
        moneyType: "Бюджет / Комерция",
        period: "4 года",
        cost: "99999 999 в год" 
    }
);

menuUpdate(courses);
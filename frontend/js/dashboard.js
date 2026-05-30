const username = localStorage.getItem("username");

const welcome =
document.getElementById("welcome");

if (welcome) {

    welcome.textContent =
    `Welcome, ${username || "User"} 👋`;

}
const count =
localStorage.getItem("projects") || 0;

document.getElementById(
    "projectCount"
).innerHTML = count;
const project =
localStorage.getItem("lastProject");

if(project){

    document.getElementById(
        "historyList"
    ).innerHTML =
    "<li>" + project + "</li>";

}

function goBuilder() {

    window.location.href =
    "builder.html";

}
function login(){

    const username =
    document.getElementById("username").value;

    if(username===""){

        alert("Enter username");

        return;
    }

    localStorage.setItem(
        "username",
        username
    );

    window.location.href =
    "dashboard.html";
}
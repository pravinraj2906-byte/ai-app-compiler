function analyze(){

    document.getElementById("result")
    .innerHTML = `

    <h2>Recommended Stack</h2>

    <p><b>Frontend:</b> React</p>

    <p><b>Backend:</b> FastAPI</p>

    <p><b>Database:</b> PostgreSQL</p>

    <p><b>Authentication:</b> JWT</p>

    <hr>

    <h2>Pages</h2>

    <ul>

        <li>Login</li>

        <li>Dashboard</li>

        <li>Contacts</li>

        <li>Payments</li>

        <li>Analytics</li>

    </ul>

    <hr>

    <h2>Database Tables</h2>

    <ul>

        <li>Users</li>

        <li>Contacts</li>

        <li>Payments</li>

        <li>Subscriptions</li>

    </ul>

    `;
}
function goArchitecture(){

    window.location.href =
    "architecture.html";

}
function generateApp(){

    const prompt =
    document.getElementById("prompt").value;

    let projects =
JSON.parse(
localStorage.getItem("projectsList")
) || [];

projects.push(prompt);

localStorage.setItem(
    "projectsList",
    JSON.stringify(projects)
);

    let count =
    Number(localStorage.getItem("projects")) || 0;

    count++;

    localStorage.setItem(
        "projects",
        count
    );

    alert(
        "Application Generated Successfully!"
    );

}
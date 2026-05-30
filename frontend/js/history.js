const table =
document.getElementById("historyTable");

const projects =
JSON.parse(
localStorage.getItem("projectsList")
) || [];

if(projects.length === 0){

    table.innerHTML = `
    <tr>
        <td colspan="2">
            No Projects Found
        </td>
    </tr>
    `;

}else{

    let rows = "";

    projects.forEach(project => {

        rows += `
        <tr>
            <td>${project}</td>
            <td>Generated</td>
        </tr>
        `;

    });

    table.innerHTML = rows;
}
function openProject(){
    window.location.href = "preview.html";
}
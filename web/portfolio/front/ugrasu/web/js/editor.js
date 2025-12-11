document.getElementById("addCode2").addEventListener("change", e => {
    document.getElementById("code2").style.display = e.target.checked ? "block" : "none";
});

async function saveModule() {
    const data = {
        title: document.getElementById("title").value,
        description: document.getElementById("description").value,
        code1: document.getElementById("code1").value,
        code2: document.getElementById("addCode2").checked
            ? document.getElementById("code2").value
            : null
    };

    const response = await fetch("http://localhost:8000/create-module", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    alert("Готово! Открой: " + result.url);
}

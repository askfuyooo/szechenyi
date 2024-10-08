//Kis plusz, hogy kötelező legyen választani :)
document.addEventListener("DOMContentLoaded", () => {
    const votesForm = document.getElementById("votesForm");

    votesForm.addEventListener("submit", (e) => {
        const target = e.target.vote.value;
        if (!target) {
            e.preventDefault();
            alert("Kérem válasszon szavazás előtt!");
        }
    });
});
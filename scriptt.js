
let emailtext = ""

function preview() {
    emailtext = document.getElementById("stuff").value.trim();

    if (!emailtext) {
        alert("Please enter the email first.")
        return
    }

    document.getElementById("confirmbox").textContent = emailtext;
    document.getElementById("secondbox").style.display = "block";
    document.getElementById("result").textContent = "";
}

function check() {
    document.getElementById("result").textContent = "Checking...";
    document.getElementById("result").style.color = "black";

    fetch('http://localhost:5000/check', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: emailtext })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "NOPE") {
            document.getElementById("result").textContent = data.status + " – " + data.reason;
            document.getElementById("result").style.color = "red";
        } else {
            document.getElementById("result").textContent = data.status + " – " + data.reason;
            document.getElementById("result").style.color = "green";
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("result").textContent = "Something went wrong.";
        document.getElementById("result").style.color = "gray";
    });
}

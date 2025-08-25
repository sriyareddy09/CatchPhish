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
    document.getElementById("result").textContent = "checking...";

    setTimeout (() => {
        const sussy = ["otp", "password", "urgent", "click", ".exe", "http", "money", "suspended", "reset" ];
        let isPhish = sussy.some(word => emailtext.toLowerCase().includes(word));

        if (isPhish) {
           document.getElementById("result").textContent = "This doesn't look like a legitimate email. Be Aware!!";
            document.getElementById("result").style.color = "red";
        } else {
           document.getElementById("result").textContent = "This does look like a legitimate email, please verify to be careful.";
            document.getElementById("result").style.color = "green";
        }

    },1000);
}
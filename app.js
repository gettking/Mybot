function createWallet() {
  fetch("http://127.0.0.1:5000/create_wallet", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      username: document.getElementById("user").value,
      password: document.getElementById("pass").value
    })
  })
  .then(res => res.json())
  .then(data => {
    alert("Wallet dibuat: " + data.address);
    localStorage.setItem("wallet", data.address);
  });
}

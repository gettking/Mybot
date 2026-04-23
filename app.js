function openCreateWallet() {
  document.getElementById("screen").innerHTML = `
    <h2>💼 CREATE WALLET</h2>

    <input id="user" placeholder="username"><br><br>
    <input id="pass" type="password" placeholder="password"><br><br>

    <button onclick="createWallet()">CREATE</button>
  `;
}

function createWallet() {

  fetch("http://127.0.0.1:5000/create_wallet", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      username: document.getElementById("user").value,
      password: document.getElementById("pass").value
    })
  })
  .then(res => res.json())
  .then(data => {

    document.getElementById("screen").innerHTML = `
      <h2>✅ WALLET CREATED</h2>
      <p><b>Address:</b> ${data.address}</p>
      <p>Save this address!</p>
    `;
  });

}

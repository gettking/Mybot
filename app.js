let wallet = JSON.parse(localStorage.getItem("wallet")) || null;

render();

// =========================
// RENDER UI
// =========================
function render() {
  const app = document.getElementById("app");

  if (!wallet) {
    app.innerHTML = `
      <h3>🧪 CREATE WALLET</h3>

      <input id="user" placeholder="username"><br>
      <input id="pass" type="password" placeholder="password"><br>

      <button onclick="createWallet()">CREATE WALLET</button>
    `;
  } else {
    app.innerHTML = `
      <div class="box">
        <h3>💼 YOUR WALLET</h3>

        <p><b>Username:</b> ${wallet.username}</p>

        <p><b>Address:</b></p>
        <div class="addr">${wallet.address}</div>

        <button onclick="copyAddr()">📋 COPY ADDRESS</button>
        <button onclick="resetWallet()">❌ DELETE WALLET</button>
      </div>
    `;
  }
}

// =========================
// CREATE WALLET
// =========================
function createWallet() {
  let user = document.getElementById("user").value;
  let pass = document.getElementById("pass").value;

  if (!user || !pass) {
    alert("Isi username & password!");
    return;
  }

  let address = "TTM-" + Math.random().toString(36).substring(2, 10).toUpperCase();

  wallet = {
    username: user,
    password: pass,
    address: address
  };

  localStorage.setItem("wallet", JSON.stringify(wallet));

  render();
}

// =========================
// COPY ADDRESS
// =========================
function copyAddr() {
  navigator.clipboard.writeText(wallet.address);
  alert("Address copied!");
}

// =========================
// RESET WALLET
// =========================
function resetWallet() {
  localStorage.removeItem("wallet");
  wallet = null;
  render();
}

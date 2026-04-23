let data = JSON.parse(localStorage.getItem("ttm")) || {
  wallet: null,
  balance: 0,
  lastFaucet: 0,
  clickPower: 1
};

function save() {
  localStorage.setItem("ttm", JSON.stringify(data));
}

// =====================
// WALLET
// =====================
function openWallet() {
  if (!data.wallet) {
    document.getElementById("screen").innerHTML = `
      <h3>Create Wallet</h3>
      <input id="u" placeholder="username"><br>
      <input id="p" type="password" placeholder="password"><br>
      <button onclick="createWallet()">CREATE</button>
    `;
  } else {
    document.getElementById("screen").innerHTML = `
      <h3>💼 WALLET</h3>
      <p>Address: ${data.wallet}</p>
      <p>Balance: ${data.balance} TTM</p>
    `;
  }
}

function createWallet() {
  let addr = "TTM" + Math.random().toString(36).substring(2,10);

  data.wallet = addr;
  data.balance = 0;

  save();

  alert("Wallet created: " + addr);
  openWallet();
}

// =====================
// FAUCET
// =====================
function openFaucet() {
  document.getElementById("screen").innerHTML = `
    <h3>💧 FAUCET</h3>
    <button onclick="claim()">CLAIM 10 TTM</button>
  `;
}

function claim() {
  let now = Date.now();

  if (now - data.lastFaucet < 43200000) {
    alert("Wait 12 hours");
    return;
  }

  data.balance += 10;
  data.lastFaucet = now;

  save();

  alert("Claimed 10 TTM!");
}

// =====================
// CLICKER
// =====================
function openClicker() {
  document.getElementById("screen").innerHTML = `
    <h3>🎮 CLICKER</h3>
    <button onclick="clickCoin()">CLICK +${data.clickPower}</button>
    <p>Balance: ${data.balance}</p>
  `;
}

function clickCoin() {
  data.balance += data.clickPower;
  save();
  openClicker();
}

// =====================
// SHOP
// =====================
function openShop() {
  document.getElementById("screen").innerHTML = `
    <h3>🛒 SHOP</h3>
    <button onclick="upgrade()">Upgrade Click (+1) - 20 TTM</button>
  `;
}

function upgrade() {
  if (data.balance < 20) {
    alert("Not enough TTM");
    return;
  }

  data.balance -= 20;
  data.clickPower += 1;

  save();

  alert("Upgraded!");
}

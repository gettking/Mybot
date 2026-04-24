function getWallet() {
  let addr = localStorage.getItem("wallet");

  fetch("http://127.0.0.1:5000/wallet/" + addr)
  .then(res => res.json())
  .then(data => {
    console.log(data);
    alert("Balance: " + data.balance);
  });
}

function faucet() {
  let addr = localStorage.getItem("wallet");

  fetch("http://127.0.0.1:5000/faucet", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      address: addr
    })
  })
  .then(res => res.json())
  .then(data => {
    if (data.error) {
      alert(data.error);
    } else {
      alert("Success! Balance: " + data.balance);
    }
  });
}

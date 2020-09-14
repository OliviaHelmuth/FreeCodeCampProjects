function checkCashRegister(price, cash, cid) {
  let cidTotal = null;
  function total(cid) {
    cid.forEach((value) => {
      cidTotal += value[1] * 100;
    });
    cidTotal /= 100;
  }
  total();

  let cashRegister = {
    status: "",
    change: [
      ["PENNY", 0],
      ["NICKEL", 0],
      ["DIME", 0],
      ["QUARTER", 0],
      ["ONE", 0],
      ["FIVE", 0],
      ["TEN", 0],
      ["TWENTY", 0],
      ["ONE HUNDRED", 0],
    ],
  };
  let change = cash - price;

  if (cidTotal < change) {
    cashRegister.status = "INSUFFICIENT_FUNDS";
  } else if (cidTotal == change) {
    cashRegister.status = "CLOSED";
  }

  console.log("change", change);
  console.log("cidTotal", cidTotal);
  // console.log('cashRegister', cashRegister);
  return cashRegister;
}

checkCashRegister(350, 1000, [
  ["PENNY", 1.01],
  ["NICKEL", 2.05],
  ["DIME", 3.1],
  ["QUARTER", 4.25],
  ["ONE", 90],
  ["FIVE", 55],
  ["TEN", 20],
  ["TWENTY", 60],
  ["ONE HUNDRED", 100],
]);

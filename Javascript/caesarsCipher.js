function rot13(str) {
  let lookUpRot13 = {
    A: "N",
    B: "O",
    C: "P",
    D: "Q",
    E: "R",
    F: "S",
    G: "T",
    H: "U",
    I: "V",
    J: "W",
    K: "X",
    L: "Y",
    M: "Z",
    N: "A",
    O: "B",
    P: "C",
    Q: "D",
    R: "E",
    S: "F",
    T: "G",
    U: "H",
    V: "I",
    W: "J",
    X: "K",
    Y: "L",
    Z: "M",
    "!": "!",
    "?": "?",
    ".": ".",
    ",": ",",
    " ": " ",
  };
  let encodedArr = str.split("");
  let decodedArr = [];
  for (let i = 0; i < encodedArr.length; i++) {
    decodedArr.push(lookUpRot13[encodedArr[i]]);
  }
  console.log(decodedArr.join(""));
  return decodedArr.join("");
}
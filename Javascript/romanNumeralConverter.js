function convertToRoman(num) {
  let lookUpRoman = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    20: "XX",
    30: "XXX",
    40: "XL",
    50: "L",
    60: "LX",
    70: "LXX",
    80: "LXXX",
    90: "XC",
    100: "C",
    200: "CC",
    300: "CCC",
    400: "CD",
    500: "D",
    600: "DC",
    700: "DCC",
    800: "DCCC",
    900: "CM",
    1000: "M",
    2000: "MM",
    3000: "MMM",
  };
  let numToArray = num.toString().split("");
  let unitArray = [];
  let romanArray = [];
  for (let i = 0; i < numToArray.length; i++) {
    if (numToArray[i] === "0") continue;
    let zero_to_add = numToArray.length - 1 - i;
    let zeros = "";
    let j = 0;
    while (j < zero_to_add) {
      zeros = zeros + "0";
      j++;
    }
    unitArray.push(numToArray[i] + zeros);
  }
  for (let i = 0; i < unitArray.length; i++) {
    romanArray.push(lookUpRoman[unitArray[i]]);
  }
  return romanArray.join("");
}
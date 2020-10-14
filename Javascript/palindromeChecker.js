function palindrome(str) {
  let newStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  let reversedStr = newStr.split("").reverse().join("");
  if (newStr === reversedStr) {
    return true;
  }
  else {
    return false
  }
}
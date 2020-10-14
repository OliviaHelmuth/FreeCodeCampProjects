function telephoneCheck(str) {
  let digitLength = /[\d]/g;
  let invalidSigns = /[\!?@#$%^&*]/g;
  let validCountryCode = /^1/;
  let brackets = /[()]/g;
  let bracketsNumbers = /(\(\d{4,11}\))/;
  let digits = str.match(digitLength);
  let signs = str.match(invalidSigns);
  let countryCode = str.match(validCountryCode);
  let brackets1 = str.match(brackets);
  let brackets2 = str.match(bracketsNumbers);

  if (signs !== null) {
    return false;
  }
  if (digits.length !== 10 && digits.length !== 11) {
    return false;
  }
  if (digits.length == 11 && !countryCode) {
    return false;
  }
  if (brackets1 !== null && brackets1.length !== 2) {
    return false;
  }
  if (brackets2 !== null) {
    return false;
  }
  return true;
}
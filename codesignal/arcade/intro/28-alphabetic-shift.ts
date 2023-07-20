const LOWERCASE_Z_CHAR_CODE = "z".charCodeAt(0);
const UPPERCASE_Z_CHAR_CODE = "Z".charCodeAt(0);
function getNextChar(char: string) {
  const currentCharCode = char.charCodeAt(0);
  switch (currentCharCode) {
    case LOWERCASE_Z_CHAR_CODE:
      return "a";
    case UPPERCASE_Z_CHAR_CODE:
      return "A";
    default:
      return String.fromCharCode(char.charCodeAt(0) + 1);
  }
}

function solution(inputString: string): string {
  return inputString.split("").map(getNextChar).join("");
}

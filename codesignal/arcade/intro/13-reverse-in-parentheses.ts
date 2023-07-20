function reverse(str: string) {
  return str.split("").reverse().join("");
}

function solution(inputString: string): string {
  let stack = [""];
  for (let char of inputString) {
    if (char === "(") {
      stack.push("");
      continue;
    }
    if (char === ")") {
      stack[stack.length - 2] += reverse(stack.pop());
      continue;
    }
    stack[stack.length - 1] += char;
  }

  return stack[0];
}

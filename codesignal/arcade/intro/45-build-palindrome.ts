function reverse(str: string) {
  return str.split("").reverse().join("");
}

function solution(st: string): string {
  // All strings can be palindromes if we were to postfix their reverse to the end.
  // In fact, they could be shorter as we could leave the last character of the first string
  // alone.
  //
  // However, in some cases, we could avoid even adding this string to the end, if
  // the string in question already contained a partial palindrome.
  // In this case, we'd just need to detect this partial palindrome and then complete
  // it using the known first half.
  //
  // To solve the problem we're going to detect the midpoint of the current string
  // and then search for palindromes to the right of this.
  const midpoint = Math.ceil(st.length / 2) - 1;

  // If the string is even we'll use the midpoint directly, but
  // if it's odd we'll start one to the left of it, in order that
  // we can detect if we already have a full odd-length palindrome.
  const start = st.length % 2 === 0 ? midpoint : midpoint - 1;
  for (let i = start; i < st.length; i++) {
    // We test whether the character at j is equal to the character at k,
    // where can be i + 1 or i + 2.
    let j = i;
    let k = st[j] === st[i + 1] ? i + 1 : st[j] === st[i + 2] ? i + 2 : -1;
    // If j does not match any k, then we set k to -1 and skip checking
    // outwards for a palindrome from this point. We increment to the next
    // character...
    if (k === -1) {
      continue;
    }

    while (j >= 0 && k < st.length && st[j] === st[k]) {
      j--;
      k++;
    }

    // If the while-loop ended due to the partial palindrome finishing before
    // reaching the boundaries of the string, skip to the next character.
    if (j >= 0 && k < st.length && st[j] !== st[k]) {
      continue;
    }

    // Otherwise the string between 0 and j (inclusive) should be reversed
    // and appended to complete the palindrome.
    return `${st}${reverse(st.slice(0, j + 1))}`;
  }

  // If no partial palindrome is found searching outwards from each character
  // in the right-side of the string, we should append a reverse of the string
  // excluding its final character. It's final character becomes its midpoint
  // causing us to produce a full odd-length palindrome.
  return `${st}${reverse(st.slice(0, st.length - 1))}`;
}

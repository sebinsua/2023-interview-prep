function solutionBadRegex(s: string): string {
  // TODO: We can't handle strings like aa?bbbb
  //       as we are erroneously classing these as "mixed"
  //       when they are bad no matter how ? is considered.
  const BAD =
    /(?<vowelsOnly>[aeiou]{3,})|(?<consonantsOnly>[bcdfghjklmnpqrstvwxyz]{5,})|(?<vowelsWildcard>[aeiou?]{3,})|(?<consonantsWildcard>[bcdfghjklmnpqrstvwxyz?]{5,})/g;

  // @ts-ignore
  const matches = Array.from(s.matchAll(BAD));
  if (!matches) {
    return "good";
  }

  const [
    matchedVowels,
    matchedConsonants,
    matchedVowelsWithWildcard,
    matchedConsonantsWithWildcard,
  ] = matches.reduce<string[]>(
    ([acc1, acc2, acc3, acc4], [, v1, v2, v3, v4]) => {
      return [acc1 ?? v1, acc2 ?? v2, acc3 ?? v3, acc4 ?? v4];
    },
    []
  );

  if (matchedVowels || matchedConsonants) {
    return "bad";
  }
  if (matchedVowelsWithWildcard || matchedConsonantsWithWildcard) {
    return "mixed";
  }

  return "good";
}

function solution(s: string): string {
  const badRegex = /[aeiou]{3}|[^aeiou?]{5}|[aeiou]{2}[?]{1}[^aeiou]{4}/;
  if (s.match(badRegex)) {
    return "bad";
  }

  const mixedRegex = /[aeiou?]{3}|[^aeiou]{5}/;
  if (s.match(mixedRegex)) {
    return "mixed";
  }

  return "good";
}

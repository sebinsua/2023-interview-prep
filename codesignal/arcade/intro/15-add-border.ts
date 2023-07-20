function solution(picture: string[]): string[] {
  const rows = picture.length;
  const columns = picture[0].length;

  const topBorder = Array(1 + columns + 1)
    .fill("*")
    .join("");
  const bottomBorder = Array(1 + columns + 1)
    .fill("*")
    .join("");

  const framedContents: string[] = [];
  for (let row = 0; row < rows; row++) {
    framedContents.push(`*${picture[row]}*`);
  }

  const framedPicture = [topBorder, ...framedContents, bottomBorder];

  return framedPicture;
}

function isFilePath(path: string[]): boolean {
  return path[path.length - 1].match(/^[^ ].*\.[^\.]+$/) !== null;
}

function solution(fileSystem: string): number {
  let previousLevel = 0;
  let currentLevel = 0;
  let longestPath = 0;
  let currentPath = [""];

  let i = 0;
  while (i < fileSystem.length) {
    if (fileSystem[i] === "\f") {
      if (isFilePath(currentPath)) {
        const filePath = currentPath.join("/");
        longestPath = Math.max(longestPath, filePath.length);
      }

      previousLevel = currentLevel;
      currentLevel = 0;

      i++;

      while (fileSystem[i] === "\t") {
        i++;
        currentLevel++;
      }

      if (currentLevel <= previousLevel) {
        currentPath = currentPath.slice(0, currentLevel);
      }
      currentPath.push("");
    }

    currentPath[currentPath.length - 1] += fileSystem[i];

    i++;
  }

  if (isFilePath(currentPath)) {
    const filePath = currentPath.join("/");
    longestPath = Math.max(longestPath, filePath.length);
  }

  return longestPath;
}

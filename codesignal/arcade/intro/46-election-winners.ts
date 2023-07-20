function solution(votes: number[], k: number): number {
  const maxVote = Math.max(...votes);

  if (k === 0) {
    // If there are no more votes left, then there is only a winner if
    // there is only one person with the maximum number of votes.
    const numberOfMaxVotes = votes.filter((vote) => vote === maxVote).length;
    return numberOfMaxVotes === 1 ? 1 : 0;
  }

  return votes.reduce((acc, vote) => acc + (vote + k > maxVote ? 1 : 0), 0);
}

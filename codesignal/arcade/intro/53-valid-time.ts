function solution(time: string): boolean {
  const [_hours, _minutes] = time.split(":");

  if (_hours.length !== 2 || _minutes.length !== 2) {
    return false;
  }

  const hours = /^\d+$/.test(_hours) ? parseInt(_hours) : -1;
  const minutes = /^\d+$/.test(_minutes) ? parseInt(_minutes) : -1;

  if (hours < 0 || hours > 23) {
    return false;
  }

  if (minutes < 0 || minutes > 59) {
    return false;
  }

  return true;
}

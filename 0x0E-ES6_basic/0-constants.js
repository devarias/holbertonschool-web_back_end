export function taskFirst() {
  return 'I prefer const when I can.';
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  return 'But sometimes let' + getLast();
}

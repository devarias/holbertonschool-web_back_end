export default function iterateThroughObject(reportWithIterator) {
  //   return reportWithIterator.join(' | ');
  let names;
  for (const item of reportWithIterator) {
    names.concat(item);
    if (!item.done) {
      names.concat(" | ");
    }
  }
  return names;
}

function cleanSet(set, startString) {
  if (!startString) return '';

  const results = [];
  for (const item of set) {
    if (item.startsWith(startString)) {
      results.push(item.slice(startString.length));
    }
  }

  return results.join('-');
}

export default cleanSet;

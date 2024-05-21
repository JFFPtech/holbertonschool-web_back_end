function cleanSet(set, startString) {
    const newSet = new Set();
    set.forEach((value) => {
        if (value.startsWith(startString)) {
        newSet.add(value);
        }
    });
    return newSet;
}

export default cleanSet;
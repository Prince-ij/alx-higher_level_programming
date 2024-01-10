#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const elem = list.filter(x => x === searchElement);
  return (elem.length);
};

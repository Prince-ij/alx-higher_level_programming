#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = process.argv.slice(2);

  let first = args[0];
  let i;

  // Find the maximum value in args
  for (i = 0; i < args.length; i++) {
    if (args[i] > first) {
      first = args[i];
    }
  }

  // Filter out the first value
  const args2 = args.filter(item => item !== first);

  let second = args2[0]; // Use args2 instead of args

  // Find the maximum value in args2
  for (i = 0; i < args2.length; i++) {
    if (args2[i] > second) {
      second = args2[i];
    }
  }

  console.log(second);
}

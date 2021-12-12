let raw = `start-A
start-b
A-c
A-b
b-d
A-end
b-end`;

let raw2 = `dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc`;

let raw3 = `
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW`;

let input = `dr-of
start-KT
yj-sk
start-gb
of-start
IJ-end
VT-sk
end-sk
VT-km
KT-end
IJ-of
dr-IJ
yj-IJ
KT-yj
gb-VT
dr-yj
VT-of
PZ-dr
KT-of
KT-gb
of-gb
dr-sk
dr-VT`;

let count = 0;
let visitedPathes = new Set();

let visit = (graph, current, path, twice) => {
  path.push(current);
  if (current === "end") {
    if (!visitedPathes.has(path.join(","))) {
      ++count;
      //      console.log(path);
    }
    visitedPathes.add(path.join(","));
    return path;
  }

  let caves;

  if (current[0].toLowerCase() === current[0]) {
    if (twice === current) {
      caves = graph[current];
      twice = undefined;
    } else {
      Object.entries(graph).forEach(([key, list]) => {
        graph[key] = list.filter((value) => value != current);
      });

      caves = graph[current];

      delete graph[current];
    }
  } else {
    caves = graph[current];
  }

  if (caves) {
    caves.forEach((cave) => {
      visit({ ...graph }, cave, [...path], twice);
    });
  }

  return path;
};

let solve = (raw) => {
  let graph = raw.split("\n").reduce((acc, pair) => {
    const [left, right] = pair.split("-");
    return {
      ...acc,
      [left]: acc[left] ? [...acc[left], right] : [right],
      [right]: acc[right] ? [...acc[right], left] : [left],
    };
  }, {});
  Object.keys(graph).forEach((key) => {
    if (key.toLowerCase() === key && key != "start" && key != "end") {
      visit({ ...graph }, "start", [], key);
    }
  });
  console.log(count);
};
solve(input);

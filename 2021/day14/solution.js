let raw = `NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C`;

let raw2 = `CHBBKPHCPHPOKNSNCOVB

SP -> K
BB -> H
BH -> S
BS -> H
PN -> P
OB -> S
ON -> C
HK -> K
BN -> V
OH -> F
OF -> C
SN -> N
PF -> H
CF -> F
HN -> S
SK -> F
SS -> C
HH -> C
SO -> B
FS -> P
CB -> V
NK -> F
KK -> P
VN -> H
KF -> K
PS -> B
HP -> B
NP -> P
OO -> B
FB -> V
PO -> B
CN -> O
HC -> B
NN -> V
FV -> F
BK -> K
VC -> K
KV -> V
VF -> V
FO -> O
FK -> B
HS -> C
OV -> F
PK -> F
VV -> S
NH -> K
SH -> H
VB -> H
NF -> P
OK -> B
FH -> F
CO -> V
BC -> K
PP -> S
OP -> V
VO -> C
NC -> F
PB -> F
KO -> O
BF -> C
VS -> K
KN -> P
BP -> F
KS -> V
SB -> H
CH -> N
HF -> O
CV -> P
NB -> V
FF -> H
OS -> S
CS -> S
KC -> F
NS -> N
NV -> O
SV -> V
BO -> V
BV -> V
CC -> F
CK -> H
KP -> C
KH -> H
KB -> F
PH -> P
VP -> P
OC -> F
FP -> N
HV -> P
HB -> H
PC -> N
VK -> H
HO -> V
CP -> F
SF -> N
FC -> P
NO -> K
VH -> S
FN -> F
PV -> O
SC -> N`;

let solve = (raw) => {
  let template = raw.split("\n\n")[0];
  let map = {};
  let input = raw
    .split("\n\n")[1]
    .split("\n")
    .forEach((row) => {
      let [left, right] = row.split(" -> ");
      map[left] = right;
    });

  for (let i = 0; i < 40; ++i) {
    console.log("iteration", i);
    let newString = "";
    for (let j = 0; j < template.length - 1; ++j) {
      let pattern = template.slice(j, j + 2);
      newString += template[j];
      if (map[pattern]) {
        newString += map[pattern];
      }
    }
    template = newString + template[template.length - 1];
    //    console.log("iteration: ", template.length, template);
  }
  let countMap = [];
  Object.values(map).forEach((value) => {
    countMap[value] = template.split(value).length - 1;
  });
  let sorted = Object.values(countMap).sort((a, b) => b - a);
  console.log(sorted[0], sorted[sorted.length - 1], sorted[0] - sorted[sorted.length - 1]);
  return sorted[0] - sorted[sorted.length - 1];
};

let solve2 = (raw) => {
  let template = raw.split("\n\n")[0];
  let map = {};
  raw
    .split("\n\n")[1]
    .split("\n")
    .forEach((row) => {
      let [left, right] = row.split(" -> ");
      map[left] = right;
    });

  let matchMap = {};
  for (let i = 0; i < template.length - 1; ++i) {
    let key = template[i] + template[i + 1];
    matchMap[key] = matchMap[key] ? ++matchMap[key] : 1;
  }
  for (let i = 0; i < 40; ++i) {
    let newMatchMap = {};
    Object.entries(matchMap).forEach(([key, count]) => {
      let one = key[0] + map[key];
      let two = map[key] + key[1];
      newMatchMap[one] = newMatchMap[one] === undefined ? count : newMatchMap[one] + count;
      newMatchMap[two] = newMatchMap[two] === undefined ? count : newMatchMap[two] + count;
    });
    matchMap = newMatchMap;
  }

  let countMap = {};
  Object.entries(matchMap).forEach(([key, count]) => {
    countMap[key[0]] = countMap[key[0]] === undefined ? count : countMap[key[0]] + count;
    countMap[key[1]] = countMap[key[1]] === undefined ? count : countMap[key[1]] + count;
  });

  let sorted = Object.values(countMap).sort((a, b) => b - a);
  return Math.ceil(sorted[0] / 2) - Math.ceil(sorted[sorted.length - 1] / 2);
};
solve2(raw2);

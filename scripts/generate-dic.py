import sys
import re

rules = {
	"autrice/S*":
	[
		"autrice/F*"
	],
	"chef/S.": [],
	"cheffe/S.":
	[
		"cheffe/F."
	],
	"docteur/S.": [],
	"docteure/S.":
	[
		"docteure/F."
	],
	"sous-chef/S.":
	[
		"sous-cheffe/F."
	]
}

newlines = [
	"iel/Q'Q*Si",
	"iels/Q'Q*Si",
	"ielle/Q'Q*Si",
	"ielles/Q'Q*Si",
	"ellui/D'Q'Q*",
	"ellui-même/D'Q'Q*",
	"elleux/D'Q'",
	"elleux-mêmes/D'Q'",
	"celleux",
	"celleux-ci",
	"celleux-là",
	"cellui",
	"cellui-ci",
	"cellui-là",
	"toustes",
	"tou·te·s",
	"tous·tes",
	"lae",
	"maon",
	"taon",
	"saon",
	"adjudante-cheffe/L'D'Q'",
	"adjudant·e-chef·fe/L'D'Q'",
	"adjudantes-cheffes/D'Q'",
	"adjudant·e·s-chef·fe·s/D'Q'",
	"adjudant·es-chef·fes/D'Q'"
]

if len(sys.argv) != 2:
	print("Usage: "+sys.argv[0]+" FILE")
	exit(0)

filename = sys.argv[1]

tmpOutput = []
with open(filename, 'r') as f:
	for line in f:
		line = line.replace("\n", "")
		if line in rules:
			tmpOutput = tmpOutput + rules[line]
		else:
			tmpOutput.append(line)

tmpOutput = tmpOutput + newlines

print(str(len(tmpOutput)-1))
for line in tmpOutput[1:]:
	print(line)

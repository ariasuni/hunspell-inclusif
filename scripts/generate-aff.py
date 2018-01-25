import sys
import re

rules = {
	"WORDCHARS -’'1234567890.":
	[
		"WORDCHARS -’'1234567890.·"
	],
	"REP ^Ca$ Ça":
	[
		"REP ' ·",
		"REP 'aiche' ·aiche·",
		"REP 'e' ·e·",
		"REP 'euse' ·euse·",
		"REP 'esse' ·esse·",
		"REP 'fe' ·fe·",
		"REP 'gne' ·gne·",
		"REP 'he' ·he·",
		"REP 'igne' ·igne·",
		"REP 'îche' ·îche·",
		"REP 'le' ·le·",
		"REP 'lle' ·lle·",
		"REP 'ne' ·ne·",
		"REP 'olle' ·olle·",
		"REP 'oresse' ·oresse·",
		"REP 'que' ·que·",
		"REP 'rice' ·rice·",
		"REP 'resse' ·resse·",
		"REP 'sse' ·sse·",
		"REP 'te' ·te·",
		"REP 'ue' ·ue·",
		"REP 've' ·ve·",
		"REP 'ë' ·ë·",
		"REP 'èche' ·èche·",
		"REP 'èke' ·èke·",
		"REP 'ène' ·ène·",
		"REP 'ère' ·ère·",
		"REP 'ète' ·ète·",
		"REP 'ève' ·ève·",
		"REP 'üe' ·üe·",
		"REP 'e' ·ë·",
		"REP 'eche' ·èche·",
		"REP 'eke' ·èke·",
		"REP 'ene' ·ène·",
		"REP 'ere' ·ère·",
		"REP 'ete' ·ète·",
		"REP 'eve' ·ève·",
		"REP 'ue' ·üe·",
		"REP ^Ca$ Ça"
	],
	"BREAK ·": [],
	"SFX F. e s [éiï]e":
	[
		"SFX F. e s [éiï]e",
		"SFX F. e ·e [éiï]e",
		"SFX F. e ·e·s [éiï]e",
		"SFX F. e ·es [éiï]e"
	],
	"SFX F. rice eurs [dt]rice":
	[
		"SFX F. rice eurs [dt]rice",
		"SFX F. rice eur·rice [dt]rice",
		"SFX F. rice eur·rices [dt]rice",
		"SFX F. rice eur·rice·s [dt]rice",
		"SFX F. rice eurice [dt]rice",
		"SFX F. rice eurices [dt]rice"
	],
	"SFX F. de ds de":
	[
		"SFX F. de ds de",
		"SFX F. de d·e de",
		"SFX F. de d·e·s de",
		"SFX F. de d·es de"
	],
	"SFX F. fe f fe":
	[
		"SFX F. fe f [^f]fe"
	],
	"SFX F. fe fs fe":
	[
		"SFX F. fe fs [^f]fe",
		"SFX F. fe f·e [^f]fe",
		"SFX F. fe f·e·s [^f]fe",
		"SFX F. fe f·es [^f]fe",
		"SFX F. ffe f effe",
		"SFX F. ffe fs effe",
		"SFX F. ffe f·fe effe",
		"SFX F. ffe f·fe·s effe",
		"SFX F. ffe f·fes effe"
	],
	"SFX F. anche ancs anche":
	[
		"SFX F. anche ancs anche",
		"SFX F. anche anc·he anche",
		"SFX F. anche anc·he·s anche",
		"SFX F. anche anc·hes anche"
	],
	"SFX F. èche ecs èche":
	[
		"SFX F. èche ecs èche",
		"SFX F. èche ec·èche èche",
		"SFX F. èche ec·èche·s èche",
		"SFX F. èche ec·èches èche"
	],
	"SFX F. aiche ais aiche":
	[
		"SFX F. aiche ais aiche",
		"SFX F. aiche ais·iche aiche",
		"SFX F. aiche ais·aiche aiche",
		"SFX F. aiche ai·iche·s aiche",
		"SFX F. aiche ai·aiche·s aiche",
		"SFX F. aiche ai·iches aiche",
		"SFX F. aiche ai·aiches aiche"
	],
	"SFX F. aîche ais aîche":
	[
		"SFX F. aîche ais aîche",
		"SFX F. aîche ais·îche aîche",
		"SFX F. aîche ais·aîche aîche",
		"SFX F. aîche ai·îche·s aîche",
		"SFX F. aîche ai·aîche·s aîche",
		"SFX F. aîche ai·îches aîche",
		"SFX F. aîche ai·aîches aîche"
	],
	"SFX F. khe khs khe":
	[
		"SFX F. khe khs khe",
		"SFX F. khe kh·e khe",
		"SFX F. khe kh·e·s khe",
		"SFX F. khe kh·es khe"
	],
	"SFX F. he hs [ut]he":
	[
		"SFX F. he hs [ut]he",
		"SFX F. he h·e [ut]he",
		"SFX F. he h·e·s [ut]he",
		"SFX F. he h·es [ut]he"
	],
	"SFX F. ke ks [^è]ke":
	[
		"SFX F. ke ks [^è]ke",
		"SFX F. ke k·e [^è]ke",
		"SFX F. ke k·e·s [^è]ke",
		"SFX F. ke k·es [^è]ke"
	],
	"SFX F. èke eks èke":
	[
		"SFX F. èke eks èke",
		"SFX F. èke ek·èke èke",
		"SFX F. èke ek·èke·s èke",
		"SFX F. èke ek·èkes èke"
	],
	"SFX F. le ls [aiouûh]le":
	[
		"SFX F. le ls [aiouûh]le",
		"SFX F. le l·e [aiouûh]le",
		"SFX F. le l·e·s [aiouûh]le",
		"SFX F. le l·es [aiouûh]le"
	],
	"SFX F. lle ls [eiu]lle":
	[
		"SFX F. lle ls [eiu]lle",
		"SFX F. lle l·le [eiu]lle",
		"SFX F. lle l·le·s [eiu]lle",
		"SFX F. lle l·les [eiu]lle"
	],
	"SFX F. olle ous olle":
	[
		"SFX F. olle ous olle",
		"SFX F. olle ou·lle olle",
		"SFX F. olle ou·lle·s olle",
		"SFX F. olle ou·lles olle",
		"SFX F. olle ou·olle olle",
		"SFX F. olle ou·olle·s olle",
		"SFX F. olle ou·olles olle"
	],
	"SFX F. ne ns [aiouï]ne":
	[
		"SFX F. ne ns [aiouï]ne",
		"SFX F. ne n·e [aiouï]ne",
		"SFX F. ne n·e·s [aiouï]ne",
		"SFX F. ne n·es [aiouï]ne"
	],
	"SFX F. nne ns [aeo]nne":
	[
		"SFX F. nne ns [aeo]nne",
		"SFX F. nne n·ne [aeo]nne",
		"SFX F. nne n·ne·s [aeo]nne",
		"SFX F. nne n·nes [aeo]nne"
	],
	"SFX F. ène ens ène":
	[
		"SFX F. ène ens ène",
		"SFX F. ène en·ène ène",
		"SFX F. ène en·ène·s ène",
		"SFX F. ène en·ènes ène"
	],
	"SFX F. igne ins igne":
	[
		"SFX F. igne ins igne",
		"SFX F. igne in·gne igne",
		"SFX F. igne in·gne·s igne",
		"SFX F. igne in·gnes igne",
		"SFX F. igne in·igne igne",
		"SFX F. igne in·igne·s igne",
		"SFX F. igne in·ignes igne"
	],
	"SFX F. re rs [aiouûy]re":
	[
		"SFX F. re rs [aiouûy]re",
		"SFX F. re r·e [aiouûy]re",
		"SFX F. re r·e·s [aiouûy]re",
		"SFX F. re r·es [aiouûy]re"
	],
	"SFX F. ère ers ère":
	[
		"SFX F. ère ers ère",
		"SFX F. ère er·ère ère",
		"SFX F. ère er·ère·s ère",
		"SFX F. ère er·ères ère"
	],
	"SFX F. se s [^us]se":
	[
		"SFX F. se s [^us]se",
		"SFX F. se s·e [^us]se",
		"SFX F. se s·es [^us]se"
	],
	"SFX F. esse es [^eo].esse":
	[
		"SFX F. esse es [^eo].esse",
		"SFX F. esse e·sse [^eo].esse",
		"SFX F. esse e·sse·s [^eo].esse",
		"SFX F. esse e·sses [^eo].esse"
	],
	"SFX F. rofesse rofès rofesse":
	[
		"SFX F. rofesse rofès rofesse",
		"SFX F. rofesse rofès·esse rofesse",
		"SFX F. rofesse rofès·esses rofesse",
		"SFX F. rofesse rofè·esse·s rofesse",
		"SFX F. rofesse rofè·esses rofesse"
	],
	"SFX F. eresse eurs eresse":
	[
		"SFX F. eresse eurs eresse",
		"SFX F. eresse eur·resse eresse",
		"SFX F. eresse eur·resse·s eresse",
		"SFX F. eresse eur·resses eresse",
		"SFX F. eresse euresse eresse",
		"SFX F. eresse euresses eresse"
	],
	"SFX F. oresse eurs oresse":
	[
		"SFX F. oresse eurs oresse",
		"SFX F. oresse eur·oresse oresse",
		"SFX F. oresse eur·oresse·s oresse",
		"SFX F. oresse eur·oresses oresse"
	],
	"SFX F. sse s [^e]sse":
	[
		"SFX F. sse s [^e]sse",
		"SFX F. sse s·se [^e]sse",
		"SFX F. sse s·ses [^e]sse",
		"SFX F. sse ·sse·s [^e]sse",
		"SFX F. sse ·sses [^e]sse"
	],
	"SFX F. sse s [^e]sse":
	[
		"SFX F. sse s [^e]sse",
		"SFX F. sse s·se [^e]sse",
		"SFX F. sse s·ses [^e]sse",
		"SFX F. sse ·sse·s [^e]sse",
		"SFX F. sse ·sses [^e]sse"
	],
	"SFX F. use us [^eo]use":
	[
		"SFX F. use us [^eo]use",
		"SFX F. use us·e [^eo]use",
		"SFX F. use us·es [^eo]use",
		"SFX F. use u·se·s [^eo]use",
		"SFX F. use u·ses [^eo]use"
	],
	"SFX F. euse eurs euse":
	[
		"SFX F. euse eurs euse",
		"SFX F. euse eur·se euse",
		"SFX F. euse eur·se·s euse",
		"SFX F. euse eur·ses euse",
		"SFX F. euse eur·euse euse",
		"SFX F. euse eur·euse·s euse",
		"SFX F. euse eur·euses euse",
		"SFX F. euse eureuse euse",
		"SFX F. euse eureuses euse"
	],
	"SFX F. te ts [^èt]te":
	[
		"SFX F. te ts [^èt]te",
		"SFX F. te t·e [^èt]te",
		"SFX F. te t·e·s [^èt]te",
		"SFX F. te t·es [^èt]te"
	],
	"SFX F. tte ts tte":
	[
		"SFX F. tte ts tte",
		"SFX F. tte t·te tte",
		"SFX F. tte t·te·s tte",
		"SFX F. tte t·tes tte"
	],
	"SFX F. ète ets ète":
	[
		"SFX F. ète ets ète",
		"SFX F. ète et·ète ète",
		"SFX F. ète et·ète·s ète",
		"SFX F. ète et·ètes ète"
	],
	"SFX F. ue us [^gq]ue":
	[
		"SFX F. ue us [^gq]ue",
		"SFX F. ue u·e [^gq]ue",
		"SFX F. ue u·e·s [^gq]ue",
		"SFX F. ue u·es [^gq]ue"
	],
	"SFX F. gue gs gue":
	[
		"SFX F. gue gs gue",
		"SFX F. gue g·ue gue",
		"SFX F. gue g·ue·s gue",
		"SFX F. gue g·ues gue"
	],
	"SFX F. cque cs cque":
	[
		"SFX F. cque cs cque",
		"SFX F. cque c·que cque",
		"SFX F. cque c·que·s cque",
		"SFX F. cque c·ques cque"
	],
	"SFX F. que cs [^c]que":
	[
		"SFX F. que cs [^c]que",
		"SFX F. que c·que [^c]que",
		"SFX F. que c·que·s [^c]que",
		"SFX F. que c·ques [^c]que"
	],
	"SFX F. ève efs ève":
	[
		"SFX F. ève efs ève",
		"SFX F. ève ef·ève ève",
		"SFX F. ève ef·ève·s ève",
		"SFX F. ève ef·èves ève"
	],
	"SFX F. ve fs [iïu]ve":
	[
		"SFX F. ve fs [iïu]ve",
		"SFX F. ve f·ve [iïu]ve",
		"SFX F. ve f·ve·s [iïu]ve",
		"SFX F. ve f·ves [iïu]ve"
	],
	"SFX F. uë us uë":
	[
		"SFX F. uë us uë",
		"SFX F. uë u·ë uë",
		"SFX F. uë u·ë·s uë",
		"SFX F. uë u·ës uë"
	],
	"SFX F. üe us üe":
	[
		"SFX F. üe us üe",
		"SFX F. uë u·üe uë",
		"SFX F. uë u·üe·s uë",
		"SFX F. uë u·ües uë"
	],
	"SFX F. ze z ze":
	[
		"SFX F. ze z ze",
		"SFX F. ze z·e ze",
		"SFX F. ze z·es ze"
	],
	"SFX W. ce x ce":
	[
		"SFX W. ce x ce",
		"SFX W. ce x·ce ce",
		"SFX W. ce x·ces ce"
	],
	"SFX W. use ux [eo]use":
	[
		"SFX W. euse eux euse",
		"SFX W. euse eux·se euse",
		"SFX W. euse eux·ses euse",
		"SFX W. euse eux·euse euse",
		"SFX W. euse eux·euses euse",
		"SFX W. ouse oux ouse",
		"SFX W. ouse oux·se ouse",
		"SFX W. ouse oux·ses ouse",
		"SFX W. ouse oux·ouse ouse",
		"SFX W. ouse oux·ouses ouse"
	],
	"SFX W. ausse aux ausse":
	[
		"SFX W. ausse aux ausse",
		"SFX W. ausse aux·sse ausse",
		"SFX W. ausse aux·sses ausse",
		"SFX W. ausse aux·ausse ausse",
		"SFX W. ausse aux·ausses ausse"
	],
	"SFX W. ousse oux ousse":
	[
		"SFX W. ousse oux ousse",
		"SFX W. ousse oux·sse ousse",
		"SFX W. ousse oux·sses ousse",
		"SFX W. ousse oux·ousse ousse",
		"SFX W. ousse oux·ousses ousse"
	],
	"SFX W. ale aux ale":
	[
		"SFX W. ale aux ale",
		"SFX W. ale al·e ale",
		"SFX W. ale aux·les ale",
		"SFX W. ale aux·ales ale"
	],
	"SFX W. elle eaux elle":
	[
		"SFX W. elle eaux elle",
		"SFX W. elle eaulle elle",
		"SFX W. elle elleau elle",
		"SFX W. elle eau·lle elle",
		"SFX W. elle eaulles elle",
		"SFX W. elle elleaux elle",
		"SFX W. elle eaux·lles elle",
		"SFX W. elle eau·elle elle",
		"SFX W. elle eaux·elles elle"
	],
	"SFX W. elle el [bv]elle":
	[
		"SFX W. elle el [bv]elle",
		"SFX W. elle el·le [bv]elle"
	],
	"SFX W. ieille ieil ieille":
	[
		"SFX W. ieille ieil ieille",
		"SFX W. ieille ieil·le ieille",
		"SFX W. ieille ieil·le ieille",
		"SFX W. ieille ieux·ieille ieille",
		"SFX W. ieille ieux·ieilles ieille",
		"SFX W. ieille ieux·ille ieille",
		"SFX W. ieille ieux·illes ieille"
	],
	"SFX F* e s/D'Q' [éiï]e":
	[
		"SFX F* e s/D'Q' [éiï]e",
		"SFX F* e ·e/D'L'Q' [éiï]e",
		"SFX F* e ·e·s/D'Q' [éiï]e",
		"SFX F* e ·es/D'Q' [éiï]e"
	],
	"SFX F* rice eurs/D'Q' [dt]rice":
	[
		"SFX F* rice eurs/D'Q' [dt]rice",
		"SFX F* rice eur·rice/D'L'Q' [dt]rice",
		"SFX F* rice eur·rice·s/D'Q' [dt]rice",
		"SFX F* rice eur·rices/D'Q' [dt]rice",
		"SFX F* rice eurice/D'L'Q' [dt]rice",
		"SFX F* rice eurices/D'Q' [dt]rice"
	],
	"SFX F* de ds/D'Q' de":
	[
		"SFX F* de ds/D'Q' de",
		"SFX F* de d·e/D'L'Q' de",
		"SFX F* de d·e·s/D'Q' de",
		"SFX F* de d·es/D'Q' de"
	],
	"SFX F* he hs/D'Q' [ut]he":
	[
		"SFX F* he hs/D'Q' [ut]he",
		"SFX F* he h·e/D'L'Q' [ut]he",
		"SFX F* he h·e·s/D'Q' [ut]he",
		"SFX F* he h·es/D'Q' [ut]he"
	],
	"SFX F* èke eks/D'Q' èke":
	[
		"SFX F* èke eks/D'Q' èke",
		"SFX F* èke ek·èke/D'L'Q' èke",
		"SFX F* èke ek·èke·s/D'Q' èke",
		"SFX F* èke ek·èkes/D'Q' èke"
	],
	"SFX F* le ls/D'Q' [aiouû]le":
	[
		"SFX F* le ls/D'Q' [aiouû]le",
		"SFX F* le l·e/D'L'Q' [aiouû]le",
		"SFX F* le l·e·s/D'Q' [aiouû]le",
		"SFX F* le l·es/D'Q' [aiouû]le"
	],
	"SFX F* lle ls/D'Q' [eiu]lle":
	[
		"SFX F* lle ls/D'Q' [eiu]lle",
		"SFX F* lle l·le/D'L'Q' [eiu]lle",
		"SFX F* lle l·le·s/D'Q' [eiu]lle",
		"SFX F* lle l·les/D'Q' [eiu]lle"
	],
	"SFX F* ne ns/D'Q' [aiouï]ne":
	[
		"SFX F* ne ns/D'Q' [aiouï]ne",
		"SFX F* ne n·e/D'L'Q' [aiouï]ne",
		"SFX F* ne n·e·s/D'Q' [aiouï]ne",
		"SFX F* ne n·es/D'Q' [aiouï]ne"
	],
	"SFX F* nne ns/D'Q' [aeo]nne":
	[
		"SFX F* nne ns/D'Q' [aeo]nne",
		"SFX F* nne n·ne/D'L'Q' [aeo]nne",
		"SFX F* nne n·ne·s/D'Q' [aeo]nne",
		"SFX F* nne n·nes/D'Q' [aeo]nne"
	],
	"SFX F* gne ns/D'Q' igne":
	[
		"SFX F* gne ns/D'Q' igne",
		"SFX F* gne n·igne/D'L'Q' igne",
		"SFX F* gne n·igne·s/D'Q' igne",
		"SFX F* gne n·ignes/D'Q' igne",
		"SFX F* gne n·gne/D'L'Q' igne",
		"SFX F* gne n·gne·s/D'Q' igne",
		"SFX F* gne n·gnes/D'Q' igne"
	],
	"SFX F* re rs/D'Q' [aiouûy]re":
	[
		"SFX F* re rs/D'Q' [aiouûy]re",
		"SFX F* re r·e/D'L'Q' [aiouûy]re",
		"SFX F* re r·e·s/D'Q' [aiouûy]re",
		"SFX F* re r·es/D'Q' [aiouûy]re"
	],
	"SFX F* ère ers/D'Q' ère":
	[
		"SFX F* ère ers/D'Q' ère",
		"SFX F* ère er·ère/D'L'Q' ère",
		"SFX F* ère er·ère·s/D'Q' ère",
		"SFX F* ère er·ères/D'Q' ère"
	],
	"SFX F* se s/D'L'Q' [^us]se":
	[
		"SFX F* se s/D'L'Q' [^us]se",
		"SFX F* se s·e/D'L'Q' [^us]se",
		"SFX F* se s·es/D'Q' [^us]se"
	],
	"SFX F* esse es/D'Q' [^eo].esse":
	[
		"SFX F* esse es/D'Q' [^eo].esse",
		"SFX F* esse e·sse/D'L'Q' [^eo].esse",
		"SFX F* esse e·sse·s/D'Q' [^eo].esse",
		"SFX F* esse e·sses/D'Q' [^eo].esse"
	],
	"SFX F* eresse eurs/D'Q' eresse":
	[
		"SFX F* eresse eurs/D'Q' eresse",
		"SFX F* eresse eur·resse/D'L'Q' eresse",
		"SFX F* eresse eur·resse·s/D'Q' eresse",
		"SFX F* eresse eur·resses/D'Q' eresse",
		"SFX F* eresse euresse/D'L'Q' eresse",
		"SFX F* eresse euresses/D'Q' eresse"
	],
	"SFX F* oresse eurs/D'Q' oresse":
	[
		"SFX F* oresse eurs/D'Q' oresse",
		"SFX F* oresse eur·oresse/D'L'Q' oresse",
		"SFX F* oresse eur·oresse·s/D'Q' oresse",
		"SFX F* oresse eur·oresses/D'Q' oresse"
	],
	"SFX F* sse s/D'L'Q' [^e]sse":
	[
		"SFX F* sse s/D'L'Q' [^e]sse",
		"SFX F* sse s·se/D'L'Q' [^e]sse",
		"SFX F* sse s·ses/D'Q' [^e]sse",
		"SFX F* sse ·sse·s/D'Q' [^e]sse",
		"SFX F* sse ·sses/D'Q' [^e]sse"
	],
	"SFX F* use us/D'L'Q' [^eo]use":
	[
		"SFX F* use us/D'L'Q' [^eo]use",
		"SFX F* use us·e/D'L'Q' [^eo]use",
		"SFX F* use us·es/D'Q' [^eo]use",
		"SFX F* use u·se·s/D'Q' [^eo]use",
		"SFX F* use u·ses/D'Q' [^eo]use"
	],
	"SFX F* euse eurs/D'Q' euse":
	[
		"SFX F* euse eurs/D'Q' euse",
		"SFX F* euse eur·se/D'L'Q' euse",
		"SFX F* euse eur·se·s/D'Q' euse",
		"SFX F* euse eur·ses/D'Q' euse",
		"SFX F* euse eur·euse/D'L'Q' euse",
		"SFX F* euse eur·euse·s/D'Q' euse",
		"SFX F* euse eur·euses/D'Q' euse",
		"SFX F* euse eureuse/D'L'Q' euse",
		"SFX F* euse eureuses/D'Q' euse"
	],
	"SFX F* te ts/D'Q' [^èt]te":
	[
		"SFX F* te ts/D'Q' [^èt]te",
		"SFX F* te t·e/D'L'Q' [^èt]te",
		"SFX F* te t·e·s/D'Q' [^èt]te",
		"SFX F* te t·es/D'Q' [^èt]te"
	],
	"SFX F* tte ts/D'Q' tte":
	[
		"SFX F* tte ts/D'Q' tte",
		"SFX F* tte t·te/D'L'Q' tte",
		"SFX F* tte t·te·s/D'Q' tte",
		"SFX F* tte t·tes/D'Q' tte"
	],
	"SFX F* ète ets/D'Q' ète":
	[
		"SFX F* ète ets/D'Q' ète",
		"SFX F* ète et·ète/D'L'Q' ète",
		"SFX F* ète et·ète·s/D'Q' ète",
		"SFX F* ète et·ètes/D'Q' ète"
	],
	"SFX F* ue us/D'Q' [^gq]ue":
	[
		"SFX F* ue us/D'Q' [^gq]ue",
		"SFX F* ue u·e/D'L'Q' [^gq]ue",
		"SFX F* ue u·e·s/D'Q' [^gq]ue",
		"SFX F* ue u·es/D'Q' [^gq]ue"
	],
	"SFX F* gue gs/D'Q' gue":
	[
		"SFX F* gue gs/D'Q' gue",
		"SFX F* gue g·ue/D'L'Q' gue",
		"SFX F* gue g·ue·s/D'Q' gue",
		"SFX F* gue g·ues/D'Q' gue"
	],
	"SFX F* cque cs/D'Q' cque":
	[
		"SFX F* cque cs/D'Q' cque",
		"SFX F* cque c·que/D'L'Q' cque",
		"SFX F* cque c·que·s/D'Q' cque",
		"SFX F* cque c·ques/D'Q' cque"
	],
	"SFX F* que cs/D'Q' [^c]que":
	[
		"SFX F* que cs/D'Q' [^c]que",
		"SFX F* que c·que/D'L'Q' [^c]que",
		"SFX F* que c·que·s/D'Q' [^c]que",
		"SFX F* que c·ques/D'Q' [^c]que"
	],
	"SFX F* ève efs/D'Q' ève":
	[
		"SFX F* ève efs/D'Q' ève",
		"SFX F* ève ef·ève/D'L'Q' ève",
		"SFX F* ève ef·ève·s/D'Q' ève",
		"SFX F* ève ef·èves/D'Q' ève"
	],
	"SFX F* ve fs/D'Q' [iïu]ve":
	[
		"SFX F* ve fs/D'Q' [iïu]ve",
		"SFX F* ve f·ve/D'L'Q' [iïu]ve",
		"SFX F* ve f·ve·s/D'Q' [iïu]ve",
		"SFX F* ve f·ves/D'Q' [iïu]ve"
	],
	"SFX F* uë us/D'Q' uë":
	[
		"SFX F* uë us/D'Q' uë",
		"SFX F* uë u·ë/D'L'Q' uë",
		"SFX F* uë u·ë·s/D'Q' uë",
		"SFX F* uë u·ës/D'Q' uë"
	],
	"SFX F* üe us/D'Q' üe":
	[
		"SFX F* üe us/D'Q' üe",
		"SFX F* üe u·üe/D'L'Q' üe",
		"SFX F* üe u·üe·s/D'Q' üe",
		"SFX F* üe u·ües/D'Q' üe"
	],
	"SFX W* ce x/D'L'Q' ce":
	[
		"SFX W* ce x/D'L'Q' ce",
		"SFX W* ce x·ce/D'Q' ce",
		"SFX W* ce x·ces/D'Q' ce"
	],
	"SFX W* use ux/D'L'Q' [eo]use":
	[
		"SFX W* euse eux/D'L'Q' euse",
		"SFX W* euse eux·se/D'L'Q' euse",
		"SFX W* euse eux·ses/D'Q' euse",
		"SFX W* euse eux·euse/D'L'Q' euse",
		"SFX W* euse eux·euses/D'Q' euse",
		"SFX W* ouse oux/D'L'Q' ouse",
		"SFX W* ouse oux·se/D'L'Q' ouse",
		"SFX W* ouse oux·ses/D'Q' ouse",
		"SFX W* ouse oux·ouse/D'L'Q' ouse",
		"SFX W* ouse oux·ouses/D'Q' ouse"
	],
	"SFX W* ousse oux/D'L'Q' ousse":
	[
		"SFX W* ousse oux/D'L'Q' ousse",
		"SFX W* ousse oux·sse/D'L'Q' ousse",
		"SFX W* ousse oux·sses/D'Q' ousse",
		"SFX W* ousse oux·ousse/D'L'Q' ousse",
		"SFX W* ousse oux·ousses/D'Q' ousse"
	],
	"SFX W* ausse aux/D'L'Q' ausse":
	[
		"SFX W* ausse aux/D'L'Q' ausse",
		"SFX W* ausse aux·sse/D'L'Q' ausse",
		"SFX W* ausse aux·sses/D'Q' ausse",
		"SFX W* ausse aux·ausse/D'L'Q' ausse",
		"SFX W* ausse aux·ausses/D'Q' ausse"
	],
	"SFX W* ale al/D'L'Q' ale":
	[
		"SFX W* ale al/D'L'Q' ale",
		"SFX W* ale al·e/D'L'Q' ale"
	],
	"SFX W* ale aux/D'Q' ale":
	[
		"SFX W* ale aux/D'Q' ale",
		"SFX W* ale aux·les/D'Q' ale",
		"SFX W* ale aux·ales/D'Q' ale"
	],
	"SFX W* elle eaux/D'Q' elle":
	[
		"SFX W* elle eaux/D'Q' elle",
		"SFX W* elle eaulle/D'L'Q' elle",
		"SFX W* elle elleau/D'L'Q' elle",
		"SFX W* elle eau·lle/D'L'Q' elle",
		"SFX W* elle eaulles/D'Q' elle",
		"SFX W* elle elleaux/D'Q' elle",
		"SFX W* elle eaux·lles/D'Q' elle",
		"SFX W* elle eau·elle/D'L'Q' elle",
		"SFX W* elle eaux·elles/D'Q' elle"
	],
	"SFX zA avoir eues avoir":
	[
		"SFX zA avoir eues avoir",
		"SFX zA avoir eu·e avoir",
		"SFX zA avoir eu·e·s avoir"
	],
	"SFX aA ller llées/q' aller":
	[
		"SFX aA ller llées/q' aller",
		"SFX aA ller llé·e/q' aller",
		"SFX aA ller llé·e·s/q' aller",
		"SFX aA ller llé·es/q' aller"
	],
	"SFX aD voyer voyées/q' envoyer":
	[
		"SFX aD voyer voyées/q' envoyer",
		"SFX aD voyer voyé·e/q' envoyer",
		"SFX aD voyer voyé·e·s/q' envoyer",
		"SFX aD voyer voyé·es/q' envoyer"
	],
	"SFX p+ ir ies/D'Q' ir":
	[
		"SFX p+ ir ies/D'Q' ir",
		"SFX p+ er é·e/L'D'Q' er",
		"SFX p+ er é·e·s/D'Q' er",
		"SFX p+ er é·es/D'Q' er",
		"SFX p+ ir i·e/L'D'Q' ir",
		"SFX p+ ir i·e·s/D'Q' ir",
		"SFX p+ ir i·es/D'Q' ir"
	],
	"SFX yK bduire bduites uire":
	[
		"SFX yK bduire bduites uire",
		"SFX yK bduire bduit·e uire",
		"SFX yK bduire bduit·e·s uire",
		"SFX yK bduire bduit·es uire"
	],
	"SFX yL uire uites/D'Q' uire":
	[
		"SFX yL uire uites/D'Q' uire",
		"SFX yL uire uit·e/L'D'Q' uire",
		"SFX yL uire uit·e·s/D'Q' uire",
		"SFX yL uire uit·es/D'Q' uire"
	],
	"SFX yM uire uites/D'Q' uire":
	[
		"SFX yM uire uites/D'Q' uire",
		"SFX yM uire uit·e/L'D'Q' uire",
		"SFX yM uire uit·e·s/D'Q' uire",
		"SFX yM uire uit·es/D'Q' uire"
	],
	"SFX yN truire truites uire":
	[
		"SFX yN truire truites uire",
		"SFX yN truire truit·e uire",
		"SFX yN truire truit·e·s uire",
		"SFX yN truire truit·es uire"
	],
	"SFX yO détruire détruites détruire":
	[
		"SFX yO détruire détruites détruire",
		"SFX yO détruire détruit·e détruire",
		"SFX yO détruire détruit·e·s détruire",
		"SFX yO détruire détruit·es détruire"
	],
	"SFX yY ccire ccises/D'Q' occire":
	[
		"SFX yY ccire ccises/D'Q' occire",
		"SFX yY ccire ccis·e/L'D'Q' occire",
		"SFX yY ccire ccis·es/D'Q' occire"
	],
	"SFX yZ rire rites rire":
	[
		"SFX yZ rire rites rire",
		"SFX yZ rire rit·e rire",
		"SFX yZ rire rit·e·s rire",
		"SFX yZ rire rit·es rire"
	],
	"SFX q+ enir enues/D'Q' enir":
	[
		"SFX q+ enir enues/D'Q' enir",
		"SFX q+ enir enu·e/L'D'Q' enir",
		"SFX q+ enir enu·e·s/D'Q' enir",
		"SFX q+ enir enu·es/D'Q' enir"
	],
	"SFX q+ tir ties/D'Q' tir":
	[
		"SFX q+ tir ties/D'Q' tir",
		"SFX q+ tir ti·e/L'D'Q' tir",
		"SFX q+ tir ti·e·s/D'Q' tir",
		"SFX q+ tir ti·es/D'Q' tir"
	],
	"SFX q+ courir courues/D'Q' courir":
	[
		"SFX q+ courir courues/D'Q' courir",
		"SFX q+ courir couru·e/L'D'Q' courir",
		"SFX q+ courir couru·e·s/D'Q' courir",
		"SFX q+ courir couru·es/D'Q' courir"
	],
	"SFX q+ ivre écues vivre":
	[
		"SFX q+ ivre écues vivre",
		"SFX q+ ivre écu·e vivre",
		"SFX q+ ivre écu·e·s vivre",
		"SFX q+ ivre écu·es vivre"
	],
	"SFX q+ aire ues aire":
	[
		"SFX q+ aire ues aire",
		"SFX q+ aire u·e aire",
		"SFX q+ aire u·e·s aire",
		"SFX q+ aire u·es aire"
	],
	"SFX q+ dre dues dre":
	[
		"SFX q+ dre dues dre",
		"SFX q+ dre du·e dre",
		"SFX q+ dre du·e·s dre",
		"SFX q+ dre du·es dre"
	],
	"SFX q+ valoir values .valoir":
	[
		"SFX q+ valoir values .valoir",
		"SFX q+ valoir valu·e .valoir",
		"SFX q+ valoir valu·e·s .valoir",
		"SFX q+ valoir valu·es .valoir"
	],
	"SFX q+ aître ues/D'Q' aître":
	[
		"SFX q+ aître ues/D'Q' aître",
		"SFX q+ aître u·e/L'D'Q' aître",
		"SFX q+ aître u·e·s/D'Q' aître",
		"SFX q+ aître u·es/D'Q' aître"
	]
}

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

current_line = None
counter = 0
line_buffer = []
for line in tmpOutput:
	if current_line:
		line_buffer.append(line)

		if len(line) > 1:
			counter = counter+1
		else:
			print(current_line+" "+str(counter))
			for l in line_buffer:
				print(l)
			current_line = None
	else:
		m = re.search("^((PFX|SFX|MAP|REP|ICONV|OCONV|BREAK)( .+)?) [0-9]+$", line)
		if m:
			line_buffer = []
			current_line = m.group(1)
			counter = 0
		else:
			print(line)

my_file = "my_text_file.txt"

fin = open(my_file, 'w')
fin.close()

text = """— Сейчас. A propos, — прибавила она, опять успокоиваясь, — нынче у меня два очень интересные человека, le vicomte de Mortemart, il est allié aux Montmorency par les Rohans 10, одна из лучших фамилий Франции. Это один из хороших эмигрантов, из настоящих. И потом l'abbé Morio; 11 вы знаете этот глубокий ум? Он был принят государем. Вы знаете?
— А! Я очень рад буду, — сказал князь. — Скажите, — прибавил он, как будто только что вспомнив что-то и особенно-небрежно, тогда как то, о чем он спрашивал, было главной целью его посещения, — правда, что l'impératrice-mère 12 желает назначения барона Функе первым секретарем в Вену? C'est un pauvre sire, ce baron, à ce qu'il paraît 13. — Князь Василий желал определить сына на это место, которое через императрицу Марию Феодоровну старались доставить барону.
Анна Павловна почти закрыла глаза в знак того, что ни она, ни кто другой не могут судить про то, что угодно или нравится императрице.
— Monsieur le baron de Funke a été recommandé à l'impératrice-mère par sa sur 14, — только сказала она грустным, сухим тоном. В то время как Анна Павловна назвала императрицу, лицо ее вдруг представило глубокое и искреннее выражение преданности и уважения, соединенное с грустью, что с ней бывало каждый раз, когда она в разговоре упоминала о своей высокой покровительнице. Она сказала, что ее величество изволила оказать барону Функе beaucoup d'estime 15, и опять взгляд ее подернулся грустью.
Князь равнодушно замолк, Анна Павловна, с свойственною ей придворною и женскою ловкостью и быстротою такта, захотела и щелкануть князя за то, что он дерзнул так отозваться о лице, рекомендованном императрице, и в то же время утешить его.
— Mais à propos de votre famille, — сказала она, — знаете ли, что ваша дочь, с тех пор как выезжает, fait les délices de tout le monde. On la trouve belle comme le jour 16."""

with open(my_file, 'a', encoding='utf-8') as fin:
    fin.write(text)

fout = open(my_file)
print(fout.read())
fout.close()

with open(my_file, 'r') as fin:
    for line in fin:
        print(line, end="")

print()
print()
print()

fout = open(my_file)
x = fout.readlines()
fout.close()

print(x)
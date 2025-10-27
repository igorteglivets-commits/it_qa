adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""


adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)



count_h = adwentures_of_tom_sawer.count("h")
print("Кількість літери 'h' у тексті:", count_h)



words = adwentures_of_tom_sawer.split()
count_title_words = sum(1 for word in words if word.istitle())
print("Кількість слів, що починаються з великої літери:", count_title_words)



words = adwentures_of_tom_sawer.split()
first_index = words.index("Tom")
second_index = words.index("Tom", first_index + 1)
print("Слово 'Tom' зустрічається вдруге на позиції:", second_index)


adwentures_of_tom_sawer_sentences = []
sentence = ""
for char in adwentures_of_tom_sawer:
    sentence += char
    if char in ".!?":
        adwentures_of_tom_sawer_sentences.append(sentence.strip())
        sentence = ""
for i, s in enumerate(adwentures_of_tom_sawer_sentences, 1):
    print(f"{i}: {s}")



fourth_sentence = adwentures_of_tom_sawer_sentences[3]
fourth_sentence_lower = fourth_sentence.lower()
print(fourth_sentence_lower)


starts_with_by_the_time = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)
print("Чи є речення, що починається з 'By the time'? :", starts_with_by_the_time)



last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print("Кількість слів в останньому реченні:", word_count)


init_code = """
if not "Text" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Text'?")

Text = USER_GLOBAL['Text']

if not "SavedText" in USER_GLOBAL:
    raise NotImplementedError("Where is 'SavedText'?")

SavedText = USER_GLOBAL['SavedText']
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "Texts": [
        prepare_test(middle_code='''text_1 = Text()
saver_1 = SavedText()
text_1.write("At the very beginning ")
saver_1.save_text(text_1)
text_1.set_font("ComicSans")
text_1.write("there was nothing.")
text_1.restore(saver_1.get_version(0))''',
                     test="text_1.show()",
                     answer="At the very beginning "),

        prepare_test(middle_code='''text_2 = Text()
saver_2 = SavedText()
text_2.write("Tomorrow at 7:15 PM.")
saver_2.save_text(text_2)
text_2.set_font("ComicSans")
text_2.write(" Sorry. 7:15 AM.")
saver_2.save_text(text_2)
text_2.write(" Near the stadium.")
text_2.restore(saver_2.get_version(1))''',
                     test="text_2.show()",
                     answer="[ComicSans]Tomorrow at 7:15 PM. Sorry. 7:15 AM.[ComicSans]"),

        prepare_test(middle_code='''text_3 = Text()
saver_3 = SavedText()
text_3.write("42+14=56; ")
saver_3.save_text(text_3)
text_3.write("1x11+2=13; ")
saver_3.save_text(text_3)
text_3.write("math is great!")''',
                     test="text_3.show()",
                     answer="42+14=56; 1x11+2=13; math is great!"),

        prepare_test(middle_code='''text_4 = Text()
saver_4 = SavedText()
text_4.write("1. Python ")
saver_4.save_text(text_4)
text_4.set_font("Times New Roman")
text_4.write("2. JavaScript ")
saver_4.save_text(text_4)
text_4.write("3. C# ")
text_4.set_font("Arial")
saver_4.save_text(text_4)
text_4.write("4. Java ")
text_4.write("5. C++ ")
text_4.restore(saver_4.get_version(2))''',
                     test="text_4.show()",
                     answer="[Arial]1. Python 2. JavaScript 3. C# [Arial]"),

        prepare_test(middle_code='''text_5 = Text()
saver_5 = SavedText()
text_5.write("first part ")
saver_5.save_text(text_5)
text_5.write("second part ")
saver_5.save_text(text_5)
text_5.write("third part ")
saver_5.save_text(text_5)
text_5.write("fourth part ")
text_5.write("fifth part ")
text_5.restore(saver_5.get_version(0))
text_5.write("is empty")''',
                     test="text_5.show()",
                     answer="first part is empty")
    ]

}

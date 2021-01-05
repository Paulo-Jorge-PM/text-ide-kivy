## Linguistic IDE

![screenshot](print_linguistic_ide.png)

Text IDE for linguistics purposes. Objective: to create a text editor software, but focusing only in the linguistics (academic aspect), not visual aspects like the traditional ones, analyzing in real time linguistics aspects like grammar, morphology, corpora techniques, statistics, automatic translation, syntax, semantics, etc. Ideally it will have a parallel website, where academics/public can update the database and contribute with updates or new plugins. In the future I plan to migrate sobre libraries to Rust language and integrate part in Rust (faster).

The core package gives acess to NLP tools that can be used without the GUI aspect, just import the one you need and get data using their functions, e.g. for translating text from english to portuguese:

```
from core.translation import Translation
translation = Translation(lang='pt')
translated = translation.translate('Example text')
```

---

## Want to run this?

You'll need: Python 3 installed; for GUI kivy is used. The file "main.py" starts the application. The following libraries will be needed:
```
kivy (see their homepage for instalation and dependencies instructions)
pip install nltk
pip install pickle
pip install marisa-trie
pip install googletrans
pip install pyspellchecker
pip install nlpnet
pip3 install bllipparser
pip install -U textblob
```

---

## Contact me:

[http://www.paulojorgepm.net](http://www.paulojorgepm.net)

# Python Word List Tool
![Correct Horse Battery Staple](https://imgs.xkcd.com/comics/password_strength.png)

Useful for quick random phrase generation. I am using this tool for a wireless captive portal.

Figured someone else could find this tool useful too.

## Usage
```python
from pywordlist import WordList
words = WordList(count=5).get_random_words()
```
This will generate a list of `5` randomly picked words from the [EFF Short Wordlist]('https://www.eff.org/files/2016/09/08/eff_short_wordlist_2_0.txt')

`words` now has the following value:

`[u'malformed', u'goatskin', u'umpire', u'equipment', u'ardently']`

If you want a larger pool, you can switch the list like so:

```python
from pywordlist import WordList
words = WordList(count=5, word_list="https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt").get_random_words()
```
`words` now has the following value:

`[u'punctual', u'giblet', u'mayflower', u'fifth', u'angling']`

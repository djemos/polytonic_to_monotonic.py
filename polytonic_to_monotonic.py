#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  
#  Copyright 2019 Dimitris Tzemos <dijemos@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")
import re
import unicodedata

MAP={'Ἄ': 'Ά',
'Ἀ': 'Α',
'ᾈ': 'Α',
'ᾉ': 'Ά',
'ᾊ': 'Ά',
'ᾋ': 'Ά',
'ᾌ': 'Ά',
'ᾍ': 'Ά',
'ᾎ': 'Α',
'ᾏ': 'Α',
'Ὃ': 'Ό',
'Ὄ': 'Ό',
'ἁ': 'α',
'ἀ': 'α',
'ᾶ': 'α',
'ἂ': 'ά',
'ᾀ': 'ά',
'ᾁ': 'α',
'ἅ': 'ά',
'ᾃ': 'ά',
'ᾄ': 'ά',
'ἄ': 'ά',
'ἆ': 'α',
'ἇ': 'α',
'ὰ': 'ά',
'ἡ': 'η',
'ῆ': 'ή',
'ᾐ': 'η',
'ᾑ': 'η',
'ᾒ': 'η',
'ᾓ': 'ή',
'ᾔ': 'ή',
'ᾕ': 'ή',
'ᾖ': 'ή',
'ᾗ': 'ή',
'ἦ': 'ή',
'ἐ': 'ε',
'ἑ': 'ε',
'ἔ': 'έ',
'ἕ': 'έ',
'ὲ': 'έ',
'έ': 'έ',
'ἰ': 'ι',
'ἱ': 'ι',
'ὶ': 'ί',
'ἴ': 'ί',
'ἵ': 'ί',
'ἷ': 'ί',
'ἶ': 'ί',
'ῖ': 'ί',
'ὐ': 'υ',
'ὑ': 'υ',
'ὔ': 'ύ',
'ὕ': 'ύ',
'ῦ': 'ύ',
'ὖ': 'ύ',
'ὗ': 'ύ',
'ὀ': 'ο',
'ὁ': 'ο',
'ὄ': 'ό',
'ὅ': 'ό',
'ὃ': 'ό',
'ᾘ': 'Η',
'ᾙ': 'Η',
'ᾚ': 'Η',
'ᾛ': 'Η',
'Ὴ': 'Η',
'Ή': 'Η',
'ᾝ': 'Η',
'ᾞ': 'Η',
'ᾟ': 'Η',
'Ἥ': 'Η',
'Ἡ': 'H',
'ῌ': 'Η',
'ὴ': 'ή',
'ῂ': 'ή',
'ῃ': 'η',
'ῄ': 'ή',
'ῇ': 'η',
'ἤ': 'ή',
'ἥ': 'ή',
'ἣ': 'ή',
'ᾕ': 'η',
'ᾔ': 'η',
'ᾠ': 'ω',
'ῶ': 'ώ',
'ᾡ': 'ω',
'ᾢ': 'ώ',
'ᾣ': 'ώ',
'ὤ': 'ω',
'ὥ': 'ώ',
'ὣ': 'ώ',
'ᾥ': 'ώ',
'ὦ': 'ω',
'ὧ': 'ω',
'ῥ': 'ρ',
'ῤ': 'ρ',
'ᾨ': 'Ω',
'ᾩ': 'Ω',
'ᾪ': 'Ώ',
'ᾫ': 'Ώ',
'ᾬ': 'Ώ',
'Ὦ': 'Ω',
'ᾭ': 'Ώ',
'ᾮ': 'Ω',
'ᾯ': 'Ω',
'ᾲ': 'ά',
'ᾳ': 'α',
'ᾴ': 'ά',
'ᾷ': 'α',
'ἀ': 'α',
'ᾼ': 'Α',
'Ά': 'Ά',
'Ἑ': 'Ε',
'Ἐ': 'Ε',
'Ἔ': 'Έ',
'ῲ': 'ώ',
'ῳ': 'ω',
'ῴ': 'ώ',
'ῷ': 'ω',
'ὤ': 'ώ',
'ὥ': 'ώ',
'ᾥ': 'ώ',
'ᾢ': 'ώ',
'ῼ': 'Ω',
'Ἰ': 'Ι',
}
        
def convert_polytonic_to_monotonic(s):
	mono_str = []
	for c in s:
		for ch in MAP:
			if ch == c:
				c=MAP[ch]		
		mono_str.append(c)
	return ''.join(mono_str)
	
	
def main(args):
	coding1 = "utf-8"
	if len(sys.argv) >=3:
		f= open(sys.argv[1], 'rb')
		text= unicode(f.read(), coding1)
		f.close()

		f= open(sys.argv[2], 'wb')
		f.write(convert_polytonic_to_monotonic(text))
		f.close()
	else:
		#Δοκιμή
		text=unicode("Ὦ κοινὸν αὐτάδελφον Ἰσμήνης κάρα,")
		print(convert_polytonic_to_monotonic(text))
    

if __name__ == '__main__':
	sys.exit(main(sys.argv))

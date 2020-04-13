#
# IranSystem encoding for Python
# Copyright (C) 2020  Ghorban M. Tavakoly <gmt3141@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import codecs

__version__ = '0.1.0'
__email__   = 'gmt3141@gmail.com'
__doc__     = 'Iransystem encoding for Python'

### Codec APIs

class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors,decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass

### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name               = 'iransystem',
        encode             = Codec().encode,
        decode             = Codec().decode,
        incrementalencoder = IncrementalEncoder,
        incrementaldecoder = IncrementalDecoder,
        streamreader       = StreamReader,
        streamwriter       = StreamWriter
    )

### Decoding Table

# Reference: https://en.wikipedia.org/wiki/Iran_System_encoding

decoding_table = (
    # ASCII
    '\x00'     #  0x00 -> NULL
    '\x01'     #  0x01 -> START OF HEADING
    '\x02'     #  0x02 -> START OF TEXT
    '\x03'     #  0x03 -> END OF TEXT
    '\x04'     #  0x04 -> END OF TRANSMISSION
    '\x05'     #  0x05 -> ENQUIRY
    '\x06'     #  0x06 -> ACKNOWLEDGE
    '\x07'     #  0x07 -> BELL
    '\x08'     #  0x08 -> BACKSPACE
    '\t'       #  0x09 -> HORIZONTAL TABULATION
    '\n'       #  0x0A -> LINE FEED
    '\x0b'     #  0x0B -> VERTICAL TABULATION
    '\x0c'     #  0x0C -> FORM FEED
    '\r'       #  0x0D -> CARRIAGE RETURN
    '\x0e'     #  0x0E -> SHIFT OUT
    '\x0f'     #  0x0F -> SHIFT IN
    '\x10'     #  0x10 -> DATA LINK ESCAPE
    '\x11'     #  0x11 -> DEVICE CONTROL ONE
    '\x12'     #  0x12 -> DEVICE CONTROL TWO
    '\x13'     #  0x13 -> DEVICE CONTROL THREE
    '\x14'     #  0x14 -> DEVICE CONTROL FOUR
    '\x15'     #  0x15 -> NEGATIVE ACKNOWLEDGE
    '\x16'     #  0x16 -> SYNCHRONOUS IDLE
    '\x17'     #  0x17 -> END OF TRANSMISSION BLOCK
    '\x18'     #  0x18 -> CANCEL
    '\x19'     #  0x19 -> END OF MEDIUM
    '\x1a'     #  0x1A -> SUBSTITUTE
    '\x1b'     #  0x1B -> ESCAPE
    '\x1c'     #  0x1C -> FILE SEPARATOR
    '\x1d'     #  0x1D -> GROUP SEPARATOR
    '\x1e'     #  0x1E -> RECORD SEPARATOR
    '\x1f'     #  0x1F -> UNIT SEPARATOR
    ' '        #  0x20 -> SPACE
    '!'        #  0x21 -> EXCLAMATION MARK
    '"'        #  0x22 -> QUOTATION MARK
    '#'        #  0x23 -> NUMBER SIGN
    '$'        #  0x24 -> DOLLAR SIGN
    '%'        #  0x25 -> PERCENT SIGN
    '&'        #  0x26 -> AMPERSAND
    "'"        #  0x27 -> APOSTROPHE
    '('        #  0x28 -> LEFT PARENTHESIS
    ')'        #  0x29 -> RIGHT PARENTHESIS
    '*'        #  0x2A -> ASTERISK
    '+'        #  0x2B -> PLUS SIGN
    ','        #  0x2C -> COMMA
    '-'        #  0x2D -> HYPHEN-MINUS
    '.'        #  0x2E -> FULL STOP
    '/'        #  0x2F -> SOLIDUS
    '0'        #  0x30 -> DIGIT ZERO
    '1'        #  0x31 -> DIGIT ONE
    '2'        #  0x32 -> DIGIT TWO
    '3'        #  0x33 -> DIGIT THREE
    '4'        #  0x34 -> DIGIT FOUR
    '5'        #  0x35 -> DIGIT FIVE
    '6'        #  0x36 -> DIGIT SIX
    '7'        #  0x37 -> DIGIT SEVEN
    '8'        #  0x38 -> DIGIT EIGHT
    '9'        #  0x39 -> DIGIT NINE
    ':'        #  0x3A -> COLON
    ';'        #  0x3B -> SEMICOLON
    '<'        #  0x3C -> LESS-THAN SIGN
    '='        #  0x3D -> EQUALS SIGN
    '>'        #  0x3E -> GREATER-THAN SIGN
    '?'        #  0x3F -> QUESTION MARK
    '@'        #  0x40 -> COMMERCIAL AT
    'A'        #  0x41 -> LATIN CAPITAL LETTER A
    'B'        #  0x42 -> LATIN CAPITAL LETTER B
    'C'        #  0x43 -> LATIN CAPITAL LETTER C
    'D'        #  0x44 -> LATIN CAPITAL LETTER D
    'E'        #  0x45 -> LATIN CAPITAL LETTER E
    'F'        #  0x46 -> LATIN CAPITAL LETTER F
    'G'        #  0x47 -> LATIN CAPITAL LETTER G
    'H'        #  0x48 -> LATIN CAPITAL LETTER H
    'I'        #  0x49 -> LATIN CAPITAL LETTER I
    'J'        #  0x4A -> LATIN CAPITAL LETTER J
    'K'        #  0x4B -> LATIN CAPITAL LETTER K
    'L'        #  0x4C -> LATIN CAPITAL LETTER L
    'M'        #  0x4D -> LATIN CAPITAL LETTER M
    'N'        #  0x4E -> LATIN CAPITAL LETTER N
    'O'        #  0x4F -> LATIN CAPITAL LETTER O
    'P'        #  0x50 -> LATIN CAPITAL LETTER P
    'Q'        #  0x51 -> LATIN CAPITAL LETTER Q
    'R'        #  0x52 -> LATIN CAPITAL LETTER R
    'S'        #  0x53 -> LATIN CAPITAL LETTER S
    'T'        #  0x54 -> LATIN CAPITAL LETTER T
    'U'        #  0x55 -> LATIN CAPITAL LETTER U
    'V'        #  0x56 -> LATIN CAPITAL LETTER V
    'W'        #  0x57 -> LATIN CAPITAL LETTER W
    'X'        #  0x58 -> LATIN CAPITAL LETTER X
    'Y'        #  0x59 -> LATIN CAPITAL LETTER Y
    'Z'        #  0x5A -> LATIN CAPITAL LETTER Z
    '['        #  0x5B -> LEFT SQUARE BRACKET
    '\\'       #  0x5C -> REVERSE SOLIDUS
    ']'        #  0x5D -> RIGHT SQUARE BRACKET
    '^'        #  0x5E -> CIRCUMFLEX ACCENT
    '_'        #  0x5F -> LOW LINE
    '`'        #  0x60 -> GRAVE ACCENT
    'a'        #  0x61 -> LATIN SMALL LETTER A
    'b'        #  0x62 -> LATIN SMALL LETTER B
    'c'        #  0x63 -> LATIN SMALL LETTER C
    'd'        #  0x64 -> LATIN SMALL LETTER D
    'e'        #  0x65 -> LATIN SMALL LETTER E
    'f'        #  0x66 -> LATIN SMALL LETTER F
    'g'        #  0x67 -> LATIN SMALL LETTER G
    'h'        #  0x68 -> LATIN SMALL LETTER H
    'i'        #  0x69 -> LATIN SMALL LETTER I
    'j'        #  0x6A -> LATIN SMALL LETTER J
    'k'        #  0x6B -> LATIN SMALL LETTER K
    'l'        #  0x6C -> LATIN SMALL LETTER L
    'm'        #  0x6D -> LATIN SMALL LETTER M
    'n'        #  0x6E -> LATIN SMALL LETTER N
    'o'        #  0x6F -> LATIN SMALL LETTER O
    'p'        #  0x70 -> LATIN SMALL LETTER P
    'q'        #  0x71 -> LATIN SMALL LETTER Q
    'r'        #  0x72 -> LATIN SMALL LETTER R
    's'        #  0x73 -> LATIN SMALL LETTER S
    't'        #  0x74 -> LATIN SMALL LETTER T
    'u'        #  0x75 -> LATIN SMALL LETTER U
    'v'        #  0x76 -> LATIN SMALL LETTER V
    'w'        #  0x77 -> LATIN SMALL LETTER W
    'x'        #  0x78 -> LATIN SMALL LETTER X
    'y'        #  0x79 -> LATIN SMALL LETTER Y
    'z'        #  0x7A -> LATIN SMALL LETTER Z
    '{'        #  0x7B -> LEFT CURLY BRACKET
    '|'        #  0x7C -> VERTICAL LINE
    '}'        #  0x7D -> RIGHT CURLY BRACKET
    '~'        #  0x7E -> TILDE
    '\x7f'     #  0x7F -> DELETE
    '\u06f0'   #  0x80 -> EXTENDED ARABIC-INDIC DIGIT ZERO
    '\u06f1'   #  0x81 -> EXTENDED ARABIC-INDIC DIGIT ONE
    '\u06f2'   #  0x82 -> EXTENDED ARABIC-INDIC DIGIT TWO
    '\u06f3'   #  0x83 -> EXTENDED ARABIC-INDIC DIGIT THREE
    '\u06f4'   #  0x84 -> EXTENDED ARABIC-INDIC DIGIT FOUR
    '\u06f5'   #  0x85 -> EXTENDED ARABIC-INDIC DIGIT FIVE
    '\u06f6'   #  0x86 -> EXTENDED ARABIC-INDIC DIGIT SIX
    '\u06f7'   #  0x87 -> EXTENDED ARABIC-INDIC DIGIT SEVEN
    '\u06f8'   #  0x88 -> EXTENDED ARABIC-INDIC DIGIT EIGHT
    '\u06f9'   #  0x89 -> EXTENDED ARABIC-INDIC DIGIT NINE
    '\u060c'   #  0x8a -> ARABIC COMMA
    '\u0640'   #  0x8b -> ARABIC TATWEEL
    '\u061f'   #  0x8c -> ARABIC QUESTION MARK
    '\u0622'   #  0x8d -> ARABIC LETTER ALEF WITH MADDA ABOVE
    '\u0626'   #  0x8e -> ARABIC LETTER YEH WITH HAMZA ABOVE
    '\u0621'   #  0x8f -> ARABIC LETTER HAMZA
    '\u0627'   #  0x90 -> ARABIC LETTER ALEF
    '\u0627'   #  0x91 -> ARABIC LETTER ALEF
    '\u0628'   #  0x92 -> ARABIC LETTER BEH
    '\u0628'   #  0x93 -> ARABIC LETTER BEH
    '\u067e'   #  0x94 -> ARABIC LETTER PEH
    '\u067e'   #  0x95 -> ARABIC LETTER PEH
    '\u062a'   #  0x96 -> ARABIC LETTER TEH
    '\u062a'   #  0x97 -> ARABIC LETTER TEH
    '\u062b'   #  0x98 -> ARABIC LETTER THEH
    '\u062b'   #  0x99 -> ARABIC LETTER THEH
    '\u062c'   #  0x9a -> ARABIC LETTER JEEM
    '\u062c'   #  0x9b -> ARABIC LETTER JEEM
    '\u0686'   #  0x9c -> ARABIC LETTER TCHEH
    '\u0686'   #  0x9d -> ARABIC LETTER TCHEH
    '\u062d'   #  0x9e -> ARABIC LETTER HAH
    '\u062d'   #  0x9f -> ARABIC LETTER HAH
    '\u062e'   #  0xa0 -> ARABIC LETTER KHAH
    '\u062e'   #  0xa1 -> ARABIC LETTER KHAH
    '\u062f'   #  0xa2 -> ARABIC LETTER DAL
    '\u0630'   #  0xa3 -> ARABIC LETTER THAL
    '\u0631'   #  0xa4 -> ARABIC LETTER REH
    '\u0632'   #  0xa5 -> ARABIC LETTER ZAIN
    '\u0698'   #  0xa6 -> ARABIC LETTER JEH
    '\u0633'   #  0xa7 -> ARABIC LETTER SEEN
    '\u0633'   #  0xa8 -> ARABIC LETTER SEEN
    '\u0634'   #  0xa9 -> ARABIC LETTER SHEEN
    '\u0634'   #  0xaa -> ARABIC LETTER SHEEN
    '\u0635'   #  0xab -> ARABIC LETTER SAD
    '\u0635'   #  0xac -> ARABIC LETTER SAD
    '\u0636'   #  0xad -> ARABIC LETTER DAD
    '\u0636'   #  0xae -> ARABIC LETTER DAD
    '\u0637'   #  0xaf -> ARABIC LETTER TAH
    '\u2591'   #  0xb0 -> LIGHT SHADE
    '\u2592'   #  0xb1 -> MEDIUM SHADE
    '\u2593'   #  0xb2 -> DARK SHADE
    '\u2502'   #  0xb3 -> BOX DRAWINGS LIGHT VERTICAL
    '\u2524'   #  0xb4 -> BOX DRAWINGS LIGHT VERTICAL AND LEFT
    '\u2561'   #  0xb5 -> BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE
    '\u2562'   #  0xb6 -> BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE
    '\u2556'   #  0xb7 -> BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE
    '\u2555'   #  0xb8 -> BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE
    '\u2563'   #  0xb9 -> BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    '\u2551'   #  0xba -> BOX DRAWINGS DOUBLE VERTICAL
    '\u2557'   #  0xbb -> BOX DRAWINGS DOUBLE DOWN AND LEFT
    '\u255d'   #  0xbc -> BOX DRAWINGS DOUBLE UP AND LEFT
    '\u255c'   #  0xbd -> BOX DRAWINGS UP DOUBLE AND LEFT SINGLE
    '\u255b'   #  0xbe -> BOX DRAWINGS UP SINGLE AND LEFT DOUBLE
    '\u2510'   #  0xbf -> BOX DRAWINGS LIGHT DOWN AND LEFT
    '\u2514'   #  0xc0 -> BOX DRAWINGS LIGHT UP AND RIGHT
    '\u2534'   #  0xc1 -> BOX DRAWINGS LIGHT UP AND HORIZONTAL
    '\u252c'   #  0xc2 -> BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    '\u251c'   #  0xc3 -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    '\u2500'   #  0xc4 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\u253c'   #  0xc5 -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    '\u255e'   #  0xc6 -> BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE
    '\u255f'   #  0xc7 -> BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE
    '\u255a'   #  0xc8 -> BOX DRAWINGS DOUBLE UP AND RIGHT
    '\u2554'   #  0xc9 -> BOX DRAWINGS DOUBLE DOWN AND RIGHT
    '\u2569'   #  0xca -> BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    '\u2566'   #  0xcb -> BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    '\u2560'   #  0xcc -> BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    '\u2550'   #  0xcd -> BOX DRAWINGS DOUBLE HORIZONTAL
    '\u256c'   #  0xce -> BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    '\u2567'   #  0xcf -> BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE
    '\u2568'   #  0xd0 -> BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE
    '\u2564'   #  0xd1 -> BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE
    '\u2565'   #  0xd2 -> BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE
    '\u2559'   #  0xd3 -> BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE
    '\u2558'   #  0xd4 -> BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE
    '\u2552'   #  0xd5 -> BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE
    '\u2553'   #  0xd6 -> BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE
    '\u256b'   #  0xd7 -> BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE
    '\u256a'   #  0xd8 -> BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE
    '\u2518'   #  0xd9 -> BOX DRAWINGS LIGHT UP AND LEFT
    '\u250c'   #  0xda -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    '\u2588'   #  0xdb -> FULL BLOCK
    '\u2584'   #  0xdc -> LOWER HALF BLOCK
    '\u258c'   #  0xdd -> LEFT HALF BLOCK
    '\u2590'   #  0xde -> RIGHT HALF BLOCK
    '\u2580'   #  0xdf -> UPPER HALF BLOCK
    '\u0638'   #  0xe0 -> ARABIC LETTER ZAH
    '\u0639'   #  0xe1 -> ARABIC LETTER AIN
    '\u0639'   #  0xe2 -> ARABIC LETTER AIN
    '\u0639'   #  0xe3 -> ARABIC LETTER AIN
    '\u0639'   #  0xe4 -> ARABIC LETTER AIN
    '\u063a'   #  0xe5 -> ARABIC LETTER GHAIN
    '\u063a'   #  0xe6 -> ARABIC LETTER GHAIN
    '\u063a'   #  0xe7 -> ARABIC LETTER GHAIN
    '\u063a'   #  0xe8 -> ARABIC LETTER GHAIN
    '\u0641'   #  0xe9 -> ARABIC LETTER FEH
    '\u0641'   #  0xea -> ARABIC LETTER FEH
    '\u0642'   #  0xeb -> ARABIC LETTER QAF
    '\u0642'   #  0xec -> ARABIC LETTER QAF
    '\u06a9'   #  0xed -> ARABIC LETTER KEHEH
    '\u0643'   #  0xee -> ARABIC LETTER KEHEH
    '\u06af'   #  0xef -> ARABIC LETTER GAF
    '\u06af'   #  0xf0 -> ARABIC LETTER GAF
    '\u0644'   #  0xf1 -> ARABIC LETTER LAM
    # this has problems in non-isolated forms!
    '\ufefb'   #  0xf2 -> ARABIC LIGATURE LAM WITH ALEF ISOLATED FORM
    '\u0644'   #  0xf3 -> ARABIC LETTER LAM
    '\u0645'   #  0xf4 -> ARABIC LETTER MEEM
    '\u0645'   #  0xf5 -> ARABIC LETTER MEEM
    '\u0646'   #  0xf6 -> ARABIC LETTER NOON
    '\u0646'   #  0xf7 -> ARABIC LETTER NOON
    '\u0648'   #  0xf8 -> ARABIC LETTER WAW
    '\u0647'   #  0xf9 -> ARABIC LETTER HEH
    '\u0647'   #  0xfa -> ARABIC LETTER HEH
    '\u0647'   #  0xfb -> ARABIC LETTER HEH
    '\u06cc'   #  0xfc -> ARABIC LETTER FARSI YEH
    '\u06cc'   #  0xfd -> ARABIC LETTER FARSI YEH
    '\u064a'   #  0xfe -> ARABIC LETTER FARSI YEH
    '\xa0'     #  0xff -> NO-BREAK SPACE
)

### Encoding table
encoding_table = codecs.charmap_build(decoding_table)

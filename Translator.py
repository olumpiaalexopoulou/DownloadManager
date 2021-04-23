# Replacing greek characters with english ones
def trans(phrase):
    translation = ""
    for i in phrase:
        if i in "αΑάΆ":
            translation = translation+"a"
        elif i in "βΒ":
            translation = translation+"b"

        elif i in 'γΓ':
            translation = translation+"g"

        elif i in 'δΔ':
            translation = translation+"d"

        elif i in 'εέΕΈ':
            translation = translation+"e"

        elif i in 'ζΖ':
            translation = translation+"z"

        elif i in 'ηήΗΉ':
            translation = translation+"h"

        elif i in 'θΘ':
            translation = translation+"th"

        elif i in 'ιίΙΊϊΐ':
            translation = translation+"i"

        elif i in 'κΚ':
            translation = translation+"k"

        elif i in 'λΛ':
            translation = translation+"l"

        elif i in 'μΜ':
            translation = translation+"m"

        elif i in 'νΝ':
            translation = translation+"n"

        elif i in 'ξΞ':
            translation = translation+"ks"

        elif i in 'οόΟΌωΩώΏ':
            translation = translation+"o"

        elif i in 'πΠ':
            translation = translation+"p"

        elif i in 'ρΡ':
            translation = translation+"r"

        elif i in 'σΣς':
            translation = translation+"s"

        elif i in 'τΤ':
            translation = translation+"t"

        elif i in 'υύΥΎ':
            translation = translation+"u"

        elif i in 'φΦ':
            translation = translation+"f"

        elif i in 'χΧ':
            translation = translation+"x"

        elif i in 'ψΨ':
            translation = translation+"ps"

        elif i in ' ':
            translation = translation+" "

        else:
            translation = translation+i
    return translation

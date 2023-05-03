l := "a"
r := "d"
u := "w"
d := "s"
block := "Space"
fp := "Numpad8"
bp := "Numpad9"
fk := "Numpad5"
bk := "Numpad6"
SetKeyDelay, 30, 30
+bp::
        if GetKeyState(%l%)
          Send, {%l% up}
          b := r
          f := l
        else
          Send, {%r% up}
          b := l
          f := r
        Send, %b%
    Send, {%f% down}{%fk% down}{%fk% up}{%f% up}
    return
l := "a"
r := "d"
u := "w"
d := "s"
block := "Space"
fp := "Numpad8"
bp := "Numpad9"
fk := "Numpad5"
bk := "Numpad6"
SetKeyDelay, 30, 30
^fk::
        if GetKeyState(%l%)
          Send, {%l% up}
          b := r
          f := l
        else
          Send, {%r% up}
          b := l
          f := r
        Send, %f%
    Send, {%f% down}{%fp% down}{%fp% up}{%f% up}
    return

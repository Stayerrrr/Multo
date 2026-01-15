import sys
import time

def run_lyrics():
    lyric = [
        ("Hindi na makalaya", 0.19),
        ("Dinadalaw mo 'ko bawat gabi", 0.12),
        ("Wala mang nakikita", 0.19),
        ("Haplos mo'y ramdam pa rin sa dilim", 0.1),
        ("Hindi na nananaginip", 0.19),
        ("Hindi na ma-makagising", 0.16),
        ("Pasindi na ng ilaw", 0.2),
        ("Minumulto na 'ko ng damdamin ko", 0.1),
        ("Ng damdamin ko", 0.12),
        ("Hindi mo ba ako lilisanin?", 0.15),
        ("Hindi pa ba sapat pagpapahirap sa 'kin? (Damdamin ko)", 0.08),
        ("Hindi na ba ma-mamamayapa?", 0.14),
        ("Hindi na ba ma-mamamayapa?", 0.14)
    ]
    
    line_delays = [1, 1.5, 1, 1.3, 1, 1, 1, 0.6, 0.1, 0.9, 0.6, 0.6, 0.6]

    print("\nMulto - Cup of Joe \n")
    time.sleep(2)

    for i, (line, char_delay) in enumerate(lyric):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(char_delay)
        time.sleep(line_delays[i])
        print()

    print("\n Code by San-Z")

run_lyrics()

# -*- coding: utf-8 -*-

import os
import itertools

day_labels = [':santa:', ':star2:', ':snowflake:', ':snowman:', ':sparkles:',
              ':fire:', ':christmas_tree:', ':gift:', ':bell:', ':tada:']

folders = [
    (10, 'Day1-9'),
    (20, 'Day10-19'),
    (26, 'Day20-25')
]

extensions = {
    'py': 'Python',
    's': 'MIPS',
    'hs': 'Haskell',
    'cpp': 'C++',
    'c': 'C',
    'rb': 'Ruby'
}

if __name__ == '__main__':
    out = ""
    soln_temp = "    * [{}]({})\n"
    symbols = itertools.cycle(list(day_labels))
    for i in range(1, 26):
        fdr = next(x[1] for x in folders if x[0] > i)
        temp = "* Day {}:  {}\n".format(i, next(symbols))
        sol_for_today = False
        for fn in os.listdir(fdr):
            try:
                name, ext = fn.split('.')
                day = int(name)
            except ValueError:
                pass
                # print("Coundn't parse: %s" % fn)
            else:
                if ext in extensions and day == i:
                    full = os.path.join(fdr, fn)
                    temp += soln_temp.format(extensions[ext], full)
                    sol_for_today = True
        if sol_for_today:
            out += temp
    print out

"""
Uno: A clone of the cardgame UNO (C)
Copyright (C) 2011  Alexander Thaller <alex.t@gmx.at>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from colorama import Fore, Back, Style

BLUE = 0
GREEN = 1
RED = 2
YELLOW = 3
BLACK = 4 #Special Card

def toString(color):
    if color == 0:
        return Back.WHITE + Fore.BLUE + Style.BRIGHT + 'Blue'
    elif color == 1:
        return Back.WHITE + Fore.GREEN + Style.BRIGHT + 'Green'
    elif color == 2:
        return Back.WHITE + Fore.RED + Style.BRIGHT + 'Red'
    elif color == 3:
        return Back.WHITE + Fore.YELLOW + Style.BRIGHT + 'Yellow'
    elif color == 4:
        return Back.WHITE + Fore.BLACK + Style.DIM +'Black' 

if __name__ == '__main__':
    assert toString(BLUE) == 'Blue'
    assert toString(GREEN) == 'Green'
    assert toString(RED) == 'Red'
    assert toString(YELLOW) == 'Yellow'
    assert toString(BLACK) == 'Black'
    
        
    

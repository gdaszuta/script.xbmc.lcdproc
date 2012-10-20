'''
    XBMC LCDproc addon
    Copyright (C) 2012 Team XBMC

    Support for extra symbols on SoundGraph iMON LCD displays
    Copyright (C) 2012 Daniel Scheller
    Original C implementation (C) 2010 theonlychrizz

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
'''

import sys

__scriptname__ = sys.modules[ "__main__" ].__scriptname__
__settings__ = sys.modules[ "__main__" ].__settings__
__cwd__ = sys.modules[ "__main__" ].__cwd__
__icon__ = sys.modules[ "__main__" ].__icon__

class LCDproc_extra_base():
  def __init__(self):
    pass

# @abstractmethod
  def Initialize(self):
    pass

# @abstractmethod
  def SetOutputIcons(self):
    pass

# @abstractmethod
  def SetOutputBars(self):
    pass

# @abstractmethod
  def SetIconState(self, icon, state):
    pass


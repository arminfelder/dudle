#!/usr/bin/env ruby

############################################################################
# Copyright 2009,2010 Benjamin Kellermann                                  #
#                                                                          #
# This file is part of dudle.                                              #
#                                                                          #
# Dudle is free software: you can redistribute it and/or modify it under   #
# the terms of the GNU Affero General Public License as published by       #
# the Free Software Foundation, either version 3 of the License, or        #
# (at your option) any later version.                                      #
#                                                                          #
# Dudle is distributed in the hope that it will be useful, but WITHOUT ANY #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public     #
# License for more details.                                                #
#                                                                          #
# You should have received a copy of the GNU Affero General Public License #
# along with dudle.  If not, see <http://www.gnu.org/licenses/>.           #
############################################################################

if __FILE__ == $0

require "dudle"

$d = Dudle.new

$d << "<div>" + _("If you find a bug or have something else, which disturbes you, please let me know:")
$d << '<a href="mailto:Benjamin_dot_Kellermann@tu-dresden_in_germany?subject=Feedback%20to%20dudle">' + _("give feedback") + "</a></div>"
$d << "<div><h2>" + _("--verbose") + "</h2>"
$d << _("The sourcecode of this application is available under the terms of")
$d << "<a href='http://www.fsf.org/licensing/licenses/agpl-3.0.html'>" + _("AGPL Version 3") + "</a>"
$d << "<br />"
$d << _("You can get the code, using") + ' <a href="http://bazaar-vcs.org/">bazaar</a>:'
$d << "<pre>bzr branch #{SITEURL} dudle</pre></div>"


$d.out
end


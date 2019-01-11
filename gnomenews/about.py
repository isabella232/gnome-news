# Copyright (C) 2015 Igor Gnatenko <ignatenko@src.gnome.org>
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk

AUTHORS = [
    "Felipe Borges",
    "Michael Catanzaro",
    "Carlos Garnacho",
    "Igor Gnatenko",
    "Patrick Grififis",
    "Yosef Or Boczko",
    "Vadim Rutkovsky",
]

ARTISTS = [
    "Allan Day"
]


class AboutDialog(Gtk.AboutDialog):
    def __init__(self, parent, version):
        Gtk.AboutDialog.__init__(self)
        self.parent = parent
        self.set_modal(True)
        self.set_transient_for(parent)
        self.set_artists(ARTISTS)
        self.set_authors(AUTHORS)
        self.set_copyright("Copyright © 2015 GNOME Foundation")
        self.set_license_type(Gtk.License.GPL_3_0)
        self.set_version(version)
        self.set_website("https://wiki.gnome.org/Design/Apps/Potential/News")
        self.set_logo_icon_name("gnome-news")

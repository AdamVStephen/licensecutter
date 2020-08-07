"""
License Cookiecutter Main module.

Requirements

1. Given a license text, create versions in various language comment syntax that can be dropped into cookiecutter files.
2. Utilities to help build a license from standard clauses and metadata.

Motivation

The open source real-time control framework MARTe and the successor MARTe2 have adopted a project standard that includes
header license data in many files (Makefiles, C++ headers and sources).  To conform to this pattern needs some support.

Side benefits : this is my first public python project with bells and whistles of CI, online documentation, yadayada.

Research

Need to also look at wider standards for best practice with regard to this.  It seems more sensible to limit the LICENSE definition
to the root of the project, and at most, ensure every file in the project point to this LICENSE.

TODO
- Bring code to PEP8 standards.
"""

import os
import pdb
import pkg_resources

class CommentStyle:
    def __init__(self, character = "-", header = None, footer = None):
        self.character = character
        if header is not None:
            self.header = header
        else:
            self.header = character
        if footer is not None:
            self.footer = footer
        else:
            self.footer = character

class DashCommentStyle(CommentStyle):
    pass

class BashCommentStyle(CommentStyle):
    def __init__(self):
        CommentStyle.__init__(self, "# ", header = "#", footer = "")

class CCommentStyle(CommentStyle):
    def __init__(self):
        CommentStyle.__init__(self, " * ", header = "/*", footer = "\n */")

class CppCommentStyle(CommentStyle):
    def __init__(self):
        CommentStyle.__init__(self, "// ", header = "// ", footer = "")

standard_licenses = {
    "MIT" : "data/MIT.license"
}

class LicenseWrapper:

    nil_license = "No license."
    
    def __init__(self,
                 license_name = None,
                 license_file = None,
                 license_text = None,
                 commentstyle = BashCommentStyle()):
        self.license_name = license_name
        self.license_file = license_file
        self.license_text = license_text
        self.commentstyle = commentstyle
        self.body = None
        if license_name is not None:
            self.load_from_data()
        if license_file is not None:
            self.load_from_path()
        if license_text is not None:
            self.load_from_text()
        if self.body is None:
            self.body = self.nil_license

    def load_from_data(self):
        if self.license_name in standard_licenses:
            license_data_file = standard_licenses[self.license_name]
            with pkg_resources.resource_stream(__name__, license_data_file) as stream:
                self.body = stream.read().decode("utf-8")

    def load_from_path(self):
        if os.path.exists(self.license_file):
            with open(self.license_file, 'r') as fh:
                self.body = fh.read()

    def load_from_text(self):
        self.body = self.license_text

    def __repr__(self):
        r = [self.commentstyle.header]
        r.extend(self.body.split('\n'))
        r.append(self.commentstyle.footer)
        suffix = "\n%s" % self.commentstyle.character
        return suffix.join(r)

if __name__ == '__main__':
    pass





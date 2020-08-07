#!/usr/bin/env python

"""Tests for `licensecutter` package."""

import pytest

#from licensecutter import licensecutter.*
from licensecutter.licensecutter import *

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

class TestCommentStyle:

    def test_default_ctor(self):
        cs = CommentStyle()
        assert(cs.header == cs.footer == cs.character == "-")

    def test_bash(self):
        cs = BashCommentStyle()
        assert(cs.header is not None)
        assert(cs.footer is not None)

    def test_C(self):
        cs = CCommentStyle()
        assert(cs.header is not None)
        assert(cs.footer is not None)

    def test_Cpp(self):
        cs = CppCommentStyle()
        assert(cs.header is not None)
        assert(cs.footer is not None)

class TestLicenseWrapper:

    def test_default_ctor(self):
        lw = LicenseWrapper()
        assert(lw.body == lw.nil_license)

    def test_text_ctor(self):
        license_text = """Test License.
Comprising Multiple Lines.
Caveat: this is not really a license at all."""
        lw = LicenseWrapper(license_text = license_text)
        assert(lw.body == license_text)

    def test_text_path(self):
        existing_license_path = 'licensecutter/data/MIT.license'
        nosuch_license_path = 'foo/bar.license'
        lw = LicenseWrapper(license_file = existing_license_path)
        assert(lw.body != lw.nil_license)
        lw = LicenseWrapper(license_file = nosuch_license_path)
        assert(lw.body == lw.nil_license)

    def test_data(self):
        lw = LicenseWrapper(license_name = "MIT")
        assert(lw.body != lw.nil_license)
        lw = LicenseWrapper(license_name = "UnknownLicense")
        assert(lw.body == lw.nil_license)

    def test_repr(self):
        for style in [CCommentStyle(), BashCommentStyle(), CppCommentStyle()]:
            lw = LicenseWrapper(commentstyle = style)
            print("-"*50+"\n"+"%s" % lw + "\n" + "-"*50 + "\n")
            lw = LicenseWrapper(license_text = "Inline license", commentstyle = style)
            print("-"*50+"\n"+"%s" % lw + "\n" + "-"*50 + "\n")
            lw = LicenseWrapper(license_file = 'licensecutter/data/MIT.license', commentstyle = style)
            print("-"*50+"\n"+"%s" % lw + "\n" + "-"*50 + "\n")
            lw = LicenseWrapper(license_name = "MIT", commentstyle = style)
            print("-"*50+"\n"+"%s" % lw + "\n" + "-"*50 + "\n")
        
    
        
        
        



# The Web Site

Scrape of all MIBs taken from http://mibs.snmplabs.com/asn1/, as of 01/31/2020.

Created with a recursive wget command.

This repo only exists because those sources don't seem to be in github.

All original MIB files are in the 'asn1' directory.

All compiled MIB .py files are in the 'pysnmp' directory.

The new site is now at https://mibs.pysnmp.com/asn1/

# Instructions

```
# Create the Python environment
pipenv shell
pipenv install

# Fetching all mibs
make fetch

# Compiling all mibs
make compile
make compile-json
make compile-with-texts

# Compiling mibs only updated and just added
make compile-changed
make compile-json-changed
make compile-with-texts-changed
```

# Issue Reports
Please report any issues to https://github.com/lextudio/pysnmp/issues

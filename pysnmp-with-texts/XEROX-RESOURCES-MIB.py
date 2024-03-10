"""SNMP MIB module (XEROX-RESOURCES-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-RESOURCES-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:23 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(hrDeviceIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex")

(IANACharset,) = mibBuilder.importSymbols(
    "IANA-CHARSET-MIB",
    "IANACharset")

(ObjectGroup,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ObjectGroup",
    "ModuleCompliance",
    "NotificationGroup")

(NotificationType,
 TimeTicks,
 Unsigned32,
 Counter32,
 IpAddress,
 iso,
 Counter64,
 ObjectIdentity,
 Gauge32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Integer32,
 ModuleIdentity,
 MibIdentifier,
 Bits) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "Counter32",
    "IpAddress",
    "iso",
    "Counter64",
    "ObjectIdentity",
    "Gauge32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Integer32",
    "ModuleIdentity",
    "MibIdentifier",
    "Bits")

(DisplayString,
 TextualConvention,
 RowStatus) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "RowStatus")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(Ordinal32,
 Integer64Low,
 Integer64High,
 Cardinal32,
 CodeIndexedStringIndex) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Ordinal32",
    "Integer64Low",
    "Integer64High",
    "Cardinal32",
    "CodeIndexedStringIndex")

(XcmPrtInterpreterLangFamily,) = mibBuilder.importSymbols(
    "XEROX-PRINTER-EXT-TC",
    "XcmPrtInterpreterLangFamily")

(XcmRsrcGroupSupport,
 XcmFontSpacing,
 XcmFontType,
 XcmRsrcPersistence,
 XcmFontPCLStyle,
 XcmRsrcType,
 XcmFontPCLStrokeWeight) = mibBuilder.importSymbols(
    "XEROX-RESOURCES-TC",
    "XcmRsrcGroupSupport",
    "XcmFontSpacing",
    "XcmFontType",
    "XcmRsrcPersistence",
    "XcmFontPCLStyle",
    "XcmRsrcType",
    "XcmFontPCLStrokeWeight")


# MODULE-IDENTITY

xcmRsrcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57)
)
xcmRsrcMIB.setLastUpdated("0210310000Z")
if mibBuilder.loadTexts:
    xcmRsrcMIB.setOrganization("""\
Xerox Corporation - Xerox Common Management Interface (XCMI) Working Group
""")
xcmRsrcMIB.setContactInfo("""\
 XCMI Editors E-Mail: coherence@crt.xerox.com -- --
""")
if mibBuilder.loadTexts:
    xcmRsrcMIB.setDescription("""\
 XCMI Document Resources MIB, Version 5.12.pub. Copyright (C) 1997-2002 Xerox
Corporation. All Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmRsrcGeneral_ObjectIdentity = ObjectIdentity
xcmRsrcGeneral = _XcmRsrcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1)
)
_XcmRsrcGeneralTable_Object = MibTable
xcmRsrcGeneralTable = _XcmRsrcGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1)
)
if mibBuilder.loadTexts:
    xcmRsrcGeneralTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralTable.setDescription("""\
A table of general counters and summary information for ease of use of the
overall Document Resources MIB on this host system. This Document Resources
General table has exactly one row, with an xcmRsrcGeneralIndex value of 1.
""")
_XcmRsrcGeneralEntry_Object = MibTableRow
xcmRsrcGeneralEntry = _XcmRsrcGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1)
)
xcmRsrcGeneralEntry.setIndexNames(
    (0, "XEROX-RESOURCES-MIB", "xcmRsrcGeneralIndex"),
)
if mibBuilder.loadTexts:
    xcmRsrcGeneralEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralEntry.setDescription("""\
A row entry of general counters and summary information for ease of use of the
overall Document Resources MIB on this host system. The Document Resources
General table has exactly one row entry, with an xcmRsrcGeneralIndex value of
1.
""")
_XcmRsrcGeneralIndex_Type = Ordinal32
_XcmRsrcGeneralIndex_Object = MibTableColumn
xcmRsrcGeneralIndex = _XcmRsrcGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 1),
    _XcmRsrcGeneralIndex_Type()
)
xcmRsrcGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmRsrcGeneralIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralIndex.setDescription("""\
An identifier of this conceptual row in the xcmRsrcGeneralTable. The
xcmRsrcGeneralTable has exactly one row, with an xcmRsrcGeneralIndex value of
1.
""")
_XcmRsrcGeneralRowStatus_Type = RowStatus
_XcmRsrcGeneralRowStatus_Object = MibTableColumn
xcmRsrcGeneralRowStatus = _XcmRsrcGeneralRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 2),
    _XcmRsrcGeneralRowStatus_Type()
)
xcmRsrcGeneralRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralRowStatus.setDescription("""\
Displays the status of this conceptual row in the xcmRsrcGeneralTable. The
xcmRsrcGeneralTable has exactly one row, with an xcmRsrcGeneralIndex value of
1.
""")


class _XcmRsrcGeneralGroupSupport_Type(XcmRsrcGroupSupport):
    """Custom type xcmRsrcGeneralGroupSupport based on XcmRsrcGroupSupport"""
    defaultValue = 2


_XcmRsrcGeneralGroupSupport_Object = MibTableColumn
xcmRsrcGeneralGroupSupport = _XcmRsrcGeneralGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 3),
    _XcmRsrcGeneralGroupSupport_Type()
)
xcmRsrcGeneralGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralGroupSupport.setDescription("""\
Indicates which object groups of the Document Resources MIB are supported by
this host system, specified in a bit-mask.
""")
_XcmRsrcGeneralCreateSupport_Type = XcmRsrcGroupSupport
_XcmRsrcGeneralCreateSupport_Object = MibTableColumn
xcmRsrcGeneralCreateSupport = _XcmRsrcGeneralCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 4),
    _XcmRsrcGeneralCreateSupport_Type()
)
xcmRsrcGeneralCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralCreateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralCreateSupport.setDescription("""\
Indicates which object groups of the Document Resources MIB are supported by
this host system for dynamic row creation (via '...RowStatus'), specified in a
bit-mask.
""")
_XcmRsrcGeneralUpdateSupport_Type = XcmRsrcGroupSupport
_XcmRsrcGeneralUpdateSupport_Object = MibTableColumn
xcmRsrcGeneralUpdateSupport = _XcmRsrcGeneralUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 5),
    _XcmRsrcGeneralUpdateSupport_Type()
)
xcmRsrcGeneralUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralUpdateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralUpdateSupport.setDescription("""\
Indicates which object groups of the Document Resources MIB are supported by
this host system for existing row update (via SNMP Set-Request PDUs), specified
in a bit-mask.
""")


class _XcmRsrcGeneralRsrcTypeAccept_Type(OctetString):
    """Custom type xcmRsrcGeneralRsrcTypeAccept based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XcmRsrcGeneralRsrcTypeAccept_Type.__name__ = "OctetString"
_XcmRsrcGeneralRsrcTypeAccept_Object = MibTableColumn
xcmRsrcGeneralRsrcTypeAccept = _XcmRsrcGeneralRsrcTypeAccept_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 6),
    _XcmRsrcGeneralRsrcTypeAccept_Type()
)
xcmRsrcGeneralRsrcTypeAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralRsrcTypeAccept.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralRsrcTypeAccept.setReference("""\
See: 'XcmRsrcType' in XCMI Document Resources TC; 'hrPrinterDetectedErrorState'
in IETF Host Resources MIB (RFC 1514/2790); Section 7.1.4 'The BITS construct'
in IETF SMIv2 (RFC 2578); Section 8 'Serialization using the BER' in IETF
Transport Mappings for SNMPv2 (RFC 1908).
""")
if mibBuilder.loadTexts:
    xcmRsrcGeneralRsrcTypeAccept.setDescription("""\
Indicates all of the document resource types which are accepted for dynamic
delivery to and use by this host system, specified in a bit-array. Usage: This
bit-array is constructed from the set of supported values from 'XcmRsrcType',
used as powers of 2 with big-endian rules - the high-order bit of the first
octet corresponds to a resource type of '0' (reserved) - the low-order bit of
the first octet corresponds to a resource type of '7'. Similar to the BITS
pseudotype defined in IETF SMIv2 (RFC 2578), which has the same bit ordering
rules but requires definitions for contiguous enumerated bits.
""")


class _XcmRsrcGeneralFontTypeAccept_Type(OctetString):
    """Custom type xcmRsrcGeneralFontTypeAccept based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmRsrcGeneralFontTypeAccept_Type.__name__ = "OctetString"
_XcmRsrcGeneralFontTypeAccept_Object = MibTableColumn
xcmRsrcGeneralFontTypeAccept = _XcmRsrcGeneralFontTypeAccept_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 7),
    _XcmRsrcGeneralFontTypeAccept_Type()
)
xcmRsrcGeneralFontTypeAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralFontTypeAccept.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralFontTypeAccept.setReference("""\
See: 'XcmFontType' in XCMI Document Resources TC; 'hrPrinterDetectedErrorState'
in IETF Host Resources MIB (RFC 1514/2790); Section 7.1.4 'The BITS construct'
in IETF SMIv2 (RFC 2578); Section 8 'Serialization using the BER' in IETF
Transport Mappings for SNMPv2 (RFC 1908).
""")
if mibBuilder.loadTexts:
    xcmRsrcGeneralFontTypeAccept.setDescription("""\
Indicates all of the font types which are accepted for dynamic delivery to and
use by this host system, specified in a bit-array. Usage: This bit-array is
constructed from the set of supported values from 'XcmFontType', used as powers
of 2 with big-endian rules - the high-order bit of the first octet corresponds
to a font type of '0' (reserved) - the low-order bit of the first octet
corresponds to a font type of '7'. Similar to the BITS pseudotype defined in
IETF SMIv2 (RFC 2578), which has the same bit ordering rules but requires
definitions for contiguous enumerated bits.
""")


class _XcmRsrcGeneralRsrcTypeSupport_Type(OctetString):
    """Custom type xcmRsrcGeneralRsrcTypeSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XcmRsrcGeneralRsrcTypeSupport_Type.__name__ = "OctetString"
_XcmRsrcGeneralRsrcTypeSupport_Object = MibTableColumn
xcmRsrcGeneralRsrcTypeSupport = _XcmRsrcGeneralRsrcTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 8),
    _XcmRsrcGeneralRsrcTypeSupport_Type()
)
xcmRsrcGeneralRsrcTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralRsrcTypeSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralRsrcTypeSupport.setReference("""\
See: 'XcmRsrcType' in XCMI Document Resources TC; 'hrPrinterDetectedErrorState'
in IETF Host Resources MIB (RFC 1514/2790); Section 7.1.4 'The BITS construct'
in IETF SMIv2 (RFC 2578); Section 8 'Serialization using the BER' in IETF
Transport Mappings for SNMPv2 (RFC 1908).
""")
if mibBuilder.loadTexts:
    xcmRsrcGeneralRsrcTypeSupport.setDescription("""\
Indicates all of the document resource types which are supported for use by
this host system, specified in a bit-array. Usage: This bit-array is
constructed from the set of supported values from 'XcmRsrcType', used as powers
of 2 with big-endian rules - the high-order bit of the first octet corresponds
to a resource type of '0' (reserved) - the low-order bit of the first octet
corresponds to a resource type of '7'. Similar to the BITS pseudotype defined
in IETF SMIv2 (RFC 2578), which has the same bit ordering rules but requires
definitions for contiguous enumerated bits.
""")


class _XcmRsrcGeneralFontTypeSupport_Type(OctetString):
    """Custom type xcmRsrcGeneralFontTypeSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmRsrcGeneralFontTypeSupport_Type.__name__ = "OctetString"
_XcmRsrcGeneralFontTypeSupport_Object = MibTableColumn
xcmRsrcGeneralFontTypeSupport = _XcmRsrcGeneralFontTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 1, 1, 1, 9),
    _XcmRsrcGeneralFontTypeSupport_Type()
)
xcmRsrcGeneralFontTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmRsrcGeneralFontTypeSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralFontTypeSupport.setReference("""\
See: 'XcmFontType' in XCMI Document Resources TC; 'hrPrinterDetectedErrorState'
in IETF Host Resources MIB (RFC 1514/2790); Section 7.1.4 'The BITS construct'
in IETF SMIv2 (RFC 2578); Section 8 'Serialization using the BER' in IETF
Transport Mappings for SNMPv2 (RFC 1908).
""")
if mibBuilder.loadTexts:
    xcmRsrcGeneralFontTypeSupport.setDescription("""\
Indicates all of the font types which are supported for use by this host
system, specified in a bit-array. Usage: This bit-array is constructed from the
set of supported values from 'XcmFontType', used as powers of 2 with big-endian
rules - the high-order bit of the first octet corresponds to a font type of '0'
(reserved) - the low-order bit of the first octet corresponds to a font type of
'7'. Similar to the BITS pseudotype defined in IETF SMIv2 (RFC 2578), which has
the same bit ordering rules but requires definitions for contiguous enumerated
bits.
""")
_XcmRsrcMIBConformance_ObjectIdentity = ObjectIdentity
xcmRsrcMIBConformance = _XcmRsrcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2)
)
_XcmRsrcMIBGroups_ObjectIdentity = ObjectIdentity
xcmRsrcMIBGroups = _XcmRsrcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 2)
)
_XcmRsrcInfo_ObjectIdentity = ObjectIdentity
xcmRsrcInfo = _XcmRsrcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3)
)
_XcmRsrcTable_Object = MibTable
xcmRsrcTable = _XcmRsrcTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1)
)
if mibBuilder.loadTexts:
    xcmRsrcTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcTable.setDescription("""\
This table should contain an entry for each unique resource available in the
printer or multi-functional device.
""")
_XcmRsrcEntry_Object = MibTableRow
xcmRsrcEntry = _XcmRsrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1)
)
xcmRsrcEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-RESOURCES-MIB", "xcmRsrcIndex"),
)
if mibBuilder.loadTexts:
    xcmRsrcEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcEntry.setDescription("""\
Entries exist in the table for each available resource on each present device.
""")
_XcmRsrcIndex_Type = Ordinal32
_XcmRsrcIndex_Object = MibTableColumn
xcmRsrcIndex = _XcmRsrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 1),
    _XcmRsrcIndex_Type()
)
xcmRsrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmRsrcIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcIndex.setDescription("""\
A unique value for each available resource on each present device. These values
may change upon addition and deletion of a resource; however, index values
should not change for existing resources at least within a power cycle; and
index values should not be re-used for different resources at least within a
power cycle.
""")
_XcmRsrcRowStatus_Type = RowStatus
_XcmRsrcRowStatus_Object = MibTableColumn
xcmRsrcRowStatus = _XcmRsrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 2),
    _XcmRsrcRowStatus_Type()
)
xcmRsrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcRowStatus.setDescription("""\
Manages the status of this conceptual row in the xcmRsrcTable. Note that the
status of a row in the table should reflect the status of the corresponding
resource, not actually drive the status of the resource; in particular,
removing a row from the table should not itself cause the removal of the
corresponding resource from the device.
""")


class _XcmRsrcType_Type(XcmRsrcType):
    """Custom type xcmRsrcType based on XcmRsrcType"""


_XcmRsrcType_Object = MibTableColumn
xcmRsrcType = _XcmRsrcType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 3),
    _XcmRsrcType_Type()
)
xcmRsrcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcType.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcType.setDescription("""\
The type of this resource, from the given enumeration.
""")


class _XcmRsrcInterpreterLangFamily_Type(XcmPrtInterpreterLangFamily):
    """Custom type xcmRsrcInterpreterLangFamily based on XcmPrtInterpreterLangFamily"""


_XcmRsrcInterpreterLangFamily_Object = MibTableColumn
xcmRsrcInterpreterLangFamily = _XcmRsrcInterpreterLangFamily_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 4),
    _XcmRsrcInterpreterLangFamily_Type()
)
xcmRsrcInterpreterLangFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcInterpreterLangFamily.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcInterpreterLangFamily.setDescription("""\
The print interpreter language or other family of imaging mechanism with which
this resource is associated, from the given enumeration.
""")
_XcmRsrcName_Type = CodeIndexedStringIndex
_XcmRsrcName_Object = MibTableColumn
xcmRsrcName = _XcmRsrcName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 5),
    _XcmRsrcName_Type()
)
xcmRsrcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcName.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcName.setDescription("""\
The resource name, the human-readable name usually used to identify the
resource by and to the device. Being of type CodeIndexedString, the resource
name may be present in multiple character sets, although it will commonly be
present in only one preferred character set, e.g. only in ASCII for the name of
a PostScript font. For a font resource, the resource name is the name of the
font, the deliverable resource which informs how to image the included set of
characters. The font is generally named in accord with the page description
language or other imaging mechanism with which the font is associated. Often
but not always, the font's name is the same as or similar to the name of the
font's typeface, its design. Typical PostScript font names include 'Helvetica'
(i.e. the medium, upright version) and 'Times-BoldItalic'. Typical PCL font
names include 'Courier10' or 'TmsRmn'. However, it should be noted that PCL
font names are normally just comments, not used for machine identification of
the font resource.
""")
_XcmRsrcDescription_Type = CodeIndexedStringIndex
_XcmRsrcDescription_Object = MibTableColumn
xcmRsrcDescription = _XcmRsrcDescription_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 6),
    _XcmRsrcDescription_Type()
)
xcmRsrcDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcDescription.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcDescription.setDescription("""\
A description of the resource, as complete as practical, including resource
type and sub-type and other significant attributes. For example, 'PostScript
Type 1 font for Times Bold Italic'.
""")
_XcmRsrcCopyright_Type = CodeIndexedStringIndex
_XcmRsrcCopyright_Object = MibTableColumn
xcmRsrcCopyright = _XcmRsrcCopyright_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 7),
    _XcmRsrcCopyright_Type()
)
xcmRsrcCopyright.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcCopyright.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcCopyright.setDescription("""\
A human readable copyright message for the resource, e.g. as may be required by
the resource's licensor. May also be null, or indicate that no rights are
claimed, e.g. 'public domain'.
""")


class _XcmRsrcPersistence_Type(XcmRsrcPersistence):
    """Custom type xcmRsrcPersistence based on XcmRsrcPersistence"""


_XcmRsrcPersistence_Object = MibTableColumn
xcmRsrcPersistence = _XcmRsrcPersistence_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 8),
    _XcmRsrcPersistence_Type()
)
xcmRsrcPersistence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcPersistence.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcPersistence.setDescription("""\
The persistence of this resource, from the given enumeration.
""")
_XcmRsrcHrStorageIndex_Type = Cardinal32
_XcmRsrcHrStorageIndex_Object = MibTableColumn
xcmRsrcHrStorageIndex = _XcmRsrcHrStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 9),
    _XcmRsrcHrStorageIndex_Type()
)
xcmRsrcHrStorageIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcHrStorageIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcHrStorageIndex.setReference("""\
See: 'hrStorageIndex' in IETF Host Resources MIB (RFC 1514, September 1993) on
page 8 - which indexes the Host Resources Storage Group (mandatory for all host
systems in HR MIB).
""")
if mibBuilder.loadTexts:
    xcmRsrcHrStorageIndex.setDescription("""\
The hrStorageIndex of the storage device or other storage resource which
contains this document resource. A hrStorageIndex points to a hrStorageEntry in
the hrStorageTable in the Host Resource MIB. Each hrStorageEntry is a sequence
of hrStorageIndex, hrStorageType, hrStorageDescr, hrStorageAllocationUnits,
hrStorageSize, hrStorageUsed, hrStorageAllocationFailures. The hrStorageType
includes hrStorageOther, hrStorageRam, hrStorageVirtualMemory,
hrStorageFixedDisk, hrStorageRemovableDisk, hrStorageFloppyDisk. A 0 index
value indicates no hrStorageEntry.
""")


class _XcmRsrcSizeHigh_Type(Integer64High):
    """Custom type xcmRsrcSizeHigh based on Integer64High"""
    defaultValue = -1


_XcmRsrcSizeHigh_Object = MibTableColumn
xcmRsrcSizeHigh = _XcmRsrcSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 10),
    _XcmRsrcSizeHigh_Type()
)
xcmRsrcSizeHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcSizeHigh.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcSizeHigh.setDescription("""\
The high-order part of the data storage size of this document resource itself,
in units of bytes. A xcmRsrcSizeHigh value of -1 indicates unknown size.
""")
_XcmRsrcSizeLow_Type = Integer64Low
_XcmRsrcSizeLow_Object = MibTableColumn
xcmRsrcSizeLow = _XcmRsrcSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 11),
    _XcmRsrcSizeLow_Type()
)
xcmRsrcSizeLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcSizeLow.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcSizeLow.setDescription("""\
The low-order part of the data storage size of this document resource itself,
in units of bytes. A xcmRsrcSizeHigh value of -1 indicates unknown size.
""")
_XcmRsrcID_Type = CodeIndexedStringIndex
_XcmRsrcID_Object = MibTableColumn
xcmRsrcID = _XcmRsrcID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 12),
    _XcmRsrcID_Type()
)
xcmRsrcID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcID.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcID.setDescription("""\
An ID, or identifier, for the resource, complementary to the resource name, as
appropriate to the resource type and sub-type. For example, for a PostScript
font or PCL font, this resource ID would be the PostScript or PCL font ID.
Where the ID is inherently an integer or other number, e.g. as for a PCL font
ID, it is nonetheless represented here as a string, e.g. '253'.
""")
_XcmRsrcVersion_Type = CodeIndexedStringIndex
_XcmRsrcVersion_Object = MibTableColumn
xcmRsrcVersion = _XcmRsrcVersion_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 1, 1, 13),
    _XcmRsrcVersion_Type()
)
xcmRsrcVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmRsrcVersion.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcVersion.setDescription("""\
The version of the resource, as appropriate to the resource type and sub-type.
Where the version is inherently an integer or other number, it is nonetheless
represented here as a string, e.g. '3'.
""")
_XcmRsrcV1EventOID_ObjectIdentity = ObjectIdentity
xcmRsrcV1EventOID = _XcmRsrcV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 2)
)
if mibBuilder.loadTexts:
    xcmRsrcV1EventOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcV1EventOID.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever a
resource entry or a subordinate entry changes. See SNMPv2 trap definition
'xcmRsrcV2Event' below for 'special semantics'.
""")
_XcmRsrcV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmRsrcV2EventPrefix = _XcmRsrcV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 2, 0)
)
_XcmFontInfo_ObjectIdentity = ObjectIdentity
xcmFontInfo = _XcmFontInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4)
)
_XcmFontTable_Object = MibTable
xcmFontTable = _XcmFontTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1)
)
if mibBuilder.loadTexts:
    xcmFontTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontTable.setDescription("""\
This table should contain an entry for each unique font available in the
device. If a font is available to multiple interpreters, there should be
multiple entries for that font, one per interpreter.
""")
_XcmFontEntry_Object = MibTableRow
xcmFontEntry = _XcmFontEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1)
)
xcmFontEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-RESOURCES-MIB", "xcmRsrcIndex"),
)
if mibBuilder.loadTexts:
    xcmFontEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontEntry.setDescription("""\
Entries exist in the table for each font available to an interpreter in the
device.
""")
_XcmFontRowStatus_Type = RowStatus
_XcmFontRowStatus_Object = MibTableColumn
xcmFontRowStatus = _XcmFontRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 1),
    _XcmFontRowStatus_Type()
)
xcmFontRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontRowStatus.setDescription("""\
Manages the status of this conceptual row in the xcmFontTable.
""")


class _XcmFontType_Type(XcmFontType):
    """Custom type xcmFontType based on XcmFontType"""


_XcmFontType_Object = MibTableColumn
xcmFontType = _XcmFontType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 2),
    _XcmFontType_Type()
)
xcmFontType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontType.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontType.setDescription("""\
The type of this font, from the given enumeration.
""")


class _XcmFontPointsMinNumerator_Type(Integer32):
    """Custom type xcmFontPointsMinNumerator based on Integer32"""
    defaultValue = -2


_XcmFontPointsMinNumerator_Object = MibTableColumn
xcmFontPointsMinNumerator = _XcmFontPointsMinNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 3),
    _XcmFontPointsMinNumerator_Type()
)
xcmFontPointsMinNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPointsMinNumerator.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPointsMinNumerator.setDescription("""\
The numerator of a fraction indicating the body size, or the minimum of the
supported range of body sizes, of the font. The size is in units of printer's
points, which units are here considered to be exactly 1/72 of an inch. Values
of -1 indicate 'infinite,' while values of -2 indicate 'unknown.'
""")


class _XcmFontPointsMaxNumerator_Type(Integer32):
    """Custom type xcmFontPointsMaxNumerator based on Integer32"""
    defaultValue = -2


_XcmFontPointsMaxNumerator_Object = MibTableColumn
xcmFontPointsMaxNumerator = _XcmFontPointsMaxNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 4),
    _XcmFontPointsMaxNumerator_Type()
)
xcmFontPointsMaxNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPointsMaxNumerator.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPointsMaxNumerator.setDescription("""\
The numerator of a fraction indicating the body size, or the maximum of the
supported range of body sizes, of the font. The size is in units of printer's
points, which units are here considered to be exactly 1/72 of an inch. Values
of -1 indicate 'infinite,' while values of -2 indicate 'unknown.'
""")


class _XcmFontPointsDenominator_Type(Integer32):
    """Custom type xcmFontPointsDenominator based on Integer32"""
    defaultValue = -2


_XcmFontPointsDenominator_Object = MibTableColumn
xcmFontPointsDenominator = _XcmFontPointsDenominator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 5),
    _XcmFontPointsDenominator_Type()
)
xcmFontPointsDenominator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPointsDenominator.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPointsDenominator.setDescription("""\
The denominator of both minimum and maximum body size. The denominator is
typically chosen to give a convenient scale and precision for expressing the
sizes. Values of -1 indicate 'infinite,' while values of -2 indicate 'unknown.'
""")


class _XcmFontSpacing_Type(XcmFontSpacing):
    """Custom type xcmFontSpacing based on XcmFontSpacing"""


_XcmFontSpacing_Object = MibTableColumn
xcmFontSpacing = _XcmFontSpacing_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 6),
    _XcmFontSpacing_Type()
)
xcmFontSpacing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontSpacing.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontSpacing.setDescription("""\
The kind of spacing of the characters in this font, from the given enumeration.
""")


class _XcmFontCharSet_Type(IANACharset):
    """Custom type xcmFontCharSet based on IANACharset"""


_XcmFontCharSet_Object = MibTableColumn
xcmFontCharSet = _XcmFontCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 4, 1, 1, 7),
    _XcmFontCharSet_Type()
)
xcmFontCharSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontCharSet.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontCharSet.setDescription("""\
The character set of this font resource. The value is the enum for the IANA-
registered coded character set, per the IANACharset textual-convention in the
Printer MIB (RFC 1759). For more info. about character sets and coded character
sets, see RFCs 2277 and 2278.
""")
_XcmFontPCLInfo_ObjectIdentity = ObjectIdentity
xcmFontPCLInfo = _XcmFontPCLInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5)
)
_XcmFontPCLTable_Object = MibTable
xcmFontPCLTable = _XcmFontPCLTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1)
)
if mibBuilder.loadTexts:
    xcmFontPCLTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPCLTable.setDescription("""\
This table should contain an entry for each unique font available in the
device. If a font is available to multiple interpreters, there should be
multiple entries for that font here, one entry per interpreter.
""")
_XcmFontPCLEntry_Object = MibTableRow
xcmFontPCLEntry = _XcmFontPCLEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1)
)
xcmFontPCLEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-RESOURCES-MIB", "xcmRsrcIndex"),
)
if mibBuilder.loadTexts:
    xcmFontPCLEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPCLEntry.setDescription("""\
Entries exist in the table for each PCL font.
""")
_XcmFontPCLRowStatus_Type = RowStatus
_XcmFontPCLRowStatus_Object = MibTableColumn
xcmFontPCLRowStatus = _XcmFontPCLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 1),
    _XcmFontPCLRowStatus_Type()
)
xcmFontPCLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPCLRowStatus.setDescription("""\
Manages the status of this conceptual row in the xcmFontPCLTable.
""")


class _XcmFontPCLTypefaceValue_Type(Integer32):
    """Custom type xcmFontPCLTypefaceValue based on Integer32"""
    defaultValue = -1


_XcmFontPCLTypefaceValue_Object = MibTableColumn
xcmFontPCLTypefaceValue = _XcmFontPCLTypefaceValue_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 2),
    _XcmFontPCLTypefaceValue_Type()
)
xcmFontPCLTypefaceValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLTypefaceValue.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPCLTypefaceValue.setReference("""\
See: 'PCL 5 Printer Language Technical Reference Manual' and 'PCL 5 Comparision
Guide' by Hewlett-Packard Corporation.
""")
if mibBuilder.loadTexts:
    xcmFontPCLTypefaceValue.setDescription("""\
The integer value specifying the PCL 'typeface' (really family) of the font.
For example, 3 normally indicates Courier, 4 indicates 'Helv'. A value of -1
indicates unknown typeface value.
""")


class _XcmFontPCLSymbolSetValue_Type(Integer32):
    """Custom type xcmFontPCLSymbolSetValue based on Integer32"""
    defaultValue = -1


_XcmFontPCLSymbolSetValue_Object = MibTableColumn
xcmFontPCLSymbolSetValue = _XcmFontPCLSymbolSetValue_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 3),
    _XcmFontPCLSymbolSetValue_Type()
)
xcmFontPCLSymbolSetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLSymbolSetValue.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPCLSymbolSetValue.setReference("""\
See: 'PCL 5 Printer Language Technical Reference Manual' and 'PCL 5 Comparision
Guide' by Hewlett-Packard Corporation.
""")
if mibBuilder.loadTexts:
    xcmFontPCLSymbolSetValue.setDescription("""\
The integer value specifying the PCL symbol set of the font. For example, 21
normally indicates ASCII, 277 indicates the HP Roman-8 set. A value of -1
indicates unknown symbol set value.
""")


class _XcmFontPCLStyle_Type(XcmFontPCLStyle):
    """Custom type xcmFontPCLStyle based on XcmFontPCLStyle"""


_XcmFontPCLStyle_Object = MibTableColumn
xcmFontPCLStyle = _XcmFontPCLStyle_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 4),
    _XcmFontPCLStyle_Type()
)
xcmFontPCLStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLStyle.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPCLStyle.setReference("""\
See: 'PCL 5 Printer Language Technical Reference Manual' and 'PCL 5 Comparision
Guide' by Hewlett-Packard Corporation.
""")
if mibBuilder.loadTexts:
    xcmFontPCLStyle.setDescription("""\
The style of the font, from the given enumeration.
""")


class _XcmFontPCLPitchMinNumerator_Type(Integer32):
    """Custom type xcmFontPCLPitchMinNumerator based on Integer32"""
    defaultValue = -2


_XcmFontPCLPitchMinNumerator_Object = MibTableColumn
xcmFontPCLPitchMinNumerator = _XcmFontPCLPitchMinNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 5),
    _XcmFontPCLPitchMinNumerator_Type()
)
xcmFontPCLPitchMinNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLPitchMinNumerator.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPCLPitchMinNumerator.setDescription("""\
The numerator of a fraction indicating the pitch, or the minimum of the
supported range of pitches, of the font. The pitch is in units of characters
per inch. Values of -1 indicate 'infinite,' while values of -2 indicate
'unknown.'
""")


class _XcmFontPCLPitchMaxNumerator_Type(Integer32):
    """Custom type xcmFontPCLPitchMaxNumerator based on Integer32"""
    defaultValue = -2


_XcmFontPCLPitchMaxNumerator_Object = MibTableColumn
xcmFontPCLPitchMaxNumerator = _XcmFontPCLPitchMaxNumerator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 6),
    _XcmFontPCLPitchMaxNumerator_Type()
)
xcmFontPCLPitchMaxNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLPitchMaxNumerator.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPCLPitchMaxNumerator.setDescription("""\
The numerator of a fraction indicating the pitch, or the maximum of the
supported range of pitches, of the font. The pitch is in units of characters
per inch. Values of -1 indicate 'infinite,' while values of -2 indicate
'unknown.'
""")


class _XcmFontPCLPitchDenominator_Type(Integer32):
    """Custom type xcmFontPCLPitchDenominator based on Integer32"""
    defaultValue = -2


_XcmFontPCLPitchDenominator_Object = MibTableColumn
xcmFontPCLPitchDenominator = _XcmFontPCLPitchDenominator_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 7),
    _XcmFontPCLPitchDenominator_Type()
)
xcmFontPCLPitchDenominator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLPitchDenominator.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPCLPitchDenominator.setDescription("""\
The denominator of both minimum and maximum pitch. The denominator is typically
chosen to give a convenient scale and precision for expressing the pitches.
Values of -1 indicate 'infinite,' while values of -2 indicate 'unknown.'
""")


class _XcmFontPCLStrokeWeight_Type(XcmFontPCLStrokeWeight):
    """Custom type xcmFontPCLStrokeWeight based on XcmFontPCLStrokeWeight"""


_XcmFontPCLStrokeWeight_Object = MibTableColumn
xcmFontPCLStrokeWeight = _XcmFontPCLStrokeWeight_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 5, 1, 1, 8),
    _XcmFontPCLStrokeWeight_Type()
)
xcmFontPCLStrokeWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmFontPCLStrokeWeight.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPCLStrokeWeight.setReference("""\
See: 'PCL 5 Printer Language Technical Reference Manual' and 'PCL 5 Comparision
Guide' by Hewlett-Packard Corporation.
""")
if mibBuilder.loadTexts:
    xcmFontPCLStrokeWeight.setDescription("""\
The PCL stroke weight of the font, from the given enumeration.
""")

# Managed Objects groups

xcmRsrcGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 2, 1)
)
xcmRsrcGeneralGroup.setObjects(
      *(("XEROX-RESOURCES-MIB", "xcmRsrcGeneralRowStatus"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralGroupSupport"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralCreateSupport"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralUpdateSupport"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralRsrcTypeAccept"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralFontTypeAccept"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralRsrcTypeSupport"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcGeneralFontTypeSupport"))
)
if mibBuilder.loadTexts:
    xcmRsrcGeneralGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcGeneralGroup.setDescription("""\
The Resources MIB General Group.
""")

xcmRsrcInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 2, 3)
)
xcmRsrcInfoGroup.setObjects(
      *(("XEROX-RESOURCES-MIB", "xcmRsrcRowStatus"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcType"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcInterpreterLangFamily"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcName"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcDescription"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcCopyright"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcPersistence"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcHrStorageIndex"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcSizeHigh"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcSizeLow"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcID"),
        ("XEROX-RESOURCES-MIB", "xcmRsrcVersion"))
)
if mibBuilder.loadTexts:
    xcmRsrcInfoGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmRsrcInfoGroup.setDescription("""\
The Document Resources MIB (Generic) Resources Group.
""")

xcmFontInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 2, 4)
)
xcmFontInfoGroup.setObjects(
      *(("XEROX-RESOURCES-MIB", "xcmFontRowStatus"),
        ("XEROX-RESOURCES-MIB", "xcmFontType"),
        ("XEROX-RESOURCES-MIB", "xcmFontPointsMinNumerator"),
        ("XEROX-RESOURCES-MIB", "xcmFontPointsMaxNumerator"),
        ("XEROX-RESOURCES-MIB", "xcmFontPointsDenominator"),
        ("XEROX-RESOURCES-MIB", "xcmFontSpacing"),
        ("XEROX-RESOURCES-MIB", "xcmFontCharSet"))
)
if mibBuilder.loadTexts:
    xcmFontInfoGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontInfoGroup.setDescription("""\
The Resources MIB (General) Fonts Group.
""")

xcmFontPCLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 2, 5)
)
xcmFontPCLGroup.setObjects(
      *(("XEROX-RESOURCES-MIB", "xcmFontPCLRowStatus"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLTypefaceValue"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLSymbolSetValue"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLStyle"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLPitchMinNumerator"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLPitchMaxNumerator"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLPitchDenominator"),
        ("XEROX-RESOURCES-MIB", "xcmFontPCLStrokeWeight"))
)
if mibBuilder.loadTexts:
    xcmFontPCLGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmFontPCLGroup.setDescription("""\
The Resources MIB PCL Fonts Group.
""")


# Notification objects

xcmRsrcV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 3, 2, 0, 1)
)
xcmRsrcV2Event.setObjects(
    ("XEROX-RESOURCES-MIB", "xcmRsrcRowStatus")
)
if mibBuilder.loadTexts:
    xcmRsrcV2Event.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmRsrcV2Event.setDescription("""\
This trap is sent whenever ANY object in a resource entry or in a subordinate
entry changes. This notification has the following special semantics: o Any
resource entry object (e.g. 'xcmRsrcPersistence' in the Resource table) whose
value has changed SHOULD also be added to this trap's variable-bindings. o Any
subordinate entry object (e.g. 'xcmFontRowStatus' in the Font table) whose
value has changed MAY also be added to this trap's variable-bindings. The above
special semantics permit optimizations by agreement between SNMP manager and
SNMP agent implementers.
""")


# Notifications groups


# Agent capabilities


# Module compliance

xcmRsrcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 57, 2, 1)
)
if mibBuilder.loadTexts:
    xcmRsrcMIBCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmRsrcMIBCompliance.setDescription("""\
The compliance statement for SNMP management agents that implement the XCMI
Document Resources MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-RESOURCES-MIB",
    **{"xcmRsrcMIB": xcmRsrcMIB,
       "xcmRsrcGeneral": xcmRsrcGeneral,
       "xcmRsrcGeneralTable": xcmRsrcGeneralTable,
       "xcmRsrcGeneralEntry": xcmRsrcGeneralEntry,
       "xcmRsrcGeneralIndex": xcmRsrcGeneralIndex,
       "xcmRsrcGeneralRowStatus": xcmRsrcGeneralRowStatus,
       "xcmRsrcGeneralGroupSupport": xcmRsrcGeneralGroupSupport,
       "xcmRsrcGeneralCreateSupport": xcmRsrcGeneralCreateSupport,
       "xcmRsrcGeneralUpdateSupport": xcmRsrcGeneralUpdateSupport,
       "xcmRsrcGeneralRsrcTypeAccept": xcmRsrcGeneralRsrcTypeAccept,
       "xcmRsrcGeneralFontTypeAccept": xcmRsrcGeneralFontTypeAccept,
       "xcmRsrcGeneralRsrcTypeSupport": xcmRsrcGeneralRsrcTypeSupport,
       "xcmRsrcGeneralFontTypeSupport": xcmRsrcGeneralFontTypeSupport,
       "xcmRsrcMIBConformance": xcmRsrcMIBConformance,
       "xcmRsrcMIBCompliance": xcmRsrcMIBCompliance,
       "xcmRsrcMIBGroups": xcmRsrcMIBGroups,
       "xcmRsrcGeneralGroup": xcmRsrcGeneralGroup,
       "xcmRsrcInfoGroup": xcmRsrcInfoGroup,
       "xcmFontInfoGroup": xcmFontInfoGroup,
       "xcmFontPCLGroup": xcmFontPCLGroup,
       "xcmRsrcInfo": xcmRsrcInfo,
       "xcmRsrcTable": xcmRsrcTable,
       "xcmRsrcEntry": xcmRsrcEntry,
       "xcmRsrcIndex": xcmRsrcIndex,
       "xcmRsrcRowStatus": xcmRsrcRowStatus,
       "xcmRsrcType": xcmRsrcType,
       "xcmRsrcInterpreterLangFamily": xcmRsrcInterpreterLangFamily,
       "xcmRsrcName": xcmRsrcName,
       "xcmRsrcDescription": xcmRsrcDescription,
       "xcmRsrcCopyright": xcmRsrcCopyright,
       "xcmRsrcPersistence": xcmRsrcPersistence,
       "xcmRsrcHrStorageIndex": xcmRsrcHrStorageIndex,
       "xcmRsrcSizeHigh": xcmRsrcSizeHigh,
       "xcmRsrcSizeLow": xcmRsrcSizeLow,
       "xcmRsrcID": xcmRsrcID,
       "xcmRsrcVersion": xcmRsrcVersion,
       "xcmRsrcV1EventOID": xcmRsrcV1EventOID,
       "xcmRsrcV2EventPrefix": xcmRsrcV2EventPrefix,
       "xcmRsrcV2Event": xcmRsrcV2Event,
       "xcmFontInfo": xcmFontInfo,
       "xcmFontTable": xcmFontTable,
       "xcmFontEntry": xcmFontEntry,
       "xcmFontRowStatus": xcmFontRowStatus,
       "xcmFontType": xcmFontType,
       "xcmFontPointsMinNumerator": xcmFontPointsMinNumerator,
       "xcmFontPointsMaxNumerator": xcmFontPointsMaxNumerator,
       "xcmFontPointsDenominator": xcmFontPointsDenominator,
       "xcmFontSpacing": xcmFontSpacing,
       "xcmFontCharSet": xcmFontCharSet,
       "xcmFontPCLInfo": xcmFontPCLInfo,
       "xcmFontPCLTable": xcmFontPCLTable,
       "xcmFontPCLEntry": xcmFontPCLEntry,
       "xcmFontPCLRowStatus": xcmFontPCLRowStatus,
       "xcmFontPCLTypefaceValue": xcmFontPCLTypefaceValue,
       "xcmFontPCLSymbolSetValue": xcmFontPCLSymbolSetValue,
       "xcmFontPCLStyle": xcmFontPCLStyle,
       "xcmFontPCLPitchMinNumerator": xcmFontPCLPitchMinNumerator,
       "xcmFontPCLPitchMaxNumerator": xcmFontPCLPitchMaxNumerator,
       "xcmFontPCLPitchDenominator": xcmFontPCLPitchDenominator,
       "xcmFontPCLStrokeWeight": xcmFontPCLStrokeWeight}
)

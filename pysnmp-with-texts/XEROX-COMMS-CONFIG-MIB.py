"""SNMP MIB module (XEROX-COMMS-CONFIG-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-COMMS-CONFIG-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:06 2024
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

(ModuleCompliance,
 ObjectGroup,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "ObjectGroup",
    "NotificationGroup")

(MibIdentifier,
 IpAddress,
 NotificationType,
 Counter32,
 Gauge32,
 TimeTicks,
 ModuleIdentity,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 iso,
 Bits,
 Counter64,
 Integer32,
 Unsigned32) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "MibIdentifier",
    "IpAddress",
    "NotificationType",
    "Counter32",
    "Gauge32",
    "TimeTicks",
    "ModuleIdentity",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "iso",
    "Bits",
    "Counter64",
    "Integer32",
    "Unsigned32")

(RowStatus,
 TextualConvention,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "RowStatus",
    "TextualConvention",
    "DisplayString")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(XcmCommsDirRecordType,
 XcmCommsDirAttributeType,
 XcmCommsConfigGroupSupport) = mibBuilder.importSymbols(
    "XEROX-COMMS-CONFIG-TC",
    "XcmCommsDirRecordType",
    "XcmCommsDirAttributeType",
    "XcmCommsConfigGroupSupport")

(XcmCommsStackExtProtocol,) = mibBuilder.importSymbols(
    "XEROX-COMMS-ENGINE-TC",
    "XcmCommsStackExtProtocol")

(zeroDotZero,
 Cardinal32,
 XcmGenOptionValueSyntax,
 Ordinal32,
 XcmFixedLocaleUtf8String) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "zeroDotZero",
    "Cardinal32",
    "XcmGenOptionValueSyntax",
    "Ordinal32",
    "XcmFixedLocaleUtf8String")


# MODULE-IDENTITY

xcmCommsConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64)
)
xcmCommsConfigMIB.setLastUpdated("0210310000Z")
if mibBuilder.loadTexts:
    xcmCommsConfigMIB.setOrganization("""\
Xerox Corporation - XCMI Working Group
""")
xcmCommsConfigMIB.setContactInfo("""\
 XCMI Editors Email: coherence@crt.xerox.com
""")
if mibBuilder.loadTexts:
    xcmCommsConfigMIB.setDescription("""\
Version: 5.11.pub The MIB module which supports active configuration discovery
of communications protocol stacks, communications end system applications,
communications intermediate systems, and communications gateways for network
accessible host systems. Usage: Note that throughout this MIB module, the INDEX
clauses referring to 'hrDeviceIndex' for the 'hrDeviceTable' (Devices Group) of
the Host Resources MIB (RFC 2790) SHALL specify host system CPUs (ie,
'hrDeviceProcessor') and shall NOT specify host system 'network interfaces',
with entries in the 'ifTable' (Interfaces Group) of MIB-II (RFC 1213).
Copyright (C) 1996-2002 Xerox Corporation. All Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmCommsConfigZeroDummy_ObjectIdentity = ObjectIdentity
xcmCommsConfigZeroDummy = _XcmCommsConfigZeroDummy_ObjectIdentity(
    (0, 0, 64)
)
_XcmCommsConfigMIBConformance_ObjectIdentity = ObjectIdentity
xcmCommsConfigMIBConformance = _XcmCommsConfigMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2)
)
_XcmCommsConfigMIBGroups_ObjectIdentity = ObjectIdentity
xcmCommsConfigMIBGroups = _XcmCommsConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2)
)
_XcmCommsConfig_ObjectIdentity = ObjectIdentity
xcmCommsConfig = _XcmCommsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3)
)
_XcmCommsConfigTable_Object = MibTable
xcmCommsConfigTable = _XcmCommsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2)
)
if mibBuilder.loadTexts:
    xcmCommsConfigTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsConfigTable.setDescription("""\
A table of the communications engines installed and (possibly) running on
platforms (ie, CPUs) on this host system.
""")
_XcmCommsConfigEntry_Object = MibTableRow
xcmCommsConfigEntry = _XcmCommsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1)
)
xcmCommsConfigEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsConfigEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsConfigEntry.setDescription("""\
An entry for a communications engine installed and (possibly) running on a
platform (ie, CPU) on this host system. Usage: Note that values of
'hrDeviceIndex' used to reference entries in the 'xcmCommsEngineTable' SHALL
reference entries in the 'hrDeviceTable' with 'hrDeviceType' equal to
'hrDeviceProcessor' (representing host system CPUs and therefore also having
corresponding entries in the 'hrProcessorTable').
""")
_XcmCommsConfigRowStatus_Type = RowStatus
_XcmCommsConfigRowStatus_Object = MibTableColumn
xcmCommsConfigRowStatus = _XcmCommsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 1),
    _XcmCommsConfigRowStatus_Type()
)
xcmCommsConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsConfigRowStatus.setDescription("""\
This object displays the status of individual conceptual rows in the
'xcmCommsConfigTable'. Usage: 'xcmCommsConfigRowStatus' is 'read-only' because
these conceptual rows shall NOT be deleted.
""")
_XcmCommsConfigActiveOptionFirst_Type = Cardinal32
_XcmCommsConfigActiveOptionFirst_Object = MibTableColumn
xcmCommsConfigActiveOptionFirst = _XcmCommsConfigActiveOptionFirst_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 2),
    _XcmCommsConfigActiveOptionFirst_Type()
)
xcmCommsConfigActiveOptionFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigActiveOptionFirst.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsConfigActiveOptionFirst.setReference("""\
See: 'xcmCommsConfigActiveOptionLast'
""")
if mibBuilder.loadTexts:
    xcmCommsConfigActiveOptionFirst.setDescription("""\
The value of 'xcmCommsOptionIndex' corresponding to the first active
configuration option (in 'xcmCommsOptionTable'), or zero if this communications
engine does NOT require such information. Usage: This 'chain' represents
currently active configuration options of this communications engine.
""")
_XcmCommsConfigActiveOptionLast_Type = Cardinal32
_XcmCommsConfigActiveOptionLast_Object = MibTableColumn
xcmCommsConfigActiveOptionLast = _XcmCommsConfigActiveOptionLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 3),
    _XcmCommsConfigActiveOptionLast_Type()
)
xcmCommsConfigActiveOptionLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigActiveOptionLast.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsConfigActiveOptionLast.setReference("""\
See: 'xcmCommsConfigActiveOptionFirst'
""")
if mibBuilder.loadTexts:
    xcmCommsConfigActiveOptionLast.setDescription("""\
The value of 'xcmCommsOptionIndex' corresponding to the last active
configuration option (in 'xcmCommsOptionTable'), or zero if this communications
engine does NOT require such information. Usage: This 'chain' represents
currently active configuration options of this communications engine. Usage:
The last entry index explicitly bounds the valid range of
'xcmCommsOptionIndex'. This is the value of the numerically highest entry
index, NOT necessarily the 'logically last' entry index in the structured tree
in 'xcmCommsOptionTable'.
""")


class _XcmCommsConfigGroupSupport_Type(XcmCommsConfigGroupSupport):
    """Custom type xcmCommsConfigGroupSupport based on XcmCommsConfigGroupSupport"""
    defaultValue = 1


_XcmCommsConfigGroupSupport_Object = MibTableColumn
xcmCommsConfigGroupSupport = _XcmCommsConfigGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 4),
    _XcmCommsConfigGroupSupport_Type()
)
xcmCommsConfigGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsConfigGroupSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Comms Config MIB object groups supported by this management agent
implementation (ie, version) on this host system, specified in a bit-mask.
Usage: Conforming management agents SHALL accurately report their support for
XCMI Comms Config MIB object groups.
""")
_XcmCommsConfigCreateSupport_Type = XcmCommsConfigGroupSupport
_XcmCommsConfigCreateSupport_Object = MibTableColumn
xcmCommsConfigCreateSupport = _XcmCommsConfigCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 5),
    _XcmCommsConfigCreateSupport_Type()
)
xcmCommsConfigCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigCreateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsConfigCreateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Comms Config MIB object groups supported for dynamic row creation
(via '...RowStatus') by this management agent implementation (ie, version) on
this host system, specified in a bit-mask. Usage: Conforming management agents
SHALL accurately report their support for XCMI Comms Config MIB object groups.
""")
_XcmCommsConfigUpdateSupport_Type = XcmCommsConfigGroupSupport
_XcmCommsConfigUpdateSupport_Object = MibTableColumn
xcmCommsConfigUpdateSupport = _XcmCommsConfigUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 3, 2, 1, 6),
    _XcmCommsConfigUpdateSupport_Type()
)
xcmCommsConfigUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsConfigUpdateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsConfigUpdateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Comms Config MIB object groups supported for existing row update
(via SNMP Set-Request PDUs) by this management agent implementation (ie,
version) on this host system, specified in a bit-mask. Usage: Conforming
management agents SHALL accurately report their support for XCMI Comms Config
MIB object groups.
""")
_XcmCommsOption_ObjectIdentity = ObjectIdentity
xcmCommsOption = _XcmCommsOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4)
)
_XcmCommsOptionTable_Object = MibTable
xcmCommsOptionTable = _XcmCommsOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2)
)
if mibBuilder.loadTexts:
    xcmCommsOptionTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionTable.setDescription("""\
A table containing information on installation, configuration, or other aspects
of communications options on this host system.
""")
_XcmCommsOptionEntry_Object = MibTableRow
xcmCommsOptionEntry = _XcmCommsOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1)
)
xcmCommsOptionEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsOptionEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionEntry.setDescription("""\
An entry containing information on installation, configuration, or other
aspects of communications options on this host system.
""")
_XcmCommsOptionIndex_Type = Ordinal32
_XcmCommsOptionIndex_Object = MibTableColumn
xcmCommsOptionIndex = _XcmCommsOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 1),
    _XcmCommsOptionIndex_Type()
)
xcmCommsOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsOptionIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmCommsOptionTable'.
""")
_XcmCommsOptionRowStatus_Type = RowStatus
_XcmCommsOptionRowStatus_Object = MibTableColumn
xcmCommsOptionRowStatus = _XcmCommsOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 2),
    _XcmCommsOptionRowStatus_Type()
)
xcmCommsOptionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionRowStatus.setDescription("""\
This object displays the status of individual conceptual rows in the
'xcmCommsOptionTable'.
""")


class _XcmCommsOptionTypeOID_Type(ObjectIdentifier):
    """Custom type xcmCommsOptionTypeOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmCommsOptionTypeOID_Object = MibTableColumn
xcmCommsOptionTypeOID = _XcmCommsOptionTypeOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 3),
    _XcmCommsOptionTypeOID_Type()
)
xcmCommsOptionTypeOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionTypeOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionTypeOID.setDescription("""\
An unambiguous communications option type, used by system administrators and
end users to identify this communications option. Usage: Since this
communications option type is specified as an object identifier, it MAY be
taken from any IETF, Xerox, third- party, or product-specific MIB, or it MAY
simply be any IETF SMIv2-style 'autonomous type'.
""")


class _XcmCommsOptionValueSyntax_Type(XcmGenOptionValueSyntax):
    """Custom type xcmCommsOptionValueSyntax based on XcmGenOptionValueSyntax"""


_XcmCommsOptionValueSyntax_Object = MibTableColumn
xcmCommsOptionValueSyntax = _XcmCommsOptionValueSyntax_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 4),
    _XcmCommsOptionValueSyntax_Type()
)
xcmCommsOptionValueSyntax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueSyntax.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionValueSyntax.setDescription("""\
A communications option value syntax, used by system administrators and end
users to specify the correct value syntax for this communications option.
Usage: This communications option value syntax is used to select which of the
following three objects shall be used to contain the value of this
communications option.
""")
_XcmCommsOptionValueInteger_Type = Integer32
_XcmCommsOptionValueInteger_Object = MibTableColumn
xcmCommsOptionValueInteger = _XcmCommsOptionValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 5),
    _XcmCommsOptionValueInteger_Type()
)
xcmCommsOptionValueInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueInteger.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionValueInteger.setReference("""\
See: 'xcmCommsOptionValueSyntax' and 'xcmCommsOptionTypeOID'
""")
if mibBuilder.loadTexts:
    xcmCommsOptionValueInteger.setDescription("""\
A communications option value integer, used by system administrators and end
users to specify the current value for a communications option with a base
value syntax of 'INTEGER'.
""")


class _XcmCommsOptionValueOID_Type(ObjectIdentifier):
    """Custom type xcmCommsOptionValueOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmCommsOptionValueOID_Object = MibTableColumn
xcmCommsOptionValueOID = _XcmCommsOptionValueOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 6),
    _XcmCommsOptionValueOID_Type()
)
xcmCommsOptionValueOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionValueOID.setReference("""\
See: 'xcmCommsOptionValueSyntax' and 'xcmCommsOptionTypeOID'
""")
if mibBuilder.loadTexts:
    xcmCommsOptionValueOID.setDescription("""\
A communications option value OID (object identifier), used by system
administrators and end users to specify the current value for a communications
option with a base value syntax of 'OBJECT IDENTIFIER'.
""")


class _XcmCommsOptionValueString_Type(OctetString):
    """Custom type xcmCommsOptionValueString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsOptionValueString_Type.__name__ = "OctetString"
_XcmCommsOptionValueString_Object = MibTableColumn
xcmCommsOptionValueString = _XcmCommsOptionValueString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 7),
    _XcmCommsOptionValueString_Type()
)
xcmCommsOptionValueString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueString.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionValueString.setReference("""\
See: 'xcmCommsOptionValueSyntax' and 'xcmCommsOptionTypeOID' See:
'xcmGenFixedLocalizationIndex' in XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsOptionValueString.setDescription("""\
A communications option value string, used by system administrators and end
users to specify the current value for a communications option with a base
value syntax of 'OCTET STRING'. Usage: This object is of type
'XcmFixedLocaleDisplayString' (if 'xcmCommsOptionValueLocalization' is zero) or
'XcmNamedLocaleUtf8String' (if 'xcmCommsOptionValueLocalization' is non-zero).
Usage: Conformant implementations MUST encrypt passwords, keys, and other
security information stored in this string object.
""")
_XcmCommsOptionValueLocalization_Type = Cardinal32
_XcmCommsOptionValueLocalization_Object = MibTableColumn
xcmCommsOptionValueLocalization = _XcmCommsOptionValueLocalization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 8),
    _XcmCommsOptionValueLocalization_Type()
)
xcmCommsOptionValueLocalization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueLocalization.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionValueLocalization.setReference("""\
See: 'xcmCommsOptionValueSyntax' and 'xcmCommsOptionTypeOID'. See:
'xcmGenFixedLocalizationIndex' in XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsOptionValueLocalization.setDescription("""\
A communications option value localization, used by system administrators and
end users to specify the ALTERNATE localization for a communications option
(different from 'xcmGenFixedLocalizationIndex'), so that
'xcmCommsOptionValueString' becomes 'XcmNamedLocaleUtf8String'. Usage: For a
communications option string to which POSIX-style localization (territory,
language, character set) is applicable (non-keyword) this object MAY contain a
suitable index value for 'xcmGenLocalizationIndex' from the XCMI General MIB,
or zero to indicate 'none'.
""")


class _XcmCommsOptionValueCodedCharSet_Type(IANACharset):
    """Custom type xcmCommsOptionValueCodedCharSet based on IANACharset"""


_XcmCommsOptionValueCodedCharSet_Object = MibTableColumn
xcmCommsOptionValueCodedCharSet = _XcmCommsOptionValueCodedCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 9),
    _XcmCommsOptionValueCodedCharSet_Type()
)
xcmCommsOptionValueCodedCharSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionValueCodedCharSet.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionValueCodedCharSet.setReference("""\
See: 'xcmCommsOptionValueSyntax' and 'xcmCommsOptionTypeOID'. See:
'IANACharset' in IETF Printer MIB (RFC 1759). See: 'xcmGenCodedCharSetTable' in
XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsOptionValueCodedCharSet.setDescription("""\
A communications option value character set, used by system administrators and
end users to specify the ALTERNATE character set for a communications option
(different from 'xcmGenFixedLocalizationIndex'), so that
'xcmCommsOptionValueString' is unambiguous. Usage: XCMI conforming management
agents shall ONLY allow Sets of this object to 'other' (none) or 'utf-8'
(Unicode/ ISO-10646 in the UTF-8 encoding, a proper superset of US-ASCII), for
consistency with the Xerox Unicode Coherence Standard.
""")
_XcmCommsOptionNextIndex_Type = Cardinal32
_XcmCommsOptionNextIndex_Object = MibTableColumn
xcmCommsOptionNextIndex = _XcmCommsOptionNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 10),
    _XcmCommsOptionNextIndex_Type()
)
xcmCommsOptionNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionNextIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionNextIndex.setReference("""\
See: 'xcmCommsOption[Family|Previous]Index'
""")
if mibBuilder.loadTexts:
    xcmCommsOptionNextIndex.setDescription("""\
The value of 'xcmCommsOptionIndex' corresponding to the next 'chained'
conceptual row in the 'xcmCommsOptionTable', or zero if this is the last
associated conceptual row in a particular vertical 'chain' within a given set.
Usage: Generally, communications options (of similar or unlike type) are
'chained' vertically via '...[Next|Previous]Index'. But, in the case where
particular communications options MUST be 'tightly coupled', they SHOULD be
'shelved' horizontally via '...[Family|Previous]Index' (eg, an IP address and
an IP subnet mask).
""")
_XcmCommsOptionPreviousIndex_Type = Cardinal32
_XcmCommsOptionPreviousIndex_Object = MibTableColumn
xcmCommsOptionPreviousIndex = _XcmCommsOptionPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 11),
    _XcmCommsOptionPreviousIndex_Type()
)
xcmCommsOptionPreviousIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionPreviousIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionPreviousIndex.setReference("""\
See: 'xcmCommsOption[Next|Family]Index'
""")
if mibBuilder.loadTexts:
    xcmCommsOptionPreviousIndex.setDescription("""\
The value of 'xcmCommsOptionIndex' corresponding to a previous associated
conceptual row in the 'xcmCommsOptionTable', or zero if this is the first
associated conceptual row in a given set. Usage: This object provides common
'backward' linkage for BOTH the 'xcmCommsOptionNextIndex' and
'xcmCommsOptionFamilyIndex' linkage objects. A previous conceptual row MAY
'forward' reference this conceptual row via either '...NextIndex' or
'...FamilyIndex' - ie, a given conceptual row MAY 'forward' reference EXACTLY
zero, one, or two 'later' conceptual rows.
""")
_XcmCommsOptionFamilyIndex_Type = Cardinal32
_XcmCommsOptionFamilyIndex_Object = MibTableColumn
xcmCommsOptionFamilyIndex = _XcmCommsOptionFamilyIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 4, 2, 1, 12),
    _XcmCommsOptionFamilyIndex_Type()
)
xcmCommsOptionFamilyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsOptionFamilyIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionFamilyIndex.setReference("""\
See: 'xcmCommsOption[Next|Previous]Index'
""")
if mibBuilder.loadTexts:
    xcmCommsOptionFamilyIndex.setDescription("""\
The value of 'xcmCommsOptionIndex' corresponding to the next 'family'
conceptual row in the 'xcmCommsOptionTable', or zero if this is the last
associated conceptual row in a particular horizontal 'shelf' (of 'family'
members) within a given set. Usage: Generally, communications options (of
similar or unlike type) are 'chained' vertically via '...[Next|Previous]Index'.
But, in the case where particular communications options MUST be 'tightly
coupled', they SHOULD be 'shelved' horizontally via '...[Family|Previous]Index'
(eg, an IP address and an IP subnet mask).
""")
_XcmCommsDirRecord_ObjectIdentity = ObjectIdentity
xcmCommsDirRecord = _XcmCommsDirRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5)
)
_XcmCommsDirRecordTable_Object = MibTable
xcmCommsDirRecordTable = _XcmCommsDirRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2)
)
if mibBuilder.loadTexts:
    xcmCommsDirRecordTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirRecordTable.setDescription("""\
A table containing directory records configured on this host system.
""")
_XcmCommsDirRecordEntry_Object = MibTableRow
xcmCommsDirRecordEntry = _XcmCommsDirRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1)
)
xcmCommsDirRecordEntry.setIndexNames(
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordType"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsDirRecordEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirRecordEntry.setDescription("""\
An entry for a directory record configured on this host system.
""")
_XcmCommsDirRecordType_Type = XcmCommsDirRecordType
_XcmCommsDirRecordType_Object = MibTableColumn
xcmCommsDirRecordType = _XcmCommsDirRecordType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 1),
    _XcmCommsDirRecordType_Type()
)
xcmCommsDirRecordType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsDirRecordType.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirRecordType.setDescription("""\
A directory record type, used to uniquely identify this directory record (and
all subordinate directory attributes), when combined with
'xcmCommsDirRecordIndex' (below).
""")
_XcmCommsDirRecordIndex_Type = Ordinal32
_XcmCommsDirRecordIndex_Object = MibTableColumn
xcmCommsDirRecordIndex = _XcmCommsDirRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 2),
    _XcmCommsDirRecordIndex_Type()
)
xcmCommsDirRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsDirRecordIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirRecordIndex.setDescription("""\
A directory record index, used to uniquely identify this directory record (and
all subordinate directory attributes), when combined with
'xcmCommsDirRecordType' (above). Usage: This directory record index SHALL be
unique for each record of a given type (value of 'xcmCommsDirRecordType'), but
NEED NOT be unique for directory records of different types. This is to permit
directory records of different types to start their numbering (value of
'xcmCommsDirRecordIndex') over from one ('1') and such usage is RECOMMENDED.
""")
_XcmCommsDirRecordRowStatus_Type = RowStatus
_XcmCommsDirRecordRowStatus_Object = MibTableColumn
xcmCommsDirRecordRowStatus = _XcmCommsDirRecordRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 3),
    _XcmCommsDirRecordRowStatus_Type()
)
xcmCommsDirRecordRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirRecordRowStatus.setReference("""\
See: 'xcmCommsConfigCreateSupport' in 'xcmCommsConfigTable'. See: 'RowStatus'
in IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI
HRX MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsDirRecordRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmCommsDirRecordTable'. Usage: Conforming implementations which support
static rows SHALL support 'active' and 'notInService' writes to this
'xcmCommsDirRecordRowStatus' row status object; and SHALL clear the
'commsDirRecordGroup' bit in 'xcmCommsConfigCreateSupport' in the
'xcmCommsConfigTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmCommsDirRecordRowStatus' row status object; and SHALL set the
'commsDirRecordGroup' bit in 'xcmCommsConfigCreateSupport' in the
'xcmCommsConfigTable'. Usage: Conforming implementations need NOT support
dynamic row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmCommsDirRecordKeyType_Type(XcmCommsDirAttributeType):
    """Custom type xcmCommsDirRecordKeyType based on XcmCommsDirAttributeType"""


_XcmCommsDirRecordKeyType_Object = MibTableColumn
xcmCommsDirRecordKeyType = _XcmCommsDirRecordKeyType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 4),
    _XcmCommsDirRecordKeyType_Type()
)
xcmCommsDirRecordKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyType.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyType.setReference("""\
See: 'XcmCommsDirAttributeType' in the XCMI CC TC 'xcmCommsDirAttributeType' in
this XCMI CC MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyType.setDescription("""\
A directory record key attribute type, used to specify a primary key attribute
for sorting this directory record, or 'unknown' if no primary key attribute is
specified. Usage: The 'Relative Distinguished Name' (RDN) of this directory
record is the tuple of the directory record type, the key attribute type, and
the key attribute value.
""")
_XcmCommsDirRecordKeyInteger_Type = Integer32
_XcmCommsDirRecordKeyInteger_Object = MibTableColumn
xcmCommsDirRecordKeyInteger = _XcmCommsDirRecordKeyInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 5),
    _XcmCommsDirRecordKeyInteger_Type()
)
xcmCommsDirRecordKeyInteger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyInteger.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyInteger.setReference("""\
See: 'xcmCommsDirRecordKeyType' in this XCMI CC MIB 'xcmCommsDirAttributeValue'
in this XCMI CC MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyInteger.setDescription("""\
A directory record key attribute integer value, used to specify a primary key
attribute for sorting this directory record, or zero ('0') if no primary key
attribute is specified. Usage: The 'Relative Distinguished Name' (RDN) of this
directory record is the tuple of the directory record type, the key attribute
type, and the key attribute value.
""")


class _XcmCommsDirRecordKeyString_Type(XcmFixedLocaleUtf8String):
    """Custom type xcmCommsDirRecordKeyString based on XcmFixedLocaleUtf8String"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleUtf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsDirRecordKeyString_Type.__name__ = "XcmFixedLocaleUtf8String"
_XcmCommsDirRecordKeyString_Object = MibTableColumn
xcmCommsDirRecordKeyString = _XcmCommsDirRecordKeyString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 6),
    _XcmCommsDirRecordKeyString_Type()
)
xcmCommsDirRecordKeyString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyString.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyString.setReference("""\
See: 'xcmCommsDirRecordKeyType' in this XCMI CC MIB 'xcmCommsDirStringValue' in
this XCMI CC MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsDirRecordKeyString.setDescription("""\
A directory record key attribute string value, used to specify a primary key
attribute for sorting this directory record, or zero ('0') if no primary key
attribute is specified. Usage: String-valued directory attributes SHALL be
specified as UTF-8 encoded Unicode (ISO 10646) strings. Usage: The 'Relative
Distinguished Name' (RDN) of this directory record is the tuple of the
directory record type, the key attribute type, and the key attribute value.
""")


class _XcmCommsDirRecordParentType_Type(XcmCommsDirRecordType):
    """Custom type xcmCommsDirRecordParentType based on XcmCommsDirRecordType"""


_XcmCommsDirRecordParentType_Object = MibTableColumn
xcmCommsDirRecordParentType = _XcmCommsDirRecordParentType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 7),
    _XcmCommsDirRecordParentType_Type()
)
xcmCommsDirRecordParentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordParentType.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirRecordParentType.setReference("""\
See: 'xcmCommsDirRecordType' in this XCMI CC MIB 'xcmCommsDirRecordIndex' in
this XCMI CC MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsDirRecordParentType.setDescription("""\
A parent directory record type, used to identify the parent directory record
(superior to this directory record), or 'unknown' if no parent directory record
is specified. Usage: Supports hierarchical directory structures. Usage: The
'Fully Qualified Distinguished Name' (FQDN) of this directory record is the
concatentation of the RDN (record key) of this directory record with the RDNs
of all superior directory records to the 'top' (highest node).
""")
_XcmCommsDirRecordParentIndex_Type = Cardinal32
_XcmCommsDirRecordParentIndex_Object = MibTableColumn
xcmCommsDirRecordParentIndex = _XcmCommsDirRecordParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 5, 2, 1, 8),
    _XcmCommsDirRecordParentIndex_Type()
)
xcmCommsDirRecordParentIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirRecordParentIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirRecordParentIndex.setReference("""\
See: 'xcmCommsDirRecordType' in this XCMI CC MIB 'xcmCommsDirRecordIndex' in
this XCMI CC MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsDirRecordParentIndex.setDescription("""\
A parent directory record index, used to identify the parent directory record
(superior to this directory record), or zero ('0') if no parent directory
record is specified. Usage: Supports hierarchical directory structures. Usage:
The 'Fully Qualified Distinguished Name' (FQDN) of this directory record is the
concatentation of the RDN (record key) of this directory record with the RDNs
of all superior directory records to the 'top' (highest node).
""")
_XcmCommsDirAttribute_ObjectIdentity = ObjectIdentity
xcmCommsDirAttribute = _XcmCommsDirAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6)
)
_XcmCommsDirAttributeTable_Object = MibTable
xcmCommsDirAttributeTable = _XcmCommsDirAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2)
)
if mibBuilder.loadTexts:
    xcmCommsDirAttributeTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeTable.setDescription("""\
A table containing integer-valued directory attributes configured on this host
system. Usage: Table contains an entry for all integer-valued and string-valued
attributes configured on this host system.
""")
_XcmCommsDirAttributeEntry_Object = MibTableRow
xcmCommsDirAttributeEntry = _XcmCommsDirAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2, 1)
)
xcmCommsDirAttributeEntry.setIndexNames(
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordType"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordIndex"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeType"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsDirAttributeEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeEntry.setDescription("""\
An entry for an integer-valued directory attribute configured on this host
system.
""")
_XcmCommsDirAttributeType_Type = XcmCommsDirAttributeType
_XcmCommsDirAttributeType_Object = MibTableColumn
xcmCommsDirAttributeType = _XcmCommsDirAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2, 1, 1),
    _XcmCommsDirAttributeType_Type()
)
xcmCommsDirAttributeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeType.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeType.setReference("""\
See: 'XcmCommsDirAttributeType' in the XCMI CC TC 'XcmCommsStackExtProtocol' in
the XCMI Comms Engine TC.
""")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeType.setDescription("""\
A directory attribute type, used to uniquely identify this integer-valued
directory attribute (and also any matching string-valued directory attribute in
'xcmCommsDirStringTable'), when combined with 'xcmCommsDirAttributeIndex'
(below). Usage: When directory attribute type indicates integer-valued, the
value of 'xcmCommsDirAttributeValue' SHALL be the actual value of this
directory attribute. Usage: When directory attribute type indicates string-
valued, the value of 'xcmCommsDirAttributeValue' SHALL be zero, EXCEPT for a
directory attribute type of 'protocolTyped...', when the protocol type shall be
specified as the integer value. The actual string-valued attribute SHALL be
specified in an exactly matching row of 'xcmCommsDirStringTable'. Usage:
Matching directory attributes (string-valued) SHALL be specified in an exactly
matching row of 'xcmCommsDirStringTable'. Matching rows have EXACTLY the SAME
values of 'xcmCommsDirRecordType', 'xcmCommsDirRecordIndex',
'xcmCommsDirAttributeType', and 'xcmCommsDirAttributeIndex'. Usage: Parallel
directory attributes (peers of this one) SHALL be specified in parallel (NOT
matching) rows of 'xcmCommsDirAttributeTable' (integer-valued attributes) or
'xcmCommsDirStringTable' (string-valued attributes). Parallel rows have EXACTLY
the SAME values of 'xcmCommsDirRecordType', 'xcmCommsDirRecordIndex', and
'xcmCommsDirAttributeIndex', but MUST have a DIFFERENT value of
'xcmCommsDirAttributeType'. Usage: When directory attribute type is
'protocolTyped...' the particular protocol layer SHALL be specified by placing
a a value from the enumeration 'XcmCommsStackExtProtocol' in
'xcmCommsDirAttributeValue' for this row.
""")
_XcmCommsDirAttributeIndex_Type = Ordinal32
_XcmCommsDirAttributeIndex_Object = MibTableColumn
xcmCommsDirAttributeIndex = _XcmCommsDirAttributeIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2, 1, 2),
    _XcmCommsDirAttributeIndex_Type()
)
xcmCommsDirAttributeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeIndex.setDescription("""\
A directory attribute index, used to uniquely identify this integer-valued
directory attribute (and also any matching string-valued directory attribute in
'xcmCommsDirStringTable'), when combined with 'xcmCommsDirAttributeType'
(above). Usage: This directory attribute index SHALL be unique for each
attribute subordinate to one directory record (ie, rows with EXACTLY the SAME
values of 'xcmCommsDirRecordType' and 'xcmCommsDirRecordIndex'). EXCEPT when
two or more different directory attributes are 'parallel'; then they SHALL have
EXACTLY the SAME value of 'xcmCommsDirAttributeIndex'. Example: The following
example illustrates the use of 'parallel' directory attributes in a 'speed
dial' entry. (Index values are shown in square brackets, for clarity.) -- Speed
Dial record (specifying sort key of user full name) [xcmCommsDirRecordType =
recordSpeedDial] [xcmCommsDirRecordIndex = 1] xcmCommsDirRecordRowStatus =
active xcmCommsDirRecordKeyType = userFullName (sort key)
xcmCommsDirRecordKeyInteger = 0 (unused) xcmCommsDirRecordKeyString = 'Fred
Flintstone' (sort key) -- String-valued attribute (user location)
[xcmCommsDirRecordType = recordSpeedDial] [xcmCommsDirRecordIndex = 1]
[xcmCommsDirAttributeType = userLocation] [xcmCommsDirAttributeIndex = 1]
xcmCommsDirAttributeRowStatus = active xcmCommsDirAttributeValue = 0 (unused)
xcmCommsDirStringRowStatus = active xcmCommsDirStringValue = 'Bldg 705, H-18'
-- String-valued attribute (primary FAX address) [xcmCommsDirRecordType =
recordSpeedDial] [xcmCommsDirRecordIndex = 1] [xcmCommsDirAttributeType =
protocolTypedAddress] [xcmCommsDirAttributeIndex = 2]
xcmCommsDirAttributeRowStatus = active xcmCommsDirAttributeValue = osiwanFax
(FAX protocol type) xcmCommsDirStringRowStatus = active xcmCommsDirStringValue
= '0+...' (FAX phone number) -- Integer-valued attribute (primary FAX highest
priority) [xcmCommsDirRecordType = recordSpeedDial] [xcmCommsDirRecordIndex =
1] [xcmCommsDirAttributeType = protocolPriority] [xcmCommsDirAttributeIndex =
2] (parallel attribute) xcmCommsDirAttributeRowStatus = active
xcmCommsDirAttributeValue = 100 (highest priority) -- Integer-valued attribute
(primary FAX max retries) [xcmCommsDirRecordType = recordSpeedDial]
[xcmCommsDirRecordIndex = 1] [xcmCommsDirAttributeType = protocolMaxRetries]
[xcmCommsDirAttributeIndex = 2] (parallel attribute)
xcmCommsDirAttributeRowStatus = active xcmCommsDirAttributeValue = 3 (FAX max
retries) -- Integer-valued attribute (primary FAX retry interval)
[xcmCommsDirRecordType = recordSpeedDial] [xcmCommsDirRecordIndex = 1]
[xcmCommsDirAttributeType = protocolRetryInterval] [xcmCommsDirAttributeIndex =
2] (parallel attribute) xcmCommsDirAttributeRowStatus = active
xcmCommsDirAttributeValue = 10 (FAX retry interval) -- String-valued attribute
(secondary FAX address) [xcmCommsDirRecordType = recordSpeedDial]
[xcmCommsDirRecordIndex = 1] [xcmCommsDirAttributeType = protocolTypedAddress]
[xcmCommsDirAttributeIndex = 3] xcmCommsDirAttributeRowStatus = active
xcmCommsDirAttributeValue = osiwanFax (FAX protocol type)
xcmCommsDirStringRowStatus = active xcmCommsDirStringValue = '0+...' (FAX phone
number) -- Integer-valued attribute (secondary FAX medium priority)
[xcmCommsDirRecordType = recordSpeedDial] [xcmCommsDirRecordIndex = 1]
[xcmCommsDirAttributeType = protocolPriority] [xcmCommsDirAttributeIndex = 3]
(parallel attribute) xcmCommsDirAttributeRowStatus = active
xcmCommsDirAttributeValue = 50 (medium priority) -- String-valued attribute
(tertiary Email address) [xcmCommsDirRecordType = recordSpeedDial]
[xcmCommsDirRecordIndex = 1] [xcmCommsDirAttributeType = protocolTypedAddress]
[xcmCommsDirAttributeIndex = 4] xcmCommsDirAttributeRowStatus = active
xcmCommsDirAttributeValue = internetSMTP (Email protocol)
xcmCommsDirStringRowStatus = active xcmCommsDirStringValue = 'fflint@...'
(Email address) -- Integer-valued attribute (tertiary Email lowest priority)
[xcmCommsDirRecordType = recordSpeedDial] [xcmCommsDirRecordIndex = 1]
[xcmCommsDirAttributeType = protocolPriority] [xcmCommsDirAttributeIndex = 4]
(parallel attribute) xcmCommsDirAttributeRowStatus = active
xcmCommsDirAttributeValue = 1 (lowest priority) Discussion: This example shows
a 'speed dial' directory record with a primary sort key (e.g., for local UI
display ordering) of the destination user's full name ('userFullName'). Also
shown are four sets of 'parallel' directory attributes: a) user location; b)
primary FAX destination (highest priority); c) secondary FAX destination
(medium priority); d) tertiary Email destination (lowest priority). Usage: Each
'parallel' directory attribute in a given set is correlated by the SAME value
of 'xcmCommsDirAttributeIndex'.
""")
_XcmCommsDirAttributeRowStatus_Type = RowStatus
_XcmCommsDirAttributeRowStatus_Object = MibTableColumn
xcmCommsDirAttributeRowStatus = _XcmCommsDirAttributeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2, 1, 3),
    _XcmCommsDirAttributeRowStatus_Type()
)
xcmCommsDirAttributeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeRowStatus.setReference("""\
See: 'xcmCommsConfigCreateSupport' in 'xcmCommsConfigTable'. See: 'RowStatus'
in IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI
HRX MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmCommsDirAttributeTable'. Usage: Conforming implementations which support
static rows SHALL support 'active' and 'notInService' writes to this
'xcmCommsDirAttributeRowStatus' row status object; and SHALL clear the
'commsDirAttributeGroup' bit in 'xcmCommsConfigCreateSupport' in the
'xcmCommsConfigTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmCommsDirAttributeRowStatus' row status object; and SHALL set the
'commsDirAttributeGroup' bit in 'xcmCommsConfigCreateSupport' in the
'xcmCommsConfigTable'. Usage: Conforming implementations need NOT support
dynamic row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")
_XcmCommsDirAttributeValue_Type = Integer32
_XcmCommsDirAttributeValue_Object = MibTableColumn
xcmCommsDirAttributeValue = _XcmCommsDirAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 6, 2, 1, 4),
    _XcmCommsDirAttributeValue_Type()
)
xcmCommsDirAttributeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeValue.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeValue.setReference("""\
See: 'xcmCommsDirAttributeType' in this XCMI CC MIB 'XcmCommsDirAttributeType'
in the XCMI CC TC 'XcmCommsStackExtProtocol' in the XCMI Comms Engine TC.
""")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeValue.setDescription("""\
A directory attribute value, the contents of this integer-valued directory
attribute, or zero if 'xcmCommsDirAttributeType' indicates string-valued, and
is NOT 'protocolTyped...'. Usage: When directory attribute type is
'protocolTyped...' the particular protocol layer SHALL be specified by placing
a a value from the enumeration 'XcmCommsStackExtProtocol' in
'xcmCommsDirAttributeValue' for this row.
""")
_XcmCommsDirString_ObjectIdentity = ObjectIdentity
xcmCommsDirString = _XcmCommsDirString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 7)
)
_XcmCommsDirStringTable_Object = MibTable
xcmCommsDirStringTable = _XcmCommsDirStringTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 7, 2)
)
if mibBuilder.loadTexts:
    xcmCommsDirStringTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirStringTable.setDescription("""\
A table containing string-valued directory attributes configured on this host
system. Usage: Table contains an entry for ONLY string-valued and configured on
this host system.
""")
_XcmCommsDirStringEntry_Object = MibTableRow
xcmCommsDirStringEntry = _XcmCommsDirStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 7, 2, 1)
)
xcmCommsDirStringEntry.setIndexNames(
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordType"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordIndex"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeType"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsDirStringEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirStringEntry.setDescription("""\
An entry containing string-valued directory attributes configured on this host
system.
""")
_XcmCommsDirStringRowStatus_Type = RowStatus
_XcmCommsDirStringRowStatus_Object = MibTableColumn
xcmCommsDirStringRowStatus = _XcmCommsDirStringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 7, 2, 1, 1),
    _XcmCommsDirStringRowStatus_Type()
)
xcmCommsDirStringRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirStringRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirStringRowStatus.setReference("""\
See: 'xcmCommsConfigCreateSupport' in 'xcmCommsConfigTable'. See: 'RowStatus'
in IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI
HRX MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsDirStringRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmCommsDirStringTable'. Usage: Conforming implementations which support
static rows SHALL support 'active' and 'notInService' writes to this
'xcmCommsDirStringRowStatus' row status object; and SHALL clear the
'commsDirStringGroup' bit in 'xcmCommsConfigCreateSupport' in the
'xcmCommsConfigTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmCommsDirStringRowStatus' row status object; and SHALL set the
'commsDirStringGroup' bit in 'xcmCommsConfigCreateSupport' in the
'xcmCommsConfigTable'. Usage: Conforming implementations need NOT support
dynamic row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmCommsDirStringValue_Type(XcmFixedLocaleUtf8String):
    """Custom type xcmCommsDirStringValue based on XcmFixedLocaleUtf8String"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleUtf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsDirStringValue_Type.__name__ = "XcmFixedLocaleUtf8String"
_XcmCommsDirStringValue_Object = MibTableColumn
xcmCommsDirStringValue = _XcmCommsDirStringValue_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 7, 2, 1, 2),
    _XcmCommsDirStringValue_Type()
)
xcmCommsDirStringValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsDirStringValue.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirStringValue.setReference("""\
See: 'xcmCommsDirAttributeType' in this XCMI CC MIB 'XcmCommsDirAttributeType'
in the XCMI CC TC.
""")
if mibBuilder.loadTexts:
    xcmCommsDirStringValue.setDescription("""\
A directory attribute value, the contents of this string-valued directory
attribute. Usage: String-valued directory attributes SHALL be specified as
UTF-8 encoded Unicode (ISO 10646) strings. Usage: When directory attribute type
is 'protocolTyped...' the particular protocol layer SHALL be specified by
placing a a value from the enumeration 'XcmCommsStackExtProtocol' in
'xcmCommsDirAttributeValue' for this row. Usage: Conformant implementations
MUST encrypt passwords, keys, and other security information stored in this
string object.
""")
_XcmCommsProtocol_ObjectIdentity = ObjectIdentity
xcmCommsProtocol = _XcmCommsProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 8)
)
_XcmCommsProtocolTable_Object = MibTable
xcmCommsProtocolTable = _XcmCommsProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 8, 2)
)
if mibBuilder.loadTexts:
    xcmCommsProtocolTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsProtocolTable.setDescription("""\
A table of available communications protocol suites and specific communications
protocols on this host system.
""")
_XcmCommsProtocolEntry_Object = MibTableRow
xcmCommsProtocolEntry = _XcmCommsProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 8, 2, 1)
)
xcmCommsProtocolEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-CONFIG-MIB", "xcmCommsProtocolType"),
)
if mibBuilder.loadTexts:
    xcmCommsProtocolEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsProtocolEntry.setDescription("""\
An entry for an available communications protocol suite or specific
communications protocol on this host system.
""")
_XcmCommsProtocolType_Type = XcmCommsStackExtProtocol
_XcmCommsProtocolType_Object = MibTableColumn
xcmCommsProtocolType = _XcmCommsProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 8, 2, 1, 1),
    _XcmCommsProtocolType_Type()
)
xcmCommsProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsProtocolType.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsProtocolType.setReference("""\
See: 'XcmCommsStackExtProtocol' in XCMI Comms Engine TC. See: 'protocolType'
enumeration and 'protocolTyped[Name|Address]' enumerations in
'XcmCommsDirAttributeType' in XCMI CC TC. See: 'xcmCommsDirAttributeType' in
XCMI CC MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsProtocolType.setDescription("""\
The type of an available communications protocol suite or specific
communications protocol on this host system. Usage: To indicate that a
communications protocol suite is available, use a suite value of
'XcmCommsStackExtProtocol', eg, 'internetSuite(140101)' for the Internet suite.
Usage: To indicate that a specific communications protocol is available, use a
specific value of 'XcmCommsStackExtProtocol', eg, 'internetFTP(141504)' for the
Internet FTP protocol.
""")
_XcmCommsProtocolRowStatus_Type = RowStatus
_XcmCommsProtocolRowStatus_Object = MibTableColumn
xcmCommsProtocolRowStatus = _XcmCommsProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 8, 2, 1, 2),
    _XcmCommsProtocolRowStatus_Type()
)
xcmCommsProtocolRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsProtocolRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsProtocolRowStatus.setDescription("""\
This object displays the status of individual conceptual rows in the
'xcmCommsProtocolTable'.
""")

# Managed Objects groups

xcmCommsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 3)
)
xcmCommsConfigGroup.setObjects(
      *(("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigRowStatus"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigActiveOptionFirst"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigActiveOptionLast"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigGroupSupport"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigCreateSupport"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsConfigUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmCommsConfigGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsConfigGroup.setDescription("""\
The Comms Config Group (Communications Configurations).
""")

xcmCommsOptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 4)
)
xcmCommsOptionGroup.setObjects(
      *(("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionRowStatus"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionTypeOID"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueSyntax"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueInteger"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueOID"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueString"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueLocalization"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionValueCodedCharSet"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionNextIndex"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionPreviousIndex"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsOptionFamilyIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsOptionGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsOptionGroup.setDescription("""\
The Comms Option Group (Communications Configuration Options).
""")

xcmCommsDirRecordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 5)
)
xcmCommsDirRecordGroup.setObjects(
      *(("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordRowStatus"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordKeyType"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordKeyInteger"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordKeyString"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordParentType"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirRecordParentIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsDirRecordGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirRecordGroup.setDescription("""\
Directory Record Group.
""")

xcmCommsDirAttributeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 6)
)
xcmCommsDirAttributeGroup.setObjects(
      *(("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeRowStatus"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirAttributeValue"))
)
if mibBuilder.loadTexts:
    xcmCommsDirAttributeGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirAttributeGroup.setDescription("""\
Directory Attribute Group.
""")

xcmCommsDirStringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 7)
)
xcmCommsDirStringGroup.setObjects(
      *(("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirStringRowStatus"),
        ("XEROX-COMMS-CONFIG-MIB", "xcmCommsDirStringValue"))
)
if mibBuilder.loadTexts:
    xcmCommsDirStringGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsDirStringGroup.setDescription("""\
Directory String Group.
""")

xcmCommsProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 2, 8)
)
xcmCommsProtocolGroup.setObjects(
    ("XEROX-COMMS-CONFIG-MIB", "xcmCommsProtocolRowStatus")
)
if mibBuilder.loadTexts:
    xcmCommsProtocolGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsProtocolGroup.setDescription("""\
Comms Protocol Group (available suites and protocols).
""")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xcmCommsConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 64, 2, 3)
)
if mibBuilder.loadTexts:
    xcmCommsConfigMIBCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmCommsConfigMIBCompliance.setDescription("""\
The compliance statements for SNMP management agents that implement the Comms
Config MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-COMMS-CONFIG-MIB",
    **{"xcmCommsConfigZeroDummy": xcmCommsConfigZeroDummy,
       "xcmCommsConfigMIB": xcmCommsConfigMIB,
       "xcmCommsConfigMIBConformance": xcmCommsConfigMIBConformance,
       "xcmCommsConfigMIBGroups": xcmCommsConfigMIBGroups,
       "xcmCommsConfigGroup": xcmCommsConfigGroup,
       "xcmCommsOptionGroup": xcmCommsOptionGroup,
       "xcmCommsDirRecordGroup": xcmCommsDirRecordGroup,
       "xcmCommsDirAttributeGroup": xcmCommsDirAttributeGroup,
       "xcmCommsDirStringGroup": xcmCommsDirStringGroup,
       "xcmCommsProtocolGroup": xcmCommsProtocolGroup,
       "xcmCommsConfigMIBCompliance": xcmCommsConfigMIBCompliance,
       "xcmCommsConfig": xcmCommsConfig,
       "xcmCommsConfigTable": xcmCommsConfigTable,
       "xcmCommsConfigEntry": xcmCommsConfigEntry,
       "xcmCommsConfigRowStatus": xcmCommsConfigRowStatus,
       "xcmCommsConfigActiveOptionFirst": xcmCommsConfigActiveOptionFirst,
       "xcmCommsConfigActiveOptionLast": xcmCommsConfigActiveOptionLast,
       "xcmCommsConfigGroupSupport": xcmCommsConfigGroupSupport,
       "xcmCommsConfigCreateSupport": xcmCommsConfigCreateSupport,
       "xcmCommsConfigUpdateSupport": xcmCommsConfigUpdateSupport,
       "xcmCommsOption": xcmCommsOption,
       "xcmCommsOptionTable": xcmCommsOptionTable,
       "xcmCommsOptionEntry": xcmCommsOptionEntry,
       "xcmCommsOptionIndex": xcmCommsOptionIndex,
       "xcmCommsOptionRowStatus": xcmCommsOptionRowStatus,
       "xcmCommsOptionTypeOID": xcmCommsOptionTypeOID,
       "xcmCommsOptionValueSyntax": xcmCommsOptionValueSyntax,
       "xcmCommsOptionValueInteger": xcmCommsOptionValueInteger,
       "xcmCommsOptionValueOID": xcmCommsOptionValueOID,
       "xcmCommsOptionValueString": xcmCommsOptionValueString,
       "xcmCommsOptionValueLocalization": xcmCommsOptionValueLocalization,
       "xcmCommsOptionValueCodedCharSet": xcmCommsOptionValueCodedCharSet,
       "xcmCommsOptionNextIndex": xcmCommsOptionNextIndex,
       "xcmCommsOptionPreviousIndex": xcmCommsOptionPreviousIndex,
       "xcmCommsOptionFamilyIndex": xcmCommsOptionFamilyIndex,
       "xcmCommsDirRecord": xcmCommsDirRecord,
       "xcmCommsDirRecordTable": xcmCommsDirRecordTable,
       "xcmCommsDirRecordEntry": xcmCommsDirRecordEntry,
       "xcmCommsDirRecordType": xcmCommsDirRecordType,
       "xcmCommsDirRecordIndex": xcmCommsDirRecordIndex,
       "xcmCommsDirRecordRowStatus": xcmCommsDirRecordRowStatus,
       "xcmCommsDirRecordKeyType": xcmCommsDirRecordKeyType,
       "xcmCommsDirRecordKeyInteger": xcmCommsDirRecordKeyInteger,
       "xcmCommsDirRecordKeyString": xcmCommsDirRecordKeyString,
       "xcmCommsDirRecordParentType": xcmCommsDirRecordParentType,
       "xcmCommsDirRecordParentIndex": xcmCommsDirRecordParentIndex,
       "xcmCommsDirAttribute": xcmCommsDirAttribute,
       "xcmCommsDirAttributeTable": xcmCommsDirAttributeTable,
       "xcmCommsDirAttributeEntry": xcmCommsDirAttributeEntry,
       "xcmCommsDirAttributeType": xcmCommsDirAttributeType,
       "xcmCommsDirAttributeIndex": xcmCommsDirAttributeIndex,
       "xcmCommsDirAttributeRowStatus": xcmCommsDirAttributeRowStatus,
       "xcmCommsDirAttributeValue": xcmCommsDirAttributeValue,
       "xcmCommsDirString": xcmCommsDirString,
       "xcmCommsDirStringTable": xcmCommsDirStringTable,
       "xcmCommsDirStringEntry": xcmCommsDirStringEntry,
       "xcmCommsDirStringRowStatus": xcmCommsDirStringRowStatus,
       "xcmCommsDirStringValue": xcmCommsDirStringValue,
       "xcmCommsProtocol": xcmCommsProtocol,
       "xcmCommsProtocolTable": xcmCommsProtocolTable,
       "xcmCommsProtocolEntry": xcmCommsProtocolEntry,
       "xcmCommsProtocolType": xcmCommsProtocolType,
       "xcmCommsProtocolRowStatus": xcmCommsProtocolRowStatus}
)

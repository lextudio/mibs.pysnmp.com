"""SNMP MIB module (XEROX-GENERAL-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-GENERAL-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:11 2024
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

(ProductID,
 hrDeviceIndex,
 InternationalDisplayString) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "ProductID",
    "hrDeviceIndex",
    "InternationalDisplayString")

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

(iso,
 Unsigned32,
 Counter64,
 ObjectIdentity,
 Integer32,
 Bits,
 Gauge32,
 ModuleIdentity,
 NotificationType,
 MibIdentifier,
 Counter32,
 TimeTicks,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 IpAddress) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "iso",
    "Unsigned32",
    "Counter64",
    "ObjectIdentity",
    "Integer32",
    "Bits",
    "Gauge32",
    "ModuleIdentity",
    "NotificationType",
    "MibIdentifier",
    "Counter32",
    "TimeTicks",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "IpAddress")

(TruthValue,
 TextualConvention,
 DisplayString,
 DateAndTime,
 RowStatus) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TruthValue",
    "TextualConvention",
    "DisplayString",
    "DateAndTime",
    "RowStatus")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(CodedLanguage,
 Ordinal32,
 XcmGenNotifyTrainingFilter,
 XcmGlobalUniqueID,
 XcmGenReconfOptionState,
 XcmGenRowPersistence,
 XcmGenOptionValueSyntax,
 zeroDotZero,
 XcmNamedLocaleUtf8String,
 Cardinal32,
 CodedCountry,
 XcmGenSNMPv2ErrorStatus,
 XcmGenNotifySchemeSupport,
 XcmGenNotifyDetailType,
 CodeIndexedStringIndex,
 XcmFixedLocaleDisplayString,
 XcmGenNotifySeverityFilter,
 XcmGenSNMPVersion,
 XcmGenGroupSupport,
 Ordinal16,
 XcmGenMessageMapStringLabel,
 XcmGenSNMPDomain) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "CodedLanguage",
    "Ordinal32",
    "XcmGenNotifyTrainingFilter",
    "XcmGlobalUniqueID",
    "XcmGenReconfOptionState",
    "XcmGenRowPersistence",
    "XcmGenOptionValueSyntax",
    "zeroDotZero",
    "XcmNamedLocaleUtf8String",
    "Cardinal32",
    "CodedCountry",
    "XcmGenSNMPv2ErrorStatus",
    "XcmGenNotifySchemeSupport",
    "XcmGenNotifyDetailType",
    "CodeIndexedStringIndex",
    "XcmFixedLocaleDisplayString",
    "XcmGenNotifySeverityFilter",
    "XcmGenSNMPVersion",
    "XcmGenGroupSupport",
    "Ordinal16",
    "XcmGenMessageMapStringLabel",
    "XcmGenSNMPDomain")


# MODULE-IDENTITY

xcmGeneralMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51)
)
xcmGeneralMIB.setLastUpdated("0504240000Z")
if mibBuilder.loadTexts:
    xcmGeneralMIB.setOrganization("""\
Xerox Corporation - XCMI Working Group
""")
xcmGeneralMIB.setContactInfo("""\
 XCMI Editors E-Mail: coherence@crt.xerox.com -- --
""")
if mibBuilder.loadTexts:
    xcmGeneralMIB.setDescription("""\
 Version: 5.402.pub Xerox General MIB See section 9 'Supplement' of XCMI
General TC for implementation and conformance guidance for this MIB module.
Copyright (C) 1995-2005 Xerox Corporation. All Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmGenZeroDummy_ObjectIdentity = ObjectIdentity
xcmGenZeroDummy = _XcmGenZeroDummy_ObjectIdentity(
    (0, 0, 51)
)
_XcmGenBase_ObjectIdentity = ObjectIdentity
xcmGenBase = _XcmGenBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1)
)
_XcmGenBaseTable_Object = MibTable
xcmGenBaseTable = _XcmGenBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2)
)
if mibBuilder.loadTexts:
    xcmGenBaseTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseTable.setDescription("""\
 A table of general counters and capabilities for ease of use of the XCMI
General MIB on this host system. Usage: The ONLY valid row in the
'xcmGenBaseTable' SHALL have an 'xcmGenBaseIndex' of one ('1').
""")
_XcmGenBaseEntry_Object = MibTableRow
xcmGenBaseEntry = _XcmGenBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1)
)
xcmGenBaseEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenBaseIndex"),
)
if mibBuilder.loadTexts:
    xcmGenBaseEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseEntry.setDescription("""\
 An entry of general counters and capabilities for ease of use of the XCMI
General MIB on this host system. Usage: The ONLY valid row in the
'xcmGenBaseTable' SHALL have an 'xcmGenBaseIndex' of one ('1').
""")
_XcmGenBaseIndex_Type = Ordinal32
_XcmGenBaseIndex_Object = MibTableColumn
xcmGenBaseIndex = _XcmGenBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 1),
    _XcmGenBaseIndex_Type()
)
xcmGenBaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenBaseIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseIndex.setDescription("""\
 A unique value used by this host system to identify this conceptual row in the
'xcmGenBaseTable'. Usage: The ONLY valid row in the 'xcmGenBaseTable' SHALL
have an 'xcmGenBaseIndex' of one ('1').
""")
_XcmGenBaseRowStatus_Type = RowStatus
_XcmGenBaseRowStatus_Object = MibTableColumn
xcmGenBaseRowStatus = _XcmGenBaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 2),
    _XcmGenBaseRowStatus_Type()
)
xcmGenBaseRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseRowStatus.setDescription("""\
 This object is used to display status of the ONLY valid conceptual row in the
'xcmGenBaseTable'. Usage: 'xcmGenBaseRowStatus' is 'read-only' because the ONLY
valid conceptual row SHALL NOT be deleted.
""")
_XcmGenBaseSystemHrDeviceIndex_Type = Cardinal32
_XcmGenBaseSystemHrDeviceIndex_Object = MibTableColumn
xcmGenBaseSystemHrDeviceIndex = _XcmGenBaseSystemHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 3),
    _XcmGenBaseSystemHrDeviceIndex_Type()
)
xcmGenBaseSystemHrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseSystemHrDeviceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseSystemHrDeviceIndex.setReference("""\
 See: 'hrDeviceIndex' in the Device group of the IETF Host Resources MIB (RFC
2790). See: 'xcmHrStoragePlatformDeviceIndex' in the Storage Ext group of the
XCMI Host Resources Ext MIB.
""")
if mibBuilder.loadTexts:
    xcmGenBaseSystemHrDeviceIndex.setDescription("""\
 The value of 'hrDeviceIndex' corresponding to the platform associated
conceptual row in the 'hrDeviceTable' representing the CPU device (of type
'hrDeviceProcessor'), which currently supports the executing process/thread of
this management agent.
""")


class _XcmGenBaseGroupSupport_Type(XcmGenGroupSupport):
    """Custom type xcmGenBaseGroupSupport based on XcmGenGroupSupport"""
    defaultValue = 3584


_XcmGenBaseGroupSupport_Object = MibTableColumn
xcmGenBaseGroupSupport = _XcmGenBaseGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 4),
    _XcmGenBaseGroupSupport_Type()
)
xcmGenBaseGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseGroupSupport.setDescription("""\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI General MIB object groups which are supported by this management
agent implementation (ie, version) on this host system, specified in a bit-
mask. Usage: Conforming management agents SHALL accurately report their support
for the XCMI General MIB object groups.
""")


class _XcmGenBaseGroupCreateSupport_Type(XcmGenGroupSupport):
    """Custom type xcmGenBaseGroupCreateSupport based on XcmGenGroupSupport"""
    defaultValue = 1536


_XcmGenBaseGroupCreateSupport_Object = MibTableColumn
xcmGenBaseGroupCreateSupport = _XcmGenBaseGroupCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 5),
    _XcmGenBaseGroupCreateSupport_Type()
)
xcmGenBaseGroupCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseGroupCreateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseGroupCreateSupport.setDescription("""\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI General MIB object groups which are supported for dynamic row
creation (via '...RowStatus') by this management agent implementation (ie,
version) on this host system, specified in a bit-mask. Usage: Conforming
management agents SHALL accurately report their support for the XCMI General
MIB object groups.
""")


class _XcmGenBaseGroupUpdateSupport_Type(XcmGenGroupSupport):
    """Custom type xcmGenBaseGroupUpdateSupport based on XcmGenGroupSupport"""
    defaultValue = 3584


_XcmGenBaseGroupUpdateSupport_Object = MibTableColumn
xcmGenBaseGroupUpdateSupport = _XcmGenBaseGroupUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 6),
    _XcmGenBaseGroupUpdateSupport_Type()
)
xcmGenBaseGroupUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseGroupUpdateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseGroupUpdateSupport.setDescription("""\
 The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI General MIB object groups which are supported for existing row
update (via SNMP Set-Request PDUs) by this management agent implementation (ie,
version) on this host system, specified in a bit-mask. Usage: Conforming
management agents SHALL accurately report their support for the XCMI General
MIB object groups.
""")
_XcmGenBaseClientDataMaxSupport_Type = Cardinal32
_XcmGenBaseClientDataMaxSupport_Object = MibTableColumn
xcmGenBaseClientDataMaxSupport = _XcmGenBaseClientDataMaxSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 7),
    _XcmGenBaseClientDataMaxSupport_Type()
)
xcmGenBaseClientDataMaxSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseClientDataMaxSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseClientDataMaxSupport.setReference("""\
 See: 'xcmGenClientDataLength'
""")
if mibBuilder.loadTexts:
    xcmGenBaseClientDataMaxSupport.setDescription("""\
 The maximum 'xcmGenClientDataLength' supported for ANY conceptual row in the
'xcmGenClientDataTable'. Usage: Conforming implementations NEED NOT support
maximum 'xcmGenClientDataLength' greater than 1 octet.
""")
_XcmGenBaseOptionSyntaxSupport_Type = Cardinal32
_XcmGenBaseOptionSyntaxSupport_Object = MibTableColumn
xcmGenBaseOptionSyntaxSupport = _XcmGenBaseOptionSyntaxSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 8),
    _XcmGenBaseOptionSyntaxSupport_Type()
)
xcmGenBaseOptionSyntaxSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseOptionSyntaxSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseOptionSyntaxSupport.setReference("""\
 See: 'XcmGenOptionValueSyntax' in the XCMI General TC
""")
if mibBuilder.loadTexts:
    xcmGenBaseOptionSyntaxSupport.setDescription("""\
 The 'xcmGenOptionValueSyntax' values supported for ANY conceptual row in the
'xcmGenOptionTable'. Usage: Conforming management agents SHALL report their
supported values as a 'bit-mask' formed via the bit-wise OR of '2**(n)', where
(n) is each supported enumerated value in the in the 'XcmGenOptionValueSyntax'
textual convention.
""")
_XcmGenBaseReconfStateSupport_Type = Cardinal32
_XcmGenBaseReconfStateSupport_Object = MibTableColumn
xcmGenBaseReconfStateSupport = _XcmGenBaseReconfStateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 9),
    _XcmGenBaseReconfStateSupport_Type()
)
xcmGenBaseReconfStateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseReconfStateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseReconfStateSupport.setReference("""\
 See: 'XcmGenReconfOptionState' in the XCMI General TC
""")
if mibBuilder.loadTexts:
    xcmGenBaseReconfStateSupport.setDescription("""\
 The 'xcmGenReconfOptionState' values supported for ANY conceptual row in the
'xcmGenReconfTable'. Usage: Conforming management agents SHALL report their
supported values as a 'bit-mask' formed via the bit-wise OR of '2**(n)', where
(n) is each supported enumerated value in the in the 'XcmGenReconfOptionState'
textual convention.
""")
_XcmGenBaseSNMPDomainSupport_Type = Cardinal32
_XcmGenBaseSNMPDomainSupport_Object = MibTableColumn
xcmGenBaseSNMPDomainSupport = _XcmGenBaseSNMPDomainSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 10),
    _XcmGenBaseSNMPDomainSupport_Type()
)
xcmGenBaseSNMPDomainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPDomainSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPDomainSupport.setReference("""\
 See: 'XcmGenSNMPDomain' in the XCMI General TC See:
'xcmGenTrapClientSNMP[Domain|Version]'.
""")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPDomainSupport.setDescription("""\
 This object is used to specify ALL transport domains (address and name spaces)
which are supported by this management agent for SNMP protocol traffic (SNMP
responses, SNMP traps, etc), in ALL versions specified by
'xcmGenBaseSNMPVersionSupport'. This object is also used to allow the
'xcmGenTrapClientTable' to be used with any URI scheme (e.g., 'mailto:') for
notifications, by specifying 'uriNotifyDomain'. Usage: Conforming management
agents SHALL report their supported values as a 'bit-mask' formed via the bit-
wise OR of '2**(n)', where (n) is each supported enumerated value in the in the
'XcmGenSNMPDomain' textual convention.
""")
_XcmGenBaseSNMPTrapSupport_Type = TruthValue
_XcmGenBaseSNMPTrapSupport_Object = MibTableColumn
xcmGenBaseSNMPTrapSupport = _XcmGenBaseSNMPTrapSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 11),
    _XcmGenBaseSNMPTrapSupport_Type()
)
xcmGenBaseSNMPTrapSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPTrapSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPTrapSupport.setReference("""\
 See: 'xcmGenBaseGroupSupport' for 'xcmGenTrapClientTable'
""")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPTrapSupport.setDescription("""\
 This object SHALL be 'true' if this management agent supports SNMP traps (in
any SNMP domain and SNMP version) and MAY support the 'xcmGenTrapClientTable'.
This object SHALL be 'false' if this management agent does NOT support SNMP
traps (in any SNMP domain and SNMP version) and does NOT support the
'xcmGenTrapClientTable'.
""")
_XcmGenBaseSNMPVersionSupport_Type = Cardinal32
_XcmGenBaseSNMPVersionSupport_Object = MibTableColumn
xcmGenBaseSNMPVersionSupport = _XcmGenBaseSNMPVersionSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 12),
    _XcmGenBaseSNMPVersionSupport_Type()
)
xcmGenBaseSNMPVersionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPVersionSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPVersionSupport.setReference("""\
 See: 'XcmGenSNMPVersion' in the XCMI General TC See:
'xcmGenTrapClientSNMP[Domain|Version]'.
""")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPVersionSupport.setDescription("""\
 This object is used to specify ALL SNMP versions (RFC 1157, RFC 1905, etc)
which are supported by this management agent for SNMP protocol traffic (SNMP
responses, SNMP traps, etc), in ALL domains specified by
'xcmGenBaseSNMPDomainSupport'. Usage: Conforming management agents SHALL report
their supported values as a 'bit-mask' formed via the bit-wise OR of '2**(n)',
where (n) is each supported enumerated value in the in the 'XcmGenSNMPVersion'
textual convention.
""")


class _XcmGenBaseSNMPReadCommunity_Type(OctetString):
    """Custom type xcmGenBaseSNMPReadCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmGenBaseSNMPReadCommunity_Type.__name__ = "OctetString"
_XcmGenBaseSNMPReadCommunity_Object = MibTableColumn
xcmGenBaseSNMPReadCommunity = _XcmGenBaseSNMPReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 13),
    _XcmGenBaseSNMPReadCommunity_Type()
)
xcmGenBaseSNMPReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPReadCommunity.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPReadCommunity.setReference("""\
 See: SNMPv1c (RFC 1157) and SNMPv2c (RFC 1905). See: 'Coexistence between
SNMPv1, SNMPv2, and SNMPv3' RFC 2576, March 2000. See:
'xcmGenBaseSNMP[Write|Trap]Community'.
""")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPReadCommunity.setDescription("""\
 This object is used to specify a 'read community name' valid for use in
SNMPv1c and SNMPv2c 'Get|GetNext|GetBulk' PDUs received (SNMP requests) and
generated (SNMP responses) by this management agent. Usage: Note that the
object 'xcmGenBaseSNMPWriteCommunity' SHALL ALSO be used to specify a 'read
community name' valid for use in SNMPv1c and SNMPv2c 'Get|GetNext|GetBulk' PDUs
received (SNMP requests) and generated (SNMP responses) by this management
agent. Note however that the object 'xcmGenBaseSNMPTrapCommunity' SHALL NOT be
used to specify a 'read community name' valid in SNMP 'Get|GetNext|GetBulk'.
Note: XCMI-defined community name objects support 64 octets maximum length and
configurable charsets, for consistency with the 'snmpCommunityName' object
defined in the SNMP Community MIB defined in RFC 2576 (March 2000). Note:
Products MAY ship with a market-specific factory default locale with a charset
other than 'utf-8', eg, in Japan a product might factory default to 'shift-
jis(17)' or 'iso-2022-jp(39)'. Such products MUST implement the
'xcmGenFixedLocalizationTable', to prevent ambiguity about the factory default
charset. Usage: For best interworking with the ('utf-8' charset ONLY) closely
related 'snmpCommunitySecurityName' object in RFC 2576, conforming management
stations and management agents SHOULD NOT configure community names longer than
32 octets. Usage: For best interworking with third-party applications,
conforming management stations and management agents SHOULD NOT configure empty
(zero-length or all spaces) community names. Usage: All XCMI conforming
management agents SHALL treat a valid 'write community name' as a valid 'read
community name' and SHALL NOT increment 'snmpInBadCommunityNames' (unknown
name) or 'snmpInBadCommunityUses' (wrong community name for operation) counters
in the SNMPv2 Agent MIB (RFC 1907). Usage: All XCMI conforming management
agents are STRONGLY RECOMMENDED to support an authenticated SNMP SetRequest to
this object, changing the system 'read community name' (for best interworking
with third-party management stations). Usage: All XCMI conforming management
agents: a) SHALL return a zero length string in response to an SNMP GetRequest
of this object; b) are STRONGLY RECOMMENDED to default this object to the
string 'public' (in the static charset); and c) MAY support multiple valid
'read community names' (by using 'xcmGenBaseReadCommunity' as a 'window' to a
community list via 'device[Set|List]' device operations in the Device Mgmt
group of the XCMI Host Resources Ext MIB). Usage: This object is of type
'XcmFixedLocaleDisplayString', with an (opaque) locale and an explicit charset
which is specified in the 'xcmGenLocalizationCharSet' object indexed by
'hrDeviceIndex' per 'xcmGenBaseSystemHrDeviceIndex' and
'xcmGenLocalizationIndex' per 'xcmGenFixedLocalizationIndex'. If
'xcmGenLocalizationTable' or 'xcmGenFixedLocalizationTable' are not implemented
on this host system, then the charset SHALL be 'utf-8(106)', ISO 10646-1 in
'UTF-8' stream encoding. Usage: All XCMI conforming management agents SHALL
allow any defined character in the configured charset of this object. All XCMI
conforming management stations SHOULD NOT write control characters or other
non-display characters into this object. WARNING: Changing the only valid 'read
community name' of an SNMP management agent will cause a COMPLETE loss of
communications unless all associated SNMP management stations (clients) ALSO
change over to the new 'read community name'!!!
""")


class _XcmGenBaseSNMPWriteCommunity_Type(OctetString):
    """Custom type xcmGenBaseSNMPWriteCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmGenBaseSNMPWriteCommunity_Type.__name__ = "OctetString"
_XcmGenBaseSNMPWriteCommunity_Object = MibTableColumn
xcmGenBaseSNMPWriteCommunity = _XcmGenBaseSNMPWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 14),
    _XcmGenBaseSNMPWriteCommunity_Type()
)
xcmGenBaseSNMPWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPWriteCommunity.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPWriteCommunity.setReference("""\
 See: SNMPv1c (RFC 1157) and SNMPv2c (RFC 1905). See: 'Coexistence between
SNMPv1, SNMPv2, and SNMPv3' RFC 2576, March 2000. See:
'xcmGenBaseSNMP[Read|Trap]Community'.
""")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPWriteCommunity.setDescription("""\
 This object is used to specify a 'write community name' valid for use in
SNMPv1c and SNMPv2c 'Set' PDUs received (SNMP requests) and generated (SNMP
responses) by this management agent. Usage: Note that the object
'xcmGenBaseSNMPWriteCommunity' SHALL ALSO be used to specify a 'read community
name' valid for use in SNMPv1c and SNMPv2c 'Get|GetNext|GetBulk' PDUs received
(SNMP requests) and generated (SNMP responses) by this management agent. Note
however that the object 'xcmGenBaseSNMPTrapCommunity' SHALL NOT be used to
specify a 'read community name' valid in SNMP 'Get|GetNext|GetBulk'. Usage: All
XCMI conforming management agents SHALL treat a valid 'write community name' as
a valid 'read community name' and SHALL NOT increment 'snmpInBadCommunityNames'
(unknown name) or 'snmpInBadCommunityUses' (wrong community name for operation)
counters in the SNMPv2 Agent MIB (RFC 1907). Note: XCMI-defined community name
objects support 64 octets maximum length and configurable charsets, for
consistency with the 'snmpCommunityName' object defined in the SNMP Community
MIB defined in RFC 2576 (March 2000). Note: Products MAY ship with a market-
specific factory default locale with a charset other than 'utf-8', eg, in Japan
a product might factory default to 'shift-jis(17)' or 'iso-2022-jp(39)'. Such
products MUST implement the 'xcmGenFixedLocalizationTable', to prevent
ambiguity about the factory default charset. Usage: For best interworking with
the ('utf-8' charset ONLY) closely related 'snmpCommunitySecurityName' object
in RFC 2576, conforming management stations and management agents SHOULD NOT
configure community names longer than 32 octets. Usage: For best interworking
with third-party applications, conforming management stations and management
agents SHOULD NOT configure empty (zero-length or all spaces) community names.
Usage: All XCMI conforming management agents are STRONGLY RECOMMENDED to
support an authenticated SNMP SetRequest to this object, changing the system
'write community name' (for best interworking with third-party management
stations). Usage: All XCMI conforming management agents: a) SHALL return a zero
length string in response to an SNMP GetRequest of this object; b) are STRONGLY
RECOMMENDED to default this object to the string 'public' (in the static
charset); and c) MAY support multiple valid 'write community names' (by using
'xcmGenBaseWriteCommunity' as a 'window' to a community list via
'device[Set|List]' device operations in the Device Mgmt group of the XCMI Host
Resources Ext MIB). Usage: This object is of type 'XcmFixedLocaleDisplayString'
(see DESCRIPTION of 'xcmGenBaseSNMPReadCommunity' above). If
'xcmGenLocalizationTable' or 'xcmGenFixedLocalizationTable' are not implemented
on this host system, then the charset SHALL be 'utf-8(106)', ISO 10646-1 in
'UTF-8' stream encoding. Usage: All XCMI conforming management agents SHALL
allow any defined character in the configured charset of this object. All XCMI
conforming management stations SHOULD NOT write control characters or other
non-display characters into this object. Usage: When an SNMP management
stations CHANGES the value of this 'write community name', an XCMI conforming
management agent SHALL use the old (previous) 'write community name' when
generating the SNMP response to the 'Set' PDU, for consistency. WARNING:
Changing the only valid 'write community name' of an SNMP management agent will
cause a COMPLETE loss of communications unless all associated SNMP management
stations (clients) ALSO change over to the new 'write community name'!!!
""")


class _XcmGenBaseSNMPTrapCommunity_Type(OctetString):
    """Custom type xcmGenBaseSNMPTrapCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmGenBaseSNMPTrapCommunity_Type.__name__ = "OctetString"
_XcmGenBaseSNMPTrapCommunity_Object = MibTableColumn
xcmGenBaseSNMPTrapCommunity = _XcmGenBaseSNMPTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 15),
    _XcmGenBaseSNMPTrapCommunity_Type()
)
xcmGenBaseSNMPTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPTrapCommunity.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPTrapCommunity.setReference("""\
 See: SNMPv1c (RFC 1157) and SNMPv2c (RFC 1905). See: 'Coexistence between
SNMPv1, SNMPv2, and SNMPv3' RFC 2576, March 2000. See:
'xcmGenBaseSNMP[Read|Write]Community'. See: 'xcmGenTrapClientSNMPCommunity'.
""")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPTrapCommunity.setDescription("""\
 This object is used to specify a 'trap community name' valid for use in
SNMPv1c and SNMPv2c 'Inform|Trap' PDUs received (SNMP requests) and generated
(SNMP traps) by this management agent. Usage: Note that the object
'xcmGenBaseSNMPWriteCommunity' SHALL ALSO be used to specify a 'read community
name' valid for use in SNMPv1c and SNMPv2c 'Get|GetNext|GetBulk' PDUs received
(SNMP requests) and generated (SNMP responses) by this management agent. Note
however that the object 'xcmGenBaseSNMPTrapCommunity' SHALL NOT be used to
specify a 'read community name' valid in SNMP 'Get|GetNext|GetBulk'. Note:
XCMI-defined community name objects support 64 octets maximum length and
configurable charsets, for consistency with the 'snmpCommunityName' object
defined in the SNMP Community MIB defined in RFC 2576 (March 2000). Note:
Products MAY ship with a market-specific factory default locale with a charset
other than 'utf-8', eg, in Japan a product might factory default to 'shift-
jis(17)' or 'iso-2022-jp(39)'. Such products MUST implement the
'xcmGenFixedLocalizationTable', to prevent ambiguity about the factory default
charset. Usage: For best interworking with the ('utf-8' charset ONLY) closely
related 'snmpCommunitySecurityName' object in RFC 2576, conforming management
stations and management agents SHOULD NOT configure community names longer than
32 octets. Usage: For best interworking with third-party applications,
conforming management stations and management agents SHOULD NOT configure empty
(zero-length or all spaces) community names. Usage: All XCMI conforming
management agents are STRONGLY RECOMMENDED to support an authenticated SNMP
SetRequest to this object, changing the system 'trap community name' (for best
interworking with third-party management stations). Usage: All XCMI conforming
management agents: a) SHALL return a zero length string in response to an SNMP
GetRequest of this object; b) are STRONGLY RECOMMENDED to default this object
to the string 'public' (in the static charset); and c) MAY support multiple
valid 'trap community names' (by using 'xcmGenBaseTrapCommunity' as a 'window'
to a community list via 'device[Set|List]' device operations in the Device Mgmt
group of the XCMI Host Resources Ext MIB). Usage: This object is of type
'XcmFixedLocaleDisplayString' (see DESCRIPTION of 'xcmGenBaseSNMPReadCommunity'
above). If 'xcmGenLocalizationTable' or 'xcmGenFixedLocalizationTable' are not
implemented on this host system, then the charset SHALL be 'utf-8(106)', ISO
10646-1 in 'UTF-8' stream encoding. Usage: All XCMI conforming management
agents SHALL allow any defined character in the configured charset of this
object. All XCMI conforming management stations SHOULD NOT write control
characters or other non-display characters into this object. WARNING: Changing
the only valid 'trap community name' of an SNMP management agent will cause a
COMPLETE loss of communications unless all associated SNMP management stations
(clients) ALSO change over to the new 'trap community name'!!!
""")


class _XcmGenBaseGroupWalkHidden_Type(XcmGenGroupSupport):
    """Custom type xcmGenBaseGroupWalkHidden based on XcmGenGroupSupport"""
    defaultValue = 12288


_XcmGenBaseGroupWalkHidden_Object = MibTableColumn
xcmGenBaseGroupWalkHidden = _XcmGenBaseGroupWalkHidden_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 16),
    _XcmGenBaseGroupWalkHidden_Type()
)
xcmGenBaseGroupWalkHidden.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmGenBaseGroupWalkHidden.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseGroupWalkHidden.setDescription("""\
 The terse control/report vector of ALL mandatory, conditionally mandatory, and
optional XCMI General MIB object groups which are hidden from MIB walks (via
SNMP GetNext or GetBulk PDUs) by this management agent implementation (ie,
version) on this host system, specified in a bit-mask. Usage: When an object
group is currently 'hidden' via 'xcmGenBaseGroupWalkHidden', XCMI conforming
management agents SHALL skip over that object group to the next
lexicographically higher object for GetNext or GetBulk requests. Usage:
Conforming management agents SHOULD hide the Message Map Message Text object
groups from MIB walks (as they MAY contain thousands of conceptual rows in
typical implementations). Usage: Conforming management agents SHALL accurately
report their hidden MIB walk XCMI General MIB object groups.
""")


class _XcmGenBaseNotifySchemeSupport_Type(XcmGenNotifySchemeSupport):
    """Custom type xcmGenBaseNotifySchemeSupport based on XcmGenNotifySchemeSupport"""
    defaultValue = 1


_XcmGenBaseNotifySchemeSupport_Object = MibTableColumn
xcmGenBaseNotifySchemeSupport = _XcmGenBaseNotifySchemeSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 17),
    _XcmGenBaseNotifySchemeSupport_Type()
)
xcmGenBaseNotifySchemeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseNotifySchemeSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseNotifySchemeSupport.setReference("""\
 See: 'XcmGenNotifySchemeSupport' in XCMI General TC. See:
'xcmGenBaseSNMPDomainSupport' in XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmGenBaseNotifySchemeSupport.setDescription("""\
 The terse conformance statement of ALL notification URI schemes which are
supported by this management agent implementation (ie, version) on this host
system, specified in a bit-mask. Usage: Conforming management agents SHALL
accurately report their support for notification URI schemes.
""")


class _XcmGenBaseNotifySeveritySupport_Type(XcmGenNotifySeverityFilter):
    """Custom type xcmGenBaseNotifySeveritySupport based on XcmGenNotifySeverityFilter"""
    defaultValue = 15


_XcmGenBaseNotifySeveritySupport_Object = MibTableColumn
xcmGenBaseNotifySeveritySupport = _XcmGenBaseNotifySeveritySupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 18),
    _XcmGenBaseNotifySeveritySupport_Type()
)
xcmGenBaseNotifySeveritySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseNotifySeveritySupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseNotifySeveritySupport.setReference("""\
 See: 'prtAlertSeverityLevel' in IETF Printer MIB (RFC 1759). See:
'XcmGenNotifySeverityFilter' in XCMI General TC. See:
'xcmGenTrapViewNotifySeverity' in XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmGenBaseNotifySeveritySupport.setDescription("""\
 The terse conformance statement of ALL notification severity filters supported
by this management agent implementation (ie, version) on this host system,
specified in a bit-mask. Usage: Individual trap definitions MAY further
constrain which notifications are 'in scope'. Usage: Conforming management
agents SHALL accurately report their support for notification severity filters.
""")


class _XcmGenBaseNotifyTrainingSupport_Type(XcmGenNotifyTrainingFilter):
    """Custom type xcmGenBaseNotifyTrainingSupport based on XcmGenNotifyTrainingFilter"""
    defaultValue = 60


_XcmGenBaseNotifyTrainingSupport_Object = MibTableColumn
xcmGenBaseNotifyTrainingSupport = _XcmGenBaseNotifyTrainingSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 19),
    _XcmGenBaseNotifyTrainingSupport_Type()
)
xcmGenBaseNotifyTrainingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseNotifyTrainingSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseNotifyTrainingSupport.setReference("""\
 See: 'prtAlertTrainingLevel' in IETF Printer MIB (RFC 1759). See:
'XcmGenNotifyTrainingFilter' in XCMI General TC. See:
'xcmGenTrapViewNotifyTraining' in XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmGenBaseNotifyTrainingSupport.setDescription("""\
 The terse conformance statement of ALL notification training filters supported
by this management agent implementation (ie, version) on this host system,
specified in a bit-mask. Usage: Individual trap definitions MAY further
constrain which notifications are 'in scope'. Usage: Conforming management
agents SHALL accurately report their support for notification training filters.
""")


class _XcmGenBaseSystem1284DeviceId_Type(DisplayString):
    """Custom type xcmGenBaseSystem1284DeviceId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenBaseSystem1284DeviceId_Type.__name__ = "DisplayString"
_XcmGenBaseSystem1284DeviceId_Object = MibTableColumn
xcmGenBaseSystem1284DeviceId = _XcmGenBaseSystem1284DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 20),
    _XcmGenBaseSystem1284DeviceId_Type()
)
xcmGenBaseSystem1284DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenBaseSystem1284DeviceId.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseSystem1284DeviceId.setDescription("""\
 The value of this variable MUST exactly match the IEEE 1284-2000 Device ID
string, except the length field MUST NOT be specified. The value is assigned by
the Printer vendor and MUST NOT be localized by the agent. The IEEE 1284-2000
Device ID is a length field followed by a case-sensitive string of ASCII
characters defining peripheral characteristics and/or capabilities. For the
purposes of this specification, the length bytes MUST NOT be included. The
Device ID sequence is composed of a series of keys and values of the form: key:
value {,value} repeated for each key As indicated, each key will have one
value, and MAY have more than one value. The minimum necessary keys (case-
sensitive) are MANUFACTURER, COMMAND SET, and MODEL. (These keys MAY be
abbreviated as MFG, CMD, and MDL respectively.) Each implementation MUST supply
these three keys and possibly additional ones as well. Each key (and each
value) is a string of characters. Any characters except colon (:), comma (,),
and semi-colon (;) MAY be included as part of the key (or value) string. Any
leading or trailing white space in the string is ignored by the parsing program
(but is still counted as part of the overall length of the sequence). An
example ID String, showing optional comment and active command set keys and
their associated values (the text is actually all on one line): MFG:Xerox;
CMD:PCL,POSTSCRIPT,PJL; MDL:WorkCentre Pro 32C; CLS:PRINTER; DES: Xerox
WorkCentre Pro 32C
""")


class _XcmGenBaseSNMPWarningTrapSupport_Type(TruthValue):
    """Custom type xcmGenBaseSNMPWarningTrapSupport based on TruthValue"""


_XcmGenBaseSNMPWarningTrapSupport_Object = MibTableColumn
xcmGenBaseSNMPWarningTrapSupport = _XcmGenBaseSNMPWarningTrapSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 1, 2, 1, 21),
    _XcmGenBaseSNMPWarningTrapSupport_Type()
)
xcmGenBaseSNMPWarningTrapSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPWarningTrapSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseSNMPWarningTrapSupport.setDescription("""\
 This object SHALL be 'true' if this management agent supports sending SNMP
warning traps. This object SHALL be 'false'if this management agent does NOT
support sending SNMP warning traps. This does not change the behavior of
support for sending 'Error Cleared' traps such sending a trap when an
alertRemovalOfBinaryChangeEntry is added to the Alert Table.
""")
_XcmGeneralMIBConformance_ObjectIdentity = ObjectIdentity
xcmGeneralMIBConformance = _XcmGeneralMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2)
)
_XcmGeneralMIBGroups_ObjectIdentity = ObjectIdentity
xcmGeneralMIBGroups = _XcmGeneralMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2)
)
_XcmGenCurrentLocalization_ObjectIdentity = ObjectIdentity
xcmGenCurrentLocalization = _XcmGenCurrentLocalization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 3)
)
_XcmGenCurrentLocalizationTable_Object = MibTable
xcmGenCurrentLocalizationTable = _XcmGenCurrentLocalizationTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 3, 1)
)
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationTable.setDescription("""\
 A table of general localization information per device. It is put in a table
so it can be per device using the hrDeviceIndex.
""")
_XcmGenCurrentLocalizationEntry_Object = MibTableRow
xcmGenCurrentLocalizationEntry = _XcmGenCurrentLocalizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 3, 1, 1)
)
xcmGenCurrentLocalizationEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationEntry.setDescription("""\
 Contains the scalar objects that we want to be per device.
""")
_XcmGenCurrentLocalizationIndex_Type = Ordinal16
_XcmGenCurrentLocalizationIndex_Object = MibTableColumn
xcmGenCurrentLocalizationIndex = _XcmGenCurrentLocalizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 3, 1, 1, 1),
    _XcmGenCurrentLocalizationIndex_Type()
)
xcmGenCurrentLocalizationIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationIndex.setDescription("""\
 The value of the 'xcmGenLocalizationIndex' corresponding to the current
language, country, and character set which SHALL be used for all objects of
type 'InternationalDisplayString' in all legacy MIBs. Note the Printer MIB has
a similar mechanism which controls only objects (of type OCTET STRING) which
are in the Printer MIB.
""")
_XcmGenCurrLocalizationRowStatus_Type = RowStatus
_XcmGenCurrLocalizationRowStatus_Object = MibTableColumn
xcmGenCurrLocalizationRowStatus = _XcmGenCurrLocalizationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 3, 1, 1, 2),
    _XcmGenCurrLocalizationRowStatus_Type()
)
xcmGenCurrLocalizationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCurrLocalizationRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCurrLocalizationRowStatus.setReference("""\
 See: 'xcmGenBaseGroupCreateSupport' in 'xcmGenBaseTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenCurrLocalizationRowStatus.setDescription("""\
 This object manages the row status of this conceptual row in the
'xcmGenCurrentLocalizationTable'. Usage: Conforming implementations which
support static rows SHALL support 'active' and 'notInService' writes to this
'xcmGenCurrLocalizationRowStatus' row status object; and SHALL clear the
'xcmGenCurrentLocalizationGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations which support dynamic rows
SHALL support 'createAndGo' and 'destroy' writes to this
'xcmGenCurrLocalizationRowStatus' row status object; and SHALL set the
'xcmGenCurrentLocalizationGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations NEED NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: Conforming implementations MAY support a single, static
conceptual row, but SHALL allocate that row with an 'hrDeviceIndex' value of
one ('1'). Usage: This row status SHALL be set, to 'active(1)' (for static
rows) or 'createAndGo(4)' (for dynamic rows), in the same PDU which sets the
current locale in 'xcmGenCurrentLocalizationIndex' (thus activating/allocating
this conceptual row). Usage: To explicitly release this conceptual row, a
management station SHALL set 'xcmGenCurrLocalizationRowStatus' to
'notInService(2)' (for static rows) or 'destroy(6)' (for dynamic rows). Usage:
See section 3.4 'Secure Modes of Operation' and section 3.5 'Secure SNMP
Get/Set Requests' in XCMI Security TC, for details of secure modes of access to
this row status object.
""")
_XcmGenLocalization_ObjectIdentity = ObjectIdentity
xcmGenLocalization = _XcmGenLocalization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4)
)
_XcmGenLocalizationTable_Object = MibTable
xcmGenLocalizationTable = _XcmGenLocalizationTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1)
)
if mibBuilder.loadTexts:
    xcmGenLocalizationTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLocalizationTable.setDescription("""\
 The available localizations in this device.
""")
_XcmGenLocalizationEntry_Object = MibTableRow
xcmGenLocalizationEntry = _XcmGenLocalizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1)
)
xcmGenLocalizationEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenLocalizationIndex"),
)
if mibBuilder.loadTexts:
    xcmGenLocalizationEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLocalizationEntry.setDescription("""\
 An entry exists in this table for each Localization, i.e. for each combination
of Language, Country (or Territory) and Coded Character Set, that is supported
in some objects of type 'InternationalDisplayString',
'XcmFixedLocaleDisplayString', 'XcmFixedLocaleUtf8String', or
'XcmNamedLocaleUtf8String' for each device on this managed system.
""")
_XcmGenLocalizationIndex_Type = Ordinal16
_XcmGenLocalizationIndex_Object = MibTableColumn
xcmGenLocalizationIndex = _XcmGenLocalizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 1),
    _XcmGenLocalizationIndex_Type()
)
xcmGenLocalizationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenLocalizationIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLocalizationIndex.setDescription("""\
 A unique value used by the device to identify this localization entry.
""")
_XcmGenLocalizationRowStatus_Type = RowStatus
_XcmGenLocalizationRowStatus_Object = MibTableColumn
xcmGenLocalizationRowStatus = _XcmGenLocalizationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 2),
    _XcmGenLocalizationRowStatus_Type()
)
xcmGenLocalizationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLocalizationRowStatus.setReference("""\
 See: 'xcmGenBaseGroupCreateSupport' in 'xcmGenBaseTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenLocalizationRowStatus.setDescription("""\
 This object manages the row status of this conceptual row in the
'xcmGenLocalizationTable'. Usage: Conforming implementations which support
static rows SHALL support 'active' and 'notInService' writes to this
'xcmGenLocalizationRowStatus' row status object; and SHALL clear the
'xcmGenLocalizationGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations which support dynamic rows
SHALL support 'createAndGo' and 'destroy' writes to this
'xcmGenLocalizationRowStatus' row status object; and SHALL set the
'xcmGenLocalizationGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: See section 3.4 'Secure Modes of Operation' and
section 3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of
secure modes of access to this row status object.
""")


class _XcmGenLocalizationASCIIName_Type(DisplayString):
    """Custom type xcmGenLocalizationASCIIName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenLocalizationASCIIName_Type.__name__ = "DisplayString"
_XcmGenLocalizationASCIIName_Object = MibTableColumn
xcmGenLocalizationASCIIName = _XcmGenLocalizationASCIIName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 3),
    _XcmGenLocalizationASCIIName_Type()
)
xcmGenLocalizationASCIIName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationASCIIName.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLocalizationASCIIName.setDescription("""\
 The unlocalized human readable name in NVT ASCII of the localization with the
language, followed by the country (or territory), followed by the character
set. Example: English US ASCII
""")


class _XcmGenLocalizationName_Type(InternationalDisplayString):
    """Custom type xcmGenLocalizationName based on InternationalDisplayString"""
    defaultHexValue = ""

    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenLocalizationName_Type.__name__ = "InternationalDisplayString"
_XcmGenLocalizationName_Object = MibTableColumn
xcmGenLocalizationName = _XcmGenLocalizationName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 4),
    _XcmGenLocalizationName_Type()
)
xcmGenLocalizationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationName.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLocalizationName.setDescription("""\
 The localized human readable name of the localization with the language,
followed by the country (or territory), followed by the character set. Example:
Japanese Japan Kanji (Represented with Kanji chars.)
""")


class _XcmGenLocalizationLanguage_Type(CodedLanguage):
    """Custom type xcmGenLocalizationLanguage based on CodedLanguage"""
    defaultHexValue = ""


_XcmGenLocalizationLanguage_Object = MibTableColumn
xcmGenLocalizationLanguage = _XcmGenLocalizationLanguage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 5),
    _XcmGenLocalizationLanguage_Type()
)
xcmGenLocalizationLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationLanguage.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLocalizationLanguage.setDescription("""\
 A two character language abreviation from ISO 639:1988 - Codes For the
Representation of Names of Languages. Examples EN, GB, CA, FR, DE.
""")


class _XcmGenLocalizationCountry_Type(CodedCountry):
    """Custom type xcmGenLocalizationCountry based on CodedCountry"""
    defaultHexValue = ""


_XcmGenLocalizationCountry_Object = MibTableColumn
xcmGenLocalizationCountry = _XcmGenLocalizationCountry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 6),
    _XcmGenLocalizationCountry_Type()
)
xcmGenLocalizationCountry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationCountry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLocalizationCountry.setDescription("""\
 A two character country or territory abbreviation from ISO 3166:1993 - Codes
for the Representation of Names of Countries. Examples: US, FR, DE, ...
""")


class _XcmGenLocalizationCharSet_Type(IANACharset):
    """Custom type xcmGenLocalizationCharSet based on IANACharset"""


_XcmGenLocalizationCharSet_Object = MibTableColumn
xcmGenLocalizationCharSet = _XcmGenLocalizationCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 4, 1, 1, 7),
    _XcmGenLocalizationCharSet_Type()
)
xcmGenLocalizationCharSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLocalizationCharSet.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLocalizationCharSet.setDescription("""\
 The charset used for this localization. The value is the enum for the charset
registered with IANA. See the 'IANACharset' textual-convention in the Printer
MIB (RFC 1759).
""")
_XcmGenCodeIndexedString_ObjectIdentity = ObjectIdentity
xcmGenCodeIndexedString = _XcmGenCodeIndexedString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5)
)
_XcmGenCodeIndexedStringTable_Object = MibTable
xcmGenCodeIndexedStringTable = _XcmGenCodeIndexedStringTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1)
)
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringTable.setDescription("""\
 The current charset-indexed strings for this device.
""")
_XcmGenCodeIndexedStringEntry_Object = MibTableRow
xcmGenCodeIndexedStringEntry = _XcmGenCodeIndexedStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1, 1)
)
xcmGenCodeIndexedStringEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenCodeIndexedStringIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenCodeIndexedStringCharSet"),
)
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringEntry.setDescription("""\
 An entry exists in this table containing a charset-indexed string in a
particular charset. There are separate sets of charset-indexed strings for each
device. If an agent supports multiple charset representations of a charset-
indexed string, including code conversion between, there will be a separate
entry for each such charset representation. Usage:
'xcmGenCodeIndexedStringCharSet' selects which charset representation is to be
returned. The value of 'xcmGenCodeIndexedStringCharSet' is the charset enum
registered with IANA. See the 'IANACharset' textual-convention in the Printer
MIB (RFC 1759). Usage: Conforming management agents SHALL NOT 'reuse' values of
'xcmGenCodeIndexedStringIndex' until its' 32-bit value wraps. This prevents
access to 'xcmGenCodeIndexedStringData' contents via 'stale' pointers
(previously cached from XCMI Job Monitoring MIB or XCMI Resources MIB). Note:
Conforming management stations SHOULD interwork with earlier (pre-XCMI 3.1)
management agents which MAY 'reuse' values of 'xcmGenCodeIndexedStringIndex'.
By first reading the pointer object in XCMI Job Monitoring MIB or XCMI
Resources MIB, the manager will avoid 'stale' pointer processing errors.
""")


class _XcmGenCodeIndexedStringIndex_Type(CodeIndexedStringIndex):
    """Custom type xcmGenCodeIndexedStringIndex based on CodeIndexedStringIndex"""
    subtypeSpec = CodeIndexedStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_XcmGenCodeIndexedStringIndex_Type.__name__ = "CodeIndexedStringIndex"
_XcmGenCodeIndexedStringIndex_Object = MibTableColumn
xcmGenCodeIndexedStringIndex = _XcmGenCodeIndexedStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1, 1, 1),
    _XcmGenCodeIndexedStringIndex_Type()
)
xcmGenCodeIndexedStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringIndex.setDescription("""\
 A unique value used by the device, along with the following
'xcmGenCodeIndexedStringCharSet', to identify this charset-indexed string
entry. Usage: Conforming management agents SHALL NOT 'reuse' values of
'xcmGenCodeIndexedStringIndex' until its' 32-bit value wraps. This prevents
access to 'xcmGenCodeIndexedStringData' contents via 'stale' pointers
(previously cached from XCMI Job Monitoring MIB or XCMI Resources MIB). Note:
Conforming management stations SHOULD interwork with earlier (pre-XCMI 3.1)
management agents which MAY 'reuse' values of 'xcmGenCodeIndexedStringIndex'.
By first reading the pointer object in XCMI Job Monitoring MIB or XCMI
Resources MIB, the manager will avoid 'stale' pointer processing errors.
""")
_XcmGenCodeIndexedStringCharSet_Type = IANACharset
_XcmGenCodeIndexedStringCharSet_Object = MibTableColumn
xcmGenCodeIndexedStringCharSet = _XcmGenCodeIndexedStringCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1, 1, 2),
    _XcmGenCodeIndexedStringCharSet_Type()
)
xcmGenCodeIndexedStringCharSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringCharSet.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringCharSet.setDescription("""\
 The charset used for this charset-indexed string entry. Usage: The value is
the enum for the charset registered with IANA. See the 'IANACharset' textual-
convention in the Printer MIB (RFC 1759).
""")
_XcmGenCodeIndexedStringRowStat_Type = RowStatus
_XcmGenCodeIndexedStringRowStat_Object = MibTableColumn
xcmGenCodeIndexedStringRowStat = _XcmGenCodeIndexedStringRowStat_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1, 1, 3),
    _XcmGenCodeIndexedStringRowStat_Type()
)
xcmGenCodeIndexedStringRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringRowStat.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringRowStat.setReference("""\
 See: 'xcmGenBaseGroupCreateSupport' in 'xcmGenBaseTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringRowStat.setDescription("""\
 This object manages the row status of this conceptual row in the
'xcmGenCodeIndexedStringTable'. Usage: Conforming implementations which support
static rows SHALL support 'active' and 'notInService' writes to this
'xcmGenCodeIndexedStringRowStat' row status object; and SHALL clear the
'xcmGenCodeIndexedStringGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations which support dynamic rows
SHALL support 'createAndGo' and 'destroy' writes to this
'xcmGenCodeIndexedStringRowStat' row status object; and SHALL set the
'xcmGenCodeIndexedStringGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: See section 3.4 'Secure Modes of Operation' and
section 3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of
secure modes of access to this row status object.
""")


class _XcmGenCodeIndexedStringData_Type(OctetString):
    """Custom type xcmGenCodeIndexedStringData based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenCodeIndexedStringData_Type.__name__ = "OctetString"
_XcmGenCodeIndexedStringData_Object = MibTableColumn
xcmGenCodeIndexedStringData = _XcmGenCodeIndexedStringData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 5, 1, 1, 4),
    _XcmGenCodeIndexedStringData_Type()
)
xcmGenCodeIndexedStringData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringData.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringData.setDescription("""\
 This is the actual charset-indexed string data, in the charset identified by
'xcmGenCodeIndexedStringCharSet'.
""")
_XcmGenCodedCharSet_ObjectIdentity = ObjectIdentity
xcmGenCodedCharSet = _XcmGenCodedCharSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6)
)
_XcmGenCodedCharSetTable_Object = MibTable
xcmGenCodedCharSetTable = _XcmGenCodedCharSetTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6, 1)
)
if mibBuilder.loadTexts:
    xcmGenCodedCharSetTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetTable.setDescription("""\
 The supported charsets for this device.
""")
_XcmGenCodedCharSetEntry_Object = MibTableRow
xcmGenCodedCharSetEntry = _XcmGenCodedCharSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6, 1, 1)
)
xcmGenCodedCharSetEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenCodedCharSetCharSet"),
)
if mibBuilder.loadTexts:
    xcmGenCodedCharSetEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetEntry.setDescription("""\
 An entry exists in this table for each charset supported in some objects of
'CodeIndexedStringIndex' type for each device.
""")
_XcmGenCodedCharSetCharSet_Type = IANACharset
_XcmGenCodedCharSetCharSet_Object = MibTableColumn
xcmGenCodedCharSetCharSet = _XcmGenCodedCharSetCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6, 1, 1, 1),
    _XcmGenCodedCharSetCharSet_Type()
)
xcmGenCodedCharSetCharSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetCharSet.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetCharSet.setReference("""\
 See the 'IANACharset' textual-convention in the Printer MIB.
""")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetCharSet.setDescription("""\
 The supported charset enum identifier, used an index for this table. The value
is the enum for the charset registered with IANA.
""")
_XcmGenCodedCharSetRowStatus_Type = RowStatus
_XcmGenCodedCharSetRowStatus_Object = MibTableColumn
xcmGenCodedCharSetRowStatus = _XcmGenCodedCharSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6, 1, 1, 2),
    _XcmGenCodedCharSetRowStatus_Type()
)
xcmGenCodedCharSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetRowStatus.setReference("""\
 See: 'xcmGenBaseGroupCreateSupport' in 'xcmGenBaseTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetRowStatus.setDescription("""\
 This object manages the row status of this conceptual row in the
'xcmGenCodedCharSetTable'. Usage: Conforming implementations which support
static rows SHALL support 'active' and 'notInService' writes to this
'xcmGenCodedCharSetRowStatus' row status object; and SHALL clear the
'xcmGenCodedCharSetGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations which support dynamic rows
SHALL support 'createAndGo' and 'destroy' writes to this
'xcmGenCodedCharSetRowStatus' row status object; and SHALL set the
'xcmGenCodedCharSetGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations NEED NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmGenCodedCharSetASCIIName_Type(DisplayString):
    """Custom type xcmGenCodedCharSetASCIIName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenCodedCharSetASCIIName_Type.__name__ = "DisplayString"
_XcmGenCodedCharSetASCIIName_Object = MibTableColumn
xcmGenCodedCharSetASCIIName = _XcmGenCodedCharSetASCIIName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 6, 1, 1, 3),
    _XcmGenCodedCharSetASCIIName_Type()
)
xcmGenCodedCharSetASCIIName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetASCIIName.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetASCIIName.setDescription("""\
 The unlocalized human readable name in ASCII of the charset. Example: 'ASCII'
""")
_XcmGenFixedLocalization_ObjectIdentity = ObjectIdentity
xcmGenFixedLocalization = _XcmGenFixedLocalization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 7)
)
_XcmGenFixedLocalizationTable_Object = MibTable
xcmGenFixedLocalizationTable = _XcmGenFixedLocalizationTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 7, 1)
)
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationTable.setReference("""\
 See: 'XcmFixedLocale[Display|Utf8]String' in the XCMI General TC.
""")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationTable.setDescription("""\
 A table of fixed localization information per device. It is put in a table so
it can be per device using the hrDeviceIndex.
""")
_XcmGenFixedLocalizationEntry_Object = MibTableRow
xcmGenFixedLocalizationEntry = _XcmGenFixedLocalizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 7, 1, 1)
)
xcmGenFixedLocalizationEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationEntry.setReference("""\
 See: 'XcmFixedLocale[Display|Utf8]String' in the XCMI General TC.
""")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationEntry.setDescription("""\
 An entry of fixed localization information per device.
""")
_XcmGenFixedLocalizationIndex_Type = Ordinal16
_XcmGenFixedLocalizationIndex_Object = MibTableColumn
xcmGenFixedLocalizationIndex = _XcmGenFixedLocalizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 7, 1, 1, 1),
    _XcmGenFixedLocalizationIndex_Type()
)
xcmGenFixedLocalizationIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationIndex.setReference("""\
 See: 'XcmFixedLocale[Display|Utf8]String' in the XCMI General TC. See: 'UTF-8,
a transformation of ISO 10646' (RFC 2279) and 'IETF Policy on Character Sets
and Languages' (RFC 2277).
""")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationIndex.setDescription("""\
 The value of the 'xcmGenLocalizationIndex' corresponding to the current
language, country, and character set which SHALL be used for all objects of
type 'XcmFixedLocaleDisplayString' in all current and future MIBs. Also, the
value of the 'xcmGenLocalizationIndex' corresponding to the language and
country (but FIXED UTF-8) which SHALL be used for all objects of type
'XcmFixedLocaleUtf8String' in all current and future MIBs.
""")
_XcmGenFixedLocalizationRowStat_Type = RowStatus
_XcmGenFixedLocalizationRowStat_Object = MibTableColumn
xcmGenFixedLocalizationRowStat = _XcmGenFixedLocalizationRowStat_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 7, 1, 1, 2),
    _XcmGenFixedLocalizationRowStat_Type()
)
xcmGenFixedLocalizationRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationRowStat.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationRowStat.setReference("""\
 See: 'xcmGenBaseGroupCreateSupport' in 'xcmGenBaseTable'. See: 'RowStatus' in
IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX
MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationRowStat.setDescription("""\
 This object manages the row status of this conceptual row in the
'xcmGenFixedLocalizationTable'. Usage: Conforming implementations which support
static rows SHALL support 'active' and 'notInService' writes to this
'xcmGenFixedLocalizationRowStat' row status object; and SHALL clear the
'xcmGenFixedLocalizationGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations which support dynamic rows
SHALL support 'createAndGo' and 'destroy' writes to this
'xcmGenFixedLocalizationRowStat' row status object; and SHALL set the
'xcmGenFixedLocalizationGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations NEED NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: Conforming implementations MAY support a single, static
conceptual row, but SHALL allocate that row with an 'hrDeviceIndex' value of
one ('1'). Usage: This row status SHALL be set, to 'active(1)' (for static
rows) or 'createAndGo(4)' (for dynamic rows), in the same PDU which sets the
fixed locale in 'xcmGenFixedLocalizationIndex' (thus activating/allocating this
conceptual row). Usage: To explicitly release this conceptual row, a management
station SHALL set 'xcmGenFixedLocalizationRowStat' to 'notInService(2)' (for
static rows) or 'destroy(6)' (for dynamic rows). Usage: See section 3.4 'Secure
Modes of Operation' and section 3.5 'Secure SNMP Get/Set Requests' in XCMI
Security TC, for details of secure modes of access to this row status object.
""")
_XcmGenLock_ObjectIdentity = ObjectIdentity
xcmGenLock = _XcmGenLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8)
)
_XcmGenLockSimple_ObjectIdentity = ObjectIdentity
xcmGenLockSimple = _XcmGenLockSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1)
)
if mibBuilder.loadTexts:
    xcmGenLockSimple.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockSimple.setDescription("""\
 This subtree is current. Subordinate objects are leaf objects.
""")
_XcmGenLockSupportMaxTimer_Type = Cardinal32
_XcmGenLockSupportMaxTimer_Object = MibScalar
xcmGenLockSupportMaxTimer = _XcmGenLockSupportMaxTimer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1, 1),
    _XcmGenLockSupportMaxTimer_Type()
)
xcmGenLockSupportMaxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenLockSupportMaxTimer.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockSupportMaxTimer.setUnits("seconds")
if mibBuilder.loadTexts:
    xcmGenLockSupportMaxTimer.setReference("""\
 See: 'xcmGenLockCurrentMaxTimer' and 'xcmGenLockOwnerTimer'
""")
if mibBuilder.loadTexts:
    xcmGenLockSupportMaxTimer.setDescription("""\
 The advisory lock supported max owner timer (in seconds) for use for ANY
advisory lock in the 'xcmGenLockTable'. Usage: The value zero ('0') represents
'no limit'. Usage: This supported max timer represents an XCMI enhancement to
the traditional advisory lock mechanism used in existing IETF MIB modules (eg,
RFC 1573). It provides reliable information to a management station contending
for advisory locks, about the MAXIMUM time supported (ie, permitted) for ANY
advisory lock by the management agent on this host system.
""")
_XcmGenLockCurrentMaxTimer_Type = Cardinal32
_XcmGenLockCurrentMaxTimer_Object = MibScalar
xcmGenLockCurrentMaxTimer = _XcmGenLockCurrentMaxTimer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1, 2),
    _XcmGenLockCurrentMaxTimer_Type()
)
xcmGenLockCurrentMaxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenLockCurrentMaxTimer.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockCurrentMaxTimer.setUnits("seconds")
if mibBuilder.loadTexts:
    xcmGenLockCurrentMaxTimer.setReference("""\
 See: 'xcmGenLockSupportMaxTimer' and 'xcmGenLockOwnerTimer'
""")
if mibBuilder.loadTexts:
    xcmGenLockCurrentMaxTimer.setDescription("""\
 The advisory lock current max owner timer (in seconds) in use for ANY advisory
lock in the 'xcmGenLockTable'. Usage: This current max timer represents an XCMI
enhancement to the traditional advisory lock mechanism used in existing IETF
MIB modules (eg, RFC 1573). It provides reliable information to a management
station contending for advisory locks, about the current MAXIMUM time until
expiration for ALL advisory locks for the management agent on this host system.
Note: To acquire an advisory lock on an ENTIRE host system, a conforming
management station (or management agent) SHALL examine
'xcmGenLockCurrentMaxTimer', add an appropriate delta for eventual processing,
and lock the 'xcmGenLockTable' itself. When 'xcmGenLockCurrentLockCount'
subsequently becomes one (1), the requesting management station (or management
agent) has acquired a lock on the ENTIRE host system (since no OTHER entity MAY
acquire any further lock, because 'xcmGenLockTable' has become 'read-only' to
all other entities), and MAY proceed accordingly.
""")
_XcmGenLockCurrentLockCount_Type = Cardinal32
_XcmGenLockCurrentLockCount_Object = MibScalar
xcmGenLockCurrentLockCount = _XcmGenLockCurrentLockCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1, 3),
    _XcmGenLockCurrentLockCount_Type()
)
xcmGenLockCurrentLockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenLockCurrentLockCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockCurrentLockCount.setReference("""\
 See: 'xcmGenLockHighestLockIndex'
""")
if mibBuilder.loadTexts:
    xcmGenLockCurrentLockCount.setDescription("""\
 The count of entries (rows) which are currently in the 'active' state in
'xcmGenLockTable'. Usage: This current lock count represents an XCMI
enhancement to the traditional advisory lock mechanism used in existing IETF
MIB modules (eg, RFC 1573).
""")
_XcmGenLockHighestLockIndex_Type = Cardinal32
_XcmGenLockHighestLockIndex_Object = MibScalar
xcmGenLockHighestLockIndex = _XcmGenLockHighestLockIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1, 4),
    _XcmGenLockHighestLockIndex_Type()
)
xcmGenLockHighestLockIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenLockHighestLockIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockHighestLockIndex.setReference("""\
 See: 'xcmGenLockCurrentLockCount'
""")
if mibBuilder.loadTexts:
    xcmGenLockHighestLockIndex.setDescription("""\
 The highest advisory lock index which has been active in the
'xcmGenLockTable'. Usage: This highest lock index represents an XCMI
enhancement to the traditional advisory lock mechanism used in existing IETF
MIB modules (eg, RFC 1573).
""")
_XcmGenLockSupportMaxCount_Type = Cardinal32
_XcmGenLockSupportMaxCount_Object = MibScalar
xcmGenLockSupportMaxCount = _XcmGenLockSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 1, 5),
    _XcmGenLockSupportMaxCount_Type()
)
xcmGenLockSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenLockSupportMaxCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockSupportMaxCount.setReference("""\
 See: 'xcmGenLockCurrentLockCount'
""")
if mibBuilder.loadTexts:
    xcmGenLockSupportMaxCount.setDescription("""\
 The maximum number of simultaneous entries (rows) supported for the
'xcmGenLockTable'. Usage: The value zero ('0') represents 'no limit'.
""")
_XcmGenLockTable_Object = MibTable
xcmGenLockTable = _XcmGenLockTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2)
)
if mibBuilder.loadTexts:
    xcmGenLockTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockTable.setReference("""\
 See: 'ifTestOwner' and the 'OwnerString' textual convention in Evolution of
the Interfaces Group of MIB-II (RFC 1573).
""")
if mibBuilder.loadTexts:
    xcmGenLockTable.setDescription("""\
 A table containing 'advisory contention lock' objects for various subtrees of
MIB objects from the complete set of IETF and XCMI MIB modules implemented by
this host system. Note: To acquire an advisory lock on an ENTIRE host system, a
conforming management station (or management agent) SHALL examine
'xcmGenLockCurrentMaxTimer', add an appropriate delta for eventual processing,
and lock the 'xcmGenLockTable' itself. When 'xcmGenLockCurrentLockCount'
subsequently becomes one (1), the requesting management station (or management
agent) has acquired a lock on the ENTIRE host system (since no OTHER entity MAY
acquire any further lock, because 'xcmGenLockTable' has become 'read-only' to
all other entities), and MAY proceed accordingly.
""")
_XcmGenLockEntry_Object = MibTableRow
xcmGenLockEntry = _XcmGenLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1)
)
xcmGenLockEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenLockIndex"),
)
if mibBuilder.loadTexts:
    xcmGenLockEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockEntry.setDescription("""\
 An entry containing 'advisory contention lock' objects for one specific
subtree of MIB objects from the complete set of IETF and XCMI MIB modules
implemented by this host system.
""")
_XcmGenLockIndex_Type = Ordinal32
_XcmGenLockIndex_Object = MibTableColumn
xcmGenLockIndex = _XcmGenLockIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1, 1),
    _XcmGenLockIndex_Type()
)
xcmGenLockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenLockIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockIndex.setReference("""\
 See: 'XcmGenLockIndex' textual convention
""")
if mibBuilder.loadTexts:
    xcmGenLockIndex.setDescription("""\
 A unique value used by this host system to identify this conceptual row in the
'xcmGenLockTable' - each conceptual row in the 'xcmGenLockTable' represents an
'advisory contention lock' on a specific subtree of MIB objects from the
complete set of IETF and XCMI MIB modules implemented by this host system.
""")
_XcmGenLockRowStatus_Type = RowStatus
_XcmGenLockRowStatus_Object = MibTableColumn
xcmGenLockRowStatus = _XcmGenLockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1, 2),
    _XcmGenLockRowStatus_Type()
)
xcmGenLockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLockRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockRowStatus.setReference("""\
 See: 'xcmGenBaseGroupCreateSupport' in 'xcmGenBaseTable'. See:
'xcmGenLockSupportMaxCount' (limit object). See: 'RowStatus' in IETF SNMPv2 TC
(RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX MIB and
'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenLockRowStatus.setDescription("""\
 This object manages the row status of this conceptual row in the
'xcmGenLockTable'. Usage: Conforming implementations which support static rows
SHALL support 'active' and 'notInService' writes to this 'xcmGenLockRowStatus'
row status object; and SHALL clear the 'xcmGenLockGroup' bit in
'xcmGenBaseGroupCreateSupport' in the 'xcmGenBaseTable'. Usage: Conforming
implementations which support dynamic rows SHALL support 'createAndGo' and
'destroy' writes to this 'xcmGenLockRowStatus' row status object; and SHALL set
the 'xcmGenLockGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations NEED NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: Conforming implementations MAY support a single, static
conceptual row, but SHALL allocate that row with an 'xcmGenLockIndex' value of
one ('1'). Usage: Conforming management stations, when they first create or
activate rows in this table, SHALL set 'xcmGenLockRowStatus' to 'active(1)'
(for static rows) or 'createAndGo(4)' (for dynamic rows),
'xcmGenLockOwnerString' (if an owner string is available),
'xcmGenLockOwnerSubtree' (if not 'zeroDotZero'), and 'xcmGenLockOwnerTimer' (to
a suitable value) SIMULTANEOUSLY (in the same SNMP Set-Request PDU). Usage:
Conforming management agents SHALL NOT accept sets to 'xcmGenLockOwnerString',
or 'xcmGenLockOwnerSubtree' AFTER row creation (these objects are 'write-
once'). Usage: To explicitly release this advisory lock, the current lock owner
(management station or management agent) SHALL set 'xcmGenLockRowStatus' in
this row to 'notInService(2)' (for static rows) or 'destroy(6)' (for dynamic
rows). Usage: See section 3.4 'Secure Modes of Operation' and section 3.5
'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure modes
of access to this row status object.
""")


class _XcmGenLockOwnerString_Type(OctetString):
    """Custom type xcmGenLockOwnerString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenLockOwnerString_Type.__name__ = "OctetString"
_XcmGenLockOwnerString_Object = MibTableColumn
xcmGenLockOwnerString = _XcmGenLockOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1, 3),
    _XcmGenLockOwnerString_Type()
)
xcmGenLockOwnerString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLockOwnerString.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockOwnerString.setReference("""\
 See: 'xcmGenLockRowStatus', 'xcmGenLockOwnerSubtree', and
'xcmGenLockOwnerTimer'. See: 'ifTestOwner' and the 'OwnerString' textual
convention in Evolution of the Interfaces Group of MIB-II (RFC 1573).
""")
if mibBuilder.loadTexts:
    xcmGenLockOwnerString.setDescription("""\
 The advisory lock owner string corresponding to the current 'owner' of this
advisory lock. Usage: Conforming management stations, when they first create or
activate rows in this table, SHALL set 'xcmGenLockRowStatus' to 'active(1)'
(for static rows) or 'createAndGo(4)' (for dynamic rows),
'xcmGenLockOwnerString' (if an owner string is available),
'xcmGenLockOwnerSubtree' (if not 'zeroDotZero'), and 'xcmGenLockOwnerTimer' (to
a suitable value) SIMULTANEOUSLY (in the same SNMP Set-Request PDU). Usage:
Conforming management agents SHALL NOT accept sets to 'xcmGenLockOwnerString',
or 'xcmGenLockOwnerSubtree' AFTER row creation (these objects are 'write-
once'). Usage: This owner string SHALL contain one or more of the following: a)
Textual form of the management station's transport address; b) Management
station name (eg, domain name); and/or c) Network management person's name,
location, or phone. In the instance that the management agent itself is the
'owner', this object SHALL be set to a string beginning with 'agent' (in
English). Usage: This object is of type 'XcmFixedLocaleDisplayString'.
""")


class _XcmGenLockOwnerSubtree_Type(ObjectIdentifier):
    """Custom type xcmGenLockOwnerSubtree based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmGenLockOwnerSubtree_Object = MibTableColumn
xcmGenLockOwnerSubtree = _XcmGenLockOwnerSubtree_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1, 4),
    _XcmGenLockOwnerSubtree_Type()
)
xcmGenLockOwnerSubtree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLockOwnerSubtree.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockOwnerSubtree.setReference("""\
 See: 'xcmGenLockRowStatus', 'xcmGenLockOwnerString', and
'xcmGenLockOwnerTimer'.
""")
if mibBuilder.loadTexts:
    xcmGenLockOwnerSubtree.setDescription("""\
 The advisory lock owner subtree (ie, scope) for the current 'owner' of this
advisory lock. Usage: Conforming management stations, when they first create or
activate rows in this table, SHALL set 'xcmGenLockRowStatus' to 'active(1)'
(for static rows) or 'createAndGo(4)' (for dynamic rows),
'xcmGenLockOwnerString' (if an owner string is available),
'xcmGenLockOwnerSubtree' (if not 'zeroDotZero'), and 'xcmGenLockOwnerTimer' (to
a suitable value) SIMULTANEOUSLY (in the same SNMP Set-Request PDU). Usage:
Conforming management agents SHALL NOT accept sets to 'xcmGenLockOwnerString',
or 'xcmGenLockOwnerSubtree' AFTER row creation (these objects are 'write-
once'). Usage: This owner subtree represents an XCMI enhancement to the
traditional advisory lock mechanism used in existing IETF MIB modules (eg, RFC
1573).
""")
_XcmGenLockOwnerTimer_Type = Cardinal32
_XcmGenLockOwnerTimer_Object = MibTableColumn
xcmGenLockOwnerTimer = _XcmGenLockOwnerTimer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 8, 2, 1, 5),
    _XcmGenLockOwnerTimer_Type()
)
xcmGenLockOwnerTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenLockOwnerTimer.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockOwnerTimer.setUnits("seconds")
if mibBuilder.loadTexts:
    xcmGenLockOwnerTimer.setReference("""\
 See: 'xcmGenLockRowStatus', 'xcmGenLockOwnerSubtree', and
'xcmGenLockOwnerSubtree'.
""")
if mibBuilder.loadTexts:
    xcmGenLockOwnerTimer.setDescription("""\
 The advisory lock owner lock time remaining for the current 'owner' of this
advisory lock (in seconds). Usage: A conforming management agent MAY choose to
reduce the 'credit' granted as a result of a set to this owner lock timer, at
its sole discretion (see 'xcmGenLockSupportMaxTimer' object). Usage: Conforming
management stations, when they first create or activate rows in this table,
SHALL set 'xcmGenLockRowStatus' to 'active(1)' (for static rows) or
'createAndGo(4)' (for dynamic rows), 'xcmGenLockOwnerString' (if an owner
string is available), 'xcmGenLockOwnerSubtree' (if not 'zeroDotZero'), and
'xcmGenLockOwnerTimer' (to a suitable value) SIMULTANEOUSLY (in the same SNMP
Set-Request PDU). Usage: Conforming management agents SHALL NOT accept sets to
'xcmGenLockOwnerString', or 'xcmGenLockOwnerSubtree' AFTER row creation (these
objects are 'write-once'). Usage: A conforming management station MAY choose to
increase or reduce the value of this owner lock timer, subsequent to initial
row creation, for example to 'refresh' the timer for an additional time
interval. Usage: A conforming management station SHALL NOT reduce the value of
this owner lock timer to zero (as an indirect 'destroy' operation). A
conforming management agent SHALL reject any such set to zero of this owner
lock timer. Usage: This owner lock timer represents an XCMI enhancement to the
traditional advisory lock mechanism used in existing IETF MIB modules (eg, RFC
1573). It provides reliable information to a management station (or management
agent) contending for this advisory lock, about the MAXIMUM time until this
advisory lock lock will be released (either by explicit action of the owner of
the advisory lock or by 'timeout' handling of the management agent itself).
""")
_XcmGenReconf_ObjectIdentity = ObjectIdentity
xcmGenReconf = _XcmGenReconf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9)
)
_XcmGenReconfSimple_ObjectIdentity = ObjectIdentity
xcmGenReconfSimple = _XcmGenReconfSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 1)
)
if mibBuilder.loadTexts:
    xcmGenReconfSimple.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfSimple.setDescription("""\
 This subtree is current. Subordinate objects are leaf objects.
""")
_XcmGenReconfActivations_Type = Counter32
_XcmGenReconfActivations_Object = MibScalar
xcmGenReconfActivations = _XcmGenReconfActivations_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 1, 1),
    _XcmGenReconfActivations_Type()
)
xcmGenReconfActivations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenReconfActivations.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfActivations.setReference("""\
 See: 'xcmGenReconfOptionState'
""")
if mibBuilder.loadTexts:
    xcmGenReconfActivations.setDescription("""\
 The count of SUCCESSFUL 'activations' of reconfiguration for this host system:
invoked by SUCCESSFUL writes to the 'xcmGenReconfOptionState' reconfiguration
invocation object of
'activateFor[ImmediateChange|RebootChange|ImmediateReboot]'; and followed by
SUCCESSFUL completions of 'activation' (without errors reports in
'xcmGenReconfError[Index|Status]'). Usage: Although no default value ('DEFVAL'
clause) is permitted (by IETF SMIv2) for this counter, conforming host systems
SHALL zero this counter upon conceptual row creation.
""")
_XcmGenReconfEntryCount_Type = Counter32
_XcmGenReconfEntryCount_Object = MibScalar
xcmGenReconfEntryCount = _XcmGenReconfEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 1, 2),
    _XcmGenReconfEntryCount_Type()
)
xcmGenReconfEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenReconfEntryCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfEntryCount.setDescription("""\
 The count of entries (rows) which are currently in the 'active' state in
'xcmGenReconfTable'.
""")
_XcmGenReconfSupportMaxCount_Type = Cardinal32
_XcmGenReconfSupportMaxCount_Object = MibScalar
xcmGenReconfSupportMaxCount = _XcmGenReconfSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 1, 3),
    _XcmGenReconfSupportMaxCount_Type()
)
xcmGenReconfSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenReconfSupportMaxCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfSupportMaxCount.setDescription("""\
 The maximum number of simultaneous entries (rows) supported for the
'xcmGenReconfTable'. Usage: The value zero ('0') represents 'no limit'.
""")
_XcmGenReconfTable_Object = MibTable
xcmGenReconfTable = _XcmGenReconfTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2)
)
if mibBuilder.loadTexts:
    xcmGenReconfTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfTable.setDescription("""\
 A table containing information on a 'reconfiguration request', for use in
atomic reconfiguration of this host system. Usage: A conforming management
station (or management agent) SHALL lock 'xcmGenReconfTable' and
'xcmGenOptionTable' before attempting to perform any 'reconfiguration request'
on a host system (via the 'xcmGenLockTable').
""")
_XcmGenReconfEntry_Object = MibTableRow
xcmGenReconfEntry = _XcmGenReconfEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1)
)
xcmGenReconfEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenReconfIndex"),
)
if mibBuilder.loadTexts:
    xcmGenReconfEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfEntry.setDescription("""\
 An entry containing information on a 'reconfiguration request', for use in
atomic reconfiguration of this host system. Usage: The ONLY valid row in the
'xcmGenReconfTable' for each supported device ('hrDeviceIndex') SHALL have an
'xcmGenReconfIndex' of one ('1').
""")
_XcmGenReconfIndex_Type = Ordinal32
_XcmGenReconfIndex_Object = MibTableColumn
xcmGenReconfIndex = _XcmGenReconfIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 1),
    _XcmGenReconfIndex_Type()
)
xcmGenReconfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenReconfIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfIndex.setReference("""\
 See: System, Device, and Software Installed/Running groups in the IETF Host
Resources MIB (RFC 2790). See: Device Info, Device Mgmt, and Device Detail
groups in the XCMI Host Resources Ext MIB.
""")
if mibBuilder.loadTexts:
    xcmGenReconfIndex.setDescription("""\
 A unique value used by this host system to identify this conceptual row in the
'xcmGenReconfTable'. Usage: The ONLY valid row in the 'xcmGenReconfTable' for
each supported device ('hrDeviceIndex') SHALL have an 'xcmGenReconfIndex' of
one ('1').
""")
_XcmGenReconfRowStatus_Type = RowStatus
_XcmGenReconfRowStatus_Object = MibTableColumn
xcmGenReconfRowStatus = _XcmGenReconfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 2),
    _XcmGenReconfRowStatus_Type()
)
xcmGenReconfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenReconfRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfRowStatus.setReference("""\
 See: 'xcmGenBaseGroupCreateSupport' in 'xcmGenBaseTable'. See:
'xcmGenReconfSupportMaxCount' (limit object). See: 'RowStatus' in IETF SNMPv2
TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX MIB and
'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenReconfRowStatus.setDescription("""\
 This object manages the row status of this conceptual row in the
'xcmGenReconfTable'. Usage: Conforming implementations which support static
rows SHALL support 'active' and 'notInService' writes to this
'xcmGenReconfRowStatus' row status object; and SHALL clear the
'xcmGenReconfGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations which support dynamic rows
SHALL support 'createAndGo' and 'destroy' writes to this
'xcmGenReconfRowStatus' row status object; and SHALL set the
'xcmGenReconfGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming management agents SHALL support
'active(1)' and SHOULD support 'notInService(2)' or 'destroy(6)' (to 'release'
the 'reconfiguration request'). Usage: Conforming management agents NEED NOT
support 'createAndGo(4)', and SHOULD NOT support 'notReady(3)' or
'createAndWait(5)'. Usage: See section 3.4 'Secure Modes of Operation' and
section 3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of
secure modes of access to this row status object.
""")
_XcmGenReconfOptionIndex_Type = Cardinal32
_XcmGenReconfOptionIndex_Object = MibTableColumn
xcmGenReconfOptionIndex = _XcmGenReconfOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 3),
    _XcmGenReconfOptionIndex_Type()
)
xcmGenReconfOptionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenReconfOptionIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfOptionIndex.setReference("""\
 See: 'xcmGenReconfActiveOptionIndex'
""")
if mibBuilder.loadTexts:
    xcmGenReconfOptionIndex.setDescription("""\
 The value of 'xcmGenOptionIndex' corresponding to the first pending
reconfiguration option (in 'xcmGenOptionTable'), or zero if there are no
pending reconfiguration options for this host system. Usage: This 'chain'
represents pending reconfiguration options of this host system.
""")


class _XcmGenReconfOptionState_Type(XcmGenReconfOptionState):
    """Custom type xcmGenReconfOptionState based on XcmGenReconfOptionState"""


_XcmGenReconfOptionState_Object = MibTableColumn
xcmGenReconfOptionState = _XcmGenReconfOptionState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 4),
    _XcmGenReconfOptionState_Type()
)
xcmGenReconfOptionState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenReconfOptionState.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfOptionState.setReference("""\
 See: 'xcmGenReconfError[Index|Status]' See: 'XcmGenReconfOptionState', in the
companion XCMI CC TC, for details of 'validation' and 'activation' operations.
See: 'xcmHrDevMgmtCommandData' in XCMI HRX MIB and 'xcmSecUserMgmtData' in XCMI
Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenReconfOptionState.setDescription("""\
 The processing state of ALL pending reconfiguration options of this host
system. A write to this object by an (authorized) management station invokes a
request for validation (or activation) of ALL pending reconfiguration options
of this host system. A read of this object returns 'idle',
'validateInProgress', or 'activateInProgress' to report the processing state of
the last 'validate...' or 'activate...' request. It is mandatory that a
conforming management agent ensure that, at system initialization, this object
SHALL be set to a value of 'idle'. Usage: Conforming management agents SHALL
'reject' any SNMP Set-Request to 'xcmGenReconfOptionState' while another
management operation is already in progress (ie, while
'xcmGenReconfOptionState' is NOT equal to 'idle') with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3). Usage: See section 3.4 'Secure Modes of
Operation' and section 3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC,
for details of secure modes of access to this option state object.
""")
_XcmGenReconfErrorIndex_Type = Cardinal32
_XcmGenReconfErrorIndex_Object = MibTableColumn
xcmGenReconfErrorIndex = _XcmGenReconfErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 5),
    _XcmGenReconfErrorIndex_Type()
)
xcmGenReconfErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenReconfErrorIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfErrorIndex.setReference("""\
 See: 'xcmGenReconfErrorStatus'
""")
if mibBuilder.loadTexts:
    xcmGenReconfErrorIndex.setDescription("""\
 The value of 'xcmGenOptionIndex' corresponding to the first pending
reconfiguration option (in 'xcmGenOptionTable') which was found to be 'in
error' (during 'validate' or 'activate' reconfiguration processing for this
host system), or zero if no error was found (eg, consistency, range, etc).
""")
_XcmGenReconfErrorStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmGenReconfErrorStatus_Object = MibTableColumn
xcmGenReconfErrorStatus = _XcmGenReconfErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 9, 2, 1, 6),
    _XcmGenReconfErrorStatus_Type()
)
xcmGenReconfErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenReconfErrorStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfErrorStatus.setReference("""\
 See: 'xcmGenReconfErrorIndex'
""")
if mibBuilder.loadTexts:
    xcmGenReconfErrorStatus.setDescription("""\
 The reconfiguration error status corresponding to the first pending
reconfiguration option (in 'xcmGenOptionTable') which was found to be 'in
error' (during 'validate' or 'activate' reconfiguration processing for this
host system), or 'noError' if no error was found (eg, consistency, range, etc).
""")
_XcmGenOption_ObjectIdentity = ObjectIdentity
xcmGenOption = _XcmGenOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10)
)
_XcmGenOptionSimple_ObjectIdentity = ObjectIdentity
xcmGenOptionSimple = _XcmGenOptionSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1)
)
if mibBuilder.loadTexts:
    xcmGenOptionSimple.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionSimple.setDescription("""\
 This subtree is current. Subordinate objects are leaf objects.
""")
_XcmGenOptionOperation_ObjectIdentity = ObjectIdentity
xcmGenOptionOperation = _XcmGenOptionOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 1)
)
_XcmGenOptionOperationInsert_ObjectIdentity = ObjectIdentity
xcmGenOptionOperationInsert = _XcmGenOptionOperationInsert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 1, 1)
)
_XcmGenOptionOperationDelete_ObjectIdentity = ObjectIdentity
xcmGenOptionOperationDelete = _XcmGenOptionOperationDelete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 1, 2)
)
_XcmGenOptionOperationReplace_ObjectIdentity = ObjectIdentity
xcmGenOptionOperationReplace = _XcmGenOptionOperationReplace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 1, 3)
)
_XcmGenOptionEntryCount_Type = Counter32
_XcmGenOptionEntryCount_Object = MibScalar
xcmGenOptionEntryCount = _XcmGenOptionEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 2),
    _XcmGenOptionEntryCount_Type()
)
xcmGenOptionEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenOptionEntryCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionEntryCount.setDescription("""\
 The count of entries (rows) which are currently in the 'active' state in
'xcmGenOptionTable'.
""")
_XcmGenOptionSupportMaxCount_Type = Cardinal32
_XcmGenOptionSupportMaxCount_Object = MibScalar
xcmGenOptionSupportMaxCount = _XcmGenOptionSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 1, 3),
    _XcmGenOptionSupportMaxCount_Type()
)
xcmGenOptionSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenOptionSupportMaxCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionSupportMaxCount.setDescription("""\
 The maximum number of simultaneous entries (rows) supported for the
'xcmGenOptionTable'. Usage: The value zero ('0') represents 'no limit'.
""")
_XcmGenOptionTable_Object = MibTable
xcmGenOptionTable = _XcmGenOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2)
)
if mibBuilder.loadTexts:
    xcmGenOptionTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionTable.setDescription("""\
 A table containing information on reconfiguration options, for use in atomic
reconfiguration of this host system. Usage: A conforming management station (or
management agent) SHALL lock 'xcmGenReconfTable' and 'xcmGenOptionTable' before
attempting to perform any 'reconfiguration request' on a host system (via the
'xcmGenLockTable'). Note: The 'xcmGenOptionTable' is indexed by
'hrDeviceIndex', so the 'hrDeviceIndex' element of a columnar object instance
ID (ie, fully specified object identifier) NEED NOT be specified in
'xcmGenOptionTypeOID'. To reconfigure objects indexed by several devices in
'hrDeviceTable' of the IETF Host Resources MIB (RFC 2790), a conforming
management station SHALL use several rows in 'xcmGenReconfTable' and several
trees of objects in 'xcmGenOptionTable' with appropriate 'hrDeviceIndex'
values. To reconfigure objects which are actually NOT indexed by
'hrDeviceIndex', it is RECOMMENDED that rows be used in 'xcmGenOptionTable'
which are indexed by 'hrDeviceIndex' for an 'hrDeviceType' of
'hrDeviceUnknown'.
""")
_XcmGenOptionEntry_Object = MibTableRow
xcmGenOptionEntry = _XcmGenOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1)
)
xcmGenOptionEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenOptionIndex"),
)
if mibBuilder.loadTexts:
    xcmGenOptionEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionEntry.setDescription("""\
 An entry containing information on a reconfiguration option, for use in atomic
reconfiguration of this host system.
""")
_XcmGenOptionIndex_Type = Ordinal32
_XcmGenOptionIndex_Object = MibTableColumn
xcmGenOptionIndex = _XcmGenOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 1),
    _XcmGenOptionIndex_Type()
)
xcmGenOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenOptionIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionIndex.setDescription("""\
 A unique value used by this host system to identify this conceptual row in the
'xcmGenOptionTable'.
""")
_XcmGenOptionRowStatus_Type = RowStatus
_XcmGenOptionRowStatus_Object = MibTableColumn
xcmGenOptionRowStatus = _XcmGenOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 2),
    _XcmGenOptionRowStatus_Type()
)
xcmGenOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionRowStatus.setReference("""\
 See: 'xcmGenBaseGroupCreateSupport' in 'xcmGenBaseTable'. See:
'xcmGenOptionSupportMaxCount' (limit object). See: 'RowStatus' in IETF SNMPv2
TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX MIB and
'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenOptionRowStatus.setDescription("""\
 This object manages the row status of this conceptual row in the
'xcmGenOptionTable'. Usage: Conforming implementations which support static
rows SHALL support 'active' and 'notInService' writes to this
'xcmGenOptionRowStatus' row status object; and SHALL clear the
'xcmGenOptionGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations which support dynamic rows
SHALL support 'createAndGo' and 'destroy' writes to this
'xcmGenOptionRowStatus' row status object; and SHALL set the
'xcmGenOptionGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming management agents SHALL support
'active(1)' and SHOULD support 'notInService(2)' or 'destroy(6)' (to 'release'
the 'reconfiguration option'). Usage: Conforming management agents NEED NOT
support 'createAndGo(4)', and SHOULD NOT support 'notReady(3)' or
'createAndWait(5)'. Usage: See section 3.4 'Secure Modes of Operation' and
section 3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of
secure modes of access to this row status object.
""")


class _XcmGenOptionTypeOID_Type(ObjectIdentifier):
    """Custom type xcmGenOptionTypeOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmGenOptionTypeOID_Object = MibTableColumn
xcmGenOptionTypeOID = _XcmGenOptionTypeOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 3),
    _XcmGenOptionTypeOID_Type()
)
xcmGenOptionTypeOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionTypeOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionTypeOID.setDescription("""\
 An unambiguous reconfiguration option type, used by system administrators and
end users to identify this reconfiguration option. Usage: Since this
reconfiguration option type is specified as an object identifier, it MAY be
taken from any IETF, Xerox, third- party, or product-specific MIB, or it MAY
simply be any IETF SMIv2-style 'autonomous type'.
""")


class _XcmGenOptionValueSyntax_Type(XcmGenOptionValueSyntax):
    """Custom type xcmGenOptionValueSyntax based on XcmGenOptionValueSyntax"""


_XcmGenOptionValueSyntax_Object = MibTableColumn
xcmGenOptionValueSyntax = _XcmGenOptionValueSyntax_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 4),
    _XcmGenOptionValueSyntax_Type()
)
xcmGenOptionValueSyntax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueSyntax.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionValueSyntax.setDescription("""\
 A reconfiguration option value syntax, used by system administrators and end
users to specify the correct value syntax for this reconfiguration option.
Usage: This reconfiguration option value syntax is used to select which of the
following three objects SHALL be used to contain the value of this
reconfiguration option.
""")
_XcmGenOptionValueInteger_Type = Integer32
_XcmGenOptionValueInteger_Object = MibTableColumn
xcmGenOptionValueInteger = _XcmGenOptionValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 5),
    _XcmGenOptionValueInteger_Type()
)
xcmGenOptionValueInteger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueInteger.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionValueInteger.setReference("""\
 See: 'xcmGenOptionValueSyntax' and 'xcmGenOptionTypeOID'
""")
if mibBuilder.loadTexts:
    xcmGenOptionValueInteger.setDescription("""\
 A reconfiguration option value integer, used by system administrators and end
users to specify the current value for a reconfiguration option with a base
value syntax of 'INTEGER'. Note: This object has the type 'Integer32', rather
than 'INTEGER'. This a work-around to compiler warnings which occur when
'INTEGER' is used without a range specification. And if we had range qualified,
it would have been identical to the SNMP 'Integer32' type. In SNMPv2, only the
'Counter64 is an integer type wider 32 bits, and for backward compatibility we
depricated the use of Counter64.
""")


class _XcmGenOptionValueOID_Type(ObjectIdentifier):
    """Custom type xcmGenOptionValueOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmGenOptionValueOID_Object = MibTableColumn
xcmGenOptionValueOID = _XcmGenOptionValueOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 6),
    _XcmGenOptionValueOID_Type()
)
xcmGenOptionValueOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionValueOID.setReference("""\
 See: 'xcmGenOptionValueSyntax' and 'xcmGenOptionTypeOID'
""")
if mibBuilder.loadTexts:
    xcmGenOptionValueOID.setDescription("""\
 A reconfiguration option value OID (object identifier), used by system
administrators and end users to specify the current value for a reconfiguration
option with a base value syntax of 'OBJECT IDENTIFIER'.
""")


class _XcmGenOptionValueString_Type(OctetString):
    """Custom type xcmGenOptionValueString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenOptionValueString_Type.__name__ = "OctetString"
_XcmGenOptionValueString_Object = MibTableColumn
xcmGenOptionValueString = _XcmGenOptionValueString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 7),
    _XcmGenOptionValueString_Type()
)
xcmGenOptionValueString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueString.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionValueString.setReference("""\
See: 'xcmGenOptionValueSyntax' and 'xcmGenOptionTypeOID' See:
'xcmGenFixedLocalizationIndex' in XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmGenOptionValueString.setDescription("""\
A reconfiguration option value string, used by system administrators and end
users to specify the current value for a reconfiguration option with a base
value syntax of 'OCTET STRING'. Usage: This object is of type
'XcmFixedLocaleDisplayString' (if 'xcmGenOptionValueLocalization' is zero) or
'XcmNamedLocaleUtf8String' (if 'xcmGenOptionValueLocalization' is non-zero).
""")
_XcmGenOptionValueLocalization_Type = Cardinal32
_XcmGenOptionValueLocalization_Object = MibTableColumn
xcmGenOptionValueLocalization = _XcmGenOptionValueLocalization_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 8),
    _XcmGenOptionValueLocalization_Type()
)
xcmGenOptionValueLocalization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueLocalization.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionValueLocalization.setReference("""\
See: 'xcmGenOptionValueSyntax' and 'xcmGenOptionTypeOID'. See:
'xcmGenFixedLocalizationIndex' in XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmGenOptionValueLocalization.setDescription("""\
A reconfiguration option value localization, used by system administrators and
end users to specify the ALTERNATE localization for a reconfiguration option
(different from 'xcmGenFixedLocalizationIndex'), so that
'xcmGenOptionValueString' becomes 'XcmNamedLocaleUtf8String'. Usage: For a
reconfiguration option string to which POSIX-style localization (territory,
language, character set) is applicable (non-keyword) this object MAY contain a
suitable index value for 'xcmGenLocalizationIndex' from the XCMI General MIB,
or zero to indicate 'none'.
""")


class _XcmGenOptionValueCodedCharSet_Type(IANACharset):
    """Custom type xcmGenOptionValueCodedCharSet based on IANACharset"""


_XcmGenOptionValueCodedCharSet_Object = MibTableColumn
xcmGenOptionValueCodedCharSet = _XcmGenOptionValueCodedCharSet_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 9),
    _XcmGenOptionValueCodedCharSet_Type()
)
xcmGenOptionValueCodedCharSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionValueCodedCharSet.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionValueCodedCharSet.setReference("""\
See: 'xcmGenOptionValueSyntax' and 'xcmGenOptionTypeOID'. See: 'IANACharset' in
IETF Printer MIB (RFC 1759). See: 'xcmGenCodedCharSetTable' in XCMI General
MIB.
""")
if mibBuilder.loadTexts:
    xcmGenOptionValueCodedCharSet.setDescription("""\
A reconfiguration option value character set, used by system administrators and
end users to specify the ALTERNATE character set for a reconfiguration option
(different from 'xcmGenFixedLocalizationIndex'), so that
'xcmGenOptionValueString' is unambiguous. Usage: XCMI conforming management
agents SHALL ONLY allow Sets of this object to 'other' (none) or 'utf-8'
(Unicode/ ISO-10646 in the UTF-8 encoding, a proper superset of US-ASCII), for
consistency with the Xerox Unicode Coherence Standard.
""")
_XcmGenOptionNextIndex_Type = Cardinal32
_XcmGenOptionNextIndex_Object = MibTableColumn
xcmGenOptionNextIndex = _XcmGenOptionNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 10),
    _XcmGenOptionNextIndex_Type()
)
xcmGenOptionNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionNextIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionNextIndex.setDescription("""\
 The value of 'xcmGenOptionIndex' corresponding to the next 'chained'
conceptual row in the 'xcmGenOptionTable', or zero if this is the last
associated conceptual row in a particular vertical 'chain' within a given set.
Usage: Generally, reconfiguration options (of similar or unlike type) are
'chained' vertically via '...[Next|Previous]Index'. But, in the case where
particular communications options MUST be 'tightly coupled', they SHOULD be
'shelved' horizontally via '...[Family|Previous]Index' (eg, an IP address and
an IP subnet mask).
""")
_XcmGenOptionPreviousIndex_Type = Cardinal32
_XcmGenOptionPreviousIndex_Object = MibTableColumn
xcmGenOptionPreviousIndex = _XcmGenOptionPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 11),
    _XcmGenOptionPreviousIndex_Type()
)
xcmGenOptionPreviousIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionPreviousIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionPreviousIndex.setDescription("""\
 The value of 'xcmGenOptionIndex' corresponding to a previous associated
conceptual row in the 'xcmGenOptionTable', or zero if this is the first
associated conceptual row in a given set. Usage: This object provides common
'backward' linkage for BOTH the 'xcmGenOptionNextIndex' and
'xcmGenOptionFamilyIndex' linkage objects. A previous conceptual row MAY
'forward' reference this conceptual row via either '...NextIndex' or
'...FamilyIndex' - ie, a given conceptual row MAY 'forward' reference EXACTLY
zero, one, or two 'later' conceptual rows.
""")
_XcmGenOptionFamilyIndex_Type = Cardinal32
_XcmGenOptionFamilyIndex_Object = MibTableColumn
xcmGenOptionFamilyIndex = _XcmGenOptionFamilyIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 10, 2, 1, 12),
    _XcmGenOptionFamilyIndex_Type()
)
xcmGenOptionFamilyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenOptionFamilyIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionFamilyIndex.setDescription("""\
 The value of 'xcmGenOptionIndex' corresponding to a next 'family' conceptual
row in the 'xcmGenOptionTable', or zero if this conceptual row has no
associated 'family' members. Usage: Generally, reconfiguration options (of
similar or unlike type) are 'chained' vertically via '...[Next|Previous]Index'.
But, in the case where particular reconfiguration options MUST be 'tightly
coupled', they SHOULD be 'shelved' horizontally via '...FamilyIndex' (eg, an IP
address and an IP subnet mask).
""")
_XcmGenClientData_ObjectIdentity = ObjectIdentity
xcmGenClientData = _XcmGenClientData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11)
)
_XcmGenClientDataSimple_ObjectIdentity = ObjectIdentity
xcmGenClientDataSimple = _XcmGenClientDataSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 1)
)
if mibBuilder.loadTexts:
    xcmGenClientDataSimple.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataSimple.setDescription("""\
 This subtree is current. Subordinate objects are leaf objects.
""")
_XcmGenClientDataEntryCount_Type = Counter32
_XcmGenClientDataEntryCount_Object = MibScalar
xcmGenClientDataEntryCount = _XcmGenClientDataEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 1, 1),
    _XcmGenClientDataEntryCount_Type()
)
xcmGenClientDataEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenClientDataEntryCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataEntryCount.setDescription("""\
 The count of entries (rows) which are currently in the 'active' state in
'xcmGenClientDataTable'.
""")
_XcmGenClientDataLastIndex_Type = Cardinal32
_XcmGenClientDataLastIndex_Object = MibScalar
xcmGenClientDataLastIndex = _XcmGenClientDataLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 1, 2),
    _XcmGenClientDataLastIndex_Type()
)
xcmGenClientDataLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenClientDataLastIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataLastIndex.setDescription("""\
 The last entry index (regardless of its current state) in the
'xcmGenClientDataTable' of this General MIB, on this host system. Usage: This
last entry index explicitly bounds the valid range of 'xcmGenClientDataIndex'.
""")
_XcmGenClientDataSupportMaxCount_Type = Cardinal32
_XcmGenClientDataSupportMaxCount_Object = MibScalar
xcmGenClientDataSupportMaxCount = _XcmGenClientDataSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 1, 3),
    _XcmGenClientDataSupportMaxCount_Type()
)
xcmGenClientDataSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenClientDataSupportMaxCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataSupportMaxCount.setDescription("""\
 The maximum number of simultaneous entries (rows) supported for the
'xcmGenClientDataTable'. Usage: The value zero ('0') represents 'no limit'.
""")
_XcmGenClientDataTable_Object = MibTable
xcmGenClientDataTable = _XcmGenClientDataTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2)
)
if mibBuilder.loadTexts:
    xcmGenClientDataTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataTable.setDescription("""\
 A table containing 'client data' objects for use by conforming management
stations/agents, particularly during installation of this host system. Usage:
For managed systems which support static rows (ie, 'read-write'), a management
station (or management agent) SHALL search 'xcmGenClientDataRowStatus', to
determine the appropriate value of 'xcmGenClientDataIndex' to use when
allocating an existing row in the 'xcmGenClientDataTable'. Usage: For managed
systems which support dynamic rows (ie, 'read-create'), a management station
(or management agent) SHALL examine 'xcmGenClientDataLastIndex', to determine
the appropriate value of 'xcmGenClientDataIndex' to use when creating a new row
in the 'xcmGenClientDataTable'. Usage: Throughout this specification, the term
'stable storage' refers to storage which is reliable over long durations
(years) and is NOT destroyed by host system reboot (eg, battery-backed DRAM is
'stable storage' - while simple DRAM is NOT 'stable storage'). Examples of
valid 'stable storage' include: NVRAM, hard disk, EEPROM, etc. Usage:
Conforming implementations SHALL preserve active 'client data' objects across
management agent power cycles, and SHALL implement one of the following two
methods: 1) The agent SHALL store 'client data' objects directly in 'stable
storage'; or 2) The agent SHALL automatically checkpoint all active 'client
data' objects to 'stable storage' with reasonable frequency (either due to a
write to some 'client data' object, or upon expiration of a product-specific
timeout). Usage: Conforming implementations MAY (optionally) support one of the
following two 'checkpoint protocols': 1) A client sends a 'Set' of
'xcmGenClientDataRowStatus' to 'active(1)', to request that a 'checkpoint' be
performed; 2a) An agent which supports 'rapid checkpoint', completes the
checkpoint to 'stable storage', and sends a 'SetResponse' with 'noError(0)';
<or> 2b) An agent which supports 'delayed checkpoint', changes
'xcmGenClientDataRowStatus' to 'notInService(2)', sends a 'SetResponse' with
'noError(0)', completes the checkpoint to 'stable storage', and later changes
'xcmGenClientDataRowStatus' back to 'active(1)'.
""")
_XcmGenClientDataEntry_Object = MibTableRow
xcmGenClientDataEntry = _XcmGenClientDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1)
)
xcmGenClientDataEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenClientDataIndex"),
)
if mibBuilder.loadTexts:
    xcmGenClientDataEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataEntry.setDescription("""\
 An entry containing 'client data' objects for use by conforming management
stations/agents, particularly during installation of this host system.
""")
_XcmGenClientDataIndex_Type = Ordinal32
_XcmGenClientDataIndex_Object = MibTableColumn
xcmGenClientDataIndex = _XcmGenClientDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 1),
    _XcmGenClientDataIndex_Type()
)
xcmGenClientDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenClientDataIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataIndex.setDescription("""\
 A unique value used by this host system to identify this conceptual row in the
'xcmGenClientDataTable'. Usage: Conforming implementations which only support a
single, statically allocated row, SHALL allocate that row with an
'xcmGenClientDataIndex' value of one (1).
""")
_XcmGenClientDataRowStatus_Type = RowStatus
_XcmGenClientDataRowStatus_Object = MibTableColumn
xcmGenClientDataRowStatus = _XcmGenClientDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 2),
    _XcmGenClientDataRowStatus_Type()
)
xcmGenClientDataRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenClientDataRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataRowStatus.setReference("""\
 See: 'xcmGenBaseGroupCreateSupport' in 'xcmGenBaseTable'. See:
'xcmGenClientDataSupportMaxCount' (limit object). See: 'RowStatus' in IETF
SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX MIB
and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenClientDataRowStatus.setDescription("""\
 This object manages the row status of this conceptual row in the
'xcmGenClientDataTable'. Usage: Conforming implementations which support static
rows SHALL support 'active' and 'notInService' writes to this
'xcmGenClientDataRowStatus' row status object; and SHALL clear the
'xcmGenClientDataGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations which support dynamic rows
SHALL support 'createAndGo' and 'destroy' writes to this
'xcmGenClientDataRowStatus' row status object; and SHALL set the
'xcmGenClientDataGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming implementations NEED NOT support dynamic
row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: Conforming implementations MAY support a single, static
conceptual row, but SHALL allocate that row with an 'xcmGenClientDataIndex'
value of one ('1'). Usage: Conforming management stations, when they first
create or activate rows in this table, SHALL set 'xcmGenClientDataRowStatus' to
'active(1)' (for static rows) or 'createAndGo(4)' (for dynamic rows),
'xcmGenClientDataRequestID' (to a suitable client global ID),
'xcmGenClientDataProductID' (to a suitable client product ID),
'xcmGenClientDataLength' (to a suitable client data length) SIMULTANEOUSLY (in
the same SNMP Set-Request PDU). Usage: Conforming management agents SHALL NOT
accept sets to 'xcmGenClientDataRequestID', 'xcmGenClientDataProductID', or
'xcmGenClientDataLength' AFTER row creation (these objects are 'write-once').
Usage: To explicitly release this conceptual row, the client data owner SHALL
set 'xcmGenClientDataRowStatus' to 'notInService(2)' (for static rows) or
'destroy(6)' (for dynamic rows). Usage: See section 3.4 'Secure Modes of
Operation' and section 3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC,
for details of secure modes of access to this row status object.
""")


class _XcmGenClientDataRequestDate_Type(DateAndTime):
    """Custom type xcmGenClientDataRequestDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmGenClientDataRequestDate_Object = MibTableColumn
xcmGenClientDataRequestDate = _XcmGenClientDataRequestDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 3),
    _XcmGenClientDataRequestDate_Type()
)
xcmGenClientDataRequestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenClientDataRequestDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataRequestDate.setReference("""\
 See: 'xcmGenClientDataRowStatus'
""")
if mibBuilder.loadTexts:
    xcmGenClientDataRequestDate.setDescription("""\
 The client data request date which uniquely timestamps the creation of this
conceptual row in the 'xcmGenClientDataTable'. Usage: This request date SHALL
be set (to a suitable value) by conforming management agents during creation of
each conceptual row in the 'xcmGenClientDataTable'. Usage: Conforming
implementations which have a source of time, SHALL set a meaningful value in
this object. ONLY those implementations which do NOT have a source of time,
SHALL return the following DEFVAL.
""")


class _XcmGenClientDataRequestID_Type(XcmGlobalUniqueID):
    """Custom type xcmGenClientDataRequestID based on XcmGlobalUniqueID"""
    defaultHexValue = ""


_XcmGenClientDataRequestID_Object = MibTableColumn
xcmGenClientDataRequestID = _XcmGenClientDataRequestID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 4),
    _XcmGenClientDataRequestID_Type()
)
xcmGenClientDataRequestID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenClientDataRequestID.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataRequestID.setReference("""\
 See: 'xcmGenClientDataRowStatus'
""")
if mibBuilder.loadTexts:
    xcmGenClientDataRequestID.setDescription("""\
 The client data owner request ID which uniquely identifies the creation of
this conceptual row in the 'xcmGenClientDataTable'. Usage: Conforming
management stations, when they first create or activate rows in this table,
SHALL set 'xcmGenClientDataRowStatus' to 'active(1)' (for static rows) or
'createAndGo(4)' (for dynamic rows), 'xcmGenClientDataRequestID' (to a suitable
client global ID), 'xcmGenClientDataProductID' (to a suitable client product
ID), 'xcmGenClientDataLength' (to a suitable client data length) SIMULTANEOUSLY
(in the same SNMP Set-Request PDU). Usage: Conforming management agents SHALL
NOT accept sets to 'xcmGenClientDataRequestID', 'xcmGenClientDataProductID', or
'xcmGenClientDataLength' AFTER row creation (these objects are 'write-once').
""")


class _XcmGenClientDataProductID_Type(ProductID):
    """Custom type xcmGenClientDataProductID based on ProductID"""
    defaultValue = "(0, 0)"


_XcmGenClientDataProductID_Object = MibTableColumn
xcmGenClientDataProductID = _XcmGenClientDataProductID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 5),
    _XcmGenClientDataProductID_Type()
)
xcmGenClientDataProductID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenClientDataProductID.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataProductID.setReference("""\
 See: 'xcmGenClientDataRowStatus' See: 'ProductID' in IETF Host Resources MIB
(RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmGenClientDataProductID.setDescription("""\
 The client data owner product ID corresponding to the current 'owner' of this
client data. Usage: Conforming management stations, when they first create or
activate rows in this table, SHALL set 'xcmGenClientDataRowStatus' to
'active(1)' (for static rows) or 'createAndGo(4)' (for dynamic rows),
'xcmGenClientDataRequestID' (to a suitable client global ID),
'xcmGenClientDataProductID' (to a suitable client product ID),
'xcmGenClientDataLength' (to a suitable client data length) SIMULTANEOUSLY (in
the same SNMP Set-Request PDU). Usage: Conforming management agents SHALL NOT
accept sets to 'xcmGenClientDataRequestID', 'xcmGenClientDataProductID', or
'xcmGenClientDataLength' AFTER row creation (these objects are 'write-once').
""")
_XcmGenClientDataLength_Type = Cardinal32
_XcmGenClientDataLength_Object = MibTableColumn
xcmGenClientDataLength = _XcmGenClientDataLength_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 6),
    _XcmGenClientDataLength_Type()
)
xcmGenClientDataLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenClientDataLength.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataLength.setReference("""\
 See: 'xcmGenClientDataRowStatus'
""")
if mibBuilder.loadTexts:
    xcmGenClientDataLength.setDescription("""\
 The client data length requested/granted for this conceptual row in the
'xcmGenClientDataTable'. Usage: Conforming implementations NEED NOT support
maximum client data length greater than 1 octet. Usage: Conforming management
stations, when they first create or activate rows in this table, SHALL set
'xcmGenClientDataRowStatus' to 'active(1)' (for static rows) or
'createAndGo(4)' (for dynamic rows), 'xcmGenClientDataRequestID' (to a suitable
client global ID), 'xcmGenClientDataProductID' (to a suitable client product
ID), 'xcmGenClientDataLength' (to a suitable client data length) SIMULTANEOUSLY
(in the same SNMP Set-Request PDU). Usage: Conforming management agents SHALL
NOT accept sets to 'xcmGenClientDataRequestID', 'xcmGenClientDataProductID', or
'xcmGenClientDataLength' AFTER row creation (these objects are 'write-once').
""")


class _XcmGenClientDataString_Type(OctetString):
    """Custom type xcmGenClientDataString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenClientDataString_Type.__name__ = "OctetString"
_XcmGenClientDataString_Object = MibTableColumn
xcmGenClientDataString = _XcmGenClientDataString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 11, 2, 1, 7),
    _XcmGenClientDataString_Type()
)
xcmGenClientDataString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenClientDataString.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataString.setReference("""\
 See: 'xcmGenClientDataRowStatus'
""")
if mibBuilder.loadTexts:
    xcmGenClientDataString.setDescription("""\
 The client data string currently set into this conceptual row in the
'xcmGenClientDataTable'. Usage: Conforming implementations NEED NOT support
maximum client data length greater than 1 octet. Usage: This data string NEED
NOT be set (to a suitable value) by the client data owner, in the same PDU
which creates each conceptual row in the 'xcmGenClientDataTable'.
""")
_XcmGenTrapClient_ObjectIdentity = ObjectIdentity
xcmGenTrapClient = _XcmGenTrapClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13)
)
_XcmGenTrapClientSimple_ObjectIdentity = ObjectIdentity
xcmGenTrapClientSimple = _XcmGenTrapClientSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 1)
)
if mibBuilder.loadTexts:
    xcmGenTrapClientSimple.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientSimple.setDescription("""\
 This subtree is current. Subordinate objects are leaf objects.
""")
_XcmGenTrapClientEntryCount_Type = Counter32
_XcmGenTrapClientEntryCount_Object = MibScalar
xcmGenTrapClientEntryCount = _XcmGenTrapClientEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 1, 1),
    _XcmGenTrapClientEntryCount_Type()
)
xcmGenTrapClientEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenTrapClientEntryCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientEntryCount.setDescription("""\
 The count of entries (rows) which are currently in the 'active' state in
'xcmGenTrapClientTable'.
""")
_XcmGenTrapClientSupportMaxCount_Type = Cardinal32
_XcmGenTrapClientSupportMaxCount_Object = MibScalar
xcmGenTrapClientSupportMaxCount = _XcmGenTrapClientSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 1, 2),
    _XcmGenTrapClientSupportMaxCount_Type()
)
xcmGenTrapClientSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenTrapClientSupportMaxCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientSupportMaxCount.setDescription("""\
 The maximum number of simultaneous entries (rows) supported for the
'xcmGenTrapClientTable'. Usage: The value zero ('0') represents 'no limit'.
""")
_XcmGenTrapClientTable_Object = MibTable
xcmGenTrapClientTable = _XcmGenTrapClientTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2)
)
if mibBuilder.loadTexts:
    xcmGenTrapClientTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientTable.setReference("""\
 See: Party group in Historic SNMPv2 Party MIB (RFC 1447).
""")
if mibBuilder.loadTexts:
    xcmGenTrapClientTable.setDescription("""\
 A table of SNMP trap clients (management stations or proxies) registered for
trap delivery from this host system. Usage: SNMP version/transport independent
trap registration. Usage: Conforming management stations SHALL create at least
one subordinate row in the 'xcmGenTrapViewTable' for each trap client that they
register in the 'xcmGenTrapClientTable'. Conforming management agents SHOULD
interpret a dangling row in the 'xcmGenTrapClientTable' (no children) as 'NO
traps in view' (existing implementations of both clients and devices are known
to consider dangling rows invalid). To register for all device traps, use a
single view of 'iso(1).org(3).dod(6).internet(1)'. Usage: Conforming management
agents SHALL delete any rows in the 'xcmGenTrapViewTable' which were
subordinate to a deleted row in the 'xcmGenTrapClientTable'.
""")
_XcmGenTrapClientEntry_Object = MibTableRow
xcmGenTrapClientEntry = _XcmGenTrapClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1)
)
xcmGenTrapClientEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenTrapClientSNMPDomain"),
    (0, "XEROX-GENERAL-MIB", "xcmGenTrapClientSNMPAddress"),
)
if mibBuilder.loadTexts:
    xcmGenTrapClientEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientEntry.setDescription("""\
 An entry for an SNMP trap client (management station or proxy) registered for
trap delivery from this host system.
""")
_XcmGenTrapClientSNMPDomain_Type = XcmGenSNMPDomain
_XcmGenTrapClientSNMPDomain_Object = MibTableColumn
xcmGenTrapClientSNMPDomain = _XcmGenTrapClientSNMPDomain_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 1),
    _XcmGenTrapClientSNMPDomain_Type()
)
xcmGenTrapClientSNMPDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPDomain.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPDomain.setReference("""\
 See: 'xcmGenBaseSNMP[Domain|Version]Support'. See: 'XcmGenSNMPDomain' textual
convention in the XCMI General TC. See: 'snmp...Domain' object identifiers in
the IETF SNMPv2 Transport Mappings (RFC 1449/1906).
""")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPDomain.setDescription("""\
 This object is used to specify the transport domain (address and name space)
which SHALL be used by this management agent for SNMP protocol traffic
(transmission of SNMP traps), in the version specified by
'xcmGenTrapClientSNMPVersion', to the trap client (management station or
proxy). This object is also used to allow the 'xcmGenTrapClientTable' to be
used with any URI scheme (e.g., 'mailto:') for notifications, by specifying
'uriNotifyDomain'.
""")


class _XcmGenTrapClientSNMPAddress_Type(OctetString):
    """Custom type xcmGenTrapClientSNMPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenTrapClientSNMPAddress_Type.__name__ = "OctetString"
_XcmGenTrapClientSNMPAddress_Object = MibTableColumn
xcmGenTrapClientSNMPAddress = _XcmGenTrapClientSNMPAddress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 2),
    _XcmGenTrapClientSNMPAddress_Type()
)
xcmGenTrapClientSNMPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPAddress.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPAddress.setReference("""\
 See: 'xcmGenBaseSNMP[Domain|Version]Support'. See: 'SnmpUDPAddress' (IP addr,
UDP port - Internet), 'SNMPOSIAddress' (len, NSAP addr, TSelector - OSI),
'SNMPNBPAddress' (object, type, zone - AppleTalk), and 'SNMPIPXAddress' (net
no, MAC addr, socket - NetWare) textual conventions in the IETF SNMPv2
Transport Mappings (RFC 1449/1906). See: 'XcmSNMPNetbiosAddress' (MAC addr,
port - NetBIOS) textual conventions in the XCMI Comms Config TC. See:
'XcmSnmpIPHostnameAddress' textual convention in the XCMI Comms Config TC.
""")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPAddress.setDescription("""\
 This object is used to specify the transport address (below SNMP) which SHALL
be used by this management agent to deliver SNMP traps to the trap client
(management station or proxy). Usage: This transport address usually consists
of an underlying network layer address with a suffixed transport selector.
Usage: This object is of type 'XcmFixedLocaleDisplayString'.
""")
_XcmGenTrapClientRowStatus_Type = RowStatus
_XcmGenTrapClientRowStatus_Object = MibTableColumn
xcmGenTrapClientRowStatus = _XcmGenTrapClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 3),
    _XcmGenTrapClientRowStatus_Type()
)
xcmGenTrapClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapClientRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientRowStatus.setReference("""\
 See: 'xcmGenBaseGroupCreateSupport' in 'xcmGenBaseTable'. See:
'xcmGenTrapClientSupportMaxCount' (limit object). See: 'RowStatus' in IETF
SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX MIB
and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenTrapClientRowStatus.setDescription("""\
 This object manages the row status of this conceptual row in the
'xcmGenTrapClientTable'. Usage: It is conformant to implement this object as
read-only, however, conforming management agents are STRONGLY RECOMMENDED to
support at least read-write access to this object. Usage: Conforming management
stations, when they first create new rows in this table, SHALL set
'xcmGenTrapClientRowStatus' (to 'createAndGo'),
'xcmGenTrapClientRowPersistence' (if not 'volatile'),
'xcmGenTrapClientSNMPVersion' (if not 'snmpV1Community'), and
'xcmGenTrapClientSNMPCommunity' (if not the current managed system default in
'xcmGenBaseSNMPTrapCommunity') SIMULTANEOUSLY (in the same SNMP Set-Request
PDU). Usage: Conforming management agents SHALL NOT accept sets to
'xcmGenTrapClientRowPersistence', 'xcmGenTrapClientSNMPVersion', or
'xcmGenTrapClientSNMPCommunity' AFTER row creation (these objects are 'write-
once'). Usage: Conforming implementations which support dynamic rows SHALL
support 'createAndGo' and 'destroy' writes to this 'xcmGenTrapClientRowStatus'
row status object; and SHALL set the 'xcmGenTrapClientGroup' bit in
'xcmGenBaseGroupCreateSupport' in the 'xcmGenBaseTable'. Usage: Conforming
management agents SHOULD NOT support 'notInService(2)', 'notReady(3)', or
'createAndWait(5)'. Usage: See section 3.4 'Secure Modes of Operation' and
section 3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of
secure modes of access to this row status object.
""")
_XcmGenTrapClientIndex_Type = Ordinal32
_XcmGenTrapClientIndex_Object = MibTableColumn
xcmGenTrapClientIndex = _XcmGenTrapClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 4),
    _XcmGenTrapClientIndex_Type()
)
xcmGenTrapClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenTrapClientIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientIndex.setDescription("""\
 A unique value ASSIGNED by this host system to identify this conceptual row in
the 'xcmGenTrapClientTable'. This object is used to specify the unique client
index which was chosen FOR the trap client registered in this conceptual row
(management station or proxy) at row creation and which SHALL be used by the
trap client to create any associated conceptual rows in the
'xcmGenTrapViewTable'. Usage: Conforming management agents NEED NOT preserve
the value of this object across power cycles for 'nonvolatile' rows in the
'xcmGenTrapClientTable', but SHALL preserve the configured associations with
(any) subordinate rows in the 'xcmGenTrapViewTable'.
""")


class _XcmGenTrapClientRowPersistence_Type(XcmGenRowPersistence):
    """Custom type xcmGenTrapClientRowPersistence based on XcmGenRowPersistence"""


_XcmGenTrapClientRowPersistence_Object = MibTableColumn
xcmGenTrapClientRowPersistence = _XcmGenTrapClientRowPersistence_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 5),
    _XcmGenTrapClientRowPersistence_Type()
)
xcmGenTrapClientRowPersistence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapClientRowPersistence.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientRowPersistence.setDescription("""\
 This object is used to specify the persistence of this conceptual row in the
'xcmGenTrapClientTable' (and associated conceptual rows in the
'xcmGenTrapViewTable'). Usage: It is conformant to implement this object as
read-only, however, conforming management agents are STRONGLY RECOMMENDED to
support at least read-write access to this object. Usage: Conforming management
stations, when they first create new rows in this table, SHALL set
'xcmGenTrapClientRowStatus' (to 'createAndGo'),
'xcmGenTrapClientRowPersistence' (if not 'volatile'),
'xcmGenTrapClientSNMPVersion' (if not 'snmpV1Community'), and
'xcmGenTrapClientSNMPCommunity' (if not the current managed system default in
'xcmGenBaseSNMPTrapCommunity') SIMULTANEOUSLY (in the same SNMP Set-Request
PDU). Usage: Conforming management agents SHALL NOT accept sets to
'xcmGenTrapClientRowPersistence', 'xcmGenTrapClientSNMPVersion', or
'xcmGenTrapClientSNMPCommunity' AFTER row creation (these objects are 'write-
once'). Usage: Dynamically created rows SHALL be given 'volatile' or
'nonvolatile' persistence. Usage: Conforming management agents SHALL support
'volatile' (lost across power cycles). Usage: Conforming management agents are
STRONGLY RECOMMENDED to support 'nonvolatile' (preserved across power cycles),
but NEED NOT support any other levels of persistence.
""")


class _XcmGenTrapClientSNMPVersion_Type(XcmGenSNMPVersion):
    """Custom type xcmGenTrapClientSNMPVersion based on XcmGenSNMPVersion"""


_XcmGenTrapClientSNMPVersion_Object = MibTableColumn
xcmGenTrapClientSNMPVersion = _XcmGenTrapClientSNMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 6),
    _XcmGenTrapClientSNMPVersion_Type()
)
xcmGenTrapClientSNMPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPVersion.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPVersion.setReference("""\
 See: 'xcmGenBaseSNMP[Domain|Version]Support'.
""")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPVersion.setDescription("""\
 This object is used to specify the SNMP version (RFC 1157, RFC 1905, etc)
which SHALL be used by this management agent for SNMP protocol traffic
(transmission of SNMP traps), in the domain specified by
'xcmGenTrapClientSNMPDomain', to the trap client (management station or proxy).
Usage: Conforming management stations, when they first create new rows in this
table, SHALL set 'xcmGenTrapClientRowStatus' (to 'createAndGo'),
'xcmGenTrapClientRowPersistence' (if not 'volatile'),
'xcmGenTrapClientSNMPVersion' (if not 'snmpV1Community'), and
'xcmGenTrapClientSNMPCommunity' (if not the current managed system default in
'xcmGenBaseSNMPTrapCommunity') SIMULTANEOUSLY (in the same SNMP Set-Request
PDU). Usage: Conforming management agents SHALL NOT accept sets to
'xcmGenTrapClientRowPersistence', 'xcmGenTrapClientSNMPVersion', or
'xcmGenTrapClientSNMPCommunity' AFTER row creation (these objects are 'write-
once').
""")


class _XcmGenTrapClientSNMPCommunity_Type(OctetString):
    """Custom type xcmGenTrapClientSNMPCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmGenTrapClientSNMPCommunity_Type.__name__ = "OctetString"
_XcmGenTrapClientSNMPCommunity_Object = MibTableColumn
xcmGenTrapClientSNMPCommunity = _XcmGenTrapClientSNMPCommunity_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 13, 2, 1, 7),
    _XcmGenTrapClientSNMPCommunity_Type()
)
xcmGenTrapClientSNMPCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPCommunity.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPCommunity.setReference("""\
 See: SNMPv1c (RFC 1157) and SNMPv2c (RFC 1905). See: 'Coexistence between
SNMPv1, SNMPv2, and SNMPv3' RFC 2576, March 2000. See:
'xcmGenBaseSNMPTrapCommunity'.
""")
if mibBuilder.loadTexts:
    xcmGenTrapClientSNMPCommunity.setDescription("""\
 This object is used to specify the 'trap community name' used in all SNMPv1c
and SNMPv2c 'Inform|Trap' PDUs which SHALL be generated by this SNMP management
agent, in the domain specified by 'xcmGenTrapClientSNMPDomain', to the trap
client (management station or proxy). Note: XCMI-defined community name objects
support 64 octets maximum length and configurable charsets, for consistency
with the 'snmpCommunityName' object defined in the SNMP Community MIB defined
in RFC 2576 (March 2000). Note: Products MAY ship with a market-specific
factory default locale with a charset other than 'utf-8', eg, in Japan a
product might factory default to 'shift-jis(17)' or 'iso-2022-jp(39)'. Such
products MUST implement the 'xcmGenFixedLocalizationTable', to prevent
ambiguity about the factory default charset. Usage: For best interworking with
the ('utf-8' charset ONLY) closely related 'snmpCommunitySecurityName' object
in RFC 2576, conforming management stations and management agents SHOULD NOT
configure community names longer than 32 octets. Usage: For best interworking
with third-party applications, conforming management stations and management
agents SHOULD NOT configure empty (zero-length or all spaces) community names.
Usage: Conforming management stations, when they first create new rows in this
table, SHALL set 'xcmGenTrapClientRowStatus' (to 'createAndGo'),
'xcmGenTrapClientRowPersistence' (if not 'volatile'),
'xcmGenTrapClientSNMPVersion' (if not 'snmpV1Community'), and
'xcmGenTrapClientSNMPCommunity' (if not the current managed system default in
'xcmGenBaseSNMPTrapCommunity') SIMULTANEOUSLY (in the same SNMP Set-Request
PDU). Usage: Conforming management agents SHALL NOT accept sets to
'xcmGenTrapClientRowPersistence', 'xcmGenTrapClientSNMPVersion', or
'xcmGenTrapClientSNMPCommunity' AFTER row creation (these objects are 'write-
once'). Usage: This object SHALL be set by all XCMI conforming SNMP trap
generators (managed host systems) to the default value of
'xcmGenBaseSNMPTrapCommunity', when NOT supplied by the requesting SNMP trap
client (management station or proxy) at the time of row creation. Usage: This
object is of type 'XcmFixedLocaleDisplayString' (see DESCRIPTION of
'xcmGenBaseSNMPReadCommunity' above). If 'xcmGenLocalizationTable' or
'xcmGenFixedLocalizationTable' are not implemented on this host system, then
the charset SHALL be 'utf-8(106)', ISO 10646-1 in 'UTF-8' stream encoding.
Usage: All XCMI conforming management agents SHALL allow any defined character
in the configured charset of this object. All XCMI conforming management
stations SHOULD NOT write control characters or other non-display characters
into this object. WARNING: Changing the configured 'trap community name' of an
SNMP trap client registration will cause a COMPLETE loss of communications
unless the associated SNMP management station (client) ALSO changes over to the
new 'trap community name'!!!
""")
_XcmGenTrapView_ObjectIdentity = ObjectIdentity
xcmGenTrapView = _XcmGenTrapView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14)
)
_XcmGenTrapViewSimple_ObjectIdentity = ObjectIdentity
xcmGenTrapViewSimple = _XcmGenTrapViewSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 1)
)
if mibBuilder.loadTexts:
    xcmGenTrapViewSimple.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapViewSimple.setDescription("""\
 This subtree is current. Subordinate objects are leaf objects.
""")
_XcmGenTrapViewEntryCount_Type = Counter32
_XcmGenTrapViewEntryCount_Object = MibScalar
xcmGenTrapViewEntryCount = _XcmGenTrapViewEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 1, 1),
    _XcmGenTrapViewEntryCount_Type()
)
xcmGenTrapViewEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenTrapViewEntryCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapViewEntryCount.setDescription("""\
 The count of entries (rows) which are currently in the 'active' state in
'xcmGenTrapViewTable'.
""")
_XcmGenTrapViewSupportMaxCount_Type = Cardinal32
_XcmGenTrapViewSupportMaxCount_Object = MibScalar
xcmGenTrapViewSupportMaxCount = _XcmGenTrapViewSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 1, 2),
    _XcmGenTrapViewSupportMaxCount_Type()
)
xcmGenTrapViewSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenTrapViewSupportMaxCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapViewSupportMaxCount.setDescription("""\
 The maximum number of simultaneous entries (rows) supported for the
'xcmGenTrapViewTable'. Usage: The value zero ('0') represents 'no limit'.
""")
_XcmGenTrapViewTable_Object = MibTable
xcmGenTrapViewTable = _XcmGenTrapViewTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2)
)
if mibBuilder.loadTexts:
    xcmGenTrapViewTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapViewTable.setReference("""\
 See: View group in Historic SNMPv2 Party MIB (RFC 1447).
""")
if mibBuilder.loadTexts:
    xcmGenTrapViewTable.setDescription("""\
 A table of SNMP trap object subtrees (ie, trap scopes) registered for trap
delivery from this host system to the associated trap client (management
station or proxy). Usage: SNMP version/transport independent trap registration.
Usage: Conforming management stations SHALL create at least one subordinate row
in the 'xcmGenTrapViewTable' for each trap client that they register in the
'xcmGenTrapClientTable'. Conforming management agents SHOULD interpret a
dangling row in the 'xcmGenTrapClientTable' (no children) as 'NO traps in view'
(existing implementations of both clients and devices are known to consider
dangling rows invalid). To register for all device traps, use a single view of
'iso(1).org(3).dod(6).internet(1)'. Usage: Conforming management agents SHALL
delete any rows in the 'xcmGenTrapViewTable' which were subordinate to a
deleted row in the 'xcmGenTrapClientTable'.
""")
_XcmGenTrapViewEntry_Object = MibTableRow
xcmGenTrapViewEntry = _XcmGenTrapViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2, 1)
)
xcmGenTrapViewEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenTrapClientIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenTrapViewObjectSubtree"),
)
if mibBuilder.loadTexts:
    xcmGenTrapViewEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapViewEntry.setDescription("""\
 An entry for an SNMP trap object subtree (ie, trap scope) registered for trap
delivery from this host system to the associated trap client (management
station or proxy).
""")
_XcmGenTrapViewObjectSubtree_Type = ObjectIdentifier
_XcmGenTrapViewObjectSubtree_Object = MibTableColumn
xcmGenTrapViewObjectSubtree = _XcmGenTrapViewObjectSubtree_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2, 1, 1),
    _XcmGenTrapViewObjectSubtree_Type()
)
xcmGenTrapViewObjectSubtree.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenTrapViewObjectSubtree.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapViewObjectSubtree.setDescription("""\
 This object is used to specify the object subtree (within MIBs) which is 'in
scope' for this trap view.
""")
_XcmGenTrapViewRowStatus_Type = RowStatus
_XcmGenTrapViewRowStatus_Object = MibTableColumn
xcmGenTrapViewRowStatus = _XcmGenTrapViewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2, 1, 2),
    _XcmGenTrapViewRowStatus_Type()
)
xcmGenTrapViewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapViewRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapViewRowStatus.setReference("""\
 See: 'xcmGenBaseGroupCreateSupport' in 'xcmGenBaseTable'. See:
'xcmGenTrapViewSupportMaxCount' (limit object). See: 'RowStatus' in IETF SNMPv2
TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI HRX MIB and
'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenTrapViewRowStatus.setDescription("""\
 This object manages the row status of this conceptual row in the
'xcmGenTrapViewTable'. Usage: Conforming implementations which support dynamic
rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmGenTrapViewRowStatus' row status object; and SHALL set the
'xcmGenTrapViewGroup' bit in 'xcmGenBaseGroupCreateSupport' in the
'xcmGenBaseTable'. Usage: Conforming management agents SHOULD NOT support
'notInService(2)', 'notReady(3)', or 'createAndWait(5)'. Usage: See section 3.4
'Secure Modes of Operation' and section 3.5 'Secure SNMP Get/Set Requests' in
XCMI Security TC, for details of secure modes of access to this row status
object.
""")


class _XcmGenTrapViewNotifySeverity_Type(XcmGenNotifySeverityFilter):
    """Custom type xcmGenTrapViewNotifySeverity based on XcmGenNotifySeverityFilter"""
    defaultValue = 15


_XcmGenTrapViewNotifySeverity_Object = MibTableColumn
xcmGenTrapViewNotifySeverity = _XcmGenTrapViewNotifySeverity_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2, 1, 3),
    _XcmGenTrapViewNotifySeverity_Type()
)
xcmGenTrapViewNotifySeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapViewNotifySeverity.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapViewNotifySeverity.setReference("""\
 See: 'prtAlertSeverityLevel' in IETF Printer MIB (RFC 1759). See:
'XcmGenNotifySeverityFilter' in XCMI General TC. See:
'xcmGenBaseNotifySeveritySupport'.
""")
if mibBuilder.loadTexts:
    xcmGenTrapViewNotifySeverity.setDescription("""\
 This object is used to specify the notification severity filter used to
'screen' notifications 'in scope' for this trap view. Usage: Individual trap
definitions MAY further constrain which notifications are 'in scope'.
""")


class _XcmGenTrapViewNotifyTraining_Type(XcmGenNotifyTrainingFilter):
    """Custom type xcmGenTrapViewNotifyTraining based on XcmGenNotifyTrainingFilter"""
    defaultValue = 60


_XcmGenTrapViewNotifyTraining_Object = MibTableColumn
xcmGenTrapViewNotifyTraining = _XcmGenTrapViewNotifyTraining_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 14, 2, 1, 4),
    _XcmGenTrapViewNotifyTraining_Type()
)
xcmGenTrapViewNotifyTraining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenTrapViewNotifyTraining.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapViewNotifyTraining.setReference("""\
 See: 'prtAlertTrainingLevel' in IETF Printer MIB (RFC 1759). See:
'XcmGenNotifyTrainingFilter' in XCMI General TC. See:
'xcmGenBaseNotifyTrainingSupport'.
""")
if mibBuilder.loadTexts:
    xcmGenTrapViewNotifyTraining.setDescription("""\
 This object is used to specify the notification training filter used to
'screen' notifications 'in scope' for this trap view. Usage: Individual trap
definitions MAY further constrain which notifications are 'in scope'.
""")
_XcmGenMessageMap_ObjectIdentity = ObjectIdentity
xcmGenMessageMap = _XcmGenMessageMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 15)
)
_XcmGenMessageMapTable_Object = MibTable
xcmGenMessageMapTable = _XcmGenMessageMapTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 15, 2)
)
if mibBuilder.loadTexts:
    xcmGenMessageMapTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenMessageMapTable.setReference("""\
 See: 'XcmGenMessageMapStringLabel' in XCMI General TC.
""")
if mibBuilder.loadTexts:
    xcmGenMessageMapTable.setDescription("""\
 A table of message string labels for the current contents of static (agent-
generated) message string objects, in all MIBs implemented by this host system.
Usage: Exposes the server's message catalog for indirect search via source
message object OIDs, yielding message string labels. Usage: Supports reliable
translation by clients (managers) of static (agent-generated) message strings,
INDEPENDENT of the current language/country/charset of the message strings on
the managed host system in the conventional MIB objects. Conformance: XCMI
conforming management agents SHALL support SNMP Get requests to the
'xcmGenMessageMapTable' (ie, agents must respond to valid explicit EXACT
requests). When 'xcmGenMessageMapTable' is currently 'hidden' via
'xcmGenBaseGroupWalkHidden', XCMI conforming management agents SHALL skip over
'xcmGenMessageMapTable' to the next lexicographically higher object for GetNext
or GetBulk requests - 'xcmGenMessageMapTable' SHOULD be invisible to MIB walks,
to avoid undesirable performance degradation with third-party network
management stations and other monitoring tools.
""")
_XcmGenMessageMapEntry_Object = MibTableRow
xcmGenMessageMapEntry = _XcmGenMessageMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 15, 2, 1)
)
xcmGenMessageMapEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenMessageMapStringIndexOID"),
)
if mibBuilder.loadTexts:
    xcmGenMessageMapEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenMessageMapEntry.setDescription("""\
 A entry for a message string label for the current contents of a static
(agent-generated) message string object, in some MIB implemented by this host
system. Conformance: XCMI conforming management agents SHALL support SNMP Get
requests to the 'xcmGenMessageMapTable' (ie, agents must respond to valid
explicit EXACT requests). When 'xcmGenMessageMapTable' is currently 'hidden'
via 'xcmGenBaseGroupWalkHidden', XCMI conforming management agents SHALL skip
over 'xcmGenMessageMapTable' to the next lexicographically higher object for
GetNext or GetBulk requests - 'xcmGenMessageMapTable' SHOULD be invisible to
MIB walks, to avoid undesirable performance degradation with third-party
network management stations and other monitoring tools.
""")
_XcmGenMessageMapStringIndexOID_Type = ObjectIdentifier
_XcmGenMessageMapStringIndexOID_Object = MibTableColumn
xcmGenMessageMapStringIndexOID = _XcmGenMessageMapStringIndexOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 15, 2, 1, 1),
    _XcmGenMessageMapStringIndexOID_Type()
)
xcmGenMessageMapStringIndexOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenMessageMapStringIndexOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenMessageMapStringIndexOID.setReference("""\
 See: 'XcmGenMessageMapStringLabel' in XCMI General TC.
""")
if mibBuilder.loadTexts:
    xcmGenMessageMapStringIndexOID.setDescription("""\
 This object is used to specify the fully qualified object identifer (w/
instance suffix) of a message string object, which contains a Xerox registered
standard or experimental message string value associated with the current
message string label specified in 'xcmGenMessageMapStringLabel'.
""")
_XcmGenMessageMapStringLabel_Type = XcmGenMessageMapStringLabel
_XcmGenMessageMapStringLabel_Object = MibTableColumn
xcmGenMessageMapStringLabel = _XcmGenMessageMapStringLabel_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 15, 2, 1, 2),
    _XcmGenMessageMapStringLabel_Type()
)
xcmGenMessageMapStringLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenMessageMapStringLabel.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenMessageMapStringLabel.setReference("""\
 See: 'XcmGenMessageMapStringLabel' in XCMI General TC.
""")
if mibBuilder.loadTexts:
    xcmGenMessageMapStringLabel.setDescription("""\
 This object is used to specify a Xerox standard or experiemental message
string label associated with the current value of the message string pointed to
by 'xcmGenMessageMapStringIndexOID'. Usage: Experimental message string labels
SHOULD NOT be used in shipping versions of Xerox-branded products or services.
They exist solely to facilitate rapid product development cycles. Usage: All
Xerox message string label values SHALL be specified using display (NOT space)
characters from the IANA registered charset 'utf-8' (ie, the UTF-8 octet-stream
encoding of ISO-10646 UCS-4, described in RFC 2279). Usage: All Xerox message
string label values SHALL contain no more than 64 UTF-8 display characters AND
no more than 128 total octets (in some scripts, less than 64 characters in
UTF-8 octet-stream encoding). Note: New or refined message label syntaxes MAY
be defined in future versions of the XCMI General TC.
""")
_XcmGenMessageText_ObjectIdentity = ObjectIdentity
xcmGenMessageText = _XcmGenMessageText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16)
)
_XcmGenMessageTextTable_Object = MibTable
xcmGenMessageTextTable = _XcmGenMessageTextTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16, 2)
)
if mibBuilder.loadTexts:
    xcmGenMessageTextTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenMessageTextTable.setReference("""\
 See: 'xcmGenMessageTextTable'
""")
if mibBuilder.loadTexts:
    xcmGenMessageTextTable.setDescription("""\
 A table of message string translations for all target locales of static
(agent-generated) message string objects, in various known (agent-supported)
source message locales. Usage: Exposes the server's message catalog for
indirect search via source message object OIDs, yielding target string values.
Usage: Supports reliable translation by servers (agents) of static (agent-
generated) message strings, INDEPENDENT of the current language/country/charset
of the message strings on the managed host system in the conventional MIB
objects. Conformance: XCMI conforming management agents SHALL support SNMP Get
requests to the 'xcmGenMessageTextTable' (ie, agents must respond to valid
explicit EXACT requests). When 'xcmGenMessageTextTable' is currently 'hidden'
via 'xcmGenBaseGroupWalkHidden', XCMI conforming management agents SHALL skip
over 'xcmGenMessageTextTable' to the next lexicographically higher object for
GetNext or GetBulk requests - 'xcmGenMessageTextTable' SHOULD be invisible to
MIB walks, to avoid undesirable performance degradation with third-party
network management stations and other monitoring tools.
""")
_XcmGenMessageTextEntry_Object = MibTableRow
xcmGenMessageTextEntry = _XcmGenMessageTextEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16, 2, 1)
)
xcmGenMessageTextEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenMessageTextStringIndexOID"),
    (0, "XEROX-GENERAL-MIB", "xcmGenMessageTextTargetLocale"),
)
if mibBuilder.loadTexts:
    xcmGenMessageTextEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenMessageTextEntry.setReference("""\
 See: 'xcmGenMessageMapTable'
""")
if mibBuilder.loadTexts:
    xcmGenMessageTextEntry.setDescription("""\
 An entry for a message string translation for one target locale of a static
(agent-generated) message string object, in some MIB implemented by this host
system. Conformance: XCMI conforming management agents SHALL support SNMP Get
requests to the 'xcmGenMessageTextTable' (ie, agents must respond to valid
explicit EXACT requests). When 'xcmGenMessageTextTable' is currently 'hidden'
via 'xcmGenBaseGroupWalkHidden', XCMI conforming management agents SHALL skip
over 'xcmGenMessageTextTable' to the next lexicographically higher object for
GetNext or GetBulk requests - 'xcmGenMessageTextTable' SHOULD be invisible to
MIB walks, to avoid undesirable performance degradation with third-party
network management stations and other monitoring tools.
""")
_XcmGenMessageTextStringIndexOID_Type = ObjectIdentifier
_XcmGenMessageTextStringIndexOID_Object = MibTableColumn
xcmGenMessageTextStringIndexOID = _XcmGenMessageTextStringIndexOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16, 2, 1, 1),
    _XcmGenMessageTextStringIndexOID_Type()
)
xcmGenMessageTextStringIndexOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenMessageTextStringIndexOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenMessageTextStringIndexOID.setReference("""\
 See: 'xcmGenMessageTextTargetLocale' See: 'xcmGenMessageTextTargetString'
""")
if mibBuilder.loadTexts:
    xcmGenMessageTextStringIndexOID.setDescription("""\
 This object is used to specify the fully qualified object identifer (w/
instance suffix) of a message string object, which contains a Xerox registered
standard or experimental message string value equivalent to the target message
string translation specified in 'xcmGenMessageTextTargetString'. The locale of
this source message string is immaterial.
""")
_XcmGenMessageTextTargetLocale_Type = Ordinal32
_XcmGenMessageTextTargetLocale_Object = MibTableColumn
xcmGenMessageTextTargetLocale = _XcmGenMessageTextTargetLocale_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16, 2, 1, 2),
    _XcmGenMessageTextTargetLocale_Type()
)
xcmGenMessageTextTargetLocale.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenMessageTextTargetLocale.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenMessageTextTargetLocale.setReference("""\
 See: 'xcmGenMessageTextStringIndexOID' See: 'xcmGenMessageTextTargetString'
""")
if mibBuilder.loadTexts:
    xcmGenMessageTextTargetLocale.setDescription("""\
 This object is used to specify the locale (language/country), as a value of
'xcmGenLocalizationIndex', of the message string translation in
'xcmGenMessageTextTargetString'.
""")


class _XcmGenMessageTextTargetString_Type(XcmNamedLocaleUtf8String):
    """Custom type xcmGenMessageTextTargetString based on XcmNamedLocaleUtf8String"""
    subtypeSpec = XcmNamedLocaleUtf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenMessageTextTargetString_Type.__name__ = "XcmNamedLocaleUtf8String"
_XcmGenMessageTextTargetString_Object = MibTableColumn
xcmGenMessageTextTargetString = _XcmGenMessageTextTargetString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 16, 2, 1, 3),
    _XcmGenMessageTextTargetString_Type()
)
xcmGenMessageTextTargetString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenMessageTextTargetString.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenMessageTextTargetString.setReference("""\
 See: 'xcmGenMessageTextStringIndexOID' See: 'xcmGenMessageTextTargetLocale'
""")
if mibBuilder.loadTexts:
    xcmGenMessageTextTargetString.setDescription("""\
 This object is used to specify a translated Xerox registered message string
value associated with the current value of the message string pointed to by
'xcmGenMessageMapStringIndexOID', in the locale specified by
'xcmGenMessageTextTargetLocale'. Usage: All Xerox registered message string
values SHALL contain no more than 128 UTF-8 display characters AND no more than
255 total octets (in some scripts, less than 128 characters in UTF-8 octet-
stream encoding).
""")
_XcmGenNotifyRule_ObjectIdentity = ObjectIdentity
xcmGenNotifyRule = _XcmGenNotifyRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17)
)
_XcmGenNotifyRuleSimple_ObjectIdentity = ObjectIdentity
xcmGenNotifyRuleSimple = _XcmGenNotifyRuleSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 1)
)
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSimple.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSimple.setDescription("""\
 This subtree is current. Subordinate objects are leaf objects.
""")
_XcmGenNotifyRuleEntryCount_Type = Counter32
_XcmGenNotifyRuleEntryCount_Object = MibScalar
xcmGenNotifyRuleEntryCount = _XcmGenNotifyRuleEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 1, 1),
    _XcmGenNotifyRuleEntryCount_Type()
)
xcmGenNotifyRuleEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEntryCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEntryCount.setDescription("""\
 The count of entries (rows) which are currently in the 'active' state in
'xcmGenNotifyRuleTable'.
""")
_XcmGenNotifyRuleSupportMaxCount_Type = Cardinal32
_XcmGenNotifyRuleSupportMaxCount_Object = MibScalar
xcmGenNotifyRuleSupportMaxCount = _XcmGenNotifyRuleSupportMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 1, 2),
    _XcmGenNotifyRuleSupportMaxCount_Type()
)
xcmGenNotifyRuleSupportMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSupportMaxCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSupportMaxCount.setDescription("""\
 The maximum number of simultaneous entries (rows) supported for the
'xcmGenNotifyRuleTable'. Usage: The value zero ('0') represents 'no limit'.
""")
_XcmGenNotifyRuleTable_Object = MibTable
xcmGenNotifyRuleTable = _XcmGenNotifyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2)
)
if mibBuilder.loadTexts:
    xcmGenNotifyRuleTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleTable.setReference("""\
 See: Section 5 'Subscription Object' and Section 5.3 'Subscription Template
Attributes' and section 5.4 'Subscription Description Attributes' in IPP Notify
(draft-ietf-ipp-not-spec-06.txt).
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleTable.setDescription("""\
 A table of notification rules (recipient/event lists) registered for event
delivery from this host system. Note: In this MIB, the term 'notification rule'
is equivalent to the term 'Subscription object' in IPP Notifications. Usage:
Conforming management agents SHALL NOT accept sets to any other columnar object
in 'xcmGenNotifyRuleTable' when 'xcmGenNotifyRuleRowStatus' is 'active'.
Dynamic rows must be deleted (with 'destroy') and then recreated (with
'createAndGo') with new columnar values. Static rows must be released (with
'notInService') and then then reallocated (with 'active') with new columnar
values. Thus only a row status transition to 'active' indicates a new
notification registration by a conforming management station. Usage: Conforming
management agents SHALL delete any rows in the 'xcmGenNotifyDetailTable' which
were subordinate to a deleted row in the 'xcmGenNotifyRuleTable'.
""")
_XcmGenNotifyRuleEntry_Object = MibTableRow
xcmGenNotifyRuleEntry = _XcmGenNotifyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1)
)
xcmGenNotifyRuleEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenNotifyRuleIndex"),
)
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEntry.setDescription("""\
 An entry for a notification rule (recipient/event list) registered for event
delivery from this host system.
""")
_XcmGenNotifyRuleIndex_Type = Ordinal32
_XcmGenNotifyRuleIndex_Object = MibTableColumn
xcmGenNotifyRuleIndex = _XcmGenNotifyRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 1),
    _XcmGenNotifyRuleIndex_Type()
)
xcmGenNotifyRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleIndex.setReference("""\
 See: Section 5.4.1 'notify-subscription-id' in IPP Notify.
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleIndex.setDescription("""\
 A unique value used by this host system to identify this conceptual row in the
'xcmGenNotifyRuleTable'.
""")
_XcmGenNotifyRuleRowStatus_Type = RowStatus
_XcmGenNotifyRuleRowStatus_Object = MibTableColumn
xcmGenNotifyRuleRowStatus = _XcmGenNotifyRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 2),
    _XcmGenNotifyRuleRowStatus_Type()
)
xcmGenNotifyRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRowStatus.setReference("""\
 See: Section 11 'Operations for Notification' in IPP Notify. See: 'RowStatus'
in IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI
HRX MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRowStatus.setDescription("""\
 This object is used to display the status of this conceptual row in the
'xcmGenNotifyRuleTable'. Usage: This object MAY be used to create
('createAndGo') and delete ('destroy') dynamic rows in the
'xcmGenNotifyRuleTable'. Also used to enable ('active') and disable
('notInService') static rows in the 'xcmGenNotifyRuleTable'. Usage: Conforming
management agents SHOULD NOT support the intermediate values 'notReady(3)' or
'createAndWait(5)'. Usage: See section 3.4 'Secure Modes of Operation' and
section 3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of
secure modes of access to this row status object.
""")


class _XcmGenNotifyRuleRowPersistence_Type(XcmGenRowPersistence):
    """Custom type xcmGenNotifyRuleRowPersistence based on XcmGenRowPersistence"""


_XcmGenNotifyRuleRowPersistence_Object = MibTableColumn
xcmGenNotifyRuleRowPersistence = _XcmGenNotifyRuleRowPersistence_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 3),
    _XcmGenNotifyRuleRowPersistence_Type()
)
xcmGenNotifyRuleRowPersistence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRowPersistence.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRowPersistence.setReference("""\
 See: Section 5.3.7 'notify-lease-duration' in IPP Notify. See: Section 5.4.3
'lease-expiration-time' in IPP Notify.
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRowPersistence.setDescription("""\
 This object is used to specify the persistence of this conceptual row in the
'xcmGenNotifyRuleTable' (and associated conceptual rows in the
'xcmGenNotifyRuleDetailTable'). Usage: Dynamically created rows SHALL be given
'volatile' or 'nonvolatile' persistence. Usage: Conforming management agents
SHALL NOT accept sets to 'xcmGenNotifyRuleRowPersistence' AFTER row creation
(this object is 'write-once'). Usage: Conforming management agents SHALL
support 'volatile' (lost across power cycles), but NEED NOT support any other
levels of persistence.
""")


class _XcmGenNotifyRuleRecipientURI_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmGenNotifyRuleRecipientURI based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenNotifyRuleRecipientURI_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmGenNotifyRuleRecipientURI_Object = MibTableColumn
xcmGenNotifyRuleRecipientURI = _XcmGenNotifyRuleRecipientURI_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 4),
    _XcmGenNotifyRuleRecipientURI_Type()
)
xcmGenNotifyRuleRecipientURI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRecipientURI.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRecipientURI.setReference("""\
 See: Section 5.3.1 'notify-recipient-uri' in IPP Notify. See: Generic URI
Syntax (RFC 2396). See: The 'mailto:' URL Scheme (RFC 2368). See: Minimal PSTN
address in Internet Mail (RFC 2303). See: Minimal FAX address in Internet Mail
(RFC 2304).
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleRecipientURI.setDescription("""\
 This object is used to specify a single recipient URI (Uniform Resource
Identifier, per Generic URI Syntax, RFC 2396) for event delivery for this
notification rule (list of events), eg, - 'mailto:joe@sample.com' (Email) -
'mailto:VOICE=+3940226338@samplevoice.com' (Voice Mail) -
'mailto:FAX=+1.800.5553000/T33S=6377@sampleserv.com' (IFax) -
'ftp://machine.sample.com/pub/event_logs' (FTP logging) Usage: 'ftp:' and
'http:' URLs specify paths for event logs. Usage: MAY include parameters for
SNMP and other URL schemes (eg,
'snmp://machine.sample.com;version=2c;community=public' for SNMPv2c delivery
with community-name of 'public'). Usage: For additional recipients, use
'notifyRecipientURI' notify details in the 'xcmGenNotifyRuleDetailTable'.
""")


class _XcmGenNotifyRuleEventNames_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmGenNotifyRuleEventNames based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenNotifyRuleEventNames_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmGenNotifyRuleEventNames_Object = MibTableColumn
xcmGenNotifyRuleEventNames = _XcmGenNotifyRuleEventNames_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 5),
    _XcmGenNotifyRuleEventNames_Type()
)
xcmGenNotifyRuleEventNames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEventNames.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEventNames.setReference("""\
 See: Section 5.3.2 'notify-events' in IPP Notify. See: TRAP-TYPE and
NOTIFICATION-TYPE names in IETF/XCMI MIBs. See: 'hrDeviceStatus' in IETF HR MIB
(RFC 2790). See: 'xcmHrDevInfoXStatus' in XCMI HRX MIB. See:
'xcmHrDevInfoConditions' in XCMI HRX MIB. See: 'hrPrinterDetectedErrorState' in
IETF HR MIB (RFC 2790). See: 'prtAlertCode' in IETF Printer MIB (RFC 1759).
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEventNames.setDescription("""\
 This object is used to specify the subscribed events for this notification
rule, as a comma-delimited list of (standard) keywords or (vendor or site-
specific) names. Usage: Keywords of IPP 'notify-events' and SNMP traps and and
SNMP state/alert enumeration keywords are interoperable (eg, 'lowPaper,jammed'
from IETF HR MIB, RFC 2790). ` Usage: Standard keywords MAY be scoped with
their source, eg, 'notify-events.job-
stopped,hrPrinterDetectedErrorState.jammed', for clarity. Usage: Conforming
management stations and management agents SHALL prefix non-standard names with
'x-' for compatibility.
""")
_XcmGenNotifyRuleEventDelay_Type = Cardinal32
_XcmGenNotifyRuleEventDelay_Object = MibTableColumn
xcmGenNotifyRuleEventDelay = _XcmGenNotifyRuleEventDelay_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 6),
    _XcmGenNotifyRuleEventDelay_Type()
)
xcmGenNotifyRuleEventDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEventDelay.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEventDelay.setReference("""\
 See: Section 5.3.8 'notify-time-interval' in IPP Notify.
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleEventDelay.setDescription("""\
 This object is used to specify a delay timer in seconds for event delivery
that rate-limits (buffers) frequent events. This timer is the minimum number of
seconds between events delivered for this notification rule
('xcmGenNotifyRuleIndex'). Usage: Conforming management agents (network
devices) SHOULD support server-side buffering of events for interoperability
(and improved performance) via 'xcmGenNotifyRuleEventDelay'. Usage: Conforming
management stations (recipients) SHOULD support client-side buffering of events
for interoperability (and not depend on this 'xcmGenNotifyRuleEventDelay'
object).
""")


class _XcmGenNotifyRuleSeverityFilter_Type(XcmGenNotifySeverityFilter):
    """Custom type xcmGenNotifyRuleSeverityFilter based on XcmGenNotifySeverityFilter"""
    defaultValue = 15


_XcmGenNotifyRuleSeverityFilter_Object = MibTableColumn
xcmGenNotifyRuleSeverityFilter = _XcmGenNotifyRuleSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 7),
    _XcmGenNotifyRuleSeverityFilter_Type()
)
xcmGenNotifyRuleSeverityFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSeverityFilter.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSeverityFilter.setReference("""\
 See: 'prtAlertSeverityLevel' in IETF Printer MIB (RFC 1759). See:
'XcmGenNotifySeverityFilter' in XCMI General TC. See:
'xcmGenBaseNotifySeveritySupport' in XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSeverityFilter.setDescription("""\
 This object is used to specify the notification severity filter used to
'screen' notifications for event delivery. Usage: Notification details MAY
further constrain which notifications are 'in scope'.
""")


class _XcmGenNotifyRuleTrainingFilter_Type(XcmGenNotifyTrainingFilter):
    """Custom type xcmGenNotifyRuleTrainingFilter based on XcmGenNotifyTrainingFilter"""
    defaultValue = 60


_XcmGenNotifyRuleTrainingFilter_Object = MibTableColumn
xcmGenNotifyRuleTrainingFilter = _XcmGenNotifyRuleTrainingFilter_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 8),
    _XcmGenNotifyRuleTrainingFilter_Type()
)
xcmGenNotifyRuleTrainingFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleTrainingFilter.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleTrainingFilter.setReference("""\
 See: 'prtAlertTrainingLevel' in IETF Printer MIB (RFC 1759). See:
'XcmGenNotifyTrainingFilter' in XCMI General TC. See:
'xcmGenBaseNotifyTrainingSupport' in XCMI General MIB.
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleTrainingFilter.setDescription("""\
 This object is used to specify the notification training filter used to
'screen' notifications for event delivery. Usage: Notification details MAY
further constrain which notifications are 'in scope'.
""")


class _XcmGenNotifyRuleCharset_Type(IANACharset):
    """Custom type xcmGenNotifyRuleCharset based on IANACharset"""


_XcmGenNotifyRuleCharset_Object = MibTableColumn
xcmGenNotifyRuleCharset = _XcmGenNotifyRuleCharset_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 9),
    _XcmGenNotifyRuleCharset_Type()
)
xcmGenNotifyRuleCharset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleCharset.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleCharset.setReference("""\
 See: Section 4.1.7 'charset' and section 4.4.17 'charset-configured' in
IPP/1.1 (RFC 2911). See: Section 5.3.5 'notify-charset' in IPP Notify. See:
IANA Charset Registration Procedures (RFC 2978). See: Codes for Representation
of Names of Charsets, ISO 3166 See: Codes for Representation of Names of
Countries, ISO 639
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleCharset.setDescription("""\
 This object is used to specify the notification charset used for notification
text in event messages, specified as an IANA registered charset identifier, eg,
'MIBenum' value (per RFC 2978). Usage: If 'xcmGenNotifyRuleCharset' is
'other(1)', then the value of 'xcmGenFixedLocalizationIndex' SHALL be used for
a notification rule locale specifier for charset.
""")


class _XcmGenNotifyRuleNaturalLanguage_Type(DisplayString):
    """Custom type xcmGenNotifyRuleNaturalLanguage based on DisplayString"""
    defaultHexValue = ""


_XcmGenNotifyRuleNaturalLanguage_Object = MibTableColumn
xcmGenNotifyRuleNaturalLanguage = _XcmGenNotifyRuleNaturalLanguage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 10),
    _XcmGenNotifyRuleNaturalLanguage_Type()
)
xcmGenNotifyRuleNaturalLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleNaturalLanguage.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleNaturalLanguage.setReference("""\
 See: Section 4.1.8 'naturalLanguage' and section 4.4.19 'natural-language-
configured' in IPP/1.1 (RFC 2911). See: Section 5.3.6 'notify-natural-language'
in IPP Notify. See: IETF Tags for Identification of Languages (RFC 3066). See:
Codes for Representation of Names of Languages, ISO 3166 See: Codes for
Representation of Names of Countries, ISO 639
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleNaturalLanguage.setDescription("""\
 This object is used to specify the notification natural language used for
notification text in event messages, specified as an IETF 'language tag' (per
RFC 3066). Usage: If 'xcmGenNotifyRuleNaturalLanguage' is empty, then the value
of 'xcmGenFixedLocalizationIndex' SHALL be used for a notification rule locale
specifier for natural language.
""")
_XcmGenNotifyRuleSequenceNumber_Type = Cardinal32
_XcmGenNotifyRuleSequenceNumber_Object = MibTableColumn
xcmGenNotifyRuleSequenceNumber = _XcmGenNotifyRuleSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 17, 2, 1, 11),
    _XcmGenNotifyRuleSequenceNumber_Type()
)
xcmGenNotifyRuleSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSequenceNumber.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSequenceNumber.setReference("""\
 See: Section 5.4.2 'notify-sequence-number' in IPP Notify.
""")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleSequenceNumber.setDescription("""\
 This object is used to specify the notification sequence number last used for
event delivery for this notification rule. Usage: Conforming management agents
SHOULD include the value of 'xcmGenNotifyRuleSequenceNumber' in all event
messages.
""")
_XcmGenNotifyDetail_ObjectIdentity = ObjectIdentity
xcmGenNotifyDetail = _XcmGenNotifyDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18)
)
_XcmGenNotifyDetailSimple_ObjectIdentity = ObjectIdentity
xcmGenNotifyDetailSimple = _XcmGenNotifyDetailSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 1)
)
if mibBuilder.loadTexts:
    xcmGenNotifyDetailSimple.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailSimple.setDescription("""\
 This subtree is current. Subordinate objects are leaf objects.
""")
_XcmGenNotifyDetailEntryCount_Type = Counter32
_XcmGenNotifyDetailEntryCount_Object = MibScalar
xcmGenNotifyDetailEntryCount = _XcmGenNotifyDetailEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 1, 1),
    _XcmGenNotifyDetailEntryCount_Type()
)
xcmGenNotifyDetailEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailEntryCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailEntryCount.setDescription("""\
 The count of entries (rows) which are currently in the 'active' state in
'xcmGenNotifyDetailTable'.
""")
_XcmGenNotifyDetailSupportMax_Type = Cardinal32
_XcmGenNotifyDetailSupportMax_Object = MibScalar
xcmGenNotifyDetailSupportMax = _XcmGenNotifyDetailSupportMax_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 1, 2),
    _XcmGenNotifyDetailSupportMax_Type()
)
xcmGenNotifyDetailSupportMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailSupportMax.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailSupportMax.setDescription("""\
 The maximum number of simultaneous entries (rows) supported for the
'xcmGenNotifyDetailTable'. Usage: The value zero ('0') represents 'no limit'.
""")
_XcmGenNotifyDetailTable_Object = MibTable
xcmGenNotifyDetailTable = _XcmGenNotifyDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2)
)
if mibBuilder.loadTexts:
    xcmGenNotifyDetailTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailTable.setReference("""\
 See: Section 5 'Subscription Object' and Section 5.3 'Subscription Template
Attributes' and section 5.4 'Subscription Description Attributes' in IPP Notify
(draft-ietf-ipp-not-spec-06.txt).
""")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailTable.setDescription("""\
 A 'sparse' table of notification detail information for notification rules
configured on this host system, augmenting the basic entries in the
'xcmGenNotifyTable'. Usage: UNLIKE the 'xcmGenOptionTable' in the XCMI General
MIB (which is a unique exception), this table of 'dictionary-based' notify
details is used with DIRECT create/update operations.
""")
_XcmGenNotifyDetailEntry_Object = MibTableRow
xcmGenNotifyDetailEntry = _XcmGenNotifyDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2, 1)
)
xcmGenNotifyDetailEntry.setIndexNames(
    (0, "XEROX-GENERAL-MIB", "xcmGenNotifyRuleIndex"),
    (0, "XEROX-GENERAL-MIB", "xcmGenNotifyDetailType"),
    (0, "XEROX-GENERAL-MIB", "xcmGenNotifyDetailIndex"),
)
if mibBuilder.loadTexts:
    xcmGenNotifyDetailEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailEntry.setDescription("""\
 An entry of notification detail information for one of the notification rules
configured on this host system, augmenting the basic entry in the
'xcmGenNotifyTable'.
""")
_XcmGenNotifyDetailType_Type = XcmGenNotifyDetailType
_XcmGenNotifyDetailType_Object = MibTableColumn
xcmGenNotifyDetailType = _XcmGenNotifyDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2, 1, 1),
    _XcmGenNotifyDetailType_Type()
)
xcmGenNotifyDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailType.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailType.setReference("""\
 See: Section 5 'Subscription Object' and Section 5.3 'Subscription Template
Attributes' and section 5.4 'Subscription Description Attributes' in IPP Notify
(draft-ietf-ipp-not-spec-06.txt). See: Section 5 'Service Attributes' (encoding
rules) in Service Location Protocol v2 (RFC 2608).
""")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailType.setDescription("""\
 The type of notify detail stored in this conceptual row in
'xcmGenNotifyDetailTable'. Usage: Conforming XCMI management stations and
agents SHALL encode notify details as UTF-8 strings (like SLPv2, RFC 2608). -
Integers SHALL be encoded as (signed) decimal strings. - Booleans SHALL be
encoded as 'true' or 'false' strings. - Strings SHALL be encoded as UTF-8
character strings. - Binary data (e.g., 'userCertificate') SHALL be stored in
SLPv2 opaque encoding (leading '\FF' and escaped octets). Usage: Conformant
implementations MUST encrypt passwords, keys, and other security information in
'xcmGenNotifyDetailString'.
""")
_XcmGenNotifyDetailIndex_Type = Ordinal32
_XcmGenNotifyDetailIndex_Object = MibTableColumn
xcmGenNotifyDetailIndex = _XcmGenNotifyDetailIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2, 1, 2),
    _XcmGenNotifyDetailIndex_Type()
)
xcmGenNotifyDetailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailIndex.setDescription("""\
 A unique value used by this host system to identify this conceptual row in the
'xcmGenNotifyDetailTable', OR a common value shared across a set of related
conceptual rows (with different values of 'xcmGenNotifyDetailType'.
""")
_XcmGenNotifyDetailRowStatus_Type = RowStatus
_XcmGenNotifyDetailRowStatus_Object = MibTableColumn
xcmGenNotifyDetailRowStatus = _XcmGenNotifyDetailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2, 1, 3),
    _XcmGenNotifyDetailRowStatus_Type()
)
xcmGenNotifyDetailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailRowStatus.setReference("""\
 See: Section 11 'Operations for Notification' in IPP Notify. See: 'RowStatus'
in IETF SNMPv2 TC (RFC 1443/1903/2579). See: 'xcmHrDevMgmtCommandData' in XCMI
HRX MIB and 'xcmSecUserMgmtData' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailRowStatus.setDescription("""\
 This object is used to display the status of this conceptual row in the
'xcmGenNotifyDetailTable'. Usage: This object MAY be used to create
('createAndGo') and delete ('destroy') dynamic rows in
'xcmGenNotifyDetailTable'. Also used to enable ('active') and disable
('notInService') static rows in the 'xcmGenNotifyTable'. Usage: Conforming
management agents SHOULD NOT support the intermediate values 'notReady(3)' or
'createAndWait(5)'. Usage: See section 3.4 'Secure Modes of Operation' and
section 3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of
secure modes of access to this row status object.
""")


class _XcmGenNotifyDetailString_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmGenNotifyDetailString based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmGenNotifyDetailString_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmGenNotifyDetailString_Object = MibTableColumn
xcmGenNotifyDetailString = _XcmGenNotifyDetailString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 18, 2, 1, 4),
    _XcmGenNotifyDetailString_Type()
)
xcmGenNotifyDetailString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailString.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailString.setReference("""\
 See: Section 5 'Subscription Object' and Section 5.3 'Subscription Template
Attributes' and section 5.4 'Subscription Description Attributes' in IPP Notify
(draft-ietf-ipp-not-spec-06.txt). See: Section 5 'Service Attributes' (encoding
rules) in Service Location Protocol v2 (RFC 2608).
""")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailString.setDescription("""\
 The string notify detail value stored in this conceptual row in
'xcmGenNotifyDetailTable'. Usage: Conforming XCMI management stations and
agents SHALL encode notify details as UTF-8 strings (like SLPv2, RFC 2608). -
Integers SHALL be encoded as (signed) decimal strings. - Booleans SHALL be
encoded as 'true' or 'false' strings. - Strings SHALL be encoded as UTF-8
character strings. - Binary data (e.g., 'userCertificate') SHALL be stored in
SLPv2 opaque encoding (leading '\FF' and escaped octets). Usage: Conformant
implementations MUST encrypt passwords, keys, and other security information in
'xcmGenNotifyDetailString'.
""")

# Managed Objects groups

xcmGenBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 1)
)
xcmGenBaseGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenBaseRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSystemHrDeviceIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseGroupSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseGroupCreateSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseGroupUpdateSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseClientDataMaxSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseOptionSyntaxSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseReconfStateSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPDomainSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPTrapSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPVersionSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPReadCommunity"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPWriteCommunity"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPTrapCommunity"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseGroupWalkHidden"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseNotifySchemeSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseNotifySeveritySupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseNotifyTrainingSupport"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSystem1284DeviceId"),
        ("XEROX-GENERAL-MIB", "xcmGenBaseSNMPWarningTrapSupport"))
)
if mibBuilder.loadTexts:
    xcmGenBaseGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenBaseGroup.setDescription("""\
 General Base Group (XCMI General MIB capabilities)
""")

xcmGenCurrentLocalizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 3)
)
xcmGenCurrentLocalizationGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenCurrentLocalizationIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenCurrLocalizationRowStatus"))
)
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCurrentLocalizationGroup.setDescription("""\
 Current Localization Group (dynamic locales)
""")

xcmGenLocalizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 4)
)
xcmGenLocalizationGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenLocalizationRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenLocalizationASCIIName"),
        ("XEROX-GENERAL-MIB", "xcmGenLocalizationName"),
        ("XEROX-GENERAL-MIB", "xcmGenLocalizationLanguage"),
        ("XEROX-GENERAL-MIB", "xcmGenLocalizationCountry"),
        ("XEROX-GENERAL-MIB", "xcmGenLocalizationCharSet"))
)
if mibBuilder.loadTexts:
    xcmGenLocalizationGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLocalizationGroup.setDescription("""\
 General Localization Group (supported dynamic/static locales)
""")

xcmGenCodeIndexedStringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 5)
)
xcmGenCodeIndexedStringGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenCodeIndexedStringRowStat"),
        ("XEROX-GENERAL-MIB", "xcmGenCodeIndexedStringData"))
)
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodeIndexedStringGroup.setDescription("""\
 Code Indexed String Group (charset conversions)
""")

xcmGenCodedCharSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 6)
)
xcmGenCodedCharSetGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenCodedCharSetRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenCodedCharSetASCIIName"))
)
if mibBuilder.loadTexts:
    xcmGenCodedCharSetGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenCodedCharSetGroup.setDescription("""\
 Coded Character Set Group (supported IANA-registered charsets)
""")

xcmGenFixedLocalizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 7)
)
xcmGenFixedLocalizationGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenFixedLocalizationIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenFixedLocalizationRowStat"))
)
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenFixedLocalizationGroup.setDescription("""\
 Fixed Localization Group (static locales)
""")

xcmGenLockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 8)
)
xcmGenLockGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenLockSupportMaxTimer"),
        ("XEROX-GENERAL-MIB", "xcmGenLockCurrentMaxTimer"),
        ("XEROX-GENERAL-MIB", "xcmGenLockCurrentLockCount"),
        ("XEROX-GENERAL-MIB", "xcmGenLockHighestLockIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenLockSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenLockRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenLockOwnerString"),
        ("XEROX-GENERAL-MIB", "xcmGenLockOwnerSubtree"),
        ("XEROX-GENERAL-MIB", "xcmGenLockOwnerTimer"))
)
if mibBuilder.loadTexts:
    xcmGenLockGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenLockGroup.setDescription("""\
 General Lock Group (advisory contention locks) Implementation of this group is
STRONGLY RECOMMENDED.
""")

xcmGenReconfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 9)
)
xcmGenReconfGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenReconfActivations"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfOptionIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfOptionState"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfErrorIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenReconfErrorStatus"))
)
if mibBuilder.loadTexts:
    xcmGenReconfGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenReconfGroup.setDescription("""\
 General Reconf Group (reconfiguration requests)
""")

xcmGenOptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 10)
)
xcmGenOptionGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenOptionEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionTypeOID"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueSyntax"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueInteger"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueOID"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueString"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueLocalization"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionValueCodedCharSet"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionNextIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionPreviousIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenOptionFamilyIndex"))
)
if mibBuilder.loadTexts:
    xcmGenOptionGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenOptionGroup.setDescription("""\
 General Option Group (reconfiguration options)
""")

xcmGenClientDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 11)
)
xcmGenClientDataGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenClientDataEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataLastIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataRequestDate"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataRequestID"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataProductID"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataLength"),
        ("XEROX-GENERAL-MIB", "xcmGenClientDataString"))
)
if mibBuilder.loadTexts:
    xcmGenClientDataGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenClientDataGroup.setDescription("""\
 Client Data Group (network device installs/upgrades)
""")

xcmGenTrapClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 13)
)
xcmGenTrapClientGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenTrapClientEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientIndex"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientRowPersistence"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientSNMPVersion"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapClientSNMPCommunity"))
)
if mibBuilder.loadTexts:
    xcmGenTrapClientGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapClientGroup.setDescription("""\
 Trap Client Group (trap destination domains/addresses)
""")

xcmGenTrapViewGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 14)
)
xcmGenTrapViewGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenTrapViewEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapViewSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapViewRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapViewNotifySeverity"),
        ("XEROX-GENERAL-MIB", "xcmGenTrapViewNotifyTraining"))
)
if mibBuilder.loadTexts:
    xcmGenTrapViewGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenTrapViewGroup.setDescription("""\
 Trap View Group (trap requested object subtrees)
""")

xcmGenMessageMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 15)
)
xcmGenMessageMapGroup.setObjects(
    ("XEROX-GENERAL-MIB", "xcmGenMessageMapStringLabel")
)
if mibBuilder.loadTexts:
    xcmGenMessageMapGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenMessageMapGroup.setDescription("""\
 Message Map Group (message labels for client localization)
""")

xcmGenMessageTextGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 16)
)
xcmGenMessageTextGroup.setObjects(
    ("XEROX-GENERAL-MIB", "xcmGenMessageTextTargetString")
)
if mibBuilder.loadTexts:
    xcmGenMessageTextGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenMessageTextGroup.setDescription("""\
 Message Text Group (message lookups for agent localization)
""")

xcmGenNotifyRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 17)
)
xcmGenNotifyRuleGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenNotifyRuleEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleSupportMaxCount"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleRowPersistence"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleRecipientURI"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleEventNames"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleEventDelay"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleSeverityFilter"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleTrainingFilter"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleCharset"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleNaturalLanguage"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyRuleSequenceNumber"))
)
if mibBuilder.loadTexts:
    xcmGenNotifyRuleGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyRuleGroup.setDescription("""\
 Notify Rule Group (notification client URI and event names)
""")

xcmGenNotifyDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 2, 18)
)
xcmGenNotifyDetailGroup.setObjects(
      *(("XEROX-GENERAL-MIB", "xcmGenNotifyDetailEntryCount"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyDetailSupportMax"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyDetailRowStatus"),
        ("XEROX-GENERAL-MIB", "xcmGenNotifyDetailString"))
)
if mibBuilder.loadTexts:
    xcmGenNotifyDetailGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmGenNotifyDetailGroup.setDescription("""\
 Notify Detail Group (notification additional details)
""")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xcmGeneralMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 51, 2, 3)
)
if mibBuilder.loadTexts:
    xcmGeneralMIBCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmGeneralMIBCompliance.setDescription("""\
 The compliance statements for SNMP management agents that implement the
General MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-GENERAL-MIB",
    **{"xcmGenZeroDummy": xcmGenZeroDummy,
       "xcmGeneralMIB": xcmGeneralMIB,
       "xcmGenBase": xcmGenBase,
       "xcmGenBaseTable": xcmGenBaseTable,
       "xcmGenBaseEntry": xcmGenBaseEntry,
       "xcmGenBaseIndex": xcmGenBaseIndex,
       "xcmGenBaseRowStatus": xcmGenBaseRowStatus,
       "xcmGenBaseSystemHrDeviceIndex": xcmGenBaseSystemHrDeviceIndex,
       "xcmGenBaseGroupSupport": xcmGenBaseGroupSupport,
       "xcmGenBaseGroupCreateSupport": xcmGenBaseGroupCreateSupport,
       "xcmGenBaseGroupUpdateSupport": xcmGenBaseGroupUpdateSupport,
       "xcmGenBaseClientDataMaxSupport": xcmGenBaseClientDataMaxSupport,
       "xcmGenBaseOptionSyntaxSupport": xcmGenBaseOptionSyntaxSupport,
       "xcmGenBaseReconfStateSupport": xcmGenBaseReconfStateSupport,
       "xcmGenBaseSNMPDomainSupport": xcmGenBaseSNMPDomainSupport,
       "xcmGenBaseSNMPTrapSupport": xcmGenBaseSNMPTrapSupport,
       "xcmGenBaseSNMPVersionSupport": xcmGenBaseSNMPVersionSupport,
       "xcmGenBaseSNMPReadCommunity": xcmGenBaseSNMPReadCommunity,
       "xcmGenBaseSNMPWriteCommunity": xcmGenBaseSNMPWriteCommunity,
       "xcmGenBaseSNMPTrapCommunity": xcmGenBaseSNMPTrapCommunity,
       "xcmGenBaseGroupWalkHidden": xcmGenBaseGroupWalkHidden,
       "xcmGenBaseNotifySchemeSupport": xcmGenBaseNotifySchemeSupport,
       "xcmGenBaseNotifySeveritySupport": xcmGenBaseNotifySeveritySupport,
       "xcmGenBaseNotifyTrainingSupport": xcmGenBaseNotifyTrainingSupport,
       "xcmGenBaseSystem1284DeviceId": xcmGenBaseSystem1284DeviceId,
       "xcmGenBaseSNMPWarningTrapSupport": xcmGenBaseSNMPWarningTrapSupport,
       "xcmGeneralMIBConformance": xcmGeneralMIBConformance,
       "xcmGeneralMIBGroups": xcmGeneralMIBGroups,
       "xcmGenBaseGroup": xcmGenBaseGroup,
       "xcmGenCurrentLocalizationGroup": xcmGenCurrentLocalizationGroup,
       "xcmGenLocalizationGroup": xcmGenLocalizationGroup,
       "xcmGenCodeIndexedStringGroup": xcmGenCodeIndexedStringGroup,
       "xcmGenCodedCharSetGroup": xcmGenCodedCharSetGroup,
       "xcmGenFixedLocalizationGroup": xcmGenFixedLocalizationGroup,
       "xcmGenLockGroup": xcmGenLockGroup,
       "xcmGenReconfGroup": xcmGenReconfGroup,
       "xcmGenOptionGroup": xcmGenOptionGroup,
       "xcmGenClientDataGroup": xcmGenClientDataGroup,
       "xcmGenTrapClientGroup": xcmGenTrapClientGroup,
       "xcmGenTrapViewGroup": xcmGenTrapViewGroup,
       "xcmGenMessageMapGroup": xcmGenMessageMapGroup,
       "xcmGenMessageTextGroup": xcmGenMessageTextGroup,
       "xcmGenNotifyRuleGroup": xcmGenNotifyRuleGroup,
       "xcmGenNotifyDetailGroup": xcmGenNotifyDetailGroup,
       "xcmGeneralMIBCompliance": xcmGeneralMIBCompliance,
       "xcmGenCurrentLocalization": xcmGenCurrentLocalization,
       "xcmGenCurrentLocalizationTable": xcmGenCurrentLocalizationTable,
       "xcmGenCurrentLocalizationEntry": xcmGenCurrentLocalizationEntry,
       "xcmGenCurrentLocalizationIndex": xcmGenCurrentLocalizationIndex,
       "xcmGenCurrLocalizationRowStatus": xcmGenCurrLocalizationRowStatus,
       "xcmGenLocalization": xcmGenLocalization,
       "xcmGenLocalizationTable": xcmGenLocalizationTable,
       "xcmGenLocalizationEntry": xcmGenLocalizationEntry,
       "xcmGenLocalizationIndex": xcmGenLocalizationIndex,
       "xcmGenLocalizationRowStatus": xcmGenLocalizationRowStatus,
       "xcmGenLocalizationASCIIName": xcmGenLocalizationASCIIName,
       "xcmGenLocalizationName": xcmGenLocalizationName,
       "xcmGenLocalizationLanguage": xcmGenLocalizationLanguage,
       "xcmGenLocalizationCountry": xcmGenLocalizationCountry,
       "xcmGenLocalizationCharSet": xcmGenLocalizationCharSet,
       "xcmGenCodeIndexedString": xcmGenCodeIndexedString,
       "xcmGenCodeIndexedStringTable": xcmGenCodeIndexedStringTable,
       "xcmGenCodeIndexedStringEntry": xcmGenCodeIndexedStringEntry,
       "xcmGenCodeIndexedStringIndex": xcmGenCodeIndexedStringIndex,
       "xcmGenCodeIndexedStringCharSet": xcmGenCodeIndexedStringCharSet,
       "xcmGenCodeIndexedStringRowStat": xcmGenCodeIndexedStringRowStat,
       "xcmGenCodeIndexedStringData": xcmGenCodeIndexedStringData,
       "xcmGenCodedCharSet": xcmGenCodedCharSet,
       "xcmGenCodedCharSetTable": xcmGenCodedCharSetTable,
       "xcmGenCodedCharSetEntry": xcmGenCodedCharSetEntry,
       "xcmGenCodedCharSetCharSet": xcmGenCodedCharSetCharSet,
       "xcmGenCodedCharSetRowStatus": xcmGenCodedCharSetRowStatus,
       "xcmGenCodedCharSetASCIIName": xcmGenCodedCharSetASCIIName,
       "xcmGenFixedLocalization": xcmGenFixedLocalization,
       "xcmGenFixedLocalizationTable": xcmGenFixedLocalizationTable,
       "xcmGenFixedLocalizationEntry": xcmGenFixedLocalizationEntry,
       "xcmGenFixedLocalizationIndex": xcmGenFixedLocalizationIndex,
       "xcmGenFixedLocalizationRowStat": xcmGenFixedLocalizationRowStat,
       "xcmGenLock": xcmGenLock,
       "xcmGenLockSimple": xcmGenLockSimple,
       "xcmGenLockSupportMaxTimer": xcmGenLockSupportMaxTimer,
       "xcmGenLockCurrentMaxTimer": xcmGenLockCurrentMaxTimer,
       "xcmGenLockCurrentLockCount": xcmGenLockCurrentLockCount,
       "xcmGenLockHighestLockIndex": xcmGenLockHighestLockIndex,
       "xcmGenLockSupportMaxCount": xcmGenLockSupportMaxCount,
       "xcmGenLockTable": xcmGenLockTable,
       "xcmGenLockEntry": xcmGenLockEntry,
       "xcmGenLockIndex": xcmGenLockIndex,
       "xcmGenLockRowStatus": xcmGenLockRowStatus,
       "xcmGenLockOwnerString": xcmGenLockOwnerString,
       "xcmGenLockOwnerSubtree": xcmGenLockOwnerSubtree,
       "xcmGenLockOwnerTimer": xcmGenLockOwnerTimer,
       "xcmGenReconf": xcmGenReconf,
       "xcmGenReconfSimple": xcmGenReconfSimple,
       "xcmGenReconfActivations": xcmGenReconfActivations,
       "xcmGenReconfEntryCount": xcmGenReconfEntryCount,
       "xcmGenReconfSupportMaxCount": xcmGenReconfSupportMaxCount,
       "xcmGenReconfTable": xcmGenReconfTable,
       "xcmGenReconfEntry": xcmGenReconfEntry,
       "xcmGenReconfIndex": xcmGenReconfIndex,
       "xcmGenReconfRowStatus": xcmGenReconfRowStatus,
       "xcmGenReconfOptionIndex": xcmGenReconfOptionIndex,
       "xcmGenReconfOptionState": xcmGenReconfOptionState,
       "xcmGenReconfErrorIndex": xcmGenReconfErrorIndex,
       "xcmGenReconfErrorStatus": xcmGenReconfErrorStatus,
       "xcmGenOption": xcmGenOption,
       "xcmGenOptionSimple": xcmGenOptionSimple,
       "xcmGenOptionOperation": xcmGenOptionOperation,
       "xcmGenOptionOperationInsert": xcmGenOptionOperationInsert,
       "xcmGenOptionOperationDelete": xcmGenOptionOperationDelete,
       "xcmGenOptionOperationReplace": xcmGenOptionOperationReplace,
       "xcmGenOptionEntryCount": xcmGenOptionEntryCount,
       "xcmGenOptionSupportMaxCount": xcmGenOptionSupportMaxCount,
       "xcmGenOptionTable": xcmGenOptionTable,
       "xcmGenOptionEntry": xcmGenOptionEntry,
       "xcmGenOptionIndex": xcmGenOptionIndex,
       "xcmGenOptionRowStatus": xcmGenOptionRowStatus,
       "xcmGenOptionTypeOID": xcmGenOptionTypeOID,
       "xcmGenOptionValueSyntax": xcmGenOptionValueSyntax,
       "xcmGenOptionValueInteger": xcmGenOptionValueInteger,
       "xcmGenOptionValueOID": xcmGenOptionValueOID,
       "xcmGenOptionValueString": xcmGenOptionValueString,
       "xcmGenOptionValueLocalization": xcmGenOptionValueLocalization,
       "xcmGenOptionValueCodedCharSet": xcmGenOptionValueCodedCharSet,
       "xcmGenOptionNextIndex": xcmGenOptionNextIndex,
       "xcmGenOptionPreviousIndex": xcmGenOptionPreviousIndex,
       "xcmGenOptionFamilyIndex": xcmGenOptionFamilyIndex,
       "xcmGenClientData": xcmGenClientData,
       "xcmGenClientDataSimple": xcmGenClientDataSimple,
       "xcmGenClientDataEntryCount": xcmGenClientDataEntryCount,
       "xcmGenClientDataLastIndex": xcmGenClientDataLastIndex,
       "xcmGenClientDataSupportMaxCount": xcmGenClientDataSupportMaxCount,
       "xcmGenClientDataTable": xcmGenClientDataTable,
       "xcmGenClientDataEntry": xcmGenClientDataEntry,
       "xcmGenClientDataIndex": xcmGenClientDataIndex,
       "xcmGenClientDataRowStatus": xcmGenClientDataRowStatus,
       "xcmGenClientDataRequestDate": xcmGenClientDataRequestDate,
       "xcmGenClientDataRequestID": xcmGenClientDataRequestID,
       "xcmGenClientDataProductID": xcmGenClientDataProductID,
       "xcmGenClientDataLength": xcmGenClientDataLength,
       "xcmGenClientDataString": xcmGenClientDataString,
       "xcmGenTrapClient": xcmGenTrapClient,
       "xcmGenTrapClientSimple": xcmGenTrapClientSimple,
       "xcmGenTrapClientEntryCount": xcmGenTrapClientEntryCount,
       "xcmGenTrapClientSupportMaxCount": xcmGenTrapClientSupportMaxCount,
       "xcmGenTrapClientTable": xcmGenTrapClientTable,
       "xcmGenTrapClientEntry": xcmGenTrapClientEntry,
       "xcmGenTrapClientSNMPDomain": xcmGenTrapClientSNMPDomain,
       "xcmGenTrapClientSNMPAddress": xcmGenTrapClientSNMPAddress,
       "xcmGenTrapClientRowStatus": xcmGenTrapClientRowStatus,
       "xcmGenTrapClientIndex": xcmGenTrapClientIndex,
       "xcmGenTrapClientRowPersistence": xcmGenTrapClientRowPersistence,
       "xcmGenTrapClientSNMPVersion": xcmGenTrapClientSNMPVersion,
       "xcmGenTrapClientSNMPCommunity": xcmGenTrapClientSNMPCommunity,
       "xcmGenTrapView": xcmGenTrapView,
       "xcmGenTrapViewSimple": xcmGenTrapViewSimple,
       "xcmGenTrapViewEntryCount": xcmGenTrapViewEntryCount,
       "xcmGenTrapViewSupportMaxCount": xcmGenTrapViewSupportMaxCount,
       "xcmGenTrapViewTable": xcmGenTrapViewTable,
       "xcmGenTrapViewEntry": xcmGenTrapViewEntry,
       "xcmGenTrapViewObjectSubtree": xcmGenTrapViewObjectSubtree,
       "xcmGenTrapViewRowStatus": xcmGenTrapViewRowStatus,
       "xcmGenTrapViewNotifySeverity": xcmGenTrapViewNotifySeverity,
       "xcmGenTrapViewNotifyTraining": xcmGenTrapViewNotifyTraining,
       "xcmGenMessageMap": xcmGenMessageMap,
       "xcmGenMessageMapTable": xcmGenMessageMapTable,
       "xcmGenMessageMapEntry": xcmGenMessageMapEntry,
       "xcmGenMessageMapStringIndexOID": xcmGenMessageMapStringIndexOID,
       "xcmGenMessageMapStringLabel": xcmGenMessageMapStringLabel,
       "xcmGenMessageText": xcmGenMessageText,
       "xcmGenMessageTextTable": xcmGenMessageTextTable,
       "xcmGenMessageTextEntry": xcmGenMessageTextEntry,
       "xcmGenMessageTextStringIndexOID": xcmGenMessageTextStringIndexOID,
       "xcmGenMessageTextTargetLocale": xcmGenMessageTextTargetLocale,
       "xcmGenMessageTextTargetString": xcmGenMessageTextTargetString,
       "xcmGenNotifyRule": xcmGenNotifyRule,
       "xcmGenNotifyRuleSimple": xcmGenNotifyRuleSimple,
       "xcmGenNotifyRuleEntryCount": xcmGenNotifyRuleEntryCount,
       "xcmGenNotifyRuleSupportMaxCount": xcmGenNotifyRuleSupportMaxCount,
       "xcmGenNotifyRuleTable": xcmGenNotifyRuleTable,
       "xcmGenNotifyRuleEntry": xcmGenNotifyRuleEntry,
       "xcmGenNotifyRuleIndex": xcmGenNotifyRuleIndex,
       "xcmGenNotifyRuleRowStatus": xcmGenNotifyRuleRowStatus,
       "xcmGenNotifyRuleRowPersistence": xcmGenNotifyRuleRowPersistence,
       "xcmGenNotifyRuleRecipientURI": xcmGenNotifyRuleRecipientURI,
       "xcmGenNotifyRuleEventNames": xcmGenNotifyRuleEventNames,
       "xcmGenNotifyRuleEventDelay": xcmGenNotifyRuleEventDelay,
       "xcmGenNotifyRuleSeverityFilter": xcmGenNotifyRuleSeverityFilter,
       "xcmGenNotifyRuleTrainingFilter": xcmGenNotifyRuleTrainingFilter,
       "xcmGenNotifyRuleCharset": xcmGenNotifyRuleCharset,
       "xcmGenNotifyRuleNaturalLanguage": xcmGenNotifyRuleNaturalLanguage,
       "xcmGenNotifyRuleSequenceNumber": xcmGenNotifyRuleSequenceNumber,
       "xcmGenNotifyDetail": xcmGenNotifyDetail,
       "xcmGenNotifyDetailSimple": xcmGenNotifyDetailSimple,
       "xcmGenNotifyDetailEntryCount": xcmGenNotifyDetailEntryCount,
       "xcmGenNotifyDetailSupportMax": xcmGenNotifyDetailSupportMax,
       "xcmGenNotifyDetailTable": xcmGenNotifyDetailTable,
       "xcmGenNotifyDetailEntry": xcmGenNotifyDetailEntry,
       "xcmGenNotifyDetailType": xcmGenNotifyDetailType,
       "xcmGenNotifyDetailIndex": xcmGenNotifyDetailIndex,
       "xcmGenNotifyDetailRowStatus": xcmGenNotifyDetailRowStatus,
       "xcmGenNotifyDetailString": xcmGenNotifyDetailString}
)

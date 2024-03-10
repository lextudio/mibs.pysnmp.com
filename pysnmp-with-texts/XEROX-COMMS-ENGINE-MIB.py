"""SNMP MIB module (XEROX-COMMS-ENGINE-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-COMMS-ENGINE-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:09 2024
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

(hrDeviceIndex,
 ProductID) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex",
    "ProductID")

(ModuleCompliance,
 ObjectGroup,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "ObjectGroup",
    "NotificationGroup")

(TimeTicks,
 Integer32,
 ModuleIdentity,
 Gauge32,
 Unsigned32,
 IpAddress,
 MibIdentifier,
 iso,
 Counter64,
 Counter32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 ObjectIdentity,
 Bits,
 NotificationType) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "TimeTicks",
    "Integer32",
    "ModuleIdentity",
    "Gauge32",
    "Unsigned32",
    "IpAddress",
    "MibIdentifier",
    "iso",
    "Counter64",
    "Counter32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "ObjectIdentity",
    "Bits",
    "NotificationType")

(TextualConvention,
 DisplayString,
 DateAndTime,
 TruthValue,
 RowStatus) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TextualConvention",
    "DisplayString",
    "DateAndTime",
    "TruthValue",
    "RowStatus")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(XcmCommsStackExtPurpose,
 XcmCommsMgmtConditions,
 XcmCommsEngineGroupSupport,
 XcmCommsMgmtCommandRequest,
 XcmCommsAddressExtForm,
 XcmCommsAddressExtScope,
 XcmCommsAddressExtFanout,
 XcmCommsMgmtState,
 XcmCommsStackExtSuiteVersion,
 XcmCommsMgmtCommandData,
 XcmCommsStackPosition,
 XcmCommsStackExtProtocol,
 XcmCommsStackExtRole,
 XcmCommsStackExtLayer,
 XcmCommsStackExtSuite) = mibBuilder.importSymbols(
    "XEROX-COMMS-ENGINE-TC",
    "XcmCommsStackExtPurpose",
    "XcmCommsMgmtConditions",
    "XcmCommsEngineGroupSupport",
    "XcmCommsMgmtCommandRequest",
    "XcmCommsAddressExtForm",
    "XcmCommsAddressExtScope",
    "XcmCommsAddressExtFanout",
    "XcmCommsMgmtState",
    "XcmCommsStackExtSuiteVersion",
    "XcmCommsMgmtCommandData",
    "XcmCommsStackPosition",
    "XcmCommsStackExtProtocol",
    "XcmCommsStackExtRole",
    "XcmCommsStackExtLayer",
    "XcmCommsStackExtSuite")

(Cardinal32,
 zeroDotZero,
 XcmGenSNMPv2ErrorStatus,
 XcmFixedLocaleDisplayString,
 Ordinal32) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Cardinal32",
    "zeroDotZero",
    "XcmGenSNMPv2ErrorStatus",
    "XcmFixedLocaleDisplayString",
    "Ordinal32")

(XcmHrDevTrafficUnit,) = mibBuilder.importSymbols(
    "XEROX-HOST-RESOURCES-EXT-TC",
    "XcmHrDevTrafficUnit")


# MODULE-IDENTITY

xcmCommsEngineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61)
)
xcmCommsEngineMIB.setLastUpdated("0209170000Z")
if mibBuilder.loadTexts:
    xcmCommsEngineMIB.setOrganization("""\
Xerox Corporation - XCMI Working Group
""")
xcmCommsEngineMIB.setContactInfo("""\
 XCMI Editors Email: coherence@crt.xerox.com
""")
if mibBuilder.loadTexts:
    xcmCommsEngineMIB.setDescription("""\
Version: 5.11.pub The MIB module for detailed protocol stack graphing, and
active management of communications protocol stacks, communications end system
applications, communications intermediate systems, and communications gateways
for network accessible host systems. Usage: Note that throughout this MIB
module, the INDEX clauses referring to 'hrDeviceIndex' for the 'hrDeviceTable'
(Devices Group) of the Host Resources MIB (RFC 2790) SHALL specify host system
CPUs (ie, 'hrDeviceProcessor') and SHALL NOT specify ANY other 'hrDeviceType'.
Usage: The object 'xcmCommsStackXrefHrCommDevIndex' in the Comms Stack Xref
Group of this MIB MAY be used to specify (for 'bottom' protocol stack layers)
the corresponding value of 'hrDeviceIndex' for network, modem, serial port, and
parallel port devices. And the object 'xcmCommsStackXrefIfIndex' MAY be used to
specify the value of 'ifIndex' for the corresponding entry in the MIB-II
'ifTable' (ie, 'network interfaces'). Copyright (C) 1995-2002 Xerox
Corporation. All Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmCommsEngineZeroDummy_ObjectIdentity = ObjectIdentity
xcmCommsEngineZeroDummy = _XcmCommsEngineZeroDummy_ObjectIdentity(
    (0, 0, 61)
)
_XcmCommsEngineMIBConformance_ObjectIdentity = ObjectIdentity
xcmCommsEngineMIBConformance = _XcmCommsEngineMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2)
)
_XcmCommsEngineMIBGroups_ObjectIdentity = ObjectIdentity
xcmCommsEngineMIBGroups = _XcmCommsEngineMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2)
)
_XcmCommsEngine_ObjectIdentity = ObjectIdentity
xcmCommsEngine = _XcmCommsEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3)
)
_XcmCommsEngineTable_Object = MibTable
xcmCommsEngineTable = _XcmCommsEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2)
)
if mibBuilder.loadTexts:
    xcmCommsEngineTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineTable.setDescription("""\
A table of the communications engines installed and (possibly) running on
platforms (ie, CPUs) on this host system.
""")
_XcmCommsEngineEntry_Object = MibTableRow
xcmCommsEngineEntry = _XcmCommsEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1)
)
xcmCommsEngineEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsEngineEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineEntry.setDescription("""\
An entry for a communications engine installed and (possibly) running on a
platform (ie, CPU) on this host system. Usage: Note that values of
'hrDeviceIndex' used to reference entries in the 'xcmCommsEngineTable' SHALL
reference entries in the 'hrDeviceTable' with 'hrDeviceType' equal to
'hrDeviceProcessor' (representing host system CPUs and therefore also having
corresponding entries in the 'hrProcessorTable').
""")
_XcmCommsEngineRowStatus_Type = RowStatus
_XcmCommsEngineRowStatus_Object = MibTableColumn
xcmCommsEngineRowStatus = _XcmCommsEngineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 1),
    _XcmCommsEngineRowStatus_Type()
)
xcmCommsEngineRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsEngineTable'.
""")


class _XcmCommsEngineName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmCommsEngineName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsEngineName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmCommsEngineName_Object = MibTableColumn
xcmCommsEngineName = _XcmCommsEngineName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 2),
    _XcmCommsEngineName_Type()
)
xcmCommsEngineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineName.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineName.setDescription("""\
Human-readable name, used by system administrators and end users to identify
this communications engine for systems management. Usage: This name SHOULD be
the one normally used in a command shell for control of this communications
engine.
""")
_XcmCommsEngineStackLast_Type = Cardinal32
_XcmCommsEngineStackLast_Object = MibTableColumn
xcmCommsEngineStackLast = _XcmCommsEngineStackLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 3),
    _XcmCommsEngineStackLast_Type()
)
xcmCommsEngineStackLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineStackLast.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineStackLast.setDescription("""\
The last entry index (regardless of its current state) in the
'xcmCommsStackTable' of this communications engine, on this host system. Usage:
The last entry index explicitly bounds the valid range of 'xcmCommsStackIndex'.
""")
_XcmCommsEngineMuxLast_Type = Cardinal32
_XcmCommsEngineMuxLast_Object = MibTableColumn
xcmCommsEngineMuxLast = _XcmCommsEngineMuxLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 4),
    _XcmCommsEngineMuxLast_Type()
)
xcmCommsEngineMuxLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineMuxLast.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineMuxLast.setDescription("""\
The last entry index (regardless of its current state) in the
'xcmCommsMuxTable' of this communications engine, on this host system. Usage:
The last entry index explicitly bounds the valid range of 'xcmCommsMuxIndex'.
""")
_XcmCommsEngineAddressLast_Type = Cardinal32
_XcmCommsEngineAddressLast_Object = MibTableColumn
xcmCommsEngineAddressLast = _XcmCommsEngineAddressLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 6),
    _XcmCommsEngineAddressLast_Type()
)
xcmCommsEngineAddressLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineAddressLast.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineAddressLast.setDescription("""\
The last entry index (regardless of its current state) in the
'xcmCommsAddressTable' of this communications engine, on this host system.
Usage: The last entry index explicitly bounds the valid range of
'xcmCommsAddressIndex'.
""")
_XcmCommsEngineMgmtLast_Type = Cardinal32
_XcmCommsEngineMgmtLast_Object = MibTableColumn
xcmCommsEngineMgmtLast = _XcmCommsEngineMgmtLast_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 7),
    _XcmCommsEngineMgmtLast_Type()
)
xcmCommsEngineMgmtLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineMgmtLast.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineMgmtLast.setDescription("""\
The last entry index (regardless of its current state) in the
'xcmCommsMgmtTable' of this communications engine, on this host system. Usage:
The last entry index explicitly bounds the valid range of 'xcmCommsMgmtIndex'.
""")


class _XcmCommsEngineGroupSupport_Type(XcmCommsEngineGroupSupport):
    """Custom type xcmCommsEngineGroupSupport based on XcmCommsEngineGroupSupport"""
    defaultValue = 1


_XcmCommsEngineGroupSupport_Object = MibTableColumn
xcmCommsEngineGroupSupport = _XcmCommsEngineGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 8),
    _XcmCommsEngineGroupSupport_Type()
)
xcmCommsEngineGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineGroupSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Comms Engine MIB object groups supported by this management agent
implementation (ie, version) on this host system, specified in a bit-mask.
Usage: Conforming management agents SHALL accurately report their support for
XCMI Comms Engine MIB object groups.
""")
_XcmCommsEngineCreateSupport_Type = XcmCommsEngineGroupSupport
_XcmCommsEngineCreateSupport_Object = MibTableColumn
xcmCommsEngineCreateSupport = _XcmCommsEngineCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 9),
    _XcmCommsEngineCreateSupport_Type()
)
xcmCommsEngineCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineCreateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineCreateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Comms Engine MIB object groups supported for dynamic row creation
(via '...RowStatus') by this management agent implementation (ie, version) on
this host system, specified in a bit-mask. Usage: Conforming management agents
SHALL accurately report their support for XCMI Comms Engine MIB object groups.
""")
_XcmCommsEngineUpdateSupport_Type = XcmCommsEngineGroupSupport
_XcmCommsEngineUpdateSupport_Object = MibTableColumn
xcmCommsEngineUpdateSupport = _XcmCommsEngineUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 3, 2, 1, 10),
    _XcmCommsEngineUpdateSupport_Type()
)
xcmCommsEngineUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineUpdateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineUpdateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Comms Engine MIB object groups supported for existing row update
(via SNMP Set-Request PDUs) by this management agent implementation (ie,
version) on this host system, specified in a bit-mask. Usage: Conforming
management agents SHALL accurately report their support for XCMI Comms Engine
MIB object groups.
""")
_XcmCommsEngineExt_ObjectIdentity = ObjectIdentity
xcmCommsEngineExt = _XcmCommsEngineExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4)
)
_XcmCommsEngineExtTable_Object = MibTable
xcmCommsEngineExtTable = _XcmCommsEngineExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2)
)
if mibBuilder.loadTexts:
    xcmCommsEngineExtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineExtTable.setDescription("""\
A 'sparse' table which augments 'xcmCommsEngineTable' with additional useful
information.
""")
_XcmCommsEngineExtEntry_Object = MibTableRow
xcmCommsEngineExtEntry = _XcmCommsEngineExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1)
)
xcmCommsEngineExtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsEngineExtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineExtEntry.setDescription("""\
A 'sparse' entry which augments 'xcmCommsEngineEntry' with additional useful
information.
""")
_XcmCommsEngineExtRowStatus_Type = RowStatus
_XcmCommsEngineExtRowStatus_Object = MibTableColumn
xcmCommsEngineExtRowStatus = _XcmCommsEngineExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 1),
    _XcmCommsEngineExtRowStatus_Type()
)
xcmCommsEngineExtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineExtRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsEngineExtTable'.
""")


class _XcmCommsEngineExtState_Type(XcmCommsMgmtState):
    """Custom type xcmCommsEngineExtState based on XcmCommsMgmtState"""


_XcmCommsEngineExtState_Object = MibTableColumn
xcmCommsEngineExtState = _XcmCommsEngineExtState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 2),
    _XcmCommsEngineExtState_Type()
)
xcmCommsEngineExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtState.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineExtState.setDescription("""\
A relatively generic description of the current state of this communications
entity.
""")
_XcmCommsEngineExtConditions_Type = XcmCommsMgmtConditions
_XcmCommsEngineExtConditions_Object = MibTableColumn
xcmCommsEngineExtConditions = _XcmCommsEngineExtConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 4),
    _XcmCommsEngineExtConditions_Type()
)
xcmCommsEngineExtConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtConditions.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineExtConditions.setDescription("""\
A relatively generic description of the current conditions of this
communications entity.
""")


class _XcmCommsEngineExtVersionID_Type(ProductID):
    """Custom type xcmCommsEngineExtVersionID based on ProductID"""
    defaultValue = "(0, 0)"


_XcmCommsEngineExtVersionID_Object = MibTableColumn
xcmCommsEngineExtVersionID = _XcmCommsEngineExtVersionID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 5),
    _XcmCommsEngineExtVersionID_Type()
)
xcmCommsEngineExtVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtVersionID.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineExtVersionID.setReference("""\
See: 'hrSW[Installed|Run]ID' in the Software Installed and Software Running
groups of the IETF HR MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmCommsEngineExtVersionID.setDescription("""\
The software product ID of the SNMP sub-agent which implements the XCMI Comms
Engine MIB on this host system. Usage: This object SHALL specify the software
product ID of an SNMP sub-agent (possibly also found in a conceptual row in the
'hrSWRunTable' and/or 'hrSWInstalledTable' in the IETF HR MIB). This object
SHALL NOT specify a particular release of the XCMI Comms Engine MIB, or the
whole host system product. Note: Contrast with 'sysObjectID' for the whole SNMP
agent in the IETF MIB-II (RFC 1213) and 'hrDeviceID' for the whole device (or
whole product, in the case of 'xcmHrDevice...') in the IETF Host Resources MIB
(RFC 2790).
""")


class _XcmCommsEngineExtVersionDate_Type(DateAndTime):
    """Custom type xcmCommsEngineExtVersionDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmCommsEngineExtVersionDate_Object = MibTableColumn
xcmCommsEngineExtVersionDate = _XcmCommsEngineExtVersionDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 6),
    _XcmCommsEngineExtVersionDate_Type()
)
xcmCommsEngineExtVersionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtVersionDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineExtVersionDate.setReference("""\
See: 'hrSW[Installed|Run]ID' in the Software Installed and Software Running
groups of the IETF HR MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmCommsEngineExtVersionDate.setDescription("""\
The software build date of the SNMP sub-agent which implements the XCMI Comms
Engine MIB on this host system. Usage: This object SHALL specify the BUILD date
of the SNMP sub-agent software (not available elsewhere in IETF/XCMI MIBs).
This object SHALL NOT specify the INSTALL date of the SNMP sub-agent software
on this host system, nor the RESET date. Note: Contrast with
'hrSWInstalledDate' in the Software Installed group of the IETF Host Resources
MIB (RFC 2790), and 'xcmHrDevInfoResetDate' in the Device Info group of the
XCMI Host Resources Extensions MIB.
""")
_XcmCommsEngineExtMgmtIndex_Type = Cardinal32
_XcmCommsEngineExtMgmtIndex_Object = MibTableColumn
xcmCommsEngineExtMgmtIndex = _XcmCommsEngineExtMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 7),
    _XcmCommsEngineExtMgmtIndex_Type()
)
xcmCommsEngineExtMgmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtMgmtIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineExtMgmtIndex.setDescription("""\
The value of 'xcmCommsMgmtIndex' corresponding to a directly associated
conceptual row in the 'xcmCommsMgmtTable', or zero if this 'managed entity'
does NOT require such information.
""")


class _XcmCommsEngineExtOwnerOID_Type(ObjectIdentifier):
    """Custom type xcmCommsEngineExtOwnerOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmCommsEngineExtOwnerOID_Object = MibTableColumn
xcmCommsEngineExtOwnerOID = _XcmCommsEngineExtOwnerOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 4, 2, 1, 8),
    _XcmCommsEngineExtOwnerOID_Type()
)
xcmCommsEngineExtOwnerOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsEngineExtOwnerOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineExtOwnerOID.setDescription("""\
The OID (object identifier) of the conceptual row or simple object which
represents some 'owner entity' associated with this entry in the
'xcmCommsEngineExtTable'.
""")
_XcmCommsStack_ObjectIdentity = ObjectIdentity
xcmCommsStack = _XcmCommsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5)
)
_XcmCommsStackTable_Object = MibTable
xcmCommsStackTable = _XcmCommsStackTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2)
)
if mibBuilder.loadTexts:
    xcmCommsStackTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackTable.setDescription("""\
A table containing information on the relationships between the multiple stack
layers or sublayers (ie, protocol entities) comprising the (possibly) running
'protocol stacks' on this host system. In particular, it contains information
about which stack layer runs 'above' and 'below' which other stack layer.
""")
_XcmCommsStackEntry_Object = MibTableRow
xcmCommsStackEntry = _XcmCommsStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1)
)
xcmCommsStackEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsStackIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsStackEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackEntry.setDescription("""\
An entry for a stack layer in a protocol stack installed and (possibly) running
on this host system.
""")
_XcmCommsStackIndex_Type = Ordinal32
_XcmCommsStackIndex_Object = MibTableColumn
xcmCommsStackIndex = _XcmCommsStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 1),
    _XcmCommsStackIndex_Type()
)
xcmCommsStackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsStackIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmCommsStackTable'.
""")
_XcmCommsStackRowStatus_Type = RowStatus
_XcmCommsStackRowStatus_Object = MibTableColumn
xcmCommsStackRowStatus = _XcmCommsStackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 2),
    _XcmCommsStackRowStatus_Type()
)
xcmCommsStackRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsStackTable'.
""")


class _XcmCommsStackTypeOID_Type(ObjectIdentifier):
    """Custom type xcmCommsStackTypeOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmCommsStackTypeOID_Object = MibTableColumn
xcmCommsStackTypeOID = _XcmCommsStackTypeOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 3),
    _XcmCommsStackTypeOID_Type()
)
xcmCommsStackTypeOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackTypeOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackTypeOID.setDescription("""\
An unambiguous stack layer type, used by system administrators and end users to
identify the type of this stack layer. Usage: Since this unambiguous stack
layer type is specified as an object identifier, it MAY be taken from any IETF,
Xerox, third- party, or product-specific MIB, or it MAY simply be any IETF
SMIv2-style 'autonomous type'. Usage: Suitable values for this unambiguous
stack layer type are specified in the companion XCMI Comms Config TC (eg,
'xcmCONetwareIPX').
""")


class _XcmCommsStackName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmCommsStackName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsStackName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmCommsStackName_Object = MibTableColumn
xcmCommsStackName = _XcmCommsStackName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 4),
    _XcmCommsStackName_Type()
)
xcmCommsStackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackName.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackName.setDescription("""\
Human-readable name, used by system administrators and end users to identify
this stack layer for systems management. Usage: This name SHOULD be the one
normally used in a command shell for control of this stack layer.
""")


class _XcmCommsStackPosition_Type(XcmCommsStackPosition):
    """Custom type xcmCommsStackPosition based on XcmCommsStackPosition"""


_XcmCommsStackPosition_Object = MibTableColumn
xcmCommsStackPosition = _XcmCommsStackPosition_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 5),
    _XcmCommsStackPosition_Type()
)
xcmCommsStackPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackPosition.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackPosition.setDescription("""\
A relatively generic description of the current position of this protocol
entity (ie, this layer) in this protocol stack. Usage: A conceptual row in
'xcmCommsStackTable', which occupies a 'bottom' position in a protocol stack
AND has a corresponding row in the 'xcmCommsStackXrefTable', SHOULD have valid
references in 'xcmCommsStackXrefIfIndex' (to IETF MIB-II) and
'xcmCommsStackXrefHrCommDevIndex' (to IETF Host Resources MIB). Usage: A
conceptual row in 'xcmCommsStackTable' which occupies a 'lowerMux' and/or an
'upperMux' position in a protocol stack SHALL have one (or two) valid
corresponding conceptual rows in the 'xcmCommsMuxTable', as the conventionally
used 'xcmCommsStack[Lower|Upper]StackIndex' objects take on zero values for
multiplexors (thus breaking the graph of the stack layers, without the use of
the 'xcmCommsMuxTable').
""")
_XcmCommsStackLowerStackIndex_Type = Cardinal32
_XcmCommsStackLowerStackIndex_Object = MibTableColumn
xcmCommsStackLowerStackIndex = _XcmCommsStackLowerStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 6),
    _XcmCommsStackLowerStackIndex_Type()
)
xcmCommsStackLowerStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackLowerStackIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackLowerStackIndex.setDescription("""\
The value of 'xcmCommsStackIndex' corresponding to a next lower associated
conceptual row in the 'xcmCommsStackTable', or zero if this stack layer's
position is either 'bottom' or 'lowerMux'.
""")
_XcmCommsStackUpperStackIndex_Type = Cardinal32
_XcmCommsStackUpperStackIndex_Object = MibTableColumn
xcmCommsStackUpperStackIndex = _XcmCommsStackUpperStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 7),
    _XcmCommsStackUpperStackIndex_Type()
)
xcmCommsStackUpperStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackUpperStackIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackUpperStackIndex.setDescription("""\
The value of 'xcmCommsStackIndex' corresponding to a next higher associated
conceptual row in the 'xcmCommsStackTable', or zero if this stack layer's
position is either 'upperMux' or sometimes 'top' (see usage note below). Usage:
Only for protocol entities whose current purpose is either
'layerInterWorkingUnit' (ie, relays or gateways) or 'systemInterWorkingUnit'
(ie, application gateways), it is permitted that the stack layer whose current
position is 'top' have an upper layer index pointing to the peer entity (also
in a 'top' position) which comprises the 'other half' of a relay or gateway
between two different address domains (ie, an active protocol conversion relay)
- that is the graphed protocol stack is an inverted 'U'.
""")
_XcmCommsStackAddressIndex_Type = Cardinal32
_XcmCommsStackAddressIndex_Object = MibTableColumn
xcmCommsStackAddressIndex = _XcmCommsStackAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 8),
    _XcmCommsStackAddressIndex_Type()
)
xcmCommsStackAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackAddressIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackAddressIndex.setDescription("""\
The value of 'xcmCommsAddressIndex' corresponding to the first associated
conceptual row in the 'xcmCommsAddressTable', or zero if this 'owner entity'
does NOT require such information.
""")
_XcmCommsStackOptionIndex_Type = Cardinal32
_XcmCommsStackOptionIndex_Object = MibTableColumn
xcmCommsStackOptionIndex = _XcmCommsStackOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 9),
    _XcmCommsStackOptionIndex_Type()
)
xcmCommsStackOptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackOptionIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackOptionIndex.setDescription("""\
The value of 'xcmCommsOptionIndex' corresponding to the first associated
conceptual row in the 'xcmCommsOptionTable', or zero if this stack layer does
NOT require such information.
""")
_XcmCommsStackLowerMuxIndex_Type = Cardinal32
_XcmCommsStackLowerMuxIndex_Object = MibTableColumn
xcmCommsStackLowerMuxIndex = _XcmCommsStackLowerMuxIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 10),
    _XcmCommsStackLowerMuxIndex_Type()
)
xcmCommsStackLowerMuxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackLowerMuxIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackLowerMuxIndex.setDescription("""\
The value of 'xcmCommsMuxIndex' corresponding to the first associated
conceptual row in the 'xcmCommsMuxTable', or zero if this stack layer's
position is NOT 'lowerMux'.
""")
_XcmCommsStackUpperMuxIndex_Type = Cardinal32
_XcmCommsStackUpperMuxIndex_Object = MibTableColumn
xcmCommsStackUpperMuxIndex = _XcmCommsStackUpperMuxIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 5, 2, 1, 11),
    _XcmCommsStackUpperMuxIndex_Type()
)
xcmCommsStackUpperMuxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackUpperMuxIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackUpperMuxIndex.setDescription("""\
The value of 'xcmCommsMuxIndex' corresponding to the first associated
conceptual row in the 'xcmCommsMuxTable', or zero if this stack layer's
position is NOT 'upperMux'.
""")
_XcmCommsStackExt_ObjectIdentity = ObjectIdentity
xcmCommsStackExt = _XcmCommsStackExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6)
)
_XcmCommsStackExtTable_Object = MibTable
xcmCommsStackExtTable = _XcmCommsStackExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2)
)
if mibBuilder.loadTexts:
    xcmCommsStackExtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtTable.setDescription("""\
A 'sparse' table which augments 'xcmCommsStackTable' with additional useful
information.
""")
_XcmCommsStackExtEntry_Object = MibTableRow
xcmCommsStackExtEntry = _XcmCommsStackExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1)
)
xcmCommsStackExtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsStackIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsStackExtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtEntry.setDescription("""\
A 'sparse' entry which augments 'xcmCommsStackEntry' with additional useful
information.
""")
_XcmCommsStackExtRowStatus_Type = RowStatus
_XcmCommsStackExtRowStatus_Object = MibTableColumn
xcmCommsStackExtRowStatus = _XcmCommsStackExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 1),
    _XcmCommsStackExtRowStatus_Type()
)
xcmCommsStackExtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsStackExtTable'.
""")


class _XcmCommsStackExtState_Type(XcmCommsMgmtState):
    """Custom type xcmCommsStackExtState based on XcmCommsMgmtState"""


_XcmCommsStackExtState_Object = MibTableColumn
xcmCommsStackExtState = _XcmCommsStackExtState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 2),
    _XcmCommsStackExtState_Type()
)
xcmCommsStackExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtState.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtState.setDescription("""\
A relatively generic description of the current state of this communications
entity.
""")
_XcmCommsStackExtConditions_Type = XcmCommsMgmtConditions
_XcmCommsStackExtConditions_Object = MibTableColumn
xcmCommsStackExtConditions = _XcmCommsStackExtConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 3),
    _XcmCommsStackExtConditions_Type()
)
xcmCommsStackExtConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtConditions.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtConditions.setDescription("""\
A relatively generic description of the current conditions of this
communications entity.
""")


class _XcmCommsStackExtPurpose_Type(XcmCommsStackExtPurpose):
    """Custom type xcmCommsStackExtPurpose based on XcmCommsStackExtPurpose"""


_XcmCommsStackExtPurpose_Object = MibTableColumn
xcmCommsStackExtPurpose = _XcmCommsStackExtPurpose_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 4),
    _XcmCommsStackExtPurpose_Type()
)
xcmCommsStackExtPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtPurpose.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtPurpose.setDescription("""\
A relatively generic description of the current purpose of this stack layer
during normal operation.
""")


class _XcmCommsStackExtRole_Type(XcmCommsStackExtRole):
    """Custom type xcmCommsStackExtRole based on XcmCommsStackExtRole"""


_XcmCommsStackExtRole_Object = MibTableColumn
xcmCommsStackExtRole = _XcmCommsStackExtRole_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 5),
    _XcmCommsStackExtRole_Type()
)
xcmCommsStackExtRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtRole.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtRole.setDescription("""\
A relatively generic description of the current role of this stack layer during
normal operation.
""")


class _XcmCommsStackExtSuite_Type(XcmCommsStackExtSuite):
    """Custom type xcmCommsStackExtSuite based on XcmCommsStackExtSuite"""


_XcmCommsStackExtSuite_Object = MibTableColumn
xcmCommsStackExtSuite = _XcmCommsStackExtSuite_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 6),
    _XcmCommsStackExtSuite_Type()
)
xcmCommsStackExtSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtSuite.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtSuite.setDescription("""\
The current protocol suite of this protocol entity (stack layer or sublayer).
""")


class _XcmCommsStackExtSuiteVersion_Type(XcmCommsStackExtSuiteVersion):
    """Custom type xcmCommsStackExtSuiteVersion based on XcmCommsStackExtSuiteVersion"""


_XcmCommsStackExtSuiteVersion_Object = MibTableColumn
xcmCommsStackExtSuiteVersion = _XcmCommsStackExtSuiteVersion_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 7),
    _XcmCommsStackExtSuiteVersion_Type()
)
xcmCommsStackExtSuiteVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtSuiteVersion.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtSuiteVersion.setDescription("""\
The current protocol suite version of this protocol entity (stack layer or
sublayer).
""")


class _XcmCommsStackExtLayer_Type(XcmCommsStackExtLayer):
    """Custom type xcmCommsStackExtLayer based on XcmCommsStackExtLayer"""


_XcmCommsStackExtLayer_Object = MibTableColumn
xcmCommsStackExtLayer = _XcmCommsStackExtLayer_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 8),
    _XcmCommsStackExtLayer_Type()
)
xcmCommsStackExtLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtLayer.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtLayer.setDescription("""\
The closest approximate layer in the OSI Reference Model (CCITT X.200 | ISO
7498) to the current behavior of this stack layer or sublayer.
""")


class _XcmCommsStackExtProtocol_Type(XcmCommsStackExtProtocol):
    """Custom type xcmCommsStackExtProtocol based on XcmCommsStackExtProtocol"""


_XcmCommsStackExtProtocol_Object = MibTableColumn
xcmCommsStackExtProtocol = _XcmCommsStackExtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 9),
    _XcmCommsStackExtProtocol_Type()
)
xcmCommsStackExtProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtProtocol.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtProtocol.setDescription("""\
The specific protocol (within a given protocol suite) currently configured for
this stack layer or sublayer.
""")
_XcmCommsStackExtMgmtIndex_Type = Cardinal32
_XcmCommsStackExtMgmtIndex_Object = MibTableColumn
xcmCommsStackExtMgmtIndex = _XcmCommsStackExtMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 10),
    _XcmCommsStackExtMgmtIndex_Type()
)
xcmCommsStackExtMgmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtMgmtIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtMgmtIndex.setDescription("""\
The value of 'xcmCommsMgmtIndex' corresponding to the directly associated
conceptual row in the 'xcmCommsMgmtTable', or zero if this 'managed entity'
does NOT require such information.
""")


class _XcmCommsStackExtOwnerOID_Type(ObjectIdentifier):
    """Custom type xcmCommsStackExtOwnerOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmCommsStackExtOwnerOID_Object = MibTableColumn
xcmCommsStackExtOwnerOID = _XcmCommsStackExtOwnerOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 6, 2, 1, 11),
    _XcmCommsStackExtOwnerOID_Type()
)
xcmCommsStackExtOwnerOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackExtOwnerOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtOwnerOID.setReference("""\
See: 'prtChannelTable' in Printer MIB (RFC 1759)
""")
if mibBuilder.loadTexts:
    xcmCommsStackExtOwnerOID.setDescription("""\
The OID (object identifier) of the conceptual row or simple object which
represents some 'owner entity' associated with this entry in the
'xcmCommsStackExtTable'. Usage: A Printer Channel, for example, might choose to
specify the OID of some conceptual row in the 'prtChannelTable'.
""")
_XcmCommsStackXref_ObjectIdentity = ObjectIdentity
xcmCommsStackXref = _XcmCommsStackXref_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7)
)
_XcmCommsStackXrefTable_Object = MibTable
xcmCommsStackXrefTable = _XcmCommsStackXrefTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2)
)
if mibBuilder.loadTexts:
    xcmCommsStackXrefTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackXrefTable.setDescription("""\
A table containing optional cross reference information for the multiple stack
layers or sublayers (ie, protocol entities) comprising the (possibly) running
'protocol stacks' on this host system.
""")
_XcmCommsStackXrefEntry_Object = MibTableRow
xcmCommsStackXrefEntry = _XcmCommsStackXrefEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1)
)
xcmCommsStackXrefEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsStackIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsStackXrefEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackXrefEntry.setDescription("""\
An entry for a stack layer in a protocol stack installed and (possibly) running
on this host system.
""")
_XcmCommsStackXrefRowStatus_Type = RowStatus
_XcmCommsStackXrefRowStatus_Object = MibTableColumn
xcmCommsStackXrefRowStatus = _XcmCommsStackXrefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 1),
    _XcmCommsStackXrefRowStatus_Type()
)
xcmCommsStackXrefRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackXrefRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsStackXrefTable'.
""")
_XcmCommsStackXrefLayerMgmtIndex_Type = Cardinal32
_XcmCommsStackXrefLayerMgmtIndex_Object = MibTableColumn
xcmCommsStackXrefLayerMgmtIndex = _XcmCommsStackXrefLayerMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 2),
    _XcmCommsStackXrefLayerMgmtIndex_Type()
)
xcmCommsStackXrefLayerMgmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefLayerMgmtIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackXrefLayerMgmtIndex.setDescription("""\
The value of 'xcmCommsStackIndex' corresponding to the one-to-one associated
conceptual row in the 'xcmCommsStackTable' which has 'xcmCommsStackExtPurpose'
of 'layerManagement', or zero if this this stack layer has no associated layer
management entity.
""")
_XcmCommsStackXrefLayerSecIndex_Type = Cardinal32
_XcmCommsStackXrefLayerSecIndex_Object = MibTableColumn
xcmCommsStackXrefLayerSecIndex = _XcmCommsStackXrefLayerSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 3),
    _XcmCommsStackXrefLayerSecIndex_Type()
)
xcmCommsStackXrefLayerSecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefLayerSecIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackXrefLayerSecIndex.setDescription("""\
The value of 'xcmCommsStackIndex' corresponding to the one-to-one associated
conceptual row in the 'xcmCommsStackTable' which has 'xcmCommsStackExtPurpose'
of 'layerSecurity', or zero if this this stack layer has no associated layer
security entity.
""")
_XcmCommsStackXrefLayerIWUIndex_Type = Cardinal32
_XcmCommsStackXrefLayerIWUIndex_Object = MibTableColumn
xcmCommsStackXrefLayerIWUIndex = _XcmCommsStackXrefLayerIWUIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 4),
    _XcmCommsStackXrefLayerIWUIndex_Type()
)
xcmCommsStackXrefLayerIWUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefLayerIWUIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackXrefLayerIWUIndex.setDescription("""\
The value of 'xcmCommsStackIndex' corresponding to the one-to-one associated
conceptual row in the 'xcmCommsStackTable' which has 'xcmCommsStackExtPurpose'
of 'layerInterWorkingUnit', or zero if this this stack layer has no associated
layer relay entity.
""")
_XcmCommsStackXrefHrSWRunIndex_Type = Cardinal32
_XcmCommsStackXrefHrSWRunIndex_Object = MibTableColumn
xcmCommsStackXrefHrSWRunIndex = _XcmCommsStackXrefHrSWRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 5),
    _XcmCommsStackXrefHrSWRunIndex_Type()
)
xcmCommsStackXrefHrSWRunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefHrSWRunIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackXrefHrSWRunIndex.setDescription("""\
The value of 'hrSWRunIndex' corresponding to the directly associated conceptual
row in the 'hrSWRunTable' of the Host Resources MIB (RFC 2790), or zero if
'hrSWRunTable' is NOT implemented.
""")
_XcmCommsStackXrefHrSWInsIndex_Type = Cardinal32
_XcmCommsStackXrefHrSWInsIndex_Object = MibTableColumn
xcmCommsStackXrefHrSWInsIndex = _XcmCommsStackXrefHrSWInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 6),
    _XcmCommsStackXrefHrSWInsIndex_Type()
)
xcmCommsStackXrefHrSWInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefHrSWInsIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackXrefHrSWInsIndex.setDescription("""\
The value of 'hrSWInstalledIndex' corresponding to the directly associated
conceptual row in the 'hrSWInstalledTable' of the Host Resources MIB (RFC
2790), or zero if 'hrSWInstalledTable' is NOT implemented.
""")
_XcmCommsStackXrefIfIndex_Type = Cardinal32
_XcmCommsStackXrefIfIndex_Object = MibTableColumn
xcmCommsStackXrefIfIndex = _XcmCommsStackXrefIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 7),
    _XcmCommsStackXrefIfIndex_Type()
)
xcmCommsStackXrefIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefIfIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackXrefIfIndex.setReference("""\
See: 'xcmCommsStackPosition' and the 'InterfaceIndex' textual convention in
Evolution of the Interfaces Group of MIB-II (RFC 1573).
""")
if mibBuilder.loadTexts:
    xcmCommsStackXrefIfIndex.setDescription("""\
The value of 'ifIndex' corresponding to the directly associated conceptual row
in the 'ifTable' (Interfaces Group) of the MIB-II (RFC 1213), or zero if the
position of this stack layer is NOT 'bottom' (ie, this stack layer does NOT
represent a physical 'network interface'). Usage: This is partially a
convenience object, since given the value of 'hrDeviceIndex' for an
'hrDeviceNetwork' type device, the corresponding 'ifIndex' is found in the
mandatory entry in the 'hrNetworkTable'. However, note that for
'hrDeviceModem', 'hrDeviceSerialPort', and 'hrDeviceParallelPort' devices, the
'xcmCommsStackXrefIfIndex' object is a NECESSITY for support of this
communications engine MIB.
""")
_XcmCommsStackXrefHrCommDevIndex_Type = Cardinal32
_XcmCommsStackXrefHrCommDevIndex_Object = MibTableColumn
xcmCommsStackXrefHrCommDevIndex = _XcmCommsStackXrefHrCommDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 7, 2, 1, 8),
    _XcmCommsStackXrefHrCommDevIndex_Type()
)
xcmCommsStackXrefHrCommDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsStackXrefHrCommDevIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackXrefHrCommDevIndex.setReference("""\
See: 'xcmCommsStackPosition' and the 'hrDeviceIndex' of the Devices Group of
the Host Resources MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmCommsStackXrefHrCommDevIndex.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the directly associated
conceptual rows in the 'hrDeviceTable' and (possibly) 'hrNetworkTable' of the
Host Resources MIB (RFC 2790), or zero if the position of this stack layer is
NOT 'bottom' (ie, this stack layer does NOT represent a physical 'network
interface'). Usage: Note that for 'hrDeviceModem', 'hrDeviceSerialPort', and
'hrDeviceParallelPort' devices, there is NO corresponding entry in the
'hrNetworkTable', a subtle difference between MIB-II (RFC 1213) and the Host
Resources MIB (RFC 2790).
""")
_XcmCommsMux_ObjectIdentity = ObjectIdentity
xcmCommsMux = _XcmCommsMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8)
)
_XcmCommsMuxTable_Object = MibTable
xcmCommsMuxTable = _XcmCommsMuxTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2)
)
if mibBuilder.loadTexts:
    xcmCommsMuxTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxTable.setDescription("""\
A table containing information on the relationships between the multiple stack
layers or sublayers (ie, protocol entities) participating in a 'upper' or
'lower' multiplexor (ie, the simultaneous adjacency of two or more 'upper' or
'lower' stack layers with a single instance of a 'base' stack layer), eg, IP (a
'base' stack layer) operating below both TCP and UDP (the 'adjacent' stack
layers).
""")
_XcmCommsMuxEntry_Object = MibTableRow
xcmCommsMuxEntry = _XcmCommsMuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1)
)
xcmCommsMuxEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsMuxEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxEntry.setDescription("""\
An entry for a 'base' stack layer participating in an 'upper' or 'lower'
multiplexor.
""")
_XcmCommsMuxIndex_Type = Ordinal32
_XcmCommsMuxIndex_Object = MibTableColumn
xcmCommsMuxIndex = _XcmCommsMuxIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 1),
    _XcmCommsMuxIndex_Type()
)
xcmCommsMuxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsMuxIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmCommsMuxTable'.
""")
_XcmCommsMuxRowStatus_Type = RowStatus
_XcmCommsMuxRowStatus_Object = MibTableColumn
xcmCommsMuxRowStatus = _XcmCommsMuxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 2),
    _XcmCommsMuxRowStatus_Type()
)
xcmCommsMuxRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsMuxTable'.
""")
_XcmCommsMuxNextIndex_Type = Cardinal32
_XcmCommsMuxNextIndex_Object = MibTableColumn
xcmCommsMuxNextIndex = _XcmCommsMuxNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 3),
    _XcmCommsMuxNextIndex_Type()
)
xcmCommsMuxNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxNextIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxNextIndex.setDescription("""\
The value of 'xcmCommsMuxIndex' corresponding to a next associated conceptual
row in the 'xcmCommsMuxTable', or zero if this is the last associated
conceptual row in a given set.
""")
_XcmCommsMuxPreviousIndex_Type = Cardinal32
_XcmCommsMuxPreviousIndex_Object = MibTableColumn
xcmCommsMuxPreviousIndex = _XcmCommsMuxPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 4),
    _XcmCommsMuxPreviousIndex_Type()
)
xcmCommsMuxPreviousIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxPreviousIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxPreviousIndex.setDescription("""\
The value of 'xcmCommsMuxIndex' corresponding to a previous associated
conceptual row in the 'xcmCommsMuxTable', or zero if this is the first
associated conceptual row in a given set.
""")
_XcmCommsMuxOptionIndex_Type = Cardinal32
_XcmCommsMuxOptionIndex_Object = MibTableColumn
xcmCommsMuxOptionIndex = _XcmCommsMuxOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 5),
    _XcmCommsMuxOptionIndex_Type()
)
xcmCommsMuxOptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxOptionIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxOptionIndex.setDescription("""\
The value of 'xcmCommsOptionIndex' corresponding to the first associated
conceptual row in the 'xcmCommsOptionTable', or zero if this multiplexor entry
does NOT require such information.
""")
_XcmCommsMuxBaseStackIndex_Type = Ordinal32
_XcmCommsMuxBaseStackIndex_Object = MibTableColumn
xcmCommsMuxBaseStackIndex = _XcmCommsMuxBaseStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 6),
    _XcmCommsMuxBaseStackIndex_Type()
)
xcmCommsMuxBaseStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxBaseStackIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxBaseStackIndex.setDescription("""\
The value of 'xcmCommsStackIndex' corresponding to the base associated
conceptual row in the 'xcmCommsStackTable'.
""")
_XcmCommsMuxAdjacentStackIndex_Type = Ordinal32
_XcmCommsMuxAdjacentStackIndex_Object = MibTableColumn
xcmCommsMuxAdjacentStackIndex = _XcmCommsMuxAdjacentStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 8, 2, 1, 7),
    _XcmCommsMuxAdjacentStackIndex_Type()
)
xcmCommsMuxAdjacentStackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxAdjacentStackIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxAdjacentStackIndex.setDescription("""\
The value of 'xcmCommsStackIndex' corresponding to the adjacent associated
conceptual row in the 'xcmCommsStackTable'.
""")
_XcmCommsMuxExt_ObjectIdentity = ObjectIdentity
xcmCommsMuxExt = _XcmCommsMuxExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9)
)
_XcmCommsMuxExtTable_Object = MibTable
xcmCommsMuxExtTable = _XcmCommsMuxExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2)
)
if mibBuilder.loadTexts:
    xcmCommsMuxExtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxExtTable.setDescription("""\
A 'sparse' table which augments 'xcmCommsMuxTable' with additional useful
information.
""")
_XcmCommsMuxExtEntry_Object = MibTableRow
xcmCommsMuxExtEntry = _XcmCommsMuxExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1)
)
xcmCommsMuxExtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsMuxExtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxExtEntry.setDescription("""\
A 'sparse' entry which augments 'xcmCommsMuxEntry' with additional useful
information.
""")
_XcmCommsMuxExtRowStatus_Type = RowStatus
_XcmCommsMuxExtRowStatus_Object = MibTableColumn
xcmCommsMuxExtRowStatus = _XcmCommsMuxExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 1),
    _XcmCommsMuxExtRowStatus_Type()
)
xcmCommsMuxExtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxExtRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsMuxExtTable'.
""")


class _XcmCommsMuxExtState_Type(XcmCommsMgmtState):
    """Custom type xcmCommsMuxExtState based on XcmCommsMgmtState"""


_XcmCommsMuxExtState_Object = MibTableColumn
xcmCommsMuxExtState = _XcmCommsMuxExtState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 2),
    _XcmCommsMuxExtState_Type()
)
xcmCommsMuxExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtState.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxExtState.setDescription("""\
A relatively generic description of the current state of this communications
entity.
""")
_XcmCommsMuxExtConditions_Type = XcmCommsMgmtConditions
_XcmCommsMuxExtConditions_Object = MibTableColumn
xcmCommsMuxExtConditions = _XcmCommsMuxExtConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 3),
    _XcmCommsMuxExtConditions_Type()
)
xcmCommsMuxExtConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtConditions.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxExtConditions.setDescription("""\
A relatively generic description of the current conditions of this
communications entity.
""")
_XcmCommsMuxExtMgmtIndex_Type = Cardinal32
_XcmCommsMuxExtMgmtIndex_Object = MibTableColumn
xcmCommsMuxExtMgmtIndex = _XcmCommsMuxExtMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 4),
    _XcmCommsMuxExtMgmtIndex_Type()
)
xcmCommsMuxExtMgmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtMgmtIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxExtMgmtIndex.setDescription("""\
The value of 'xcmCommsMgmtIndex' corresponding to the directly associated
conceptual row in the 'xcmCommsMgmtTable', or zero if this 'managed entity'
does NOT require such information.
""")


class _XcmCommsMuxExtAddressIndex_Type(Cardinal32):
    """Custom type xcmCommsMuxExtAddressIndex based on Cardinal32"""
    defaultHexValue = 0


_XcmCommsMuxExtAddressIndex_Object = MibTableColumn
xcmCommsMuxExtAddressIndex = _XcmCommsMuxExtAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 5),
    _XcmCommsMuxExtAddressIndex_Type()
)
xcmCommsMuxExtAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtAddressIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxExtAddressIndex.setDescription("""\
The value of 'xcmCommsAddressIndex' corresponding to the first associated
conceptual row in the 'xcmCommsAddressTable', or zero if this 'owner entity'
does NOT require such information.
""")


class _XcmCommsMuxExtOwnerOID_Type(ObjectIdentifier):
    """Custom type xcmCommsMuxExtOwnerOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmCommsMuxExtOwnerOID_Object = MibTableColumn
xcmCommsMuxExtOwnerOID = _XcmCommsMuxExtOwnerOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 9, 2, 1, 6),
    _XcmCommsMuxExtOwnerOID_Type()
)
xcmCommsMuxExtOwnerOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMuxExtOwnerOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxExtOwnerOID.setDescription("""\
The OID (object identifier) of the conceptual row or simple object which
represents some 'owner entity' associated with this entry in the
'xcmCommsMuxExtTable'.
""")
_XcmCommsAddress_ObjectIdentity = ObjectIdentity
xcmCommsAddress = _XcmCommsAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10)
)
_XcmCommsAddressTable_Object = MibTable
xcmCommsAddressTable = _XcmCommsAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2)
)
if mibBuilder.loadTexts:
    xcmCommsAddressTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressTable.setDescription("""\
A table containing information on unicast, multicast, and broadcast addresses
(remote/local) known to this host system.
""")
_XcmCommsAddressEntry_Object = MibTableRow
xcmCommsAddressEntry = _XcmCommsAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1)
)
xcmCommsAddressEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsAddressEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressEntry.setDescription("""\
An entry containing information on one unicast, multicast, or broadcast address
(remote/local) known to this host system.
""")
_XcmCommsAddressIndex_Type = Ordinal32
_XcmCommsAddressIndex_Object = MibTableColumn
xcmCommsAddressIndex = _XcmCommsAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 1),
    _XcmCommsAddressIndex_Type()
)
xcmCommsAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsAddressIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmCommsAddressTable'.
""")
_XcmCommsAddressRowStatus_Type = RowStatus
_XcmCommsAddressRowStatus_Object = MibTableColumn
xcmCommsAddressRowStatus = _XcmCommsAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 2),
    _XcmCommsAddressRowStatus_Type()
)
xcmCommsAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsAddressTable'.
""")


class _XcmCommsAddressTypeOID_Type(ObjectIdentifier):
    """Custom type xcmCommsAddressTypeOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmCommsAddressTypeOID_Object = MibTableColumn
xcmCommsAddressTypeOID = _XcmCommsAddressTypeOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 3),
    _XcmCommsAddressTypeOID_Type()
)
xcmCommsAddressTypeOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressTypeOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressTypeOID.setDescription("""\
An unambiguous address type, used by system administrators and end users to
identify the type of this address. Usage: Since this unambiguous address type
is specified as an object identifier, it MAY be taken from any IETF, Xerox,
third- party, or product-specific MIB, or it MAY simply be any IETF SMIv2-style
'autonomous type'. Usage: Suitable values for this unambiguous address type are
specified in the companion XCMI Comms Config TC (eg, 'xcmCONetwareIPX').
""")
_XcmCommsAddressUserRole_Type = Integer32
_XcmCommsAddressUserRole_Object = MibTableColumn
xcmCommsAddressUserRole = _XcmCommsAddressUserRole_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 4),
    _XcmCommsAddressUserRole_Type()
)
xcmCommsAddressUserRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressUserRole.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressUserRole.setReference("""\
See: 'XcmSecUserRole' in the XCMI Security/AAA TC. See:
'xcmDevHelpCommsAddressIndex' in the XCMI Ext to IETF Host Resources MIB.
""")
if mibBuilder.loadTexts:
    xcmCommsAddressUserRole.setDescription("""\
An unambiguous address user role, used by system administrators and end users
to identify the user role of this address. Usage: This unambiguous address user
role is specified by a value defined in the textual convention 'XcmSecUserRole'
in the XCMI Security/AAA TC. Usage: This unambiguous address user role is
weakly typed here to avoid cyclic compilation dependencies between XCMI MIBs.
Usage: A chain of 'xcmCommsAddressEntry' objects MAY be pointed to by
'xcmDevHelpCommsAddressIndex' in the Device Help group of the XCMI Ext to IETF
Host Resources MIB. In this case, the 'xcmCommsAddressTypeOID' object MAY
contain values such as 'xcmCOOsiwanPSTNAddress' (analog phone number),
'xcmCOOsiwanFaxAddress' (fax phone number), etc, taken from the XCMI Comms
Config TC. In this case, the 'xcmCommsAddressUserRole' object MAY be used to
specify the role of the system admin, system operator, etc (whose name is
specified by 'xcmCommsAddressName', address format is specified by
'xcmCommsAddressTypeOID', and actual address is specified by
'xcmCommsAddressCanonical').
""")


class _XcmCommsAddressName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmCommsAddressName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsAddressName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmCommsAddressName_Object = MibTableColumn
xcmCommsAddressName = _XcmCommsAddressName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 5),
    _XcmCommsAddressName_Type()
)
xcmCommsAddressName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressName.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressName.setDescription("""\
Human-readable name, used by system administrators and end users to identify
this protocol entity. Usage: This name SHOULD be the one normally used in a
command shell for control of this protocol entity. Usage: When a chain of
'xcmCommsAddressEntry' objects is pointed to by 'xcmHrDevHelpCommsAddressIndex'
in the Device Help group of the XCMI Ext to IETF Host Resources MIB (see the
'xcmCommsAddressUserRole' object above) special semantics apply. In this case,
the 'xcmCommsAddressName' object MAY be used to specify the name of the system
admin, system operator, etc (whose role is specified by
'xcmCommsAddressUserRole', address format is specified by
'xcmCommsAddressTypeOID', and actual address is specified by
'xcmCommsAddressCanonical').
""")


class _XcmCommsAddressCanonical_Type(OctetString):
    """Custom type xcmCommsAddressCanonical based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsAddressCanonical_Type.__name__ = "OctetString"
_XcmCommsAddressCanonical_Object = MibTableColumn
xcmCommsAddressCanonical = _XcmCommsAddressCanonical_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 6),
    _XcmCommsAddressCanonical_Type()
)
xcmCommsAddressCanonical.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressCanonical.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressCanonical.setDescription("""\
The current canonical address of this protocol entity.
""")
_XcmCommsAddressNextIndex_Type = Cardinal32
_XcmCommsAddressNextIndex_Object = MibTableColumn
xcmCommsAddressNextIndex = _XcmCommsAddressNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 7),
    _XcmCommsAddressNextIndex_Type()
)
xcmCommsAddressNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressNextIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressNextIndex.setDescription("""\
The value of 'xcmCommsAddressIndex' corresponding to a next associated
conceptual row in the 'xcmCommsAddressTable', or zero if this is the last
associated conceptual row in a given set. Usage: A locally administered
'directory' MAY be searched and/or managed via use of the
'xcmCommsAddressNextIndex' and the 'xcmCommsAddressPreviousIndex' objects
referenced from each base protocol entity (ie, stack layer).
""")
_XcmCommsAddressPreviousIndex_Type = Cardinal32
_XcmCommsAddressPreviousIndex_Object = MibTableColumn
xcmCommsAddressPreviousIndex = _XcmCommsAddressPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 8),
    _XcmCommsAddressPreviousIndex_Type()
)
xcmCommsAddressPreviousIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressPreviousIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressPreviousIndex.setDescription("""\
The value of 'xcmCommsAddressIndex' corresponding to a previous associated
conceptual row in the 'xcmCommsAddressTable', or zero if this is the first
associated conceptual row in a given set.
""")


class _XcmCommsAddressOptionIndex_Type(Cardinal32):
    """Custom type xcmCommsAddressOptionIndex based on Cardinal32"""
    defaultHexValue = 0


_XcmCommsAddressOptionIndex_Object = MibTableColumn
xcmCommsAddressOptionIndex = _XcmCommsAddressOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 10, 2, 1, 9),
    _XcmCommsAddressOptionIndex_Type()
)
xcmCommsAddressOptionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressOptionIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressOptionIndex.setDescription("""\
The value of 'xcmCommsOptionIndex' corresponding to the first associated
conceptual row in the 'xcmCommsOptionTable', or zero if this address entry does
NOT require such information.
""")
_XcmCommsAddressExt_ObjectIdentity = ObjectIdentity
xcmCommsAddressExt = _XcmCommsAddressExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11)
)
_XcmCommsAddressExtTable_Object = MibTable
xcmCommsAddressExtTable = _XcmCommsAddressExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2)
)
if mibBuilder.loadTexts:
    xcmCommsAddressExtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressExtTable.setDescription("""\
A 'sparse' table which augments 'xcmCommsAddressTable' with additional useful
information.
""")
_XcmCommsAddressExtEntry_Object = MibTableRow
xcmCommsAddressExtEntry = _XcmCommsAddressExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1)
)
xcmCommsAddressExtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsAddressExtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressExtEntry.setDescription("""\
A 'sparse' entry which augments 'xcmCommsAddressEntry' with additional useful
information.
""")
_XcmCommsAddressExtRowStatus_Type = RowStatus
_XcmCommsAddressExtRowStatus_Object = MibTableColumn
xcmCommsAddressExtRowStatus = _XcmCommsAddressExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 1),
    _XcmCommsAddressExtRowStatus_Type()
)
xcmCommsAddressExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressExtRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsAddressExtTable'.
""")


class _XcmCommsAddressExtState_Type(XcmCommsMgmtState):
    """Custom type xcmCommsAddressExtState based on XcmCommsMgmtState"""


_XcmCommsAddressExtState_Object = MibTableColumn
xcmCommsAddressExtState = _XcmCommsAddressExtState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 2),
    _XcmCommsAddressExtState_Type()
)
xcmCommsAddressExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAddressExtState.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressExtState.setDescription("""\
A relatively generic description of the current state of this communications
entity.
""")
_XcmCommsAddressExtConditions_Type = XcmCommsMgmtConditions
_XcmCommsAddressExtConditions_Object = MibTableColumn
xcmCommsAddressExtConditions = _XcmCommsAddressExtConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 3),
    _XcmCommsAddressExtConditions_Type()
)
xcmCommsAddressExtConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAddressExtConditions.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressExtConditions.setDescription("""\
A relatively generic description of the current conditions of this
communications entity.
""")


class _XcmCommsAddressExtForm_Type(XcmCommsAddressExtForm):
    """Custom type xcmCommsAddressExtForm based on XcmCommsAddressExtForm"""


_XcmCommsAddressExtForm_Object = MibTableColumn
xcmCommsAddressExtForm = _XcmCommsAddressExtForm_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 4),
    _XcmCommsAddressExtForm_Type()
)
xcmCommsAddressExtForm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtForm.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressExtForm.setDescription("""\
The current address form of this protocol entity.
""")


class _XcmCommsAddressExtScope_Type(XcmCommsAddressExtScope):
    """Custom type xcmCommsAddressExtScope based on XcmCommsAddressExtScope"""


_XcmCommsAddressExtScope_Object = MibTableColumn
xcmCommsAddressExtScope = _XcmCommsAddressExtScope_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 5),
    _XcmCommsAddressExtScope_Type()
)
xcmCommsAddressExtScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtScope.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressExtScope.setDescription("""\
The current address scope of this protocol entity.
""")


class _XcmCommsAddressExtFanout_Type(XcmCommsAddressExtFanout):
    """Custom type xcmCommsAddressExtFanout based on XcmCommsAddressExtFanout"""


_XcmCommsAddressExtFanout_Object = MibTableColumn
xcmCommsAddressExtFanout = _XcmCommsAddressExtFanout_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 6),
    _XcmCommsAddressExtFanout_Type()
)
xcmCommsAddressExtFanout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtFanout.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressExtFanout.setDescription("""\
The current address fan out of this protocol entity.
""")


class _XcmCommsAddressExtMgmtIndex_Type(Cardinal32):
    """Custom type xcmCommsAddressExtMgmtIndex based on Cardinal32"""
    defaultHexValue = 0


_XcmCommsAddressExtMgmtIndex_Object = MibTableColumn
xcmCommsAddressExtMgmtIndex = _XcmCommsAddressExtMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 7),
    _XcmCommsAddressExtMgmtIndex_Type()
)
xcmCommsAddressExtMgmtIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtMgmtIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressExtMgmtIndex.setDescription("""\
The value of 'xcmCommsMgmtIndex' corresponding to the directly associated
conceptual row in the 'xcmCommsMgmtTable', or zero if this 'managed entity'
does NOT require such information.
""")


class _XcmCommsAddressExtOwnerOID_Type(ObjectIdentifier):
    """Custom type xcmCommsAddressExtOwnerOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmCommsAddressExtOwnerOID_Object = MibTableColumn
xcmCommsAddressExtOwnerOID = _XcmCommsAddressExtOwnerOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 11, 2, 1, 8),
    _XcmCommsAddressExtOwnerOID_Type()
)
xcmCommsAddressExtOwnerOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsAddressExtOwnerOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressExtOwnerOID.setDescription("""\
The OID (object identifier) of the conceptual row or simple object which
represents some 'owner entity' associated with this entry in the
'xcmCommsAddressExtTable'.
""")
_XcmCommsTraffic_ObjectIdentity = ObjectIdentity
xcmCommsTraffic = _XcmCommsTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12)
)
_XcmCommsTrafficTable_Object = MibTable
xcmCommsTrafficTable = _XcmCommsTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2)
)
if mibBuilder.loadTexts:
    xcmCommsTrafficTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsTrafficTable.setDescription("""\
A table containing input and output traffic counters for stack layers.
""")
_XcmCommsTrafficEntry_Object = MibTableRow
xcmCommsTrafficEntry = _XcmCommsTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1)
)
xcmCommsTrafficEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsStackIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsTrafficEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsTrafficEntry.setDescription("""\
An entry containing input and output traffic counters for this stack layer.
""")
_XcmCommsTrafficRowStatus_Type = RowStatus
_XcmCommsTrafficRowStatus_Object = MibTableColumn
xcmCommsTrafficRowStatus = _XcmCommsTrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 1),
    _XcmCommsTrafficRowStatus_Type()
)
xcmCommsTrafficRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsTrafficRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsTrafficTable'.
""")


class _XcmCommsTrafficInputUnit_Type(XcmHrDevTrafficUnit):
    """Custom type xcmCommsTrafficInputUnit based on XcmHrDevTrafficUnit"""


_XcmCommsTrafficInputUnit_Object = MibTableColumn
xcmCommsTrafficInputUnit = _XcmCommsTrafficInputUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 2),
    _XcmCommsTrafficInputUnit_Type()
)
xcmCommsTrafficInputUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficInputUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsTrafficInputUnit.setDescription("""\
A layer input unit, used by system administrators and end users of this layer
for traffic counters.
""")


class _XcmCommsTrafficOutputUnit_Type(XcmHrDevTrafficUnit):
    """Custom type xcmCommsTrafficOutputUnit based on XcmHrDevTrafficUnit"""


_XcmCommsTrafficOutputUnit_Object = MibTableColumn
xcmCommsTrafficOutputUnit = _XcmCommsTrafficOutputUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 3),
    _XcmCommsTrafficOutputUnit_Type()
)
xcmCommsTrafficOutputUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficOutputUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsTrafficOutputUnit.setDescription("""\
A layer output unit, used by system administrators and end users of this layer
for traffic counters.
""")
_XcmCommsTrafficInputCount_Type = Counter32
_XcmCommsTrafficInputCount_Object = MibTableColumn
xcmCommsTrafficInputCount = _XcmCommsTrafficInputCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 4),
    _XcmCommsTrafficInputCount_Type()
)
xcmCommsTrafficInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficInputCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsTrafficInputCount.setDescription("""\
A layer input traffic count, used by system administrators and end users of
this layer. Usage: Although no default value ('DEFVAL' clause) is permitted (by
IETF SMIv2) for this counter, conforming host systems SHALL zero this counter
upon conceptual row creation.
""")
_XcmCommsTrafficOutputCount_Type = Counter32
_XcmCommsTrafficOutputCount_Object = MibTableColumn
xcmCommsTrafficOutputCount = _XcmCommsTrafficOutputCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 5),
    _XcmCommsTrafficOutputCount_Type()
)
xcmCommsTrafficOutputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficOutputCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsTrafficOutputCount.setDescription("""\
A layer output traffic count, used by system administrators and end users of
this layer. Usage: Although no default value ('DEFVAL' clause) is permitted (by
IETF SMIv2) for this counter, conforming host systems SHALL zero this counter
upon conceptual row creation.
""")
_XcmCommsTrafficInputErrors_Type = Counter32
_XcmCommsTrafficInputErrors_Object = MibTableColumn
xcmCommsTrafficInputErrors = _XcmCommsTrafficInputErrors_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 6),
    _XcmCommsTrafficInputErrors_Type()
)
xcmCommsTrafficInputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficInputErrors.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsTrafficInputErrors.setDescription("""\
A layer input errors count, used by system administrators and end users of this
layer. Usage: Although no default value ('DEFVAL' clause) is permitted (by IETF
SMIv2) for this counter, conforming host systems SHALL zero this counter upon
conceptual row creation.
""")
_XcmCommsTrafficOutputErrors_Type = Counter32
_XcmCommsTrafficOutputErrors_Object = MibTableColumn
xcmCommsTrafficOutputErrors = _XcmCommsTrafficOutputErrors_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 12, 2, 1, 7),
    _XcmCommsTrafficOutputErrors_Type()
)
xcmCommsTrafficOutputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsTrafficOutputErrors.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsTrafficOutputErrors.setDescription("""\
A layer output errors count, used by system administrators and end users of
this layer. Usage: Although no default value ('DEFVAL' clause) is permitted (by
IETF SMIv2) for this counter, conforming host systems SHALL zero this counter
upon conceptual row creation.
""")
_XcmCommsAccess_ObjectIdentity = ObjectIdentity
xcmCommsAccess = _XcmCommsAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13)
)
_XcmCommsAccessTable_Object = MibTable
xcmCommsAccessTable = _XcmCommsAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2)
)
if mibBuilder.loadTexts:
    xcmCommsAccessTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAccessTable.setDescription("""\
A table containing current, high-water mark, and maximum permitted values for
both connection (or association) and message (or datagram) ports at the upper
sides (ie, service provider interfaces) of stack layers.
""")
_XcmCommsAccessEntry_Object = MibTableRow
xcmCommsAccessEntry = _XcmCommsAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1)
)
xcmCommsAccessEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsStackIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsAccessEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAccessEntry.setDescription("""\
A table containing current, high-water mark, and maximum permitted values for
both connection (or association) and message (or datagram) ports at the upper
side (ie, service provider interface) of this stack layer.
""")
_XcmCommsAccessRowStatus_Type = RowStatus
_XcmCommsAccessRowStatus_Object = MibTableColumn
xcmCommsAccessRowStatus = _XcmCommsAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 1),
    _XcmCommsAccessRowStatus_Type()
)
xcmCommsAccessRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAccessRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsAccessTable'.
""")
_XcmCommsAccessConnectPorts_Type = Gauge32
_XcmCommsAccessConnectPorts_Object = MibTableColumn
xcmCommsAccessConnectPorts = _XcmCommsAccessConnectPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 2),
    _XcmCommsAccessConnectPorts_Type()
)
xcmCommsAccessConnectPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessConnectPorts.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAccessConnectPorts.setDescription("""\
The current number of connection (or association) ports open at the upper side
(ie, service provider interface) of this layer.
""")
_XcmCommsAccessHighConnectPorts_Type = Gauge32
_XcmCommsAccessHighConnectPorts_Object = MibTableColumn
xcmCommsAccessHighConnectPorts = _XcmCommsAccessHighConnectPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 3),
    _XcmCommsAccessHighConnectPorts_Type()
)
xcmCommsAccessHighConnectPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessHighConnectPorts.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAccessHighConnectPorts.setDescription("""\
The highest number of connection (or association) ports open at the upper side
(ie, service provider interface) of this layer.
""")
_XcmCommsAccessMaxConnectPorts_Type = Cardinal32
_XcmCommsAccessMaxConnectPorts_Object = MibTableColumn
xcmCommsAccessMaxConnectPorts = _XcmCommsAccessMaxConnectPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 4),
    _XcmCommsAccessMaxConnectPorts_Type()
)
xcmCommsAccessMaxConnectPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessMaxConnectPorts.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAccessMaxConnectPorts.setDescription("""\
The maximum number of connection (or association) ports permitted at the upper
side (ie, service provider interface) of this layer.
""")
_XcmCommsAccessDatagramPorts_Type = Gauge32
_XcmCommsAccessDatagramPorts_Object = MibTableColumn
xcmCommsAccessDatagramPorts = _XcmCommsAccessDatagramPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 5),
    _XcmCommsAccessDatagramPorts_Type()
)
xcmCommsAccessDatagramPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessDatagramPorts.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAccessDatagramPorts.setDescription("""\
The current number of message (or datagram) ports open at the upper side (ie,
service provider interface) of this layer.
""")
_XcmCommsAccessHighDatagramPorts_Type = Gauge32
_XcmCommsAccessHighDatagramPorts_Object = MibTableColumn
xcmCommsAccessHighDatagramPorts = _XcmCommsAccessHighDatagramPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 6),
    _XcmCommsAccessHighDatagramPorts_Type()
)
xcmCommsAccessHighDatagramPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessHighDatagramPorts.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAccessHighDatagramPorts.setDescription("""\
The highest number of message (or datagram) ports open at the upper side (ie,
service provider interface) of this layer.
""")
_XcmCommsAccessMaxDatagramPorts_Type = Cardinal32
_XcmCommsAccessMaxDatagramPorts_Object = MibTableColumn
xcmCommsAccessMaxDatagramPorts = _XcmCommsAccessMaxDatagramPorts_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 13, 2, 1, 7),
    _XcmCommsAccessMaxDatagramPorts_Type()
)
xcmCommsAccessMaxDatagramPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsAccessMaxDatagramPorts.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAccessMaxDatagramPorts.setDescription("""\
The maximum number of message (or datagram) ports permitted at the upper side
(ie, service provider interface) of this layer.
""")
_XcmCommsMgmt_ObjectIdentity = ObjectIdentity
xcmCommsMgmt = _XcmCommsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14)
)
_XcmCommsMgmtTable_Object = MibTable
xcmCommsMgmtTable = _XcmCommsMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2)
)
if mibBuilder.loadTexts:
    xcmCommsMgmtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMgmtTable.setDescription("""\
A table containing additional management control objects for installed and
(possibly) active entities on this host system and supporting detailed and
extensible 'states' and 'conditions'.
""")
_XcmCommsMgmtEntry_Object = MibTableRow
xcmCommsMgmtEntry = _XcmCommsMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1)
)
xcmCommsMgmtEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtIndex"),
)
if mibBuilder.loadTexts:
    xcmCommsMgmtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMgmtEntry.setDescription("""\
An entry containing additional management control objects for installed and
(possibly) active entity on this host system and supporting detailed and
extensible 'states' and 'conditions'.
""")
_XcmCommsMgmtIndex_Type = Ordinal32
_XcmCommsMgmtIndex_Object = MibTableColumn
xcmCommsMgmtIndex = _XcmCommsMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 1),
    _XcmCommsMgmtIndex_Type()
)
xcmCommsMgmtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmCommsMgmtIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMgmtIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmCommsMgmtTable'.
""")
_XcmCommsMgmtRowStatus_Type = RowStatus
_XcmCommsMgmtRowStatus_Object = MibTableColumn
xcmCommsMgmtRowStatus = _XcmCommsMgmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 2),
    _XcmCommsMgmtRowStatus_Type()
)
xcmCommsMgmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsMgmtRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMgmtRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmCommsMgmtTable'.
""")


class _XcmCommsMgmtCommandRequest_Type(XcmCommsMgmtCommandRequest):
    """Custom type xcmCommsMgmtCommandRequest based on XcmCommsMgmtCommandRequest"""


_XcmCommsMgmtCommandRequest_Object = MibTableColumn
xcmCommsMgmtCommandRequest = _XcmCommsMgmtCommandRequest_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 3),
    _XcmCommsMgmtCommandRequest_Type()
)
xcmCommsMgmtCommandRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandRequest.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandRequest.setReference("""\
See: 'xcmCommsMgmtCommand[Data|Status|InProgress]'
""")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandRequest.setDescription("""\
The most recent comms management command request specified for this conceptual
row in the 'xcmCommsMgmtTable'. Usage: Conforming management agents SHALL
'reject' any SNMP Set-Request to 'xcmCommsMgmtCommand[Request|Data]' while
another management operation is already in progress (ie, while
'xcmCommsMgmtCommandInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3). Usage: Conforming management stations SHALL
set 'xcmCommsMgmtCommandRequest' (mgmt operation) and 'xcmCommsMgmtCommandData'
(mgmt arguments) SIMULTANEOUSLY (in the same SNMP Set-Request PDU).
""")


class _XcmCommsMgmtCommandData_Type(XcmCommsMgmtCommandData):
    """Custom type xcmCommsMgmtCommandData based on XcmCommsMgmtCommandData"""
    defaultHexValue = ""

    subtypeSpec = XcmCommsMgmtCommandData.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmCommsMgmtCommandData_Type.__name__ = "XcmCommsMgmtCommandData"
_XcmCommsMgmtCommandData_Object = MibTableColumn
xcmCommsMgmtCommandData = _XcmCommsMgmtCommandData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 4),
    _XcmCommsMgmtCommandData_Type()
)
xcmCommsMgmtCommandData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandData.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandData.setReference("""\
See: 'xcmCommsMgmtCommand[Request|Status|InProgress]'
""")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandData.setDescription("""\
The most recent comms management command data (if any) specified for this
conceptual row in the 'xcmCommsMgmtTable'. Usage: Conforming management agents
SHALL 'reject' any SNMP Set-Request to 'xcmCommsMgmtCommand[Request|Data]'
while another management operation is already in progress (ie, while
'xcmCommsMgmtCommandInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3). Usage: Conforming management stations SHALL
set 'xcmCommsMgmtCommandRequest' (mgmt operation) and 'xcmCommsMgmtCommandData'
(mgmt arguments) SIMULTANEOUSLY (in the same SNMP Set-Request PDU). Usage:
Conformant implementations MUST encrypt passwords, keys, and other security
information stored in this string object.
""")
_XcmCommsMgmtCommandStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmCommsMgmtCommandStatus_Object = MibTableColumn
xcmCommsMgmtCommandStatus = _XcmCommsMgmtCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 5),
    _XcmCommsMgmtCommandStatus_Type()
)
xcmCommsMgmtCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandStatus.setReference("""\
See: 'xcmCommsMgmtCommand[Request|Data|InProgress]'
""")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandStatus.setDescription("""\
The simple comms management error status associated with this conceptual row in
'xcmCommsMgmtTable'. Usage: Conforming management agents SHALL set this object
to the value returned in an SNMP Set-Response PDU when a simple comms
management operation is 'accepted', ie, when 'xcmCommsMgmtCommandInProgress'
goes from 'false' to 'true'. Usage: Conforming management agents SHALL set this
object to the value of the completion status of the (possibly deferred) simple
comms management operation, when 'xcmCommsMgmtCommandInProgress' goes from
'true' to 'false'.
""")


class _XcmCommsMgmtCommandInProgress_Type(TruthValue):
    """Custom type xcmCommsMgmtCommandInProgress based on TruthValue"""


_XcmCommsMgmtCommandInProgress_Object = MibTableColumn
xcmCommsMgmtCommandInProgress = _XcmCommsMgmtCommandInProgress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 14, 2, 1, 6),
    _XcmCommsMgmtCommandInProgress_Type()
)
xcmCommsMgmtCommandInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandInProgress.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandInProgress.setReference("""\
See: 'xcmCommsMgmtCommand[Request|Data|Status]'
""")
if mibBuilder.loadTexts:
    xcmCommsMgmtCommandInProgress.setDescription("""\
The comms management in progress status associated with this conceptual row in
'xcmCommsMgmtTable'. Usage: Conforming management agents SHALL 'reject' any
SNMP Set-Request to 'xcmCommsMgmtCommand[Request|Data]' while another
management operation is already in progress (ie, while
'xcmCommsMgmtCommandInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3).
""")

# Managed Objects groups

xcmCommsEngineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 3)
)
xcmCommsEngineGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineName"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineStackLast"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineMuxLast"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineAddressLast"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineMgmtLast"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineGroupSupport"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineCreateSupport"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmCommsEngineGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineGroup.setDescription("""\
Comms Engine Group (Comms Engines).
""")

xcmCommsEngineExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 4)
)
xcmCommsEngineExtGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtState"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtConditions"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtVersionID"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtVersionDate"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtMgmtIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsEngineExtOwnerOID"))
)
if mibBuilder.loadTexts:
    xcmCommsEngineExtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsEngineExtGroup.setDescription("""\
Comms Engine Ext Group (Comms Engines).
""")

xcmCommsStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 5)
)
xcmCommsStackGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackTypeOID"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackName"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackPosition"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackLowerStackIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackUpperStackIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackAddressIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackOptionIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackLowerMuxIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackUpperMuxIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsStackGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackGroup.setDescription("""\
Comms Stack Group (Stack Layers).
""")

xcmCommsStackExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 6)
)
xcmCommsStackExtGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtState"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtConditions"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtPurpose"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtRole"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtSuite"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtSuiteVersion"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtLayer"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtProtocol"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtMgmtIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackExtOwnerOID"))
)
if mibBuilder.loadTexts:
    xcmCommsStackExtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackExtGroup.setDescription("""\
Comms Stack Ext Group (Stack Layers).
""")

xcmCommsStackXrefGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 7)
)
xcmCommsStackXrefGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefLayerMgmtIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefLayerSecIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefLayerIWUIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefHrSWRunIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefHrSWInsIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefIfIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsStackXrefHrCommDevIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsStackXrefGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsStackXrefGroup.setDescription("""\
Comms Stack Xref Group (Stack Layers).
""")

xcmCommsMuxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 8)
)
xcmCommsMuxGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxNextIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxPreviousIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxOptionIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxBaseStackIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxAdjacentStackIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsMuxGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxGroup.setDescription("""\
Comms Mux Group (Multiplexors).
""")

xcmCommsMuxExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 9)
)
xcmCommsMuxExtGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtState"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtConditions"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtMgmtIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtAddressIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMuxExtOwnerOID"))
)
if mibBuilder.loadTexts:
    xcmCommsMuxExtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMuxExtGroup.setDescription("""\
Comms Mux Ext Group (Multiplexors).
""")

xcmCommsAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 10)
)
xcmCommsAddressGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressTypeOID"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressUserRole"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressName"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressCanonical"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressNextIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressPreviousIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressOptionIndex"))
)
if mibBuilder.loadTexts:
    xcmCommsAddressGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressGroup.setDescription("""\
Comms Address Group (Directories).
""")

xcmCommsAddressExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 11)
)
xcmCommsAddressExtGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtState"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtConditions"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtForm"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtScope"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtFanout"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtMgmtIndex"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAddressExtOwnerOID"))
)
if mibBuilder.loadTexts:
    xcmCommsAddressExtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAddressExtGroup.setDescription("""\
Comms Address Ext Group (Directories).
""")

xcmCommsTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 12)
)
xcmCommsTrafficGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficInputUnit"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficOutputUnit"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficInputCount"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficOutputCount"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficInputErrors"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsTrafficOutputErrors"))
)
if mibBuilder.loadTexts:
    xcmCommsTrafficGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsTrafficGroup.setDescription("""\
Comms Traffic Group (Stack Layer Traffic Counters).
""")

xcmCommsAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 13)
)
xcmCommsAccessGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessConnectPorts"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessHighConnectPorts"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessMaxConnectPorts"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessDatagramPorts"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessHighDatagramPorts"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsAccessMaxDatagramPorts"))
)
if mibBuilder.loadTexts:
    xcmCommsAccessGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsAccessGroup.setDescription("""\
Comms Access Group (Stack Layer Access Counters).
""")

xcmCommsMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 2, 14)
)
xcmCommsMgmtGroup.setObjects(
      *(("XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtRowStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtCommandRequest"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtCommandData"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtCommandStatus"),
        ("XEROX-COMMS-ENGINE-MIB", "xcmCommsMgmtCommandInProgress"))
)
if mibBuilder.loadTexts:
    xcmCommsMgmtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmCommsMgmtGroup.setDescription("""\
Comms Mgmt Group (State Management).
""")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xcmCommsEngineMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 3)
)
if mibBuilder.loadTexts:
    xcmCommsEngineMIBCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmCommsEngineMIBCompliance.setDescription("""\
The compliance statements for SNMP management agents that implement the Comms
Engine MIB.
""")

xcmCommsEngineMIBHelpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 61, 2, 4)
)
if mibBuilder.loadTexts:
    xcmCommsEngineMIBHelpCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmCommsEngineMIBHelpCompliance.setDescription("""\
The compliance statements for SNMP management agents that implement a subset of
the Comms Engine MIB, for the sole purpose of supporting extended 'contact'
information per device, via the Device Help group of the XCMI Ext to Host
Resources MIB. Usage: See 'Usage' paragraphs in the DESCRIPTION sub-clauses of
the following OBJECT clauses for additional usage details.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-COMMS-ENGINE-MIB",
    **{"xcmCommsEngineZeroDummy": xcmCommsEngineZeroDummy,
       "xcmCommsEngineMIB": xcmCommsEngineMIB,
       "xcmCommsEngineMIBConformance": xcmCommsEngineMIBConformance,
       "xcmCommsEngineMIBGroups": xcmCommsEngineMIBGroups,
       "xcmCommsEngineGroup": xcmCommsEngineGroup,
       "xcmCommsEngineExtGroup": xcmCommsEngineExtGroup,
       "xcmCommsStackGroup": xcmCommsStackGroup,
       "xcmCommsStackExtGroup": xcmCommsStackExtGroup,
       "xcmCommsStackXrefGroup": xcmCommsStackXrefGroup,
       "xcmCommsMuxGroup": xcmCommsMuxGroup,
       "xcmCommsMuxExtGroup": xcmCommsMuxExtGroup,
       "xcmCommsAddressGroup": xcmCommsAddressGroup,
       "xcmCommsAddressExtGroup": xcmCommsAddressExtGroup,
       "xcmCommsTrafficGroup": xcmCommsTrafficGroup,
       "xcmCommsAccessGroup": xcmCommsAccessGroup,
       "xcmCommsMgmtGroup": xcmCommsMgmtGroup,
       "xcmCommsEngineMIBCompliance": xcmCommsEngineMIBCompliance,
       "xcmCommsEngineMIBHelpCompliance": xcmCommsEngineMIBHelpCompliance,
       "xcmCommsEngine": xcmCommsEngine,
       "xcmCommsEngineTable": xcmCommsEngineTable,
       "xcmCommsEngineEntry": xcmCommsEngineEntry,
       "xcmCommsEngineRowStatus": xcmCommsEngineRowStatus,
       "xcmCommsEngineName": xcmCommsEngineName,
       "xcmCommsEngineStackLast": xcmCommsEngineStackLast,
       "xcmCommsEngineMuxLast": xcmCommsEngineMuxLast,
       "xcmCommsEngineAddressLast": xcmCommsEngineAddressLast,
       "xcmCommsEngineMgmtLast": xcmCommsEngineMgmtLast,
       "xcmCommsEngineGroupSupport": xcmCommsEngineGroupSupport,
       "xcmCommsEngineCreateSupport": xcmCommsEngineCreateSupport,
       "xcmCommsEngineUpdateSupport": xcmCommsEngineUpdateSupport,
       "xcmCommsEngineExt": xcmCommsEngineExt,
       "xcmCommsEngineExtTable": xcmCommsEngineExtTable,
       "xcmCommsEngineExtEntry": xcmCommsEngineExtEntry,
       "xcmCommsEngineExtRowStatus": xcmCommsEngineExtRowStatus,
       "xcmCommsEngineExtState": xcmCommsEngineExtState,
       "xcmCommsEngineExtConditions": xcmCommsEngineExtConditions,
       "xcmCommsEngineExtVersionID": xcmCommsEngineExtVersionID,
       "xcmCommsEngineExtVersionDate": xcmCommsEngineExtVersionDate,
       "xcmCommsEngineExtMgmtIndex": xcmCommsEngineExtMgmtIndex,
       "xcmCommsEngineExtOwnerOID": xcmCommsEngineExtOwnerOID,
       "xcmCommsStack": xcmCommsStack,
       "xcmCommsStackTable": xcmCommsStackTable,
       "xcmCommsStackEntry": xcmCommsStackEntry,
       "xcmCommsStackIndex": xcmCommsStackIndex,
       "xcmCommsStackRowStatus": xcmCommsStackRowStatus,
       "xcmCommsStackTypeOID": xcmCommsStackTypeOID,
       "xcmCommsStackName": xcmCommsStackName,
       "xcmCommsStackPosition": xcmCommsStackPosition,
       "xcmCommsStackLowerStackIndex": xcmCommsStackLowerStackIndex,
       "xcmCommsStackUpperStackIndex": xcmCommsStackUpperStackIndex,
       "xcmCommsStackAddressIndex": xcmCommsStackAddressIndex,
       "xcmCommsStackOptionIndex": xcmCommsStackOptionIndex,
       "xcmCommsStackLowerMuxIndex": xcmCommsStackLowerMuxIndex,
       "xcmCommsStackUpperMuxIndex": xcmCommsStackUpperMuxIndex,
       "xcmCommsStackExt": xcmCommsStackExt,
       "xcmCommsStackExtTable": xcmCommsStackExtTable,
       "xcmCommsStackExtEntry": xcmCommsStackExtEntry,
       "xcmCommsStackExtRowStatus": xcmCommsStackExtRowStatus,
       "xcmCommsStackExtState": xcmCommsStackExtState,
       "xcmCommsStackExtConditions": xcmCommsStackExtConditions,
       "xcmCommsStackExtPurpose": xcmCommsStackExtPurpose,
       "xcmCommsStackExtRole": xcmCommsStackExtRole,
       "xcmCommsStackExtSuite": xcmCommsStackExtSuite,
       "xcmCommsStackExtSuiteVersion": xcmCommsStackExtSuiteVersion,
       "xcmCommsStackExtLayer": xcmCommsStackExtLayer,
       "xcmCommsStackExtProtocol": xcmCommsStackExtProtocol,
       "xcmCommsStackExtMgmtIndex": xcmCommsStackExtMgmtIndex,
       "xcmCommsStackExtOwnerOID": xcmCommsStackExtOwnerOID,
       "xcmCommsStackXref": xcmCommsStackXref,
       "xcmCommsStackXrefTable": xcmCommsStackXrefTable,
       "xcmCommsStackXrefEntry": xcmCommsStackXrefEntry,
       "xcmCommsStackXrefRowStatus": xcmCommsStackXrefRowStatus,
       "xcmCommsStackXrefLayerMgmtIndex": xcmCommsStackXrefLayerMgmtIndex,
       "xcmCommsStackXrefLayerSecIndex": xcmCommsStackXrefLayerSecIndex,
       "xcmCommsStackXrefLayerIWUIndex": xcmCommsStackXrefLayerIWUIndex,
       "xcmCommsStackXrefHrSWRunIndex": xcmCommsStackXrefHrSWRunIndex,
       "xcmCommsStackXrefHrSWInsIndex": xcmCommsStackXrefHrSWInsIndex,
       "xcmCommsStackXrefIfIndex": xcmCommsStackXrefIfIndex,
       "xcmCommsStackXrefHrCommDevIndex": xcmCommsStackXrefHrCommDevIndex,
       "xcmCommsMux": xcmCommsMux,
       "xcmCommsMuxTable": xcmCommsMuxTable,
       "xcmCommsMuxEntry": xcmCommsMuxEntry,
       "xcmCommsMuxIndex": xcmCommsMuxIndex,
       "xcmCommsMuxRowStatus": xcmCommsMuxRowStatus,
       "xcmCommsMuxNextIndex": xcmCommsMuxNextIndex,
       "xcmCommsMuxPreviousIndex": xcmCommsMuxPreviousIndex,
       "xcmCommsMuxOptionIndex": xcmCommsMuxOptionIndex,
       "xcmCommsMuxBaseStackIndex": xcmCommsMuxBaseStackIndex,
       "xcmCommsMuxAdjacentStackIndex": xcmCommsMuxAdjacentStackIndex,
       "xcmCommsMuxExt": xcmCommsMuxExt,
       "xcmCommsMuxExtTable": xcmCommsMuxExtTable,
       "xcmCommsMuxExtEntry": xcmCommsMuxExtEntry,
       "xcmCommsMuxExtRowStatus": xcmCommsMuxExtRowStatus,
       "xcmCommsMuxExtState": xcmCommsMuxExtState,
       "xcmCommsMuxExtConditions": xcmCommsMuxExtConditions,
       "xcmCommsMuxExtMgmtIndex": xcmCommsMuxExtMgmtIndex,
       "xcmCommsMuxExtAddressIndex": xcmCommsMuxExtAddressIndex,
       "xcmCommsMuxExtOwnerOID": xcmCommsMuxExtOwnerOID,
       "xcmCommsAddress": xcmCommsAddress,
       "xcmCommsAddressTable": xcmCommsAddressTable,
       "xcmCommsAddressEntry": xcmCommsAddressEntry,
       "xcmCommsAddressIndex": xcmCommsAddressIndex,
       "xcmCommsAddressRowStatus": xcmCommsAddressRowStatus,
       "xcmCommsAddressTypeOID": xcmCommsAddressTypeOID,
       "xcmCommsAddressUserRole": xcmCommsAddressUserRole,
       "xcmCommsAddressName": xcmCommsAddressName,
       "xcmCommsAddressCanonical": xcmCommsAddressCanonical,
       "xcmCommsAddressNextIndex": xcmCommsAddressNextIndex,
       "xcmCommsAddressPreviousIndex": xcmCommsAddressPreviousIndex,
       "xcmCommsAddressOptionIndex": xcmCommsAddressOptionIndex,
       "xcmCommsAddressExt": xcmCommsAddressExt,
       "xcmCommsAddressExtTable": xcmCommsAddressExtTable,
       "xcmCommsAddressExtEntry": xcmCommsAddressExtEntry,
       "xcmCommsAddressExtRowStatus": xcmCommsAddressExtRowStatus,
       "xcmCommsAddressExtState": xcmCommsAddressExtState,
       "xcmCommsAddressExtConditions": xcmCommsAddressExtConditions,
       "xcmCommsAddressExtForm": xcmCommsAddressExtForm,
       "xcmCommsAddressExtScope": xcmCommsAddressExtScope,
       "xcmCommsAddressExtFanout": xcmCommsAddressExtFanout,
       "xcmCommsAddressExtMgmtIndex": xcmCommsAddressExtMgmtIndex,
       "xcmCommsAddressExtOwnerOID": xcmCommsAddressExtOwnerOID,
       "xcmCommsTraffic": xcmCommsTraffic,
       "xcmCommsTrafficTable": xcmCommsTrafficTable,
       "xcmCommsTrafficEntry": xcmCommsTrafficEntry,
       "xcmCommsTrafficRowStatus": xcmCommsTrafficRowStatus,
       "xcmCommsTrafficInputUnit": xcmCommsTrafficInputUnit,
       "xcmCommsTrafficOutputUnit": xcmCommsTrafficOutputUnit,
       "xcmCommsTrafficInputCount": xcmCommsTrafficInputCount,
       "xcmCommsTrafficOutputCount": xcmCommsTrafficOutputCount,
       "xcmCommsTrafficInputErrors": xcmCommsTrafficInputErrors,
       "xcmCommsTrafficOutputErrors": xcmCommsTrafficOutputErrors,
       "xcmCommsAccess": xcmCommsAccess,
       "xcmCommsAccessTable": xcmCommsAccessTable,
       "xcmCommsAccessEntry": xcmCommsAccessEntry,
       "xcmCommsAccessRowStatus": xcmCommsAccessRowStatus,
       "xcmCommsAccessConnectPorts": xcmCommsAccessConnectPorts,
       "xcmCommsAccessHighConnectPorts": xcmCommsAccessHighConnectPorts,
       "xcmCommsAccessMaxConnectPorts": xcmCommsAccessMaxConnectPorts,
       "xcmCommsAccessDatagramPorts": xcmCommsAccessDatagramPorts,
       "xcmCommsAccessHighDatagramPorts": xcmCommsAccessHighDatagramPorts,
       "xcmCommsAccessMaxDatagramPorts": xcmCommsAccessMaxDatagramPorts,
       "xcmCommsMgmt": xcmCommsMgmt,
       "xcmCommsMgmtTable": xcmCommsMgmtTable,
       "xcmCommsMgmtEntry": xcmCommsMgmtEntry,
       "xcmCommsMgmtIndex": xcmCommsMgmtIndex,
       "xcmCommsMgmtRowStatus": xcmCommsMgmtRowStatus,
       "xcmCommsMgmtCommandRequest": xcmCommsMgmtCommandRequest,
       "xcmCommsMgmtCommandData": xcmCommsMgmtCommandData,
       "xcmCommsMgmtCommandStatus": xcmCommsMgmtCommandStatus,
       "xcmCommsMgmtCommandInProgress": xcmCommsMgmtCommandInProgress}
)

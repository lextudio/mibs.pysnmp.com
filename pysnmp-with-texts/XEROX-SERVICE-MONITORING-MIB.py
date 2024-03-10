"""SNMP MIB module (XEROX-SERVICE-MONITORING-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-SERVICE-MONITORING-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:25 2024
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

(ObjectGroup,
 NotificationGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ObjectGroup",
    "NotificationGroup",
    "ModuleCompliance")

(Counter32,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 ModuleIdentity,
 IpAddress,
 iso,
 TimeTicks,
 MibIdentifier,
 NotificationType,
 Unsigned32,
 Integer32,
 Counter64,
 Gauge32,
 ObjectIdentity,
 Bits) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Counter32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "ModuleIdentity",
    "IpAddress",
    "iso",
    "TimeTicks",
    "MibIdentifier",
    "NotificationType",
    "Unsigned32",
    "Integer32",
    "Counter64",
    "Gauge32",
    "ObjectIdentity",
    "Bits")

(DisplayString,
 DateAndTime,
 TextualConvention,
 RowStatus,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "DateAndTime",
    "TextualConvention",
    "RowStatus",
    "TruthValue")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(XcmCommsStackExtProtocol,
 XcmCommsMgmtConditions,
 XcmCommsMgmtState) = mibBuilder.importSymbols(
    "XEROX-COMMS-ENGINE-TC",
    "XcmCommsStackExtProtocol",
    "XcmCommsMgmtConditions",
    "XcmCommsMgmtState")

(XcmFixedLocaleDisplayString,
 zeroDotZero,
 Ordinal32,
 XcmGenSNMPv2ErrorStatus,
 Cardinal32) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "XcmFixedLocaleDisplayString",
    "zeroDotZero",
    "Ordinal32",
    "XcmGenSNMPv2ErrorStatus",
    "Cardinal32")

(XcmHrDpaState,
 XcmHrDevDetailUnitClass,
 XcmHrDpaConditions,
 XcmHrDpaAvailability) = mibBuilder.importSymbols(
    "XEROX-HOST-RESOURCES-EXT-TC",
    "XcmHrDpaState",
    "XcmHrDevDetailUnitClass",
    "XcmHrDpaConditions",
    "XcmHrDpaAvailability")

(XcmSvcMonGroupSupport,
 XcmSvcMonServiceMgmtOperation,
 XcmSvcMonServiceMgmtData,
 XcmSvcMonServiceDetailType,
 XcmSvcMonServiceDetailClass,
 XcmSvcMonServiceType) = mibBuilder.importSymbols(
    "XEROX-SERVICE-MONITORING-TC",
    "XcmSvcMonGroupSupport",
    "XcmSvcMonServiceMgmtOperation",
    "XcmSvcMonServiceMgmtData",
    "XcmSvcMonServiceDetailType",
    "XcmSvcMonServiceDetailClass",
    "XcmSvcMonServiceType")


# MODULE-IDENTITY

xcmSvcMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74)
)
xcmSvcMonMIB.setLastUpdated("0603170000Z")
if mibBuilder.loadTexts:
    xcmSvcMonMIB.setOrganization("""\
Xerox Corporation - XCMI Working Group
""")
xcmSvcMonMIB.setContactInfo("""\
 XCMI Editors Email: coherence@crt.xerox.com
""")
if mibBuilder.loadTexts:
    xcmSvcMonMIB.setDescription("""\
Version: 5.502.pub The MIB module for basic configuration and active management
of application services for network accessible host systems. See: IETF Network
Services Monitoring MIB (IETF RFC 1565, January 1994). See: IETF Host Resources
MIB (IETF RFC 2790, March 2000). See: OSI Reference Model - Part 1: Basic
Reference Model (CCITT X.200:1992 | ISO 7498-1:1992). See: OSI Reference Model
- Part 4: Systems Management (CCITT X.700:1992 | ISO 7498-4:1992). Copyright
(C) 1996-2006 Xerox Corporation. All Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmSvcMonZeroDummy_ObjectIdentity = ObjectIdentity
xcmSvcMonZeroDummy = _XcmSvcMonZeroDummy_ObjectIdentity(
    (0, 0, 74)
)
_XcmSvcMonGeneral_ObjectIdentity = ObjectIdentity
xcmSvcMonGeneral = _XcmSvcMonGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1)
)
_XcmSvcMonGeneralTable_Object = MibTable
xcmSvcMonGeneralTable = _XcmSvcMonGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonGeneralTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralTable.setDescription("""\
A table of general counters and capabilities for ease of use of the XCMI
Service Monitoring MIB on this host system. Usage: The ONLY valid row in the
'xcmSvcMonGeneralTable' SHALL have an 'xcmSvcMonGeneralIndex' of one ('1').
""")
_XcmSvcMonGeneralEntry_Object = MibTableRow
xcmSvcMonGeneralEntry = _XcmSvcMonGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1)
)
xcmSvcMonGeneralEntry.setIndexNames(
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralIndex"),
)
if mibBuilder.loadTexts:
    xcmSvcMonGeneralEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralEntry.setDescription("""\
An entry of general counters and capabilities for ease of use of the XCMI
Service Monitoring MIB on this host system. Usage: The ONLY valid row in the
'xcmSvcMonGeneralTable' SHALL have an 'xcmSvcMonGeneralIndex' of one ('1').
""")
_XcmSvcMonGeneralIndex_Type = Ordinal32
_XcmSvcMonGeneralIndex_Object = MibTableColumn
xcmSvcMonGeneralIndex = _XcmSvcMonGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 1),
    _XcmSvcMonGeneralIndex_Type()
)
xcmSvcMonGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmSvcMonGeneralTable'. Usage: The ONLY valid row in the
'xcmSvcMonGeneralTable' SHALL have an 'xcmSvcMonGeneralIndex' of one ('1').
Usage: 'xcmSvcMonGeneralRowStatus' is 'read-only' because the ONLY valid
conceptual row SHALL NOT be deleted.
""")
_XcmSvcMonGeneralRowStatus_Type = RowStatus
_XcmSvcMonGeneralRowStatus_Object = MibTableColumn
xcmSvcMonGeneralRowStatus = _XcmSvcMonGeneralRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 2),
    _XcmSvcMonGeneralRowStatus_Type()
)
xcmSvcMonGeneralRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralRowStatus.setDescription("""\
This object is used to display status of the ONLY valid conceptual row in the
'xcmSvcMonGeneralTable'. Usage: 'xcmSvcMonGeneralRowStatus' is 'read-only'
because the ONLY valid conceptual row SHALL NOT be deleted.
""")


class _XcmSvcMonGeneralVersionID_Type(ProductID):
    """Custom type xcmSvcMonGeneralVersionID based on ProductID"""
    defaultValue = "(0, 0)"


_XcmSvcMonGeneralVersionID_Object = MibTableColumn
xcmSvcMonGeneralVersionID = _XcmSvcMonGeneralVersionID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 3),
    _XcmSvcMonGeneralVersionID_Type()
)
xcmSvcMonGeneralVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralVersionID.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralVersionID.setReference("""\
See: 'hrSW[Installed|Run]ID' in the Software Installed and Software Running
groups of the IETF HR MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralVersionID.setDescription("""\
The software product ID of the SNMP sub-agent which implements the XCMI Service
Monitoring MIB on this host system. Usage: This object SHALL specify the
software product ID of an SNMP sub-agent (possibly also found in a conceptual
row in the 'hrSWRunTable' and/or 'hrSWInstalledTable' in the IETF HR MIB). This
object SHALL NOT specify a particular release of the XCMI Service Monitoring
MIB, or the whole host system product. Note: Contrast with 'sysObjectID' for
the whole SNMP agent in the IETF MIB-II (RFC 1213) and 'hrDeviceID' for the
whole device (or whole product, in the case of 'xcmHrDevice...') in the IETF
Host Resources MIB (RFC 2790).
""")


class _XcmSvcMonGeneralVersionDate_Type(DateAndTime):
    """Custom type xcmSvcMonGeneralVersionDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmSvcMonGeneralVersionDate_Object = MibTableColumn
xcmSvcMonGeneralVersionDate = _XcmSvcMonGeneralVersionDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 4),
    _XcmSvcMonGeneralVersionDate_Type()
)
xcmSvcMonGeneralVersionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralVersionDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralVersionDate.setReference("""\
See: 'hrSW[Installed|Run]ID' in the Software Installed and Software Running
groups of the IETF HR MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralVersionDate.setDescription("""\
The software build date of the SNMP sub-agent which implements the XCMI Service
Monitoring MIB on this host system. Usage: This object SHALL specify the BUILD
date of the SNMP sub-agent software (not available elsewhere in IETF/XCMI
MIBs). This object SHALL NOT specify the INSTALL date of the SNMP sub-agent
software on this host system, nor the RESET date. Note: Contrast with
'hrSWInstalledDate' in the Software Installed group of the IETF Host Resources
MIB (RFC 2790), and 'xcmHrDevInfoResetDate' in the Device Info group of the
XCMI Host Resources Extensions MIB.
""")


class _XcmSvcMonGeneralGroupSupport_Type(XcmSvcMonGroupSupport):
    """Custom type xcmSvcMonGeneralGroupSupport based on XcmSvcMonGroupSupport"""
    defaultValue = 1


_XcmSvcMonGeneralGroupSupport_Object = MibTableColumn
xcmSvcMonGeneralGroupSupport = _XcmSvcMonGeneralGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 5),
    _XcmSvcMonGeneralGroupSupport_Type()
)
xcmSvcMonGeneralGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralGroupSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Service Monitoring MIB groups supported by this management agent
implementation (ie, version) on this host system, specified in a bit-mask.
Usage: Conforming management agents SHALL accurately report their support for
XCMI Service Monitoring MIB groups.
""")
_XcmSvcMonGeneralCreateSupport_Type = XcmSvcMonGroupSupport
_XcmSvcMonGeneralCreateSupport_Object = MibTableColumn
xcmSvcMonGeneralCreateSupport = _XcmSvcMonGeneralCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 6),
    _XcmSvcMonGeneralCreateSupport_Type()
)
xcmSvcMonGeneralCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralCreateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralCreateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Service Monitoring MIB groups supported for dynamic row creation
(via '...RowStatus') by this management agent implementation (ie, version) on
this host system, specified in a bit-mask. Usage: Conforming management agents
SHALL accurately report their support for XCMI Service Monitoring MIB groups.
""")
_XcmSvcMonGeneralUpdateSupport_Type = XcmSvcMonGroupSupport
_XcmSvcMonGeneralUpdateSupport_Object = MibTableColumn
xcmSvcMonGeneralUpdateSupport = _XcmSvcMonGeneralUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 1, 2, 1, 7),
    _XcmSvcMonGeneralUpdateSupport_Type()
)
xcmSvcMonGeneralUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralUpdateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralUpdateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Service Monitoring MIB groups supported for existing row update
(via SNMP Set-Request PDUs) by this management agent implementation (ie,
version) on this host system, specified in a bit-mask. Usage: Conforming
management agents SHALL accurately report their support for XCMI Service
Monitoring MIB groups.
""")
_XcmSvcMonMIBConformance_ObjectIdentity = ObjectIdentity
xcmSvcMonMIBConformance = _XcmSvcMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2)
)
_XcmSvcMonMIBGroups_ObjectIdentity = ObjectIdentity
xcmSvcMonMIBGroups = _XcmSvcMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2)
)
_XcmSvcMonQueue_ObjectIdentity = ObjectIdentity
xcmSvcMonQueue = _XcmSvcMonQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3)
)
_XcmSvcMonQueueTable_Object = MibTable
xcmSvcMonQueueTable = _XcmSvcMonQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueTable.setReference("""\
See: 'xcmSvcMonQueueOnSystem', and 'xcmSvcMonQueueRoutingIndex'. See:
'xcmHrDevInfoRealization' in XCMI Ext to Host Res MIB. See:
'xcmJobGenBasicTable' in XCMI Job Monitoring MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueTable.setDescription("""\
A table of the external job queues supported and (possibly) active, for some
'physical', 'logical', or 'logicalAndPhysical' device on this host system.
Usage: These externally visible job queues MAY actually be configured on
external print/file servers (remote) or on the managed system itself (local).
Usage: For example, a 'logical printer' might support one or more external
(network) job queues. Note: The 'xcmJobGenBasicTable' in the XCMI Job
Monitoring MIB (indexed by 'hrDeviceIndex' from the IETF Host Resources MIB)
displays the unordered union of all jobs present in the (one or more) 'local'
queues supported by each 'physical', 'logical', or 'logicalAndPhysical' device
on this host system. Note: The XCMI Comms Engine MIB is indexed by devices of
type 'CPU', while the 'xcmSvcMonQueueTable' is indexed by application devices
of type 'printer', 'fax', etc. Usage: Throughout this specification, the term
'stable storage' refers to storage which is reliable over long durations
(years) and is NOT destroyed by host system reboot (eg, battery-backed DRAM is
'stable storage' - while simple DRAM is NOT 'stable storage'). Examples of
valid 'stable storage' include: NVRAM, hard disk, EEPROM, etc. Usage:
Conforming implementations SHALL preserve active queue table objects across
management agent power cycles, and SHALL implement one of the following two
methods: 1) The agent SHALL store queue table objects directly in 'stable
storage'; or 2) The agent SHALL automatically checkpoint all active queue table
objects to 'stable storage' with reasonable frequency (either due to a write to
some queue table object, or upon expiration of a product-specific timeout).
Usage: Conforming implementations MAY (optionally) support one of the following
two 'checkpoint protocols': 1) A client sends a 'Set' of
'xcmSvcMonQueueRowStatus' to 'active(1)', to request that a 'checkpoint' be
performed; 2a) An agent which supports 'rapid checkpoint', completes the
checkpoint to 'stable storage', and sends a 'SetResponse' with 'noError(0)';
<or> 2b) An agent which supports 'delayed checkpoint', changes
'xcmSvcMonQueueRowStatus' to 'notInService(2)', sends a 'SetResponse' with
'noError(0)', completes the checkpoint to 'stable storage', and changes
'xcmSvcMonQueueRowStatus' back to 'active(1)'.
""")
_XcmSvcMonQueueEntry_Object = MibTableRow
xcmSvcMonQueueEntry = _XcmSvcMonQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1)
)
xcmSvcMonQueueEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueIndex"),
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueEntry.setReference("""\
See: 'xcmSvcMonQueueOnSystem', and 'xcmSvcMonQueueRoutingIndex'. See:
'xcmHrDevInfoRealization' in XCMI Ext to Host Res MIB. See:
'xcmJobGenBasicTable' in XCMI Job Monitoring MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueEntry.setDescription("""\
An entry for an external job queue supported and (possibly) active, for some
'physical', 'logical', or 'logicalAndPhysical' device on this host system.
Usage: This externally visible job queue MAY actually be configured on an
external print/file server (remote) or on the managed system itself (local).
""")
_XcmSvcMonQueueIndex_Type = Ordinal32
_XcmSvcMonQueueIndex_Object = MibTableColumn
xcmSvcMonQueueIndex = _XcmSvcMonQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 1),
    _XcmSvcMonQueueIndex_Type()
)
xcmSvcMonQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmSvcMonQueueTable'. Usage: This object SHALL be permanent (ie, preserved
across all hardware resets).
""")
_XcmSvcMonQueueRowStatus_Type = RowStatus
_XcmSvcMonQueueRowStatus_Object = MibTableColumn
xcmSvcMonQueueRowStatus = _XcmSvcMonQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 2),
    _XcmSvcMonQueueRowStatus_Type()
)
xcmSvcMonQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowStatus.setReference("""\
See: 'xcmSvcMonGeneralCreateSupport' in 'xcmSvcMonGeneralTable'. See:
'RowStatus' in IETF SNMPv2 TC (RFC 1443/1903/2579). See:
'xcmHrDevMgmtCommandData' in XCMI HRX MIB and 'xcmSecUserMgmtData' in XCMI
Security MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmSvcMonQueueTable' and (optionally) in the 'xcmSvcMonQueueExtTable' (if
implementated on this system). Usage: Conforming implementations which support
static rows SHALL support 'active' and 'notInService' writes to this
'xcmSvcMonQueueRowStatus' row status object; and SHALL clear the
'svcMonQueueGroup' bit in 'xcmSvcMonGeneralCreateSupport' in the
'xcmSvcMonGeneralTable'. Usage: Conforming implementations which support
dynamic rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmSvcMonQueueRowStatus' row status object; and SHALL set the
'svcMonQueueGroup' bit in 'xcmSvcMonGeneralCreateSupport' in the
'xcmSvcMonGeneralTable'. Usage: Conforming implementations need NOT support
dynamic row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmSvcMonQueueDomain_Type(XcmCommsStackExtProtocol):
    """Custom type xcmSvcMonQueueDomain based on XcmCommsStackExtProtocol"""


_XcmSvcMonQueueDomain_Object = MibTableColumn
xcmSvcMonQueueDomain = _XcmSvcMonQueueDomain_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 3),
    _XcmSvcMonQueueDomain_Type()
)
xcmSvcMonQueueDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueueDomain.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueDomain.setReference("""\
See: 'xcmSvcMonQueue[Path|Name]'
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueDomain.setDescription("""\
The queue namespace domain (directory protocol) for the queue path and queue
name (eg, 'internetDNS', 'netwareNDS'). Usage: This queue namespace domain
SHALL be a valid directory protocol enumeration from 'XcmCommsStackExtProtocol'
in the XCMI Comms Engine TC. Usage: When a remote management station (client)
creates a row in 'xcmSvcMonQueueTable' (via 'xcmSvcMonQueueRowStatus'), this
queue namespace domain SHALL be specified. Note: For implementation efficiency,
this object uses the integer 'XcmCommStackExtProtocol' values (from the XCMI
Comms Engine MIB) rather than the equivalent 'XcmCO...' OID values (from the
XCMI Comms Config MIB).
""")


class _XcmSvcMonQueuePath_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmSvcMonQueuePath based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonQueuePath_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmSvcMonQueuePath_Object = MibTableColumn
xcmSvcMonQueuePath = _XcmSvcMonQueuePath_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 4),
    _XcmSvcMonQueuePath_Type()
)
xcmSvcMonQueuePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueuePath.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueuePath.setReference("""\
See: 'xcmSvcMonQueue[Domain|Name]'
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueuePath.setDescription("""\
Human-readable queue path, used by system administrators and end-users to
specify the 'full network path' of a file server (eg, Novell Bindery) or
directory tree (eg, Novell NDS) which, when prefixed to the following
'xcmSvcMonQueueName' object, specifies a 'full network queue name' of this
queue. Usage: This queue path SHOULD be the one normally used in a command
shell for control of this queue. Usage: When a remote management station
(client) creates a row in 'xcmSvcMonQueueTable' (via
'xcmSvcMonQueueRowStatus'), this queue path SHALL be specified.
""")


class _XcmSvcMonQueueName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmSvcMonQueueName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonQueueName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmSvcMonQueueName_Object = MibTableColumn
xcmSvcMonQueueName = _XcmSvcMonQueueName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 5),
    _XcmSvcMonQueueName_Type()
)
xcmSvcMonQueueName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueueName.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueName.setReference("""\
See: 'xcmSvcMonQueue[Domain|Path]' See: 'xcmJobGenBasicTable' in XCMI Job
Monitoring MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueName.setDescription("""\
Human-readable queue name, used by system administrators and end-users to
specify the 'simple name' of this queue (or in the Novell NDS case, the context
and simple name concatenated), which, when suffixed to the preceding
'xcmSvcMonQueuePath' object, specifies a 'full network queue name' of this
queue. Usage: This queue name SHOULD be the one normally used in a command
shell for control of this queue. Usage: When a remote management station
(client) creates a row in 'xcmSvcMonQueueTable' (via
'xcmSvcMonQueueRowStatus'), this queue name SHALL be specified.
""")


class _XcmSvcMonQueueOnSystem_Type(TruthValue):
    """Custom type xcmSvcMonQueueOnSystem based on TruthValue"""


_XcmSvcMonQueueOnSystem_Object = MibTableColumn
xcmSvcMonQueueOnSystem = _XcmSvcMonQueueOnSystem_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 3, 2, 1, 6),
    _XcmSvcMonQueueOnSystem_Type()
)
xcmSvcMonQueueOnSystem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueueOnSystem.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueOnSystem.setReference("""\
See: 'xcmSvcMonQueueRoutingIndex'.
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueOnSystem.setDescription("""\
Specifies whether this queue is present on this host system (local) or is on
another network system (remote).
""")
_XcmSvcMonQueueExt_ObjectIdentity = ObjectIdentity
xcmSvcMonQueueExt = _XcmSvcMonQueueExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4)
)
_XcmSvcMonQueueExtV1EventOID_ObjectIdentity = ObjectIdentity
xcmSvcMonQueueExtV1EventOID = _XcmSvcMonQueueExtV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 1)
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtV1EventOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtV1EventOID.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever
'xcmSvcMonQueue[State|Conditions|FaultCount]' changes. See SNMPv2 trap
definition 'xcmSvcMonQueueExtV2Event' below for 'special semantics'.
""")
_XcmSvcMonQueueExtV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmSvcMonQueueExtV2EventPrefix = _XcmSvcMonQueueExtV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 1, 0)
)
_XcmSvcMonQueueExtTable_Object = MibTable
xcmSvcMonQueueExtTable = _XcmSvcMonQueueExtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtTable.setReference("""\
See: 'xcmSvcMonQueueTable' in this MIB module.
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtTable.setDescription("""\
A table which augments 'xcmSvcMonQueueTable', with dynamic queue routing
(forwarding), state, conditions, fault info, create date, lifetime jobs, and
last connect date and jobs. Usage: Conforming implementations SHALL preserve
active queue table objects across management agent power cycles, and SHALL
implement one of the following two methods: 1) The agent SHALL store queue
table objects directly in 'stable storage'; or 2) The agent SHALL automatically
checkpoint all active queue table objects to 'stable storage' with reasonable
frequency (either due to a write to some queue table object, or upon expiration
of a product-specific timeout).
""")
_XcmSvcMonQueueExtEntry_Object = MibTableRow
xcmSvcMonQueueExtEntry = _XcmSvcMonQueueExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1)
)
xcmSvcMonQueueEntry.registerAugmentions(
    ("XEROX-SERVICE-MONITORING-MIB",
     "xcmSvcMonQueueExtEntry")
)
xcmSvcMonQueueExtEntry.setIndexNames(*xcmSvcMonQueueEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtEntry.setReference("""\
See: 'xcmSvcMonQueueTable' in this MIB module.
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtEntry.setDescription("""\
An entry which augments 'xcmSvcMonQueueTable', with dynamic queue routing
(forwarding), state, conditions, and fault info.
""")
_XcmSvcMonQueueRoutingIndex_Type = Cardinal32
_XcmSvcMonQueueRoutingIndex_Object = MibTableColumn
xcmSvcMonQueueRoutingIndex = _XcmSvcMonQueueRoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 1),
    _XcmSvcMonQueueRoutingIndex_Type()
)
xcmSvcMonQueueRoutingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRoutingIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRoutingIndex.setReference("""\
See: 'xcmSvcMonQueueOnSystem'.
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRoutingIndex.setDescription("""\
The (optional) routing index of this queue. Usage: This (optional) routing
index, for queue indirection mapping, specifies 'xcmSvcMonQueueIndex' for the
NEXT queue closer to (or on) this host system, or zero if none. Usage: It is
common for more than one off-system (remote) queue to be forwarded to the same
on-system (local) queue. Multiple off-system (remote) entries in the
'xcmSvcMonQueueTable' (for a given device) MAY forward to the same on-system
(local) entry.
""")


class _XcmSvcMonQueueState_Type(XcmCommsMgmtState):
    """Custom type xcmSvcMonQueueState based on XcmCommsMgmtState"""


_XcmSvcMonQueueState_Object = MibTableColumn
xcmSvcMonQueueState = _XcmSvcMonQueueState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 2),
    _XcmSvcMonQueueState_Type()
)
xcmSvcMonQueueState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueState.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueState.setReference("""\
See: 'XcmCommsMgmt[State|Conditions]' in XCMI Comms Engine. See:
'xcmSvcMonQueueConditions'
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueState.setDescription("""\
The current state of this queue. Usage: This queue state specifies the
operational state of the application service or the network communications path
to this queue. Usage: This queue state need NOT be reported for a 'remote'
queue (ie, 'xcmSvcMonQueueOnSystem' is 'false'), although in some cases (eg,
Novell PServer), the state of (connectivity to) the 'remote' queue is known
(and SHALL be reported) on the managed system. Usage: This queue state SHALL be
as reported in the XCMI Comms Config/Engine MIB objects for this queue.
""")
_XcmSvcMonQueueConditions_Type = XcmCommsMgmtConditions
_XcmSvcMonQueueConditions_Object = MibTableColumn
xcmSvcMonQueueConditions = _XcmSvcMonQueueConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 3),
    _XcmSvcMonQueueConditions_Type()
)
xcmSvcMonQueueConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueConditions.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueConditions.setReference("""\
See: 'XcmCommsMgmt[State|Conditions]' in XCMI Comms Engine. See:
'xcmSvcMonQueueState'
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueConditions.setDescription("""\
The current conditions (ie, state reasons) of this queue. Usage: These queue
conditions qualify the operational state of the application service or the
network communications path to this queue. Usage: These queue conditions need
NOT be reported for a 'remote' queue (ie, 'xcmSvcMonQueueOnSystem' is 'false'),
although in some cases (eg, Novell PServer), the state of (connectivity to) the
'remote' queue is known (and SHALL be reported) on the managed system. Usage:
These queue conditions SHALL be as reported in the XCMI Comms Config/Engine MIB
objects for this queue.
""")
_XcmSvcMonQueueFaultCount_Type = Counter32
_XcmSvcMonQueueFaultCount_Object = MibTableColumn
xcmSvcMonQueueFaultCount = _XcmSvcMonQueueFaultCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 4),
    _XcmSvcMonQueueFaultCount_Type()
)
xcmSvcMonQueueFaultCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultCount.setReference("""\
See: 'xcmSvcMonQueue[State|Conditions]'
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultCount.setDescription("""\
The current fault count of this queue. Usage: This queue fault count qualifies
the operational state of the application service or the network communications
path to this queue. Usage: This queue fault count need NOT be reported for a
'remote' queue (ie, 'xcmSvcMonQueueOnSystem' is 'false'), although in some
cases (eg, Novell PServer), the state of (connectivity to) the 'remote' queue
is known (and SHALL be reported) on the managed system. Usage: This queue fault
count SHALL be as reported in any relevant device- or service-specific MIB for
this queue. Usage: Although no default value ('DEFVAL' clause) is permitted (by
IETF SMIv2) for this counter, conforming host systems SHALL zero this counter
upon conceptual row creation.
""")
_XcmSvcMonQueueFaultCode_Type = Integer32
_XcmSvcMonQueueFaultCode_Object = MibTableColumn
xcmSvcMonQueueFaultCode = _XcmSvcMonQueueFaultCode_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 5),
    _XcmSvcMonQueueFaultCode_Type()
)
xcmSvcMonQueueFaultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultCode.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultCode.setReference("""\
See: 'xcmSvcMonQueue[State|Conditions]'
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultCode.setDescription("""\
Encoded current fault code of this queue. Usage: This queue fault code
qualifies the operational state of the application service or the network
communications path to this queue. Usage: This queue fault code need NOT be
reported for a 'remote' queue (ie, 'xcmSvcMonQueueOnSystem' is 'false'),
although in some cases (eg, Novell PServer), the state of (connectivity to) the
'remote' queue is known (and SHALL be reported) on the managed system. Usage:
This queue fault code SHALL be as reported in any relevant device- or service-
specific MIB for this queue.
""")


class _XcmSvcMonQueueFaultString_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmSvcMonQueueFaultString based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonQueueFaultString_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmSvcMonQueueFaultString_Object = MibTableColumn
xcmSvcMonQueueFaultString = _XcmSvcMonQueueFaultString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 6),
    _XcmSvcMonQueueFaultString_Type()
)
xcmSvcMonQueueFaultString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultString.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultString.setReference("""\
See: 'xcmSvcMonQueue[State|Conditions]'
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueFaultString.setDescription("""\
Human-readable current fault string of this queue. Usage: This queue fault
string qualifies the operational state of the application service or the
network communications path to this queue. Usage: This queue fault string need
NOT be reported for a 'remote' queue (ie, 'xcmSvcMonQueueOnSystem' is 'false'),
although in some cases (eg, Novell PServer), the state of (connectivity to) the
'remote' queue is known (and SHALL be reported) on the managed system. Usage:
This queue fault string SHALL be as reported in any relevant device- or
service-specific MIB for this queue.
""")


class _XcmSvcMonQueueRowCreateDate_Type(DateAndTime):
    """Custom type xcmSvcMonQueueRowCreateDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmSvcMonQueueRowCreateDate_Object = MibTableColumn
xcmSvcMonQueueRowCreateDate = _XcmSvcMonQueueRowCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 7),
    _XcmSvcMonQueueRowCreateDate_Type()
)
xcmSvcMonQueueRowCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowCreateDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowCreateDate.setReference("""\
See: 'xcmSvcMonQueueOnSystem'. See: 'xcmSvcMonQueueRowTotalJobs'
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowCreateDate.setDescription("""\
The date and time of creation of this conceptual row in the
'xcmSvcMonQueueTable' (and 'xcmSvcMonQueueExtTable').
""")
_XcmSvcMonQueueRowTotalJobs_Type = Counter32
_XcmSvcMonQueueRowTotalJobs_Object = MibTableColumn
xcmSvcMonQueueRowTotalJobs = _XcmSvcMonQueueRowTotalJobs_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 8),
    _XcmSvcMonQueueRowTotalJobs_Type()
)
xcmSvcMonQueueRowTotalJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowTotalJobs.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowTotalJobs.setReference("""\
See: 'xcmSvcMonQueueOnSystem'. See: 'xcmSvcMonQueueRowTotalJobs'
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueRowTotalJobs.setDescription("""\
The total jobs completed for this remote/local external job queue, since
'xcmSvcMonQueueRowCreateDate'. Usage: Although no default value ('DEFVAL'
clause) is permitted (by IETF SMIv2) for this counter, conforming host systems
SHALL zero this counter upon conceptual row creation.
""")


class _XcmSvcMonQueueLastConnectDate_Type(DateAndTime):
    """Custom type xcmSvcMonQueueLastConnectDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_XcmSvcMonQueueLastConnectDate_Object = MibTableColumn
xcmSvcMonQueueLastConnectDate = _XcmSvcMonQueueLastConnectDate_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 9),
    _XcmSvcMonQueueLastConnectDate_Type()
)
xcmSvcMonQueueLastConnectDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueLastConnectDate.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueLastConnectDate.setReference("""\
See: 'xcmSvcMonQueueOnSystem'. See: 'xcmSvcMonQueueLastConnectJobs'
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueLastConnectDate.setDescription("""\
The date and time of last connect (and/or login) to this remote or local
external job queue.
""")
_XcmSvcMonQueueLastConnectJobs_Type = Counter32
_XcmSvcMonQueueLastConnectJobs_Object = MibTableColumn
xcmSvcMonQueueLastConnectJobs = _XcmSvcMonQueueLastConnectJobs_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 2, 1, 10),
    _XcmSvcMonQueueLastConnectJobs_Type()
)
xcmSvcMonQueueLastConnectJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonQueueLastConnectJobs.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueLastConnectJobs.setReference("""\
See: 'xcmSvcMonQueueOnSystem'. See: 'xcmSvcMonQueueRowTotalJobs'
""")
if mibBuilder.loadTexts:
    xcmSvcMonQueueLastConnectJobs.setDescription("""\
The total jobs completed for this remote/local external job queue, since
'xcmSvcMonQueueLastConnectDate'. Usage: Although no default value ('DEFVAL'
clause) is permitted (by IETF SMIv2) for this counter, conforming host systems
SHALL zero this counter upon conceptual row creation.
""")
_XcmSvcMonService_ObjectIdentity = ObjectIdentity
xcmSvcMonService = _XcmSvcMonService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5)
)
_XcmSvcMonServiceV1EventOID_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceV1EventOID = _XcmSvcMonServiceV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 1)
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceV1EventOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceV1EventOID.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever a
service status changes. See SNMPv2 trap definition 'xcmSvcMonServiceV2Event'
below for 'special semantics'.
""")
_XcmSvcMonServiceV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceV2EventPrefix = _XcmSvcMonServiceV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 1, 0)
)
_XcmSvcMonServiceTable_Object = MibTable
xcmSvcMonServiceTable = _XcmSvcMonServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceTable.setReference("""\
See: 'xcmSecServiceTable' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceTable.setDescription("""\
A table of the system and/or end-user services supported and (possibly) ready
on this host system, and (possibly) associated with one or more 'physical',
'logical', or 'logicalAndPhysical' devices on this host system presenting job
services and one or more external devices (for security, accounting, etc),
attached to this host system.
""")
_XcmSvcMonServiceEntry_Object = MibTableRow
xcmSvcMonServiceEntry = _XcmSvcMonServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1)
)
xcmSvcMonServiceEntry.setIndexNames(
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceIndex"),
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceEntry.setReference("""\
See: 'xcmSecServiceEntry' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceEntry.setDescription("""\
An entry for a system and/or end-user service supported and (possibly) ready on
this host system, and (possibly) associated with one or more 'physical',
'logical', or 'logicalAndPhysical' devices on this host system presenting job
services and one or more external devices (for security, accounting, etc),
attached to this host system.
""")
_XcmSvcMonServiceIndex_Type = Ordinal32
_XcmSvcMonServiceIndex_Object = MibTableColumn
xcmSvcMonServiceIndex = _XcmSvcMonServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 1),
    _XcmSvcMonServiceIndex_Type()
)
xcmSvcMonServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmSvcMonServiceTable'. Usage: Conforming management stations and management
agents SHALL ensure that 'xcmSvcMonServiceIndex' is equal to
'xcmSecServiceIndex' for the same service (if the XCMI Security MIB is also
implemented). Usage: This object SHALL be permanent (ie, preserved across all
hardware resets).
""")
_XcmSvcMonServiceRowStatus_Type = RowStatus
_XcmSvcMonServiceRowStatus_Object = MibTableColumn
xcmSvcMonServiceRowStatus = _XcmSvcMonServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 2),
    _XcmSvcMonServiceRowStatus_Type()
)
xcmSvcMonServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceRowStatus.setReference("""\
See: 'xcmSvcMonGeneralCreateSupport' in 'xcmSvcMonGeneralTable'. See:
'RowStatus' in IETF SNMPv2 TC (RFC 1443/1903/2579). See:
'xcmHrDevMgmtCommandData' in XCMI HRX MIB and 'xcmSecUserMgmtData' in XCMI
Security MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmSvcMonServiceTable' and (optionally) in the 'xcmSvcMonServiceMgmtTable' (if
implemented on this system). Usage: Conforming management stations and
management agents SHALL ensure that 'xcmSvcMonServiceIndex' is equal to
'xcmSecServiceIndex' for the same service (if the XCMI Security MIB is also
implemented). Usage: Conforming implementations which support static rows SHALL
support 'active' and 'notInService' writes to this 'xcmSvcMonServiceRowStatus'
row status object; and SHALL clear the 'svcMonServiceGroup' bit in
'xcmSvcMonGeneralCreateSupport' in the 'xcmSvcMonGeneralTable'. Usage:
Conforming implementations which support dynamic rows SHALL support
'createAndGo' and 'destroy' writes to this 'xcmSvcMonServiceRowStatus' row
status object; and SHALL set the 'svcMonServiceGroup' bit in
'xcmSvcMonGeneralCreateSupport' in the 'xcmSvcMonGeneralTable'. Usage:
Conforming implementations need NOT support dynamic row creation (via
'createAndGo(4)') nor dynamic row deletion (via 'destroy(6)'). Usage: See
section 3.4 'Secure Modes of Operation' and section 3.5 'Secure SNMP Get/Set
Requests' in XCMI Security TC, for details of secure modes of access to this
row status object.
""")


class _XcmSvcMonServiceName_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmSvcMonServiceName based on XcmFixedLocaleDisplayString"""
    defaultHexValue = ""

    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceName_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmSvcMonServiceName_Object = MibTableColumn
xcmSvcMonServiceName = _XcmSvcMonServiceName_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 3),
    _XcmSvcMonServiceName_Type()
)
xcmSvcMonServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceName.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceName.setReference("""\
See: Section 9.5.1 'Server-name' in DPA (ISO/IEC 10175-1 Final Text, March
1996). See: 'xcmHrDevInfoName' in XCMI Ext to Host Res MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceName.setDescription("""\
A human-readable name, used by system administrators and end-users to identify
this service. Usage: This name SHALL be either: a) the name normally used in a
command shell for control of this service (eg,
'showstopper.sample.com/bin/scan2file'); or b) the local user-friendly service
name (eg, 'ScanToFile'). Usage: Conforming implementations need NOT ensure that
each 'xcmSvcMonServiceEntry' has a non-empty (on the managed system)
'xcmSvcMonServiceName' (ie, names support is optional), but a given
'xcmSvcMonServiceName' SHALL be found via the same value of
'xcmSecServiceIndex' on the same managed system (ie, service names SHALL be
persistent).
""")


class _XcmSvcMonServiceCurrentState_Type(XcmHrDpaState):
    """Custom type xcmSvcMonServiceCurrentState based on XcmHrDpaState"""


_XcmSvcMonServiceCurrentState_Object = MibTableColumn
xcmSvcMonServiceCurrentState = _XcmSvcMonServiceCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 4),
    _XcmSvcMonServiceCurrentState_Type()
)
xcmSvcMonServiceCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceCurrentState.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceCurrentState.setReference("""\
See: Section 9.5.4 'Server-state' and section 9.1.6.4 'State' (generic object
state) in DPA (ISO/IEC 10175-1 Final Text, March 1996). See: Section D.2.3
'Server State Transitions' in DPA Mgmt Service (ISO 10175-3 Draft, October
1996). See: 'hrDeviceStatus' in IETF Host Resources MIB (RFC 2790). See:
'xcmHrDevInfoXStatus' and 'xcmHrDevInfoConditions' in XCMI Ext to Host
Resources MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceCurrentState.setDescription("""\
The current state of this system and/or end-user service. Usage: The current
DPA object generic state of a service.
""")


class _XcmSvcMonServicePreviousState_Type(XcmHrDpaState):
    """Custom type xcmSvcMonServicePreviousState based on XcmHrDpaState"""


_XcmSvcMonServicePreviousState_Object = MibTableColumn
xcmSvcMonServicePreviousState = _XcmSvcMonServicePreviousState_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 5),
    _XcmSvcMonServicePreviousState_Type()
)
xcmSvcMonServicePreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServicePreviousState.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServicePreviousState.setReference("""\
See: Section 9.5.4 'Server-state' and section 9.1.6.4 'State' (generic object
state) in DPA (ISO/IEC 10175-1 Final Text, March 1996). See: Section D.2.3
'Server State Transitions' in DPA Mgmt Service (ISO 10175-3 Draft, October
1996). See: 'hrDeviceStatus' in IETF Host Resources MIB (RFC 2790). See:
'xcmHrDevInfoXStatus' and 'xcmHrDevInfoConditions' in XCMI Ext to Host
Resources MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServicePreviousState.setDescription("""\
The previous state of this system and/or end-user service. Usage: The previous
DPA object generic state of a service.
""")
_XcmSvcMonServiceConditions_Type = XcmHrDpaConditions
_XcmSvcMonServiceConditions_Object = MibTableColumn
xcmSvcMonServiceConditions = _XcmSvcMonServiceConditions_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 6),
    _XcmSvcMonServiceConditions_Type()
)
xcmSvcMonServiceConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceConditions.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceConditions.setReference("""\
See: Section 9.5.4 'Server-state' and section 9.1.6.4 'State' (generic object
state) in DPA (ISO/IEC 10175-1 Final Text, March 1996). See: Section D.2.3
'Server State Transitions' in DPA Mgmt Service (ISO 10175-3 Draft, October
1996). See: 'hrDeviceStatus' in IETF Host Resources MIB (RFC 2790). See:
'xcmHrDevInfoXStatus' and 'xcmHrDevInfoConditions' in XCMI Ext to Host
Resources MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceConditions.setDescription("""\
The current conditions (ie, state reasons) of this system and/or end-user
service.
""")


class _XcmSvcMonServiceAvailability_Type(XcmHrDpaAvailability):
    """Custom type xcmSvcMonServiceAvailability based on XcmHrDpaAvailability"""


_XcmSvcMonServiceAvailability_Object = MibTableColumn
xcmSvcMonServiceAvailability = _XcmSvcMonServiceAvailability_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 7),
    _XcmSvcMonServiceAvailability_Type()
)
xcmSvcMonServiceAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceAvailability.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceAvailability.setReference("""\
See: Section 9.1.6.6 '[Generic attribute] Availability' and Annex A 'id-val-
availability-...' in DPA (ISO/IEC 10175-1 Final Text, March 1996).
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceAvailability.setDescription("""\
The availability of this system and/or end-user service.
""")
_XcmSvcMonServicePhysicalDevice_Type = Cardinal32
_XcmSvcMonServicePhysicalDevice_Object = MibTableColumn
xcmSvcMonServicePhysicalDevice = _XcmSvcMonServicePhysicalDevice_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 8),
    _XcmSvcMonServicePhysicalDevice_Type()
)
xcmSvcMonServicePhysicalDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServicePhysicalDevice.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServicePhysicalDevice.setReference("""\
See: 'hrDeviceIndex' in the Device group of IETF Host Resources MIB (RFC 2790).
See: 'xcmHrDevInfoRealization' in the Device Info group of XCMI Ext to Host
Resources MIB. See: Section 9.4 (pages 181 to 184) of DPA (Document Printing
Application) ISO/IEC 10175 (Final Text, March 1996) for a discussion of
'printer realizations' of 'physical', 'logical', and 'logical-and-physical'
types (the latter peculiar to DPA).
""")
if mibBuilder.loadTexts:
    xcmSvcMonServicePhysicalDevice.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the first associated physical
device row in the 'hrDeviceTable' in the Host Resources MIB (RFC 2790) and an
(optional) associated row in 'xcmHrDevInfoTable' of the XCMI Ext to Host
Resources MIB, or zero if none. Usage: Conforming implementations SHALL ensure
that physical devices underlying services are 'visible'.
""")
_XcmSvcMonServiceLogicalDevice_Type = Cardinal32
_XcmSvcMonServiceLogicalDevice_Object = MibTableColumn
xcmSvcMonServiceLogicalDevice = _XcmSvcMonServiceLogicalDevice_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 9),
    _XcmSvcMonServiceLogicalDevice_Type()
)
xcmSvcMonServiceLogicalDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceLogicalDevice.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceLogicalDevice.setReference("""\
See: 'xcmSvcMonServicePhysicalDevice' above.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceLogicalDevice.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the first associated logical
device row in the 'hrDeviceTable' in the Host Resources MIB (RFC 2790) and an
(optional) associated row in 'xcmHrDevInfoTable' of the XCMI Ext to Host
Resources MIB, or zero if none. Usage: Conforming implementations SHALL ensure
that logical devices presenting services are 'visible'.
""")
_XcmSvcMonServiceExternalDevice_Type = Cardinal32
_XcmSvcMonServiceExternalDevice_Object = MibTableColumn
xcmSvcMonServiceExternalDevice = _XcmSvcMonServiceExternalDevice_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 10),
    _XcmSvcMonServiceExternalDevice_Type()
)
xcmSvcMonServiceExternalDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceExternalDevice.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceExternalDevice.setReference("""\
See: 'hrDeviceIndex' in the Device group of IETF Host Resources MIB (RFC 2790).
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceExternalDevice.setDescription("""\
The value of 'hrDeviceIndex' corresponding to the first associated external
device row in the 'hrDeviceTable' in the Host Resources MIB (RFC 2790) and an
(optional) associated row in 'xcmHrDevInfoTable' of the XCMI Ext to Host
Resources MIB, or zero if none. Usage: Such an external device is termed a
'foreign attachment' and SHALL have 'xcmHrDevInfoRealization' of 'physical' in
the Device Info group of the XCMI Ext to Host Resources MIB - such a device
performs some security processing (any authentication, authorization, or
accounting), job processing, job finishing, or other off-system activity, on
behalf of this service.
""")
_XcmSvcMonServiceSWRun_Type = Cardinal32
_XcmSvcMonServiceSWRun_Object = MibTableColumn
xcmSvcMonServiceSWRun = _XcmSvcMonServiceSWRun_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 11),
    _XcmSvcMonServiceSWRun_Type()
)
xcmSvcMonServiceSWRun.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceSWRun.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceSWRun.setReference("""\
See: 'hrSWRunIndex' in the Software Running group of IETF Host Resources MIB
(RFC 2790). See: Software Running Extensions group of XCMI Ext to Host
Resources MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceSWRun.setDescription("""\
The value of 'hrSWRunIndex' corresponding to the first associated conceptual
row in the 'hrSWRunTable' of the Host Resources MIB (RFC 2790) and an
(optional) associated row in 'xcmHrSWRunTable' of the XCMI Ext to Host
Resources MIB, or zero if none. Usage: A 'chain' of one or more Software
Running entries in the Host Resources MIB MAY be associated with this service.
By convention, the FIRST of these entries SHALL represent the security
functional unit of this service.
""")
_XcmSvcMonServiceSWInstalled_Type = Cardinal32
_XcmSvcMonServiceSWInstalled_Object = MibTableColumn
xcmSvcMonServiceSWInstalled = _XcmSvcMonServiceSWInstalled_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 12),
    _XcmSvcMonServiceSWInstalled_Type()
)
xcmSvcMonServiceSWInstalled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceSWInstalled.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceSWInstalled.setReference("""\
See: 'hrSWInstalledIndex' in the Software Installed group of IETF Host
Resources MIB (RFC 2790). See: Software Installed Extensions group of XCMI Ext
to Host Resources MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceSWInstalled.setDescription("""\
The value of 'hrSWInstalledIndex' corresponding to the first associated
conceptual row in the 'hrSWInstalledTable' of the Host Resources MIB (RFC 2790)
and an (optional) associated row in 'xcmHrSWInstalledTable' in XCMI Ext to Host
Resources MIB, or zero if none. Usage: A 'chain' of one or more Software
Installed entries in the Host Resources MIB MAY be associated with a service.
By convention, the FIRST of these entries SHALL represent the security
functional unit of a service.
""")
_XcmSvcMonServiceStorage_Type = Cardinal32
_XcmSvcMonServiceStorage_Object = MibTableColumn
xcmSvcMonServiceStorage = _XcmSvcMonServiceStorage_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 13),
    _XcmSvcMonServiceStorage_Type()
)
xcmSvcMonServiceStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceStorage.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceStorage.setReference("""\
See: 'hrStorageIndex' in the Storage group of IETF Host Resources MIB (RFC
2790). See: Storage Extensions group of XCMI Ext to Host Resources MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceStorage.setDescription("""\
The value of 'hrStorageIndex' corresponding to the first associated conceptual
row in the 'hrStorageTable' of the Host Resources MIB (RFC 2790) and an
(optional) associated row in 'xcmHrStorageTable' of the XCMI Ext to Host
Resources MIB, or zero if none. Usage: A 'chain' of one or more Storage entries
in the Host Resources MIB MAY be associated with a service.
""")


class _XcmSvcMonServicePriority_Type(Integer32):
    """Custom type xcmSvcMonServicePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XcmSvcMonServicePriority_Type.__name__ = "Integer32"
_XcmSvcMonServicePriority_Object = MibTableColumn
xcmSvcMonServicePriority = _XcmSvcMonServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 14),
    _XcmSvcMonServicePriority_Type()
)
xcmSvcMonServicePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServicePriority.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServicePriority.setReference("""\
See: 'xcmHrDevInfoPriority' in XCMI Ext to Host Resources MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServicePriority.setDescription("""\
The current priority of this system and/or end-user service. Usage: The
scheduling priority of this service, where '0' is unspecified (default), '1' is
lowest, and '100' is highest.
""")


class _XcmSvcMonServiceType_Type(XcmSvcMonServiceType):
    """Custom type xcmSvcMonServiceType based on XcmSvcMonServiceType"""


_XcmSvcMonServiceType_Object = MibTableColumn
xcmSvcMonServiceType = _XcmSvcMonServiceType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 15),
    _XcmSvcMonServiceType_Type()
)
xcmSvcMonServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceType.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceType.setDescription("""\
The explicit type of this system and/or end-user service.
""")


class _XcmSvcMonServiceStateDetail_Type(OctetString):
    """Custom type xcmSvcMonServiceStateDetail based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XcmSvcMonServiceStateDetail_Type.__name__ = "OctetString"
_XcmSvcMonServiceStateDetail_Object = MibTableColumn
xcmSvcMonServiceStateDetail = _XcmSvcMonServiceStateDetail_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 2, 1, 16),
    _XcmSvcMonServiceStateDetail_Type()
)
xcmSvcMonServiceStateDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceStateDetail.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceStateDetail.setReference("""\
See: 'XcmSvcMonServiceStateDetail' in XCMI Service Monitor MIB TC; Section
7.1.4 'The BITS construct' in the IETF Coexistence between Version 1, Version
2, and Version 3 of the Internet-standard Network Management Framework SMIv2
(RFC 2578)
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceStateDetail.setDescription("""\
This object represents additional status details to further describe the
current state of the service. Usage: This bit-array is constructed from the set
of supported values from 'XcmSvcMonServiceStateDetail', used as powers of 2
with big-endian rules - the high-order bit of the first octet corresponds to a
service state detail '0' (reserved) - the low-order bit of the first octet
corresponds to a service state detail of '7'. Similar to the BITS pseudotype
defined in IETF SMIv2 (RFC 2578), which has the same bit ordering rules but
requires definitions for contiguous enumerated bits.
""")
_XcmSvcMonServiceDetail_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceDetail = _XcmSvcMonServiceDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6)
)
_XcmSvcMonServiceDetailTable_Object = MibTable
xcmSvcMonServiceDetailTable = _XcmSvcMonServiceDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailTable.setDescription("""\
A 'sparse' table containing service detail information for installed and
(possibly) active services on this host system, augmenting the basic entries in
the 'xcmSvcMonServiceTable' of the XCMI Service Monitoring MIB. Usage: UNLIKE
the 'xcmGenOptionTable' in the XCMI General MIB (which is a unique exception),
this table of 'dictionary-based' service details is used with DIRECT
create/update operations.
""")
_XcmSvcMonServiceDetailEntry_Object = MibTableRow
xcmSvcMonServiceDetailEntry = _XcmSvcMonServiceDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1)
)
xcmSvcMonServiceDetailEntry.setIndexNames(
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceIndex"),
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailClass"),
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailType"),
    (0, "XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailIndex"),
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailEntry.setDescription("""\
A 'sparse' entry containing service detail information for an installed and
(possibly) active service on this host system, augmenting a basic entry in the
'xcmSvcMonServiceTable' of the XCMI Service Monitoring MIB.
""")
_XcmSvcMonServiceDetailClass_Type = XcmSvcMonServiceDetailClass
_XcmSvcMonServiceDetailClass_Object = MibTableColumn
xcmSvcMonServiceDetailClass = _XcmSvcMonServiceDetailClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 1),
    _XcmSvcMonServiceDetailClass_Type()
)
xcmSvcMonServiceDetailClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailClass.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailClass.setDescription("""\
A service detail class, used by system administrators and end users to specify
the correct class for this service detail.
""")
_XcmSvcMonServiceDetailType_Type = XcmSvcMonServiceDetailType
_XcmSvcMonServiceDetailType_Object = MibTableColumn
xcmSvcMonServiceDetailType = _XcmSvcMonServiceDetailType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 2),
    _XcmSvcMonServiceDetailType_Type()
)
xcmSvcMonServiceDetailType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailType.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailType.setDescription("""\
A service detail type, used by system administrators and end users to specify
the correct type for this service detail.
""")
_XcmSvcMonServiceDetailIndex_Type = Ordinal32
_XcmSvcMonServiceDetailIndex_Object = MibTableColumn
xcmSvcMonServiceDetailIndex = _XcmSvcMonServiceDetailIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 3),
    _XcmSvcMonServiceDetailIndex_Type()
)
xcmSvcMonServiceDetailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmSvcMonServiceDetailTable', OR a common value shared across a set of related
conceptual rows (with different values of 'xcmSvcMonServiceDetailType'. Usage:
For service detail types which are single-valued, this index SHALL be used to
correlate related single-valued details. Usage: For service detail types which
are multi-valued, this index SHALL be used to enumerate lists of multi-valued
details.
""")
_XcmSvcMonServiceDetailRowStatus_Type = RowStatus
_XcmSvcMonServiceDetailRowStatus_Object = MibTableColumn
xcmSvcMonServiceDetailRowStatus = _XcmSvcMonServiceDetailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 4),
    _XcmSvcMonServiceDetailRowStatus_Type()
)
xcmSvcMonServiceDetailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailRowStatus.setReference("""\
See: 'xcmSvcMonGeneralCreateSupport' in 'xcmSvcMonGeneralTable'. See:
'RowStatus' in IETF SNMPv2 TC (RFC 1443/1903/2579). See:
'xcmHrDevMgmtCommandData' in XCMI HRX MIB and 'xcmSecUserMgmtData' in XCMI
Security MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailRowStatus.setDescription("""\
This object is used to create and delete individual conceptual rows in the
'xcmSvcMonServiceDetailTable'. Usage: Conforming implementations which support
static rows SHALL support 'active' and 'notInService' writes to this
'xcmSvcMonServiceDetailRowStatus' row status object; and SHALL clear the
'svcMonServiceDetailGroup' bit in 'xcmSvcMonGeneralCreateSupport' in the
'xcmSvcMonGeneralTable'. Usage: Conforming implementations which support
dynamic rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmSvcMonServiceDetailRowStatus' row status object; and SHALL set the
'svcMonServiceDetailGroup' bit in 'xcmSvcMonGeneralCreateSupport' in the
'xcmSvcMonGeneralTable'. Usage: Conforming implementations need NOT support
dynamic row creation (via 'createAndGo(4)') nor dynamic row deletion (via
'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and section
3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of secure
modes of access to this row status object.
""")


class _XcmSvcMonServiceDetailUnitClass_Type(XcmHrDevDetailUnitClass):
    """Custom type xcmSvcMonServiceDetailUnitClass based on XcmHrDevDetailUnitClass"""


_XcmSvcMonServiceDetailUnitClass_Object = MibTableColumn
xcmSvcMonServiceDetailUnitClass = _XcmSvcMonServiceDetailUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 5),
    _XcmSvcMonServiceDetailUnitClass_Type()
)
xcmSvcMonServiceDetailUnitClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailUnitClass.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailUnitClass.setReference("""\
See: 'xcmSvcMonServiceDetailUnit'
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailUnitClass.setDescription("""\
The value unit class of the detail information specified in this conceptual row
in the 'xcmSvcMonServiceDetailTable'. Usage: Used to select a textual
convention for specifying the value unit of this service detail. Usage: The
'xcmSvcMonServiceDetail[UnitClass|Class]' objects are used to specify the value
syntax AND the value unit of the 'xcmSvcMonServiceDetail[Integer|OID|String]'
value objects.
""")
_XcmSvcMonServiceDetailUnit_Type = Cardinal32
_XcmSvcMonServiceDetailUnit_Object = MibTableColumn
xcmSvcMonServiceDetailUnit = _XcmSvcMonServiceDetailUnit_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 6),
    _XcmSvcMonServiceDetailUnit_Type()
)
xcmSvcMonServiceDetailUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailUnit.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailUnit.setReference("""\
See: 'xcmSvcMonServiceDetailUnitClass'
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailUnit.setDescription("""\
The value unit of the detail information specified in this conceptual row in
the 'xcmSvcMonServiceDetailTable'. Usage: Used to select an enumerated choice
from a textual convention to specify the value unit of this service detail.
Usage: The 'xcmSvcMonServiceDetail[UnitClass|Class]' objects are used to
specify the value syntax AND the value unit of the
'xcmSvcMonServiceDetail[Integer|OID|String]' value objects.
""")
_XcmSvcMonServiceDetailInteger_Type = Integer32
_XcmSvcMonServiceDetailInteger_Object = MibTableColumn
xcmSvcMonServiceDetailInteger = _XcmSvcMonServiceDetailInteger_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 7),
    _XcmSvcMonServiceDetailInteger_Type()
)
xcmSvcMonServiceDetailInteger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailInteger.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailInteger.setReference("""\
See: 'xcmSvcMonServiceDetailOID' and 'xcmSvcMonServiceDetailString' See:
'xcmSvcMonServiceDetailUnitClass' and 'xcmSvcMonServiceDetailUnit' for syntax
of detail value
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailInteger.setDescription("""\
A service detail value integer, used by system administrators and end users to
specify the current value for a service detail with a base value syntax of
'INTEGER'.
""")


class _XcmSvcMonServiceDetailOID_Type(ObjectIdentifier):
    """Custom type xcmSvcMonServiceDetailOID based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_XcmSvcMonServiceDetailOID_Object = MibTableColumn
xcmSvcMonServiceDetailOID = _XcmSvcMonServiceDetailOID_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 8),
    _XcmSvcMonServiceDetailOID_Type()
)
xcmSvcMonServiceDetailOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailOID.setReference("""\
See: 'xcmSvcMonServiceDetailInteger' and 'xcmSvcMonServiceDetailString' See:
'xcmSvcMonServiceDetailUnitClass' and 'xcmSvcMonServiceDetailUnit' for syntax
of detail value
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailOID.setDescription("""\
A service detail value OID (object identifier), used by system administrators
and end users to specify the current value for a service detail with a base
value syntax of 'OBJECT IDENTIFIER'.
""")


class _XcmSvcMonServiceDetailString_Type(OctetString):
    """Custom type xcmSvcMonServiceDetailString based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceDetailString_Type.__name__ = "OctetString"
_XcmSvcMonServiceDetailString_Object = MibTableColumn
xcmSvcMonServiceDetailString = _XcmSvcMonServiceDetailString_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 6, 2, 1, 9),
    _XcmSvcMonServiceDetailString_Type()
)
xcmSvcMonServiceDetailString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailString.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailString.setReference("""\
See: 'xcmSvcMonServiceDetailInteger' and 'xcmSvcMonServiceDetailOID' See:
'xcmSvcMonServiceDetailUnitClass' and 'xcmSvcMonServiceDetailUnit' for syntax
of detail value
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailString.setDescription("""\
A service detail value string, used by system administrators and end users to
specify the current value for a service detail with a base value syntax of
'OCTET STRING'. Usage: This object is of type 'XcmFixedLocaleDisplayString'.
Usage: Conformant implementations MUST encrypt passwords, keys, and other
security information stored in this string object.
""")
_XcmSvcMonServiceMgmt_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceMgmt = _XcmSvcMonServiceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7)
)
_XcmSvcMonServiceMgmtV1EventOID_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceMgmtV1EventOID = _XcmSvcMonServiceMgmtV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 1)
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtV1EventOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtV1EventOID.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever an
'xcmSvcMonServiceMgmtOperation' completes. See SNMPv2 trap definition
'xcmSvcMonServiceMgmtV2Event' below for 'special semantics'.
""")
_XcmSvcMonServiceMgmtV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmSvcMonServiceMgmtV2EventPrefix = _XcmSvcMonServiceMgmtV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 1, 0)
)
_XcmSvcMonServiceMgmtTable_Object = MibTable
xcmSvcMonServiceMgmtTable = _XcmSvcMonServiceMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2)
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtTable.setDescription("""\
A table containing service management requests for control of system and/or
end-user services on this host system.
""")
_XcmSvcMonServiceMgmtEntry_Object = MibTableRow
xcmSvcMonServiceMgmtEntry = _XcmSvcMonServiceMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1)
)
xcmSvcMonServiceEntry.registerAugmentions(
    ("XEROX-SERVICE-MONITORING-MIB",
     "xcmSvcMonServiceMgmtEntry")
)
xcmSvcMonServiceMgmtEntry.setIndexNames(*xcmSvcMonServiceEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtEntry.setDescription("""\
An entry containing a service management request for control of a system and/or
end-user service on this host system.
""")
_XcmSvcMonServiceMgmtOperation_Type = XcmSvcMonServiceMgmtOperation
_XcmSvcMonServiceMgmtOperation_Object = MibTableColumn
xcmSvcMonServiceMgmtOperation = _XcmSvcMonServiceMgmtOperation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 1),
    _XcmSvcMonServiceMgmtOperation_Type()
)
xcmSvcMonServiceMgmtOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtOperation.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtOperation.setReference("""\
See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX Sys Admin (IEEE
1387.4 / Draft 8, October 1994). See: OBJECT clause in MODULE-COMPLIANCE macro
of XCMI Service Monitoring MIB, for compliance info.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtOperation.setDescription("""\
The most recent service management operation specified for this conceptual row
in the 'xcmSvcMonServiceMgmtTable'. Usage: Conforming management agents SHALL
'reject' any SNMP Set-Request to 'xcmSvcMonServiceMgmt[Operation|Data]' while
another management operation is already in progress (ie, while
'xcmSvcMonServiceMgmtInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3). Usage: Conforming management stations SHALL
set 'xcmSvcMonServiceMgmtOperation' (mgmt operation) and
'xcmSvcMonServiceMgmtData' (mgmt arguments) SIMULTANEOUSLY (in the same SNMP
Set-Request PDU).
""")


class _XcmSvcMonServiceMgmtData_Type(XcmSvcMonServiceMgmtData):
    """Custom type xcmSvcMonServiceMgmtData based on XcmSvcMonServiceMgmtData"""
    defaultHexValue = ""

    subtypeSpec = XcmSvcMonServiceMgmtData.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceMgmtData_Type.__name__ = "XcmSvcMonServiceMgmtData"
_XcmSvcMonServiceMgmtData_Object = MibTableColumn
xcmSvcMonServiceMgmtData = _XcmSvcMonServiceMgmtData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 2),
    _XcmSvcMonServiceMgmtData_Type()
)
xcmSvcMonServiceMgmtData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtData.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtData.setReference("""\
See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX Sys Admin (IEEE
1387.4 / Draft 8, October 1994). See: OBJECT clause in MODULE-COMPLIANCE macro
of XCMI Service Monitoring MIB, for compliance info. See:
'XcmHrDevMgmtCommandDataTag' textual convention, Section 3.4 'XCMI Standard
Tagged Management Data', and Section 3.5 'Simple Device Management Requests' in
XCMI Ext to Host Resources TC. See: Section 3.5.3 'Secure Simple Device Mgmt
Requests' in XCMI Security TC.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtData.setDescription("""\
The most recent service management data specified for this conceptual row in
the 'xcmSvcMonServiceMgmtTable'. Usage: Conforming management agents SHALL
'reject' any SNMP Set-Request to 'xcmSvcMonServiceMgmt[Operation|Data]' while
another management operation is already in progress (ie, while
'xcmSvcMonServiceMgmtInProgress' is 'true') with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3). Usage: Conforming management stations SHALL
set 'xcmSvcMonServiceMgmtOperation' (mgmt operation) and
'xcmSvcMonServiceMgmtData' (mgmt arguments) SIMULTANEOUSLY (in the same SNMP
Set-Request PDU). Usage: Conformant implementations MUST encrypt passwords,
keys, and other security information stored in this string object. Usage:
Management strings will be formatted as specified in the
'XcmHrDevMgmtCommandDataTag' textual convention. This means that the
'TT=value:' string format will be used with all management strings. Usage:
Strings that have been specified by XCMI are provided in the
'XcmSvcMonServiceMgmtData'.
""")
_XcmSvcMonServiceMgmtStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmSvcMonServiceMgmtStatus_Object = MibTableColumn
xcmSvcMonServiceMgmtStatus = _XcmSvcMonServiceMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 3),
    _XcmSvcMonServiceMgmtStatus_Type()
)
xcmSvcMonServiceMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtStatus.setReference("""\
See: 'xcmSvcMonServiceMgmt[Operation|Data|InProgress]'
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtStatus.setDescription("""\
The service management error status associated with this conceptual row in
'xcmSvcMonServiceMgmtTable'. Usage: Conforming management agents SHALL set this
object to the value returned in an SNMP Set-Response PDU when a service
management operation is 'accepted', ie, when 'xcmSvcMonServiceMgmtInProgress'
goes from 'false' to 'true'. Usage: Conforming management agents SHALL set this
object to the value of the completion status of the (possibly deferred) service
management operation, when 'xcmSvcMonServiceMgmtInProgress' goes from 'true' to
'false'.
""")


class _XcmSvcMonServiceMgmtInProgress_Type(TruthValue):
    """Custom type xcmSvcMonServiceMgmtInProgress based on TruthValue"""


_XcmSvcMonServiceMgmtInProgress_Object = MibTableColumn
xcmSvcMonServiceMgmtInProgress = _XcmSvcMonServiceMgmtInProgress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 4),
    _XcmSvcMonServiceMgmtInProgress_Type()
)
xcmSvcMonServiceMgmtInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtInProgress.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtInProgress.setReference("""\
See: 'xcmSvcMonServiceMgmt[Operation|Data|Status]'
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtInProgress.setDescription("""\
The service management in progress status associated with this conceptual row
in 'xcmSvcMonServiceMgmtTable'. Usage: Conforming management agents SHALL
'reject' any SNMP Set-Request to 'xcmSvcMonServiceMgmt[Operation|Data]' while
another management operation is already in progress (ie, while
'xcmSvcMonServiceMgmtInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3).
""")
_XcmSvcMonServiceMgmtRowStatus_Type = RowStatus
_XcmSvcMonServiceMgmtRowStatus_Object = MibTableColumn
xcmSvcMonServiceMgmtRowStatus = _XcmSvcMonServiceMgmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 5),
    _XcmSvcMonServiceMgmtRowStatus_Type()
)
xcmSvcMonServiceMgmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtRowStatus.setReference("""\
See: xcmSvcMonGeneralCreateSupport in the xcmSvcMonServiceGeneralTable. See:
RowStatus in IETF SNMPv2 TC (RFC 1443/1903/2579). See: xcmSvcMonServiceMgmtData
in XCMI Service Monitoring MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtRowStatus.setDescription("""\
This object manages the row status of this conceptual row in the
'xcmSvcMonServiceMgmtTable'. Usage: Conforming implementations which support
static rows SHALL support 'active' and 'notInService' writes to this
'xcmSvcMonServiceMgmtRowStatus' row status object; and SHALL clear the
'xcmSvcMonServiceMgmtGroup' bit in 'xcmSvcMonGeneralCreateSupport' in the
'xcmSvcMonServiceGeneralTable'. Usage: Conforming implementations which support
dynamic rows SHALL support 'createAndGo' and 'destroy' writes to this
'xcmSvcMonServiceMgmtRowStatus' row status object; and SHALL set the
'xcmSvcMonServiceMgmtGroup' bit in 'xcmSvcMonGeneralCreateSupport' in the
'xcmSvcMonServiceGeneralTable'. Usage: Conforming implementations need NOT
support dynamic row creation (via 'createAndGo(4)') nor dynamic row deletion
(via 'destroy(6)'). Usage: See section 3.4 'Secure Modes of Operation' and
section 3.5 'Secure SNMP Get/Set Requests' in XCMI Security TC, for details of
secure modes of access to this row status object.
""")


class _XcmSvcMonServiceMgmtUserPassword_Type(OctetString):
    """Custom type xcmSvcMonServiceMgmtUserPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceMgmtUserPassword_Type.__name__ = "OctetString"
_XcmSvcMonServiceMgmtUserPassword_Object = MibTableColumn
xcmSvcMonServiceMgmtUserPassword = _XcmSvcMonServiceMgmtUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 6),
    _XcmSvcMonServiceMgmtUserPassword_Type()
)
xcmSvcMonServiceMgmtUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtUserPassword.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtUserPassword.setReference("""\
See: 'xcmSvcMonServiceMgmt[Operator|Admin]Password' See: Section 3.5.2 'Secure
Password Change Requests' in XCMI Security TC. See: 'xcmSysAdminRequestTable'
in XCMI System Admin MIB and 'xcmSecUserTable' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtUserPassword.setDescription("""\
A protected end user password for this device. Usage: Conformant
implementations MUST encrypt passwords, keys, and other security information
stored in this string object. Usage: When changing the [User|Operator|Admin]
Password, conformant implementations MUST encrypt the NEW password that is
submitted in 'xcmSvcMonServiceMgmtData'. Usage: All XCMI conforming management
agents: a) SHOULD always return a zero length string in response to an SNMP
GetRequest of this object; b) SHALL NOT return the contents of this object in
cleartext (ie, unencrypted) in response to an SNMP GetRequest; c) SHOULD
support (ie, accept) an authenticated SNMP SetRequest changing the system 'end
user password' that is used in this object.
""")


class _XcmSvcMonServiceMgmtOperatorPassword_Type(OctetString):
    """Custom type xcmSvcMonServiceMgmtOperatorPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceMgmtOperatorPassword_Type.__name__ = "OctetString"
_XcmSvcMonServiceMgmtOperatorPassword_Object = MibTableColumn
xcmSvcMonServiceMgmtOperatorPassword = _XcmSvcMonServiceMgmtOperatorPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 7),
    _XcmSvcMonServiceMgmtOperatorPassword_Type()
)
xcmSvcMonServiceMgmtOperatorPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtOperatorPassword.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtOperatorPassword.setReference("""\
See: 'xcmSvcMonServiceMgmt[User|Admin]Password' See: Section 3.5.2 'Secure
Password Change Requests' in XCMI Security TC. See: 'xcmSysAdminRequestTable'
in XCMI System Admin MIB and 'xcmSecUserTable' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtOperatorPassword.setDescription("""\
A protected system operator password for this device. Usage: Conformant
implementations MUST encrypt passwords, keys, and other security information
stored in this string object. Usage: When changing the [User|Operator|Admin]
Password, conformant implementations MUST encrypt the NEW password that is
submitted in 'xcmSvcMonServiceMgmtData'. Usage: All XCMI conforming management
agents: a) SHOULD always return a zero length string in response to an SNMP
GetRequest of this object; b) SHALL NOT return the contents of this object in
cleartext (ie, unencrypted) in response to an SNMP GetRequest; c) SHOULD
support (ie, accept) an authenticated SNMP SetRequest changing the system
'operator password' that is used in this object.
""")


class _XcmSvcMonServiceMgmtAdminPassword_Type(OctetString):
    """Custom type xcmSvcMonServiceMgmtAdminPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSvcMonServiceMgmtAdminPassword_Type.__name__ = "OctetString"
_XcmSvcMonServiceMgmtAdminPassword_Object = MibTableColumn
xcmSvcMonServiceMgmtAdminPassword = _XcmSvcMonServiceMgmtAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 2, 1, 8),
    _XcmSvcMonServiceMgmtAdminPassword_Type()
)
xcmSvcMonServiceMgmtAdminPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtAdminPassword.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtAdminPassword.setReference("""\
See: 'xcmSvcMonServiceMgmt[User|Operator]Password' See: Section 3.5.2 'Secure
Password Change Requests' in XCMI Security TC. See: 'xcmSysAdminRequestTable'
in XCMI System Admin MIB and 'xcmSecUserTable' in XCMI Security MIB.
""")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtAdminPassword.setDescription("""\
A protected system administrator password for this device. Usage: Conformant
implementations MUST encrypt passwords, keys, and other security information
stored in this string object. Usage: When changing the [User|Operator|Admin]
Password, conformant implementations MUST encrypt the NEW password that is
submitted in 'xcmSvcMonServiceMgmtData'. Usage: All XCMI conforming management
agents: a) SHOULD always return a zero length string in response to an SNMP
GetRequest of this object; b) SHALL NOT return the contents of this object in
cleartext (ie, unencrypted) in response to an SNMP GetRequest; c) SHOULD
support (ie, accept) an authenticated SNMP SetRequest changing the system
'administrator password' that is used in this object.
""")

# Managed Objects groups

xcmSvcMonGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 1)
)
xcmSvcMonGeneralGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralRowStatus"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralVersionID"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralVersionDate"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralGroupSupport"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralCreateSupport"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonGeneralUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmSvcMonGeneralGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonGeneralGroup.setDescription("""\
The Service Monitoring General Group.
""")

xcmSvcMonQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 3)
)
xcmSvcMonQueueGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueRowStatus"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueDomain"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueuePath"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueName"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueOnSystem"))
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueGroup.setDescription("""\
The Service Monitoring Associated Queue Group.
""")

xcmSvcMonQueueExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 4)
)
xcmSvcMonQueueExtGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueRoutingIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueConditions"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultCount"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultCode"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultString"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueRowCreateDate"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueRowTotalJobs"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueLastConnectDate"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueLastConnectJobs"))
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtGroup.setDescription("""\
The Service Monitoring Associated Queue Ext Group.
""")

xcmSvcMonServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 5)
)
xcmSvcMonServiceGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceRowStatus"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceName"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceCurrentState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServicePreviousState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceConditions"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceAvailability"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServicePhysicalDevice"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceLogicalDevice"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceExternalDevice"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceSWRun"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceSWInstalled"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceStorage"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServicePriority"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceType"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceStateDetail"))
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceGroup.setDescription("""\
The Service Monitoring Service Group.
""")

xcmSvcMonServiceDetailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 6)
)
xcmSvcMonServiceDetailGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailRowStatus"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailUnitClass"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailUnit"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailInteger"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailOID"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceDetailString"))
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceDetailGroup.setDescription("""\
The Service Monitoring Service Detail Group.
""")

xcmSvcMonServiceMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 2, 7)
)
xcmSvcMonServiceMgmtGroup.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtOperation"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtData"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtStatus"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtInProgress"))
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtGroup.setDescription("""\
The Service Monitoring Service Mgmt Group.
""")


# Notification objects

xcmSvcMonQueueExtV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 4, 1, 0, 1)
)
xcmSvcMonQueueExtV2Event.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueOnSystem"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueConditions"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultCount"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultCode"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonQueueFaultString"))
)
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtV2Event.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmSvcMonQueueExtV2Event.setDescription("""\
This is the definition of the SNMPv2 trap sent whenever
'xcmSvcMonQueue[State|Conditions|FaultCount]' changes. Note: The variable-
bindings of this trap have been chosen to specify a complete associated queue
status change while keeping trap messages reasonably concise (generally a few
hundred octets at most). This notification has the following special semantics:
o The queue's 'xcmSvcMonQueueIndex' field value SHALL be appended to this trap
object ID, as a BER binary OID suffix. This trap OID qualifier allows service
management/monitoring applications to limit the alerts they receive to ones
generated by associated queues of interest.
""")

xcmSvcMonServiceV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 5, 1, 0, 1)
)
xcmSvcMonServiceV2Event.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceCurrentState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServicePreviousState"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceConditions"))
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceV2Event.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmSvcMonServiceV2Event.setDescription("""\
This trap is sent whenever 'XcmSvcMonService[CurrentState|Conditions]' changes.
Note: The variable-bindings of this trap have been chosen to specify a complete
service status change while keeping trap messages reasonably concise (generally
a few hundred octets at most). This notification has the following special
semantics: o The service's 'xcmSvcMonServiceIndex' field value SHALL be
appended to this trap object ID, as a BER binary OID suffix. This trap OID
qualifier allows service management/monitoring applications to limit the alerts
they receive to ones generated by services of interest.
""")

xcmSvcMonServiceMgmtV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 7, 1, 0, 1)
)
xcmSvcMonServiceMgmtV2Event.setObjects(
      *(("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceIndex"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtOperation"),
        ("XEROX-SERVICE-MONITORING-MIB", "xcmSvcMonServiceMgmtStatus"))
)
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtV2Event.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmSvcMonServiceMgmtV2Event.setDescription("""\
This trap is sent whenever an 'XcmSvcMonServiceMgmtOperation' completes, ie,
when 'xcmSvcMonServiceMgmtStatus' becomes the completed operation status and
'XcmSvcMonServiceMgmtInProgress' goes from 'true' to 'false'. Note: The
variable-bindings of this trap have been chosen to specify a complete
management operation result while keeping trap messages reasonably concise
(generally a few hundred octets at most). This notification has the following
special semantics: o The service's 'xcmSvcMonServiceIndex' field value SHALL be
appended to this trap object ID, as a BER binary OID suffix. This trap OID
qualifier allows service management/monitoring applications to limit the alerts
they receive to ones generated by requests they have submitted.
""")


# Notifications groups


# Agent capabilities


# Module compliance

xcmSvcMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 74, 2, 3)
)
if mibBuilder.loadTexts:
    xcmSvcMonMIBCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmSvcMonMIBCompliance.setDescription("""\
The compliance statements for SNMP management agents that implement the Service
Monitoring MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-SERVICE-MONITORING-MIB",
    **{"xcmSvcMonZeroDummy": xcmSvcMonZeroDummy,
       "xcmSvcMonMIB": xcmSvcMonMIB,
       "xcmSvcMonGeneral": xcmSvcMonGeneral,
       "xcmSvcMonGeneralTable": xcmSvcMonGeneralTable,
       "xcmSvcMonGeneralEntry": xcmSvcMonGeneralEntry,
       "xcmSvcMonGeneralIndex": xcmSvcMonGeneralIndex,
       "xcmSvcMonGeneralRowStatus": xcmSvcMonGeneralRowStatus,
       "xcmSvcMonGeneralVersionID": xcmSvcMonGeneralVersionID,
       "xcmSvcMonGeneralVersionDate": xcmSvcMonGeneralVersionDate,
       "xcmSvcMonGeneralGroupSupport": xcmSvcMonGeneralGroupSupport,
       "xcmSvcMonGeneralCreateSupport": xcmSvcMonGeneralCreateSupport,
       "xcmSvcMonGeneralUpdateSupport": xcmSvcMonGeneralUpdateSupport,
       "xcmSvcMonMIBConformance": xcmSvcMonMIBConformance,
       "xcmSvcMonMIBGroups": xcmSvcMonMIBGroups,
       "xcmSvcMonGeneralGroup": xcmSvcMonGeneralGroup,
       "xcmSvcMonQueueGroup": xcmSvcMonQueueGroup,
       "xcmSvcMonQueueExtGroup": xcmSvcMonQueueExtGroup,
       "xcmSvcMonServiceGroup": xcmSvcMonServiceGroup,
       "xcmSvcMonServiceDetailGroup": xcmSvcMonServiceDetailGroup,
       "xcmSvcMonServiceMgmtGroup": xcmSvcMonServiceMgmtGroup,
       "xcmSvcMonMIBCompliance": xcmSvcMonMIBCompliance,
       "xcmSvcMonQueue": xcmSvcMonQueue,
       "xcmSvcMonQueueTable": xcmSvcMonQueueTable,
       "xcmSvcMonQueueEntry": xcmSvcMonQueueEntry,
       "xcmSvcMonQueueIndex": xcmSvcMonQueueIndex,
       "xcmSvcMonQueueRowStatus": xcmSvcMonQueueRowStatus,
       "xcmSvcMonQueueDomain": xcmSvcMonQueueDomain,
       "xcmSvcMonQueuePath": xcmSvcMonQueuePath,
       "xcmSvcMonQueueName": xcmSvcMonQueueName,
       "xcmSvcMonQueueOnSystem": xcmSvcMonQueueOnSystem,
       "xcmSvcMonQueueExt": xcmSvcMonQueueExt,
       "xcmSvcMonQueueExtV1EventOID": xcmSvcMonQueueExtV1EventOID,
       "xcmSvcMonQueueExtV2EventPrefix": xcmSvcMonQueueExtV2EventPrefix,
       "xcmSvcMonQueueExtV2Event": xcmSvcMonQueueExtV2Event,
       "xcmSvcMonQueueExtTable": xcmSvcMonQueueExtTable,
       "xcmSvcMonQueueExtEntry": xcmSvcMonQueueExtEntry,
       "xcmSvcMonQueueRoutingIndex": xcmSvcMonQueueRoutingIndex,
       "xcmSvcMonQueueState": xcmSvcMonQueueState,
       "xcmSvcMonQueueConditions": xcmSvcMonQueueConditions,
       "xcmSvcMonQueueFaultCount": xcmSvcMonQueueFaultCount,
       "xcmSvcMonQueueFaultCode": xcmSvcMonQueueFaultCode,
       "xcmSvcMonQueueFaultString": xcmSvcMonQueueFaultString,
       "xcmSvcMonQueueRowCreateDate": xcmSvcMonQueueRowCreateDate,
       "xcmSvcMonQueueRowTotalJobs": xcmSvcMonQueueRowTotalJobs,
       "xcmSvcMonQueueLastConnectDate": xcmSvcMonQueueLastConnectDate,
       "xcmSvcMonQueueLastConnectJobs": xcmSvcMonQueueLastConnectJobs,
       "xcmSvcMonService": xcmSvcMonService,
       "xcmSvcMonServiceV1EventOID": xcmSvcMonServiceV1EventOID,
       "xcmSvcMonServiceV2EventPrefix": xcmSvcMonServiceV2EventPrefix,
       "xcmSvcMonServiceV2Event": xcmSvcMonServiceV2Event,
       "xcmSvcMonServiceTable": xcmSvcMonServiceTable,
       "xcmSvcMonServiceEntry": xcmSvcMonServiceEntry,
       "xcmSvcMonServiceIndex": xcmSvcMonServiceIndex,
       "xcmSvcMonServiceRowStatus": xcmSvcMonServiceRowStatus,
       "xcmSvcMonServiceName": xcmSvcMonServiceName,
       "xcmSvcMonServiceCurrentState": xcmSvcMonServiceCurrentState,
       "xcmSvcMonServicePreviousState": xcmSvcMonServicePreviousState,
       "xcmSvcMonServiceConditions": xcmSvcMonServiceConditions,
       "xcmSvcMonServiceAvailability": xcmSvcMonServiceAvailability,
       "xcmSvcMonServicePhysicalDevice": xcmSvcMonServicePhysicalDevice,
       "xcmSvcMonServiceLogicalDevice": xcmSvcMonServiceLogicalDevice,
       "xcmSvcMonServiceExternalDevice": xcmSvcMonServiceExternalDevice,
       "xcmSvcMonServiceSWRun": xcmSvcMonServiceSWRun,
       "xcmSvcMonServiceSWInstalled": xcmSvcMonServiceSWInstalled,
       "xcmSvcMonServiceStorage": xcmSvcMonServiceStorage,
       "xcmSvcMonServicePriority": xcmSvcMonServicePriority,
       "xcmSvcMonServiceType": xcmSvcMonServiceType,
       "xcmSvcMonServiceStateDetail": xcmSvcMonServiceStateDetail,
       "xcmSvcMonServiceDetail": xcmSvcMonServiceDetail,
       "xcmSvcMonServiceDetailTable": xcmSvcMonServiceDetailTable,
       "xcmSvcMonServiceDetailEntry": xcmSvcMonServiceDetailEntry,
       "xcmSvcMonServiceDetailClass": xcmSvcMonServiceDetailClass,
       "xcmSvcMonServiceDetailType": xcmSvcMonServiceDetailType,
       "xcmSvcMonServiceDetailIndex": xcmSvcMonServiceDetailIndex,
       "xcmSvcMonServiceDetailRowStatus": xcmSvcMonServiceDetailRowStatus,
       "xcmSvcMonServiceDetailUnitClass": xcmSvcMonServiceDetailUnitClass,
       "xcmSvcMonServiceDetailUnit": xcmSvcMonServiceDetailUnit,
       "xcmSvcMonServiceDetailInteger": xcmSvcMonServiceDetailInteger,
       "xcmSvcMonServiceDetailOID": xcmSvcMonServiceDetailOID,
       "xcmSvcMonServiceDetailString": xcmSvcMonServiceDetailString,
       "xcmSvcMonServiceMgmt": xcmSvcMonServiceMgmt,
       "xcmSvcMonServiceMgmtV1EventOID": xcmSvcMonServiceMgmtV1EventOID,
       "xcmSvcMonServiceMgmtV2EventPrefix": xcmSvcMonServiceMgmtV2EventPrefix,
       "xcmSvcMonServiceMgmtV2Event": xcmSvcMonServiceMgmtV2Event,
       "xcmSvcMonServiceMgmtTable": xcmSvcMonServiceMgmtTable,
       "xcmSvcMonServiceMgmtEntry": xcmSvcMonServiceMgmtEntry,
       "xcmSvcMonServiceMgmtOperation": xcmSvcMonServiceMgmtOperation,
       "xcmSvcMonServiceMgmtData": xcmSvcMonServiceMgmtData,
       "xcmSvcMonServiceMgmtStatus": xcmSvcMonServiceMgmtStatus,
       "xcmSvcMonServiceMgmtInProgress": xcmSvcMonServiceMgmtInProgress,
       "xcmSvcMonServiceMgmtRowStatus": xcmSvcMonServiceMgmtRowStatus,
       "xcmSvcMonServiceMgmtUserPassword": xcmSvcMonServiceMgmtUserPassword,
       "xcmSvcMonServiceMgmtOperatorPassword": xcmSvcMonServiceMgmtOperatorPassword,
       "xcmSvcMonServiceMgmtAdminPassword": xcmSvcMonServiceMgmtAdminPassword}
)

"""SNMP MIB module (XEROX-SIMPLE-JOB-MGMT-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-SIMPLE-JOB-MGMT-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:28 2024
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

(NotificationGroup,
 ModuleCompliance,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ModuleCompliance",
    "ObjectGroup")

(TimeTicks,
 Gauge32,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Integer32,
 Unsigned32,
 Bits,
 iso,
 IpAddress,
 Counter32,
 ModuleIdentity,
 NotificationType,
 Counter64,
 MibIdentifier) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "TimeTicks",
    "Gauge32",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Integer32",
    "Unsigned32",
    "Bits",
    "iso",
    "IpAddress",
    "Counter32",
    "ModuleIdentity",
    "NotificationType",
    "Counter64",
    "MibIdentifier")

(RowStatus,
 TruthValue,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "RowStatus",
    "TruthValue",
    "DisplayString",
    "TextualConvention")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(Ordinal32,
 XcmGenSNMPv2ErrorStatus,
 XcmFixedLocaleDisplayString) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Ordinal32",
    "XcmGenSNMPv2ErrorStatus",
    "XcmFixedLocaleDisplayString")

(xcmJobIdentifierOnSystem,
 xcmJobGenBasicEntry) = mibBuilder.importSymbols(
    "XEROX-JOB-MONITORING-MIB",
    "xcmJobIdentifierOnSystem",
    "xcmJobGenBasicEntry")

(XcmSimpleJobMgmtOperation,
 XcmSimpleJobMgmtGroupSupport,
 XcmSimpleJobMgmtData) = mibBuilder.importSymbols(
    "XEROX-SIMPLE-JOB-MGMT-TC",
    "XcmSimpleJobMgmtOperation",
    "XcmSimpleJobMgmtGroupSupport",
    "XcmSimpleJobMgmtData")


# MODULE-IDENTITY

xcmSimpleJobMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76)
)
xcmSimpleJobMgmtMIB.setLastUpdated("0209170000Z")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtMIB.setOrganization("""\
Xerox Corporation - XCMI Working Group
""")
xcmSimpleJobMgmtMIB.setContactInfo("""\
 XCMI Editors Email: coherence@crt.xerox.com
""")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtMIB.setDescription("""\
Version: 5.10.pub The MIB module for performing lightweight management of jobs
in network accessible host systems. See: Document Printing Application - Part
1: Abstract Service (ISO 10175-1 / Final Text, March 1996). See: POSIX System
Administration - Part 4: Print Interfaces (IEEE 1387.4 / Draft 8, October
1994). See: OSI Reference Model - Part 1: Basic Reference Model (CCITT
X.200:1992 | ISO 7498-1:1992). Copyright (C) 1997-2002 Xerox Corporation. All
Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XcmSimpleJobBase_ObjectIdentity = ObjectIdentity
xcmSimpleJobBase = _XcmSimpleJobBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1)
)
_XcmSimpleJobBaseTable_Object = MibTable
xcmSimpleJobBaseTable = _XcmSimpleJobBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2)
)
if mibBuilder.loadTexts:
    xcmSimpleJobBaseTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseTable.setDescription("""\
A table of general counters and capabilities for ease of use of the XCMI Simple
Job Mgmt MIB on this host system. Usage: The ONLY valid row in the
'xcmSimpleJobBaseTable' shall ALWAYS have an 'xcmSimpleJobBaseIndex' of one
('1').
""")
_XcmSimpleJobBaseEntry_Object = MibTableRow
xcmSimpleJobBaseEntry = _XcmSimpleJobBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1)
)
xcmSimpleJobBaseEntry.setIndexNames(
    (0, "XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobBaseIndex"),
)
if mibBuilder.loadTexts:
    xcmSimpleJobBaseEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseEntry.setDescription("""\
An entry of general counters and capabilities for ease of use of the XCMI
Simple Job Mgmt MIB on this host system. Usage: The ONLY valid row in the
'xcmSimpleJobBaseTable' shall ALWAYS have an 'xcmSimpleJobBaseIndex' of one
('1').
""")
_XcmSimpleJobBaseIndex_Type = Ordinal32
_XcmSimpleJobBaseIndex_Object = MibTableColumn
xcmSimpleJobBaseIndex = _XcmSimpleJobBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1, 1),
    _XcmSimpleJobBaseIndex_Type()
)
xcmSimpleJobBaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmSimpleJobBaseTable'. Usage: The ONLY valid row in the
'xcmSimpleJobBaseTable' shall ALWAYS have an 'xcmSimpleJobBaseIndex' of one
('1').
""")
_XcmSimpleJobBaseRowStatus_Type = RowStatus
_XcmSimpleJobBaseRowStatus_Object = MibTableColumn
xcmSimpleJobBaseRowStatus = _XcmSimpleJobBaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1, 2),
    _XcmSimpleJobBaseRowStatus_Type()
)
xcmSimpleJobBaseRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseRowStatus.setDescription("""\
This object is used to display status of the ONLY valid conceptual row in the
'xcmSimpleJobBaseTable'. Usage: 'xcmSimpleJobBaseRowStatus' is 'read-only'
because the ONLY valid conceptual row shall NOT be deleted.
""")


class _XcmSimpleJobBaseGroupSupport_Type(XcmSimpleJobMgmtGroupSupport):
    """Custom type xcmSimpleJobBaseGroupSupport based on XcmSimpleJobMgmtGroupSupport"""
    defaultValue = 3


_XcmSimpleJobBaseGroupSupport_Object = MibTableColumn
xcmSimpleJobBaseGroupSupport = _XcmSimpleJobBaseGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1, 3),
    _XcmSimpleJobBaseGroupSupport_Type()
)
xcmSimpleJobBaseGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseGroupSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Simple Job Mgmt MIB groups supported by this management agent
implementation (ie, version) on this host system, specified in a bit-mask.
Usage: Conforming management agents shall ALWAYS accurately report their
support for XCMI Simple Job Mgmt MIB groups.
""")
_XcmSimpleJobBaseCreateSupport_Type = XcmSimpleJobMgmtGroupSupport
_XcmSimpleJobBaseCreateSupport_Object = MibTableColumn
xcmSimpleJobBaseCreateSupport = _XcmSimpleJobBaseCreateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1, 4),
    _XcmSimpleJobBaseCreateSupport_Type()
)
xcmSimpleJobBaseCreateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseCreateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseCreateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Simple Job Mgmt MIB groups supported for dynamic row creation
(via '...RowStatus') by this management agent implementation (ie, version) on
this host system, specified in a bit-mask. Usage: Conforming management agents
shall ALWAYS accurately report their support for XCMI Simple Job Mgmt MIB
groups.
""")


class _XcmSimpleJobBaseUpdateSupport_Type(XcmSimpleJobMgmtGroupSupport):
    """Custom type xcmSimpleJobBaseUpdateSupport based on XcmSimpleJobMgmtGroupSupport"""
    defaultValue = 2


_XcmSimpleJobBaseUpdateSupport_Object = MibTableColumn
xcmSimpleJobBaseUpdateSupport = _XcmSimpleJobBaseUpdateSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 1, 2, 1, 5),
    _XcmSimpleJobBaseUpdateSupport_Type()
)
xcmSimpleJobBaseUpdateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseUpdateSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseUpdateSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional XCMI Simple Job Mgmt MIB groups supported for existing row update (via
SNMP Set-Request PDUs) by this management agent implementation (ie, version) on
this host system, specified in a bit-mask. Usage: Conforming management agents
shall ALWAYS accurately report their support for XCMI Simple Job Mgmt MIB
groups.
""")
_XcmSimpleJobMgmtMIBConformance_ObjectIdentity = ObjectIdentity
xcmSimpleJobMgmtMIBConformance = _XcmSimpleJobMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2)
)
_XcmSimpleJobMgmtMIBGroups_ObjectIdentity = ObjectIdentity
xcmSimpleJobMgmtMIBGroups = _XcmSimpleJobMgmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2, 2)
)
_XcmSimpleJobMgmt_ObjectIdentity = ObjectIdentity
xcmSimpleJobMgmt = _XcmSimpleJobMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3)
)
_XcmSimpleJobMgmtV1EventOID_ObjectIdentity = ObjectIdentity
xcmSimpleJobMgmtV1EventOID = _XcmSimpleJobMgmtV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 1)
)
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtV1EventOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtV1EventOID.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever an
'xcmSimpleJobMgmtOperation' completes. See SNMPv2 trap definition
'xcmSimpleJobMgmtV2Event' below for 'special semantics'.
""")
_XcmSimpleJobMgmtV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmSimpleJobMgmtV2EventPrefix = _XcmSimpleJobMgmtV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 1, 0)
)
_XcmSimpleJobMgmtTable_Object = MibTable
xcmSimpleJobMgmtTable = _XcmSimpleJobMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2)
)
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtTable.setDescription("""\
A table which augments the 'xcmJobGenBasicTable' in the XCMI Job Monitoring
MIB, to support simple job management of jobs on this host system.
""")
_XcmSimpleJobMgmtEntry_Object = MibTableRow
xcmSimpleJobMgmtEntry = _XcmSimpleJobMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2, 1)
)
xcmJobGenBasicEntry.registerAugmentions(
    ("XEROX-SIMPLE-JOB-MGMT-MIB",
     "xcmSimpleJobMgmtEntry")
)
xcmSimpleJobMgmtEntry.setIndexNames(*xcmJobGenBasicEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtEntry.setDescription("""\
An entry which augments an 'xcmJobGenBasicEntry' in the XCMI Job Monitoring
MIB, to support simple job management of a job on this host system.
""")
_XcmSimpleJobMgmtOperation_Type = XcmSimpleJobMgmtOperation
_XcmSimpleJobMgmtOperation_Object = MibTableColumn
xcmSimpleJobMgmtOperation = _XcmSimpleJobMgmtOperation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2, 1, 1),
    _XcmSimpleJobMgmtOperation_Type()
)
xcmSimpleJobMgmtOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtOperation.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtOperation.setReference("""\
See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX Sys Admin (IEEE
1387.4 / Draft 8, October 1994). See: OBJECT clauses in MODULE-COMPLIANCE macro
of XCMI Simple Job Mgmt MIB, for compliance info.
""")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtOperation.setDescription("""\
The simple job management operation specified for this conceptual row in the
'xcmSimpleJobMgmtTable' and the 'xcmJobGenBasicTable' (XCMI Job Monitoring
MIB). Usage: Conforming management agents SHALL 'reject' any SNMP Set-Operation
to 'xcmSimpleJobMgmt[Operation|Data]' while another management operation is
already in progress (ie, while 'xcmSimpleJobMgmtInProgress' is 'true'), with
'badValue' (SNMPv1) or 'inconsistentValue' (SNMPv2/v3). Usage: Conforming
management stations SHALL set 'xcmSimpleJobMgmtOperation' (mgmt operation) and
'xcmSimpleJobMgmtData' (mgmt arguments) SIMULTANEOUSLY (in the same SNMP Set-
Operation PDU). Usage: Performing 'delete' (system operator) shall ALWAYS force
'xcmJobCurrentState' to 'completed(17)' immediately, and MAY affect
'xcmJobAccountingBasicRowStatus'. Usage: Performing 'remove' (user cancel)
shall ALWAYS force 'xcmJobCurrentState' to 'completed(17)' in a timely fashion,
but shall NOT affect 'xcmJobAccountingBasicRowStatus'.
""")


class _XcmSimpleJobMgmtData_Type(XcmSimpleJobMgmtData):
    """Custom type xcmSimpleJobMgmtData based on XcmSimpleJobMgmtData"""
    defaultHexValue = ""

    subtypeSpec = XcmSimpleJobMgmtData.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSimpleJobMgmtData_Type.__name__ = "XcmSimpleJobMgmtData"
_XcmSimpleJobMgmtData_Object = MibTableColumn
xcmSimpleJobMgmtData = _XcmSimpleJobMgmtData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2, 1, 2),
    _XcmSimpleJobMgmtData_Type()
)
xcmSimpleJobMgmtData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtData.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtData.setReference("""\
See: Security Config, Account, and User groups in XCMI Security MIB. See:
Section 6.6 'Security in DPA' (pages 38 to 39) of DPA (ISO 10175-1 / Final
Text, March 1996). See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX
Sys Admin (IEEE 1387.4 / Draft 8, October 1994). See: OBJECT clauses in MODULE-
COMPLIANCE macro of XCMI Simple Job Mgmt MIB, for compliance info.
""")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtData.setDescription("""\
The simple job management data specified for this conceptual row in the
'xcmSimpleJobMgmtTable' and the 'xcmJobGenBasicTable' (XCMI Job Monitoring
MIB). Usage: Conforming management agents SHALL 'reject' any SNMP Set-Operation
to 'xcmSimpleJobMgmt[Operation|Data]' while another management operation is
already in progress (ie, while 'xcmSimpleJobMgmtInProgress' is 'true'), with
'badValue' (SNMPv1) or 'inconsistentValue' (SNMPv2/v3). Usage: Conforming
management stations SHALL set 'xcmSimpleJobMgmtOperation' (mgmt operation) and
'xcmSimpleJobMgmtData' (mgmt arguments) SIMULTANEOUSLY (in the same SNMP Set-
Operation PDU).
""")
_XcmSimpleJobMgmtStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmSimpleJobMgmtStatus_Object = MibTableColumn
xcmSimpleJobMgmtStatus = _XcmSimpleJobMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2, 1, 3),
    _XcmSimpleJobMgmtStatus_Type()
)
xcmSimpleJobMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtStatus.setReference("""\
See: 'xcmSimpleJobMgmt[Operation|Data|InProgress]'
""")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtStatus.setDescription("""\
The simple job management error status associated with this conceptual row in
'xcmSimpleJobMgmtTable'. Usage: Conforming management agents shall ALWAYS set
this object to the value returned in an SNMP Set-Response PDU when a simple job
management operation is 'accepted', ie, when 'xcmSimpleJobMgmtInProgress' goes
from 'false' to 'true'. Usage: Conforming management agents shall ALWAYS set
this object to the value of the completion status of the (possibly deferred)
simple job management operation, when 'xcmSimpleJobMgmtInProgress' goes from
'true' to 'false'.
""")


class _XcmSimpleJobMgmtInProgress_Type(TruthValue):
    """Custom type xcmSimpleJobMgmtInProgress based on TruthValue"""


_XcmSimpleJobMgmtInProgress_Object = MibTableColumn
xcmSimpleJobMgmtInProgress = _XcmSimpleJobMgmtInProgress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 2, 1, 4),
    _XcmSimpleJobMgmtInProgress_Type()
)
xcmSimpleJobMgmtInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtInProgress.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtInProgress.setReference("""\
See: 'xcmSimpleJobMgmt[Operation|Data|Status]'
""")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtInProgress.setDescription("""\
The simple job management in progress status associated with this conceptual
row in 'xcmSimpleJobMgmtTable'. Usage: Conforming management agents SHALL
'reject' any SNMP Set-Operation to 'xcmSimpleJobMgmt[Operation|Data]' while
another management operation is already in progress (ie, while
'xcmSimpleJobMgmtInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3).
""")
_XcmSimpleJobIntercept_ObjectIdentity = ObjectIdentity
xcmSimpleJobIntercept = _XcmSimpleJobIntercept_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4)
)
_XcmSimpleJobInterceptV1EventOID_ObjectIdentity = ObjectIdentity
xcmSimpleJobInterceptV1EventOID = _XcmSimpleJobInterceptV1EventOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 1)
)
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptV1EventOID.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptV1EventOID.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap sent whenever an
'xcmSimpleJobInterceptOperation' completes. See SNMPv2 trap definition
'xcmSimpleJobInterceptV2Event' below for 'special semantics'.
""")
_XcmSimpleJobInterceptV2EventPrefix_ObjectIdentity = ObjectIdentity
xcmSimpleJobInterceptV2EventPrefix = _XcmSimpleJobInterceptV2EventPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 1, 0)
)
_XcmSimpleJobInterceptTable_Object = MibTable
xcmSimpleJobInterceptTable = _XcmSimpleJobInterceptTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2)
)
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptTable.setDescription("""\
A table which is indexed by the future 'xcmJobClientId' in the XCMI Job
Monitoring MIB, to support simple job intercept requests for upstream jobs (off
this host system).
""")
_XcmSimpleJobInterceptEntry_Object = MibTableRow
xcmSimpleJobInterceptEntry = _XcmSimpleJobInterceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1)
)
xcmSimpleJobInterceptEntry.setIndexNames(
    (0, "XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptClientId"),
)
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptEntry.setDescription("""\
An entry which is indexed by the future 'xcmJobClientId' in the XCMI Job
Monitoring MIB, to support a simple job intercept request for an upstream job
(off this host system).
""")


class _XcmSimpleJobInterceptClientId_Type(XcmFixedLocaleDisplayString):
    """Custom type xcmSimpleJobInterceptClientId based on XcmFixedLocaleDisplayString"""
    subtypeSpec = XcmFixedLocaleDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_XcmSimpleJobInterceptClientId_Type.__name__ = "XcmFixedLocaleDisplayString"
_XcmSimpleJobInterceptClientId_Object = MibTableColumn
xcmSimpleJobInterceptClientId = _XcmSimpleJobInterceptClientId_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 1),
    _XcmSimpleJobInterceptClientId_Type()
)
xcmSimpleJobInterceptClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptClientId.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptClientId.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmSimpleJobInterceptTable'. Usage: The future value of 'xcmJobClientId' from
the XCMI Job Monitoring MIB which uniquely identifies this client's job. Usage:
XCMI conforming management agents MAY choose to REJECT any attempt at row
creation in the 'xcmSimpleJobInterceptTable' which specifies a value for
'xcmSimpleJobInterceptClientId' that does NOT conform to the
'XcmGlobalUniqueID' format (therefore cannot be appended onto the trap OID for
any job-related traps). Usage: XCMI conforming management agents MAY choose to
ACCEPT any attempt at row creation in the 'xcmSimpleJobInterceptTable' which
specifies a value for 'xcmSimpleJobInterceptClientId' that is nonetheless
unique in the scope of the managed system (but not append it onto the trap OID
for any job-related traps). Usage: XCMI conforming management stations (ie,
clients) shall ALWAYS submit an 'xcmJobClientId' in 'XcmGlobalUniqueID' format.
XCMI conforming management agents (ie, servers and devices) shall ALWAYS append
such an 'xcmJobClientId' onto the trap OID for any job-related traps. Usage:
Non-XCMI conforming management stations (ie, clients) MAY submit a non-unique
'xcmJobClientId', although they may be otherwise strictly conformant DPA (ISO
10175) clients.
""")
_XcmSimpleJobInterceptRowStatus_Type = RowStatus
_XcmSimpleJobInterceptRowStatus_Object = MibTableColumn
xcmSimpleJobInterceptRowStatus = _XcmSimpleJobInterceptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 2),
    _XcmSimpleJobInterceptRowStatus_Type()
)
xcmSimpleJobInterceptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptRowStatus.setDescription("""\
This object is used to create and destroy individual conceptual rows in
'xcmSimpleJobInterceptTable'.
""")
_XcmSimpleJobInterceptOperation_Type = XcmSimpleJobMgmtOperation
_XcmSimpleJobInterceptOperation_Object = MibTableColumn
xcmSimpleJobInterceptOperation = _XcmSimpleJobInterceptOperation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 3),
    _XcmSimpleJobInterceptOperation_Type()
)
xcmSimpleJobInterceptOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptOperation.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptOperation.setReference("""\
See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX Sys Admin (IEEE
1387.4 / Draft 8, October 1994). See: OBJECT clauses in MODULE-COMPLIANCE macro
of XCMI Simple Job Mgmt MIB, for compliance info.
""")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptOperation.setDescription("""\
The simple job intercept operation specified for this conceptual row in the
'xcmSimpleJobInterceptTable' and the 'xcmJobClientId' object (XCMI Job
Monitoring MIB). Usage: Conforming management agents SHALL 'reject' any SNMP
Set-Operation to 'xcmSimpleJobIntercept[Operation|Data]' while another
management operation is already in progress (ie, while
'xcmSimpleJobInterceptInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3). Usage: Conforming management stations SHALL
set 'xcmSimpleJobInterceptOperation' (mgmt operation) and
'xcmSimpleJobInterceptData' (mgmt arguments) SIMULTANEOUSLY (in the same SNMP
Set-Operation PDU).
""")


class _XcmSimpleJobInterceptData_Type(XcmSimpleJobMgmtData):
    """Custom type xcmSimpleJobInterceptData based on XcmSimpleJobMgmtData"""
    defaultHexValue = ""

    subtypeSpec = XcmSimpleJobMgmtData.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XcmSimpleJobInterceptData_Type.__name__ = "XcmSimpleJobMgmtData"
_XcmSimpleJobInterceptData_Object = MibTableColumn
xcmSimpleJobInterceptData = _XcmSimpleJobInterceptData_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 4),
    _XcmSimpleJobInterceptData_Type()
)
xcmSimpleJobInterceptData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptData.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptData.setReference("""\
See: Security Config, Account, and User groups in XCMI Security MIB. See:
Section 6.6 'Security in DPA' (pages 38 to 39) of DPA (ISO 10175-1 / Final
Text, March 1996). See: Section 4 'Print Utilities' (pages 71 to 212) of POSIX
Sys Admin (IEEE 1387.4 / Draft 8, October 1994). See: OBJECT clauses in MODULE-
COMPLIANCE macro of XCMI Simple Job Mgmt MIB, for compliance info.
""")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptData.setDescription("""\
The simple job intercept data specified for this conceptual row in the
'xcmSimpleJobInterceptTable' and the 'xcmJobClientId' object (XCMI Job
Monitoring MIB). Usage: Conforming management agents SHALL 'reject' any SNMP
Set-Operation to 'xcmSimpleJobIntercept[Operation|Data]' while another
management operation is already in progress (ie, while
'xcmSimpleJobInterceptInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3). Usage: Conforming management stations SHALL
set 'xcmSimpleJobInterceptOperation' (mgmt operation) and
'xcmSimpleJobInterceptData' (mgmt arguments) SIMULTANEOUSLY (in the same SNMP
Set-Operation PDU).
""")
_XcmSimpleJobInterceptStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmSimpleJobInterceptStatus_Object = MibTableColumn
xcmSimpleJobInterceptStatus = _XcmSimpleJobInterceptStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 5),
    _XcmSimpleJobInterceptStatus_Type()
)
xcmSimpleJobInterceptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptStatus.setReference("""\
See: 'xcmSimpleJobIntercept[Operation|Data|InProgress]'
""")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptStatus.setDescription("""\
The simple job intercept error status associated with this conceptual row in
'xcmSimpleJobInterceptTable'. Usage: Conforming management agents shall ALWAYS
set this object to the value returned in an SNMP Set-Response PDU when a simple
job intercept operation is 'accepted', ie, when
'xcmSimpleJobInterceptInProgress' goes from 'false' to 'true'. Usage:
Conforming management agents shall ALWAYS set this object to the value of the
completion status of the (possibly deferred) simple job intercept operation,
when 'xcmSimpleJobInterceptInProgress' goes from 'true' to 'false'.
""")


class _XcmSimpleJobInterceptInProgress_Type(TruthValue):
    """Custom type xcmSimpleJobInterceptInProgress based on TruthValue"""


_XcmSimpleJobInterceptInProgress_Object = MibTableColumn
xcmSimpleJobInterceptInProgress = _XcmSimpleJobInterceptInProgress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 2, 1, 6),
    _XcmSimpleJobInterceptInProgress_Type()
)
xcmSimpleJobInterceptInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptInProgress.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptInProgress.setReference("""\
See: 'xcmSimpleJobIntercept[Operation|Data|Status]'
""")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptInProgress.setDescription("""\
The simple job intercept in progress status associated with this conceptual row
in 'xcmSimpleJobInterceptTable'. Usage: Conforming management agents SHALL
'reject' any SNMP Set-Operation to 'xcmSimpleJobIntercept[Operation|Data]'
while another management operation is already in progress (ie, while
'xcmSimpleJobInterceptInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3).
""")

# Managed Objects groups

xcmSimpleJobBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2, 2, 1)
)
xcmSimpleJobBaseGroup.setObjects(
      *(("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobBaseRowStatus"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobBaseGroupSupport"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobBaseCreateSupport"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobBaseUpdateSupport"))
)
if mibBuilder.loadTexts:
    xcmSimpleJobBaseGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobBaseGroup.setDescription("""\
The Simple Job Base Group
""")

xcmSimpleJobMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2, 2, 3)
)
xcmSimpleJobMgmtGroup.setObjects(
      *(("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtOperation"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtData"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtStatus"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtInProgress"))
)
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtGroup.setDescription("""\
The Simple Job Mgmt Group
""")

xcmSimpleJobInterceptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2, 2, 4)
)
xcmSimpleJobInterceptGroup.setObjects(
      *(("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptClientId"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptRowStatus"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptOperation"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptData"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptStatus"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptInProgress"))
)
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptGroup.setDescription("""\
The Simple Job Intercept Group
""")


# Notification objects

xcmSimpleJobMgmtV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 3, 1, 0, 1)
)
xcmSimpleJobMgmtV2Event.setObjects(
      *(("HOST-RESOURCES-MIB", "hrDeviceIndex"),
        ("XEROX-JOB-MONITORING-MIB", "xcmJobIdentifierOnSystem"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtOperation"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobMgmtStatus"))
)
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtV2Event.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtV2Event.setDescription("""\
This trap is sent whenever an 'XcmSimpleJobMgmtOperation' completes, ie, when
'xcmSimpleJobMgmtStatus' becomes a completed operation status and
'XcmSimpleJobMgmtInProgress' goes from 'true' to 'false'. Note: The
'hrDeviceIndex' is included for convenience, even though the IETF Printer MIB
doesn't include 'hrDeviceIndex' in its traps. Then the management station
doesn't have to parse the received varBind OIDs on a trap in order to discover
which device trapped. Note: The variable-bindings of this trap have been chosen
to specify a complete job management operation result while keeping trap
messages reasonably concise (generally a few hundred octets at most). This
notification has the following special semantics: o If the job's
'xcmJobClientId' field is non-empty and it is a valid 'XcmGlobalUniqueID'
representation, its value shall ALWAYS be appended to this trap object ID, as a
BER binary OID suffix. Note: The BER binary OID suffix shall NOT include the
BER tag of 6 indicating an OID and shall NOT include the BER length field in
octets of the OID suffix. This trap OID qualifier allows job-submission and
job-monitoring applications to limit the alerts they receive to ones generated
by jobs which they have submitted. Note: The sum of the trap varBind values
must be less than can fit into a PDU on any transport, roughly 540 octets on
some transports. Thus implementors are warned to minimize the length of the
'xcmJobClientId' and 'xcmJobIdentifierOnSystem' objects.
""")

xcmSimpleJobInterceptV2Event = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 4, 1, 0, 1)
)
xcmSimpleJobInterceptV2Event.setObjects(
      *(("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptClientId"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptOperation"),
        ("XEROX-SIMPLE-JOB-MGMT-MIB", "xcmSimpleJobInterceptStatus"))
)
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptV2Event.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmSimpleJobInterceptV2Event.setDescription("""\
This trap is sent whenever an 'XcmSimpleJobInterceptOperation' completes. Note:
The variable-bindings of this trap have been chosen to specify a complete job
intercept operation result while keeping trap messages reasonably concise
(generally a few hundred octets at most). This notification has the following
special semantics: o If 'xcmSimpleJobInterceptClientId' is non-empty and it is
a valid 'XcmGlobalUniqueID' representation, its value shall ALWAYS be appended
to this trap object ID, as a BER binary OID suffix. Note: The BER binary OID
suffix shall NOT include the BER tag of 6 indicating an OID and shall NOT
include the BER length field in octets of the OID suffix. This trap OID
qualifier allows job-submission and job-monitoring applications to limit the
alerts they receive to ones generated by jobs which they have submitted. Note:
The sum of the trap varBind values must be less than can fit into a PDU on any
transport, roughly 540 octets on some transports. Thus implementors are warned
to minimize the length of the 'xcmJobClientId' and 'xcmJobIdentifierOnSystem'
objects.
""")


# Notifications groups


# Agent capabilities


# Module compliance

xcmSimpleJobMgmtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 76, 2, 3)
)
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtMIBCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmSimpleJobMgmtMIBCompliance.setDescription("""\
The compliance statements for SNMP intercept agents that implement the Simple
Job Mgmt MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-SIMPLE-JOB-MGMT-MIB",
    **{"xcmSimpleJobMgmtMIB": xcmSimpleJobMgmtMIB,
       "xcmSimpleJobBase": xcmSimpleJobBase,
       "xcmSimpleJobBaseTable": xcmSimpleJobBaseTable,
       "xcmSimpleJobBaseEntry": xcmSimpleJobBaseEntry,
       "xcmSimpleJobBaseIndex": xcmSimpleJobBaseIndex,
       "xcmSimpleJobBaseRowStatus": xcmSimpleJobBaseRowStatus,
       "xcmSimpleJobBaseGroupSupport": xcmSimpleJobBaseGroupSupport,
       "xcmSimpleJobBaseCreateSupport": xcmSimpleJobBaseCreateSupport,
       "xcmSimpleJobBaseUpdateSupport": xcmSimpleJobBaseUpdateSupport,
       "xcmSimpleJobMgmtMIBConformance": xcmSimpleJobMgmtMIBConformance,
       "xcmSimpleJobMgmtMIBGroups": xcmSimpleJobMgmtMIBGroups,
       "xcmSimpleJobBaseGroup": xcmSimpleJobBaseGroup,
       "xcmSimpleJobMgmtGroup": xcmSimpleJobMgmtGroup,
       "xcmSimpleJobInterceptGroup": xcmSimpleJobInterceptGroup,
       "xcmSimpleJobMgmtMIBCompliance": xcmSimpleJobMgmtMIBCompliance,
       "xcmSimpleJobMgmt": xcmSimpleJobMgmt,
       "xcmSimpleJobMgmtV1EventOID": xcmSimpleJobMgmtV1EventOID,
       "xcmSimpleJobMgmtV2EventPrefix": xcmSimpleJobMgmtV2EventPrefix,
       "xcmSimpleJobMgmtV2Event": xcmSimpleJobMgmtV2Event,
       "xcmSimpleJobMgmtTable": xcmSimpleJobMgmtTable,
       "xcmSimpleJobMgmtEntry": xcmSimpleJobMgmtEntry,
       "xcmSimpleJobMgmtOperation": xcmSimpleJobMgmtOperation,
       "xcmSimpleJobMgmtData": xcmSimpleJobMgmtData,
       "xcmSimpleJobMgmtStatus": xcmSimpleJobMgmtStatus,
       "xcmSimpleJobMgmtInProgress": xcmSimpleJobMgmtInProgress,
       "xcmSimpleJobIntercept": xcmSimpleJobIntercept,
       "xcmSimpleJobInterceptV1EventOID": xcmSimpleJobInterceptV1EventOID,
       "xcmSimpleJobInterceptV2EventPrefix": xcmSimpleJobInterceptV2EventPrefix,
       "xcmSimpleJobInterceptV2Event": xcmSimpleJobInterceptV2Event,
       "xcmSimpleJobInterceptTable": xcmSimpleJobInterceptTable,
       "xcmSimpleJobInterceptEntry": xcmSimpleJobInterceptEntry,
       "xcmSimpleJobInterceptClientId": xcmSimpleJobInterceptClientId,
       "xcmSimpleJobInterceptRowStatus": xcmSimpleJobInterceptRowStatus,
       "xcmSimpleJobInterceptOperation": xcmSimpleJobInterceptOperation,
       "xcmSimpleJobInterceptData": xcmSimpleJobInterceptData,
       "xcmSimpleJobInterceptStatus": xcmSimpleJobInterceptStatus,
       "xcmSimpleJobInterceptInProgress": xcmSimpleJobInterceptInProgress}
)

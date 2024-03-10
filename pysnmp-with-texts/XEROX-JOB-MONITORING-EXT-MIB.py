"""SNMP MIB module (XEROX-JOB-MONITORING-EXT-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-JOB-MONITORING-EXT-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 12:03:15 2024
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

(jmNumberOfInterveningJobs,
 jmJobKOctetsProcessed,
 jmJobImpressionsPerCopyRequested,
 jmJobEntry,
 jmJobStateReasons1,
 jmJobImpressionsCompleted,
 jmJobKOctetsPerCopyRequested,
 jmJobState) = mibBuilder.importSymbols(
    "Job-Monitoring-MIB",
    "jmNumberOfInterveningJobs",
    "jmJobKOctetsProcessed",
    "jmJobImpressionsPerCopyRequested",
    "jmJobEntry",
    "jmJobStateReasons1",
    "jmJobImpressionsCompleted",
    "jmJobKOctetsPerCopyRequested",
    "jmJobState")

(ObjectGroup,
 NotificationGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ObjectGroup",
    "NotificationGroup",
    "ModuleCompliance")

(TimeTicks,
 MibIdentifier,
 Bits,
 iso,
 Unsigned32,
 IpAddress,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Integer32,
 Gauge32,
 ObjectIdentity,
 Counter32,
 Counter64,
 ModuleIdentity,
 NotificationType) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "TimeTicks",
    "MibIdentifier",
    "Bits",
    "iso",
    "Unsigned32",
    "IpAddress",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Integer32",
    "Gauge32",
    "ObjectIdentity",
    "Counter32",
    "Counter64",
    "ModuleIdentity",
    "NotificationType")

(DisplayString,
 TruthValue,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TruthValue",
    "TextualConvention")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(XcmGenSNMPv2ErrorStatus,
 Ordinal32) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "XcmGenSNMPv2ErrorStatus",
    "Ordinal32")


# MODULE-IDENTITY

xcmJmxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83)
)
xcmJmxMIB.setLastUpdated("0211070000Z")
if mibBuilder.loadTexts:
    xcmJmxMIB.setOrganization("""\
Xerox Corporation - XCMI Working Group
""")
xcmJmxMIB.setContactInfo("""\
 XCMI Editors Email: coherence@crt.xerox.com
""")
if mibBuilder.loadTexts:
    xcmJmxMIB.setDescription("""\
Version: 5.401.pub The MIB module for job administration and job notifications
for systems that implement the PWG Job Monitoring MIB (RFC 2707). See: Section
7 'Conformance Requirements and Implementers Guide' of the XCMI Job Monitoring
TC (40jobtc.txt) for implementation and conformance guidance for the PWG Job
Monitoring MIB (RFC 2707) and for mapping to the XCMI Job Monitoring MIB.
Copyright (C) 2001-2002 Xerox Corporation. All Rights Reserved.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmJmxGroupSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )

    if mibBuilder.loadTexts:
        description = """\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional PWG Job Monitoring MIB (RFC 2707) and XCMI Ext to PWG Job Monitoring
MIB objects which are supported by this management agent implementation (i.e.,
version) on this host system, specified in a bit-mask. The current set of
values (which may be extended in the future) is given below: -- PWG Job
Monitoring MIB groups 1 : jmGeneralGroup -- 2**0 2 : jmJobIDGroup -- 2**1 4 :
jmJobGroup -- 2**2 8 : jmAttributeGroup -- 2**3 -- XCMI Ext to PWG Job
Monitoring MIB groups 16 : jmxGeneralGroup -- 2**4 32 : jmxJobAdminGroup --
2**5 64 : jmxJobTrapsGroup -- 2**6 128 : jmxJobOperationTrapsGroup -- 2**7
Usage: Conforming management agents shall ALWAYS accurately report their
support for PWG Job Monitoring MIB (RFC 2707) and XCMI Ext to PWG Job
Monitoring MIB object groups.
"""


class XcmJmxJobAdminOperation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("cancelJob", 3),
          ("holdJob", 4),
          ("other", 1),
          ("promoteJob", 10),
          ("releaseJob", 5),
          ("reprocessJob", 7),
          ("restartJob", 6),
          ("resumeJob", 9),
          ("suspendJob", 8),
          ("unknown", 2))
    )

    if mibBuilder.loadTexts:
        description = """\
The current or most recent administrative operation on this job (submitted via
SNMP, IPP, or any other job control protocol).
"""


class XcmJmxJobAccntSupport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 5),
          ("off", 4),
          ("on", 3),
          ("other", 1))
    )

    if mibBuilder.loadTexts:
        description = """\
Presence and configuration of a Job Accounting on the device. Note: This
enumeration may be extended for more granularity in the future.
"""


# MIB Managed Objects in the order of their OIDs

_XcmJmxMIBObjects_ObjectIdentity = ObjectIdentity
xcmJmxMIBObjects = _XcmJmxMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1)
)
_XcmJmxGeneral_ObjectIdentity = ObjectIdentity
xcmJmxGeneral = _XcmJmxGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1)
)
_XcmJmxGeneralTable_Object = MibTable
xcmJmxGeneralTable = _XcmJmxGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xcmJmxGeneralTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxGeneralTable.setDescription("""\
A table of general counters and information for ease of use of the XCMI Ext to
PWG Job Monitoring MIB and the PWG Job Monitoring MIB (RFC 2707) on this host
system. Usage: The ONLY valid row in the 'xcmJmxGeneralTable' shall ALWAYS have
an 'xcmJmxGeneralIndex' of one ('1').
""")
_XcmJmxGeneralEntry_Object = MibTableRow
xcmJmxGeneralEntry = _XcmJmxGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1)
)
xcmJmxGeneralEntry.setIndexNames(
    (0, "XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxGeneralIndex"),
)
if mibBuilder.loadTexts:
    xcmJmxGeneralEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxGeneralEntry.setDescription("""\
An entry of general counters and information for ease of use of the XCMI Ext to
PWG Job Monitoring MIB and the PWG Job Monitoring MIB (RFC 2707) on this host
system. Usage: The ONLY valid row in the 'xcmJmxGeneralTable' shall ALWAYS have
an 'xcmJmxGeneralIndex' of one ('1').
""")
_XcmJmxGeneralIndex_Type = Ordinal32
_XcmJmxGeneralIndex_Object = MibTableColumn
xcmJmxGeneralIndex = _XcmJmxGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 1),
    _XcmJmxGeneralIndex_Type()
)
xcmJmxGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmJmxGeneralIndex.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxGeneralIndex.setDescription("""\
A unique value used by this host system to identify this conceptual row in the
'xcmJmxGeneralTable'. Usage: The ONLY valid row in the 'xcmJmxGeneralTable'
shall ALWAYS have an 'xcmJmxGeneralIndex' of one ('1').
""")


class _XcmJmxGeneralGroupSupport_Type(XcmJmxGroupSupport):
    """Custom type xcmJmxGeneralGroupSupport based on XcmJmxGroupSupport"""
    defaultValue = 31


_XcmJmxGeneralGroupSupport_Object = MibTableColumn
xcmJmxGeneralGroupSupport = _XcmJmxGeneralGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 2),
    _XcmJmxGeneralGroupSupport_Type()
)
xcmJmxGeneralGroupSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxGeneralGroupSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxGeneralGroupSupport.setDescription("""\
The terse conformance statement of ALL mandatory, conditionally mandatory, and
optional PWG Job Monitoring MIB (RFC 2707) and XCMI Ext to PWG Job Monitoring
MIB objects which are supported by this management agent implementation (i.e.,
version) on this host system, specified in a bit-mask. Usage: Conforming
management agents shall ALWAYS accurately report their support for PWG Job
Monitoring MIB (RFC 2707) and XCMI Ext to PWG Job Monitoring MIB object groups.
""")
_XcmJmxGeneralJobCreatedCount_Type = Counter32
_XcmJmxGeneralJobCreatedCount_Object = MibTableColumn
xcmJmxGeneralJobCreatedCount = _XcmJmxGeneralJobCreatedCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 3),
    _XcmJmxGeneralJobCreatedCount_Type()
)
xcmJmxGeneralJobCreatedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobCreatedCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobCreatedCount.setDescription("""\
Total number of jobs that have been created on this managed system. The managed
system MAY preserve this count across initializations and resets. Usage: If the
value of this counter is not preserved across initializations and resets, then
it SHALL be set to zero upon system initialization or reset. Usage: A managed
system SHALL return zero if the number of jobs created is not known.
""")
_XcmJmxGeneralJobCompletedCount_Type = Counter32
_XcmJmxGeneralJobCompletedCount_Object = MibTableColumn
xcmJmxGeneralJobCompletedCount = _XcmJmxGeneralJobCompletedCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 4),
    _XcmJmxGeneralJobCompletedCount_Type()
)
xcmJmxGeneralJobCompletedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobCompletedCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobCompletedCount.setDescription("""\
Total number of jobs that have completed on this managed system. The managed
system MAY preserve this count across initializations and resets. Usage: If the
value of this counter is not preserved across initializations and resets, then
it SHALL be set to zero upon system initialization or reset. Usage: A managed
system SHALL return zero if the number of jobs created is not known.
""")
_XcmJmxGeneralJobOperationCount_Type = Counter32
_XcmJmxGeneralJobOperationCount_Object = MibTableColumn
xcmJmxGeneralJobOperationCount = _XcmJmxGeneralJobOperationCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 5),
    _XcmJmxGeneralJobOperationCount_Type()
)
xcmJmxGeneralJobOperationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobOperationCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobOperationCount.setDescription("""\
Total number of job operations that have been executed on this managed system.
The managed system MAY preserve this count across initializations and resets.
Usage: If the value of this counter is not preserved across initializations and
resets, then it SHALL be set to zero upon system initialization or reset.
Usage: A managed system SHALL return zero if the number of jobs created is not
known.
""")
_XcmJmxGeneralJobTrapCount_Type = Counter32
_XcmJmxGeneralJobTrapCount_Object = MibTableColumn
xcmJmxGeneralJobTrapCount = _XcmJmxGeneralJobTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 6),
    _XcmJmxGeneralJobTrapCount_Type()
)
xcmJmxGeneralJobTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobTrapCount.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobTrapCount.setDescription("""\
Total number of job traps that have been sent from this managed system. The
managed system MAY preserve this count across initializations and resets.
Usage: If the value of this counter is not preserved across initializations and
resets, then it SHALL be set to zero upon system initialization or reset.
Usage: A managed system SHALL return zero if the number of jobs created is not
known.
""")


class _XcmJmxGeneralJobAccntSupport_Type(XcmJmxJobAccntSupport):
    """Custom type xcmJmxGeneralJobAccntSupport based on XcmJmxJobAccntSupport"""


_XcmJmxGeneralJobAccntSupport_Object = MibTableColumn
xcmJmxGeneralJobAccntSupport = _XcmJmxGeneralJobAccntSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 7),
    _XcmJmxGeneralJobAccntSupport_Type()
)
xcmJmxGeneralJobAccntSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobAccntSupport.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobAccntSupport.setDescription("""\
This is a way to turn the Job Accounting in the device on and off when the
printer supports the PWG job accounting mib. If the job accounting within the
device is off then the group support will report no no group supported. If job
accounting is on then the appropriate groups will be reported as supported.
""")
_XcmJmxJobAdmin_ObjectIdentity = ObjectIdentity
xcmJmxJobAdmin = _XcmJmxJobAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 2)
)
_XcmJmxJobAdminTable_Object = MibTable
xcmJmxJobAdminTable = _XcmJmxJobAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xcmJmxJobAdminTable.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobAdminTable.setReference("""\
See: 'jmJobTable' in Job Monitoring MIB [RFC-2707].
""")
if mibBuilder.loadTexts:
    xcmJmxJobAdminTable.setDescription("""\
A table containing job operation requests for control of jobs on this host
system.
""")
_XcmJmxJobAdminEntry_Object = MibTableRow
xcmJmxJobAdminEntry = _XcmJmxJobAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 2, 1, 1)
)
jmJobEntry.registerAugmentions(
    ("XEROX-JOB-MONITORING-EXT-MIB",
     "xcmJmxJobAdminEntry")
)
xcmJmxJobAdminEntry.setIndexNames(*jmJobEntry.getIndexNames())
if mibBuilder.loadTexts:
    xcmJmxJobAdminEntry.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobAdminEntry.setDescription("""\
An entry containing a job operation request for control of a job on this host
system.
""")


class _XcmJmxJobAdminOperation_Type(XcmJmxJobAdminOperation):
    """Custom type xcmJmxJobAdminOperation based on XcmJmxJobAdminOperation"""


_XcmJmxJobAdminOperation_Object = MibTableColumn
xcmJmxJobAdminOperation = _XcmJmxJobAdminOperation_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 2, 1, 1, 1),
    _XcmJmxJobAdminOperation_Type()
)
xcmJmxJobAdminOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcmJmxJobAdminOperation.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobAdminOperation.setReference("""\
See: Section 3.3 'Job Operations' in IPP Model and Semantics [RFC-2911]. See:
Section 4 'Job Operations' in IPP Job and Printer Admin Operations [IPP-ADMIN].
See: 'xcmHrDevMgmtCommandDataTag' textual convention, Section 3.4 'XCMI
Standard Tagged Management Data', and Section 3.5 'Simple Device Management
Requests' in XCMI Host Resources Ext TC (for security issues). See: Section
3.5.3 'Secure Simple Device Mgmt Requests' in XCMI Security TC (for security
issues). See: 'xcmJmxJobAdmin[Status|InProgress]'
""")
if mibBuilder.loadTexts:
    xcmJmxJobAdminOperation.setDescription("""\
The current or most recent administrative operation on this job (submitted via
SNMP, IPP, or any other job control protocol). Usage: Conforming management
agents shall ALWAYS 'reject' any SNMP Set-Request to 'xcmJmxJobAdminOperation'
while another job operation request is already in progress (i.e., while
'xcmJmxJobAdminInProgress' is 'true'), with 'badValue' (SNMPv1) or
'inconsistentValue' (SNMPv2/v3).
""")
_XcmJmxJobAdminStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmJmxJobAdminStatus_Object = MibTableColumn
xcmJmxJobAdminStatus = _XcmJmxJobAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 2, 1, 1, 2),
    _XcmJmxJobAdminStatus_Type()
)
xcmJmxJobAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxJobAdminStatus.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobAdminStatus.setReference("""\
See: 'xcmJmxJobAdmin[Operation|InProgress]'
""")
if mibBuilder.loadTexts:
    xcmJmxJobAdminStatus.setDescription("""\
The job operation error status associated with this conceptual row in
'xcmJmxJobAdminTable'. Usage: Conforming management agents shall ALWAYS set
this object to the value returned in an SNMP Set-Response PDU when a job
operation request is 'accepted', ie, when 'xcmJmxJobAdminInProgress' goes from
'false' to 'true'. Usage: Conforming management agents shall ALWAYS set this
object to the value of the completion status of the (possibly deferred) job
operation request, when 'xcmJmxJobAdminInProgress' goes from 'true' to 'false'.
""")


class _XcmJmxJobAdminInProgress_Type(TruthValue):
    """Custom type xcmJmxJobAdminInProgress based on TruthValue"""


_XcmJmxJobAdminInProgress_Object = MibTableColumn
xcmJmxJobAdminInProgress = _XcmJmxJobAdminInProgress_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 2, 1, 1, 3),
    _XcmJmxJobAdminInProgress_Type()
)
xcmJmxJobAdminInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxJobAdminInProgress.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobAdminInProgress.setReference("""\
See: 'xcmJmxJobAdmin[Operation|Status]'
""")
if mibBuilder.loadTexts:
    xcmJmxJobAdminInProgress.setDescription("""\
The job operation in progress status associated with this conceptual row in
'xcmJmxJobAdminTable'. 'true' if job operation is in progress; otherwise,
'false'. Usage: Conforming management agents shall ALWAYS 'reject' any SNMP
Set-Request to 'xcmJmxJobAdminOperation' while another job operation request is
already in progress (i.e., while 'xcmJmxJobAdminInProgress' is 'true'), with
'badValue' (SNMPv1) or 'inconsistentValue' (SNMPv2/v3).
""")
_XcmJmxMIBNotifications_ObjectIdentity = ObjectIdentity
xcmJmxMIBNotifications = _XcmJmxMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2)
)
_XcmJmxJobOperationV1Enterprise_ObjectIdentity = ObjectIdentity
xcmJmxJobOperationV1Enterprise = _XcmJmxJobOperationV1Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 1)
)
if mibBuilder.loadTexts:
    xcmJmxJobOperationV1Enterprise.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobOperationV1Enterprise.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap for a Job operation
complete event sent by this managed system.
""")
_XcmJmxJobOperationV2TrapPrefix_ObjectIdentity = ObjectIdentity
xcmJmxJobOperationV2TrapPrefix = _XcmJmxJobOperationV2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 1, 0)
)
_XcmJmxJobStateV1Enterprise_ObjectIdentity = ObjectIdentity
xcmJmxJobStateV1Enterprise = _XcmJmxJobStateV1Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 2)
)
if mibBuilder.loadTexts:
    xcmJmxJobStateV1Enterprise.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobStateV1Enterprise.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap for a Job state
changed event sent by this managed system.
""")
_XcmJmxJobStateV2TrapPrefix_ObjectIdentity = ObjectIdentity
xcmJmxJobStateV2TrapPrefix = _XcmJmxJobStateV2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 2, 0)
)
_XcmJmxJobCreatedV1Enterprise_ObjectIdentity = ObjectIdentity
xcmJmxJobCreatedV1Enterprise = _XcmJmxJobCreatedV1Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 3)
)
if mibBuilder.loadTexts:
    xcmJmxJobCreatedV1Enterprise.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobCreatedV1Enterprise.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap for a Job created
event sent by this managed system.
""")
_XcmJmxJobCreatedV2TrapPrefix_ObjectIdentity = ObjectIdentity
xcmJmxJobCreatedV2TrapPrefix = _XcmJmxJobCreatedV2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 3, 0)
)
_XcmJmxJobCompletedV1Enterprise_ObjectIdentity = ObjectIdentity
xcmJmxJobCompletedV1Enterprise = _XcmJmxJobCompletedV1Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 4)
)
if mibBuilder.loadTexts:
    xcmJmxJobCompletedV1Enterprise.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobCompletedV1Enterprise.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap for a Job completed
event sent by this managed system.
""")
_XcmJmxJobCompletedV2TrapPrefix_ObjectIdentity = ObjectIdentity
xcmJmxJobCompletedV2TrapPrefix = _XcmJmxJobCompletedV2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 4, 0)
)
_XcmJmxJobStoppedV1Enterprise_ObjectIdentity = ObjectIdentity
xcmJmxJobStoppedV1Enterprise = _XcmJmxJobStoppedV1Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 5)
)
if mibBuilder.loadTexts:
    xcmJmxJobStoppedV1Enterprise.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobStoppedV1Enterprise.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap for a Job stopped
event sent by this managed system.
""")
_XcmJmxJobStoppedV2TrapPrefix_ObjectIdentity = ObjectIdentity
xcmJmxJobStoppedV2TrapPrefix = _XcmJmxJobStoppedV2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 5, 0)
)
_XcmJmxJobConfigV1Enterprise_ObjectIdentity = ObjectIdentity
xcmJmxJobConfigV1Enterprise = _XcmJmxJobConfigV1Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 6)
)
if mibBuilder.loadTexts:
    xcmJmxJobConfigV1Enterprise.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobConfigV1Enterprise.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap for a Job config
changed event sent by this managed system.
""")
_XcmJmxJobConfigV2TrapPrefix_ObjectIdentity = ObjectIdentity
xcmJmxJobConfigV2TrapPrefix = _XcmJmxJobConfigV2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 6, 0)
)
_XcmJmxJobProgressV1Enterprise_ObjectIdentity = ObjectIdentity
xcmJmxJobProgressV1Enterprise = _XcmJmxJobProgressV1Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 7)
)
if mibBuilder.loadTexts:
    xcmJmxJobProgressV1Enterprise.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobProgressV1Enterprise.setDescription("""\
The value of the enterprise-specific OID in an SNMPv1 trap for a Job progress
event sent by this managed system.
""")
_XcmJmxJobProgressV2TrapPrefix_ObjectIdentity = ObjectIdentity
xcmJmxJobProgressV2TrapPrefix = _XcmJmxJobProgressV2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 7, 0)
)
_XcmJmxMIBConformance_ObjectIdentity = ObjectIdentity
xcmJmxMIBConformance = _XcmJmxMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 3)
)
_XcmJmxMIBObjectGroups_ObjectIdentity = ObjectIdentity
xcmJmxMIBObjectGroups = _XcmJmxMIBObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 3, 2)
)
_XcmJmxMIBTrapGroups_ObjectIdentity = ObjectIdentity
xcmJmxMIBTrapGroups = _XcmJmxMIBTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 3, 3)
)

# Managed Objects groups

xcmJmxGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 3, 2, 1)
)
xcmJmxGeneralGroup.setObjects(
      *(("XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxGeneralGroupSupport"),
        ("XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxGeneralJobCreatedCount"),
        ("XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxGeneralJobCompletedCount"),
        ("XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxGeneralJobOperationCount"),
        ("XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxGeneralJobTrapCount"))
)
if mibBuilder.loadTexts:
    xcmJmxGeneralGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxGeneralGroup.setDescription("""\
The general group.
""")

xcmJmxJobAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 3, 2, 2)
)
xcmJmxJobAdminGroup.setObjects(
      *(("XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxJobAdminOperation"),
        ("XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxJobAdminStatus"),
        ("XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxJobAdminInProgress"))
)
if mibBuilder.loadTexts:
    xcmJmxJobAdminGroup.setStatus("current")
if mibBuilder.loadTexts:
    xcmJmxJobAdminGroup.setDescription("""\
The job administration group.
""")


# Notification objects

xcmJmxJobOperationV2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 1, 0, 1)
)
xcmJmxJobOperationV2Trap.setObjects(
      *(("Job-Monitoring-MIB", "jmJobState"),
        ("Job-Monitoring-MIB", "jmJobStateReasons1"),
        ("XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxJobAdminOperation"),
        ("XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxJobAdminStatus"))
)
if mibBuilder.loadTexts:
    xcmJmxJobOperationV2Trap.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmJmxJobOperationV2Trap.setDescription("""\
This SMIv2 trap corresponds to a Job operation complete event. The values of
'jmGeneralJobSetIndex' and 'jmJobIndex' for use with 'jmJobTable' for this Job
are conveyed in the instance qualifier (OID suffix) of 'jmJobOperation'.
Additional variable-bindings MAY be appended to this trap: - Systems with the
Host Resources MIB (RFC 2790) MAY add 'hrSystemDate' (compare to IPP 'printer-
current-time') - Systems MAY add other variable-bindings from any MIB
""")

xcmJmxJobStateV2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 2, 0, 1)
)
xcmJmxJobStateV2Trap.setObjects(
      *(("Job-Monitoring-MIB", "jmJobState"),
        ("Job-Monitoring-MIB", "jmJobStateReasons1"))
)
if mibBuilder.loadTexts:
    xcmJmxJobStateV2Trap.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmJmxJobStateV2Trap.setDescription("""\
This SMIv2 trap corresponds to IPP 'job-state-changed' event. The values of
'jmGeneralJobSetIndex' and 'jmJobIndex' for use with 'jmJobTable' for this Job
are conveyed in the instance qualifier (OID suffix) of 'jmJobState'. Additional
variable-bindings MAY be appended to this trap: - Systems with the Host
Resources MIB (RFC 2790) MAY add 'hrSystemDate' (compare to IPP 'printer-
current-time') - Systems MAY add other variable-bindings from any MIB
""")

xcmJmxJobCreatedV2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 3, 0, 1)
)
xcmJmxJobCreatedV2Trap.setObjects(
      *(("Job-Monitoring-MIB", "jmJobState"),
        ("Job-Monitoring-MIB", "jmJobStateReasons1"),
        ("Job-Monitoring-MIB", "jmNumberOfInterveningJobs"))
)
if mibBuilder.loadTexts:
    xcmJmxJobCreatedV2Trap.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmJmxJobCreatedV2Trap.setDescription("""\
This SMIv2 trap corresponds to IPP 'job-created' event.
""")

xcmJmxJobCompletedV2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 4, 0, 1)
)
xcmJmxJobCompletedV2Trap.setObjects(
      *(("Job-Monitoring-MIB", "jmJobState"),
        ("Job-Monitoring-MIB", "jmJobStateReasons1"),
        ("Job-Monitoring-MIB", "jmJobKOctetsProcessed"),
        ("Job-Monitoring-MIB", "jmJobImpressionsCompleted"))
)
if mibBuilder.loadTexts:
    xcmJmxJobCompletedV2Trap.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmJmxJobCompletedV2Trap.setDescription("""\
This SMIv2 trap corresponds to IPP 'job-completed' event.
""")

xcmJmxJobStoppedV2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 5, 0, 1)
)
xcmJmxJobStoppedV2Trap.setObjects(
      *(("Job-Monitoring-MIB", "jmJobState"),
        ("Job-Monitoring-MIB", "jmJobStateReasons1"),
        ("Job-Monitoring-MIB", "jmJobKOctetsProcessed"),
        ("Job-Monitoring-MIB", "jmJobImpressionsCompleted"))
)
if mibBuilder.loadTexts:
    xcmJmxJobStoppedV2Trap.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmJmxJobStoppedV2Trap.setDescription("""\
This SMIv2 trap corresponds to IPP 'job-stopped' event.
""")

xcmJmxJobConfigV2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 6, 0, 1)
)
xcmJmxJobConfigV2Trap.setObjects(
      *(("Job-Monitoring-MIB", "jmJobState"),
        ("Job-Monitoring-MIB", "jmJobStateReasons1"),
        ("Job-Monitoring-MIB", "jmNumberOfInterveningJobs"))
)
if mibBuilder.loadTexts:
    xcmJmxJobConfigV2Trap.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmJmxJobConfigV2Trap.setDescription("""\
This SMIv2 trap corresponds to IPP 'job-config-changed' event.
""")

xcmJmxJobProgressV2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 2, 7, 0, 1)
)
xcmJmxJobProgressV2Trap.setObjects(
      *(("Job-Monitoring-MIB", "jmJobKOctetsPerCopyRequested"),
        ("Job-Monitoring-MIB", "jmJobKOctetsProcessed"),
        ("Job-Monitoring-MIB", "jmJobImpressionsPerCopyRequested"),
        ("Job-Monitoring-MIB", "jmJobImpressionsCompleted"))
)
if mibBuilder.loadTexts:
    xcmJmxJobProgressV2Trap.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmJmxJobProgressV2Trap.setDescription("""\
This SMIv2 trap corresponds to an IPP 'job-progress' event.
""")


# Notifications groups


# Agent capabilities


# Module compliance

xcmJmxMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 3, 1)
)
if mibBuilder.loadTexts:
    xcmJmxMIBCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    xcmJmxMIBCompliance.setDescription("""\
The compliance statement for agents that implement this Job Admin MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-JOB-MONITORING-EXT-MIB",
    **{"XcmJmxGroupSupport": XcmJmxGroupSupport,
       "XcmJmxJobAdminOperation": XcmJmxJobAdminOperation,
       "XcmJmxJobAccntSupport": XcmJmxJobAccntSupport,
       "xcmJmxMIB": xcmJmxMIB,
       "xcmJmxMIBObjects": xcmJmxMIBObjects,
       "xcmJmxGeneral": xcmJmxGeneral,
       "xcmJmxGeneralTable": xcmJmxGeneralTable,
       "xcmJmxGeneralEntry": xcmJmxGeneralEntry,
       "xcmJmxGeneralIndex": xcmJmxGeneralIndex,
       "xcmJmxGeneralGroupSupport": xcmJmxGeneralGroupSupport,
       "xcmJmxGeneralJobCreatedCount": xcmJmxGeneralJobCreatedCount,
       "xcmJmxGeneralJobCompletedCount": xcmJmxGeneralJobCompletedCount,
       "xcmJmxGeneralJobOperationCount": xcmJmxGeneralJobOperationCount,
       "xcmJmxGeneralJobTrapCount": xcmJmxGeneralJobTrapCount,
       "xcmJmxGeneralJobAccntSupport": xcmJmxGeneralJobAccntSupport,
       "xcmJmxJobAdmin": xcmJmxJobAdmin,
       "xcmJmxJobAdminTable": xcmJmxJobAdminTable,
       "xcmJmxJobAdminEntry": xcmJmxJobAdminEntry,
       "xcmJmxJobAdminOperation": xcmJmxJobAdminOperation,
       "xcmJmxJobAdminStatus": xcmJmxJobAdminStatus,
       "xcmJmxJobAdminInProgress": xcmJmxJobAdminInProgress,
       "xcmJmxMIBNotifications": xcmJmxMIBNotifications,
       "xcmJmxJobOperationV1Enterprise": xcmJmxJobOperationV1Enterprise,
       "xcmJmxJobOperationV2TrapPrefix": xcmJmxJobOperationV2TrapPrefix,
       "xcmJmxJobOperationV2Trap": xcmJmxJobOperationV2Trap,
       "xcmJmxJobStateV1Enterprise": xcmJmxJobStateV1Enterprise,
       "xcmJmxJobStateV2TrapPrefix": xcmJmxJobStateV2TrapPrefix,
       "xcmJmxJobStateV2Trap": xcmJmxJobStateV2Trap,
       "xcmJmxJobCreatedV1Enterprise": xcmJmxJobCreatedV1Enterprise,
       "xcmJmxJobCreatedV2TrapPrefix": xcmJmxJobCreatedV2TrapPrefix,
       "xcmJmxJobCreatedV2Trap": xcmJmxJobCreatedV2Trap,
       "xcmJmxJobCompletedV1Enterprise": xcmJmxJobCompletedV1Enterprise,
       "xcmJmxJobCompletedV2TrapPrefix": xcmJmxJobCompletedV2TrapPrefix,
       "xcmJmxJobCompletedV2Trap": xcmJmxJobCompletedV2Trap,
       "xcmJmxJobStoppedV1Enterprise": xcmJmxJobStoppedV1Enterprise,
       "xcmJmxJobStoppedV2TrapPrefix": xcmJmxJobStoppedV2TrapPrefix,
       "xcmJmxJobStoppedV2Trap": xcmJmxJobStoppedV2Trap,
       "xcmJmxJobConfigV1Enterprise": xcmJmxJobConfigV1Enterprise,
       "xcmJmxJobConfigV2TrapPrefix": xcmJmxJobConfigV2TrapPrefix,
       "xcmJmxJobConfigV2Trap": xcmJmxJobConfigV2Trap,
       "xcmJmxJobProgressV1Enterprise": xcmJmxJobProgressV1Enterprise,
       "xcmJmxJobProgressV2TrapPrefix": xcmJmxJobProgressV2TrapPrefix,
       "xcmJmxJobProgressV2Trap": xcmJmxJobProgressV2Trap,
       "xcmJmxMIBConformance": xcmJmxMIBConformance,
       "xcmJmxMIBCompliance": xcmJmxMIBCompliance,
       "xcmJmxMIBObjectGroups": xcmJmxMIBObjectGroups,
       "xcmJmxGeneralGroup": xcmJmxGeneralGroup,
       "xcmJmxJobAdminGroup": xcmJmxJobAdminGroup,
       "xcmJmxMIBTrapGroups": xcmJmxMIBTrapGroups}
)

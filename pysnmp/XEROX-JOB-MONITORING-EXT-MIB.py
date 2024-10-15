# SNMP MIB module (XEROX-JOB-MONITORING-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-JOB-MONITORING-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:24 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

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

(jmJobEntry,
 jmJobImpressionsCompleted,
 jmJobImpressionsPerCopyRequested,
 jmJobKOctetsPerCopyRequested,
 jmJobKOctetsProcessed,
 jmJobState,
 jmJobStateReasons1,
 jmNumberOfInterveningJobs) = mibBuilder.importSymbols(
    "Job-Monitoring-MIB",
    "jmJobEntry",
    "jmJobImpressionsCompleted",
    "jmJobImpressionsPerCopyRequested",
    "jmJobKOctetsPerCopyRequested",
    "jmJobKOctetsProcessed",
    "jmJobState",
    "jmJobStateReasons1",
    "jmNumberOfInterveningJobs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")

(Ordinal32,
 XcmGenSNMPv2ErrorStatus) = mibBuilder.importSymbols(
    "XEROX-GENERAL-TC",
    "Ordinal32",
    "XcmGenSNMPv2ErrorStatus")


# MODULE-IDENTITY

xcmJmxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 83)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmJmxGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmJmxJobAdminOperation(Integer32, TextualConvention):
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



class XcmJmxJobAccntSupport(Integer32, TextualConvention):
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
_XcmJmxGeneralEntry_Object = MibTableRow
xcmJmxGeneralEntry = _XcmJmxGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1)
)
xcmJmxGeneralEntry.setIndexNames(
    (0, "XEROX-JOB-MONITORING-EXT-MIB", "xcmJmxGeneralIndex"),
)
if mibBuilder.loadTexts:
    xcmJmxGeneralEntry.setStatus("current")
_XcmJmxGeneralIndex_Type = Ordinal32
_XcmJmxGeneralIndex_Object = MibTableColumn
xcmJmxGeneralIndex = _XcmJmxGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 1),
    _XcmJmxGeneralIndex_Type()
)
xcmJmxGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xcmJmxGeneralIndex.setStatus("current")


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
_XcmJmxGeneralJobCreatedCount_Type = Counter32
_XcmJmxGeneralJobCreatedCount_Object = MibTableColumn
xcmJmxGeneralJobCreatedCount = _XcmJmxGeneralJobCreatedCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 3),
    _XcmJmxGeneralJobCreatedCount_Type()
)
xcmJmxGeneralJobCreatedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobCreatedCount.setStatus("current")
_XcmJmxGeneralJobCompletedCount_Type = Counter32
_XcmJmxGeneralJobCompletedCount_Object = MibTableColumn
xcmJmxGeneralJobCompletedCount = _XcmJmxGeneralJobCompletedCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 4),
    _XcmJmxGeneralJobCompletedCount_Type()
)
xcmJmxGeneralJobCompletedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobCompletedCount.setStatus("current")
_XcmJmxGeneralJobOperationCount_Type = Counter32
_XcmJmxGeneralJobOperationCount_Object = MibTableColumn
xcmJmxGeneralJobOperationCount = _XcmJmxGeneralJobOperationCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 5),
    _XcmJmxGeneralJobOperationCount_Type()
)
xcmJmxGeneralJobOperationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobOperationCount.setStatus("current")
_XcmJmxGeneralJobTrapCount_Type = Counter32
_XcmJmxGeneralJobTrapCount_Object = MibTableColumn
xcmJmxGeneralJobTrapCount = _XcmJmxGeneralJobTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 1, 2, 1, 6),
    _XcmJmxGeneralJobTrapCount_Type()
)
xcmJmxGeneralJobTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxGeneralJobTrapCount.setStatus("current")


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
_XcmJmxJobAdminEntry_Object = MibTableRow
xcmJmxJobAdminEntry = _XcmJmxJobAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xcmJmxJobAdminEntry.setStatus("current")


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
_XcmJmxJobAdminStatus_Type = XcmGenSNMPv2ErrorStatus
_XcmJmxJobAdminStatus_Object = MibTableColumn
xcmJmxJobAdminStatus = _XcmJmxJobAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 83, 1, 2, 1, 1, 2),
    _XcmJmxJobAdminStatus_Type()
)
xcmJmxJobAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcmJmxJobAdminStatus.setStatus("current")


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
jmJobEntry.registerAugmentions(
    ("XEROX-JOB-MONITORING-EXT-MIB",
     "xcmJmxJobAdminEntry")
)
xcmJmxJobAdminEntry.setIndexNames(*jmJobEntry.getIndexNames())

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

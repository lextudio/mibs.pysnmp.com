# SNMP MIB module (CISCO-CUICAPPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CUICAPPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:51 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCuicappsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 718)
)
ciscoCuicappsMIB.setRevisions(
        ("2010-01-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CuicServiceStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("notResponding", 3),
          ("partialService", 2),
          ("unknown", 4))
    )



class CuicSubsystemId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCuicappsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCuicappsMIBNotifs = _CiscoCuicappsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 0)
)
_CiscoCuicappsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCuicappsMIBObjects = _CiscoCuicappsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1)
)
_CuicGeneralInfoTable_Object = MibTable
cuicGeneralInfoTable = _CuicGeneralInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 1)
)
if mibBuilder.loadTexts:
    cuicGeneralInfoTable.setStatus("current")
_CuicGeneralInfoEntry_Object = MibTableRow
cuicGeneralInfoEntry = _CuicGeneralInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 1, 1)
)
cuicGeneralInfoEntry.setIndexNames(
    (0, "CISCO-CUICAPPS-MIB", "cuicGeneralInfoIndex"),
)
if mibBuilder.loadTexts:
    cuicGeneralInfoEntry.setStatus("current")
_CuicGeneralInfoIndex_Type = CuicSubsystemId
_CuicGeneralInfoIndex_Object = MibTableColumn
cuicGeneralInfoIndex = _CuicGeneralInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 1, 1, 1),
    _CuicGeneralInfoIndex_Type()
)
cuicGeneralInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cuicGeneralInfoIndex.setStatus("current")
_CuicGeneralInfoServerName_Type = SnmpAdminString
_CuicGeneralInfoServerName_Object = MibTableColumn
cuicGeneralInfoServerName = _CuicGeneralInfoServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 1, 1, 2),
    _CuicGeneralInfoServerName_Type()
)
cuicGeneralInfoServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicGeneralInfoServerName.setStatus("current")
_CuicGeneralInfoServerDescription_Type = SnmpAdminString
_CuicGeneralInfoServerDescription_Object = MibTableColumn
cuicGeneralInfoServerDescription = _CuicGeneralInfoServerDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 1, 1, 3),
    _CuicGeneralInfoServerDescription_Type()
)
cuicGeneralInfoServerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicGeneralInfoServerDescription.setStatus("current")
_CuicGeneralInfoVersion_Type = SnmpAdminString
_CuicGeneralInfoVersion_Object = MibTableColumn
cuicGeneralInfoVersion = _CuicGeneralInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 1, 1, 4),
    _CuicGeneralInfoVersion_Type()
)
cuicGeneralInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicGeneralInfoVersion.setStatus("current")
_CuicGeneralInfoStartTime_Type = DateAndTime
_CuicGeneralInfoStartTime_Object = MibTableColumn
cuicGeneralInfoStartTime = _CuicGeneralInfoStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 1, 1, 5),
    _CuicGeneralInfoStartTime_Type()
)
cuicGeneralInfoStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicGeneralInfoStartTime.setStatus("current")
_CuicGeneralInfoTimeZoneName_Type = SnmpAdminString
_CuicGeneralInfoTimeZoneName_Object = MibTableColumn
cuicGeneralInfoTimeZoneName = _CuicGeneralInfoTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 1, 1, 6),
    _CuicGeneralInfoTimeZoneName_Type()
)
cuicGeneralInfoTimeZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicGeneralInfoTimeZoneName.setStatus("current")
_CuicGeneralInfoSystemStatus_Type = CuicServiceStatus
_CuicGeneralInfoSystemStatus_Object = MibTableColumn
cuicGeneralInfoSystemStatus = _CuicGeneralInfoSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 1, 1, 7),
    _CuicGeneralInfoSystemStatus_Type()
)
cuicGeneralInfoSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicGeneralInfoSystemStatus.setStatus("current")
_CuicGeneralInfoOpsConsoleURL_Type = CiscoURLString
_CuicGeneralInfoOpsConsoleURL_Object = MibTableColumn
cuicGeneralInfoOpsConsoleURL = _CuicGeneralInfoOpsConsoleURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 1, 1, 8),
    _CuicGeneralInfoOpsConsoleURL_Type()
)
cuicGeneralInfoOpsConsoleURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicGeneralInfoOpsConsoleURL.setStatus("current")


class _CuicGeneralInfoEnableNotifications_Type(TruthValue):
    """Custom type cuicGeneralInfoEnableNotifications based on TruthValue"""


_CuicGeneralInfoEnableNotifications_Object = MibTableColumn
cuicGeneralInfoEnableNotifications = _CuicGeneralInfoEnableNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 1, 1, 9),
    _CuicGeneralInfoEnableNotifications_Type()
)
cuicGeneralInfoEnableNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuicGeneralInfoEnableNotifications.setStatus("current")
_CuicLicenseInfoTable_Object = MibTable
cuicLicenseInfoTable = _CuicLicenseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 2)
)
if mibBuilder.loadTexts:
    cuicLicenseInfoTable.setStatus("current")
_CuicLicenseInfoEntry_Object = MibTableRow
cuicLicenseInfoEntry = _CuicLicenseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 2, 1)
)
cuicLicenseInfoEntry.setIndexNames(
    (0, "CISCO-CUICAPPS-MIB", "cuicLicenseInfoIndex"),
)
if mibBuilder.loadTexts:
    cuicLicenseInfoEntry.setStatus("current")
_CuicLicenseInfoIndex_Type = CuicSubsystemId
_CuicLicenseInfoIndex_Object = MibTableColumn
cuicLicenseInfoIndex = _CuicLicenseInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 2, 1, 1),
    _CuicLicenseInfoIndex_Type()
)
cuicLicenseInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cuicLicenseInfoIndex.setStatus("current")


class _CuicLicenseInfoType_Type(Integer32):
    """Custom type cuicLicenseInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("premium", 4),
          ("standard", 3),
          ("trial", 2),
          ("unknown", 1))
    )


_CuicLicenseInfoType_Type.__name__ = "Integer32"
_CuicLicenseInfoType_Object = MibTableColumn
cuicLicenseInfoType = _CuicLicenseInfoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 2, 1, 2),
    _CuicLicenseInfoType_Type()
)
cuicLicenseInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicLicenseInfoType.setStatus("current")
_CuicLicenseInfoStartTime_Type = DateAndTime
_CuicLicenseInfoStartTime_Object = MibTableColumn
cuicLicenseInfoStartTime = _CuicLicenseInfoStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 2, 1, 3),
    _CuicLicenseInfoStartTime_Type()
)
cuicLicenseInfoStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicLicenseInfoStartTime.setStatus("current")
_CuicLicenseInfoExpirationTime_Type = DateAndTime
_CuicLicenseInfoExpirationTime_Object = MibTableColumn
cuicLicenseInfoExpirationTime = _CuicLicenseInfoExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 2, 1, 4),
    _CuicLicenseInfoExpirationTime_Type()
)
cuicLicenseInfoExpirationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicLicenseInfoExpirationTime.setStatus("current")
_CuicLicenseInfoHost_Type = SnmpAdminString
_CuicLicenseInfoHost_Object = MibTableColumn
cuicLicenseInfoHost = _CuicLicenseInfoHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 2, 1, 5),
    _CuicLicenseInfoHost_Type()
)
cuicLicenseInfoHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicLicenseInfoHost.setStatus("current")
_CuicReportingTable_Object = MibTable
cuicReportingTable = _CuicReportingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3)
)
if mibBuilder.loadTexts:
    cuicReportingTable.setStatus("current")
_CuicReportingEntry_Object = MibTableRow
cuicReportingEntry = _CuicReportingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1)
)
cuicReportingEntry.setIndexNames(
    (0, "CISCO-CUICAPPS-MIB", "cuicReportingIndex"),
)
if mibBuilder.loadTexts:
    cuicReportingEntry.setStatus("current")
_CuicReportingIndex_Type = CuicSubsystemId
_CuicReportingIndex_Object = MibTableColumn
cuicReportingIndex = _CuicReportingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1, 1),
    _CuicReportingIndex_Type()
)
cuicReportingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cuicReportingIndex.setStatus("current")
_CuicReportingDataSourceCount_Type = Gauge32
_CuicReportingDataSourceCount_Object = MibTableColumn
cuicReportingDataSourceCount = _CuicReportingDataSourceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1, 2),
    _CuicReportingDataSourceCount_Type()
)
cuicReportingDataSourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicReportingDataSourceCount.setStatus("current")
if mibBuilder.loadTexts:
    cuicReportingDataSourceCount.setUnits("data sources")
_CuicReportingEngineStatus_Type = CuicServiceStatus
_CuicReportingEngineStatus_Object = MibTableColumn
cuicReportingEngineStatus = _CuicReportingEngineStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1, 3),
    _CuicReportingEngineStatus_Type()
)
cuicReportingEngineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicReportingEngineStatus.setStatus("current")
_CuicReportingHistoricalReportDefinitionCount_Type = Gauge32
_CuicReportingHistoricalReportDefinitionCount_Object = MibTableColumn
cuicReportingHistoricalReportDefinitionCount = _CuicReportingHistoricalReportDefinitionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1, 4),
    _CuicReportingHistoricalReportDefinitionCount_Type()
)
cuicReportingHistoricalReportDefinitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicReportingHistoricalReportDefinitionCount.setStatus("current")
if mibBuilder.loadTexts:
    cuicReportingHistoricalReportDefinitionCount.setUnits("report definitions")
_CuicReportingRealTimeReportDefinitionCount_Type = Gauge32
_CuicReportingRealTimeReportDefinitionCount_Object = MibTableColumn
cuicReportingRealTimeReportDefinitionCount = _CuicReportingRealTimeReportDefinitionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1, 5),
    _CuicReportingRealTimeReportDefinitionCount_Type()
)
cuicReportingRealTimeReportDefinitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicReportingRealTimeReportDefinitionCount.setStatus("current")
if mibBuilder.loadTexts:
    cuicReportingRealTimeReportDefinitionCount.setUnits("report definitions")
_CuicReportingHistoricalReportRunning_Type = Gauge32
_CuicReportingHistoricalReportRunning_Object = MibTableColumn
cuicReportingHistoricalReportRunning = _CuicReportingHistoricalReportRunning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1, 6),
    _CuicReportingHistoricalReportRunning_Type()
)
cuicReportingHistoricalReportRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicReportingHistoricalReportRunning.setStatus("current")
if mibBuilder.loadTexts:
    cuicReportingHistoricalReportRunning.setUnits("reports")
_CuicReportingHistoricalReportWaiting_Type = Gauge32
_CuicReportingHistoricalReportWaiting_Object = MibTableColumn
cuicReportingHistoricalReportWaiting = _CuicReportingHistoricalReportWaiting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1, 7),
    _CuicReportingHistoricalReportWaiting_Type()
)
cuicReportingHistoricalReportWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicReportingHistoricalReportWaiting.setStatus("current")
if mibBuilder.loadTexts:
    cuicReportingHistoricalReportWaiting.setUnits("reports")
_CuicReportingTotalKickedOffHistoricalReports_Type = Counter32
_CuicReportingTotalKickedOffHistoricalReports_Object = MibTableColumn
cuicReportingTotalKickedOffHistoricalReports = _CuicReportingTotalKickedOffHistoricalReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1, 8),
    _CuicReportingTotalKickedOffHistoricalReports_Type()
)
cuicReportingTotalKickedOffHistoricalReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicReportingTotalKickedOffHistoricalReports.setStatus("current")
if mibBuilder.loadTexts:
    cuicReportingTotalKickedOffHistoricalReports.setUnits("reports")
_CuicReportingRealTimeReportRunning_Type = Gauge32
_CuicReportingRealTimeReportRunning_Object = MibTableColumn
cuicReportingRealTimeReportRunning = _CuicReportingRealTimeReportRunning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1, 9),
    _CuicReportingRealTimeReportRunning_Type()
)
cuicReportingRealTimeReportRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicReportingRealTimeReportRunning.setStatus("current")
if mibBuilder.loadTexts:
    cuicReportingRealTimeReportRunning.setUnits("reports")
_CuicReportingTotalKickedOffRealTimeReports_Type = Counter32
_CuicReportingTotalKickedOffRealTimeReports_Object = MibTableColumn
cuicReportingTotalKickedOffRealTimeReports = _CuicReportingTotalKickedOffRealTimeReports_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1, 10),
    _CuicReportingTotalKickedOffRealTimeReports_Type()
)
cuicReportingTotalKickedOffRealTimeReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicReportingTotalKickedOffRealTimeReports.setStatus("current")
if mibBuilder.loadTexts:
    cuicReportingTotalKickedOffRealTimeReports.setUnits("reports")
_CuicReportingRealTimeReportWaiting_Type = Gauge32
_CuicReportingRealTimeReportWaiting_Object = MibTableColumn
cuicReportingRealTimeReportWaiting = _CuicReportingRealTimeReportWaiting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 3, 1, 11),
    _CuicReportingRealTimeReportWaiting_Type()
)
cuicReportingRealTimeReportWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicReportingRealTimeReportWaiting.setStatus("current")
if mibBuilder.loadTexts:
    cuicReportingRealTimeReportWaiting.setUnits("reports")
_CuicSchedulerTable_Object = MibTable
cuicSchedulerTable = _CuicSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 4)
)
if mibBuilder.loadTexts:
    cuicSchedulerTable.setStatus("current")
_CuicSchedulerEntry_Object = MibTableRow
cuicSchedulerEntry = _CuicSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 4, 1)
)
cuicSchedulerEntry.setIndexNames(
    (0, "CISCO-CUICAPPS-MIB", "cuicSchedulerIndex"),
)
if mibBuilder.loadTexts:
    cuicSchedulerEntry.setStatus("current")
_CuicSchedulerIndex_Type = CuicSubsystemId
_CuicSchedulerIndex_Object = MibTableColumn
cuicSchedulerIndex = _CuicSchedulerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 4, 1, 1),
    _CuicSchedulerIndex_Type()
)
cuicSchedulerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cuicSchedulerIndex.setStatus("current")
_CuicSchedulerStatus_Type = CuicServiceStatus
_CuicSchedulerStatus_Object = MibTableColumn
cuicSchedulerStatus = _CuicSchedulerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 4, 1, 2),
    _CuicSchedulerStatus_Type()
)
cuicSchedulerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicSchedulerStatus.setStatus("current")
_CuicSchedulerEmailServerStatus_Type = CuicServiceStatus
_CuicSchedulerEmailServerStatus_Object = MibTableColumn
cuicSchedulerEmailServerStatus = _CuicSchedulerEmailServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 4, 1, 3),
    _CuicSchedulerEmailServerStatus_Type()
)
cuicSchedulerEmailServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicSchedulerEmailServerStatus.setStatus("current")
_CuicSchedulerJobsCompletedCount_Type = Counter32
_CuicSchedulerJobsCompletedCount_Object = MibTableColumn
cuicSchedulerJobsCompletedCount = _CuicSchedulerJobsCompletedCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 4, 1, 4),
    _CuicSchedulerJobsCompletedCount_Type()
)
cuicSchedulerJobsCompletedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicSchedulerJobsCompletedCount.setStatus("current")
if mibBuilder.loadTexts:
    cuicSchedulerJobsCompletedCount.setUnits("jobs")
_CuicSchedulerJobsRunningCount_Type = Gauge32
_CuicSchedulerJobsRunningCount_Object = MibTableColumn
cuicSchedulerJobsRunningCount = _CuicSchedulerJobsRunningCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 4, 1, 5),
    _CuicSchedulerJobsRunningCount_Type()
)
cuicSchedulerJobsRunningCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicSchedulerJobsRunningCount.setStatus("current")
if mibBuilder.loadTexts:
    cuicSchedulerJobsRunningCount.setUnits("jobs")
_CuicSchedulerJobsFailedCount_Type = Counter32
_CuicSchedulerJobsFailedCount_Object = MibTableColumn
cuicSchedulerJobsFailedCount = _CuicSchedulerJobsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 4, 1, 6),
    _CuicSchedulerJobsFailedCount_Type()
)
cuicSchedulerJobsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicSchedulerJobsFailedCount.setStatus("current")
if mibBuilder.loadTexts:
    cuicSchedulerJobsFailedCount.setUnits("jobs")
_CuicDbInfoTable_Object = MibTable
cuicDbInfoTable = _CuicDbInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 5)
)
if mibBuilder.loadTexts:
    cuicDbInfoTable.setStatus("current")
_CuicDbInfoEntry_Object = MibTableRow
cuicDbInfoEntry = _CuicDbInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 5, 1)
)
cuicDbInfoEntry.setIndexNames(
    (0, "CISCO-CUICAPPS-MIB", "cuicDbInfoIndex"),
)
if mibBuilder.loadTexts:
    cuicDbInfoEntry.setStatus("current")
_CuicDbInfoIndex_Type = CuicSubsystemId
_CuicDbInfoIndex_Object = MibTableColumn
cuicDbInfoIndex = _CuicDbInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 5, 1, 1),
    _CuicDbInfoIndex_Type()
)
cuicDbInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cuicDbInfoIndex.setStatus("current")
_CuicDbInfoStatus_Type = CuicServiceStatus
_CuicDbInfoStatus_Object = MibTableColumn
cuicDbInfoStatus = _CuicDbInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 5, 1, 2),
    _CuicDbInfoStatus_Type()
)
cuicDbInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicDbInfoStatus.setStatus("current")
_CuicDbInfoReplicationStatus_Type = CuicServiceStatus
_CuicDbInfoReplicationStatus_Object = MibTableColumn
cuicDbInfoReplicationStatus = _CuicDbInfoReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 5, 1, 3),
    _CuicDbInfoReplicationStatus_Type()
)
cuicDbInfoReplicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicDbInfoReplicationStatus.setStatus("current")


class _CuicDbInfoTmpSpaceUsed_Type(Gauge32):
    """Custom type cuicDbInfoTmpSpaceUsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CuicDbInfoTmpSpaceUsed_Type.__name__ = "Gauge32"
_CuicDbInfoTmpSpaceUsed_Object = MibTableColumn
cuicDbInfoTmpSpaceUsed = _CuicDbInfoTmpSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 5, 1, 4),
    _CuicDbInfoTmpSpaceUsed_Type()
)
cuicDbInfoTmpSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicDbInfoTmpSpaceUsed.setStatus("current")
if mibBuilder.loadTexts:
    cuicDbInfoTmpSpaceUsed.setUnits("percent")


class _CuicDbInfoSpaceUsed_Type(Gauge32):
    """Custom type cuicDbInfoSpaceUsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CuicDbInfoSpaceUsed_Type.__name__ = "Gauge32"
_CuicDbInfoSpaceUsed_Object = MibTableColumn
cuicDbInfoSpaceUsed = _CuicDbInfoSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 5, 1, 5),
    _CuicDbInfoSpaceUsed_Type()
)
cuicDbInfoSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicDbInfoSpaceUsed.setStatus("current")
if mibBuilder.loadTexts:
    cuicDbInfoSpaceUsed.setUnits("percent")
_CuicClusterTable_Object = MibTable
cuicClusterTable = _CuicClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 6)
)
if mibBuilder.loadTexts:
    cuicClusterTable.setStatus("current")
_CuicClusterEntry_Object = MibTableRow
cuicClusterEntry = _CuicClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 6, 1)
)
cuicClusterEntry.setIndexNames(
    (0, "CISCO-CUICAPPS-MIB", "cuicClusterIndex"),
)
if mibBuilder.loadTexts:
    cuicClusterEntry.setStatus("current")
_CuicClusterIndex_Type = CuicSubsystemId
_CuicClusterIndex_Object = MibTableColumn
cuicClusterIndex = _CuicClusterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 6, 1, 1),
    _CuicClusterIndex_Type()
)
cuicClusterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cuicClusterIndex.setStatus("current")
_CuicClusterName_Type = SnmpAdminString
_CuicClusterName_Object = MibTableColumn
cuicClusterName = _CuicClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 6, 1, 2),
    _CuicClusterName_Type()
)
cuicClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicClusterName.setStatus("current")
_CuicClusterServerCount_Type = Gauge32
_CuicClusterServerCount_Object = MibTableColumn
cuicClusterServerCount = _CuicClusterServerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 6, 1, 3),
    _CuicClusterServerCount_Type()
)
cuicClusterServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicClusterServerCount.setStatus("current")
if mibBuilder.loadTexts:
    cuicClusterServerCount.setUnits("servers")
_CuicClusterFirstNodeName_Type = SnmpAdminString
_CuicClusterFirstNodeName_Object = MibTableColumn
cuicClusterFirstNodeName = _CuicClusterFirstNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 6, 1, 4),
    _CuicClusterFirstNodeName_Type()
)
cuicClusterFirstNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicClusterFirstNodeName.setStatus("current")
_CuicDatasourceTable_Object = MibTable
cuicDatasourceTable = _CuicDatasourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 7)
)
if mibBuilder.loadTexts:
    cuicDatasourceTable.setStatus("current")
_CuicDatasourceEntry_Object = MibTableRow
cuicDatasourceEntry = _CuicDatasourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 7, 1)
)
cuicDatasourceEntry.setIndexNames(
    (0, "CISCO-CUICAPPS-MIB", "cuicDatasourceIndex"),
)
if mibBuilder.loadTexts:
    cuicDatasourceEntry.setStatus("current")


class _CuicDatasourceIndex_Type(Unsigned32):
    """Custom type cuicDatasourceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CuicDatasourceIndex_Type.__name__ = "Unsigned32"
_CuicDatasourceIndex_Object = MibTableColumn
cuicDatasourceIndex = _CuicDatasourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 7, 1, 1),
    _CuicDatasourceIndex_Type()
)
cuicDatasourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cuicDatasourceIndex.setStatus("current")
_CuicDatasourceName_Type = SnmpAdminString
_CuicDatasourceName_Object = MibTableColumn
cuicDatasourceName = _CuicDatasourceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 7, 1, 2),
    _CuicDatasourceName_Type()
)
cuicDatasourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicDatasourceName.setStatus("current")


class _CuicDatasourceStatus_Type(Integer32):
    """Custom type cuicDatasourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("unknown", 3))
    )


_CuicDatasourceStatus_Type.__name__ = "Integer32"
_CuicDatasourceStatus_Object = MibTableColumn
cuicDatasourceStatus = _CuicDatasourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 7, 1, 3),
    _CuicDatasourceStatus_Type()
)
cuicDatasourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicDatasourceStatus.setStatus("current")
_CuicDatasourceHost_Type = SnmpAdminString
_CuicDatasourceHost_Object = MibTableColumn
cuicDatasourceHost = _CuicDatasourceHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 7, 1, 4),
    _CuicDatasourceHost_Type()
)
cuicDatasourceHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicDatasourceHost.setStatus("current")


class _CuicDatasourceType_Type(Integer32):
    """Custom type cuicDatasourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informix", 3),
          ("mssql", 2),
          ("other", 1))
    )


_CuicDatasourceType_Type.__name__ = "Integer32"
_CuicDatasourceType_Object = MibTableColumn
cuicDatasourceType = _CuicDatasourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 7, 1, 5),
    _CuicDatasourceType_Type()
)
cuicDatasourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicDatasourceType.setStatus("current")
_CuicSecurityTable_Object = MibTable
cuicSecurityTable = _CuicSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 8)
)
if mibBuilder.loadTexts:
    cuicSecurityTable.setStatus("current")
_CuicSecurityEntry_Object = MibTableRow
cuicSecurityEntry = _CuicSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 8, 1)
)
cuicSecurityEntry.setIndexNames(
    (0, "CISCO-CUICAPPS-MIB", "cuicSecurityIndex"),
)
if mibBuilder.loadTexts:
    cuicSecurityEntry.setStatus("current")
_CuicSecurityIndex_Type = CuicSubsystemId
_CuicSecurityIndex_Object = MibTableColumn
cuicSecurityIndex = _CuicSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 8, 1, 1),
    _CuicSecurityIndex_Type()
)
cuicSecurityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cuicSecurityIndex.setStatus("current")
_CuicSecurityUsersConfigured_Type = Gauge32
_CuicSecurityUsersConfigured_Object = MibTableColumn
cuicSecurityUsersConfigured = _CuicSecurityUsersConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 8, 1, 2),
    _CuicSecurityUsersConfigured_Type()
)
cuicSecurityUsersConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicSecurityUsersConfigured.setStatus("current")
if mibBuilder.loadTexts:
    cuicSecurityUsersConfigured.setUnits("users")
_CuicSecurityUsersLoggedIn_Type = Gauge32
_CuicSecurityUsersLoggedIn_Object = MibTableColumn
cuicSecurityUsersLoggedIn = _CuicSecurityUsersLoggedIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 8, 1, 3),
    _CuicSecurityUsersLoggedIn_Type()
)
cuicSecurityUsersLoggedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicSecurityUsersLoggedIn.setStatus("current")
if mibBuilder.loadTexts:
    cuicSecurityUsersLoggedIn.setUnits("users")
_CuicSecurityLoginFailedAttempts_Type = Counter32
_CuicSecurityLoginFailedAttempts_Object = MibTableColumn
cuicSecurityLoginFailedAttempts = _CuicSecurityLoginFailedAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 8, 1, 4),
    _CuicSecurityLoginFailedAttempts_Type()
)
cuicSecurityLoginFailedAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicSecurityLoginFailedAttempts.setStatus("current")
_CuicSecurityGroupsConfigured_Type = Gauge32
_CuicSecurityGroupsConfigured_Object = MibTableColumn
cuicSecurityGroupsConfigured = _CuicSecurityGroupsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 8, 1, 5),
    _CuicSecurityGroupsConfigured_Type()
)
cuicSecurityGroupsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicSecurityGroupsConfigured.setStatus("current")
if mibBuilder.loadTexts:
    cuicSecurityGroupsConfigured.setUnits("groups")
_CuicThreadPoolInfo_ObjectIdentity = ObjectIdentity
cuicThreadPoolInfo = _CuicThreadPoolInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 9)
)
_CuicThreadsMaxAvailable_Type = Gauge32
_CuicThreadsMaxAvailable_Object = MibScalar
cuicThreadsMaxAvailable = _CuicThreadsMaxAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 9, 1),
    _CuicThreadsMaxAvailable_Type()
)
cuicThreadsMaxAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicThreadsMaxAvailable.setStatus("current")
if mibBuilder.loadTexts:
    cuicThreadsMaxAvailable.setUnits("threads")
_CuicThreadsRunning_Type = Gauge32
_CuicThreadsRunning_Object = MibScalar
cuicThreadsRunning = _CuicThreadsRunning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 9, 2),
    _CuicThreadsRunning_Type()
)
cuicThreadsRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicThreadsRunning.setStatus("current")
if mibBuilder.loadTexts:
    cuicThreadsRunning.setUnits("threads")
_CuicQueuedTasks_Type = Gauge32
_CuicQueuedTasks_Object = MibScalar
cuicQueuedTasks = _CuicQueuedTasks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 9, 3),
    _CuicQueuedTasks_Type()
)
cuicQueuedTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicQueuedTasks.setStatus("current")
if mibBuilder.loadTexts:
    cuicQueuedTasks.setUnits("tasks")
_CuicQueuedTasksMax_Type = Gauge32
_CuicQueuedTasksMax_Object = MibScalar
cuicQueuedTasksMax = _CuicQueuedTasksMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 9, 4),
    _CuicQueuedTasksMax_Type()
)
cuicQueuedTasksMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicQueuedTasksMax.setStatus("current")
if mibBuilder.loadTexts:
    cuicQueuedTasksMax.setUnits("tasks")
_CuicEnvInfo_ObjectIdentity = ObjectIdentity
cuicEnvInfo = _CuicEnvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 10)
)
_CuicWaErrors_Type = Counter32
_CuicWaErrors_Object = MibScalar
cuicWaErrors = _CuicWaErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 10, 1),
    _CuicWaErrors_Type()
)
cuicWaErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicWaErrors.setStatus("current")
if mibBuilder.loadTexts:
    cuicWaErrors.setUnits("errors")
_CuicWaSessionsActive_Type = Gauge32
_CuicWaSessionsActive_Object = MibScalar
cuicWaSessionsActive = _CuicWaSessionsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 10, 2),
    _CuicWaSessionsActive_Type()
)
cuicWaSessionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicWaSessionsActive.setStatus("current")
if mibBuilder.loadTexts:
    cuicWaSessionsActive.setUnits("sessions")


class _CuicJvmPercentCPUTime_Type(Gauge32):
    """Custom type cuicJvmPercentCPUTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CuicJvmPercentCPUTime_Type.__name__ = "Gauge32"
_CuicJvmPercentCPUTime_Object = MibScalar
cuicJvmPercentCPUTime = _CuicJvmPercentCPUTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 10, 3),
    _CuicJvmPercentCPUTime_Type()
)
cuicJvmPercentCPUTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicJvmPercentCPUTime.setStatus("current")
if mibBuilder.loadTexts:
    cuicJvmPercentCPUTime.setUnits("percent")
_CuicJvmMemoryFree_Type = Gauge32
_CuicJvmMemoryFree_Object = MibScalar
cuicJvmMemoryFree = _CuicJvmMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 10, 4),
    _CuicJvmMemoryFree_Type()
)
cuicJvmMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicJvmMemoryFree.setStatus("current")
if mibBuilder.loadTexts:
    cuicJvmMemoryFree.setUnits("kilo bytes")
_CuicJvmMemoryTotal_Type = Gauge32
_CuicJvmMemoryTotal_Object = MibScalar
cuicJvmMemoryTotal = _CuicJvmMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 10, 5),
    _CuicJvmMemoryTotal_Type()
)
cuicJvmMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicJvmMemoryTotal.setStatus("current")
if mibBuilder.loadTexts:
    cuicJvmMemoryTotal.setUnits("kilo bytes")
_CuicJvmMemoryMax_Type = Gauge32
_CuicJvmMemoryMax_Object = MibScalar
cuicJvmMemoryMax = _CuicJvmMemoryMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 10, 6),
    _CuicJvmMemoryMax_Type()
)
cuicJvmMemoryMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicJvmMemoryMax.setStatus("current")
if mibBuilder.loadTexts:
    cuicJvmMemoryMax.setUnits("kilo bytes")
_CuicTomcatThreadsBusy_Type = Gauge32
_CuicTomcatThreadsBusy_Object = MibScalar
cuicTomcatThreadsBusy = _CuicTomcatThreadsBusy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 10, 7),
    _CuicTomcatThreadsBusy_Type()
)
cuicTomcatThreadsBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicTomcatThreadsBusy.setStatus("current")
if mibBuilder.loadTexts:
    cuicTomcatThreadsBusy.setUnits("threads")
_CuicTomcatThreadsTotal_Type = Gauge32
_CuicTomcatThreadsTotal_Object = MibScalar
cuicTomcatThreadsTotal = _CuicTomcatThreadsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 10, 8),
    _CuicTomcatThreadsTotal_Type()
)
cuicTomcatThreadsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicTomcatThreadsTotal.setStatus("current")
if mibBuilder.loadTexts:
    cuicTomcatThreadsTotal.setUnits("threads")
_CuicTomcatThreadsMax_Type = Gauge32
_CuicTomcatThreadsMax_Object = MibScalar
cuicTomcatThreadsMax = _CuicTomcatThreadsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 10, 9),
    _CuicTomcatThreadsMax_Type()
)
cuicTomcatThreadsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuicTomcatThreadsMax.setStatus("current")
if mibBuilder.loadTexts:
    cuicTomcatThreadsMax.setUnits("threads")
_CuicNotificationInfo_ObjectIdentity = ObjectIdentity
cuicNotificationInfo = _CuicNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 11)
)
_CuicEventId_Type = Unsigned32
_CuicEventId_Object = MibScalar
cuicEventId = _CuicEventId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 11, 1),
    _CuicEventId_Type()
)
cuicEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cuicEventId.setStatus("current")
_CuicEventHostName_Type = SnmpAdminString
_CuicEventHostName_Object = MibScalar
cuicEventHostName = _CuicEventHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 11, 2),
    _CuicEventHostName_Type()
)
cuicEventHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cuicEventHostName.setStatus("current")
_CuicEventAppName_Type = SnmpAdminString
_CuicEventAppName_Object = MibScalar
cuicEventAppName = _CuicEventAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 11, 3),
    _CuicEventAppName_Type()
)
cuicEventAppName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cuicEventAppName.setStatus("current")
_CuicEventName_Type = SnmpAdminString
_CuicEventName_Object = MibScalar
cuicEventName = _CuicEventName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 11, 4),
    _CuicEventName_Type()
)
cuicEventName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cuicEventName.setStatus("current")


class _CuicEventState_Type(Integer32):
    """Custom type cuicEventState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("raise", 1))
    )


_CuicEventState_Type.__name__ = "Integer32"
_CuicEventState_Object = MibScalar
cuicEventState = _CuicEventState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 11, 5),
    _CuicEventState_Type()
)
cuicEventState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cuicEventState.setStatus("current")


class _CuicEventSeverity_Type(Integer32):
    """Custom type cuicEventSeverity based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("informational", 7),
          ("notice", 6),
          ("warning", 5))
    )


_CuicEventSeverity_Type.__name__ = "Integer32"
_CuicEventSeverity_Object = MibScalar
cuicEventSeverity = _CuicEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 11, 6),
    _CuicEventSeverity_Type()
)
cuicEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cuicEventSeverity.setStatus("current")
_CuicEventTimestamp_Type = DateAndTime
_CuicEventTimestamp_Object = MibScalar
cuicEventTimestamp = _CuicEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 11, 7),
    _CuicEventTimestamp_Type()
)
cuicEventTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cuicEventTimestamp.setStatus("current")
_CuicEventText_Type = SnmpAdminString
_CuicEventText_Object = MibScalar
cuicEventText = _CuicEventText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 1, 11, 8),
    _CuicEventText_Type()
)
cuicEventText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cuicEventText.setStatus("current")
_CiscoCuicappsMIBConform_ObjectIdentity = ObjectIdentity
ciscoCuicappsMIBConform = _CiscoCuicappsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2)
)
_CiscoCuicappsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCuicappsMIBCompliances = _CiscoCuicappsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 1)
)
_CiscoCuicappsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCuicappsMIBGroups = _CiscoCuicappsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2)
)

# Managed Objects groups

cuicGeneralInfoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 1)
)
cuicGeneralInfoTableGroup.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicGeneralInfoServerName"),
        ("CISCO-CUICAPPS-MIB", "cuicGeneralInfoServerDescription"),
        ("CISCO-CUICAPPS-MIB", "cuicGeneralInfoVersion"),
        ("CISCO-CUICAPPS-MIB", "cuicGeneralInfoStartTime"),
        ("CISCO-CUICAPPS-MIB", "cuicGeneralInfoTimeZoneName"),
        ("CISCO-CUICAPPS-MIB", "cuicGeneralInfoSystemStatus"),
        ("CISCO-CUICAPPS-MIB", "cuicGeneralInfoOpsConsoleURL"),
        ("CISCO-CUICAPPS-MIB", "cuicGeneralInfoEnableNotifications"))
)
if mibBuilder.loadTexts:
    cuicGeneralInfoTableGroup.setStatus("current")

cuicLicenseInfoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 2)
)
cuicLicenseInfoTableGroup.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicLicenseInfoType"),
        ("CISCO-CUICAPPS-MIB", "cuicLicenseInfoStartTime"),
        ("CISCO-CUICAPPS-MIB", "cuicLicenseInfoExpirationTime"),
        ("CISCO-CUICAPPS-MIB", "cuicLicenseInfoHost"))
)
if mibBuilder.loadTexts:
    cuicLicenseInfoTableGroup.setStatus("current")

cuicReportingTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 3)
)
cuicReportingTableGroup.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicReportingDataSourceCount"),
        ("CISCO-CUICAPPS-MIB", "cuicReportingEngineStatus"),
        ("CISCO-CUICAPPS-MIB", "cuicReportingHistoricalReportDefinitionCount"),
        ("CISCO-CUICAPPS-MIB", "cuicReportingRealTimeReportDefinitionCount"),
        ("CISCO-CUICAPPS-MIB", "cuicReportingHistoricalReportRunning"),
        ("CISCO-CUICAPPS-MIB", "cuicReportingHistoricalReportWaiting"),
        ("CISCO-CUICAPPS-MIB", "cuicReportingTotalKickedOffHistoricalReports"),
        ("CISCO-CUICAPPS-MIB", "cuicReportingRealTimeReportRunning"),
        ("CISCO-CUICAPPS-MIB", "cuicReportingTotalKickedOffRealTimeReports"),
        ("CISCO-CUICAPPS-MIB", "cuicReportingRealTimeReportWaiting"))
)
if mibBuilder.loadTexts:
    cuicReportingTableGroup.setStatus("current")

cuicReportSchedulerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 4)
)
cuicReportSchedulerTableGroup.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicSchedulerStatus"),
        ("CISCO-CUICAPPS-MIB", "cuicSchedulerEmailServerStatus"),
        ("CISCO-CUICAPPS-MIB", "cuicSchedulerJobsCompletedCount"),
        ("CISCO-CUICAPPS-MIB", "cuicSchedulerJobsRunningCount"),
        ("CISCO-CUICAPPS-MIB", "cuicSchedulerJobsFailedCount"))
)
if mibBuilder.loadTexts:
    cuicReportSchedulerTableGroup.setStatus("current")

cuicDbInfoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 5)
)
cuicDbInfoTableGroup.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicDbInfoStatus"),
        ("CISCO-CUICAPPS-MIB", "cuicDbInfoReplicationStatus"),
        ("CISCO-CUICAPPS-MIB", "cuicDbInfoTmpSpaceUsed"),
        ("CISCO-CUICAPPS-MIB", "cuicDbInfoSpaceUsed"))
)
if mibBuilder.loadTexts:
    cuicDbInfoTableGroup.setStatus("current")

cuicClusterInfoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 6)
)
cuicClusterInfoTableGroup.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicClusterName"),
        ("CISCO-CUICAPPS-MIB", "cuicClusterServerCount"),
        ("CISCO-CUICAPPS-MIB", "cuicClusterFirstNodeName"))
)
if mibBuilder.loadTexts:
    cuicClusterInfoTableGroup.setStatus("current")

cuicDatasourceInfoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 7)
)
cuicDatasourceInfoTableGroup.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicDatasourceName"),
        ("CISCO-CUICAPPS-MIB", "cuicDatasourceStatus"),
        ("CISCO-CUICAPPS-MIB", "cuicDatasourceHost"),
        ("CISCO-CUICAPPS-MIB", "cuicDatasourceType"))
)
if mibBuilder.loadTexts:
    cuicDatasourceInfoTableGroup.setStatus("current")

cuicSecurityTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 8)
)
cuicSecurityTableGroup.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicSecurityUsersConfigured"),
        ("CISCO-CUICAPPS-MIB", "cuicSecurityUsersLoggedIn"),
        ("CISCO-CUICAPPS-MIB", "cuicSecurityLoginFailedAttempts"),
        ("CISCO-CUICAPPS-MIB", "cuicSecurityGroupsConfigured"))
)
if mibBuilder.loadTexts:
    cuicSecurityTableGroup.setStatus("current")

cuicNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 9)
)
cuicNotificationInfoGroup.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicEventId"),
        ("CISCO-CUICAPPS-MIB", "cuicEventHostName"),
        ("CISCO-CUICAPPS-MIB", "cuicEventAppName"),
        ("CISCO-CUICAPPS-MIB", "cuicEventName"),
        ("CISCO-CUICAPPS-MIB", "cuicEventState"),
        ("CISCO-CUICAPPS-MIB", "cuicEventSeverity"),
        ("CISCO-CUICAPPS-MIB", "cuicEventTimestamp"),
        ("CISCO-CUICAPPS-MIB", "cuicEventText"))
)
if mibBuilder.loadTexts:
    cuicNotificationInfoGroup.setStatus("current")

cuicThreadPoolInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 11)
)
cuicThreadPoolInfoGroup.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicThreadsMaxAvailable"),
        ("CISCO-CUICAPPS-MIB", "cuicThreadsRunning"),
        ("CISCO-CUICAPPS-MIB", "cuicQueuedTasks"),
        ("CISCO-CUICAPPS-MIB", "cuicQueuedTasksMax"))
)
if mibBuilder.loadTexts:
    cuicThreadPoolInfoGroup.setStatus("current")

cuicEnvInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 12)
)
cuicEnvInfoGroup.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicWaErrors"),
        ("CISCO-CUICAPPS-MIB", "cuicWaSessionsActive"),
        ("CISCO-CUICAPPS-MIB", "cuicJvmPercentCPUTime"),
        ("CISCO-CUICAPPS-MIB", "cuicJvmMemoryFree"),
        ("CISCO-CUICAPPS-MIB", "cuicJvmMemoryTotal"),
        ("CISCO-CUICAPPS-MIB", "cuicJvmMemoryMax"),
        ("CISCO-CUICAPPS-MIB", "cuicTomcatThreadsBusy"),
        ("CISCO-CUICAPPS-MIB", "cuicTomcatThreadsTotal"),
        ("CISCO-CUICAPPS-MIB", "cuicTomcatThreadsMax"))
)
if mibBuilder.loadTexts:
    cuicEnvInfoGroup.setStatus("current")


# Notification objects

ciscoCuicappsMIBEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 0, 1)
)
ciscoCuicappsMIBEvent.setObjects(
      *(("CISCO-CUICAPPS-MIB", "cuicEventId"),
        ("CISCO-CUICAPPS-MIB", "cuicEventHostName"),
        ("CISCO-CUICAPPS-MIB", "cuicEventAppName"),
        ("CISCO-CUICAPPS-MIB", "cuicEventName"),
        ("CISCO-CUICAPPS-MIB", "cuicEventState"),
        ("CISCO-CUICAPPS-MIB", "cuicEventSeverity"),
        ("CISCO-CUICAPPS-MIB", "cuicEventTimestamp"),
        ("CISCO-CUICAPPS-MIB", "cuicEventText"))
)
if mibBuilder.loadTexts:
    ciscoCuicappsMIBEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoCuicappsMIBEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 2, 10)
)
ciscoCuicappsMIBEventGroup.setObjects(
    ("CISCO-CUICAPPS-MIB", "ciscoCuicappsMIBEvent")
)
if mibBuilder.loadTexts:
    ciscoCuicappsMIBEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCuicAppsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 718, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCuicAppsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CUICAPPS-MIB",
    **{"CuicServiceStatus": CuicServiceStatus,
       "CuicSubsystemId": CuicSubsystemId,
       "ciscoCuicappsMIB": ciscoCuicappsMIB,
       "ciscoCuicappsMIBNotifs": ciscoCuicappsMIBNotifs,
       "ciscoCuicappsMIBEvent": ciscoCuicappsMIBEvent,
       "ciscoCuicappsMIBObjects": ciscoCuicappsMIBObjects,
       "cuicGeneralInfoTable": cuicGeneralInfoTable,
       "cuicGeneralInfoEntry": cuicGeneralInfoEntry,
       "cuicGeneralInfoIndex": cuicGeneralInfoIndex,
       "cuicGeneralInfoServerName": cuicGeneralInfoServerName,
       "cuicGeneralInfoServerDescription": cuicGeneralInfoServerDescription,
       "cuicGeneralInfoVersion": cuicGeneralInfoVersion,
       "cuicGeneralInfoStartTime": cuicGeneralInfoStartTime,
       "cuicGeneralInfoTimeZoneName": cuicGeneralInfoTimeZoneName,
       "cuicGeneralInfoSystemStatus": cuicGeneralInfoSystemStatus,
       "cuicGeneralInfoOpsConsoleURL": cuicGeneralInfoOpsConsoleURL,
       "cuicGeneralInfoEnableNotifications": cuicGeneralInfoEnableNotifications,
       "cuicLicenseInfoTable": cuicLicenseInfoTable,
       "cuicLicenseInfoEntry": cuicLicenseInfoEntry,
       "cuicLicenseInfoIndex": cuicLicenseInfoIndex,
       "cuicLicenseInfoType": cuicLicenseInfoType,
       "cuicLicenseInfoStartTime": cuicLicenseInfoStartTime,
       "cuicLicenseInfoExpirationTime": cuicLicenseInfoExpirationTime,
       "cuicLicenseInfoHost": cuicLicenseInfoHost,
       "cuicReportingTable": cuicReportingTable,
       "cuicReportingEntry": cuicReportingEntry,
       "cuicReportingIndex": cuicReportingIndex,
       "cuicReportingDataSourceCount": cuicReportingDataSourceCount,
       "cuicReportingEngineStatus": cuicReportingEngineStatus,
       "cuicReportingHistoricalReportDefinitionCount": cuicReportingHistoricalReportDefinitionCount,
       "cuicReportingRealTimeReportDefinitionCount": cuicReportingRealTimeReportDefinitionCount,
       "cuicReportingHistoricalReportRunning": cuicReportingHistoricalReportRunning,
       "cuicReportingHistoricalReportWaiting": cuicReportingHistoricalReportWaiting,
       "cuicReportingTotalKickedOffHistoricalReports": cuicReportingTotalKickedOffHistoricalReports,
       "cuicReportingRealTimeReportRunning": cuicReportingRealTimeReportRunning,
       "cuicReportingTotalKickedOffRealTimeReports": cuicReportingTotalKickedOffRealTimeReports,
       "cuicReportingRealTimeReportWaiting": cuicReportingRealTimeReportWaiting,
       "cuicSchedulerTable": cuicSchedulerTable,
       "cuicSchedulerEntry": cuicSchedulerEntry,
       "cuicSchedulerIndex": cuicSchedulerIndex,
       "cuicSchedulerStatus": cuicSchedulerStatus,
       "cuicSchedulerEmailServerStatus": cuicSchedulerEmailServerStatus,
       "cuicSchedulerJobsCompletedCount": cuicSchedulerJobsCompletedCount,
       "cuicSchedulerJobsRunningCount": cuicSchedulerJobsRunningCount,
       "cuicSchedulerJobsFailedCount": cuicSchedulerJobsFailedCount,
       "cuicDbInfoTable": cuicDbInfoTable,
       "cuicDbInfoEntry": cuicDbInfoEntry,
       "cuicDbInfoIndex": cuicDbInfoIndex,
       "cuicDbInfoStatus": cuicDbInfoStatus,
       "cuicDbInfoReplicationStatus": cuicDbInfoReplicationStatus,
       "cuicDbInfoTmpSpaceUsed": cuicDbInfoTmpSpaceUsed,
       "cuicDbInfoSpaceUsed": cuicDbInfoSpaceUsed,
       "cuicClusterTable": cuicClusterTable,
       "cuicClusterEntry": cuicClusterEntry,
       "cuicClusterIndex": cuicClusterIndex,
       "cuicClusterName": cuicClusterName,
       "cuicClusterServerCount": cuicClusterServerCount,
       "cuicClusterFirstNodeName": cuicClusterFirstNodeName,
       "cuicDatasourceTable": cuicDatasourceTable,
       "cuicDatasourceEntry": cuicDatasourceEntry,
       "cuicDatasourceIndex": cuicDatasourceIndex,
       "cuicDatasourceName": cuicDatasourceName,
       "cuicDatasourceStatus": cuicDatasourceStatus,
       "cuicDatasourceHost": cuicDatasourceHost,
       "cuicDatasourceType": cuicDatasourceType,
       "cuicSecurityTable": cuicSecurityTable,
       "cuicSecurityEntry": cuicSecurityEntry,
       "cuicSecurityIndex": cuicSecurityIndex,
       "cuicSecurityUsersConfigured": cuicSecurityUsersConfigured,
       "cuicSecurityUsersLoggedIn": cuicSecurityUsersLoggedIn,
       "cuicSecurityLoginFailedAttempts": cuicSecurityLoginFailedAttempts,
       "cuicSecurityGroupsConfigured": cuicSecurityGroupsConfigured,
       "cuicThreadPoolInfo": cuicThreadPoolInfo,
       "cuicThreadsMaxAvailable": cuicThreadsMaxAvailable,
       "cuicThreadsRunning": cuicThreadsRunning,
       "cuicQueuedTasks": cuicQueuedTasks,
       "cuicQueuedTasksMax": cuicQueuedTasksMax,
       "cuicEnvInfo": cuicEnvInfo,
       "cuicWaErrors": cuicWaErrors,
       "cuicWaSessionsActive": cuicWaSessionsActive,
       "cuicJvmPercentCPUTime": cuicJvmPercentCPUTime,
       "cuicJvmMemoryFree": cuicJvmMemoryFree,
       "cuicJvmMemoryTotal": cuicJvmMemoryTotal,
       "cuicJvmMemoryMax": cuicJvmMemoryMax,
       "cuicTomcatThreadsBusy": cuicTomcatThreadsBusy,
       "cuicTomcatThreadsTotal": cuicTomcatThreadsTotal,
       "cuicTomcatThreadsMax": cuicTomcatThreadsMax,
       "cuicNotificationInfo": cuicNotificationInfo,
       "cuicEventId": cuicEventId,
       "cuicEventHostName": cuicEventHostName,
       "cuicEventAppName": cuicEventAppName,
       "cuicEventName": cuicEventName,
       "cuicEventState": cuicEventState,
       "cuicEventSeverity": cuicEventSeverity,
       "cuicEventTimestamp": cuicEventTimestamp,
       "cuicEventText": cuicEventText,
       "ciscoCuicappsMIBConform": ciscoCuicappsMIBConform,
       "ciscoCuicappsMIBCompliances": ciscoCuicappsMIBCompliances,
       "ciscoCuicAppsMIBCompliance": ciscoCuicAppsMIBCompliance,
       "ciscoCuicappsMIBGroups": ciscoCuicappsMIBGroups,
       "cuicGeneralInfoTableGroup": cuicGeneralInfoTableGroup,
       "cuicLicenseInfoTableGroup": cuicLicenseInfoTableGroup,
       "cuicReportingTableGroup": cuicReportingTableGroup,
       "cuicReportSchedulerTableGroup": cuicReportSchedulerTableGroup,
       "cuicDbInfoTableGroup": cuicDbInfoTableGroup,
       "cuicClusterInfoTableGroup": cuicClusterInfoTableGroup,
       "cuicDatasourceInfoTableGroup": cuicDatasourceInfoTableGroup,
       "cuicSecurityTableGroup": cuicSecurityTableGroup,
       "cuicNotificationInfoGroup": cuicNotificationInfoGroup,
       "ciscoCuicappsMIBEventGroup": ciscoCuicappsMIBEventGroup,
       "cuicThreadPoolInfoGroup": cuicThreadPoolInfoGroup,
       "cuicEnvInfoGroup": cuicEnvInfoGroup}
)

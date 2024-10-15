# SNMP MIB module (CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:14 2024
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

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsEquipmentOperability,
 CucsEquipmentPowerState,
 CucsEquipmentPresence,
 CucsEquipmentSensorThresholdStatus,
 CucsMemoryVisibility,
 CucsProcessorEnvStatsHistThresholded,
 CucsProcessorEnvStatsThresholded,
 CucsProcessorErrorStatsThresholded,
 CucsProcessorQualArch,
 CucsProcessorRuntimeHistThresholded,
 CucsProcessorRuntimeThresholded,
 CucsProcessorUnitArch) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsEquipmentOperability",
    "CucsEquipmentPowerState",
    "CucsEquipmentPresence",
    "CucsEquipmentSensorThresholdStatus",
    "CucsMemoryVisibility",
    "CucsProcessorEnvStatsHistThresholded",
    "CucsProcessorEnvStatsThresholded",
    "CucsProcessorErrorStatsThresholded",
    "CucsProcessorQualArch",
    "CucsProcessorRuntimeHistThresholded",
    "CucsProcessorRuntimeThresholded",
    "CucsProcessorUnitArch")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 MacAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsProcessorObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsProcessorCoreTable_Object = MibTable
cucsProcessorCoreTable = _CucsProcessorCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 1)
)
if mibBuilder.loadTexts:
    cucsProcessorCoreTable.setStatus("current")
_CucsProcessorCoreEntry_Object = MibTableRow
cucsProcessorCoreEntry = _CucsProcessorCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 1, 1)
)
cucsProcessorCoreEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB", "cucsProcessorCoreInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcessorCoreEntry.setStatus("current")
_CucsProcessorCoreInstanceId_Type = CucsManagedObjectId
_CucsProcessorCoreInstanceId_Object = MibTableColumn
cucsProcessorCoreInstanceId = _CucsProcessorCoreInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 1, 1, 1),
    _CucsProcessorCoreInstanceId_Type()
)
cucsProcessorCoreInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcessorCoreInstanceId.setStatus("current")
_CucsProcessorCoreDn_Type = CucsManagedObjectDn
_CucsProcessorCoreDn_Object = MibTableColumn
cucsProcessorCoreDn = _CucsProcessorCoreDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 1, 1, 2),
    _CucsProcessorCoreDn_Type()
)
cucsProcessorCoreDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorCoreDn.setStatus("current")
_CucsProcessorCoreRn_Type = SnmpAdminString
_CucsProcessorCoreRn_Object = MibTableColumn
cucsProcessorCoreRn = _CucsProcessorCoreRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 1, 1, 3),
    _CucsProcessorCoreRn_Type()
)
cucsProcessorCoreRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorCoreRn.setStatus("current")
_CucsProcessorCoreId_Type = Gauge32
_CucsProcessorCoreId_Object = MibTableColumn
cucsProcessorCoreId = _CucsProcessorCoreId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 1, 1, 4),
    _CucsProcessorCoreId_Type()
)
cucsProcessorCoreId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorCoreId.setStatus("current")
_CucsProcessorEnvStatsTable_Object = MibTable
cucsProcessorEnvStatsTable = _CucsProcessorEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2)
)
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsTable.setStatus("current")
_CucsProcessorEnvStatsEntry_Object = MibTableRow
cucsProcessorEnvStatsEntry = _CucsProcessorEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1)
)
cucsProcessorEnvStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB", "cucsProcessorEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsEntry.setStatus("current")
_CucsProcessorEnvStatsInstanceId_Type = CucsManagedObjectId
_CucsProcessorEnvStatsInstanceId_Object = MibTableColumn
cucsProcessorEnvStatsInstanceId = _CucsProcessorEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 1),
    _CucsProcessorEnvStatsInstanceId_Type()
)
cucsProcessorEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsInstanceId.setStatus("current")
_CucsProcessorEnvStatsDn_Type = CucsManagedObjectDn
_CucsProcessorEnvStatsDn_Object = MibTableColumn
cucsProcessorEnvStatsDn = _CucsProcessorEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 2),
    _CucsProcessorEnvStatsDn_Type()
)
cucsProcessorEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsDn.setStatus("current")
_CucsProcessorEnvStatsRn_Type = SnmpAdminString
_CucsProcessorEnvStatsRn_Object = MibTableColumn
cucsProcessorEnvStatsRn = _CucsProcessorEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 3),
    _CucsProcessorEnvStatsRn_Type()
)
cucsProcessorEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsRn.setStatus("current")
_CucsProcessorEnvStatsInputCurrent_Type = Integer32
_CucsProcessorEnvStatsInputCurrent_Object = MibTableColumn
cucsProcessorEnvStatsInputCurrent = _CucsProcessorEnvStatsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 4),
    _CucsProcessorEnvStatsInputCurrent_Type()
)
cucsProcessorEnvStatsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsInputCurrent.setStatus("current")
_CucsProcessorEnvStatsInputCurrentAvg_Type = Integer32
_CucsProcessorEnvStatsInputCurrentAvg_Object = MibTableColumn
cucsProcessorEnvStatsInputCurrentAvg = _CucsProcessorEnvStatsInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 5),
    _CucsProcessorEnvStatsInputCurrentAvg_Type()
)
cucsProcessorEnvStatsInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsInputCurrentAvg.setStatus("current")
_CucsProcessorEnvStatsInputCurrentMax_Type = Integer32
_CucsProcessorEnvStatsInputCurrentMax_Object = MibTableColumn
cucsProcessorEnvStatsInputCurrentMax = _CucsProcessorEnvStatsInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 6),
    _CucsProcessorEnvStatsInputCurrentMax_Type()
)
cucsProcessorEnvStatsInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsInputCurrentMax.setStatus("current")
_CucsProcessorEnvStatsInputCurrentMin_Type = Integer32
_CucsProcessorEnvStatsInputCurrentMin_Object = MibTableColumn
cucsProcessorEnvStatsInputCurrentMin = _CucsProcessorEnvStatsInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 7),
    _CucsProcessorEnvStatsInputCurrentMin_Type()
)
cucsProcessorEnvStatsInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsInputCurrentMin.setStatus("current")
_CucsProcessorEnvStatsIntervals_Type = Gauge32
_CucsProcessorEnvStatsIntervals_Object = MibTableColumn
cucsProcessorEnvStatsIntervals = _CucsProcessorEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 8),
    _CucsProcessorEnvStatsIntervals_Type()
)
cucsProcessorEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsIntervals.setStatus("current")
_CucsProcessorEnvStatsSuspect_Type = TruthValue
_CucsProcessorEnvStatsSuspect_Object = MibTableColumn
cucsProcessorEnvStatsSuspect = _CucsProcessorEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 9),
    _CucsProcessorEnvStatsSuspect_Type()
)
cucsProcessorEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsSuspect.setStatus("current")
_CucsProcessorEnvStatsTemperature_Type = Integer32
_CucsProcessorEnvStatsTemperature_Object = MibTableColumn
cucsProcessorEnvStatsTemperature = _CucsProcessorEnvStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 10),
    _CucsProcessorEnvStatsTemperature_Type()
)
cucsProcessorEnvStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsTemperature.setStatus("current")
_CucsProcessorEnvStatsTemperatureAvg_Type = Integer32
_CucsProcessorEnvStatsTemperatureAvg_Object = MibTableColumn
cucsProcessorEnvStatsTemperatureAvg = _CucsProcessorEnvStatsTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 11),
    _CucsProcessorEnvStatsTemperatureAvg_Type()
)
cucsProcessorEnvStatsTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsTemperatureAvg.setStatus("current")
_CucsProcessorEnvStatsTemperatureMax_Type = Integer32
_CucsProcessorEnvStatsTemperatureMax_Object = MibTableColumn
cucsProcessorEnvStatsTemperatureMax = _CucsProcessorEnvStatsTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 12),
    _CucsProcessorEnvStatsTemperatureMax_Type()
)
cucsProcessorEnvStatsTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsTemperatureMax.setStatus("current")
_CucsProcessorEnvStatsTemperatureMin_Type = Integer32
_CucsProcessorEnvStatsTemperatureMin_Object = MibTableColumn
cucsProcessorEnvStatsTemperatureMin = _CucsProcessorEnvStatsTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 13),
    _CucsProcessorEnvStatsTemperatureMin_Type()
)
cucsProcessorEnvStatsTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsTemperatureMin.setStatus("current")
_CucsProcessorEnvStatsThresholded_Type = CucsProcessorEnvStatsThresholded
_CucsProcessorEnvStatsThresholded_Object = MibTableColumn
cucsProcessorEnvStatsThresholded = _CucsProcessorEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 14),
    _CucsProcessorEnvStatsThresholded_Type()
)
cucsProcessorEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsThresholded.setStatus("current")
_CucsProcessorEnvStatsTimeCollected_Type = DateAndTime
_CucsProcessorEnvStatsTimeCollected_Object = MibTableColumn
cucsProcessorEnvStatsTimeCollected = _CucsProcessorEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 15),
    _CucsProcessorEnvStatsTimeCollected_Type()
)
cucsProcessorEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsTimeCollected.setStatus("current")
_CucsProcessorEnvStatsUpdate_Type = Gauge32
_CucsProcessorEnvStatsUpdate_Object = MibTableColumn
cucsProcessorEnvStatsUpdate = _CucsProcessorEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 2, 1, 16),
    _CucsProcessorEnvStatsUpdate_Type()
)
cucsProcessorEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsUpdate.setStatus("current")
_CucsProcessorEnvStatsHistTable_Object = MibTable
cucsProcessorEnvStatsHistTable = _CucsProcessorEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3)
)
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistTable.setStatus("current")
_CucsProcessorEnvStatsHistEntry_Object = MibTableRow
cucsProcessorEnvStatsHistEntry = _CucsProcessorEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1)
)
cucsProcessorEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB", "cucsProcessorEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistEntry.setStatus("current")
_CucsProcessorEnvStatsHistInstanceId_Type = CucsManagedObjectId
_CucsProcessorEnvStatsHistInstanceId_Object = MibTableColumn
cucsProcessorEnvStatsHistInstanceId = _CucsProcessorEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 1),
    _CucsProcessorEnvStatsHistInstanceId_Type()
)
cucsProcessorEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistInstanceId.setStatus("current")
_CucsProcessorEnvStatsHistDn_Type = CucsManagedObjectDn
_CucsProcessorEnvStatsHistDn_Object = MibTableColumn
cucsProcessorEnvStatsHistDn = _CucsProcessorEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 2),
    _CucsProcessorEnvStatsHistDn_Type()
)
cucsProcessorEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistDn.setStatus("current")
_CucsProcessorEnvStatsHistRn_Type = SnmpAdminString
_CucsProcessorEnvStatsHistRn_Object = MibTableColumn
cucsProcessorEnvStatsHistRn = _CucsProcessorEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 3),
    _CucsProcessorEnvStatsHistRn_Type()
)
cucsProcessorEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistRn.setStatus("current")
_CucsProcessorEnvStatsHistId_Type = Unsigned64
_CucsProcessorEnvStatsHistId_Object = MibTableColumn
cucsProcessorEnvStatsHistId = _CucsProcessorEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 4),
    _CucsProcessorEnvStatsHistId_Type()
)
cucsProcessorEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistId.setStatus("current")
_CucsProcessorEnvStatsHistInputCurrent_Type = Integer32
_CucsProcessorEnvStatsHistInputCurrent_Object = MibTableColumn
cucsProcessorEnvStatsHistInputCurrent = _CucsProcessorEnvStatsHistInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 5),
    _CucsProcessorEnvStatsHistInputCurrent_Type()
)
cucsProcessorEnvStatsHistInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistInputCurrent.setStatus("current")
_CucsProcessorEnvStatsHistInputCurrentAvg_Type = Integer32
_CucsProcessorEnvStatsHistInputCurrentAvg_Object = MibTableColumn
cucsProcessorEnvStatsHistInputCurrentAvg = _CucsProcessorEnvStatsHistInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 6),
    _CucsProcessorEnvStatsHistInputCurrentAvg_Type()
)
cucsProcessorEnvStatsHistInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistInputCurrentAvg.setStatus("current")
_CucsProcessorEnvStatsHistInputCurrentMax_Type = Integer32
_CucsProcessorEnvStatsHistInputCurrentMax_Object = MibTableColumn
cucsProcessorEnvStatsHistInputCurrentMax = _CucsProcessorEnvStatsHistInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 7),
    _CucsProcessorEnvStatsHistInputCurrentMax_Type()
)
cucsProcessorEnvStatsHistInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistInputCurrentMax.setStatus("current")
_CucsProcessorEnvStatsHistInputCurrentMin_Type = Integer32
_CucsProcessorEnvStatsHistInputCurrentMin_Object = MibTableColumn
cucsProcessorEnvStatsHistInputCurrentMin = _CucsProcessorEnvStatsHistInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 8),
    _CucsProcessorEnvStatsHistInputCurrentMin_Type()
)
cucsProcessorEnvStatsHistInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistInputCurrentMin.setStatus("current")
_CucsProcessorEnvStatsHistMostRecent_Type = TruthValue
_CucsProcessorEnvStatsHistMostRecent_Object = MibTableColumn
cucsProcessorEnvStatsHistMostRecent = _CucsProcessorEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 9),
    _CucsProcessorEnvStatsHistMostRecent_Type()
)
cucsProcessorEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistMostRecent.setStatus("current")
_CucsProcessorEnvStatsHistSuspect_Type = TruthValue
_CucsProcessorEnvStatsHistSuspect_Object = MibTableColumn
cucsProcessorEnvStatsHistSuspect = _CucsProcessorEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 10),
    _CucsProcessorEnvStatsHistSuspect_Type()
)
cucsProcessorEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistSuspect.setStatus("current")
_CucsProcessorEnvStatsHistTemperature_Type = Integer32
_CucsProcessorEnvStatsHistTemperature_Object = MibTableColumn
cucsProcessorEnvStatsHistTemperature = _CucsProcessorEnvStatsHistTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 11),
    _CucsProcessorEnvStatsHistTemperature_Type()
)
cucsProcessorEnvStatsHistTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistTemperature.setStatus("current")
_CucsProcessorEnvStatsHistTemperatureAvg_Type = Integer32
_CucsProcessorEnvStatsHistTemperatureAvg_Object = MibTableColumn
cucsProcessorEnvStatsHistTemperatureAvg = _CucsProcessorEnvStatsHistTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 12),
    _CucsProcessorEnvStatsHistTemperatureAvg_Type()
)
cucsProcessorEnvStatsHistTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistTemperatureAvg.setStatus("current")
_CucsProcessorEnvStatsHistTemperatureMax_Type = Integer32
_CucsProcessorEnvStatsHistTemperatureMax_Object = MibTableColumn
cucsProcessorEnvStatsHistTemperatureMax = _CucsProcessorEnvStatsHistTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 13),
    _CucsProcessorEnvStatsHistTemperatureMax_Type()
)
cucsProcessorEnvStatsHistTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistTemperatureMax.setStatus("current")
_CucsProcessorEnvStatsHistTemperatureMin_Type = Integer32
_CucsProcessorEnvStatsHistTemperatureMin_Object = MibTableColumn
cucsProcessorEnvStatsHistTemperatureMin = _CucsProcessorEnvStatsHistTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 14),
    _CucsProcessorEnvStatsHistTemperatureMin_Type()
)
cucsProcessorEnvStatsHistTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistTemperatureMin.setStatus("current")
_CucsProcessorEnvStatsHistThresholded_Type = CucsProcessorEnvStatsHistThresholded
_CucsProcessorEnvStatsHistThresholded_Object = MibTableColumn
cucsProcessorEnvStatsHistThresholded = _CucsProcessorEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 15),
    _CucsProcessorEnvStatsHistThresholded_Type()
)
cucsProcessorEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistThresholded.setStatus("current")
_CucsProcessorEnvStatsHistTimeCollected_Type = DateAndTime
_CucsProcessorEnvStatsHistTimeCollected_Object = MibTableColumn
cucsProcessorEnvStatsHistTimeCollected = _CucsProcessorEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 3, 1, 16),
    _CucsProcessorEnvStatsHistTimeCollected_Type()
)
cucsProcessorEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorEnvStatsHistTimeCollected.setStatus("current")
_CucsProcessorErrorStatsTable_Object = MibTable
cucsProcessorErrorStatsTable = _CucsProcessorErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4)
)
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsTable.setStatus("current")
_CucsProcessorErrorStatsEntry_Object = MibTableRow
cucsProcessorErrorStatsEntry = _CucsProcessorErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1)
)
cucsProcessorErrorStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB", "cucsProcessorErrorStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsEntry.setStatus("current")
_CucsProcessorErrorStatsInstanceId_Type = CucsManagedObjectId
_CucsProcessorErrorStatsInstanceId_Object = MibTableColumn
cucsProcessorErrorStatsInstanceId = _CucsProcessorErrorStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 1),
    _CucsProcessorErrorStatsInstanceId_Type()
)
cucsProcessorErrorStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsInstanceId.setStatus("current")
_CucsProcessorErrorStatsDn_Type = CucsManagedObjectDn
_CucsProcessorErrorStatsDn_Object = MibTableColumn
cucsProcessorErrorStatsDn = _CucsProcessorErrorStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 2),
    _CucsProcessorErrorStatsDn_Type()
)
cucsProcessorErrorStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsDn.setStatus("current")
_CucsProcessorErrorStatsRn_Type = SnmpAdminString
_CucsProcessorErrorStatsRn_Object = MibTableColumn
cucsProcessorErrorStatsRn = _CucsProcessorErrorStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 3),
    _CucsProcessorErrorStatsRn_Type()
)
cucsProcessorErrorStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsRn.setStatus("current")
_CucsProcessorErrorStatsIntervals_Type = Gauge32
_CucsProcessorErrorStatsIntervals_Object = MibTableColumn
cucsProcessorErrorStatsIntervals = _CucsProcessorErrorStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 4),
    _CucsProcessorErrorStatsIntervals_Type()
)
cucsProcessorErrorStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsIntervals.setStatus("current")
_CucsProcessorErrorStatsMirroringInterSockErrors_Type = Counter32
_CucsProcessorErrorStatsMirroringInterSockErrors_Object = MibTableColumn
cucsProcessorErrorStatsMirroringInterSockErrors = _CucsProcessorErrorStatsMirroringInterSockErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 5),
    _CucsProcessorErrorStatsMirroringInterSockErrors_Type()
)
cucsProcessorErrorStatsMirroringInterSockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringInterSockErrors.setStatus("current")
_CucsProcessorErrorStatsMirroringInterSockErrors15Min_Type = Gauge32
_CucsProcessorErrorStatsMirroringInterSockErrors15Min_Object = MibTableColumn
cucsProcessorErrorStatsMirroringInterSockErrors15Min = _CucsProcessorErrorStatsMirroringInterSockErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 6),
    _CucsProcessorErrorStatsMirroringInterSockErrors15Min_Type()
)
cucsProcessorErrorStatsMirroringInterSockErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringInterSockErrors15Min.setStatus("current")
_CucsProcessorErrorStatsMirroringInterSockErrors15MinH_Type = Gauge32
_CucsProcessorErrorStatsMirroringInterSockErrors15MinH_Object = MibTableColumn
cucsProcessorErrorStatsMirroringInterSockErrors15MinH = _CucsProcessorErrorStatsMirroringInterSockErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 7),
    _CucsProcessorErrorStatsMirroringInterSockErrors15MinH_Type()
)
cucsProcessorErrorStatsMirroringInterSockErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringInterSockErrors15MinH.setStatus("current")
_CucsProcessorErrorStatsMirroringInterSockErrors1Day_Type = Gauge32
_CucsProcessorErrorStatsMirroringInterSockErrors1Day_Object = MibTableColumn
cucsProcessorErrorStatsMirroringInterSockErrors1Day = _CucsProcessorErrorStatsMirroringInterSockErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 8),
    _CucsProcessorErrorStatsMirroringInterSockErrors1Day_Type()
)
cucsProcessorErrorStatsMirroringInterSockErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringInterSockErrors1Day.setStatus("current")
_CucsProcessorErrorStatsMirroringInterSockErrors1DayH_Type = Gauge32
_CucsProcessorErrorStatsMirroringInterSockErrors1DayH_Object = MibTableColumn
cucsProcessorErrorStatsMirroringInterSockErrors1DayH = _CucsProcessorErrorStatsMirroringInterSockErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 9),
    _CucsProcessorErrorStatsMirroringInterSockErrors1DayH_Type()
)
cucsProcessorErrorStatsMirroringInterSockErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringInterSockErrors1DayH.setStatus("current")
_CucsProcessorErrorStatsMirroringInterSockErrors1Hour_Type = Gauge32
_CucsProcessorErrorStatsMirroringInterSockErrors1Hour_Object = MibTableColumn
cucsProcessorErrorStatsMirroringInterSockErrors1Hour = _CucsProcessorErrorStatsMirroringInterSockErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 10),
    _CucsProcessorErrorStatsMirroringInterSockErrors1Hour_Type()
)
cucsProcessorErrorStatsMirroringInterSockErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringInterSockErrors1Hour.setStatus("current")
_CucsProcessorErrorStatsMirroringInterSockErrors1HourH_Type = Gauge32
_CucsProcessorErrorStatsMirroringInterSockErrors1HourH_Object = MibTableColumn
cucsProcessorErrorStatsMirroringInterSockErrors1HourH = _CucsProcessorErrorStatsMirroringInterSockErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 11),
    _CucsProcessorErrorStatsMirroringInterSockErrors1HourH_Type()
)
cucsProcessorErrorStatsMirroringInterSockErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringInterSockErrors1HourH.setStatus("current")
_CucsProcessorErrorStatsMirroringInterSockErrors1Week_Type = Gauge32
_CucsProcessorErrorStatsMirroringInterSockErrors1Week_Object = MibTableColumn
cucsProcessorErrorStatsMirroringInterSockErrors1Week = _CucsProcessorErrorStatsMirroringInterSockErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 12),
    _CucsProcessorErrorStatsMirroringInterSockErrors1Week_Type()
)
cucsProcessorErrorStatsMirroringInterSockErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringInterSockErrors1Week.setStatus("current")
_CucsProcessorErrorStatsMirroringInterSockErrors1WeekH_Type = Gauge32
_CucsProcessorErrorStatsMirroringInterSockErrors1WeekH_Object = MibTableColumn
cucsProcessorErrorStatsMirroringInterSockErrors1WeekH = _CucsProcessorErrorStatsMirroringInterSockErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 13),
    _CucsProcessorErrorStatsMirroringInterSockErrors1WeekH_Type()
)
cucsProcessorErrorStatsMirroringInterSockErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringInterSockErrors1WeekH.setStatus("current")
_CucsProcessorErrorStatsMirroringIntraSockErrors_Type = Counter32
_CucsProcessorErrorStatsMirroringIntraSockErrors_Object = MibTableColumn
cucsProcessorErrorStatsMirroringIntraSockErrors = _CucsProcessorErrorStatsMirroringIntraSockErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 14),
    _CucsProcessorErrorStatsMirroringIntraSockErrors_Type()
)
cucsProcessorErrorStatsMirroringIntraSockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringIntraSockErrors.setStatus("current")
_CucsProcessorErrorStatsMirroringIntraSockErrors15Min_Type = Gauge32
_CucsProcessorErrorStatsMirroringIntraSockErrors15Min_Object = MibTableColumn
cucsProcessorErrorStatsMirroringIntraSockErrors15Min = _CucsProcessorErrorStatsMirroringIntraSockErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 15),
    _CucsProcessorErrorStatsMirroringIntraSockErrors15Min_Type()
)
cucsProcessorErrorStatsMirroringIntraSockErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringIntraSockErrors15Min.setStatus("current")
_CucsProcessorErrorStatsMirroringIntraSockErrors15MinH_Type = Gauge32
_CucsProcessorErrorStatsMirroringIntraSockErrors15MinH_Object = MibTableColumn
cucsProcessorErrorStatsMirroringIntraSockErrors15MinH = _CucsProcessorErrorStatsMirroringIntraSockErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 16),
    _CucsProcessorErrorStatsMirroringIntraSockErrors15MinH_Type()
)
cucsProcessorErrorStatsMirroringIntraSockErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringIntraSockErrors15MinH.setStatus("current")
_CucsProcessorErrorStatsMirroringIntraSockErrors1Day_Type = Gauge32
_CucsProcessorErrorStatsMirroringIntraSockErrors1Day_Object = MibTableColumn
cucsProcessorErrorStatsMirroringIntraSockErrors1Day = _CucsProcessorErrorStatsMirroringIntraSockErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 17),
    _CucsProcessorErrorStatsMirroringIntraSockErrors1Day_Type()
)
cucsProcessorErrorStatsMirroringIntraSockErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringIntraSockErrors1Day.setStatus("current")
_CucsProcessorErrorStatsMirroringIntraSockErrors1DayH_Type = Gauge32
_CucsProcessorErrorStatsMirroringIntraSockErrors1DayH_Object = MibTableColumn
cucsProcessorErrorStatsMirroringIntraSockErrors1DayH = _CucsProcessorErrorStatsMirroringIntraSockErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 18),
    _CucsProcessorErrorStatsMirroringIntraSockErrors1DayH_Type()
)
cucsProcessorErrorStatsMirroringIntraSockErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringIntraSockErrors1DayH.setStatus("current")
_CucsProcessorErrorStatsMirroringIntraSockErrors1Hour_Type = Gauge32
_CucsProcessorErrorStatsMirroringIntraSockErrors1Hour_Object = MibTableColumn
cucsProcessorErrorStatsMirroringIntraSockErrors1Hour = _CucsProcessorErrorStatsMirroringIntraSockErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 19),
    _CucsProcessorErrorStatsMirroringIntraSockErrors1Hour_Type()
)
cucsProcessorErrorStatsMirroringIntraSockErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringIntraSockErrors1Hour.setStatus("current")
_CucsProcessorErrorStatsMirroringIntraSockErrors1HourH_Type = Gauge32
_CucsProcessorErrorStatsMirroringIntraSockErrors1HourH_Object = MibTableColumn
cucsProcessorErrorStatsMirroringIntraSockErrors1HourH = _CucsProcessorErrorStatsMirroringIntraSockErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 20),
    _CucsProcessorErrorStatsMirroringIntraSockErrors1HourH_Type()
)
cucsProcessorErrorStatsMirroringIntraSockErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringIntraSockErrors1HourH.setStatus("current")
_CucsProcessorErrorStatsMirroringIntraSockErrors1Week_Type = Gauge32
_CucsProcessorErrorStatsMirroringIntraSockErrors1Week_Object = MibTableColumn
cucsProcessorErrorStatsMirroringIntraSockErrors1Week = _CucsProcessorErrorStatsMirroringIntraSockErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 21),
    _CucsProcessorErrorStatsMirroringIntraSockErrors1Week_Type()
)
cucsProcessorErrorStatsMirroringIntraSockErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringIntraSockErrors1Week.setStatus("current")
_CucsProcessorErrorStatsMirroringIntraSockErrors1WeekH_Type = Gauge32
_CucsProcessorErrorStatsMirroringIntraSockErrors1WeekH_Object = MibTableColumn
cucsProcessorErrorStatsMirroringIntraSockErrors1WeekH = _CucsProcessorErrorStatsMirroringIntraSockErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 22),
    _CucsProcessorErrorStatsMirroringIntraSockErrors1WeekH_Type()
)
cucsProcessorErrorStatsMirroringIntraSockErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringIntraSockErrors1WeekH.setStatus("current")
_CucsProcessorErrorStatsSmiLinkCorrErrors_Type = Counter32
_CucsProcessorErrorStatsSmiLinkCorrErrors_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkCorrErrors = _CucsProcessorErrorStatsSmiLinkCorrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 23),
    _CucsProcessorErrorStatsSmiLinkCorrErrors_Type()
)
cucsProcessorErrorStatsSmiLinkCorrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkCorrErrors.setStatus("current")
_CucsProcessorErrorStatsSmiLinkCorrErrors15Min_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkCorrErrors15Min_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkCorrErrors15Min = _CucsProcessorErrorStatsSmiLinkCorrErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 24),
    _CucsProcessorErrorStatsSmiLinkCorrErrors15Min_Type()
)
cucsProcessorErrorStatsSmiLinkCorrErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkCorrErrors15Min.setStatus("current")
_CucsProcessorErrorStatsSmiLinkCorrErrors15MinH_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkCorrErrors15MinH_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkCorrErrors15MinH = _CucsProcessorErrorStatsSmiLinkCorrErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 25),
    _CucsProcessorErrorStatsSmiLinkCorrErrors15MinH_Type()
)
cucsProcessorErrorStatsSmiLinkCorrErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkCorrErrors15MinH.setStatus("current")
_CucsProcessorErrorStatsSmiLinkCorrErrors1Day_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkCorrErrors1Day_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkCorrErrors1Day = _CucsProcessorErrorStatsSmiLinkCorrErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 26),
    _CucsProcessorErrorStatsSmiLinkCorrErrors1Day_Type()
)
cucsProcessorErrorStatsSmiLinkCorrErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkCorrErrors1Day.setStatus("current")
_CucsProcessorErrorStatsSmiLinkCorrErrors1DayH_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkCorrErrors1DayH_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkCorrErrors1DayH = _CucsProcessorErrorStatsSmiLinkCorrErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 27),
    _CucsProcessorErrorStatsSmiLinkCorrErrors1DayH_Type()
)
cucsProcessorErrorStatsSmiLinkCorrErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkCorrErrors1DayH.setStatus("current")
_CucsProcessorErrorStatsSmiLinkCorrErrors1Hour_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkCorrErrors1Hour_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkCorrErrors1Hour = _CucsProcessorErrorStatsSmiLinkCorrErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 28),
    _CucsProcessorErrorStatsSmiLinkCorrErrors1Hour_Type()
)
cucsProcessorErrorStatsSmiLinkCorrErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkCorrErrors1Hour.setStatus("current")
_CucsProcessorErrorStatsSmiLinkCorrErrors1HourH_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkCorrErrors1HourH_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkCorrErrors1HourH = _CucsProcessorErrorStatsSmiLinkCorrErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 29),
    _CucsProcessorErrorStatsSmiLinkCorrErrors1HourH_Type()
)
cucsProcessorErrorStatsSmiLinkCorrErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkCorrErrors1HourH.setStatus("current")
_CucsProcessorErrorStatsSmiLinkCorrErrors1Week_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkCorrErrors1Week_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkCorrErrors1Week = _CucsProcessorErrorStatsSmiLinkCorrErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 30),
    _CucsProcessorErrorStatsSmiLinkCorrErrors1Week_Type()
)
cucsProcessorErrorStatsSmiLinkCorrErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkCorrErrors1Week.setStatus("current")
_CucsProcessorErrorStatsSmiLinkCorrErrors1WeekH_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkCorrErrors1WeekH_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkCorrErrors1WeekH = _CucsProcessorErrorStatsSmiLinkCorrErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 31),
    _CucsProcessorErrorStatsSmiLinkCorrErrors1WeekH_Type()
)
cucsProcessorErrorStatsSmiLinkCorrErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkCorrErrors1WeekH.setStatus("current")
_CucsProcessorErrorStatsSmiLinkUncorrErrors_Type = Counter32
_CucsProcessorErrorStatsSmiLinkUncorrErrors_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkUncorrErrors = _CucsProcessorErrorStatsSmiLinkUncorrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 32),
    _CucsProcessorErrorStatsSmiLinkUncorrErrors_Type()
)
cucsProcessorErrorStatsSmiLinkUncorrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkUncorrErrors.setStatus("current")
_CucsProcessorErrorStatsSmiLinkUncorrErrors15Min_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkUncorrErrors15Min_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkUncorrErrors15Min = _CucsProcessorErrorStatsSmiLinkUncorrErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 33),
    _CucsProcessorErrorStatsSmiLinkUncorrErrors15Min_Type()
)
cucsProcessorErrorStatsSmiLinkUncorrErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkUncorrErrors15Min.setStatus("current")
_CucsProcessorErrorStatsSmiLinkUncorrErrors15MinH_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkUncorrErrors15MinH_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkUncorrErrors15MinH = _CucsProcessorErrorStatsSmiLinkUncorrErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 34),
    _CucsProcessorErrorStatsSmiLinkUncorrErrors15MinH_Type()
)
cucsProcessorErrorStatsSmiLinkUncorrErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkUncorrErrors15MinH.setStatus("current")
_CucsProcessorErrorStatsSmiLinkUncorrErrors1Day_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkUncorrErrors1Day_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkUncorrErrors1Day = _CucsProcessorErrorStatsSmiLinkUncorrErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 35),
    _CucsProcessorErrorStatsSmiLinkUncorrErrors1Day_Type()
)
cucsProcessorErrorStatsSmiLinkUncorrErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkUncorrErrors1Day.setStatus("current")
_CucsProcessorErrorStatsSmiLinkUncorrErrors1DayH_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkUncorrErrors1DayH_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkUncorrErrors1DayH = _CucsProcessorErrorStatsSmiLinkUncorrErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 36),
    _CucsProcessorErrorStatsSmiLinkUncorrErrors1DayH_Type()
)
cucsProcessorErrorStatsSmiLinkUncorrErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkUncorrErrors1DayH.setStatus("current")
_CucsProcessorErrorStatsSmiLinkUncorrErrors1Hour_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkUncorrErrors1Hour_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkUncorrErrors1Hour = _CucsProcessorErrorStatsSmiLinkUncorrErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 37),
    _CucsProcessorErrorStatsSmiLinkUncorrErrors1Hour_Type()
)
cucsProcessorErrorStatsSmiLinkUncorrErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkUncorrErrors1Hour.setStatus("current")
_CucsProcessorErrorStatsSmiLinkUncorrErrors1HourH_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkUncorrErrors1HourH_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkUncorrErrors1HourH = _CucsProcessorErrorStatsSmiLinkUncorrErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 38),
    _CucsProcessorErrorStatsSmiLinkUncorrErrors1HourH_Type()
)
cucsProcessorErrorStatsSmiLinkUncorrErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkUncorrErrors1HourH.setStatus("current")
_CucsProcessorErrorStatsSmiLinkUncorrErrors1Week_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkUncorrErrors1Week_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkUncorrErrors1Week = _CucsProcessorErrorStatsSmiLinkUncorrErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 39),
    _CucsProcessorErrorStatsSmiLinkUncorrErrors1Week_Type()
)
cucsProcessorErrorStatsSmiLinkUncorrErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkUncorrErrors1Week.setStatus("current")
_CucsProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkUncorrErrors1WeekH = _CucsProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 40),
    _CucsProcessorErrorStatsSmiLinkUncorrErrors1WeekH_Type()
)
cucsProcessorErrorStatsSmiLinkUncorrErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkUncorrErrors1WeekH.setStatus("current")
_CucsProcessorErrorStatsSparingErrors_Type = Counter32
_CucsProcessorErrorStatsSparingErrors_Object = MibTableColumn
cucsProcessorErrorStatsSparingErrors = _CucsProcessorErrorStatsSparingErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 41),
    _CucsProcessorErrorStatsSparingErrors_Type()
)
cucsProcessorErrorStatsSparingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSparingErrors.setStatus("current")
_CucsProcessorErrorStatsSparingErrors15Min_Type = Gauge32
_CucsProcessorErrorStatsSparingErrors15Min_Object = MibTableColumn
cucsProcessorErrorStatsSparingErrors15Min = _CucsProcessorErrorStatsSparingErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 42),
    _CucsProcessorErrorStatsSparingErrors15Min_Type()
)
cucsProcessorErrorStatsSparingErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSparingErrors15Min.setStatus("current")
_CucsProcessorErrorStatsSparingErrors15MinH_Type = Gauge32
_CucsProcessorErrorStatsSparingErrors15MinH_Object = MibTableColumn
cucsProcessorErrorStatsSparingErrors15MinH = _CucsProcessorErrorStatsSparingErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 43),
    _CucsProcessorErrorStatsSparingErrors15MinH_Type()
)
cucsProcessorErrorStatsSparingErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSparingErrors15MinH.setStatus("current")
_CucsProcessorErrorStatsSparingErrors1Day_Type = Gauge32
_CucsProcessorErrorStatsSparingErrors1Day_Object = MibTableColumn
cucsProcessorErrorStatsSparingErrors1Day = _CucsProcessorErrorStatsSparingErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 44),
    _CucsProcessorErrorStatsSparingErrors1Day_Type()
)
cucsProcessorErrorStatsSparingErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSparingErrors1Day.setStatus("current")
_CucsProcessorErrorStatsSparingErrors1DayH_Type = Gauge32
_CucsProcessorErrorStatsSparingErrors1DayH_Object = MibTableColumn
cucsProcessorErrorStatsSparingErrors1DayH = _CucsProcessorErrorStatsSparingErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 45),
    _CucsProcessorErrorStatsSparingErrors1DayH_Type()
)
cucsProcessorErrorStatsSparingErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSparingErrors1DayH.setStatus("current")
_CucsProcessorErrorStatsSparingErrors1Hour_Type = Gauge32
_CucsProcessorErrorStatsSparingErrors1Hour_Object = MibTableColumn
cucsProcessorErrorStatsSparingErrors1Hour = _CucsProcessorErrorStatsSparingErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 46),
    _CucsProcessorErrorStatsSparingErrors1Hour_Type()
)
cucsProcessorErrorStatsSparingErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSparingErrors1Hour.setStatus("current")
_CucsProcessorErrorStatsSparingErrors1HourH_Type = Gauge32
_CucsProcessorErrorStatsSparingErrors1HourH_Object = MibTableColumn
cucsProcessorErrorStatsSparingErrors1HourH = _CucsProcessorErrorStatsSparingErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 47),
    _CucsProcessorErrorStatsSparingErrors1HourH_Type()
)
cucsProcessorErrorStatsSparingErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSparingErrors1HourH.setStatus("current")
_CucsProcessorErrorStatsSparingErrors1Week_Type = Gauge32
_CucsProcessorErrorStatsSparingErrors1Week_Object = MibTableColumn
cucsProcessorErrorStatsSparingErrors1Week = _CucsProcessorErrorStatsSparingErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 48),
    _CucsProcessorErrorStatsSparingErrors1Week_Type()
)
cucsProcessorErrorStatsSparingErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSparingErrors1Week.setStatus("current")
_CucsProcessorErrorStatsSparingErrors1WeekH_Type = Gauge32
_CucsProcessorErrorStatsSparingErrors1WeekH_Object = MibTableColumn
cucsProcessorErrorStatsSparingErrors1WeekH = _CucsProcessorErrorStatsSparingErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 49),
    _CucsProcessorErrorStatsSparingErrors1WeekH_Type()
)
cucsProcessorErrorStatsSparingErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSparingErrors1WeekH.setStatus("current")
_CucsProcessorErrorStatsSuspect_Type = TruthValue
_CucsProcessorErrorStatsSuspect_Object = MibTableColumn
cucsProcessorErrorStatsSuspect = _CucsProcessorErrorStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 50),
    _CucsProcessorErrorStatsSuspect_Type()
)
cucsProcessorErrorStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSuspect.setStatus("current")
_CucsProcessorErrorStatsThresholded_Type = CucsProcessorErrorStatsThresholded
_CucsProcessorErrorStatsThresholded_Object = MibTableColumn
cucsProcessorErrorStatsThresholded = _CucsProcessorErrorStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 51),
    _CucsProcessorErrorStatsThresholded_Type()
)
cucsProcessorErrorStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsThresholded.setStatus("current")
_CucsProcessorErrorStatsTimeCollected_Type = DateAndTime
_CucsProcessorErrorStatsTimeCollected_Object = MibTableColumn
cucsProcessorErrorStatsTimeCollected = _CucsProcessorErrorStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 52),
    _CucsProcessorErrorStatsTimeCollected_Type()
)
cucsProcessorErrorStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsTimeCollected.setStatus("current")
_CucsProcessorErrorStatsUpdate_Type = Gauge32
_CucsProcessorErrorStatsUpdate_Object = MibTableColumn
cucsProcessorErrorStatsUpdate = _CucsProcessorErrorStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 53),
    _CucsProcessorErrorStatsUpdate_Type()
)
cucsProcessorErrorStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsUpdate.setStatus("current")
_CucsProcessorErrorStatsMirroringInterSockErrors2Weeks_Type = Gauge32
_CucsProcessorErrorStatsMirroringInterSockErrors2Weeks_Object = MibTableColumn
cucsProcessorErrorStatsMirroringInterSockErrors2Weeks = _CucsProcessorErrorStatsMirroringInterSockErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 54),
    _CucsProcessorErrorStatsMirroringInterSockErrors2Weeks_Type()
)
cucsProcessorErrorStatsMirroringInterSockErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringInterSockErrors2Weeks.setStatus("current")
_CucsProcessorErrorStatsMirroringInterSockErrors2WeeksH_Type = Gauge32
_CucsProcessorErrorStatsMirroringInterSockErrors2WeeksH_Object = MibTableColumn
cucsProcessorErrorStatsMirroringInterSockErrors2WeeksH = _CucsProcessorErrorStatsMirroringInterSockErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 55),
    _CucsProcessorErrorStatsMirroringInterSockErrors2WeeksH_Type()
)
cucsProcessorErrorStatsMirroringInterSockErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringInterSockErrors2WeeksH.setStatus("current")
_CucsProcessorErrorStatsMirroringIntraSockErrors2Weeks_Type = Gauge32
_CucsProcessorErrorStatsMirroringIntraSockErrors2Weeks_Object = MibTableColumn
cucsProcessorErrorStatsMirroringIntraSockErrors2Weeks = _CucsProcessorErrorStatsMirroringIntraSockErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 56),
    _CucsProcessorErrorStatsMirroringIntraSockErrors2Weeks_Type()
)
cucsProcessorErrorStatsMirroringIntraSockErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringIntraSockErrors2Weeks.setStatus("current")
_CucsProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Type = Gauge32
_CucsProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Object = MibTableColumn
cucsProcessorErrorStatsMirroringIntraSockErrors2WeeksH = _CucsProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 57),
    _CucsProcessorErrorStatsMirroringIntraSockErrors2WeeksH_Type()
)
cucsProcessorErrorStatsMirroringIntraSockErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsMirroringIntraSockErrors2WeeksH.setStatus("current")
_CucsProcessorErrorStatsSmiLinkCorrErrors2Weeks_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkCorrErrors2Weeks_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkCorrErrors2Weeks = _CucsProcessorErrorStatsSmiLinkCorrErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 58),
    _CucsProcessorErrorStatsSmiLinkCorrErrors2Weeks_Type()
)
cucsProcessorErrorStatsSmiLinkCorrErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkCorrErrors2Weeks.setStatus("current")
_CucsProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkCorrErrors2WeeksH = _CucsProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 59),
    _CucsProcessorErrorStatsSmiLinkCorrErrors2WeeksH_Type()
)
cucsProcessorErrorStatsSmiLinkCorrErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkCorrErrors2WeeksH.setStatus("current")
_CucsProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkUncorrErrors2Weeks = _CucsProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 60),
    _CucsProcessorErrorStatsSmiLinkUncorrErrors2Weeks_Type()
)
cucsProcessorErrorStatsSmiLinkUncorrErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkUncorrErrors2Weeks.setStatus("current")
_CucsProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Type = Gauge32
_CucsProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Object = MibTableColumn
cucsProcessorErrorStatsSmiLinkUncorrErrors2WeeksH = _CucsProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 61),
    _CucsProcessorErrorStatsSmiLinkUncorrErrors2WeeksH_Type()
)
cucsProcessorErrorStatsSmiLinkUncorrErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSmiLinkUncorrErrors2WeeksH.setStatus("current")
_CucsProcessorErrorStatsSparingErrors2Weeks_Type = Gauge32
_CucsProcessorErrorStatsSparingErrors2Weeks_Object = MibTableColumn
cucsProcessorErrorStatsSparingErrors2Weeks = _CucsProcessorErrorStatsSparingErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 62),
    _CucsProcessorErrorStatsSparingErrors2Weeks_Type()
)
cucsProcessorErrorStatsSparingErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSparingErrors2Weeks.setStatus("current")
_CucsProcessorErrorStatsSparingErrors2WeeksH_Type = Gauge32
_CucsProcessorErrorStatsSparingErrors2WeeksH_Object = MibTableColumn
cucsProcessorErrorStatsSparingErrors2WeeksH = _CucsProcessorErrorStatsSparingErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 4, 1, 63),
    _CucsProcessorErrorStatsSparingErrors2WeeksH_Type()
)
cucsProcessorErrorStatsSparingErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorErrorStatsSparingErrors2WeeksH.setStatus("current")
_CucsProcessorQualTable_Object = MibTable
cucsProcessorQualTable = _CucsProcessorQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5)
)
if mibBuilder.loadTexts:
    cucsProcessorQualTable.setStatus("current")
_CucsProcessorQualEntry_Object = MibTableRow
cucsProcessorQualEntry = _CucsProcessorQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1)
)
cucsProcessorQualEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB", "cucsProcessorQualInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcessorQualEntry.setStatus("current")
_CucsProcessorQualInstanceId_Type = CucsManagedObjectId
_CucsProcessorQualInstanceId_Object = MibTableColumn
cucsProcessorQualInstanceId = _CucsProcessorQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 1),
    _CucsProcessorQualInstanceId_Type()
)
cucsProcessorQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcessorQualInstanceId.setStatus("current")
_CucsProcessorQualDn_Type = CucsManagedObjectDn
_CucsProcessorQualDn_Object = MibTableColumn
cucsProcessorQualDn = _CucsProcessorQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 2),
    _CucsProcessorQualDn_Type()
)
cucsProcessorQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualDn.setStatus("current")
_CucsProcessorQualRn_Type = SnmpAdminString
_CucsProcessorQualRn_Object = MibTableColumn
cucsProcessorQualRn = _CucsProcessorQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 3),
    _CucsProcessorQualRn_Type()
)
cucsProcessorQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualRn.setStatus("current")
_CucsProcessorQualArch_Type = CucsProcessorQualArch
_CucsProcessorQualArch_Object = MibTableColumn
cucsProcessorQualArch = _CucsProcessorQualArch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 4),
    _CucsProcessorQualArch_Type()
)
cucsProcessorQualArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualArch.setStatus("current")
_CucsProcessorQualMaxCores_Type = Gauge32
_CucsProcessorQualMaxCores_Object = MibTableColumn
cucsProcessorQualMaxCores = _CucsProcessorQualMaxCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 5),
    _CucsProcessorQualMaxCores_Type()
)
cucsProcessorQualMaxCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualMaxCores.setStatus("current")
_CucsProcessorQualMaxProcs_Type = Gauge32
_CucsProcessorQualMaxProcs_Object = MibTableColumn
cucsProcessorQualMaxProcs = _CucsProcessorQualMaxProcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 6),
    _CucsProcessorQualMaxProcs_Type()
)
cucsProcessorQualMaxProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualMaxProcs.setStatus("current")
_CucsProcessorQualMaxThreads_Type = Gauge32
_CucsProcessorQualMaxThreads_Object = MibTableColumn
cucsProcessorQualMaxThreads = _CucsProcessorQualMaxThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 7),
    _CucsProcessorQualMaxThreads_Type()
)
cucsProcessorQualMaxThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualMaxThreads.setStatus("current")
_CucsProcessorQualMinCores_Type = Gauge32
_CucsProcessorQualMinCores_Object = MibTableColumn
cucsProcessorQualMinCores = _CucsProcessorQualMinCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 8),
    _CucsProcessorQualMinCores_Type()
)
cucsProcessorQualMinCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualMinCores.setStatus("current")
_CucsProcessorQualMinProcs_Type = Gauge32
_CucsProcessorQualMinProcs_Object = MibTableColumn
cucsProcessorQualMinProcs = _CucsProcessorQualMinProcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 9),
    _CucsProcessorQualMinProcs_Type()
)
cucsProcessorQualMinProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualMinProcs.setStatus("current")
_CucsProcessorQualMinThreads_Type = Gauge32
_CucsProcessorQualMinThreads_Object = MibTableColumn
cucsProcessorQualMinThreads = _CucsProcessorQualMinThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 10),
    _CucsProcessorQualMinThreads_Type()
)
cucsProcessorQualMinThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualMinThreads.setStatus("current")
_CucsProcessorQualModel_Type = SnmpAdminString
_CucsProcessorQualModel_Object = MibTableColumn
cucsProcessorQualModel = _CucsProcessorQualModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 11),
    _CucsProcessorQualModel_Type()
)
cucsProcessorQualModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualModel.setStatus("current")
_CucsProcessorQualSpeed_Type = Integer32
_CucsProcessorQualSpeed_Object = MibTableColumn
cucsProcessorQualSpeed = _CucsProcessorQualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 12),
    _CucsProcessorQualSpeed_Type()
)
cucsProcessorQualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualSpeed.setStatus("current")
_CucsProcessorQualStepping_Type = Gauge32
_CucsProcessorQualStepping_Object = MibTableColumn
cucsProcessorQualStepping = _CucsProcessorQualStepping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 5, 1, 13),
    _CucsProcessorQualStepping_Type()
)
cucsProcessorQualStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorQualStepping.setStatus("current")
_CucsProcessorRuntimeTable_Object = MibTable
cucsProcessorRuntimeTable = _CucsProcessorRuntimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6)
)
if mibBuilder.loadTexts:
    cucsProcessorRuntimeTable.setStatus("current")
_CucsProcessorRuntimeEntry_Object = MibTableRow
cucsProcessorRuntimeEntry = _CucsProcessorRuntimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1)
)
cucsProcessorRuntimeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB", "cucsProcessorRuntimeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcessorRuntimeEntry.setStatus("current")
_CucsProcessorRuntimeInstanceId_Type = CucsManagedObjectId
_CucsProcessorRuntimeInstanceId_Object = MibTableColumn
cucsProcessorRuntimeInstanceId = _CucsProcessorRuntimeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 1),
    _CucsProcessorRuntimeInstanceId_Type()
)
cucsProcessorRuntimeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeInstanceId.setStatus("current")
_CucsProcessorRuntimeDn_Type = CucsManagedObjectDn
_CucsProcessorRuntimeDn_Object = MibTableColumn
cucsProcessorRuntimeDn = _CucsProcessorRuntimeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 2),
    _CucsProcessorRuntimeDn_Type()
)
cucsProcessorRuntimeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeDn.setStatus("current")
_CucsProcessorRuntimeRn_Type = SnmpAdminString
_CucsProcessorRuntimeRn_Object = MibTableColumn
cucsProcessorRuntimeRn = _CucsProcessorRuntimeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 3),
    _CucsProcessorRuntimeRn_Type()
)
cucsProcessorRuntimeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeRn.setStatus("current")
_CucsProcessorRuntimeIntervals_Type = Gauge32
_CucsProcessorRuntimeIntervals_Object = MibTableColumn
cucsProcessorRuntimeIntervals = _CucsProcessorRuntimeIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 4),
    _CucsProcessorRuntimeIntervals_Type()
)
cucsProcessorRuntimeIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeIntervals.setStatus("current")
_CucsProcessorRuntimeLoad_Type = Integer32
_CucsProcessorRuntimeLoad_Object = MibTableColumn
cucsProcessorRuntimeLoad = _CucsProcessorRuntimeLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 5),
    _CucsProcessorRuntimeLoad_Type()
)
cucsProcessorRuntimeLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeLoad.setStatus("current")
_CucsProcessorRuntimeLoadAvg_Type = Integer32
_CucsProcessorRuntimeLoadAvg_Object = MibTableColumn
cucsProcessorRuntimeLoadAvg = _CucsProcessorRuntimeLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 6),
    _CucsProcessorRuntimeLoadAvg_Type()
)
cucsProcessorRuntimeLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeLoadAvg.setStatus("current")
_CucsProcessorRuntimeLoadMax_Type = Integer32
_CucsProcessorRuntimeLoadMax_Object = MibTableColumn
cucsProcessorRuntimeLoadMax = _CucsProcessorRuntimeLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 7),
    _CucsProcessorRuntimeLoadMax_Type()
)
cucsProcessorRuntimeLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeLoadMax.setStatus("current")
_CucsProcessorRuntimeLoadMin_Type = Integer32
_CucsProcessorRuntimeLoadMin_Object = MibTableColumn
cucsProcessorRuntimeLoadMin = _CucsProcessorRuntimeLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 8),
    _CucsProcessorRuntimeLoadMin_Type()
)
cucsProcessorRuntimeLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeLoadMin.setStatus("current")
_CucsProcessorRuntimeSuspect_Type = TruthValue
_CucsProcessorRuntimeSuspect_Object = MibTableColumn
cucsProcessorRuntimeSuspect = _CucsProcessorRuntimeSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 9),
    _CucsProcessorRuntimeSuspect_Type()
)
cucsProcessorRuntimeSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeSuspect.setStatus("current")
_CucsProcessorRuntimeThresholded_Type = CucsProcessorRuntimeThresholded
_CucsProcessorRuntimeThresholded_Object = MibTableColumn
cucsProcessorRuntimeThresholded = _CucsProcessorRuntimeThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 10),
    _CucsProcessorRuntimeThresholded_Type()
)
cucsProcessorRuntimeThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeThresholded.setStatus("current")
_CucsProcessorRuntimeTimeCollected_Type = DateAndTime
_CucsProcessorRuntimeTimeCollected_Object = MibTableColumn
cucsProcessorRuntimeTimeCollected = _CucsProcessorRuntimeTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 11),
    _CucsProcessorRuntimeTimeCollected_Type()
)
cucsProcessorRuntimeTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeTimeCollected.setStatus("current")
_CucsProcessorRuntimeUpdate_Type = Gauge32
_CucsProcessorRuntimeUpdate_Object = MibTableColumn
cucsProcessorRuntimeUpdate = _CucsProcessorRuntimeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 12),
    _CucsProcessorRuntimeUpdate_Type()
)
cucsProcessorRuntimeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeUpdate.setStatus("current")
_CucsProcessorRuntimeUptime_Type = TimeIntervalSec
_CucsProcessorRuntimeUptime_Object = MibTableColumn
cucsProcessorRuntimeUptime = _CucsProcessorRuntimeUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 6, 1, 13),
    _CucsProcessorRuntimeUptime_Type()
)
cucsProcessorRuntimeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeUptime.setStatus("current")
_CucsProcessorRuntimeHistTable_Object = MibTable
cucsProcessorRuntimeHistTable = _CucsProcessorRuntimeHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7)
)
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistTable.setStatus("current")
_CucsProcessorRuntimeHistEntry_Object = MibTableRow
cucsProcessorRuntimeHistEntry = _CucsProcessorRuntimeHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1)
)
cucsProcessorRuntimeHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB", "cucsProcessorRuntimeHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistEntry.setStatus("current")
_CucsProcessorRuntimeHistInstanceId_Type = CucsManagedObjectId
_CucsProcessorRuntimeHistInstanceId_Object = MibTableColumn
cucsProcessorRuntimeHistInstanceId = _CucsProcessorRuntimeHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 1),
    _CucsProcessorRuntimeHistInstanceId_Type()
)
cucsProcessorRuntimeHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistInstanceId.setStatus("current")
_CucsProcessorRuntimeHistDn_Type = CucsManagedObjectDn
_CucsProcessorRuntimeHistDn_Object = MibTableColumn
cucsProcessorRuntimeHistDn = _CucsProcessorRuntimeHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 2),
    _CucsProcessorRuntimeHistDn_Type()
)
cucsProcessorRuntimeHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistDn.setStatus("current")
_CucsProcessorRuntimeHistRn_Type = SnmpAdminString
_CucsProcessorRuntimeHistRn_Object = MibTableColumn
cucsProcessorRuntimeHistRn = _CucsProcessorRuntimeHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 3),
    _CucsProcessorRuntimeHistRn_Type()
)
cucsProcessorRuntimeHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistRn.setStatus("current")
_CucsProcessorRuntimeHistId_Type = Unsigned64
_CucsProcessorRuntimeHistId_Object = MibTableColumn
cucsProcessorRuntimeHistId = _CucsProcessorRuntimeHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 4),
    _CucsProcessorRuntimeHistId_Type()
)
cucsProcessorRuntimeHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistId.setStatus("current")
_CucsProcessorRuntimeHistLoad_Type = Integer32
_CucsProcessorRuntimeHistLoad_Object = MibTableColumn
cucsProcessorRuntimeHistLoad = _CucsProcessorRuntimeHistLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 5),
    _CucsProcessorRuntimeHistLoad_Type()
)
cucsProcessorRuntimeHistLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistLoad.setStatus("current")
_CucsProcessorRuntimeHistLoadAvg_Type = Integer32
_CucsProcessorRuntimeHistLoadAvg_Object = MibTableColumn
cucsProcessorRuntimeHistLoadAvg = _CucsProcessorRuntimeHistLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 6),
    _CucsProcessorRuntimeHistLoadAvg_Type()
)
cucsProcessorRuntimeHistLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistLoadAvg.setStatus("current")
_CucsProcessorRuntimeHistLoadMax_Type = Integer32
_CucsProcessorRuntimeHistLoadMax_Object = MibTableColumn
cucsProcessorRuntimeHistLoadMax = _CucsProcessorRuntimeHistLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 7),
    _CucsProcessorRuntimeHistLoadMax_Type()
)
cucsProcessorRuntimeHistLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistLoadMax.setStatus("current")
_CucsProcessorRuntimeHistLoadMin_Type = Integer32
_CucsProcessorRuntimeHistLoadMin_Object = MibTableColumn
cucsProcessorRuntimeHistLoadMin = _CucsProcessorRuntimeHistLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 8),
    _CucsProcessorRuntimeHistLoadMin_Type()
)
cucsProcessorRuntimeHistLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistLoadMin.setStatus("current")
_CucsProcessorRuntimeHistMostRecent_Type = TruthValue
_CucsProcessorRuntimeHistMostRecent_Object = MibTableColumn
cucsProcessorRuntimeHistMostRecent = _CucsProcessorRuntimeHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 9),
    _CucsProcessorRuntimeHistMostRecent_Type()
)
cucsProcessorRuntimeHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistMostRecent.setStatus("current")
_CucsProcessorRuntimeHistSuspect_Type = TruthValue
_CucsProcessorRuntimeHistSuspect_Object = MibTableColumn
cucsProcessorRuntimeHistSuspect = _CucsProcessorRuntimeHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 10),
    _CucsProcessorRuntimeHistSuspect_Type()
)
cucsProcessorRuntimeHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistSuspect.setStatus("current")
_CucsProcessorRuntimeHistThresholded_Type = CucsProcessorRuntimeHistThresholded
_CucsProcessorRuntimeHistThresholded_Object = MibTableColumn
cucsProcessorRuntimeHistThresholded = _CucsProcessorRuntimeHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 11),
    _CucsProcessorRuntimeHistThresholded_Type()
)
cucsProcessorRuntimeHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistThresholded.setStatus("current")
_CucsProcessorRuntimeHistTimeCollected_Type = DateAndTime
_CucsProcessorRuntimeHistTimeCollected_Object = MibTableColumn
cucsProcessorRuntimeHistTimeCollected = _CucsProcessorRuntimeHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 7, 1, 12),
    _CucsProcessorRuntimeHistTimeCollected_Type()
)
cucsProcessorRuntimeHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorRuntimeHistTimeCollected.setStatus("current")
_CucsProcessorThreadTable_Object = MibTable
cucsProcessorThreadTable = _CucsProcessorThreadTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 8)
)
if mibBuilder.loadTexts:
    cucsProcessorThreadTable.setStatus("current")
_CucsProcessorThreadEntry_Object = MibTableRow
cucsProcessorThreadEntry = _CucsProcessorThreadEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 8, 1)
)
cucsProcessorThreadEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB", "cucsProcessorThreadInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcessorThreadEntry.setStatus("current")
_CucsProcessorThreadInstanceId_Type = CucsManagedObjectId
_CucsProcessorThreadInstanceId_Object = MibTableColumn
cucsProcessorThreadInstanceId = _CucsProcessorThreadInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 8, 1, 1),
    _CucsProcessorThreadInstanceId_Type()
)
cucsProcessorThreadInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcessorThreadInstanceId.setStatus("current")
_CucsProcessorThreadDn_Type = CucsManagedObjectDn
_CucsProcessorThreadDn_Object = MibTableColumn
cucsProcessorThreadDn = _CucsProcessorThreadDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 8, 1, 2),
    _CucsProcessorThreadDn_Type()
)
cucsProcessorThreadDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorThreadDn.setStatus("current")
_CucsProcessorThreadRn_Type = SnmpAdminString
_CucsProcessorThreadRn_Object = MibTableColumn
cucsProcessorThreadRn = _CucsProcessorThreadRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 8, 1, 3),
    _CucsProcessorThreadRn_Type()
)
cucsProcessorThreadRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorThreadRn.setStatus("current")
_CucsProcessorThreadId_Type = Gauge32
_CucsProcessorThreadId_Object = MibTableColumn
cucsProcessorThreadId = _CucsProcessorThreadId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 8, 1, 4),
    _CucsProcessorThreadId_Type()
)
cucsProcessorThreadId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorThreadId.setStatus("current")
_CucsProcessorUnitTable_Object = MibTable
cucsProcessorUnitTable = _CucsProcessorUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9)
)
if mibBuilder.loadTexts:
    cucsProcessorUnitTable.setStatus("current")
_CucsProcessorUnitEntry_Object = MibTableRow
cucsProcessorUnitEntry = _CucsProcessorUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1)
)
cucsProcessorUnitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB", "cucsProcessorUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcessorUnitEntry.setStatus("current")
_CucsProcessorUnitInstanceId_Type = CucsManagedObjectId
_CucsProcessorUnitInstanceId_Object = MibTableColumn
cucsProcessorUnitInstanceId = _CucsProcessorUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 1),
    _CucsProcessorUnitInstanceId_Type()
)
cucsProcessorUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcessorUnitInstanceId.setStatus("current")
_CucsProcessorUnitDn_Type = CucsManagedObjectDn
_CucsProcessorUnitDn_Object = MibTableColumn
cucsProcessorUnitDn = _CucsProcessorUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 2),
    _CucsProcessorUnitDn_Type()
)
cucsProcessorUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitDn.setStatus("current")
_CucsProcessorUnitRn_Type = SnmpAdminString
_CucsProcessorUnitRn_Object = MibTableColumn
cucsProcessorUnitRn = _CucsProcessorUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 3),
    _CucsProcessorUnitRn_Type()
)
cucsProcessorUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitRn.setStatus("current")
_CucsProcessorUnitArch_Type = CucsProcessorUnitArch
_CucsProcessorUnitArch_Object = MibTableColumn
cucsProcessorUnitArch = _CucsProcessorUnitArch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 4),
    _CucsProcessorUnitArch_Type()
)
cucsProcessorUnitArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitArch.setStatus("current")
_CucsProcessorUnitCores_Type = Gauge32
_CucsProcessorUnitCores_Object = MibTableColumn
cucsProcessorUnitCores = _CucsProcessorUnitCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 5),
    _CucsProcessorUnitCores_Type()
)
cucsProcessorUnitCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitCores.setStatus("current")
_CucsProcessorUnitCoresEnabled_Type = Gauge32
_CucsProcessorUnitCoresEnabled_Object = MibTableColumn
cucsProcessorUnitCoresEnabled = _CucsProcessorUnitCoresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 6),
    _CucsProcessorUnitCoresEnabled_Type()
)
cucsProcessorUnitCoresEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitCoresEnabled.setStatus("current")
_CucsProcessorUnitId_Type = Gauge32
_CucsProcessorUnitId_Object = MibTableColumn
cucsProcessorUnitId = _CucsProcessorUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 7),
    _CucsProcessorUnitId_Type()
)
cucsProcessorUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitId.setStatus("current")
_CucsProcessorUnitModel_Type = SnmpAdminString
_CucsProcessorUnitModel_Object = MibTableColumn
cucsProcessorUnitModel = _CucsProcessorUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 8),
    _CucsProcessorUnitModel_Type()
)
cucsProcessorUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitModel.setStatus("current")
_CucsProcessorUnitOperState_Type = CucsEquipmentOperability
_CucsProcessorUnitOperState_Object = MibTableColumn
cucsProcessorUnitOperState = _CucsProcessorUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 9),
    _CucsProcessorUnitOperState_Type()
)
cucsProcessorUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitOperState.setStatus("current")
_CucsProcessorUnitOperability_Type = CucsEquipmentOperability
_CucsProcessorUnitOperability_Object = MibTableColumn
cucsProcessorUnitOperability = _CucsProcessorUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 10),
    _CucsProcessorUnitOperability_Type()
)
cucsProcessorUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitOperability.setStatus("current")
_CucsProcessorUnitPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsProcessorUnitPerf_Object = MibTableColumn
cucsProcessorUnitPerf = _CucsProcessorUnitPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 11),
    _CucsProcessorUnitPerf_Type()
)
cucsProcessorUnitPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitPerf.setStatus("current")
_CucsProcessorUnitPower_Type = CucsEquipmentPowerState
_CucsProcessorUnitPower_Object = MibTableColumn
cucsProcessorUnitPower = _CucsProcessorUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 12),
    _CucsProcessorUnitPower_Type()
)
cucsProcessorUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitPower.setStatus("current")
_CucsProcessorUnitPresence_Type = CucsEquipmentPresence
_CucsProcessorUnitPresence_Object = MibTableColumn
cucsProcessorUnitPresence = _CucsProcessorUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 13),
    _CucsProcessorUnitPresence_Type()
)
cucsProcessorUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitPresence.setStatus("current")
_CucsProcessorUnitRevision_Type = SnmpAdminString
_CucsProcessorUnitRevision_Object = MibTableColumn
cucsProcessorUnitRevision = _CucsProcessorUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 14),
    _CucsProcessorUnitRevision_Type()
)
cucsProcessorUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitRevision.setStatus("current")
_CucsProcessorUnitSerial_Type = SnmpAdminString
_CucsProcessorUnitSerial_Object = MibTableColumn
cucsProcessorUnitSerial = _CucsProcessorUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 15),
    _CucsProcessorUnitSerial_Type()
)
cucsProcessorUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitSerial.setStatus("current")
_CucsProcessorUnitSocketDesignation_Type = SnmpAdminString
_CucsProcessorUnitSocketDesignation_Object = MibTableColumn
cucsProcessorUnitSocketDesignation = _CucsProcessorUnitSocketDesignation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 16),
    _CucsProcessorUnitSocketDesignation_Type()
)
cucsProcessorUnitSocketDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitSocketDesignation.setStatus("current")
_CucsProcessorUnitSpeed_Type = Integer32
_CucsProcessorUnitSpeed_Object = MibTableColumn
cucsProcessorUnitSpeed = _CucsProcessorUnitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 17),
    _CucsProcessorUnitSpeed_Type()
)
cucsProcessorUnitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitSpeed.setStatus("current")
_CucsProcessorUnitStepping_Type = Gauge32
_CucsProcessorUnitStepping_Object = MibTableColumn
cucsProcessorUnitStepping = _CucsProcessorUnitStepping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 18),
    _CucsProcessorUnitStepping_Type()
)
cucsProcessorUnitStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitStepping.setStatus("current")
_CucsProcessorUnitThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsProcessorUnitThermal_Object = MibTableColumn
cucsProcessorUnitThermal = _CucsProcessorUnitThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 19),
    _CucsProcessorUnitThermal_Type()
)
cucsProcessorUnitThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitThermal.setStatus("current")
_CucsProcessorUnitThreads_Type = Gauge32
_CucsProcessorUnitThreads_Object = MibTableColumn
cucsProcessorUnitThreads = _CucsProcessorUnitThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 20),
    _CucsProcessorUnitThreads_Type()
)
cucsProcessorUnitThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitThreads.setStatus("current")
_CucsProcessorUnitVendor_Type = SnmpAdminString
_CucsProcessorUnitVendor_Object = MibTableColumn
cucsProcessorUnitVendor = _CucsProcessorUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 21),
    _CucsProcessorUnitVendor_Type()
)
cucsProcessorUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitVendor.setStatus("current")
_CucsProcessorUnitVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsProcessorUnitVoltage_Object = MibTableColumn
cucsProcessorUnitVoltage = _CucsProcessorUnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 22),
    _CucsProcessorUnitVoltage_Type()
)
cucsProcessorUnitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitVoltage.setStatus("current")
_CucsProcessorUnitVisibility_Type = CucsMemoryVisibility
_CucsProcessorUnitVisibility_Object = MibTableColumn
cucsProcessorUnitVisibility = _CucsProcessorUnitVisibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 23),
    _CucsProcessorUnitVisibility_Type()
)
cucsProcessorUnitVisibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitVisibility.setStatus("current")
_CucsProcessorUnitOperQualifierReason_Type = SnmpAdminString
_CucsProcessorUnitOperQualifierReason_Object = MibTableColumn
cucsProcessorUnitOperQualifierReason = _CucsProcessorUnitOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 24),
    _CucsProcessorUnitOperQualifierReason_Type()
)
cucsProcessorUnitOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitOperQualifierReason.setStatus("current")
_CucsProcessorUnitLocationDn_Type = SnmpAdminString
_CucsProcessorUnitLocationDn_Object = MibTableColumn
cucsProcessorUnitLocationDn = _CucsProcessorUnitLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 9, 1, 25),
    _CucsProcessorUnitLocationDn_Type()
)
cucsProcessorUnitLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitLocationDn.setStatus("current")
_CucsProcessorUnitAssocCtxTable_Object = MibTable
cucsProcessorUnitAssocCtxTable = _CucsProcessorUnitAssocCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 10)
)
if mibBuilder.loadTexts:
    cucsProcessorUnitAssocCtxTable.setStatus("current")
_CucsProcessorUnitAssocCtxEntry_Object = MibTableRow
cucsProcessorUnitAssocCtxEntry = _CucsProcessorUnitAssocCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 10, 1)
)
cucsProcessorUnitAssocCtxEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB", "cucsProcessorUnitAssocCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcessorUnitAssocCtxEntry.setStatus("current")
_CucsProcessorUnitAssocCtxInstanceId_Type = CucsManagedObjectId
_CucsProcessorUnitAssocCtxInstanceId_Object = MibTableColumn
cucsProcessorUnitAssocCtxInstanceId = _CucsProcessorUnitAssocCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 10, 1, 1),
    _CucsProcessorUnitAssocCtxInstanceId_Type()
)
cucsProcessorUnitAssocCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcessorUnitAssocCtxInstanceId.setStatus("current")
_CucsProcessorUnitAssocCtxDn_Type = CucsManagedObjectDn
_CucsProcessorUnitAssocCtxDn_Object = MibTableColumn
cucsProcessorUnitAssocCtxDn = _CucsProcessorUnitAssocCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 10, 1, 2),
    _CucsProcessorUnitAssocCtxDn_Type()
)
cucsProcessorUnitAssocCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitAssocCtxDn.setStatus("current")
_CucsProcessorUnitAssocCtxRn_Type = SnmpAdminString
_CucsProcessorUnitAssocCtxRn_Object = MibTableColumn
cucsProcessorUnitAssocCtxRn = _CucsProcessorUnitAssocCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 10, 1, 3),
    _CucsProcessorUnitAssocCtxRn_Type()
)
cucsProcessorUnitAssocCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitAssocCtxRn.setStatus("current")
_CucsProcessorUnitAssocCtxFruCapDn_Type = SnmpAdminString
_CucsProcessorUnitAssocCtxFruCapDn_Object = MibTableColumn
cucsProcessorUnitAssocCtxFruCapDn = _CucsProcessorUnitAssocCtxFruCapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 10, 1, 4),
    _CucsProcessorUnitAssocCtxFruCapDn_Type()
)
cucsProcessorUnitAssocCtxFruCapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitAssocCtxFruCapDn.setStatus("current")
_CucsProcessorUnitAssocCtxStepping_Type = Gauge32
_CucsProcessorUnitAssocCtxStepping_Object = MibTableColumn
cucsProcessorUnitAssocCtxStepping = _CucsProcessorUnitAssocCtxStepping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 41, 10, 1, 5),
    _CucsProcessorUnitAssocCtxStepping_Type()
)
cucsProcessorUnitAssocCtxStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcessorUnitAssocCtxStepping.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB",
    **{"cucsProcessorObjects": cucsProcessorObjects,
       "cucsProcessorCoreTable": cucsProcessorCoreTable,
       "cucsProcessorCoreEntry": cucsProcessorCoreEntry,
       "cucsProcessorCoreInstanceId": cucsProcessorCoreInstanceId,
       "cucsProcessorCoreDn": cucsProcessorCoreDn,
       "cucsProcessorCoreRn": cucsProcessorCoreRn,
       "cucsProcessorCoreId": cucsProcessorCoreId,
       "cucsProcessorEnvStatsTable": cucsProcessorEnvStatsTable,
       "cucsProcessorEnvStatsEntry": cucsProcessorEnvStatsEntry,
       "cucsProcessorEnvStatsInstanceId": cucsProcessorEnvStatsInstanceId,
       "cucsProcessorEnvStatsDn": cucsProcessorEnvStatsDn,
       "cucsProcessorEnvStatsRn": cucsProcessorEnvStatsRn,
       "cucsProcessorEnvStatsInputCurrent": cucsProcessorEnvStatsInputCurrent,
       "cucsProcessorEnvStatsInputCurrentAvg": cucsProcessorEnvStatsInputCurrentAvg,
       "cucsProcessorEnvStatsInputCurrentMax": cucsProcessorEnvStatsInputCurrentMax,
       "cucsProcessorEnvStatsInputCurrentMin": cucsProcessorEnvStatsInputCurrentMin,
       "cucsProcessorEnvStatsIntervals": cucsProcessorEnvStatsIntervals,
       "cucsProcessorEnvStatsSuspect": cucsProcessorEnvStatsSuspect,
       "cucsProcessorEnvStatsTemperature": cucsProcessorEnvStatsTemperature,
       "cucsProcessorEnvStatsTemperatureAvg": cucsProcessorEnvStatsTemperatureAvg,
       "cucsProcessorEnvStatsTemperatureMax": cucsProcessorEnvStatsTemperatureMax,
       "cucsProcessorEnvStatsTemperatureMin": cucsProcessorEnvStatsTemperatureMin,
       "cucsProcessorEnvStatsThresholded": cucsProcessorEnvStatsThresholded,
       "cucsProcessorEnvStatsTimeCollected": cucsProcessorEnvStatsTimeCollected,
       "cucsProcessorEnvStatsUpdate": cucsProcessorEnvStatsUpdate,
       "cucsProcessorEnvStatsHistTable": cucsProcessorEnvStatsHistTable,
       "cucsProcessorEnvStatsHistEntry": cucsProcessorEnvStatsHistEntry,
       "cucsProcessorEnvStatsHistInstanceId": cucsProcessorEnvStatsHistInstanceId,
       "cucsProcessorEnvStatsHistDn": cucsProcessorEnvStatsHistDn,
       "cucsProcessorEnvStatsHistRn": cucsProcessorEnvStatsHistRn,
       "cucsProcessorEnvStatsHistId": cucsProcessorEnvStatsHistId,
       "cucsProcessorEnvStatsHistInputCurrent": cucsProcessorEnvStatsHistInputCurrent,
       "cucsProcessorEnvStatsHistInputCurrentAvg": cucsProcessorEnvStatsHistInputCurrentAvg,
       "cucsProcessorEnvStatsHistInputCurrentMax": cucsProcessorEnvStatsHistInputCurrentMax,
       "cucsProcessorEnvStatsHistInputCurrentMin": cucsProcessorEnvStatsHistInputCurrentMin,
       "cucsProcessorEnvStatsHistMostRecent": cucsProcessorEnvStatsHistMostRecent,
       "cucsProcessorEnvStatsHistSuspect": cucsProcessorEnvStatsHistSuspect,
       "cucsProcessorEnvStatsHistTemperature": cucsProcessorEnvStatsHistTemperature,
       "cucsProcessorEnvStatsHistTemperatureAvg": cucsProcessorEnvStatsHistTemperatureAvg,
       "cucsProcessorEnvStatsHistTemperatureMax": cucsProcessorEnvStatsHistTemperatureMax,
       "cucsProcessorEnvStatsHistTemperatureMin": cucsProcessorEnvStatsHistTemperatureMin,
       "cucsProcessorEnvStatsHistThresholded": cucsProcessorEnvStatsHistThresholded,
       "cucsProcessorEnvStatsHistTimeCollected": cucsProcessorEnvStatsHistTimeCollected,
       "cucsProcessorErrorStatsTable": cucsProcessorErrorStatsTable,
       "cucsProcessorErrorStatsEntry": cucsProcessorErrorStatsEntry,
       "cucsProcessorErrorStatsInstanceId": cucsProcessorErrorStatsInstanceId,
       "cucsProcessorErrorStatsDn": cucsProcessorErrorStatsDn,
       "cucsProcessorErrorStatsRn": cucsProcessorErrorStatsRn,
       "cucsProcessorErrorStatsIntervals": cucsProcessorErrorStatsIntervals,
       "cucsProcessorErrorStatsMirroringInterSockErrors": cucsProcessorErrorStatsMirroringInterSockErrors,
       "cucsProcessorErrorStatsMirroringInterSockErrors15Min": cucsProcessorErrorStatsMirroringInterSockErrors15Min,
       "cucsProcessorErrorStatsMirroringInterSockErrors15MinH": cucsProcessorErrorStatsMirroringInterSockErrors15MinH,
       "cucsProcessorErrorStatsMirroringInterSockErrors1Day": cucsProcessorErrorStatsMirroringInterSockErrors1Day,
       "cucsProcessorErrorStatsMirroringInterSockErrors1DayH": cucsProcessorErrorStatsMirroringInterSockErrors1DayH,
       "cucsProcessorErrorStatsMirroringInterSockErrors1Hour": cucsProcessorErrorStatsMirroringInterSockErrors1Hour,
       "cucsProcessorErrorStatsMirroringInterSockErrors1HourH": cucsProcessorErrorStatsMirroringInterSockErrors1HourH,
       "cucsProcessorErrorStatsMirroringInterSockErrors1Week": cucsProcessorErrorStatsMirroringInterSockErrors1Week,
       "cucsProcessorErrorStatsMirroringInterSockErrors1WeekH": cucsProcessorErrorStatsMirroringInterSockErrors1WeekH,
       "cucsProcessorErrorStatsMirroringIntraSockErrors": cucsProcessorErrorStatsMirroringIntraSockErrors,
       "cucsProcessorErrorStatsMirroringIntraSockErrors15Min": cucsProcessorErrorStatsMirroringIntraSockErrors15Min,
       "cucsProcessorErrorStatsMirroringIntraSockErrors15MinH": cucsProcessorErrorStatsMirroringIntraSockErrors15MinH,
       "cucsProcessorErrorStatsMirroringIntraSockErrors1Day": cucsProcessorErrorStatsMirroringIntraSockErrors1Day,
       "cucsProcessorErrorStatsMirroringIntraSockErrors1DayH": cucsProcessorErrorStatsMirroringIntraSockErrors1DayH,
       "cucsProcessorErrorStatsMirroringIntraSockErrors1Hour": cucsProcessorErrorStatsMirroringIntraSockErrors1Hour,
       "cucsProcessorErrorStatsMirroringIntraSockErrors1HourH": cucsProcessorErrorStatsMirroringIntraSockErrors1HourH,
       "cucsProcessorErrorStatsMirroringIntraSockErrors1Week": cucsProcessorErrorStatsMirroringIntraSockErrors1Week,
       "cucsProcessorErrorStatsMirroringIntraSockErrors1WeekH": cucsProcessorErrorStatsMirroringIntraSockErrors1WeekH,
       "cucsProcessorErrorStatsSmiLinkCorrErrors": cucsProcessorErrorStatsSmiLinkCorrErrors,
       "cucsProcessorErrorStatsSmiLinkCorrErrors15Min": cucsProcessorErrorStatsSmiLinkCorrErrors15Min,
       "cucsProcessorErrorStatsSmiLinkCorrErrors15MinH": cucsProcessorErrorStatsSmiLinkCorrErrors15MinH,
       "cucsProcessorErrorStatsSmiLinkCorrErrors1Day": cucsProcessorErrorStatsSmiLinkCorrErrors1Day,
       "cucsProcessorErrorStatsSmiLinkCorrErrors1DayH": cucsProcessorErrorStatsSmiLinkCorrErrors1DayH,
       "cucsProcessorErrorStatsSmiLinkCorrErrors1Hour": cucsProcessorErrorStatsSmiLinkCorrErrors1Hour,
       "cucsProcessorErrorStatsSmiLinkCorrErrors1HourH": cucsProcessorErrorStatsSmiLinkCorrErrors1HourH,
       "cucsProcessorErrorStatsSmiLinkCorrErrors1Week": cucsProcessorErrorStatsSmiLinkCorrErrors1Week,
       "cucsProcessorErrorStatsSmiLinkCorrErrors1WeekH": cucsProcessorErrorStatsSmiLinkCorrErrors1WeekH,
       "cucsProcessorErrorStatsSmiLinkUncorrErrors": cucsProcessorErrorStatsSmiLinkUncorrErrors,
       "cucsProcessorErrorStatsSmiLinkUncorrErrors15Min": cucsProcessorErrorStatsSmiLinkUncorrErrors15Min,
       "cucsProcessorErrorStatsSmiLinkUncorrErrors15MinH": cucsProcessorErrorStatsSmiLinkUncorrErrors15MinH,
       "cucsProcessorErrorStatsSmiLinkUncorrErrors1Day": cucsProcessorErrorStatsSmiLinkUncorrErrors1Day,
       "cucsProcessorErrorStatsSmiLinkUncorrErrors1DayH": cucsProcessorErrorStatsSmiLinkUncorrErrors1DayH,
       "cucsProcessorErrorStatsSmiLinkUncorrErrors1Hour": cucsProcessorErrorStatsSmiLinkUncorrErrors1Hour,
       "cucsProcessorErrorStatsSmiLinkUncorrErrors1HourH": cucsProcessorErrorStatsSmiLinkUncorrErrors1HourH,
       "cucsProcessorErrorStatsSmiLinkUncorrErrors1Week": cucsProcessorErrorStatsSmiLinkUncorrErrors1Week,
       "cucsProcessorErrorStatsSmiLinkUncorrErrors1WeekH": cucsProcessorErrorStatsSmiLinkUncorrErrors1WeekH,
       "cucsProcessorErrorStatsSparingErrors": cucsProcessorErrorStatsSparingErrors,
       "cucsProcessorErrorStatsSparingErrors15Min": cucsProcessorErrorStatsSparingErrors15Min,
       "cucsProcessorErrorStatsSparingErrors15MinH": cucsProcessorErrorStatsSparingErrors15MinH,
       "cucsProcessorErrorStatsSparingErrors1Day": cucsProcessorErrorStatsSparingErrors1Day,
       "cucsProcessorErrorStatsSparingErrors1DayH": cucsProcessorErrorStatsSparingErrors1DayH,
       "cucsProcessorErrorStatsSparingErrors1Hour": cucsProcessorErrorStatsSparingErrors1Hour,
       "cucsProcessorErrorStatsSparingErrors1HourH": cucsProcessorErrorStatsSparingErrors1HourH,
       "cucsProcessorErrorStatsSparingErrors1Week": cucsProcessorErrorStatsSparingErrors1Week,
       "cucsProcessorErrorStatsSparingErrors1WeekH": cucsProcessorErrorStatsSparingErrors1WeekH,
       "cucsProcessorErrorStatsSuspect": cucsProcessorErrorStatsSuspect,
       "cucsProcessorErrorStatsThresholded": cucsProcessorErrorStatsThresholded,
       "cucsProcessorErrorStatsTimeCollected": cucsProcessorErrorStatsTimeCollected,
       "cucsProcessorErrorStatsUpdate": cucsProcessorErrorStatsUpdate,
       "cucsProcessorErrorStatsMirroringInterSockErrors2Weeks": cucsProcessorErrorStatsMirroringInterSockErrors2Weeks,
       "cucsProcessorErrorStatsMirroringInterSockErrors2WeeksH": cucsProcessorErrorStatsMirroringInterSockErrors2WeeksH,
       "cucsProcessorErrorStatsMirroringIntraSockErrors2Weeks": cucsProcessorErrorStatsMirroringIntraSockErrors2Weeks,
       "cucsProcessorErrorStatsMirroringIntraSockErrors2WeeksH": cucsProcessorErrorStatsMirroringIntraSockErrors2WeeksH,
       "cucsProcessorErrorStatsSmiLinkCorrErrors2Weeks": cucsProcessorErrorStatsSmiLinkCorrErrors2Weeks,
       "cucsProcessorErrorStatsSmiLinkCorrErrors2WeeksH": cucsProcessorErrorStatsSmiLinkCorrErrors2WeeksH,
       "cucsProcessorErrorStatsSmiLinkUncorrErrors2Weeks": cucsProcessorErrorStatsSmiLinkUncorrErrors2Weeks,
       "cucsProcessorErrorStatsSmiLinkUncorrErrors2WeeksH": cucsProcessorErrorStatsSmiLinkUncorrErrors2WeeksH,
       "cucsProcessorErrorStatsSparingErrors2Weeks": cucsProcessorErrorStatsSparingErrors2Weeks,
       "cucsProcessorErrorStatsSparingErrors2WeeksH": cucsProcessorErrorStatsSparingErrors2WeeksH,
       "cucsProcessorQualTable": cucsProcessorQualTable,
       "cucsProcessorQualEntry": cucsProcessorQualEntry,
       "cucsProcessorQualInstanceId": cucsProcessorQualInstanceId,
       "cucsProcessorQualDn": cucsProcessorQualDn,
       "cucsProcessorQualRn": cucsProcessorQualRn,
       "cucsProcessorQualArch": cucsProcessorQualArch,
       "cucsProcessorQualMaxCores": cucsProcessorQualMaxCores,
       "cucsProcessorQualMaxProcs": cucsProcessorQualMaxProcs,
       "cucsProcessorQualMaxThreads": cucsProcessorQualMaxThreads,
       "cucsProcessorQualMinCores": cucsProcessorQualMinCores,
       "cucsProcessorQualMinProcs": cucsProcessorQualMinProcs,
       "cucsProcessorQualMinThreads": cucsProcessorQualMinThreads,
       "cucsProcessorQualModel": cucsProcessorQualModel,
       "cucsProcessorQualSpeed": cucsProcessorQualSpeed,
       "cucsProcessorQualStepping": cucsProcessorQualStepping,
       "cucsProcessorRuntimeTable": cucsProcessorRuntimeTable,
       "cucsProcessorRuntimeEntry": cucsProcessorRuntimeEntry,
       "cucsProcessorRuntimeInstanceId": cucsProcessorRuntimeInstanceId,
       "cucsProcessorRuntimeDn": cucsProcessorRuntimeDn,
       "cucsProcessorRuntimeRn": cucsProcessorRuntimeRn,
       "cucsProcessorRuntimeIntervals": cucsProcessorRuntimeIntervals,
       "cucsProcessorRuntimeLoad": cucsProcessorRuntimeLoad,
       "cucsProcessorRuntimeLoadAvg": cucsProcessorRuntimeLoadAvg,
       "cucsProcessorRuntimeLoadMax": cucsProcessorRuntimeLoadMax,
       "cucsProcessorRuntimeLoadMin": cucsProcessorRuntimeLoadMin,
       "cucsProcessorRuntimeSuspect": cucsProcessorRuntimeSuspect,
       "cucsProcessorRuntimeThresholded": cucsProcessorRuntimeThresholded,
       "cucsProcessorRuntimeTimeCollected": cucsProcessorRuntimeTimeCollected,
       "cucsProcessorRuntimeUpdate": cucsProcessorRuntimeUpdate,
       "cucsProcessorRuntimeUptime": cucsProcessorRuntimeUptime,
       "cucsProcessorRuntimeHistTable": cucsProcessorRuntimeHistTable,
       "cucsProcessorRuntimeHistEntry": cucsProcessorRuntimeHistEntry,
       "cucsProcessorRuntimeHistInstanceId": cucsProcessorRuntimeHistInstanceId,
       "cucsProcessorRuntimeHistDn": cucsProcessorRuntimeHistDn,
       "cucsProcessorRuntimeHistRn": cucsProcessorRuntimeHistRn,
       "cucsProcessorRuntimeHistId": cucsProcessorRuntimeHistId,
       "cucsProcessorRuntimeHistLoad": cucsProcessorRuntimeHistLoad,
       "cucsProcessorRuntimeHistLoadAvg": cucsProcessorRuntimeHistLoadAvg,
       "cucsProcessorRuntimeHistLoadMax": cucsProcessorRuntimeHistLoadMax,
       "cucsProcessorRuntimeHistLoadMin": cucsProcessorRuntimeHistLoadMin,
       "cucsProcessorRuntimeHistMostRecent": cucsProcessorRuntimeHistMostRecent,
       "cucsProcessorRuntimeHistSuspect": cucsProcessorRuntimeHistSuspect,
       "cucsProcessorRuntimeHistThresholded": cucsProcessorRuntimeHistThresholded,
       "cucsProcessorRuntimeHistTimeCollected": cucsProcessorRuntimeHistTimeCollected,
       "cucsProcessorThreadTable": cucsProcessorThreadTable,
       "cucsProcessorThreadEntry": cucsProcessorThreadEntry,
       "cucsProcessorThreadInstanceId": cucsProcessorThreadInstanceId,
       "cucsProcessorThreadDn": cucsProcessorThreadDn,
       "cucsProcessorThreadRn": cucsProcessorThreadRn,
       "cucsProcessorThreadId": cucsProcessorThreadId,
       "cucsProcessorUnitTable": cucsProcessorUnitTable,
       "cucsProcessorUnitEntry": cucsProcessorUnitEntry,
       "cucsProcessorUnitInstanceId": cucsProcessorUnitInstanceId,
       "cucsProcessorUnitDn": cucsProcessorUnitDn,
       "cucsProcessorUnitRn": cucsProcessorUnitRn,
       "cucsProcessorUnitArch": cucsProcessorUnitArch,
       "cucsProcessorUnitCores": cucsProcessorUnitCores,
       "cucsProcessorUnitCoresEnabled": cucsProcessorUnitCoresEnabled,
       "cucsProcessorUnitId": cucsProcessorUnitId,
       "cucsProcessorUnitModel": cucsProcessorUnitModel,
       "cucsProcessorUnitOperState": cucsProcessorUnitOperState,
       "cucsProcessorUnitOperability": cucsProcessorUnitOperability,
       "cucsProcessorUnitPerf": cucsProcessorUnitPerf,
       "cucsProcessorUnitPower": cucsProcessorUnitPower,
       "cucsProcessorUnitPresence": cucsProcessorUnitPresence,
       "cucsProcessorUnitRevision": cucsProcessorUnitRevision,
       "cucsProcessorUnitSerial": cucsProcessorUnitSerial,
       "cucsProcessorUnitSocketDesignation": cucsProcessorUnitSocketDesignation,
       "cucsProcessorUnitSpeed": cucsProcessorUnitSpeed,
       "cucsProcessorUnitStepping": cucsProcessorUnitStepping,
       "cucsProcessorUnitThermal": cucsProcessorUnitThermal,
       "cucsProcessorUnitThreads": cucsProcessorUnitThreads,
       "cucsProcessorUnitVendor": cucsProcessorUnitVendor,
       "cucsProcessorUnitVoltage": cucsProcessorUnitVoltage,
       "cucsProcessorUnitVisibility": cucsProcessorUnitVisibility,
       "cucsProcessorUnitOperQualifierReason": cucsProcessorUnitOperQualifierReason,
       "cucsProcessorUnitLocationDn": cucsProcessorUnitLocationDn,
       "cucsProcessorUnitAssocCtxTable": cucsProcessorUnitAssocCtxTable,
       "cucsProcessorUnitAssocCtxEntry": cucsProcessorUnitAssocCtxEntry,
       "cucsProcessorUnitAssocCtxInstanceId": cucsProcessorUnitAssocCtxInstanceId,
       "cucsProcessorUnitAssocCtxDn": cucsProcessorUnitAssocCtxDn,
       "cucsProcessorUnitAssocCtxRn": cucsProcessorUnitAssocCtxRn,
       "cucsProcessorUnitAssocCtxFruCapDn": cucsProcessorUnitAssocCtxFruCapDn,
       "cucsProcessorUnitAssocCtxStepping": cucsProcessorUnitAssocCtxStepping}
)

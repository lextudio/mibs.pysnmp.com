# SNMP MIB module (CISCO-UNIFIED-COMPUTING-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-MEMORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:57 2024
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
 CucsMemoryAdminState,
 CucsMemoryArrayEnvStatsHistThresholded,
 CucsMemoryArrayEnvStatsThresholded,
 CucsMemoryArrayId,
 CucsMemoryBufferUnitEnvStatsHistThresholded,
 CucsMemoryBufferUnitEnvStatsThresholded,
 CucsMemoryBufferUnitId,
 CucsMemoryErrorCorrection,
 CucsMemoryErrorStatsThresholded,
 CucsMemoryFormFactor,
 CucsMemoryIssues,
 CucsMemoryRuntimeHistThresholded,
 CucsMemoryRuntimeThresholded,
 CucsMemoryRuntimeType,
 CucsMemoryType,
 CucsMemoryUnitEnvStatsHistThresholded,
 CucsMemoryUnitEnvStatsThresholded,
 CucsMemoryUnitId,
 CucsMemoryUnitOperability,
 CucsMemoryVisibility) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsEquipmentOperability",
    "CucsEquipmentPowerState",
    "CucsEquipmentPresence",
    "CucsEquipmentSensorThresholdStatus",
    "CucsMemoryAdminState",
    "CucsMemoryArrayEnvStatsHistThresholded",
    "CucsMemoryArrayEnvStatsThresholded",
    "CucsMemoryArrayId",
    "CucsMemoryBufferUnitEnvStatsHistThresholded",
    "CucsMemoryBufferUnitEnvStatsThresholded",
    "CucsMemoryBufferUnitId",
    "CucsMemoryErrorCorrection",
    "CucsMemoryErrorStatsThresholded",
    "CucsMemoryFormFactor",
    "CucsMemoryIssues",
    "CucsMemoryRuntimeHistThresholded",
    "CucsMemoryRuntimeThresholded",
    "CucsMemoryRuntimeType",
    "CucsMemoryType",
    "CucsMemoryUnitEnvStatsHistThresholded",
    "CucsMemoryUnitEnvStatsThresholded",
    "CucsMemoryUnitId",
    "CucsMemoryUnitOperability",
    "CucsMemoryVisibility")

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

cucsMemoryObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsMemoryArrayTable_Object = MibTable
cucsMemoryArrayTable = _CucsMemoryArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1)
)
if mibBuilder.loadTexts:
    cucsMemoryArrayTable.setStatus("current")
_CucsMemoryArrayEntry_Object = MibTableRow
cucsMemoryArrayEntry = _CucsMemoryArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1)
)
cucsMemoryArrayEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryArrayInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryArrayEntry.setStatus("current")
_CucsMemoryArrayInstanceId_Type = CucsManagedObjectId
_CucsMemoryArrayInstanceId_Object = MibTableColumn
cucsMemoryArrayInstanceId = _CucsMemoryArrayInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 1),
    _CucsMemoryArrayInstanceId_Type()
)
cucsMemoryArrayInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryArrayInstanceId.setStatus("current")
_CucsMemoryArrayDn_Type = CucsManagedObjectDn
_CucsMemoryArrayDn_Object = MibTableColumn
cucsMemoryArrayDn = _CucsMemoryArrayDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 2),
    _CucsMemoryArrayDn_Type()
)
cucsMemoryArrayDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayDn.setStatus("current")
_CucsMemoryArrayRn_Type = SnmpAdminString
_CucsMemoryArrayRn_Object = MibTableColumn
cucsMemoryArrayRn = _CucsMemoryArrayRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 3),
    _CucsMemoryArrayRn_Type()
)
cucsMemoryArrayRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayRn.setStatus("current")
_CucsMemoryArrayCpuId_Type = Gauge32
_CucsMemoryArrayCpuId_Object = MibTableColumn
cucsMemoryArrayCpuId = _CucsMemoryArrayCpuId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 4),
    _CucsMemoryArrayCpuId_Type()
)
cucsMemoryArrayCpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayCpuId.setStatus("current")
_CucsMemoryArrayCurrCapacity_Type = Gauge32
_CucsMemoryArrayCurrCapacity_Object = MibTableColumn
cucsMemoryArrayCurrCapacity = _CucsMemoryArrayCurrCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 5),
    _CucsMemoryArrayCurrCapacity_Type()
)
cucsMemoryArrayCurrCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayCurrCapacity.setStatus("current")
_CucsMemoryArrayErrorCorrection_Type = CucsMemoryErrorCorrection
_CucsMemoryArrayErrorCorrection_Object = MibTableColumn
cucsMemoryArrayErrorCorrection = _CucsMemoryArrayErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 6),
    _CucsMemoryArrayErrorCorrection_Type()
)
cucsMemoryArrayErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayErrorCorrection.setStatus("current")
_CucsMemoryArrayId_Type = CucsMemoryArrayId
_CucsMemoryArrayId_Object = MibTableColumn
cucsMemoryArrayId = _CucsMemoryArrayId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 7),
    _CucsMemoryArrayId_Type()
)
cucsMemoryArrayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayId.setStatus("current")
_CucsMemoryArrayMaxCapacity_Type = Gauge32
_CucsMemoryArrayMaxCapacity_Object = MibTableColumn
cucsMemoryArrayMaxCapacity = _CucsMemoryArrayMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 8),
    _CucsMemoryArrayMaxCapacity_Type()
)
cucsMemoryArrayMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayMaxCapacity.setStatus("current")
_CucsMemoryArrayMaxDevices_Type = Gauge32
_CucsMemoryArrayMaxDevices_Object = MibTableColumn
cucsMemoryArrayMaxDevices = _CucsMemoryArrayMaxDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 9),
    _CucsMemoryArrayMaxDevices_Type()
)
cucsMemoryArrayMaxDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayMaxDevices.setStatus("current")
_CucsMemoryArrayModel_Type = SnmpAdminString
_CucsMemoryArrayModel_Object = MibTableColumn
cucsMemoryArrayModel = _CucsMemoryArrayModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 10),
    _CucsMemoryArrayModel_Type()
)
cucsMemoryArrayModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayModel.setStatus("current")
_CucsMemoryArrayOperState_Type = CucsEquipmentOperability
_CucsMemoryArrayOperState_Object = MibTableColumn
cucsMemoryArrayOperState = _CucsMemoryArrayOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 11),
    _CucsMemoryArrayOperState_Type()
)
cucsMemoryArrayOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayOperState.setStatus("current")
_CucsMemoryArrayOperability_Type = CucsEquipmentOperability
_CucsMemoryArrayOperability_Object = MibTableColumn
cucsMemoryArrayOperability = _CucsMemoryArrayOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 12),
    _CucsMemoryArrayOperability_Type()
)
cucsMemoryArrayOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayOperability.setStatus("current")
_CucsMemoryArrayPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsMemoryArrayPerf_Object = MibTableColumn
cucsMemoryArrayPerf = _CucsMemoryArrayPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 13),
    _CucsMemoryArrayPerf_Type()
)
cucsMemoryArrayPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayPerf.setStatus("current")
_CucsMemoryArrayPopulated_Type = Gauge32
_CucsMemoryArrayPopulated_Object = MibTableColumn
cucsMemoryArrayPopulated = _CucsMemoryArrayPopulated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 14),
    _CucsMemoryArrayPopulated_Type()
)
cucsMemoryArrayPopulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayPopulated.setStatus("current")
_CucsMemoryArrayPower_Type = CucsEquipmentPowerState
_CucsMemoryArrayPower_Object = MibTableColumn
cucsMemoryArrayPower = _CucsMemoryArrayPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 15),
    _CucsMemoryArrayPower_Type()
)
cucsMemoryArrayPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayPower.setStatus("current")
_CucsMemoryArrayPresence_Type = CucsEquipmentPresence
_CucsMemoryArrayPresence_Object = MibTableColumn
cucsMemoryArrayPresence = _CucsMemoryArrayPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 16),
    _CucsMemoryArrayPresence_Type()
)
cucsMemoryArrayPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayPresence.setStatus("current")
_CucsMemoryArrayRevision_Type = SnmpAdminString
_CucsMemoryArrayRevision_Object = MibTableColumn
cucsMemoryArrayRevision = _CucsMemoryArrayRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 17),
    _CucsMemoryArrayRevision_Type()
)
cucsMemoryArrayRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayRevision.setStatus("current")
_CucsMemoryArraySerial_Type = SnmpAdminString
_CucsMemoryArraySerial_Object = MibTableColumn
cucsMemoryArraySerial = _CucsMemoryArraySerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 18),
    _CucsMemoryArraySerial_Type()
)
cucsMemoryArraySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArraySerial.setStatus("current")
_CucsMemoryArrayThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsMemoryArrayThermal_Object = MibTableColumn
cucsMemoryArrayThermal = _CucsMemoryArrayThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 19),
    _CucsMemoryArrayThermal_Type()
)
cucsMemoryArrayThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayThermal.setStatus("current")
_CucsMemoryArrayVendor_Type = SnmpAdminString
_CucsMemoryArrayVendor_Object = MibTableColumn
cucsMemoryArrayVendor = _CucsMemoryArrayVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 20),
    _CucsMemoryArrayVendor_Type()
)
cucsMemoryArrayVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayVendor.setStatus("current")
_CucsMemoryArrayVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsMemoryArrayVoltage_Object = MibTableColumn
cucsMemoryArrayVoltage = _CucsMemoryArrayVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 21),
    _CucsMemoryArrayVoltage_Type()
)
cucsMemoryArrayVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayVoltage.setStatus("current")
_CucsMemoryArrayOperQualifierReason_Type = SnmpAdminString
_CucsMemoryArrayOperQualifierReason_Object = MibTableColumn
cucsMemoryArrayOperQualifierReason = _CucsMemoryArrayOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 22),
    _CucsMemoryArrayOperQualifierReason_Type()
)
cucsMemoryArrayOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayOperQualifierReason.setStatus("current")
_CucsMemoryArrayLocationDn_Type = SnmpAdminString
_CucsMemoryArrayLocationDn_Object = MibTableColumn
cucsMemoryArrayLocationDn = _CucsMemoryArrayLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 1, 1, 23),
    _CucsMemoryArrayLocationDn_Type()
)
cucsMemoryArrayLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayLocationDn.setStatus("current")
_CucsMemoryArrayEnvStatsTable_Object = MibTable
cucsMemoryArrayEnvStatsTable = _CucsMemoryArrayEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2)
)
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsTable.setStatus("current")
_CucsMemoryArrayEnvStatsEntry_Object = MibTableRow
cucsMemoryArrayEnvStatsEntry = _CucsMemoryArrayEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1)
)
cucsMemoryArrayEnvStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryArrayEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsEntry.setStatus("current")
_CucsMemoryArrayEnvStatsInstanceId_Type = CucsManagedObjectId
_CucsMemoryArrayEnvStatsInstanceId_Object = MibTableColumn
cucsMemoryArrayEnvStatsInstanceId = _CucsMemoryArrayEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 1),
    _CucsMemoryArrayEnvStatsInstanceId_Type()
)
cucsMemoryArrayEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsInstanceId.setStatus("current")
_CucsMemoryArrayEnvStatsDn_Type = CucsManagedObjectDn
_CucsMemoryArrayEnvStatsDn_Object = MibTableColumn
cucsMemoryArrayEnvStatsDn = _CucsMemoryArrayEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 2),
    _CucsMemoryArrayEnvStatsDn_Type()
)
cucsMemoryArrayEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsDn.setStatus("current")
_CucsMemoryArrayEnvStatsRn_Type = SnmpAdminString
_CucsMemoryArrayEnvStatsRn_Object = MibTableColumn
cucsMemoryArrayEnvStatsRn = _CucsMemoryArrayEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 3),
    _CucsMemoryArrayEnvStatsRn_Type()
)
cucsMemoryArrayEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsRn.setStatus("current")
_CucsMemoryArrayEnvStatsInputCurrent_Type = Integer32
_CucsMemoryArrayEnvStatsInputCurrent_Object = MibTableColumn
cucsMemoryArrayEnvStatsInputCurrent = _CucsMemoryArrayEnvStatsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 4),
    _CucsMemoryArrayEnvStatsInputCurrent_Type()
)
cucsMemoryArrayEnvStatsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsInputCurrent.setStatus("current")
_CucsMemoryArrayEnvStatsInputCurrentAvg_Type = Integer32
_CucsMemoryArrayEnvStatsInputCurrentAvg_Object = MibTableColumn
cucsMemoryArrayEnvStatsInputCurrentAvg = _CucsMemoryArrayEnvStatsInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 5),
    _CucsMemoryArrayEnvStatsInputCurrentAvg_Type()
)
cucsMemoryArrayEnvStatsInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsInputCurrentAvg.setStatus("current")
_CucsMemoryArrayEnvStatsInputCurrentMax_Type = Integer32
_CucsMemoryArrayEnvStatsInputCurrentMax_Object = MibTableColumn
cucsMemoryArrayEnvStatsInputCurrentMax = _CucsMemoryArrayEnvStatsInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 6),
    _CucsMemoryArrayEnvStatsInputCurrentMax_Type()
)
cucsMemoryArrayEnvStatsInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsInputCurrentMax.setStatus("current")
_CucsMemoryArrayEnvStatsInputCurrentMin_Type = Integer32
_CucsMemoryArrayEnvStatsInputCurrentMin_Object = MibTableColumn
cucsMemoryArrayEnvStatsInputCurrentMin = _CucsMemoryArrayEnvStatsInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 7),
    _CucsMemoryArrayEnvStatsInputCurrentMin_Type()
)
cucsMemoryArrayEnvStatsInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsInputCurrentMin.setStatus("current")
_CucsMemoryArrayEnvStatsIntervals_Type = Gauge32
_CucsMemoryArrayEnvStatsIntervals_Object = MibTableColumn
cucsMemoryArrayEnvStatsIntervals = _CucsMemoryArrayEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 8),
    _CucsMemoryArrayEnvStatsIntervals_Type()
)
cucsMemoryArrayEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsIntervals.setStatus("current")
_CucsMemoryArrayEnvStatsSuspect_Type = TruthValue
_CucsMemoryArrayEnvStatsSuspect_Object = MibTableColumn
cucsMemoryArrayEnvStatsSuspect = _CucsMemoryArrayEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 9),
    _CucsMemoryArrayEnvStatsSuspect_Type()
)
cucsMemoryArrayEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsSuspect.setStatus("current")
_CucsMemoryArrayEnvStatsThresholded_Type = CucsMemoryArrayEnvStatsThresholded
_CucsMemoryArrayEnvStatsThresholded_Object = MibTableColumn
cucsMemoryArrayEnvStatsThresholded = _CucsMemoryArrayEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 10),
    _CucsMemoryArrayEnvStatsThresholded_Type()
)
cucsMemoryArrayEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsThresholded.setStatus("current")
_CucsMemoryArrayEnvStatsTimeCollected_Type = DateAndTime
_CucsMemoryArrayEnvStatsTimeCollected_Object = MibTableColumn
cucsMemoryArrayEnvStatsTimeCollected = _CucsMemoryArrayEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 11),
    _CucsMemoryArrayEnvStatsTimeCollected_Type()
)
cucsMemoryArrayEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsTimeCollected.setStatus("current")
_CucsMemoryArrayEnvStatsUpdate_Type = Gauge32
_CucsMemoryArrayEnvStatsUpdate_Object = MibTableColumn
cucsMemoryArrayEnvStatsUpdate = _CucsMemoryArrayEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 2, 1, 12),
    _CucsMemoryArrayEnvStatsUpdate_Type()
)
cucsMemoryArrayEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsUpdate.setStatus("current")
_CucsMemoryArrayEnvStatsHistTable_Object = MibTable
cucsMemoryArrayEnvStatsHistTable = _CucsMemoryArrayEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3)
)
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistTable.setStatus("current")
_CucsMemoryArrayEnvStatsHistEntry_Object = MibTableRow
cucsMemoryArrayEnvStatsHistEntry = _CucsMemoryArrayEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1)
)
cucsMemoryArrayEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryArrayEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistEntry.setStatus("current")
_CucsMemoryArrayEnvStatsHistInstanceId_Type = CucsManagedObjectId
_CucsMemoryArrayEnvStatsHistInstanceId_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistInstanceId = _CucsMemoryArrayEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 1),
    _CucsMemoryArrayEnvStatsHistInstanceId_Type()
)
cucsMemoryArrayEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistInstanceId.setStatus("current")
_CucsMemoryArrayEnvStatsHistDn_Type = CucsManagedObjectDn
_CucsMemoryArrayEnvStatsHistDn_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistDn = _CucsMemoryArrayEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 2),
    _CucsMemoryArrayEnvStatsHistDn_Type()
)
cucsMemoryArrayEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistDn.setStatus("current")
_CucsMemoryArrayEnvStatsHistRn_Type = SnmpAdminString
_CucsMemoryArrayEnvStatsHistRn_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistRn = _CucsMemoryArrayEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 3),
    _CucsMemoryArrayEnvStatsHistRn_Type()
)
cucsMemoryArrayEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistRn.setStatus("current")
_CucsMemoryArrayEnvStatsHistId_Type = Unsigned64
_CucsMemoryArrayEnvStatsHistId_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistId = _CucsMemoryArrayEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 4),
    _CucsMemoryArrayEnvStatsHistId_Type()
)
cucsMemoryArrayEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistId.setStatus("current")
_CucsMemoryArrayEnvStatsHistInputCurrent_Type = Integer32
_CucsMemoryArrayEnvStatsHistInputCurrent_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistInputCurrent = _CucsMemoryArrayEnvStatsHistInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 5),
    _CucsMemoryArrayEnvStatsHistInputCurrent_Type()
)
cucsMemoryArrayEnvStatsHistInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistInputCurrent.setStatus("current")
_CucsMemoryArrayEnvStatsHistInputCurrentAvg_Type = Integer32
_CucsMemoryArrayEnvStatsHistInputCurrentAvg_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistInputCurrentAvg = _CucsMemoryArrayEnvStatsHistInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 6),
    _CucsMemoryArrayEnvStatsHistInputCurrentAvg_Type()
)
cucsMemoryArrayEnvStatsHistInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistInputCurrentAvg.setStatus("current")
_CucsMemoryArrayEnvStatsHistInputCurrentMax_Type = Integer32
_CucsMemoryArrayEnvStatsHistInputCurrentMax_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistInputCurrentMax = _CucsMemoryArrayEnvStatsHistInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 7),
    _CucsMemoryArrayEnvStatsHistInputCurrentMax_Type()
)
cucsMemoryArrayEnvStatsHistInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistInputCurrentMax.setStatus("current")
_CucsMemoryArrayEnvStatsHistInputCurrentMin_Type = Integer32
_CucsMemoryArrayEnvStatsHistInputCurrentMin_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistInputCurrentMin = _CucsMemoryArrayEnvStatsHistInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 8),
    _CucsMemoryArrayEnvStatsHistInputCurrentMin_Type()
)
cucsMemoryArrayEnvStatsHistInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistInputCurrentMin.setStatus("current")
_CucsMemoryArrayEnvStatsHistMostRecent_Type = TruthValue
_CucsMemoryArrayEnvStatsHistMostRecent_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistMostRecent = _CucsMemoryArrayEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 9),
    _CucsMemoryArrayEnvStatsHistMostRecent_Type()
)
cucsMemoryArrayEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistMostRecent.setStatus("current")
_CucsMemoryArrayEnvStatsHistSuspect_Type = TruthValue
_CucsMemoryArrayEnvStatsHistSuspect_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistSuspect = _CucsMemoryArrayEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 10),
    _CucsMemoryArrayEnvStatsHistSuspect_Type()
)
cucsMemoryArrayEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistSuspect.setStatus("current")
_CucsMemoryArrayEnvStatsHistThresholded_Type = CucsMemoryArrayEnvStatsHistThresholded
_CucsMemoryArrayEnvStatsHistThresholded_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistThresholded = _CucsMemoryArrayEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 11),
    _CucsMemoryArrayEnvStatsHistThresholded_Type()
)
cucsMemoryArrayEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistThresholded.setStatus("current")
_CucsMemoryArrayEnvStatsHistTimeCollected_Type = DateAndTime
_CucsMemoryArrayEnvStatsHistTimeCollected_Object = MibTableColumn
cucsMemoryArrayEnvStatsHistTimeCollected = _CucsMemoryArrayEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 3, 1, 12),
    _CucsMemoryArrayEnvStatsHistTimeCollected_Type()
)
cucsMemoryArrayEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryArrayEnvStatsHistTimeCollected.setStatus("current")
_CucsMemoryBufferUnitTable_Object = MibTable
cucsMemoryBufferUnitTable = _CucsMemoryBufferUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4)
)
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitTable.setStatus("current")
_CucsMemoryBufferUnitEntry_Object = MibTableRow
cucsMemoryBufferUnitEntry = _CucsMemoryBufferUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1)
)
cucsMemoryBufferUnitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryBufferUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEntry.setStatus("current")
_CucsMemoryBufferUnitInstanceId_Type = CucsManagedObjectId
_CucsMemoryBufferUnitInstanceId_Object = MibTableColumn
cucsMemoryBufferUnitInstanceId = _CucsMemoryBufferUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 1),
    _CucsMemoryBufferUnitInstanceId_Type()
)
cucsMemoryBufferUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitInstanceId.setStatus("current")
_CucsMemoryBufferUnitDn_Type = CucsManagedObjectDn
_CucsMemoryBufferUnitDn_Object = MibTableColumn
cucsMemoryBufferUnitDn = _CucsMemoryBufferUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 2),
    _CucsMemoryBufferUnitDn_Type()
)
cucsMemoryBufferUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitDn.setStatus("current")
_CucsMemoryBufferUnitRn_Type = SnmpAdminString
_CucsMemoryBufferUnitRn_Object = MibTableColumn
cucsMemoryBufferUnitRn = _CucsMemoryBufferUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 3),
    _CucsMemoryBufferUnitRn_Type()
)
cucsMemoryBufferUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitRn.setStatus("current")
_CucsMemoryBufferUnitId_Type = CucsMemoryBufferUnitId
_CucsMemoryBufferUnitId_Object = MibTableColumn
cucsMemoryBufferUnitId = _CucsMemoryBufferUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 4),
    _CucsMemoryBufferUnitId_Type()
)
cucsMemoryBufferUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitId.setStatus("current")
_CucsMemoryBufferUnitModel_Type = SnmpAdminString
_CucsMemoryBufferUnitModel_Object = MibTableColumn
cucsMemoryBufferUnitModel = _CucsMemoryBufferUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 5),
    _CucsMemoryBufferUnitModel_Type()
)
cucsMemoryBufferUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitModel.setStatus("current")
_CucsMemoryBufferUnitOperState_Type = CucsEquipmentOperability
_CucsMemoryBufferUnitOperState_Object = MibTableColumn
cucsMemoryBufferUnitOperState = _CucsMemoryBufferUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 6),
    _CucsMemoryBufferUnitOperState_Type()
)
cucsMemoryBufferUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitOperState.setStatus("current")
_CucsMemoryBufferUnitOperability_Type = CucsEquipmentOperability
_CucsMemoryBufferUnitOperability_Object = MibTableColumn
cucsMemoryBufferUnitOperability = _CucsMemoryBufferUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 7),
    _CucsMemoryBufferUnitOperability_Type()
)
cucsMemoryBufferUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitOperability.setStatus("current")
_CucsMemoryBufferUnitPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsMemoryBufferUnitPerf_Object = MibTableColumn
cucsMemoryBufferUnitPerf = _CucsMemoryBufferUnitPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 8),
    _CucsMemoryBufferUnitPerf_Type()
)
cucsMemoryBufferUnitPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitPerf.setStatus("current")
_CucsMemoryBufferUnitPower_Type = CucsEquipmentPowerState
_CucsMemoryBufferUnitPower_Object = MibTableColumn
cucsMemoryBufferUnitPower = _CucsMemoryBufferUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 9),
    _CucsMemoryBufferUnitPower_Type()
)
cucsMemoryBufferUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitPower.setStatus("current")
_CucsMemoryBufferUnitPresence_Type = CucsEquipmentPresence
_CucsMemoryBufferUnitPresence_Object = MibTableColumn
cucsMemoryBufferUnitPresence = _CucsMemoryBufferUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 10),
    _CucsMemoryBufferUnitPresence_Type()
)
cucsMemoryBufferUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitPresence.setStatus("current")
_CucsMemoryBufferUnitRevision_Type = SnmpAdminString
_CucsMemoryBufferUnitRevision_Object = MibTableColumn
cucsMemoryBufferUnitRevision = _CucsMemoryBufferUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 11),
    _CucsMemoryBufferUnitRevision_Type()
)
cucsMemoryBufferUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitRevision.setStatus("current")
_CucsMemoryBufferUnitSerial_Type = SnmpAdminString
_CucsMemoryBufferUnitSerial_Object = MibTableColumn
cucsMemoryBufferUnitSerial = _CucsMemoryBufferUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 12),
    _CucsMemoryBufferUnitSerial_Type()
)
cucsMemoryBufferUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitSerial.setStatus("current")
_CucsMemoryBufferUnitThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsMemoryBufferUnitThermal_Object = MibTableColumn
cucsMemoryBufferUnitThermal = _CucsMemoryBufferUnitThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 13),
    _CucsMemoryBufferUnitThermal_Type()
)
cucsMemoryBufferUnitThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitThermal.setStatus("current")
_CucsMemoryBufferUnitVendor_Type = SnmpAdminString
_CucsMemoryBufferUnitVendor_Object = MibTableColumn
cucsMemoryBufferUnitVendor = _CucsMemoryBufferUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 14),
    _CucsMemoryBufferUnitVendor_Type()
)
cucsMemoryBufferUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitVendor.setStatus("current")
_CucsMemoryBufferUnitVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsMemoryBufferUnitVoltage_Object = MibTableColumn
cucsMemoryBufferUnitVoltage = _CucsMemoryBufferUnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 15),
    _CucsMemoryBufferUnitVoltage_Type()
)
cucsMemoryBufferUnitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitVoltage.setStatus("current")
_CucsMemoryBufferUnitOperQualifierReason_Type = SnmpAdminString
_CucsMemoryBufferUnitOperQualifierReason_Object = MibTableColumn
cucsMemoryBufferUnitOperQualifierReason = _CucsMemoryBufferUnitOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 16),
    _CucsMemoryBufferUnitOperQualifierReason_Type()
)
cucsMemoryBufferUnitOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitOperQualifierReason.setStatus("current")
_CucsMemoryBufferUnitLocationDn_Type = SnmpAdminString
_CucsMemoryBufferUnitLocationDn_Object = MibTableColumn
cucsMemoryBufferUnitLocationDn = _CucsMemoryBufferUnitLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 4, 1, 17),
    _CucsMemoryBufferUnitLocationDn_Type()
)
cucsMemoryBufferUnitLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitLocationDn.setStatus("current")
_CucsMemoryBufferUnitEnvStatsTable_Object = MibTable
cucsMemoryBufferUnitEnvStatsTable = _CucsMemoryBufferUnitEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5)
)
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsTable.setStatus("current")
_CucsMemoryBufferUnitEnvStatsEntry_Object = MibTableRow
cucsMemoryBufferUnitEnvStatsEntry = _CucsMemoryBufferUnitEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1)
)
cucsMemoryBufferUnitEnvStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryBufferUnitEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsEntry.setStatus("current")
_CucsMemoryBufferUnitEnvStatsInstanceId_Type = CucsManagedObjectId
_CucsMemoryBufferUnitEnvStatsInstanceId_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsInstanceId = _CucsMemoryBufferUnitEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 1),
    _CucsMemoryBufferUnitEnvStatsInstanceId_Type()
)
cucsMemoryBufferUnitEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsInstanceId.setStatus("current")
_CucsMemoryBufferUnitEnvStatsDn_Type = CucsManagedObjectDn
_CucsMemoryBufferUnitEnvStatsDn_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsDn = _CucsMemoryBufferUnitEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 2),
    _CucsMemoryBufferUnitEnvStatsDn_Type()
)
cucsMemoryBufferUnitEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsDn.setStatus("current")
_CucsMemoryBufferUnitEnvStatsRn_Type = SnmpAdminString
_CucsMemoryBufferUnitEnvStatsRn_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsRn = _CucsMemoryBufferUnitEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 3),
    _CucsMemoryBufferUnitEnvStatsRn_Type()
)
cucsMemoryBufferUnitEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsRn.setStatus("current")
_CucsMemoryBufferUnitEnvStatsIntervals_Type = Gauge32
_CucsMemoryBufferUnitEnvStatsIntervals_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsIntervals = _CucsMemoryBufferUnitEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 4),
    _CucsMemoryBufferUnitEnvStatsIntervals_Type()
)
cucsMemoryBufferUnitEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsIntervals.setStatus("current")
_CucsMemoryBufferUnitEnvStatsSuspect_Type = TruthValue
_CucsMemoryBufferUnitEnvStatsSuspect_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsSuspect = _CucsMemoryBufferUnitEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 5),
    _CucsMemoryBufferUnitEnvStatsSuspect_Type()
)
cucsMemoryBufferUnitEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsSuspect.setStatus("current")
_CucsMemoryBufferUnitEnvStatsTemperature_Type = Integer32
_CucsMemoryBufferUnitEnvStatsTemperature_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsTemperature = _CucsMemoryBufferUnitEnvStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 6),
    _CucsMemoryBufferUnitEnvStatsTemperature_Type()
)
cucsMemoryBufferUnitEnvStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsTemperature.setStatus("current")
_CucsMemoryBufferUnitEnvStatsTemperatureAvg_Type = Integer32
_CucsMemoryBufferUnitEnvStatsTemperatureAvg_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsTemperatureAvg = _CucsMemoryBufferUnitEnvStatsTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 7),
    _CucsMemoryBufferUnitEnvStatsTemperatureAvg_Type()
)
cucsMemoryBufferUnitEnvStatsTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsTemperatureAvg.setStatus("current")
_CucsMemoryBufferUnitEnvStatsTemperatureMax_Type = Integer32
_CucsMemoryBufferUnitEnvStatsTemperatureMax_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsTemperatureMax = _CucsMemoryBufferUnitEnvStatsTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 8),
    _CucsMemoryBufferUnitEnvStatsTemperatureMax_Type()
)
cucsMemoryBufferUnitEnvStatsTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsTemperatureMax.setStatus("current")
_CucsMemoryBufferUnitEnvStatsTemperatureMin_Type = Integer32
_CucsMemoryBufferUnitEnvStatsTemperatureMin_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsTemperatureMin = _CucsMemoryBufferUnitEnvStatsTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 9),
    _CucsMemoryBufferUnitEnvStatsTemperatureMin_Type()
)
cucsMemoryBufferUnitEnvStatsTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsTemperatureMin.setStatus("current")
_CucsMemoryBufferUnitEnvStatsThresholded_Type = CucsMemoryBufferUnitEnvStatsThresholded
_CucsMemoryBufferUnitEnvStatsThresholded_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsThresholded = _CucsMemoryBufferUnitEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 10),
    _CucsMemoryBufferUnitEnvStatsThresholded_Type()
)
cucsMemoryBufferUnitEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsThresholded.setStatus("current")
_CucsMemoryBufferUnitEnvStatsTimeCollected_Type = DateAndTime
_CucsMemoryBufferUnitEnvStatsTimeCollected_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsTimeCollected = _CucsMemoryBufferUnitEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 11),
    _CucsMemoryBufferUnitEnvStatsTimeCollected_Type()
)
cucsMemoryBufferUnitEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsTimeCollected.setStatus("current")
_CucsMemoryBufferUnitEnvStatsUpdate_Type = Gauge32
_CucsMemoryBufferUnitEnvStatsUpdate_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsUpdate = _CucsMemoryBufferUnitEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 5, 1, 12),
    _CucsMemoryBufferUnitEnvStatsUpdate_Type()
)
cucsMemoryBufferUnitEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsUpdate.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistTable_Object = MibTable
cucsMemoryBufferUnitEnvStatsHistTable = _CucsMemoryBufferUnitEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6)
)
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistTable.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistEntry_Object = MibTableRow
cucsMemoryBufferUnitEnvStatsHistEntry = _CucsMemoryBufferUnitEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1)
)
cucsMemoryBufferUnitEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryBufferUnitEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistEntry.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistInstanceId_Type = CucsManagedObjectId
_CucsMemoryBufferUnitEnvStatsHistInstanceId_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistInstanceId = _CucsMemoryBufferUnitEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 1),
    _CucsMemoryBufferUnitEnvStatsHistInstanceId_Type()
)
cucsMemoryBufferUnitEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistInstanceId.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistDn_Type = CucsManagedObjectDn
_CucsMemoryBufferUnitEnvStatsHistDn_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistDn = _CucsMemoryBufferUnitEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 2),
    _CucsMemoryBufferUnitEnvStatsHistDn_Type()
)
cucsMemoryBufferUnitEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistDn.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistRn_Type = SnmpAdminString
_CucsMemoryBufferUnitEnvStatsHistRn_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistRn = _CucsMemoryBufferUnitEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 3),
    _CucsMemoryBufferUnitEnvStatsHistRn_Type()
)
cucsMemoryBufferUnitEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistRn.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistId_Type = Unsigned64
_CucsMemoryBufferUnitEnvStatsHistId_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistId = _CucsMemoryBufferUnitEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 4),
    _CucsMemoryBufferUnitEnvStatsHistId_Type()
)
cucsMemoryBufferUnitEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistId.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistMostRecent_Type = TruthValue
_CucsMemoryBufferUnitEnvStatsHistMostRecent_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistMostRecent = _CucsMemoryBufferUnitEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 5),
    _CucsMemoryBufferUnitEnvStatsHistMostRecent_Type()
)
cucsMemoryBufferUnitEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistMostRecent.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistSuspect_Type = TruthValue
_CucsMemoryBufferUnitEnvStatsHistSuspect_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistSuspect = _CucsMemoryBufferUnitEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 6),
    _CucsMemoryBufferUnitEnvStatsHistSuspect_Type()
)
cucsMemoryBufferUnitEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistSuspect.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistTemperature_Type = Integer32
_CucsMemoryBufferUnitEnvStatsHistTemperature_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistTemperature = _CucsMemoryBufferUnitEnvStatsHistTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 7),
    _CucsMemoryBufferUnitEnvStatsHistTemperature_Type()
)
cucsMemoryBufferUnitEnvStatsHistTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistTemperature.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistTemperatureAvg_Type = Integer32
_CucsMemoryBufferUnitEnvStatsHistTemperatureAvg_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistTemperatureAvg = _CucsMemoryBufferUnitEnvStatsHistTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 8),
    _CucsMemoryBufferUnitEnvStatsHistTemperatureAvg_Type()
)
cucsMemoryBufferUnitEnvStatsHistTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistTemperatureAvg.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistTemperatureMax_Type = Integer32
_CucsMemoryBufferUnitEnvStatsHistTemperatureMax_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistTemperatureMax = _CucsMemoryBufferUnitEnvStatsHistTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 9),
    _CucsMemoryBufferUnitEnvStatsHistTemperatureMax_Type()
)
cucsMemoryBufferUnitEnvStatsHistTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistTemperatureMax.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistTemperatureMin_Type = Integer32
_CucsMemoryBufferUnitEnvStatsHistTemperatureMin_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistTemperatureMin = _CucsMemoryBufferUnitEnvStatsHistTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 10),
    _CucsMemoryBufferUnitEnvStatsHistTemperatureMin_Type()
)
cucsMemoryBufferUnitEnvStatsHistTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistTemperatureMin.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistThresholded_Type = CucsMemoryBufferUnitEnvStatsHistThresholded
_CucsMemoryBufferUnitEnvStatsHistThresholded_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistThresholded = _CucsMemoryBufferUnitEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 11),
    _CucsMemoryBufferUnitEnvStatsHistThresholded_Type()
)
cucsMemoryBufferUnitEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistThresholded.setStatus("current")
_CucsMemoryBufferUnitEnvStatsHistTimeCollected_Type = DateAndTime
_CucsMemoryBufferUnitEnvStatsHistTimeCollected_Object = MibTableColumn
cucsMemoryBufferUnitEnvStatsHistTimeCollected = _CucsMemoryBufferUnitEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 6, 1, 12),
    _CucsMemoryBufferUnitEnvStatsHistTimeCollected_Type()
)
cucsMemoryBufferUnitEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryBufferUnitEnvStatsHistTimeCollected.setStatus("current")
_CucsMemoryErrorStatsTable_Object = MibTable
cucsMemoryErrorStatsTable = _CucsMemoryErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7)
)
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsTable.setStatus("current")
_CucsMemoryErrorStatsEntry_Object = MibTableRow
cucsMemoryErrorStatsEntry = _CucsMemoryErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1)
)
cucsMemoryErrorStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryErrorStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEntry.setStatus("current")
_CucsMemoryErrorStatsInstanceId_Type = CucsManagedObjectId
_CucsMemoryErrorStatsInstanceId_Object = MibTableColumn
cucsMemoryErrorStatsInstanceId = _CucsMemoryErrorStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 1),
    _CucsMemoryErrorStatsInstanceId_Type()
)
cucsMemoryErrorStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsInstanceId.setStatus("current")
_CucsMemoryErrorStatsDn_Type = CucsManagedObjectDn
_CucsMemoryErrorStatsDn_Object = MibTableColumn
cucsMemoryErrorStatsDn = _CucsMemoryErrorStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 2),
    _CucsMemoryErrorStatsDn_Type()
)
cucsMemoryErrorStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsDn.setStatus("current")
_CucsMemoryErrorStatsRn_Type = SnmpAdminString
_CucsMemoryErrorStatsRn_Object = MibTableColumn
cucsMemoryErrorStatsRn = _CucsMemoryErrorStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 3),
    _CucsMemoryErrorStatsRn_Type()
)
cucsMemoryErrorStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsRn.setStatus("current")
_CucsMemoryErrorStatsAddressParityErrors_Type = Counter32
_CucsMemoryErrorStatsAddressParityErrors_Object = MibTableColumn
cucsMemoryErrorStatsAddressParityErrors = _CucsMemoryErrorStatsAddressParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 4),
    _CucsMemoryErrorStatsAddressParityErrors_Type()
)
cucsMemoryErrorStatsAddressParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsAddressParityErrors.setStatus("current")
_CucsMemoryErrorStatsAddressParityErrors15Min_Type = Gauge32
_CucsMemoryErrorStatsAddressParityErrors15Min_Object = MibTableColumn
cucsMemoryErrorStatsAddressParityErrors15Min = _CucsMemoryErrorStatsAddressParityErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 5),
    _CucsMemoryErrorStatsAddressParityErrors15Min_Type()
)
cucsMemoryErrorStatsAddressParityErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsAddressParityErrors15Min.setStatus("current")
_CucsMemoryErrorStatsAddressParityErrors15MinH_Type = Gauge32
_CucsMemoryErrorStatsAddressParityErrors15MinH_Object = MibTableColumn
cucsMemoryErrorStatsAddressParityErrors15MinH = _CucsMemoryErrorStatsAddressParityErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 6),
    _CucsMemoryErrorStatsAddressParityErrors15MinH_Type()
)
cucsMemoryErrorStatsAddressParityErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsAddressParityErrors15MinH.setStatus("current")
_CucsMemoryErrorStatsAddressParityErrors1Day_Type = Gauge32
_CucsMemoryErrorStatsAddressParityErrors1Day_Object = MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1Day = _CucsMemoryErrorStatsAddressParityErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 7),
    _CucsMemoryErrorStatsAddressParityErrors1Day_Type()
)
cucsMemoryErrorStatsAddressParityErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsAddressParityErrors1Day.setStatus("current")
_CucsMemoryErrorStatsAddressParityErrors1DayH_Type = Gauge32
_CucsMemoryErrorStatsAddressParityErrors1DayH_Object = MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1DayH = _CucsMemoryErrorStatsAddressParityErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 8),
    _CucsMemoryErrorStatsAddressParityErrors1DayH_Type()
)
cucsMemoryErrorStatsAddressParityErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsAddressParityErrors1DayH.setStatus("current")
_CucsMemoryErrorStatsAddressParityErrors1Hour_Type = Gauge32
_CucsMemoryErrorStatsAddressParityErrors1Hour_Object = MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1Hour = _CucsMemoryErrorStatsAddressParityErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 9),
    _CucsMemoryErrorStatsAddressParityErrors1Hour_Type()
)
cucsMemoryErrorStatsAddressParityErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsAddressParityErrors1Hour.setStatus("current")
_CucsMemoryErrorStatsAddressParityErrors1HourH_Type = Gauge32
_CucsMemoryErrorStatsAddressParityErrors1HourH_Object = MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1HourH = _CucsMemoryErrorStatsAddressParityErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 10),
    _CucsMemoryErrorStatsAddressParityErrors1HourH_Type()
)
cucsMemoryErrorStatsAddressParityErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsAddressParityErrors1HourH.setStatus("current")
_CucsMemoryErrorStatsAddressParityErrors1Week_Type = Gauge32
_CucsMemoryErrorStatsAddressParityErrors1Week_Object = MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1Week = _CucsMemoryErrorStatsAddressParityErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 11),
    _CucsMemoryErrorStatsAddressParityErrors1Week_Type()
)
cucsMemoryErrorStatsAddressParityErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsAddressParityErrors1Week.setStatus("current")
_CucsMemoryErrorStatsAddressParityErrors1WeekH_Type = Gauge32
_CucsMemoryErrorStatsAddressParityErrors1WeekH_Object = MibTableColumn
cucsMemoryErrorStatsAddressParityErrors1WeekH = _CucsMemoryErrorStatsAddressParityErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 12),
    _CucsMemoryErrorStatsAddressParityErrors1WeekH_Type()
)
cucsMemoryErrorStatsAddressParityErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsAddressParityErrors1WeekH.setStatus("current")
_CucsMemoryErrorStatsEccMultibitErrors_Type = Counter32
_CucsMemoryErrorStatsEccMultibitErrors_Object = MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors = _CucsMemoryErrorStatsEccMultibitErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 13),
    _CucsMemoryErrorStatsEccMultibitErrors_Type()
)
cucsMemoryErrorStatsEccMultibitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccMultibitErrors.setStatus("current")
_CucsMemoryErrorStatsEccMultibitErrors15Min_Type = Gauge32
_CucsMemoryErrorStatsEccMultibitErrors15Min_Object = MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors15Min = _CucsMemoryErrorStatsEccMultibitErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 14),
    _CucsMemoryErrorStatsEccMultibitErrors15Min_Type()
)
cucsMemoryErrorStatsEccMultibitErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccMultibitErrors15Min.setStatus("current")
_CucsMemoryErrorStatsEccMultibitErrors15MinH_Type = Gauge32
_CucsMemoryErrorStatsEccMultibitErrors15MinH_Object = MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors15MinH = _CucsMemoryErrorStatsEccMultibitErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 15),
    _CucsMemoryErrorStatsEccMultibitErrors15MinH_Type()
)
cucsMemoryErrorStatsEccMultibitErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccMultibitErrors15MinH.setStatus("current")
_CucsMemoryErrorStatsEccMultibitErrors1Day_Type = Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1Day_Object = MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1Day = _CucsMemoryErrorStatsEccMultibitErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 16),
    _CucsMemoryErrorStatsEccMultibitErrors1Day_Type()
)
cucsMemoryErrorStatsEccMultibitErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccMultibitErrors1Day.setStatus("current")
_CucsMemoryErrorStatsEccMultibitErrors1DayH_Type = Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1DayH_Object = MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1DayH = _CucsMemoryErrorStatsEccMultibitErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 17),
    _CucsMemoryErrorStatsEccMultibitErrors1DayH_Type()
)
cucsMemoryErrorStatsEccMultibitErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccMultibitErrors1DayH.setStatus("current")
_CucsMemoryErrorStatsEccMultibitErrors1Hour_Type = Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1Hour_Object = MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1Hour = _CucsMemoryErrorStatsEccMultibitErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 18),
    _CucsMemoryErrorStatsEccMultibitErrors1Hour_Type()
)
cucsMemoryErrorStatsEccMultibitErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccMultibitErrors1Hour.setStatus("current")
_CucsMemoryErrorStatsEccMultibitErrors1HourH_Type = Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1HourH_Object = MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1HourH = _CucsMemoryErrorStatsEccMultibitErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 19),
    _CucsMemoryErrorStatsEccMultibitErrors1HourH_Type()
)
cucsMemoryErrorStatsEccMultibitErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccMultibitErrors1HourH.setStatus("current")
_CucsMemoryErrorStatsEccMultibitErrors1Week_Type = Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1Week_Object = MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1Week = _CucsMemoryErrorStatsEccMultibitErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 20),
    _CucsMemoryErrorStatsEccMultibitErrors1Week_Type()
)
cucsMemoryErrorStatsEccMultibitErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccMultibitErrors1Week.setStatus("current")
_CucsMemoryErrorStatsEccMultibitErrors1WeekH_Type = Gauge32
_CucsMemoryErrorStatsEccMultibitErrors1WeekH_Object = MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors1WeekH = _CucsMemoryErrorStatsEccMultibitErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 21),
    _CucsMemoryErrorStatsEccMultibitErrors1WeekH_Type()
)
cucsMemoryErrorStatsEccMultibitErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccMultibitErrors1WeekH.setStatus("current")
_CucsMemoryErrorStatsEccSinglebitErrors_Type = Counter32
_CucsMemoryErrorStatsEccSinglebitErrors_Object = MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors = _CucsMemoryErrorStatsEccSinglebitErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 22),
    _CucsMemoryErrorStatsEccSinglebitErrors_Type()
)
cucsMemoryErrorStatsEccSinglebitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccSinglebitErrors.setStatus("current")
_CucsMemoryErrorStatsEccSinglebitErrors15Min_Type = Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors15Min_Object = MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors15Min = _CucsMemoryErrorStatsEccSinglebitErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 23),
    _CucsMemoryErrorStatsEccSinglebitErrors15Min_Type()
)
cucsMemoryErrorStatsEccSinglebitErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccSinglebitErrors15Min.setStatus("current")
_CucsMemoryErrorStatsEccSinglebitErrors15MinH_Type = Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors15MinH_Object = MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors15MinH = _CucsMemoryErrorStatsEccSinglebitErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 24),
    _CucsMemoryErrorStatsEccSinglebitErrors15MinH_Type()
)
cucsMemoryErrorStatsEccSinglebitErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccSinglebitErrors15MinH.setStatus("current")
_CucsMemoryErrorStatsEccSinglebitErrors1Day_Type = Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1Day_Object = MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1Day = _CucsMemoryErrorStatsEccSinglebitErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 25),
    _CucsMemoryErrorStatsEccSinglebitErrors1Day_Type()
)
cucsMemoryErrorStatsEccSinglebitErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccSinglebitErrors1Day.setStatus("current")
_CucsMemoryErrorStatsEccSinglebitErrors1DayH_Type = Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1DayH_Object = MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1DayH = _CucsMemoryErrorStatsEccSinglebitErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 26),
    _CucsMemoryErrorStatsEccSinglebitErrors1DayH_Type()
)
cucsMemoryErrorStatsEccSinglebitErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccSinglebitErrors1DayH.setStatus("current")
_CucsMemoryErrorStatsEccSinglebitErrors1Hour_Type = Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1Hour_Object = MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1Hour = _CucsMemoryErrorStatsEccSinglebitErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 27),
    _CucsMemoryErrorStatsEccSinglebitErrors1Hour_Type()
)
cucsMemoryErrorStatsEccSinglebitErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccSinglebitErrors1Hour.setStatus("current")
_CucsMemoryErrorStatsEccSinglebitErrors1HourH_Type = Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1HourH_Object = MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1HourH = _CucsMemoryErrorStatsEccSinglebitErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 28),
    _CucsMemoryErrorStatsEccSinglebitErrors1HourH_Type()
)
cucsMemoryErrorStatsEccSinglebitErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccSinglebitErrors1HourH.setStatus("current")
_CucsMemoryErrorStatsEccSinglebitErrors1Week_Type = Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1Week_Object = MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1Week = _CucsMemoryErrorStatsEccSinglebitErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 29),
    _CucsMemoryErrorStatsEccSinglebitErrors1Week_Type()
)
cucsMemoryErrorStatsEccSinglebitErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccSinglebitErrors1Week.setStatus("current")
_CucsMemoryErrorStatsEccSinglebitErrors1WeekH_Type = Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors1WeekH_Object = MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors1WeekH = _CucsMemoryErrorStatsEccSinglebitErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 30),
    _CucsMemoryErrorStatsEccSinglebitErrors1WeekH_Type()
)
cucsMemoryErrorStatsEccSinglebitErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccSinglebitErrors1WeekH.setStatus("current")
_CucsMemoryErrorStatsIntervals_Type = Gauge32
_CucsMemoryErrorStatsIntervals_Object = MibTableColumn
cucsMemoryErrorStatsIntervals = _CucsMemoryErrorStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 31),
    _CucsMemoryErrorStatsIntervals_Type()
)
cucsMemoryErrorStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsIntervals.setStatus("current")
_CucsMemoryErrorStatsMismatchErrors_Type = Counter32
_CucsMemoryErrorStatsMismatchErrors_Object = MibTableColumn
cucsMemoryErrorStatsMismatchErrors = _CucsMemoryErrorStatsMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 32),
    _CucsMemoryErrorStatsMismatchErrors_Type()
)
cucsMemoryErrorStatsMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsMismatchErrors.setStatus("current")
_CucsMemoryErrorStatsMismatchErrors15Min_Type = Gauge32
_CucsMemoryErrorStatsMismatchErrors15Min_Object = MibTableColumn
cucsMemoryErrorStatsMismatchErrors15Min = _CucsMemoryErrorStatsMismatchErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 33),
    _CucsMemoryErrorStatsMismatchErrors15Min_Type()
)
cucsMemoryErrorStatsMismatchErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsMismatchErrors15Min.setStatus("current")
_CucsMemoryErrorStatsMismatchErrors15MinH_Type = Gauge32
_CucsMemoryErrorStatsMismatchErrors15MinH_Object = MibTableColumn
cucsMemoryErrorStatsMismatchErrors15MinH = _CucsMemoryErrorStatsMismatchErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 34),
    _CucsMemoryErrorStatsMismatchErrors15MinH_Type()
)
cucsMemoryErrorStatsMismatchErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsMismatchErrors15MinH.setStatus("current")
_CucsMemoryErrorStatsMismatchErrors1Day_Type = Gauge32
_CucsMemoryErrorStatsMismatchErrors1Day_Object = MibTableColumn
cucsMemoryErrorStatsMismatchErrors1Day = _CucsMemoryErrorStatsMismatchErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 35),
    _CucsMemoryErrorStatsMismatchErrors1Day_Type()
)
cucsMemoryErrorStatsMismatchErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsMismatchErrors1Day.setStatus("current")
_CucsMemoryErrorStatsMismatchErrors1DayH_Type = Gauge32
_CucsMemoryErrorStatsMismatchErrors1DayH_Object = MibTableColumn
cucsMemoryErrorStatsMismatchErrors1DayH = _CucsMemoryErrorStatsMismatchErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 36),
    _CucsMemoryErrorStatsMismatchErrors1DayH_Type()
)
cucsMemoryErrorStatsMismatchErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsMismatchErrors1DayH.setStatus("current")
_CucsMemoryErrorStatsMismatchErrors1Hour_Type = Gauge32
_CucsMemoryErrorStatsMismatchErrors1Hour_Object = MibTableColumn
cucsMemoryErrorStatsMismatchErrors1Hour = _CucsMemoryErrorStatsMismatchErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 37),
    _CucsMemoryErrorStatsMismatchErrors1Hour_Type()
)
cucsMemoryErrorStatsMismatchErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsMismatchErrors1Hour.setStatus("current")
_CucsMemoryErrorStatsMismatchErrors1HourH_Type = Gauge32
_CucsMemoryErrorStatsMismatchErrors1HourH_Object = MibTableColumn
cucsMemoryErrorStatsMismatchErrors1HourH = _CucsMemoryErrorStatsMismatchErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 38),
    _CucsMemoryErrorStatsMismatchErrors1HourH_Type()
)
cucsMemoryErrorStatsMismatchErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsMismatchErrors1HourH.setStatus("current")
_CucsMemoryErrorStatsMismatchErrors1Week_Type = Gauge32
_CucsMemoryErrorStatsMismatchErrors1Week_Object = MibTableColumn
cucsMemoryErrorStatsMismatchErrors1Week = _CucsMemoryErrorStatsMismatchErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 39),
    _CucsMemoryErrorStatsMismatchErrors1Week_Type()
)
cucsMemoryErrorStatsMismatchErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsMismatchErrors1Week.setStatus("current")
_CucsMemoryErrorStatsMismatchErrors1WeekH_Type = Gauge32
_CucsMemoryErrorStatsMismatchErrors1WeekH_Object = MibTableColumn
cucsMemoryErrorStatsMismatchErrors1WeekH = _CucsMemoryErrorStatsMismatchErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 40),
    _CucsMemoryErrorStatsMismatchErrors1WeekH_Type()
)
cucsMemoryErrorStatsMismatchErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsMismatchErrors1WeekH.setStatus("current")
_CucsMemoryErrorStatsSuspect_Type = TruthValue
_CucsMemoryErrorStatsSuspect_Object = MibTableColumn
cucsMemoryErrorStatsSuspect = _CucsMemoryErrorStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 41),
    _CucsMemoryErrorStatsSuspect_Type()
)
cucsMemoryErrorStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsSuspect.setStatus("current")
_CucsMemoryErrorStatsThresholded_Type = CucsMemoryErrorStatsThresholded
_CucsMemoryErrorStatsThresholded_Object = MibTableColumn
cucsMemoryErrorStatsThresholded = _CucsMemoryErrorStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 42),
    _CucsMemoryErrorStatsThresholded_Type()
)
cucsMemoryErrorStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsThresholded.setStatus("current")
_CucsMemoryErrorStatsTimeCollected_Type = DateAndTime
_CucsMemoryErrorStatsTimeCollected_Object = MibTableColumn
cucsMemoryErrorStatsTimeCollected = _CucsMemoryErrorStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 43),
    _CucsMemoryErrorStatsTimeCollected_Type()
)
cucsMemoryErrorStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsTimeCollected.setStatus("current")
_CucsMemoryErrorStatsUpdate_Type = Gauge32
_CucsMemoryErrorStatsUpdate_Object = MibTableColumn
cucsMemoryErrorStatsUpdate = _CucsMemoryErrorStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 44),
    _CucsMemoryErrorStatsUpdate_Type()
)
cucsMemoryErrorStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsUpdate.setStatus("current")
_CucsMemoryErrorStatsAddressParityErrors2Weeks_Type = Gauge32
_CucsMemoryErrorStatsAddressParityErrors2Weeks_Object = MibTableColumn
cucsMemoryErrorStatsAddressParityErrors2Weeks = _CucsMemoryErrorStatsAddressParityErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 45),
    _CucsMemoryErrorStatsAddressParityErrors2Weeks_Type()
)
cucsMemoryErrorStatsAddressParityErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsAddressParityErrors2Weeks.setStatus("current")
_CucsMemoryErrorStatsAddressParityErrors2WeeksH_Type = Gauge32
_CucsMemoryErrorStatsAddressParityErrors2WeeksH_Object = MibTableColumn
cucsMemoryErrorStatsAddressParityErrors2WeeksH = _CucsMemoryErrorStatsAddressParityErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 46),
    _CucsMemoryErrorStatsAddressParityErrors2WeeksH_Type()
)
cucsMemoryErrorStatsAddressParityErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsAddressParityErrors2WeeksH.setStatus("current")
_CucsMemoryErrorStatsEccMultibitErrors2Weeks_Type = Gauge32
_CucsMemoryErrorStatsEccMultibitErrors2Weeks_Object = MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors2Weeks = _CucsMemoryErrorStatsEccMultibitErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 47),
    _CucsMemoryErrorStatsEccMultibitErrors2Weeks_Type()
)
cucsMemoryErrorStatsEccMultibitErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccMultibitErrors2Weeks.setStatus("current")
_CucsMemoryErrorStatsEccMultibitErrors2WeeksH_Type = Gauge32
_CucsMemoryErrorStatsEccMultibitErrors2WeeksH_Object = MibTableColumn
cucsMemoryErrorStatsEccMultibitErrors2WeeksH = _CucsMemoryErrorStatsEccMultibitErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 48),
    _CucsMemoryErrorStatsEccMultibitErrors2WeeksH_Type()
)
cucsMemoryErrorStatsEccMultibitErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccMultibitErrors2WeeksH.setStatus("current")
_CucsMemoryErrorStatsEccSinglebitErrors2Weeks_Type = Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors2Weeks_Object = MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors2Weeks = _CucsMemoryErrorStatsEccSinglebitErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 49),
    _CucsMemoryErrorStatsEccSinglebitErrors2Weeks_Type()
)
cucsMemoryErrorStatsEccSinglebitErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccSinglebitErrors2Weeks.setStatus("current")
_CucsMemoryErrorStatsEccSinglebitErrors2WeeksH_Type = Gauge32
_CucsMemoryErrorStatsEccSinglebitErrors2WeeksH_Object = MibTableColumn
cucsMemoryErrorStatsEccSinglebitErrors2WeeksH = _CucsMemoryErrorStatsEccSinglebitErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 50),
    _CucsMemoryErrorStatsEccSinglebitErrors2WeeksH_Type()
)
cucsMemoryErrorStatsEccSinglebitErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsEccSinglebitErrors2WeeksH.setStatus("current")
_CucsMemoryErrorStatsMismatchErrors2Weeks_Type = Gauge32
_CucsMemoryErrorStatsMismatchErrors2Weeks_Object = MibTableColumn
cucsMemoryErrorStatsMismatchErrors2Weeks = _CucsMemoryErrorStatsMismatchErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 51),
    _CucsMemoryErrorStatsMismatchErrors2Weeks_Type()
)
cucsMemoryErrorStatsMismatchErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsMismatchErrors2Weeks.setStatus("current")
_CucsMemoryErrorStatsMismatchErrors2WeeksH_Type = Gauge32
_CucsMemoryErrorStatsMismatchErrors2WeeksH_Object = MibTableColumn
cucsMemoryErrorStatsMismatchErrors2WeeksH = _CucsMemoryErrorStatsMismatchErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 7, 1, 52),
    _CucsMemoryErrorStatsMismatchErrors2WeeksH_Type()
)
cucsMemoryErrorStatsMismatchErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryErrorStatsMismatchErrors2WeeksH.setStatus("current")
_CucsMemoryQualTable_Object = MibTable
cucsMemoryQualTable = _CucsMemoryQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8)
)
if mibBuilder.loadTexts:
    cucsMemoryQualTable.setStatus("current")
_CucsMemoryQualEntry_Object = MibTableRow
cucsMemoryQualEntry = _CucsMemoryQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8, 1)
)
cucsMemoryQualEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryQualInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryQualEntry.setStatus("current")
_CucsMemoryQualInstanceId_Type = CucsManagedObjectId
_CucsMemoryQualInstanceId_Object = MibTableColumn
cucsMemoryQualInstanceId = _CucsMemoryQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8, 1, 1),
    _CucsMemoryQualInstanceId_Type()
)
cucsMemoryQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryQualInstanceId.setStatus("current")
_CucsMemoryQualDn_Type = CucsManagedObjectDn
_CucsMemoryQualDn_Object = MibTableColumn
cucsMemoryQualDn = _CucsMemoryQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8, 1, 2),
    _CucsMemoryQualDn_Type()
)
cucsMemoryQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryQualDn.setStatus("current")
_CucsMemoryQualRn_Type = SnmpAdminString
_CucsMemoryQualRn_Object = MibTableColumn
cucsMemoryQualRn = _CucsMemoryQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8, 1, 3),
    _CucsMemoryQualRn_Type()
)
cucsMemoryQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryQualRn.setStatus("current")
_CucsMemoryQualClock_Type = Gauge32
_CucsMemoryQualClock_Object = MibTableColumn
cucsMemoryQualClock = _CucsMemoryQualClock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8, 1, 4),
    _CucsMemoryQualClock_Type()
)
cucsMemoryQualClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryQualClock.setStatus("current")
_CucsMemoryQualLatency_Type = Integer32
_CucsMemoryQualLatency_Object = MibTableColumn
cucsMemoryQualLatency = _CucsMemoryQualLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8, 1, 5),
    _CucsMemoryQualLatency_Type()
)
cucsMemoryQualLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryQualLatency.setStatus("current")
_CucsMemoryQualMaxCap_Type = Gauge32
_CucsMemoryQualMaxCap_Object = MibTableColumn
cucsMemoryQualMaxCap = _CucsMemoryQualMaxCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8, 1, 6),
    _CucsMemoryQualMaxCap_Type()
)
cucsMemoryQualMaxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryQualMaxCap.setStatus("current")
_CucsMemoryQualMinCap_Type = Gauge32
_CucsMemoryQualMinCap_Object = MibTableColumn
cucsMemoryQualMinCap = _CucsMemoryQualMinCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8, 1, 7),
    _CucsMemoryQualMinCap_Type()
)
cucsMemoryQualMinCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryQualMinCap.setStatus("current")
_CucsMemoryQualSpeed_Type = Gauge32
_CucsMemoryQualSpeed_Object = MibTableColumn
cucsMemoryQualSpeed = _CucsMemoryQualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8, 1, 8),
    _CucsMemoryQualSpeed_Type()
)
cucsMemoryQualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryQualSpeed.setStatus("current")
_CucsMemoryQualUnits_Type = Gauge32
_CucsMemoryQualUnits_Object = MibTableColumn
cucsMemoryQualUnits = _CucsMemoryQualUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8, 1, 9),
    _CucsMemoryQualUnits_Type()
)
cucsMemoryQualUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryQualUnits.setStatus("current")
_CucsMemoryQualWidth_Type = Gauge32
_CucsMemoryQualWidth_Object = MibTableColumn
cucsMemoryQualWidth = _CucsMemoryQualWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 8, 1, 10),
    _CucsMemoryQualWidth_Type()
)
cucsMemoryQualWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryQualWidth.setStatus("current")
_CucsMemoryRuntimeTable_Object = MibTable
cucsMemoryRuntimeTable = _CucsMemoryRuntimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9)
)
if mibBuilder.loadTexts:
    cucsMemoryRuntimeTable.setStatus("current")
_CucsMemoryRuntimeEntry_Object = MibTableRow
cucsMemoryRuntimeEntry = _CucsMemoryRuntimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1)
)
cucsMemoryRuntimeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryRuntimeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryRuntimeEntry.setStatus("current")
_CucsMemoryRuntimeInstanceId_Type = CucsManagedObjectId
_CucsMemoryRuntimeInstanceId_Object = MibTableColumn
cucsMemoryRuntimeInstanceId = _CucsMemoryRuntimeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 1),
    _CucsMemoryRuntimeInstanceId_Type()
)
cucsMemoryRuntimeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeInstanceId.setStatus("current")
_CucsMemoryRuntimeDn_Type = CucsManagedObjectDn
_CucsMemoryRuntimeDn_Object = MibTableColumn
cucsMemoryRuntimeDn = _CucsMemoryRuntimeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 2),
    _CucsMemoryRuntimeDn_Type()
)
cucsMemoryRuntimeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeDn.setStatus("current")
_CucsMemoryRuntimeRn_Type = SnmpAdminString
_CucsMemoryRuntimeRn_Object = MibTableColumn
cucsMemoryRuntimeRn = _CucsMemoryRuntimeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 3),
    _CucsMemoryRuntimeRn_Type()
)
cucsMemoryRuntimeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeRn.setStatus("current")
_CucsMemoryRuntimeAvailable_Type = Gauge32
_CucsMemoryRuntimeAvailable_Object = MibTableColumn
cucsMemoryRuntimeAvailable = _CucsMemoryRuntimeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 4),
    _CucsMemoryRuntimeAvailable_Type()
)
cucsMemoryRuntimeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeAvailable.setStatus("current")
_CucsMemoryRuntimeAvailableAvg_Type = Gauge32
_CucsMemoryRuntimeAvailableAvg_Object = MibTableColumn
cucsMemoryRuntimeAvailableAvg = _CucsMemoryRuntimeAvailableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 5),
    _CucsMemoryRuntimeAvailableAvg_Type()
)
cucsMemoryRuntimeAvailableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeAvailableAvg.setStatus("current")
_CucsMemoryRuntimeAvailableMax_Type = Gauge32
_CucsMemoryRuntimeAvailableMax_Object = MibTableColumn
cucsMemoryRuntimeAvailableMax = _CucsMemoryRuntimeAvailableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 6),
    _CucsMemoryRuntimeAvailableMax_Type()
)
cucsMemoryRuntimeAvailableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeAvailableMax.setStatus("current")
_CucsMemoryRuntimeAvailableMin_Type = Gauge32
_CucsMemoryRuntimeAvailableMin_Object = MibTableColumn
cucsMemoryRuntimeAvailableMin = _CucsMemoryRuntimeAvailableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 7),
    _CucsMemoryRuntimeAvailableMin_Type()
)
cucsMemoryRuntimeAvailableMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeAvailableMin.setStatus("current")
_CucsMemoryRuntimeCached_Type = Gauge32
_CucsMemoryRuntimeCached_Object = MibTableColumn
cucsMemoryRuntimeCached = _CucsMemoryRuntimeCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 8),
    _CucsMemoryRuntimeCached_Type()
)
cucsMemoryRuntimeCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeCached.setStatus("current")
_CucsMemoryRuntimeCachedAvg_Type = Gauge32
_CucsMemoryRuntimeCachedAvg_Object = MibTableColumn
cucsMemoryRuntimeCachedAvg = _CucsMemoryRuntimeCachedAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 9),
    _CucsMemoryRuntimeCachedAvg_Type()
)
cucsMemoryRuntimeCachedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeCachedAvg.setStatus("current")
_CucsMemoryRuntimeCachedMax_Type = Gauge32
_CucsMemoryRuntimeCachedMax_Object = MibTableColumn
cucsMemoryRuntimeCachedMax = _CucsMemoryRuntimeCachedMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 10),
    _CucsMemoryRuntimeCachedMax_Type()
)
cucsMemoryRuntimeCachedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeCachedMax.setStatus("current")
_CucsMemoryRuntimeCachedMin_Type = Gauge32
_CucsMemoryRuntimeCachedMin_Object = MibTableColumn
cucsMemoryRuntimeCachedMin = _CucsMemoryRuntimeCachedMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 11),
    _CucsMemoryRuntimeCachedMin_Type()
)
cucsMemoryRuntimeCachedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeCachedMin.setStatus("current")
_CucsMemoryRuntimeIntervals_Type = Gauge32
_CucsMemoryRuntimeIntervals_Object = MibTableColumn
cucsMemoryRuntimeIntervals = _CucsMemoryRuntimeIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 12),
    _CucsMemoryRuntimeIntervals_Type()
)
cucsMemoryRuntimeIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeIntervals.setStatus("current")
_CucsMemoryRuntimeSuspect_Type = TruthValue
_CucsMemoryRuntimeSuspect_Object = MibTableColumn
cucsMemoryRuntimeSuspect = _CucsMemoryRuntimeSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 13),
    _CucsMemoryRuntimeSuspect_Type()
)
cucsMemoryRuntimeSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeSuspect.setStatus("current")
_CucsMemoryRuntimeThresholded_Type = CucsMemoryRuntimeThresholded
_CucsMemoryRuntimeThresholded_Object = MibTableColumn
cucsMemoryRuntimeThresholded = _CucsMemoryRuntimeThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 14),
    _CucsMemoryRuntimeThresholded_Type()
)
cucsMemoryRuntimeThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeThresholded.setStatus("current")
_CucsMemoryRuntimeTimeCollected_Type = DateAndTime
_CucsMemoryRuntimeTimeCollected_Object = MibTableColumn
cucsMemoryRuntimeTimeCollected = _CucsMemoryRuntimeTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 15),
    _CucsMemoryRuntimeTimeCollected_Type()
)
cucsMemoryRuntimeTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeTimeCollected.setStatus("current")
_CucsMemoryRuntimeTotal_Type = Gauge32
_CucsMemoryRuntimeTotal_Object = MibTableColumn
cucsMemoryRuntimeTotal = _CucsMemoryRuntimeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 16),
    _CucsMemoryRuntimeTotal_Type()
)
cucsMemoryRuntimeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeTotal.setStatus("current")
_CucsMemoryRuntimeTotalAvg_Type = Gauge32
_CucsMemoryRuntimeTotalAvg_Object = MibTableColumn
cucsMemoryRuntimeTotalAvg = _CucsMemoryRuntimeTotalAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 17),
    _CucsMemoryRuntimeTotalAvg_Type()
)
cucsMemoryRuntimeTotalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeTotalAvg.setStatus("current")
_CucsMemoryRuntimeTotalMax_Type = Gauge32
_CucsMemoryRuntimeTotalMax_Object = MibTableColumn
cucsMemoryRuntimeTotalMax = _CucsMemoryRuntimeTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 18),
    _CucsMemoryRuntimeTotalMax_Type()
)
cucsMemoryRuntimeTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeTotalMax.setStatus("current")
_CucsMemoryRuntimeTotalMin_Type = Gauge32
_CucsMemoryRuntimeTotalMin_Object = MibTableColumn
cucsMemoryRuntimeTotalMin = _CucsMemoryRuntimeTotalMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 19),
    _CucsMemoryRuntimeTotalMin_Type()
)
cucsMemoryRuntimeTotalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeTotalMin.setStatus("current")
_CucsMemoryRuntimeType_Type = CucsMemoryRuntimeType
_CucsMemoryRuntimeType_Object = MibTableColumn
cucsMemoryRuntimeType = _CucsMemoryRuntimeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 20),
    _CucsMemoryRuntimeType_Type()
)
cucsMemoryRuntimeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeType.setStatus("current")
_CucsMemoryRuntimeUpdate_Type = Gauge32
_CucsMemoryRuntimeUpdate_Object = MibTableColumn
cucsMemoryRuntimeUpdate = _CucsMemoryRuntimeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 9, 1, 21),
    _CucsMemoryRuntimeUpdate_Type()
)
cucsMemoryRuntimeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeUpdate.setStatus("current")
_CucsMemoryRuntimeHistTable_Object = MibTable
cucsMemoryRuntimeHistTable = _CucsMemoryRuntimeHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10)
)
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistTable.setStatus("current")
_CucsMemoryRuntimeHistEntry_Object = MibTableRow
cucsMemoryRuntimeHistEntry = _CucsMemoryRuntimeHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1)
)
cucsMemoryRuntimeHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryRuntimeHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistEntry.setStatus("current")
_CucsMemoryRuntimeHistInstanceId_Type = CucsManagedObjectId
_CucsMemoryRuntimeHistInstanceId_Object = MibTableColumn
cucsMemoryRuntimeHistInstanceId = _CucsMemoryRuntimeHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 1),
    _CucsMemoryRuntimeHistInstanceId_Type()
)
cucsMemoryRuntimeHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistInstanceId.setStatus("current")
_CucsMemoryRuntimeHistDn_Type = CucsManagedObjectDn
_CucsMemoryRuntimeHistDn_Object = MibTableColumn
cucsMemoryRuntimeHistDn = _CucsMemoryRuntimeHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 2),
    _CucsMemoryRuntimeHistDn_Type()
)
cucsMemoryRuntimeHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistDn.setStatus("current")
_CucsMemoryRuntimeHistRn_Type = SnmpAdminString
_CucsMemoryRuntimeHistRn_Object = MibTableColumn
cucsMemoryRuntimeHistRn = _CucsMemoryRuntimeHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 3),
    _CucsMemoryRuntimeHistRn_Type()
)
cucsMemoryRuntimeHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistRn.setStatus("current")
_CucsMemoryRuntimeHistAvailable_Type = Gauge32
_CucsMemoryRuntimeHistAvailable_Object = MibTableColumn
cucsMemoryRuntimeHistAvailable = _CucsMemoryRuntimeHistAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 4),
    _CucsMemoryRuntimeHistAvailable_Type()
)
cucsMemoryRuntimeHistAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistAvailable.setStatus("current")
_CucsMemoryRuntimeHistAvailableAvg_Type = Gauge32
_CucsMemoryRuntimeHistAvailableAvg_Object = MibTableColumn
cucsMemoryRuntimeHistAvailableAvg = _CucsMemoryRuntimeHistAvailableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 5),
    _CucsMemoryRuntimeHistAvailableAvg_Type()
)
cucsMemoryRuntimeHistAvailableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistAvailableAvg.setStatus("current")
_CucsMemoryRuntimeHistAvailableMax_Type = Gauge32
_CucsMemoryRuntimeHistAvailableMax_Object = MibTableColumn
cucsMemoryRuntimeHistAvailableMax = _CucsMemoryRuntimeHistAvailableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 6),
    _CucsMemoryRuntimeHistAvailableMax_Type()
)
cucsMemoryRuntimeHistAvailableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistAvailableMax.setStatus("current")
_CucsMemoryRuntimeHistAvailableMin_Type = Gauge32
_CucsMemoryRuntimeHistAvailableMin_Object = MibTableColumn
cucsMemoryRuntimeHistAvailableMin = _CucsMemoryRuntimeHistAvailableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 7),
    _CucsMemoryRuntimeHistAvailableMin_Type()
)
cucsMemoryRuntimeHistAvailableMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistAvailableMin.setStatus("current")
_CucsMemoryRuntimeHistCached_Type = Gauge32
_CucsMemoryRuntimeHistCached_Object = MibTableColumn
cucsMemoryRuntimeHistCached = _CucsMemoryRuntimeHistCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 8),
    _CucsMemoryRuntimeHistCached_Type()
)
cucsMemoryRuntimeHistCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistCached.setStatus("current")
_CucsMemoryRuntimeHistCachedAvg_Type = Gauge32
_CucsMemoryRuntimeHistCachedAvg_Object = MibTableColumn
cucsMemoryRuntimeHistCachedAvg = _CucsMemoryRuntimeHistCachedAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 9),
    _CucsMemoryRuntimeHistCachedAvg_Type()
)
cucsMemoryRuntimeHistCachedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistCachedAvg.setStatus("current")
_CucsMemoryRuntimeHistCachedMax_Type = Gauge32
_CucsMemoryRuntimeHistCachedMax_Object = MibTableColumn
cucsMemoryRuntimeHistCachedMax = _CucsMemoryRuntimeHistCachedMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 10),
    _CucsMemoryRuntimeHistCachedMax_Type()
)
cucsMemoryRuntimeHistCachedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistCachedMax.setStatus("current")
_CucsMemoryRuntimeHistCachedMin_Type = Gauge32
_CucsMemoryRuntimeHistCachedMin_Object = MibTableColumn
cucsMemoryRuntimeHistCachedMin = _CucsMemoryRuntimeHistCachedMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 11),
    _CucsMemoryRuntimeHistCachedMin_Type()
)
cucsMemoryRuntimeHistCachedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistCachedMin.setStatus("current")
_CucsMemoryRuntimeHistId_Type = Unsigned64
_CucsMemoryRuntimeHistId_Object = MibTableColumn
cucsMemoryRuntimeHistId = _CucsMemoryRuntimeHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 12),
    _CucsMemoryRuntimeHistId_Type()
)
cucsMemoryRuntimeHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistId.setStatus("current")
_CucsMemoryRuntimeHistMostRecent_Type = TruthValue
_CucsMemoryRuntimeHistMostRecent_Object = MibTableColumn
cucsMemoryRuntimeHistMostRecent = _CucsMemoryRuntimeHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 13),
    _CucsMemoryRuntimeHistMostRecent_Type()
)
cucsMemoryRuntimeHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistMostRecent.setStatus("current")
_CucsMemoryRuntimeHistSuspect_Type = TruthValue
_CucsMemoryRuntimeHistSuspect_Object = MibTableColumn
cucsMemoryRuntimeHistSuspect = _CucsMemoryRuntimeHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 14),
    _CucsMemoryRuntimeHistSuspect_Type()
)
cucsMemoryRuntimeHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistSuspect.setStatus("current")
_CucsMemoryRuntimeHistThresholded_Type = CucsMemoryRuntimeHistThresholded
_CucsMemoryRuntimeHistThresholded_Object = MibTableColumn
cucsMemoryRuntimeHistThresholded = _CucsMemoryRuntimeHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 15),
    _CucsMemoryRuntimeHistThresholded_Type()
)
cucsMemoryRuntimeHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistThresholded.setStatus("current")
_CucsMemoryRuntimeHistTimeCollected_Type = DateAndTime
_CucsMemoryRuntimeHistTimeCollected_Object = MibTableColumn
cucsMemoryRuntimeHistTimeCollected = _CucsMemoryRuntimeHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 16),
    _CucsMemoryRuntimeHistTimeCollected_Type()
)
cucsMemoryRuntimeHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistTimeCollected.setStatus("current")
_CucsMemoryRuntimeHistTotal_Type = Gauge32
_CucsMemoryRuntimeHistTotal_Object = MibTableColumn
cucsMemoryRuntimeHistTotal = _CucsMemoryRuntimeHistTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 17),
    _CucsMemoryRuntimeHistTotal_Type()
)
cucsMemoryRuntimeHistTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistTotal.setStatus("current")
_CucsMemoryRuntimeHistTotalAvg_Type = Gauge32
_CucsMemoryRuntimeHistTotalAvg_Object = MibTableColumn
cucsMemoryRuntimeHistTotalAvg = _CucsMemoryRuntimeHistTotalAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 18),
    _CucsMemoryRuntimeHistTotalAvg_Type()
)
cucsMemoryRuntimeHistTotalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistTotalAvg.setStatus("current")
_CucsMemoryRuntimeHistTotalMax_Type = Gauge32
_CucsMemoryRuntimeHistTotalMax_Object = MibTableColumn
cucsMemoryRuntimeHistTotalMax = _CucsMemoryRuntimeHistTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 19),
    _CucsMemoryRuntimeHistTotalMax_Type()
)
cucsMemoryRuntimeHistTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistTotalMax.setStatus("current")
_CucsMemoryRuntimeHistTotalMin_Type = Gauge32
_CucsMemoryRuntimeHistTotalMin_Object = MibTableColumn
cucsMemoryRuntimeHistTotalMin = _CucsMemoryRuntimeHistTotalMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 10, 1, 20),
    _CucsMemoryRuntimeHistTotalMin_Type()
)
cucsMemoryRuntimeHistTotalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryRuntimeHistTotalMin.setStatus("current")
_CucsMemoryUnitTable_Object = MibTable
cucsMemoryUnitTable = _CucsMemoryUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11)
)
if mibBuilder.loadTexts:
    cucsMemoryUnitTable.setStatus("current")
_CucsMemoryUnitEntry_Object = MibTableRow
cucsMemoryUnitEntry = _CucsMemoryUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1)
)
cucsMemoryUnitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryUnitEntry.setStatus("current")
_CucsMemoryUnitInstanceId_Type = CucsManagedObjectId
_CucsMemoryUnitInstanceId_Object = MibTableColumn
cucsMemoryUnitInstanceId = _CucsMemoryUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 1),
    _CucsMemoryUnitInstanceId_Type()
)
cucsMemoryUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryUnitInstanceId.setStatus("current")
_CucsMemoryUnitDn_Type = CucsManagedObjectDn
_CucsMemoryUnitDn_Object = MibTableColumn
cucsMemoryUnitDn = _CucsMemoryUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 2),
    _CucsMemoryUnitDn_Type()
)
cucsMemoryUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitDn.setStatus("current")
_CucsMemoryUnitRn_Type = SnmpAdminString
_CucsMemoryUnitRn_Object = MibTableColumn
cucsMemoryUnitRn = _CucsMemoryUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 3),
    _CucsMemoryUnitRn_Type()
)
cucsMemoryUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitRn.setStatus("current")
_CucsMemoryUnitArray_Type = Gauge32
_CucsMemoryUnitArray_Object = MibTableColumn
cucsMemoryUnitArray = _CucsMemoryUnitArray_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 4),
    _CucsMemoryUnitArray_Type()
)
cucsMemoryUnitArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitArray.setStatus("current")
_CucsMemoryUnitBank_Type = Gauge32
_CucsMemoryUnitBank_Object = MibTableColumn
cucsMemoryUnitBank = _CucsMemoryUnitBank_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 5),
    _CucsMemoryUnitBank_Type()
)
cucsMemoryUnitBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitBank.setStatus("current")
_CucsMemoryUnitCapacity_Type = Gauge32
_CucsMemoryUnitCapacity_Object = MibTableColumn
cucsMemoryUnitCapacity = _CucsMemoryUnitCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 6),
    _CucsMemoryUnitCapacity_Type()
)
cucsMemoryUnitCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitCapacity.setStatus("current")
_CucsMemoryUnitClock_Type = Gauge32
_CucsMemoryUnitClock_Object = MibTableColumn
cucsMemoryUnitClock = _CucsMemoryUnitClock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 7),
    _CucsMemoryUnitClock_Type()
)
cucsMemoryUnitClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitClock.setStatus("current")
_CucsMemoryUnitFormFactor_Type = CucsMemoryFormFactor
_CucsMemoryUnitFormFactor_Object = MibTableColumn
cucsMemoryUnitFormFactor = _CucsMemoryUnitFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 8),
    _CucsMemoryUnitFormFactor_Type()
)
cucsMemoryUnitFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitFormFactor.setStatus("current")
_CucsMemoryUnitId_Type = CucsMemoryUnitId
_CucsMemoryUnitId_Object = MibTableColumn
cucsMemoryUnitId = _CucsMemoryUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 9),
    _CucsMemoryUnitId_Type()
)
cucsMemoryUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitId.setStatus("current")
_CucsMemoryUnitLatency_Type = Integer32
_CucsMemoryUnitLatency_Object = MibTableColumn
cucsMemoryUnitLatency = _CucsMemoryUnitLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 10),
    _CucsMemoryUnitLatency_Type()
)
cucsMemoryUnitLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitLatency.setStatus("current")
_CucsMemoryUnitLocation_Type = SnmpAdminString
_CucsMemoryUnitLocation_Object = MibTableColumn
cucsMemoryUnitLocation = _CucsMemoryUnitLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 11),
    _CucsMemoryUnitLocation_Type()
)
cucsMemoryUnitLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitLocation.setStatus("current")
_CucsMemoryUnitModel_Type = SnmpAdminString
_CucsMemoryUnitModel_Object = MibTableColumn
cucsMemoryUnitModel = _CucsMemoryUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 12),
    _CucsMemoryUnitModel_Type()
)
cucsMemoryUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitModel.setStatus("current")
_CucsMemoryUnitOperState_Type = CucsEquipmentOperability
_CucsMemoryUnitOperState_Object = MibTableColumn
cucsMemoryUnitOperState = _CucsMemoryUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 13),
    _CucsMemoryUnitOperState_Type()
)
cucsMemoryUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitOperState.setStatus("current")
_CucsMemoryUnitOperability_Type = CucsMemoryUnitOperability
_CucsMemoryUnitOperability_Object = MibTableColumn
cucsMemoryUnitOperability = _CucsMemoryUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 14),
    _CucsMemoryUnitOperability_Type()
)
cucsMemoryUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitOperability.setStatus("current")
_CucsMemoryUnitPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsMemoryUnitPerf_Object = MibTableColumn
cucsMemoryUnitPerf = _CucsMemoryUnitPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 15),
    _CucsMemoryUnitPerf_Type()
)
cucsMemoryUnitPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitPerf.setStatus("current")
_CucsMemoryUnitPower_Type = CucsEquipmentPowerState
_CucsMemoryUnitPower_Object = MibTableColumn
cucsMemoryUnitPower = _CucsMemoryUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 16),
    _CucsMemoryUnitPower_Type()
)
cucsMemoryUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitPower.setStatus("current")
_CucsMemoryUnitPresence_Type = CucsEquipmentPresence
_CucsMemoryUnitPresence_Object = MibTableColumn
cucsMemoryUnitPresence = _CucsMemoryUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 17),
    _CucsMemoryUnitPresence_Type()
)
cucsMemoryUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitPresence.setStatus("current")
_CucsMemoryUnitRevision_Type = SnmpAdminString
_CucsMemoryUnitRevision_Object = MibTableColumn
cucsMemoryUnitRevision = _CucsMemoryUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 18),
    _CucsMemoryUnitRevision_Type()
)
cucsMemoryUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitRevision.setStatus("current")
_CucsMemoryUnitSerial_Type = SnmpAdminString
_CucsMemoryUnitSerial_Object = MibTableColumn
cucsMemoryUnitSerial = _CucsMemoryUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 19),
    _CucsMemoryUnitSerial_Type()
)
cucsMemoryUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitSerial.setStatus("current")
_CucsMemoryUnitSet_Type = Gauge32
_CucsMemoryUnitSet_Object = MibTableColumn
cucsMemoryUnitSet = _CucsMemoryUnitSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 20),
    _CucsMemoryUnitSet_Type()
)
cucsMemoryUnitSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitSet.setStatus("current")
_CucsMemoryUnitSpeed_Type = Gauge32
_CucsMemoryUnitSpeed_Object = MibTableColumn
cucsMemoryUnitSpeed = _CucsMemoryUnitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 21),
    _CucsMemoryUnitSpeed_Type()
)
cucsMemoryUnitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitSpeed.setStatus("current")
_CucsMemoryUnitThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsMemoryUnitThermal_Object = MibTableColumn
cucsMemoryUnitThermal = _CucsMemoryUnitThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 22),
    _CucsMemoryUnitThermal_Type()
)
cucsMemoryUnitThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitThermal.setStatus("current")
_CucsMemoryUnitType_Type = CucsMemoryType
_CucsMemoryUnitType_Object = MibTableColumn
cucsMemoryUnitType = _CucsMemoryUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 23),
    _CucsMemoryUnitType_Type()
)
cucsMemoryUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitType.setStatus("current")
_CucsMemoryUnitVendor_Type = SnmpAdminString
_CucsMemoryUnitVendor_Object = MibTableColumn
cucsMemoryUnitVendor = _CucsMemoryUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 24),
    _CucsMemoryUnitVendor_Type()
)
cucsMemoryUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitVendor.setStatus("current")
_CucsMemoryUnitVisibility_Type = CucsMemoryVisibility
_CucsMemoryUnitVisibility_Object = MibTableColumn
cucsMemoryUnitVisibility = _CucsMemoryUnitVisibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 25),
    _CucsMemoryUnitVisibility_Type()
)
cucsMemoryUnitVisibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitVisibility.setStatus("current")
_CucsMemoryUnitVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsMemoryUnitVoltage_Object = MibTableColumn
cucsMemoryUnitVoltage = _CucsMemoryUnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 26),
    _CucsMemoryUnitVoltage_Type()
)
cucsMemoryUnitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitVoltage.setStatus("current")
_CucsMemoryUnitWidth_Type = Gauge32
_CucsMemoryUnitWidth_Object = MibTableColumn
cucsMemoryUnitWidth = _CucsMemoryUnitWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 27),
    _CucsMemoryUnitWidth_Type()
)
cucsMemoryUnitWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitWidth.setStatus("current")
_CucsMemoryUnitAdminState_Type = CucsMemoryAdminState
_CucsMemoryUnitAdminState_Object = MibTableColumn
cucsMemoryUnitAdminState = _CucsMemoryUnitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 28),
    _CucsMemoryUnitAdminState_Type()
)
cucsMemoryUnitAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitAdminState.setStatus("current")
_CucsMemoryUnitOperQualifier_Type = CucsMemoryIssues
_CucsMemoryUnitOperQualifier_Object = MibTableColumn
cucsMemoryUnitOperQualifier = _CucsMemoryUnitOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 29),
    _CucsMemoryUnitOperQualifier_Type()
)
cucsMemoryUnitOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitOperQualifier.setStatus("current")
_CucsMemoryUnitOperQualifierReason_Type = SnmpAdminString
_CucsMemoryUnitOperQualifierReason_Object = MibTableColumn
cucsMemoryUnitOperQualifierReason = _CucsMemoryUnitOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 30),
    _CucsMemoryUnitOperQualifierReason_Type()
)
cucsMemoryUnitOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitOperQualifierReason.setStatus("current")
_CucsMemoryUnitLocationDn_Type = SnmpAdminString
_CucsMemoryUnitLocationDn_Object = MibTableColumn
cucsMemoryUnitLocationDn = _CucsMemoryUnitLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 11, 1, 31),
    _CucsMemoryUnitLocationDn_Type()
)
cucsMemoryUnitLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitLocationDn.setStatus("current")
_CucsMemoryUnitEnvStatsTable_Object = MibTable
cucsMemoryUnitEnvStatsTable = _CucsMemoryUnitEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12)
)
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsTable.setStatus("current")
_CucsMemoryUnitEnvStatsEntry_Object = MibTableRow
cucsMemoryUnitEnvStatsEntry = _CucsMemoryUnitEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1)
)
cucsMemoryUnitEnvStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryUnitEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsEntry.setStatus("current")
_CucsMemoryUnitEnvStatsInstanceId_Type = CucsManagedObjectId
_CucsMemoryUnitEnvStatsInstanceId_Object = MibTableColumn
cucsMemoryUnitEnvStatsInstanceId = _CucsMemoryUnitEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 1),
    _CucsMemoryUnitEnvStatsInstanceId_Type()
)
cucsMemoryUnitEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsInstanceId.setStatus("current")
_CucsMemoryUnitEnvStatsDn_Type = CucsManagedObjectDn
_CucsMemoryUnitEnvStatsDn_Object = MibTableColumn
cucsMemoryUnitEnvStatsDn = _CucsMemoryUnitEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 2),
    _CucsMemoryUnitEnvStatsDn_Type()
)
cucsMemoryUnitEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsDn.setStatus("current")
_CucsMemoryUnitEnvStatsRn_Type = SnmpAdminString
_CucsMemoryUnitEnvStatsRn_Object = MibTableColumn
cucsMemoryUnitEnvStatsRn = _CucsMemoryUnitEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 3),
    _CucsMemoryUnitEnvStatsRn_Type()
)
cucsMemoryUnitEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsRn.setStatus("current")
_CucsMemoryUnitEnvStatsIntervals_Type = Gauge32
_CucsMemoryUnitEnvStatsIntervals_Object = MibTableColumn
cucsMemoryUnitEnvStatsIntervals = _CucsMemoryUnitEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 4),
    _CucsMemoryUnitEnvStatsIntervals_Type()
)
cucsMemoryUnitEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsIntervals.setStatus("current")
_CucsMemoryUnitEnvStatsSuspect_Type = TruthValue
_CucsMemoryUnitEnvStatsSuspect_Object = MibTableColumn
cucsMemoryUnitEnvStatsSuspect = _CucsMemoryUnitEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 5),
    _CucsMemoryUnitEnvStatsSuspect_Type()
)
cucsMemoryUnitEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsSuspect.setStatus("current")
_CucsMemoryUnitEnvStatsTemperature_Type = Integer32
_CucsMemoryUnitEnvStatsTemperature_Object = MibTableColumn
cucsMemoryUnitEnvStatsTemperature = _CucsMemoryUnitEnvStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 6),
    _CucsMemoryUnitEnvStatsTemperature_Type()
)
cucsMemoryUnitEnvStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsTemperature.setStatus("current")
_CucsMemoryUnitEnvStatsTemperatureAvg_Type = Integer32
_CucsMemoryUnitEnvStatsTemperatureAvg_Object = MibTableColumn
cucsMemoryUnitEnvStatsTemperatureAvg = _CucsMemoryUnitEnvStatsTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 7),
    _CucsMemoryUnitEnvStatsTemperatureAvg_Type()
)
cucsMemoryUnitEnvStatsTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsTemperatureAvg.setStatus("current")
_CucsMemoryUnitEnvStatsTemperatureMax_Type = Integer32
_CucsMemoryUnitEnvStatsTemperatureMax_Object = MibTableColumn
cucsMemoryUnitEnvStatsTemperatureMax = _CucsMemoryUnitEnvStatsTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 8),
    _CucsMemoryUnitEnvStatsTemperatureMax_Type()
)
cucsMemoryUnitEnvStatsTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsTemperatureMax.setStatus("current")
_CucsMemoryUnitEnvStatsTemperatureMin_Type = Integer32
_CucsMemoryUnitEnvStatsTemperatureMin_Object = MibTableColumn
cucsMemoryUnitEnvStatsTemperatureMin = _CucsMemoryUnitEnvStatsTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 9),
    _CucsMemoryUnitEnvStatsTemperatureMin_Type()
)
cucsMemoryUnitEnvStatsTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsTemperatureMin.setStatus("current")
_CucsMemoryUnitEnvStatsThresholded_Type = CucsMemoryUnitEnvStatsThresholded
_CucsMemoryUnitEnvStatsThresholded_Object = MibTableColumn
cucsMemoryUnitEnvStatsThresholded = _CucsMemoryUnitEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 10),
    _CucsMemoryUnitEnvStatsThresholded_Type()
)
cucsMemoryUnitEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsThresholded.setStatus("current")
_CucsMemoryUnitEnvStatsTimeCollected_Type = DateAndTime
_CucsMemoryUnitEnvStatsTimeCollected_Object = MibTableColumn
cucsMemoryUnitEnvStatsTimeCollected = _CucsMemoryUnitEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 11),
    _CucsMemoryUnitEnvStatsTimeCollected_Type()
)
cucsMemoryUnitEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsTimeCollected.setStatus("current")
_CucsMemoryUnitEnvStatsUpdate_Type = Gauge32
_CucsMemoryUnitEnvStatsUpdate_Object = MibTableColumn
cucsMemoryUnitEnvStatsUpdate = _CucsMemoryUnitEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 12, 1, 12),
    _CucsMemoryUnitEnvStatsUpdate_Type()
)
cucsMemoryUnitEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsUpdate.setStatus("current")
_CucsMemoryUnitEnvStatsHistTable_Object = MibTable
cucsMemoryUnitEnvStatsHistTable = _CucsMemoryUnitEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13)
)
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistTable.setStatus("current")
_CucsMemoryUnitEnvStatsHistEntry_Object = MibTableRow
cucsMemoryUnitEnvStatsHistEntry = _CucsMemoryUnitEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1)
)
cucsMemoryUnitEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MEMORY-MIB", "cucsMemoryUnitEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistEntry.setStatus("current")
_CucsMemoryUnitEnvStatsHistInstanceId_Type = CucsManagedObjectId
_CucsMemoryUnitEnvStatsHistInstanceId_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistInstanceId = _CucsMemoryUnitEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 1),
    _CucsMemoryUnitEnvStatsHistInstanceId_Type()
)
cucsMemoryUnitEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistInstanceId.setStatus("current")
_CucsMemoryUnitEnvStatsHistDn_Type = CucsManagedObjectDn
_CucsMemoryUnitEnvStatsHistDn_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistDn = _CucsMemoryUnitEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 2),
    _CucsMemoryUnitEnvStatsHistDn_Type()
)
cucsMemoryUnitEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistDn.setStatus("current")
_CucsMemoryUnitEnvStatsHistRn_Type = SnmpAdminString
_CucsMemoryUnitEnvStatsHistRn_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistRn = _CucsMemoryUnitEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 3),
    _CucsMemoryUnitEnvStatsHistRn_Type()
)
cucsMemoryUnitEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistRn.setStatus("current")
_CucsMemoryUnitEnvStatsHistId_Type = Unsigned64
_CucsMemoryUnitEnvStatsHistId_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistId = _CucsMemoryUnitEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 4),
    _CucsMemoryUnitEnvStatsHistId_Type()
)
cucsMemoryUnitEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistId.setStatus("current")
_CucsMemoryUnitEnvStatsHistMostRecent_Type = TruthValue
_CucsMemoryUnitEnvStatsHistMostRecent_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistMostRecent = _CucsMemoryUnitEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 5),
    _CucsMemoryUnitEnvStatsHistMostRecent_Type()
)
cucsMemoryUnitEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistMostRecent.setStatus("current")
_CucsMemoryUnitEnvStatsHistSuspect_Type = TruthValue
_CucsMemoryUnitEnvStatsHistSuspect_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistSuspect = _CucsMemoryUnitEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 6),
    _CucsMemoryUnitEnvStatsHistSuspect_Type()
)
cucsMemoryUnitEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistSuspect.setStatus("current")
_CucsMemoryUnitEnvStatsHistTemperature_Type = Integer32
_CucsMemoryUnitEnvStatsHistTemperature_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistTemperature = _CucsMemoryUnitEnvStatsHistTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 7),
    _CucsMemoryUnitEnvStatsHistTemperature_Type()
)
cucsMemoryUnitEnvStatsHistTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistTemperature.setStatus("current")
_CucsMemoryUnitEnvStatsHistTemperatureAvg_Type = Integer32
_CucsMemoryUnitEnvStatsHistTemperatureAvg_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistTemperatureAvg = _CucsMemoryUnitEnvStatsHistTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 8),
    _CucsMemoryUnitEnvStatsHistTemperatureAvg_Type()
)
cucsMemoryUnitEnvStatsHistTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistTemperatureAvg.setStatus("current")
_CucsMemoryUnitEnvStatsHistTemperatureMax_Type = Integer32
_CucsMemoryUnitEnvStatsHistTemperatureMax_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistTemperatureMax = _CucsMemoryUnitEnvStatsHistTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 9),
    _CucsMemoryUnitEnvStatsHistTemperatureMax_Type()
)
cucsMemoryUnitEnvStatsHistTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistTemperatureMax.setStatus("current")
_CucsMemoryUnitEnvStatsHistTemperatureMin_Type = Integer32
_CucsMemoryUnitEnvStatsHistTemperatureMin_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistTemperatureMin = _CucsMemoryUnitEnvStatsHistTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 10),
    _CucsMemoryUnitEnvStatsHistTemperatureMin_Type()
)
cucsMemoryUnitEnvStatsHistTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistTemperatureMin.setStatus("current")
_CucsMemoryUnitEnvStatsHistThresholded_Type = CucsMemoryUnitEnvStatsHistThresholded
_CucsMemoryUnitEnvStatsHistThresholded_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistThresholded = _CucsMemoryUnitEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 11),
    _CucsMemoryUnitEnvStatsHistThresholded_Type()
)
cucsMemoryUnitEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistThresholded.setStatus("current")
_CucsMemoryUnitEnvStatsHistTimeCollected_Type = DateAndTime
_CucsMemoryUnitEnvStatsHistTimeCollected_Object = MibTableColumn
cucsMemoryUnitEnvStatsHistTimeCollected = _CucsMemoryUnitEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 30, 13, 1, 12),
    _CucsMemoryUnitEnvStatsHistTimeCollected_Type()
)
cucsMemoryUnitEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMemoryUnitEnvStatsHistTimeCollected.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-MEMORY-MIB",
    **{"cucsMemoryObjects": cucsMemoryObjects,
       "cucsMemoryArrayTable": cucsMemoryArrayTable,
       "cucsMemoryArrayEntry": cucsMemoryArrayEntry,
       "cucsMemoryArrayInstanceId": cucsMemoryArrayInstanceId,
       "cucsMemoryArrayDn": cucsMemoryArrayDn,
       "cucsMemoryArrayRn": cucsMemoryArrayRn,
       "cucsMemoryArrayCpuId": cucsMemoryArrayCpuId,
       "cucsMemoryArrayCurrCapacity": cucsMemoryArrayCurrCapacity,
       "cucsMemoryArrayErrorCorrection": cucsMemoryArrayErrorCorrection,
       "cucsMemoryArrayId": cucsMemoryArrayId,
       "cucsMemoryArrayMaxCapacity": cucsMemoryArrayMaxCapacity,
       "cucsMemoryArrayMaxDevices": cucsMemoryArrayMaxDevices,
       "cucsMemoryArrayModel": cucsMemoryArrayModel,
       "cucsMemoryArrayOperState": cucsMemoryArrayOperState,
       "cucsMemoryArrayOperability": cucsMemoryArrayOperability,
       "cucsMemoryArrayPerf": cucsMemoryArrayPerf,
       "cucsMemoryArrayPopulated": cucsMemoryArrayPopulated,
       "cucsMemoryArrayPower": cucsMemoryArrayPower,
       "cucsMemoryArrayPresence": cucsMemoryArrayPresence,
       "cucsMemoryArrayRevision": cucsMemoryArrayRevision,
       "cucsMemoryArraySerial": cucsMemoryArraySerial,
       "cucsMemoryArrayThermal": cucsMemoryArrayThermal,
       "cucsMemoryArrayVendor": cucsMemoryArrayVendor,
       "cucsMemoryArrayVoltage": cucsMemoryArrayVoltage,
       "cucsMemoryArrayOperQualifierReason": cucsMemoryArrayOperQualifierReason,
       "cucsMemoryArrayLocationDn": cucsMemoryArrayLocationDn,
       "cucsMemoryArrayEnvStatsTable": cucsMemoryArrayEnvStatsTable,
       "cucsMemoryArrayEnvStatsEntry": cucsMemoryArrayEnvStatsEntry,
       "cucsMemoryArrayEnvStatsInstanceId": cucsMemoryArrayEnvStatsInstanceId,
       "cucsMemoryArrayEnvStatsDn": cucsMemoryArrayEnvStatsDn,
       "cucsMemoryArrayEnvStatsRn": cucsMemoryArrayEnvStatsRn,
       "cucsMemoryArrayEnvStatsInputCurrent": cucsMemoryArrayEnvStatsInputCurrent,
       "cucsMemoryArrayEnvStatsInputCurrentAvg": cucsMemoryArrayEnvStatsInputCurrentAvg,
       "cucsMemoryArrayEnvStatsInputCurrentMax": cucsMemoryArrayEnvStatsInputCurrentMax,
       "cucsMemoryArrayEnvStatsInputCurrentMin": cucsMemoryArrayEnvStatsInputCurrentMin,
       "cucsMemoryArrayEnvStatsIntervals": cucsMemoryArrayEnvStatsIntervals,
       "cucsMemoryArrayEnvStatsSuspect": cucsMemoryArrayEnvStatsSuspect,
       "cucsMemoryArrayEnvStatsThresholded": cucsMemoryArrayEnvStatsThresholded,
       "cucsMemoryArrayEnvStatsTimeCollected": cucsMemoryArrayEnvStatsTimeCollected,
       "cucsMemoryArrayEnvStatsUpdate": cucsMemoryArrayEnvStatsUpdate,
       "cucsMemoryArrayEnvStatsHistTable": cucsMemoryArrayEnvStatsHistTable,
       "cucsMemoryArrayEnvStatsHistEntry": cucsMemoryArrayEnvStatsHistEntry,
       "cucsMemoryArrayEnvStatsHistInstanceId": cucsMemoryArrayEnvStatsHistInstanceId,
       "cucsMemoryArrayEnvStatsHistDn": cucsMemoryArrayEnvStatsHistDn,
       "cucsMemoryArrayEnvStatsHistRn": cucsMemoryArrayEnvStatsHistRn,
       "cucsMemoryArrayEnvStatsHistId": cucsMemoryArrayEnvStatsHistId,
       "cucsMemoryArrayEnvStatsHistInputCurrent": cucsMemoryArrayEnvStatsHistInputCurrent,
       "cucsMemoryArrayEnvStatsHistInputCurrentAvg": cucsMemoryArrayEnvStatsHistInputCurrentAvg,
       "cucsMemoryArrayEnvStatsHistInputCurrentMax": cucsMemoryArrayEnvStatsHistInputCurrentMax,
       "cucsMemoryArrayEnvStatsHistInputCurrentMin": cucsMemoryArrayEnvStatsHistInputCurrentMin,
       "cucsMemoryArrayEnvStatsHistMostRecent": cucsMemoryArrayEnvStatsHistMostRecent,
       "cucsMemoryArrayEnvStatsHistSuspect": cucsMemoryArrayEnvStatsHistSuspect,
       "cucsMemoryArrayEnvStatsHistThresholded": cucsMemoryArrayEnvStatsHistThresholded,
       "cucsMemoryArrayEnvStatsHistTimeCollected": cucsMemoryArrayEnvStatsHistTimeCollected,
       "cucsMemoryBufferUnitTable": cucsMemoryBufferUnitTable,
       "cucsMemoryBufferUnitEntry": cucsMemoryBufferUnitEntry,
       "cucsMemoryBufferUnitInstanceId": cucsMemoryBufferUnitInstanceId,
       "cucsMemoryBufferUnitDn": cucsMemoryBufferUnitDn,
       "cucsMemoryBufferUnitRn": cucsMemoryBufferUnitRn,
       "cucsMemoryBufferUnitId": cucsMemoryBufferUnitId,
       "cucsMemoryBufferUnitModel": cucsMemoryBufferUnitModel,
       "cucsMemoryBufferUnitOperState": cucsMemoryBufferUnitOperState,
       "cucsMemoryBufferUnitOperability": cucsMemoryBufferUnitOperability,
       "cucsMemoryBufferUnitPerf": cucsMemoryBufferUnitPerf,
       "cucsMemoryBufferUnitPower": cucsMemoryBufferUnitPower,
       "cucsMemoryBufferUnitPresence": cucsMemoryBufferUnitPresence,
       "cucsMemoryBufferUnitRevision": cucsMemoryBufferUnitRevision,
       "cucsMemoryBufferUnitSerial": cucsMemoryBufferUnitSerial,
       "cucsMemoryBufferUnitThermal": cucsMemoryBufferUnitThermal,
       "cucsMemoryBufferUnitVendor": cucsMemoryBufferUnitVendor,
       "cucsMemoryBufferUnitVoltage": cucsMemoryBufferUnitVoltage,
       "cucsMemoryBufferUnitOperQualifierReason": cucsMemoryBufferUnitOperQualifierReason,
       "cucsMemoryBufferUnitLocationDn": cucsMemoryBufferUnitLocationDn,
       "cucsMemoryBufferUnitEnvStatsTable": cucsMemoryBufferUnitEnvStatsTable,
       "cucsMemoryBufferUnitEnvStatsEntry": cucsMemoryBufferUnitEnvStatsEntry,
       "cucsMemoryBufferUnitEnvStatsInstanceId": cucsMemoryBufferUnitEnvStatsInstanceId,
       "cucsMemoryBufferUnitEnvStatsDn": cucsMemoryBufferUnitEnvStatsDn,
       "cucsMemoryBufferUnitEnvStatsRn": cucsMemoryBufferUnitEnvStatsRn,
       "cucsMemoryBufferUnitEnvStatsIntervals": cucsMemoryBufferUnitEnvStatsIntervals,
       "cucsMemoryBufferUnitEnvStatsSuspect": cucsMemoryBufferUnitEnvStatsSuspect,
       "cucsMemoryBufferUnitEnvStatsTemperature": cucsMemoryBufferUnitEnvStatsTemperature,
       "cucsMemoryBufferUnitEnvStatsTemperatureAvg": cucsMemoryBufferUnitEnvStatsTemperatureAvg,
       "cucsMemoryBufferUnitEnvStatsTemperatureMax": cucsMemoryBufferUnitEnvStatsTemperatureMax,
       "cucsMemoryBufferUnitEnvStatsTemperatureMin": cucsMemoryBufferUnitEnvStatsTemperatureMin,
       "cucsMemoryBufferUnitEnvStatsThresholded": cucsMemoryBufferUnitEnvStatsThresholded,
       "cucsMemoryBufferUnitEnvStatsTimeCollected": cucsMemoryBufferUnitEnvStatsTimeCollected,
       "cucsMemoryBufferUnitEnvStatsUpdate": cucsMemoryBufferUnitEnvStatsUpdate,
       "cucsMemoryBufferUnitEnvStatsHistTable": cucsMemoryBufferUnitEnvStatsHistTable,
       "cucsMemoryBufferUnitEnvStatsHistEntry": cucsMemoryBufferUnitEnvStatsHistEntry,
       "cucsMemoryBufferUnitEnvStatsHistInstanceId": cucsMemoryBufferUnitEnvStatsHistInstanceId,
       "cucsMemoryBufferUnitEnvStatsHistDn": cucsMemoryBufferUnitEnvStatsHistDn,
       "cucsMemoryBufferUnitEnvStatsHistRn": cucsMemoryBufferUnitEnvStatsHistRn,
       "cucsMemoryBufferUnitEnvStatsHistId": cucsMemoryBufferUnitEnvStatsHistId,
       "cucsMemoryBufferUnitEnvStatsHistMostRecent": cucsMemoryBufferUnitEnvStatsHistMostRecent,
       "cucsMemoryBufferUnitEnvStatsHistSuspect": cucsMemoryBufferUnitEnvStatsHistSuspect,
       "cucsMemoryBufferUnitEnvStatsHistTemperature": cucsMemoryBufferUnitEnvStatsHistTemperature,
       "cucsMemoryBufferUnitEnvStatsHistTemperatureAvg": cucsMemoryBufferUnitEnvStatsHistTemperatureAvg,
       "cucsMemoryBufferUnitEnvStatsHistTemperatureMax": cucsMemoryBufferUnitEnvStatsHistTemperatureMax,
       "cucsMemoryBufferUnitEnvStatsHistTemperatureMin": cucsMemoryBufferUnitEnvStatsHistTemperatureMin,
       "cucsMemoryBufferUnitEnvStatsHistThresholded": cucsMemoryBufferUnitEnvStatsHistThresholded,
       "cucsMemoryBufferUnitEnvStatsHistTimeCollected": cucsMemoryBufferUnitEnvStatsHistTimeCollected,
       "cucsMemoryErrorStatsTable": cucsMemoryErrorStatsTable,
       "cucsMemoryErrorStatsEntry": cucsMemoryErrorStatsEntry,
       "cucsMemoryErrorStatsInstanceId": cucsMemoryErrorStatsInstanceId,
       "cucsMemoryErrorStatsDn": cucsMemoryErrorStatsDn,
       "cucsMemoryErrorStatsRn": cucsMemoryErrorStatsRn,
       "cucsMemoryErrorStatsAddressParityErrors": cucsMemoryErrorStatsAddressParityErrors,
       "cucsMemoryErrorStatsAddressParityErrors15Min": cucsMemoryErrorStatsAddressParityErrors15Min,
       "cucsMemoryErrorStatsAddressParityErrors15MinH": cucsMemoryErrorStatsAddressParityErrors15MinH,
       "cucsMemoryErrorStatsAddressParityErrors1Day": cucsMemoryErrorStatsAddressParityErrors1Day,
       "cucsMemoryErrorStatsAddressParityErrors1DayH": cucsMemoryErrorStatsAddressParityErrors1DayH,
       "cucsMemoryErrorStatsAddressParityErrors1Hour": cucsMemoryErrorStatsAddressParityErrors1Hour,
       "cucsMemoryErrorStatsAddressParityErrors1HourH": cucsMemoryErrorStatsAddressParityErrors1HourH,
       "cucsMemoryErrorStatsAddressParityErrors1Week": cucsMemoryErrorStatsAddressParityErrors1Week,
       "cucsMemoryErrorStatsAddressParityErrors1WeekH": cucsMemoryErrorStatsAddressParityErrors1WeekH,
       "cucsMemoryErrorStatsEccMultibitErrors": cucsMemoryErrorStatsEccMultibitErrors,
       "cucsMemoryErrorStatsEccMultibitErrors15Min": cucsMemoryErrorStatsEccMultibitErrors15Min,
       "cucsMemoryErrorStatsEccMultibitErrors15MinH": cucsMemoryErrorStatsEccMultibitErrors15MinH,
       "cucsMemoryErrorStatsEccMultibitErrors1Day": cucsMemoryErrorStatsEccMultibitErrors1Day,
       "cucsMemoryErrorStatsEccMultibitErrors1DayH": cucsMemoryErrorStatsEccMultibitErrors1DayH,
       "cucsMemoryErrorStatsEccMultibitErrors1Hour": cucsMemoryErrorStatsEccMultibitErrors1Hour,
       "cucsMemoryErrorStatsEccMultibitErrors1HourH": cucsMemoryErrorStatsEccMultibitErrors1HourH,
       "cucsMemoryErrorStatsEccMultibitErrors1Week": cucsMemoryErrorStatsEccMultibitErrors1Week,
       "cucsMemoryErrorStatsEccMultibitErrors1WeekH": cucsMemoryErrorStatsEccMultibitErrors1WeekH,
       "cucsMemoryErrorStatsEccSinglebitErrors": cucsMemoryErrorStatsEccSinglebitErrors,
       "cucsMemoryErrorStatsEccSinglebitErrors15Min": cucsMemoryErrorStatsEccSinglebitErrors15Min,
       "cucsMemoryErrorStatsEccSinglebitErrors15MinH": cucsMemoryErrorStatsEccSinglebitErrors15MinH,
       "cucsMemoryErrorStatsEccSinglebitErrors1Day": cucsMemoryErrorStatsEccSinglebitErrors1Day,
       "cucsMemoryErrorStatsEccSinglebitErrors1DayH": cucsMemoryErrorStatsEccSinglebitErrors1DayH,
       "cucsMemoryErrorStatsEccSinglebitErrors1Hour": cucsMemoryErrorStatsEccSinglebitErrors1Hour,
       "cucsMemoryErrorStatsEccSinglebitErrors1HourH": cucsMemoryErrorStatsEccSinglebitErrors1HourH,
       "cucsMemoryErrorStatsEccSinglebitErrors1Week": cucsMemoryErrorStatsEccSinglebitErrors1Week,
       "cucsMemoryErrorStatsEccSinglebitErrors1WeekH": cucsMemoryErrorStatsEccSinglebitErrors1WeekH,
       "cucsMemoryErrorStatsIntervals": cucsMemoryErrorStatsIntervals,
       "cucsMemoryErrorStatsMismatchErrors": cucsMemoryErrorStatsMismatchErrors,
       "cucsMemoryErrorStatsMismatchErrors15Min": cucsMemoryErrorStatsMismatchErrors15Min,
       "cucsMemoryErrorStatsMismatchErrors15MinH": cucsMemoryErrorStatsMismatchErrors15MinH,
       "cucsMemoryErrorStatsMismatchErrors1Day": cucsMemoryErrorStatsMismatchErrors1Day,
       "cucsMemoryErrorStatsMismatchErrors1DayH": cucsMemoryErrorStatsMismatchErrors1DayH,
       "cucsMemoryErrorStatsMismatchErrors1Hour": cucsMemoryErrorStatsMismatchErrors1Hour,
       "cucsMemoryErrorStatsMismatchErrors1HourH": cucsMemoryErrorStatsMismatchErrors1HourH,
       "cucsMemoryErrorStatsMismatchErrors1Week": cucsMemoryErrorStatsMismatchErrors1Week,
       "cucsMemoryErrorStatsMismatchErrors1WeekH": cucsMemoryErrorStatsMismatchErrors1WeekH,
       "cucsMemoryErrorStatsSuspect": cucsMemoryErrorStatsSuspect,
       "cucsMemoryErrorStatsThresholded": cucsMemoryErrorStatsThresholded,
       "cucsMemoryErrorStatsTimeCollected": cucsMemoryErrorStatsTimeCollected,
       "cucsMemoryErrorStatsUpdate": cucsMemoryErrorStatsUpdate,
       "cucsMemoryErrorStatsAddressParityErrors2Weeks": cucsMemoryErrorStatsAddressParityErrors2Weeks,
       "cucsMemoryErrorStatsAddressParityErrors2WeeksH": cucsMemoryErrorStatsAddressParityErrors2WeeksH,
       "cucsMemoryErrorStatsEccMultibitErrors2Weeks": cucsMemoryErrorStatsEccMultibitErrors2Weeks,
       "cucsMemoryErrorStatsEccMultibitErrors2WeeksH": cucsMemoryErrorStatsEccMultibitErrors2WeeksH,
       "cucsMemoryErrorStatsEccSinglebitErrors2Weeks": cucsMemoryErrorStatsEccSinglebitErrors2Weeks,
       "cucsMemoryErrorStatsEccSinglebitErrors2WeeksH": cucsMemoryErrorStatsEccSinglebitErrors2WeeksH,
       "cucsMemoryErrorStatsMismatchErrors2Weeks": cucsMemoryErrorStatsMismatchErrors2Weeks,
       "cucsMemoryErrorStatsMismatchErrors2WeeksH": cucsMemoryErrorStatsMismatchErrors2WeeksH,
       "cucsMemoryQualTable": cucsMemoryQualTable,
       "cucsMemoryQualEntry": cucsMemoryQualEntry,
       "cucsMemoryQualInstanceId": cucsMemoryQualInstanceId,
       "cucsMemoryQualDn": cucsMemoryQualDn,
       "cucsMemoryQualRn": cucsMemoryQualRn,
       "cucsMemoryQualClock": cucsMemoryQualClock,
       "cucsMemoryQualLatency": cucsMemoryQualLatency,
       "cucsMemoryQualMaxCap": cucsMemoryQualMaxCap,
       "cucsMemoryQualMinCap": cucsMemoryQualMinCap,
       "cucsMemoryQualSpeed": cucsMemoryQualSpeed,
       "cucsMemoryQualUnits": cucsMemoryQualUnits,
       "cucsMemoryQualWidth": cucsMemoryQualWidth,
       "cucsMemoryRuntimeTable": cucsMemoryRuntimeTable,
       "cucsMemoryRuntimeEntry": cucsMemoryRuntimeEntry,
       "cucsMemoryRuntimeInstanceId": cucsMemoryRuntimeInstanceId,
       "cucsMemoryRuntimeDn": cucsMemoryRuntimeDn,
       "cucsMemoryRuntimeRn": cucsMemoryRuntimeRn,
       "cucsMemoryRuntimeAvailable": cucsMemoryRuntimeAvailable,
       "cucsMemoryRuntimeAvailableAvg": cucsMemoryRuntimeAvailableAvg,
       "cucsMemoryRuntimeAvailableMax": cucsMemoryRuntimeAvailableMax,
       "cucsMemoryRuntimeAvailableMin": cucsMemoryRuntimeAvailableMin,
       "cucsMemoryRuntimeCached": cucsMemoryRuntimeCached,
       "cucsMemoryRuntimeCachedAvg": cucsMemoryRuntimeCachedAvg,
       "cucsMemoryRuntimeCachedMax": cucsMemoryRuntimeCachedMax,
       "cucsMemoryRuntimeCachedMin": cucsMemoryRuntimeCachedMin,
       "cucsMemoryRuntimeIntervals": cucsMemoryRuntimeIntervals,
       "cucsMemoryRuntimeSuspect": cucsMemoryRuntimeSuspect,
       "cucsMemoryRuntimeThresholded": cucsMemoryRuntimeThresholded,
       "cucsMemoryRuntimeTimeCollected": cucsMemoryRuntimeTimeCollected,
       "cucsMemoryRuntimeTotal": cucsMemoryRuntimeTotal,
       "cucsMemoryRuntimeTotalAvg": cucsMemoryRuntimeTotalAvg,
       "cucsMemoryRuntimeTotalMax": cucsMemoryRuntimeTotalMax,
       "cucsMemoryRuntimeTotalMin": cucsMemoryRuntimeTotalMin,
       "cucsMemoryRuntimeType": cucsMemoryRuntimeType,
       "cucsMemoryRuntimeUpdate": cucsMemoryRuntimeUpdate,
       "cucsMemoryRuntimeHistTable": cucsMemoryRuntimeHistTable,
       "cucsMemoryRuntimeHistEntry": cucsMemoryRuntimeHistEntry,
       "cucsMemoryRuntimeHistInstanceId": cucsMemoryRuntimeHistInstanceId,
       "cucsMemoryRuntimeHistDn": cucsMemoryRuntimeHistDn,
       "cucsMemoryRuntimeHistRn": cucsMemoryRuntimeHistRn,
       "cucsMemoryRuntimeHistAvailable": cucsMemoryRuntimeHistAvailable,
       "cucsMemoryRuntimeHistAvailableAvg": cucsMemoryRuntimeHistAvailableAvg,
       "cucsMemoryRuntimeHistAvailableMax": cucsMemoryRuntimeHistAvailableMax,
       "cucsMemoryRuntimeHistAvailableMin": cucsMemoryRuntimeHistAvailableMin,
       "cucsMemoryRuntimeHistCached": cucsMemoryRuntimeHistCached,
       "cucsMemoryRuntimeHistCachedAvg": cucsMemoryRuntimeHistCachedAvg,
       "cucsMemoryRuntimeHistCachedMax": cucsMemoryRuntimeHistCachedMax,
       "cucsMemoryRuntimeHistCachedMin": cucsMemoryRuntimeHistCachedMin,
       "cucsMemoryRuntimeHistId": cucsMemoryRuntimeHistId,
       "cucsMemoryRuntimeHistMostRecent": cucsMemoryRuntimeHistMostRecent,
       "cucsMemoryRuntimeHistSuspect": cucsMemoryRuntimeHistSuspect,
       "cucsMemoryRuntimeHistThresholded": cucsMemoryRuntimeHistThresholded,
       "cucsMemoryRuntimeHistTimeCollected": cucsMemoryRuntimeHistTimeCollected,
       "cucsMemoryRuntimeHistTotal": cucsMemoryRuntimeHistTotal,
       "cucsMemoryRuntimeHistTotalAvg": cucsMemoryRuntimeHistTotalAvg,
       "cucsMemoryRuntimeHistTotalMax": cucsMemoryRuntimeHistTotalMax,
       "cucsMemoryRuntimeHistTotalMin": cucsMemoryRuntimeHistTotalMin,
       "cucsMemoryUnitTable": cucsMemoryUnitTable,
       "cucsMemoryUnitEntry": cucsMemoryUnitEntry,
       "cucsMemoryUnitInstanceId": cucsMemoryUnitInstanceId,
       "cucsMemoryUnitDn": cucsMemoryUnitDn,
       "cucsMemoryUnitRn": cucsMemoryUnitRn,
       "cucsMemoryUnitArray": cucsMemoryUnitArray,
       "cucsMemoryUnitBank": cucsMemoryUnitBank,
       "cucsMemoryUnitCapacity": cucsMemoryUnitCapacity,
       "cucsMemoryUnitClock": cucsMemoryUnitClock,
       "cucsMemoryUnitFormFactor": cucsMemoryUnitFormFactor,
       "cucsMemoryUnitId": cucsMemoryUnitId,
       "cucsMemoryUnitLatency": cucsMemoryUnitLatency,
       "cucsMemoryUnitLocation": cucsMemoryUnitLocation,
       "cucsMemoryUnitModel": cucsMemoryUnitModel,
       "cucsMemoryUnitOperState": cucsMemoryUnitOperState,
       "cucsMemoryUnitOperability": cucsMemoryUnitOperability,
       "cucsMemoryUnitPerf": cucsMemoryUnitPerf,
       "cucsMemoryUnitPower": cucsMemoryUnitPower,
       "cucsMemoryUnitPresence": cucsMemoryUnitPresence,
       "cucsMemoryUnitRevision": cucsMemoryUnitRevision,
       "cucsMemoryUnitSerial": cucsMemoryUnitSerial,
       "cucsMemoryUnitSet": cucsMemoryUnitSet,
       "cucsMemoryUnitSpeed": cucsMemoryUnitSpeed,
       "cucsMemoryUnitThermal": cucsMemoryUnitThermal,
       "cucsMemoryUnitType": cucsMemoryUnitType,
       "cucsMemoryUnitVendor": cucsMemoryUnitVendor,
       "cucsMemoryUnitVisibility": cucsMemoryUnitVisibility,
       "cucsMemoryUnitVoltage": cucsMemoryUnitVoltage,
       "cucsMemoryUnitWidth": cucsMemoryUnitWidth,
       "cucsMemoryUnitAdminState": cucsMemoryUnitAdminState,
       "cucsMemoryUnitOperQualifier": cucsMemoryUnitOperQualifier,
       "cucsMemoryUnitOperQualifierReason": cucsMemoryUnitOperQualifierReason,
       "cucsMemoryUnitLocationDn": cucsMemoryUnitLocationDn,
       "cucsMemoryUnitEnvStatsTable": cucsMemoryUnitEnvStatsTable,
       "cucsMemoryUnitEnvStatsEntry": cucsMemoryUnitEnvStatsEntry,
       "cucsMemoryUnitEnvStatsInstanceId": cucsMemoryUnitEnvStatsInstanceId,
       "cucsMemoryUnitEnvStatsDn": cucsMemoryUnitEnvStatsDn,
       "cucsMemoryUnitEnvStatsRn": cucsMemoryUnitEnvStatsRn,
       "cucsMemoryUnitEnvStatsIntervals": cucsMemoryUnitEnvStatsIntervals,
       "cucsMemoryUnitEnvStatsSuspect": cucsMemoryUnitEnvStatsSuspect,
       "cucsMemoryUnitEnvStatsTemperature": cucsMemoryUnitEnvStatsTemperature,
       "cucsMemoryUnitEnvStatsTemperatureAvg": cucsMemoryUnitEnvStatsTemperatureAvg,
       "cucsMemoryUnitEnvStatsTemperatureMax": cucsMemoryUnitEnvStatsTemperatureMax,
       "cucsMemoryUnitEnvStatsTemperatureMin": cucsMemoryUnitEnvStatsTemperatureMin,
       "cucsMemoryUnitEnvStatsThresholded": cucsMemoryUnitEnvStatsThresholded,
       "cucsMemoryUnitEnvStatsTimeCollected": cucsMemoryUnitEnvStatsTimeCollected,
       "cucsMemoryUnitEnvStatsUpdate": cucsMemoryUnitEnvStatsUpdate,
       "cucsMemoryUnitEnvStatsHistTable": cucsMemoryUnitEnvStatsHistTable,
       "cucsMemoryUnitEnvStatsHistEntry": cucsMemoryUnitEnvStatsHistEntry,
       "cucsMemoryUnitEnvStatsHistInstanceId": cucsMemoryUnitEnvStatsHistInstanceId,
       "cucsMemoryUnitEnvStatsHistDn": cucsMemoryUnitEnvStatsHistDn,
       "cucsMemoryUnitEnvStatsHistRn": cucsMemoryUnitEnvStatsHistRn,
       "cucsMemoryUnitEnvStatsHistId": cucsMemoryUnitEnvStatsHistId,
       "cucsMemoryUnitEnvStatsHistMostRecent": cucsMemoryUnitEnvStatsHistMostRecent,
       "cucsMemoryUnitEnvStatsHistSuspect": cucsMemoryUnitEnvStatsHistSuspect,
       "cucsMemoryUnitEnvStatsHistTemperature": cucsMemoryUnitEnvStatsHistTemperature,
       "cucsMemoryUnitEnvStatsHistTemperatureAvg": cucsMemoryUnitEnvStatsHistTemperatureAvg,
       "cucsMemoryUnitEnvStatsHistTemperatureMax": cucsMemoryUnitEnvStatsHistTemperatureMax,
       "cucsMemoryUnitEnvStatsHistTemperatureMin": cucsMemoryUnitEnvStatsHistTemperatureMin,
       "cucsMemoryUnitEnvStatsHistThresholded": cucsMemoryUnitEnvStatsHistThresholded,
       "cucsMemoryUnitEnvStatsHistTimeCollected": cucsMemoryUnitEnvStatsHistTimeCollected}
)

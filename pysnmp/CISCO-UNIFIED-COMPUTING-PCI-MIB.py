# SNMP MIB module (CISCO-UNIFIED-COMPUTING-PCI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-PCI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:07 2024
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

(CucsEquipmentDiscoveryState,
 CucsEquipmentOperability,
 CucsEquipmentPowerState,
 CucsEquipmentPresence,
 CucsEquipmentSensorThresholdStatus,
 CucsPciEquipSlotId) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsEquipmentDiscoveryState",
    "CucsEquipmentOperability",
    "CucsEquipmentPowerState",
    "CucsEquipmentPresence",
    "CucsEquipmentSensorThresholdStatus",
    "CucsPciEquipSlotId")

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

cucsPciObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsPciUnitTable_Object = MibTable
cucsPciUnitTable = _CucsPciUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1)
)
if mibBuilder.loadTexts:
    cucsPciUnitTable.setStatus("current")
_CucsPciUnitEntry_Object = MibTableRow
cucsPciUnitEntry = _CucsPciUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1)
)
cucsPciUnitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PCI-MIB", "cucsPciUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPciUnitEntry.setStatus("current")
_CucsPciUnitInstanceId_Type = CucsManagedObjectId
_CucsPciUnitInstanceId_Object = MibTableColumn
cucsPciUnitInstanceId = _CucsPciUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 1),
    _CucsPciUnitInstanceId_Type()
)
cucsPciUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPciUnitInstanceId.setStatus("current")
_CucsPciUnitDn_Type = CucsManagedObjectDn
_CucsPciUnitDn_Object = MibTableColumn
cucsPciUnitDn = _CucsPciUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 2),
    _CucsPciUnitDn_Type()
)
cucsPciUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitDn.setStatus("current")
_CucsPciUnitRn_Type = SnmpAdminString
_CucsPciUnitRn_Object = MibTableColumn
cucsPciUnitRn = _CucsPciUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 3),
    _CucsPciUnitRn_Type()
)
cucsPciUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitRn.setStatus("current")
_CucsPciUnitId_Type = Gauge32
_CucsPciUnitId_Object = MibTableColumn
cucsPciUnitId = _CucsPciUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 4),
    _CucsPciUnitId_Type()
)
cucsPciUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitId.setStatus("current")
_CucsPciUnitModel_Type = SnmpAdminString
_CucsPciUnitModel_Object = MibTableColumn
cucsPciUnitModel = _CucsPciUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 5),
    _CucsPciUnitModel_Type()
)
cucsPciUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitModel.setStatus("current")
_CucsPciUnitOperState_Type = CucsEquipmentOperability
_CucsPciUnitOperState_Object = MibTableColumn
cucsPciUnitOperState = _CucsPciUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 6),
    _CucsPciUnitOperState_Type()
)
cucsPciUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitOperState.setStatus("current")
_CucsPciUnitOperability_Type = CucsEquipmentOperability
_CucsPciUnitOperability_Object = MibTableColumn
cucsPciUnitOperability = _CucsPciUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 7),
    _CucsPciUnitOperability_Type()
)
cucsPciUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitOperability.setStatus("current")
_CucsPciUnitPciAddr_Type = SnmpAdminString
_CucsPciUnitPciAddr_Object = MibTableColumn
cucsPciUnitPciAddr = _CucsPciUnitPciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 8),
    _CucsPciUnitPciAddr_Type()
)
cucsPciUnitPciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitPciAddr.setStatus("current")
_CucsPciUnitPciSlot_Type = SnmpAdminString
_CucsPciUnitPciSlot_Object = MibTableColumn
cucsPciUnitPciSlot = _CucsPciUnitPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 9),
    _CucsPciUnitPciSlot_Type()
)
cucsPciUnitPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitPciSlot.setStatus("current")
_CucsPciUnitPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsPciUnitPerf_Object = MibTableColumn
cucsPciUnitPerf = _CucsPciUnitPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 10),
    _CucsPciUnitPerf_Type()
)
cucsPciUnitPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitPerf.setStatus("current")
_CucsPciUnitPower_Type = CucsEquipmentPowerState
_CucsPciUnitPower_Object = MibTableColumn
cucsPciUnitPower = _CucsPciUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 11),
    _CucsPciUnitPower_Type()
)
cucsPciUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitPower.setStatus("current")
_CucsPciUnitPresence_Type = CucsEquipmentPresence
_CucsPciUnitPresence_Object = MibTableColumn
cucsPciUnitPresence = _CucsPciUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 12),
    _CucsPciUnitPresence_Type()
)
cucsPciUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitPresence.setStatus("current")
_CucsPciUnitRevision_Type = SnmpAdminString
_CucsPciUnitRevision_Object = MibTableColumn
cucsPciUnitRevision = _CucsPciUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 13),
    _CucsPciUnitRevision_Type()
)
cucsPciUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitRevision.setStatus("current")
_CucsPciUnitSerial_Type = SnmpAdminString
_CucsPciUnitSerial_Object = MibTableColumn
cucsPciUnitSerial = _CucsPciUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 14),
    _CucsPciUnitSerial_Type()
)
cucsPciUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitSerial.setStatus("current")
_CucsPciUnitThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsPciUnitThermal_Object = MibTableColumn
cucsPciUnitThermal = _CucsPciUnitThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 15),
    _CucsPciUnitThermal_Type()
)
cucsPciUnitThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitThermal.setStatus("current")
_CucsPciUnitVendor_Type = SnmpAdminString
_CucsPciUnitVendor_Object = MibTableColumn
cucsPciUnitVendor = _CucsPciUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 16),
    _CucsPciUnitVendor_Type()
)
cucsPciUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitVendor.setStatus("current")
_CucsPciUnitVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsPciUnitVoltage_Object = MibTableColumn
cucsPciUnitVoltage = _CucsPciUnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 17),
    _CucsPciUnitVoltage_Type()
)
cucsPciUnitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitVoltage.setStatus("current")
_CucsPciUnitOperQualifierReason_Type = SnmpAdminString
_CucsPciUnitOperQualifierReason_Object = MibTableColumn
cucsPciUnitOperQualifierReason = _CucsPciUnitOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 18),
    _CucsPciUnitOperQualifierReason_Type()
)
cucsPciUnitOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitOperQualifierReason.setStatus("current")
_CucsPciUnitLocationDn_Type = SnmpAdminString
_CucsPciUnitLocationDn_Object = MibTableColumn
cucsPciUnitLocationDn = _CucsPciUnitLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 1, 1, 19),
    _CucsPciUnitLocationDn_Type()
)
cucsPciUnitLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciUnitLocationDn.setStatus("current")
_CucsPciEquipSlotTable_Object = MibTable
cucsPciEquipSlotTable = _CucsPciEquipSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2)
)
if mibBuilder.loadTexts:
    cucsPciEquipSlotTable.setStatus("current")
_CucsPciEquipSlotEntry_Object = MibTableRow
cucsPciEquipSlotEntry = _CucsPciEquipSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1)
)
cucsPciEquipSlotEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PCI-MIB", "cucsPciEquipSlotInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPciEquipSlotEntry.setStatus("current")
_CucsPciEquipSlotInstanceId_Type = CucsManagedObjectId
_CucsPciEquipSlotInstanceId_Object = MibTableColumn
cucsPciEquipSlotInstanceId = _CucsPciEquipSlotInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 1),
    _CucsPciEquipSlotInstanceId_Type()
)
cucsPciEquipSlotInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPciEquipSlotInstanceId.setStatus("current")
_CucsPciEquipSlotDn_Type = CucsManagedObjectDn
_CucsPciEquipSlotDn_Object = MibTableColumn
cucsPciEquipSlotDn = _CucsPciEquipSlotDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 2),
    _CucsPciEquipSlotDn_Type()
)
cucsPciEquipSlotDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotDn.setStatus("current")
_CucsPciEquipSlotRn_Type = SnmpAdminString
_CucsPciEquipSlotRn_Object = MibTableColumn
cucsPciEquipSlotRn = _CucsPciEquipSlotRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 3),
    _CucsPciEquipSlotRn_Type()
)
cucsPciEquipSlotRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotRn.setStatus("current")
_CucsPciEquipSlotControllerReported_Type = SnmpAdminString
_CucsPciEquipSlotControllerReported_Object = MibTableColumn
cucsPciEquipSlotControllerReported = _CucsPciEquipSlotControllerReported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 4),
    _CucsPciEquipSlotControllerReported_Type()
)
cucsPciEquipSlotControllerReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotControllerReported.setStatus("current")
_CucsPciEquipSlotDiscoveryState_Type = CucsEquipmentDiscoveryState
_CucsPciEquipSlotDiscoveryState_Object = MibTableColumn
cucsPciEquipSlotDiscoveryState = _CucsPciEquipSlotDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 5),
    _CucsPciEquipSlotDiscoveryState_Type()
)
cucsPciEquipSlotDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotDiscoveryState.setStatus("current")
_CucsPciEquipSlotFltAggr_Type = Unsigned64
_CucsPciEquipSlotFltAggr_Object = MibTableColumn
cucsPciEquipSlotFltAggr = _CucsPciEquipSlotFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 6),
    _CucsPciEquipSlotFltAggr_Type()
)
cucsPciEquipSlotFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotFltAggr.setStatus("current")
_CucsPciEquipSlotHostReported_Type = SnmpAdminString
_CucsPciEquipSlotHostReported_Object = MibTableColumn
cucsPciEquipSlotHostReported = _CucsPciEquipSlotHostReported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 7),
    _CucsPciEquipSlotHostReported_Type()
)
cucsPciEquipSlotHostReported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotHostReported.setStatus("current")
_CucsPciEquipSlotId_Type = CucsPciEquipSlotId
_CucsPciEquipSlotId_Object = MibTableColumn
cucsPciEquipSlotId = _CucsPciEquipSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 8),
    _CucsPciEquipSlotId_Type()
)
cucsPciEquipSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotId.setStatus("current")
_CucsPciEquipSlotMacLeft_Type = MacAddress
_CucsPciEquipSlotMacLeft_Object = MibTableColumn
cucsPciEquipSlotMacLeft = _CucsPciEquipSlotMacLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 9),
    _CucsPciEquipSlotMacLeft_Type()
)
cucsPciEquipSlotMacLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotMacLeft.setStatus("current")
_CucsPciEquipSlotMacRight_Type = MacAddress
_CucsPciEquipSlotMacRight_Object = MibTableColumn
cucsPciEquipSlotMacRight = _CucsPciEquipSlotMacRight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 10),
    _CucsPciEquipSlotMacRight_Type()
)
cucsPciEquipSlotMacRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotMacRight.setStatus("current")
_CucsPciEquipSlotModel_Type = SnmpAdminString
_CucsPciEquipSlotModel_Object = MibTableColumn
cucsPciEquipSlotModel = _CucsPciEquipSlotModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 11),
    _CucsPciEquipSlotModel_Type()
)
cucsPciEquipSlotModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotModel.setStatus("current")
_CucsPciEquipSlotRevision_Type = SnmpAdminString
_CucsPciEquipSlotRevision_Object = MibTableColumn
cucsPciEquipSlotRevision = _CucsPciEquipSlotRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 12),
    _CucsPciEquipSlotRevision_Type()
)
cucsPciEquipSlotRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotRevision.setStatus("current")
_CucsPciEquipSlotSerial_Type = SnmpAdminString
_CucsPciEquipSlotSerial_Object = MibTableColumn
cucsPciEquipSlotSerial = _CucsPciEquipSlotSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 13),
    _CucsPciEquipSlotSerial_Type()
)
cucsPciEquipSlotSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotSerial.setStatus("current")
_CucsPciEquipSlotSmbiosId_Type = Gauge32
_CucsPciEquipSlotSmbiosId_Object = MibTableColumn
cucsPciEquipSlotSmbiosId = _CucsPciEquipSlotSmbiosId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 14),
    _CucsPciEquipSlotSmbiosId_Type()
)
cucsPciEquipSlotSmbiosId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotSmbiosId.setStatus("current")
_CucsPciEquipSlotVendor_Type = SnmpAdminString
_CucsPciEquipSlotVendor_Object = MibTableColumn
cucsPciEquipSlotVendor = _CucsPciEquipSlotVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 36, 2, 1, 15),
    _CucsPciEquipSlotVendor_Type()
)
cucsPciEquipSlotVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPciEquipSlotVendor.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-PCI-MIB",
    **{"cucsPciObjects": cucsPciObjects,
       "cucsPciUnitTable": cucsPciUnitTable,
       "cucsPciUnitEntry": cucsPciUnitEntry,
       "cucsPciUnitInstanceId": cucsPciUnitInstanceId,
       "cucsPciUnitDn": cucsPciUnitDn,
       "cucsPciUnitRn": cucsPciUnitRn,
       "cucsPciUnitId": cucsPciUnitId,
       "cucsPciUnitModel": cucsPciUnitModel,
       "cucsPciUnitOperState": cucsPciUnitOperState,
       "cucsPciUnitOperability": cucsPciUnitOperability,
       "cucsPciUnitPciAddr": cucsPciUnitPciAddr,
       "cucsPciUnitPciSlot": cucsPciUnitPciSlot,
       "cucsPciUnitPerf": cucsPciUnitPerf,
       "cucsPciUnitPower": cucsPciUnitPower,
       "cucsPciUnitPresence": cucsPciUnitPresence,
       "cucsPciUnitRevision": cucsPciUnitRevision,
       "cucsPciUnitSerial": cucsPciUnitSerial,
       "cucsPciUnitThermal": cucsPciUnitThermal,
       "cucsPciUnitVendor": cucsPciUnitVendor,
       "cucsPciUnitVoltage": cucsPciUnitVoltage,
       "cucsPciUnitOperQualifierReason": cucsPciUnitOperQualifierReason,
       "cucsPciUnitLocationDn": cucsPciUnitLocationDn,
       "cucsPciEquipSlotTable": cucsPciEquipSlotTable,
       "cucsPciEquipSlotEntry": cucsPciEquipSlotEntry,
       "cucsPciEquipSlotInstanceId": cucsPciEquipSlotInstanceId,
       "cucsPciEquipSlotDn": cucsPciEquipSlotDn,
       "cucsPciEquipSlotRn": cucsPciEquipSlotRn,
       "cucsPciEquipSlotControllerReported": cucsPciEquipSlotControllerReported,
       "cucsPciEquipSlotDiscoveryState": cucsPciEquipSlotDiscoveryState,
       "cucsPciEquipSlotFltAggr": cucsPciEquipSlotFltAggr,
       "cucsPciEquipSlotHostReported": cucsPciEquipSlotHostReported,
       "cucsPciEquipSlotId": cucsPciEquipSlotId,
       "cucsPciEquipSlotMacLeft": cucsPciEquipSlotMacLeft,
       "cucsPciEquipSlotMacRight": cucsPciEquipSlotMacRight,
       "cucsPciEquipSlotModel": cucsPciEquipSlotModel,
       "cucsPciEquipSlotRevision": cucsPciEquipSlotRevision,
       "cucsPciEquipSlotSerial": cucsPciEquipSlotSerial,
       "cucsPciEquipSlotSmbiosId": cucsPciEquipSlotSmbiosId,
       "cucsPciEquipSlotVendor": cucsPciEquipSlotVendor}
)

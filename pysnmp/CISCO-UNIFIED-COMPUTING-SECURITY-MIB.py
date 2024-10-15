# SNMP MIB module (CISCO-UNIFIED-COMPUTING-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:17 2024
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
 CucsSecurityUnitId) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsEquipmentOperability",
    "CucsEquipmentPowerState",
    "CucsEquipmentPresence",
    "CucsEquipmentSensorThresholdStatus",
    "CucsSecurityUnitId")

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

cucsSecurityObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsSecurityUnitTable_Object = MibTable
cucsSecurityUnitTable = _CucsSecurityUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1)
)
if mibBuilder.loadTexts:
    cucsSecurityUnitTable.setStatus("current")
_CucsSecurityUnitEntry_Object = MibTableRow
cucsSecurityUnitEntry = _CucsSecurityUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1)
)
cucsSecurityUnitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SECURITY-MIB", "cucsSecurityUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSecurityUnitEntry.setStatus("current")
_CucsSecurityUnitInstanceId_Type = CucsManagedObjectId
_CucsSecurityUnitInstanceId_Object = MibTableColumn
cucsSecurityUnitInstanceId = _CucsSecurityUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 1),
    _CucsSecurityUnitInstanceId_Type()
)
cucsSecurityUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSecurityUnitInstanceId.setStatus("current")
_CucsSecurityUnitDn_Type = CucsManagedObjectDn
_CucsSecurityUnitDn_Object = MibTableColumn
cucsSecurityUnitDn = _CucsSecurityUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 2),
    _CucsSecurityUnitDn_Type()
)
cucsSecurityUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitDn.setStatus("current")
_CucsSecurityUnitRn_Type = SnmpAdminString
_CucsSecurityUnitRn_Object = MibTableColumn
cucsSecurityUnitRn = _CucsSecurityUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 3),
    _CucsSecurityUnitRn_Type()
)
cucsSecurityUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitRn.setStatus("current")
_CucsSecurityUnitId_Type = CucsSecurityUnitId
_CucsSecurityUnitId_Object = MibTableColumn
cucsSecurityUnitId = _CucsSecurityUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 4),
    _CucsSecurityUnitId_Type()
)
cucsSecurityUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitId.setStatus("current")
_CucsSecurityUnitLocationDn_Type = SnmpAdminString
_CucsSecurityUnitLocationDn_Object = MibTableColumn
cucsSecurityUnitLocationDn = _CucsSecurityUnitLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 5),
    _CucsSecurityUnitLocationDn_Type()
)
cucsSecurityUnitLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitLocationDn.setStatus("current")
_CucsSecurityUnitModel_Type = SnmpAdminString
_CucsSecurityUnitModel_Object = MibTableColumn
cucsSecurityUnitModel = _CucsSecurityUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 6),
    _CucsSecurityUnitModel_Type()
)
cucsSecurityUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitModel.setStatus("current")
_CucsSecurityUnitOperQualifierReason_Type = SnmpAdminString
_CucsSecurityUnitOperQualifierReason_Object = MibTableColumn
cucsSecurityUnitOperQualifierReason = _CucsSecurityUnitOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 7),
    _CucsSecurityUnitOperQualifierReason_Type()
)
cucsSecurityUnitOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitOperQualifierReason.setStatus("current")
_CucsSecurityUnitOperState_Type = CucsEquipmentOperability
_CucsSecurityUnitOperState_Object = MibTableColumn
cucsSecurityUnitOperState = _CucsSecurityUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 8),
    _CucsSecurityUnitOperState_Type()
)
cucsSecurityUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitOperState.setStatus("current")
_CucsSecurityUnitOperability_Type = CucsEquipmentOperability
_CucsSecurityUnitOperability_Object = MibTableColumn
cucsSecurityUnitOperability = _CucsSecurityUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 9),
    _CucsSecurityUnitOperability_Type()
)
cucsSecurityUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitOperability.setStatus("current")
_CucsSecurityUnitPartNumber_Type = SnmpAdminString
_CucsSecurityUnitPartNumber_Object = MibTableColumn
cucsSecurityUnitPartNumber = _CucsSecurityUnitPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 10),
    _CucsSecurityUnitPartNumber_Type()
)
cucsSecurityUnitPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitPartNumber.setStatus("current")
_CucsSecurityUnitPciAddr_Type = SnmpAdminString
_CucsSecurityUnitPciAddr_Object = MibTableColumn
cucsSecurityUnitPciAddr = _CucsSecurityUnitPciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 11),
    _CucsSecurityUnitPciAddr_Type()
)
cucsSecurityUnitPciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitPciAddr.setStatus("current")
_CucsSecurityUnitPciSlot_Type = SnmpAdminString
_CucsSecurityUnitPciSlot_Object = MibTableColumn
cucsSecurityUnitPciSlot = _CucsSecurityUnitPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 12),
    _CucsSecurityUnitPciSlot_Type()
)
cucsSecurityUnitPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitPciSlot.setStatus("current")
_CucsSecurityUnitPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsSecurityUnitPerf_Object = MibTableColumn
cucsSecurityUnitPerf = _CucsSecurityUnitPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 13),
    _CucsSecurityUnitPerf_Type()
)
cucsSecurityUnitPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitPerf.setStatus("current")
_CucsSecurityUnitPower_Type = CucsEquipmentPowerState
_CucsSecurityUnitPower_Object = MibTableColumn
cucsSecurityUnitPower = _CucsSecurityUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 14),
    _CucsSecurityUnitPower_Type()
)
cucsSecurityUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitPower.setStatus("current")
_CucsSecurityUnitPresence_Type = CucsEquipmentPresence
_CucsSecurityUnitPresence_Object = MibTableColumn
cucsSecurityUnitPresence = _CucsSecurityUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 15),
    _CucsSecurityUnitPresence_Type()
)
cucsSecurityUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitPresence.setStatus("current")
_CucsSecurityUnitRevision_Type = SnmpAdminString
_CucsSecurityUnitRevision_Object = MibTableColumn
cucsSecurityUnitRevision = _CucsSecurityUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 16),
    _CucsSecurityUnitRevision_Type()
)
cucsSecurityUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitRevision.setStatus("current")
_CucsSecurityUnitSerial_Type = SnmpAdminString
_CucsSecurityUnitSerial_Object = MibTableColumn
cucsSecurityUnitSerial = _CucsSecurityUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 17),
    _CucsSecurityUnitSerial_Type()
)
cucsSecurityUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitSerial.setStatus("current")
_CucsSecurityUnitThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsSecurityUnitThermal_Object = MibTableColumn
cucsSecurityUnitThermal = _CucsSecurityUnitThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 18),
    _CucsSecurityUnitThermal_Type()
)
cucsSecurityUnitThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitThermal.setStatus("current")
_CucsSecurityUnitVendor_Type = SnmpAdminString
_CucsSecurityUnitVendor_Object = MibTableColumn
cucsSecurityUnitVendor = _CucsSecurityUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 19),
    _CucsSecurityUnitVendor_Type()
)
cucsSecurityUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitVendor.setStatus("current")
_CucsSecurityUnitVid_Type = SnmpAdminString
_CucsSecurityUnitVid_Object = MibTableColumn
cucsSecurityUnitVid = _CucsSecurityUnitVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 20),
    _CucsSecurityUnitVid_Type()
)
cucsSecurityUnitVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitVid.setStatus("current")
_CucsSecurityUnitVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsSecurityUnitVoltage_Object = MibTableColumn
cucsSecurityUnitVoltage = _CucsSecurityUnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 21),
    _CucsSecurityUnitVoltage_Type()
)
cucsSecurityUnitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSecurityUnitVoltage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-SECURITY-MIB",
    **{"cucsSecurityObjects": cucsSecurityObjects,
       "cucsSecurityUnitTable": cucsSecurityUnitTable,
       "cucsSecurityUnitEntry": cucsSecurityUnitEntry,
       "cucsSecurityUnitInstanceId": cucsSecurityUnitInstanceId,
       "cucsSecurityUnitDn": cucsSecurityUnitDn,
       "cucsSecurityUnitRn": cucsSecurityUnitRn,
       "cucsSecurityUnitId": cucsSecurityUnitId,
       "cucsSecurityUnitLocationDn": cucsSecurityUnitLocationDn,
       "cucsSecurityUnitModel": cucsSecurityUnitModel,
       "cucsSecurityUnitOperQualifierReason": cucsSecurityUnitOperQualifierReason,
       "cucsSecurityUnitOperState": cucsSecurityUnitOperState,
       "cucsSecurityUnitOperability": cucsSecurityUnitOperability,
       "cucsSecurityUnitPartNumber": cucsSecurityUnitPartNumber,
       "cucsSecurityUnitPciAddr": cucsSecurityUnitPciAddr,
       "cucsSecurityUnitPciSlot": cucsSecurityUnitPciSlot,
       "cucsSecurityUnitPerf": cucsSecurityUnitPerf,
       "cucsSecurityUnitPower": cucsSecurityUnitPower,
       "cucsSecurityUnitPresence": cucsSecurityUnitPresence,
       "cucsSecurityUnitRevision": cucsSecurityUnitRevision,
       "cucsSecurityUnitSerial": cucsSecurityUnitSerial,
       "cucsSecurityUnitThermal": cucsSecurityUnitThermal,
       "cucsSecurityUnitVendor": cucsSecurityUnitVendor,
       "cucsSecurityUnitVid": cucsSecurityUnitVid,
       "cucsSecurityUnitVoltage": cucsSecurityUnitVoltage}
)

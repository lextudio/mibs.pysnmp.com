# SNMP MIB module (CISCO-UNIFIED-COMPUTING-GRAPHICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-GRAPHICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:38 2024
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
 CucsFsmLifecycle) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsEquipmentOperability",
    "CucsEquipmentPowerState",
    "CucsEquipmentPresence",
    "CucsEquipmentSensorThresholdStatus",
    "CucsFsmLifecycle")

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

cucsGraphicsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsGraphicsCardTable_Object = MibTable
cucsGraphicsCardTable = _CucsGraphicsCardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1)
)
if mibBuilder.loadTexts:
    cucsGraphicsCardTable.setStatus("current")
_CucsGraphicsCardEntry_Object = MibTableRow
cucsGraphicsCardEntry = _CucsGraphicsCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1)
)
cucsGraphicsCardEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-GRAPHICS-MIB", "cucsGraphicsCardInstanceId"),
)
if mibBuilder.loadTexts:
    cucsGraphicsCardEntry.setStatus("current")
_CucsGraphicsCardInstanceId_Type = CucsManagedObjectId
_CucsGraphicsCardInstanceId_Object = MibTableColumn
cucsGraphicsCardInstanceId = _CucsGraphicsCardInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 1),
    _CucsGraphicsCardInstanceId_Type()
)
cucsGraphicsCardInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsGraphicsCardInstanceId.setStatus("current")
_CucsGraphicsCardDn_Type = CucsManagedObjectDn
_CucsGraphicsCardDn_Object = MibTableColumn
cucsGraphicsCardDn = _CucsGraphicsCardDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 2),
    _CucsGraphicsCardDn_Type()
)
cucsGraphicsCardDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardDn.setStatus("current")
_CucsGraphicsCardRn_Type = SnmpAdminString
_CucsGraphicsCardRn_Object = MibTableColumn
cucsGraphicsCardRn = _CucsGraphicsCardRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 3),
    _CucsGraphicsCardRn_Type()
)
cucsGraphicsCardRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardRn.setStatus("current")
_CucsGraphicsCardDeviceId_Type = Gauge32
_CucsGraphicsCardDeviceId_Object = MibTableColumn
cucsGraphicsCardDeviceId = _CucsGraphicsCardDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 4),
    _CucsGraphicsCardDeviceId_Type()
)
cucsGraphicsCardDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardDeviceId.setStatus("current")
_CucsGraphicsCardId_Type = Gauge32
_CucsGraphicsCardId_Object = MibTableColumn
cucsGraphicsCardId = _CucsGraphicsCardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 5),
    _CucsGraphicsCardId_Type()
)
cucsGraphicsCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardId.setStatus("current")
_CucsGraphicsCardIsSupported_Type = TruthValue
_CucsGraphicsCardIsSupported_Object = MibTableColumn
cucsGraphicsCardIsSupported = _CucsGraphicsCardIsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 6),
    _CucsGraphicsCardIsSupported_Type()
)
cucsGraphicsCardIsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardIsSupported.setStatus("current")
_CucsGraphicsCardLc_Type = CucsFsmLifecycle
_CucsGraphicsCardLc_Object = MibTableColumn
cucsGraphicsCardLc = _CucsGraphicsCardLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 7),
    _CucsGraphicsCardLc_Type()
)
cucsGraphicsCardLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardLc.setStatus("current")
_CucsGraphicsCardModel_Type = SnmpAdminString
_CucsGraphicsCardModel_Object = MibTableColumn
cucsGraphicsCardModel = _CucsGraphicsCardModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 8),
    _CucsGraphicsCardModel_Type()
)
cucsGraphicsCardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardModel.setStatus("current")
_CucsGraphicsCardOperQualifierReason_Type = SnmpAdminString
_CucsGraphicsCardOperQualifierReason_Object = MibTableColumn
cucsGraphicsCardOperQualifierReason = _CucsGraphicsCardOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 9),
    _CucsGraphicsCardOperQualifierReason_Type()
)
cucsGraphicsCardOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardOperQualifierReason.setStatus("current")
_CucsGraphicsCardOperState_Type = CucsEquipmentOperability
_CucsGraphicsCardOperState_Object = MibTableColumn
cucsGraphicsCardOperState = _CucsGraphicsCardOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 10),
    _CucsGraphicsCardOperState_Type()
)
cucsGraphicsCardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardOperState.setStatus("current")
_CucsGraphicsCardOperability_Type = CucsEquipmentOperability
_CucsGraphicsCardOperability_Object = MibTableColumn
cucsGraphicsCardOperability = _CucsGraphicsCardOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 11),
    _CucsGraphicsCardOperability_Type()
)
cucsGraphicsCardOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardOperability.setStatus("current")
_CucsGraphicsCardPciAddr_Type = SnmpAdminString
_CucsGraphicsCardPciAddr_Object = MibTableColumn
cucsGraphicsCardPciAddr = _CucsGraphicsCardPciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 12),
    _CucsGraphicsCardPciAddr_Type()
)
cucsGraphicsCardPciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardPciAddr.setStatus("current")
_CucsGraphicsCardPciSlot_Type = SnmpAdminString
_CucsGraphicsCardPciSlot_Object = MibTableColumn
cucsGraphicsCardPciSlot = _CucsGraphicsCardPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 13),
    _CucsGraphicsCardPciSlot_Type()
)
cucsGraphicsCardPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardPciSlot.setStatus("current")
_CucsGraphicsCardPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsGraphicsCardPerf_Object = MibTableColumn
cucsGraphicsCardPerf = _CucsGraphicsCardPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 14),
    _CucsGraphicsCardPerf_Type()
)
cucsGraphicsCardPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardPerf.setStatus("current")
_CucsGraphicsCardPower_Type = CucsEquipmentPowerState
_CucsGraphicsCardPower_Object = MibTableColumn
cucsGraphicsCardPower = _CucsGraphicsCardPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 15),
    _CucsGraphicsCardPower_Type()
)
cucsGraphicsCardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardPower.setStatus("current")
_CucsGraphicsCardPresence_Type = CucsEquipmentPresence
_CucsGraphicsCardPresence_Object = MibTableColumn
cucsGraphicsCardPresence = _CucsGraphicsCardPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 16),
    _CucsGraphicsCardPresence_Type()
)
cucsGraphicsCardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardPresence.setStatus("current")
_CucsGraphicsCardRevision_Type = SnmpAdminString
_CucsGraphicsCardRevision_Object = MibTableColumn
cucsGraphicsCardRevision = _CucsGraphicsCardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 17),
    _CucsGraphicsCardRevision_Type()
)
cucsGraphicsCardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardRevision.setStatus("current")
_CucsGraphicsCardSerial_Type = SnmpAdminString
_CucsGraphicsCardSerial_Object = MibTableColumn
cucsGraphicsCardSerial = _CucsGraphicsCardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 18),
    _CucsGraphicsCardSerial_Type()
)
cucsGraphicsCardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardSerial.setStatus("current")
_CucsGraphicsCardSubDeviceId_Type = Gauge32
_CucsGraphicsCardSubDeviceId_Object = MibTableColumn
cucsGraphicsCardSubDeviceId = _CucsGraphicsCardSubDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 19),
    _CucsGraphicsCardSubDeviceId_Type()
)
cucsGraphicsCardSubDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardSubDeviceId.setStatus("current")
_CucsGraphicsCardSubVendorId_Type = Gauge32
_CucsGraphicsCardSubVendorId_Object = MibTableColumn
cucsGraphicsCardSubVendorId = _CucsGraphicsCardSubVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 20),
    _CucsGraphicsCardSubVendorId_Type()
)
cucsGraphicsCardSubVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardSubVendorId.setStatus("current")
_CucsGraphicsCardThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsGraphicsCardThermal_Object = MibTableColumn
cucsGraphicsCardThermal = _CucsGraphicsCardThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 21),
    _CucsGraphicsCardThermal_Type()
)
cucsGraphicsCardThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardThermal.setStatus("current")
_CucsGraphicsCardVendor_Type = SnmpAdminString
_CucsGraphicsCardVendor_Object = MibTableColumn
cucsGraphicsCardVendor = _CucsGraphicsCardVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 22),
    _CucsGraphicsCardVendor_Type()
)
cucsGraphicsCardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardVendor.setStatus("current")
_CucsGraphicsCardVendorId_Type = Gauge32
_CucsGraphicsCardVendorId_Object = MibTableColumn
cucsGraphicsCardVendorId = _CucsGraphicsCardVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 23),
    _CucsGraphicsCardVendorId_Type()
)
cucsGraphicsCardVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardVendorId.setStatus("current")
_CucsGraphicsCardVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsGraphicsCardVoltage_Object = MibTableColumn
cucsGraphicsCardVoltage = _CucsGraphicsCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 24),
    _CucsGraphicsCardVoltage_Type()
)
cucsGraphicsCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardVoltage.setStatus("current")
_CucsGraphicsCardLocationDn_Type = SnmpAdminString
_CucsGraphicsCardLocationDn_Object = MibTableColumn
cucsGraphicsCardLocationDn = _CucsGraphicsCardLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 25),
    _CucsGraphicsCardLocationDn_Type()
)
cucsGraphicsCardLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardLocationDn.setStatus("current")
_CucsGraphicsCardStepping_Type = SnmpAdminString
_CucsGraphicsCardStepping_Object = MibTableColumn
cucsGraphicsCardStepping = _CucsGraphicsCardStepping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 26),
    _CucsGraphicsCardStepping_Type()
)
cucsGraphicsCardStepping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardStepping.setStatus("current")
_CucsGraphicsCardExpanderSlot_Type = SnmpAdminString
_CucsGraphicsCardExpanderSlot_Object = MibTableColumn
cucsGraphicsCardExpanderSlot = _CucsGraphicsCardExpanderSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 27),
    _CucsGraphicsCardExpanderSlot_Type()
)
cucsGraphicsCardExpanderSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardExpanderSlot.setStatus("current")
_CucsGraphicsCardFirmwareVersion_Type = SnmpAdminString
_CucsGraphicsCardFirmwareVersion_Object = MibTableColumn
cucsGraphicsCardFirmwareVersion = _CucsGraphicsCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 28),
    _CucsGraphicsCardFirmwareVersion_Type()
)
cucsGraphicsCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardFirmwareVersion.setStatus("current")
_CucsGraphicsCardPciAddrList_Type = SnmpAdminString
_CucsGraphicsCardPciAddrList_Object = MibTableColumn
cucsGraphicsCardPciAddrList = _CucsGraphicsCardPciAddrList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 1, 1, 29),
    _CucsGraphicsCardPciAddrList_Type()
)
cucsGraphicsCardPciAddrList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsCardPciAddrList.setStatus("current")
_CucsGraphicsControllerTable_Object = MibTable
cucsGraphicsControllerTable = _CucsGraphicsControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2)
)
if mibBuilder.loadTexts:
    cucsGraphicsControllerTable.setStatus("current")
_CucsGraphicsControllerEntry_Object = MibTableRow
cucsGraphicsControllerEntry = _CucsGraphicsControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1)
)
cucsGraphicsControllerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-GRAPHICS-MIB", "cucsGraphicsControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsGraphicsControllerEntry.setStatus("current")
_CucsGraphicsControllerInstanceId_Type = CucsManagedObjectId
_CucsGraphicsControllerInstanceId_Object = MibTableColumn
cucsGraphicsControllerInstanceId = _CucsGraphicsControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 1),
    _CucsGraphicsControllerInstanceId_Type()
)
cucsGraphicsControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsGraphicsControllerInstanceId.setStatus("current")
_CucsGraphicsControllerDn_Type = CucsManagedObjectDn
_CucsGraphicsControllerDn_Object = MibTableColumn
cucsGraphicsControllerDn = _CucsGraphicsControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 2),
    _CucsGraphicsControllerDn_Type()
)
cucsGraphicsControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerDn.setStatus("current")
_CucsGraphicsControllerRn_Type = SnmpAdminString
_CucsGraphicsControllerRn_Object = MibTableColumn
cucsGraphicsControllerRn = _CucsGraphicsControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 3),
    _CucsGraphicsControllerRn_Type()
)
cucsGraphicsControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerRn.setStatus("current")
_CucsGraphicsControllerId_Type = Gauge32
_CucsGraphicsControllerId_Object = MibTableColumn
cucsGraphicsControllerId = _CucsGraphicsControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 4),
    _CucsGraphicsControllerId_Type()
)
cucsGraphicsControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerId.setStatus("current")
_CucsGraphicsControllerModel_Type = SnmpAdminString
_CucsGraphicsControllerModel_Object = MibTableColumn
cucsGraphicsControllerModel = _CucsGraphicsControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 5),
    _CucsGraphicsControllerModel_Type()
)
cucsGraphicsControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerModel.setStatus("current")
_CucsGraphicsControllerOperQualifierReason_Type = SnmpAdminString
_CucsGraphicsControllerOperQualifierReason_Object = MibTableColumn
cucsGraphicsControllerOperQualifierReason = _CucsGraphicsControllerOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 6),
    _CucsGraphicsControllerOperQualifierReason_Type()
)
cucsGraphicsControllerOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerOperQualifierReason.setStatus("current")
_CucsGraphicsControllerOperState_Type = CucsEquipmentOperability
_CucsGraphicsControllerOperState_Object = MibTableColumn
cucsGraphicsControllerOperState = _CucsGraphicsControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 7),
    _CucsGraphicsControllerOperState_Type()
)
cucsGraphicsControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerOperState.setStatus("current")
_CucsGraphicsControllerOperability_Type = CucsEquipmentOperability
_CucsGraphicsControllerOperability_Object = MibTableColumn
cucsGraphicsControllerOperability = _CucsGraphicsControllerOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 8),
    _CucsGraphicsControllerOperability_Type()
)
cucsGraphicsControllerOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerOperability.setStatus("current")
_CucsGraphicsControllerPciAddr_Type = SnmpAdminString
_CucsGraphicsControllerPciAddr_Object = MibTableColumn
cucsGraphicsControllerPciAddr = _CucsGraphicsControllerPciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 9),
    _CucsGraphicsControllerPciAddr_Type()
)
cucsGraphicsControllerPciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerPciAddr.setStatus("current")
_CucsGraphicsControllerPciSlot_Type = SnmpAdminString
_CucsGraphicsControllerPciSlot_Object = MibTableColumn
cucsGraphicsControllerPciSlot = _CucsGraphicsControllerPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 10),
    _CucsGraphicsControllerPciSlot_Type()
)
cucsGraphicsControllerPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerPciSlot.setStatus("current")
_CucsGraphicsControllerPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsGraphicsControllerPerf_Object = MibTableColumn
cucsGraphicsControllerPerf = _CucsGraphicsControllerPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 11),
    _CucsGraphicsControllerPerf_Type()
)
cucsGraphicsControllerPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerPerf.setStatus("current")
_CucsGraphicsControllerPower_Type = CucsEquipmentPowerState
_CucsGraphicsControllerPower_Object = MibTableColumn
cucsGraphicsControllerPower = _CucsGraphicsControllerPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 12),
    _CucsGraphicsControllerPower_Type()
)
cucsGraphicsControllerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerPower.setStatus("current")
_CucsGraphicsControllerPresence_Type = CucsEquipmentPresence
_CucsGraphicsControllerPresence_Object = MibTableColumn
cucsGraphicsControllerPresence = _CucsGraphicsControllerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 13),
    _CucsGraphicsControllerPresence_Type()
)
cucsGraphicsControllerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerPresence.setStatus("current")
_CucsGraphicsControllerRevision_Type = SnmpAdminString
_CucsGraphicsControllerRevision_Object = MibTableColumn
cucsGraphicsControllerRevision = _CucsGraphicsControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 14),
    _CucsGraphicsControllerRevision_Type()
)
cucsGraphicsControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerRevision.setStatus("current")
_CucsGraphicsControllerSerial_Type = SnmpAdminString
_CucsGraphicsControllerSerial_Object = MibTableColumn
cucsGraphicsControllerSerial = _CucsGraphicsControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 15),
    _CucsGraphicsControllerSerial_Type()
)
cucsGraphicsControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerSerial.setStatus("current")
_CucsGraphicsControllerThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsGraphicsControllerThermal_Object = MibTableColumn
cucsGraphicsControllerThermal = _CucsGraphicsControllerThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 16),
    _CucsGraphicsControllerThermal_Type()
)
cucsGraphicsControllerThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerThermal.setStatus("current")
_CucsGraphicsControllerVendor_Type = SnmpAdminString
_CucsGraphicsControllerVendor_Object = MibTableColumn
cucsGraphicsControllerVendor = _CucsGraphicsControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 17),
    _CucsGraphicsControllerVendor_Type()
)
cucsGraphicsControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerVendor.setStatus("current")
_CucsGraphicsControllerVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsGraphicsControllerVoltage_Object = MibTableColumn
cucsGraphicsControllerVoltage = _CucsGraphicsControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 18),
    _CucsGraphicsControllerVoltage_Type()
)
cucsGraphicsControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerVoltage.setStatus("current")
_CucsGraphicsControllerLocationDn_Type = SnmpAdminString
_CucsGraphicsControllerLocationDn_Object = MibTableColumn
cucsGraphicsControllerLocationDn = _CucsGraphicsControllerLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 73, 2, 1, 19),
    _CucsGraphicsControllerLocationDn_Type()
)
cucsGraphicsControllerLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsGraphicsControllerLocationDn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-GRAPHICS-MIB",
    **{"cucsGraphicsObjects": cucsGraphicsObjects,
       "cucsGraphicsCardTable": cucsGraphicsCardTable,
       "cucsGraphicsCardEntry": cucsGraphicsCardEntry,
       "cucsGraphicsCardInstanceId": cucsGraphicsCardInstanceId,
       "cucsGraphicsCardDn": cucsGraphicsCardDn,
       "cucsGraphicsCardRn": cucsGraphicsCardRn,
       "cucsGraphicsCardDeviceId": cucsGraphicsCardDeviceId,
       "cucsGraphicsCardId": cucsGraphicsCardId,
       "cucsGraphicsCardIsSupported": cucsGraphicsCardIsSupported,
       "cucsGraphicsCardLc": cucsGraphicsCardLc,
       "cucsGraphicsCardModel": cucsGraphicsCardModel,
       "cucsGraphicsCardOperQualifierReason": cucsGraphicsCardOperQualifierReason,
       "cucsGraphicsCardOperState": cucsGraphicsCardOperState,
       "cucsGraphicsCardOperability": cucsGraphicsCardOperability,
       "cucsGraphicsCardPciAddr": cucsGraphicsCardPciAddr,
       "cucsGraphicsCardPciSlot": cucsGraphicsCardPciSlot,
       "cucsGraphicsCardPerf": cucsGraphicsCardPerf,
       "cucsGraphicsCardPower": cucsGraphicsCardPower,
       "cucsGraphicsCardPresence": cucsGraphicsCardPresence,
       "cucsGraphicsCardRevision": cucsGraphicsCardRevision,
       "cucsGraphicsCardSerial": cucsGraphicsCardSerial,
       "cucsGraphicsCardSubDeviceId": cucsGraphicsCardSubDeviceId,
       "cucsGraphicsCardSubVendorId": cucsGraphicsCardSubVendorId,
       "cucsGraphicsCardThermal": cucsGraphicsCardThermal,
       "cucsGraphicsCardVendor": cucsGraphicsCardVendor,
       "cucsGraphicsCardVendorId": cucsGraphicsCardVendorId,
       "cucsGraphicsCardVoltage": cucsGraphicsCardVoltage,
       "cucsGraphicsCardLocationDn": cucsGraphicsCardLocationDn,
       "cucsGraphicsCardStepping": cucsGraphicsCardStepping,
       "cucsGraphicsCardExpanderSlot": cucsGraphicsCardExpanderSlot,
       "cucsGraphicsCardFirmwareVersion": cucsGraphicsCardFirmwareVersion,
       "cucsGraphicsCardPciAddrList": cucsGraphicsCardPciAddrList,
       "cucsGraphicsControllerTable": cucsGraphicsControllerTable,
       "cucsGraphicsControllerEntry": cucsGraphicsControllerEntry,
       "cucsGraphicsControllerInstanceId": cucsGraphicsControllerInstanceId,
       "cucsGraphicsControllerDn": cucsGraphicsControllerDn,
       "cucsGraphicsControllerRn": cucsGraphicsControllerRn,
       "cucsGraphicsControllerId": cucsGraphicsControllerId,
       "cucsGraphicsControllerModel": cucsGraphicsControllerModel,
       "cucsGraphicsControllerOperQualifierReason": cucsGraphicsControllerOperQualifierReason,
       "cucsGraphicsControllerOperState": cucsGraphicsControllerOperState,
       "cucsGraphicsControllerOperability": cucsGraphicsControllerOperability,
       "cucsGraphicsControllerPciAddr": cucsGraphicsControllerPciAddr,
       "cucsGraphicsControllerPciSlot": cucsGraphicsControllerPciSlot,
       "cucsGraphicsControllerPerf": cucsGraphicsControllerPerf,
       "cucsGraphicsControllerPower": cucsGraphicsControllerPower,
       "cucsGraphicsControllerPresence": cucsGraphicsControllerPresence,
       "cucsGraphicsControllerRevision": cucsGraphicsControllerRevision,
       "cucsGraphicsControllerSerial": cucsGraphicsControllerSerial,
       "cucsGraphicsControllerThermal": cucsGraphicsControllerThermal,
       "cucsGraphicsControllerVendor": cucsGraphicsControllerVendor,
       "cucsGraphicsControllerVoltage": cucsGraphicsControllerVoltage,
       "cucsGraphicsControllerLocationDn": cucsGraphicsControllerLocationDn}
)

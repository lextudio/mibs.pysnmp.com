# SNMP MIB module (GX2HFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GX2HFC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:30 2024
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

(gi,
 motproxies) = mibBuilder.importSymbols(
    "NLS-BBNIDENT-MIB",
    "gi",
    "motproxies")

(trapChangedObjectId,
 trapChangedValueInteger,
 trapIdentifier,
 trapNETrapLastTrapTimeStamp,
 trapNetworkElemAdminState,
 trapNetworkElemAlarmStatus,
 trapNetworkElemAvailStatus,
 trapNetworkElemModelNumber,
 trapNetworkElemOperState,
 trapNetworkElemSerialNum,
 trapPerceivedSeverity,
 trapText) = mibBuilder.importSymbols(
    "NLSBBN-TRAPS-MIB",
    "trapChangedObjectId",
    "trapChangedValueInteger",
    "trapIdentifier",
    "trapNETrapLastTrapTimeStamp",
    "trapNetworkElemAdminState",
    "trapNetworkElemAlarmStatus",
    "trapNetworkElemAvailStatus",
    "trapNetworkElemModelNumber",
    "trapNetworkElemOperState",
    "trapNetworkElemSerialNum",
    "trapPerceivedSeverity",
    "trapText")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hfc_ObjectIdentity = ObjectIdentity
hfc = _Hfc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1)
)
_HfcCommon_ObjectIdentity = ObjectIdentity
hfcCommon = _HfcCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1)
)
_HfcCommonTable_Object = MibTable
hfcCommonTable = _HfcCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hfcCommonTable.setStatus("mandatory")
_HfcCommonTableEntry_Object = MibTableRow
hfcCommonTableEntry = _HfcCommonTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1)
)
hfcCommonTableEntry.setIndexNames(
    (0, "GX2HFC-MIB", "hfcCommonTableIndex"),
)
if mibBuilder.loadTexts:
    hfcCommonTableEntry.setStatus("mandatory")


class _HfcCommonTableIndex_Type(Integer32):
    """Custom type hfcCommonTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HfcCommonTableIndex_Type.__name__ = "Integer32"
_HfcCommonTableIndex_Object = MibTableColumn
hfcCommonTableIndex = _HfcCommonTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 1),
    _HfcCommonTableIndex_Type()
)
hfcCommonTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcCommonTableIndex.setStatus("mandatory")


class _HfcUnitName_Type(DisplayString):
    """Custom type hfcUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcUnitName_Type.__name__ = "DisplayString"
_HfcUnitName_Object = MibTableColumn
hfcUnitName = _HfcUnitName_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 2),
    _HfcUnitName_Type()
)
hfcUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hfcUnitName.setStatus("mandatory")
_HfcUnitTypeDescriptorPointer_Type = ObjectIdentifier
_HfcUnitTypeDescriptorPointer_Object = MibTableColumn
hfcUnitTypeDescriptorPointer = _HfcUnitTypeDescriptorPointer_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 3),
    _HfcUnitTypeDescriptorPointer_Type()
)
hfcUnitTypeDescriptorPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcUnitTypeDescriptorPointer.setStatus("mandatory")


class _HfcUnitHwVersion_Type(DisplayString):
    """Custom type hfcUnitHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcUnitHwVersion_Type.__name__ = "DisplayString"
_HfcUnitHwVersion_Object = MibTableColumn
hfcUnitHwVersion = _HfcUnitHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 4),
    _HfcUnitHwVersion_Type()
)
hfcUnitHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcUnitHwVersion.setStatus("mandatory")


class _HfcUnitFwVersion_Type(DisplayString):
    """Custom type hfcUnitFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcUnitFwVersion_Type.__name__ = "DisplayString"
_HfcUnitFwVersion_Object = MibTableColumn
hfcUnitFwVersion = _HfcUnitFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 5),
    _HfcUnitFwVersion_Type()
)
hfcUnitFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcUnitFwVersion.setStatus("mandatory")


class _HfcUnitModelNumber_Type(DisplayString):
    """Custom type hfcUnitModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcUnitModelNumber_Type.__name__ = "DisplayString"
_HfcUnitModelNumber_Object = MibTableColumn
hfcUnitModelNumber = _HfcUnitModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 6),
    _HfcUnitModelNumber_Type()
)
hfcUnitModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcUnitModelNumber.setStatus("mandatory")


class _HfcUnitLocation_Type(DisplayString):
    """Custom type hfcUnitLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcUnitLocation_Type.__name__ = "DisplayString"
_HfcUnitLocation_Object = MibTableColumn
hfcUnitLocation = _HfcUnitLocation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 7),
    _HfcUnitLocation_Type()
)
hfcUnitLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hfcUnitLocation.setStatus("mandatory")


class _HfcUnitSerialNumber_Type(DisplayString):
    """Custom type hfcUnitSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcUnitSerialNumber_Type.__name__ = "DisplayString"
_HfcUnitSerialNumber_Object = MibTableColumn
hfcUnitSerialNumber = _HfcUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 8),
    _HfcUnitSerialNumber_Type()
)
hfcUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcUnitSerialNumber.setStatus("mandatory")


class _HfcUnitAdministrativeState_Type(Integer32):
    """Custom type hfcUnitAdministrativeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("factoryAccess", 3),
          ("operatorAccess", 2),
          ("readOnly", 1))
    )


_HfcUnitAdministrativeState_Type.__name__ = "Integer32"
_HfcUnitAdministrativeState_Object = MibTableColumn
hfcUnitAdministrativeState = _HfcUnitAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 9),
    _HfcUnitAdministrativeState_Type()
)
hfcUnitAdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcUnitAdministrativeState.setStatus("mandatory")


class _HfcUnitOperationalState_Type(Integer32):
    """Custom type hfcUnitOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HfcUnitOperationalState_Type.__name__ = "Integer32"
_HfcUnitOperationalState_Object = MibTableColumn
hfcUnitOperationalState = _HfcUnitOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 10),
    _HfcUnitOperationalState_Type()
)
hfcUnitOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcUnitOperationalState.setStatus("mandatory")


class _HfcUnitAlarmStatus_Type(Integer32):
    """Custom type hfcUnitAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_HfcUnitAlarmStatus_Type.__name__ = "Integer32"
_HfcUnitAlarmStatus_Object = MibTableColumn
hfcUnitAlarmStatus = _HfcUnitAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 11),
    _HfcUnitAlarmStatus_Type()
)
hfcUnitAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcUnitAlarmStatus.setStatus("mandatory")


class _HfcUnitAvailabilityStatus_Type(Integer32):
    """Custom type hfcUnitAvailabilityStatus based on Integer32"""
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
        *(("available", 10),
          ("degraded", 7),
          ("dependency", 6),
          ("failed", 2),
          ("inTest", 1),
          ("logFull", 9),
          ("notInstalled", 8),
          ("offDuty", 5),
          ("offLine", 4),
          ("powerOff", 3))
    )


_HfcUnitAvailabilityStatus_Type.__name__ = "Integer32"
_HfcUnitAvailabilityStatus_Object = MibTableColumn
hfcUnitAvailabilityStatus = _HfcUnitAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 12),
    _HfcUnitAvailabilityStatus_Type()
)
hfcUnitAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcUnitAvailabilityStatus.setStatus("mandatory")
_HfcLogicalRfNetworkDescriptor_Type = ObjectIdentifier
_HfcLogicalRfNetworkDescriptor_Object = MibTableColumn
hfcLogicalRfNetworkDescriptor = _HfcLogicalRfNetworkDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 13),
    _HfcLogicalRfNetworkDescriptor_Type()
)
hfcLogicalRfNetworkDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcLogicalRfNetworkDescriptor.setStatus("mandatory")


class _HfcUnitDetected_Type(DisplayString):
    """Custom type hfcUnitDetected based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HfcUnitDetected_Type.__name__ = "DisplayString"
_HfcUnitDetected_Object = MibTableColumn
hfcUnitDetected = _HfcUnitDetected_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 14),
    _HfcUnitDetected_Type()
)
hfcUnitDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcUnitDetected.setStatus("mandatory")
_HfcNELastTrapTimeStamp_Type = TimeTicks
_HfcNELastTrapTimeStamp_Object = MibTableColumn
hfcNELastTrapTimeStamp = _HfcNELastTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 15),
    _HfcNELastTrapTimeStamp_Type()
)
hfcNELastTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcNELastTrapTimeStamp.setStatus("mandatory")


class _HfcPhysicalAddress_Type(DisplayString):
    """Custom type hfcPhysicalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcPhysicalAddress_Type.__name__ = "DisplayString"
_HfcPhysicalAddress_Object = MibTableColumn
hfcPhysicalAddress = _HfcPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 16),
    _HfcPhysicalAddress_Type()
)
hfcPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcPhysicalAddress.setStatus("mandatory")


class _HfcDateCode_Type(DisplayString):
    """Custom type hfcDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcDateCode_Type.__name__ = "DisplayString"
_HfcDateCode_Object = MibTableColumn
hfcDateCode = _HfcDateCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 17),
    _HfcDateCode_Type()
)
hfcDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcDateCode.setStatus("mandatory")


class _HfcNeighbor1IPAddress_Type(DisplayString):
    """Custom type hfcNeighbor1IPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcNeighbor1IPAddress_Type.__name__ = "DisplayString"
_HfcNeighbor1IPAddress_Object = MibTableColumn
hfcNeighbor1IPAddress = _HfcNeighbor1IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 18),
    _HfcNeighbor1IPAddress_Type()
)
hfcNeighbor1IPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcNeighbor1IPAddress.setStatus("mandatory")


class _HfcNeighbor2IPAddress_Type(DisplayString):
    """Custom type hfcNeighbor2IPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcNeighbor2IPAddress_Type.__name__ = "DisplayString"
_HfcNeighbor2IPAddress_Object = MibTableColumn
hfcNeighbor2IPAddress = _HfcNeighbor2IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 19),
    _HfcNeighbor2IPAddress_Type()
)
hfcNeighbor2IPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcNeighbor2IPAddress.setStatus("mandatory")


class _HfcfinshedGoodsPartNumber_Type(DisplayString):
    """Custom type hfcfinshedGoodsPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcfinshedGoodsPartNumber_Type.__name__ = "DisplayString"
_HfcfinshedGoodsPartNumber_Object = MibTableColumn
hfcfinshedGoodsPartNumber = _HfcfinshedGoodsPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 20),
    _HfcfinshedGoodsPartNumber_Type()
)
hfcfinshedGoodsPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcfinshedGoodsPartNumber.setStatus("mandatory")


class _HfcManufactureLocation_Type(DisplayString):
    """Custom type hfcManufactureLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcManufactureLocation_Type.__name__ = "DisplayString"
_HfcManufactureLocation_Object = MibTableColumn
hfcManufactureLocation = _HfcManufactureLocation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 21),
    _HfcManufactureLocation_Type()
)
hfcManufactureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcManufactureLocation.setStatus("mandatory")
_HfcDeviceSlotLocation_Type = Integer32
_HfcDeviceSlotLocation_Object = MibTableColumn
hfcDeviceSlotLocation = _HfcDeviceSlotLocation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 22),
    _HfcDeviceSlotLocation_Type()
)
hfcDeviceSlotLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcDeviceSlotLocation.setStatus("mandatory")


class _HfcBelongsTo_Type(DisplayString):
    """Custom type hfcBelongsTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcBelongsTo_Type.__name__ = "DisplayString"
_HfcBelongsTo_Object = MibTableColumn
hfcBelongsTo = _HfcBelongsTo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 23),
    _HfcBelongsTo_Type()
)
hfcBelongsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcBelongsTo.setStatus("mandatory")
_HfcModuleType_Type = Integer32
_HfcModuleType_Object = MibTableColumn
hfcModuleType = _HfcModuleType_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 24),
    _HfcModuleType_Type()
)
hfcModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcModuleType.setStatus("mandatory")
_HfcDevicePositionData_Type = Integer32
_HfcDevicePositionData_Object = MibTableColumn
hfcDevicePositionData = _HfcDevicePositionData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 25),
    _HfcDevicePositionData_Type()
)
hfcDevicePositionData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcDevicePositionData.setStatus("mandatory")


class _HfcExtendableSlotData_Type(DisplayString):
    """Custom type hfcExtendableSlotData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcExtendableSlotData_Type.__name__ = "DisplayString"
_HfcExtendableSlotData_Object = MibTableColumn
hfcExtendableSlotData = _HfcExtendableSlotData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 26),
    _HfcExtendableSlotData_Type()
)
hfcExtendableSlotData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcExtendableSlotData.setStatus("mandatory")


class _HfcActualModelNumber_Type(DisplayString):
    """Custom type hfcActualModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HfcActualModelNumber_Type.__name__ = "DisplayString"
_HfcActualModelNumber_Object = MibTableColumn
hfcActualModelNumber = _HfcActualModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 27),
    _HfcActualModelNumber_Type()
)
hfcActualModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hfcActualModelNumber.setStatus("mandatory")
_HfcDevices_ObjectIdentity = ObjectIdentity
hfcDevices = _HfcDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2)
)
_Gx2_ObjectIdentity = ObjectIdentity
gx2 = _Gx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 1)
)
_HfcUnknownType_ObjectIdentity = ObjectIdentity
hfcUnknownType = _HfcUnknownType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 2)
)
_Gx2Cm_ObjectIdentity = ObjectIdentity
gx2Cm = _Gx2Cm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3)
)
_Gx2Lm_ObjectIdentity = ObjectIdentity
gx2Lm = _Gx2Lm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 4)
)
_Gx2Lmc_ObjectIdentity = ObjectIdentity
gx2Lmc = _Gx2Lmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 5)
)
_Gx2Rx200_ObjectIdentity = ObjectIdentity
gx2Rx200 = _Gx2Rx200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6)
)
_Gx2Psdc_ObjectIdentity = ObjectIdentity
gx2Psdc = _Gx2Psdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7)
)
_Gx2Rsw200_ObjectIdentity = ObjectIdentity
gx2Rsw200 = _Gx2Rsw200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8)
)
_Gx2Rx1000_ObjectIdentity = ObjectIdentity
gx2Rx1000 = _Gx2Rx1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9)
)
_Gx2Lm870C_ObjectIdentity = ObjectIdentity
gx2Lm870C = _Gx2Lm870C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10)
)
_Gx2EDFA_ObjectIdentity = ObjectIdentity
gx2EDFA = _Gx2EDFA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11)
)
_Gx2Em870_ObjectIdentity = ObjectIdentity
gx2Em870 = _Gx2Em870_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12)
)
_Gx2Drr3x_ObjectIdentity = ObjectIdentity
gx2Drr3x = _Gx2Drr3x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13)
)
_Gx2Drr4x_ObjectIdentity = ObjectIdentity
gx2Drr4x = _Gx2Drr4x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14)
)
_Gx2Osw10b_ObjectIdentity = ObjectIdentity
gx2Osw10b = _Gx2Osw10b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15)
)
_Gx2Dm870_ObjectIdentity = ObjectIdentity
gx2Dm870 = _Gx2Dm870_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16)
)
_Gx2OA100BD_ObjectIdentity = ObjectIdentity
gx2OA100BD = _Gx2OA100BD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17)
)
_Gx2Rsw1000b_ObjectIdentity = ObjectIdentity
gx2Rsw1000b = _Gx2Rsw1000b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18)
)
_Gx2Dm200_ObjectIdentity = ObjectIdentity
gx2Dm200 = _Gx2Dm200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19)
)
_Gx2CEB_ObjectIdentity = ObjectIdentity
gx2CEB = _Gx2CEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20)
)
_Gx2Drr2x_ObjectIdentity = ObjectIdentity
gx2Drr2x = _Gx2Drr2x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 21)
)
_Gx2Rfa1000_ObjectIdentity = ObjectIdentity
gx2Rfa1000 = _Gx2Rfa1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22)
)
_Gx2Liteps_ObjectIdentity = ObjectIdentity
gx2Liteps = _Gx2Liteps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23)
)
_Gx2Em870x2_ObjectIdentity = ObjectIdentity
gx2Em870x2 = _Gx2Em870x2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 24)
)
_Gx2Drt4x_ObjectIdentity = ObjectIdentity
gx2Drt4x = _Gx2Drt4x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 25)
)
_Gx2Drt2x_ObjectIdentity = ObjectIdentity
gx2Drt2x = _Gx2Drt2x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 26)
)
_Gx2LmE_ObjectIdentity = ObjectIdentity
gx2LmE = _Gx2LmE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27)
)
_Gx2Dm1000_ObjectIdentity = ObjectIdentity
gx2Dm1000 = _Gx2Dm1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28)
)
_Gx2Rx200BX4_ObjectIdentity = ObjectIdentity
gx2Rx200BX4 = _Gx2Rx200BX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29)
)
_Gx2Em1000_ObjectIdentity = ObjectIdentity
gx2Em1000 = _Gx2Em1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30)
)
_Gx2Lm1000s_ObjectIdentity = ObjectIdentity
gx2Lm1000s = _Gx2Lm1000s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31)
)
_Gx2Rx085BX4_ObjectIdentity = ObjectIdentity
gx2Rx085BX4 = _Gx2Rx085BX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32)
)
_Gx2Ea1000_ObjectIdentity = ObjectIdentity
gx2Ea1000 = _Gx2Ea1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33)
)
_Gx2Dm2000_ObjectIdentity = ObjectIdentity
gx2Dm2000 = _Gx2Dm2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34)
)
_Gx2DualDrr2x_ObjectIdentity = ObjectIdentity
gx2DualDrr2x = _Gx2DualDrr2x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35)
)
_Gx2Gs1000_ObjectIdentity = ObjectIdentity
gx2Gs1000 = _Gx2Gs1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36)
)

# Managed Objects groups


# Notification objects

trapHfcNewNEFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 1, 0, 1)
)
trapHfcNewNEFound.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapHfcNewNEFound.setStatus(
        ""
    )

trapHfcNewNELost = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 1, 0, 2)
)
trapHfcNewNELost.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapHfcNewNELost.setStatus(
        ""
    )

trapToBeSendQueueOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 1, 0, 3)
)
trapToBeSendQueueOverflow.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapToBeSendQueueOverflow.setStatus(
        ""
    )

trapHfcNameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 1, 0, 4)
)
trapHfcNameChange.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapHfcNameChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GX2HFC-MIB",
    **{"hfc": hfc,
       "hfcCommon": hfcCommon,
       "hfcCommonTable": hfcCommonTable,
       "hfcCommonTableEntry": hfcCommonTableEntry,
       "hfcCommonTableIndex": hfcCommonTableIndex,
       "hfcUnitName": hfcUnitName,
       "hfcUnitTypeDescriptorPointer": hfcUnitTypeDescriptorPointer,
       "hfcUnitHwVersion": hfcUnitHwVersion,
       "hfcUnitFwVersion": hfcUnitFwVersion,
       "hfcUnitModelNumber": hfcUnitModelNumber,
       "hfcUnitLocation": hfcUnitLocation,
       "hfcUnitSerialNumber": hfcUnitSerialNumber,
       "hfcUnitAdministrativeState": hfcUnitAdministrativeState,
       "hfcUnitOperationalState": hfcUnitOperationalState,
       "hfcUnitAlarmStatus": hfcUnitAlarmStatus,
       "hfcUnitAvailabilityStatus": hfcUnitAvailabilityStatus,
       "hfcLogicalRfNetworkDescriptor": hfcLogicalRfNetworkDescriptor,
       "hfcUnitDetected": hfcUnitDetected,
       "hfcNELastTrapTimeStamp": hfcNELastTrapTimeStamp,
       "hfcPhysicalAddress": hfcPhysicalAddress,
       "hfcDateCode": hfcDateCode,
       "hfcNeighbor1IPAddress": hfcNeighbor1IPAddress,
       "hfcNeighbor2IPAddress": hfcNeighbor2IPAddress,
       "hfcfinshedGoodsPartNumber": hfcfinshedGoodsPartNumber,
       "hfcManufactureLocation": hfcManufactureLocation,
       "hfcDeviceSlotLocation": hfcDeviceSlotLocation,
       "hfcBelongsTo": hfcBelongsTo,
       "hfcModuleType": hfcModuleType,
       "hfcDevicePositionData": hfcDevicePositionData,
       "hfcExtendableSlotData": hfcExtendableSlotData,
       "hfcActualModelNumber": hfcActualModelNumber,
       "hfcDevices": hfcDevices,
       "gx2": gx2,
       "trapHfcNewNEFound": trapHfcNewNEFound,
       "trapHfcNewNELost": trapHfcNewNELost,
       "trapToBeSendQueueOverflow": trapToBeSendQueueOverflow,
       "trapHfcNameChange": trapHfcNameChange,
       "hfcUnknownType": hfcUnknownType,
       "gx2Cm": gx2Cm,
       "gx2Lm": gx2Lm,
       "gx2Lmc": gx2Lmc,
       "gx2Rx200": gx2Rx200,
       "gx2Psdc": gx2Psdc,
       "gx2Rsw200": gx2Rsw200,
       "gx2Rx1000": gx2Rx1000,
       "gx2Lm870C": gx2Lm870C,
       "gx2EDFA": gx2EDFA,
       "gx2Em870": gx2Em870,
       "gx2Drr3x": gx2Drr3x,
       "gx2Drr4x": gx2Drr4x,
       "gx2Osw10b": gx2Osw10b,
       "gx2Dm870": gx2Dm870,
       "gx2OA100BD": gx2OA100BD,
       "gx2Rsw1000b": gx2Rsw1000b,
       "gx2Dm200": gx2Dm200,
       "gx2CEB": gx2CEB,
       "gx2Drr2x": gx2Drr2x,
       "gx2Rfa1000": gx2Rfa1000,
       "gx2Liteps": gx2Liteps,
       "gx2Em870x2": gx2Em870x2,
       "gx2Drt4x": gx2Drt4x,
       "gx2Drt2x": gx2Drt2x,
       "gx2LmE": gx2LmE,
       "gx2Dm1000": gx2Dm1000,
       "gx2Rx200BX4": gx2Rx200BX4,
       "gx2Em1000": gx2Em1000,
       "gx2Lm1000s": gx2Lm1000s,
       "gx2Rx085BX4": gx2Rx085BX4,
       "gx2Ea1000": gx2Ea1000,
       "gx2Dm2000": gx2Dm2000,
       "gx2DualDrr2x": gx2DualDrr2x,
       "gx2Gs1000": gx2Gs1000}
)

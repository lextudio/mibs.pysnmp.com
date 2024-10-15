# SNMP MIB module (HUAWEI-ENTITY-EXTENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ENTITY-EXTENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:40 2024
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

(PhysicalClass,
 PhysicalIndex,
 entPhysicalIndex,
 entPhysicalVendorType) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalClass",
    "PhysicalIndex",
    "entPhysicalIndex",
    "entPhysicalVendorType")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 Bits,
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

(AutonomousType,
 DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwEntityExtentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HwAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("down", 12),
          ("locked", 2),
          ("loopback", 13),
          ("notSupported", 1),
          ("shuttingDown", 3),
          ("unlocked", 4),
          ("up", 11))
    )



class HwOperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12,
              13,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("connect", 13),
          ("disabled", 2),
          ("down", 12),
          ("enabled", 3),
          ("linkDown", 17),
          ("linkUp", 16),
          ("notSupported", 1),
          ("offline", 4),
          ("protocolUp", 15),
          ("up", 11))
    )



class HwStandbyStatus(Integer32, TextualConvention):
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
        *(("coldStandby", 3),
          ("hotStandby", 2),
          ("notSupported", 1),
          ("providingService", 4))
    )



class HwAlarmStatus(Bits, TextualConvention):
    status = "current"


class HWLevelState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highLevel", 2),
          ("lowLevel", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwEntityExtObjects_ObjectIdentity = ObjectIdentity
hwEntityExtObjects = _HwEntityExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1)
)
_HwEntityState_ObjectIdentity = ObjectIdentity
hwEntityState = _HwEntityState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1)
)
_HwEntityStateTable_Object = MibTable
hwEntityStateTable = _HwEntityStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwEntityStateTable.setStatus("current")
_HwEntityStateEntry_Object = MibTableRow
hwEntityStateEntry = _HwEntityStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1)
)
hwEntityStateEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwEntityStateEntry.setStatus("current")
_HwEntityAdminStatus_Type = HwAdminState
_HwEntityAdminStatus_Object = MibTableColumn
hwEntityAdminStatus = _HwEntityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 1),
    _HwEntityAdminStatus_Type()
)
hwEntityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityAdminStatus.setStatus("current")
_HwEntityOperStatus_Type = HwOperState
_HwEntityOperStatus_Object = MibTableColumn
hwEntityOperStatus = _HwEntityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 2),
    _HwEntityOperStatus_Type()
)
hwEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOperStatus.setStatus("current")
_HwEntityStandbyStatus_Type = HwStandbyStatus
_HwEntityStandbyStatus_Object = MibTableColumn
hwEntityStandbyStatus = _HwEntityStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 3),
    _HwEntityStandbyStatus_Type()
)
hwEntityStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityStandbyStatus.setStatus("current")
_HwEntityAlarmLight_Type = HwAlarmStatus
_HwEntityAlarmLight_Object = MibTableColumn
hwEntityAlarmLight = _HwEntityAlarmLight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 4),
    _HwEntityAlarmLight_Type()
)
hwEntityAlarmLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityAlarmLight.setStatus("current")


class _HwEntityCpuUsage_Type(Integer32):
    """Custom type hwEntityCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwEntityCpuUsage_Type.__name__ = "Integer32"
_HwEntityCpuUsage_Object = MibTableColumn
hwEntityCpuUsage = _HwEntityCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 5),
    _HwEntityCpuUsage_Type()
)
hwEntityCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityCpuUsage.setStatus("current")


class _HwEntityCpuUsageThreshold_Type(Integer32):
    """Custom type hwEntityCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwEntityCpuUsageThreshold_Type.__name__ = "Integer32"
_HwEntityCpuUsageThreshold_Object = MibTableColumn
hwEntityCpuUsageThreshold = _HwEntityCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 6),
    _HwEntityCpuUsageThreshold_Type()
)
hwEntityCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityCpuUsageThreshold.setStatus("current")


class _HwEntityMemUsage_Type(Integer32):
    """Custom type hwEntityMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwEntityMemUsage_Type.__name__ = "Integer32"
_HwEntityMemUsage_Object = MibTableColumn
hwEntityMemUsage = _HwEntityMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 7),
    _HwEntityMemUsage_Type()
)
hwEntityMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityMemUsage.setStatus("current")


class _HwEntityMemUsageThreshold_Type(Integer32):
    """Custom type hwEntityMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwEntityMemUsageThreshold_Type.__name__ = "Integer32"
_HwEntityMemUsageThreshold_Object = MibTableColumn
hwEntityMemUsageThreshold = _HwEntityMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 8),
    _HwEntityMemUsageThreshold_Type()
)
hwEntityMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityMemUsageThreshold.setStatus("current")
_HwEntityMemSize_Type = Integer32
_HwEntityMemSize_Object = MibTableColumn
hwEntityMemSize = _HwEntityMemSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 9),
    _HwEntityMemSize_Type()
)
hwEntityMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityMemSize.setStatus("current")
if mibBuilder.loadTexts:
    hwEntityMemSize.setUnits("bytes")
_HwEntityUpTime_Type = Integer32
_HwEntityUpTime_Object = MibTableColumn
hwEntityUpTime = _HwEntityUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 10),
    _HwEntityUpTime_Type()
)
hwEntityUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hwEntityUpTime.setUnits("seconds")
_HwEntityTemperature_Type = Integer32
_HwEntityTemperature_Object = MibTableColumn
hwEntityTemperature = _HwEntityTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 11),
    _HwEntityTemperature_Type()
)
hwEntityTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityTemperature.setStatus("current")
_HwEntityTemperatureThreshold_Type = Integer32
_HwEntityTemperatureThreshold_Object = MibTableColumn
hwEntityTemperatureThreshold = _HwEntityTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 12),
    _HwEntityTemperatureThreshold_Type()
)
hwEntityTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityTemperatureThreshold.setStatus("current")
_HwEntityVoltage_Type = Integer32
_HwEntityVoltage_Object = MibTableColumn
hwEntityVoltage = _HwEntityVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 13),
    _HwEntityVoltage_Type()
)
hwEntityVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityVoltage.setStatus("current")
_HwEntityVoltageLowThreshold_Type = Integer32
_HwEntityVoltageLowThreshold_Object = MibTableColumn
hwEntityVoltageLowThreshold = _HwEntityVoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 14),
    _HwEntityVoltageLowThreshold_Type()
)
hwEntityVoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityVoltageLowThreshold.setStatus("current")
_HwEntityVoltageHighThreshold_Type = Integer32
_HwEntityVoltageHighThreshold_Object = MibTableColumn
hwEntityVoltageHighThreshold = _HwEntityVoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 15),
    _HwEntityVoltageHighThreshold_Type()
)
hwEntityVoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityVoltageHighThreshold.setStatus("current")
_HwEntityTemperatureLowThreshold_Type = Integer32
_HwEntityTemperatureLowThreshold_Object = MibTableColumn
hwEntityTemperatureLowThreshold = _HwEntityTemperatureLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 16),
    _HwEntityTemperatureLowThreshold_Type()
)
hwEntityTemperatureLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityTemperatureLowThreshold.setStatus("current")
_HwEntityOpticalPower_Type = Integer32
_HwEntityOpticalPower_Object = MibTableColumn
hwEntityOpticalPower = _HwEntityOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 17),
    _HwEntityOpticalPower_Type()
)
hwEntityOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalPower.setStatus("current")
_HwEntityCurrent_Type = Integer32
_HwEntityCurrent_Object = MibTableColumn
hwEntityCurrent = _HwEntityCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 18),
    _HwEntityCurrent_Type()
)
hwEntityCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityCurrent.setStatus("current")
if mibBuilder.loadTexts:
    hwEntityCurrent.setUnits("A")
_HwEntityMemSizeMega_Type = Integer32
_HwEntityMemSizeMega_Object = MibTableColumn
hwEntityMemSizeMega = _HwEntityMemSizeMega_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 19),
    _HwEntityMemSizeMega_Type()
)
hwEntityMemSizeMega.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityMemSizeMega.setStatus("current")
if mibBuilder.loadTexts:
    hwEntityMemSizeMega.setUnits("M bytes")


class _HwEntityPortType_Type(Integer32):
    """Custom type hwEntityPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fiber100", 3),
          ("fiber1000", 4),
          ("fiber10000", 5),
          ("notSupported", 1),
          ("optical", 7),
          ("opticalnotExist", 6))
    )


_HwEntityPortType_Type.__name__ = "Integer32"
_HwEntityPortType_Object = MibTableColumn
hwEntityPortType = _HwEntityPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 20),
    _HwEntityPortType_Type()
)
hwEntityPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityPortType.setStatus("current")


class _HwEntityDuplex_Type(Integer32):
    """Custom type hwEntityDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 3),
          ("notSupported", 1))
    )


_HwEntityDuplex_Type.__name__ = "Integer32"
_HwEntityDuplex_Object = MibTableColumn
hwEntityDuplex = _HwEntityDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 21),
    _HwEntityDuplex_Type()
)
hwEntityDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityDuplex.setStatus("current")
_HwEntityOpticalPowerRx_Type = Integer32
_HwEntityOpticalPowerRx_Object = MibTableColumn
hwEntityOpticalPowerRx = _HwEntityOpticalPowerRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 22),
    _HwEntityOpticalPowerRx_Type()
)
hwEntityOpticalPowerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalPowerRx.setStatus("current")


class _HwEntityCpuUsageLowThreshold_Type(Integer32):
    """Custom type hwEntityCpuUsageLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwEntityCpuUsageLowThreshold_Type.__name__ = "Integer32"
_HwEntityCpuUsageLowThreshold_Object = MibTableColumn
hwEntityCpuUsageLowThreshold = _HwEntityCpuUsageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 23),
    _HwEntityCpuUsageLowThreshold_Type()
)
hwEntityCpuUsageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityCpuUsageLowThreshold.setStatus("current")
_HwEntityBoardPower_Type = Integer32
_HwEntityBoardPower_Object = MibTableColumn
hwEntityBoardPower = _HwEntityBoardPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 24),
    _HwEntityBoardPower_Type()
)
hwEntityBoardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityBoardPower.setStatus("current")
_HwEntityCpuFrequency_Type = Integer32
_HwEntityCpuFrequency_Object = MibTableColumn
hwEntityCpuFrequency = _HwEntityCpuFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 25),
    _HwEntityCpuFrequency_Type()
)
hwEntityCpuFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityCpuFrequency.setStatus("current")
if mibBuilder.loadTexts:
    hwEntityCpuFrequency.setUnits("bytes")


class _HwEntitySupportFlexCard_Type(Integer32):
    """Custom type hwEntitySupportFlexCard based on Integer32"""
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
        *(("dummy", 4),
          ("flexible", 2),
          ("notSupported", 1),
          ("unflexible", 3))
    )


_HwEntitySupportFlexCard_Type.__name__ = "Integer32"
_HwEntitySupportFlexCard_Object = MibTableColumn
hwEntitySupportFlexCard = _HwEntitySupportFlexCard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 26),
    _HwEntitySupportFlexCard_Type()
)
hwEntitySupportFlexCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntitySupportFlexCard.setStatus("current")


class _HwEntityBoardClass_Type(Integer32):
    """Custom type hwEntityBoardClass based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ecu", 6),
          ("fan", 7),
          ("icu", 5),
          ("lcd", 9),
          ("lpu", 3),
          ("mpu", 2),
          ("notSupported", 1),
          ("power", 8),
          ("sfu", 4))
    )


_HwEntityBoardClass_Type.__name__ = "Integer32"
_HwEntityBoardClass_Object = MibTableColumn
hwEntityBoardClass = _HwEntityBoardClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 27),
    _HwEntityBoardClass_Type()
)
hwEntityBoardClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityBoardClass.setStatus("current")


class _HwNseOpmStatus_Type(Integer32):
    """Custom type hwNseOpmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwNseOpmStatus_Type.__name__ = "Integer32"
_HwNseOpmStatus_Object = MibTableColumn
hwNseOpmStatus = _HwNseOpmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 28),
    _HwNseOpmStatus_Type()
)
hwNseOpmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNseOpmStatus.setStatus("current")
_HwEntityCpuMaxUsage_Type = Integer32
_HwEntityCpuMaxUsage_Object = MibTableColumn
hwEntityCpuMaxUsage = _HwEntityCpuMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 29),
    _HwEntityCpuMaxUsage_Type()
)
hwEntityCpuMaxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityCpuMaxUsage.setStatus("current")
_HwEntityCPUType_Type = SnmpAdminString
_HwEntityCPUType_Object = MibTableColumn
hwEntityCPUType = _HwEntityCPUType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 30),
    _HwEntityCPUType_Type()
)
hwEntityCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityCPUType.setStatus("current")
_HwEntityMemoryType_Type = SnmpAdminString
_HwEntityMemoryType_Object = MibTableColumn
hwEntityMemoryType = _HwEntityMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 31),
    _HwEntityMemoryType_Type()
)
hwEntityMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityMemoryType.setStatus("current")
_HwEntityFlashSize_Type = Integer32
_HwEntityFlashSize_Object = MibTableColumn
hwEntityFlashSize = _HwEntityFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 32),
    _HwEntityFlashSize_Type()
)
hwEntityFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityFlashSize.setStatus("current")
_HwEntityIfUpTimes_Type = Integer32
_HwEntityIfUpTimes_Object = MibTableColumn
hwEntityIfUpTimes = _HwEntityIfUpTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 33),
    _HwEntityIfUpTimes_Type()
)
hwEntityIfUpTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityIfUpTimes.setStatus("current")
_HwEntityIfDownTimes_Type = Integer32
_HwEntityIfDownTimes_Object = MibTableColumn
hwEntityIfDownTimes = _HwEntityIfDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 34),
    _HwEntityIfDownTimes_Type()
)
hwEntityIfDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityIfDownTimes.setStatus("current")
_HwEntityCPUAvgUsage_Type = Integer32
_HwEntityCPUAvgUsage_Object = MibTableColumn
hwEntityCPUAvgUsage = _HwEntityCPUAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 35),
    _HwEntityCPUAvgUsage_Type()
)
hwEntityCPUAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityCPUAvgUsage.setStatus("current")


class _HwEntityMemoryAvgUsage_Type(Integer32):
    """Custom type hwEntityMemoryAvgUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwEntityMemoryAvgUsage_Type.__name__ = "Integer32"
_HwEntityMemoryAvgUsage_Object = MibTableColumn
hwEntityMemoryAvgUsage = _HwEntityMemoryAvgUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 1, 1, 36),
    _HwEntityMemoryAvgUsage_Type()
)
hwEntityMemoryAvgUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityMemoryAvgUsage.setStatus("current")
_HwRUModuleInfoTable_Object = MibTable
hwRUModuleInfoTable = _HwRUModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwRUModuleInfoTable.setStatus("current")
_HwRUModuleInfoEntry_Object = MibTableRow
hwRUModuleInfoEntry = _HwRUModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1)
)
hwRUModuleInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwRUModuleInfoEntry.setStatus("current")
_HwEntityBomId_Type = SnmpAdminString
_HwEntityBomId_Object = MibTableColumn
hwEntityBomId = _HwEntityBomId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1, 1),
    _HwEntityBomId_Type()
)
hwEntityBomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityBomId.setStatus("current")
_HwEntityBomEnDesc_Type = SnmpAdminString
_HwEntityBomEnDesc_Object = MibTableColumn
hwEntityBomEnDesc = _HwEntityBomEnDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1, 2),
    _HwEntityBomEnDesc_Type()
)
hwEntityBomEnDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityBomEnDesc.setStatus("current")
_HwEntityBomLocalDesc_Type = SnmpAdminString
_HwEntityBomLocalDesc_Object = MibTableColumn
hwEntityBomLocalDesc = _HwEntityBomLocalDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1, 3),
    _HwEntityBomLocalDesc_Type()
)
hwEntityBomLocalDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityBomLocalDesc.setStatus("obsolete")
_HwEntityManufacturedDate_Type = DateAndTime
_HwEntityManufacturedDate_Object = MibTableColumn
hwEntityManufacturedDate = _HwEntityManufacturedDate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1, 4),
    _HwEntityManufacturedDate_Type()
)
hwEntityManufacturedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityManufacturedDate.setStatus("current")
_HwEntityManufactureCode_Type = Integer32
_HwEntityManufactureCode_Object = MibTableColumn
hwEntityManufactureCode = _HwEntityManufactureCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1, 5),
    _HwEntityManufactureCode_Type()
)
hwEntityManufactureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityManufactureCode.setStatus("obsolete")
_HwEntityCLEICode_Type = SnmpAdminString
_HwEntityCLEICode_Object = MibTableColumn
hwEntityCLEICode = _HwEntityCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1, 6),
    _HwEntityCLEICode_Type()
)
hwEntityCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityCLEICode.setStatus("current")
_HwEntityUpdateLog_Type = SnmpAdminString
_HwEntityUpdateLog_Object = MibTableColumn
hwEntityUpdateLog = _HwEntityUpdateLog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1, 7),
    _HwEntityUpdateLog_Type()
)
hwEntityUpdateLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityUpdateLog.setStatus("obsolete")
_HwEntityArchivesInfoVersion_Type = SnmpAdminString
_HwEntityArchivesInfoVersion_Object = MibTableColumn
hwEntityArchivesInfoVersion = _HwEntityArchivesInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1, 8),
    _HwEntityArchivesInfoVersion_Type()
)
hwEntityArchivesInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityArchivesInfoVersion.setStatus("current")
_HwEntityOpenBomId_Type = SnmpAdminString
_HwEntityOpenBomId_Object = MibTableColumn
hwEntityOpenBomId = _HwEntityOpenBomId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1, 9),
    _HwEntityOpenBomId_Type()
)
hwEntityOpenBomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpenBomId.setStatus("current")
_HwEntityIssueNum_Type = SnmpAdminString
_HwEntityIssueNum_Object = MibTableColumn
hwEntityIssueNum = _HwEntityIssueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1, 10),
    _HwEntityIssueNum_Type()
)
hwEntityIssueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityIssueNum.setStatus("current")
_HwEntityBoardType_Type = SnmpAdminString
_HwEntityBoardType_Object = MibTableColumn
hwEntityBoardType = _HwEntityBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 2, 1, 11),
    _HwEntityBoardType_Type()
)
hwEntityBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityBoardType.setStatus("current")
_HwOpticalModuleInfoTable_Object = MibTable
hwOpticalModuleInfoTable = _HwOpticalModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwOpticalModuleInfoTable.setStatus("current")
_HwOpticalModuleInfoEntry_Object = MibTableRow
hwOpticalModuleInfoEntry = _HwOpticalModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1)
)
hwOpticalModuleInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwOpticalModuleInfoEntry.setStatus("current")


class _HwEntityOpticalMode_Type(Integer32):
    """Custom type hwEntityOpticalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("multiMode5", 3),
          ("multiMode6", 4),
          ("noValue", 5),
          ("notSupported", 1),
          ("singleMode", 2))
    )


_HwEntityOpticalMode_Type.__name__ = "Integer32"
_HwEntityOpticalMode_Object = MibTableColumn
hwEntityOpticalMode = _HwEntityOpticalMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 1),
    _HwEntityOpticalMode_Type()
)
hwEntityOpticalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalMode.setStatus("current")
_HwEntityOpticalWaveLength_Type = Integer32
_HwEntityOpticalWaveLength_Object = MibTableColumn
hwEntityOpticalWaveLength = _HwEntityOpticalWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 2),
    _HwEntityOpticalWaveLength_Type()
)
hwEntityOpticalWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalWaveLength.setStatus("current")
_HwEntityOpticalTransDistance_Type = Integer32
_HwEntityOpticalTransDistance_Object = MibTableColumn
hwEntityOpticalTransDistance = _HwEntityOpticalTransDistance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 3),
    _HwEntityOpticalTransDistance_Type()
)
hwEntityOpticalTransDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalTransDistance.setStatus("current")
_HwEntityOpticalVendorSn_Type = SnmpAdminString
_HwEntityOpticalVendorSn_Object = MibTableColumn
hwEntityOpticalVendorSn = _HwEntityOpticalVendorSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 4),
    _HwEntityOpticalVendorSn_Type()
)
hwEntityOpticalVendorSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalVendorSn.setStatus("current")
_HwEntityOpticalTemperature_Type = Integer32
_HwEntityOpticalTemperature_Object = MibTableColumn
hwEntityOpticalTemperature = _HwEntityOpticalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 5),
    _HwEntityOpticalTemperature_Type()
)
hwEntityOpticalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalTemperature.setStatus("current")
_HwEntityOpticalVoltage_Type = Integer32
_HwEntityOpticalVoltage_Object = MibTableColumn
hwEntityOpticalVoltage = _HwEntityOpticalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 6),
    _HwEntityOpticalVoltage_Type()
)
hwEntityOpticalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalVoltage.setStatus("current")
_HwEntityOpticalBiasCurrent_Type = Integer32
_HwEntityOpticalBiasCurrent_Object = MibTableColumn
hwEntityOpticalBiasCurrent = _HwEntityOpticalBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 7),
    _HwEntityOpticalBiasCurrent_Type()
)
hwEntityOpticalBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalBiasCurrent.setStatus("current")
_HwEntityOpticalRxPower_Type = Integer32
_HwEntityOpticalRxPower_Object = MibTableColumn
hwEntityOpticalRxPower = _HwEntityOpticalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 8),
    _HwEntityOpticalRxPower_Type()
)
hwEntityOpticalRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalRxPower.setStatus("current")
_HwEntityOpticalTxPower_Type = Integer32
_HwEntityOpticalTxPower_Object = MibTableColumn
hwEntityOpticalTxPower = _HwEntityOpticalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 9),
    _HwEntityOpticalTxPower_Type()
)
hwEntityOpticalTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalTxPower.setStatus("current")


class _HwEntityOpticalType_Type(Integer32):
    """Custom type hwEntityOpticalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("cfp", 9),
          ("copper", 5),
          ("esfp", 4),
          ("gbic", 2),
          ("sc", 1),
          ("sfp", 3),
          ("transponder", 8),
          ("unknown", 0),
          ("xenpak", 7),
          ("xfp", 6))
    )


_HwEntityOpticalType_Type.__name__ = "Integer32"
_HwEntityOpticalType_Object = MibTableColumn
hwEntityOpticalType = _HwEntityOpticalType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 10),
    _HwEntityOpticalType_Type()
)
hwEntityOpticalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalType.setStatus("current")
_HwEntityOpticalTransBW_Type = Integer32
_HwEntityOpticalTransBW_Object = MibTableColumn
hwEntityOpticalTransBW = _HwEntityOpticalTransBW_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 11),
    _HwEntityOpticalTransBW_Type()
)
hwEntityOpticalTransBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalTransBW.setStatus("current")


class _HwEntityOpticalFiberType_Type(Integer32):
    """Custom type hwEntityOpticalFiberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("bnc-tnc", 4),
          ("coaxial-headers", 5),
          ("copper-pigtail", 21),
          ("fiberJack", 6),
          ("hssdcII", 20),
          ("lc", 7),
          ("mt-rj", 8),
          ("mu", 9),
          ("optical-pigtail", 11),
          ("sc", 1),
          ("sg", 10),
          ("style-1-copper-connector", 2),
          ("style-2-copper-connector", 3),
          ("unknown", 0))
    )


_HwEntityOpticalFiberType_Type.__name__ = "Integer32"
_HwEntityOpticalFiberType_Object = MibTableColumn
hwEntityOpticalFiberType = _HwEntityOpticalFiberType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 12),
    _HwEntityOpticalFiberType_Type()
)
hwEntityOpticalFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalFiberType.setStatus("current")
_HwEntityOpticalRxLowThreshold_Type = Integer32
_HwEntityOpticalRxLowThreshold_Object = MibTableColumn
hwEntityOpticalRxLowThreshold = _HwEntityOpticalRxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 13),
    _HwEntityOpticalRxLowThreshold_Type()
)
hwEntityOpticalRxLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalRxLowThreshold.setStatus("current")
_HwEntityOpticalRxHighThreshold_Type = Integer32
_HwEntityOpticalRxHighThreshold_Object = MibTableColumn
hwEntityOpticalRxHighThreshold = _HwEntityOpticalRxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 14),
    _HwEntityOpticalRxHighThreshold_Type()
)
hwEntityOpticalRxHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalRxHighThreshold.setStatus("current")
_HwEntityOpticalTxLowThreshold_Type = Integer32
_HwEntityOpticalTxLowThreshold_Object = MibTableColumn
hwEntityOpticalTxLowThreshold = _HwEntityOpticalTxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 15),
    _HwEntityOpticalTxLowThreshold_Type()
)
hwEntityOpticalTxLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalTxLowThreshold.setStatus("current")
_HwEntityOpticalTxHighThreshold_Type = Integer32
_HwEntityOpticalTxHighThreshold_Object = MibTableColumn
hwEntityOpticalTxHighThreshold = _HwEntityOpticalTxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 16),
    _HwEntityOpticalTxHighThreshold_Type()
)
hwEntityOpticalTxHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalTxHighThreshold.setStatus("current")


class _HwEntityOpticalPlug_Type(Integer32):
    """Custom type hwEntityOpticalPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSupported", 0),
          ("true", 1))
    )


_HwEntityOpticalPlug_Type.__name__ = "Integer32"
_HwEntityOpticalPlug_Object = MibTableColumn
hwEntityOpticalPlug = _HwEntityOpticalPlug_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 17),
    _HwEntityOpticalPlug_Type()
)
hwEntityOpticalPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalPlug.setStatus("current")


class _HwEntityOpticalDirectionType_Type(Integer32):
    """Custom type hwEntityOpticalDirectionType based on Integer32"""
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
        *(("notSupported", 1),
          ("oneFiberBidirection", 3),
          ("twoFiberBidirection", 2),
          ("twoFiberTwoPortBidirection", 4))
    )


_HwEntityOpticalDirectionType_Type.__name__ = "Integer32"
_HwEntityOpticalDirectionType_Object = MibTableColumn
hwEntityOpticalDirectionType = _HwEntityOpticalDirectionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 18),
    _HwEntityOpticalDirectionType_Type()
)
hwEntityOpticalDirectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalDirectionType.setStatus("current")


class _HwEntityOpticalUserEeprom_Type(DisplayString):
    """Custom type hwEntityOpticalUserEeprom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_HwEntityOpticalUserEeprom_Type.__name__ = "DisplayString"
_HwEntityOpticalUserEeprom_Object = MibTableColumn
hwEntityOpticalUserEeprom = _HwEntityOpticalUserEeprom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 19),
    _HwEntityOpticalUserEeprom_Type()
)
hwEntityOpticalUserEeprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalUserEeprom.setStatus("current")
_HwEntityOpticalRxLowWarnThreshold_Type = Integer32
_HwEntityOpticalRxLowWarnThreshold_Object = MibTableColumn
hwEntityOpticalRxLowWarnThreshold = _HwEntityOpticalRxLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 20),
    _HwEntityOpticalRxLowWarnThreshold_Type()
)
hwEntityOpticalRxLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalRxLowWarnThreshold.setStatus("current")
_HwEntityOpticalRxHighWarnThreshold_Type = Integer32
_HwEntityOpticalRxHighWarnThreshold_Object = MibTableColumn
hwEntityOpticalRxHighWarnThreshold = _HwEntityOpticalRxHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 21),
    _HwEntityOpticalRxHighWarnThreshold_Type()
)
hwEntityOpticalRxHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalRxHighWarnThreshold.setStatus("current")
_HwEntityOpticalTxLowWarnThreshold_Type = Integer32
_HwEntityOpticalTxLowWarnThreshold_Object = MibTableColumn
hwEntityOpticalTxLowWarnThreshold = _HwEntityOpticalTxLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 22),
    _HwEntityOpticalTxLowWarnThreshold_Type()
)
hwEntityOpticalTxLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalTxLowWarnThreshold.setStatus("current")
_HwEntityOpticalTxHighWarnThreshold_Type = Integer32
_HwEntityOpticalTxHighWarnThreshold_Object = MibTableColumn
hwEntityOpticalTxHighWarnThreshold = _HwEntityOpticalTxHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 3, 1, 23),
    _HwEntityOpticalTxHighWarnThreshold_Type()
)
hwEntityOpticalTxHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityOpticalTxHighWarnThreshold.setStatus("current")
_HwMonitorInputTable_Object = MibTable
hwMonitorInputTable = _HwMonitorInputTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwMonitorInputTable.setStatus("current")
_HwMonitorInputEntry_Object = MibTableRow
hwMonitorInputEntry = _HwMonitorInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 4, 1)
)
hwMonitorInputEntry.setIndexNames(
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorInputIndex"),
)
if mibBuilder.loadTexts:
    hwMonitorInputEntry.setStatus("current")


class _HwMonitorInputIndex_Type(Integer32):
    """Custom type hwMonitorInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HwMonitorInputIndex_Type.__name__ = "Integer32"
_HwMonitorInputIndex_Object = MibTableColumn
hwMonitorInputIndex = _HwMonitorInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 4, 1, 1),
    _HwMonitorInputIndex_Type()
)
hwMonitorInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMonitorInputIndex.setStatus("current")
_HwMonitorInputName_Type = DisplayString
_HwMonitorInputName_Object = MibTableColumn
hwMonitorInputName = _HwMonitorInputName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 4, 1, 2),
    _HwMonitorInputName_Type()
)
hwMonitorInputName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorInputName.setStatus("current")
_HwMonitorInputState_Type = HWLevelState
_HwMonitorInputState_Object = MibTableColumn
hwMonitorInputState = _HwMonitorInputState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 4, 1, 3),
    _HwMonitorInputState_Type()
)
hwMonitorInputState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorInputState.setStatus("current")
_HwMonitorInputStateEnable_Type = EnabledStatus
_HwMonitorInputStateEnable_Object = MibTableColumn
hwMonitorInputStateEnable = _HwMonitorInputStateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 4, 1, 4),
    _HwMonitorInputStateEnable_Type()
)
hwMonitorInputStateEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorInputStateEnable.setStatus("current")
_HwMonitorInputRowStatus_Type = RowStatus
_HwMonitorInputRowStatus_Object = MibTableColumn
hwMonitorInputRowStatus = _HwMonitorInputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 4, 1, 5),
    _HwMonitorInputRowStatus_Type()
)
hwMonitorInputRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorInputRowStatus.setStatus("current")
_HwMonitorOutputTable_Object = MibTable
hwMonitorOutputTable = _HwMonitorOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwMonitorOutputTable.setStatus("current")
_HwMonitorOutputEntry_Object = MibTableRow
hwMonitorOutputEntry = _HwMonitorOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 5, 1)
)
hwMonitorOutputEntry.setIndexNames(
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorOutputIndex"),
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorOutputRuleIndex"),
)
if mibBuilder.loadTexts:
    hwMonitorOutputEntry.setStatus("current")


class _HwMonitorOutputIndex_Type(Integer32):
    """Custom type hwMonitorOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HwMonitorOutputIndex_Type.__name__ = "Integer32"
_HwMonitorOutputIndex_Object = MibTableColumn
hwMonitorOutputIndex = _HwMonitorOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 5, 1, 1),
    _HwMonitorOutputIndex_Type()
)
hwMonitorOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMonitorOutputIndex.setStatus("current")


class _HwMonitorOutputRuleIndex_Type(Integer32):
    """Custom type hwMonitorOutputRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwMonitorOutputRuleIndex_Type.__name__ = "Integer32"
_HwMonitorOutputRuleIndex_Object = MibTableColumn
hwMonitorOutputRuleIndex = _HwMonitorOutputRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 5, 1, 2),
    _HwMonitorOutputRuleIndex_Type()
)
hwMonitorOutputRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMonitorOutputRuleIndex.setStatus("current")
_HwMonitorOutputMask_Type = DisplayString
_HwMonitorOutputMask_Object = MibTableColumn
hwMonitorOutputMask = _HwMonitorOutputMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 5, 1, 3),
    _HwMonitorOutputMask_Type()
)
hwMonitorOutputMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorOutputMask.setStatus("current")
_HwMonitorOutputKey_Type = DisplayString
_HwMonitorOutputKey_Object = MibTableColumn
hwMonitorOutputKey = _HwMonitorOutputKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 5, 1, 4),
    _HwMonitorOutputKey_Type()
)
hwMonitorOutputKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorOutputKey.setStatus("current")
_HwMonitorOutputRowStatus_Type = RowStatus
_HwMonitorOutputRowStatus_Object = MibTableColumn
hwMonitorOutputRowStatus = _HwMonitorOutputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 5, 1, 5),
    _HwMonitorOutputRowStatus_Type()
)
hwMonitorOutputRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMonitorOutputRowStatus.setStatus("current")
_HwEntPowerUsedInfoTable_Object = MibTable
hwEntPowerUsedInfoTable = _HwEntPowerUsedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwEntPowerUsedInfoTable.setStatus("current")
_HwEntPowerUsedInfoEntry_Object = MibTableRow
hwEntPowerUsedInfoEntry = _HwEntPowerUsedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 6, 1)
)
hwEntPowerUsedInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwEntPowerUsedInfoEntry.setStatus("current")
_HwEntPowerUsedInfoBoardName_Type = OctetString
_HwEntPowerUsedInfoBoardName_Object = MibTableColumn
hwEntPowerUsedInfoBoardName = _HwEntPowerUsedInfoBoardName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 6, 1, 1),
    _HwEntPowerUsedInfoBoardName_Type()
)
hwEntPowerUsedInfoBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntPowerUsedInfoBoardName.setStatus("current")
_HwEntPowerUsedInfoBoardType_Type = OctetString
_HwEntPowerUsedInfoBoardType_Object = MibTableColumn
hwEntPowerUsedInfoBoardType = _HwEntPowerUsedInfoBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 6, 1, 2),
    _HwEntPowerUsedInfoBoardType_Type()
)
hwEntPowerUsedInfoBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntPowerUsedInfoBoardType.setStatus("current")
_HwEntPowerUsedInfoBoardSlot_Type = Integer32
_HwEntPowerUsedInfoBoardSlot_Object = MibTableColumn
hwEntPowerUsedInfoBoardSlot = _HwEntPowerUsedInfoBoardSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 6, 1, 3),
    _HwEntPowerUsedInfoBoardSlot_Type()
)
hwEntPowerUsedInfoBoardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntPowerUsedInfoBoardSlot.setStatus("current")
_HwEntPowerUsedInfoPower_Type = Integer32
_HwEntPowerUsedInfoPower_Object = MibTableColumn
hwEntPowerUsedInfoPower = _HwEntPowerUsedInfoPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 6, 1, 4),
    _HwEntPowerUsedInfoPower_Type()
)
hwEntPowerUsedInfoPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntPowerUsedInfoPower.setStatus("current")
_HwVirtualCableTestTable_Object = MibTable
hwVirtualCableTestTable = _HwVirtualCableTestTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwVirtualCableTestTable.setStatus("current")
_HwVirtualCableTestEntry_Object = MibTableRow
hwVirtualCableTestEntry = _HwVirtualCableTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1)
)
hwVirtualCableTestEntry.setIndexNames(
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestIfIndex"),
)
if mibBuilder.loadTexts:
    hwVirtualCableTestEntry.setStatus("current")
_HwVirtualCableTestIfIndex_Type = InterfaceIndex
_HwVirtualCableTestIfIndex_Object = MibTableColumn
hwVirtualCableTestIfIndex = _HwVirtualCableTestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 1),
    _HwVirtualCableTestIfIndex_Type()
)
hwVirtualCableTestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVirtualCableTestIfIndex.setStatus("current")


class _HwVirtualCableTestPairStatus_Type(Integer32):
    """Custom type hwVirtualCableTestPairStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abnormalCrossTalk", 5),
          ("abnormalOpen", 2),
          ("abnormalOpenShort", 4),
          ("abnormalShort", 3),
          ("normal", 1),
          ("notSupport", 7),
          ("unknown", 6))
    )


_HwVirtualCableTestPairStatus_Type.__name__ = "Integer32"
_HwVirtualCableTestPairStatus_Object = MibTableColumn
hwVirtualCableTestPairStatus = _HwVirtualCableTestPairStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 2),
    _HwVirtualCableTestPairStatus_Type()
)
hwVirtualCableTestPairStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVirtualCableTestPairStatus.setStatus("current")
_HwVirtualCableTestPairLength_Type = Integer32
_HwVirtualCableTestPairLength_Object = MibTableColumn
hwVirtualCableTestPairLength = _HwVirtualCableTestPairLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 3),
    _HwVirtualCableTestPairLength_Type()
)
hwVirtualCableTestPairLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVirtualCableTestPairLength.setStatus("current")


class _HwVirtualCableTestOperation_Type(Integer32):
    """Custom type hwVirtualCableTestOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readyStartTest", 3),
          ("resetTestValue", 2),
          ("startTest", 1))
    )


_HwVirtualCableTestOperation_Type.__name__ = "Integer32"
_HwVirtualCableTestOperation_Object = MibTableColumn
hwVirtualCableTestOperation = _HwVirtualCableTestOperation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 4),
    _HwVirtualCableTestOperation_Type()
)
hwVirtualCableTestOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVirtualCableTestOperation.setStatus("current")
_HwVirtualCableTestLastTime_Type = Integer32
_HwVirtualCableTestLastTime_Object = MibTableColumn
hwVirtualCableTestLastTime = _HwVirtualCableTestLastTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 5),
    _HwVirtualCableTestLastTime_Type()
)
hwVirtualCableTestLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVirtualCableTestLastTime.setStatus("current")


class _HwVirtualCableTestPairAStatus_Type(Integer32):
    """Custom type hwVirtualCableTestPairAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abnormalCrossTalk", 5),
          ("abnormalOpen", 2),
          ("abnormalOpenShort", 4),
          ("abnormalShort", 3),
          ("normal", 1),
          ("notSupport", 7),
          ("unknown", 6))
    )


_HwVirtualCableTestPairAStatus_Type.__name__ = "Integer32"
_HwVirtualCableTestPairAStatus_Object = MibTableColumn
hwVirtualCableTestPairAStatus = _HwVirtualCableTestPairAStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 6),
    _HwVirtualCableTestPairAStatus_Type()
)
hwVirtualCableTestPairAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVirtualCableTestPairAStatus.setStatus("current")


class _HwVirtualCableTestPairBStatus_Type(Integer32):
    """Custom type hwVirtualCableTestPairBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abnormalCrossTalk", 5),
          ("abnormalOpen", 2),
          ("abnormalOpenShort", 4),
          ("abnormalShort", 3),
          ("normal", 1),
          ("notSupport", 7),
          ("unknown", 6))
    )


_HwVirtualCableTestPairBStatus_Type.__name__ = "Integer32"
_HwVirtualCableTestPairBStatus_Object = MibTableColumn
hwVirtualCableTestPairBStatus = _HwVirtualCableTestPairBStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 7),
    _HwVirtualCableTestPairBStatus_Type()
)
hwVirtualCableTestPairBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVirtualCableTestPairBStatus.setStatus("current")


class _HwVirtualCableTestPairCStatus_Type(Integer32):
    """Custom type hwVirtualCableTestPairCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abnormalCrossTalk", 5),
          ("abnormalOpen", 2),
          ("abnormalOpenShort", 4),
          ("abnormalShort", 3),
          ("normal", 1),
          ("notSupport", 7),
          ("unknown", 6))
    )


_HwVirtualCableTestPairCStatus_Type.__name__ = "Integer32"
_HwVirtualCableTestPairCStatus_Object = MibTableColumn
hwVirtualCableTestPairCStatus = _HwVirtualCableTestPairCStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 8),
    _HwVirtualCableTestPairCStatus_Type()
)
hwVirtualCableTestPairCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVirtualCableTestPairCStatus.setStatus("current")


class _HwVirtualCableTestPairDStatus_Type(Integer32):
    """Custom type hwVirtualCableTestPairDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abnormalCrossTalk", 5),
          ("abnormalOpen", 2),
          ("abnormalOpenShort", 4),
          ("abnormalShort", 3),
          ("normal", 1),
          ("notSupport", 7),
          ("unknown", 6))
    )


_HwVirtualCableTestPairDStatus_Type.__name__ = "Integer32"
_HwVirtualCableTestPairDStatus_Object = MibTableColumn
hwVirtualCableTestPairDStatus = _HwVirtualCableTestPairDStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 9),
    _HwVirtualCableTestPairDStatus_Type()
)
hwVirtualCableTestPairDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVirtualCableTestPairDStatus.setStatus("current")
_HwVirtualCableTestPairALength_Type = Integer32
_HwVirtualCableTestPairALength_Object = MibTableColumn
hwVirtualCableTestPairALength = _HwVirtualCableTestPairALength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 10),
    _HwVirtualCableTestPairALength_Type()
)
hwVirtualCableTestPairALength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVirtualCableTestPairALength.setStatus("current")
_HwVirtualCableTestPairBLength_Type = Integer32
_HwVirtualCableTestPairBLength_Object = MibTableColumn
hwVirtualCableTestPairBLength = _HwVirtualCableTestPairBLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 11),
    _HwVirtualCableTestPairBLength_Type()
)
hwVirtualCableTestPairBLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVirtualCableTestPairBLength.setStatus("current")
_HwVirtualCableTestPairCLength_Type = Integer32
_HwVirtualCableTestPairCLength_Object = MibTableColumn
hwVirtualCableTestPairCLength = _HwVirtualCableTestPairCLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 12),
    _HwVirtualCableTestPairCLength_Type()
)
hwVirtualCableTestPairCLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVirtualCableTestPairCLength.setStatus("current")
_HwVirtualCableTestPairDLength_Type = Integer32
_HwVirtualCableTestPairDLength_Object = MibTableColumn
hwVirtualCableTestPairDLength = _HwVirtualCableTestPairDLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 7, 1, 13),
    _HwVirtualCableTestPairDLength_Type()
)
hwVirtualCableTestPairDLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVirtualCableTestPairDLength.setStatus("current")
_HwTemperatureThresholdTable_Object = MibTable
hwTemperatureThresholdTable = _HwTemperatureThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hwTemperatureThresholdTable.setStatus("current")
_HwTemperatureThresholdEntry_Object = MibTableRow
hwTemperatureThresholdEntry = _HwTemperatureThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 8, 1)
)
hwTemperatureThresholdEntry.setIndexNames(
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempSlotId"),
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempI2CId"),
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempAddr"),
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempChannel"),
)
if mibBuilder.loadTexts:
    hwTemperatureThresholdEntry.setStatus("current")
_HwEntityTempSlotId_Type = Integer32
_HwEntityTempSlotId_Object = MibTableColumn
hwEntityTempSlotId = _HwEntityTempSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 8, 1, 1),
    _HwEntityTempSlotId_Type()
)
hwEntityTempSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityTempSlotId.setStatus("current")
_HwEntityTempI2CId_Type = Integer32
_HwEntityTempI2CId_Object = MibTableColumn
hwEntityTempI2CId = _HwEntityTempI2CId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 8, 1, 2),
    _HwEntityTempI2CId_Type()
)
hwEntityTempI2CId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityTempI2CId.setStatus("current")
_HwEntityTempAddr_Type = Integer32
_HwEntityTempAddr_Object = MibTableColumn
hwEntityTempAddr = _HwEntityTempAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 8, 1, 3),
    _HwEntityTempAddr_Type()
)
hwEntityTempAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityTempAddr.setStatus("current")
_HwEntityTempChannel_Type = Integer32
_HwEntityTempChannel_Object = MibTableColumn
hwEntityTempChannel = _HwEntityTempChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 8, 1, 4),
    _HwEntityTempChannel_Type()
)
hwEntityTempChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityTempChannel.setStatus("current")


class _HwEntityTempStatus_Type(Integer32):
    """Custom type hwEntityTempStatus based on Integer32"""
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
        *(("fatal", 4),
          ("major", 3),
          ("minor", 2),
          ("normal", 1))
    )


_HwEntityTempStatus_Type.__name__ = "Integer32"
_HwEntityTempStatus_Object = MibTableColumn
hwEntityTempStatus = _HwEntityTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 8, 1, 5),
    _HwEntityTempStatus_Type()
)
hwEntityTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityTempStatus.setStatus("current")
_HwEntityTempValue_Type = Integer32
_HwEntityTempValue_Object = MibTableColumn
hwEntityTempValue = _HwEntityTempValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 8, 1, 6),
    _HwEntityTempValue_Type()
)
hwEntityTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityTempValue.setStatus("current")
_HwEntityTempMinorAlmThreshold_Type = Integer32
_HwEntityTempMinorAlmThreshold_Object = MibTableColumn
hwEntityTempMinorAlmThreshold = _HwEntityTempMinorAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 8, 1, 7),
    _HwEntityTempMinorAlmThreshold_Type()
)
hwEntityTempMinorAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityTempMinorAlmThreshold.setStatus("current")
_HwEntityTempMajorAlmThreshold_Type = Integer32
_HwEntityTempMajorAlmThreshold_Object = MibTableColumn
hwEntityTempMajorAlmThreshold = _HwEntityTempMajorAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 8, 1, 8),
    _HwEntityTempMajorAlmThreshold_Type()
)
hwEntityTempMajorAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityTempMajorAlmThreshold.setStatus("current")
_HwEntityTempFatalAlmThreshold_Type = Integer32
_HwEntityTempFatalAlmThreshold_Object = MibTableColumn
hwEntityTempFatalAlmThreshold = _HwEntityTempFatalAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 8, 1, 9),
    _HwEntityTempFatalAlmThreshold_Type()
)
hwEntityTempFatalAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityTempFatalAlmThreshold.setStatus("current")
_HwVoltageInfoTable_Object = MibTable
hwVoltageInfoTable = _HwVoltageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hwVoltageInfoTable.setStatus("current")
_HwVoltageInfoEntry_Object = MibTableRow
hwVoltageInfoEntry = _HwVoltageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1)
)
hwVoltageInfoEntry.setIndexNames(
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolSlot"),
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolI2CId"),
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolAddr"),
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolChannel"),
)
if mibBuilder.loadTexts:
    hwVoltageInfoEntry.setStatus("current")
_HwEntityVolSlot_Type = Integer32
_HwEntityVolSlot_Object = MibTableColumn
hwEntityVolSlot = _HwEntityVolSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 1),
    _HwEntityVolSlot_Type()
)
hwEntityVolSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityVolSlot.setStatus("current")
_HwEntityVolI2CId_Type = Integer32
_HwEntityVolI2CId_Object = MibTableColumn
hwEntityVolI2CId = _HwEntityVolI2CId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 2),
    _HwEntityVolI2CId_Type()
)
hwEntityVolI2CId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityVolI2CId.setStatus("current")
_HwEntityVolAddr_Type = Integer32
_HwEntityVolAddr_Object = MibTableColumn
hwEntityVolAddr = _HwEntityVolAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 3),
    _HwEntityVolAddr_Type()
)
hwEntityVolAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityVolAddr.setStatus("current")
_HwEntityVolChannel_Type = Integer32
_HwEntityVolChannel_Object = MibTableColumn
hwEntityVolChannel = _HwEntityVolChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 4),
    _HwEntityVolChannel_Type()
)
hwEntityVolChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityVolChannel.setStatus("current")


class _HwEntityVolStatus_Type(Integer32):
    """Custom type hwEntityVolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fatal", 3),
          ("major", 2),
          ("normal", 1))
    )


_HwEntityVolStatus_Type.__name__ = "Integer32"
_HwEntityVolStatus_Object = MibTableColumn
hwEntityVolStatus = _HwEntityVolStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 5),
    _HwEntityVolStatus_Type()
)
hwEntityVolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityVolStatus.setStatus("current")
_HwEntityVolRequired_Type = Integer32
_HwEntityVolRequired_Object = MibTableColumn
hwEntityVolRequired = _HwEntityVolRequired_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 6),
    _HwEntityVolRequired_Type()
)
hwEntityVolRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityVolRequired.setStatus("current")
_HwEntityVolCurValue_Type = Integer32
_HwEntityVolCurValue_Object = MibTableColumn
hwEntityVolCurValue = _HwEntityVolCurValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 7),
    _HwEntityVolCurValue_Type()
)
hwEntityVolCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityVolCurValue.setStatus("current")
_HwEntityVolRatio_Type = Integer32
_HwEntityVolRatio_Object = MibTableColumn
hwEntityVolRatio = _HwEntityVolRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 8),
    _HwEntityVolRatio_Type()
)
hwEntityVolRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityVolRatio.setStatus("current")
_HwEntityVolLowAlmMajor_Type = Integer32
_HwEntityVolLowAlmMajor_Object = MibTableColumn
hwEntityVolLowAlmMajor = _HwEntityVolLowAlmMajor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 9),
    _HwEntityVolLowAlmMajor_Type()
)
hwEntityVolLowAlmMajor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityVolLowAlmMajor.setStatus("current")
_HwEntityVolLowAlmFatal_Type = Integer32
_HwEntityVolLowAlmFatal_Object = MibTableColumn
hwEntityVolLowAlmFatal = _HwEntityVolLowAlmFatal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 10),
    _HwEntityVolLowAlmFatal_Type()
)
hwEntityVolLowAlmFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityVolLowAlmFatal.setStatus("current")
_HwEntityVolHighAlmMajor_Type = Integer32
_HwEntityVolHighAlmMajor_Object = MibTableColumn
hwEntityVolHighAlmMajor = _HwEntityVolHighAlmMajor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 11),
    _HwEntityVolHighAlmMajor_Type()
)
hwEntityVolHighAlmMajor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityVolHighAlmMajor.setStatus("current")
_HwEntityVolHighAlmFatal_Type = Integer32
_HwEntityVolHighAlmFatal_Object = MibTableColumn
hwEntityVolHighAlmFatal = _HwEntityVolHighAlmFatal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 9, 1, 12),
    _HwEntityVolHighAlmFatal_Type()
)
hwEntityVolHighAlmFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityVolHighAlmFatal.setStatus("current")
_HwFanStatusTable_Object = MibTable
hwFanStatusTable = _HwFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hwFanStatusTable.setStatus("current")
_HwFanStatusEntry_Object = MibTableRow
hwFanStatusEntry = _HwFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 10, 1)
)
hwFanStatusEntry.setIndexNames(
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwEntityFanSlot"),
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwEntityFanSn"),
)
if mibBuilder.loadTexts:
    hwFanStatusEntry.setStatus("current")
_HwEntityFanSlot_Type = Integer32
_HwEntityFanSlot_Object = MibTableColumn
hwEntityFanSlot = _HwEntityFanSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 10, 1, 1),
    _HwEntityFanSlot_Type()
)
hwEntityFanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityFanSlot.setStatus("current")
_HwEntityFanSn_Type = Integer32
_HwEntityFanSn_Object = MibTableColumn
hwEntityFanSn = _HwEntityFanSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 10, 1, 2),
    _HwEntityFanSn_Type()
)
hwEntityFanSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityFanSn.setStatus("current")


class _HwEntityFanReg_Type(Integer32):
    """Custom type hwEntityFanReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HwEntityFanReg_Type.__name__ = "Integer32"
_HwEntityFanReg_Object = MibTableColumn
hwEntityFanReg = _HwEntityFanReg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 10, 1, 3),
    _HwEntityFanReg_Type()
)
hwEntityFanReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityFanReg.setStatus("current")


class _HwEntityFanSpdAdjMode_Type(Integer32):
    """Custom type hwEntityFanSpdAdjMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2),
          ("unknown", 3))
    )


_HwEntityFanSpdAdjMode_Type.__name__ = "Integer32"
_HwEntityFanSpdAdjMode_Object = MibTableColumn
hwEntityFanSpdAdjMode = _HwEntityFanSpdAdjMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 10, 1, 4),
    _HwEntityFanSpdAdjMode_Type()
)
hwEntityFanSpdAdjMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityFanSpdAdjMode.setStatus("current")
_HwEntityFanSpeed_Type = Integer32
_HwEntityFanSpeed_Object = MibTableColumn
hwEntityFanSpeed = _HwEntityFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 10, 1, 5),
    _HwEntityFanSpeed_Type()
)
hwEntityFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityFanSpeed.setStatus("current")


class _HwEntityFanPresent_Type(Integer32):
    """Custom type hwEntityFanPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("present", 1))
    )


_HwEntityFanPresent_Type.__name__ = "Integer32"
_HwEntityFanPresent_Object = MibTableColumn
hwEntityFanPresent = _HwEntityFanPresent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 10, 1, 6),
    _HwEntityFanPresent_Type()
)
hwEntityFanPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityFanPresent.setStatus("current")


class _HwEntityFanState_Type(Integer32):
    """Custom type hwEntityFanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_HwEntityFanState_Type.__name__ = "Integer32"
_HwEntityFanState_Object = MibTableColumn
hwEntityFanState = _HwEntityFanState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 10, 1, 7),
    _HwEntityFanState_Type()
)
hwEntityFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityFanState.setStatus("current")
_HwEntityGlobalPara_ObjectIdentity = ObjectIdentity
hwEntityGlobalPara = _HwEntityGlobalPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 11)
)


class _HwEntityServiceType_Type(Integer32):
    """Custom type hwEntityServiceType based on Integer32"""
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
        *(("firewall", 2),
          ("ipsec", 4),
          ("load-balance", 3),
          ("netstream", 5),
          ("sslvpn", 1),
          ("wlan", 6))
    )


_HwEntityServiceType_Type.__name__ = "Integer32"
_HwEntityServiceType_Object = MibScalar
hwEntityServiceType = _HwEntityServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 11, 1),
    _HwEntityServiceType_Type()
)
hwEntityServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityServiceType.setStatus("current")
_HwPortBip8StatisticsTable_Object = MibTable
hwPortBip8StatisticsTable = _HwPortBip8StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hwPortBip8StatisticsTable.setStatus("current")
_HwPortBip8StatisticsEntry_Object = MibTableRow
hwPortBip8StatisticsEntry = _HwPortBip8StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 12, 1)
)
hwPortBip8StatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwPortBip8StatisticsEntry.setStatus("current")
_HwPhysicalPortBip8StatisticsEB_Type = Counter64
_HwPhysicalPortBip8StatisticsEB_Object = MibTableColumn
hwPhysicalPortBip8StatisticsEB = _HwPhysicalPortBip8StatisticsEB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 12, 1, 1),
    _HwPhysicalPortBip8StatisticsEB_Type()
)
hwPhysicalPortBip8StatisticsEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPhysicalPortBip8StatisticsEB.setStatus("current")
_HwPhysicalPortBip8StatisticsES_Type = Counter64
_HwPhysicalPortBip8StatisticsES_Object = MibTableColumn
hwPhysicalPortBip8StatisticsES = _HwPhysicalPortBip8StatisticsES_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 12, 1, 2),
    _HwPhysicalPortBip8StatisticsES_Type()
)
hwPhysicalPortBip8StatisticsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPhysicalPortBip8StatisticsES.setStatus("current")
_HwPhysicalPortBip8StatisticsSES_Type = Counter64
_HwPhysicalPortBip8StatisticsSES_Object = MibTableColumn
hwPhysicalPortBip8StatisticsSES = _HwPhysicalPortBip8StatisticsSES_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 12, 1, 3),
    _HwPhysicalPortBip8StatisticsSES_Type()
)
hwPhysicalPortBip8StatisticsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPhysicalPortBip8StatisticsSES.setStatus("current")
_HwPhysicalPortBip8StatisticsUAS_Type = Counter64
_HwPhysicalPortBip8StatisticsUAS_Object = MibTableColumn
hwPhysicalPortBip8StatisticsUAS = _HwPhysicalPortBip8StatisticsUAS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 12, 1, 4),
    _HwPhysicalPortBip8StatisticsUAS_Type()
)
hwPhysicalPortBip8StatisticsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPhysicalPortBip8StatisticsUAS.setStatus("current")
_HwPhysicalPortBip8StatisticsBBE_Type = Counter64
_HwPhysicalPortBip8StatisticsBBE_Object = MibTableColumn
hwPhysicalPortBip8StatisticsBBE = _HwPhysicalPortBip8StatisticsBBE_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 12, 1, 5),
    _HwPhysicalPortBip8StatisticsBBE_Type()
)
hwPhysicalPortBip8StatisticsBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPhysicalPortBip8StatisticsBBE.setStatus("current")
_HwPhysicalPortSpeed_Type = Unsigned32
_HwPhysicalPortSpeed_Object = MibTableColumn
hwPhysicalPortSpeed = _HwPhysicalPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 1, 1, 12, 1, 6),
    _HwPhysicalPortSpeed_Type()
)
hwPhysicalPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPhysicalPortSpeed.setStatus("current")
_HwEntityExtTraps_ObjectIdentity = ObjectIdentity
hwEntityExtTraps = _HwEntityExtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2)
)
_HwEntityExtTrapsPrefix_ObjectIdentity = ObjectIdentity
hwEntityExtTrapsPrefix = _HwEntityExtTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0)
)
_HwDevicePowerInfoObjects_ObjectIdentity = ObjectIdentity
hwDevicePowerInfoObjects = _HwDevicePowerInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 3)
)
_HwDevicePowerInfoTotalPower_Type = Integer32
_HwDevicePowerInfoTotalPower_Object = MibScalar
hwDevicePowerInfoTotalPower = _HwDevicePowerInfoTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 3, 1),
    _HwDevicePowerInfoTotalPower_Type()
)
hwDevicePowerInfoTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDevicePowerInfoTotalPower.setStatus("current")
_HwDevicePowerInfoUsedPower_Type = Integer32
_HwDevicePowerInfoUsedPower_Object = MibScalar
hwDevicePowerInfoUsedPower = _HwDevicePowerInfoUsedPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 3, 2),
    _HwDevicePowerInfoUsedPower_Type()
)
hwDevicePowerInfoUsedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDevicePowerInfoUsedPower.setStatus("current")
_HwEntityExtConformance_ObjectIdentity = ObjectIdentity
hwEntityExtConformance = _HwEntityExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4)
)
_HwEntityExtCompliances_ObjectIdentity = ObjectIdentity
hwEntityExtCompliances = _HwEntityExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 1)
)
_HwEntityExtGroups_ObjectIdentity = ObjectIdentity
hwEntityExtGroups = _HwEntityExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2)
)
_HwPnpObjects_ObjectIdentity = ObjectIdentity
hwPnpObjects = _HwPnpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5)
)
_HwPnpInfo_ObjectIdentity = ObjectIdentity
hwPnpInfo = _HwPnpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 1)
)
_HwHardwareCapaSequenceNo_Type = SnmpAdminString
_HwHardwareCapaSequenceNo_Object = MibScalar
hwHardwareCapaSequenceNo = _HwHardwareCapaSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 1, 1),
    _HwHardwareCapaSequenceNo_Type()
)
hwHardwareCapaSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHardwareCapaSequenceNo.setStatus("current")
_HwPnpTraps_ObjectIdentity = ObjectIdentity
hwPnpTraps = _HwPnpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 2)
)
_HwPnpOperateTable_Object = MibTable
hwPnpOperateTable = _HwPnpOperateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 3)
)
if mibBuilder.loadTexts:
    hwPnpOperateTable.setStatus("current")
_HwPnpOperateEntry_Object = MibTableRow
hwPnpOperateEntry = _HwPnpOperateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 3, 1)
)
hwPnpOperateEntry.setIndexNames(
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwFileGeneIndex"),
)
if mibBuilder.loadTexts:
    hwPnpOperateEntry.setStatus("current")


class _HwFileGeneIndex_Type(Integer32):
    """Custom type hwFileGeneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwFileGeneIndex_Type.__name__ = "Integer32"
_HwFileGeneIndex_Object = MibTableColumn
hwFileGeneIndex = _HwFileGeneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 3, 1, 1),
    _HwFileGeneIndex_Type()
)
hwFileGeneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFileGeneIndex.setStatus("current")


class _HwFileGeneOperState_Type(Integer32):
    """Custom type hwFileGeneOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("opDestoryError", 7),
          ("opGetFileError", 3),
          ("opInProgress", 1),
          ("opInvalidDestName", 4),
          ("opNoFlashSpace", 5),
          ("opSuccess", 2),
          ("opWriteFileError", 6))
    )


_HwFileGeneOperState_Type.__name__ = "Integer32"
_HwFileGeneOperState_Object = MibTableColumn
hwFileGeneOperState = _HwFileGeneOperState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 3, 1, 2),
    _HwFileGeneOperState_Type()
)
hwFileGeneOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFileGeneOperState.setStatus("current")


class _HwFileGeneResourceType_Type(Integer32):
    """Custom type hwFileGeneResourceType based on Integer32"""
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
        *(("pnpPreDisposeCapability", 4),
          ("pnpcard", 1),
          ("pnphardcapability", 3),
          ("pnpsubcard", 2))
    )


_HwFileGeneResourceType_Type.__name__ = "Integer32"
_HwFileGeneResourceType_Object = MibTableColumn
hwFileGeneResourceType = _HwFileGeneResourceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 3, 1, 3),
    _HwFileGeneResourceType_Type()
)
hwFileGeneResourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFileGeneResourceType.setStatus("current")


class _HwFileGeneResourceID_Type(SnmpAdminString):
    """Custom type hwFileGeneResourceID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwFileGeneResourceID_Type.__name__ = "SnmpAdminString"
_HwFileGeneResourceID_Object = MibTableColumn
hwFileGeneResourceID = _HwFileGeneResourceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 3, 1, 4),
    _HwFileGeneResourceID_Type()
)
hwFileGeneResourceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFileGeneResourceID.setStatus("current")


class _HwFileGeneDestinationFile_Type(SnmpAdminString):
    """Custom type hwFileGeneDestinationFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwFileGeneDestinationFile_Type.__name__ = "SnmpAdminString"
_HwFileGeneDestinationFile_Object = MibTableColumn
hwFileGeneDestinationFile = _HwFileGeneDestinationFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 3, 1, 5),
    _HwFileGeneDestinationFile_Type()
)
hwFileGeneDestinationFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFileGeneDestinationFile.setStatus("current")
_HwFileGeneRowStatus_Type = RowStatus
_HwFileGeneRowStatus_Object = MibTableColumn
hwFileGeneRowStatus = _HwFileGeneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 3, 1, 6),
    _HwFileGeneRowStatus_Type()
)
hwFileGeneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFileGeneRowStatus.setStatus("current")
_HwSystemGlobalObjects_ObjectIdentity = ObjectIdentity
hwSystemGlobalObjects = _HwSystemGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 6)
)


class _HwEntitySystemNetID_Type(OctetString):
    """Custom type hwEntitySystemNetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HwEntitySystemNetID_Type.__name__ = "OctetString"
_HwEntitySystemNetID_Object = MibScalar
hwEntitySystemNetID = _HwEntitySystemNetID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 6, 1),
    _HwEntitySystemNetID_Type()
)
hwEntitySystemNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntitySystemNetID.setStatus("current")
_HwEntitySoftwareName_Type = SnmpAdminString
_HwEntitySoftwareName_Object = MibScalar
hwEntitySoftwareName = _HwEntitySoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 6, 2),
    _HwEntitySoftwareName_Type()
)
hwEntitySoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntitySoftwareName.setStatus("current")
_HwEntitySoftwareVersion_Type = SnmpAdminString
_HwEntitySoftwareVersion_Object = MibScalar
hwEntitySoftwareVersion = _HwEntitySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 6, 3),
    _HwEntitySoftwareVersion_Type()
)
hwEntitySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntitySoftwareVersion.setStatus("current")
_HwEntitySoftwareVendor_Type = SnmpAdminString
_HwEntitySoftwareVendor_Object = MibScalar
hwEntitySoftwareVendor = _HwEntitySoftwareVendor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 6, 4),
    _HwEntitySoftwareVendor_Type()
)
hwEntitySoftwareVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntitySoftwareVendor.setStatus("current")
_HwEntitySystemModel_Type = SnmpAdminString
_HwEntitySystemModel_Object = MibScalar
hwEntitySystemModel = _HwEntitySystemModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 6, 5),
    _HwEntitySystemModel_Type()
)
hwEntitySystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntitySystemModel.setStatus("current")
_HwEntitySystemTime_Type = SnmpAdminString
_HwEntitySystemTime_Object = MibScalar
hwEntitySystemTime = _HwEntitySystemTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 6, 6),
    _HwEntitySystemTime_Type()
)
hwEntitySystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntitySystemTime.setStatus("current")
_HwEntitySystemMacAddress_Type = SnmpAdminString
_HwEntitySystemMacAddress_Object = MibScalar
hwEntitySystemMacAddress = _HwEntitySystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 6, 7),
    _HwEntitySystemMacAddress_Type()
)
hwEntitySystemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntitySystemMacAddress.setStatus("current")


class _HwEntitySystemReset_Type(Integer32):
    """Custom type hwEntitySystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("restart", 2))
    )


_HwEntitySystemReset_Type.__name__ = "Integer32"
_HwEntitySystemReset_Object = MibScalar
hwEntitySystemReset = _HwEntitySystemReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 6, 8),
    _HwEntitySystemReset_Type()
)
hwEntitySystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntitySystemReset.setStatus("current")


class _HwEntitySystemHealthInterval_Type(Integer32):
    """Custom type hwEntitySystemHealthInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900),
    )


_HwEntitySystemHealthInterval_Type.__name__ = "Integer32"
_HwEntitySystemHealthInterval_Object = MibScalar
hwEntitySystemHealthInterval = _HwEntitySystemHealthInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 6, 9),
    _HwEntitySystemHealthInterval_Type()
)
hwEntitySystemHealthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntitySystemHealthInterval.setStatus("current")


class _HwEntitySystemNEId_Type(Integer32):
    """Custom type hwEntitySystemNEId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_HwEntitySystemNEId_Type.__name__ = "Integer32"
_HwEntitySystemNEId_Object = MibScalar
hwEntitySystemNEId = _HwEntitySystemNEId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 6, 10),
    _HwEntitySystemNEId_Type()
)
hwEntitySystemNEId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntitySystemNEId.setStatus("current")
_HwHeartbeatObjects_ObjectIdentity = ObjectIdentity
hwHeartbeatObjects = _HwHeartbeatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 7)
)
_HwHeartbeatConfig_ObjectIdentity = ObjectIdentity
hwHeartbeatConfig = _HwHeartbeatConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 7, 1)
)


class _HwEntityHeartbeatOnOff_Type(Integer32):
    """Custom type hwEntityHeartbeatOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HwEntityHeartbeatOnOff_Type.__name__ = "Integer32"
_HwEntityHeartbeatOnOff_Object = MibScalar
hwEntityHeartbeatOnOff = _HwEntityHeartbeatOnOff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 7, 1, 1),
    _HwEntityHeartbeatOnOff_Type()
)
hwEntityHeartbeatOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityHeartbeatOnOff.setStatus("current")


class _HwEntityHeartbeatPeriod_Type(Integer32):
    """Custom type hwEntityHeartbeatPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_HwEntityHeartbeatPeriod_Type.__name__ = "Integer32"
_HwEntityHeartbeatPeriod_Object = MibScalar
hwEntityHeartbeatPeriod = _HwEntityHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 7, 1, 2),
    _HwEntityHeartbeatPeriod_Type()
)
hwEntityHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityHeartbeatPeriod.setStatus("current")
_HwHeartbeatTrapPrefix_ObjectIdentity = ObjectIdentity
hwHeartbeatTrapPrefix = _HwHeartbeatTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 7, 2)
)
_HwPreDisposeObjects_ObjectIdentity = ObjectIdentity
hwPreDisposeObjects = _HwPreDisposeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8)
)
_HwPreDisposeInfo_ObjectIdentity = ObjectIdentity
hwPreDisposeInfo = _HwPreDisposeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 1)
)
_HwPreDisposeSequenceNo_Type = SnmpAdminString
_HwPreDisposeSequenceNo_Object = MibScalar
hwPreDisposeSequenceNo = _HwPreDisposeSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 1, 1),
    _HwPreDisposeSequenceNo_Type()
)
hwPreDisposeSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPreDisposeSequenceNo.setStatus("current")
_HwPreDisposedTraps_ObjectIdentity = ObjectIdentity
hwPreDisposedTraps = _HwPreDisposedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 2)
)
_HwPreDisposeConfigTable_Object = MibTable
hwPreDisposeConfigTable = _HwPreDisposeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 3)
)
if mibBuilder.loadTexts:
    hwPreDisposeConfigTable.setStatus("current")
_HwPreDisposeConfigEntry_Object = MibTableRow
hwPreDisposeConfigEntry = _HwPreDisposeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 3, 1)
)
hwPreDisposeConfigEntry.setIndexNames(
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeSlot"),
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeCardId"),
)
if mibBuilder.loadTexts:
    hwPreDisposeConfigEntry.setStatus("current")
_HwDisposeSlot_Type = Integer32
_HwDisposeSlot_Object = MibTableColumn
hwDisposeSlot = _HwDisposeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 3, 1, 1),
    _HwDisposeSlot_Type()
)
hwDisposeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDisposeSlot.setStatus("current")
_HwDisposeCardId_Type = Integer32
_HwDisposeCardId_Object = MibTableColumn
hwDisposeCardId = _HwDisposeCardId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 3, 1, 2),
    _HwDisposeCardId_Type()
)
hwDisposeCardId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDisposeCardId.setStatus("current")
_HwDisposeSbom_Type = OctetString
_HwDisposeSbom_Object = MibTableColumn
hwDisposeSbom = _HwDisposeSbom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 3, 1, 3),
    _HwDisposeSbom_Type()
)
hwDisposeSbom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDisposeSbom.setStatus("current")
_HwDisposeRowStatus_Type = RowStatus
_HwDisposeRowStatus_Object = MibTableColumn
hwDisposeRowStatus = _HwDisposeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 3, 1, 4),
    _HwDisposeRowStatus_Type()
)
hwDisposeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDisposeRowStatus.setStatus("current")


class _HwDisposeOperState_Type(Integer32):
    """Custom type hwDisposeOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("opAlreadyPredispose", 5),
          ("opCardConflict", 6),
          ("opCardNotSupportPredispose", 4),
          ("opDevNotSupportPredispose", 3),
          ("opDevOperationError", 7),
          ("opInProgress", 2),
          ("opSuccess", 1))
    )


_HwDisposeOperState_Type.__name__ = "Integer32"
_HwDisposeOperState_Object = MibTableColumn
hwDisposeOperState = _HwDisposeOperState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 3, 1, 5),
    _HwDisposeOperState_Type()
)
hwDisposeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisposeOperState.setStatus("current")
_HwPreDisposeEntInfoTable_Object = MibTable
hwPreDisposeEntInfoTable = _HwPreDisposeEntInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 4)
)
if mibBuilder.loadTexts:
    hwPreDisposeEntInfoTable.setStatus("current")
_HwPreDisposeEntInfoEntry_Object = MibTableRow
hwPreDisposeEntInfoEntry = _HwPreDisposeEntInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 4, 1)
)
hwPreDisposeEntInfoEntry.setIndexNames(
    (0, "HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeEntPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwPreDisposeEntInfoEntry.setStatus("current")
_HwDisposeEntPhysicalIndex_Type = PhysicalIndex
_HwDisposeEntPhysicalIndex_Object = MibTableColumn
hwDisposeEntPhysicalIndex = _HwDisposeEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 4, 1, 1),
    _HwDisposeEntPhysicalIndex_Type()
)
hwDisposeEntPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDisposeEntPhysicalIndex.setStatus("current")
_HwDisposeEntPhysicalDescr_Type = SnmpAdminString
_HwDisposeEntPhysicalDescr_Object = MibTableColumn
hwDisposeEntPhysicalDescr = _HwDisposeEntPhysicalDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 4, 1, 2),
    _HwDisposeEntPhysicalDescr_Type()
)
hwDisposeEntPhysicalDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisposeEntPhysicalDescr.setStatus("current")
_HwDisposeEntPhysicalVendorType_Type = AutonomousType
_HwDisposeEntPhysicalVendorType_Object = MibTableColumn
hwDisposeEntPhysicalVendorType = _HwDisposeEntPhysicalVendorType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 4, 1, 3),
    _HwDisposeEntPhysicalVendorType_Type()
)
hwDisposeEntPhysicalVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisposeEntPhysicalVendorType.setStatus("current")


class _HwDisposeEntPhysicalContainedIn_Type(Integer32):
    """Custom type hwDisposeEntPhysicalContainedIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwDisposeEntPhysicalContainedIn_Type.__name__ = "Integer32"
_HwDisposeEntPhysicalContainedIn_Object = MibTableColumn
hwDisposeEntPhysicalContainedIn = _HwDisposeEntPhysicalContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 4, 1, 4),
    _HwDisposeEntPhysicalContainedIn_Type()
)
hwDisposeEntPhysicalContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisposeEntPhysicalContainedIn.setStatus("current")
_HwDisposeEntPhysicalClass_Type = PhysicalClass
_HwDisposeEntPhysicalClass_Object = MibTableColumn
hwDisposeEntPhysicalClass = _HwDisposeEntPhysicalClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 4, 1, 5),
    _HwDisposeEntPhysicalClass_Type()
)
hwDisposeEntPhysicalClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisposeEntPhysicalClass.setStatus("current")


class _HwDisposeEntPhysicalParentRelPos_Type(Integer32):
    """Custom type hwDisposeEntPhysicalParentRelPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_HwDisposeEntPhysicalParentRelPos_Type.__name__ = "Integer32"
_HwDisposeEntPhysicalParentRelPos_Object = MibTableColumn
hwDisposeEntPhysicalParentRelPos = _HwDisposeEntPhysicalParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 4, 1, 6),
    _HwDisposeEntPhysicalParentRelPos_Type()
)
hwDisposeEntPhysicalParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisposeEntPhysicalParentRelPos.setStatus("current")
_HwDisposeEntPhysicalName_Type = SnmpAdminString
_HwDisposeEntPhysicalName_Object = MibTableColumn
hwDisposeEntPhysicalName = _HwDisposeEntPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 4, 1, 7),
    _HwDisposeEntPhysicalName_Type()
)
hwDisposeEntPhysicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisposeEntPhysicalName.setStatus("current")

# Managed Objects groups

hwEntityExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 1)
)
hwEntityExtGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAdminStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOperStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityStandbyStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAlarmLight"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCpuUsage"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCpuUsageThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityMemUsage"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityMemUsageThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityMemSize"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityUpTime"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTemperature"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTemperatureThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVoltage"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVoltageLowThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVoltageHighThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTemperatureLowThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalPower"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCurrent"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityMemSizeMega"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityPortType"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityDuplex"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalPowerRx"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCpuUsageLowThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityBoardPower"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCpuFrequency"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntitySupportFlexCard"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityBoardClass"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwNseOpmStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCpuMaxUsage"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityServiceType"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCPUType"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityMemoryType"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityFlashSize"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityIfUpTimes"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityIfDownTimes"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCPUAvgUsage"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityMemoryAvgUsage"))
)
if mibBuilder.loadTexts:
    hwEntityExtGroup.setStatus("current")

hwRUModuleInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 3)
)
hwRUModuleInfoGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityBomId"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityBomEnDesc"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityManufacturedDate"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCLEICode"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityArchivesInfoVersion"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpenBomId"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityIssueNum"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityBoardType"))
)
if mibBuilder.loadTexts:
    hwRUModuleInfoGroup.setStatus("current")

hwEntityExtOldObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 4)
)
hwEntityExtOldObjectsGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityBomLocalDesc"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityManufactureCode"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityUpdateLog"))
)
if mibBuilder.loadTexts:
    hwEntityExtOldObjectsGroup.setStatus("obsolete")

hwOpticalModuleInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 5)
)
hwOpticalModuleInfoGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalMode"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalWaveLength"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalTransDistance"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalVendorSn"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalTemperature"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalVoltage"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalBiasCurrent"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalRxPower"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalTxPower"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalType"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalTransBW"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalFiberType"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalRxLowThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalRxHighThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalTxLowThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalTxHighThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalPlug"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalDirectionType"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityOpticalUserEeprom"))
)
if mibBuilder.loadTexts:
    hwOpticalModuleInfoGroup.setStatus("current")

hwMonitorInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 6)
)
hwMonitorInputGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorInputName"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorInputState"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorInputStateEnable"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorInputRowStatus"))
)
if mibBuilder.loadTexts:
    hwMonitorInputGroup.setStatus("current")

hwMonitorOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 7)
)
hwMonitorOutputGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorOutputMask"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorOutputKey"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorOutputRowStatus"))
)
if mibBuilder.loadTexts:
    hwMonitorOutputGroup.setStatus("current")

hwEntPowerUsedInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 8)
)
hwEntPowerUsedInfoGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntPowerUsedInfoBoardName"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntPowerUsedInfoBoardType"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntPowerUsedInfoBoardSlot"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntPowerUsedInfoPower"))
)
if mibBuilder.loadTexts:
    hwEntPowerUsedInfoGroup.setStatus("current")

hwDevicePowerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 9)
)
hwDevicePowerInfoGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwDevicePowerInfoTotalPower"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDevicePowerInfoUsedPower"))
)
if mibBuilder.loadTexts:
    hwDevicePowerInfoGroup.setStatus("current")

hwVirtualCableTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 10)
)
hwVirtualCableTestGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestPairStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestPairLength"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestOperation"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestLastTime"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestPairAStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestPairBStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestPairCStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestPairDStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestPairALength"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestPairBLength"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestPairCLength"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwVirtualCableTestPairDLength"))
)
if mibBuilder.loadTexts:
    hwVirtualCableTestGroup.setStatus("current")

hwTemperatureThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 11)
)
hwTemperatureThresholdGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempSlotId"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempI2CId"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempAddr"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempChannel"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempValue"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempMinorAlmThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempMajorAlmThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTempFatalAlmThreshold"))
)
if mibBuilder.loadTexts:
    hwTemperatureThresholdGroup.setStatus("current")

hwVoltageInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 12)
)
hwVoltageInfoGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolSlot"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolI2CId"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolAddr"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolChannel"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolRequired"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolLowAlmMajor"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolLowAlmFatal"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolHighAlmMajor"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolHighAlmFatal"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolCurValue"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVolRatio"))
)
if mibBuilder.loadTexts:
    hwVoltageInfoGroup.setStatus("current")

hwFanStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 13)
)
hwFanStatusGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityFanSlot"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityFanSn"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityFanReg"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityFanSpdAdjMode"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityFanSpeed"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityFanPresent"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityFanState"))
)
if mibBuilder.loadTexts:
    hwFanStatusGroup.setStatus("current")

hwPnpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 14)
)
hwPnpGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwHardwareCapaSequenceNo"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwFileGeneIndex"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwFileGeneResourceType"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwFileGeneResourceID"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwFileGeneDestinationFile"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwFileGeneOperState"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwFileGeneRowStatus"))
)
if mibBuilder.loadTexts:
    hwPnpGroup.setStatus("current")

hwSystemGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 15)
)
hwSystemGlobalGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntitySystemNetID"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntitySoftwareName"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntitySoftwareVersion"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntitySoftwareVendor"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntitySystemModel"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntitySystemTime"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntitySystemMacAddress"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntitySystemReset"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntitySystemHealthInterval"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntitySystemNEId"))
)
if mibBuilder.loadTexts:
    hwSystemGlobalGroup.setStatus("current")

hwHeartbeatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 16)
)
hwHeartbeatGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityHeartbeatOnOff"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityHeartbeatPeriod"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityHeartbeatTrap"))
)
if mibBuilder.loadTexts:
    hwHeartbeatGroup.setStatus("current")

hwPortBip8StatisticsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 17)
)
hwPortBip8StatisticsObjectGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwPhysicalPortBip8StatisticsEB"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwPhysicalPortBip8StatisticsES"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwPhysicalPortBip8StatisticsSES"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwPhysicalPortBip8StatisticsUAS"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwPhysicalPortBip8StatisticsBBE"))
)
if mibBuilder.loadTexts:
    hwPortBip8StatisticsObjectGroup.setStatus("current")

hwPredisposeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 18)
)
hwPredisposeGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwPreDisposeSequenceNo"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeSlot"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeCardId"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeSbom"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeRowStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeOperState"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeEntPhysicalIndex"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeEntPhysicalDescr"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeEntPhysicalVendorType"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeEntPhysicalContainedIn"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeEntPhysicalClass"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeEntPhysicalParentRelPos"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeEntPhysicalName"))
)
if mibBuilder.loadTexts:
    hwPredisposeGroup.setStatus("current")


# Notification objects

hwEntityExtTemperatureThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 1)
)
hwEntityExtTemperatureThresholdNotification.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTemperature"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTemperatureThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAdminStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAlarmLight"))
)
if mibBuilder.loadTexts:
    hwEntityExtTemperatureThresholdNotification.setStatus(
        "current"
    )

hwEntityExtVoltageLowThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 2)
)
hwEntityExtVoltageLowThresholdNotification.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVoltage"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVoltageLowThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAdminStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAlarmLight"))
)
if mibBuilder.loadTexts:
    hwEntityExtVoltageLowThresholdNotification.setStatus(
        "current"
    )

hwEntityExtVoltageHighThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 3)
)
hwEntityExtVoltageHighThresholdNotification.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVoltage"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityVoltageHighThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAdminStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAlarmLight"))
)
if mibBuilder.loadTexts:
    hwEntityExtVoltageHighThresholdNotification.setStatus(
        "current"
    )

hwEntityExtCpuUsageThresholdNotfication = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 4)
)
hwEntityExtCpuUsageThresholdNotfication.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCpuUsage"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCpuUsageThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTemperature"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTemperatureThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAdminStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAlarmLight"))
)
if mibBuilder.loadTexts:
    hwEntityExtCpuUsageThresholdNotfication.setStatus(
        "current"
    )

hwEntityExtMemUsageThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 5)
)
hwEntityExtMemUsageThresholdNotification.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityMemUsage"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityMemUsageThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityMemSize"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAdminStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAlarmLight"))
)
if mibBuilder.loadTexts:
    hwEntityExtMemUsageThresholdNotification.setStatus(
        "current"
    )

hwEntityExtOperEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 6)
)
hwEntityExtOperEnabled.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAdminStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAlarmLight"))
)
if mibBuilder.loadTexts:
    hwEntityExtOperEnabled.setStatus(
        "current"
    )

hwEntityExtOperDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 7)
)
hwEntityExtOperDisabled.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAdminStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAlarmLight"))
)
if mibBuilder.loadTexts:
    hwEntityExtOperDisabled.setStatus(
        "current"
    )

hwEntityExtMonitorBoardAbnormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 8)
)
if mibBuilder.loadTexts:
    hwEntityExtMonitorBoardAbnormalNotification.setStatus(
        "current"
    )

hwEntityExtMonitorBoardNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 9)
)
if mibBuilder.loadTexts:
    hwEntityExtMonitorBoardNormalNotification.setStatus(
        "current"
    )

hwEntityExtMonitorPortAbnormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 10)
)
hwEntityExtMonitorPortAbnormalNotification.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorInputState"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorInputName"))
)
if mibBuilder.loadTexts:
    hwEntityExtMonitorPortAbnormalNotification.setStatus(
        "current"
    )

hwEntityExtMonitorPortNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 11)
)
hwEntityExtMonitorPortNormalNotification.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorInputState"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwMonitorInputName"))
)
if mibBuilder.loadTexts:
    hwEntityExtMonitorPortNormalNotification.setStatus(
        "current"
    )

hwEntityExtCpuUsageLowThresholdNotfication = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 2, 0, 12)
)
hwEntityExtCpuUsageLowThresholdNotfication.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCpuUsage"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityCpuUsageThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTemperature"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityTemperatureThreshold"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAdminStatus"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityAlarmLight"))
)
if mibBuilder.loadTexts:
    hwEntityExtCpuUsageLowThresholdNotfication.setStatus(
        "current"
    )

hwHardwareCapaChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 5, 2, 1)
)
hwHardwareCapaChangeNotification.setObjects(
    ("HUAWEI-ENTITY-EXTENT-MIB", "hwHardwareCapaSequenceNo")
)
if mibBuilder.loadTexts:
    hwHardwareCapaChangeNotification.setStatus(
        "current"
    )

hwEntityHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hwEntityHeartbeatTrap.setStatus(
        "current"
    )

hwInsertDiffFromPreDisposed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 2, 1)
)
hwInsertDiffFromPreDisposed.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeEntPhysicalIndex"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwDisposeEntPhysicalVendorType"),
        ("ENTITY-MIB", "entPhysicalVendorType"))
)
if mibBuilder.loadTexts:
    hwInsertDiffFromPreDisposed.setStatus(
        "current"
    )

hwPreDisposedChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 8, 2, 2)
)
hwPreDisposedChangeNotification.setObjects(
    ("HUAWEI-ENTITY-EXTENT-MIB", "hwPreDisposeSequenceNo")
)
if mibBuilder.loadTexts:
    hwPreDisposedChangeNotification.setStatus(
        "current"
    )


# Notifications groups

hwEntityExtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 2, 2)
)
hwEntityExtNotificationGroup.setObjects(
      *(("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtTemperatureThresholdNotification"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtVoltageLowThresholdNotification"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtVoltageHighThresholdNotification"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtCpuUsageThresholdNotfication"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtMemUsageThresholdNotification"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtOperEnabled"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtOperDisabled"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtMonitorBoardAbnormalNotification"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtMonitorBoardNormalNotification"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtMonitorPortAbnormalNotification"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtMonitorPortNormalNotification"),
        ("HUAWEI-ENTITY-EXTENT-MIB", "hwEntityExtCpuUsageLowThresholdNotfication"))
)
if mibBuilder.loadTexts:
    hwEntityExtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwEntityExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 31, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwEntityExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ENTITY-EXTENT-MIB",
    **{"HwAdminState": HwAdminState,
       "HwOperState": HwOperState,
       "HwStandbyStatus": HwStandbyStatus,
       "HwAlarmStatus": HwAlarmStatus,
       "HWLevelState": HWLevelState,
       "hwEntityExtentMIB": hwEntityExtentMIB,
       "hwEntityExtObjects": hwEntityExtObjects,
       "hwEntityState": hwEntityState,
       "hwEntityStateTable": hwEntityStateTable,
       "hwEntityStateEntry": hwEntityStateEntry,
       "hwEntityAdminStatus": hwEntityAdminStatus,
       "hwEntityOperStatus": hwEntityOperStatus,
       "hwEntityStandbyStatus": hwEntityStandbyStatus,
       "hwEntityAlarmLight": hwEntityAlarmLight,
       "hwEntityCpuUsage": hwEntityCpuUsage,
       "hwEntityCpuUsageThreshold": hwEntityCpuUsageThreshold,
       "hwEntityMemUsage": hwEntityMemUsage,
       "hwEntityMemUsageThreshold": hwEntityMemUsageThreshold,
       "hwEntityMemSize": hwEntityMemSize,
       "hwEntityUpTime": hwEntityUpTime,
       "hwEntityTemperature": hwEntityTemperature,
       "hwEntityTemperatureThreshold": hwEntityTemperatureThreshold,
       "hwEntityVoltage": hwEntityVoltage,
       "hwEntityVoltageLowThreshold": hwEntityVoltageLowThreshold,
       "hwEntityVoltageHighThreshold": hwEntityVoltageHighThreshold,
       "hwEntityTemperatureLowThreshold": hwEntityTemperatureLowThreshold,
       "hwEntityOpticalPower": hwEntityOpticalPower,
       "hwEntityCurrent": hwEntityCurrent,
       "hwEntityMemSizeMega": hwEntityMemSizeMega,
       "hwEntityPortType": hwEntityPortType,
       "hwEntityDuplex": hwEntityDuplex,
       "hwEntityOpticalPowerRx": hwEntityOpticalPowerRx,
       "hwEntityCpuUsageLowThreshold": hwEntityCpuUsageLowThreshold,
       "hwEntityBoardPower": hwEntityBoardPower,
       "hwEntityCpuFrequency": hwEntityCpuFrequency,
       "hwEntitySupportFlexCard": hwEntitySupportFlexCard,
       "hwEntityBoardClass": hwEntityBoardClass,
       "hwNseOpmStatus": hwNseOpmStatus,
       "hwEntityCpuMaxUsage": hwEntityCpuMaxUsage,
       "hwEntityCPUType": hwEntityCPUType,
       "hwEntityMemoryType": hwEntityMemoryType,
       "hwEntityFlashSize": hwEntityFlashSize,
       "hwEntityIfUpTimes": hwEntityIfUpTimes,
       "hwEntityIfDownTimes": hwEntityIfDownTimes,
       "hwEntityCPUAvgUsage": hwEntityCPUAvgUsage,
       "hwEntityMemoryAvgUsage": hwEntityMemoryAvgUsage,
       "hwRUModuleInfoTable": hwRUModuleInfoTable,
       "hwRUModuleInfoEntry": hwRUModuleInfoEntry,
       "hwEntityBomId": hwEntityBomId,
       "hwEntityBomEnDesc": hwEntityBomEnDesc,
       "hwEntityBomLocalDesc": hwEntityBomLocalDesc,
       "hwEntityManufacturedDate": hwEntityManufacturedDate,
       "hwEntityManufactureCode": hwEntityManufactureCode,
       "hwEntityCLEICode": hwEntityCLEICode,
       "hwEntityUpdateLog": hwEntityUpdateLog,
       "hwEntityArchivesInfoVersion": hwEntityArchivesInfoVersion,
       "hwEntityOpenBomId": hwEntityOpenBomId,
       "hwEntityIssueNum": hwEntityIssueNum,
       "hwEntityBoardType": hwEntityBoardType,
       "hwOpticalModuleInfoTable": hwOpticalModuleInfoTable,
       "hwOpticalModuleInfoEntry": hwOpticalModuleInfoEntry,
       "hwEntityOpticalMode": hwEntityOpticalMode,
       "hwEntityOpticalWaveLength": hwEntityOpticalWaveLength,
       "hwEntityOpticalTransDistance": hwEntityOpticalTransDistance,
       "hwEntityOpticalVendorSn": hwEntityOpticalVendorSn,
       "hwEntityOpticalTemperature": hwEntityOpticalTemperature,
       "hwEntityOpticalVoltage": hwEntityOpticalVoltage,
       "hwEntityOpticalBiasCurrent": hwEntityOpticalBiasCurrent,
       "hwEntityOpticalRxPower": hwEntityOpticalRxPower,
       "hwEntityOpticalTxPower": hwEntityOpticalTxPower,
       "hwEntityOpticalType": hwEntityOpticalType,
       "hwEntityOpticalTransBW": hwEntityOpticalTransBW,
       "hwEntityOpticalFiberType": hwEntityOpticalFiberType,
       "hwEntityOpticalRxLowThreshold": hwEntityOpticalRxLowThreshold,
       "hwEntityOpticalRxHighThreshold": hwEntityOpticalRxHighThreshold,
       "hwEntityOpticalTxLowThreshold": hwEntityOpticalTxLowThreshold,
       "hwEntityOpticalTxHighThreshold": hwEntityOpticalTxHighThreshold,
       "hwEntityOpticalPlug": hwEntityOpticalPlug,
       "hwEntityOpticalDirectionType": hwEntityOpticalDirectionType,
       "hwEntityOpticalUserEeprom": hwEntityOpticalUserEeprom,
       "hwEntityOpticalRxLowWarnThreshold": hwEntityOpticalRxLowWarnThreshold,
       "hwEntityOpticalRxHighWarnThreshold": hwEntityOpticalRxHighWarnThreshold,
       "hwEntityOpticalTxLowWarnThreshold": hwEntityOpticalTxLowWarnThreshold,
       "hwEntityOpticalTxHighWarnThreshold": hwEntityOpticalTxHighWarnThreshold,
       "hwMonitorInputTable": hwMonitorInputTable,
       "hwMonitorInputEntry": hwMonitorInputEntry,
       "hwMonitorInputIndex": hwMonitorInputIndex,
       "hwMonitorInputName": hwMonitorInputName,
       "hwMonitorInputState": hwMonitorInputState,
       "hwMonitorInputStateEnable": hwMonitorInputStateEnable,
       "hwMonitorInputRowStatus": hwMonitorInputRowStatus,
       "hwMonitorOutputTable": hwMonitorOutputTable,
       "hwMonitorOutputEntry": hwMonitorOutputEntry,
       "hwMonitorOutputIndex": hwMonitorOutputIndex,
       "hwMonitorOutputRuleIndex": hwMonitorOutputRuleIndex,
       "hwMonitorOutputMask": hwMonitorOutputMask,
       "hwMonitorOutputKey": hwMonitorOutputKey,
       "hwMonitorOutputRowStatus": hwMonitorOutputRowStatus,
       "hwEntPowerUsedInfoTable": hwEntPowerUsedInfoTable,
       "hwEntPowerUsedInfoEntry": hwEntPowerUsedInfoEntry,
       "hwEntPowerUsedInfoBoardName": hwEntPowerUsedInfoBoardName,
       "hwEntPowerUsedInfoBoardType": hwEntPowerUsedInfoBoardType,
       "hwEntPowerUsedInfoBoardSlot": hwEntPowerUsedInfoBoardSlot,
       "hwEntPowerUsedInfoPower": hwEntPowerUsedInfoPower,
       "hwVirtualCableTestTable": hwVirtualCableTestTable,
       "hwVirtualCableTestEntry": hwVirtualCableTestEntry,
       "hwVirtualCableTestIfIndex": hwVirtualCableTestIfIndex,
       "hwVirtualCableTestPairStatus": hwVirtualCableTestPairStatus,
       "hwVirtualCableTestPairLength": hwVirtualCableTestPairLength,
       "hwVirtualCableTestOperation": hwVirtualCableTestOperation,
       "hwVirtualCableTestLastTime": hwVirtualCableTestLastTime,
       "hwVirtualCableTestPairAStatus": hwVirtualCableTestPairAStatus,
       "hwVirtualCableTestPairBStatus": hwVirtualCableTestPairBStatus,
       "hwVirtualCableTestPairCStatus": hwVirtualCableTestPairCStatus,
       "hwVirtualCableTestPairDStatus": hwVirtualCableTestPairDStatus,
       "hwVirtualCableTestPairALength": hwVirtualCableTestPairALength,
       "hwVirtualCableTestPairBLength": hwVirtualCableTestPairBLength,
       "hwVirtualCableTestPairCLength": hwVirtualCableTestPairCLength,
       "hwVirtualCableTestPairDLength": hwVirtualCableTestPairDLength,
       "hwTemperatureThresholdTable": hwTemperatureThresholdTable,
       "hwTemperatureThresholdEntry": hwTemperatureThresholdEntry,
       "hwEntityTempSlotId": hwEntityTempSlotId,
       "hwEntityTempI2CId": hwEntityTempI2CId,
       "hwEntityTempAddr": hwEntityTempAddr,
       "hwEntityTempChannel": hwEntityTempChannel,
       "hwEntityTempStatus": hwEntityTempStatus,
       "hwEntityTempValue": hwEntityTempValue,
       "hwEntityTempMinorAlmThreshold": hwEntityTempMinorAlmThreshold,
       "hwEntityTempMajorAlmThreshold": hwEntityTempMajorAlmThreshold,
       "hwEntityTempFatalAlmThreshold": hwEntityTempFatalAlmThreshold,
       "hwVoltageInfoTable": hwVoltageInfoTable,
       "hwVoltageInfoEntry": hwVoltageInfoEntry,
       "hwEntityVolSlot": hwEntityVolSlot,
       "hwEntityVolI2CId": hwEntityVolI2CId,
       "hwEntityVolAddr": hwEntityVolAddr,
       "hwEntityVolChannel": hwEntityVolChannel,
       "hwEntityVolStatus": hwEntityVolStatus,
       "hwEntityVolRequired": hwEntityVolRequired,
       "hwEntityVolCurValue": hwEntityVolCurValue,
       "hwEntityVolRatio": hwEntityVolRatio,
       "hwEntityVolLowAlmMajor": hwEntityVolLowAlmMajor,
       "hwEntityVolLowAlmFatal": hwEntityVolLowAlmFatal,
       "hwEntityVolHighAlmMajor": hwEntityVolHighAlmMajor,
       "hwEntityVolHighAlmFatal": hwEntityVolHighAlmFatal,
       "hwFanStatusTable": hwFanStatusTable,
       "hwFanStatusEntry": hwFanStatusEntry,
       "hwEntityFanSlot": hwEntityFanSlot,
       "hwEntityFanSn": hwEntityFanSn,
       "hwEntityFanReg": hwEntityFanReg,
       "hwEntityFanSpdAdjMode": hwEntityFanSpdAdjMode,
       "hwEntityFanSpeed": hwEntityFanSpeed,
       "hwEntityFanPresent": hwEntityFanPresent,
       "hwEntityFanState": hwEntityFanState,
       "hwEntityGlobalPara": hwEntityGlobalPara,
       "hwEntityServiceType": hwEntityServiceType,
       "hwPortBip8StatisticsTable": hwPortBip8StatisticsTable,
       "hwPortBip8StatisticsEntry": hwPortBip8StatisticsEntry,
       "hwPhysicalPortBip8StatisticsEB": hwPhysicalPortBip8StatisticsEB,
       "hwPhysicalPortBip8StatisticsES": hwPhysicalPortBip8StatisticsES,
       "hwPhysicalPortBip8StatisticsSES": hwPhysicalPortBip8StatisticsSES,
       "hwPhysicalPortBip8StatisticsUAS": hwPhysicalPortBip8StatisticsUAS,
       "hwPhysicalPortBip8StatisticsBBE": hwPhysicalPortBip8StatisticsBBE,
       "hwPhysicalPortSpeed": hwPhysicalPortSpeed,
       "hwEntityExtTraps": hwEntityExtTraps,
       "hwEntityExtTrapsPrefix": hwEntityExtTrapsPrefix,
       "hwEntityExtTemperatureThresholdNotification": hwEntityExtTemperatureThresholdNotification,
       "hwEntityExtVoltageLowThresholdNotification": hwEntityExtVoltageLowThresholdNotification,
       "hwEntityExtVoltageHighThresholdNotification": hwEntityExtVoltageHighThresholdNotification,
       "hwEntityExtCpuUsageThresholdNotfication": hwEntityExtCpuUsageThresholdNotfication,
       "hwEntityExtMemUsageThresholdNotification": hwEntityExtMemUsageThresholdNotification,
       "hwEntityExtOperEnabled": hwEntityExtOperEnabled,
       "hwEntityExtOperDisabled": hwEntityExtOperDisabled,
       "hwEntityExtMonitorBoardAbnormalNotification": hwEntityExtMonitorBoardAbnormalNotification,
       "hwEntityExtMonitorBoardNormalNotification": hwEntityExtMonitorBoardNormalNotification,
       "hwEntityExtMonitorPortAbnormalNotification": hwEntityExtMonitorPortAbnormalNotification,
       "hwEntityExtMonitorPortNormalNotification": hwEntityExtMonitorPortNormalNotification,
       "hwEntityExtCpuUsageLowThresholdNotfication": hwEntityExtCpuUsageLowThresholdNotfication,
       "hwDevicePowerInfoObjects": hwDevicePowerInfoObjects,
       "hwDevicePowerInfoTotalPower": hwDevicePowerInfoTotalPower,
       "hwDevicePowerInfoUsedPower": hwDevicePowerInfoUsedPower,
       "hwEntityExtConformance": hwEntityExtConformance,
       "hwEntityExtCompliances": hwEntityExtCompliances,
       "hwEntityExtCompliance": hwEntityExtCompliance,
       "hwEntityExtGroups": hwEntityExtGroups,
       "hwEntityExtGroup": hwEntityExtGroup,
       "hwEntityExtNotificationGroup": hwEntityExtNotificationGroup,
       "hwRUModuleInfoGroup": hwRUModuleInfoGroup,
       "hwEntityExtOldObjectsGroup": hwEntityExtOldObjectsGroup,
       "hwOpticalModuleInfoGroup": hwOpticalModuleInfoGroup,
       "hwMonitorInputGroup": hwMonitorInputGroup,
       "hwMonitorOutputGroup": hwMonitorOutputGroup,
       "hwEntPowerUsedInfoGroup": hwEntPowerUsedInfoGroup,
       "hwDevicePowerInfoGroup": hwDevicePowerInfoGroup,
       "hwVirtualCableTestGroup": hwVirtualCableTestGroup,
       "hwTemperatureThresholdGroup": hwTemperatureThresholdGroup,
       "hwVoltageInfoGroup": hwVoltageInfoGroup,
       "hwFanStatusGroup": hwFanStatusGroup,
       "hwPnpGroup": hwPnpGroup,
       "hwSystemGlobalGroup": hwSystemGlobalGroup,
       "hwHeartbeatGroup": hwHeartbeatGroup,
       "hwPortBip8StatisticsObjectGroup": hwPortBip8StatisticsObjectGroup,
       "hwPredisposeGroup": hwPredisposeGroup,
       "hwPnpObjects": hwPnpObjects,
       "hwPnpInfo": hwPnpInfo,
       "hwHardwareCapaSequenceNo": hwHardwareCapaSequenceNo,
       "hwPnpTraps": hwPnpTraps,
       "hwHardwareCapaChangeNotification": hwHardwareCapaChangeNotification,
       "hwPnpOperateTable": hwPnpOperateTable,
       "hwPnpOperateEntry": hwPnpOperateEntry,
       "hwFileGeneIndex": hwFileGeneIndex,
       "hwFileGeneOperState": hwFileGeneOperState,
       "hwFileGeneResourceType": hwFileGeneResourceType,
       "hwFileGeneResourceID": hwFileGeneResourceID,
       "hwFileGeneDestinationFile": hwFileGeneDestinationFile,
       "hwFileGeneRowStatus": hwFileGeneRowStatus,
       "hwSystemGlobalObjects": hwSystemGlobalObjects,
       "hwEntitySystemNetID": hwEntitySystemNetID,
       "hwEntitySoftwareName": hwEntitySoftwareName,
       "hwEntitySoftwareVersion": hwEntitySoftwareVersion,
       "hwEntitySoftwareVendor": hwEntitySoftwareVendor,
       "hwEntitySystemModel": hwEntitySystemModel,
       "hwEntitySystemTime": hwEntitySystemTime,
       "hwEntitySystemMacAddress": hwEntitySystemMacAddress,
       "hwEntitySystemReset": hwEntitySystemReset,
       "hwEntitySystemHealthInterval": hwEntitySystemHealthInterval,
       "hwEntitySystemNEId": hwEntitySystemNEId,
       "hwHeartbeatObjects": hwHeartbeatObjects,
       "hwHeartbeatConfig": hwHeartbeatConfig,
       "hwEntityHeartbeatOnOff": hwEntityHeartbeatOnOff,
       "hwEntityHeartbeatPeriod": hwEntityHeartbeatPeriod,
       "hwHeartbeatTrapPrefix": hwHeartbeatTrapPrefix,
       "hwEntityHeartbeatTrap": hwEntityHeartbeatTrap,
       "hwPreDisposeObjects": hwPreDisposeObjects,
       "hwPreDisposeInfo": hwPreDisposeInfo,
       "hwPreDisposeSequenceNo": hwPreDisposeSequenceNo,
       "hwPreDisposedTraps": hwPreDisposedTraps,
       "hwInsertDiffFromPreDisposed": hwInsertDiffFromPreDisposed,
       "hwPreDisposedChangeNotification": hwPreDisposedChangeNotification,
       "hwPreDisposeConfigTable": hwPreDisposeConfigTable,
       "hwPreDisposeConfigEntry": hwPreDisposeConfigEntry,
       "hwDisposeSlot": hwDisposeSlot,
       "hwDisposeCardId": hwDisposeCardId,
       "hwDisposeSbom": hwDisposeSbom,
       "hwDisposeRowStatus": hwDisposeRowStatus,
       "hwDisposeOperState": hwDisposeOperState,
       "hwPreDisposeEntInfoTable": hwPreDisposeEntInfoTable,
       "hwPreDisposeEntInfoEntry": hwPreDisposeEntInfoEntry,
       "hwDisposeEntPhysicalIndex": hwDisposeEntPhysicalIndex,
       "hwDisposeEntPhysicalDescr": hwDisposeEntPhysicalDescr,
       "hwDisposeEntPhysicalVendorType": hwDisposeEntPhysicalVendorType,
       "hwDisposeEntPhysicalContainedIn": hwDisposeEntPhysicalContainedIn,
       "hwDisposeEntPhysicalClass": hwDisposeEntPhysicalClass,
       "hwDisposeEntPhysicalParentRelPos": hwDisposeEntPhysicalParentRelPos,
       "hwDisposeEntPhysicalName": hwDisposeEntPhysicalName}
)

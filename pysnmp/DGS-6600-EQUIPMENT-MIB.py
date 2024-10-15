# SNMP MIB module (DGS-6600-EQUIPMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS-6600-EQUIPMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:27:58 2024
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

(dgs6600_system,) = mibBuilder.importSymbols(
    "DGS-6600-ID-MIB",
    "dgs6600-system")

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

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

dgs6600EquipmentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChassisControlModuleLEDInfo_ObjectIdentity = ObjectIdentity
chassisControlModuleLEDInfo = _ChassisControlModuleLEDInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 1)
)
_ChassisControlModuleLEDInfoTable_Object = MibTable
chassisControlModuleLEDInfoTable = _ChassisControlModuleLEDInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    chassisControlModuleLEDInfoTable.setStatus("current")
_ChassisControlModuleLEDInfoEntry_Object = MibTableRow
chassisControlModuleLEDInfoEntry = _ChassisControlModuleLEDInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 1, 1, 1)
)
chassisControlModuleLEDInfoEntry.setIndexNames(
    (0, "DGS-6600-EQUIPMENT-MIB", "chassisControlModuleLEDInfoIndex"),
)
if mibBuilder.loadTexts:
    chassisControlModuleLEDInfoEntry.setStatus("current")


class _ChassisControlModuleLEDInfoIndex_Type(Integer32):
    """Custom type chassisControlModuleLEDInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ChassisControlModuleLEDInfoIndex_Type.__name__ = "Integer32"
_ChassisControlModuleLEDInfoIndex_Object = MibTableColumn
chassisControlModuleLEDInfoIndex = _ChassisControlModuleLEDInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 1, 1, 1, 1),
    _ChassisControlModuleLEDInfoIndex_Type()
)
chassisControlModuleLEDInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisControlModuleLEDInfoIndex.setStatus("current")


class _ChassisControlModuleLEDInfoConsole_Type(Integer32):
    """Custom type chassisControlModuleLEDInfoConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 1),
          ("usb", 2))
    )


_ChassisControlModuleLEDInfoConsole_Type.__name__ = "Integer32"
_ChassisControlModuleLEDInfoConsole_Object = MibTableColumn
chassisControlModuleLEDInfoConsole = _ChassisControlModuleLEDInfoConsole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 1, 1, 1, 2),
    _ChassisControlModuleLEDInfoConsole_Type()
)
chassisControlModuleLEDInfoConsole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisControlModuleLEDInfoConsole.setStatus("current")


class _ChassisControlModuleLEDInfoMaster_Type(Integer32):
    """Custom type chassisControlModuleLEDInfoMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_ChassisControlModuleLEDInfoMaster_Type.__name__ = "Integer32"
_ChassisControlModuleLEDInfoMaster_Object = MibTableColumn
chassisControlModuleLEDInfoMaster = _ChassisControlModuleLEDInfoMaster_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 1, 1, 1, 3),
    _ChassisControlModuleLEDInfoMaster_Type()
)
chassisControlModuleLEDInfoMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisControlModuleLEDInfoMaster.setStatus("current")


class _ChassisControlModuleLEDInfoCPUUtilization_Type(Integer32):
    """Custom type chassisControlModuleLEDInfoCPUUtilization based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight-LEDs", 8),
          ("five-LEDs", 5),
          ("four-LEDs", 4),
          ("one-LED", 1),
          ("seven-LEDs", 7),
          ("six-LEDs", 6),
          ("three-LEDs", 3),
          ("two-LEDs", 2),
          ("zero-LED", 0))
    )


_ChassisControlModuleLEDInfoCPUUtilization_Type.__name__ = "Integer32"
_ChassisControlModuleLEDInfoCPUUtilization_Object = MibTableColumn
chassisControlModuleLEDInfoCPUUtilization = _ChassisControlModuleLEDInfoCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 1, 1, 1, 4),
    _ChassisControlModuleLEDInfoCPUUtilization_Type()
)
chassisControlModuleLEDInfoCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisControlModuleLEDInfoCPUUtilization.setStatus("current")


class _ChassisControlModuleLEDInfoMgmtPortStatus_Type(Integer32):
    """Custom type chassisControlModuleLEDInfoMgmtPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blinking-green", 3),
          ("off", 1),
          ("steady-green", 2))
    )


_ChassisControlModuleLEDInfoMgmtPortStatus_Type.__name__ = "Integer32"
_ChassisControlModuleLEDInfoMgmtPortStatus_Object = MibTableColumn
chassisControlModuleLEDInfoMgmtPortStatus = _ChassisControlModuleLEDInfoMgmtPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 1, 1, 1, 5),
    _ChassisControlModuleLEDInfoMgmtPortStatus_Type()
)
chassisControlModuleLEDInfoMgmtPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisControlModuleLEDInfoMgmtPortStatus.setStatus("current")


class _ChassisControlModuleLEDInfoMgmtPortSpeed_Type(Integer32):
    """Custom type chassisControlModuleLEDInfoMgmtPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-0", 1),
          ("link-100", 2),
          ("link-1000", 3))
    )


_ChassisControlModuleLEDInfoMgmtPortSpeed_Type.__name__ = "Integer32"
_ChassisControlModuleLEDInfoMgmtPortSpeed_Object = MibTableColumn
chassisControlModuleLEDInfoMgmtPortSpeed = _ChassisControlModuleLEDInfoMgmtPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 1, 1, 1, 6),
    _ChassisControlModuleLEDInfoMgmtPortSpeed_Type()
)
chassisControlModuleLEDInfoMgmtPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisControlModuleLEDInfoMgmtPortSpeed.setStatus("current")
_ChassisPowerInfo_ObjectIdentity = ObjectIdentity
chassisPowerInfo = _ChassisPowerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 2)
)
_ChassisPowerInfoTable_Object = MibTable
chassisPowerInfoTable = _ChassisPowerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    chassisPowerInfoTable.setStatus("current")
_ChassisPowerInfoEntry_Object = MibTableRow
chassisPowerInfoEntry = _ChassisPowerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 2, 1, 1)
)
chassisPowerInfoEntry.setIndexNames(
    (0, "DGS-6600-EQUIPMENT-MIB", "chassisPowerIndex"),
)
if mibBuilder.loadTexts:
    chassisPowerInfoEntry.setStatus("current")


class _ChassisPowerIndex_Type(Integer32):
    """Custom type chassisPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ChassisPowerIndex_Type.__name__ = "Integer32"
_ChassisPowerIndex_Object = MibTableColumn
chassisPowerIndex = _ChassisPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 2, 1, 1, 1),
    _ChassisPowerIndex_Type()
)
chassisPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerIndex.setStatus("current")


class _ChassisPowerExist_Type(Integer32):
    """Custom type chassisPowerExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("exist", 2))
    )


_ChassisPowerExist_Type.__name__ = "Integer32"
_ChassisPowerExist_Object = MibTableColumn
chassisPowerExist = _ChassisPowerExist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 2, 1, 1, 2),
    _ChassisPowerExist_Type()
)
chassisPowerExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerExist.setStatus("current")


class _ChassisPowerType_Type(Integer32):
    """Custom type chassisPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("AC", 1),
          ("DC", 2),
          ("Unknown", 3))
    )


_ChassisPowerType_Type.__name__ = "Integer32"
_ChassisPowerType_Object = MibTableColumn
chassisPowerType = _ChassisPowerType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 2, 1, 1, 3),
    _ChassisPowerType_Type()
)
chassisPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerType.setStatus("current")


class _ChassisPowerAlive_Type(Integer32):
    """Custom type chassisPowerAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("in-operation", 2))
    )


_ChassisPowerAlive_Type.__name__ = "Integer32"
_ChassisPowerAlive_Object = MibTableColumn
chassisPowerAlive = _ChassisPowerAlive_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 2, 1, 1, 4),
    _ChassisPowerAlive_Type()
)
chassisPowerAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerAlive.setStatus("current")
_ChassisPowerVoltage_Type = Integer32
_ChassisPowerVoltage_Object = MibTableColumn
chassisPowerVoltage = _ChassisPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 2, 1, 1, 5),
    _ChassisPowerVoltage_Type()
)
chassisPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerVoltage.setStatus("current")
_ChassisPowerCurrent_Type = Integer32
_ChassisPowerCurrent_Object = MibTableColumn
chassisPowerCurrent = _ChassisPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 2, 1, 1, 6),
    _ChassisPowerCurrent_Type()
)
chassisPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerCurrent.setStatus("current")
_ChassisPowerPowerWatt_Type = Integer32
_ChassisPowerPowerWatt_Object = MibTableColumn
chassisPowerPowerWatt = _ChassisPowerPowerWatt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 2, 1, 1, 7),
    _ChassisPowerPowerWatt_Type()
)
chassisPowerPowerWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerPowerWatt.setStatus("current")
_ChassisPowerFanSpeed_Type = Integer32
_ChassisPowerFanSpeed_Object = MibTableColumn
chassisPowerFanSpeed = _ChassisPowerFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 2, 1, 1, 8),
    _ChassisPowerFanSpeed_Type()
)
chassisPowerFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerFanSpeed.setStatus("current")
_ChassisFanTrayInfo_ObjectIdentity = ObjectIdentity
chassisFanTrayInfo = _ChassisFanTrayInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 3)
)


class _ChassisFanTrayInfoState_Type(Integer32):
    """Custom type chassisFanTrayInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("in-operation", 3),
          ("not-exist", 1))
    )


_ChassisFanTrayInfoState_Type.__name__ = "Integer32"
_ChassisFanTrayInfoState_Object = MibScalar
chassisFanTrayInfoState = _ChassisFanTrayInfoState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 3, 1),
    _ChassisFanTrayInfoState_Type()
)
chassisFanTrayInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanTrayInfoState.setStatus("current")
_ChassisFanInfoTable_Object = MibTable
chassisFanInfoTable = _ChassisFanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    chassisFanInfoTable.setStatus("current")
_ChassisFanInfoEntry_Object = MibTableRow
chassisFanInfoEntry = _ChassisFanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 3, 2, 1)
)
chassisFanInfoEntry.setIndexNames(
    (0, "DGS-6600-EQUIPMENT-MIB", "chassisFanIndex"),
)
if mibBuilder.loadTexts:
    chassisFanInfoEntry.setStatus("current")


class _ChassisFanIndex_Type(Integer32):
    """Custom type chassisFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ChassisFanIndex_Type.__name__ = "Integer32"
_ChassisFanIndex_Object = MibTableColumn
chassisFanIndex = _ChassisFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 3, 2, 1, 1),
    _ChassisFanIndex_Type()
)
chassisFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanIndex.setStatus("current")


class _ChassisFanStatus_Type(Integer32):
    """Custom type chassisFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2))
    )


_ChassisFanStatus_Type.__name__ = "Integer32"
_ChassisFanStatus_Object = MibTableColumn
chassisFanStatus = _ChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 3, 2, 1, 2),
    _ChassisFanStatus_Type()
)
chassisFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanStatus.setStatus("current")
_ChassisFanSpeed_Type = Integer32
_ChassisFanSpeed_Object = MibTableColumn
chassisFanSpeed = _ChassisFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 3, 2, 1, 3),
    _ChassisFanSpeed_Type()
)
chassisFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanSpeed.setStatus("current")
_ChassisSlotInfo_ObjectIdentity = ObjectIdentity
chassisSlotInfo = _ChassisSlotInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4)
)
_ChassisSlotInfoTable_Object = MibTable
chassisSlotInfoTable = _ChassisSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    chassisSlotInfoTable.setStatus("current")
_ChassisSlotInfoEntry_Object = MibTableRow
chassisSlotInfoEntry = _ChassisSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1)
)
chassisSlotInfoEntry.setIndexNames(
    (0, "DGS-6600-EQUIPMENT-MIB", "chassisSlotIndex"),
)
if mibBuilder.loadTexts:
    chassisSlotInfoEntry.setStatus("current")


class _ChassisSlotIndex_Type(Integer32):
    """Custom type chassisSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ChassisSlotIndex_Type.__name__ = "Integer32"
_ChassisSlotIndex_Object = MibTableColumn
chassisSlotIndex = _ChassisSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 1),
    _ChassisSlotIndex_Type()
)
chassisSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotIndex.setStatus("current")


class _ChassisSlotState_Type(Integer32):
    """Custom type chassisSlotState based on Integer32"""
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
        *(("booting", 4),
          ("empty", 1),
          ("failed", 3),
          ("in-operation", 5),
          ("no-power", 2))
    )


_ChassisSlotState_Type.__name__ = "Integer32"
_ChassisSlotState_Object = MibTableColumn
chassisSlotState = _ChassisSlotState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 2),
    _ChassisSlotState_Type()
)
chassisSlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotState.setStatus("current")


class _ChassisSlotLEDPoEModeEnabled_Type(Integer32):
    """Custom type chassisSlotLEDPoEModeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChassisSlotLEDPoEModeEnabled_Type.__name__ = "Integer32"
_ChassisSlotLEDPoEModeEnabled_Object = MibTableColumn
chassisSlotLEDPoEModeEnabled = _ChassisSlotLEDPoEModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 3),
    _ChassisSlotLEDPoEModeEnabled_Type()
)
chassisSlotLEDPoEModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotLEDPoEModeEnabled.setStatus("current")
_ChassisSlotModel_Type = DisplayString
_ChassisSlotModel_Object = MibTableColumn
chassisSlotModel = _ChassisSlotModel_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 4),
    _ChassisSlotModel_Type()
)
chassisSlotModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotModel.setStatus("current")
_ChassisSlotSerialNumber_Type = DisplayString
_ChassisSlotSerialNumber_Object = MibTableColumn
chassisSlotSerialNumber = _ChassisSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 5),
    _ChassisSlotSerialNumber_Type()
)
chassisSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotSerialNumber.setStatus("current")
_ChassisSlotHwVersion_Type = DisplayString
_ChassisSlotHwVersion_Object = MibTableColumn
chassisSlotHwVersion = _ChassisSlotHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 6),
    _ChassisSlotHwVersion_Type()
)
chassisSlotHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotHwVersion.setStatus("current")
_ChassisSlotPCBAVersion_Type = DisplayString
_ChassisSlotPCBAVersion_Object = MibTableColumn
chassisSlotPCBAVersion = _ChassisSlotPCBAVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 7),
    _ChassisSlotPCBAVersion_Type()
)
chassisSlotPCBAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotPCBAVersion.setStatus("current")
_ChassisSlotBootloaderVersion_Type = DisplayString
_ChassisSlotBootloaderVersion_Object = MibTableColumn
chassisSlotBootloaderVersion = _ChassisSlotBootloaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 8),
    _ChassisSlotBootloaderVersion_Type()
)
chassisSlotBootloaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotBootloaderVersion.setStatus("current")
_ChassisSlotRuntimeVersion_Type = DisplayString
_ChassisSlotRuntimeVersion_Object = MibTableColumn
chassisSlotRuntimeVersion = _ChassisSlotRuntimeVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 9),
    _ChassisSlotRuntimeVersion_Type()
)
chassisSlotRuntimeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotRuntimeVersion.setStatus("current")
_ChassisSlotCPLDVersion_Type = DisplayString
_ChassisSlotCPLDVersion_Object = MibTableColumn
chassisSlotCPLDVersion = _ChassisSlotCPLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 10),
    _ChassisSlotCPLDVersion_Type()
)
chassisSlotCPLDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotCPLDVersion.setStatus("current")
_ChassisSlotFirsMacAddress_Type = MacAddress
_ChassisSlotFirsMacAddress_Object = MibTableColumn
chassisSlotFirsMacAddress = _ChassisSlotFirsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 11),
    _ChassisSlotFirsMacAddress_Type()
)
chassisSlotFirsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotFirsMacAddress.setStatus("current")
_ChassisSlotNumberOfMacAddress_Type = Integer32
_ChassisSlotNumberOfMacAddress_Object = MibTableColumn
chassisSlotNumberOfMacAddress = _ChassisSlotNumberOfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 4, 1, 1, 12),
    _ChassisSlotNumberOfMacAddress_Type()
)
chassisSlotNumberOfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotNumberOfMacAddress.setStatus("current")
_ChassisTemperatureInfo_ObjectIdentity = ObjectIdentity
chassisTemperatureInfo = _ChassisTemperatureInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5)
)
_ChassisTemperatureInfoTable_Object = MibTable
chassisTemperatureInfoTable = _ChassisTemperatureInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    chassisTemperatureInfoTable.setStatus("current")
_ChassisTemperatureInfoEntry_Object = MibTableRow
chassisTemperatureInfoEntry = _ChassisTemperatureInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1, 1)
)
chassisTemperatureInfoEntry.setIndexNames(
    (0, "DGS-6600-EQUIPMENT-MIB", "chassisTemperatureSlotIndex"),
)
if mibBuilder.loadTexts:
    chassisTemperatureInfoEntry.setStatus("current")


class _ChassisTemperatureSlotIndex_Type(Integer32):
    """Custom type chassisTemperatureSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ChassisTemperatureSlotIndex_Type.__name__ = "Integer32"
_ChassisTemperatureSlotIndex_Object = MibTableColumn
chassisTemperatureSlotIndex = _ChassisTemperatureSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1, 1, 1),
    _ChassisTemperatureSlotIndex_Type()
)
chassisTemperatureSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperatureSlotIndex.setStatus("current")
_ChassisTemperatureInletCurrent_Type = DisplayString
_ChassisTemperatureInletCurrent_Object = MibTableColumn
chassisTemperatureInletCurrent = _ChassisTemperatureInletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1, 1, 2),
    _ChassisTemperatureInletCurrent_Type()
)
chassisTemperatureInletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperatureInletCurrent.setStatus("current")
_ChassisTemperatureInletOverheat_Type = DisplayString
_ChassisTemperatureInletOverheat_Object = MibTableColumn
chassisTemperatureInletOverheat = _ChassisTemperatureInletOverheat_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1, 1, 3),
    _ChassisTemperatureInletOverheat_Type()
)
chassisTemperatureInletOverheat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperatureInletOverheat.setStatus("current")
_ChassisTemperatureInletHeatdown_Type = DisplayString
_ChassisTemperatureInletHeatdown_Object = MibTableColumn
chassisTemperatureInletHeatdown = _ChassisTemperatureInletHeatdown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1, 1, 4),
    _ChassisTemperatureInletHeatdown_Type()
)
chassisTemperatureInletHeatdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperatureInletHeatdown.setStatus("current")
_ChassisTemperatureCenterCurrent_Type = DisplayString
_ChassisTemperatureCenterCurrent_Object = MibTableColumn
chassisTemperatureCenterCurrent = _ChassisTemperatureCenterCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1, 1, 5),
    _ChassisTemperatureCenterCurrent_Type()
)
chassisTemperatureCenterCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperatureCenterCurrent.setStatus("current")
_ChassisTemperatureCenterOverheat_Type = DisplayString
_ChassisTemperatureCenterOverheat_Object = MibTableColumn
chassisTemperatureCenterOverheat = _ChassisTemperatureCenterOverheat_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1, 1, 6),
    _ChassisTemperatureCenterOverheat_Type()
)
chassisTemperatureCenterOverheat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperatureCenterOverheat.setStatus("current")
_ChassisTemperatureCenterHeatdown_Type = DisplayString
_ChassisTemperatureCenterHeatdown_Object = MibTableColumn
chassisTemperatureCenterHeatdown = _ChassisTemperatureCenterHeatdown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1, 1, 7),
    _ChassisTemperatureCenterHeatdown_Type()
)
chassisTemperatureCenterHeatdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperatureCenterHeatdown.setStatus("current")
_ChassisTemperatureOutletCurrent_Type = DisplayString
_ChassisTemperatureOutletCurrent_Object = MibTableColumn
chassisTemperatureOutletCurrent = _ChassisTemperatureOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1, 1, 8),
    _ChassisTemperatureOutletCurrent_Type()
)
chassisTemperatureOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperatureOutletCurrent.setStatus("current")
_ChassisTemperatureOutletOverheat_Type = DisplayString
_ChassisTemperatureOutletOverheat_Object = MibTableColumn
chassisTemperatureOutletOverheat = _ChassisTemperatureOutletOverheat_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1, 1, 9),
    _ChassisTemperatureOutletOverheat_Type()
)
chassisTemperatureOutletOverheat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperatureOutletOverheat.setStatus("current")
_ChassisTemperatureOutletHeatdown_Type = DisplayString
_ChassisTemperatureOutletHeatdown_Object = MibTableColumn
chassisTemperatureOutletHeatdown = _ChassisTemperatureOutletHeatdown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 5, 1, 1, 10),
    _ChassisTemperatureOutletHeatdown_Type()
)
chassisTemperatureOutletHeatdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperatureOutletHeatdown.setStatus("current")
_ChassisPortLEDInfo_ObjectIdentity = ObjectIdentity
chassisPortLEDInfo = _ChassisPortLEDInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 6)
)
_ChassisPortLEDInfoTable_Object = MibTable
chassisPortLEDInfoTable = _ChassisPortLEDInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    chassisPortLEDInfoTable.setStatus("current")
_ChassisPortLEDInfoEntry_Object = MibTableRow
chassisPortLEDInfoEntry = _ChassisPortLEDInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 6, 1, 1)
)
chassisPortLEDInfoEntry.setIndexNames(
    (0, "DGS-6600-EQUIPMENT-MIB", "chassisPortLEDIFIndex"),
)
if mibBuilder.loadTexts:
    chassisPortLEDInfoEntry.setStatus("current")
_ChassisPortLEDIFIndex_Type = Integer32
_ChassisPortLEDIFIndex_Object = MibTableColumn
chassisPortLEDIFIndex = _ChassisPortLEDIFIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 6, 1, 1, 1),
    _ChassisPortLEDIFIndex_Type()
)
chassisPortLEDIFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPortLEDIFIndex.setStatus("current")
_ChassisPortLEDIFName_Type = DisplayString
_ChassisPortLEDIFName_Object = MibTableColumn
chassisPortLEDIFName = _ChassisPortLEDIFName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 6, 1, 1, 2),
    _ChassisPortLEDIFName_Type()
)
chassisPortLEDIFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPortLEDIFName.setStatus("current")


class _ChassisPortLEDStatus_Type(Integer32):
    """Custom type chassisPortLEDStatus based on Integer32"""
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
        *(("blinking-amber", 4),
          ("blinking-green", 5),
          ("off", 1),
          ("steady-amber", 2),
          ("steady-green", 3))
    )


_ChassisPortLEDStatus_Type.__name__ = "Integer32"
_ChassisPortLEDStatus_Object = MibTableColumn
chassisPortLEDStatus = _ChassisPortLEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 6, 1, 1, 3),
    _ChassisPortLEDStatus_Type()
)
chassisPortLEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPortLEDStatus.setStatus("current")


class _ChassisPortLEDMode_Type(Integer32):
    """Custom type chassisPortLEDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("poe", 2))
    )


_ChassisPortLEDMode_Type.__name__ = "Integer32"
_ChassisPortLEDMode_Object = MibTableColumn
chassisPortLEDMode = _ChassisPortLEDMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 6, 1, 1, 4),
    _ChassisPortLEDMode_Type()
)
chassisPortLEDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPortLEDMode.setStatus("current")


class _ChassisPortLEDMediumType_Type(Integer32):
    """Custom type chassisPortLEDMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_ChassisPortLEDMediumType_Type.__name__ = "Integer32"
_ChassisPortLEDMediumType_Object = MibTableColumn
chassisPortLEDMediumType = _ChassisPortLEDMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 2, 6, 1, 1, 5),
    _ChassisPortLEDMediumType_Type()
)
chassisPortLEDMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPortLEDMediumType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS-6600-EQUIPMENT-MIB",
    **{"dgs6600EquipmentMIB": dgs6600EquipmentMIB,
       "chassisControlModuleLEDInfo": chassisControlModuleLEDInfo,
       "chassisControlModuleLEDInfoTable": chassisControlModuleLEDInfoTable,
       "chassisControlModuleLEDInfoEntry": chassisControlModuleLEDInfoEntry,
       "chassisControlModuleLEDInfoIndex": chassisControlModuleLEDInfoIndex,
       "chassisControlModuleLEDInfoConsole": chassisControlModuleLEDInfoConsole,
       "chassisControlModuleLEDInfoMaster": chassisControlModuleLEDInfoMaster,
       "chassisControlModuleLEDInfoCPUUtilization": chassisControlModuleLEDInfoCPUUtilization,
       "chassisControlModuleLEDInfoMgmtPortStatus": chassisControlModuleLEDInfoMgmtPortStatus,
       "chassisControlModuleLEDInfoMgmtPortSpeed": chassisControlModuleLEDInfoMgmtPortSpeed,
       "chassisPowerInfo": chassisPowerInfo,
       "chassisPowerInfoTable": chassisPowerInfoTable,
       "chassisPowerInfoEntry": chassisPowerInfoEntry,
       "chassisPowerIndex": chassisPowerIndex,
       "chassisPowerExist": chassisPowerExist,
       "chassisPowerType": chassisPowerType,
       "chassisPowerAlive": chassisPowerAlive,
       "chassisPowerVoltage": chassisPowerVoltage,
       "chassisPowerCurrent": chassisPowerCurrent,
       "chassisPowerPowerWatt": chassisPowerPowerWatt,
       "chassisPowerFanSpeed": chassisPowerFanSpeed,
       "chassisFanTrayInfo": chassisFanTrayInfo,
       "chassisFanTrayInfoState": chassisFanTrayInfoState,
       "chassisFanInfoTable": chassisFanInfoTable,
       "chassisFanInfoEntry": chassisFanInfoEntry,
       "chassisFanIndex": chassisFanIndex,
       "chassisFanStatus": chassisFanStatus,
       "chassisFanSpeed": chassisFanSpeed,
       "chassisSlotInfo": chassisSlotInfo,
       "chassisSlotInfoTable": chassisSlotInfoTable,
       "chassisSlotInfoEntry": chassisSlotInfoEntry,
       "chassisSlotIndex": chassisSlotIndex,
       "chassisSlotState": chassisSlotState,
       "chassisSlotLEDPoEModeEnabled": chassisSlotLEDPoEModeEnabled,
       "chassisSlotModel": chassisSlotModel,
       "chassisSlotSerialNumber": chassisSlotSerialNumber,
       "chassisSlotHwVersion": chassisSlotHwVersion,
       "chassisSlotPCBAVersion": chassisSlotPCBAVersion,
       "chassisSlotBootloaderVersion": chassisSlotBootloaderVersion,
       "chassisSlotRuntimeVersion": chassisSlotRuntimeVersion,
       "chassisSlotCPLDVersion": chassisSlotCPLDVersion,
       "chassisSlotFirsMacAddress": chassisSlotFirsMacAddress,
       "chassisSlotNumberOfMacAddress": chassisSlotNumberOfMacAddress,
       "chassisTemperatureInfo": chassisTemperatureInfo,
       "chassisTemperatureInfoTable": chassisTemperatureInfoTable,
       "chassisTemperatureInfoEntry": chassisTemperatureInfoEntry,
       "chassisTemperatureSlotIndex": chassisTemperatureSlotIndex,
       "chassisTemperatureInletCurrent": chassisTemperatureInletCurrent,
       "chassisTemperatureInletOverheat": chassisTemperatureInletOverheat,
       "chassisTemperatureInletHeatdown": chassisTemperatureInletHeatdown,
       "chassisTemperatureCenterCurrent": chassisTemperatureCenterCurrent,
       "chassisTemperatureCenterOverheat": chassisTemperatureCenterOverheat,
       "chassisTemperatureCenterHeatdown": chassisTemperatureCenterHeatdown,
       "chassisTemperatureOutletCurrent": chassisTemperatureOutletCurrent,
       "chassisTemperatureOutletOverheat": chassisTemperatureOutletOverheat,
       "chassisTemperatureOutletHeatdown": chassisTemperatureOutletHeatdown,
       "chassisPortLEDInfo": chassisPortLEDInfo,
       "chassisPortLEDInfoTable": chassisPortLEDInfoTable,
       "chassisPortLEDInfoEntry": chassisPortLEDInfoEntry,
       "chassisPortLEDIFIndex": chassisPortLEDIFIndex,
       "chassisPortLEDIFName": chassisPortLEDIFName,
       "chassisPortLEDStatus": chassisPortLEDStatus,
       "chassisPortLEDMode": chassisPortLEDMode,
       "chassisPortLEDMediumType": chassisPortLEDMediumType}
)

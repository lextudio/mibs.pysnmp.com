# SNMP MIB module (OPLINK-BTI-OPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Oplink-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:56 2024
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

(mngdproducts,) = mibBuilder.importSymbols(
    "Oplink-MIB",
    "mngdproducts")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

deviceOPSMv2_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7)
)
deviceOPSMv2_MIB.setRevisions(
        ("2013-04-02 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HeTenthdB(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class HeTenthdBm(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class HeTenthmA(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class HeTenthmV(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class HeTenthCentigrade(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


# MIB Managed Objects in the order of their OIDs

_Version2_ObjectIdentity = ObjectIdentity
version2 = _Version2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1)
)
_EmuTable_Object = MibTable
emuTable = _EmuTable_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    emuTable.setStatus("current")
_EmuEntry_Object = MibTableRow
emuEntry = _EmuEntry_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1)
)
emuEntry.setIndexNames(
    (0, "OPLINK-BTI-OPS-MIB", "emuChassisId"),
    (0, "OPLINK-BTI-OPS-MIB", "emuSlotId"),
    (0, "OPLINK-BTI-OPS-MIB", "emuItemId"),
)
if mibBuilder.loadTexts:
    emuEntry.setStatus("current")
_EmuMfgName_Type = DisplayString
_EmuMfgName_Object = MibTableColumn
emuMfgName = _EmuMfgName_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 1),
    _EmuMfgName_Type()
)
emuMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuMfgName.setStatus("current")
_EmuModuleType_Type = DisplayString
_EmuModuleType_Object = MibTableColumn
emuModuleType = _EmuModuleType_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 2),
    _EmuModuleType_Type()
)
emuModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuModuleType.setStatus("current")
_EmuPartNum_Type = DisplayString
_EmuPartNum_Object = MibTableColumn
emuPartNum = _EmuPartNum_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 3),
    _EmuPartNum_Type()
)
emuPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuPartNum.setStatus("current")


class _EmuSerialNum_Type(DisplayString):
    """Custom type emuSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EmuSerialNum_Type.__name__ = "DisplayString"
_EmuSerialNum_Object = MibTableColumn
emuSerialNum = _EmuSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 4),
    _EmuSerialNum_Type()
)
emuSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuSerialNum.setStatus("current")
_EmuMfgDate_Type = DisplayString
_EmuMfgDate_Object = MibTableColumn
emuMfgDate = _EmuMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 5),
    _EmuMfgDate_Type()
)
emuMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuMfgDate.setStatus("current")
_EmuCaliDate_Type = DisplayString
_EmuCaliDate_Object = MibTableColumn
emuCaliDate = _EmuCaliDate_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 6),
    _EmuCaliDate_Type()
)
emuCaliDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuCaliDate.setStatus("current")
_EmuFirmwareVer_Type = DisplayString
_EmuFirmwareVer_Object = MibTableColumn
emuFirmwareVer = _EmuFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 7),
    _EmuFirmwareVer_Type()
)
emuFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuFirmwareVer.setStatus("current")
_EmuHardwareVer_Type = DisplayString
_EmuHardwareVer_Object = MibTableColumn
emuHardwareVer = _EmuHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 8),
    _EmuHardwareVer_Type()
)
emuHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuHardwareVer.setStatus("current")
_EmuVendorID_Type = DisplayString
_EmuVendorID_Object = MibTableColumn
emuVendorID = _EmuVendorID_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 9),
    _EmuVendorID_Type()
)
emuVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuVendorID.setStatus("current")


class _EmuSysDate_Type(DisplayString):
    """Custom type emuSysDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_EmuSysDate_Type.__name__ = "DisplayString"
_EmuSysDate_Object = MibTableColumn
emuSysDate = _EmuSysDate_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 10),
    _EmuSysDate_Type()
)
emuSysDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuSysDate.setStatus("current")


class _EmuSysTime_Type(DisplayString):
    """Custom type emuSysTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_EmuSysTime_Type.__name__ = "DisplayString"
_EmuSysTime_Object = MibTableColumn
emuSysTime = _EmuSysTime_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 11),
    _EmuSysTime_Type()
)
emuSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuSysTime.setStatus("current")


class _EmuIpAddr_Type(DisplayString):
    """Custom type emuIpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 15),
    )


_EmuIpAddr_Type.__name__ = "DisplayString"
_EmuIpAddr_Object = MibTableColumn
emuIpAddr = _EmuIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 12),
    _EmuIpAddr_Type()
)
emuIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuIpAddr.setStatus("current")


class _EmuNetMask_Type(DisplayString):
    """Custom type emuNetMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 15),
    )


_EmuNetMask_Type.__name__ = "DisplayString"
_EmuNetMask_Object = MibTableColumn
emuNetMask = _EmuNetMask_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 13),
    _EmuNetMask_Type()
)
emuNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuNetMask.setStatus("current")


class _EmuGateway_Type(DisplayString):
    """Custom type emuGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 15),
    )


_EmuGateway_Type.__name__ = "DisplayString"
_EmuGateway_Object = MibTableColumn
emuGateway = _EmuGateway_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 14),
    _EmuGateway_Type()
)
emuGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuGateway.setStatus("current")


class _EmuMacAddr_Type(DisplayString):
    """Custom type emuMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_EmuMacAddr_Type.__name__ = "DisplayString"
_EmuMacAddr_Object = MibTableColumn
emuMacAddr = _EmuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 15),
    _EmuMacAddr_Type()
)
emuMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuMacAddr.setStatus("current")
_EmuUptime_Type = Integer32
_EmuUptime_Object = MibTableColumn
emuUptime = _EmuUptime_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 16),
    _EmuUptime_Type()
)
emuUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuUptime.setStatus("current")
_EmuBoardTemp_Type = HeTenthCentigrade
_EmuBoardTemp_Object = MibTableColumn
emuBoardTemp = _EmuBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 17),
    _EmuBoardTemp_Type()
)
emuBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuBoardTemp.setStatus("current")
_EmuHighTemperatureThreshold_Type = HeTenthCentigrade
_EmuHighTemperatureThreshold_Object = MibTableColumn
emuHighTemperatureThreshold = _EmuHighTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 18),
    _EmuHighTemperatureThreshold_Type()
)
emuHighTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuHighTemperatureThreshold.setStatus("current")
_EmuLowTemperatureThreshold_Type = HeTenthCentigrade
_EmuLowTemperatureThreshold_Object = MibTableColumn
emuLowTemperatureThreshold = _EmuLowTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 19),
    _EmuLowTemperatureThreshold_Type()
)
emuLowTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuLowTemperatureThreshold.setStatus("current")
_EmuGetModConfig_Type = DisplayString
_EmuGetModConfig_Object = MibTableColumn
emuGetModConfig = _EmuGetModConfig_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 20),
    _EmuGetModConfig_Type()
)
emuGetModConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuGetModConfig.setStatus("current")


class _EmuDelModConfig_Type(DisplayString):
    """Custom type emuDelModConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EmuDelModConfig_Type.__name__ = "DisplayString"
_EmuDelModConfig_Object = MibTableColumn
emuDelModConfig = _EmuDelModConfig_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 21),
    _EmuDelModConfig_Type()
)
emuDelModConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuDelModConfig.setStatus("current")


class _EmuAddModConfig_Type(DisplayString):
    """Custom type emuAddModConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EmuAddModConfig_Type.__name__ = "DisplayString"
_EmuAddModConfig_Object = MibTableColumn
emuAddModConfig = _EmuAddModConfig_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 22),
    _EmuAddModConfig_Type()
)
emuAddModConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuAddModConfig.setStatus("current")


class _EmuSaveConfig_Type(DisplayString):
    """Custom type emuSaveConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
    )


_EmuSaveConfig_Type.__name__ = "DisplayString"
_EmuSaveConfig_Object = MibTableColumn
emuSaveConfig = _EmuSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 23),
    _EmuSaveConfig_Type()
)
emuSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuSaveConfig.setStatus("current")


class _EmuRestoreDefault_Type(DisplayString):
    """Custom type emuRestoreDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
    )


_EmuRestoreDefault_Type.__name__ = "DisplayString"
_EmuRestoreDefault_Object = MibTableColumn
emuRestoreDefault = _EmuRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 24),
    _EmuRestoreDefault_Type()
)
emuRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuRestoreDefault.setStatus("current")


class _EmuReset_Type(DisplayString):
    """Custom type emuReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
    )


_EmuReset_Type.__name__ = "DisplayString"
_EmuReset_Object = MibTableColumn
emuReset = _EmuReset_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 25),
    _EmuReset_Type()
)
emuReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuReset.setStatus("current")


class _EmuFirmwareUpgradeStart_Type(DisplayString):
    """Custom type emuFirmwareUpgradeStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_EmuFirmwareUpgradeStart_Type.__name__ = "DisplayString"
_EmuFirmwareUpgradeStart_Object = MibTableColumn
emuFirmwareUpgradeStart = _EmuFirmwareUpgradeStart_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 40),
    _EmuFirmwareUpgradeStart_Type()
)
emuFirmwareUpgradeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuFirmwareUpgradeStart.setStatus("current")
_EmuFirmwareUpgradeStatus_Type = DisplayString
_EmuFirmwareUpgradeStatus_Object = MibTableColumn
emuFirmwareUpgradeStatus = _EmuFirmwareUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 41),
    _EmuFirmwareUpgradeStatus_Type()
)
emuFirmwareUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuFirmwareUpgradeStatus.setStatus("current")


class _EmuGetSNMPConfig_Type(OctetString):
    """Custom type emuGetSNMPConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1200),
    )


_EmuGetSNMPConfig_Type.__name__ = "OctetString"
_EmuGetSNMPConfig_Object = MibTableColumn
emuGetSNMPConfig = _EmuGetSNMPConfig_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 50),
    _EmuGetSNMPConfig_Type()
)
emuGetSNMPConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuGetSNMPConfig.setStatus("current")


class _EmuDelSNMPConfig_Type(OctetString):
    """Custom type emuDelSNMPConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EmuDelSNMPConfig_Type.__name__ = "OctetString"
_EmuDelSNMPConfig_Object = MibTableColumn
emuDelSNMPConfig = _EmuDelSNMPConfig_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 51),
    _EmuDelSNMPConfig_Type()
)
emuDelSNMPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuDelSNMPConfig.setStatus("current")


class _EmuAddSNMPConfig_Type(OctetString):
    """Custom type emuAddSNMPConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_EmuAddSNMPConfig_Type.__name__ = "OctetString"
_EmuAddSNMPConfig_Object = MibTableColumn
emuAddSNMPConfig = _EmuAddSNMPConfig_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 52),
    _EmuAddSNMPConfig_Type()
)
emuAddSNMPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emuAddSNMPConfig.setStatus("current")
_EmuGetCurrentAlarm_Type = OctetString
_EmuGetCurrentAlarm_Object = MibTableColumn
emuGetCurrentAlarm = _EmuGetCurrentAlarm_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 60),
    _EmuGetCurrentAlarm_Type()
)
emuGetCurrentAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuGetCurrentAlarm.setStatus("current")


class _EmuGetHisAlarm_Type(DisplayString):
    """Custom type emuGetHisAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_EmuGetHisAlarm_Type.__name__ = "DisplayString"
_EmuGetHisAlarm_Object = MibTableColumn
emuGetHisAlarm = _EmuGetHisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 61),
    _EmuGetHisAlarm_Type()
)
emuGetHisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emuGetHisAlarm.setStatus("current")


class _EmuChassisId_Type(Integer32):
    """Custom type emuChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_EmuChassisId_Type.__name__ = "Integer32"
_EmuChassisId_Object = MibTableColumn
emuChassisId = _EmuChassisId_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 1001),
    _EmuChassisId_Type()
)
emuChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    emuChassisId.setStatus("current")


class _EmuSlotId_Type(Integer32):
    """Custom type emuSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_EmuSlotId_Type.__name__ = "Integer32"
_EmuSlotId_Object = MibTableColumn
emuSlotId = _EmuSlotId_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 1002),
    _EmuSlotId_Type()
)
emuSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    emuSlotId.setStatus("current")


class _EmuItemId_Type(Integer32):
    """Custom type emuItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_EmuItemId_Type.__name__ = "Integer32"
_EmuItemId_Object = MibTableColumn
emuItemId = _EmuItemId_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1, 1, 1003),
    _EmuItemId_Type()
)
emuItemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    emuItemId.setStatus("current")
_OpsmTable_Object = MibTable
opsmTable = _OpsmTable_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    opsmTable.setStatus("current")
_OpsmEntry_Object = MibTableRow
opsmEntry = _OpsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1)
)
opsmEntry.setIndexNames(
    (0, "OPLINK-BTI-OPS-MIB", "opsmChassisId"),
    (0, "OPLINK-BTI-OPS-MIB", "opsmSlotId"),
    (0, "OPLINK-BTI-OPS-MIB", "opsmItemId"),
)
if mibBuilder.loadTexts:
    opsmEntry.setStatus("current")
_OpsmMfgName_Type = DisplayString
_OpsmMfgName_Object = MibTableColumn
opsmMfgName = _OpsmMfgName_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 1),
    _OpsmMfgName_Type()
)
opsmMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmMfgName.setStatus("current")
_OpsmPartNum_Type = DisplayString
_OpsmPartNum_Object = MibTableColumn
opsmPartNum = _OpsmPartNum_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 2),
    _OpsmPartNum_Type()
)
opsmPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmPartNum.setStatus("current")
_OpsmSerialNum_Type = DisplayString
_OpsmSerialNum_Object = MibTableColumn
opsmSerialNum = _OpsmSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 3),
    _OpsmSerialNum_Type()
)
opsmSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmSerialNum.setStatus("current")
_OpsmMfgDate_Type = DisplayString
_OpsmMfgDate_Object = MibTableColumn
opsmMfgDate = _OpsmMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 4),
    _OpsmMfgDate_Type()
)
opsmMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmMfgDate.setStatus("current")
_OpsmCaliDate_Type = DisplayString
_OpsmCaliDate_Object = MibTableColumn
opsmCaliDate = _OpsmCaliDate_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 5),
    _OpsmCaliDate_Type()
)
opsmCaliDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmCaliDate.setStatus("current")
_OpsmHardwareVer_Type = DisplayString
_OpsmHardwareVer_Object = MibTableColumn
opsmHardwareVer = _OpsmHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 6),
    _OpsmHardwareVer_Type()
)
opsmHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmHardwareVer.setStatus("current")
_OpsmVendorID_Type = DisplayString
_OpsmVendorID_Object = MibTableColumn
opsmVendorID = _OpsmVendorID_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 7),
    _OpsmVendorID_Type()
)
opsmVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmVendorID.setStatus("current")
_OpsmModuleType_Type = DisplayString
_OpsmModuleType_Object = MibTableColumn
opsmModuleType = _OpsmModuleType_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 8),
    _OpsmModuleType_Type()
)
opsmModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmModuleType.setStatus("current")
_OpsmFirmwareVer_Type = DisplayString
_OpsmFirmwareVer_Object = MibTableColumn
opsmFirmwareVer = _OpsmFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 9),
    _OpsmFirmwareVer_Type()
)
opsmFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmFirmwareVer.setStatus("current")
_OpsmReset_Type = Integer32
_OpsmReset_Object = MibTableColumn
opsmReset = _OpsmReset_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 10),
    _OpsmReset_Type()
)
opsmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmReset.setStatus("current")
_OpsmProtectionMode_Type = Integer32
_OpsmProtectionMode_Object = MibTableColumn
opsmProtectionMode = _OpsmProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 20),
    _OpsmProtectionMode_Type()
)
opsmProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmProtectionMode.setStatus("current")
_OpsmRevertiveSetting_Type = Integer32
_OpsmRevertiveSetting_Object = MibTableColumn
opsmRevertiveSetting = _OpsmRevertiveSetting_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 21),
    _OpsmRevertiveSetting_Type()
)
opsmRevertiveSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmRevertiveSetting.setStatus("current")
_OpsmDiffSwitchSetting_Type = Integer32
_OpsmDiffSwitchSetting_Object = MibTableColumn
opsmDiffSwitchSetting = _OpsmDiffSwitchSetting_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 22),
    _OpsmDiffSwitchSetting_Type()
)
opsmDiffSwitchSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmDiffSwitchSetting.setStatus("current")
_OpsmDiffAlarmThreshold_Type = HeTenthdBm
_OpsmDiffAlarmThreshold_Object = MibTableColumn
opsmDiffAlarmThreshold = _OpsmDiffAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 23),
    _OpsmDiffAlarmThreshold_Type()
)
opsmDiffAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmDiffAlarmThreshold.setStatus("current")
_OpsmDiffSwitchThreshold_Type = HeTenthdBm
_OpsmDiffSwitchThreshold_Object = MibTableColumn
opsmDiffSwitchThreshold = _OpsmDiffSwitchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 24),
    _OpsmDiffSwitchThreshold_Type()
)
opsmDiffSwitchThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmDiffSwitchThreshold.setStatus("current")
_OpsmInherentDiffOffset_Type = HeTenthdBm
_OpsmInherentDiffOffset_Object = MibTableColumn
opsmInherentDiffOffset = _OpsmInherentDiffOffset_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 25),
    _OpsmInherentDiffOffset_Type()
)
opsmInherentDiffOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmInherentDiffOffset.setStatus("current")
_OpsmWTRTime_Type = Integer32
_OpsmWTRTime_Object = MibTableColumn
opsmWTRTime = _OpsmWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 26),
    _OpsmWTRTime_Type()
)
opsmWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmWTRTime.setStatus("current")
_OpsmSwitchStatus_Type = Integer32
_OpsmSwitchStatus_Object = MibTableColumn
opsmSwitchStatus = _OpsmSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 27),
    _OpsmSwitchStatus_Type()
)
opsmSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmSwitchStatus.setStatus("current")
_OpsmSwitchPosition_Type = Integer32
_OpsmSwitchPosition_Object = MibTableColumn
opsmSwitchPosition = _OpsmSwitchPosition_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 28),
    _OpsmSwitchPosition_Type()
)
opsmSwitchPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmSwitchPosition.setStatus("current")
_OpsmInputLosAlarmThrPathP_Type = HeTenthdBm
_OpsmInputLosAlarmThrPathP_Object = MibTableColumn
opsmInputLosAlarmThrPathP = _OpsmInputLosAlarmThrPathP_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 40),
    _OpsmInputLosAlarmThrPathP_Type()
)
opsmInputLosAlarmThrPathP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmInputLosAlarmThrPathP.setStatus("current")
_OpsmInputLosAlarmThrPathS_Type = HeTenthdBm
_OpsmInputLosAlarmThrPathS_Object = MibTableColumn
opsmInputLosAlarmThrPathS = _OpsmInputLosAlarmThrPathS_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 41),
    _OpsmInputLosAlarmThrPathS_Type()
)
opsmInputLosAlarmThrPathS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmInputLosAlarmThrPathS.setStatus("current")
_OpsmInputLosAlarmHys_Type = HeTenthdBm
_OpsmInputLosAlarmHys_Object = MibTableColumn
opsmInputLosAlarmHys = _OpsmInputLosAlarmHys_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 42),
    _OpsmInputLosAlarmHys_Type()
)
opsmInputLosAlarmHys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opsmInputLosAlarmHys.setStatus("current")
_OpsmInputPowerPathP_Type = Integer32
_OpsmInputPowerPathP_Object = MibTableColumn
opsmInputPowerPathP = _OpsmInputPowerPathP_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 43),
    _OpsmInputPowerPathP_Type()
)
opsmInputPowerPathP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmInputPowerPathP.setStatus("current")
_OpsmInputPowerPathS_Type = Integer32
_OpsmInputPowerPathS_Object = MibTableColumn
opsmInputPowerPathS = _OpsmInputPowerPathS_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 44),
    _OpsmInputPowerPathS_Type()
)
opsmInputPowerPathS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmInputPowerPathS.setStatus("current")
_OpsmSwitchCount_Type = Integer32
_OpsmSwitchCount_Object = MibTableColumn
opsmSwitchCount = _OpsmSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 45),
    _OpsmSwitchCount_Type()
)
opsmSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmSwitchCount.setStatus("current")


class _OpsmChassisId_Type(Integer32):
    """Custom type opsmChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_OpsmChassisId_Type.__name__ = "Integer32"
_OpsmChassisId_Object = MibTableColumn
opsmChassisId = _OpsmChassisId_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 1001),
    _OpsmChassisId_Type()
)
opsmChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opsmChassisId.setStatus("current")


class _OpsmSlotId_Type(Integer32):
    """Custom type opsmSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_OpsmSlotId_Type.__name__ = "Integer32"
_OpsmSlotId_Object = MibTableColumn
opsmSlotId = _OpsmSlotId_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 1002),
    _OpsmSlotId_Type()
)
opsmSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opsmSlotId.setStatus("current")


class _OpsmItemId_Type(Integer32):
    """Custom type opsmItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_OpsmItemId_Type.__name__ = "Integer32"
_OpsmItemId_Object = MibTableColumn
opsmItemId = _OpsmItemId_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 2, 1, 1003),
    _OpsmItemId_Type()
)
opsmItemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opsmItemId.setStatus("current")
_OplkV6Traps_ObjectIdentity = ObjectIdentity
oplkV6Traps = _OplkV6Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001)
)
_OplkemuNotifications_ObjectIdentity = ObjectIdentity
oplkemuNotifications = _OplkemuNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1)
)
_OplkemuNotificationPrefix_ObjectIdentity = ObjectIdentity
oplkemuNotificationPrefix = _OplkemuNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0)
)
_OplkopsmNotifications_ObjectIdentity = ObjectIdentity
oplkopsmNotifications = _OplkopsmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2)
)
_OplkopsmNotificationPrefix_ObjectIdentity = ObjectIdentity
oplkopsmNotificationPrefix = _OplkopsmNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0)
)
_OplinkTrapCode_Type = DisplayString
_OplinkTrapCode_Object = MibScalar
oplinkTrapCode = _OplinkTrapCode_Object(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1002),
    _OplinkTrapCode_Type()
)
oplinkTrapCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oplinkTrapCode.setStatus("current")

# Managed Objects groups


# Notification objects

oplinkemuTemperatureAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 1)
)
oplinkemuTemperatureAbnormal.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuTemperatureAbnormal.setStatus(
        "current"
    )

oplinkemuTemperatureResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 2)
)
oplinkemuTemperatureResume.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuTemperatureResume.setStatus(
        "current"
    )

oplinkemuFanRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 3)
)
oplinkemuFanRemove.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuFanRemove.setStatus(
        "current"
    )

oplinkemuFanInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 4)
)
oplinkemuFanInsert.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuFanInsert.setStatus(
        "current"
    )

oplinkemuPowerRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 5)
)
oplinkemuPowerRemove.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuPowerRemove.setStatus(
        "current"
    )

oplinkemuPowerInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 6)
)
oplinkemuPowerInsert.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuPowerInsert.setStatus(
        "current"
    )

oplinkemuVoltageAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 7)
)
oplinkemuVoltageAbnormal.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuVoltageAbnormal.setStatus(
        "current"
    )

oplinkemuVoltageResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 8)
)
oplinkemuVoltageResume.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuVoltageResume.setStatus(
        "current"
    )

oplinkemuSubCardDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 9)
)
oplinkemuSubCardDelete.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuSubCardDelete.setStatus(
        "current"
    )

oplinkemuSubCardAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 10)
)
oplinkemuSubCardAdd.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuSubCardAdd.setStatus(
        "current"
    )

oplinkemuSubCardUnmatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 11)
)
oplinkemuSubCardUnmatch.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuSubCardUnmatch.setStatus(
        "current"
    )

oplinkemuSubCardMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 1, 0, 12)
)
oplinkemuSubCardMatch.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkemuSubCardMatch.setStatus(
        "current"
    )

oplinkopsmInputLosRPI1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 1)
)
oplinkopsmInputLosRPI1.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmInputLosRPI1.setStatus(
        "current"
    )

oplinkopsmInputLosResumeRPI1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 2)
)
oplinkopsmInputLosResumeRPI1.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmInputLosResumeRPI1.setStatus(
        "current"
    )

oplinkopsmInputLosRSI1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 3)
)
oplinkopsmInputLosRSI1.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmInputLosRSI1.setStatus(
        "current"
    )

oplinkopsmInputLosResumeRSI1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 4)
)
oplinkopsmInputLosResumeRSI1.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmInputLosResumeRSI1.setStatus(
        "current"
    )

oplinkopsmInputLosRPI2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 5)
)
oplinkopsmInputLosRPI2.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmInputLosRPI2.setStatus(
        "current"
    )

oplinkopsmInputLosResumeRPI2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 6)
)
oplinkopsmInputLosResumeRPI2.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmInputLosResumeRPI2.setStatus(
        "current"
    )

oplinkopsmInputLosRSI2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 7)
)
oplinkopsmInputLosRSI2.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmInputLosRSI2.setStatus(
        "current"
    )

oplinkopsmInputLosResumeRSI2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 8)
)
oplinkopsmInputLosResumeRSI2.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmInputLosResumeRSI2.setStatus(
        "current"
    )

oplinkopsmPowerDiffChannel1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 9)
)
oplinkopsmPowerDiffChannel1.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmPowerDiffChannel1.setStatus(
        "current"
    )

oplinkopsmPowerDiffResumeChannel1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 10)
)
oplinkopsmPowerDiffResumeChannel1.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmPowerDiffResumeChannel1.setStatus(
        "current"
    )

oplinkopsmPowerDiffChannel2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 11)
)
oplinkopsmPowerDiffChannel2.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmPowerDiffChannel2.setStatus(
        "current"
    )

oplinkopsmPowerDiffResumeChannel2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 12)
)
oplinkopsmPowerDiffResumeChannel2.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmPowerDiffResumeChannel2.setStatus(
        "current"
    )

oplinkopsmSwitchFailChannel1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 13)
)
oplinkopsmSwitchFailChannel1.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmSwitchFailChannel1.setStatus(
        "current"
    )

oplinkopsmSwitchSuccessChannel1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 14)
)
oplinkopsmSwitchSuccessChannel1.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmSwitchSuccessChannel1.setStatus(
        "current"
    )

oplinkopsmSwitchFailChannel2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 15)
)
oplinkopsmSwitchFailChannel2.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmSwitchFailChannel2.setStatus(
        "current"
    )

oplinkopsmSwitchSuccessChannel2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19547, 1, 7, 1, 1001, 2, 0, 16)
)
oplinkopsmSwitchSuccessChannel2.setObjects(
    ("OPLINK-BTI-OPS-MIB", "oplinkTrapCode")
)
if mibBuilder.loadTexts:
    oplinkopsmSwitchSuccessChannel2.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPLINK-BTI-OPS-MIB",
    **{"HeTenthdB": HeTenthdB,
       "HeTenthdBm": HeTenthdBm,
       "HeTenthmA": HeTenthmA,
       "HeTenthmV": HeTenthmV,
       "HeTenthCentigrade": HeTenthCentigrade,
       "deviceOPSMv2-MIB": deviceOPSMv2_MIB,
       "version2": version2,
       "emuTable": emuTable,
       "emuEntry": emuEntry,
       "emuMfgName": emuMfgName,
       "emuModuleType": emuModuleType,
       "emuPartNum": emuPartNum,
       "emuSerialNum": emuSerialNum,
       "emuMfgDate": emuMfgDate,
       "emuCaliDate": emuCaliDate,
       "emuFirmwareVer": emuFirmwareVer,
       "emuHardwareVer": emuHardwareVer,
       "emuVendorID": emuVendorID,
       "emuSysDate": emuSysDate,
       "emuSysTime": emuSysTime,
       "emuIpAddr": emuIpAddr,
       "emuNetMask": emuNetMask,
       "emuGateway": emuGateway,
       "emuMacAddr": emuMacAddr,
       "emuUptime": emuUptime,
       "emuBoardTemp": emuBoardTemp,
       "emuHighTemperatureThreshold": emuHighTemperatureThreshold,
       "emuLowTemperatureThreshold": emuLowTemperatureThreshold,
       "emuGetModConfig": emuGetModConfig,
       "emuDelModConfig": emuDelModConfig,
       "emuAddModConfig": emuAddModConfig,
       "emuSaveConfig": emuSaveConfig,
       "emuRestoreDefault": emuRestoreDefault,
       "emuReset": emuReset,
       "emuFirmwareUpgradeStart": emuFirmwareUpgradeStart,
       "emuFirmwareUpgradeStatus": emuFirmwareUpgradeStatus,
       "emuGetSNMPConfig": emuGetSNMPConfig,
       "emuDelSNMPConfig": emuDelSNMPConfig,
       "emuAddSNMPConfig": emuAddSNMPConfig,
       "emuGetCurrentAlarm": emuGetCurrentAlarm,
       "emuGetHisAlarm": emuGetHisAlarm,
       "emuChassisId": emuChassisId,
       "emuSlotId": emuSlotId,
       "emuItemId": emuItemId,
       "opsmTable": opsmTable,
       "opsmEntry": opsmEntry,
       "opsmMfgName": opsmMfgName,
       "opsmPartNum": opsmPartNum,
       "opsmSerialNum": opsmSerialNum,
       "opsmMfgDate": opsmMfgDate,
       "opsmCaliDate": opsmCaliDate,
       "opsmHardwareVer": opsmHardwareVer,
       "opsmVendorID": opsmVendorID,
       "opsmModuleType": opsmModuleType,
       "opsmFirmwareVer": opsmFirmwareVer,
       "opsmReset": opsmReset,
       "opsmProtectionMode": opsmProtectionMode,
       "opsmRevertiveSetting": opsmRevertiveSetting,
       "opsmDiffSwitchSetting": opsmDiffSwitchSetting,
       "opsmDiffAlarmThreshold": opsmDiffAlarmThreshold,
       "opsmDiffSwitchThreshold": opsmDiffSwitchThreshold,
       "opsmInherentDiffOffset": opsmInherentDiffOffset,
       "opsmWTRTime": opsmWTRTime,
       "opsmSwitchStatus": opsmSwitchStatus,
       "opsmSwitchPosition": opsmSwitchPosition,
       "opsmInputLosAlarmThrPathP": opsmInputLosAlarmThrPathP,
       "opsmInputLosAlarmThrPathS": opsmInputLosAlarmThrPathS,
       "opsmInputLosAlarmHys": opsmInputLosAlarmHys,
       "opsmInputPowerPathP": opsmInputPowerPathP,
       "opsmInputPowerPathS": opsmInputPowerPathS,
       "opsmSwitchCount": opsmSwitchCount,
       "opsmChassisId": opsmChassisId,
       "opsmSlotId": opsmSlotId,
       "opsmItemId": opsmItemId,
       "oplkV6Traps": oplkV6Traps,
       "oplkemuNotifications": oplkemuNotifications,
       "oplkemuNotificationPrefix": oplkemuNotificationPrefix,
       "oplinkemuTemperatureAbnormal": oplinkemuTemperatureAbnormal,
       "oplinkemuTemperatureResume": oplinkemuTemperatureResume,
       "oplinkemuFanRemove": oplinkemuFanRemove,
       "oplinkemuFanInsert": oplinkemuFanInsert,
       "oplinkemuPowerRemove": oplinkemuPowerRemove,
       "oplinkemuPowerInsert": oplinkemuPowerInsert,
       "oplinkemuVoltageAbnormal": oplinkemuVoltageAbnormal,
       "oplinkemuVoltageResume": oplinkemuVoltageResume,
       "oplinkemuSubCardDelete": oplinkemuSubCardDelete,
       "oplinkemuSubCardAdd": oplinkemuSubCardAdd,
       "oplinkemuSubCardUnmatch": oplinkemuSubCardUnmatch,
       "oplinkemuSubCardMatch": oplinkemuSubCardMatch,
       "oplkopsmNotifications": oplkopsmNotifications,
       "oplkopsmNotificationPrefix": oplkopsmNotificationPrefix,
       "oplinkopsmInputLosRPI1": oplinkopsmInputLosRPI1,
       "oplinkopsmInputLosResumeRPI1": oplinkopsmInputLosResumeRPI1,
       "oplinkopsmInputLosRSI1": oplinkopsmInputLosRSI1,
       "oplinkopsmInputLosResumeRSI1": oplinkopsmInputLosResumeRSI1,
       "oplinkopsmInputLosRPI2": oplinkopsmInputLosRPI2,
       "oplinkopsmInputLosResumeRPI2": oplinkopsmInputLosResumeRPI2,
       "oplinkopsmInputLosRSI2": oplinkopsmInputLosRSI2,
       "oplinkopsmInputLosResumeRSI2": oplinkopsmInputLosResumeRSI2,
       "oplinkopsmPowerDiffChannel1": oplinkopsmPowerDiffChannel1,
       "oplinkopsmPowerDiffResumeChannel1": oplinkopsmPowerDiffResumeChannel1,
       "oplinkopsmPowerDiffChannel2": oplinkopsmPowerDiffChannel2,
       "oplinkopsmPowerDiffResumeChannel2": oplinkopsmPowerDiffResumeChannel2,
       "oplinkopsmSwitchFailChannel1": oplinkopsmSwitchFailChannel1,
       "oplinkopsmSwitchSuccessChannel1": oplinkopsmSwitchSuccessChannel1,
       "oplinkopsmSwitchFailChannel2": oplinkopsmSwitchFailChannel2,
       "oplinkopsmSwitchSuccessChannel2": oplinkopsmSwitchSuccessChannel2,
       "oplinkTrapCode": oplinkTrapCode}
)

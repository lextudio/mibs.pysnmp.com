# SNMP MIB module (EtherWAN-sw72000) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EtherWAN-sw72000
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:13 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lanSwitch = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1)
)
lanSwitch.setRevisions(
        ("2009-02-18 00:00",
         "2008-12-30 00:00",
         "2006-10-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Etherwan_ObjectIdentity = ObjectIdentity
etherwan = _Etherwan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736)
)
_Sw72000_ObjectIdentity = ObjectIdentity
sw72000 = _Sw72000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1)
)
_EwnSystem_ObjectIdentity = ObjectIdentity
ewnSystem = _EwnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1)
)


class _EwnSystemFirmwareRev_Type(DisplayString):
    """Custom type ewnSystemFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EwnSystemFirmwareRev_Type.__name__ = "DisplayString"
_EwnSystemFirmwareRev_Object = MibScalar
ewnSystemFirmwareRev = _EwnSystemFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 1),
    _EwnSystemFirmwareRev_Type()
)
ewnSystemFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnSystemFirmwareRev.setStatus("current")


class _EwnSystemConfigOperation_Type(Integer32):
    """Custom type ewnSystemConfigOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadDefault", 1),
          ("none", 0),
          ("saveCurrent", 2))
    )


_EwnSystemConfigOperation_Type.__name__ = "Integer32"
_EwnSystemConfigOperation_Object = MibScalar
ewnSystemConfigOperation = _EwnSystemConfigOperation_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 2),
    _EwnSystemConfigOperation_Type()
)
ewnSystemConfigOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSystemConfigOperation.setStatus("current")


class _EwnSystemReboot_Type(Integer32):
    """Custom type ewnSystemReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnSystemReboot_Type.__name__ = "Integer32"
_EwnSystemReboot_Object = MibScalar
ewnSystemReboot = _EwnSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 3),
    _EwnSystemReboot_Type()
)
ewnSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSystemReboot.setStatus("current")


class _EwnSystemRebootRequired_Type(Integer32):
    """Custom type ewnSystemRebootRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rebootNotRequired", 0),
          ("rebootRequired", 1))
    )


_EwnSystemRebootRequired_Type.__name__ = "Integer32"
_EwnSystemRebootRequired_Object = MibScalar
ewnSystemRebootRequired = _EwnSystemRebootRequired_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 4),
    _EwnSystemRebootRequired_Type()
)
ewnSystemRebootRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnSystemRebootRequired.setStatus("current")
_EwnSystemTFTP_ObjectIdentity = ObjectIdentity
ewnSystemTFTP = _EwnSystemTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 5)
)


class _EwnSystemTFTPFilename_Type(DisplayString):
    """Custom type ewnSystemTFTPFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_EwnSystemTFTPFilename_Type.__name__ = "DisplayString"
_EwnSystemTFTPFilename_Object = MibScalar
ewnSystemTFTPFilename = _EwnSystemTFTPFilename_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 5, 1),
    _EwnSystemTFTPFilename_Type()
)
ewnSystemTFTPFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSystemTFTPFilename.setStatus("current")
_EwnSystemTFTPIpAddress_Type = IpAddress
_EwnSystemTFTPIpAddress_Object = MibScalar
ewnSystemTFTPIpAddress = _EwnSystemTFTPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 5, 2),
    _EwnSystemTFTPIpAddress_Type()
)
ewnSystemTFTPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSystemTFTPIpAddress.setStatus("current")


class _EwnSystemTFTPAction_Type(Integer32):
    """Custom type ewnSystemTFTPAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backupConfiguration", 2),
          ("installConfiguration", 1))
    )


_EwnSystemTFTPAction_Type.__name__ = "Integer32"
_EwnSystemTFTPAction_Object = MibScalar
ewnSystemTFTPAction = _EwnSystemTFTPAction_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 5, 3),
    _EwnSystemTFTPAction_Type()
)
ewnSystemTFTPAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSystemTFTPAction.setStatus("current")


class _EwnSystemTFTPState_Type(Integer32):
    """Custom type ewnSystemTFTPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("done", 3),
          ("error", 4),
          ("inProgress", 2),
          ("none", 0),
          ("start", 1))
    )


_EwnSystemTFTPState_Type.__name__ = "Integer32"
_EwnSystemTFTPState_Object = MibScalar
ewnSystemTFTPState = _EwnSystemTFTPState_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 5, 4),
    _EwnSystemTFTPState_Type()
)
ewnSystemTFTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSystemTFTPState.setStatus("current")


class _EwnSystemProductModel_Type(DisplayString):
    """Custom type ewnSystemProductModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EwnSystemProductModel_Type.__name__ = "DisplayString"
_EwnSystemProductModel_Object = MibScalar
ewnSystemProductModel = _EwnSystemProductModel_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 6),
    _EwnSystemProductModel_Type()
)
ewnSystemProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnSystemProductModel.setStatus("current")


class _EwnSystemHardwareRev_Type(DisplayString):
    """Custom type ewnSystemHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EwnSystemHardwareRev_Type.__name__ = "DisplayString"
_EwnSystemHardwareRev_Object = MibScalar
ewnSystemHardwareRev = _EwnSystemHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 7),
    _EwnSystemHardwareRev_Type()
)
ewnSystemHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnSystemHardwareRev.setStatus("current")
_EwnSystemGatewayIpAddress_Type = IpAddress
_EwnSystemGatewayIpAddress_Object = MibScalar
ewnSystemGatewayIpAddress = _EwnSystemGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 8),
    _EwnSystemGatewayIpAddress_Type()
)
ewnSystemGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSystemGatewayIpAddress.setStatus("current")
_EwnSystemMacAddr_Type = OctetString
_EwnSystemMacAddr_Object = MibScalar
ewnSystemMacAddr = _EwnSystemMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 9),
    _EwnSystemMacAddr_Type()
)
ewnSystemMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnSystemMacAddr.setStatus("current")


class _EwnSystemPassword_Type(DisplayString):
    """Custom type ewnSystemPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_EwnSystemPassword_Type.__name__ = "DisplayString"
_EwnSystemPassword_Object = MibScalar
ewnSystemPassword = _EwnSystemPassword_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 10),
    _EwnSystemPassword_Type()
)
ewnSystemPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSystemPassword.setStatus("current")


class _EwnSystemPasswordEncrypted_Type(DisplayString):
    """Custom type ewnSystemPasswordEncrypted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_EwnSystemPasswordEncrypted_Type.__name__ = "DisplayString"
_EwnSystemPasswordEncrypted_Object = MibScalar
ewnSystemPasswordEncrypted = _EwnSystemPasswordEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 11),
    _EwnSystemPasswordEncrypted_Type()
)
ewnSystemPasswordEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSystemPasswordEncrypted.setStatus("current")


class _EwnSystemAutoSaveState_Type(Integer32):
    """Custom type ewnSystemAutoSaveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnSystemAutoSaveState_Type.__name__ = "Integer32"
_EwnSystemAutoSaveState_Object = MibScalar
ewnSystemAutoSaveState = _EwnSystemAutoSaveState_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 12),
    _EwnSystemAutoSaveState_Type()
)
ewnSystemAutoSaveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSystemAutoSaveState.setStatus("current")


class _EwnSystemAutoSaveDelay_Type(Integer32):
    """Custom type ewnSystemAutoSaveDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_EwnSystemAutoSaveDelay_Type.__name__ = "Integer32"
_EwnSystemAutoSaveDelay_Object = MibScalar
ewnSystemAutoSaveDelay = _EwnSystemAutoSaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 1, 13),
    _EwnSystemAutoSaveDelay_Type()
)
ewnSystemAutoSaveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSystemAutoSaveDelay.setStatus("current")
_EwnPort_ObjectIdentity = ObjectIdentity
ewnPort = _EwnPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2)
)
_EwnPortCount_Type = Integer32
_EwnPortCount_Object = MibScalar
ewnPortCount = _EwnPortCount_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 1),
    _EwnPortCount_Type()
)
ewnPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnPortCount.setStatus("current")
_EwnPortTable_Object = MibTable
ewnPortTable = _EwnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ewnPortTable.setStatus("current")
_EwnPortEntry_Object = MibTableRow
ewnPortEntry = _EwnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1)
)
ewnPortEntry.setIndexNames(
    (0, "EtherWAN-sw72000", "ewnPortNo"),
)
if mibBuilder.loadTexts:
    ewnPortEntry.setStatus("current")


class _EwnPortNo_Type(Integer32):
    """Custom type ewnPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EwnPortNo_Type.__name__ = "Integer32"
_EwnPortNo_Object = MibTableColumn
ewnPortNo = _EwnPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 1),
    _EwnPortNo_Type()
)
ewnPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnPortNo.setStatus("current")


class _EwnPortString_Type(DisplayString):
    """Custom type ewnPortString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EwnPortString_Type.__name__ = "DisplayString"
_EwnPortString_Object = MibTableColumn
ewnPortString = _EwnPortString_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 2),
    _EwnPortString_Type()
)
ewnPortString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnPortString.setStatus("current")


class _EwnPortHardwareType_Type(Integer32):
    """Custom type ewnPortHardwareType based on Integer32"""
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
        *(("type100M", 2),
          ("type100MFX", 6),
          ("type10M", 1),
          ("type1G", 4),
          ("type1GFx", 5),
          ("typeMII", 3),
          ("typeUnknown", 7))
    )


_EwnPortHardwareType_Type.__name__ = "Integer32"
_EwnPortHardwareType_Object = MibTableColumn
ewnPortHardwareType = _EwnPortHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 3),
    _EwnPortHardwareType_Type()
)
ewnPortHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnPortHardwareType.setStatus("current")


class _EwnPortLinkStatus_Type(Integer32):
    """Custom type ewnPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_EwnPortLinkStatus_Type.__name__ = "Integer32"
_EwnPortLinkStatus_Object = MibTableColumn
ewnPortLinkStatus = _EwnPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 4),
    _EwnPortLinkStatus_Type()
)
ewnPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnPortLinkStatus.setStatus("current")


class _EwnPortLinkConfig_Type(Integer32):
    """Custom type ewnPortLinkConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_EwnPortLinkConfig_Type.__name__ = "Integer32"
_EwnPortLinkConfig_Object = MibTableColumn
ewnPortLinkConfig = _EwnPortLinkConfig_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 5),
    _EwnPortLinkConfig_Type()
)
ewnPortLinkConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortLinkConfig.setStatus("current")


class _EwnPortSpeedStatus_Type(Integer32):
    """Custom type ewnPortSpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 0),
          ("speed1G", 2))
    )


_EwnPortSpeedStatus_Type.__name__ = "Integer32"
_EwnPortSpeedStatus_Object = MibTableColumn
ewnPortSpeedStatus = _EwnPortSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 6),
    _EwnPortSpeedStatus_Type()
)
ewnPortSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnPortSpeedStatus.setStatus("current")


class _EwnPortSpeedConfig_Type(Integer32):
    """Custom type ewnPortSpeedConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed100M", 1),
          ("speed10M", 0),
          ("speed1G", 2),
          ("speedAuto", 3))
    )


_EwnPortSpeedConfig_Type.__name__ = "Integer32"
_EwnPortSpeedConfig_Object = MibTableColumn
ewnPortSpeedConfig = _EwnPortSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 7),
    _EwnPortSpeedConfig_Type()
)
ewnPortSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortSpeedConfig.setStatus("current")


class _EwnPortDupStatus_Type(Integer32):
    """Custom type ewnPortDupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("full", 1),
          ("half", 0))
    )


_EwnPortDupStatus_Type.__name__ = "Integer32"
_EwnPortDupStatus_Object = MibTableColumn
ewnPortDupStatus = _EwnPortDupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 8),
    _EwnPortDupStatus_Type()
)
ewnPortDupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnPortDupStatus.setStatus("current")


class _EwnPortDupConfig_Type(Integer32):
    """Custom type ewnPortDupConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("full", 1),
          ("half", 0))
    )


_EwnPortDupConfig_Type.__name__ = "Integer32"
_EwnPortDupConfig_Object = MibTableColumn
ewnPortDupConfig = _EwnPortDupConfig_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 9),
    _EwnPortDupConfig_Type()
)
ewnPortDupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortDupConfig.setStatus("current")


class _EwnPortFlowStatus_Type(Integer32):
    """Custom type ewnPortFlowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("rxOnOnly", 3),
          ("txOnOnly", 2),
          ("txRxOn", 1))
    )


_EwnPortFlowStatus_Type.__name__ = "Integer32"
_EwnPortFlowStatus_Object = MibTableColumn
ewnPortFlowStatus = _EwnPortFlowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 10),
    _EwnPortFlowStatus_Type()
)
ewnPortFlowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnPortFlowStatus.setStatus("current")


class _EwnPortFlowConfig_Type(Integer32):
    """Custom type ewnPortFlowConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnPortFlowConfig_Type.__name__ = "Integer32"
_EwnPortFlowConfig_Object = MibTableColumn
ewnPortFlowConfig = _EwnPortFlowConfig_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 11),
    _EwnPortFlowConfig_Type()
)
ewnPortFlowConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortFlowConfig.setStatus("current")


class _EwnPortBroadcastLimit_Type(Integer32):
    """Custom type ewnPortBroadcastLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EwnPortBroadcastLimit_Type.__name__ = "Integer32"
_EwnPortBroadcastLimit_Object = MibTableColumn
ewnPortBroadcastLimit = _EwnPortBroadcastLimit_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 13),
    _EwnPortBroadcastLimit_Type()
)
ewnPortBroadcastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortBroadcastLimit.setStatus("current")


class _EwnPortDlfMulticastLimit_Type(Integer32):
    """Custom type ewnPortDlfMulticastLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EwnPortDlfMulticastLimit_Type.__name__ = "Integer32"
_EwnPortDlfMulticastLimit_Object = MibTableColumn
ewnPortDlfMulticastLimit = _EwnPortDlfMulticastLimit_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 15),
    _EwnPortDlfMulticastLimit_Type()
)
ewnPortDlfMulticastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortDlfMulticastLimit.setStatus("current")


class _EwnPortLimitLevel_Type(Integer32):
    """Custom type ewnPortLimitLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EwnPortLimitLevel_Type.__name__ = "Integer32"
_EwnPortLimitLevel_Object = MibTableColumn
ewnPortLimitLevel = _EwnPortLimitLevel_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 16),
    _EwnPortLimitLevel_Type()
)
ewnPortLimitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortLimitLevel.setStatus("current")


class _EwnPortPriority_Type(Integer32):
    """Custom type ewnPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EwnPortPriority_Type.__name__ = "Integer32"
_EwnPortPriority_Object = MibTableColumn
ewnPortPriority = _EwnPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 17),
    _EwnPortPriority_Type()
)
ewnPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortPriority.setStatus("current")


class _EwnPortSwitchMode_Type(Integer32):
    """Custom type ewnPortSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 2),
          ("max-ACCESS", 1),
          ("normal", 0),
          ("trunk", 3))
    )


_EwnPortSwitchMode_Type.__name__ = "Integer32"
_EwnPortSwitchMode_Object = MibTableColumn
ewnPortSwitchMode = _EwnPortSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 18),
    _EwnPortSwitchMode_Type()
)
ewnPortSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortSwitchMode.setStatus("current")


class _EwnPortPVID_Type(Integer32):
    """Custom type ewnPortPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_EwnPortPVID_Type.__name__ = "Integer32"
_EwnPortPVID_Object = MibTableColumn
ewnPortPVID = _EwnPortPVID_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 19),
    _EwnPortPVID_Type()
)
ewnPortPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortPVID.setStatus("current")


class _EwnPortResetRMONCount_Type(Integer32):
    """Custom type ewnPortResetRMONCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnPortResetRMONCount_Type.__name__ = "Integer32"
_EwnPortResetRMONCount_Object = MibTableColumn
ewnPortResetRMONCount = _EwnPortResetRMONCount_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 20),
    _EwnPortResetRMONCount_Type()
)
ewnPortResetRMONCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortResetRMONCount.setStatus("current")


class _EwnPortAliasName_Type(DisplayString):
    """Custom type ewnPortAliasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_EwnPortAliasName_Type.__name__ = "DisplayString"
_EwnPortAliasName_Object = MibTableColumn
ewnPortAliasName = _EwnPortAliasName_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 2, 2, 1, 21),
    _EwnPortAliasName_Type()
)
ewnPortAliasName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnPortAliasName.setStatus("current")
_EwnMirror_ObjectIdentity = ObjectIdentity
ewnMirror = _EwnMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 3)
)
_EwnMirrorAvailablePortMap_Type = OctetString
_EwnMirrorAvailablePortMap_Object = MibScalar
ewnMirrorAvailablePortMap = _EwnMirrorAvailablePortMap_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 3, 1),
    _EwnMirrorAvailablePortMap_Type()
)
ewnMirrorAvailablePortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnMirrorAvailablePortMap.setStatus("current")
_EwnMirrorCount_Type = Integer32
_EwnMirrorCount_Object = MibScalar
ewnMirrorCount = _EwnMirrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 3, 2),
    _EwnMirrorCount_Type()
)
ewnMirrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnMirrorCount.setStatus("current")
_EwnMirrorTable_Object = MibTable
ewnMirrorTable = _EwnMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ewnMirrorTable.setStatus("current")
_EwnMirrorEntry_Object = MibTableRow
ewnMirrorEntry = _EwnMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 3, 3, 1)
)
ewnMirrorEntry.setIndexNames(
    (0, "EtherWAN-sw72000", "ewnMirrorIndex"),
)
if mibBuilder.loadTexts:
    ewnMirrorEntry.setStatus("current")


class _EwnMirrorIndex_Type(Integer32):
    """Custom type ewnMirrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EwnMirrorIndex_Type.__name__ = "Integer32"
_EwnMirrorIndex_Object = MibTableColumn
ewnMirrorIndex = _EwnMirrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 3, 3, 1, 1),
    _EwnMirrorIndex_Type()
)
ewnMirrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnMirrorIndex.setStatus("current")
_EwnMirrorToPort_Type = Integer32
_EwnMirrorToPort_Object = MibTableColumn
ewnMirrorToPort = _EwnMirrorToPort_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 3, 3, 1, 2),
    _EwnMirrorToPort_Type()
)
ewnMirrorToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnMirrorToPort.setStatus("current")
_EwnMirrorFromPortMap_Type = OctetString
_EwnMirrorFromPortMap_Object = MibTableColumn
ewnMirrorFromPortMap = _EwnMirrorFromPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 3, 3, 1, 3),
    _EwnMirrorFromPortMap_Type()
)
ewnMirrorFromPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnMirrorFromPortMap.setStatus("current")


class _EwnMirrorMode_Type(Integer32):
    """Custom type ewnMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("receive", 1),
          ("receiveandtransmit", 3),
          ("transmit", 2))
    )


_EwnMirrorMode_Type.__name__ = "Integer32"
_EwnMirrorMode_Object = MibTableColumn
ewnMirrorMode = _EwnMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 3, 3, 1, 4),
    _EwnMirrorMode_Type()
)
ewnMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnMirrorMode.setStatus("current")
_EwnTrunk_ObjectIdentity = ObjectIdentity
ewnTrunk = _EwnTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 4)
)
_EwnTrunkCount_Type = Integer32
_EwnTrunkCount_Object = MibScalar
ewnTrunkCount = _EwnTrunkCount_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 4, 1),
    _EwnTrunkCount_Type()
)
ewnTrunkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnTrunkCount.setStatus("current")
_EwnTrunkTable_Object = MibTable
ewnTrunkTable = _EwnTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ewnTrunkTable.setStatus("current")
_EwnTrunkEntry_Object = MibTableRow
ewnTrunkEntry = _EwnTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 4, 2, 1)
)
ewnTrunkEntry.setIndexNames(
    (0, "EtherWAN-sw72000", "ewnTrunkIndex"),
)
if mibBuilder.loadTexts:
    ewnTrunkEntry.setStatus("current")


class _EwnTrunkIndex_Type(Integer32):
    """Custom type ewnTrunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EwnTrunkIndex_Type.__name__ = "Integer32"
_EwnTrunkIndex_Object = MibTableColumn
ewnTrunkIndex = _EwnTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 4, 2, 1, 1),
    _EwnTrunkIndex_Type()
)
ewnTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnTrunkIndex.setStatus("current")
_EwnTrunkPortMap_Type = OctetString
_EwnTrunkPortMap_Object = MibTableColumn
ewnTrunkPortMap = _EwnTrunkPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 4, 2, 1, 2),
    _EwnTrunkPortMap_Type()
)
ewnTrunkPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnTrunkPortMap.setStatus("current")
_EwnTrunkAvailPortMap_Type = OctetString
_EwnTrunkAvailPortMap_Object = MibTableColumn
ewnTrunkAvailPortMap = _EwnTrunkAvailPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 4, 2, 1, 3),
    _EwnTrunkAvailPortMap_Type()
)
ewnTrunkAvailPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnTrunkAvailPortMap.setStatus("current")


class _EwnTrunkMaxNumOfPorts_Type(Integer32):
    """Custom type ewnTrunkMaxNumOfPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EwnTrunkMaxNumOfPorts_Type.__name__ = "Integer32"
_EwnTrunkMaxNumOfPorts_Object = MibTableColumn
ewnTrunkMaxNumOfPorts = _EwnTrunkMaxNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 4, 2, 1, 4),
    _EwnTrunkMaxNumOfPorts_Type()
)
ewnTrunkMaxNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnTrunkMaxNumOfPorts.setStatus("current")
_EwnLACP_ObjectIdentity = ObjectIdentity
ewnLACP = _EwnLACP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5)
)
_EwnLACP1_ObjectIdentity = ObjectIdentity
ewnLACP1 = _EwnLACP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 1)
)
_EwnLACPSYSPriority_Type = Integer32
_EwnLACPSYSPriority_Object = MibScalar
ewnLACPSYSPriority = _EwnLACPSYSPriority_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 1, 1),
    _EwnLACPSYSPriority_Type()
)
ewnLACPSYSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnLACPSYSPriority.setStatus("current")
_EwnLACPTable_Object = MibTable
ewnLACPTable = _EwnLACPTable_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ewnLACPTable.setStatus("current")
_EwnLACPCONFENTRY_Object = MibTableRow
ewnLACPCONFENTRY = _EwnLACPCONFENTRY_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 1, 2, 1)
)
ewnLACPCONFENTRY.setIndexNames(
    (0, "EtherWAN-sw72000", "ewnLACPPortIndex"),
)
if mibBuilder.loadTexts:
    ewnLACPCONFENTRY.setStatus("current")


class _EwnLACPPortIndex_Type(Integer32):
    """Custom type ewnLACPPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EwnLACPPortIndex_Type.__name__ = "Integer32"
_EwnLACPPortIndex_Object = MibTableColumn
ewnLACPPortIndex = _EwnLACPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 1, 2, 1, 1),
    _EwnLACPPortIndex_Type()
)
ewnLACPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnLACPPortIndex.setStatus("current")


class _EwnLACPPortName_Type(DisplayString):
    """Custom type ewnLACPPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EwnLACPPortName_Type.__name__ = "DisplayString"
_EwnLACPPortName_Object = MibTableColumn
ewnLACPPortName = _EwnLACPPortName_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 1, 2, 1, 2),
    _EwnLACPPortName_Type()
)
ewnLACPPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnLACPPortName.setStatus("current")


class _EwnLACPTimeout_Type(Integer32):
    """Custom type ewnLACPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("long", 1),
          ("short", 0))
    )


_EwnLACPTimeout_Type.__name__ = "Integer32"
_EwnLACPTimeout_Object = MibTableColumn
ewnLACPTimeout = _EwnLACPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 1, 2, 1, 3),
    _EwnLACPTimeout_Type()
)
ewnLACPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnLACPTimeout.setStatus("current")
_EwnLACPPriority_Type = Integer32
_EwnLACPPriority_Object = MibTableColumn
ewnLACPPriority = _EwnLACPPriority_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 1, 2, 1, 4),
    _EwnLACPPriority_Type()
)
ewnLACPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnLACPPriority.setStatus("current")
_EwnLACP2_ObjectIdentity = ObjectIdentity
ewnLACP2 = _EwnLACP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 2)
)
_EwnLACPPortTable_Object = MibTable
ewnLACPPortTable = _EwnLACPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    ewnLACPPortTable.setStatus("current")
_EwnLACPAGGENTRY_Object = MibTableRow
ewnLACPAGGENTRY = _EwnLACPAGGENTRY_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 2, 1, 1)
)
ewnLACPAGGENTRY.setIndexNames(
    (0, "EtherWAN-sw72000", "ewnLACPIndex"),
)
if mibBuilder.loadTexts:
    ewnLACPAGGENTRY.setStatus("current")


class _EwnLACPIndex_Type(Integer32):
    """Custom type ewnLACPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EwnLACPIndex_Type.__name__ = "Integer32"
_EwnLACPIndex_Object = MibTableColumn
ewnLACPIndex = _EwnLACPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 2, 1, 1, 1),
    _EwnLACPIndex_Type()
)
ewnLACPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnLACPIndex.setStatus("current")


class _EwnLACPPortString_Type(DisplayString):
    """Custom type ewnLACPPortString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EwnLACPPortString_Type.__name__ = "DisplayString"
_EwnLACPPortString_Object = MibTableColumn
ewnLACPPortString = _EwnLACPPortString_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 2, 1, 1, 2),
    _EwnLACPPortString_Type()
)
ewnLACPPortString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnLACPPortString.setStatus("current")


class _EwnLACPAdminKey_Type(Integer32):
    """Custom type ewnLACPAdminKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("group1", 1),
          ("group2", 2),
          ("group3", 3),
          ("statictrunk", 4))
    )


_EwnLACPAdminKey_Type.__name__ = "Integer32"
_EwnLACPAdminKey_Object = MibTableColumn
ewnLACPAdminKey = _EwnLACPAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 2, 1, 1, 3),
    _EwnLACPAdminKey_Type()
)
ewnLACPAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnLACPAdminKey.setStatus("current")


class _EwnLACPPortMode_Type(Integer32):
    """Custom type ewnLACPPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notAvailable", 2),
          ("passive", 0))
    )


_EwnLACPPortMode_Type.__name__ = "Integer32"
_EwnLACPPortMode_Object = MibTableColumn
ewnLACPPortMode = _EwnLACPPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 5, 2, 1, 1, 4),
    _EwnLACPPortMode_Type()
)
ewnLACPPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnLACPPortMode.setStatus("current")
_EwnBridge_ObjectIdentity = ObjectIdentity
ewnBridge = _EwnBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 6)
)


class _EwnBridgeSTPState_Type(Integer32):
    """Custom type ewnBridgeSTPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnBridgeSTPState_Type.__name__ = "Integer32"
_EwnBridgeSTPState_Object = MibScalar
ewnBridgeSTPState = _EwnBridgeSTPState_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 6, 1),
    _EwnBridgeSTPState_Type()
)
ewnBridgeSTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnBridgeSTPState.setStatus("current")
_EwnBridgeAgingTime_Type = Integer32
_EwnBridgeAgingTime_Object = MibScalar
ewnBridgeAgingTime = _EwnBridgeAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 6, 2),
    _EwnBridgeAgingTime_Type()
)
ewnBridgeAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnBridgeAgingTime.setStatus("current")
_EwnIGMP_ObjectIdentity = ObjectIdentity
ewnIGMP = _EwnIGMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7)
)


class _EwnIGMPState_Type(Integer32):
    """Custom type ewnIGMPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disabled", 0),
          ("passive", 1))
    )


_EwnIGMPState_Type.__name__ = "Integer32"
_EwnIGMPState_Object = MibScalar
ewnIGMPState = _EwnIGMPState_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 1),
    _EwnIGMPState_Type()
)
ewnIGMPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnIGMPState.setStatus("current")
_EwnIGMPCfgTable_Object = MibTable
ewnIGMPCfgTable = _EwnIGMPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ewnIGMPCfgTable.setStatus("current")
_EwnIGMPCfgEntry_Object = MibTableRow
ewnIGMPCfgEntry = _EwnIGMPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 2, 1)
)
ewnIGMPCfgEntry.setIndexNames(
    (0, "EtherWAN-sw72000", "ewnIGMPCfgIndex"),
)
if mibBuilder.loadTexts:
    ewnIGMPCfgEntry.setStatus("current")


class _EwnIGMPCfgIndex_Type(Integer32):
    """Custom type ewnIGMPCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EwnIGMPCfgIndex_Type.__name__ = "Integer32"
_EwnIGMPCfgIndex_Object = MibTableColumn
ewnIGMPCfgIndex = _EwnIGMPCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 2, 1, 1),
    _EwnIGMPCfgIndex_Type()
)
ewnIGMPCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnIGMPCfgIndex.setStatus("current")
_EwnIGMPCfgVlanID_Type = Integer32
_EwnIGMPCfgVlanID_Object = MibTableColumn
ewnIGMPCfgVlanID = _EwnIGMPCfgVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 2, 1, 2),
    _EwnIGMPCfgVlanID_Type()
)
ewnIGMPCfgVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnIGMPCfgVlanID.setStatus("current")


class _EwnIGMPCfgIGMPVersion_Type(Integer32):
    """Custom type ewnIGMPCfgIGMPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EwnIGMPCfgIGMPVersion_Type.__name__ = "Integer32"
_EwnIGMPCfgIGMPVersion_Object = MibTableColumn
ewnIGMPCfgIGMPVersion = _EwnIGMPCfgIGMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 2, 1, 3),
    _EwnIGMPCfgIGMPVersion_Type()
)
ewnIGMPCfgIGMPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnIGMPCfgIGMPVersion.setStatus("current")


class _EwnIGMPCfgFastLeave_Type(Integer32):
    """Custom type ewnIGMPCfgFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EwnIGMPCfgFastLeave_Type.__name__ = "Integer32"
_EwnIGMPCfgFastLeave_Object = MibTableColumn
ewnIGMPCfgFastLeave = _EwnIGMPCfgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 2, 1, 4),
    _EwnIGMPCfgFastLeave_Type()
)
ewnIGMPCfgFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnIGMPCfgFastLeave.setStatus("current")


class _EwnIGMPCfgQueryInterval_Type(Integer32):
    """Custom type ewnIGMPCfgQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18000),
    )


_EwnIGMPCfgQueryInterval_Type.__name__ = "Integer32"
_EwnIGMPCfgQueryInterval_Object = MibTableColumn
ewnIGMPCfgQueryInterval = _EwnIGMPCfgQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 2, 1, 5),
    _EwnIGMPCfgQueryInterval_Type()
)
ewnIGMPCfgQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnIGMPCfgQueryInterval.setStatus("current")


class _EwnIGMPCfgMaxResponseTime_Type(Integer32):
    """Custom type ewnIGMPCfgMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_EwnIGMPCfgMaxResponseTime_Type.__name__ = "Integer32"
_EwnIGMPCfgMaxResponseTime_Object = MibTableColumn
ewnIGMPCfgMaxResponseTime = _EwnIGMPCfgMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 2, 1, 6),
    _EwnIGMPCfgMaxResponseTime_Type()
)
ewnIGMPCfgMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnIGMPCfgMaxResponseTime.setStatus("current")


class _EwnIGMPCfgReportSuppression_Type(Integer32):
    """Custom type ewnIGMPCfgReportSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EwnIGMPCfgReportSuppression_Type.__name__ = "Integer32"
_EwnIGMPCfgReportSuppression_Object = MibTableColumn
ewnIGMPCfgReportSuppression = _EwnIGMPCfgReportSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 2, 1, 7),
    _EwnIGMPCfgReportSuppression_Type()
)
ewnIGMPCfgReportSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnIGMPCfgReportSuppression.setStatus("current")
_EwnIGMPRecordTable_Object = MibTable
ewnIGMPRecordTable = _EwnIGMPRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    ewnIGMPRecordTable.setStatus("current")
_EwnIGMPRecordEntry_Object = MibTableRow
ewnIGMPRecordEntry = _EwnIGMPRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 3, 1)
)
ewnIGMPRecordEntry.setIndexNames(
    (0, "EtherWAN-sw72000", "ewnIGMPRecordIndex"),
)
if mibBuilder.loadTexts:
    ewnIGMPRecordEntry.setStatus("current")


class _EwnIGMPRecordIndex_Type(Integer32):
    """Custom type ewnIGMPRecordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EwnIGMPRecordIndex_Type.__name__ = "Integer32"
_EwnIGMPRecordIndex_Object = MibTableColumn
ewnIGMPRecordIndex = _EwnIGMPRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 3, 1, 1),
    _EwnIGMPRecordIndex_Type()
)
ewnIGMPRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnIGMPRecordIndex.setStatus("current")
_EwnIGMPRecordGroupAddress_Type = IpAddress
_EwnIGMPRecordGroupAddress_Object = MibTableColumn
ewnIGMPRecordGroupAddress = _EwnIGMPRecordGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 3, 1, 2),
    _EwnIGMPRecordGroupAddress_Type()
)
ewnIGMPRecordGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnIGMPRecordGroupAddress.setStatus("current")
_EwnIGMPRecordInterface_Type = DisplayString
_EwnIGMPRecordInterface_Object = MibTableColumn
ewnIGMPRecordInterface = _EwnIGMPRecordInterface_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 3, 1, 3),
    _EwnIGMPRecordInterface_Type()
)
ewnIGMPRecordInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnIGMPRecordInterface.setStatus("current")
_EwnIGMPRecordUpTime_Type = DisplayString
_EwnIGMPRecordUpTime_Object = MibTableColumn
ewnIGMPRecordUpTime = _EwnIGMPRecordUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 3, 1, 4),
    _EwnIGMPRecordUpTime_Type()
)
ewnIGMPRecordUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnIGMPRecordUpTime.setStatus("current")
_EwnIGMPRecordExpireTime_Type = DisplayString
_EwnIGMPRecordExpireTime_Object = MibTableColumn
ewnIGMPRecordExpireTime = _EwnIGMPRecordExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 3, 1, 5),
    _EwnIGMPRecordExpireTime_Type()
)
ewnIGMPRecordExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnIGMPRecordExpireTime.setStatus("current")
_EwnIGMPRecordLastReporter_Type = IpAddress
_EwnIGMPRecordLastReporter_Object = MibTableColumn
ewnIGMPRecordLastReporter = _EwnIGMPRecordLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 7, 3, 1, 6),
    _EwnIGMPRecordLastReporter_Type()
)
ewnIGMPRecordLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnIGMPRecordLastReporter.setStatus("current")
_EwnVLAN_ObjectIdentity = ObjectIdentity
ewnVLAN = _EwnVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8)
)


class _EwnVLANGVRPState_Type(Integer32):
    """Custom type ewnVLANGVRPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnVLANGVRPState_Type.__name__ = "Integer32"
_EwnVLANGVRPState_Object = MibScalar
ewnVLANGVRPState = _EwnVLANGVRPState_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 1),
    _EwnVLANGVRPState_Type()
)
ewnVLANGVRPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnVLANGVRPState.setStatus("current")
_EwnVLANTable_Object = MibTable
ewnVLANTable = _EwnVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ewnVLANTable.setStatus("current")
_EwnVLANEntry_Object = MibTableRow
ewnVLANEntry = _EwnVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1)
)
ewnVLANEntry.setIndexNames(
    (0, "EtherWAN-sw72000", "ewnVLANIndex"),
)
if mibBuilder.loadTexts:
    ewnVLANEntry.setStatus("current")


class _EwnVLANIndex_Type(Integer32):
    """Custom type ewnVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_EwnVLANIndex_Type.__name__ = "Integer32"
_EwnVLANIndex_Object = MibTableColumn
ewnVLANIndex = _EwnVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1, 1),
    _EwnVLANIndex_Type()
)
ewnVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnVLANIndex.setStatus("current")


class _EwnVLANID_Type(Integer32):
    """Custom type ewnVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_EwnVLANID_Type.__name__ = "Integer32"
_EwnVLANID_Object = MibTableColumn
ewnVLANID = _EwnVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1, 2),
    _EwnVLANID_Type()
)
ewnVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnVLANID.setStatus("current")


class _EwnVLANName_Type(DisplayString):
    """Custom type ewnVLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EwnVLANName_Type.__name__ = "DisplayString"
_EwnVLANName_Object = MibTableColumn
ewnVLANName = _EwnVLANName_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1, 3),
    _EwnVLANName_Type()
)
ewnVLANName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnVLANName.setStatus("current")


class _EwnVLANState_Type(Integer32):
    """Custom type ewnVLANState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disabled", 1),
          ("invalid", 0))
    )


_EwnVLANState_Type.__name__ = "Integer32"
_EwnVLANState_Object = MibTableColumn
ewnVLANState = _EwnVLANState_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1, 4),
    _EwnVLANState_Type()
)
ewnVLANState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnVLANState.setStatus("current")


class _EwnVLANType_Type(Integer32):
    """Custom type ewnVLANType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("invalid", 0),
          ("static", 1))
    )


_EwnVLANType_Type.__name__ = "Integer32"
_EwnVLANType_Object = MibTableColumn
ewnVLANType = _EwnVLANType_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1, 5),
    _EwnVLANType_Type()
)
ewnVLANType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnVLANType.setStatus("current")
_EwnVLANStaticPortMap_Type = OctetString
_EwnVLANStaticPortMap_Object = MibTableColumn
ewnVLANStaticPortMap = _EwnVLANStaticPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1, 6),
    _EwnVLANStaticPortMap_Type()
)
ewnVLANStaticPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnVLANStaticPortMap.setStatus("current")
_EwnVLANStaticUntaggedPortMap_Type = OctetString
_EwnVLANStaticUntaggedPortMap_Object = MibTableColumn
ewnVLANStaticUntaggedPortMap = _EwnVLANStaticUntaggedPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1, 7),
    _EwnVLANStaticUntaggedPortMap_Type()
)
ewnVLANStaticUntaggedPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnVLANStaticUntaggedPortMap.setStatus("current")
_EwnVLANCurrentPortMap_Type = OctetString
_EwnVLANCurrentPortMap_Object = MibTableColumn
ewnVLANCurrentPortMap = _EwnVLANCurrentPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1, 8),
    _EwnVLANCurrentPortMap_Type()
)
ewnVLANCurrentPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnVLANCurrentPortMap.setStatus("current")
_EwnVLANCurrentUntaggedPortMap_Type = OctetString
_EwnVLANCurrentUntaggedPortMap_Object = MibTableColumn
ewnVLANCurrentUntaggedPortMap = _EwnVLANCurrentUntaggedPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1, 9),
    _EwnVLANCurrentUntaggedPortMap_Type()
)
ewnVLANCurrentUntaggedPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnVLANCurrentUntaggedPortMap.setStatus("current")
_EwnVLANCurrentRegisteredPortMap_Type = OctetString
_EwnVLANCurrentRegisteredPortMap_Object = MibTableColumn
ewnVLANCurrentRegisteredPortMap = _EwnVLANCurrentRegisteredPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1, 10),
    _EwnVLANCurrentRegisteredPortMap_Type()
)
ewnVLANCurrentRegisteredPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnVLANCurrentRegisteredPortMap.setStatus("current")


class _EwnVLANIPAddress_Type(DisplayString):
    """Custom type ewnVLANIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_EwnVLANIPAddress_Type.__name__ = "DisplayString"
_EwnVLANIPAddress_Object = MibTableColumn
ewnVLANIPAddress = _EwnVLANIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 2, 1, 11),
    _EwnVLANIPAddress_Type()
)
ewnVLANIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnVLANIPAddress.setStatus("current")


class _EwnVLANAddVlan_Type(Integer32):
    """Custom type ewnVLANAddVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_EwnVLANAddVlan_Type.__name__ = "Integer32"
_EwnVLANAddVlan_Object = MibScalar
ewnVLANAddVlan = _EwnVLANAddVlan_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 3),
    _EwnVLANAddVlan_Type()
)
ewnVLANAddVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnVLANAddVlan.setStatus("current")


class _EwnVLANDeleteVlan_Type(Integer32):
    """Custom type ewnVLANDeleteVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_EwnVLANDeleteVlan_Type.__name__ = "Integer32"
_EwnVLANDeleteVlan_Object = MibScalar
ewnVLANDeleteVlan = _EwnVLANDeleteVlan_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 8, 4),
    _EwnVLANDeleteVlan_Type()
)
ewnVLANDeleteVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnVLANDeleteVlan.setStatus("current")
_EwnQoS_ObjectIdentity = ObjectIdentity
ewnQoS = _EwnQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 9)
)


class _EwnQoSState_Type(Integer32):
    """Custom type ewnQoSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnQoSState_Type.__name__ = "Integer32"
_EwnQoSState_Object = MibScalar
ewnQoSState = _EwnQoSState_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 9, 1),
    _EwnQoSState_Type()
)
ewnQoSState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnQoSState.setStatus("current")


class _EwnQoSTrust_Type(Integer32):
    """Custom type ewnQoSTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("cosanddscp", 3),
          ("dscp", 2),
          ("none", 0))
    )


_EwnQoSTrust_Type.__name__ = "Integer32"
_EwnQoSTrust_Object = MibScalar
ewnQoSTrust = _EwnQoSTrust_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 9, 2),
    _EwnQoSTrust_Type()
)
ewnQoSTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnQoSTrust.setStatus("current")


class _EwnQoSPriorityQueueOut_Type(Integer32):
    """Custom type ewnQoSPriorityQueueOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnQoSPriorityQueueOut_Type.__name__ = "Integer32"
_EwnQoSPriorityQueueOut_Object = MibScalar
ewnQoSPriorityQueueOut = _EwnQoSPriorityQueueOut_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 9, 3),
    _EwnQoSPriorityQueueOut_Type()
)
ewnQoSPriorityQueueOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnQoSPriorityQueueOut.setStatus("current")
_EwnQoSWRRqueueTable_Object = MibTable
ewnQoSWRRqueueTable = _EwnQoSWRRqueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 9, 4)
)
if mibBuilder.loadTexts:
    ewnQoSWRRqueueTable.setStatus("current")
_EwnQoSWRRqueueEntry_Object = MibTableRow
ewnQoSWRRqueueEntry = _EwnQoSWRRqueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 9, 4, 1)
)
ewnQoSWRRqueueEntry.setIndexNames(
    (0, "EtherWAN-sw72000", "ewnQoSQueueIndex"),
)
if mibBuilder.loadTexts:
    ewnQoSWRRqueueEntry.setStatus("current")


class _EwnQoSQueueIndex_Type(Integer32):
    """Custom type ewnQoSQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EwnQoSQueueIndex_Type.__name__ = "Integer32"
_EwnQoSQueueIndex_Object = MibTableColumn
ewnQoSQueueIndex = _EwnQoSQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 9, 4, 1, 1),
    _EwnQoSQueueIndex_Type()
)
ewnQoSQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnQoSQueueIndex.setStatus("current")
_EwnQoSWRRqueueID_Type = Integer32
_EwnQoSWRRqueueID_Object = MibTableColumn
ewnQoSWRRqueueID = _EwnQoSWRRqueueID_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 9, 4, 1, 2),
    _EwnQoSWRRqueueID_Type()
)
ewnQoSWRRqueueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnQoSWRRqueueID.setStatus("current")


class _EwnQoSWRRqueueCoSmap_Type(DisplayString):
    """Custom type ewnQoSWRRqueueCoSmap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_EwnQoSWRRqueueCoSmap_Type.__name__ = "DisplayString"
_EwnQoSWRRqueueCoSmap_Object = MibTableColumn
ewnQoSWRRqueueCoSmap = _EwnQoSWRRqueueCoSmap_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 9, 4, 1, 3),
    _EwnQoSWRRqueueCoSmap_Type()
)
ewnQoSWRRqueueCoSmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnQoSWRRqueueCoSmap.setStatus("current")
_EwnQoSWRRqueueDSCPmap_Type = OctetString
_EwnQoSWRRqueueDSCPmap_Object = MibTableColumn
ewnQoSWRRqueueDSCPmap = _EwnQoSWRRqueueDSCPmap_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 9, 4, 1, 4),
    _EwnQoSWRRqueueDSCPmap_Type()
)
ewnQoSWRRqueueDSCPmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnQoSWRRqueueDSCPmap.setStatus("current")


class _EwnQoSWRRqueueBandwidth_Type(Integer32):
    """Custom type ewnQoSWRRqueueBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 55),
    )


_EwnQoSWRRqueueBandwidth_Type.__name__ = "Integer32"
_EwnQoSWRRqueueBandwidth_Object = MibTableColumn
ewnQoSWRRqueueBandwidth = _EwnQoSWRRqueueBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 9, 4, 1, 5),
    _EwnQoSWRRqueueBandwidth_Type()
)
ewnQoSWRRqueueBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnQoSWRRqueueBandwidth.setStatus("current")
_EwnSNMP_ObjectIdentity = ObjectIdentity
ewnSNMP = _EwnSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10)
)


class _EwnSNMPState_Type(Integer32):
    """Custom type ewnSNMPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnSNMPState_Type.__name__ = "Integer32"
_EwnSNMPState_Object = MibScalar
ewnSNMPState = _EwnSNMPState_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 1),
    _EwnSNMPState_Type()
)
ewnSNMPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPState.setStatus("current")


class _EwnSNMPCommunitySet_Type(DisplayString):
    """Custom type ewnSNMPCommunitySet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EwnSNMPCommunitySet_Type.__name__ = "DisplayString"
_EwnSNMPCommunitySet_Object = MibScalar
ewnSNMPCommunitySet = _EwnSNMPCommunitySet_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 2),
    _EwnSNMPCommunitySet_Type()
)
ewnSNMPCommunitySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPCommunitySet.setStatus("current")


class _EwnSNMPCommunityGet_Type(DisplayString):
    """Custom type ewnSNMPCommunityGet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EwnSNMPCommunityGet_Type.__name__ = "DisplayString"
_EwnSNMPCommunityGet_Object = MibScalar
ewnSNMPCommunityGet = _EwnSNMPCommunityGet_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 3),
    _EwnSNMPCommunityGet_Type()
)
ewnSNMPCommunityGet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPCommunityGet.setStatus("current")


class _EwnSNMPTrapCommunity1_Type(DisplayString):
    """Custom type ewnSNMPTrapCommunity1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EwnSNMPTrapCommunity1_Type.__name__ = "DisplayString"
_EwnSNMPTrapCommunity1_Object = MibScalar
ewnSNMPTrapCommunity1 = _EwnSNMPTrapCommunity1_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 4),
    _EwnSNMPTrapCommunity1_Type()
)
ewnSNMPTrapCommunity1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapCommunity1.setStatus("current")


class _EwnSNMPTrapCommunity2_Type(DisplayString):
    """Custom type ewnSNMPTrapCommunity2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EwnSNMPTrapCommunity2_Type.__name__ = "DisplayString"
_EwnSNMPTrapCommunity2_Object = MibScalar
ewnSNMPTrapCommunity2 = _EwnSNMPTrapCommunity2_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 5),
    _EwnSNMPTrapCommunity2_Type()
)
ewnSNMPTrapCommunity2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapCommunity2.setStatus("current")


class _EwnSNMPTrapCommunity3_Type(DisplayString):
    """Custom type ewnSNMPTrapCommunity3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EwnSNMPTrapCommunity3_Type.__name__ = "DisplayString"
_EwnSNMPTrapCommunity3_Object = MibScalar
ewnSNMPTrapCommunity3 = _EwnSNMPTrapCommunity3_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 6),
    _EwnSNMPTrapCommunity3_Type()
)
ewnSNMPTrapCommunity3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapCommunity3.setStatus("current")


class _EwnSNMPTrapCommunity4_Type(DisplayString):
    """Custom type ewnSNMPTrapCommunity4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EwnSNMPTrapCommunity4_Type.__name__ = "DisplayString"
_EwnSNMPTrapCommunity4_Object = MibScalar
ewnSNMPTrapCommunity4 = _EwnSNMPTrapCommunity4_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 7),
    _EwnSNMPTrapCommunity4_Type()
)
ewnSNMPTrapCommunity4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapCommunity4.setStatus("current")


class _EwnSNMPTrapCommunity5_Type(DisplayString):
    """Custom type ewnSNMPTrapCommunity5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EwnSNMPTrapCommunity5_Type.__name__ = "DisplayString"
_EwnSNMPTrapCommunity5_Object = MibScalar
ewnSNMPTrapCommunity5 = _EwnSNMPTrapCommunity5_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 8),
    _EwnSNMPTrapCommunity5_Type()
)
ewnSNMPTrapCommunity5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapCommunity5.setStatus("current")
_EwnSNMPTrapIpAddress1_Type = IpAddress
_EwnSNMPTrapIpAddress1_Object = MibScalar
ewnSNMPTrapIpAddress1 = _EwnSNMPTrapIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 9),
    _EwnSNMPTrapIpAddress1_Type()
)
ewnSNMPTrapIpAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapIpAddress1.setStatus("current")
_EwnSNMPTrapIpAddress2_Type = IpAddress
_EwnSNMPTrapIpAddress2_Object = MibScalar
ewnSNMPTrapIpAddress2 = _EwnSNMPTrapIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 10),
    _EwnSNMPTrapIpAddress2_Type()
)
ewnSNMPTrapIpAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapIpAddress2.setStatus("current")
_EwnSNMPTrapIpAddress3_Type = IpAddress
_EwnSNMPTrapIpAddress3_Object = MibScalar
ewnSNMPTrapIpAddress3 = _EwnSNMPTrapIpAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 11),
    _EwnSNMPTrapIpAddress3_Type()
)
ewnSNMPTrapIpAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapIpAddress3.setStatus("current")
_EwnSNMPTrapIpAddress4_Type = IpAddress
_EwnSNMPTrapIpAddress4_Object = MibScalar
ewnSNMPTrapIpAddress4 = _EwnSNMPTrapIpAddress4_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 12),
    _EwnSNMPTrapIpAddress4_Type()
)
ewnSNMPTrapIpAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapIpAddress4.setStatus("current")
_EwnSNMPTrapIpAddress5_Type = IpAddress
_EwnSNMPTrapIpAddress5_Object = MibScalar
ewnSNMPTrapIpAddress5 = _EwnSNMPTrapIpAddress5_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 13),
    _EwnSNMPTrapIpAddress5_Type()
)
ewnSNMPTrapIpAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapIpAddress5.setStatus("current")


class _EwnSNMPTrapLinkDown_Type(Integer32):
    """Custom type ewnSNMPTrapLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnSNMPTrapLinkDown_Type.__name__ = "Integer32"
_EwnSNMPTrapLinkDown_Object = MibScalar
ewnSNMPTrapLinkDown = _EwnSNMPTrapLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 16),
    _EwnSNMPTrapLinkDown_Type()
)
ewnSNMPTrapLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapLinkDown.setStatus("current")


class _EwnSNMPTrapLinkUp_Type(Integer32):
    """Custom type ewnSNMPTrapLinkUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnSNMPTrapLinkUp_Type.__name__ = "Integer32"
_EwnSNMPTrapLinkUp_Object = MibScalar
ewnSNMPTrapLinkUp = _EwnSNMPTrapLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 17),
    _EwnSNMPTrapLinkUp_Type()
)
ewnSNMPTrapLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPTrapLinkUp.setStatus("current")


class _EwnSNMPResetNeed_Type(Integer32):
    """Custom type ewnSNMPResetNeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EwnSNMPResetNeed_Type.__name__ = "Integer32"
_EwnSNMPResetNeed_Object = MibScalar
ewnSNMPResetNeed = _EwnSNMPResetNeed_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 20),
    _EwnSNMPResetNeed_Type()
)
ewnSNMPResetNeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnSNMPResetNeed.setStatus("current")


class _EwnSNMPResetSNMP_Type(Integer32):
    """Custom type ewnSNMPResetSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnSNMPResetSNMP_Type.__name__ = "Integer32"
_EwnSNMPResetSNMP_Object = MibScalar
ewnSNMPResetSNMP = _EwnSNMPResetSNMP_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 21),
    _EwnSNMPResetSNMP_Type()
)
ewnSNMPResetSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPResetSNMP.setStatus("current")


class _EwnSNMPResetRMONCount_Type(Integer32):
    """Custom type ewnSNMPResetRMONCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EwnSNMPResetRMONCount_Type.__name__ = "Integer32"
_EwnSNMPResetRMONCount_Object = MibScalar
ewnSNMPResetRMONCount = _EwnSNMPResetRMONCount_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 10, 22),
    _EwnSNMPResetRMONCount_Type()
)
ewnSNMPResetRMONCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ewnSNMPResetRMONCount.setStatus("current")
_EwnSDB_ObjectIdentity = ObjectIdentity
ewnSDB = _EwnSDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 11)
)
_EwnBridgeSDBTable_Object = MibTable
ewnBridgeSDBTable = _EwnBridgeSDBTable_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    ewnBridgeSDBTable.setStatus("current")
_EwnBridgeSDBEntry_Object = MibTableRow
ewnBridgeSDBEntry = _EwnBridgeSDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 11, 1, 1)
)
ewnBridgeSDBEntry.setIndexNames(
    (0, "EtherWAN-sw72000", "ewnBridgeSDBIndex"),
)
if mibBuilder.loadTexts:
    ewnBridgeSDBEntry.setStatus("current")


class _EwnBridgeSDBIndex_Type(Integer32):
    """Custom type ewnBridgeSDBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EwnBridgeSDBIndex_Type.__name__ = "Integer32"
_EwnBridgeSDBIndex_Object = MibTableColumn
ewnBridgeSDBIndex = _EwnBridgeSDBIndex_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 11, 1, 1, 1),
    _EwnBridgeSDBIndex_Type()
)
ewnBridgeSDBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnBridgeSDBIndex.setStatus("current")
_EwnBridgeSDBMacAddress_Type = PhysAddress
_EwnBridgeSDBMacAddress_Object = MibTableColumn
ewnBridgeSDBMacAddress = _EwnBridgeSDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 11, 1, 1, 2),
    _EwnBridgeSDBMacAddress_Type()
)
ewnBridgeSDBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnBridgeSDBMacAddress.setStatus("current")
_EwnBridgeSDBVlanId_Type = Integer32
_EwnBridgeSDBVlanId_Object = MibTableColumn
ewnBridgeSDBVlanId = _EwnBridgeSDBVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 11, 1, 1, 3),
    _EwnBridgeSDBVlanId_Type()
)
ewnBridgeSDBVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnBridgeSDBVlanId.setStatus("current")
_EwnBridgeSDBPortNo_Type = Integer32
_EwnBridgeSDBPortNo_Object = MibTableColumn
ewnBridgeSDBPortNo = _EwnBridgeSDBPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 11, 1, 1, 4),
    _EwnBridgeSDBPortNo_Type()
)
ewnBridgeSDBPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ewnBridgeSDBPortNo.setStatus("current")
_EwnRadius_ObjectIdentity = ObjectIdentity
ewnRadius = _EwnRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 12)
)
_EwnDHCP_ObjectIdentity = ObjectIdentity
ewnDHCP = _EwnDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 13)
)
_EwnSensor_ObjectIdentity = ObjectIdentity
ewnSensor = _EwnSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2736, 1, 1, 14)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EtherWAN-sw72000",
    **{"etherwan": etherwan,
       "lanSwitch": lanSwitch,
       "sw72000": sw72000,
       "ewnSystem": ewnSystem,
       "ewnSystemFirmwareRev": ewnSystemFirmwareRev,
       "ewnSystemConfigOperation": ewnSystemConfigOperation,
       "ewnSystemReboot": ewnSystemReboot,
       "ewnSystemRebootRequired": ewnSystemRebootRequired,
       "ewnSystemTFTP": ewnSystemTFTP,
       "ewnSystemTFTPFilename": ewnSystemTFTPFilename,
       "ewnSystemTFTPIpAddress": ewnSystemTFTPIpAddress,
       "ewnSystemTFTPAction": ewnSystemTFTPAction,
       "ewnSystemTFTPState": ewnSystemTFTPState,
       "ewnSystemProductModel": ewnSystemProductModel,
       "ewnSystemHardwareRev": ewnSystemHardwareRev,
       "ewnSystemGatewayIpAddress": ewnSystemGatewayIpAddress,
       "ewnSystemMacAddr": ewnSystemMacAddr,
       "ewnSystemPassword": ewnSystemPassword,
       "ewnSystemPasswordEncrypted": ewnSystemPasswordEncrypted,
       "ewnSystemAutoSaveState": ewnSystemAutoSaveState,
       "ewnSystemAutoSaveDelay": ewnSystemAutoSaveDelay,
       "ewnPort": ewnPort,
       "ewnPortCount": ewnPortCount,
       "ewnPortTable": ewnPortTable,
       "ewnPortEntry": ewnPortEntry,
       "ewnPortNo": ewnPortNo,
       "ewnPortString": ewnPortString,
       "ewnPortHardwareType": ewnPortHardwareType,
       "ewnPortLinkStatus": ewnPortLinkStatus,
       "ewnPortLinkConfig": ewnPortLinkConfig,
       "ewnPortSpeedStatus": ewnPortSpeedStatus,
       "ewnPortSpeedConfig": ewnPortSpeedConfig,
       "ewnPortDupStatus": ewnPortDupStatus,
       "ewnPortDupConfig": ewnPortDupConfig,
       "ewnPortFlowStatus": ewnPortFlowStatus,
       "ewnPortFlowConfig": ewnPortFlowConfig,
       "ewnPortBroadcastLimit": ewnPortBroadcastLimit,
       "ewnPortDlfMulticastLimit": ewnPortDlfMulticastLimit,
       "ewnPortLimitLevel": ewnPortLimitLevel,
       "ewnPortPriority": ewnPortPriority,
       "ewnPortSwitchMode": ewnPortSwitchMode,
       "ewnPortPVID": ewnPortPVID,
       "ewnPortResetRMONCount": ewnPortResetRMONCount,
       "ewnPortAliasName": ewnPortAliasName,
       "ewnMirror": ewnMirror,
       "ewnMirrorAvailablePortMap": ewnMirrorAvailablePortMap,
       "ewnMirrorCount": ewnMirrorCount,
       "ewnMirrorTable": ewnMirrorTable,
       "ewnMirrorEntry": ewnMirrorEntry,
       "ewnMirrorIndex": ewnMirrorIndex,
       "ewnMirrorToPort": ewnMirrorToPort,
       "ewnMirrorFromPortMap": ewnMirrorFromPortMap,
       "ewnMirrorMode": ewnMirrorMode,
       "ewnTrunk": ewnTrunk,
       "ewnTrunkCount": ewnTrunkCount,
       "ewnTrunkTable": ewnTrunkTable,
       "ewnTrunkEntry": ewnTrunkEntry,
       "ewnTrunkIndex": ewnTrunkIndex,
       "ewnTrunkPortMap": ewnTrunkPortMap,
       "ewnTrunkAvailPortMap": ewnTrunkAvailPortMap,
       "ewnTrunkMaxNumOfPorts": ewnTrunkMaxNumOfPorts,
       "ewnLACP": ewnLACP,
       "ewnLACP1": ewnLACP1,
       "ewnLACPSYSPriority": ewnLACPSYSPriority,
       "ewnLACPTable": ewnLACPTable,
       "ewnLACPCONFENTRY": ewnLACPCONFENTRY,
       "ewnLACPPortIndex": ewnLACPPortIndex,
       "ewnLACPPortName": ewnLACPPortName,
       "ewnLACPTimeout": ewnLACPTimeout,
       "ewnLACPPriority": ewnLACPPriority,
       "ewnLACP2": ewnLACP2,
       "ewnLACPPortTable": ewnLACPPortTable,
       "ewnLACPAGGENTRY": ewnLACPAGGENTRY,
       "ewnLACPIndex": ewnLACPIndex,
       "ewnLACPPortString": ewnLACPPortString,
       "ewnLACPAdminKey": ewnLACPAdminKey,
       "ewnLACPPortMode": ewnLACPPortMode,
       "ewnBridge": ewnBridge,
       "ewnBridgeSTPState": ewnBridgeSTPState,
       "ewnBridgeAgingTime": ewnBridgeAgingTime,
       "ewnIGMP": ewnIGMP,
       "ewnIGMPState": ewnIGMPState,
       "ewnIGMPCfgTable": ewnIGMPCfgTable,
       "ewnIGMPCfgEntry": ewnIGMPCfgEntry,
       "ewnIGMPCfgIndex": ewnIGMPCfgIndex,
       "ewnIGMPCfgVlanID": ewnIGMPCfgVlanID,
       "ewnIGMPCfgIGMPVersion": ewnIGMPCfgIGMPVersion,
       "ewnIGMPCfgFastLeave": ewnIGMPCfgFastLeave,
       "ewnIGMPCfgQueryInterval": ewnIGMPCfgQueryInterval,
       "ewnIGMPCfgMaxResponseTime": ewnIGMPCfgMaxResponseTime,
       "ewnIGMPCfgReportSuppression": ewnIGMPCfgReportSuppression,
       "ewnIGMPRecordTable": ewnIGMPRecordTable,
       "ewnIGMPRecordEntry": ewnIGMPRecordEntry,
       "ewnIGMPRecordIndex": ewnIGMPRecordIndex,
       "ewnIGMPRecordGroupAddress": ewnIGMPRecordGroupAddress,
       "ewnIGMPRecordInterface": ewnIGMPRecordInterface,
       "ewnIGMPRecordUpTime": ewnIGMPRecordUpTime,
       "ewnIGMPRecordExpireTime": ewnIGMPRecordExpireTime,
       "ewnIGMPRecordLastReporter": ewnIGMPRecordLastReporter,
       "ewnVLAN": ewnVLAN,
       "ewnVLANGVRPState": ewnVLANGVRPState,
       "ewnVLANTable": ewnVLANTable,
       "ewnVLANEntry": ewnVLANEntry,
       "ewnVLANIndex": ewnVLANIndex,
       "ewnVLANID": ewnVLANID,
       "ewnVLANName": ewnVLANName,
       "ewnVLANState": ewnVLANState,
       "ewnVLANType": ewnVLANType,
       "ewnVLANStaticPortMap": ewnVLANStaticPortMap,
       "ewnVLANStaticUntaggedPortMap": ewnVLANStaticUntaggedPortMap,
       "ewnVLANCurrentPortMap": ewnVLANCurrentPortMap,
       "ewnVLANCurrentUntaggedPortMap": ewnVLANCurrentUntaggedPortMap,
       "ewnVLANCurrentRegisteredPortMap": ewnVLANCurrentRegisteredPortMap,
       "ewnVLANIPAddress": ewnVLANIPAddress,
       "ewnVLANAddVlan": ewnVLANAddVlan,
       "ewnVLANDeleteVlan": ewnVLANDeleteVlan,
       "ewnQoS": ewnQoS,
       "ewnQoSState": ewnQoSState,
       "ewnQoSTrust": ewnQoSTrust,
       "ewnQoSPriorityQueueOut": ewnQoSPriorityQueueOut,
       "ewnQoSWRRqueueTable": ewnQoSWRRqueueTable,
       "ewnQoSWRRqueueEntry": ewnQoSWRRqueueEntry,
       "ewnQoSQueueIndex": ewnQoSQueueIndex,
       "ewnQoSWRRqueueID": ewnQoSWRRqueueID,
       "ewnQoSWRRqueueCoSmap": ewnQoSWRRqueueCoSmap,
       "ewnQoSWRRqueueDSCPmap": ewnQoSWRRqueueDSCPmap,
       "ewnQoSWRRqueueBandwidth": ewnQoSWRRqueueBandwidth,
       "ewnSNMP": ewnSNMP,
       "ewnSNMPState": ewnSNMPState,
       "ewnSNMPCommunitySet": ewnSNMPCommunitySet,
       "ewnSNMPCommunityGet": ewnSNMPCommunityGet,
       "ewnSNMPTrapCommunity1": ewnSNMPTrapCommunity1,
       "ewnSNMPTrapCommunity2": ewnSNMPTrapCommunity2,
       "ewnSNMPTrapCommunity3": ewnSNMPTrapCommunity3,
       "ewnSNMPTrapCommunity4": ewnSNMPTrapCommunity4,
       "ewnSNMPTrapCommunity5": ewnSNMPTrapCommunity5,
       "ewnSNMPTrapIpAddress1": ewnSNMPTrapIpAddress1,
       "ewnSNMPTrapIpAddress2": ewnSNMPTrapIpAddress2,
       "ewnSNMPTrapIpAddress3": ewnSNMPTrapIpAddress3,
       "ewnSNMPTrapIpAddress4": ewnSNMPTrapIpAddress4,
       "ewnSNMPTrapIpAddress5": ewnSNMPTrapIpAddress5,
       "ewnSNMPTrapLinkDown": ewnSNMPTrapLinkDown,
       "ewnSNMPTrapLinkUp": ewnSNMPTrapLinkUp,
       "ewnSNMPResetNeed": ewnSNMPResetNeed,
       "ewnSNMPResetSNMP": ewnSNMPResetSNMP,
       "ewnSNMPResetRMONCount": ewnSNMPResetRMONCount,
       "ewnSDB": ewnSDB,
       "ewnBridgeSDBTable": ewnBridgeSDBTable,
       "ewnBridgeSDBEntry": ewnBridgeSDBEntry,
       "ewnBridgeSDBIndex": ewnBridgeSDBIndex,
       "ewnBridgeSDBMacAddress": ewnBridgeSDBMacAddress,
       "ewnBridgeSDBVlanId": ewnBridgeSDBVlanId,
       "ewnBridgeSDBPortNo": ewnBridgeSDBPortNo,
       "ewnRadius": ewnRadius,
       "ewnDHCP": ewnDHCP,
       "ewnSensor": ewnSensor}
)

# SNMP MIB module (ExaltComProducts) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ExaltComProducts
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:58 2024
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

(AcmModulationT,
 AlarmLevelT,
 AuxNmsMode,
 EnableStatusT,
 EthAuxStatusT,
 EthMainStatusT,
 EthPortMode,
 ExaltEnableT,
 FileTransferStartT,
 FileTransferTypeT,
 Led4ColorT,
 NtpClientEnableT,
 Te1LboT,
 Te1LineCodeT,
 Te1LoopBackModeT,
 Te1StatusT,
 TimeZoneT,
 VlanGroupT,
 VlanStatusT,
 exaltcommunications) = mibBuilder.importSymbols(
    "ExaltComm",
    "AcmModulationT",
    "AlarmLevelT",
    "AuxNmsMode",
    "EnableStatusT",
    "EthAuxStatusT",
    "EthMainStatusT",
    "EthPortMode",
    "ExaltEnableT",
    "FileTransferStartT",
    "FileTransferTypeT",
    "Led4ColorT",
    "NtpClientEnableT",
    "Te1LboT",
    "Te1LineCodeT",
    "Te1LoopBackModeT",
    "Te1StatusT",
    "TimeZoneT",
    "VlanGroupT",
    "VlanStatusT",
    "exaltcommunications")

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

productsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1)
)
productsMIB.setRevisions(
        ("2013-04-29 10:21",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PwType(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 16),
    )



# MIB Managed Objects in the order of their OIDs

_ProductsMIBNotifications_ObjectIdentity = ObjectIdentity
productsMIBNotifications = _ProductsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1)
)
_ProductsMIBObjects_ObjectIdentity = ObjectIdentity
productsMIBObjects = _ProductsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2)
)
_RadioInfo_ObjectIdentity = ObjectIdentity
radioInfo = _RadioInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1)
)
if mibBuilder.loadTexts:
    radioInfo.setStatus("current")


class _ModelName_Type(DisplayString):
    """Custom type modelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ModelName_Type.__name__ = "DisplayString"
_ModelName_Object = MibScalar
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 1),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("current")


class _PartNumber_Type(DisplayString):
    """Custom type partNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PartNumber_Type.__name__ = "DisplayString"
_PartNumber_Object = MibScalar
partNumber = _PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 2),
    _PartNumber_Type()
)
partNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partNumber.setStatus("current")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 3),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _InterfaceType_Type(DisplayString):
    """Custom type interfaceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_InterfaceType_Type.__name__ = "DisplayString"
_InterfaceType_Object = MibScalar
interfaceType = _InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 4),
    _InterfaceType_Type()
)
interfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceType.setStatus("current")


class _FirmwareVersion_Type(DisplayString):
    """Custom type firmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FirmwareVersion_Type.__name__ = "DisplayString"
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 5),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")


class _BootVersion_Type(DisplayString):
    """Custom type bootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BootVersion_Type.__name__ = "DisplayString"
_BootVersion_Object = MibScalar
bootVersion = _BootVersion_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 6),
    _BootVersion_Type()
)
bootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersion.setStatus("current")


class _RdkDbVer_Type(DisplayString):
    """Custom type rdkDbVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RdkDbVer_Type.__name__ = "DisplayString"
_RdkDbVer_Object = MibScalar
rdkDbVer = _RdkDbVer_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 11),
    _RdkDbVer_Type()
)
rdkDbVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdkDbVer.setStatus("current")


class _TxFreqRange_Type(DisplayString):
    """Custom type txFreqRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TxFreqRange_Type.__name__ = "DisplayString"
_TxFreqRange_Object = MibScalar
txFreqRange = _TxFreqRange_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 12),
    _TxFreqRange_Type()
)
txFreqRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFreqRange.setStatus("current")


class _RxFreqRange_Type(DisplayString):
    """Custom type rxFreqRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RxFreqRange_Type.__name__ = "DisplayString"
_RxFreqRange_Object = MibScalar
rxFreqRange = _RxFreqRange_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 13),
    _RxFreqRange_Type()
)
rxFreqRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFreqRange.setStatus("current")


class _RfFreqBand_Type(DisplayString):
    """Custom type rfFreqBand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RfFreqBand_Type.__name__ = "DisplayString"
_RfFreqBand_Object = MibScalar
rfFreqBand = _RfFreqBand_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 14),
    _RfFreqBand_Type()
)
rfFreqBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfFreqBand.setStatus("current")


class _HwId_Type(DisplayString):
    """Custom type hwId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwId_Type.__name__ = "DisplayString"
_HwId_Object = MibScalar
hwId = _HwId_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 15),
    _HwId_Type()
)
hwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwId.setStatus("current")


class _ModelNumber_Type(DisplayString):
    """Custom type modelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModelNumber_Type.__name__ = "DisplayString"
_ModelNumber_Object = MibScalar
modelNumber = _ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1, 16),
    _ModelNumber_Type()
)
modelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelNumber.setStatus("current")
_RadioAdmin_ObjectIdentity = ObjectIdentity
radioAdmin = _RadioAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2)
)
if mibBuilder.loadTexts:
    radioAdmin.setStatus("current")


class _SysDate_Type(DisplayString):
    """Custom type sysDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_SysDate_Type.__name__ = "DisplayString"
_SysDate_Object = MibScalar
sysDate = _SysDate_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 1),
    _SysDate_Type()
)
sysDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDate.setStatus("current")
if mibBuilder.loadTexts:
    sysDate.setUnits("MM/DD/YYYY")


class _SysTime_Type(DisplayString):
    """Custom type sysTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SysTime_Type.__name__ = "DisplayString"
_SysTime_Object = MibScalar
sysTime = _SysTime_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 2),
    _SysTime_Type()
)
sysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTime.setStatus("current")
_RadioName_ObjectIdentity = ObjectIdentity
radioName = _RadioName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 3)
)


class _RnLocal_Type(DisplayString):
    """Custom type rnLocal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RnLocal_Type.__name__ = "DisplayString"
_RnLocal_Object = MibScalar
rnLocal = _RnLocal_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 3, 1),
    _RnLocal_Type()
)
rnLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rnLocal.setStatus("current")


class _RnRemote_Type(DisplayString):
    """Custom type rnRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RnRemote_Type.__name__ = "DisplayString"
_RnRemote_Object = MibScalar
rnRemote = _RnRemote_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 3, 2),
    _RnRemote_Type()
)
rnRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rnRemote.setStatus("current")


class _LinkName_Type(DisplayString):
    """Custom type linkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LinkName_Type.__name__ = "DisplayString"
_LinkName_Object = MibScalar
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 4),
    _LinkName_Type()
)
linkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkName.setStatus("current")


class _LinkSecKey_Type(DisplayString):
    """Custom type linkSecKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_LinkSecKey_Type.__name__ = "DisplayString"
_LinkSecKey_Object = MibScalar
linkSecKey = _LinkSecKey_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 5),
    _LinkSecKey_Type()
)
linkSecKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkSecKey.setStatus("current")


class _AdminPassword_Type(DisplayString):
    """Custom type adminPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AdminPassword_Type.__name__ = "DisplayString"
_AdminPassword_Object = MibScalar
adminPassword = _AdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 6),
    _AdminPassword_Type()
)
adminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminPassword.setStatus("current")


class _UserPassword_Type(DisplayString):
    """Custom type userPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_UserPassword_Type.__name__ = "DisplayString"
_UserPassword_Object = MibScalar
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 7),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")
_IpAddress_ObjectIdentity = ObjectIdentity
ipAddress = _IpAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 8)
)
_IpLocal_Type = IpAddress
_IpLocal_Object = MibScalar
ipLocal = _IpLocal_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 8, 1),
    _IpLocal_Type()
)
ipLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLocal.setStatus("current")
_IpRemote_Type = IpAddress
_IpRemote_Object = MibScalar
ipRemote = _IpRemote_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 8, 2),
    _IpRemote_Type()
)
ipRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRemote.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 9),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")


class _IpAddressNetmask_Type(DisplayString):
    """Custom type ipAddressNetmask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 18),
    )


_IpAddressNetmask_Type.__name__ = "DisplayString"
_IpAddressNetmask_Object = MibScalar
ipAddressNetmask = _IpAddressNetmask_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 10),
    _IpAddressNetmask_Type()
)
ipAddressNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressNetmask.setStatus("current")
if mibBuilder.loadTexts:
    ipAddressNetmask.setUnits("IP/NN Where NN=00 To 32")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 11),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")


class _AesEnable_Type(Integer32):
    """Custom type aesEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aesDisable", 0),
          ("aesEnable", 1))
    )


_AesEnable_Type.__name__ = "Integer32"
_AesEnable_Object = MibScalar
aesEnable = _AesEnable_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 12),
    _AesEnable_Type()
)
aesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesEnable.setStatus("current")


class _AesKey_Type(DisplayString):
    """Custom type aesKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AesKey_Type.__name__ = "DisplayString"
_AesKey_Object = MibScalar
aesKey = _AesKey_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 13),
    _AesKey_Type()
)
aesKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aesKey.setStatus("current")


class _LicKey_Type(DisplayString):
    """Custom type licKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LicKey_Type.__name__ = "DisplayString"
_LicKey_Object = MibScalar
licKey = _LicKey_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 14),
    _LicKey_Type()
)
licKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licKey.setStatus("current")
_SnmpConfig_ObjectIdentity = ObjectIdentity
snmpConfig = _SnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17)
)
_TrapIpaddr_Type = IpAddress
_TrapIpaddr_Object = MibScalar
trapIpaddr = _TrapIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 1),
    _TrapIpaddr_Type()
)
trapIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIpaddr.setStatus("current")
_TrapAuth_Type = EnableStatusT
_TrapAuth_Object = MibScalar
trapAuth = _TrapAuth_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 2),
    _TrapAuth_Type()
)
trapAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAuth.setStatus("current")
_TrapReboot_Type = EnableStatusT
_TrapReboot_Object = MibScalar
trapReboot = _TrapReboot_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 3),
    _TrapReboot_Type()
)
trapReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReboot.setStatus("current")
_TrapLocLinkStat_Type = EnableStatusT
_TrapLocLinkStat_Object = MibScalar
trapLocLinkStat = _TrapLocLinkStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 4),
    _TrapLocLinkStat_Type()
)
trapLocLinkStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLocLinkStat.setStatus("current")
_TrapLocAlarmStat_Type = EnableStatusT
_TrapLocAlarmStat_Object = MibScalar
trapLocAlarmStat = _TrapLocAlarmStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 5),
    _TrapLocAlarmStat_Type()
)
trapLocAlarmStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLocAlarmStat.setStatus("current")
_TrapRemAlarmStat_Type = EnableStatusT
_TrapRemAlarmStat_Object = MibScalar
trapRemAlarmStat = _TrapRemAlarmStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 6),
    _TrapRemAlarmStat_Type()
)
trapRemAlarmStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapRemAlarmStat.setStatus("current")
_TrapLocRslStat_Type = EnableStatusT
_TrapLocRslStat_Object = MibScalar
trapLocRslStat = _TrapLocRslStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 7),
    _TrapLocRslStat_Type()
)
trapLocRslStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLocRslStat.setStatus("current")
_TrapLocTempStat_Type = EnableStatusT
_TrapLocTempStat_Object = MibScalar
trapLocTempStat = _TrapLocTempStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 8),
    _TrapLocTempStat_Type()
)
trapLocTempStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLocTempStat.setStatus("current")
_TrapLocRslThreshold_Type = Integer32
_TrapLocRslThreshold_Object = MibScalar
trapLocRslThreshold = _TrapLocRslThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 9),
    _TrapLocRslThreshold_Type()
)
trapLocRslThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLocRslThreshold.setStatus("current")
_Trapv1Enable_Type = EnableStatusT
_Trapv1Enable_Object = MibScalar
trapv1Enable = _Trapv1Enable_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 10),
    _Trapv1Enable_Type()
)
trapv1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapv1Enable.setStatus("current")
_Trapv2cEnable_Type = EnableStatusT
_Trapv2cEnable_Object = MibScalar
trapv2cEnable = _Trapv2cEnable_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 11),
    _Trapv2cEnable_Type()
)
trapv2cEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapv2cEnable.setStatus("current")
_Trapv3Enable_Type = EnableStatusT
_Trapv3Enable_Object = MibScalar
trapv3Enable = _Trapv3Enable_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 17, 12),
    _Trapv3Enable_Type()
)
trapv3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapv3Enable.setStatus("current")
_Ntp_ObjectIdentity = ObjectIdentity
ntp = _Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 18)
)
if mibBuilder.loadTexts:
    ntp.setStatus("current")
_NtpClientEnable_Type = NtpClientEnableT
_NtpClientEnable_Object = MibScalar
ntpClientEnable = _NtpClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 18, 1),
    _NtpClientEnable_Type()
)
ntpClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClientEnable.setStatus("current")


class _NtpServer1IpAddr_Type(DisplayString):
    """Custom type ntpServer1IpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_NtpServer1IpAddr_Type.__name__ = "DisplayString"
_NtpServer1IpAddr_Object = MibScalar
ntpServer1IpAddr = _NtpServer1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 18, 2),
    _NtpServer1IpAddr_Type()
)
ntpServer1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServer1IpAddr.setStatus("current")


class _NtpServer2IpAddr_Type(DisplayString):
    """Custom type ntpServer2IpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_NtpServer2IpAddr_Type.__name__ = "DisplayString"
_NtpServer2IpAddr_Object = MibScalar
ntpServer2IpAddr = _NtpServer2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 18, 3),
    _NtpServer2IpAddr_Type()
)
ntpServer2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServer2IpAddr.setStatus("current")


class _NtpServer3IpAddr_Type(DisplayString):
    """Custom type ntpServer3IpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_NtpServer3IpAddr_Type.__name__ = "DisplayString"
_NtpServer3IpAddr_Object = MibScalar
ntpServer3IpAddr = _NtpServer3IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 18, 4),
    _NtpServer3IpAddr_Type()
)
ntpServer3IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServer3IpAddr.setStatus("current")


class _NtpServer4IpAddr_Type(DisplayString):
    """Custom type ntpServer4IpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_NtpServer4IpAddr_Type.__name__ = "DisplayString"
_NtpServer4IpAddr_Object = MibScalar
ntpServer4IpAddr = _NtpServer4IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 18, 5),
    _NtpServer4IpAddr_Type()
)
ntpServer4IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServer4IpAddr.setStatus("current")
_NtpTimeZoneSelect_Type = TimeZoneT
_NtpTimeZoneSelect_Object = MibScalar
ntpTimeZoneSelect = _NtpTimeZoneSelect_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 18, 6),
    _NtpTimeZoneSelect_Type()
)
ntpTimeZoneSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTimeZoneSelect.setStatus("current")


class _CommitNtpSettings_Type(DisplayString):
    """Custom type commitNtpSettings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 200),
    )


_CommitNtpSettings_Type.__name__ = "DisplayString"
_CommitNtpSettings_Object = MibScalar
commitNtpSettings = _CommitNtpSettings_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 18, 1000),
    _CommitNtpSettings_Type()
)
commitNtpSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitNtpSettings.setStatus("current")


class _CommitAdminSettings_Type(DisplayString):
    """Custom type commitAdminSettings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 200),
    )


_CommitAdminSettings_Type.__name__ = "DisplayString"
_CommitAdminSettings_Object = MibScalar
commitAdminSettings = _CommitAdminSettings_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 2, 1000),
    _CommitAdminSettings_Type()
)
commitAdminSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitAdminSettings.setStatus("current")
_RadioConfig_ObjectIdentity = ObjectIdentity
radioConfig = _RadioConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3)
)
if mibBuilder.loadTexts:
    radioConfig.setStatus("current")
_SystemConfig_ObjectIdentity = ObjectIdentity
systemConfig = _SystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    systemConfig.setStatus("current")
_CommitSystemSettings_Type = DisplayString
_CommitSystemSettings_Object = MibScalar
commitSystemSettings = _CommitSystemSettings_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 1000),
    _CommitSystemSettings_Type()
)
commitSystemSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitSystemSettings.setStatus("current")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    interface.setStatus("current")
_Te1_ObjectIdentity = ObjectIdentity
te1 = _Te1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    te1.setStatus("current")
_Te1NumChannels_Type = Gauge32
_Te1NumChannels_Object = MibScalar
te1NumChannels = _Te1NumChannels_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2, 1),
    _Te1NumChannels_Type()
)
te1NumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    te1NumChannels.setStatus("current")
if mibBuilder.loadTexts:
    te1NumChannels.setUnits("channels")
_Te1NumActiveChannels_Type = Gauge32
_Te1NumActiveChannels_Object = MibScalar
te1NumActiveChannels = _Te1NumActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2, 2),
    _Te1NumActiveChannels_Type()
)
te1NumActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    te1NumActiveChannels.setStatus("current")
if mibBuilder.loadTexts:
    te1NumActiveChannels.setUnits("channels")


class _SelectT1orE1_Type(Integer32):
    """Custom type selectT1orE1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("t1", 0))
    )


_SelectT1orE1_Type.__name__ = "Integer32"
_SelectT1orE1_Object = MibScalar
selectT1orE1 = _SelectT1orE1_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2, 3),
    _SelectT1orE1_Type()
)
selectT1orE1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selectT1orE1.setStatus("current")
_Te1Interfaces_Object = MibTable
te1Interfaces = _Te1Interfaces_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2, 4)
)
if mibBuilder.loadTexts:
    te1Interfaces.setStatus("current")
_Te1Interface_Object = MibTableRow
te1Interface = _Te1Interface_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2, 4, 1)
)
te1Interface.setIndexNames(
    (0, "ExaltComProducts", "te1Status"),
    (0, "ExaltComProducts", "t1LBO"),
    (0, "ExaltComProducts", "te1AIS"),
    (0, "ExaltComProducts", "t1LineCode"),
    (0, "ExaltComProducts", "te1LoopBackMode"),
)
if mibBuilder.loadTexts:
    te1Interface.setStatus("current")
_Te1Status_Type = Te1StatusT
_Te1Status_Object = MibTableColumn
te1Status = _Te1Status_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2, 4, 1, 1),
    _Te1Status_Type()
)
te1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    te1Status.setStatus("current")
_T1LBO_Type = Te1LboT
_T1LBO_Object = MibTableColumn
t1LBO = _T1LBO_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2, 4, 1, 2),
    _T1LBO_Type()
)
t1LBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1LBO.setStatus("current")
if mibBuilder.loadTexts:
    t1LBO.setUnits("feet")
_Te1AIS_Type = Te1StatusT
_Te1AIS_Object = MibTableColumn
te1AIS = _Te1AIS_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2, 4, 1, 3),
    _Te1AIS_Type()
)
te1AIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    te1AIS.setStatus("current")
_T1LineCode_Type = Te1LineCodeT
_T1LineCode_Object = MibTableColumn
t1LineCode = _T1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2, 4, 1, 4),
    _T1LineCode_Type()
)
t1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1LineCode.setStatus("current")
_Te1LoopBackMode_Type = Te1LoopBackModeT
_Te1LoopBackMode_Object = MibTableColumn
te1LoopBackMode = _Te1LoopBackMode_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2, 4, 1, 5),
    _Te1LoopBackMode_Type()
)
te1LoopBackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    te1LoopBackMode.setStatus("current")


class _CommitTe1Settings_Type(DisplayString):
    """Custom type commitTe1Settings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 200),
    )


_CommitTe1Settings_Type.__name__ = "DisplayString"
_CommitTe1Settings_Object = MibScalar
commitTe1Settings = _CommitTe1Settings_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 2, 1000),
    _CommitTe1Settings_Type()
)
commitTe1Settings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitTe1Settings.setStatus("current")
_FileManagement_ObjectIdentity = ObjectIdentity
fileManagement = _FileManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    fileManagement.setStatus("current")


class _CurrentFwFilename_Type(DisplayString):
    """Custom type currentFwFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CurrentFwFilename_Type.__name__ = "DisplayString"
_CurrentFwFilename_Object = MibScalar
currentFwFilename = _CurrentFwFilename_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 3, 1),
    _CurrentFwFilename_Type()
)
currentFwFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFwFilename.setStatus("current")


class _AlternateFwFilename_Type(DisplayString):
    """Custom type alternateFwFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AlternateFwFilename_Type.__name__ = "DisplayString"
_AlternateFwFilename_Object = MibScalar
alternateFwFilename = _AlternateFwFilename_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 3, 2),
    _AlternateFwFilename_Type()
)
alternateFwFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alternateFwFilename.setStatus("current")


class _SwapFWimage_Type(DisplayString):
    """Custom type swapFWimage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_SwapFWimage_Type.__name__ = "DisplayString"
_SwapFWimage_Object = MibScalar
swapFWimage = _SwapFWimage_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 3, 3),
    _SwapFWimage_Type()
)
swapFWimage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swapFWimage.setStatus("current")
_FileTransfer_ObjectIdentity = ObjectIdentity
fileTransfer = _FileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 3, 4)
)
if mibBuilder.loadTexts:
    fileTransfer.setStatus("current")


class _TftpServerIp_Type(DisplayString):
    """Custom type tftpServerIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 15),
    )


_TftpServerIp_Type.__name__ = "DisplayString"
_TftpServerIp_Object = MibScalar
tftpServerIp = _TftpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 3, 4, 1),
    _TftpServerIp_Type()
)
tftpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerIp.setStatus("current")


class _UploadFilename_Type(DisplayString):
    """Custom type uploadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UploadFilename_Type.__name__ = "DisplayString"
_UploadFilename_Object = MibScalar
uploadFilename = _UploadFilename_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 3, 4, 2),
    _UploadFilename_Type()
)
uploadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadFilename.setStatus("current")
_TransferType_Type = FileTransferTypeT
_TransferType_Object = MibScalar
transferType = _TransferType_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 3, 4, 3),
    _TransferType_Type()
)
transferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferType.setStatus("current")
_TransferStart_Type = FileTransferStartT
_TransferStart_Object = MibScalar
transferStart = _TransferStart_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 3, 4, 4),
    _TransferStart_Type()
)
transferStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferStart.setStatus("current")


class _TransferStatus_Type(DisplayString):
    """Custom type transferStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TransferStatus_Type.__name__ = "DisplayString"
_TransferStatus_Object = MibScalar
transferStatus = _TransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 3, 4, 5),
    _TransferStatus_Type()
)
transferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferStatus.setStatus("current")


class _FactoryFwFilename_Type(DisplayString):
    """Custom type factoryFwFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FactoryFwFilename_Type.__name__ = "DisplayString"
_FactoryFwFilename_Object = MibScalar
factoryFwFilename = _FactoryFwFilename_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 3, 5),
    _FactoryFwFilename_Type()
)
factoryFwFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryFwFilename.setStatus("current")
_RadioMonitor_ObjectIdentity = ObjectIdentity
radioMonitor = _RadioMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4)
)
if mibBuilder.loadTexts:
    radioMonitor.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2)
)
_AlmLocal_ObjectIdentity = ObjectIdentity
almLocal = _AlmLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3)
)
_LocSysAlarms_ObjectIdentity = ObjectIdentity
locSysAlarms = _LocSysAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 1)
)
_LocLinkState_Type = AlarmLevelT
_LocLinkState_Object = MibScalar
locLinkState = _LocLinkState_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 1, 1),
    _LocLinkState_Type()
)
locLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locLinkState.setStatus("current")
_LocTempAlarm_Type = AlarmLevelT
_LocTempAlarm_Object = MibScalar
locTempAlarm = _LocTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 1, 2),
    _LocTempAlarm_Type()
)
locTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locTempAlarm.setStatus("current")
_LocCurrentTemp_Type = Integer32
_LocCurrentTemp_Object = MibScalar
locCurrentTemp = _LocCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 1, 3),
    _LocCurrentTemp_Type()
)
locCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locCurrentTemp.setStatus("current")
if mibBuilder.loadTexts:
    locCurrentTemp.setUnits("C")
_LocCurrentTempS_Type = DisplayString
_LocCurrentTempS_Object = MibScalar
locCurrentTempS = _LocCurrentTempS_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 1, 4),
    _LocCurrentTempS_Type()
)
locCurrentTempS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locCurrentTempS.setStatus("current")
_LocLinkSecMismatch_Type = AlarmLevelT
_LocLinkSecMismatch_Object = MibScalar
locLinkSecMismatch = _LocLinkSecMismatch_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 1, 9),
    _LocLinkSecMismatch_Type()
)
locLinkSecMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locLinkSecMismatch.setStatus("current")
_LocLinkStateV_Type = AlarmLevelT
_LocLinkStateV_Object = MibScalar
locLinkStateV = _LocLinkStateV_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 1, 15),
    _LocLinkStateV_Type()
)
locLinkStateV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locLinkStateV.setStatus("current")
_LocLinkStateH_Type = AlarmLevelT
_LocLinkStateH_Object = MibScalar
locLinkStateH = _LocLinkStateH_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 1, 16),
    _LocLinkStateH_Type()
)
locLinkStateH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locLinkStateH.setStatus("current")
_LocEthAlarms_ObjectIdentity = ObjectIdentity
locEthAlarms = _LocEthAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 2)
)
_LocTe1Alarms_ObjectIdentity = ObjectIdentity
locTe1Alarms = _LocTe1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 3)
)
_LocTe1LinkSummary_Type = Led4ColorT
_LocTe1LinkSummary_Object = MibScalar
locTe1LinkSummary = _LocTe1LinkSummary_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 3, 1),
    _LocTe1LinkSummary_Type()
)
locTe1LinkSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locTe1LinkSummary.setStatus("current")
_LocTE1Alarms_Object = MibTable
locTE1Alarms = _LocTE1Alarms_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    locTE1Alarms.setStatus("current")
_LocTe1AlarmsEntry_Object = MibTableRow
locTe1AlarmsEntry = _LocTe1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 3, 2, 1)
)
locTe1AlarmsEntry.setIndexNames(
    (0, "ExaltComProducts", "locTe1Alarm"),
)
if mibBuilder.loadTexts:
    locTe1AlarmsEntry.setStatus("current")
_LocTe1Alarm_Type = AlarmLevelT
_LocTe1Alarm_Object = MibTableColumn
locTe1Alarm = _LocTe1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 3, 2, 1, 1),
    _LocTe1Alarm_Type()
)
locTe1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locTe1Alarm.setStatus("current")
_AlmRemote_ObjectIdentity = ObjectIdentity
almRemote = _AlmRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4)
)
_RemSysAlarms_ObjectIdentity = ObjectIdentity
remSysAlarms = _RemSysAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 1)
)
_RemLinkState_Type = AlarmLevelT
_RemLinkState_Object = MibScalar
remLinkState = _RemLinkState_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 1, 1),
    _RemLinkState_Type()
)
remLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remLinkState.setStatus("current")
_RemTempAlarm_Type = AlarmLevelT
_RemTempAlarm_Object = MibScalar
remTempAlarm = _RemTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 1, 2),
    _RemTempAlarm_Type()
)
remTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTempAlarm.setStatus("current")
_RemCurrentTemp_Type = Integer32
_RemCurrentTemp_Object = MibScalar
remCurrentTemp = _RemCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 1, 3),
    _RemCurrentTemp_Type()
)
remCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remCurrentTemp.setStatus("current")
if mibBuilder.loadTexts:
    remCurrentTemp.setUnits("C")
_RemCurrentTempS_Type = DisplayString
_RemCurrentTempS_Object = MibScalar
remCurrentTempS = _RemCurrentTempS_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 1, 4),
    _RemCurrentTempS_Type()
)
remCurrentTempS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remCurrentTempS.setStatus("current")
_RemLinkSecMismatch_Type = AlarmLevelT
_RemLinkSecMismatch_Object = MibScalar
remLinkSecMismatch = _RemLinkSecMismatch_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 1, 9),
    _RemLinkSecMismatch_Type()
)
remLinkSecMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remLinkSecMismatch.setStatus("current")
_RemLinkStateV_Type = AlarmLevelT
_RemLinkStateV_Object = MibScalar
remLinkStateV = _RemLinkStateV_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 1, 15),
    _RemLinkStateV_Type()
)
remLinkStateV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remLinkStateV.setStatus("current")
_RemLinkStateH_Type = AlarmLevelT
_RemLinkStateH_Object = MibScalar
remLinkStateH = _RemLinkStateH_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 1, 16),
    _RemLinkStateH_Type()
)
remLinkStateH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remLinkStateH.setStatus("current")
_RemEthAlarms_ObjectIdentity = ObjectIdentity
remEthAlarms = _RemEthAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 2)
)
_RemTe1Alarms_ObjectIdentity = ObjectIdentity
remTe1Alarms = _RemTe1Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 3)
)
_RemTe1LinkSummary_Type = Led4ColorT
_RemTe1LinkSummary_Object = MibScalar
remTe1LinkSummary = _RemTe1LinkSummary_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 3, 1),
    _RemTe1LinkSummary_Type()
)
remTe1LinkSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTe1LinkSummary.setStatus("current")
_RemTE1Alarms_Object = MibTable
remTE1Alarms = _RemTE1Alarms_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 3, 2)
)
if mibBuilder.loadTexts:
    remTE1Alarms.setStatus("current")
_RemTe1AlarmsEntry_Object = MibTableRow
remTe1AlarmsEntry = _RemTe1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 3, 2, 1)
)
remTe1AlarmsEntry.setIndexNames(
    (0, "ExaltComProducts", "remTe1Alarm"),
)
if mibBuilder.loadTexts:
    remTe1AlarmsEntry.setStatus("current")
_RemTe1Alarm_Type = AlarmLevelT
_RemTe1Alarm_Object = MibTableColumn
remTe1Alarm = _RemTe1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 3, 2, 1, 1),
    _RemTe1Alarm_Type()
)
remTe1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTe1Alarm.setStatus("current")
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3)
)
_PerfLocal_ObjectIdentity = ObjectIdentity
perfLocal = _PerfLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1)
)
_LocCurrentBER_Type = Integer32
_LocCurrentBER_Object = MibScalar
locCurrentBER = _LocCurrentBER_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 1),
    _LocCurrentBER_Type()
)
locCurrentBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locCurrentBER.setStatus("current")
if mibBuilder.loadTexts:
    locCurrentBER.setUnits("BER * 1000000.0")
_LocCurrentBERstr_Type = DisplayString
_LocCurrentBERstr_Object = MibScalar
locCurrentBERstr = _LocCurrentBERstr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 2),
    _LocCurrentBERstr_Type()
)
locCurrentBERstr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locCurrentBERstr.setStatus("current")
_LocCurrentRSL_Type = Integer32
_LocCurrentRSL_Object = MibScalar
locCurrentRSL = _LocCurrentRSL_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 3),
    _LocCurrentRSL_Type()
)
locCurrentRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locCurrentRSL.setStatus("current")
if mibBuilder.loadTexts:
    locCurrentRSL.setUnits("dBm")
_LocCurrentRSLstr_Type = DisplayString
_LocCurrentRSLstr_Object = MibScalar
locCurrentRSLstr = _LocCurrentRSLstr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 4),
    _LocCurrentRSLstr_Type()
)
locCurrentRSLstr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locCurrentRSLstr.setStatus("current")
_LocErrorDuration_Type = Integer32
_LocErrorDuration_Object = MibScalar
locErrorDuration = _LocErrorDuration_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 5),
    _LocErrorDuration_Type()
)
locErrorDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locErrorDuration.setStatus("current")
if mibBuilder.loadTexts:
    locErrorDuration.setUnits("Seconds")
_LocErrorDurationStr_Type = DisplayString
_LocErrorDurationStr_Object = MibScalar
locErrorDurationStr = _LocErrorDurationStr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 6),
    _LocErrorDurationStr_Type()
)
locErrorDurationStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locErrorDurationStr.setStatus("current")
_LocUnavailDuration_Type = Integer32
_LocUnavailDuration_Object = MibScalar
locUnavailDuration = _LocUnavailDuration_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 7),
    _LocUnavailDuration_Type()
)
locUnavailDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locUnavailDuration.setStatus("current")
if mibBuilder.loadTexts:
    locUnavailDuration.setUnits("Seconds")
_LocUnavailDurationStr_Type = DisplayString
_LocUnavailDurationStr_Object = MibScalar
locUnavailDurationStr = _LocUnavailDurationStr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 8),
    _LocUnavailDurationStr_Type()
)
locUnavailDurationStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locUnavailDurationStr.setStatus("current")
_LocMinRSL_Type = Integer32
_LocMinRSL_Object = MibScalar
locMinRSL = _LocMinRSL_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 9),
    _LocMinRSL_Type()
)
locMinRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMinRSL.setStatus("current")
if mibBuilder.loadTexts:
    locMinRSL.setUnits("dBm")
_LocMinRSLstr_Type = DisplayString
_LocMinRSLstr_Object = MibScalar
locMinRSLstr = _LocMinRSLstr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 10),
    _LocMinRSLstr_Type()
)
locMinRSLstr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMinRSLstr.setStatus("current")
_LocMinRSLtimestamp_Type = DisplayString
_LocMinRSLtimestamp_Object = MibScalar
locMinRSLtimestamp = _LocMinRSLtimestamp_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 11),
    _LocMinRSLtimestamp_Type()
)
locMinRSLtimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMinRSLtimestamp.setStatus("current")
_LocMaxRSL_Type = Integer32
_LocMaxRSL_Object = MibScalar
locMaxRSL = _LocMaxRSL_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 12),
    _LocMaxRSL_Type()
)
locMaxRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMaxRSL.setStatus("current")
if mibBuilder.loadTexts:
    locMaxRSL.setUnits("dBm")
_LocMaxRSLstr_Type = DisplayString
_LocMaxRSLstr_Object = MibScalar
locMaxRSLstr = _LocMaxRSLstr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 13),
    _LocMaxRSLstr_Type()
)
locMaxRSLstr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMaxRSLstr.setStatus("current")
if mibBuilder.loadTexts:
    locMaxRSLstr.setUnits("dBm")
_LocSampleDuration_Type = Integer32
_LocSampleDuration_Object = MibScalar
locSampleDuration = _LocSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 14),
    _LocSampleDuration_Type()
)
locSampleDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locSampleDuration.setStatus("current")
if mibBuilder.loadTexts:
    locSampleDuration.setUnits("Seconds")
_LocSampleDurationStr_Type = DisplayString
_LocSampleDurationStr_Object = MibScalar
locSampleDurationStr = _LocSampleDurationStr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 15),
    _LocSampleDurationStr_Type()
)
locSampleDurationStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locSampleDurationStr.setStatus("current")
_LocEthPerfInterfaces_Object = MibTable
locEthPerfInterfaces = _LocEthPerfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 16)
)
if mibBuilder.loadTexts:
    locEthPerfInterfaces.setStatus("current")
_LocEthPerfInterfacesEntry_Object = MibTableRow
locEthPerfInterfacesEntry = _LocEthPerfInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 16, 1)
)
locEthPerfInterfacesEntry.setIndexNames(
    (0, "ExaltComProducts", "locEthUtilizationIn"),
    (0, "ExaltComProducts", "locEthUtilizationOut"),
)
if mibBuilder.loadTexts:
    locEthPerfInterfacesEntry.setStatus("current")


class _LocEthUtilizationIn_Type(Integer32):
    """Custom type locEthUtilizationIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LocEthUtilizationIn_Type.__name__ = "Integer32"
_LocEthUtilizationIn_Object = MibTableColumn
locEthUtilizationIn = _LocEthUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 16, 1, 1),
    _LocEthUtilizationIn_Type()
)
locEthUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locEthUtilizationIn.setStatus("current")


class _LocEthUtilizationOut_Type(Integer32):
    """Custom type locEthUtilizationOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LocEthUtilizationOut_Type.__name__ = "Integer32"
_LocEthUtilizationOut_Object = MibTableColumn
locEthUtilizationOut = _LocEthUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 16, 1, 2),
    _LocEthUtilizationOut_Type()
)
locEthUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locEthUtilizationOut.setStatus("current")
_LocEthUtilizationWatermarkEnabled_Type = ExaltEnableT
_LocEthUtilizationWatermarkEnabled_Object = MibScalar
locEthUtilizationWatermarkEnabled = _LocEthUtilizationWatermarkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 17),
    _LocEthUtilizationWatermarkEnabled_Type()
)
locEthUtilizationWatermarkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locEthUtilizationWatermarkEnabled.setStatus("current")


class _LocEthUtilizationWatermark_Type(Integer32):
    """Custom type locEthUtilizationWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LocEthUtilizationWatermark_Type.__name__ = "Integer32"
_LocEthUtilizationWatermark_Object = MibScalar
locEthUtilizationWatermark = _LocEthUtilizationWatermark_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 18),
    _LocEthUtilizationWatermark_Type()
)
locEthUtilizationWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locEthUtilizationWatermark.setStatus("current")
_LocEthUtilizationWatermarkTrapEnabled_Type = ExaltEnableT
_LocEthUtilizationWatermarkTrapEnabled_Object = MibScalar
locEthUtilizationWatermarkTrapEnabled = _LocEthUtilizationWatermarkTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 19),
    _LocEthUtilizationWatermarkTrapEnabled_Type()
)
locEthUtilizationWatermarkTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locEthUtilizationWatermarkTrapEnabled.setStatus("current")


class _LocEthUtilizationWatermarkTrapDuration_Type(Integer32):
    """Custom type locEthUtilizationWatermarkTrapDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_LocEthUtilizationWatermarkTrapDuration_Type.__name__ = "Integer32"
_LocEthUtilizationWatermarkTrapDuration_Object = MibScalar
locEthUtilizationWatermarkTrapDuration = _LocEthUtilizationWatermarkTrapDuration_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 20),
    _LocEthUtilizationWatermarkTrapDuration_Type()
)
locEthUtilizationWatermarkTrapDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locEthUtilizationWatermarkTrapDuration.setStatus("current")
_LocMaximumTxModulation_Type = AcmModulationT
_LocMaximumTxModulation_Object = MibScalar
locMaximumTxModulation = _LocMaximumTxModulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 100),
    _LocMaximumTxModulation_Type()
)
locMaximumTxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMaximumTxModulation.setStatus("current")
_LocActiveTxModulation_Type = AcmModulationT
_LocActiveTxModulation_Object = MibScalar
locActiveTxModulation = _LocActiveTxModulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 101),
    _LocActiveTxModulation_Type()
)
locActiveTxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locActiveTxModulation.setStatus("current")
_LocMinimumTxModulation_Type = AcmModulationT
_LocMinimumTxModulation_Object = MibScalar
locMinimumTxModulation = _LocMinimumTxModulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 102),
    _LocMinimumTxModulation_Type()
)
locMinimumTxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMinimumTxModulation.setStatus("current")
_LocMaximumRxModulation_Type = AcmModulationT
_LocMaximumRxModulation_Object = MibScalar
locMaximumRxModulation = _LocMaximumRxModulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 103),
    _LocMaximumRxModulation_Type()
)
locMaximumRxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMaximumRxModulation.setStatus("current")
_LocActiveRxModulation_Type = AcmModulationT
_LocActiveRxModulation_Object = MibScalar
locActiveRxModulation = _LocActiveRxModulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 104),
    _LocActiveRxModulation_Type()
)
locActiveRxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locActiveRxModulation.setStatus("current")
_LocMinimumRxModulation_Type = AcmModulationT
_LocMinimumRxModulation_Object = MibScalar
locMinimumRxModulation = _LocMinimumRxModulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 105),
    _LocMinimumRxModulation_Type()
)
locMinimumRxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMinimumRxModulation.setStatus("current")
_LocMaximumTxEthernetThroughput_Type = Integer32
_LocMaximumTxEthernetThroughput_Object = MibScalar
locMaximumTxEthernetThroughput = _LocMaximumTxEthernetThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 106),
    _LocMaximumTxEthernetThroughput_Type()
)
locMaximumTxEthernetThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMaximumTxEthernetThroughput.setStatus("current")
_LocActiveTxEthernetThroughput_Type = Integer32
_LocActiveTxEthernetThroughput_Object = MibScalar
locActiveTxEthernetThroughput = _LocActiveTxEthernetThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 107),
    _LocActiveTxEthernetThroughput_Type()
)
locActiveTxEthernetThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locActiveTxEthernetThroughput.setStatus("current")
_LocMinimumTxEthernetThroughput_Type = Integer32
_LocMinimumTxEthernetThroughput_Object = MibScalar
locMinimumTxEthernetThroughput = _LocMinimumTxEthernetThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 108),
    _LocMinimumTxEthernetThroughput_Type()
)
locMinimumTxEthernetThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMinimumTxEthernetThroughput.setStatus("current")
_LocMaximumRxEthernetThroughput_Type = Integer32
_LocMaximumRxEthernetThroughput_Object = MibScalar
locMaximumRxEthernetThroughput = _LocMaximumRxEthernetThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 109),
    _LocMaximumRxEthernetThroughput_Type()
)
locMaximumRxEthernetThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMaximumRxEthernetThroughput.setStatus("current")
_LocActiveRxEthernetThroughput_Type = Integer32
_LocActiveRxEthernetThroughput_Object = MibScalar
locActiveRxEthernetThroughput = _LocActiveRxEthernetThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 110),
    _LocActiveRxEthernetThroughput_Type()
)
locActiveRxEthernetThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locActiveRxEthernetThroughput.setStatus("current")
_LocMinimumRxEthernetThroughput_Type = Integer32
_LocMinimumRxEthernetThroughput_Object = MibScalar
locMinimumRxEthernetThroughput = _LocMinimumRxEthernetThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 111),
    _LocMinimumRxEthernetThroughput_Type()
)
locMinimumRxEthernetThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locMinimumRxEthernetThroughput.setStatus("current")
_LocResetStats_Type = DisplayString
_LocResetStats_Object = MibScalar
locResetStats = _LocResetStats_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 1, 1000),
    _LocResetStats_Type()
)
locResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locResetStats.setStatus("current")
_PerfRemote_ObjectIdentity = ObjectIdentity
perfRemote = _PerfRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2)
)
_RemCurrentBER_Type = Integer32
_RemCurrentBER_Object = MibScalar
remCurrentBER = _RemCurrentBER_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 1),
    _RemCurrentBER_Type()
)
remCurrentBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remCurrentBER.setStatus("current")
if mibBuilder.loadTexts:
    remCurrentBER.setUnits("BER * 1000000.0")
_RemCurrentBERstr_Type = DisplayString
_RemCurrentBERstr_Object = MibScalar
remCurrentBERstr = _RemCurrentBERstr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 2),
    _RemCurrentBERstr_Type()
)
remCurrentBERstr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remCurrentBERstr.setStatus("current")
_RemCurrentRSL_Type = Integer32
_RemCurrentRSL_Object = MibScalar
remCurrentRSL = _RemCurrentRSL_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 3),
    _RemCurrentRSL_Type()
)
remCurrentRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remCurrentRSL.setStatus("current")
if mibBuilder.loadTexts:
    remCurrentRSL.setUnits("dBm")
_RemCurrentRSLstr_Type = DisplayString
_RemCurrentRSLstr_Object = MibScalar
remCurrentRSLstr = _RemCurrentRSLstr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 4),
    _RemCurrentRSLstr_Type()
)
remCurrentRSLstr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remCurrentRSLstr.setStatus("current")
_RemErrorDuration_Type = Integer32
_RemErrorDuration_Object = MibScalar
remErrorDuration = _RemErrorDuration_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 5),
    _RemErrorDuration_Type()
)
remErrorDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remErrorDuration.setStatus("current")
if mibBuilder.loadTexts:
    remErrorDuration.setUnits("Seconds")
_RemErrorDurationStr_Type = DisplayString
_RemErrorDurationStr_Object = MibScalar
remErrorDurationStr = _RemErrorDurationStr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 6),
    _RemErrorDurationStr_Type()
)
remErrorDurationStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remErrorDurationStr.setStatus("current")
_RemUnavailDuration_Type = Integer32
_RemUnavailDuration_Object = MibScalar
remUnavailDuration = _RemUnavailDuration_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 7),
    _RemUnavailDuration_Type()
)
remUnavailDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remUnavailDuration.setStatus("current")
if mibBuilder.loadTexts:
    remUnavailDuration.setUnits("Seconds")
_RemUnavailDurationStr_Type = DisplayString
_RemUnavailDurationStr_Object = MibScalar
remUnavailDurationStr = _RemUnavailDurationStr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 8),
    _RemUnavailDurationStr_Type()
)
remUnavailDurationStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remUnavailDurationStr.setStatus("current")
_RemMinRSL_Type = Integer32
_RemMinRSL_Object = MibScalar
remMinRSL = _RemMinRSL_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 9),
    _RemMinRSL_Type()
)
remMinRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remMinRSL.setStatus("current")
if mibBuilder.loadTexts:
    remMinRSL.setUnits("dBm")
_RemMinRSLstr_Type = DisplayString
_RemMinRSLstr_Object = MibScalar
remMinRSLstr = _RemMinRSLstr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 10),
    _RemMinRSLstr_Type()
)
remMinRSLstr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remMinRSLstr.setStatus("current")
_RemMinRSLtimestamp_Type = DisplayString
_RemMinRSLtimestamp_Object = MibScalar
remMinRSLtimestamp = _RemMinRSLtimestamp_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 11),
    _RemMinRSLtimestamp_Type()
)
remMinRSLtimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remMinRSLtimestamp.setStatus("current")
_RemMaxRSL_Type = Integer32
_RemMaxRSL_Object = MibScalar
remMaxRSL = _RemMaxRSL_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 12),
    _RemMaxRSL_Type()
)
remMaxRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remMaxRSL.setStatus("current")
if mibBuilder.loadTexts:
    remMaxRSL.setUnits("dBm")
_RemMaxRSLstr_Type = DisplayString
_RemMaxRSLstr_Object = MibScalar
remMaxRSLstr = _RemMaxRSLstr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 13),
    _RemMaxRSLstr_Type()
)
remMaxRSLstr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remMaxRSLstr.setStatus("current")
if mibBuilder.loadTexts:
    remMaxRSLstr.setUnits("dBm")
_RemSampleDuration_Type = Integer32
_RemSampleDuration_Object = MibScalar
remSampleDuration = _RemSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 14),
    _RemSampleDuration_Type()
)
remSampleDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remSampleDuration.setStatus("current")
if mibBuilder.loadTexts:
    remSampleDuration.setUnits("Seconds")
_RemSampleDurationStr_Type = DisplayString
_RemSampleDurationStr_Object = MibScalar
remSampleDurationStr = _RemSampleDurationStr_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 15),
    _RemSampleDurationStr_Type()
)
remSampleDurationStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remSampleDurationStr.setStatus("current")
_RemResetStats_Type = DisplayString
_RemResetStats_Object = MibScalar
remResetStats = _RemResetStats_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 3, 2, 1000),
    _RemResetStats_Type()
)
remResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remResetStats.setStatus("current")
_UserThroughput_ObjectIdentity = ObjectIdentity
userThroughput = _UserThroughput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 5)
)
_AggregateUserThroughput_Type = DisplayString
_AggregateUserThroughput_Object = MibScalar
aggregateUserThroughput = _AggregateUserThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 5, 1),
    _AggregateUserThroughput_Type()
)
aggregateUserThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregateUserThroughput.setStatus("current")
if mibBuilder.loadTexts:
    aggregateUserThroughput.setUnits("MBit/s")
_InboundEthernetThroughput_Type = DisplayString
_InboundEthernetThroughput_Object = MibScalar
inboundEthernetThroughput = _InboundEthernetThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 5, 2),
    _InboundEthernetThroughput_Type()
)
inboundEthernetThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundEthernetThroughput.setStatus("current")
if mibBuilder.loadTexts:
    inboundEthernetThroughput.setUnits("MBit/s")
_OutboundEthernetThroughput_Type = DisplayString
_OutboundEthernetThroughput_Object = MibScalar
outboundEthernetThroughput = _OutboundEthernetThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 5, 3),
    _OutboundEthernetThroughput_Type()
)
outboundEthernetThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundEthernetThroughput.setStatus("current")
if mibBuilder.loadTexts:
    outboundEthernetThroughput.setUnits("MBit/s")
_FullDuplexEthernetThroughput_Type = DisplayString
_FullDuplexEthernetThroughput_Object = MibScalar
fullDuplexEthernetThroughput = _FullDuplexEthernetThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 5, 4),
    _FullDuplexEthernetThroughput_Type()
)
fullDuplexEthernetThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fullDuplexEthernetThroughput.setStatus("current")
if mibBuilder.loadTexts:
    fullDuplexEthernetThroughput.setUnits("MBit/s")


class _RadioReboot_Type(DisplayString):
    """Custom type radioReboot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RadioReboot_Type.__name__ = "DisplayString"
_RadioReboot_Object = MibScalar
radioReboot = _RadioReboot_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 1000),
    _RadioReboot_Type()
)
radioReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioReboot.setStatus("current")
_ProductsMIBConformance_ObjectIdentity = ObjectIdentity
productsMIBConformance = _ProductsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 3)
)
_ProductsMIBCompliances_ObjectIdentity = ObjectIdentity
productsMIBCompliances = _ProductsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 3, 1)
)
_ProductsMIBGroups_ObjectIdentity = ObjectIdentity
productsMIBGroups = _ProductsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 3, 2)
)

# Managed Objects groups

productsAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25651, 1, 3, 2, 1)
)
productsAllObjects.setObjects(
      *(("ExaltComProducts", "modelName"),
        ("ExaltComProducts", "partNumber"),
        ("ExaltComProducts", "serialNumber"),
        ("ExaltComProducts", "interfaceType"),
        ("ExaltComProducts", "firmwareVersion"),
        ("ExaltComProducts", "bootVersion"),
        ("ExaltComProducts", "rfFreqBand"),
        ("ExaltComProducts", "sysDate"),
        ("ExaltComProducts", "sysTime"),
        ("ExaltComProducts", "rnLocal"),
        ("ExaltComProducts", "rnRemote"),
        ("ExaltComProducts", "linkName"),
        ("ExaltComProducts", "linkSecKey"),
        ("ExaltComProducts", "adminPassword"),
        ("ExaltComProducts", "userPassword"),
        ("ExaltComProducts", "ipLocal"),
        ("ExaltComProducts", "ipRemote"),
        ("ExaltComProducts", "subnetMask"),
        ("ExaltComProducts", "ipAddressNetmask"),
        ("ExaltComProducts", "defaultGateway"),
        ("ExaltComProducts", "commitAdminSettings"),
        ("ExaltComProducts", "te1NumChannels"),
        ("ExaltComProducts", "te1NumActiveChannels"),
        ("ExaltComProducts", "selectT1orE1"),
        ("ExaltComProducts", "commitTe1Settings"),
        ("ExaltComProducts", "currentFwFilename"),
        ("ExaltComProducts", "alternateFwFilename"),
        ("ExaltComProducts", "swapFWimage"),
        ("ExaltComProducts", "locLinkState"),
        ("ExaltComProducts", "locLinkStateV"),
        ("ExaltComProducts", "locLinkStateH"),
        ("ExaltComProducts", "locTe1LinkSummary"),
        ("ExaltComProducts", "locTempAlarm"),
        ("ExaltComProducts", "locCurrentTemp"),
        ("ExaltComProducts", "locCurrentTempS"),
        ("ExaltComProducts", "locLinkSecMismatch"),
        ("ExaltComProducts", "remLinkState"),
        ("ExaltComProducts", "remLinkStateV"),
        ("ExaltComProducts", "remLinkStateH"),
        ("ExaltComProducts", "remTe1LinkSummary"),
        ("ExaltComProducts", "remTempAlarm"),
        ("ExaltComProducts", "remCurrentTemp"),
        ("ExaltComProducts", "remCurrentTempS"),
        ("ExaltComProducts", "remLinkSecMismatch"),
        ("ExaltComProducts", "locCurrentBER"),
        ("ExaltComProducts", "locCurrentBERstr"),
        ("ExaltComProducts", "locCurrentRSL"),
        ("ExaltComProducts", "locCurrentRSLstr"),
        ("ExaltComProducts", "locErrorDuration"),
        ("ExaltComProducts", "locErrorDurationStr"),
        ("ExaltComProducts", "locUnavailDuration"),
        ("ExaltComProducts", "locUnavailDurationStr"),
        ("ExaltComProducts", "locMinRSL"),
        ("ExaltComProducts", "locMinRSLstr"),
        ("ExaltComProducts", "locMinRSLtimestamp"),
        ("ExaltComProducts", "locMaxRSL"),
        ("ExaltComProducts", "locMaxRSLstr"),
        ("ExaltComProducts", "locSampleDuration"),
        ("ExaltComProducts", "locSampleDurationStr"),
        ("ExaltComProducts", "locResetStats"),
        ("ExaltComProducts", "remCurrentBER"),
        ("ExaltComProducts", "remCurrentBERstr"),
        ("ExaltComProducts", "remCurrentRSL"),
        ("ExaltComProducts", "remCurrentRSLstr"),
        ("ExaltComProducts", "remErrorDuration"),
        ("ExaltComProducts", "remErrorDurationStr"),
        ("ExaltComProducts", "remUnavailDuration"),
        ("ExaltComProducts", "remUnavailDurationStr"),
        ("ExaltComProducts", "remMinRSL"),
        ("ExaltComProducts", "remMinRSLstr"),
        ("ExaltComProducts", "remMinRSLtimestamp"),
        ("ExaltComProducts", "remMaxRSL"),
        ("ExaltComProducts", "remMaxRSLstr"),
        ("ExaltComProducts", "remSampleDuration"),
        ("ExaltComProducts", "remSampleDurationStr"),
        ("ExaltComProducts", "remResetStats"),
        ("ExaltComProducts", "radioReboot"),
        ("ExaltComProducts", "te1Status"),
        ("ExaltComProducts", "t1LBO"),
        ("ExaltComProducts", "te1AIS"),
        ("ExaltComProducts", "t1LineCode"),
        ("ExaltComProducts", "te1LoopBackMode"),
        ("ExaltComProducts", "locTe1Alarm"),
        ("ExaltComProducts", "remTe1Alarm"),
        ("ExaltComProducts", "aesEnable"),
        ("ExaltComProducts", "licKey"),
        ("ExaltComProducts", "aggregateUserThroughput"),
        ("ExaltComProducts", "inboundEthernetThroughput"),
        ("ExaltComProducts", "outboundEthernetThroughput"),
        ("ExaltComProducts", "fullDuplexEthernetThroughput"),
        ("ExaltComProducts", "locEthUtilizationIn"),
        ("ExaltComProducts", "locEthUtilizationOut"),
        ("ExaltComProducts", "locEthUtilizationWatermarkEnabled"),
        ("ExaltComProducts", "locEthUtilizationWatermark"),
        ("ExaltComProducts", "locEthUtilizationWatermarkTrapEnabled"),
        ("ExaltComProducts", "locEthUtilizationWatermarkTrapDuration"))
)
if mibBuilder.loadTexts:
    productsAllObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ExaltComProducts",
    **{"PwType": PwType,
       "productsMIB": productsMIB,
       "productsMIBNotifications": productsMIBNotifications,
       "productsMIBObjects": productsMIBObjects,
       "radioInfo": radioInfo,
       "modelName": modelName,
       "partNumber": partNumber,
       "serialNumber": serialNumber,
       "interfaceType": interfaceType,
       "firmwareVersion": firmwareVersion,
       "bootVersion": bootVersion,
       "rdkDbVer": rdkDbVer,
       "txFreqRange": txFreqRange,
       "rxFreqRange": rxFreqRange,
       "rfFreqBand": rfFreqBand,
       "hwId": hwId,
       "modelNumber": modelNumber,
       "radioAdmin": radioAdmin,
       "sysDate": sysDate,
       "sysTime": sysTime,
       "radioName": radioName,
       "rnLocal": rnLocal,
       "rnRemote": rnRemote,
       "linkName": linkName,
       "linkSecKey": linkSecKey,
       "adminPassword": adminPassword,
       "userPassword": userPassword,
       "ipAddress": ipAddress,
       "ipLocal": ipLocal,
       "ipRemote": ipRemote,
       "subnetMask": subnetMask,
       "ipAddressNetmask": ipAddressNetmask,
       "defaultGateway": defaultGateway,
       "aesEnable": aesEnable,
       "aesKey": aesKey,
       "licKey": licKey,
       "snmpConfig": snmpConfig,
       "trapIpaddr": trapIpaddr,
       "trapAuth": trapAuth,
       "trapReboot": trapReboot,
       "trapLocLinkStat": trapLocLinkStat,
       "trapLocAlarmStat": trapLocAlarmStat,
       "trapRemAlarmStat": trapRemAlarmStat,
       "trapLocRslStat": trapLocRslStat,
       "trapLocTempStat": trapLocTempStat,
       "trapLocRslThreshold": trapLocRslThreshold,
       "trapv1Enable": trapv1Enable,
       "trapv2cEnable": trapv2cEnable,
       "trapv3Enable": trapv3Enable,
       "ntp": ntp,
       "ntpClientEnable": ntpClientEnable,
       "ntpServer1IpAddr": ntpServer1IpAddr,
       "ntpServer2IpAddr": ntpServer2IpAddr,
       "ntpServer3IpAddr": ntpServer3IpAddr,
       "ntpServer4IpAddr": ntpServer4IpAddr,
       "ntpTimeZoneSelect": ntpTimeZoneSelect,
       "commitNtpSettings": commitNtpSettings,
       "commitAdminSettings": commitAdminSettings,
       "radioConfig": radioConfig,
       "systemConfig": systemConfig,
       "commitSystemSettings": commitSystemSettings,
       "interface": interface,
       "te1": te1,
       "te1NumChannels": te1NumChannels,
       "te1NumActiveChannels": te1NumActiveChannels,
       "selectT1orE1": selectT1orE1,
       "te1Interfaces": te1Interfaces,
       "te1Interface": te1Interface,
       "te1Status": te1Status,
       "t1LBO": t1LBO,
       "te1AIS": te1AIS,
       "t1LineCode": t1LineCode,
       "te1LoopBackMode": te1LoopBackMode,
       "commitTe1Settings": commitTe1Settings,
       "fileManagement": fileManagement,
       "currentFwFilename": currentFwFilename,
       "alternateFwFilename": alternateFwFilename,
       "swapFWimage": swapFWimage,
       "fileTransfer": fileTransfer,
       "tftpServerIp": tftpServerIp,
       "uploadFilename": uploadFilename,
       "transferType": transferType,
       "transferStart": transferStart,
       "transferStatus": transferStatus,
       "factoryFwFilename": factoryFwFilename,
       "radioMonitor": radioMonitor,
       "alarms": alarms,
       "almLocal": almLocal,
       "locSysAlarms": locSysAlarms,
       "locLinkState": locLinkState,
       "locTempAlarm": locTempAlarm,
       "locCurrentTemp": locCurrentTemp,
       "locCurrentTempS": locCurrentTempS,
       "locLinkSecMismatch": locLinkSecMismatch,
       "locLinkStateV": locLinkStateV,
       "locLinkStateH": locLinkStateH,
       "locEthAlarms": locEthAlarms,
       "locTe1Alarms": locTe1Alarms,
       "locTe1LinkSummary": locTe1LinkSummary,
       "locTE1Alarms": locTE1Alarms,
       "locTe1AlarmsEntry": locTe1AlarmsEntry,
       "locTe1Alarm": locTe1Alarm,
       "almRemote": almRemote,
       "remSysAlarms": remSysAlarms,
       "remLinkState": remLinkState,
       "remTempAlarm": remTempAlarm,
       "remCurrentTemp": remCurrentTemp,
       "remCurrentTempS": remCurrentTempS,
       "remLinkSecMismatch": remLinkSecMismatch,
       "remLinkStateV": remLinkStateV,
       "remLinkStateH": remLinkStateH,
       "remEthAlarms": remEthAlarms,
       "remTe1Alarms": remTe1Alarms,
       "remTe1LinkSummary": remTe1LinkSummary,
       "remTE1Alarms": remTE1Alarms,
       "remTe1AlarmsEntry": remTe1AlarmsEntry,
       "remTe1Alarm": remTe1Alarm,
       "performance": performance,
       "perfLocal": perfLocal,
       "locCurrentBER": locCurrentBER,
       "locCurrentBERstr": locCurrentBERstr,
       "locCurrentRSL": locCurrentRSL,
       "locCurrentRSLstr": locCurrentRSLstr,
       "locErrorDuration": locErrorDuration,
       "locErrorDurationStr": locErrorDurationStr,
       "locUnavailDuration": locUnavailDuration,
       "locUnavailDurationStr": locUnavailDurationStr,
       "locMinRSL": locMinRSL,
       "locMinRSLstr": locMinRSLstr,
       "locMinRSLtimestamp": locMinRSLtimestamp,
       "locMaxRSL": locMaxRSL,
       "locMaxRSLstr": locMaxRSLstr,
       "locSampleDuration": locSampleDuration,
       "locSampleDurationStr": locSampleDurationStr,
       "locEthPerfInterfaces": locEthPerfInterfaces,
       "locEthPerfInterfacesEntry": locEthPerfInterfacesEntry,
       "locEthUtilizationIn": locEthUtilizationIn,
       "locEthUtilizationOut": locEthUtilizationOut,
       "locEthUtilizationWatermarkEnabled": locEthUtilizationWatermarkEnabled,
       "locEthUtilizationWatermark": locEthUtilizationWatermark,
       "locEthUtilizationWatermarkTrapEnabled": locEthUtilizationWatermarkTrapEnabled,
       "locEthUtilizationWatermarkTrapDuration": locEthUtilizationWatermarkTrapDuration,
       "locMaximumTxModulation": locMaximumTxModulation,
       "locActiveTxModulation": locActiveTxModulation,
       "locMinimumTxModulation": locMinimumTxModulation,
       "locMaximumRxModulation": locMaximumRxModulation,
       "locActiveRxModulation": locActiveRxModulation,
       "locMinimumRxModulation": locMinimumRxModulation,
       "locMaximumTxEthernetThroughput": locMaximumTxEthernetThroughput,
       "locActiveTxEthernetThroughput": locActiveTxEthernetThroughput,
       "locMinimumTxEthernetThroughput": locMinimumTxEthernetThroughput,
       "locMaximumRxEthernetThroughput": locMaximumRxEthernetThroughput,
       "locActiveRxEthernetThroughput": locActiveRxEthernetThroughput,
       "locMinimumRxEthernetThroughput": locMinimumRxEthernetThroughput,
       "locResetStats": locResetStats,
       "perfRemote": perfRemote,
       "remCurrentBER": remCurrentBER,
       "remCurrentBERstr": remCurrentBERstr,
       "remCurrentRSL": remCurrentRSL,
       "remCurrentRSLstr": remCurrentRSLstr,
       "remErrorDuration": remErrorDuration,
       "remErrorDurationStr": remErrorDurationStr,
       "remUnavailDuration": remUnavailDuration,
       "remUnavailDurationStr": remUnavailDurationStr,
       "remMinRSL": remMinRSL,
       "remMinRSLstr": remMinRSLstr,
       "remMinRSLtimestamp": remMinRSLtimestamp,
       "remMaxRSL": remMaxRSL,
       "remMaxRSLstr": remMaxRSLstr,
       "remSampleDuration": remSampleDuration,
       "remSampleDurationStr": remSampleDurationStr,
       "remResetStats": remResetStats,
       "userThroughput": userThroughput,
       "aggregateUserThroughput": aggregateUserThroughput,
       "inboundEthernetThroughput": inboundEthernetThroughput,
       "outboundEthernetThroughput": outboundEthernetThroughput,
       "fullDuplexEthernetThroughput": fullDuplexEthernetThroughput,
       "radioReboot": radioReboot,
       "productsMIBConformance": productsMIBConformance,
       "productsMIBCompliances": productsMIBCompliances,
       "productsMIBGroups": productsMIBGroups,
       "productsAllObjects": productsAllObjects}
)

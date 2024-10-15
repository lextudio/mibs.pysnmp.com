# SNMP MIB module (ZYXEL-SYSTEM-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-SYSTEM-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:54 2024
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelSysMgmt_ObjectIdentity = ObjectIdentity
zyxelSysMgmt = _ZyxelSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1)
)


class _ZySysMgmtConfigSave_Type(Integer32):
    """Custom type zySysMgmtConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_ZySysMgmtConfigSave_Type.__name__ = "Integer32"
_ZySysMgmtConfigSave_Object = MibScalar
zySysMgmtConfigSave = _ZySysMgmtConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 1),
    _ZySysMgmtConfigSave_Type()
)
zySysMgmtConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtConfigSave.setStatus("current")


class _ZySysMgmtBootupConfig_Type(Integer32):
    """Custom type zySysMgmtBootupConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_ZySysMgmtBootupConfig_Type.__name__ = "Integer32"
_ZySysMgmtBootupConfig_Object = MibScalar
zySysMgmtBootupConfig = _ZySysMgmtBootupConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 2),
    _ZySysMgmtBootupConfig_Type()
)
zySysMgmtBootupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtBootupConfig.setStatus("current")


class _ZySysMgmtReboot_Type(Integer32):
    """Custom type zySysMgmtReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reboot", 1))
    )


_ZySysMgmtReboot_Type.__name__ = "Integer32"
_ZySysMgmtReboot_Object = MibScalar
zySysMgmtReboot = _ZySysMgmtReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 3),
    _ZySysMgmtReboot_Type()
)
zySysMgmtReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtReboot.setStatus("current")


class _ZySysMgmtDefaultConfig_Type(Integer32):
    """Custom type zySysMgmtDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("resetToDefault", 1))
    )


_ZySysMgmtDefaultConfig_Type.__name__ = "Integer32"
_ZySysMgmtDefaultConfig_Object = MibScalar
zySysMgmtDefaultConfig = _ZySysMgmtDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 4),
    _ZySysMgmtDefaultConfig_Type()
)
zySysMgmtDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtDefaultConfig.setStatus("current")


class _ZySysMgmtLastActionStatus_Type(Integer32):
    """Custom type zySysMgmtLastActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("none", 0),
          ("success", 1))
    )


_ZySysMgmtLastActionStatus_Type.__name__ = "Integer32"
_ZySysMgmtLastActionStatus_Object = MibScalar
zySysMgmtLastActionStatus = _ZySysMgmtLastActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 5),
    _ZySysMgmtLastActionStatus_Type()
)
zySysMgmtLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMgmtLastActionStatus.setStatus("current")


class _ZySysMgmtSysStatus_Type(Bits):
    """Custom type zySysMgmtSysStatus based on Bits"""
    namedValues = NamedValues(
        *(("sysAlarmDetected", 0),
          ("sysFanRPMError", 2),
          ("sysNoDefect", 4),
          ("sysTemperatureError", 1),
          ("sysVoltageRangeError", 3))
    )

_ZySysMgmtSysStatus_Type.__name__ = "Bits"
_ZySysMgmtSysStatus_Object = MibScalar
zySysMgmtSysStatus = _ZySysMgmtSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 6),
    _ZySysMgmtSysStatus_Type()
)
zySysMgmtSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMgmtSysStatus.setStatus("current")
_ZySysMgmtCPUUsage_Type = Integer32
_ZySysMgmtCPUUsage_Object = MibScalar
zySysMgmtCPUUsage = _ZySysMgmtCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 7),
    _ZySysMgmtCPUUsage_Type()
)
zySysMgmtCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMgmtCPUUsage.setStatus("current")


class _ZySysMgmtBootupImage_Type(Integer32):
    """Custom type zySysMgmtBootupImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )


_ZySysMgmtBootupImage_Type.__name__ = "Integer32"
_ZySysMgmtBootupImage_Object = MibScalar
zySysMgmtBootupImage = _ZySysMgmtBootupImage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 8),
    _ZySysMgmtBootupImage_Type()
)
zySysMgmtBootupImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtBootupImage.setStatus("current")


class _ZySysMgmtCounterReset_Type(Integer32):
    """Custom type zySysMgmtCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ZySysMgmtCounterReset_Type.__name__ = "Integer32"
_ZySysMgmtCounterReset_Object = MibScalar
zySysMgmtCounterReset = _ZySysMgmtCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 9),
    _ZySysMgmtCounterReset_Type()
)
zySysMgmtCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtCounterReset.setStatus("current")
_ZyxelSysMgmtTftpServiceSetup_ObjectIdentity = ObjectIdentity
zyxelSysMgmtTftpServiceSetup = _ZyxelSysMgmtTftpServiceSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10)
)
_ZySysMgmtTftpServiceServerIpAddress_Type = IpAddress
_ZySysMgmtTftpServiceServerIpAddress_Object = MibScalar
zySysMgmtTftpServiceServerIpAddress = _ZySysMgmtTftpServiceServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 1),
    _ZySysMgmtTftpServiceServerIpAddress_Type()
)
zySysMgmtTftpServiceServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtTftpServiceServerIpAddress.setStatus("current")
_ZySysMgmtTftpRemoteFileName_Type = DisplayString
_ZySysMgmtTftpRemoteFileName_Object = MibScalar
zySysMgmtTftpRemoteFileName = _ZySysMgmtTftpRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 2),
    _ZySysMgmtTftpRemoteFileName_Type()
)
zySysMgmtTftpRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtTftpRemoteFileName.setStatus("current")


class _ZySysMgmtTftpConfigIndex_Type(Integer32):
    """Custom type zySysMgmtTftpConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_ZySysMgmtTftpConfigIndex_Type.__name__ = "Integer32"
_ZySysMgmtTftpConfigIndex_Object = MibScalar
zySysMgmtTftpConfigIndex = _ZySysMgmtTftpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 3),
    _ZySysMgmtTftpConfigIndex_Type()
)
zySysMgmtTftpConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtTftpConfigIndex.setStatus("current")


class _ZySysMgmtTftpAction_Type(Integer32):
    """Custom type zySysMgmtTftpAction based on Integer32"""
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
        *(("backupConfig", 1),
          ("mergeConfig", 3),
          ("none", 0),
          ("restoreConfig", 2))
    )


_ZySysMgmtTftpAction_Type.__name__ = "Integer32"
_ZySysMgmtTftpAction_Object = MibScalar
zySysMgmtTftpAction = _ZySysMgmtTftpAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 4),
    _ZySysMgmtTftpAction_Type()
)
zySysMgmtTftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtTftpAction.setStatus("current")


class _ZySysMgmtTftpActionStatus_Type(Integer32):
    """Custom type zySysMgmtTftpActionStatus based on Integer32"""
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
        *(("fail", 2),
          ("none", 0),
          ("success", 1),
          ("underAction", 3))
    )


_ZySysMgmtTftpActionStatus_Type.__name__ = "Integer32"
_ZySysMgmtTftpActionStatus_Object = MibScalar
zySysMgmtTftpActionStatus = _ZySysMgmtTftpActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 5),
    _ZySysMgmtTftpActionStatus_Type()
)
zySysMgmtTftpActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMgmtTftpActionStatus.setStatus("current")


class _ZySysMgmtTftpActionPrivilege13_Type(Integer32):
    """Custom type zySysMgmtTftpActionPrivilege13 based on Integer32"""
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
        *(("backupConfig", 1),
          ("mergeConfig", 3),
          ("none", 0),
          ("restoreConfig", 2))
    )


_ZySysMgmtTftpActionPrivilege13_Type.__name__ = "Integer32"
_ZySysMgmtTftpActionPrivilege13_Object = MibScalar
zySysMgmtTftpActionPrivilege13 = _ZySysMgmtTftpActionPrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 113),
    _ZySysMgmtTftpActionPrivilege13_Type()
)
zySysMgmtTftpActionPrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtTftpActionPrivilege13.setStatus("current")


class _ZySysMgmtReloadFactoryDefault_Type(Integer32):
    """Custom type zySysMgmtReloadFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reloadFactoryDefault", 1))
    )


_ZySysMgmtReloadFactoryDefault_Type.__name__ = "Integer32"
_ZySysMgmtReloadFactoryDefault_Object = MibScalar
zySysMgmtReloadFactoryDefault = _ZySysMgmtReloadFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 11),
    _ZySysMgmtReloadFactoryDefault_Type()
)
zySysMgmtReloadFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtReloadFactoryDefault.setStatus("current")


class _ZySysMgmtReloadStackingDefault_Type(Integer32):
    """Custom type zySysMgmtReloadStackingDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reloadStackingDefault", 1))
    )


_ZySysMgmtReloadStackingDefault_Type.__name__ = "Integer32"
_ZySysMgmtReloadStackingDefault_Object = MibScalar
zySysMgmtReloadStackingDefault = _ZySysMgmtReloadStackingDefault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 12),
    _ZySysMgmtReloadStackingDefault_Type()
)
zySysMgmtReloadStackingDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtReloadStackingDefault.setStatus("current")


class _ZySysMgmtConfigSavePrivilege13_Type(Integer32):
    """Custom type zySysMgmtConfigSavePrivilege13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_ZySysMgmtConfigSavePrivilege13_Type.__name__ = "Integer32"
_ZySysMgmtConfigSavePrivilege13_Object = MibScalar
zySysMgmtConfigSavePrivilege13 = _ZySysMgmtConfigSavePrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 113),
    _ZySysMgmtConfigSavePrivilege13_Type()
)
zySysMgmtConfigSavePrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtConfigSavePrivilege13.setStatus("current")


class _ZySysMgmtDefaultConfigPrivilege13_Type(Integer32):
    """Custom type zySysMgmtDefaultConfigPrivilege13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("resetToDefault", 1))
    )


_ZySysMgmtDefaultConfigPrivilege13_Type.__name__ = "Integer32"
_ZySysMgmtDefaultConfigPrivilege13_Object = MibScalar
zySysMgmtDefaultConfigPrivilege13 = _ZySysMgmtDefaultConfigPrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 213),
    _ZySysMgmtDefaultConfigPrivilege13_Type()
)
zySysMgmtDefaultConfigPrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtDefaultConfigPrivilege13.setStatus("current")
_ZyxelSysMgmtNotifications_ObjectIdentity = ObjectIdentity
zyxelSysMgmtNotifications = _ZyxelSysMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2)
)

# Managed Objects groups


# Notification objects

zySysMgmtUncontrolledSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2, 1)
)
if mibBuilder.loadTexts:
    zySysMgmtUncontrolledSystemReset.setStatus(
        "current"
    )

zySysMgmtControlledSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2, 2)
)
if mibBuilder.loadTexts:
    zySysMgmtControlledSystemReset.setStatus(
        "current"
    )

zySysMgmtBootImageInconsistence = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2, 3)
)
if mibBuilder.loadTexts:
    zySysMgmtBootImageInconsistence.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-SYSTEM-MGMT-MIB",
    **{"zyxelManagement": zyxelManagement,
       "zyxelSysMgmt": zyxelSysMgmt,
       "zySysMgmtConfigSave": zySysMgmtConfigSave,
       "zySysMgmtBootupConfig": zySysMgmtBootupConfig,
       "zySysMgmtReboot": zySysMgmtReboot,
       "zySysMgmtDefaultConfig": zySysMgmtDefaultConfig,
       "zySysMgmtLastActionStatus": zySysMgmtLastActionStatus,
       "zySysMgmtSysStatus": zySysMgmtSysStatus,
       "zySysMgmtCPUUsage": zySysMgmtCPUUsage,
       "zySysMgmtBootupImage": zySysMgmtBootupImage,
       "zySysMgmtCounterReset": zySysMgmtCounterReset,
       "zyxelSysMgmtTftpServiceSetup": zyxelSysMgmtTftpServiceSetup,
       "zySysMgmtTftpServiceServerIpAddress": zySysMgmtTftpServiceServerIpAddress,
       "zySysMgmtTftpRemoteFileName": zySysMgmtTftpRemoteFileName,
       "zySysMgmtTftpConfigIndex": zySysMgmtTftpConfigIndex,
       "zySysMgmtTftpAction": zySysMgmtTftpAction,
       "zySysMgmtTftpActionStatus": zySysMgmtTftpActionStatus,
       "zySysMgmtTftpActionPrivilege13": zySysMgmtTftpActionPrivilege13,
       "zySysMgmtReloadFactoryDefault": zySysMgmtReloadFactoryDefault,
       "zySysMgmtReloadStackingDefault": zySysMgmtReloadStackingDefault,
       "zySysMgmtConfigSavePrivilege13": zySysMgmtConfigSavePrivilege13,
       "zySysMgmtDefaultConfigPrivilege13": zySysMgmtDefaultConfigPrivilege13,
       "zyxelSysMgmtNotifications": zyxelSysMgmtNotifications,
       "zySysMgmtUncontrolledSystemReset": zySysMgmtUncontrolledSystemReset,
       "zySysMgmtControlledSystemReset": zySysMgmtControlledSystemReset,
       "zySysMgmtBootImageInconsistence": zySysMgmtBootImageInconsistence}
)

# SNMP MIB module (NConsole-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NConsole-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:16 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Avanti_ObjectIdentity = ObjectIdentity
avanti = _Avanti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117)
)
_Nconsolemib_ObjectIdentity = ObjectIdentity
nconsolemib = _Nconsolemib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1)
)
_Serverinfo_ObjectIdentity = ObjectIdentity
serverinfo = _Serverinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1)
)


class _ServerName_Type(DisplayString):
    """Custom type serverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ServerName_Type.__name__ = "DisplayString"
_ServerName_Object = MibScalar
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 1),
    _ServerName_Type()
)
serverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverName.setStatus("mandatory")


class _ServerNwRevInfo_Type(DisplayString):
    """Custom type serverNwRevInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ServerNwRevInfo_Type.__name__ = "DisplayString"
_ServerNwRevInfo_Object = MibScalar
serverNwRevInfo = _ServerNwRevInfo_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 2),
    _ServerNwRevInfo_Type()
)
serverNwRevInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNwRevInfo.setStatus("mandatory")
_ServerNwSerialNumber_Type = Integer32
_ServerNwSerialNumber_Object = MibScalar
serverNwSerialNumber = _ServerNwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 3),
    _ServerNwSerialNumber_Type()
)
serverNwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNwSerialNumber.setStatus("mandatory")


class _ServerTimeLocal_Type(DisplayString):
    """Custom type serverTimeLocal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ServerTimeLocal_Type.__name__ = "DisplayString"
_ServerTimeLocal_Object = MibScalar
serverTimeLocal = _ServerTimeLocal_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 4),
    _ServerTimeLocal_Type()
)
serverTimeLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTimeLocal.setStatus("mandatory")
_ServerTimeUTC_Type = Integer32
_ServerTimeUTC_Object = MibScalar
serverTimeUTC = _ServerTimeUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 5),
    _ServerTimeUTC_Type()
)
serverTimeUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTimeUTC.setStatus("mandatory")
_ServerUpTime_Type = TimeTicks
_ServerUpTime_Object = MibScalar
serverUpTime = _ServerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 6),
    _ServerUpTime_Type()
)
serverUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverUpTime.setStatus("mandatory")
_ServerCpuUtil_Type = Integer32
_ServerCpuUtil_Object = MibScalar
serverCpuUtil = _ServerCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 7),
    _ServerCpuUtil_Type()
)
serverCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCpuUtil.setStatus("mandatory")
_ServerCpuCount_Type = Integer32
_ServerCpuCount_Object = MibScalar
serverCpuCount = _ServerCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 8),
    _ServerCpuCount_Type()
)
serverCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCpuCount.setStatus("mandatory")
_ServerCpuSpeed_Type = Integer32
_ServerCpuSpeed_Object = MibScalar
serverCpuSpeed = _ServerCpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 9),
    _ServerCpuSpeed_Type()
)
serverCpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCpuSpeed.setStatus("mandatory")
_ServerCacheHits_Type = Integer32
_ServerCacheHits_Object = MibScalar
serverCacheHits = _ServerCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 10),
    _ServerCacheHits_Type()
)
serverCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCacheHits.setStatus("mandatory")
_ServerCacheLRU_Type = TimeTicks
_ServerCacheLRU_Object = MibScalar
serverCacheLRU = _ServerCacheLRU_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 11),
    _ServerCacheLRU_Type()
)
serverCacheLRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCacheLRU.setStatus("mandatory")
_ServerCacheRatio_Type = Integer32
_ServerCacheRatio_Object = MibScalar
serverCacheRatio = _ServerCacheRatio_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 12),
    _ServerCacheRatio_Type()
)
serverCacheRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCacheRatio.setStatus("mandatory")
_ServerLicenses_Type = Integer32
_ServerLicenses_Object = MibScalar
serverLicenses = _ServerLicenses_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 13),
    _ServerLicenses_Type()
)
serverLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverLicenses.setStatus("mandatory")
_ServerConns_Type = Integer32
_ServerConns_Object = MibScalar
serverConns = _ServerConns_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 14),
    _ServerConns_Type()
)
serverConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConns.setStatus("mandatory")
_ServerUsers_Type = Integer32
_ServerUsers_Object = MibScalar
serverUsers = _ServerUsers_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 15),
    _ServerUsers_Type()
)
serverUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverUsers.setStatus("mandatory")


class _ServerAllowUnencryptedPwds_Type(DisplayString):
    """Custom type serverAllowUnencryptedPwds based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ServerAllowUnencryptedPwds_Type.__name__ = "DisplayString"
_ServerAllowUnencryptedPwds_Object = MibScalar
serverAllowUnencryptedPwds = _ServerAllowUnencryptedPwds_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 16),
    _ServerAllowUnencryptedPwds_Type()
)
serverAllowUnencryptedPwds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAllowUnencryptedPwds.setStatus("mandatory")


class _ServerDOSPresent_Type(DisplayString):
    """Custom type serverDOSPresent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ServerDOSPresent_Type.__name__ = "DisplayString"
_ServerDOSPresent_Object = MibScalar
serverDOSPresent = _ServerDOSPresent_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 17),
    _ServerDOSPresent_Type()
)
serverDOSPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverDOSPresent.setStatus("mandatory")


class _ServerLoginStatus_Type(DisplayString):
    """Custom type serverLoginStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ServerLoginStatus_Type.__name__ = "DisplayString"
_ServerLoginStatus_Object = MibScalar
serverLoginStatus = _ServerLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 18),
    _ServerLoginStatus_Type()
)
serverLoginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverLoginStatus.setStatus("mandatory")


class _ServerRemoteStatus_Type(DisplayString):
    """Custom type serverRemoteStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ServerRemoteStatus_Type.__name__ = "DisplayString"
_ServerRemoteStatus_Object = MibScalar
serverRemoteStatus = _ServerRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 19),
    _ServerRemoteStatus_Type()
)
serverRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverRemoteStatus.setStatus("mandatory")
_ServerSecurityRestrictionLevel_Type = Integer32
_ServerSecurityRestrictionLevel_Object = MibScalar
serverSecurityRestrictionLevel = _ServerSecurityRestrictionLevel_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 20),
    _ServerSecurityRestrictionLevel_Type()
)
serverSecurityRestrictionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverSecurityRestrictionLevel.setStatus("mandatory")
_ServerNumOfActiveDrives_Type = Integer32
_ServerNumOfActiveDrives_Object = MibScalar
serverNumOfActiveDrives = _ServerNumOfActiveDrives_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 21),
    _ServerNumOfActiveDrives_Type()
)
serverNumOfActiveDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNumOfActiveDrives.setStatus("mandatory")
_ServerNumOfMountedVols_Type = Integer32
_ServerNumOfMountedVols_Object = MibScalar
serverNumOfMountedVols = _ServerNumOfMountedVols_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 22),
    _ServerNumOfMountedVols_Type()
)
serverNumOfMountedVols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverNumOfMountedVols.setStatus("mandatory")


class _ServerStartupFilePath_Type(DisplayString):
    """Custom type serverStartupFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ServerStartupFilePath_Type.__name__ = "DisplayString"
_ServerStartupFilePath_Object = MibScalar
serverStartupFilePath = _ServerStartupFilePath_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 23),
    _ServerStartupFilePath_Type()
)
serverStartupFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverStartupFilePath.setStatus("mandatory")


class _ServerAutoexecFilePath_Type(DisplayString):
    """Custom type serverAutoexecFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ServerAutoexecFilePath_Type.__name__ = "DisplayString"
_ServerAutoexecFilePath_Object = MibScalar
serverAutoexecFilePath = _ServerAutoexecFilePath_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 1, 24),
    _ServerAutoexecFilePath_Type()
)
serverAutoexecFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAutoexecFilePath.setStatus("mandatory")
_Configinfo_ObjectIdentity = ObjectIdentity
configinfo = _Configinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2)
)


class _ConfigVersion_Type(DisplayString):
    """Custom type configVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ConfigVersion_Type.__name__ = "DisplayString"
_ConfigVersion_Object = MibScalar
configVersion = _ConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 1),
    _ConfigVersion_Type()
)
configVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configVersion.setStatus("mandatory")
_ConfigCycleLength_Type = Integer32
_ConfigCycleLength_Object = MibScalar
configCycleLength = _ConfigCycleLength_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 2),
    _ConfigCycleLength_Type()
)
configCycleLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configCycleLength.setStatus("mandatory")


class _ConfigStartTime_Type(DisplayString):
    """Custom type configStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_ConfigStartTime_Type.__name__ = "DisplayString"
_ConfigStartTime_Object = MibScalar
configStartTime = _ConfigStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 3),
    _ConfigStartTime_Type()
)
configStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configStartTime.setStatus("mandatory")


class _ConfigStopTime_Type(DisplayString):
    """Custom type configStopTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_ConfigStopTime_Type.__name__ = "DisplayString"
_ConfigStopTime_Object = MibScalar
configStopTime = _ConfigStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 4),
    _ConfigStopTime_Type()
)
configStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configStopTime.setStatus("mandatory")


class _ConfigKeyboardStatus_Type(DisplayString):
    """Custom type configKeyboardStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_ConfigKeyboardStatus_Type.__name__ = "DisplayString"
_ConfigKeyboardStatus_Object = MibScalar
configKeyboardStatus = _ConfigKeyboardStatus_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 5),
    _ConfigKeyboardStatus_Type()
)
configKeyboardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configKeyboardStatus.setStatus("mandatory")


class _ConfigKeyboardAutoLock_Type(DisplayString):
    """Custom type configKeyboardAutoLock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ConfigKeyboardAutoLock_Type.__name__ = "DisplayString"
_ConfigKeyboardAutoLock_Object = MibScalar
configKeyboardAutoLock = _ConfigKeyboardAutoLock_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 6),
    _ConfigKeyboardAutoLock_Type()
)
configKeyboardAutoLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configKeyboardAutoLock.setStatus("mandatory")
_ConfigScreenSaverTimeout_Type = Integer32
_ConfigScreenSaverTimeout_Object = MibScalar
configScreenSaverTimeout = _ConfigScreenSaverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 7),
    _ConfigScreenSaverTimeout_Type()
)
configScreenSaverTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configScreenSaverTimeout.setStatus("mandatory")


class _ConfigArchiveStatus_Type(DisplayString):
    """Custom type configArchiveStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_ConfigArchiveStatus_Type.__name__ = "DisplayString"
_ConfigArchiveStatus_Object = MibScalar
configArchiveStatus = _ConfigArchiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 8),
    _ConfigArchiveStatus_Type()
)
configArchiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configArchiveStatus.setStatus("mandatory")
_ConfigArchiveMaxDays_Type = Integer32
_ConfigArchiveMaxDays_Object = MibScalar
configArchiveMaxDays = _ConfigArchiveMaxDays_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 9),
    _ConfigArchiveMaxDays_Type()
)
configArchiveMaxDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configArchiveMaxDays.setStatus("mandatory")


class _ConfigDataFileName_Type(DisplayString):
    """Custom type configDataFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ConfigDataFileName_Type.__name__ = "DisplayString"
_ConfigDataFileName_Object = MibScalar
configDataFileName = _ConfigDataFileName_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 10),
    _ConfigDataFileName_Type()
)
configDataFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDataFileName.setStatus("mandatory")


class _ConfigDataFileFormat_Type(DisplayString):
    """Custom type configDataFileFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ConfigDataFileFormat_Type.__name__ = "DisplayString"
_ConfigDataFileFormat_Object = MibScalar
configDataFileFormat = _ConfigDataFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 11),
    _ConfigDataFileFormat_Type()
)
configDataFileFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDataFileFormat.setStatus("mandatory")


class _ConfigLogFileName_Type(DisplayString):
    """Custom type configLogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ConfigLogFileName_Type.__name__ = "DisplayString"
_ConfigLogFileName_Object = MibScalar
configLogFileName = _ConfigLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 12),
    _ConfigLogFileName_Type()
)
configLogFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configLogFileName.setStatus("mandatory")


class _ConfigTrendFileName_Type(DisplayString):
    """Custom type configTrendFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ConfigTrendFileName_Type.__name__ = "DisplayString"
_ConfigTrendFileName_Object = MibScalar
configTrendFileName = _ConfigTrendFileName_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 13),
    _ConfigTrendFileName_Type()
)
configTrendFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTrendFileName.setStatus("mandatory")
_ConfigTrendMaxDays_Type = Integer32
_ConfigTrendMaxDays_Object = MibScalar
configTrendMaxDays = _ConfigTrendMaxDays_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 2, 14),
    _ConfigTrendMaxDays_Type()
)
configTrendMaxDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTrendMaxDays.setStatus("mandatory")
_Memoryinfo_ObjectIdentity = ObjectIdentity
memoryinfo = _Memoryinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3)
)
_MemoryTotalRAM_Type = Integer32
_MemoryTotalRAM_Object = MibScalar
memoryTotalRAM = _MemoryTotalRAM_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 1),
    _MemoryTotalRAM_Type()
)
memoryTotalRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTotalRAM.setStatus("mandatory")
_MemoryServerWorkRAM_Type = Integer32
_MemoryServerWorkRAM_Object = MibScalar
memoryServerWorkRAM = _MemoryServerWorkRAM_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 2),
    _MemoryServerWorkRAM_Type()
)
memoryServerWorkRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryServerWorkRAM.setStatus("mandatory")
_MemoryDOS_Type = Integer32
_MemoryDOS_Object = MibScalar
memoryDOS = _MemoryDOS_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 3),
    _MemoryDOS_Type()
)
memoryDOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryDOS.setStatus("mandatory")
_MemoryBaseRAM_Type = Integer32
_MemoryBaseRAM_Object = MibScalar
memoryBaseRAM = _MemoryBaseRAM_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 4),
    _MemoryBaseRAM_Type()
)
memoryBaseRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryBaseRAM.setStatus("mandatory")
_MemoryAllocPoolTotal_Type = Integer32
_MemoryAllocPoolTotal_Object = MibScalar
memoryAllocPoolTotal = _MemoryAllocPoolTotal_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 5),
    _MemoryAllocPoolTotal_Type()
)
memoryAllocPoolTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAllocPoolTotal.setStatus("mandatory")
_MemoryAllocPoolInUse_Type = Integer32
_MemoryAllocPoolInUse_Object = MibScalar
memoryAllocPoolInUse = _MemoryAllocPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 6),
    _MemoryAllocPoolInUse_Type()
)
memoryAllocPoolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAllocPoolInUse.setStatus("mandatory")
_MemoryCacheBufferPool_Type = Integer32
_MemoryCacheBufferPool_Object = MibScalar
memoryCacheBufferPool = _MemoryCacheBufferPool_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 7),
    _MemoryCacheBufferPool_Type()
)
memoryCacheBufferPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheBufferPool.setStatus("mandatory")
_MemoryCacheMovablePool_Type = Integer32
_MemoryCacheMovablePool_Object = MibScalar
memoryCacheMovablePool = _MemoryCacheMovablePool_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 8),
    _MemoryCacheMovablePool_Type()
)
memoryCacheMovablePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheMovablePool.setStatus("mandatory")
_MemoryCacheNonMovablePool_Type = Integer32
_MemoryCacheNonMovablePool_Object = MibScalar
memoryCacheNonMovablePool = _MemoryCacheNonMovablePool_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 9),
    _MemoryCacheNonMovablePool_Type()
)
memoryCacheNonMovablePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryCacheNonMovablePool.setStatus("mandatory")
_MemoryNw3PermMemoryPoolTotal_Type = Integer32
_MemoryNw3PermMemoryPoolTotal_Object = MibScalar
memoryNw3PermMemoryPoolTotal = _MemoryNw3PermMemoryPoolTotal_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 10),
    _MemoryNw3PermMemoryPoolTotal_Type()
)
memoryNw3PermMemoryPoolTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryNw3PermMemoryPoolTotal.setStatus("mandatory")
_MemoryNw3PermMemoryPoolInUse_Type = Integer32
_MemoryNw3PermMemoryPoolInUse_Object = MibScalar
memoryNw3PermMemoryPoolInUse = _MemoryNw3PermMemoryPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 11),
    _MemoryNw3PermMemoryPoolInUse_Type()
)
memoryNw3PermMemoryPoolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryNw3PermMemoryPoolInUse.setStatus("mandatory")
_MemoryNw4CodeDataPool_Type = Integer32
_MemoryNw4CodeDataPool_Object = MibScalar
memoryNw4CodeDataPool = _MemoryNw4CodeDataPool_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 3, 12),
    _MemoryNw4CodeDataPool_Type()
)
memoryNw4CodeDataPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryNw4CodeDataPool.setStatus("mandatory")
_Moduleinfo_ObjectIdentity = ObjectIdentity
moduleinfo = _Moduleinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4)
)
_ModuleCount_Type = Integer32
_ModuleCount_Object = MibScalar
moduleCount = _ModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 1),
    _ModuleCount_Type()
)
moduleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCount.setStatus("mandatory")
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("mandatory")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1)
)
moduleEntry.setIndexNames(
    (0, "NConsole-MIB", "moduleIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("mandatory")
_ModuleIndex_Type = Integer32
_ModuleIndex_Object = MibTableColumn
moduleIndex = _ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 1),
    _ModuleIndex_Type()
)
moduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIndex.setStatus("mandatory")


class _ModuleName_Type(DisplayString):
    """Custom type moduleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_ModuleName_Type.__name__ = "DisplayString"
_ModuleName_Object = MibTableColumn
moduleName = _ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 2),
    _ModuleName_Type()
)
moduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleName.setStatus("mandatory")


class _ModuleDesc_Type(DisplayString):
    """Custom type moduleDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ModuleDesc_Type.__name__ = "DisplayString"
_ModuleDesc_Object = MibTableColumn
moduleDesc = _ModuleDesc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 3),
    _ModuleDesc_Type()
)
moduleDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDesc.setStatus("mandatory")


class _ModuleCopyright_Type(DisplayString):
    """Custom type moduleCopyright based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ModuleCopyright_Type.__name__ = "DisplayString"
_ModuleCopyright_Object = MibTableColumn
moduleCopyright = _ModuleCopyright_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 4),
    _ModuleCopyright_Type()
)
moduleCopyright.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCopyright.setStatus("mandatory")


class _ModuleVersion_Type(DisplayString):
    """Custom type moduleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ModuleVersion_Type.__name__ = "DisplayString"
_ModuleVersion_Object = MibTableColumn
moduleVersion = _ModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 5),
    _ModuleVersion_Type()
)
moduleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVersion.setStatus("mandatory")


class _ModuleCompileDate_Type(DisplayString):
    """Custom type moduleCompileDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ModuleCompileDate_Type.__name__ = "DisplayString"
_ModuleCompileDate_Object = MibTableColumn
moduleCompileDate = _ModuleCompileDate_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 6),
    _ModuleCompileDate_Type()
)
moduleCompileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCompileDate.setStatus("mandatory")
_ModuleCodeSize_Type = Integer32
_ModuleCodeSize_Object = MibTableColumn
moduleCodeSize = _ModuleCodeSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 7),
    _ModuleCodeSize_Type()
)
moduleCodeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCodeSize.setStatus("mandatory")
_ModuleDataSize_Type = Integer32
_ModuleDataSize_Object = MibTableColumn
moduleDataSize = _ModuleDataSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 8),
    _ModuleDataSize_Type()
)
moduleDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDataSize.setStatus("mandatory")
_ModuleSmallMemoryAlloc_Type = Integer32
_ModuleSmallMemoryAlloc_Object = MibTableColumn
moduleSmallMemoryAlloc = _ModuleSmallMemoryAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 9),
    _ModuleSmallMemoryAlloc_Type()
)
moduleSmallMemoryAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSmallMemoryAlloc.setStatus("mandatory")
_ModuleMediumMemoryAlloc_Type = Integer32
_ModuleMediumMemoryAlloc_Object = MibTableColumn
moduleMediumMemoryAlloc = _ModuleMediumMemoryAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 10),
    _ModuleMediumMemoryAlloc_Type()
)
moduleMediumMemoryAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleMediumMemoryAlloc.setStatus("mandatory")
_ModuleLargeMemoryAlloc_Type = Integer32
_ModuleLargeMemoryAlloc_Object = MibTableColumn
moduleLargeMemoryAlloc = _ModuleLargeMemoryAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 11),
    _ModuleLargeMemoryAlloc_Type()
)
moduleLargeMemoryAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleLargeMemoryAlloc.setStatus("mandatory")
_ModuleActiveProcesses_Type = Integer32
_ModuleActiveProcesses_Object = MibTableColumn
moduleActiveProcesses = _ModuleActiveProcesses_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 12),
    _ModuleActiveProcesses_Type()
)
moduleActiveProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleActiveProcesses.setStatus("mandatory")
_ModuleActiveScreens_Type = Integer32
_ModuleActiveScreens_Object = MibTableColumn
moduleActiveScreens = _ModuleActiveScreens_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 4, 2, 1, 13),
    _ModuleActiveScreens_Type()
)
moduleActiveScreens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleActiveScreens.setStatus("mandatory")
_Netinfo_ObjectIdentity = ObjectIdentity
netinfo = _Netinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5)
)
_NetCount_Type = Integer32
_NetCount_Object = MibScalar
netCount = _NetCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 1),
    _NetCount_Type()
)
netCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netCount.setStatus("mandatory")
_NetTable_Object = MibTable
netTable = _NetTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2)
)
if mibBuilder.loadTexts:
    netTable.setStatus("mandatory")
_NetEntry_Object = MibTableRow
netEntry = _NetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1)
)
netEntry.setIndexNames(
    (0, "NConsole-MIB", "netIndex"),
)
if mibBuilder.loadTexts:
    netEntry.setStatus("mandatory")
_NetIndex_Type = Integer32
_NetIndex_Object = MibTableColumn
netIndex = _NetIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 1),
    _NetIndex_Type()
)
netIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIndex.setStatus("mandatory")


class _NetDriverName_Type(DisplayString):
    """Custom type netDriverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NetDriverName_Type.__name__ = "DisplayString"
_NetDriverName_Object = MibTableColumn
netDriverName = _NetDriverName_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 2),
    _NetDriverName_Type()
)
netDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netDriverName.setStatus("mandatory")


class _NetDriverDesc_Type(DisplayString):
    """Custom type netDriverDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NetDriverDesc_Type.__name__ = "DisplayString"
_NetDriverDesc_Object = MibTableColumn
netDriverDesc = _NetDriverDesc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 3),
    _NetDriverDesc_Type()
)
netDriverDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netDriverDesc.setStatus("mandatory")


class _NetFrameDesc_Type(DisplayString):
    """Custom type netFrameDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NetFrameDesc_Type.__name__ = "DisplayString"
_NetFrameDesc_Object = MibTableColumn
netFrameDesc = _NetFrameDesc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 4),
    _NetFrameDesc_Type()
)
netFrameDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netFrameDesc.setStatus("mandatory")


class _NetLogicalName_Type(DisplayString):
    """Custom type netLogicalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_NetLogicalName_Type.__name__ = "DisplayString"
_NetLogicalName_Object = MibTableColumn
netLogicalName = _NetLogicalName_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 5),
    _NetLogicalName_Type()
)
netLogicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLogicalName.setStatus("mandatory")


class _NetProtocolDesc_Type(DisplayString):
    """Custom type netProtocolDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NetProtocolDesc_Type.__name__ = "DisplayString"
_NetProtocolDesc_Object = MibTableColumn
netProtocolDesc = _NetProtocolDesc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 6),
    _NetProtocolDesc_Type()
)
netProtocolDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netProtocolDesc.setStatus("mandatory")


class _NetNodeID_Type(OctetString):
    """Custom type netNodeID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NetNodeID_Type.__name__ = "OctetString"
_NetNodeID_Object = MibTableColumn
netNodeID = _NetNodeID_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 7),
    _NetNodeID_Type()
)
netNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netNodeID.setStatus("mandatory")
_NetLineSpeed_Type = Integer32
_NetLineSpeed_Object = MibTableColumn
netLineSpeed = _NetLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 8),
    _NetLineSpeed_Type()
)
netLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLineSpeed.setStatus("mandatory")
_NetMaxPacketSize_Type = Integer32
_NetMaxPacketSize_Object = MibTableColumn
netMaxPacketSize = _NetMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 9),
    _NetMaxPacketSize_Type()
)
netMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMaxPacketSize.setStatus("mandatory")
_NetMaxRecvSize_Type = Integer32
_NetMaxRecvSize_Object = MibTableColumn
netMaxRecvSize = _NetMaxRecvSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 10),
    _NetMaxRecvSize_Type()
)
netMaxRecvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMaxRecvSize.setStatus("mandatory")
_NetMaxProtocolSize_Type = Integer32
_NetMaxProtocolSize_Object = MibTableColumn
netMaxProtocolSize = _NetMaxProtocolSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 11),
    _NetMaxProtocolSize_Type()
)
netMaxProtocolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMaxProtocolSize.setStatus("mandatory")


class _NetPrimaryIOPort_Type(DisplayString):
    """Custom type netPrimaryIOPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NetPrimaryIOPort_Type.__name__ = "DisplayString"
_NetPrimaryIOPort_Object = MibTableColumn
netPrimaryIOPort = _NetPrimaryIOPort_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 12),
    _NetPrimaryIOPort_Type()
)
netPrimaryIOPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPrimaryIOPort.setStatus("mandatory")


class _NetPrimaryMemoryDecode_Type(DisplayString):
    """Custom type netPrimaryMemoryDecode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NetPrimaryMemoryDecode_Type.__name__ = "DisplayString"
_NetPrimaryMemoryDecode_Object = MibTableColumn
netPrimaryMemoryDecode = _NetPrimaryMemoryDecode_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 13),
    _NetPrimaryMemoryDecode_Type()
)
netPrimaryMemoryDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPrimaryMemoryDecode.setStatus("mandatory")


class _NetPrimaryInterrupt_Type(DisplayString):
    """Custom type netPrimaryInterrupt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_NetPrimaryInterrupt_Type.__name__ = "DisplayString"
_NetPrimaryInterrupt_Object = MibTableColumn
netPrimaryInterrupt = _NetPrimaryInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 14),
    _NetPrimaryInterrupt_Type()
)
netPrimaryInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPrimaryInterrupt.setStatus("mandatory")


class _NetPrimaryDMA_Type(DisplayString):
    """Custom type netPrimaryDMA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_NetPrimaryDMA_Type.__name__ = "DisplayString"
_NetPrimaryDMA_Object = MibTableColumn
netPrimaryDMA = _NetPrimaryDMA_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 15),
    _NetPrimaryDMA_Type()
)
netPrimaryDMA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPrimaryDMA.setStatus("mandatory")


class _NetSecondaryIOPort_Type(DisplayString):
    """Custom type netSecondaryIOPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NetSecondaryIOPort_Type.__name__ = "DisplayString"
_NetSecondaryIOPort_Object = MibTableColumn
netSecondaryIOPort = _NetSecondaryIOPort_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 16),
    _NetSecondaryIOPort_Type()
)
netSecondaryIOPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netSecondaryIOPort.setStatus("mandatory")


class _NetSecondaryMemoryDecode_Type(DisplayString):
    """Custom type netSecondaryMemoryDecode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NetSecondaryMemoryDecode_Type.__name__ = "DisplayString"
_NetSecondaryMemoryDecode_Object = MibTableColumn
netSecondaryMemoryDecode = _NetSecondaryMemoryDecode_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 17),
    _NetSecondaryMemoryDecode_Type()
)
netSecondaryMemoryDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netSecondaryMemoryDecode.setStatus("mandatory")


class _NetSecondaryInterrupt_Type(DisplayString):
    """Custom type netSecondaryInterrupt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_NetSecondaryInterrupt_Type.__name__ = "DisplayString"
_NetSecondaryInterrupt_Object = MibTableColumn
netSecondaryInterrupt = _NetSecondaryInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 18),
    _NetSecondaryInterrupt_Type()
)
netSecondaryInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netSecondaryInterrupt.setStatus("mandatory")


class _NetSecondaryDMA_Type(DisplayString):
    """Custom type netSecondaryDMA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_NetSecondaryDMA_Type.__name__ = "DisplayString"
_NetSecondaryDMA_Object = MibTableColumn
netSecondaryDMA = _NetSecondaryDMA_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 19),
    _NetSecondaryDMA_Type()
)
netSecondaryDMA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netSecondaryDMA.setStatus("mandatory")
_NetTotalRxPacketCount_Type = Integer32
_NetTotalRxPacketCount_Object = MibTableColumn
netTotalRxPacketCount = _NetTotalRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 20),
    _NetTotalRxPacketCount_Type()
)
netTotalRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netTotalRxPacketCount.setStatus("mandatory")
_NetPacketRxOverflowCount_Type = Integer32
_NetPacketRxOverflowCount_Object = MibTableColumn
netPacketRxOverflowCount = _NetPacketRxOverflowCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 21),
    _NetPacketRxOverflowCount_Type()
)
netPacketRxOverflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketRxOverflowCount.setStatus("mandatory")
_NetPacketRxTooBigCount_Type = Integer32
_NetPacketRxTooBigCount_Object = MibTableColumn
netPacketRxTooBigCount = _NetPacketRxTooBigCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 22),
    _NetPacketRxTooBigCount_Type()
)
netPacketRxTooBigCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketRxTooBigCount.setStatus("mandatory")
_NetPacketRxTooSmallCount_Type = Integer32
_NetPacketRxTooSmallCount_Object = MibTableColumn
netPacketRxTooSmallCount = _NetPacketRxTooSmallCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 23),
    _NetPacketRxTooSmallCount_Type()
)
netPacketRxTooSmallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketRxTooSmallCount.setStatus("mandatory")
_NetPacketRxMiscErrorCount_Type = Integer32
_NetPacketRxMiscErrorCount_Object = MibTableColumn
netPacketRxMiscErrorCount = _NetPacketRxMiscErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 24),
    _NetPacketRxMiscErrorCount_Type()
)
netPacketRxMiscErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketRxMiscErrorCount.setStatus("mandatory")
_NetChecksumErrorCount_Type = Integer32
_NetChecksumErrorCount_Object = MibTableColumn
netChecksumErrorCount = _NetChecksumErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 25),
    _NetChecksumErrorCount_Type()
)
netChecksumErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netChecksumErrorCount.setStatus("mandatory")
_NetHardwareRxMismatchCount_Type = Integer32
_NetHardwareRxMismatchCount_Object = MibTableColumn
netHardwareRxMismatchCount = _NetHardwareRxMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 26),
    _NetHardwareRxMismatchCount_Type()
)
netHardwareRxMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netHardwareRxMismatchCount.setStatus("mandatory")
_NetTotalTxPacketCount_Type = Integer32
_NetTotalTxPacketCount_Object = MibTableColumn
netTotalTxPacketCount = _NetTotalTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 27),
    _NetTotalTxPacketCount_Type()
)
netTotalTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netTotalTxPacketCount.setStatus("mandatory")
_NetNoECBAvailableCount_Type = Integer32
_NetNoECBAvailableCount_Object = MibTableColumn
netNoECBAvailableCount = _NetNoECBAvailableCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 28),
    _NetNoECBAvailableCount_Type()
)
netNoECBAvailableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netNoECBAvailableCount.setStatus("mandatory")
_NetPacketTxTooBigCount_Type = Integer32
_NetPacketTxTooBigCount_Object = MibTableColumn
netPacketTxTooBigCount = _NetPacketTxTooBigCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 29),
    _NetPacketTxTooBigCount_Type()
)
netPacketTxTooBigCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketTxTooBigCount.setStatus("mandatory")
_NetPacketTxTooSmallCount_Type = Integer32
_NetPacketTxTooSmallCount_Object = MibTableColumn
netPacketTxTooSmallCount = _NetPacketTxTooSmallCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 30),
    _NetPacketTxTooSmallCount_Type()
)
netPacketTxTooSmallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketTxTooSmallCount.setStatus("mandatory")
_NetPacketTxMiscErrorCount_Type = Integer32
_NetPacketTxMiscErrorCount_Object = MibTableColumn
netPacketTxMiscErrorCount = _NetPacketTxMiscErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 31),
    _NetPacketTxMiscErrorCount_Type()
)
netPacketTxMiscErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netPacketTxMiscErrorCount.setStatus("mandatory")
_NetRetryTxCount_Type = Integer32
_NetRetryTxCount_Object = MibTableColumn
netRetryTxCount = _NetRetryTxCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 5, 2, 1, 32),
    _NetRetryTxCount_Type()
)
netRetryTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netRetryTxCount.setStatus("mandatory")
_Nicstats_ObjectIdentity = ObjectIdentity
nicstats = _Nicstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6)
)
_NicCount_Type = Integer32
_NicCount_Object = MibScalar
nicCount = _NicCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 1),
    _NicCount_Type()
)
nicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicCount.setStatus("mandatory")
_NicTable_Object = MibTable
nicTable = _NicTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2)
)
if mibBuilder.loadTexts:
    nicTable.setStatus("mandatory")
_NicEntry_Object = MibTableRow
nicEntry = _NicEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2, 1)
)
nicEntry.setIndexNames(
    (0, "NConsole-MIB", "nicIndex"),
)
if mibBuilder.loadTexts:
    nicEntry.setStatus("mandatory")
_NicIndex_Type = Integer32
_NicIndex_Object = MibTableColumn
nicIndex = _NicIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2, 1, 1),
    _NicIndex_Type()
)
nicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicIndex.setStatus("mandatory")


class _NicNodeID_Type(OctetString):
    """Custom type nicNodeID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NicNodeID_Type.__name__ = "OctetString"
_NicNodeID_Object = MibTableColumn
nicNodeID = _NicNodeID_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2, 1, 2),
    _NicNodeID_Type()
)
nicNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicNodeID.setStatus("mandatory")
_NicCurrRxPacketCount_Type = Integer32
_NicCurrRxPacketCount_Object = MibTableColumn
nicCurrRxPacketCount = _NicCurrRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2, 1, 3),
    _NicCurrRxPacketCount_Type()
)
nicCurrRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicCurrRxPacketCount.setStatus("mandatory")
_NicAvgRxPacketCount_Type = Integer32
_NicAvgRxPacketCount_Object = MibTableColumn
nicAvgRxPacketCount = _NicAvgRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2, 1, 4),
    _NicAvgRxPacketCount_Type()
)
nicAvgRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicAvgRxPacketCount.setStatus("mandatory")
_NicPeakRxPacketCount_Type = Integer32
_NicPeakRxPacketCount_Object = MibTableColumn
nicPeakRxPacketCount = _NicPeakRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2, 1, 5),
    _NicPeakRxPacketCount_Type()
)
nicPeakRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicPeakRxPacketCount.setStatus("mandatory")
_NicCumlRxPacketCount_Type = Integer32
_NicCumlRxPacketCount_Object = MibTableColumn
nicCumlRxPacketCount = _NicCumlRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2, 1, 6),
    _NicCumlRxPacketCount_Type()
)
nicCumlRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicCumlRxPacketCount.setStatus("mandatory")
_NicCurrTxPacketCount_Type = Integer32
_NicCurrTxPacketCount_Object = MibTableColumn
nicCurrTxPacketCount = _NicCurrTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2, 1, 7),
    _NicCurrTxPacketCount_Type()
)
nicCurrTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicCurrTxPacketCount.setStatus("mandatory")
_NicAvgTxPacketCount_Type = Integer32
_NicAvgTxPacketCount_Object = MibTableColumn
nicAvgTxPacketCount = _NicAvgTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2, 1, 8),
    _NicAvgTxPacketCount_Type()
)
nicAvgTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicAvgTxPacketCount.setStatus("mandatory")
_NicPeakTxPacketCount_Type = Integer32
_NicPeakTxPacketCount_Object = MibTableColumn
nicPeakTxPacketCount = _NicPeakTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2, 1, 9),
    _NicPeakTxPacketCount_Type()
)
nicPeakTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicPeakTxPacketCount.setStatus("mandatory")
_NicCumlTxPacketCount_Type = Integer32
_NicCumlTxPacketCount_Object = MibTableColumn
nicCumlTxPacketCount = _NicCumlTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 6, 2, 1, 10),
    _NicCumlTxPacketCount_Type()
)
nicCumlTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicCumlTxPacketCount.setStatus("mandatory")
_Setparminfo_ObjectIdentity = ObjectIdentity
setparminfo = _Setparminfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 7)
)
_SetparmTable_Object = MibTable
setparmTable = _SetparmTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 7, 1)
)
if mibBuilder.loadTexts:
    setparmTable.setStatus("mandatory")
_SetparmEntry_Object = MibTableRow
setparmEntry = _SetparmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 7, 1, 1)
)
setparmEntry.setIndexNames(
    (0, "NConsole-MIB", "setparmIndex"),
)
if mibBuilder.loadTexts:
    setparmEntry.setStatus("mandatory")
_SetparmIndex_Type = Integer32
_SetparmIndex_Object = MibTableColumn
setparmIndex = _SetparmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 7, 1, 1, 1),
    _SetparmIndex_Type()
)
setparmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setparmIndex.setStatus("mandatory")


class _SetparmName_Type(DisplayString):
    """Custom type setparmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SetparmName_Type.__name__ = "DisplayString"
_SetparmName_Object = MibTableColumn
setparmName = _SetparmName_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 7, 1, 1, 2),
    _SetparmName_Type()
)
setparmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setparmName.setStatus("mandatory")


class _SetparmDesc_Type(DisplayString):
    """Custom type setparmDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 576),
    )


_SetparmDesc_Type.__name__ = "DisplayString"
_SetparmDesc_Object = MibTableColumn
setparmDesc = _SetparmDesc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 7, 1, 1, 3),
    _SetparmDesc_Type()
)
setparmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setparmDesc.setStatus("mandatory")


class _SetparmCategory_Type(DisplayString):
    """Custom type setparmCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SetparmCategory_Type.__name__ = "DisplayString"
_SetparmCategory_Object = MibTableColumn
setparmCategory = _SetparmCategory_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 7, 1, 1, 4),
    _SetparmCategory_Type()
)
setparmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setparmCategory.setStatus("mandatory")


class _SetparmFlags_Type(DisplayString):
    """Custom type setparmFlags based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SetparmFlags_Type.__name__ = "DisplayString"
_SetparmFlags_Object = MibTableColumn
setparmFlags = _SetparmFlags_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 7, 1, 1, 5),
    _SetparmFlags_Type()
)
setparmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setparmFlags.setStatus("mandatory")


class _SetparmCurrent_Type(DisplayString):
    """Custom type setparmCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SetparmCurrent_Type.__name__ = "DisplayString"
_SetparmCurrent_Object = MibTableColumn
setparmCurrent = _SetparmCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 7, 1, 1, 6),
    _SetparmCurrent_Type()
)
setparmCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setparmCurrent.setStatus("mandatory")


class _SetparmMinimum_Type(DisplayString):
    """Custom type setparmMinimum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SetparmMinimum_Type.__name__ = "DisplayString"
_SetparmMinimum_Object = MibTableColumn
setparmMinimum = _SetparmMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 7, 1, 1, 7),
    _SetparmMinimum_Type()
)
setparmMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setparmMinimum.setStatus("mandatory")


class _SetparmMaximum_Type(DisplayString):
    """Custom type setparmMaximum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SetparmMaximum_Type.__name__ = "DisplayString"
_SetparmMaximum_Object = MibTableColumn
setparmMaximum = _SetparmMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 7, 1, 1, 8),
    _SetparmMaximum_Type()
)
setparmMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setparmMaximum.setStatus("mandatory")
_Serverstats_ObjectIdentity = ObjectIdentity
serverstats = _Serverstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8)
)


class _ServerCycleStartTime_Type(DisplayString):
    """Custom type serverCycleStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ServerCycleStartTime_Type.__name__ = "DisplayString"
_ServerCycleStartTime_Object = MibScalar
serverCycleStartTime = _ServerCycleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 1),
    _ServerCycleStartTime_Type()
)
serverCycleStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCycleStartTime.setStatus("mandatory")
_ServerCycleStartUTC_Type = Integer32
_ServerCycleStartUTC_Object = MibScalar
serverCycleStartUTC = _ServerCycleStartUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 2),
    _ServerCycleStartUTC_Type()
)
serverCycleStartUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCycleStartUTC.setStatus("mandatory")
_ServerCycleElapsedTicks_Type = TimeTicks
_ServerCycleElapsedTicks_Object = MibScalar
serverCycleElapsedTicks = _ServerCycleElapsedTicks_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 3),
    _ServerCycleElapsedTicks_Type()
)
serverCycleElapsedTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCycleElapsedTicks.setStatus("mandatory")
_ServerCycleLengthTicks_Type = TimeTicks
_ServerCycleLengthTicks_Object = MibScalar
serverCycleLengthTicks = _ServerCycleLengthTicks_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 4),
    _ServerCycleLengthTicks_Type()
)
serverCycleLengthTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCycleLengthTicks.setStatus("mandatory")
_ServerCurrUtil_Type = Integer32
_ServerCurrUtil_Object = MibScalar
serverCurrUtil = _ServerCurrUtil_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 5),
    _ServerCurrUtil_Type()
)
serverCurrUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrUtil.setStatus("mandatory")
_ServerAvgUtil_Type = Integer32
_ServerAvgUtil_Object = MibScalar
serverAvgUtil = _ServerAvgUtil_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 6),
    _ServerAvgUtil_Type()
)
serverAvgUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgUtil.setStatus("mandatory")
_ServerPeakUtil_Type = Integer32
_ServerPeakUtil_Object = MibScalar
serverPeakUtil = _ServerPeakUtil_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 7),
    _ServerPeakUtil_Type()
)
serverPeakUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakUtil.setStatus("mandatory")
_ServerCurrCacheRatio_Type = Integer32
_ServerCurrCacheRatio_Object = MibScalar
serverCurrCacheRatio = _ServerCurrCacheRatio_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 8),
    _ServerCurrCacheRatio_Type()
)
serverCurrCacheRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrCacheRatio.setStatus("mandatory")
_ServerAvgCacheRatio_Type = Integer32
_ServerAvgCacheRatio_Object = MibScalar
serverAvgCacheRatio = _ServerAvgCacheRatio_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 9),
    _ServerAvgCacheRatio_Type()
)
serverAvgCacheRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgCacheRatio.setStatus("mandatory")
_ServerMinCacheRatio_Type = Integer32
_ServerMinCacheRatio_Object = MibScalar
serverMinCacheRatio = _ServerMinCacheRatio_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 10),
    _ServerMinCacheRatio_Type()
)
serverMinCacheRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverMinCacheRatio.setStatus("mandatory")
_ServerCurrCacheHits_Type = Integer32
_ServerCurrCacheHits_Object = MibScalar
serverCurrCacheHits = _ServerCurrCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 11),
    _ServerCurrCacheHits_Type()
)
serverCurrCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrCacheHits.setStatus("mandatory")
_ServerAvgCacheHits_Type = Integer32
_ServerAvgCacheHits_Object = MibScalar
serverAvgCacheHits = _ServerAvgCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 12),
    _ServerAvgCacheHits_Type()
)
serverAvgCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgCacheHits.setStatus("mandatory")
_ServerMinCacheHits_Type = Integer32
_ServerMinCacheHits_Object = MibScalar
serverMinCacheHits = _ServerMinCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 13),
    _ServerMinCacheHits_Type()
)
serverMinCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverMinCacheHits.setStatus("mandatory")
_ServerCurrFSPs_Type = Integer32
_ServerCurrFSPs_Object = MibScalar
serverCurrFSPs = _ServerCurrFSPs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 14),
    _ServerCurrFSPs_Type()
)
serverCurrFSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrFSPs.setStatus("mandatory")
_ServerAvgFSPs_Type = Integer32
_ServerAvgFSPs_Object = MibScalar
serverAvgFSPs = _ServerAvgFSPs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 15),
    _ServerAvgFSPs_Type()
)
serverAvgFSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgFSPs.setStatus("mandatory")
_ServerPeakFSPs_Type = Integer32
_ServerPeakFSPs_Object = MibScalar
serverPeakFSPs = _ServerPeakFSPs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 16),
    _ServerPeakFSPs_Type()
)
serverPeakFSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakFSPs.setStatus("mandatory")
_ServerCurrProcs_Type = Integer32
_ServerCurrProcs_Object = MibScalar
serverCurrProcs = _ServerCurrProcs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 17),
    _ServerCurrProcs_Type()
)
serverCurrProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrProcs.setStatus("mandatory")
_ServerAvgProcs_Type = Integer32
_ServerAvgProcs_Object = MibScalar
serverAvgProcs = _ServerAvgProcs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 18),
    _ServerAvgProcs_Type()
)
serverAvgProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgProcs.setStatus("mandatory")
_ServerPeakProcs_Type = Integer32
_ServerPeakProcs_Object = MibScalar
serverPeakProcs = _ServerPeakProcs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 19),
    _ServerPeakProcs_Type()
)
serverPeakProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakProcs.setStatus("mandatory")
_ServerCurrConns_Type = Integer32
_ServerCurrConns_Object = MibScalar
serverCurrConns = _ServerCurrConns_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 20),
    _ServerCurrConns_Type()
)
serverCurrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrConns.setStatus("mandatory")
_ServerAvgConns_Type = Integer32
_ServerAvgConns_Object = MibScalar
serverAvgConns = _ServerAvgConns_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 21),
    _ServerAvgConns_Type()
)
serverAvgConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgConns.setStatus("mandatory")
_ServerPeakConns_Type = Integer32
_ServerPeakConns_Object = MibScalar
serverPeakConns = _ServerPeakConns_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 22),
    _ServerPeakConns_Type()
)
serverPeakConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakConns.setStatus("mandatory")
_ServerCurrUsers_Type = Integer32
_ServerCurrUsers_Object = MibScalar
serverCurrUsers = _ServerCurrUsers_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 23),
    _ServerCurrUsers_Type()
)
serverCurrUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrUsers.setStatus("mandatory")
_ServerAvgUsers_Type = Integer32
_ServerAvgUsers_Object = MibScalar
serverAvgUsers = _ServerAvgUsers_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 24),
    _ServerAvgUsers_Type()
)
serverAvgUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgUsers.setStatus("mandatory")
_ServerPeakUsers_Type = Integer32
_ServerPeakUsers_Object = MibScalar
serverPeakUsers = _ServerPeakUsers_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 25),
    _ServerPeakUsers_Type()
)
serverPeakUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakUsers.setStatus("mandatory")
_ServerCurrRecvBuffs_Type = Integer32
_ServerCurrRecvBuffs_Object = MibScalar
serverCurrRecvBuffs = _ServerCurrRecvBuffs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 26),
    _ServerCurrRecvBuffs_Type()
)
serverCurrRecvBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrRecvBuffs.setStatus("mandatory")
_ServerAvgRecvBuffs_Type = Integer32
_ServerAvgRecvBuffs_Object = MibScalar
serverAvgRecvBuffs = _ServerAvgRecvBuffs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 27),
    _ServerAvgRecvBuffs_Type()
)
serverAvgRecvBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgRecvBuffs.setStatus("mandatory")
_ServerPeakRecvBuffs_Type = Integer32
_ServerPeakRecvBuffs_Object = MibScalar
serverPeakRecvBuffs = _ServerPeakRecvBuffs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 28),
    _ServerPeakRecvBuffs_Type()
)
serverPeakRecvBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakRecvBuffs.setStatus("mandatory")
_ServerCurrDirBuffs_Type = Integer32
_ServerCurrDirBuffs_Object = MibScalar
serverCurrDirBuffs = _ServerCurrDirBuffs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 29),
    _ServerCurrDirBuffs_Type()
)
serverCurrDirBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrDirBuffs.setStatus("mandatory")
_ServerAvgDirBuffs_Type = Integer32
_ServerAvgDirBuffs_Object = MibScalar
serverAvgDirBuffs = _ServerAvgDirBuffs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 30),
    _ServerAvgDirBuffs_Type()
)
serverAvgDirBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgDirBuffs.setStatus("mandatory")
_ServerPeakDirBuffs_Type = Integer32
_ServerPeakDirBuffs_Object = MibScalar
serverPeakDirBuffs = _ServerPeakDirBuffs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 31),
    _ServerPeakDirBuffs_Type()
)
serverPeakDirBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakDirBuffs.setStatus("mandatory")
_ServerCurrOpenFiles_Type = Integer32
_ServerCurrOpenFiles_Object = MibScalar
serverCurrOpenFiles = _ServerCurrOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 32),
    _ServerCurrOpenFiles_Type()
)
serverCurrOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrOpenFiles.setStatus("mandatory")
_ServerAvgOpenFiles_Type = Integer32
_ServerAvgOpenFiles_Object = MibScalar
serverAvgOpenFiles = _ServerAvgOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 33),
    _ServerAvgOpenFiles_Type()
)
serverAvgOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgOpenFiles.setStatus("mandatory")
_ServerPeakOpenFiles_Type = Integer32
_ServerPeakOpenFiles_Object = MibScalar
serverPeakOpenFiles = _ServerPeakOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 34),
    _ServerPeakOpenFiles_Type()
)
serverPeakOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakOpenFiles.setStatus("mandatory")
_ServerCurrIOsPending_Type = Integer32
_ServerCurrIOsPending_Object = MibScalar
serverCurrIOsPending = _ServerCurrIOsPending_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 35),
    _ServerCurrIOsPending_Type()
)
serverCurrIOsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrIOsPending.setStatus("mandatory")
_ServerAvgIOsPending_Type = Integer32
_ServerAvgIOsPending_Object = MibScalar
serverAvgIOsPending = _ServerAvgIOsPending_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 36),
    _ServerAvgIOsPending_Type()
)
serverAvgIOsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgIOsPending.setStatus("mandatory")
_ServerPeakIOsPending_Type = Integer32
_ServerPeakIOsPending_Object = MibScalar
serverPeakIOsPending = _ServerPeakIOsPending_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 37),
    _ServerPeakIOsPending_Type()
)
serverPeakIOsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakIOsPending.setStatus("mandatory")
_ServerCumlIOsPending_Type = Integer32
_ServerCumlIOsPending_Object = MibScalar
serverCumlIOsPending = _ServerCumlIOsPending_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 38),
    _ServerCumlIOsPending_Type()
)
serverCumlIOsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlIOsPending.setStatus("mandatory")
_ServerCurrDirtyBlocks_Type = Integer32
_ServerCurrDirtyBlocks_Object = MibScalar
serverCurrDirtyBlocks = _ServerCurrDirtyBlocks_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 39),
    _ServerCurrDirtyBlocks_Type()
)
serverCurrDirtyBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrDirtyBlocks.setStatus("mandatory")
_ServerAvgDirtyBlocks_Type = Integer32
_ServerAvgDirtyBlocks_Object = MibScalar
serverAvgDirtyBlocks = _ServerAvgDirtyBlocks_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 40),
    _ServerAvgDirtyBlocks_Type()
)
serverAvgDirtyBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgDirtyBlocks.setStatus("mandatory")
_ServerPeakDirtyBlocks_Type = Integer32
_ServerPeakDirtyBlocks_Object = MibScalar
serverPeakDirtyBlocks = _ServerPeakDirtyBlocks_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 41),
    _ServerPeakDirtyBlocks_Type()
)
serverPeakDirtyBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakDirtyBlocks.setStatus("mandatory")
_ServerCumlDirtyBlocks_Type = Integer32
_ServerCumlDirtyBlocks_Object = MibScalar
serverCumlDirtyBlocks = _ServerCumlDirtyBlocks_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 42),
    _ServerCumlDirtyBlocks_Type()
)
serverCumlDirtyBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlDirtyBlocks.setStatus("mandatory")
_ServerCurrDiskReads_Type = Integer32
_ServerCurrDiskReads_Object = MibScalar
serverCurrDiskReads = _ServerCurrDiskReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 43),
    _ServerCurrDiskReads_Type()
)
serverCurrDiskReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrDiskReads.setStatus("mandatory")
_ServerAvgDiskReads_Type = Integer32
_ServerAvgDiskReads_Object = MibScalar
serverAvgDiskReads = _ServerAvgDiskReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 44),
    _ServerAvgDiskReads_Type()
)
serverAvgDiskReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgDiskReads.setStatus("mandatory")
_ServerPeakDiskReads_Type = Integer32
_ServerPeakDiskReads_Object = MibScalar
serverPeakDiskReads = _ServerPeakDiskReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 45),
    _ServerPeakDiskReads_Type()
)
serverPeakDiskReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakDiskReads.setStatus("mandatory")
_ServerCumlDiskReads_Type = Integer32
_ServerCumlDiskReads_Object = MibScalar
serverCumlDiskReads = _ServerCumlDiskReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 46),
    _ServerCumlDiskReads_Type()
)
serverCumlDiskReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlDiskReads.setStatus("mandatory")
_ServerCurrDiskReadBytes_Type = Integer32
_ServerCurrDiskReadBytes_Object = MibScalar
serverCurrDiskReadBytes = _ServerCurrDiskReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 47),
    _ServerCurrDiskReadBytes_Type()
)
serverCurrDiskReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrDiskReadBytes.setStatus("mandatory")
_ServerAvgDiskReadBytes_Type = Integer32
_ServerAvgDiskReadBytes_Object = MibScalar
serverAvgDiskReadBytes = _ServerAvgDiskReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 48),
    _ServerAvgDiskReadBytes_Type()
)
serverAvgDiskReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgDiskReadBytes.setStatus("mandatory")
_ServerPeakDiskReadBytes_Type = Integer32
_ServerPeakDiskReadBytes_Object = MibScalar
serverPeakDiskReadBytes = _ServerPeakDiskReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 49),
    _ServerPeakDiskReadBytes_Type()
)
serverPeakDiskReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakDiskReadBytes.setStatus("mandatory")
_ServerCumlDiskReadBytes_Type = Integer32
_ServerCumlDiskReadBytes_Object = MibScalar
serverCumlDiskReadBytes = _ServerCumlDiskReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 50),
    _ServerCumlDiskReadBytes_Type()
)
serverCumlDiskReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlDiskReadBytes.setStatus("mandatory")
_ServerCurrDiskWrites_Type = Integer32
_ServerCurrDiskWrites_Object = MibScalar
serverCurrDiskWrites = _ServerCurrDiskWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 51),
    _ServerCurrDiskWrites_Type()
)
serverCurrDiskWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrDiskWrites.setStatus("mandatory")
_ServerAvgDiskWrites_Type = Integer32
_ServerAvgDiskWrites_Object = MibScalar
serverAvgDiskWrites = _ServerAvgDiskWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 52),
    _ServerAvgDiskWrites_Type()
)
serverAvgDiskWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgDiskWrites.setStatus("mandatory")
_ServerPeakDiskWrites_Type = Integer32
_ServerPeakDiskWrites_Object = MibScalar
serverPeakDiskWrites = _ServerPeakDiskWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 53),
    _ServerPeakDiskWrites_Type()
)
serverPeakDiskWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakDiskWrites.setStatus("mandatory")
_ServerCumlDiskWrites_Type = Integer32
_ServerCumlDiskWrites_Object = MibScalar
serverCumlDiskWrites = _ServerCumlDiskWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 54),
    _ServerCumlDiskWrites_Type()
)
serverCumlDiskWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlDiskWrites.setStatus("mandatory")
_ServerCurrDiskWriteBytes_Type = Integer32
_ServerCurrDiskWriteBytes_Object = MibScalar
serverCurrDiskWriteBytes = _ServerCurrDiskWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 55),
    _ServerCurrDiskWriteBytes_Type()
)
serverCurrDiskWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrDiskWriteBytes.setStatus("mandatory")
_ServerAvgDiskWriteBytes_Type = Integer32
_ServerAvgDiskWriteBytes_Object = MibScalar
serverAvgDiskWriteBytes = _ServerAvgDiskWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 56),
    _ServerAvgDiskWriteBytes_Type()
)
serverAvgDiskWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgDiskWriteBytes.setStatus("mandatory")
_ServerPeakDiskWriteBytes_Type = Integer32
_ServerPeakDiskWriteBytes_Object = MibScalar
serverPeakDiskWriteBytes = _ServerPeakDiskWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 57),
    _ServerPeakDiskWriteBytes_Type()
)
serverPeakDiskWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakDiskWriteBytes.setStatus("mandatory")
_ServerCumlDiskWriteBytes_Type = Integer32
_ServerCumlDiskWriteBytes_Object = MibScalar
serverCumlDiskWriteBytes = _ServerCumlDiskWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 58),
    _ServerCumlDiskWriteBytes_Type()
)
serverCumlDiskWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlDiskWriteBytes.setStatus("mandatory")
_ServerCurrRoutedPkts_Type = Integer32
_ServerCurrRoutedPkts_Object = MibScalar
serverCurrRoutedPkts = _ServerCurrRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 59),
    _ServerCurrRoutedPkts_Type()
)
serverCurrRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrRoutedPkts.setStatus("mandatory")
_ServerAvgRoutedPkts_Type = Integer32
_ServerAvgRoutedPkts_Object = MibScalar
serverAvgRoutedPkts = _ServerAvgRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 60),
    _ServerAvgRoutedPkts_Type()
)
serverAvgRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgRoutedPkts.setStatus("mandatory")
_ServerPeakRoutedPkts_Type = Integer32
_ServerPeakRoutedPkts_Object = MibScalar
serverPeakRoutedPkts = _ServerPeakRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 61),
    _ServerPeakRoutedPkts_Type()
)
serverPeakRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakRoutedPkts.setStatus("mandatory")
_ServerCumlRoutedPkts_Type = Integer32
_ServerCumlRoutedPkts_Object = MibScalar
serverCumlRoutedPkts = _ServerCumlRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 62),
    _ServerCumlRoutedPkts_Type()
)
serverCumlRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlRoutedPkts.setStatus("mandatory")
_ServerCurrRxPkts_Type = Integer32
_ServerCurrRxPkts_Object = MibScalar
serverCurrRxPkts = _ServerCurrRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 63),
    _ServerCurrRxPkts_Type()
)
serverCurrRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrRxPkts.setStatus("mandatory")
_ServerAvgRxPkts_Type = Integer32
_ServerAvgRxPkts_Object = MibScalar
serverAvgRxPkts = _ServerAvgRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 64),
    _ServerAvgRxPkts_Type()
)
serverAvgRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgRxPkts.setStatus("mandatory")
_ServerPeakRxPkts_Type = Integer32
_ServerPeakRxPkts_Object = MibScalar
serverPeakRxPkts = _ServerPeakRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 65),
    _ServerPeakRxPkts_Type()
)
serverPeakRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakRxPkts.setStatus("mandatory")
_ServerCumlRxPkts_Type = Integer32
_ServerCumlRxPkts_Object = MibScalar
serverCumlRxPkts = _ServerCumlRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 66),
    _ServerCumlRxPkts_Type()
)
serverCumlRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlRxPkts.setStatus("mandatory")
_ServerCurrRxBytes_Type = Integer32
_ServerCurrRxBytes_Object = MibScalar
serverCurrRxBytes = _ServerCurrRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 67),
    _ServerCurrRxBytes_Type()
)
serverCurrRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrRxBytes.setStatus("mandatory")
_ServerAvgRxBytes_Type = Integer32
_ServerAvgRxBytes_Object = MibScalar
serverAvgRxBytes = _ServerAvgRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 68),
    _ServerAvgRxBytes_Type()
)
serverAvgRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgRxBytes.setStatus("mandatory")
_ServerPeakRxBytes_Type = Integer32
_ServerPeakRxBytes_Object = MibScalar
serverPeakRxBytes = _ServerPeakRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 69),
    _ServerPeakRxBytes_Type()
)
serverPeakRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakRxBytes.setStatus("mandatory")
_ServerCumlRxBytes_Type = Integer32
_ServerCumlRxBytes_Object = MibScalar
serverCumlRxBytes = _ServerCumlRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 70),
    _ServerCumlRxBytes_Type()
)
serverCumlRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlRxBytes.setStatus("mandatory")
_ServerCurrTxPkts_Type = Integer32
_ServerCurrTxPkts_Object = MibScalar
serverCurrTxPkts = _ServerCurrTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 71),
    _ServerCurrTxPkts_Type()
)
serverCurrTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrTxPkts.setStatus("mandatory")
_ServerAvgTxPkts_Type = Integer32
_ServerAvgTxPkts_Object = MibScalar
serverAvgTxPkts = _ServerAvgTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 72),
    _ServerAvgTxPkts_Type()
)
serverAvgTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgTxPkts.setStatus("mandatory")
_ServerPeakTxPkts_Type = Integer32
_ServerPeakTxPkts_Object = MibScalar
serverPeakTxPkts = _ServerPeakTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 73),
    _ServerPeakTxPkts_Type()
)
serverPeakTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakTxPkts.setStatus("mandatory")
_ServerCumlTxPkts_Type = Integer32
_ServerCumlTxPkts_Object = MibScalar
serverCumlTxPkts = _ServerCumlTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 74),
    _ServerCumlTxPkts_Type()
)
serverCumlTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlTxPkts.setStatus("mandatory")
_ServerCurrTxBytes_Type = Integer32
_ServerCurrTxBytes_Object = MibScalar
serverCurrTxBytes = _ServerCurrTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 75),
    _ServerCurrTxBytes_Type()
)
serverCurrTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrTxBytes.setStatus("mandatory")
_ServerAvgTxBytes_Type = Integer32
_ServerAvgTxBytes_Object = MibScalar
serverAvgTxBytes = _ServerAvgTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 76),
    _ServerAvgTxBytes_Type()
)
serverAvgTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgTxBytes.setStatus("mandatory")
_ServerPeakTxBytes_Type = Integer32
_ServerPeakTxBytes_Object = MibScalar
serverPeakTxBytes = _ServerPeakTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 77),
    _ServerPeakTxBytes_Type()
)
serverPeakTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakTxBytes.setStatus("mandatory")
_ServerCumlTxBytes_Type = Integer32
_ServerCumlTxBytes_Object = MibScalar
serverCumlTxBytes = _ServerCumlTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 78),
    _ServerCumlTxBytes_Type()
)
serverCumlTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlTxBytes.setStatus("mandatory")
_ServerCurrDirSearch_Type = Integer32
_ServerCurrDirSearch_Object = MibScalar
serverCurrDirSearch = _ServerCurrDirSearch_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 79),
    _ServerCurrDirSearch_Type()
)
serverCurrDirSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrDirSearch.setStatus("mandatory")
_ServerAvgDirSearch_Type = Integer32
_ServerAvgDirSearch_Object = MibScalar
serverAvgDirSearch = _ServerAvgDirSearch_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 80),
    _ServerAvgDirSearch_Type()
)
serverAvgDirSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgDirSearch.setStatus("mandatory")
_ServerPeakDirSearch_Type = Integer32
_ServerPeakDirSearch_Object = MibScalar
serverPeakDirSearch = _ServerPeakDirSearch_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 81),
    _ServerPeakDirSearch_Type()
)
serverPeakDirSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakDirSearch.setStatus("mandatory")
_ServerCumlDirSearch_Type = Integer32
_ServerCumlDirSearch_Object = MibScalar
serverCumlDirSearch = _ServerCumlDirSearch_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 82),
    _ServerCumlDirSearch_Type()
)
serverCumlDirSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlDirSearch.setStatus("mandatory")
_ServerCurrFileCreates_Type = Integer32
_ServerCurrFileCreates_Object = MibScalar
serverCurrFileCreates = _ServerCurrFileCreates_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 83),
    _ServerCurrFileCreates_Type()
)
serverCurrFileCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrFileCreates.setStatus("mandatory")
_ServerAvgFileCreates_Type = Integer32
_ServerAvgFileCreates_Object = MibScalar
serverAvgFileCreates = _ServerAvgFileCreates_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 84),
    _ServerAvgFileCreates_Type()
)
serverAvgFileCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgFileCreates.setStatus("mandatory")
_ServerPeakFileCreates_Type = Integer32
_ServerPeakFileCreates_Object = MibScalar
serverPeakFileCreates = _ServerPeakFileCreates_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 85),
    _ServerPeakFileCreates_Type()
)
serverPeakFileCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakFileCreates.setStatus("mandatory")
_ServerCumlFileCreates_Type = Integer32
_ServerCumlFileCreates_Object = MibScalar
serverCumlFileCreates = _ServerCumlFileCreates_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 86),
    _ServerCumlFileCreates_Type()
)
serverCumlFileCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlFileCreates.setStatus("mandatory")
_ServerCurrFileOpens_Type = Integer32
_ServerCurrFileOpens_Object = MibScalar
serverCurrFileOpens = _ServerCurrFileOpens_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 87),
    _ServerCurrFileOpens_Type()
)
serverCurrFileOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrFileOpens.setStatus("mandatory")
_ServerAvgFileOpens_Type = Integer32
_ServerAvgFileOpens_Object = MibScalar
serverAvgFileOpens = _ServerAvgFileOpens_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 88),
    _ServerAvgFileOpens_Type()
)
serverAvgFileOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgFileOpens.setStatus("mandatory")
_ServerPeakFileOpens_Type = Integer32
_ServerPeakFileOpens_Object = MibScalar
serverPeakFileOpens = _ServerPeakFileOpens_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 89),
    _ServerPeakFileOpens_Type()
)
serverPeakFileOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakFileOpens.setStatus("mandatory")
_ServerCumlFileOpens_Type = Integer32
_ServerCumlFileOpens_Object = MibScalar
serverCumlFileOpens = _ServerCumlFileOpens_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 90),
    _ServerCumlFileOpens_Type()
)
serverCumlFileOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlFileOpens.setStatus("mandatory")
_ServerCurrFileDeletes_Type = Integer32
_ServerCurrFileDeletes_Object = MibScalar
serverCurrFileDeletes = _ServerCurrFileDeletes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 91),
    _ServerCurrFileDeletes_Type()
)
serverCurrFileDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrFileDeletes.setStatus("mandatory")
_ServerAvgFileDeletes_Type = Integer32
_ServerAvgFileDeletes_Object = MibScalar
serverAvgFileDeletes = _ServerAvgFileDeletes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 92),
    _ServerAvgFileDeletes_Type()
)
serverAvgFileDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgFileDeletes.setStatus("mandatory")
_ServerPeakFileDeletes_Type = Integer32
_ServerPeakFileDeletes_Object = MibScalar
serverPeakFileDeletes = _ServerPeakFileDeletes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 93),
    _ServerPeakFileDeletes_Type()
)
serverPeakFileDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakFileDeletes.setStatus("mandatory")
_ServerCumlFileDeletes_Type = Integer32
_ServerCumlFileDeletes_Object = MibScalar
serverCumlFileDeletes = _ServerCumlFileDeletes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 94),
    _ServerCumlFileDeletes_Type()
)
serverCumlFileDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlFileDeletes.setStatus("mandatory")
_ServerCurrFileReads_Type = Integer32
_ServerCurrFileReads_Object = MibScalar
serverCurrFileReads = _ServerCurrFileReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 95),
    _ServerCurrFileReads_Type()
)
serverCurrFileReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrFileReads.setStatus("mandatory")
_ServerAvgFileReads_Type = Integer32
_ServerAvgFileReads_Object = MibScalar
serverAvgFileReads = _ServerAvgFileReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 96),
    _ServerAvgFileReads_Type()
)
serverAvgFileReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgFileReads.setStatus("mandatory")
_ServerPeakFileReads_Type = Integer32
_ServerPeakFileReads_Object = MibScalar
serverPeakFileReads = _ServerPeakFileReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 97),
    _ServerPeakFileReads_Type()
)
serverPeakFileReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakFileReads.setStatus("mandatory")
_ServerCumlFileReads_Type = Integer32
_ServerCumlFileReads_Object = MibScalar
serverCumlFileReads = _ServerCumlFileReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 98),
    _ServerCumlFileReads_Type()
)
serverCumlFileReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlFileReads.setStatus("mandatory")
_ServerCurrFileReadBytes_Type = Integer32
_ServerCurrFileReadBytes_Object = MibScalar
serverCurrFileReadBytes = _ServerCurrFileReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 99),
    _ServerCurrFileReadBytes_Type()
)
serverCurrFileReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrFileReadBytes.setStatus("mandatory")
_ServerAvgFileReadBytes_Type = Integer32
_ServerAvgFileReadBytes_Object = MibScalar
serverAvgFileReadBytes = _ServerAvgFileReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 100),
    _ServerAvgFileReadBytes_Type()
)
serverAvgFileReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgFileReadBytes.setStatus("mandatory")
_ServerPeakFileReadBytes_Type = Integer32
_ServerPeakFileReadBytes_Object = MibScalar
serverPeakFileReadBytes = _ServerPeakFileReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 101),
    _ServerPeakFileReadBytes_Type()
)
serverPeakFileReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakFileReadBytes.setStatus("mandatory")
_ServerCumlFileReadBytes_Type = Integer32
_ServerCumlFileReadBytes_Object = MibScalar
serverCumlFileReadBytes = _ServerCumlFileReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 102),
    _ServerCumlFileReadBytes_Type()
)
serverCumlFileReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlFileReadBytes.setStatus("mandatory")
_ServerCurrFileWrites_Type = Integer32
_ServerCurrFileWrites_Object = MibScalar
serverCurrFileWrites = _ServerCurrFileWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 103),
    _ServerCurrFileWrites_Type()
)
serverCurrFileWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrFileWrites.setStatus("mandatory")
_ServerAvgFileWrites_Type = Integer32
_ServerAvgFileWrites_Object = MibScalar
serverAvgFileWrites = _ServerAvgFileWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 104),
    _ServerAvgFileWrites_Type()
)
serverAvgFileWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgFileWrites.setStatus("mandatory")
_ServerPeakFileWrites_Type = Integer32
_ServerPeakFileWrites_Object = MibScalar
serverPeakFileWrites = _ServerPeakFileWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 105),
    _ServerPeakFileWrites_Type()
)
serverPeakFileWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakFileWrites.setStatus("mandatory")
_ServerCumlFileWrites_Type = Integer32
_ServerCumlFileWrites_Object = MibScalar
serverCumlFileWrites = _ServerCumlFileWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 106),
    _ServerCumlFileWrites_Type()
)
serverCumlFileWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlFileWrites.setStatus("mandatory")
_ServerCurrFileWriteBytes_Type = Integer32
_ServerCurrFileWriteBytes_Object = MibScalar
serverCurrFileWriteBytes = _ServerCurrFileWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 107),
    _ServerCurrFileWriteBytes_Type()
)
serverCurrFileWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCurrFileWriteBytes.setStatus("mandatory")
_ServerAvgFileWriteBytes_Type = Integer32
_ServerAvgFileWriteBytes_Object = MibScalar
serverAvgFileWriteBytes = _ServerAvgFileWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 108),
    _ServerAvgFileWriteBytes_Type()
)
serverAvgFileWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAvgFileWriteBytes.setStatus("mandatory")
_ServerPeakFileWriteBytes_Type = Integer32
_ServerPeakFileWriteBytes_Object = MibScalar
serverPeakFileWriteBytes = _ServerPeakFileWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 109),
    _ServerPeakFileWriteBytes_Type()
)
serverPeakFileWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverPeakFileWriteBytes.setStatus("mandatory")
_ServerCumlFileWriteBytes_Type = Integer32
_ServerCumlFileWriteBytes_Object = MibScalar
serverCumlFileWriteBytes = _ServerCumlFileWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 8, 110),
    _ServerCumlFileWriteBytes_Type()
)
serverCumlFileWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCumlFileWriteBytes.setStatus("mandatory")
_Servertrends_ObjectIdentity = ObjectIdentity
servertrends = _Servertrends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9)
)
_ServerTrendTable_Object = MibTable
serverTrendTable = _ServerTrendTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1)
)
if mibBuilder.loadTexts:
    serverTrendTable.setStatus("mandatory")
_ServerTrendEntry_Object = MibTableRow
serverTrendEntry = _ServerTrendEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1)
)
serverTrendEntry.setIndexNames(
    (0, "NConsole-MIB", "serverTrendIndex"),
)
if mibBuilder.loadTexts:
    serverTrendEntry.setStatus("mandatory")
_ServerTrendIndex_Type = Integer32
_ServerTrendIndex_Object = MibTableColumn
serverTrendIndex = _ServerTrendIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 1),
    _ServerTrendIndex_Type()
)
serverTrendIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendIndex.setStatus("mandatory")


class _ServerTrendStartTime_Type(DisplayString):
    """Custom type serverTrendStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ServerTrendStartTime_Type.__name__ = "DisplayString"
_ServerTrendStartTime_Object = MibTableColumn
serverTrendStartTime = _ServerTrendStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 2),
    _ServerTrendStartTime_Type()
)
serverTrendStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendStartTime.setStatus("mandatory")
_ServerTrendStartUTC_Type = Integer32
_ServerTrendStartUTC_Object = MibTableColumn
serverTrendStartUTC = _ServerTrendStartUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 3),
    _ServerTrendStartUTC_Type()
)
serverTrendStartUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendStartUTC.setStatus("mandatory")


class _ServerTrendStopTime_Type(DisplayString):
    """Custom type serverTrendStopTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ServerTrendStopTime_Type.__name__ = "DisplayString"
_ServerTrendStopTime_Object = MibTableColumn
serverTrendStopTime = _ServerTrendStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 4),
    _ServerTrendStopTime_Type()
)
serverTrendStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendStopTime.setStatus("mandatory")
_ServerTrendStopUTC_Type = Integer32
_ServerTrendStopUTC_Object = MibTableColumn
serverTrendStopUTC = _ServerTrendStopUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 5),
    _ServerTrendStopUTC_Type()
)
serverTrendStopUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendStopUTC.setStatus("mandatory")
_ServerTrendUpTime_Type = TimeTicks
_ServerTrendUpTime_Object = MibTableColumn
serverTrendUpTime = _ServerTrendUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 6),
    _ServerTrendUpTime_Type()
)
serverTrendUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendUpTime.setStatus("mandatory")
_ServerTrendCacheLRU_Type = TimeTicks
_ServerTrendCacheLRU_Object = MibTableColumn
serverTrendCacheLRU = _ServerTrendCacheLRU_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 7),
    _ServerTrendCacheLRU_Type()
)
serverTrendCacheLRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCacheLRU.setStatus("mandatory")
_ServerTrendAvgUtil_Type = Integer32
_ServerTrendAvgUtil_Object = MibTableColumn
serverTrendAvgUtil = _ServerTrendAvgUtil_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 8),
    _ServerTrendAvgUtil_Type()
)
serverTrendAvgUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgUtil.setStatus("mandatory")
_ServerTrendPeakUtil_Type = Integer32
_ServerTrendPeakUtil_Object = MibTableColumn
serverTrendPeakUtil = _ServerTrendPeakUtil_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 9),
    _ServerTrendPeakUtil_Type()
)
serverTrendPeakUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakUtil.setStatus("mandatory")
_ServerTrendAvgConns_Type = Integer32
_ServerTrendAvgConns_Object = MibTableColumn
serverTrendAvgConns = _ServerTrendAvgConns_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 10),
    _ServerTrendAvgConns_Type()
)
serverTrendAvgConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgConns.setStatus("mandatory")
_ServerTrendPeakConns_Type = Integer32
_ServerTrendPeakConns_Object = MibTableColumn
serverTrendPeakConns = _ServerTrendPeakConns_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 11),
    _ServerTrendPeakConns_Type()
)
serverTrendPeakConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakConns.setStatus("mandatory")
_ServerTrendAvgUsers_Type = Integer32
_ServerTrendAvgUsers_Object = MibTableColumn
serverTrendAvgUsers = _ServerTrendAvgUsers_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 12),
    _ServerTrendAvgUsers_Type()
)
serverTrendAvgUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgUsers.setStatus("mandatory")
_ServerTrendPeakUsers_Type = Integer32
_ServerTrendPeakUsers_Object = MibTableColumn
serverTrendPeakUsers = _ServerTrendPeakUsers_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 13),
    _ServerTrendPeakUsers_Type()
)
serverTrendPeakUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakUsers.setStatus("mandatory")
_ServerTrendAvgFSPs_Type = Integer32
_ServerTrendAvgFSPs_Object = MibTableColumn
serverTrendAvgFSPs = _ServerTrendAvgFSPs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 14),
    _ServerTrendAvgFSPs_Type()
)
serverTrendAvgFSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgFSPs.setStatus("mandatory")
_ServerTrendPeakFSPs_Type = Integer32
_ServerTrendPeakFSPs_Object = MibTableColumn
serverTrendPeakFSPs = _ServerTrendPeakFSPs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 15),
    _ServerTrendPeakFSPs_Type()
)
serverTrendPeakFSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakFSPs.setStatus("mandatory")
_ServerTrendAvgProcs_Type = Integer32
_ServerTrendAvgProcs_Object = MibTableColumn
serverTrendAvgProcs = _ServerTrendAvgProcs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 16),
    _ServerTrendAvgProcs_Type()
)
serverTrendAvgProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgProcs.setStatus("mandatory")
_ServerTrendPeakProcs_Type = Integer32
_ServerTrendPeakProcs_Object = MibTableColumn
serverTrendPeakProcs = _ServerTrendPeakProcs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 17),
    _ServerTrendPeakProcs_Type()
)
serverTrendPeakProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakProcs.setStatus("mandatory")
_ServerTrendAvgCacheRatio_Type = Integer32
_ServerTrendAvgCacheRatio_Object = MibTableColumn
serverTrendAvgCacheRatio = _ServerTrendAvgCacheRatio_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 18),
    _ServerTrendAvgCacheRatio_Type()
)
serverTrendAvgCacheRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgCacheRatio.setStatus("mandatory")
_ServerTrendMinCacheRatio_Type = Integer32
_ServerTrendMinCacheRatio_Object = MibTableColumn
serverTrendMinCacheRatio = _ServerTrendMinCacheRatio_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 19),
    _ServerTrendMinCacheRatio_Type()
)
serverTrendMinCacheRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendMinCacheRatio.setStatus("mandatory")
_ServerTrendAvgCacheHits_Type = Integer32
_ServerTrendAvgCacheHits_Object = MibTableColumn
serverTrendAvgCacheHits = _ServerTrendAvgCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 20),
    _ServerTrendAvgCacheHits_Type()
)
serverTrendAvgCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgCacheHits.setStatus("mandatory")
_ServerTrendMinCacheHits_Type = Integer32
_ServerTrendMinCacheHits_Object = MibTableColumn
serverTrendMinCacheHits = _ServerTrendMinCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 21),
    _ServerTrendMinCacheHits_Type()
)
serverTrendMinCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendMinCacheHits.setStatus("mandatory")
_ServerTrendAvgDirBuffs_Type = Integer32
_ServerTrendAvgDirBuffs_Object = MibTableColumn
serverTrendAvgDirBuffs = _ServerTrendAvgDirBuffs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 22),
    _ServerTrendAvgDirBuffs_Type()
)
serverTrendAvgDirBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgDirBuffs.setStatus("mandatory")
_ServerTrendPeakDirBuffs_Type = Integer32
_ServerTrendPeakDirBuffs_Object = MibTableColumn
serverTrendPeakDirBuffs = _ServerTrendPeakDirBuffs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 23),
    _ServerTrendPeakDirBuffs_Type()
)
serverTrendPeakDirBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakDirBuffs.setStatus("mandatory")
_ServerTrendAvgRecvBuffs_Type = Integer32
_ServerTrendAvgRecvBuffs_Object = MibTableColumn
serverTrendAvgRecvBuffs = _ServerTrendAvgRecvBuffs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 24),
    _ServerTrendAvgRecvBuffs_Type()
)
serverTrendAvgRecvBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgRecvBuffs.setStatus("mandatory")
_ServerTrendPeakRecvBuffs_Type = Integer32
_ServerTrendPeakRecvBuffs_Object = MibTableColumn
serverTrendPeakRecvBuffs = _ServerTrendPeakRecvBuffs_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 25),
    _ServerTrendPeakRecvBuffs_Type()
)
serverTrendPeakRecvBuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakRecvBuffs.setStatus("mandatory")
_ServerTrendAvgOpenFiles_Type = Integer32
_ServerTrendAvgOpenFiles_Object = MibTableColumn
serverTrendAvgOpenFiles = _ServerTrendAvgOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 26),
    _ServerTrendAvgOpenFiles_Type()
)
serverTrendAvgOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgOpenFiles.setStatus("mandatory")
_ServerTrendPeakOpenFiles_Type = Integer32
_ServerTrendPeakOpenFiles_Object = MibTableColumn
serverTrendPeakOpenFiles = _ServerTrendPeakOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 27),
    _ServerTrendPeakOpenFiles_Type()
)
serverTrendPeakOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakOpenFiles.setStatus("mandatory")
_ServerTrendAvgIOsPending_Type = Integer32
_ServerTrendAvgIOsPending_Object = MibTableColumn
serverTrendAvgIOsPending = _ServerTrendAvgIOsPending_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 28),
    _ServerTrendAvgIOsPending_Type()
)
serverTrendAvgIOsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgIOsPending.setStatus("mandatory")
_ServerTrendPeakIOsPending_Type = Integer32
_ServerTrendPeakIOsPending_Object = MibTableColumn
serverTrendPeakIOsPending = _ServerTrendPeakIOsPending_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 29),
    _ServerTrendPeakIOsPending_Type()
)
serverTrendPeakIOsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakIOsPending.setStatus("mandatory")
_ServerTrendCumlIOsPending_Type = Integer32
_ServerTrendCumlIOsPending_Object = MibTableColumn
serverTrendCumlIOsPending = _ServerTrendCumlIOsPending_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 30),
    _ServerTrendCumlIOsPending_Type()
)
serverTrendCumlIOsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlIOsPending.setStatus("mandatory")
_ServerTrendAvgDirtyBlocks_Type = Integer32
_ServerTrendAvgDirtyBlocks_Object = MibTableColumn
serverTrendAvgDirtyBlocks = _ServerTrendAvgDirtyBlocks_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 31),
    _ServerTrendAvgDirtyBlocks_Type()
)
serverTrendAvgDirtyBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgDirtyBlocks.setStatus("mandatory")
_ServerTrendPeakDirtyBlocks_Type = Integer32
_ServerTrendPeakDirtyBlocks_Object = MibTableColumn
serverTrendPeakDirtyBlocks = _ServerTrendPeakDirtyBlocks_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 32),
    _ServerTrendPeakDirtyBlocks_Type()
)
serverTrendPeakDirtyBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakDirtyBlocks.setStatus("mandatory")
_ServerTrendCumlDirtyBlocks_Type = Integer32
_ServerTrendCumlDirtyBlocks_Object = MibTableColumn
serverTrendCumlDirtyBlocks = _ServerTrendCumlDirtyBlocks_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 33),
    _ServerTrendCumlDirtyBlocks_Type()
)
serverTrendCumlDirtyBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlDirtyBlocks.setStatus("mandatory")
_ServerTrendAvgDiskReads_Type = Integer32
_ServerTrendAvgDiskReads_Object = MibTableColumn
serverTrendAvgDiskReads = _ServerTrendAvgDiskReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 34),
    _ServerTrendAvgDiskReads_Type()
)
serverTrendAvgDiskReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgDiskReads.setStatus("mandatory")
_ServerTrendPeakDiskReads_Type = Integer32
_ServerTrendPeakDiskReads_Object = MibTableColumn
serverTrendPeakDiskReads = _ServerTrendPeakDiskReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 35),
    _ServerTrendPeakDiskReads_Type()
)
serverTrendPeakDiskReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakDiskReads.setStatus("mandatory")
_ServerTrendCumlDiskReads_Type = Integer32
_ServerTrendCumlDiskReads_Object = MibTableColumn
serverTrendCumlDiskReads = _ServerTrendCumlDiskReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 36),
    _ServerTrendCumlDiskReads_Type()
)
serverTrendCumlDiskReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlDiskReads.setStatus("mandatory")
_ServerTrendAvgDiskReadBytes_Type = Integer32
_ServerTrendAvgDiskReadBytes_Object = MibTableColumn
serverTrendAvgDiskReadBytes = _ServerTrendAvgDiskReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 37),
    _ServerTrendAvgDiskReadBytes_Type()
)
serverTrendAvgDiskReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgDiskReadBytes.setStatus("mandatory")
_ServerTrendPeakDiskReadBytes_Type = Integer32
_ServerTrendPeakDiskReadBytes_Object = MibTableColumn
serverTrendPeakDiskReadBytes = _ServerTrendPeakDiskReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 38),
    _ServerTrendPeakDiskReadBytes_Type()
)
serverTrendPeakDiskReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakDiskReadBytes.setStatus("mandatory")
_ServerTrendCumlDiskReadBytes_Type = Integer32
_ServerTrendCumlDiskReadBytes_Object = MibTableColumn
serverTrendCumlDiskReadBytes = _ServerTrendCumlDiskReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 39),
    _ServerTrendCumlDiskReadBytes_Type()
)
serverTrendCumlDiskReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlDiskReadBytes.setStatus("mandatory")
_ServerTrendAvgDiskWrites_Type = Integer32
_ServerTrendAvgDiskWrites_Object = MibTableColumn
serverTrendAvgDiskWrites = _ServerTrendAvgDiskWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 40),
    _ServerTrendAvgDiskWrites_Type()
)
serverTrendAvgDiskWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgDiskWrites.setStatus("mandatory")
_ServerTrendPeakDiskWrites_Type = Integer32
_ServerTrendPeakDiskWrites_Object = MibTableColumn
serverTrendPeakDiskWrites = _ServerTrendPeakDiskWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 41),
    _ServerTrendPeakDiskWrites_Type()
)
serverTrendPeakDiskWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakDiskWrites.setStatus("mandatory")
_ServerTrendCumlDiskWrites_Type = Integer32
_ServerTrendCumlDiskWrites_Object = MibTableColumn
serverTrendCumlDiskWrites = _ServerTrendCumlDiskWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 42),
    _ServerTrendCumlDiskWrites_Type()
)
serverTrendCumlDiskWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlDiskWrites.setStatus("mandatory")
_ServerTrendAvgDiskWriteBytes_Type = Integer32
_ServerTrendAvgDiskWriteBytes_Object = MibTableColumn
serverTrendAvgDiskWriteBytes = _ServerTrendAvgDiskWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 43),
    _ServerTrendAvgDiskWriteBytes_Type()
)
serverTrendAvgDiskWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgDiskWriteBytes.setStatus("mandatory")
_ServerTrendPeakDiskWriteBytes_Type = Integer32
_ServerTrendPeakDiskWriteBytes_Object = MibTableColumn
serverTrendPeakDiskWriteBytes = _ServerTrendPeakDiskWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 44),
    _ServerTrendPeakDiskWriteBytes_Type()
)
serverTrendPeakDiskWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakDiskWriteBytes.setStatus("mandatory")
_ServerTrendCumlDiskWriteBytes_Type = Integer32
_ServerTrendCumlDiskWriteBytes_Object = MibTableColumn
serverTrendCumlDiskWriteBytes = _ServerTrendCumlDiskWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 45),
    _ServerTrendCumlDiskWriteBytes_Type()
)
serverTrendCumlDiskWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlDiskWriteBytes.setStatus("mandatory")
_ServerTrendAvgRoutedPkts_Type = Integer32
_ServerTrendAvgRoutedPkts_Object = MibTableColumn
serverTrendAvgRoutedPkts = _ServerTrendAvgRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 46),
    _ServerTrendAvgRoutedPkts_Type()
)
serverTrendAvgRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgRoutedPkts.setStatus("mandatory")
_ServerTrendPeakRoutedPkts_Type = Integer32
_ServerTrendPeakRoutedPkts_Object = MibTableColumn
serverTrendPeakRoutedPkts = _ServerTrendPeakRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 47),
    _ServerTrendPeakRoutedPkts_Type()
)
serverTrendPeakRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakRoutedPkts.setStatus("mandatory")
_ServerTrendCumlRoutedPkts_Type = Integer32
_ServerTrendCumlRoutedPkts_Object = MibTableColumn
serverTrendCumlRoutedPkts = _ServerTrendCumlRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 48),
    _ServerTrendCumlRoutedPkts_Type()
)
serverTrendCumlRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlRoutedPkts.setStatus("mandatory")
_ServerTrendAvgRxPkts_Type = Integer32
_ServerTrendAvgRxPkts_Object = MibTableColumn
serverTrendAvgRxPkts = _ServerTrendAvgRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 49),
    _ServerTrendAvgRxPkts_Type()
)
serverTrendAvgRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgRxPkts.setStatus("mandatory")
_ServerTrendPeakRxPkts_Type = Integer32
_ServerTrendPeakRxPkts_Object = MibTableColumn
serverTrendPeakRxPkts = _ServerTrendPeakRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 50),
    _ServerTrendPeakRxPkts_Type()
)
serverTrendPeakRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakRxPkts.setStatus("mandatory")
_ServerTrendCumlRxPkts_Type = Integer32
_ServerTrendCumlRxPkts_Object = MibTableColumn
serverTrendCumlRxPkts = _ServerTrendCumlRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 51),
    _ServerTrendCumlRxPkts_Type()
)
serverTrendCumlRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlRxPkts.setStatus("mandatory")
_ServerTrendAvgRxBytes_Type = Integer32
_ServerTrendAvgRxBytes_Object = MibTableColumn
serverTrendAvgRxBytes = _ServerTrendAvgRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 52),
    _ServerTrendAvgRxBytes_Type()
)
serverTrendAvgRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgRxBytes.setStatus("mandatory")
_ServerTrendPeakRxBytes_Type = Integer32
_ServerTrendPeakRxBytes_Object = MibTableColumn
serverTrendPeakRxBytes = _ServerTrendPeakRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 53),
    _ServerTrendPeakRxBytes_Type()
)
serverTrendPeakRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakRxBytes.setStatus("mandatory")
_ServerTrendCumlRxBytes_Type = Integer32
_ServerTrendCumlRxBytes_Object = MibTableColumn
serverTrendCumlRxBytes = _ServerTrendCumlRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 54),
    _ServerTrendCumlRxBytes_Type()
)
serverTrendCumlRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlRxBytes.setStatus("mandatory")
_ServerTrendAvgTxPkts_Type = Integer32
_ServerTrendAvgTxPkts_Object = MibTableColumn
serverTrendAvgTxPkts = _ServerTrendAvgTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 55),
    _ServerTrendAvgTxPkts_Type()
)
serverTrendAvgTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgTxPkts.setStatus("mandatory")
_ServerTrendPeakTxPkts_Type = Integer32
_ServerTrendPeakTxPkts_Object = MibTableColumn
serverTrendPeakTxPkts = _ServerTrendPeakTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 56),
    _ServerTrendPeakTxPkts_Type()
)
serverTrendPeakTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakTxPkts.setStatus("mandatory")
_ServerTrendCumlTxPkts_Type = Integer32
_ServerTrendCumlTxPkts_Object = MibTableColumn
serverTrendCumlTxPkts = _ServerTrendCumlTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 57),
    _ServerTrendCumlTxPkts_Type()
)
serverTrendCumlTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlTxPkts.setStatus("mandatory")
_ServerTrendAvgTxBytes_Type = Integer32
_ServerTrendAvgTxBytes_Object = MibTableColumn
serverTrendAvgTxBytes = _ServerTrendAvgTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 58),
    _ServerTrendAvgTxBytes_Type()
)
serverTrendAvgTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgTxBytes.setStatus("mandatory")
_ServerTrendPeakTxBytes_Type = Integer32
_ServerTrendPeakTxBytes_Object = MibTableColumn
serverTrendPeakTxBytes = _ServerTrendPeakTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 59),
    _ServerTrendPeakTxBytes_Type()
)
serverTrendPeakTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakTxBytes.setStatus("mandatory")
_ServerTrendCumlTxBytes_Type = Integer32
_ServerTrendCumlTxBytes_Object = MibTableColumn
serverTrendCumlTxBytes = _ServerTrendCumlTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 60),
    _ServerTrendCumlTxBytes_Type()
)
serverTrendCumlTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlTxBytes.setStatus("mandatory")
_ServerTrendAvgDirSearch_Type = Integer32
_ServerTrendAvgDirSearch_Object = MibTableColumn
serverTrendAvgDirSearch = _ServerTrendAvgDirSearch_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 61),
    _ServerTrendAvgDirSearch_Type()
)
serverTrendAvgDirSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgDirSearch.setStatus("mandatory")
_ServerTrendPeakDirSearch_Type = Integer32
_ServerTrendPeakDirSearch_Object = MibTableColumn
serverTrendPeakDirSearch = _ServerTrendPeakDirSearch_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 62),
    _ServerTrendPeakDirSearch_Type()
)
serverTrendPeakDirSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakDirSearch.setStatus("mandatory")
_ServerTrendCumlDirSearch_Type = Integer32
_ServerTrendCumlDirSearch_Object = MibTableColumn
serverTrendCumlDirSearch = _ServerTrendCumlDirSearch_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 63),
    _ServerTrendCumlDirSearch_Type()
)
serverTrendCumlDirSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlDirSearch.setStatus("mandatory")
_ServerTrendAvgFileCreates_Type = Integer32
_ServerTrendAvgFileCreates_Object = MibTableColumn
serverTrendAvgFileCreates = _ServerTrendAvgFileCreates_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 64),
    _ServerTrendAvgFileCreates_Type()
)
serverTrendAvgFileCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgFileCreates.setStatus("mandatory")
_ServerTrendPeakFileCreates_Type = Integer32
_ServerTrendPeakFileCreates_Object = MibTableColumn
serverTrendPeakFileCreates = _ServerTrendPeakFileCreates_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 65),
    _ServerTrendPeakFileCreates_Type()
)
serverTrendPeakFileCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakFileCreates.setStatus("mandatory")
_ServerTrendCumlFileCreates_Type = Integer32
_ServerTrendCumlFileCreates_Object = MibTableColumn
serverTrendCumlFileCreates = _ServerTrendCumlFileCreates_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 66),
    _ServerTrendCumlFileCreates_Type()
)
serverTrendCumlFileCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlFileCreates.setStatus("mandatory")
_ServerTrendAvgFileOpens_Type = Integer32
_ServerTrendAvgFileOpens_Object = MibTableColumn
serverTrendAvgFileOpens = _ServerTrendAvgFileOpens_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 67),
    _ServerTrendAvgFileOpens_Type()
)
serverTrendAvgFileOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgFileOpens.setStatus("mandatory")
_ServerTrendPeakFileOpens_Type = Integer32
_ServerTrendPeakFileOpens_Object = MibTableColumn
serverTrendPeakFileOpens = _ServerTrendPeakFileOpens_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 68),
    _ServerTrendPeakFileOpens_Type()
)
serverTrendPeakFileOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakFileOpens.setStatus("mandatory")
_ServerTrendCumlFileOpens_Type = Integer32
_ServerTrendCumlFileOpens_Object = MibTableColumn
serverTrendCumlFileOpens = _ServerTrendCumlFileOpens_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 69),
    _ServerTrendCumlFileOpens_Type()
)
serverTrendCumlFileOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlFileOpens.setStatus("mandatory")
_ServerTrendAvgFileDeletes_Type = Integer32
_ServerTrendAvgFileDeletes_Object = MibTableColumn
serverTrendAvgFileDeletes = _ServerTrendAvgFileDeletes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 70),
    _ServerTrendAvgFileDeletes_Type()
)
serverTrendAvgFileDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgFileDeletes.setStatus("mandatory")
_ServerTrendPeakFileDeletes_Type = Integer32
_ServerTrendPeakFileDeletes_Object = MibTableColumn
serverTrendPeakFileDeletes = _ServerTrendPeakFileDeletes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 71),
    _ServerTrendPeakFileDeletes_Type()
)
serverTrendPeakFileDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakFileDeletes.setStatus("mandatory")
_ServerTrendCumlFileDeletes_Type = Integer32
_ServerTrendCumlFileDeletes_Object = MibTableColumn
serverTrendCumlFileDeletes = _ServerTrendCumlFileDeletes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 72),
    _ServerTrendCumlFileDeletes_Type()
)
serverTrendCumlFileDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlFileDeletes.setStatus("mandatory")
_ServerTrendAvgFileReads_Type = Integer32
_ServerTrendAvgFileReads_Object = MibTableColumn
serverTrendAvgFileReads = _ServerTrendAvgFileReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 73),
    _ServerTrendAvgFileReads_Type()
)
serverTrendAvgFileReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgFileReads.setStatus("mandatory")
_ServerTrendPeakFileReads_Type = Integer32
_ServerTrendPeakFileReads_Object = MibTableColumn
serverTrendPeakFileReads = _ServerTrendPeakFileReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 74),
    _ServerTrendPeakFileReads_Type()
)
serverTrendPeakFileReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakFileReads.setStatus("mandatory")
_ServerTrendCumlFileReads_Type = Integer32
_ServerTrendCumlFileReads_Object = MibTableColumn
serverTrendCumlFileReads = _ServerTrendCumlFileReads_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 75),
    _ServerTrendCumlFileReads_Type()
)
serverTrendCumlFileReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlFileReads.setStatus("mandatory")
_ServerTrendAvgFileReadBytes_Type = Integer32
_ServerTrendAvgFileReadBytes_Object = MibTableColumn
serverTrendAvgFileReadBytes = _ServerTrendAvgFileReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 76),
    _ServerTrendAvgFileReadBytes_Type()
)
serverTrendAvgFileReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgFileReadBytes.setStatus("mandatory")
_ServerTrendPeakFileReadBytes_Type = Integer32
_ServerTrendPeakFileReadBytes_Object = MibTableColumn
serverTrendPeakFileReadBytes = _ServerTrendPeakFileReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 77),
    _ServerTrendPeakFileReadBytes_Type()
)
serverTrendPeakFileReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakFileReadBytes.setStatus("mandatory")
_ServerTrendCumlFileReadBytes_Type = Integer32
_ServerTrendCumlFileReadBytes_Object = MibTableColumn
serverTrendCumlFileReadBytes = _ServerTrendCumlFileReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 78),
    _ServerTrendCumlFileReadBytes_Type()
)
serverTrendCumlFileReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlFileReadBytes.setStatus("mandatory")
_ServerTrendAvgFileWrites_Type = Integer32
_ServerTrendAvgFileWrites_Object = MibTableColumn
serverTrendAvgFileWrites = _ServerTrendAvgFileWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 79),
    _ServerTrendAvgFileWrites_Type()
)
serverTrendAvgFileWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgFileWrites.setStatus("mandatory")
_ServerTrendPeakFileWrites_Type = Integer32
_ServerTrendPeakFileWrites_Object = MibTableColumn
serverTrendPeakFileWrites = _ServerTrendPeakFileWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 80),
    _ServerTrendPeakFileWrites_Type()
)
serverTrendPeakFileWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakFileWrites.setStatus("mandatory")
_ServerTrendCumlFileWrites_Type = Integer32
_ServerTrendCumlFileWrites_Object = MibTableColumn
serverTrendCumlFileWrites = _ServerTrendCumlFileWrites_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 81),
    _ServerTrendCumlFileWrites_Type()
)
serverTrendCumlFileWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlFileWrites.setStatus("mandatory")
_ServerTrendAvgFileWriteBytes_Type = Integer32
_ServerTrendAvgFileWriteBytes_Object = MibTableColumn
serverTrendAvgFileWriteBytes = _ServerTrendAvgFileWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 82),
    _ServerTrendAvgFileWriteBytes_Type()
)
serverTrendAvgFileWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendAvgFileWriteBytes.setStatus("mandatory")
_ServerTrendPeakFileWriteBytes_Type = Integer32
_ServerTrendPeakFileWriteBytes_Object = MibTableColumn
serverTrendPeakFileWriteBytes = _ServerTrendPeakFileWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 83),
    _ServerTrendPeakFileWriteBytes_Type()
)
serverTrendPeakFileWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendPeakFileWriteBytes.setStatus("mandatory")
_ServerTrendCumlFileWriteBytes_Type = Integer32
_ServerTrendCumlFileWriteBytes_Object = MibTableColumn
serverTrendCumlFileWriteBytes = _ServerTrendCumlFileWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 84),
    _ServerTrendCumlFileWriteBytes_Type()
)
serverTrendCumlFileWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendCumlFileWriteBytes.setStatus("mandatory")
_ServerTrendMemoryAllocPoolTotal_Type = Integer32
_ServerTrendMemoryAllocPoolTotal_Object = MibTableColumn
serverTrendMemoryAllocPoolTotal = _ServerTrendMemoryAllocPoolTotal_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 85),
    _ServerTrendMemoryAllocPoolTotal_Type()
)
serverTrendMemoryAllocPoolTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendMemoryAllocPoolTotal.setStatus("mandatory")
_ServerTrendMemoryAllocPoolInUse_Type = Integer32
_ServerTrendMemoryAllocPoolInUse_Object = MibTableColumn
serverTrendMemoryAllocPoolInUse = _ServerTrendMemoryAllocPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 86),
    _ServerTrendMemoryAllocPoolInUse_Type()
)
serverTrendMemoryAllocPoolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendMemoryAllocPoolInUse.setStatus("mandatory")
_ServerTrendMemoryCacheBufferPool_Type = Integer32
_ServerTrendMemoryCacheBufferPool_Object = MibTableColumn
serverTrendMemoryCacheBufferPool = _ServerTrendMemoryCacheBufferPool_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 87),
    _ServerTrendMemoryCacheBufferPool_Type()
)
serverTrendMemoryCacheBufferPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendMemoryCacheBufferPool.setStatus("mandatory")
_ServerTrendMemoryCacheMovablePool_Type = Integer32
_ServerTrendMemoryCacheMovablePool_Object = MibTableColumn
serverTrendMemoryCacheMovablePool = _ServerTrendMemoryCacheMovablePool_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 88),
    _ServerTrendMemoryCacheMovablePool_Type()
)
serverTrendMemoryCacheMovablePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendMemoryCacheMovablePool.setStatus("mandatory")
_ServerTrendMemoryCacheNonMovablePool_Type = Integer32
_ServerTrendMemoryCacheNonMovablePool_Object = MibTableColumn
serverTrendMemoryCacheNonMovablePool = _ServerTrendMemoryCacheNonMovablePool_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 89),
    _ServerTrendMemoryCacheNonMovablePool_Type()
)
serverTrendMemoryCacheNonMovablePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendMemoryCacheNonMovablePool.setStatus("mandatory")
_ServerTrendMemoryNw3PermMemoryPoolTotal_Type = Integer32
_ServerTrendMemoryNw3PermMemoryPoolTotal_Object = MibTableColumn
serverTrendMemoryNw3PermMemoryPoolTotal = _ServerTrendMemoryNw3PermMemoryPoolTotal_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 90),
    _ServerTrendMemoryNw3PermMemoryPoolTotal_Type()
)
serverTrendMemoryNw3PermMemoryPoolTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendMemoryNw3PermMemoryPoolTotal.setStatus("mandatory")
_ServerTrendMemoryNw3PermMemoryPoolInUse_Type = Integer32
_ServerTrendMemoryNw3PermMemoryPoolInUse_Object = MibTableColumn
serverTrendMemoryNw3PermMemoryPoolInUse = _ServerTrendMemoryNw3PermMemoryPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 91),
    _ServerTrendMemoryNw3PermMemoryPoolInUse_Type()
)
serverTrendMemoryNw3PermMemoryPoolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendMemoryNw3PermMemoryPoolInUse.setStatus("mandatory")
_ServerTrendMemoryNw4CodeDataPool_Type = Integer32
_ServerTrendMemoryNw4CodeDataPool_Object = MibTableColumn
serverTrendMemoryNw4CodeDataPool = _ServerTrendMemoryNw4CodeDataPool_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 9, 1, 1, 92),
    _ServerTrendMemoryNw4CodeDataPool_Type()
)
serverTrendMemoryNw4CodeDataPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverTrendMemoryNw4CodeDataPool.setStatus("mandatory")
_Volinfo_ObjectIdentity = ObjectIdentity
volinfo = _Volinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10)
)
_VolCount_Type = Integer32
_VolCount_Object = MibScalar
volCount = _VolCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 1),
    _VolCount_Type()
)
volCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCount.setStatus("mandatory")
_VolTable_Object = MibTable
volTable = _VolTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2)
)
if mibBuilder.loadTexts:
    volTable.setStatus("mandatory")
_VolEntry_Object = MibTableRow
volEntry = _VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2, 1)
)
volEntry.setIndexNames(
    (0, "NConsole-MIB", "volIndex"),
)
if mibBuilder.loadTexts:
    volEntry.setStatus("mandatory")
_VolIndex_Type = Integer32
_VolIndex_Object = MibTableColumn
volIndex = _VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2, 1, 1),
    _VolIndex_Type()
)
volIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIndex.setStatus("mandatory")


class _VolName_Type(DisplayString):
    """Custom type volName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VolName_Type.__name__ = "DisplayString"
_VolName_Object = MibTableColumn
volName = _VolName_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2, 1, 2),
    _VolName_Type()
)
volName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volName.setStatus("mandatory")
_VolDriveNumber_Type = Integer32
_VolDriveNumber_Object = MibTableColumn
volDriveNumber = _VolDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2, 1, 3),
    _VolDriveNumber_Type()
)
volDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDriveNumber.setStatus("mandatory")
_VolBlockSize_Type = Integer32
_VolBlockSize_Object = MibTableColumn
volBlockSize = _VolBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2, 1, 4),
    _VolBlockSize_Type()
)
volBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volBlockSize.setStatus("mandatory")
_VolDirSlots_Type = Integer32
_VolDirSlots_Object = MibTableColumn
volDirSlots = _VolDirSlots_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2, 1, 5),
    _VolDirSlots_Type()
)
volDirSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDirSlots.setStatus("mandatory")
_VolDirSlotsFree_Type = Integer32
_VolDirSlotsFree_Object = MibTableColumn
volDirSlotsFree = _VolDirSlotsFree_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2, 1, 6),
    _VolDirSlotsFree_Type()
)
volDirSlotsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDirSlotsFree.setStatus("mandatory")
_VolDiskSpace_Type = Integer32
_VolDiskSpace_Object = MibTableColumn
volDiskSpace = _VolDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2, 1, 7),
    _VolDiskSpace_Type()
)
volDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDiskSpace.setStatus("mandatory")
_VolDiskSpaceFree_Type = Integer32
_VolDiskSpaceFree_Object = MibTableColumn
volDiskSpaceFree = _VolDiskSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2, 1, 8),
    _VolDiskSpaceFree_Type()
)
volDiskSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDiskSpaceFree.setStatus("mandatory")
_VolDiskSpacePurgable_Type = Integer32
_VolDiskSpacePurgable_Object = MibTableColumn
volDiskSpacePurgable = _VolDiskSpacePurgable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2, 1, 9),
    _VolDiskSpacePurgable_Type()
)
volDiskSpacePurgable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDiskSpacePurgable.setStatus("mandatory")
_VolDiskSpaceNotYetPurgable_Type = Integer32
_VolDiskSpaceNotYetPurgable_Object = MibTableColumn
volDiskSpaceNotYetPurgable = _VolDiskSpaceNotYetPurgable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 10, 2, 1, 10),
    _VolDiskSpaceNotYetPurgable_Type()
)
volDiskSpaceNotYetPurgable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDiskSpaceNotYetPurgable.setStatus("mandatory")
_Voltrends_ObjectIdentity = ObjectIdentity
voltrends = _Voltrends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11)
)
_VolTrendTable_Object = MibTable
volTrendTable = _VolTrendTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1)
)
if mibBuilder.loadTexts:
    volTrendTable.setStatus("mandatory")
_VolTrendEntry_Object = MibTableRow
volTrendEntry = _VolTrendEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1)
)
volTrendEntry.setIndexNames(
    (0, "NConsole-MIB", "volTrendCycleIndex"),
    (0, "NConsole-MIB", "volTrendVolumeIndex"),
)
if mibBuilder.loadTexts:
    volTrendEntry.setStatus("mandatory")
_VolTrendCycleIndex_Type = Integer32
_VolTrendCycleIndex_Object = MibTableColumn
volTrendCycleIndex = _VolTrendCycleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 1),
    _VolTrendCycleIndex_Type()
)
volTrendCycleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendCycleIndex.setStatus("mandatory")
_VolTrendVolumeIndex_Type = Integer32
_VolTrendVolumeIndex_Object = MibTableColumn
volTrendVolumeIndex = _VolTrendVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 2),
    _VolTrendVolumeIndex_Type()
)
volTrendVolumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendVolumeIndex.setStatus("mandatory")


class _VolTrendStartTime_Type(DisplayString):
    """Custom type volTrendStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VolTrendStartTime_Type.__name__ = "DisplayString"
_VolTrendStartTime_Object = MibTableColumn
volTrendStartTime = _VolTrendStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 3),
    _VolTrendStartTime_Type()
)
volTrendStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendStartTime.setStatus("mandatory")
_VolTrendStartUTC_Type = Integer32
_VolTrendStartUTC_Object = MibTableColumn
volTrendStartUTC = _VolTrendStartUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 4),
    _VolTrendStartUTC_Type()
)
volTrendStartUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendStartUTC.setStatus("mandatory")


class _VolTrendStopTime_Type(DisplayString):
    """Custom type volTrendStopTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VolTrendStopTime_Type.__name__ = "DisplayString"
_VolTrendStopTime_Object = MibTableColumn
volTrendStopTime = _VolTrendStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 5),
    _VolTrendStopTime_Type()
)
volTrendStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendStopTime.setStatus("mandatory")
_VolTrendStopUTC_Type = Integer32
_VolTrendStopUTC_Object = MibTableColumn
volTrendStopUTC = _VolTrendStopUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 6),
    _VolTrendStopUTC_Type()
)
volTrendStopUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendStopUTC.setStatus("mandatory")


class _VolTrendName_Type(DisplayString):
    """Custom type volTrendName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VolTrendName_Type.__name__ = "DisplayString"
_VolTrendName_Object = MibTableColumn
volTrendName = _VolTrendName_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 7),
    _VolTrendName_Type()
)
volTrendName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendName.setStatus("mandatory")
_VolTrendDirSlots_Type = Integer32
_VolTrendDirSlots_Object = MibTableColumn
volTrendDirSlots = _VolTrendDirSlots_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 8),
    _VolTrendDirSlots_Type()
)
volTrendDirSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendDirSlots.setStatus("mandatory")
_VolTrendDirSlotsFree_Type = Integer32
_VolTrendDirSlotsFree_Object = MibTableColumn
volTrendDirSlotsFree = _VolTrendDirSlotsFree_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 9),
    _VolTrendDirSlotsFree_Type()
)
volTrendDirSlotsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendDirSlotsFree.setStatus("mandatory")
_VolTrendDiskSpace_Type = Integer32
_VolTrendDiskSpace_Object = MibTableColumn
volTrendDiskSpace = _VolTrendDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 10),
    _VolTrendDiskSpace_Type()
)
volTrendDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendDiskSpace.setStatus("mandatory")
_VolTrendDiskSpaceFree_Type = Integer32
_VolTrendDiskSpaceFree_Object = MibTableColumn
volTrendDiskSpaceFree = _VolTrendDiskSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 11),
    _VolTrendDiskSpaceFree_Type()
)
volTrendDiskSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendDiskSpaceFree.setStatus("mandatory")
_VolTrendDiskSpacePurgable_Type = Integer32
_VolTrendDiskSpacePurgable_Object = MibTableColumn
volTrendDiskSpacePurgable = _VolTrendDiskSpacePurgable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 12),
    _VolTrendDiskSpacePurgable_Type()
)
volTrendDiskSpacePurgable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendDiskSpacePurgable.setStatus("mandatory")
_VolTrendDiskSpaceNotYetPurgable_Type = Integer32
_VolTrendDiskSpaceNotYetPurgable_Object = MibTableColumn
volTrendDiskSpaceNotYetPurgable = _VolTrendDiskSpaceNotYetPurgable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 11, 1, 1, 13),
    _VolTrendDiskSpaceNotYetPurgable_Type()
)
volTrendDiskSpaceNotYetPurgable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTrendDiskSpaceNotYetPurgable.setStatus("mandatory")
_Driveinfo_ObjectIdentity = ObjectIdentity
driveinfo = _Driveinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12)
)
_DriveCount_Type = Integer32
_DriveCount_Object = MibScalar
driveCount = _DriveCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 1),
    _DriveCount_Type()
)
driveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveCount.setStatus("mandatory")
_DriveTable_Object = MibTable
driveTable = _DriveTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2)
)
if mibBuilder.loadTexts:
    driveTable.setStatus("mandatory")
_DriveEntry_Object = MibTableRow
driveEntry = _DriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1)
)
driveEntry.setIndexNames(
    (0, "NConsole-MIB", "driveIndex"),
)
if mibBuilder.loadTexts:
    driveEntry.setStatus("mandatory")
_DriveIndex_Type = Integer32
_DriveIndex_Object = MibTableColumn
driveIndex = _DriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 1),
    _DriveIndex_Type()
)
driveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveIndex.setStatus("mandatory")


class _DriveDesc_Type(DisplayString):
    """Custom type driveDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DriveDesc_Type.__name__ = "DisplayString"
_DriveDesc_Object = MibTableColumn
driveDesc = _DriveDesc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 2),
    _DriveDesc_Type()
)
driveDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveDesc.setStatus("mandatory")


class _DriveType_Type(DisplayString):
    """Custom type driveType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DriveType_Type.__name__ = "DisplayString"
_DriveType_Object = MibTableColumn
driveType = _DriveType_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 3),
    _DriveType_Type()
)
driveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveType.setStatus("mandatory")
_DriveControllerCardID_Type = Integer32
_DriveControllerCardID_Object = MibTableColumn
driveControllerCardID = _DriveControllerCardID_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 4),
    _DriveControllerCardID_Type()
)
driveControllerCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveControllerCardID.setStatus("mandatory")
_DriveControllerDeviceID_Type = Integer32
_DriveControllerDeviceID_Object = MibTableColumn
driveControllerDeviceID = _DriveControllerDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 5),
    _DriveControllerDeviceID_Type()
)
driveControllerDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveControllerDeviceID.setStatus("mandatory")
_DriveControllerDriveID_Type = Integer32
_DriveControllerDriveID_Object = MibTableColumn
driveControllerDriveID = _DriveControllerDriveID_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 6),
    _DriveControllerDriveID_Type()
)
driveControllerDriveID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveControllerDriveID.setStatus("mandatory")
_DriveCylinderCount_Type = Integer32
_DriveCylinderCount_Object = MibTableColumn
driveCylinderCount = _DriveCylinderCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 7),
    _DriveCylinderCount_Type()
)
driveCylinderCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveCylinderCount.setStatus("mandatory")
_DriveHeadCount_Type = Integer32
_DriveHeadCount_Object = MibTableColumn
driveHeadCount = _DriveHeadCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 8),
    _DriveHeadCount_Type()
)
driveHeadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveHeadCount.setStatus("mandatory")
_DriveSectorsPerTrack_Type = Integer32
_DriveSectorsPerTrack_Object = MibTableColumn
driveSectorsPerTrack = _DriveSectorsPerTrack_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 9),
    _DriveSectorsPerTrack_Type()
)
driveSectorsPerTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveSectorsPerTrack.setStatus("mandatory")
_DriveSize_Type = Integer32
_DriveSize_Object = MibTableColumn
driveSize = _DriveSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 10),
    _DriveSize_Type()
)
driveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveSize.setStatus("mandatory")
_DriveNumberOfPartitions_Type = Integer32
_DriveNumberOfPartitions_Object = MibTableColumn
driveNumberOfPartitions = _DriveNumberOfPartitions_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 11),
    _DriveNumberOfPartitions_Type()
)
driveNumberOfPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveNumberOfPartitions.setStatus("mandatory")


class _DriveNetWarePartitionStatus_Type(DisplayString):
    """Custom type driveNetWarePartitionStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DriveNetWarePartitionStatus_Type.__name__ = "DisplayString"
_DriveNetWarePartitionStatus_Object = MibTableColumn
driveNetWarePartitionStatus = _DriveNetWarePartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 12),
    _DriveNetWarePartitionStatus_Type()
)
driveNetWarePartitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveNetWarePartitionStatus.setStatus("mandatory")


class _DriveNetWarePartitionType_Type(DisplayString):
    """Custom type driveNetWarePartitionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DriveNetWarePartitionType_Type.__name__ = "DisplayString"
_DriveNetWarePartitionType_Object = MibTableColumn
driveNetWarePartitionType = _DriveNetWarePartitionType_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 13),
    _DriveNetWarePartitionType_Type()
)
driveNetWarePartitionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveNetWarePartitionType.setStatus("mandatory")
_DriveNetWarePartitionSize_Type = Integer32
_DriveNetWarePartitionSize_Object = MibTableColumn
driveNetWarePartitionSize = _DriveNetWarePartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 14),
    _DriveNetWarePartitionSize_Type()
)
driveNetWarePartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveNetWarePartitionSize.setStatus("mandatory")


class _DriveMirrorFlag_Type(DisplayString):
    """Custom type driveMirrorFlag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_DriveMirrorFlag_Type.__name__ = "DisplayString"
_DriveMirrorFlag_Object = MibTableColumn
driveMirrorFlag = _DriveMirrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 15),
    _DriveMirrorFlag_Type()
)
driveMirrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveMirrorFlag.setStatus("mandatory")


class _DriveMirrorStatus_Type(DisplayString):
    """Custom type driveMirrorStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_DriveMirrorStatus_Type.__name__ = "DisplayString"
_DriveMirrorStatus_Object = MibTableColumn
driveMirrorStatus = _DriveMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 16),
    _DriveMirrorStatus_Type()
)
driveMirrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveMirrorStatus.setStatus("mandatory")
_DriveRemirrorPercentage_Type = Integer32
_DriveRemirrorPercentage_Object = MibTableColumn
driveRemirrorPercentage = _DriveRemirrorPercentage_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 17),
    _DriveRemirrorPercentage_Type()
)
driveRemirrorPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveRemirrorPercentage.setStatus("mandatory")
_DriveRedirectionSize_Type = Integer32
_DriveRedirectionSize_Object = MibTableColumn
driveRedirectionSize = _DriveRedirectionSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 18),
    _DriveRedirectionSize_Type()
)
driveRedirectionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveRedirectionSize.setStatus("mandatory")
_DriveRedirectedSize_Type = Integer32
_DriveRedirectedSize_Object = MibTableColumn
driveRedirectedSize = _DriveRedirectedSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 19),
    _DriveRedirectedSize_Type()
)
driveRedirectedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveRedirectedSize.setStatus("mandatory")
_DriveRedirectionReservedSize_Type = Integer32
_DriveRedirectionReservedSize_Object = MibTableColumn
driveRedirectionReservedSize = _DriveRedirectionReservedSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 12, 2, 1, 20),
    _DriveRedirectionReservedSize_Type()
)
driveRedirectionReservedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveRedirectionReservedSize.setStatus("mandatory")
_Drivetrends_ObjectIdentity = ObjectIdentity
drivetrends = _Drivetrends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13)
)
_DriveTrendsTable_Object = MibTable
driveTrendsTable = _DriveTrendsTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1)
)
if mibBuilder.loadTexts:
    driveTrendsTable.setStatus("mandatory")
_DriveTrendEntry_Object = MibTableRow
driveTrendEntry = _DriveTrendEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1)
)
driveTrendEntry.setIndexNames(
    (0, "NConsole-MIB", "driveTrendCycleIndex"),
    (0, "NConsole-MIB", "driveTrendDriveIndex"),
)
if mibBuilder.loadTexts:
    driveTrendEntry.setStatus("mandatory")
_DriveTrendCycleIndex_Type = Integer32
_DriveTrendCycleIndex_Object = MibTableColumn
driveTrendCycleIndex = _DriveTrendCycleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1, 1),
    _DriveTrendCycleIndex_Type()
)
driveTrendCycleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTrendCycleIndex.setStatus("mandatory")
_DriveTrendDriveIndex_Type = Integer32
_DriveTrendDriveIndex_Object = MibTableColumn
driveTrendDriveIndex = _DriveTrendDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1, 2),
    _DriveTrendDriveIndex_Type()
)
driveTrendDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTrendDriveIndex.setStatus("mandatory")


class _DriveTrendStartTime_Type(DisplayString):
    """Custom type driveTrendStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DriveTrendStartTime_Type.__name__ = "DisplayString"
_DriveTrendStartTime_Object = MibTableColumn
driveTrendStartTime = _DriveTrendStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1, 3),
    _DriveTrendStartTime_Type()
)
driveTrendStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTrendStartTime.setStatus("mandatory")
_DriveTrendStartUTC_Type = Integer32
_DriveTrendStartUTC_Object = MibTableColumn
driveTrendStartUTC = _DriveTrendStartUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1, 4),
    _DriveTrendStartUTC_Type()
)
driveTrendStartUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTrendStartUTC.setStatus("mandatory")


class _DriveTrendStopTime_Type(DisplayString):
    """Custom type driveTrendStopTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DriveTrendStopTime_Type.__name__ = "DisplayString"
_DriveTrendStopTime_Object = MibTableColumn
driveTrendStopTime = _DriveTrendStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1, 5),
    _DriveTrendStopTime_Type()
)
driveTrendStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTrendStopTime.setStatus("mandatory")
_DriveTrendStopUTC_Type = Integer32
_DriveTrendStopUTC_Object = MibTableColumn
driveTrendStopUTC = _DriveTrendStopUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1, 6),
    _DriveTrendStopUTC_Type()
)
driveTrendStopUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTrendStopUTC.setStatus("mandatory")


class _DriveTrendDesc_Type(DisplayString):
    """Custom type driveTrendDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DriveTrendDesc_Type.__name__ = "DisplayString"
_DriveTrendDesc_Object = MibTableColumn
driveTrendDesc = _DriveTrendDesc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1, 7),
    _DriveTrendDesc_Type()
)
driveTrendDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTrendDesc.setStatus("mandatory")
_DriveTrendSize_Type = Integer32
_DriveTrendSize_Object = MibTableColumn
driveTrendSize = _DriveTrendSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1, 8),
    _DriveTrendSize_Type()
)
driveTrendSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTrendSize.setStatus("mandatory")
_DriveTrendRedirectionSize_Type = Integer32
_DriveTrendRedirectionSize_Object = MibTableColumn
driveTrendRedirectionSize = _DriveTrendRedirectionSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1, 9),
    _DriveTrendRedirectionSize_Type()
)
driveTrendRedirectionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTrendRedirectionSize.setStatus("mandatory")
_DriveTrendRedirectedSize_Type = Integer32
_DriveTrendRedirectedSize_Object = MibTableColumn
driveTrendRedirectedSize = _DriveTrendRedirectedSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1, 10),
    _DriveTrendRedirectedSize_Type()
)
driveTrendRedirectedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTrendRedirectedSize.setStatus("mandatory")
_DriveTrendRedirectionReservedSize_Type = Integer32
_DriveTrendRedirectionReservedSize_Object = MibTableColumn
driveTrendRedirectionReservedSize = _DriveTrendRedirectionReservedSize_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 13, 1, 1, 11),
    _DriveTrendRedirectionReservedSize_Type()
)
driveTrendRedirectionReservedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTrendRedirectionReservedSize.setStatus("mandatory")
_Nictrends_ObjectIdentity = ObjectIdentity
nictrends = _Nictrends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14)
)
_NicTrendsTable_Object = MibTable
nicTrendsTable = _NicTrendsTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1)
)
if mibBuilder.loadTexts:
    nicTrendsTable.setStatus("mandatory")
_NicTrendEntry_Object = MibTableRow
nicTrendEntry = _NicTrendEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1)
)
nicTrendEntry.setIndexNames(
    (0, "NConsole-MIB", "nicTrendCycleIndex"),
    (0, "NConsole-MIB", "nicTrendNICIndex"),
)
if mibBuilder.loadTexts:
    nicTrendEntry.setStatus("mandatory")
_NicTrendCycleIndex_Type = Integer32
_NicTrendCycleIndex_Object = MibTableColumn
nicTrendCycleIndex = _NicTrendCycleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 1),
    _NicTrendCycleIndex_Type()
)
nicTrendCycleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendCycleIndex.setStatus("mandatory")
_NicTrendNICIndex_Type = Integer32
_NicTrendNICIndex_Object = MibTableColumn
nicTrendNICIndex = _NicTrendNICIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 2),
    _NicTrendNICIndex_Type()
)
nicTrendNICIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendNICIndex.setStatus("mandatory")


class _NicTrendStartTime_Type(DisplayString):
    """Custom type nicTrendStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NicTrendStartTime_Type.__name__ = "DisplayString"
_NicTrendStartTime_Object = MibTableColumn
nicTrendStartTime = _NicTrendStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 3),
    _NicTrendStartTime_Type()
)
nicTrendStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendStartTime.setStatus("mandatory")
_NicTrendStartUTC_Type = Integer32
_NicTrendStartUTC_Object = MibTableColumn
nicTrendStartUTC = _NicTrendStartUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 4),
    _NicTrendStartUTC_Type()
)
nicTrendStartUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendStartUTC.setStatus("mandatory")


class _NicTrendStopTime_Type(DisplayString):
    """Custom type nicTrendStopTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NicTrendStopTime_Type.__name__ = "DisplayString"
_NicTrendStopTime_Object = MibTableColumn
nicTrendStopTime = _NicTrendStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 5),
    _NicTrendStopTime_Type()
)
nicTrendStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendStopTime.setStatus("mandatory")
_NicTrendStopUTC_Type = Integer32
_NicTrendStopUTC_Object = MibTableColumn
nicTrendStopUTC = _NicTrendStopUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 6),
    _NicTrendStopUTC_Type()
)
nicTrendStopUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendStopUTC.setStatus("mandatory")


class _NicTrendNodeID_Type(OctetString):
    """Custom type nicTrendNodeID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NicTrendNodeID_Type.__name__ = "OctetString"
_NicTrendNodeID_Object = MibTableColumn
nicTrendNodeID = _NicTrendNodeID_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 7),
    _NicTrendNodeID_Type()
)
nicTrendNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendNodeID.setStatus("mandatory")
_NicTrendAvgRxPacketCount_Type = Integer32
_NicTrendAvgRxPacketCount_Object = MibTableColumn
nicTrendAvgRxPacketCount = _NicTrendAvgRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 8),
    _NicTrendAvgRxPacketCount_Type()
)
nicTrendAvgRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendAvgRxPacketCount.setStatus("mandatory")
_NicTrendPeakRxPacketCount_Type = Integer32
_NicTrendPeakRxPacketCount_Object = MibTableColumn
nicTrendPeakRxPacketCount = _NicTrendPeakRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 9),
    _NicTrendPeakRxPacketCount_Type()
)
nicTrendPeakRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendPeakRxPacketCount.setStatus("mandatory")
_NicTrendCumlRxPacketCount_Type = Integer32
_NicTrendCumlRxPacketCount_Object = MibTableColumn
nicTrendCumlRxPacketCount = _NicTrendCumlRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 10),
    _NicTrendCumlRxPacketCount_Type()
)
nicTrendCumlRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendCumlRxPacketCount.setStatus("mandatory")
_NicTrendAvgTxPacketCount_Type = Integer32
_NicTrendAvgTxPacketCount_Object = MibTableColumn
nicTrendAvgTxPacketCount = _NicTrendAvgTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 11),
    _NicTrendAvgTxPacketCount_Type()
)
nicTrendAvgTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendAvgTxPacketCount.setStatus("mandatory")
_NicTrendPeakTxPacketCount_Type = Integer32
_NicTrendPeakTxPacketCount_Object = MibTableColumn
nicTrendPeakTxPacketCount = _NicTrendPeakTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 12),
    _NicTrendPeakTxPacketCount_Type()
)
nicTrendPeakTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendPeakTxPacketCount.setStatus("mandatory")
_NicTrendCumlTxPacketCount_Type = Integer32
_NicTrendCumlTxPacketCount_Object = MibTableColumn
nicTrendCumlTxPacketCount = _NicTrendCumlTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 14, 1, 1, 13),
    _NicTrendCumlTxPacketCount_Type()
)
nicTrendCumlTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicTrendCumlTxPacketCount.setStatus("mandatory")
_Protocolinfo_ObjectIdentity = ObjectIdentity
protocolinfo = _Protocolinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15)
)
_ProtocolCount_Type = Integer32
_ProtocolCount_Object = MibScalar
protocolCount = _ProtocolCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 1),
    _ProtocolCount_Type()
)
protocolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolCount.setStatus("mandatory")
_ProtocolTable_Object = MibTable
protocolTable = _ProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2)
)
if mibBuilder.loadTexts:
    protocolTable.setStatus("mandatory")
_ProtocolEntry_Object = MibTableRow
protocolEntry = _ProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2, 1)
)
protocolEntry.setIndexNames(
    (0, "NConsole-MIB", "protocolIndex"),
)
if mibBuilder.loadTexts:
    protocolEntry.setStatus("mandatory")
_ProtocolIndex_Type = Integer32
_ProtocolIndex_Object = MibTableColumn
protocolIndex = _ProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2, 1, 1),
    _ProtocolIndex_Type()
)
protocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolIndex.setStatus("mandatory")


class _ProtocolDesc_Type(DisplayString):
    """Custom type protocolDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProtocolDesc_Type.__name__ = "DisplayString"
_ProtocolDesc_Object = MibTableColumn
protocolDesc = _ProtocolDesc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2, 1, 2),
    _ProtocolDesc_Type()
)
protocolDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolDesc.setStatus("mandatory")
_ProtocolCurrRxPacketCount_Type = Integer32
_ProtocolCurrRxPacketCount_Object = MibTableColumn
protocolCurrRxPacketCount = _ProtocolCurrRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2, 1, 3),
    _ProtocolCurrRxPacketCount_Type()
)
protocolCurrRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolCurrRxPacketCount.setStatus("mandatory")
_ProtocolAvgRxPacketCount_Type = Integer32
_ProtocolAvgRxPacketCount_Object = MibTableColumn
protocolAvgRxPacketCount = _ProtocolAvgRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2, 1, 4),
    _ProtocolAvgRxPacketCount_Type()
)
protocolAvgRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolAvgRxPacketCount.setStatus("mandatory")
_ProtocolPeakRxPacketCount_Type = Integer32
_ProtocolPeakRxPacketCount_Object = MibTableColumn
protocolPeakRxPacketCount = _ProtocolPeakRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2, 1, 5),
    _ProtocolPeakRxPacketCount_Type()
)
protocolPeakRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolPeakRxPacketCount.setStatus("mandatory")
_ProtocolCumlRxPacketCount_Type = Integer32
_ProtocolCumlRxPacketCount_Object = MibTableColumn
protocolCumlRxPacketCount = _ProtocolCumlRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2, 1, 6),
    _ProtocolCumlRxPacketCount_Type()
)
protocolCumlRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolCumlRxPacketCount.setStatus("mandatory")
_ProtocolCurrTxPacketCount_Type = Integer32
_ProtocolCurrTxPacketCount_Object = MibTableColumn
protocolCurrTxPacketCount = _ProtocolCurrTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2, 1, 7),
    _ProtocolCurrTxPacketCount_Type()
)
protocolCurrTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolCurrTxPacketCount.setStatus("mandatory")
_ProtocolAvgTxPacketCount_Type = Integer32
_ProtocolAvgTxPacketCount_Object = MibTableColumn
protocolAvgTxPacketCount = _ProtocolAvgTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2, 1, 8),
    _ProtocolAvgTxPacketCount_Type()
)
protocolAvgTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolAvgTxPacketCount.setStatus("mandatory")
_ProtocolPeakTxPacketCount_Type = Integer32
_ProtocolPeakTxPacketCount_Object = MibTableColumn
protocolPeakTxPacketCount = _ProtocolPeakTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2, 1, 9),
    _ProtocolPeakTxPacketCount_Type()
)
protocolPeakTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolPeakTxPacketCount.setStatus("mandatory")
_ProtocolCumlTxPacketCount_Type = Integer32
_ProtocolCumlTxPacketCount_Object = MibTableColumn
protocolCumlTxPacketCount = _ProtocolCumlTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 15, 2, 1, 10),
    _ProtocolCumlTxPacketCount_Type()
)
protocolCumlTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolCumlTxPacketCount.setStatus("mandatory")
_Protocoltrends_ObjectIdentity = ObjectIdentity
protocoltrends = _Protocoltrends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16)
)
_ProtocolTrendsTable_Object = MibTable
protocolTrendsTable = _ProtocolTrendsTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1)
)
if mibBuilder.loadTexts:
    protocolTrendsTable.setStatus("mandatory")
_ProtocolTrendEntry_Object = MibTableRow
protocolTrendEntry = _ProtocolTrendEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1)
)
protocolTrendEntry.setIndexNames(
    (0, "NConsole-MIB", "protocolTrendCycleIndex"),
    (0, "NConsole-MIB", "protocolTrendProtocolIndex"),
)
if mibBuilder.loadTexts:
    protocolTrendEntry.setStatus("mandatory")
_ProtocolTrendCycleIndex_Type = Integer32
_ProtocolTrendCycleIndex_Object = MibTableColumn
protocolTrendCycleIndex = _ProtocolTrendCycleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 1),
    _ProtocolTrendCycleIndex_Type()
)
protocolTrendCycleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendCycleIndex.setStatus("mandatory")
_ProtocolTrendProtocolIndex_Type = Integer32
_ProtocolTrendProtocolIndex_Object = MibTableColumn
protocolTrendProtocolIndex = _ProtocolTrendProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 2),
    _ProtocolTrendProtocolIndex_Type()
)
protocolTrendProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendProtocolIndex.setStatus("mandatory")


class _ProtocolTrendStartTime_Type(DisplayString):
    """Custom type protocolTrendStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProtocolTrendStartTime_Type.__name__ = "DisplayString"
_ProtocolTrendStartTime_Object = MibTableColumn
protocolTrendStartTime = _ProtocolTrendStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 3),
    _ProtocolTrendStartTime_Type()
)
protocolTrendStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendStartTime.setStatus("mandatory")
_ProtocolTrendStartUTC_Type = Integer32
_ProtocolTrendStartUTC_Object = MibTableColumn
protocolTrendStartUTC = _ProtocolTrendStartUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 4),
    _ProtocolTrendStartUTC_Type()
)
protocolTrendStartUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendStartUTC.setStatus("mandatory")


class _ProtocolTrendStopTime_Type(DisplayString):
    """Custom type protocolTrendStopTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProtocolTrendStopTime_Type.__name__ = "DisplayString"
_ProtocolTrendStopTime_Object = MibTableColumn
protocolTrendStopTime = _ProtocolTrendStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 5),
    _ProtocolTrendStopTime_Type()
)
protocolTrendStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendStopTime.setStatus("mandatory")
_ProtocolTrendStopUTC_Type = Integer32
_ProtocolTrendStopUTC_Object = MibTableColumn
protocolTrendStopUTC = _ProtocolTrendStopUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 6),
    _ProtocolTrendStopUTC_Type()
)
protocolTrendStopUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendStopUTC.setStatus("mandatory")


class _ProtocolTrendDesc_Type(DisplayString):
    """Custom type protocolTrendDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProtocolTrendDesc_Type.__name__ = "DisplayString"
_ProtocolTrendDesc_Object = MibTableColumn
protocolTrendDesc = _ProtocolTrendDesc_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 7),
    _ProtocolTrendDesc_Type()
)
protocolTrendDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendDesc.setStatus("mandatory")
_ProtocolTrendAvgRxPacketCount_Type = Integer32
_ProtocolTrendAvgRxPacketCount_Object = MibTableColumn
protocolTrendAvgRxPacketCount = _ProtocolTrendAvgRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 8),
    _ProtocolTrendAvgRxPacketCount_Type()
)
protocolTrendAvgRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendAvgRxPacketCount.setStatus("mandatory")
_ProtocolTrendPeakRxPacketCount_Type = Integer32
_ProtocolTrendPeakRxPacketCount_Object = MibTableColumn
protocolTrendPeakRxPacketCount = _ProtocolTrendPeakRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 9),
    _ProtocolTrendPeakRxPacketCount_Type()
)
protocolTrendPeakRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendPeakRxPacketCount.setStatus("mandatory")
_ProtocolTrendCumlRxPacketCount_Type = Integer32
_ProtocolTrendCumlRxPacketCount_Object = MibTableColumn
protocolTrendCumlRxPacketCount = _ProtocolTrendCumlRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 10),
    _ProtocolTrendCumlRxPacketCount_Type()
)
protocolTrendCumlRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendCumlRxPacketCount.setStatus("mandatory")
_ProtocolTrendAvgTxPacketCount_Type = Integer32
_ProtocolTrendAvgTxPacketCount_Object = MibTableColumn
protocolTrendAvgTxPacketCount = _ProtocolTrendAvgTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 11),
    _ProtocolTrendAvgTxPacketCount_Type()
)
protocolTrendAvgTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendAvgTxPacketCount.setStatus("mandatory")
_ProtocolTrendPeakTxPacketCount_Type = Integer32
_ProtocolTrendPeakTxPacketCount_Object = MibTableColumn
protocolTrendPeakTxPacketCount = _ProtocolTrendPeakTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 12),
    _ProtocolTrendPeakTxPacketCount_Type()
)
protocolTrendPeakTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendPeakTxPacketCount.setStatus("mandatory")
_ProtocolTrendCumlTxPacketCount_Type = Integer32
_ProtocolTrendCumlTxPacketCount_Object = MibTableColumn
protocolTrendCumlTxPacketCount = _ProtocolTrendCumlTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 16, 1, 1, 13),
    _ProtocolTrendCumlTxPacketCount_Type()
)
protocolTrendCumlTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolTrendCumlTxPacketCount.setStatus("mandatory")
_Sftserverinfo_ObjectIdentity = ObjectIdentity
sftserverinfo = _Sftserverinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 17)
)
_Sftmemoryinfo_ObjectIdentity = ObjectIdentity
sftmemoryinfo = _Sftmemoryinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 18)
)
_Sftmoduleinfo_ObjectIdentity = ObjectIdentity
sftmoduleinfo = _Sftmoduleinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 19)
)
_Sftnetinfo_ObjectIdentity = ObjectIdentity
sftnetinfo = _Sftnetinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 20)
)
_Sftsetparminfo_ObjectIdentity = ObjectIdentity
sftsetparminfo = _Sftsetparminfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 21)
)
_Sftservertrends_ObjectIdentity = ObjectIdentity
sftservertrends = _Sftservertrends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 22)
)
_Smpinfo_ObjectIdentity = ObjectIdentity
smpinfo = _Smpinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 23)
)
_SmpCount_Type = Integer32
_SmpCount_Object = MibScalar
smpCount = _SmpCount_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 23, 1),
    _SmpCount_Type()
)
smpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpCount.setStatus("mandatory")
_SmpTable_Object = MibTable
smpTable = _SmpTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 23, 2)
)
if mibBuilder.loadTexts:
    smpTable.setStatus("mandatory")
_SmpEntry_Object = MibTableRow
smpEntry = _SmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 23, 2, 1)
)
smpEntry.setIndexNames(
    (0, "NConsole-MIB", "smpIndex"),
)
if mibBuilder.loadTexts:
    smpEntry.setStatus("mandatory")
_SmpIndex_Type = Integer32
_SmpIndex_Object = MibTableColumn
smpIndex = _SmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 23, 2, 1, 1),
    _SmpIndex_Type()
)
smpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpIndex.setStatus("mandatory")
_SmpCurrUtil_Type = Integer32
_SmpCurrUtil_Object = MibTableColumn
smpCurrUtil = _SmpCurrUtil_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 23, 2, 1, 2),
    _SmpCurrUtil_Type()
)
smpCurrUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpCurrUtil.setStatus("mandatory")
_SmpAvgUtil_Type = Integer32
_SmpAvgUtil_Object = MibTableColumn
smpAvgUtil = _SmpAvgUtil_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 23, 2, 1, 3),
    _SmpAvgUtil_Type()
)
smpAvgUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpAvgUtil.setStatus("mandatory")
_SmpPeakUtil_Type = Integer32
_SmpPeakUtil_Object = MibTableColumn
smpPeakUtil = _SmpPeakUtil_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 23, 2, 1, 4),
    _SmpPeakUtil_Type()
)
smpPeakUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpPeakUtil.setStatus("mandatory")
_Smptrends_ObjectIdentity = ObjectIdentity
smptrends = _Smptrends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1117, 1, 24)
)
_SmpTrendTable_Object = MibTable
smpTrendTable = _SmpTrendTable_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 24, 1)
)
if mibBuilder.loadTexts:
    smpTrendTable.setStatus("mandatory")
_SmpTrendEntry_Object = MibTableRow
smpTrendEntry = _SmpTrendEntry_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 24, 1, 1)
)
smpTrendEntry.setIndexNames(
    (0, "NConsole-MIB", "smpTrendCycleIndex"),
    (0, "NConsole-MIB", "smpTrendProcessorIndex"),
)
if mibBuilder.loadTexts:
    smpTrendEntry.setStatus("mandatory")
_SmpTrendCycleIndex_Type = Integer32
_SmpTrendCycleIndex_Object = MibTableColumn
smpTrendCycleIndex = _SmpTrendCycleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 24, 1, 1, 1),
    _SmpTrendCycleIndex_Type()
)
smpTrendCycleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpTrendCycleIndex.setStatus("mandatory")
_SmpTrendProcessorIndex_Type = Integer32
_SmpTrendProcessorIndex_Object = MibTableColumn
smpTrendProcessorIndex = _SmpTrendProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 24, 1, 1, 2),
    _SmpTrendProcessorIndex_Type()
)
smpTrendProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpTrendProcessorIndex.setStatus("mandatory")


class _SmpTrendStartTime_Type(DisplayString):
    """Custom type smpTrendStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmpTrendStartTime_Type.__name__ = "DisplayString"
_SmpTrendStartTime_Object = MibTableColumn
smpTrendStartTime = _SmpTrendStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 24, 1, 1, 3),
    _SmpTrendStartTime_Type()
)
smpTrendStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpTrendStartTime.setStatus("mandatory")
_SmpTrendStartUTC_Type = Integer32
_SmpTrendStartUTC_Object = MibTableColumn
smpTrendStartUTC = _SmpTrendStartUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 24, 1, 1, 4),
    _SmpTrendStartUTC_Type()
)
smpTrendStartUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpTrendStartUTC.setStatus("mandatory")


class _SmpTrendStopTime_Type(DisplayString):
    """Custom type smpTrendStopTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmpTrendStopTime_Type.__name__ = "DisplayString"
_SmpTrendStopTime_Object = MibTableColumn
smpTrendStopTime = _SmpTrendStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 24, 1, 1, 5),
    _SmpTrendStopTime_Type()
)
smpTrendStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpTrendStopTime.setStatus("mandatory")
_SmpTrendStopUTC_Type = Integer32
_SmpTrendStopUTC_Object = MibTableColumn
smpTrendStopUTC = _SmpTrendStopUTC_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 24, 1, 1, 6),
    _SmpTrendStopUTC_Type()
)
smpTrendStopUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpTrendStopUTC.setStatus("mandatory")
_SmpTrendAvgUtil_Type = Integer32
_SmpTrendAvgUtil_Object = MibTableColumn
smpTrendAvgUtil = _SmpTrendAvgUtil_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 24, 1, 1, 7),
    _SmpTrendAvgUtil_Type()
)
smpTrendAvgUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpTrendAvgUtil.setStatus("mandatory")
_SmpTrendPeakUtil_Type = Integer32
_SmpTrendPeakUtil_Object = MibTableColumn
smpTrendPeakUtil = _SmpTrendPeakUtil_Object(
    (1, 3, 6, 1, 4, 1, 1117, 1, 24, 1, 1, 8),
    _SmpTrendPeakUtil_Type()
)
smpTrendPeakUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smpTrendPeakUtil.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NConsole-MIB",
    **{"avanti": avanti,
       "nconsolemib": nconsolemib,
       "serverinfo": serverinfo,
       "serverName": serverName,
       "serverNwRevInfo": serverNwRevInfo,
       "serverNwSerialNumber": serverNwSerialNumber,
       "serverTimeLocal": serverTimeLocal,
       "serverTimeUTC": serverTimeUTC,
       "serverUpTime": serverUpTime,
       "serverCpuUtil": serverCpuUtil,
       "serverCpuCount": serverCpuCount,
       "serverCpuSpeed": serverCpuSpeed,
       "serverCacheHits": serverCacheHits,
       "serverCacheLRU": serverCacheLRU,
       "serverCacheRatio": serverCacheRatio,
       "serverLicenses": serverLicenses,
       "serverConns": serverConns,
       "serverUsers": serverUsers,
       "serverAllowUnencryptedPwds": serverAllowUnencryptedPwds,
       "serverDOSPresent": serverDOSPresent,
       "serverLoginStatus": serverLoginStatus,
       "serverRemoteStatus": serverRemoteStatus,
       "serverSecurityRestrictionLevel": serverSecurityRestrictionLevel,
       "serverNumOfActiveDrives": serverNumOfActiveDrives,
       "serverNumOfMountedVols": serverNumOfMountedVols,
       "serverStartupFilePath": serverStartupFilePath,
       "serverAutoexecFilePath": serverAutoexecFilePath,
       "configinfo": configinfo,
       "configVersion": configVersion,
       "configCycleLength": configCycleLength,
       "configStartTime": configStartTime,
       "configStopTime": configStopTime,
       "configKeyboardStatus": configKeyboardStatus,
       "configKeyboardAutoLock": configKeyboardAutoLock,
       "configScreenSaverTimeout": configScreenSaverTimeout,
       "configArchiveStatus": configArchiveStatus,
       "configArchiveMaxDays": configArchiveMaxDays,
       "configDataFileName": configDataFileName,
       "configDataFileFormat": configDataFileFormat,
       "configLogFileName": configLogFileName,
       "configTrendFileName": configTrendFileName,
       "configTrendMaxDays": configTrendMaxDays,
       "memoryinfo": memoryinfo,
       "memoryTotalRAM": memoryTotalRAM,
       "memoryServerWorkRAM": memoryServerWorkRAM,
       "memoryDOS": memoryDOS,
       "memoryBaseRAM": memoryBaseRAM,
       "memoryAllocPoolTotal": memoryAllocPoolTotal,
       "memoryAllocPoolInUse": memoryAllocPoolInUse,
       "memoryCacheBufferPool": memoryCacheBufferPool,
       "memoryCacheMovablePool": memoryCacheMovablePool,
       "memoryCacheNonMovablePool": memoryCacheNonMovablePool,
       "memoryNw3PermMemoryPoolTotal": memoryNw3PermMemoryPoolTotal,
       "memoryNw3PermMemoryPoolInUse": memoryNw3PermMemoryPoolInUse,
       "memoryNw4CodeDataPool": memoryNw4CodeDataPool,
       "moduleinfo": moduleinfo,
       "moduleCount": moduleCount,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleIndex": moduleIndex,
       "moduleName": moduleName,
       "moduleDesc": moduleDesc,
       "moduleCopyright": moduleCopyright,
       "moduleVersion": moduleVersion,
       "moduleCompileDate": moduleCompileDate,
       "moduleCodeSize": moduleCodeSize,
       "moduleDataSize": moduleDataSize,
       "moduleSmallMemoryAlloc": moduleSmallMemoryAlloc,
       "moduleMediumMemoryAlloc": moduleMediumMemoryAlloc,
       "moduleLargeMemoryAlloc": moduleLargeMemoryAlloc,
       "moduleActiveProcesses": moduleActiveProcesses,
       "moduleActiveScreens": moduleActiveScreens,
       "netinfo": netinfo,
       "netCount": netCount,
       "netTable": netTable,
       "netEntry": netEntry,
       "netIndex": netIndex,
       "netDriverName": netDriverName,
       "netDriverDesc": netDriverDesc,
       "netFrameDesc": netFrameDesc,
       "netLogicalName": netLogicalName,
       "netProtocolDesc": netProtocolDesc,
       "netNodeID": netNodeID,
       "netLineSpeed": netLineSpeed,
       "netMaxPacketSize": netMaxPacketSize,
       "netMaxRecvSize": netMaxRecvSize,
       "netMaxProtocolSize": netMaxProtocolSize,
       "netPrimaryIOPort": netPrimaryIOPort,
       "netPrimaryMemoryDecode": netPrimaryMemoryDecode,
       "netPrimaryInterrupt": netPrimaryInterrupt,
       "netPrimaryDMA": netPrimaryDMA,
       "netSecondaryIOPort": netSecondaryIOPort,
       "netSecondaryMemoryDecode": netSecondaryMemoryDecode,
       "netSecondaryInterrupt": netSecondaryInterrupt,
       "netSecondaryDMA": netSecondaryDMA,
       "netTotalRxPacketCount": netTotalRxPacketCount,
       "netPacketRxOverflowCount": netPacketRxOverflowCount,
       "netPacketRxTooBigCount": netPacketRxTooBigCount,
       "netPacketRxTooSmallCount": netPacketRxTooSmallCount,
       "netPacketRxMiscErrorCount": netPacketRxMiscErrorCount,
       "netChecksumErrorCount": netChecksumErrorCount,
       "netHardwareRxMismatchCount": netHardwareRxMismatchCount,
       "netTotalTxPacketCount": netTotalTxPacketCount,
       "netNoECBAvailableCount": netNoECBAvailableCount,
       "netPacketTxTooBigCount": netPacketTxTooBigCount,
       "netPacketTxTooSmallCount": netPacketTxTooSmallCount,
       "netPacketTxMiscErrorCount": netPacketTxMiscErrorCount,
       "netRetryTxCount": netRetryTxCount,
       "nicstats": nicstats,
       "nicCount": nicCount,
       "nicTable": nicTable,
       "nicEntry": nicEntry,
       "nicIndex": nicIndex,
       "nicNodeID": nicNodeID,
       "nicCurrRxPacketCount": nicCurrRxPacketCount,
       "nicAvgRxPacketCount": nicAvgRxPacketCount,
       "nicPeakRxPacketCount": nicPeakRxPacketCount,
       "nicCumlRxPacketCount": nicCumlRxPacketCount,
       "nicCurrTxPacketCount": nicCurrTxPacketCount,
       "nicAvgTxPacketCount": nicAvgTxPacketCount,
       "nicPeakTxPacketCount": nicPeakTxPacketCount,
       "nicCumlTxPacketCount": nicCumlTxPacketCount,
       "setparminfo": setparminfo,
       "setparmTable": setparmTable,
       "setparmEntry": setparmEntry,
       "setparmIndex": setparmIndex,
       "setparmName": setparmName,
       "setparmDesc": setparmDesc,
       "setparmCategory": setparmCategory,
       "setparmFlags": setparmFlags,
       "setparmCurrent": setparmCurrent,
       "setparmMinimum": setparmMinimum,
       "setparmMaximum": setparmMaximum,
       "serverstats": serverstats,
       "serverCycleStartTime": serverCycleStartTime,
       "serverCycleStartUTC": serverCycleStartUTC,
       "serverCycleElapsedTicks": serverCycleElapsedTicks,
       "serverCycleLengthTicks": serverCycleLengthTicks,
       "serverCurrUtil": serverCurrUtil,
       "serverAvgUtil": serverAvgUtil,
       "serverPeakUtil": serverPeakUtil,
       "serverCurrCacheRatio": serverCurrCacheRatio,
       "serverAvgCacheRatio": serverAvgCacheRatio,
       "serverMinCacheRatio": serverMinCacheRatio,
       "serverCurrCacheHits": serverCurrCacheHits,
       "serverAvgCacheHits": serverAvgCacheHits,
       "serverMinCacheHits": serverMinCacheHits,
       "serverCurrFSPs": serverCurrFSPs,
       "serverAvgFSPs": serverAvgFSPs,
       "serverPeakFSPs": serverPeakFSPs,
       "serverCurrProcs": serverCurrProcs,
       "serverAvgProcs": serverAvgProcs,
       "serverPeakProcs": serverPeakProcs,
       "serverCurrConns": serverCurrConns,
       "serverAvgConns": serverAvgConns,
       "serverPeakConns": serverPeakConns,
       "serverCurrUsers": serverCurrUsers,
       "serverAvgUsers": serverAvgUsers,
       "serverPeakUsers": serverPeakUsers,
       "serverCurrRecvBuffs": serverCurrRecvBuffs,
       "serverAvgRecvBuffs": serverAvgRecvBuffs,
       "serverPeakRecvBuffs": serverPeakRecvBuffs,
       "serverCurrDirBuffs": serverCurrDirBuffs,
       "serverAvgDirBuffs": serverAvgDirBuffs,
       "serverPeakDirBuffs": serverPeakDirBuffs,
       "serverCurrOpenFiles": serverCurrOpenFiles,
       "serverAvgOpenFiles": serverAvgOpenFiles,
       "serverPeakOpenFiles": serverPeakOpenFiles,
       "serverCurrIOsPending": serverCurrIOsPending,
       "serverAvgIOsPending": serverAvgIOsPending,
       "serverPeakIOsPending": serverPeakIOsPending,
       "serverCumlIOsPending": serverCumlIOsPending,
       "serverCurrDirtyBlocks": serverCurrDirtyBlocks,
       "serverAvgDirtyBlocks": serverAvgDirtyBlocks,
       "serverPeakDirtyBlocks": serverPeakDirtyBlocks,
       "serverCumlDirtyBlocks": serverCumlDirtyBlocks,
       "serverCurrDiskReads": serverCurrDiskReads,
       "serverAvgDiskReads": serverAvgDiskReads,
       "serverPeakDiskReads": serverPeakDiskReads,
       "serverCumlDiskReads": serverCumlDiskReads,
       "serverCurrDiskReadBytes": serverCurrDiskReadBytes,
       "serverAvgDiskReadBytes": serverAvgDiskReadBytes,
       "serverPeakDiskReadBytes": serverPeakDiskReadBytes,
       "serverCumlDiskReadBytes": serverCumlDiskReadBytes,
       "serverCurrDiskWrites": serverCurrDiskWrites,
       "serverAvgDiskWrites": serverAvgDiskWrites,
       "serverPeakDiskWrites": serverPeakDiskWrites,
       "serverCumlDiskWrites": serverCumlDiskWrites,
       "serverCurrDiskWriteBytes": serverCurrDiskWriteBytes,
       "serverAvgDiskWriteBytes": serverAvgDiskWriteBytes,
       "serverPeakDiskWriteBytes": serverPeakDiskWriteBytes,
       "serverCumlDiskWriteBytes": serverCumlDiskWriteBytes,
       "serverCurrRoutedPkts": serverCurrRoutedPkts,
       "serverAvgRoutedPkts": serverAvgRoutedPkts,
       "serverPeakRoutedPkts": serverPeakRoutedPkts,
       "serverCumlRoutedPkts": serverCumlRoutedPkts,
       "serverCurrRxPkts": serverCurrRxPkts,
       "serverAvgRxPkts": serverAvgRxPkts,
       "serverPeakRxPkts": serverPeakRxPkts,
       "serverCumlRxPkts": serverCumlRxPkts,
       "serverCurrRxBytes": serverCurrRxBytes,
       "serverAvgRxBytes": serverAvgRxBytes,
       "serverPeakRxBytes": serverPeakRxBytes,
       "serverCumlRxBytes": serverCumlRxBytes,
       "serverCurrTxPkts": serverCurrTxPkts,
       "serverAvgTxPkts": serverAvgTxPkts,
       "serverPeakTxPkts": serverPeakTxPkts,
       "serverCumlTxPkts": serverCumlTxPkts,
       "serverCurrTxBytes": serverCurrTxBytes,
       "serverAvgTxBytes": serverAvgTxBytes,
       "serverPeakTxBytes": serverPeakTxBytes,
       "serverCumlTxBytes": serverCumlTxBytes,
       "serverCurrDirSearch": serverCurrDirSearch,
       "serverAvgDirSearch": serverAvgDirSearch,
       "serverPeakDirSearch": serverPeakDirSearch,
       "serverCumlDirSearch": serverCumlDirSearch,
       "serverCurrFileCreates": serverCurrFileCreates,
       "serverAvgFileCreates": serverAvgFileCreates,
       "serverPeakFileCreates": serverPeakFileCreates,
       "serverCumlFileCreates": serverCumlFileCreates,
       "serverCurrFileOpens": serverCurrFileOpens,
       "serverAvgFileOpens": serverAvgFileOpens,
       "serverPeakFileOpens": serverPeakFileOpens,
       "serverCumlFileOpens": serverCumlFileOpens,
       "serverCurrFileDeletes": serverCurrFileDeletes,
       "serverAvgFileDeletes": serverAvgFileDeletes,
       "serverPeakFileDeletes": serverPeakFileDeletes,
       "serverCumlFileDeletes": serverCumlFileDeletes,
       "serverCurrFileReads": serverCurrFileReads,
       "serverAvgFileReads": serverAvgFileReads,
       "serverPeakFileReads": serverPeakFileReads,
       "serverCumlFileReads": serverCumlFileReads,
       "serverCurrFileReadBytes": serverCurrFileReadBytes,
       "serverAvgFileReadBytes": serverAvgFileReadBytes,
       "serverPeakFileReadBytes": serverPeakFileReadBytes,
       "serverCumlFileReadBytes": serverCumlFileReadBytes,
       "serverCurrFileWrites": serverCurrFileWrites,
       "serverAvgFileWrites": serverAvgFileWrites,
       "serverPeakFileWrites": serverPeakFileWrites,
       "serverCumlFileWrites": serverCumlFileWrites,
       "serverCurrFileWriteBytes": serverCurrFileWriteBytes,
       "serverAvgFileWriteBytes": serverAvgFileWriteBytes,
       "serverPeakFileWriteBytes": serverPeakFileWriteBytes,
       "serverCumlFileWriteBytes": serverCumlFileWriteBytes,
       "servertrends": servertrends,
       "serverTrendTable": serverTrendTable,
       "serverTrendEntry": serverTrendEntry,
       "serverTrendIndex": serverTrendIndex,
       "serverTrendStartTime": serverTrendStartTime,
       "serverTrendStartUTC": serverTrendStartUTC,
       "serverTrendStopTime": serverTrendStopTime,
       "serverTrendStopUTC": serverTrendStopUTC,
       "serverTrendUpTime": serverTrendUpTime,
       "serverTrendCacheLRU": serverTrendCacheLRU,
       "serverTrendAvgUtil": serverTrendAvgUtil,
       "serverTrendPeakUtil": serverTrendPeakUtil,
       "serverTrendAvgConns": serverTrendAvgConns,
       "serverTrendPeakConns": serverTrendPeakConns,
       "serverTrendAvgUsers": serverTrendAvgUsers,
       "serverTrendPeakUsers": serverTrendPeakUsers,
       "serverTrendAvgFSPs": serverTrendAvgFSPs,
       "serverTrendPeakFSPs": serverTrendPeakFSPs,
       "serverTrendAvgProcs": serverTrendAvgProcs,
       "serverTrendPeakProcs": serverTrendPeakProcs,
       "serverTrendAvgCacheRatio": serverTrendAvgCacheRatio,
       "serverTrendMinCacheRatio": serverTrendMinCacheRatio,
       "serverTrendAvgCacheHits": serverTrendAvgCacheHits,
       "serverTrendMinCacheHits": serverTrendMinCacheHits,
       "serverTrendAvgDirBuffs": serverTrendAvgDirBuffs,
       "serverTrendPeakDirBuffs": serverTrendPeakDirBuffs,
       "serverTrendAvgRecvBuffs": serverTrendAvgRecvBuffs,
       "serverTrendPeakRecvBuffs": serverTrendPeakRecvBuffs,
       "serverTrendAvgOpenFiles": serverTrendAvgOpenFiles,
       "serverTrendPeakOpenFiles": serverTrendPeakOpenFiles,
       "serverTrendAvgIOsPending": serverTrendAvgIOsPending,
       "serverTrendPeakIOsPending": serverTrendPeakIOsPending,
       "serverTrendCumlIOsPending": serverTrendCumlIOsPending,
       "serverTrendAvgDirtyBlocks": serverTrendAvgDirtyBlocks,
       "serverTrendPeakDirtyBlocks": serverTrendPeakDirtyBlocks,
       "serverTrendCumlDirtyBlocks": serverTrendCumlDirtyBlocks,
       "serverTrendAvgDiskReads": serverTrendAvgDiskReads,
       "serverTrendPeakDiskReads": serverTrendPeakDiskReads,
       "serverTrendCumlDiskReads": serverTrendCumlDiskReads,
       "serverTrendAvgDiskReadBytes": serverTrendAvgDiskReadBytes,
       "serverTrendPeakDiskReadBytes": serverTrendPeakDiskReadBytes,
       "serverTrendCumlDiskReadBytes": serverTrendCumlDiskReadBytes,
       "serverTrendAvgDiskWrites": serverTrendAvgDiskWrites,
       "serverTrendPeakDiskWrites": serverTrendPeakDiskWrites,
       "serverTrendCumlDiskWrites": serverTrendCumlDiskWrites,
       "serverTrendAvgDiskWriteBytes": serverTrendAvgDiskWriteBytes,
       "serverTrendPeakDiskWriteBytes": serverTrendPeakDiskWriteBytes,
       "serverTrendCumlDiskWriteBytes": serverTrendCumlDiskWriteBytes,
       "serverTrendAvgRoutedPkts": serverTrendAvgRoutedPkts,
       "serverTrendPeakRoutedPkts": serverTrendPeakRoutedPkts,
       "serverTrendCumlRoutedPkts": serverTrendCumlRoutedPkts,
       "serverTrendAvgRxPkts": serverTrendAvgRxPkts,
       "serverTrendPeakRxPkts": serverTrendPeakRxPkts,
       "serverTrendCumlRxPkts": serverTrendCumlRxPkts,
       "serverTrendAvgRxBytes": serverTrendAvgRxBytes,
       "serverTrendPeakRxBytes": serverTrendPeakRxBytes,
       "serverTrendCumlRxBytes": serverTrendCumlRxBytes,
       "serverTrendAvgTxPkts": serverTrendAvgTxPkts,
       "serverTrendPeakTxPkts": serverTrendPeakTxPkts,
       "serverTrendCumlTxPkts": serverTrendCumlTxPkts,
       "serverTrendAvgTxBytes": serverTrendAvgTxBytes,
       "serverTrendPeakTxBytes": serverTrendPeakTxBytes,
       "serverTrendCumlTxBytes": serverTrendCumlTxBytes,
       "serverTrendAvgDirSearch": serverTrendAvgDirSearch,
       "serverTrendPeakDirSearch": serverTrendPeakDirSearch,
       "serverTrendCumlDirSearch": serverTrendCumlDirSearch,
       "serverTrendAvgFileCreates": serverTrendAvgFileCreates,
       "serverTrendPeakFileCreates": serverTrendPeakFileCreates,
       "serverTrendCumlFileCreates": serverTrendCumlFileCreates,
       "serverTrendAvgFileOpens": serverTrendAvgFileOpens,
       "serverTrendPeakFileOpens": serverTrendPeakFileOpens,
       "serverTrendCumlFileOpens": serverTrendCumlFileOpens,
       "serverTrendAvgFileDeletes": serverTrendAvgFileDeletes,
       "serverTrendPeakFileDeletes": serverTrendPeakFileDeletes,
       "serverTrendCumlFileDeletes": serverTrendCumlFileDeletes,
       "serverTrendAvgFileReads": serverTrendAvgFileReads,
       "serverTrendPeakFileReads": serverTrendPeakFileReads,
       "serverTrendCumlFileReads": serverTrendCumlFileReads,
       "serverTrendAvgFileReadBytes": serverTrendAvgFileReadBytes,
       "serverTrendPeakFileReadBytes": serverTrendPeakFileReadBytes,
       "serverTrendCumlFileReadBytes": serverTrendCumlFileReadBytes,
       "serverTrendAvgFileWrites": serverTrendAvgFileWrites,
       "serverTrendPeakFileWrites": serverTrendPeakFileWrites,
       "serverTrendCumlFileWrites": serverTrendCumlFileWrites,
       "serverTrendAvgFileWriteBytes": serverTrendAvgFileWriteBytes,
       "serverTrendPeakFileWriteBytes": serverTrendPeakFileWriteBytes,
       "serverTrendCumlFileWriteBytes": serverTrendCumlFileWriteBytes,
       "serverTrendMemoryAllocPoolTotal": serverTrendMemoryAllocPoolTotal,
       "serverTrendMemoryAllocPoolInUse": serverTrendMemoryAllocPoolInUse,
       "serverTrendMemoryCacheBufferPool": serverTrendMemoryCacheBufferPool,
       "serverTrendMemoryCacheMovablePool": serverTrendMemoryCacheMovablePool,
       "serverTrendMemoryCacheNonMovablePool": serverTrendMemoryCacheNonMovablePool,
       "serverTrendMemoryNw3PermMemoryPoolTotal": serverTrendMemoryNw3PermMemoryPoolTotal,
       "serverTrendMemoryNw3PermMemoryPoolInUse": serverTrendMemoryNw3PermMemoryPoolInUse,
       "serverTrendMemoryNw4CodeDataPool": serverTrendMemoryNw4CodeDataPool,
       "volinfo": volinfo,
       "volCount": volCount,
       "volTable": volTable,
       "volEntry": volEntry,
       "volIndex": volIndex,
       "volName": volName,
       "volDriveNumber": volDriveNumber,
       "volBlockSize": volBlockSize,
       "volDirSlots": volDirSlots,
       "volDirSlotsFree": volDirSlotsFree,
       "volDiskSpace": volDiskSpace,
       "volDiskSpaceFree": volDiskSpaceFree,
       "volDiskSpacePurgable": volDiskSpacePurgable,
       "volDiskSpaceNotYetPurgable": volDiskSpaceNotYetPurgable,
       "voltrends": voltrends,
       "volTrendTable": volTrendTable,
       "volTrendEntry": volTrendEntry,
       "volTrendCycleIndex": volTrendCycleIndex,
       "volTrendVolumeIndex": volTrendVolumeIndex,
       "volTrendStartTime": volTrendStartTime,
       "volTrendStartUTC": volTrendStartUTC,
       "volTrendStopTime": volTrendStopTime,
       "volTrendStopUTC": volTrendStopUTC,
       "volTrendName": volTrendName,
       "volTrendDirSlots": volTrendDirSlots,
       "volTrendDirSlotsFree": volTrendDirSlotsFree,
       "volTrendDiskSpace": volTrendDiskSpace,
       "volTrendDiskSpaceFree": volTrendDiskSpaceFree,
       "volTrendDiskSpacePurgable": volTrendDiskSpacePurgable,
       "volTrendDiskSpaceNotYetPurgable": volTrendDiskSpaceNotYetPurgable,
       "driveinfo": driveinfo,
       "driveCount": driveCount,
       "driveTable": driveTable,
       "driveEntry": driveEntry,
       "driveIndex": driveIndex,
       "driveDesc": driveDesc,
       "driveType": driveType,
       "driveControllerCardID": driveControllerCardID,
       "driveControllerDeviceID": driveControllerDeviceID,
       "driveControllerDriveID": driveControllerDriveID,
       "driveCylinderCount": driveCylinderCount,
       "driveHeadCount": driveHeadCount,
       "driveSectorsPerTrack": driveSectorsPerTrack,
       "driveSize": driveSize,
       "driveNumberOfPartitions": driveNumberOfPartitions,
       "driveNetWarePartitionStatus": driveNetWarePartitionStatus,
       "driveNetWarePartitionType": driveNetWarePartitionType,
       "driveNetWarePartitionSize": driveNetWarePartitionSize,
       "driveMirrorFlag": driveMirrorFlag,
       "driveMirrorStatus": driveMirrorStatus,
       "driveRemirrorPercentage": driveRemirrorPercentage,
       "driveRedirectionSize": driveRedirectionSize,
       "driveRedirectedSize": driveRedirectedSize,
       "driveRedirectionReservedSize": driveRedirectionReservedSize,
       "drivetrends": drivetrends,
       "driveTrendsTable": driveTrendsTable,
       "driveTrendEntry": driveTrendEntry,
       "driveTrendCycleIndex": driveTrendCycleIndex,
       "driveTrendDriveIndex": driveTrendDriveIndex,
       "driveTrendStartTime": driveTrendStartTime,
       "driveTrendStartUTC": driveTrendStartUTC,
       "driveTrendStopTime": driveTrendStopTime,
       "driveTrendStopUTC": driveTrendStopUTC,
       "driveTrendDesc": driveTrendDesc,
       "driveTrendSize": driveTrendSize,
       "driveTrendRedirectionSize": driveTrendRedirectionSize,
       "driveTrendRedirectedSize": driveTrendRedirectedSize,
       "driveTrendRedirectionReservedSize": driveTrendRedirectionReservedSize,
       "nictrends": nictrends,
       "nicTrendsTable": nicTrendsTable,
       "nicTrendEntry": nicTrendEntry,
       "nicTrendCycleIndex": nicTrendCycleIndex,
       "nicTrendNICIndex": nicTrendNICIndex,
       "nicTrendStartTime": nicTrendStartTime,
       "nicTrendStartUTC": nicTrendStartUTC,
       "nicTrendStopTime": nicTrendStopTime,
       "nicTrendStopUTC": nicTrendStopUTC,
       "nicTrendNodeID": nicTrendNodeID,
       "nicTrendAvgRxPacketCount": nicTrendAvgRxPacketCount,
       "nicTrendPeakRxPacketCount": nicTrendPeakRxPacketCount,
       "nicTrendCumlRxPacketCount": nicTrendCumlRxPacketCount,
       "nicTrendAvgTxPacketCount": nicTrendAvgTxPacketCount,
       "nicTrendPeakTxPacketCount": nicTrendPeakTxPacketCount,
       "nicTrendCumlTxPacketCount": nicTrendCumlTxPacketCount,
       "protocolinfo": protocolinfo,
       "protocolCount": protocolCount,
       "protocolTable": protocolTable,
       "protocolEntry": protocolEntry,
       "protocolIndex": protocolIndex,
       "protocolDesc": protocolDesc,
       "protocolCurrRxPacketCount": protocolCurrRxPacketCount,
       "protocolAvgRxPacketCount": protocolAvgRxPacketCount,
       "protocolPeakRxPacketCount": protocolPeakRxPacketCount,
       "protocolCumlRxPacketCount": protocolCumlRxPacketCount,
       "protocolCurrTxPacketCount": protocolCurrTxPacketCount,
       "protocolAvgTxPacketCount": protocolAvgTxPacketCount,
       "protocolPeakTxPacketCount": protocolPeakTxPacketCount,
       "protocolCumlTxPacketCount": protocolCumlTxPacketCount,
       "protocoltrends": protocoltrends,
       "protocolTrendsTable": protocolTrendsTable,
       "protocolTrendEntry": protocolTrendEntry,
       "protocolTrendCycleIndex": protocolTrendCycleIndex,
       "protocolTrendProtocolIndex": protocolTrendProtocolIndex,
       "protocolTrendStartTime": protocolTrendStartTime,
       "protocolTrendStartUTC": protocolTrendStartUTC,
       "protocolTrendStopTime": protocolTrendStopTime,
       "protocolTrendStopUTC": protocolTrendStopUTC,
       "protocolTrendDesc": protocolTrendDesc,
       "protocolTrendAvgRxPacketCount": protocolTrendAvgRxPacketCount,
       "protocolTrendPeakRxPacketCount": protocolTrendPeakRxPacketCount,
       "protocolTrendCumlRxPacketCount": protocolTrendCumlRxPacketCount,
       "protocolTrendAvgTxPacketCount": protocolTrendAvgTxPacketCount,
       "protocolTrendPeakTxPacketCount": protocolTrendPeakTxPacketCount,
       "protocolTrendCumlTxPacketCount": protocolTrendCumlTxPacketCount,
       "sftserverinfo": sftserverinfo,
       "sftmemoryinfo": sftmemoryinfo,
       "sftmoduleinfo": sftmoduleinfo,
       "sftnetinfo": sftnetinfo,
       "sftsetparminfo": sftsetparminfo,
       "sftservertrends": sftservertrends,
       "smpinfo": smpinfo,
       "smpCount": smpCount,
       "smpTable": smpTable,
       "smpEntry": smpEntry,
       "smpIndex": smpIndex,
       "smpCurrUtil": smpCurrUtil,
       "smpAvgUtil": smpAvgUtil,
       "smpPeakUtil": smpPeakUtil,
       "smptrends": smptrends,
       "smpTrendTable": smpTrendTable,
       "smpTrendEntry": smpTrendEntry,
       "smpTrendCycleIndex": smpTrendCycleIndex,
       "smpTrendProcessorIndex": smpTrendProcessorIndex,
       "smpTrendStartTime": smpTrendStartTime,
       "smpTrendStartUTC": smpTrendStartUTC,
       "smpTrendStopTime": smpTrendStopTime,
       "smpTrendStopUTC": smpTrendStopUTC,
       "smpTrendAvgUtil": smpTrendAvgUtil,
       "smpTrendPeakUtil": smpTrendPeakUtil}
)

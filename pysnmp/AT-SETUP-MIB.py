# SNMP MIB module (AT-SETUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-SETUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:32 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

setup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500)
)
setup.setRevisions(
        ("2013-10-14 00:00",
         "2012-09-21 00:00",
         "2010-11-20 00:00",
         "2010-10-08 00:00",
         "2010-09-10 00:00",
         "2010-09-08 00:00",
         "2010-06-15 00:15",
         "2010-04-09 00:00",
         "2008-10-02 00:00",
         "2008-09-30 00:00",
         "2008-09-24 00:00",
         "2008-05-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SystemFileOperationType(Integer32, TextualConvention):
    status = "current"
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
        *(("failure", 3),
          ("idle", 1),
          ("saving", 4),
          ("success", 2),
          ("syncing", 5))
    )



# MIB Managed Objects in the order of their OIDs



class _RestartDevice_Type(Integer32):
    """Custom type restartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RestartDevice_Type.__name__ = "Integer32"
_RestartDevice_Object = MibScalar
restartDevice = _RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 1),
    _RestartDevice_Type()
)
restartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartDevice.setStatus("deprecated")
_Firmware_ObjectIdentity = ObjectIdentity
firmware = _Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2)
)
_CurrentFirmware_ObjectIdentity = ObjectIdentity
currentFirmware = _CurrentFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1)
)
_CurrSoftVersion_Type = DisplayString
_CurrSoftVersion_Object = MibScalar
currSoftVersion = _CurrSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 1),
    _CurrSoftVersion_Type()
)
currSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currSoftVersion.setStatus("current")
_CurrSoftName_Type = DisplayString
_CurrSoftName_Object = MibScalar
currSoftName = _CurrSoftName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 2),
    _CurrSoftName_Type()
)
currSoftName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currSoftName.setStatus("current")
_CurrSoftSaveAs_Type = DisplayString
_CurrSoftSaveAs_Object = MibScalar
currSoftSaveAs = _CurrSoftSaveAs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 3),
    _CurrSoftSaveAs_Type()
)
currSoftSaveAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currSoftSaveAs.setStatus("deprecated")
_CurrSoftSaveToFile_Type = DisplayString
_CurrSoftSaveToFile_Object = MibScalar
currSoftSaveToFile = _CurrSoftSaveToFile_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 4),
    _CurrSoftSaveToFile_Type()
)
currSoftSaveToFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currSoftSaveToFile.setStatus("current")
_CurrSoftSaveStatus_Type = SystemFileOperationType
_CurrSoftSaveStatus_Object = MibScalar
currSoftSaveStatus = _CurrSoftSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 5),
    _CurrSoftSaveStatus_Type()
)
currSoftSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currSoftSaveStatus.setStatus("current")
_CurrSoftLastSaveResult_Type = DisplayString
_CurrSoftLastSaveResult_Object = MibScalar
currSoftLastSaveResult = _CurrSoftLastSaveResult_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 6),
    _CurrSoftLastSaveResult_Type()
)
currSoftLastSaveResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currSoftLastSaveResult.setStatus("current")
_NextBootFirmware_ObjectIdentity = ObjectIdentity
nextBootFirmware = _NextBootFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2)
)
_NextBootVersion_Type = DisplayString
_NextBootVersion_Object = MibScalar
nextBootVersion = _NextBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 1),
    _NextBootVersion_Type()
)
nextBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextBootVersion.setStatus("current")
_NextBootPath_Type = DisplayString
_NextBootPath_Object = MibScalar
nextBootPath = _NextBootPath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 2),
    _NextBootPath_Type()
)
nextBootPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextBootPath.setStatus("current")
_NextBootSetStatus_Type = SystemFileOperationType
_NextBootSetStatus_Object = MibScalar
nextBootSetStatus = _NextBootSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 3),
    _NextBootSetStatus_Type()
)
nextBootSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextBootSetStatus.setStatus("current")
_NextBootLastSetResult_Type = DisplayString
_NextBootLastSetResult_Object = MibScalar
nextBootLastSetResult = _NextBootLastSetResult_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 4),
    _NextBootLastSetResult_Type()
)
nextBootLastSetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextBootLastSetResult.setStatus("current")
_BackupFirmware_ObjectIdentity = ObjectIdentity
backupFirmware = _BackupFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3)
)
_BackupVersion_Type = DisplayString
_BackupVersion_Object = MibScalar
backupVersion = _BackupVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 1),
    _BackupVersion_Type()
)
backupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupVersion.setStatus("current")
_BackupPath_Type = DisplayString
_BackupPath_Object = MibScalar
backupPath = _BackupPath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 2),
    _BackupPath_Type()
)
backupPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupPath.setStatus("current")
_BackupSetStatus_Type = SystemFileOperationType
_BackupSetStatus_Object = MibScalar
backupSetStatus = _BackupSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 3),
    _BackupSetStatus_Type()
)
backupSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupSetStatus.setStatus("current")
_BackupLastSetResult_Type = DisplayString
_BackupLastSetResult_Object = MibScalar
backupLastSetResult = _BackupLastSetResult_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 4),
    _BackupLastSetResult_Type()
)
backupLastSetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupLastSetResult.setStatus("current")
_DeviceConfiguration_ObjectIdentity = ObjectIdentity
deviceConfiguration = _DeviceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3)
)
_RunningConfig_ObjectIdentity = ObjectIdentity
runningConfig = _RunningConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1)
)
_RunCnfgSaveAs_Type = DisplayString
_RunCnfgSaveAs_Object = MibScalar
runCnfgSaveAs = _RunCnfgSaveAs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1, 1),
    _RunCnfgSaveAs_Type()
)
runCnfgSaveAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runCnfgSaveAs.setStatus("current")
_RunCnfgSaveAsStatus_Type = SystemFileOperationType
_RunCnfgSaveAsStatus_Object = MibScalar
runCnfgSaveAsStatus = _RunCnfgSaveAsStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1, 2),
    _RunCnfgSaveAsStatus_Type()
)
runCnfgSaveAsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runCnfgSaveAsStatus.setStatus("current")
_RunCnfgLastSaveResult_Type = DisplayString
_RunCnfgLastSaveResult_Object = MibScalar
runCnfgLastSaveResult = _RunCnfgLastSaveResult_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1, 3),
    _RunCnfgLastSaveResult_Type()
)
runCnfgLastSaveResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    runCnfgLastSaveResult.setStatus("current")
_NextBootConfig_ObjectIdentity = ObjectIdentity
nextBootConfig = _NextBootConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2)
)
_BootCnfgPath_Type = DisplayString
_BootCnfgPath_Object = MibScalar
bootCnfgPath = _BootCnfgPath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 1),
    _BootCnfgPath_Type()
)
bootCnfgPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootCnfgPath.setStatus("current")
_BootCnfgExists_Type = TruthValue
_BootCnfgExists_Object = MibScalar
bootCnfgExists = _BootCnfgExists_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 2),
    _BootCnfgExists_Type()
)
bootCnfgExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootCnfgExists.setStatus("current")
_BootCnfgSetStatus_Type = SystemFileOperationType
_BootCnfgSetStatus_Object = MibScalar
bootCnfgSetStatus = _BootCnfgSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 3),
    _BootCnfgSetStatus_Type()
)
bootCnfgSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootCnfgSetStatus.setStatus("current")
_BootCnfgLastSetResult_Type = DisplayString
_BootCnfgLastSetResult_Object = MibScalar
bootCnfgLastSetResult = _BootCnfgLastSetResult_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 4),
    _BootCnfgLastSetResult_Type()
)
bootCnfgLastSetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootCnfgLastSetResult.setStatus("current")
_DefaultConfig_ObjectIdentity = ObjectIdentity
defaultConfig = _DefaultConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3)
)
_DfltCnfgPath_Type = DisplayString
_DfltCnfgPath_Object = MibScalar
dfltCnfgPath = _DfltCnfgPath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3, 1),
    _DfltCnfgPath_Type()
)
dfltCnfgPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfltCnfgPath.setStatus("current")
_DfltCnfgExists_Type = TruthValue
_DfltCnfgExists_Object = MibScalar
dfltCnfgExists = _DfltCnfgExists_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3, 2),
    _DfltCnfgExists_Type()
)
dfltCnfgExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfltCnfgExists.setStatus("current")
_BackupConfig_ObjectIdentity = ObjectIdentity
backupConfig = _BackupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4)
)
_BackupCnfgPath_Type = DisplayString
_BackupCnfgPath_Object = MibScalar
backupCnfgPath = _BackupCnfgPath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 1),
    _BackupCnfgPath_Type()
)
backupCnfgPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupCnfgPath.setStatus("current")
_BackupCnfgExists_Type = TruthValue
_BackupCnfgExists_Object = MibScalar
backupCnfgExists = _BackupCnfgExists_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 2),
    _BackupCnfgExists_Type()
)
backupCnfgExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupCnfgExists.setStatus("current")
_BackupCnfgSetStatus_Type = SystemFileOperationType
_BackupCnfgSetStatus_Object = MibScalar
backupCnfgSetStatus = _BackupCnfgSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 3),
    _BackupCnfgSetStatus_Type()
)
backupCnfgSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupCnfgSetStatus.setStatus("current")
_BackupCnfgLastSetResult_Type = DisplayString
_BackupCnfgLastSetResult_Object = MibScalar
backupCnfgLastSetResult = _BackupCnfgLastSetResult_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 4),
    _BackupCnfgLastSetResult_Type()
)
backupCnfgLastSetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupCnfgLastSetResult.setStatus("current")
_RestartStkMemberDevice_Type = Integer32
_RestartStkMemberDevice_Object = MibScalar
restartStkMemberDevice = _RestartStkMemberDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 4),
    _RestartStkMemberDevice_Type()
)
restartStkMemberDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartStkMemberDevice.setStatus("current")
_ServiceConfig_ObjectIdentity = ObjectIdentity
serviceConfig = _ServiceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5)
)
_SrvcTelnetEnable_Type = TruthValue
_SrvcTelnetEnable_Object = MibScalar
srvcTelnetEnable = _SrvcTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5, 1),
    _SrvcTelnetEnable_Type()
)
srvcTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvcTelnetEnable.setStatus("current")
_SrvcSshEnable_Type = TruthValue
_SrvcSshEnable_Object = MibScalar
srvcSshEnable = _SrvcSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5, 2),
    _SrvcSshEnable_Type()
)
srvcSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvcSshEnable.setStatus("current")
_GuiConfig_ObjectIdentity = ObjectIdentity
guiConfig = _GuiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6)
)
_GuiAppletConfig_ObjectIdentity = ObjectIdentity
guiAppletConfig = _GuiAppletConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1)
)
_GuiAppletSysSwVer_Type = DisplayString
_GuiAppletSysSwVer_Object = MibScalar
guiAppletSysSwVer = _GuiAppletSysSwVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1, 1),
    _GuiAppletSysSwVer_Type()
)
guiAppletSysSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    guiAppletSysSwVer.setStatus("current")
_GuiAppletSwVer_Type = DisplayString
_GuiAppletSwVer_Object = MibScalar
guiAppletSwVer = _GuiAppletSwVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1, 2),
    _GuiAppletSwVer_Type()
)
guiAppletSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    guiAppletSwVer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-SETUP-MIB",
    **{"SystemFileOperationType": SystemFileOperationType,
       "setup": setup,
       "restartDevice": restartDevice,
       "firmware": firmware,
       "currentFirmware": currentFirmware,
       "currSoftVersion": currSoftVersion,
       "currSoftName": currSoftName,
       "currSoftSaveAs": currSoftSaveAs,
       "currSoftSaveToFile": currSoftSaveToFile,
       "currSoftSaveStatus": currSoftSaveStatus,
       "currSoftLastSaveResult": currSoftLastSaveResult,
       "nextBootFirmware": nextBootFirmware,
       "nextBootVersion": nextBootVersion,
       "nextBootPath": nextBootPath,
       "nextBootSetStatus": nextBootSetStatus,
       "nextBootLastSetResult": nextBootLastSetResult,
       "backupFirmware": backupFirmware,
       "backupVersion": backupVersion,
       "backupPath": backupPath,
       "backupSetStatus": backupSetStatus,
       "backupLastSetResult": backupLastSetResult,
       "deviceConfiguration": deviceConfiguration,
       "runningConfig": runningConfig,
       "runCnfgSaveAs": runCnfgSaveAs,
       "runCnfgSaveAsStatus": runCnfgSaveAsStatus,
       "runCnfgLastSaveResult": runCnfgLastSaveResult,
       "nextBootConfig": nextBootConfig,
       "bootCnfgPath": bootCnfgPath,
       "bootCnfgExists": bootCnfgExists,
       "bootCnfgSetStatus": bootCnfgSetStatus,
       "bootCnfgLastSetResult": bootCnfgLastSetResult,
       "defaultConfig": defaultConfig,
       "dfltCnfgPath": dfltCnfgPath,
       "dfltCnfgExists": dfltCnfgExists,
       "backupConfig": backupConfig,
       "backupCnfgPath": backupCnfgPath,
       "backupCnfgExists": backupCnfgExists,
       "backupCnfgSetStatus": backupCnfgSetStatus,
       "backupCnfgLastSetResult": backupCnfgLastSetResult,
       "restartStkMemberDevice": restartStkMemberDevice,
       "serviceConfig": serviceConfig,
       "srvcTelnetEnable": srvcTelnetEnable,
       "srvcSshEnable": srvcSshEnable,
       "guiConfig": guiConfig,
       "guiAppletConfig": guiAppletConfig,
       "guiAppletSysSwVer": guiAppletSysSwVer,
       "guiAppletSwVer": guiAppletSwVer}
)

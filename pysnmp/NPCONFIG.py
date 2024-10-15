# SNMP MIB module (NPCONFIG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NPCONFIG
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:05 2024
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
 enterprises,
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")


# MODULE-IDENTITY

npconfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13)
)
npconfig.setRevisions(
        ("2007-12-20 00:00",
         "2006-10-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NpconfigNotifications_ObjectIdentity = ObjectIdentity
npconfigNotifications = _NpconfigNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 0)
)
_NpconfigRowAction_Type = RowStatus
_NpconfigRowAction_Object = MibScalar
npconfigRowAction = _NpconfigRowAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 1),
    _NpconfigRowAction_Type()
)
npconfigRowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigRowAction.setStatus("current")
_NpconfigHistorySize_Type = Unsigned32
_NpconfigHistorySize_Object = MibScalar
npconfigHistorySize = _NpconfigHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 2),
    _NpconfigHistorySize_Type()
)
npconfigHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigHistorySize.setStatus("current")
_NpconfigCurrHistorySize_Type = Unsigned32
_NpconfigCurrHistorySize_Object = MibScalar
npconfigCurrHistorySize = _NpconfigCurrHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 3),
    _NpconfigCurrHistorySize_Type()
)
npconfigCurrHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigCurrHistorySize.setStatus("current")


class _NpconfigUseRunningAsSaved_Type(Integer32):
    """Custom type npconfigUseRunningAsSaved based on Integer32"""
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


_NpconfigUseRunningAsSaved_Type.__name__ = "Integer32"
_NpconfigUseRunningAsSaved_Object = MibScalar
npconfigUseRunningAsSaved = _NpconfigUseRunningAsSaved_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 4),
    _NpconfigUseRunningAsSaved_Type()
)
npconfigUseRunningAsSaved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigUseRunningAsSaved.setStatus("current")


class _NpconfigRestoreType_Type(Integer32):
    """Custom type npconfigRestoreType based on Integer32"""
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
        *(("http", 4),
          ("scp", 1),
          ("sftp", 2),
          ("tftp", 3))
    )


_NpconfigRestoreType_Type.__name__ = "Integer32"
_NpconfigRestoreType_Object = MibScalar
npconfigRestoreType = _NpconfigRestoreType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 5),
    _NpconfigRestoreType_Type()
)
npconfigRestoreType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigRestoreType.setStatus("current")


class _NpconfigBackupType_Type(Integer32):
    """Custom type npconfigBackupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("scp", 1),
          ("sftp", 2),
          ("tftp", 3))
    )


_NpconfigBackupType_Type.__name__ = "Integer32"
_NpconfigBackupType_Object = MibScalar
npconfigBackupType = _NpconfigBackupType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 6),
    _NpconfigBackupType_Type()
)
npconfigBackupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigBackupType.setStatus("current")


class _NpconfigState_Type(Integer32):
    """Custom type npconfigState based on Integer32"""
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
        *(("init", 1),
          ("resetToDefaults", 2),
          ("restoreBackup", 4),
          ("restoreRemote", 3))
    )


_NpconfigState_Type.__name__ = "Integer32"
_NpconfigState_Object = MibScalar
npconfigState = _NpconfigState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 7),
    _NpconfigState_Type()
)
npconfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigState.setStatus("current")
_NpconfigBackupTableTable_Object = MibTable
npconfigBackupTableTable = _NpconfigBackupTableTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 8)
)
if mibBuilder.loadTexts:
    npconfigBackupTableTable.setStatus("current")
_NpconfigBackupTableEntry_Object = MibTableRow
npconfigBackupTableEntry = _NpconfigBackupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 8, 1)
)
npconfigBackupTableEntry.setIndexNames(
    (0, "NPCONFIG", "npconfigBackupNo"),
)
if mibBuilder.loadTexts:
    npconfigBackupTableEntry.setStatus("current")


class _NpconfigBackupNo_Type(Integer32):
    """Custom type npconfigBackupNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NpconfigBackupNo_Type.__name__ = "Integer32"
_NpconfigBackupNo_Object = MibTableColumn
npconfigBackupNo = _NpconfigBackupNo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 8, 1, 1),
    _NpconfigBackupNo_Type()
)
npconfigBackupNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigBackupNo.setStatus("current")
_NpconfigBackupName_Type = DisplayString
_NpconfigBackupName_Object = MibTableColumn
npconfigBackupName = _NpconfigBackupName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 8, 1, 2),
    _NpconfigBackupName_Type()
)
npconfigBackupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigBackupName.setStatus("current")
_NpconfigBackupDescription_Type = DisplayString
_NpconfigBackupDescription_Object = MibTableColumn
npconfigBackupDescription = _NpconfigBackupDescription_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 8, 1, 3),
    _NpconfigBackupDescription_Type()
)
npconfigBackupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigBackupDescription.setStatus("current")
_NpconfigBackupUrl_Type = DisplayString
_NpconfigBackupUrl_Object = MibTableColumn
npconfigBackupUrl = _NpconfigBackupUrl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 8, 1, 4),
    _NpconfigBackupUrl_Type()
)
npconfigBackupUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigBackupUrl.setStatus("current")
_NpconfigBackupStatus_Type = RowStatus
_NpconfigBackupStatus_Object = MibTableColumn
npconfigBackupStatus = _NpconfigBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 8, 1, 5),
    _NpconfigBackupStatus_Type()
)
npconfigBackupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigBackupStatus.setStatus("current")
_NpconfigBackupDate_Type = DisplayString
_NpconfigBackupDate_Object = MibTableColumn
npconfigBackupDate = _NpconfigBackupDate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 8, 1, 6),
    _NpconfigBackupDate_Type()
)
npconfigBackupDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigBackupDate.setStatus("current")
_NpconfigTftpServer_Type = IpAddress
_NpconfigTftpServer_Object = MibScalar
npconfigTftpServer = _NpconfigTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 9),
    _NpconfigTftpServer_Type()
)
npconfigTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigTftpServer.setStatus("current")
_NpconfigServerIP_Type = IpAddress
_NpconfigServerIP_Object = MibScalar
npconfigServerIP = _NpconfigServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 10),
    _NpconfigServerIP_Type()
)
npconfigServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigServerIP.setStatus("current")
_NpconfigRemoteFile_Type = DisplayString
_NpconfigRemoteFile_Object = MibScalar
npconfigRemoteFile = _NpconfigRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 11),
    _NpconfigRemoteFile_Type()
)
npconfigRemoteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigRemoteFile.setStatus("current")
_NpconfigLocalFile_Type = DisplayString
_NpconfigLocalFile_Object = MibScalar
npconfigLocalFile = _NpconfigLocalFile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 12),
    _NpconfigLocalFile_Type()
)
npconfigLocalFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigLocalFile.setStatus("current")
_Npconfiguser_Type = DisplayString
_Npconfiguser_Object = MibScalar
npconfiguser = _Npconfiguser_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 13),
    _Npconfiguser_Type()
)
npconfiguser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfiguser.setStatus("current")
_Npconfigpassword_Type = DisplayString
_Npconfigpassword_Object = MibScalar
npconfigpassword = _Npconfigpassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 14),
    _Npconfigpassword_Type()
)
npconfigpassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npconfigpassword.setStatus("current")

# Managed Objects groups


# Notification objects

npconfigConfigChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 13, 0, 1)
)
if mibBuilder.loadTexts:
    npconfigConfigChangeEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NPCONFIG",
    **{"npconfig": npconfig,
       "npconfigNotifications": npconfigNotifications,
       "npconfigConfigChangeEvent": npconfigConfigChangeEvent,
       "npconfigRowAction": npconfigRowAction,
       "npconfigHistorySize": npconfigHistorySize,
       "npconfigCurrHistorySize": npconfigCurrHistorySize,
       "npconfigUseRunningAsSaved": npconfigUseRunningAsSaved,
       "npconfigRestoreType": npconfigRestoreType,
       "npconfigBackupType": npconfigBackupType,
       "npconfigState": npconfigState,
       "npconfigBackupTableTable": npconfigBackupTableTable,
       "npconfigBackupTableEntry": npconfigBackupTableEntry,
       "npconfigBackupNo": npconfigBackupNo,
       "npconfigBackupName": npconfigBackupName,
       "npconfigBackupDescription": npconfigBackupDescription,
       "npconfigBackupUrl": npconfigBackupUrl,
       "npconfigBackupStatus": npconfigBackupStatus,
       "npconfigBackupDate": npconfigBackupDate,
       "npconfigTftpServer": npconfigTftpServer,
       "npconfigServerIP": npconfigServerIP,
       "npconfigRemoteFile": npconfigRemoteFile,
       "npconfigLocalFile": npconfigLocalFile,
       "npconfiguser": npconfiguser,
       "npconfigpassword": npconfigpassword}
)

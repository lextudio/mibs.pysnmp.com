# SNMP MIB module (DELL-NETWORKING-COPY-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-COPY-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:50 2024
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dellNetCopyConfigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5)
)
dellNetCopyConfigMib.setRevisions(
        ("2009-05-14 13:00",
         "2007-06-19 12:00",
         "2003-03-01 12:00")
)


# Types definitions



class DellNetConfigFileLocation(Integer32):
    """Custom type DellNetConfigFileLocation based on Integer32"""
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
        *(("flash", 1),
          ("ftp", 4),
          ("nfsmount", 7),
          ("scp", 5),
          ("slot0", 2),
          ("tftp", 3),
          ("usbflash", 6))
    )





class DellNetConfigFileType(Integer32):
    """Custom type DellNetConfigFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dellNetFile", 1),
          ("runningConfig", 2),
          ("startupConfig", 3))
    )





class DellNetConfigCopyState(Integer32):
    """Custom type DellNetConfigCopyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("running", 1),
          ("successful", 2))
    )





class DellNetConfigCopyFailCause(Integer32):
    """Custom type DellNetConfigCopyFailCause based on Integer32"""
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
        *(("badFileName", 1),
          ("copyInProgress", 2),
          ("diskFull", 3),
          ("fileExist", 4),
          ("fileNotFound", 5),
          ("timeout", 6),
          ("unknown", 7))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetCopyConfigObjects_ObjectIdentity = ObjectIdentity
dellNetCopyConfigObjects = _DellNetCopyConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1)
)
_DellNetCopyConfig_ObjectIdentity = ObjectIdentity
dellNetCopyConfig = _DellNetCopyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1)
)
_DellNetCopyTable_Object = MibTable
dellNetCopyTable = _DellNetCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetCopyTable.setStatus("current")
_DellNetCopyEntry_Object = MibTableRow
dellNetCopyEntry = _DellNetCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1)
)
dellNetCopyEntry.setIndexNames(
    (0, "DELL-NETWORKING-COPY-CONFIG-MIB", "copyConfigIndex"),
)
if mibBuilder.loadTexts:
    dellNetCopyEntry.setStatus("current")
_CopyConfigIndex_Type = Integer32
_CopyConfigIndex_Object = MibTableColumn
copyConfigIndex = _CopyConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 1),
    _CopyConfigIndex_Type()
)
copyConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    copyConfigIndex.setStatus("current")
_CopySrcFileType_Type = DellNetConfigFileType
_CopySrcFileType_Object = MibTableColumn
copySrcFileType = _CopySrcFileType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 2),
    _CopySrcFileType_Type()
)
copySrcFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copySrcFileType.setStatus("current")
_CopySrcFileLocation_Type = DellNetConfigFileLocation
_CopySrcFileLocation_Object = MibTableColumn
copySrcFileLocation = _CopySrcFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 3),
    _CopySrcFileLocation_Type()
)
copySrcFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copySrcFileLocation.setStatus("current")
_CopySrcFileName_Type = DisplayString
_CopySrcFileName_Object = MibTableColumn
copySrcFileName = _CopySrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 4),
    _CopySrcFileName_Type()
)
copySrcFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copySrcFileName.setStatus("current")
_CopyDestFileType_Type = DellNetConfigFileType
_CopyDestFileType_Object = MibTableColumn
copyDestFileType = _CopyDestFileType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 5),
    _CopyDestFileType_Type()
)
copyDestFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyDestFileType.setStatus("current")
_CopyDestFileLocation_Type = DellNetConfigFileLocation
_CopyDestFileLocation_Object = MibTableColumn
copyDestFileLocation = _CopyDestFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 6),
    _CopyDestFileLocation_Type()
)
copyDestFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyDestFileLocation.setStatus("current")
_CopyDestFileName_Type = DisplayString
_CopyDestFileName_Object = MibTableColumn
copyDestFileName = _CopyDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 7),
    _CopyDestFileName_Type()
)
copyDestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyDestFileName.setStatus("current")
_CopyServerAddress_Type = IpAddress
_CopyServerAddress_Object = MibTableColumn
copyServerAddress = _CopyServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 8),
    _CopyServerAddress_Type()
)
copyServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyServerAddress.setStatus("deprecated")


class _CopyUserName_Type(DisplayString):
    """Custom type copyUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CopyUserName_Type.__name__ = "DisplayString"
_CopyUserName_Object = MibTableColumn
copyUserName = _CopyUserName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 9),
    _CopyUserName_Type()
)
copyUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyUserName.setStatus("current")


class _CopyUserPassword_Type(DisplayString):
    """Custom type copyUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CopyUserPassword_Type.__name__ = "DisplayString"
_CopyUserPassword_Object = MibTableColumn
copyUserPassword = _CopyUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 10),
    _CopyUserPassword_Type()
)
copyUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyUserPassword.setStatus("current")
_CopyState_Type = DellNetConfigCopyState
_CopyState_Object = MibTableColumn
copyState = _CopyState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 11),
    _CopyState_Type()
)
copyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyState.setStatus("current")
_CopyTimeStarted_Type = TimeTicks
_CopyTimeStarted_Object = MibTableColumn
copyTimeStarted = _CopyTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 12),
    _CopyTimeStarted_Type()
)
copyTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyTimeStarted.setStatus("current")
_CopyTimeCompleted_Type = TimeTicks
_CopyTimeCompleted_Object = MibTableColumn
copyTimeCompleted = _CopyTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 13),
    _CopyTimeCompleted_Type()
)
copyTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyTimeCompleted.setStatus("current")
_CopyFailCause_Type = DellNetConfigCopyFailCause
_CopyFailCause_Object = MibTableColumn
copyFailCause = _CopyFailCause_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 14),
    _CopyFailCause_Type()
)
copyFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyFailCause.setStatus("current")
_CopyEntryRowStatus_Type = RowStatus
_CopyEntryRowStatus_Object = MibTableColumn
copyEntryRowStatus = _CopyEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 15),
    _CopyEntryRowStatus_Type()
)
copyEntryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyEntryRowStatus.setStatus("current")
_CopyServerInetAddressType_Type = InetAddressType
_CopyServerInetAddressType_Object = MibTableColumn
copyServerInetAddressType = _CopyServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 16),
    _CopyServerInetAddressType_Type()
)
copyServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyServerInetAddressType.setStatus("current")
_CopyServerInetAddress_Type = InetAddress
_CopyServerInetAddress_Object = MibTableColumn
copyServerInetAddress = _CopyServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 1, 1, 1, 17),
    _CopyServerInetAddress_Type()
)
copyServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copyServerInetAddress.setStatus("current")
_DellNetCopyConfigTraps_ObjectIdentity = ObjectIdentity
dellNetCopyConfigTraps = _DellNetCopyConfigTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2)
)
_CopyAlarmMibNotifications_ObjectIdentity = ObjectIdentity
copyAlarmMibNotifications = _CopyAlarmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 0)
)
_CopyAlarmVariable_ObjectIdentity = ObjectIdentity
copyAlarmVariable = _CopyAlarmVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 1)
)
_CopyAlarmLevel_Type = Integer32
_CopyAlarmLevel_Object = MibScalar
copyAlarmLevel = _CopyAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 1, 1),
    _CopyAlarmLevel_Type()
)
copyAlarmLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    copyAlarmLevel.setStatus("current")
_CopyAlarmString_Type = OctetString
_CopyAlarmString_Object = MibScalar
copyAlarmString = _CopyAlarmString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 1, 2),
    _CopyAlarmString_Type()
)
copyAlarmString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    copyAlarmString.setStatus("current")
_CopyAlarmIndex_Type = Integer32
_CopyAlarmIndex_Object = MibScalar
copyAlarmIndex = _CopyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 1, 3),
    _CopyAlarmIndex_Type()
)
copyAlarmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    copyAlarmIndex.setStatus("current")

# Managed Objects groups


# Notification objects

copyConfigCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 0, 1)
)
copyConfigCompleted.setObjects(
      *(("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmLevel"),
        ("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmString"),
        ("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmIndex"))
)
if mibBuilder.loadTexts:
    copyConfigCompleted.setStatus(
        "current"
    )

configConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 0, 2)
)
configConflict.setObjects(
      *(("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmLevel"),
        ("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmString"),
        ("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmIndex"))
)
if mibBuilder.loadTexts:
    configConflict.setStatus(
        "current"
    )

configConflictClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 0, 3)
)
configConflictClear.setObjects(
      *(("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmLevel"),
        ("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmString"),
        ("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmIndex"))
)
if mibBuilder.loadTexts:
    configConflictClear.setStatus(
        "current"
    )

batchConfigCommitProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 0, 4)
)
batchConfigCommitProgress.setObjects(
      *(("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmLevel"),
        ("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmString"),
        ("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmIndex"))
)
if mibBuilder.loadTexts:
    batchConfigCommitProgress.setStatus(
        "current"
    )

batchConfigCommitCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 5, 1, 2, 0, 5)
)
batchConfigCommitCompleted.setObjects(
      *(("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmLevel"),
        ("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmString"),
        ("DELL-NETWORKING-COPY-CONFIG-MIB", "copyAlarmIndex"))
)
if mibBuilder.loadTexts:
    batchConfigCommitCompleted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-COPY-CONFIG-MIB",
    **{"DellNetConfigFileLocation": DellNetConfigFileLocation,
       "DellNetConfigFileType": DellNetConfigFileType,
       "DellNetConfigCopyState": DellNetConfigCopyState,
       "DellNetConfigCopyFailCause": DellNetConfigCopyFailCause,
       "dellNetCopyConfigMib": dellNetCopyConfigMib,
       "dellNetCopyConfigObjects": dellNetCopyConfigObjects,
       "dellNetCopyConfig": dellNetCopyConfig,
       "dellNetCopyTable": dellNetCopyTable,
       "dellNetCopyEntry": dellNetCopyEntry,
       "copyConfigIndex": copyConfigIndex,
       "copySrcFileType": copySrcFileType,
       "copySrcFileLocation": copySrcFileLocation,
       "copySrcFileName": copySrcFileName,
       "copyDestFileType": copyDestFileType,
       "copyDestFileLocation": copyDestFileLocation,
       "copyDestFileName": copyDestFileName,
       "copyServerAddress": copyServerAddress,
       "copyUserName": copyUserName,
       "copyUserPassword": copyUserPassword,
       "copyState": copyState,
       "copyTimeStarted": copyTimeStarted,
       "copyTimeCompleted": copyTimeCompleted,
       "copyFailCause": copyFailCause,
       "copyEntryRowStatus": copyEntryRowStatus,
       "copyServerInetAddressType": copyServerInetAddressType,
       "copyServerInetAddress": copyServerInetAddress,
       "dellNetCopyConfigTraps": dellNetCopyConfigTraps,
       "copyAlarmMibNotifications": copyAlarmMibNotifications,
       "copyConfigCompleted": copyConfigCompleted,
       "configConflict": configConflict,
       "configConflictClear": configConflictClear,
       "batchConfigCommitProgress": batchConfigCommitProgress,
       "batchConfigCommitCompleted": batchConfigCommitCompleted,
       "copyAlarmVariable": copyAlarmVariable,
       "copyAlarmLevel": copyAlarmLevel,
       "copyAlarmString": copyAlarmString,
       "copyAlarmIndex": copyAlarmIndex}
)

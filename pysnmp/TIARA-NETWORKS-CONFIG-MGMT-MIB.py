# SNMP MIB module (TIARA-NETWORKS-CONFIG-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-NETWORKS-CONFIG-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:37 2024
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
 NotificationType,
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
    "NotificationType",
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

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraConfigMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4)
)
tiaraConfigMgmtMib.setRevisions(
        ("1900-08-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfgMedium(Integer32, TextualConvention):
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
        *(("commandSource", 1),
          ("current", 2),
          ("erase-flash", 4),
          ("flash", 3),
          ("network", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CfgOperations_ObjectIdentity = ObjectIdentity
cfgOperations = _CfgOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1)
)
_CfgNetOperTable_Object = MibTable
cfgNetOperTable = _CfgNetOperTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cfgNetOperTable.setStatus("current")
_CfgNetOperEntry_Object = MibTableRow
cfgNetOperEntry = _CfgNetOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 1, 1)
)
cfgNetOperEntry.setIndexNames(
    (0, "TIARA-NETWORKS-CONFIG-MGMT-MIB", "cfgNetOperRandomNumber"),
)
if mibBuilder.loadTexts:
    cfgNetOperEntry.setStatus("current")
_CfgNetOperRandomNumber_Type = Integer32
_CfgNetOperRandomNumber_Object = MibTableColumn
cfgNetOperRandomNumber = _CfgNetOperRandomNumber_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 1, 1, 1),
    _CfgNetOperRandomNumber_Type()
)
cfgNetOperRandomNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgNetOperRandomNumber.setStatus("current")


class _CfgNetOperCommand_Type(Integer32):
    """Custom type cfgNetOperCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("save", 2))
    )


_CfgNetOperCommand_Type.__name__ = "Integer32"
_CfgNetOperCommand_Object = MibTableColumn
cfgNetOperCommand = _CfgNetOperCommand_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 1, 1, 2),
    _CfgNetOperCommand_Type()
)
cfgNetOperCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetOperCommand.setStatus("current")
_CfgNetOperAddress_Type = IpAddress
_CfgNetOperAddress_Object = MibTableColumn
cfgNetOperAddress = _CfgNetOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 1, 1, 3),
    _CfgNetOperAddress_Type()
)
cfgNetOperAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetOperAddress.setStatus("current")


class _CfgNetOperFileName_Type(DisplayString):
    """Custom type cfgNetOperFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CfgNetOperFileName_Type.__name__ = "DisplayString"
_CfgNetOperFileName_Object = MibTableColumn
cfgNetOperFileName = _CfgNetOperFileName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 1, 1, 4),
    _CfgNetOperFileName_Type()
)
cfgNetOperFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNetOperFileName.setStatus("current")


class _CfgNetOperStatus_Type(Integer32):
    """Custom type cfgNetOperStatus based on Integer32"""
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
        *(("fileAccessError", 4),
          ("fileOpenError", 6),
          ("idle", 0),
          ("inProgress", 1),
          ("networkError", 3),
          ("notEnoughMemory", 7),
          ("operationSuccess", 2),
          ("serverAccessError", 5),
          ("unknownFailure", 8))
    )


_CfgNetOperStatus_Type.__name__ = "Integer32"
_CfgNetOperStatus_Object = MibTableColumn
cfgNetOperStatus = _CfgNetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 1, 1, 5),
    _CfgNetOperStatus_Type()
)
cfgNetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgNetOperStatus.setStatus("current")
_CfgFlashOperTable_Object = MibTable
cfgFlashOperTable = _CfgFlashOperTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    cfgFlashOperTable.setStatus("current")
_CfgFlashOperEntry_Object = MibTableRow
cfgFlashOperEntry = _CfgFlashOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 2, 1)
)
cfgFlashOperEntry.setIndexNames(
    (0, "TIARA-NETWORKS-CONFIG-MGMT-MIB", "cfgFlashOperRandomNumber"),
)
if mibBuilder.loadTexts:
    cfgFlashOperEntry.setStatus("current")
_CfgFlashOperRandomNumber_Type = Integer32
_CfgFlashOperRandomNumber_Object = MibTableColumn
cfgFlashOperRandomNumber = _CfgFlashOperRandomNumber_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 2, 1, 1),
    _CfgFlashOperRandomNumber_Type()
)
cfgFlashOperRandomNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFlashOperRandomNumber.setStatus("current")


class _CfgFlashOperCommand_Type(Integer32):
    """Custom type cfgFlashOperCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("config", 3),
          ("erase", 2),
          ("save", 1))
    )


_CfgFlashOperCommand_Type.__name__ = "Integer32"
_CfgFlashOperCommand_Object = MibTableColumn
cfgFlashOperCommand = _CfgFlashOperCommand_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 2, 1, 2),
    _CfgFlashOperCommand_Type()
)
cfgFlashOperCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFlashOperCommand.setStatus("current")


class _CfgFlashOperFileName_Type(DisplayString):
    """Custom type cfgFlashOperFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CfgFlashOperFileName_Type.__name__ = "DisplayString"
_CfgFlashOperFileName_Object = MibTableColumn
cfgFlashOperFileName = _CfgFlashOperFileName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 2, 1, 3),
    _CfgFlashOperFileName_Type()
)
cfgFlashOperFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFlashOperFileName.setStatus("current")


class _CfgFlashOperStatus_Type(Integer32):
    """Custom type cfgFlashOperStatus based on Integer32"""
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
        *(("fileAccessError", 4),
          ("fileOpenError", 6),
          ("idle", 0),
          ("inProgress", 1),
          ("networkError", 3),
          ("notEnoughMemory", 7),
          ("operationSuccess", 2),
          ("serverAccessError", 5),
          ("unknownFailure", 8))
    )


_CfgFlashOperStatus_Type.__name__ = "Integer32"
_CfgFlashOperStatus_Object = MibTableColumn
cfgFlashOperStatus = _CfgFlashOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 1, 2, 1, 4),
    _CfgFlashOperStatus_Type()
)
cfgFlashOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgFlashOperStatus.setStatus("current")
_CfgMgmtEvents_ObjectIdentity = ObjectIdentity
cfgMgmtEvents = _CfgMgmtEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2)
)
_CfgCurrentLastChanged_Type = TimeTicks
_CfgCurrentLastChanged_Object = MibScalar
cfgCurrentLastChanged = _CfgCurrentLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 1),
    _CfgCurrentLastChanged_Type()
)
cfgCurrentLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgCurrentLastChanged.setStatus("current")
_CfgCurrentLastSaved_Type = TimeTicks
_CfgCurrentLastSaved_Object = MibScalar
cfgCurrentLastSaved = _CfgCurrentLastSaved_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 2),
    _CfgCurrentLastSaved_Type()
)
cfgCurrentLastSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgCurrentLastSaved.setStatus("current")


class _CfgMaxEvents_Type(Integer32):
    """Custom type cfgMaxEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CfgMaxEvents_Type.__name__ = "Integer32"
_CfgMaxEvents_Object = MibScalar
cfgMaxEvents = _CfgMaxEvents_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 3),
    _CfgMaxEvents_Type()
)
cfgMaxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgMaxEvents.setStatus("current")
_CfgEventTable_Object = MibTable
cfgEventTable = _CfgEventTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    cfgEventTable.setStatus("current")
_CfgEventEntry_Object = MibTableRow
cfgEventEntry = _CfgEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 4, 1)
)
cfgEventEntry.setIndexNames(
    (0, "TIARA-NETWORKS-CONFIG-MGMT-MIB", "cfgEventIndex"),
)
if mibBuilder.loadTexts:
    cfgEventEntry.setStatus("current")


class _CfgEventIndex_Type(Integer32):
    """Custom type cfgEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_CfgEventIndex_Type.__name__ = "Integer32"
_CfgEventIndex_Object = MibTableColumn
cfgEventIndex = _CfgEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 4, 1, 1),
    _CfgEventIndex_Type()
)
cfgEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgEventIndex.setStatus("current")
_CfgEventTime_Type = TimeTicks
_CfgEventTime_Object = MibTableColumn
cfgEventTime = _CfgEventTime_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 4, 1, 2),
    _CfgEventTime_Type()
)
cfgEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEventTime.setStatus("current")


class _CfgEventConfigProtocol_Type(Integer32):
    """Custom type cfgEventConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commandLine", 1),
          ("http", 3),
          ("snmp", 2))
    )


_CfgEventConfigProtocol_Type.__name__ = "Integer32"
_CfgEventConfigProtocol_Object = MibTableColumn
cfgEventConfigProtocol = _CfgEventConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 4, 1, 3),
    _CfgEventConfigProtocol_Type()
)
cfgEventConfigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEventConfigProtocol.setStatus("current")
_CfgEventConfigSrc_Type = CfgMedium
_CfgEventConfigSrc_Object = MibTableColumn
cfgEventConfigSrc = _CfgEventConfigSrc_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 4, 1, 4),
    _CfgEventConfigSrc_Type()
)
cfgEventConfigSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEventConfigSrc.setStatus("current")
_CfgEventConfigDst_Type = CfgMedium
_CfgEventConfigDst_Object = MibTableColumn
cfgEventConfigDst = _CfgEventConfigDst_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 4, 1, 5),
    _CfgEventConfigDst_Type()
)
cfgEventConfigDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEventConfigDst.setStatus("current")


class _CfgEventLoginType_Type(Integer32):
    """Custom type cfgEventLoginType based on Integer32"""
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
        *(("console", 2),
          ("dial", 5),
          ("other", 6),
          ("rlogin", 4),
          ("telnet", 3),
          ("unknown", 1))
    )


_CfgEventLoginType_Type.__name__ = "Integer32"
_CfgEventLoginType_Object = MibTableColumn
cfgEventLoginType = _CfgEventLoginType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 4, 1, 6),
    _CfgEventLoginType_Type()
)
cfgEventLoginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEventLoginType.setStatus("current")


class _CfgEventTerminalUser_Type(DisplayString):
    """Custom type cfgEventTerminalUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CfgEventTerminalUser_Type.__name__ = "DisplayString"
_CfgEventTerminalUser_Object = MibTableColumn
cfgEventTerminalUser = _CfgEventTerminalUser_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 4, 1, 7),
    _CfgEventTerminalUser_Type()
)
cfgEventTerminalUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEventTerminalUser.setStatus("current")
_CfgEventConfigSrcAddress_Type = IpAddress
_CfgEventConfigSrcAddress_Object = MibTableColumn
cfgEventConfigSrcAddress = _CfgEventConfigSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 4, 1, 8),
    _CfgEventConfigSrcAddress_Type()
)
cfgEventConfigSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEventConfigSrcAddress.setStatus("current")


class _CfgEventFileName_Type(DisplayString):
    """Custom type cfgEventFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CfgEventFileName_Type.__name__ = "DisplayString"
_CfgEventFileName_Object = MibTableColumn
cfgEventFileName = _CfgEventFileName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 2, 4, 1, 9),
    _CfgEventFileName_Type()
)
cfgEventFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEventFileName.setStatus("current")
_CfgNotificationEnables_ObjectIdentity = ObjectIdentity
cfgNotificationEnables = _CfgNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 3)
)


class _CfgEnableChangeNotification_Type(TruthValue):
    """Custom type cfgEnableChangeNotification based on TruthValue"""


_CfgEnableChangeNotification_Object = MibScalar
cfgEnableChangeNotification = _CfgEnableChangeNotification_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 3, 1),
    _CfgEnableChangeNotification_Type()
)
cfgEnableChangeNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEnableChangeNotification.setStatus("current")


class _CfgEnableSaveNotification_Type(TruthValue):
    """Custom type cfgEnableSaveNotification based on TruthValue"""


_CfgEnableSaveNotification_Object = MibScalar
cfgEnableSaveNotification = _CfgEnableSaveNotification_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 3, 2),
    _CfgEnableSaveNotification_Type()
)
cfgEnableSaveNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEnableSaveNotification.setStatus("current")
_CfgMgmtNotifications_ObjectIdentity = ObjectIdentity
cfgMgmtNotifications = _CfgMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 4)
)

# Managed Objects groups


# Notification objects

cfgEventChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 4, 0, 1)
)
cfgEventChangeNotification.setObjects(
      *(("TIARA-NETWORKS-CONFIG-MGMT-MIB", "cfgEventConfigProtocol"),
        ("TIARA-NETWORKS-CONFIG-MGMT-MIB", "cfgEventConfigSrc"),
        ("TIARA-NETWORKS-CONFIG-MGMT-MIB", "cfgEventConfigDst"))
)
if mibBuilder.loadTexts:
    cfgEventChangeNotification.setStatus(
        ""
    )

cfgEventSaveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 4, 4, 0, 2)
)
cfgEventSaveNotification.setObjects(
      *(("TIARA-NETWORKS-CONFIG-MGMT-MIB", "cfgEventConfigProtocol"),
        ("TIARA-NETWORKS-CONFIG-MGMT-MIB", "cfgEventConfigSrc"),
        ("TIARA-NETWORKS-CONFIG-MGMT-MIB", "cfgEventConfigDst"))
)
if mibBuilder.loadTexts:
    cfgEventSaveNotification.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-NETWORKS-CONFIG-MGMT-MIB",
    **{"CfgMedium": CfgMedium,
       "tiaraConfigMgmtMib": tiaraConfigMgmtMib,
       "cfgOperations": cfgOperations,
       "cfgNetOperTable": cfgNetOperTable,
       "cfgNetOperEntry": cfgNetOperEntry,
       "cfgNetOperRandomNumber": cfgNetOperRandomNumber,
       "cfgNetOperCommand": cfgNetOperCommand,
       "cfgNetOperAddress": cfgNetOperAddress,
       "cfgNetOperFileName": cfgNetOperFileName,
       "cfgNetOperStatus": cfgNetOperStatus,
       "cfgFlashOperTable": cfgFlashOperTable,
       "cfgFlashOperEntry": cfgFlashOperEntry,
       "cfgFlashOperRandomNumber": cfgFlashOperRandomNumber,
       "cfgFlashOperCommand": cfgFlashOperCommand,
       "cfgFlashOperFileName": cfgFlashOperFileName,
       "cfgFlashOperStatus": cfgFlashOperStatus,
       "cfgMgmtEvents": cfgMgmtEvents,
       "cfgCurrentLastChanged": cfgCurrentLastChanged,
       "cfgCurrentLastSaved": cfgCurrentLastSaved,
       "cfgMaxEvents": cfgMaxEvents,
       "cfgEventTable": cfgEventTable,
       "cfgEventEntry": cfgEventEntry,
       "cfgEventIndex": cfgEventIndex,
       "cfgEventTime": cfgEventTime,
       "cfgEventConfigProtocol": cfgEventConfigProtocol,
       "cfgEventConfigSrc": cfgEventConfigSrc,
       "cfgEventConfigDst": cfgEventConfigDst,
       "cfgEventLoginType": cfgEventLoginType,
       "cfgEventTerminalUser": cfgEventTerminalUser,
       "cfgEventConfigSrcAddress": cfgEventConfigSrcAddress,
       "cfgEventFileName": cfgEventFileName,
       "cfgNotificationEnables": cfgNotificationEnables,
       "cfgEnableChangeNotification": cfgEnableChangeNotification,
       "cfgEnableSaveNotification": cfgEnableSaveNotification,
       "cfgMgmtNotifications": cfgMgmtNotifications,
       "cfgEventChangeNotification": cfgEventChangeNotification,
       "cfgEventSaveNotification": cfgEventSaveNotification}
)

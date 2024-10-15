# SNMP MIB module (CONFIG-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CONFIG-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:55 2024
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

(ntEnterpriseDataTasmanMgmt,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanMgmt")

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

nnconfigMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4)
)
nnconfigMgmtMib.setRevisions(
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

_NncfgOperations_ObjectIdentity = ObjectIdentity
nncfgOperations = _NncfgOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 1)
)
_NncfgNetOperTable_Object = MibTable
nncfgNetOperTable = _NncfgNetOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    nncfgNetOperTable.setStatus("current")
_NncfgNetOperEntry_Object = MibTableRow
nncfgNetOperEntry = _NncfgNetOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 1, 1, 1)
)
nncfgNetOperEntry.setIndexNames(
    (0, "CONFIG-MGMT-MIB", "nncfgNetOperRandomNumber"),
)
if mibBuilder.loadTexts:
    nncfgNetOperEntry.setStatus("current")
_NncfgNetOperRandomNumber_Type = Integer32
_NncfgNetOperRandomNumber_Object = MibTableColumn
nncfgNetOperRandomNumber = _NncfgNetOperRandomNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 1, 1, 1, 1),
    _NncfgNetOperRandomNumber_Type()
)
nncfgNetOperRandomNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncfgNetOperRandomNumber.setStatus("current")


class _NncfgNetOperCommand_Type(Integer32):
    """Custom type nncfgNetOperCommand based on Integer32"""
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


_NncfgNetOperCommand_Type.__name__ = "Integer32"
_NncfgNetOperCommand_Object = MibTableColumn
nncfgNetOperCommand = _NncfgNetOperCommand_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 1, 1, 1, 2),
    _NncfgNetOperCommand_Type()
)
nncfgNetOperCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncfgNetOperCommand.setStatus("current")
_NncfgNetOperAddress_Type = IpAddress
_NncfgNetOperAddress_Object = MibTableColumn
nncfgNetOperAddress = _NncfgNetOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 1, 1, 1, 3),
    _NncfgNetOperAddress_Type()
)
nncfgNetOperAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncfgNetOperAddress.setStatus("current")


class _NncfgNetOperFileName_Type(DisplayString):
    """Custom type nncfgNetOperFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NncfgNetOperFileName_Type.__name__ = "DisplayString"
_NncfgNetOperFileName_Object = MibTableColumn
nncfgNetOperFileName = _NncfgNetOperFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 1, 1, 1, 4),
    _NncfgNetOperFileName_Type()
)
nncfgNetOperFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncfgNetOperFileName.setStatus("current")


class _NncfgNetOperStatus_Type(Integer32):
    """Custom type nncfgNetOperStatus based on Integer32"""
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


_NncfgNetOperStatus_Type.__name__ = "Integer32"
_NncfgNetOperStatus_Object = MibTableColumn
nncfgNetOperStatus = _NncfgNetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 1, 1, 1, 5),
    _NncfgNetOperStatus_Type()
)
nncfgNetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgNetOperStatus.setStatus("current")
_NncfgMgmtEvents_ObjectIdentity = ObjectIdentity
nncfgMgmtEvents = _NncfgMgmtEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2)
)
_NncfgCurrentLastChanged_Type = TimeTicks
_NncfgCurrentLastChanged_Object = MibScalar
nncfgCurrentLastChanged = _NncfgCurrentLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 1),
    _NncfgCurrentLastChanged_Type()
)
nncfgCurrentLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgCurrentLastChanged.setStatus("current")
_NncfgCurrentLastSaved_Type = TimeTicks
_NncfgCurrentLastSaved_Object = MibScalar
nncfgCurrentLastSaved = _NncfgCurrentLastSaved_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 2),
    _NncfgCurrentLastSaved_Type()
)
nncfgCurrentLastSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgCurrentLastSaved.setStatus("current")


class _NncfgMaxEvents_Type(Integer32):
    """Custom type nncfgMaxEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_NncfgMaxEvents_Type.__name__ = "Integer32"
_NncfgMaxEvents_Object = MibScalar
nncfgMaxEvents = _NncfgMaxEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 3),
    _NncfgMaxEvents_Type()
)
nncfgMaxEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgMaxEvents.setStatus("current")
_NncfgEventTable_Object = MibTable
nncfgEventTable = _NncfgEventTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    nncfgEventTable.setStatus("current")
_NncfgEventEntry_Object = MibTableRow
nncfgEventEntry = _NncfgEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 4, 1)
)
nncfgEventEntry.setIndexNames(
    (0, "CONFIG-MGMT-MIB", "nncfgEventIndex"),
)
if mibBuilder.loadTexts:
    nncfgEventEntry.setStatus("current")


class _NncfgEventIndex_Type(Integer32):
    """Custom type nncfgEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_NncfgEventIndex_Type.__name__ = "Integer32"
_NncfgEventIndex_Object = MibTableColumn
nncfgEventIndex = _NncfgEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 4, 1, 1),
    _NncfgEventIndex_Type()
)
nncfgEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncfgEventIndex.setStatus("current")
_NncfgEventTime_Type = TimeTicks
_NncfgEventTime_Object = MibTableColumn
nncfgEventTime = _NncfgEventTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 4, 1, 2),
    _NncfgEventTime_Type()
)
nncfgEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgEventTime.setStatus("current")


class _NncfgEventConfigProtocol_Type(Integer32):
    """Custom type nncfgEventConfigProtocol based on Integer32"""
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


_NncfgEventConfigProtocol_Type.__name__ = "Integer32"
_NncfgEventConfigProtocol_Object = MibTableColumn
nncfgEventConfigProtocol = _NncfgEventConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 4, 1, 3),
    _NncfgEventConfigProtocol_Type()
)
nncfgEventConfigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgEventConfigProtocol.setStatus("current")
_NncfgEventConfigSrc_Type = CfgMedium
_NncfgEventConfigSrc_Object = MibTableColumn
nncfgEventConfigSrc = _NncfgEventConfigSrc_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 4, 1, 4),
    _NncfgEventConfigSrc_Type()
)
nncfgEventConfigSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgEventConfigSrc.setStatus("current")
_NncfgEventConfigDst_Type = CfgMedium
_NncfgEventConfigDst_Object = MibTableColumn
nncfgEventConfigDst = _NncfgEventConfigDst_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 4, 1, 5),
    _NncfgEventConfigDst_Type()
)
nncfgEventConfigDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgEventConfigDst.setStatus("current")


class _NncfgEventLoginType_Type(Integer32):
    """Custom type nncfgEventLoginType based on Integer32"""
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


_NncfgEventLoginType_Type.__name__ = "Integer32"
_NncfgEventLoginType_Object = MibTableColumn
nncfgEventLoginType = _NncfgEventLoginType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 4, 1, 6),
    _NncfgEventLoginType_Type()
)
nncfgEventLoginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgEventLoginType.setStatus("current")


class _NncfgEventTerminalUser_Type(DisplayString):
    """Custom type nncfgEventTerminalUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NncfgEventTerminalUser_Type.__name__ = "DisplayString"
_NncfgEventTerminalUser_Object = MibTableColumn
nncfgEventTerminalUser = _NncfgEventTerminalUser_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 4, 1, 7),
    _NncfgEventTerminalUser_Type()
)
nncfgEventTerminalUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgEventTerminalUser.setStatus("current")
_NncfgEventConfigSrcAddress_Type = IpAddress
_NncfgEventConfigSrcAddress_Object = MibTableColumn
nncfgEventConfigSrcAddress = _NncfgEventConfigSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 4, 1, 8),
    _NncfgEventConfigSrcAddress_Type()
)
nncfgEventConfigSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgEventConfigSrcAddress.setStatus("current")


class _NncfgEventFileName_Type(DisplayString):
    """Custom type nncfgEventFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NncfgEventFileName_Type.__name__ = "DisplayString"
_NncfgEventFileName_Object = MibTableColumn
nncfgEventFileName = _NncfgEventFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 2, 4, 1, 9),
    _NncfgEventFileName_Type()
)
nncfgEventFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncfgEventFileName.setStatus("current")
_NncfgNotificationEnables_ObjectIdentity = ObjectIdentity
nncfgNotificationEnables = _NncfgNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 3)
)


class _NncfgEnableChangeNotification_Type(TruthValue):
    """Custom type nncfgEnableChangeNotification based on TruthValue"""


_NncfgEnableChangeNotification_Object = MibScalar
nncfgEnableChangeNotification = _NncfgEnableChangeNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 3, 1),
    _NncfgEnableChangeNotification_Type()
)
nncfgEnableChangeNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncfgEnableChangeNotification.setStatus("current")


class _NncfgEnableSaveNotification_Type(TruthValue):
    """Custom type nncfgEnableSaveNotification based on TruthValue"""


_NncfgEnableSaveNotification_Object = MibScalar
nncfgEnableSaveNotification = _NncfgEnableSaveNotification_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 3, 2),
    _NncfgEnableSaveNotification_Type()
)
nncfgEnableSaveNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncfgEnableSaveNotification.setStatus("current")
_NncfgMgmtNotifications_ObjectIdentity = ObjectIdentity
nncfgMgmtNotifications = _NncfgMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 4)
)
_NncfgMgmtTraps_ObjectIdentity = ObjectIdentity
nncfgMgmtTraps = _NncfgMgmtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 4, 0)
)

# Managed Objects groups


# Notification objects

nncfgEventChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 4, 0, 1)
)
nncfgEventChangeNotification.setObjects(
      *(("CONFIG-MGMT-MIB", "nncfgEventConfigProtocol"),
        ("CONFIG-MGMT-MIB", "nncfgEventConfigSrc"),
        ("CONFIG-MGMT-MIB", "nncfgEventConfigDst"))
)
if mibBuilder.loadTexts:
    nncfgEventChangeNotification.setStatus(
        "current"
    )

nncfgEventSaveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 4, 0, 2)
)
nncfgEventSaveNotification.setObjects(
      *(("CONFIG-MGMT-MIB", "nncfgEventConfigProtocol"),
        ("CONFIG-MGMT-MIB", "nncfgEventConfigSrc"),
        ("CONFIG-MGMT-MIB", "nncfgEventConfigDst"))
)
if mibBuilder.loadTexts:
    nncfgEventSaveNotification.setStatus(
        "current"
    )


# Notifications groups

nnconfigMgmtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 4, 5)
)
nnconfigMgmtNotificationGroup.setObjects(
      *(("CONFIG-MGMT-MIB", "nncfgEventChangeNotification"),
        ("CONFIG-MGMT-MIB", "nncfgEventSaveNotification"))
)
if mibBuilder.loadTexts:
    nnconfigMgmtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONFIG-MGMT-MIB",
    **{"CfgMedium": CfgMedium,
       "nnconfigMgmtMib": nnconfigMgmtMib,
       "nncfgOperations": nncfgOperations,
       "nncfgNetOperTable": nncfgNetOperTable,
       "nncfgNetOperEntry": nncfgNetOperEntry,
       "nncfgNetOperRandomNumber": nncfgNetOperRandomNumber,
       "nncfgNetOperCommand": nncfgNetOperCommand,
       "nncfgNetOperAddress": nncfgNetOperAddress,
       "nncfgNetOperFileName": nncfgNetOperFileName,
       "nncfgNetOperStatus": nncfgNetOperStatus,
       "nncfgMgmtEvents": nncfgMgmtEvents,
       "nncfgCurrentLastChanged": nncfgCurrentLastChanged,
       "nncfgCurrentLastSaved": nncfgCurrentLastSaved,
       "nncfgMaxEvents": nncfgMaxEvents,
       "nncfgEventTable": nncfgEventTable,
       "nncfgEventEntry": nncfgEventEntry,
       "nncfgEventIndex": nncfgEventIndex,
       "nncfgEventTime": nncfgEventTime,
       "nncfgEventConfigProtocol": nncfgEventConfigProtocol,
       "nncfgEventConfigSrc": nncfgEventConfigSrc,
       "nncfgEventConfigDst": nncfgEventConfigDst,
       "nncfgEventLoginType": nncfgEventLoginType,
       "nncfgEventTerminalUser": nncfgEventTerminalUser,
       "nncfgEventConfigSrcAddress": nncfgEventConfigSrcAddress,
       "nncfgEventFileName": nncfgEventFileName,
       "nncfgNotificationEnables": nncfgNotificationEnables,
       "nncfgEnableChangeNotification": nncfgEnableChangeNotification,
       "nncfgEnableSaveNotification": nncfgEnableSaveNotification,
       "nncfgMgmtNotifications": nncfgMgmtNotifications,
       "nncfgMgmtTraps": nncfgMgmtTraps,
       "nncfgEventChangeNotification": nncfgEventChangeNotification,
       "nncfgEventSaveNotification": nncfgEventSaveNotification,
       "nnconfigMgmtNotificationGroup": nnconfigMgmtNotificationGroup}
)

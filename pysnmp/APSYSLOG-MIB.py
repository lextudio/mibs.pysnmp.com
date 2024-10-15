# SNMP MIB module (APSYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APSYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:01 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

apSyslogModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("debug", 9),
          ("emergency", 1),
          ("info", 7),
          ("major", 3),
          ("minor", 4),
          ("notice", 6),
          ("trace", 8),
          ("warning", 5))
    )



# MIB Managed Objects in the order of their OIDs

_ApSyslogMIBObjects_ObjectIdentity = ObjectIdentity
apSyslogMIBObjects = _ApSyslogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1)
)
_ApSyslogBasic_ObjectIdentity = ObjectIdentity
apSyslogBasic = _ApSyslogBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 1)
)
_ApSyslogNotificationsSent_Type = Counter32
_ApSyslogNotificationsSent_Object = MibScalar
apSyslogNotificationsSent = _ApSyslogNotificationsSent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 1, 1),
    _ApSyslogNotificationsSent_Type()
)
apSyslogNotificationsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogNotificationsSent.setStatus("current")
if mibBuilder.loadTexts:
    apSyslogNotificationsSent.setUnits("notifications")


class _ApSyslogNotificationsEnabled_Type(TruthValue):
    """Custom type apSyslogNotificationsEnabled based on TruthValue"""


_ApSyslogNotificationsEnabled_Object = MibScalar
apSyslogNotificationsEnabled = _ApSyslogNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 1, 2),
    _ApSyslogNotificationsEnabled_Type()
)
apSyslogNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogNotificationsEnabled.setStatus("current")


class _ApSyslogMaxLevel_Type(SyslogLevel):
    """Custom type apSyslogMaxLevel based on SyslogLevel"""


_ApSyslogMaxLevel_Object = MibScalar
apSyslogMaxLevel = _ApSyslogMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 1, 3),
    _ApSyslogMaxLevel_Type()
)
apSyslogMaxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogMaxLevel.setStatus("current")
_ApSyslogMsgIgnores_Type = Counter32
_ApSyslogMsgIgnores_Object = MibScalar
apSyslogMsgIgnores = _ApSyslogMsgIgnores_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 1, 4),
    _ApSyslogMsgIgnores_Type()
)
apSyslogMsgIgnores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogMsgIgnores.setStatus("current")
if mibBuilder.loadTexts:
    apSyslogMsgIgnores.setUnits("messages")
_ApSyslogMsgDrops_Type = Counter32
_ApSyslogMsgDrops_Object = MibScalar
apSyslogMsgDrops = _ApSyslogMsgDrops_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 1, 5),
    _ApSyslogMsgDrops_Type()
)
apSyslogMsgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogMsgDrops.setStatus("current")
if mibBuilder.loadTexts:
    apSyslogMsgDrops.setUnits("messages")
_ApSyslogHistory_ObjectIdentity = ObjectIdentity
apSyslogHistory = _ApSyslogHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 2)
)


class _ApSyslogHistTableMaxLength_Type(Integer32):
    """Custom type apSyslogHistTableMaxLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_ApSyslogHistTableMaxLength_Type.__name__ = "Integer32"
_ApSyslogHistTableMaxLength_Object = MibScalar
apSyslogHistTableMaxLength = _ApSyslogHistTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 2, 1),
    _ApSyslogHistTableMaxLength_Type()
)
apSyslogHistTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogHistTableMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    apSyslogHistTableMaxLength.setUnits("entries")
_ApSyslogHistMsgsFlushed_Type = Counter32
_ApSyslogHistMsgsFlushed_Object = MibScalar
apSyslogHistMsgsFlushed = _ApSyslogHistMsgsFlushed_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 2, 2),
    _ApSyslogHistMsgsFlushed_Type()
)
apSyslogHistMsgsFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogHistMsgsFlushed.setStatus("current")
if mibBuilder.loadTexts:
    apSyslogHistMsgsFlushed.setUnits("messages")
_ApSyslogHistoryTable_Object = MibTable
apSyslogHistoryTable = _ApSyslogHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    apSyslogHistoryTable.setStatus("current")
_ApSyslogHistoryEntry_Object = MibTableRow
apSyslogHistoryEntry = _ApSyslogHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 2, 3, 1)
)
apSyslogHistoryEntry.setIndexNames(
    (0, "APSYSLOG-MIB", "apSyslogHistIndex"),
)
if mibBuilder.loadTexts:
    apSyslogHistoryEntry.setStatus("current")


class _ApSyslogHistIndex_Type(Integer32):
    """Custom type apSyslogHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApSyslogHistIndex_Type.__name__ = "Integer32"
_ApSyslogHistIndex_Object = MibTableColumn
apSyslogHistIndex = _ApSyslogHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 2, 3, 1, 1),
    _ApSyslogHistIndex_Type()
)
apSyslogHistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogHistIndex.setStatus("current")


class _ApSyslogHistFrom_Type(DisplayString):
    """Custom type apSyslogHistFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ApSyslogHistFrom_Type.__name__ = "DisplayString"
_ApSyslogHistFrom_Object = MibTableColumn
apSyslogHistFrom = _ApSyslogHistFrom_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 2, 3, 1, 2),
    _ApSyslogHistFrom_Type()
)
apSyslogHistFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogHistFrom.setStatus("current")
_ApSyslogHistLevel_Type = SyslogLevel
_ApSyslogHistLevel_Object = MibTableColumn
apSyslogHistLevel = _ApSyslogHistLevel_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 2, 3, 1, 3),
    _ApSyslogHistLevel_Type()
)
apSyslogHistLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogHistLevel.setStatus("current")


class _ApSyslogHistType_Type(DisplayString):
    """Custom type apSyslogHistType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ApSyslogHistType_Type.__name__ = "DisplayString"
_ApSyslogHistType_Object = MibTableColumn
apSyslogHistType = _ApSyslogHistType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 2, 3, 1, 4),
    _ApSyslogHistType_Type()
)
apSyslogHistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogHistType.setStatus("current")


class _ApSyslogHistContent_Type(DisplayString):
    """Custom type apSyslogHistContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSyslogHistContent_Type.__name__ = "DisplayString"
_ApSyslogHistContent_Object = MibTableColumn
apSyslogHistContent = _ApSyslogHistContent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 2, 3, 1, 5),
    _ApSyslogHistContent_Type()
)
apSyslogHistContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogHistContent.setStatus("current")
_ApSyslogHistTimestamp_Type = TimeStamp
_ApSyslogHistTimestamp_Object = MibTableColumn
apSyslogHistTimestamp = _ApSyslogHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 1, 2, 3, 1, 6),
    _ApSyslogHistTimestamp_Type()
)
apSyslogHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSyslogHistTimestamp.setStatus("current")
_ApSyslogMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
apSyslogMIBNotificationPrefix = _ApSyslogMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 2)
)
_ApSyslogMIBNotifications_ObjectIdentity = ObjectIdentity
apSyslogMIBNotifications = _ApSyslogMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 2, 0)
)
_ApSyslogMIBConformance_ObjectIdentity = ObjectIdentity
apSyslogMIBConformance = _ApSyslogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 3)
)
_ApSyslogMIBCompliances_ObjectIdentity = ObjectIdentity
apSyslogMIBCompliances = _ApSyslogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 3, 1)
)
_ApSyslogMIBGroups_ObjectIdentity = ObjectIdentity
apSyslogMIBGroups = _ApSyslogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 3, 2)
)

# Managed Objects groups

apSyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 3, 2, 1)
)
apSyslogGroup.setObjects(
      *(("APSYSLOG-MIB", "apSyslogNotificationsSent"),
        ("APSYSLOG-MIB", "apSyslogNotificationsEnabled"),
        ("APSYSLOG-MIB", "apSyslogMaxLevel"),
        ("APSYSLOG-MIB", "apSyslogMsgIgnores"),
        ("APSYSLOG-MIB", "apSyslogMsgDrops"),
        ("APSYSLOG-MIB", "apSyslogHistTableMaxLength"),
        ("APSYSLOG-MIB", "apSyslogHistMsgsFlushed"),
        ("APSYSLOG-MIB", "apSyslogHistIndex"),
        ("APSYSLOG-MIB", "apSyslogHistFrom"),
        ("APSYSLOG-MIB", "apSyslogHistLevel"),
        ("APSYSLOG-MIB", "apSyslogHistType"),
        ("APSYSLOG-MIB", "apSyslogHistContent"),
        ("APSYSLOG-MIB", "apSyslogHistTimestamp"))
)
if mibBuilder.loadTexts:
    apSyslogGroup.setStatus("current")


# Notification objects

apSyslogMessageGenerated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 2, 0, 1)
)
apSyslogMessageGenerated.setObjects(
      *(("APSYSLOG-MIB", "apSyslogHistFrom"),
        ("APSYSLOG-MIB", "apSyslogHistLevel"),
        ("APSYSLOG-MIB", "apSyslogHistType"),
        ("APSYSLOG-MIB", "apSyslogHistContent"),
        ("APSYSLOG-MIB", "apSyslogHistTimestamp"))
)
if mibBuilder.loadTexts:
    apSyslogMessageGenerated.setStatus(
        "current"
    )


# Notifications groups

apSyslogNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 1, 3, 2, 2)
)
apSyslogNotificationsGroup.setObjects(
    ("APSYSLOG-MIB", "apSyslogMessageGenerated")
)
if mibBuilder.loadTexts:
    apSyslogNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APSYSLOG-MIB",
    **{"SyslogLevel": SyslogLevel,
       "apSyslogModule": apSyslogModule,
       "apSyslogMIBObjects": apSyslogMIBObjects,
       "apSyslogBasic": apSyslogBasic,
       "apSyslogNotificationsSent": apSyslogNotificationsSent,
       "apSyslogNotificationsEnabled": apSyslogNotificationsEnabled,
       "apSyslogMaxLevel": apSyslogMaxLevel,
       "apSyslogMsgIgnores": apSyslogMsgIgnores,
       "apSyslogMsgDrops": apSyslogMsgDrops,
       "apSyslogHistory": apSyslogHistory,
       "apSyslogHistTableMaxLength": apSyslogHistTableMaxLength,
       "apSyslogHistMsgsFlushed": apSyslogHistMsgsFlushed,
       "apSyslogHistoryTable": apSyslogHistoryTable,
       "apSyslogHistoryEntry": apSyslogHistoryEntry,
       "apSyslogHistIndex": apSyslogHistIndex,
       "apSyslogHistFrom": apSyslogHistFrom,
       "apSyslogHistLevel": apSyslogHistLevel,
       "apSyslogHistType": apSyslogHistType,
       "apSyslogHistContent": apSyslogHistContent,
       "apSyslogHistTimestamp": apSyslogHistTimestamp,
       "apSyslogMIBNotificationPrefix": apSyslogMIBNotificationPrefix,
       "apSyslogMIBNotifications": apSyslogMIBNotifications,
       "apSyslogMessageGenerated": apSyslogMessageGenerated,
       "apSyslogMIBConformance": apSyslogMIBConformance,
       "apSyslogMIBCompliances": apSyslogMIBCompliances,
       "apSyslogMIBGroups": apSyslogMIBGroups,
       "apSyslogGroup": apSyslogGroup,
       "apSyslogNotificationsGroup": apSyslogNotificationsGroup}
)

# SNMP MIB module (TIMETRA-CLEAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-CLEAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:02:04 2024
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxEventAppIndex,) = mibBuilder.importSymbols(
    "TIMETRA-LOG-MIB",
    "tmnxEventAppIndex")

(TNamedItem,
 TmnxActionType) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TmnxActionType")


# MODULE-IDENTITY

timetraClearMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 13)
)
timetraClearMIBModule.setRevisions(
        ("1905-01-24 00:00",
         "1904-06-02 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1902-02-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxClearConformance_ObjectIdentity = ObjectIdentity
tmnxClearConformance = _TmnxClearConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13)
)
_TmnxClearCompliances_ObjectIdentity = ObjectIdentity
tmnxClearCompliances = _TmnxClearCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13, 1)
)
_TmnxClearGroups_ObjectIdentity = ObjectIdentity
tmnxClearGroups = _TmnxClearGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13, 2)
)
_TmnxClearObjs_ObjectIdentity = ObjectIdentity
tmnxClearObjs = _TmnxClearObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13)
)
_TmnxClearTable_Object = MibTable
tmnxClearTable = _TmnxClearTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    tmnxClearTable.setStatus("current")
_TmnxClearEntry_Object = MibTableRow
tmnxClearEntry = _TmnxClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1)
)
tmnxClearEntry.setIndexNames(
    (0, "TIMETRA-LOG-MIB", "tmnxEventAppIndex"),
    (0, "TIMETRA-CLEAR-MIB", "tmnxClearIndex"),
)
if mibBuilder.loadTexts:
    tmnxClearEntry.setStatus("current")


class _TmnxClearIndex_Type(Integer32):
    """Custom type tmnxClearIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxClearIndex_Type.__name__ = "Integer32"
_TmnxClearIndex_Object = MibTableColumn
tmnxClearIndex = _TmnxClearIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 1),
    _TmnxClearIndex_Type()
)
tmnxClearIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxClearIndex.setStatus("current")
_TmnxClearName_Type = TNamedItem
_TmnxClearName_Object = MibTableColumn
tmnxClearName = _TmnxClearName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 2),
    _TmnxClearName_Type()
)
tmnxClearName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxClearName.setStatus("current")


class _TmnxClearParams_Type(OctetString):
    """Custom type tmnxClearParams based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxClearParams_Type.__name__ = "OctetString"
_TmnxClearParams_Object = MibTableColumn
tmnxClearParams = _TmnxClearParams_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 3),
    _TmnxClearParams_Type()
)
tmnxClearParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxClearParams.setStatus("current")


class _TmnxClearAction_Type(TmnxActionType):
    """Custom type tmnxClearAction based on TmnxActionType"""


_TmnxClearAction_Object = MibTableColumn
tmnxClearAction = _TmnxClearAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 4),
    _TmnxClearAction_Type()
)
tmnxClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxClearAction.setStatus("current")
_TmnxClearLastClearedTime_Type = TimeStamp
_TmnxClearLastClearedTime_Object = MibTableColumn
tmnxClearLastClearedTime = _TmnxClearLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 5),
    _TmnxClearLastClearedTime_Type()
)
tmnxClearLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxClearLastClearedTime.setStatus("current")


class _TmnxClearResult_Type(Integer32):
    """Custom type tmnxClearResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_TmnxClearResult_Type.__name__ = "Integer32"
_TmnxClearResult_Object = MibTableColumn
tmnxClearResult = _TmnxClearResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 6),
    _TmnxClearResult_Type()
)
tmnxClearResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxClearResult.setStatus("current")


class _TmnxClearErrorText_Type(OctetString):
    """Custom type tmnxClearErrorText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxClearErrorText_Type.__name__ = "OctetString"
_TmnxClearErrorText_Object = MibTableColumn
tmnxClearErrorText = _TmnxClearErrorText_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 13, 1, 1, 7),
    _TmnxClearErrorText_Type()
)
tmnxClearErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxClearErrorText.setStatus("current")
_TmnxClearNotificationsPrefix_ObjectIdentity = ObjectIdentity
tmnxClearNotificationsPrefix = _TmnxClearNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 13)
)
_TmnxClearNotifications_ObjectIdentity = ObjectIdentity
tmnxClearNotifications = _TmnxClearNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 13, 0)
)

# Managed Objects groups

tmnxClearGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13, 2, 1)
)
tmnxClearGroup.setObjects(
      *(("TIMETRA-CLEAR-MIB", "tmnxClearName"),
        ("TIMETRA-CLEAR-MIB", "tmnxClearParams"),
        ("TIMETRA-CLEAR-MIB", "tmnxClearAction"),
        ("TIMETRA-CLEAR-MIB", "tmnxClearLastClearedTime"),
        ("TIMETRA-CLEAR-MIB", "tmnxClearResult"),
        ("TIMETRA-CLEAR-MIB", "tmnxClearErrorText"))
)
if mibBuilder.loadTexts:
    tmnxClearGroup.setStatus("current")


# Notification objects

tmnxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 13, 0, 1)
)
tmnxClear.setObjects(
      *(("TIMETRA-CLEAR-MIB", "tmnxClearName"),
        ("TIMETRA-CLEAR-MIB", "tmnxClearParams"),
        ("TIMETRA-CLEAR-MIB", "tmnxClearLastClearedTime"),
        ("TIMETRA-CLEAR-MIB", "tmnxClearResult"),
        ("TIMETRA-CLEAR-MIB", "tmnxClearErrorText"))
)
if mibBuilder.loadTexts:
    tmnxClear.setStatus(
        "current"
    )


# Notifications groups

tmnxClearNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13, 2, 2)
)
tmnxClearNotificationGroup.setObjects(
    ("TIMETRA-CLEAR-MIB", "tmnxClear")
)
if mibBuilder.loadTexts:
    tmnxClearNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxClearCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxClearCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-CLEAR-MIB",
    **{"timetraClearMIBModule": timetraClearMIBModule,
       "tmnxClearConformance": tmnxClearConformance,
       "tmnxClearCompliances": tmnxClearCompliances,
       "tmnxClearCompliance": tmnxClearCompliance,
       "tmnxClearGroups": tmnxClearGroups,
       "tmnxClearGroup": tmnxClearGroup,
       "tmnxClearNotificationGroup": tmnxClearNotificationGroup,
       "tmnxClearObjs": tmnxClearObjs,
       "tmnxClearTable": tmnxClearTable,
       "tmnxClearEntry": tmnxClearEntry,
       "tmnxClearIndex": tmnxClearIndex,
       "tmnxClearName": tmnxClearName,
       "tmnxClearParams": tmnxClearParams,
       "tmnxClearAction": tmnxClearAction,
       "tmnxClearLastClearedTime": tmnxClearLastClearedTime,
       "tmnxClearResult": tmnxClearResult,
       "tmnxClearErrorText": tmnxClearErrorText,
       "tmnxClearNotificationsPrefix": tmnxClearNotificationsPrefix,
       "tmnxClearNotifications": tmnxClearNotifications,
       "tmnxClear": tmnxClear}
)

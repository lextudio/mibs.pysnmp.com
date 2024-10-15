# SNMP MIB module (JUNIPER-CFGMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-CFGMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:51 2024
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

(jnxCmNotifications,
 jnxMibs) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxCmNotifications",
    "jnxMibs")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxCfgMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18)
)
jnxCfgMgmt.setRevisions(
        ("2003-11-19 00:00",
         "2003-10-24 00:00",
         "2002-05-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxCmCfChgSource(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("autoinstall", 7),
          ("button", 6),
          ("cli", 2),
          ("junoscript", 3),
          ("other", 1),
          ("snmp", 5),
          ("synchronize", 4),
          ("unknown", 8))
    )



class JnxCmRescueCfgState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonexistant", 1),
          ("updated", 2))
    )



# MIB Managed Objects in the order of their OIDs

_JnxCmCfgChg_ObjectIdentity = ObjectIdentity
jnxCmCfgChg = _JnxCmCfgChg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1)
)


class _JnxCmCfgChgLatestIndex_Type(Integer32):
    """Custom type jnxCmCfgChgLatestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxCmCfgChgLatestIndex_Type.__name__ = "Integer32"
_JnxCmCfgChgLatestIndex_Object = MibScalar
jnxCmCfgChgLatestIndex = _JnxCmCfgChgLatestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 1),
    _JnxCmCfgChgLatestIndex_Type()
)
jnxCmCfgChgLatestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmCfgChgLatestIndex.setStatus("current")
_JnxCmCfgChgLatestTime_Type = TimeTicks
_JnxCmCfgChgLatestTime_Object = MibScalar
jnxCmCfgChgLatestTime = _JnxCmCfgChgLatestTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 2),
    _JnxCmCfgChgLatestTime_Type()
)
jnxCmCfgChgLatestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmCfgChgLatestTime.setStatus("current")
_JnxCmCfgChgLatestDate_Type = DateAndTime
_JnxCmCfgChgLatestDate_Object = MibScalar
jnxCmCfgChgLatestDate = _JnxCmCfgChgLatestDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 3),
    _JnxCmCfgChgLatestDate_Type()
)
jnxCmCfgChgLatestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmCfgChgLatestDate.setStatus("current")
_JnxCmCfgChgLatestSource_Type = JnxCmCfChgSource
_JnxCmCfgChgLatestSource_Object = MibScalar
jnxCmCfgChgLatestSource = _JnxCmCfgChgLatestSource_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 4),
    _JnxCmCfgChgLatestSource_Type()
)
jnxCmCfgChgLatestSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmCfgChgLatestSource.setStatus("current")
_JnxCmCfgChgLatestUser_Type = DisplayString
_JnxCmCfgChgLatestUser_Object = MibScalar
jnxCmCfgChgLatestUser = _JnxCmCfgChgLatestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 5),
    _JnxCmCfgChgLatestUser_Type()
)
jnxCmCfgChgLatestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmCfgChgLatestUser.setStatus("current")


class _JnxCmCfgChgMaxEventEntries_Type(Integer32):
    """Custom type jnxCmCfgChgMaxEventEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxCmCfgChgMaxEventEntries_Type.__name__ = "Integer32"
_JnxCmCfgChgMaxEventEntries_Object = MibScalar
jnxCmCfgChgMaxEventEntries = _JnxCmCfgChgMaxEventEntries_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 6),
    _JnxCmCfgChgMaxEventEntries_Type()
)
jnxCmCfgChgMaxEventEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmCfgChgMaxEventEntries.setStatus("current")
_JnxCmCfgChgEventTable_Object = MibTable
jnxCmCfgChgEventTable = _JnxCmCfgChgEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7)
)
if mibBuilder.loadTexts:
    jnxCmCfgChgEventTable.setStatus("current")
_JnxCmCfgChgEventEntry_Object = MibTableRow
jnxCmCfgChgEventEntry = _JnxCmCfgChgEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1)
)
jnxCmCfgChgEventEntry.setIndexNames(
    (0, "JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventIndex"),
)
if mibBuilder.loadTexts:
    jnxCmCfgChgEventEntry.setStatus("current")


class _JnxCmCfgChgEventIndex_Type(Integer32):
    """Custom type jnxCmCfgChgEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxCmCfgChgEventIndex_Type.__name__ = "Integer32"
_JnxCmCfgChgEventIndex_Object = MibTableColumn
jnxCmCfgChgEventIndex = _JnxCmCfgChgEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 1),
    _JnxCmCfgChgEventIndex_Type()
)
jnxCmCfgChgEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxCmCfgChgEventIndex.setStatus("current")
_JnxCmCfgChgEventTime_Type = TimeTicks
_JnxCmCfgChgEventTime_Object = MibTableColumn
jnxCmCfgChgEventTime = _JnxCmCfgChgEventTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 2),
    _JnxCmCfgChgEventTime_Type()
)
jnxCmCfgChgEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmCfgChgEventTime.setStatus("current")
_JnxCmCfgChgEventDate_Type = DateAndTime
_JnxCmCfgChgEventDate_Object = MibTableColumn
jnxCmCfgChgEventDate = _JnxCmCfgChgEventDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 3),
    _JnxCmCfgChgEventDate_Type()
)
jnxCmCfgChgEventDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmCfgChgEventDate.setStatus("current")
_JnxCmCfgChgEventSource_Type = JnxCmCfChgSource
_JnxCmCfgChgEventSource_Object = MibTableColumn
jnxCmCfgChgEventSource = _JnxCmCfgChgEventSource_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 4),
    _JnxCmCfgChgEventSource_Type()
)
jnxCmCfgChgEventSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmCfgChgEventSource.setStatus("current")
_JnxCmCfgChgEventUser_Type = DisplayString
_JnxCmCfgChgEventUser_Object = MibTableColumn
jnxCmCfgChgEventUser = _JnxCmCfgChgEventUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 5),
    _JnxCmCfgChgEventUser_Type()
)
jnxCmCfgChgEventUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmCfgChgEventUser.setStatus("current")
_JnxCmCfgChgEventLog_Type = DisplayString
_JnxCmCfgChgEventLog_Object = MibTableColumn
jnxCmCfgChgEventLog = _JnxCmCfgChgEventLog_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 6),
    _JnxCmCfgChgEventLog_Type()
)
jnxCmCfgChgEventLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmCfgChgEventLog.setStatus("current")
_JnxCmRescueChg_ObjectIdentity = ObjectIdentity
jnxCmRescueChg = _JnxCmRescueChg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 2)
)
_JnxCmRescueChgTime_Type = TimeTicks
_JnxCmRescueChgTime_Object = MibScalar
jnxCmRescueChgTime = _JnxCmRescueChgTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 2, 1),
    _JnxCmRescueChgTime_Type()
)
jnxCmRescueChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmRescueChgTime.setStatus("current")
_JnxCmRescueChgDate_Type = DateAndTime
_JnxCmRescueChgDate_Object = MibScalar
jnxCmRescueChgDate = _JnxCmRescueChgDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 2, 2),
    _JnxCmRescueChgDate_Type()
)
jnxCmRescueChgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmRescueChgDate.setStatus("current")
_JnxCmRescueChgSource_Type = JnxCmCfChgSource
_JnxCmRescueChgSource_Object = MibScalar
jnxCmRescueChgSource = _JnxCmRescueChgSource_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 2, 3),
    _JnxCmRescueChgSource_Type()
)
jnxCmRescueChgSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmRescueChgSource.setStatus("current")
_JnxCmRescueChgUser_Type = DisplayString
_JnxCmRescueChgUser_Object = MibScalar
jnxCmRescueChgUser = _JnxCmRescueChgUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 2, 4),
    _JnxCmRescueChgUser_Type()
)
jnxCmRescueChgUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmRescueChgUser.setStatus("current")
_JnxCmRescueChgState_Type = JnxCmRescueCfgState
_JnxCmRescueChgState_Object = MibScalar
jnxCmRescueChgState = _JnxCmRescueChgState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 18, 2, 5),
    _JnxCmRescueChgState_Type()
)
jnxCmRescueChgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCmRescueChgState.setStatus("current")
_JnxCmNotificationsPrefix_ObjectIdentity = ObjectIdentity
jnxCmNotificationsPrefix = _JnxCmNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 5, 0)
)

# Managed Objects groups


# Notification objects

jnxCmCfgChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 5, 0, 1)
)
jnxCmCfgChange.setObjects(
      *(("JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventTime"),
        ("JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventDate"),
        ("JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventSource"),
        ("JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventUser"),
        ("JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventLog"))
)
if mibBuilder.loadTexts:
    jnxCmCfgChange.setStatus(
        "current"
    )

jnxCmRescueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 5, 0, 2)
)
jnxCmRescueChange.setObjects(
      *(("JUNIPER-CFGMGMT-MIB", "jnxCmRescueChgTime"),
        ("JUNIPER-CFGMGMT-MIB", "jnxCmRescueChgDate"),
        ("JUNIPER-CFGMGMT-MIB", "jnxCmRescueChgSource"),
        ("JUNIPER-CFGMGMT-MIB", "jnxCmRescueChgUser"),
        ("JUNIPER-CFGMGMT-MIB", "jnxCmRescueChgState"))
)
if mibBuilder.loadTexts:
    jnxCmRescueChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-CFGMGMT-MIB",
    **{"JnxCmCfChgSource": JnxCmCfChgSource,
       "JnxCmRescueCfgState": JnxCmRescueCfgState,
       "jnxCfgMgmt": jnxCfgMgmt,
       "jnxCmCfgChg": jnxCmCfgChg,
       "jnxCmCfgChgLatestIndex": jnxCmCfgChgLatestIndex,
       "jnxCmCfgChgLatestTime": jnxCmCfgChgLatestTime,
       "jnxCmCfgChgLatestDate": jnxCmCfgChgLatestDate,
       "jnxCmCfgChgLatestSource": jnxCmCfgChgLatestSource,
       "jnxCmCfgChgLatestUser": jnxCmCfgChgLatestUser,
       "jnxCmCfgChgMaxEventEntries": jnxCmCfgChgMaxEventEntries,
       "jnxCmCfgChgEventTable": jnxCmCfgChgEventTable,
       "jnxCmCfgChgEventEntry": jnxCmCfgChgEventEntry,
       "jnxCmCfgChgEventIndex": jnxCmCfgChgEventIndex,
       "jnxCmCfgChgEventTime": jnxCmCfgChgEventTime,
       "jnxCmCfgChgEventDate": jnxCmCfgChgEventDate,
       "jnxCmCfgChgEventSource": jnxCmCfgChgEventSource,
       "jnxCmCfgChgEventUser": jnxCmCfgChgEventUser,
       "jnxCmCfgChgEventLog": jnxCmCfgChgEventLog,
       "jnxCmRescueChg": jnxCmRescueChg,
       "jnxCmRescueChgTime": jnxCmRescueChgTime,
       "jnxCmRescueChgDate": jnxCmRescueChgDate,
       "jnxCmRescueChgSource": jnxCmRescueChgSource,
       "jnxCmRescueChgUser": jnxCmRescueChgUser,
       "jnxCmRescueChgState": jnxCmRescueChgState,
       "jnxCmNotificationsPrefix": jnxCmNotificationsPrefix,
       "jnxCmCfgChange": jnxCmCfgChange,
       "jnxCmRescueChange": jnxCmRescueChange}
)

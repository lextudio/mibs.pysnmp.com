# SNMP MIB module (JUNIPER-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:15 2024
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(jnxMibs,
 jnxSonetNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs",
    "jnxSonetNotifications")

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

jnxSonet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20)
)
jnxSonet.setRevisions(
        ("2002-12-12 00:00",
         "2002-08-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxSonetAlarmId(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JnxSonetAlarms_ObjectIdentity = ObjectIdentity
jnxSonetAlarms = _JnxSonetAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1)
)
_JnxSonetAlarmTable_Object = MibTable
jnxSonetAlarmTable = _JnxSonetAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSonetAlarmTable.setStatus("current")
_JnxSonetAlarmEntry_Object = MibTableRow
jnxSonetAlarmEntry = _JnxSonetAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1)
)
jnxSonetAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxSonetAlarmEntry.setStatus("current")
_JnxSonetCurrentAlarms_Type = JnxSonetAlarmId
_JnxSonetCurrentAlarms_Object = MibTableColumn
jnxSonetCurrentAlarms = _JnxSonetCurrentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 1),
    _JnxSonetCurrentAlarms_Type()
)
jnxSonetCurrentAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSonetCurrentAlarms.setStatus("current")
_JnxSonetLastAlarmId_Type = JnxSonetAlarmId
_JnxSonetLastAlarmId_Object = MibTableColumn
jnxSonetLastAlarmId = _JnxSonetLastAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 2),
    _JnxSonetLastAlarmId_Type()
)
jnxSonetLastAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSonetLastAlarmId.setStatus("current")
_JnxSonetLastAlarmTime_Type = TimeTicks
_JnxSonetLastAlarmTime_Object = MibTableColumn
jnxSonetLastAlarmTime = _JnxSonetLastAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 3),
    _JnxSonetLastAlarmTime_Type()
)
jnxSonetLastAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSonetLastAlarmTime.setStatus("current")
_JnxSonetLastAlarmDate_Type = DateAndTime
_JnxSonetLastAlarmDate_Object = MibTableColumn
jnxSonetLastAlarmDate = _JnxSonetLastAlarmDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 4),
    _JnxSonetLastAlarmDate_Type()
)
jnxSonetLastAlarmDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSonetLastAlarmDate.setStatus("current")


class _JnxSonetLastAlarmEvent_Type(Integer32):
    """Custom type jnxSonetLastAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 3),
          ("none", 1),
          ("set", 2))
    )


_JnxSonetLastAlarmEvent_Type.__name__ = "Integer32"
_JnxSonetLastAlarmEvent_Object = MibTableColumn
jnxSonetLastAlarmEvent = _JnxSonetLastAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 5),
    _JnxSonetLastAlarmEvent_Type()
)
jnxSonetLastAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSonetLastAlarmEvent.setStatus("current")
_JnxSonetNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxSonetNotificationPrefix = _JnxSonetNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 6, 0)
)

# Managed Objects groups


# Notification objects

jnxSonetAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 6, 0, 1)
)
jnxSonetAlarmSet.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmId"),
        ("JUNIPER-SONET-MIB", "jnxSonetCurrentAlarms"),
        ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxSonetAlarmSet.setStatus(
        "current"
    )

jnxSonetAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 6, 0, 2)
)
jnxSonetAlarmCleared.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmId"),
        ("JUNIPER-SONET-MIB", "jnxSonetCurrentAlarms"),
        ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxSonetAlarmCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SONET-MIB",
    **{"JnxSonetAlarmId": JnxSonetAlarmId,
       "jnxSonet": jnxSonet,
       "jnxSonetAlarms": jnxSonetAlarms,
       "jnxSonetAlarmTable": jnxSonetAlarmTable,
       "jnxSonetAlarmEntry": jnxSonetAlarmEntry,
       "jnxSonetCurrentAlarms": jnxSonetCurrentAlarms,
       "jnxSonetLastAlarmId": jnxSonetLastAlarmId,
       "jnxSonetLastAlarmTime": jnxSonetLastAlarmTime,
       "jnxSonetLastAlarmDate": jnxSonetLastAlarmDate,
       "jnxSonetLastAlarmEvent": jnxSonetLastAlarmEvent,
       "jnxSonetNotificationPrefix": jnxSonetNotificationPrefix,
       "jnxSonetAlarmSet": jnxSonetAlarmSet,
       "jnxSonetAlarmCleared": jnxSonetAlarmCleared}
)

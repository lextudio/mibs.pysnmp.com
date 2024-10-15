# SNMP MIB module (NET-SNMP-PERIODIC-NOTIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NET-SNMP-PERIODIC-NOTIFY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:25 2024
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

(netSnmpModuleIDs,
 netSnmpNotifications,
 netSnmpObjects) = mibBuilder.importSymbols(
    "NET-SNMP-MIB",
    "netSnmpModuleIDs",
    "netSnmpNotifications",
    "netSnmpObjects")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

netSnmpPeriodicNotifyMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5)
)
netSnmpPeriodicNotifyMib.setRevisions(
        ("2011-04-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsPNScalars_ObjectIdentity = ObjectIdentity
nsPNScalars = _NsPNScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 1)
)
_NsPNTables_ObjectIdentity = ObjectIdentity
nsPNTables = _NsPNTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 2)
)
_NsPNotifyObjects_ObjectIdentity = ObjectIdentity
nsPNotifyObjects = _NsPNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3)
)
_NsPNPeriodicTime_Type = Unsigned32
_NsPNPeriodicTime_Object = MibScalar
nsPNPeriodicTime = _NsPNPeriodicTime_Object(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 1),
    _NsPNPeriodicTime_Type()
)
nsPNPeriodicTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsPNPeriodicTime.setStatus("current")
_NsPNotifyMessageNumber_Type = Unsigned32
_NsPNotifyMessageNumber_Object = MibScalar
nsPNotifyMessageNumber = _NsPNotifyMessageNumber_Object(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 2),
    _NsPNotifyMessageNumber_Type()
)
nsPNotifyMessageNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsPNotifyMessageNumber.setStatus("current")
_NsPNotifyMaxMessageNumber_Type = Unsigned32
_NsPNotifyMaxMessageNumber_Object = MibScalar
nsPNotifyMaxMessageNumber = _NsPNotifyMaxMessageNumber_Object(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 3),
    _NsPNotifyMaxMessageNumber_Type()
)
nsPNotifyMaxMessageNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nsPNotifyMaxMessageNumber.setStatus("current")
_NsPNotificationPrefix_ObjectIdentity = ObjectIdentity
nsPNotificationPrefix = _NsPNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4)
)
_NsPNotifications_ObjectIdentity = ObjectIdentity
nsPNotifications = _NsPNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 0)
)
_NsPNotificationObjects_ObjectIdentity = ObjectIdentity
nsPNotificationObjects = _NsPNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 1)
)

# Managed Objects groups


# Notification objects

nsNotifyPeriodicNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 0, 1)
)
if mibBuilder.loadTexts:
    nsNotifyPeriodicNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NET-SNMP-PERIODIC-NOTIFY-MIB",
    **{"netSnmpPeriodicNotifyMib": netSnmpPeriodicNotifyMib,
       "nsPNScalars": nsPNScalars,
       "nsPNTables": nsPNTables,
       "nsPNotifyObjects": nsPNotifyObjects,
       "nsPNPeriodicTime": nsPNPeriodicTime,
       "nsPNotifyMessageNumber": nsPNotifyMessageNumber,
       "nsPNotifyMaxMessageNumber": nsPNotifyMaxMessageNumber,
       "nsPNotificationPrefix": nsPNotificationPrefix,
       "nsPNotifications": nsPNotifications,
       "nsNotifyPeriodicNotification": nsNotifyPeriodicNotification,
       "nsPNotificationObjects": nsPNotificationObjects}
)

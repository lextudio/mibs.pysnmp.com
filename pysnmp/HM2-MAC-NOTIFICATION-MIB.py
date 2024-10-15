# SNMP MIB module (HM2-MAC-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-MAC-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:06 2024
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hm2MACNotificationMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 35)
)
hm2MACNotificationMib.setRevisions(
        ("2012-03-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2MACNotifyMibNotifications_ObjectIdentity = ObjectIdentity
hm2MACNotifyMibNotifications = _Hm2MACNotifyMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 35, 0)
)
_Hm2MACNotifyMibObjects_ObjectIdentity = ObjectIdentity
hm2MACNotifyMibObjects = _Hm2MACNotifyMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 35, 1)
)


class _Hm2MACNotifyAdminState_Type(HmEnabledStatus):
    """Custom type hm2MACNotifyAdminState based on HmEnabledStatus"""


_Hm2MACNotifyAdminState_Object = MibScalar
hm2MACNotifyAdminState = _Hm2MACNotifyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 35, 1, 1),
    _Hm2MACNotifyAdminState_Type()
)
hm2MACNotifyAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2MACNotifyAdminState.setStatus("current")


class _Hm2MACNotifyInterval_Type(Integer32):
    """Custom type hm2MACNotifyInterval based on Integer32"""
    defaultValue = 1


_Hm2MACNotifyInterval_Object = MibScalar
hm2MACNotifyInterval = _Hm2MACNotifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 35, 1, 2),
    _Hm2MACNotifyInterval_Type()
)
hm2MACNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2MACNotifyInterval.setStatus("current")
_Hm2MACNotifyInterfaceTable_Object = MibTable
hm2MACNotifyInterfaceTable = _Hm2MACNotifyInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 35, 1, 10)
)
if mibBuilder.loadTexts:
    hm2MACNotifyInterfaceTable.setStatus("current")
_Hm2MACNotifyInterfaceEntry_Object = MibTableRow
hm2MACNotifyInterfaceEntry = _Hm2MACNotifyInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 35, 1, 10, 1)
)
hm2MACNotifyInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2MACNotifyInterfaceEntry.setStatus("current")


class _Hm2MACNotifyInterfaceAdminState_Type(HmEnabledStatus):
    """Custom type hm2MACNotifyInterfaceAdminState based on HmEnabledStatus"""


_Hm2MACNotifyInterfaceAdminState_Object = MibTableColumn
hm2MACNotifyInterfaceAdminState = _Hm2MACNotifyInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 35, 1, 10, 1, 1),
    _Hm2MACNotifyInterfaceAdminState_Type()
)
hm2MACNotifyInterfaceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2MACNotifyInterfaceAdminState.setStatus("current")
_Hm2MACNotifyInterfaceMACAddr_Type = MacAddress
_Hm2MACNotifyInterfaceMACAddr_Object = MibTableColumn
hm2MACNotifyInterfaceMACAddr = _Hm2MACNotifyInterfaceMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 35, 1, 10, 1, 2),
    _Hm2MACNotifyInterfaceMACAddr_Type()
)
hm2MACNotifyInterfaceMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MACNotifyInterfaceMACAddr.setStatus("current")


class _Hm2MACNotifyInterfaceMACStatus_Type(Integer32):
    """Custom type hm2MACNotifyInterfaceMACStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("added", 2),
          ("other", 1),
          ("removed", 3))
    )


_Hm2MACNotifyInterfaceMACStatus_Type.__name__ = "Integer32"
_Hm2MACNotifyInterfaceMACStatus_Object = MibTableColumn
hm2MACNotifyInterfaceMACStatus = _Hm2MACNotifyInterfaceMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 35, 1, 10, 1, 3),
    _Hm2MACNotifyInterfaceMACStatus_Type()
)
hm2MACNotifyInterfaceMACStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MACNotifyInterfaceMACStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hm2MACNotificationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 35, 0, 1)
)
hm2MACNotificationTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HM2-MAC-NOTIFICATION-MIB", "hm2MACNotifyInterfaceMACAddr"),
        ("HM2-MAC-NOTIFICATION-MIB", "hm2MACNotifyInterfaceMACStatus"))
)
if mibBuilder.loadTexts:
    hm2MACNotificationTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-MAC-NOTIFICATION-MIB",
    **{"hm2MACNotificationMib": hm2MACNotificationMib,
       "hm2MACNotifyMibNotifications": hm2MACNotifyMibNotifications,
       "hm2MACNotificationTrap": hm2MACNotificationTrap,
       "hm2MACNotifyMibObjects": hm2MACNotifyMibObjects,
       "hm2MACNotifyAdminState": hm2MACNotifyAdminState,
       "hm2MACNotifyInterval": hm2MACNotifyInterval,
       "hm2MACNotifyInterfaceTable": hm2MACNotifyInterfaceTable,
       "hm2MACNotifyInterfaceEntry": hm2MACNotifyInterfaceEntry,
       "hm2MACNotifyInterfaceAdminState": hm2MACNotifyInterfaceAdminState,
       "hm2MACNotifyInterfaceMACAddr": hm2MACNotifyInterfaceMACAddr,
       "hm2MACNotifyInterfaceMACStatus": hm2MACNotifyInterfaceMACStatus}
)

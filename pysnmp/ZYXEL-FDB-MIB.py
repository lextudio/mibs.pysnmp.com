# SNMP MIB module (ZYXEL-FDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-FDB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:51 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelFdb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMacStatus_ObjectIdentity = ObjectIdentity
zyxelMacStatus = _ZyxelMacStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1)
)
_ZyMacFlush_Type = EnabledStatus
_ZyMacFlush_Object = MibScalar
zyMacFlush = _ZyMacFlush_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 1),
    _ZyMacFlush_Type()
)
zyMacFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacFlush.setStatus("current")
_ZyMacFlushPort_Type = Integer32
_ZyMacFlushPort_Object = MibScalar
zyMacFlushPort = _ZyMacFlushPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 2),
    _ZyMacFlushPort_Type()
)
zyMacFlushPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacFlushPort.setStatus("current")
_ZyMacFlushVlan_Type = Integer32
_ZyMacFlushVlan_Object = MibScalar
zyMacFlushVlan = _ZyMacFlushVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 3),
    _ZyMacFlushVlan_Type()
)
zyMacFlushVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacFlushVlan.setStatus("current")
_ZyxelMacStatusNotifications_ObjectIdentity = ObjectIdentity
zyxelMacStatusNotifications = _ZyxelMacStatusNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2)
)

# Managed Objects groups


# Notification objects

zyMacForwardingTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2, 1)
)
if mibBuilder.loadTexts:
    zyMacForwardingTableFull.setStatus(
        "current"
    )

zyMacForwardingTableFullRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2, 2)
)
if mibBuilder.loadTexts:
    zyMacForwardingTableFullRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-FDB-MIB",
    **{"zyxelFdb": zyxelFdb,
       "zyxelMacStatus": zyxelMacStatus,
       "zyMacFlush": zyMacFlush,
       "zyMacFlushPort": zyMacFlushPort,
       "zyMacFlushVlan": zyMacFlushVlan,
       "zyxelMacStatusNotifications": zyxelMacStatusNotifications,
       "zyMacForwardingTableFull": zyMacForwardingTableFull,
       "zyMacForwardingTableFullRecovered": zyMacForwardingTableFullRecovered}
)

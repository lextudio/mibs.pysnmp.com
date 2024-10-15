# SNMP MIB module (ZYXEL-STORM-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-STORM-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:50 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

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

zyxelStormControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelStormControlSetup_ObjectIdentity = ObjectIdentity
zyxelStormControlSetup = _ZyxelStormControlSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1)
)
_ZyStromControlState_Type = EnabledStatus
_ZyStromControlState_Object = MibScalar
zyStromControlState = _ZyStromControlState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 1),
    _ZyStromControlState_Type()
)
zyStromControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlState.setStatus("current")
_ZyxelStromControlPortTable_Object = MibTable
zyxelStromControlPortTable = _ZyxelStromControlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelStromControlPortTable.setStatus("current")
_ZyxelStromControlPortEntry_Object = MibTableRow
zyxelStromControlPortEntry = _ZyxelStromControlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1)
)
zyxelStromControlPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelStromControlPortEntry.setStatus("current")
_ZyStromControlPortBroadcastState_Type = EnabledStatus
_ZyStromControlPortBroadcastState_Object = MibTableColumn
zyStromControlPortBroadcastState = _ZyStromControlPortBroadcastState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 1),
    _ZyStromControlPortBroadcastState_Type()
)
zyStromControlPortBroadcastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortBroadcastState.setStatus("current")
_ZyStromControlPortBroadcastRate_Type = Integer32
_ZyStromControlPortBroadcastRate_Object = MibTableColumn
zyStromControlPortBroadcastRate = _ZyStromControlPortBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 2),
    _ZyStromControlPortBroadcastRate_Type()
)
zyStromControlPortBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortBroadcastRate.setStatus("current")
_ZyStromControlPortMulticastState_Type = EnabledStatus
_ZyStromControlPortMulticastState_Object = MibTableColumn
zyStromControlPortMulticastState = _ZyStromControlPortMulticastState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 3),
    _ZyStromControlPortMulticastState_Type()
)
zyStromControlPortMulticastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortMulticastState.setStatus("current")
_ZyStromControlPortMulticastRate_Type = Integer32
_ZyStromControlPortMulticastRate_Object = MibTableColumn
zyStromControlPortMulticastRate = _ZyStromControlPortMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 4),
    _ZyStromControlPortMulticastRate_Type()
)
zyStromControlPortMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortMulticastRate.setStatus("current")
_ZyStromControlPortDlfState_Type = EnabledStatus
_ZyStromControlPortDlfState_Object = MibTableColumn
zyStromControlPortDlfState = _ZyStromControlPortDlfState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 5),
    _ZyStromControlPortDlfState_Type()
)
zyStromControlPortDlfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortDlfState.setStatus("current")
_ZyStromControlPortDlfRate_Type = Integer32
_ZyStromControlPortDlfRate_Object = MibTableColumn
zyStromControlPortDlfRate = _ZyStromControlPortDlfRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 78, 1, 2, 1, 6),
    _ZyStromControlPortDlfRate_Type()
)
zyStromControlPortDlfRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStromControlPortDlfRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-STORM-CONTROL-MIB",
    **{"zyxelStormControl": zyxelStormControl,
       "zyxelStormControlSetup": zyxelStormControlSetup,
       "zyStromControlState": zyStromControlState,
       "zyxelStromControlPortTable": zyxelStromControlPortTable,
       "zyxelStromControlPortEntry": zyxelStromControlPortEntry,
       "zyStromControlPortBroadcastState": zyStromControlPortBroadcastState,
       "zyStromControlPortBroadcastRate": zyStromControlPortBroadcastRate,
       "zyStromControlPortMulticastState": zyStromControlPortMulticastState,
       "zyStromControlPortMulticastRate": zyStromControlPortMulticastRate,
       "zyStromControlPortDlfState": zyStromControlPortDlfState,
       "zyStromControlPortDlfRate": zyStromControlPortDlfRate}
)

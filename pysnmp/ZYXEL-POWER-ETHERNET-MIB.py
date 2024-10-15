# SNMP MIB module (ZYXEL-POWER-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-POWER-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:37 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelPoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelPoeSetup_ObjectIdentity = ObjectIdentity
zyxelPoeSetup = _ZyxelPoeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1)
)


class _ZyPoeMode_Type(Integer32):
    """Custom type zyPoeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("classification", 1),
          ("consumption", 0))
    )


_ZyPoeMode_Type.__name__ = "Integer32"
_ZyPoeMode_Object = MibScalar
zyPoeMode = _ZyPoeMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 1),
    _ZyPoeMode_Type()
)
zyPoeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPoeMode.setStatus("current")
_ZyxelPoePsePortTable_Object = MibTable
zyxelPoePsePortTable = _ZyxelPoePsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelPoePsePortTable.setStatus("current")
_ZyxelPoePsePortEntry_Object = MibTableRow
zyxelPoePsePortEntry = _ZyxelPoePsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2, 1)
)
zyxelPoePsePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelPoePsePortEntry.setStatus("current")
_ZyPoePsePortMaxPower_Type = Integer32
_ZyPoePsePortMaxPower_Object = MibTableColumn
zyPoePsePortMaxPower = _ZyPoePsePortMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2, 1, 1),
    _ZyPoePsePortMaxPower_Type()
)
zyPoePsePortMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPoePsePortMaxPower.setStatus("current")
_ZyxelPoeStatus_ObjectIdentity = ObjectIdentity
zyxelPoeStatus = _ZyxelPoeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2)
)
_ZyxelPoePsePortInfoTable_Object = MibTable
zyxelPoePsePortInfoTable = _ZyxelPoePsePortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelPoePsePortInfoTable.setStatus("current")
_ZyxelPoePsePortInfoEntry_Object = MibTableRow
zyxelPoePsePortInfoEntry = _ZyxelPoePsePortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2, 1, 1)
)
zyxelPoePsePortInfoEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelPoePsePortInfoEntry.setStatus("current")
_ZyPoePsePortInfoPowerConsumption_Type = Integer32
_ZyPoePsePortInfoPowerConsumption_Object = MibTableColumn
zyPoePsePortInfoPowerConsumption = _ZyPoePsePortInfoPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2, 1, 1, 1),
    _ZyPoePsePortInfoPowerConsumption_Type()
)
zyPoePsePortInfoPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPoePsePortInfoPowerConsumption.setStatus("current")
_ZyxelPoeTrapInfoObject_ObjectIdentity = ObjectIdentity
zyxelPoeTrapInfoObject = _ZyxelPoeTrapInfoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 3)
)


class _ZyPoeTrapPsePowerSupplyFailedReason_Type(Integer32):
    """Custom type zyPoeTrapPsePowerSupplyFailedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalPowerSupplyForPoeFailed", 0),
          ("rpsFanFailed", 2),
          ("rpsForPoeFailed", 1),
          ("rpsOverTemperature", 3))
    )


_ZyPoeTrapPsePowerSupplyFailedReason_Type.__name__ = "Integer32"
_ZyPoeTrapPsePowerSupplyFailedReason_Object = MibScalar
zyPoeTrapPsePowerSupplyFailedReason = _ZyPoeTrapPsePowerSupplyFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 3, 1),
    _ZyPoeTrapPsePowerSupplyFailedReason_Type()
)
zyPoeTrapPsePowerSupplyFailedReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPoeTrapPsePowerSupplyFailedReason.setStatus("current")
_ZyxelPoeNotifications_ObjectIdentity = ObjectIdentity
zyxelPoeNotifications = _ZyxelPoeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4)
)

# Managed Objects groups


# Notification objects

zyPoePowerPortOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 1)
)
zyPoePowerPortOverload.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortOverload.setStatus(
        "current"
    )

zyPoePowerPortShortCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 2)
)
zyPoePowerPortShortCircuit.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortShortCircuit.setStatus(
        "current"
    )

zyPoePowerPortOverSystemBudget = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 3)
)
zyPoePowerPortOverSystemBudget.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortOverSystemBudget.setStatus(
        "current"
    )

zyPoePsePowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 4)
)
zyPoePsePowerSupplyFailed.setObjects(
    ("ZYXEL-POWER-ETHERNET-MIB", "zyPoeTrapPsePowerSupplyFailedReason")
)
if mibBuilder.loadTexts:
    zyPoePsePowerSupplyFailed.setStatus(
        "current"
    )

zyPoePowerPortOverloadRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 5)
)
zyPoePowerPortOverloadRecovered.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortOverloadRecovered.setStatus(
        "current"
    )

zyPoePowerPortShortCircuitRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 6)
)
zyPoePowerPortShortCircuitRecovered.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortShortCircuitRecovered.setStatus(
        "current"
    )

zyPoePowerPortOverSystemBudgetRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 7)
)
zyPoePowerPortOverSystemBudgetRecovered.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zyPoePowerPortOverSystemBudgetRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-POWER-ETHERNET-MIB",
    **{"zyxelPoe": zyxelPoe,
       "zyxelPoeSetup": zyxelPoeSetup,
       "zyPoeMode": zyPoeMode,
       "zyxelPoePsePortTable": zyxelPoePsePortTable,
       "zyxelPoePsePortEntry": zyxelPoePsePortEntry,
       "zyPoePsePortMaxPower": zyPoePsePortMaxPower,
       "zyxelPoeStatus": zyxelPoeStatus,
       "zyxelPoePsePortInfoTable": zyxelPoePsePortInfoTable,
       "zyxelPoePsePortInfoEntry": zyxelPoePsePortInfoEntry,
       "zyPoePsePortInfoPowerConsumption": zyPoePsePortInfoPowerConsumption,
       "zyxelPoeTrapInfoObject": zyxelPoeTrapInfoObject,
       "zyPoeTrapPsePowerSupplyFailedReason": zyPoeTrapPsePowerSupplyFailedReason,
       "zyxelPoeNotifications": zyxelPoeNotifications,
       "zyPoePowerPortOverload": zyPoePowerPortOverload,
       "zyPoePowerPortShortCircuit": zyPoePowerPortShortCircuit,
       "zyPoePowerPortOverSystemBudget": zyPoePowerPortOverSystemBudget,
       "zyPoePsePowerSupplyFailed": zyPoePsePowerSupplyFailed,
       "zyPoePowerPortOverloadRecovered": zyPoePowerPortOverloadRecovered,
       "zyPoePowerPortShortCircuitRecovered": zyPoePowerPortShortCircuitRecovered,
       "zyPoePowerPortOverSystemBudgetRecovered": zyPoePowerPortOverSystemBudgetRecovered}
)

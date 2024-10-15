# SNMP MIB module (ELTEX-MES-LINKAGG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-LINKAGG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:53 2024
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

(eltMesLinkAgg,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesLinkAgg")

(dot3adAggPortEntry,) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "dot3adAggPortEntry")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(rlDot3adAggBalanceEntry,) = mibBuilder.importSymbols(
    "RADLAN-TRUNK-MIB",
    "rlDot3adAggBalanceEntry")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesLagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesLagMIBObjects_ObjectIdentity = ObjectIdentity
eltMesLagMIBObjects = _EltMesLagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1)
)
_EltMesLinkAggGlobal_ObjectIdentity = ObjectIdentity
eltMesLinkAggGlobal = _EltMesLinkAggGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 1)
)
_EltMesLinkAggPort_ObjectIdentity = ObjectIdentity
eltMesLinkAggPort = _EltMesLinkAggPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2)
)
_EltAggPortTable_Object = MibTable
eltAggPortTable = _EltAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltAggPortTable.setStatus("current")
_EltAggPortEntry_Object = MibTableRow
eltAggPortEntry = _EltAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltAggPortEntry.setStatus("current")
_EltAggPortPassive_Type = TruthValue
_EltAggPortPassive_Object = MibTableColumn
eltAggPortPassive = _EltAggPortPassive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 1, 1, 1),
    _EltAggPortPassive_Type()
)
eltAggPortPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltAggPortPassive.setStatus("current")
_EltAggBalanceTable_Object = MibTable
eltAggBalanceTable = _EltAggBalanceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eltAggBalanceTable.setStatus("current")
_EltAggBalanceEntry_Object = MibTableRow
eltAggBalanceEntry = _EltAggBalanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    eltAggBalanceEntry.setStatus("current")


class _EltAggBalanceMplsAware_Type(TruthValue):
    """Custom type eltAggBalanceMplsAware based on TruthValue"""


_EltAggBalanceMplsAware_Object = MibTableColumn
eltAggBalanceMplsAware = _EltAggBalanceMplsAware_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 9, 1, 1, 2, 2, 1, 1),
    _EltAggBalanceMplsAware_Type()
)
eltAggBalanceMplsAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltAggBalanceMplsAware.setStatus("current")
dot3adAggPortEntry.registerAugmentions(
    ("ELTEX-MES-LINKAGG-MIB",
     "eltAggPortEntry")
)
eltAggPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
rlDot3adAggBalanceEntry.registerAugmentions(
    ("ELTEX-MES-LINKAGG-MIB",
     "eltAggBalanceEntry")
)
eltAggBalanceEntry.setIndexNames(*rlDot3adAggBalanceEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-LINKAGG-MIB",
    **{"eltMesLagMIB": eltMesLagMIB,
       "eltMesLagMIBObjects": eltMesLagMIBObjects,
       "eltMesLinkAggGlobal": eltMesLinkAggGlobal,
       "eltMesLinkAggPort": eltMesLinkAggPort,
       "eltAggPortTable": eltAggPortTable,
       "eltAggPortEntry": eltAggPortEntry,
       "eltAggPortPassive": eltAggPortPassive,
       "eltAggBalanceTable": eltAggBalanceTable,
       "eltAggBalanceEntry": eltAggBalanceEntry,
       "eltAggBalanceMplsAware": eltAggBalanceMplsAware}
)

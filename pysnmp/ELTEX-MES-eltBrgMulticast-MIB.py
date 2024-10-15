# SNMP MIB module (ELTEX-MES-eltBrgMulticast-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-eltBrgMulticast-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:09 2024
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

(eltMesMacMulticast,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesMacMulticast")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

(rlIgmpMldSnoopVlanEntry,) = mibBuilder.importSymbols(
    "RADLAN-rlMacMulticast-MIB",
    "rlIgmpMldSnoopVlanEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesMldSnoop_ObjectIdentity = ObjectIdentity
eltMesMldSnoop = _EltMesMldSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5)
)
_EltIgmpMldSnoopVlanTable_Object = MibTable
eltIgmpMldSnoopVlanTable = _EltIgmpMldSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5)
)
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanTable.setStatus("current")
_EltIgmpMldSnoopVlanEntry_Object = MibTableRow
eltIgmpMldSnoopVlanEntry = _EltIgmpMldSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1)
)
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanEntry.setStatus("current")


class _EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Type(TruthValue):
    """Custom type eltIgmpMldSnoopVlanIsImmediateLeaveHostBased based on TruthValue"""


_EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Object = MibTableColumn
eltIgmpMldSnoopVlanIsImmediateLeaveHostBased = _EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1, 1),
    _EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Type()
)
eltIgmpMldSnoopVlanIsImmediateLeaveHostBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanIsImmediateLeaveHostBased.setStatus("current")


class _EltIgmpMldSnoopVlanCos_Type(Integer32):
    """Custom type eltIgmpMldSnoopVlanCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_EltIgmpMldSnoopVlanCos_Type.__name__ = "Integer32"
_EltIgmpMldSnoopVlanCos_Object = MibTableColumn
eltIgmpMldSnoopVlanCos = _EltIgmpMldSnoopVlanCos_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1, 2),
    _EltIgmpMldSnoopVlanCos_Type()
)
eltIgmpMldSnoopVlanCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanCos.setStatus("current")
_EltIgmpMldSnoopVlanReplaceSourceIp_Type = InetAddress
_EltIgmpMldSnoopVlanReplaceSourceIp_Object = MibTableColumn
eltIgmpMldSnoopVlanReplaceSourceIp = _EltIgmpMldSnoopVlanReplaceSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 55, 5, 5, 1, 3),
    _EltIgmpMldSnoopVlanReplaceSourceIp_Type()
)
eltIgmpMldSnoopVlanReplaceSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIgmpMldSnoopVlanReplaceSourceIp.setStatus("current")
rlIgmpMldSnoopVlanEntry.registerAugmentions(
    ("ELTEX-MES-eltBrgMulticast-MIB",
     "eltIgmpMldSnoopVlanEntry")
)
eltIgmpMldSnoopVlanEntry.setIndexNames(*rlIgmpMldSnoopVlanEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-eltBrgMulticast-MIB",
    **{"eltMesMldSnoop": eltMesMldSnoop,
       "eltIgmpMldSnoopVlanTable": eltIgmpMldSnoopVlanTable,
       "eltIgmpMldSnoopVlanEntry": eltIgmpMldSnoopVlanEntry,
       "eltIgmpMldSnoopVlanIsImmediateLeaveHostBased": eltIgmpMldSnoopVlanIsImmediateLeaveHostBased,
       "eltIgmpMldSnoopVlanCos": eltIgmpMldSnoopVlanCos,
       "eltIgmpMldSnoopVlanReplaceSourceIp": eltIgmpMldSnoopVlanReplaceSourceIp}
)

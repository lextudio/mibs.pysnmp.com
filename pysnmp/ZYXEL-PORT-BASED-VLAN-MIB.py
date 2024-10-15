# SNMP MIB module (ZYXEL-PORT-BASED-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-PORT-BASED-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:33 2024
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

zyxelPortBasedVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelPortBasedVlanSetup_ObjectIdentity = ObjectIdentity
zyxelPortBasedVlanSetup = _ZyxelPortBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1)
)
_ZyxelPortBasedVlanTable_Object = MibTable
zyxelPortBasedVlanTable = _ZyxelPortBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelPortBasedVlanTable.setStatus("current")
_ZyxelPortBasedVlanEntry_Object = MibTableRow
zyxelPortBasedVlanEntry = _ZyxelPortBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1, 1, 1)
)
zyxelPortBasedVlanEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelPortBasedVlanEntry.setStatus("current")
_ZyPortBasedVlanPorts_Type = PortList
_ZyPortBasedVlanPorts_Object = MibTableColumn
zyPortBasedVlanPorts = _ZyPortBasedVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 63, 1, 1, 1, 1),
    _ZyPortBasedVlanPorts_Type()
)
zyPortBasedVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortBasedVlanPorts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-PORT-BASED-VLAN-MIB",
    **{"zyxelPortBasedVlan": zyxelPortBasedVlan,
       "zyxelPortBasedVlanSetup": zyxelPortBasedVlanSetup,
       "zyxelPortBasedVlanTable": zyxelPortBasedVlanTable,
       "zyxelPortBasedVlanEntry": zyxelPortBasedVlanEntry,
       "zyPortBasedVlanPorts": zyPortBasedVlanPorts}
)

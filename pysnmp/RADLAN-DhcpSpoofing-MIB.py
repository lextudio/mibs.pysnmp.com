# SNMP MIB module (RADLAN-DhcpSpoofing-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-DhcpSpoofing-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:14 2024
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

(PortList,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "dot1qVlanIndex")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlDhcpSpoofing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 113)
)
rlDhcpSpoofing.setRevisions(
        ("2006-05-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDhcpSpoofingServerPorts_Type = PortList
_RlDhcpSpoofingServerPorts_Object = MibScalar
rlDhcpSpoofingServerPorts = _RlDhcpSpoofingServerPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 113, 1),
    _RlDhcpSpoofingServerPorts_Type()
)
rlDhcpSpoofingServerPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSpoofingServerPorts.setStatus("current")
_RlDhcpSpoofingVlanTable_Object = MibTable
rlDhcpSpoofingVlanTable = _RlDhcpSpoofingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 113, 2)
)
if mibBuilder.loadTexts:
    rlDhcpSpoofingVlanTable.setStatus("current")
_RlDhcpSpoofingVlanEntry_Object = MibTableRow
rlDhcpSpoofingVlanEntry = _RlDhcpSpoofingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 113, 2, 1)
)
rlDhcpSpoofingVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpSpoofingVlanEntry.setStatus("current")
_RlDhcpSpoofingEnabled_Type = TruthValue
_RlDhcpSpoofingEnabled_Object = MibTableColumn
rlDhcpSpoofingEnabled = _RlDhcpSpoofingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 113, 2, 1, 1),
    _RlDhcpSpoofingEnabled_Type()
)
rlDhcpSpoofingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSpoofingEnabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-DhcpSpoofing-MIB",
    **{"rlDhcpSpoofing": rlDhcpSpoofing,
       "rlDhcpSpoofingServerPorts": rlDhcpSpoofingServerPorts,
       "rlDhcpSpoofingVlanTable": rlDhcpSpoofingVlanTable,
       "rlDhcpSpoofingVlanEntry": rlDhcpSpoofingVlanEntry,
       "rlDhcpSpoofingEnabled": rlDhcpSpoofingEnabled}
)

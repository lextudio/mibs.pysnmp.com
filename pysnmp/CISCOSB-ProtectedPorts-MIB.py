# SNMP MIB module (CISCOSB-ProtectedPorts-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-ProtectedPorts-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:41 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlProtectedPorts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132)
)
rlProtectedPorts.setRevisions(
        ("2008-05-03 12:34",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlProtectedPortsTable_Object = MibTable
rlProtectedPortsTable = _RlProtectedPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1)
)
if mibBuilder.loadTexts:
    rlProtectedPortsTable.setStatus("current")
_RlProtectedPortsEntry_Object = MibTableRow
rlProtectedPortsEntry = _RlProtectedPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1, 1)
)
rlProtectedPortsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlProtectedPortsEntry.setStatus("current")


class _RlProtectedPortType_Type(Integer32):
    """Custom type rlProtectedPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-protected", 1),
          ("protected", 2))
    )


_RlProtectedPortType_Type.__name__ = "Integer32"
_RlProtectedPortType_Object = MibTableColumn
rlProtectedPortType = _RlProtectedPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1, 1, 1),
    _RlProtectedPortType_Type()
)
rlProtectedPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlProtectedPortType.setStatus("current")


class _RlProtectedPortCommunity_Type(Integer32):
    """Custom type rlProtectedPortCommunity based on Integer32"""
    defaultValue = 0


_RlProtectedPortCommunity_Object = MibTableColumn
rlProtectedPortCommunity = _RlProtectedPortCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 1, 1, 2),
    _RlProtectedPortCommunity_Type()
)
rlProtectedPortCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlProtectedPortCommunity.setStatus("current")
_RlProtectedPortsStatusTable_Object = MibTable
rlProtectedPortsStatusTable = _RlProtectedPortsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 2)
)
if mibBuilder.loadTexts:
    rlProtectedPortsStatusTable.setStatus("current")
_RlProtectedPortsStatusEntry_Object = MibTableRow
rlProtectedPortsStatusEntry = _RlProtectedPortsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 2, 1)
)
rlProtectedPortsStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlProtectedPortsStatusEntry.setStatus("current")
_RlProtectedPortEgressPorts_Type = PortList
_RlProtectedPortEgressPorts_Object = MibTableColumn
rlProtectedPortEgressPorts = _RlProtectedPortEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 2, 1, 1),
    _RlProtectedPortEgressPorts_Type()
)
rlProtectedPortEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlProtectedPortEgressPorts.setStatus("current")


class _RlProtectedPortsGlobalEnable_Type(TruthValue):
    """Custom type rlProtectedPortsGlobalEnable based on TruthValue"""


_RlProtectedPortsGlobalEnable_Object = MibScalar
rlProtectedPortsGlobalEnable = _RlProtectedPortsGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132, 3),
    _RlProtectedPortsGlobalEnable_Type()
)
rlProtectedPortsGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlProtectedPortsGlobalEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-ProtectedPorts-MIB",
    **{"rlProtectedPorts": rlProtectedPorts,
       "rlProtectedPortsTable": rlProtectedPortsTable,
       "rlProtectedPortsEntry": rlProtectedPortsEntry,
       "rlProtectedPortType": rlProtectedPortType,
       "rlProtectedPortCommunity": rlProtectedPortCommunity,
       "rlProtectedPortsStatusTable": rlProtectedPortsStatusTable,
       "rlProtectedPortsStatusEntry": rlProtectedPortsStatusEntry,
       "rlProtectedPortEgressPorts": rlProtectedPortEgressPorts,
       "rlProtectedPortsGlobalEnable": rlProtectedPortsGlobalEnable}
)

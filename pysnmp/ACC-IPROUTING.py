# SNMP MIB module (ACC-IPROUTING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-IPROUTING
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:24 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccIpRoutingTable_Object = MibTable
accIpRoutingTable = _AccIpRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    accIpRoutingTable.setStatus("mandatory")
_AccIpRoutingEntry_Object = MibTableRow
accIpRoutingEntry = _AccIpRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 12, 1)
)
accIpRoutingEntry.setIndexNames(
    (0, "ACC-IPROUTING", "ipRouteDest"),
)
if mibBuilder.loadTexts:
    accIpRoutingEntry.setStatus("mandatory")
_AccIpRouteDestSubnet_Type = IpAddress
_AccIpRouteDestSubnet_Object = MibTableColumn
accIpRouteDestSubnet = _AccIpRouteDestSubnet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 12, 1, 2),
    _AccIpRouteDestSubnet_Type()
)
accIpRouteDestSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpRouteDestSubnet.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-IPROUTING",
    **{"accIpRoutingTable": accIpRoutingTable,
       "accIpRoutingEntry": accIpRoutingEntry,
       "accIpRouteDestSubnet": accIpRouteDestSubnet}
)
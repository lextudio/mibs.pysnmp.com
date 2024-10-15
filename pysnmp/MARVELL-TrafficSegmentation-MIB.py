# SNMP MIB module (MARVELL-TrafficSegmentation-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MARVELL-TrafficSegmentation-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:27 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlTrafficSeg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 138)
)
rlTrafficSeg.setRevisions(
        ("2008-05-03 12:34",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlTrafficSegConfigTable_Object = MibTable
rlTrafficSegConfigTable = _RlTrafficSegConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 1)
)
if mibBuilder.loadTexts:
    rlTrafficSegConfigTable.setStatus("current")
_RlTrafficSegConfigEntry_Object = MibTableRow
rlTrafficSegConfigEntry = _RlTrafficSegConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 1, 1)
)
rlTrafficSegConfigEntry.setIndexNames(
    (0, "MARVELL-TrafficSegmentation-MIB", "rlTrafficSegConfigIndex"),
)
if mibBuilder.loadTexts:
    rlTrafficSegConfigEntry.setStatus("current")


class _RlTrafficSegConfigIndex_Type(Unsigned32):
    """Custom type rlTrafficSegConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlTrafficSegConfigIndex_Type.__name__ = "Unsigned32"
_RlTrafficSegConfigIndex_Object = MibTableColumn
rlTrafficSegConfigIndex = _RlTrafficSegConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 1, 1, 1),
    _RlTrafficSegConfigIndex_Type()
)
rlTrafficSegConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTrafficSegConfigIndex.setStatus("current")
_RlTrafficSegConfigIngressPorts_Type = PortList
_RlTrafficSegConfigIngressPorts_Object = MibTableColumn
rlTrafficSegConfigIngressPorts = _RlTrafficSegConfigIngressPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 1, 1, 2),
    _RlTrafficSegConfigIngressPorts_Type()
)
rlTrafficSegConfigIngressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTrafficSegConfigIngressPorts.setStatus("current")
_RlTrafficSegConfigEgressPorts_Type = PortList
_RlTrafficSegConfigEgressPorts_Object = MibTableColumn
rlTrafficSegConfigEgressPorts = _RlTrafficSegConfigEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 1, 1, 3),
    _RlTrafficSegConfigEgressPorts_Type()
)
rlTrafficSegConfigEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTrafficSegConfigEgressPorts.setStatus("current")
_RlTrafficSegConfigRowStatus_Type = RowStatus
_RlTrafficSegConfigRowStatus_Object = MibTableColumn
rlTrafficSegConfigRowStatus = _RlTrafficSegConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 1, 1, 4),
    _RlTrafficSegConfigRowStatus_Type()
)
rlTrafficSegConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlTrafficSegConfigRowStatus.setStatus("current")
_RlTrafficSegTable_Object = MibTable
rlTrafficSegTable = _RlTrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 2)
)
if mibBuilder.loadTexts:
    rlTrafficSegTable.setStatus("current")
_RlTrafficSegEntry_Object = MibTableRow
rlTrafficSegEntry = _RlTrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 2, 1)
)
rlTrafficSegEntry.setIndexNames(
    (0, "MARVELL-TrafficSegmentation-MIB", "rlTrafficSegIndex"),
)
if mibBuilder.loadTexts:
    rlTrafficSegEntry.setStatus("current")


class _RlTrafficSegIndex_Type(Unsigned32):
    """Custom type rlTrafficSegIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlTrafficSegIndex_Type.__name__ = "Unsigned32"
_RlTrafficSegIndex_Object = MibTableColumn
rlTrafficSegIndex = _RlTrafficSegIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 2, 1, 1),
    _RlTrafficSegIndex_Type()
)
rlTrafficSegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTrafficSegIndex.setStatus("current")
_RlTrafficSegIngressPorts_Type = PortList
_RlTrafficSegIngressPorts_Object = MibTableColumn
rlTrafficSegIngressPorts = _RlTrafficSegIngressPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 2, 1, 2),
    _RlTrafficSegIngressPorts_Type()
)
rlTrafficSegIngressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTrafficSegIngressPorts.setStatus("current")
_RlTrafficSegEgressPorts_Type = PortList
_RlTrafficSegEgressPorts_Object = MibTableColumn
rlTrafficSegEgressPorts = _RlTrafficSegEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 2, 1, 3),
    _RlTrafficSegEgressPorts_Type()
)
rlTrafficSegEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTrafficSegEgressPorts.setStatus("current")
_RlTrafficSegRowStatus_Type = RowStatus
_RlTrafficSegRowStatus_Object = MibTableColumn
rlTrafficSegRowStatus = _RlTrafficSegRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 138, 2, 1, 4),
    _RlTrafficSegRowStatus_Type()
)
rlTrafficSegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlTrafficSegRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MARVELL-TrafficSegmentation-MIB",
    **{"rlTrafficSeg": rlTrafficSeg,
       "rlTrafficSegConfigTable": rlTrafficSegConfigTable,
       "rlTrafficSegConfigEntry": rlTrafficSegConfigEntry,
       "rlTrafficSegConfigIndex": rlTrafficSegConfigIndex,
       "rlTrafficSegConfigIngressPorts": rlTrafficSegConfigIngressPorts,
       "rlTrafficSegConfigEgressPorts": rlTrafficSegConfigEgressPorts,
       "rlTrafficSegConfigRowStatus": rlTrafficSegConfigRowStatus,
       "rlTrafficSegTable": rlTrafficSegTable,
       "rlTrafficSegEntry": rlTrafficSegEntry,
       "rlTrafficSegIndex": rlTrafficSegIndex,
       "rlTrafficSegIngressPorts": rlTrafficSegIngressPorts,
       "rlTrafficSegEgressPorts": rlTrafficSegEgressPorts,
       "rlTrafficSegRowStatus": rlTrafficSegRowStatus}
)

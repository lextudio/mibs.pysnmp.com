# SNMP MIB module (H3C-UNICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-UNICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:36 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cUnicast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 44)
)
h3cUnicast.setRevisions(
        ("2005-03-24 14:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cURPFTable_Object = MibTable
h3cURPFTable = _H3cURPFTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 44, 1)
)
if mibBuilder.loadTexts:
    h3cURPFTable.setStatus("current")
_H3cURPFEntry_Object = MibTableRow
h3cURPFEntry = _H3cURPFEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 44, 1, 1)
)
h3cURPFEntry.setIndexNames(
    (0, "H3C-UNICAST-MIB", "h3cURPFIfIndex"),
)
if mibBuilder.loadTexts:
    h3cURPFEntry.setStatus("current")
_H3cURPFIfIndex_Type = Integer32
_H3cURPFIfIndex_Object = MibTableColumn
h3cURPFIfIndex = _H3cURPFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 44, 1, 1, 1),
    _H3cURPFIfIndex_Type()
)
h3cURPFIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cURPFIfIndex.setStatus("current")


class _H3cURPFEnabled_Type(TruthValue):
    """Custom type h3cURPFEnabled based on TruthValue"""


_H3cURPFEnabled_Object = MibTableColumn
h3cURPFEnabled = _H3cURPFEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 44, 1, 1, 2),
    _H3cURPFEnabled_Type()
)
h3cURPFEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cURPFEnabled.setStatus("current")
_H3cURPFSlotID_Type = Integer32
_H3cURPFSlotID_Object = MibTableColumn
h3cURPFSlotID = _H3cURPFSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 44, 1, 1, 3),
    _H3cURPFSlotID_Type()
)
h3cURPFSlotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cURPFSlotID.setStatus("current")
_H3cURPFTotalReceivedPacket_Type = Counter64
_H3cURPFTotalReceivedPacket_Object = MibTableColumn
h3cURPFTotalReceivedPacket = _H3cURPFTotalReceivedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 44, 1, 1, 4),
    _H3cURPFTotalReceivedPacket_Type()
)
h3cURPFTotalReceivedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cURPFTotalReceivedPacket.setStatus("current")
_H3cURPFDroppedPacket_Type = Counter64
_H3cURPFDroppedPacket_Object = MibTableColumn
h3cURPFDroppedPacket = _H3cURPFDroppedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 44, 1, 1, 5),
    _H3cURPFDroppedPacket_Type()
)
h3cURPFDroppedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cURPFDroppedPacket.setStatus("current")


class _H3cURPFClearStat_Type(Integer32):
    """Custom type h3cURPFClearStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("reset", 1))
    )


_H3cURPFClearStat_Type.__name__ = "Integer32"
_H3cURPFClearStat_Object = MibTableColumn
h3cURPFClearStat = _H3cURPFClearStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 44, 1, 1, 6),
    _H3cURPFClearStat_Type()
)
h3cURPFClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cURPFClearStat.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-UNICAST-MIB",
    **{"h3cUnicast": h3cUnicast,
       "h3cURPFTable": h3cURPFTable,
       "h3cURPFEntry": h3cURPFEntry,
       "h3cURPFIfIndex": h3cURPFIfIndex,
       "h3cURPFEnabled": h3cURPFEnabled,
       "h3cURPFSlotID": h3cURPFSlotID,
       "h3cURPFTotalReceivedPacket": h3cURPFTotalReceivedPacket,
       "h3cURPFDroppedPacket": h3cURPFDroppedPacket,
       "h3cURPFClearStat": h3cURPFClearStat}
)

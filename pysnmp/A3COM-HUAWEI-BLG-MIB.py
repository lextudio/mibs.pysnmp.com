# SNMP MIB module (A3COM-HUAWEI-BLG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-BLG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:22 2024
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
    "A3COM-HUAWEI-OID-MIB",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

h3cBlg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108)
)
h3cBlg.setRevisions(
        ("2009-09-15 11:11",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CounterClear(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )



# MIB Managed Objects in the order of their OIDs

_H3cBlgObjects_ObjectIdentity = ObjectIdentity
h3cBlgObjects = _H3cBlgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1)
)
_H3cBlgStatsTable_Object = MibTable
h3cBlgStatsTable = _H3cBlgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1)
)
if mibBuilder.loadTexts:
    h3cBlgStatsTable.setStatus("current")
_H3cBlgStatsEntry_Object = MibTableRow
h3cBlgStatsEntry = _H3cBlgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1)
)
h3cBlgStatsEntry.setIndexNames(
    (0, "A3COM-HUAWEI-BLG-MIB", "h3cBlgIndex"),
)
if mibBuilder.loadTexts:
    h3cBlgStatsEntry.setStatus("current")


class _H3cBlgIndex_Type(Integer32):
    """Custom type h3cBlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cBlgIndex_Type.__name__ = "Integer32"
_H3cBlgIndex_Object = MibTableColumn
h3cBlgIndex = _H3cBlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 1),
    _H3cBlgIndex_Type()
)
h3cBlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cBlgIndex.setStatus("current")
_H3cBlgGroupTxPacketCount_Type = Counter64
_H3cBlgGroupTxPacketCount_Object = MibTableColumn
h3cBlgGroupTxPacketCount = _H3cBlgGroupTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 2),
    _H3cBlgGroupTxPacketCount_Type()
)
h3cBlgGroupTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBlgGroupTxPacketCount.setStatus("current")
_H3cBlgGroupRxPacketCount_Type = Counter64
_H3cBlgGroupRxPacketCount_Object = MibTableColumn
h3cBlgGroupRxPacketCount = _H3cBlgGroupRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 3),
    _H3cBlgGroupRxPacketCount_Type()
)
h3cBlgGroupRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBlgGroupRxPacketCount.setStatus("current")
_H3cBlgGroupTxByteCount_Type = Counter64
_H3cBlgGroupTxByteCount_Object = MibTableColumn
h3cBlgGroupTxByteCount = _H3cBlgGroupTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 4),
    _H3cBlgGroupTxByteCount_Type()
)
h3cBlgGroupTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBlgGroupTxByteCount.setStatus("current")
_H3cBlgGroupRxByteCount_Type = Counter64
_H3cBlgGroupRxByteCount_Object = MibTableColumn
h3cBlgGroupRxByteCount = _H3cBlgGroupRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 5),
    _H3cBlgGroupRxByteCount_Type()
)
h3cBlgGroupRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBlgGroupRxByteCount.setStatus("current")
_H3cBlgGroupCountClear_Type = CounterClear
_H3cBlgGroupCountClear_Object = MibTableColumn
h3cBlgGroupCountClear = _H3cBlgGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 6),
    _H3cBlgGroupCountClear_Type()
)
h3cBlgGroupCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cBlgGroupCountClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-BLG-MIB",
    **{"CounterClear": CounterClear,
       "h3cBlg": h3cBlg,
       "h3cBlgObjects": h3cBlgObjects,
       "h3cBlgStatsTable": h3cBlgStatsTable,
       "h3cBlgStatsEntry": h3cBlgStatsEntry,
       "h3cBlgIndex": h3cBlgIndex,
       "h3cBlgGroupTxPacketCount": h3cBlgGroupTxPacketCount,
       "h3cBlgGroupRxPacketCount": h3cBlgGroupRxPacketCount,
       "h3cBlgGroupTxByteCount": h3cBlgGroupTxByteCount,
       "h3cBlgGroupRxByteCount": h3cBlgGroupRxByteCount,
       "h3cBlgGroupCountClear": h3cBlgGroupCountClear}
)

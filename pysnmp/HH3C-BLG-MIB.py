# SNMP MIB module (HH3C-BLG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-BLG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:32 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cBlg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 108)
)
hh3cBlg.setRevisions(
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

_Hh3cBlgObjects_ObjectIdentity = ObjectIdentity
hh3cBlgObjects = _Hh3cBlgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 108, 1)
)
_Hh3cBlgStatsTable_Object = MibTable
hh3cBlgStatsTable = _Hh3cBlgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cBlgStatsTable.setStatus("current")
_Hh3cBlgStatsEntry_Object = MibTableRow
hh3cBlgStatsEntry = _Hh3cBlgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1)
)
hh3cBlgStatsEntry.setIndexNames(
    (0, "HH3C-BLG-MIB", "hh3cBlgIndex"),
)
if mibBuilder.loadTexts:
    hh3cBlgStatsEntry.setStatus("current")


class _Hh3cBlgIndex_Type(Integer32):
    """Custom type hh3cBlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cBlgIndex_Type.__name__ = "Integer32"
_Hh3cBlgIndex_Object = MibTableColumn
hh3cBlgIndex = _Hh3cBlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 1),
    _Hh3cBlgIndex_Type()
)
hh3cBlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBlgIndex.setStatus("current")
_Hh3cBlgGroupTxPacketCount_Type = Counter64
_Hh3cBlgGroupTxPacketCount_Object = MibTableColumn
hh3cBlgGroupTxPacketCount = _Hh3cBlgGroupTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 2),
    _Hh3cBlgGroupTxPacketCount_Type()
)
hh3cBlgGroupTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBlgGroupTxPacketCount.setStatus("current")
_Hh3cBlgGroupRxPacketCount_Type = Counter64
_Hh3cBlgGroupRxPacketCount_Object = MibTableColumn
hh3cBlgGroupRxPacketCount = _Hh3cBlgGroupRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 3),
    _Hh3cBlgGroupRxPacketCount_Type()
)
hh3cBlgGroupRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBlgGroupRxPacketCount.setStatus("current")
_Hh3cBlgGroupTxByteCount_Type = Counter64
_Hh3cBlgGroupTxByteCount_Object = MibTableColumn
hh3cBlgGroupTxByteCount = _Hh3cBlgGroupTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 4),
    _Hh3cBlgGroupTxByteCount_Type()
)
hh3cBlgGroupTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBlgGroupTxByteCount.setStatus("current")
_Hh3cBlgGroupRxByteCount_Type = Counter64
_Hh3cBlgGroupRxByteCount_Object = MibTableColumn
hh3cBlgGroupRxByteCount = _Hh3cBlgGroupRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 5),
    _Hh3cBlgGroupRxByteCount_Type()
)
hh3cBlgGroupRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBlgGroupRxByteCount.setStatus("current")
_Hh3cBlgGroupCountClear_Type = CounterClear
_Hh3cBlgGroupCountClear_Object = MibTableColumn
hh3cBlgGroupCountClear = _Hh3cBlgGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 6),
    _Hh3cBlgGroupCountClear_Type()
)
hh3cBlgGroupCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBlgGroupCountClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-BLG-MIB",
    **{"CounterClear": CounterClear,
       "hh3cBlg": hh3cBlg,
       "hh3cBlgObjects": hh3cBlgObjects,
       "hh3cBlgStatsTable": hh3cBlgStatsTable,
       "hh3cBlgStatsEntry": hh3cBlgStatsEntry,
       "hh3cBlgIndex": hh3cBlgIndex,
       "hh3cBlgGroupTxPacketCount": hh3cBlgGroupTxPacketCount,
       "hh3cBlgGroupRxPacketCount": hh3cBlgGroupRxPacketCount,
       "hh3cBlgGroupTxByteCount": hh3cBlgGroupTxByteCount,
       "hh3cBlgGroupRxByteCount": hh3cBlgGroupRxByteCount,
       "hh3cBlgGroupCountClear": hh3cBlgGroupCountClear}
)

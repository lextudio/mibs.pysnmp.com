# SNMP MIB module (HUAWEI-HQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-HQOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:56 2024
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

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwHQOS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132)
)
hwHQOS.setRevisions(
        ("2014-08-04 15:58",
         "2014-07-23 15:58",
         "2014-06-03 14:55",
         "2014-05-06 19:15",
         "2013-04-24 14:43",
         "2014-03-25 14:33",
         "2013-11-20 14:43",
         "2013-09-30 14:43",
         "2013-09-16 16:09",
         "2013-07-29 14:43",
         "2013-04-10 14:43",
         "2014-08-04 15:58",
         "2014-12-22 15:58")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CosType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )



# MIB Managed Objects in the order of their OIDs

_HwhqosStat_ObjectIdentity = ObjectIdentity
hwhqosStat = _HwhqosStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1)
)
_HwhqosIfStatTable_Object = MibTable
hwhqosIfStatTable = _HwhqosIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1)
)
if mibBuilder.loadTexts:
    hwhqosIfStatTable.setStatus("current")
_HwhqosIfStatEntry_Object = MibTableRow
hwhqosIfStatEntry = _HwhqosIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1)
)
hwhqosIfStatEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserLayer1"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserLayer2"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosQueueIndex"),
)
if mibBuilder.loadTexts:
    hwhqosIfStatEntry.setStatus("current")


class _HwhqosIfIndex_Type(Integer32):
    """Custom type hwhqosIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosIfIndex_Type.__name__ = "Integer32"
_HwhqosIfIndex_Object = MibTableColumn
hwhqosIfIndex = _HwhqosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 1),
    _HwhqosIfIndex_Type()
)
hwhqosIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfIndex.setStatus("current")


class _HwhqosDirection_Type(Integer32):
    """Custom type hwhqosDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("absent", 255),
          ("inbound", 1),
          ("outbound", 2))
    )


_HwhqosDirection_Type.__name__ = "Integer32"
_HwhqosDirection_Object = MibTableColumn
hwhqosDirection = _HwhqosDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 2),
    _HwhqosDirection_Type()
)
hwhqosDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosDirection.setStatus("current")


class _HwhqosUserLayer1_Type(Integer32):
    """Custom type hwhqosUserLayer1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosUserLayer1_Type.__name__ = "Integer32"
_HwhqosUserLayer1_Object = MibTableColumn
hwhqosUserLayer1 = _HwhqosUserLayer1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 3),
    _HwhqosUserLayer1_Type()
)
hwhqosUserLayer1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosUserLayer1.setStatus("current")


class _HwhqosUserLayer2_Type(Integer32):
    """Custom type hwhqosUserLayer2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosUserLayer2_Type.__name__ = "Integer32"
_HwhqosUserLayer2_Object = MibTableColumn
hwhqosUserLayer2 = _HwhqosUserLayer2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 4),
    _HwhqosUserLayer2_Type()
)
hwhqosUserLayer2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosUserLayer2.setStatus("current")


class _HwhqosQueueIndex_Type(Integer32):
    """Custom type hwhqosQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosQueueIndex_Type.__name__ = "Integer32"
_HwhqosQueueIndex_Object = MibTableColumn
hwhqosQueueIndex = _HwhqosQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 5),
    _HwhqosQueueIndex_Type()
)
hwhqosQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosQueueIndex.setStatus("current")
_HwhqosQueueForwardPackets_Type = Counter64
_HwhqosQueueForwardPackets_Object = MibTableColumn
hwhqosQueueForwardPackets = _HwhqosQueueForwardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 6),
    _HwhqosQueueForwardPackets_Type()
)
hwhqosQueueForwardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosQueueForwardPackets.setStatus("current")
_HwhqosQueueForwardBytes_Type = Counter64
_HwhqosQueueForwardBytes_Object = MibTableColumn
hwhqosQueueForwardBytes = _HwhqosQueueForwardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 7),
    _HwhqosQueueForwardBytes_Type()
)
hwhqosQueueForwardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosQueueForwardBytes.setStatus("current")
_HwhqosQueueDropPackets_Type = Counter64
_HwhqosQueueDropPackets_Object = MibTableColumn
hwhqosQueueDropPackets = _HwhqosQueueDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 8),
    _HwhqosQueueDropPackets_Type()
)
hwhqosQueueDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosQueueDropPackets.setStatus("current")
_HwhqosQueueDropBytes_Type = Counter64
_HwhqosQueueDropBytes_Object = MibTableColumn
hwhqosQueueDropBytes = _HwhqosQueueDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 9),
    _HwhqosQueueDropBytes_Type()
)
hwhqosQueueDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosQueueDropBytes.setStatus("current")
_HwhqosQueueRemarkPackets_Type = Counter64
_HwhqosQueueRemarkPackets_Object = MibTableColumn
hwhqosQueueRemarkPackets = _HwhqosQueueRemarkPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 10),
    _HwhqosQueueRemarkPackets_Type()
)
hwhqosQueueRemarkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosQueueRemarkPackets.setStatus("current")
_HwhqosQueueRemarkBytes_Type = Counter64
_HwhqosQueueRemarkBytes_Object = MibTableColumn
hwhqosQueueRemarkBytes = _HwhqosQueueRemarkBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 11),
    _HwhqosQueueRemarkBytes_Type()
)
hwhqosQueueRemarkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosQueueRemarkBytes.setStatus("current")


class _HwhqosSetZero_Type(Integer32):
    """Custom type hwhqosSetZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setZero", 1)
    )


_HwhqosSetZero_Type.__name__ = "Integer32"
_HwhqosSetZero_Object = MibTableColumn
hwhqosSetZero = _HwhqosSetZero_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 12),
    _HwhqosSetZero_Type()
)
hwhqosSetZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwhqosSetZero.setStatus("current")
_HwhqosQueueForwardPacketRate_Type = Counter64
_HwhqosQueueForwardPacketRate_Object = MibTableColumn
hwhqosQueueForwardPacketRate = _HwhqosQueueForwardPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 13),
    _HwhqosQueueForwardPacketRate_Type()
)
hwhqosQueueForwardPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosQueueForwardPacketRate.setStatus("current")
_HwhqosQueueForwardByteRate_Type = Counter64
_HwhqosQueueForwardByteRate_Object = MibTableColumn
hwhqosQueueForwardByteRate = _HwhqosQueueForwardByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 14),
    _HwhqosQueueForwardByteRate_Type()
)
hwhqosQueueForwardByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosQueueForwardByteRate.setStatus("current")
_HwhqosQueueDropPacketRate_Type = Counter64
_HwhqosQueueDropPacketRate_Object = MibTableColumn
hwhqosQueueDropPacketRate = _HwhqosQueueDropPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 15),
    _HwhqosQueueDropPacketRate_Type()
)
hwhqosQueueDropPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosQueueDropPacketRate.setStatus("current")
_HwhqosQueueDropByteRate_Type = Counter64
_HwhqosQueueDropByteRate_Object = MibTableColumn
hwhqosQueueDropByteRate = _HwhqosQueueDropByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 1, 1, 16),
    _HwhqosQueueDropByteRate_Type()
)
hwhqosQueueDropByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosQueueDropByteRate.setStatus("current")
_HwhqosAtmPvcStatTable_Object = MibTable
hwhqosAtmPvcStatTable = _HwhqosAtmPvcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2)
)
if mibBuilder.loadTexts:
    hwhqosAtmPvcStatTable.setStatus("current")
_HwhqosAtmPvcStatEntry_Object = MibTableRow
hwhqosAtmPvcStatEntry = _HwhqosAtmPvcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1)
)
hwhqosAtmPvcStatEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosAtmPvcIfIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosAtmPvcVPI"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosAtmPvcVCI"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosAtmPvcDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosAtmPvcUserLayer1"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosAtmPvcUserLayer2"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosAtmPvcQueueIndex"),
)
if mibBuilder.loadTexts:
    hwhqosAtmPvcStatEntry.setStatus("current")


class _HwhqosAtmPvcIfIndex_Type(Integer32):
    """Custom type hwhqosAtmPvcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosAtmPvcIfIndex_Type.__name__ = "Integer32"
_HwhqosAtmPvcIfIndex_Object = MibTableColumn
hwhqosAtmPvcIfIndex = _HwhqosAtmPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 1),
    _HwhqosAtmPvcIfIndex_Type()
)
hwhqosAtmPvcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosAtmPvcIfIndex.setStatus("current")


class _HwhqosAtmPvcVPI_Type(Integer32):
    """Custom type hwhqosAtmPvcVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosAtmPvcVPI_Type.__name__ = "Integer32"
_HwhqosAtmPvcVPI_Object = MibTableColumn
hwhqosAtmPvcVPI = _HwhqosAtmPvcVPI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 2),
    _HwhqosAtmPvcVPI_Type()
)
hwhqosAtmPvcVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosAtmPvcVPI.setStatus("current")


class _HwhqosAtmPvcVCI_Type(Integer32):
    """Custom type hwhqosAtmPvcVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosAtmPvcVCI_Type.__name__ = "Integer32"
_HwhqosAtmPvcVCI_Object = MibTableColumn
hwhqosAtmPvcVCI = _HwhqosAtmPvcVCI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 3),
    _HwhqosAtmPvcVCI_Type()
)
hwhqosAtmPvcVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosAtmPvcVCI.setStatus("current")


class _HwhqosAtmPvcDirection_Type(Integer32):
    """Custom type hwhqosAtmPvcDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("absent", 255),
          ("inbound", 1),
          ("outbound", 2))
    )


_HwhqosAtmPvcDirection_Type.__name__ = "Integer32"
_HwhqosAtmPvcDirection_Object = MibTableColumn
hwhqosAtmPvcDirection = _HwhqosAtmPvcDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 4),
    _HwhqosAtmPvcDirection_Type()
)
hwhqosAtmPvcDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosAtmPvcDirection.setStatus("current")


class _HwhqosAtmPvcUserLayer1_Type(Integer32):
    """Custom type hwhqosAtmPvcUserLayer1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosAtmPvcUserLayer1_Type.__name__ = "Integer32"
_HwhqosAtmPvcUserLayer1_Object = MibTableColumn
hwhqosAtmPvcUserLayer1 = _HwhqosAtmPvcUserLayer1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 5),
    _HwhqosAtmPvcUserLayer1_Type()
)
hwhqosAtmPvcUserLayer1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosAtmPvcUserLayer1.setStatus("current")


class _HwhqosAtmPvcUserLayer2_Type(Integer32):
    """Custom type hwhqosAtmPvcUserLayer2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosAtmPvcUserLayer2_Type.__name__ = "Integer32"
_HwhqosAtmPvcUserLayer2_Object = MibTableColumn
hwhqosAtmPvcUserLayer2 = _HwhqosAtmPvcUserLayer2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 6),
    _HwhqosAtmPvcUserLayer2_Type()
)
hwhqosAtmPvcUserLayer2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosAtmPvcUserLayer2.setStatus("current")


class _HwhqosAtmPvcQueueIndex_Type(Integer32):
    """Custom type hwhqosAtmPvcQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosAtmPvcQueueIndex_Type.__name__ = "Integer32"
_HwhqosAtmPvcQueueIndex_Object = MibTableColumn
hwhqosAtmPvcQueueIndex = _HwhqosAtmPvcQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 7),
    _HwhqosAtmPvcQueueIndex_Type()
)
hwhqosAtmPvcQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosAtmPvcQueueIndex.setStatus("current")
_HwhqosAtmPvcQueueForwardPackets_Type = Counter64
_HwhqosAtmPvcQueueForwardPackets_Object = MibTableColumn
hwhqosAtmPvcQueueForwardPackets = _HwhqosAtmPvcQueueForwardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 8),
    _HwhqosAtmPvcQueueForwardPackets_Type()
)
hwhqosAtmPvcQueueForwardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosAtmPvcQueueForwardPackets.setStatus("current")
_HwhqosAtmPvcQueueForwardBytes_Type = Counter64
_HwhqosAtmPvcQueueForwardBytes_Object = MibTableColumn
hwhqosAtmPvcQueueForwardBytes = _HwhqosAtmPvcQueueForwardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 9),
    _HwhqosAtmPvcQueueForwardBytes_Type()
)
hwhqosAtmPvcQueueForwardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosAtmPvcQueueForwardBytes.setStatus("current")
_HwhqosAtmPvcQueueDropPackets_Type = Counter64
_HwhqosAtmPvcQueueDropPackets_Object = MibTableColumn
hwhqosAtmPvcQueueDropPackets = _HwhqosAtmPvcQueueDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 10),
    _HwhqosAtmPvcQueueDropPackets_Type()
)
hwhqosAtmPvcQueueDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosAtmPvcQueueDropPackets.setStatus("current")
_HwhqosAtmPvcQueueDropBytes_Type = Counter64
_HwhqosAtmPvcQueueDropBytes_Object = MibTableColumn
hwhqosAtmPvcQueueDropBytes = _HwhqosAtmPvcQueueDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 11),
    _HwhqosAtmPvcQueueDropBytes_Type()
)
hwhqosAtmPvcQueueDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosAtmPvcQueueDropBytes.setStatus("current")
_HwhqosAtmPvcQueueRemarkPackets_Type = Counter64
_HwhqosAtmPvcQueueRemarkPackets_Object = MibTableColumn
hwhqosAtmPvcQueueRemarkPackets = _HwhqosAtmPvcQueueRemarkPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 12),
    _HwhqosAtmPvcQueueRemarkPackets_Type()
)
hwhqosAtmPvcQueueRemarkPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosAtmPvcQueueRemarkPackets.setStatus("current")
_HwhqosAtmPvcQueueRemarkBytes_Type = Counter64
_HwhqosAtmPvcQueueRemarkBytes_Object = MibTableColumn
hwhqosAtmPvcQueueRemarkBytes = _HwhqosAtmPvcQueueRemarkBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 2, 1, 13),
    _HwhqosAtmPvcQueueRemarkBytes_Type()
)
hwhqosAtmPvcQueueRemarkBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosAtmPvcQueueRemarkBytes.setStatus("current")
_HwhqosPortQueueTable_Object = MibTable
hwhqosPortQueueTable = _HwhqosPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 3)
)
if mibBuilder.loadTexts:
    hwhqosPortQueueTable.setStatus("current")
_HwhqosPortQueueEntry_Object = MibTableRow
hwhqosPortQueueEntry = _HwhqosPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 3, 1)
)
hwhqosPortQueueEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosPortQueueIfIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosPortQueueCosValue"),
)
if mibBuilder.loadTexts:
    hwhqosPortQueueEntry.setStatus("current")


class _HwhqosPortQueueIfIndex_Type(Integer32):
    """Custom type hwhqosPortQueueIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosPortQueueIfIndex_Type.__name__ = "Integer32"
_HwhqosPortQueueIfIndex_Object = MibTableColumn
hwhqosPortQueueIfIndex = _HwhqosPortQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 3, 1, 1),
    _HwhqosPortQueueIfIndex_Type()
)
hwhqosPortQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosPortQueueIfIndex.setStatus("current")


class _HwhqosPortQueueCosValue_Type(Integer32):
    """Custom type hwhqosPortQueueCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("portqueueAF1", 2),
          ("portqueueAF2", 3),
          ("portqueueAF3", 4),
          ("portqueueAF4", 5),
          ("portqueueBE", 1),
          ("portqueueCS6", 7),
          ("portqueueCS7", 8),
          ("portqueueEF", 6))
    )


_HwhqosPortQueueCosValue_Type.__name__ = "Integer32"
_HwhqosPortQueueCosValue_Object = MibTableColumn
hwhqosPortQueueCosValue = _HwhqosPortQueueCosValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 3, 1, 2),
    _HwhqosPortQueueCosValue_Type()
)
hwhqosPortQueueCosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosPortQueueCosValue.setStatus("current")


class _HwhqosPortQueueArithmetic_Type(Integer32):
    """Custom type hwhqosPortQueueArithmetic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portqueueLPQ", 3),
          ("portqueuePQ", 1),
          ("portqueueWFQ", 2))
    )


_HwhqosPortQueueArithmetic_Type.__name__ = "Integer32"
_HwhqosPortQueueArithmetic_Object = MibTableColumn
hwhqosPortQueueArithmetic = _HwhqosPortQueueArithmetic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 3, 1, 11),
    _HwhqosPortQueueArithmetic_Type()
)
hwhqosPortQueueArithmetic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosPortQueueArithmetic.setStatus("current")
_HwhqosPortQueueWeightValue_Type = Integer32
_HwhqosPortQueueWeightValue_Object = MibTableColumn
hwhqosPortQueueWeightValue = _HwhqosPortQueueWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 3, 1, 12),
    _HwhqosPortQueueWeightValue_Type()
)
hwhqosPortQueueWeightValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosPortQueueWeightValue.setStatus("current")
_HwhqosPortQueueShaValue_Type = Unsigned32
_HwhqosPortQueueShaValue_Object = MibTableColumn
hwhqosPortQueueShaValue = _HwhqosPortQueueShaValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 3, 1, 13),
    _HwhqosPortQueueShaValue_Type()
)
hwhqosPortQueueShaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosPortQueueShaValue.setStatus("current")
_HwhqosPortQueueShaPercent_Type = Integer32
_HwhqosPortQueueShaPercent_Object = MibTableColumn
hwhqosPortQueueShaPercent = _HwhqosPortQueueShaPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 3, 1, 14),
    _HwhqosPortQueueShaPercent_Type()
)
hwhqosPortQueueShaPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosPortQueueShaPercent.setStatus("current")


class _HwhqosPortQueueWredName_Type(OctetString):
    """Custom type hwhqosPortQueueWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosPortQueueWredName_Type.__name__ = "OctetString"
_HwhqosPortQueueWredName_Object = MibTableColumn
hwhqosPortQueueWredName = _HwhqosPortQueueWredName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 3, 1, 15),
    _HwhqosPortQueueWredName_Type()
)
hwhqosPortQueueWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosPortQueueWredName.setStatus("current")


class _HwhqosPortQueuePbsValue_Type(Integer32):
    """Custom type hwhqosPortQueuePbsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 262144),
    )


_HwhqosPortQueuePbsValue_Type.__name__ = "Integer32"
_HwhqosPortQueuePbsValue_Object = MibTableColumn
hwhqosPortQueuePbsValue = _HwhqosPortQueuePbsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 3, 1, 16),
    _HwhqosPortQueuePbsValue_Type()
)
hwhqosPortQueuePbsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosPortQueuePbsValue.setStatus("current")
_HwhqosPortQueueRowStatus_Type = RowStatus
_HwhqosPortQueueRowStatus_Object = MibTableColumn
hwhqosPortQueueRowStatus = _HwhqosPortQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 3, 1, 51),
    _HwhqosPortQueueRowStatus_Type()
)
hwhqosPortQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosPortQueueRowStatus.setStatus("current")
_HwhqosWredTable_Object = MibTable
hwhqosWredTable = _HwhqosWredTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4)
)
if mibBuilder.loadTexts:
    hwhqosWredTable.setStatus("current")
_HwhqosWredEntry_Object = MibTableRow
hwhqosWredEntry = _HwhqosWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1)
)
hwhqosWredEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosWredName"),
)
if mibBuilder.loadTexts:
    hwhqosWredEntry.setStatus("current")


class _HwhqosWredName_Type(OctetString):
    """Custom type hwhqosWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosWredName_Type.__name__ = "OctetString"
_HwhqosWredName_Object = MibTableColumn
hwhqosWredName = _HwhqosWredName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1, 1),
    _HwhqosWredName_Type()
)
hwhqosWredName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosWredName.setStatus("current")
_HwhqosWredGreenLowLimit_Type = Integer32
_HwhqosWredGreenLowLimit_Object = MibTableColumn
hwhqosWredGreenLowLimit = _HwhqosWredGreenLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1, 11),
    _HwhqosWredGreenLowLimit_Type()
)
hwhqosWredGreenLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredGreenLowLimit.setStatus("current")
_HwhqosWredGreenHighLimit_Type = Integer32
_HwhqosWredGreenHighLimit_Object = MibTableColumn
hwhqosWredGreenHighLimit = _HwhqosWredGreenHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1, 12),
    _HwhqosWredGreenHighLimit_Type()
)
hwhqosWredGreenHighLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredGreenHighLimit.setStatus("current")
_HwhqosWredGreenDiscardPercent_Type = Integer32
_HwhqosWredGreenDiscardPercent_Object = MibTableColumn
hwhqosWredGreenDiscardPercent = _HwhqosWredGreenDiscardPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1, 13),
    _HwhqosWredGreenDiscardPercent_Type()
)
hwhqosWredGreenDiscardPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredGreenDiscardPercent.setStatus("current")
_HwhqosWredYellowLowLimit_Type = Integer32
_HwhqosWredYellowLowLimit_Object = MibTableColumn
hwhqosWredYellowLowLimit = _HwhqosWredYellowLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1, 14),
    _HwhqosWredYellowLowLimit_Type()
)
hwhqosWredYellowLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredYellowLowLimit.setStatus("current")
_HwhqosWredYellowHighLimit_Type = Integer32
_HwhqosWredYellowHighLimit_Object = MibTableColumn
hwhqosWredYellowHighLimit = _HwhqosWredYellowHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1, 15),
    _HwhqosWredYellowHighLimit_Type()
)
hwhqosWredYellowHighLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredYellowHighLimit.setStatus("current")
_HwhqosWredYellowDiscardPercent_Type = Integer32
_HwhqosWredYellowDiscardPercent_Object = MibTableColumn
hwhqosWredYellowDiscardPercent = _HwhqosWredYellowDiscardPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1, 16),
    _HwhqosWredYellowDiscardPercent_Type()
)
hwhqosWredYellowDiscardPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredYellowDiscardPercent.setStatus("current")
_HwhqosWredRedLowLimit_Type = Integer32
_HwhqosWredRedLowLimit_Object = MibTableColumn
hwhqosWredRedLowLimit = _HwhqosWredRedLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1, 17),
    _HwhqosWredRedLowLimit_Type()
)
hwhqosWredRedLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredRedLowLimit.setStatus("current")
_HwhqosWredRedHighLimit_Type = Integer32
_HwhqosWredRedHighLimit_Object = MibTableColumn
hwhqosWredRedHighLimit = _HwhqosWredRedHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1, 18),
    _HwhqosWredRedHighLimit_Type()
)
hwhqosWredRedHighLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredRedHighLimit.setStatus("current")
_HwhqosWredRedDiscardPercent_Type = Integer32
_HwhqosWredRedDiscardPercent_Object = MibTableColumn
hwhqosWredRedDiscardPercent = _HwhqosWredRedDiscardPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1, 19),
    _HwhqosWredRedDiscardPercent_Type()
)
hwhqosWredRedDiscardPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredRedDiscardPercent.setStatus("current")
_HwhqosWredRowStatus_Type = RowStatus
_HwhqosWredRowStatus_Object = MibTableColumn
hwhqosWredRowStatus = _HwhqosWredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 4, 1, 51),
    _HwhqosWredRowStatus_Type()
)
hwhqosWredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredRowStatus.setStatus("current")
_HwhqosIfQueueStatTable_Object = MibTable
hwhqosIfQueueStatTable = _HwhqosIfQueueStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 5)
)
if mibBuilder.loadTexts:
    hwhqosIfQueueStatTable.setStatus("current")
_HwhqosIfQueueStatEntry_Object = MibTableRow
hwhqosIfQueueStatEntry = _HwhqosIfQueueStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 5, 1)
)
hwhqosIfQueueStatEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfQueueStatIfIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfQueueStatQueueIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfQueueStatDirection"),
)
if mibBuilder.loadTexts:
    hwhqosIfQueueStatEntry.setStatus("current")
_HwhqosIfQueueStatIfIndex_Type = InterfaceIndex
_HwhqosIfQueueStatIfIndex_Object = MibTableColumn
hwhqosIfQueueStatIfIndex = _HwhqosIfQueueStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 5, 1, 1),
    _HwhqosIfQueueStatIfIndex_Type()
)
hwhqosIfQueueStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfQueueStatIfIndex.setStatus("current")


class _HwhqosIfQueueStatQueueIndex_Type(Integer32):
    """Custom type hwhqosIfQueueStatQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwhqosIfQueueStatQueueIndex_Type.__name__ = "Integer32"
_HwhqosIfQueueStatQueueIndex_Object = MibTableColumn
hwhqosIfQueueStatQueueIndex = _HwhqosIfQueueStatQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 5, 1, 2),
    _HwhqosIfQueueStatQueueIndex_Type()
)
hwhqosIfQueueStatQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfQueueStatQueueIndex.setStatus("current")


class _HwhqosIfQueueStatDirection_Type(Integer32):
    """Custom type hwhqosIfQueueStatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosIfQueueStatDirection_Type.__name__ = "Integer32"
_HwhqosIfQueueStatDirection_Object = MibTableColumn
hwhqosIfQueueStatDirection = _HwhqosIfQueueStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 5, 1, 3),
    _HwhqosIfQueueStatDirection_Type()
)
hwhqosIfQueueStatDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfQueueStatDirection.setStatus("current")
_HwhqosIfQueueStatForwardPackets_Type = Counter64
_HwhqosIfQueueStatForwardPackets_Object = MibTableColumn
hwhqosIfQueueStatForwardPackets = _HwhqosIfQueueStatForwardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 5, 1, 4),
    _HwhqosIfQueueStatForwardPackets_Type()
)
hwhqosIfQueueStatForwardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosIfQueueStatForwardPackets.setStatus("current")
_HwhqosIfQueueStatForwardBytes_Type = Counter64
_HwhqosIfQueueStatForwardBytes_Object = MibTableColumn
hwhqosIfQueueStatForwardBytes = _HwhqosIfQueueStatForwardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 5, 1, 5),
    _HwhqosIfQueueStatForwardBytes_Type()
)
hwhqosIfQueueStatForwardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosIfQueueStatForwardBytes.setStatus("current")
_HwhqosIfQueueStatDropPackets_Type = Counter64
_HwhqosIfQueueStatDropPackets_Object = MibTableColumn
hwhqosIfQueueStatDropPackets = _HwhqosIfQueueStatDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 5, 1, 6),
    _HwhqosIfQueueStatDropPackets_Type()
)
hwhqosIfQueueStatDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosIfQueueStatDropPackets.setStatus("current")
_HwhqosIfQueueStatDropBytes_Type = Counter64
_HwhqosIfQueueStatDropBytes_Object = MibTableColumn
hwhqosIfQueueStatDropBytes = _HwhqosIfQueueStatDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 5, 1, 7),
    _HwhqosIfQueueStatDropBytes_Type()
)
hwhqosIfQueueStatDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosIfQueueStatDropBytes.setStatus("current")
_HwhqosUserQueueStatTable_Object = MibTable
hwhqosUserQueueStatTable = _HwhqosUserQueueStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6)
)
if mibBuilder.loadTexts:
    hwhqosUserQueueStatTable.setStatus("current")
_HwhqosUserQueueStatEntry_Object = MibTableRow
hwhqosUserQueueStatEntry = _HwhqosUserQueueStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1)
)
hwhqosUserQueueStatEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueStatType"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueStatNameString"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueStatDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueStatQueueIndex"),
)
if mibBuilder.loadTexts:
    hwhqosUserQueueStatEntry.setStatus("current")


class _HwhqosUserQueueStatType_Type(Integer32):
    """Custom type hwhqosUserQueueStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("mactunel", 2),
          ("userclassifier", 3))
    )


_HwhqosUserQueueStatType_Type.__name__ = "Integer32"
_HwhqosUserQueueStatType_Object = MibTableColumn
hwhqosUserQueueStatType = _HwhqosUserQueueStatType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1, 1),
    _HwhqosUserQueueStatType_Type()
)
hwhqosUserQueueStatType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatType.setStatus("current")
_HwhqosUserQueueStatNameString_Type = OctetString
_HwhqosUserQueueStatNameString_Object = MibTableColumn
hwhqosUserQueueStatNameString = _HwhqosUserQueueStatNameString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1, 2),
    _HwhqosUserQueueStatNameString_Type()
)
hwhqosUserQueueStatNameString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatNameString.setStatus("current")


class _HwhqosUserQueueStatDirection_Type(Integer32):
    """Custom type hwhqosUserQueueStatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosUserQueueStatDirection_Type.__name__ = "Integer32"
_HwhqosUserQueueStatDirection_Object = MibTableColumn
hwhqosUserQueueStatDirection = _HwhqosUserQueueStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1, 3),
    _HwhqosUserQueueStatDirection_Type()
)
hwhqosUserQueueStatDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatDirection.setStatus("current")


class _HwhqosUserQueueStatQueueIndex_Type(Integer32):
    """Custom type hwhqosUserQueueStatQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("total", 9))
    )


_HwhqosUserQueueStatQueueIndex_Type.__name__ = "Integer32"
_HwhqosUserQueueStatQueueIndex_Object = MibTableColumn
hwhqosUserQueueStatQueueIndex = _HwhqosUserQueueStatQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1, 4),
    _HwhqosUserQueueStatQueueIndex_Type()
)
hwhqosUserQueueStatQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatQueueIndex.setStatus("current")
_HwhqosUserQueueStatForwardPackets_Type = Counter64
_HwhqosUserQueueStatForwardPackets_Object = MibTableColumn
hwhqosUserQueueStatForwardPackets = _HwhqosUserQueueStatForwardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1, 5),
    _HwhqosUserQueueStatForwardPackets_Type()
)
hwhqosUserQueueStatForwardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatForwardPackets.setStatus("current")
_HwhqosUserQueueStatForwardBytes_Type = Counter64
_HwhqosUserQueueStatForwardBytes_Object = MibTableColumn
hwhqosUserQueueStatForwardBytes = _HwhqosUserQueueStatForwardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1, 6),
    _HwhqosUserQueueStatForwardBytes_Type()
)
hwhqosUserQueueStatForwardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatForwardBytes.setStatus("current")
_HwhqosUserQueueStatDropPackets_Type = Counter64
_HwhqosUserQueueStatDropPackets_Object = MibTableColumn
hwhqosUserQueueStatDropPackets = _HwhqosUserQueueStatDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1, 7),
    _HwhqosUserQueueStatDropPackets_Type()
)
hwhqosUserQueueStatDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatDropPackets.setStatus("current")
_HwhqosUserQueueStatDropBytes_Type = Counter64
_HwhqosUserQueueStatDropBytes_Object = MibTableColumn
hwhqosUserQueueStatDropBytes = _HwhqosUserQueueStatDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1, 8),
    _HwhqosUserQueueStatDropBytes_Type()
)
hwhqosUserQueueStatDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatDropBytes.setStatus("current")


class _HwhqosUserQueueStatReset_Type(Integer32):
    """Custom type hwhqosUserQueueStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwhqosUserQueueStatReset_Type.__name__ = "Integer32"
_HwhqosUserQueueStatReset_Object = MibTableColumn
hwhqosUserQueueStatReset = _HwhqosUserQueueStatReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1, 9),
    _HwhqosUserQueueStatReset_Type()
)
hwhqosUserQueueStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatReset.setStatus("current")
_HwhqosUserQueueStatLastResetTime_Type = TimeTicks
_HwhqosUserQueueStatLastResetTime_Object = MibTableColumn
hwhqosUserQueueStatLastResetTime = _HwhqosUserQueueStatLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1, 10),
    _HwhqosUserQueueStatLastResetTime_Type()
)
hwhqosUserQueueStatLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatLastResetTime.setStatus("current")
_HwhqosUserQueueStatPerDropPackets_Type = Counter64
_HwhqosUserQueueStatPerDropPackets_Object = MibTableColumn
hwhqosUserQueueStatPerDropPackets = _HwhqosUserQueueStatPerDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 6, 1, 11),
    _HwhqosUserQueueStatPerDropPackets_Type()
)
hwhqosUserQueueStatPerDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatPerDropPackets.setStatus("current")
_HwhqosUserGroupQueueStatTable_Object = MibTable
hwhqosUserGroupQueueStatTable = _HwhqosUserGroupQueueStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 7)
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatTable.setStatus("current")
_HwhqosUserGroupQueueStatEntry_Object = MibTableRow
hwhqosUserGroupQueueStatEntry = _HwhqosUserGroupQueueStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 7, 1)
)
hwhqosUserGroupQueueStatEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatGroupName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatDirection"),
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatEntry.setStatus("current")
_HwhqosUserGroupQueueStatGroupName_Type = OctetString
_HwhqosUserGroupQueueStatGroupName_Object = MibTableColumn
hwhqosUserGroupQueueStatGroupName = _HwhqosUserGroupQueueStatGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 7, 1, 1),
    _HwhqosUserGroupQueueStatGroupName_Type()
)
hwhqosUserGroupQueueStatGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatGroupName.setStatus("current")


class _HwhqosUserGroupQueueStatDirection_Type(Integer32):
    """Custom type hwhqosUserGroupQueueStatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbount", 1),
          ("outbound", 2))
    )


_HwhqosUserGroupQueueStatDirection_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueStatDirection_Object = MibTableColumn
hwhqosUserGroupQueueStatDirection = _HwhqosUserGroupQueueStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 7, 1, 2),
    _HwhqosUserGroupQueueStatDirection_Type()
)
hwhqosUserGroupQueueStatDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatDirection.setStatus("current")
_HwhqosUserGroupQueueForwardPackets_Type = Counter64
_HwhqosUserGroupQueueForwardPackets_Object = MibTableColumn
hwhqosUserGroupQueueForwardPackets = _HwhqosUserGroupQueueForwardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 7, 1, 3),
    _HwhqosUserGroupQueueForwardPackets_Type()
)
hwhqosUserGroupQueueForwardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueForwardPackets.setStatus("current")
_HwhqosUserGroupQueueForwardBytes_Type = Counter64
_HwhqosUserGroupQueueForwardBytes_Object = MibTableColumn
hwhqosUserGroupQueueForwardBytes = _HwhqosUserGroupQueueForwardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 7, 1, 4),
    _HwhqosUserGroupQueueForwardBytes_Type()
)
hwhqosUserGroupQueueForwardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueForwardBytes.setStatus("current")
_HwhqosUserGroupQueueDropPackets_Type = Counter64
_HwhqosUserGroupQueueDropPackets_Object = MibTableColumn
hwhqosUserGroupQueueDropPackets = _HwhqosUserGroupQueueDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 7, 1, 5),
    _HwhqosUserGroupQueueDropPackets_Type()
)
hwhqosUserGroupQueueDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueDropPackets.setStatus("current")
_HwhqosUserGroupQueueDropBytes_Type = Counter64
_HwhqosUserGroupQueueDropBytes_Object = MibTableColumn
hwhqosUserGroupQueueDropBytes = _HwhqosUserGroupQueueDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 7, 1, 6),
    _HwhqosUserGroupQueueDropBytes_Type()
)
hwhqosUserGroupQueueDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueDropBytes.setStatus("current")


class _HwhqosUserGroupQueueStatReset_Type(Integer32):
    """Custom type hwhqosUserGroupQueueStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwhqosUserGroupQueueStatReset_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueStatReset_Object = MibTableColumn
hwhqosUserGroupQueueStatReset = _HwhqosUserGroupQueueStatReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 7, 1, 7),
    _HwhqosUserGroupQueueStatReset_Type()
)
hwhqosUserGroupQueueStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatReset.setStatus("current")
_HwhqosUserGroupQueueStatLastResetTime_Type = TimeTicks
_HwhqosUserGroupQueueStatLastResetTime_Object = MibTableColumn
hwhqosUserGroupQueueStatLastResetTime = _HwhqosUserGroupQueueStatLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 7, 1, 8),
    _HwhqosUserGroupQueueStatLastResetTime_Type()
)
hwhqosUserGroupQueueStatLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatLastResetTime.setStatus("current")
_HwVPNHQoSTunnelStatisticsTable_Object = MibTable
hwVPNHQoSTunnelStatisticsTable = _HwVPNHQoSTunnelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 8)
)
if mibBuilder.loadTexts:
    hwVPNHQoSTunnelStatisticsTable.setStatus("current")
_HwVPNHQoSTunnelStatisticsEntry_Object = MibTableRow
hwVPNHQoSTunnelStatisticsEntry = _HwVPNHQoSTunnelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 8, 1)
)
hwVPNHQoSTunnelStatisticsEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwVPNHQoSTunnelIfIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwVPNHQoSVPNType"),
    (0, "HUAWEI-HQOS-MIB", "hwVPNHQoSVPNValue"),
)
if mibBuilder.loadTexts:
    hwVPNHQoSTunnelStatisticsEntry.setStatus("current")
_HwVPNHQoSTunnelIfIndex_Type = Integer32
_HwVPNHQoSTunnelIfIndex_Object = MibTableColumn
hwVPNHQoSTunnelIfIndex = _HwVPNHQoSTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 8, 1, 1),
    _HwVPNHQoSTunnelIfIndex_Type()
)
hwVPNHQoSTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVPNHQoSTunnelIfIndex.setStatus("current")


class _HwVPNHQoSVPNType_Type(Integer32):
    """Custom type hwVPNHQoSVPNType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HwVPNHQoSVPNType_Type.__name__ = "Integer32"
_HwVPNHQoSVPNType_Object = MibTableColumn
hwVPNHQoSVPNType = _HwVPNHQoSVPNType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 8, 1, 2),
    _HwVPNHQoSVPNType_Type()
)
hwVPNHQoSVPNType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVPNHQoSVPNType.setStatus("current")
_HwVPNHQoSVPNValue_Type = OctetString
_HwVPNHQoSVPNValue_Object = MibTableColumn
hwVPNHQoSVPNValue = _HwVPNHQoSVPNValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 8, 1, 3),
    _HwVPNHQoSVPNValue_Type()
)
hwVPNHQoSVPNValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVPNHQoSVPNValue.setStatus("current")
_HwVPNHQoSPassBytes_Type = Counter64
_HwVPNHQoSPassBytes_Object = MibTableColumn
hwVPNHQoSPassBytes = _HwVPNHQoSPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 8, 1, 4),
    _HwVPNHQoSPassBytes_Type()
)
hwVPNHQoSPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVPNHQoSPassBytes.setStatus("current")
_HwVPNHQoSPassPackets_Type = Counter64
_HwVPNHQoSPassPackets_Object = MibTableColumn
hwVPNHQoSPassPackets = _HwVPNHQoSPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 8, 1, 5),
    _HwVPNHQoSPassPackets_Type()
)
hwVPNHQoSPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVPNHQoSPassPackets.setStatus("current")
_HwVPNHQoSDropPackets_Type = Counter64
_HwVPNHQoSDropPackets_Object = MibTableColumn
hwVPNHQoSDropPackets = _HwVPNHQoSDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 8, 1, 6),
    _HwVPNHQoSDropPackets_Type()
)
hwVPNHQoSDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVPNHQoSDropPackets.setStatus("current")
_HwVPNHQoSDropBytes_Type = Counter64
_HwVPNHQoSDropBytes_Object = MibTableColumn
hwVPNHQoSDropBytes = _HwVPNHQoSDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 8, 1, 7),
    _HwVPNHQoSDropBytes_Type()
)
hwVPNHQoSDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVPNHQoSDropBytes.setStatus("current")
_HwhqosTunnelStatisticsTable_Object = MibTable
hwhqosTunnelStatisticsTable = _HwhqosTunnelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9)
)
if mibBuilder.loadTexts:
    hwhqosTunnelStatisticsTable.setStatus("current")
_HwhqosTunnelStatisticsEntry_Object = MibTableRow
hwhqosTunnelStatisticsEntry = _HwhqosTunnelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9, 1)
)
hwhqosTunnelStatisticsEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosTunnelIfIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosTunnelCosType"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosTunnelVPNType"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosTunnelVPNName"),
)
if mibBuilder.loadTexts:
    hwhqosTunnelStatisticsEntry.setStatus("current")
_HwhqosTunnelIfIndex_Type = Integer32
_HwhqosTunnelIfIndex_Object = MibTableColumn
hwhqosTunnelIfIndex = _HwhqosTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9, 1, 1),
    _HwhqosTunnelIfIndex_Type()
)
hwhqosTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosTunnelIfIndex.setStatus("current")
_HwhqosTunnelCosType_Type = CosType
_HwhqosTunnelCosType_Object = MibTableColumn
hwhqosTunnelCosType = _HwhqosTunnelCosType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9, 1, 2),
    _HwhqosTunnelCosType_Type()
)
hwhqosTunnelCosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosTunnelCosType.setStatus("current")


class _HwhqosTunnelVPNType_Type(Integer32):
    """Custom type hwhqosTunnelVPNType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HwhqosTunnelVPNType_Type.__name__ = "Integer32"
_HwhqosTunnelVPNType_Object = MibTableColumn
hwhqosTunnelVPNType = _HwhqosTunnelVPNType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9, 1, 3),
    _HwhqosTunnelVPNType_Type()
)
hwhqosTunnelVPNType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosTunnelVPNType.setStatus("current")


class _HwhqosTunnelVPNName_Type(OctetString):
    """Custom type hwhqosTunnelVPNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwhqosTunnelVPNName_Type.__name__ = "OctetString"
_HwhqosTunnelVPNName_Object = MibTableColumn
hwhqosTunnelVPNName = _HwhqosTunnelVPNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9, 1, 4),
    _HwhqosTunnelVPNName_Type()
)
hwhqosTunnelVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosTunnelVPNName.setStatus("current")
_HwhqosTunnelPassBytes_Type = Counter64
_HwhqosTunnelPassBytes_Object = MibTableColumn
hwhqosTunnelPassBytes = _HwhqosTunnelPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9, 1, 5),
    _HwhqosTunnelPassBytes_Type()
)
hwhqosTunnelPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosTunnelPassBytes.setStatus("current")
_HwhqosTunnelPassPackets_Type = Counter64
_HwhqosTunnelPassPackets_Object = MibTableColumn
hwhqosTunnelPassPackets = _HwhqosTunnelPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9, 1, 6),
    _HwhqosTunnelPassPackets_Type()
)
hwhqosTunnelPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosTunnelPassPackets.setStatus("current")
_HwhqosTunnelDropBytes_Type = Counter64
_HwhqosTunnelDropBytes_Object = MibTableColumn
hwhqosTunnelDropBytes = _HwhqosTunnelDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9, 1, 7),
    _HwhqosTunnelDropBytes_Type()
)
hwhqosTunnelDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosTunnelDropBytes.setStatus("current")
_HwhqosTunnelDropPackets_Type = Counter64
_HwhqosTunnelDropPackets_Object = MibTableColumn
hwhqosTunnelDropPackets = _HwhqosTunnelDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9, 1, 8),
    _HwhqosTunnelDropPackets_Type()
)
hwhqosTunnelDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosTunnelDropPackets.setStatus("current")
_HwhqosTunnelPassedByteRate_Type = Counter64
_HwhqosTunnelPassedByteRate_Object = MibTableColumn
hwhqosTunnelPassedByteRate = _HwhqosTunnelPassedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9, 1, 9),
    _HwhqosTunnelPassedByteRate_Type()
)
hwhqosTunnelPassedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosTunnelPassedByteRate.setStatus("current")
_HwhqosTunnelPassPacketRate_Type = Counter64
_HwhqosTunnelPassPacketRate_Object = MibTableColumn
hwhqosTunnelPassPacketRate = _HwhqosTunnelPassPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 9, 1, 10),
    _HwhqosTunnelPassPacketRate_Type()
)
hwhqosTunnelPassPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosTunnelPassPacketRate.setStatus("current")
_HwhqosProfileTable_Object = MibTable
hwhqosProfileTable = _HwhqosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 10)
)
if mibBuilder.loadTexts:
    hwhqosProfileTable.setStatus("current")
_HwhqosProfileEntry_Object = MibTableRow
hwhqosProfileEntry = _HwhqosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 10, 1)
)
hwhqosProfileEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileName"),
)
if mibBuilder.loadTexts:
    hwhqosProfileEntry.setStatus("current")


class _HwhqosProfileName_Type(OctetString):
    """Custom type hwhqosProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwhqosProfileName_Type.__name__ = "OctetString"
_HwhqosProfileName_Object = MibTableColumn
hwhqosProfileName = _HwhqosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 10, 1, 1),
    _HwhqosProfileName_Type()
)
hwhqosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileName.setStatus("current")


class _HwhqosProfileDescription_Type(OctetString):
    """Custom type hwhqosProfileDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwhqosProfileDescription_Type.__name__ = "OctetString"
_HwhqosProfileDescription_Object = MibTableColumn
hwhqosProfileDescription = _HwhqosProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 10, 1, 2),
    _HwhqosProfileDescription_Type()
)
hwhqosProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileDescription.setStatus("current")
_HwhqosProfileRowStatus_Type = RowStatus
_HwhqosProfileRowStatus_Object = MibTableColumn
hwhqosProfileRowStatus = _HwhqosProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 10, 1, 50),
    _HwhqosProfileRowStatus_Type()
)
hwhqosProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileRowStatus.setStatus("current")
_HwhqosProfileSuppressionTable_Object = MibTable
hwhqosProfileSuppressionTable = _HwhqosProfileSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 11)
)
if mibBuilder.loadTexts:
    hwhqosProfileSuppressionTable.setStatus("current")
_HwhqosProfileSuppressionEntry_Object = MibTableRow
hwhqosProfileSuppressionEntry = _HwhqosProfileSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 11, 1)
)
hwhqosProfileSuppressionEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosSuppressionDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosSuppressionType"),
)
if mibBuilder.loadTexts:
    hwhqosProfileSuppressionEntry.setStatus("current")


class _HwhqosSuppressionDirection_Type(Integer32):
    """Custom type hwhqosSuppressionDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("inout", 3),
          ("outbound", 2))
    )


_HwhqosSuppressionDirection_Type.__name__ = "Integer32"
_HwhqosSuppressionDirection_Object = MibTableColumn
hwhqosSuppressionDirection = _HwhqosSuppressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 11, 1, 1),
    _HwhqosSuppressionDirection_Type()
)
hwhqosSuppressionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosSuppressionDirection.setStatus("current")


class _HwhqosSuppressionType_Type(Integer32):
    """Custom type hwhqosSuppressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2),
          ("unkonwnUnicast", 3))
    )


_HwhqosSuppressionType_Type.__name__ = "Integer32"
_HwhqosSuppressionType_Object = MibTableColumn
hwhqosSuppressionType = _HwhqosSuppressionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 11, 1, 2),
    _HwhqosSuppressionType_Type()
)
hwhqosSuppressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosSuppressionType.setStatus("current")


class _HwhqosSuppressionCirValue_Type(Integer32):
    """Custom type hwhqosSuppressionCirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_HwhqosSuppressionCirValue_Type.__name__ = "Integer32"
_HwhqosSuppressionCirValue_Object = MibTableColumn
hwhqosSuppressionCirValue = _HwhqosSuppressionCirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 11, 1, 3),
    _HwhqosSuppressionCirValue_Type()
)
hwhqosSuppressionCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosSuppressionCirValue.setStatus("current")


class _HwhqosSuppressionCbsValue_Type(Integer32):
    """Custom type hwhqosSuppressionCbsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 33554432),
    )


_HwhqosSuppressionCbsValue_Type.__name__ = "Integer32"
_HwhqosSuppressionCbsValue_Object = MibTableColumn
hwhqosSuppressionCbsValue = _HwhqosSuppressionCbsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 11, 1, 4),
    _HwhqosSuppressionCbsValue_Type()
)
hwhqosSuppressionCbsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosSuppressionCbsValue.setStatus("current")
_HwhqosSuppressionRowStatus_Type = RowStatus
_HwhqosSuppressionRowStatus_Object = MibTableColumn
hwhqosSuppressionRowStatus = _HwhqosSuppressionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 11, 1, 50),
    _HwhqosSuppressionRowStatus_Type()
)
hwhqosSuppressionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosSuppressionRowStatus.setStatus("current")
_HwhqosProfileCarTable_Object = MibTable
hwhqosProfileCarTable = _HwhqosProfileCarTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 12)
)
if mibBuilder.loadTexts:
    hwhqosProfileCarTable.setStatus("current")
_HwhqosProfileCarEntry_Object = MibTableRow
hwhqosProfileCarEntry = _HwhqosProfileCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 12, 1)
)
hwhqosProfileCarEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileCarDirection"),
)
if mibBuilder.loadTexts:
    hwhqosProfileCarEntry.setStatus("current")


class _HwhqosProfileCarDirection_Type(Integer32):
    """Custom type hwhqosProfileCarDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("inout", 3),
          ("outbound", 2))
    )


_HwhqosProfileCarDirection_Type.__name__ = "Integer32"
_HwhqosProfileCarDirection_Object = MibTableColumn
hwhqosProfileCarDirection = _HwhqosProfileCarDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 12, 1, 1),
    _HwhqosProfileCarDirection_Type()
)
hwhqosProfileCarDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarDirection.setStatus("current")


class _HwhqosProfileCarCirValue_Type(Unsigned32):
    """Custom type hwhqosProfileCarCirValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwhqosProfileCarCirValue_Type.__name__ = "Unsigned32"
_HwhqosProfileCarCirValue_Object = MibTableColumn
hwhqosProfileCarCirValue = _HwhqosProfileCarCirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 12, 1, 2),
    _HwhqosProfileCarCirValue_Type()
)
hwhqosProfileCarCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileCarCirValue.setStatus("current")


class _HwhqosProfileCarPirValue_Type(Unsigned32):
    """Custom type hwhqosProfileCarPirValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwhqosProfileCarPirValue_Type.__name__ = "Unsigned32"
_HwhqosProfileCarPirValue_Object = MibTableColumn
hwhqosProfileCarPirValue = _HwhqosProfileCarPirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 12, 1, 3),
    _HwhqosProfileCarPirValue_Type()
)
hwhqosProfileCarPirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileCarPirValue.setStatus("current")


class _HwhqosProfileCarCbsValue_Type(Unsigned32):
    """Custom type hwhqosProfileCarCbsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwhqosProfileCarCbsValue_Type.__name__ = "Unsigned32"
_HwhqosProfileCarCbsValue_Object = MibTableColumn
hwhqosProfileCarCbsValue = _HwhqosProfileCarCbsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 12, 1, 4),
    _HwhqosProfileCarCbsValue_Type()
)
hwhqosProfileCarCbsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileCarCbsValue.setStatus("current")


class _HwhqosProfileCarPbsValue_Type(Unsigned32):
    """Custom type hwhqosProfileCarPbsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwhqosProfileCarPbsValue_Type.__name__ = "Unsigned32"
_HwhqosProfileCarPbsValue_Object = MibTableColumn
hwhqosProfileCarPbsValue = _HwhqosProfileCarPbsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 12, 1, 5),
    _HwhqosProfileCarPbsValue_Type()
)
hwhqosProfileCarPbsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileCarPbsValue.setStatus("current")


class _HwhqosProfileCarGreenAction_Type(Integer32):
    """Custom type hwhqosProfileCarGreenAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("pass", 1))
    )


_HwhqosProfileCarGreenAction_Type.__name__ = "Integer32"
_HwhqosProfileCarGreenAction_Object = MibTableColumn
hwhqosProfileCarGreenAction = _HwhqosProfileCarGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 12, 1, 6),
    _HwhqosProfileCarGreenAction_Type()
)
hwhqosProfileCarGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileCarGreenAction.setStatus("current")


class _HwhqosProfileCarYellowAction_Type(Integer32):
    """Custom type hwhqosProfileCarYellowAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("pass", 1))
    )


_HwhqosProfileCarYellowAction_Type.__name__ = "Integer32"
_HwhqosProfileCarYellowAction_Object = MibTableColumn
hwhqosProfileCarYellowAction = _HwhqosProfileCarYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 12, 1, 7),
    _HwhqosProfileCarYellowAction_Type()
)
hwhqosProfileCarYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileCarYellowAction.setStatus("current")


class _HwhqosProfileCarRedAction_Type(Integer32):
    """Custom type hwhqosProfileCarRedAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("pass", 1))
    )


_HwhqosProfileCarRedAction_Type.__name__ = "Integer32"
_HwhqosProfileCarRedAction_Object = MibTableColumn
hwhqosProfileCarRedAction = _HwhqosProfileCarRedAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 12, 1, 8),
    _HwhqosProfileCarRedAction_Type()
)
hwhqosProfileCarRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileCarRedAction.setStatus("current")
_HwhqosProfileCarRowStatus_Type = RowStatus
_HwhqosProfileCarRowStatus_Object = MibTableColumn
hwhqosProfileCarRowStatus = _HwhqosProfileCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 12, 1, 50),
    _HwhqosProfileCarRowStatus_Type()
)
hwhqosProfileCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileCarRowStatus.setStatus("current")
_HwhqosProfileUserQueueTable_Object = MibTable
hwhqosProfileUserQueueTable = _HwhqosProfileUserQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 13)
)
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueTable.setStatus("current")
_HwhqosProfileUserQueueEntry_Object = MibTableRow
hwhqosProfileUserQueueEntry = _HwhqosProfileUserQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 13, 1)
)
hwhqosProfileUserQueueEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueDirection"),
)
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueEntry.setStatus("current")


class _HwhqosProfileUserQueueDirection_Type(Integer32):
    """Custom type hwhqosProfileUserQueueDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("inout", 3),
          ("outbound", 2))
    )


_HwhqosProfileUserQueueDirection_Type.__name__ = "Integer32"
_HwhqosProfileUserQueueDirection_Object = MibTableColumn
hwhqosProfileUserQueueDirection = _HwhqosProfileUserQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 13, 1, 1),
    _HwhqosProfileUserQueueDirection_Type()
)
hwhqosProfileUserQueueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueDirection.setStatus("current")


class _HwhqosProfileUserQueueCirValue_Type(Integer32):
    """Custom type hwhqosProfileUserQueueCirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 10000000),
    )


_HwhqosProfileUserQueueCirValue_Type.__name__ = "Integer32"
_HwhqosProfileUserQueueCirValue_Object = MibTableColumn
hwhqosProfileUserQueueCirValue = _HwhqosProfileUserQueueCirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 13, 1, 2),
    _HwhqosProfileUserQueueCirValue_Type()
)
hwhqosProfileUserQueueCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueCirValue.setStatus("current")


class _HwhqosProfileUserQueuePirValue_Type(Integer32):
    """Custom type hwhqosProfileUserQueuePirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 10000000),
    )


_HwhqosProfileUserQueuePirValue_Type.__name__ = "Integer32"
_HwhqosProfileUserQueuePirValue_Object = MibTableColumn
hwhqosProfileUserQueuePirValue = _HwhqosProfileUserQueuePirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 13, 1, 3),
    _HwhqosProfileUserQueuePirValue_Type()
)
hwhqosProfileUserQueuePirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueuePirValue.setStatus("current")


class _HwhqosProfileUserQueueFlowQueueName_Type(OctetString):
    """Custom type hwhqosProfileUserQueueFlowQueueName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosProfileUserQueueFlowQueueName_Type.__name__ = "OctetString"
_HwhqosProfileUserQueueFlowQueueName_Object = MibTableColumn
hwhqosProfileUserQueueFlowQueueName = _HwhqosProfileUserQueueFlowQueueName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 13, 1, 4),
    _HwhqosProfileUserQueueFlowQueueName_Type()
)
hwhqosProfileUserQueueFlowQueueName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueFlowQueueName.setStatus("current")


class _HwhqosProfileUserQueueMappingName_Type(OctetString):
    """Custom type hwhqosProfileUserQueueMappingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosProfileUserQueueMappingName_Type.__name__ = "OctetString"
_HwhqosProfileUserQueueMappingName_Object = MibTableColumn
hwhqosProfileUserQueueMappingName = _HwhqosProfileUserQueueMappingName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 13, 1, 5),
    _HwhqosProfileUserQueueMappingName_Type()
)
hwhqosProfileUserQueueMappingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueMappingName.setStatus("current")


class _HwhqosProfileUserQueueGroupName_Type(OctetString):
    """Custom type hwhqosProfileUserQueueGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosProfileUserQueueGroupName_Type.__name__ = "OctetString"
_HwhqosProfileUserQueueGroupName_Object = MibTableColumn
hwhqosProfileUserQueueGroupName = _HwhqosProfileUserQueueGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 13, 1, 6),
    _HwhqosProfileUserQueueGroupName_Type()
)
hwhqosProfileUserQueueGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueGroupName.setStatus("current")


class _HwhqosProfileUserQueueServiceTemplateName_Type(OctetString):
    """Custom type hwhqosProfileUserQueueServiceTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosProfileUserQueueServiceTemplateName_Type.__name__ = "OctetString"
_HwhqosProfileUserQueueServiceTemplateName_Object = MibTableColumn
hwhqosProfileUserQueueServiceTemplateName = _HwhqosProfileUserQueueServiceTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 13, 1, 7),
    _HwhqosProfileUserQueueServiceTemplateName_Type()
)
hwhqosProfileUserQueueServiceTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueServiceTemplateName.setStatus("current")
_HwhqosProfileUserQueueRowStatus_Type = RowStatus
_HwhqosProfileUserQueueRowStatus_Object = MibTableColumn
hwhqosProfileUserQueueRowStatus = _HwhqosProfileUserQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 13, 1, 50),
    _HwhqosProfileUserQueueRowStatus_Type()
)
hwhqosProfileUserQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueRowStatus.setStatus("current")
_HwhqosProfileApplyTable_Object = MibTable
hwhqosProfileApplyTable = _HwhqosProfileApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 14)
)
if mibBuilder.loadTexts:
    hwhqosProfileApplyTable.setStatus("current")
_HwhqosProfileApplyEntry_Object = MibTableRow
hwhqosProfileApplyEntry = _HwhqosProfileApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 14, 1)
)
hwhqosProfileApplyEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileApplyDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileApplyPevid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileApplyCevid"),
)
if mibBuilder.loadTexts:
    hwhqosProfileApplyEntry.setStatus("current")
_HwhqosProfileInterfaceIndex_Type = InterfaceIndex
_HwhqosProfileInterfaceIndex_Object = MibTableColumn
hwhqosProfileInterfaceIndex = _HwhqosProfileInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 14, 1, 1),
    _HwhqosProfileInterfaceIndex_Type()
)
hwhqosProfileInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileInterfaceIndex.setStatus("current")


class _HwhqosProfileApplyDirection_Type(Integer32):
    """Custom type hwhqosProfileApplyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosProfileApplyDirection_Type.__name__ = "Integer32"
_HwhqosProfileApplyDirection_Object = MibTableColumn
hwhqosProfileApplyDirection = _HwhqosProfileApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 14, 1, 2),
    _HwhqosProfileApplyDirection_Type()
)
hwhqosProfileApplyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileApplyDirection.setStatus("current")


class _HwhqosProfileApplyPevid_Type(Integer32):
    """Custom type hwhqosProfileApplyPevid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwhqosProfileApplyPevid_Type.__name__ = "Integer32"
_HwhqosProfileApplyPevid_Object = MibTableColumn
hwhqosProfileApplyPevid = _HwhqosProfileApplyPevid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 14, 1, 3),
    _HwhqosProfileApplyPevid_Type()
)
hwhqosProfileApplyPevid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileApplyPevid.setStatus("current")


class _HwhqosProfileApplyCevid_Type(Integer32):
    """Custom type hwhqosProfileApplyCevid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwhqosProfileApplyCevid_Type.__name__ = "Integer32"
_HwhqosProfileApplyCevid_Object = MibTableColumn
hwhqosProfileApplyCevid = _HwhqosProfileApplyCevid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 14, 1, 4),
    _HwhqosProfileApplyCevid_Type()
)
hwhqosProfileApplyCevid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileApplyCevid.setStatus("current")


class _HwhqosProfileApplyName_Type(OctetString):
    """Custom type hwhqosProfileApplyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwhqosProfileApplyName_Type.__name__ = "OctetString"
_HwhqosProfileApplyName_Object = MibTableColumn
hwhqosProfileApplyName = _HwhqosProfileApplyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 14, 1, 5),
    _HwhqosProfileApplyName_Type()
)
hwhqosProfileApplyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileApplyName.setStatus("current")


class _HwhqosProfileApplyIdentifier_Type(Integer32):
    """Custom type hwhqosProfileApplyIdentifier based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ceVid", 3),
          ("none", 1),
          ("peCeVid", 5),
          ("peVid", 4),
          ("vlanId", 2))
    )


_HwhqosProfileApplyIdentifier_Type.__name__ = "Integer32"
_HwhqosProfileApplyIdentifier_Object = MibTableColumn
hwhqosProfileApplyIdentifier = _HwhqosProfileApplyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 14, 1, 6),
    _HwhqosProfileApplyIdentifier_Type()
)
hwhqosProfileApplyIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileApplyIdentifier.setStatus("current")


class _HwhqosGroupName_Type(OctetString):
    """Custom type hwhqosGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosGroupName_Type.__name__ = "OctetString"
_HwhqosGroupName_Object = MibTableColumn
hwhqosGroupName = _HwhqosGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 14, 1, 7),
    _HwhqosGroupName_Type()
)
hwhqosGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosGroupName.setStatus("current")
_HwhqosProfileApplyRowStatus_Type = RowStatus
_HwhqosProfileApplyRowStatus_Object = MibTableColumn
hwhqosProfileApplyRowStatus = _HwhqosProfileApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 14, 1, 50),
    _HwhqosProfileApplyRowStatus_Type()
)
hwhqosProfileApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileApplyRowStatus.setStatus("current")
_HwhqosFlowMappingTable_Object = MibTable
hwhqosFlowMappingTable = _HwhqosFlowMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 15)
)
if mibBuilder.loadTexts:
    hwhqosFlowMappingTable.setStatus("current")
_HwhqosFlowMappingEntry_Object = MibTableRow
hwhqosFlowMappingEntry = _HwhqosFlowMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 15, 1)
)
hwhqosFlowMappingEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosFlowMappingName"),
)
if mibBuilder.loadTexts:
    hwhqosFlowMappingEntry.setStatus("current")


class _HwhqosFlowMappingName_Type(OctetString):
    """Custom type hwhqosFlowMappingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosFlowMappingName_Type.__name__ = "OctetString"
_HwhqosFlowMappingName_Object = MibTableColumn
hwhqosFlowMappingName = _HwhqosFlowMappingName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 15, 1, 1),
    _HwhqosFlowMappingName_Type()
)
hwhqosFlowMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosFlowMappingName.setStatus("current")
_HwhqosFlowMappingRowStatus_Type = RowStatus
_HwhqosFlowMappingRowStatus_Object = MibTableColumn
hwhqosFlowMappingRowStatus = _HwhqosFlowMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 15, 1, 50),
    _HwhqosFlowMappingRowStatus_Type()
)
hwhqosFlowMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowMappingRowStatus.setStatus("current")
_HwhqosFlowMappingCfgTable_Object = MibTable
hwhqosFlowMappingCfgTable = _HwhqosFlowMappingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 16)
)
if mibBuilder.loadTexts:
    hwhqosFlowMappingCfgTable.setStatus("current")
_HwhqosFlowMappingCfgEntry_Object = MibTableRow
hwhqosFlowMappingCfgEntry = _HwhqosFlowMappingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 16, 1)
)
hwhqosFlowMappingCfgEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosFlowMappingName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosFolwMappingCfgQueueCosValue"),
)
if mibBuilder.loadTexts:
    hwhqosFlowMappingCfgEntry.setStatus("current")


class _HwhqosFolwMappingCfgQueueCosValue_Type(Integer32):
    """Custom type hwhqosFolwMappingCfgQueueCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwhqosFolwMappingCfgQueueCosValue_Type.__name__ = "Integer32"
_HwhqosFolwMappingCfgQueueCosValue_Object = MibTableColumn
hwhqosFolwMappingCfgQueueCosValue = _HwhqosFolwMappingCfgQueueCosValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 16, 1, 1),
    _HwhqosFolwMappingCfgQueueCosValue_Type()
)
hwhqosFolwMappingCfgQueueCosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosFolwMappingCfgQueueCosValue.setStatus("current")


class _HwhqosFlowMappingCfgPortQueueCosValue_Type(Integer32):
    """Custom type hwhqosFlowMappingCfgPortQueueCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwhqosFlowMappingCfgPortQueueCosValue_Type.__name__ = "Integer32"
_HwhqosFlowMappingCfgPortQueueCosValue_Object = MibTableColumn
hwhqosFlowMappingCfgPortQueueCosValue = _HwhqosFlowMappingCfgPortQueueCosValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 16, 1, 2),
    _HwhqosFlowMappingCfgPortQueueCosValue_Type()
)
hwhqosFlowMappingCfgPortQueueCosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowMappingCfgPortQueueCosValue.setStatus("current")
_HwhqosFlowMappingCfgRowStatus_Type = RowStatus
_HwhqosFlowMappingCfgRowStatus_Object = MibTableColumn
hwhqosFlowMappingCfgRowStatus = _HwhqosFlowMappingCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 16, 1, 50),
    _HwhqosFlowMappingCfgRowStatus_Type()
)
hwhqosFlowMappingCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowMappingCfgRowStatus.setStatus("current")
_HwhqosFlowQueueTable_Object = MibTable
hwhqosFlowQueueTable = _HwhqosFlowQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 17)
)
if mibBuilder.loadTexts:
    hwhqosFlowQueueTable.setStatus("current")
_HwhqosFlowQueueEntry_Object = MibTableRow
hwhqosFlowQueueEntry = _HwhqosFlowQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 17, 1)
)
hwhqosFlowQueueEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosFlowQueueName"),
)
if mibBuilder.loadTexts:
    hwhqosFlowQueueEntry.setStatus("current")


class _HwhqosFlowQueueName_Type(OctetString):
    """Custom type hwhqosFlowQueueName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosFlowQueueName_Type.__name__ = "OctetString"
_HwhqosFlowQueueName_Object = MibTableColumn
hwhqosFlowQueueName = _HwhqosFlowQueueName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 17, 1, 1),
    _HwhqosFlowQueueName_Type()
)
hwhqosFlowQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosFlowQueueName.setStatus("current")
_HwhqosFlowQueueRowStatus_Type = RowStatus
_HwhqosFlowQueueRowStatus_Object = MibTableColumn
hwhqosFlowQueueRowStatus = _HwhqosFlowQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 17, 1, 50),
    _HwhqosFlowQueueRowStatus_Type()
)
hwhqosFlowQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueRowStatus.setStatus("current")
_HwhqosFlowQueueCfgTable_Object = MibTable
hwhqosFlowQueueCfgTable = _HwhqosFlowQueueCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 18)
)
if mibBuilder.loadTexts:
    hwhqosFlowQueueCfgTable.setStatus("current")
_HwhqosFlowQueueCfgEntry_Object = MibTableRow
hwhqosFlowQueueCfgEntry = _HwhqosFlowQueueCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 18, 1)
)
hwhqosFlowQueueCfgEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosFlowQueueName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosFlowQueueCfgCosValue"),
)
if mibBuilder.loadTexts:
    hwhqosFlowQueueCfgEntry.setStatus("current")


class _HwhqosFlowQueueCfgCosValue_Type(Integer32):
    """Custom type hwhqosFlowQueueCfgCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwhqosFlowQueueCfgCosValue_Type.__name__ = "Integer32"
_HwhqosFlowQueueCfgCosValue_Object = MibTableColumn
hwhqosFlowQueueCfgCosValue = _HwhqosFlowQueueCfgCosValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 18, 1, 1),
    _HwhqosFlowQueueCfgCosValue_Type()
)
hwhqosFlowQueueCfgCosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueCfgCosValue.setStatus("current")


class _HwhqosFlowQueueCfgType_Type(Integer32):
    """Custom type hwhqosFlowQueueCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lpq", 3),
          ("pq", 1),
          ("wfq", 2))
    )


_HwhqosFlowQueueCfgType_Type.__name__ = "Integer32"
_HwhqosFlowQueueCfgType_Object = MibTableColumn
hwhqosFlowQueueCfgType = _HwhqosFlowQueueCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 18, 1, 2),
    _HwhqosFlowQueueCfgType_Type()
)
hwhqosFlowQueueCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueCfgType.setStatus("current")


class _HwhqosFlowQueueCfgWeightValue_Type(Integer32):
    """Custom type hwhqosFlowQueueCfgWeightValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_HwhqosFlowQueueCfgWeightValue_Type.__name__ = "Integer32"
_HwhqosFlowQueueCfgWeightValue_Object = MibTableColumn
hwhqosFlowQueueCfgWeightValue = _HwhqosFlowQueueCfgWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 18, 1, 3),
    _HwhqosFlowQueueCfgWeightValue_Type()
)
hwhqosFlowQueueCfgWeightValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueCfgWeightValue.setStatus("current")


class _HwhqosFlowQueueCfgShapingValue_Type(Unsigned32):
    """Custom type hwhqosFlowQueueCfgShapingValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 4294967295),
    )


_HwhqosFlowQueueCfgShapingValue_Type.__name__ = "Unsigned32"
_HwhqosFlowQueueCfgShapingValue_Object = MibTableColumn
hwhqosFlowQueueCfgShapingValue = _HwhqosFlowQueueCfgShapingValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 18, 1, 4),
    _HwhqosFlowQueueCfgShapingValue_Type()
)
hwhqosFlowQueueCfgShapingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueCfgShapingValue.setStatus("current")


class _HwhqosFlowQueueCfgShapingPercentageValue_Type(Integer32):
    """Custom type hwhqosFlowQueueCfgShapingPercentageValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_HwhqosFlowQueueCfgShapingPercentageValue_Type.__name__ = "Integer32"
_HwhqosFlowQueueCfgShapingPercentageValue_Object = MibTableColumn
hwhqosFlowQueueCfgShapingPercentageValue = _HwhqosFlowQueueCfgShapingPercentageValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 18, 1, 5),
    _HwhqosFlowQueueCfgShapingPercentageValue_Type()
)
hwhqosFlowQueueCfgShapingPercentageValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueCfgShapingPercentageValue.setStatus("current")


class _HwhqosFlowQueueCfgWredName_Type(OctetString):
    """Custom type hwhqosFlowQueueCfgWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosFlowQueueCfgWredName_Type.__name__ = "OctetString"
_HwhqosFlowQueueCfgWredName_Object = MibTableColumn
hwhqosFlowQueueCfgWredName = _HwhqosFlowQueueCfgWredName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 18, 1, 6),
    _HwhqosFlowQueueCfgWredName_Type()
)
hwhqosFlowQueueCfgWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueCfgWredName.setStatus("current")


class _HwhqosFlowQueueCfgPbsValue_Type(Integer32):
    """Custom type hwhqosFlowQueueCfgPbsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4194304),
    )


_HwhqosFlowQueueCfgPbsValue_Type.__name__ = "Integer32"
_HwhqosFlowQueueCfgPbsValue_Object = MibTableColumn
hwhqosFlowQueueCfgPbsValue = _HwhqosFlowQueueCfgPbsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 18, 1, 7),
    _HwhqosFlowQueueCfgPbsValue_Type()
)
hwhqosFlowQueueCfgPbsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueCfgPbsValue.setStatus("current")
_HwhqosFlowQueueCfgRowStatus_Type = RowStatus
_HwhqosFlowQueueCfgRowStatus_Object = MibTableColumn
hwhqosFlowQueueCfgRowStatus = _HwhqosFlowQueueCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 18, 1, 50),
    _HwhqosFlowQueueCfgRowStatus_Type()
)
hwhqosFlowQueueCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueCfgRowStatus.setStatus("current")
_HwhqosFlowWredTable_Object = MibTable
hwhqosFlowWredTable = _HwhqosFlowWredTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 19)
)
if mibBuilder.loadTexts:
    hwhqosFlowWredTable.setStatus("current")
_HwhqosFlowWredEntry_Object = MibTableRow
hwhqosFlowWredEntry = _HwhqosFlowWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 19, 1)
)
hwhqosFlowWredEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosFlowWredName"),
)
if mibBuilder.loadTexts:
    hwhqosFlowWredEntry.setStatus("current")


class _HwhqosFlowWredName_Type(OctetString):
    """Custom type hwhqosFlowWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosFlowWredName_Type.__name__ = "OctetString"
_HwhqosFlowWredName_Object = MibTableColumn
hwhqosFlowWredName = _HwhqosFlowWredName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 19, 1, 1),
    _HwhqosFlowWredName_Type()
)
hwhqosFlowWredName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosFlowWredName.setStatus("current")
_HwhqosFlowWredRowStatus_Type = RowStatus
_HwhqosFlowWredRowStatus_Object = MibTableColumn
hwhqosFlowWredRowStatus = _HwhqosFlowWredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 19, 1, 50),
    _HwhqosFlowWredRowStatus_Type()
)
hwhqosFlowWredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowWredRowStatus.setStatus("current")
_HwhqosFlowWredColorTable_Object = MibTable
hwhqosFlowWredColorTable = _HwhqosFlowWredColorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 20)
)
if mibBuilder.loadTexts:
    hwhqosFlowWredColorTable.setStatus("current")
_HwhqosFlowWredColorEntry_Object = MibTableRow
hwhqosFlowWredColorEntry = _HwhqosFlowWredColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 20, 1)
)
hwhqosFlowWredColorEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosFlowWredName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosFlowWredColor"),
)
if mibBuilder.loadTexts:
    hwhqosFlowWredColorEntry.setStatus("current")


class _HwhqosFlowWredColor_Type(Integer32):
    """Custom type hwhqosFlowWredColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )


_HwhqosFlowWredColor_Type.__name__ = "Integer32"
_HwhqosFlowWredColor_Object = MibTableColumn
hwhqosFlowWredColor = _HwhqosFlowWredColor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 20, 1, 1),
    _HwhqosFlowWredColor_Type()
)
hwhqosFlowWredColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosFlowWredColor.setStatus("current")


class _HwhqosFlowWredColorLowlimitPercentage_Type(Integer32):
    """Custom type hwhqosFlowWredColorLowlimitPercentage based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwhqosFlowWredColorLowlimitPercentage_Type.__name__ = "Integer32"
_HwhqosFlowWredColorLowlimitPercentage_Object = MibTableColumn
hwhqosFlowWredColorLowlimitPercentage = _HwhqosFlowWredColorLowlimitPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 20, 1, 2),
    _HwhqosFlowWredColorLowlimitPercentage_Type()
)
hwhqosFlowWredColorLowlimitPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowWredColorLowlimitPercentage.setStatus("current")


class _HwhqosFlowWredColorHighlimitPercentage_Type(Integer32):
    """Custom type hwhqosFlowWredColorHighlimitPercentage based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwhqosFlowWredColorHighlimitPercentage_Type.__name__ = "Integer32"
_HwhqosFlowWredColorHighlimitPercentage_Object = MibTableColumn
hwhqosFlowWredColorHighlimitPercentage = _HwhqosFlowWredColorHighlimitPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 20, 1, 3),
    _HwhqosFlowWredColorHighlimitPercentage_Type()
)
hwhqosFlowWredColorHighlimitPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowWredColorHighlimitPercentage.setStatus("current")


class _HwhqosFlowWredColorDiscardPercentage_Type(Integer32):
    """Custom type hwhqosFlowWredColorDiscardPercentage based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwhqosFlowWredColorDiscardPercentage_Type.__name__ = "Integer32"
_HwhqosFlowWredColorDiscardPercentage_Object = MibTableColumn
hwhqosFlowWredColorDiscardPercentage = _HwhqosFlowWredColorDiscardPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 20, 1, 4),
    _HwhqosFlowWredColorDiscardPercentage_Type()
)
hwhqosFlowWredColorDiscardPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowWredColorDiscardPercentage.setStatus("current")
_HwhqosFlowWredColorRowStatus_Type = RowStatus
_HwhqosFlowWredColorRowStatus_Object = MibTableColumn
hwhqosFlowWredColorRowStatus = _HwhqosFlowWredColorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 20, 1, 50),
    _HwhqosFlowWredColorRowStatus_Type()
)
hwhqosFlowWredColorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowWredColorRowStatus.setStatus("current")
_HwhqosUserGroupQueueTable_Object = MibTable
hwhqosUserGroupQueueTable = _HwhqosUserGroupQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 21)
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueTable.setStatus("current")
_HwhqosUserGroupQueueEntry_Object = MibTableRow
hwhqosUserGroupQueueEntry = _HwhqosUserGroupQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 21, 1)
)
hwhqosUserGroupQueueEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueName"),
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueEntry.setStatus("current")


class _HwhqosUserGroupQueueName_Type(OctetString):
    """Custom type hwhqosUserGroupQueueName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosUserGroupQueueName_Type.__name__ = "OctetString"
_HwhqosUserGroupQueueName_Object = MibTableColumn
hwhqosUserGroupQueueName = _HwhqosUserGroupQueueName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 21, 1, 1),
    _HwhqosUserGroupQueueName_Type()
)
hwhqosUserGroupQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueName.setStatus("current")


class _HwhqosUserGroupQueueSlotNumber_Type(Integer32):
    """Custom type hwhqosUserGroupQueueSlotNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_HwhqosUserGroupQueueSlotNumber_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueSlotNumber_Object = MibTableColumn
hwhqosUserGroupQueueSlotNumber = _HwhqosUserGroupQueueSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 21, 1, 2),
    _HwhqosUserGroupQueueSlotNumber_Type()
)
hwhqosUserGroupQueueSlotNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueSlotNumber.setStatus("current")
_HwhqosUserGroupQueueRowStatus_Type = RowStatus
_HwhqosUserGroupQueueRowStatus_Object = MibTableColumn
hwhqosUserGroupQueueRowStatus = _HwhqosUserGroupQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 21, 1, 50),
    _HwhqosUserGroupQueueRowStatus_Type()
)
hwhqosUserGroupQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueRowStatus.setStatus("current")
_HwhqosUserGroupQueueShapingTable_Object = MibTable
hwhqosUserGroupQueueShapingTable = _HwhqosUserGroupQueueShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 22)
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueShapingTable.setStatus("current")
_HwhqosUserGroupQueueShapingEntry_Object = MibTableRow
hwhqosUserGroupQueueShapingEntry = _HwhqosUserGroupQueueShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 22, 1)
)
hwhqosUserGroupQueueShapingEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueShapingDirection"),
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueShapingEntry.setStatus("current")


class _HwhqosUserGroupQueueShapingDirection_Type(Integer32):
    """Custom type hwhqosUserGroupQueueShapingDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosUserGroupQueueShapingDirection_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueShapingDirection_Object = MibTableColumn
hwhqosUserGroupQueueShapingDirection = _HwhqosUserGroupQueueShapingDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 22, 1, 1),
    _HwhqosUserGroupQueueShapingDirection_Type()
)
hwhqosUserGroupQueueShapingDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueShapingDirection.setStatus("current")


class _HwhqosUserGroupQueueShapingValue_Type(Integer32):
    """Custom type hwhqosUserGroupQueueShapingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(66, 10000000),
    )


_HwhqosUserGroupQueueShapingValue_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueShapingValue_Object = MibTableColumn
hwhqosUserGroupQueueShapingValue = _HwhqosUserGroupQueueShapingValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 22, 1, 2),
    _HwhqosUserGroupQueueShapingValue_Type()
)
hwhqosUserGroupQueueShapingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueShapingValue.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueShapingValue.setUnits("Kbps")


class _HwhqosUserGroupQueuePbsValue_Type(Integer32):
    """Custom type hwhqosUserGroupQueuePbsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2097152),
    )


_HwhqosUserGroupQueuePbsValue_Type.__name__ = "Integer32"
_HwhqosUserGroupQueuePbsValue_Object = MibTableColumn
hwhqosUserGroupQueuePbsValue = _HwhqosUserGroupQueuePbsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 22, 1, 3),
    _HwhqosUserGroupQueuePbsValue_Type()
)
hwhqosUserGroupQueuePbsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueuePbsValue.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueuePbsValue.setUnits("bytes")
_HwhqosUserGroupQueueShapingRowStatus_Type = RowStatus
_HwhqosUserGroupQueueShapingRowStatus_Object = MibTableColumn
hwhqosUserGroupQueueShapingRowStatus = _HwhqosUserGroupQueueShapingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 22, 1, 50),
    _HwhqosUserGroupQueueShapingRowStatus_Type()
)
hwhqosUserGroupQueueShapingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueShapingRowStatus.setStatus("current")
_HwhqosUserQueueTable_Object = MibTable
hwhqosUserQueueTable = _HwhqosUserQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 23)
)
if mibBuilder.loadTexts:
    hwhqosUserQueueTable.setStatus("current")
_HwhqosUserQueueEntry_Object = MibTableRow
hwhqosUserQueueEntry = _HwhqosUserQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 23, 1)
)
hwhqosUserQueueEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueDirection"),
)
if mibBuilder.loadTexts:
    hwhqosUserQueueEntry.setStatus("current")
_HwhqosUserQueueInterfaceIndex_Type = InterfaceIndex
_HwhqosUserQueueInterfaceIndex_Object = MibTableColumn
hwhqosUserQueueInterfaceIndex = _HwhqosUserQueueInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 23, 1, 1),
    _HwhqosUserQueueInterfaceIndex_Type()
)
hwhqosUserQueueInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueInterfaceIndex.setStatus("current")


class _HwhqosUserQueueDirection_Type(Integer32):
    """Custom type hwhqosUserQueueDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosUserQueueDirection_Type.__name__ = "Integer32"
_HwhqosUserQueueDirection_Object = MibTableColumn
hwhqosUserQueueDirection = _HwhqosUserQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 23, 1, 2),
    _HwhqosUserQueueDirection_Type()
)
hwhqosUserQueueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueDirection.setStatus("current")


class _HwhqosUserQueueCirValue_Type(Integer32):
    """Custom type hwhqosUserQueueCirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1000000),
    )


_HwhqosUserQueueCirValue_Type.__name__ = "Integer32"
_HwhqosUserQueueCirValue_Object = MibTableColumn
hwhqosUserQueueCirValue = _HwhqosUserQueueCirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 23, 1, 3),
    _HwhqosUserQueueCirValue_Type()
)
hwhqosUserQueueCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserQueueCirValue.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosUserQueueCirValue.setUnits("Kbps")


class _HwhqosUserQueuePirValue_Type(Integer32):
    """Custom type hwhqosUserQueuePirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1000000),
    )


_HwhqosUserQueuePirValue_Type.__name__ = "Integer32"
_HwhqosUserQueuePirValue_Object = MibTableColumn
hwhqosUserQueuePirValue = _HwhqosUserQueuePirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 23, 1, 4),
    _HwhqosUserQueuePirValue_Type()
)
hwhqosUserQueuePirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserQueuePirValue.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosUserQueuePirValue.setUnits("Kbps")


class _HwhqosUserQueueFlowQueueName_Type(OctetString):
    """Custom type hwhqosUserQueueFlowQueueName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosUserQueueFlowQueueName_Type.__name__ = "OctetString"
_HwhqosUserQueueFlowQueueName_Object = MibTableColumn
hwhqosUserQueueFlowQueueName = _HwhqosUserQueueFlowQueueName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 23, 1, 5),
    _HwhqosUserQueueFlowQueueName_Type()
)
hwhqosUserQueueFlowQueueName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserQueueFlowQueueName.setStatus("current")


class _HwhqosUserQueueFlowMappingName_Type(OctetString):
    """Custom type hwhqosUserQueueFlowMappingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosUserQueueFlowMappingName_Type.__name__ = "OctetString"
_HwhqosUserQueueFlowMappingName_Object = MibTableColumn
hwhqosUserQueueFlowMappingName = _HwhqosUserQueueFlowMappingName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 23, 1, 6),
    _HwhqosUserQueueFlowMappingName_Type()
)
hwhqosUserQueueFlowMappingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserQueueFlowMappingName.setStatus("current")


class _HwhqosUserQueueGroupName_Type(OctetString):
    """Custom type hwhqosUserQueueGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosUserQueueGroupName_Type.__name__ = "OctetString"
_HwhqosUserQueueGroupName_Object = MibTableColumn
hwhqosUserQueueGroupName = _HwhqosUserQueueGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 23, 1, 7),
    _HwhqosUserQueueGroupName_Type()
)
hwhqosUserQueueGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserQueueGroupName.setStatus("current")


class _HwhqosUserQueueServiceTemplateName_Type(OctetString):
    """Custom type hwhqosUserQueueServiceTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosUserQueueServiceTemplateName_Type.__name__ = "OctetString"
_HwhqosUserQueueServiceTemplateName_Object = MibTableColumn
hwhqosUserQueueServiceTemplateName = _HwhqosUserQueueServiceTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 23, 1, 8),
    _HwhqosUserQueueServiceTemplateName_Type()
)
hwhqosUserQueueServiceTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserQueueServiceTemplateName.setStatus("current")
_HwhqosUserQueueRowStatus_Type = RowStatus
_HwhqosUserQueueRowStatus_Object = MibTableColumn
hwhqosUserQueueRowStatus = _HwhqosUserQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 23, 1, 50),
    _HwhqosUserQueueRowStatus_Type()
)
hwhqosUserQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserQueueRowStatus.setStatus("current")
_HwhqosBehaviorUserQueueTable_Object = MibTable
hwhqosBehaviorUserQueueTable = _HwhqosBehaviorUserQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 24)
)
if mibBuilder.loadTexts:
    hwhqosBehaviorUserQueueTable.setStatus("current")
_HwhqosBehaviorUserQueueEntry_Object = MibTableRow
hwhqosBehaviorUserQueueEntry = _HwhqosBehaviorUserQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 24, 1)
)
hwhqosBehaviorUserQueueEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosBehaviorName"),
)
if mibBuilder.loadTexts:
    hwhqosBehaviorUserQueueEntry.setStatus("current")


class _HwhqosBehaviorName_Type(OctetString):
    """Custom type hwhqosBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosBehaviorName_Type.__name__ = "OctetString"
_HwhqosBehaviorName_Object = MibTableColumn
hwhqosBehaviorName = _HwhqosBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 24, 1, 1),
    _HwhqosBehaviorName_Type()
)
hwhqosBehaviorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosBehaviorName.setStatus("current")


class _HwhqosBehaviorCirValue_Type(Integer32):
    """Custom type hwhqosBehaviorCirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 10000000),
    )


_HwhqosBehaviorCirValue_Type.__name__ = "Integer32"
_HwhqosBehaviorCirValue_Object = MibTableColumn
hwhqosBehaviorCirValue = _HwhqosBehaviorCirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 24, 1, 2),
    _HwhqosBehaviorCirValue_Type()
)
hwhqosBehaviorCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBehaviorCirValue.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosBehaviorCirValue.setUnits("Kbps")


class _HwhqosBehaviorPirValue_Type(Integer32):
    """Custom type hwhqosBehaviorPirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 10000000),
    )


_HwhqosBehaviorPirValue_Type.__name__ = "Integer32"
_HwhqosBehaviorPirValue_Object = MibTableColumn
hwhqosBehaviorPirValue = _HwhqosBehaviorPirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 24, 1, 3),
    _HwhqosBehaviorPirValue_Type()
)
hwhqosBehaviorPirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBehaviorPirValue.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosBehaviorPirValue.setUnits("Kbps")


class _HwhqosBehaviorFlowQueueName_Type(OctetString):
    """Custom type hwhqosBehaviorFlowQueueName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosBehaviorFlowQueueName_Type.__name__ = "OctetString"
_HwhqosBehaviorFlowQueueName_Object = MibTableColumn
hwhqosBehaviorFlowQueueName = _HwhqosBehaviorFlowQueueName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 24, 1, 4),
    _HwhqosBehaviorFlowQueueName_Type()
)
hwhqosBehaviorFlowQueueName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBehaviorFlowQueueName.setStatus("current")


class _HwhqosBehaviorFlowMappingName_Type(OctetString):
    """Custom type hwhqosBehaviorFlowMappingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosBehaviorFlowMappingName_Type.__name__ = "OctetString"
_HwhqosBehaviorFlowMappingName_Object = MibTableColumn
hwhqosBehaviorFlowMappingName = _HwhqosBehaviorFlowMappingName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 24, 1, 5),
    _HwhqosBehaviorFlowMappingName_Type()
)
hwhqosBehaviorFlowMappingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBehaviorFlowMappingName.setStatus("current")


class _HwhqosBehaviorGroupName_Type(OctetString):
    """Custom type hwhqosBehaviorGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosBehaviorGroupName_Type.__name__ = "OctetString"
_HwhqosBehaviorGroupName_Object = MibTableColumn
hwhqosBehaviorGroupName = _HwhqosBehaviorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 24, 1, 6),
    _HwhqosBehaviorGroupName_Type()
)
hwhqosBehaviorGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBehaviorGroupName.setStatus("current")


class _HwhqosBehaviorServiceTemplateName_Type(OctetString):
    """Custom type hwhqosBehaviorServiceTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosBehaviorServiceTemplateName_Type.__name__ = "OctetString"
_HwhqosBehaviorServiceTemplateName_Object = MibTableColumn
hwhqosBehaviorServiceTemplateName = _HwhqosBehaviorServiceTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 24, 1, 7),
    _HwhqosBehaviorServiceTemplateName_Type()
)
hwhqosBehaviorServiceTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBehaviorServiceTemplateName.setStatus("current")
_HwhqosBehaviorUserQueueRowStatus_Type = RowStatus
_HwhqosBehaviorUserQueueRowStatus_Object = MibTableColumn
hwhqosBehaviorUserQueueRowStatus = _HwhqosBehaviorUserQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 24, 1, 50),
    _HwhqosBehaviorUserQueueRowStatus_Type()
)
hwhqosBehaviorUserQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBehaviorUserQueueRowStatus.setStatus("current")
_HwhqosBandwidthTable_Object = MibTable
hwhqosBandwidthTable = _HwhqosBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 25)
)
if mibBuilder.loadTexts:
    hwhqosBandwidthTable.setStatus("current")
_HwhqosBandwidthEntry_Object = MibTableRow
hwhqosBandwidthEntry = _HwhqosBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 25, 1)
)
hwhqosBandwidthEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosBandwidthInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwhqosBandwidthEntry.setStatus("current")
_HwhqosBandwidthInterfaceIndex_Type = InterfaceIndex
_HwhqosBandwidthInterfaceIndex_Object = MibTableColumn
hwhqosBandwidthInterfaceIndex = _HwhqosBandwidthInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 25, 1, 1),
    _HwhqosBandwidthInterfaceIndex_Type()
)
hwhqosBandwidthInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosBandwidthInterfaceIndex.setStatus("current")


class _HwhqosBandwidthValue_Type(Integer32):
    """Custom type hwhqosBandwidthValue based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwhqosBandwidthValue_Type.__name__ = "Integer32"
_HwhqosBandwidthValue_Object = MibTableColumn
hwhqosBandwidthValue = _HwhqosBandwidthValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 25, 1, 2),
    _HwhqosBandwidthValue_Type()
)
hwhqosBandwidthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBandwidthValue.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosBandwidthValue.setUnits("Mbps")
_HwhqosBandwidthRowStatus_Type = RowStatus
_HwhqosBandwidthRowStatus_Object = MibTableColumn
hwhqosBandwidthRowStatus = _HwhqosBandwidthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 25, 1, 50),
    _HwhqosBandwidthRowStatus_Type()
)
hwhqosBandwidthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBandwidthRowStatus.setStatus("current")
_HwhqosServiceTemplateTable_Object = MibTable
hwhqosServiceTemplateTable = _HwhqosServiceTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 26)
)
if mibBuilder.loadTexts:
    hwhqosServiceTemplateTable.setStatus("current")
_HwhqosServiceTemplateEntry_Object = MibTableRow
hwhqosServiceTemplateEntry = _HwhqosServiceTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 26, 1)
)
hwhqosServiceTemplateEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceTemplateName"),
)
if mibBuilder.loadTexts:
    hwhqosServiceTemplateEntry.setStatus("current")


class _HwhqosServiceTemplateName_Type(OctetString):
    """Custom type hwhqosServiceTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosServiceTemplateName_Type.__name__ = "OctetString"
_HwhqosServiceTemplateName_Object = MibTableColumn
hwhqosServiceTemplateName = _HwhqosServiceTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 26, 1, 1),
    _HwhqosServiceTemplateName_Type()
)
hwhqosServiceTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosServiceTemplateName.setStatus("current")


class _HwhqosSlotNumber_Type(Integer32):
    """Custom type hwhqosSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwhqosSlotNumber_Type.__name__ = "Integer32"
_HwhqosSlotNumber_Object = MibTableColumn
hwhqosSlotNumber = _HwhqosSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 26, 1, 2),
    _HwhqosSlotNumber_Type()
)
hwhqosSlotNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosSlotNumber.setStatus("current")
_HwhqosServiceTemplateRowStatus_Type = RowStatus
_HwhqosServiceTemplateRowStatus_Object = MibTableColumn
hwhqosServiceTemplateRowStatus = _HwhqosServiceTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 26, 1, 50),
    _HwhqosServiceTemplateRowStatus_Type()
)
hwhqosServiceTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceTemplateRowStatus.setStatus("current")
_HwhqosNetworkHeaderLengthTable_Object = MibTable
hwhqosNetworkHeaderLengthTable = _HwhqosNetworkHeaderLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 27)
)
if mibBuilder.loadTexts:
    hwhqosNetworkHeaderLengthTable.setStatus("current")
_HwhqosNetworkHeaderLengthEntry_Object = MibTableRow
hwhqosNetworkHeaderLengthEntry = _HwhqosNetworkHeaderLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 27, 1)
)
hwhqosNetworkHeaderLengthEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceTemplateName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosNetworkHeaderLengthDirection"),
)
if mibBuilder.loadTexts:
    hwhqosNetworkHeaderLengthEntry.setStatus("current")


class _HwhqosNetworkHeaderLengthDirection_Type(Integer32):
    """Custom type hwhqosNetworkHeaderLengthDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosNetworkHeaderLengthDirection_Type.__name__ = "Integer32"
_HwhqosNetworkHeaderLengthDirection_Object = MibTableColumn
hwhqosNetworkHeaderLengthDirection = _HwhqosNetworkHeaderLengthDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 27, 1, 1),
    _HwhqosNetworkHeaderLengthDirection_Type()
)
hwhqosNetworkHeaderLengthDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosNetworkHeaderLengthDirection.setStatus("current")


class _HwhqosNetWorkHeaderLengthValue_Type(Integer32):
    """Custom type hwhqosNetWorkHeaderLengthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-63, 63),
    )


_HwhqosNetWorkHeaderLengthValue_Type.__name__ = "Integer32"
_HwhqosNetWorkHeaderLengthValue_Object = MibTableColumn
hwhqosNetWorkHeaderLengthValue = _HwhqosNetWorkHeaderLengthValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 27, 1, 2),
    _HwhqosNetWorkHeaderLengthValue_Type()
)
hwhqosNetWorkHeaderLengthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosNetWorkHeaderLengthValue.setStatus("current")
_HwhqosNetWorkHeaderLengthRowStatus_Type = RowStatus
_HwhqosNetWorkHeaderLengthRowStatus_Object = MibTableColumn
hwhqosNetWorkHeaderLengthRowStatus = _HwhqosNetWorkHeaderLengthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 27, 1, 50),
    _HwhqosNetWorkHeaderLengthRowStatus_Type()
)
hwhqosNetWorkHeaderLengthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosNetWorkHeaderLengthRowStatus.setStatus("current")
_HwhqosServiceTemplateApplyTable_Object = MibTable
hwhqosServiceTemplateApplyTable = _HwhqosServiceTemplateApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 28)
)
if mibBuilder.loadTexts:
    hwhqosServiceTemplateApplyTable.setStatus("current")
_HwhqosServiceTemplateApplyEntry_Object = MibTableRow
hwhqosServiceTemplateApplyEntry = _HwhqosServiceTemplateApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 28, 1)
)
hwhqosServiceTemplateApplyEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceTemplateApplyInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwhqosServiceTemplateApplyEntry.setStatus("current")
_HwhqosServiceTemplateApplyInterfaceIndex_Type = InterfaceIndex
_HwhqosServiceTemplateApplyInterfaceIndex_Object = MibTableColumn
hwhqosServiceTemplateApplyInterfaceIndex = _HwhqosServiceTemplateApplyInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 28, 1, 1),
    _HwhqosServiceTemplateApplyInterfaceIndex_Type()
)
hwhqosServiceTemplateApplyInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosServiceTemplateApplyInterfaceIndex.setStatus("current")


class _HwhqosApplyServiceTemplateName_Type(OctetString):
    """Custom type hwhqosApplyServiceTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosApplyServiceTemplateName_Type.__name__ = "OctetString"
_HwhqosApplyServiceTemplateName_Object = MibTableColumn
hwhqosApplyServiceTemplateName = _HwhqosApplyServiceTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 28, 1, 2),
    _HwhqosApplyServiceTemplateName_Type()
)
hwhqosApplyServiceTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosApplyServiceTemplateName.setStatus("current")
_HwhqosServiceTemplateApplyRowStatus_Type = RowStatus
_HwhqosServiceTemplateApplyRowStatus_Object = MibTableColumn
hwhqosServiceTemplateApplyRowStatus = _HwhqosServiceTemplateApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 28, 1, 50),
    _HwhqosServiceTemplateApplyRowStatus_Type()
)
hwhqosServiceTemplateApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceTemplateApplyRowStatus.setStatus("current")
_HwhqosProfileUserQueueStatisticsTable_Object = MibTable
hwhqosProfileUserQueueStatisticsTable = _HwhqosProfileUserQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29)
)
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsTable.setStatus("current")
_HwhqosProfileUserQueueStatisticsEntry_Object = MibTableRow
hwhqosProfileUserQueueStatisticsEntry = _HwhqosProfileUserQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1)
)
hwhqosProfileUserQueueStatisticsEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsPevid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsCevid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsSlotNumber"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsQueueIndex"),
)
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsEntry.setStatus("current")
_HwhqosProfileUserQueueStatisticsInterfaceIndex_Type = InterfaceIndex
_HwhqosProfileUserQueueStatisticsInterfaceIndex_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsInterfaceIndex = _HwhqosProfileUserQueueStatisticsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 1),
    _HwhqosProfileUserQueueStatisticsInterfaceIndex_Type()
)
hwhqosProfileUserQueueStatisticsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsInterfaceIndex.setStatus("current")


class _HwhqosProfileUserQueueStatisticsDirection_Type(Integer32):
    """Custom type hwhqosProfileUserQueueStatisticsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosProfileUserQueueStatisticsDirection_Type.__name__ = "Integer32"
_HwhqosProfileUserQueueStatisticsDirection_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsDirection = _HwhqosProfileUserQueueStatisticsDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 2),
    _HwhqosProfileUserQueueStatisticsDirection_Type()
)
hwhqosProfileUserQueueStatisticsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsDirection.setStatus("current")


class _HwhqosProfileUserQueueStatisticsPevid_Type(Integer32):
    """Custom type hwhqosProfileUserQueueStatisticsPevid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwhqosProfileUserQueueStatisticsPevid_Type.__name__ = "Integer32"
_HwhqosProfileUserQueueStatisticsPevid_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsPevid = _HwhqosProfileUserQueueStatisticsPevid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 3),
    _HwhqosProfileUserQueueStatisticsPevid_Type()
)
hwhqosProfileUserQueueStatisticsPevid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsPevid.setStatus("current")


class _HwhqosProfileUserQueueStatisticsCevid_Type(Integer32):
    """Custom type hwhqosProfileUserQueueStatisticsCevid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwhqosProfileUserQueueStatisticsCevid_Type.__name__ = "Integer32"
_HwhqosProfileUserQueueStatisticsCevid_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsCevid = _HwhqosProfileUserQueueStatisticsCevid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 4),
    _HwhqosProfileUserQueueStatisticsCevid_Type()
)
hwhqosProfileUserQueueStatisticsCevid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsCevid.setStatus("current")


class _HwhqosProfileUserQueueStatisticsSlotNumber_Type(Integer32):
    """Custom type hwhqosProfileUserQueueStatisticsSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwhqosProfileUserQueueStatisticsSlotNumber_Type.__name__ = "Integer32"
_HwhqosProfileUserQueueStatisticsSlotNumber_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsSlotNumber = _HwhqosProfileUserQueueStatisticsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 5),
    _HwhqosProfileUserQueueStatisticsSlotNumber_Type()
)
hwhqosProfileUserQueueStatisticsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsSlotNumber.setStatus("current")


class _HwhqosProfileUserQueueStatisticsQueueIndex_Type(Integer32):
    """Custom type hwhqosProfileUserQueueStatisticsQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("total", 9))
    )


_HwhqosProfileUserQueueStatisticsQueueIndex_Type.__name__ = "Integer32"
_HwhqosProfileUserQueueStatisticsQueueIndex_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsQueueIndex = _HwhqosProfileUserQueueStatisticsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 6),
    _HwhqosProfileUserQueueStatisticsQueueIndex_Type()
)
hwhqosProfileUserQueueStatisticsQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsQueueIndex.setStatus("current")


class _HwhqosProfileUserQueueStatisticsReset_Type(Integer32):
    """Custom type hwhqosProfileUserQueueStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwhqosProfileUserQueueStatisticsReset_Type.__name__ = "Integer32"
_HwhqosProfileUserQueueStatisticsReset_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsReset = _HwhqosProfileUserQueueStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 7),
    _HwhqosProfileUserQueueStatisticsReset_Type()
)
hwhqosProfileUserQueueStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsReset.setStatus("current")
_HwhqosProfileUserQueueStatisticsPassPackets_Type = Counter64
_HwhqosProfileUserQueueStatisticsPassPackets_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsPassPackets = _HwhqosProfileUserQueueStatisticsPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 8),
    _HwhqosProfileUserQueueStatisticsPassPackets_Type()
)
hwhqosProfileUserQueueStatisticsPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsPassPackets.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsPassPackets.setUnits("packets")
_HwhqosProfileUserQueueStatisticsPassBytes_Type = Counter64
_HwhqosProfileUserQueueStatisticsPassBytes_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsPassBytes = _HwhqosProfileUserQueueStatisticsPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 9),
    _HwhqosProfileUserQueueStatisticsPassBytes_Type()
)
hwhqosProfileUserQueueStatisticsPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsPassBytes.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsPassBytes.setUnits("bytes")
_HwhqosProfileUserQueueStatisticsDropPackets_Type = Counter64
_HwhqosProfileUserQueueStatisticsDropPackets_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsDropPackets = _HwhqosProfileUserQueueStatisticsDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 10),
    _HwhqosProfileUserQueueStatisticsDropPackets_Type()
)
hwhqosProfileUserQueueStatisticsDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsDropPackets.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsDropPackets.setUnits("packets")
_HwhqosProfileUserQueueStatisticsDropBytes_Type = Counter64
_HwhqosProfileUserQueueStatisticsDropBytes_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsDropBytes = _HwhqosProfileUserQueueStatisticsDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 11),
    _HwhqosProfileUserQueueStatisticsDropBytes_Type()
)
hwhqosProfileUserQueueStatisticsDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsDropBytes.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsDropBytes.setUnits("bytes")
_HwhqosProfileUserQueueStatisticsPassPacketsRate_Type = Counter64
_HwhqosProfileUserQueueStatisticsPassPacketsRate_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsPassPacketsRate = _HwhqosProfileUserQueueStatisticsPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 12),
    _HwhqosProfileUserQueueStatisticsPassPacketsRate_Type()
)
hwhqosProfileUserQueueStatisticsPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsPassPacketsRate.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsPassPacketsRate.setUnits("pps")
_HwhqosProfileUserQueueStatisticsPassBytesRate_Type = Counter64
_HwhqosProfileUserQueueStatisticsPassBytesRate_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsPassBytesRate = _HwhqosProfileUserQueueStatisticsPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 13),
    _HwhqosProfileUserQueueStatisticsPassBytesRate_Type()
)
hwhqosProfileUserQueueStatisticsPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsPassBytesRate.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsPassBytesRate.setUnits("bps")
_HwhqosProfileUserQueueStatisticsDropPacketsRate_Type = Counter64
_HwhqosProfileUserQueueStatisticsDropPacketsRate_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsDropPacketsRate = _HwhqosProfileUserQueueStatisticsDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 14),
    _HwhqosProfileUserQueueStatisticsDropPacketsRate_Type()
)
hwhqosProfileUserQueueStatisticsDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsDropPacketsRate.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsDropPacketsRate.setUnits("pps")
_HwhqosProfileUserQueueStatisticsDropBytesRate_Type = Counter64
_HwhqosProfileUserQueueStatisticsDropBytesRate_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsDropBytesRate = _HwhqosProfileUserQueueStatisticsDropBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 15),
    _HwhqosProfileUserQueueStatisticsDropBytesRate_Type()
)
hwhqosProfileUserQueueStatisticsDropBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsDropBytesRate.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsDropBytesRate.setUnits("bps")
_HwhqosProfileUserQueueStatisticsTrafficTowardsThisInterface_Type = Counter64
_HwhqosProfileUserQueueStatisticsTrafficTowardsThisInterface_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsTrafficTowardsThisInterface = _HwhqosProfileUserQueueStatisticsTrafficTowardsThisInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 16),
    _HwhqosProfileUserQueueStatisticsTrafficTowardsThisInterface_Type()
)
hwhqosProfileUserQueueStatisticsTrafficTowardsThisInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsTrafficTowardsThisInterface.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsTrafficTowardsThisInterface.setUnits("bps")


class _HwhqosProfileUserQueueStatisticsConfiguredCir_Type(Unsigned32):
    """Custom type hwhqosProfileUserQueueStatisticsConfiguredCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 4294967294),
    )


_HwhqosProfileUserQueueStatisticsConfiguredCir_Type.__name__ = "Unsigned32"
_HwhqosProfileUserQueueStatisticsConfiguredCir_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsConfiguredCir = _HwhqosProfileUserQueueStatisticsConfiguredCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 17),
    _HwhqosProfileUserQueueStatisticsConfiguredCir_Type()
)
hwhqosProfileUserQueueStatisticsConfiguredCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsConfiguredCir.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsConfiguredCir.setUnits("kbps")


class _HwhqosProfileUserQueueStatisticsConfiguredPir_Type(Unsigned32):
    """Custom type hwhqosProfileUserQueueStatisticsConfiguredPir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 4294967294),
    )


_HwhqosProfileUserQueueStatisticsConfiguredPir_Type.__name__ = "Unsigned32"
_HwhqosProfileUserQueueStatisticsConfiguredPir_Object = MibTableColumn
hwhqosProfileUserQueueStatisticsConfiguredPir = _HwhqosProfileUserQueueStatisticsConfiguredPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 29, 1, 18),
    _HwhqosProfileUserQueueStatisticsConfiguredPir_Type()
)
hwhqosProfileUserQueueStatisticsConfiguredPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsConfiguredPir.setStatus("current")
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsConfiguredPir.setUnits("kbps")
_HwhqosProfileCarStatisticsTable_Object = MibTable
hwhqosProfileCarStatisticsTable = _HwhqosProfileCarStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30)
)
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsTable.setStatus("current")
_HwhqosProfileCarStatisticsEntry_Object = MibTableRow
hwhqosProfileCarStatisticsEntry = _HwhqosProfileCarStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1)
)
hwhqosProfileCarStatisticsEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsPevid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsCevid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsType"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsSlotNumber"),
)
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsEntry.setStatus("current")
_HwhqosProfileCarStatisticsInterfaceIndex_Type = InterfaceIndex
_HwhqosProfileCarStatisticsInterfaceIndex_Object = MibTableColumn
hwhqosProfileCarStatisticsInterfaceIndex = _HwhqosProfileCarStatisticsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 1),
    _HwhqosProfileCarStatisticsInterfaceIndex_Type()
)
hwhqosProfileCarStatisticsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsInterfaceIndex.setStatus("current")


class _HwhqosProfileCarStatisticsDirection_Type(Integer32):
    """Custom type hwhqosProfileCarStatisticsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosProfileCarStatisticsDirection_Type.__name__ = "Integer32"
_HwhqosProfileCarStatisticsDirection_Object = MibTableColumn
hwhqosProfileCarStatisticsDirection = _HwhqosProfileCarStatisticsDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 2),
    _HwhqosProfileCarStatisticsDirection_Type()
)
hwhqosProfileCarStatisticsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsDirection.setStatus("current")


class _HwhqosProfileCarStatisticsPevid_Type(Integer32):
    """Custom type hwhqosProfileCarStatisticsPevid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwhqosProfileCarStatisticsPevid_Type.__name__ = "Integer32"
_HwhqosProfileCarStatisticsPevid_Object = MibTableColumn
hwhqosProfileCarStatisticsPevid = _HwhqosProfileCarStatisticsPevid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 3),
    _HwhqosProfileCarStatisticsPevid_Type()
)
hwhqosProfileCarStatisticsPevid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsPevid.setStatus("current")


class _HwhqosProfileCarStatisticsCevid_Type(Integer32):
    """Custom type hwhqosProfileCarStatisticsCevid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwhqosProfileCarStatisticsCevid_Type.__name__ = "Integer32"
_HwhqosProfileCarStatisticsCevid_Object = MibTableColumn
hwhqosProfileCarStatisticsCevid = _HwhqosProfileCarStatisticsCevid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 4),
    _HwhqosProfileCarStatisticsCevid_Type()
)
hwhqosProfileCarStatisticsCevid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsCevid.setStatus("current")


class _HwhqosProfileCarStatisticsType_Type(Integer32):
    """Custom type hwhqosProfileCarStatisticsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("broadcastSuppression", 2),
          ("car", 1),
          ("multicastSuppression", 3),
          ("unknownUnicastSuppression", 4))
    )


_HwhqosProfileCarStatisticsType_Type.__name__ = "Integer32"
_HwhqosProfileCarStatisticsType_Object = MibTableColumn
hwhqosProfileCarStatisticsType = _HwhqosProfileCarStatisticsType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 5),
    _HwhqosProfileCarStatisticsType_Type()
)
hwhqosProfileCarStatisticsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsType.setStatus("current")


class _HwhqosProfileCarStatisticsSlotNumber_Type(Integer32):
    """Custom type hwhqosProfileCarStatisticsSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwhqosProfileCarStatisticsSlotNumber_Type.__name__ = "Integer32"
_HwhqosProfileCarStatisticsSlotNumber_Object = MibTableColumn
hwhqosProfileCarStatisticsSlotNumber = _HwhqosProfileCarStatisticsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 6),
    _HwhqosProfileCarStatisticsSlotNumber_Type()
)
hwhqosProfileCarStatisticsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsSlotNumber.setStatus("current")


class _HwhqosProfileCarStatisticsReset_Type(Integer32):
    """Custom type hwhqosProfileCarStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwhqosProfileCarStatisticsReset_Type.__name__ = "Integer32"
_HwhqosProfileCarStatisticsReset_Object = MibTableColumn
hwhqosProfileCarStatisticsReset = _HwhqosProfileCarStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 7),
    _HwhqosProfileCarStatisticsReset_Type()
)
hwhqosProfileCarStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsReset.setStatus("current")
_HwhqosProfileCarStatisticsPassPackets_Type = Counter64
_HwhqosProfileCarStatisticsPassPackets_Object = MibTableColumn
hwhqosProfileCarStatisticsPassPackets = _HwhqosProfileCarStatisticsPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 8),
    _HwhqosProfileCarStatisticsPassPackets_Type()
)
hwhqosProfileCarStatisticsPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsPassPackets.setStatus("current")
_HwhqosProfileCarStatisticsPassBytes_Type = Counter64
_HwhqosProfileCarStatisticsPassBytes_Object = MibTableColumn
hwhqosProfileCarStatisticsPassBytes = _HwhqosProfileCarStatisticsPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 9),
    _HwhqosProfileCarStatisticsPassBytes_Type()
)
hwhqosProfileCarStatisticsPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsPassBytes.setStatus("current")
_HwhqosProfileCarStatisticsDropPackets_Type = Counter64
_HwhqosProfileCarStatisticsDropPackets_Object = MibTableColumn
hwhqosProfileCarStatisticsDropPackets = _HwhqosProfileCarStatisticsDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 10),
    _HwhqosProfileCarStatisticsDropPackets_Type()
)
hwhqosProfileCarStatisticsDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsDropPackets.setStatus("current")
_HwhqosProfileCarStatisticsDropBytes_Type = Counter64
_HwhqosProfileCarStatisticsDropBytes_Object = MibTableColumn
hwhqosProfileCarStatisticsDropBytes = _HwhqosProfileCarStatisticsDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 11),
    _HwhqosProfileCarStatisticsDropBytes_Type()
)
hwhqosProfileCarStatisticsDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsDropBytes.setStatus("current")
_HwhqosProfileCarStatisticsPassPacketsRate_Type = Counter64
_HwhqosProfileCarStatisticsPassPacketsRate_Object = MibTableColumn
hwhqosProfileCarStatisticsPassPacketsRate = _HwhqosProfileCarStatisticsPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 12),
    _HwhqosProfileCarStatisticsPassPacketsRate_Type()
)
hwhqosProfileCarStatisticsPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsPassPacketsRate.setStatus("current")
_HwhqosProfileCarStatisticsPassBytesRate_Type = Counter64
_HwhqosProfileCarStatisticsPassBytesRate_Object = MibTableColumn
hwhqosProfileCarStatisticsPassBytesRate = _HwhqosProfileCarStatisticsPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 13),
    _HwhqosProfileCarStatisticsPassBytesRate_Type()
)
hwhqosProfileCarStatisticsPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsPassBytesRate.setStatus("current")
_HwhqosProfileCarStatisticsDropPacketsRate_Type = Counter64
_HwhqosProfileCarStatisticsDropPacketsRate_Object = MibTableColumn
hwhqosProfileCarStatisticsDropPacketsRate = _HwhqosProfileCarStatisticsDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 14),
    _HwhqosProfileCarStatisticsDropPacketsRate_Type()
)
hwhqosProfileCarStatisticsDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsDropPacketsRate.setStatus("current")
_HwhqosProfileCarStatisticsDropBytesRate_Type = Counter64
_HwhqosProfileCarStatisticsDropBytesRate_Object = MibTableColumn
hwhqosProfileCarStatisticsDropBytesRate = _HwhqosProfileCarStatisticsDropBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 30, 1, 15),
    _HwhqosProfileCarStatisticsDropBytesRate_Type()
)
hwhqosProfileCarStatisticsDropBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsDropBytesRate.setStatus("current")
_HwhqosUserQueueStatisticsTable_Object = MibTable
hwhqosUserQueueStatisticsTable = _HwhqosUserQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31)
)
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsTable.setStatus("current")
_HwhqosUserQueueStatisticsEntry_Object = MibTableRow
hwhqosUserQueueStatisticsEntry = _HwhqosUserQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1)
)
hwhqosUserQueueStatisticsEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsSlotNumber"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsQueueIndex"),
)
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsEntry.setStatus("current")
_HwhqosUserQueueStatisticsInterfaceIndex_Type = InterfaceIndex
_HwhqosUserQueueStatisticsInterfaceIndex_Object = MibTableColumn
hwhqosUserQueueStatisticsInterfaceIndex = _HwhqosUserQueueStatisticsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 1),
    _HwhqosUserQueueStatisticsInterfaceIndex_Type()
)
hwhqosUserQueueStatisticsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsInterfaceIndex.setStatus("current")


class _HwhqosUserQueueStatisticsDirection_Type(Integer32):
    """Custom type hwhqosUserQueueStatisticsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosUserQueueStatisticsDirection_Type.__name__ = "Integer32"
_HwhqosUserQueueStatisticsDirection_Object = MibTableColumn
hwhqosUserQueueStatisticsDirection = _HwhqosUserQueueStatisticsDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 2),
    _HwhqosUserQueueStatisticsDirection_Type()
)
hwhqosUserQueueStatisticsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsDirection.setStatus("current")


class _HwhqosUserQueueStatisticsSlotNumber_Type(Integer32):
    """Custom type hwhqosUserQueueStatisticsSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwhqosUserQueueStatisticsSlotNumber_Type.__name__ = "Integer32"
_HwhqosUserQueueStatisticsSlotNumber_Object = MibTableColumn
hwhqosUserQueueStatisticsSlotNumber = _HwhqosUserQueueStatisticsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 3),
    _HwhqosUserQueueStatisticsSlotNumber_Type()
)
hwhqosUserQueueStatisticsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsSlotNumber.setStatus("current")


class _HwhqosUserQueueStatisticsQueueIndex_Type(Integer32):
    """Custom type hwhqosUserQueueStatisticsQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("total", 9))
    )


_HwhqosUserQueueStatisticsQueueIndex_Type.__name__ = "Integer32"
_HwhqosUserQueueStatisticsQueueIndex_Object = MibTableColumn
hwhqosUserQueueStatisticsQueueIndex = _HwhqosUserQueueStatisticsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 4),
    _HwhqosUserQueueStatisticsQueueIndex_Type()
)
hwhqosUserQueueStatisticsQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsQueueIndex.setStatus("current")


class _HwhqosUserQueueStatisticsReset_Type(Integer32):
    """Custom type hwhqosUserQueueStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwhqosUserQueueStatisticsReset_Type.__name__ = "Integer32"
_HwhqosUserQueueStatisticsReset_Object = MibTableColumn
hwhqosUserQueueStatisticsReset = _HwhqosUserQueueStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 5),
    _HwhqosUserQueueStatisticsReset_Type()
)
hwhqosUserQueueStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsReset.setStatus("current")
_HwhqosUserQueueStatisticsPassPackets_Type = Counter64
_HwhqosUserQueueStatisticsPassPackets_Object = MibTableColumn
hwhqosUserQueueStatisticsPassPackets = _HwhqosUserQueueStatisticsPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 6),
    _HwhqosUserQueueStatisticsPassPackets_Type()
)
hwhqosUserQueueStatisticsPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsPassPackets.setStatus("current")
_HwhqosUserQueueStatisticsPassBytes_Type = Counter64
_HwhqosUserQueueStatisticsPassBytes_Object = MibTableColumn
hwhqosUserQueueStatisticsPassBytes = _HwhqosUserQueueStatisticsPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 7),
    _HwhqosUserQueueStatisticsPassBytes_Type()
)
hwhqosUserQueueStatisticsPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsPassBytes.setStatus("current")
_HwhqosUserQueueStatisticsDropPackets_Type = Counter64
_HwhqosUserQueueStatisticsDropPackets_Object = MibTableColumn
hwhqosUserQueueStatisticsDropPackets = _HwhqosUserQueueStatisticsDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 8),
    _HwhqosUserQueueStatisticsDropPackets_Type()
)
hwhqosUserQueueStatisticsDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsDropPackets.setStatus("current")
_HwhqosUserQueueStatisticsDropBytes_Type = Counter64
_HwhqosUserQueueStatisticsDropBytes_Object = MibTableColumn
hwhqosUserQueueStatisticsDropBytes = _HwhqosUserQueueStatisticsDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 9),
    _HwhqosUserQueueStatisticsDropBytes_Type()
)
hwhqosUserQueueStatisticsDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsDropBytes.setStatus("current")
_HwhqosUserQueueStatisticsPassPacketsRate_Type = Counter64
_HwhqosUserQueueStatisticsPassPacketsRate_Object = MibTableColumn
hwhqosUserQueueStatisticsPassPacketsRate = _HwhqosUserQueueStatisticsPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 10),
    _HwhqosUserQueueStatisticsPassPacketsRate_Type()
)
hwhqosUserQueueStatisticsPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsPassPacketsRate.setStatus("current")
_HwhqosUserQueueStatisticsPassBytesRate_Type = Counter64
_HwhqosUserQueueStatisticsPassBytesRate_Object = MibTableColumn
hwhqosUserQueueStatisticsPassBytesRate = _HwhqosUserQueueStatisticsPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 11),
    _HwhqosUserQueueStatisticsPassBytesRate_Type()
)
hwhqosUserQueueStatisticsPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsPassBytesRate.setStatus("current")
_HwhqosUserQueueStatisticsDropPacketsRate_Type = Counter64
_HwhqosUserQueueStatisticsDropPacketsRate_Object = MibTableColumn
hwhqosUserQueueStatisticsDropPacketsRate = _HwhqosUserQueueStatisticsDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 12),
    _HwhqosUserQueueStatisticsDropPacketsRate_Type()
)
hwhqosUserQueueStatisticsDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsDropPacketsRate.setStatus("current")
_HwhqosUserQueueStatisticsDropBytesRate_Type = Counter64
_HwhqosUserQueueStatisticsDropBytesRate_Object = MibTableColumn
hwhqosUserQueueStatisticsDropBytesRate = _HwhqosUserQueueStatisticsDropBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 31, 1, 13),
    _HwhqosUserQueueStatisticsDropBytesRate_Type()
)
hwhqosUserQueueStatisticsDropBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsDropBytesRate.setStatus("current")
_HwhqosUserQueueClassifierStatisticsTable_Object = MibTable
hwhqosUserQueueClassifierStatisticsTable = _HwhqosUserQueueClassifierStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32)
)
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsTable.setStatus("current")
_HwhqosUserQueueClassifierStatisticsEntry_Object = MibTableRow
hwhqosUserQueueClassifierStatisticsEntry = _HwhqosUserQueueClassifierStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1)
)
hwhqosUserQueueClassifierStatisticsEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsClassifierName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsSlotNumber"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsQueueIndex"),
)
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsEntry.setStatus("current")
_HwhqosUserQueueClassifierStatisticsInterfaceIndex_Type = InterfaceIndex
_HwhqosUserQueueClassifierStatisticsInterfaceIndex_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsInterfaceIndex = _HwhqosUserQueueClassifierStatisticsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 1),
    _HwhqosUserQueueClassifierStatisticsInterfaceIndex_Type()
)
hwhqosUserQueueClassifierStatisticsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsInterfaceIndex.setStatus("current")


class _HwhqosUserQueueClassifierStatisticsDirection_Type(Integer32):
    """Custom type hwhqosUserQueueClassifierStatisticsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosUserQueueClassifierStatisticsDirection_Type.__name__ = "Integer32"
_HwhqosUserQueueClassifierStatisticsDirection_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsDirection = _HwhqosUserQueueClassifierStatisticsDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 2),
    _HwhqosUserQueueClassifierStatisticsDirection_Type()
)
hwhqosUserQueueClassifierStatisticsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsDirection.setStatus("current")


class _HwhqosUserQueueClassifierStatisticsClassifierName_Type(OctetString):
    """Custom type hwhqosUserQueueClassifierStatisticsClassifierName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosUserQueueClassifierStatisticsClassifierName_Type.__name__ = "OctetString"
_HwhqosUserQueueClassifierStatisticsClassifierName_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsClassifierName = _HwhqosUserQueueClassifierStatisticsClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 3),
    _HwhqosUserQueueClassifierStatisticsClassifierName_Type()
)
hwhqosUserQueueClassifierStatisticsClassifierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsClassifierName.setStatus("current")


class _HwhqosUserQueueClassifierStatisticsSlotNumber_Type(Integer32):
    """Custom type hwhqosUserQueueClassifierStatisticsSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwhqosUserQueueClassifierStatisticsSlotNumber_Type.__name__ = "Integer32"
_HwhqosUserQueueClassifierStatisticsSlotNumber_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsSlotNumber = _HwhqosUserQueueClassifierStatisticsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 4),
    _HwhqosUserQueueClassifierStatisticsSlotNumber_Type()
)
hwhqosUserQueueClassifierStatisticsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsSlotNumber.setStatus("current")


class _HwhqosUserQueueClassifierStatisticsQueueIndex_Type(Integer32):
    """Custom type hwhqosUserQueueClassifierStatisticsQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("total", 9))
    )


_HwhqosUserQueueClassifierStatisticsQueueIndex_Type.__name__ = "Integer32"
_HwhqosUserQueueClassifierStatisticsQueueIndex_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsQueueIndex = _HwhqosUserQueueClassifierStatisticsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 5),
    _HwhqosUserQueueClassifierStatisticsQueueIndex_Type()
)
hwhqosUserQueueClassifierStatisticsQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsQueueIndex.setStatus("current")


class _HwhqosUserQueueClassifierStatisticsReset_Type(Integer32):
    """Custom type hwhqosUserQueueClassifierStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwhqosUserQueueClassifierStatisticsReset_Type.__name__ = "Integer32"
_HwhqosUserQueueClassifierStatisticsReset_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsReset = _HwhqosUserQueueClassifierStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 6),
    _HwhqosUserQueueClassifierStatisticsReset_Type()
)
hwhqosUserQueueClassifierStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsReset.setStatus("current")
_HwhqosUserQueueClassifierStatisticsPassPackets_Type = Counter64
_HwhqosUserQueueClassifierStatisticsPassPackets_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsPassPackets = _HwhqosUserQueueClassifierStatisticsPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 7),
    _HwhqosUserQueueClassifierStatisticsPassPackets_Type()
)
hwhqosUserQueueClassifierStatisticsPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsPassPackets.setStatus("current")
_HwhqosUserQueueClassifierStatisticsPassBytes_Type = Counter64
_HwhqosUserQueueClassifierStatisticsPassBytes_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsPassBytes = _HwhqosUserQueueClassifierStatisticsPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 8),
    _HwhqosUserQueueClassifierStatisticsPassBytes_Type()
)
hwhqosUserQueueClassifierStatisticsPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsPassBytes.setStatus("current")
_HwhqosUserQueueClassifierStatisticsDropPackets_Type = Counter64
_HwhqosUserQueueClassifierStatisticsDropPackets_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsDropPackets = _HwhqosUserQueueClassifierStatisticsDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 9),
    _HwhqosUserQueueClassifierStatisticsDropPackets_Type()
)
hwhqosUserQueueClassifierStatisticsDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsDropPackets.setStatus("current")
_HwhqosUserQueueClassifierStatisticsDropBytes_Type = Counter64
_HwhqosUserQueueClassifierStatisticsDropBytes_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsDropBytes = _HwhqosUserQueueClassifierStatisticsDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 10),
    _HwhqosUserQueueClassifierStatisticsDropBytes_Type()
)
hwhqosUserQueueClassifierStatisticsDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsDropBytes.setStatus("current")
_HwhqosUserQueueClassifierStatisticsPassPacketsRate_Type = Counter64
_HwhqosUserQueueClassifierStatisticsPassPacketsRate_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsPassPacketsRate = _HwhqosUserQueueClassifierStatisticsPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 11),
    _HwhqosUserQueueClassifierStatisticsPassPacketsRate_Type()
)
hwhqosUserQueueClassifierStatisticsPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsPassPacketsRate.setStatus("current")
_HwhqosUserQueueClassifierStatisticsPassBytesRate_Type = Counter64
_HwhqosUserQueueClassifierStatisticsPassBytesRate_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsPassBytesRate = _HwhqosUserQueueClassifierStatisticsPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 12),
    _HwhqosUserQueueClassifierStatisticsPassBytesRate_Type()
)
hwhqosUserQueueClassifierStatisticsPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsPassBytesRate.setStatus("current")
_HwhqosUserQueueClassifierStatisticsDropPacketsRate_Type = Counter64
_HwhqosUserQueueClassifierStatisticsDropPacketsRate_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsDropPacketsRate = _HwhqosUserQueueClassifierStatisticsDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 13),
    _HwhqosUserQueueClassifierStatisticsDropPacketsRate_Type()
)
hwhqosUserQueueClassifierStatisticsDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsDropPacketsRate.setStatus("current")
_HwhqosUserQueueClassifierStatisticsDropBytesRate_Type = Counter64
_HwhqosUserQueueClassifierStatisticsDropBytesRate_Object = MibTableColumn
hwhqosUserQueueClassifierStatisticsDropBytesRate = _HwhqosUserQueueClassifierStatisticsDropBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 32, 1, 14),
    _HwhqosUserQueueClassifierStatisticsDropBytesRate_Type()
)
hwhqosUserQueueClassifierStatisticsDropBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsDropBytesRate.setStatus("current")
_HwhqosUserGroupQueueStatisticsTable_Object = MibTable
hwhqosUserGroupQueueStatisticsTable = _HwhqosUserGroupQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33)
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsTable.setStatus("current")
_HwhqosUserGroupQueueStatisticsEntry_Object = MibTableRow
hwhqosUserGroupQueueStatisticsEntry = _HwhqosUserGroupQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1)
)
hwhqosUserGroupQueueStatisticsEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsGroupName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsSlotNumber"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsQueueIndex"),
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsEntry.setStatus("current")


class _HwhqosUserGroupQueueStatisticsGroupName_Type(OctetString):
    """Custom type hwhqosUserGroupQueueStatisticsGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosUserGroupQueueStatisticsGroupName_Type.__name__ = "OctetString"
_HwhqosUserGroupQueueStatisticsGroupName_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsGroupName = _HwhqosUserGroupQueueStatisticsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 1),
    _HwhqosUserGroupQueueStatisticsGroupName_Type()
)
hwhqosUserGroupQueueStatisticsGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsGroupName.setStatus("current")


class _HwhqosUserGroupQueueStatisticsDirection_Type(Integer32):
    """Custom type hwhqosUserGroupQueueStatisticsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosUserGroupQueueStatisticsDirection_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueStatisticsDirection_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsDirection = _HwhqosUserGroupQueueStatisticsDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 2),
    _HwhqosUserGroupQueueStatisticsDirection_Type()
)
hwhqosUserGroupQueueStatisticsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsDirection.setStatus("current")


class _HwhqosUserGroupQueueStatisticsSlotNumber_Type(Integer32):
    """Custom type hwhqosUserGroupQueueStatisticsSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwhqosUserGroupQueueStatisticsSlotNumber_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueStatisticsSlotNumber_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsSlotNumber = _HwhqosUserGroupQueueStatisticsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 3),
    _HwhqosUserGroupQueueStatisticsSlotNumber_Type()
)
hwhqosUserGroupQueueStatisticsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsSlotNumber.setStatus("current")


class _HwhqosUserGroupQueueStatisticsQueueIndex_Type(Integer32):
    """Custom type hwhqosUserGroupQueueStatisticsQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("total", 9))
    )


_HwhqosUserGroupQueueStatisticsQueueIndex_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueStatisticsQueueIndex_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsQueueIndex = _HwhqosUserGroupQueueStatisticsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 4),
    _HwhqosUserGroupQueueStatisticsQueueIndex_Type()
)
hwhqosUserGroupQueueStatisticsQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsQueueIndex.setStatus("current")


class _HwhqosUserGroupQueueStatisticsReset_Type(Integer32):
    """Custom type hwhqosUserGroupQueueStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwhqosUserGroupQueueStatisticsReset_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueStatisticsReset_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsReset = _HwhqosUserGroupQueueStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 5),
    _HwhqosUserGroupQueueStatisticsReset_Type()
)
hwhqosUserGroupQueueStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsReset.setStatus("current")
_HwhqosUserGroupQueueStatisticsPassPackets_Type = Counter64
_HwhqosUserGroupQueueStatisticsPassPackets_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsPassPackets = _HwhqosUserGroupQueueStatisticsPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 6),
    _HwhqosUserGroupQueueStatisticsPassPackets_Type()
)
hwhqosUserGroupQueueStatisticsPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsPassPackets.setStatus("current")
_HwhqosUserGroupQueueStatisticsPassBytes_Type = Counter64
_HwhqosUserGroupQueueStatisticsPassBytes_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsPassBytes = _HwhqosUserGroupQueueStatisticsPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 7),
    _HwhqosUserGroupQueueStatisticsPassBytes_Type()
)
hwhqosUserGroupQueueStatisticsPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsPassBytes.setStatus("current")
_HwhqosUserGroupQueueStatisticsDropPackets_Type = Counter64
_HwhqosUserGroupQueueStatisticsDropPackets_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsDropPackets = _HwhqosUserGroupQueueStatisticsDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 8),
    _HwhqosUserGroupQueueStatisticsDropPackets_Type()
)
hwhqosUserGroupQueueStatisticsDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsDropPackets.setStatus("current")
_HwhqosUserGroupQueueStatisticsDropBytes_Type = Counter64
_HwhqosUserGroupQueueStatisticsDropBytes_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsDropBytes = _HwhqosUserGroupQueueStatisticsDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 9),
    _HwhqosUserGroupQueueStatisticsDropBytes_Type()
)
hwhqosUserGroupQueueStatisticsDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsDropBytes.setStatus("current")
_HwhqosUserGroupQueueStatisticsPassPacketsRate_Type = Counter64
_HwhqosUserGroupQueueStatisticsPassPacketsRate_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsPassPacketsRate = _HwhqosUserGroupQueueStatisticsPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 10),
    _HwhqosUserGroupQueueStatisticsPassPacketsRate_Type()
)
hwhqosUserGroupQueueStatisticsPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsPassPacketsRate.setStatus("current")
_HwhqosUserGroupQueueStatisticsPassBytesRate_Type = Counter64
_HwhqosUserGroupQueueStatisticsPassBytesRate_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsPassBytesRate = _HwhqosUserGroupQueueStatisticsPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 11),
    _HwhqosUserGroupQueueStatisticsPassBytesRate_Type()
)
hwhqosUserGroupQueueStatisticsPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsPassBytesRate.setStatus("current")
_HwhqosUserGroupQueueStatisticsDropPacketsRate_Type = Counter64
_HwhqosUserGroupQueueStatisticsDropPacketsRate_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsDropPacketsRate = _HwhqosUserGroupQueueStatisticsDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 12),
    _HwhqosUserGroupQueueStatisticsDropPacketsRate_Type()
)
hwhqosUserGroupQueueStatisticsDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsDropPacketsRate.setStatus("current")
_HwhqosUserGroupQueueStatisticsDropBytesRate_Type = Counter64
_HwhqosUserGroupQueueStatisticsDropBytesRate_Object = MibTableColumn
hwhqosUserGroupQueueStatisticsDropBytesRate = _HwhqosUserGroupQueueStatisticsDropBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 33, 1, 13),
    _HwhqosUserGroupQueueStatisticsDropBytesRate_Type()
)
hwhqosUserGroupQueueStatisticsDropBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsDropBytesRate.setStatus("current")
_HwhqosFlowQueueShaperTable_Object = MibTable
hwhqosFlowQueueShaperTable = _HwhqosFlowQueueShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34)
)
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperTable.setStatus("current")
_HwhqosFlowQueueShaperEntry_Object = MibTableRow
hwhqosFlowQueueShaperEntry = _HwhqosFlowQueueShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34, 1)
)
hwhqosFlowQueueShaperEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosFlowQueueName"),
)
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperEntry.setStatus("current")


class _HwhqosFlowQueueShaperBE_Type(Integer32):
    """Custom type hwhqosFlowQueueShaperBE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosFlowQueueShaperBE_Type.__name__ = "Integer32"
_HwhqosFlowQueueShaperBE_Object = MibTableColumn
hwhqosFlowQueueShaperBE = _HwhqosFlowQueueShaperBE_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34, 1, 1),
    _HwhqosFlowQueueShaperBE_Type()
)
hwhqosFlowQueueShaperBE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperBE.setStatus("current")


class _HwhqosFlowQueueShaperAF1_Type(Integer32):
    """Custom type hwhqosFlowQueueShaperAF1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosFlowQueueShaperAF1_Type.__name__ = "Integer32"
_HwhqosFlowQueueShaperAF1_Object = MibTableColumn
hwhqosFlowQueueShaperAF1 = _HwhqosFlowQueueShaperAF1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34, 1, 2),
    _HwhqosFlowQueueShaperAF1_Type()
)
hwhqosFlowQueueShaperAF1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperAF1.setStatus("current")


class _HwhqosFlowQueueShaperAF2_Type(Integer32):
    """Custom type hwhqosFlowQueueShaperAF2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosFlowQueueShaperAF2_Type.__name__ = "Integer32"
_HwhqosFlowQueueShaperAF2_Object = MibTableColumn
hwhqosFlowQueueShaperAF2 = _HwhqosFlowQueueShaperAF2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34, 1, 3),
    _HwhqosFlowQueueShaperAF2_Type()
)
hwhqosFlowQueueShaperAF2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperAF2.setStatus("current")


class _HwhqosFlowQueueShaperAF3_Type(Integer32):
    """Custom type hwhqosFlowQueueShaperAF3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosFlowQueueShaperAF3_Type.__name__ = "Integer32"
_HwhqosFlowQueueShaperAF3_Object = MibTableColumn
hwhqosFlowQueueShaperAF3 = _HwhqosFlowQueueShaperAF3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34, 1, 4),
    _HwhqosFlowQueueShaperAF3_Type()
)
hwhqosFlowQueueShaperAF3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperAF3.setStatus("current")


class _HwhqosFlowQueueShaperAF4_Type(Integer32):
    """Custom type hwhqosFlowQueueShaperAF4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosFlowQueueShaperAF4_Type.__name__ = "Integer32"
_HwhqosFlowQueueShaperAF4_Object = MibTableColumn
hwhqosFlowQueueShaperAF4 = _HwhqosFlowQueueShaperAF4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34, 1, 5),
    _HwhqosFlowQueueShaperAF4_Type()
)
hwhqosFlowQueueShaperAF4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperAF4.setStatus("current")


class _HwhqosFlowQueueShaperEF_Type(Integer32):
    """Custom type hwhqosFlowQueueShaperEF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosFlowQueueShaperEF_Type.__name__ = "Integer32"
_HwhqosFlowQueueShaperEF_Object = MibTableColumn
hwhqosFlowQueueShaperEF = _HwhqosFlowQueueShaperEF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34, 1, 6),
    _HwhqosFlowQueueShaperEF_Type()
)
hwhqosFlowQueueShaperEF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperEF.setStatus("current")


class _HwhqosFlowQueueShaperCS6_Type(Integer32):
    """Custom type hwhqosFlowQueueShaperCS6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosFlowQueueShaperCS6_Type.__name__ = "Integer32"
_HwhqosFlowQueueShaperCS6_Object = MibTableColumn
hwhqosFlowQueueShaperCS6 = _HwhqosFlowQueueShaperCS6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34, 1, 7),
    _HwhqosFlowQueueShaperCS6_Type()
)
hwhqosFlowQueueShaperCS6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperCS6.setStatus("current")


class _HwhqosFlowQueueShaperCS7_Type(Integer32):
    """Custom type hwhqosFlowQueueShaperCS7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosFlowQueueShaperCS7_Type.__name__ = "Integer32"
_HwhqosFlowQueueShaperCS7_Object = MibTableColumn
hwhqosFlowQueueShaperCS7 = _HwhqosFlowQueueShaperCS7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34, 1, 8),
    _HwhqosFlowQueueShaperCS7_Type()
)
hwhqosFlowQueueShaperCS7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperCS7.setStatus("current")


class _HwhqosFlowQueueShaperValue_Type(Integer32):
    """Custom type hwhqosFlowQueueShaperValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_HwhqosFlowQueueShaperValue_Type.__name__ = "Integer32"
_HwhqosFlowQueueShaperValue_Object = MibTableColumn
hwhqosFlowQueueShaperValue = _HwhqosFlowQueueShaperValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34, 1, 9),
    _HwhqosFlowQueueShaperValue_Type()
)
hwhqosFlowQueueShaperValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperValue.setStatus("current")
_HwhqosFlowQueueShaperRowStatus_Type = RowStatus
_HwhqosFlowQueueShaperRowStatus_Object = MibTableColumn
hwhqosFlowQueueShaperRowStatus = _HwhqosFlowQueueShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 34, 1, 50),
    _HwhqosFlowQueueShaperRowStatus_Type()
)
hwhqosFlowQueueShaperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperRowStatus.setStatus("current")
_HwhqosWredQueueDepthTable_Object = MibTable
hwhqosWredQueueDepthTable = _HwhqosWredQueueDepthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 35)
)
if mibBuilder.loadTexts:
    hwhqosWredQueueDepthTable.setStatus("current")
_HwhqosWredQueueDepthEntry_Object = MibTableRow
hwhqosWredQueueDepthEntry = _HwhqosWredQueueDepthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 35, 1)
)
hwhqosWredQueueDepthEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosWredQueueDepthType"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosWredQueueDepthWredName"),
)
if mibBuilder.loadTexts:
    hwhqosWredQueueDepthEntry.setStatus("current")


class _HwhqosWredQueueDepthType_Type(Integer32):
    """Custom type hwhqosWredQueueDepthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flowwred", 1),
          ("portwred", 2))
    )


_HwhqosWredQueueDepthType_Type.__name__ = "Integer32"
_HwhqosWredQueueDepthType_Object = MibTableColumn
hwhqosWredQueueDepthType = _HwhqosWredQueueDepthType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 35, 1, 1),
    _HwhqosWredQueueDepthType_Type()
)
hwhqosWredQueueDepthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosWredQueueDepthType.setStatus("current")


class _HwhqosWredQueueDepthWredName_Type(OctetString):
    """Custom type hwhqosWredQueueDepthWredName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosWredQueueDepthWredName_Type.__name__ = "OctetString"
_HwhqosWredQueueDepthWredName_Object = MibTableColumn
hwhqosWredQueueDepthWredName = _HwhqosWredQueueDepthWredName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 35, 1, 2),
    _HwhqosWredQueueDepthWredName_Type()
)
hwhqosWredQueueDepthWredName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosWredQueueDepthWredName.setStatus("current")


class _HwhqosWredQueueDepthValue_Type(Integer32):
    """Custom type hwhqosWredQueueDepthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131072),
    )


_HwhqosWredQueueDepthValue_Type.__name__ = "Integer32"
_HwhqosWredQueueDepthValue_Object = MibTableColumn
hwhqosWredQueueDepthValue = _HwhqosWredQueueDepthValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 35, 1, 3),
    _HwhqosWredQueueDepthValue_Type()
)
hwhqosWredQueueDepthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredQueueDepthValue.setStatus("current")
_HwhqosWredQueueDepthRowStatus_Type = RowStatus
_HwhqosWredQueueDepthRowStatus_Object = MibTableColumn
hwhqosWredQueueDepthRowStatus = _HwhqosWredQueueDepthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 35, 1, 50),
    _HwhqosWredQueueDepthRowStatus_Type()
)
hwhqosWredQueueDepthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosWredQueueDepthRowStatus.setStatus("current")
_HwhqosBandwidthCheckTable_Object = MibTable
hwhqosBandwidthCheckTable = _HwhqosBandwidthCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 36)
)
if mibBuilder.loadTexts:
    hwhqosBandwidthCheckTable.setStatus("current")
_HwhqosBandwidthCheckEntry_Object = MibTableRow
hwhqosBandwidthCheckEntry = _HwhqosBandwidthCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 36, 1)
)
hwhqosBandwidthCheckEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosBandwidthCheckInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosBandwidthCheckDirection"),
)
if mibBuilder.loadTexts:
    hwhqosBandwidthCheckEntry.setStatus("current")
_HwhqosBandwidthCheckInterfaceIndex_Type = InterfaceIndex
_HwhqosBandwidthCheckInterfaceIndex_Object = MibTableColumn
hwhqosBandwidthCheckInterfaceIndex = _HwhqosBandwidthCheckInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 36, 1, 1),
    _HwhqosBandwidthCheckInterfaceIndex_Type()
)
hwhqosBandwidthCheckInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosBandwidthCheckInterfaceIndex.setStatus("current")


class _HwhqosBandwidthCheckDirection_Type(Integer32):
    """Custom type hwhqosBandwidthCheckDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosBandwidthCheckDirection_Type.__name__ = "Integer32"
_HwhqosBandwidthCheckDirection_Object = MibTableColumn
hwhqosBandwidthCheckDirection = _HwhqosBandwidthCheckDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 36, 1, 2),
    _HwhqosBandwidthCheckDirection_Type()
)
hwhqosBandwidthCheckDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBandwidthCheckDirection.setStatus("current")


class _HwhqosBandwidthCheckValue_Type(Integer32):
    """Custom type hwhqosBandwidthCheckValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosBandwidthCheckValue_Type.__name__ = "Integer32"
_HwhqosBandwidthCheckValue_Object = MibTableColumn
hwhqosBandwidthCheckValue = _HwhqosBandwidthCheckValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 36, 1, 3),
    _HwhqosBandwidthCheckValue_Type()
)
hwhqosBandwidthCheckValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBandwidthCheckValue.setStatus("current")
_HwhqosBandwidthCheckRowStatus_Type = RowStatus
_HwhqosBandwidthCheckRowStatus_Object = MibTableColumn
hwhqosBandwidthCheckRowStatus = _HwhqosBandwidthCheckRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 36, 1, 50),
    _HwhqosBandwidthCheckRowStatus_Type()
)
hwhqosBandwidthCheckRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosBandwidthCheckRowStatus.setStatus("current")
_HwhqosServiceIdentifyPolicyTable_Object = MibTable
hwhqosServiceIdentifyPolicyTable = _HwhqosServiceIdentifyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 37)
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyTable.setStatus("current")
_HwhqosServiceIdentifyPolicyEntry_Object = MibTableRow
hwhqosServiceIdentifyPolicyEntry = _HwhqosServiceIdentifyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 37, 1)
)
hwhqosServiceIdentifyPolicyEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyName"),
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyEntry.setStatus("current")


class _HwhqosServiceIdentifyPolicyName_Type(OctetString):
    """Custom type hwhqosServiceIdentifyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosServiceIdentifyPolicyName_Type.__name__ = "OctetString"
_HwhqosServiceIdentifyPolicyName_Object = MibTableColumn
hwhqosServiceIdentifyPolicyName = _HwhqosServiceIdentifyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 37, 1, 1),
    _HwhqosServiceIdentifyPolicyName_Type()
)
hwhqosServiceIdentifyPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyName.setStatus("current")
_HwhqosServiceIdentifyPolicyRowStatus_Type = RowStatus
_HwhqosServiceIdentifyPolicyRowStatus_Object = MibTableColumn
hwhqosServiceIdentifyPolicyRowStatus = _HwhqosServiceIdentifyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 37, 1, 50),
    _HwhqosServiceIdentifyPolicyRowStatus_Type()
)
hwhqosServiceIdentifyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyRowStatus.setStatus("current")
_HwhqosServiceIdentifyPolicyApplyTable_Object = MibTable
hwhqosServiceIdentifyPolicyApplyTable = _HwhqosServiceIdentifyPolicyApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 38)
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyApplyTable.setStatus("current")
_HwhqosServiceIdentifyPolicyApplyEntry_Object = MibTableRow
hwhqosServiceIdentifyPolicyApplyEntry = _HwhqosServiceIdentifyPolicyApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 38, 1)
)
hwhqosServiceIdentifyPolicyApplyEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyApplyInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyApplyEntry.setStatus("current")
_HwhqosServiceIdentifyPolicyApplyInterfaceIndex_Type = InterfaceIndex
_HwhqosServiceIdentifyPolicyApplyInterfaceIndex_Object = MibTableColumn
hwhqosServiceIdentifyPolicyApplyInterfaceIndex = _HwhqosServiceIdentifyPolicyApplyInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 38, 1, 1),
    _HwhqosServiceIdentifyPolicyApplyInterfaceIndex_Type()
)
hwhqosServiceIdentifyPolicyApplyInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyApplyInterfaceIndex.setStatus("current")


class _HwhqosServiceIdentifyPolicyApplyName_Type(OctetString):
    """Custom type hwhqosServiceIdentifyPolicyApplyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosServiceIdentifyPolicyApplyName_Type.__name__ = "OctetString"
_HwhqosServiceIdentifyPolicyApplyName_Object = MibTableColumn
hwhqosServiceIdentifyPolicyApplyName = _HwhqosServiceIdentifyPolicyApplyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 38, 1, 2),
    _HwhqosServiceIdentifyPolicyApplyName_Type()
)
hwhqosServiceIdentifyPolicyApplyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyApplyName.setStatus("current")
_HwhqosServiceIdentifyPolicyApplyRowStatus_Type = RowStatus
_HwhqosServiceIdentifyPolicyApplyRowStatus_Object = MibTableColumn
hwhqosServiceIdentifyPolicyApplyRowStatus = _HwhqosServiceIdentifyPolicyApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 38, 1, 50),
    _HwhqosServiceIdentifyPolicyApplyRowStatus_Type()
)
hwhqosServiceIdentifyPolicyApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyApplyRowStatus.setStatus("current")
_HwhqosServiceIdentifyPolicyTypeTable_Object = MibTable
hwhqosServiceIdentifyPolicyTypeTable = _HwhqosServiceIdentifyPolicyTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 39)
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyTypeTable.setStatus("current")
_HwhqosServiceIdentifyPolicyTypeEntry_Object = MibTableRow
hwhqosServiceIdentifyPolicyTypeEntry = _HwhqosServiceIdentifyPolicyTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 39, 1)
)
hwhqosServiceIdentifyPolicyTypeEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyName"),
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyTypeEntry.setStatus("current")


class _HwhqosServiceIdentifyPolicyTypeValue_Type(Integer32):
    """Custom type hwhqosServiceIdentifyPolicyTypeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cosinnervlan", 3),
          ("cosoutervlan", 4),
          ("dhcpoption60", 6),
          ("dscp", 5),
          ("innervlan", 1),
          ("outervlan", 2))
    )


_HwhqosServiceIdentifyPolicyTypeValue_Type.__name__ = "Integer32"
_HwhqosServiceIdentifyPolicyTypeValue_Object = MibTableColumn
hwhqosServiceIdentifyPolicyTypeValue = _HwhqosServiceIdentifyPolicyTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 39, 1, 1),
    _HwhqosServiceIdentifyPolicyTypeValue_Type()
)
hwhqosServiceIdentifyPolicyTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyTypeValue.setStatus("current")
_HwhqosServiceIdentifyPolicyTypeRowStatus_Type = RowStatus
_HwhqosServiceIdentifyPolicyTypeRowStatus_Object = MibTableColumn
hwhqosServiceIdentifyPolicyTypeRowStatus = _HwhqosServiceIdentifyPolicyTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 39, 1, 50),
    _HwhqosServiceIdentifyPolicyTypeRowStatus_Type()
)
hwhqosServiceIdentifyPolicyTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyTypeRowStatus.setStatus("current")
_HwhqosServiceIdentifyPolicyVlanTable_Object = MibTable
hwhqosServiceIdentifyPolicyVlanTable = _HwhqosServiceIdentifyPolicyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 40)
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyVlanTable.setStatus("current")
_HwhqosServiceIdentifyPolicyVlanEntry_Object = MibTableRow
hwhqosServiceIdentifyPolicyVlanEntry = _HwhqosServiceIdentifyPolicyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 40, 1)
)
hwhqosServiceIdentifyPolicyVlanEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyVlanID"),
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyVlanEntry.setStatus("current")


class _HwhqosServiceIdentifyPolicyVlanID_Type(Integer32):
    """Custom type hwhqosServiceIdentifyPolicyVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwhqosServiceIdentifyPolicyVlanID_Type.__name__ = "Integer32"
_HwhqosServiceIdentifyPolicyVlanID_Object = MibTableColumn
hwhqosServiceIdentifyPolicyVlanID = _HwhqosServiceIdentifyPolicyVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 40, 1, 1),
    _HwhqosServiceIdentifyPolicyVlanID_Type()
)
hwhqosServiceIdentifyPolicyVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyVlanID.setStatus("current")


class _HwhqosServiceIdentifyPolicyVlanDomainName_Type(OctetString):
    """Custom type hwhqosServiceIdentifyPolicyVlanDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosServiceIdentifyPolicyVlanDomainName_Type.__name__ = "OctetString"
_HwhqosServiceIdentifyPolicyVlanDomainName_Object = MibTableColumn
hwhqosServiceIdentifyPolicyVlanDomainName = _HwhqosServiceIdentifyPolicyVlanDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 40, 1, 2),
    _HwhqosServiceIdentifyPolicyVlanDomainName_Type()
)
hwhqosServiceIdentifyPolicyVlanDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyVlanDomainName.setStatus("current")
_HwhqosServiceIdentifyPolicyVlanRowStatus_Type = RowStatus
_HwhqosServiceIdentifyPolicyVlanRowStatus_Object = MibTableColumn
hwhqosServiceIdentifyPolicyVlanRowStatus = _HwhqosServiceIdentifyPolicyVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 40, 1, 50),
    _HwhqosServiceIdentifyPolicyVlanRowStatus_Type()
)
hwhqosServiceIdentifyPolicyVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyVlanRowStatus.setStatus("current")
_HwhqosServiceIdentifyPolicy8021pTable_Object = MibTable
hwhqosServiceIdentifyPolicy8021pTable = _HwhqosServiceIdentifyPolicy8021pTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 41)
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicy8021pTable.setStatus("current")
_HwhqosServiceIdentifyPolicy8021pEntry_Object = MibTableRow
hwhqosServiceIdentifyPolicy8021pEntry = _HwhqosServiceIdentifyPolicy8021pEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 41, 1)
)
hwhqosServiceIdentifyPolicy8021pEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicy8021pCosID"),
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicy8021pEntry.setStatus("current")


class _HwhqosServiceIdentifyPolicy8021pCosID_Type(Integer32):
    """Custom type hwhqosServiceIdentifyPolicy8021pCosID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwhqosServiceIdentifyPolicy8021pCosID_Type.__name__ = "Integer32"
_HwhqosServiceIdentifyPolicy8021pCosID_Object = MibTableColumn
hwhqosServiceIdentifyPolicy8021pCosID = _HwhqosServiceIdentifyPolicy8021pCosID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 41, 1, 1),
    _HwhqosServiceIdentifyPolicy8021pCosID_Type()
)
hwhqosServiceIdentifyPolicy8021pCosID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicy8021pCosID.setStatus("current")


class _HwhqosServiceIdentifyPolicy8021pDomainName_Type(OctetString):
    """Custom type hwhqosServiceIdentifyPolicy8021pDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosServiceIdentifyPolicy8021pDomainName_Type.__name__ = "OctetString"
_HwhqosServiceIdentifyPolicy8021pDomainName_Object = MibTableColumn
hwhqosServiceIdentifyPolicy8021pDomainName = _HwhqosServiceIdentifyPolicy8021pDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 41, 1, 2),
    _HwhqosServiceIdentifyPolicy8021pDomainName_Type()
)
hwhqosServiceIdentifyPolicy8021pDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicy8021pDomainName.setStatus("current")
_HwhqosServiceIdentifyPolicy8021pRowStatus_Type = RowStatus
_HwhqosServiceIdentifyPolicy8021pRowStatus_Object = MibTableColumn
hwhqosServiceIdentifyPolicy8021pRowStatus = _HwhqosServiceIdentifyPolicy8021pRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 41, 1, 50),
    _HwhqosServiceIdentifyPolicy8021pRowStatus_Type()
)
hwhqosServiceIdentifyPolicy8021pRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicy8021pRowStatus.setStatus("current")
_HwhqosServiceIdentifyPolicyDscpTable_Object = MibTable
hwhqosServiceIdentifyPolicyDscpTable = _HwhqosServiceIdentifyPolicyDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 42)
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyDscpTable.setStatus("current")
_HwhqosServiceIdentifyPolicyDscpEntry_Object = MibTableRow
hwhqosServiceIdentifyPolicyDscpEntry = _HwhqosServiceIdentifyPolicyDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 42, 1)
)
hwhqosServiceIdentifyPolicyDscpEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyDscpID"),
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyDscpEntry.setStatus("current")


class _HwhqosServiceIdentifyPolicyDscpID_Type(Integer32):
    """Custom type hwhqosServiceIdentifyPolicyDscpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwhqosServiceIdentifyPolicyDscpID_Type.__name__ = "Integer32"
_HwhqosServiceIdentifyPolicyDscpID_Object = MibTableColumn
hwhqosServiceIdentifyPolicyDscpID = _HwhqosServiceIdentifyPolicyDscpID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 42, 1, 1),
    _HwhqosServiceIdentifyPolicyDscpID_Type()
)
hwhqosServiceIdentifyPolicyDscpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyDscpID.setStatus("current")


class _HwhqosServiceIdentifyPolicyDscpDomainName_Type(OctetString):
    """Custom type hwhqosServiceIdentifyPolicyDscpDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosServiceIdentifyPolicyDscpDomainName_Type.__name__ = "OctetString"
_HwhqosServiceIdentifyPolicyDscpDomainName_Object = MibTableColumn
hwhqosServiceIdentifyPolicyDscpDomainName = _HwhqosServiceIdentifyPolicyDscpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 42, 1, 2),
    _HwhqosServiceIdentifyPolicyDscpDomainName_Type()
)
hwhqosServiceIdentifyPolicyDscpDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyDscpDomainName.setStatus("current")
_HwhqosServiceIdentifyPolicyDscpRowStatus_Type = RowStatus
_HwhqosServiceIdentifyPolicyDscpRowStatus_Object = MibTableColumn
hwhqosServiceIdentifyPolicyDscpRowStatus = _HwhqosServiceIdentifyPolicyDscpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 42, 1, 50),
    _HwhqosServiceIdentifyPolicyDscpRowStatus_Type()
)
hwhqosServiceIdentifyPolicyDscpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyDscpRowStatus.setStatus("current")
_HwhqosServiceIdentifyPolicyOption60Table_Object = MibTable
hwhqosServiceIdentifyPolicyOption60Table = _HwhqosServiceIdentifyPolicyOption60Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 43)
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyOption60Table.setStatus("current")
_HwhqosServiceIdentifyPolicyOption60Entry_Object = MibTableRow
hwhqosServiceIdentifyPolicyOption60Entry = _HwhqosServiceIdentifyPolicyOption60Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 43, 1)
)
hwhqosServiceIdentifyPolicyOption60Entry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyName"),
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyOption60Entry.setStatus("current")


class _HwhqosServiceIdentifyPolicyOption60_Type(Integer32):
    """Custom type hwhqosServiceIdentifyPolicyOption60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosServiceIdentifyPolicyOption60_Type.__name__ = "Integer32"
_HwhqosServiceIdentifyPolicyOption60_Object = MibTableColumn
hwhqosServiceIdentifyPolicyOption60 = _HwhqosServiceIdentifyPolicyOption60_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 43, 1, 1),
    _HwhqosServiceIdentifyPolicyOption60_Type()
)
hwhqosServiceIdentifyPolicyOption60.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyOption60.setStatus("current")
_HwhqosServiceIdentifyPolicyOption60RowStatus_Type = RowStatus
_HwhqosServiceIdentifyPolicyOption60RowStatus_Object = MibTableColumn
hwhqosServiceIdentifyPolicyOption60RowStatus = _HwhqosServiceIdentifyPolicyOption60RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 43, 1, 50),
    _HwhqosServiceIdentifyPolicyOption60RowStatus_Type()
)
hwhqosServiceIdentifyPolicyOption60RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyOption60RowStatus.setStatus("current")
_HwhqosDomainRateLimitModeTable_Object = MibTable
hwhqosDomainRateLimitModeTable = _HwhqosDomainRateLimitModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 44)
)
if mibBuilder.loadTexts:
    hwhqosDomainRateLimitModeTable.setStatus("current")
_HwhqosDomainRateLimitModeEntry_Object = MibTableRow
hwhqosDomainRateLimitModeEntry = _HwhqosDomainRateLimitModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 44, 1)
)
hwhqosDomainRateLimitModeEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosDomainRateLimitModeDomainName"),
)
if mibBuilder.loadTexts:
    hwhqosDomainRateLimitModeEntry.setStatus("current")


class _HwhqosDomainRateLimitModeDomainName_Type(OctetString):
    """Custom type hwhqosDomainRateLimitModeDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosDomainRateLimitModeDomainName_Type.__name__ = "OctetString"
_HwhqosDomainRateLimitModeDomainName_Object = MibTableColumn
hwhqosDomainRateLimitModeDomainName = _HwhqosDomainRateLimitModeDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 44, 1, 1),
    _HwhqosDomainRateLimitModeDomainName_Type()
)
hwhqosDomainRateLimitModeDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosDomainRateLimitModeDomainName.setStatus("current")


class _HwhqosDomainRateLimitModeDirection_Type(Integer32):
    """Custom type hwhqosDomainRateLimitModeDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosDomainRateLimitModeDirection_Type.__name__ = "Integer32"
_HwhqosDomainRateLimitModeDirection_Object = MibTableColumn
hwhqosDomainRateLimitModeDirection = _HwhqosDomainRateLimitModeDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 44, 1, 2),
    _HwhqosDomainRateLimitModeDirection_Type()
)
hwhqosDomainRateLimitModeDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosDomainRateLimitModeDirection.setStatus("current")


class _HwhqosDomainRateLimitModeRateLimitMode_Type(Integer32):
    """Custom type hwhqosDomainRateLimitModeRateLimitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("car", 2),
          ("sq", 1))
    )


_HwhqosDomainRateLimitModeRateLimitMode_Type.__name__ = "Integer32"
_HwhqosDomainRateLimitModeRateLimitMode_Object = MibTableColumn
hwhqosDomainRateLimitModeRateLimitMode = _HwhqosDomainRateLimitModeRateLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 44, 1, 3),
    _HwhqosDomainRateLimitModeRateLimitMode_Type()
)
hwhqosDomainRateLimitModeRateLimitMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosDomainRateLimitModeRateLimitMode.setStatus("current")
_HwhqosDomainRateLimitModeRowStatus_Type = RowStatus
_HwhqosDomainRateLimitModeRowStatus_Object = MibTableColumn
hwhqosDomainRateLimitModeRowStatus = _HwhqosDomainRateLimitModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 44, 1, 50),
    _HwhqosDomainRateLimitModeRowStatus_Type()
)
hwhqosDomainRateLimitModeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosDomainRateLimitModeRowStatus.setStatus("current")
_HwhqosDomainSessionGroupExcludeTable_Object = MibTable
hwhqosDomainSessionGroupExcludeTable = _HwhqosDomainSessionGroupExcludeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 45)
)
if mibBuilder.loadTexts:
    hwhqosDomainSessionGroupExcludeTable.setStatus("current")
_HwhqosDomainSessionGroupExcludeEntry_Object = MibTableRow
hwhqosDomainSessionGroupExcludeEntry = _HwhqosDomainSessionGroupExcludeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 45, 1)
)
hwhqosDomainSessionGroupExcludeEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosDomainSessionGroupExcludeDomainName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosDomainSessionGroupExcludeDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosDomainSessionGroupExcludeMode"),
)
if mibBuilder.loadTexts:
    hwhqosDomainSessionGroupExcludeEntry.setStatus("current")


class _HwhqosDomainSessionGroupExcludeDomainName_Type(OctetString):
    """Custom type hwhqosDomainSessionGroupExcludeDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosDomainSessionGroupExcludeDomainName_Type.__name__ = "OctetString"
_HwhqosDomainSessionGroupExcludeDomainName_Object = MibTableColumn
hwhqosDomainSessionGroupExcludeDomainName = _HwhqosDomainSessionGroupExcludeDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 45, 1, 1),
    _HwhqosDomainSessionGroupExcludeDomainName_Type()
)
hwhqosDomainSessionGroupExcludeDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosDomainSessionGroupExcludeDomainName.setStatus("current")


class _HwhqosDomainSessionGroupExcludeDirection_Type(Integer32):
    """Custom type hwhqosDomainSessionGroupExcludeDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosDomainSessionGroupExcludeDirection_Type.__name__ = "Integer32"
_HwhqosDomainSessionGroupExcludeDirection_Object = MibTableColumn
hwhqosDomainSessionGroupExcludeDirection = _HwhqosDomainSessionGroupExcludeDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 45, 1, 2),
    _HwhqosDomainSessionGroupExcludeDirection_Type()
)
hwhqosDomainSessionGroupExcludeDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosDomainSessionGroupExcludeDirection.setStatus("current")


class _HwhqosDomainSessionGroupExcludeMode_Type(Integer32):
    """Custom type hwhqosDomainSessionGroupExcludeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("car", 2),
          ("sq", 1))
    )


_HwhqosDomainSessionGroupExcludeMode_Type.__name__ = "Integer32"
_HwhqosDomainSessionGroupExcludeMode_Object = MibTableColumn
hwhqosDomainSessionGroupExcludeMode = _HwhqosDomainSessionGroupExcludeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 45, 1, 3),
    _HwhqosDomainSessionGroupExcludeMode_Type()
)
hwhqosDomainSessionGroupExcludeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosDomainSessionGroupExcludeMode.setStatus("current")
_HwhqosDomainSessionGroupExcludeRowStatus_Type = RowStatus
_HwhqosDomainSessionGroupExcludeRowStatus_Object = MibTableColumn
hwhqosDomainSessionGroupExcludeRowStatus = _HwhqosDomainSessionGroupExcludeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 45, 1, 50),
    _HwhqosDomainSessionGroupExcludeRowStatus_Type()
)
hwhqosDomainSessionGroupExcludeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosDomainSessionGroupExcludeRowStatus.setStatus("current")
_HwhqosDomainUserMaxSessionTable_Object = MibTable
hwhqosDomainUserMaxSessionTable = _HwhqosDomainUserMaxSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 46)
)
if mibBuilder.loadTexts:
    hwhqosDomainUserMaxSessionTable.setStatus("current")
_HwhqosDomainUserMaxSessionEntry_Object = MibTableRow
hwhqosDomainUserMaxSessionEntry = _HwhqosDomainUserMaxSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 46, 1)
)
hwhqosDomainUserMaxSessionEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosDomainUserMaxSessionDomainName"),
)
if mibBuilder.loadTexts:
    hwhqosDomainUserMaxSessionEntry.setStatus("current")


class _HwhqosDomainUserMaxSessionDomainName_Type(OctetString):
    """Custom type hwhqosDomainUserMaxSessionDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosDomainUserMaxSessionDomainName_Type.__name__ = "OctetString"
_HwhqosDomainUserMaxSessionDomainName_Object = MibTableColumn
hwhqosDomainUserMaxSessionDomainName = _HwhqosDomainUserMaxSessionDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 46, 1, 1),
    _HwhqosDomainUserMaxSessionDomainName_Type()
)
hwhqosDomainUserMaxSessionDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosDomainUserMaxSessionDomainName.setStatus("current")


class _HwhqosDomainUserMaxSessionNum_Type(Integer32):
    """Custom type hwhqosDomainUserMaxSessionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 147456),
    )


_HwhqosDomainUserMaxSessionNum_Type.__name__ = "Integer32"
_HwhqosDomainUserMaxSessionNum_Object = MibTableColumn
hwhqosDomainUserMaxSessionNum = _HwhqosDomainUserMaxSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 46, 1, 2),
    _HwhqosDomainUserMaxSessionNum_Type()
)
hwhqosDomainUserMaxSessionNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosDomainUserMaxSessionNum.setStatus("current")
_HwhqosDomainUserMaxSessionRowStatus_Type = RowStatus
_HwhqosDomainUserMaxSessionRowStatus_Object = MibTableColumn
hwhqosDomainUserMaxSessionRowStatus = _HwhqosDomainUserMaxSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 46, 1, 50),
    _HwhqosDomainUserMaxSessionRowStatus_Type()
)
hwhqosDomainUserMaxSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosDomainUserMaxSessionRowStatus.setStatus("current")
_HwhqosUpdateUseridProfileTable_Object = MibTable
hwhqosUpdateUseridProfileTable = _HwhqosUpdateUseridProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 47)
)
if mibBuilder.loadTexts:
    hwhqosUpdateUseridProfileTable.setStatus("current")
_HwhqosUpdateUseridProfileEntry_Object = MibTableRow
hwhqosUpdateUseridProfileEntry = _HwhqosUpdateUseridProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 47, 1)
)
hwhqosUpdateUseridProfileEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUpdateUseridProfileUserid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUpdateUseridProfileDirection"),
)
if mibBuilder.loadTexts:
    hwhqosUpdateUseridProfileEntry.setStatus("current")


class _HwhqosUpdateUseridProfileUserid_Type(Integer32):
    """Custom type hwhqosUpdateUseridProfileUserid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 164864),
    )


_HwhqosUpdateUseridProfileUserid_Type.__name__ = "Integer32"
_HwhqosUpdateUseridProfileUserid_Object = MibTableColumn
hwhqosUpdateUseridProfileUserid = _HwhqosUpdateUseridProfileUserid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 47, 1, 1),
    _HwhqosUpdateUseridProfileUserid_Type()
)
hwhqosUpdateUseridProfileUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUpdateUseridProfileUserid.setStatus("current")


class _HwhqosUpdateUseridProfileDirection_Type(Integer32):
    """Custom type hwhqosUpdateUseridProfileDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosUpdateUseridProfileDirection_Type.__name__ = "Integer32"
_HwhqosUpdateUseridProfileDirection_Object = MibTableColumn
hwhqosUpdateUseridProfileDirection = _HwhqosUpdateUseridProfileDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 47, 1, 2),
    _HwhqosUpdateUseridProfileDirection_Type()
)
hwhqosUpdateUseridProfileDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUpdateUseridProfileDirection.setStatus("current")


class _HwhqosUpdateUseridProfileName_Type(OctetString):
    """Custom type hwhqosUpdateUseridProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwhqosUpdateUseridProfileName_Type.__name__ = "OctetString"
_HwhqosUpdateUseridProfileName_Object = MibTableColumn
hwhqosUpdateUseridProfileName = _HwhqosUpdateUseridProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 47, 1, 3),
    _HwhqosUpdateUseridProfileName_Type()
)
hwhqosUpdateUseridProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUpdateUseridProfileName.setStatus("current")
_HwhqosUpdateUseridProfileRowStatus_Type = RowStatus
_HwhqosUpdateUseridProfileRowStatus_Object = MibTableColumn
hwhqosUpdateUseridProfileRowStatus = _HwhqosUpdateUseridProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 47, 1, 50),
    _HwhqosUpdateUseridProfileRowStatus_Type()
)
hwhqosUpdateUseridProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUpdateUseridProfileRowStatus.setStatus("current")
_HwhqosDomainUserPriorityTable_Object = MibTable
hwhqosDomainUserPriorityTable = _HwhqosDomainUserPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 48)
)
if mibBuilder.loadTexts:
    hwhqosDomainUserPriorityTable.setStatus("current")
_HwhqosDomainUserPriorityEntry_Object = MibTableRow
hwhqosDomainUserPriorityEntry = _HwhqosDomainUserPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 48, 1)
)
hwhqosDomainUserPriorityEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosDomainUserPriorityDomainName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosDomainUserPriorityDirection"),
)
if mibBuilder.loadTexts:
    hwhqosDomainUserPriorityEntry.setStatus("current")


class _HwhqosDomainUserPriorityDomainName_Type(OctetString):
    """Custom type hwhqosDomainUserPriorityDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosDomainUserPriorityDomainName_Type.__name__ = "OctetString"
_HwhqosDomainUserPriorityDomainName_Object = MibTableColumn
hwhqosDomainUserPriorityDomainName = _HwhqosDomainUserPriorityDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 48, 1, 1),
    _HwhqosDomainUserPriorityDomainName_Type()
)
hwhqosDomainUserPriorityDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosDomainUserPriorityDomainName.setStatus("current")


class _HwhqosDomainUserPriorityDirection_Type(Integer32):
    """Custom type hwhqosDomainUserPriorityDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosDomainUserPriorityDirection_Type.__name__ = "Integer32"
_HwhqosDomainUserPriorityDirection_Object = MibTableColumn
hwhqosDomainUserPriorityDirection = _HwhqosDomainUserPriorityDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 48, 1, 2),
    _HwhqosDomainUserPriorityDirection_Type()
)
hwhqosDomainUserPriorityDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosDomainUserPriorityDirection.setStatus("current")


class _HwhqosDomainUserPriorityValue_Type(Integer32):
    """Custom type hwhqosDomainUserPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 1),
          ("priority1", 2),
          ("priority2", 3),
          ("priority3", 4),
          ("priority4", 5),
          ("priority5", 6),
          ("priority6", 7),
          ("priority7", 8),
          ("trust8021pinner", 9),
          ("trust8021pouter", 10),
          ("trustdscpinner", 13),
          ("trustdscpouter", 14),
          ("trustexpinner", 11),
          ("trustexpouter", 12),
          ("unchangeable", 15))
    )


_HwhqosDomainUserPriorityValue_Type.__name__ = "Integer32"
_HwhqosDomainUserPriorityValue_Object = MibTableColumn
hwhqosDomainUserPriorityValue = _HwhqosDomainUserPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 48, 1, 3),
    _HwhqosDomainUserPriorityValue_Type()
)
hwhqosDomainUserPriorityValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosDomainUserPriorityValue.setStatus("current")
_HwhqosDomainUserPriorityRowStatus_Type = RowStatus
_HwhqosDomainUserPriorityRowStatus_Object = MibTableColumn
hwhqosDomainUserPriorityRowStatus = _HwhqosDomainUserPriorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 48, 1, 50),
    _HwhqosDomainUserPriorityRowStatus_Type()
)
hwhqosDomainUserPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosDomainUserPriorityRowStatus.setStatus("current")
_HwhqosTMScheduleModeTable_Object = MibTable
hwhqosTMScheduleModeTable = _HwhqosTMScheduleModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 50)
)
if mibBuilder.loadTexts:
    hwhqosTMScheduleModeTable.setStatus("current")
_HwhqosTMScheduleModeEntry_Object = MibTableRow
hwhqosTMScheduleModeEntry = _HwhqosTMScheduleModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 50, 1)
)
hwhqosTMScheduleModeEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosTMScheduleModeSlot"),
)
if mibBuilder.loadTexts:
    hwhqosTMScheduleModeEntry.setStatus("current")


class _HwhqosTMScheduleModeSlot_Type(Integer32):
    """Custom type hwhqosTMScheduleModeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwhqosTMScheduleModeSlot_Type.__name__ = "Integer32"
_HwhqosTMScheduleModeSlot_Object = MibTableColumn
hwhqosTMScheduleModeSlot = _HwhqosTMScheduleModeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 50, 1, 1),
    _HwhqosTMScheduleModeSlot_Type()
)
hwhqosTMScheduleModeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosTMScheduleModeSlot.setStatus("current")


class _HwhqosTMScheduleModeSimpleEnable_Type(Integer32):
    """Custom type hwhqosTMScheduleModeSimpleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("simple", 1)
    )


_HwhqosTMScheduleModeSimpleEnable_Type.__name__ = "Integer32"
_HwhqosTMScheduleModeSimpleEnable_Object = MibTableColumn
hwhqosTMScheduleModeSimpleEnable = _HwhqosTMScheduleModeSimpleEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 50, 1, 2),
    _HwhqosTMScheduleModeSimpleEnable_Type()
)
hwhqosTMScheduleModeSimpleEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosTMScheduleModeSimpleEnable.setStatus("current")
_HwhqosTMScheduleModeRowStatus_Type = RowStatus
_HwhqosTMScheduleModeRowStatus_Object = MibTableColumn
hwhqosTMScheduleModeRowStatus = _HwhqosTMScheduleModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 50, 1, 50),
    _HwhqosTMScheduleModeRowStatus_Type()
)
hwhqosTMScheduleModeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosTMScheduleModeRowStatus.setStatus("current")
_HwhqosUserBandwidthTable_Object = MibTable
hwhqosUserBandwidthTable = _HwhqosUserBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 51)
)
if mibBuilder.loadTexts:
    hwhqosUserBandwidthTable.setStatus("current")
_HwhqosUserBandwidthEntry_Object = MibTableRow
hwhqosUserBandwidthEntry = _HwhqosUserBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 51, 1)
)
hwhqosUserBandwidthEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserBandwidthUserid"),
)
if mibBuilder.loadTexts:
    hwhqosUserBandwidthEntry.setStatus("current")


class _HwhqosUserBandwidthUserid_Type(Integer32):
    """Custom type hwhqosUserBandwidthUserid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 164864),
    )


_HwhqosUserBandwidthUserid_Type.__name__ = "Integer32"
_HwhqosUserBandwidthUserid_Object = MibTableColumn
hwhqosUserBandwidthUserid = _HwhqosUserBandwidthUserid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 51, 1, 1),
    _HwhqosUserBandwidthUserid_Type()
)
hwhqosUserBandwidthUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserBandwidthUserid.setStatus("current")
_HwhqosUserBandwidthCir_Type = Integer32
_HwhqosUserBandwidthCir_Object = MibTableColumn
hwhqosUserBandwidthCir = _HwhqosUserBandwidthCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 51, 1, 2),
    _HwhqosUserBandwidthCir_Type()
)
hwhqosUserBandwidthCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserBandwidthCir.setStatus("current")
_HwhqosUserBandwidthPir_Type = Integer32
_HwhqosUserBandwidthPir_Object = MibTableColumn
hwhqosUserBandwidthPir = _HwhqosUserBandwidthPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 51, 1, 3),
    _HwhqosUserBandwidthPir_Type()
)
hwhqosUserBandwidthPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserBandwidthPir.setStatus("current")
_HwhqosUserBandwidthCommittedCir_Type = Integer32
_HwhqosUserBandwidthCommittedCir_Object = MibTableColumn
hwhqosUserBandwidthCommittedCir = _HwhqosUserBandwidthCommittedCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 51, 1, 4),
    _HwhqosUserBandwidthCommittedCir_Type()
)
hwhqosUserBandwidthCommittedCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserBandwidthCommittedCir.setStatus("current")
_HwhqosUserBandwidthRowStatus_Type = RowStatus
_HwhqosUserBandwidthRowStatus_Object = MibTableColumn
hwhqosUserBandwidthRowStatus = _HwhqosUserBandwidthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 51, 1, 50),
    _HwhqosUserBandwidthRowStatus_Type()
)
hwhqosUserBandwidthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserBandwidthRowStatus.setStatus("current")
_HwhqosUseridStatTable_Object = MibTable
hwhqosUseridStatTable = _HwhqosUseridStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52)
)
if mibBuilder.loadTexts:
    hwhqosUseridStatTable.setStatus("current")
_HwhqosUseridStatEntry_Object = MibTableRow
hwhqosUseridStatEntry = _HwhqosUseridStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1)
)
hwhqosUseridStatEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUseridStatUserid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUseridStatQueue"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUseridStatDirection"),
)
if mibBuilder.loadTexts:
    hwhqosUseridStatEntry.setStatus("current")


class _HwhqosUseridStatUserid_Type(Integer32):
    """Custom type hwhqosUseridStatUserid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 164864),
    )


_HwhqosUseridStatUserid_Type.__name__ = "Integer32"
_HwhqosUseridStatUserid_Object = MibTableColumn
hwhqosUseridStatUserid = _HwhqosUseridStatUserid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 1),
    _HwhqosUseridStatUserid_Type()
)
hwhqosUseridStatUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUseridStatUserid.setStatus("current")


class _HwhqosUseridStatQueue_Type(Integer32):
    """Custom type hwhqosUseridStatQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("total", 9))
    )


_HwhqosUseridStatQueue_Type.__name__ = "Integer32"
_HwhqosUseridStatQueue_Object = MibTableColumn
hwhqosUseridStatQueue = _HwhqosUseridStatQueue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 2),
    _HwhqosUseridStatQueue_Type()
)
hwhqosUseridStatQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUseridStatQueue.setStatus("current")


class _HwhqosUseridStatDirection_Type(Integer32):
    """Custom type hwhqosUseridStatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosUseridStatDirection_Type.__name__ = "Integer32"
_HwhqosUseridStatDirection_Object = MibTableColumn
hwhqosUseridStatDirection = _HwhqosUseridStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 3),
    _HwhqosUseridStatDirection_Type()
)
hwhqosUseridStatDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUseridStatDirection.setStatus("current")
_HwhqosUseridStatPassBytes_Type = Counter64
_HwhqosUseridStatPassBytes_Object = MibTableColumn
hwhqosUseridStatPassBytes = _HwhqosUseridStatPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 4),
    _HwhqosUseridStatPassBytes_Type()
)
hwhqosUseridStatPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUseridStatPassBytes.setStatus("current")
_HwhqosUseridStatDropBytes_Type = Counter64
_HwhqosUseridStatDropBytes_Object = MibTableColumn
hwhqosUseridStatDropBytes = _HwhqosUseridStatDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 5),
    _HwhqosUseridStatDropBytes_Type()
)
hwhqosUseridStatDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUseridStatDropBytes.setStatus("current")
_HwhqosUseridStatPassPackets_Type = Counter64
_HwhqosUseridStatPassPackets_Object = MibTableColumn
hwhqosUseridStatPassPackets = _HwhqosUseridStatPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 6),
    _HwhqosUseridStatPassPackets_Type()
)
hwhqosUseridStatPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUseridStatPassPackets.setStatus("current")
_HwhqosUseridStatDropPackets_Type = Counter64
_HwhqosUseridStatDropPackets_Object = MibTableColumn
hwhqosUseridStatDropPackets = _HwhqosUseridStatDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 7),
    _HwhqosUseridStatDropPackets_Type()
)
hwhqosUseridStatDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUseridStatDropPackets.setStatus("current")
_HwhqosUseridStatPassPacketsRate_Type = Counter64
_HwhqosUseridStatPassPacketsRate_Object = MibTableColumn
hwhqosUseridStatPassPacketsRate = _HwhqosUseridStatPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 8),
    _HwhqosUseridStatPassPacketsRate_Type()
)
hwhqosUseridStatPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUseridStatPassPacketsRate.setStatus("current")
_HwhqosUseridStatDropPacketsRate_Type = Counter64
_HwhqosUseridStatDropPacketsRate_Object = MibTableColumn
hwhqosUseridStatDropPacketsRate = _HwhqosUseridStatDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 9),
    _HwhqosUseridStatDropPacketsRate_Type()
)
hwhqosUseridStatDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUseridStatDropPacketsRate.setStatus("current")


class _HwhqosUseridStatReset_Type(Integer32):
    """Custom type hwhqosUseridStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwhqosUseridStatReset_Type.__name__ = "Integer32"
_HwhqosUseridStatReset_Object = MibTableColumn
hwhqosUseridStatReset = _HwhqosUseridStatReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 10),
    _HwhqosUseridStatReset_Type()
)
hwhqosUseridStatReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUseridStatReset.setStatus("current")
_HwhqosUseridStatPassBytesRate_Type = Counter64
_HwhqosUseridStatPassBytesRate_Object = MibTableColumn
hwhqosUseridStatPassBytesRate = _HwhqosUseridStatPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 11),
    _HwhqosUseridStatPassBytesRate_Type()
)
hwhqosUseridStatPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUseridStatPassBytesRate.setStatus("current")
_HwhqosUseridStatDropBytesRate_Type = Counter64
_HwhqosUseridStatDropBytesRate_Object = MibTableColumn
hwhqosUseridStatDropBytesRate = _HwhqosUseridStatDropBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 52, 1, 12),
    _HwhqosUseridStatDropBytesRate_Type()
)
hwhqosUseridStatDropBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUseridStatDropBytesRate.setStatus("current")
_HwhqosFatherUserGroupQueueApplyTable_Object = MibTable
hwhqosFatherUserGroupQueueApplyTable = _HwhqosFatherUserGroupQueueApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 53)
)
if mibBuilder.loadTexts:
    hwhqosFatherUserGroupQueueApplyTable.setStatus("current")
_HwhqosFatherUserGroupQueueApplyEntry_Object = MibTableRow
hwhqosFatherUserGroupQueueApplyEntry = _HwhqosFatherUserGroupQueueApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 53, 1)
)
hwhqosFatherUserGroupQueueApplyEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosFatherUserGroupQueueApplyInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosFatherUserGroupQueueApplyDirection"),
)
if mibBuilder.loadTexts:
    hwhqosFatherUserGroupQueueApplyEntry.setStatus("current")
_HwhqosFatherUserGroupQueueApplyInterfaceIndex_Type = InterfaceIndex
_HwhqosFatherUserGroupQueueApplyInterfaceIndex_Object = MibTableColumn
hwhqosFatherUserGroupQueueApplyInterfaceIndex = _HwhqosFatherUserGroupQueueApplyInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 53, 1, 1),
    _HwhqosFatherUserGroupQueueApplyInterfaceIndex_Type()
)
hwhqosFatherUserGroupQueueApplyInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosFatherUserGroupQueueApplyInterfaceIndex.setStatus("current")


class _HwhqosFatherUserGroupQueueApplyDirection_Type(Integer32):
    """Custom type hwhqosFatherUserGroupQueueApplyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("outbound", 2)
    )


_HwhqosFatherUserGroupQueueApplyDirection_Type.__name__ = "Integer32"
_HwhqosFatherUserGroupQueueApplyDirection_Object = MibTableColumn
hwhqosFatherUserGroupQueueApplyDirection = _HwhqosFatherUserGroupQueueApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 53, 1, 2),
    _HwhqosFatherUserGroupQueueApplyDirection_Type()
)
hwhqosFatherUserGroupQueueApplyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosFatherUserGroupQueueApplyDirection.setStatus("current")


class _HwhqosFatherUserGroupQueueApplyName_Type(OctetString):
    """Custom type hwhqosFatherUserGroupQueueApplyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosFatherUserGroupQueueApplyName_Type.__name__ = "OctetString"
_HwhqosFatherUserGroupQueueApplyName_Object = MibTableColumn
hwhqosFatherUserGroupQueueApplyName = _HwhqosFatherUserGroupQueueApplyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 53, 1, 3),
    _HwhqosFatherUserGroupQueueApplyName_Type()
)
hwhqosFatherUserGroupQueueApplyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFatherUserGroupQueueApplyName.setStatus("current")
_HwhqosFatherUserGroupQueueApplyRowStatus_Type = RowStatus
_HwhqosFatherUserGroupQueueApplyRowStatus_Object = MibTableColumn
hwhqosFatherUserGroupQueueApplyRowStatus = _HwhqosFatherUserGroupQueueApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 53, 1, 50),
    _HwhqosFatherUserGroupQueueApplyRowStatus_Type()
)
hwhqosFatherUserGroupQueueApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosFatherUserGroupQueueApplyRowStatus.setStatus("current")
_HwhqosUserGroupQueueApplyTable_Object = MibTable
hwhqosUserGroupQueueApplyTable = _HwhqosUserGroupQueueApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 54)
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueApplyTable.setStatus("current")
_HwhqosUserGroupQueueApplyEntry_Object = MibTableRow
hwhqosUserGroupQueueApplyEntry = _HwhqosUserGroupQueueApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 54, 1)
)
hwhqosUserGroupQueueApplyEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueApplyInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueApplyPeVid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueApplyCeVid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueApplyDirection"),
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueApplyEntry.setStatus("current")
_HwhqosUserGroupQueueApplyInterfaceIndex_Type = InterfaceIndex
_HwhqosUserGroupQueueApplyInterfaceIndex_Object = MibTableColumn
hwhqosUserGroupQueueApplyInterfaceIndex = _HwhqosUserGroupQueueApplyInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 54, 1, 1),
    _HwhqosUserGroupQueueApplyInterfaceIndex_Type()
)
hwhqosUserGroupQueueApplyInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueApplyInterfaceIndex.setStatus("current")


class _HwhqosUserGroupQueueApplyPeVid_Type(Integer32):
    """Custom type hwhqosUserGroupQueueApplyPeVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwhqosUserGroupQueueApplyPeVid_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueApplyPeVid_Object = MibTableColumn
hwhqosUserGroupQueueApplyPeVid = _HwhqosUserGroupQueueApplyPeVid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 54, 1, 2),
    _HwhqosUserGroupQueueApplyPeVid_Type()
)
hwhqosUserGroupQueueApplyPeVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueApplyPeVid.setStatus("current")


class _HwhqosUserGroupQueueApplyCeVid_Type(Integer32):
    """Custom type hwhqosUserGroupQueueApplyCeVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwhqosUserGroupQueueApplyCeVid_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueApplyCeVid_Object = MibTableColumn
hwhqosUserGroupQueueApplyCeVid = _HwhqosUserGroupQueueApplyCeVid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 54, 1, 3),
    _HwhqosUserGroupQueueApplyCeVid_Type()
)
hwhqosUserGroupQueueApplyCeVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueApplyCeVid.setStatus("current")


class _HwhqosUserGroupQueueApplyDirection_Type(Integer32):
    """Custom type hwhqosUserGroupQueueApplyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosUserGroupQueueApplyDirection_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueApplyDirection_Object = MibTableColumn
hwhqosUserGroupQueueApplyDirection = _HwhqosUserGroupQueueApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 54, 1, 4),
    _HwhqosUserGroupQueueApplyDirection_Type()
)
hwhqosUserGroupQueueApplyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueApplyDirection.setStatus("current")
_HwhqosUserGroupQueueApplyName_Type = OctetString
_HwhqosUserGroupQueueApplyName_Object = MibTableColumn
hwhqosUserGroupQueueApplyName = _HwhqosUserGroupQueueApplyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 54, 1, 5),
    _HwhqosUserGroupQueueApplyName_Type()
)
hwhqosUserGroupQueueApplyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueApplyName.setStatus("current")


class _HwhqosUserGroupQueueApplyEachvlan_Type(Integer32):
    """Custom type hwhqosUserGroupQueueApplyEachvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eachCevid", 3),
          ("eachPevid", 2),
          ("eachVlan", 1),
          ("none", 4))
    )


_HwhqosUserGroupQueueApplyEachvlan_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueApplyEachvlan_Object = MibTableColumn
hwhqosUserGroupQueueApplyEachvlan = _HwhqosUserGroupQueueApplyEachvlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 54, 1, 6),
    _HwhqosUserGroupQueueApplyEachvlan_Type()
)
hwhqosUserGroupQueueApplyEachvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueApplyEachvlan.setStatus("current")
_HwhqosUserGroupQueueApplyRowStatus_Type = RowStatus
_HwhqosUserGroupQueueApplyRowStatus_Object = MibTableColumn
hwhqosUserGroupQueueApplyRowStatus = _HwhqosUserGroupQueueApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 54, 1, 50),
    _HwhqosUserGroupQueueApplyRowStatus_Type()
)
hwhqosUserGroupQueueApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueApplyRowStatus.setStatus("current")
_HwhqosProfileApplyDomainTable_Object = MibTable
hwhqosProfileApplyDomainTable = _HwhqosProfileApplyDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 55)
)
if mibBuilder.loadTexts:
    hwhqosProfileApplyDomainTable.setStatus("current")
_HwhqosProfileApplyDomainEntry_Object = MibTableRow
hwhqosProfileApplyDomainEntry = _HwhqosProfileApplyDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 55, 1)
)
hwhqosProfileApplyDomainEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileApplyDomainName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileApplyDomainDirection"),
)
if mibBuilder.loadTexts:
    hwhqosProfileApplyDomainEntry.setStatus("current")
_HwhqosProfileApplyDomainName_Type = OctetString
_HwhqosProfileApplyDomainName_Object = MibTableColumn
hwhqosProfileApplyDomainName = _HwhqosProfileApplyDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 55, 1, 1),
    _HwhqosProfileApplyDomainName_Type()
)
hwhqosProfileApplyDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileApplyDomainName.setStatus("current")


class _HwhqosProfileApplyDomainDirection_Type(Integer32):
    """Custom type hwhqosProfileApplyDomainDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosProfileApplyDomainDirection_Type.__name__ = "Integer32"
_HwhqosProfileApplyDomainDirection_Object = MibTableColumn
hwhqosProfileApplyDomainDirection = _HwhqosProfileApplyDomainDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 55, 1, 2),
    _HwhqosProfileApplyDomainDirection_Type()
)
hwhqosProfileApplyDomainDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileApplyDomainDirection.setStatus("current")
_HwhqosProfileApplyDomainProfileName_Type = OctetString
_HwhqosProfileApplyDomainProfileName_Object = MibTableColumn
hwhqosProfileApplyDomainProfileName = _HwhqosProfileApplyDomainProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 55, 1, 3),
    _HwhqosProfileApplyDomainProfileName_Type()
)
hwhqosProfileApplyDomainProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileApplyDomainProfileName.setStatus("current")
_HwhqosProfileApplyDomainRowStatus_Type = RowStatus
_HwhqosProfileApplyDomainRowStatus_Object = MibTableColumn
hwhqosProfileApplyDomainRowStatus = _HwhqosProfileApplyDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 55, 1, 50),
    _HwhqosProfileApplyDomainRowStatus_Type()
)
hwhqosProfileApplyDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileApplyDomainRowStatus.setStatus("current")
_HwhqosProfileApplyUserVlanTable_Object = MibTable
hwhqosProfileApplyUserVlanTable = _HwhqosProfileApplyUserVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 56)
)
if mibBuilder.loadTexts:
    hwhqosProfileApplyUserVlanTable.setStatus("current")
_HwhqosProfileApplyUserVlanEntry_Object = MibTableRow
hwhqosProfileApplyUserVlanEntry = _HwhqosProfileApplyUserVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 56, 1)
)
hwhqosProfileApplyUserVlanEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileApplyUserVlanInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileApplyUserVlanPeVid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileApplyUserVlanCeVid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileApplyUserVlanDirection"),
)
if mibBuilder.loadTexts:
    hwhqosProfileApplyUserVlanEntry.setStatus("current")
_HwhqosProfileApplyUserVlanInterfaceIndex_Type = InterfaceIndex
_HwhqosProfileApplyUserVlanInterfaceIndex_Object = MibTableColumn
hwhqosProfileApplyUserVlanInterfaceIndex = _HwhqosProfileApplyUserVlanInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 56, 1, 1),
    _HwhqosProfileApplyUserVlanInterfaceIndex_Type()
)
hwhqosProfileApplyUserVlanInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileApplyUserVlanInterfaceIndex.setStatus("current")


class _HwhqosProfileApplyUserVlanPeVid_Type(Integer32):
    """Custom type hwhqosProfileApplyUserVlanPeVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwhqosProfileApplyUserVlanPeVid_Type.__name__ = "Integer32"
_HwhqosProfileApplyUserVlanPeVid_Object = MibTableColumn
hwhqosProfileApplyUserVlanPeVid = _HwhqosProfileApplyUserVlanPeVid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 56, 1, 2),
    _HwhqosProfileApplyUserVlanPeVid_Type()
)
hwhqosProfileApplyUserVlanPeVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileApplyUserVlanPeVid.setStatus("current")


class _HwhqosProfileApplyUserVlanCeVid_Type(Integer32):
    """Custom type hwhqosProfileApplyUserVlanCeVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwhqosProfileApplyUserVlanCeVid_Type.__name__ = "Integer32"
_HwhqosProfileApplyUserVlanCeVid_Object = MibTableColumn
hwhqosProfileApplyUserVlanCeVid = _HwhqosProfileApplyUserVlanCeVid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 56, 1, 3),
    _HwhqosProfileApplyUserVlanCeVid_Type()
)
hwhqosProfileApplyUserVlanCeVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileApplyUserVlanCeVid.setStatus("current")


class _HwhqosProfileApplyUserVlanDirection_Type(Integer32):
    """Custom type hwhqosProfileApplyUserVlanDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosProfileApplyUserVlanDirection_Type.__name__ = "Integer32"
_HwhqosProfileApplyUserVlanDirection_Object = MibTableColumn
hwhqosProfileApplyUserVlanDirection = _HwhqosProfileApplyUserVlanDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 56, 1, 4),
    _HwhqosProfileApplyUserVlanDirection_Type()
)
hwhqosProfileApplyUserVlanDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileApplyUserVlanDirection.setStatus("current")
_HwhqosProfileApplyUserVlanProfileName_Type = OctetString
_HwhqosProfileApplyUserVlanProfileName_Object = MibTableColumn
hwhqosProfileApplyUserVlanProfileName = _HwhqosProfileApplyUserVlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 56, 1, 5),
    _HwhqosProfileApplyUserVlanProfileName_Type()
)
hwhqosProfileApplyUserVlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileApplyUserVlanProfileName.setStatus("current")


class _HwhqosProfileApplyUserVlanEach_Type(Integer32):
    """Custom type hwhqosProfileApplyUserVlanEach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosProfileApplyUserVlanEach_Type.__name__ = "Integer32"
_HwhqosProfileApplyUserVlanEach_Object = MibTableColumn
hwhqosProfileApplyUserVlanEach = _HwhqosProfileApplyUserVlanEach_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 56, 1, 6),
    _HwhqosProfileApplyUserVlanEach_Type()
)
hwhqosProfileApplyUserVlanEach.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileApplyUserVlanEach.setStatus("current")
_HwhqosProfileApplyUserVlanRowStatus_Type = RowStatus
_HwhqosProfileApplyUserVlanRowStatus_Object = MibTableColumn
hwhqosProfileApplyUserVlanRowStatus = _HwhqosProfileApplyUserVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 56, 1, 50),
    _HwhqosProfileApplyUserVlanRowStatus_Type()
)
hwhqosProfileApplyUserVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileApplyUserVlanRowStatus.setStatus("current")
_HwhqosLinkAdjRemoteEnableTable_Object = MibTable
hwhqosLinkAdjRemoteEnableTable = _HwhqosLinkAdjRemoteEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 57)
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteEnableTable.setStatus("current")
_HwhqosLinkAdjRemoteEnableEntry_Object = MibTableRow
hwhqosLinkAdjRemoteEnableEntry = _HwhqosLinkAdjRemoteEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 57, 1)
)
hwhqosLinkAdjRemoteEnableEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteEnableType"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteEnableSlot"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteEnableDomainName"),
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteEnableEntry.setStatus("current")


class _HwhqosLinkAdjRemoteEnableType_Type(Integer32):
    """Custom type hwhqosLinkAdjRemoteEnableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domain", 2),
          ("system", 1))
    )


_HwhqosLinkAdjRemoteEnableType_Type.__name__ = "Integer32"
_HwhqosLinkAdjRemoteEnableType_Object = MibTableColumn
hwhqosLinkAdjRemoteEnableType = _HwhqosLinkAdjRemoteEnableType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 57, 1, 1),
    _HwhqosLinkAdjRemoteEnableType_Type()
)
hwhqosLinkAdjRemoteEnableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteEnableType.setStatus("current")
_HwhqosLinkAdjRemoteEnableSlot_Type = Integer32
_HwhqosLinkAdjRemoteEnableSlot_Object = MibTableColumn
hwhqosLinkAdjRemoteEnableSlot = _HwhqosLinkAdjRemoteEnableSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 57, 1, 2),
    _HwhqosLinkAdjRemoteEnableSlot_Type()
)
hwhqosLinkAdjRemoteEnableSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteEnableSlot.setStatus("current")


class _HwhqosLinkAdjRemoteEnableDomainName_Type(OctetString):
    """Custom type hwhqosLinkAdjRemoteEnableDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosLinkAdjRemoteEnableDomainName_Type.__name__ = "OctetString"
_HwhqosLinkAdjRemoteEnableDomainName_Object = MibTableColumn
hwhqosLinkAdjRemoteEnableDomainName = _HwhqosLinkAdjRemoteEnableDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 57, 1, 3),
    _HwhqosLinkAdjRemoteEnableDomainName_Type()
)
hwhqosLinkAdjRemoteEnableDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteEnableDomainName.setStatus("current")


class _HwhqosLinkAdjRemoteEnable_Type(Integer32):
    """Custom type hwhqosLinkAdjRemoteEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosLinkAdjRemoteEnable_Type.__name__ = "Integer32"
_HwhqosLinkAdjRemoteEnable_Object = MibTableColumn
hwhqosLinkAdjRemoteEnable = _HwhqosLinkAdjRemoteEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 57, 1, 4),
    _HwhqosLinkAdjRemoteEnable_Type()
)
hwhqosLinkAdjRemoteEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteEnable.setStatus("current")
_HwhqosLinkAdjRemoteEnableRowStatus_Type = RowStatus
_HwhqosLinkAdjRemoteEnableRowStatus_Object = MibTableColumn
hwhqosLinkAdjRemoteEnableRowStatus = _HwhqosLinkAdjRemoteEnableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 57, 1, 50),
    _HwhqosLinkAdjRemoteEnableRowStatus_Type()
)
hwhqosLinkAdjRemoteEnableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteEnableRowStatus.setStatus("current")
_HwhqosLinkAdjShapingModeTable_Object = MibTable
hwhqosLinkAdjShapingModeTable = _HwhqosLinkAdjShapingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 58)
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjShapingModeTable.setStatus("current")
_HwhqosLinkAdjShapingModeEntry_Object = MibTableRow
hwhqosLinkAdjShapingModeEntry = _HwhqosLinkAdjShapingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 58, 1)
)
hwhqosLinkAdjShapingModeEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosLinkAdjShapingModeType"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosLinkAdjShapingModeInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosLinkAdjShapingModeDomainName"),
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjShapingModeEntry.setStatus("current")


class _HwhqosLinkAdjShapingModeType_Type(Integer32):
    """Custom type hwhqosLinkAdjShapingModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domain", 2),
          ("interface", 1))
    )


_HwhqosLinkAdjShapingModeType_Type.__name__ = "Integer32"
_HwhqosLinkAdjShapingModeType_Object = MibTableColumn
hwhqosLinkAdjShapingModeType = _HwhqosLinkAdjShapingModeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 58, 1, 1),
    _HwhqosLinkAdjShapingModeType_Type()
)
hwhqosLinkAdjShapingModeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosLinkAdjShapingModeType.setStatus("current")
_HwhqosLinkAdjShapingModeInterfaceIndex_Type = Integer32
_HwhqosLinkAdjShapingModeInterfaceIndex_Object = MibTableColumn
hwhqosLinkAdjShapingModeInterfaceIndex = _HwhqosLinkAdjShapingModeInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 58, 1, 2),
    _HwhqosLinkAdjShapingModeInterfaceIndex_Type()
)
hwhqosLinkAdjShapingModeInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosLinkAdjShapingModeInterfaceIndex.setStatus("current")


class _HwhqosLinkAdjShapingModeDomainName_Type(OctetString):
    """Custom type hwhqosLinkAdjShapingModeDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosLinkAdjShapingModeDomainName_Type.__name__ = "OctetString"
_HwhqosLinkAdjShapingModeDomainName_Object = MibTableColumn
hwhqosLinkAdjShapingModeDomainName = _HwhqosLinkAdjShapingModeDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 58, 1, 3),
    _HwhqosLinkAdjShapingModeDomainName_Type()
)
hwhqosLinkAdjShapingModeDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosLinkAdjShapingModeDomainName.setStatus("current")


class _HwhqosLinkAdjShapingMode_Type(Integer32):
    """Custom type hwhqosLinkAdjShapingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cell", 2),
          ("frame", 1))
    )


_HwhqosLinkAdjShapingMode_Type.__name__ = "Integer32"
_HwhqosLinkAdjShapingMode_Object = MibTableColumn
hwhqosLinkAdjShapingMode = _HwhqosLinkAdjShapingMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 58, 1, 4),
    _HwhqosLinkAdjShapingMode_Type()
)
hwhqosLinkAdjShapingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosLinkAdjShapingMode.setStatus("current")
_HwhqosLinkAdjShapingModeRowStatus_Type = RowStatus
_HwhqosLinkAdjShapingModeRowStatus_Object = MibTableColumn
hwhqosLinkAdjShapingModeRowStatus = _HwhqosLinkAdjShapingModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 58, 1, 50),
    _HwhqosLinkAdjShapingModeRowStatus_Type()
)
hwhqosLinkAdjShapingModeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosLinkAdjShapingModeRowStatus.setStatus("current")
_HwhqosLinkAdjRemoteTable_Object = MibTable
hwhqosLinkAdjRemoteTable = _HwhqosLinkAdjRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 59)
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteTable.setStatus("current")
_HwhqosLinkAdjRemoteEntry_Object = MibTableRow
hwhqosLinkAdjRemoteEntry = _HwhqosLinkAdjRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 59, 1)
)
hwhqosLinkAdjRemoteEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteType"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteInterfaceIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteDomainName"),
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteEntry.setStatus("current")


class _HwhqosLinkAdjRemoteType_Type(Integer32):
    """Custom type hwhqosLinkAdjRemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domain", 2),
          ("interface", 1))
    )


_HwhqosLinkAdjRemoteType_Type.__name__ = "Integer32"
_HwhqosLinkAdjRemoteType_Object = MibTableColumn
hwhqosLinkAdjRemoteType = _HwhqosLinkAdjRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 59, 1, 1),
    _HwhqosLinkAdjRemoteType_Type()
)
hwhqosLinkAdjRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteType.setStatus("current")
_HwhqosLinkAdjRemoteInterfaceIndex_Type = Integer32
_HwhqosLinkAdjRemoteInterfaceIndex_Object = MibTableColumn
hwhqosLinkAdjRemoteInterfaceIndex = _HwhqosLinkAdjRemoteInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 59, 1, 2),
    _HwhqosLinkAdjRemoteInterfaceIndex_Type()
)
hwhqosLinkAdjRemoteInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteInterfaceIndex.setStatus("current")


class _HwhqosLinkAdjRemoteDomainName_Type(OctetString):
    """Custom type hwhqosLinkAdjRemoteDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosLinkAdjRemoteDomainName_Type.__name__ = "OctetString"
_HwhqosLinkAdjRemoteDomainName_Object = MibTableColumn
hwhqosLinkAdjRemoteDomainName = _HwhqosLinkAdjRemoteDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 59, 1, 3),
    _HwhqosLinkAdjRemoteDomainName_Type()
)
hwhqosLinkAdjRemoteDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteDomainName.setStatus("current")
_HwhqosLinkAdjRemoteValue_Type = Integer32
_HwhqosLinkAdjRemoteValue_Object = MibTableColumn
hwhqosLinkAdjRemoteValue = _HwhqosLinkAdjRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 59, 1, 4),
    _HwhqosLinkAdjRemoteValue_Type()
)
hwhqosLinkAdjRemoteValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteValue.setStatus("current")
_HwhqosLinkAdjRemoteRowStatus_Type = RowStatus
_HwhqosLinkAdjRemoteRowStatus_Object = MibTableColumn
hwhqosLinkAdjRemoteRowStatus = _HwhqosLinkAdjRemoteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 59, 1, 50),
    _HwhqosLinkAdjRemoteRowStatus_Type()
)
hwhqosLinkAdjRemoteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteRowStatus.setStatus("current")
_HwhqosLinkAdjLocalTable_Object = MibTable
hwhqosLinkAdjLocalTable = _HwhqosLinkAdjLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 60)
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjLocalTable.setStatus("current")
_HwhqosLinkAdjLocalEntry_Object = MibTableRow
hwhqosLinkAdjLocalEntry = _HwhqosLinkAdjLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 60, 1)
)
hwhqosLinkAdjLocalEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosLinkAdjLocalSlotNumber"),
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjLocalEntry.setStatus("current")


class _HwhqosLinkAdjLocalSlotNumber_Type(Integer32):
    """Custom type hwhqosLinkAdjLocalSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwhqosLinkAdjLocalSlotNumber_Type.__name__ = "Integer32"
_HwhqosLinkAdjLocalSlotNumber_Object = MibTableColumn
hwhqosLinkAdjLocalSlotNumber = _HwhqosLinkAdjLocalSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 60, 1, 1),
    _HwhqosLinkAdjLocalSlotNumber_Type()
)
hwhqosLinkAdjLocalSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosLinkAdjLocalSlotNumber.setStatus("current")
_HwhqosLinkAdjLocalValue_Type = Integer32
_HwhqosLinkAdjLocalValue_Object = MibTableColumn
hwhqosLinkAdjLocalValue = _HwhqosLinkAdjLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 60, 1, 2),
    _HwhqosLinkAdjLocalValue_Type()
)
hwhqosLinkAdjLocalValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosLinkAdjLocalValue.setStatus("current")
_HwhqosLinkAdjLocalRowStatus_Type = RowStatus
_HwhqosLinkAdjLocalRowStatus_Object = MibTableColumn
hwhqosLinkAdjLocalRowStatus = _HwhqosLinkAdjLocalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 60, 1, 50),
    _HwhqosLinkAdjLocalRowStatus_Type()
)
hwhqosLinkAdjLocalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosLinkAdjLocalRowStatus.setStatus("current")
_HwhqosLinkAdjExcludeTable_Object = MibTable
hwhqosLinkAdjExcludeTable = _HwhqosLinkAdjExcludeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 61)
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjExcludeTable.setStatus("current")
_HwhqosLinkAdjExcludeEntry_Object = MibTableRow
hwhqosLinkAdjExcludeEntry = _HwhqosLinkAdjExcludeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 61, 1)
)
hwhqosLinkAdjExcludeEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosLinkAdjExcludeSlotNumber"),
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjExcludeEntry.setStatus("current")


class _HwhqosLinkAdjExcludeSlotNumber_Type(Integer32):
    """Custom type hwhqosLinkAdjExcludeSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwhqosLinkAdjExcludeSlotNumber_Type.__name__ = "Integer32"
_HwhqosLinkAdjExcludeSlotNumber_Object = MibTableColumn
hwhqosLinkAdjExcludeSlotNumber = _HwhqosLinkAdjExcludeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 61, 1, 1),
    _HwhqosLinkAdjExcludeSlotNumber_Type()
)
hwhqosLinkAdjExcludeSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosLinkAdjExcludeSlotNumber.setStatus("current")


class _HwhqosLinkAdjExcludeEnable_Type(Integer32):
    """Custom type hwhqosLinkAdjExcludeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwhqosLinkAdjExcludeEnable_Type.__name__ = "Integer32"
_HwhqosLinkAdjExcludeEnable_Object = MibTableColumn
hwhqosLinkAdjExcludeEnable = _HwhqosLinkAdjExcludeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 61, 1, 2),
    _HwhqosLinkAdjExcludeEnable_Type()
)
hwhqosLinkAdjExcludeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosLinkAdjExcludeEnable.setStatus("current")
_HwhqosLinkAdjExcludeRowStatus_Type = RowStatus
_HwhqosLinkAdjExcludeRowStatus_Object = MibTableColumn
hwhqosLinkAdjExcludeRowStatus = _HwhqosLinkAdjExcludeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 61, 1, 50),
    _HwhqosLinkAdjExcludeRowStatus_Type()
)
hwhqosLinkAdjExcludeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosLinkAdjExcludeRowStatus.setStatus("current")
_HwhqosProfileInfoTable_Object = MibTable
hwhqosProfileInfoTable = _HwhqosProfileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 62)
)
if mibBuilder.loadTexts:
    hwhqosProfileInfoTable.setStatus("current")
_HwhqosProfileInfoEntry_Object = MibTableRow
hwhqosProfileInfoEntry = _HwhqosProfileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 62, 1)
)
hwhqosProfileInfoEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileInfoName"),
)
if mibBuilder.loadTexts:
    hwhqosProfileInfoEntry.setStatus("current")


class _HwhqosProfileInfoName_Type(OctetString):
    """Custom type hwhqosProfileInfoName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwhqosProfileInfoName_Type.__name__ = "OctetString"
_HwhqosProfileInfoName_Object = MibTableColumn
hwhqosProfileInfoName = _HwhqosProfileInfoName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 62, 1, 1),
    _HwhqosProfileInfoName_Type()
)
hwhqosProfileInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileInfoName.setStatus("current")


class _HwhqosProfileInfoDescription_Type(OctetString):
    """Custom type hwhqosProfileInfoDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_HwhqosProfileInfoDescription_Type.__name__ = "OctetString"
_HwhqosProfileInfoDescription_Object = MibTableColumn
hwhqosProfileInfoDescription = _HwhqosProfileInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 62, 1, 2),
    _HwhqosProfileInfoDescription_Type()
)
hwhqosProfileInfoDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileInfoDescription.setStatus("current")
_HwhqosProfileInfoRowStatus_Type = RowStatus
_HwhqosProfileInfoRowStatus_Object = MibTableColumn
hwhqosProfileInfoRowStatus = _HwhqosProfileInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 62, 1, 50),
    _HwhqosProfileInfoRowStatus_Type()
)
hwhqosProfileInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileInfoRowStatus.setStatus("current")
_HwhqosUserGroupQueueTemplateTable_Object = MibTable
hwhqosUserGroupQueueTemplateTable = _HwhqosUserGroupQueueTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 63)
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueTemplateTable.setStatus("current")
_HwhqosUserGroupQueueTemplateEntry_Object = MibTableRow
hwhqosUserGroupQueueTemplateEntry = _HwhqosUserGroupQueueTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 63, 1)
)
hwhqosUserGroupQueueTemplateEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueTemplateName"),
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueTemplateEntry.setStatus("current")


class _HwhqosUserGroupQueueTemplateName_Type(OctetString):
    """Custom type hwhqosUserGroupQueueTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosUserGroupQueueTemplateName_Type.__name__ = "OctetString"
_HwhqosUserGroupQueueTemplateName_Object = MibTableColumn
hwhqosUserGroupQueueTemplateName = _HwhqosUserGroupQueueTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 63, 1, 1),
    _HwhqosUserGroupQueueTemplateName_Type()
)
hwhqosUserGroupQueueTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueTemplateName.setStatus("current")


class _HwhqosUserGroupQueueTemplateModeTemplate_Type(Integer32):
    """Custom type hwhqosUserGroupQueueTemplateModeTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwhqosUserGroupQueueTemplateModeTemplate_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueTemplateModeTemplate_Object = MibTableColumn
hwhqosUserGroupQueueTemplateModeTemplate = _HwhqosUserGroupQueueTemplateModeTemplate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 63, 1, 2),
    _HwhqosUserGroupQueueTemplateModeTemplate_Type()
)
hwhqosUserGroupQueueTemplateModeTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueTemplateModeTemplate.setStatus("current")
_HwhqosUserGroupQueueTemplateRowStatus_Type = RowStatus
_HwhqosUserGroupQueueTemplateRowStatus_Object = MibTableColumn
hwhqosUserGroupQueueTemplateRowStatus = _HwhqosUserGroupQueueTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 63, 1, 50),
    _HwhqosUserGroupQueueTemplateRowStatus_Type()
)
hwhqosUserGroupQueueTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueTemplateRowStatus.setStatus("current")
_HwhqosProfileWeightTable_Object = MibTable
hwhqosProfileWeightTable = _HwhqosProfileWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 64)
)
if mibBuilder.loadTexts:
    hwhqosProfileWeightTable.setStatus("current")
_HwhqosProfileWeightEntry_Object = MibTableRow
hwhqosProfileWeightEntry = _HwhqosProfileWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 64, 1)
)
hwhqosProfileWeightEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileName"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosProfileWeightDirection"),
)
if mibBuilder.loadTexts:
    hwhqosProfileWeightEntry.setStatus("current")


class _HwhqosProfileWeightDirection_Type(Integer32):
    """Custom type hwhqosProfileWeightDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("inout", 3),
          ("outbound", 2))
    )


_HwhqosProfileWeightDirection_Type.__name__ = "Integer32"
_HwhqosProfileWeightDirection_Object = MibTableColumn
hwhqosProfileWeightDirection = _HwhqosProfileWeightDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 64, 1, 1),
    _HwhqosProfileWeightDirection_Type()
)
hwhqosProfileWeightDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosProfileWeightDirection.setStatus("current")


class _HwhqosProfileWeightValue_Type(Integer32):
    """Custom type hwhqosProfileWeightValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_HwhqosProfileWeightValue_Type.__name__ = "Integer32"
_HwhqosProfileWeightValue_Object = MibTableColumn
hwhqosProfileWeightValue = _HwhqosProfileWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 64, 1, 2),
    _HwhqosProfileWeightValue_Type()
)
hwhqosProfileWeightValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileWeightValue.setStatus("current")
_HwhqosProfileWeightRowStatus_Type = RowStatus
_HwhqosProfileWeightRowStatus_Object = MibTableColumn
hwhqosProfileWeightRowStatus = _HwhqosProfileWeightRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 64, 1, 50),
    _HwhqosProfileWeightRowStatus_Type()
)
hwhqosProfileWeightRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosProfileWeightRowStatus.setStatus("current")
_HwhqosUserQueueApplyAlarmTable_Object = MibTable
hwhqosUserQueueApplyAlarmTable = _HwhqosUserQueueApplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 65)
)
if mibBuilder.loadTexts:
    hwhqosUserQueueApplyAlarmTable.setStatus("current")
_HwhqosUserQueueApplyAlarmEntry_Object = MibTableRow
hwhqosUserQueueApplyAlarmEntry = _HwhqosUserQueueApplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 65, 1)
)
hwhqosUserQueueApplyAlarmEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueApplyAlarmIfNetName"),
)
if mibBuilder.loadTexts:
    hwhqosUserQueueApplyAlarmEntry.setStatus("current")


class _HwhqosUserQueueApplyAlarmIfNetName_Type(OctetString):
    """Custom type hwhqosUserQueueApplyAlarmIfNetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 511),
    )


_HwhqosUserQueueApplyAlarmIfNetName_Type.__name__ = "OctetString"
_HwhqosUserQueueApplyAlarmIfNetName_Object = MibTableColumn
hwhqosUserQueueApplyAlarmIfNetName = _HwhqosUserQueueApplyAlarmIfNetName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 65, 1, 1),
    _HwhqosUserQueueApplyAlarmIfNetName_Type()
)
hwhqosUserQueueApplyAlarmIfNetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserQueueApplyAlarmIfNetName.setStatus("current")
_HwhqosPortQueueStatDiscardAlarmTrapTable_Object = MibTable
hwhqosPortQueueStatDiscardAlarmTrapTable = _HwhqosPortQueueStatDiscardAlarmTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 66)
)
if mibBuilder.loadTexts:
    hwhqosPortQueueStatDiscardAlarmTrapTable.setStatus("current")
_HwhqosPortQueueStatDiscardAlarmTrapEntry_Object = MibTableRow
hwhqosPortQueueStatDiscardAlarmTrapEntry = _HwhqosPortQueueStatDiscardAlarmTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 66, 1)
)
hwhqosPortQueueStatDiscardAlarmTrapEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosPortQueueInterfaceTrap"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosPortQueueCosValueTrap"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosPortQueueDiscardTypeTrap"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosPortQueueDiscardValueTrap"),
)
if mibBuilder.loadTexts:
    hwhqosPortQueueStatDiscardAlarmTrapEntry.setStatus("current")


class _HwhqosPortQueueInterfaceTrap_Type(OctetString):
    """Custom type hwhqosPortQueueInterfaceTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 511),
    )


_HwhqosPortQueueInterfaceTrap_Type.__name__ = "OctetString"
_HwhqosPortQueueInterfaceTrap_Object = MibTableColumn
hwhqosPortQueueInterfaceTrap = _HwhqosPortQueueInterfaceTrap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 66, 1, 1),
    _HwhqosPortQueueInterfaceTrap_Type()
)
hwhqosPortQueueInterfaceTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosPortQueueInterfaceTrap.setStatus("current")


class _HwhqosPortQueueCosValueTrap_Type(Integer32):
    """Custom type hwhqosPortQueueCosValueTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("portqueueAF1", 2),
          ("portqueueAF2", 3),
          ("portqueueAF3", 4),
          ("portqueueAF4", 5),
          ("portqueueBE", 1),
          ("portqueueCS6", 7),
          ("portqueueCS7", 8),
          ("portqueueEF", 6))
    )


_HwhqosPortQueueCosValueTrap_Type.__name__ = "Integer32"
_HwhqosPortQueueCosValueTrap_Object = MibTableColumn
hwhqosPortQueueCosValueTrap = _HwhqosPortQueueCosValueTrap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 66, 1, 2),
    _HwhqosPortQueueCosValueTrap_Type()
)
hwhqosPortQueueCosValueTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosPortQueueCosValueTrap.setStatus("current")


class _HwhqosPortQueueDiscardTypeTrap_Type(Integer32):
    """Custom type hwhqosPortQueueDiscardTypeTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discardbyte", 2),
          ("discardpacket", 1),
          ("discardpacketratio", 3))
    )


_HwhqosPortQueueDiscardTypeTrap_Type.__name__ = "Integer32"
_HwhqosPortQueueDiscardTypeTrap_Object = MibTableColumn
hwhqosPortQueueDiscardTypeTrap = _HwhqosPortQueueDiscardTypeTrap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 66, 1, 3),
    _HwhqosPortQueueDiscardTypeTrap_Type()
)
hwhqosPortQueueDiscardTypeTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosPortQueueDiscardTypeTrap.setStatus("current")


class _HwhqosPortQueueDiscardValueTrap_Type(OctetString):
    """Custom type hwhqosPortQueueDiscardValueTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 511),
    )


_HwhqosPortQueueDiscardValueTrap_Type.__name__ = "OctetString"
_HwhqosPortQueueDiscardValueTrap_Object = MibTableColumn
hwhqosPortQueueDiscardValueTrap = _HwhqosPortQueueDiscardValueTrap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 66, 1, 4),
    _HwhqosPortQueueDiscardValueTrap_Type()
)
hwhqosPortQueueDiscardValueTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosPortQueueDiscardValueTrap.setStatus("current")
_HwhqosPortQueueStatDiscardAlarmCancelTable_Object = MibTable
hwhqosPortQueueStatDiscardAlarmCancelTable = _HwhqosPortQueueStatDiscardAlarmCancelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 67)
)
if mibBuilder.loadTexts:
    hwhqosPortQueueStatDiscardAlarmCancelTable.setStatus("current")
_HwhqosPortQueueStatDiscardAlarmCancelEntry_Object = MibTableRow
hwhqosPortQueueStatDiscardAlarmCancelEntry = _HwhqosPortQueueStatDiscardAlarmCancelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 67, 1)
)
hwhqosPortQueueStatDiscardAlarmCancelEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosPortQueueInterfaceCancel"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosPortQueueCosValueCancel"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosPortQueueDiscardTypeCancel"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosPortQueueDiscardValueCancel"),
)
if mibBuilder.loadTexts:
    hwhqosPortQueueStatDiscardAlarmCancelEntry.setStatus("current")


class _HwhqosPortQueueInterfaceCancel_Type(OctetString):
    """Custom type hwhqosPortQueueInterfaceCancel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 511),
    )


_HwhqosPortQueueInterfaceCancel_Type.__name__ = "OctetString"
_HwhqosPortQueueInterfaceCancel_Object = MibTableColumn
hwhqosPortQueueInterfaceCancel = _HwhqosPortQueueInterfaceCancel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 67, 1, 1),
    _HwhqosPortQueueInterfaceCancel_Type()
)
hwhqosPortQueueInterfaceCancel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosPortQueueInterfaceCancel.setStatus("current")


class _HwhqosPortQueueCosValueCancel_Type(Integer32):
    """Custom type hwhqosPortQueueCosValueCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("portqueueAF1", 2),
          ("portqueueAF2", 3),
          ("portqueueAF3", 4),
          ("portqueueAF4", 5),
          ("portqueueBE", 1),
          ("portqueueCS6", 7),
          ("portqueueCS7", 8),
          ("portqueueEF", 6))
    )


_HwhqosPortQueueCosValueCancel_Type.__name__ = "Integer32"
_HwhqosPortQueueCosValueCancel_Object = MibTableColumn
hwhqosPortQueueCosValueCancel = _HwhqosPortQueueCosValueCancel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 67, 1, 2),
    _HwhqosPortQueueCosValueCancel_Type()
)
hwhqosPortQueueCosValueCancel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosPortQueueCosValueCancel.setStatus("current")


class _HwhqosPortQueueDiscardTypeCancel_Type(Integer32):
    """Custom type hwhqosPortQueueDiscardTypeCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discardbyte", 2),
          ("discardpacket", 1),
          ("discardpacketratio", 3))
    )


_HwhqosPortQueueDiscardTypeCancel_Type.__name__ = "Integer32"
_HwhqosPortQueueDiscardTypeCancel_Object = MibTableColumn
hwhqosPortQueueDiscardTypeCancel = _HwhqosPortQueueDiscardTypeCancel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 67, 1, 3),
    _HwhqosPortQueueDiscardTypeCancel_Type()
)
hwhqosPortQueueDiscardTypeCancel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosPortQueueDiscardTypeCancel.setStatus("current")


class _HwhqosPortQueueDiscardValueCancel_Type(OctetString):
    """Custom type hwhqosPortQueueDiscardValueCancel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 511),
    )


_HwhqosPortQueueDiscardValueCancel_Type.__name__ = "OctetString"
_HwhqosPortQueueDiscardValueCancel_Object = MibTableColumn
hwhqosPortQueueDiscardValueCancel = _HwhqosPortQueueDiscardValueCancel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 67, 1, 4),
    _HwhqosPortQueueDiscardValueCancel_Type()
)
hwhqosPortQueueDiscardValueCancel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosPortQueueDiscardValueCancel.setStatus("current")
_HwhqosIfUserQueueTable_Object = MibTable
hwhqosIfUserQueueTable = _HwhqosIfUserQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 68)
)
if mibBuilder.loadTexts:
    hwhqosIfUserQueueTable.setStatus("current")
_HwhqosIfUserQueueEntry_Object = MibTableRow
hwhqosIfUserQueueEntry = _HwhqosIfUserQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 68, 1)
)
hwhqosIfUserQueueEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfUserQueueIfIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfUserQueueAclType"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfUserQueueAclID1"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfUserQueueAclID2"),
)
if mibBuilder.loadTexts:
    hwhqosIfUserQueueEntry.setStatus("current")
_HwhqosIfUserQueueIfIndex_Type = Integer32
_HwhqosIfUserQueueIfIndex_Object = MibTableColumn
hwhqosIfUserQueueIfIndex = _HwhqosIfUserQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 68, 1, 1),
    _HwhqosIfUserQueueIfIndex_Type()
)
hwhqosIfUserQueueIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueIfIndex.setStatus("current")


class _HwhqosIfUserQueueAclType_Type(Integer32):
    """Custom type hwhqosIfUserQueueAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_HwhqosIfUserQueueAclType_Type.__name__ = "Integer32"
_HwhqosIfUserQueueAclType_Object = MibTableColumn
hwhqosIfUserQueueAclType = _HwhqosIfUserQueueAclType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 68, 1, 2),
    _HwhqosIfUserQueueAclType_Type()
)
hwhqosIfUserQueueAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueAclType.setStatus("current")
_HwhqosIfUserQueueAclID1_Type = Integer32
_HwhqosIfUserQueueAclID1_Object = MibTableColumn
hwhqosIfUserQueueAclID1 = _HwhqosIfUserQueueAclID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 68, 1, 3),
    _HwhqosIfUserQueueAclID1_Type()
)
hwhqosIfUserQueueAclID1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueAclID1.setStatus("current")
_HwhqosIfUserQueueAclID2_Type = Integer32
_HwhqosIfUserQueueAclID2_Object = MibTableColumn
hwhqosIfUserQueueAclID2 = _HwhqosIfUserQueueAclID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 68, 1, 4),
    _HwhqosIfUserQueueAclID2_Type()
)
hwhqosIfUserQueueAclID2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueAclID2.setStatus("current")


class _HwhqosIfUserQueuePir_Type(Integer32):
    """Custom type hwhqosIfUserQueuePir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 10000000),
    )


_HwhqosIfUserQueuePir_Type.__name__ = "Integer32"
_HwhqosIfUserQueuePir_Object = MibTableColumn
hwhqosIfUserQueuePir = _HwhqosIfUserQueuePir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 68, 1, 6),
    _HwhqosIfUserQueuePir_Type()
)
hwhqosIfUserQueuePir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosIfUserQueuePir.setStatus("current")


class _HwhqosIfUserQueueFlowQueueProfileName_Type(OctetString):
    """Custom type hwhqosIfUserQueueFlowQueueProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosIfUserQueueFlowQueueProfileName_Type.__name__ = "OctetString"
_HwhqosIfUserQueueFlowQueueProfileName_Object = MibTableColumn
hwhqosIfUserQueueFlowQueueProfileName = _HwhqosIfUserQueueFlowQueueProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 68, 1, 7),
    _HwhqosIfUserQueueFlowQueueProfileName_Type()
)
hwhqosIfUserQueueFlowQueueProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueFlowQueueProfileName.setStatus("current")


class _HwhqosIfUserQueueFlowMappingProfileName_Type(OctetString):
    """Custom type hwhqosIfUserQueueFlowMappingProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwhqosIfUserQueueFlowMappingProfileName_Type.__name__ = "OctetString"
_HwhqosIfUserQueueFlowMappingProfileName_Object = MibTableColumn
hwhqosIfUserQueueFlowMappingProfileName = _HwhqosIfUserQueueFlowMappingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 68, 1, 8),
    _HwhqosIfUserQueueFlowMappingProfileName_Type()
)
hwhqosIfUserQueueFlowMappingProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueFlowMappingProfileName.setStatus("current")
_HwhqosIfUserQueueRowStatus_Type = RowStatus
_HwhqosIfUserQueueRowStatus_Object = MibTableColumn
hwhqosIfUserQueueRowStatus = _HwhqosIfUserQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 68, 1, 9),
    _HwhqosIfUserQueueRowStatus_Type()
)
hwhqosIfUserQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueRowStatus.setStatus("current")
_HwhqosIfUserQueueStatisticsTable_Object = MibTable
hwhqosIfUserQueueStatisticsTable = _HwhqosIfUserQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69)
)
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsTable.setStatus("current")
_HwhqosIfUserQueueStatisticsEntry_Object = MibTableRow
hwhqosIfUserQueueStatisticsEntry = _HwhqosIfUserQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69, 1)
)
hwhqosIfUserQueueStatisticsEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfUserQueueStatisticsIfIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfUserQueueStatisticsAclType"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfUserQueueStatisticsAclID1"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfUserQueueStatisticsAclID2"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosIfUserQueueStatisticsQueueIndex"),
)
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsEntry.setStatus("current")
_HwhqosIfUserQueueStatisticsIfIndex_Type = Integer32
_HwhqosIfUserQueueStatisticsIfIndex_Object = MibTableColumn
hwhqosIfUserQueueStatisticsIfIndex = _HwhqosIfUserQueueStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69, 1, 1),
    _HwhqosIfUserQueueStatisticsIfIndex_Type()
)
hwhqosIfUserQueueStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsIfIndex.setStatus("current")


class _HwhqosIfUserQueueStatisticsAclType_Type(Integer32):
    """Custom type hwhqosIfUserQueueStatisticsAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_HwhqosIfUserQueueStatisticsAclType_Type.__name__ = "Integer32"
_HwhqosIfUserQueueStatisticsAclType_Object = MibTableColumn
hwhqosIfUserQueueStatisticsAclType = _HwhqosIfUserQueueStatisticsAclType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69, 1, 2),
    _HwhqosIfUserQueueStatisticsAclType_Type()
)
hwhqosIfUserQueueStatisticsAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsAclType.setStatus("current")
_HwhqosIfUserQueueStatisticsAclID1_Type = Integer32
_HwhqosIfUserQueueStatisticsAclID1_Object = MibTableColumn
hwhqosIfUserQueueStatisticsAclID1 = _HwhqosIfUserQueueStatisticsAclID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69, 1, 3),
    _HwhqosIfUserQueueStatisticsAclID1_Type()
)
hwhqosIfUserQueueStatisticsAclID1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsAclID1.setStatus("current")
_HwhqosIfUserQueueStatisticsAclID2_Type = Integer32
_HwhqosIfUserQueueStatisticsAclID2_Object = MibTableColumn
hwhqosIfUserQueueStatisticsAclID2 = _HwhqosIfUserQueueStatisticsAclID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69, 1, 4),
    _HwhqosIfUserQueueStatisticsAclID2_Type()
)
hwhqosIfUserQueueStatisticsAclID2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsAclID2.setStatus("current")


class _HwhqosIfUserQueueStatisticsQueueIndex_Type(Integer32):
    """Custom type hwhqosIfUserQueueStatisticsQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("total", 255))
    )


_HwhqosIfUserQueueStatisticsQueueIndex_Type.__name__ = "Integer32"
_HwhqosIfUserQueueStatisticsQueueIndex_Object = MibTableColumn
hwhqosIfUserQueueStatisticsQueueIndex = _HwhqosIfUserQueueStatisticsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69, 1, 5),
    _HwhqosIfUserQueueStatisticsQueueIndex_Type()
)
hwhqosIfUserQueueStatisticsQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsQueueIndex.setStatus("current")
_HwhqosIfUserQueueStatisticsQueuePassPackets_Type = Counter64
_HwhqosIfUserQueueStatisticsQueuePassPackets_Object = MibTableColumn
hwhqosIfUserQueueStatisticsQueuePassPackets = _HwhqosIfUserQueueStatisticsQueuePassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69, 1, 6),
    _HwhqosIfUserQueueStatisticsQueuePassPackets_Type()
)
hwhqosIfUserQueueStatisticsQueuePassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsQueuePassPackets.setStatus("current")
_HwhqosIfUserQueueStatisticsQueuePassBytes_Type = Counter64
_HwhqosIfUserQueueStatisticsQueuePassBytes_Object = MibTableColumn
hwhqosIfUserQueueStatisticsQueuePassBytes = _HwhqosIfUserQueueStatisticsQueuePassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69, 1, 7),
    _HwhqosIfUserQueueStatisticsQueuePassBytes_Type()
)
hwhqosIfUserQueueStatisticsQueuePassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsQueuePassBytes.setStatus("current")
_HwhqosIfUserQueueStatisticsQueueDropPackets_Type = Counter64
_HwhqosIfUserQueueStatisticsQueueDropPackets_Object = MibTableColumn
hwhqosIfUserQueueStatisticsQueueDropPackets = _HwhqosIfUserQueueStatisticsQueueDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69, 1, 8),
    _HwhqosIfUserQueueStatisticsQueueDropPackets_Type()
)
hwhqosIfUserQueueStatisticsQueueDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsQueueDropPackets.setStatus("current")
_HwhqosIfUserQueueStatisticsQueueDropBytes_Type = Counter64
_HwhqosIfUserQueueStatisticsQueueDropBytes_Object = MibTableColumn
hwhqosIfUserQueueStatisticsQueueDropBytes = _HwhqosIfUserQueueStatisticsQueueDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69, 1, 9),
    _HwhqosIfUserQueueStatisticsQueueDropBytes_Type()
)
hwhqosIfUserQueueStatisticsQueueDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsQueueDropBytes.setStatus("current")


class _HwhqosIfUserQueueStatisticsReset_Type(Integer32):
    """Custom type hwhqosIfUserQueueStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_HwhqosIfUserQueueStatisticsReset_Type.__name__ = "Integer32"
_HwhqosIfUserQueueStatisticsReset_Object = MibTableColumn
hwhqosIfUserQueueStatisticsReset = _HwhqosIfUserQueueStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 69, 1, 10),
    _HwhqosIfUserQueueStatisticsReset_Type()
)
hwhqosIfUserQueueStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwhqosIfUserQueueStatisticsReset.setStatus("current")
_HwhqosUserQueueShapeAllTrafficTable_Object = MibTable
hwhqosUserQueueShapeAllTrafficTable = _HwhqosUserQueueShapeAllTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 70)
)
if mibBuilder.loadTexts:
    hwhqosUserQueueShapeAllTrafficTable.setStatus("current")
_HwhqosUserQueueShapeAllTrafficEntry_Object = MibTableRow
hwhqosUserQueueShapeAllTrafficEntry = _HwhqosUserQueueShapeAllTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 70, 1)
)
hwhqosUserQueueShapeAllTrafficEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserQueueShapeAllTrafficInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwhqosUserQueueShapeAllTrafficEntry.setStatus("current")
_HwhqosUserQueueShapeAllTrafficInterfaceIndex_Type = Integer32
_HwhqosUserQueueShapeAllTrafficInterfaceIndex_Object = MibTableColumn
hwhqosUserQueueShapeAllTrafficInterfaceIndex = _HwhqosUserQueueShapeAllTrafficInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 70, 1, 1),
    _HwhqosUserQueueShapeAllTrafficInterfaceIndex_Type()
)
hwhqosUserQueueShapeAllTrafficInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwhqosUserQueueShapeAllTrafficInterfaceIndex.setStatus("current")
_HwhqosUserQueueShapeAllTrafficRowStatus_Type = RowStatus
_HwhqosUserQueueShapeAllTrafficRowStatus_Object = MibTableColumn
hwhqosUserQueueShapeAllTrafficRowStatus = _HwhqosUserQueueShapeAllTrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 70, 1, 2),
    _HwhqosUserQueueShapeAllTrafficRowStatus_Type()
)
hwhqosUserQueueShapeAllTrafficRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserQueueShapeAllTrafficRowStatus.setStatus("current")
_HwhqosUserGroupQueueInterfaceStatisticsTable_Object = MibTable
hwhqosUserGroupQueueInterfaceStatisticsTable = _HwhqosUserGroupQueueInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71)
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsTable.setStatus("current")
_HwhqosUserGroupQueueInterfaceStatisticsEntry_Object = MibTableRow
hwhqosUserGroupQueueInterfaceStatisticsEntry = _HwhqosUserGroupQueueInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1)
)
hwhqosUserGroupQueueInterfaceStatisticsEntry.setIndexNames(
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsIfIndex"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsDirection"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsPevid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsCevid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsVlanid"),
    (0, "HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsQueueIndex"),
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsEntry.setStatus("current")


class _HwhqosUserGroupQueueInterfaceStatisticsIfIndex_Type(Integer32):
    """Custom type hwhqosUserGroupQueueInterfaceStatisticsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwhqosUserGroupQueueInterfaceStatisticsIfIndex_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueInterfaceStatisticsIfIndex_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsIfIndex = _HwhqosUserGroupQueueInterfaceStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 1),
    _HwhqosUserGroupQueueInterfaceStatisticsIfIndex_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsIfIndex.setStatus("current")


class _HwhqosUserGroupQueueInterfaceStatisticsDirection_Type(Integer32):
    """Custom type hwhqosUserGroupQueueInterfaceStatisticsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosUserGroupQueueInterfaceStatisticsDirection_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueInterfaceStatisticsDirection_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsDirection = _HwhqosUserGroupQueueInterfaceStatisticsDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 2),
    _HwhqosUserGroupQueueInterfaceStatisticsDirection_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsDirection.setStatus("current")


class _HwhqosUserGroupQueueInterfaceStatisticsPevid_Type(Integer32):
    """Custom type hwhqosUserGroupQueueInterfaceStatisticsPevid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwhqosUserGroupQueueInterfaceStatisticsPevid_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueInterfaceStatisticsPevid_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsPevid = _HwhqosUserGroupQueueInterfaceStatisticsPevid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 3),
    _HwhqosUserGroupQueueInterfaceStatisticsPevid_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsPevid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsPevid.setStatus("current")


class _HwhqosUserGroupQueueInterfaceStatisticsCevid_Type(Integer32):
    """Custom type hwhqosUserGroupQueueInterfaceStatisticsCevid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwhqosUserGroupQueueInterfaceStatisticsCevid_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueInterfaceStatisticsCevid_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsCevid = _HwhqosUserGroupQueueInterfaceStatisticsCevid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 4),
    _HwhqosUserGroupQueueInterfaceStatisticsCevid_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsCevid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsCevid.setStatus("current")


class _HwhqosUserGroupQueueInterfaceStatisticsVlanid_Type(Integer32):
    """Custom type hwhqosUserGroupQueueInterfaceStatisticsVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwhqosUserGroupQueueInterfaceStatisticsVlanid_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueInterfaceStatisticsVlanid_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsVlanid = _HwhqosUserGroupQueueInterfaceStatisticsVlanid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 5),
    _HwhqosUserGroupQueueInterfaceStatisticsVlanid_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsVlanid.setStatus("current")


class _HwhqosUserGroupQueueInterfaceStatisticsQueueIndex_Type(Integer32):
    """Custom type hwhqosUserGroupQueueInterfaceStatisticsQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("total", 9))
    )


_HwhqosUserGroupQueueInterfaceStatisticsQueueIndex_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueInterfaceStatisticsQueueIndex_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsQueueIndex = _HwhqosUserGroupQueueInterfaceStatisticsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 6),
    _HwhqosUserGroupQueueInterfaceStatisticsQueueIndex_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsQueueIndex.setStatus("current")


class _HwhqosUserGroupQueueInterfaceStatisticsReset_Type(Integer32):
    """Custom type hwhqosUserGroupQueueInterfaceStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwhqosUserGroupQueueInterfaceStatisticsReset_Type.__name__ = "Integer32"
_HwhqosUserGroupQueueInterfaceStatisticsReset_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsReset = _HwhqosUserGroupQueueInterfaceStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 7),
    _HwhqosUserGroupQueueInterfaceStatisticsReset_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsReset.setStatus("current")
_HwhqosUserGroupQueueInterfaceStatisticsPassPackets_Type = Counter64
_HwhqosUserGroupQueueInterfaceStatisticsPassPackets_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsPassPackets = _HwhqosUserGroupQueueInterfaceStatisticsPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 8),
    _HwhqosUserGroupQueueInterfaceStatisticsPassPackets_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsPassPackets.setStatus("current")
_HwhqosUserGroupQueueInterfaceStatisticsPassBytes_Type = Counter64
_HwhqosUserGroupQueueInterfaceStatisticsPassBytes_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsPassBytes = _HwhqosUserGroupQueueInterfaceStatisticsPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 9),
    _HwhqosUserGroupQueueInterfaceStatisticsPassBytes_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsPassBytes.setStatus("current")
_HwhqosUserGroupQueueInterfaceStatisticsDropPackets_Type = Counter64
_HwhqosUserGroupQueueInterfaceStatisticsDropPackets_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsDropPackets = _HwhqosUserGroupQueueInterfaceStatisticsDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 10),
    _HwhqosUserGroupQueueInterfaceStatisticsDropPackets_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsDropPackets.setStatus("current")
_HwhqosUserGroupQueueInterfaceStatisticsDropBytes_Type = Counter64
_HwhqosUserGroupQueueInterfaceStatisticsDropBytes_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsDropBytes = _HwhqosUserGroupQueueInterfaceStatisticsDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 11),
    _HwhqosUserGroupQueueInterfaceStatisticsDropBytes_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsDropBytes.setStatus("current")
_HwhqosUserGroupQueueInterfaceStatisticsPassPacketsRate_Type = Counter64
_HwhqosUserGroupQueueInterfaceStatisticsPassPacketsRate_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsPassPacketsRate = _HwhqosUserGroupQueueInterfaceStatisticsPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 12),
    _HwhqosUserGroupQueueInterfaceStatisticsPassPacketsRate_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsPassPacketsRate.setStatus("current")
_HwhqosUserGroupQueueInterfaceStatisticsPassBytesRate_Type = Counter64
_HwhqosUserGroupQueueInterfaceStatisticsPassBytesRate_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsPassBytesRate = _HwhqosUserGroupQueueInterfaceStatisticsPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 13),
    _HwhqosUserGroupQueueInterfaceStatisticsPassBytesRate_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsPassBytesRate.setStatus("current")
_HwhqosUserGroupQueueInterfaceStatisticsDropPacketsRate_Type = Counter64
_HwhqosUserGroupQueueInterfaceStatisticsDropPacketsRate_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsDropPacketsRate = _HwhqosUserGroupQueueInterfaceStatisticsDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 14),
    _HwhqosUserGroupQueueInterfaceStatisticsDropPacketsRate_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsDropPacketsRate.setStatus("current")
_HwhqosUserGroupQueueInterfaceStatisticsDropBytesRate_Type = Counter64
_HwhqosUserGroupQueueInterfaceStatisticsDropBytesRate_Object = MibTableColumn
hwhqosUserGroupQueueInterfaceStatisticsDropBytesRate = _HwhqosUserGroupQueueInterfaceStatisticsDropBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 1, 71, 1, 15),
    _HwhqosUserGroupQueueInterfaceStatisticsDropBytesRate_Type()
)
hwhqosUserGroupQueueInterfaceStatisticsDropBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsDropBytesRate.setStatus("current")
_HwhqosObjects_ObjectIdentity = ObjectIdentity
hwhqosObjects = _HwhqosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 2)
)
_HwhqosUserFrameId_Type = Integer32
_HwhqosUserFrameId_Object = MibScalar
hwhqosUserFrameId = _HwhqosUserFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 2, 1),
    _HwhqosUserFrameId_Type()
)
hwhqosUserFrameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserFrameId.setStatus("current")
_HwhqosUserSlotId_Type = Integer32
_HwhqosUserSlotId_Object = MibScalar
hwhqosUserSlotId = _HwhqosUserSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 2, 2),
    _HwhqosUserSlotId_Type()
)
hwhqosUserSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserSlotId.setStatus("current")
_HwhqosUserPortId_Type = Integer32
_HwhqosUserPortId_Object = MibScalar
hwhqosUserPortId = _HwhqosUserPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 2, 3),
    _HwhqosUserPortId_Type()
)
hwhqosUserPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserPortId.setStatus("current")


class _HwhqosUserQueueApplyFailDirection_Type(Integer32):
    """Custom type hwhqosUserQueueApplyFailDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwhqosUserQueueApplyFailDirection_Type.__name__ = "Integer32"
_HwhqosUserQueueApplyFailDirection_Object = MibScalar
hwhqosUserQueueApplyFailDirection = _HwhqosUserQueueApplyFailDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 2, 4),
    _HwhqosUserQueueApplyFailDirection_Type()
)
hwhqosUserQueueApplyFailDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwhqosUserQueueApplyFailDirection.setStatus("current")
_HwhqosTraps_ObjectIdentity = ObjectIdentity
hwhqosTraps = _HwhqosTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 3)
)
_HwhqosConformance_ObjectIdentity = ObjectIdentity
hwhqosConformance = _HwhqosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4)
)
_HwhqosCompliances_ObjectIdentity = ObjectIdentity
hwhqosCompliances = _HwhqosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 1)
)
_HwhqosGroups_ObjectIdentity = ObjectIdentity
hwhqosGroups = _HwhqosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2)
)

# Managed Objects groups

hwhqosIfStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 1)
)
hwhqosIfStatGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosQueueForwardPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosQueueForwardBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosQueueDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosQueueDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosQueueRemarkPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosQueueRemarkBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosSetZero"),
        ("HUAWEI-HQOS-MIB", "hwhqosQueueForwardPacketRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosQueueForwardByteRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosQueueDropPacketRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosQueueDropByteRate"))
)
if mibBuilder.loadTexts:
    hwhqosIfStatGroup.setStatus("current")

hqhqosAtmPvcStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 2)
)
hqhqosAtmPvcStatGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosAtmPvcQueueForwardPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosAtmPvcQueueForwardBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosAtmPvcQueueDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosAtmPvcQueueDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosAtmPvcQueueRemarkPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosAtmPvcQueueRemarkBytes"))
)
if mibBuilder.loadTexts:
    hqhqosAtmPvcStatGroup.setStatus("current")

hwhqosPortQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 3)
)
hwhqosPortQueueGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosPortQueueArithmetic"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueueWeightValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueueShaValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueueShaPercent"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueueWredName"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueuePbsValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueueRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosPortQueueGroup.setStatus("current")

hwhqosWredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 4)
)
hwhqosWredGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosWredGreenLowLimit"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredGreenHighLimit"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredGreenDiscardPercent"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredYellowLowLimit"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredYellowHighLimit"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredYellowDiscardPercent"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredRedLowLimit"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredRedHighLimit"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredRedDiscardPercent"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosWredGroup.setStatus("current")

hwhqosIfQueueStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 5)
)
hwhqosIfQueueStatGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosIfQueueStatForwardPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosIfQueueStatForwardBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosIfQueueStatDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosIfQueueStatDropPackets"))
)
if mibBuilder.loadTexts:
    hwhqosIfQueueStatGroup.setStatus("current")

hwhqosUserQueueStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 6)
)
hwhqosUserQueueStatGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatForwardPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatForwardBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatReset"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatLastResetTime"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatPerDropPackets"))
)
if mibBuilder.loadTexts:
    hwhqosUserQueueStatGroup.setStatus("current")

hwhqosUserGroupQueueStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 7)
)
hwhqosUserGroupQueueStatGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatReset"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueForwardBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueForwardPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatLastResetTime"))
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatGroup.setStatus("current")

hwhqosObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 8)
)
hwhqosObjectsGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserFrameId"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserSlotId"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserPortId"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueApplyFailDirection"))
)
if mibBuilder.loadTexts:
    hwhqosObjectsGroup.setStatus("current")

hwhqosVpnQoSTunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 10)
)
hwhqosVpnQoSTunnelStatGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwVPNHQoSTunnelIfIndex"),
        ("HUAWEI-HQOS-MIB", "hwVPNHQoSVPNType"),
        ("HUAWEI-HQOS-MIB", "hwVPNHQoSVPNValue"),
        ("HUAWEI-HQOS-MIB", "hwVPNHQoSPassBytes"),
        ("HUAWEI-HQOS-MIB", "hwVPNHQoSPassPackets"),
        ("HUAWEI-HQOS-MIB", "hwVPNHQoSDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwVPNHQoSDropBytes"))
)
if mibBuilder.loadTexts:
    hwhqosVpnQoSTunnelStatGroup.setStatus("current")

hwhqosTunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 11)
)
hwhqosTunnelStatGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosTunnelIfIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosTunnelCosType"),
        ("HUAWEI-HQOS-MIB", "hwhqosTunnelVPNType"),
        ("HUAWEI-HQOS-MIB", "hwhqosTunnelVPNName"),
        ("HUAWEI-HQOS-MIB", "hwhqosTunnelPassBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosTunnelPassPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosTunnelDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosTunnelDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosTunnelPassedByteRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosTunnelPassPacketRate"))
)
if mibBuilder.loadTexts:
    hwhqosTunnelStatGroup.setStatus("current")

hwhqosProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 12)
)
hwhqosProfileGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosProfileName"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosProfileGroup.setStatus("current")

hwhqosProfileSuppressionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 13)
)
hwhqosProfileSuppressionGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosSuppressionDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosSuppressionType"),
        ("HUAWEI-HQOS-MIB", "hwhqosSuppressionCirValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosSuppressionCbsValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosSuppressionRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosProfileSuppressionGroup.setStatus("current")

hwhqosProfileCarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 14)
)
hwhqosProfileCarGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosProfileCarDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarCirValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarPirValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarCbsValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarPbsValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarGreenAction"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarYellowAction"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarRedAction"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosProfileCarGroup.setStatus("current")

hwhqosProfileUserQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 15)
)
hwhqosProfileUserQueueGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueCirValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueuePirValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueFlowQueueName"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueMappingName"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueGroupName"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueServiceTemplateName"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueGroup.setStatus("current")

hwhqosProfileUserApplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 16)
)
hwhqosProfileUserApplyGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosProfileInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyPevid"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyCevid"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyName"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyIdentifier"),
        ("HUAWEI-HQOS-MIB", "hwhqosGroupName"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosProfileUserApplyGroup.setStatus("current")

hwhqosFlowMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 17)
)
hwhqosFlowMappingGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosFlowMappingName"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowMappingRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosFlowMappingGroup.setStatus("current")

hwhqosFlowMappingCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 18)
)
hwhqosFlowMappingCfgGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosFolwMappingCfgQueueCosValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowMappingCfgPortQueueCosValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowMappingCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosFlowMappingCfgGroup.setStatus("current")

hwhqosFlowQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 19)
)
hwhqosFlowQueueGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosFlowQueueName"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosFlowQueueGroup.setStatus("current")

hwhqosFlowQueueCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 20)
)
hwhqosFlowQueueCfgGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosFlowQueueCfgCosValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueCfgType"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueCfgWeightValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueCfgShapingValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueCfgShapingPercentageValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueCfgPbsValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueCfgWredName"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosFlowQueueCfgGroup.setStatus("current")

hwhqosFlowWredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 21)
)
hwhqosFlowWredGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosFlowWredName"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowWredRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosFlowWredGroup.setStatus("current")

hwhqosFlowWredColorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 22)
)
hwhqosFlowWredColorGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosFlowWredColor"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowWredColorLowlimitPercentage"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowWredColorHighlimitPercentage"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowWredColorDiscardPercentage"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowWredColorRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosFlowWredColorGroup.setStatus("current")

hwhqosUserGroupQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 23)
)
hwhqosUserGroupQueueGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueSlotNumber"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueGroup.setStatus("current")

hwhqosUserGroupQueueShapingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 24)
)
hwhqosUserGroupQueueShapingGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueShapingDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueShapingValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueuePbsValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueShapingRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueShapingGroup.setStatus("current")

hwhqosUserQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 25)
)
hwhqosUserQueueGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserQueueInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueCirValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueuePirValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueFlowQueueName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueFlowMappingName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueGroupName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueServiceTemplateName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosUserQueueGroup.setStatus("current")

hwhqosBehaviorUserQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 26)
)
hwhqosBehaviorUserQueueGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosBehaviorName"),
        ("HUAWEI-HQOS-MIB", "hwhqosBehaviorCirValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosBehaviorPirValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosBehaviorFlowQueueName"),
        ("HUAWEI-HQOS-MIB", "hwhqosBehaviorFlowMappingName"),
        ("HUAWEI-HQOS-MIB", "hwhqosBehaviorGroupName"),
        ("HUAWEI-HQOS-MIB", "hwhqosBehaviorServiceTemplateName"),
        ("HUAWEI-HQOS-MIB", "hwhqosBehaviorUserQueueRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosBehaviorUserQueueGroup.setStatus("current")

hwhqosBandwidthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 27)
)
hwhqosBandwidthGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosBandwidthInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosBandwidthValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosBandwidthRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosBandwidthGroup.setStatus("current")

hwhqosServiceTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 28)
)
hwhqosServiceTemplateGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosServiceTemplateName"),
        ("HUAWEI-HQOS-MIB", "hwhqosSlotNumber"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceTemplateRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosServiceTemplateGroup.setStatus("current")

hwhqosNetworkHeaderLengthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 29)
)
hwhqosNetworkHeaderLengthGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosNetworkHeaderLengthDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosNetWorkHeaderLengthValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosNetWorkHeaderLengthRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosNetworkHeaderLengthGroup.setStatus("current")

hwhqosServiceTemplateApplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 30)
)
hwhqosServiceTemplateApplyGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosServiceTemplateApplyInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosApplyServiceTemplateName"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceTemplateApplyRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosServiceTemplateApplyGroup.setStatus("current")

hwhqosProfileUserQueueStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 31)
)
hwhqosProfileUserQueueStatisticsGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsPevid"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsCevid"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsSlotNumber"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsQueueIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsReset"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsPassPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsPassBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsPassPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsPassBytesRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsDropPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsDropBytesRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsTrafficTowardsThisInterface"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsConfiguredCir"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileUserQueueStatisticsConfiguredPir"))
)
if mibBuilder.loadTexts:
    hwhqosProfileUserQueueStatisticsGroup.setStatus("current")

hwhqosProfileCarStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 32)
)
hwhqosProfileCarStatisticsGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsPevid"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsCevid"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsType"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsSlotNumber"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsReset"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsPassPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsPassBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsPassPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsPassBytesRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsDropPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileCarStatisticsDropBytesRate"))
)
if mibBuilder.loadTexts:
    hwhqosProfileCarStatisticsGroup.setStatus("current")

hwhqosUserQueueStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 33)
)
hwhqosUserQueueStatisticsGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsSlotNumber"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsQueueIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsReset"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsPassPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsPassBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsPassPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsPassBytesRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsDropPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatisticsDropBytesRate"))
)
if mibBuilder.loadTexts:
    hwhqosUserQueueStatisticsGroup.setStatus("current")

hwhqosUserQueueClassifierStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 34)
)
hwhqosUserQueueClassifierStatisticsGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsClassifierName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsSlotNumber"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsQueueIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsReset"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsPassPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsPassBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsPassPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsPassBytesRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsDropPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueClassifierStatisticsDropBytesRate"))
)
if mibBuilder.loadTexts:
    hwhqosUserQueueClassifierStatisticsGroup.setStatus("current")

hwhqosUserGroupQueueStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 35)
)
hwhqosUserGroupQueueStatisticsGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsGroupName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsSlotNumber"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsQueueIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsReset"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsPassPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsPassBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsPassPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsPassBytesRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsDropPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueStatisticsDropBytesRate"))
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueStatisticsGroup.setStatus("current")

hwhqosFlowQueueShaperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 36)
)
hwhqosFlowQueueShaperGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosFlowQueueShaperBE"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueShaperAF1"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueShaperAF2"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueShaperAF3"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueShaperAF4"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueShaperEF"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueShaperCS6"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueShaperCS7"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueShaperValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosFlowQueueShaperRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosFlowQueueShaperGroup.setStatus("current")

hwhqosWredQueueDepthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 37)
)
hwhqosWredQueueDepthGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosWredQueueDepthType"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredQueueDepthWredName"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredQueueDepthValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosWredQueueDepthRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosWredQueueDepthGroup.setStatus("current")

hwhqosBandwidthCheck = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 38)
)
hwhqosBandwidthCheck.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosBandwidthCheckInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosBandwidthCheckValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosBandwidthCheckRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosBandwidthCheck.setStatus("current")

hwhqosServiceIdentifyPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 39)
)
hwhqosServiceIdentifyPolicyGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyName"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyGroup.setStatus("current")

hwhqosServiceIdentifyPolicyApplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 40)
)
hwhqosServiceIdentifyPolicyApplyGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyApplyInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyApplyName"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyApplyRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyApplyGroup.setStatus("current")

hwhqosServiceIdentifyPolicyTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 41)
)
hwhqosServiceIdentifyPolicyTypeGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyTypeValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyTypeRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyTypeGroup.setStatus("current")

hwhqosServiceIdentifyPolicyVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 42)
)
hwhqosServiceIdentifyPolicyVlanGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyVlanID"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyVlanDomainName"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyVlanRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyVlanGroup.setStatus("current")

hwhqosServiceIdentifyPolicy8021pGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 43)
)
hwhqosServiceIdentifyPolicy8021pGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicy8021pCosID"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicy8021pDomainName"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicy8021pRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicy8021pGroup.setStatus("current")

hwhqosServiceIdentifyPolicyDscpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 44)
)
hwhqosServiceIdentifyPolicyDscpGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyDscpID"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyDscpDomainName"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyDscpRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyDscpGroup.setStatus("current")

hwhqosServiceIdentifyPolicyOption60Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 45)
)
hwhqosServiceIdentifyPolicyOption60Group.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyOption60"),
        ("HUAWEI-HQOS-MIB", "hwhqosServiceIdentifyPolicyOption60RowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosServiceIdentifyPolicyOption60Group.setStatus("current")

hwhqosDomainRateLimitModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 46)
)
hwhqosDomainRateLimitModeGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosDomainRateLimitModeDomainName"),
        ("HUAWEI-HQOS-MIB", "hwhqosDomainRateLimitModeRateLimitMode"),
        ("HUAWEI-HQOS-MIB", "hwhqosDomainRateLimitModeRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosDomainRateLimitModeGroup.setStatus("current")

hwhqosDomainSessionGroupExcludeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 47)
)
hwhqosDomainSessionGroupExcludeGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosDomainSessionGroupExcludeDomainName"),
        ("HUAWEI-HQOS-MIB", "hwhqosDomainSessionGroupExcludeRowStatus"),
        ("HUAWEI-HQOS-MIB", "hwhqosDomainSessionGroupExcludeMode"))
)
if mibBuilder.loadTexts:
    hwhqosDomainSessionGroupExcludeGroup.setStatus("current")

hwhqosDomainUserMaxSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 48)
)
hwhqosDomainUserMaxSessionGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosDomainUserMaxSessionDomainName"),
        ("HUAWEI-HQOS-MIB", "hwhqosDomainUserMaxSessionNum"),
        ("HUAWEI-HQOS-MIB", "hwhqosDomainUserMaxSessionRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosDomainUserMaxSessionGroup.setStatus("current")

hwhqosUpdateUseridProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 49)
)
hwhqosUpdateUseridProfileGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUpdateUseridProfileUserid"),
        ("HUAWEI-HQOS-MIB", "hwhqosUpdateUseridProfileDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosUpdateUseridProfileName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUpdateUseridProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosUpdateUseridProfileGroup.setStatus("current")

hwhqosDomainUserPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 50)
)
hwhqosDomainUserPriorityGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosDomainUserPriorityDomainName"),
        ("HUAWEI-HQOS-MIB", "hwhqosDomainUserPriorityDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosDomainUserPriorityRowStatus"),
        ("HUAWEI-HQOS-MIB", "hwhqosDomainUserPriorityValue"))
)
if mibBuilder.loadTexts:
    hwhqosDomainUserPriorityGroup.setStatus("current")

hwhqosUseridStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 52)
)
hwhqosUseridStatGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUseridStatUserid"),
        ("HUAWEI-HQOS-MIB", "hwhqosUseridStatQueue"),
        ("HUAWEI-HQOS-MIB", "hwhqosUseridStatDirection"))
)
if mibBuilder.loadTexts:
    hwhqosUseridStatGroup.setStatus("current")

hwhqosFatherUserGroupQueueApplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 55)
)
hwhqosFatherUserGroupQueueApplyGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosFatherUserGroupQueueApplyInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosFatherUserGroupQueueApplyDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosFatherUserGroupQueueApplyName"),
        ("HUAWEI-HQOS-MIB", "hwhqosFatherUserGroupQueueApplyRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosFatherUserGroupQueueApplyGroup.setStatus("current")

hwhqosUserGroupQueueApplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 56)
)
hwhqosUserGroupQueueApplyGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueApplyInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueApplyDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueApplyPeVid"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueApplyCeVid"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueApplyName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueApplyEachvlan"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueApplyRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueApplyGroup.setStatus("current")

hwhqosProfileApplyDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 57)
)
hwhqosProfileApplyDomainGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosProfileApplyDomainName"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyDomainDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyDomainProfileName"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyDomainRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosProfileApplyDomainGroup.setStatus("current")

hwhqosProfileApplyUserVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 58)
)
hwhqosProfileApplyUserVlanGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosProfileApplyUserVlanInterfaceIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyUserVlanDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyUserVlanPeVid"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyUserVlanCeVid"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyUserVlanProfileName"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyUserVlanEach"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileApplyUserVlanRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosProfileApplyUserVlanGroup.setStatus("current")

hwhqosLinkAdjRemoteEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 59)
)
hwhqosLinkAdjRemoteEnableGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteEnableType"),
        ("HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteEnable"),
        ("HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteEnableSlot"),
        ("HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteEnableRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteEnableGroup.setStatus("current")

hwhqosLinkAdjShapingModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 60)
)
hwhqosLinkAdjShapingModeGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosLinkAdjShapingModeType"),
        ("HUAWEI-HQOS-MIB", "hwhqosLinkAdjShapingMode"),
        ("HUAWEI-HQOS-MIB", "hwhqosLinkAdjShapingModeRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjShapingModeGroup.setStatus("current")

hwhqosLinkAdjRemoteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 61)
)
hwhqosLinkAdjRemoteGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteType"),
        ("HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosLinkAdjRemoteRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjRemoteGroup.setStatus("current")

hwhqosLinkAdjLocalTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 62)
)
hwhqosLinkAdjLocalTableGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosLinkAdjLocalSlotNumber"),
        ("HUAWEI-HQOS-MIB", "hwhqosLinkAdjLocalValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosLinkAdjLocalRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjLocalTableGroup.setStatus("current")

hwhqosLinkAdjExcludeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 63)
)
hwhqosLinkAdjExcludeGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosLinkAdjExcludeSlotNumber"),
        ("HUAWEI-HQOS-MIB", "hwhqosLinkAdjExcludeEnable"),
        ("HUAWEI-HQOS-MIB", "hwhqosLinkAdjExcludeRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosLinkAdjExcludeGroup.setStatus("current")

hwhqosProfileInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 64)
)
hwhqosProfileInfoGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosProfileInfoName"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileInfoDescription"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileInfoRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosProfileInfoGroup.setStatus("current")

hwhqosUserGroupQueueTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 65)
)
hwhqosUserGroupQueueTemplateGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueTemplateName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueTemplateModeTemplate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueTemplateRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueTemplateGroup.setStatus("current")

hwhqosProfileWeightGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 66)
)
hwhqosProfileWeightGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosProfileWeightDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileWeightValue"),
        ("HUAWEI-HQOS-MIB", "hwhqosProfileWeightRowStatus"))
)
if mibBuilder.loadTexts:
    hwhqosProfileWeightGroup.setStatus("current")

hwhqosUserGroupQueueInterfaceStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 70)
)
hwhqosUserGroupQueueInterfaceStatisticsGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsIfIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsDirection"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsPevid"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsCevid"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsVlanid"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsQueueIndex"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsReset"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsPassPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsPassBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsDropPackets"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsDropBytes"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsPassPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsPassBytesRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsDropPacketsRate"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserGroupQueueInterfaceStatisticsDropBytesRate"))
)
if mibBuilder.loadTexts:
    hwhqosUserGroupQueueInterfaceStatisticsGroup.setStatus("current")


# Notification objects

hwhqosUserQueueStatDiscardAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 3, 1)
)
hwhqosUserQueueStatDiscardAlarmTrap.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserFrameId"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserSlotId"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserPortId"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatPerDropPackets"))
)
if mibBuilder.loadTexts:
    hwhqosUserQueueStatDiscardAlarmTrap.setStatus(
        "current"
    )

hwhqosUserQueueApplyPirFailAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 3, 2)
)
hwhqosUserQueueApplyPirFailAlarmTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueApplyFailDirection"))
)
if mibBuilder.loadTexts:
    hwhqosUserQueueApplyPirFailAlarmTrap.setStatus(
        "current"
    )

hwhqosUserQueueApplyPirSucessAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 3, 3)
)
hwhqosUserQueueApplyPirSucessAlarmTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueApplyFailDirection"))
)
if mibBuilder.loadTexts:
    hwhqosUserQueueApplyPirSucessAlarmTrap.setStatus(
        "current"
    )

hwhqosUserQueueApplyAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 3, 4)
)
hwhqosUserQueueApplyAlarmTrap.setObjects(
    ("HUAWEI-HQOS-MIB", "hwhqosUserQueueApplyAlarmIfNetName")
)
if mibBuilder.loadTexts:
    hwhqosUserQueueApplyAlarmTrap.setStatus(
        "current"
    )

hwhqosPortQueueStatDiscardAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 3, 5)
)
hwhqosPortQueueStatDiscardAlarmTrap.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosPortQueueInterfaceTrap"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueueCosValueTrap"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueueDiscardTypeTrap"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueueDiscardValueTrap"))
)
if mibBuilder.loadTexts:
    hwhqosPortQueueStatDiscardAlarmTrap.setStatus(
        "current"
    )

hwhqosPortQueueStatDiscardAlarmCancelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 3, 6)
)
hwhqosPortQueueStatDiscardAlarmCancelTrap.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosPortQueueInterfaceCancel"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueueCosValueCancel"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueueDiscardTypeCancel"),
        ("HUAWEI-HQOS-MIB", "hwhqosPortQueueDiscardValueCancel"))
)
if mibBuilder.loadTexts:
    hwhqosPortQueueStatDiscardAlarmCancelTrap.setStatus(
        "current"
    )


# Notifications groups

hwhqosUserQueueStatTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 9)
)
hwhqosUserQueueStatTrapGroup.setObjects(
      *(("HUAWEI-HQOS-MIB", "hwhqosUserQueueStatDiscardAlarmTrap"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueApplyPirFailAlarmTrap"),
        ("HUAWEI-HQOS-MIB", "hwhqosUserQueueApplyPirSucessAlarmTrap"))
)
if mibBuilder.loadTexts:
    hwhqosUserQueueStatTrapGroup.setStatus(
        "current"
    )

hwhqosUserQueueApplyAlarmGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 67)
)
hwhqosUserQueueApplyAlarmGroup.setObjects(
    ("HUAWEI-HQOS-MIB", "hwhqosUserQueueApplyAlarmTrap")
)
if mibBuilder.loadTexts:
    hwhqosUserQueueApplyAlarmGroup.setStatus(
        "current"
    )

hwhqosPortQueueStatDiscardAlarmTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 68)
)
hwhqosPortQueueStatDiscardAlarmTrapGroup.setObjects(
    ("HUAWEI-HQOS-MIB", "hwhqosPortQueueStatDiscardAlarmTrap")
)
if mibBuilder.loadTexts:
    hwhqosPortQueueStatDiscardAlarmTrapGroup.setStatus(
        "current"
    )

hwhqosPortQueueStatDiscarAlarmCancelGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 2, 69)
)
hwhqosPortQueueStatDiscarAlarmCancelGroup.setObjects(
    ("HUAWEI-HQOS-MIB", "hwhqosPortQueueStatDiscardAlarmCancelTrap")
)
if mibBuilder.loadTexts:
    hwhqosPortQueueStatDiscarAlarmCancelGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwhqosUserQueueStatCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 132, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwhqosUserQueueStatCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-HQOS-MIB",
    **{"CosType": CosType,
       "hwHQOS": hwHQOS,
       "hwhqosStat": hwhqosStat,
       "hwhqosIfStatTable": hwhqosIfStatTable,
       "hwhqosIfStatEntry": hwhqosIfStatEntry,
       "hwhqosIfIndex": hwhqosIfIndex,
       "hwhqosDirection": hwhqosDirection,
       "hwhqosUserLayer1": hwhqosUserLayer1,
       "hwhqosUserLayer2": hwhqosUserLayer2,
       "hwhqosQueueIndex": hwhqosQueueIndex,
       "hwhqosQueueForwardPackets": hwhqosQueueForwardPackets,
       "hwhqosQueueForwardBytes": hwhqosQueueForwardBytes,
       "hwhqosQueueDropPackets": hwhqosQueueDropPackets,
       "hwhqosQueueDropBytes": hwhqosQueueDropBytes,
       "hwhqosQueueRemarkPackets": hwhqosQueueRemarkPackets,
       "hwhqosQueueRemarkBytes": hwhqosQueueRemarkBytes,
       "hwhqosSetZero": hwhqosSetZero,
       "hwhqosQueueForwardPacketRate": hwhqosQueueForwardPacketRate,
       "hwhqosQueueForwardByteRate": hwhqosQueueForwardByteRate,
       "hwhqosQueueDropPacketRate": hwhqosQueueDropPacketRate,
       "hwhqosQueueDropByteRate": hwhqosQueueDropByteRate,
       "hwhqosAtmPvcStatTable": hwhqosAtmPvcStatTable,
       "hwhqosAtmPvcStatEntry": hwhqosAtmPvcStatEntry,
       "hwhqosAtmPvcIfIndex": hwhqosAtmPvcIfIndex,
       "hwhqosAtmPvcVPI": hwhqosAtmPvcVPI,
       "hwhqosAtmPvcVCI": hwhqosAtmPvcVCI,
       "hwhqosAtmPvcDirection": hwhqosAtmPvcDirection,
       "hwhqosAtmPvcUserLayer1": hwhqosAtmPvcUserLayer1,
       "hwhqosAtmPvcUserLayer2": hwhqosAtmPvcUserLayer2,
       "hwhqosAtmPvcQueueIndex": hwhqosAtmPvcQueueIndex,
       "hwhqosAtmPvcQueueForwardPackets": hwhqosAtmPvcQueueForwardPackets,
       "hwhqosAtmPvcQueueForwardBytes": hwhqosAtmPvcQueueForwardBytes,
       "hwhqosAtmPvcQueueDropPackets": hwhqosAtmPvcQueueDropPackets,
       "hwhqosAtmPvcQueueDropBytes": hwhqosAtmPvcQueueDropBytes,
       "hwhqosAtmPvcQueueRemarkPackets": hwhqosAtmPvcQueueRemarkPackets,
       "hwhqosAtmPvcQueueRemarkBytes": hwhqosAtmPvcQueueRemarkBytes,
       "hwhqosPortQueueTable": hwhqosPortQueueTable,
       "hwhqosPortQueueEntry": hwhqosPortQueueEntry,
       "hwhqosPortQueueIfIndex": hwhqosPortQueueIfIndex,
       "hwhqosPortQueueCosValue": hwhqosPortQueueCosValue,
       "hwhqosPortQueueArithmetic": hwhqosPortQueueArithmetic,
       "hwhqosPortQueueWeightValue": hwhqosPortQueueWeightValue,
       "hwhqosPortQueueShaValue": hwhqosPortQueueShaValue,
       "hwhqosPortQueueShaPercent": hwhqosPortQueueShaPercent,
       "hwhqosPortQueueWredName": hwhqosPortQueueWredName,
       "hwhqosPortQueuePbsValue": hwhqosPortQueuePbsValue,
       "hwhqosPortQueueRowStatus": hwhqosPortQueueRowStatus,
       "hwhqosWredTable": hwhqosWredTable,
       "hwhqosWredEntry": hwhqosWredEntry,
       "hwhqosWredName": hwhqosWredName,
       "hwhqosWredGreenLowLimit": hwhqosWredGreenLowLimit,
       "hwhqosWredGreenHighLimit": hwhqosWredGreenHighLimit,
       "hwhqosWredGreenDiscardPercent": hwhqosWredGreenDiscardPercent,
       "hwhqosWredYellowLowLimit": hwhqosWredYellowLowLimit,
       "hwhqosWredYellowHighLimit": hwhqosWredYellowHighLimit,
       "hwhqosWredYellowDiscardPercent": hwhqosWredYellowDiscardPercent,
       "hwhqosWredRedLowLimit": hwhqosWredRedLowLimit,
       "hwhqosWredRedHighLimit": hwhqosWredRedHighLimit,
       "hwhqosWredRedDiscardPercent": hwhqosWredRedDiscardPercent,
       "hwhqosWredRowStatus": hwhqosWredRowStatus,
       "hwhqosIfQueueStatTable": hwhqosIfQueueStatTable,
       "hwhqosIfQueueStatEntry": hwhqosIfQueueStatEntry,
       "hwhqosIfQueueStatIfIndex": hwhqosIfQueueStatIfIndex,
       "hwhqosIfQueueStatQueueIndex": hwhqosIfQueueStatQueueIndex,
       "hwhqosIfQueueStatDirection": hwhqosIfQueueStatDirection,
       "hwhqosIfQueueStatForwardPackets": hwhqosIfQueueStatForwardPackets,
       "hwhqosIfQueueStatForwardBytes": hwhqosIfQueueStatForwardBytes,
       "hwhqosIfQueueStatDropPackets": hwhqosIfQueueStatDropPackets,
       "hwhqosIfQueueStatDropBytes": hwhqosIfQueueStatDropBytes,
       "hwhqosUserQueueStatTable": hwhqosUserQueueStatTable,
       "hwhqosUserQueueStatEntry": hwhqosUserQueueStatEntry,
       "hwhqosUserQueueStatType": hwhqosUserQueueStatType,
       "hwhqosUserQueueStatNameString": hwhqosUserQueueStatNameString,
       "hwhqosUserQueueStatDirection": hwhqosUserQueueStatDirection,
       "hwhqosUserQueueStatQueueIndex": hwhqosUserQueueStatQueueIndex,
       "hwhqosUserQueueStatForwardPackets": hwhqosUserQueueStatForwardPackets,
       "hwhqosUserQueueStatForwardBytes": hwhqosUserQueueStatForwardBytes,
       "hwhqosUserQueueStatDropPackets": hwhqosUserQueueStatDropPackets,
       "hwhqosUserQueueStatDropBytes": hwhqosUserQueueStatDropBytes,
       "hwhqosUserQueueStatReset": hwhqosUserQueueStatReset,
       "hwhqosUserQueueStatLastResetTime": hwhqosUserQueueStatLastResetTime,
       "hwhqosUserQueueStatPerDropPackets": hwhqosUserQueueStatPerDropPackets,
       "hwhqosUserGroupQueueStatTable": hwhqosUserGroupQueueStatTable,
       "hwhqosUserGroupQueueStatEntry": hwhqosUserGroupQueueStatEntry,
       "hwhqosUserGroupQueueStatGroupName": hwhqosUserGroupQueueStatGroupName,
       "hwhqosUserGroupQueueStatDirection": hwhqosUserGroupQueueStatDirection,
       "hwhqosUserGroupQueueForwardPackets": hwhqosUserGroupQueueForwardPackets,
       "hwhqosUserGroupQueueForwardBytes": hwhqosUserGroupQueueForwardBytes,
       "hwhqosUserGroupQueueDropPackets": hwhqosUserGroupQueueDropPackets,
       "hwhqosUserGroupQueueDropBytes": hwhqosUserGroupQueueDropBytes,
       "hwhqosUserGroupQueueStatReset": hwhqosUserGroupQueueStatReset,
       "hwhqosUserGroupQueueStatLastResetTime": hwhqosUserGroupQueueStatLastResetTime,
       "hwVPNHQoSTunnelStatisticsTable": hwVPNHQoSTunnelStatisticsTable,
       "hwVPNHQoSTunnelStatisticsEntry": hwVPNHQoSTunnelStatisticsEntry,
       "hwVPNHQoSTunnelIfIndex": hwVPNHQoSTunnelIfIndex,
       "hwVPNHQoSVPNType": hwVPNHQoSVPNType,
       "hwVPNHQoSVPNValue": hwVPNHQoSVPNValue,
       "hwVPNHQoSPassBytes": hwVPNHQoSPassBytes,
       "hwVPNHQoSPassPackets": hwVPNHQoSPassPackets,
       "hwVPNHQoSDropPackets": hwVPNHQoSDropPackets,
       "hwVPNHQoSDropBytes": hwVPNHQoSDropBytes,
       "hwhqosTunnelStatisticsTable": hwhqosTunnelStatisticsTable,
       "hwhqosTunnelStatisticsEntry": hwhqosTunnelStatisticsEntry,
       "hwhqosTunnelIfIndex": hwhqosTunnelIfIndex,
       "hwhqosTunnelCosType": hwhqosTunnelCosType,
       "hwhqosTunnelVPNType": hwhqosTunnelVPNType,
       "hwhqosTunnelVPNName": hwhqosTunnelVPNName,
       "hwhqosTunnelPassBytes": hwhqosTunnelPassBytes,
       "hwhqosTunnelPassPackets": hwhqosTunnelPassPackets,
       "hwhqosTunnelDropBytes": hwhqosTunnelDropBytes,
       "hwhqosTunnelDropPackets": hwhqosTunnelDropPackets,
       "hwhqosTunnelPassedByteRate": hwhqosTunnelPassedByteRate,
       "hwhqosTunnelPassPacketRate": hwhqosTunnelPassPacketRate,
       "hwhqosProfileTable": hwhqosProfileTable,
       "hwhqosProfileEntry": hwhqosProfileEntry,
       "hwhqosProfileName": hwhqosProfileName,
       "hwhqosProfileDescription": hwhqosProfileDescription,
       "hwhqosProfileRowStatus": hwhqosProfileRowStatus,
       "hwhqosProfileSuppressionTable": hwhqosProfileSuppressionTable,
       "hwhqosProfileSuppressionEntry": hwhqosProfileSuppressionEntry,
       "hwhqosSuppressionDirection": hwhqosSuppressionDirection,
       "hwhqosSuppressionType": hwhqosSuppressionType,
       "hwhqosSuppressionCirValue": hwhqosSuppressionCirValue,
       "hwhqosSuppressionCbsValue": hwhqosSuppressionCbsValue,
       "hwhqosSuppressionRowStatus": hwhqosSuppressionRowStatus,
       "hwhqosProfileCarTable": hwhqosProfileCarTable,
       "hwhqosProfileCarEntry": hwhqosProfileCarEntry,
       "hwhqosProfileCarDirection": hwhqosProfileCarDirection,
       "hwhqosProfileCarCirValue": hwhqosProfileCarCirValue,
       "hwhqosProfileCarPirValue": hwhqosProfileCarPirValue,
       "hwhqosProfileCarCbsValue": hwhqosProfileCarCbsValue,
       "hwhqosProfileCarPbsValue": hwhqosProfileCarPbsValue,
       "hwhqosProfileCarGreenAction": hwhqosProfileCarGreenAction,
       "hwhqosProfileCarYellowAction": hwhqosProfileCarYellowAction,
       "hwhqosProfileCarRedAction": hwhqosProfileCarRedAction,
       "hwhqosProfileCarRowStatus": hwhqosProfileCarRowStatus,
       "hwhqosProfileUserQueueTable": hwhqosProfileUserQueueTable,
       "hwhqosProfileUserQueueEntry": hwhqosProfileUserQueueEntry,
       "hwhqosProfileUserQueueDirection": hwhqosProfileUserQueueDirection,
       "hwhqosProfileUserQueueCirValue": hwhqosProfileUserQueueCirValue,
       "hwhqosProfileUserQueuePirValue": hwhqosProfileUserQueuePirValue,
       "hwhqosProfileUserQueueFlowQueueName": hwhqosProfileUserQueueFlowQueueName,
       "hwhqosProfileUserQueueMappingName": hwhqosProfileUserQueueMappingName,
       "hwhqosProfileUserQueueGroupName": hwhqosProfileUserQueueGroupName,
       "hwhqosProfileUserQueueServiceTemplateName": hwhqosProfileUserQueueServiceTemplateName,
       "hwhqosProfileUserQueueRowStatus": hwhqosProfileUserQueueRowStatus,
       "hwhqosProfileApplyTable": hwhqosProfileApplyTable,
       "hwhqosProfileApplyEntry": hwhqosProfileApplyEntry,
       "hwhqosProfileInterfaceIndex": hwhqosProfileInterfaceIndex,
       "hwhqosProfileApplyDirection": hwhqosProfileApplyDirection,
       "hwhqosProfileApplyPevid": hwhqosProfileApplyPevid,
       "hwhqosProfileApplyCevid": hwhqosProfileApplyCevid,
       "hwhqosProfileApplyName": hwhqosProfileApplyName,
       "hwhqosProfileApplyIdentifier": hwhqosProfileApplyIdentifier,
       "hwhqosGroupName": hwhqosGroupName,
       "hwhqosProfileApplyRowStatus": hwhqosProfileApplyRowStatus,
       "hwhqosFlowMappingTable": hwhqosFlowMappingTable,
       "hwhqosFlowMappingEntry": hwhqosFlowMappingEntry,
       "hwhqosFlowMappingName": hwhqosFlowMappingName,
       "hwhqosFlowMappingRowStatus": hwhqosFlowMappingRowStatus,
       "hwhqosFlowMappingCfgTable": hwhqosFlowMappingCfgTable,
       "hwhqosFlowMappingCfgEntry": hwhqosFlowMappingCfgEntry,
       "hwhqosFolwMappingCfgQueueCosValue": hwhqosFolwMappingCfgQueueCosValue,
       "hwhqosFlowMappingCfgPortQueueCosValue": hwhqosFlowMappingCfgPortQueueCosValue,
       "hwhqosFlowMappingCfgRowStatus": hwhqosFlowMappingCfgRowStatus,
       "hwhqosFlowQueueTable": hwhqosFlowQueueTable,
       "hwhqosFlowQueueEntry": hwhqosFlowQueueEntry,
       "hwhqosFlowQueueName": hwhqosFlowQueueName,
       "hwhqosFlowQueueRowStatus": hwhqosFlowQueueRowStatus,
       "hwhqosFlowQueueCfgTable": hwhqosFlowQueueCfgTable,
       "hwhqosFlowQueueCfgEntry": hwhqosFlowQueueCfgEntry,
       "hwhqosFlowQueueCfgCosValue": hwhqosFlowQueueCfgCosValue,
       "hwhqosFlowQueueCfgType": hwhqosFlowQueueCfgType,
       "hwhqosFlowQueueCfgWeightValue": hwhqosFlowQueueCfgWeightValue,
       "hwhqosFlowQueueCfgShapingValue": hwhqosFlowQueueCfgShapingValue,
       "hwhqosFlowQueueCfgShapingPercentageValue": hwhqosFlowQueueCfgShapingPercentageValue,
       "hwhqosFlowQueueCfgWredName": hwhqosFlowQueueCfgWredName,
       "hwhqosFlowQueueCfgPbsValue": hwhqosFlowQueueCfgPbsValue,
       "hwhqosFlowQueueCfgRowStatus": hwhqosFlowQueueCfgRowStatus,
       "hwhqosFlowWredTable": hwhqosFlowWredTable,
       "hwhqosFlowWredEntry": hwhqosFlowWredEntry,
       "hwhqosFlowWredName": hwhqosFlowWredName,
       "hwhqosFlowWredRowStatus": hwhqosFlowWredRowStatus,
       "hwhqosFlowWredColorTable": hwhqosFlowWredColorTable,
       "hwhqosFlowWredColorEntry": hwhqosFlowWredColorEntry,
       "hwhqosFlowWredColor": hwhqosFlowWredColor,
       "hwhqosFlowWredColorLowlimitPercentage": hwhqosFlowWredColorLowlimitPercentage,
       "hwhqosFlowWredColorHighlimitPercentage": hwhqosFlowWredColorHighlimitPercentage,
       "hwhqosFlowWredColorDiscardPercentage": hwhqosFlowWredColorDiscardPercentage,
       "hwhqosFlowWredColorRowStatus": hwhqosFlowWredColorRowStatus,
       "hwhqosUserGroupQueueTable": hwhqosUserGroupQueueTable,
       "hwhqosUserGroupQueueEntry": hwhqosUserGroupQueueEntry,
       "hwhqosUserGroupQueueName": hwhqosUserGroupQueueName,
       "hwhqosUserGroupQueueSlotNumber": hwhqosUserGroupQueueSlotNumber,
       "hwhqosUserGroupQueueRowStatus": hwhqosUserGroupQueueRowStatus,
       "hwhqosUserGroupQueueShapingTable": hwhqosUserGroupQueueShapingTable,
       "hwhqosUserGroupQueueShapingEntry": hwhqosUserGroupQueueShapingEntry,
       "hwhqosUserGroupQueueShapingDirection": hwhqosUserGroupQueueShapingDirection,
       "hwhqosUserGroupQueueShapingValue": hwhqosUserGroupQueueShapingValue,
       "hwhqosUserGroupQueuePbsValue": hwhqosUserGroupQueuePbsValue,
       "hwhqosUserGroupQueueShapingRowStatus": hwhqosUserGroupQueueShapingRowStatus,
       "hwhqosUserQueueTable": hwhqosUserQueueTable,
       "hwhqosUserQueueEntry": hwhqosUserQueueEntry,
       "hwhqosUserQueueInterfaceIndex": hwhqosUserQueueInterfaceIndex,
       "hwhqosUserQueueDirection": hwhqosUserQueueDirection,
       "hwhqosUserQueueCirValue": hwhqosUserQueueCirValue,
       "hwhqosUserQueuePirValue": hwhqosUserQueuePirValue,
       "hwhqosUserQueueFlowQueueName": hwhqosUserQueueFlowQueueName,
       "hwhqosUserQueueFlowMappingName": hwhqosUserQueueFlowMappingName,
       "hwhqosUserQueueGroupName": hwhqosUserQueueGroupName,
       "hwhqosUserQueueServiceTemplateName": hwhqosUserQueueServiceTemplateName,
       "hwhqosUserQueueRowStatus": hwhqosUserQueueRowStatus,
       "hwhqosBehaviorUserQueueTable": hwhqosBehaviorUserQueueTable,
       "hwhqosBehaviorUserQueueEntry": hwhqosBehaviorUserQueueEntry,
       "hwhqosBehaviorName": hwhqosBehaviorName,
       "hwhqosBehaviorCirValue": hwhqosBehaviorCirValue,
       "hwhqosBehaviorPirValue": hwhqosBehaviorPirValue,
       "hwhqosBehaviorFlowQueueName": hwhqosBehaviorFlowQueueName,
       "hwhqosBehaviorFlowMappingName": hwhqosBehaviorFlowMappingName,
       "hwhqosBehaviorGroupName": hwhqosBehaviorGroupName,
       "hwhqosBehaviorServiceTemplateName": hwhqosBehaviorServiceTemplateName,
       "hwhqosBehaviorUserQueueRowStatus": hwhqosBehaviorUserQueueRowStatus,
       "hwhqosBandwidthTable": hwhqosBandwidthTable,
       "hwhqosBandwidthEntry": hwhqosBandwidthEntry,
       "hwhqosBandwidthInterfaceIndex": hwhqosBandwidthInterfaceIndex,
       "hwhqosBandwidthValue": hwhqosBandwidthValue,
       "hwhqosBandwidthRowStatus": hwhqosBandwidthRowStatus,
       "hwhqosServiceTemplateTable": hwhqosServiceTemplateTable,
       "hwhqosServiceTemplateEntry": hwhqosServiceTemplateEntry,
       "hwhqosServiceTemplateName": hwhqosServiceTemplateName,
       "hwhqosSlotNumber": hwhqosSlotNumber,
       "hwhqosServiceTemplateRowStatus": hwhqosServiceTemplateRowStatus,
       "hwhqosNetworkHeaderLengthTable": hwhqosNetworkHeaderLengthTable,
       "hwhqosNetworkHeaderLengthEntry": hwhqosNetworkHeaderLengthEntry,
       "hwhqosNetworkHeaderLengthDirection": hwhqosNetworkHeaderLengthDirection,
       "hwhqosNetWorkHeaderLengthValue": hwhqosNetWorkHeaderLengthValue,
       "hwhqosNetWorkHeaderLengthRowStatus": hwhqosNetWorkHeaderLengthRowStatus,
       "hwhqosServiceTemplateApplyTable": hwhqosServiceTemplateApplyTable,
       "hwhqosServiceTemplateApplyEntry": hwhqosServiceTemplateApplyEntry,
       "hwhqosServiceTemplateApplyInterfaceIndex": hwhqosServiceTemplateApplyInterfaceIndex,
       "hwhqosApplyServiceTemplateName": hwhqosApplyServiceTemplateName,
       "hwhqosServiceTemplateApplyRowStatus": hwhqosServiceTemplateApplyRowStatus,
       "hwhqosProfileUserQueueStatisticsTable": hwhqosProfileUserQueueStatisticsTable,
       "hwhqosProfileUserQueueStatisticsEntry": hwhqosProfileUserQueueStatisticsEntry,
       "hwhqosProfileUserQueueStatisticsInterfaceIndex": hwhqosProfileUserQueueStatisticsInterfaceIndex,
       "hwhqosProfileUserQueueStatisticsDirection": hwhqosProfileUserQueueStatisticsDirection,
       "hwhqosProfileUserQueueStatisticsPevid": hwhqosProfileUserQueueStatisticsPevid,
       "hwhqosProfileUserQueueStatisticsCevid": hwhqosProfileUserQueueStatisticsCevid,
       "hwhqosProfileUserQueueStatisticsSlotNumber": hwhqosProfileUserQueueStatisticsSlotNumber,
       "hwhqosProfileUserQueueStatisticsQueueIndex": hwhqosProfileUserQueueStatisticsQueueIndex,
       "hwhqosProfileUserQueueStatisticsReset": hwhqosProfileUserQueueStatisticsReset,
       "hwhqosProfileUserQueueStatisticsPassPackets": hwhqosProfileUserQueueStatisticsPassPackets,
       "hwhqosProfileUserQueueStatisticsPassBytes": hwhqosProfileUserQueueStatisticsPassBytes,
       "hwhqosProfileUserQueueStatisticsDropPackets": hwhqosProfileUserQueueStatisticsDropPackets,
       "hwhqosProfileUserQueueStatisticsDropBytes": hwhqosProfileUserQueueStatisticsDropBytes,
       "hwhqosProfileUserQueueStatisticsPassPacketsRate": hwhqosProfileUserQueueStatisticsPassPacketsRate,
       "hwhqosProfileUserQueueStatisticsPassBytesRate": hwhqosProfileUserQueueStatisticsPassBytesRate,
       "hwhqosProfileUserQueueStatisticsDropPacketsRate": hwhqosProfileUserQueueStatisticsDropPacketsRate,
       "hwhqosProfileUserQueueStatisticsDropBytesRate": hwhqosProfileUserQueueStatisticsDropBytesRate,
       "hwhqosProfileUserQueueStatisticsTrafficTowardsThisInterface": hwhqosProfileUserQueueStatisticsTrafficTowardsThisInterface,
       "hwhqosProfileUserQueueStatisticsConfiguredCir": hwhqosProfileUserQueueStatisticsConfiguredCir,
       "hwhqosProfileUserQueueStatisticsConfiguredPir": hwhqosProfileUserQueueStatisticsConfiguredPir,
       "hwhqosProfileCarStatisticsTable": hwhqosProfileCarStatisticsTable,
       "hwhqosProfileCarStatisticsEntry": hwhqosProfileCarStatisticsEntry,
       "hwhqosProfileCarStatisticsInterfaceIndex": hwhqosProfileCarStatisticsInterfaceIndex,
       "hwhqosProfileCarStatisticsDirection": hwhqosProfileCarStatisticsDirection,
       "hwhqosProfileCarStatisticsPevid": hwhqosProfileCarStatisticsPevid,
       "hwhqosProfileCarStatisticsCevid": hwhqosProfileCarStatisticsCevid,
       "hwhqosProfileCarStatisticsType": hwhqosProfileCarStatisticsType,
       "hwhqosProfileCarStatisticsSlotNumber": hwhqosProfileCarStatisticsSlotNumber,
       "hwhqosProfileCarStatisticsReset": hwhqosProfileCarStatisticsReset,
       "hwhqosProfileCarStatisticsPassPackets": hwhqosProfileCarStatisticsPassPackets,
       "hwhqosProfileCarStatisticsPassBytes": hwhqosProfileCarStatisticsPassBytes,
       "hwhqosProfileCarStatisticsDropPackets": hwhqosProfileCarStatisticsDropPackets,
       "hwhqosProfileCarStatisticsDropBytes": hwhqosProfileCarStatisticsDropBytes,
       "hwhqosProfileCarStatisticsPassPacketsRate": hwhqosProfileCarStatisticsPassPacketsRate,
       "hwhqosProfileCarStatisticsPassBytesRate": hwhqosProfileCarStatisticsPassBytesRate,
       "hwhqosProfileCarStatisticsDropPacketsRate": hwhqosProfileCarStatisticsDropPacketsRate,
       "hwhqosProfileCarStatisticsDropBytesRate": hwhqosProfileCarStatisticsDropBytesRate,
       "hwhqosUserQueueStatisticsTable": hwhqosUserQueueStatisticsTable,
       "hwhqosUserQueueStatisticsEntry": hwhqosUserQueueStatisticsEntry,
       "hwhqosUserQueueStatisticsInterfaceIndex": hwhqosUserQueueStatisticsInterfaceIndex,
       "hwhqosUserQueueStatisticsDirection": hwhqosUserQueueStatisticsDirection,
       "hwhqosUserQueueStatisticsSlotNumber": hwhqosUserQueueStatisticsSlotNumber,
       "hwhqosUserQueueStatisticsQueueIndex": hwhqosUserQueueStatisticsQueueIndex,
       "hwhqosUserQueueStatisticsReset": hwhqosUserQueueStatisticsReset,
       "hwhqosUserQueueStatisticsPassPackets": hwhqosUserQueueStatisticsPassPackets,
       "hwhqosUserQueueStatisticsPassBytes": hwhqosUserQueueStatisticsPassBytes,
       "hwhqosUserQueueStatisticsDropPackets": hwhqosUserQueueStatisticsDropPackets,
       "hwhqosUserQueueStatisticsDropBytes": hwhqosUserQueueStatisticsDropBytes,
       "hwhqosUserQueueStatisticsPassPacketsRate": hwhqosUserQueueStatisticsPassPacketsRate,
       "hwhqosUserQueueStatisticsPassBytesRate": hwhqosUserQueueStatisticsPassBytesRate,
       "hwhqosUserQueueStatisticsDropPacketsRate": hwhqosUserQueueStatisticsDropPacketsRate,
       "hwhqosUserQueueStatisticsDropBytesRate": hwhqosUserQueueStatisticsDropBytesRate,
       "hwhqosUserQueueClassifierStatisticsTable": hwhqosUserQueueClassifierStatisticsTable,
       "hwhqosUserQueueClassifierStatisticsEntry": hwhqosUserQueueClassifierStatisticsEntry,
       "hwhqosUserQueueClassifierStatisticsInterfaceIndex": hwhqosUserQueueClassifierStatisticsInterfaceIndex,
       "hwhqosUserQueueClassifierStatisticsDirection": hwhqosUserQueueClassifierStatisticsDirection,
       "hwhqosUserQueueClassifierStatisticsClassifierName": hwhqosUserQueueClassifierStatisticsClassifierName,
       "hwhqosUserQueueClassifierStatisticsSlotNumber": hwhqosUserQueueClassifierStatisticsSlotNumber,
       "hwhqosUserQueueClassifierStatisticsQueueIndex": hwhqosUserQueueClassifierStatisticsQueueIndex,
       "hwhqosUserQueueClassifierStatisticsReset": hwhqosUserQueueClassifierStatisticsReset,
       "hwhqosUserQueueClassifierStatisticsPassPackets": hwhqosUserQueueClassifierStatisticsPassPackets,
       "hwhqosUserQueueClassifierStatisticsPassBytes": hwhqosUserQueueClassifierStatisticsPassBytes,
       "hwhqosUserQueueClassifierStatisticsDropPackets": hwhqosUserQueueClassifierStatisticsDropPackets,
       "hwhqosUserQueueClassifierStatisticsDropBytes": hwhqosUserQueueClassifierStatisticsDropBytes,
       "hwhqosUserQueueClassifierStatisticsPassPacketsRate": hwhqosUserQueueClassifierStatisticsPassPacketsRate,
       "hwhqosUserQueueClassifierStatisticsPassBytesRate": hwhqosUserQueueClassifierStatisticsPassBytesRate,
       "hwhqosUserQueueClassifierStatisticsDropPacketsRate": hwhqosUserQueueClassifierStatisticsDropPacketsRate,
       "hwhqosUserQueueClassifierStatisticsDropBytesRate": hwhqosUserQueueClassifierStatisticsDropBytesRate,
       "hwhqosUserGroupQueueStatisticsTable": hwhqosUserGroupQueueStatisticsTable,
       "hwhqosUserGroupQueueStatisticsEntry": hwhqosUserGroupQueueStatisticsEntry,
       "hwhqosUserGroupQueueStatisticsGroupName": hwhqosUserGroupQueueStatisticsGroupName,
       "hwhqosUserGroupQueueStatisticsDirection": hwhqosUserGroupQueueStatisticsDirection,
       "hwhqosUserGroupQueueStatisticsSlotNumber": hwhqosUserGroupQueueStatisticsSlotNumber,
       "hwhqosUserGroupQueueStatisticsQueueIndex": hwhqosUserGroupQueueStatisticsQueueIndex,
       "hwhqosUserGroupQueueStatisticsReset": hwhqosUserGroupQueueStatisticsReset,
       "hwhqosUserGroupQueueStatisticsPassPackets": hwhqosUserGroupQueueStatisticsPassPackets,
       "hwhqosUserGroupQueueStatisticsPassBytes": hwhqosUserGroupQueueStatisticsPassBytes,
       "hwhqosUserGroupQueueStatisticsDropPackets": hwhqosUserGroupQueueStatisticsDropPackets,
       "hwhqosUserGroupQueueStatisticsDropBytes": hwhqosUserGroupQueueStatisticsDropBytes,
       "hwhqosUserGroupQueueStatisticsPassPacketsRate": hwhqosUserGroupQueueStatisticsPassPacketsRate,
       "hwhqosUserGroupQueueStatisticsPassBytesRate": hwhqosUserGroupQueueStatisticsPassBytesRate,
       "hwhqosUserGroupQueueStatisticsDropPacketsRate": hwhqosUserGroupQueueStatisticsDropPacketsRate,
       "hwhqosUserGroupQueueStatisticsDropBytesRate": hwhqosUserGroupQueueStatisticsDropBytesRate,
       "hwhqosFlowQueueShaperTable": hwhqosFlowQueueShaperTable,
       "hwhqosFlowQueueShaperEntry": hwhqosFlowQueueShaperEntry,
       "hwhqosFlowQueueShaperBE": hwhqosFlowQueueShaperBE,
       "hwhqosFlowQueueShaperAF1": hwhqosFlowQueueShaperAF1,
       "hwhqosFlowQueueShaperAF2": hwhqosFlowQueueShaperAF2,
       "hwhqosFlowQueueShaperAF3": hwhqosFlowQueueShaperAF3,
       "hwhqosFlowQueueShaperAF4": hwhqosFlowQueueShaperAF4,
       "hwhqosFlowQueueShaperEF": hwhqosFlowQueueShaperEF,
       "hwhqosFlowQueueShaperCS6": hwhqosFlowQueueShaperCS6,
       "hwhqosFlowQueueShaperCS7": hwhqosFlowQueueShaperCS7,
       "hwhqosFlowQueueShaperValue": hwhqosFlowQueueShaperValue,
       "hwhqosFlowQueueShaperRowStatus": hwhqosFlowQueueShaperRowStatus,
       "hwhqosWredQueueDepthTable": hwhqosWredQueueDepthTable,
       "hwhqosWredQueueDepthEntry": hwhqosWredQueueDepthEntry,
       "hwhqosWredQueueDepthType": hwhqosWredQueueDepthType,
       "hwhqosWredQueueDepthWredName": hwhqosWredQueueDepthWredName,
       "hwhqosWredQueueDepthValue": hwhqosWredQueueDepthValue,
       "hwhqosWredQueueDepthRowStatus": hwhqosWredQueueDepthRowStatus,
       "hwhqosBandwidthCheckTable": hwhqosBandwidthCheckTable,
       "hwhqosBandwidthCheckEntry": hwhqosBandwidthCheckEntry,
       "hwhqosBandwidthCheckInterfaceIndex": hwhqosBandwidthCheckInterfaceIndex,
       "hwhqosBandwidthCheckDirection": hwhqosBandwidthCheckDirection,
       "hwhqosBandwidthCheckValue": hwhqosBandwidthCheckValue,
       "hwhqosBandwidthCheckRowStatus": hwhqosBandwidthCheckRowStatus,
       "hwhqosServiceIdentifyPolicyTable": hwhqosServiceIdentifyPolicyTable,
       "hwhqosServiceIdentifyPolicyEntry": hwhqosServiceIdentifyPolicyEntry,
       "hwhqosServiceIdentifyPolicyName": hwhqosServiceIdentifyPolicyName,
       "hwhqosServiceIdentifyPolicyRowStatus": hwhqosServiceIdentifyPolicyRowStatus,
       "hwhqosServiceIdentifyPolicyApplyTable": hwhqosServiceIdentifyPolicyApplyTable,
       "hwhqosServiceIdentifyPolicyApplyEntry": hwhqosServiceIdentifyPolicyApplyEntry,
       "hwhqosServiceIdentifyPolicyApplyInterfaceIndex": hwhqosServiceIdentifyPolicyApplyInterfaceIndex,
       "hwhqosServiceIdentifyPolicyApplyName": hwhqosServiceIdentifyPolicyApplyName,
       "hwhqosServiceIdentifyPolicyApplyRowStatus": hwhqosServiceIdentifyPolicyApplyRowStatus,
       "hwhqosServiceIdentifyPolicyTypeTable": hwhqosServiceIdentifyPolicyTypeTable,
       "hwhqosServiceIdentifyPolicyTypeEntry": hwhqosServiceIdentifyPolicyTypeEntry,
       "hwhqosServiceIdentifyPolicyTypeValue": hwhqosServiceIdentifyPolicyTypeValue,
       "hwhqosServiceIdentifyPolicyTypeRowStatus": hwhqosServiceIdentifyPolicyTypeRowStatus,
       "hwhqosServiceIdentifyPolicyVlanTable": hwhqosServiceIdentifyPolicyVlanTable,
       "hwhqosServiceIdentifyPolicyVlanEntry": hwhqosServiceIdentifyPolicyVlanEntry,
       "hwhqosServiceIdentifyPolicyVlanID": hwhqosServiceIdentifyPolicyVlanID,
       "hwhqosServiceIdentifyPolicyVlanDomainName": hwhqosServiceIdentifyPolicyVlanDomainName,
       "hwhqosServiceIdentifyPolicyVlanRowStatus": hwhqosServiceIdentifyPolicyVlanRowStatus,
       "hwhqosServiceIdentifyPolicy8021pTable": hwhqosServiceIdentifyPolicy8021pTable,
       "hwhqosServiceIdentifyPolicy8021pEntry": hwhqosServiceIdentifyPolicy8021pEntry,
       "hwhqosServiceIdentifyPolicy8021pCosID": hwhqosServiceIdentifyPolicy8021pCosID,
       "hwhqosServiceIdentifyPolicy8021pDomainName": hwhqosServiceIdentifyPolicy8021pDomainName,
       "hwhqosServiceIdentifyPolicy8021pRowStatus": hwhqosServiceIdentifyPolicy8021pRowStatus,
       "hwhqosServiceIdentifyPolicyDscpTable": hwhqosServiceIdentifyPolicyDscpTable,
       "hwhqosServiceIdentifyPolicyDscpEntry": hwhqosServiceIdentifyPolicyDscpEntry,
       "hwhqosServiceIdentifyPolicyDscpID": hwhqosServiceIdentifyPolicyDscpID,
       "hwhqosServiceIdentifyPolicyDscpDomainName": hwhqosServiceIdentifyPolicyDscpDomainName,
       "hwhqosServiceIdentifyPolicyDscpRowStatus": hwhqosServiceIdentifyPolicyDscpRowStatus,
       "hwhqosServiceIdentifyPolicyOption60Table": hwhqosServiceIdentifyPolicyOption60Table,
       "hwhqosServiceIdentifyPolicyOption60Entry": hwhqosServiceIdentifyPolicyOption60Entry,
       "hwhqosServiceIdentifyPolicyOption60": hwhqosServiceIdentifyPolicyOption60,
       "hwhqosServiceIdentifyPolicyOption60RowStatus": hwhqosServiceIdentifyPolicyOption60RowStatus,
       "hwhqosDomainRateLimitModeTable": hwhqosDomainRateLimitModeTable,
       "hwhqosDomainRateLimitModeEntry": hwhqosDomainRateLimitModeEntry,
       "hwhqosDomainRateLimitModeDomainName": hwhqosDomainRateLimitModeDomainName,
       "hwhqosDomainRateLimitModeDirection": hwhqosDomainRateLimitModeDirection,
       "hwhqosDomainRateLimitModeRateLimitMode": hwhqosDomainRateLimitModeRateLimitMode,
       "hwhqosDomainRateLimitModeRowStatus": hwhqosDomainRateLimitModeRowStatus,
       "hwhqosDomainSessionGroupExcludeTable": hwhqosDomainSessionGroupExcludeTable,
       "hwhqosDomainSessionGroupExcludeEntry": hwhqosDomainSessionGroupExcludeEntry,
       "hwhqosDomainSessionGroupExcludeDomainName": hwhqosDomainSessionGroupExcludeDomainName,
       "hwhqosDomainSessionGroupExcludeDirection": hwhqosDomainSessionGroupExcludeDirection,
       "hwhqosDomainSessionGroupExcludeMode": hwhqosDomainSessionGroupExcludeMode,
       "hwhqosDomainSessionGroupExcludeRowStatus": hwhqosDomainSessionGroupExcludeRowStatus,
       "hwhqosDomainUserMaxSessionTable": hwhqosDomainUserMaxSessionTable,
       "hwhqosDomainUserMaxSessionEntry": hwhqosDomainUserMaxSessionEntry,
       "hwhqosDomainUserMaxSessionDomainName": hwhqosDomainUserMaxSessionDomainName,
       "hwhqosDomainUserMaxSessionNum": hwhqosDomainUserMaxSessionNum,
       "hwhqosDomainUserMaxSessionRowStatus": hwhqosDomainUserMaxSessionRowStatus,
       "hwhqosUpdateUseridProfileTable": hwhqosUpdateUseridProfileTable,
       "hwhqosUpdateUseridProfileEntry": hwhqosUpdateUseridProfileEntry,
       "hwhqosUpdateUseridProfileUserid": hwhqosUpdateUseridProfileUserid,
       "hwhqosUpdateUseridProfileDirection": hwhqosUpdateUseridProfileDirection,
       "hwhqosUpdateUseridProfileName": hwhqosUpdateUseridProfileName,
       "hwhqosUpdateUseridProfileRowStatus": hwhqosUpdateUseridProfileRowStatus,
       "hwhqosDomainUserPriorityTable": hwhqosDomainUserPriorityTable,
       "hwhqosDomainUserPriorityEntry": hwhqosDomainUserPriorityEntry,
       "hwhqosDomainUserPriorityDomainName": hwhqosDomainUserPriorityDomainName,
       "hwhqosDomainUserPriorityDirection": hwhqosDomainUserPriorityDirection,
       "hwhqosDomainUserPriorityValue": hwhqosDomainUserPriorityValue,
       "hwhqosDomainUserPriorityRowStatus": hwhqosDomainUserPriorityRowStatus,
       "hwhqosTMScheduleModeTable": hwhqosTMScheduleModeTable,
       "hwhqosTMScheduleModeEntry": hwhqosTMScheduleModeEntry,
       "hwhqosTMScheduleModeSlot": hwhqosTMScheduleModeSlot,
       "hwhqosTMScheduleModeSimpleEnable": hwhqosTMScheduleModeSimpleEnable,
       "hwhqosTMScheduleModeRowStatus": hwhqosTMScheduleModeRowStatus,
       "hwhqosUserBandwidthTable": hwhqosUserBandwidthTable,
       "hwhqosUserBandwidthEntry": hwhqosUserBandwidthEntry,
       "hwhqosUserBandwidthUserid": hwhqosUserBandwidthUserid,
       "hwhqosUserBandwidthCir": hwhqosUserBandwidthCir,
       "hwhqosUserBandwidthPir": hwhqosUserBandwidthPir,
       "hwhqosUserBandwidthCommittedCir": hwhqosUserBandwidthCommittedCir,
       "hwhqosUserBandwidthRowStatus": hwhqosUserBandwidthRowStatus,
       "hwhqosUseridStatTable": hwhqosUseridStatTable,
       "hwhqosUseridStatEntry": hwhqosUseridStatEntry,
       "hwhqosUseridStatUserid": hwhqosUseridStatUserid,
       "hwhqosUseridStatQueue": hwhqosUseridStatQueue,
       "hwhqosUseridStatDirection": hwhqosUseridStatDirection,
       "hwhqosUseridStatPassBytes": hwhqosUseridStatPassBytes,
       "hwhqosUseridStatDropBytes": hwhqosUseridStatDropBytes,
       "hwhqosUseridStatPassPackets": hwhqosUseridStatPassPackets,
       "hwhqosUseridStatDropPackets": hwhqosUseridStatDropPackets,
       "hwhqosUseridStatPassPacketsRate": hwhqosUseridStatPassPacketsRate,
       "hwhqosUseridStatDropPacketsRate": hwhqosUseridStatDropPacketsRate,
       "hwhqosUseridStatReset": hwhqosUseridStatReset,
       "hwhqosUseridStatPassBytesRate": hwhqosUseridStatPassBytesRate,
       "hwhqosUseridStatDropBytesRate": hwhqosUseridStatDropBytesRate,
       "hwhqosFatherUserGroupQueueApplyTable": hwhqosFatherUserGroupQueueApplyTable,
       "hwhqosFatherUserGroupQueueApplyEntry": hwhqosFatherUserGroupQueueApplyEntry,
       "hwhqosFatherUserGroupQueueApplyInterfaceIndex": hwhqosFatherUserGroupQueueApplyInterfaceIndex,
       "hwhqosFatherUserGroupQueueApplyDirection": hwhqosFatherUserGroupQueueApplyDirection,
       "hwhqosFatherUserGroupQueueApplyName": hwhqosFatherUserGroupQueueApplyName,
       "hwhqosFatherUserGroupQueueApplyRowStatus": hwhqosFatherUserGroupQueueApplyRowStatus,
       "hwhqosUserGroupQueueApplyTable": hwhqosUserGroupQueueApplyTable,
       "hwhqosUserGroupQueueApplyEntry": hwhqosUserGroupQueueApplyEntry,
       "hwhqosUserGroupQueueApplyInterfaceIndex": hwhqosUserGroupQueueApplyInterfaceIndex,
       "hwhqosUserGroupQueueApplyPeVid": hwhqosUserGroupQueueApplyPeVid,
       "hwhqosUserGroupQueueApplyCeVid": hwhqosUserGroupQueueApplyCeVid,
       "hwhqosUserGroupQueueApplyDirection": hwhqosUserGroupQueueApplyDirection,
       "hwhqosUserGroupQueueApplyName": hwhqosUserGroupQueueApplyName,
       "hwhqosUserGroupQueueApplyEachvlan": hwhqosUserGroupQueueApplyEachvlan,
       "hwhqosUserGroupQueueApplyRowStatus": hwhqosUserGroupQueueApplyRowStatus,
       "hwhqosProfileApplyDomainTable": hwhqosProfileApplyDomainTable,
       "hwhqosProfileApplyDomainEntry": hwhqosProfileApplyDomainEntry,
       "hwhqosProfileApplyDomainName": hwhqosProfileApplyDomainName,
       "hwhqosProfileApplyDomainDirection": hwhqosProfileApplyDomainDirection,
       "hwhqosProfileApplyDomainProfileName": hwhqosProfileApplyDomainProfileName,
       "hwhqosProfileApplyDomainRowStatus": hwhqosProfileApplyDomainRowStatus,
       "hwhqosProfileApplyUserVlanTable": hwhqosProfileApplyUserVlanTable,
       "hwhqosProfileApplyUserVlanEntry": hwhqosProfileApplyUserVlanEntry,
       "hwhqosProfileApplyUserVlanInterfaceIndex": hwhqosProfileApplyUserVlanInterfaceIndex,
       "hwhqosProfileApplyUserVlanPeVid": hwhqosProfileApplyUserVlanPeVid,
       "hwhqosProfileApplyUserVlanCeVid": hwhqosProfileApplyUserVlanCeVid,
       "hwhqosProfileApplyUserVlanDirection": hwhqosProfileApplyUserVlanDirection,
       "hwhqosProfileApplyUserVlanProfileName": hwhqosProfileApplyUserVlanProfileName,
       "hwhqosProfileApplyUserVlanEach": hwhqosProfileApplyUserVlanEach,
       "hwhqosProfileApplyUserVlanRowStatus": hwhqosProfileApplyUserVlanRowStatus,
       "hwhqosLinkAdjRemoteEnableTable": hwhqosLinkAdjRemoteEnableTable,
       "hwhqosLinkAdjRemoteEnableEntry": hwhqosLinkAdjRemoteEnableEntry,
       "hwhqosLinkAdjRemoteEnableType": hwhqosLinkAdjRemoteEnableType,
       "hwhqosLinkAdjRemoteEnableSlot": hwhqosLinkAdjRemoteEnableSlot,
       "hwhqosLinkAdjRemoteEnableDomainName": hwhqosLinkAdjRemoteEnableDomainName,
       "hwhqosLinkAdjRemoteEnable": hwhqosLinkAdjRemoteEnable,
       "hwhqosLinkAdjRemoteEnableRowStatus": hwhqosLinkAdjRemoteEnableRowStatus,
       "hwhqosLinkAdjShapingModeTable": hwhqosLinkAdjShapingModeTable,
       "hwhqosLinkAdjShapingModeEntry": hwhqosLinkAdjShapingModeEntry,
       "hwhqosLinkAdjShapingModeType": hwhqosLinkAdjShapingModeType,
       "hwhqosLinkAdjShapingModeInterfaceIndex": hwhqosLinkAdjShapingModeInterfaceIndex,
       "hwhqosLinkAdjShapingModeDomainName": hwhqosLinkAdjShapingModeDomainName,
       "hwhqosLinkAdjShapingMode": hwhqosLinkAdjShapingMode,
       "hwhqosLinkAdjShapingModeRowStatus": hwhqosLinkAdjShapingModeRowStatus,
       "hwhqosLinkAdjRemoteTable": hwhqosLinkAdjRemoteTable,
       "hwhqosLinkAdjRemoteEntry": hwhqosLinkAdjRemoteEntry,
       "hwhqosLinkAdjRemoteType": hwhqosLinkAdjRemoteType,
       "hwhqosLinkAdjRemoteInterfaceIndex": hwhqosLinkAdjRemoteInterfaceIndex,
       "hwhqosLinkAdjRemoteDomainName": hwhqosLinkAdjRemoteDomainName,
       "hwhqosLinkAdjRemoteValue": hwhqosLinkAdjRemoteValue,
       "hwhqosLinkAdjRemoteRowStatus": hwhqosLinkAdjRemoteRowStatus,
       "hwhqosLinkAdjLocalTable": hwhqosLinkAdjLocalTable,
       "hwhqosLinkAdjLocalEntry": hwhqosLinkAdjLocalEntry,
       "hwhqosLinkAdjLocalSlotNumber": hwhqosLinkAdjLocalSlotNumber,
       "hwhqosLinkAdjLocalValue": hwhqosLinkAdjLocalValue,
       "hwhqosLinkAdjLocalRowStatus": hwhqosLinkAdjLocalRowStatus,
       "hwhqosLinkAdjExcludeTable": hwhqosLinkAdjExcludeTable,
       "hwhqosLinkAdjExcludeEntry": hwhqosLinkAdjExcludeEntry,
       "hwhqosLinkAdjExcludeSlotNumber": hwhqosLinkAdjExcludeSlotNumber,
       "hwhqosLinkAdjExcludeEnable": hwhqosLinkAdjExcludeEnable,
       "hwhqosLinkAdjExcludeRowStatus": hwhqosLinkAdjExcludeRowStatus,
       "hwhqosProfileInfoTable": hwhqosProfileInfoTable,
       "hwhqosProfileInfoEntry": hwhqosProfileInfoEntry,
       "hwhqosProfileInfoName": hwhqosProfileInfoName,
       "hwhqosProfileInfoDescription": hwhqosProfileInfoDescription,
       "hwhqosProfileInfoRowStatus": hwhqosProfileInfoRowStatus,
       "hwhqosUserGroupQueueTemplateTable": hwhqosUserGroupQueueTemplateTable,
       "hwhqosUserGroupQueueTemplateEntry": hwhqosUserGroupQueueTemplateEntry,
       "hwhqosUserGroupQueueTemplateName": hwhqosUserGroupQueueTemplateName,
       "hwhqosUserGroupQueueTemplateModeTemplate": hwhqosUserGroupQueueTemplateModeTemplate,
       "hwhqosUserGroupQueueTemplateRowStatus": hwhqosUserGroupQueueTemplateRowStatus,
       "hwhqosProfileWeightTable": hwhqosProfileWeightTable,
       "hwhqosProfileWeightEntry": hwhqosProfileWeightEntry,
       "hwhqosProfileWeightDirection": hwhqosProfileWeightDirection,
       "hwhqosProfileWeightValue": hwhqosProfileWeightValue,
       "hwhqosProfileWeightRowStatus": hwhqosProfileWeightRowStatus,
       "hwhqosUserQueueApplyAlarmTable": hwhqosUserQueueApplyAlarmTable,
       "hwhqosUserQueueApplyAlarmEntry": hwhqosUserQueueApplyAlarmEntry,
       "hwhqosUserQueueApplyAlarmIfNetName": hwhqosUserQueueApplyAlarmIfNetName,
       "hwhqosPortQueueStatDiscardAlarmTrapTable": hwhqosPortQueueStatDiscardAlarmTrapTable,
       "hwhqosPortQueueStatDiscardAlarmTrapEntry": hwhqosPortQueueStatDiscardAlarmTrapEntry,
       "hwhqosPortQueueInterfaceTrap": hwhqosPortQueueInterfaceTrap,
       "hwhqosPortQueueCosValueTrap": hwhqosPortQueueCosValueTrap,
       "hwhqosPortQueueDiscardTypeTrap": hwhqosPortQueueDiscardTypeTrap,
       "hwhqosPortQueueDiscardValueTrap": hwhqosPortQueueDiscardValueTrap,
       "hwhqosPortQueueStatDiscardAlarmCancelTable": hwhqosPortQueueStatDiscardAlarmCancelTable,
       "hwhqosPortQueueStatDiscardAlarmCancelEntry": hwhqosPortQueueStatDiscardAlarmCancelEntry,
       "hwhqosPortQueueInterfaceCancel": hwhqosPortQueueInterfaceCancel,
       "hwhqosPortQueueCosValueCancel": hwhqosPortQueueCosValueCancel,
       "hwhqosPortQueueDiscardTypeCancel": hwhqosPortQueueDiscardTypeCancel,
       "hwhqosPortQueueDiscardValueCancel": hwhqosPortQueueDiscardValueCancel,
       "hwhqosIfUserQueueTable": hwhqosIfUserQueueTable,
       "hwhqosIfUserQueueEntry": hwhqosIfUserQueueEntry,
       "hwhqosIfUserQueueIfIndex": hwhqosIfUserQueueIfIndex,
       "hwhqosIfUserQueueAclType": hwhqosIfUserQueueAclType,
       "hwhqosIfUserQueueAclID1": hwhqosIfUserQueueAclID1,
       "hwhqosIfUserQueueAclID2": hwhqosIfUserQueueAclID2,
       "hwhqosIfUserQueuePir": hwhqosIfUserQueuePir,
       "hwhqosIfUserQueueFlowQueueProfileName": hwhqosIfUserQueueFlowQueueProfileName,
       "hwhqosIfUserQueueFlowMappingProfileName": hwhqosIfUserQueueFlowMappingProfileName,
       "hwhqosIfUserQueueRowStatus": hwhqosIfUserQueueRowStatus,
       "hwhqosIfUserQueueStatisticsTable": hwhqosIfUserQueueStatisticsTable,
       "hwhqosIfUserQueueStatisticsEntry": hwhqosIfUserQueueStatisticsEntry,
       "hwhqosIfUserQueueStatisticsIfIndex": hwhqosIfUserQueueStatisticsIfIndex,
       "hwhqosIfUserQueueStatisticsAclType": hwhqosIfUserQueueStatisticsAclType,
       "hwhqosIfUserQueueStatisticsAclID1": hwhqosIfUserQueueStatisticsAclID1,
       "hwhqosIfUserQueueStatisticsAclID2": hwhqosIfUserQueueStatisticsAclID2,
       "hwhqosIfUserQueueStatisticsQueueIndex": hwhqosIfUserQueueStatisticsQueueIndex,
       "hwhqosIfUserQueueStatisticsQueuePassPackets": hwhqosIfUserQueueStatisticsQueuePassPackets,
       "hwhqosIfUserQueueStatisticsQueuePassBytes": hwhqosIfUserQueueStatisticsQueuePassBytes,
       "hwhqosIfUserQueueStatisticsQueueDropPackets": hwhqosIfUserQueueStatisticsQueueDropPackets,
       "hwhqosIfUserQueueStatisticsQueueDropBytes": hwhqosIfUserQueueStatisticsQueueDropBytes,
       "hwhqosIfUserQueueStatisticsReset": hwhqosIfUserQueueStatisticsReset,
       "hwhqosUserQueueShapeAllTrafficTable": hwhqosUserQueueShapeAllTrafficTable,
       "hwhqosUserQueueShapeAllTrafficEntry": hwhqosUserQueueShapeAllTrafficEntry,
       "hwhqosUserQueueShapeAllTrafficInterfaceIndex": hwhqosUserQueueShapeAllTrafficInterfaceIndex,
       "hwhqosUserQueueShapeAllTrafficRowStatus": hwhqosUserQueueShapeAllTrafficRowStatus,
       "hwhqosUserGroupQueueInterfaceStatisticsTable": hwhqosUserGroupQueueInterfaceStatisticsTable,
       "hwhqosUserGroupQueueInterfaceStatisticsEntry": hwhqosUserGroupQueueInterfaceStatisticsEntry,
       "hwhqosUserGroupQueueInterfaceStatisticsIfIndex": hwhqosUserGroupQueueInterfaceStatisticsIfIndex,
       "hwhqosUserGroupQueueInterfaceStatisticsDirection": hwhqosUserGroupQueueInterfaceStatisticsDirection,
       "hwhqosUserGroupQueueInterfaceStatisticsPevid": hwhqosUserGroupQueueInterfaceStatisticsPevid,
       "hwhqosUserGroupQueueInterfaceStatisticsCevid": hwhqosUserGroupQueueInterfaceStatisticsCevid,
       "hwhqosUserGroupQueueInterfaceStatisticsVlanid": hwhqosUserGroupQueueInterfaceStatisticsVlanid,
       "hwhqosUserGroupQueueInterfaceStatisticsQueueIndex": hwhqosUserGroupQueueInterfaceStatisticsQueueIndex,
       "hwhqosUserGroupQueueInterfaceStatisticsReset": hwhqosUserGroupQueueInterfaceStatisticsReset,
       "hwhqosUserGroupQueueInterfaceStatisticsPassPackets": hwhqosUserGroupQueueInterfaceStatisticsPassPackets,
       "hwhqosUserGroupQueueInterfaceStatisticsPassBytes": hwhqosUserGroupQueueInterfaceStatisticsPassBytes,
       "hwhqosUserGroupQueueInterfaceStatisticsDropPackets": hwhqosUserGroupQueueInterfaceStatisticsDropPackets,
       "hwhqosUserGroupQueueInterfaceStatisticsDropBytes": hwhqosUserGroupQueueInterfaceStatisticsDropBytes,
       "hwhqosUserGroupQueueInterfaceStatisticsPassPacketsRate": hwhqosUserGroupQueueInterfaceStatisticsPassPacketsRate,
       "hwhqosUserGroupQueueInterfaceStatisticsPassBytesRate": hwhqosUserGroupQueueInterfaceStatisticsPassBytesRate,
       "hwhqosUserGroupQueueInterfaceStatisticsDropPacketsRate": hwhqosUserGroupQueueInterfaceStatisticsDropPacketsRate,
       "hwhqosUserGroupQueueInterfaceStatisticsDropBytesRate": hwhqosUserGroupQueueInterfaceStatisticsDropBytesRate,
       "hwhqosObjects": hwhqosObjects,
       "hwhqosUserFrameId": hwhqosUserFrameId,
       "hwhqosUserSlotId": hwhqosUserSlotId,
       "hwhqosUserPortId": hwhqosUserPortId,
       "hwhqosUserQueueApplyFailDirection": hwhqosUserQueueApplyFailDirection,
       "hwhqosTraps": hwhqosTraps,
       "hwhqosUserQueueStatDiscardAlarmTrap": hwhqosUserQueueStatDiscardAlarmTrap,
       "hwhqosUserQueueApplyPirFailAlarmTrap": hwhqosUserQueueApplyPirFailAlarmTrap,
       "hwhqosUserQueueApplyPirSucessAlarmTrap": hwhqosUserQueueApplyPirSucessAlarmTrap,
       "hwhqosUserQueueApplyAlarmTrap": hwhqosUserQueueApplyAlarmTrap,
       "hwhqosPortQueueStatDiscardAlarmTrap": hwhqosPortQueueStatDiscardAlarmTrap,
       "hwhqosPortQueueStatDiscardAlarmCancelTrap": hwhqosPortQueueStatDiscardAlarmCancelTrap,
       "hwhqosConformance": hwhqosConformance,
       "hwhqosCompliances": hwhqosCompliances,
       "hwhqosUserQueueStatCompliances": hwhqosUserQueueStatCompliances,
       "hwhqosGroups": hwhqosGroups,
       "hwhqosIfStatGroup": hwhqosIfStatGroup,
       "hqhqosAtmPvcStatGroup": hqhqosAtmPvcStatGroup,
       "hwhqosPortQueueGroup": hwhqosPortQueueGroup,
       "hwhqosWredGroup": hwhqosWredGroup,
       "hwhqosIfQueueStatGroup": hwhqosIfQueueStatGroup,
       "hwhqosUserQueueStatGroup": hwhqosUserQueueStatGroup,
       "hwhqosUserGroupQueueStatGroup": hwhqosUserGroupQueueStatGroup,
       "hwhqosObjectsGroup": hwhqosObjectsGroup,
       "hwhqosUserQueueStatTrapGroup": hwhqosUserQueueStatTrapGroup,
       "hwhqosVpnQoSTunnelStatGroup": hwhqosVpnQoSTunnelStatGroup,
       "hwhqosTunnelStatGroup": hwhqosTunnelStatGroup,
       "hwhqosProfileGroup": hwhqosProfileGroup,
       "hwhqosProfileSuppressionGroup": hwhqosProfileSuppressionGroup,
       "hwhqosProfileCarGroup": hwhqosProfileCarGroup,
       "hwhqosProfileUserQueueGroup": hwhqosProfileUserQueueGroup,
       "hwhqosProfileUserApplyGroup": hwhqosProfileUserApplyGroup,
       "hwhqosFlowMappingGroup": hwhqosFlowMappingGroup,
       "hwhqosFlowMappingCfgGroup": hwhqosFlowMappingCfgGroup,
       "hwhqosFlowQueueGroup": hwhqosFlowQueueGroup,
       "hwhqosFlowQueueCfgGroup": hwhqosFlowQueueCfgGroup,
       "hwhqosFlowWredGroup": hwhqosFlowWredGroup,
       "hwhqosFlowWredColorGroup": hwhqosFlowWredColorGroup,
       "hwhqosUserGroupQueueGroup": hwhqosUserGroupQueueGroup,
       "hwhqosUserGroupQueueShapingGroup": hwhqosUserGroupQueueShapingGroup,
       "hwhqosUserQueueGroup": hwhqosUserQueueGroup,
       "hwhqosBehaviorUserQueueGroup": hwhqosBehaviorUserQueueGroup,
       "hwhqosBandwidthGroup": hwhqosBandwidthGroup,
       "hwhqosServiceTemplateGroup": hwhqosServiceTemplateGroup,
       "hwhqosNetworkHeaderLengthGroup": hwhqosNetworkHeaderLengthGroup,
       "hwhqosServiceTemplateApplyGroup": hwhqosServiceTemplateApplyGroup,
       "hwhqosProfileUserQueueStatisticsGroup": hwhqosProfileUserQueueStatisticsGroup,
       "hwhqosProfileCarStatisticsGroup": hwhqosProfileCarStatisticsGroup,
       "hwhqosUserQueueStatisticsGroup": hwhqosUserQueueStatisticsGroup,
       "hwhqosUserQueueClassifierStatisticsGroup": hwhqosUserQueueClassifierStatisticsGroup,
       "hwhqosUserGroupQueueStatisticsGroup": hwhqosUserGroupQueueStatisticsGroup,
       "hwhqosFlowQueueShaperGroup": hwhqosFlowQueueShaperGroup,
       "hwhqosWredQueueDepthGroup": hwhqosWredQueueDepthGroup,
       "hwhqosBandwidthCheck": hwhqosBandwidthCheck,
       "hwhqosServiceIdentifyPolicyGroup": hwhqosServiceIdentifyPolicyGroup,
       "hwhqosServiceIdentifyPolicyApplyGroup": hwhqosServiceIdentifyPolicyApplyGroup,
       "hwhqosServiceIdentifyPolicyTypeGroup": hwhqosServiceIdentifyPolicyTypeGroup,
       "hwhqosServiceIdentifyPolicyVlanGroup": hwhqosServiceIdentifyPolicyVlanGroup,
       "hwhqosServiceIdentifyPolicy8021pGroup": hwhqosServiceIdentifyPolicy8021pGroup,
       "hwhqosServiceIdentifyPolicyDscpGroup": hwhqosServiceIdentifyPolicyDscpGroup,
       "hwhqosServiceIdentifyPolicyOption60Group": hwhqosServiceIdentifyPolicyOption60Group,
       "hwhqosDomainRateLimitModeGroup": hwhqosDomainRateLimitModeGroup,
       "hwhqosDomainSessionGroupExcludeGroup": hwhqosDomainSessionGroupExcludeGroup,
       "hwhqosDomainUserMaxSessionGroup": hwhqosDomainUserMaxSessionGroup,
       "hwhqosUpdateUseridProfileGroup": hwhqosUpdateUseridProfileGroup,
       "hwhqosDomainUserPriorityGroup": hwhqosDomainUserPriorityGroup,
       "hwhqosUseridStatGroup": hwhqosUseridStatGroup,
       "hwhqosFatherUserGroupQueueApplyGroup": hwhqosFatherUserGroupQueueApplyGroup,
       "hwhqosUserGroupQueueApplyGroup": hwhqosUserGroupQueueApplyGroup,
       "hwhqosProfileApplyDomainGroup": hwhqosProfileApplyDomainGroup,
       "hwhqosProfileApplyUserVlanGroup": hwhqosProfileApplyUserVlanGroup,
       "hwhqosLinkAdjRemoteEnableGroup": hwhqosLinkAdjRemoteEnableGroup,
       "hwhqosLinkAdjShapingModeGroup": hwhqosLinkAdjShapingModeGroup,
       "hwhqosLinkAdjRemoteGroup": hwhqosLinkAdjRemoteGroup,
       "hwhqosLinkAdjLocalTableGroup": hwhqosLinkAdjLocalTableGroup,
       "hwhqosLinkAdjExcludeGroup": hwhqosLinkAdjExcludeGroup,
       "hwhqosProfileInfoGroup": hwhqosProfileInfoGroup,
       "hwhqosUserGroupQueueTemplateGroup": hwhqosUserGroupQueueTemplateGroup,
       "hwhqosProfileWeightGroup": hwhqosProfileWeightGroup,
       "hwhqosUserQueueApplyAlarmGroup": hwhqosUserQueueApplyAlarmGroup,
       "hwhqosPortQueueStatDiscardAlarmTrapGroup": hwhqosPortQueueStatDiscardAlarmTrapGroup,
       "hwhqosPortQueueStatDiscarAlarmCancelGroup": hwhqosPortQueueStatDiscarAlarmCancelGroup,
       "hwhqosUserGroupQueueInterfaceStatisticsGroup": hwhqosUserGroupQueueInterfaceStatisticsGroup}
)

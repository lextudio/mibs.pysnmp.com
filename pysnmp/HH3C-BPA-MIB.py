# SNMP MIB module (HH3C-BPA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-BPA-MIB
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cBpa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144)
)
hh3cBpa.setRevisions(
        ("2013-11-13 11:28",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cBpaObjects_ObjectIdentity = ObjectIdentity
hh3cBpaObjects = _Hh3cBpaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1)
)
_Hh3cBpaCfgTable_Object = MibTable
hh3cBpaCfgTable = _Hh3cBpaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cBpaCfgTable.setStatus("current")
_Hh3cBpaCfgEntry_Object = MibTableRow
hh3cBpaCfgEntry = _Hh3cBpaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 1, 1)
)
hh3cBpaCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-BPA-MIB", "hh3cBpaDirection"),
)
if mibBuilder.loadTexts:
    hh3cBpaCfgEntry.setStatus("current")


class _Hh3cBpaDirection_Type(Integer32):
    """Custom type hh3cBpaDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_Hh3cBpaDirection_Type.__name__ = "Integer32"
_Hh3cBpaDirection_Object = MibTableColumn
hh3cBpaDirection = _Hh3cBpaDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 1, 1, 1),
    _Hh3cBpaDirection_Type()
)
hh3cBpaDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBpaDirection.setStatus("current")


class _Hh3cBpaSrcOrDest_Type(Integer32):
    """Custom type hh3cBpaSrcOrDest based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("destination", 2),
          ("source", 1))
    )


_Hh3cBpaSrcOrDest_Type.__name__ = "Integer32"
_Hh3cBpaSrcOrDest_Object = MibTableColumn
hh3cBpaSrcOrDest = _Hh3cBpaSrcOrDest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 1, 1, 2),
    _Hh3cBpaSrcOrDest_Type()
)
hh3cBpaSrcOrDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cBpaSrcOrDest.setStatus("current")
_Hh3cBpaRowStatus_Type = RowStatus
_Hh3cBpaRowStatus_Object = MibTableColumn
hh3cBpaRowStatus = _Hh3cBpaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 1, 1, 3),
    _Hh3cBpaRowStatus_Type()
)
hh3cBpaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cBpaRowStatus.setStatus("current")
_Hh3cBpaStatTable_Object = MibTable
hh3cBpaStatTable = _Hh3cBpaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cBpaStatTable.setStatus("current")
_Hh3cBpaStatEntry_Object = MibTableRow
hh3cBpaStatEntry = _Hh3cBpaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 2, 1)
)
hh3cBpaStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-BPA-MIB", "hh3cBpaTrafficType"),
    (0, "HH3C-BPA-MIB", "hh3cBpaTrafficIndex"),
)
if mibBuilder.loadTexts:
    hh3cBpaStatEntry.setStatus("current")
_Hh3cBpaTrafficType_Type = InetAddressType
_Hh3cBpaTrafficType_Object = MibTableColumn
hh3cBpaTrafficType = _Hh3cBpaTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 2, 1, 1),
    _Hh3cBpaTrafficType_Type()
)
hh3cBpaTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBpaTrafficType.setStatus("current")


class _Hh3cBpaTrafficIndex_Type(Integer32):
    """Custom type hh3cBpaTrafficIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cBpaTrafficIndex_Type.__name__ = "Integer32"
_Hh3cBpaTrafficIndex_Object = MibTableColumn
hh3cBpaTrafficIndex = _Hh3cBpaTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 2, 1, 2),
    _Hh3cBpaTrafficIndex_Type()
)
hh3cBpaTrafficIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBpaTrafficIndex.setStatus("current")
_Hh3cBpaInPacketCount_Type = Counter64
_Hh3cBpaInPacketCount_Object = MibTableColumn
hh3cBpaInPacketCount = _Hh3cBpaInPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 2, 1, 3),
    _Hh3cBpaInPacketCount_Type()
)
hh3cBpaInPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBpaInPacketCount.setStatus("current")
_Hh3cBpaInOctetCount_Type = Counter64
_Hh3cBpaInOctetCount_Object = MibTableColumn
hh3cBpaInOctetCount = _Hh3cBpaInOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 2, 1, 4),
    _Hh3cBpaInOctetCount_Type()
)
hh3cBpaInOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBpaInOctetCount.setStatus("current")
_Hh3cBpaOutPacketCount_Type = Counter64
_Hh3cBpaOutPacketCount_Object = MibTableColumn
hh3cBpaOutPacketCount = _Hh3cBpaOutPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 2, 1, 5),
    _Hh3cBpaOutPacketCount_Type()
)
hh3cBpaOutPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBpaOutPacketCount.setStatus("current")
_Hh3cBpaOutOctetCount_Type = Counter64
_Hh3cBpaOutOctetCount_Object = MibTableColumn
hh3cBpaOutOctetCount = _Hh3cBpaOutOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144, 1, 2, 1, 6),
    _Hh3cBpaOutOctetCount_Type()
)
hh3cBpaOutOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBpaOutOctetCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-BPA-MIB",
    **{"hh3cBpa": hh3cBpa,
       "hh3cBpaObjects": hh3cBpaObjects,
       "hh3cBpaCfgTable": hh3cBpaCfgTable,
       "hh3cBpaCfgEntry": hh3cBpaCfgEntry,
       "hh3cBpaDirection": hh3cBpaDirection,
       "hh3cBpaSrcOrDest": hh3cBpaSrcOrDest,
       "hh3cBpaRowStatus": hh3cBpaRowStatus,
       "hh3cBpaStatTable": hh3cBpaStatTable,
       "hh3cBpaStatEntry": hh3cBpaStatEntry,
       "hh3cBpaTrafficType": hh3cBpaTrafficType,
       "hh3cBpaTrafficIndex": hh3cBpaTrafficIndex,
       "hh3cBpaInPacketCount": hh3cBpaInPacketCount,
       "hh3cBpaInOctetCount": hh3cBpaInOctetCount,
       "hh3cBpaOutPacketCount": hh3cBpaOutPacketCount,
       "hh3cBpaOutOctetCount": hh3cBpaOutOctetCount}
)

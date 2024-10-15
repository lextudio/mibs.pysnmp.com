# SNMP MIB module (HPN-ICF-BPA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-BPA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:32 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfBpa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144)
)
hpnicfBpa.setRevisions(
        ("2013-11-13 11:28",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfBpaObjects_ObjectIdentity = ObjectIdentity
hpnicfBpaObjects = _HpnicfBpaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1)
)
_HpnicfBpaCfgTable_Object = MibTable
hpnicfBpaCfgTable = _HpnicfBpaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfBpaCfgTable.setStatus("current")
_HpnicfBpaCfgEntry_Object = MibTableRow
hpnicfBpaCfgEntry = _HpnicfBpaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 1, 1)
)
hpnicfBpaCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-BPA-MIB", "hpnicfBpaDirection"),
)
if mibBuilder.loadTexts:
    hpnicfBpaCfgEntry.setStatus("current")


class _HpnicfBpaDirection_Type(Integer32):
    """Custom type hpnicfBpaDirection based on Integer32"""
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


_HpnicfBpaDirection_Type.__name__ = "Integer32"
_HpnicfBpaDirection_Object = MibTableColumn
hpnicfBpaDirection = _HpnicfBpaDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 1, 1, 1),
    _HpnicfBpaDirection_Type()
)
hpnicfBpaDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfBpaDirection.setStatus("current")


class _HpnicfBpaSrcOrDest_Type(Integer32):
    """Custom type hpnicfBpaSrcOrDest based on Integer32"""
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


_HpnicfBpaSrcOrDest_Type.__name__ = "Integer32"
_HpnicfBpaSrcOrDest_Object = MibTableColumn
hpnicfBpaSrcOrDest = _HpnicfBpaSrcOrDest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 1, 1, 2),
    _HpnicfBpaSrcOrDest_Type()
)
hpnicfBpaSrcOrDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfBpaSrcOrDest.setStatus("current")
_HpnicfBpaRowStatus_Type = RowStatus
_HpnicfBpaRowStatus_Object = MibTableColumn
hpnicfBpaRowStatus = _HpnicfBpaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 1, 1, 3),
    _HpnicfBpaRowStatus_Type()
)
hpnicfBpaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfBpaRowStatus.setStatus("current")
_HpnicfBpaStatTable_Object = MibTable
hpnicfBpaStatTable = _HpnicfBpaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfBpaStatTable.setStatus("current")
_HpnicfBpaStatEntry_Object = MibTableRow
hpnicfBpaStatEntry = _HpnicfBpaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1)
)
hpnicfBpaStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-BPA-MIB", "hpnicfBpaTrafficType"),
    (0, "HPN-ICF-BPA-MIB", "hpnicfBpaTrafficIndex"),
)
if mibBuilder.loadTexts:
    hpnicfBpaStatEntry.setStatus("current")
_HpnicfBpaTrafficType_Type = InetAddressType
_HpnicfBpaTrafficType_Object = MibTableColumn
hpnicfBpaTrafficType = _HpnicfBpaTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 1),
    _HpnicfBpaTrafficType_Type()
)
hpnicfBpaTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfBpaTrafficType.setStatus("current")


class _HpnicfBpaTrafficIndex_Type(Integer32):
    """Custom type hpnicfBpaTrafficIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfBpaTrafficIndex_Type.__name__ = "Integer32"
_HpnicfBpaTrafficIndex_Object = MibTableColumn
hpnicfBpaTrafficIndex = _HpnicfBpaTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 2),
    _HpnicfBpaTrafficIndex_Type()
)
hpnicfBpaTrafficIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfBpaTrafficIndex.setStatus("current")
_HpnicfBpaInPacketCount_Type = Counter64
_HpnicfBpaInPacketCount_Object = MibTableColumn
hpnicfBpaInPacketCount = _HpnicfBpaInPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 3),
    _HpnicfBpaInPacketCount_Type()
)
hpnicfBpaInPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBpaInPacketCount.setStatus("current")
_HpnicfBpaInOctetCount_Type = Counter64
_HpnicfBpaInOctetCount_Object = MibTableColumn
hpnicfBpaInOctetCount = _HpnicfBpaInOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 4),
    _HpnicfBpaInOctetCount_Type()
)
hpnicfBpaInOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBpaInOctetCount.setStatus("current")
_HpnicfBpaOutPacketCount_Type = Counter64
_HpnicfBpaOutPacketCount_Object = MibTableColumn
hpnicfBpaOutPacketCount = _HpnicfBpaOutPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 5),
    _HpnicfBpaOutPacketCount_Type()
)
hpnicfBpaOutPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBpaOutPacketCount.setStatus("current")
_HpnicfBpaOutOctetCount_Type = Counter64
_HpnicfBpaOutOctetCount_Object = MibTableColumn
hpnicfBpaOutOctetCount = _HpnicfBpaOutOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144, 1, 2, 1, 6),
    _HpnicfBpaOutOctetCount_Type()
)
hpnicfBpaOutOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBpaOutOctetCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-BPA-MIB",
    **{"hpnicfBpa": hpnicfBpa,
       "hpnicfBpaObjects": hpnicfBpaObjects,
       "hpnicfBpaCfgTable": hpnicfBpaCfgTable,
       "hpnicfBpaCfgEntry": hpnicfBpaCfgEntry,
       "hpnicfBpaDirection": hpnicfBpaDirection,
       "hpnicfBpaSrcOrDest": hpnicfBpaSrcOrDest,
       "hpnicfBpaRowStatus": hpnicfBpaRowStatus,
       "hpnicfBpaStatTable": hpnicfBpaStatTable,
       "hpnicfBpaStatEntry": hpnicfBpaStatEntry,
       "hpnicfBpaTrafficType": hpnicfBpaTrafficType,
       "hpnicfBpaTrafficIndex": hpnicfBpaTrafficIndex,
       "hpnicfBpaInPacketCount": hpnicfBpaInPacketCount,
       "hpnicfBpaInOctetCount": hpnicfBpaInOctetCount,
       "hpnicfBpaOutPacketCount": hpnicfBpaOutPacketCount,
       "hpnicfBpaOutOctetCount": hpnicfBpaOutOctetCount}
)

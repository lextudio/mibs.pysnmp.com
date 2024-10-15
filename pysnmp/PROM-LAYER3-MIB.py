# SNMP MIB module (PROM-LAYER3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PROM-LAYER3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:49 2024
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

(MacAddress,
 promSwitching) = mibBuilder.importSymbols(
    "PROMINET-MIB",
    "MacAddress",
    "promSwitching")

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



class IPIPXNetNumber(OctetString):
    """Custom type IPIPXNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class PromL3AddrFwdTblType(Integer32):
    """Custom type PromL3AddrFwdTblType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipmulticast", 2),
          ("ipunicast", 1),
          ("ipx", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PromSwitchingLayerIII_ObjectIdentity = ObjectIdentity
promSwitchingLayerIII = _PromSwitchingLayerIII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6)
)
_PromL3AddrFwdMgmt_ObjectIdentity = ObjectIdentity
promL3AddrFwdMgmt = _PromL3AddrFwdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1)
)
_PromL3AddrFwdDataBaseMgmt_ObjectIdentity = ObjectIdentity
promL3AddrFwdDataBaseMgmt = _PromL3AddrFwdDataBaseMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1)
)


class _PromL3AddrFwdIPUnicastStatus_Type(Integer32):
    """Custom type promL3AddrFwdIPUnicastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipunicastDisabled", 2),
          ("ipunicastEnabled", 1))
    )


_PromL3AddrFwdIPUnicastStatus_Type.__name__ = "Integer32"
_PromL3AddrFwdIPUnicastStatus_Object = MibScalar
promL3AddrFwdIPUnicastStatus = _PromL3AddrFwdIPUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 1),
    _PromL3AddrFwdIPUnicastStatus_Type()
)
promL3AddrFwdIPUnicastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPUnicastStatus.setStatus("mandatory")


class _PromL3AddrFwdIPUnicastMode_Type(Integer32):
    """Custom type promL3AddrFwdIPUnicastMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipunicastDA", 1),
          ("ipunicastSADA", 2))
    )


_PromL3AddrFwdIPUnicastMode_Type.__name__ = "Integer32"
_PromL3AddrFwdIPUnicastMode_Object = MibScalar
promL3AddrFwdIPUnicastMode = _PromL3AddrFwdIPUnicastMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 2),
    _PromL3AddrFwdIPUnicastMode_Type()
)
promL3AddrFwdIPUnicastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPUnicastMode.setStatus("mandatory")


class _PromL3AddrFwdIPUnicastHash_Type(Integer32):
    """Custom type promL3AddrFwdIPUnicastHash based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipunicast10bit", 2),
          ("ipunicast12bit", 3),
          ("ipunicast8bit", 1))
    )


_PromL3AddrFwdIPUnicastHash_Type.__name__ = "Integer32"
_PromL3AddrFwdIPUnicastHash_Object = MibScalar
promL3AddrFwdIPUnicastHash = _PromL3AddrFwdIPUnicastHash_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 3),
    _PromL3AddrFwdIPUnicastHash_Type()
)
promL3AddrFwdIPUnicastHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPUnicastHash.setStatus("mandatory")


class _PromL3AddrFwdIPUnicastAgeStatus_Type(Integer32):
    """Custom type promL3AddrFwdIPUnicastAgeStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipunicastAgeDisabled", 2),
          ("ipunicastAgeEnabled", 1))
    )


_PromL3AddrFwdIPUnicastAgeStatus_Type.__name__ = "Integer32"
_PromL3AddrFwdIPUnicastAgeStatus_Object = MibScalar
promL3AddrFwdIPUnicastAgeStatus = _PromL3AddrFwdIPUnicastAgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 4),
    _PromL3AddrFwdIPUnicastAgeStatus_Type()
)
promL3AddrFwdIPUnicastAgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPUnicastAgeStatus.setStatus("mandatory")


class _PromL3AddrFwdIPUnicastAgePeriod_Type(Integer32):
    """Custom type promL3AddrFwdIPUnicastAgePeriod based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 360),
    )


_PromL3AddrFwdIPUnicastAgePeriod_Type.__name__ = "Integer32"
_PromL3AddrFwdIPUnicastAgePeriod_Object = MibScalar
promL3AddrFwdIPUnicastAgePeriod = _PromL3AddrFwdIPUnicastAgePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 5),
    _PromL3AddrFwdIPUnicastAgePeriod_Type()
)
promL3AddrFwdIPUnicastAgePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPUnicastAgePeriod.setStatus("mandatory")


class _PromL3AddrFwdIPUnicastMaxEntries_Type(Integer32):
    """Custom type promL3AddrFwdIPUnicastMaxEntries based on Integer32"""
    defaultValue = 15000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_PromL3AddrFwdIPUnicastMaxEntries_Type.__name__ = "Integer32"
_PromL3AddrFwdIPUnicastMaxEntries_Object = MibScalar
promL3AddrFwdIPUnicastMaxEntries = _PromL3AddrFwdIPUnicastMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 6),
    _PromL3AddrFwdIPUnicastMaxEntries_Type()
)
promL3AddrFwdIPUnicastMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPUnicastMaxEntries.setStatus("mandatory")
_PromL3AddrFwdIPUnicastActiveEntries_Type = Counter32
_PromL3AddrFwdIPUnicastActiveEntries_Object = MibScalar
promL3AddrFwdIPUnicastActiveEntries = _PromL3AddrFwdIPUnicastActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 7),
    _PromL3AddrFwdIPUnicastActiveEntries_Type()
)
promL3AddrFwdIPUnicastActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPUnicastActiveEntries.setStatus("mandatory")
_PromL3AddrFwdIPUnicastAddedEntries_Type = Counter32
_PromL3AddrFwdIPUnicastAddedEntries_Object = MibScalar
promL3AddrFwdIPUnicastAddedEntries = _PromL3AddrFwdIPUnicastAddedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 8),
    _PromL3AddrFwdIPUnicastAddedEntries_Type()
)
promL3AddrFwdIPUnicastAddedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPUnicastAddedEntries.setStatus("mandatory")
_PromL3AddrFwdIPUnicastRemovedEntries_Type = Counter32
_PromL3AddrFwdIPUnicastRemovedEntries_Object = MibScalar
promL3AddrFwdIPUnicastRemovedEntries = _PromL3AddrFwdIPUnicastRemovedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 9),
    _PromL3AddrFwdIPUnicastRemovedEntries_Type()
)
promL3AddrFwdIPUnicastRemovedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPUnicastRemovedEntries.setStatus("mandatory")
_PromL3AddrFwdIPUnicastAgedEntries_Type = Counter32
_PromL3AddrFwdIPUnicastAgedEntries_Object = MibScalar
promL3AddrFwdIPUnicastAgedEntries = _PromL3AddrFwdIPUnicastAgedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 10),
    _PromL3AddrFwdIPUnicastAgedEntries_Type()
)
promL3AddrFwdIPUnicastAgedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPUnicastAgedEntries.setStatus("mandatory")


class _PromL3AddrFwdIPMulticastStatus_Type(Integer32):
    """Custom type promL3AddrFwdIPMulticastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipmulticastDisabled", 2),
          ("ipmulticastEnabled", 1))
    )


_PromL3AddrFwdIPMulticastStatus_Type.__name__ = "Integer32"
_PromL3AddrFwdIPMulticastStatus_Object = MibScalar
promL3AddrFwdIPMulticastStatus = _PromL3AddrFwdIPMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 11),
    _PromL3AddrFwdIPMulticastStatus_Type()
)
promL3AddrFwdIPMulticastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPMulticastStatus.setStatus("mandatory")


class _PromL3AddrFwdIPMulticastMode_Type(Integer32):
    """Custom type promL3AddrFwdIPMulticastMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipmulticastDA", 1),
          ("ipmulticastSADA", 2))
    )


_PromL3AddrFwdIPMulticastMode_Type.__name__ = "Integer32"
_PromL3AddrFwdIPMulticastMode_Object = MibScalar
promL3AddrFwdIPMulticastMode = _PromL3AddrFwdIPMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 12),
    _PromL3AddrFwdIPMulticastMode_Type()
)
promL3AddrFwdIPMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPMulticastMode.setStatus("mandatory")


class _PromL3AddrFwdIPMulticastHash_Type(Integer32):
    """Custom type promL3AddrFwdIPMulticastHash based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipmulticast10bit", 2),
          ("ipmulticast12bit", 3),
          ("ipmulticast8bit", 1))
    )


_PromL3AddrFwdIPMulticastHash_Type.__name__ = "Integer32"
_PromL3AddrFwdIPMulticastHash_Object = MibScalar
promL3AddrFwdIPMulticastHash = _PromL3AddrFwdIPMulticastHash_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 13),
    _PromL3AddrFwdIPMulticastHash_Type()
)
promL3AddrFwdIPMulticastHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPMulticastHash.setStatus("mandatory")


class _PromL3AddrFwdIPMulticastAgeStatus_Type(Integer32):
    """Custom type promL3AddrFwdIPMulticastAgeStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipmulticastAgeDisabled", 2),
          ("ipmulticastAgeEnabled", 1))
    )


_PromL3AddrFwdIPMulticastAgeStatus_Type.__name__ = "Integer32"
_PromL3AddrFwdIPMulticastAgeStatus_Object = MibScalar
promL3AddrFwdIPMulticastAgeStatus = _PromL3AddrFwdIPMulticastAgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 14),
    _PromL3AddrFwdIPMulticastAgeStatus_Type()
)
promL3AddrFwdIPMulticastAgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPMulticastAgeStatus.setStatus("mandatory")


class _PromL3AddrFwdIPMulticastAgePeriod_Type(Integer32):
    """Custom type promL3AddrFwdIPMulticastAgePeriod based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 360),
    )


_PromL3AddrFwdIPMulticastAgePeriod_Type.__name__ = "Integer32"
_PromL3AddrFwdIPMulticastAgePeriod_Object = MibScalar
promL3AddrFwdIPMulticastAgePeriod = _PromL3AddrFwdIPMulticastAgePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 15),
    _PromL3AddrFwdIPMulticastAgePeriod_Type()
)
promL3AddrFwdIPMulticastAgePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPMulticastAgePeriod.setStatus("mandatory")


class _PromL3AddrFwdIPMulticastMaxEntries_Type(Integer32):
    """Custom type promL3AddrFwdIPMulticastMaxEntries based on Integer32"""
    defaultValue = 15000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_PromL3AddrFwdIPMulticastMaxEntries_Type.__name__ = "Integer32"
_PromL3AddrFwdIPMulticastMaxEntries_Object = MibScalar
promL3AddrFwdIPMulticastMaxEntries = _PromL3AddrFwdIPMulticastMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 16),
    _PromL3AddrFwdIPMulticastMaxEntries_Type()
)
promL3AddrFwdIPMulticastMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPMulticastMaxEntries.setStatus("mandatory")
_PromL3AddrFwdIPMulticastActiveEntries_Type = Counter32
_PromL3AddrFwdIPMulticastActiveEntries_Object = MibScalar
promL3AddrFwdIPMulticastActiveEntries = _PromL3AddrFwdIPMulticastActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 17),
    _PromL3AddrFwdIPMulticastActiveEntries_Type()
)
promL3AddrFwdIPMulticastActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPMulticastActiveEntries.setStatus("mandatory")
_PromL3AddrFwdIPMulticastAddedEntries_Type = Counter32
_PromL3AddrFwdIPMulticastAddedEntries_Object = MibScalar
promL3AddrFwdIPMulticastAddedEntries = _PromL3AddrFwdIPMulticastAddedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 18),
    _PromL3AddrFwdIPMulticastAddedEntries_Type()
)
promL3AddrFwdIPMulticastAddedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPMulticastAddedEntries.setStatus("mandatory")
_PromL3AddrFwdIPMulticastRemovedEntries_Type = Counter32
_PromL3AddrFwdIPMulticastRemovedEntries_Object = MibScalar
promL3AddrFwdIPMulticastRemovedEntries = _PromL3AddrFwdIPMulticastRemovedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 19),
    _PromL3AddrFwdIPMulticastRemovedEntries_Type()
)
promL3AddrFwdIPMulticastRemovedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPMulticastRemovedEntries.setStatus("mandatory")
_PromL3AddrFwdIPMulticastAgedEntries_Type = Counter32
_PromL3AddrFwdIPMulticastAgedEntries_Object = MibScalar
promL3AddrFwdIPMulticastAgedEntries = _PromL3AddrFwdIPMulticastAgedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 20),
    _PromL3AddrFwdIPMulticastAgedEntries_Type()
)
promL3AddrFwdIPMulticastAgedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPMulticastAgedEntries.setStatus("mandatory")


class _PromL3AddrFwdIPXStatus_Type(Integer32):
    """Custom type promL3AddrFwdIPXStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipxDisabled", 2),
          ("ipxEnabled", 1))
    )


_PromL3AddrFwdIPXStatus_Type.__name__ = "Integer32"
_PromL3AddrFwdIPXStatus_Object = MibScalar
promL3AddrFwdIPXStatus = _PromL3AddrFwdIPXStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 21),
    _PromL3AddrFwdIPXStatus_Type()
)
promL3AddrFwdIPXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPXStatus.setStatus("mandatory")


class _PromL3AddrFwdIPXMode_Type(Integer32):
    """Custom type promL3AddrFwdIPXMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipxDA", 1),
          ("ipxSADA", 2))
    )


_PromL3AddrFwdIPXMode_Type.__name__ = "Integer32"
_PromL3AddrFwdIPXMode_Object = MibScalar
promL3AddrFwdIPXMode = _PromL3AddrFwdIPXMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 22),
    _PromL3AddrFwdIPXMode_Type()
)
promL3AddrFwdIPXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPXMode.setStatus("mandatory")


class _PromL3AddrFwdIPXHash_Type(Integer32):
    """Custom type promL3AddrFwdIPXHash based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipx10bit", 2),
          ("ipx12bit", 3),
          ("ipx8bit", 1))
    )


_PromL3AddrFwdIPXHash_Type.__name__ = "Integer32"
_PromL3AddrFwdIPXHash_Object = MibScalar
promL3AddrFwdIPXHash = _PromL3AddrFwdIPXHash_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 23),
    _PromL3AddrFwdIPXHash_Type()
)
promL3AddrFwdIPXHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPXHash.setStatus("mandatory")


class _PromL3AddrFwdIPXAgeStatus_Type(Integer32):
    """Custom type promL3AddrFwdIPXAgeStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipxAgeDisabled", 2),
          ("ipxAgeEnabled", 1))
    )


_PromL3AddrFwdIPXAgeStatus_Type.__name__ = "Integer32"
_PromL3AddrFwdIPXAgeStatus_Object = MibScalar
promL3AddrFwdIPXAgeStatus = _PromL3AddrFwdIPXAgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 24),
    _PromL3AddrFwdIPXAgeStatus_Type()
)
promL3AddrFwdIPXAgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPXAgeStatus.setStatus("mandatory")


class _PromL3AddrFwdIPXAgePeriod_Type(Integer32):
    """Custom type promL3AddrFwdIPXAgePeriod based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 360),
    )


_PromL3AddrFwdIPXAgePeriod_Type.__name__ = "Integer32"
_PromL3AddrFwdIPXAgePeriod_Object = MibScalar
promL3AddrFwdIPXAgePeriod = _PromL3AddrFwdIPXAgePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 25),
    _PromL3AddrFwdIPXAgePeriod_Type()
)
promL3AddrFwdIPXAgePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPXAgePeriod.setStatus("mandatory")


class _PromL3AddrFwdIPXMaxEntries_Type(Integer32):
    """Custom type promL3AddrFwdIPXMaxEntries based on Integer32"""
    defaultValue = 15000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_PromL3AddrFwdIPXMaxEntries_Type.__name__ = "Integer32"
_PromL3AddrFwdIPXMaxEntries_Object = MibScalar
promL3AddrFwdIPXMaxEntries = _PromL3AddrFwdIPXMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 26),
    _PromL3AddrFwdIPXMaxEntries_Type()
)
promL3AddrFwdIPXMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdIPXMaxEntries.setStatus("mandatory")
_PromL3AddrFwdIPXActiveEntries_Type = Counter32
_PromL3AddrFwdIPXActiveEntries_Object = MibScalar
promL3AddrFwdIPXActiveEntries = _PromL3AddrFwdIPXActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 27),
    _PromL3AddrFwdIPXActiveEntries_Type()
)
promL3AddrFwdIPXActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPXActiveEntries.setStatus("mandatory")
_PromL3AddrFwdIPXAddedEntries_Type = Counter32
_PromL3AddrFwdIPXAddedEntries_Object = MibScalar
promL3AddrFwdIPXAddedEntries = _PromL3AddrFwdIPXAddedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 28),
    _PromL3AddrFwdIPXAddedEntries_Type()
)
promL3AddrFwdIPXAddedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPXAddedEntries.setStatus("mandatory")
_PromL3AddrFwdIPXRemovedEntries_Type = Counter32
_PromL3AddrFwdIPXRemovedEntries_Object = MibScalar
promL3AddrFwdIPXRemovedEntries = _PromL3AddrFwdIPXRemovedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 29),
    _PromL3AddrFwdIPXRemovedEntries_Type()
)
promL3AddrFwdIPXRemovedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPXRemovedEntries.setStatus("mandatory")
_PromL3AddrFwdIPXAgedEntries_Type = Counter32
_PromL3AddrFwdIPXAgedEntries_Object = MibScalar
promL3AddrFwdIPXAgedEntries = _PromL3AddrFwdIPXAgedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 30),
    _PromL3AddrFwdIPXAgedEntries_Type()
)
promL3AddrFwdIPXAgedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdIPXAgedEntries.setStatus("mandatory")


class _PromL3AddrFwdSysMaxEntries_Type(Integer32):
    """Custom type promL3AddrFwdSysMaxEntries based on Integer32"""
    defaultValue = 130000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_PromL3AddrFwdSysMaxEntries_Type.__name__ = "Integer32"
_PromL3AddrFwdSysMaxEntries_Object = MibScalar
promL3AddrFwdSysMaxEntries = _PromL3AddrFwdSysMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 31),
    _PromL3AddrFwdSysMaxEntries_Type()
)
promL3AddrFwdSysMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL3AddrFwdSysMaxEntries.setStatus("mandatory")
_PromL3AddrFwdCacheTable_Object = MibTable
promL3AddrFwdCacheTable = _PromL3AddrFwdCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32)
)
if mibBuilder.loadTexts:
    promL3AddrFwdCacheTable.setStatus("mandatory")
_PromL3AddrFwdCacheEntry_Object = MibTableRow
promL3AddrFwdCacheEntry = _PromL3AddrFwdCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1)
)
promL3AddrFwdCacheEntry.setIndexNames(
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdCacheFabricPortID"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdCacheTblType"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdCacheDstAddr"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdCacheSrcAddr"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdCacheDstVlanID"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdCacheSrcVlanID"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdCacheDstPort"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdCacheSrcPort"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdCacheComp"),
)
if mibBuilder.loadTexts:
    promL3AddrFwdCacheEntry.setStatus("mandatory")
_PromL3AddrFwdCacheFabricPortID_Type = Integer32
_PromL3AddrFwdCacheFabricPortID_Object = MibTableColumn
promL3AddrFwdCacheFabricPortID = _PromL3AddrFwdCacheFabricPortID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 1),
    _PromL3AddrFwdCacheFabricPortID_Type()
)
promL3AddrFwdCacheFabricPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheFabricPortID.setStatus("mandatory")
_PromL3AddrFwdCacheTblType_Type = PromL3AddrFwdTblType
_PromL3AddrFwdCacheTblType_Object = MibTableColumn
promL3AddrFwdCacheTblType = _PromL3AddrFwdCacheTblType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 2),
    _PromL3AddrFwdCacheTblType_Type()
)
promL3AddrFwdCacheTblType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheTblType.setStatus("mandatory")
_PromL3AddrFwdCacheDstAddr_Type = IPIPXNetNumber
_PromL3AddrFwdCacheDstAddr_Object = MibTableColumn
promL3AddrFwdCacheDstAddr = _PromL3AddrFwdCacheDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 3),
    _PromL3AddrFwdCacheDstAddr_Type()
)
promL3AddrFwdCacheDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheDstAddr.setStatus("mandatory")
_PromL3AddrFwdCacheSrcAddr_Type = IPIPXNetNumber
_PromL3AddrFwdCacheSrcAddr_Object = MibTableColumn
promL3AddrFwdCacheSrcAddr = _PromL3AddrFwdCacheSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 4),
    _PromL3AddrFwdCacheSrcAddr_Type()
)
promL3AddrFwdCacheSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheSrcAddr.setStatus("mandatory")
_PromL3AddrFwdCacheDstVlanID_Type = Integer32
_PromL3AddrFwdCacheDstVlanID_Object = MibTableColumn
promL3AddrFwdCacheDstVlanID = _PromL3AddrFwdCacheDstVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 5),
    _PromL3AddrFwdCacheDstVlanID_Type()
)
promL3AddrFwdCacheDstVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheDstVlanID.setStatus("mandatory")
_PromL3AddrFwdCacheSrcVlanID_Type = Integer32
_PromL3AddrFwdCacheSrcVlanID_Object = MibTableColumn
promL3AddrFwdCacheSrcVlanID = _PromL3AddrFwdCacheSrcVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 6),
    _PromL3AddrFwdCacheSrcVlanID_Type()
)
promL3AddrFwdCacheSrcVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheSrcVlanID.setStatus("mandatory")


class _PromL3AddrFwdCacheDstPort_Type(Integer32):
    """Custom type promL3AddrFwdCacheDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PromL3AddrFwdCacheDstPort_Type.__name__ = "Integer32"
_PromL3AddrFwdCacheDstPort_Object = MibTableColumn
promL3AddrFwdCacheDstPort = _PromL3AddrFwdCacheDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 7),
    _PromL3AddrFwdCacheDstPort_Type()
)
promL3AddrFwdCacheDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheDstPort.setStatus("mandatory")


class _PromL3AddrFwdCacheSrcPort_Type(Integer32):
    """Custom type promL3AddrFwdCacheSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PromL3AddrFwdCacheSrcPort_Type.__name__ = "Integer32"
_PromL3AddrFwdCacheSrcPort_Object = MibTableColumn
promL3AddrFwdCacheSrcPort = _PromL3AddrFwdCacheSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 8),
    _PromL3AddrFwdCacheSrcPort_Type()
)
promL3AddrFwdCacheSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheSrcPort.setStatus("mandatory")


class _PromL3AddrFwdCacheComp_Type(Integer32):
    """Custom type promL3AddrFwdCacheComp based on Integer32"""
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
        *(("da", 1),
          ("da-dp", 4),
          ("da-prot", 3),
          ("da-sa", 2),
          ("da-sa-dp-sp", 6),
          ("da-sa-prot", 5))
    )


_PromL3AddrFwdCacheComp_Type.__name__ = "Integer32"
_PromL3AddrFwdCacheComp_Object = MibTableColumn
promL3AddrFwdCacheComp = _PromL3AddrFwdCacheComp_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 9),
    _PromL3AddrFwdCacheComp_Type()
)
promL3AddrFwdCacheComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheComp.setStatus("mandatory")
_PromL3AddrFwdCacheNxtHopMac_Type = MacAddress
_PromL3AddrFwdCacheNxtHopMac_Object = MibTableColumn
promL3AddrFwdCacheNxtHopMac = _PromL3AddrFwdCacheNxtHopMac_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 10),
    _PromL3AddrFwdCacheNxtHopMac_Type()
)
promL3AddrFwdCacheNxtHopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheNxtHopMac.setStatus("mandatory")


class _PromL3AddrFwdCacheIPXUse_Type(Integer32):
    """Custom type promL3AddrFwdCacheIPXUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useFWDhost", 2),
          ("usePDUhost", 1))
    )


_PromL3AddrFwdCacheIPXUse_Type.__name__ = "Integer32"
_PromL3AddrFwdCacheIPXUse_Object = MibTableColumn
promL3AddrFwdCacheIPXUse = _PromL3AddrFwdCacheIPXUse_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 11),
    _PromL3AddrFwdCacheIPXUse_Type()
)
promL3AddrFwdCacheIPXUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheIPXUse.setStatus("mandatory")


class _PromL3AddrFwdCacheFormat_Type(Integer32):
    """Custom type promL3AddrFwdCacheFormat based on Integer32"""
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
        *(("etherIPXDSAP", 2),
          ("etherIPXRAW", 4),
          ("etherSNAP", 3),
          ("etherV2", 1))
    )


_PromL3AddrFwdCacheFormat_Type.__name__ = "Integer32"
_PromL3AddrFwdCacheFormat_Object = MibTableColumn
promL3AddrFwdCacheFormat = _PromL3AddrFwdCacheFormat_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 12),
    _PromL3AddrFwdCacheFormat_Type()
)
promL3AddrFwdCacheFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheFormat.setStatus("mandatory")


class _PromL3AddrFwdCacheTTL_Type(Integer32):
    """Custom type promL3AddrFwdCacheTTL based on Integer32"""
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
        *(("ttl-GT128", 4),
          ("ttl-GT32", 2),
          ("ttl-GT64", 3),
          ("ttl-IGNORE", 1))
    )


_PromL3AddrFwdCacheTTL_Type.__name__ = "Integer32"
_PromL3AddrFwdCacheTTL_Object = MibTableColumn
promL3AddrFwdCacheTTL = _PromL3AddrFwdCacheTTL_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 13),
    _PromL3AddrFwdCacheTTL_Type()
)
promL3AddrFwdCacheTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheTTL.setStatus("mandatory")


class _PromL3AddrFwdCacheFilter_Type(Integer32):
    """Custom type promL3AddrFwdCacheFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filterOFF", 2),
          ("filterON", 1))
    )


_PromL3AddrFwdCacheFilter_Type.__name__ = "Integer32"
_PromL3AddrFwdCacheFilter_Object = MibTableColumn
promL3AddrFwdCacheFilter = _PromL3AddrFwdCacheFilter_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 14),
    _PromL3AddrFwdCacheFilter_Type()
)
promL3AddrFwdCacheFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheFilter.setStatus("mandatory")


class _PromL3AddrFwdCachePriority_Type(Integer32):
    """Custom type promL3AddrFwdCachePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PromL3AddrFwdCachePriority_Type.__name__ = "Integer32"
_PromL3AddrFwdCachePriority_Object = MibTableColumn
promL3AddrFwdCachePriority = _PromL3AddrFwdCachePriority_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 15),
    _PromL3AddrFwdCachePriority_Type()
)
promL3AddrFwdCachePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCachePriority.setStatus("mandatory")


class _PromL3AddrFwdCachePersistence_Type(Integer32):
    """Custom type promL3AddrFwdCachePersistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnTimeout", 3),
          ("invalid", 1),
          ("permanent", 2))
    )


_PromL3AddrFwdCachePersistence_Type.__name__ = "Integer32"
_PromL3AddrFwdCachePersistence_Object = MibTableColumn
promL3AddrFwdCachePersistence = _PromL3AddrFwdCachePersistence_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 16),
    _PromL3AddrFwdCachePersistence_Type()
)
promL3AddrFwdCachePersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCachePersistence.setStatus("mandatory")


class _PromL3AddrFwdCacheStatus_Type(Integer32):
    """Custom type promL3AddrFwdCacheStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learned", 1),
          ("mgmt", 2))
    )


_PromL3AddrFwdCacheStatus_Type.__name__ = "Integer32"
_PromL3AddrFwdCacheStatus_Object = MibTableColumn
promL3AddrFwdCacheStatus = _PromL3AddrFwdCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 32, 1, 17),
    _PromL3AddrFwdCacheStatus_Type()
)
promL3AddrFwdCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdCacheStatus.setStatus("mandatory")
_PromL3AddrFwdControlTable_Object = MibTable
promL3AddrFwdControlTable = _PromL3AddrFwdControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33)
)
if mibBuilder.loadTexts:
    promL3AddrFwdControlTable.setStatus("mandatory")
_PromL3AddrFwdControlEntry_Object = MibTableRow
promL3AddrFwdControlEntry = _PromL3AddrFwdControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1)
)
promL3AddrFwdControlEntry.setIndexNames(
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdControlFabricPortID"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdControlTblType"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdControlDstAddr"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdControlSrcAddr"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdControlDstVlanID"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdControlSrcVlanID"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdControlDstPort"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdControlSrcPort"),
    (0, "PROM-LAYER3-MIB", "promL3AddrFwdControlComp"),
)
if mibBuilder.loadTexts:
    promL3AddrFwdControlEntry.setStatus("mandatory")
_PromL3AddrFwdControlFabricPortID_Type = Integer32
_PromL3AddrFwdControlFabricPortID_Object = MibTableColumn
promL3AddrFwdControlFabricPortID = _PromL3AddrFwdControlFabricPortID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 1),
    _PromL3AddrFwdControlFabricPortID_Type()
)
promL3AddrFwdControlFabricPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlFabricPortID.setStatus("mandatory")
_PromL3AddrFwdControlTblType_Type = PromL3AddrFwdTblType
_PromL3AddrFwdControlTblType_Object = MibTableColumn
promL3AddrFwdControlTblType = _PromL3AddrFwdControlTblType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 2),
    _PromL3AddrFwdControlTblType_Type()
)
promL3AddrFwdControlTblType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlTblType.setStatus("mandatory")
_PromL3AddrFwdControlDstAddr_Type = IPIPXNetNumber
_PromL3AddrFwdControlDstAddr_Object = MibTableColumn
promL3AddrFwdControlDstAddr = _PromL3AddrFwdControlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 3),
    _PromL3AddrFwdControlDstAddr_Type()
)
promL3AddrFwdControlDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlDstAddr.setStatus("mandatory")
_PromL3AddrFwdControlSrcAddr_Type = IPIPXNetNumber
_PromL3AddrFwdControlSrcAddr_Object = MibTableColumn
promL3AddrFwdControlSrcAddr = _PromL3AddrFwdControlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 4),
    _PromL3AddrFwdControlSrcAddr_Type()
)
promL3AddrFwdControlSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlSrcAddr.setStatus("mandatory")
_PromL3AddrFwdControlDstVlanID_Type = Integer32
_PromL3AddrFwdControlDstVlanID_Object = MibTableColumn
promL3AddrFwdControlDstVlanID = _PromL3AddrFwdControlDstVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 5),
    _PromL3AddrFwdControlDstVlanID_Type()
)
promL3AddrFwdControlDstVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlDstVlanID.setStatus("mandatory")
_PromL3AddrFwdControlSrcVlanID_Type = Integer32
_PromL3AddrFwdControlSrcVlanID_Object = MibTableColumn
promL3AddrFwdControlSrcVlanID = _PromL3AddrFwdControlSrcVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 6),
    _PromL3AddrFwdControlSrcVlanID_Type()
)
promL3AddrFwdControlSrcVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlSrcVlanID.setStatus("mandatory")


class _PromL3AddrFwdControlDstPort_Type(Integer32):
    """Custom type promL3AddrFwdControlDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PromL3AddrFwdControlDstPort_Type.__name__ = "Integer32"
_PromL3AddrFwdControlDstPort_Object = MibTableColumn
promL3AddrFwdControlDstPort = _PromL3AddrFwdControlDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 7),
    _PromL3AddrFwdControlDstPort_Type()
)
promL3AddrFwdControlDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlDstPort.setStatus("mandatory")


class _PromL3AddrFwdControlSrcPort_Type(Integer32):
    """Custom type promL3AddrFwdControlSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PromL3AddrFwdControlSrcPort_Type.__name__ = "Integer32"
_PromL3AddrFwdControlSrcPort_Object = MibTableColumn
promL3AddrFwdControlSrcPort = _PromL3AddrFwdControlSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 8),
    _PromL3AddrFwdControlSrcPort_Type()
)
promL3AddrFwdControlSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlSrcPort.setStatus("mandatory")


class _PromL3AddrFwdControlComp_Type(Integer32):
    """Custom type promL3AddrFwdControlComp based on Integer32"""
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
        *(("da", 1),
          ("da-dp", 4),
          ("da-prot", 3),
          ("da-sa", 2),
          ("da-sa-dp-sp", 6),
          ("da-sa-prot", 5))
    )


_PromL3AddrFwdControlComp_Type.__name__ = "Integer32"
_PromL3AddrFwdControlComp_Object = MibTableColumn
promL3AddrFwdControlComp = _PromL3AddrFwdControlComp_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 9),
    _PromL3AddrFwdControlComp_Type()
)
promL3AddrFwdControlComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlComp.setStatus("mandatory")
_PromL3AddrFwdControlNxtHopMac_Type = MacAddress
_PromL3AddrFwdControlNxtHopMac_Object = MibTableColumn
promL3AddrFwdControlNxtHopMac = _PromL3AddrFwdControlNxtHopMac_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 10),
    _PromL3AddrFwdControlNxtHopMac_Type()
)
promL3AddrFwdControlNxtHopMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlNxtHopMac.setStatus("mandatory")


class _PromL3AddrFwdControlIPXUse_Type(Integer32):
    """Custom type promL3AddrFwdControlIPXUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useFWDhost", 2),
          ("usePDUhost", 1))
    )


_PromL3AddrFwdControlIPXUse_Type.__name__ = "Integer32"
_PromL3AddrFwdControlIPXUse_Object = MibTableColumn
promL3AddrFwdControlIPXUse = _PromL3AddrFwdControlIPXUse_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 11),
    _PromL3AddrFwdControlIPXUse_Type()
)
promL3AddrFwdControlIPXUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlIPXUse.setStatus("mandatory")


class _PromL3AddrFwdControlFormat_Type(Integer32):
    """Custom type promL3AddrFwdControlFormat based on Integer32"""
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
        *(("etherIPXDSAP", 2),
          ("etherIPXRAW", 4),
          ("etherSNAP", 3),
          ("etherV2", 1))
    )


_PromL3AddrFwdControlFormat_Type.__name__ = "Integer32"
_PromL3AddrFwdControlFormat_Object = MibTableColumn
promL3AddrFwdControlFormat = _PromL3AddrFwdControlFormat_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 12),
    _PromL3AddrFwdControlFormat_Type()
)
promL3AddrFwdControlFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlFormat.setStatus("mandatory")


class _PromL3AddrFwdControlTTL_Type(Integer32):
    """Custom type promL3AddrFwdControlTTL based on Integer32"""
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
        *(("ttl-GT128", 4),
          ("ttl-GT32", 2),
          ("ttl-GT64", 3),
          ("ttl-IGNORE", 1))
    )


_PromL3AddrFwdControlTTL_Type.__name__ = "Integer32"
_PromL3AddrFwdControlTTL_Object = MibTableColumn
promL3AddrFwdControlTTL = _PromL3AddrFwdControlTTL_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 13),
    _PromL3AddrFwdControlTTL_Type()
)
promL3AddrFwdControlTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlTTL.setStatus("mandatory")


class _PromL3AddrFwdControlFilter_Type(Integer32):
    """Custom type promL3AddrFwdControlFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filterOFF", 2),
          ("filterON", 1))
    )


_PromL3AddrFwdControlFilter_Type.__name__ = "Integer32"
_PromL3AddrFwdControlFilter_Object = MibTableColumn
promL3AddrFwdControlFilter = _PromL3AddrFwdControlFilter_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 14),
    _PromL3AddrFwdControlFilter_Type()
)
promL3AddrFwdControlFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlFilter.setStatus("mandatory")


class _PromL3AddrFwdControlPriority_Type(Integer32):
    """Custom type promL3AddrFwdControlPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PromL3AddrFwdControlPriority_Type.__name__ = "Integer32"
_PromL3AddrFwdControlPriority_Object = MibTableColumn
promL3AddrFwdControlPriority = _PromL3AddrFwdControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 15),
    _PromL3AddrFwdControlPriority_Type()
)
promL3AddrFwdControlPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlPriority.setStatus("mandatory")


class _PromL3AddrFwdControlPersistence_Type(Integer32):
    """Custom type promL3AddrFwdControlPersistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnTimeout", 3),
          ("invalid", 1),
          ("permanent", 2))
    )


_PromL3AddrFwdControlPersistence_Type.__name__ = "Integer32"
_PromL3AddrFwdControlPersistence_Object = MibTableColumn
promL3AddrFwdControlPersistence = _PromL3AddrFwdControlPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 6, 1, 1, 33, 1, 16),
    _PromL3AddrFwdControlPersistence_Type()
)
promL3AddrFwdControlPersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL3AddrFwdControlPersistence.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROM-LAYER3-MIB",
    **{"IPIPXNetNumber": IPIPXNetNumber,
       "PromL3AddrFwdTblType": PromL3AddrFwdTblType,
       "promSwitchingLayerIII": promSwitchingLayerIII,
       "promL3AddrFwdMgmt": promL3AddrFwdMgmt,
       "promL3AddrFwdDataBaseMgmt": promL3AddrFwdDataBaseMgmt,
       "promL3AddrFwdIPUnicastStatus": promL3AddrFwdIPUnicastStatus,
       "promL3AddrFwdIPUnicastMode": promL3AddrFwdIPUnicastMode,
       "promL3AddrFwdIPUnicastHash": promL3AddrFwdIPUnicastHash,
       "promL3AddrFwdIPUnicastAgeStatus": promL3AddrFwdIPUnicastAgeStatus,
       "promL3AddrFwdIPUnicastAgePeriod": promL3AddrFwdIPUnicastAgePeriod,
       "promL3AddrFwdIPUnicastMaxEntries": promL3AddrFwdIPUnicastMaxEntries,
       "promL3AddrFwdIPUnicastActiveEntries": promL3AddrFwdIPUnicastActiveEntries,
       "promL3AddrFwdIPUnicastAddedEntries": promL3AddrFwdIPUnicastAddedEntries,
       "promL3AddrFwdIPUnicastRemovedEntries": promL3AddrFwdIPUnicastRemovedEntries,
       "promL3AddrFwdIPUnicastAgedEntries": promL3AddrFwdIPUnicastAgedEntries,
       "promL3AddrFwdIPMulticastStatus": promL3AddrFwdIPMulticastStatus,
       "promL3AddrFwdIPMulticastMode": promL3AddrFwdIPMulticastMode,
       "promL3AddrFwdIPMulticastHash": promL3AddrFwdIPMulticastHash,
       "promL3AddrFwdIPMulticastAgeStatus": promL3AddrFwdIPMulticastAgeStatus,
       "promL3AddrFwdIPMulticastAgePeriod": promL3AddrFwdIPMulticastAgePeriod,
       "promL3AddrFwdIPMulticastMaxEntries": promL3AddrFwdIPMulticastMaxEntries,
       "promL3AddrFwdIPMulticastActiveEntries": promL3AddrFwdIPMulticastActiveEntries,
       "promL3AddrFwdIPMulticastAddedEntries": promL3AddrFwdIPMulticastAddedEntries,
       "promL3AddrFwdIPMulticastRemovedEntries": promL3AddrFwdIPMulticastRemovedEntries,
       "promL3AddrFwdIPMulticastAgedEntries": promL3AddrFwdIPMulticastAgedEntries,
       "promL3AddrFwdIPXStatus": promL3AddrFwdIPXStatus,
       "promL3AddrFwdIPXMode": promL3AddrFwdIPXMode,
       "promL3AddrFwdIPXHash": promL3AddrFwdIPXHash,
       "promL3AddrFwdIPXAgeStatus": promL3AddrFwdIPXAgeStatus,
       "promL3AddrFwdIPXAgePeriod": promL3AddrFwdIPXAgePeriod,
       "promL3AddrFwdIPXMaxEntries": promL3AddrFwdIPXMaxEntries,
       "promL3AddrFwdIPXActiveEntries": promL3AddrFwdIPXActiveEntries,
       "promL3AddrFwdIPXAddedEntries": promL3AddrFwdIPXAddedEntries,
       "promL3AddrFwdIPXRemovedEntries": promL3AddrFwdIPXRemovedEntries,
       "promL3AddrFwdIPXAgedEntries": promL3AddrFwdIPXAgedEntries,
       "promL3AddrFwdSysMaxEntries": promL3AddrFwdSysMaxEntries,
       "promL3AddrFwdCacheTable": promL3AddrFwdCacheTable,
       "promL3AddrFwdCacheEntry": promL3AddrFwdCacheEntry,
       "promL3AddrFwdCacheFabricPortID": promL3AddrFwdCacheFabricPortID,
       "promL3AddrFwdCacheTblType": promL3AddrFwdCacheTblType,
       "promL3AddrFwdCacheDstAddr": promL3AddrFwdCacheDstAddr,
       "promL3AddrFwdCacheSrcAddr": promL3AddrFwdCacheSrcAddr,
       "promL3AddrFwdCacheDstVlanID": promL3AddrFwdCacheDstVlanID,
       "promL3AddrFwdCacheSrcVlanID": promL3AddrFwdCacheSrcVlanID,
       "promL3AddrFwdCacheDstPort": promL3AddrFwdCacheDstPort,
       "promL3AddrFwdCacheSrcPort": promL3AddrFwdCacheSrcPort,
       "promL3AddrFwdCacheComp": promL3AddrFwdCacheComp,
       "promL3AddrFwdCacheNxtHopMac": promL3AddrFwdCacheNxtHopMac,
       "promL3AddrFwdCacheIPXUse": promL3AddrFwdCacheIPXUse,
       "promL3AddrFwdCacheFormat": promL3AddrFwdCacheFormat,
       "promL3AddrFwdCacheTTL": promL3AddrFwdCacheTTL,
       "promL3AddrFwdCacheFilter": promL3AddrFwdCacheFilter,
       "promL3AddrFwdCachePriority": promL3AddrFwdCachePriority,
       "promL3AddrFwdCachePersistence": promL3AddrFwdCachePersistence,
       "promL3AddrFwdCacheStatus": promL3AddrFwdCacheStatus,
       "promL3AddrFwdControlTable": promL3AddrFwdControlTable,
       "promL3AddrFwdControlEntry": promL3AddrFwdControlEntry,
       "promL3AddrFwdControlFabricPortID": promL3AddrFwdControlFabricPortID,
       "promL3AddrFwdControlTblType": promL3AddrFwdControlTblType,
       "promL3AddrFwdControlDstAddr": promL3AddrFwdControlDstAddr,
       "promL3AddrFwdControlSrcAddr": promL3AddrFwdControlSrcAddr,
       "promL3AddrFwdControlDstVlanID": promL3AddrFwdControlDstVlanID,
       "promL3AddrFwdControlSrcVlanID": promL3AddrFwdControlSrcVlanID,
       "promL3AddrFwdControlDstPort": promL3AddrFwdControlDstPort,
       "promL3AddrFwdControlSrcPort": promL3AddrFwdControlSrcPort,
       "promL3AddrFwdControlComp": promL3AddrFwdControlComp,
       "promL3AddrFwdControlNxtHopMac": promL3AddrFwdControlNxtHopMac,
       "promL3AddrFwdControlIPXUse": promL3AddrFwdControlIPXUse,
       "promL3AddrFwdControlFormat": promL3AddrFwdControlFormat,
       "promL3AddrFwdControlTTL": promL3AddrFwdControlTTL,
       "promL3AddrFwdControlFilter": promL3AddrFwdControlFilter,
       "promL3AddrFwdControlPriority": promL3AddrFwdControlPriority,
       "promL3AddrFwdControlPersistence": promL3AddrFwdControlPersistence}
)

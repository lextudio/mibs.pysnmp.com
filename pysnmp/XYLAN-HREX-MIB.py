# SNMP MIB module (XYLAN-HREX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-HREX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:05 2024
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

(xylanHrexArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanHrexArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanHrexRegisterTable_Object = MibTable
xylanHrexRegisterTable = _XylanHrexRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 1)
)
if mibBuilder.loadTexts:
    xylanHrexRegisterTable.setStatus("mandatory")
_XylanHrexRegisterEntry_Object = MibTableRow
xylanHrexRegisterEntry = _XylanHrexRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 1, 1)
)
xylanHrexRegisterEntry.setIndexNames(
    (0, "XYLAN-HREX-MIB", "xylanHrexRegisterNumber"),
)
if mibBuilder.loadTexts:
    xylanHrexRegisterEntry.setStatus("mandatory")


class _XylanHrexRegisterNumber_Type(Integer32):
    """Custom type xylanHrexRegisterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_XylanHrexRegisterNumber_Type.__name__ = "Integer32"
_XylanHrexRegisterNumber_Object = MibTableColumn
xylanHrexRegisterNumber = _XylanHrexRegisterNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 1, 1, 1),
    _XylanHrexRegisterNumber_Type()
)
xylanHrexRegisterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexRegisterNumber.setStatus("mandatory")


class _XylanHrexRegisterAllowType_Type(Integer32):
    """Custom type xylanHrexRegisterAllowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("cip", 2),
          ("invalid", 0),
          ("m013", 3),
          ("mpoa", 4),
          ("routing", 5),
          ("vrrp", 6))
    )


_XylanHrexRegisterAllowType_Type.__name__ = "Integer32"
_XylanHrexRegisterAllowType_Object = MibTableColumn
xylanHrexRegisterAllowType = _XylanHrexRegisterAllowType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 1, 1, 2),
    _XylanHrexRegisterAllowType_Type()
)
xylanHrexRegisterAllowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanHrexRegisterAllowType.setStatus("mandatory")


class _XylanHrexRegisterUseType_Type(Integer32):
    """Custom type xylanHrexRegisterUseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cip", 2),
          ("invalid", 0),
          ("m013", 3),
          ("mpoa", 4),
          ("routing", 5),
          ("unused", 1),
          ("vrrp", 6))
    )


_XylanHrexRegisterUseType_Type.__name__ = "Integer32"
_XylanHrexRegisterUseType_Object = MibTableColumn
xylanHrexRegisterUseType = _XylanHrexRegisterUseType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 1, 1, 3),
    _XylanHrexRegisterUseType_Type()
)
xylanHrexRegisterUseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexRegisterUseType.setStatus("mandatory")
_XylanHrexStatistics_ObjectIdentity = ObjectIdentity
xylanHrexStatistics = _XylanHrexStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 2)
)
_XylanHrexIpPacketsReceived_Type = Counter32
_XylanHrexIpPacketsReceived_Object = MibScalar
xylanHrexIpPacketsReceived = _XylanHrexIpPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 2, 1),
    _XylanHrexIpPacketsReceived_Type()
)
xylanHrexIpPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexIpPacketsReceived.setStatus("mandatory")
_XylanHrexIpPacketsForwarded_Type = Counter32
_XylanHrexIpPacketsForwarded_Object = MibScalar
xylanHrexIpPacketsForwarded = _XylanHrexIpPacketsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 2, 2),
    _XylanHrexIpPacketsForwarded_Type()
)
xylanHrexIpPacketsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexIpPacketsForwarded.setStatus("mandatory")
_XylanHrexIpPacketsDiscarded_Type = Counter32
_XylanHrexIpPacketsDiscarded_Object = MibScalar
xylanHrexIpPacketsDiscarded = _XylanHrexIpPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 2, 3),
    _XylanHrexIpPacketsDiscarded_Type()
)
xylanHrexIpPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexIpPacketsDiscarded.setStatus("mandatory")
_XylanHrexIpxPacketsReceived_Type = Counter32
_XylanHrexIpxPacketsReceived_Object = MibScalar
xylanHrexIpxPacketsReceived = _XylanHrexIpxPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 2, 4),
    _XylanHrexIpxPacketsReceived_Type()
)
xylanHrexIpxPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexIpxPacketsReceived.setStatus("mandatory")
_XylanHrexIpxPacketsForwarded_Type = Counter32
_XylanHrexIpxPacketsForwarded_Object = MibScalar
xylanHrexIpxPacketsForwarded = _XylanHrexIpxPacketsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 2, 5),
    _XylanHrexIpxPacketsForwarded_Type()
)
xylanHrexIpxPacketsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexIpxPacketsForwarded.setStatus("mandatory")
_XylanHrexIpxPacketsDiscarded_Type = Counter32
_XylanHrexIpxPacketsDiscarded_Object = MibScalar
xylanHrexIpxPacketsDiscarded = _XylanHrexIpxPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 2, 6),
    _XylanHrexIpxPacketsDiscarded_Type()
)
xylanHrexIpxPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexIpxPacketsDiscarded.setStatus("mandatory")
_XylanHrexUtilization_ObjectIdentity = ObjectIdentity
xylanHrexUtilization = _XylanHrexUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 3)
)
_XylanHrexPseudoCamHashTotal_Type = Counter32
_XylanHrexPseudoCamHashTotal_Object = MibScalar
xylanHrexPseudoCamHashTotal = _XylanHrexPseudoCamHashTotal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 3, 1),
    _XylanHrexPseudoCamHashTotal_Type()
)
xylanHrexPseudoCamHashTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexPseudoCamHashTotal.setStatus("mandatory")
_XylanHrexPseudoCamHashFree_Type = Counter32
_XylanHrexPseudoCamHashFree_Object = MibScalar
xylanHrexPseudoCamHashFree = _XylanHrexPseudoCamHashFree_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 3, 2),
    _XylanHrexPseudoCamHashFree_Type()
)
xylanHrexPseudoCamHashFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexPseudoCamHashFree.setStatus("mandatory")
_XylanHrexPseudoCamCollisionTotal_Type = Counter32
_XylanHrexPseudoCamCollisionTotal_Object = MibScalar
xylanHrexPseudoCamCollisionTotal = _XylanHrexPseudoCamCollisionTotal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 3, 3),
    _XylanHrexPseudoCamCollisionTotal_Type()
)
xylanHrexPseudoCamCollisionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexPseudoCamCollisionTotal.setStatus("mandatory")
_XylanHrexPseudoCamCollisionFree_Type = Counter32
_XylanHrexPseudoCamCollisionFree_Object = MibScalar
xylanHrexPseudoCamCollisionFree = _XylanHrexPseudoCamCollisionFree_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 3, 4),
    _XylanHrexPseudoCamCollisionFree_Type()
)
xylanHrexPseudoCamCollisionFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexPseudoCamCollisionFree.setStatus("mandatory")
_XylanHrexCacheTotal_Type = Counter32
_XylanHrexCacheTotal_Object = MibScalar
xylanHrexCacheTotal = _XylanHrexCacheTotal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 3, 5),
    _XylanHrexCacheTotal_Type()
)
xylanHrexCacheTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexCacheTotal.setStatus("mandatory")
_XylanHrexCacheFree_Type = Counter32
_XylanHrexCacheFree_Object = MibScalar
xylanHrexCacheFree = _XylanHrexCacheFree_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 3, 6),
    _XylanHrexCacheFree_Type()
)
xylanHrexCacheFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexCacheFree.setStatus("mandatory")
_XylanHrexCollisionLengthMax_Type = Counter32
_XylanHrexCollisionLengthMax_Object = MibScalar
xylanHrexCollisionLengthMax = _XylanHrexCollisionLengthMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 3, 7),
    _XylanHrexCollisionLengthMax_Type()
)
xylanHrexCollisionLengthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexCollisionLengthMax.setStatus("mandatory")
_XylanHrexCollisionLengthAvg_Type = Counter32
_XylanHrexCollisionLengthAvg_Object = MibScalar
xylanHrexCollisionLengthAvg = _XylanHrexCollisionLengthAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 3, 8),
    _XylanHrexCollisionLengthAvg_Type()
)
xylanHrexCollisionLengthAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanHrexCollisionLengthAvg.setStatus("mandatory")
_XylanHrexHash_ObjectIdentity = ObjectIdentity
xylanHrexHash = _XylanHrexHash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 4)
)
_XylanHrexHashOptimize_Type = Integer32
_XylanHrexHashOptimize_Object = MibScalar
xylanHrexHashOptimize = _XylanHrexHashOptimize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 4, 1),
    _XylanHrexHashOptimize_Type()
)
xylanHrexHashOptimize.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    xylanHrexHashOptimize.setStatus("mandatory")
_XylanHrexHashDefault_Type = Integer32
_XylanHrexHashDefault_Object = MibScalar
xylanHrexHashDefault = _XylanHrexHashDefault_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 31, 4, 2),
    _XylanHrexHashDefault_Type()
)
xylanHrexHashDefault.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    xylanHrexHashDefault.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-HREX-MIB",
    **{"xylanHrexRegisterTable": xylanHrexRegisterTable,
       "xylanHrexRegisterEntry": xylanHrexRegisterEntry,
       "xylanHrexRegisterNumber": xylanHrexRegisterNumber,
       "xylanHrexRegisterAllowType": xylanHrexRegisterAllowType,
       "xylanHrexRegisterUseType": xylanHrexRegisterUseType,
       "xylanHrexStatistics": xylanHrexStatistics,
       "xylanHrexIpPacketsReceived": xylanHrexIpPacketsReceived,
       "xylanHrexIpPacketsForwarded": xylanHrexIpPacketsForwarded,
       "xylanHrexIpPacketsDiscarded": xylanHrexIpPacketsDiscarded,
       "xylanHrexIpxPacketsReceived": xylanHrexIpxPacketsReceived,
       "xylanHrexIpxPacketsForwarded": xylanHrexIpxPacketsForwarded,
       "xylanHrexIpxPacketsDiscarded": xylanHrexIpxPacketsDiscarded,
       "xylanHrexUtilization": xylanHrexUtilization,
       "xylanHrexPseudoCamHashTotal": xylanHrexPseudoCamHashTotal,
       "xylanHrexPseudoCamHashFree": xylanHrexPseudoCamHashFree,
       "xylanHrexPseudoCamCollisionTotal": xylanHrexPseudoCamCollisionTotal,
       "xylanHrexPseudoCamCollisionFree": xylanHrexPseudoCamCollisionFree,
       "xylanHrexCacheTotal": xylanHrexCacheTotal,
       "xylanHrexCacheFree": xylanHrexCacheFree,
       "xylanHrexCollisionLengthMax": xylanHrexCollisionLengthMax,
       "xylanHrexCollisionLengthAvg": xylanHrexCollisionLengthAvg,
       "xylanHrexHash": xylanHrexHash,
       "xylanHrexHashOptimize": xylanHrexHashOptimize,
       "xylanHrexHashDefault": xylanHrexHashDefault}
)

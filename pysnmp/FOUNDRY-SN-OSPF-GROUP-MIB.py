# SNMP MIB module (FOUNDRY-SN-OSPF-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-OSPF-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:47 2024
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

(snOspf,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "snOspf")

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



class AreaID(IpAddress):
    """Custom type AreaID based on IpAddress"""




class RouterID(IpAddress):
    """Custom type RouterID based on IpAddress"""




class Metric(Integer32):
    """Custom type Metric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class BigMetric(Integer32):
    """Custom type BigMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )





class TruthVal(Integer32):
    """Custom type TruthVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )





class RtrStatus(Integer32):
    """Custom type RtrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )





class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class HelloRange(Integer32):
    """Custom type HelloRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )





class UpToMaxAge(Integer32):
    """Custom type UpToMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )





class DesignatedRouterPriority(Integer32):
    """Custom type DesignatedRouterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class TOSType(Integer32):
    """Custom type TOSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnOspfGen_ObjectIdentity = ObjectIdentity
snOspfGen = _SnOspfGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1)
)
_SnOspfRouterId_Type = RouterID
_SnOspfRouterId_Object = MibScalar
snOspfRouterId = _SnOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 1),
    _SnOspfRouterId_Type()
)
snOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRouterId.setStatus("mandatory")
_SnOspfAdminStat_Type = RtrStatus
_SnOspfAdminStat_Object = MibScalar
snOspfAdminStat = _SnOspfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 2),
    _SnOspfAdminStat_Type()
)
snOspfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfAdminStat.setStatus("mandatory")
_SnOspfASBdrRtrStatus_Type = TruthVal
_SnOspfASBdrRtrStatus_Object = MibScalar
snOspfASBdrRtrStatus = _SnOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 3),
    _SnOspfASBdrRtrStatus_Type()
)
snOspfASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfASBdrRtrStatus.setStatus("mandatory")
_SnOspfRedisMode_Type = RtrStatus
_SnOspfRedisMode_Object = MibScalar
snOspfRedisMode = _SnOspfRedisMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 4),
    _SnOspfRedisMode_Type()
)
snOspfRedisMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRedisMode.setStatus("mandatory")


class _SnOspfDefaultOspfMetricValue_Type(Integer32):
    """Custom type snOspfDefaultOspfMetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnOspfDefaultOspfMetricValue_Type.__name__ = "Integer32"
_SnOspfDefaultOspfMetricValue_Object = MibScalar
snOspfDefaultOspfMetricValue = _SnOspfDefaultOspfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 5),
    _SnOspfDefaultOspfMetricValue_Type()
)
snOspfDefaultOspfMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfDefaultOspfMetricValue.setStatus("mandatory")
_SnOspfExternLSACount_Type = Gauge32
_SnOspfExternLSACount_Object = MibScalar
snOspfExternLSACount = _SnOspfExternLSACount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 6),
    _SnOspfExternLSACount_Type()
)
snOspfExternLSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfExternLSACount.setStatus("mandatory")
_SnOspfExternLSACksumSum_Type = Integer32
_SnOspfExternLSACksumSum_Object = MibScalar
snOspfExternLSACksumSum = _SnOspfExternLSACksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 7),
    _SnOspfExternLSACksumSum_Type()
)
snOspfExternLSACksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfExternLSACksumSum.setStatus("mandatory")
_SnOspfOriginateNewLSAs_Type = Counter32
_SnOspfOriginateNewLSAs_Object = MibScalar
snOspfOriginateNewLSAs = _SnOspfOriginateNewLSAs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 8),
    _SnOspfOriginateNewLSAs_Type()
)
snOspfOriginateNewLSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfOriginateNewLSAs.setStatus("mandatory")
_SnOspfRxNewLSAs_Type = Counter32
_SnOspfRxNewLSAs_Object = MibScalar
snOspfRxNewLSAs = _SnOspfRxNewLSAs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 9),
    _SnOspfRxNewLSAs_Type()
)
snOspfRxNewLSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfRxNewLSAs.setStatus("mandatory")


class _SnOspfOspfRedisMetricType_Type(Integer32):
    """Custom type snOspfOspfRedisMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_SnOspfOspfRedisMetricType_Type.__name__ = "Integer32"
_SnOspfOspfRedisMetricType_Object = MibScalar
snOspfOspfRedisMetricType = _SnOspfOspfRedisMetricType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 10),
    _SnOspfOspfRedisMetricType_Type()
)
snOspfOspfRedisMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfOspfRedisMetricType.setStatus("mandatory")
_SnOspfExtLsdbLimit_Type = Integer32
_SnOspfExtLsdbLimit_Object = MibScalar
snOspfExtLsdbLimit = _SnOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 11),
    _SnOspfExtLsdbLimit_Type()
)
snOspfExtLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfExtLsdbLimit.setStatus("mandatory")


class _SnOspfExitOverflowInterval_Type(Integer32):
    """Custom type snOspfExitOverflowInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SnOspfExitOverflowInterval_Type.__name__ = "Integer32"
_SnOspfExitOverflowInterval_Object = MibScalar
snOspfExitOverflowInterval = _SnOspfExitOverflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 12),
    _SnOspfExitOverflowInterval_Type()
)
snOspfExitOverflowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfExitOverflowInterval.setStatus("mandatory")


class _SnOspfRfc1583Compatibility_Type(Integer32):
    """Custom type snOspfRfc1583Compatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnOspfRfc1583Compatibility_Type.__name__ = "Integer32"
_SnOspfRfc1583Compatibility_Object = MibScalar
snOspfRfc1583Compatibility = _SnOspfRfc1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 13),
    _SnOspfRfc1583Compatibility_Type()
)
snOspfRfc1583Compatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRfc1583Compatibility.setStatus("mandatory")


class _SnOspfRouterIdFormat_Type(Integer32):
    """Custom type snOspfRouterIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integer", 0),
          ("ipAddress", 1))
    )


_SnOspfRouterIdFormat_Type.__name__ = "Integer32"
_SnOspfRouterIdFormat_Object = MibScalar
snOspfRouterIdFormat = _SnOspfRouterIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 14),
    _SnOspfRouterIdFormat_Type()
)
snOspfRouterIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRouterIdFormat.setStatus("mandatory")


class _SnOspfDistance_Type(Integer32):
    """Custom type snOspfDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnOspfDistance_Type.__name__ = "Integer32"
_SnOspfDistance_Object = MibScalar
snOspfDistance = _SnOspfDistance_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 15),
    _SnOspfDistance_Type()
)
snOspfDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfDistance.setStatus("obsolete")


class _SnOspfDistanceIntra_Type(Integer32):
    """Custom type snOspfDistanceIntra based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnOspfDistanceIntra_Type.__name__ = "Integer32"
_SnOspfDistanceIntra_Object = MibScalar
snOspfDistanceIntra = _SnOspfDistanceIntra_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 16),
    _SnOspfDistanceIntra_Type()
)
snOspfDistanceIntra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfDistanceIntra.setStatus("mandatory")


class _SnOspfDistanceInter_Type(Integer32):
    """Custom type snOspfDistanceInter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnOspfDistanceInter_Type.__name__ = "Integer32"
_SnOspfDistanceInter_Object = MibScalar
snOspfDistanceInter = _SnOspfDistanceInter_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 17),
    _SnOspfDistanceInter_Type()
)
snOspfDistanceInter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfDistanceInter.setStatus("mandatory")


class _SnOspfDistanceExternal_Type(Integer32):
    """Custom type snOspfDistanceExternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnOspfDistanceExternal_Type.__name__ = "Integer32"
_SnOspfDistanceExternal_Object = MibScalar
snOspfDistanceExternal = _SnOspfDistanceExternal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 1, 18),
    _SnOspfDistanceExternal_Type()
)
snOspfDistanceExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfDistanceExternal.setStatus("mandatory")
_SnOspfArea_ObjectIdentity = ObjectIdentity
snOspfArea = _SnOspfArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 2)
)
_SnOspfAreaTable_Object = MibTable
snOspfAreaTable = _SnOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    snOspfAreaTable.setStatus("mandatory")
_SnOspfAreaEntry_Object = MibTableRow
snOspfAreaEntry = _SnOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 2, 1, 1)
)
snOspfAreaEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfAreaId"),
)
if mibBuilder.loadTexts:
    snOspfAreaEntry.setStatus("mandatory")
_SnOspfAreaId_Type = AreaID
_SnOspfAreaId_Object = MibTableColumn
snOspfAreaId = _SnOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 2, 1, 1, 1),
    _SnOspfAreaId_Type()
)
snOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaId.setStatus("mandatory")


class _SnOspfImportASExtern_Type(Integer32):
    """Custom type snOspfImportASExtern based on Integer32"""
    defaultValue = 1


_SnOspfImportASExtern_Object = MibTableColumn
snOspfImportASExtern = _SnOspfImportASExtern_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 2, 1, 1, 2),
    _SnOspfImportASExtern_Type()
)
snOspfImportASExtern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfImportASExtern.setStatus("mandatory")
_SnOspfStubMetric_Type = BigMetric
_SnOspfStubMetric_Object = MibTableColumn
snOspfStubMetric = _SnOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 2, 1, 1, 3),
    _SnOspfStubMetric_Type()
)
snOspfStubMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfStubMetric.setStatus("mandatory")


class _SnOspfAreaRowStatus_Type(Integer32):
    """Custom type snOspfAreaRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnOspfAreaRowStatus_Type.__name__ = "Integer32"
_SnOspfAreaRowStatus_Object = MibTableColumn
snOspfAreaRowStatus = _SnOspfAreaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 2, 1, 1, 4),
    _SnOspfAreaRowStatus_Type()
)
snOspfAreaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfAreaRowStatus.setStatus("mandatory")


class _SnOspfAreaIdFormat_Type(Integer32):
    """Custom type snOspfAreaIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integer", 0),
          ("ipAddress", 1))
    )


_SnOspfAreaIdFormat_Type.__name__ = "Integer32"
_SnOspfAreaIdFormat_Object = MibTableColumn
snOspfAreaIdFormat = _SnOspfAreaIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 2, 1, 1, 5),
    _SnOspfAreaIdFormat_Type()
)
snOspfAreaIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfAreaIdFormat.setStatus("mandatory")
_SnOspfAddrRange_ObjectIdentity = ObjectIdentity
snOspfAddrRange = _SnOspfAddrRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 3)
)
_SnOspfAreaRangeTable_Object = MibTable
snOspfAreaRangeTable = _SnOspfAreaRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    snOspfAreaRangeTable.setStatus("mandatory")
_SnOspfAreaRangeEntry_Object = MibTableRow
snOspfAreaRangeEntry = _SnOspfAreaRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 3, 1, 1)
)
snOspfAreaRangeEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfAreaRangeAreaID"),
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfAreaRangeNet"),
)
if mibBuilder.loadTexts:
    snOspfAreaRangeEntry.setStatus("mandatory")
_SnOspfAreaRangeAreaID_Type = AreaID
_SnOspfAreaRangeAreaID_Object = MibTableColumn
snOspfAreaRangeAreaID = _SnOspfAreaRangeAreaID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 3, 1, 1, 1),
    _SnOspfAreaRangeAreaID_Type()
)
snOspfAreaRangeAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaRangeAreaID.setStatus("mandatory")
_SnOspfAreaRangeNet_Type = IpAddress
_SnOspfAreaRangeNet_Object = MibTableColumn
snOspfAreaRangeNet = _SnOspfAreaRangeNet_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 3, 1, 1, 2),
    _SnOspfAreaRangeNet_Type()
)
snOspfAreaRangeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaRangeNet.setStatus("mandatory")
_SnOspfAreaRangeMask_Type = IpAddress
_SnOspfAreaRangeMask_Object = MibTableColumn
snOspfAreaRangeMask = _SnOspfAreaRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 3, 1, 1, 3),
    _SnOspfAreaRangeMask_Type()
)
snOspfAreaRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfAreaRangeMask.setStatus("mandatory")


class _SnOspfAreaRangeRowStatus_Type(Integer32):
    """Custom type snOspfAreaRangeRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnOspfAreaRangeRowStatus_Type.__name__ = "Integer32"
_SnOspfAreaRangeRowStatus_Object = MibTableColumn
snOspfAreaRangeRowStatus = _SnOspfAreaRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 3, 1, 1, 4),
    _SnOspfAreaRangeRowStatus_Type()
)
snOspfAreaRangeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfAreaRangeRowStatus.setStatus("mandatory")


class _SnOspfAreaRangeAreaIdFormat_Type(Integer32):
    """Custom type snOspfAreaRangeAreaIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integer", 0),
          ("ipAddress", 1))
    )


_SnOspfAreaRangeAreaIdFormat_Type.__name__ = "Integer32"
_SnOspfAreaRangeAreaIdFormat_Object = MibTableColumn
snOspfAreaRangeAreaIdFormat = _SnOspfAreaRangeAreaIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 3, 1, 1, 5),
    _SnOspfAreaRangeAreaIdFormat_Type()
)
snOspfAreaRangeAreaIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaRangeAreaIdFormat.setStatus("mandatory")
_SnOspfIntf_ObjectIdentity = ObjectIdentity
snOspfIntf = _SnOspfIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4)
)
_SnOspfIfTable_Object = MibTable
snOspfIfTable = _SnOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    snOspfIfTable.setStatus("deprecated")
_SnOspfIfEntry_Object = MibTableRow
snOspfIfEntry = _SnOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1)
)
snOspfIfEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfPort"),
)
if mibBuilder.loadTexts:
    snOspfIfEntry.setStatus("deprecated")
_SnOspfIfPort_Type = Integer32
_SnOspfIfPort_Object = MibTableColumn
snOspfIfPort = _SnOspfIfPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 1),
    _SnOspfIfPort_Type()
)
snOspfIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfPort.setStatus("deprecated")


class _SnOspfIfAreaId_Type(AreaID):
    """Custom type snOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_SnOspfIfAreaId_Object = MibTableColumn
snOspfIfAreaId = _SnOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 2),
    _SnOspfIfAreaId_Type()
)
snOspfIfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfAreaId.setStatus("deprecated")


class _SnOspfIfAdminStat_Type(RtrStatus):
    """Custom type snOspfIfAdminStat based on RtrStatus"""


_SnOspfIfAdminStat_Object = MibTableColumn
snOspfIfAdminStat = _SnOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 3),
    _SnOspfIfAdminStat_Type()
)
snOspfIfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfAdminStat.setStatus("deprecated")


class _SnOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type snOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_SnOspfIfRtrPriority_Object = MibTableColumn
snOspfIfRtrPriority = _SnOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 4),
    _SnOspfIfRtrPriority_Type()
)
snOspfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfRtrPriority.setStatus("deprecated")


class _SnOspfIfTransitDelay_Type(UpToMaxAge):
    """Custom type snOspfIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_SnOspfIfTransitDelay_Object = MibTableColumn
snOspfIfTransitDelay = _SnOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 5),
    _SnOspfIfTransitDelay_Type()
)
snOspfIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfTransitDelay.setStatus("deprecated")


class _SnOspfIfRetransInterval_Type(UpToMaxAge):
    """Custom type snOspfIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_SnOspfIfRetransInterval_Object = MibTableColumn
snOspfIfRetransInterval = _SnOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 6),
    _SnOspfIfRetransInterval_Type()
)
snOspfIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfRetransInterval.setStatus("deprecated")


class _SnOspfIfHelloInterval_Type(HelloRange):
    """Custom type snOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_SnOspfIfHelloInterval_Object = MibTableColumn
snOspfIfHelloInterval = _SnOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 7),
    _SnOspfIfHelloInterval_Type()
)
snOspfIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfHelloInterval.setStatus("deprecated")


class _SnOspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type snOspfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_SnOspfIfRtrDeadInterval_Object = MibTableColumn
snOspfIfRtrDeadInterval = _SnOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 8),
    _SnOspfIfRtrDeadInterval_Type()
)
snOspfIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfRtrDeadInterval.setStatus("deprecated")


class _SnOspfIfAuthType_Type(Integer32):
    """Custom type snOspfIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnOspfIfAuthType_Type.__name__ = "Integer32"
_SnOspfIfAuthType_Object = MibTableColumn
snOspfIfAuthType = _SnOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 9),
    _SnOspfIfAuthType_Type()
)
snOspfIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfAuthType.setStatus("deprecated")


class _SnOspfIfAuthKey_Type(OctetString):
    """Custom type snOspfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnOspfIfAuthKey_Type.__name__ = "OctetString"
_SnOspfIfAuthKey_Object = MibTableColumn
snOspfIfAuthKey = _SnOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 10),
    _SnOspfIfAuthKey_Type()
)
snOspfIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfAuthKey.setStatus("deprecated")


class _SnOspfIfMetricValue_Type(Integer32):
    """Custom type snOspfIfMetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnOspfIfMetricValue_Type.__name__ = "Integer32"
_SnOspfIfMetricValue_Object = MibTableColumn
snOspfIfMetricValue = _SnOspfIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 11),
    _SnOspfIfMetricValue_Type()
)
snOspfIfMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfMetricValue.setStatus("deprecated")


class _SnOspfIfRowStatus_Type(Integer32):
    """Custom type snOspfIfRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnOspfIfRowStatus_Type.__name__ = "Integer32"
_SnOspfIfRowStatus_Object = MibTableColumn
snOspfIfRowStatus = _SnOspfIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 12),
    _SnOspfIfRowStatus_Type()
)
snOspfIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfRowStatus.setStatus("deprecated")


class _SnOspfIfMd5AuthKeyId_Type(Integer32):
    """Custom type snOspfIfMd5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnOspfIfMd5AuthKeyId_Type.__name__ = "Integer32"
_SnOspfIfMd5AuthKeyId_Object = MibTableColumn
snOspfIfMd5AuthKeyId = _SnOspfIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 13),
    _SnOspfIfMd5AuthKeyId_Type()
)
snOspfIfMd5AuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfMd5AuthKeyId.setStatus("deprecated")


class _SnOspfIfMd5AuthKey_Type(OctetString):
    """Custom type snOspfIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnOspfIfMd5AuthKey_Type.__name__ = "OctetString"
_SnOspfIfMd5AuthKey_Object = MibTableColumn
snOspfIfMd5AuthKey = _SnOspfIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 14),
    _SnOspfIfMd5AuthKey_Type()
)
snOspfIfMd5AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfMd5AuthKey.setStatus("deprecated")


class _SnOspfIfMd5ActivationWaitTime_Type(Integer32):
    """Custom type snOspfIfMd5ActivationWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_SnOspfIfMd5ActivationWaitTime_Type.__name__ = "Integer32"
_SnOspfIfMd5ActivationWaitTime_Object = MibTableColumn
snOspfIfMd5ActivationWaitTime = _SnOspfIfMd5ActivationWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 15),
    _SnOspfIfMd5ActivationWaitTime_Type()
)
snOspfIfMd5ActivationWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfMd5ActivationWaitTime.setStatus("deprecated")


class _SnOspfIfAreaIdFormat_Type(Integer32):
    """Custom type snOspfIfAreaIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integer", 0),
          ("ipAddress", 1))
    )


_SnOspfIfAreaIdFormat_Type.__name__ = "Integer32"
_SnOspfIfAreaIdFormat_Object = MibTableColumn
snOspfIfAreaIdFormat = _SnOspfIfAreaIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 16),
    _SnOspfIfAreaIdFormat_Type()
)
snOspfIfAreaIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfAreaIdFormat.setStatus("deprecated")


class _SnOspfIfPassiveMode_Type(Integer32):
    """Custom type snOspfIfPassiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnOspfIfPassiveMode_Type.__name__ = "Integer32"
_SnOspfIfPassiveMode_Object = MibTableColumn
snOspfIfPassiveMode = _SnOspfIfPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 17),
    _SnOspfIfPassiveMode_Type()
)
snOspfIfPassiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfPassiveMode.setStatus("deprecated")


class _SnOspfIfDatabaseFilterAllOut_Type(Integer32):
    """Custom type snOspfIfDatabaseFilterAllOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnOspfIfDatabaseFilterAllOut_Type.__name__ = "Integer32"
_SnOspfIfDatabaseFilterAllOut_Object = MibTableColumn
snOspfIfDatabaseFilterAllOut = _SnOspfIfDatabaseFilterAllOut_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 18),
    _SnOspfIfDatabaseFilterAllOut_Type()
)
snOspfIfDatabaseFilterAllOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfDatabaseFilterAllOut.setStatus("deprecated")


class _SnOspfIfMtuIgnore_Type(Integer32):
    """Custom type snOspfIfMtuIgnore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnOspfIfMtuIgnore_Type.__name__ = "Integer32"
_SnOspfIfMtuIgnore_Object = MibTableColumn
snOspfIfMtuIgnore = _SnOspfIfMtuIgnore_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 19),
    _SnOspfIfMtuIgnore_Type()
)
snOspfIfMtuIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfMtuIgnore.setStatus("deprecated")


class _SnOspfIfNetworkP2mp_Type(Integer32):
    """Custom type snOspfIfNetworkP2mp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnOspfIfNetworkP2mp_Type.__name__ = "Integer32"
_SnOspfIfNetworkP2mp_Object = MibTableColumn
snOspfIfNetworkP2mp = _SnOspfIfNetworkP2mp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 1, 1, 20),
    _SnOspfIfNetworkP2mp_Type()
)
snOspfIfNetworkP2mp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIfNetworkP2mp.setStatus("deprecated")
_SnOspfIf2Table_Object = MibTable
snOspfIf2Table = _SnOspfIf2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    snOspfIf2Table.setStatus("mandatory")
_SnOspfIf2Entry_Object = MibTableRow
snOspfIf2Entry = _SnOspfIf2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1)
)
snOspfIf2Entry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIf2Port"),
)
if mibBuilder.loadTexts:
    snOspfIf2Entry.setStatus("mandatory")
_SnOspfIf2Port_Type = Integer32
_SnOspfIf2Port_Object = MibTableColumn
snOspfIf2Port = _SnOspfIf2Port_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 1),
    _SnOspfIf2Port_Type()
)
snOspfIf2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIf2Port.setStatus("mandatory")


class _SnOspfIf2AreaId_Type(AreaID):
    """Custom type snOspfIf2AreaId based on AreaID"""
    defaultHexValue = "00000000"


_SnOspfIf2AreaId_Object = MibTableColumn
snOspfIf2AreaId = _SnOspfIf2AreaId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 2),
    _SnOspfIf2AreaId_Type()
)
snOspfIf2AreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2AreaId.setStatus("mandatory")


class _SnOspfIf2AdminStat_Type(RtrStatus):
    """Custom type snOspfIf2AdminStat based on RtrStatus"""


_SnOspfIf2AdminStat_Object = MibTableColumn
snOspfIf2AdminStat = _SnOspfIf2AdminStat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 3),
    _SnOspfIf2AdminStat_Type()
)
snOspfIf2AdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2AdminStat.setStatus("mandatory")


class _SnOspfIf2RtrPriority_Type(DesignatedRouterPriority):
    """Custom type snOspfIf2RtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_SnOspfIf2RtrPriority_Object = MibTableColumn
snOspfIf2RtrPriority = _SnOspfIf2RtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 4),
    _SnOspfIf2RtrPriority_Type()
)
snOspfIf2RtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2RtrPriority.setStatus("mandatory")


class _SnOspfIf2TransitDelay_Type(UpToMaxAge):
    """Custom type snOspfIf2TransitDelay based on UpToMaxAge"""
    defaultValue = 1


_SnOspfIf2TransitDelay_Object = MibTableColumn
snOspfIf2TransitDelay = _SnOspfIf2TransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 5),
    _SnOspfIf2TransitDelay_Type()
)
snOspfIf2TransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2TransitDelay.setStatus("mandatory")


class _SnOspfIf2RetransInterval_Type(UpToMaxAge):
    """Custom type snOspfIf2RetransInterval based on UpToMaxAge"""
    defaultValue = 5


_SnOspfIf2RetransInterval_Object = MibTableColumn
snOspfIf2RetransInterval = _SnOspfIf2RetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 6),
    _SnOspfIf2RetransInterval_Type()
)
snOspfIf2RetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2RetransInterval.setStatus("mandatory")


class _SnOspfIf2HelloInterval_Type(HelloRange):
    """Custom type snOspfIf2HelloInterval based on HelloRange"""
    defaultValue = 10


_SnOspfIf2HelloInterval_Object = MibTableColumn
snOspfIf2HelloInterval = _SnOspfIf2HelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 7),
    _SnOspfIf2HelloInterval_Type()
)
snOspfIf2HelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2HelloInterval.setStatus("mandatory")


class _SnOspfIf2RtrDeadInterval_Type(PositiveInteger):
    """Custom type snOspfIf2RtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_SnOspfIf2RtrDeadInterval_Object = MibTableColumn
snOspfIf2RtrDeadInterval = _SnOspfIf2RtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 8),
    _SnOspfIf2RtrDeadInterval_Type()
)
snOspfIf2RtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2RtrDeadInterval.setStatus("mandatory")


class _SnOspfIf2AuthType_Type(Integer32):
    """Custom type snOspfIf2AuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnOspfIf2AuthType_Type.__name__ = "Integer32"
_SnOspfIf2AuthType_Object = MibTableColumn
snOspfIf2AuthType = _SnOspfIf2AuthType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 9),
    _SnOspfIf2AuthType_Type()
)
snOspfIf2AuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2AuthType.setStatus("mandatory")


class _SnOspfIf2AuthKey_Type(OctetString):
    """Custom type snOspfIf2AuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnOspfIf2AuthKey_Type.__name__ = "OctetString"
_SnOspfIf2AuthKey_Object = MibTableColumn
snOspfIf2AuthKey = _SnOspfIf2AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 10),
    _SnOspfIf2AuthKey_Type()
)
snOspfIf2AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2AuthKey.setStatus("mandatory")


class _SnOspfIf2MetricValue_Type(Integer32):
    """Custom type snOspfIf2MetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnOspfIf2MetricValue_Type.__name__ = "Integer32"
_SnOspfIf2MetricValue_Object = MibTableColumn
snOspfIf2MetricValue = _SnOspfIf2MetricValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 11),
    _SnOspfIf2MetricValue_Type()
)
snOspfIf2MetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2MetricValue.setStatus("mandatory")


class _SnOspfIf2RowStatus_Type(Integer32):
    """Custom type snOspfIf2RowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnOspfIf2RowStatus_Type.__name__ = "Integer32"
_SnOspfIf2RowStatus_Object = MibTableColumn
snOspfIf2RowStatus = _SnOspfIf2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 12),
    _SnOspfIf2RowStatus_Type()
)
snOspfIf2RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2RowStatus.setStatus("mandatory")


class _SnOspfIf2Md5AuthKeyId_Type(Integer32):
    """Custom type snOspfIf2Md5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnOspfIf2Md5AuthKeyId_Type.__name__ = "Integer32"
_SnOspfIf2Md5AuthKeyId_Object = MibTableColumn
snOspfIf2Md5AuthKeyId = _SnOspfIf2Md5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 13),
    _SnOspfIf2Md5AuthKeyId_Type()
)
snOspfIf2Md5AuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2Md5AuthKeyId.setStatus("mandatory")


class _SnOspfIf2Md5AuthKey_Type(OctetString):
    """Custom type snOspfIf2Md5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnOspfIf2Md5AuthKey_Type.__name__ = "OctetString"
_SnOspfIf2Md5AuthKey_Object = MibTableColumn
snOspfIf2Md5AuthKey = _SnOspfIf2Md5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 14),
    _SnOspfIf2Md5AuthKey_Type()
)
snOspfIf2Md5AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2Md5AuthKey.setStatus("mandatory")


class _SnOspfIf2Md5ActivationWaitTime_Type(Integer32):
    """Custom type snOspfIf2Md5ActivationWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_SnOspfIf2Md5ActivationWaitTime_Type.__name__ = "Integer32"
_SnOspfIf2Md5ActivationWaitTime_Object = MibTableColumn
snOspfIf2Md5ActivationWaitTime = _SnOspfIf2Md5ActivationWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 15),
    _SnOspfIf2Md5ActivationWaitTime_Type()
)
snOspfIf2Md5ActivationWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2Md5ActivationWaitTime.setStatus("mandatory")


class _SnOspfIf2AreaIdFormat_Type(Integer32):
    """Custom type snOspfIf2AreaIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integer", 0),
          ("ipAddress", 1))
    )


_SnOspfIf2AreaIdFormat_Type.__name__ = "Integer32"
_SnOspfIf2AreaIdFormat_Object = MibTableColumn
snOspfIf2AreaIdFormat = _SnOspfIf2AreaIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 16),
    _SnOspfIf2AreaIdFormat_Type()
)
snOspfIf2AreaIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIf2AreaIdFormat.setStatus("mandatory")


class _SnOspfIf2PassiveMode_Type(Integer32):
    """Custom type snOspfIf2PassiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnOspfIf2PassiveMode_Type.__name__ = "Integer32"
_SnOspfIf2PassiveMode_Object = MibTableColumn
snOspfIf2PassiveMode = _SnOspfIf2PassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 17),
    _SnOspfIf2PassiveMode_Type()
)
snOspfIf2PassiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2PassiveMode.setStatus("mandatory")


class _SnOspfIf2DatabaseFilterAllOut_Type(Integer32):
    """Custom type snOspfIf2DatabaseFilterAllOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnOspfIf2DatabaseFilterAllOut_Type.__name__ = "Integer32"
_SnOspfIf2DatabaseFilterAllOut_Object = MibTableColumn
snOspfIf2DatabaseFilterAllOut = _SnOspfIf2DatabaseFilterAllOut_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 18),
    _SnOspfIf2DatabaseFilterAllOut_Type()
)
snOspfIf2DatabaseFilterAllOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2DatabaseFilterAllOut.setStatus("mandatory")


class _SnOspfIf2MtuIgnore_Type(Integer32):
    """Custom type snOspfIf2MtuIgnore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnOspfIf2MtuIgnore_Type.__name__ = "Integer32"
_SnOspfIf2MtuIgnore_Object = MibTableColumn
snOspfIf2MtuIgnore = _SnOspfIf2MtuIgnore_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 19),
    _SnOspfIf2MtuIgnore_Type()
)
snOspfIf2MtuIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2MtuIgnore.setStatus("mandatory")


class _SnOspfIf2NetworkP2mp_Type(Integer32):
    """Custom type snOspfIf2NetworkP2mp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnOspfIf2NetworkP2mp_Type.__name__ = "Integer32"
_SnOspfIf2NetworkP2mp_Object = MibTableColumn
snOspfIf2NetworkP2mp = _SnOspfIf2NetworkP2mp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 4, 2, 1, 20),
    _SnOspfIf2NetworkP2mp_Type()
)
snOspfIf2NetworkP2mp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfIf2NetworkP2mp.setStatus("mandatory")
_SnOspfVirtIf_ObjectIdentity = ObjectIdentity
snOspfVirtIf = _SnOspfVirtIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5)
)
_SnOspfVirtIfTable_Object = MibTable
snOspfVirtIfTable = _SnOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    snOspfVirtIfTable.setStatus("mandatory")
_SnOspfVirtIfEntry_Object = MibTableRow
snOspfVirtIfEntry = _SnOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1)
)
snOspfVirtIfEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfAreaID"),
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    snOspfVirtIfEntry.setStatus("mandatory")
_SnOspfVirtIfAreaID_Type = AreaID
_SnOspfVirtIfAreaID_Object = MibTableColumn
snOspfVirtIfAreaID = _SnOspfVirtIfAreaID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 1),
    _SnOspfVirtIfAreaID_Type()
)
snOspfVirtIfAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfAreaID.setStatus("mandatory")
_SnOspfVirtIfNeighbor_Type = RouterID
_SnOspfVirtIfNeighbor_Object = MibTableColumn
snOspfVirtIfNeighbor = _SnOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 2),
    _SnOspfVirtIfNeighbor_Type()
)
snOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfNeighbor.setStatus("mandatory")


class _SnOspfVirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type snOspfVirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_SnOspfVirtIfTransitDelay_Object = MibTableColumn
snOspfVirtIfTransitDelay = _SnOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 3),
    _SnOspfVirtIfTransitDelay_Type()
)
snOspfVirtIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfVirtIfTransitDelay.setStatus("mandatory")


class _SnOspfVirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type snOspfVirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_SnOspfVirtIfRetransInterval_Object = MibTableColumn
snOspfVirtIfRetransInterval = _SnOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 4),
    _SnOspfVirtIfRetransInterval_Type()
)
snOspfVirtIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfVirtIfRetransInterval.setStatus("mandatory")


class _SnOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type snOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_SnOspfVirtIfHelloInterval_Object = MibTableColumn
snOspfVirtIfHelloInterval = _SnOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 5),
    _SnOspfVirtIfHelloInterval_Type()
)
snOspfVirtIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfVirtIfHelloInterval.setStatus("mandatory")


class _SnOspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type snOspfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 60


_SnOspfVirtIfRtrDeadInterval_Object = MibTableColumn
snOspfVirtIfRtrDeadInterval = _SnOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 6),
    _SnOspfVirtIfRtrDeadInterval_Type()
)
snOspfVirtIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfVirtIfRtrDeadInterval.setStatus("mandatory")


class _SnOspfVirtIfAuthType_Type(Integer32):
    """Custom type snOspfVirtIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnOspfVirtIfAuthType_Type.__name__ = "Integer32"
_SnOspfVirtIfAuthType_Object = MibTableColumn
snOspfVirtIfAuthType = _SnOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 7),
    _SnOspfVirtIfAuthType_Type()
)
snOspfVirtIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfVirtIfAuthType.setStatus("mandatory")


class _SnOspfVirtIfAuthKey_Type(OctetString):
    """Custom type snOspfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_SnOspfVirtIfAuthKey_Object = MibTableColumn
snOspfVirtIfAuthKey = _SnOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 8),
    _SnOspfVirtIfAuthKey_Type()
)
snOspfVirtIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfVirtIfAuthKey.setStatus("mandatory")


class _SnOspfVirtIfRowStatus_Type(Integer32):
    """Custom type snOspfVirtIfRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnOspfVirtIfRowStatus_Type.__name__ = "Integer32"
_SnOspfVirtIfRowStatus_Object = MibTableColumn
snOspfVirtIfRowStatus = _SnOspfVirtIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 9),
    _SnOspfVirtIfRowStatus_Type()
)
snOspfVirtIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfVirtIfRowStatus.setStatus("mandatory")


class _SnOspfVirtIfMd5AuthKeyId_Type(Integer32):
    """Custom type snOspfVirtIfMd5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnOspfVirtIfMd5AuthKeyId_Type.__name__ = "Integer32"
_SnOspfVirtIfMd5AuthKeyId_Object = MibTableColumn
snOspfVirtIfMd5AuthKeyId = _SnOspfVirtIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 10),
    _SnOspfVirtIfMd5AuthKeyId_Type()
)
snOspfVirtIfMd5AuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfVirtIfMd5AuthKeyId.setStatus("mandatory")


class _SnOspfVirtIfMd5AuthKey_Type(OctetString):
    """Custom type snOspfVirtIfMd5AuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnOspfVirtIfMd5AuthKey_Type.__name__ = "OctetString"
_SnOspfVirtIfMd5AuthKey_Object = MibTableColumn
snOspfVirtIfMd5AuthKey = _SnOspfVirtIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 11),
    _SnOspfVirtIfMd5AuthKey_Type()
)
snOspfVirtIfMd5AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfVirtIfMd5AuthKey.setStatus("mandatory")


class _SnOspfVirtIfMd5ActivationWaitTime_Type(Integer32):
    """Custom type snOspfVirtIfMd5ActivationWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_SnOspfVirtIfMd5ActivationWaitTime_Type.__name__ = "Integer32"
_SnOspfVirtIfMd5ActivationWaitTime_Object = MibTableColumn
snOspfVirtIfMd5ActivationWaitTime = _SnOspfVirtIfMd5ActivationWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 12),
    _SnOspfVirtIfMd5ActivationWaitTime_Type()
)
snOspfVirtIfMd5ActivationWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfVirtIfMd5ActivationWaitTime.setStatus("mandatory")


class _SnOspfVirtIfAreaIdFormat_Type(Integer32):
    """Custom type snOspfVirtIfAreaIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integer", 0),
          ("ipAddress", 1))
    )


_SnOspfVirtIfAreaIdFormat_Type.__name__ = "Integer32"
_SnOspfVirtIfAreaIdFormat_Object = MibTableColumn
snOspfVirtIfAreaIdFormat = _SnOspfVirtIfAreaIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 5, 1, 1, 13),
    _SnOspfVirtIfAreaIdFormat_Type()
)
snOspfVirtIfAreaIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfAreaIdFormat.setStatus("mandatory")
_SnOspfRedis_ObjectIdentity = ObjectIdentity
snOspfRedis = _SnOspfRedis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6)
)
_SnOspfRedisTable_Object = MibTable
snOspfRedisTable = _SnOspfRedisTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1)
)
if mibBuilder.loadTexts:
    snOspfRedisTable.setStatus("mandatory")
_SnOspfRedisEntry_Object = MibTableRow
snOspfRedisEntry = _SnOspfRedisEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1, 1)
)
snOspfRedisEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRedisIndex"),
)
if mibBuilder.loadTexts:
    snOspfRedisEntry.setStatus("mandatory")


class _SnOspfRedisIndex_Type(Integer32):
    """Custom type snOspfRedisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SnOspfRedisIndex_Type.__name__ = "Integer32"
_SnOspfRedisIndex_Object = MibTableColumn
snOspfRedisIndex = _SnOspfRedisIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1, 1, 1),
    _SnOspfRedisIndex_Type()
)
snOspfRedisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfRedisIndex.setStatus("mandatory")
_SnOspfRedisIpAddress_Type = IpAddress
_SnOspfRedisIpAddress_Object = MibTableColumn
snOspfRedisIpAddress = _SnOspfRedisIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1, 1, 2),
    _SnOspfRedisIpAddress_Type()
)
snOspfRedisIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRedisIpAddress.setStatus("mandatory")
_SnOspfRedisMask_Type = IpAddress
_SnOspfRedisMask_Object = MibTableColumn
snOspfRedisMask = _SnOspfRedisMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1, 1, 3),
    _SnOspfRedisMask_Type()
)
snOspfRedisMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRedisMask.setStatus("mandatory")


class _SnOspfRedisAction_Type(Integer32):
    """Custom type snOspfRedisAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("import", 1),
          ("noImport", 0))
    )


_SnOspfRedisAction_Type.__name__ = "Integer32"
_SnOspfRedisAction_Object = MibTableColumn
snOspfRedisAction = _SnOspfRedisAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1, 1, 4),
    _SnOspfRedisAction_Type()
)
snOspfRedisAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRedisAction.setStatus("mandatory")


class _SnOspfRedisProtocol_Type(Integer32):
    """Custom type snOspfRedisProtocol based on Integer32"""
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
        *(("all", 2),
          ("bgp", 4),
          ("connected", 5),
          ("isis", 6),
          ("rip", 1),
          ("static", 3))
    )


_SnOspfRedisProtocol_Type.__name__ = "Integer32"
_SnOspfRedisProtocol_Object = MibTableColumn
snOspfRedisProtocol = _SnOspfRedisProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1, 1, 5),
    _SnOspfRedisProtocol_Type()
)
snOspfRedisProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRedisProtocol.setStatus("mandatory")


class _SnOspfRedisSetOspfMetric_Type(Integer32):
    """Custom type snOspfRedisSetOspfMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnOspfRedisSetOspfMetric_Type.__name__ = "Integer32"
_SnOspfRedisSetOspfMetric_Object = MibTableColumn
snOspfRedisSetOspfMetric = _SnOspfRedisSetOspfMetric_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1, 1, 6),
    _SnOspfRedisSetOspfMetric_Type()
)
snOspfRedisSetOspfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRedisSetOspfMetric.setStatus("mandatory")
_SnOspfRedisOspfMetricValue_Type = Metric
_SnOspfRedisOspfMetricValue_Object = MibTableColumn
snOspfRedisOspfMetricValue = _SnOspfRedisOspfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1, 1, 7),
    _SnOspfRedisOspfMetricValue_Type()
)
snOspfRedisOspfMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRedisOspfMetricValue.setStatus("mandatory")


class _SnOspfRedisMatchRipMetric_Type(Integer32):
    """Custom type snOspfRedisMatchRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnOspfRedisMatchRipMetric_Type.__name__ = "Integer32"
_SnOspfRedisMatchRipMetric_Object = MibTableColumn
snOspfRedisMatchRipMetric = _SnOspfRedisMatchRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1, 1, 8),
    _SnOspfRedisMatchRipMetric_Type()
)
snOspfRedisMatchRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRedisMatchRipMetric.setStatus("mandatory")


class _SnOspfRedisRipMetricValue_Type(Integer32):
    """Custom type snOspfRedisRipMetricValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SnOspfRedisRipMetricValue_Type.__name__ = "Integer32"
_SnOspfRedisRipMetricValue_Object = MibTableColumn
snOspfRedisRipMetricValue = _SnOspfRedisRipMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1, 1, 9),
    _SnOspfRedisRipMetricValue_Type()
)
snOspfRedisRipMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRedisRipMetricValue.setStatus("mandatory")


class _SnOspfRedisRowStatus_Type(Integer32):
    """Custom type snOspfRedisRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnOspfRedisRowStatus_Type.__name__ = "Integer32"
_SnOspfRedisRowStatus_Object = MibTableColumn
snOspfRedisRowStatus = _SnOspfRedisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 6, 1, 1, 10),
    _SnOspfRedisRowStatus_Type()
)
snOspfRedisRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfRedisRowStatus.setStatus("mandatory")
_SnOspfNbr_ObjectIdentity = ObjectIdentity
snOspfNbr = _SnOspfNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7)
)
_SnOspfNbrTable_Object = MibTable
snOspfNbrTable = _SnOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1)
)
if mibBuilder.loadTexts:
    snOspfNbrTable.setStatus("mandatory")
_SnOspfNbrEntry_Object = MibTableRow
snOspfNbrEntry = _SnOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1, 1)
)
snOspfNbrEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfNbrEntryIndex"),
)
if mibBuilder.loadTexts:
    snOspfNbrEntry.setStatus("mandatory")
_SnOspfNbrEntryIndex_Type = Integer32
_SnOspfNbrEntryIndex_Object = MibTableColumn
snOspfNbrEntryIndex = _SnOspfNbrEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1, 1, 1),
    _SnOspfNbrEntryIndex_Type()
)
snOspfNbrEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfNbrEntryIndex.setStatus("mandatory")
_SnOspfNbrPort_Type = Integer32
_SnOspfNbrPort_Object = MibTableColumn
snOspfNbrPort = _SnOspfNbrPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1, 1, 2),
    _SnOspfNbrPort_Type()
)
snOspfNbrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfNbrPort.setStatus("mandatory")
_SnOspfNbrIpAddr_Type = IpAddress
_SnOspfNbrIpAddr_Object = MibTableColumn
snOspfNbrIpAddr = _SnOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1, 1, 3),
    _SnOspfNbrIpAddr_Type()
)
snOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfNbrIpAddr.setStatus("mandatory")
_SnOspfNbrIndex_Type = Integer32
_SnOspfNbrIndex_Object = MibTableColumn
snOspfNbrIndex = _SnOspfNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1, 1, 4),
    _SnOspfNbrIndex_Type()
)
snOspfNbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfNbrIndex.setStatus("mandatory")


class _SnOspfNbrRtrId_Type(RouterID):
    """Custom type snOspfNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_SnOspfNbrRtrId_Object = MibTableColumn
snOspfNbrRtrId = _SnOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1, 1, 5),
    _SnOspfNbrRtrId_Type()
)
snOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfNbrRtrId.setStatus("mandatory")


class _SnOspfNbrOptions_Type(Integer32):
    """Custom type snOspfNbrOptions based on Integer32"""
    defaultValue = 0


_SnOspfNbrOptions_Object = MibTableColumn
snOspfNbrOptions = _SnOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1, 1, 6),
    _SnOspfNbrOptions_Type()
)
snOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfNbrOptions.setStatus("mandatory")


class _SnOspfNbrPriority_Type(DesignatedRouterPriority):
    """Custom type snOspfNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_SnOspfNbrPriority_Object = MibTableColumn
snOspfNbrPriority = _SnOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1, 1, 7),
    _SnOspfNbrPriority_Type()
)
snOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfNbrPriority.setStatus("mandatory")


class _SnOspfNbrState_Type(Integer32):
    """Custom type snOspfNbrState based on Integer32"""
    defaultValue = 1

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
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangeStart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoWay", 4))
    )


_SnOspfNbrState_Type.__name__ = "Integer32"
_SnOspfNbrState_Object = MibTableColumn
snOspfNbrState = _SnOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1, 1, 8),
    _SnOspfNbrState_Type()
)
snOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfNbrState.setStatus("mandatory")
_SnOspfNbrEvents_Type = Counter32
_SnOspfNbrEvents_Object = MibTableColumn
snOspfNbrEvents = _SnOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1, 1, 9),
    _SnOspfNbrEvents_Type()
)
snOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfNbrEvents.setStatus("mandatory")
_SnOspfNbrLsRetransQLen_Type = Gauge32
_SnOspfNbrLsRetransQLen_Object = MibTableColumn
snOspfNbrLsRetransQLen = _SnOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 7, 1, 1, 10),
    _SnOspfNbrLsRetransQLen_Type()
)
snOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfNbrLsRetransQLen.setStatus("mandatory")
_SnOspfVirtNbr_ObjectIdentity = ObjectIdentity
snOspfVirtNbr = _SnOspfVirtNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8)
)
_SnOspfVirtNbrTable_Object = MibTable
snOspfVirtNbrTable = _SnOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8, 1)
)
if mibBuilder.loadTexts:
    snOspfVirtNbrTable.setStatus("mandatory")
_SnOspfVirtNbrEntry_Object = MibTableRow
snOspfVirtNbrEntry = _SnOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8, 1, 1)
)
snOspfVirtNbrEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtNbrEntryIndex"),
)
if mibBuilder.loadTexts:
    snOspfVirtNbrEntry.setStatus("mandatory")
_SnOspfVirtNbrEntryIndex_Type = Integer32
_SnOspfVirtNbrEntryIndex_Object = MibTableColumn
snOspfVirtNbrEntryIndex = _SnOspfVirtNbrEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8, 1, 1, 1),
    _SnOspfVirtNbrEntryIndex_Type()
)
snOspfVirtNbrEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtNbrEntryIndex.setStatus("mandatory")
_SnOspfVirtNbrArea_Type = AreaID
_SnOspfVirtNbrArea_Object = MibTableColumn
snOspfVirtNbrArea = _SnOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8, 1, 1, 2),
    _SnOspfVirtNbrArea_Type()
)
snOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtNbrArea.setStatus("mandatory")
_SnOspfVirtNbrRtrId_Type = RouterID
_SnOspfVirtNbrRtrId_Object = MibTableColumn
snOspfVirtNbrRtrId = _SnOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8, 1, 1, 3),
    _SnOspfVirtNbrRtrId_Type()
)
snOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtNbrRtrId.setStatus("mandatory")
_SnOspfVirtNbrIpAddr_Type = IpAddress
_SnOspfVirtNbrIpAddr_Object = MibTableColumn
snOspfVirtNbrIpAddr = _SnOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8, 1, 1, 4),
    _SnOspfVirtNbrIpAddr_Type()
)
snOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtNbrIpAddr.setStatus("mandatory")
_SnOspfVirtNbrOptions_Type = Integer32
_SnOspfVirtNbrOptions_Object = MibTableColumn
snOspfVirtNbrOptions = _SnOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8, 1, 1, 5),
    _SnOspfVirtNbrOptions_Type()
)
snOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtNbrOptions.setStatus("mandatory")


class _SnOspfVirtNbrState_Type(Integer32):
    """Custom type snOspfVirtNbrState based on Integer32"""
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
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangeStart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoWay", 4))
    )


_SnOspfVirtNbrState_Type.__name__ = "Integer32"
_SnOspfVirtNbrState_Object = MibTableColumn
snOspfVirtNbrState = _SnOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8, 1, 1, 6),
    _SnOspfVirtNbrState_Type()
)
snOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtNbrState.setStatus("mandatory")
_SnOspfVirtNbrEvents_Type = Counter32
_SnOspfVirtNbrEvents_Object = MibTableColumn
snOspfVirtNbrEvents = _SnOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8, 1, 1, 7),
    _SnOspfVirtNbrEvents_Type()
)
snOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtNbrEvents.setStatus("mandatory")
_SnOspfVirtNbrLSRetransQLen_Type = Gauge32
_SnOspfVirtNbrLSRetransQLen_Object = MibTableColumn
snOspfVirtNbrLSRetransQLen = _SnOspfVirtNbrLSRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8, 1, 1, 8),
    _SnOspfVirtNbrLSRetransQLen_Type()
)
snOspfVirtNbrLSRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtNbrLSRetransQLen.setStatus("mandatory")


class _SnOspfVirtNbrAreaIdFormat_Type(Integer32):
    """Custom type snOspfVirtNbrAreaIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integer", 0),
          ("ipAddress", 1))
    )


_SnOspfVirtNbrAreaIdFormat_Type.__name__ = "Integer32"
_SnOspfVirtNbrAreaIdFormat_Object = MibTableColumn
snOspfVirtNbrAreaIdFormat = _SnOspfVirtNbrAreaIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 8, 1, 1, 9),
    _SnOspfVirtNbrAreaIdFormat_Type()
)
snOspfVirtNbrAreaIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtNbrAreaIdFormat.setStatus("mandatory")
_SnOspfLsdb_ObjectIdentity = ObjectIdentity
snOspfLsdb = _SnOspfLsdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9)
)
_SnOspfLsdbTable_Object = MibTable
snOspfLsdbTable = _SnOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1)
)
if mibBuilder.loadTexts:
    snOspfLsdbTable.setStatus("mandatory")
_SnOspfLsdbEntry_Object = MibTableRow
snOspfLsdbEntry = _SnOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1, 1)
)
snOspfLsdbEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfLsdbEntryIndex"),
)
if mibBuilder.loadTexts:
    snOspfLsdbEntry.setStatus("mandatory")
_SnOspfLsdbEntryIndex_Type = Integer32
_SnOspfLsdbEntryIndex_Object = MibTableColumn
snOspfLsdbEntryIndex = _SnOspfLsdbEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1, 1, 1),
    _SnOspfLsdbEntryIndex_Type()
)
snOspfLsdbEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfLsdbEntryIndex.setStatus("mandatory")
_SnOspfLsdbAreaId_Type = AreaID
_SnOspfLsdbAreaId_Object = MibTableColumn
snOspfLsdbAreaId = _SnOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1, 1, 2),
    _SnOspfLsdbAreaId_Type()
)
snOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfLsdbAreaId.setStatus("mandatory")


class _SnOspfLsdbType_Type(Integer32):
    """Custom type snOspfLsdbType based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("asExternalLink", 5),
          ("asSummaryLink", 4),
          ("multicastLink", 6),
          ("networkLink", 2),
          ("nssaExternalLink", 7),
          ("opaqueAreaLink", 10),
          ("opaqueAsLink", 11),
          ("opaqueLink", 9),
          ("routerLink", 1),
          ("summaryLink", 3))
    )


_SnOspfLsdbType_Type.__name__ = "Integer32"
_SnOspfLsdbType_Object = MibTableColumn
snOspfLsdbType = _SnOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1, 1, 3),
    _SnOspfLsdbType_Type()
)
snOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfLsdbType.setStatus("mandatory")
_SnOspfLsdbLsId_Type = IpAddress
_SnOspfLsdbLsId_Object = MibTableColumn
snOspfLsdbLsId = _SnOspfLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1, 1, 4),
    _SnOspfLsdbLsId_Type()
)
snOspfLsdbLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfLsdbLsId.setStatus("mandatory")
_SnOspfLsdbRouterId_Type = RouterID
_SnOspfLsdbRouterId_Object = MibTableColumn
snOspfLsdbRouterId = _SnOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1, 1, 5),
    _SnOspfLsdbRouterId_Type()
)
snOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfLsdbRouterId.setStatus("mandatory")
_SnOspfLsdbSequence_Type = Integer32
_SnOspfLsdbSequence_Object = MibTableColumn
snOspfLsdbSequence = _SnOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1, 1, 6),
    _SnOspfLsdbSequence_Type()
)
snOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfLsdbSequence.setStatus("mandatory")
_SnOspfLsdbAge_Type = Integer32
_SnOspfLsdbAge_Object = MibTableColumn
snOspfLsdbAge = _SnOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1, 1, 7),
    _SnOspfLsdbAge_Type()
)
snOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfLsdbAge.setStatus("mandatory")
_SnOspfLsdbChecksum_Type = Integer32
_SnOspfLsdbChecksum_Object = MibTableColumn
snOspfLsdbChecksum = _SnOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1, 1, 8),
    _SnOspfLsdbChecksum_Type()
)
snOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfLsdbChecksum.setStatus("mandatory")


class _SnOspfLsdbAdvertisement_Type(OctetString):
    """Custom type snOspfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_SnOspfLsdbAdvertisement_Type.__name__ = "OctetString"
_SnOspfLsdbAdvertisement_Object = MibTableColumn
snOspfLsdbAdvertisement = _SnOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1, 1, 9),
    _SnOspfLsdbAdvertisement_Type()
)
snOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfLsdbAdvertisement.setStatus("mandatory")


class _SnOspfLsdbAreaIdFormat_Type(Integer32):
    """Custom type snOspfLsdbAreaIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integer", 0),
          ("ipAddress", 1))
    )


_SnOspfLsdbAreaIdFormat_Type.__name__ = "Integer32"
_SnOspfLsdbAreaIdFormat_Object = MibTableColumn
snOspfLsdbAreaIdFormat = _SnOspfLsdbAreaIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 9, 1, 1, 10),
    _SnOspfLsdbAreaIdFormat_Type()
)
snOspfLsdbAreaIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfLsdbAreaIdFormat.setStatus("mandatory")
_SnOspfExtLsdb_ObjectIdentity = ObjectIdentity
snOspfExtLsdb = _SnOspfExtLsdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 10)
)
_SnOspfExtLsdbTable_Object = MibTable
snOspfExtLsdbTable = _SnOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 10, 1)
)
if mibBuilder.loadTexts:
    snOspfExtLsdbTable.setStatus("mandatory")
_SnOspfExtLsdbEntry_Object = MibTableRow
snOspfExtLsdbEntry = _SnOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 10, 1, 1)
)
snOspfExtLsdbEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfExtLsdbEntryIndex"),
)
if mibBuilder.loadTexts:
    snOspfExtLsdbEntry.setStatus("mandatory")
_SnOspfExtLsdbEntryIndex_Type = Integer32
_SnOspfExtLsdbEntryIndex_Object = MibTableColumn
snOspfExtLsdbEntryIndex = _SnOspfExtLsdbEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 10, 1, 1, 1),
    _SnOspfExtLsdbEntryIndex_Type()
)
snOspfExtLsdbEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfExtLsdbEntryIndex.setStatus("mandatory")


class _SnOspfExtLsdbType_Type(Integer32):
    """Custom type snOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_SnOspfExtLsdbType_Type.__name__ = "Integer32"
_SnOspfExtLsdbType_Object = MibTableColumn
snOspfExtLsdbType = _SnOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 10, 1, 1, 2),
    _SnOspfExtLsdbType_Type()
)
snOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfExtLsdbType.setStatus("mandatory")
_SnOspfExtLsdbLsId_Type = IpAddress
_SnOspfExtLsdbLsId_Object = MibTableColumn
snOspfExtLsdbLsId = _SnOspfExtLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 10, 1, 1, 3),
    _SnOspfExtLsdbLsId_Type()
)
snOspfExtLsdbLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfExtLsdbLsId.setStatus("mandatory")
_SnOspfExtLsdbRouterId_Type = RouterID
_SnOspfExtLsdbRouterId_Object = MibTableColumn
snOspfExtLsdbRouterId = _SnOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 10, 1, 1, 4),
    _SnOspfExtLsdbRouterId_Type()
)
snOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfExtLsdbRouterId.setStatus("mandatory")
_SnOspfExtLsdbSequence_Type = Integer32
_SnOspfExtLsdbSequence_Object = MibTableColumn
snOspfExtLsdbSequence = _SnOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 10, 1, 1, 5),
    _SnOspfExtLsdbSequence_Type()
)
snOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfExtLsdbSequence.setStatus("mandatory")
_SnOspfExtLsdbAge_Type = Integer32
_SnOspfExtLsdbAge_Object = MibTableColumn
snOspfExtLsdbAge = _SnOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 10, 1, 1, 6),
    _SnOspfExtLsdbAge_Type()
)
snOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfExtLsdbAge.setStatus("mandatory")
_SnOspfExtLsdbChecksum_Type = Integer32
_SnOspfExtLsdbChecksum_Object = MibTableColumn
snOspfExtLsdbChecksum = _SnOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 10, 1, 1, 7),
    _SnOspfExtLsdbChecksum_Type()
)
snOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfExtLsdbChecksum.setStatus("mandatory")


class _SnOspfExtLsdbAdvertisement_Type(OctetString):
    """Custom type snOspfExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )


_SnOspfExtLsdbAdvertisement_Type.__name__ = "OctetString"
_SnOspfExtLsdbAdvertisement_Object = MibTableColumn
snOspfExtLsdbAdvertisement = _SnOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 10, 1, 1, 8),
    _SnOspfExtLsdbAdvertisement_Type()
)
snOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfExtLsdbAdvertisement.setStatus("mandatory")
_SnOspfAreaStatus_ObjectIdentity = ObjectIdentity
snOspfAreaStatus = _SnOspfAreaStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11)
)
_SnOspfAreaStatusTable_Object = MibTable
snOspfAreaStatusTable = _SnOspfAreaStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1)
)
if mibBuilder.loadTexts:
    snOspfAreaStatusTable.setStatus("mandatory")
_SnOspfAreaStatusEntry_Object = MibTableRow
snOspfAreaStatusEntry = _SnOspfAreaStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1, 1)
)
snOspfAreaStatusEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfAreaStatusEntryIndex"),
)
if mibBuilder.loadTexts:
    snOspfAreaStatusEntry.setStatus("mandatory")
_SnOspfAreaStatusEntryIndex_Type = Integer32
_SnOspfAreaStatusEntryIndex_Object = MibTableColumn
snOspfAreaStatusEntryIndex = _SnOspfAreaStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1, 1, 1),
    _SnOspfAreaStatusEntryIndex_Type()
)
snOspfAreaStatusEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaStatusEntryIndex.setStatus("mandatory")
_SnOspfAreaStatusAreaId_Type = AreaID
_SnOspfAreaStatusAreaId_Object = MibTableColumn
snOspfAreaStatusAreaId = _SnOspfAreaStatusAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1, 1, 2),
    _SnOspfAreaStatusAreaId_Type()
)
snOspfAreaStatusAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaStatusAreaId.setStatus("mandatory")


class _SnOspfAreaStatusImportASExtern_Type(Integer32):
    """Custom type snOspfAreaStatusImportASExtern based on Integer32"""
    defaultValue = 1


_SnOspfAreaStatusImportASExtern_Object = MibTableColumn
snOspfAreaStatusImportASExtern = _SnOspfAreaStatusImportASExtern_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1, 1, 3),
    _SnOspfAreaStatusImportASExtern_Type()
)
snOspfAreaStatusImportASExtern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaStatusImportASExtern.setStatus("mandatory")
_SnOspfAreaStatusStubMetric_Type = BigMetric
_SnOspfAreaStatusStubMetric_Object = MibTableColumn
snOspfAreaStatusStubMetric = _SnOspfAreaStatusStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1, 1, 4),
    _SnOspfAreaStatusStubMetric_Type()
)
snOspfAreaStatusStubMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaStatusStubMetric.setStatus("mandatory")
_SnOspfAreaStatusSpfRuns_Type = Counter32
_SnOspfAreaStatusSpfRuns_Object = MibTableColumn
snOspfAreaStatusSpfRuns = _SnOspfAreaStatusSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1, 1, 5),
    _SnOspfAreaStatusSpfRuns_Type()
)
snOspfAreaStatusSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaStatusSpfRuns.setStatus("mandatory")


class _SnOspfAreaStatusAreaBdrRtrCount_Type(Gauge32):
    """Custom type snOspfAreaStatusAreaBdrRtrCount based on Gauge32"""
    defaultValue = 0


_SnOspfAreaStatusAreaBdrRtrCount_Object = MibTableColumn
snOspfAreaStatusAreaBdrRtrCount = _SnOspfAreaStatusAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1, 1, 6),
    _SnOspfAreaStatusAreaBdrRtrCount_Type()
)
snOspfAreaStatusAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaStatusAreaBdrRtrCount.setStatus("mandatory")


class _SnOspfAreaStatusASBdrRtrCount_Type(Gauge32):
    """Custom type snOspfAreaStatusASBdrRtrCount based on Gauge32"""
    defaultValue = 0


_SnOspfAreaStatusASBdrRtrCount_Object = MibTableColumn
snOspfAreaStatusASBdrRtrCount = _SnOspfAreaStatusASBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1, 1, 7),
    _SnOspfAreaStatusASBdrRtrCount_Type()
)
snOspfAreaStatusASBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaStatusASBdrRtrCount.setStatus("mandatory")


class _SnOspfAreaStatusLSACount_Type(Gauge32):
    """Custom type snOspfAreaStatusLSACount based on Gauge32"""
    defaultValue = 0


_SnOspfAreaStatusLSACount_Object = MibTableColumn
snOspfAreaStatusLSACount = _SnOspfAreaStatusLSACount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1, 1, 8),
    _SnOspfAreaStatusLSACount_Type()
)
snOspfAreaStatusLSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaStatusLSACount.setStatus("mandatory")


class _SnOspfAreaStatusLSACksumSum_Type(Integer32):
    """Custom type snOspfAreaStatusLSACksumSum based on Integer32"""
    defaultValue = 0


_SnOspfAreaStatusLSACksumSum_Object = MibTableColumn
snOspfAreaStatusLSACksumSum = _SnOspfAreaStatusLSACksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1, 1, 9),
    _SnOspfAreaStatusLSACksumSum_Type()
)
snOspfAreaStatusLSACksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaStatusLSACksumSum.setStatus("mandatory")


class _SnOspfAreaStatusAreaIdFormat_Type(Integer32):
    """Custom type snOspfAreaStatusAreaIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integer", 0),
          ("ipAddress", 1))
    )


_SnOspfAreaStatusAreaIdFormat_Type.__name__ = "Integer32"
_SnOspfAreaStatusAreaIdFormat_Object = MibTableColumn
snOspfAreaStatusAreaIdFormat = _SnOspfAreaStatusAreaIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 11, 1, 1, 10),
    _SnOspfAreaStatusAreaIdFormat_Type()
)
snOspfAreaStatusAreaIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfAreaStatusAreaIdFormat.setStatus("mandatory")
_SnOspfIfStatus_ObjectIdentity = ObjectIdentity
snOspfIfStatus = _SnOspfIfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12)
)
_SnOspfIfStatusTable_Object = MibTable
snOspfIfStatusTable = _SnOspfIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1)
)
if mibBuilder.loadTexts:
    snOspfIfStatusTable.setStatus("mandatory")
_SnOspfIfStatusEntry_Object = MibTableRow
snOspfIfStatusEntry = _SnOspfIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1)
)
snOspfIfStatusEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfIfStatusEntryIndex"),
)
if mibBuilder.loadTexts:
    snOspfIfStatusEntry.setStatus("mandatory")
_SnOspfIfStatusEntryIndex_Type = Integer32
_SnOspfIfStatusEntryIndex_Object = MibTableColumn
snOspfIfStatusEntryIndex = _SnOspfIfStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 1),
    _SnOspfIfStatusEntryIndex_Type()
)
snOspfIfStatusEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusEntryIndex.setStatus("mandatory")
_SnOspfIfStatusPort_Type = Integer32
_SnOspfIfStatusPort_Object = MibTableColumn
snOspfIfStatusPort = _SnOspfIfStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 2),
    _SnOspfIfStatusPort_Type()
)
snOspfIfStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusPort.setStatus("mandatory")
_SnOspfIfStatusIpAddress_Type = IpAddress
_SnOspfIfStatusIpAddress_Object = MibTableColumn
snOspfIfStatusIpAddress = _SnOspfIfStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 3),
    _SnOspfIfStatusIpAddress_Type()
)
snOspfIfStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusIpAddress.setStatus("mandatory")


class _SnOspfIfStatusAreaId_Type(AreaID):
    """Custom type snOspfIfStatusAreaId based on AreaID"""
    defaultHexValue = "00000000"


_SnOspfIfStatusAreaId_Object = MibTableColumn
snOspfIfStatusAreaId = _SnOspfIfStatusAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 4),
    _SnOspfIfStatusAreaId_Type()
)
snOspfIfStatusAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusAreaId.setStatus("mandatory")


class _SnOspfIfStatusType_Type(Integer32):
    """Custom type snOspfIfStatusType based on Integer32"""
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
          ("nbma", 2),
          ("pointToPoint", 3))
    )


_SnOspfIfStatusType_Type.__name__ = "Integer32"
_SnOspfIfStatusType_Object = MibTableColumn
snOspfIfStatusType = _SnOspfIfStatusType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 5),
    _SnOspfIfStatusType_Type()
)
snOspfIfStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusType.setStatus("mandatory")
_SnOspfIfStatusAdminStat_Type = RtrStatus
_SnOspfIfStatusAdminStat_Object = MibTableColumn
snOspfIfStatusAdminStat = _SnOspfIfStatusAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 6),
    _SnOspfIfStatusAdminStat_Type()
)
snOspfIfStatusAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusAdminStat.setStatus("mandatory")


class _SnOspfIfStatusRtrPriority_Type(DesignatedRouterPriority):
    """Custom type snOspfIfStatusRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_SnOspfIfStatusRtrPriority_Object = MibTableColumn
snOspfIfStatusRtrPriority = _SnOspfIfStatusRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 7),
    _SnOspfIfStatusRtrPriority_Type()
)
snOspfIfStatusRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusRtrPriority.setStatus("mandatory")


class _SnOspfIfStatusTransitDelay_Type(UpToMaxAge):
    """Custom type snOspfIfStatusTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_SnOspfIfStatusTransitDelay_Object = MibTableColumn
snOspfIfStatusTransitDelay = _SnOspfIfStatusTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 8),
    _SnOspfIfStatusTransitDelay_Type()
)
snOspfIfStatusTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusTransitDelay.setStatus("mandatory")


class _SnOspfIfStatusRetransInterval_Type(UpToMaxAge):
    """Custom type snOspfIfStatusRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_SnOspfIfStatusRetransInterval_Object = MibTableColumn
snOspfIfStatusRetransInterval = _SnOspfIfStatusRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 9),
    _SnOspfIfStatusRetransInterval_Type()
)
snOspfIfStatusRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusRetransInterval.setStatus("mandatory")


class _SnOspfIfStatusHelloInterval_Type(HelloRange):
    """Custom type snOspfIfStatusHelloInterval based on HelloRange"""
    defaultValue = 10


_SnOspfIfStatusHelloInterval_Object = MibTableColumn
snOspfIfStatusHelloInterval = _SnOspfIfStatusHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 10),
    _SnOspfIfStatusHelloInterval_Type()
)
snOspfIfStatusHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusHelloInterval.setStatus("mandatory")


class _SnOspfIfStatusRtrDeadInterval_Type(PositiveInteger):
    """Custom type snOspfIfStatusRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_SnOspfIfStatusRtrDeadInterval_Object = MibTableColumn
snOspfIfStatusRtrDeadInterval = _SnOspfIfStatusRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 11),
    _SnOspfIfStatusRtrDeadInterval_Type()
)
snOspfIfStatusRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusRtrDeadInterval.setStatus("mandatory")


class _SnOspfIfStatusState_Type(Integer32):
    """Custom type snOspfIfStatusState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("backupDesignatedRouter", 6),
          ("designatedRouter", 5),
          ("down", 1),
          ("loopback", 2),
          ("otherDesignatedRouter", 7),
          ("pointToPoint", 4),
          ("waiting", 3))
    )


_SnOspfIfStatusState_Type.__name__ = "Integer32"
_SnOspfIfStatusState_Object = MibTableColumn
snOspfIfStatusState = _SnOspfIfStatusState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 12),
    _SnOspfIfStatusState_Type()
)
snOspfIfStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusState.setStatus("mandatory")


class _SnOspfIfStatusDesignatedRouter_Type(IpAddress):
    """Custom type snOspfIfStatusDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_SnOspfIfStatusDesignatedRouter_Object = MibTableColumn
snOspfIfStatusDesignatedRouter = _SnOspfIfStatusDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 13),
    _SnOspfIfStatusDesignatedRouter_Type()
)
snOspfIfStatusDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusDesignatedRouter.setStatus("mandatory")


class _SnOspfIfStatusBackupDesignatedRouter_Type(IpAddress):
    """Custom type snOspfIfStatusBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_SnOspfIfStatusBackupDesignatedRouter_Object = MibTableColumn
snOspfIfStatusBackupDesignatedRouter = _SnOspfIfStatusBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 14),
    _SnOspfIfStatusBackupDesignatedRouter_Type()
)
snOspfIfStatusBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusBackupDesignatedRouter.setStatus("mandatory")
_SnOspfIfStatusEvents_Type = Counter32
_SnOspfIfStatusEvents_Object = MibTableColumn
snOspfIfStatusEvents = _SnOspfIfStatusEvents_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 15),
    _SnOspfIfStatusEvents_Type()
)
snOspfIfStatusEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusEvents.setStatus("mandatory")


class _SnOspfIfStatusAuthType_Type(Integer32):
    """Custom type snOspfIfStatusAuthType based on Integer32"""
    defaultValue = 0


_SnOspfIfStatusAuthType_Object = MibTableColumn
snOspfIfStatusAuthType = _SnOspfIfStatusAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 16),
    _SnOspfIfStatusAuthType_Type()
)
snOspfIfStatusAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusAuthType.setStatus("mandatory")


class _SnOspfIfStatusAuthKey_Type(OctetString):
    """Custom type snOspfIfStatusAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnOspfIfStatusAuthKey_Type.__name__ = "OctetString"
_SnOspfIfStatusAuthKey_Object = MibTableColumn
snOspfIfStatusAuthKey = _SnOspfIfStatusAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 17),
    _SnOspfIfStatusAuthKey_Type()
)
snOspfIfStatusAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusAuthKey.setStatus("mandatory")
_SnOspfIfStatusMetricValue_Type = Metric
_SnOspfIfStatusMetricValue_Object = MibTableColumn
snOspfIfStatusMetricValue = _SnOspfIfStatusMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 18),
    _SnOspfIfStatusMetricValue_Type()
)
snOspfIfStatusMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusMetricValue.setStatus("mandatory")


class _SnOspfIfStatusMd5AuthKeyId_Type(Integer32):
    """Custom type snOspfIfStatusMd5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnOspfIfStatusMd5AuthKeyId_Type.__name__ = "Integer32"
_SnOspfIfStatusMd5AuthKeyId_Object = MibTableColumn
snOspfIfStatusMd5AuthKeyId = _SnOspfIfStatusMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 19),
    _SnOspfIfStatusMd5AuthKeyId_Type()
)
snOspfIfStatusMd5AuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusMd5AuthKeyId.setStatus("mandatory")


class _SnOspfIfStatusMd5AuthKey_Type(OctetString):
    """Custom type snOspfIfStatusMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnOspfIfStatusMd5AuthKey_Type.__name__ = "OctetString"
_SnOspfIfStatusMd5AuthKey_Object = MibTableColumn
snOspfIfStatusMd5AuthKey = _SnOspfIfStatusMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 20),
    _SnOspfIfStatusMd5AuthKey_Type()
)
snOspfIfStatusMd5AuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusMd5AuthKey.setStatus("mandatory")


class _SnOspfIfStatusMd5ActivationWaitTime_Type(Integer32):
    """Custom type snOspfIfStatusMd5ActivationWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_SnOspfIfStatusMd5ActivationWaitTime_Type.__name__ = "Integer32"
_SnOspfIfStatusMd5ActivationWaitTime_Object = MibTableColumn
snOspfIfStatusMd5ActivationWaitTime = _SnOspfIfStatusMd5ActivationWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 21),
    _SnOspfIfStatusMd5ActivationWaitTime_Type()
)
snOspfIfStatusMd5ActivationWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusMd5ActivationWaitTime.setStatus("mandatory")


class _SnOspfIfStatusAreaIdFormat_Type(Integer32):
    """Custom type snOspfIfStatusAreaIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integer", 0),
          ("ipAddress", 1))
    )


_SnOspfIfStatusAreaIdFormat_Type.__name__ = "Integer32"
_SnOspfIfStatusAreaIdFormat_Object = MibTableColumn
snOspfIfStatusAreaIdFormat = _SnOspfIfStatusAreaIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 12, 1, 1, 22),
    _SnOspfIfStatusAreaIdFormat_Type()
)
snOspfIfStatusAreaIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfIfStatusAreaIdFormat.setStatus("mandatory")
_SnOspfVirtIfStatus_ObjectIdentity = ObjectIdentity
snOspfVirtIfStatus = _SnOspfVirtIfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13)
)
_SnOspfVirtIfStatusTable_Object = MibTable
snOspfVirtIfStatusTable = _SnOspfVirtIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1)
)
if mibBuilder.loadTexts:
    snOspfVirtIfStatusTable.setStatus("mandatory")
_SnOspfVirtIfStatusEntry_Object = MibTableRow
snOspfVirtIfStatusEntry = _SnOspfVirtIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1)
)
snOspfVirtIfStatusEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusEntryIndex"),
)
if mibBuilder.loadTexts:
    snOspfVirtIfStatusEntry.setStatus("mandatory")
_SnOspfVirtIfStatusEntryIndex_Type = Integer32
_SnOspfVirtIfStatusEntryIndex_Object = MibTableColumn
snOspfVirtIfStatusEntryIndex = _SnOspfVirtIfStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 1),
    _SnOspfVirtIfStatusEntryIndex_Type()
)
snOspfVirtIfStatusEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusEntryIndex.setStatus("mandatory")
_SnOspfVirtIfStatusAreaID_Type = AreaID
_SnOspfVirtIfStatusAreaID_Object = MibTableColumn
snOspfVirtIfStatusAreaID = _SnOspfVirtIfStatusAreaID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 2),
    _SnOspfVirtIfStatusAreaID_Type()
)
snOspfVirtIfStatusAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusAreaID.setStatus("mandatory")
_SnOspfVirtIfStatusNeighbor_Type = RouterID
_SnOspfVirtIfStatusNeighbor_Object = MibTableColumn
snOspfVirtIfStatusNeighbor = _SnOspfVirtIfStatusNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 3),
    _SnOspfVirtIfStatusNeighbor_Type()
)
snOspfVirtIfStatusNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusNeighbor.setStatus("mandatory")


class _SnOspfVirtIfStatusTransitDelay_Type(UpToMaxAge):
    """Custom type snOspfVirtIfStatusTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_SnOspfVirtIfStatusTransitDelay_Object = MibTableColumn
snOspfVirtIfStatusTransitDelay = _SnOspfVirtIfStatusTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 4),
    _SnOspfVirtIfStatusTransitDelay_Type()
)
snOspfVirtIfStatusTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusTransitDelay.setStatus("mandatory")


class _SnOspfVirtIfStatusRetransInterval_Type(UpToMaxAge):
    """Custom type snOspfVirtIfStatusRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_SnOspfVirtIfStatusRetransInterval_Object = MibTableColumn
snOspfVirtIfStatusRetransInterval = _SnOspfVirtIfStatusRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 5),
    _SnOspfVirtIfStatusRetransInterval_Type()
)
snOspfVirtIfStatusRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusRetransInterval.setStatus("mandatory")


class _SnOspfVirtIfStatusHelloInterval_Type(HelloRange):
    """Custom type snOspfVirtIfStatusHelloInterval based on HelloRange"""
    defaultValue = 10


_SnOspfVirtIfStatusHelloInterval_Object = MibTableColumn
snOspfVirtIfStatusHelloInterval = _SnOspfVirtIfStatusHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 6),
    _SnOspfVirtIfStatusHelloInterval_Type()
)
snOspfVirtIfStatusHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusHelloInterval.setStatus("mandatory")


class _SnOspfVirtIfStatusRtrDeadInterval_Type(PositiveInteger):
    """Custom type snOspfVirtIfStatusRtrDeadInterval based on PositiveInteger"""
    defaultValue = 60


_SnOspfVirtIfStatusRtrDeadInterval_Object = MibTableColumn
snOspfVirtIfStatusRtrDeadInterval = _SnOspfVirtIfStatusRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 7),
    _SnOspfVirtIfStatusRtrDeadInterval_Type()
)
snOspfVirtIfStatusRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusRtrDeadInterval.setStatus("mandatory")


class _SnOspfVirtIfStatusState_Type(Integer32):
    """Custom type snOspfVirtIfStatusState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_SnOspfVirtIfStatusState_Type.__name__ = "Integer32"
_SnOspfVirtIfStatusState_Object = MibTableColumn
snOspfVirtIfStatusState = _SnOspfVirtIfStatusState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 8),
    _SnOspfVirtIfStatusState_Type()
)
snOspfVirtIfStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusState.setStatus("mandatory")
_SnOspfVirtIfStatusEvents_Type = Counter32
_SnOspfVirtIfStatusEvents_Object = MibTableColumn
snOspfVirtIfStatusEvents = _SnOspfVirtIfStatusEvents_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 9),
    _SnOspfVirtIfStatusEvents_Type()
)
snOspfVirtIfStatusEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusEvents.setStatus("mandatory")


class _SnOspfVirtIfStatusAuthType_Type(Integer32):
    """Custom type snOspfVirtIfStatusAuthType based on Integer32"""
    defaultValue = 0


_SnOspfVirtIfStatusAuthType_Object = MibTableColumn
snOspfVirtIfStatusAuthType = _SnOspfVirtIfStatusAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 10),
    _SnOspfVirtIfStatusAuthType_Type()
)
snOspfVirtIfStatusAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusAuthType.setStatus("mandatory")


class _SnOspfVirtIfStatusAuthKey_Type(OctetString):
    """Custom type snOspfVirtIfStatusAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnOspfVirtIfStatusAuthKey_Type.__name__ = "OctetString"
_SnOspfVirtIfStatusAuthKey_Object = MibTableColumn
snOspfVirtIfStatusAuthKey = _SnOspfVirtIfStatusAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 11),
    _SnOspfVirtIfStatusAuthKey_Type()
)
snOspfVirtIfStatusAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusAuthKey.setStatus("mandatory")


class _SnOspfVirtIfStatusMd5AuthKeyId_Type(Integer32):
    """Custom type snOspfVirtIfStatusMd5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnOspfVirtIfStatusMd5AuthKeyId_Type.__name__ = "Integer32"
_SnOspfVirtIfStatusMd5AuthKeyId_Object = MibTableColumn
snOspfVirtIfStatusMd5AuthKeyId = _SnOspfVirtIfStatusMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 12),
    _SnOspfVirtIfStatusMd5AuthKeyId_Type()
)
snOspfVirtIfStatusMd5AuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusMd5AuthKeyId.setStatus("mandatory")


class _SnOspfVirtIfStatusMd5AuthKey_Type(OctetString):
    """Custom type snOspfVirtIfStatusMd5AuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnOspfVirtIfStatusMd5AuthKey_Type.__name__ = "OctetString"
_SnOspfVirtIfStatusMd5AuthKey_Object = MibTableColumn
snOspfVirtIfStatusMd5AuthKey = _SnOspfVirtIfStatusMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 13),
    _SnOspfVirtIfStatusMd5AuthKey_Type()
)
snOspfVirtIfStatusMd5AuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusMd5AuthKey.setStatus("mandatory")


class _SnOspfVirtIfStatusMd5ActivationWaitTime_Type(Integer32):
    """Custom type snOspfVirtIfStatusMd5ActivationWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_SnOspfVirtIfStatusMd5ActivationWaitTime_Type.__name__ = "Integer32"
_SnOspfVirtIfStatusMd5ActivationWaitTime_Object = MibTableColumn
snOspfVirtIfStatusMd5ActivationWaitTime = _SnOspfVirtIfStatusMd5ActivationWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 14),
    _SnOspfVirtIfStatusMd5ActivationWaitTime_Type()
)
snOspfVirtIfStatusMd5ActivationWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusMd5ActivationWaitTime.setStatus("mandatory")


class _SnOspfVirtIfStatusAreaIdFormat_Type(Integer32):
    """Custom type snOspfVirtIfStatusAreaIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integer", 0),
          ("ipAddress", 1))
    )


_SnOspfVirtIfStatusAreaIdFormat_Type.__name__ = "Integer32"
_SnOspfVirtIfStatusAreaIdFormat_Object = MibTableColumn
snOspfVirtIfStatusAreaIdFormat = _SnOspfVirtIfStatusAreaIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 13, 1, 1, 15),
    _SnOspfVirtIfStatusAreaIdFormat_Type()
)
snOspfVirtIfStatusAreaIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfVirtIfStatusAreaIdFormat.setStatus("mandatory")
_SnOspfRoutingInfo_ObjectIdentity = ObjectIdentity
snOspfRoutingInfo = _SnOspfRoutingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 14)
)
_SnOspfRoutingInfoTable_Object = MibTable
snOspfRoutingInfoTable = _SnOspfRoutingInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 14, 1)
)
if mibBuilder.loadTexts:
    snOspfRoutingInfoTable.setStatus("mandatory")
_SnOspfRoutingInfoEntry_Object = MibTableRow
snOspfRoutingInfoEntry = _SnOspfRoutingInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 14, 1, 1)
)
snOspfRoutingInfoEntry.setIndexNames(
    (0, "FOUNDRY-SN-OSPF-GROUP-MIB", "snOspfRoutingInfoIndex"),
)
if mibBuilder.loadTexts:
    snOspfRoutingInfoEntry.setStatus("mandatory")
_SnOspfRoutingInfoIndex_Type = Integer32
_SnOspfRoutingInfoIndex_Object = MibTableColumn
snOspfRoutingInfoIndex = _SnOspfRoutingInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 14, 1, 1, 1),
    _SnOspfRoutingInfoIndex_Type()
)
snOspfRoutingInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfRoutingInfoIndex.setStatus("mandatory")
_SnOspfRoutingInfoRouterID_Type = RouterID
_SnOspfRoutingInfoRouterID_Object = MibTableColumn
snOspfRoutingInfoRouterID = _SnOspfRoutingInfoRouterID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 14, 1, 1, 2),
    _SnOspfRoutingInfoRouterID_Type()
)
snOspfRoutingInfoRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfRoutingInfoRouterID.setStatus("mandatory")


class _SnOspfRoutingInfoRouterType_Type(Integer32):
    """Custom type snOspfRoutingInfoRouterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abr", 1),
          ("abrANDasbr", 3),
          ("asbr", 2))
    )


_SnOspfRoutingInfoRouterType_Type.__name__ = "Integer32"
_SnOspfRoutingInfoRouterType_Object = MibTableColumn
snOspfRoutingInfoRouterType = _SnOspfRoutingInfoRouterType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 14, 1, 1, 3),
    _SnOspfRoutingInfoRouterType_Type()
)
snOspfRoutingInfoRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfRoutingInfoRouterType.setStatus("mandatory")
_SnOspfRoutingInfoNextHopRouterID_Type = RouterID
_SnOspfRoutingInfoNextHopRouterID_Object = MibTableColumn
snOspfRoutingInfoNextHopRouterID = _SnOspfRoutingInfoNextHopRouterID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 14, 1, 1, 4),
    _SnOspfRoutingInfoNextHopRouterID_Type()
)
snOspfRoutingInfoNextHopRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfRoutingInfoNextHopRouterID.setStatus("mandatory")
_SnOspfRoutingInfoOutgoingInterface_Type = Integer32
_SnOspfRoutingInfoOutgoingInterface_Object = MibTableColumn
snOspfRoutingInfoOutgoingInterface = _SnOspfRoutingInfoOutgoingInterface_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 14, 1, 1, 5),
    _SnOspfRoutingInfoOutgoingInterface_Type()
)
snOspfRoutingInfoOutgoingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfRoutingInfoOutgoingInterface.setStatus("mandatory")
_SnOspfTrapControl_ObjectIdentity = ObjectIdentity
snOspfTrapControl = _SnOspfTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 15)
)


class _SnOspfSetTrap_Type(OctetString):
    """Custom type snOspfSetTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SnOspfSetTrap_Type.__name__ = "OctetString"
_SnOspfSetTrap_Object = MibScalar
snOspfSetTrap = _SnOspfSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 15, 1),
    _SnOspfSetTrap_Type()
)
snOspfSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfSetTrap.setStatus("mandatory")


class _SnOspfConfigErrorType_Type(Integer32):
    """Custom type snOspfConfigErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("areaMismatch", 2),
          ("authFailure", 6),
          ("authTypeMismatch", 5),
          ("badVersion", 1),
          ("deadIntervalMismatch", 9),
          ("helloIntervalMismatch", 8),
          ("netMaskMismatch", 7),
          ("optionMismatch", 10),
          ("unUsed", 0),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4))
    )


_SnOspfConfigErrorType_Type.__name__ = "Integer32"
_SnOspfConfigErrorType_Object = MibScalar
snOspfConfigErrorType = _SnOspfConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 15, 2),
    _SnOspfConfigErrorType_Type()
)
snOspfConfigErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfConfigErrorType.setStatus("mandatory")


class _SnOspfPacketType_Type(Integer32):
    """Custom type snOspfPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dbDescript", 2),
          ("hello", 1),
          ("lsAck", 5),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("unUsed", 0))
    )


_SnOspfPacketType_Type.__name__ = "Integer32"
_SnOspfPacketType_Object = MibScalar
snOspfPacketType = _SnOspfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 15, 3),
    _SnOspfPacketType_Type()
)
snOspfPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfPacketType.setStatus("mandatory")
_SnOspfPacketSrc_Type = IpAddress
_SnOspfPacketSrc_Object = MibScalar
snOspfPacketSrc = _SnOspfPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 15, 4),
    _SnOspfPacketSrc_Type()
)
snOspfPacketSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snOspfPacketSrc.setStatus("mandatory")
_SnOspfTrapsGenerationMode_Type = RtrStatus
_SnOspfTrapsGenerationMode_Object = MibScalar
snOspfTrapsGenerationMode = _SnOspfTrapsGenerationMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 4, 15, 5),
    _SnOspfTrapsGenerationMode_Type()
)
snOspfTrapsGenerationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snOspfTrapsGenerationMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-OSPF-GROUP-MIB",
    **{"AreaID": AreaID,
       "RouterID": RouterID,
       "Metric": Metric,
       "BigMetric": BigMetric,
       "TruthVal": TruthVal,
       "RtrStatus": RtrStatus,
       "PositiveInteger": PositiveInteger,
       "HelloRange": HelloRange,
       "UpToMaxAge": UpToMaxAge,
       "DesignatedRouterPriority": DesignatedRouterPriority,
       "TOSType": TOSType,
       "snOspfGen": snOspfGen,
       "snOspfRouterId": snOspfRouterId,
       "snOspfAdminStat": snOspfAdminStat,
       "snOspfASBdrRtrStatus": snOspfASBdrRtrStatus,
       "snOspfRedisMode": snOspfRedisMode,
       "snOspfDefaultOspfMetricValue": snOspfDefaultOspfMetricValue,
       "snOspfExternLSACount": snOspfExternLSACount,
       "snOspfExternLSACksumSum": snOspfExternLSACksumSum,
       "snOspfOriginateNewLSAs": snOspfOriginateNewLSAs,
       "snOspfRxNewLSAs": snOspfRxNewLSAs,
       "snOspfOspfRedisMetricType": snOspfOspfRedisMetricType,
       "snOspfExtLsdbLimit": snOspfExtLsdbLimit,
       "snOspfExitOverflowInterval": snOspfExitOverflowInterval,
       "snOspfRfc1583Compatibility": snOspfRfc1583Compatibility,
       "snOspfRouterIdFormat": snOspfRouterIdFormat,
       "snOspfDistance": snOspfDistance,
       "snOspfDistanceIntra": snOspfDistanceIntra,
       "snOspfDistanceInter": snOspfDistanceInter,
       "snOspfDistanceExternal": snOspfDistanceExternal,
       "snOspfArea": snOspfArea,
       "snOspfAreaTable": snOspfAreaTable,
       "snOspfAreaEntry": snOspfAreaEntry,
       "snOspfAreaId": snOspfAreaId,
       "snOspfImportASExtern": snOspfImportASExtern,
       "snOspfStubMetric": snOspfStubMetric,
       "snOspfAreaRowStatus": snOspfAreaRowStatus,
       "snOspfAreaIdFormat": snOspfAreaIdFormat,
       "snOspfAddrRange": snOspfAddrRange,
       "snOspfAreaRangeTable": snOspfAreaRangeTable,
       "snOspfAreaRangeEntry": snOspfAreaRangeEntry,
       "snOspfAreaRangeAreaID": snOspfAreaRangeAreaID,
       "snOspfAreaRangeNet": snOspfAreaRangeNet,
       "snOspfAreaRangeMask": snOspfAreaRangeMask,
       "snOspfAreaRangeRowStatus": snOspfAreaRangeRowStatus,
       "snOspfAreaRangeAreaIdFormat": snOspfAreaRangeAreaIdFormat,
       "snOspfIntf": snOspfIntf,
       "snOspfIfTable": snOspfIfTable,
       "snOspfIfEntry": snOspfIfEntry,
       "snOspfIfPort": snOspfIfPort,
       "snOspfIfAreaId": snOspfIfAreaId,
       "snOspfIfAdminStat": snOspfIfAdminStat,
       "snOspfIfRtrPriority": snOspfIfRtrPriority,
       "snOspfIfTransitDelay": snOspfIfTransitDelay,
       "snOspfIfRetransInterval": snOspfIfRetransInterval,
       "snOspfIfHelloInterval": snOspfIfHelloInterval,
       "snOspfIfRtrDeadInterval": snOspfIfRtrDeadInterval,
       "snOspfIfAuthType": snOspfIfAuthType,
       "snOspfIfAuthKey": snOspfIfAuthKey,
       "snOspfIfMetricValue": snOspfIfMetricValue,
       "snOspfIfRowStatus": snOspfIfRowStatus,
       "snOspfIfMd5AuthKeyId": snOspfIfMd5AuthKeyId,
       "snOspfIfMd5AuthKey": snOspfIfMd5AuthKey,
       "snOspfIfMd5ActivationWaitTime": snOspfIfMd5ActivationWaitTime,
       "snOspfIfAreaIdFormat": snOspfIfAreaIdFormat,
       "snOspfIfPassiveMode": snOspfIfPassiveMode,
       "snOspfIfDatabaseFilterAllOut": snOspfIfDatabaseFilterAllOut,
       "snOspfIfMtuIgnore": snOspfIfMtuIgnore,
       "snOspfIfNetworkP2mp": snOspfIfNetworkP2mp,
       "snOspfIf2Table": snOspfIf2Table,
       "snOspfIf2Entry": snOspfIf2Entry,
       "snOspfIf2Port": snOspfIf2Port,
       "snOspfIf2AreaId": snOspfIf2AreaId,
       "snOspfIf2AdminStat": snOspfIf2AdminStat,
       "snOspfIf2RtrPriority": snOspfIf2RtrPriority,
       "snOspfIf2TransitDelay": snOspfIf2TransitDelay,
       "snOspfIf2RetransInterval": snOspfIf2RetransInterval,
       "snOspfIf2HelloInterval": snOspfIf2HelloInterval,
       "snOspfIf2RtrDeadInterval": snOspfIf2RtrDeadInterval,
       "snOspfIf2AuthType": snOspfIf2AuthType,
       "snOspfIf2AuthKey": snOspfIf2AuthKey,
       "snOspfIf2MetricValue": snOspfIf2MetricValue,
       "snOspfIf2RowStatus": snOspfIf2RowStatus,
       "snOspfIf2Md5AuthKeyId": snOspfIf2Md5AuthKeyId,
       "snOspfIf2Md5AuthKey": snOspfIf2Md5AuthKey,
       "snOspfIf2Md5ActivationWaitTime": snOspfIf2Md5ActivationWaitTime,
       "snOspfIf2AreaIdFormat": snOspfIf2AreaIdFormat,
       "snOspfIf2PassiveMode": snOspfIf2PassiveMode,
       "snOspfIf2DatabaseFilterAllOut": snOspfIf2DatabaseFilterAllOut,
       "snOspfIf2MtuIgnore": snOspfIf2MtuIgnore,
       "snOspfIf2NetworkP2mp": snOspfIf2NetworkP2mp,
       "snOspfVirtIf": snOspfVirtIf,
       "snOspfVirtIfTable": snOspfVirtIfTable,
       "snOspfVirtIfEntry": snOspfVirtIfEntry,
       "snOspfVirtIfAreaID": snOspfVirtIfAreaID,
       "snOspfVirtIfNeighbor": snOspfVirtIfNeighbor,
       "snOspfVirtIfTransitDelay": snOspfVirtIfTransitDelay,
       "snOspfVirtIfRetransInterval": snOspfVirtIfRetransInterval,
       "snOspfVirtIfHelloInterval": snOspfVirtIfHelloInterval,
       "snOspfVirtIfRtrDeadInterval": snOspfVirtIfRtrDeadInterval,
       "snOspfVirtIfAuthType": snOspfVirtIfAuthType,
       "snOspfVirtIfAuthKey": snOspfVirtIfAuthKey,
       "snOspfVirtIfRowStatus": snOspfVirtIfRowStatus,
       "snOspfVirtIfMd5AuthKeyId": snOspfVirtIfMd5AuthKeyId,
       "snOspfVirtIfMd5AuthKey": snOspfVirtIfMd5AuthKey,
       "snOspfVirtIfMd5ActivationWaitTime": snOspfVirtIfMd5ActivationWaitTime,
       "snOspfVirtIfAreaIdFormat": snOspfVirtIfAreaIdFormat,
       "snOspfRedis": snOspfRedis,
       "snOspfRedisTable": snOspfRedisTable,
       "snOspfRedisEntry": snOspfRedisEntry,
       "snOspfRedisIndex": snOspfRedisIndex,
       "snOspfRedisIpAddress": snOspfRedisIpAddress,
       "snOspfRedisMask": snOspfRedisMask,
       "snOspfRedisAction": snOspfRedisAction,
       "snOspfRedisProtocol": snOspfRedisProtocol,
       "snOspfRedisSetOspfMetric": snOspfRedisSetOspfMetric,
       "snOspfRedisOspfMetricValue": snOspfRedisOspfMetricValue,
       "snOspfRedisMatchRipMetric": snOspfRedisMatchRipMetric,
       "snOspfRedisRipMetricValue": snOspfRedisRipMetricValue,
       "snOspfRedisRowStatus": snOspfRedisRowStatus,
       "snOspfNbr": snOspfNbr,
       "snOspfNbrTable": snOspfNbrTable,
       "snOspfNbrEntry": snOspfNbrEntry,
       "snOspfNbrEntryIndex": snOspfNbrEntryIndex,
       "snOspfNbrPort": snOspfNbrPort,
       "snOspfNbrIpAddr": snOspfNbrIpAddr,
       "snOspfNbrIndex": snOspfNbrIndex,
       "snOspfNbrRtrId": snOspfNbrRtrId,
       "snOspfNbrOptions": snOspfNbrOptions,
       "snOspfNbrPriority": snOspfNbrPriority,
       "snOspfNbrState": snOspfNbrState,
       "snOspfNbrEvents": snOspfNbrEvents,
       "snOspfNbrLsRetransQLen": snOspfNbrLsRetransQLen,
       "snOspfVirtNbr": snOspfVirtNbr,
       "snOspfVirtNbrTable": snOspfVirtNbrTable,
       "snOspfVirtNbrEntry": snOspfVirtNbrEntry,
       "snOspfVirtNbrEntryIndex": snOspfVirtNbrEntryIndex,
       "snOspfVirtNbrArea": snOspfVirtNbrArea,
       "snOspfVirtNbrRtrId": snOspfVirtNbrRtrId,
       "snOspfVirtNbrIpAddr": snOspfVirtNbrIpAddr,
       "snOspfVirtNbrOptions": snOspfVirtNbrOptions,
       "snOspfVirtNbrState": snOspfVirtNbrState,
       "snOspfVirtNbrEvents": snOspfVirtNbrEvents,
       "snOspfVirtNbrLSRetransQLen": snOspfVirtNbrLSRetransQLen,
       "snOspfVirtNbrAreaIdFormat": snOspfVirtNbrAreaIdFormat,
       "snOspfLsdb": snOspfLsdb,
       "snOspfLsdbTable": snOspfLsdbTable,
       "snOspfLsdbEntry": snOspfLsdbEntry,
       "snOspfLsdbEntryIndex": snOspfLsdbEntryIndex,
       "snOspfLsdbAreaId": snOspfLsdbAreaId,
       "snOspfLsdbType": snOspfLsdbType,
       "snOspfLsdbLsId": snOspfLsdbLsId,
       "snOspfLsdbRouterId": snOspfLsdbRouterId,
       "snOspfLsdbSequence": snOspfLsdbSequence,
       "snOspfLsdbAge": snOspfLsdbAge,
       "snOspfLsdbChecksum": snOspfLsdbChecksum,
       "snOspfLsdbAdvertisement": snOspfLsdbAdvertisement,
       "snOspfLsdbAreaIdFormat": snOspfLsdbAreaIdFormat,
       "snOspfExtLsdb": snOspfExtLsdb,
       "snOspfExtLsdbTable": snOspfExtLsdbTable,
       "snOspfExtLsdbEntry": snOspfExtLsdbEntry,
       "snOspfExtLsdbEntryIndex": snOspfExtLsdbEntryIndex,
       "snOspfExtLsdbType": snOspfExtLsdbType,
       "snOspfExtLsdbLsId": snOspfExtLsdbLsId,
       "snOspfExtLsdbRouterId": snOspfExtLsdbRouterId,
       "snOspfExtLsdbSequence": snOspfExtLsdbSequence,
       "snOspfExtLsdbAge": snOspfExtLsdbAge,
       "snOspfExtLsdbChecksum": snOspfExtLsdbChecksum,
       "snOspfExtLsdbAdvertisement": snOspfExtLsdbAdvertisement,
       "snOspfAreaStatus": snOspfAreaStatus,
       "snOspfAreaStatusTable": snOspfAreaStatusTable,
       "snOspfAreaStatusEntry": snOspfAreaStatusEntry,
       "snOspfAreaStatusEntryIndex": snOspfAreaStatusEntryIndex,
       "snOspfAreaStatusAreaId": snOspfAreaStatusAreaId,
       "snOspfAreaStatusImportASExtern": snOspfAreaStatusImportASExtern,
       "snOspfAreaStatusStubMetric": snOspfAreaStatusStubMetric,
       "snOspfAreaStatusSpfRuns": snOspfAreaStatusSpfRuns,
       "snOspfAreaStatusAreaBdrRtrCount": snOspfAreaStatusAreaBdrRtrCount,
       "snOspfAreaStatusASBdrRtrCount": snOspfAreaStatusASBdrRtrCount,
       "snOspfAreaStatusLSACount": snOspfAreaStatusLSACount,
       "snOspfAreaStatusLSACksumSum": snOspfAreaStatusLSACksumSum,
       "snOspfAreaStatusAreaIdFormat": snOspfAreaStatusAreaIdFormat,
       "snOspfIfStatus": snOspfIfStatus,
       "snOspfIfStatusTable": snOspfIfStatusTable,
       "snOspfIfStatusEntry": snOspfIfStatusEntry,
       "snOspfIfStatusEntryIndex": snOspfIfStatusEntryIndex,
       "snOspfIfStatusPort": snOspfIfStatusPort,
       "snOspfIfStatusIpAddress": snOspfIfStatusIpAddress,
       "snOspfIfStatusAreaId": snOspfIfStatusAreaId,
       "snOspfIfStatusType": snOspfIfStatusType,
       "snOspfIfStatusAdminStat": snOspfIfStatusAdminStat,
       "snOspfIfStatusRtrPriority": snOspfIfStatusRtrPriority,
       "snOspfIfStatusTransitDelay": snOspfIfStatusTransitDelay,
       "snOspfIfStatusRetransInterval": snOspfIfStatusRetransInterval,
       "snOspfIfStatusHelloInterval": snOspfIfStatusHelloInterval,
       "snOspfIfStatusRtrDeadInterval": snOspfIfStatusRtrDeadInterval,
       "snOspfIfStatusState": snOspfIfStatusState,
       "snOspfIfStatusDesignatedRouter": snOspfIfStatusDesignatedRouter,
       "snOspfIfStatusBackupDesignatedRouter": snOspfIfStatusBackupDesignatedRouter,
       "snOspfIfStatusEvents": snOspfIfStatusEvents,
       "snOspfIfStatusAuthType": snOspfIfStatusAuthType,
       "snOspfIfStatusAuthKey": snOspfIfStatusAuthKey,
       "snOspfIfStatusMetricValue": snOspfIfStatusMetricValue,
       "snOspfIfStatusMd5AuthKeyId": snOspfIfStatusMd5AuthKeyId,
       "snOspfIfStatusMd5AuthKey": snOspfIfStatusMd5AuthKey,
       "snOspfIfStatusMd5ActivationWaitTime": snOspfIfStatusMd5ActivationWaitTime,
       "snOspfIfStatusAreaIdFormat": snOspfIfStatusAreaIdFormat,
       "snOspfVirtIfStatus": snOspfVirtIfStatus,
       "snOspfVirtIfStatusTable": snOspfVirtIfStatusTable,
       "snOspfVirtIfStatusEntry": snOspfVirtIfStatusEntry,
       "snOspfVirtIfStatusEntryIndex": snOspfVirtIfStatusEntryIndex,
       "snOspfVirtIfStatusAreaID": snOspfVirtIfStatusAreaID,
       "snOspfVirtIfStatusNeighbor": snOspfVirtIfStatusNeighbor,
       "snOspfVirtIfStatusTransitDelay": snOspfVirtIfStatusTransitDelay,
       "snOspfVirtIfStatusRetransInterval": snOspfVirtIfStatusRetransInterval,
       "snOspfVirtIfStatusHelloInterval": snOspfVirtIfStatusHelloInterval,
       "snOspfVirtIfStatusRtrDeadInterval": snOspfVirtIfStatusRtrDeadInterval,
       "snOspfVirtIfStatusState": snOspfVirtIfStatusState,
       "snOspfVirtIfStatusEvents": snOspfVirtIfStatusEvents,
       "snOspfVirtIfStatusAuthType": snOspfVirtIfStatusAuthType,
       "snOspfVirtIfStatusAuthKey": snOspfVirtIfStatusAuthKey,
       "snOspfVirtIfStatusMd5AuthKeyId": snOspfVirtIfStatusMd5AuthKeyId,
       "snOspfVirtIfStatusMd5AuthKey": snOspfVirtIfStatusMd5AuthKey,
       "snOspfVirtIfStatusMd5ActivationWaitTime": snOspfVirtIfStatusMd5ActivationWaitTime,
       "snOspfVirtIfStatusAreaIdFormat": snOspfVirtIfStatusAreaIdFormat,
       "snOspfRoutingInfo": snOspfRoutingInfo,
       "snOspfRoutingInfoTable": snOspfRoutingInfoTable,
       "snOspfRoutingInfoEntry": snOspfRoutingInfoEntry,
       "snOspfRoutingInfoIndex": snOspfRoutingInfoIndex,
       "snOspfRoutingInfoRouterID": snOspfRoutingInfoRouterID,
       "snOspfRoutingInfoRouterType": snOspfRoutingInfoRouterType,
       "snOspfRoutingInfoNextHopRouterID": snOspfRoutingInfoNextHopRouterID,
       "snOspfRoutingInfoOutgoingInterface": snOspfRoutingInfoOutgoingInterface,
       "snOspfTrapControl": snOspfTrapControl,
       "snOspfSetTrap": snOspfSetTrap,
       "snOspfConfigErrorType": snOspfConfigErrorType,
       "snOspfPacketType": snOspfPacketType,
       "snOspfPacketSrc": snOspfPacketSrc,
       "snOspfTrapsGenerationMode": snOspfTrapsGenerationMode}
)

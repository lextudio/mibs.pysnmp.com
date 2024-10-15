# SNMP MIB module (HP-ICF-OSPFV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-OSPFV3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:56 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(HpicfOspfLogAction,
 HpicfOspfLogType) = mibBuilder.importSymbols(
    "HP-ICF-OSPF",
    "HpicfOspfLogAction",
    "HpicfOspfLogType")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(BigMetric,
 Metric) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "BigMetric",
    "Metric")

(Ospfv3RouterIdTC,
 ospfv3AreaAggregateEntry,
 ospfv3AreaEntry,
 ospfv3AreaLsdbAreaId,
 ospfv3AreaLsdbEntry,
 ospfv3AreaLsdbLsid,
 ospfv3AreaLsdbRouterId,
 ospfv3AreaLsdbType,
 ospfv3AsLsdbEntry,
 ospfv3IfEntry,
 ospfv3IfIndex,
 ospfv3IfInstId,
 ospfv3LinkLsdbEntry,
 ospfv3LinkLsdbIfIndex,
 ospfv3LinkLsdbIfInstId,
 ospfv3LinkLsdbLsid,
 ospfv3LinkLsdbRouterId,
 ospfv3LinkLsdbType,
 ospfv3NbrEntry) = mibBuilder.importSymbols(
    "OSPFV3-MIB",
    "Ospfv3RouterIdTC",
    "ospfv3AreaAggregateEntry",
    "ospfv3AreaEntry",
    "ospfv3AreaLsdbAreaId",
    "ospfv3AreaLsdbEntry",
    "ospfv3AreaLsdbLsid",
    "ospfv3AreaLsdbRouterId",
    "ospfv3AreaLsdbType",
    "ospfv3AsLsdbEntry",
    "ospfv3IfEntry",
    "ospfv3IfIndex",
    "ospfv3IfInstId",
    "ospfv3LinkLsdbEntry",
    "ospfv3LinkLsdbIfIndex",
    "ospfv3LinkLsdbIfInstId",
    "ospfv3LinkLsdbLsid",
    "ospfv3LinkLsdbRouterId",
    "ospfv3LinkLsdbType",
    "ospfv3NbrEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfOspfv3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44)
)
hpicfOspfv3MIB.setRevisions(
        ("2017-05-18 00:00",
         "2014-06-13 00:00",
         "2012-04-30 00:00",
         "2012-04-20 00:00",
         "2011-06-13 19:53",
         "2010-11-04 00:00",
         "2009-02-05 18:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfOspfv3Objects_ObjectIdentity = ObjectIdentity
hpicfOspfv3Objects = _HpicfOspfv3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1)
)
_HpicfOspfv3GeneralGroup_ObjectIdentity = ObjectIdentity
hpicfOspfv3GeneralGroup = _HpicfOspfv3GeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1)
)
_HpicfOspfv3DefaultImportMetric_Type = BigMetric
_HpicfOspfv3DefaultImportMetric_Object = MibScalar
hpicfOspfv3DefaultImportMetric = _HpicfOspfv3DefaultImportMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 1),
    _HpicfOspfv3DefaultImportMetric_Type()
)
hpicfOspfv3DefaultImportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3DefaultImportMetric.setStatus("current")


class _HpicfOspfv3DefaultImportMetricType_Type(Integer32):
    """Custom type hpicfOspfv3DefaultImportMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalType1", 1),
          ("externalType2", 2))
    )


_HpicfOspfv3DefaultImportMetricType_Type.__name__ = "Integer32"
_HpicfOspfv3DefaultImportMetricType_Object = MibScalar
hpicfOspfv3DefaultImportMetricType = _HpicfOspfv3DefaultImportMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 2),
    _HpicfOspfv3DefaultImportMetricType_Type()
)
hpicfOspfv3DefaultImportMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3DefaultImportMetricType.setStatus("current")


class _HpicfOspfv3IntraAreaDistance_Type(Integer32):
    """Custom type hpicfOspfv3IntraAreaDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfOspfv3IntraAreaDistance_Type.__name__ = "Integer32"
_HpicfOspfv3IntraAreaDistance_Object = MibScalar
hpicfOspfv3IntraAreaDistance = _HpicfOspfv3IntraAreaDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 3),
    _HpicfOspfv3IntraAreaDistance_Type()
)
hpicfOspfv3IntraAreaDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3IntraAreaDistance.setStatus("current")


class _HpicfOspfv3InterAreaDistance_Type(Integer32):
    """Custom type hpicfOspfv3InterAreaDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfOspfv3InterAreaDistance_Type.__name__ = "Integer32"
_HpicfOspfv3InterAreaDistance_Object = MibScalar
hpicfOspfv3InterAreaDistance = _HpicfOspfv3InterAreaDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 4),
    _HpicfOspfv3InterAreaDistance_Type()
)
hpicfOspfv3InterAreaDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3InterAreaDistance.setStatus("current")


class _HpicfOspfv3ExternalDistance_Type(Integer32):
    """Custom type hpicfOspfv3ExternalDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfOspfv3ExternalDistance_Type.__name__ = "Integer32"
_HpicfOspfv3ExternalDistance_Object = MibScalar
hpicfOspfv3ExternalDistance = _HpicfOspfv3ExternalDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 5),
    _HpicfOspfv3ExternalDistance_Type()
)
hpicfOspfv3ExternalDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3ExternalDistance.setStatus("current")


class _HpicfOspfv3SpfThrottleStartInterval_Type(Integer32):
    """Custom type hpicfOspfv3SpfThrottleStartInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HpicfOspfv3SpfThrottleStartInterval_Type.__name__ = "Integer32"
_HpicfOspfv3SpfThrottleStartInterval_Object = MibScalar
hpicfOspfv3SpfThrottleStartInterval = _HpicfOspfv3SpfThrottleStartInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 7),
    _HpicfOspfv3SpfThrottleStartInterval_Type()
)
hpicfOspfv3SpfThrottleStartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3SpfThrottleStartInterval.setStatus("current")


class _HpicfOspfv3SpfThrottleWaitInterval_Type(Integer32):
    """Custom type hpicfOspfv3SpfThrottleWaitInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HpicfOspfv3SpfThrottleWaitInterval_Type.__name__ = "Integer32"
_HpicfOspfv3SpfThrottleWaitInterval_Object = MibScalar
hpicfOspfv3SpfThrottleWaitInterval = _HpicfOspfv3SpfThrottleWaitInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 8),
    _HpicfOspfv3SpfThrottleWaitInterval_Type()
)
hpicfOspfv3SpfThrottleWaitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3SpfThrottleWaitInterval.setStatus("current")


class _HpicfOspfv3SpfThrottleMaxWaitTime_Type(Integer32):
    """Custom type hpicfOspfv3SpfThrottleMaxWaitTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HpicfOspfv3SpfThrottleMaxWaitTime_Type.__name__ = "Integer32"
_HpicfOspfv3SpfThrottleMaxWaitTime_Object = MibScalar
hpicfOspfv3SpfThrottleMaxWaitTime = _HpicfOspfv3SpfThrottleMaxWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 9),
    _HpicfOspfv3SpfThrottleMaxWaitTime_Type()
)
hpicfOspfv3SpfThrottleMaxWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3SpfThrottleMaxWaitTime.setStatus("current")
_HpicfOspfv3SpfThrottleCurrentSpfInterval_Type = Unsigned32
_HpicfOspfv3SpfThrottleCurrentSpfInterval_Object = MibScalar
hpicfOspfv3SpfThrottleCurrentSpfInterval = _HpicfOspfv3SpfThrottleCurrentSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 10),
    _HpicfOspfv3SpfThrottleCurrentSpfInterval_Type()
)
hpicfOspfv3SpfThrottleCurrentSpfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3SpfThrottleCurrentSpfInterval.setStatus("current")
_HpicfOspfv3AreaCount_Type = Unsigned32
_HpicfOspfv3AreaCount_Object = MibScalar
hpicfOspfv3AreaCount = _HpicfOspfv3AreaCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 11),
    _HpicfOspfv3AreaCount_Type()
)
hpicfOspfv3AreaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaCount.setStatus("current")


class _HpicfOspfv3RestartHelper_Type(TruthValue):
    """Custom type hpicfOspfv3RestartHelper based on TruthValue"""


_HpicfOspfv3RestartHelper_Object = MibScalar
hpicfOspfv3RestartHelper = _HpicfOspfv3RestartHelper_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 12),
    _HpicfOspfv3RestartHelper_Type()
)
hpicfOspfv3RestartHelper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3RestartHelper.setStatus("current")


class _HpicfOspfv3ASscopeUnknownLsaCount_Type(Counter32):
    """Custom type hpicfOspfv3ASscopeUnknownLsaCount based on Counter32"""
    defaultValue = 0


_HpicfOspfv3ASscopeUnknownLsaCount_Object = MibScalar
hpicfOspfv3ASscopeUnknownLsaCount = _HpicfOspfv3ASscopeUnknownLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 13),
    _HpicfOspfv3ASscopeUnknownLsaCount_Type()
)
hpicfOspfv3ASscopeUnknownLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3ASscopeUnknownLsaCount.setStatus("current")


class _HpicfOspfv3LinkLsdbStatLinkLsa_Type(Counter32):
    """Custom type hpicfOspfv3LinkLsdbStatLinkLsa based on Counter32"""
    defaultValue = 0


_HpicfOspfv3LinkLsdbStatLinkLsa_Object = MibScalar
hpicfOspfv3LinkLsdbStatLinkLsa = _HpicfOspfv3LinkLsdbStatLinkLsa_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 14),
    _HpicfOspfv3LinkLsdbStatLinkLsa_Type()
)
hpicfOspfv3LinkLsdbStatLinkLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3LinkLsdbStatLinkLsa.setStatus("current")


class _HpicfOspfv3TotalUnknownLsa_Type(Unsigned32):
    """Custom type hpicfOspfv3TotalUnknownLsa based on Unsigned32"""
    defaultValue = 0


_HpicfOspfv3TotalUnknownLsa_Object = MibScalar
hpicfOspfv3TotalUnknownLsa = _HpicfOspfv3TotalUnknownLsa_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 15),
    _HpicfOspfv3TotalUnknownLsa_Type()
)
hpicfOspfv3TotalUnknownLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3TotalUnknownLsa.setStatus("current")
_HpicfOspfv3ReferenceCost_Type = Metric
_HpicfOspfv3ReferenceCost_Object = MibScalar
hpicfOspfv3ReferenceCost = _HpicfOspfv3ReferenceCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 1, 16),
    _HpicfOspfv3ReferenceCost_Type()
)
hpicfOspfv3ReferenceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3ReferenceCost.setStatus("current")
_HpicfOspfv3AsLsdbTable_Object = MibTable
hpicfOspfv3AsLsdbTable = _HpicfOspfv3AsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbTable.setStatus("current")
_HpicfOspfv3AsLsdbEntry_Object = MibTableRow
hpicfOspfv3AsLsdbEntry = _HpicfOspfv3AsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbEntry.setStatus("current")


class _HpicfOspfv3AsLsdbEFTFlags_Type(Bits):
    """Custom type hpicfOspfv3AsLsdbEFTFlags based on Bits"""
    namedValues = NamedValues(
        *(("bitE", 0),
          ("bitF", 1),
          ("bitT", 2))
    )

_HpicfOspfv3AsLsdbEFTFlags_Type.__name__ = "Bits"
_HpicfOspfv3AsLsdbEFTFlags_Object = MibTableColumn
hpicfOspfv3AsLsdbEFTFlags = _HpicfOspfv3AsLsdbEFTFlags_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2, 1, 1),
    _HpicfOspfv3AsLsdbEFTFlags_Type()
)
hpicfOspfv3AsLsdbEFTFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbEFTFlags.setStatus("current")
_HpicfOspfv3AsLsdbMetric_Type = Metric
_HpicfOspfv3AsLsdbMetric_Object = MibTableColumn
hpicfOspfv3AsLsdbMetric = _HpicfOspfv3AsLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2, 1, 2),
    _HpicfOspfv3AsLsdbMetric_Type()
)
hpicfOspfv3AsLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbMetric.setStatus("current")
_HpicfOspfv3AsLsdbPrefixLength_Type = Unsigned32
_HpicfOspfv3AsLsdbPrefixLength_Object = MibTableColumn
hpicfOspfv3AsLsdbPrefixLength = _HpicfOspfv3AsLsdbPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2, 1, 3),
    _HpicfOspfv3AsLsdbPrefixLength_Type()
)
hpicfOspfv3AsLsdbPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbPrefixLength.setStatus("current")
_HpicfOspfv3AsLsdbPrefixOptions_Type = Unsigned32
_HpicfOspfv3AsLsdbPrefixOptions_Object = MibTableColumn
hpicfOspfv3AsLsdbPrefixOptions = _HpicfOspfv3AsLsdbPrefixOptions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2, 1, 4),
    _HpicfOspfv3AsLsdbPrefixOptions_Type()
)
hpicfOspfv3AsLsdbPrefixOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbPrefixOptions.setStatus("current")
_HpicfOspfv3AsLsdbRefLsType_Type = Unsigned32
_HpicfOspfv3AsLsdbRefLsType_Object = MibTableColumn
hpicfOspfv3AsLsdbRefLsType = _HpicfOspfv3AsLsdbRefLsType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2, 1, 5),
    _HpicfOspfv3AsLsdbRefLsType_Type()
)
hpicfOspfv3AsLsdbRefLsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbRefLsType.setStatus("current")
_HpicfOspfv3AsLsdbAddrPrefix_Type = InetAddressIPv6
_HpicfOspfv3AsLsdbAddrPrefix_Object = MibTableColumn
hpicfOspfv3AsLsdbAddrPrefix = _HpicfOspfv3AsLsdbAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2, 1, 6),
    _HpicfOspfv3AsLsdbAddrPrefix_Type()
)
hpicfOspfv3AsLsdbAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbAddrPrefix.setStatus("current")
_HpicfOspfv3AsLsdbFwdingAddress_Type = InetAddressIPv6
_HpicfOspfv3AsLsdbFwdingAddress_Object = MibTableColumn
hpicfOspfv3AsLsdbFwdingAddress = _HpicfOspfv3AsLsdbFwdingAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2, 1, 7),
    _HpicfOspfv3AsLsdbFwdingAddress_Type()
)
hpicfOspfv3AsLsdbFwdingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbFwdingAddress.setStatus("current")
_HpicfOspfv3AsLsdbExtRouteTags_Type = Unsigned32
_HpicfOspfv3AsLsdbExtRouteTags_Object = MibTableColumn
hpicfOspfv3AsLsdbExtRouteTags = _HpicfOspfv3AsLsdbExtRouteTags_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2, 1, 8),
    _HpicfOspfv3AsLsdbExtRouteTags_Type()
)
hpicfOspfv3AsLsdbExtRouteTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbExtRouteTags.setStatus("current")
_HpicfOspfv3AsLsdbRefLsId_Type = Unsigned32
_HpicfOspfv3AsLsdbRefLsId_Object = MibTableColumn
hpicfOspfv3AsLsdbRefLsId = _HpicfOspfv3AsLsdbRefLsId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2, 1, 9),
    _HpicfOspfv3AsLsdbRefLsId_Type()
)
hpicfOspfv3AsLsdbRefLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbRefLsId.setStatus("current")
_HpicfOspfv3AsLsdbLsaLength_Type = Unsigned32
_HpicfOspfv3AsLsdbLsaLength_Object = MibTableColumn
hpicfOspfv3AsLsdbLsaLength = _HpicfOspfv3AsLsdbLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 2, 1, 10),
    _HpicfOspfv3AsLsdbLsaLength_Type()
)
hpicfOspfv3AsLsdbLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbLsaLength.setStatus("current")
_HpicfOspfv3AreaLsdbTable_Object = MibTable
hpicfOspfv3AreaLsdbTable = _HpicfOspfv3AreaLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbTable.setStatus("current")
_HpicfOspfv3AreaLsdbEntry_Object = MibTableRow
hpicfOspfv3AreaLsdbEntry = _HpicfOspfv3AreaLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbEntry.setStatus("current")


class _HpicfOspfv3AreaLsdbRtrCapBits_Type(Bits):
    """Custom type hpicfOspfv3AreaLsdbRtrCapBits based on Bits"""
    namedValues = NamedValues(
        *(("bitB", 2),
          ("bitE", 1),
          ("bitNt", 4),
          ("bitV", 0),
          ("bitW", 3))
    )

_HpicfOspfv3AreaLsdbRtrCapBits_Type.__name__ = "Bits"
_HpicfOspfv3AreaLsdbRtrCapBits_Object = MibTableColumn
hpicfOspfv3AreaLsdbRtrCapBits = _HpicfOspfv3AreaLsdbRtrCapBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 1),
    _HpicfOspfv3AreaLsdbRtrCapBits_Type()
)
hpicfOspfv3AreaLsdbRtrCapBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbRtrCapBits.setStatus("current")
_HpicfOspfv3AreaLsdbOptions_Type = Unsigned32
_HpicfOspfv3AreaLsdbOptions_Object = MibTableColumn
hpicfOspfv3AreaLsdbOptions = _HpicfOspfv3AreaLsdbOptions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 2),
    _HpicfOspfv3AreaLsdbOptions_Type()
)
hpicfOspfv3AreaLsdbOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbOptions.setStatus("current")
_HpicfOspfv3AreaLsdbMetric_Type = Metric
_HpicfOspfv3AreaLsdbMetric_Object = MibTableColumn
hpicfOspfv3AreaLsdbMetric = _HpicfOspfv3AreaLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 3),
    _HpicfOspfv3AreaLsdbMetric_Type()
)
hpicfOspfv3AreaLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbMetric.setStatus("current")
_HpicfOspfv3AreaLsdbPrefixLength_Type = Unsigned32
_HpicfOspfv3AreaLsdbPrefixLength_Object = MibTableColumn
hpicfOspfv3AreaLsdbPrefixLength = _HpicfOspfv3AreaLsdbPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 4),
    _HpicfOspfv3AreaLsdbPrefixLength_Type()
)
hpicfOspfv3AreaLsdbPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbPrefixLength.setStatus("current")
_HpicfOspfv3AreaLsdbPrefixOptions_Type = Unsigned32
_HpicfOspfv3AreaLsdbPrefixOptions_Object = MibTableColumn
hpicfOspfv3AreaLsdbPrefixOptions = _HpicfOspfv3AreaLsdbPrefixOptions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 5),
    _HpicfOspfv3AreaLsdbPrefixOptions_Type()
)
hpicfOspfv3AreaLsdbPrefixOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbPrefixOptions.setStatus("current")
_HpicfOspfv3AreaLsdbAddrPrefix_Type = InetAddressIPv6
_HpicfOspfv3AreaLsdbAddrPrefix_Object = MibTableColumn
hpicfOspfv3AreaLsdbAddrPrefix = _HpicfOspfv3AreaLsdbAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 6),
    _HpicfOspfv3AreaLsdbAddrPrefix_Type()
)
hpicfOspfv3AreaLsdbAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbAddrPrefix.setStatus("current")
_HpicfOspfv3AreaLsdbDstRtrId_Type = Ospfv3RouterIdTC
_HpicfOspfv3AreaLsdbDstRtrId_Object = MibTableColumn
hpicfOspfv3AreaLsdbDstRtrId = _HpicfOspfv3AreaLsdbDstRtrId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 7),
    _HpicfOspfv3AreaLsdbDstRtrId_Type()
)
hpicfOspfv3AreaLsdbDstRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbDstRtrId.setStatus("current")
_HpicfOspfv3AreaLsdbNumPrefixes_Type = Unsigned32
_HpicfOspfv3AreaLsdbNumPrefixes_Object = MibTableColumn
hpicfOspfv3AreaLsdbNumPrefixes = _HpicfOspfv3AreaLsdbNumPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 8),
    _HpicfOspfv3AreaLsdbNumPrefixes_Type()
)
hpicfOspfv3AreaLsdbNumPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbNumPrefixes.setStatus("current")
_HpicfOspfv3AreaLsdbRefLsType_Type = Unsigned32
_HpicfOspfv3AreaLsdbRefLsType_Object = MibTableColumn
hpicfOspfv3AreaLsdbRefLsType = _HpicfOspfv3AreaLsdbRefLsType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 9),
    _HpicfOspfv3AreaLsdbRefLsType_Type()
)
hpicfOspfv3AreaLsdbRefLsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbRefLsType.setStatus("current")
_HpicfOspfv3AreaLsdbRefLsId_Type = Unsigned32
_HpicfOspfv3AreaLsdbRefLsId_Object = MibTableColumn
hpicfOspfv3AreaLsdbRefLsId = _HpicfOspfv3AreaLsdbRefLsId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 10),
    _HpicfOspfv3AreaLsdbRefLsId_Type()
)
hpicfOspfv3AreaLsdbRefLsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbRefLsId.setStatus("current")
_HpicfOspfv3AreaLsdbRefAdvRtrId_Type = Ospfv3RouterIdTC
_HpicfOspfv3AreaLsdbRefAdvRtrId_Object = MibTableColumn
hpicfOspfv3AreaLsdbRefAdvRtrId = _HpicfOspfv3AreaLsdbRefAdvRtrId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 11),
    _HpicfOspfv3AreaLsdbRefAdvRtrId_Type()
)
hpicfOspfv3AreaLsdbRefAdvRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbRefAdvRtrId.setStatus("current")


class _HpicfOspfv3AreaLsdbEFTFlags_Type(Bits):
    """Custom type hpicfOspfv3AreaLsdbEFTFlags based on Bits"""
    namedValues = NamedValues(
        *(("bitE", 0),
          ("bitF", 1),
          ("bitT", 2))
    )

_HpicfOspfv3AreaLsdbEFTFlags_Type.__name__ = "Bits"
_HpicfOspfv3AreaLsdbEFTFlags_Object = MibTableColumn
hpicfOspfv3AreaLsdbEFTFlags = _HpicfOspfv3AreaLsdbEFTFlags_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 12),
    _HpicfOspfv3AreaLsdbEFTFlags_Type()
)
hpicfOspfv3AreaLsdbEFTFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbEFTFlags.setStatus("current")
_HpicfOspfv3AreaLsdbFwdingAddress_Type = InetAddressIPv6
_HpicfOspfv3AreaLsdbFwdingAddress_Object = MibTableColumn
hpicfOspfv3AreaLsdbFwdingAddress = _HpicfOspfv3AreaLsdbFwdingAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 13),
    _HpicfOspfv3AreaLsdbFwdingAddress_Type()
)
hpicfOspfv3AreaLsdbFwdingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbFwdingAddress.setStatus("current")
_HpicfOspfv3AreaLsdbExtRouteTags_Type = Unsigned32
_HpicfOspfv3AreaLsdbExtRouteTags_Object = MibTableColumn
hpicfOspfv3AreaLsdbExtRouteTags = _HpicfOspfv3AreaLsdbExtRouteTags_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 14),
    _HpicfOspfv3AreaLsdbExtRouteTags_Type()
)
hpicfOspfv3AreaLsdbExtRouteTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbExtRouteTags.setStatus("current")
_HpicfOspfv3AreaLsdbLsaLength_Type = Unsigned32
_HpicfOspfv3AreaLsdbLsaLength_Object = MibTableColumn
hpicfOspfv3AreaLsdbLsaLength = _HpicfOspfv3AreaLsdbLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 15),
    _HpicfOspfv3AreaLsdbLsaLength_Type()
)
hpicfOspfv3AreaLsdbLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbLsaLength.setStatus("current")
_HpicfOspfv3AreaLsdbLinks_Type = Counter32
_HpicfOspfv3AreaLsdbLinks_Object = MibTableColumn
hpicfOspfv3AreaLsdbLinks = _HpicfOspfv3AreaLsdbLinks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 3, 1, 16),
    _HpicfOspfv3AreaLsdbLinks_Type()
)
hpicfOspfv3AreaLsdbLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbLinks.setStatus("current")
_HpicfOspfv3LinkLsdbTable_Object = MibTable
hpicfOspfv3LinkLsdbTable = _HpicfOspfv3LinkLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfOspfv3LinkLsdbTable.setStatus("current")
_HpicfOspfv3LinkLsdbEntry_Object = MibTableRow
hpicfOspfv3LinkLsdbEntry = _HpicfOspfv3LinkLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfv3LinkLsdbEntry.setStatus("current")
_HpicfOspfv3LinkLsdbRtrPriority_Type = Unsigned32
_HpicfOspfv3LinkLsdbRtrPriority_Object = MibTableColumn
hpicfOspfv3LinkLsdbRtrPriority = _HpicfOspfv3LinkLsdbRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 4, 1, 1),
    _HpicfOspfv3LinkLsdbRtrPriority_Type()
)
hpicfOspfv3LinkLsdbRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3LinkLsdbRtrPriority.setStatus("current")
_HpicfOspfv3LinkLsdbOptions_Type = Unsigned32
_HpicfOspfv3LinkLsdbOptions_Object = MibTableColumn
hpicfOspfv3LinkLsdbOptions = _HpicfOspfv3LinkLsdbOptions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 4, 1, 2),
    _HpicfOspfv3LinkLsdbOptions_Type()
)
hpicfOspfv3LinkLsdbOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3LinkLsdbOptions.setStatus("current")
_HpicfOspfv3LinkLsdbLocalAddress_Type = InetAddressIPv6
_HpicfOspfv3LinkLsdbLocalAddress_Object = MibTableColumn
hpicfOspfv3LinkLsdbLocalAddress = _HpicfOspfv3LinkLsdbLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 4, 1, 3),
    _HpicfOspfv3LinkLsdbLocalAddress_Type()
)
hpicfOspfv3LinkLsdbLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3LinkLsdbLocalAddress.setStatus("current")
_HpicfOspfv3LinkLsdbNumPrefixes_Type = Unsigned32
_HpicfOspfv3LinkLsdbNumPrefixes_Object = MibTableColumn
hpicfOspfv3LinkLsdbNumPrefixes = _HpicfOspfv3LinkLsdbNumPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 4, 1, 4),
    _HpicfOspfv3LinkLsdbNumPrefixes_Type()
)
hpicfOspfv3LinkLsdbNumPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3LinkLsdbNumPrefixes.setStatus("current")
_HpicfOspfv3LinkLsdbLsaLength_Type = Unsigned32
_HpicfOspfv3LinkLsdbLsaLength_Object = MibTableColumn
hpicfOspfv3LinkLsdbLsaLength = _HpicfOspfv3LinkLsdbLsaLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 4, 1, 5),
    _HpicfOspfv3LinkLsdbLsaLength_Type()
)
hpicfOspfv3LinkLsdbLsaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3LinkLsdbLsaLength.setStatus("current")
_HpicfOspfv3IfTable_Object = MibTable
hpicfOspfv3IfTable = _HpicfOspfv3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfOspfv3IfTable.setStatus("current")
_HpicfOspfv3IfEntry_Object = MibTableRow
hpicfOspfv3IfEntry = _HpicfOspfv3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfv3IfEntry.setStatus("current")


class _HpicfOspfv3IfPassive_Type(TruthValue):
    """Custom type hpicfOspfv3IfPassive based on TruthValue"""


_HpicfOspfv3IfPassive_Object = MibTableColumn
hpicfOspfv3IfPassive = _HpicfOspfv3IfPassive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 5, 1, 1),
    _HpicfOspfv3IfPassive_Type()
)
hpicfOspfv3IfPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOspfv3IfPassive.setStatus("current")
_HpicfOspfv3IfNbrCount_Type = Unsigned32
_HpicfOspfv3IfNbrCount_Object = MibTableColumn
hpicfOspfv3IfNbrCount = _HpicfOspfv3IfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 5, 1, 2),
    _HpicfOspfv3IfNbrCount_Type()
)
hpicfOspfv3IfNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfNbrCount.setStatus("current")
_HpicfOspfv3IfDRAddr_Type = InetAddressIPv6
_HpicfOspfv3IfDRAddr_Object = MibTableColumn
hpicfOspfv3IfDRAddr = _HpicfOspfv3IfDRAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 5, 1, 10),
    _HpicfOspfv3IfDRAddr_Type()
)
hpicfOspfv3IfDRAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfDRAddr.setStatus("current")
_HpicfOspfv3IfBDRAddr_Type = InetAddressIPv6
_HpicfOspfv3IfBDRAddr_Object = MibTableColumn
hpicfOspfv3IfBDRAddr = _HpicfOspfv3IfBDRAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 5, 1, 11),
    _HpicfOspfv3IfBDRAddr_Type()
)
hpicfOspfv3IfBDRAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfBDRAddr.setStatus("current")
_HpicfOspfv3IfHelloDueTime_Type = Unsigned32
_HpicfOspfv3IfHelloDueTime_Object = MibTableColumn
hpicfOspfv3IfHelloDueTime = _HpicfOspfv3IfHelloDueTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 5, 1, 12),
    _HpicfOspfv3IfHelloDueTime_Type()
)
hpicfOspfv3IfHelloDueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfHelloDueTime.setStatus("current")
_HpicfOspfv3IfAdjNbrCount_Type = Unsigned32
_HpicfOspfv3IfAdjNbrCount_Object = MibTableColumn
hpicfOspfv3IfAdjNbrCount = _HpicfOspfv3IfAdjNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 5, 1, 13),
    _HpicfOspfv3IfAdjNbrCount_Type()
)
hpicfOspfv3IfAdjNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfAdjNbrCount.setStatus("current")
_HpicfOspfv3NbrTable_Object = MibTable
hpicfOspfv3NbrTable = _HpicfOspfv3NbrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfOspfv3NbrTable.setStatus("current")
_HpicfOspfv3NbrEntry_Object = MibTableRow
hpicfOspfv3NbrEntry = _HpicfOspfv3NbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfv3NbrEntry.setStatus("current")
_HpicfOspfv3NbrUpTime_Type = Unsigned32
_HpicfOspfv3NbrUpTime_Object = MibTableColumn
hpicfOspfv3NbrUpTime = _HpicfOspfv3NbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 6, 1, 1),
    _HpicfOspfv3NbrUpTime_Type()
)
hpicfOspfv3NbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3NbrUpTime.setStatus("current")
_HpicfOspfv3NbrTimeToExpiry_Type = Unsigned32
_HpicfOspfv3NbrTimeToExpiry_Object = MibTableColumn
hpicfOspfv3NbrTimeToExpiry = _HpicfOspfv3NbrTimeToExpiry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 6, 1, 2),
    _HpicfOspfv3NbrTimeToExpiry_Type()
)
hpicfOspfv3NbrTimeToExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3NbrTimeToExpiry.setStatus("current")
_HpicfOspfv3NbrDataBaseSummary_Type = Gauge32
_HpicfOspfv3NbrDataBaseSummary_Object = MibTableColumn
hpicfOspfv3NbrDataBaseSummary = _HpicfOspfv3NbrDataBaseSummary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 6, 1, 3),
    _HpicfOspfv3NbrDataBaseSummary_Type()
)
hpicfOspfv3NbrDataBaseSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3NbrDataBaseSummary.setStatus("current")
_HpicfOspfv3NbrLinkStateRequest_Type = Gauge32
_HpicfOspfv3NbrLinkStateRequest_Object = MibTableColumn
hpicfOspfv3NbrLinkStateRequest = _HpicfOspfv3NbrLinkStateRequest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 6, 1, 4),
    _HpicfOspfv3NbrLinkStateRequest_Type()
)
hpicfOspfv3NbrLinkStateRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3NbrLinkStateRequest.setStatus("current")


class _HpicfOspfv3NbrRestartState_Type(Integer32):
    """Custom type hpicfOspfv3NbrRestartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("helper", 1),
          ("normal", 0))
    )


_HpicfOspfv3NbrRestartState_Type.__name__ = "Integer32"
_HpicfOspfv3NbrRestartState_Object = MibTableColumn
hpicfOspfv3NbrRestartState = _HpicfOspfv3NbrRestartState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 6, 1, 5),
    _HpicfOspfv3NbrRestartState_Type()
)
hpicfOspfv3NbrRestartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3NbrRestartState.setStatus("current")
_HpicfOspfv3IfStatsTable_Object = MibTable
hpicfOspfv3IfStatsTable = _HpicfOspfv3IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfOspfv3IfStatsTable.setStatus("current")
_HpicfOspfv3IfStatsEntry_Object = MibTableRow
hpicfOspfv3IfStatsEntry = _HpicfOspfv3IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1)
)
hpicfOspfv3IfStatsEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3IfIndex"),
    (0, "OSPFV3-MIB", "ospfv3IfInstId"),
)
if mibBuilder.loadTexts:
    hpicfOspfv3IfStatsEntry.setStatus("current")
_HpicfOspfv3IfSentHelloPkt_Type = Counter32
_HpicfOspfv3IfSentHelloPkt_Object = MibTableColumn
hpicfOspfv3IfSentHelloPkt = _HpicfOspfv3IfSentHelloPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 1),
    _HpicfOspfv3IfSentHelloPkt_Type()
)
hpicfOspfv3IfSentHelloPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfSentHelloPkt.setStatus("current")
_HpicfOspfv3IfSentDDPkt_Type = Counter32
_HpicfOspfv3IfSentDDPkt_Object = MibTableColumn
hpicfOspfv3IfSentDDPkt = _HpicfOspfv3IfSentDDPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 2),
    _HpicfOspfv3IfSentDDPkt_Type()
)
hpicfOspfv3IfSentDDPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfSentDDPkt.setStatus("current")
_HpicfOspfv3IfSentLSRPkt_Type = Counter32
_HpicfOspfv3IfSentLSRPkt_Object = MibTableColumn
hpicfOspfv3IfSentLSRPkt = _HpicfOspfv3IfSentLSRPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 3),
    _HpicfOspfv3IfSentLSRPkt_Type()
)
hpicfOspfv3IfSentLSRPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfSentLSRPkt.setStatus("current")
_HpicfOspfv3IfSentLSUPkt_Type = Counter32
_HpicfOspfv3IfSentLSUPkt_Object = MibTableColumn
hpicfOspfv3IfSentLSUPkt = _HpicfOspfv3IfSentLSUPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 4),
    _HpicfOspfv3IfSentLSUPkt_Type()
)
hpicfOspfv3IfSentLSUPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfSentLSUPkt.setStatus("current")
_HpicfOspfv3IfSentLSAPkt_Type = Counter32
_HpicfOspfv3IfSentLSAPkt_Object = MibTableColumn
hpicfOspfv3IfSentLSAPkt = _HpicfOspfv3IfSentLSAPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 5),
    _HpicfOspfv3IfSentLSAPkt_Type()
)
hpicfOspfv3IfSentLSAPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfSentLSAPkt.setStatus("current")
_HpicfOspfv3IfRcvdHelloPkt_Type = Counter32
_HpicfOspfv3IfRcvdHelloPkt_Object = MibTableColumn
hpicfOspfv3IfRcvdHelloPkt = _HpicfOspfv3IfRcvdHelloPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 6),
    _HpicfOspfv3IfRcvdHelloPkt_Type()
)
hpicfOspfv3IfRcvdHelloPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfRcvdHelloPkt.setStatus("current")
_HpicfOspfv3IfRcvdDDPkt_Type = Counter32
_HpicfOspfv3IfRcvdDDPkt_Object = MibTableColumn
hpicfOspfv3IfRcvdDDPkt = _HpicfOspfv3IfRcvdDDPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 7),
    _HpicfOspfv3IfRcvdDDPkt_Type()
)
hpicfOspfv3IfRcvdDDPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfRcvdDDPkt.setStatus("current")
_HpicfOspfv3IfRcvdLSRPkt_Type = Counter32
_HpicfOspfv3IfRcvdLSRPkt_Object = MibTableColumn
hpicfOspfv3IfRcvdLSRPkt = _HpicfOspfv3IfRcvdLSRPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 8),
    _HpicfOspfv3IfRcvdLSRPkt_Type()
)
hpicfOspfv3IfRcvdLSRPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfRcvdLSRPkt.setStatus("current")
_HpicfOspfv3IfRcvdLSUPkt_Type = Counter32
_HpicfOspfv3IfRcvdLSUPkt_Object = MibTableColumn
hpicfOspfv3IfRcvdLSUPkt = _HpicfOspfv3IfRcvdLSUPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 9),
    _HpicfOspfv3IfRcvdLSUPkt_Type()
)
hpicfOspfv3IfRcvdLSUPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfRcvdLSUPkt.setStatus("current")
_HpicfOspfv3IfRcvdLSAPkt_Type = Counter32
_HpicfOspfv3IfRcvdLSAPkt_Object = MibTableColumn
hpicfOspfv3IfRcvdLSAPkt = _HpicfOspfv3IfRcvdLSAPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 10),
    _HpicfOspfv3IfRcvdLSAPkt_Type()
)
hpicfOspfv3IfRcvdLSAPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfRcvdLSAPkt.setStatus("current")
_HpicfOspfv3IfSentTotalErrorCount_Type = Counter32
_HpicfOspfv3IfSentTotalErrorCount_Object = MibTableColumn
hpicfOspfv3IfSentTotalErrorCount = _HpicfOspfv3IfSentTotalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 11),
    _HpicfOspfv3IfSentTotalErrorCount_Type()
)
hpicfOspfv3IfSentTotalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfSentTotalErrorCount.setStatus("current")
_HpicfOspfv3IfRcvdTotalErrorCount_Type = Counter32
_HpicfOspfv3IfRcvdTotalErrorCount_Object = MibTableColumn
hpicfOspfv3IfRcvdTotalErrorCount = _HpicfOspfv3IfRcvdTotalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 7, 1, 12),
    _HpicfOspfv3IfRcvdTotalErrorCount_Type()
)
hpicfOspfv3IfRcvdTotalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfRcvdTotalErrorCount.setStatus("current")
_HpicfOspfv3IfErrorTable_Object = MibTable
hpicfOspfv3IfErrorTable = _HpicfOspfv3IfErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfOspfv3IfErrorTable.setStatus("current")
_HpicfOspfv3IfErrorEntry_Object = MibTableRow
hpicfOspfv3IfErrorEntry = _HpicfOspfv3IfErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 8, 1)
)
hpicfOspfv3IfErrorEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3IfIndex"),
    (0, "OSPFV3-MIB", "ospfv3IfInstId"),
    (0, "HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfErrorType"),
)
if mibBuilder.loadTexts:
    hpicfOspfv3IfErrorEntry.setStatus("current")


class _HpicfOspfv3IfErrorType_Type(Integer32):
    """Custom type hpicfOspfv3IfErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfOspfv3IfErrorType_Type.__name__ = "Integer32"
_HpicfOspfv3IfErrorType_Object = MibTableColumn
hpicfOspfv3IfErrorType = _HpicfOspfv3IfErrorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 8, 1, 1),
    _HpicfOspfv3IfErrorType_Type()
)
hpicfOspfv3IfErrorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfv3IfErrorType.setStatus("current")
_HpicfOspfv3IfErrorCount_Type = Counter32
_HpicfOspfv3IfErrorCount_Object = MibTableColumn
hpicfOspfv3IfErrorCount = _HpicfOspfv3IfErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 8, 1, 2),
    _HpicfOspfv3IfErrorCount_Type()
)
hpicfOspfv3IfErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IfErrorCount.setStatus("current")
_HpicfOspfv3IfClearStatsTable_Object = MibTable
hpicfOspfv3IfClearStatsTable = _HpicfOspfv3IfClearStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 9)
)
if mibBuilder.loadTexts:
    hpicfOspfv3IfClearStatsTable.setStatus("current")
_HpicfOspfv3IfClearStatsEntry_Object = MibTableRow
hpicfOspfv3IfClearStatsEntry = _HpicfOspfv3IfClearStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 9, 1)
)
hpicfOspfv3IfClearStatsEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3IfIndex"),
    (0, "OSPFV3-MIB", "ospfv3IfInstId"),
)
if mibBuilder.loadTexts:
    hpicfOspfv3IfClearStatsEntry.setStatus("current")


class _HpicfOspfv3ClearCounters_Type(TruthValue):
    """Custom type hpicfOspfv3ClearCounters based on TruthValue"""


_HpicfOspfv3ClearCounters_Object = MibTableColumn
hpicfOspfv3ClearCounters = _HpicfOspfv3ClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 9, 1, 1),
    _HpicfOspfv3ClearCounters_Type()
)
hpicfOspfv3ClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3ClearCounters.setStatus("current")
_HpicfOspfv3SpfTable_Object = MibTable
hpicfOspfv3SpfTable = _HpicfOspfv3SpfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 10)
)
if mibBuilder.loadTexts:
    hpicfOspfv3SpfTable.setStatus("current")
_HpicfOspfv3SpfEntry_Object = MibTableRow
hpicfOspfv3SpfEntry = _HpicfOspfv3SpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 10, 1)
)
hpicfOspfv3SpfEntry.setIndexNames(
    (0, "HP-ICF-OSPFV3-MIB", "hpicfOspfv3SpfIndex"),
)
if mibBuilder.loadTexts:
    hpicfOspfv3SpfEntry.setStatus("current")
_HpicfOspfv3SpfIndex_Type = Unsigned32
_HpicfOspfv3SpfIndex_Object = MibTableColumn
hpicfOspfv3SpfIndex = _HpicfOspfv3SpfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 10, 1, 1),
    _HpicfOspfv3SpfIndex_Type()
)
hpicfOspfv3SpfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfv3SpfIndex.setStatus("current")
_HpicfOspfv3SpfReason_Type = Unsigned32
_HpicfOspfv3SpfReason_Object = MibTableColumn
hpicfOspfv3SpfReason = _HpicfOspfv3SpfReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 10, 1, 2),
    _HpicfOspfv3SpfReason_Type()
)
hpicfOspfv3SpfReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3SpfReason.setStatus("current")
_HpicfOspfv3LogTable_Object = MibTable
hpicfOspfv3LogTable = _HpicfOspfv3LogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 11)
)
if mibBuilder.loadTexts:
    hpicfOspfv3LogTable.setStatus("current")
_HpicfOspfv3LogEntry_Object = MibTableRow
hpicfOspfv3LogEntry = _HpicfOspfv3LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 11, 1)
)
hpicfOspfv3LogEntry.setIndexNames(
    (0, "HP-ICF-OSPFV3-MIB", "hpicfOspfv3LogType"),
)
if mibBuilder.loadTexts:
    hpicfOspfv3LogEntry.setStatus("current")
_HpicfOspfv3LogType_Type = HpicfOspfLogType
_HpicfOspfv3LogType_Object = MibTableColumn
hpicfOspfv3LogType = _HpicfOspfv3LogType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 11, 1, 1),
    _HpicfOspfv3LogType_Type()
)
hpicfOspfv3LogType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfv3LogType.setStatus("current")
_HpicfOspfv3LogAction_Type = HpicfOspfLogAction
_HpicfOspfv3LogAction_Object = MibTableColumn
hpicfOspfv3LogAction = _HpicfOspfv3LogAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 11, 1, 2),
    _HpicfOspfv3LogAction_Type()
)
hpicfOspfv3LogAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3LogAction.setStatus("current")
_HpicfOspfv3RouterLSATable_Object = MibTable
hpicfOspfv3RouterLSATable = _HpicfOspfv3RouterLSATable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 12)
)
if mibBuilder.loadTexts:
    hpicfOspfv3RouterLSATable.setStatus("current")
_HpicfOspfv3RouterLSAEntry_Object = MibTableRow
hpicfOspfv3RouterLSAEntry = _HpicfOspfv3RouterLSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 12, 1)
)
hpicfOspfv3RouterLSAEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbAreaId"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbType"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbRouterId"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbLsid"),
    (0, "HP-ICF-OSPFV3-MIB", "hpicfOspfv3RouterLSANbrIfId"),
    (0, "HP-ICF-OSPFV3-MIB", "hpicfOspfv3RouterLSANbrRtrId"),
)
if mibBuilder.loadTexts:
    hpicfOspfv3RouterLSAEntry.setStatus("current")
_HpicfOspfv3RouterLSANbrIfId_Type = Unsigned32
_HpicfOspfv3RouterLSANbrIfId_Object = MibTableColumn
hpicfOspfv3RouterLSANbrIfId = _HpicfOspfv3RouterLSANbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 12, 1, 1),
    _HpicfOspfv3RouterLSANbrIfId_Type()
)
hpicfOspfv3RouterLSANbrIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfv3RouterLSANbrIfId.setStatus("current")
_HpicfOspfv3RouterLSANbrRtrId_Type = Ospfv3RouterIdTC
_HpicfOspfv3RouterLSANbrRtrId_Object = MibTableColumn
hpicfOspfv3RouterLSANbrRtrId = _HpicfOspfv3RouterLSANbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 12, 1, 2),
    _HpicfOspfv3RouterLSANbrRtrId_Type()
)
hpicfOspfv3RouterLSANbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfv3RouterLSANbrRtrId.setStatus("current")
_HpicfOspfv3RouterLSAIfType_Type = Unsigned32
_HpicfOspfv3RouterLSAIfType_Object = MibTableColumn
hpicfOspfv3RouterLSAIfType = _HpicfOspfv3RouterLSAIfType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 12, 1, 3),
    _HpicfOspfv3RouterLSAIfType_Type()
)
hpicfOspfv3RouterLSAIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3RouterLSAIfType.setStatus("current")


class _HpicfOspfv3RouterLSAMetric_Type(Unsigned32):
    """Custom type hpicfOspfv3RouterLSAMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfOspfv3RouterLSAMetric_Type.__name__ = "Unsigned32"
_HpicfOspfv3RouterLSAMetric_Object = MibTableColumn
hpicfOspfv3RouterLSAMetric = _HpicfOspfv3RouterLSAMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 12, 1, 4),
    _HpicfOspfv3RouterLSAMetric_Type()
)
hpicfOspfv3RouterLSAMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3RouterLSAMetric.setStatus("current")


class _HpicfOspfv3RouterLSAIfId_Type(Unsigned32):
    """Custom type hpicfOspfv3RouterLSAIfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfOspfv3RouterLSAIfId_Type.__name__ = "Unsigned32"
_HpicfOspfv3RouterLSAIfId_Object = MibTableColumn
hpicfOspfv3RouterLSAIfId = _HpicfOspfv3RouterLSAIfId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 12, 1, 5),
    _HpicfOspfv3RouterLSAIfId_Type()
)
hpicfOspfv3RouterLSAIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3RouterLSAIfId.setStatus("current")
_HpicfOspfv3NetworkLSATable_Object = MibTable
hpicfOspfv3NetworkLSATable = _HpicfOspfv3NetworkLSATable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 13)
)
if mibBuilder.loadTexts:
    hpicfOspfv3NetworkLSATable.setStatus("current")
_HpicfOspfv3NetworkLSAEntry_Object = MibTableRow
hpicfOspfv3NetworkLSAEntry = _HpicfOspfv3NetworkLSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 13, 1)
)
hpicfOspfv3NetworkLSAEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbAreaId"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbType"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbRouterId"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbLsid"),
    (0, "HP-ICF-OSPFV3-MIB", "hpicfOspfv3NetworkLSASeqNum"),
)
if mibBuilder.loadTexts:
    hpicfOspfv3NetworkLSAEntry.setStatus("current")
_HpicfOspfv3NetworkLSASeqNum_Type = Unsigned32
_HpicfOspfv3NetworkLSASeqNum_Object = MibTableColumn
hpicfOspfv3NetworkLSASeqNum = _HpicfOspfv3NetworkLSASeqNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 13, 1, 1),
    _HpicfOspfv3NetworkLSASeqNum_Type()
)
hpicfOspfv3NetworkLSASeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfv3NetworkLSASeqNum.setStatus("current")
_HpicfOspfv3NetworkLSAAttachedRouter_Type = Ospfv3RouterIdTC
_HpicfOspfv3NetworkLSAAttachedRouter_Object = MibTableColumn
hpicfOspfv3NetworkLSAAttachedRouter = _HpicfOspfv3NetworkLSAAttachedRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 13, 1, 2),
    _HpicfOspfv3NetworkLSAAttachedRouter_Type()
)
hpicfOspfv3NetworkLSAAttachedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3NetworkLSAAttachedRouter.setStatus("current")
_HpicfOspfv3IntraAPLSATable_Object = MibTable
hpicfOspfv3IntraAPLSATable = _HpicfOspfv3IntraAPLSATable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 14)
)
if mibBuilder.loadTexts:
    hpicfOspfv3IntraAPLSATable.setStatus("current")
_HpicfOspfv3IntraAPLSAEntry_Object = MibTableRow
hpicfOspfv3IntraAPLSAEntry = _HpicfOspfv3IntraAPLSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 14, 1)
)
hpicfOspfv3IntraAPLSAEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbAreaId"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbType"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbRouterId"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbLsid"),
    (0, "HP-ICF-OSPFV3-MIB", "hpicfOspfv3IntraAPAddrPrefix"),
    (0, "HP-ICF-OSPFV3-MIB", "hpicfOspfv3IntraAPPrefixLength"),
)
if mibBuilder.loadTexts:
    hpicfOspfv3IntraAPLSAEntry.setStatus("current")
_HpicfOspfv3IntraAPAddrPrefix_Type = InetAddressIPv6
_HpicfOspfv3IntraAPAddrPrefix_Object = MibTableColumn
hpicfOspfv3IntraAPAddrPrefix = _HpicfOspfv3IntraAPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 14, 1, 1),
    _HpicfOspfv3IntraAPAddrPrefix_Type()
)
hpicfOspfv3IntraAPAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfv3IntraAPAddrPrefix.setStatus("current")
_HpicfOspfv3IntraAPPrefixLength_Type = Unsigned32
_HpicfOspfv3IntraAPPrefixLength_Object = MibTableColumn
hpicfOspfv3IntraAPPrefixLength = _HpicfOspfv3IntraAPPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 14, 1, 2),
    _HpicfOspfv3IntraAPPrefixLength_Type()
)
hpicfOspfv3IntraAPPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfv3IntraAPPrefixLength.setStatus("current")
_HpicfOspfv3IntraAPPrefixOptions_Type = Unsigned32
_HpicfOspfv3IntraAPPrefixOptions_Object = MibTableColumn
hpicfOspfv3IntraAPPrefixOptions = _HpicfOspfv3IntraAPPrefixOptions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 14, 1, 3),
    _HpicfOspfv3IntraAPPrefixOptions_Type()
)
hpicfOspfv3IntraAPPrefixOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IntraAPPrefixOptions.setStatus("current")
_HpicfOspfv3IntraAPMetric_Type = Metric
_HpicfOspfv3IntraAPMetric_Object = MibTableColumn
hpicfOspfv3IntraAPMetric = _HpicfOspfv3IntraAPMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 14, 1, 4),
    _HpicfOspfv3IntraAPMetric_Type()
)
hpicfOspfv3IntraAPMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3IntraAPMetric.setStatus("current")
_HpicfOspfv3LinkLSATable_Object = MibTable
hpicfOspfv3LinkLSATable = _HpicfOspfv3LinkLSATable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 15)
)
if mibBuilder.loadTexts:
    hpicfOspfv3LinkLSATable.setStatus("current")
_HpicfOspfv3LinkLSAEntry_Object = MibTableRow
hpicfOspfv3LinkLSAEntry = _HpicfOspfv3LinkLSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 15, 1)
)
hpicfOspfv3LinkLSAEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3LinkLsdbIfIndex"),
    (0, "OSPFV3-MIB", "ospfv3LinkLsdbIfInstId"),
    (0, "OSPFV3-MIB", "ospfv3LinkLsdbType"),
    (0, "OSPFV3-MIB", "ospfv3LinkLsdbRouterId"),
    (0, "OSPFV3-MIB", "ospfv3LinkLsdbLsid"),
    (0, "HP-ICF-OSPFV3-MIB", "hpicfOspfv3LinkAddrPrefix"),
    (0, "HP-ICF-OSPFV3-MIB", "hpicfOspfv3LinkPrefixLength"),
)
if mibBuilder.loadTexts:
    hpicfOspfv3LinkLSAEntry.setStatus("current")
_HpicfOspfv3LinkAddrPrefix_Type = InetAddressIPv6
_HpicfOspfv3LinkAddrPrefix_Object = MibTableColumn
hpicfOspfv3LinkAddrPrefix = _HpicfOspfv3LinkAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 15, 1, 1),
    _HpicfOspfv3LinkAddrPrefix_Type()
)
hpicfOspfv3LinkAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfv3LinkAddrPrefix.setStatus("current")
_HpicfOspfv3LinkPrefixLength_Type = Unsigned32
_HpicfOspfv3LinkPrefixLength_Object = MibTableColumn
hpicfOspfv3LinkPrefixLength = _HpicfOspfv3LinkPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 15, 1, 2),
    _HpicfOspfv3LinkPrefixLength_Type()
)
hpicfOspfv3LinkPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfv3LinkPrefixLength.setStatus("current")


class _HpicfOspfv3LinkPrefixOptions_Type(Unsigned32):
    """Custom type hpicfOspfv3LinkPrefixOptions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfOspfv3LinkPrefixOptions_Type.__name__ = "Unsigned32"
_HpicfOspfv3LinkPrefixOptions_Object = MibTableColumn
hpicfOspfv3LinkPrefixOptions = _HpicfOspfv3LinkPrefixOptions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 15, 1, 3),
    _HpicfOspfv3LinkPrefixOptions_Type()
)
hpicfOspfv3LinkPrefixOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3LinkPrefixOptions.setStatus("current")
_HpicfOspfv3Trap_ObjectIdentity = ObjectIdentity
hpicfOspfv3Trap = _HpicfOspfv3Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 16)
)
_HpicfOspfv3Traps_ObjectIdentity = ObjectIdentity
hpicfOspfv3Traps = _HpicfOspfv3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 16, 0)
)
_HpicfOspfv3TrapControl_ObjectIdentity = ObjectIdentity
hpicfOspfv3TrapControl = _HpicfOspfv3TrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 16, 1)
)


class _HpicfOspfv3SetTrap_Type(OctetString):
    """Custom type hpicfOspfv3SetTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HpicfOspfv3SetTrap_Type.__name__ = "OctetString"
_HpicfOspfv3SetTrap_Object = MibScalar
hpicfOspfv3SetTrap = _HpicfOspfv3SetTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 16, 1, 1),
    _HpicfOspfv3SetTrap_Type()
)
hpicfOspfv3SetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3SetTrap.setStatus("current")
_HpicfOspfv3AreaTable_Object = MibTable
hpicfOspfv3AreaTable = _HpicfOspfv3AreaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17)
)
if mibBuilder.loadTexts:
    hpicfOspfv3AreaTable.setStatus("current")
_HpicfOspfv3AreaEntry_Object = MibTableRow
hpicfOspfv3AreaEntry = _HpicfOspfv3AreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfv3AreaEntry.setStatus("current")
_HpicfOspfv3AreaNbrDownCount_Type = Counter32
_HpicfOspfv3AreaNbrDownCount_Object = MibTableColumn
hpicfOspfv3AreaNbrDownCount = _HpicfOspfv3AreaNbrDownCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17, 1, 8),
    _HpicfOspfv3AreaNbrDownCount_Type()
)
hpicfOspfv3AreaNbrDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaNbrDownCount.setStatus("current")
_HpicfOspfv3AreaNbrAttemptCount_Type = Counter32
_HpicfOspfv3AreaNbrAttemptCount_Object = MibTableColumn
hpicfOspfv3AreaNbrAttemptCount = _HpicfOspfv3AreaNbrAttemptCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17, 1, 9),
    _HpicfOspfv3AreaNbrAttemptCount_Type()
)
hpicfOspfv3AreaNbrAttemptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaNbrAttemptCount.setStatus("current")
_HpicfOspfv3AreaNbrInitCount_Type = Counter32
_HpicfOspfv3AreaNbrInitCount_Object = MibTableColumn
hpicfOspfv3AreaNbrInitCount = _HpicfOspfv3AreaNbrInitCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17, 1, 10),
    _HpicfOspfv3AreaNbrInitCount_Type()
)
hpicfOspfv3AreaNbrInitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaNbrInitCount.setStatus("current")
_HpicfOspfv3AreaNbr2wayCount_Type = Counter32
_HpicfOspfv3AreaNbr2wayCount_Object = MibTableColumn
hpicfOspfv3AreaNbr2wayCount = _HpicfOspfv3AreaNbr2wayCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17, 1, 11),
    _HpicfOspfv3AreaNbr2wayCount_Type()
)
hpicfOspfv3AreaNbr2wayCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaNbr2wayCount.setStatus("current")
_HpicfOspfv3AreaNbrExstartCount_Type = Counter32
_HpicfOspfv3AreaNbrExstartCount_Object = MibTableColumn
hpicfOspfv3AreaNbrExstartCount = _HpicfOspfv3AreaNbrExstartCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17, 1, 12),
    _HpicfOspfv3AreaNbrExstartCount_Type()
)
hpicfOspfv3AreaNbrExstartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaNbrExstartCount.setStatus("current")
_HpicfOspfv3AreaNbrExchangeCount_Type = Counter32
_HpicfOspfv3AreaNbrExchangeCount_Object = MibTableColumn
hpicfOspfv3AreaNbrExchangeCount = _HpicfOspfv3AreaNbrExchangeCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17, 1, 13),
    _HpicfOspfv3AreaNbrExchangeCount_Type()
)
hpicfOspfv3AreaNbrExchangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaNbrExchangeCount.setStatus("current")
_HpicfOspfv3AreaNbrLoadingCount_Type = Counter32
_HpicfOspfv3AreaNbrLoadingCount_Object = MibTableColumn
hpicfOspfv3AreaNbrLoadingCount = _HpicfOspfv3AreaNbrLoadingCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17, 1, 14),
    _HpicfOspfv3AreaNbrLoadingCount_Type()
)
hpicfOspfv3AreaNbrLoadingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaNbrLoadingCount.setStatus("current")
_HpicfOspfv3AreaNbrFullCount_Type = Counter32
_HpicfOspfv3AreaNbrFullCount_Object = MibTableColumn
hpicfOspfv3AreaNbrFullCount = _HpicfOspfv3AreaNbrFullCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17, 1, 15),
    _HpicfOspfv3AreaNbrFullCount_Type()
)
hpicfOspfv3AreaNbrFullCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaNbrFullCount.setStatus("current")
_HpicfOspfv3AreaInterfaceCount_Type = Counter32
_HpicfOspfv3AreaInterfaceCount_Object = MibTableColumn
hpicfOspfv3AreaInterfaceCount = _HpicfOspfv3AreaInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17, 1, 16),
    _HpicfOspfv3AreaInterfaceCount_Type()
)
hpicfOspfv3AreaInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaInterfaceCount.setStatus("current")


class _HpicfOspfv3AreaScopeUnknownLsaCount_Type(Counter32):
    """Custom type hpicfOspfv3AreaScopeUnknownLsaCount based on Counter32"""
    defaultValue = 0


_HpicfOspfv3AreaScopeUnknownLsaCount_Object = MibTableColumn
hpicfOspfv3AreaScopeUnknownLsaCount = _HpicfOspfv3AreaScopeUnknownLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 17, 1, 17),
    _HpicfOspfv3AreaScopeUnknownLsaCount_Type()
)
hpicfOspfv3AreaScopeUnknownLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaScopeUnknownLsaCount.setStatus("current")
_HpicfOspfv3AreaAggregateTable_Object = MibTable
hpicfOspfv3AreaAggregateTable = _HpicfOspfv3AreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 19)
)
if mibBuilder.loadTexts:
    hpicfOspfv3AreaAggregateTable.setStatus("current")
_HpicfOspfv3AreaAggregateEntry_Object = MibTableRow
hpicfOspfv3AreaAggregateEntry = _HpicfOspfv3AreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 19, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfv3AreaAggregateEntry.setStatus("current")


class _HpicfOspfv3AreaAggregateCost_Type(BigMetric):
    """Custom type hpicfOspfv3AreaAggregateCost based on BigMetric"""
    defaultValue = 0


_HpicfOspfv3AreaAggregateCost_Object = MibTableColumn
hpicfOspfv3AreaAggregateCost = _HpicfOspfv3AreaAggregateCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 19, 1, 1),
    _HpicfOspfv3AreaAggregateCost_Type()
)
hpicfOspfv3AreaAggregateCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaAggregateCost.setStatus("current")
_HpicfOspfv3AreaLsdbStatsTable_Object = MibTable
hpicfOspfv3AreaLsdbStatsTable = _HpicfOspfv3AreaLsdbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 20)
)
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbStatsTable.setStatus("current")
_HpicfOspfv3AreaLsdbStatsEntry_Object = MibTableRow
hpicfOspfv3AreaLsdbStatsEntry = _HpicfOspfv3AreaLsdbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 20, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbStatsEntry.setStatus("current")


class _HpicfOspfv3AreaLsdbStatRtrLsaCnt_Type(Counter32):
    """Custom type hpicfOspfv3AreaLsdbStatRtrLsaCnt based on Counter32"""
    defaultValue = 0


_HpicfOspfv3AreaLsdbStatRtrLsaCnt_Object = MibTableColumn
hpicfOspfv3AreaLsdbStatRtrLsaCnt = _HpicfOspfv3AreaLsdbStatRtrLsaCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 20, 1, 1),
    _HpicfOspfv3AreaLsdbStatRtrLsaCnt_Type()
)
hpicfOspfv3AreaLsdbStatRtrLsaCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbStatRtrLsaCnt.setStatus("current")


class _HpicfOspfv3AreaLsdbStatNwLsaCnt_Type(Counter32):
    """Custom type hpicfOspfv3AreaLsdbStatNwLsaCnt based on Counter32"""
    defaultValue = 0


_HpicfOspfv3AreaLsdbStatNwLsaCnt_Object = MibTableColumn
hpicfOspfv3AreaLsdbStatNwLsaCnt = _HpicfOspfv3AreaLsdbStatNwLsaCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 20, 1, 2),
    _HpicfOspfv3AreaLsdbStatNwLsaCnt_Type()
)
hpicfOspfv3AreaLsdbStatNwLsaCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbStatNwLsaCnt.setStatus("current")


class _HpicfOspfv3AreaLsdbStatInterPreLsaCnt_Type(Counter32):
    """Custom type hpicfOspfv3AreaLsdbStatInterPreLsaCnt based on Counter32"""
    defaultValue = 0


_HpicfOspfv3AreaLsdbStatInterPreLsaCnt_Object = MibTableColumn
hpicfOspfv3AreaLsdbStatInterPreLsaCnt = _HpicfOspfv3AreaLsdbStatInterPreLsaCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 20, 1, 3),
    _HpicfOspfv3AreaLsdbStatInterPreLsaCnt_Type()
)
hpicfOspfv3AreaLsdbStatInterPreLsaCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbStatInterPreLsaCnt.setStatus("current")


class _HpicfOspfv3AreaLsdbStatInterRtrLsaCnt_Type(Counter32):
    """Custom type hpicfOspfv3AreaLsdbStatInterRtrLsaCnt based on Counter32"""
    defaultValue = 0


_HpicfOspfv3AreaLsdbStatInterRtrLsaCnt_Object = MibTableColumn
hpicfOspfv3AreaLsdbStatInterRtrLsaCnt = _HpicfOspfv3AreaLsdbStatInterRtrLsaCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 20, 1, 4),
    _HpicfOspfv3AreaLsdbStatInterRtrLsaCnt_Type()
)
hpicfOspfv3AreaLsdbStatInterRtrLsaCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbStatInterRtrLsaCnt.setStatus("current")


class _HpicfOspfv3AreaLsdbStatIntraPreLsaCnt_Type(Counter32):
    """Custom type hpicfOspfv3AreaLsdbStatIntraPreLsaCnt based on Counter32"""
    defaultValue = 0


_HpicfOspfv3AreaLsdbStatIntraPreLsaCnt_Object = MibTableColumn
hpicfOspfv3AreaLsdbStatIntraPreLsaCnt = _HpicfOspfv3AreaLsdbStatIntraPreLsaCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 1, 20, 1, 5),
    _HpicfOspfv3AreaLsdbStatIntraPreLsaCnt_Type()
)
hpicfOspfv3AreaLsdbStatIntraPreLsaCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbStatIntraPreLsaCnt.setStatus("current")
_HpicfOspfv3Conformance_ObjectIdentity = ObjectIdentity
hpicfOspfv3Conformance = _HpicfOspfv3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2)
)
_HpicfOspfv3Groups_ObjectIdentity = ObjectIdentity
hpicfOspfv3Groups = _HpicfOspfv3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1)
)
_HpicfOspfv3Compliances_ObjectIdentity = ObjectIdentity
hpicfOspfv3Compliances = _HpicfOspfv3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 2)
)
_HpicfOspfv3IfMetricObjects_ObjectIdentity = ObjectIdentity
hpicfOspfv3IfMetricObjects = _HpicfOspfv3IfMetricObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 4)
)
_HpicfOspfv3IfMetricTable_Object = MibTable
hpicfOspfv3IfMetricTable = _HpicfOspfv3IfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfv3IfMetricTable.setStatus("current")
_HpicfOspfv3IfMetricEntry_Object = MibTableRow
hpicfOspfv3IfMetricEntry = _HpicfOspfv3IfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfv3IfMetricEntry.setStatus("current")


class _HpicfOspfv3IfFlagValue_Type(Integer32):
    """Custom type hpicfOspfv3IfFlagValue based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_HpicfOspfv3IfFlagValue_Type.__name__ = "Integer32"
_HpicfOspfv3IfFlagValue_Object = MibTableColumn
hpicfOspfv3IfFlagValue = _HpicfOspfv3IfFlagValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 4, 1, 1, 1),
    _HpicfOspfv3IfFlagValue_Type()
)
hpicfOspfv3IfFlagValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfv3IfFlagValue.setStatus("current")
ospfv3AsLsdbEntry.registerAugmentions(
    ("HP-ICF-OSPFV3-MIB",
     "hpicfOspfv3AsLsdbEntry")
)
hpicfOspfv3AsLsdbEntry.setIndexNames(*ospfv3AsLsdbEntry.getIndexNames())
ospfv3AreaLsdbEntry.registerAugmentions(
    ("HP-ICF-OSPFV3-MIB",
     "hpicfOspfv3AreaLsdbEntry")
)
hpicfOspfv3AreaLsdbEntry.setIndexNames(*ospfv3AreaLsdbEntry.getIndexNames())
ospfv3LinkLsdbEntry.registerAugmentions(
    ("HP-ICF-OSPFV3-MIB",
     "hpicfOspfv3LinkLsdbEntry")
)
hpicfOspfv3LinkLsdbEntry.setIndexNames(*ospfv3LinkLsdbEntry.getIndexNames())
ospfv3IfEntry.registerAugmentions(
    ("HP-ICF-OSPFV3-MIB",
     "hpicfOspfv3IfEntry")
)
hpicfOspfv3IfEntry.setIndexNames(*ospfv3IfEntry.getIndexNames())
ospfv3NbrEntry.registerAugmentions(
    ("HP-ICF-OSPFV3-MIB",
     "hpicfOspfv3NbrEntry")
)
hpicfOspfv3NbrEntry.setIndexNames(*ospfv3NbrEntry.getIndexNames())
ospfv3AreaEntry.registerAugmentions(
    ("HP-ICF-OSPFV3-MIB",
     "hpicfOspfv3AreaEntry")
)
hpicfOspfv3AreaEntry.setIndexNames(*ospfv3AreaEntry.getIndexNames())
ospfv3AreaAggregateEntry.registerAugmentions(
    ("HP-ICF-OSPFV3-MIB",
     "hpicfOspfv3AreaAggregateEntry")
)
hpicfOspfv3AreaAggregateEntry.setIndexNames(*ospfv3AreaAggregateEntry.getIndexNames())
ospfv3AreaEntry.registerAugmentions(
    ("HP-ICF-OSPFV3-MIB",
     "hpicfOspfv3AreaLsdbStatsEntry")
)
hpicfOspfv3AreaLsdbStatsEntry.setIndexNames(*ospfv3AreaEntry.getIndexNames())
ospfv3IfEntry.registerAugmentions(
    ("HP-ICF-OSPFV3-MIB",
     "hpicfOspfv3IfMetricEntry")
)
hpicfOspfv3IfMetricEntry.setIndexNames(*ospfv3IfEntry.getIndexNames())

# Managed Objects groups

hpicfOspfv3BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 1)
)
hpicfOspfv3BasicGroup.setObjects(
      *(("HP-ICF-OSPFV3-MIB", "hpicfOspfv3DefaultImportMetric"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3DefaultImportMetricType"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3ReferenceCost"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IntraAreaDistance"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3InterAreaDistance"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3ExternalDistance"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3SpfThrottleStartInterval"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3SpfThrottleWaitInterval"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3SpfThrottleMaxWaitTime"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3SpfThrottleCurrentSpfInterval"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaAggregateCost"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3RestartHelper"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3ASscopeUnknownLsaCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3LinkLsdbStatLinkLsa"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3TotalUnknownLsa"))
)
if mibBuilder.loadTexts:
    hpicfOspfv3BasicGroup.setStatus("current")

hpicfOspfv3AsLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 2)
)
hpicfOspfv3AsLsdbGroup.setObjects(
      *(("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AsLsdbEFTFlags"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AsLsdbMetric"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AsLsdbPrefixLength"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AsLsdbPrefixOptions"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AsLsdbRefLsType"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AsLsdbAddrPrefix"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AsLsdbFwdingAddress"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AsLsdbExtRouteTags"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AsLsdbRefLsId"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AsLsdbLsaLength"))
)
if mibBuilder.loadTexts:
    hpicfOspfv3AsLsdbGroup.setStatus("current")

hpicfOspfv3AreaLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 3)
)
hpicfOspfv3AreaLsdbGroup.setObjects(
      *(("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbRtrCapBits"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbOptions"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbMetric"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbPrefixLength"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbPrefixOptions"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbAddrPrefix"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbDstRtrId"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbNumPrefixes"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbRefLsType"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbRefLsId"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbRefAdvRtrId"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbEFTFlags"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbFwdingAddress"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbExtRouteTags"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3RouterLSAIfType"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3RouterLSAMetric"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3RouterLSAIfId"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3NetworkLSAAttachedRouter"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IntraAPPrefixOptions"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IntraAPMetric"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbLsaLength"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbLinks"))
)
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbGroup.setStatus("current")

hpicfOspfv3LinkLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 4)
)
hpicfOspfv3LinkLsdbGroup.setObjects(
      *(("HP-ICF-OSPFV3-MIB", "hpicfOspfv3LinkLsdbRtrPriority"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3LinkLsdbOptions"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3LinkLsdbLocalAddress"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3LinkLsdbNumPrefixes"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3LinkPrefixOptions"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3LinkLsdbLsaLength"))
)
if mibBuilder.loadTexts:
    hpicfOspfv3LinkLsdbGroup.setStatus("current")

hpicfOspfv3LogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 8)
)
hpicfOspfv3LogGroup.setObjects(
    ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3LogAction")
)
if mibBuilder.loadTexts:
    hpicfOspfv3LogGroup.setStatus("current")

hpicfOspfv3TrapControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 9)
)
hpicfOspfv3TrapControlGroup.setObjects(
    ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3SetTrap")
)
if mibBuilder.loadTexts:
    hpicfOspfv3TrapControlGroup.setStatus("current")

hpicfOspfv3AreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 11)
)
hpicfOspfv3AreaGroup.setObjects(
      *(("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaNbrDownCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaNbrAttemptCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaNbrInitCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaNbr2wayCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaNbrExstartCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaNbrExchangeCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaNbrLoadingCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaNbrFullCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaInterfaceCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaScopeUnknownLsaCount"))
)
if mibBuilder.loadTexts:
    hpicfOspfv3AreaGroup.setStatus("current")

hpicfOspfv3AreaLsdbStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 13)
)
hpicfOspfv3AreaLsdbStatsGroup.setObjects(
      *(("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbStatRtrLsaCnt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbStatNwLsaCnt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbStatInterPreLsaCnt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbStatInterRtrLsaCnt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3AreaLsdbStatIntraPreLsaCnt"))
)
if mibBuilder.loadTexts:
    hpicfOspfv3AreaLsdbStatsGroup.setStatus("current")

hpicfOspfv3NbrGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 14)
)
hpicfOspfv3NbrGroup1.setObjects(
      *(("HP-ICF-OSPFV3-MIB", "hpicfOspfv3NbrUpTime"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3NbrTimeToExpiry"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3NbrDataBaseSummary"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3NbrLinkStateRequest"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3NbrRestartState"))
)
if mibBuilder.loadTexts:
    hpicfOspfv3NbrGroup1.setStatus("current")

hpicfOspfv3StatisticGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 15)
)
hpicfOspfv3StatisticGroup1.setObjects(
      *(("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfSentHelloPkt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfSentDDPkt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfSentLSRPkt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfSentLSUPkt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfSentLSAPkt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfRcvdHelloPkt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfRcvdDDPkt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfRcvdLSRPkt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfRcvdLSUPkt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfRcvdLSAPkt"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfErrorCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfSentTotalErrorCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfRcvdTotalErrorCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3ClearCounters"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3SpfReason"))
)
if mibBuilder.loadTexts:
    hpicfOspfv3StatisticGroup1.setStatus("current")

hpicfOspfv3IfGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 16)
)
hpicfOspfv3IfGroup1.setObjects(
      *(("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfPassive"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfNbrCount"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfDRAddr"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfBDRAddr"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfHelloDueTime"),
        ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfAdjNbrCount"))
)
if mibBuilder.loadTexts:
    hpicfOspfv3IfGroup1.setStatus("current")

hpicfOspfv3MetricGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 1, 17)
)
hpicfOspfv3MetricGroup.setObjects(
    ("HP-ICF-OSPFV3-MIB", "hpicfOspfv3IfFlagValue")
)
if mibBuilder.loadTexts:
    hpicfOspfv3MetricGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfOspfv3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfv3Compliance.setStatus(
        "deprecated"
    )

hpicfOspfv3Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 44, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfOspfv3Compliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-OSPFV3-MIB",
    **{"hpicfOspfv3MIB": hpicfOspfv3MIB,
       "hpicfOspfv3Objects": hpicfOspfv3Objects,
       "hpicfOspfv3GeneralGroup": hpicfOspfv3GeneralGroup,
       "hpicfOspfv3DefaultImportMetric": hpicfOspfv3DefaultImportMetric,
       "hpicfOspfv3DefaultImportMetricType": hpicfOspfv3DefaultImportMetricType,
       "hpicfOspfv3IntraAreaDistance": hpicfOspfv3IntraAreaDistance,
       "hpicfOspfv3InterAreaDistance": hpicfOspfv3InterAreaDistance,
       "hpicfOspfv3ExternalDistance": hpicfOspfv3ExternalDistance,
       "hpicfOspfv3SpfThrottleStartInterval": hpicfOspfv3SpfThrottleStartInterval,
       "hpicfOspfv3SpfThrottleWaitInterval": hpicfOspfv3SpfThrottleWaitInterval,
       "hpicfOspfv3SpfThrottleMaxWaitTime": hpicfOspfv3SpfThrottleMaxWaitTime,
       "hpicfOspfv3SpfThrottleCurrentSpfInterval": hpicfOspfv3SpfThrottleCurrentSpfInterval,
       "hpicfOspfv3AreaCount": hpicfOspfv3AreaCount,
       "hpicfOspfv3RestartHelper": hpicfOspfv3RestartHelper,
       "hpicfOspfv3ASscopeUnknownLsaCount": hpicfOspfv3ASscopeUnknownLsaCount,
       "hpicfOspfv3LinkLsdbStatLinkLsa": hpicfOspfv3LinkLsdbStatLinkLsa,
       "hpicfOspfv3TotalUnknownLsa": hpicfOspfv3TotalUnknownLsa,
       "hpicfOspfv3ReferenceCost": hpicfOspfv3ReferenceCost,
       "hpicfOspfv3AsLsdbTable": hpicfOspfv3AsLsdbTable,
       "hpicfOspfv3AsLsdbEntry": hpicfOspfv3AsLsdbEntry,
       "hpicfOspfv3AsLsdbEFTFlags": hpicfOspfv3AsLsdbEFTFlags,
       "hpicfOspfv3AsLsdbMetric": hpicfOspfv3AsLsdbMetric,
       "hpicfOspfv3AsLsdbPrefixLength": hpicfOspfv3AsLsdbPrefixLength,
       "hpicfOspfv3AsLsdbPrefixOptions": hpicfOspfv3AsLsdbPrefixOptions,
       "hpicfOspfv3AsLsdbRefLsType": hpicfOspfv3AsLsdbRefLsType,
       "hpicfOspfv3AsLsdbAddrPrefix": hpicfOspfv3AsLsdbAddrPrefix,
       "hpicfOspfv3AsLsdbFwdingAddress": hpicfOspfv3AsLsdbFwdingAddress,
       "hpicfOspfv3AsLsdbExtRouteTags": hpicfOspfv3AsLsdbExtRouteTags,
       "hpicfOspfv3AsLsdbRefLsId": hpicfOspfv3AsLsdbRefLsId,
       "hpicfOspfv3AsLsdbLsaLength": hpicfOspfv3AsLsdbLsaLength,
       "hpicfOspfv3AreaLsdbTable": hpicfOspfv3AreaLsdbTable,
       "hpicfOspfv3AreaLsdbEntry": hpicfOspfv3AreaLsdbEntry,
       "hpicfOspfv3AreaLsdbRtrCapBits": hpicfOspfv3AreaLsdbRtrCapBits,
       "hpicfOspfv3AreaLsdbOptions": hpicfOspfv3AreaLsdbOptions,
       "hpicfOspfv3AreaLsdbMetric": hpicfOspfv3AreaLsdbMetric,
       "hpicfOspfv3AreaLsdbPrefixLength": hpicfOspfv3AreaLsdbPrefixLength,
       "hpicfOspfv3AreaLsdbPrefixOptions": hpicfOspfv3AreaLsdbPrefixOptions,
       "hpicfOspfv3AreaLsdbAddrPrefix": hpicfOspfv3AreaLsdbAddrPrefix,
       "hpicfOspfv3AreaLsdbDstRtrId": hpicfOspfv3AreaLsdbDstRtrId,
       "hpicfOspfv3AreaLsdbNumPrefixes": hpicfOspfv3AreaLsdbNumPrefixes,
       "hpicfOspfv3AreaLsdbRefLsType": hpicfOspfv3AreaLsdbRefLsType,
       "hpicfOspfv3AreaLsdbRefLsId": hpicfOspfv3AreaLsdbRefLsId,
       "hpicfOspfv3AreaLsdbRefAdvRtrId": hpicfOspfv3AreaLsdbRefAdvRtrId,
       "hpicfOspfv3AreaLsdbEFTFlags": hpicfOspfv3AreaLsdbEFTFlags,
       "hpicfOspfv3AreaLsdbFwdingAddress": hpicfOspfv3AreaLsdbFwdingAddress,
       "hpicfOspfv3AreaLsdbExtRouteTags": hpicfOspfv3AreaLsdbExtRouteTags,
       "hpicfOspfv3AreaLsdbLsaLength": hpicfOspfv3AreaLsdbLsaLength,
       "hpicfOspfv3AreaLsdbLinks": hpicfOspfv3AreaLsdbLinks,
       "hpicfOspfv3LinkLsdbTable": hpicfOspfv3LinkLsdbTable,
       "hpicfOspfv3LinkLsdbEntry": hpicfOspfv3LinkLsdbEntry,
       "hpicfOspfv3LinkLsdbRtrPriority": hpicfOspfv3LinkLsdbRtrPriority,
       "hpicfOspfv3LinkLsdbOptions": hpicfOspfv3LinkLsdbOptions,
       "hpicfOspfv3LinkLsdbLocalAddress": hpicfOspfv3LinkLsdbLocalAddress,
       "hpicfOspfv3LinkLsdbNumPrefixes": hpicfOspfv3LinkLsdbNumPrefixes,
       "hpicfOspfv3LinkLsdbLsaLength": hpicfOspfv3LinkLsdbLsaLength,
       "hpicfOspfv3IfTable": hpicfOspfv3IfTable,
       "hpicfOspfv3IfEntry": hpicfOspfv3IfEntry,
       "hpicfOspfv3IfPassive": hpicfOspfv3IfPassive,
       "hpicfOspfv3IfNbrCount": hpicfOspfv3IfNbrCount,
       "hpicfOspfv3IfDRAddr": hpicfOspfv3IfDRAddr,
       "hpicfOspfv3IfBDRAddr": hpicfOspfv3IfBDRAddr,
       "hpicfOspfv3IfHelloDueTime": hpicfOspfv3IfHelloDueTime,
       "hpicfOspfv3IfAdjNbrCount": hpicfOspfv3IfAdjNbrCount,
       "hpicfOspfv3NbrTable": hpicfOspfv3NbrTable,
       "hpicfOspfv3NbrEntry": hpicfOspfv3NbrEntry,
       "hpicfOspfv3NbrUpTime": hpicfOspfv3NbrUpTime,
       "hpicfOspfv3NbrTimeToExpiry": hpicfOspfv3NbrTimeToExpiry,
       "hpicfOspfv3NbrDataBaseSummary": hpicfOspfv3NbrDataBaseSummary,
       "hpicfOspfv3NbrLinkStateRequest": hpicfOspfv3NbrLinkStateRequest,
       "hpicfOspfv3NbrRestartState": hpicfOspfv3NbrRestartState,
       "hpicfOspfv3IfStatsTable": hpicfOspfv3IfStatsTable,
       "hpicfOspfv3IfStatsEntry": hpicfOspfv3IfStatsEntry,
       "hpicfOspfv3IfSentHelloPkt": hpicfOspfv3IfSentHelloPkt,
       "hpicfOspfv3IfSentDDPkt": hpicfOspfv3IfSentDDPkt,
       "hpicfOspfv3IfSentLSRPkt": hpicfOspfv3IfSentLSRPkt,
       "hpicfOspfv3IfSentLSUPkt": hpicfOspfv3IfSentLSUPkt,
       "hpicfOspfv3IfSentLSAPkt": hpicfOspfv3IfSentLSAPkt,
       "hpicfOspfv3IfRcvdHelloPkt": hpicfOspfv3IfRcvdHelloPkt,
       "hpicfOspfv3IfRcvdDDPkt": hpicfOspfv3IfRcvdDDPkt,
       "hpicfOspfv3IfRcvdLSRPkt": hpicfOspfv3IfRcvdLSRPkt,
       "hpicfOspfv3IfRcvdLSUPkt": hpicfOspfv3IfRcvdLSUPkt,
       "hpicfOspfv3IfRcvdLSAPkt": hpicfOspfv3IfRcvdLSAPkt,
       "hpicfOspfv3IfSentTotalErrorCount": hpicfOspfv3IfSentTotalErrorCount,
       "hpicfOspfv3IfRcvdTotalErrorCount": hpicfOspfv3IfRcvdTotalErrorCount,
       "hpicfOspfv3IfErrorTable": hpicfOspfv3IfErrorTable,
       "hpicfOspfv3IfErrorEntry": hpicfOspfv3IfErrorEntry,
       "hpicfOspfv3IfErrorType": hpicfOspfv3IfErrorType,
       "hpicfOspfv3IfErrorCount": hpicfOspfv3IfErrorCount,
       "hpicfOspfv3IfClearStatsTable": hpicfOspfv3IfClearStatsTable,
       "hpicfOspfv3IfClearStatsEntry": hpicfOspfv3IfClearStatsEntry,
       "hpicfOspfv3ClearCounters": hpicfOspfv3ClearCounters,
       "hpicfOspfv3SpfTable": hpicfOspfv3SpfTable,
       "hpicfOspfv3SpfEntry": hpicfOspfv3SpfEntry,
       "hpicfOspfv3SpfIndex": hpicfOspfv3SpfIndex,
       "hpicfOspfv3SpfReason": hpicfOspfv3SpfReason,
       "hpicfOspfv3LogTable": hpicfOspfv3LogTable,
       "hpicfOspfv3LogEntry": hpicfOspfv3LogEntry,
       "hpicfOspfv3LogType": hpicfOspfv3LogType,
       "hpicfOspfv3LogAction": hpicfOspfv3LogAction,
       "hpicfOspfv3RouterLSATable": hpicfOspfv3RouterLSATable,
       "hpicfOspfv3RouterLSAEntry": hpicfOspfv3RouterLSAEntry,
       "hpicfOspfv3RouterLSANbrIfId": hpicfOspfv3RouterLSANbrIfId,
       "hpicfOspfv3RouterLSANbrRtrId": hpicfOspfv3RouterLSANbrRtrId,
       "hpicfOspfv3RouterLSAIfType": hpicfOspfv3RouterLSAIfType,
       "hpicfOspfv3RouterLSAMetric": hpicfOspfv3RouterLSAMetric,
       "hpicfOspfv3RouterLSAIfId": hpicfOspfv3RouterLSAIfId,
       "hpicfOspfv3NetworkLSATable": hpicfOspfv3NetworkLSATable,
       "hpicfOspfv3NetworkLSAEntry": hpicfOspfv3NetworkLSAEntry,
       "hpicfOspfv3NetworkLSASeqNum": hpicfOspfv3NetworkLSASeqNum,
       "hpicfOspfv3NetworkLSAAttachedRouter": hpicfOspfv3NetworkLSAAttachedRouter,
       "hpicfOspfv3IntraAPLSATable": hpicfOspfv3IntraAPLSATable,
       "hpicfOspfv3IntraAPLSAEntry": hpicfOspfv3IntraAPLSAEntry,
       "hpicfOspfv3IntraAPAddrPrefix": hpicfOspfv3IntraAPAddrPrefix,
       "hpicfOspfv3IntraAPPrefixLength": hpicfOspfv3IntraAPPrefixLength,
       "hpicfOspfv3IntraAPPrefixOptions": hpicfOspfv3IntraAPPrefixOptions,
       "hpicfOspfv3IntraAPMetric": hpicfOspfv3IntraAPMetric,
       "hpicfOspfv3LinkLSATable": hpicfOspfv3LinkLSATable,
       "hpicfOspfv3LinkLSAEntry": hpicfOspfv3LinkLSAEntry,
       "hpicfOspfv3LinkAddrPrefix": hpicfOspfv3LinkAddrPrefix,
       "hpicfOspfv3LinkPrefixLength": hpicfOspfv3LinkPrefixLength,
       "hpicfOspfv3LinkPrefixOptions": hpicfOspfv3LinkPrefixOptions,
       "hpicfOspfv3Trap": hpicfOspfv3Trap,
       "hpicfOspfv3Traps": hpicfOspfv3Traps,
       "hpicfOspfv3TrapControl": hpicfOspfv3TrapControl,
       "hpicfOspfv3SetTrap": hpicfOspfv3SetTrap,
       "hpicfOspfv3AreaTable": hpicfOspfv3AreaTable,
       "hpicfOspfv3AreaEntry": hpicfOspfv3AreaEntry,
       "hpicfOspfv3AreaNbrDownCount": hpicfOspfv3AreaNbrDownCount,
       "hpicfOspfv3AreaNbrAttemptCount": hpicfOspfv3AreaNbrAttemptCount,
       "hpicfOspfv3AreaNbrInitCount": hpicfOspfv3AreaNbrInitCount,
       "hpicfOspfv3AreaNbr2wayCount": hpicfOspfv3AreaNbr2wayCount,
       "hpicfOspfv3AreaNbrExstartCount": hpicfOspfv3AreaNbrExstartCount,
       "hpicfOspfv3AreaNbrExchangeCount": hpicfOspfv3AreaNbrExchangeCount,
       "hpicfOspfv3AreaNbrLoadingCount": hpicfOspfv3AreaNbrLoadingCount,
       "hpicfOspfv3AreaNbrFullCount": hpicfOspfv3AreaNbrFullCount,
       "hpicfOspfv3AreaInterfaceCount": hpicfOspfv3AreaInterfaceCount,
       "hpicfOspfv3AreaScopeUnknownLsaCount": hpicfOspfv3AreaScopeUnknownLsaCount,
       "hpicfOspfv3AreaAggregateTable": hpicfOspfv3AreaAggregateTable,
       "hpicfOspfv3AreaAggregateEntry": hpicfOspfv3AreaAggregateEntry,
       "hpicfOspfv3AreaAggregateCost": hpicfOspfv3AreaAggregateCost,
       "hpicfOspfv3AreaLsdbStatsTable": hpicfOspfv3AreaLsdbStatsTable,
       "hpicfOspfv3AreaLsdbStatsEntry": hpicfOspfv3AreaLsdbStatsEntry,
       "hpicfOspfv3AreaLsdbStatRtrLsaCnt": hpicfOspfv3AreaLsdbStatRtrLsaCnt,
       "hpicfOspfv3AreaLsdbStatNwLsaCnt": hpicfOspfv3AreaLsdbStatNwLsaCnt,
       "hpicfOspfv3AreaLsdbStatInterPreLsaCnt": hpicfOspfv3AreaLsdbStatInterPreLsaCnt,
       "hpicfOspfv3AreaLsdbStatInterRtrLsaCnt": hpicfOspfv3AreaLsdbStatInterRtrLsaCnt,
       "hpicfOspfv3AreaLsdbStatIntraPreLsaCnt": hpicfOspfv3AreaLsdbStatIntraPreLsaCnt,
       "hpicfOspfv3Conformance": hpicfOspfv3Conformance,
       "hpicfOspfv3Groups": hpicfOspfv3Groups,
       "hpicfOspfv3BasicGroup": hpicfOspfv3BasicGroup,
       "hpicfOspfv3AsLsdbGroup": hpicfOspfv3AsLsdbGroup,
       "hpicfOspfv3AreaLsdbGroup": hpicfOspfv3AreaLsdbGroup,
       "hpicfOspfv3LinkLsdbGroup": hpicfOspfv3LinkLsdbGroup,
       "hpicfOspfv3LogGroup": hpicfOspfv3LogGroup,
       "hpicfOspfv3TrapControlGroup": hpicfOspfv3TrapControlGroup,
       "hpicfOspfv3AreaGroup": hpicfOspfv3AreaGroup,
       "hpicfOspfv3AreaLsdbStatsGroup": hpicfOspfv3AreaLsdbStatsGroup,
       "hpicfOspfv3NbrGroup1": hpicfOspfv3NbrGroup1,
       "hpicfOspfv3StatisticGroup1": hpicfOspfv3StatisticGroup1,
       "hpicfOspfv3IfGroup1": hpicfOspfv3IfGroup1,
       "hpicfOspfv3MetricGroup": hpicfOspfv3MetricGroup,
       "hpicfOspfv3Compliances": hpicfOspfv3Compliances,
       "hpicfOspfv3Compliance": hpicfOspfv3Compliance,
       "hpicfOspfv3Compliance2": hpicfOspfv3Compliance2,
       "hpicfOspfv3IfMetricObjects": hpicfOspfv3IfMetricObjects,
       "hpicfOspfv3IfMetricTable": hpicfOspfv3IfMetricTable,
       "hpicfOspfv3IfMetricEntry": hpicfOspfv3IfMetricEntry,
       "hpicfOspfv3IfFlagValue": hpicfOspfv3IfFlagValue}
)

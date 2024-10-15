# SNMP MIB module (HP-ICF-OSPF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-OSPF
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:55 2024
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

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(AreaID,
 BigMetric,
 Metric,
 PositiveInteger,
 ospfAddressLessIf,
 ospfAreaAggregateEntry,
 ospfExtLsdbEntry,
 ospfIfEntry,
 ospfIfIpAddress,
 ospfIfMetricEntry,
 ospfLsdbAreaId,
 ospfLsdbEntry,
 ospfLsdbLsid,
 ospfLsdbRouterId,
 ospfLsdbType,
 ospfNbrEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "BigMetric",
    "Metric",
    "PositiveInteger",
    "ospfAddressLessIf",
    "ospfAreaAggregateEntry",
    "ospfExtLsdbEntry",
    "ospfIfEntry",
    "ospfIfIpAddress",
    "ospfIfMetricEntry",
    "ospfLsdbAreaId",
    "ospfLsdbEntry",
    "ospfLsdbLsid",
    "ospfLsdbRouterId",
    "ospfLsdbType",
    "ospfNbrEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14)
)
hpicfOspf.setRevisions(
        ("2017-05-18 00:00",
         "2016-01-10 10:00",
         "2010-10-28 10:00",
         "2010-03-25 00:00",
         "2009-03-05 00:00",
         "2008-10-15 03:39",
         "2008-03-28 03:39",
         "2007-04-02 09:33",
         "2006-07-10 20:10",
         "2003-05-13 02:02",
         "2001-11-13 03:39")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfOspfRouterIdTc(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class HpicfOspfLogType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("neighborAdjacencyChanges", 1),
          ("other", 2))
    )



class HpicfOspfLogAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledWithDetail", 3))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfOspfObjects_ObjectIdentity = ObjectIdentity
hpicfOspfObjects = _HpicfOspfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1)
)
_HpicfOspfGeneral_ObjectIdentity = ObjectIdentity
hpicfOspfGeneral = _HpicfOspfGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1)
)
_HpicfOspf1583CompatibilityMode_Type = TruthValue
_HpicfOspf1583CompatibilityMode_Object = MibScalar
hpicfOspf1583CompatibilityMode = _HpicfOspf1583CompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 1),
    _HpicfOspf1583CompatibilityMode_Type()
)
hpicfOspf1583CompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspf1583CompatibilityMode.setStatus("current")
_HpicfOspfDefaultImportMetric_Type = BigMetric
_HpicfOspfDefaultImportMetric_Object = MibScalar
hpicfOspfDefaultImportMetric = _HpicfOspfDefaultImportMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 2),
    _HpicfOspfDefaultImportMetric_Type()
)
hpicfOspfDefaultImportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfDefaultImportMetric.setStatus("current")


class _HpicfOspfDefaultImportMetricType_Type(Integer32):
    """Custom type hpicfOspfDefaultImportMetricType based on Integer32"""
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


_HpicfOspfDefaultImportMetricType_Type.__name__ = "Integer32"
_HpicfOspfDefaultImportMetricType_Object = MibScalar
hpicfOspfDefaultImportMetricType = _HpicfOspfDefaultImportMetricType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 3),
    _HpicfOspfDefaultImportMetricType_Type()
)
hpicfOspfDefaultImportMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfDefaultImportMetricType.setStatus("current")


class _HpicfOspfIntraAreaDistance_Type(Integer32):
    """Custom type hpicfOspfIntraAreaDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfOspfIntraAreaDistance_Type.__name__ = "Integer32"
_HpicfOspfIntraAreaDistance_Object = MibScalar
hpicfOspfIntraAreaDistance = _HpicfOspfIntraAreaDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 4),
    _HpicfOspfIntraAreaDistance_Type()
)
hpicfOspfIntraAreaDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfIntraAreaDistance.setStatus("current")


class _HpicfOspfInterAreaDistance_Type(Integer32):
    """Custom type hpicfOspfInterAreaDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfOspfInterAreaDistance_Type.__name__ = "Integer32"
_HpicfOspfInterAreaDistance_Object = MibScalar
hpicfOspfInterAreaDistance = _HpicfOspfInterAreaDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 5),
    _HpicfOspfInterAreaDistance_Type()
)
hpicfOspfInterAreaDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfInterAreaDistance.setStatus("current")


class _HpicfOspfExternalDistance_Type(Integer32):
    """Custom type hpicfOspfExternalDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfOspfExternalDistance_Type.__name__ = "Integer32"
_HpicfOspfExternalDistance_Object = MibScalar
hpicfOspfExternalDistance = _HpicfOspfExternalDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 6),
    _HpicfOspfExternalDistance_Type()
)
hpicfOspfExternalDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfExternalDistance.setStatus("current")


class _HpicfOspfSpfThrottleStartInterval_Type(Integer32):
    """Custom type hpicfOspfSpfThrottleStartInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HpicfOspfSpfThrottleStartInterval_Type.__name__ = "Integer32"
_HpicfOspfSpfThrottleStartInterval_Object = MibScalar
hpicfOspfSpfThrottleStartInterval = _HpicfOspfSpfThrottleStartInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 7),
    _HpicfOspfSpfThrottleStartInterval_Type()
)
hpicfOspfSpfThrottleStartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfSpfThrottleStartInterval.setStatus("current")


class _HpicfOspfSpfThrottleWaitInterval_Type(Integer32):
    """Custom type hpicfOspfSpfThrottleWaitInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HpicfOspfSpfThrottleWaitInterval_Type.__name__ = "Integer32"
_HpicfOspfSpfThrottleWaitInterval_Object = MibScalar
hpicfOspfSpfThrottleWaitInterval = _HpicfOspfSpfThrottleWaitInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 8),
    _HpicfOspfSpfThrottleWaitInterval_Type()
)
hpicfOspfSpfThrottleWaitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfSpfThrottleWaitInterval.setStatus("current")


class _HpicfOspfSpfThrottleMaxWaitTime_Type(Integer32):
    """Custom type hpicfOspfSpfThrottleMaxWaitTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HpicfOspfSpfThrottleMaxWaitTime_Type.__name__ = "Integer32"
_HpicfOspfSpfThrottleMaxWaitTime_Object = MibScalar
hpicfOspfSpfThrottleMaxWaitTime = _HpicfOspfSpfThrottleMaxWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 9),
    _HpicfOspfSpfThrottleMaxWaitTime_Type()
)
hpicfOspfSpfThrottleMaxWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfSpfThrottleMaxWaitTime.setStatus("current")
_HpicfOspfSpfThrottleCurrentSpfInterval_Type = Unsigned32
_HpicfOspfSpfThrottleCurrentSpfInterval_Object = MibScalar
hpicfOspfSpfThrottleCurrentSpfInterval = _HpicfOspfSpfThrottleCurrentSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 10),
    _HpicfOspfSpfThrottleCurrentSpfInterval_Type()
)
hpicfOspfSpfThrottleCurrentSpfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfSpfThrottleCurrentSpfInterval.setStatus("current")
_HpicfOspfReferenceCost_Type = Metric
_HpicfOspfReferenceCost_Object = MibScalar
hpicfOspfReferenceCost = _HpicfOspfReferenceCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 1, 11),
    _HpicfOspfReferenceCost_Type()
)
hpicfOspfReferenceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfReferenceCost.setStatus("current")
_HpicfOspfRedistTable_Object = MibTable
hpicfOspfRedistTable = _HpicfOspfRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfOspfRedistTable.setStatus("current")
_HpicfOspfRedistEntry_Object = MibTableRow
hpicfOspfRedistEntry = _HpicfOspfRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 2, 1)
)
hpicfOspfRedistEntry.setIndexNames(
    (0, "HP-ICF-OSPF", "hpicfOspfRedistSrcProto"),
)
if mibBuilder.loadTexts:
    hpicfOspfRedistEntry.setStatus("current")
_HpicfOspfRedistSrcProto_Type = IANAipRouteProtocol
_HpicfOspfRedistSrcProto_Object = MibTableColumn
hpicfOspfRedistSrcProto = _HpicfOspfRedistSrcProto_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 2, 1, 1),
    _HpicfOspfRedistSrcProto_Type()
)
hpicfOspfRedistSrcProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfRedistSrcProto.setStatus("current")
_HpicfOspfRedistEnabled_Type = TruthValue
_HpicfOspfRedistEnabled_Object = MibTableColumn
hpicfOspfRedistEnabled = _HpicfOspfRedistEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 2, 1, 2),
    _HpicfOspfRedistEnabled_Type()
)
hpicfOspfRedistEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfRedistEnabled.setStatus("current")
_HpicfOspfRedistRestrictTable_Object = MibTable
hpicfOspfRedistRestrictTable = _HpicfOspfRedistRestrictTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfOspfRedistRestrictTable.setStatus("current")
_HpicfOspfRedistRestrictEntry_Object = MibTableRow
hpicfOspfRedistRestrictEntry = _HpicfOspfRedistRestrictEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 3, 1)
)
hpicfOspfRedistRestrictEntry.setIndexNames(
    (0, "HP-ICF-OSPF", "hpicfOspfRedistRestrictAddr"),
    (0, "HP-ICF-OSPF", "hpicfOspfRedistRestrictMask"),
)
if mibBuilder.loadTexts:
    hpicfOspfRedistRestrictEntry.setStatus("current")
_HpicfOspfRedistRestrictAddr_Type = IpAddress
_HpicfOspfRedistRestrictAddr_Object = MibTableColumn
hpicfOspfRedistRestrictAddr = _HpicfOspfRedistRestrictAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 3, 1, 1),
    _HpicfOspfRedistRestrictAddr_Type()
)
hpicfOspfRedistRestrictAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfRedistRestrictAddr.setStatus("current")
_HpicfOspfRedistRestrictMask_Type = IpAddress
_HpicfOspfRedistRestrictMask_Object = MibTableColumn
hpicfOspfRedistRestrictMask = _HpicfOspfRedistRestrictMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 3, 1, 2),
    _HpicfOspfRedistRestrictMask_Type()
)
hpicfOspfRedistRestrictMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfRedistRestrictMask.setStatus("current")
_HpicfOspfRedistRestrictStatus_Type = RowStatus
_HpicfOspfRedistRestrictStatus_Object = MibTableColumn
hpicfOspfRedistRestrictStatus = _HpicfOspfRedistRestrictStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 3, 1, 3),
    _HpicfOspfRedistRestrictStatus_Type()
)
hpicfOspfRedistRestrictStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOspfRedistRestrictStatus.setStatus("current")
_HpicfOspfLogTable_Object = MibTable
hpicfOspfLogTable = _HpicfOspfLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfOspfLogTable.setStatus("current")
_HpicfOspfLogEntry_Object = MibTableRow
hpicfOspfLogEntry = _HpicfOspfLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 4, 1)
)
hpicfOspfLogEntry.setIndexNames(
    (0, "HP-ICF-OSPF", "hpicfOspfLogType"),
)
if mibBuilder.loadTexts:
    hpicfOspfLogEntry.setStatus("current")
_HpicfOspfLogType_Type = HpicfOspfLogType
_HpicfOspfLogType_Object = MibTableColumn
hpicfOspfLogType = _HpicfOspfLogType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 4, 1, 1),
    _HpicfOspfLogType_Type()
)
hpicfOspfLogType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfLogType.setStatus("current")
_HpicfOspfLogAction_Type = HpicfOspfLogAction
_HpicfOspfLogAction_Object = MibTableColumn
hpicfOspfLogAction = _HpicfOspfLogAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 4, 1, 2),
    _HpicfOspfLogAction_Type()
)
hpicfOspfLogAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfLogAction.setStatus("current")
_HpicfOspfNbrTable_Object = MibTable
hpicfOspfNbrTable = _HpicfOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfOspfNbrTable.setStatus("current")
_HpicfOspfNbrEntry_Object = MibTableRow
hpicfOspfNbrEntry = _HpicfOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfNbrEntry.setStatus("current")
_HpicfOspfNbrUpTime_Type = PositiveInteger
_HpicfOspfNbrUpTime_Object = MibTableColumn
hpicfOspfNbrUpTime = _HpicfOspfNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 5, 1, 1),
    _HpicfOspfNbrUpTime_Type()
)
hpicfOspfNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfNbrUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOspfNbrUpTime.setUnits("seconds")
_HpicfOspfNbrTimeToExpiry_Type = PositiveInteger
_HpicfOspfNbrTimeToExpiry_Object = MibTableColumn
hpicfOspfNbrTimeToExpiry = _HpicfOspfNbrTimeToExpiry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 5, 1, 2),
    _HpicfOspfNbrTimeToExpiry_Type()
)
hpicfOspfNbrTimeToExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfNbrTimeToExpiry.setStatus("current")


class _HpicfOspfNbrDesignatedRouter_Type(IpAddress):
    """Custom type hpicfOspfNbrDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_HpicfOspfNbrDesignatedRouter_Object = MibTableColumn
hpicfOspfNbrDesignatedRouter = _HpicfOspfNbrDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 5, 1, 3),
    _HpicfOspfNbrDesignatedRouter_Type()
)
hpicfOspfNbrDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfNbrDesignatedRouter.setStatus("current")


class _HpicfOspfNbrBackupDesignatedRouter_Type(IpAddress):
    """Custom type hpicfOspfNbrBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_HpicfOspfNbrBackupDesignatedRouter_Object = MibTableColumn
hpicfOspfNbrBackupDesignatedRouter = _HpicfOspfNbrBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 5, 1, 4),
    _HpicfOspfNbrBackupDesignatedRouter_Type()
)
hpicfOspfNbrBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfNbrBackupDesignatedRouter.setStatus("current")
_HpicfOspfNbrAreaId_Type = AreaID
_HpicfOspfNbrAreaId_Object = MibTableColumn
hpicfOspfNbrAreaId = _HpicfOspfNbrAreaId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 5, 1, 5),
    _HpicfOspfNbrAreaId_Type()
)
hpicfOspfNbrAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfNbrAreaId.setStatus("current")
_HpicfOspfNbrInterfaceName_Type = DisplayString
_HpicfOspfNbrInterfaceName_Object = MibTableColumn
hpicfOspfNbrInterfaceName = _HpicfOspfNbrInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 5, 1, 6),
    _HpicfOspfNbrInterfaceName_Type()
)
hpicfOspfNbrInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfNbrInterfaceName.setStatus("current")


class _HpicfOspfNbrBfdState_Type(Integer32):
    """Custom type hpicfOspfNbrBfdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("down", 3),
          ("notConfigured", 0),
          ("up", 2))
    )


_HpicfOspfNbrBfdState_Type.__name__ = "Integer32"
_HpicfOspfNbrBfdState_Object = MibTableColumn
hpicfOspfNbrBfdState = _HpicfOspfNbrBfdState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 5, 1, 7),
    _HpicfOspfNbrBfdState_Type()
)
hpicfOspfNbrBfdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfNbrBfdState.setStatus("current")
_HpicfOspfAreaAggregateTable_Object = MibTable
hpicfOspfAreaAggregateTable = _HpicfOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfOspfAreaAggregateTable.setStatus("current")
_HpicfOspfAreaAggregateEntry_Object = MibTableRow
hpicfOspfAreaAggregateEntry = _HpicfOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfAreaAggregateEntry.setStatus("current")


class _HpicfOspfAreaAggregateCost_Type(BigMetric):
    """Custom type hpicfOspfAreaAggregateCost based on BigMetric"""
    defaultValue = 0


_HpicfOspfAreaAggregateCost_Object = MibTableColumn
hpicfOspfAreaAggregateCost = _HpicfOspfAreaAggregateCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 6, 1, 1),
    _HpicfOspfAreaAggregateCost_Type()
)
hpicfOspfAreaAggregateCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOspfAreaAggregateCost.setStatus("current")


class _HpicfOspfAreaAggregateType_Type(Integer32):
    """Custom type hpicfOspfAreaAggregateType based on Integer32"""
    defaultValue = 2

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


_HpicfOspfAreaAggregateType_Type.__name__ = "Integer32"
_HpicfOspfAreaAggregateType_Object = MibTableColumn
hpicfOspfAreaAggregateType = _HpicfOspfAreaAggregateType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 1, 6, 1, 2),
    _HpicfOspfAreaAggregateType_Type()
)
hpicfOspfAreaAggregateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfOspfAreaAggregateType.setStatus("current")
_HpicfOspfConformance_ObjectIdentity = ObjectIdentity
hpicfOspfConformance = _HpicfOspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2)
)
_HpicfOspfGroups_ObjectIdentity = ObjectIdentity
hpicfOspfGroups = _HpicfOspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1)
)
_HpicfOspfCompliances_ObjectIdentity = ObjectIdentity
hpicfOspfCompliances = _HpicfOspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 2)
)
_HpicfOspfReqGroups_ObjectIdentity = ObjectIdentity
hpicfOspfReqGroups = _HpicfOspfReqGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 3)
)
_HpicfOspfRetransGroups_ObjectIdentity = ObjectIdentity
hpicfOspfRetransGroups = _HpicfOspfRetransGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 4)
)
_HpicfOspfFloodGroups_ObjectIdentity = ObjectIdentity
hpicfOspfFloodGroups = _HpicfOspfFloodGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 5)
)
_HpicfOspfRouteGroup_ObjectIdentity = ObjectIdentity
hpicfOspfRouteGroup = _HpicfOspfRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 3)
)
_HpicfOspfNssaType1_ObjectIdentity = ObjectIdentity
hpicfOspfNssaType1 = _HpicfOspfNssaType1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 3, 1)
)
_HpicfOspfNssaType2_ObjectIdentity = ObjectIdentity
hpicfOspfNssaType2 = _HpicfOspfNssaType2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 3, 2)
)
_HpicfOspfIfTable_Object = MibTable
hpicfOspfIfTable = _HpicfOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 4)
)
if mibBuilder.loadTexts:
    hpicfOspfIfTable.setStatus("current")
_HpicfOspfIfEntry_Object = MibTableRow
hpicfOspfIfEntry = _HpicfOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfIfEntry.setStatus("current")


class _HpicfOspfIfPassive_Type(TruthValue):
    """Custom type hpicfOspfIfPassive based on TruthValue"""


_HpicfOspfIfPassive_Object = MibTableColumn
hpicfOspfIfPassive = _HpicfOspfIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 4, 1, 1),
    _HpicfOspfIfPassive_Type()
)
hpicfOspfIfPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfIfPassive.setStatus("current")
_HpicfOspfIfNbrCount_Type = Unsigned32
_HpicfOspfIfNbrCount_Object = MibTableColumn
hpicfOspfIfNbrCount = _HpicfOspfIfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 4, 1, 2),
    _HpicfOspfIfNbrCount_Type()
)
hpicfOspfIfNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfIfNbrCount.setStatus("current")


class _HpicfOspfIfBfdEnbl_Type(TruthValue):
    """Custom type hpicfOspfIfBfdEnbl based on TruthValue"""


_HpicfOspfIfBfdEnbl_Object = MibTableColumn
hpicfOspfIfBfdEnbl = _HpicfOspfIfBfdEnbl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 4, 1, 3),
    _HpicfOspfIfBfdEnbl_Type()
)
hpicfOspfIfBfdEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfIfBfdEnbl.setStatus("current")
_HpicfOspfIfStatsTable_Object = MibTable
hpicfOspfIfStatsTable = _HpicfOspfIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5)
)
if mibBuilder.loadTexts:
    hpicfOspfIfStatsTable.setStatus("current")
_HpicfOspfIfStatsEntry_Object = MibTableRow
hpicfOspfIfStatsEntry = _HpicfOspfIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5, 1)
)
hpicfOspfIfStatsEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    hpicfOspfIfStatsEntry.setStatus("current")
_HpicfOspfSentHelloPkt_Type = Counter32
_HpicfOspfSentHelloPkt_Object = MibTableColumn
hpicfOspfSentHelloPkt = _HpicfOspfSentHelloPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5, 1, 1),
    _HpicfOspfSentHelloPkt_Type()
)
hpicfOspfSentHelloPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfSentHelloPkt.setStatus("current")
_HpicfOspfSentDDPkt_Type = Counter32
_HpicfOspfSentDDPkt_Object = MibTableColumn
hpicfOspfSentDDPkt = _HpicfOspfSentDDPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5, 1, 2),
    _HpicfOspfSentDDPkt_Type()
)
hpicfOspfSentDDPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfSentDDPkt.setStatus("current")
_HpicfOspfSentLSRPkt_Type = Counter32
_HpicfOspfSentLSRPkt_Object = MibTableColumn
hpicfOspfSentLSRPkt = _HpicfOspfSentLSRPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5, 1, 3),
    _HpicfOspfSentLSRPkt_Type()
)
hpicfOspfSentLSRPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfSentLSRPkt.setStatus("current")
_HpicfOspfSentLSUPkt_Type = Counter32
_HpicfOspfSentLSUPkt_Object = MibTableColumn
hpicfOspfSentLSUPkt = _HpicfOspfSentLSUPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5, 1, 4),
    _HpicfOspfSentLSUPkt_Type()
)
hpicfOspfSentLSUPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfSentLSUPkt.setStatus("current")
_HpicfOspfSentLSAPkt_Type = Counter32
_HpicfOspfSentLSAPkt_Object = MibTableColumn
hpicfOspfSentLSAPkt = _HpicfOspfSentLSAPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5, 1, 5),
    _HpicfOspfSentLSAPkt_Type()
)
hpicfOspfSentLSAPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfSentLSAPkt.setStatus("current")
_HpicfOspfRcvdHelloPkt_Type = Counter32
_HpicfOspfRcvdHelloPkt_Object = MibTableColumn
hpicfOspfRcvdHelloPkt = _HpicfOspfRcvdHelloPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5, 1, 6),
    _HpicfOspfRcvdHelloPkt_Type()
)
hpicfOspfRcvdHelloPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRcvdHelloPkt.setStatus("current")
_HpicfOspfRcvdDDPkt_Type = Counter32
_HpicfOspfRcvdDDPkt_Object = MibTableColumn
hpicfOspfRcvdDDPkt = _HpicfOspfRcvdDDPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5, 1, 7),
    _HpicfOspfRcvdDDPkt_Type()
)
hpicfOspfRcvdDDPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRcvdDDPkt.setStatus("current")
_HpicfOspfRcvdLSRPkt_Type = Counter32
_HpicfOspfRcvdLSRPkt_Object = MibTableColumn
hpicfOspfRcvdLSRPkt = _HpicfOspfRcvdLSRPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5, 1, 8),
    _HpicfOspfRcvdLSRPkt_Type()
)
hpicfOspfRcvdLSRPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRcvdLSRPkt.setStatus("current")
_HpicfOspfRcvdLSUPkt_Type = Counter32
_HpicfOspfRcvdLSUPkt_Object = MibTableColumn
hpicfOspfRcvdLSUPkt = _HpicfOspfRcvdLSUPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5, 1, 9),
    _HpicfOspfRcvdLSUPkt_Type()
)
hpicfOspfRcvdLSUPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRcvdLSUPkt.setStatus("current")
_HpicfOspfRcvdLSAPkt_Type = Counter32
_HpicfOspfRcvdLSAPkt_Object = MibTableColumn
hpicfOspfRcvdLSAPkt = _HpicfOspfRcvdLSAPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 5, 1, 10),
    _HpicfOspfRcvdLSAPkt_Type()
)
hpicfOspfRcvdLSAPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRcvdLSAPkt.setStatus("current")
_HpicfOspfIfErrorTable_Object = MibTable
hpicfOspfIfErrorTable = _HpicfOspfIfErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 6)
)
if mibBuilder.loadTexts:
    hpicfOspfIfErrorTable.setStatus("current")
_HpicfOspfIfErrorEntry_Object = MibTableRow
hpicfOspfIfErrorEntry = _HpicfOspfIfErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 6, 1)
)
hpicfOspfIfErrorEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
    (0, "HP-ICF-OSPF", "hpicfOspfIfErrorType"),
)
if mibBuilder.loadTexts:
    hpicfOspfIfErrorEntry.setStatus("current")


class _HpicfOspfIfErrorType_Type(Integer32):
    """Custom type hpicfOspfIfErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_HpicfOspfIfErrorType_Type.__name__ = "Integer32"
_HpicfOspfIfErrorType_Object = MibTableColumn
hpicfOspfIfErrorType = _HpicfOspfIfErrorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 6, 1, 1),
    _HpicfOspfIfErrorType_Type()
)
hpicfOspfIfErrorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfIfErrorType.setStatus("current")
_HpicfOspfIfErrorCount_Type = Counter32
_HpicfOspfIfErrorCount_Object = MibTableColumn
hpicfOspfIfErrorCount = _HpicfOspfIfErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 6, 1, 2),
    _HpicfOspfIfErrorCount_Type()
)
hpicfOspfIfErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfIfErrorCount.setStatus("current")
_HpicfOspfIfClearStatsTable_Object = MibTable
hpicfOspfIfClearStatsTable = _HpicfOspfIfClearStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 7)
)
if mibBuilder.loadTexts:
    hpicfOspfIfClearStatsTable.setStatus("current")
_HpicfOspfIfClearStatsEntry_Object = MibTableRow
hpicfOspfIfClearStatsEntry = _HpicfOspfIfClearStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 7, 1)
)
hpicfOspfIfClearStatsEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    hpicfOspfIfClearStatsEntry.setStatus("current")


class _HpicfOspfClearCounters_Type(TruthValue):
    """Custom type hpicfOspfClearCounters based on TruthValue"""


_HpicfOspfClearCounters_Object = MibTableColumn
hpicfOspfClearCounters = _HpicfOspfClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 7, 1, 1),
    _HpicfOspfClearCounters_Type()
)
hpicfOspfClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfClearCounters.setStatus("current")
_HpicfOspfSpfTable_Object = MibTable
hpicfOspfSpfTable = _HpicfOspfSpfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 8)
)
if mibBuilder.loadTexts:
    hpicfOspfSpfTable.setStatus("current")
_HpicfOspfSpfEntry_Object = MibTableRow
hpicfOspfSpfEntry = _HpicfOspfSpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 8, 1)
)
hpicfOspfSpfEntry.setIndexNames(
    (0, "HP-ICF-OSPF", "hpicfOspfSpfInstance"),
)
if mibBuilder.loadTexts:
    hpicfOspfSpfEntry.setStatus("current")


class _HpicfOspfSpfInstance_Type(Integer32):
    """Custom type hpicfOspfSpfInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_HpicfOspfSpfInstance_Type.__name__ = "Integer32"
_HpicfOspfSpfInstance_Object = MibTableColumn
hpicfOspfSpfInstance = _HpicfOspfSpfInstance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 8, 1, 1),
    _HpicfOspfSpfInstance_Type()
)
hpicfOspfSpfInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfSpfInstance.setStatus("current")
_HpicfOspfSpfReason_Type = Integer32
_HpicfOspfSpfReason_Object = MibTableColumn
hpicfOspfSpfReason = _HpicfOspfSpfReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 8, 1, 2),
    _HpicfOspfSpfReason_Type()
)
hpicfOspfSpfReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfSpfReason.setStatus("current")
_HpicfOspfSpfTime_Type = Integer32
_HpicfOspfSpfTime_Object = MibTableColumn
hpicfOspfSpfTime = _HpicfOspfSpfTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 8, 1, 3),
    _HpicfOspfSpfTime_Type()
)
hpicfOspfSpfTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfSpfTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOspfSpfTime.setUnits("seconds")
_HpicfOspfReqTable_Object = MibTable
hpicfOspfReqTable = _HpicfOspfReqTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 9)
)
if mibBuilder.loadTexts:
    hpicfOspfReqTable.setStatus("current")
_HpicfOspfReqEntry_Object = MibTableRow
hpicfOspfReqEntry = _HpicfOspfReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 9, 1)
)
hpicfOspfReqEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    hpicfOspfReqEntry.setStatus("current")


class _HpicfOspfReqType_Type(Integer32):
    """Custom type hpicfOspfReqType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("areaOpaqueLink", 10),
          ("asExternalLink", 5),
          ("asSummaryLink", 4),
          ("multicastLink", 6),
          ("networkLink", 2),
          ("nssaExternalLink", 7),
          ("routerLink", 1),
          ("summaryLink", 3))
    )


_HpicfOspfReqType_Type.__name__ = "Integer32"
_HpicfOspfReqType_Object = MibTableColumn
hpicfOspfReqType = _HpicfOspfReqType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 9, 1, 1),
    _HpicfOspfReqType_Type()
)
hpicfOspfReqType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfReqType.setStatus("current")
_HpicfOspfReqLsid_Type = IpAddress
_HpicfOspfReqLsid_Object = MibTableColumn
hpicfOspfReqLsid = _HpicfOspfReqLsid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 9, 1, 2),
    _HpicfOspfReqLsid_Type()
)
hpicfOspfReqLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfReqLsid.setStatus("current")
_HpicfOspfReqRouterId_Type = IpAddress
_HpicfOspfReqRouterId_Object = MibTableColumn
hpicfOspfReqRouterId = _HpicfOspfReqRouterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 9, 1, 3),
    _HpicfOspfReqRouterId_Type()
)
hpicfOspfReqRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfReqRouterId.setStatus("current")
_HpicfOspfReqSequence_Type = Integer32
_HpicfOspfReqSequence_Object = MibTableColumn
hpicfOspfReqSequence = _HpicfOspfReqSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 9, 1, 4),
    _HpicfOspfReqSequence_Type()
)
hpicfOspfReqSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfReqSequence.setStatus("current")
_HpicfOspfReqAge_Type = Integer32
_HpicfOspfReqAge_Object = MibTableColumn
hpicfOspfReqAge = _HpicfOspfReqAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 9, 1, 5),
    _HpicfOspfReqAge_Type()
)
hpicfOspfReqAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfReqAge.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOspfReqAge.setUnits("seconds")
_HpicfOspfReqChecksum_Type = Integer32
_HpicfOspfReqChecksum_Object = MibTableColumn
hpicfOspfReqChecksum = _HpicfOspfReqChecksum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 9, 1, 6),
    _HpicfOspfReqChecksum_Type()
)
hpicfOspfReqChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfReqChecksum.setStatus("current")
_HpicfOspfRetransTable_Object = MibTable
hpicfOspfRetransTable = _HpicfOspfRetransTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 10)
)
if mibBuilder.loadTexts:
    hpicfOspfRetransTable.setStatus("current")
_HpicfOspfRetransEntry_Object = MibTableRow
hpicfOspfRetransEntry = _HpicfOspfRetransEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 10, 1)
)
hpicfOspfRetransEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    hpicfOspfRetransEntry.setStatus("current")


class _HpicfOspfRetransType_Type(Integer32):
    """Custom type hpicfOspfRetransType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("areaOpaqueLink", 10),
          ("asExternalLink", 5),
          ("asSummaryLink", 4),
          ("multicastLink", 6),
          ("networkLink", 2),
          ("nssaExternalLink", 7),
          ("routerLink", 1),
          ("summaryLink", 3))
    )


_HpicfOspfRetransType_Type.__name__ = "Integer32"
_HpicfOspfRetransType_Object = MibTableColumn
hpicfOspfRetransType = _HpicfOspfRetransType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 10, 1, 1),
    _HpicfOspfRetransType_Type()
)
hpicfOspfRetransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRetransType.setStatus("current")
_HpicfOspfRetransLsid_Type = IpAddress
_HpicfOspfRetransLsid_Object = MibTableColumn
hpicfOspfRetransLsid = _HpicfOspfRetransLsid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 10, 1, 2),
    _HpicfOspfRetransLsid_Type()
)
hpicfOspfRetransLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRetransLsid.setStatus("current")
_HpicfOspfRetransRouterId_Type = IpAddress
_HpicfOspfRetransRouterId_Object = MibTableColumn
hpicfOspfRetransRouterId = _HpicfOspfRetransRouterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 10, 1, 3),
    _HpicfOspfRetransRouterId_Type()
)
hpicfOspfRetransRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRetransRouterId.setStatus("current")
_HpicfOspfRetransSequence_Type = Integer32
_HpicfOspfRetransSequence_Object = MibTableColumn
hpicfOspfRetransSequence = _HpicfOspfRetransSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 10, 1, 4),
    _HpicfOspfRetransSequence_Type()
)
hpicfOspfRetransSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRetransSequence.setStatus("current")
_HpicfOspfRetransAge_Type = Integer32
_HpicfOspfRetransAge_Object = MibTableColumn
hpicfOspfRetransAge = _HpicfOspfRetransAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 10, 1, 5),
    _HpicfOspfRetransAge_Type()
)
hpicfOspfRetransAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRetransAge.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOspfRetransAge.setUnits("seconds")
_HpicfOspfRetransChecksum_Type = Integer32
_HpicfOspfRetransChecksum_Object = MibTableColumn
hpicfOspfRetransChecksum = _HpicfOspfRetransChecksum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 10, 1, 6),
    _HpicfOspfRetransChecksum_Type()
)
hpicfOspfRetransChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRetransChecksum.setStatus("current")
_HpicfOspfFloodTable_Object = MibTable
hpicfOspfFloodTable = _HpicfOspfFloodTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 11)
)
if mibBuilder.loadTexts:
    hpicfOspfFloodTable.setStatus("current")
_HpicfOspfFloodEntry_Object = MibTableRow
hpicfOspfFloodEntry = _HpicfOspfFloodEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 11, 1)
)
hpicfOspfFloodEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    hpicfOspfFloodEntry.setStatus("current")


class _HpicfOspfFloodType_Type(Integer32):
    """Custom type hpicfOspfFloodType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("areaOpaqueLink", 10),
          ("asExternalLink", 5),
          ("asSummaryLink", 4),
          ("multicastLink", 6),
          ("networkLink", 2),
          ("nssaExternalLink", 7),
          ("routerLink", 1),
          ("summaryLink", 3))
    )


_HpicfOspfFloodType_Type.__name__ = "Integer32"
_HpicfOspfFloodType_Object = MibTableColumn
hpicfOspfFloodType = _HpicfOspfFloodType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 11, 1, 1),
    _HpicfOspfFloodType_Type()
)
hpicfOspfFloodType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfFloodType.setStatus("current")
_HpicfOspfFloodLsid_Type = IpAddress
_HpicfOspfFloodLsid_Object = MibTableColumn
hpicfOspfFloodLsid = _HpicfOspfFloodLsid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 11, 1, 2),
    _HpicfOspfFloodLsid_Type()
)
hpicfOspfFloodLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfFloodLsid.setStatus("current")
_HpicfOspfFloodRouterId_Type = IpAddress
_HpicfOspfFloodRouterId_Object = MibTableColumn
hpicfOspfFloodRouterId = _HpicfOspfFloodRouterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 11, 1, 3),
    _HpicfOspfFloodRouterId_Type()
)
hpicfOspfFloodRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfFloodRouterId.setStatus("current")
_HpicfOspfFloodSequence_Type = Integer32
_HpicfOspfFloodSequence_Object = MibTableColumn
hpicfOspfFloodSequence = _HpicfOspfFloodSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 11, 1, 4),
    _HpicfOspfFloodSequence_Type()
)
hpicfOspfFloodSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfFloodSequence.setStatus("current")
_HpicfOspfFloodAge_Type = Integer32
_HpicfOspfFloodAge_Object = MibTableColumn
hpicfOspfFloodAge = _HpicfOspfFloodAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 11, 1, 5),
    _HpicfOspfFloodAge_Type()
)
hpicfOspfFloodAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfFloodAge.setStatus("current")
if mibBuilder.loadTexts:
    hpicfOspfFloodAge.setUnits("seconds")
_HpicfOspfFloodChecksum_Type = Integer32
_HpicfOspfFloodChecksum_Object = MibTableColumn
hpicfOspfFloodChecksum = _HpicfOspfFloodChecksum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 11, 1, 6),
    _HpicfOspfFloodChecksum_Type()
)
hpicfOspfFloodChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfFloodChecksum.setStatus("current")
_HpicfOspfSpfTimerElapsed_Type = Unsigned32
_HpicfOspfSpfTimerElapsed_Object = MibScalar
hpicfOspfSpfTimerElapsed = _HpicfOspfSpfTimerElapsed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 12),
    _HpicfOspfSpfTimerElapsed_Type()
)
hpicfOspfSpfTimerElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfSpfTimerElapsed.setStatus("current")
_HpicfOspfAreaLsdbTable_Object = MibTable
hpicfOspfAreaLsdbTable = _HpicfOspfAreaLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 14)
)
if mibBuilder.loadTexts:
    hpicfOspfAreaLsdbTable.setStatus("current")
_HpicfOspfAreaLsdbEntry_Object = MibTableRow
hpicfOspfAreaLsdbEntry = _HpicfOspfAreaLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 14, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfAreaLsdbEntry.setStatus("current")
_HpicfOspfAreaLsdbRtrCapBits_Type = Unsigned32
_HpicfOspfAreaLsdbRtrCapBits_Object = MibTableColumn
hpicfOspfAreaLsdbRtrCapBits = _HpicfOspfAreaLsdbRtrCapBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 14, 1, 1),
    _HpicfOspfAreaLsdbRtrCapBits_Type()
)
hpicfOspfAreaLsdbRtrCapBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfAreaLsdbRtrCapBits.setStatus("current")
_HpicfOspfAreaLsdbOptions_Type = Unsigned32
_HpicfOspfAreaLsdbOptions_Object = MibTableColumn
hpicfOspfAreaLsdbOptions = _HpicfOspfAreaLsdbOptions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 14, 1, 2),
    _HpicfOspfAreaLsdbOptions_Type()
)
hpicfOspfAreaLsdbOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfAreaLsdbOptions.setStatus("current")
_HpicfOspfAreaLsdbMetric_Type = Metric
_HpicfOspfAreaLsdbMetric_Object = MibTableColumn
hpicfOspfAreaLsdbMetric = _HpicfOspfAreaLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 14, 1, 3),
    _HpicfOspfAreaLsdbMetric_Type()
)
hpicfOspfAreaLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfAreaLsdbMetric.setStatus("current")
_HpicfOspfAreaLsdbAddrPrefix_Type = Unsigned32
_HpicfOspfAreaLsdbAddrPrefix_Object = MibTableColumn
hpicfOspfAreaLsdbAddrPrefix = _HpicfOspfAreaLsdbAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 14, 1, 4),
    _HpicfOspfAreaLsdbAddrPrefix_Type()
)
hpicfOspfAreaLsdbAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfAreaLsdbAddrPrefix.setStatus("current")
_HpicfOspfAreaLsdbFwdingAddress_Type = HpicfOspfRouterIdTc
_HpicfOspfAreaLsdbFwdingAddress_Object = MibTableColumn
hpicfOspfAreaLsdbFwdingAddress = _HpicfOspfAreaLsdbFwdingAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 14, 1, 5),
    _HpicfOspfAreaLsdbFwdingAddress_Type()
)
hpicfOspfAreaLsdbFwdingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfAreaLsdbFwdingAddress.setStatus("current")
_HpicfOspfAreaLsdbExtRouteTags_Type = Unsigned32
_HpicfOspfAreaLsdbExtRouteTags_Object = MibTableColumn
hpicfOspfAreaLsdbExtRouteTags = _HpicfOspfAreaLsdbExtRouteTags_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 14, 1, 6),
    _HpicfOspfAreaLsdbExtRouteTags_Type()
)
hpicfOspfAreaLsdbExtRouteTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfAreaLsdbExtRouteTags.setStatus("current")
_HpicfOspfTOS_Type = Unsigned32
_HpicfOspfTOS_Object = MibTableColumn
hpicfOspfTOS = _HpicfOspfTOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 14, 1, 7),
    _HpicfOspfTOS_Type()
)
hpicfOspfTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfTOS.setStatus("current")
_HpicfOspfLsdbRouterLinks_Type = Unsigned32
_HpicfOspfLsdbRouterLinks_Object = MibTableColumn
hpicfOspfLsdbRouterLinks = _HpicfOspfLsdbRouterLinks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 14, 1, 8),
    _HpicfOspfLsdbRouterLinks_Type()
)
hpicfOspfLsdbRouterLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfLsdbRouterLinks.setStatus("current")
_HpicfOspfLsdbBitE_Type = Unsigned32
_HpicfOspfLsdbBitE_Object = MibTableColumn
hpicfOspfLsdbBitE = _HpicfOspfLsdbBitE_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 14, 1, 9),
    _HpicfOspfLsdbBitE_Type()
)
hpicfOspfLsdbBitE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfLsdbBitE.setStatus("current")
_HpicfOspfRouterLSATable_Object = MibTable
hpicfOspfRouterLSATable = _HpicfOspfRouterLSATable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 15)
)
if mibBuilder.loadTexts:
    hpicfOspfRouterLSATable.setStatus("current")
_HpicfOspfRouterLSAEntry_Object = MibTableRow
hpicfOspfRouterLSAEntry = _HpicfOspfRouterLSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 15, 1)
)
hpicfOspfRouterLSAEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfLsdbAreaId"),
    (0, "OSPF-MIB", "ospfLsdbType"),
    (0, "OSPF-MIB", "ospfLsdbLsid"),
    (0, "OSPF-MIB", "ospfLsdbRouterId"),
    (0, "HP-ICF-OSPF", "hpicfOspfRouterLSANbrRtrId"),
)
if mibBuilder.loadTexts:
    hpicfOspfRouterLSAEntry.setStatus("current")
_HpicfOspfRouterLSANbrRtrId_Type = HpicfOspfRouterIdTc
_HpicfOspfRouterLSANbrRtrId_Object = MibTableColumn
hpicfOspfRouterLSANbrRtrId = _HpicfOspfRouterLSANbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 15, 1, 1),
    _HpicfOspfRouterLSANbrRtrId_Type()
)
hpicfOspfRouterLSANbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfRouterLSANbrRtrId.setStatus("current")
_HpicfOspfRouterLSAIfType_Type = Unsigned32
_HpicfOspfRouterLSAIfType_Object = MibTableColumn
hpicfOspfRouterLSAIfType = _HpicfOspfRouterLSAIfType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 15, 1, 2),
    _HpicfOspfRouterLSAIfType_Type()
)
hpicfOspfRouterLSAIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRouterLSAIfType.setStatus("current")
_HpicfOspfRouterLSAMetric_Type = Metric
_HpicfOspfRouterLSAMetric_Object = MibTableColumn
hpicfOspfRouterLSAMetric = _HpicfOspfRouterLSAMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 15, 1, 3),
    _HpicfOspfRouterLSAMetric_Type()
)
hpicfOspfRouterLSAMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRouterLSAMetric.setStatus("current")
_HpicfOspfRouterLSAIfId_Type = HpicfOspfRouterIdTc
_HpicfOspfRouterLSAIfId_Object = MibTableColumn
hpicfOspfRouterLSAIfId = _HpicfOspfRouterLSAIfId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 15, 1, 4),
    _HpicfOspfRouterLSAIfId_Type()
)
hpicfOspfRouterLSAIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRouterLSAIfId.setStatus("current")


class _HpicfOspfRouterLSATOSMetric_Type(Unsigned32):
    """Custom type hpicfOspfRouterLSATOSMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpicfOspfRouterLSATOSMetric_Type.__name__ = "Unsigned32"
_HpicfOspfRouterLSATOSMetric_Object = MibTableColumn
hpicfOspfRouterLSATOSMetric = _HpicfOspfRouterLSATOSMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 15, 1, 5),
    _HpicfOspfRouterLSATOSMetric_Type()
)
hpicfOspfRouterLSATOSMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfRouterLSATOSMetric.setStatus("current")
_HpicfOspfNetworkLSATable_Object = MibTable
hpicfOspfNetworkLSATable = _HpicfOspfNetworkLSATable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 16)
)
if mibBuilder.loadTexts:
    hpicfOspfNetworkLSATable.setStatus("current")
_HpicfOspfNetworkLSAEntry_Object = MibTableRow
hpicfOspfNetworkLSAEntry = _HpicfOspfNetworkLSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 16, 1)
)
hpicfOspfNetworkLSAEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfLsdbAreaId"),
    (0, "OSPF-MIB", "ospfLsdbType"),
    (0, "OSPF-MIB", "ospfLsdbLsid"),
    (0, "OSPF-MIB", "ospfLsdbRouterId"),
    (0, "HP-ICF-OSPF", "hpicfOspfNetworkLSASeqNum"),
)
if mibBuilder.loadTexts:
    hpicfOspfNetworkLSAEntry.setStatus("current")
_HpicfOspfNetworkLSASeqNum_Type = Unsigned32
_HpicfOspfNetworkLSASeqNum_Object = MibTableColumn
hpicfOspfNetworkLSASeqNum = _HpicfOspfNetworkLSASeqNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 16, 1, 1),
    _HpicfOspfNetworkLSASeqNum_Type()
)
hpicfOspfNetworkLSASeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfOspfNetworkLSASeqNum.setStatus("current")
_HpicfOspfNetworkLSAAttachedRouter_Type = HpicfOspfRouterIdTc
_HpicfOspfNetworkLSAAttachedRouter_Object = MibTableColumn
hpicfOspfNetworkLSAAttachedRouter = _HpicfOspfNetworkLSAAttachedRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 16, 1, 2),
    _HpicfOspfNetworkLSAAttachedRouter_Type()
)
hpicfOspfNetworkLSAAttachedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfNetworkLSAAttachedRouter.setStatus("current")
_HpicfOspfExtLsdbTable_Object = MibTable
hpicfOspfExtLsdbTable = _HpicfOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 17)
)
if mibBuilder.loadTexts:
    hpicfOspfExtLsdbTable.setStatus("current")
_HpicfOspfExtLsdbEntry_Object = MibTableRow
hpicfOspfExtLsdbEntry = _HpicfOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 17, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfExtLsdbEntry.setStatus("current")
_HpicfOspfExtLsdbMetric_Type = Unsigned32
_HpicfOspfExtLsdbMetric_Object = MibTableColumn
hpicfOspfExtLsdbMetric = _HpicfOspfExtLsdbMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 17, 1, 1),
    _HpicfOspfExtLsdbMetric_Type()
)
hpicfOspfExtLsdbMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfExtLsdbMetric.setStatus("current")
_HpicfOspfExtLsdbOptions_Type = Unsigned32
_HpicfOspfExtLsdbOptions_Object = MibTableColumn
hpicfOspfExtLsdbOptions = _HpicfOspfExtLsdbOptions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 17, 1, 2),
    _HpicfOspfExtLsdbOptions_Type()
)
hpicfOspfExtLsdbOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfExtLsdbOptions.setStatus("current")
_HpicfOspfExtLsdbFwdingAddress_Type = HpicfOspfRouterIdTc
_HpicfOspfExtLsdbFwdingAddress_Object = MibTableColumn
hpicfOspfExtLsdbFwdingAddress = _HpicfOspfExtLsdbFwdingAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 17, 1, 3),
    _HpicfOspfExtLsdbFwdingAddress_Type()
)
hpicfOspfExtLsdbFwdingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfExtLsdbFwdingAddress.setStatus("current")
_HpicfOspfExtLsdbExtRouteTags_Type = Unsigned32
_HpicfOspfExtLsdbExtRouteTags_Object = MibTableColumn
hpicfOspfExtLsdbExtRouteTags = _HpicfOspfExtLsdbExtRouteTags_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 17, 1, 4),
    _HpicfOspfExtLsdbExtRouteTags_Type()
)
hpicfOspfExtLsdbExtRouteTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfExtLsdbExtRouteTags.setStatus("current")
_HpicfOspfExtLsdbBitE_Type = Unsigned32
_HpicfOspfExtLsdbBitE_Object = MibTableColumn
hpicfOspfExtLsdbBitE = _HpicfOspfExtLsdbBitE_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 17, 1, 5),
    _HpicfOspfExtLsdbBitE_Type()
)
hpicfOspfExtLsdbBitE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfOspfExtLsdbBitE.setStatus("current")
_HpicfOspfIfMetricObjects_ObjectIdentity = ObjectIdentity
hpicfOspfIfMetricObjects = _HpicfOspfIfMetricObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 18)
)
_HpicfOspfIfMetricTable_Object = MibTable
hpicfOspfIfMetricTable = _HpicfOspfIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 18, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfIfMetricTable.setStatus("current")
_HpicfOspfIfMetricEntry_Object = MibTableRow
hpicfOspfIfMetricEntry = _HpicfOspfIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 18, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfIfMetricEntry.setStatus("current")


class _HpicfOspfIfFlagValue_Type(Integer32):
    """Custom type hpicfOspfIfFlagValue based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_HpicfOspfIfFlagValue_Type.__name__ = "Integer32"
_HpicfOspfIfFlagValue_Object = MibTableColumn
hpicfOspfIfFlagValue = _HpicfOspfIfFlagValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 18, 1, 1, 1),
    _HpicfOspfIfFlagValue_Type()
)
hpicfOspfIfFlagValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfOspfIfFlagValue.setStatus("current")
ospfNbrEntry.registerAugmentions(
    ("HP-ICF-OSPF",
     "hpicfOspfNbrEntry")
)
hpicfOspfNbrEntry.setIndexNames(*ospfNbrEntry.getIndexNames())
ospfAreaAggregateEntry.registerAugmentions(
    ("HP-ICF-OSPF",
     "hpicfOspfAreaAggregateEntry")
)
hpicfOspfAreaAggregateEntry.setIndexNames(*ospfAreaAggregateEntry.getIndexNames())
ospfIfEntry.registerAugmentions(
    ("HP-ICF-OSPF",
     "hpicfOspfIfEntry")
)
hpicfOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfLsdbEntry.registerAugmentions(
    ("HP-ICF-OSPF",
     "hpicfOspfAreaLsdbEntry")
)
hpicfOspfAreaLsdbEntry.setIndexNames(*ospfLsdbEntry.getIndexNames())
ospfExtLsdbEntry.registerAugmentions(
    ("HP-ICF-OSPF",
     "hpicfOspfExtLsdbEntry")
)
hpicfOspfExtLsdbEntry.setIndexNames(*ospfExtLsdbEntry.getIndexNames())
ospfIfMetricEntry.registerAugmentions(
    ("HP-ICF-OSPF",
     "hpicfOspfIfMetricEntry")
)
hpicfOspfIfMetricEntry.setIndexNames(*ospfIfMetricEntry.getIndexNames())

# Managed Objects groups

hpicfOspfBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 1)
)
hpicfOspfBaseGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspf1583CompatibilityMode"),
        ("HP-ICF-OSPF", "hpicfOspfDefaultImportMetric"),
        ("HP-ICF-OSPF", "hpicfOspfDefaultImportMetricType"))
)
if mibBuilder.loadTexts:
    hpicfOspfBaseGroup.setStatus("current")

hpicfOspfRedistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 2)
)
hpicfOspfRedistGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfRedistEnabled"),
        ("HP-ICF-OSPF", "hpicfOspfRedistRestrictStatus"))
)
if mibBuilder.loadTexts:
    hpicfOspfRedistGroup.setStatus("current")

hpicfOspfDistanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 3)
)
hpicfOspfDistanceGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfIntraAreaDistance"),
        ("HP-ICF-OSPF", "hpicfOspfInterAreaDistance"),
        ("HP-ICF-OSPF", "hpicfOspfExternalDistance"))
)
if mibBuilder.loadTexts:
    hpicfOspfDistanceGroup.setStatus("current")

hpicfOspfStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 4)
)
hpicfOspfStatisticGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfSentHelloPkt"),
        ("HP-ICF-OSPF", "hpicfOspfSentDDPkt"),
        ("HP-ICF-OSPF", "hpicfOspfSentLSRPkt"),
        ("HP-ICF-OSPF", "hpicfOspfSentLSUPkt"),
        ("HP-ICF-OSPF", "hpicfOspfSentLSAPkt"),
        ("HP-ICF-OSPF", "hpicfOspfRcvdHelloPkt"),
        ("HP-ICF-OSPF", "hpicfOspfRcvdDDPkt"),
        ("HP-ICF-OSPF", "hpicfOspfRcvdLSRPkt"),
        ("HP-ICF-OSPF", "hpicfOspfRcvdLSUPkt"),
        ("HP-ICF-OSPF", "hpicfOspfRcvdLSAPkt"),
        ("HP-ICF-OSPF", "hpicfOspfIfErrorCount"),
        ("HP-ICF-OSPF", "hpicfOspfClearCounters"),
        ("HP-ICF-OSPF", "hpicfOspfSpfReason"),
        ("HP-ICF-OSPF", "hpicfOspfSpfTime"))
)
if mibBuilder.loadTexts:
    hpicfOspfStatisticGroup.setStatus("current")

hpicfOspfSpfTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 5)
)
hpicfOspfSpfTimerGroup.setObjects(
    ("HP-ICF-OSPF", "hpicfOspfSpfTimerElapsed")
)
if mibBuilder.loadTexts:
    hpicfOspfSpfTimerGroup.setStatus("current")

hpicfOspfLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 6)
)
hpicfOspfLogGroup.setObjects(
    ("HP-ICF-OSPF", "hpicfOspfLogAction")
)
if mibBuilder.loadTexts:
    hpicfOspfLogGroup.setStatus("current")

hpicfOspfNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 7)
)
hpicfOspfNbrGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfNbrUpTime"),
        ("HP-ICF-OSPF", "hpicfOspfNbrTimeToExpiry"),
        ("HP-ICF-OSPF", "hpicfOspfNbrDesignatedRouter"),
        ("HP-ICF-OSPF", "hpicfOspfNbrBackupDesignatedRouter"),
        ("HP-ICF-OSPF", "hpicfOspfNbrAreaId"),
        ("HP-ICF-OSPF", "hpicfOspfNbrInterfaceName"))
)
if mibBuilder.loadTexts:
    hpicfOspfNbrGroup.setStatus("deprecated")

hpicfOspfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 8)
)
hpicfOspfIfGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfIfPassive"),
        ("HP-ICF-OSPF", "hpicfOspfIfNbrCount"),
        ("HP-ICF-OSPF", "hpicfOspfIfBfdEnbl"))
)
if mibBuilder.loadTexts:
    hpicfOspfIfGroup.setStatus("current")

hpicfOspfAreaLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 9)
)
hpicfOspfAreaLsdbGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfAreaLsdbRtrCapBits"),
        ("HP-ICF-OSPF", "hpicfOspfAreaLsdbOptions"),
        ("HP-ICF-OSPF", "hpicfOspfAreaLsdbMetric"),
        ("HP-ICF-OSPF", "hpicfOspfAreaLsdbAddrPrefix"),
        ("HP-ICF-OSPF", "hpicfOspfAreaLsdbFwdingAddress"),
        ("HP-ICF-OSPF", "hpicfOspfAreaLsdbExtRouteTags"),
        ("HP-ICF-OSPF", "hpicfOspfRouterLSAIfType"),
        ("HP-ICF-OSPF", "hpicfOspfRouterLSAMetric"),
        ("HP-ICF-OSPF", "hpicfOspfRouterLSAIfId"),
        ("HP-ICF-OSPF", "hpicfOspfNetworkLSAAttachedRouter"),
        ("HP-ICF-OSPF", "hpicfOspfTOS"),
        ("HP-ICF-OSPF", "hpicfOspfLsdbRouterLinks"),
        ("HP-ICF-OSPF", "hpicfOspfRouterLSATOSMetric"),
        ("HP-ICF-OSPF", "hpicfOspfLsdbBitE"))
)
if mibBuilder.loadTexts:
    hpicfOspfAreaLsdbGroup.setStatus("current")

hpicfOspfExtLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 10)
)
hpicfOspfExtLsdbGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfExtLsdbMetric"),
        ("HP-ICF-OSPF", "hpicfOspfExtLsdbOptions"),
        ("HP-ICF-OSPF", "hpicfOspfExtLsdbFwdingAddress"),
        ("HP-ICF-OSPF", "hpicfOspfExtLsdbExtRouteTags"),
        ("HP-ICF-OSPF", "hpicfOspfExtLsdbBitE"))
)
if mibBuilder.loadTexts:
    hpicfOspfExtLsdbGroup.setStatus("current")

hpicfOspfAreaAggregateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 11)
)
hpicfOspfAreaAggregateGroup.setObjects(
    ("HP-ICF-OSPF", "hpicfOspfAreaAggregateCost")
)
if mibBuilder.loadTexts:
    hpicfOspfAreaAggregateGroup.setStatus("current")

hpicfOspfSpfDelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 12)
)
hpicfOspfSpfDelayGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfSpfThrottleStartInterval"),
        ("HP-ICF-OSPF", "hpicfOspfSpfThrottleWaitInterval"),
        ("HP-ICF-OSPF", "hpicfOspfSpfThrottleMaxWaitTime"),
        ("HP-ICF-OSPF", "hpicfOspfSpfThrottleCurrentSpfInterval"))
)
if mibBuilder.loadTexts:
    hpicfOspfSpfDelayGroup.setStatus("current")

hpicfOspfAreaAggregateGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 13)
)
hpicfOspfAreaAggregateGroup1.setObjects(
    ("HP-ICF-OSPF", "hpicfOspfAreaAggregateType")
)
if mibBuilder.loadTexts:
    hpicfOspfAreaAggregateGroup1.setStatus("current")

hpicfOspfNbrGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 14)
)
hpicfOspfNbrGroup1.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfNbrUpTime"),
        ("HP-ICF-OSPF", "hpicfOspfNbrTimeToExpiry"),
        ("HP-ICF-OSPF", "hpicfOspfNbrDesignatedRouter"),
        ("HP-ICF-OSPF", "hpicfOspfNbrBackupDesignatedRouter"),
        ("HP-ICF-OSPF", "hpicfOspfNbrAreaId"),
        ("HP-ICF-OSPF", "hpicfOspfNbrInterfaceName"),
        ("HP-ICF-OSPF", "hpicfOspfNbrBfdState"))
)
if mibBuilder.loadTexts:
    hpicfOspfNbrGroup1.setStatus("current")

hpicfOspfReferenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 15)
)
hpicfOspfReferenceGroup.setObjects(
    ("HP-ICF-OSPF", "hpicfOspfReferenceCost")
)
if mibBuilder.loadTexts:
    hpicfOspfReferenceGroup.setStatus("current")

hpicfOspfMetricGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 1, 16)
)
hpicfOspfMetricGroup.setObjects(
    ("HP-ICF-OSPF", "hpicfOspfIfFlagValue")
)
if mibBuilder.loadTexts:
    hpicfOspfMetricGroup.setStatus("current")

hpicfOspfReqManGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 3, 1)
)
hpicfOspfReqManGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfReqType"),
        ("HP-ICF-OSPF", "hpicfOspfReqLsid"),
        ("HP-ICF-OSPF", "hpicfOspfReqRouterId"))
)
if mibBuilder.loadTexts:
    hpicfOspfReqManGroup.setStatus("current")

hpicfOspfReqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 3, 2)
)
hpicfOspfReqGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfReqSequence"),
        ("HP-ICF-OSPF", "hpicfOspfReqChecksum"),
        ("HP-ICF-OSPF", "hpicfOspfReqAge"))
)
if mibBuilder.loadTexts:
    hpicfOspfReqGroup.setStatus("current")

hpicfOspfRetransManGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 4, 1)
)
hpicfOspfRetransManGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfRetransType"),
        ("HP-ICF-OSPF", "hpicfOspfRetransLsid"),
        ("HP-ICF-OSPF", "hpicfOspfRetransRouterId"))
)
if mibBuilder.loadTexts:
    hpicfOspfRetransManGroup.setStatus("current")

hpicfOspfRetransGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 4, 2)
)
hpicfOspfRetransGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfRetransSequence"),
        ("HP-ICF-OSPF", "hpicfOspfRetransChecksum"),
        ("HP-ICF-OSPF", "hpicfOspfRetransAge"))
)
if mibBuilder.loadTexts:
    hpicfOspfRetransGroup.setStatus("current")

hpicfOspfFloodManGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 5, 1)
)
hpicfOspfFloodManGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfFloodType"),
        ("HP-ICF-OSPF", "hpicfOspfFloodLsid"),
        ("HP-ICF-OSPF", "hpicfOspfFloodRouterId"))
)
if mibBuilder.loadTexts:
    hpicfOspfFloodManGroup.setStatus("current")

hpicfOspfFloodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 5, 2)
)
hpicfOspfFloodGroup.setObjects(
      *(("HP-ICF-OSPF", "hpicfOspfFloodSequence"),
        ("HP-ICF-OSPF", "hpicfOspfFloodChecksum"),
        ("HP-ICF-OSPF", "hpicfOspfFloodAge"))
)
if mibBuilder.loadTexts:
    hpicfOspfFloodGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfOspfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfOspfCompliance.setStatus(
        "current"
    )

hpicfOspfReqCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfOspfReqCompliance.setStatus(
        "current"
    )

hpicfOspfFloodCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfOspfFloodCompliance.setStatus(
        "current"
    )

hpicfOspfRetransCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfOspfRetransCompliance.setStatus(
        "current"
    )

hpicfOspfCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfOspfCompliance1.setStatus(
        "deprecated"
    )

hpicfOspfSpfDelayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hpicfOspfSpfDelayCompliance.setStatus(
        "current"
    )

hpicfOspfAreaAggregateCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hpicfOspfAreaAggregateCompliance.setStatus(
        "current"
    )

hpicfOspfCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 2, 8)
)
if mibBuilder.loadTexts:
    hpicfOspfCompliance2.setStatus(
        "deprecated"
    )

hpicfOspfCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14, 2, 2, 9)
)
if mibBuilder.loadTexts:
    hpicfOspfCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-OSPF",
    **{"HpicfOspfRouterIdTc": HpicfOspfRouterIdTc,
       "HpicfOspfLogType": HpicfOspfLogType,
       "HpicfOspfLogAction": HpicfOspfLogAction,
       "hpicfOspf": hpicfOspf,
       "hpicfOspfObjects": hpicfOspfObjects,
       "hpicfOspfGeneral": hpicfOspfGeneral,
       "hpicfOspf1583CompatibilityMode": hpicfOspf1583CompatibilityMode,
       "hpicfOspfDefaultImportMetric": hpicfOspfDefaultImportMetric,
       "hpicfOspfDefaultImportMetricType": hpicfOspfDefaultImportMetricType,
       "hpicfOspfIntraAreaDistance": hpicfOspfIntraAreaDistance,
       "hpicfOspfInterAreaDistance": hpicfOspfInterAreaDistance,
       "hpicfOspfExternalDistance": hpicfOspfExternalDistance,
       "hpicfOspfSpfThrottleStartInterval": hpicfOspfSpfThrottleStartInterval,
       "hpicfOspfSpfThrottleWaitInterval": hpicfOspfSpfThrottleWaitInterval,
       "hpicfOspfSpfThrottleMaxWaitTime": hpicfOspfSpfThrottleMaxWaitTime,
       "hpicfOspfSpfThrottleCurrentSpfInterval": hpicfOspfSpfThrottleCurrentSpfInterval,
       "hpicfOspfReferenceCost": hpicfOspfReferenceCost,
       "hpicfOspfRedistTable": hpicfOspfRedistTable,
       "hpicfOspfRedistEntry": hpicfOspfRedistEntry,
       "hpicfOspfRedistSrcProto": hpicfOspfRedistSrcProto,
       "hpicfOspfRedistEnabled": hpicfOspfRedistEnabled,
       "hpicfOspfRedistRestrictTable": hpicfOspfRedistRestrictTable,
       "hpicfOspfRedistRestrictEntry": hpicfOspfRedistRestrictEntry,
       "hpicfOspfRedistRestrictAddr": hpicfOspfRedistRestrictAddr,
       "hpicfOspfRedistRestrictMask": hpicfOspfRedistRestrictMask,
       "hpicfOspfRedistRestrictStatus": hpicfOspfRedistRestrictStatus,
       "hpicfOspfLogTable": hpicfOspfLogTable,
       "hpicfOspfLogEntry": hpicfOspfLogEntry,
       "hpicfOspfLogType": hpicfOspfLogType,
       "hpicfOspfLogAction": hpicfOspfLogAction,
       "hpicfOspfNbrTable": hpicfOspfNbrTable,
       "hpicfOspfNbrEntry": hpicfOspfNbrEntry,
       "hpicfOspfNbrUpTime": hpicfOspfNbrUpTime,
       "hpicfOspfNbrTimeToExpiry": hpicfOspfNbrTimeToExpiry,
       "hpicfOspfNbrDesignatedRouter": hpicfOspfNbrDesignatedRouter,
       "hpicfOspfNbrBackupDesignatedRouter": hpicfOspfNbrBackupDesignatedRouter,
       "hpicfOspfNbrAreaId": hpicfOspfNbrAreaId,
       "hpicfOspfNbrInterfaceName": hpicfOspfNbrInterfaceName,
       "hpicfOspfNbrBfdState": hpicfOspfNbrBfdState,
       "hpicfOspfAreaAggregateTable": hpicfOspfAreaAggregateTable,
       "hpicfOspfAreaAggregateEntry": hpicfOspfAreaAggregateEntry,
       "hpicfOspfAreaAggregateCost": hpicfOspfAreaAggregateCost,
       "hpicfOspfAreaAggregateType": hpicfOspfAreaAggregateType,
       "hpicfOspfConformance": hpicfOspfConformance,
       "hpicfOspfGroups": hpicfOspfGroups,
       "hpicfOspfBaseGroup": hpicfOspfBaseGroup,
       "hpicfOspfRedistGroup": hpicfOspfRedistGroup,
       "hpicfOspfDistanceGroup": hpicfOspfDistanceGroup,
       "hpicfOspfStatisticGroup": hpicfOspfStatisticGroup,
       "hpicfOspfSpfTimerGroup": hpicfOspfSpfTimerGroup,
       "hpicfOspfLogGroup": hpicfOspfLogGroup,
       "hpicfOspfNbrGroup": hpicfOspfNbrGroup,
       "hpicfOspfIfGroup": hpicfOspfIfGroup,
       "hpicfOspfAreaLsdbGroup": hpicfOspfAreaLsdbGroup,
       "hpicfOspfExtLsdbGroup": hpicfOspfExtLsdbGroup,
       "hpicfOspfAreaAggregateGroup": hpicfOspfAreaAggregateGroup,
       "hpicfOspfSpfDelayGroup": hpicfOspfSpfDelayGroup,
       "hpicfOspfAreaAggregateGroup1": hpicfOspfAreaAggregateGroup1,
       "hpicfOspfNbrGroup1": hpicfOspfNbrGroup1,
       "hpicfOspfReferenceGroup": hpicfOspfReferenceGroup,
       "hpicfOspfMetricGroup": hpicfOspfMetricGroup,
       "hpicfOspfCompliances": hpicfOspfCompliances,
       "hpicfOspfCompliance": hpicfOspfCompliance,
       "hpicfOspfReqCompliance": hpicfOspfReqCompliance,
       "hpicfOspfFloodCompliance": hpicfOspfFloodCompliance,
       "hpicfOspfRetransCompliance": hpicfOspfRetransCompliance,
       "hpicfOspfCompliance1": hpicfOspfCompliance1,
       "hpicfOspfSpfDelayCompliance": hpicfOspfSpfDelayCompliance,
       "hpicfOspfAreaAggregateCompliance": hpicfOspfAreaAggregateCompliance,
       "hpicfOspfCompliance2": hpicfOspfCompliance2,
       "hpicfOspfCompliance3": hpicfOspfCompliance3,
       "hpicfOspfReqGroups": hpicfOspfReqGroups,
       "hpicfOspfReqManGroup": hpicfOspfReqManGroup,
       "hpicfOspfReqGroup": hpicfOspfReqGroup,
       "hpicfOspfRetransGroups": hpicfOspfRetransGroups,
       "hpicfOspfRetransManGroup": hpicfOspfRetransManGroup,
       "hpicfOspfRetransGroup": hpicfOspfRetransGroup,
       "hpicfOspfFloodGroups": hpicfOspfFloodGroups,
       "hpicfOspfFloodManGroup": hpicfOspfFloodManGroup,
       "hpicfOspfFloodGroup": hpicfOspfFloodGroup,
       "hpicfOspfRouteGroup": hpicfOspfRouteGroup,
       "hpicfOspfNssaType1": hpicfOspfNssaType1,
       "hpicfOspfNssaType2": hpicfOspfNssaType2,
       "hpicfOspfIfTable": hpicfOspfIfTable,
       "hpicfOspfIfEntry": hpicfOspfIfEntry,
       "hpicfOspfIfPassive": hpicfOspfIfPassive,
       "hpicfOspfIfNbrCount": hpicfOspfIfNbrCount,
       "hpicfOspfIfBfdEnbl": hpicfOspfIfBfdEnbl,
       "hpicfOspfIfStatsTable": hpicfOspfIfStatsTable,
       "hpicfOspfIfStatsEntry": hpicfOspfIfStatsEntry,
       "hpicfOspfSentHelloPkt": hpicfOspfSentHelloPkt,
       "hpicfOspfSentDDPkt": hpicfOspfSentDDPkt,
       "hpicfOspfSentLSRPkt": hpicfOspfSentLSRPkt,
       "hpicfOspfSentLSUPkt": hpicfOspfSentLSUPkt,
       "hpicfOspfSentLSAPkt": hpicfOspfSentLSAPkt,
       "hpicfOspfRcvdHelloPkt": hpicfOspfRcvdHelloPkt,
       "hpicfOspfRcvdDDPkt": hpicfOspfRcvdDDPkt,
       "hpicfOspfRcvdLSRPkt": hpicfOspfRcvdLSRPkt,
       "hpicfOspfRcvdLSUPkt": hpicfOspfRcvdLSUPkt,
       "hpicfOspfRcvdLSAPkt": hpicfOspfRcvdLSAPkt,
       "hpicfOspfIfErrorTable": hpicfOspfIfErrorTable,
       "hpicfOspfIfErrorEntry": hpicfOspfIfErrorEntry,
       "hpicfOspfIfErrorType": hpicfOspfIfErrorType,
       "hpicfOspfIfErrorCount": hpicfOspfIfErrorCount,
       "hpicfOspfIfClearStatsTable": hpicfOspfIfClearStatsTable,
       "hpicfOspfIfClearStatsEntry": hpicfOspfIfClearStatsEntry,
       "hpicfOspfClearCounters": hpicfOspfClearCounters,
       "hpicfOspfSpfTable": hpicfOspfSpfTable,
       "hpicfOspfSpfEntry": hpicfOspfSpfEntry,
       "hpicfOspfSpfInstance": hpicfOspfSpfInstance,
       "hpicfOspfSpfReason": hpicfOspfSpfReason,
       "hpicfOspfSpfTime": hpicfOspfSpfTime,
       "hpicfOspfReqTable": hpicfOspfReqTable,
       "hpicfOspfReqEntry": hpicfOspfReqEntry,
       "hpicfOspfReqType": hpicfOspfReqType,
       "hpicfOspfReqLsid": hpicfOspfReqLsid,
       "hpicfOspfReqRouterId": hpicfOspfReqRouterId,
       "hpicfOspfReqSequence": hpicfOspfReqSequence,
       "hpicfOspfReqAge": hpicfOspfReqAge,
       "hpicfOspfReqChecksum": hpicfOspfReqChecksum,
       "hpicfOspfRetransTable": hpicfOspfRetransTable,
       "hpicfOspfRetransEntry": hpicfOspfRetransEntry,
       "hpicfOspfRetransType": hpicfOspfRetransType,
       "hpicfOspfRetransLsid": hpicfOspfRetransLsid,
       "hpicfOspfRetransRouterId": hpicfOspfRetransRouterId,
       "hpicfOspfRetransSequence": hpicfOspfRetransSequence,
       "hpicfOspfRetransAge": hpicfOspfRetransAge,
       "hpicfOspfRetransChecksum": hpicfOspfRetransChecksum,
       "hpicfOspfFloodTable": hpicfOspfFloodTable,
       "hpicfOspfFloodEntry": hpicfOspfFloodEntry,
       "hpicfOspfFloodType": hpicfOspfFloodType,
       "hpicfOspfFloodLsid": hpicfOspfFloodLsid,
       "hpicfOspfFloodRouterId": hpicfOspfFloodRouterId,
       "hpicfOspfFloodSequence": hpicfOspfFloodSequence,
       "hpicfOspfFloodAge": hpicfOspfFloodAge,
       "hpicfOspfFloodChecksum": hpicfOspfFloodChecksum,
       "hpicfOspfSpfTimerElapsed": hpicfOspfSpfTimerElapsed,
       "hpicfOspfAreaLsdbTable": hpicfOspfAreaLsdbTable,
       "hpicfOspfAreaLsdbEntry": hpicfOspfAreaLsdbEntry,
       "hpicfOspfAreaLsdbRtrCapBits": hpicfOspfAreaLsdbRtrCapBits,
       "hpicfOspfAreaLsdbOptions": hpicfOspfAreaLsdbOptions,
       "hpicfOspfAreaLsdbMetric": hpicfOspfAreaLsdbMetric,
       "hpicfOspfAreaLsdbAddrPrefix": hpicfOspfAreaLsdbAddrPrefix,
       "hpicfOspfAreaLsdbFwdingAddress": hpicfOspfAreaLsdbFwdingAddress,
       "hpicfOspfAreaLsdbExtRouteTags": hpicfOspfAreaLsdbExtRouteTags,
       "hpicfOspfTOS": hpicfOspfTOS,
       "hpicfOspfLsdbRouterLinks": hpicfOspfLsdbRouterLinks,
       "hpicfOspfLsdbBitE": hpicfOspfLsdbBitE,
       "hpicfOspfRouterLSATable": hpicfOspfRouterLSATable,
       "hpicfOspfRouterLSAEntry": hpicfOspfRouterLSAEntry,
       "hpicfOspfRouterLSANbrRtrId": hpicfOspfRouterLSANbrRtrId,
       "hpicfOspfRouterLSAIfType": hpicfOspfRouterLSAIfType,
       "hpicfOspfRouterLSAMetric": hpicfOspfRouterLSAMetric,
       "hpicfOspfRouterLSAIfId": hpicfOspfRouterLSAIfId,
       "hpicfOspfRouterLSATOSMetric": hpicfOspfRouterLSATOSMetric,
       "hpicfOspfNetworkLSATable": hpicfOspfNetworkLSATable,
       "hpicfOspfNetworkLSAEntry": hpicfOspfNetworkLSAEntry,
       "hpicfOspfNetworkLSASeqNum": hpicfOspfNetworkLSASeqNum,
       "hpicfOspfNetworkLSAAttachedRouter": hpicfOspfNetworkLSAAttachedRouter,
       "hpicfOspfExtLsdbTable": hpicfOspfExtLsdbTable,
       "hpicfOspfExtLsdbEntry": hpicfOspfExtLsdbEntry,
       "hpicfOspfExtLsdbMetric": hpicfOspfExtLsdbMetric,
       "hpicfOspfExtLsdbOptions": hpicfOspfExtLsdbOptions,
       "hpicfOspfExtLsdbFwdingAddress": hpicfOspfExtLsdbFwdingAddress,
       "hpicfOspfExtLsdbExtRouteTags": hpicfOspfExtLsdbExtRouteTags,
       "hpicfOspfExtLsdbBitE": hpicfOspfExtLsdbBitE,
       "hpicfOspfIfMetricObjects": hpicfOspfIfMetricObjects,
       "hpicfOspfIfMetricTable": hpicfOspfIfMetricTable,
       "hpicfOspfIfMetricEntry": hpicfOspfIfMetricEntry,
       "hpicfOspfIfFlagValue": hpicfOspfIfFlagValue}
)

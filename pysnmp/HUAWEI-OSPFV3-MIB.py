# SNMP MIB module (HUAWEI-OSPFV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-OSPFV3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:26 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(BigMetric,
 DesignatedRouterPriority,
 HelloRange,
 Metric,
 Status) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "BigMetric",
    "DesignatedRouterPriority",
    "HelloRange",
    "Metric",
    "Status")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

hwOspfv3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147)
)
hwOspfv3.setRevisions(
        ("2015-05-03 11:10",
         "2015-04-03 11:10",
         "2007-06-12 21:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWOspfv3UpToRefreshIntervalTc(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class HWOspfv3DeadIntRangeTc(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class HWOspfv3RouterIdTc(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class HWOspfv3LsIdTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class HWOspfv3AreaIdTc(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class HWOspfv3IfInstIdTc(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class HWOspfv3LsaSequenceTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class HWOspfv3LsaAgeTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
        ValueRangeConstraint(32768, 36368),
    )



class HWHelloRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_HwOspfv3Notifications_ObjectIdentity = ObjectIdentity
hwOspfv3Notifications = _HwOspfv3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0)
)
_HwOspfv3Objects_ObjectIdentity = ObjectIdentity
hwOspfv3Objects = _HwOspfv3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1)
)
_HwOspfv3GeneralGroup_ObjectIdentity = ObjectIdentity
hwOspfv3GeneralGroup = _HwOspfv3GeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1)
)
_HwOspfv3RouterId_Type = HWOspfv3RouterIdTc
_HwOspfv3RouterId_Object = MibScalar
hwOspfv3RouterId = _HwOspfv3RouterId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 1),
    _HwOspfv3RouterId_Type()
)
hwOspfv3RouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOspfv3RouterId.setStatus("current")
_HwOspfv3AdminStatus_Type = Status
_HwOspfv3AdminStatus_Object = MibScalar
hwOspfv3AdminStatus = _HwOspfv3AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 2),
    _HwOspfv3AdminStatus_Type()
)
hwOspfv3AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOspfv3AdminStatus.setStatus("current")


class _HwOspfv3VersionNumber_Type(Integer32):
    """Custom type hwOspfv3VersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("version3", 3)
    )


_HwOspfv3VersionNumber_Type.__name__ = "Integer32"
_HwOspfv3VersionNumber_Object = MibScalar
hwOspfv3VersionNumber = _HwOspfv3VersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 3),
    _HwOspfv3VersionNumber_Type()
)
hwOspfv3VersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VersionNumber.setStatus("current")
_HwOspfv3AreaBdrRtrStatus_Type = TruthValue
_HwOspfv3AreaBdrRtrStatus_Object = MibScalar
hwOspfv3AreaBdrRtrStatus = _HwOspfv3AreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 4),
    _HwOspfv3AreaBdrRtrStatus_Type()
)
hwOspfv3AreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaBdrRtrStatus.setStatus("current")
_HwOspfv3AsBdrRtrStatus_Type = TruthValue
_HwOspfv3AsBdrRtrStatus_Object = MibScalar
hwOspfv3AsBdrRtrStatus = _HwOspfv3AsBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 5),
    _HwOspfv3AsBdrRtrStatus_Type()
)
hwOspfv3AsBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOspfv3AsBdrRtrStatus.setStatus("current")
_HwOspfv3AsScopeLsaCount_Type = Gauge32
_HwOspfv3AsScopeLsaCount_Object = MibScalar
hwOspfv3AsScopeLsaCount = _HwOspfv3AsScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 6),
    _HwOspfv3AsScopeLsaCount_Type()
)
hwOspfv3AsScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AsScopeLsaCount.setStatus("current")
_HwOspfv3AsScopeLsaCksumSum_Type = Unsigned32
_HwOspfv3AsScopeLsaCksumSum_Object = MibScalar
hwOspfv3AsScopeLsaCksumSum = _HwOspfv3AsScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 7),
    _HwOspfv3AsScopeLsaCksumSum_Type()
)
hwOspfv3AsScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AsScopeLsaCksumSum.setStatus("current")
_HwOspfv3OriginateNewLsas_Type = Counter32
_HwOspfv3OriginateNewLsas_Object = MibScalar
hwOspfv3OriginateNewLsas = _HwOspfv3OriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 8),
    _HwOspfv3OriginateNewLsas_Type()
)
hwOspfv3OriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3OriginateNewLsas.setStatus("current")
_HwOspfv3RxNewLsas_Type = Counter32
_HwOspfv3RxNewLsas_Object = MibScalar
hwOspfv3RxNewLsas = _HwOspfv3RxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 9),
    _HwOspfv3RxNewLsas_Type()
)
hwOspfv3RxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3RxNewLsas.setStatus("current")
_HwOspfv3ExtLsaCount_Type = Gauge32
_HwOspfv3ExtLsaCount_Object = MibScalar
hwOspfv3ExtLsaCount = _HwOspfv3ExtLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 10),
    _HwOspfv3ExtLsaCount_Type()
)
hwOspfv3ExtLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3ExtLsaCount.setStatus("current")


class _HwOspfv3ExtAreaLsdbLimit_Type(Integer32):
    """Custom type hwOspfv3ExtAreaLsdbLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_HwOspfv3ExtAreaLsdbLimit_Type.__name__ = "Integer32"
_HwOspfv3ExtAreaLsdbLimit_Object = MibScalar
hwOspfv3ExtAreaLsdbLimit = _HwOspfv3ExtAreaLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 11),
    _HwOspfv3ExtAreaLsdbLimit_Type()
)
hwOspfv3ExtAreaLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOspfv3ExtAreaLsdbLimit.setStatus("current")


class _HwOspfv3RestartSupport_Type(Integer32):
    """Custom type hwOspfv3RestartSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("plannedAndUnplanned", 3),
          ("plannedOnly", 2))
    )


_HwOspfv3RestartSupport_Type.__name__ = "Integer32"
_HwOspfv3RestartSupport_Object = MibScalar
hwOspfv3RestartSupport = _HwOspfv3RestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 12),
    _HwOspfv3RestartSupport_Type()
)
hwOspfv3RestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOspfv3RestartSupport.setStatus("current")
_HwOspfv3RestartInterval_Type = HWOspfv3UpToRefreshIntervalTc
_HwOspfv3RestartInterval_Object = MibScalar
hwOspfv3RestartInterval = _HwOspfv3RestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 13),
    _HwOspfv3RestartInterval_Type()
)
hwOspfv3RestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOspfv3RestartInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3RestartInterval.setUnits("seconds")


class _HwOspfv3RestartStatus_Type(Integer32):
    """Custom type hwOspfv3RestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRestarting", 1),
          ("plannedRestart", 2),
          ("unplannedRestart", 3))
    )


_HwOspfv3RestartStatus_Type.__name__ = "Integer32"
_HwOspfv3RestartStatus_Object = MibScalar
hwOspfv3RestartStatus = _HwOspfv3RestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 14),
    _HwOspfv3RestartStatus_Type()
)
hwOspfv3RestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3RestartStatus.setStatus("current")
_HwOspfv3RestartAge_Type = HWOspfv3UpToRefreshIntervalTc
_HwOspfv3RestartAge_Object = MibScalar
hwOspfv3RestartAge = _HwOspfv3RestartAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 15),
    _HwOspfv3RestartAge_Type()
)
hwOspfv3RestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3RestartAge.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3RestartAge.setUnits("seconds")


class _HwOspfv3RestartExitRc_Type(Integer32):
    """Custom type hwOspfv3RestartExitRc based on Integer32"""
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
        *(("completed", 3),
          ("inProgress", 2),
          ("none", 1),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_HwOspfv3RestartExitRc_Type.__name__ = "Integer32"
_HwOspfv3RestartExitRc_Object = MibScalar
hwOspfv3RestartExitRc = _HwOspfv3RestartExitRc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 16),
    _HwOspfv3RestartExitRc_Type()
)
hwOspfv3RestartExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3RestartExitRc.setStatus("current")
_HwOspfv3NotificationEnable_Type = TruthValue
_HwOspfv3NotificationEnable_Object = MibScalar
hwOspfv3NotificationEnable = _HwOspfv3NotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 17),
    _HwOspfv3NotificationEnable_Type()
)
hwOspfv3NotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOspfv3NotificationEnable.setStatus("current")


class _HwOspfv3ReferenceBandwidth_Type(Unsigned32):
    """Custom type hwOspfv3ReferenceBandwidth based on Unsigned32"""
    defaultValue = 100000


_HwOspfv3ReferenceBandwidth_Object = MibScalar
hwOspfv3ReferenceBandwidth = _HwOspfv3ReferenceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 1, 18),
    _HwOspfv3ReferenceBandwidth_Type()
)
hwOspfv3ReferenceBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOspfv3ReferenceBandwidth.setStatus("current")
_HwOspfv3AreaTable_Object = MibTable
hwOspfv3AreaTable = _HwOspfv3AreaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2)
)
if mibBuilder.loadTexts:
    hwOspfv3AreaTable.setStatus("current")
_HwOspfv3AreaEntry_Object = MibTableRow
hwOspfv3AreaEntry = _HwOspfv3AreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1)
)
hwOspfv3AreaEntry.setIndexNames(
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AreaId"),
)
if mibBuilder.loadTexts:
    hwOspfv3AreaEntry.setStatus("current")
_HwOspfv3AreaId_Type = HWOspfv3AreaIdTc
_HwOspfv3AreaId_Object = MibTableColumn
hwOspfv3AreaId = _HwOspfv3AreaId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 1),
    _HwOspfv3AreaId_Type()
)
hwOspfv3AreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AreaId.setStatus("current")


class _HwOspfv3AreaImportAsExtern_Type(Integer32):
    """Custom type hwOspfv3AreaImportAsExtern based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("importExternal", 1),
          ("importNoExternal", 2),
          ("importNssa", 3))
    )


_HwOspfv3AreaImportAsExtern_Type.__name__ = "Integer32"
_HwOspfv3AreaImportAsExtern_Object = MibTableColumn
hwOspfv3AreaImportAsExtern = _HwOspfv3AreaImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 2),
    _HwOspfv3AreaImportAsExtern_Type()
)
hwOspfv3AreaImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3AreaImportAsExtern.setStatus("current")
_HwOspfv3AreaSpfRuns_Type = Counter32
_HwOspfv3AreaSpfRuns_Object = MibTableColumn
hwOspfv3AreaSpfRuns = _HwOspfv3AreaSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 3),
    _HwOspfv3AreaSpfRuns_Type()
)
hwOspfv3AreaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaSpfRuns.setStatus("current")


class _HwOspfv3AreaBdrRtrCount_Type(Gauge32):
    """Custom type hwOspfv3AreaBdrRtrCount based on Gauge32"""
    defaultValue = 0


_HwOspfv3AreaBdrRtrCount_Object = MibTableColumn
hwOspfv3AreaBdrRtrCount = _HwOspfv3AreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 4),
    _HwOspfv3AreaBdrRtrCount_Type()
)
hwOspfv3AreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaBdrRtrCount.setStatus("current")


class _HwOspfv3AreaAsBdrRtrCount_Type(Gauge32):
    """Custom type hwOspfv3AreaAsBdrRtrCount based on Gauge32"""
    defaultValue = 0


_HwOspfv3AreaAsBdrRtrCount_Object = MibTableColumn
hwOspfv3AreaAsBdrRtrCount = _HwOspfv3AreaAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 5),
    _HwOspfv3AreaAsBdrRtrCount_Type()
)
hwOspfv3AreaAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaAsBdrRtrCount.setStatus("current")


class _HwOspfv3AreaScopeLsaCount_Type(Gauge32):
    """Custom type hwOspfv3AreaScopeLsaCount based on Gauge32"""
    defaultValue = 0


_HwOspfv3AreaScopeLsaCount_Object = MibTableColumn
hwOspfv3AreaScopeLsaCount = _HwOspfv3AreaScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 6),
    _HwOspfv3AreaScopeLsaCount_Type()
)
hwOspfv3AreaScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaScopeLsaCount.setStatus("current")
_HwOspfv3AreaScopeLsaCksumSum_Type = Unsigned32
_HwOspfv3AreaScopeLsaCksumSum_Object = MibTableColumn
hwOspfv3AreaScopeLsaCksumSum = _HwOspfv3AreaScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 7),
    _HwOspfv3AreaScopeLsaCksumSum_Type()
)
hwOspfv3AreaScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaScopeLsaCksumSum.setStatus("current")


class _HwOspfv3AreaSummary_Type(Integer32):
    """Custom type hwOspfv3AreaSummary based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_HwOspfv3AreaSummary_Type.__name__ = "Integer32"
_HwOspfv3AreaSummary_Object = MibTableColumn
hwOspfv3AreaSummary = _HwOspfv3AreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 8),
    _HwOspfv3AreaSummary_Type()
)
hwOspfv3AreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3AreaSummary.setStatus("current")
_HwOspfv3AreaRowStatus_Type = RowStatus
_HwOspfv3AreaRowStatus_Object = MibTableColumn
hwOspfv3AreaRowStatus = _HwOspfv3AreaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 9),
    _HwOspfv3AreaRowStatus_Type()
)
hwOspfv3AreaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3AreaRowStatus.setStatus("current")
_HwOspfv3AreaStubMetric_Type = BigMetric
_HwOspfv3AreaStubMetric_Object = MibTableColumn
hwOspfv3AreaStubMetric = _HwOspfv3AreaStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 10),
    _HwOspfv3AreaStubMetric_Type()
)
hwOspfv3AreaStubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3AreaStubMetric.setStatus("current")


class _HwOspfv3AreaNssaTranslatorRole_Type(Integer32):
    """Custom type hwOspfv3AreaNssaTranslatorRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("candidate", 2))
    )


_HwOspfv3AreaNssaTranslatorRole_Type.__name__ = "Integer32"
_HwOspfv3AreaNssaTranslatorRole_Object = MibTableColumn
hwOspfv3AreaNssaTranslatorRole = _HwOspfv3AreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 11),
    _HwOspfv3AreaNssaTranslatorRole_Type()
)
hwOspfv3AreaNssaTranslatorRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3AreaNssaTranslatorRole.setStatus("current")


class _HwOspfv3AreaNssaTranslatorState_Type(Integer32):
    """Custom type hwOspfv3AreaNssaTranslatorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("elected", 2),
          ("enabled", 1))
    )


_HwOspfv3AreaNssaTranslatorState_Type.__name__ = "Integer32"
_HwOspfv3AreaNssaTranslatorState_Object = MibTableColumn
hwOspfv3AreaNssaTranslatorState = _HwOspfv3AreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 12),
    _HwOspfv3AreaNssaTranslatorState_Type()
)
hwOspfv3AreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaNssaTranslatorState.setStatus("current")


class _HwOspfv3AreaNssaTranslatorStabInterval_Type(Unsigned32):
    """Custom type hwOspfv3AreaNssaTranslatorStabInterval based on Unsigned32"""
    defaultValue = 40


_HwOspfv3AreaNssaTranslatorStabInterval_Object = MibTableColumn
hwOspfv3AreaNssaTranslatorStabInterval = _HwOspfv3AreaNssaTranslatorStabInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 13),
    _HwOspfv3AreaNssaTranslatorStabInterval_Type()
)
hwOspfv3AreaNssaTranslatorStabInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3AreaNssaTranslatorStabInterval.setStatus("current")
_HwOspfv3AreaNssaTranslatorEvents_Type = Counter32
_HwOspfv3AreaNssaTranslatorEvents_Object = MibTableColumn
hwOspfv3AreaNssaTranslatorEvents = _HwOspfv3AreaNssaTranslatorEvents_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 2, 1, 14),
    _HwOspfv3AreaNssaTranslatorEvents_Type()
)
hwOspfv3AreaNssaTranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaNssaTranslatorEvents.setStatus("current")
_HwOspfv3AsLsdbTable_Object = MibTable
hwOspfv3AsLsdbTable = _HwOspfv3AsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 3)
)
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbTable.setStatus("current")
_HwOspfv3AsLsdbEntry_Object = MibTableRow
hwOspfv3AsLsdbEntry = _HwOspfv3AsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 3, 1)
)
hwOspfv3AsLsdbEntry.setIndexNames(
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AsLsdbType"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AsLsdbRouterId"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AsLsdbLsId"),
)
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbEntry.setStatus("current")


class _HwOspfv3AsLsdbType_Type(Unsigned32):
    """Custom type hwOspfv3AsLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwOspfv3AsLsdbType_Type.__name__ = "Unsigned32"
_HwOspfv3AsLsdbType_Object = MibTableColumn
hwOspfv3AsLsdbType = _HwOspfv3AsLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 3, 1, 1),
    _HwOspfv3AsLsdbType_Type()
)
hwOspfv3AsLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbType.setStatus("current")
_HwOspfv3AsLsdbRouterId_Type = HWOspfv3RouterIdTc
_HwOspfv3AsLsdbRouterId_Object = MibTableColumn
hwOspfv3AsLsdbRouterId = _HwOspfv3AsLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 3, 1, 2),
    _HwOspfv3AsLsdbRouterId_Type()
)
hwOspfv3AsLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbRouterId.setStatus("current")
_HwOspfv3AsLsdbLsId_Type = Unsigned32
_HwOspfv3AsLsdbLsId_Object = MibTableColumn
hwOspfv3AsLsdbLsId = _HwOspfv3AsLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 3, 1, 3),
    _HwOspfv3AsLsdbLsId_Type()
)
hwOspfv3AsLsdbLsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbLsId.setStatus("current")
_HwOspfv3AsLsdbSequence_Type = HWOspfv3LsaSequenceTC
_HwOspfv3AsLsdbSequence_Object = MibTableColumn
hwOspfv3AsLsdbSequence = _HwOspfv3AsLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 3, 1, 4),
    _HwOspfv3AsLsdbSequence_Type()
)
hwOspfv3AsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbSequence.setStatus("current")
_HwOspfv3AsLsdbAge_Type = HWOspfv3LsaAgeTC
_HwOspfv3AsLsdbAge_Object = MibTableColumn
hwOspfv3AsLsdbAge = _HwOspfv3AsLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 3, 1, 5),
    _HwOspfv3AsLsdbAge_Type()
)
hwOspfv3AsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbAge.setUnits("seconds")
_HwOspfv3AsLsdbChecksum_Type = Integer32
_HwOspfv3AsLsdbChecksum_Object = MibTableColumn
hwOspfv3AsLsdbChecksum = _HwOspfv3AsLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 3, 1, 6),
    _HwOspfv3AsLsdbChecksum_Type()
)
hwOspfv3AsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbChecksum.setStatus("current")


class _HwOspfv3AsLsdbAdvertisement_Type(OctetString):
    """Custom type hwOspfv3AsLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HwOspfv3AsLsdbAdvertisement_Type.__name__ = "OctetString"
_HwOspfv3AsLsdbAdvertisement_Object = MibTableColumn
hwOspfv3AsLsdbAdvertisement = _HwOspfv3AsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 3, 1, 7),
    _HwOspfv3AsLsdbAdvertisement_Type()
)
hwOspfv3AsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbAdvertisement.setStatus("current")
_HwOspfv3AsLsdbTypeKnown_Type = TruthValue
_HwOspfv3AsLsdbTypeKnown_Object = MibTableColumn
hwOspfv3AsLsdbTypeKnown = _HwOspfv3AsLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 3, 1, 8),
    _HwOspfv3AsLsdbTypeKnown_Type()
)
hwOspfv3AsLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbTypeKnown.setStatus("current")
_HwOspfv3AreaLsdbTable_Object = MibTable
hwOspfv3AreaLsdbTable = _HwOspfv3AreaLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 4)
)
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbTable.setStatus("current")
_HwOspfv3AreaLsdbEntry_Object = MibTableRow
hwOspfv3AreaLsdbEntry = _HwOspfv3AreaLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 4, 1)
)
hwOspfv3AreaLsdbEntry.setIndexNames(
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AreaLsdbAreaId"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AreaLsdbType"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AreaLsdbRouterId"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AreaLsdbLsId"),
)
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbEntry.setStatus("current")
_HwOspfv3AreaLsdbAreaId_Type = HWOspfv3AreaIdTc
_HwOspfv3AreaLsdbAreaId_Object = MibTableColumn
hwOspfv3AreaLsdbAreaId = _HwOspfv3AreaLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 4, 1, 1),
    _HwOspfv3AreaLsdbAreaId_Type()
)
hwOspfv3AreaLsdbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbAreaId.setStatus("current")


class _HwOspfv3AreaLsdbType_Type(Unsigned32):
    """Custom type hwOspfv3AreaLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwOspfv3AreaLsdbType_Type.__name__ = "Unsigned32"
_HwOspfv3AreaLsdbType_Object = MibTableColumn
hwOspfv3AreaLsdbType = _HwOspfv3AreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 4, 1, 2),
    _HwOspfv3AreaLsdbType_Type()
)
hwOspfv3AreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbType.setStatus("current")
_HwOspfv3AreaLsdbRouterId_Type = HWOspfv3RouterIdTc
_HwOspfv3AreaLsdbRouterId_Object = MibTableColumn
hwOspfv3AreaLsdbRouterId = _HwOspfv3AreaLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 4, 1, 3),
    _HwOspfv3AreaLsdbRouterId_Type()
)
hwOspfv3AreaLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbRouterId.setStatus("current")
_HwOspfv3AreaLsdbLsId_Type = Unsigned32
_HwOspfv3AreaLsdbLsId_Object = MibTableColumn
hwOspfv3AreaLsdbLsId = _HwOspfv3AreaLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 4, 1, 4),
    _HwOspfv3AreaLsdbLsId_Type()
)
hwOspfv3AreaLsdbLsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbLsId.setStatus("current")
_HwOspfv3AreaLsdbSequence_Type = HWOspfv3LsaSequenceTC
_HwOspfv3AreaLsdbSequence_Object = MibTableColumn
hwOspfv3AreaLsdbSequence = _HwOspfv3AreaLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 4, 1, 5),
    _HwOspfv3AreaLsdbSequence_Type()
)
hwOspfv3AreaLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbSequence.setStatus("current")
_HwOspfv3AreaLsdbAge_Type = HWOspfv3LsaAgeTC
_HwOspfv3AreaLsdbAge_Object = MibTableColumn
hwOspfv3AreaLsdbAge = _HwOspfv3AreaLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 4, 1, 6),
    _HwOspfv3AreaLsdbAge_Type()
)
hwOspfv3AreaLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbAge.setUnits("seconds")
_HwOspfv3AreaLsdbChecksum_Type = Integer32
_HwOspfv3AreaLsdbChecksum_Object = MibTableColumn
hwOspfv3AreaLsdbChecksum = _HwOspfv3AreaLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 4, 1, 7),
    _HwOspfv3AreaLsdbChecksum_Type()
)
hwOspfv3AreaLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbChecksum.setStatus("current")


class _HwOspfv3AreaLsdbAdvertisement_Type(OctetString):
    """Custom type hwOspfv3AreaLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HwOspfv3AreaLsdbAdvertisement_Type.__name__ = "OctetString"
_HwOspfv3AreaLsdbAdvertisement_Object = MibTableColumn
hwOspfv3AreaLsdbAdvertisement = _HwOspfv3AreaLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 4, 1, 8),
    _HwOspfv3AreaLsdbAdvertisement_Type()
)
hwOspfv3AreaLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbAdvertisement.setStatus("current")
_HwOspfv3AreaLsdbTypeKnown_Type = TruthValue
_HwOspfv3AreaLsdbTypeKnown_Object = MibTableColumn
hwOspfv3AreaLsdbTypeKnown = _HwOspfv3AreaLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 4, 1, 9),
    _HwOspfv3AreaLsdbTypeKnown_Type()
)
hwOspfv3AreaLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbTypeKnown.setStatus("current")
_HwOspfv3LinkLsdbTable_Object = MibTable
hwOspfv3LinkLsdbTable = _HwOspfv3LinkLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5)
)
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbTable.setStatus("current")
_HwOspfv3LinkLsdbEntry_Object = MibTableRow
hwOspfv3LinkLsdbEntry = _HwOspfv3LinkLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5, 1)
)
hwOspfv3LinkLsdbEntry.setIndexNames(
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3LinkLsdbIfIndex"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3LinkLsdbIfInstId"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3LinkLsdbType"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3LinkLsdbRouterId"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3LinkLsdbLsId"),
)
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbEntry.setStatus("current")
_HwOspfv3LinkLsdbIfIndex_Type = InterfaceIndex
_HwOspfv3LinkLsdbIfIndex_Object = MibTableColumn
hwOspfv3LinkLsdbIfIndex = _HwOspfv3LinkLsdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5, 1, 1),
    _HwOspfv3LinkLsdbIfIndex_Type()
)
hwOspfv3LinkLsdbIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbIfIndex.setStatus("current")
_HwOspfv3LinkLsdbIfInstId_Type = HWOspfv3IfInstIdTc
_HwOspfv3LinkLsdbIfInstId_Object = MibTableColumn
hwOspfv3LinkLsdbIfInstId = _HwOspfv3LinkLsdbIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5, 1, 2),
    _HwOspfv3LinkLsdbIfInstId_Type()
)
hwOspfv3LinkLsdbIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbIfInstId.setStatus("current")


class _HwOspfv3LinkLsdbType_Type(Unsigned32):
    """Custom type hwOspfv3LinkLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwOspfv3LinkLsdbType_Type.__name__ = "Unsigned32"
_HwOspfv3LinkLsdbType_Object = MibTableColumn
hwOspfv3LinkLsdbType = _HwOspfv3LinkLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5, 1, 3),
    _HwOspfv3LinkLsdbType_Type()
)
hwOspfv3LinkLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbType.setStatus("current")
_HwOspfv3LinkLsdbRouterId_Type = HWOspfv3RouterIdTc
_HwOspfv3LinkLsdbRouterId_Object = MibTableColumn
hwOspfv3LinkLsdbRouterId = _HwOspfv3LinkLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5, 1, 4),
    _HwOspfv3LinkLsdbRouterId_Type()
)
hwOspfv3LinkLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbRouterId.setStatus("current")
_HwOspfv3LinkLsdbLsId_Type = HWOspfv3LsIdTC
_HwOspfv3LinkLsdbLsId_Object = MibTableColumn
hwOspfv3LinkLsdbLsId = _HwOspfv3LinkLsdbLsId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5, 1, 5),
    _HwOspfv3LinkLsdbLsId_Type()
)
hwOspfv3LinkLsdbLsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbLsId.setStatus("current")
_HwOspfv3LinkLsdbSequence_Type = HWOspfv3LsaSequenceTC
_HwOspfv3LinkLsdbSequence_Object = MibTableColumn
hwOspfv3LinkLsdbSequence = _HwOspfv3LinkLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5, 1, 6),
    _HwOspfv3LinkLsdbSequence_Type()
)
hwOspfv3LinkLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbSequence.setStatus("current")
_HwOspfv3LinkLsdbAge_Type = HWOspfv3LsaAgeTC
_HwOspfv3LinkLsdbAge_Object = MibTableColumn
hwOspfv3LinkLsdbAge = _HwOspfv3LinkLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5, 1, 7),
    _HwOspfv3LinkLsdbAge_Type()
)
hwOspfv3LinkLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbAge.setUnits("seconds")
_HwOspfv3LinkLsdbChecksum_Type = Integer32
_HwOspfv3LinkLsdbChecksum_Object = MibTableColumn
hwOspfv3LinkLsdbChecksum = _HwOspfv3LinkLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5, 1, 8),
    _HwOspfv3LinkLsdbChecksum_Type()
)
hwOspfv3LinkLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbChecksum.setStatus("current")


class _HwOspfv3LinkLsdbAdvertisement_Type(OctetString):
    """Custom type hwOspfv3LinkLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HwOspfv3LinkLsdbAdvertisement_Type.__name__ = "OctetString"
_HwOspfv3LinkLsdbAdvertisement_Object = MibTableColumn
hwOspfv3LinkLsdbAdvertisement = _HwOspfv3LinkLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5, 1, 9),
    _HwOspfv3LinkLsdbAdvertisement_Type()
)
hwOspfv3LinkLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbAdvertisement.setStatus("current")
_HwOspfv3LinkLsdbTypeKnown_Type = TruthValue
_HwOspfv3LinkLsdbTypeKnown_Object = MibTableColumn
hwOspfv3LinkLsdbTypeKnown = _HwOspfv3LinkLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 5, 1, 10),
    _HwOspfv3LinkLsdbTypeKnown_Type()
)
hwOspfv3LinkLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbTypeKnown.setStatus("current")
_HwOspfv3IfTable_Object = MibTable
hwOspfv3IfTable = _HwOspfv3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6)
)
if mibBuilder.loadTexts:
    hwOspfv3IfTable.setStatus("current")
_HwOspfv3IfEntry_Object = MibTableRow
hwOspfv3IfEntry = _HwOspfv3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1)
)
hwOspfv3IfEntry.setIndexNames(
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3IfIndex"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3IfInstId"),
)
if mibBuilder.loadTexts:
    hwOspfv3IfEntry.setStatus("current")
_HwOspfv3IfIndex_Type = InterfaceIndex
_HwOspfv3IfIndex_Object = MibTableColumn
hwOspfv3IfIndex = _HwOspfv3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 1),
    _HwOspfv3IfIndex_Type()
)
hwOspfv3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3IfIndex.setStatus("current")
_HwOspfv3IfInstId_Type = HWOspfv3IfInstIdTc
_HwOspfv3IfInstId_Object = MibTableColumn
hwOspfv3IfInstId = _HwOspfv3IfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 2),
    _HwOspfv3IfInstId_Type()
)
hwOspfv3IfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3IfInstId.setStatus("current")


class _HwOspfv3IfAreaId_Type(HWOspfv3AreaIdTc):
    """Custom type hwOspfv3IfAreaId based on HWOspfv3AreaIdTc"""
    defaultValue = 0


_HwOspfv3IfAreaId_Object = MibTableColumn
hwOspfv3IfAreaId = _HwOspfv3IfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 3),
    _HwOspfv3IfAreaId_Type()
)
hwOspfv3IfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfAreaId.setStatus("current")


class _HwOspfv3IfType_Type(Integer32):
    """Custom type hwOspfv3IfType based on Integer32"""
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
        *(("broadcast", 1),
          ("loopback", 4),
          ("nbma", 2),
          ("p2mpNonbroadcast", 6),
          ("pointToMultipoint", 5),
          ("pointToPoint", 3))
    )


_HwOspfv3IfType_Type.__name__ = "Integer32"
_HwOspfv3IfType_Object = MibTableColumn
hwOspfv3IfType = _HwOspfv3IfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 4),
    _HwOspfv3IfType_Type()
)
hwOspfv3IfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfType.setStatus("current")


class _HwOspfv3IfAdminStatus_Type(Status):
    """Custom type hwOspfv3IfAdminStatus based on Status"""


_HwOspfv3IfAdminStatus_Object = MibTableColumn
hwOspfv3IfAdminStatus = _HwOspfv3IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 5),
    _HwOspfv3IfAdminStatus_Type()
)
hwOspfv3IfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfAdminStatus.setStatus("current")


class _HwOspfv3IfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type hwOspfv3IfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_HwOspfv3IfRtrPriority_Object = MibTableColumn
hwOspfv3IfRtrPriority = _HwOspfv3IfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 6),
    _HwOspfv3IfRtrPriority_Type()
)
hwOspfv3IfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfRtrPriority.setStatus("current")


class _HwOspfv3IfTransitDelay_Type(HWOspfv3UpToRefreshIntervalTc):
    """Custom type hwOspfv3IfTransitDelay based on HWOspfv3UpToRefreshIntervalTc"""
    defaultValue = 1


_HwOspfv3IfTransitDelay_Object = MibTableColumn
hwOspfv3IfTransitDelay = _HwOspfv3IfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 7),
    _HwOspfv3IfTransitDelay_Type()
)
hwOspfv3IfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3IfTransitDelay.setUnits("seconds")


class _HwOspfv3IfRetransInterval_Type(HWOspfv3UpToRefreshIntervalTc):
    """Custom type hwOspfv3IfRetransInterval based on HWOspfv3UpToRefreshIntervalTc"""
    defaultValue = 5


_HwOspfv3IfRetransInterval_Object = MibTableColumn
hwOspfv3IfRetransInterval = _HwOspfv3IfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 8),
    _HwOspfv3IfRetransInterval_Type()
)
hwOspfv3IfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3IfRetransInterval.setUnits("seconds")


class _HwOspfv3IfHelloInterval_Type(HWHelloRange):
    """Custom type hwOspfv3IfHelloInterval based on HWHelloRange"""
    defaultValue = 10


_HwOspfv3IfHelloInterval_Object = MibTableColumn
hwOspfv3IfHelloInterval = _HwOspfv3IfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 9),
    _HwOspfv3IfHelloInterval_Type()
)
hwOspfv3IfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3IfHelloInterval.setUnits("seconds")


class _HwOspfv3IfRtrDeadInterval_Type(HWOspfv3DeadIntRangeTc):
    """Custom type hwOspfv3IfRtrDeadInterval based on HWOspfv3DeadIntRangeTc"""
    defaultValue = 40


_HwOspfv3IfRtrDeadInterval_Object = MibTableColumn
hwOspfv3IfRtrDeadInterval = _HwOspfv3IfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 10),
    _HwOspfv3IfRtrDeadInterval_Type()
)
hwOspfv3IfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3IfRtrDeadInterval.setUnits("seconds")


class _HwOspfv3IfState_Type(Integer32):
    """Custom type hwOspfv3IfState based on Integer32"""
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


_HwOspfv3IfState_Type.__name__ = "Integer32"
_HwOspfv3IfState_Object = MibTableColumn
hwOspfv3IfState = _HwOspfv3IfState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 11),
    _HwOspfv3IfState_Type()
)
hwOspfv3IfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3IfState.setStatus("current")
_HwOspfv3IfDesignatedRouter_Type = HWOspfv3RouterIdTc
_HwOspfv3IfDesignatedRouter_Object = MibTableColumn
hwOspfv3IfDesignatedRouter = _HwOspfv3IfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 12),
    _HwOspfv3IfDesignatedRouter_Type()
)
hwOspfv3IfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3IfDesignatedRouter.setStatus("current")
_HwOspfv3IfBackupDesignatedRouter_Type = HWOspfv3RouterIdTc
_HwOspfv3IfBackupDesignatedRouter_Object = MibTableColumn
hwOspfv3IfBackupDesignatedRouter = _HwOspfv3IfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 13),
    _HwOspfv3IfBackupDesignatedRouter_Type()
)
hwOspfv3IfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3IfBackupDesignatedRouter.setStatus("current")
_HwOspfv3IfEvents_Type = Counter32
_HwOspfv3IfEvents_Object = MibTableColumn
hwOspfv3IfEvents = _HwOspfv3IfEvents_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 14),
    _HwOspfv3IfEvents_Type()
)
hwOspfv3IfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3IfEvents.setStatus("current")
_HwOspfv3IfRowStatus_Type = RowStatus
_HwOspfv3IfRowStatus_Object = MibTableColumn
hwOspfv3IfRowStatus = _HwOspfv3IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 15),
    _HwOspfv3IfRowStatus_Type()
)
hwOspfv3IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfRowStatus.setStatus("current")
_HwOspfv3IfMetricValue_Type = Metric
_HwOspfv3IfMetricValue_Object = MibTableColumn
hwOspfv3IfMetricValue = _HwOspfv3IfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 16),
    _HwOspfv3IfMetricValue_Type()
)
hwOspfv3IfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfMetricValue.setStatus("current")
_HwOspfv3IfLinkScopeLsaCount_Type = Gauge32
_HwOspfv3IfLinkScopeLsaCount_Object = MibTableColumn
hwOspfv3IfLinkScopeLsaCount = _HwOspfv3IfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 17),
    _HwOspfv3IfLinkScopeLsaCount_Type()
)
hwOspfv3IfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3IfLinkScopeLsaCount.setStatus("current")
_HwOspfv3IfLinkLsaCksumSum_Type = Unsigned32
_HwOspfv3IfLinkLsaCksumSum_Object = MibTableColumn
hwOspfv3IfLinkLsaCksumSum = _HwOspfv3IfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 18),
    _HwOspfv3IfLinkLsaCksumSum_Type()
)
hwOspfv3IfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3IfLinkLsaCksumSum.setStatus("current")


class _HwOspfv3IfPollInterval_Type(Unsigned32):
    """Custom type hwOspfv3IfPollInterval based on Unsigned32"""
    defaultValue = 120


_HwOspfv3IfPollInterval_Object = MibTableColumn
hwOspfv3IfPollInterval = _HwOspfv3IfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 19),
    _HwOspfv3IfPollInterval_Type()
)
hwOspfv3IfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3IfPollInterval.setUnits("seconds")


class _HwOspfv3IfMulticastForwarding_Type(Integer32):
    """Custom type hwOspfv3IfMulticastForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_HwOspfv3IfMulticastForwarding_Type.__name__ = "Integer32"
_HwOspfv3IfMulticastForwarding_Object = MibTableColumn
hwOspfv3IfMulticastForwarding = _HwOspfv3IfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 6, 1, 20),
    _HwOspfv3IfMulticastForwarding_Type()
)
hwOspfv3IfMulticastForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3IfMulticastForwarding.setStatus("current")
_HwOspfv3VirtIfTable_Object = MibTable
hwOspfv3VirtIfTable = _HwOspfv3VirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7)
)
if mibBuilder.loadTexts:
    hwOspfv3VirtIfTable.setStatus("current")
_HwOspfv3VirtIfEntry_Object = MibTableRow
hwOspfv3VirtIfEntry = _HwOspfv3VirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1)
)
hwOspfv3VirtIfEntry.setIndexNames(
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfAreaId"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    hwOspfv3VirtIfEntry.setStatus("current")
_HwOspfv3VirtIfAreaId_Type = HWOspfv3AreaIdTc
_HwOspfv3VirtIfAreaId_Object = MibTableColumn
hwOspfv3VirtIfAreaId = _HwOspfv3VirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 1),
    _HwOspfv3VirtIfAreaId_Type()
)
hwOspfv3VirtIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfAreaId.setStatus("current")
_HwOspfv3VirtIfNeighbor_Type = HWOspfv3RouterIdTc
_HwOspfv3VirtIfNeighbor_Object = MibTableColumn
hwOspfv3VirtIfNeighbor = _HwOspfv3VirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 2),
    _HwOspfv3VirtIfNeighbor_Type()
)
hwOspfv3VirtIfNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfNeighbor.setStatus("current")
_HwOspfv3VirtIfIndex_Type = InterfaceIndex
_HwOspfv3VirtIfIndex_Object = MibTableColumn
hwOspfv3VirtIfIndex = _HwOspfv3VirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 3),
    _HwOspfv3VirtIfIndex_Type()
)
hwOspfv3VirtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfIndex.setStatus("current")
_HwOspfv3VirtIfInstId_Type = HWOspfv3IfInstIdTc
_HwOspfv3VirtIfInstId_Object = MibTableColumn
hwOspfv3VirtIfInstId = _HwOspfv3VirtIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 4),
    _HwOspfv3VirtIfInstId_Type()
)
hwOspfv3VirtIfInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfInstId.setStatus("current")


class _HwOspfv3VirtIfTransitDelay_Type(HWOspfv3UpToRefreshIntervalTc):
    """Custom type hwOspfv3VirtIfTransitDelay based on HWOspfv3UpToRefreshIntervalTc"""
    defaultValue = 1


_HwOspfv3VirtIfTransitDelay_Object = MibTableColumn
hwOspfv3VirtIfTransitDelay = _HwOspfv3VirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 5),
    _HwOspfv3VirtIfTransitDelay_Type()
)
hwOspfv3VirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfTransitDelay.setUnits("seconds")


class _HwOspfv3VirtIfRetransInterval_Type(HWOspfv3UpToRefreshIntervalTc):
    """Custom type hwOspfv3VirtIfRetransInterval based on HWOspfv3UpToRefreshIntervalTc"""
    defaultValue = 5


_HwOspfv3VirtIfRetransInterval_Object = MibTableColumn
hwOspfv3VirtIfRetransInterval = _HwOspfv3VirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 6),
    _HwOspfv3VirtIfRetransInterval_Type()
)
hwOspfv3VirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfRetransInterval.setUnits("seconds")


class _HwOspfv3VirtIfHelloInterval_Type(HelloRange):
    """Custom type hwOspfv3VirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_HwOspfv3VirtIfHelloInterval_Object = MibTableColumn
hwOspfv3VirtIfHelloInterval = _HwOspfv3VirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 7),
    _HwOspfv3VirtIfHelloInterval_Type()
)
hwOspfv3VirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfHelloInterval.setUnits("seconds")


class _HwOspfv3VirtIfRtrDeadInterval_Type(HWOspfv3DeadIntRangeTc):
    """Custom type hwOspfv3VirtIfRtrDeadInterval based on HWOspfv3DeadIntRangeTc"""
    defaultValue = 40


_HwOspfv3VirtIfRtrDeadInterval_Object = MibTableColumn
hwOspfv3VirtIfRtrDeadInterval = _HwOspfv3VirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 8),
    _HwOspfv3VirtIfRtrDeadInterval_Type()
)
hwOspfv3VirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfRtrDeadInterval.setUnits("seconds")


class _HwOspfv3VirtIfState_Type(Integer32):
    """Custom type hwOspfv3VirtIfState based on Integer32"""
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


_HwOspfv3VirtIfState_Type.__name__ = "Integer32"
_HwOspfv3VirtIfState_Object = MibTableColumn
hwOspfv3VirtIfState = _HwOspfv3VirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 9),
    _HwOspfv3VirtIfState_Type()
)
hwOspfv3VirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfState.setStatus("current")
_HwOspfv3VirtIfEvents_Type = Counter32
_HwOspfv3VirtIfEvents_Object = MibTableColumn
hwOspfv3VirtIfEvents = _HwOspfv3VirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 10),
    _HwOspfv3VirtIfEvents_Type()
)
hwOspfv3VirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfEvents.setStatus("current")
_HwOspfv3VirtIfRowStatus_Type = RowStatus
_HwOspfv3VirtIfRowStatus_Object = MibTableColumn
hwOspfv3VirtIfRowStatus = _HwOspfv3VirtIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 11),
    _HwOspfv3VirtIfRowStatus_Type()
)
hwOspfv3VirtIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfRowStatus.setStatus("current")
_HwOspfv3VirtIfLinkScopeLsaCount_Type = Gauge32
_HwOspfv3VirtIfLinkScopeLsaCount_Object = MibTableColumn
hwOspfv3VirtIfLinkScopeLsaCount = _HwOspfv3VirtIfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 12),
    _HwOspfv3VirtIfLinkScopeLsaCount_Type()
)
hwOspfv3VirtIfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfLinkScopeLsaCount.setStatus("current")
_HwOspfv3VirtIfLinkLsaCksumSum_Type = Unsigned32
_HwOspfv3VirtIfLinkLsaCksumSum_Object = MibTableColumn
hwOspfv3VirtIfLinkLsaCksumSum = _HwOspfv3VirtIfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 7, 1, 13),
    _HwOspfv3VirtIfLinkLsaCksumSum_Type()
)
hwOspfv3VirtIfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtIfLinkLsaCksumSum.setStatus("current")
_HwOspfv3NbrTable_Object = MibTable
hwOspfv3NbrTable = _HwOspfv3NbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8)
)
if mibBuilder.loadTexts:
    hwOspfv3NbrTable.setStatus("current")
_HwOspfv3NbrEntry_Object = MibTableRow
hwOspfv3NbrEntry = _HwOspfv3NbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1)
)
hwOspfv3NbrEntry.setIndexNames(
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3NbrIfIndex"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3NbrIfInstId"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3NbrRtrId"),
)
if mibBuilder.loadTexts:
    hwOspfv3NbrEntry.setStatus("current")
_HwOspfv3NbrIfIndex_Type = InterfaceIndex
_HwOspfv3NbrIfIndex_Object = MibTableColumn
hwOspfv3NbrIfIndex = _HwOspfv3NbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 1),
    _HwOspfv3NbrIfIndex_Type()
)
hwOspfv3NbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3NbrIfIndex.setStatus("current")
_HwOspfv3NbrIfInstId_Type = HWOspfv3IfInstIdTc
_HwOspfv3NbrIfInstId_Object = MibTableColumn
hwOspfv3NbrIfInstId = _HwOspfv3NbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 2),
    _HwOspfv3NbrIfInstId_Type()
)
hwOspfv3NbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3NbrIfInstId.setStatus("current")
_HwOspfv3NbrRtrId_Type = HWOspfv3RouterIdTc
_HwOspfv3NbrRtrId_Object = MibTableColumn
hwOspfv3NbrRtrId = _HwOspfv3NbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 3),
    _HwOspfv3NbrRtrId_Type()
)
hwOspfv3NbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3NbrRtrId.setStatus("current")
_HwOspfv3NbrAddressType_Type = InetAddressType
_HwOspfv3NbrAddressType_Object = MibTableColumn
hwOspfv3NbrAddressType = _HwOspfv3NbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 4),
    _HwOspfv3NbrAddressType_Type()
)
hwOspfv3NbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrAddressType.setStatus("current")
_HwOspfv3NbrAddress_Type = InetAddress
_HwOspfv3NbrAddress_Object = MibTableColumn
hwOspfv3NbrAddress = _HwOspfv3NbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 5),
    _HwOspfv3NbrAddress_Type()
)
hwOspfv3NbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrAddress.setStatus("current")
_HwOspfv3NbrOptions_Type = Integer32
_HwOspfv3NbrOptions_Object = MibTableColumn
hwOspfv3NbrOptions = _HwOspfv3NbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 6),
    _HwOspfv3NbrOptions_Type()
)
hwOspfv3NbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrOptions.setStatus("current")
_HwOspfv3NbrPriority_Type = DesignatedRouterPriority
_HwOspfv3NbrPriority_Object = MibTableColumn
hwOspfv3NbrPriority = _HwOspfv3NbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 7),
    _HwOspfv3NbrPriority_Type()
)
hwOspfv3NbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrPriority.setStatus("current")


class _HwOspfv3NbrState_Type(Integer32):
    """Custom type hwOspfv3NbrState based on Integer32"""
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


_HwOspfv3NbrState_Type.__name__ = "Integer32"
_HwOspfv3NbrState_Object = MibTableColumn
hwOspfv3NbrState = _HwOspfv3NbrState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 8),
    _HwOspfv3NbrState_Type()
)
hwOspfv3NbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrState.setStatus("current")
_HwOspfv3NbrEvents_Type = Counter32
_HwOspfv3NbrEvents_Object = MibTableColumn
hwOspfv3NbrEvents = _HwOspfv3NbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 9),
    _HwOspfv3NbrEvents_Type()
)
hwOspfv3NbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrEvents.setStatus("current")
_HwOspfv3NbrLsRetransQLen_Type = Gauge32
_HwOspfv3NbrLsRetransQLen_Object = MibTableColumn
hwOspfv3NbrLsRetransQLen = _HwOspfv3NbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 10),
    _HwOspfv3NbrLsRetransQLen_Type()
)
hwOspfv3NbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrLsRetransQLen.setStatus("current")
_HwOspfv3NbrHelloSuppressed_Type = TruthValue
_HwOspfv3NbrHelloSuppressed_Object = MibTableColumn
hwOspfv3NbrHelloSuppressed = _HwOspfv3NbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 11),
    _HwOspfv3NbrHelloSuppressed_Type()
)
hwOspfv3NbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrHelloSuppressed.setStatus("current")
_HwOspfv3NbrIfId_Type = InterfaceIndex
_HwOspfv3NbrIfId_Object = MibTableColumn
hwOspfv3NbrIfId = _HwOspfv3NbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 12),
    _HwOspfv3NbrIfId_Type()
)
hwOspfv3NbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrIfId.setStatus("current")


class _HwOspfv3NbrRestartHelperStatus_Type(Integer32):
    """Custom type hwOspfv3NbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("helping", 2),
          ("notHelping", 1))
    )


_HwOspfv3NbrRestartHelperStatus_Type.__name__ = "Integer32"
_HwOspfv3NbrRestartHelperStatus_Object = MibTableColumn
hwOspfv3NbrRestartHelperStatus = _HwOspfv3NbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 13),
    _HwOspfv3NbrRestartHelperStatus_Type()
)
hwOspfv3NbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrRestartHelperStatus.setStatus("current")
_HwOspfv3NbrRestartHelperAge_Type = HWOspfv3UpToRefreshIntervalTc
_HwOspfv3NbrRestartHelperAge_Object = MibTableColumn
hwOspfv3NbrRestartHelperAge = _HwOspfv3NbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 14),
    _HwOspfv3NbrRestartHelperAge_Type()
)
hwOspfv3NbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3NbrRestartHelperAge.setUnits("seconds")


class _HwOspfv3NbrRestartHelperExitRc_Type(Integer32):
    """Custom type hwOspfv3NbrRestartHelperExitRc based on Integer32"""
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
        *(("completed", 3),
          ("inProgress", 2),
          ("none", 1),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_HwOspfv3NbrRestartHelperExitRc_Type.__name__ = "Integer32"
_HwOspfv3NbrRestartHelperExitRc_Object = MibTableColumn
hwOspfv3NbrRestartHelperExitRc = _HwOspfv3NbrRestartHelperExitRc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 8, 1, 15),
    _HwOspfv3NbrRestartHelperExitRc_Type()
)
hwOspfv3NbrRestartHelperExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NbrRestartHelperExitRc.setStatus("current")
_HwOspfv3CfgNbrTable_Object = MibTable
hwOspfv3CfgNbrTable = _HwOspfv3CfgNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 9)
)
if mibBuilder.loadTexts:
    hwOspfv3CfgNbrTable.setStatus("current")
_HwOspfv3CfgNbrEntry_Object = MibTableRow
hwOspfv3CfgNbrEntry = _HwOspfv3CfgNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 9, 1)
)
hwOspfv3CfgNbrEntry.setIndexNames(
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3CfgNbrIfIndex"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3CfgNbrIfInstId"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3CfgNbrRtrId"),
)
if mibBuilder.loadTexts:
    hwOspfv3CfgNbrEntry.setStatus("current")
_HwOspfv3CfgNbrIfIndex_Type = InterfaceIndex
_HwOspfv3CfgNbrIfIndex_Object = MibTableColumn
hwOspfv3CfgNbrIfIndex = _HwOspfv3CfgNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 9, 1, 1),
    _HwOspfv3CfgNbrIfIndex_Type()
)
hwOspfv3CfgNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3CfgNbrIfIndex.setStatus("current")
_HwOspfv3CfgNbrIfInstId_Type = HWOspfv3IfInstIdTc
_HwOspfv3CfgNbrIfInstId_Object = MibTableColumn
hwOspfv3CfgNbrIfInstId = _HwOspfv3CfgNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 9, 1, 2),
    _HwOspfv3CfgNbrIfInstId_Type()
)
hwOspfv3CfgNbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3CfgNbrIfInstId.setStatus("current")
_HwOspfv3CfgNbrRtrId_Type = HWOspfv3RouterIdTc
_HwOspfv3CfgNbrRtrId_Object = MibTableColumn
hwOspfv3CfgNbrRtrId = _HwOspfv3CfgNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 9, 1, 3),
    _HwOspfv3CfgNbrRtrId_Type()
)
hwOspfv3CfgNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3CfgNbrRtrId.setStatus("current")


class _HwOspfv3CfgNbrPriority_Type(DesignatedRouterPriority):
    """Custom type hwOspfv3CfgNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_HwOspfv3CfgNbrPriority_Object = MibTableColumn
hwOspfv3CfgNbrPriority = _HwOspfv3CfgNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 9, 1, 4),
    _HwOspfv3CfgNbrPriority_Type()
)
hwOspfv3CfgNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3CfgNbrPriority.setStatus("current")
_HwOspfv3CfgNbrRowStatus_Type = RowStatus
_HwOspfv3CfgNbrRowStatus_Object = MibTableColumn
hwOspfv3CfgNbrRowStatus = _HwOspfv3CfgNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 9, 1, 5),
    _HwOspfv3CfgNbrRowStatus_Type()
)
hwOspfv3CfgNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3CfgNbrRowStatus.setStatus("current")
_HwOspfv3VirtNbrTable_Object = MibTable
hwOspfv3VirtNbrTable = _HwOspfv3VirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10)
)
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrTable.setStatus("current")
_HwOspfv3VirtNbrEntry_Object = MibTableRow
hwOspfv3VirtNbrEntry = _HwOspfv3VirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1)
)
hwOspfv3VirtNbrEntry.setIndexNames(
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrArea"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrEntry.setStatus("current")
_HwOspfv3VirtNbrArea_Type = HWOspfv3AreaIdTc
_HwOspfv3VirtNbrArea_Object = MibTableColumn
hwOspfv3VirtNbrArea = _HwOspfv3VirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 1),
    _HwOspfv3VirtNbrArea_Type()
)
hwOspfv3VirtNbrArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrArea.setStatus("current")
_HwOspfv3VirtNbrRtrId_Type = HWOspfv3RouterIdTc
_HwOspfv3VirtNbrRtrId_Object = MibTableColumn
hwOspfv3VirtNbrRtrId = _HwOspfv3VirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 2),
    _HwOspfv3VirtNbrRtrId_Type()
)
hwOspfv3VirtNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrRtrId.setStatus("current")
_HwOspfv3VirtNbrIfIndex_Type = InterfaceIndex
_HwOspfv3VirtNbrIfIndex_Object = MibTableColumn
hwOspfv3VirtNbrIfIndex = _HwOspfv3VirtNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 3),
    _HwOspfv3VirtNbrIfIndex_Type()
)
hwOspfv3VirtNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrIfIndex.setStatus("current")
_HwOspfv3VirtNbrIfInstId_Type = HWOspfv3IfInstIdTc
_HwOspfv3VirtNbrIfInstId_Object = MibTableColumn
hwOspfv3VirtNbrIfInstId = _HwOspfv3VirtNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 4),
    _HwOspfv3VirtNbrIfInstId_Type()
)
hwOspfv3VirtNbrIfInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrIfInstId.setStatus("current")
_HwOspfv3VirtNbrAddressType_Type = InetAddressType
_HwOspfv3VirtNbrAddressType_Object = MibTableColumn
hwOspfv3VirtNbrAddressType = _HwOspfv3VirtNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 5),
    _HwOspfv3VirtNbrAddressType_Type()
)
hwOspfv3VirtNbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrAddressType.setStatus("current")
_HwOspfv3VirtNbrAddress_Type = InetAddress
_HwOspfv3VirtNbrAddress_Object = MibTableColumn
hwOspfv3VirtNbrAddress = _HwOspfv3VirtNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 6),
    _HwOspfv3VirtNbrAddress_Type()
)
hwOspfv3VirtNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrAddress.setStatus("current")
_HwOspfv3VirtNbrOptions_Type = Integer32
_HwOspfv3VirtNbrOptions_Object = MibTableColumn
hwOspfv3VirtNbrOptions = _HwOspfv3VirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 7),
    _HwOspfv3VirtNbrOptions_Type()
)
hwOspfv3VirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrOptions.setStatus("current")


class _HwOspfv3VirtNbrState_Type(Integer32):
    """Custom type hwOspfv3VirtNbrState based on Integer32"""
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


_HwOspfv3VirtNbrState_Type.__name__ = "Integer32"
_HwOspfv3VirtNbrState_Object = MibTableColumn
hwOspfv3VirtNbrState = _HwOspfv3VirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 8),
    _HwOspfv3VirtNbrState_Type()
)
hwOspfv3VirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrState.setStatus("current")
_HwOspfv3VirtNbrEvents_Type = Counter32
_HwOspfv3VirtNbrEvents_Object = MibTableColumn
hwOspfv3VirtNbrEvents = _HwOspfv3VirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 9),
    _HwOspfv3VirtNbrEvents_Type()
)
hwOspfv3VirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrEvents.setStatus("current")
_HwOspfv3VirtNbrLsRetransQLen_Type = Gauge32
_HwOspfv3VirtNbrLsRetransQLen_Object = MibTableColumn
hwOspfv3VirtNbrLsRetransQLen = _HwOspfv3VirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 10),
    _HwOspfv3VirtNbrLsRetransQLen_Type()
)
hwOspfv3VirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrLsRetransQLen.setStatus("current")
_HwOspfv3VirtNbrHelloSuppressed_Type = TruthValue
_HwOspfv3VirtNbrHelloSuppressed_Object = MibTableColumn
hwOspfv3VirtNbrHelloSuppressed = _HwOspfv3VirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 11),
    _HwOspfv3VirtNbrHelloSuppressed_Type()
)
hwOspfv3VirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrHelloSuppressed.setStatus("current")
_HwOspfv3VirtNbrIfId_Type = InterfaceIndex
_HwOspfv3VirtNbrIfId_Object = MibTableColumn
hwOspfv3VirtNbrIfId = _HwOspfv3VirtNbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 12),
    _HwOspfv3VirtNbrIfId_Type()
)
hwOspfv3VirtNbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrIfId.setStatus("current")


class _HwOspfv3VirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type hwOspfv3VirtNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("helping", 2),
          ("notHelping", 1))
    )


_HwOspfv3VirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_HwOspfv3VirtNbrRestartHelperStatus_Object = MibTableColumn
hwOspfv3VirtNbrRestartHelperStatus = _HwOspfv3VirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 13),
    _HwOspfv3VirtNbrRestartHelperStatus_Type()
)
hwOspfv3VirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrRestartHelperStatus.setStatus("current")
_HwOspfv3VirtNbrRestartHelperAge_Type = HWOspfv3UpToRefreshIntervalTc
_HwOspfv3VirtNbrRestartHelperAge_Object = MibTableColumn
hwOspfv3VirtNbrRestartHelperAge = _HwOspfv3VirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 14),
    _HwOspfv3VirtNbrRestartHelperAge_Type()
)
hwOspfv3VirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrRestartHelperAge.setUnits("seconds")


class _HwOspfv3VirtNbrRestartHelperExitRc_Type(Integer32):
    """Custom type hwOspfv3VirtNbrRestartHelperExitRc based on Integer32"""
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
        *(("completed", 3),
          ("inProgress", 2),
          ("none", 1),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_HwOspfv3VirtNbrRestartHelperExitRc_Type.__name__ = "Integer32"
_HwOspfv3VirtNbrRestartHelperExitRc_Object = MibTableColumn
hwOspfv3VirtNbrRestartHelperExitRc = _HwOspfv3VirtNbrRestartHelperExitRc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 10, 1, 15),
    _HwOspfv3VirtNbrRestartHelperExitRc_Type()
)
hwOspfv3VirtNbrRestartHelperExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrRestartHelperExitRc.setStatus("current")
_HwOspfv3AreaAggregateTable_Object = MibTable
hwOspfv3AreaAggregateTable = _HwOspfv3AreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 11)
)
if mibBuilder.loadTexts:
    hwOspfv3AreaAggregateTable.setStatus("current")
_HwOspfv3AreaAggregateEntry_Object = MibTableRow
hwOspfv3AreaAggregateEntry = _HwOspfv3AreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 11, 1)
)
hwOspfv3AreaAggregateEntry.setIndexNames(
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AreaAggregateAreaId"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AreaAggregateAreaLsdbType"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AreaAggregatePrefixType"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AreaAggregatePrefix"),
    (0, "HUAWEI-OSPFV3-MIB", "hwOspfv3AreaAggregatePrefixLength"),
)
if mibBuilder.loadTexts:
    hwOspfv3AreaAggregateEntry.setStatus("current")
_HwOspfv3AreaAggregateAreaId_Type = HWOspfv3AreaIdTc
_HwOspfv3AreaAggregateAreaId_Object = MibTableColumn
hwOspfv3AreaAggregateAreaId = _HwOspfv3AreaAggregateAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 11, 1, 1),
    _HwOspfv3AreaAggregateAreaId_Type()
)
hwOspfv3AreaAggregateAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AreaAggregateAreaId.setStatus("current")


class _HwOspfv3AreaAggregateAreaLsdbType_Type(Integer32):
    """Custom type hwOspfv3AreaAggregateAreaLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8195,
              8199)
        )
    )
    namedValues = NamedValues(
        *(("interAreaPrefixLsa", 8195),
          ("nssaExternalLsa", 8199))
    )


_HwOspfv3AreaAggregateAreaLsdbType_Type.__name__ = "Integer32"
_HwOspfv3AreaAggregateAreaLsdbType_Object = MibTableColumn
hwOspfv3AreaAggregateAreaLsdbType = _HwOspfv3AreaAggregateAreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 11, 1, 2),
    _HwOspfv3AreaAggregateAreaLsdbType_Type()
)
hwOspfv3AreaAggregateAreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AreaAggregateAreaLsdbType.setStatus("current")
_HwOspfv3AreaAggregatePrefixType_Type = InetAddressType
_HwOspfv3AreaAggregatePrefixType_Object = MibTableColumn
hwOspfv3AreaAggregatePrefixType = _HwOspfv3AreaAggregatePrefixType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 11, 1, 4),
    _HwOspfv3AreaAggregatePrefixType_Type()
)
hwOspfv3AreaAggregatePrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AreaAggregatePrefixType.setStatus("current")
_HwOspfv3AreaAggregatePrefix_Type = InetAddress
_HwOspfv3AreaAggregatePrefix_Object = MibTableColumn
hwOspfv3AreaAggregatePrefix = _HwOspfv3AreaAggregatePrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 11, 1, 5),
    _HwOspfv3AreaAggregatePrefix_Type()
)
hwOspfv3AreaAggregatePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AreaAggregatePrefix.setStatus("current")


class _HwOspfv3AreaAggregatePrefixLength_Type(InetAddressPrefixLength):
    """Custom type hwOspfv3AreaAggregatePrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwOspfv3AreaAggregatePrefixLength_Type.__name__ = "InetAddressPrefixLength"
_HwOspfv3AreaAggregatePrefixLength_Object = MibTableColumn
hwOspfv3AreaAggregatePrefixLength = _HwOspfv3AreaAggregatePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 11, 1, 6),
    _HwOspfv3AreaAggregatePrefixLength_Type()
)
hwOspfv3AreaAggregatePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOspfv3AreaAggregatePrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    hwOspfv3AreaAggregatePrefixLength.setUnits("bits")
_HwOspfv3AreaAggregateRowStatus_Type = RowStatus
_HwOspfv3AreaAggregateRowStatus_Object = MibTableColumn
hwOspfv3AreaAggregateRowStatus = _HwOspfv3AreaAggregateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 11, 1, 7),
    _HwOspfv3AreaAggregateRowStatus_Type()
)
hwOspfv3AreaAggregateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3AreaAggregateRowStatus.setStatus("current")


class _HwOspfv3AreaAggregateEffect_Type(Integer32):
    """Custom type hwOspfv3AreaAggregateEffect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertiseMatching", 1),
          ("doNotAdvertiseMatching", 2))
    )


_HwOspfv3AreaAggregateEffect_Type.__name__ = "Integer32"
_HwOspfv3AreaAggregateEffect_Object = MibTableColumn
hwOspfv3AreaAggregateEffect = _HwOspfv3AreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 11, 1, 8),
    _HwOspfv3AreaAggregateEffect_Type()
)
hwOspfv3AreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOspfv3AreaAggregateEffect.setStatus("current")
_HwOspfv3NotificationEntry_ObjectIdentity = ObjectIdentity
hwOspfv3NotificationEntry = _HwOspfv3NotificationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 12)
)


class _HwOspfv3ConfigErrorType_Type(Integer32):
    """Custom type hwOspfv3ConfigErrorType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("areaMismatch", 2),
          ("badVersion", 1),
          ("deadIntervalMismatch", 6),
          ("duplicateRouterId", 9),
          ("helloIntervalMismatch", 5),
          ("mtuMismatch", 8),
          ("noError", 10),
          ("optionMismatch", 7),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4))
    )


_HwOspfv3ConfigErrorType_Type.__name__ = "Integer32"
_HwOspfv3ConfigErrorType_Object = MibScalar
hwOspfv3ConfigErrorType = _HwOspfv3ConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 12, 1),
    _HwOspfv3ConfigErrorType_Type()
)
hwOspfv3ConfigErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwOspfv3ConfigErrorType.setStatus("current")


class _HwOspfv3PacketType_Type(Integer32):
    """Custom type hwOspfv3PacketType based on Integer32"""
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
        *(("dbDescript", 2),
          ("hello", 1),
          ("lsAck", 5),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("nullPacket", 6))
    )


_HwOspfv3PacketType_Type.__name__ = "Integer32"
_HwOspfv3PacketType_Object = MibScalar
hwOspfv3PacketType = _HwOspfv3PacketType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 12, 2),
    _HwOspfv3PacketType_Type()
)
hwOspfv3PacketType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwOspfv3PacketType.setStatus("current")
_HwOspfv3PacketSrc_Type = InetAddress
_HwOspfv3PacketSrc_Object = MibScalar
hwOspfv3PacketSrc = _HwOspfv3PacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 12, 3),
    _HwOspfv3PacketSrc_Type()
)
hwOspfv3PacketSrc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwOspfv3PacketSrc.setStatus("current")


class _HwOspfv3IfName_Type(OctetString):
    """Custom type hwOspfv3IfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwOspfv3IfName_Type.__name__ = "OctetString"
_HwOspfv3IfName_Object = MibScalar
hwOspfv3IfName = _HwOspfv3IfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 12, 4),
    _HwOspfv3IfName_Type()
)
hwOspfv3IfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwOspfv3IfName.setStatus("current")


class _HwOspfv3IfStateChgReason_Type(Integer32):
    """Custom type hwOspfv3IfStateChgReason based on Integer32"""
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
        *(("backupSeenOccured", 4),
          ("interfaceDown", 8),
          ("interfaceUp", 2),
          ("loopInd", 6),
          ("neighborChangeEventOccured", 5),
          ("noEvent", 1),
          ("unloopInd", 7),
          ("waitTimerExpired", 3))
    )


_HwOspfv3IfStateChgReason_Type.__name__ = "Integer32"
_HwOspfv3IfStateChgReason_Object = MibScalar
hwOspfv3IfStateChgReason = _HwOspfv3IfStateChgReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 12, 5),
    _HwOspfv3IfStateChgReason_Type()
)
hwOspfv3IfStateChgReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwOspfv3IfStateChgReason.setStatus("current")


class _HwOspfv3NbrStateChgReason_Type(Integer32):
    """Custom type hwOspfv3NbrStateChgReason based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("establishedAdjacency", 9),
          ("exchangeDone", 6),
          ("inactivityTimerExpired", 13),
          ("linkDown", 14),
          ("loadingDone", 8),
          ("mismatchInSeqNumber", 10),
          ("nbrKilled", 12),
          ("negotiationDone", 5),
          ("noEvent", 1),
          ("receivedBadLSRequest", 7),
          ("receivedHelloPacket", 2),
          ("receivedOneWay", 11),
          ("receivedTwoWay", 4),
          ("start", 3))
    )


_HwOspfv3NbrStateChgReason_Type.__name__ = "Integer32"
_HwOspfv3NbrStateChgReason_Object = MibScalar
hwOspfv3NbrStateChgReason = _HwOspfv3NbrStateChgReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 12, 6),
    _HwOspfv3NbrStateChgReason_Type()
)
hwOspfv3NbrStateChgReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwOspfv3NbrStateChgReason.setStatus("current")


class _HwOspfv3ProcessId_Type(Integer32):
    """Custom type hwOspfv3ProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwOspfv3ProcessId_Type.__name__ = "Integer32"
_HwOspfv3ProcessId_Object = MibScalar
hwOspfv3ProcessId = _HwOspfv3ProcessId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 12, 7),
    _HwOspfv3ProcessId_Type()
)
hwOspfv3ProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3ProcessId.setStatus("current")
_HwOspfv3AreaIdIndex_Type = HWOspfv3AreaIdTc
_HwOspfv3AreaIdIndex_Object = MibScalar
hwOspfv3AreaIdIndex = _HwOspfv3AreaIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 12, 8),
    _HwOspfv3AreaIdIndex_Type()
)
hwOspfv3AreaIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3AreaIdIndex.setStatus("current")
_HwOspfv3NewRouterId_Type = HWOspfv3RouterIdTc
_HwOspfv3NewRouterId_Object = MibScalar
hwOspfv3NewRouterId = _HwOspfv3NewRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 1, 12, 9),
    _HwOspfv3NewRouterId_Type()
)
hwOspfv3NewRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOspfv3NewRouterId.setStatus("current")
_HwOspfv3Conformance_ObjectIdentity = ObjectIdentity
hwOspfv3Conformance = _HwOspfv3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2)
)
_HwOspfv3Groups_ObjectIdentity = ObjectIdentity
hwOspfv3Groups = _HwOspfv3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1)
)
_HwOspfv3Compliances_ObjectIdentity = ObjectIdentity
hwOspfv3Compliances = _HwOspfv3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 2)
)

# Managed Objects groups

hwOspfv3BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 1)
)
hwOspfv3BasicGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AdminStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VersionNumber"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaBdrRtrStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AsBdrRtrStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AsScopeLsaCount"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AsScopeLsaCksumSum"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3OriginateNewLsas"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3RxNewLsas"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3ExtLsaCount"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3ExtAreaLsdbLimit"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3RestartSupport"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3RestartInterval"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3RestartStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3RestartAge"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3RestartExitRc"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NotificationEnable"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3ReferenceBandwidth"))
)
if mibBuilder.loadTexts:
    hwOspfv3BasicGroup.setStatus("current")

hwOspfv3AreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 2)
)
hwOspfv3AreaGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaImportAsExtern"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaSpfRuns"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaBdrRtrCount"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaAsBdrRtrCount"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaScopeLsaCount"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaScopeLsaCksumSum"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaSummary"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaRowStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaStubMetric"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaNssaTranslatorRole"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaNssaTranslatorState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaNssaTranslatorStabInterval"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaNssaTranslatorEvents"))
)
if mibBuilder.loadTexts:
    hwOspfv3AreaGroup.setStatus("current")

hwOspfv3AsLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 3)
)
hwOspfv3AsLsdbGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3AsLsdbSequence"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AsLsdbAge"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AsLsdbChecksum"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AsLsdbAdvertisement"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AsLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    hwOspfv3AsLsdbGroup.setStatus("current")

hwOspfv3AreaLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 4)
)
hwOspfv3AreaLsdbGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaLsdbSequence"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaLsdbAge"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaLsdbChecksum"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaLsdbAdvertisement"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    hwOspfv3AreaLsdbGroup.setStatus("current")

hwOspfv3LinkLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 5)
)
hwOspfv3LinkLsdbGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3LinkLsdbSequence"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3LinkLsdbAge"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3LinkLsdbChecksum"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3LinkLsdbAdvertisement"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3LinkLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    hwOspfv3LinkLsdbGroup.setStatus("current")

hwOspfv3IfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 6)
)
hwOspfv3IfGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3IfAreaId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfType"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfAdminStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfRtrPriority"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfTransitDelay"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfRetransInterval"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfHelloInterval"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfRtrDeadInterval"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfDesignatedRouter"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfBackupDesignatedRouter"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfEvents"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfRowStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfMetricValue"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfLinkScopeLsaCount"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfLinkLsaCksumSum"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfPollInterval"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfMulticastForwarding"))
)
if mibBuilder.loadTexts:
    hwOspfv3IfGroup.setStatus("current")

hwOspfv3VirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 7)
)
hwOspfv3VirtIfGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfIndex"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfInstId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfTransitDelay"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfRetransInterval"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfHelloInterval"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfRtrDeadInterval"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfEvents"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfRowStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfLinkScopeLsaCount"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfLinkLsaCksumSum"))
)
if mibBuilder.loadTexts:
    hwOspfv3VirtIfGroup.setStatus("current")

hwOspfv3NbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 8)
)
hwOspfv3NbrGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrAddressType"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrAddress"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrOptions"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrPriority"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrEvents"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrLsRetransQLen"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrHelloSuppressed"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrIfId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrRestartHelperStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrRestartHelperAge"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    hwOspfv3NbrGroup.setStatus("current")

hwOspfv3CfgNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 9)
)
hwOspfv3CfgNbrGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3CfgNbrPriority"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3CfgNbrRowStatus"))
)
if mibBuilder.loadTexts:
    hwOspfv3CfgNbrGroup.setStatus("current")

hwOspfv3VirtNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 10)
)
hwOspfv3VirtNbrGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrIfIndex"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrIfInstId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrAddressType"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrAddress"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrOptions"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrEvents"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrLsRetransQLen"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrHelloSuppressed"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrIfId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrRestartHelperStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrRestartHelperAge"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrGroup.setStatus("current")

hwOspfv3AreaAggregateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 11)
)
hwOspfv3AreaAggregateGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaAggregateRowStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaAggregateEffect"))
)
if mibBuilder.loadTexts:
    hwOspfv3AreaAggregateGroup.setStatus("current")

hwOspfv3NotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 12)
)
hwOspfv3NotificationObjectGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3ConfigErrorType"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3PacketType"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3PacketSrc"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfName"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfStateChgReason"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrStateChgReason"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3ProcessId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaIdIndex"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NewRouterId"))
)
if mibBuilder.loadTexts:
    hwOspfv3NotificationObjectGroup.setStatus("current")


# Notification objects

hwOspfv3VirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 1)
)
hwOspfv3VirtIfStateChange.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfStateChgReason"))
)
if mibBuilder.loadTexts:
    hwOspfv3VirtIfStateChange.setStatus(
        "current"
    )

hwOspfv3NbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 2)
)
hwOspfv3NbrStateChange.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfName"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrStateChgReason"))
)
if mibBuilder.loadTexts:
    hwOspfv3NbrStateChange.setStatus(
        "current"
    )

hwOspfv3VirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 3)
)
hwOspfv3VirtNbrStateChange.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrStateChgReason"))
)
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrStateChange.setStatus(
        "current"
    )

hwOspfv3IfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 4)
)
hwOspfv3IfConfigError.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3PacketSrc"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3ConfigErrorType"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3PacketType"))
)
if mibBuilder.loadTexts:
    hwOspfv3IfConfigError.setStatus(
        "current"
    )

hwOspfv3VirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 5)
)
hwOspfv3VirtIfConfigError.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3ConfigErrorType"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3PacketType"))
)
if mibBuilder.loadTexts:
    hwOspfv3VirtIfConfigError.setStatus(
        "current"
    )

hwOspfv3IfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 6)
)
hwOspfv3IfRxBadPacket.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3PacketSrc"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3PacketType"))
)
if mibBuilder.loadTexts:
    hwOspfv3IfRxBadPacket.setStatus(
        "current"
    )

hwOspfv3VirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 7)
)
hwOspfv3VirtIfRxBadPacket.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3PacketType"))
)
if mibBuilder.loadTexts:
    hwOspfv3VirtIfRxBadPacket.setStatus(
        "current"
    )

hwOspfv3IfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 8)
)
hwOspfv3IfStateChange.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfState"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfName"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfStateChgReason"))
)
if mibBuilder.loadTexts:
    hwOspfv3IfStateChange.setStatus(
        "current"
    )

hwOspfv3RestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 9)
)
hwOspfv3RestartStatusChange.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3RestartStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3RestartInterval"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3RestartExitRc"))
)
if mibBuilder.loadTexts:
    hwOspfv3RestartStatusChange.setStatus(
        "current"
    )

hwOspfv3NbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 10)
)
hwOspfv3NbrRestartHelperStatusChange.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrRestartHelperStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrRestartHelperAge"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    hwOspfv3NbrRestartHelperStatusChange.setStatus(
        "current"
    )

hwOspfv3VirtNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 11)
)
hwOspfv3VirtNbrRestartHelperStatusChange.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrRestartHelperStatus"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrRestartHelperAge"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    hwOspfv3VirtNbrRestartHelperStatusChange.setStatus(
        "current"
    )

hwOspfv3NssaTranslatorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 12)
)
hwOspfv3NssaTranslatorStatusChange.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaNssaTranslatorState"))
)
if mibBuilder.loadTexts:
    hwOspfv3NssaTranslatorStatusChange.setStatus(
        "current"
    )

hwOspfv3LastAuthKeyExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 13)
)
hwOspfv3LastAuthKeyExpiry.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfName"))
)
if mibBuilder.loadTexts:
    hwOspfv3LastAuthKeyExpiry.setStatus(
        "current"
    )

hwOspfv3AuthSequenceNumWrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 14)
)
hwOspfv3AuthSequenceNumWrap.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfName"))
)
if mibBuilder.loadTexts:
    hwOspfv3AuthSequenceNumWrap.setStatus(
        "current"
    )

hwOspfv3IntraAreaRouterIdConflictRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 0, 15)
)
hwOspfv3IntraAreaRouterIdConflictRecovered.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3ProcessId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AreaIdIndex"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3RouterId"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NewRouterId"))
)
if mibBuilder.loadTexts:
    hwOspfv3IntraAreaRouterIdConflictRecovered.setStatus(
        "current"
    )


# Notifications groups

hwOspfv3NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 1, 13)
)
hwOspfv3NotificationGroup.setObjects(
      *(("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfStateChange"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrStateChange"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrStateChange"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfConfigError"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfConfigError"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfRxBadPacket"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtIfRxBadPacket"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IfStateChange"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3RestartStatusChange"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NbrRestartHelperStatusChange"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3VirtNbrRestartHelperStatusChange"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3NssaTranslatorStatusChange"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3LastAuthKeyExpiry"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3AuthSequenceNumWrap"),
        ("HUAWEI-OSPFV3-MIB", "hwOspfv3IntraAreaRouterIdConflictRecovered"))
)
if mibBuilder.loadTexts:
    hwOspfv3NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwOspfv3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwOspfv3Compliance.setStatus(
        "current"
    )

hwOspfv3ReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 147, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hwOspfv3ReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-OSPFV3-MIB",
    **{"HWOspfv3UpToRefreshIntervalTc": HWOspfv3UpToRefreshIntervalTc,
       "HWOspfv3DeadIntRangeTc": HWOspfv3DeadIntRangeTc,
       "HWOspfv3RouterIdTc": HWOspfv3RouterIdTc,
       "HWOspfv3LsIdTC": HWOspfv3LsIdTC,
       "HWOspfv3AreaIdTc": HWOspfv3AreaIdTc,
       "HWOspfv3IfInstIdTc": HWOspfv3IfInstIdTc,
       "HWOspfv3LsaSequenceTC": HWOspfv3LsaSequenceTC,
       "HWOspfv3LsaAgeTC": HWOspfv3LsaAgeTC,
       "HWHelloRange": HWHelloRange,
       "hwOspfv3": hwOspfv3,
       "hwOspfv3Notifications": hwOspfv3Notifications,
       "hwOspfv3VirtIfStateChange": hwOspfv3VirtIfStateChange,
       "hwOspfv3NbrStateChange": hwOspfv3NbrStateChange,
       "hwOspfv3VirtNbrStateChange": hwOspfv3VirtNbrStateChange,
       "hwOspfv3IfConfigError": hwOspfv3IfConfigError,
       "hwOspfv3VirtIfConfigError": hwOspfv3VirtIfConfigError,
       "hwOspfv3IfRxBadPacket": hwOspfv3IfRxBadPacket,
       "hwOspfv3VirtIfRxBadPacket": hwOspfv3VirtIfRxBadPacket,
       "hwOspfv3IfStateChange": hwOspfv3IfStateChange,
       "hwOspfv3RestartStatusChange": hwOspfv3RestartStatusChange,
       "hwOspfv3NbrRestartHelperStatusChange": hwOspfv3NbrRestartHelperStatusChange,
       "hwOspfv3VirtNbrRestartHelperStatusChange": hwOspfv3VirtNbrRestartHelperStatusChange,
       "hwOspfv3NssaTranslatorStatusChange": hwOspfv3NssaTranslatorStatusChange,
       "hwOspfv3LastAuthKeyExpiry": hwOspfv3LastAuthKeyExpiry,
       "hwOspfv3AuthSequenceNumWrap": hwOspfv3AuthSequenceNumWrap,
       "hwOspfv3IntraAreaRouterIdConflictRecovered": hwOspfv3IntraAreaRouterIdConflictRecovered,
       "hwOspfv3Objects": hwOspfv3Objects,
       "hwOspfv3GeneralGroup": hwOspfv3GeneralGroup,
       "hwOspfv3RouterId": hwOspfv3RouterId,
       "hwOspfv3AdminStatus": hwOspfv3AdminStatus,
       "hwOspfv3VersionNumber": hwOspfv3VersionNumber,
       "hwOspfv3AreaBdrRtrStatus": hwOspfv3AreaBdrRtrStatus,
       "hwOspfv3AsBdrRtrStatus": hwOspfv3AsBdrRtrStatus,
       "hwOspfv3AsScopeLsaCount": hwOspfv3AsScopeLsaCount,
       "hwOspfv3AsScopeLsaCksumSum": hwOspfv3AsScopeLsaCksumSum,
       "hwOspfv3OriginateNewLsas": hwOspfv3OriginateNewLsas,
       "hwOspfv3RxNewLsas": hwOspfv3RxNewLsas,
       "hwOspfv3ExtLsaCount": hwOspfv3ExtLsaCount,
       "hwOspfv3ExtAreaLsdbLimit": hwOspfv3ExtAreaLsdbLimit,
       "hwOspfv3RestartSupport": hwOspfv3RestartSupport,
       "hwOspfv3RestartInterval": hwOspfv3RestartInterval,
       "hwOspfv3RestartStatus": hwOspfv3RestartStatus,
       "hwOspfv3RestartAge": hwOspfv3RestartAge,
       "hwOspfv3RestartExitRc": hwOspfv3RestartExitRc,
       "hwOspfv3NotificationEnable": hwOspfv3NotificationEnable,
       "hwOspfv3ReferenceBandwidth": hwOspfv3ReferenceBandwidth,
       "hwOspfv3AreaTable": hwOspfv3AreaTable,
       "hwOspfv3AreaEntry": hwOspfv3AreaEntry,
       "hwOspfv3AreaId": hwOspfv3AreaId,
       "hwOspfv3AreaImportAsExtern": hwOspfv3AreaImportAsExtern,
       "hwOspfv3AreaSpfRuns": hwOspfv3AreaSpfRuns,
       "hwOspfv3AreaBdrRtrCount": hwOspfv3AreaBdrRtrCount,
       "hwOspfv3AreaAsBdrRtrCount": hwOspfv3AreaAsBdrRtrCount,
       "hwOspfv3AreaScopeLsaCount": hwOspfv3AreaScopeLsaCount,
       "hwOspfv3AreaScopeLsaCksumSum": hwOspfv3AreaScopeLsaCksumSum,
       "hwOspfv3AreaSummary": hwOspfv3AreaSummary,
       "hwOspfv3AreaRowStatus": hwOspfv3AreaRowStatus,
       "hwOspfv3AreaStubMetric": hwOspfv3AreaStubMetric,
       "hwOspfv3AreaNssaTranslatorRole": hwOspfv3AreaNssaTranslatorRole,
       "hwOspfv3AreaNssaTranslatorState": hwOspfv3AreaNssaTranslatorState,
       "hwOspfv3AreaNssaTranslatorStabInterval": hwOspfv3AreaNssaTranslatorStabInterval,
       "hwOspfv3AreaNssaTranslatorEvents": hwOspfv3AreaNssaTranslatorEvents,
       "hwOspfv3AsLsdbTable": hwOspfv3AsLsdbTable,
       "hwOspfv3AsLsdbEntry": hwOspfv3AsLsdbEntry,
       "hwOspfv3AsLsdbType": hwOspfv3AsLsdbType,
       "hwOspfv3AsLsdbRouterId": hwOspfv3AsLsdbRouterId,
       "hwOspfv3AsLsdbLsId": hwOspfv3AsLsdbLsId,
       "hwOspfv3AsLsdbSequence": hwOspfv3AsLsdbSequence,
       "hwOspfv3AsLsdbAge": hwOspfv3AsLsdbAge,
       "hwOspfv3AsLsdbChecksum": hwOspfv3AsLsdbChecksum,
       "hwOspfv3AsLsdbAdvertisement": hwOspfv3AsLsdbAdvertisement,
       "hwOspfv3AsLsdbTypeKnown": hwOspfv3AsLsdbTypeKnown,
       "hwOspfv3AreaLsdbTable": hwOspfv3AreaLsdbTable,
       "hwOspfv3AreaLsdbEntry": hwOspfv3AreaLsdbEntry,
       "hwOspfv3AreaLsdbAreaId": hwOspfv3AreaLsdbAreaId,
       "hwOspfv3AreaLsdbType": hwOspfv3AreaLsdbType,
       "hwOspfv3AreaLsdbRouterId": hwOspfv3AreaLsdbRouterId,
       "hwOspfv3AreaLsdbLsId": hwOspfv3AreaLsdbLsId,
       "hwOspfv3AreaLsdbSequence": hwOspfv3AreaLsdbSequence,
       "hwOspfv3AreaLsdbAge": hwOspfv3AreaLsdbAge,
       "hwOspfv3AreaLsdbChecksum": hwOspfv3AreaLsdbChecksum,
       "hwOspfv3AreaLsdbAdvertisement": hwOspfv3AreaLsdbAdvertisement,
       "hwOspfv3AreaLsdbTypeKnown": hwOspfv3AreaLsdbTypeKnown,
       "hwOspfv3LinkLsdbTable": hwOspfv3LinkLsdbTable,
       "hwOspfv3LinkLsdbEntry": hwOspfv3LinkLsdbEntry,
       "hwOspfv3LinkLsdbIfIndex": hwOspfv3LinkLsdbIfIndex,
       "hwOspfv3LinkLsdbIfInstId": hwOspfv3LinkLsdbIfInstId,
       "hwOspfv3LinkLsdbType": hwOspfv3LinkLsdbType,
       "hwOspfv3LinkLsdbRouterId": hwOspfv3LinkLsdbRouterId,
       "hwOspfv3LinkLsdbLsId": hwOspfv3LinkLsdbLsId,
       "hwOspfv3LinkLsdbSequence": hwOspfv3LinkLsdbSequence,
       "hwOspfv3LinkLsdbAge": hwOspfv3LinkLsdbAge,
       "hwOspfv3LinkLsdbChecksum": hwOspfv3LinkLsdbChecksum,
       "hwOspfv3LinkLsdbAdvertisement": hwOspfv3LinkLsdbAdvertisement,
       "hwOspfv3LinkLsdbTypeKnown": hwOspfv3LinkLsdbTypeKnown,
       "hwOspfv3IfTable": hwOspfv3IfTable,
       "hwOspfv3IfEntry": hwOspfv3IfEntry,
       "hwOspfv3IfIndex": hwOspfv3IfIndex,
       "hwOspfv3IfInstId": hwOspfv3IfInstId,
       "hwOspfv3IfAreaId": hwOspfv3IfAreaId,
       "hwOspfv3IfType": hwOspfv3IfType,
       "hwOspfv3IfAdminStatus": hwOspfv3IfAdminStatus,
       "hwOspfv3IfRtrPriority": hwOspfv3IfRtrPriority,
       "hwOspfv3IfTransitDelay": hwOspfv3IfTransitDelay,
       "hwOspfv3IfRetransInterval": hwOspfv3IfRetransInterval,
       "hwOspfv3IfHelloInterval": hwOspfv3IfHelloInterval,
       "hwOspfv3IfRtrDeadInterval": hwOspfv3IfRtrDeadInterval,
       "hwOspfv3IfState": hwOspfv3IfState,
       "hwOspfv3IfDesignatedRouter": hwOspfv3IfDesignatedRouter,
       "hwOspfv3IfBackupDesignatedRouter": hwOspfv3IfBackupDesignatedRouter,
       "hwOspfv3IfEvents": hwOspfv3IfEvents,
       "hwOspfv3IfRowStatus": hwOspfv3IfRowStatus,
       "hwOspfv3IfMetricValue": hwOspfv3IfMetricValue,
       "hwOspfv3IfLinkScopeLsaCount": hwOspfv3IfLinkScopeLsaCount,
       "hwOspfv3IfLinkLsaCksumSum": hwOspfv3IfLinkLsaCksumSum,
       "hwOspfv3IfPollInterval": hwOspfv3IfPollInterval,
       "hwOspfv3IfMulticastForwarding": hwOspfv3IfMulticastForwarding,
       "hwOspfv3VirtIfTable": hwOspfv3VirtIfTable,
       "hwOspfv3VirtIfEntry": hwOspfv3VirtIfEntry,
       "hwOspfv3VirtIfAreaId": hwOspfv3VirtIfAreaId,
       "hwOspfv3VirtIfNeighbor": hwOspfv3VirtIfNeighbor,
       "hwOspfv3VirtIfIndex": hwOspfv3VirtIfIndex,
       "hwOspfv3VirtIfInstId": hwOspfv3VirtIfInstId,
       "hwOspfv3VirtIfTransitDelay": hwOspfv3VirtIfTransitDelay,
       "hwOspfv3VirtIfRetransInterval": hwOspfv3VirtIfRetransInterval,
       "hwOspfv3VirtIfHelloInterval": hwOspfv3VirtIfHelloInterval,
       "hwOspfv3VirtIfRtrDeadInterval": hwOspfv3VirtIfRtrDeadInterval,
       "hwOspfv3VirtIfState": hwOspfv3VirtIfState,
       "hwOspfv3VirtIfEvents": hwOspfv3VirtIfEvents,
       "hwOspfv3VirtIfRowStatus": hwOspfv3VirtIfRowStatus,
       "hwOspfv3VirtIfLinkScopeLsaCount": hwOspfv3VirtIfLinkScopeLsaCount,
       "hwOspfv3VirtIfLinkLsaCksumSum": hwOspfv3VirtIfLinkLsaCksumSum,
       "hwOspfv3NbrTable": hwOspfv3NbrTable,
       "hwOspfv3NbrEntry": hwOspfv3NbrEntry,
       "hwOspfv3NbrIfIndex": hwOspfv3NbrIfIndex,
       "hwOspfv3NbrIfInstId": hwOspfv3NbrIfInstId,
       "hwOspfv3NbrRtrId": hwOspfv3NbrRtrId,
       "hwOspfv3NbrAddressType": hwOspfv3NbrAddressType,
       "hwOspfv3NbrAddress": hwOspfv3NbrAddress,
       "hwOspfv3NbrOptions": hwOspfv3NbrOptions,
       "hwOspfv3NbrPriority": hwOspfv3NbrPriority,
       "hwOspfv3NbrState": hwOspfv3NbrState,
       "hwOspfv3NbrEvents": hwOspfv3NbrEvents,
       "hwOspfv3NbrLsRetransQLen": hwOspfv3NbrLsRetransQLen,
       "hwOspfv3NbrHelloSuppressed": hwOspfv3NbrHelloSuppressed,
       "hwOspfv3NbrIfId": hwOspfv3NbrIfId,
       "hwOspfv3NbrRestartHelperStatus": hwOspfv3NbrRestartHelperStatus,
       "hwOspfv3NbrRestartHelperAge": hwOspfv3NbrRestartHelperAge,
       "hwOspfv3NbrRestartHelperExitRc": hwOspfv3NbrRestartHelperExitRc,
       "hwOspfv3CfgNbrTable": hwOspfv3CfgNbrTable,
       "hwOspfv3CfgNbrEntry": hwOspfv3CfgNbrEntry,
       "hwOspfv3CfgNbrIfIndex": hwOspfv3CfgNbrIfIndex,
       "hwOspfv3CfgNbrIfInstId": hwOspfv3CfgNbrIfInstId,
       "hwOspfv3CfgNbrRtrId": hwOspfv3CfgNbrRtrId,
       "hwOspfv3CfgNbrPriority": hwOspfv3CfgNbrPriority,
       "hwOspfv3CfgNbrRowStatus": hwOspfv3CfgNbrRowStatus,
       "hwOspfv3VirtNbrTable": hwOspfv3VirtNbrTable,
       "hwOspfv3VirtNbrEntry": hwOspfv3VirtNbrEntry,
       "hwOspfv3VirtNbrArea": hwOspfv3VirtNbrArea,
       "hwOspfv3VirtNbrRtrId": hwOspfv3VirtNbrRtrId,
       "hwOspfv3VirtNbrIfIndex": hwOspfv3VirtNbrIfIndex,
       "hwOspfv3VirtNbrIfInstId": hwOspfv3VirtNbrIfInstId,
       "hwOspfv3VirtNbrAddressType": hwOspfv3VirtNbrAddressType,
       "hwOspfv3VirtNbrAddress": hwOspfv3VirtNbrAddress,
       "hwOspfv3VirtNbrOptions": hwOspfv3VirtNbrOptions,
       "hwOspfv3VirtNbrState": hwOspfv3VirtNbrState,
       "hwOspfv3VirtNbrEvents": hwOspfv3VirtNbrEvents,
       "hwOspfv3VirtNbrLsRetransQLen": hwOspfv3VirtNbrLsRetransQLen,
       "hwOspfv3VirtNbrHelloSuppressed": hwOspfv3VirtNbrHelloSuppressed,
       "hwOspfv3VirtNbrIfId": hwOspfv3VirtNbrIfId,
       "hwOspfv3VirtNbrRestartHelperStatus": hwOspfv3VirtNbrRestartHelperStatus,
       "hwOspfv3VirtNbrRestartHelperAge": hwOspfv3VirtNbrRestartHelperAge,
       "hwOspfv3VirtNbrRestartHelperExitRc": hwOspfv3VirtNbrRestartHelperExitRc,
       "hwOspfv3AreaAggregateTable": hwOspfv3AreaAggregateTable,
       "hwOspfv3AreaAggregateEntry": hwOspfv3AreaAggregateEntry,
       "hwOspfv3AreaAggregateAreaId": hwOspfv3AreaAggregateAreaId,
       "hwOspfv3AreaAggregateAreaLsdbType": hwOspfv3AreaAggregateAreaLsdbType,
       "hwOspfv3AreaAggregatePrefixType": hwOspfv3AreaAggregatePrefixType,
       "hwOspfv3AreaAggregatePrefix": hwOspfv3AreaAggregatePrefix,
       "hwOspfv3AreaAggregatePrefixLength": hwOspfv3AreaAggregatePrefixLength,
       "hwOspfv3AreaAggregateRowStatus": hwOspfv3AreaAggregateRowStatus,
       "hwOspfv3AreaAggregateEffect": hwOspfv3AreaAggregateEffect,
       "hwOspfv3NotificationEntry": hwOspfv3NotificationEntry,
       "hwOspfv3ConfigErrorType": hwOspfv3ConfigErrorType,
       "hwOspfv3PacketType": hwOspfv3PacketType,
       "hwOspfv3PacketSrc": hwOspfv3PacketSrc,
       "hwOspfv3IfName": hwOspfv3IfName,
       "hwOspfv3IfStateChgReason": hwOspfv3IfStateChgReason,
       "hwOspfv3NbrStateChgReason": hwOspfv3NbrStateChgReason,
       "hwOspfv3ProcessId": hwOspfv3ProcessId,
       "hwOspfv3AreaIdIndex": hwOspfv3AreaIdIndex,
       "hwOspfv3NewRouterId": hwOspfv3NewRouterId,
       "hwOspfv3Conformance": hwOspfv3Conformance,
       "hwOspfv3Groups": hwOspfv3Groups,
       "hwOspfv3BasicGroup": hwOspfv3BasicGroup,
       "hwOspfv3AreaGroup": hwOspfv3AreaGroup,
       "hwOspfv3AsLsdbGroup": hwOspfv3AsLsdbGroup,
       "hwOspfv3AreaLsdbGroup": hwOspfv3AreaLsdbGroup,
       "hwOspfv3LinkLsdbGroup": hwOspfv3LinkLsdbGroup,
       "hwOspfv3IfGroup": hwOspfv3IfGroup,
       "hwOspfv3VirtIfGroup": hwOspfv3VirtIfGroup,
       "hwOspfv3NbrGroup": hwOspfv3NbrGroup,
       "hwOspfv3CfgNbrGroup": hwOspfv3CfgNbrGroup,
       "hwOspfv3VirtNbrGroup": hwOspfv3VirtNbrGroup,
       "hwOspfv3AreaAggregateGroup": hwOspfv3AreaAggregateGroup,
       "hwOspfv3NotificationObjectGroup": hwOspfv3NotificationObjectGroup,
       "hwOspfv3NotificationGroup": hwOspfv3NotificationGroup,
       "hwOspfv3Compliances": hwOspfv3Compliances,
       "hwOspfv3Compliance": hwOspfv3Compliance,
       "hwOspfv3ReadOnlyCompliance": hwOspfv3ReadOnlyCompliance}
)

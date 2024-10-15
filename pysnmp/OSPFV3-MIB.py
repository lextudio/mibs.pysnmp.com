# SNMP MIB module (OSPFV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OSPFV3-MIB
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ospfv3MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 191)
)
ospfv3MIB.setRevisions(
        ("2009-08-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Ospfv3UpToRefreshIntervalTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )



class Ospfv3DeadIntervalRangeTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class Ospfv3RouterIdTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class Ospfv3LsIdTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class Ospfv3AreaIdTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class Ospfv3IfInstIdTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class Ospfv3LsaSequenceTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class Ospfv3LsaAgeTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
        ValueRangeConstraint(32768, 36368),
    )



# MIB Managed Objects in the order of their OIDs

_Ospfv3Notifications_ObjectIdentity = ObjectIdentity
ospfv3Notifications = _Ospfv3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 191, 0)
)
_Ospfv3Objects_ObjectIdentity = ObjectIdentity
ospfv3Objects = _Ospfv3Objects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 191, 1)
)
_Ospfv3GeneralGroup_ObjectIdentity = ObjectIdentity
ospfv3GeneralGroup = _Ospfv3GeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 191, 1, 1)
)
_Ospfv3RouterId_Type = Ospfv3RouterIdTC
_Ospfv3RouterId_Object = MibScalar
ospfv3RouterId = _Ospfv3RouterId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 1),
    _Ospfv3RouterId_Type()
)
ospfv3RouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3RouterId.setStatus("current")
_Ospfv3AdminStatus_Type = Status
_Ospfv3AdminStatus_Object = MibScalar
ospfv3AdminStatus = _Ospfv3AdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 2),
    _Ospfv3AdminStatus_Type()
)
ospfv3AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3AdminStatus.setStatus("current")


class _Ospfv3VersionNumber_Type(Integer32):
    """Custom type ospfv3VersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("version3", 3)
    )


_Ospfv3VersionNumber_Type.__name__ = "Integer32"
_Ospfv3VersionNumber_Object = MibScalar
ospfv3VersionNumber = _Ospfv3VersionNumber_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 3),
    _Ospfv3VersionNumber_Type()
)
ospfv3VersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VersionNumber.setStatus("current")
_Ospfv3AreaBdrRtrStatus_Type = TruthValue
_Ospfv3AreaBdrRtrStatus_Object = MibScalar
ospfv3AreaBdrRtrStatus = _Ospfv3AreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 4),
    _Ospfv3AreaBdrRtrStatus_Type()
)
ospfv3AreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaBdrRtrStatus.setStatus("current")
_Ospfv3ASBdrRtrStatus_Type = TruthValue
_Ospfv3ASBdrRtrStatus_Object = MibScalar
ospfv3ASBdrRtrStatus = _Ospfv3ASBdrRtrStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 5),
    _Ospfv3ASBdrRtrStatus_Type()
)
ospfv3ASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3ASBdrRtrStatus.setStatus("current")
_Ospfv3AsScopeLsaCount_Type = Gauge32
_Ospfv3AsScopeLsaCount_Object = MibScalar
ospfv3AsScopeLsaCount = _Ospfv3AsScopeLsaCount_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 6),
    _Ospfv3AsScopeLsaCount_Type()
)
ospfv3AsScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AsScopeLsaCount.setStatus("current")
_Ospfv3AsScopeLsaCksumSum_Type = Unsigned32
_Ospfv3AsScopeLsaCksumSum_Object = MibScalar
ospfv3AsScopeLsaCksumSum = _Ospfv3AsScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 7),
    _Ospfv3AsScopeLsaCksumSum_Type()
)
ospfv3AsScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AsScopeLsaCksumSum.setStatus("current")
_Ospfv3OriginateNewLsas_Type = Counter32
_Ospfv3OriginateNewLsas_Object = MibScalar
ospfv3OriginateNewLsas = _Ospfv3OriginateNewLsas_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 8),
    _Ospfv3OriginateNewLsas_Type()
)
ospfv3OriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3OriginateNewLsas.setStatus("current")
_Ospfv3RxNewLsas_Type = Counter32
_Ospfv3RxNewLsas_Object = MibScalar
ospfv3RxNewLsas = _Ospfv3RxNewLsas_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 9),
    _Ospfv3RxNewLsas_Type()
)
ospfv3RxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3RxNewLsas.setStatus("current")
_Ospfv3ExtLsaCount_Type = Gauge32
_Ospfv3ExtLsaCount_Object = MibScalar
ospfv3ExtLsaCount = _Ospfv3ExtLsaCount_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 10),
    _Ospfv3ExtLsaCount_Type()
)
ospfv3ExtLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3ExtLsaCount.setStatus("current")


class _Ospfv3ExtAreaLsdbLimit_Type(Integer32):
    """Custom type ospfv3ExtAreaLsdbLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Ospfv3ExtAreaLsdbLimit_Type.__name__ = "Integer32"
_Ospfv3ExtAreaLsdbLimit_Object = MibScalar
ospfv3ExtAreaLsdbLimit = _Ospfv3ExtAreaLsdbLimit_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 11),
    _Ospfv3ExtAreaLsdbLimit_Type()
)
ospfv3ExtAreaLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3ExtAreaLsdbLimit.setStatus("current")
_Ospfv3ExitOverflowInterval_Type = Unsigned32
_Ospfv3ExitOverflowInterval_Object = MibScalar
ospfv3ExitOverflowInterval = _Ospfv3ExitOverflowInterval_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 12),
    _Ospfv3ExitOverflowInterval_Type()
)
ospfv3ExitOverflowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3ExitOverflowInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3ExitOverflowInterval.setUnits("seconds")
_Ospfv3DemandExtensions_Type = TruthValue
_Ospfv3DemandExtensions_Object = MibScalar
ospfv3DemandExtensions = _Ospfv3DemandExtensions_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 13),
    _Ospfv3DemandExtensions_Type()
)
ospfv3DemandExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3DemandExtensions.setStatus("current")


class _Ospfv3ReferenceBandwidth_Type(Unsigned32):
    """Custom type ospfv3ReferenceBandwidth based on Unsigned32"""
    defaultValue = 100000


_Ospfv3ReferenceBandwidth_Object = MibScalar
ospfv3ReferenceBandwidth = _Ospfv3ReferenceBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 14),
    _Ospfv3ReferenceBandwidth_Type()
)
ospfv3ReferenceBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3ReferenceBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3ReferenceBandwidth.setUnits("kilobits per second")


class _Ospfv3RestartSupport_Type(Integer32):
    """Custom type ospfv3RestartSupport based on Integer32"""
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


_Ospfv3RestartSupport_Type.__name__ = "Integer32"
_Ospfv3RestartSupport_Object = MibScalar
ospfv3RestartSupport = _Ospfv3RestartSupport_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 15),
    _Ospfv3RestartSupport_Type()
)
ospfv3RestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3RestartSupport.setStatus("current")


class _Ospfv3RestartInterval_Type(Ospfv3UpToRefreshIntervalTC):
    """Custom type ospfv3RestartInterval based on Ospfv3UpToRefreshIntervalTC"""
    defaultValue = 120


_Ospfv3RestartInterval_Object = MibScalar
ospfv3RestartInterval = _Ospfv3RestartInterval_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 16),
    _Ospfv3RestartInterval_Type()
)
ospfv3RestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3RestartInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3RestartInterval.setUnits("seconds")


class _Ospfv3RestartStrictLsaChecking_Type(TruthValue):
    """Custom type ospfv3RestartStrictLsaChecking based on TruthValue"""


_Ospfv3RestartStrictLsaChecking_Object = MibScalar
ospfv3RestartStrictLsaChecking = _Ospfv3RestartStrictLsaChecking_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 17),
    _Ospfv3RestartStrictLsaChecking_Type()
)
ospfv3RestartStrictLsaChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3RestartStrictLsaChecking.setStatus("current")


class _Ospfv3RestartStatus_Type(Integer32):
    """Custom type ospfv3RestartStatus based on Integer32"""
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


_Ospfv3RestartStatus_Type.__name__ = "Integer32"
_Ospfv3RestartStatus_Object = MibScalar
ospfv3RestartStatus = _Ospfv3RestartStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 18),
    _Ospfv3RestartStatus_Type()
)
ospfv3RestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3RestartStatus.setStatus("current")
_Ospfv3RestartAge_Type = Ospfv3UpToRefreshIntervalTC
_Ospfv3RestartAge_Object = MibScalar
ospfv3RestartAge = _Ospfv3RestartAge_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 19),
    _Ospfv3RestartAge_Type()
)
ospfv3RestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3RestartAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3RestartAge.setUnits("seconds")


class _Ospfv3RestartExitReason_Type(Integer32):
    """Custom type ospfv3RestartExitReason based on Integer32"""
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


_Ospfv3RestartExitReason_Type.__name__ = "Integer32"
_Ospfv3RestartExitReason_Object = MibScalar
ospfv3RestartExitReason = _Ospfv3RestartExitReason_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 20),
    _Ospfv3RestartExitReason_Type()
)
ospfv3RestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3RestartExitReason.setStatus("current")
_Ospfv3NotificationEnable_Type = TruthValue
_Ospfv3NotificationEnable_Object = MibScalar
ospfv3NotificationEnable = _Ospfv3NotificationEnable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 21),
    _Ospfv3NotificationEnable_Type()
)
ospfv3NotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3NotificationEnable.setStatus("current")
_Ospfv3StubRouterSupport_Type = TruthValue
_Ospfv3StubRouterSupport_Object = MibScalar
ospfv3StubRouterSupport = _Ospfv3StubRouterSupport_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 22),
    _Ospfv3StubRouterSupport_Type()
)
ospfv3StubRouterSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3StubRouterSupport.setStatus("current")


class _Ospfv3StubRouterAdvertisement_Type(Integer32):
    """Custom type ospfv3StubRouterAdvertisement based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("doNotAdvertise", 1))
    )


_Ospfv3StubRouterAdvertisement_Type.__name__ = "Integer32"
_Ospfv3StubRouterAdvertisement_Object = MibScalar
ospfv3StubRouterAdvertisement = _Ospfv3StubRouterAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 23),
    _Ospfv3StubRouterAdvertisement_Type()
)
ospfv3StubRouterAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfv3StubRouterAdvertisement.setStatus("current")
_Ospfv3DiscontinuityTime_Type = TimeStamp
_Ospfv3DiscontinuityTime_Object = MibScalar
ospfv3DiscontinuityTime = _Ospfv3DiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 24),
    _Ospfv3DiscontinuityTime_Type()
)
ospfv3DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3DiscontinuityTime.setStatus("current")
_Ospfv3RestartTime_Type = TimeStamp
_Ospfv3RestartTime_Object = MibScalar
ospfv3RestartTime = _Ospfv3RestartTime_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 1, 25),
    _Ospfv3RestartTime_Type()
)
ospfv3RestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3RestartTime.setStatus("current")
_Ospfv3AreaTable_Object = MibTable
ospfv3AreaTable = _Ospfv3AreaTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2)
)
if mibBuilder.loadTexts:
    ospfv3AreaTable.setStatus("current")
_Ospfv3AreaEntry_Object = MibTableRow
ospfv3AreaEntry = _Ospfv3AreaEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1)
)
ospfv3AreaEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3AreaId"),
)
if mibBuilder.loadTexts:
    ospfv3AreaEntry.setStatus("current")
_Ospfv3AreaId_Type = Ospfv3AreaIdTC
_Ospfv3AreaId_Object = MibTableColumn
ospfv3AreaId = _Ospfv3AreaId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 1),
    _Ospfv3AreaId_Type()
)
ospfv3AreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AreaId.setStatus("current")


class _Ospfv3AreaImportAsExtern_Type(Integer32):
    """Custom type ospfv3AreaImportAsExtern based on Integer32"""
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


_Ospfv3AreaImportAsExtern_Type.__name__ = "Integer32"
_Ospfv3AreaImportAsExtern_Object = MibTableColumn
ospfv3AreaImportAsExtern = _Ospfv3AreaImportAsExtern_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 2),
    _Ospfv3AreaImportAsExtern_Type()
)
ospfv3AreaImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3AreaImportAsExtern.setStatus("current")
_Ospfv3AreaSpfRuns_Type = Counter32
_Ospfv3AreaSpfRuns_Object = MibTableColumn
ospfv3AreaSpfRuns = _Ospfv3AreaSpfRuns_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 3),
    _Ospfv3AreaSpfRuns_Type()
)
ospfv3AreaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaSpfRuns.setStatus("current")


class _Ospfv3AreaBdrRtrCount_Type(Gauge32):
    """Custom type ospfv3AreaBdrRtrCount based on Gauge32"""
    defaultValue = 0


_Ospfv3AreaBdrRtrCount_Object = MibTableColumn
ospfv3AreaBdrRtrCount = _Ospfv3AreaBdrRtrCount_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 4),
    _Ospfv3AreaBdrRtrCount_Type()
)
ospfv3AreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaBdrRtrCount.setStatus("current")


class _Ospfv3AreaAsBdrRtrCount_Type(Gauge32):
    """Custom type ospfv3AreaAsBdrRtrCount based on Gauge32"""
    defaultValue = 0


_Ospfv3AreaAsBdrRtrCount_Object = MibTableColumn
ospfv3AreaAsBdrRtrCount = _Ospfv3AreaAsBdrRtrCount_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 5),
    _Ospfv3AreaAsBdrRtrCount_Type()
)
ospfv3AreaAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaAsBdrRtrCount.setStatus("current")


class _Ospfv3AreaScopeLsaCount_Type(Gauge32):
    """Custom type ospfv3AreaScopeLsaCount based on Gauge32"""
    defaultValue = 0


_Ospfv3AreaScopeLsaCount_Object = MibTableColumn
ospfv3AreaScopeLsaCount = _Ospfv3AreaScopeLsaCount_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 6),
    _Ospfv3AreaScopeLsaCount_Type()
)
ospfv3AreaScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaScopeLsaCount.setStatus("current")
_Ospfv3AreaScopeLsaCksumSum_Type = Unsigned32
_Ospfv3AreaScopeLsaCksumSum_Object = MibTableColumn
ospfv3AreaScopeLsaCksumSum = _Ospfv3AreaScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 7),
    _Ospfv3AreaScopeLsaCksumSum_Type()
)
ospfv3AreaScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaScopeLsaCksumSum.setStatus("current")


class _Ospfv3AreaSummary_Type(Integer32):
    """Custom type ospfv3AreaSummary based on Integer32"""
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


_Ospfv3AreaSummary_Type.__name__ = "Integer32"
_Ospfv3AreaSummary_Object = MibTableColumn
ospfv3AreaSummary = _Ospfv3AreaSummary_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 8),
    _Ospfv3AreaSummary_Type()
)
ospfv3AreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3AreaSummary.setStatus("current")
_Ospfv3AreaRowStatus_Type = RowStatus
_Ospfv3AreaRowStatus_Object = MibTableColumn
ospfv3AreaRowStatus = _Ospfv3AreaRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 9),
    _Ospfv3AreaRowStatus_Type()
)
ospfv3AreaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3AreaRowStatus.setStatus("current")
_Ospfv3AreaStubMetric_Type = BigMetric
_Ospfv3AreaStubMetric_Object = MibTableColumn
ospfv3AreaStubMetric = _Ospfv3AreaStubMetric_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 10),
    _Ospfv3AreaStubMetric_Type()
)
ospfv3AreaStubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3AreaStubMetric.setStatus("current")


class _Ospfv3AreaNssaTranslatorRole_Type(Integer32):
    """Custom type ospfv3AreaNssaTranslatorRole based on Integer32"""
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


_Ospfv3AreaNssaTranslatorRole_Type.__name__ = "Integer32"
_Ospfv3AreaNssaTranslatorRole_Object = MibTableColumn
ospfv3AreaNssaTranslatorRole = _Ospfv3AreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 11),
    _Ospfv3AreaNssaTranslatorRole_Type()
)
ospfv3AreaNssaTranslatorRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3AreaNssaTranslatorRole.setStatus("current")


class _Ospfv3AreaNssaTranslatorState_Type(Integer32):
    """Custom type ospfv3AreaNssaTranslatorState based on Integer32"""
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


_Ospfv3AreaNssaTranslatorState_Type.__name__ = "Integer32"
_Ospfv3AreaNssaTranslatorState_Object = MibTableColumn
ospfv3AreaNssaTranslatorState = _Ospfv3AreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 12),
    _Ospfv3AreaNssaTranslatorState_Type()
)
ospfv3AreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaNssaTranslatorState.setStatus("current")


class _Ospfv3AreaNssaTranslatorStabInterval_Type(Unsigned32):
    """Custom type ospfv3AreaNssaTranslatorStabInterval based on Unsigned32"""
    defaultValue = 40


_Ospfv3AreaNssaTranslatorStabInterval_Object = MibTableColumn
ospfv3AreaNssaTranslatorStabInterval = _Ospfv3AreaNssaTranslatorStabInterval_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 13),
    _Ospfv3AreaNssaTranslatorStabInterval_Type()
)
ospfv3AreaNssaTranslatorStabInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3AreaNssaTranslatorStabInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3AreaNssaTranslatorStabInterval.setUnits("seconds")
_Ospfv3AreaNssaTranslatorEvents_Type = Counter32
_Ospfv3AreaNssaTranslatorEvents_Object = MibTableColumn
ospfv3AreaNssaTranslatorEvents = _Ospfv3AreaNssaTranslatorEvents_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 14),
    _Ospfv3AreaNssaTranslatorEvents_Type()
)
ospfv3AreaNssaTranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaNssaTranslatorEvents.setStatus("current")


class _Ospfv3AreaStubMetricType_Type(Integer32):
    """Custom type ospfv3AreaStubMetricType based on Integer32"""
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
        *(("comparableCost", 2),
          ("nonComparable", 3),
          ("ospfv3Metric", 1))
    )


_Ospfv3AreaStubMetricType_Type.__name__ = "Integer32"
_Ospfv3AreaStubMetricType_Object = MibTableColumn
ospfv3AreaStubMetricType = _Ospfv3AreaStubMetricType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 15),
    _Ospfv3AreaStubMetricType_Type()
)
ospfv3AreaStubMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3AreaStubMetricType.setStatus("current")


class _Ospfv3AreaTEEnabled_Type(TruthValue):
    """Custom type ospfv3AreaTEEnabled based on TruthValue"""


_Ospfv3AreaTEEnabled_Object = MibTableColumn
ospfv3AreaTEEnabled = _Ospfv3AreaTEEnabled_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 2, 1, 16),
    _Ospfv3AreaTEEnabled_Type()
)
ospfv3AreaTEEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3AreaTEEnabled.setStatus("current")
_Ospfv3AsLsdbTable_Object = MibTable
ospfv3AsLsdbTable = _Ospfv3AsLsdbTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 3)
)
if mibBuilder.loadTexts:
    ospfv3AsLsdbTable.setStatus("current")
_Ospfv3AsLsdbEntry_Object = MibTableRow
ospfv3AsLsdbEntry = _Ospfv3AsLsdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 3, 1)
)
ospfv3AsLsdbEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3AsLsdbType"),
    (0, "OSPFV3-MIB", "ospfv3AsLsdbRouterId"),
    (0, "OSPFV3-MIB", "ospfv3AsLsdbLsid"),
)
if mibBuilder.loadTexts:
    ospfv3AsLsdbEntry.setStatus("current")


class _Ospfv3AsLsdbType_Type(Unsigned32):
    """Custom type ospfv3AsLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ospfv3AsLsdbType_Type.__name__ = "Unsigned32"
_Ospfv3AsLsdbType_Object = MibTableColumn
ospfv3AsLsdbType = _Ospfv3AsLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 3, 1, 1),
    _Ospfv3AsLsdbType_Type()
)
ospfv3AsLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AsLsdbType.setStatus("current")
_Ospfv3AsLsdbRouterId_Type = Ospfv3RouterIdTC
_Ospfv3AsLsdbRouterId_Object = MibTableColumn
ospfv3AsLsdbRouterId = _Ospfv3AsLsdbRouterId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 3, 1, 2),
    _Ospfv3AsLsdbRouterId_Type()
)
ospfv3AsLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AsLsdbRouterId.setStatus("current")
_Ospfv3AsLsdbLsid_Type = Ospfv3LsIdTC
_Ospfv3AsLsdbLsid_Object = MibTableColumn
ospfv3AsLsdbLsid = _Ospfv3AsLsdbLsid_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 3, 1, 3),
    _Ospfv3AsLsdbLsid_Type()
)
ospfv3AsLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AsLsdbLsid.setStatus("current")
_Ospfv3AsLsdbSequence_Type = Ospfv3LsaSequenceTC
_Ospfv3AsLsdbSequence_Object = MibTableColumn
ospfv3AsLsdbSequence = _Ospfv3AsLsdbSequence_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 3, 1, 4),
    _Ospfv3AsLsdbSequence_Type()
)
ospfv3AsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AsLsdbSequence.setStatus("current")
_Ospfv3AsLsdbAge_Type = Ospfv3LsaAgeTC
_Ospfv3AsLsdbAge_Object = MibTableColumn
ospfv3AsLsdbAge = _Ospfv3AsLsdbAge_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 3, 1, 5),
    _Ospfv3AsLsdbAge_Type()
)
ospfv3AsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AsLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3AsLsdbAge.setUnits("seconds")
_Ospfv3AsLsdbChecksum_Type = Integer32
_Ospfv3AsLsdbChecksum_Object = MibTableColumn
ospfv3AsLsdbChecksum = _Ospfv3AsLsdbChecksum_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 3, 1, 6),
    _Ospfv3AsLsdbChecksum_Type()
)
ospfv3AsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AsLsdbChecksum.setStatus("current")


class _Ospfv3AsLsdbAdvertisement_Type(OctetString):
    """Custom type ospfv3AsLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Ospfv3AsLsdbAdvertisement_Type.__name__ = "OctetString"
_Ospfv3AsLsdbAdvertisement_Object = MibTableColumn
ospfv3AsLsdbAdvertisement = _Ospfv3AsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 3, 1, 7),
    _Ospfv3AsLsdbAdvertisement_Type()
)
ospfv3AsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AsLsdbAdvertisement.setStatus("current")
_Ospfv3AsLsdbTypeKnown_Type = TruthValue
_Ospfv3AsLsdbTypeKnown_Object = MibTableColumn
ospfv3AsLsdbTypeKnown = _Ospfv3AsLsdbTypeKnown_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 3, 1, 8),
    _Ospfv3AsLsdbTypeKnown_Type()
)
ospfv3AsLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AsLsdbTypeKnown.setStatus("current")
_Ospfv3AreaLsdbTable_Object = MibTable
ospfv3AreaLsdbTable = _Ospfv3AreaLsdbTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 4)
)
if mibBuilder.loadTexts:
    ospfv3AreaLsdbTable.setStatus("current")
_Ospfv3AreaLsdbEntry_Object = MibTableRow
ospfv3AreaLsdbEntry = _Ospfv3AreaLsdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 4, 1)
)
ospfv3AreaLsdbEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbAreaId"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbType"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbRouterId"),
    (0, "OSPFV3-MIB", "ospfv3AreaLsdbLsid"),
)
if mibBuilder.loadTexts:
    ospfv3AreaLsdbEntry.setStatus("current")
_Ospfv3AreaLsdbAreaId_Type = Ospfv3AreaIdTC
_Ospfv3AreaLsdbAreaId_Object = MibTableColumn
ospfv3AreaLsdbAreaId = _Ospfv3AreaLsdbAreaId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 4, 1, 1),
    _Ospfv3AreaLsdbAreaId_Type()
)
ospfv3AreaLsdbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AreaLsdbAreaId.setStatus("current")


class _Ospfv3AreaLsdbType_Type(Unsigned32):
    """Custom type ospfv3AreaLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ospfv3AreaLsdbType_Type.__name__ = "Unsigned32"
_Ospfv3AreaLsdbType_Object = MibTableColumn
ospfv3AreaLsdbType = _Ospfv3AreaLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 4, 1, 2),
    _Ospfv3AreaLsdbType_Type()
)
ospfv3AreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AreaLsdbType.setStatus("current")
_Ospfv3AreaLsdbRouterId_Type = Ospfv3RouterIdTC
_Ospfv3AreaLsdbRouterId_Object = MibTableColumn
ospfv3AreaLsdbRouterId = _Ospfv3AreaLsdbRouterId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 4, 1, 3),
    _Ospfv3AreaLsdbRouterId_Type()
)
ospfv3AreaLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AreaLsdbRouterId.setStatus("current")
_Ospfv3AreaLsdbLsid_Type = Ospfv3LsIdTC
_Ospfv3AreaLsdbLsid_Object = MibTableColumn
ospfv3AreaLsdbLsid = _Ospfv3AreaLsdbLsid_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 4, 1, 4),
    _Ospfv3AreaLsdbLsid_Type()
)
ospfv3AreaLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AreaLsdbLsid.setStatus("current")
_Ospfv3AreaLsdbSequence_Type = Ospfv3LsaSequenceTC
_Ospfv3AreaLsdbSequence_Object = MibTableColumn
ospfv3AreaLsdbSequence = _Ospfv3AreaLsdbSequence_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 4, 1, 5),
    _Ospfv3AreaLsdbSequence_Type()
)
ospfv3AreaLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaLsdbSequence.setStatus("current")
_Ospfv3AreaLsdbAge_Type = Ospfv3LsaAgeTC
_Ospfv3AreaLsdbAge_Object = MibTableColumn
ospfv3AreaLsdbAge = _Ospfv3AreaLsdbAge_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 4, 1, 6),
    _Ospfv3AreaLsdbAge_Type()
)
ospfv3AreaLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3AreaLsdbAge.setUnits("seconds")
_Ospfv3AreaLsdbChecksum_Type = Integer32
_Ospfv3AreaLsdbChecksum_Object = MibTableColumn
ospfv3AreaLsdbChecksum = _Ospfv3AreaLsdbChecksum_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 4, 1, 7),
    _Ospfv3AreaLsdbChecksum_Type()
)
ospfv3AreaLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaLsdbChecksum.setStatus("current")


class _Ospfv3AreaLsdbAdvertisement_Type(OctetString):
    """Custom type ospfv3AreaLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Ospfv3AreaLsdbAdvertisement_Type.__name__ = "OctetString"
_Ospfv3AreaLsdbAdvertisement_Object = MibTableColumn
ospfv3AreaLsdbAdvertisement = _Ospfv3AreaLsdbAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 4, 1, 8),
    _Ospfv3AreaLsdbAdvertisement_Type()
)
ospfv3AreaLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaLsdbAdvertisement.setStatus("current")
_Ospfv3AreaLsdbTypeKnown_Type = TruthValue
_Ospfv3AreaLsdbTypeKnown_Object = MibTableColumn
ospfv3AreaLsdbTypeKnown = _Ospfv3AreaLsdbTypeKnown_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 4, 1, 9),
    _Ospfv3AreaLsdbTypeKnown_Type()
)
ospfv3AreaLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3AreaLsdbTypeKnown.setStatus("current")
_Ospfv3LinkLsdbTable_Object = MibTable
ospfv3LinkLsdbTable = _Ospfv3LinkLsdbTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5)
)
if mibBuilder.loadTexts:
    ospfv3LinkLsdbTable.setStatus("current")
_Ospfv3LinkLsdbEntry_Object = MibTableRow
ospfv3LinkLsdbEntry = _Ospfv3LinkLsdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5, 1)
)
ospfv3LinkLsdbEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3LinkLsdbIfIndex"),
    (0, "OSPFV3-MIB", "ospfv3LinkLsdbIfInstId"),
    (0, "OSPFV3-MIB", "ospfv3LinkLsdbType"),
    (0, "OSPFV3-MIB", "ospfv3LinkLsdbRouterId"),
    (0, "OSPFV3-MIB", "ospfv3LinkLsdbLsid"),
)
if mibBuilder.loadTexts:
    ospfv3LinkLsdbEntry.setStatus("current")
_Ospfv3LinkLsdbIfIndex_Type = InterfaceIndex
_Ospfv3LinkLsdbIfIndex_Object = MibTableColumn
ospfv3LinkLsdbIfIndex = _Ospfv3LinkLsdbIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5, 1, 1),
    _Ospfv3LinkLsdbIfIndex_Type()
)
ospfv3LinkLsdbIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3LinkLsdbIfIndex.setStatus("current")
_Ospfv3LinkLsdbIfInstId_Type = Ospfv3IfInstIdTC
_Ospfv3LinkLsdbIfInstId_Object = MibTableColumn
ospfv3LinkLsdbIfInstId = _Ospfv3LinkLsdbIfInstId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5, 1, 2),
    _Ospfv3LinkLsdbIfInstId_Type()
)
ospfv3LinkLsdbIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3LinkLsdbIfInstId.setStatus("current")


class _Ospfv3LinkLsdbType_Type(Unsigned32):
    """Custom type ospfv3LinkLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ospfv3LinkLsdbType_Type.__name__ = "Unsigned32"
_Ospfv3LinkLsdbType_Object = MibTableColumn
ospfv3LinkLsdbType = _Ospfv3LinkLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5, 1, 3),
    _Ospfv3LinkLsdbType_Type()
)
ospfv3LinkLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3LinkLsdbType.setStatus("current")
_Ospfv3LinkLsdbRouterId_Type = Ospfv3RouterIdTC
_Ospfv3LinkLsdbRouterId_Object = MibTableColumn
ospfv3LinkLsdbRouterId = _Ospfv3LinkLsdbRouterId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5, 1, 4),
    _Ospfv3LinkLsdbRouterId_Type()
)
ospfv3LinkLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3LinkLsdbRouterId.setStatus("current")
_Ospfv3LinkLsdbLsid_Type = Ospfv3LsIdTC
_Ospfv3LinkLsdbLsid_Object = MibTableColumn
ospfv3LinkLsdbLsid = _Ospfv3LinkLsdbLsid_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5, 1, 5),
    _Ospfv3LinkLsdbLsid_Type()
)
ospfv3LinkLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3LinkLsdbLsid.setStatus("current")
_Ospfv3LinkLsdbSequence_Type = Ospfv3LsaSequenceTC
_Ospfv3LinkLsdbSequence_Object = MibTableColumn
ospfv3LinkLsdbSequence = _Ospfv3LinkLsdbSequence_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5, 1, 6),
    _Ospfv3LinkLsdbSequence_Type()
)
ospfv3LinkLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3LinkLsdbSequence.setStatus("current")
_Ospfv3LinkLsdbAge_Type = Ospfv3LsaAgeTC
_Ospfv3LinkLsdbAge_Object = MibTableColumn
ospfv3LinkLsdbAge = _Ospfv3LinkLsdbAge_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5, 1, 7),
    _Ospfv3LinkLsdbAge_Type()
)
ospfv3LinkLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3LinkLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3LinkLsdbAge.setUnits("seconds")
_Ospfv3LinkLsdbChecksum_Type = Integer32
_Ospfv3LinkLsdbChecksum_Object = MibTableColumn
ospfv3LinkLsdbChecksum = _Ospfv3LinkLsdbChecksum_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5, 1, 8),
    _Ospfv3LinkLsdbChecksum_Type()
)
ospfv3LinkLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3LinkLsdbChecksum.setStatus("current")


class _Ospfv3LinkLsdbAdvertisement_Type(OctetString):
    """Custom type ospfv3LinkLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Ospfv3LinkLsdbAdvertisement_Type.__name__ = "OctetString"
_Ospfv3LinkLsdbAdvertisement_Object = MibTableColumn
ospfv3LinkLsdbAdvertisement = _Ospfv3LinkLsdbAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5, 1, 9),
    _Ospfv3LinkLsdbAdvertisement_Type()
)
ospfv3LinkLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3LinkLsdbAdvertisement.setStatus("current")
_Ospfv3LinkLsdbTypeKnown_Type = TruthValue
_Ospfv3LinkLsdbTypeKnown_Object = MibTableColumn
ospfv3LinkLsdbTypeKnown = _Ospfv3LinkLsdbTypeKnown_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 5, 1, 10),
    _Ospfv3LinkLsdbTypeKnown_Type()
)
ospfv3LinkLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3LinkLsdbTypeKnown.setStatus("current")
_Ospfv3HostTable_Object = MibTable
ospfv3HostTable = _Ospfv3HostTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 6)
)
if mibBuilder.loadTexts:
    ospfv3HostTable.setStatus("current")
_Ospfv3HostEntry_Object = MibTableRow
ospfv3HostEntry = _Ospfv3HostEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 6, 1)
)
ospfv3HostEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3HostAddressType"),
    (0, "OSPFV3-MIB", "ospfv3HostAddress"),
)
if mibBuilder.loadTexts:
    ospfv3HostEntry.setStatus("current")
_Ospfv3HostAddressType_Type = InetAddressType
_Ospfv3HostAddressType_Object = MibTableColumn
ospfv3HostAddressType = _Ospfv3HostAddressType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 6, 1, 1),
    _Ospfv3HostAddressType_Type()
)
ospfv3HostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3HostAddressType.setStatus("current")
_Ospfv3HostAddress_Type = InetAddress
_Ospfv3HostAddress_Object = MibTableColumn
ospfv3HostAddress = _Ospfv3HostAddress_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 6, 1, 2),
    _Ospfv3HostAddress_Type()
)
ospfv3HostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3HostAddress.setStatus("current")
_Ospfv3HostMetric_Type = Metric
_Ospfv3HostMetric_Object = MibTableColumn
ospfv3HostMetric = _Ospfv3HostMetric_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 6, 1, 3),
    _Ospfv3HostMetric_Type()
)
ospfv3HostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3HostMetric.setStatus("current")
_Ospfv3HostRowStatus_Type = RowStatus
_Ospfv3HostRowStatus_Object = MibTableColumn
ospfv3HostRowStatus = _Ospfv3HostRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 6, 1, 4),
    _Ospfv3HostRowStatus_Type()
)
ospfv3HostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3HostRowStatus.setStatus("current")
_Ospfv3HostAreaID_Type = Ospfv3AreaIdTC
_Ospfv3HostAreaID_Object = MibTableColumn
ospfv3HostAreaID = _Ospfv3HostAreaID_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 6, 1, 5),
    _Ospfv3HostAreaID_Type()
)
ospfv3HostAreaID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3HostAreaID.setStatus("current")
_Ospfv3IfTable_Object = MibTable
ospfv3IfTable = _Ospfv3IfTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7)
)
if mibBuilder.loadTexts:
    ospfv3IfTable.setStatus("current")
_Ospfv3IfEntry_Object = MibTableRow
ospfv3IfEntry = _Ospfv3IfEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1)
)
ospfv3IfEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3IfIndex"),
    (0, "OSPFV3-MIB", "ospfv3IfInstId"),
)
if mibBuilder.loadTexts:
    ospfv3IfEntry.setStatus("current")
_Ospfv3IfIndex_Type = InterfaceIndex
_Ospfv3IfIndex_Object = MibTableColumn
ospfv3IfIndex = _Ospfv3IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 1),
    _Ospfv3IfIndex_Type()
)
ospfv3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3IfIndex.setStatus("current")
_Ospfv3IfInstId_Type = Ospfv3IfInstIdTC
_Ospfv3IfInstId_Object = MibTableColumn
ospfv3IfInstId = _Ospfv3IfInstId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 2),
    _Ospfv3IfInstId_Type()
)
ospfv3IfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3IfInstId.setStatus("current")


class _Ospfv3IfAreaId_Type(Ospfv3AreaIdTC):
    """Custom type ospfv3IfAreaId based on Ospfv3AreaIdTC"""
    defaultValue = 0


_Ospfv3IfAreaId_Object = MibTableColumn
ospfv3IfAreaId = _Ospfv3IfAreaId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 3),
    _Ospfv3IfAreaId_Type()
)
ospfv3IfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfAreaId.setStatus("current")


class _Ospfv3IfType_Type(Integer32):
    """Custom type ospfv3IfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToMultipoint", 5),
          ("pointToPoint", 3))
    )


_Ospfv3IfType_Type.__name__ = "Integer32"
_Ospfv3IfType_Object = MibTableColumn
ospfv3IfType = _Ospfv3IfType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 4),
    _Ospfv3IfType_Type()
)
ospfv3IfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfType.setStatus("current")


class _Ospfv3IfAdminStatus_Type(Status):
    """Custom type ospfv3IfAdminStatus based on Status"""


_Ospfv3IfAdminStatus_Object = MibTableColumn
ospfv3IfAdminStatus = _Ospfv3IfAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 5),
    _Ospfv3IfAdminStatus_Type()
)
ospfv3IfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfAdminStatus.setStatus("current")


class _Ospfv3IfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type ospfv3IfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_Ospfv3IfRtrPriority_Object = MibTableColumn
ospfv3IfRtrPriority = _Ospfv3IfRtrPriority_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 6),
    _Ospfv3IfRtrPriority_Type()
)
ospfv3IfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfRtrPriority.setStatus("current")


class _Ospfv3IfTransitDelay_Type(Ospfv3UpToRefreshIntervalTC):
    """Custom type ospfv3IfTransitDelay based on Ospfv3UpToRefreshIntervalTC"""
    defaultValue = 1


_Ospfv3IfTransitDelay_Object = MibTableColumn
ospfv3IfTransitDelay = _Ospfv3IfTransitDelay_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 7),
    _Ospfv3IfTransitDelay_Type()
)
ospfv3IfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3IfTransitDelay.setUnits("seconds")


class _Ospfv3IfRetransInterval_Type(Ospfv3UpToRefreshIntervalTC):
    """Custom type ospfv3IfRetransInterval based on Ospfv3UpToRefreshIntervalTC"""
    defaultValue = 5


_Ospfv3IfRetransInterval_Object = MibTableColumn
ospfv3IfRetransInterval = _Ospfv3IfRetransInterval_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 8),
    _Ospfv3IfRetransInterval_Type()
)
ospfv3IfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3IfRetransInterval.setUnits("seconds")


class _Ospfv3IfHelloInterval_Type(HelloRange):
    """Custom type ospfv3IfHelloInterval based on HelloRange"""
    defaultValue = 10


_Ospfv3IfHelloInterval_Object = MibTableColumn
ospfv3IfHelloInterval = _Ospfv3IfHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 9),
    _Ospfv3IfHelloInterval_Type()
)
ospfv3IfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3IfHelloInterval.setUnits("seconds")


class _Ospfv3IfRtrDeadInterval_Type(Ospfv3DeadIntervalRangeTC):
    """Custom type ospfv3IfRtrDeadInterval based on Ospfv3DeadIntervalRangeTC"""
    defaultValue = 40


_Ospfv3IfRtrDeadInterval_Object = MibTableColumn
ospfv3IfRtrDeadInterval = _Ospfv3IfRtrDeadInterval_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 10),
    _Ospfv3IfRtrDeadInterval_Type()
)
ospfv3IfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3IfRtrDeadInterval.setUnits("seconds")


class _Ospfv3IfPollInterval_Type(Unsigned32):
    """Custom type ospfv3IfPollInterval based on Unsigned32"""
    defaultValue = 120


_Ospfv3IfPollInterval_Object = MibTableColumn
ospfv3IfPollInterval = _Ospfv3IfPollInterval_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 11),
    _Ospfv3IfPollInterval_Type()
)
ospfv3IfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3IfPollInterval.setUnits("seconds")


class _Ospfv3IfState_Type(Integer32):
    """Custom type ospfv3IfState based on Integer32"""
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
        *(("backupDesignatedRouter", 6),
          ("designatedRouter", 5),
          ("down", 1),
          ("loopback", 2),
          ("otherDesignatedRouter", 7),
          ("pointToPoint", 4),
          ("standby", 8),
          ("waiting", 3))
    )


_Ospfv3IfState_Type.__name__ = "Integer32"
_Ospfv3IfState_Object = MibTableColumn
ospfv3IfState = _Ospfv3IfState_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 12),
    _Ospfv3IfState_Type()
)
ospfv3IfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3IfState.setStatus("current")
_Ospfv3IfDesignatedRouter_Type = Ospfv3RouterIdTC
_Ospfv3IfDesignatedRouter_Object = MibTableColumn
ospfv3IfDesignatedRouter = _Ospfv3IfDesignatedRouter_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 13),
    _Ospfv3IfDesignatedRouter_Type()
)
ospfv3IfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3IfDesignatedRouter.setStatus("current")
_Ospfv3IfBackupDesignatedRouter_Type = Ospfv3RouterIdTC
_Ospfv3IfBackupDesignatedRouter_Object = MibTableColumn
ospfv3IfBackupDesignatedRouter = _Ospfv3IfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 14),
    _Ospfv3IfBackupDesignatedRouter_Type()
)
ospfv3IfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3IfBackupDesignatedRouter.setStatus("current")
_Ospfv3IfEvents_Type = Counter32
_Ospfv3IfEvents_Object = MibTableColumn
ospfv3IfEvents = _Ospfv3IfEvents_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 15),
    _Ospfv3IfEvents_Type()
)
ospfv3IfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3IfEvents.setStatus("current")
_Ospfv3IfRowStatus_Type = RowStatus
_Ospfv3IfRowStatus_Object = MibTableColumn
ospfv3IfRowStatus = _Ospfv3IfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 16),
    _Ospfv3IfRowStatus_Type()
)
ospfv3IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfRowStatus.setStatus("current")


class _Ospfv3IfDemand_Type(TruthValue):
    """Custom type ospfv3IfDemand based on TruthValue"""


_Ospfv3IfDemand_Object = MibTableColumn
ospfv3IfDemand = _Ospfv3IfDemand_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 17),
    _Ospfv3IfDemand_Type()
)
ospfv3IfDemand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfDemand.setStatus("current")
_Ospfv3IfMetricValue_Type = Metric
_Ospfv3IfMetricValue_Object = MibTableColumn
ospfv3IfMetricValue = _Ospfv3IfMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 18),
    _Ospfv3IfMetricValue_Type()
)
ospfv3IfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfMetricValue.setStatus("current")
_Ospfv3IfLinkScopeLsaCount_Type = Gauge32
_Ospfv3IfLinkScopeLsaCount_Object = MibTableColumn
ospfv3IfLinkScopeLsaCount = _Ospfv3IfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 19),
    _Ospfv3IfLinkScopeLsaCount_Type()
)
ospfv3IfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3IfLinkScopeLsaCount.setStatus("current")
_Ospfv3IfLinkLsaCksumSum_Type = Unsigned32
_Ospfv3IfLinkLsaCksumSum_Object = MibTableColumn
ospfv3IfLinkLsaCksumSum = _Ospfv3IfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 20),
    _Ospfv3IfLinkLsaCksumSum_Type()
)
ospfv3IfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3IfLinkLsaCksumSum.setStatus("current")


class _Ospfv3IfDemandNbrProbe_Type(TruthValue):
    """Custom type ospfv3IfDemandNbrProbe based on TruthValue"""


_Ospfv3IfDemandNbrProbe_Object = MibTableColumn
ospfv3IfDemandNbrProbe = _Ospfv3IfDemandNbrProbe_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 21),
    _Ospfv3IfDemandNbrProbe_Type()
)
ospfv3IfDemandNbrProbe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfDemandNbrProbe.setStatus("current")


class _Ospfv3IfDemandNbrProbeRetransLimit_Type(Unsigned32):
    """Custom type ospfv3IfDemandNbrProbeRetransLimit based on Unsigned32"""
    defaultValue = 10


_Ospfv3IfDemandNbrProbeRetransLimit_Object = MibTableColumn
ospfv3IfDemandNbrProbeRetransLimit = _Ospfv3IfDemandNbrProbeRetransLimit_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 22),
    _Ospfv3IfDemandNbrProbeRetransLimit_Type()
)
ospfv3IfDemandNbrProbeRetransLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfDemandNbrProbeRetransLimit.setStatus("current")


class _Ospfv3IfDemandNbrProbeInterval_Type(Unsigned32):
    """Custom type ospfv3IfDemandNbrProbeInterval based on Unsigned32"""
    defaultValue = 120


_Ospfv3IfDemandNbrProbeInterval_Object = MibTableColumn
ospfv3IfDemandNbrProbeInterval = _Ospfv3IfDemandNbrProbeInterval_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 23),
    _Ospfv3IfDemandNbrProbeInterval_Type()
)
ospfv3IfDemandNbrProbeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfDemandNbrProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3IfDemandNbrProbeInterval.setUnits("seconds")


class _Ospfv3IfTEDisabled_Type(TruthValue):
    """Custom type ospfv3IfTEDisabled based on TruthValue"""


_Ospfv3IfTEDisabled_Object = MibTableColumn
ospfv3IfTEDisabled = _Ospfv3IfTEDisabled_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 24),
    _Ospfv3IfTEDisabled_Type()
)
ospfv3IfTEDisabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfTEDisabled.setStatus("current")


class _Ospfv3IfLinkLSASuppression_Type(TruthValue):
    """Custom type ospfv3IfLinkLSASuppression based on TruthValue"""


_Ospfv3IfLinkLSASuppression_Object = MibTableColumn
ospfv3IfLinkLSASuppression = _Ospfv3IfLinkLSASuppression_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 7, 1, 25),
    _Ospfv3IfLinkLSASuppression_Type()
)
ospfv3IfLinkLSASuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3IfLinkLSASuppression.setStatus("current")
_Ospfv3VirtIfTable_Object = MibTable
ospfv3VirtIfTable = _Ospfv3VirtIfTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8)
)
if mibBuilder.loadTexts:
    ospfv3VirtIfTable.setStatus("current")
_Ospfv3VirtIfEntry_Object = MibTableRow
ospfv3VirtIfEntry = _Ospfv3VirtIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1)
)
ospfv3VirtIfEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3VirtIfAreaId"),
    (0, "OSPFV3-MIB", "ospfv3VirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    ospfv3VirtIfEntry.setStatus("current")
_Ospfv3VirtIfAreaId_Type = Ospfv3AreaIdTC
_Ospfv3VirtIfAreaId_Object = MibTableColumn
ospfv3VirtIfAreaId = _Ospfv3VirtIfAreaId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 1),
    _Ospfv3VirtIfAreaId_Type()
)
ospfv3VirtIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3VirtIfAreaId.setStatus("current")
_Ospfv3VirtIfNeighbor_Type = Ospfv3RouterIdTC
_Ospfv3VirtIfNeighbor_Object = MibTableColumn
ospfv3VirtIfNeighbor = _Ospfv3VirtIfNeighbor_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 2),
    _Ospfv3VirtIfNeighbor_Type()
)
ospfv3VirtIfNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3VirtIfNeighbor.setStatus("current")
_Ospfv3VirtIfIndex_Type = InterfaceIndex
_Ospfv3VirtIfIndex_Object = MibTableColumn
ospfv3VirtIfIndex = _Ospfv3VirtIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 3),
    _Ospfv3VirtIfIndex_Type()
)
ospfv3VirtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtIfIndex.setStatus("current")
_Ospfv3VirtIfInstId_Type = Ospfv3IfInstIdTC
_Ospfv3VirtIfInstId_Object = MibTableColumn
ospfv3VirtIfInstId = _Ospfv3VirtIfInstId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 4),
    _Ospfv3VirtIfInstId_Type()
)
ospfv3VirtIfInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtIfInstId.setStatus("current")


class _Ospfv3VirtIfTransitDelay_Type(Ospfv3UpToRefreshIntervalTC):
    """Custom type ospfv3VirtIfTransitDelay based on Ospfv3UpToRefreshIntervalTC"""
    defaultValue = 1


_Ospfv3VirtIfTransitDelay_Object = MibTableColumn
ospfv3VirtIfTransitDelay = _Ospfv3VirtIfTransitDelay_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 5),
    _Ospfv3VirtIfTransitDelay_Type()
)
ospfv3VirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3VirtIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3VirtIfTransitDelay.setUnits("seconds")


class _Ospfv3VirtIfRetransInterval_Type(Ospfv3UpToRefreshIntervalTC):
    """Custom type ospfv3VirtIfRetransInterval based on Ospfv3UpToRefreshIntervalTC"""
    defaultValue = 5


_Ospfv3VirtIfRetransInterval_Object = MibTableColumn
ospfv3VirtIfRetransInterval = _Ospfv3VirtIfRetransInterval_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 6),
    _Ospfv3VirtIfRetransInterval_Type()
)
ospfv3VirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3VirtIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3VirtIfRetransInterval.setUnits("seconds")


class _Ospfv3VirtIfHelloInterval_Type(HelloRange):
    """Custom type ospfv3VirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_Ospfv3VirtIfHelloInterval_Object = MibTableColumn
ospfv3VirtIfHelloInterval = _Ospfv3VirtIfHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 7),
    _Ospfv3VirtIfHelloInterval_Type()
)
ospfv3VirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3VirtIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3VirtIfHelloInterval.setUnits("seconds")


class _Ospfv3VirtIfRtrDeadInterval_Type(Ospfv3DeadIntervalRangeTC):
    """Custom type ospfv3VirtIfRtrDeadInterval based on Ospfv3DeadIntervalRangeTC"""
    defaultValue = 60


_Ospfv3VirtIfRtrDeadInterval_Object = MibTableColumn
ospfv3VirtIfRtrDeadInterval = _Ospfv3VirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 8),
    _Ospfv3VirtIfRtrDeadInterval_Type()
)
ospfv3VirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3VirtIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3VirtIfRtrDeadInterval.setUnits("seconds")


class _Ospfv3VirtIfState_Type(Integer32):
    """Custom type ospfv3VirtIfState based on Integer32"""
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


_Ospfv3VirtIfState_Type.__name__ = "Integer32"
_Ospfv3VirtIfState_Object = MibTableColumn
ospfv3VirtIfState = _Ospfv3VirtIfState_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 9),
    _Ospfv3VirtIfState_Type()
)
ospfv3VirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtIfState.setStatus("current")
_Ospfv3VirtIfEvents_Type = Counter32
_Ospfv3VirtIfEvents_Object = MibTableColumn
ospfv3VirtIfEvents = _Ospfv3VirtIfEvents_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 10),
    _Ospfv3VirtIfEvents_Type()
)
ospfv3VirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtIfEvents.setStatus("current")
_Ospfv3VirtIfRowStatus_Type = RowStatus
_Ospfv3VirtIfRowStatus_Object = MibTableColumn
ospfv3VirtIfRowStatus = _Ospfv3VirtIfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 11),
    _Ospfv3VirtIfRowStatus_Type()
)
ospfv3VirtIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3VirtIfRowStatus.setStatus("current")
_Ospfv3VirtIfLinkScopeLsaCount_Type = Gauge32
_Ospfv3VirtIfLinkScopeLsaCount_Object = MibTableColumn
ospfv3VirtIfLinkScopeLsaCount = _Ospfv3VirtIfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 12),
    _Ospfv3VirtIfLinkScopeLsaCount_Type()
)
ospfv3VirtIfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtIfLinkScopeLsaCount.setStatus("current")
_Ospfv3VirtIfLinkLsaCksumSum_Type = Unsigned32
_Ospfv3VirtIfLinkLsaCksumSum_Object = MibTableColumn
ospfv3VirtIfLinkLsaCksumSum = _Ospfv3VirtIfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 8, 1, 13),
    _Ospfv3VirtIfLinkLsaCksumSum_Type()
)
ospfv3VirtIfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtIfLinkLsaCksumSum.setStatus("current")
_Ospfv3NbrTable_Object = MibTable
ospfv3NbrTable = _Ospfv3NbrTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9)
)
if mibBuilder.loadTexts:
    ospfv3NbrTable.setStatus("current")
_Ospfv3NbrEntry_Object = MibTableRow
ospfv3NbrEntry = _Ospfv3NbrEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1)
)
ospfv3NbrEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3NbrIfIndex"),
    (0, "OSPFV3-MIB", "ospfv3NbrIfInstId"),
    (0, "OSPFV3-MIB", "ospfv3NbrRtrId"),
)
if mibBuilder.loadTexts:
    ospfv3NbrEntry.setStatus("current")
_Ospfv3NbrIfIndex_Type = InterfaceIndex
_Ospfv3NbrIfIndex_Object = MibTableColumn
ospfv3NbrIfIndex = _Ospfv3NbrIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 1),
    _Ospfv3NbrIfIndex_Type()
)
ospfv3NbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3NbrIfIndex.setStatus("current")
_Ospfv3NbrIfInstId_Type = Ospfv3IfInstIdTC
_Ospfv3NbrIfInstId_Object = MibTableColumn
ospfv3NbrIfInstId = _Ospfv3NbrIfInstId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 2),
    _Ospfv3NbrIfInstId_Type()
)
ospfv3NbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3NbrIfInstId.setStatus("current")
_Ospfv3NbrRtrId_Type = Ospfv3RouterIdTC
_Ospfv3NbrRtrId_Object = MibTableColumn
ospfv3NbrRtrId = _Ospfv3NbrRtrId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 3),
    _Ospfv3NbrRtrId_Type()
)
ospfv3NbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3NbrRtrId.setStatus("current")
_Ospfv3NbrAddressType_Type = InetAddressType
_Ospfv3NbrAddressType_Object = MibTableColumn
ospfv3NbrAddressType = _Ospfv3NbrAddressType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 4),
    _Ospfv3NbrAddressType_Type()
)
ospfv3NbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrAddressType.setStatus("current")
_Ospfv3NbrAddress_Type = InetAddress
_Ospfv3NbrAddress_Object = MibTableColumn
ospfv3NbrAddress = _Ospfv3NbrAddress_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 5),
    _Ospfv3NbrAddress_Type()
)
ospfv3NbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrAddress.setStatus("current")
_Ospfv3NbrOptions_Type = Integer32
_Ospfv3NbrOptions_Object = MibTableColumn
ospfv3NbrOptions = _Ospfv3NbrOptions_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 6),
    _Ospfv3NbrOptions_Type()
)
ospfv3NbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrOptions.setStatus("current")
_Ospfv3NbrPriority_Type = DesignatedRouterPriority
_Ospfv3NbrPriority_Object = MibTableColumn
ospfv3NbrPriority = _Ospfv3NbrPriority_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 7),
    _Ospfv3NbrPriority_Type()
)
ospfv3NbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrPriority.setStatus("current")


class _Ospfv3NbrState_Type(Integer32):
    """Custom type ospfv3NbrState based on Integer32"""
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


_Ospfv3NbrState_Type.__name__ = "Integer32"
_Ospfv3NbrState_Object = MibTableColumn
ospfv3NbrState = _Ospfv3NbrState_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 8),
    _Ospfv3NbrState_Type()
)
ospfv3NbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrState.setStatus("current")
_Ospfv3NbrEvents_Type = Counter32
_Ospfv3NbrEvents_Object = MibTableColumn
ospfv3NbrEvents = _Ospfv3NbrEvents_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 9),
    _Ospfv3NbrEvents_Type()
)
ospfv3NbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrEvents.setStatus("current")
_Ospfv3NbrLsRetransQLen_Type = Gauge32
_Ospfv3NbrLsRetransQLen_Object = MibTableColumn
ospfv3NbrLsRetransQLen = _Ospfv3NbrLsRetransQLen_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 10),
    _Ospfv3NbrLsRetransQLen_Type()
)
ospfv3NbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrLsRetransQLen.setStatus("current")
_Ospfv3NbrHelloSuppressed_Type = TruthValue
_Ospfv3NbrHelloSuppressed_Object = MibTableColumn
ospfv3NbrHelloSuppressed = _Ospfv3NbrHelloSuppressed_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 11),
    _Ospfv3NbrHelloSuppressed_Type()
)
ospfv3NbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrHelloSuppressed.setStatus("current")
_Ospfv3NbrIfId_Type = InterfaceIndex
_Ospfv3NbrIfId_Object = MibTableColumn
ospfv3NbrIfId = _Ospfv3NbrIfId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 12),
    _Ospfv3NbrIfId_Type()
)
ospfv3NbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrIfId.setStatus("current")


class _Ospfv3NbrRestartHelperStatus_Type(Integer32):
    """Custom type ospfv3NbrRestartHelperStatus based on Integer32"""
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


_Ospfv3NbrRestartHelperStatus_Type.__name__ = "Integer32"
_Ospfv3NbrRestartHelperStatus_Object = MibTableColumn
ospfv3NbrRestartHelperStatus = _Ospfv3NbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 13),
    _Ospfv3NbrRestartHelperStatus_Type()
)
ospfv3NbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrRestartHelperStatus.setStatus("current")
_Ospfv3NbrRestartHelperAge_Type = Ospfv3UpToRefreshIntervalTC
_Ospfv3NbrRestartHelperAge_Object = MibTableColumn
ospfv3NbrRestartHelperAge = _Ospfv3NbrRestartHelperAge_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 14),
    _Ospfv3NbrRestartHelperAge_Type()
)
ospfv3NbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3NbrRestartHelperAge.setUnits("seconds")


class _Ospfv3NbrRestartHelperExitReason_Type(Integer32):
    """Custom type ospfv3NbrRestartHelperExitReason based on Integer32"""
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


_Ospfv3NbrRestartHelperExitReason_Type.__name__ = "Integer32"
_Ospfv3NbrRestartHelperExitReason_Object = MibTableColumn
ospfv3NbrRestartHelperExitReason = _Ospfv3NbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 9, 1, 15),
    _Ospfv3NbrRestartHelperExitReason_Type()
)
ospfv3NbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3NbrRestartHelperExitReason.setStatus("current")
_Ospfv3CfgNbrTable_Object = MibTable
ospfv3CfgNbrTable = _Ospfv3CfgNbrTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 10)
)
if mibBuilder.loadTexts:
    ospfv3CfgNbrTable.setStatus("current")
_Ospfv3CfgNbrEntry_Object = MibTableRow
ospfv3CfgNbrEntry = _Ospfv3CfgNbrEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 10, 1)
)
ospfv3CfgNbrEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3CfgNbrIfIndex"),
    (0, "OSPFV3-MIB", "ospfv3CfgNbrIfInstId"),
    (0, "OSPFV3-MIB", "ospfv3CfgNbrAddressType"),
    (0, "OSPFV3-MIB", "ospfv3CfgNbrAddress"),
)
if mibBuilder.loadTexts:
    ospfv3CfgNbrEntry.setStatus("current")
_Ospfv3CfgNbrIfIndex_Type = InterfaceIndex
_Ospfv3CfgNbrIfIndex_Object = MibTableColumn
ospfv3CfgNbrIfIndex = _Ospfv3CfgNbrIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 10, 1, 1),
    _Ospfv3CfgNbrIfIndex_Type()
)
ospfv3CfgNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3CfgNbrIfIndex.setStatus("current")
_Ospfv3CfgNbrIfInstId_Type = Ospfv3IfInstIdTC
_Ospfv3CfgNbrIfInstId_Object = MibTableColumn
ospfv3CfgNbrIfInstId = _Ospfv3CfgNbrIfInstId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 10, 1, 2),
    _Ospfv3CfgNbrIfInstId_Type()
)
ospfv3CfgNbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3CfgNbrIfInstId.setStatus("current")
_Ospfv3CfgNbrAddressType_Type = InetAddressType
_Ospfv3CfgNbrAddressType_Object = MibTableColumn
ospfv3CfgNbrAddressType = _Ospfv3CfgNbrAddressType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 10, 1, 3),
    _Ospfv3CfgNbrAddressType_Type()
)
ospfv3CfgNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3CfgNbrAddressType.setStatus("current")
_Ospfv3CfgNbrAddress_Type = InetAddress
_Ospfv3CfgNbrAddress_Object = MibTableColumn
ospfv3CfgNbrAddress = _Ospfv3CfgNbrAddress_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 10, 1, 4),
    _Ospfv3CfgNbrAddress_Type()
)
ospfv3CfgNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3CfgNbrAddress.setStatus("current")


class _Ospfv3CfgNbrPriority_Type(DesignatedRouterPriority):
    """Custom type ospfv3CfgNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_Ospfv3CfgNbrPriority_Object = MibTableColumn
ospfv3CfgNbrPriority = _Ospfv3CfgNbrPriority_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 10, 1, 5),
    _Ospfv3CfgNbrPriority_Type()
)
ospfv3CfgNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3CfgNbrPriority.setStatus("current")
_Ospfv3CfgNbrRowStatus_Type = RowStatus
_Ospfv3CfgNbrRowStatus_Object = MibTableColumn
ospfv3CfgNbrRowStatus = _Ospfv3CfgNbrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 10, 1, 6),
    _Ospfv3CfgNbrRowStatus_Type()
)
ospfv3CfgNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3CfgNbrRowStatus.setStatus("current")
_Ospfv3VirtNbrTable_Object = MibTable
ospfv3VirtNbrTable = _Ospfv3VirtNbrTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11)
)
if mibBuilder.loadTexts:
    ospfv3VirtNbrTable.setStatus("current")
_Ospfv3VirtNbrEntry_Object = MibTableRow
ospfv3VirtNbrEntry = _Ospfv3VirtNbrEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1)
)
ospfv3VirtNbrEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3VirtNbrArea"),
    (0, "OSPFV3-MIB", "ospfv3VirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    ospfv3VirtNbrEntry.setStatus("current")
_Ospfv3VirtNbrArea_Type = Ospfv3AreaIdTC
_Ospfv3VirtNbrArea_Object = MibTableColumn
ospfv3VirtNbrArea = _Ospfv3VirtNbrArea_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 1),
    _Ospfv3VirtNbrArea_Type()
)
ospfv3VirtNbrArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3VirtNbrArea.setStatus("current")
_Ospfv3VirtNbrRtrId_Type = Ospfv3RouterIdTC
_Ospfv3VirtNbrRtrId_Object = MibTableColumn
ospfv3VirtNbrRtrId = _Ospfv3VirtNbrRtrId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 2),
    _Ospfv3VirtNbrRtrId_Type()
)
ospfv3VirtNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3VirtNbrRtrId.setStatus("current")
_Ospfv3VirtNbrIfIndex_Type = InterfaceIndex
_Ospfv3VirtNbrIfIndex_Object = MibTableColumn
ospfv3VirtNbrIfIndex = _Ospfv3VirtNbrIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 3),
    _Ospfv3VirtNbrIfIndex_Type()
)
ospfv3VirtNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrIfIndex.setStatus("current")
_Ospfv3VirtNbrIfInstId_Type = Ospfv3IfInstIdTC
_Ospfv3VirtNbrIfInstId_Object = MibTableColumn
ospfv3VirtNbrIfInstId = _Ospfv3VirtNbrIfInstId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 4),
    _Ospfv3VirtNbrIfInstId_Type()
)
ospfv3VirtNbrIfInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrIfInstId.setStatus("current")
_Ospfv3VirtNbrAddressType_Type = InetAddressType
_Ospfv3VirtNbrAddressType_Object = MibTableColumn
ospfv3VirtNbrAddressType = _Ospfv3VirtNbrAddressType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 5),
    _Ospfv3VirtNbrAddressType_Type()
)
ospfv3VirtNbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrAddressType.setStatus("current")
_Ospfv3VirtNbrAddress_Type = InetAddress
_Ospfv3VirtNbrAddress_Object = MibTableColumn
ospfv3VirtNbrAddress = _Ospfv3VirtNbrAddress_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 6),
    _Ospfv3VirtNbrAddress_Type()
)
ospfv3VirtNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrAddress.setStatus("current")
_Ospfv3VirtNbrOptions_Type = Integer32
_Ospfv3VirtNbrOptions_Object = MibTableColumn
ospfv3VirtNbrOptions = _Ospfv3VirtNbrOptions_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 7),
    _Ospfv3VirtNbrOptions_Type()
)
ospfv3VirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrOptions.setStatus("current")


class _Ospfv3VirtNbrState_Type(Integer32):
    """Custom type ospfv3VirtNbrState based on Integer32"""
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


_Ospfv3VirtNbrState_Type.__name__ = "Integer32"
_Ospfv3VirtNbrState_Object = MibTableColumn
ospfv3VirtNbrState = _Ospfv3VirtNbrState_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 8),
    _Ospfv3VirtNbrState_Type()
)
ospfv3VirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrState.setStatus("current")
_Ospfv3VirtNbrEvents_Type = Counter32
_Ospfv3VirtNbrEvents_Object = MibTableColumn
ospfv3VirtNbrEvents = _Ospfv3VirtNbrEvents_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 9),
    _Ospfv3VirtNbrEvents_Type()
)
ospfv3VirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrEvents.setStatus("current")
_Ospfv3VirtNbrLsRetransQLen_Type = Gauge32
_Ospfv3VirtNbrLsRetransQLen_Object = MibTableColumn
ospfv3VirtNbrLsRetransQLen = _Ospfv3VirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 10),
    _Ospfv3VirtNbrLsRetransQLen_Type()
)
ospfv3VirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrLsRetransQLen.setStatus("current")
_Ospfv3VirtNbrHelloSuppressed_Type = TruthValue
_Ospfv3VirtNbrHelloSuppressed_Object = MibTableColumn
ospfv3VirtNbrHelloSuppressed = _Ospfv3VirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 11),
    _Ospfv3VirtNbrHelloSuppressed_Type()
)
ospfv3VirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrHelloSuppressed.setStatus("current")
_Ospfv3VirtNbrIfId_Type = InterfaceIndex
_Ospfv3VirtNbrIfId_Object = MibTableColumn
ospfv3VirtNbrIfId = _Ospfv3VirtNbrIfId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 12),
    _Ospfv3VirtNbrIfId_Type()
)
ospfv3VirtNbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrIfId.setStatus("current")


class _Ospfv3VirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type ospfv3VirtNbrRestartHelperStatus based on Integer32"""
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


_Ospfv3VirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_Ospfv3VirtNbrRestartHelperStatus_Object = MibTableColumn
ospfv3VirtNbrRestartHelperStatus = _Ospfv3VirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 13),
    _Ospfv3VirtNbrRestartHelperStatus_Type()
)
ospfv3VirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrRestartHelperStatus.setStatus("current")
_Ospfv3VirtNbrRestartHelperAge_Type = Ospfv3UpToRefreshIntervalTC
_Ospfv3VirtNbrRestartHelperAge_Object = MibTableColumn
ospfv3VirtNbrRestartHelperAge = _Ospfv3VirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 14),
    _Ospfv3VirtNbrRestartHelperAge_Type()
)
ospfv3VirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3VirtNbrRestartHelperAge.setUnits("seconds")


class _Ospfv3VirtNbrRestartHelperExitReason_Type(Integer32):
    """Custom type ospfv3VirtNbrRestartHelperExitReason based on Integer32"""
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


_Ospfv3VirtNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_Ospfv3VirtNbrRestartHelperExitReason_Object = MibTableColumn
ospfv3VirtNbrRestartHelperExitReason = _Ospfv3VirtNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 11, 1, 15),
    _Ospfv3VirtNbrRestartHelperExitReason_Type()
)
ospfv3VirtNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtNbrRestartHelperExitReason.setStatus("current")
_Ospfv3AreaAggregateTable_Object = MibTable
ospfv3AreaAggregateTable = _Ospfv3AreaAggregateTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 12)
)
if mibBuilder.loadTexts:
    ospfv3AreaAggregateTable.setStatus("current")
_Ospfv3AreaAggregateEntry_Object = MibTableRow
ospfv3AreaAggregateEntry = _Ospfv3AreaAggregateEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 12, 1)
)
ospfv3AreaAggregateEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3AreaAggregateAreaID"),
    (0, "OSPFV3-MIB", "ospfv3AreaAggregateAreaLsdbType"),
    (0, "OSPFV3-MIB", "ospfv3AreaAggregatePrefixType"),
    (0, "OSPFV3-MIB", "ospfv3AreaAggregatePrefix"),
    (0, "OSPFV3-MIB", "ospfv3AreaAggregatePrefixLength"),
)
if mibBuilder.loadTexts:
    ospfv3AreaAggregateEntry.setStatus("current")
_Ospfv3AreaAggregateAreaID_Type = Ospfv3AreaIdTC
_Ospfv3AreaAggregateAreaID_Object = MibTableColumn
ospfv3AreaAggregateAreaID = _Ospfv3AreaAggregateAreaID_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 12, 1, 1),
    _Ospfv3AreaAggregateAreaID_Type()
)
ospfv3AreaAggregateAreaID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AreaAggregateAreaID.setStatus("current")


class _Ospfv3AreaAggregateAreaLsdbType_Type(Integer32):
    """Custom type ospfv3AreaAggregateAreaLsdbType based on Integer32"""
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


_Ospfv3AreaAggregateAreaLsdbType_Type.__name__ = "Integer32"
_Ospfv3AreaAggregateAreaLsdbType_Object = MibTableColumn
ospfv3AreaAggregateAreaLsdbType = _Ospfv3AreaAggregateAreaLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 12, 1, 2),
    _Ospfv3AreaAggregateAreaLsdbType_Type()
)
ospfv3AreaAggregateAreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AreaAggregateAreaLsdbType.setStatus("current")
_Ospfv3AreaAggregatePrefixType_Type = InetAddressType
_Ospfv3AreaAggregatePrefixType_Object = MibTableColumn
ospfv3AreaAggregatePrefixType = _Ospfv3AreaAggregatePrefixType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 12, 1, 3),
    _Ospfv3AreaAggregatePrefixType_Type()
)
ospfv3AreaAggregatePrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AreaAggregatePrefixType.setStatus("current")


class _Ospfv3AreaAggregatePrefix_Type(InetAddress):
    """Custom type ospfv3AreaAggregatePrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ospfv3AreaAggregatePrefix_Type.__name__ = "InetAddress"
_Ospfv3AreaAggregatePrefix_Object = MibTableColumn
ospfv3AreaAggregatePrefix = _Ospfv3AreaAggregatePrefix_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 12, 1, 4),
    _Ospfv3AreaAggregatePrefix_Type()
)
ospfv3AreaAggregatePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AreaAggregatePrefix.setStatus("current")


class _Ospfv3AreaAggregatePrefixLength_Type(InetAddressPrefixLength):
    """Custom type ospfv3AreaAggregatePrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 128),
    )


_Ospfv3AreaAggregatePrefixLength_Type.__name__ = "InetAddressPrefixLength"
_Ospfv3AreaAggregatePrefixLength_Object = MibTableColumn
ospfv3AreaAggregatePrefixLength = _Ospfv3AreaAggregatePrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 12, 1, 5),
    _Ospfv3AreaAggregatePrefixLength_Type()
)
ospfv3AreaAggregatePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3AreaAggregatePrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3AreaAggregatePrefixLength.setUnits("bits")
_Ospfv3AreaAggregateRowStatus_Type = RowStatus
_Ospfv3AreaAggregateRowStatus_Object = MibTableColumn
ospfv3AreaAggregateRowStatus = _Ospfv3AreaAggregateRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 12, 1, 6),
    _Ospfv3AreaAggregateRowStatus_Type()
)
ospfv3AreaAggregateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3AreaAggregateRowStatus.setStatus("current")


class _Ospfv3AreaAggregateEffect_Type(Integer32):
    """Custom type ospfv3AreaAggregateEffect based on Integer32"""
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


_Ospfv3AreaAggregateEffect_Type.__name__ = "Integer32"
_Ospfv3AreaAggregateEffect_Object = MibTableColumn
ospfv3AreaAggregateEffect = _Ospfv3AreaAggregateEffect_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 12, 1, 7),
    _Ospfv3AreaAggregateEffect_Type()
)
ospfv3AreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3AreaAggregateEffect.setStatus("current")


class _Ospfv3AreaAggregateRouteTag_Type(Unsigned32):
    """Custom type ospfv3AreaAggregateRouteTag based on Unsigned32"""
    defaultValue = 0


_Ospfv3AreaAggregateRouteTag_Object = MibTableColumn
ospfv3AreaAggregateRouteTag = _Ospfv3AreaAggregateRouteTag_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 12, 1, 8),
    _Ospfv3AreaAggregateRouteTag_Type()
)
ospfv3AreaAggregateRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfv3AreaAggregateRouteTag.setStatus("current")
_Ospfv3VirtLinkLsdbTable_Object = MibTable
ospfv3VirtLinkLsdbTable = _Ospfv3VirtLinkLsdbTable_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13)
)
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbTable.setStatus("current")
_Ospfv3VirtLinkLsdbEntry_Object = MibTableRow
ospfv3VirtLinkLsdbEntry = _Ospfv3VirtLinkLsdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13, 1)
)
ospfv3VirtLinkLsdbEntry.setIndexNames(
    (0, "OSPFV3-MIB", "ospfv3VirtLinkLsdbIfAreaId"),
    (0, "OSPFV3-MIB", "ospfv3VirtLinkLsdbIfNeighbor"),
    (0, "OSPFV3-MIB", "ospfv3VirtLinkLsdbType"),
    (0, "OSPFV3-MIB", "ospfv3VirtLinkLsdbRouterId"),
    (0, "OSPFV3-MIB", "ospfv3VirtLinkLsdbLsid"),
)
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbEntry.setStatus("current")
_Ospfv3VirtLinkLsdbIfAreaId_Type = Ospfv3AreaIdTC
_Ospfv3VirtLinkLsdbIfAreaId_Object = MibTableColumn
ospfv3VirtLinkLsdbIfAreaId = _Ospfv3VirtLinkLsdbIfAreaId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13, 1, 1),
    _Ospfv3VirtLinkLsdbIfAreaId_Type()
)
ospfv3VirtLinkLsdbIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbIfAreaId.setStatus("current")
_Ospfv3VirtLinkLsdbIfNeighbor_Type = Ospfv3RouterIdTC
_Ospfv3VirtLinkLsdbIfNeighbor_Object = MibTableColumn
ospfv3VirtLinkLsdbIfNeighbor = _Ospfv3VirtLinkLsdbIfNeighbor_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13, 1, 2),
    _Ospfv3VirtLinkLsdbIfNeighbor_Type()
)
ospfv3VirtLinkLsdbIfNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbIfNeighbor.setStatus("current")


class _Ospfv3VirtLinkLsdbType_Type(Unsigned32):
    """Custom type ospfv3VirtLinkLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ospfv3VirtLinkLsdbType_Type.__name__ = "Unsigned32"
_Ospfv3VirtLinkLsdbType_Object = MibTableColumn
ospfv3VirtLinkLsdbType = _Ospfv3VirtLinkLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13, 1, 3),
    _Ospfv3VirtLinkLsdbType_Type()
)
ospfv3VirtLinkLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbType.setStatus("current")
_Ospfv3VirtLinkLsdbRouterId_Type = Ospfv3RouterIdTC
_Ospfv3VirtLinkLsdbRouterId_Object = MibTableColumn
ospfv3VirtLinkLsdbRouterId = _Ospfv3VirtLinkLsdbRouterId_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13, 1, 4),
    _Ospfv3VirtLinkLsdbRouterId_Type()
)
ospfv3VirtLinkLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbRouterId.setStatus("current")
_Ospfv3VirtLinkLsdbLsid_Type = Ospfv3LsIdTC
_Ospfv3VirtLinkLsdbLsid_Object = MibTableColumn
ospfv3VirtLinkLsdbLsid = _Ospfv3VirtLinkLsdbLsid_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13, 1, 5),
    _Ospfv3VirtLinkLsdbLsid_Type()
)
ospfv3VirtLinkLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbLsid.setStatus("current")
_Ospfv3VirtLinkLsdbSequence_Type = Ospfv3LsaSequenceTC
_Ospfv3VirtLinkLsdbSequence_Object = MibTableColumn
ospfv3VirtLinkLsdbSequence = _Ospfv3VirtLinkLsdbSequence_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13, 1, 6),
    _Ospfv3VirtLinkLsdbSequence_Type()
)
ospfv3VirtLinkLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbSequence.setStatus("current")
_Ospfv3VirtLinkLsdbAge_Type = Ospfv3LsaAgeTC
_Ospfv3VirtLinkLsdbAge_Object = MibTableColumn
ospfv3VirtLinkLsdbAge = _Ospfv3VirtLinkLsdbAge_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13, 1, 7),
    _Ospfv3VirtLinkLsdbAge_Type()
)
ospfv3VirtLinkLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbAge.setUnits("seconds")
_Ospfv3VirtLinkLsdbChecksum_Type = Integer32
_Ospfv3VirtLinkLsdbChecksum_Object = MibTableColumn
ospfv3VirtLinkLsdbChecksum = _Ospfv3VirtLinkLsdbChecksum_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13, 1, 8),
    _Ospfv3VirtLinkLsdbChecksum_Type()
)
ospfv3VirtLinkLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbChecksum.setStatus("current")


class _Ospfv3VirtLinkLsdbAdvertisement_Type(OctetString):
    """Custom type ospfv3VirtLinkLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_Ospfv3VirtLinkLsdbAdvertisement_Type.__name__ = "OctetString"
_Ospfv3VirtLinkLsdbAdvertisement_Object = MibTableColumn
ospfv3VirtLinkLsdbAdvertisement = _Ospfv3VirtLinkLsdbAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13, 1, 9),
    _Ospfv3VirtLinkLsdbAdvertisement_Type()
)
ospfv3VirtLinkLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbAdvertisement.setStatus("current")
_Ospfv3VirtLinkLsdbTypeKnown_Type = TruthValue
_Ospfv3VirtLinkLsdbTypeKnown_Object = MibTableColumn
ospfv3VirtLinkLsdbTypeKnown = _Ospfv3VirtLinkLsdbTypeKnown_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 13, 1, 10),
    _Ospfv3VirtLinkLsdbTypeKnown_Type()
)
ospfv3VirtLinkLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbTypeKnown.setStatus("current")
_Ospfv3NotificationEntry_ObjectIdentity = ObjectIdentity
ospfv3NotificationEntry = _Ospfv3NotificationEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 191, 1, 14)
)


class _Ospfv3ConfigErrorType_Type(Integer32):
    """Custom type ospfv3ConfigErrorType based on Integer32"""
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


_Ospfv3ConfigErrorType_Type.__name__ = "Integer32"
_Ospfv3ConfigErrorType_Object = MibScalar
ospfv3ConfigErrorType = _Ospfv3ConfigErrorType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 14, 1),
    _Ospfv3ConfigErrorType_Type()
)
ospfv3ConfigErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfv3ConfigErrorType.setStatus("current")


class _Ospfv3PacketType_Type(Integer32):
    """Custom type ospfv3PacketType based on Integer32"""
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


_Ospfv3PacketType_Type.__name__ = "Integer32"
_Ospfv3PacketType_Object = MibScalar
ospfv3PacketType = _Ospfv3PacketType_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 14, 2),
    _Ospfv3PacketType_Type()
)
ospfv3PacketType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfv3PacketType.setStatus("current")
_Ospfv3PacketSrc_Type = InetAddressIPv6
_Ospfv3PacketSrc_Object = MibScalar
ospfv3PacketSrc = _Ospfv3PacketSrc_Object(
    (1, 3, 6, 1, 2, 1, 191, 1, 14, 3),
    _Ospfv3PacketSrc_Type()
)
ospfv3PacketSrc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ospfv3PacketSrc.setStatus("current")
_Ospfv3Conformance_ObjectIdentity = ObjectIdentity
ospfv3Conformance = _Ospfv3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 191, 2)
)
_Ospfv3Groups_ObjectIdentity = ObjectIdentity
ospfv3Groups = _Ospfv3Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 191, 2, 1)
)
_Ospfv3Compliances_ObjectIdentity = ObjectIdentity
ospfv3Compliances = _Ospfv3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 191, 2, 2)
)

# Managed Objects groups

ospfv3BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 1)
)
ospfv3BasicGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3AdminStatus"),
        ("OSPFV3-MIB", "ospfv3VersionNumber"),
        ("OSPFV3-MIB", "ospfv3AreaBdrRtrStatus"),
        ("OSPFV3-MIB", "ospfv3ASBdrRtrStatus"),
        ("OSPFV3-MIB", "ospfv3AsScopeLsaCount"),
        ("OSPFV3-MIB", "ospfv3AsScopeLsaCksumSum"),
        ("OSPFV3-MIB", "ospfv3OriginateNewLsas"),
        ("OSPFV3-MIB", "ospfv3RxNewLsas"),
        ("OSPFV3-MIB", "ospfv3ExtLsaCount"),
        ("OSPFV3-MIB", "ospfv3ExtAreaLsdbLimit"),
        ("OSPFV3-MIB", "ospfv3ExitOverflowInterval"),
        ("OSPFV3-MIB", "ospfv3DemandExtensions"),
        ("OSPFV3-MIB", "ospfv3ReferenceBandwidth"),
        ("OSPFV3-MIB", "ospfv3RestartSupport"),
        ("OSPFV3-MIB", "ospfv3RestartInterval"),
        ("OSPFV3-MIB", "ospfv3RestartStrictLsaChecking"),
        ("OSPFV3-MIB", "ospfv3RestartStatus"),
        ("OSPFV3-MIB", "ospfv3RestartAge"),
        ("OSPFV3-MIB", "ospfv3RestartExitReason"),
        ("OSPFV3-MIB", "ospfv3NotificationEnable"),
        ("OSPFV3-MIB", "ospfv3StubRouterSupport"),
        ("OSPFV3-MIB", "ospfv3StubRouterAdvertisement"),
        ("OSPFV3-MIB", "ospfv3DiscontinuityTime"),
        ("OSPFV3-MIB", "ospfv3RestartTime"))
)
if mibBuilder.loadTexts:
    ospfv3BasicGroup.setStatus("current")

ospfv3AreaGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 2)
)
ospfv3AreaGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3AreaImportAsExtern"),
        ("OSPFV3-MIB", "ospfv3AreaSpfRuns"),
        ("OSPFV3-MIB", "ospfv3AreaBdrRtrCount"),
        ("OSPFV3-MIB", "ospfv3AreaAsBdrRtrCount"),
        ("OSPFV3-MIB", "ospfv3AreaScopeLsaCount"),
        ("OSPFV3-MIB", "ospfv3AreaScopeLsaCksumSum"),
        ("OSPFV3-MIB", "ospfv3AreaSummary"),
        ("OSPFV3-MIB", "ospfv3AreaRowStatus"),
        ("OSPFV3-MIB", "ospfv3AreaStubMetric"),
        ("OSPFV3-MIB", "ospfv3AreaNssaTranslatorRole"),
        ("OSPFV3-MIB", "ospfv3AreaNssaTranslatorState"),
        ("OSPFV3-MIB", "ospfv3AreaNssaTranslatorStabInterval"),
        ("OSPFV3-MIB", "ospfv3AreaNssaTranslatorEvents"),
        ("OSPFV3-MIB", "ospfv3AreaStubMetricType"),
        ("OSPFV3-MIB", "ospfv3AreaTEEnabled"))
)
if mibBuilder.loadTexts:
    ospfv3AreaGroup.setStatus("current")

ospfv3AsLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 3)
)
ospfv3AsLsdbGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3AsLsdbSequence"),
        ("OSPFV3-MIB", "ospfv3AsLsdbAge"),
        ("OSPFV3-MIB", "ospfv3AsLsdbChecksum"),
        ("OSPFV3-MIB", "ospfv3AsLsdbAdvertisement"),
        ("OSPFV3-MIB", "ospfv3AsLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    ospfv3AsLsdbGroup.setStatus("current")

ospfv3AreaLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 4)
)
ospfv3AreaLsdbGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3AreaLsdbSequence"),
        ("OSPFV3-MIB", "ospfv3AreaLsdbAge"),
        ("OSPFV3-MIB", "ospfv3AreaLsdbChecksum"),
        ("OSPFV3-MIB", "ospfv3AreaLsdbAdvertisement"),
        ("OSPFV3-MIB", "ospfv3AreaLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    ospfv3AreaLsdbGroup.setStatus("current")

ospfv3LinkLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 5)
)
ospfv3LinkLsdbGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3LinkLsdbSequence"),
        ("OSPFV3-MIB", "ospfv3LinkLsdbAge"),
        ("OSPFV3-MIB", "ospfv3LinkLsdbChecksum"),
        ("OSPFV3-MIB", "ospfv3LinkLsdbAdvertisement"),
        ("OSPFV3-MIB", "ospfv3LinkLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    ospfv3LinkLsdbGroup.setStatus("current")

ospfv3HostGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 6)
)
ospfv3HostGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3HostMetric"),
        ("OSPFV3-MIB", "ospfv3HostRowStatus"),
        ("OSPFV3-MIB", "ospfv3HostAreaID"))
)
if mibBuilder.loadTexts:
    ospfv3HostGroup.setStatus("current")

ospfv3IfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 7)
)
ospfv3IfGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3IfAreaId"),
        ("OSPFV3-MIB", "ospfv3IfType"),
        ("OSPFV3-MIB", "ospfv3IfAdminStatus"),
        ("OSPFV3-MIB", "ospfv3IfRtrPriority"),
        ("OSPFV3-MIB", "ospfv3IfTransitDelay"),
        ("OSPFV3-MIB", "ospfv3IfRetransInterval"),
        ("OSPFV3-MIB", "ospfv3IfHelloInterval"),
        ("OSPFV3-MIB", "ospfv3IfRtrDeadInterval"),
        ("OSPFV3-MIB", "ospfv3IfPollInterval"),
        ("OSPFV3-MIB", "ospfv3IfState"),
        ("OSPFV3-MIB", "ospfv3IfDesignatedRouter"),
        ("OSPFV3-MIB", "ospfv3IfBackupDesignatedRouter"),
        ("OSPFV3-MIB", "ospfv3IfEvents"),
        ("OSPFV3-MIB", "ospfv3IfRowStatus"),
        ("OSPFV3-MIB", "ospfv3IfDemand"),
        ("OSPFV3-MIB", "ospfv3IfMetricValue"),
        ("OSPFV3-MIB", "ospfv3IfLinkScopeLsaCount"),
        ("OSPFV3-MIB", "ospfv3IfLinkLsaCksumSum"),
        ("OSPFV3-MIB", "ospfv3IfDemandNbrProbe"),
        ("OSPFV3-MIB", "ospfv3IfDemandNbrProbeRetransLimit"),
        ("OSPFV3-MIB", "ospfv3IfDemandNbrProbeInterval"),
        ("OSPFV3-MIB", "ospfv3IfTEDisabled"),
        ("OSPFV3-MIB", "ospfv3IfLinkLSASuppression"))
)
if mibBuilder.loadTexts:
    ospfv3IfGroup.setStatus("current")

ospfv3VirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 8)
)
ospfv3VirtIfGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3VirtIfIndex"),
        ("OSPFV3-MIB", "ospfv3VirtIfInstId"),
        ("OSPFV3-MIB", "ospfv3VirtIfTransitDelay"),
        ("OSPFV3-MIB", "ospfv3VirtIfRetransInterval"),
        ("OSPFV3-MIB", "ospfv3VirtIfHelloInterval"),
        ("OSPFV3-MIB", "ospfv3VirtIfRtrDeadInterval"),
        ("OSPFV3-MIB", "ospfv3VirtIfState"),
        ("OSPFV3-MIB", "ospfv3VirtIfEvents"),
        ("OSPFV3-MIB", "ospfv3VirtIfRowStatus"),
        ("OSPFV3-MIB", "ospfv3VirtIfLinkScopeLsaCount"),
        ("OSPFV3-MIB", "ospfv3VirtIfLinkLsaCksumSum"))
)
if mibBuilder.loadTexts:
    ospfv3VirtIfGroup.setStatus("current")

ospfv3NbrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 9)
)
ospfv3NbrGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3NbrAddressType"),
        ("OSPFV3-MIB", "ospfv3NbrAddress"),
        ("OSPFV3-MIB", "ospfv3NbrOptions"),
        ("OSPFV3-MIB", "ospfv3NbrPriority"),
        ("OSPFV3-MIB", "ospfv3NbrState"),
        ("OSPFV3-MIB", "ospfv3NbrEvents"),
        ("OSPFV3-MIB", "ospfv3NbrLsRetransQLen"),
        ("OSPFV3-MIB", "ospfv3NbrHelloSuppressed"),
        ("OSPFV3-MIB", "ospfv3NbrIfId"),
        ("OSPFV3-MIB", "ospfv3NbrRestartHelperStatus"),
        ("OSPFV3-MIB", "ospfv3NbrRestartHelperAge"),
        ("OSPFV3-MIB", "ospfv3NbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    ospfv3NbrGroup.setStatus("current")

ospfv3CfgNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 10)
)
ospfv3CfgNbrGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3CfgNbrPriority"),
        ("OSPFV3-MIB", "ospfv3CfgNbrRowStatus"))
)
if mibBuilder.loadTexts:
    ospfv3CfgNbrGroup.setStatus("current")

ospfv3VirtNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 11)
)
ospfv3VirtNbrGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3VirtNbrIfIndex"),
        ("OSPFV3-MIB", "ospfv3VirtNbrIfInstId"),
        ("OSPFV3-MIB", "ospfv3VirtNbrAddressType"),
        ("OSPFV3-MIB", "ospfv3VirtNbrAddress"),
        ("OSPFV3-MIB", "ospfv3VirtNbrOptions"),
        ("OSPFV3-MIB", "ospfv3VirtNbrState"),
        ("OSPFV3-MIB", "ospfv3VirtNbrEvents"),
        ("OSPFV3-MIB", "ospfv3VirtNbrLsRetransQLen"),
        ("OSPFV3-MIB", "ospfv3VirtNbrHelloSuppressed"),
        ("OSPFV3-MIB", "ospfv3VirtNbrIfId"),
        ("OSPFV3-MIB", "ospfv3VirtNbrRestartHelperStatus"),
        ("OSPFV3-MIB", "ospfv3VirtNbrRestartHelperAge"),
        ("OSPFV3-MIB", "ospfv3VirtNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    ospfv3VirtNbrGroup.setStatus("current")

ospfv3AreaAggregateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 12)
)
ospfv3AreaAggregateGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3AreaAggregateRowStatus"),
        ("OSPFV3-MIB", "ospfv3AreaAggregateEffect"),
        ("OSPFV3-MIB", "ospfv3AreaAggregateRouteTag"))
)
if mibBuilder.loadTexts:
    ospfv3AreaAggregateGroup.setStatus("current")

ospfv3VirtLinkLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 13)
)
ospfv3VirtLinkLsdbGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3VirtLinkLsdbSequence"),
        ("OSPFV3-MIB", "ospfv3VirtLinkLsdbAge"),
        ("OSPFV3-MIB", "ospfv3VirtLinkLsdbChecksum"),
        ("OSPFV3-MIB", "ospfv3VirtLinkLsdbAdvertisement"),
        ("OSPFV3-MIB", "ospfv3VirtLinkLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    ospfv3VirtLinkLsdbGroup.setStatus("current")

ospfv3NotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 14)
)
ospfv3NotificationObjectGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3ConfigErrorType"),
        ("OSPFV3-MIB", "ospfv3PacketType"),
        ("OSPFV3-MIB", "ospfv3PacketSrc"))
)
if mibBuilder.loadTexts:
    ospfv3NotificationObjectGroup.setStatus("current")


# Notification objects

ospfv3VirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 1)
)
ospfv3VirtIfStateChange.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3VirtIfState"))
)
if mibBuilder.loadTexts:
    ospfv3VirtIfStateChange.setStatus(
        "current"
    )

ospfv3NbrStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 2)
)
ospfv3NbrStateChange.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3NbrState"))
)
if mibBuilder.loadTexts:
    ospfv3NbrStateChange.setStatus(
        "current"
    )

ospfv3VirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 3)
)
ospfv3VirtNbrStateChange.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3VirtNbrState"))
)
if mibBuilder.loadTexts:
    ospfv3VirtNbrStateChange.setStatus(
        "current"
    )

ospfv3IfConfigError = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 4)
)
ospfv3IfConfigError.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3IfState"),
        ("OSPFV3-MIB", "ospfv3PacketSrc"),
        ("OSPFV3-MIB", "ospfv3ConfigErrorType"),
        ("OSPFV3-MIB", "ospfv3PacketType"))
)
if mibBuilder.loadTexts:
    ospfv3IfConfigError.setStatus(
        "current"
    )

ospfv3VirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 5)
)
ospfv3VirtIfConfigError.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3VirtIfState"),
        ("OSPFV3-MIB", "ospfv3ConfigErrorType"),
        ("OSPFV3-MIB", "ospfv3PacketType"))
)
if mibBuilder.loadTexts:
    ospfv3VirtIfConfigError.setStatus(
        "current"
    )

ospfv3IfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 6)
)
ospfv3IfRxBadPacket.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3IfState"),
        ("OSPFV3-MIB", "ospfv3PacketSrc"),
        ("OSPFV3-MIB", "ospfv3PacketType"))
)
if mibBuilder.loadTexts:
    ospfv3IfRxBadPacket.setStatus(
        "current"
    )

ospfv3VirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 7)
)
ospfv3VirtIfRxBadPacket.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3VirtIfState"),
        ("OSPFV3-MIB", "ospfv3PacketType"))
)
if mibBuilder.loadTexts:
    ospfv3VirtIfRxBadPacket.setStatus(
        "current"
    )

ospfv3LsdbOverflow = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 8)
)
ospfv3LsdbOverflow.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3ExtAreaLsdbLimit"))
)
if mibBuilder.loadTexts:
    ospfv3LsdbOverflow.setStatus(
        "current"
    )

ospfv3LsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 9)
)
ospfv3LsdbApproachingOverflow.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3ExtAreaLsdbLimit"))
)
if mibBuilder.loadTexts:
    ospfv3LsdbApproachingOverflow.setStatus(
        "current"
    )

ospfv3IfStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 10)
)
ospfv3IfStateChange.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3IfState"))
)
if mibBuilder.loadTexts:
    ospfv3IfStateChange.setStatus(
        "current"
    )

ospfv3NssaTranslatorStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 11)
)
ospfv3NssaTranslatorStatusChange.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3AreaNssaTranslatorState"))
)
if mibBuilder.loadTexts:
    ospfv3NssaTranslatorStatusChange.setStatus(
        "current"
    )

ospfv3RestartStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 12)
)
ospfv3RestartStatusChange.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3RestartStatus"),
        ("OSPFV3-MIB", "ospfv3RestartInterval"),
        ("OSPFV3-MIB", "ospfv3RestartExitReason"))
)
if mibBuilder.loadTexts:
    ospfv3RestartStatusChange.setStatus(
        "current"
    )

ospfv3NbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 13)
)
ospfv3NbrRestartHelperStatusChange.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3NbrRestartHelperStatus"),
        ("OSPFV3-MIB", "ospfv3NbrRestartHelperAge"),
        ("OSPFV3-MIB", "ospfv3NbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    ospfv3NbrRestartHelperStatusChange.setStatus(
        "current"
    )

ospfv3VirtNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 191, 0, 14)
)
ospfv3VirtNbrRestartHelperStatusChange.setObjects(
      *(("OSPFV3-MIB", "ospfv3RouterId"),
        ("OSPFV3-MIB", "ospfv3VirtNbrRestartHelperStatus"),
        ("OSPFV3-MIB", "ospfv3VirtNbrRestartHelperAge"),
        ("OSPFV3-MIB", "ospfv3VirtNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    ospfv3VirtNbrRestartHelperStatusChange.setStatus(
        "current"
    )


# Notifications groups

ospfv3NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 191, 2, 1, 15)
)
ospfv3NotificationGroup.setObjects(
      *(("OSPFV3-MIB", "ospfv3VirtIfStateChange"),
        ("OSPFV3-MIB", "ospfv3NbrStateChange"),
        ("OSPFV3-MIB", "ospfv3VirtNbrStateChange"),
        ("OSPFV3-MIB", "ospfv3IfConfigError"),
        ("OSPFV3-MIB", "ospfv3VirtIfConfigError"),
        ("OSPFV3-MIB", "ospfv3IfRxBadPacket"),
        ("OSPFV3-MIB", "ospfv3VirtIfRxBadPacket"),
        ("OSPFV3-MIB", "ospfv3LsdbOverflow"),
        ("OSPFV3-MIB", "ospfv3LsdbApproachingOverflow"),
        ("OSPFV3-MIB", "ospfv3IfStateChange"),
        ("OSPFV3-MIB", "ospfv3NssaTranslatorStatusChange"),
        ("OSPFV3-MIB", "ospfv3RestartStatusChange"),
        ("OSPFV3-MIB", "ospfv3NbrRestartHelperStatusChange"),
        ("OSPFV3-MIB", "ospfv3VirtNbrRestartHelperStatusChange"))
)
if mibBuilder.loadTexts:
    ospfv3NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ospfv3FullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 191, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ospfv3FullCompliance.setStatus(
        "current"
    )

ospfv3ReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 191, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ospfv3ReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OSPFV3-MIB",
    **{"Ospfv3UpToRefreshIntervalTC": Ospfv3UpToRefreshIntervalTC,
       "Ospfv3DeadIntervalRangeTC": Ospfv3DeadIntervalRangeTC,
       "Ospfv3RouterIdTC": Ospfv3RouterIdTC,
       "Ospfv3LsIdTC": Ospfv3LsIdTC,
       "Ospfv3AreaIdTC": Ospfv3AreaIdTC,
       "Ospfv3IfInstIdTC": Ospfv3IfInstIdTC,
       "Ospfv3LsaSequenceTC": Ospfv3LsaSequenceTC,
       "Ospfv3LsaAgeTC": Ospfv3LsaAgeTC,
       "ospfv3MIB": ospfv3MIB,
       "ospfv3Notifications": ospfv3Notifications,
       "ospfv3VirtIfStateChange": ospfv3VirtIfStateChange,
       "ospfv3NbrStateChange": ospfv3NbrStateChange,
       "ospfv3VirtNbrStateChange": ospfv3VirtNbrStateChange,
       "ospfv3IfConfigError": ospfv3IfConfigError,
       "ospfv3VirtIfConfigError": ospfv3VirtIfConfigError,
       "ospfv3IfRxBadPacket": ospfv3IfRxBadPacket,
       "ospfv3VirtIfRxBadPacket": ospfv3VirtIfRxBadPacket,
       "ospfv3LsdbOverflow": ospfv3LsdbOverflow,
       "ospfv3LsdbApproachingOverflow": ospfv3LsdbApproachingOverflow,
       "ospfv3IfStateChange": ospfv3IfStateChange,
       "ospfv3NssaTranslatorStatusChange": ospfv3NssaTranslatorStatusChange,
       "ospfv3RestartStatusChange": ospfv3RestartStatusChange,
       "ospfv3NbrRestartHelperStatusChange": ospfv3NbrRestartHelperStatusChange,
       "ospfv3VirtNbrRestartHelperStatusChange": ospfv3VirtNbrRestartHelperStatusChange,
       "ospfv3Objects": ospfv3Objects,
       "ospfv3GeneralGroup": ospfv3GeneralGroup,
       "ospfv3RouterId": ospfv3RouterId,
       "ospfv3AdminStatus": ospfv3AdminStatus,
       "ospfv3VersionNumber": ospfv3VersionNumber,
       "ospfv3AreaBdrRtrStatus": ospfv3AreaBdrRtrStatus,
       "ospfv3ASBdrRtrStatus": ospfv3ASBdrRtrStatus,
       "ospfv3AsScopeLsaCount": ospfv3AsScopeLsaCount,
       "ospfv3AsScopeLsaCksumSum": ospfv3AsScopeLsaCksumSum,
       "ospfv3OriginateNewLsas": ospfv3OriginateNewLsas,
       "ospfv3RxNewLsas": ospfv3RxNewLsas,
       "ospfv3ExtLsaCount": ospfv3ExtLsaCount,
       "ospfv3ExtAreaLsdbLimit": ospfv3ExtAreaLsdbLimit,
       "ospfv3ExitOverflowInterval": ospfv3ExitOverflowInterval,
       "ospfv3DemandExtensions": ospfv3DemandExtensions,
       "ospfv3ReferenceBandwidth": ospfv3ReferenceBandwidth,
       "ospfv3RestartSupport": ospfv3RestartSupport,
       "ospfv3RestartInterval": ospfv3RestartInterval,
       "ospfv3RestartStrictLsaChecking": ospfv3RestartStrictLsaChecking,
       "ospfv3RestartStatus": ospfv3RestartStatus,
       "ospfv3RestartAge": ospfv3RestartAge,
       "ospfv3RestartExitReason": ospfv3RestartExitReason,
       "ospfv3NotificationEnable": ospfv3NotificationEnable,
       "ospfv3StubRouterSupport": ospfv3StubRouterSupport,
       "ospfv3StubRouterAdvertisement": ospfv3StubRouterAdvertisement,
       "ospfv3DiscontinuityTime": ospfv3DiscontinuityTime,
       "ospfv3RestartTime": ospfv3RestartTime,
       "ospfv3AreaTable": ospfv3AreaTable,
       "ospfv3AreaEntry": ospfv3AreaEntry,
       "ospfv3AreaId": ospfv3AreaId,
       "ospfv3AreaImportAsExtern": ospfv3AreaImportAsExtern,
       "ospfv3AreaSpfRuns": ospfv3AreaSpfRuns,
       "ospfv3AreaBdrRtrCount": ospfv3AreaBdrRtrCount,
       "ospfv3AreaAsBdrRtrCount": ospfv3AreaAsBdrRtrCount,
       "ospfv3AreaScopeLsaCount": ospfv3AreaScopeLsaCount,
       "ospfv3AreaScopeLsaCksumSum": ospfv3AreaScopeLsaCksumSum,
       "ospfv3AreaSummary": ospfv3AreaSummary,
       "ospfv3AreaRowStatus": ospfv3AreaRowStatus,
       "ospfv3AreaStubMetric": ospfv3AreaStubMetric,
       "ospfv3AreaNssaTranslatorRole": ospfv3AreaNssaTranslatorRole,
       "ospfv3AreaNssaTranslatorState": ospfv3AreaNssaTranslatorState,
       "ospfv3AreaNssaTranslatorStabInterval": ospfv3AreaNssaTranslatorStabInterval,
       "ospfv3AreaNssaTranslatorEvents": ospfv3AreaNssaTranslatorEvents,
       "ospfv3AreaStubMetricType": ospfv3AreaStubMetricType,
       "ospfv3AreaTEEnabled": ospfv3AreaTEEnabled,
       "ospfv3AsLsdbTable": ospfv3AsLsdbTable,
       "ospfv3AsLsdbEntry": ospfv3AsLsdbEntry,
       "ospfv3AsLsdbType": ospfv3AsLsdbType,
       "ospfv3AsLsdbRouterId": ospfv3AsLsdbRouterId,
       "ospfv3AsLsdbLsid": ospfv3AsLsdbLsid,
       "ospfv3AsLsdbSequence": ospfv3AsLsdbSequence,
       "ospfv3AsLsdbAge": ospfv3AsLsdbAge,
       "ospfv3AsLsdbChecksum": ospfv3AsLsdbChecksum,
       "ospfv3AsLsdbAdvertisement": ospfv3AsLsdbAdvertisement,
       "ospfv3AsLsdbTypeKnown": ospfv3AsLsdbTypeKnown,
       "ospfv3AreaLsdbTable": ospfv3AreaLsdbTable,
       "ospfv3AreaLsdbEntry": ospfv3AreaLsdbEntry,
       "ospfv3AreaLsdbAreaId": ospfv3AreaLsdbAreaId,
       "ospfv3AreaLsdbType": ospfv3AreaLsdbType,
       "ospfv3AreaLsdbRouterId": ospfv3AreaLsdbRouterId,
       "ospfv3AreaLsdbLsid": ospfv3AreaLsdbLsid,
       "ospfv3AreaLsdbSequence": ospfv3AreaLsdbSequence,
       "ospfv3AreaLsdbAge": ospfv3AreaLsdbAge,
       "ospfv3AreaLsdbChecksum": ospfv3AreaLsdbChecksum,
       "ospfv3AreaLsdbAdvertisement": ospfv3AreaLsdbAdvertisement,
       "ospfv3AreaLsdbTypeKnown": ospfv3AreaLsdbTypeKnown,
       "ospfv3LinkLsdbTable": ospfv3LinkLsdbTable,
       "ospfv3LinkLsdbEntry": ospfv3LinkLsdbEntry,
       "ospfv3LinkLsdbIfIndex": ospfv3LinkLsdbIfIndex,
       "ospfv3LinkLsdbIfInstId": ospfv3LinkLsdbIfInstId,
       "ospfv3LinkLsdbType": ospfv3LinkLsdbType,
       "ospfv3LinkLsdbRouterId": ospfv3LinkLsdbRouterId,
       "ospfv3LinkLsdbLsid": ospfv3LinkLsdbLsid,
       "ospfv3LinkLsdbSequence": ospfv3LinkLsdbSequence,
       "ospfv3LinkLsdbAge": ospfv3LinkLsdbAge,
       "ospfv3LinkLsdbChecksum": ospfv3LinkLsdbChecksum,
       "ospfv3LinkLsdbAdvertisement": ospfv3LinkLsdbAdvertisement,
       "ospfv3LinkLsdbTypeKnown": ospfv3LinkLsdbTypeKnown,
       "ospfv3HostTable": ospfv3HostTable,
       "ospfv3HostEntry": ospfv3HostEntry,
       "ospfv3HostAddressType": ospfv3HostAddressType,
       "ospfv3HostAddress": ospfv3HostAddress,
       "ospfv3HostMetric": ospfv3HostMetric,
       "ospfv3HostRowStatus": ospfv3HostRowStatus,
       "ospfv3HostAreaID": ospfv3HostAreaID,
       "ospfv3IfTable": ospfv3IfTable,
       "ospfv3IfEntry": ospfv3IfEntry,
       "ospfv3IfIndex": ospfv3IfIndex,
       "ospfv3IfInstId": ospfv3IfInstId,
       "ospfv3IfAreaId": ospfv3IfAreaId,
       "ospfv3IfType": ospfv3IfType,
       "ospfv3IfAdminStatus": ospfv3IfAdminStatus,
       "ospfv3IfRtrPriority": ospfv3IfRtrPriority,
       "ospfv3IfTransitDelay": ospfv3IfTransitDelay,
       "ospfv3IfRetransInterval": ospfv3IfRetransInterval,
       "ospfv3IfHelloInterval": ospfv3IfHelloInterval,
       "ospfv3IfRtrDeadInterval": ospfv3IfRtrDeadInterval,
       "ospfv3IfPollInterval": ospfv3IfPollInterval,
       "ospfv3IfState": ospfv3IfState,
       "ospfv3IfDesignatedRouter": ospfv3IfDesignatedRouter,
       "ospfv3IfBackupDesignatedRouter": ospfv3IfBackupDesignatedRouter,
       "ospfv3IfEvents": ospfv3IfEvents,
       "ospfv3IfRowStatus": ospfv3IfRowStatus,
       "ospfv3IfDemand": ospfv3IfDemand,
       "ospfv3IfMetricValue": ospfv3IfMetricValue,
       "ospfv3IfLinkScopeLsaCount": ospfv3IfLinkScopeLsaCount,
       "ospfv3IfLinkLsaCksumSum": ospfv3IfLinkLsaCksumSum,
       "ospfv3IfDemandNbrProbe": ospfv3IfDemandNbrProbe,
       "ospfv3IfDemandNbrProbeRetransLimit": ospfv3IfDemandNbrProbeRetransLimit,
       "ospfv3IfDemandNbrProbeInterval": ospfv3IfDemandNbrProbeInterval,
       "ospfv3IfTEDisabled": ospfv3IfTEDisabled,
       "ospfv3IfLinkLSASuppression": ospfv3IfLinkLSASuppression,
       "ospfv3VirtIfTable": ospfv3VirtIfTable,
       "ospfv3VirtIfEntry": ospfv3VirtIfEntry,
       "ospfv3VirtIfAreaId": ospfv3VirtIfAreaId,
       "ospfv3VirtIfNeighbor": ospfv3VirtIfNeighbor,
       "ospfv3VirtIfIndex": ospfv3VirtIfIndex,
       "ospfv3VirtIfInstId": ospfv3VirtIfInstId,
       "ospfv3VirtIfTransitDelay": ospfv3VirtIfTransitDelay,
       "ospfv3VirtIfRetransInterval": ospfv3VirtIfRetransInterval,
       "ospfv3VirtIfHelloInterval": ospfv3VirtIfHelloInterval,
       "ospfv3VirtIfRtrDeadInterval": ospfv3VirtIfRtrDeadInterval,
       "ospfv3VirtIfState": ospfv3VirtIfState,
       "ospfv3VirtIfEvents": ospfv3VirtIfEvents,
       "ospfv3VirtIfRowStatus": ospfv3VirtIfRowStatus,
       "ospfv3VirtIfLinkScopeLsaCount": ospfv3VirtIfLinkScopeLsaCount,
       "ospfv3VirtIfLinkLsaCksumSum": ospfv3VirtIfLinkLsaCksumSum,
       "ospfv3NbrTable": ospfv3NbrTable,
       "ospfv3NbrEntry": ospfv3NbrEntry,
       "ospfv3NbrIfIndex": ospfv3NbrIfIndex,
       "ospfv3NbrIfInstId": ospfv3NbrIfInstId,
       "ospfv3NbrRtrId": ospfv3NbrRtrId,
       "ospfv3NbrAddressType": ospfv3NbrAddressType,
       "ospfv3NbrAddress": ospfv3NbrAddress,
       "ospfv3NbrOptions": ospfv3NbrOptions,
       "ospfv3NbrPriority": ospfv3NbrPriority,
       "ospfv3NbrState": ospfv3NbrState,
       "ospfv3NbrEvents": ospfv3NbrEvents,
       "ospfv3NbrLsRetransQLen": ospfv3NbrLsRetransQLen,
       "ospfv3NbrHelloSuppressed": ospfv3NbrHelloSuppressed,
       "ospfv3NbrIfId": ospfv3NbrIfId,
       "ospfv3NbrRestartHelperStatus": ospfv3NbrRestartHelperStatus,
       "ospfv3NbrRestartHelperAge": ospfv3NbrRestartHelperAge,
       "ospfv3NbrRestartHelperExitReason": ospfv3NbrRestartHelperExitReason,
       "ospfv3CfgNbrTable": ospfv3CfgNbrTable,
       "ospfv3CfgNbrEntry": ospfv3CfgNbrEntry,
       "ospfv3CfgNbrIfIndex": ospfv3CfgNbrIfIndex,
       "ospfv3CfgNbrIfInstId": ospfv3CfgNbrIfInstId,
       "ospfv3CfgNbrAddressType": ospfv3CfgNbrAddressType,
       "ospfv3CfgNbrAddress": ospfv3CfgNbrAddress,
       "ospfv3CfgNbrPriority": ospfv3CfgNbrPriority,
       "ospfv3CfgNbrRowStatus": ospfv3CfgNbrRowStatus,
       "ospfv3VirtNbrTable": ospfv3VirtNbrTable,
       "ospfv3VirtNbrEntry": ospfv3VirtNbrEntry,
       "ospfv3VirtNbrArea": ospfv3VirtNbrArea,
       "ospfv3VirtNbrRtrId": ospfv3VirtNbrRtrId,
       "ospfv3VirtNbrIfIndex": ospfv3VirtNbrIfIndex,
       "ospfv3VirtNbrIfInstId": ospfv3VirtNbrIfInstId,
       "ospfv3VirtNbrAddressType": ospfv3VirtNbrAddressType,
       "ospfv3VirtNbrAddress": ospfv3VirtNbrAddress,
       "ospfv3VirtNbrOptions": ospfv3VirtNbrOptions,
       "ospfv3VirtNbrState": ospfv3VirtNbrState,
       "ospfv3VirtNbrEvents": ospfv3VirtNbrEvents,
       "ospfv3VirtNbrLsRetransQLen": ospfv3VirtNbrLsRetransQLen,
       "ospfv3VirtNbrHelloSuppressed": ospfv3VirtNbrHelloSuppressed,
       "ospfv3VirtNbrIfId": ospfv3VirtNbrIfId,
       "ospfv3VirtNbrRestartHelperStatus": ospfv3VirtNbrRestartHelperStatus,
       "ospfv3VirtNbrRestartHelperAge": ospfv3VirtNbrRestartHelperAge,
       "ospfv3VirtNbrRestartHelperExitReason": ospfv3VirtNbrRestartHelperExitReason,
       "ospfv3AreaAggregateTable": ospfv3AreaAggregateTable,
       "ospfv3AreaAggregateEntry": ospfv3AreaAggregateEntry,
       "ospfv3AreaAggregateAreaID": ospfv3AreaAggregateAreaID,
       "ospfv3AreaAggregateAreaLsdbType": ospfv3AreaAggregateAreaLsdbType,
       "ospfv3AreaAggregatePrefixType": ospfv3AreaAggregatePrefixType,
       "ospfv3AreaAggregatePrefix": ospfv3AreaAggregatePrefix,
       "ospfv3AreaAggregatePrefixLength": ospfv3AreaAggregatePrefixLength,
       "ospfv3AreaAggregateRowStatus": ospfv3AreaAggregateRowStatus,
       "ospfv3AreaAggregateEffect": ospfv3AreaAggregateEffect,
       "ospfv3AreaAggregateRouteTag": ospfv3AreaAggregateRouteTag,
       "ospfv3VirtLinkLsdbTable": ospfv3VirtLinkLsdbTable,
       "ospfv3VirtLinkLsdbEntry": ospfv3VirtLinkLsdbEntry,
       "ospfv3VirtLinkLsdbIfAreaId": ospfv3VirtLinkLsdbIfAreaId,
       "ospfv3VirtLinkLsdbIfNeighbor": ospfv3VirtLinkLsdbIfNeighbor,
       "ospfv3VirtLinkLsdbType": ospfv3VirtLinkLsdbType,
       "ospfv3VirtLinkLsdbRouterId": ospfv3VirtLinkLsdbRouterId,
       "ospfv3VirtLinkLsdbLsid": ospfv3VirtLinkLsdbLsid,
       "ospfv3VirtLinkLsdbSequence": ospfv3VirtLinkLsdbSequence,
       "ospfv3VirtLinkLsdbAge": ospfv3VirtLinkLsdbAge,
       "ospfv3VirtLinkLsdbChecksum": ospfv3VirtLinkLsdbChecksum,
       "ospfv3VirtLinkLsdbAdvertisement": ospfv3VirtLinkLsdbAdvertisement,
       "ospfv3VirtLinkLsdbTypeKnown": ospfv3VirtLinkLsdbTypeKnown,
       "ospfv3NotificationEntry": ospfv3NotificationEntry,
       "ospfv3ConfigErrorType": ospfv3ConfigErrorType,
       "ospfv3PacketType": ospfv3PacketType,
       "ospfv3PacketSrc": ospfv3PacketSrc,
       "ospfv3Conformance": ospfv3Conformance,
       "ospfv3Groups": ospfv3Groups,
       "ospfv3BasicGroup": ospfv3BasicGroup,
       "ospfv3AreaGroup": ospfv3AreaGroup,
       "ospfv3AsLsdbGroup": ospfv3AsLsdbGroup,
       "ospfv3AreaLsdbGroup": ospfv3AreaLsdbGroup,
       "ospfv3LinkLsdbGroup": ospfv3LinkLsdbGroup,
       "ospfv3HostGroup": ospfv3HostGroup,
       "ospfv3IfGroup": ospfv3IfGroup,
       "ospfv3VirtIfGroup": ospfv3VirtIfGroup,
       "ospfv3NbrGroup": ospfv3NbrGroup,
       "ospfv3CfgNbrGroup": ospfv3CfgNbrGroup,
       "ospfv3VirtNbrGroup": ospfv3VirtNbrGroup,
       "ospfv3AreaAggregateGroup": ospfv3AreaAggregateGroup,
       "ospfv3VirtLinkLsdbGroup": ospfv3VirtLinkLsdbGroup,
       "ospfv3NotificationObjectGroup": ospfv3NotificationObjectGroup,
       "ospfv3NotificationGroup": ospfv3NotificationGroup,
       "ospfv3Compliances": ospfv3Compliances,
       "ospfv3FullCompliance": ospfv3FullCompliance,
       "ospfv3ReadOnlyCompliance": ospfv3ReadOnlyCompliance}
)

# SNMP MIB module (OSPFV3-MIB-JUNIPER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OSPFV3-MIB-JUNIPER
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:46 2024
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
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(jnxOspfv3Experiment,) = mibBuilder.importSymbols(
    "JUNIPER-EXPERIMENT-MIB",
    "jnxOspfv3Experiment")

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

jnxOspfv3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1)
)
jnxOspfv3MIB.setRevisions(
        ("2006-08-09 12:00",
         "2011-03-30 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxOspfv3UpToRefreshIntervalTc(Integer32, TextualConvention):
    status = "deprecated"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )



class JnxOspfv3DeadIntRangeTc(Integer32, TextualConvention):
    status = "deprecated"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class JnxOspfv3RouterIdTc(Unsigned32, TextualConvention):
    status = "deprecated"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class JnxOspfv3AreaIdTc(Unsigned32, TextualConvention):
    status = "deprecated"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class JnxOspfv3IfInstIdTc(Integer32, TextualConvention):
    status = "deprecated"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_JnxOspfv3Notifications_ObjectIdentity = ObjectIdentity
jnxOspfv3Notifications = _JnxOspfv3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0)
)
_JnxOspfv3Objects_ObjectIdentity = ObjectIdentity
jnxOspfv3Objects = _JnxOspfv3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1)
)
_JnxOspfv3GeneralGroup_ObjectIdentity = ObjectIdentity
jnxOspfv3GeneralGroup = _JnxOspfv3GeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1)
)
_JnxOspfv3RouterId_Type = JnxOspfv3RouterIdTc
_JnxOspfv3RouterId_Object = MibScalar
jnxOspfv3RouterId = _JnxOspfv3RouterId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 1),
    _JnxOspfv3RouterId_Type()
)
jnxOspfv3RouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOspfv3RouterId.setStatus("deprecated")
_JnxOspfv3AdminStat_Type = Status
_JnxOspfv3AdminStat_Object = MibScalar
jnxOspfv3AdminStat = _JnxOspfv3AdminStat_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 2),
    _JnxOspfv3AdminStat_Type()
)
jnxOspfv3AdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOspfv3AdminStat.setStatus("deprecated")


class _JnxOspfv3VersionNumber_Type(Integer32):
    """Custom type jnxOspfv3VersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("version3", 3)
    )


_JnxOspfv3VersionNumber_Type.__name__ = "Integer32"
_JnxOspfv3VersionNumber_Object = MibScalar
jnxOspfv3VersionNumber = _JnxOspfv3VersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 3),
    _JnxOspfv3VersionNumber_Type()
)
jnxOspfv3VersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VersionNumber.setStatus("deprecated")
_JnxOspfv3AreaBdrRtrStatus_Type = TruthValue
_JnxOspfv3AreaBdrRtrStatus_Object = MibScalar
jnxOspfv3AreaBdrRtrStatus = _JnxOspfv3AreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 4),
    _JnxOspfv3AreaBdrRtrStatus_Type()
)
jnxOspfv3AreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaBdrRtrStatus.setStatus("deprecated")
_JnxOspfv3ASBdrRtrStatus_Type = TruthValue
_JnxOspfv3ASBdrRtrStatus_Object = MibScalar
jnxOspfv3ASBdrRtrStatus = _JnxOspfv3ASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 5),
    _JnxOspfv3ASBdrRtrStatus_Type()
)
jnxOspfv3ASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOspfv3ASBdrRtrStatus.setStatus("deprecated")
_JnxOspfv3AsScopeLsaCount_Type = Gauge32
_JnxOspfv3AsScopeLsaCount_Object = MibScalar
jnxOspfv3AsScopeLsaCount = _JnxOspfv3AsScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 6),
    _JnxOspfv3AsScopeLsaCount_Type()
)
jnxOspfv3AsScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AsScopeLsaCount.setStatus("deprecated")
_JnxOspfv3AsScopeLsaCksumSum_Type = Integer32
_JnxOspfv3AsScopeLsaCksumSum_Object = MibScalar
jnxOspfv3AsScopeLsaCksumSum = _JnxOspfv3AsScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 7),
    _JnxOspfv3AsScopeLsaCksumSum_Type()
)
jnxOspfv3AsScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AsScopeLsaCksumSum.setStatus("deprecated")
_JnxOspfv3OriginateNewLsas_Type = Counter32
_JnxOspfv3OriginateNewLsas_Object = MibScalar
jnxOspfv3OriginateNewLsas = _JnxOspfv3OriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 8),
    _JnxOspfv3OriginateNewLsas_Type()
)
jnxOspfv3OriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3OriginateNewLsas.setStatus("deprecated")
_JnxOspfv3RxNewLsas_Type = Counter32
_JnxOspfv3RxNewLsas_Object = MibScalar
jnxOspfv3RxNewLsas = _JnxOspfv3RxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 9),
    _JnxOspfv3RxNewLsas_Type()
)
jnxOspfv3RxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3RxNewLsas.setStatus("deprecated")
_JnxOspfv3ExtLsaCount_Type = Gauge32
_JnxOspfv3ExtLsaCount_Object = MibScalar
jnxOspfv3ExtLsaCount = _JnxOspfv3ExtLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 10),
    _JnxOspfv3ExtLsaCount_Type()
)
jnxOspfv3ExtLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3ExtLsaCount.setStatus("deprecated")


class _JnxOspfv3ExtAreaLsdbLimit_Type(Integer32):
    """Custom type jnxOspfv3ExtAreaLsdbLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_JnxOspfv3ExtAreaLsdbLimit_Type.__name__ = "Integer32"
_JnxOspfv3ExtAreaLsdbLimit_Object = MibScalar
jnxOspfv3ExtAreaLsdbLimit = _JnxOspfv3ExtAreaLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 11),
    _JnxOspfv3ExtAreaLsdbLimit_Type()
)
jnxOspfv3ExtAreaLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOspfv3ExtAreaLsdbLimit.setStatus("deprecated")


class _JnxOspfv3MulticastExtensions_Type(Bits):
    """Custom type jnxOspfv3MulticastExtensions based on Bits"""
    namedValues = NamedValues(
        *(("interAreaMulticast", 1),
          ("interAsMulticast", 2),
          ("intraAreaMulticast", 0))
    )

_JnxOspfv3MulticastExtensions_Type.__name__ = "Bits"
_JnxOspfv3MulticastExtensions_Object = MibScalar
jnxOspfv3MulticastExtensions = _JnxOspfv3MulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 12),
    _JnxOspfv3MulticastExtensions_Type()
)
jnxOspfv3MulticastExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOspfv3MulticastExtensions.setStatus("deprecated")
_JnxOspfv3ExitOverflowInterval_Type = Unsigned32
_JnxOspfv3ExitOverflowInterval_Object = MibScalar
jnxOspfv3ExitOverflowInterval = _JnxOspfv3ExitOverflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 13),
    _JnxOspfv3ExitOverflowInterval_Type()
)
jnxOspfv3ExitOverflowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOspfv3ExitOverflowInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3ExitOverflowInterval.setUnits("seconds")
_JnxOspfv3DemandExtensions_Type = TruthValue
_JnxOspfv3DemandExtensions_Object = MibScalar
jnxOspfv3DemandExtensions = _JnxOspfv3DemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 14),
    _JnxOspfv3DemandExtensions_Type()
)
jnxOspfv3DemandExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOspfv3DemandExtensions.setStatus("deprecated")
_JnxOspfv3ReferenceBandwidth_Type = Unsigned32
_JnxOspfv3ReferenceBandwidth_Object = MibScalar
jnxOspfv3ReferenceBandwidth = _JnxOspfv3ReferenceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 15),
    _JnxOspfv3ReferenceBandwidth_Type()
)
jnxOspfv3ReferenceBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOspfv3ReferenceBandwidth.setStatus("deprecated")


class _JnxOspfv3RestartSupport_Type(Integer32):
    """Custom type jnxOspfv3RestartSupport based on Integer32"""
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


_JnxOspfv3RestartSupport_Type.__name__ = "Integer32"
_JnxOspfv3RestartSupport_Object = MibScalar
jnxOspfv3RestartSupport = _JnxOspfv3RestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 16),
    _JnxOspfv3RestartSupport_Type()
)
jnxOspfv3RestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOspfv3RestartSupport.setStatus("deprecated")
_JnxOspfv3RestartInterval_Type = JnxOspfv3UpToRefreshIntervalTc
_JnxOspfv3RestartInterval_Object = MibScalar
jnxOspfv3RestartInterval = _JnxOspfv3RestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 17),
    _JnxOspfv3RestartInterval_Type()
)
jnxOspfv3RestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOspfv3RestartInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3RestartInterval.setUnits("seconds")


class _JnxOspfv3RestartStatus_Type(Integer32):
    """Custom type jnxOspfv3RestartStatus based on Integer32"""
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


_JnxOspfv3RestartStatus_Type.__name__ = "Integer32"
_JnxOspfv3RestartStatus_Object = MibScalar
jnxOspfv3RestartStatus = _JnxOspfv3RestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 18),
    _JnxOspfv3RestartStatus_Type()
)
jnxOspfv3RestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3RestartStatus.setStatus("deprecated")
_JnxOspfv3RestartAge_Type = JnxOspfv3UpToRefreshIntervalTc
_JnxOspfv3RestartAge_Object = MibScalar
jnxOspfv3RestartAge = _JnxOspfv3RestartAge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 19),
    _JnxOspfv3RestartAge_Type()
)
jnxOspfv3RestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3RestartAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3RestartAge.setUnits("seconds")


class _JnxOspfv3RestartExitRc_Type(Integer32):
    """Custom type jnxOspfv3RestartExitRc based on Integer32"""
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


_JnxOspfv3RestartExitRc_Type.__name__ = "Integer32"
_JnxOspfv3RestartExitRc_Object = MibScalar
jnxOspfv3RestartExitRc = _JnxOspfv3RestartExitRc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 20),
    _JnxOspfv3RestartExitRc_Type()
)
jnxOspfv3RestartExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3RestartExitRc.setStatus("deprecated")


class _JnxOspfv3NotificationEnable_Type(TruthValue):
    """Custom type jnxOspfv3NotificationEnable based on TruthValue"""


_JnxOspfv3NotificationEnable_Object = MibScalar
jnxOspfv3NotificationEnable = _JnxOspfv3NotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 1, 21),
    _JnxOspfv3NotificationEnable_Type()
)
jnxOspfv3NotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOspfv3NotificationEnable.setStatus("deprecated")
_JnxOspfv3AreaTable_Object = MibTable
jnxOspfv3AreaTable = _JnxOspfv3AreaTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxOspfv3AreaTable.setStatus("deprecated")
_JnxOspfv3AreaEntry_Object = MibTableRow
jnxOspfv3AreaEntry = _JnxOspfv3AreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1)
)
jnxOspfv3AreaEntry.setIndexNames(
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaId"),
)
if mibBuilder.loadTexts:
    jnxOspfv3AreaEntry.setStatus("deprecated")
_JnxOspfv3AreaId_Type = JnxOspfv3AreaIdTc
_JnxOspfv3AreaId_Object = MibTableColumn
jnxOspfv3AreaId = _JnxOspfv3AreaId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 1),
    _JnxOspfv3AreaId_Type()
)
jnxOspfv3AreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AreaId.setStatus("deprecated")


class _JnxOspfv3ImportAsExtern_Type(Integer32):
    """Custom type jnxOspfv3ImportAsExtern based on Integer32"""
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


_JnxOspfv3ImportAsExtern_Type.__name__ = "Integer32"
_JnxOspfv3ImportAsExtern_Object = MibTableColumn
jnxOspfv3ImportAsExtern = _JnxOspfv3ImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 2),
    _JnxOspfv3ImportAsExtern_Type()
)
jnxOspfv3ImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3ImportAsExtern.setStatus("deprecated")
_JnxOspfv3AreaSpfRuns_Type = Counter32
_JnxOspfv3AreaSpfRuns_Object = MibTableColumn
jnxOspfv3AreaSpfRuns = _JnxOspfv3AreaSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 3),
    _JnxOspfv3AreaSpfRuns_Type()
)
jnxOspfv3AreaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaSpfRuns.setStatus("deprecated")
_JnxOspfv3AreaBdrRtrCount_Type = Gauge32
_JnxOspfv3AreaBdrRtrCount_Object = MibTableColumn
jnxOspfv3AreaBdrRtrCount = _JnxOspfv3AreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 4),
    _JnxOspfv3AreaBdrRtrCount_Type()
)
jnxOspfv3AreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaBdrRtrCount.setStatus("deprecated")
_JnxOspfv3AreaAsBdrRtrCount_Type = Gauge32
_JnxOspfv3AreaAsBdrRtrCount_Object = MibTableColumn
jnxOspfv3AreaAsBdrRtrCount = _JnxOspfv3AreaAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 5),
    _JnxOspfv3AreaAsBdrRtrCount_Type()
)
jnxOspfv3AreaAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaAsBdrRtrCount.setStatus("deprecated")
_JnxOspfv3AreaScopeLsaCount_Type = Gauge32
_JnxOspfv3AreaScopeLsaCount_Object = MibTableColumn
jnxOspfv3AreaScopeLsaCount = _JnxOspfv3AreaScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 6),
    _JnxOspfv3AreaScopeLsaCount_Type()
)
jnxOspfv3AreaScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaScopeLsaCount.setStatus("deprecated")
_JnxOspfv3AreaScopeLsaCksumSum_Type = Integer32
_JnxOspfv3AreaScopeLsaCksumSum_Object = MibTableColumn
jnxOspfv3AreaScopeLsaCksumSum = _JnxOspfv3AreaScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 7),
    _JnxOspfv3AreaScopeLsaCksumSum_Type()
)
jnxOspfv3AreaScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaScopeLsaCksumSum.setStatus("deprecated")


class _JnxOspfv3AreaSummary_Type(Integer32):
    """Custom type jnxOspfv3AreaSummary based on Integer32"""
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


_JnxOspfv3AreaSummary_Type.__name__ = "Integer32"
_JnxOspfv3AreaSummary_Object = MibTableColumn
jnxOspfv3AreaSummary = _JnxOspfv3AreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 8),
    _JnxOspfv3AreaSummary_Type()
)
jnxOspfv3AreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3AreaSummary.setStatus("deprecated")
_JnxOspfv3AreaStatus_Type = RowStatus
_JnxOspfv3AreaStatus_Object = MibTableColumn
jnxOspfv3AreaStatus = _JnxOspfv3AreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 9),
    _JnxOspfv3AreaStatus_Type()
)
jnxOspfv3AreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3AreaStatus.setStatus("deprecated")
_JnxOspfv3StubMetric_Type = BigMetric
_JnxOspfv3StubMetric_Object = MibTableColumn
jnxOspfv3StubMetric = _JnxOspfv3StubMetric_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 10),
    _JnxOspfv3StubMetric_Type()
)
jnxOspfv3StubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3StubMetric.setStatus("deprecated")


class _JnxOspfv3AreaNssaTranslatorRole_Type(Integer32):
    """Custom type jnxOspfv3AreaNssaTranslatorRole based on Integer32"""
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


_JnxOspfv3AreaNssaTranslatorRole_Type.__name__ = "Integer32"
_JnxOspfv3AreaNssaTranslatorRole_Object = MibTableColumn
jnxOspfv3AreaNssaTranslatorRole = _JnxOspfv3AreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 11),
    _JnxOspfv3AreaNssaTranslatorRole_Type()
)
jnxOspfv3AreaNssaTranslatorRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3AreaNssaTranslatorRole.setStatus("deprecated")


class _JnxOspfv3AreaNssaTranslatorState_Type(Integer32):
    """Custom type jnxOspfv3AreaNssaTranslatorState based on Integer32"""
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


_JnxOspfv3AreaNssaTranslatorState_Type.__name__ = "Integer32"
_JnxOspfv3AreaNssaTranslatorState_Object = MibTableColumn
jnxOspfv3AreaNssaTranslatorState = _JnxOspfv3AreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 12),
    _JnxOspfv3AreaNssaTranslatorState_Type()
)
jnxOspfv3AreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaNssaTranslatorState.setStatus("deprecated")


class _JnxOspfv3AreaNssaTranslatorStabInt_Type(Unsigned32):
    """Custom type jnxOspfv3AreaNssaTranslatorStabInt based on Unsigned32"""
    defaultValue = 40


_JnxOspfv3AreaNssaTranslatorStabInt_Object = MibTableColumn
jnxOspfv3AreaNssaTranslatorStabInt = _JnxOspfv3AreaNssaTranslatorStabInt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 13),
    _JnxOspfv3AreaNssaTranslatorStabInt_Type()
)
jnxOspfv3AreaNssaTranslatorStabInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3AreaNssaTranslatorStabInt.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3AreaNssaTranslatorStabInt.setUnits("seconds")
_JnxOspfv3AreaNssaTranslatorEvents_Type = Counter32
_JnxOspfv3AreaNssaTranslatorEvents_Object = MibTableColumn
jnxOspfv3AreaNssaTranslatorEvents = _JnxOspfv3AreaNssaTranslatorEvents_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 14),
    _JnxOspfv3AreaNssaTranslatorEvents_Type()
)
jnxOspfv3AreaNssaTranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaNssaTranslatorEvents.setStatus("deprecated")


class _JnxOspfv3AreaStubMetricType_Type(Integer32):
    """Custom type jnxOspfv3AreaStubMetricType based on Integer32"""
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


_JnxOspfv3AreaStubMetricType_Type.__name__ = "Integer32"
_JnxOspfv3AreaStubMetricType_Object = MibTableColumn
jnxOspfv3AreaStubMetricType = _JnxOspfv3AreaStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 2, 1, 15),
    _JnxOspfv3AreaStubMetricType_Type()
)
jnxOspfv3AreaStubMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3AreaStubMetricType.setStatus("deprecated")
_JnxOspfv3AsLsdbTable_Object = MibTable
jnxOspfv3AsLsdbTable = _JnxOspfv3AsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbTable.setStatus("deprecated")
_JnxOspfv3AsLsdbEntry_Object = MibTableRow
jnxOspfv3AsLsdbEntry = _JnxOspfv3AsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 3, 1)
)
jnxOspfv3AsLsdbEntry.setIndexNames(
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AsLsdbType"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AsLsdbRouterId"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AsLsdbLsid"),
)
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbEntry.setStatus("deprecated")


class _JnxOspfv3AsLsdbType_Type(Unsigned32):
    """Custom type jnxOspfv3AsLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxOspfv3AsLsdbType_Type.__name__ = "Unsigned32"
_JnxOspfv3AsLsdbType_Object = MibTableColumn
jnxOspfv3AsLsdbType = _JnxOspfv3AsLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 3, 1, 1),
    _JnxOspfv3AsLsdbType_Type()
)
jnxOspfv3AsLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbType.setStatus("deprecated")
_JnxOspfv3AsLsdbRouterId_Type = JnxOspfv3RouterIdTc
_JnxOspfv3AsLsdbRouterId_Object = MibTableColumn
jnxOspfv3AsLsdbRouterId = _JnxOspfv3AsLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 3, 1, 2),
    _JnxOspfv3AsLsdbRouterId_Type()
)
jnxOspfv3AsLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbRouterId.setStatus("deprecated")
_JnxOspfv3AsLsdbLsid_Type = Unsigned32
_JnxOspfv3AsLsdbLsid_Object = MibTableColumn
jnxOspfv3AsLsdbLsid = _JnxOspfv3AsLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 3, 1, 3),
    _JnxOspfv3AsLsdbLsid_Type()
)
jnxOspfv3AsLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbLsid.setStatus("deprecated")
_JnxOspfv3AsLsdbSequence_Type = Integer32
_JnxOspfv3AsLsdbSequence_Object = MibTableColumn
jnxOspfv3AsLsdbSequence = _JnxOspfv3AsLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 3, 1, 4),
    _JnxOspfv3AsLsdbSequence_Type()
)
jnxOspfv3AsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbSequence.setStatus("deprecated")
_JnxOspfv3AsLsdbAge_Type = Integer32
_JnxOspfv3AsLsdbAge_Object = MibTableColumn
jnxOspfv3AsLsdbAge = _JnxOspfv3AsLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 3, 1, 5),
    _JnxOspfv3AsLsdbAge_Type()
)
jnxOspfv3AsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbAge.setUnits("seconds")
_JnxOspfv3AsLsdbChecksum_Type = Integer32
_JnxOspfv3AsLsdbChecksum_Object = MibTableColumn
jnxOspfv3AsLsdbChecksum = _JnxOspfv3AsLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 3, 1, 6),
    _JnxOspfv3AsLsdbChecksum_Type()
)
jnxOspfv3AsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbChecksum.setStatus("deprecated")


class _JnxOspfv3AsLsdbAdvertisement_Type(OctetString):
    """Custom type jnxOspfv3AsLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_JnxOspfv3AsLsdbAdvertisement_Type.__name__ = "OctetString"
_JnxOspfv3AsLsdbAdvertisement_Object = MibTableColumn
jnxOspfv3AsLsdbAdvertisement = _JnxOspfv3AsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 3, 1, 7),
    _JnxOspfv3AsLsdbAdvertisement_Type()
)
jnxOspfv3AsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbAdvertisement.setStatus("deprecated")
_JnxOspfv3AsLsdbTypeKnown_Type = TruthValue
_JnxOspfv3AsLsdbTypeKnown_Object = MibTableColumn
jnxOspfv3AsLsdbTypeKnown = _JnxOspfv3AsLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 3, 1, 8),
    _JnxOspfv3AsLsdbTypeKnown_Type()
)
jnxOspfv3AsLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbTypeKnown.setStatus("deprecated")
_JnxOspfv3AreaLsdbTable_Object = MibTable
jnxOspfv3AreaLsdbTable = _JnxOspfv3AreaLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbTable.setStatus("deprecated")
_JnxOspfv3AreaLsdbEntry_Object = MibTableRow
jnxOspfv3AreaLsdbEntry = _JnxOspfv3AreaLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 4, 1)
)
jnxOspfv3AreaLsdbEntry.setIndexNames(
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaLsdbAreaId"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaLsdbType"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaLsdbRouterId"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaLsdbLsid"),
)
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbEntry.setStatus("deprecated")
_JnxOspfv3AreaLsdbAreaId_Type = JnxOspfv3AreaIdTc
_JnxOspfv3AreaLsdbAreaId_Object = MibTableColumn
jnxOspfv3AreaLsdbAreaId = _JnxOspfv3AreaLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 4, 1, 1),
    _JnxOspfv3AreaLsdbAreaId_Type()
)
jnxOspfv3AreaLsdbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbAreaId.setStatus("deprecated")


class _JnxOspfv3AreaLsdbType_Type(Unsigned32):
    """Custom type jnxOspfv3AreaLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxOspfv3AreaLsdbType_Type.__name__ = "Unsigned32"
_JnxOspfv3AreaLsdbType_Object = MibTableColumn
jnxOspfv3AreaLsdbType = _JnxOspfv3AreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 4, 1, 2),
    _JnxOspfv3AreaLsdbType_Type()
)
jnxOspfv3AreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbType.setStatus("deprecated")
_JnxOspfv3AreaLsdbRouterId_Type = JnxOspfv3RouterIdTc
_JnxOspfv3AreaLsdbRouterId_Object = MibTableColumn
jnxOspfv3AreaLsdbRouterId = _JnxOspfv3AreaLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 4, 1, 3),
    _JnxOspfv3AreaLsdbRouterId_Type()
)
jnxOspfv3AreaLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbRouterId.setStatus("deprecated")
_JnxOspfv3AreaLsdbLsid_Type = Unsigned32
_JnxOspfv3AreaLsdbLsid_Object = MibTableColumn
jnxOspfv3AreaLsdbLsid = _JnxOspfv3AreaLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 4, 1, 4),
    _JnxOspfv3AreaLsdbLsid_Type()
)
jnxOspfv3AreaLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbLsid.setStatus("deprecated")
_JnxOspfv3AreaLsdbSequence_Type = Integer32
_JnxOspfv3AreaLsdbSequence_Object = MibTableColumn
jnxOspfv3AreaLsdbSequence = _JnxOspfv3AreaLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 4, 1, 5),
    _JnxOspfv3AreaLsdbSequence_Type()
)
jnxOspfv3AreaLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbSequence.setStatus("deprecated")
_JnxOspfv3AreaLsdbAge_Type = Integer32
_JnxOspfv3AreaLsdbAge_Object = MibTableColumn
jnxOspfv3AreaLsdbAge = _JnxOspfv3AreaLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 4, 1, 6),
    _JnxOspfv3AreaLsdbAge_Type()
)
jnxOspfv3AreaLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbAge.setUnits("seconds")
_JnxOspfv3AreaLsdbChecksum_Type = Integer32
_JnxOspfv3AreaLsdbChecksum_Object = MibTableColumn
jnxOspfv3AreaLsdbChecksum = _JnxOspfv3AreaLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 4, 1, 7),
    _JnxOspfv3AreaLsdbChecksum_Type()
)
jnxOspfv3AreaLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbChecksum.setStatus("deprecated")


class _JnxOspfv3AreaLsdbAdvertisement_Type(OctetString):
    """Custom type jnxOspfv3AreaLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_JnxOspfv3AreaLsdbAdvertisement_Type.__name__ = "OctetString"
_JnxOspfv3AreaLsdbAdvertisement_Object = MibTableColumn
jnxOspfv3AreaLsdbAdvertisement = _JnxOspfv3AreaLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 4, 1, 8),
    _JnxOspfv3AreaLsdbAdvertisement_Type()
)
jnxOspfv3AreaLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbAdvertisement.setStatus("deprecated")
_JnxOspfv3AreaLsdbTypeKnown_Type = TruthValue
_JnxOspfv3AreaLsdbTypeKnown_Object = MibTableColumn
jnxOspfv3AreaLsdbTypeKnown = _JnxOspfv3AreaLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 4, 1, 9),
    _JnxOspfv3AreaLsdbTypeKnown_Type()
)
jnxOspfv3AreaLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbTypeKnown.setStatus("deprecated")
_JnxOspfv3LinkLsdbTable_Object = MibTable
jnxOspfv3LinkLsdbTable = _JnxOspfv3LinkLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbTable.setStatus("deprecated")
_JnxOspfv3LinkLsdbEntry_Object = MibTableRow
jnxOspfv3LinkLsdbEntry = _JnxOspfv3LinkLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5, 1)
)
jnxOspfv3LinkLsdbEntry.setIndexNames(
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3LinkLsdbIfIndex"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3LinkLsdbIfInstId"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3LinkLsdbType"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3LinkLsdbRouterId"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3LinkLsdbLsid"),
)
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbEntry.setStatus("deprecated")
_JnxOspfv3LinkLsdbIfIndex_Type = InterfaceIndex
_JnxOspfv3LinkLsdbIfIndex_Object = MibTableColumn
jnxOspfv3LinkLsdbIfIndex = _JnxOspfv3LinkLsdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5, 1, 1),
    _JnxOspfv3LinkLsdbIfIndex_Type()
)
jnxOspfv3LinkLsdbIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbIfIndex.setStatus("deprecated")
_JnxOspfv3LinkLsdbIfInstId_Type = JnxOspfv3IfInstIdTc
_JnxOspfv3LinkLsdbIfInstId_Object = MibTableColumn
jnxOspfv3LinkLsdbIfInstId = _JnxOspfv3LinkLsdbIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5, 1, 2),
    _JnxOspfv3LinkLsdbIfInstId_Type()
)
jnxOspfv3LinkLsdbIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbIfInstId.setStatus("deprecated")


class _JnxOspfv3LinkLsdbType_Type(Unsigned32):
    """Custom type jnxOspfv3LinkLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxOspfv3LinkLsdbType_Type.__name__ = "Unsigned32"
_JnxOspfv3LinkLsdbType_Object = MibTableColumn
jnxOspfv3LinkLsdbType = _JnxOspfv3LinkLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5, 1, 3),
    _JnxOspfv3LinkLsdbType_Type()
)
jnxOspfv3LinkLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbType.setStatus("deprecated")
_JnxOspfv3LinkLsdbRouterId_Type = JnxOspfv3RouterIdTc
_JnxOspfv3LinkLsdbRouterId_Object = MibTableColumn
jnxOspfv3LinkLsdbRouterId = _JnxOspfv3LinkLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5, 1, 4),
    _JnxOspfv3LinkLsdbRouterId_Type()
)
jnxOspfv3LinkLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbRouterId.setStatus("deprecated")
_JnxOspfv3LinkLsdbLsid_Type = Unsigned32
_JnxOspfv3LinkLsdbLsid_Object = MibTableColumn
jnxOspfv3LinkLsdbLsid = _JnxOspfv3LinkLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5, 1, 5),
    _JnxOspfv3LinkLsdbLsid_Type()
)
jnxOspfv3LinkLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbLsid.setStatus("deprecated")
_JnxOspfv3LinkLsdbSequence_Type = Integer32
_JnxOspfv3LinkLsdbSequence_Object = MibTableColumn
jnxOspfv3LinkLsdbSequence = _JnxOspfv3LinkLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5, 1, 6),
    _JnxOspfv3LinkLsdbSequence_Type()
)
jnxOspfv3LinkLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbSequence.setStatus("deprecated")
_JnxOspfv3LinkLsdbAge_Type = Integer32
_JnxOspfv3LinkLsdbAge_Object = MibTableColumn
jnxOspfv3LinkLsdbAge = _JnxOspfv3LinkLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5, 1, 7),
    _JnxOspfv3LinkLsdbAge_Type()
)
jnxOspfv3LinkLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbAge.setUnits("seconds")
_JnxOspfv3LinkLsdbChecksum_Type = Integer32
_JnxOspfv3LinkLsdbChecksum_Object = MibTableColumn
jnxOspfv3LinkLsdbChecksum = _JnxOspfv3LinkLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5, 1, 8),
    _JnxOspfv3LinkLsdbChecksum_Type()
)
jnxOspfv3LinkLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbChecksum.setStatus("deprecated")


class _JnxOspfv3LinkLsdbAdvertisement_Type(OctetString):
    """Custom type jnxOspfv3LinkLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_JnxOspfv3LinkLsdbAdvertisement_Type.__name__ = "OctetString"
_JnxOspfv3LinkLsdbAdvertisement_Object = MibTableColumn
jnxOspfv3LinkLsdbAdvertisement = _JnxOspfv3LinkLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5, 1, 9),
    _JnxOspfv3LinkLsdbAdvertisement_Type()
)
jnxOspfv3LinkLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbAdvertisement.setStatus("deprecated")
_JnxOspfv3LinkLsdbTypeKnown_Type = TruthValue
_JnxOspfv3LinkLsdbTypeKnown_Object = MibTableColumn
jnxOspfv3LinkLsdbTypeKnown = _JnxOspfv3LinkLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 5, 1, 10),
    _JnxOspfv3LinkLsdbTypeKnown_Type()
)
jnxOspfv3LinkLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbTypeKnown.setStatus("deprecated")
_JnxOspfv3HostTable_Object = MibTable
jnxOspfv3HostTable = _JnxOspfv3HostTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    jnxOspfv3HostTable.setStatus("deprecated")
_JnxOspfv3HostEntry_Object = MibTableRow
jnxOspfv3HostEntry = _JnxOspfv3HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 6, 1)
)
jnxOspfv3HostEntry.setIndexNames(
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3HostAddressType"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3HostAddress"),
)
if mibBuilder.loadTexts:
    jnxOspfv3HostEntry.setStatus("deprecated")
_JnxOspfv3HostAddressType_Type = InetAddressType
_JnxOspfv3HostAddressType_Object = MibTableColumn
jnxOspfv3HostAddressType = _JnxOspfv3HostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 6, 1, 1),
    _JnxOspfv3HostAddressType_Type()
)
jnxOspfv3HostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3HostAddressType.setStatus("deprecated")


class _JnxOspfv3HostAddress_Type(InetAddress):
    """Custom type jnxOspfv3HostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_JnxOspfv3HostAddress_Type.__name__ = "InetAddress"
_JnxOspfv3HostAddress_Object = MibTableColumn
jnxOspfv3HostAddress = _JnxOspfv3HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 6, 1, 2),
    _JnxOspfv3HostAddress_Type()
)
jnxOspfv3HostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3HostAddress.setStatus("deprecated")
_JnxOspfv3HostMetric_Type = Metric
_JnxOspfv3HostMetric_Object = MibTableColumn
jnxOspfv3HostMetric = _JnxOspfv3HostMetric_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 6, 1, 3),
    _JnxOspfv3HostMetric_Type()
)
jnxOspfv3HostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3HostMetric.setStatus("deprecated")
_JnxOspfv3HostStatus_Type = RowStatus
_JnxOspfv3HostStatus_Object = MibTableColumn
jnxOspfv3HostStatus = _JnxOspfv3HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 6, 1, 4),
    _JnxOspfv3HostStatus_Type()
)
jnxOspfv3HostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3HostStatus.setStatus("deprecated")
_JnxOspfv3HostAreaID_Type = JnxOspfv3AreaIdTc
_JnxOspfv3HostAreaID_Object = MibTableColumn
jnxOspfv3HostAreaID = _JnxOspfv3HostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 6, 1, 5),
    _JnxOspfv3HostAreaID_Type()
)
jnxOspfv3HostAreaID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3HostAreaID.setStatus("deprecated")
_JnxOspfv3IfTable_Object = MibTable
jnxOspfv3IfTable = _JnxOspfv3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    jnxOspfv3IfTable.setStatus("deprecated")
_JnxOspfv3IfEntry_Object = MibTableRow
jnxOspfv3IfEntry = _JnxOspfv3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1)
)
jnxOspfv3IfEntry.setIndexNames(
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3IfIndex"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3IfInstId"),
)
if mibBuilder.loadTexts:
    jnxOspfv3IfEntry.setStatus("deprecated")
_JnxOspfv3IfIndex_Type = InterfaceIndex
_JnxOspfv3IfIndex_Object = MibTableColumn
jnxOspfv3IfIndex = _JnxOspfv3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 1),
    _JnxOspfv3IfIndex_Type()
)
jnxOspfv3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3IfIndex.setStatus("deprecated")
_JnxOspfv3IfInstId_Type = JnxOspfv3IfInstIdTc
_JnxOspfv3IfInstId_Object = MibTableColumn
jnxOspfv3IfInstId = _JnxOspfv3IfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 2),
    _JnxOspfv3IfInstId_Type()
)
jnxOspfv3IfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3IfInstId.setStatus("deprecated")


class _JnxOspfv3IfAreaId_Type(JnxOspfv3AreaIdTc):
    """Custom type jnxOspfv3IfAreaId based on JnxOspfv3AreaIdTc"""
    defaultValue = 0


_JnxOspfv3IfAreaId_Object = MibTableColumn
jnxOspfv3IfAreaId = _JnxOspfv3IfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 3),
    _JnxOspfv3IfAreaId_Type()
)
jnxOspfv3IfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfAreaId.setStatus("deprecated")


class _JnxOspfv3IfType_Type(Integer32):
    """Custom type jnxOspfv3IfType based on Integer32"""
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


_JnxOspfv3IfType_Type.__name__ = "Integer32"
_JnxOspfv3IfType_Object = MibTableColumn
jnxOspfv3IfType = _JnxOspfv3IfType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 4),
    _JnxOspfv3IfType_Type()
)
jnxOspfv3IfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfType.setStatus("deprecated")


class _JnxOspfv3IfAdminStat_Type(Status):
    """Custom type jnxOspfv3IfAdminStat based on Status"""


_JnxOspfv3IfAdminStat_Object = MibTableColumn
jnxOspfv3IfAdminStat = _JnxOspfv3IfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 5),
    _JnxOspfv3IfAdminStat_Type()
)
jnxOspfv3IfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfAdminStat.setStatus("deprecated")


class _JnxOspfv3IfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type jnxOspfv3IfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_JnxOspfv3IfRtrPriority_Object = MibTableColumn
jnxOspfv3IfRtrPriority = _JnxOspfv3IfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 6),
    _JnxOspfv3IfRtrPriority_Type()
)
jnxOspfv3IfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfRtrPriority.setStatus("deprecated")


class _JnxOspfv3IfTransitDelay_Type(JnxOspfv3UpToRefreshIntervalTc):
    """Custom type jnxOspfv3IfTransitDelay based on JnxOspfv3UpToRefreshIntervalTc"""
    defaultValue = 1


_JnxOspfv3IfTransitDelay_Object = MibTableColumn
jnxOspfv3IfTransitDelay = _JnxOspfv3IfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 7),
    _JnxOspfv3IfTransitDelay_Type()
)
jnxOspfv3IfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfTransitDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3IfTransitDelay.setUnits("seconds")


class _JnxOspfv3IfRetransInterval_Type(JnxOspfv3UpToRefreshIntervalTc):
    """Custom type jnxOspfv3IfRetransInterval based on JnxOspfv3UpToRefreshIntervalTc"""
    defaultValue = 5


_JnxOspfv3IfRetransInterval_Object = MibTableColumn
jnxOspfv3IfRetransInterval = _JnxOspfv3IfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 8),
    _JnxOspfv3IfRetransInterval_Type()
)
jnxOspfv3IfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfRetransInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3IfRetransInterval.setUnits("seconds")


class _JnxOspfv3IfHelloInterval_Type(HelloRange):
    """Custom type jnxOspfv3IfHelloInterval based on HelloRange"""
    defaultValue = 10


_JnxOspfv3IfHelloInterval_Object = MibTableColumn
jnxOspfv3IfHelloInterval = _JnxOspfv3IfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 9),
    _JnxOspfv3IfHelloInterval_Type()
)
jnxOspfv3IfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfHelloInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3IfHelloInterval.setUnits("seconds")


class _JnxOspfv3IfRtrDeadInterval_Type(JnxOspfv3DeadIntRangeTc):
    """Custom type jnxOspfv3IfRtrDeadInterval based on JnxOspfv3DeadIntRangeTc"""
    defaultValue = 40


_JnxOspfv3IfRtrDeadInterval_Object = MibTableColumn
jnxOspfv3IfRtrDeadInterval = _JnxOspfv3IfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 10),
    _JnxOspfv3IfRtrDeadInterval_Type()
)
jnxOspfv3IfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfRtrDeadInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3IfRtrDeadInterval.setUnits("seconds")


class _JnxOspfv3IfPollInterval_Type(Unsigned32):
    """Custom type jnxOspfv3IfPollInterval based on Unsigned32"""
    defaultValue = 120


_JnxOspfv3IfPollInterval_Object = MibTableColumn
jnxOspfv3IfPollInterval = _JnxOspfv3IfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 11),
    _JnxOspfv3IfPollInterval_Type()
)
jnxOspfv3IfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfPollInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3IfPollInterval.setUnits("seconds")


class _JnxOspfv3IfState_Type(Integer32):
    """Custom type jnxOspfv3IfState based on Integer32"""
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


_JnxOspfv3IfState_Type.__name__ = "Integer32"
_JnxOspfv3IfState_Object = MibTableColumn
jnxOspfv3IfState = _JnxOspfv3IfState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 12),
    _JnxOspfv3IfState_Type()
)
jnxOspfv3IfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3IfState.setStatus("deprecated")
_JnxOspfv3IfDesignatedRouter_Type = JnxOspfv3RouterIdTc
_JnxOspfv3IfDesignatedRouter_Object = MibTableColumn
jnxOspfv3IfDesignatedRouter = _JnxOspfv3IfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 13),
    _JnxOspfv3IfDesignatedRouter_Type()
)
jnxOspfv3IfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3IfDesignatedRouter.setStatus("deprecated")
_JnxOspfv3IfBackupDesignatedRouter_Type = JnxOspfv3RouterIdTc
_JnxOspfv3IfBackupDesignatedRouter_Object = MibTableColumn
jnxOspfv3IfBackupDesignatedRouter = _JnxOspfv3IfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 14),
    _JnxOspfv3IfBackupDesignatedRouter_Type()
)
jnxOspfv3IfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3IfBackupDesignatedRouter.setStatus("deprecated")
_JnxOspfv3IfEvents_Type = Counter32
_JnxOspfv3IfEvents_Object = MibTableColumn
jnxOspfv3IfEvents = _JnxOspfv3IfEvents_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 15),
    _JnxOspfv3IfEvents_Type()
)
jnxOspfv3IfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3IfEvents.setStatus("deprecated")
_JnxOspfv3IfStatus_Type = RowStatus
_JnxOspfv3IfStatus_Object = MibTableColumn
jnxOspfv3IfStatus = _JnxOspfv3IfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 16),
    _JnxOspfv3IfStatus_Type()
)
jnxOspfv3IfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfStatus.setStatus("deprecated")


class _JnxOspfv3IfMulticastForwarding_Type(Integer32):
    """Custom type jnxOspfv3IfMulticastForwarding based on Integer32"""
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


_JnxOspfv3IfMulticastForwarding_Type.__name__ = "Integer32"
_JnxOspfv3IfMulticastForwarding_Object = MibTableColumn
jnxOspfv3IfMulticastForwarding = _JnxOspfv3IfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 17),
    _JnxOspfv3IfMulticastForwarding_Type()
)
jnxOspfv3IfMulticastForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfMulticastForwarding.setStatus("deprecated")


class _JnxOspfv3IfDemand_Type(TruthValue):
    """Custom type jnxOspfv3IfDemand based on TruthValue"""


_JnxOspfv3IfDemand_Object = MibTableColumn
jnxOspfv3IfDemand = _JnxOspfv3IfDemand_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 18),
    _JnxOspfv3IfDemand_Type()
)
jnxOspfv3IfDemand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfDemand.setStatus("deprecated")
_JnxOspfv3IfMetricValue_Type = Metric
_JnxOspfv3IfMetricValue_Object = MibTableColumn
jnxOspfv3IfMetricValue = _JnxOspfv3IfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 19),
    _JnxOspfv3IfMetricValue_Type()
)
jnxOspfv3IfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfMetricValue.setStatus("deprecated")
_JnxOspfv3IfLinkScopeLsaCount_Type = Gauge32
_JnxOspfv3IfLinkScopeLsaCount_Object = MibTableColumn
jnxOspfv3IfLinkScopeLsaCount = _JnxOspfv3IfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 20),
    _JnxOspfv3IfLinkScopeLsaCount_Type()
)
jnxOspfv3IfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3IfLinkScopeLsaCount.setStatus("deprecated")
_JnxOspfv3IfLinkLsaCksumSum_Type = Integer32
_JnxOspfv3IfLinkLsaCksumSum_Object = MibTableColumn
jnxOspfv3IfLinkLsaCksumSum = _JnxOspfv3IfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 21),
    _JnxOspfv3IfLinkLsaCksumSum_Type()
)
jnxOspfv3IfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3IfLinkLsaCksumSum.setStatus("deprecated")


class _JnxOspfv3IfDemandNbrProbe_Type(TruthValue):
    """Custom type jnxOspfv3IfDemandNbrProbe based on TruthValue"""


_JnxOspfv3IfDemandNbrProbe_Object = MibTableColumn
jnxOspfv3IfDemandNbrProbe = _JnxOspfv3IfDemandNbrProbe_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 22),
    _JnxOspfv3IfDemandNbrProbe_Type()
)
jnxOspfv3IfDemandNbrProbe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfDemandNbrProbe.setStatus("deprecated")


class _JnxOspfv3IfDemandNbrProbeRetxLimit_Type(Unsigned32):
    """Custom type jnxOspfv3IfDemandNbrProbeRetxLimit based on Unsigned32"""
    defaultValue = 10


_JnxOspfv3IfDemandNbrProbeRetxLimit_Object = MibTableColumn
jnxOspfv3IfDemandNbrProbeRetxLimit = _JnxOspfv3IfDemandNbrProbeRetxLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 23),
    _JnxOspfv3IfDemandNbrProbeRetxLimit_Type()
)
jnxOspfv3IfDemandNbrProbeRetxLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfDemandNbrProbeRetxLimit.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3IfDemandNbrProbeRetxLimit.setUnits("seconds")


class _JnxOspfv3IfDemandNbrProbeInterval_Type(Unsigned32):
    """Custom type jnxOspfv3IfDemandNbrProbeInterval based on Unsigned32"""
    defaultValue = 120


_JnxOspfv3IfDemandNbrProbeInterval_Object = MibTableColumn
jnxOspfv3IfDemandNbrProbeInterval = _JnxOspfv3IfDemandNbrProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 7, 1, 24),
    _JnxOspfv3IfDemandNbrProbeInterval_Type()
)
jnxOspfv3IfDemandNbrProbeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3IfDemandNbrProbeInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3IfDemandNbrProbeInterval.setUnits("seconds")
_JnxOspfv3VirtIfTable_Object = MibTable
jnxOspfv3VirtIfTable = _JnxOspfv3VirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfTable.setStatus("deprecated")
_JnxOspfv3VirtIfEntry_Object = MibTableRow
jnxOspfv3VirtIfEntry = _JnxOspfv3VirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1)
)
jnxOspfv3VirtIfEntry.setIndexNames(
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfAreaId"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfEntry.setStatus("deprecated")
_JnxOspfv3VirtIfAreaId_Type = JnxOspfv3AreaIdTc
_JnxOspfv3VirtIfAreaId_Object = MibTableColumn
jnxOspfv3VirtIfAreaId = _JnxOspfv3VirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 1),
    _JnxOspfv3VirtIfAreaId_Type()
)
jnxOspfv3VirtIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfAreaId.setStatus("deprecated")
_JnxOspfv3VirtIfNeighbor_Type = JnxOspfv3RouterIdTc
_JnxOspfv3VirtIfNeighbor_Object = MibTableColumn
jnxOspfv3VirtIfNeighbor = _JnxOspfv3VirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 2),
    _JnxOspfv3VirtIfNeighbor_Type()
)
jnxOspfv3VirtIfNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfNeighbor.setStatus("deprecated")
_JnxOspfv3VirtIfIndex_Type = InterfaceIndex
_JnxOspfv3VirtIfIndex_Object = MibTableColumn
jnxOspfv3VirtIfIndex = _JnxOspfv3VirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 3),
    _JnxOspfv3VirtIfIndex_Type()
)
jnxOspfv3VirtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfIndex.setStatus("deprecated")


class _JnxOspfv3VirtIfInstId_Type(JnxOspfv3IfInstIdTc):
    """Custom type jnxOspfv3VirtIfInstId based on JnxOspfv3IfInstIdTc"""
    defaultValue = 0


_JnxOspfv3VirtIfInstId_Object = MibTableColumn
jnxOspfv3VirtIfInstId = _JnxOspfv3VirtIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 4),
    _JnxOspfv3VirtIfInstId_Type()
)
jnxOspfv3VirtIfInstId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfInstId.setStatus("deprecated")


class _JnxOspfv3VirtIfTransitDelay_Type(JnxOspfv3UpToRefreshIntervalTc):
    """Custom type jnxOspfv3VirtIfTransitDelay based on JnxOspfv3UpToRefreshIntervalTc"""
    defaultValue = 1


_JnxOspfv3VirtIfTransitDelay_Object = MibTableColumn
jnxOspfv3VirtIfTransitDelay = _JnxOspfv3VirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 5),
    _JnxOspfv3VirtIfTransitDelay_Type()
)
jnxOspfv3VirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfTransitDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfTransitDelay.setUnits("seconds")


class _JnxOspfv3VirtIfRetransInterval_Type(JnxOspfv3UpToRefreshIntervalTc):
    """Custom type jnxOspfv3VirtIfRetransInterval based on JnxOspfv3UpToRefreshIntervalTc"""
    defaultValue = 5


_JnxOspfv3VirtIfRetransInterval_Object = MibTableColumn
jnxOspfv3VirtIfRetransInterval = _JnxOspfv3VirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 6),
    _JnxOspfv3VirtIfRetransInterval_Type()
)
jnxOspfv3VirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfRetransInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfRetransInterval.setUnits("seconds")


class _JnxOspfv3VirtIfHelloInterval_Type(HelloRange):
    """Custom type jnxOspfv3VirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_JnxOspfv3VirtIfHelloInterval_Object = MibTableColumn
jnxOspfv3VirtIfHelloInterval = _JnxOspfv3VirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 7),
    _JnxOspfv3VirtIfHelloInterval_Type()
)
jnxOspfv3VirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfHelloInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfHelloInterval.setUnits("seconds")


class _JnxOspfv3VirtIfRtrDeadInterval_Type(JnxOspfv3DeadIntRangeTc):
    """Custom type jnxOspfv3VirtIfRtrDeadInterval based on JnxOspfv3DeadIntRangeTc"""
    defaultValue = 60


_JnxOspfv3VirtIfRtrDeadInterval_Object = MibTableColumn
jnxOspfv3VirtIfRtrDeadInterval = _JnxOspfv3VirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 8),
    _JnxOspfv3VirtIfRtrDeadInterval_Type()
)
jnxOspfv3VirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfRtrDeadInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfRtrDeadInterval.setUnits("seconds")


class _JnxOspfv3VirtIfState_Type(Integer32):
    """Custom type jnxOspfv3VirtIfState based on Integer32"""
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


_JnxOspfv3VirtIfState_Type.__name__ = "Integer32"
_JnxOspfv3VirtIfState_Object = MibTableColumn
jnxOspfv3VirtIfState = _JnxOspfv3VirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 9),
    _JnxOspfv3VirtIfState_Type()
)
jnxOspfv3VirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfState.setStatus("deprecated")
_JnxOspfv3VirtIfEvents_Type = Counter32
_JnxOspfv3VirtIfEvents_Object = MibTableColumn
jnxOspfv3VirtIfEvents = _JnxOspfv3VirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 10),
    _JnxOspfv3VirtIfEvents_Type()
)
jnxOspfv3VirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfEvents.setStatus("deprecated")
_JnxOspfv3VirtIfStatus_Type = RowStatus
_JnxOspfv3VirtIfStatus_Object = MibTableColumn
jnxOspfv3VirtIfStatus = _JnxOspfv3VirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 11),
    _JnxOspfv3VirtIfStatus_Type()
)
jnxOspfv3VirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfStatus.setStatus("deprecated")
_JnxOspfv3VirtIfLinkScopeLsaCount_Type = Gauge32
_JnxOspfv3VirtIfLinkScopeLsaCount_Object = MibTableColumn
jnxOspfv3VirtIfLinkScopeLsaCount = _JnxOspfv3VirtIfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 12),
    _JnxOspfv3VirtIfLinkScopeLsaCount_Type()
)
jnxOspfv3VirtIfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfLinkScopeLsaCount.setStatus("deprecated")
_JnxOspfv3VirtIfLinkLsaCksumSum_Type = Integer32
_JnxOspfv3VirtIfLinkLsaCksumSum_Object = MibTableColumn
jnxOspfv3VirtIfLinkLsaCksumSum = _JnxOspfv3VirtIfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 8, 1, 13),
    _JnxOspfv3VirtIfLinkLsaCksumSum_Type()
)
jnxOspfv3VirtIfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfLinkLsaCksumSum.setStatus("deprecated")
_JnxOspfv3NbrTable_Object = MibTable
jnxOspfv3NbrTable = _JnxOspfv3NbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    jnxOspfv3NbrTable.setStatus("deprecated")
_JnxOspfv3NbrEntry_Object = MibTableRow
jnxOspfv3NbrEntry = _JnxOspfv3NbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1)
)
jnxOspfv3NbrEntry.setIndexNames(
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrIfIndex"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrIfInstId"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrRtrId"),
)
if mibBuilder.loadTexts:
    jnxOspfv3NbrEntry.setStatus("deprecated")
_JnxOspfv3NbrIfIndex_Type = InterfaceIndex
_JnxOspfv3NbrIfIndex_Object = MibTableColumn
jnxOspfv3NbrIfIndex = _JnxOspfv3NbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 1),
    _JnxOspfv3NbrIfIndex_Type()
)
jnxOspfv3NbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3NbrIfIndex.setStatus("deprecated")
_JnxOspfv3NbrIfInstId_Type = JnxOspfv3IfInstIdTc
_JnxOspfv3NbrIfInstId_Object = MibTableColumn
jnxOspfv3NbrIfInstId = _JnxOspfv3NbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 2),
    _JnxOspfv3NbrIfInstId_Type()
)
jnxOspfv3NbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3NbrIfInstId.setStatus("deprecated")
_JnxOspfv3NbrRtrId_Type = JnxOspfv3RouterIdTc
_JnxOspfv3NbrRtrId_Object = MibTableColumn
jnxOspfv3NbrRtrId = _JnxOspfv3NbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 3),
    _JnxOspfv3NbrRtrId_Type()
)
jnxOspfv3NbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3NbrRtrId.setStatus("deprecated")
_JnxOspfv3NbrAddressType_Type = InetAddressType
_JnxOspfv3NbrAddressType_Object = MibTableColumn
jnxOspfv3NbrAddressType = _JnxOspfv3NbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 4),
    _JnxOspfv3NbrAddressType_Type()
)
jnxOspfv3NbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrAddressType.setStatus("deprecated")


class _JnxOspfv3NbrAddress_Type(InetAddress):
    """Custom type jnxOspfv3NbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_JnxOspfv3NbrAddress_Type.__name__ = "InetAddress"
_JnxOspfv3NbrAddress_Object = MibTableColumn
jnxOspfv3NbrAddress = _JnxOspfv3NbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 5),
    _JnxOspfv3NbrAddress_Type()
)
jnxOspfv3NbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrAddress.setStatus("deprecated")
_JnxOspfv3NbrOptions_Type = Integer32
_JnxOspfv3NbrOptions_Object = MibTableColumn
jnxOspfv3NbrOptions = _JnxOspfv3NbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 6),
    _JnxOspfv3NbrOptions_Type()
)
jnxOspfv3NbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrOptions.setStatus("deprecated")
_JnxOspfv3NbrPriority_Type = DesignatedRouterPriority
_JnxOspfv3NbrPriority_Object = MibTableColumn
jnxOspfv3NbrPriority = _JnxOspfv3NbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 7),
    _JnxOspfv3NbrPriority_Type()
)
jnxOspfv3NbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrPriority.setStatus("deprecated")


class _JnxOspfv3NbrState_Type(Integer32):
    """Custom type jnxOspfv3NbrState based on Integer32"""
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


_JnxOspfv3NbrState_Type.__name__ = "Integer32"
_JnxOspfv3NbrState_Object = MibTableColumn
jnxOspfv3NbrState = _JnxOspfv3NbrState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 8),
    _JnxOspfv3NbrState_Type()
)
jnxOspfv3NbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrState.setStatus("deprecated")
_JnxOspfv3NbrEvents_Type = Counter32
_JnxOspfv3NbrEvents_Object = MibTableColumn
jnxOspfv3NbrEvents = _JnxOspfv3NbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 9),
    _JnxOspfv3NbrEvents_Type()
)
jnxOspfv3NbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrEvents.setStatus("deprecated")
_JnxOspfv3NbrLsRetransQLen_Type = Gauge32
_JnxOspfv3NbrLsRetransQLen_Object = MibTableColumn
jnxOspfv3NbrLsRetransQLen = _JnxOspfv3NbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 10),
    _JnxOspfv3NbrLsRetransQLen_Type()
)
jnxOspfv3NbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrLsRetransQLen.setStatus("deprecated")
_JnxOspfv3NbrHelloSuppressed_Type = TruthValue
_JnxOspfv3NbrHelloSuppressed_Object = MibTableColumn
jnxOspfv3NbrHelloSuppressed = _JnxOspfv3NbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 11),
    _JnxOspfv3NbrHelloSuppressed_Type()
)
jnxOspfv3NbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrHelloSuppressed.setStatus("deprecated")
_JnxOspfv3NbrIfId_Type = InterfaceIndex
_JnxOspfv3NbrIfId_Object = MibTableColumn
jnxOspfv3NbrIfId = _JnxOspfv3NbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 12),
    _JnxOspfv3NbrIfId_Type()
)
jnxOspfv3NbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrIfId.setStatus("deprecated")


class _JnxOspfv3NbrRestartHelperStatus_Type(Integer32):
    """Custom type jnxOspfv3NbrRestartHelperStatus based on Integer32"""
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


_JnxOspfv3NbrRestartHelperStatus_Type.__name__ = "Integer32"
_JnxOspfv3NbrRestartHelperStatus_Object = MibTableColumn
jnxOspfv3NbrRestartHelperStatus = _JnxOspfv3NbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 13),
    _JnxOspfv3NbrRestartHelperStatus_Type()
)
jnxOspfv3NbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrRestartHelperStatus.setStatus("deprecated")
_JnxOspfv3NbrRestartHelperAge_Type = JnxOspfv3UpToRefreshIntervalTc
_JnxOspfv3NbrRestartHelperAge_Object = MibTableColumn
jnxOspfv3NbrRestartHelperAge = _JnxOspfv3NbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 14),
    _JnxOspfv3NbrRestartHelperAge_Type()
)
jnxOspfv3NbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrRestartHelperAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3NbrRestartHelperAge.setUnits("seconds")


class _JnxOspfv3NbrRestartHelperExitRc_Type(Integer32):
    """Custom type jnxOspfv3NbrRestartHelperExitRc based on Integer32"""
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


_JnxOspfv3NbrRestartHelperExitRc_Type.__name__ = "Integer32"
_JnxOspfv3NbrRestartHelperExitRc_Object = MibTableColumn
jnxOspfv3NbrRestartHelperExitRc = _JnxOspfv3NbrRestartHelperExitRc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 9, 1, 15),
    _JnxOspfv3NbrRestartHelperExitRc_Type()
)
jnxOspfv3NbrRestartHelperExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3NbrRestartHelperExitRc.setStatus("deprecated")
_JnxOspfv3CfgNbrTable_Object = MibTable
jnxOspfv3CfgNbrTable = _JnxOspfv3CfgNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    jnxOspfv3CfgNbrTable.setStatus("deprecated")
_JnxOspfv3CfgNbrEntry_Object = MibTableRow
jnxOspfv3CfgNbrEntry = _JnxOspfv3CfgNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 10, 1)
)
jnxOspfv3CfgNbrEntry.setIndexNames(
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3CfgNbrIfIndex"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3CfgNbrIfInstId"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3CfgNbrAddressType"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3CfgNbrAddress"),
)
if mibBuilder.loadTexts:
    jnxOspfv3CfgNbrEntry.setStatus("deprecated")
_JnxOspfv3CfgNbrIfIndex_Type = InterfaceIndex
_JnxOspfv3CfgNbrIfIndex_Object = MibTableColumn
jnxOspfv3CfgNbrIfIndex = _JnxOspfv3CfgNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 10, 1, 1),
    _JnxOspfv3CfgNbrIfIndex_Type()
)
jnxOspfv3CfgNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3CfgNbrIfIndex.setStatus("deprecated")
_JnxOspfv3CfgNbrIfInstId_Type = JnxOspfv3IfInstIdTc
_JnxOspfv3CfgNbrIfInstId_Object = MibTableColumn
jnxOspfv3CfgNbrIfInstId = _JnxOspfv3CfgNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 10, 1, 2),
    _JnxOspfv3CfgNbrIfInstId_Type()
)
jnxOspfv3CfgNbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3CfgNbrIfInstId.setStatus("deprecated")
_JnxOspfv3CfgNbrAddressType_Type = InetAddressType
_JnxOspfv3CfgNbrAddressType_Object = MibTableColumn
jnxOspfv3CfgNbrAddressType = _JnxOspfv3CfgNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 10, 1, 3),
    _JnxOspfv3CfgNbrAddressType_Type()
)
jnxOspfv3CfgNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3CfgNbrAddressType.setStatus("deprecated")


class _JnxOspfv3CfgNbrAddress_Type(InetAddress):
    """Custom type jnxOspfv3CfgNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_JnxOspfv3CfgNbrAddress_Type.__name__ = "InetAddress"
_JnxOspfv3CfgNbrAddress_Object = MibTableColumn
jnxOspfv3CfgNbrAddress = _JnxOspfv3CfgNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 10, 1, 4),
    _JnxOspfv3CfgNbrAddress_Type()
)
jnxOspfv3CfgNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3CfgNbrAddress.setStatus("deprecated")


class _JnxOspfv3CfgNbrPriority_Type(DesignatedRouterPriority):
    """Custom type jnxOspfv3CfgNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_JnxOspfv3CfgNbrPriority_Object = MibTableColumn
jnxOspfv3CfgNbrPriority = _JnxOspfv3CfgNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 10, 1, 5),
    _JnxOspfv3CfgNbrPriority_Type()
)
jnxOspfv3CfgNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3CfgNbrPriority.setStatus("deprecated")
_JnxOspfv3CfgNbrStatus_Type = RowStatus
_JnxOspfv3CfgNbrStatus_Object = MibTableColumn
jnxOspfv3CfgNbrStatus = _JnxOspfv3CfgNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 10, 1, 6),
    _JnxOspfv3CfgNbrStatus_Type()
)
jnxOspfv3CfgNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3CfgNbrStatus.setStatus("deprecated")
_JnxOspfv3VirtNbrTable_Object = MibTable
jnxOspfv3VirtNbrTable = _JnxOspfv3VirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrTable.setStatus("deprecated")
_JnxOspfv3VirtNbrEntry_Object = MibTableRow
jnxOspfv3VirtNbrEntry = _JnxOspfv3VirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1)
)
jnxOspfv3VirtNbrEntry.setIndexNames(
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrArea"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrEntry.setStatus("deprecated")
_JnxOspfv3VirtNbrArea_Type = JnxOspfv3AreaIdTc
_JnxOspfv3VirtNbrArea_Object = MibTableColumn
jnxOspfv3VirtNbrArea = _JnxOspfv3VirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 1),
    _JnxOspfv3VirtNbrArea_Type()
)
jnxOspfv3VirtNbrArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrArea.setStatus("deprecated")
_JnxOspfv3VirtNbrRtrId_Type = JnxOspfv3RouterIdTc
_JnxOspfv3VirtNbrRtrId_Object = MibTableColumn
jnxOspfv3VirtNbrRtrId = _JnxOspfv3VirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 2),
    _JnxOspfv3VirtNbrRtrId_Type()
)
jnxOspfv3VirtNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrRtrId.setStatus("deprecated")
_JnxOspfv3VirtNbrIfIndex_Type = InterfaceIndex
_JnxOspfv3VirtNbrIfIndex_Object = MibTableColumn
jnxOspfv3VirtNbrIfIndex = _JnxOspfv3VirtNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 3),
    _JnxOspfv3VirtNbrIfIndex_Type()
)
jnxOspfv3VirtNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrIfIndex.setStatus("deprecated")
_JnxOspfv3VirtNbrIfInstId_Type = JnxOspfv3IfInstIdTc
_JnxOspfv3VirtNbrIfInstId_Object = MibTableColumn
jnxOspfv3VirtNbrIfInstId = _JnxOspfv3VirtNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 4),
    _JnxOspfv3VirtNbrIfInstId_Type()
)
jnxOspfv3VirtNbrIfInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrIfInstId.setStatus("deprecated")
_JnxOspfv3VirtNbrAddressType_Type = InetAddressType
_JnxOspfv3VirtNbrAddressType_Object = MibTableColumn
jnxOspfv3VirtNbrAddressType = _JnxOspfv3VirtNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 5),
    _JnxOspfv3VirtNbrAddressType_Type()
)
jnxOspfv3VirtNbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrAddressType.setStatus("deprecated")


class _JnxOspfv3VirtNbrAddress_Type(InetAddress):
    """Custom type jnxOspfv3VirtNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_JnxOspfv3VirtNbrAddress_Type.__name__ = "InetAddress"
_JnxOspfv3VirtNbrAddress_Object = MibTableColumn
jnxOspfv3VirtNbrAddress = _JnxOspfv3VirtNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 6),
    _JnxOspfv3VirtNbrAddress_Type()
)
jnxOspfv3VirtNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrAddress.setStatus("deprecated")
_JnxOspfv3VirtNbrOptions_Type = Integer32
_JnxOspfv3VirtNbrOptions_Object = MibTableColumn
jnxOspfv3VirtNbrOptions = _JnxOspfv3VirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 7),
    _JnxOspfv3VirtNbrOptions_Type()
)
jnxOspfv3VirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrOptions.setStatus("deprecated")


class _JnxOspfv3VirtNbrState_Type(Integer32):
    """Custom type jnxOspfv3VirtNbrState based on Integer32"""
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


_JnxOspfv3VirtNbrState_Type.__name__ = "Integer32"
_JnxOspfv3VirtNbrState_Object = MibTableColumn
jnxOspfv3VirtNbrState = _JnxOspfv3VirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 8),
    _JnxOspfv3VirtNbrState_Type()
)
jnxOspfv3VirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrState.setStatus("deprecated")
_JnxOspfv3VirtNbrEvents_Type = Counter32
_JnxOspfv3VirtNbrEvents_Object = MibTableColumn
jnxOspfv3VirtNbrEvents = _JnxOspfv3VirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 9),
    _JnxOspfv3VirtNbrEvents_Type()
)
jnxOspfv3VirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrEvents.setStatus("deprecated")
_JnxOspfv3VirtNbrLsRetransQLen_Type = Gauge32
_JnxOspfv3VirtNbrLsRetransQLen_Object = MibTableColumn
jnxOspfv3VirtNbrLsRetransQLen = _JnxOspfv3VirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 10),
    _JnxOspfv3VirtNbrLsRetransQLen_Type()
)
jnxOspfv3VirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrLsRetransQLen.setStatus("deprecated")
_JnxOspfv3VirtNbrHelloSuppressed_Type = TruthValue
_JnxOspfv3VirtNbrHelloSuppressed_Object = MibTableColumn
jnxOspfv3VirtNbrHelloSuppressed = _JnxOspfv3VirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 11),
    _JnxOspfv3VirtNbrHelloSuppressed_Type()
)
jnxOspfv3VirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrHelloSuppressed.setStatus("deprecated")
_JnxOspfv3VirtNbrIfId_Type = InterfaceIndex
_JnxOspfv3VirtNbrIfId_Object = MibTableColumn
jnxOspfv3VirtNbrIfId = _JnxOspfv3VirtNbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 12),
    _JnxOspfv3VirtNbrIfId_Type()
)
jnxOspfv3VirtNbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrIfId.setStatus("deprecated")


class _JnxOspfv3VirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type jnxOspfv3VirtNbrRestartHelperStatus based on Integer32"""
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


_JnxOspfv3VirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_JnxOspfv3VirtNbrRestartHelperStatus_Object = MibTableColumn
jnxOspfv3VirtNbrRestartHelperStatus = _JnxOspfv3VirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 13),
    _JnxOspfv3VirtNbrRestartHelperStatus_Type()
)
jnxOspfv3VirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrRestartHelperStatus.setStatus("deprecated")
_JnxOspfv3VirtNbrRestartHelperAge_Type = JnxOspfv3UpToRefreshIntervalTc
_JnxOspfv3VirtNbrRestartHelperAge_Object = MibTableColumn
jnxOspfv3VirtNbrRestartHelperAge = _JnxOspfv3VirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 14),
    _JnxOspfv3VirtNbrRestartHelperAge_Type()
)
jnxOspfv3VirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrRestartHelperAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrRestartHelperAge.setUnits("seconds")


class _JnxOspfv3VirtNbrRestartHelperExitRc_Type(Integer32):
    """Custom type jnxOspfv3VirtNbrRestartHelperExitRc based on Integer32"""
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


_JnxOspfv3VirtNbrRestartHelperExitRc_Type.__name__ = "Integer32"
_JnxOspfv3VirtNbrRestartHelperExitRc_Object = MibTableColumn
jnxOspfv3VirtNbrRestartHelperExitRc = _JnxOspfv3VirtNbrRestartHelperExitRc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 11, 1, 15),
    _JnxOspfv3VirtNbrRestartHelperExitRc_Type()
)
jnxOspfv3VirtNbrRestartHelperExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrRestartHelperExitRc.setStatus("deprecated")
_JnxOspfv3AreaAggregateTable_Object = MibTable
jnxOspfv3AreaAggregateTable = _JnxOspfv3AreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 12)
)
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregateTable.setStatus("deprecated")
_JnxOspfv3AreaAggregateEntry_Object = MibTableRow
jnxOspfv3AreaAggregateEntry = _JnxOspfv3AreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 12, 1)
)
jnxOspfv3AreaAggregateEntry.setIndexNames(
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaAggregateAreaID"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaAggregateAreaLsdbType"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaAggregatePrefixType"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaAggregatePrefix"),
    (0, "OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaAggregatePrefixLength"),
)
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregateEntry.setStatus("deprecated")
_JnxOspfv3AreaAggregateAreaID_Type = JnxOspfv3AreaIdTc
_JnxOspfv3AreaAggregateAreaID_Object = MibTableColumn
jnxOspfv3AreaAggregateAreaID = _JnxOspfv3AreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 12, 1, 1),
    _JnxOspfv3AreaAggregateAreaID_Type()
)
jnxOspfv3AreaAggregateAreaID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregateAreaID.setStatus("deprecated")


class _JnxOspfv3AreaAggregateAreaLsdbType_Type(Integer32):
    """Custom type jnxOspfv3AreaAggregateAreaLsdbType based on Integer32"""
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


_JnxOspfv3AreaAggregateAreaLsdbType_Type.__name__ = "Integer32"
_JnxOspfv3AreaAggregateAreaLsdbType_Object = MibTableColumn
jnxOspfv3AreaAggregateAreaLsdbType = _JnxOspfv3AreaAggregateAreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 12, 1, 2),
    _JnxOspfv3AreaAggregateAreaLsdbType_Type()
)
jnxOspfv3AreaAggregateAreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregateAreaLsdbType.setStatus("deprecated")
_JnxOspfv3AreaAggregatePrefixType_Type = InetAddressType
_JnxOspfv3AreaAggregatePrefixType_Object = MibTableColumn
jnxOspfv3AreaAggregatePrefixType = _JnxOspfv3AreaAggregatePrefixType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 12, 1, 4),
    _JnxOspfv3AreaAggregatePrefixType_Type()
)
jnxOspfv3AreaAggregatePrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregatePrefixType.setStatus("deprecated")


class _JnxOspfv3AreaAggregatePrefix_Type(InetAddress):
    """Custom type jnxOspfv3AreaAggregatePrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JnxOspfv3AreaAggregatePrefix_Type.__name__ = "InetAddress"
_JnxOspfv3AreaAggregatePrefix_Object = MibTableColumn
jnxOspfv3AreaAggregatePrefix = _JnxOspfv3AreaAggregatePrefix_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 12, 1, 5),
    _JnxOspfv3AreaAggregatePrefix_Type()
)
jnxOspfv3AreaAggregatePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregatePrefix.setStatus("deprecated")


class _JnxOspfv3AreaAggregatePrefixLength_Type(InetAddressPrefixLength):
    """Custom type jnxOspfv3AreaAggregatePrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 128),
    )


_JnxOspfv3AreaAggregatePrefixLength_Type.__name__ = "InetAddressPrefixLength"
_JnxOspfv3AreaAggregatePrefixLength_Object = MibTableColumn
jnxOspfv3AreaAggregatePrefixLength = _JnxOspfv3AreaAggregatePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 12, 1, 6),
    _JnxOspfv3AreaAggregatePrefixLength_Type()
)
jnxOspfv3AreaAggregatePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregatePrefixLength.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregatePrefixLength.setUnits("bits")
_JnxOspfv3AreaAggregateStatus_Type = RowStatus
_JnxOspfv3AreaAggregateStatus_Object = MibTableColumn
jnxOspfv3AreaAggregateStatus = _JnxOspfv3AreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 12, 1, 7),
    _JnxOspfv3AreaAggregateStatus_Type()
)
jnxOspfv3AreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregateStatus.setStatus("deprecated")


class _JnxOspfv3AreaAggregateEffect_Type(Integer32):
    """Custom type jnxOspfv3AreaAggregateEffect based on Integer32"""
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


_JnxOspfv3AreaAggregateEffect_Type.__name__ = "Integer32"
_JnxOspfv3AreaAggregateEffect_Object = MibTableColumn
jnxOspfv3AreaAggregateEffect = _JnxOspfv3AreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 12, 1, 8),
    _JnxOspfv3AreaAggregateEffect_Type()
)
jnxOspfv3AreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregateEffect.setStatus("deprecated")


class _JnxOspfv3AreaAggregateRouteTag_Type(Integer32):
    """Custom type jnxOspfv3AreaAggregateRouteTag based on Integer32"""
    defaultValue = 0


_JnxOspfv3AreaAggregateRouteTag_Object = MibTableColumn
jnxOspfv3AreaAggregateRouteTag = _JnxOspfv3AreaAggregateRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 12, 1, 9),
    _JnxOspfv3AreaAggregateRouteTag_Type()
)
jnxOspfv3AreaAggregateRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregateRouteTag.setStatus("deprecated")
_JnxOspfv3NotificationEntry_ObjectIdentity = ObjectIdentity
jnxOspfv3NotificationEntry = _JnxOspfv3NotificationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 13)
)


class _JnxOspfv3ConfigErrorType_Type(Integer32):
    """Custom type jnxOspfv3ConfigErrorType based on Integer32"""
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


_JnxOspfv3ConfigErrorType_Type.__name__ = "Integer32"
_JnxOspfv3ConfigErrorType_Object = MibScalar
jnxOspfv3ConfigErrorType = _JnxOspfv3ConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 13, 1),
    _JnxOspfv3ConfigErrorType_Type()
)
jnxOspfv3ConfigErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOspfv3ConfigErrorType.setStatus("deprecated")


class _JnxOspfv3PacketType_Type(Integer32):
    """Custom type jnxOspfv3PacketType based on Integer32"""
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


_JnxOspfv3PacketType_Type.__name__ = "Integer32"
_JnxOspfv3PacketType_Object = MibScalar
jnxOspfv3PacketType = _JnxOspfv3PacketType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 13, 2),
    _JnxOspfv3PacketType_Type()
)
jnxOspfv3PacketType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOspfv3PacketType.setStatus("deprecated")
_JnxOspfv3PacketSrc_Type = InetAddress
_JnxOspfv3PacketSrc_Object = MibScalar
jnxOspfv3PacketSrc = _JnxOspfv3PacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 1, 13, 3),
    _JnxOspfv3PacketSrc_Type()
)
jnxOspfv3PacketSrc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOspfv3PacketSrc.setStatus("deprecated")
_JnxOspfv3Conformance_ObjectIdentity = ObjectIdentity
jnxOspfv3Conformance = _JnxOspfv3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2)
)
_JnxOspfv3Groups_ObjectIdentity = ObjectIdentity
jnxOspfv3Groups = _JnxOspfv3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1)
)
_JnxOspfv3Compliances_ObjectIdentity = ObjectIdentity
jnxOspfv3Compliances = _JnxOspfv3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 2)
)

# Managed Objects groups

jnxOspfv3BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 1)
)
jnxOspfv3BasicGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AdminStat"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VersionNumber"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaBdrRtrStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3ASBdrRtrStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AsScopeLsaCount"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AsScopeLsaCksumSum"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3OriginateNewLsas"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3RxNewLsas"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3ExtLsaCount"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3ExtAreaLsdbLimit"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3MulticastExtensions"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3ExitOverflowInterval"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3DemandExtensions"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3ReferenceBandwidth"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3RestartSupport"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3RestartInterval"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3RestartStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3RestartAge"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3RestartExitRc"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NotificationEnable"))
)
if mibBuilder.loadTexts:
    jnxOspfv3BasicGroup.setStatus("deprecated")

jnxOspfv3AreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 2)
)
jnxOspfv3AreaGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3ImportAsExtern"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaSpfRuns"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaBdrRtrCount"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaAsBdrRtrCount"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaScopeLsaCount"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaScopeLsaCksumSum"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaSummary"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3StubMetric"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaNssaTranslatorRole"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaNssaTranslatorState"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaNssaTranslatorStabInt"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaNssaTranslatorEvents"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaStubMetricType"))
)
if mibBuilder.loadTexts:
    jnxOspfv3AreaGroup.setStatus("deprecated")

jnxOspfv3AsLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 3)
)
jnxOspfv3AsLsdbGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3AsLsdbSequence"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AsLsdbAge"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AsLsdbChecksum"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AsLsdbAdvertisement"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AsLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    jnxOspfv3AsLsdbGroup.setStatus("deprecated")

jnxOspfv3AreaLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 4)
)
jnxOspfv3AreaLsdbGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaLsdbSequence"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaLsdbAge"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaLsdbChecksum"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaLsdbAdvertisement"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    jnxOspfv3AreaLsdbGroup.setStatus("deprecated")

jnxOspfv3LinkLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 5)
)
jnxOspfv3LinkLsdbGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3LinkLsdbSequence"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3LinkLsdbAge"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3LinkLsdbChecksum"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3LinkLsdbAdvertisement"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3LinkLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    jnxOspfv3LinkLsdbGroup.setStatus("deprecated")

jnxOspfv3HostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 6)
)
jnxOspfv3HostGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3HostMetric"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3HostStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3HostAreaID"))
)
if mibBuilder.loadTexts:
    jnxOspfv3HostGroup.setStatus("deprecated")

jnxOspfv3IfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 7)
)
jnxOspfv3IfGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfAreaId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfType"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfAdminStat"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfRtrPriority"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfTransitDelay"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfRetransInterval"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfHelloInterval"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfRtrDeadInterval"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfPollInterval"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfState"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfDesignatedRouter"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfBackupDesignatedRouter"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfEvents"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfMulticastForwarding"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfDemand"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfMetricValue"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfLinkScopeLsaCount"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfLinkLsaCksumSum"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfDemandNbrProbe"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfDemandNbrProbeRetxLimit"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfDemandNbrProbeInterval"))
)
if mibBuilder.loadTexts:
    jnxOspfv3IfGroup.setStatus("deprecated")

jnxOspfv3VirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 8)
)
jnxOspfv3VirtIfGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfIndex"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfInstId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfTransitDelay"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfRetransInterval"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfHelloInterval"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfRtrDeadInterval"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfState"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfEvents"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfLinkScopeLsaCount"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfLinkLsaCksumSum"))
)
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfGroup.setStatus("deprecated")

jnxOspfv3NbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 9)
)
jnxOspfv3NbrGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrAddressType"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrAddress"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrOptions"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrPriority"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrState"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrEvents"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrLsRetransQLen"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrHelloSuppressed"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrIfId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrRestartHelperStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrRestartHelperAge"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    jnxOspfv3NbrGroup.setStatus("deprecated")

jnxOspfv3CfgNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 10)
)
jnxOspfv3CfgNbrGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3CfgNbrPriority"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3CfgNbrStatus"))
)
if mibBuilder.loadTexts:
    jnxOspfv3CfgNbrGroup.setStatus("deprecated")

jnxOspfv3VirtNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 11)
)
jnxOspfv3VirtNbrGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrIfIndex"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrIfInstId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrAddressType"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrAddress"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrOptions"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrState"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrEvents"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrLsRetransQLen"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrHelloSuppressed"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrIfId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrRestartHelperStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrRestartHelperAge"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrGroup.setStatus("deprecated")

jnxOspfv3AreaAggregateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 12)
)
jnxOspfv3AreaAggregateGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaAggregateStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaAggregateEffect"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaAggregateRouteTag"))
)
if mibBuilder.loadTexts:
    jnxOspfv3AreaAggregateGroup.setStatus("deprecated")

jnxOspfv3NotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 13)
)
jnxOspfv3NotificationObjectGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3ConfigErrorType"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3PacketType"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3PacketSrc"))
)
if mibBuilder.loadTexts:
    jnxOspfv3NotificationObjectGroup.setStatus("deprecated")


# Notification objects

jnxOspfv3VirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 1)
)
jnxOspfv3VirtIfStateChange.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfState"))
)
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfStateChange.setStatus(
        "deprecated"
    )

jnxOspfv3NbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 2)
)
jnxOspfv3NbrStateChange.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrState"))
)
if mibBuilder.loadTexts:
    jnxOspfv3NbrStateChange.setStatus(
        "deprecated"
    )

jnxOspfv3VirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 3)
)
jnxOspfv3VirtNbrStateChange.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrState"))
)
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrStateChange.setStatus(
        "deprecated"
    )

jnxOspfv3IfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 4)
)
jnxOspfv3IfConfigError.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfState"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3PacketSrc"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3ConfigErrorType"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3PacketType"))
)
if mibBuilder.loadTexts:
    jnxOspfv3IfConfigError.setStatus(
        "deprecated"
    )

jnxOspfv3VirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 5)
)
jnxOspfv3VirtIfConfigError.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfState"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3ConfigErrorType"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3PacketType"))
)
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfConfigError.setStatus(
        "deprecated"
    )

jnxOspfv3IfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 6)
)
jnxOspfv3IfRxBadPacket.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfState"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3PacketSrc"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3PacketType"))
)
if mibBuilder.loadTexts:
    jnxOspfv3IfRxBadPacket.setStatus(
        "deprecated"
    )

jnxOspfv3VirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 7)
)
jnxOspfv3VirtIfRxBadPacket.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfState"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3PacketType"))
)
if mibBuilder.loadTexts:
    jnxOspfv3VirtIfRxBadPacket.setStatus(
        "deprecated"
    )

jnxOspfv3LsdbOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 8)
)
jnxOspfv3LsdbOverflow.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3ExtAreaLsdbLimit"))
)
if mibBuilder.loadTexts:
    jnxOspfv3LsdbOverflow.setStatus(
        "deprecated"
    )

jnxOspfv3LsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 9)
)
jnxOspfv3LsdbApproachingOverflow.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3ExtAreaLsdbLimit"))
)
if mibBuilder.loadTexts:
    jnxOspfv3LsdbApproachingOverflow.setStatus(
        "deprecated"
    )

jnxOspfv3IfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 10)
)
jnxOspfv3IfStateChange.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfState"))
)
if mibBuilder.loadTexts:
    jnxOspfv3IfStateChange.setStatus(
        "deprecated"
    )

jnxOspfv3NssaTranslatorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 11)
)
jnxOspfv3NssaTranslatorStatusChange.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3AreaNssaTranslatorState"))
)
if mibBuilder.loadTexts:
    jnxOspfv3NssaTranslatorStatusChange.setStatus(
        "deprecated"
    )

jnxOspfv3RestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 12)
)
jnxOspfv3RestartStatusChange.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3RestartStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3RestartInterval"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3RestartExitRc"))
)
if mibBuilder.loadTexts:
    jnxOspfv3RestartStatusChange.setStatus(
        "deprecated"
    )

jnxOspfv3NbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 13)
)
jnxOspfv3NbrRestartHelperStatusChange.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrRestartHelperStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrRestartHelperAge"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    jnxOspfv3NbrRestartHelperStatusChange.setStatus(
        "deprecated"
    )

jnxOspfv3VirtNbrRestartHelperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 0, 14)
)
jnxOspfv3VirtNbrRestartHelperStatusChange.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3RouterId"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrRestartHelperStatus"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrRestartHelperAge"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    jnxOspfv3VirtNbrRestartHelperStatusChange.setStatus(
        "deprecated"
    )


# Notifications groups

jnxOspfv3NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 1, 14)
)
jnxOspfv3NotificationGroup.setObjects(
      *(("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfStateChange"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrStateChange"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrStateChange"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfConfigError"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfConfigError"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfRxBadPacket"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtIfRxBadPacket"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3LsdbOverflow"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3LsdbApproachingOverflow"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3IfStateChange"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NssaTranslatorStatusChange"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3RestartStatusChange"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3NbrRestartHelperStatusChange"),
        ("OSPFV3-MIB-JUNIPER", "jnxOspfv3VirtNbrRestartHelperStatusChange"))
)
if mibBuilder.loadTexts:
    jnxOspfv3NotificationGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

jnxOspfv3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 5, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    jnxOspfv3Compliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OSPFV3-MIB-JUNIPER",
    **{"JnxOspfv3UpToRefreshIntervalTc": JnxOspfv3UpToRefreshIntervalTc,
       "JnxOspfv3DeadIntRangeTc": JnxOspfv3DeadIntRangeTc,
       "JnxOspfv3RouterIdTc": JnxOspfv3RouterIdTc,
       "JnxOspfv3AreaIdTc": JnxOspfv3AreaIdTc,
       "JnxOspfv3IfInstIdTc": JnxOspfv3IfInstIdTc,
       "jnxOspfv3MIB": jnxOspfv3MIB,
       "jnxOspfv3Notifications": jnxOspfv3Notifications,
       "jnxOspfv3VirtIfStateChange": jnxOspfv3VirtIfStateChange,
       "jnxOspfv3NbrStateChange": jnxOspfv3NbrStateChange,
       "jnxOspfv3VirtNbrStateChange": jnxOspfv3VirtNbrStateChange,
       "jnxOspfv3IfConfigError": jnxOspfv3IfConfigError,
       "jnxOspfv3VirtIfConfigError": jnxOspfv3VirtIfConfigError,
       "jnxOspfv3IfRxBadPacket": jnxOspfv3IfRxBadPacket,
       "jnxOspfv3VirtIfRxBadPacket": jnxOspfv3VirtIfRxBadPacket,
       "jnxOspfv3LsdbOverflow": jnxOspfv3LsdbOverflow,
       "jnxOspfv3LsdbApproachingOverflow": jnxOspfv3LsdbApproachingOverflow,
       "jnxOspfv3IfStateChange": jnxOspfv3IfStateChange,
       "jnxOspfv3NssaTranslatorStatusChange": jnxOspfv3NssaTranslatorStatusChange,
       "jnxOspfv3RestartStatusChange": jnxOspfv3RestartStatusChange,
       "jnxOspfv3NbrRestartHelperStatusChange": jnxOspfv3NbrRestartHelperStatusChange,
       "jnxOspfv3VirtNbrRestartHelperStatusChange": jnxOspfv3VirtNbrRestartHelperStatusChange,
       "jnxOspfv3Objects": jnxOspfv3Objects,
       "jnxOspfv3GeneralGroup": jnxOspfv3GeneralGroup,
       "jnxOspfv3RouterId": jnxOspfv3RouterId,
       "jnxOspfv3AdminStat": jnxOspfv3AdminStat,
       "jnxOspfv3VersionNumber": jnxOspfv3VersionNumber,
       "jnxOspfv3AreaBdrRtrStatus": jnxOspfv3AreaBdrRtrStatus,
       "jnxOspfv3ASBdrRtrStatus": jnxOspfv3ASBdrRtrStatus,
       "jnxOspfv3AsScopeLsaCount": jnxOspfv3AsScopeLsaCount,
       "jnxOspfv3AsScopeLsaCksumSum": jnxOspfv3AsScopeLsaCksumSum,
       "jnxOspfv3OriginateNewLsas": jnxOspfv3OriginateNewLsas,
       "jnxOspfv3RxNewLsas": jnxOspfv3RxNewLsas,
       "jnxOspfv3ExtLsaCount": jnxOspfv3ExtLsaCount,
       "jnxOspfv3ExtAreaLsdbLimit": jnxOspfv3ExtAreaLsdbLimit,
       "jnxOspfv3MulticastExtensions": jnxOspfv3MulticastExtensions,
       "jnxOspfv3ExitOverflowInterval": jnxOspfv3ExitOverflowInterval,
       "jnxOspfv3DemandExtensions": jnxOspfv3DemandExtensions,
       "jnxOspfv3ReferenceBandwidth": jnxOspfv3ReferenceBandwidth,
       "jnxOspfv3RestartSupport": jnxOspfv3RestartSupport,
       "jnxOspfv3RestartInterval": jnxOspfv3RestartInterval,
       "jnxOspfv3RestartStatus": jnxOspfv3RestartStatus,
       "jnxOspfv3RestartAge": jnxOspfv3RestartAge,
       "jnxOspfv3RestartExitRc": jnxOspfv3RestartExitRc,
       "jnxOspfv3NotificationEnable": jnxOspfv3NotificationEnable,
       "jnxOspfv3AreaTable": jnxOspfv3AreaTable,
       "jnxOspfv3AreaEntry": jnxOspfv3AreaEntry,
       "jnxOspfv3AreaId": jnxOspfv3AreaId,
       "jnxOspfv3ImportAsExtern": jnxOspfv3ImportAsExtern,
       "jnxOspfv3AreaSpfRuns": jnxOspfv3AreaSpfRuns,
       "jnxOspfv3AreaBdrRtrCount": jnxOspfv3AreaBdrRtrCount,
       "jnxOspfv3AreaAsBdrRtrCount": jnxOspfv3AreaAsBdrRtrCount,
       "jnxOspfv3AreaScopeLsaCount": jnxOspfv3AreaScopeLsaCount,
       "jnxOspfv3AreaScopeLsaCksumSum": jnxOspfv3AreaScopeLsaCksumSum,
       "jnxOspfv3AreaSummary": jnxOspfv3AreaSummary,
       "jnxOspfv3AreaStatus": jnxOspfv3AreaStatus,
       "jnxOspfv3StubMetric": jnxOspfv3StubMetric,
       "jnxOspfv3AreaNssaTranslatorRole": jnxOspfv3AreaNssaTranslatorRole,
       "jnxOspfv3AreaNssaTranslatorState": jnxOspfv3AreaNssaTranslatorState,
       "jnxOspfv3AreaNssaTranslatorStabInt": jnxOspfv3AreaNssaTranslatorStabInt,
       "jnxOspfv3AreaNssaTranslatorEvents": jnxOspfv3AreaNssaTranslatorEvents,
       "jnxOspfv3AreaStubMetricType": jnxOspfv3AreaStubMetricType,
       "jnxOspfv3AsLsdbTable": jnxOspfv3AsLsdbTable,
       "jnxOspfv3AsLsdbEntry": jnxOspfv3AsLsdbEntry,
       "jnxOspfv3AsLsdbType": jnxOspfv3AsLsdbType,
       "jnxOspfv3AsLsdbRouterId": jnxOspfv3AsLsdbRouterId,
       "jnxOspfv3AsLsdbLsid": jnxOspfv3AsLsdbLsid,
       "jnxOspfv3AsLsdbSequence": jnxOspfv3AsLsdbSequence,
       "jnxOspfv3AsLsdbAge": jnxOspfv3AsLsdbAge,
       "jnxOspfv3AsLsdbChecksum": jnxOspfv3AsLsdbChecksum,
       "jnxOspfv3AsLsdbAdvertisement": jnxOspfv3AsLsdbAdvertisement,
       "jnxOspfv3AsLsdbTypeKnown": jnxOspfv3AsLsdbTypeKnown,
       "jnxOspfv3AreaLsdbTable": jnxOspfv3AreaLsdbTable,
       "jnxOspfv3AreaLsdbEntry": jnxOspfv3AreaLsdbEntry,
       "jnxOspfv3AreaLsdbAreaId": jnxOspfv3AreaLsdbAreaId,
       "jnxOspfv3AreaLsdbType": jnxOspfv3AreaLsdbType,
       "jnxOspfv3AreaLsdbRouterId": jnxOspfv3AreaLsdbRouterId,
       "jnxOspfv3AreaLsdbLsid": jnxOspfv3AreaLsdbLsid,
       "jnxOspfv3AreaLsdbSequence": jnxOspfv3AreaLsdbSequence,
       "jnxOspfv3AreaLsdbAge": jnxOspfv3AreaLsdbAge,
       "jnxOspfv3AreaLsdbChecksum": jnxOspfv3AreaLsdbChecksum,
       "jnxOspfv3AreaLsdbAdvertisement": jnxOspfv3AreaLsdbAdvertisement,
       "jnxOspfv3AreaLsdbTypeKnown": jnxOspfv3AreaLsdbTypeKnown,
       "jnxOspfv3LinkLsdbTable": jnxOspfv3LinkLsdbTable,
       "jnxOspfv3LinkLsdbEntry": jnxOspfv3LinkLsdbEntry,
       "jnxOspfv3LinkLsdbIfIndex": jnxOspfv3LinkLsdbIfIndex,
       "jnxOspfv3LinkLsdbIfInstId": jnxOspfv3LinkLsdbIfInstId,
       "jnxOspfv3LinkLsdbType": jnxOspfv3LinkLsdbType,
       "jnxOspfv3LinkLsdbRouterId": jnxOspfv3LinkLsdbRouterId,
       "jnxOspfv3LinkLsdbLsid": jnxOspfv3LinkLsdbLsid,
       "jnxOspfv3LinkLsdbSequence": jnxOspfv3LinkLsdbSequence,
       "jnxOspfv3LinkLsdbAge": jnxOspfv3LinkLsdbAge,
       "jnxOspfv3LinkLsdbChecksum": jnxOspfv3LinkLsdbChecksum,
       "jnxOspfv3LinkLsdbAdvertisement": jnxOspfv3LinkLsdbAdvertisement,
       "jnxOspfv3LinkLsdbTypeKnown": jnxOspfv3LinkLsdbTypeKnown,
       "jnxOspfv3HostTable": jnxOspfv3HostTable,
       "jnxOspfv3HostEntry": jnxOspfv3HostEntry,
       "jnxOspfv3HostAddressType": jnxOspfv3HostAddressType,
       "jnxOspfv3HostAddress": jnxOspfv3HostAddress,
       "jnxOspfv3HostMetric": jnxOspfv3HostMetric,
       "jnxOspfv3HostStatus": jnxOspfv3HostStatus,
       "jnxOspfv3HostAreaID": jnxOspfv3HostAreaID,
       "jnxOspfv3IfTable": jnxOspfv3IfTable,
       "jnxOspfv3IfEntry": jnxOspfv3IfEntry,
       "jnxOspfv3IfIndex": jnxOspfv3IfIndex,
       "jnxOspfv3IfInstId": jnxOspfv3IfInstId,
       "jnxOspfv3IfAreaId": jnxOspfv3IfAreaId,
       "jnxOspfv3IfType": jnxOspfv3IfType,
       "jnxOspfv3IfAdminStat": jnxOspfv3IfAdminStat,
       "jnxOspfv3IfRtrPriority": jnxOspfv3IfRtrPriority,
       "jnxOspfv3IfTransitDelay": jnxOspfv3IfTransitDelay,
       "jnxOspfv3IfRetransInterval": jnxOspfv3IfRetransInterval,
       "jnxOspfv3IfHelloInterval": jnxOspfv3IfHelloInterval,
       "jnxOspfv3IfRtrDeadInterval": jnxOspfv3IfRtrDeadInterval,
       "jnxOspfv3IfPollInterval": jnxOspfv3IfPollInterval,
       "jnxOspfv3IfState": jnxOspfv3IfState,
       "jnxOspfv3IfDesignatedRouter": jnxOspfv3IfDesignatedRouter,
       "jnxOspfv3IfBackupDesignatedRouter": jnxOspfv3IfBackupDesignatedRouter,
       "jnxOspfv3IfEvents": jnxOspfv3IfEvents,
       "jnxOspfv3IfStatus": jnxOspfv3IfStatus,
       "jnxOspfv3IfMulticastForwarding": jnxOspfv3IfMulticastForwarding,
       "jnxOspfv3IfDemand": jnxOspfv3IfDemand,
       "jnxOspfv3IfMetricValue": jnxOspfv3IfMetricValue,
       "jnxOspfv3IfLinkScopeLsaCount": jnxOspfv3IfLinkScopeLsaCount,
       "jnxOspfv3IfLinkLsaCksumSum": jnxOspfv3IfLinkLsaCksumSum,
       "jnxOspfv3IfDemandNbrProbe": jnxOspfv3IfDemandNbrProbe,
       "jnxOspfv3IfDemandNbrProbeRetxLimit": jnxOspfv3IfDemandNbrProbeRetxLimit,
       "jnxOspfv3IfDemandNbrProbeInterval": jnxOspfv3IfDemandNbrProbeInterval,
       "jnxOspfv3VirtIfTable": jnxOspfv3VirtIfTable,
       "jnxOspfv3VirtIfEntry": jnxOspfv3VirtIfEntry,
       "jnxOspfv3VirtIfAreaId": jnxOspfv3VirtIfAreaId,
       "jnxOspfv3VirtIfNeighbor": jnxOspfv3VirtIfNeighbor,
       "jnxOspfv3VirtIfIndex": jnxOspfv3VirtIfIndex,
       "jnxOspfv3VirtIfInstId": jnxOspfv3VirtIfInstId,
       "jnxOspfv3VirtIfTransitDelay": jnxOspfv3VirtIfTransitDelay,
       "jnxOspfv3VirtIfRetransInterval": jnxOspfv3VirtIfRetransInterval,
       "jnxOspfv3VirtIfHelloInterval": jnxOspfv3VirtIfHelloInterval,
       "jnxOspfv3VirtIfRtrDeadInterval": jnxOspfv3VirtIfRtrDeadInterval,
       "jnxOspfv3VirtIfState": jnxOspfv3VirtIfState,
       "jnxOspfv3VirtIfEvents": jnxOspfv3VirtIfEvents,
       "jnxOspfv3VirtIfStatus": jnxOspfv3VirtIfStatus,
       "jnxOspfv3VirtIfLinkScopeLsaCount": jnxOspfv3VirtIfLinkScopeLsaCount,
       "jnxOspfv3VirtIfLinkLsaCksumSum": jnxOspfv3VirtIfLinkLsaCksumSum,
       "jnxOspfv3NbrTable": jnxOspfv3NbrTable,
       "jnxOspfv3NbrEntry": jnxOspfv3NbrEntry,
       "jnxOspfv3NbrIfIndex": jnxOspfv3NbrIfIndex,
       "jnxOspfv3NbrIfInstId": jnxOspfv3NbrIfInstId,
       "jnxOspfv3NbrRtrId": jnxOspfv3NbrRtrId,
       "jnxOspfv3NbrAddressType": jnxOspfv3NbrAddressType,
       "jnxOspfv3NbrAddress": jnxOspfv3NbrAddress,
       "jnxOspfv3NbrOptions": jnxOspfv3NbrOptions,
       "jnxOspfv3NbrPriority": jnxOspfv3NbrPriority,
       "jnxOspfv3NbrState": jnxOspfv3NbrState,
       "jnxOspfv3NbrEvents": jnxOspfv3NbrEvents,
       "jnxOspfv3NbrLsRetransQLen": jnxOspfv3NbrLsRetransQLen,
       "jnxOspfv3NbrHelloSuppressed": jnxOspfv3NbrHelloSuppressed,
       "jnxOspfv3NbrIfId": jnxOspfv3NbrIfId,
       "jnxOspfv3NbrRestartHelperStatus": jnxOspfv3NbrRestartHelperStatus,
       "jnxOspfv3NbrRestartHelperAge": jnxOspfv3NbrRestartHelperAge,
       "jnxOspfv3NbrRestartHelperExitRc": jnxOspfv3NbrRestartHelperExitRc,
       "jnxOspfv3CfgNbrTable": jnxOspfv3CfgNbrTable,
       "jnxOspfv3CfgNbrEntry": jnxOspfv3CfgNbrEntry,
       "jnxOspfv3CfgNbrIfIndex": jnxOspfv3CfgNbrIfIndex,
       "jnxOspfv3CfgNbrIfInstId": jnxOspfv3CfgNbrIfInstId,
       "jnxOspfv3CfgNbrAddressType": jnxOspfv3CfgNbrAddressType,
       "jnxOspfv3CfgNbrAddress": jnxOspfv3CfgNbrAddress,
       "jnxOspfv3CfgNbrPriority": jnxOspfv3CfgNbrPriority,
       "jnxOspfv3CfgNbrStatus": jnxOspfv3CfgNbrStatus,
       "jnxOspfv3VirtNbrTable": jnxOspfv3VirtNbrTable,
       "jnxOspfv3VirtNbrEntry": jnxOspfv3VirtNbrEntry,
       "jnxOspfv3VirtNbrArea": jnxOspfv3VirtNbrArea,
       "jnxOspfv3VirtNbrRtrId": jnxOspfv3VirtNbrRtrId,
       "jnxOspfv3VirtNbrIfIndex": jnxOspfv3VirtNbrIfIndex,
       "jnxOspfv3VirtNbrIfInstId": jnxOspfv3VirtNbrIfInstId,
       "jnxOspfv3VirtNbrAddressType": jnxOspfv3VirtNbrAddressType,
       "jnxOspfv3VirtNbrAddress": jnxOspfv3VirtNbrAddress,
       "jnxOspfv3VirtNbrOptions": jnxOspfv3VirtNbrOptions,
       "jnxOspfv3VirtNbrState": jnxOspfv3VirtNbrState,
       "jnxOspfv3VirtNbrEvents": jnxOspfv3VirtNbrEvents,
       "jnxOspfv3VirtNbrLsRetransQLen": jnxOspfv3VirtNbrLsRetransQLen,
       "jnxOspfv3VirtNbrHelloSuppressed": jnxOspfv3VirtNbrHelloSuppressed,
       "jnxOspfv3VirtNbrIfId": jnxOspfv3VirtNbrIfId,
       "jnxOspfv3VirtNbrRestartHelperStatus": jnxOspfv3VirtNbrRestartHelperStatus,
       "jnxOspfv3VirtNbrRestartHelperAge": jnxOspfv3VirtNbrRestartHelperAge,
       "jnxOspfv3VirtNbrRestartHelperExitRc": jnxOspfv3VirtNbrRestartHelperExitRc,
       "jnxOspfv3AreaAggregateTable": jnxOspfv3AreaAggregateTable,
       "jnxOspfv3AreaAggregateEntry": jnxOspfv3AreaAggregateEntry,
       "jnxOspfv3AreaAggregateAreaID": jnxOspfv3AreaAggregateAreaID,
       "jnxOspfv3AreaAggregateAreaLsdbType": jnxOspfv3AreaAggregateAreaLsdbType,
       "jnxOspfv3AreaAggregatePrefixType": jnxOspfv3AreaAggregatePrefixType,
       "jnxOspfv3AreaAggregatePrefix": jnxOspfv3AreaAggregatePrefix,
       "jnxOspfv3AreaAggregatePrefixLength": jnxOspfv3AreaAggregatePrefixLength,
       "jnxOspfv3AreaAggregateStatus": jnxOspfv3AreaAggregateStatus,
       "jnxOspfv3AreaAggregateEffect": jnxOspfv3AreaAggregateEffect,
       "jnxOspfv3AreaAggregateRouteTag": jnxOspfv3AreaAggregateRouteTag,
       "jnxOspfv3NotificationEntry": jnxOspfv3NotificationEntry,
       "jnxOspfv3ConfigErrorType": jnxOspfv3ConfigErrorType,
       "jnxOspfv3PacketType": jnxOspfv3PacketType,
       "jnxOspfv3PacketSrc": jnxOspfv3PacketSrc,
       "jnxOspfv3Conformance": jnxOspfv3Conformance,
       "jnxOspfv3Groups": jnxOspfv3Groups,
       "jnxOspfv3BasicGroup": jnxOspfv3BasicGroup,
       "jnxOspfv3AreaGroup": jnxOspfv3AreaGroup,
       "jnxOspfv3AsLsdbGroup": jnxOspfv3AsLsdbGroup,
       "jnxOspfv3AreaLsdbGroup": jnxOspfv3AreaLsdbGroup,
       "jnxOspfv3LinkLsdbGroup": jnxOspfv3LinkLsdbGroup,
       "jnxOspfv3HostGroup": jnxOspfv3HostGroup,
       "jnxOspfv3IfGroup": jnxOspfv3IfGroup,
       "jnxOspfv3VirtIfGroup": jnxOspfv3VirtIfGroup,
       "jnxOspfv3NbrGroup": jnxOspfv3NbrGroup,
       "jnxOspfv3CfgNbrGroup": jnxOspfv3CfgNbrGroup,
       "jnxOspfv3VirtNbrGroup": jnxOspfv3VirtNbrGroup,
       "jnxOspfv3AreaAggregateGroup": jnxOspfv3AreaAggregateGroup,
       "jnxOspfv3NotificationObjectGroup": jnxOspfv3NotificationObjectGroup,
       "jnxOspfv3NotificationGroup": jnxOspfv3NotificationGroup,
       "jnxOspfv3Compliances": jnxOspfv3Compliances,
       "jnxOspfv3Compliance": jnxOspfv3Compliance}
)

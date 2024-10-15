# SNMP MIB module (RADLAN-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:47 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(AreaID,
 BigMetric,
 DesignatedRouterPriority,
 HelloRange,
 Metric,
 PositiveInteger,
 RouterID,
 Status,
 TOSType,
 UpToMaxAge) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "BigMetric",
    "DesignatedRouterPriority",
    "HelloRange",
    "Metric",
    "PositiveInteger",
    "RouterID",
    "Status",
    "TOSType",
    "UpToMaxAge")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

rlOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 210)
)
rlOspf.setRevisions(
        ("2011-05-04 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlOspfProcessID(Integer32, TextualConvention):
    status = "current"


class RlOspfFastHelloMultiplierRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )



class RlOspfRestartHelperStatus(Integer32, TextualConvention):
    status = "current"
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



class RlOspfRestartExitReason(Integer32, TextualConvention):
    status = "current"
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



class RlOspfRouterIdType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("manual", 2))
    )



class RlOspfAuthenticationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              9)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 0),
          ("null", 9),
          ("simplePassword", 1))
    )



class RlOspfUpToRefreshIntervalTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class RlOspfDeadIntervalRangeTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_RlOspfInstance_Type = RlOspfProcessID
_RlOspfInstance_Object = MibScalar
rlOspfInstance = _RlOspfInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 1),
    _RlOspfInstance_Type()
)
rlOspfInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfInstance.setStatus("current")
_RlOspfGeneralGroupTable_Object = MibTable
rlOspfGeneralGroupTable = _RlOspfGeneralGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2)
)
if mibBuilder.loadTexts:
    rlOspfGeneralGroupTable.setStatus("current")
_RlOspfGeneralGroupEntry_Object = MibTableRow
rlOspfGeneralGroupEntry = _RlOspfGeneralGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1)
)
rlOspfGeneralGroupEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfProcessId"),
)
if mibBuilder.loadTexts:
    rlOspfGeneralGroupEntry.setStatus("current")
_RlOspfProcessId_Type = RlOspfProcessID
_RlOspfProcessId_Object = MibTableColumn
rlOspfProcessId = _RlOspfProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 1),
    _RlOspfProcessId_Type()
)
rlOspfProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfProcessId.setStatus("current")
_RlOspfRouterId_Type = RouterID
_RlOspfRouterId_Object = MibTableColumn
rlOspfRouterId = _RlOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 2),
    _RlOspfRouterId_Type()
)
rlOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfRouterId.setStatus("current")
_RlOspfAdminStat_Type = Status
_RlOspfAdminStat_Object = MibTableColumn
rlOspfAdminStat = _RlOspfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 3),
    _RlOspfAdminStat_Type()
)
rlOspfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfAdminStat.setStatus("current")


class _RlOspfVersionNumber_Type(Integer32):
    """Custom type rlOspfVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("version2", 2)
    )


_RlOspfVersionNumber_Type.__name__ = "Integer32"
_RlOspfVersionNumber_Object = MibTableColumn
rlOspfVersionNumber = _RlOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 4),
    _RlOspfVersionNumber_Type()
)
rlOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVersionNumber.setStatus("current")
_RlOspfAreaBdrRtrStatus_Type = TruthValue
_RlOspfAreaBdrRtrStatus_Object = MibTableColumn
rlOspfAreaBdrRtrStatus = _RlOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 5),
    _RlOspfAreaBdrRtrStatus_Type()
)
rlOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaBdrRtrStatus.setStatus("current")
_RlOspfASBdrRtrStatus_Type = TruthValue
_RlOspfASBdrRtrStatus_Object = MibTableColumn
rlOspfASBdrRtrStatus = _RlOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 6),
    _RlOspfASBdrRtrStatus_Type()
)
rlOspfASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfASBdrRtrStatus.setStatus("current")
_RlOspfExternLsaCount_Type = Gauge32
_RlOspfExternLsaCount_Object = MibTableColumn
rlOspfExternLsaCount = _RlOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 7),
    _RlOspfExternLsaCount_Type()
)
rlOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternLsaCount.setStatus("current")
_RlOspfExternLsaCksumSum_Type = Integer32
_RlOspfExternLsaCksumSum_Object = MibTableColumn
rlOspfExternLsaCksumSum = _RlOspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 8),
    _RlOspfExternLsaCksumSum_Type()
)
rlOspfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExternLsaCksumSum.setStatus("current")
_RlOspfTOSSupport_Type = TruthValue
_RlOspfTOSSupport_Object = MibTableColumn
rlOspfTOSSupport = _RlOspfTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 9),
    _RlOspfTOSSupport_Type()
)
rlOspfTOSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfTOSSupport.setStatus("current")
_RlOspfOriginateNewLsas_Type = Counter32
_RlOspfOriginateNewLsas_Object = MibTableColumn
rlOspfOriginateNewLsas = _RlOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 10),
    _RlOspfOriginateNewLsas_Type()
)
rlOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfOriginateNewLsas.setStatus("current")
_RlOspfRxNewLsas_Type = Counter32
_RlOspfRxNewLsas_Object = MibTableColumn
rlOspfRxNewLsas = _RlOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 11),
    _RlOspfRxNewLsas_Type()
)
rlOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRxNewLsas.setStatus("current")


class _RlOspfExtLsdbLimit_Type(Integer32):
    """Custom type rlOspfExtLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_RlOspfExtLsdbLimit_Type.__name__ = "Integer32"
_RlOspfExtLsdbLimit_Object = MibTableColumn
rlOspfExtLsdbLimit = _RlOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 12),
    _RlOspfExtLsdbLimit_Type()
)
rlOspfExtLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfExtLsdbLimit.setStatus("current")


class _RlOspfMulticastExtensions_Type(Integer32):
    """Custom type rlOspfMulticastExtensions based on Integer32"""
    defaultValue = 0


_RlOspfMulticastExtensions_Object = MibTableColumn
rlOspfMulticastExtensions = _RlOspfMulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 13),
    _RlOspfMulticastExtensions_Type()
)
rlOspfMulticastExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfMulticastExtensions.setStatus("current")


class _RlOspfExitOverflowInterval_Type(PositiveInteger):
    """Custom type rlOspfExitOverflowInterval based on PositiveInteger"""
    defaultValue = 0


_RlOspfExitOverflowInterval_Object = MibTableColumn
rlOspfExitOverflowInterval = _RlOspfExitOverflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 14),
    _RlOspfExitOverflowInterval_Type()
)
rlOspfExitOverflowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfExitOverflowInterval.setStatus("current")
_RlOspfDemandExtensions_Type = TruthValue
_RlOspfDemandExtensions_Object = MibTableColumn
rlOspfDemandExtensions = _RlOspfDemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 15),
    _RlOspfDemandExtensions_Type()
)
rlOspfDemandExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfDemandExtensions.setStatus("current")
_RlOspfRFC1583Compatibility_Type = TruthValue
_RlOspfRFC1583Compatibility_Object = MibTableColumn
rlOspfRFC1583Compatibility = _RlOspfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 16),
    _RlOspfRFC1583Compatibility_Type()
)
rlOspfRFC1583Compatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfRFC1583Compatibility.setStatus("current")
_RlOspfOpaqueLsaSupport_Type = TruthValue
_RlOspfOpaqueLsaSupport_Object = MibTableColumn
rlOspfOpaqueLsaSupport = _RlOspfOpaqueLsaSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 17),
    _RlOspfOpaqueLsaSupport_Type()
)
rlOspfOpaqueLsaSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfOpaqueLsaSupport.setStatus("current")
_RlOspfReferenceBandwidth_Type = Unsigned32
_RlOspfReferenceBandwidth_Object = MibTableColumn
rlOspfReferenceBandwidth = _RlOspfReferenceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 18),
    _RlOspfReferenceBandwidth_Type()
)
rlOspfReferenceBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfReferenceBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfReferenceBandwidth.setUnits("kilobits per second")


class _RlOspfRestartSupport_Type(Integer32):
    """Custom type rlOspfRestartSupport based on Integer32"""
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


_RlOspfRestartSupport_Type.__name__ = "Integer32"
_RlOspfRestartSupport_Object = MibTableColumn
rlOspfRestartSupport = _RlOspfRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 19),
    _RlOspfRestartSupport_Type()
)
rlOspfRestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfRestartSupport.setStatus("current")


class _RlOspfRestartInterval_Type(Integer32):
    """Custom type rlOspfRestartInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_RlOspfRestartInterval_Type.__name__ = "Integer32"
_RlOspfRestartInterval_Object = MibTableColumn
rlOspfRestartInterval = _RlOspfRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 20),
    _RlOspfRestartInterval_Type()
)
rlOspfRestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfRestartInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfRestartInterval.setUnits("seconds")
_RlOspfRestartStrictLsaChecking_Type = TruthValue
_RlOspfRestartStrictLsaChecking_Object = MibTableColumn
rlOspfRestartStrictLsaChecking = _RlOspfRestartStrictLsaChecking_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 21),
    _RlOspfRestartStrictLsaChecking_Type()
)
rlOspfRestartStrictLsaChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfRestartStrictLsaChecking.setStatus("current")


class _RlOspfRestartStatus_Type(Integer32):
    """Custom type rlOspfRestartStatus based on Integer32"""
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


_RlOspfRestartStatus_Type.__name__ = "Integer32"
_RlOspfRestartStatus_Object = MibTableColumn
rlOspfRestartStatus = _RlOspfRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 22),
    _RlOspfRestartStatus_Type()
)
rlOspfRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRestartStatus.setStatus("current")
_RlOspfRestartAge_Type = Unsigned32
_RlOspfRestartAge_Object = MibTableColumn
rlOspfRestartAge = _RlOspfRestartAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 23),
    _RlOspfRestartAge_Type()
)
rlOspfRestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRestartAge.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfRestartAge.setUnits("seconds")


class _RlOspfRestartExitReason_Type(Integer32):
    """Custom type rlOspfRestartExitReason based on Integer32"""
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


_RlOspfRestartExitReason_Type.__name__ = "Integer32"
_RlOspfRestartExitReason_Object = MibTableColumn
rlOspfRestartExitReason = _RlOspfRestartExitReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 24),
    _RlOspfRestartExitReason_Type()
)
rlOspfRestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRestartExitReason.setStatus("current")
_RlOspfAsLsaCount_Type = Gauge32
_RlOspfAsLsaCount_Object = MibTableColumn
rlOspfAsLsaCount = _RlOspfAsLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 25),
    _RlOspfAsLsaCount_Type()
)
rlOspfAsLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAsLsaCount.setStatus("current")
_RlOspfAsLsaCksumSum_Type = Unsigned32
_RlOspfAsLsaCksumSum_Object = MibTableColumn
rlOspfAsLsaCksumSum = _RlOspfAsLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 26),
    _RlOspfAsLsaCksumSum_Type()
)
rlOspfAsLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAsLsaCksumSum.setStatus("current")
_RlOspfStubRouterSupport_Type = TruthValue
_RlOspfStubRouterSupport_Object = MibTableColumn
rlOspfStubRouterSupport = _RlOspfStubRouterSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 27),
    _RlOspfStubRouterSupport_Type()
)
rlOspfStubRouterSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfStubRouterSupport.setStatus("current")


class _RlOspfStubRouterAdvertisement_Type(Integer32):
    """Custom type rlOspfStubRouterAdvertisement based on Integer32"""
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


_RlOspfStubRouterAdvertisement_Type.__name__ = "Integer32"
_RlOspfStubRouterAdvertisement_Object = MibTableColumn
rlOspfStubRouterAdvertisement = _RlOspfStubRouterAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 28),
    _RlOspfStubRouterAdvertisement_Type()
)
rlOspfStubRouterAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfStubRouterAdvertisement.setStatus("current")
_RlOspfDiscontinuityTime_Type = TimeStamp
_RlOspfDiscontinuityTime_Object = MibTableColumn
rlOspfDiscontinuityTime = _RlOspfDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 29),
    _RlOspfDiscontinuityTime_Type()
)
rlOspfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfDiscontinuityTime.setStatus("current")
_RlOspfGeneralGroupStatus_Type = RowStatus
_RlOspfGeneralGroupStatus_Object = MibTableColumn
rlOspfGeneralGroupStatus = _RlOspfGeneralGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 30),
    _RlOspfGeneralGroupStatus_Type()
)
rlOspfGeneralGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfGeneralGroupStatus.setStatus("current")


class _RlOspfLogAdjacencyChanges_Type(Integer32):
    """Custom type rlOspfLogAdjacencyChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("detail", 2),
          ("disable", 3),
          ("enable", 1))
    )


_RlOspfLogAdjacencyChanges_Type.__name__ = "Integer32"
_RlOspfLogAdjacencyChanges_Object = MibTableColumn
rlOspfLogAdjacencyChanges = _RlOspfLogAdjacencyChanges_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 31),
    _RlOspfLogAdjacencyChanges_Type()
)
rlOspfLogAdjacencyChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfLogAdjacencyChanges.setStatus("current")
_RlOspfPassiveInterface_Type = TruthValue
_RlOspfPassiveInterface_Object = MibTableColumn
rlOspfPassiveInterface = _RlOspfPassiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 32),
    _RlOspfPassiveInterface_Type()
)
rlOspfPassiveInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfPassiveInterface.setStatus("current")


class _RlOspfDefaultMetric_Type(Integer32):
    """Custom type rlOspfDefaultMetric based on Integer32"""
    defaultValue = 0


_RlOspfDefaultMetric_Object = MibTableColumn
rlOspfDefaultMetric = _RlOspfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 33),
    _RlOspfDefaultMetric_Type()
)
rlOspfDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfDefaultMetric.setStatus("current")


class _RlOspfMaximumRedistPrefixNum_Type(Integer32):
    """Custom type rlOspfMaximumRedistPrefixNum based on Integer32"""
    defaultValue = 0


_RlOspfMaximumRedistPrefixNum_Object = MibTableColumn
rlOspfMaximumRedistPrefixNum = _RlOspfMaximumRedistPrefixNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 34),
    _RlOspfMaximumRedistPrefixNum_Type()
)
rlOspfMaximumRedistPrefixNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfMaximumRedistPrefixNum.setStatus("current")


class _RlOspfMaximumRedistPrefixThreshold_Type(Integer32):
    """Custom type rlOspfMaximumRedistPrefixThreshold based on Integer32"""
    defaultValue = 75


_RlOspfMaximumRedistPrefixThreshold_Object = MibTableColumn
rlOspfMaximumRedistPrefixThreshold = _RlOspfMaximumRedistPrefixThreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 35),
    _RlOspfMaximumRedistPrefixThreshold_Type()
)
rlOspfMaximumRedistPrefixThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfMaximumRedistPrefixThreshold.setStatus("current")


class _RlOspfMaximumRedistPrefixWarningOnly_Type(TruthValue):
    """Custom type rlOspfMaximumRedistPrefixWarningOnly based on TruthValue"""


_RlOspfMaximumRedistPrefixWarningOnly_Object = MibTableColumn
rlOspfMaximumRedistPrefixWarningOnly = _RlOspfMaximumRedistPrefixWarningOnly_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 36),
    _RlOspfMaximumRedistPrefixWarningOnly_Type()
)
rlOspfMaximumRedistPrefixWarningOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfMaximumRedistPrefixWarningOnly.setStatus("current")


class _RlOspfOperStatus_Type(Integer32):
    """Custom type rlOspfOperStatus based on Integer32"""
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
        *(("actFailed", 5),
          ("down", 2),
          ("goingDown", 4),
          ("goingUp", 3),
          ("up", 1))
    )


_RlOspfOperStatus_Type.__name__ = "Integer32"
_RlOspfOperStatus_Object = MibTableColumn
rlOspfOperStatus = _RlOspfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 37),
    _RlOspfOperStatus_Type()
)
rlOspfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfOperStatus.setStatus("current")
_RlOspfNextRouterId_Type = RouterID
_RlOspfNextRouterId_Object = MibTableColumn
rlOspfNextRouterId = _RlOspfNextRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 38),
    _RlOspfNextRouterId_Type()
)
rlOspfNextRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNextRouterId.setStatus("current")
_RlOspfRouterIdType_Type = RlOspfRouterIdType
_RlOspfRouterIdType_Object = MibTableColumn
rlOspfRouterIdType = _RlOspfRouterIdType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 39),
    _RlOspfRouterIdType_Type()
)
rlOspfRouterIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRouterIdType.setStatus("current")
_RlOspfNextRouterIdType_Type = RlOspfRouterIdType
_RlOspfNextRouterIdType_Object = MibTableColumn
rlOspfNextRouterIdType = _RlOspfNextRouterIdType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 40),
    _RlOspfNextRouterIdType_Type()
)
rlOspfNextRouterIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNextRouterIdType.setStatus("current")
_RlOspfASBdrRtrActualStatus_Type = TruthValue
_RlOspfASBdrRtrActualStatus_Object = MibTableColumn
rlOspfASBdrRtrActualStatus = _RlOspfASBdrRtrActualStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 41),
    _RlOspfASBdrRtrActualStatus_Type()
)
rlOspfASBdrRtrActualStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfASBdrRtrActualStatus.setStatus("current")


class _RlOspfCalcMaxDelay_Type(Unsigned32):
    """Custom type rlOspfCalcMaxDelay based on Unsigned32"""
    defaultValue = 5000


_RlOspfCalcMaxDelay_Object = MibTableColumn
rlOspfCalcMaxDelay = _RlOspfCalcMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 42),
    _RlOspfCalcMaxDelay_Type()
)
rlOspfCalcMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfCalcMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfCalcMaxDelay.setUnits("milliseconds")


class _RlOspfRteMaxEqCostPaths_Type(Unsigned32):
    """Custom type rlOspfRteMaxEqCostPaths based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfRteMaxEqCostPaths_Type.__name__ = "Unsigned32"
_RlOspfRteMaxEqCostPaths_Object = MibTableColumn
rlOspfRteMaxEqCostPaths = _RlOspfRteMaxEqCostPaths_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 2, 1, 43),
    _RlOspfRteMaxEqCostPaths_Type()
)
rlOspfRteMaxEqCostPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfRteMaxEqCostPaths.setStatus("current")
_RlOspfAreaTable_Object = MibTable
rlOspfAreaTable = _RlOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3)
)
if mibBuilder.loadTexts:
    rlOspfAreaTable.setStatus("current")
_RlOspfAreaEntry_Object = MibTableRow
rlOspfAreaEntry = _RlOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1)
)
rlOspfAreaEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfAreaProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfAreaId"),
)
if mibBuilder.loadTexts:
    rlOspfAreaEntry.setStatus("current")
_RlOspfAreaProcessId_Type = RlOspfProcessID
_RlOspfAreaProcessId_Object = MibTableColumn
rlOspfAreaProcessId = _RlOspfAreaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 1),
    _RlOspfAreaProcessId_Type()
)
rlOspfAreaProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaProcessId.setStatus("current")
_RlOspfAreaId_Type = AreaID
_RlOspfAreaId_Object = MibTableColumn
rlOspfAreaId = _RlOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 2),
    _RlOspfAreaId_Type()
)
rlOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaId.setStatus("current")


class _RlOspfAuthType_Type(RlOspfAuthenticationType):
    """Custom type rlOspfAuthType based on RlOspfAuthenticationType"""


_RlOspfAuthType_Object = MibTableColumn
rlOspfAuthType = _RlOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 3),
    _RlOspfAuthType_Type()
)
rlOspfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAuthType.setStatus("current")


class _RlOspfImportAsExtern_Type(Integer32):
    """Custom type rlOspfImportAsExtern based on Integer32"""
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


_RlOspfImportAsExtern_Type.__name__ = "Integer32"
_RlOspfImportAsExtern_Object = MibTableColumn
rlOspfImportAsExtern = _RlOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 4),
    _RlOspfImportAsExtern_Type()
)
rlOspfImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfImportAsExtern.setStatus("current")
_RlOspfSpfRuns_Type = Counter32
_RlOspfSpfRuns_Object = MibTableColumn
rlOspfSpfRuns = _RlOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 5),
    _RlOspfSpfRuns_Type()
)
rlOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSpfRuns.setStatus("current")
_RlOspfAreaBdrRtrCount_Type = Gauge32
_RlOspfAreaBdrRtrCount_Object = MibTableColumn
rlOspfAreaBdrRtrCount = _RlOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 6),
    _RlOspfAreaBdrRtrCount_Type()
)
rlOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaBdrRtrCount.setStatus("current")
_RlOspfAsBdrRtrCount_Type = Gauge32
_RlOspfAsBdrRtrCount_Object = MibTableColumn
rlOspfAsBdrRtrCount = _RlOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 7),
    _RlOspfAsBdrRtrCount_Type()
)
rlOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAsBdrRtrCount.setStatus("current")
_RlOspfAreaLsaCount_Type = Gauge32
_RlOspfAreaLsaCount_Object = MibTableColumn
rlOspfAreaLsaCount = _RlOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 8),
    _RlOspfAreaLsaCount_Type()
)
rlOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaLsaCount.setStatus("current")


class _RlOspfAreaLsaCksumSum_Type(Integer32):
    """Custom type rlOspfAreaLsaCksumSum based on Integer32"""
    defaultValue = 0


_RlOspfAreaLsaCksumSum_Object = MibTableColumn
rlOspfAreaLsaCksumSum = _RlOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 9),
    _RlOspfAreaLsaCksumSum_Type()
)
rlOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaLsaCksumSum.setStatus("current")


class _RlOspfAreaSummary_Type(Integer32):
    """Custom type rlOspfAreaSummary based on Integer32"""
    defaultValue = 1

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


_RlOspfAreaSummary_Type.__name__ = "Integer32"
_RlOspfAreaSummary_Object = MibTableColumn
rlOspfAreaSummary = _RlOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 10),
    _RlOspfAreaSummary_Type()
)
rlOspfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaSummary.setStatus("current")
_RlOspfAreaStatus_Type = RowStatus
_RlOspfAreaStatus_Object = MibTableColumn
rlOspfAreaStatus = _RlOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 11),
    _RlOspfAreaStatus_Type()
)
rlOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaStatus.setStatus("current")


class _RlOspfAreaNssaTranslatorRole_Type(Integer32):
    """Custom type rlOspfAreaNssaTranslatorRole based on Integer32"""
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


_RlOspfAreaNssaTranslatorRole_Type.__name__ = "Integer32"
_RlOspfAreaNssaTranslatorRole_Object = MibTableColumn
rlOspfAreaNssaTranslatorRole = _RlOspfAreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 12),
    _RlOspfAreaNssaTranslatorRole_Type()
)
rlOspfAreaNssaTranslatorRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaNssaTranslatorRole.setStatus("current")


class _RlOspfAreaNssaTranslatorState_Type(Integer32):
    """Custom type rlOspfAreaNssaTranslatorState based on Integer32"""
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


_RlOspfAreaNssaTranslatorState_Type.__name__ = "Integer32"
_RlOspfAreaNssaTranslatorState_Object = MibTableColumn
rlOspfAreaNssaTranslatorState = _RlOspfAreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 13),
    _RlOspfAreaNssaTranslatorState_Type()
)
rlOspfAreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaNssaTranslatorState.setStatus("current")


class _RlOspfAreaNssaTranslatorStabilityInterval_Type(PositiveInteger):
    """Custom type rlOspfAreaNssaTranslatorStabilityInterval based on PositiveInteger"""
    defaultValue = 40


_RlOspfAreaNssaTranslatorStabilityInterval_Object = MibTableColumn
rlOspfAreaNssaTranslatorStabilityInterval = _RlOspfAreaNssaTranslatorStabilityInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 14),
    _RlOspfAreaNssaTranslatorStabilityInterval_Type()
)
rlOspfAreaNssaTranslatorStabilityInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaNssaTranslatorStabilityInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfAreaNssaTranslatorStabilityInterval.setUnits("seconds")
_RlOspfAreaNssaTranslatorEvents_Type = Counter32
_RlOspfAreaNssaTranslatorEvents_Object = MibTableColumn
rlOspfAreaNssaTranslatorEvents = _RlOspfAreaNssaTranslatorEvents_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 15),
    _RlOspfAreaNssaTranslatorEvents_Type()
)
rlOspfAreaNssaTranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaNssaTranslatorEvents.setStatus("current")


class _RlOspfAreaAdminStat_Type(Status):
    """Custom type rlOspfAreaAdminStat based on Status"""


_RlOspfAreaAdminStat_Object = MibTableColumn
rlOspfAreaAdminStat = _RlOspfAreaAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 16),
    _RlOspfAreaAdminStat_Type()
)
rlOspfAreaAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaAdminStat.setStatus("current")


class _RlOspfAreaOperStatus_Type(Integer32):
    """Custom type rlOspfAreaOperStatus based on Integer32"""
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
        *(("actFailed", 5),
          ("down", 2),
          ("goingDown", 4),
          ("goingUp", 3),
          ("up", 1))
    )


_RlOspfAreaOperStatus_Type.__name__ = "Integer32"
_RlOspfAreaOperStatus_Object = MibTableColumn
rlOspfAreaOperStatus = _RlOspfAreaOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 17),
    _RlOspfAreaOperStatus_Type()
)
rlOspfAreaOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaOperStatus.setStatus("current")


class _RlOspfAreaFilterPrefixListIn_Type(DisplayString):
    """Custom type rlOspfAreaFilterPrefixListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlOspfAreaFilterPrefixListIn_Type.__name__ = "DisplayString"
_RlOspfAreaFilterPrefixListIn_Object = MibTableColumn
rlOspfAreaFilterPrefixListIn = _RlOspfAreaFilterPrefixListIn_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 18),
    _RlOspfAreaFilterPrefixListIn_Type()
)
rlOspfAreaFilterPrefixListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaFilterPrefixListIn.setStatus("current")


class _RlOspfAreaFilterPrefixListOut_Type(DisplayString):
    """Custom type rlOspfAreaFilterPrefixListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlOspfAreaFilterPrefixListOut_Type.__name__ = "DisplayString"
_RlOspfAreaFilterPrefixListOut_Object = MibTableColumn
rlOspfAreaFilterPrefixListOut = _RlOspfAreaFilterPrefixListOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 3, 1, 19),
    _RlOspfAreaFilterPrefixListOut_Type()
)
rlOspfAreaFilterPrefixListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaFilterPrefixListOut.setStatus("current")
_RlOspfStubAreaTable_Object = MibTable
rlOspfStubAreaTable = _RlOspfStubAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 4)
)
if mibBuilder.loadTexts:
    rlOspfStubAreaTable.setStatus("current")
_RlOspfStubAreaEntry_Object = MibTableRow
rlOspfStubAreaEntry = _RlOspfStubAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 4, 1)
)
rlOspfStubAreaEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfStubProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfStubAreaId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfStubTOS"),
)
if mibBuilder.loadTexts:
    rlOspfStubAreaEntry.setStatus("current")
_RlOspfStubProcessId_Type = RlOspfProcessID
_RlOspfStubProcessId_Object = MibTableColumn
rlOspfStubProcessId = _RlOspfStubProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 4, 1, 1),
    _RlOspfStubProcessId_Type()
)
rlOspfStubProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfStubProcessId.setStatus("current")
_RlOspfStubAreaId_Type = AreaID
_RlOspfStubAreaId_Object = MibTableColumn
rlOspfStubAreaId = _RlOspfStubAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 4, 1, 2),
    _RlOspfStubAreaId_Type()
)
rlOspfStubAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfStubAreaId.setStatus("current")
_RlOspfStubTOS_Type = TOSType
_RlOspfStubTOS_Object = MibTableColumn
rlOspfStubTOS = _RlOspfStubTOS_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 4, 1, 3),
    _RlOspfStubTOS_Type()
)
rlOspfStubTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfStubTOS.setStatus("current")
_RlOspfStubMetric_Type = BigMetric
_RlOspfStubMetric_Object = MibTableColumn
rlOspfStubMetric = _RlOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 4, 1, 4),
    _RlOspfStubMetric_Type()
)
rlOspfStubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfStubMetric.setStatus("current")
_RlOspfStubStatus_Type = RowStatus
_RlOspfStubStatus_Object = MibTableColumn
rlOspfStubStatus = _RlOspfStubStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 4, 1, 5),
    _RlOspfStubStatus_Type()
)
rlOspfStubStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfStubStatus.setStatus("current")


class _RlOspfStubMetricType_Type(Integer32):
    """Custom type rlOspfStubMetricType based on Integer32"""
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
          ("ospfMetric", 1))
    )


_RlOspfStubMetricType_Type.__name__ = "Integer32"
_RlOspfStubMetricType_Object = MibTableColumn
rlOspfStubMetricType = _RlOspfStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 4, 1, 6),
    _RlOspfStubMetricType_Type()
)
rlOspfStubMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfStubMetricType.setStatus("current")
_RlOspfLsdbTable_Object = MibTable
rlOspfLsdbTable = _RlOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 5)
)
if mibBuilder.loadTexts:
    rlOspfLsdbTable.setStatus("current")
_RlOspfLsdbEntry_Object = MibTableRow
rlOspfLsdbEntry = _RlOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 5, 1)
)
rlOspfLsdbEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfLsdbProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfLsdbAreaId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfLsdbType"),
    (0, "RADLAN-OSPF-MIB", "rlOspfLsdbLsid"),
    (0, "RADLAN-OSPF-MIB", "rlOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfLsdbEntry.setStatus("current")
_RlOspfLsdbProcessId_Type = RlOspfProcessID
_RlOspfLsdbProcessId_Object = MibTableColumn
rlOspfLsdbProcessId = _RlOspfLsdbProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 5, 1, 1),
    _RlOspfLsdbProcessId_Type()
)
rlOspfLsdbProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLsdbProcessId.setStatus("current")
_RlOspfLsdbAreaId_Type = AreaID
_RlOspfLsdbAreaId_Object = MibTableColumn
rlOspfLsdbAreaId = _RlOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 5, 1, 2),
    _RlOspfLsdbAreaId_Type()
)
rlOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLsdbAreaId.setStatus("current")


class _RlOspfLsdbType_Type(Integer32):
    """Custom type rlOspfLsdbType based on Integer32"""
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


_RlOspfLsdbType_Type.__name__ = "Integer32"
_RlOspfLsdbType_Object = MibTableColumn
rlOspfLsdbType = _RlOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 5, 1, 3),
    _RlOspfLsdbType_Type()
)
rlOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLsdbType.setStatus("current")
_RlOspfLsdbLsid_Type = IpAddress
_RlOspfLsdbLsid_Object = MibTableColumn
rlOspfLsdbLsid = _RlOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 5, 1, 4),
    _RlOspfLsdbLsid_Type()
)
rlOspfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLsdbLsid.setStatus("current")
_RlOspfLsdbRouterId_Type = RouterID
_RlOspfLsdbRouterId_Object = MibTableColumn
rlOspfLsdbRouterId = _RlOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 5, 1, 5),
    _RlOspfLsdbRouterId_Type()
)
rlOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLsdbRouterId.setStatus("current")
_RlOspfLsdbSequence_Type = Integer32
_RlOspfLsdbSequence_Object = MibTableColumn
rlOspfLsdbSequence = _RlOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 5, 1, 6),
    _RlOspfLsdbSequence_Type()
)
rlOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLsdbSequence.setStatus("current")
_RlOspfLsdbAge_Type = Integer32
_RlOspfLsdbAge_Object = MibTableColumn
rlOspfLsdbAge = _RlOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 5, 1, 7),
    _RlOspfLsdbAge_Type()
)
rlOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfLsdbAge.setUnits("seconds")
_RlOspfLsdbChecksum_Type = Integer32
_RlOspfLsdbChecksum_Object = MibTableColumn
rlOspfLsdbChecksum = _RlOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 5, 1, 8),
    _RlOspfLsdbChecksum_Type()
)
rlOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLsdbChecksum.setStatus("current")


class _RlOspfLsdbAdvertisement_Type(OctetString):
    """Custom type rlOspfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_RlOspfLsdbAdvertisement_Type.__name__ = "OctetString"
_RlOspfLsdbAdvertisement_Object = MibTableColumn
rlOspfLsdbAdvertisement = _RlOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 5, 1, 9),
    _RlOspfLsdbAdvertisement_Type()
)
rlOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLsdbAdvertisement.setStatus("current")
_RlOspfAreaRangeTable_Object = MibTable
rlOspfAreaRangeTable = _RlOspfAreaRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 6)
)
if mibBuilder.loadTexts:
    rlOspfAreaRangeTable.setStatus("obsolete")
_RlOspfAreaRangeEntry_Object = MibTableRow
rlOspfAreaRangeEntry = _RlOspfAreaRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 6, 1)
)
rlOspfAreaRangeEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfAreaRangeProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfAreaRangeAreaId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfAreaRangeNet"),
)
if mibBuilder.loadTexts:
    rlOspfAreaRangeEntry.setStatus("obsolete")
_RlOspfAreaRangeProcessId_Type = RlOspfProcessID
_RlOspfAreaRangeProcessId_Object = MibTableColumn
rlOspfAreaRangeProcessId = _RlOspfAreaRangeProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 6, 1, 1),
    _RlOspfAreaRangeProcessId_Type()
)
rlOspfAreaRangeProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaRangeProcessId.setStatus("obsolete")
_RlOspfAreaRangeAreaId_Type = AreaID
_RlOspfAreaRangeAreaId_Object = MibTableColumn
rlOspfAreaRangeAreaId = _RlOspfAreaRangeAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 6, 1, 2),
    _RlOspfAreaRangeAreaId_Type()
)
rlOspfAreaRangeAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaRangeAreaId.setStatus("obsolete")
_RlOspfAreaRangeNet_Type = IpAddress
_RlOspfAreaRangeNet_Object = MibTableColumn
rlOspfAreaRangeNet = _RlOspfAreaRangeNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 6, 1, 3),
    _RlOspfAreaRangeNet_Type()
)
rlOspfAreaRangeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaRangeNet.setStatus("obsolete")
_RlOspfAreaRangeMask_Type = IpAddress
_RlOspfAreaRangeMask_Object = MibTableColumn
rlOspfAreaRangeMask = _RlOspfAreaRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 6, 1, 4),
    _RlOspfAreaRangeMask_Type()
)
rlOspfAreaRangeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaRangeMask.setStatus("obsolete")
_RlOspfAreaRangeStatus_Type = RowStatus
_RlOspfAreaRangeStatus_Object = MibTableColumn
rlOspfAreaRangeStatus = _RlOspfAreaRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 6, 1, 5),
    _RlOspfAreaRangeStatus_Type()
)
rlOspfAreaRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaRangeStatus.setStatus("obsolete")


class _RlOspfAreaRangeEffect_Type(Integer32):
    """Custom type rlOspfAreaRangeEffect based on Integer32"""
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


_RlOspfAreaRangeEffect_Type.__name__ = "Integer32"
_RlOspfAreaRangeEffect_Object = MibTableColumn
rlOspfAreaRangeEffect = _RlOspfAreaRangeEffect_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 6, 1, 6),
    _RlOspfAreaRangeEffect_Type()
)
rlOspfAreaRangeEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaRangeEffect.setStatus("obsolete")
_RlOspfHostTable_Object = MibTable
rlOspfHostTable = _RlOspfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 7)
)
if mibBuilder.loadTexts:
    rlOspfHostTable.setStatus("current")
_RlOspfHostEntry_Object = MibTableRow
rlOspfHostEntry = _RlOspfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 7, 1)
)
rlOspfHostEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfHostProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfHostIpAddress"),
    (0, "RADLAN-OSPF-MIB", "rlOspfHostTOS"),
)
if mibBuilder.loadTexts:
    rlOspfHostEntry.setStatus("current")
_RlOspfHostProcessId_Type = RlOspfProcessID
_RlOspfHostProcessId_Object = MibTableColumn
rlOspfHostProcessId = _RlOspfHostProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 7, 1, 1),
    _RlOspfHostProcessId_Type()
)
rlOspfHostProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfHostProcessId.setStatus("current")
_RlOspfHostIpAddress_Type = IpAddress
_RlOspfHostIpAddress_Object = MibTableColumn
rlOspfHostIpAddress = _RlOspfHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 7, 1, 2),
    _RlOspfHostIpAddress_Type()
)
rlOspfHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfHostIpAddress.setStatus("current")
_RlOspfHostTOS_Type = TOSType
_RlOspfHostTOS_Object = MibTableColumn
rlOspfHostTOS = _RlOspfHostTOS_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 7, 1, 3),
    _RlOspfHostTOS_Type()
)
rlOspfHostTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfHostTOS.setStatus("current")
_RlOspfHostMetric_Type = Metric
_RlOspfHostMetric_Object = MibTableColumn
rlOspfHostMetric = _RlOspfHostMetric_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 7, 1, 4),
    _RlOspfHostMetric_Type()
)
rlOspfHostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfHostMetric.setStatus("current")
_RlOspfHostStatus_Type = RowStatus
_RlOspfHostStatus_Object = MibTableColumn
rlOspfHostStatus = _RlOspfHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 7, 1, 5),
    _RlOspfHostStatus_Type()
)
rlOspfHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfHostStatus.setStatus("current")
_RlOspfHostAreaID_Type = AreaID
_RlOspfHostAreaID_Object = MibTableColumn
rlOspfHostAreaID = _RlOspfHostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 7, 1, 6),
    _RlOspfHostAreaID_Type()
)
rlOspfHostAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfHostAreaID.setStatus("deprecated")
_RlOspfHostCfgAreaID_Type = AreaID
_RlOspfHostCfgAreaID_Object = MibTableColumn
rlOspfHostCfgAreaID = _RlOspfHostCfgAreaID_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 7, 1, 7),
    _RlOspfHostCfgAreaID_Type()
)
rlOspfHostCfgAreaID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfHostCfgAreaID.setStatus("current")
_RlOspfIfTable_Object = MibTable
rlOspfIfTable = _RlOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8)
)
if mibBuilder.loadTexts:
    rlOspfIfTable.setStatus("current")
_RlOspfIfEntry_Object = MibTableRow
rlOspfIfEntry = _RlOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1)
)
rlOspfIfEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfIfProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfIfIpAddress"),
    (0, "RADLAN-OSPF-MIB", "rlOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    rlOspfIfEntry.setStatus("current")
_RlOspfIfProcessId_Type = RlOspfProcessID
_RlOspfIfProcessId_Object = MibTableColumn
rlOspfIfProcessId = _RlOspfIfProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 1),
    _RlOspfIfProcessId_Type()
)
rlOspfIfProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfProcessId.setStatus("current")
_RlOspfIfIpAddress_Type = IpAddress
_RlOspfIfIpAddress_Object = MibTableColumn
rlOspfIfIpAddress = _RlOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 2),
    _RlOspfIfIpAddress_Type()
)
rlOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfIpAddress.setStatus("current")
_RlOspfAddressLessIf_Type = InterfaceIndexOrZero
_RlOspfAddressLessIf_Object = MibTableColumn
rlOspfAddressLessIf = _RlOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 3),
    _RlOspfAddressLessIf_Type()
)
rlOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAddressLessIf.setStatus("current")


class _RlOspfIfAreaId_Type(AreaID):
    """Custom type rlOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_RlOspfIfAreaId_Object = MibTableColumn
rlOspfIfAreaId = _RlOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 4),
    _RlOspfIfAreaId_Type()
)
rlOspfIfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfAreaId.setStatus("current")


class _RlOspfIfType_Type(Integer32):
    """Custom type rlOspfIfType based on Integer32"""
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


_RlOspfIfType_Type.__name__ = "Integer32"
_RlOspfIfType_Object = MibTableColumn
rlOspfIfType = _RlOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 5),
    _RlOspfIfType_Type()
)
rlOspfIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfType.setStatus("current")


class _RlOspfIfAdminStat_Type(Status):
    """Custom type rlOspfIfAdminStat based on Status"""


_RlOspfIfAdminStat_Object = MibTableColumn
rlOspfIfAdminStat = _RlOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 6),
    _RlOspfIfAdminStat_Type()
)
rlOspfIfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfAdminStat.setStatus("current")


class _RlOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type rlOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_RlOspfIfRtrPriority_Object = MibTableColumn
rlOspfIfRtrPriority = _RlOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 7),
    _RlOspfIfRtrPriority_Type()
)
rlOspfIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfRtrPriority.setStatus("current")


class _RlOspfIfTransitDelay_Type(RlOspfUpToRefreshIntervalTC):
    """Custom type rlOspfIfTransitDelay based on RlOspfUpToRefreshIntervalTC"""
    defaultValue = 1


_RlOspfIfTransitDelay_Object = MibTableColumn
rlOspfIfTransitDelay = _RlOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 8),
    _RlOspfIfTransitDelay_Type()
)
rlOspfIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfIfTransitDelay.setUnits("seconds")


class _RlOspfIfRetransInterval_Type(RlOspfUpToRefreshIntervalTC):
    """Custom type rlOspfIfRetransInterval based on RlOspfUpToRefreshIntervalTC"""
    defaultValue = 5


_RlOspfIfRetransInterval_Object = MibTableColumn
rlOspfIfRetransInterval = _RlOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 9),
    _RlOspfIfRetransInterval_Type()
)
rlOspfIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfIfRetransInterval.setUnits("seconds")


class _RlOspfIfHelloInterval_Type(HelloRange):
    """Custom type rlOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_RlOspfIfHelloInterval_Object = MibTableColumn
rlOspfIfHelloInterval = _RlOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 10),
    _RlOspfIfHelloInterval_Type()
)
rlOspfIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfIfHelloInterval.setUnits("seconds")


class _RlOspfIfRtrDeadInterval_Type(RlOspfDeadIntervalRangeTC):
    """Custom type rlOspfIfRtrDeadInterval based on RlOspfDeadIntervalRangeTC"""
    defaultValue = 40


_RlOspfIfRtrDeadInterval_Object = MibTableColumn
rlOspfIfRtrDeadInterval = _RlOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 11),
    _RlOspfIfRtrDeadInterval_Type()
)
rlOspfIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfIfRtrDeadInterval.setUnits("seconds")


class _RlOspfIfPollInterval_Type(PositiveInteger):
    """Custom type rlOspfIfPollInterval based on PositiveInteger"""
    defaultValue = 120


_RlOspfIfPollInterval_Object = MibTableColumn
rlOspfIfPollInterval = _RlOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 12),
    _RlOspfIfPollInterval_Type()
)
rlOspfIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfIfPollInterval.setUnits("seconds")


class _RlOspfIfState_Type(Integer32):
    """Custom type rlOspfIfState based on Integer32"""
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


_RlOspfIfState_Type.__name__ = "Integer32"
_RlOspfIfState_Object = MibTableColumn
rlOspfIfState = _RlOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 13),
    _RlOspfIfState_Type()
)
rlOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfState.setStatus("current")


class _RlOspfIfDesignatedRouter_Type(IpAddress):
    """Custom type rlOspfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_RlOspfIfDesignatedRouter_Object = MibTableColumn
rlOspfIfDesignatedRouter = _RlOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 14),
    _RlOspfIfDesignatedRouter_Type()
)
rlOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfDesignatedRouter.setStatus("current")


class _RlOspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type rlOspfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_RlOspfIfBackupDesignatedRouter_Object = MibTableColumn
rlOspfIfBackupDesignatedRouter = _RlOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 15),
    _RlOspfIfBackupDesignatedRouter_Type()
)
rlOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfBackupDesignatedRouter.setStatus("current")
_RlOspfIfEvents_Type = Counter32
_RlOspfIfEvents_Object = MibTableColumn
rlOspfIfEvents = _RlOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 16),
    _RlOspfIfEvents_Type()
)
rlOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfEvents.setStatus("current")


class _RlOspfIfAuthKey_Type(OctetString):
    """Custom type rlOspfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RlOspfIfAuthKey_Type.__name__ = "OctetString"
_RlOspfIfAuthKey_Object = MibTableColumn
rlOspfIfAuthKey = _RlOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 17),
    _RlOspfIfAuthKey_Type()
)
rlOspfIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfAuthKey.setStatus("current")
_RlOspfIfStatus_Type = RowStatus
_RlOspfIfStatus_Object = MibTableColumn
rlOspfIfStatus = _RlOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 18),
    _RlOspfIfStatus_Type()
)
rlOspfIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfStatus.setStatus("current")


class _RlOspfIfMulticastForwarding_Type(Integer32):
    """Custom type rlOspfIfMulticastForwarding based on Integer32"""
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


_RlOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_RlOspfIfMulticastForwarding_Object = MibTableColumn
rlOspfIfMulticastForwarding = _RlOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 19),
    _RlOspfIfMulticastForwarding_Type()
)
rlOspfIfMulticastForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfMulticastForwarding.setStatus("current")


class _RlOspfIfDemand_Type(TruthValue):
    """Custom type rlOspfIfDemand based on TruthValue"""


_RlOspfIfDemand_Object = MibTableColumn
rlOspfIfDemand = _RlOspfIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 20),
    _RlOspfIfDemand_Type()
)
rlOspfIfDemand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfDemand.setStatus("current")


class _RlOspfIfAuthType_Type(RlOspfAuthenticationType):
    """Custom type rlOspfIfAuthType based on RlOspfAuthenticationType"""


_RlOspfIfAuthType_Object = MibTableColumn
rlOspfIfAuthType = _RlOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 21),
    _RlOspfIfAuthType_Type()
)
rlOspfIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfAuthType.setStatus("current")
_RlOspfIfLsaCount_Type = Gauge32
_RlOspfIfLsaCount_Object = MibTableColumn
rlOspfIfLsaCount = _RlOspfIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 22),
    _RlOspfIfLsaCount_Type()
)
rlOspfIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfLsaCount.setStatus("current")
_RlOspfIfLsaCksumSum_Type = Unsigned32
_RlOspfIfLsaCksumSum_Object = MibTableColumn
rlOspfIfLsaCksumSum = _RlOspfIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 23),
    _RlOspfIfLsaCksumSum_Type()
)
rlOspfIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfLsaCksumSum.setStatus("current")
_RlOspfIfDesignatedRouterId_Type = RouterID
_RlOspfIfDesignatedRouterId_Object = MibTableColumn
rlOspfIfDesignatedRouterId = _RlOspfIfDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 24),
    _RlOspfIfDesignatedRouterId_Type()
)
rlOspfIfDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfDesignatedRouterId.setStatus("current")
_RlOspfIfBackupDesignatedRouterId_Type = RouterID
_RlOspfIfBackupDesignatedRouterId_Object = MibTableColumn
rlOspfIfBackupDesignatedRouterId = _RlOspfIfBackupDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 25),
    _RlOspfIfBackupDesignatedRouterId_Type()
)
rlOspfIfBackupDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfBackupDesignatedRouterId.setStatus("current")


class _RlOspfIfOperStatus_Type(Integer32):
    """Custom type rlOspfIfOperStatus based on Integer32"""
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
        *(("actFailed", 5),
          ("down", 2),
          ("goingDown", 4),
          ("goingUp", 3),
          ("up", 1))
    )


_RlOspfIfOperStatus_Type.__name__ = "Integer32"
_RlOspfIfOperStatus_Object = MibTableColumn
rlOspfIfOperStatus = _RlOspfIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 26),
    _RlOspfIfOperStatus_Type()
)
rlOspfIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfOperStatus.setStatus("current")


class _RlOspfIfAuthKeyChain_Type(OctetString):
    """Custom type rlOspfIfAuthKeyChain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RlOspfIfAuthKeyChain_Type.__name__ = "OctetString"
_RlOspfIfAuthKeyChain_Object = MibTableColumn
rlOspfIfAuthKeyChain = _RlOspfIfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 27),
    _RlOspfIfAuthKeyChain_Type()
)
rlOspfIfAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfAuthKeyChain.setStatus("current")


class _RlOspfIfPassive_Type(TruthValue):
    """Custom type rlOspfIfPassive based on TruthValue"""


_RlOspfIfPassive_Object = MibTableColumn
rlOspfIfPassive = _RlOspfIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 28),
    _RlOspfIfPassive_Type()
)
rlOspfIfPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfIfPassive.setStatus("current")


class _RlOspfIfLsaRefreshIntvl_Type(Integer32):
    """Custom type rlOspfIfLsaRefreshIntvl based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_RlOspfIfLsaRefreshIntvl_Type.__name__ = "Integer32"
_RlOspfIfLsaRefreshIntvl_Object = MibTableColumn
rlOspfIfLsaRefreshIntvl = _RlOspfIfLsaRefreshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 29),
    _RlOspfIfLsaRefreshIntvl_Type()
)
rlOspfIfLsaRefreshIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfIfLsaRefreshIntvl.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfIfLsaRefreshIntvl.setUnits("seconds")


class _RlOspfIfFastHelloMultiplier_Type(RlOspfFastHelloMultiplierRange):
    """Custom type rlOspfIfFastHelloMultiplier based on RlOspfFastHelloMultiplierRange"""
    defaultValue = 5


_RlOspfIfFastHelloMultiplier_Object = MibTableColumn
rlOspfIfFastHelloMultiplier = _RlOspfIfFastHelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 30),
    _RlOspfIfFastHelloMultiplier_Type()
)
rlOspfIfFastHelloMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfFastHelloMultiplier.setStatus("current")


class _RlOspfIfMtuIgnore_Type(TruthValue):
    """Custom type rlOspfIfMtuIgnore based on TruthValue"""


_RlOspfIfMtuIgnore_Object = MibTableColumn
rlOspfIfMtuIgnore = _RlOspfIfMtuIgnore_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 31),
    _RlOspfIfMtuIgnore_Type()
)
rlOspfIfMtuIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfIfMtuIgnore.setStatus("current")
_RlOspfIfNameLookup_Type = TruthValue
_RlOspfIfNameLookup_Object = MibTableColumn
rlOspfIfNameLookup = _RlOspfIfNameLookup_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 32),
    _RlOspfIfNameLookup_Type()
)
rlOspfIfNameLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfIfNameLookup.setStatus("current")
_RlOspfIfIfIndex_Type = Integer32
_RlOspfIfIfIndex_Object = MibTableColumn
rlOspfIfIfIndex = _RlOspfIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 33),
    _RlOspfIfIfIndex_Type()
)
rlOspfIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfIfIndex.setStatus("current")
_RlOspfIfActualAuthType_Type = RlOspfAuthenticationType
_RlOspfIfActualAuthType_Object = MibTableColumn
rlOspfIfActualAuthType = _RlOspfIfActualAuthType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 8, 1, 34),
    _RlOspfIfActualAuthType_Type()
)
rlOspfIfActualAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfActualAuthType.setStatus("current")
_RlOspfIfMetricTable_Object = MibTable
rlOspfIfMetricTable = _RlOspfIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 9)
)
if mibBuilder.loadTexts:
    rlOspfIfMetricTable.setStatus("current")
_RlOspfIfMetricEntry_Object = MibTableRow
rlOspfIfMetricEntry = _RlOspfIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 9, 1)
)
rlOspfIfMetricEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfIfMetricProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfIfMetricIpAddress"),
    (0, "RADLAN-OSPF-MIB", "rlOspfIfMetricAddressLessIf"),
    (0, "RADLAN-OSPF-MIB", "rlOspfIfMetricTOS"),
)
if mibBuilder.loadTexts:
    rlOspfIfMetricEntry.setStatus("current")
_RlOspfIfMetricProcessId_Type = RlOspfProcessID
_RlOspfIfMetricProcessId_Object = MibTableColumn
rlOspfIfMetricProcessId = _RlOspfIfMetricProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 9, 1, 1),
    _RlOspfIfMetricProcessId_Type()
)
rlOspfIfMetricProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfMetricProcessId.setStatus("current")
_RlOspfIfMetricIpAddress_Type = IpAddress
_RlOspfIfMetricIpAddress_Object = MibTableColumn
rlOspfIfMetricIpAddress = _RlOspfIfMetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 9, 1, 2),
    _RlOspfIfMetricIpAddress_Type()
)
rlOspfIfMetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfMetricIpAddress.setStatus("current")
_RlOspfIfMetricAddressLessIf_Type = InterfaceIndexOrZero
_RlOspfIfMetricAddressLessIf_Object = MibTableColumn
rlOspfIfMetricAddressLessIf = _RlOspfIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 9, 1, 3),
    _RlOspfIfMetricAddressLessIf_Type()
)
rlOspfIfMetricAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfMetricAddressLessIf.setStatus("current")
_RlOspfIfMetricTOS_Type = TOSType
_RlOspfIfMetricTOS_Object = MibTableColumn
rlOspfIfMetricTOS = _RlOspfIfMetricTOS_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 9, 1, 4),
    _RlOspfIfMetricTOS_Type()
)
rlOspfIfMetricTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfIfMetricTOS.setStatus("current")
_RlOspfIfMetricValue_Type = Metric
_RlOspfIfMetricValue_Object = MibTableColumn
rlOspfIfMetricValue = _RlOspfIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 9, 1, 5),
    _RlOspfIfMetricValue_Type()
)
rlOspfIfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfMetricValue.setStatus("current")
_RlOspfIfMetricStatus_Type = RowStatus
_RlOspfIfMetricStatus_Object = MibTableColumn
rlOspfIfMetricStatus = _RlOspfIfMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 9, 1, 6),
    _RlOspfIfMetricStatus_Type()
)
rlOspfIfMetricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfIfMetricStatus.setStatus("current")
_RlOspfVirtIfTable_Object = MibTable
rlOspfVirtIfTable = _RlOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10)
)
if mibBuilder.loadTexts:
    rlOspfVirtIfTable.setStatus("current")
_RlOspfVirtIfEntry_Object = MibTableRow
rlOspfVirtIfEntry = _RlOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1)
)
rlOspfVirtIfEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtIfProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtIfAreaId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    rlOspfVirtIfEntry.setStatus("current")
_RlOspfVirtIfProcessId_Type = RlOspfProcessID
_RlOspfVirtIfProcessId_Object = MibTableColumn
rlOspfVirtIfProcessId = _RlOspfVirtIfProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 1),
    _RlOspfVirtIfProcessId_Type()
)
rlOspfVirtIfProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtIfProcessId.setStatus("current")
_RlOspfVirtIfAreaId_Type = AreaID
_RlOspfVirtIfAreaId_Object = MibTableColumn
rlOspfVirtIfAreaId = _RlOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 2),
    _RlOspfVirtIfAreaId_Type()
)
rlOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtIfAreaId.setStatus("current")
_RlOspfVirtIfNeighbor_Type = RouterID
_RlOspfVirtIfNeighbor_Object = MibTableColumn
rlOspfVirtIfNeighbor = _RlOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 3),
    _RlOspfVirtIfNeighbor_Type()
)
rlOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtIfNeighbor.setStatus("current")


class _RlOspfVirtIfTransitDelay_Type(RlOspfUpToRefreshIntervalTC):
    """Custom type rlOspfVirtIfTransitDelay based on RlOspfUpToRefreshIntervalTC"""
    defaultValue = 1


_RlOspfVirtIfTransitDelay_Object = MibTableColumn
rlOspfVirtIfTransitDelay = _RlOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 4),
    _RlOspfVirtIfTransitDelay_Type()
)
rlOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfVirtIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfVirtIfTransitDelay.setUnits("seconds")


class _RlOspfVirtIfRetransInterval_Type(RlOspfUpToRefreshIntervalTC):
    """Custom type rlOspfVirtIfRetransInterval based on RlOspfUpToRefreshIntervalTC"""
    defaultValue = 5


_RlOspfVirtIfRetransInterval_Object = MibTableColumn
rlOspfVirtIfRetransInterval = _RlOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 5),
    _RlOspfVirtIfRetransInterval_Type()
)
rlOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfVirtIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfVirtIfRetransInterval.setUnits("seconds")


class _RlOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type rlOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_RlOspfVirtIfHelloInterval_Object = MibTableColumn
rlOspfVirtIfHelloInterval = _RlOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 6),
    _RlOspfVirtIfHelloInterval_Type()
)
rlOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfVirtIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfVirtIfHelloInterval.setUnits("seconds")


class _RlOspfVirtIfRtrDeadInterval_Type(RlOspfDeadIntervalRangeTC):
    """Custom type rlOspfVirtIfRtrDeadInterval based on RlOspfDeadIntervalRangeTC"""
    defaultValue = 60


_RlOspfVirtIfRtrDeadInterval_Object = MibTableColumn
rlOspfVirtIfRtrDeadInterval = _RlOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 7),
    _RlOspfVirtIfRtrDeadInterval_Type()
)
rlOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfVirtIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfVirtIfRtrDeadInterval.setUnits("seconds")


class _RlOspfVirtIfState_Type(Integer32):
    """Custom type rlOspfVirtIfState based on Integer32"""
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


_RlOspfVirtIfState_Type.__name__ = "Integer32"
_RlOspfVirtIfState_Object = MibTableColumn
rlOspfVirtIfState = _RlOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 8),
    _RlOspfVirtIfState_Type()
)
rlOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtIfState.setStatus("current")
_RlOspfVirtIfEvents_Type = Counter32
_RlOspfVirtIfEvents_Object = MibTableColumn
rlOspfVirtIfEvents = _RlOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 9),
    _RlOspfVirtIfEvents_Type()
)
rlOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtIfEvents.setStatus("current")


class _RlOspfVirtIfAuthKey_Type(OctetString):
    """Custom type rlOspfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RlOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_RlOspfVirtIfAuthKey_Object = MibTableColumn
rlOspfVirtIfAuthKey = _RlOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 10),
    _RlOspfVirtIfAuthKey_Type()
)
rlOspfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfVirtIfAuthKey.setStatus("current")
_RlOspfVirtIfStatus_Type = RowStatus
_RlOspfVirtIfStatus_Object = MibTableColumn
rlOspfVirtIfStatus = _RlOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 11),
    _RlOspfVirtIfStatus_Type()
)
rlOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfVirtIfStatus.setStatus("current")


class _RlOspfVirtIfAuthType_Type(RlOspfAuthenticationType):
    """Custom type rlOspfVirtIfAuthType based on RlOspfAuthenticationType"""


_RlOspfVirtIfAuthType_Object = MibTableColumn
rlOspfVirtIfAuthType = _RlOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 12),
    _RlOspfVirtIfAuthType_Type()
)
rlOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfVirtIfAuthType.setStatus("current")
_RlOspfVirtIfLsaCount_Type = Gauge32
_RlOspfVirtIfLsaCount_Object = MibTableColumn
rlOspfVirtIfLsaCount = _RlOspfVirtIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 13),
    _RlOspfVirtIfLsaCount_Type()
)
rlOspfVirtIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtIfLsaCount.setStatus("current")
_RlOspfVirtIfLsaCksumSum_Type = Unsigned32
_RlOspfVirtIfLsaCksumSum_Object = MibTableColumn
rlOspfVirtIfLsaCksumSum = _RlOspfVirtIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 14),
    _RlOspfVirtIfLsaCksumSum_Type()
)
rlOspfVirtIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtIfLsaCksumSum.setStatus("current")


class _RlOspfVirtIfAuthKeyChain_Type(OctetString):
    """Custom type rlOspfVirtIfAuthKeyChain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RlOspfVirtIfAuthKeyChain_Type.__name__ = "OctetString"
_RlOspfVirtIfAuthKeyChain_Object = MibTableColumn
rlOspfVirtIfAuthKeyChain = _RlOspfVirtIfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 15),
    _RlOspfVirtIfAuthKeyChain_Type()
)
rlOspfVirtIfAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfVirtIfAuthKeyChain.setStatus("current")


class _RlOspfVirtIfAdminStatus_Type(Status):
    """Custom type rlOspfVirtIfAdminStatus based on Status"""


_RlOspfVirtIfAdminStatus_Object = MibTableColumn
rlOspfVirtIfAdminStatus = _RlOspfVirtIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 16),
    _RlOspfVirtIfAdminStatus_Type()
)
rlOspfVirtIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfVirtIfAdminStatus.setStatus("current")


class _RlOspfVirtIfOperStatus_Type(Integer32):
    """Custom type rlOspfVirtIfOperStatus based on Integer32"""
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
        *(("actFailed", 5),
          ("down", 2),
          ("goingDown", 4),
          ("goingUp", 3),
          ("up", 1))
    )


_RlOspfVirtIfOperStatus_Type.__name__ = "Integer32"
_RlOspfVirtIfOperStatus_Object = MibTableColumn
rlOspfVirtIfOperStatus = _RlOspfVirtIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 17),
    _RlOspfVirtIfOperStatus_Type()
)
rlOspfVirtIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtIfOperStatus.setStatus("current")
_RlOspfVirtIfIndex_Type = Integer32
_RlOspfVirtIfIndex_Object = MibTableColumn
rlOspfVirtIfIndex = _RlOspfVirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 18),
    _RlOspfVirtIfIndex_Type()
)
rlOspfVirtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtIfIndex.setStatus("current")
_RlOspfVirtIfActualAuthType_Type = RlOspfAuthenticationType
_RlOspfVirtIfActualAuthType_Object = MibTableColumn
rlOspfVirtIfActualAuthType = _RlOspfVirtIfActualAuthType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 10, 1, 19),
    _RlOspfVirtIfActualAuthType_Type()
)
rlOspfVirtIfActualAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtIfActualAuthType.setStatus("current")
_RlOspfNbrTable_Object = MibTable
rlOspfNbrTable = _RlOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11)
)
if mibBuilder.loadTexts:
    rlOspfNbrTable.setStatus("current")
_RlOspfNbrEntry_Object = MibTableRow
rlOspfNbrEntry = _RlOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1)
)
rlOspfNbrEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfNbrProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfNbrIpAddr"),
    (0, "RADLAN-OSPF-MIB", "rlOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    rlOspfNbrEntry.setStatus("current")
_RlOspfNbrProcessId_Type = RlOspfProcessID
_RlOspfNbrProcessId_Object = MibTableColumn
rlOspfNbrProcessId = _RlOspfNbrProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 1),
    _RlOspfNbrProcessId_Type()
)
rlOspfNbrProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrProcessId.setStatus("current")
_RlOspfNbrIpAddr_Type = IpAddress
_RlOspfNbrIpAddr_Object = MibTableColumn
rlOspfNbrIpAddr = _RlOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 2),
    _RlOspfNbrIpAddr_Type()
)
rlOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrIpAddr.setStatus("current")
_RlOspfNbrAddressLessIndex_Type = InterfaceIndexOrZero
_RlOspfNbrAddressLessIndex_Object = MibTableColumn
rlOspfNbrAddressLessIndex = _RlOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 3),
    _RlOspfNbrAddressLessIndex_Type()
)
rlOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrAddressLessIndex.setStatus("current")


class _RlOspfNbrRtrId_Type(RouterID):
    """Custom type rlOspfNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_RlOspfNbrRtrId_Object = MibTableColumn
rlOspfNbrRtrId = _RlOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 4),
    _RlOspfNbrRtrId_Type()
)
rlOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrRtrId.setStatus("current")


class _RlOspfNbrOptions_Type(Integer32):
    """Custom type rlOspfNbrOptions based on Integer32"""
    defaultValue = 0


_RlOspfNbrOptions_Object = MibTableColumn
rlOspfNbrOptions = _RlOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 5),
    _RlOspfNbrOptions_Type()
)
rlOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrOptions.setStatus("current")


class _RlOspfNbrPriority_Type(DesignatedRouterPriority):
    """Custom type rlOspfNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_RlOspfNbrPriority_Object = MibTableColumn
rlOspfNbrPriority = _RlOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 6),
    _RlOspfNbrPriority_Type()
)
rlOspfNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfNbrPriority.setStatus("current")


class _RlOspfNbrState_Type(Integer32):
    """Custom type rlOspfNbrState based on Integer32"""
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


_RlOspfNbrState_Type.__name__ = "Integer32"
_RlOspfNbrState_Object = MibTableColumn
rlOspfNbrState = _RlOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 7),
    _RlOspfNbrState_Type()
)
rlOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrState.setStatus("current")
_RlOspfNbrEvents_Type = Counter32
_RlOspfNbrEvents_Object = MibTableColumn
rlOspfNbrEvents = _RlOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 8),
    _RlOspfNbrEvents_Type()
)
rlOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrEvents.setStatus("current")
_RlOspfNbrLsRetransQLen_Type = Gauge32
_RlOspfNbrLsRetransQLen_Object = MibTableColumn
rlOspfNbrLsRetransQLen = _RlOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 9),
    _RlOspfNbrLsRetransQLen_Type()
)
rlOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrLsRetransQLen.setStatus("current")
_RlOspfNbmaNbrStatus_Type = RowStatus
_RlOspfNbmaNbrStatus_Object = MibTableColumn
rlOspfNbmaNbrStatus = _RlOspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 10),
    _RlOspfNbmaNbrStatus_Type()
)
rlOspfNbmaNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfNbmaNbrStatus.setStatus("current")


class _RlOspfNbmaNbrPermanence_Type(Integer32):
    """Custom type rlOspfNbmaNbrPermanence based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2))
    )


_RlOspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_RlOspfNbmaNbrPermanence_Object = MibTableColumn
rlOspfNbmaNbrPermanence = _RlOspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 11),
    _RlOspfNbmaNbrPermanence_Type()
)
rlOspfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbmaNbrPermanence.setStatus("current")
_RlOspfNbrHelloSuppressed_Type = TruthValue
_RlOspfNbrHelloSuppressed_Object = MibTableColumn
rlOspfNbrHelloSuppressed = _RlOspfNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 12),
    _RlOspfNbrHelloSuppressed_Type()
)
rlOspfNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrHelloSuppressed.setStatus("current")


class _RlOspfNbrRestartHelperStatus_Type(Integer32):
    """Custom type rlOspfNbrRestartHelperStatus based on Integer32"""
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


_RlOspfNbrRestartHelperStatus_Type.__name__ = "Integer32"
_RlOspfNbrRestartHelperStatus_Object = MibTableColumn
rlOspfNbrRestartHelperStatus = _RlOspfNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 13),
    _RlOspfNbrRestartHelperStatus_Type()
)
rlOspfNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrRestartHelperStatus.setStatus("current")
_RlOspfNbrRestartHelperAge_Type = Unsigned32
_RlOspfNbrRestartHelperAge_Object = MibTableColumn
rlOspfNbrRestartHelperAge = _RlOspfNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 14),
    _RlOspfNbrRestartHelperAge_Type()
)
rlOspfNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfNbrRestartHelperAge.setUnits("seconds")


class _RlOspfNbrRestartHelperExitReason_Type(Integer32):
    """Custom type rlOspfNbrRestartHelperExitReason based on Integer32"""
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


_RlOspfNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_RlOspfNbrRestartHelperExitReason_Object = MibTableColumn
rlOspfNbrRestartHelperExitReason = _RlOspfNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 15),
    _RlOspfNbrRestartHelperExitReason_Type()
)
rlOspfNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrRestartHelperExitReason.setStatus("current")
_RlOspfNbrDeadTime_Type = PositiveInteger
_RlOspfNbrDeadTime_Object = MibTableColumn
rlOspfNbrDeadTime = _RlOspfNbrDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 16),
    _RlOspfNbrDeadTime_Type()
)
rlOspfNbrDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrDeadTime.setStatus("current")
_RlOspfNbrAreaId_Type = AreaID
_RlOspfNbrAreaId_Object = MibTableColumn
rlOspfNbrAreaId = _RlOspfNbrAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 17),
    _RlOspfNbrAreaId_Type()
)
rlOspfNbrAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrAreaId.setStatus("current")
_RlOspfNbrIfIndex_Type = Integer32
_RlOspfNbrIfIndex_Object = MibTableColumn
rlOspfNbrIfIndex = _RlOspfNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 18),
    _RlOspfNbrIfIndex_Type()
)
rlOspfNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrIfIndex.setStatus("current")
_RlOspfNbrIfIpAddr_Type = IpAddress
_RlOspfNbrIfIpAddr_Object = MibTableColumn
rlOspfNbrIfIpAddr = _RlOspfNbrIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 11, 1, 19),
    _RlOspfNbrIfIpAddr_Type()
)
rlOspfNbrIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNbrIfIpAddr.setStatus("current")
_RlOspfVirtNbrTable_Object = MibTable
rlOspfVirtNbrTable = _RlOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12)
)
if mibBuilder.loadTexts:
    rlOspfVirtNbrTable.setStatus("current")
_RlOspfVirtNbrEntry_Object = MibTableRow
rlOspfVirtNbrEntry = _RlOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1)
)
rlOspfVirtNbrEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtNbrProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtNbrArea"),
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    rlOspfVirtNbrEntry.setStatus("current")
_RlOspfVirtNbrProcessId_Type = RlOspfProcessID
_RlOspfVirtNbrProcessId_Object = MibTableColumn
rlOspfVirtNbrProcessId = _RlOspfVirtNbrProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 1),
    _RlOspfVirtNbrProcessId_Type()
)
rlOspfVirtNbrProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrProcessId.setStatus("current")
_RlOspfVirtNbrArea_Type = AreaID
_RlOspfVirtNbrArea_Object = MibTableColumn
rlOspfVirtNbrArea = _RlOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 2),
    _RlOspfVirtNbrArea_Type()
)
rlOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrArea.setStatus("current")
_RlOspfVirtNbrRtrId_Type = RouterID
_RlOspfVirtNbrRtrId_Object = MibTableColumn
rlOspfVirtNbrRtrId = _RlOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 3),
    _RlOspfVirtNbrRtrId_Type()
)
rlOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrRtrId.setStatus("current")
_RlOspfVirtNbrIpAddr_Type = IpAddress
_RlOspfVirtNbrIpAddr_Object = MibTableColumn
rlOspfVirtNbrIpAddr = _RlOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 4),
    _RlOspfVirtNbrIpAddr_Type()
)
rlOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrIpAddr.setStatus("current")
_RlOspfVirtNbrOptions_Type = Integer32
_RlOspfVirtNbrOptions_Object = MibTableColumn
rlOspfVirtNbrOptions = _RlOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 5),
    _RlOspfVirtNbrOptions_Type()
)
rlOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrOptions.setStatus("current")


class _RlOspfVirtNbrState_Type(Integer32):
    """Custom type rlOspfVirtNbrState based on Integer32"""
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


_RlOspfVirtNbrState_Type.__name__ = "Integer32"
_RlOspfVirtNbrState_Object = MibTableColumn
rlOspfVirtNbrState = _RlOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 6),
    _RlOspfVirtNbrState_Type()
)
rlOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrState.setStatus("current")
_RlOspfVirtNbrEvents_Type = Counter32
_RlOspfVirtNbrEvents_Object = MibTableColumn
rlOspfVirtNbrEvents = _RlOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 7),
    _RlOspfVirtNbrEvents_Type()
)
rlOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrEvents.setStatus("current")
_RlOspfVirtNbrLsRetransQLen_Type = Gauge32
_RlOspfVirtNbrLsRetransQLen_Object = MibTableColumn
rlOspfVirtNbrLsRetransQLen = _RlOspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 8),
    _RlOspfVirtNbrLsRetransQLen_Type()
)
rlOspfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrLsRetransQLen.setStatus("current")
_RlOspfVirtNbrHelloSuppressed_Type = TruthValue
_RlOspfVirtNbrHelloSuppressed_Object = MibTableColumn
rlOspfVirtNbrHelloSuppressed = _RlOspfVirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 9),
    _RlOspfVirtNbrHelloSuppressed_Type()
)
rlOspfVirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrHelloSuppressed.setStatus("current")


class _RlOspfVirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type rlOspfVirtNbrRestartHelperStatus based on Integer32"""
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


_RlOspfVirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_RlOspfVirtNbrRestartHelperStatus_Object = MibTableColumn
rlOspfVirtNbrRestartHelperStatus = _RlOspfVirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 10),
    _RlOspfVirtNbrRestartHelperStatus_Type()
)
rlOspfVirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrRestartHelperStatus.setStatus("current")
_RlOspfVirtNbrRestartHelperAge_Type = Unsigned32
_RlOspfVirtNbrRestartHelperAge_Object = MibTableColumn
rlOspfVirtNbrRestartHelperAge = _RlOspfVirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 11),
    _RlOspfVirtNbrRestartHelperAge_Type()
)
rlOspfVirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfVirtNbrRestartHelperAge.setUnits("seconds")


class _RlOspfVirtNbrRestartHelperExitReason_Type(Integer32):
    """Custom type rlOspfVirtNbrRestartHelperExitReason based on Integer32"""
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


_RlOspfVirtNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_RlOspfVirtNbrRestartHelperExitReason_Object = MibTableColumn
rlOspfVirtNbrRestartHelperExitReason = _RlOspfVirtNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 12),
    _RlOspfVirtNbrRestartHelperExitReason_Type()
)
rlOspfVirtNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrRestartHelperExitReason.setStatus("current")
_RlOspfVirtNbrDeadTime_Type = PositiveInteger
_RlOspfVirtNbrDeadTime_Object = MibTableColumn
rlOspfVirtNbrDeadTime = _RlOspfVirtNbrDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 12, 1, 13),
    _RlOspfVirtNbrDeadTime_Type()
)
rlOspfVirtNbrDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtNbrDeadTime.setStatus("current")
_RlOspfExtLsdbTable_Object = MibTable
rlOspfExtLsdbTable = _RlOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 13)
)
if mibBuilder.loadTexts:
    rlOspfExtLsdbTable.setStatus("deprecated")
_RlOspfExtLsdbEntry_Object = MibTableRow
rlOspfExtLsdbEntry = _RlOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 13, 1)
)
rlOspfExtLsdbEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfExtLsdbProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfExtLsdbType"),
    (0, "RADLAN-OSPF-MIB", "rlOspfExtLsdbLsid"),
    (0, "RADLAN-OSPF-MIB", "rlOspfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfExtLsdbEntry.setStatus("deprecated")
_RlOspfExtLsdbProcessId_Type = RlOspfProcessID
_RlOspfExtLsdbProcessId_Object = MibTableColumn
rlOspfExtLsdbProcessId = _RlOspfExtLsdbProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 13, 1, 1),
    _RlOspfExtLsdbProcessId_Type()
)
rlOspfExtLsdbProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExtLsdbProcessId.setStatus("current")


class _RlOspfExtLsdbType_Type(Integer32):
    """Custom type rlOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_RlOspfExtLsdbType_Type.__name__ = "Integer32"
_RlOspfExtLsdbType_Object = MibTableColumn
rlOspfExtLsdbType = _RlOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 13, 1, 2),
    _RlOspfExtLsdbType_Type()
)
rlOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExtLsdbType.setStatus("deprecated")
_RlOspfExtLsdbLsid_Type = IpAddress
_RlOspfExtLsdbLsid_Object = MibTableColumn
rlOspfExtLsdbLsid = _RlOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 13, 1, 3),
    _RlOspfExtLsdbLsid_Type()
)
rlOspfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExtLsdbLsid.setStatus("deprecated")
_RlOspfExtLsdbRouterId_Type = RouterID
_RlOspfExtLsdbRouterId_Object = MibTableColumn
rlOspfExtLsdbRouterId = _RlOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 13, 1, 4),
    _RlOspfExtLsdbRouterId_Type()
)
rlOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExtLsdbRouterId.setStatus("deprecated")
_RlOspfExtLsdbSequence_Type = Integer32
_RlOspfExtLsdbSequence_Object = MibTableColumn
rlOspfExtLsdbSequence = _RlOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 13, 1, 5),
    _RlOspfExtLsdbSequence_Type()
)
rlOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExtLsdbSequence.setStatus("deprecated")
_RlOspfExtLsdbAge_Type = Integer32
_RlOspfExtLsdbAge_Object = MibTableColumn
rlOspfExtLsdbAge = _RlOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 13, 1, 6),
    _RlOspfExtLsdbAge_Type()
)
rlOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExtLsdbAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    rlOspfExtLsdbAge.setUnits("seconds")
_RlOspfExtLsdbChecksum_Type = Integer32
_RlOspfExtLsdbChecksum_Object = MibTableColumn
rlOspfExtLsdbChecksum = _RlOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 13, 1, 7),
    _RlOspfExtLsdbChecksum_Type()
)
rlOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExtLsdbChecksum.setStatus("deprecated")


class _RlOspfExtLsdbAdvertisement_Type(OctetString):
    """Custom type rlOspfExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )


_RlOspfExtLsdbAdvertisement_Type.__name__ = "OctetString"
_RlOspfExtLsdbAdvertisement_Object = MibTableColumn
rlOspfExtLsdbAdvertisement = _RlOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 13, 1, 8),
    _RlOspfExtLsdbAdvertisement_Type()
)
rlOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfExtLsdbAdvertisement.setStatus("deprecated")
_RlOspfAreaAggregateTable_Object = MibTable
rlOspfAreaAggregateTable = _RlOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 14)
)
if mibBuilder.loadTexts:
    rlOspfAreaAggregateTable.setStatus("current")
_RlOspfAreaAggregateEntry_Object = MibTableRow
rlOspfAreaAggregateEntry = _RlOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 14, 1)
)
rlOspfAreaAggregateEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfAreaAggregateProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfAreaAggregateAreaID"),
    (0, "RADLAN-OSPF-MIB", "rlOspfAreaAggregateLsdbType"),
    (0, "RADLAN-OSPF-MIB", "rlOspfAreaAggregateNet"),
    (0, "RADLAN-OSPF-MIB", "rlOspfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    rlOspfAreaAggregateEntry.setStatus("current")
_RlOspfAreaAggregateProcessId_Type = RlOspfProcessID
_RlOspfAreaAggregateProcessId_Object = MibTableColumn
rlOspfAreaAggregateProcessId = _RlOspfAreaAggregateProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 14, 1, 1),
    _RlOspfAreaAggregateProcessId_Type()
)
rlOspfAreaAggregateProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaAggregateProcessId.setStatus("current")
_RlOspfAreaAggregateAreaID_Type = AreaID
_RlOspfAreaAggregateAreaID_Object = MibTableColumn
rlOspfAreaAggregateAreaID = _RlOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 14, 1, 2),
    _RlOspfAreaAggregateAreaID_Type()
)
rlOspfAreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaAggregateAreaID.setStatus("current")


class _RlOspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type rlOspfAreaAggregateLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("nssaExternalLink", 7),
          ("summaryLink", 3))
    )


_RlOspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_RlOspfAreaAggregateLsdbType_Object = MibTableColumn
rlOspfAreaAggregateLsdbType = _RlOspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 14, 1, 3),
    _RlOspfAreaAggregateLsdbType_Type()
)
rlOspfAreaAggregateLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaAggregateLsdbType.setStatus("current")
_RlOspfAreaAggregateNet_Type = IpAddress
_RlOspfAreaAggregateNet_Object = MibTableColumn
rlOspfAreaAggregateNet = _RlOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 14, 1, 4),
    _RlOspfAreaAggregateNet_Type()
)
rlOspfAreaAggregateNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaAggregateNet.setStatus("current")
_RlOspfAreaAggregateMask_Type = IpAddress
_RlOspfAreaAggregateMask_Object = MibTableColumn
rlOspfAreaAggregateMask = _RlOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 14, 1, 5),
    _RlOspfAreaAggregateMask_Type()
)
rlOspfAreaAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAreaAggregateMask.setStatus("current")
_RlOspfAreaAggregateStatus_Type = RowStatus
_RlOspfAreaAggregateStatus_Object = MibTableColumn
rlOspfAreaAggregateStatus = _RlOspfAreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 14, 1, 6),
    _RlOspfAreaAggregateStatus_Type()
)
rlOspfAreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaAggregateStatus.setStatus("current")


class _RlOspfAreaAggregateEffect_Type(Integer32):
    """Custom type rlOspfAreaAggregateEffect based on Integer32"""
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


_RlOspfAreaAggregateEffect_Type.__name__ = "Integer32"
_RlOspfAreaAggregateEffect_Object = MibTableColumn
rlOspfAreaAggregateEffect = _RlOspfAreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 14, 1, 7),
    _RlOspfAreaAggregateEffect_Type()
)
rlOspfAreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaAggregateEffect.setStatus("current")


class _RlOspfAreaAggregateExtRouteTag_Type(Unsigned32):
    """Custom type rlOspfAreaAggregateExtRouteTag based on Unsigned32"""
    defaultValue = 0


_RlOspfAreaAggregateExtRouteTag_Object = MibTableColumn
rlOspfAreaAggregateExtRouteTag = _RlOspfAreaAggregateExtRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 14, 1, 8),
    _RlOspfAreaAggregateExtRouteTag_Type()
)
rlOspfAreaAggregateExtRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOspfAreaAggregateExtRouteTag.setStatus("current")
_RlOspfLocalLsdbTable_Object = MibTable
rlOspfLocalLsdbTable = _RlOspfLocalLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18)
)
if mibBuilder.loadTexts:
    rlOspfLocalLsdbTable.setStatus("current")
_RlOspfLocalLsdbEntry_Object = MibTableRow
rlOspfLocalLsdbEntry = _RlOspfLocalLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1)
)
rlOspfLocalLsdbEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfLocalLsdbProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfLocalLsdbIpAddress"),
    (0, "RADLAN-OSPF-MIB", "rlOspfLocalLsdbAddressLessIf"),
    (0, "RADLAN-OSPF-MIB", "rlOspfLocalLsdbType"),
    (0, "RADLAN-OSPF-MIB", "rlOspfLocalLsdbLsid"),
    (0, "RADLAN-OSPF-MIB", "rlOspfLocalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfLocalLsdbEntry.setStatus("current")
_RlOspfLocalLsdbProcessId_Type = Unsigned32
_RlOspfLocalLsdbProcessId_Object = MibTableColumn
rlOspfLocalLsdbProcessId = _RlOspfLocalLsdbProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1, 1),
    _RlOspfLocalLsdbProcessId_Type()
)
rlOspfLocalLsdbProcessId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbProcessId.setStatus("current")
_RlOspfLocalLsdbIpAddress_Type = IpAddress
_RlOspfLocalLsdbIpAddress_Object = MibTableColumn
rlOspfLocalLsdbIpAddress = _RlOspfLocalLsdbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1, 2),
    _RlOspfLocalLsdbIpAddress_Type()
)
rlOspfLocalLsdbIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbIpAddress.setStatus("current")
_RlOspfLocalLsdbAddressLessIf_Type = InterfaceIndexOrZero
_RlOspfLocalLsdbAddressLessIf_Object = MibTableColumn
rlOspfLocalLsdbAddressLessIf = _RlOspfLocalLsdbAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1, 3),
    _RlOspfLocalLsdbAddressLessIf_Type()
)
rlOspfLocalLsdbAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbAddressLessIf.setStatus("current")


class _RlOspfLocalLsdbType_Type(Integer32):
    """Custom type rlOspfLocalLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            9
        )
    )
    namedValues = NamedValues(
        ("localOpaqueLink", 9)
    )


_RlOspfLocalLsdbType_Type.__name__ = "Integer32"
_RlOspfLocalLsdbType_Object = MibTableColumn
rlOspfLocalLsdbType = _RlOspfLocalLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1, 4),
    _RlOspfLocalLsdbType_Type()
)
rlOspfLocalLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbType.setStatus("current")
_RlOspfLocalLsdbLsid_Type = IpAddress
_RlOspfLocalLsdbLsid_Object = MibTableColumn
rlOspfLocalLsdbLsid = _RlOspfLocalLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1, 5),
    _RlOspfLocalLsdbLsid_Type()
)
rlOspfLocalLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbLsid.setStatus("current")
_RlOspfLocalLsdbRouterId_Type = RouterID
_RlOspfLocalLsdbRouterId_Object = MibTableColumn
rlOspfLocalLsdbRouterId = _RlOspfLocalLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1, 6),
    _RlOspfLocalLsdbRouterId_Type()
)
rlOspfLocalLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbRouterId.setStatus("current")
_RlOspfLocalLsdbSequence_Type = Integer32
_RlOspfLocalLsdbSequence_Object = MibTableColumn
rlOspfLocalLsdbSequence = _RlOspfLocalLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1, 7),
    _RlOspfLocalLsdbSequence_Type()
)
rlOspfLocalLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbSequence.setStatus("current")
_RlOspfLocalLsdbAge_Type = Integer32
_RlOspfLocalLsdbAge_Object = MibTableColumn
rlOspfLocalLsdbAge = _RlOspfLocalLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1, 8),
    _RlOspfLocalLsdbAge_Type()
)
rlOspfLocalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbAge.setUnits("seconds")
_RlOspfLocalLsdbChecksum_Type = Integer32
_RlOspfLocalLsdbChecksum_Object = MibTableColumn
rlOspfLocalLsdbChecksum = _RlOspfLocalLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1, 9),
    _RlOspfLocalLsdbChecksum_Type()
)
rlOspfLocalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbChecksum.setStatus("current")


class _RlOspfLocalLsdbAdvertisement_Type(OctetString):
    """Custom type rlOspfLocalLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_RlOspfLocalLsdbAdvertisement_Type.__name__ = "OctetString"
_RlOspfLocalLsdbAdvertisement_Object = MibTableColumn
rlOspfLocalLsdbAdvertisement = _RlOspfLocalLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1, 10),
    _RlOspfLocalLsdbAdvertisement_Type()
)
rlOspfLocalLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbAdvertisement.setStatus("current")
_RlOspfLocalLsdbAreaId_Type = AreaID
_RlOspfLocalLsdbAreaId_Object = MibTableColumn
rlOspfLocalLsdbAreaId = _RlOspfLocalLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 18, 1, 11),
    _RlOspfLocalLsdbAreaId_Type()
)
rlOspfLocalLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfLocalLsdbAreaId.setStatus("current")
_RlOspfVirtLocalLsdbTable_Object = MibTable
rlOspfVirtLocalLsdbTable = _RlOspfVirtLocalLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19)
)
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbTable.setStatus("current")
_RlOspfVirtLocalLsdbEntry_Object = MibTableRow
rlOspfVirtLocalLsdbEntry = _RlOspfVirtLocalLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19, 1)
)
rlOspfVirtLocalLsdbEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtLocalLsdbProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtLocalLsdbTransitArea"),
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtLocalLsdbNeighbor"),
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtLocalLsdbType"),
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtLocalLsdbLsid"),
    (0, "RADLAN-OSPF-MIB", "rlOspfVirtLocalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbEntry.setStatus("current")
_RlOspfVirtLocalLsdbProcessId_Type = Unsigned32
_RlOspfVirtLocalLsdbProcessId_Object = MibTableColumn
rlOspfVirtLocalLsdbProcessId = _RlOspfVirtLocalLsdbProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19, 1, 1),
    _RlOspfVirtLocalLsdbProcessId_Type()
)
rlOspfVirtLocalLsdbProcessId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbProcessId.setStatus("current")
_RlOspfVirtLocalLsdbTransitArea_Type = AreaID
_RlOspfVirtLocalLsdbTransitArea_Object = MibTableColumn
rlOspfVirtLocalLsdbTransitArea = _RlOspfVirtLocalLsdbTransitArea_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19, 1, 2),
    _RlOspfVirtLocalLsdbTransitArea_Type()
)
rlOspfVirtLocalLsdbTransitArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbTransitArea.setStatus("current")
_RlOspfVirtLocalLsdbNeighbor_Type = RouterID
_RlOspfVirtLocalLsdbNeighbor_Object = MibTableColumn
rlOspfVirtLocalLsdbNeighbor = _RlOspfVirtLocalLsdbNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19, 1, 3),
    _RlOspfVirtLocalLsdbNeighbor_Type()
)
rlOspfVirtLocalLsdbNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbNeighbor.setStatus("current")


class _RlOspfVirtLocalLsdbType_Type(Integer32):
    """Custom type rlOspfVirtLocalLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            9
        )
    )
    namedValues = NamedValues(
        ("localOpaqueLink", 9)
    )


_RlOspfVirtLocalLsdbType_Type.__name__ = "Integer32"
_RlOspfVirtLocalLsdbType_Object = MibTableColumn
rlOspfVirtLocalLsdbType = _RlOspfVirtLocalLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19, 1, 4),
    _RlOspfVirtLocalLsdbType_Type()
)
rlOspfVirtLocalLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbType.setStatus("current")
_RlOspfVirtLocalLsdbLsid_Type = IpAddress
_RlOspfVirtLocalLsdbLsid_Object = MibTableColumn
rlOspfVirtLocalLsdbLsid = _RlOspfVirtLocalLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19, 1, 5),
    _RlOspfVirtLocalLsdbLsid_Type()
)
rlOspfVirtLocalLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbLsid.setStatus("current")
_RlOspfVirtLocalLsdbRouterId_Type = RouterID
_RlOspfVirtLocalLsdbRouterId_Object = MibTableColumn
rlOspfVirtLocalLsdbRouterId = _RlOspfVirtLocalLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19, 1, 6),
    _RlOspfVirtLocalLsdbRouterId_Type()
)
rlOspfVirtLocalLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbRouterId.setStatus("current")
_RlOspfVirtLocalLsdbSequence_Type = Integer32
_RlOspfVirtLocalLsdbSequence_Object = MibTableColumn
rlOspfVirtLocalLsdbSequence = _RlOspfVirtLocalLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19, 1, 7),
    _RlOspfVirtLocalLsdbSequence_Type()
)
rlOspfVirtLocalLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbSequence.setStatus("current")
_RlOspfVirtLocalLsdbAge_Type = Integer32
_RlOspfVirtLocalLsdbAge_Object = MibTableColumn
rlOspfVirtLocalLsdbAge = _RlOspfVirtLocalLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19, 1, 8),
    _RlOspfVirtLocalLsdbAge_Type()
)
rlOspfVirtLocalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbAge.setUnits("seconds")
_RlOspfVirtLocalLsdbChecksum_Type = Integer32
_RlOspfVirtLocalLsdbChecksum_Object = MibTableColumn
rlOspfVirtLocalLsdbChecksum = _RlOspfVirtLocalLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19, 1, 9),
    _RlOspfVirtLocalLsdbChecksum_Type()
)
rlOspfVirtLocalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbChecksum.setStatus("current")


class _RlOspfVirtLocalLsdbAdvertisement_Type(OctetString):
    """Custom type rlOspfVirtLocalLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_RlOspfVirtLocalLsdbAdvertisement_Type.__name__ = "OctetString"
_RlOspfVirtLocalLsdbAdvertisement_Object = MibTableColumn
rlOspfVirtLocalLsdbAdvertisement = _RlOspfVirtLocalLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 19, 1, 10),
    _RlOspfVirtLocalLsdbAdvertisement_Type()
)
rlOspfVirtLocalLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfVirtLocalLsdbAdvertisement.setStatus("current")
_RlOspfEnableTrapsOspfErrors_Type = Integer32
_RlOspfEnableTrapsOspfErrors_Object = MibScalar
rlOspfEnableTrapsOspfErrors = _RlOspfEnableTrapsOspfErrors_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 20),
    _RlOspfEnableTrapsOspfErrors_Type()
)
rlOspfEnableTrapsOspfErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfEnableTrapsOspfErrors.setStatus("current")
_RlOspfEnableTrapsOspfLsa_Type = Integer32
_RlOspfEnableTrapsOspfLsa_Object = MibScalar
rlOspfEnableTrapsOspfLsa = _RlOspfEnableTrapsOspfLsa_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 21),
    _RlOspfEnableTrapsOspfLsa_Type()
)
rlOspfEnableTrapsOspfLsa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfEnableTrapsOspfLsa.setStatus("current")


class _RlOspfEnableTrapsOspfRateLimitSeconds_Type(Integer32):
    """Custom type rlOspfEnableTrapsOspfRateLimitSeconds based on Integer32"""
    defaultValue = 10


_RlOspfEnableTrapsOspfRateLimitSeconds_Object = MibScalar
rlOspfEnableTrapsOspfRateLimitSeconds = _RlOspfEnableTrapsOspfRateLimitSeconds_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 22),
    _RlOspfEnableTrapsOspfRateLimitSeconds_Type()
)
rlOspfEnableTrapsOspfRateLimitSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfEnableTrapsOspfRateLimitSeconds.setStatus("current")


class _RlOspfEnableTrapsOspfRateLimitTrapNumber_Type(Integer32):
    """Custom type rlOspfEnableTrapsOspfRateLimitTrapNumber based on Integer32"""
    defaultValue = 7


_RlOspfEnableTrapsOspfRateLimitTrapNumber_Object = MibScalar
rlOspfEnableTrapsOspfRateLimitTrapNumber = _RlOspfEnableTrapsOspfRateLimitTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 23),
    _RlOspfEnableTrapsOspfRateLimitTrapNumber_Type()
)
rlOspfEnableTrapsOspfRateLimitTrapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfEnableTrapsOspfRateLimitTrapNumber.setStatus("current")
_RlOspfEnableTrapsOspfTransmit_Type = Integer32
_RlOspfEnableTrapsOspfTransmit_Object = MibScalar
rlOspfEnableTrapsOspfTransmit = _RlOspfEnableTrapsOspfTransmit_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 24),
    _RlOspfEnableTrapsOspfTransmit_Type()
)
rlOspfEnableTrapsOspfTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfEnableTrapsOspfTransmit.setStatus("current")
_RlOspfEnableTrapsOspfStateChange_Type = Integer32
_RlOspfEnableTrapsOspfStateChange_Object = MibScalar
rlOspfEnableTrapsOspfStateChange = _RlOspfEnableTrapsOspfStateChange_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 25),
    _RlOspfEnableTrapsOspfStateChange_Type()
)
rlOspfEnableTrapsOspfStateChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfEnableTrapsOspfStateChange.setStatus("current")
_RlOspfExt_ObjectIdentity = ObjectIdentity
rlOspfExt = _RlOspfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 210, 26)
)
_RlOspfBrRouterTable_Object = MibTable
rlOspfBrRouterTable = _RlOspfBrRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 26, 1)
)
if mibBuilder.loadTexts:
    rlOspfBrRouterTable.setStatus("current")
_RlOspfBrRouterEntry_Object = MibTableRow
rlOspfBrRouterEntry = _RlOspfBrRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 26, 1, 1)
)
rlOspfBrRouterEntry.setIndexNames(
    (0, "RADLAN-OSPF-MIB", "rlOspfBrRouterProcessId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfBrRouterAreaId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfBrRouterRouterId"),
    (0, "RADLAN-OSPF-MIB", "rlOspfBrRouterNextHopIp"),
    (0, "RADLAN-OSPF-MIB", "rlOspfBrRouterOutIf"),
)
if mibBuilder.loadTexts:
    rlOspfBrRouterEntry.setStatus("current")
_RlOspfBrRouterProcessId_Type = RlOspfProcessID
_RlOspfBrRouterProcessId_Object = MibTableColumn
rlOspfBrRouterProcessId = _RlOspfBrRouterProcessId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 26, 1, 1, 1),
    _RlOspfBrRouterProcessId_Type()
)
rlOspfBrRouterProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfBrRouterProcessId.setStatus("current")
_RlOspfBrRouterAreaId_Type = AreaID
_RlOspfBrRouterAreaId_Object = MibTableColumn
rlOspfBrRouterAreaId = _RlOspfBrRouterAreaId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 26, 1, 1, 2),
    _RlOspfBrRouterAreaId_Type()
)
rlOspfBrRouterAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfBrRouterAreaId.setStatus("current")
_RlOspfBrRouterRouterId_Type = RouterID
_RlOspfBrRouterRouterId_Object = MibTableColumn
rlOspfBrRouterRouterId = _RlOspfBrRouterRouterId_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 26, 1, 1, 3),
    _RlOspfBrRouterRouterId_Type()
)
rlOspfBrRouterRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfBrRouterRouterId.setStatus("current")
_RlOspfBrRouterNextHopIp_Type = IpAddress
_RlOspfBrRouterNextHopIp_Object = MibTableColumn
rlOspfBrRouterNextHopIp = _RlOspfBrRouterNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 26, 1, 1, 4),
    _RlOspfBrRouterNextHopIp_Type()
)
rlOspfBrRouterNextHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfBrRouterNextHopIp.setStatus("current")
_RlOspfBrRouterOutIf_Type = InterfaceIndexOrZero
_RlOspfBrRouterOutIf_Object = MibTableColumn
rlOspfBrRouterOutIf = _RlOspfBrRouterOutIf_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 26, 1, 1, 5),
    _RlOspfBrRouterOutIf_Type()
)
rlOspfBrRouterOutIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfBrRouterOutIf.setStatus("current")


class _RlOspfBrRouterRouteType_Type(Integer32):
    """Custom type rlOspfBrRouterRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inter", 2),
          ("intra", 1))
    )


_RlOspfBrRouterRouteType_Type.__name__ = "Integer32"
_RlOspfBrRouterRouteType_Object = MibTableColumn
rlOspfBrRouterRouteType = _RlOspfBrRouterRouteType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 26, 1, 1, 6),
    _RlOspfBrRouterRouteType_Type()
)
rlOspfBrRouterRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfBrRouterRouteType.setStatus("current")
_RlOspfBrRouterRouteCost_Type = Unsigned32
_RlOspfBrRouterRouteCost_Object = MibTableColumn
rlOspfBrRouterRouteCost = _RlOspfBrRouterRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 26, 1, 1, 7),
    _RlOspfBrRouterRouteCost_Type()
)
rlOspfBrRouterRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfBrRouterRouteCost.setStatus("current")


class _RlOspfBrRouterRouterType_Type(Integer32):
    """Custom type rlOspfBrRouterRouterType based on Integer32"""
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
          ("asbr", 2),
          ("both", 3))
    )


_RlOspfBrRouterRouterType_Type.__name__ = "Integer32"
_RlOspfBrRouterRouterType_Object = MibTableColumn
rlOspfBrRouterRouterType = _RlOspfBrRouterRouterType_Object(
    (1, 3, 6, 1, 4, 1, 89, 210, 26, 1, 1, 8),
    _RlOspfBrRouterRouterType_Type()
)
rlOspfBrRouterRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfBrRouterRouterType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-OSPF-MIB",
    **{"RlOspfProcessID": RlOspfProcessID,
       "RlOspfFastHelloMultiplierRange": RlOspfFastHelloMultiplierRange,
       "RlOspfRestartHelperStatus": RlOspfRestartHelperStatus,
       "RlOspfRestartExitReason": RlOspfRestartExitReason,
       "RlOspfRouterIdType": RlOspfRouterIdType,
       "RlOspfAuthenticationType": RlOspfAuthenticationType,
       "RlOspfUpToRefreshIntervalTC": RlOspfUpToRefreshIntervalTC,
       "RlOspfDeadIntervalRangeTC": RlOspfDeadIntervalRangeTC,
       "rlOspf": rlOspf,
       "rlOspfInstance": rlOspfInstance,
       "rlOspfGeneralGroupTable": rlOspfGeneralGroupTable,
       "rlOspfGeneralGroupEntry": rlOspfGeneralGroupEntry,
       "rlOspfProcessId": rlOspfProcessId,
       "rlOspfRouterId": rlOspfRouterId,
       "rlOspfAdminStat": rlOspfAdminStat,
       "rlOspfVersionNumber": rlOspfVersionNumber,
       "rlOspfAreaBdrRtrStatus": rlOspfAreaBdrRtrStatus,
       "rlOspfASBdrRtrStatus": rlOspfASBdrRtrStatus,
       "rlOspfExternLsaCount": rlOspfExternLsaCount,
       "rlOspfExternLsaCksumSum": rlOspfExternLsaCksumSum,
       "rlOspfTOSSupport": rlOspfTOSSupport,
       "rlOspfOriginateNewLsas": rlOspfOriginateNewLsas,
       "rlOspfRxNewLsas": rlOspfRxNewLsas,
       "rlOspfExtLsdbLimit": rlOspfExtLsdbLimit,
       "rlOspfMulticastExtensions": rlOspfMulticastExtensions,
       "rlOspfExitOverflowInterval": rlOspfExitOverflowInterval,
       "rlOspfDemandExtensions": rlOspfDemandExtensions,
       "rlOspfRFC1583Compatibility": rlOspfRFC1583Compatibility,
       "rlOspfOpaqueLsaSupport": rlOspfOpaqueLsaSupport,
       "rlOspfReferenceBandwidth": rlOspfReferenceBandwidth,
       "rlOspfRestartSupport": rlOspfRestartSupport,
       "rlOspfRestartInterval": rlOspfRestartInterval,
       "rlOspfRestartStrictLsaChecking": rlOspfRestartStrictLsaChecking,
       "rlOspfRestartStatus": rlOspfRestartStatus,
       "rlOspfRestartAge": rlOspfRestartAge,
       "rlOspfRestartExitReason": rlOspfRestartExitReason,
       "rlOspfAsLsaCount": rlOspfAsLsaCount,
       "rlOspfAsLsaCksumSum": rlOspfAsLsaCksumSum,
       "rlOspfStubRouterSupport": rlOspfStubRouterSupport,
       "rlOspfStubRouterAdvertisement": rlOspfStubRouterAdvertisement,
       "rlOspfDiscontinuityTime": rlOspfDiscontinuityTime,
       "rlOspfGeneralGroupStatus": rlOspfGeneralGroupStatus,
       "rlOspfLogAdjacencyChanges": rlOspfLogAdjacencyChanges,
       "rlOspfPassiveInterface": rlOspfPassiveInterface,
       "rlOspfDefaultMetric": rlOspfDefaultMetric,
       "rlOspfMaximumRedistPrefixNum": rlOspfMaximumRedistPrefixNum,
       "rlOspfMaximumRedistPrefixThreshold": rlOspfMaximumRedistPrefixThreshold,
       "rlOspfMaximumRedistPrefixWarningOnly": rlOspfMaximumRedistPrefixWarningOnly,
       "rlOspfOperStatus": rlOspfOperStatus,
       "rlOspfNextRouterId": rlOspfNextRouterId,
       "rlOspfRouterIdType": rlOspfRouterIdType,
       "rlOspfNextRouterIdType": rlOspfNextRouterIdType,
       "rlOspfASBdrRtrActualStatus": rlOspfASBdrRtrActualStatus,
       "rlOspfCalcMaxDelay": rlOspfCalcMaxDelay,
       "rlOspfRteMaxEqCostPaths": rlOspfRteMaxEqCostPaths,
       "rlOspfAreaTable": rlOspfAreaTable,
       "rlOspfAreaEntry": rlOspfAreaEntry,
       "rlOspfAreaProcessId": rlOspfAreaProcessId,
       "rlOspfAreaId": rlOspfAreaId,
       "rlOspfAuthType": rlOspfAuthType,
       "rlOspfImportAsExtern": rlOspfImportAsExtern,
       "rlOspfSpfRuns": rlOspfSpfRuns,
       "rlOspfAreaBdrRtrCount": rlOspfAreaBdrRtrCount,
       "rlOspfAsBdrRtrCount": rlOspfAsBdrRtrCount,
       "rlOspfAreaLsaCount": rlOspfAreaLsaCount,
       "rlOspfAreaLsaCksumSum": rlOspfAreaLsaCksumSum,
       "rlOspfAreaSummary": rlOspfAreaSummary,
       "rlOspfAreaStatus": rlOspfAreaStatus,
       "rlOspfAreaNssaTranslatorRole": rlOspfAreaNssaTranslatorRole,
       "rlOspfAreaNssaTranslatorState": rlOspfAreaNssaTranslatorState,
       "rlOspfAreaNssaTranslatorStabilityInterval": rlOspfAreaNssaTranslatorStabilityInterval,
       "rlOspfAreaNssaTranslatorEvents": rlOspfAreaNssaTranslatorEvents,
       "rlOspfAreaAdminStat": rlOspfAreaAdminStat,
       "rlOspfAreaOperStatus": rlOspfAreaOperStatus,
       "rlOspfAreaFilterPrefixListIn": rlOspfAreaFilterPrefixListIn,
       "rlOspfAreaFilterPrefixListOut": rlOspfAreaFilterPrefixListOut,
       "rlOspfStubAreaTable": rlOspfStubAreaTable,
       "rlOspfStubAreaEntry": rlOspfStubAreaEntry,
       "rlOspfStubProcessId": rlOspfStubProcessId,
       "rlOspfStubAreaId": rlOspfStubAreaId,
       "rlOspfStubTOS": rlOspfStubTOS,
       "rlOspfStubMetric": rlOspfStubMetric,
       "rlOspfStubStatus": rlOspfStubStatus,
       "rlOspfStubMetricType": rlOspfStubMetricType,
       "rlOspfLsdbTable": rlOspfLsdbTable,
       "rlOspfLsdbEntry": rlOspfLsdbEntry,
       "rlOspfLsdbProcessId": rlOspfLsdbProcessId,
       "rlOspfLsdbAreaId": rlOspfLsdbAreaId,
       "rlOspfLsdbType": rlOspfLsdbType,
       "rlOspfLsdbLsid": rlOspfLsdbLsid,
       "rlOspfLsdbRouterId": rlOspfLsdbRouterId,
       "rlOspfLsdbSequence": rlOspfLsdbSequence,
       "rlOspfLsdbAge": rlOspfLsdbAge,
       "rlOspfLsdbChecksum": rlOspfLsdbChecksum,
       "rlOspfLsdbAdvertisement": rlOspfLsdbAdvertisement,
       "rlOspfAreaRangeTable": rlOspfAreaRangeTable,
       "rlOspfAreaRangeEntry": rlOspfAreaRangeEntry,
       "rlOspfAreaRangeProcessId": rlOspfAreaRangeProcessId,
       "rlOspfAreaRangeAreaId": rlOspfAreaRangeAreaId,
       "rlOspfAreaRangeNet": rlOspfAreaRangeNet,
       "rlOspfAreaRangeMask": rlOspfAreaRangeMask,
       "rlOspfAreaRangeStatus": rlOspfAreaRangeStatus,
       "rlOspfAreaRangeEffect": rlOspfAreaRangeEffect,
       "rlOspfHostTable": rlOspfHostTable,
       "rlOspfHostEntry": rlOspfHostEntry,
       "rlOspfHostProcessId": rlOspfHostProcessId,
       "rlOspfHostIpAddress": rlOspfHostIpAddress,
       "rlOspfHostTOS": rlOspfHostTOS,
       "rlOspfHostMetric": rlOspfHostMetric,
       "rlOspfHostStatus": rlOspfHostStatus,
       "rlOspfHostAreaID": rlOspfHostAreaID,
       "rlOspfHostCfgAreaID": rlOspfHostCfgAreaID,
       "rlOspfIfTable": rlOspfIfTable,
       "rlOspfIfEntry": rlOspfIfEntry,
       "rlOspfIfProcessId": rlOspfIfProcessId,
       "rlOspfIfIpAddress": rlOspfIfIpAddress,
       "rlOspfAddressLessIf": rlOspfAddressLessIf,
       "rlOspfIfAreaId": rlOspfIfAreaId,
       "rlOspfIfType": rlOspfIfType,
       "rlOspfIfAdminStat": rlOspfIfAdminStat,
       "rlOspfIfRtrPriority": rlOspfIfRtrPriority,
       "rlOspfIfTransitDelay": rlOspfIfTransitDelay,
       "rlOspfIfRetransInterval": rlOspfIfRetransInterval,
       "rlOspfIfHelloInterval": rlOspfIfHelloInterval,
       "rlOspfIfRtrDeadInterval": rlOspfIfRtrDeadInterval,
       "rlOspfIfPollInterval": rlOspfIfPollInterval,
       "rlOspfIfState": rlOspfIfState,
       "rlOspfIfDesignatedRouter": rlOspfIfDesignatedRouter,
       "rlOspfIfBackupDesignatedRouter": rlOspfIfBackupDesignatedRouter,
       "rlOspfIfEvents": rlOspfIfEvents,
       "rlOspfIfAuthKey": rlOspfIfAuthKey,
       "rlOspfIfStatus": rlOspfIfStatus,
       "rlOspfIfMulticastForwarding": rlOspfIfMulticastForwarding,
       "rlOspfIfDemand": rlOspfIfDemand,
       "rlOspfIfAuthType": rlOspfIfAuthType,
       "rlOspfIfLsaCount": rlOspfIfLsaCount,
       "rlOspfIfLsaCksumSum": rlOspfIfLsaCksumSum,
       "rlOspfIfDesignatedRouterId": rlOspfIfDesignatedRouterId,
       "rlOspfIfBackupDesignatedRouterId": rlOspfIfBackupDesignatedRouterId,
       "rlOspfIfOperStatus": rlOspfIfOperStatus,
       "rlOspfIfAuthKeyChain": rlOspfIfAuthKeyChain,
       "rlOspfIfPassive": rlOspfIfPassive,
       "rlOspfIfLsaRefreshIntvl": rlOspfIfLsaRefreshIntvl,
       "rlOspfIfFastHelloMultiplier": rlOspfIfFastHelloMultiplier,
       "rlOspfIfMtuIgnore": rlOspfIfMtuIgnore,
       "rlOspfIfNameLookup": rlOspfIfNameLookup,
       "rlOspfIfIfIndex": rlOspfIfIfIndex,
       "rlOspfIfActualAuthType": rlOspfIfActualAuthType,
       "rlOspfIfMetricTable": rlOspfIfMetricTable,
       "rlOspfIfMetricEntry": rlOspfIfMetricEntry,
       "rlOspfIfMetricProcessId": rlOspfIfMetricProcessId,
       "rlOspfIfMetricIpAddress": rlOspfIfMetricIpAddress,
       "rlOspfIfMetricAddressLessIf": rlOspfIfMetricAddressLessIf,
       "rlOspfIfMetricTOS": rlOspfIfMetricTOS,
       "rlOspfIfMetricValue": rlOspfIfMetricValue,
       "rlOspfIfMetricStatus": rlOspfIfMetricStatus,
       "rlOspfVirtIfTable": rlOspfVirtIfTable,
       "rlOspfVirtIfEntry": rlOspfVirtIfEntry,
       "rlOspfVirtIfProcessId": rlOspfVirtIfProcessId,
       "rlOspfVirtIfAreaId": rlOspfVirtIfAreaId,
       "rlOspfVirtIfNeighbor": rlOspfVirtIfNeighbor,
       "rlOspfVirtIfTransitDelay": rlOspfVirtIfTransitDelay,
       "rlOspfVirtIfRetransInterval": rlOspfVirtIfRetransInterval,
       "rlOspfVirtIfHelloInterval": rlOspfVirtIfHelloInterval,
       "rlOspfVirtIfRtrDeadInterval": rlOspfVirtIfRtrDeadInterval,
       "rlOspfVirtIfState": rlOspfVirtIfState,
       "rlOspfVirtIfEvents": rlOspfVirtIfEvents,
       "rlOspfVirtIfAuthKey": rlOspfVirtIfAuthKey,
       "rlOspfVirtIfStatus": rlOspfVirtIfStatus,
       "rlOspfVirtIfAuthType": rlOspfVirtIfAuthType,
       "rlOspfVirtIfLsaCount": rlOspfVirtIfLsaCount,
       "rlOspfVirtIfLsaCksumSum": rlOspfVirtIfLsaCksumSum,
       "rlOspfVirtIfAuthKeyChain": rlOspfVirtIfAuthKeyChain,
       "rlOspfVirtIfAdminStatus": rlOspfVirtIfAdminStatus,
       "rlOspfVirtIfOperStatus": rlOspfVirtIfOperStatus,
       "rlOspfVirtIfIndex": rlOspfVirtIfIndex,
       "rlOspfVirtIfActualAuthType": rlOspfVirtIfActualAuthType,
       "rlOspfNbrTable": rlOspfNbrTable,
       "rlOspfNbrEntry": rlOspfNbrEntry,
       "rlOspfNbrProcessId": rlOspfNbrProcessId,
       "rlOspfNbrIpAddr": rlOspfNbrIpAddr,
       "rlOspfNbrAddressLessIndex": rlOspfNbrAddressLessIndex,
       "rlOspfNbrRtrId": rlOspfNbrRtrId,
       "rlOspfNbrOptions": rlOspfNbrOptions,
       "rlOspfNbrPriority": rlOspfNbrPriority,
       "rlOspfNbrState": rlOspfNbrState,
       "rlOspfNbrEvents": rlOspfNbrEvents,
       "rlOspfNbrLsRetransQLen": rlOspfNbrLsRetransQLen,
       "rlOspfNbmaNbrStatus": rlOspfNbmaNbrStatus,
       "rlOspfNbmaNbrPermanence": rlOspfNbmaNbrPermanence,
       "rlOspfNbrHelloSuppressed": rlOspfNbrHelloSuppressed,
       "rlOspfNbrRestartHelperStatus": rlOspfNbrRestartHelperStatus,
       "rlOspfNbrRestartHelperAge": rlOspfNbrRestartHelperAge,
       "rlOspfNbrRestartHelperExitReason": rlOspfNbrRestartHelperExitReason,
       "rlOspfNbrDeadTime": rlOspfNbrDeadTime,
       "rlOspfNbrAreaId": rlOspfNbrAreaId,
       "rlOspfNbrIfIndex": rlOspfNbrIfIndex,
       "rlOspfNbrIfIpAddr": rlOspfNbrIfIpAddr,
       "rlOspfVirtNbrTable": rlOspfVirtNbrTable,
       "rlOspfVirtNbrEntry": rlOspfVirtNbrEntry,
       "rlOspfVirtNbrProcessId": rlOspfVirtNbrProcessId,
       "rlOspfVirtNbrArea": rlOspfVirtNbrArea,
       "rlOspfVirtNbrRtrId": rlOspfVirtNbrRtrId,
       "rlOspfVirtNbrIpAddr": rlOspfVirtNbrIpAddr,
       "rlOspfVirtNbrOptions": rlOspfVirtNbrOptions,
       "rlOspfVirtNbrState": rlOspfVirtNbrState,
       "rlOspfVirtNbrEvents": rlOspfVirtNbrEvents,
       "rlOspfVirtNbrLsRetransQLen": rlOspfVirtNbrLsRetransQLen,
       "rlOspfVirtNbrHelloSuppressed": rlOspfVirtNbrHelloSuppressed,
       "rlOspfVirtNbrRestartHelperStatus": rlOspfVirtNbrRestartHelperStatus,
       "rlOspfVirtNbrRestartHelperAge": rlOspfVirtNbrRestartHelperAge,
       "rlOspfVirtNbrRestartHelperExitReason": rlOspfVirtNbrRestartHelperExitReason,
       "rlOspfVirtNbrDeadTime": rlOspfVirtNbrDeadTime,
       "rlOspfExtLsdbTable": rlOspfExtLsdbTable,
       "rlOspfExtLsdbEntry": rlOspfExtLsdbEntry,
       "rlOspfExtLsdbProcessId": rlOspfExtLsdbProcessId,
       "rlOspfExtLsdbType": rlOspfExtLsdbType,
       "rlOspfExtLsdbLsid": rlOspfExtLsdbLsid,
       "rlOspfExtLsdbRouterId": rlOspfExtLsdbRouterId,
       "rlOspfExtLsdbSequence": rlOspfExtLsdbSequence,
       "rlOspfExtLsdbAge": rlOspfExtLsdbAge,
       "rlOspfExtLsdbChecksum": rlOspfExtLsdbChecksum,
       "rlOspfExtLsdbAdvertisement": rlOspfExtLsdbAdvertisement,
       "rlOspfAreaAggregateTable": rlOspfAreaAggregateTable,
       "rlOspfAreaAggregateEntry": rlOspfAreaAggregateEntry,
       "rlOspfAreaAggregateProcessId": rlOspfAreaAggregateProcessId,
       "rlOspfAreaAggregateAreaID": rlOspfAreaAggregateAreaID,
       "rlOspfAreaAggregateLsdbType": rlOspfAreaAggregateLsdbType,
       "rlOspfAreaAggregateNet": rlOspfAreaAggregateNet,
       "rlOspfAreaAggregateMask": rlOspfAreaAggregateMask,
       "rlOspfAreaAggregateStatus": rlOspfAreaAggregateStatus,
       "rlOspfAreaAggregateEffect": rlOspfAreaAggregateEffect,
       "rlOspfAreaAggregateExtRouteTag": rlOspfAreaAggregateExtRouteTag,
       "rlOspfLocalLsdbTable": rlOspfLocalLsdbTable,
       "rlOspfLocalLsdbEntry": rlOspfLocalLsdbEntry,
       "rlOspfLocalLsdbProcessId": rlOspfLocalLsdbProcessId,
       "rlOspfLocalLsdbIpAddress": rlOspfLocalLsdbIpAddress,
       "rlOspfLocalLsdbAddressLessIf": rlOspfLocalLsdbAddressLessIf,
       "rlOspfLocalLsdbType": rlOspfLocalLsdbType,
       "rlOspfLocalLsdbLsid": rlOspfLocalLsdbLsid,
       "rlOspfLocalLsdbRouterId": rlOspfLocalLsdbRouterId,
       "rlOspfLocalLsdbSequence": rlOspfLocalLsdbSequence,
       "rlOspfLocalLsdbAge": rlOspfLocalLsdbAge,
       "rlOspfLocalLsdbChecksum": rlOspfLocalLsdbChecksum,
       "rlOspfLocalLsdbAdvertisement": rlOspfLocalLsdbAdvertisement,
       "rlOspfLocalLsdbAreaId": rlOspfLocalLsdbAreaId,
       "rlOspfVirtLocalLsdbTable": rlOspfVirtLocalLsdbTable,
       "rlOspfVirtLocalLsdbEntry": rlOspfVirtLocalLsdbEntry,
       "rlOspfVirtLocalLsdbProcessId": rlOspfVirtLocalLsdbProcessId,
       "rlOspfVirtLocalLsdbTransitArea": rlOspfVirtLocalLsdbTransitArea,
       "rlOspfVirtLocalLsdbNeighbor": rlOspfVirtLocalLsdbNeighbor,
       "rlOspfVirtLocalLsdbType": rlOspfVirtLocalLsdbType,
       "rlOspfVirtLocalLsdbLsid": rlOspfVirtLocalLsdbLsid,
       "rlOspfVirtLocalLsdbRouterId": rlOspfVirtLocalLsdbRouterId,
       "rlOspfVirtLocalLsdbSequence": rlOspfVirtLocalLsdbSequence,
       "rlOspfVirtLocalLsdbAge": rlOspfVirtLocalLsdbAge,
       "rlOspfVirtLocalLsdbChecksum": rlOspfVirtLocalLsdbChecksum,
       "rlOspfVirtLocalLsdbAdvertisement": rlOspfVirtLocalLsdbAdvertisement,
       "rlOspfEnableTrapsOspfErrors": rlOspfEnableTrapsOspfErrors,
       "rlOspfEnableTrapsOspfLsa": rlOspfEnableTrapsOspfLsa,
       "rlOspfEnableTrapsOspfRateLimitSeconds": rlOspfEnableTrapsOspfRateLimitSeconds,
       "rlOspfEnableTrapsOspfRateLimitTrapNumber": rlOspfEnableTrapsOspfRateLimitTrapNumber,
       "rlOspfEnableTrapsOspfTransmit": rlOspfEnableTrapsOspfTransmit,
       "rlOspfEnableTrapsOspfStateChange": rlOspfEnableTrapsOspfStateChange,
       "rlOspfExt": rlOspfExt,
       "rlOspfBrRouterTable": rlOspfBrRouterTable,
       "rlOspfBrRouterEntry": rlOspfBrRouterEntry,
       "rlOspfBrRouterProcessId": rlOspfBrRouterProcessId,
       "rlOspfBrRouterAreaId": rlOspfBrRouterAreaId,
       "rlOspfBrRouterRouterId": rlOspfBrRouterRouterId,
       "rlOspfBrRouterNextHopIp": rlOspfBrRouterNextHopIp,
       "rlOspfBrRouterOutIf": rlOspfBrRouterOutIf,
       "rlOspfBrRouterRouteType": rlOspfBrRouterRouteType,
       "rlOspfBrRouterRouteCost": rlOspfBrRouterRouteCost,
       "rlOspfBrRouterRouterType": rlOspfBrRouterRouterType}
)

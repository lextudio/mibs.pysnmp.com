# SNMP MIB module (OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:41 2024
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

ospf = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 14)
)
ospf.setRevisions(
        ("2006-11-10 00:00",
         "1995-01-20 12:25")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AreaID(IpAddress, TextualConvention):
    status = "current"


class RouterID(IpAddress, TextualConvention):
    status = "current"


class Metric(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BigMetric(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class Status(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



class PositiveInteger(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class HelloRange(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class UpToMaxAge(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class DesignatedRouterPriority(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TOSType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-0"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )



class OspfAuthenticationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 0),
          ("simplePassword", 1))
    )



# MIB Managed Objects in the order of their OIDs

_OspfGeneralGroup_ObjectIdentity = ObjectIdentity
ospfGeneralGroup = _OspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 1)
)
_OspfRouterId_Type = RouterID
_OspfRouterId_Object = MibScalar
ospfRouterId = _OspfRouterId_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 1),
    _OspfRouterId_Type()
)
ospfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRouterId.setStatus("current")
_OspfAdminStat_Type = Status
_OspfAdminStat_Object = MibScalar
ospfAdminStat = _OspfAdminStat_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 2),
    _OspfAdminStat_Type()
)
ospfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAdminStat.setStatus("current")


class _OspfVersionNumber_Type(Integer32):
    """Custom type ospfVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("version2", 2)
    )


_OspfVersionNumber_Type.__name__ = "Integer32"
_OspfVersionNumber_Object = MibScalar
ospfVersionNumber = _OspfVersionNumber_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 3),
    _OspfVersionNumber_Type()
)
ospfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVersionNumber.setStatus("current")
_OspfAreaBdrRtrStatus_Type = TruthValue
_OspfAreaBdrRtrStatus_Object = MibScalar
ospfAreaBdrRtrStatus = _OspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 4),
    _OspfAreaBdrRtrStatus_Type()
)
ospfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaBdrRtrStatus.setStatus("current")
_OspfASBdrRtrStatus_Type = TruthValue
_OspfASBdrRtrStatus_Object = MibScalar
ospfASBdrRtrStatus = _OspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 5),
    _OspfASBdrRtrStatus_Type()
)
ospfASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfASBdrRtrStatus.setStatus("current")
_OspfExternLsaCount_Type = Gauge32
_OspfExternLsaCount_Object = MibScalar
ospfExternLsaCount = _OspfExternLsaCount_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 6),
    _OspfExternLsaCount_Type()
)
ospfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternLsaCount.setStatus("current")
_OspfExternLsaCksumSum_Type = Integer32
_OspfExternLsaCksumSum_Object = MibScalar
ospfExternLsaCksumSum = _OspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 7),
    _OspfExternLsaCksumSum_Type()
)
ospfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternLsaCksumSum.setStatus("current")
_OspfTOSSupport_Type = TruthValue
_OspfTOSSupport_Object = MibScalar
ospfTOSSupport = _OspfTOSSupport_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 8),
    _OspfTOSSupport_Type()
)
ospfTOSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfTOSSupport.setStatus("current")
_OspfOriginateNewLsas_Type = Counter32
_OspfOriginateNewLsas_Object = MibScalar
ospfOriginateNewLsas = _OspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 9),
    _OspfOriginateNewLsas_Type()
)
ospfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfOriginateNewLsas.setStatus("current")
_OspfRxNewLsas_Type = Counter32
_OspfRxNewLsas_Object = MibScalar
ospfRxNewLsas = _OspfRxNewLsas_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 10),
    _OspfRxNewLsas_Type()
)
ospfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRxNewLsas.setStatus("current")


class _OspfExtLsdbLimit_Type(Integer32):
    """Custom type ospfExtLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_OspfExtLsdbLimit_Type.__name__ = "Integer32"
_OspfExtLsdbLimit_Object = MibScalar
ospfExtLsdbLimit = _OspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 11),
    _OspfExtLsdbLimit_Type()
)
ospfExtLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfExtLsdbLimit.setStatus("current")


class _OspfMulticastExtensions_Type(Integer32):
    """Custom type ospfMulticastExtensions based on Integer32"""
    defaultValue = 0


_OspfMulticastExtensions_Object = MibScalar
ospfMulticastExtensions = _OspfMulticastExtensions_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 12),
    _OspfMulticastExtensions_Type()
)
ospfMulticastExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfMulticastExtensions.setStatus("current")


class _OspfExitOverflowInterval_Type(PositiveInteger):
    """Custom type ospfExitOverflowInterval based on PositiveInteger"""
    defaultValue = 0


_OspfExitOverflowInterval_Object = MibScalar
ospfExitOverflowInterval = _OspfExitOverflowInterval_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 13),
    _OspfExitOverflowInterval_Type()
)
ospfExitOverflowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfExitOverflowInterval.setStatus("current")
_OspfDemandExtensions_Type = TruthValue
_OspfDemandExtensions_Object = MibScalar
ospfDemandExtensions = _OspfDemandExtensions_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 14),
    _OspfDemandExtensions_Type()
)
ospfDemandExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfDemandExtensions.setStatus("current")
_OspfRFC1583Compatibility_Type = TruthValue
_OspfRFC1583Compatibility_Object = MibScalar
ospfRFC1583Compatibility = _OspfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 15),
    _OspfRFC1583Compatibility_Type()
)
ospfRFC1583Compatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRFC1583Compatibility.setStatus("current")
_OspfOpaqueLsaSupport_Type = TruthValue
_OspfOpaqueLsaSupport_Object = MibScalar
ospfOpaqueLsaSupport = _OspfOpaqueLsaSupport_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 16),
    _OspfOpaqueLsaSupport_Type()
)
ospfOpaqueLsaSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfOpaqueLsaSupport.setStatus("current")
_OspfReferenceBandwidth_Type = Unsigned32
_OspfReferenceBandwidth_Object = MibScalar
ospfReferenceBandwidth = _OspfReferenceBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 17),
    _OspfReferenceBandwidth_Type()
)
ospfReferenceBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfReferenceBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    ospfReferenceBandwidth.setUnits("kilobits per second")


class _OspfRestartSupport_Type(Integer32):
    """Custom type ospfRestartSupport based on Integer32"""
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


_OspfRestartSupport_Type.__name__ = "Integer32"
_OspfRestartSupport_Object = MibScalar
ospfRestartSupport = _OspfRestartSupport_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 18),
    _OspfRestartSupport_Type()
)
ospfRestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRestartSupport.setStatus("current")


class _OspfRestartInterval_Type(Integer32):
    """Custom type ospfRestartInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_OspfRestartInterval_Type.__name__ = "Integer32"
_OspfRestartInterval_Object = MibScalar
ospfRestartInterval = _OspfRestartInterval_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 19),
    _OspfRestartInterval_Type()
)
ospfRestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRestartInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfRestartInterval.setUnits("seconds")
_OspfRestartStrictLsaChecking_Type = TruthValue
_OspfRestartStrictLsaChecking_Object = MibScalar
ospfRestartStrictLsaChecking = _OspfRestartStrictLsaChecking_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 20),
    _OspfRestartStrictLsaChecking_Type()
)
ospfRestartStrictLsaChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRestartStrictLsaChecking.setStatus("current")


class _OspfRestartStatus_Type(Integer32):
    """Custom type ospfRestartStatus based on Integer32"""
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


_OspfRestartStatus_Type.__name__ = "Integer32"
_OspfRestartStatus_Object = MibScalar
ospfRestartStatus = _OspfRestartStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 21),
    _OspfRestartStatus_Type()
)
ospfRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRestartStatus.setStatus("current")
_OspfRestartAge_Type = Unsigned32
_OspfRestartAge_Object = MibScalar
ospfRestartAge = _OspfRestartAge_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 22),
    _OspfRestartAge_Type()
)
ospfRestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRestartAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfRestartAge.setUnits("seconds")


class _OspfRestartExitReason_Type(Integer32):
    """Custom type ospfRestartExitReason based on Integer32"""
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


_OspfRestartExitReason_Type.__name__ = "Integer32"
_OspfRestartExitReason_Object = MibScalar
ospfRestartExitReason = _OspfRestartExitReason_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 23),
    _OspfRestartExitReason_Type()
)
ospfRestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRestartExitReason.setStatus("current")
_OspfAsLsaCount_Type = Gauge32
_OspfAsLsaCount_Object = MibScalar
ospfAsLsaCount = _OspfAsLsaCount_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 24),
    _OspfAsLsaCount_Type()
)
ospfAsLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAsLsaCount.setStatus("current")
_OspfAsLsaCksumSum_Type = Unsigned32
_OspfAsLsaCksumSum_Object = MibScalar
ospfAsLsaCksumSum = _OspfAsLsaCksumSum_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 25),
    _OspfAsLsaCksumSum_Type()
)
ospfAsLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAsLsaCksumSum.setStatus("current")
_OspfStubRouterSupport_Type = TruthValue
_OspfStubRouterSupport_Object = MibScalar
ospfStubRouterSupport = _OspfStubRouterSupport_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 26),
    _OspfStubRouterSupport_Type()
)
ospfStubRouterSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStubRouterSupport.setStatus("current")


class _OspfStubRouterAdvertisement_Type(Integer32):
    """Custom type ospfStubRouterAdvertisement based on Integer32"""
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


_OspfStubRouterAdvertisement_Type.__name__ = "Integer32"
_OspfStubRouterAdvertisement_Object = MibScalar
ospfStubRouterAdvertisement = _OspfStubRouterAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 27),
    _OspfStubRouterAdvertisement_Type()
)
ospfStubRouterAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfStubRouterAdvertisement.setStatus("current")
_OspfDiscontinuityTime_Type = TimeStamp
_OspfDiscontinuityTime_Object = MibScalar
ospfDiscontinuityTime = _OspfDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 14, 1, 28),
    _OspfDiscontinuityTime_Type()
)
ospfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDiscontinuityTime.setStatus("current")
_OspfAreaTable_Object = MibTable
ospfAreaTable = _OspfAreaTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 2)
)
if mibBuilder.loadTexts:
    ospfAreaTable.setStatus("current")
_OspfAreaEntry_Object = MibTableRow
ospfAreaEntry = _OspfAreaEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1)
)
ospfAreaEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfAreaId"),
)
if mibBuilder.loadTexts:
    ospfAreaEntry.setStatus("current")
_OspfAreaId_Type = AreaID
_OspfAreaId_Object = MibTableColumn
ospfAreaId = _OspfAreaId_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 1),
    _OspfAreaId_Type()
)
ospfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaId.setStatus("current")


class _OspfAuthType_Type(OspfAuthenticationType):
    """Custom type ospfAuthType based on OspfAuthenticationType"""


_OspfAuthType_Object = MibTableColumn
ospfAuthType = _OspfAuthType_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 2),
    _OspfAuthType_Type()
)
ospfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfAuthType.setStatus("obsolete")


class _OspfImportAsExtern_Type(Integer32):
    """Custom type ospfImportAsExtern based on Integer32"""
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


_OspfImportAsExtern_Type.__name__ = "Integer32"
_OspfImportAsExtern_Object = MibTableColumn
ospfImportAsExtern = _OspfImportAsExtern_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 3),
    _OspfImportAsExtern_Type()
)
ospfImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfImportAsExtern.setStatus("current")
_OspfSpfRuns_Type = Counter32
_OspfSpfRuns_Object = MibTableColumn
ospfSpfRuns = _OspfSpfRuns_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 4),
    _OspfSpfRuns_Type()
)
ospfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfSpfRuns.setStatus("current")
_OspfAreaBdrRtrCount_Type = Gauge32
_OspfAreaBdrRtrCount_Object = MibTableColumn
ospfAreaBdrRtrCount = _OspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 5),
    _OspfAreaBdrRtrCount_Type()
)
ospfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaBdrRtrCount.setStatus("current")
_OspfAsBdrRtrCount_Type = Gauge32
_OspfAsBdrRtrCount_Object = MibTableColumn
ospfAsBdrRtrCount = _OspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 6),
    _OspfAsBdrRtrCount_Type()
)
ospfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAsBdrRtrCount.setStatus("current")
_OspfAreaLsaCount_Type = Gauge32
_OspfAreaLsaCount_Object = MibTableColumn
ospfAreaLsaCount = _OspfAreaLsaCount_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 7),
    _OspfAreaLsaCount_Type()
)
ospfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaLsaCount.setStatus("current")


class _OspfAreaLsaCksumSum_Type(Integer32):
    """Custom type ospfAreaLsaCksumSum based on Integer32"""
    defaultValue = 0


_OspfAreaLsaCksumSum_Object = MibTableColumn
ospfAreaLsaCksumSum = _OspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 8),
    _OspfAreaLsaCksumSum_Type()
)
ospfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaLsaCksumSum.setStatus("current")


class _OspfAreaSummary_Type(Integer32):
    """Custom type ospfAreaSummary based on Integer32"""
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


_OspfAreaSummary_Type.__name__ = "Integer32"
_OspfAreaSummary_Object = MibTableColumn
ospfAreaSummary = _OspfAreaSummary_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 9),
    _OspfAreaSummary_Type()
)
ospfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfAreaSummary.setStatus("current")
_OspfAreaStatus_Type = RowStatus
_OspfAreaStatus_Object = MibTableColumn
ospfAreaStatus = _OspfAreaStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 10),
    _OspfAreaStatus_Type()
)
ospfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfAreaStatus.setStatus("current")


class _OspfAreaNssaTranslatorRole_Type(Integer32):
    """Custom type ospfAreaNssaTranslatorRole based on Integer32"""
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


_OspfAreaNssaTranslatorRole_Type.__name__ = "Integer32"
_OspfAreaNssaTranslatorRole_Object = MibTableColumn
ospfAreaNssaTranslatorRole = _OspfAreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 11),
    _OspfAreaNssaTranslatorRole_Type()
)
ospfAreaNssaTranslatorRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfAreaNssaTranslatorRole.setStatus("current")


class _OspfAreaNssaTranslatorState_Type(Integer32):
    """Custom type ospfAreaNssaTranslatorState based on Integer32"""
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


_OspfAreaNssaTranslatorState_Type.__name__ = "Integer32"
_OspfAreaNssaTranslatorState_Object = MibTableColumn
ospfAreaNssaTranslatorState = _OspfAreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 12),
    _OspfAreaNssaTranslatorState_Type()
)
ospfAreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNssaTranslatorState.setStatus("current")


class _OspfAreaNssaTranslatorStabilityInterval_Type(PositiveInteger):
    """Custom type ospfAreaNssaTranslatorStabilityInterval based on PositiveInteger"""
    defaultValue = 40


_OspfAreaNssaTranslatorStabilityInterval_Object = MibTableColumn
ospfAreaNssaTranslatorStabilityInterval = _OspfAreaNssaTranslatorStabilityInterval_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 13),
    _OspfAreaNssaTranslatorStabilityInterval_Type()
)
ospfAreaNssaTranslatorStabilityInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfAreaNssaTranslatorStabilityInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfAreaNssaTranslatorStabilityInterval.setUnits("seconds")
_OspfAreaNssaTranslatorEvents_Type = Counter32
_OspfAreaNssaTranslatorEvents_Object = MibTableColumn
ospfAreaNssaTranslatorEvents = _OspfAreaNssaTranslatorEvents_Object(
    (1, 3, 6, 1, 2, 1, 14, 2, 1, 14),
    _OspfAreaNssaTranslatorEvents_Type()
)
ospfAreaNssaTranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNssaTranslatorEvents.setStatus("current")
_OspfStubAreaTable_Object = MibTable
ospfStubAreaTable = _OspfStubAreaTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 3)
)
if mibBuilder.loadTexts:
    ospfStubAreaTable.setStatus("current")
_OspfStubAreaEntry_Object = MibTableRow
ospfStubAreaEntry = _OspfStubAreaEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 3, 1)
)
ospfStubAreaEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfStubAreaId"),
    (0, "OSPF-MIB", "ospfStubTOS"),
)
if mibBuilder.loadTexts:
    ospfStubAreaEntry.setStatus("current")
_OspfStubAreaId_Type = AreaID
_OspfStubAreaId_Object = MibTableColumn
ospfStubAreaId = _OspfStubAreaId_Object(
    (1, 3, 6, 1, 2, 1, 14, 3, 1, 1),
    _OspfStubAreaId_Type()
)
ospfStubAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStubAreaId.setStatus("current")
_OspfStubTOS_Type = TOSType
_OspfStubTOS_Object = MibTableColumn
ospfStubTOS = _OspfStubTOS_Object(
    (1, 3, 6, 1, 2, 1, 14, 3, 1, 2),
    _OspfStubTOS_Type()
)
ospfStubTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStubTOS.setStatus("current")
_OspfStubMetric_Type = BigMetric
_OspfStubMetric_Object = MibTableColumn
ospfStubMetric = _OspfStubMetric_Object(
    (1, 3, 6, 1, 2, 1, 14, 3, 1, 3),
    _OspfStubMetric_Type()
)
ospfStubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfStubMetric.setStatus("current")
_OspfStubStatus_Type = RowStatus
_OspfStubStatus_Object = MibTableColumn
ospfStubStatus = _OspfStubStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 3, 1, 4),
    _OspfStubStatus_Type()
)
ospfStubStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfStubStatus.setStatus("current")


class _OspfStubMetricType_Type(Integer32):
    """Custom type ospfStubMetricType based on Integer32"""
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


_OspfStubMetricType_Type.__name__ = "Integer32"
_OspfStubMetricType_Object = MibTableColumn
ospfStubMetricType = _OspfStubMetricType_Object(
    (1, 3, 6, 1, 2, 1, 14, 3, 1, 5),
    _OspfStubMetricType_Type()
)
ospfStubMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfStubMetricType.setStatus("current")
_OspfLsdbTable_Object = MibTable
ospfLsdbTable = _OspfLsdbTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 4)
)
if mibBuilder.loadTexts:
    ospfLsdbTable.setStatus("current")
_OspfLsdbEntry_Object = MibTableRow
ospfLsdbEntry = _OspfLsdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 4, 1)
)
ospfLsdbEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfLsdbAreaId"),
    (0, "OSPF-MIB", "ospfLsdbType"),
    (0, "OSPF-MIB", "ospfLsdbLsid"),
    (0, "OSPF-MIB", "ospfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfLsdbEntry.setStatus("current")
_OspfLsdbAreaId_Type = AreaID
_OspfLsdbAreaId_Object = MibTableColumn
ospfLsdbAreaId = _OspfLsdbAreaId_Object(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 1),
    _OspfLsdbAreaId_Type()
)
ospfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbAreaId.setStatus("current")


class _OspfLsdbType_Type(Integer32):
    """Custom type ospfLsdbType based on Integer32"""
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


_OspfLsdbType_Type.__name__ = "Integer32"
_OspfLsdbType_Object = MibTableColumn
ospfLsdbType = _OspfLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 2),
    _OspfLsdbType_Type()
)
ospfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbType.setStatus("current")
_OspfLsdbLsid_Type = IpAddress
_OspfLsdbLsid_Object = MibTableColumn
ospfLsdbLsid = _OspfLsdbLsid_Object(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 3),
    _OspfLsdbLsid_Type()
)
ospfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbLsid.setStatus("current")
_OspfLsdbRouterId_Type = RouterID
_OspfLsdbRouterId_Object = MibTableColumn
ospfLsdbRouterId = _OspfLsdbRouterId_Object(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 4),
    _OspfLsdbRouterId_Type()
)
ospfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbRouterId.setStatus("current")
_OspfLsdbSequence_Type = Integer32
_OspfLsdbSequence_Object = MibTableColumn
ospfLsdbSequence = _OspfLsdbSequence_Object(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 5),
    _OspfLsdbSequence_Type()
)
ospfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbSequence.setStatus("current")
_OspfLsdbAge_Type = Integer32
_OspfLsdbAge_Object = MibTableColumn
ospfLsdbAge = _OspfLsdbAge_Object(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 6),
    _OspfLsdbAge_Type()
)
ospfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfLsdbAge.setUnits("seconds")
_OspfLsdbChecksum_Type = Integer32
_OspfLsdbChecksum_Object = MibTableColumn
ospfLsdbChecksum = _OspfLsdbChecksum_Object(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 7),
    _OspfLsdbChecksum_Type()
)
ospfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbChecksum.setStatus("current")


class _OspfLsdbAdvertisement_Type(OctetString):
    """Custom type ospfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_OspfLsdbAdvertisement_Type.__name__ = "OctetString"
_OspfLsdbAdvertisement_Object = MibTableColumn
ospfLsdbAdvertisement = _OspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 14, 4, 1, 8),
    _OspfLsdbAdvertisement_Type()
)
ospfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbAdvertisement.setStatus("current")
_OspfAreaRangeTable_Object = MibTable
ospfAreaRangeTable = _OspfAreaRangeTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 5)
)
if mibBuilder.loadTexts:
    ospfAreaRangeTable.setStatus("obsolete")
_OspfAreaRangeEntry_Object = MibTableRow
ospfAreaRangeEntry = _OspfAreaRangeEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 5, 1)
)
ospfAreaRangeEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfAreaRangeAreaId"),
    (0, "OSPF-MIB", "ospfAreaRangeNet"),
)
if mibBuilder.loadTexts:
    ospfAreaRangeEntry.setStatus("obsolete")
_OspfAreaRangeAreaId_Type = AreaID
_OspfAreaRangeAreaId_Object = MibTableColumn
ospfAreaRangeAreaId = _OspfAreaRangeAreaId_Object(
    (1, 3, 6, 1, 2, 1, 14, 5, 1, 1),
    _OspfAreaRangeAreaId_Type()
)
ospfAreaRangeAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRangeAreaId.setStatus("obsolete")
_OspfAreaRangeNet_Type = IpAddress
_OspfAreaRangeNet_Object = MibTableColumn
ospfAreaRangeNet = _OspfAreaRangeNet_Object(
    (1, 3, 6, 1, 2, 1, 14, 5, 1, 2),
    _OspfAreaRangeNet_Type()
)
ospfAreaRangeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaRangeNet.setStatus("obsolete")
_OspfAreaRangeMask_Type = IpAddress
_OspfAreaRangeMask_Object = MibTableColumn
ospfAreaRangeMask = _OspfAreaRangeMask_Object(
    (1, 3, 6, 1, 2, 1, 14, 5, 1, 3),
    _OspfAreaRangeMask_Type()
)
ospfAreaRangeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfAreaRangeMask.setStatus("obsolete")
_OspfAreaRangeStatus_Type = RowStatus
_OspfAreaRangeStatus_Object = MibTableColumn
ospfAreaRangeStatus = _OspfAreaRangeStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 5, 1, 4),
    _OspfAreaRangeStatus_Type()
)
ospfAreaRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfAreaRangeStatus.setStatus("obsolete")


class _OspfAreaRangeEffect_Type(Integer32):
    """Custom type ospfAreaRangeEffect based on Integer32"""
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


_OspfAreaRangeEffect_Type.__name__ = "Integer32"
_OspfAreaRangeEffect_Object = MibTableColumn
ospfAreaRangeEffect = _OspfAreaRangeEffect_Object(
    (1, 3, 6, 1, 2, 1, 14, 5, 1, 5),
    _OspfAreaRangeEffect_Type()
)
ospfAreaRangeEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfAreaRangeEffect.setStatus("obsolete")
_OspfHostTable_Object = MibTable
ospfHostTable = _OspfHostTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 6)
)
if mibBuilder.loadTexts:
    ospfHostTable.setStatus("current")
_OspfHostEntry_Object = MibTableRow
ospfHostEntry = _OspfHostEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 6, 1)
)
ospfHostEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfHostIpAddress"),
    (0, "OSPF-MIB", "ospfHostTOS"),
)
if mibBuilder.loadTexts:
    ospfHostEntry.setStatus("current")
_OspfHostIpAddress_Type = IpAddress
_OspfHostIpAddress_Object = MibTableColumn
ospfHostIpAddress = _OspfHostIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 14, 6, 1, 1),
    _OspfHostIpAddress_Type()
)
ospfHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfHostIpAddress.setStatus("current")
_OspfHostTOS_Type = TOSType
_OspfHostTOS_Object = MibTableColumn
ospfHostTOS = _OspfHostTOS_Object(
    (1, 3, 6, 1, 2, 1, 14, 6, 1, 2),
    _OspfHostTOS_Type()
)
ospfHostTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfHostTOS.setStatus("current")
_OspfHostMetric_Type = Metric
_OspfHostMetric_Object = MibTableColumn
ospfHostMetric = _OspfHostMetric_Object(
    (1, 3, 6, 1, 2, 1, 14, 6, 1, 3),
    _OspfHostMetric_Type()
)
ospfHostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfHostMetric.setStatus("current")
_OspfHostStatus_Type = RowStatus
_OspfHostStatus_Object = MibTableColumn
ospfHostStatus = _OspfHostStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 6, 1, 4),
    _OspfHostStatus_Type()
)
ospfHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfHostStatus.setStatus("current")
_OspfHostAreaID_Type = AreaID
_OspfHostAreaID_Object = MibTableColumn
ospfHostAreaID = _OspfHostAreaID_Object(
    (1, 3, 6, 1, 2, 1, 14, 6, 1, 5),
    _OspfHostAreaID_Type()
)
ospfHostAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfHostAreaID.setStatus("deprecated")
_OspfHostCfgAreaID_Type = AreaID
_OspfHostCfgAreaID_Object = MibTableColumn
ospfHostCfgAreaID = _OspfHostCfgAreaID_Object(
    (1, 3, 6, 1, 2, 1, 14, 6, 1, 6),
    _OspfHostCfgAreaID_Type()
)
ospfHostCfgAreaID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfHostCfgAreaID.setStatus("current")
_OspfIfTable_Object = MibTable
ospfIfTable = _OspfIfTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 7)
)
if mibBuilder.loadTexts:
    ospfIfTable.setStatus("current")
_OspfIfEntry_Object = MibTableRow
ospfIfEntry = _OspfIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1)
)
ospfIfEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    ospfIfEntry.setStatus("current")
_OspfIfIpAddress_Type = IpAddress
_OspfIfIpAddress_Object = MibTableColumn
ospfIfIpAddress = _OspfIfIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 1),
    _OspfIfIpAddress_Type()
)
ospfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfIpAddress.setStatus("current")
_OspfAddressLessIf_Type = InterfaceIndexOrZero
_OspfAddressLessIf_Object = MibTableColumn
ospfAddressLessIf = _OspfAddressLessIf_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 2),
    _OspfAddressLessIf_Type()
)
ospfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAddressLessIf.setStatus("current")


class _OspfIfAreaId_Type(AreaID):
    """Custom type ospfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_OspfIfAreaId_Object = MibTableColumn
ospfIfAreaId = _OspfIfAreaId_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 3),
    _OspfIfAreaId_Type()
)
ospfIfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfAreaId.setStatus("current")


class _OspfIfType_Type(Integer32):
    """Custom type ospfIfType based on Integer32"""
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


_OspfIfType_Type.__name__ = "Integer32"
_OspfIfType_Object = MibTableColumn
ospfIfType = _OspfIfType_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 4),
    _OspfIfType_Type()
)
ospfIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfType.setStatus("current")


class _OspfIfAdminStat_Type(Status):
    """Custom type ospfIfAdminStat based on Status"""


_OspfIfAdminStat_Object = MibTableColumn
ospfIfAdminStat = _OspfIfAdminStat_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 5),
    _OspfIfAdminStat_Type()
)
ospfIfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfAdminStat.setStatus("current")


class _OspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type ospfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_OspfIfRtrPriority_Object = MibTableColumn
ospfIfRtrPriority = _OspfIfRtrPriority_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 6),
    _OspfIfRtrPriority_Type()
)
ospfIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfRtrPriority.setStatus("current")


class _OspfIfTransitDelay_Type(UpToMaxAge):
    """Custom type ospfIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_OspfIfTransitDelay_Object = MibTableColumn
ospfIfTransitDelay = _OspfIfTransitDelay_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 7),
    _OspfIfTransitDelay_Type()
)
ospfIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    ospfIfTransitDelay.setUnits("seconds")


class _OspfIfRetransInterval_Type(UpToMaxAge):
    """Custom type ospfIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_OspfIfRetransInterval_Object = MibTableColumn
ospfIfRetransInterval = _OspfIfRetransInterval_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 8),
    _OspfIfRetransInterval_Type()
)
ospfIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfIfRetransInterval.setUnits("seconds")


class _OspfIfHelloInterval_Type(HelloRange):
    """Custom type ospfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_OspfIfHelloInterval_Object = MibTableColumn
ospfIfHelloInterval = _OspfIfHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 9),
    _OspfIfHelloInterval_Type()
)
ospfIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfIfHelloInterval.setUnits("seconds")


class _OspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type ospfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_OspfIfRtrDeadInterval_Object = MibTableColumn
ospfIfRtrDeadInterval = _OspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 10),
    _OspfIfRtrDeadInterval_Type()
)
ospfIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfIfRtrDeadInterval.setUnits("seconds")


class _OspfIfPollInterval_Type(PositiveInteger):
    """Custom type ospfIfPollInterval based on PositiveInteger"""
    defaultValue = 120


_OspfIfPollInterval_Object = MibTableColumn
ospfIfPollInterval = _OspfIfPollInterval_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 11),
    _OspfIfPollInterval_Type()
)
ospfIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfIfPollInterval.setUnits("seconds")


class _OspfIfState_Type(Integer32):
    """Custom type ospfIfState based on Integer32"""
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


_OspfIfState_Type.__name__ = "Integer32"
_OspfIfState_Object = MibTableColumn
ospfIfState = _OspfIfState_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 12),
    _OspfIfState_Type()
)
ospfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfState.setStatus("current")


class _OspfIfDesignatedRouter_Type(IpAddress):
    """Custom type ospfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_OspfIfDesignatedRouter_Object = MibTableColumn
ospfIfDesignatedRouter = _OspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 13),
    _OspfIfDesignatedRouter_Type()
)
ospfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfDesignatedRouter.setStatus("current")


class _OspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type ospfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_OspfIfBackupDesignatedRouter_Object = MibTableColumn
ospfIfBackupDesignatedRouter = _OspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 14),
    _OspfIfBackupDesignatedRouter_Type()
)
ospfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfBackupDesignatedRouter.setStatus("current")
_OspfIfEvents_Type = Counter32
_OspfIfEvents_Object = MibTableColumn
ospfIfEvents = _OspfIfEvents_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 15),
    _OspfIfEvents_Type()
)
ospfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfEvents.setStatus("current")


class _OspfIfAuthKey_Type(OctetString):
    """Custom type ospfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspfIfAuthKey_Type.__name__ = "OctetString"
_OspfIfAuthKey_Object = MibTableColumn
ospfIfAuthKey = _OspfIfAuthKey_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 16),
    _OspfIfAuthKey_Type()
)
ospfIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfAuthKey.setStatus("current")
_OspfIfStatus_Type = RowStatus
_OspfIfStatus_Object = MibTableColumn
ospfIfStatus = _OspfIfStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 17),
    _OspfIfStatus_Type()
)
ospfIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfStatus.setStatus("current")


class _OspfIfMulticastForwarding_Type(Integer32):
    """Custom type ospfIfMulticastForwarding based on Integer32"""
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


_OspfIfMulticastForwarding_Type.__name__ = "Integer32"
_OspfIfMulticastForwarding_Object = MibTableColumn
ospfIfMulticastForwarding = _OspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 18),
    _OspfIfMulticastForwarding_Type()
)
ospfIfMulticastForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfMulticastForwarding.setStatus("current")


class _OspfIfDemand_Type(TruthValue):
    """Custom type ospfIfDemand based on TruthValue"""


_OspfIfDemand_Object = MibTableColumn
ospfIfDemand = _OspfIfDemand_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 19),
    _OspfIfDemand_Type()
)
ospfIfDemand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfDemand.setStatus("current")


class _OspfIfAuthType_Type(OspfAuthenticationType):
    """Custom type ospfIfAuthType based on OspfAuthenticationType"""


_OspfIfAuthType_Object = MibTableColumn
ospfIfAuthType = _OspfIfAuthType_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 20),
    _OspfIfAuthType_Type()
)
ospfIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfAuthType.setStatus("current")
_OspfIfLsaCount_Type = Gauge32
_OspfIfLsaCount_Object = MibTableColumn
ospfIfLsaCount = _OspfIfLsaCount_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 21),
    _OspfIfLsaCount_Type()
)
ospfIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfLsaCount.setStatus("current")
_OspfIfLsaCksumSum_Type = Unsigned32
_OspfIfLsaCksumSum_Object = MibTableColumn
ospfIfLsaCksumSum = _OspfIfLsaCksumSum_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 22),
    _OspfIfLsaCksumSum_Type()
)
ospfIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfLsaCksumSum.setStatus("current")
_OspfIfDesignatedRouterId_Type = RouterID
_OspfIfDesignatedRouterId_Object = MibTableColumn
ospfIfDesignatedRouterId = _OspfIfDesignatedRouterId_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 23),
    _OspfIfDesignatedRouterId_Type()
)
ospfIfDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfDesignatedRouterId.setStatus("current")
_OspfIfBackupDesignatedRouterId_Type = RouterID
_OspfIfBackupDesignatedRouterId_Object = MibTableColumn
ospfIfBackupDesignatedRouterId = _OspfIfBackupDesignatedRouterId_Object(
    (1, 3, 6, 1, 2, 1, 14, 7, 1, 24),
    _OspfIfBackupDesignatedRouterId_Type()
)
ospfIfBackupDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfBackupDesignatedRouterId.setStatus("current")
_OspfIfMetricTable_Object = MibTable
ospfIfMetricTable = _OspfIfMetricTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 8)
)
if mibBuilder.loadTexts:
    ospfIfMetricTable.setStatus("current")
_OspfIfMetricEntry_Object = MibTableRow
ospfIfMetricEntry = _OspfIfMetricEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 8, 1)
)
ospfIfMetricEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfMetricIpAddress"),
    (0, "OSPF-MIB", "ospfIfMetricAddressLessIf"),
    (0, "OSPF-MIB", "ospfIfMetricTOS"),
)
if mibBuilder.loadTexts:
    ospfIfMetricEntry.setStatus("current")
_OspfIfMetricIpAddress_Type = IpAddress
_OspfIfMetricIpAddress_Object = MibTableColumn
ospfIfMetricIpAddress = _OspfIfMetricIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 14, 8, 1, 1),
    _OspfIfMetricIpAddress_Type()
)
ospfIfMetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfMetricIpAddress.setStatus("current")
_OspfIfMetricAddressLessIf_Type = InterfaceIndexOrZero
_OspfIfMetricAddressLessIf_Object = MibTableColumn
ospfIfMetricAddressLessIf = _OspfIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 2, 1, 14, 8, 1, 2),
    _OspfIfMetricAddressLessIf_Type()
)
ospfIfMetricAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfMetricAddressLessIf.setStatus("current")
_OspfIfMetricTOS_Type = TOSType
_OspfIfMetricTOS_Object = MibTableColumn
ospfIfMetricTOS = _OspfIfMetricTOS_Object(
    (1, 3, 6, 1, 2, 1, 14, 8, 1, 3),
    _OspfIfMetricTOS_Type()
)
ospfIfMetricTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfMetricTOS.setStatus("current")
_OspfIfMetricValue_Type = Metric
_OspfIfMetricValue_Object = MibTableColumn
ospfIfMetricValue = _OspfIfMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 14, 8, 1, 4),
    _OspfIfMetricValue_Type()
)
ospfIfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfMetricValue.setStatus("current")
_OspfIfMetricStatus_Type = RowStatus
_OspfIfMetricStatus_Object = MibTableColumn
ospfIfMetricStatus = _OspfIfMetricStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 8, 1, 5),
    _OspfIfMetricStatus_Type()
)
ospfIfMetricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfMetricStatus.setStatus("current")
_OspfVirtIfTable_Object = MibTable
ospfVirtIfTable = _OspfVirtIfTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 9)
)
if mibBuilder.loadTexts:
    ospfVirtIfTable.setStatus("current")
_OspfVirtIfEntry_Object = MibTableRow
ospfVirtIfEntry = _OspfVirtIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1)
)
ospfVirtIfEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfVirtIfAreaId"),
    (0, "OSPF-MIB", "ospfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    ospfVirtIfEntry.setStatus("current")
_OspfVirtIfAreaId_Type = AreaID
_OspfVirtIfAreaId_Object = MibTableColumn
ospfVirtIfAreaId = _OspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 1),
    _OspfVirtIfAreaId_Type()
)
ospfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIfAreaId.setStatus("current")
_OspfVirtIfNeighbor_Type = RouterID
_OspfVirtIfNeighbor_Object = MibTableColumn
ospfVirtIfNeighbor = _OspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 2),
    _OspfVirtIfNeighbor_Type()
)
ospfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIfNeighbor.setStatus("current")


class _OspfVirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type ospfVirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_OspfVirtIfTransitDelay_Object = MibTableColumn
ospfVirtIfTransitDelay = _OspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 3),
    _OspfVirtIfTransitDelay_Type()
)
ospfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfVirtIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    ospfVirtIfTransitDelay.setUnits("seconds")


class _OspfVirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type ospfVirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_OspfVirtIfRetransInterval_Object = MibTableColumn
ospfVirtIfRetransInterval = _OspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 4),
    _OspfVirtIfRetransInterval_Type()
)
ospfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfVirtIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfVirtIfRetransInterval.setUnits("seconds")


class _OspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type ospfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_OspfVirtIfHelloInterval_Object = MibTableColumn
ospfVirtIfHelloInterval = _OspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 5),
    _OspfVirtIfHelloInterval_Type()
)
ospfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfVirtIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfVirtIfHelloInterval.setUnits("seconds")


class _OspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type ospfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 60


_OspfVirtIfRtrDeadInterval_Object = MibTableColumn
ospfVirtIfRtrDeadInterval = _OspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 6),
    _OspfVirtIfRtrDeadInterval_Type()
)
ospfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfVirtIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    ospfVirtIfRtrDeadInterval.setUnits("seconds")


class _OspfVirtIfState_Type(Integer32):
    """Custom type ospfVirtIfState based on Integer32"""
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


_OspfVirtIfState_Type.__name__ = "Integer32"
_OspfVirtIfState_Object = MibTableColumn
ospfVirtIfState = _OspfVirtIfState_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 7),
    _OspfVirtIfState_Type()
)
ospfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIfState.setStatus("current")
_OspfVirtIfEvents_Type = Counter32
_OspfVirtIfEvents_Object = MibTableColumn
ospfVirtIfEvents = _OspfVirtIfEvents_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 8),
    _OspfVirtIfEvents_Type()
)
ospfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIfEvents.setStatus("current")


class _OspfVirtIfAuthKey_Type(OctetString):
    """Custom type ospfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspfVirtIfAuthKey_Type.__name__ = "OctetString"
_OspfVirtIfAuthKey_Object = MibTableColumn
ospfVirtIfAuthKey = _OspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 9),
    _OspfVirtIfAuthKey_Type()
)
ospfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfVirtIfAuthKey.setStatus("current")
_OspfVirtIfStatus_Type = RowStatus
_OspfVirtIfStatus_Object = MibTableColumn
ospfVirtIfStatus = _OspfVirtIfStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 10),
    _OspfVirtIfStatus_Type()
)
ospfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfVirtIfStatus.setStatus("current")


class _OspfVirtIfAuthType_Type(OspfAuthenticationType):
    """Custom type ospfVirtIfAuthType based on OspfAuthenticationType"""


_OspfVirtIfAuthType_Object = MibTableColumn
ospfVirtIfAuthType = _OspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 11),
    _OspfVirtIfAuthType_Type()
)
ospfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfVirtIfAuthType.setStatus("current")
_OspfVirtIfLsaCount_Type = Gauge32
_OspfVirtIfLsaCount_Object = MibTableColumn
ospfVirtIfLsaCount = _OspfVirtIfLsaCount_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 12),
    _OspfVirtIfLsaCount_Type()
)
ospfVirtIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIfLsaCount.setStatus("current")
_OspfVirtIfLsaCksumSum_Type = Unsigned32
_OspfVirtIfLsaCksumSum_Object = MibTableColumn
ospfVirtIfLsaCksumSum = _OspfVirtIfLsaCksumSum_Object(
    (1, 3, 6, 1, 2, 1, 14, 9, 1, 13),
    _OspfVirtIfLsaCksumSum_Type()
)
ospfVirtIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIfLsaCksumSum.setStatus("current")
_OspfNbrTable_Object = MibTable
ospfNbrTable = _OspfNbrTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 10)
)
if mibBuilder.loadTexts:
    ospfNbrTable.setStatus("current")
_OspfNbrEntry_Object = MibTableRow
ospfNbrEntry = _OspfNbrEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1)
)
ospfNbrEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfNbrIpAddr"),
    (0, "OSPF-MIB", "ospfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    ospfNbrEntry.setStatus("current")
_OspfNbrIpAddr_Type = IpAddress
_OspfNbrIpAddr_Object = MibTableColumn
ospfNbrIpAddr = _OspfNbrIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 1),
    _OspfNbrIpAddr_Type()
)
ospfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrIpAddr.setStatus("current")
_OspfNbrAddressLessIndex_Type = InterfaceIndexOrZero
_OspfNbrAddressLessIndex_Object = MibTableColumn
ospfNbrAddressLessIndex = _OspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 2),
    _OspfNbrAddressLessIndex_Type()
)
ospfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrAddressLessIndex.setStatus("current")


class _OspfNbrRtrId_Type(RouterID):
    """Custom type ospfNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_OspfNbrRtrId_Object = MibTableColumn
ospfNbrRtrId = _OspfNbrRtrId_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 3),
    _OspfNbrRtrId_Type()
)
ospfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrRtrId.setStatus("current")


class _OspfNbrOptions_Type(Integer32):
    """Custom type ospfNbrOptions based on Integer32"""
    defaultValue = 0


_OspfNbrOptions_Object = MibTableColumn
ospfNbrOptions = _OspfNbrOptions_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 4),
    _OspfNbrOptions_Type()
)
ospfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrOptions.setStatus("current")


class _OspfNbrPriority_Type(DesignatedRouterPriority):
    """Custom type ospfNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_OspfNbrPriority_Object = MibTableColumn
ospfNbrPriority = _OspfNbrPriority_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 5),
    _OspfNbrPriority_Type()
)
ospfNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNbrPriority.setStatus("current")


class _OspfNbrState_Type(Integer32):
    """Custom type ospfNbrState based on Integer32"""
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


_OspfNbrState_Type.__name__ = "Integer32"
_OspfNbrState_Object = MibTableColumn
ospfNbrState = _OspfNbrState_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 6),
    _OspfNbrState_Type()
)
ospfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrState.setStatus("current")
_OspfNbrEvents_Type = Counter32
_OspfNbrEvents_Object = MibTableColumn
ospfNbrEvents = _OspfNbrEvents_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 7),
    _OspfNbrEvents_Type()
)
ospfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrEvents.setStatus("current")
_OspfNbrLsRetransQLen_Type = Gauge32
_OspfNbrLsRetransQLen_Object = MibTableColumn
ospfNbrLsRetransQLen = _OspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 8),
    _OspfNbrLsRetransQLen_Type()
)
ospfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrLsRetransQLen.setStatus("current")
_OspfNbmaNbrStatus_Type = RowStatus
_OspfNbmaNbrStatus_Object = MibTableColumn
ospfNbmaNbrStatus = _OspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 9),
    _OspfNbmaNbrStatus_Type()
)
ospfNbmaNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNbmaNbrStatus.setStatus("current")


class _OspfNbmaNbrPermanence_Type(Integer32):
    """Custom type ospfNbmaNbrPermanence based on Integer32"""
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


_OspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_OspfNbmaNbrPermanence_Object = MibTableColumn
ospfNbmaNbrPermanence = _OspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 10),
    _OspfNbmaNbrPermanence_Type()
)
ospfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbmaNbrPermanence.setStatus("current")
_OspfNbrHelloSuppressed_Type = TruthValue
_OspfNbrHelloSuppressed_Object = MibTableColumn
ospfNbrHelloSuppressed = _OspfNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 11),
    _OspfNbrHelloSuppressed_Type()
)
ospfNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrHelloSuppressed.setStatus("current")


class _OspfNbrRestartHelperStatus_Type(Integer32):
    """Custom type ospfNbrRestartHelperStatus based on Integer32"""
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


_OspfNbrRestartHelperStatus_Type.__name__ = "Integer32"
_OspfNbrRestartHelperStatus_Object = MibTableColumn
ospfNbrRestartHelperStatus = _OspfNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 12),
    _OspfNbrRestartHelperStatus_Type()
)
ospfNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrRestartHelperStatus.setStatus("current")
_OspfNbrRestartHelperAge_Type = Unsigned32
_OspfNbrRestartHelperAge_Object = MibTableColumn
ospfNbrRestartHelperAge = _OspfNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 13),
    _OspfNbrRestartHelperAge_Type()
)
ospfNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfNbrRestartHelperAge.setUnits("seconds")


class _OspfNbrRestartHelperExitReason_Type(Integer32):
    """Custom type ospfNbrRestartHelperExitReason based on Integer32"""
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


_OspfNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_OspfNbrRestartHelperExitReason_Object = MibTableColumn
ospfNbrRestartHelperExitReason = _OspfNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 2, 1, 14, 10, 1, 14),
    _OspfNbrRestartHelperExitReason_Type()
)
ospfNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrRestartHelperExitReason.setStatus("current")
_OspfVirtNbrTable_Object = MibTable
ospfVirtNbrTable = _OspfVirtNbrTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 11)
)
if mibBuilder.loadTexts:
    ospfVirtNbrTable.setStatus("current")
_OspfVirtNbrEntry_Object = MibTableRow
ospfVirtNbrEntry = _OspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1)
)
ospfVirtNbrEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfVirtNbrArea"),
    (0, "OSPF-MIB", "ospfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    ospfVirtNbrEntry.setStatus("current")
_OspfVirtNbrArea_Type = AreaID
_OspfVirtNbrArea_Object = MibTableColumn
ospfVirtNbrArea = _OspfVirtNbrArea_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 1),
    _OspfVirtNbrArea_Type()
)
ospfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrArea.setStatus("current")
_OspfVirtNbrRtrId_Type = RouterID
_OspfVirtNbrRtrId_Object = MibTableColumn
ospfVirtNbrRtrId = _OspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 2),
    _OspfVirtNbrRtrId_Type()
)
ospfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrRtrId.setStatus("current")
_OspfVirtNbrIpAddr_Type = IpAddress
_OspfVirtNbrIpAddr_Object = MibTableColumn
ospfVirtNbrIpAddr = _OspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 3),
    _OspfVirtNbrIpAddr_Type()
)
ospfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrIpAddr.setStatus("current")
_OspfVirtNbrOptions_Type = Integer32
_OspfVirtNbrOptions_Object = MibTableColumn
ospfVirtNbrOptions = _OspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 4),
    _OspfVirtNbrOptions_Type()
)
ospfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrOptions.setStatus("current")


class _OspfVirtNbrState_Type(Integer32):
    """Custom type ospfVirtNbrState based on Integer32"""
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


_OspfVirtNbrState_Type.__name__ = "Integer32"
_OspfVirtNbrState_Object = MibTableColumn
ospfVirtNbrState = _OspfVirtNbrState_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 5),
    _OspfVirtNbrState_Type()
)
ospfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrState.setStatus("current")
_OspfVirtNbrEvents_Type = Counter32
_OspfVirtNbrEvents_Object = MibTableColumn
ospfVirtNbrEvents = _OspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 6),
    _OspfVirtNbrEvents_Type()
)
ospfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrEvents.setStatus("current")
_OspfVirtNbrLsRetransQLen_Type = Gauge32
_OspfVirtNbrLsRetransQLen_Object = MibTableColumn
ospfVirtNbrLsRetransQLen = _OspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 7),
    _OspfVirtNbrLsRetransQLen_Type()
)
ospfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrLsRetransQLen.setStatus("current")
_OspfVirtNbrHelloSuppressed_Type = TruthValue
_OspfVirtNbrHelloSuppressed_Object = MibTableColumn
ospfVirtNbrHelloSuppressed = _OspfVirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 8),
    _OspfVirtNbrHelloSuppressed_Type()
)
ospfVirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrHelloSuppressed.setStatus("current")


class _OspfVirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type ospfVirtNbrRestartHelperStatus based on Integer32"""
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


_OspfVirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_OspfVirtNbrRestartHelperStatus_Object = MibTableColumn
ospfVirtNbrRestartHelperStatus = _OspfVirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 9),
    _OspfVirtNbrRestartHelperStatus_Type()
)
ospfVirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrRestartHelperStatus.setStatus("current")
_OspfVirtNbrRestartHelperAge_Type = Unsigned32
_OspfVirtNbrRestartHelperAge_Object = MibTableColumn
ospfVirtNbrRestartHelperAge = _OspfVirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 10),
    _OspfVirtNbrRestartHelperAge_Type()
)
ospfVirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfVirtNbrRestartHelperAge.setUnits("seconds")


class _OspfVirtNbrRestartHelperExitReason_Type(Integer32):
    """Custom type ospfVirtNbrRestartHelperExitReason based on Integer32"""
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


_OspfVirtNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_OspfVirtNbrRestartHelperExitReason_Object = MibTableColumn
ospfVirtNbrRestartHelperExitReason = _OspfVirtNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 2, 1, 14, 11, 1, 11),
    _OspfVirtNbrRestartHelperExitReason_Type()
)
ospfVirtNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrRestartHelperExitReason.setStatus("current")
_OspfExtLsdbTable_Object = MibTable
ospfExtLsdbTable = _OspfExtLsdbTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 12)
)
if mibBuilder.loadTexts:
    ospfExtLsdbTable.setStatus("deprecated")
_OspfExtLsdbEntry_Object = MibTableRow
ospfExtLsdbEntry = _OspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 12, 1)
)
ospfExtLsdbEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfExtLsdbType"),
    (0, "OSPF-MIB", "ospfExtLsdbLsid"),
    (0, "OSPF-MIB", "ospfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfExtLsdbEntry.setStatus("deprecated")


class _OspfExtLsdbType_Type(Integer32):
    """Custom type ospfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_OspfExtLsdbType_Type.__name__ = "Integer32"
_OspfExtLsdbType_Object = MibTableColumn
ospfExtLsdbType = _OspfExtLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 14, 12, 1, 1),
    _OspfExtLsdbType_Type()
)
ospfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExtLsdbType.setStatus("deprecated")
_OspfExtLsdbLsid_Type = IpAddress
_OspfExtLsdbLsid_Object = MibTableColumn
ospfExtLsdbLsid = _OspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 2, 1, 14, 12, 1, 2),
    _OspfExtLsdbLsid_Type()
)
ospfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExtLsdbLsid.setStatus("deprecated")
_OspfExtLsdbRouterId_Type = RouterID
_OspfExtLsdbRouterId_Object = MibTableColumn
ospfExtLsdbRouterId = _OspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 2, 1, 14, 12, 1, 3),
    _OspfExtLsdbRouterId_Type()
)
ospfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExtLsdbRouterId.setStatus("deprecated")
_OspfExtLsdbSequence_Type = Integer32
_OspfExtLsdbSequence_Object = MibTableColumn
ospfExtLsdbSequence = _OspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 2, 1, 14, 12, 1, 4),
    _OspfExtLsdbSequence_Type()
)
ospfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExtLsdbSequence.setStatus("deprecated")
_OspfExtLsdbAge_Type = Integer32
_OspfExtLsdbAge_Object = MibTableColumn
ospfExtLsdbAge = _OspfExtLsdbAge_Object(
    (1, 3, 6, 1, 2, 1, 14, 12, 1, 5),
    _OspfExtLsdbAge_Type()
)
ospfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExtLsdbAge.setStatus("deprecated")
if mibBuilder.loadTexts:
    ospfExtLsdbAge.setUnits("seconds")
_OspfExtLsdbChecksum_Type = Integer32
_OspfExtLsdbChecksum_Object = MibTableColumn
ospfExtLsdbChecksum = _OspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 2, 1, 14, 12, 1, 6),
    _OspfExtLsdbChecksum_Type()
)
ospfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExtLsdbChecksum.setStatus("deprecated")


class _OspfExtLsdbAdvertisement_Type(OctetString):
    """Custom type ospfExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )


_OspfExtLsdbAdvertisement_Type.__name__ = "OctetString"
_OspfExtLsdbAdvertisement_Object = MibTableColumn
ospfExtLsdbAdvertisement = _OspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 14, 12, 1, 7),
    _OspfExtLsdbAdvertisement_Type()
)
ospfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExtLsdbAdvertisement.setStatus("deprecated")
_OspfRouteGroup_ObjectIdentity = ObjectIdentity
ospfRouteGroup = _OspfRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 13)
)
_OspfIntraArea_ObjectIdentity = ObjectIdentity
ospfIntraArea = _OspfIntraArea_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 13, 1)
)
_OspfInterArea_ObjectIdentity = ObjectIdentity
ospfInterArea = _OspfInterArea_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 13, 2)
)
_OspfExternalType1_ObjectIdentity = ObjectIdentity
ospfExternalType1 = _OspfExternalType1_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 13, 3)
)
_OspfExternalType2_ObjectIdentity = ObjectIdentity
ospfExternalType2 = _OspfExternalType2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 13, 4)
)
_OspfAreaAggregateTable_Object = MibTable
ospfAreaAggregateTable = _OspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 14)
)
if mibBuilder.loadTexts:
    ospfAreaAggregateTable.setStatus("current")
_OspfAreaAggregateEntry_Object = MibTableRow
ospfAreaAggregateEntry = _OspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 14, 1)
)
ospfAreaAggregateEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfAreaAggregateAreaID"),
    (0, "OSPF-MIB", "ospfAreaAggregateLsdbType"),
    (0, "OSPF-MIB", "ospfAreaAggregateNet"),
    (0, "OSPF-MIB", "ospfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    ospfAreaAggregateEntry.setStatus("current")
_OspfAreaAggregateAreaID_Type = AreaID
_OspfAreaAggregateAreaID_Object = MibTableColumn
ospfAreaAggregateAreaID = _OspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 2, 1, 14, 14, 1, 1),
    _OspfAreaAggregateAreaID_Type()
)
ospfAreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaAggregateAreaID.setStatus("current")


class _OspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type ospfAreaAggregateLsdbType based on Integer32"""
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


_OspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_OspfAreaAggregateLsdbType_Object = MibTableColumn
ospfAreaAggregateLsdbType = _OspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 14, 14, 1, 2),
    _OspfAreaAggregateLsdbType_Type()
)
ospfAreaAggregateLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaAggregateLsdbType.setStatus("current")
_OspfAreaAggregateNet_Type = IpAddress
_OspfAreaAggregateNet_Object = MibTableColumn
ospfAreaAggregateNet = _OspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 2, 1, 14, 14, 1, 3),
    _OspfAreaAggregateNet_Type()
)
ospfAreaAggregateNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaAggregateNet.setStatus("current")
_OspfAreaAggregateMask_Type = IpAddress
_OspfAreaAggregateMask_Object = MibTableColumn
ospfAreaAggregateMask = _OspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 2, 1, 14, 14, 1, 4),
    _OspfAreaAggregateMask_Type()
)
ospfAreaAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaAggregateMask.setStatus("current")
_OspfAreaAggregateStatus_Type = RowStatus
_OspfAreaAggregateStatus_Object = MibTableColumn
ospfAreaAggregateStatus = _OspfAreaAggregateStatus_Object(
    (1, 3, 6, 1, 2, 1, 14, 14, 1, 5),
    _OspfAreaAggregateStatus_Type()
)
ospfAreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfAreaAggregateStatus.setStatus("current")


class _OspfAreaAggregateEffect_Type(Integer32):
    """Custom type ospfAreaAggregateEffect based on Integer32"""
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


_OspfAreaAggregateEffect_Type.__name__ = "Integer32"
_OspfAreaAggregateEffect_Object = MibTableColumn
ospfAreaAggregateEffect = _OspfAreaAggregateEffect_Object(
    (1, 3, 6, 1, 2, 1, 14, 14, 1, 6),
    _OspfAreaAggregateEffect_Type()
)
ospfAreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfAreaAggregateEffect.setStatus("current")


class _OspfAreaAggregateExtRouteTag_Type(Unsigned32):
    """Custom type ospfAreaAggregateExtRouteTag based on Unsigned32"""
    defaultValue = 0


_OspfAreaAggregateExtRouteTag_Object = MibTableColumn
ospfAreaAggregateExtRouteTag = _OspfAreaAggregateExtRouteTag_Object(
    (1, 3, 6, 1, 2, 1, 14, 14, 1, 7),
    _OspfAreaAggregateExtRouteTag_Type()
)
ospfAreaAggregateExtRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfAreaAggregateExtRouteTag.setStatus("current")
_OspfConformance_ObjectIdentity = ObjectIdentity
ospfConformance = _OspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 15)
)
_OspfGroups_ObjectIdentity = ObjectIdentity
ospfGroups = _OspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 15, 1)
)
_OspfCompliances_ObjectIdentity = ObjectIdentity
ospfCompliances = _OspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 14, 15, 2)
)
_OspfLocalLsdbTable_Object = MibTable
ospfLocalLsdbTable = _OspfLocalLsdbTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 17)
)
if mibBuilder.loadTexts:
    ospfLocalLsdbTable.setStatus("current")
_OspfLocalLsdbEntry_Object = MibTableRow
ospfLocalLsdbEntry = _OspfLocalLsdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 17, 1)
)
ospfLocalLsdbEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfLocalLsdbIpAddress"),
    (0, "OSPF-MIB", "ospfLocalLsdbAddressLessIf"),
    (0, "OSPF-MIB", "ospfLocalLsdbType"),
    (0, "OSPF-MIB", "ospfLocalLsdbLsid"),
    (0, "OSPF-MIB", "ospfLocalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfLocalLsdbEntry.setStatus("current")
_OspfLocalLsdbIpAddress_Type = IpAddress
_OspfLocalLsdbIpAddress_Object = MibTableColumn
ospfLocalLsdbIpAddress = _OspfLocalLsdbIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 14, 17, 1, 1),
    _OspfLocalLsdbIpAddress_Type()
)
ospfLocalLsdbIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfLocalLsdbIpAddress.setStatus("current")
_OspfLocalLsdbAddressLessIf_Type = InterfaceIndexOrZero
_OspfLocalLsdbAddressLessIf_Object = MibTableColumn
ospfLocalLsdbAddressLessIf = _OspfLocalLsdbAddressLessIf_Object(
    (1, 3, 6, 1, 2, 1, 14, 17, 1, 2),
    _OspfLocalLsdbAddressLessIf_Type()
)
ospfLocalLsdbAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfLocalLsdbAddressLessIf.setStatus("current")


class _OspfLocalLsdbType_Type(Integer32):
    """Custom type ospfLocalLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            9
        )
    )
    namedValues = NamedValues(
        ("localOpaqueLink", 9)
    )


_OspfLocalLsdbType_Type.__name__ = "Integer32"
_OspfLocalLsdbType_Object = MibTableColumn
ospfLocalLsdbType = _OspfLocalLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 14, 17, 1, 3),
    _OspfLocalLsdbType_Type()
)
ospfLocalLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfLocalLsdbType.setStatus("current")
_OspfLocalLsdbLsid_Type = IpAddress
_OspfLocalLsdbLsid_Object = MibTableColumn
ospfLocalLsdbLsid = _OspfLocalLsdbLsid_Object(
    (1, 3, 6, 1, 2, 1, 14, 17, 1, 4),
    _OspfLocalLsdbLsid_Type()
)
ospfLocalLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfLocalLsdbLsid.setStatus("current")
_OspfLocalLsdbRouterId_Type = RouterID
_OspfLocalLsdbRouterId_Object = MibTableColumn
ospfLocalLsdbRouterId = _OspfLocalLsdbRouterId_Object(
    (1, 3, 6, 1, 2, 1, 14, 17, 1, 5),
    _OspfLocalLsdbRouterId_Type()
)
ospfLocalLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfLocalLsdbRouterId.setStatus("current")
_OspfLocalLsdbSequence_Type = Integer32
_OspfLocalLsdbSequence_Object = MibTableColumn
ospfLocalLsdbSequence = _OspfLocalLsdbSequence_Object(
    (1, 3, 6, 1, 2, 1, 14, 17, 1, 6),
    _OspfLocalLsdbSequence_Type()
)
ospfLocalLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLocalLsdbSequence.setStatus("current")
_OspfLocalLsdbAge_Type = Integer32
_OspfLocalLsdbAge_Object = MibTableColumn
ospfLocalLsdbAge = _OspfLocalLsdbAge_Object(
    (1, 3, 6, 1, 2, 1, 14, 17, 1, 7),
    _OspfLocalLsdbAge_Type()
)
ospfLocalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLocalLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfLocalLsdbAge.setUnits("seconds")
_OspfLocalLsdbChecksum_Type = Integer32
_OspfLocalLsdbChecksum_Object = MibTableColumn
ospfLocalLsdbChecksum = _OspfLocalLsdbChecksum_Object(
    (1, 3, 6, 1, 2, 1, 14, 17, 1, 8),
    _OspfLocalLsdbChecksum_Type()
)
ospfLocalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLocalLsdbChecksum.setStatus("current")


class _OspfLocalLsdbAdvertisement_Type(OctetString):
    """Custom type ospfLocalLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_OspfLocalLsdbAdvertisement_Type.__name__ = "OctetString"
_OspfLocalLsdbAdvertisement_Object = MibTableColumn
ospfLocalLsdbAdvertisement = _OspfLocalLsdbAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 14, 17, 1, 9),
    _OspfLocalLsdbAdvertisement_Type()
)
ospfLocalLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLocalLsdbAdvertisement.setStatus("current")
_OspfVirtLocalLsdbTable_Object = MibTable
ospfVirtLocalLsdbTable = _OspfVirtLocalLsdbTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 18)
)
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbTable.setStatus("current")
_OspfVirtLocalLsdbEntry_Object = MibTableRow
ospfVirtLocalLsdbEntry = _OspfVirtLocalLsdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 18, 1)
)
ospfVirtLocalLsdbEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfVirtLocalLsdbTransitArea"),
    (0, "OSPF-MIB", "ospfVirtLocalLsdbNeighbor"),
    (0, "OSPF-MIB", "ospfVirtLocalLsdbType"),
    (0, "OSPF-MIB", "ospfVirtLocalLsdbLsid"),
    (0, "OSPF-MIB", "ospfVirtLocalLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbEntry.setStatus("current")
_OspfVirtLocalLsdbTransitArea_Type = AreaID
_OspfVirtLocalLsdbTransitArea_Object = MibTableColumn
ospfVirtLocalLsdbTransitArea = _OspfVirtLocalLsdbTransitArea_Object(
    (1, 3, 6, 1, 2, 1, 14, 18, 1, 1),
    _OspfVirtLocalLsdbTransitArea_Type()
)
ospfVirtLocalLsdbTransitArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbTransitArea.setStatus("current")
_OspfVirtLocalLsdbNeighbor_Type = RouterID
_OspfVirtLocalLsdbNeighbor_Object = MibTableColumn
ospfVirtLocalLsdbNeighbor = _OspfVirtLocalLsdbNeighbor_Object(
    (1, 3, 6, 1, 2, 1, 14, 18, 1, 2),
    _OspfVirtLocalLsdbNeighbor_Type()
)
ospfVirtLocalLsdbNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbNeighbor.setStatus("current")


class _OspfVirtLocalLsdbType_Type(Integer32):
    """Custom type ospfVirtLocalLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            9
        )
    )
    namedValues = NamedValues(
        ("localOpaqueLink", 9)
    )


_OspfVirtLocalLsdbType_Type.__name__ = "Integer32"
_OspfVirtLocalLsdbType_Object = MibTableColumn
ospfVirtLocalLsdbType = _OspfVirtLocalLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 14, 18, 1, 3),
    _OspfVirtLocalLsdbType_Type()
)
ospfVirtLocalLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbType.setStatus("current")
_OspfVirtLocalLsdbLsid_Type = IpAddress
_OspfVirtLocalLsdbLsid_Object = MibTableColumn
ospfVirtLocalLsdbLsid = _OspfVirtLocalLsdbLsid_Object(
    (1, 3, 6, 1, 2, 1, 14, 18, 1, 4),
    _OspfVirtLocalLsdbLsid_Type()
)
ospfVirtLocalLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbLsid.setStatus("current")
_OspfVirtLocalLsdbRouterId_Type = RouterID
_OspfVirtLocalLsdbRouterId_Object = MibTableColumn
ospfVirtLocalLsdbRouterId = _OspfVirtLocalLsdbRouterId_Object(
    (1, 3, 6, 1, 2, 1, 14, 18, 1, 5),
    _OspfVirtLocalLsdbRouterId_Type()
)
ospfVirtLocalLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbRouterId.setStatus("current")
_OspfVirtLocalLsdbSequence_Type = Integer32
_OspfVirtLocalLsdbSequence_Object = MibTableColumn
ospfVirtLocalLsdbSequence = _OspfVirtLocalLsdbSequence_Object(
    (1, 3, 6, 1, 2, 1, 14, 18, 1, 6),
    _OspfVirtLocalLsdbSequence_Type()
)
ospfVirtLocalLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbSequence.setStatus("current")
_OspfVirtLocalLsdbAge_Type = Integer32
_OspfVirtLocalLsdbAge_Object = MibTableColumn
ospfVirtLocalLsdbAge = _OspfVirtLocalLsdbAge_Object(
    (1, 3, 6, 1, 2, 1, 14, 18, 1, 7),
    _OspfVirtLocalLsdbAge_Type()
)
ospfVirtLocalLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbAge.setUnits("seconds")
_OspfVirtLocalLsdbChecksum_Type = Integer32
_OspfVirtLocalLsdbChecksum_Object = MibTableColumn
ospfVirtLocalLsdbChecksum = _OspfVirtLocalLsdbChecksum_Object(
    (1, 3, 6, 1, 2, 1, 14, 18, 1, 8),
    _OspfVirtLocalLsdbChecksum_Type()
)
ospfVirtLocalLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbChecksum.setStatus("current")


class _OspfVirtLocalLsdbAdvertisement_Type(OctetString):
    """Custom type ospfVirtLocalLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_OspfVirtLocalLsdbAdvertisement_Type.__name__ = "OctetString"
_OspfVirtLocalLsdbAdvertisement_Object = MibTableColumn
ospfVirtLocalLsdbAdvertisement = _OspfVirtLocalLsdbAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 14, 18, 1, 9),
    _OspfVirtLocalLsdbAdvertisement_Type()
)
ospfVirtLocalLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbAdvertisement.setStatus("current")
_OspfAsLsdbTable_Object = MibTable
ospfAsLsdbTable = _OspfAsLsdbTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 19)
)
if mibBuilder.loadTexts:
    ospfAsLsdbTable.setStatus("current")
_OspfAsLsdbEntry_Object = MibTableRow
ospfAsLsdbEntry = _OspfAsLsdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 19, 1)
)
ospfAsLsdbEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfAsLsdbType"),
    (0, "OSPF-MIB", "ospfAsLsdbLsid"),
    (0, "OSPF-MIB", "ospfAsLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfAsLsdbEntry.setStatus("current")


class _OspfAsLsdbType_Type(Integer32):
    """Custom type ospfAsLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              11)
        )
    )
    namedValues = NamedValues(
        *(("asExternalLink", 5),
          ("asOpaqueLink", 11))
    )


_OspfAsLsdbType_Type.__name__ = "Integer32"
_OspfAsLsdbType_Object = MibTableColumn
ospfAsLsdbType = _OspfAsLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 14, 19, 1, 1),
    _OspfAsLsdbType_Type()
)
ospfAsLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfAsLsdbType.setStatus("current")
_OspfAsLsdbLsid_Type = IpAddress
_OspfAsLsdbLsid_Object = MibTableColumn
ospfAsLsdbLsid = _OspfAsLsdbLsid_Object(
    (1, 3, 6, 1, 2, 1, 14, 19, 1, 2),
    _OspfAsLsdbLsid_Type()
)
ospfAsLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfAsLsdbLsid.setStatus("current")
_OspfAsLsdbRouterId_Type = RouterID
_OspfAsLsdbRouterId_Object = MibTableColumn
ospfAsLsdbRouterId = _OspfAsLsdbRouterId_Object(
    (1, 3, 6, 1, 2, 1, 14, 19, 1, 3),
    _OspfAsLsdbRouterId_Type()
)
ospfAsLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfAsLsdbRouterId.setStatus("current")
_OspfAsLsdbSequence_Type = Integer32
_OspfAsLsdbSequence_Object = MibTableColumn
ospfAsLsdbSequence = _OspfAsLsdbSequence_Object(
    (1, 3, 6, 1, 2, 1, 14, 19, 1, 4),
    _OspfAsLsdbSequence_Type()
)
ospfAsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAsLsdbSequence.setStatus("current")
_OspfAsLsdbAge_Type = Integer32
_OspfAsLsdbAge_Object = MibTableColumn
ospfAsLsdbAge = _OspfAsLsdbAge_Object(
    (1, 3, 6, 1, 2, 1, 14, 19, 1, 5),
    _OspfAsLsdbAge_Type()
)
ospfAsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAsLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    ospfAsLsdbAge.setUnits("seconds")
_OspfAsLsdbChecksum_Type = Integer32
_OspfAsLsdbChecksum_Object = MibTableColumn
ospfAsLsdbChecksum = _OspfAsLsdbChecksum_Object(
    (1, 3, 6, 1, 2, 1, 14, 19, 1, 6),
    _OspfAsLsdbChecksum_Type()
)
ospfAsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAsLsdbChecksum.setStatus("current")


class _OspfAsLsdbAdvertisement_Type(OctetString):
    """Custom type ospfAsLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_OspfAsLsdbAdvertisement_Type.__name__ = "OctetString"
_OspfAsLsdbAdvertisement_Object = MibTableColumn
ospfAsLsdbAdvertisement = _OspfAsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 14, 19, 1, 7),
    _OspfAsLsdbAdvertisement_Type()
)
ospfAsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAsLsdbAdvertisement.setStatus("current")
_OspfAreaLsaCountTable_Object = MibTable
ospfAreaLsaCountTable = _OspfAreaLsaCountTable_Object(
    (1, 3, 6, 1, 2, 1, 14, 20)
)
if mibBuilder.loadTexts:
    ospfAreaLsaCountTable.setStatus("current")
_OspfAreaLsaCountEntry_Object = MibTableRow
ospfAreaLsaCountEntry = _OspfAreaLsaCountEntry_Object(
    (1, 3, 6, 1, 2, 1, 14, 20, 1)
)
ospfAreaLsaCountEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfAreaLsaCountAreaId"),
    (0, "OSPF-MIB", "ospfAreaLsaCountLsaType"),
)
if mibBuilder.loadTexts:
    ospfAreaLsaCountEntry.setStatus("current")
_OspfAreaLsaCountAreaId_Type = AreaID
_OspfAreaLsaCountAreaId_Object = MibTableColumn
ospfAreaLsaCountAreaId = _OspfAreaLsaCountAreaId_Object(
    (1, 3, 6, 1, 2, 1, 14, 20, 1, 1),
    _OspfAreaLsaCountAreaId_Type()
)
ospfAreaLsaCountAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfAreaLsaCountAreaId.setStatus("current")


class _OspfAreaLsaCountLsaType_Type(Integer32):
    """Custom type ospfAreaLsaCountLsaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              10)
        )
    )
    namedValues = NamedValues(
        *(("areaOpaqueLink", 10),
          ("asSummaryLink", 4),
          ("multicastLink", 6),
          ("networkLink", 2),
          ("nssaExternalLink", 7),
          ("routerLink", 1),
          ("summaryLink", 3))
    )


_OspfAreaLsaCountLsaType_Type.__name__ = "Integer32"
_OspfAreaLsaCountLsaType_Object = MibTableColumn
ospfAreaLsaCountLsaType = _OspfAreaLsaCountLsaType_Object(
    (1, 3, 6, 1, 2, 1, 14, 20, 1, 2),
    _OspfAreaLsaCountLsaType_Type()
)
ospfAreaLsaCountLsaType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfAreaLsaCountLsaType.setStatus("current")
_OspfAreaLsaCountNumber_Type = Gauge32
_OspfAreaLsaCountNumber_Object = MibTableColumn
ospfAreaLsaCountNumber = _OspfAreaLsaCountNumber_Object(
    (1, 3, 6, 1, 2, 1, 14, 20, 1, 3),
    _OspfAreaLsaCountNumber_Type()
)
ospfAreaLsaCountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaLsaCountNumber.setStatus("current")

# Managed Objects groups

ospfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 1)
)
ospfBasicGroup.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfAdminStat"),
        ("OSPF-MIB", "ospfVersionNumber"),
        ("OSPF-MIB", "ospfAreaBdrRtrStatus"),
        ("OSPF-MIB", "ospfASBdrRtrStatus"),
        ("OSPF-MIB", "ospfExternLsaCount"),
        ("OSPF-MIB", "ospfExternLsaCksumSum"),
        ("OSPF-MIB", "ospfTOSSupport"),
        ("OSPF-MIB", "ospfOriginateNewLsas"),
        ("OSPF-MIB", "ospfRxNewLsas"),
        ("OSPF-MIB", "ospfExtLsdbLimit"),
        ("OSPF-MIB", "ospfMulticastExtensions"),
        ("OSPF-MIB", "ospfExitOverflowInterval"),
        ("OSPF-MIB", "ospfDemandExtensions"))
)
if mibBuilder.loadTexts:
    ospfBasicGroup.setStatus("deprecated")

ospfAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 2)
)
ospfAreaGroup.setObjects(
      *(("OSPF-MIB", "ospfAreaId"),
        ("OSPF-MIB", "ospfImportAsExtern"),
        ("OSPF-MIB", "ospfSpfRuns"),
        ("OSPF-MIB", "ospfAreaBdrRtrCount"),
        ("OSPF-MIB", "ospfAsBdrRtrCount"),
        ("OSPF-MIB", "ospfAreaLsaCount"),
        ("OSPF-MIB", "ospfAreaLsaCksumSum"),
        ("OSPF-MIB", "ospfAreaSummary"),
        ("OSPF-MIB", "ospfAreaStatus"))
)
if mibBuilder.loadTexts:
    ospfAreaGroup.setStatus("deprecated")

ospfStubAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 3)
)
ospfStubAreaGroup.setObjects(
      *(("OSPF-MIB", "ospfStubAreaId"),
        ("OSPF-MIB", "ospfStubTOS"),
        ("OSPF-MIB", "ospfStubMetric"),
        ("OSPF-MIB", "ospfStubStatus"),
        ("OSPF-MIB", "ospfStubMetricType"))
)
if mibBuilder.loadTexts:
    ospfStubAreaGroup.setStatus("current")

ospfLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 4)
)
ospfLsdbGroup.setObjects(
      *(("OSPF-MIB", "ospfLsdbAreaId"),
        ("OSPF-MIB", "ospfLsdbType"),
        ("OSPF-MIB", "ospfLsdbLsid"),
        ("OSPF-MIB", "ospfLsdbRouterId"),
        ("OSPF-MIB", "ospfLsdbSequence"),
        ("OSPF-MIB", "ospfLsdbAge"),
        ("OSPF-MIB", "ospfLsdbChecksum"),
        ("OSPF-MIB", "ospfLsdbAdvertisement"))
)
if mibBuilder.loadTexts:
    ospfLsdbGroup.setStatus("current")

ospfAreaRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 5)
)
ospfAreaRangeGroup.setObjects(
      *(("OSPF-MIB", "ospfAreaRangeAreaId"),
        ("OSPF-MIB", "ospfAreaRangeNet"),
        ("OSPF-MIB", "ospfAreaRangeMask"),
        ("OSPF-MIB", "ospfAreaRangeStatus"),
        ("OSPF-MIB", "ospfAreaRangeEffect"))
)
if mibBuilder.loadTexts:
    ospfAreaRangeGroup.setStatus("obsolete")

ospfHostGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 6)
)
ospfHostGroup.setObjects(
      *(("OSPF-MIB", "ospfHostIpAddress"),
        ("OSPF-MIB", "ospfHostTOS"),
        ("OSPF-MIB", "ospfHostMetric"),
        ("OSPF-MIB", "ospfHostStatus"),
        ("OSPF-MIB", "ospfHostAreaID"))
)
if mibBuilder.loadTexts:
    ospfHostGroup.setStatus("deprecated")

ospfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 7)
)
ospfIfGroup.setObjects(
      *(("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-MIB", "ospfIfAreaId"),
        ("OSPF-MIB", "ospfIfType"),
        ("OSPF-MIB", "ospfIfAdminStat"),
        ("OSPF-MIB", "ospfIfRtrPriority"),
        ("OSPF-MIB", "ospfIfTransitDelay"),
        ("OSPF-MIB", "ospfIfRetransInterval"),
        ("OSPF-MIB", "ospfIfHelloInterval"),
        ("OSPF-MIB", "ospfIfRtrDeadInterval"),
        ("OSPF-MIB", "ospfIfPollInterval"),
        ("OSPF-MIB", "ospfIfState"),
        ("OSPF-MIB", "ospfIfDesignatedRouter"),
        ("OSPF-MIB", "ospfIfBackupDesignatedRouter"),
        ("OSPF-MIB", "ospfIfEvents"),
        ("OSPF-MIB", "ospfIfAuthType"),
        ("OSPF-MIB", "ospfIfAuthKey"),
        ("OSPF-MIB", "ospfIfStatus"),
        ("OSPF-MIB", "ospfIfMulticastForwarding"),
        ("OSPF-MIB", "ospfIfDemand"))
)
if mibBuilder.loadTexts:
    ospfIfGroup.setStatus("deprecated")

ospfIfMetricGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 8)
)
ospfIfMetricGroup.setObjects(
      *(("OSPF-MIB", "ospfIfMetricIpAddress"),
        ("OSPF-MIB", "ospfIfMetricAddressLessIf"),
        ("OSPF-MIB", "ospfIfMetricTOS"),
        ("OSPF-MIB", "ospfIfMetricValue"),
        ("OSPF-MIB", "ospfIfMetricStatus"))
)
if mibBuilder.loadTexts:
    ospfIfMetricGroup.setStatus("current")

ospfVirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 9)
)
ospfVirtIfGroup.setObjects(
      *(("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-MIB", "ospfVirtIfTransitDelay"),
        ("OSPF-MIB", "ospfVirtIfRetransInterval"),
        ("OSPF-MIB", "ospfVirtIfHelloInterval"),
        ("OSPF-MIB", "ospfVirtIfRtrDeadInterval"),
        ("OSPF-MIB", "ospfVirtIfState"),
        ("OSPF-MIB", "ospfVirtIfEvents"),
        ("OSPF-MIB", "ospfVirtIfAuthType"),
        ("OSPF-MIB", "ospfVirtIfAuthKey"),
        ("OSPF-MIB", "ospfVirtIfStatus"))
)
if mibBuilder.loadTexts:
    ospfVirtIfGroup.setStatus("deprecated")

ospfNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 10)
)
ospfNbrGroup.setObjects(
      *(("OSPF-MIB", "ospfNbrIpAddr"),
        ("OSPF-MIB", "ospfNbrAddressLessIndex"),
        ("OSPF-MIB", "ospfNbrRtrId"),
        ("OSPF-MIB", "ospfNbrOptions"),
        ("OSPF-MIB", "ospfNbrPriority"),
        ("OSPF-MIB", "ospfNbrState"),
        ("OSPF-MIB", "ospfNbrEvents"),
        ("OSPF-MIB", "ospfNbrLsRetransQLen"),
        ("OSPF-MIB", "ospfNbmaNbrStatus"),
        ("OSPF-MIB", "ospfNbmaNbrPermanence"),
        ("OSPF-MIB", "ospfNbrHelloSuppressed"))
)
if mibBuilder.loadTexts:
    ospfNbrGroup.setStatus("deprecated")

ospfVirtNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 11)
)
ospfVirtNbrGroup.setObjects(
      *(("OSPF-MIB", "ospfVirtNbrArea"),
        ("OSPF-MIB", "ospfVirtNbrRtrId"),
        ("OSPF-MIB", "ospfVirtNbrIpAddr"),
        ("OSPF-MIB", "ospfVirtNbrOptions"),
        ("OSPF-MIB", "ospfVirtNbrState"),
        ("OSPF-MIB", "ospfVirtNbrEvents"),
        ("OSPF-MIB", "ospfVirtNbrLsRetransQLen"),
        ("OSPF-MIB", "ospfVirtNbrHelloSuppressed"))
)
if mibBuilder.loadTexts:
    ospfVirtNbrGroup.setStatus("deprecated")

ospfExtLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 12)
)
ospfExtLsdbGroup.setObjects(
      *(("OSPF-MIB", "ospfExtLsdbType"),
        ("OSPF-MIB", "ospfExtLsdbLsid"),
        ("OSPF-MIB", "ospfExtLsdbRouterId"),
        ("OSPF-MIB", "ospfExtLsdbSequence"),
        ("OSPF-MIB", "ospfExtLsdbAge"),
        ("OSPF-MIB", "ospfExtLsdbChecksum"),
        ("OSPF-MIB", "ospfExtLsdbAdvertisement"))
)
if mibBuilder.loadTexts:
    ospfExtLsdbGroup.setStatus("deprecated")

ospfAreaAggregateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 13)
)
ospfAreaAggregateGroup.setObjects(
      *(("OSPF-MIB", "ospfAreaAggregateAreaID"),
        ("OSPF-MIB", "ospfAreaAggregateLsdbType"),
        ("OSPF-MIB", "ospfAreaAggregateNet"),
        ("OSPF-MIB", "ospfAreaAggregateMask"),
        ("OSPF-MIB", "ospfAreaAggregateStatus"),
        ("OSPF-MIB", "ospfAreaAggregateEffect"))
)
if mibBuilder.loadTexts:
    ospfAreaAggregateGroup.setStatus("deprecated")

ospfLocalLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 14)
)
ospfLocalLsdbGroup.setObjects(
      *(("OSPF-MIB", "ospfLocalLsdbSequence"),
        ("OSPF-MIB", "ospfLocalLsdbAge"),
        ("OSPF-MIB", "ospfLocalLsdbChecksum"),
        ("OSPF-MIB", "ospfLocalLsdbAdvertisement"))
)
if mibBuilder.loadTexts:
    ospfLocalLsdbGroup.setStatus("current")

ospfVirtLocalLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 15)
)
ospfVirtLocalLsdbGroup.setObjects(
      *(("OSPF-MIB", "ospfVirtLocalLsdbSequence"),
        ("OSPF-MIB", "ospfVirtLocalLsdbAge"),
        ("OSPF-MIB", "ospfVirtLocalLsdbChecksum"),
        ("OSPF-MIB", "ospfVirtLocalLsdbAdvertisement"))
)
if mibBuilder.loadTexts:
    ospfVirtLocalLsdbGroup.setStatus("current")

ospfAsLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 16)
)
ospfAsLsdbGroup.setObjects(
      *(("OSPF-MIB", "ospfAsLsdbSequence"),
        ("OSPF-MIB", "ospfAsLsdbAge"),
        ("OSPF-MIB", "ospfAsLsdbChecksum"),
        ("OSPF-MIB", "ospfAsLsdbAdvertisement"))
)
if mibBuilder.loadTexts:
    ospfAsLsdbGroup.setStatus("current")

ospfBasicGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 17)
)
ospfBasicGroup2.setObjects(
      *(("OSPF-MIB", "ospfRouterId"),
        ("OSPF-MIB", "ospfAdminStat"),
        ("OSPF-MIB", "ospfVersionNumber"),
        ("OSPF-MIB", "ospfAreaBdrRtrStatus"),
        ("OSPF-MIB", "ospfASBdrRtrStatus"),
        ("OSPF-MIB", "ospfExternLsaCount"),
        ("OSPF-MIB", "ospfExternLsaCksumSum"),
        ("OSPF-MIB", "ospfTOSSupport"),
        ("OSPF-MIB", "ospfOriginateNewLsas"),
        ("OSPF-MIB", "ospfRxNewLsas"),
        ("OSPF-MIB", "ospfExtLsdbLimit"),
        ("OSPF-MIB", "ospfMulticastExtensions"),
        ("OSPF-MIB", "ospfExitOverflowInterval"),
        ("OSPF-MIB", "ospfDemandExtensions"),
        ("OSPF-MIB", "ospfRFC1583Compatibility"),
        ("OSPF-MIB", "ospfOpaqueLsaSupport"),
        ("OSPF-MIB", "ospfReferenceBandwidth"),
        ("OSPF-MIB", "ospfRestartSupport"),
        ("OSPF-MIB", "ospfRestartInterval"),
        ("OSPF-MIB", "ospfRestartStrictLsaChecking"),
        ("OSPF-MIB", "ospfRestartStatus"),
        ("OSPF-MIB", "ospfRestartAge"),
        ("OSPF-MIB", "ospfRestartExitReason"),
        ("OSPF-MIB", "ospfAsLsaCount"),
        ("OSPF-MIB", "ospfAsLsaCksumSum"),
        ("OSPF-MIB", "ospfStubRouterSupport"),
        ("OSPF-MIB", "ospfStubRouterAdvertisement"),
        ("OSPF-MIB", "ospfDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    ospfBasicGroup2.setStatus("current")

ospfAreaGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 18)
)
ospfAreaGroup2.setObjects(
      *(("OSPF-MIB", "ospfAreaId"),
        ("OSPF-MIB", "ospfImportAsExtern"),
        ("OSPF-MIB", "ospfSpfRuns"),
        ("OSPF-MIB", "ospfAreaBdrRtrCount"),
        ("OSPF-MIB", "ospfAsBdrRtrCount"),
        ("OSPF-MIB", "ospfAreaLsaCount"),
        ("OSPF-MIB", "ospfAreaLsaCksumSum"),
        ("OSPF-MIB", "ospfAreaSummary"),
        ("OSPF-MIB", "ospfAreaStatus"),
        ("OSPF-MIB", "ospfAreaNssaTranslatorRole"),
        ("OSPF-MIB", "ospfAreaNssaTranslatorState"),
        ("OSPF-MIB", "ospfAreaNssaTranslatorStabilityInterval"),
        ("OSPF-MIB", "ospfAreaNssaTranslatorEvents"))
)
if mibBuilder.loadTexts:
    ospfAreaGroup2.setStatus("current")

ospfIfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 19)
)
ospfIfGroup2.setObjects(
      *(("OSPF-MIB", "ospfIfIpAddress"),
        ("OSPF-MIB", "ospfAddressLessIf"),
        ("OSPF-MIB", "ospfIfAreaId"),
        ("OSPF-MIB", "ospfIfType"),
        ("OSPF-MIB", "ospfIfAdminStat"),
        ("OSPF-MIB", "ospfIfRtrPriority"),
        ("OSPF-MIB", "ospfIfTransitDelay"),
        ("OSPF-MIB", "ospfIfRetransInterval"),
        ("OSPF-MIB", "ospfIfHelloInterval"),
        ("OSPF-MIB", "ospfIfRtrDeadInterval"),
        ("OSPF-MIB", "ospfIfPollInterval"),
        ("OSPF-MIB", "ospfIfState"),
        ("OSPF-MIB", "ospfIfDesignatedRouter"),
        ("OSPF-MIB", "ospfIfBackupDesignatedRouter"),
        ("OSPF-MIB", "ospfIfEvents"),
        ("OSPF-MIB", "ospfIfAuthType"),
        ("OSPF-MIB", "ospfIfAuthKey"),
        ("OSPF-MIB", "ospfIfStatus"),
        ("OSPF-MIB", "ospfIfMulticastForwarding"),
        ("OSPF-MIB", "ospfIfDemand"),
        ("OSPF-MIB", "ospfIfLsaCount"),
        ("OSPF-MIB", "ospfIfLsaCksumSum"))
)
if mibBuilder.loadTexts:
    ospfIfGroup2.setStatus("current")

ospfVirtIfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 20)
)
ospfVirtIfGroup2.setObjects(
      *(("OSPF-MIB", "ospfVirtIfAreaId"),
        ("OSPF-MIB", "ospfVirtIfNeighbor"),
        ("OSPF-MIB", "ospfVirtIfTransitDelay"),
        ("OSPF-MIB", "ospfVirtIfRetransInterval"),
        ("OSPF-MIB", "ospfVirtIfHelloInterval"),
        ("OSPF-MIB", "ospfVirtIfRtrDeadInterval"),
        ("OSPF-MIB", "ospfVirtIfState"),
        ("OSPF-MIB", "ospfVirtIfEvents"),
        ("OSPF-MIB", "ospfVirtIfAuthType"),
        ("OSPF-MIB", "ospfVirtIfAuthKey"),
        ("OSPF-MIB", "ospfVirtIfStatus"),
        ("OSPF-MIB", "ospfVirtIfLsaCount"),
        ("OSPF-MIB", "ospfVirtIfLsaCksumSum"),
        ("OSPF-MIB", "ospfIfDesignatedRouterId"),
        ("OSPF-MIB", "ospfIfBackupDesignatedRouterId"))
)
if mibBuilder.loadTexts:
    ospfVirtIfGroup2.setStatus("current")

ospfNbrGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 21)
)
ospfNbrGroup2.setObjects(
      *(("OSPF-MIB", "ospfNbrIpAddr"),
        ("OSPF-MIB", "ospfNbrAddressLessIndex"),
        ("OSPF-MIB", "ospfNbrRtrId"),
        ("OSPF-MIB", "ospfNbrOptions"),
        ("OSPF-MIB", "ospfNbrPriority"),
        ("OSPF-MIB", "ospfNbrState"),
        ("OSPF-MIB", "ospfNbrEvents"),
        ("OSPF-MIB", "ospfNbrLsRetransQLen"),
        ("OSPF-MIB", "ospfNbmaNbrStatus"),
        ("OSPF-MIB", "ospfNbmaNbrPermanence"),
        ("OSPF-MIB", "ospfNbrHelloSuppressed"),
        ("OSPF-MIB", "ospfNbrRestartHelperStatus"),
        ("OSPF-MIB", "ospfNbrRestartHelperAge"),
        ("OSPF-MIB", "ospfNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    ospfNbrGroup2.setStatus("current")

ospfVirtNbrGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 22)
)
ospfVirtNbrGroup2.setObjects(
      *(("OSPF-MIB", "ospfVirtNbrArea"),
        ("OSPF-MIB", "ospfVirtNbrRtrId"),
        ("OSPF-MIB", "ospfVirtNbrIpAddr"),
        ("OSPF-MIB", "ospfVirtNbrOptions"),
        ("OSPF-MIB", "ospfVirtNbrState"),
        ("OSPF-MIB", "ospfVirtNbrEvents"),
        ("OSPF-MIB", "ospfVirtNbrLsRetransQLen"),
        ("OSPF-MIB", "ospfVirtNbrHelloSuppressed"),
        ("OSPF-MIB", "ospfVirtNbrRestartHelperStatus"),
        ("OSPF-MIB", "ospfVirtNbrRestartHelperAge"),
        ("OSPF-MIB", "ospfVirtNbrRestartHelperExitReason"))
)
if mibBuilder.loadTexts:
    ospfVirtNbrGroup2.setStatus("current")

ospfAreaAggregateGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 23)
)
ospfAreaAggregateGroup2.setObjects(
      *(("OSPF-MIB", "ospfAreaAggregateAreaID"),
        ("OSPF-MIB", "ospfAreaAggregateLsdbType"),
        ("OSPF-MIB", "ospfAreaAggregateNet"),
        ("OSPF-MIB", "ospfAreaAggregateMask"),
        ("OSPF-MIB", "ospfAreaAggregateStatus"),
        ("OSPF-MIB", "ospfAreaAggregateEffect"),
        ("OSPF-MIB", "ospfAreaAggregateExtRouteTag"))
)
if mibBuilder.loadTexts:
    ospfAreaAggregateGroup2.setStatus("current")

ospfAreaLsaCountGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 24)
)
ospfAreaLsaCountGroup.setObjects(
    ("OSPF-MIB", "ospfAreaLsaCountNumber")
)
if mibBuilder.loadTexts:
    ospfAreaLsaCountGroup.setStatus("current")

ospfHostGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 25)
)
ospfHostGroup2.setObjects(
      *(("OSPF-MIB", "ospfHostIpAddress"),
        ("OSPF-MIB", "ospfHostTOS"),
        ("OSPF-MIB", "ospfHostMetric"),
        ("OSPF-MIB", "ospfHostStatus"),
        ("OSPF-MIB", "ospfHostCfgAreaID"))
)
if mibBuilder.loadTexts:
    ospfHostGroup2.setStatus("current")

ospfObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 14, 15, 1, 26)
)
ospfObsoleteGroup.setObjects(
    ("OSPF-MIB", "ospfAuthType")
)
if mibBuilder.loadTexts:
    ospfObsoleteGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ospfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 14, 15, 2, 1)
)
if mibBuilder.loadTexts:
    ospfCompliance.setStatus(
        "deprecated"
    )

ospfCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 14, 15, 2, 2)
)
if mibBuilder.loadTexts:
    ospfCompliance2.setStatus(
        "current"
    )

ospfComplianceObsolete = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 14, 15, 2, 3)
)
if mibBuilder.loadTexts:
    ospfComplianceObsolete.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OSPF-MIB",
    **{"AreaID": AreaID,
       "RouterID": RouterID,
       "Metric": Metric,
       "BigMetric": BigMetric,
       "Status": Status,
       "PositiveInteger": PositiveInteger,
       "HelloRange": HelloRange,
       "UpToMaxAge": UpToMaxAge,
       "DesignatedRouterPriority": DesignatedRouterPriority,
       "TOSType": TOSType,
       "OspfAuthenticationType": OspfAuthenticationType,
       "ospf": ospf,
       "ospfGeneralGroup": ospfGeneralGroup,
       "ospfRouterId": ospfRouterId,
       "ospfAdminStat": ospfAdminStat,
       "ospfVersionNumber": ospfVersionNumber,
       "ospfAreaBdrRtrStatus": ospfAreaBdrRtrStatus,
       "ospfASBdrRtrStatus": ospfASBdrRtrStatus,
       "ospfExternLsaCount": ospfExternLsaCount,
       "ospfExternLsaCksumSum": ospfExternLsaCksumSum,
       "ospfTOSSupport": ospfTOSSupport,
       "ospfOriginateNewLsas": ospfOriginateNewLsas,
       "ospfRxNewLsas": ospfRxNewLsas,
       "ospfExtLsdbLimit": ospfExtLsdbLimit,
       "ospfMulticastExtensions": ospfMulticastExtensions,
       "ospfExitOverflowInterval": ospfExitOverflowInterval,
       "ospfDemandExtensions": ospfDemandExtensions,
       "ospfRFC1583Compatibility": ospfRFC1583Compatibility,
       "ospfOpaqueLsaSupport": ospfOpaqueLsaSupport,
       "ospfReferenceBandwidth": ospfReferenceBandwidth,
       "ospfRestartSupport": ospfRestartSupport,
       "ospfRestartInterval": ospfRestartInterval,
       "ospfRestartStrictLsaChecking": ospfRestartStrictLsaChecking,
       "ospfRestartStatus": ospfRestartStatus,
       "ospfRestartAge": ospfRestartAge,
       "ospfRestartExitReason": ospfRestartExitReason,
       "ospfAsLsaCount": ospfAsLsaCount,
       "ospfAsLsaCksumSum": ospfAsLsaCksumSum,
       "ospfStubRouterSupport": ospfStubRouterSupport,
       "ospfStubRouterAdvertisement": ospfStubRouterAdvertisement,
       "ospfDiscontinuityTime": ospfDiscontinuityTime,
       "ospfAreaTable": ospfAreaTable,
       "ospfAreaEntry": ospfAreaEntry,
       "ospfAreaId": ospfAreaId,
       "ospfAuthType": ospfAuthType,
       "ospfImportAsExtern": ospfImportAsExtern,
       "ospfSpfRuns": ospfSpfRuns,
       "ospfAreaBdrRtrCount": ospfAreaBdrRtrCount,
       "ospfAsBdrRtrCount": ospfAsBdrRtrCount,
       "ospfAreaLsaCount": ospfAreaLsaCount,
       "ospfAreaLsaCksumSum": ospfAreaLsaCksumSum,
       "ospfAreaSummary": ospfAreaSummary,
       "ospfAreaStatus": ospfAreaStatus,
       "ospfAreaNssaTranslatorRole": ospfAreaNssaTranslatorRole,
       "ospfAreaNssaTranslatorState": ospfAreaNssaTranslatorState,
       "ospfAreaNssaTranslatorStabilityInterval": ospfAreaNssaTranslatorStabilityInterval,
       "ospfAreaNssaTranslatorEvents": ospfAreaNssaTranslatorEvents,
       "ospfStubAreaTable": ospfStubAreaTable,
       "ospfStubAreaEntry": ospfStubAreaEntry,
       "ospfStubAreaId": ospfStubAreaId,
       "ospfStubTOS": ospfStubTOS,
       "ospfStubMetric": ospfStubMetric,
       "ospfStubStatus": ospfStubStatus,
       "ospfStubMetricType": ospfStubMetricType,
       "ospfLsdbTable": ospfLsdbTable,
       "ospfLsdbEntry": ospfLsdbEntry,
       "ospfLsdbAreaId": ospfLsdbAreaId,
       "ospfLsdbType": ospfLsdbType,
       "ospfLsdbLsid": ospfLsdbLsid,
       "ospfLsdbRouterId": ospfLsdbRouterId,
       "ospfLsdbSequence": ospfLsdbSequence,
       "ospfLsdbAge": ospfLsdbAge,
       "ospfLsdbChecksum": ospfLsdbChecksum,
       "ospfLsdbAdvertisement": ospfLsdbAdvertisement,
       "ospfAreaRangeTable": ospfAreaRangeTable,
       "ospfAreaRangeEntry": ospfAreaRangeEntry,
       "ospfAreaRangeAreaId": ospfAreaRangeAreaId,
       "ospfAreaRangeNet": ospfAreaRangeNet,
       "ospfAreaRangeMask": ospfAreaRangeMask,
       "ospfAreaRangeStatus": ospfAreaRangeStatus,
       "ospfAreaRangeEffect": ospfAreaRangeEffect,
       "ospfHostTable": ospfHostTable,
       "ospfHostEntry": ospfHostEntry,
       "ospfHostIpAddress": ospfHostIpAddress,
       "ospfHostTOS": ospfHostTOS,
       "ospfHostMetric": ospfHostMetric,
       "ospfHostStatus": ospfHostStatus,
       "ospfHostAreaID": ospfHostAreaID,
       "ospfHostCfgAreaID": ospfHostCfgAreaID,
       "ospfIfTable": ospfIfTable,
       "ospfIfEntry": ospfIfEntry,
       "ospfIfIpAddress": ospfIfIpAddress,
       "ospfAddressLessIf": ospfAddressLessIf,
       "ospfIfAreaId": ospfIfAreaId,
       "ospfIfType": ospfIfType,
       "ospfIfAdminStat": ospfIfAdminStat,
       "ospfIfRtrPriority": ospfIfRtrPriority,
       "ospfIfTransitDelay": ospfIfTransitDelay,
       "ospfIfRetransInterval": ospfIfRetransInterval,
       "ospfIfHelloInterval": ospfIfHelloInterval,
       "ospfIfRtrDeadInterval": ospfIfRtrDeadInterval,
       "ospfIfPollInterval": ospfIfPollInterval,
       "ospfIfState": ospfIfState,
       "ospfIfDesignatedRouter": ospfIfDesignatedRouter,
       "ospfIfBackupDesignatedRouter": ospfIfBackupDesignatedRouter,
       "ospfIfEvents": ospfIfEvents,
       "ospfIfAuthKey": ospfIfAuthKey,
       "ospfIfStatus": ospfIfStatus,
       "ospfIfMulticastForwarding": ospfIfMulticastForwarding,
       "ospfIfDemand": ospfIfDemand,
       "ospfIfAuthType": ospfIfAuthType,
       "ospfIfLsaCount": ospfIfLsaCount,
       "ospfIfLsaCksumSum": ospfIfLsaCksumSum,
       "ospfIfDesignatedRouterId": ospfIfDesignatedRouterId,
       "ospfIfBackupDesignatedRouterId": ospfIfBackupDesignatedRouterId,
       "ospfIfMetricTable": ospfIfMetricTable,
       "ospfIfMetricEntry": ospfIfMetricEntry,
       "ospfIfMetricIpAddress": ospfIfMetricIpAddress,
       "ospfIfMetricAddressLessIf": ospfIfMetricAddressLessIf,
       "ospfIfMetricTOS": ospfIfMetricTOS,
       "ospfIfMetricValue": ospfIfMetricValue,
       "ospfIfMetricStatus": ospfIfMetricStatus,
       "ospfVirtIfTable": ospfVirtIfTable,
       "ospfVirtIfEntry": ospfVirtIfEntry,
       "ospfVirtIfAreaId": ospfVirtIfAreaId,
       "ospfVirtIfNeighbor": ospfVirtIfNeighbor,
       "ospfVirtIfTransitDelay": ospfVirtIfTransitDelay,
       "ospfVirtIfRetransInterval": ospfVirtIfRetransInterval,
       "ospfVirtIfHelloInterval": ospfVirtIfHelloInterval,
       "ospfVirtIfRtrDeadInterval": ospfVirtIfRtrDeadInterval,
       "ospfVirtIfState": ospfVirtIfState,
       "ospfVirtIfEvents": ospfVirtIfEvents,
       "ospfVirtIfAuthKey": ospfVirtIfAuthKey,
       "ospfVirtIfStatus": ospfVirtIfStatus,
       "ospfVirtIfAuthType": ospfVirtIfAuthType,
       "ospfVirtIfLsaCount": ospfVirtIfLsaCount,
       "ospfVirtIfLsaCksumSum": ospfVirtIfLsaCksumSum,
       "ospfNbrTable": ospfNbrTable,
       "ospfNbrEntry": ospfNbrEntry,
       "ospfNbrIpAddr": ospfNbrIpAddr,
       "ospfNbrAddressLessIndex": ospfNbrAddressLessIndex,
       "ospfNbrRtrId": ospfNbrRtrId,
       "ospfNbrOptions": ospfNbrOptions,
       "ospfNbrPriority": ospfNbrPriority,
       "ospfNbrState": ospfNbrState,
       "ospfNbrEvents": ospfNbrEvents,
       "ospfNbrLsRetransQLen": ospfNbrLsRetransQLen,
       "ospfNbmaNbrStatus": ospfNbmaNbrStatus,
       "ospfNbmaNbrPermanence": ospfNbmaNbrPermanence,
       "ospfNbrHelloSuppressed": ospfNbrHelloSuppressed,
       "ospfNbrRestartHelperStatus": ospfNbrRestartHelperStatus,
       "ospfNbrRestartHelperAge": ospfNbrRestartHelperAge,
       "ospfNbrRestartHelperExitReason": ospfNbrRestartHelperExitReason,
       "ospfVirtNbrTable": ospfVirtNbrTable,
       "ospfVirtNbrEntry": ospfVirtNbrEntry,
       "ospfVirtNbrArea": ospfVirtNbrArea,
       "ospfVirtNbrRtrId": ospfVirtNbrRtrId,
       "ospfVirtNbrIpAddr": ospfVirtNbrIpAddr,
       "ospfVirtNbrOptions": ospfVirtNbrOptions,
       "ospfVirtNbrState": ospfVirtNbrState,
       "ospfVirtNbrEvents": ospfVirtNbrEvents,
       "ospfVirtNbrLsRetransQLen": ospfVirtNbrLsRetransQLen,
       "ospfVirtNbrHelloSuppressed": ospfVirtNbrHelloSuppressed,
       "ospfVirtNbrRestartHelperStatus": ospfVirtNbrRestartHelperStatus,
       "ospfVirtNbrRestartHelperAge": ospfVirtNbrRestartHelperAge,
       "ospfVirtNbrRestartHelperExitReason": ospfVirtNbrRestartHelperExitReason,
       "ospfExtLsdbTable": ospfExtLsdbTable,
       "ospfExtLsdbEntry": ospfExtLsdbEntry,
       "ospfExtLsdbType": ospfExtLsdbType,
       "ospfExtLsdbLsid": ospfExtLsdbLsid,
       "ospfExtLsdbRouterId": ospfExtLsdbRouterId,
       "ospfExtLsdbSequence": ospfExtLsdbSequence,
       "ospfExtLsdbAge": ospfExtLsdbAge,
       "ospfExtLsdbChecksum": ospfExtLsdbChecksum,
       "ospfExtLsdbAdvertisement": ospfExtLsdbAdvertisement,
       "ospfRouteGroup": ospfRouteGroup,
       "ospfIntraArea": ospfIntraArea,
       "ospfInterArea": ospfInterArea,
       "ospfExternalType1": ospfExternalType1,
       "ospfExternalType2": ospfExternalType2,
       "ospfAreaAggregateTable": ospfAreaAggregateTable,
       "ospfAreaAggregateEntry": ospfAreaAggregateEntry,
       "ospfAreaAggregateAreaID": ospfAreaAggregateAreaID,
       "ospfAreaAggregateLsdbType": ospfAreaAggregateLsdbType,
       "ospfAreaAggregateNet": ospfAreaAggregateNet,
       "ospfAreaAggregateMask": ospfAreaAggregateMask,
       "ospfAreaAggregateStatus": ospfAreaAggregateStatus,
       "ospfAreaAggregateEffect": ospfAreaAggregateEffect,
       "ospfAreaAggregateExtRouteTag": ospfAreaAggregateExtRouteTag,
       "ospfConformance": ospfConformance,
       "ospfGroups": ospfGroups,
       "ospfBasicGroup": ospfBasicGroup,
       "ospfAreaGroup": ospfAreaGroup,
       "ospfStubAreaGroup": ospfStubAreaGroup,
       "ospfLsdbGroup": ospfLsdbGroup,
       "ospfAreaRangeGroup": ospfAreaRangeGroup,
       "ospfHostGroup": ospfHostGroup,
       "ospfIfGroup": ospfIfGroup,
       "ospfIfMetricGroup": ospfIfMetricGroup,
       "ospfVirtIfGroup": ospfVirtIfGroup,
       "ospfNbrGroup": ospfNbrGroup,
       "ospfVirtNbrGroup": ospfVirtNbrGroup,
       "ospfExtLsdbGroup": ospfExtLsdbGroup,
       "ospfAreaAggregateGroup": ospfAreaAggregateGroup,
       "ospfLocalLsdbGroup": ospfLocalLsdbGroup,
       "ospfVirtLocalLsdbGroup": ospfVirtLocalLsdbGroup,
       "ospfAsLsdbGroup": ospfAsLsdbGroup,
       "ospfBasicGroup2": ospfBasicGroup2,
       "ospfAreaGroup2": ospfAreaGroup2,
       "ospfIfGroup2": ospfIfGroup2,
       "ospfVirtIfGroup2": ospfVirtIfGroup2,
       "ospfNbrGroup2": ospfNbrGroup2,
       "ospfVirtNbrGroup2": ospfVirtNbrGroup2,
       "ospfAreaAggregateGroup2": ospfAreaAggregateGroup2,
       "ospfAreaLsaCountGroup": ospfAreaLsaCountGroup,
       "ospfHostGroup2": ospfHostGroup2,
       "ospfObsoleteGroup": ospfObsoleteGroup,
       "ospfCompliances": ospfCompliances,
       "ospfCompliance": ospfCompliance,
       "ospfCompliance2": ospfCompliance2,
       "ospfComplianceObsolete": ospfComplianceObsolete,
       "ospfLocalLsdbTable": ospfLocalLsdbTable,
       "ospfLocalLsdbEntry": ospfLocalLsdbEntry,
       "ospfLocalLsdbIpAddress": ospfLocalLsdbIpAddress,
       "ospfLocalLsdbAddressLessIf": ospfLocalLsdbAddressLessIf,
       "ospfLocalLsdbType": ospfLocalLsdbType,
       "ospfLocalLsdbLsid": ospfLocalLsdbLsid,
       "ospfLocalLsdbRouterId": ospfLocalLsdbRouterId,
       "ospfLocalLsdbSequence": ospfLocalLsdbSequence,
       "ospfLocalLsdbAge": ospfLocalLsdbAge,
       "ospfLocalLsdbChecksum": ospfLocalLsdbChecksum,
       "ospfLocalLsdbAdvertisement": ospfLocalLsdbAdvertisement,
       "ospfVirtLocalLsdbTable": ospfVirtLocalLsdbTable,
       "ospfVirtLocalLsdbEntry": ospfVirtLocalLsdbEntry,
       "ospfVirtLocalLsdbTransitArea": ospfVirtLocalLsdbTransitArea,
       "ospfVirtLocalLsdbNeighbor": ospfVirtLocalLsdbNeighbor,
       "ospfVirtLocalLsdbType": ospfVirtLocalLsdbType,
       "ospfVirtLocalLsdbLsid": ospfVirtLocalLsdbLsid,
       "ospfVirtLocalLsdbRouterId": ospfVirtLocalLsdbRouterId,
       "ospfVirtLocalLsdbSequence": ospfVirtLocalLsdbSequence,
       "ospfVirtLocalLsdbAge": ospfVirtLocalLsdbAge,
       "ospfVirtLocalLsdbChecksum": ospfVirtLocalLsdbChecksum,
       "ospfVirtLocalLsdbAdvertisement": ospfVirtLocalLsdbAdvertisement,
       "ospfAsLsdbTable": ospfAsLsdbTable,
       "ospfAsLsdbEntry": ospfAsLsdbEntry,
       "ospfAsLsdbType": ospfAsLsdbType,
       "ospfAsLsdbLsid": ospfAsLsdbLsid,
       "ospfAsLsdbRouterId": ospfAsLsdbRouterId,
       "ospfAsLsdbSequence": ospfAsLsdbSequence,
       "ospfAsLsdbAge": ospfAsLsdbAge,
       "ospfAsLsdbChecksum": ospfAsLsdbChecksum,
       "ospfAsLsdbAdvertisement": ospfAsLsdbAdvertisement,
       "ospfAreaLsaCountTable": ospfAreaLsaCountTable,
       "ospfAreaLsaCountEntry": ospfAreaLsaCountEntry,
       "ospfAreaLsaCountAreaId": ospfAreaLsaCountAreaId,
       "ospfAreaLsaCountLsaType": ospfAreaLsaCountLsaType,
       "ospfAreaLsaCountNumber": ospfAreaLsaCountNumber}
)

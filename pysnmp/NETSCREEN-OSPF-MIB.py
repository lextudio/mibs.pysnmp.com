# SNMP MIB module (NETSCREEN-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:48 2024
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

(netscreenVR,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVR")

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

nsOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AreaID(IpAddress, TextualConvention):
    status = "deprecated"


class RouterID(IpAddress, TextualConvention):
    status = "deprecated"


class Metric(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BigMetric(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )



class Status(Integer32, TextualConvention):
    status = "deprecated"
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
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class HelloRange(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class UpToMaxAge(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class InterfaceIndex(Integer32, TextualConvention):
    status = "deprecated"


class DesignatedRouterPriority(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TOSType(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )



# MIB Managed Objects in the order of their OIDs

_NsOspfGeneralTable_Object = MibTable
nsOspfGeneralTable = _NsOspfGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1)
)
if mibBuilder.loadTexts:
    nsOspfGeneralTable.setStatus("deprecated")
_NsOspfGeneralEntry_Object = MibTableRow
nsOspfGeneralEntry = _NsOspfGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1)
)
nsOspfGeneralEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfGeneralVRID"),
)
if mibBuilder.loadTexts:
    nsOspfGeneralEntry.setStatus("deprecated")
_NsOspfRouterId_Type = RouterID
_NsOspfRouterId_Object = MibTableColumn
nsOspfRouterId = _NsOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 1),
    _NsOspfRouterId_Type()
)
nsOspfRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfRouterId.setStatus("deprecated")
_NsOspfAdminStat_Type = Status
_NsOspfAdminStat_Object = MibTableColumn
nsOspfAdminStat = _NsOspfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 2),
    _NsOspfAdminStat_Type()
)
nsOspfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAdminStat.setStatus("deprecated")


class _NsOspfVersionNumber_Type(Integer32):
    """Custom type nsOspfVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("version2", 2)
    )


_NsOspfVersionNumber_Type.__name__ = "Integer32"
_NsOspfVersionNumber_Object = MibTableColumn
nsOspfVersionNumber = _NsOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 3),
    _NsOspfVersionNumber_Type()
)
nsOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVersionNumber.setStatus("deprecated")
_NsOspfAreaBdrRtrStatus_Type = TruthValue
_NsOspfAreaBdrRtrStatus_Object = MibTableColumn
nsOspfAreaBdrRtrStatus = _NsOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 4),
    _NsOspfAreaBdrRtrStatus_Type()
)
nsOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAreaBdrRtrStatus.setStatus("deprecated")
_NsOspfASBdrRtrStatus_Type = TruthValue
_NsOspfASBdrRtrStatus_Object = MibTableColumn
nsOspfASBdrRtrStatus = _NsOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 5),
    _NsOspfASBdrRtrStatus_Type()
)
nsOspfASBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfASBdrRtrStatus.setStatus("deprecated")
_NsOspfExternLsaCount_Type = Gauge32
_NsOspfExternLsaCount_Object = MibTableColumn
nsOspfExternLsaCount = _NsOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 6),
    _NsOspfExternLsaCount_Type()
)
nsOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExternLsaCount.setStatus("deprecated")
_NsOspfExternLsaCksumSum_Type = Integer32
_NsOspfExternLsaCksumSum_Object = MibTableColumn
nsOspfExternLsaCksumSum = _NsOspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 7),
    _NsOspfExternLsaCksumSum_Type()
)
nsOspfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExternLsaCksumSum.setStatus("deprecated")
_NsOspfTOSSupport_Type = TruthValue
_NsOspfTOSSupport_Object = MibTableColumn
nsOspfTOSSupport = _NsOspfTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 8),
    _NsOspfTOSSupport_Type()
)
nsOspfTOSSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfTOSSupport.setStatus("deprecated")
_NsOspfOriginateNewLsas_Type = Counter32
_NsOspfOriginateNewLsas_Object = MibTableColumn
nsOspfOriginateNewLsas = _NsOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 9),
    _NsOspfOriginateNewLsas_Type()
)
nsOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfOriginateNewLsas.setStatus("deprecated")
_NsOspfRxNewLsas_Type = Counter32
_NsOspfRxNewLsas_Object = MibTableColumn
nsOspfRxNewLsas = _NsOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 10),
    _NsOspfRxNewLsas_Type()
)
nsOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfRxNewLsas.setStatus("deprecated")


class _NsOspfExtLsdbLimit_Type(Integer32):
    """Custom type nsOspfExtLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NsOspfExtLsdbLimit_Type.__name__ = "Integer32"
_NsOspfExtLsdbLimit_Object = MibTableColumn
nsOspfExtLsdbLimit = _NsOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 11),
    _NsOspfExtLsdbLimit_Type()
)
nsOspfExtLsdbLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExtLsdbLimit.setStatus("deprecated")


class _NsOspfMulticastExtensions_Type(Integer32):
    """Custom type nsOspfMulticastExtensions based on Integer32"""
    defaultValue = 0


_NsOspfMulticastExtensions_Object = MibTableColumn
nsOspfMulticastExtensions = _NsOspfMulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 12),
    _NsOspfMulticastExtensions_Type()
)
nsOspfMulticastExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfMulticastExtensions.setStatus("deprecated")


class _NsOspfExitOverflowInterval_Type(PositiveInteger):
    """Custom type nsOspfExitOverflowInterval based on PositiveInteger"""
    defaultValue = 0


_NsOspfExitOverflowInterval_Object = MibTableColumn
nsOspfExitOverflowInterval = _NsOspfExitOverflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 13),
    _NsOspfExitOverflowInterval_Type()
)
nsOspfExitOverflowInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExitOverflowInterval.setStatus("deprecated")
_NsOspfDemandExtensions_Type = TruthValue
_NsOspfDemandExtensions_Object = MibTableColumn
nsOspfDemandExtensions = _NsOspfDemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 14),
    _NsOspfDemandExtensions_Type()
)
nsOspfDemandExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfDemandExtensions.setStatus("deprecated")


class _NsOspfGeneralVRID_Type(Integer32):
    """Custom type nsOspfGeneralVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfGeneralVRID_Type.__name__ = "Integer32"
_NsOspfGeneralVRID_Object = MibTableColumn
nsOspfGeneralVRID = _NsOspfGeneralVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 1, 1, 15),
    _NsOspfGeneralVRID_Type()
)
nsOspfGeneralVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfGeneralVRID.setStatus("deprecated")
_NsOspfAreaTable_Object = MibTable
nsOspfAreaTable = _NsOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2)
)
if mibBuilder.loadTexts:
    nsOspfAreaTable.setStatus("deprecated")
_NsOspfAreaEntry_Object = MibTableRow
nsOspfAreaEntry = _NsOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2, 1)
)
nsOspfAreaEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfAreaId"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfAreaVRID"),
)
if mibBuilder.loadTexts:
    nsOspfAreaEntry.setStatus("deprecated")
_NsOspfAreaId_Type = AreaID
_NsOspfAreaId_Object = MibTableColumn
nsOspfAreaId = _NsOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2, 1, 1),
    _NsOspfAreaId_Type()
)
nsOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAreaId.setStatus("deprecated")


class _NsOspfImportAsExtern_Type(Integer32):
    """Custom type nsOspfImportAsExtern based on Integer32"""
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


_NsOspfImportAsExtern_Type.__name__ = "Integer32"
_NsOspfImportAsExtern_Object = MibTableColumn
nsOspfImportAsExtern = _NsOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2, 1, 3),
    _NsOspfImportAsExtern_Type()
)
nsOspfImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfImportAsExtern.setStatus("deprecated")
_NsOspfSpfRuns_Type = Counter32
_NsOspfSpfRuns_Object = MibTableColumn
nsOspfSpfRuns = _NsOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2, 1, 4),
    _NsOspfSpfRuns_Type()
)
nsOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfSpfRuns.setStatus("deprecated")
_NsOspfAreaBdrRtrCount_Type = Gauge32
_NsOspfAreaBdrRtrCount_Object = MibTableColumn
nsOspfAreaBdrRtrCount = _NsOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2, 1, 5),
    _NsOspfAreaBdrRtrCount_Type()
)
nsOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAreaBdrRtrCount.setStatus("deprecated")
_NsOspfAsBdrRtrCount_Type = Gauge32
_NsOspfAsBdrRtrCount_Object = MibTableColumn
nsOspfAsBdrRtrCount = _NsOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2, 1, 6),
    _NsOspfAsBdrRtrCount_Type()
)
nsOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAsBdrRtrCount.setStatus("deprecated")
_NsOspfAreaLsaCount_Type = Gauge32
_NsOspfAreaLsaCount_Object = MibTableColumn
nsOspfAreaLsaCount = _NsOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2, 1, 7),
    _NsOspfAreaLsaCount_Type()
)
nsOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAreaLsaCount.setStatus("deprecated")


class _NsOspfAreaLsaCksumSum_Type(Integer32):
    """Custom type nsOspfAreaLsaCksumSum based on Integer32"""
    defaultValue = 0


_NsOspfAreaLsaCksumSum_Object = MibTableColumn
nsOspfAreaLsaCksumSum = _NsOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2, 1, 8),
    _NsOspfAreaLsaCksumSum_Type()
)
nsOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAreaLsaCksumSum.setStatus("deprecated")


class _NsOspfAreaSummary_Type(Integer32):
    """Custom type nsOspfAreaSummary based on Integer32"""
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


_NsOspfAreaSummary_Type.__name__ = "Integer32"
_NsOspfAreaSummary_Object = MibTableColumn
nsOspfAreaSummary = _NsOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2, 1, 9),
    _NsOspfAreaSummary_Type()
)
nsOspfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfAreaSummary.setStatus("deprecated")
_NsOspfAreaStatus_Type = RowStatus
_NsOspfAreaStatus_Object = MibTableColumn
nsOspfAreaStatus = _NsOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2, 1, 10),
    _NsOspfAreaStatus_Type()
)
nsOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfAreaStatus.setStatus("deprecated")


class _NsOspfAreaVRID_Type(Integer32):
    """Custom type nsOspfAreaVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfAreaVRID_Type.__name__ = "Integer32"
_NsOspfAreaVRID_Object = MibTableColumn
nsOspfAreaVRID = _NsOspfAreaVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 2, 1, 11),
    _NsOspfAreaVRID_Type()
)
nsOspfAreaVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAreaVRID.setStatus("deprecated")
_NsOspfStubAreaTable_Object = MibTable
nsOspfStubAreaTable = _NsOspfStubAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 3)
)
if mibBuilder.loadTexts:
    nsOspfStubAreaTable.setStatus("deprecated")
_NsOspfStubAreaEntry_Object = MibTableRow
nsOspfStubAreaEntry = _NsOspfStubAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 3, 1)
)
nsOspfStubAreaEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfStubAreaId"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfStubTOS"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfStubVRID"),
)
if mibBuilder.loadTexts:
    nsOspfStubAreaEntry.setStatus("deprecated")
_NsOspfStubAreaId_Type = AreaID
_NsOspfStubAreaId_Object = MibTableColumn
nsOspfStubAreaId = _NsOspfStubAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 3, 1, 1),
    _NsOspfStubAreaId_Type()
)
nsOspfStubAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfStubAreaId.setStatus("deprecated")
_NsOspfStubTOS_Type = TOSType
_NsOspfStubTOS_Object = MibTableColumn
nsOspfStubTOS = _NsOspfStubTOS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 3, 1, 2),
    _NsOspfStubTOS_Type()
)
nsOspfStubTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfStubTOS.setStatus("deprecated")
_NsOspfStubMetric_Type = BigMetric
_NsOspfStubMetric_Object = MibTableColumn
nsOspfStubMetric = _NsOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 3, 1, 3),
    _NsOspfStubMetric_Type()
)
nsOspfStubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfStubMetric.setStatus("deprecated")
_NsOspfStubStatus_Type = RowStatus
_NsOspfStubStatus_Object = MibTableColumn
nsOspfStubStatus = _NsOspfStubStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 3, 1, 4),
    _NsOspfStubStatus_Type()
)
nsOspfStubStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfStubStatus.setStatus("deprecated")


class _NsOspfStubMetricType_Type(Integer32):
    """Custom type nsOspfStubMetricType based on Integer32"""
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
          ("nsOspfMetric", 1))
    )


_NsOspfStubMetricType_Type.__name__ = "Integer32"
_NsOspfStubMetricType_Object = MibTableColumn
nsOspfStubMetricType = _NsOspfStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 3, 1, 5),
    _NsOspfStubMetricType_Type()
)
nsOspfStubMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfStubMetricType.setStatus("deprecated")


class _NsOspfStubVRID_Type(Integer32):
    """Custom type nsOspfStubVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfStubVRID_Type.__name__ = "Integer32"
_NsOspfStubVRID_Object = MibTableColumn
nsOspfStubVRID = _NsOspfStubVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 3, 1, 6),
    _NsOspfStubVRID_Type()
)
nsOspfStubVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfStubVRID.setStatus("deprecated")
_NsOspfLsdbTable_Object = MibTable
nsOspfLsdbTable = _NsOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 4)
)
if mibBuilder.loadTexts:
    nsOspfLsdbTable.setStatus("deprecated")
_NsOspfLsdbEntry_Object = MibTableRow
nsOspfLsdbEntry = _NsOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 4, 1)
)
nsOspfLsdbEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfLsdbAreaId"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfLsdbType"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfLsdbLsid"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfLsdbRouterId"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfLsdbVRID"),
)
if mibBuilder.loadTexts:
    nsOspfLsdbEntry.setStatus("deprecated")
_NsOspfLsdbAreaId_Type = AreaID
_NsOspfLsdbAreaId_Object = MibTableColumn
nsOspfLsdbAreaId = _NsOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 4, 1, 1),
    _NsOspfLsdbAreaId_Type()
)
nsOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfLsdbAreaId.setStatus("deprecated")


class _NsOspfLsdbType_Type(Integer32):
    """Custom type nsOspfLsdbType based on Integer32"""
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
        *(("asExternalLink", 5),
          ("asSummaryLink", 4),
          ("multicastLink", 6),
          ("networkLink", 2),
          ("nssaExternalLink", 7),
          ("routerLink", 1),
          ("summaryLink", 3))
    )


_NsOspfLsdbType_Type.__name__ = "Integer32"
_NsOspfLsdbType_Object = MibTableColumn
nsOspfLsdbType = _NsOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 4, 1, 2),
    _NsOspfLsdbType_Type()
)
nsOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfLsdbType.setStatus("deprecated")
_NsOspfLsdbLsid_Type = IpAddress
_NsOspfLsdbLsid_Object = MibTableColumn
nsOspfLsdbLsid = _NsOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 4, 1, 3),
    _NsOspfLsdbLsid_Type()
)
nsOspfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfLsdbLsid.setStatus("deprecated")
_NsOspfLsdbRouterId_Type = RouterID
_NsOspfLsdbRouterId_Object = MibTableColumn
nsOspfLsdbRouterId = _NsOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 4, 1, 4),
    _NsOspfLsdbRouterId_Type()
)
nsOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfLsdbRouterId.setStatus("deprecated")
_NsOspfLsdbSequence_Type = Integer32
_NsOspfLsdbSequence_Object = MibTableColumn
nsOspfLsdbSequence = _NsOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 4, 1, 5),
    _NsOspfLsdbSequence_Type()
)
nsOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfLsdbSequence.setStatus("deprecated")
_NsOspfLsdbAge_Type = Integer32
_NsOspfLsdbAge_Object = MibTableColumn
nsOspfLsdbAge = _NsOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 4, 1, 6),
    _NsOspfLsdbAge_Type()
)
nsOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfLsdbAge.setStatus("deprecated")
_NsOspfLsdbChecksum_Type = Integer32
_NsOspfLsdbChecksum_Object = MibTableColumn
nsOspfLsdbChecksum = _NsOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 4, 1, 7),
    _NsOspfLsdbChecksum_Type()
)
nsOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfLsdbChecksum.setStatus("deprecated")


class _NsOspfLsdbAdvertisement_Type(OctetString):
    """Custom type nsOspfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_NsOspfLsdbAdvertisement_Type.__name__ = "OctetString"
_NsOspfLsdbAdvertisement_Object = MibTableColumn
nsOspfLsdbAdvertisement = _NsOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 4, 1, 8),
    _NsOspfLsdbAdvertisement_Type()
)
nsOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfLsdbAdvertisement.setStatus("deprecated")


class _NsOspfLsdbVRID_Type(Integer32):
    """Custom type nsOspfLsdbVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfLsdbVRID_Type.__name__ = "Integer32"
_NsOspfLsdbVRID_Object = MibTableColumn
nsOspfLsdbVRID = _NsOspfLsdbVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 4, 1, 9),
    _NsOspfLsdbVRID_Type()
)
nsOspfLsdbVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfLsdbVRID.setStatus("deprecated")
_NsOspfHostTable_Object = MibTable
nsOspfHostTable = _NsOspfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 6)
)
if mibBuilder.loadTexts:
    nsOspfHostTable.setStatus("deprecated")
_NsOspfHostEntry_Object = MibTableRow
nsOspfHostEntry = _NsOspfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 6, 1)
)
nsOspfHostEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfHostIpAddress"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfHostTOS"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfHostVRID"),
)
if mibBuilder.loadTexts:
    nsOspfHostEntry.setStatus("deprecated")
_NsOspfHostIpAddress_Type = IpAddress
_NsOspfHostIpAddress_Object = MibTableColumn
nsOspfHostIpAddress = _NsOspfHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 6, 1, 1),
    _NsOspfHostIpAddress_Type()
)
nsOspfHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfHostIpAddress.setStatus("deprecated")
_NsOspfHostTOS_Type = TOSType
_NsOspfHostTOS_Object = MibTableColumn
nsOspfHostTOS = _NsOspfHostTOS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 6, 1, 2),
    _NsOspfHostTOS_Type()
)
nsOspfHostTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfHostTOS.setStatus("deprecated")
_NsOspfHostMetric_Type = Metric
_NsOspfHostMetric_Object = MibTableColumn
nsOspfHostMetric = _NsOspfHostMetric_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 6, 1, 3),
    _NsOspfHostMetric_Type()
)
nsOspfHostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfHostMetric.setStatus("deprecated")
_NsOspfHostStatus_Type = RowStatus
_NsOspfHostStatus_Object = MibTableColumn
nsOspfHostStatus = _NsOspfHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 6, 1, 4),
    _NsOspfHostStatus_Type()
)
nsOspfHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfHostStatus.setStatus("deprecated")
_NsOspfHostAreaID_Type = AreaID
_NsOspfHostAreaID_Object = MibTableColumn
nsOspfHostAreaID = _NsOspfHostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 6, 1, 5),
    _NsOspfHostAreaID_Type()
)
nsOspfHostAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfHostAreaID.setStatus("deprecated")


class _NsOspfHostVRID_Type(Integer32):
    """Custom type nsOspfHostVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfHostVRID_Type.__name__ = "Integer32"
_NsOspfHostVRID_Object = MibTableColumn
nsOspfHostVRID = _NsOspfHostVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 6, 1, 6),
    _NsOspfHostVRID_Type()
)
nsOspfHostVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfHostVRID.setStatus("deprecated")
_NsOspfIfTable_Object = MibTable
nsOspfIfTable = _NsOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7)
)
if mibBuilder.loadTexts:
    nsOspfIfTable.setStatus("deprecated")
_NsOspfIfEntry_Object = MibTableRow
nsOspfIfEntry = _NsOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1)
)
nsOspfIfEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfIfIpAddress"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfAddressLessIf"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfIfVRID"),
)
if mibBuilder.loadTexts:
    nsOspfIfEntry.setStatus("deprecated")
_NsOspfIfIpAddress_Type = IpAddress
_NsOspfIfIpAddress_Object = MibTableColumn
nsOspfIfIpAddress = _NsOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 1),
    _NsOspfIfIpAddress_Type()
)
nsOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfIfIpAddress.setStatus("deprecated")
_NsOspfAddressLessIf_Type = Integer32
_NsOspfAddressLessIf_Object = MibTableColumn
nsOspfAddressLessIf = _NsOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 2),
    _NsOspfAddressLessIf_Type()
)
nsOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAddressLessIf.setStatus("deprecated")


class _NsOspfIfAreaId_Type(AreaID):
    """Custom type nsOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_NsOspfIfAreaId_Object = MibTableColumn
nsOspfIfAreaId = _NsOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 3),
    _NsOspfIfAreaId_Type()
)
nsOspfIfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfAreaId.setStatus("deprecated")


class _NsOspfIfType_Type(Integer32):
    """Custom type nsOspfIfType based on Integer32"""
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


_NsOspfIfType_Type.__name__ = "Integer32"
_NsOspfIfType_Object = MibTableColumn
nsOspfIfType = _NsOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 4),
    _NsOspfIfType_Type()
)
nsOspfIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfType.setStatus("deprecated")


class _NsOspfIfAdminStat_Type(Status):
    """Custom type nsOspfIfAdminStat based on Status"""


_NsOspfIfAdminStat_Object = MibTableColumn
nsOspfIfAdminStat = _NsOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 5),
    _NsOspfIfAdminStat_Type()
)
nsOspfIfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfAdminStat.setStatus("deprecated")


class _NsOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type nsOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_NsOspfIfRtrPriority_Object = MibTableColumn
nsOspfIfRtrPriority = _NsOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 6),
    _NsOspfIfRtrPriority_Type()
)
nsOspfIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfRtrPriority.setStatus("deprecated")


class _NsOspfIfTransitDelay_Type(UpToMaxAge):
    """Custom type nsOspfIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_NsOspfIfTransitDelay_Object = MibTableColumn
nsOspfIfTransitDelay = _NsOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 7),
    _NsOspfIfTransitDelay_Type()
)
nsOspfIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfTransitDelay.setStatus("deprecated")


class _NsOspfIfRetransInterval_Type(UpToMaxAge):
    """Custom type nsOspfIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_NsOspfIfRetransInterval_Object = MibTableColumn
nsOspfIfRetransInterval = _NsOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 8),
    _NsOspfIfRetransInterval_Type()
)
nsOspfIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfRetransInterval.setStatus("deprecated")


class _NsOspfIfHelloInterval_Type(HelloRange):
    """Custom type nsOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_NsOspfIfHelloInterval_Object = MibTableColumn
nsOspfIfHelloInterval = _NsOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 9),
    _NsOspfIfHelloInterval_Type()
)
nsOspfIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfHelloInterval.setStatus("deprecated")


class _NsOspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type nsOspfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_NsOspfIfRtrDeadInterval_Object = MibTableColumn
nsOspfIfRtrDeadInterval = _NsOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 10),
    _NsOspfIfRtrDeadInterval_Type()
)
nsOspfIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfRtrDeadInterval.setStatus("deprecated")


class _NsOspfIfPollInterval_Type(PositiveInteger):
    """Custom type nsOspfIfPollInterval based on PositiveInteger"""
    defaultValue = 120


_NsOspfIfPollInterval_Object = MibTableColumn
nsOspfIfPollInterval = _NsOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 11),
    _NsOspfIfPollInterval_Type()
)
nsOspfIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfPollInterval.setStatus("deprecated")


class _NsOspfIfState_Type(Integer32):
    """Custom type nsOspfIfState based on Integer32"""
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


_NsOspfIfState_Type.__name__ = "Integer32"
_NsOspfIfState_Object = MibTableColumn
nsOspfIfState = _NsOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 12),
    _NsOspfIfState_Type()
)
nsOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfIfState.setStatus("deprecated")


class _NsOspfIfDesignatedRouter_Type(IpAddress):
    """Custom type nsOspfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_NsOspfIfDesignatedRouter_Object = MibTableColumn
nsOspfIfDesignatedRouter = _NsOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 13),
    _NsOspfIfDesignatedRouter_Type()
)
nsOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfIfDesignatedRouter.setStatus("deprecated")


class _NsOspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type nsOspfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_NsOspfIfBackupDesignatedRouter_Object = MibTableColumn
nsOspfIfBackupDesignatedRouter = _NsOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 14),
    _NsOspfIfBackupDesignatedRouter_Type()
)
nsOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfIfBackupDesignatedRouter.setStatus("deprecated")
_NsOspfIfEvents_Type = Counter32
_NsOspfIfEvents_Object = MibTableColumn
nsOspfIfEvents = _NsOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 15),
    _NsOspfIfEvents_Type()
)
nsOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfIfEvents.setStatus("deprecated")


class _NsOspfIfAuthKey_Type(OctetString):
    """Custom type nsOspfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NsOspfIfAuthKey_Type.__name__ = "OctetString"
_NsOspfIfAuthKey_Object = MibTableColumn
nsOspfIfAuthKey = _NsOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 16),
    _NsOspfIfAuthKey_Type()
)
nsOspfIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfAuthKey.setStatus("deprecated")
_NsOspfIfStatus_Type = RowStatus
_NsOspfIfStatus_Object = MibTableColumn
nsOspfIfStatus = _NsOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 17),
    _NsOspfIfStatus_Type()
)
nsOspfIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfStatus.setStatus("deprecated")


class _NsOspfIfMulticastForwarding_Type(Integer32):
    """Custom type nsOspfIfMulticastForwarding based on Integer32"""
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


_NsOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_NsOspfIfMulticastForwarding_Object = MibTableColumn
nsOspfIfMulticastForwarding = _NsOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 18),
    _NsOspfIfMulticastForwarding_Type()
)
nsOspfIfMulticastForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfMulticastForwarding.setStatus("deprecated")


class _NsOspfIfDemand_Type(TruthValue):
    """Custom type nsOspfIfDemand based on TruthValue"""


_NsOspfIfDemand_Object = MibTableColumn
nsOspfIfDemand = _NsOspfIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 19),
    _NsOspfIfDemand_Type()
)
nsOspfIfDemand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfDemand.setStatus("deprecated")


class _NsOspfIfAuthType_Type(Integer32):
    """Custom type nsOspfIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NsOspfIfAuthType_Type.__name__ = "Integer32"
_NsOspfIfAuthType_Object = MibTableColumn
nsOspfIfAuthType = _NsOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 20),
    _NsOspfIfAuthType_Type()
)
nsOspfIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfAuthType.setStatus("deprecated")


class _NsOspfIfVRID_Type(Integer32):
    """Custom type nsOspfIfVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfIfVRID_Type.__name__ = "Integer32"
_NsOspfIfVRID_Object = MibTableColumn
nsOspfIfVRID = _NsOspfIfVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 7, 1, 21),
    _NsOspfIfVRID_Type()
)
nsOspfIfVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfIfVRID.setStatus("deprecated")
_NsOspfIfMetricTable_Object = MibTable
nsOspfIfMetricTable = _NsOspfIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 8)
)
if mibBuilder.loadTexts:
    nsOspfIfMetricTable.setStatus("deprecated")
_NsOspfIfMetricEntry_Object = MibTableRow
nsOspfIfMetricEntry = _NsOspfIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 8, 1)
)
nsOspfIfMetricEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfIfMetricIpAddress"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfIfMetricAddressLessIf"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfIfMetricTOS"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfIfMetricVRID"),
)
if mibBuilder.loadTexts:
    nsOspfIfMetricEntry.setStatus("deprecated")
_NsOspfIfMetricIpAddress_Type = IpAddress
_NsOspfIfMetricIpAddress_Object = MibTableColumn
nsOspfIfMetricIpAddress = _NsOspfIfMetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 8, 1, 1),
    _NsOspfIfMetricIpAddress_Type()
)
nsOspfIfMetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfIfMetricIpAddress.setStatus("deprecated")
_NsOspfIfMetricAddressLessIf_Type = Integer32
_NsOspfIfMetricAddressLessIf_Object = MibTableColumn
nsOspfIfMetricAddressLessIf = _NsOspfIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 8, 1, 2),
    _NsOspfIfMetricAddressLessIf_Type()
)
nsOspfIfMetricAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfIfMetricAddressLessIf.setStatus("deprecated")
_NsOspfIfMetricTOS_Type = TOSType
_NsOspfIfMetricTOS_Object = MibTableColumn
nsOspfIfMetricTOS = _NsOspfIfMetricTOS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 8, 1, 3),
    _NsOspfIfMetricTOS_Type()
)
nsOspfIfMetricTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfIfMetricTOS.setStatus("deprecated")
_NsOspfIfMetricValue_Type = Metric
_NsOspfIfMetricValue_Object = MibTableColumn
nsOspfIfMetricValue = _NsOspfIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 8, 1, 4),
    _NsOspfIfMetricValue_Type()
)
nsOspfIfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfMetricValue.setStatus("deprecated")
_NsOspfIfMetricStatus_Type = RowStatus
_NsOspfIfMetricStatus_Object = MibTableColumn
nsOspfIfMetricStatus = _NsOspfIfMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 8, 1, 5),
    _NsOspfIfMetricStatus_Type()
)
nsOspfIfMetricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfIfMetricStatus.setStatus("deprecated")


class _NsOspfIfMetricVRID_Type(Integer32):
    """Custom type nsOspfIfMetricVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfIfMetricVRID_Type.__name__ = "Integer32"
_NsOspfIfMetricVRID_Object = MibTableColumn
nsOspfIfMetricVRID = _NsOspfIfMetricVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 8, 1, 6),
    _NsOspfIfMetricVRID_Type()
)
nsOspfIfMetricVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfIfMetricVRID.setStatus("deprecated")
_NsOspfVirtIfTable_Object = MibTable
nsOspfVirtIfTable = _NsOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9)
)
if mibBuilder.loadTexts:
    nsOspfVirtIfTable.setStatus("deprecated")
_NsOspfVirtIfEntry_Object = MibTableRow
nsOspfVirtIfEntry = _NsOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1)
)
nsOspfVirtIfEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfVirtIfAreaId"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfVirtIfNeighbor"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfVirtIfVRID"),
)
if mibBuilder.loadTexts:
    nsOspfVirtIfEntry.setStatus("deprecated")
_NsOspfVirtIfAreaId_Type = AreaID
_NsOspfVirtIfAreaId_Object = MibTableColumn
nsOspfVirtIfAreaId = _NsOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 1),
    _NsOspfVirtIfAreaId_Type()
)
nsOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtIfAreaId.setStatus("deprecated")
_NsOspfVirtIfNeighbor_Type = RouterID
_NsOspfVirtIfNeighbor_Object = MibTableColumn
nsOspfVirtIfNeighbor = _NsOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 2),
    _NsOspfVirtIfNeighbor_Type()
)
nsOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtIfNeighbor.setStatus("deprecated")


class _NsOspfVirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type nsOspfVirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_NsOspfVirtIfTransitDelay_Object = MibTableColumn
nsOspfVirtIfTransitDelay = _NsOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 3),
    _NsOspfVirtIfTransitDelay_Type()
)
nsOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfVirtIfTransitDelay.setStatus("deprecated")


class _NsOspfVirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type nsOspfVirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_NsOspfVirtIfRetransInterval_Object = MibTableColumn
nsOspfVirtIfRetransInterval = _NsOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 4),
    _NsOspfVirtIfRetransInterval_Type()
)
nsOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfVirtIfRetransInterval.setStatus("deprecated")


class _NsOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type nsOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_NsOspfVirtIfHelloInterval_Object = MibTableColumn
nsOspfVirtIfHelloInterval = _NsOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 5),
    _NsOspfVirtIfHelloInterval_Type()
)
nsOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfVirtIfHelloInterval.setStatus("deprecated")


class _NsOspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type nsOspfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 60


_NsOspfVirtIfRtrDeadInterval_Object = MibTableColumn
nsOspfVirtIfRtrDeadInterval = _NsOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 6),
    _NsOspfVirtIfRtrDeadInterval_Type()
)
nsOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfVirtIfRtrDeadInterval.setStatus("deprecated")


class _NsOspfVirtIfState_Type(Integer32):
    """Custom type nsOspfVirtIfState based on Integer32"""
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


_NsOspfVirtIfState_Type.__name__ = "Integer32"
_NsOspfVirtIfState_Object = MibTableColumn
nsOspfVirtIfState = _NsOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 7),
    _NsOspfVirtIfState_Type()
)
nsOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtIfState.setStatus("deprecated")
_NsOspfVirtIfEvents_Type = Counter32
_NsOspfVirtIfEvents_Object = MibTableColumn
nsOspfVirtIfEvents = _NsOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 8),
    _NsOspfVirtIfEvents_Type()
)
nsOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtIfEvents.setStatus("deprecated")


class _NsOspfVirtIfAuthKey_Type(OctetString):
    """Custom type nsOspfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NsOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_NsOspfVirtIfAuthKey_Object = MibTableColumn
nsOspfVirtIfAuthKey = _NsOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 9),
    _NsOspfVirtIfAuthKey_Type()
)
nsOspfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfVirtIfAuthKey.setStatus("deprecated")
_NsOspfVirtIfStatus_Type = RowStatus
_NsOspfVirtIfStatus_Object = MibTableColumn
nsOspfVirtIfStatus = _NsOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 10),
    _NsOspfVirtIfStatus_Type()
)
nsOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfVirtIfStatus.setStatus("deprecated")


class _NsOspfVirtIfAuthType_Type(Integer32):
    """Custom type nsOspfVirtIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NsOspfVirtIfAuthType_Type.__name__ = "Integer32"
_NsOspfVirtIfAuthType_Object = MibTableColumn
nsOspfVirtIfAuthType = _NsOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 11),
    _NsOspfVirtIfAuthType_Type()
)
nsOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfVirtIfAuthType.setStatus("deprecated")


class _NsOspfVirtIfVRID_Type(Integer32):
    """Custom type nsOspfVirtIfVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfVirtIfVRID_Type.__name__ = "Integer32"
_NsOspfVirtIfVRID_Object = MibTableColumn
nsOspfVirtIfVRID = _NsOspfVirtIfVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 9, 1, 12),
    _NsOspfVirtIfVRID_Type()
)
nsOspfVirtIfVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtIfVRID.setStatus("deprecated")
_NsOspfNbrTable_Object = MibTable
nsOspfNbrTable = _NsOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10)
)
if mibBuilder.loadTexts:
    nsOspfNbrTable.setStatus("deprecated")
_NsOspfNbrEntry_Object = MibTableRow
nsOspfNbrEntry = _NsOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1)
)
nsOspfNbrEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfNbrIpAddr"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfNbrAddressLessIndex"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfNbrVRID"),
)
if mibBuilder.loadTexts:
    nsOspfNbrEntry.setStatus("deprecated")
_NsOspfNbrIpAddr_Type = IpAddress
_NsOspfNbrIpAddr_Object = MibTableColumn
nsOspfNbrIpAddr = _NsOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 1),
    _NsOspfNbrIpAddr_Type()
)
nsOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfNbrIpAddr.setStatus("deprecated")
_NsOspfNbrAddressLessIndex_Type = InterfaceIndex
_NsOspfNbrAddressLessIndex_Object = MibTableColumn
nsOspfNbrAddressLessIndex = _NsOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 2),
    _NsOspfNbrAddressLessIndex_Type()
)
nsOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfNbrAddressLessIndex.setStatus("deprecated")


class _NsOspfNbrRtrId_Type(RouterID):
    """Custom type nsOspfNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_NsOspfNbrRtrId_Object = MibTableColumn
nsOspfNbrRtrId = _NsOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 3),
    _NsOspfNbrRtrId_Type()
)
nsOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfNbrRtrId.setStatus("deprecated")


class _NsOspfNbrOptions_Type(Integer32):
    """Custom type nsOspfNbrOptions based on Integer32"""
    defaultValue = 0


_NsOspfNbrOptions_Object = MibTableColumn
nsOspfNbrOptions = _NsOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 4),
    _NsOspfNbrOptions_Type()
)
nsOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfNbrOptions.setStatus("deprecated")


class _NsOspfNbrPriority_Type(DesignatedRouterPriority):
    """Custom type nsOspfNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_NsOspfNbrPriority_Object = MibTableColumn
nsOspfNbrPriority = _NsOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 5),
    _NsOspfNbrPriority_Type()
)
nsOspfNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfNbrPriority.setStatus("deprecated")


class _NsOspfNbrState_Type(Integer32):
    """Custom type nsOspfNbrState based on Integer32"""
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


_NsOspfNbrState_Type.__name__ = "Integer32"
_NsOspfNbrState_Object = MibTableColumn
nsOspfNbrState = _NsOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 6),
    _NsOspfNbrState_Type()
)
nsOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfNbrState.setStatus("deprecated")
_NsOspfNbrEvents_Type = Counter32
_NsOspfNbrEvents_Object = MibTableColumn
nsOspfNbrEvents = _NsOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 7),
    _NsOspfNbrEvents_Type()
)
nsOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfNbrEvents.setStatus("deprecated")
_NsOspfNbrLsRetransQLen_Type = Gauge32
_NsOspfNbrLsRetransQLen_Object = MibTableColumn
nsOspfNbrLsRetransQLen = _NsOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 8),
    _NsOspfNbrLsRetransQLen_Type()
)
nsOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfNbrLsRetransQLen.setStatus("deprecated")
_NsOspfNbmaNbrStatus_Type = RowStatus
_NsOspfNbmaNbrStatus_Object = MibTableColumn
nsOspfNbmaNbrStatus = _NsOspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 9),
    _NsOspfNbmaNbrStatus_Type()
)
nsOspfNbmaNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfNbmaNbrStatus.setStatus("deprecated")


class _NsOspfNbmaNbrPermanence_Type(Integer32):
    """Custom type nsOspfNbmaNbrPermanence based on Integer32"""
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


_NsOspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_NsOspfNbmaNbrPermanence_Object = MibTableColumn
nsOspfNbmaNbrPermanence = _NsOspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 10),
    _NsOspfNbmaNbrPermanence_Type()
)
nsOspfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfNbmaNbrPermanence.setStatus("deprecated")
_NsOspfNbrHelloSuppressed_Type = TruthValue
_NsOspfNbrHelloSuppressed_Object = MibTableColumn
nsOspfNbrHelloSuppressed = _NsOspfNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 11),
    _NsOspfNbrHelloSuppressed_Type()
)
nsOspfNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfNbrHelloSuppressed.setStatus("deprecated")


class _NsOspfNbrVRID_Type(Integer32):
    """Custom type nsOspfNbrVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfNbrVRID_Type.__name__ = "Integer32"
_NsOspfNbrVRID_Object = MibTableColumn
nsOspfNbrVRID = _NsOspfNbrVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 10, 1, 12),
    _NsOspfNbrVRID_Type()
)
nsOspfNbrVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfNbrVRID.setStatus("deprecated")
_NsOspfVirtNbrTable_Object = MibTable
nsOspfVirtNbrTable = _NsOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 11)
)
if mibBuilder.loadTexts:
    nsOspfVirtNbrTable.setStatus("deprecated")
_NsOspfVirtNbrEntry_Object = MibTableRow
nsOspfVirtNbrEntry = _NsOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 11, 1)
)
nsOspfVirtNbrEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfVirtNbrArea"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfVirtNbrRtrId"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfVirtNbrVRID"),
)
if mibBuilder.loadTexts:
    nsOspfVirtNbrEntry.setStatus("deprecated")
_NsOspfVirtNbrArea_Type = AreaID
_NsOspfVirtNbrArea_Object = MibTableColumn
nsOspfVirtNbrArea = _NsOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 11, 1, 1),
    _NsOspfVirtNbrArea_Type()
)
nsOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtNbrArea.setStatus("deprecated")
_NsOspfVirtNbrRtrId_Type = RouterID
_NsOspfVirtNbrRtrId_Object = MibTableColumn
nsOspfVirtNbrRtrId = _NsOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 11, 1, 2),
    _NsOspfVirtNbrRtrId_Type()
)
nsOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtNbrRtrId.setStatus("deprecated")
_NsOspfVirtNbrIpAddr_Type = IpAddress
_NsOspfVirtNbrIpAddr_Object = MibTableColumn
nsOspfVirtNbrIpAddr = _NsOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 11, 1, 3),
    _NsOspfVirtNbrIpAddr_Type()
)
nsOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtNbrIpAddr.setStatus("deprecated")
_NsOspfVirtNbrOptions_Type = Integer32
_NsOspfVirtNbrOptions_Object = MibTableColumn
nsOspfVirtNbrOptions = _NsOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 11, 1, 4),
    _NsOspfVirtNbrOptions_Type()
)
nsOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtNbrOptions.setStatus("deprecated")


class _NsOspfVirtNbrState_Type(Integer32):
    """Custom type nsOspfVirtNbrState based on Integer32"""
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


_NsOspfVirtNbrState_Type.__name__ = "Integer32"
_NsOspfVirtNbrState_Object = MibTableColumn
nsOspfVirtNbrState = _NsOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 11, 1, 5),
    _NsOspfVirtNbrState_Type()
)
nsOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtNbrState.setStatus("deprecated")
_NsOspfVirtNbrEvents_Type = Counter32
_NsOspfVirtNbrEvents_Object = MibTableColumn
nsOspfVirtNbrEvents = _NsOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 11, 1, 6),
    _NsOspfVirtNbrEvents_Type()
)
nsOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtNbrEvents.setStatus("deprecated")
_NsOspfVirtNbrLsRetransQLen_Type = Gauge32
_NsOspfVirtNbrLsRetransQLen_Object = MibTableColumn
nsOspfVirtNbrLsRetransQLen = _NsOspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 11, 1, 7),
    _NsOspfVirtNbrLsRetransQLen_Type()
)
nsOspfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtNbrLsRetransQLen.setStatus("deprecated")
_NsOspfVirtNbrHelloSuppressed_Type = TruthValue
_NsOspfVirtNbrHelloSuppressed_Object = MibTableColumn
nsOspfVirtNbrHelloSuppressed = _NsOspfVirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 11, 1, 8),
    _NsOspfVirtNbrHelloSuppressed_Type()
)
nsOspfVirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtNbrHelloSuppressed.setStatus("deprecated")


class _NsOspfVirtNbrVRID_Type(Integer32):
    """Custom type nsOspfVirtNbrVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfVirtNbrVRID_Type.__name__ = "Integer32"
_NsOspfVirtNbrVRID_Object = MibTableColumn
nsOspfVirtNbrVRID = _NsOspfVirtNbrVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 11, 1, 9),
    _NsOspfVirtNbrVRID_Type()
)
nsOspfVirtNbrVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfVirtNbrVRID.setStatus("deprecated")
_NsOspfExtLsdbTable_Object = MibTable
nsOspfExtLsdbTable = _NsOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 12)
)
if mibBuilder.loadTexts:
    nsOspfExtLsdbTable.setStatus("deprecated")
_NsOspfExtLsdbEntry_Object = MibTableRow
nsOspfExtLsdbEntry = _NsOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 12, 1)
)
nsOspfExtLsdbEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfExtLsdbType"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfExtLsdbLsid"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfExtLsdbRouterId"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfExtLsdbVRID"),
)
if mibBuilder.loadTexts:
    nsOspfExtLsdbEntry.setStatus("deprecated")


class _NsOspfExtLsdbType_Type(Integer32):
    """Custom type nsOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_NsOspfExtLsdbType_Type.__name__ = "Integer32"
_NsOspfExtLsdbType_Object = MibTableColumn
nsOspfExtLsdbType = _NsOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 12, 1, 1),
    _NsOspfExtLsdbType_Type()
)
nsOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExtLsdbType.setStatus("deprecated")
_NsOspfExtLsdbLsid_Type = IpAddress
_NsOspfExtLsdbLsid_Object = MibTableColumn
nsOspfExtLsdbLsid = _NsOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 12, 1, 2),
    _NsOspfExtLsdbLsid_Type()
)
nsOspfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExtLsdbLsid.setStatus("deprecated")
_NsOspfExtLsdbRouterId_Type = RouterID
_NsOspfExtLsdbRouterId_Object = MibTableColumn
nsOspfExtLsdbRouterId = _NsOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 12, 1, 3),
    _NsOspfExtLsdbRouterId_Type()
)
nsOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExtLsdbRouterId.setStatus("deprecated")
_NsOspfExtLsdbSequence_Type = Integer32
_NsOspfExtLsdbSequence_Object = MibTableColumn
nsOspfExtLsdbSequence = _NsOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 12, 1, 4),
    _NsOspfExtLsdbSequence_Type()
)
nsOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExtLsdbSequence.setStatus("deprecated")
_NsOspfExtLsdbAge_Type = Integer32
_NsOspfExtLsdbAge_Object = MibTableColumn
nsOspfExtLsdbAge = _NsOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 12, 1, 5),
    _NsOspfExtLsdbAge_Type()
)
nsOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExtLsdbAge.setStatus("deprecated")
_NsOspfExtLsdbChecksum_Type = Integer32
_NsOspfExtLsdbChecksum_Object = MibTableColumn
nsOspfExtLsdbChecksum = _NsOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 12, 1, 6),
    _NsOspfExtLsdbChecksum_Type()
)
nsOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExtLsdbChecksum.setStatus("deprecated")


class _NsOspfExtLsdbAdvertisement_Type(OctetString):
    """Custom type nsOspfExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )


_NsOspfExtLsdbAdvertisement_Type.__name__ = "OctetString"
_NsOspfExtLsdbAdvertisement_Object = MibTableColumn
nsOspfExtLsdbAdvertisement = _NsOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 12, 1, 7),
    _NsOspfExtLsdbAdvertisement_Type()
)
nsOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExtLsdbAdvertisement.setStatus("deprecated")


class _NsOspfExtLsdbVRID_Type(Integer32):
    """Custom type nsOspfExtLsdbVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfExtLsdbVRID_Type.__name__ = "Integer32"
_NsOspfExtLsdbVRID_Object = MibTableColumn
nsOspfExtLsdbVRID = _NsOspfExtLsdbVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 12, 1, 8),
    _NsOspfExtLsdbVRID_Type()
)
nsOspfExtLsdbVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfExtLsdbVRID.setStatus("deprecated")
_NsOspfAreaAggregateTable_Object = MibTable
nsOspfAreaAggregateTable = _NsOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 14)
)
if mibBuilder.loadTexts:
    nsOspfAreaAggregateTable.setStatus("deprecated")
_NsOspfAreaAggregateEntry_Object = MibTableRow
nsOspfAreaAggregateEntry = _NsOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 14, 1)
)
nsOspfAreaAggregateEntry.setIndexNames(
    (0, "NETSCREEN-OSPF-MIB", "nsOspfAreaAggregateAreaID"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfAreaAggregateLsdbType"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfAreaAggregateNet"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfAreaAggregateMask"),
    (0, "NETSCREEN-OSPF-MIB", "nsOspfAreaAggregateVRID"),
)
if mibBuilder.loadTexts:
    nsOspfAreaAggregateEntry.setStatus("deprecated")
_NsOspfAreaAggregateAreaID_Type = AreaID
_NsOspfAreaAggregateAreaID_Object = MibTableColumn
nsOspfAreaAggregateAreaID = _NsOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 14, 1, 1),
    _NsOspfAreaAggregateAreaID_Type()
)
nsOspfAreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAreaAggregateAreaID.setStatus("deprecated")


class _NsOspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type nsOspfAreaAggregateLsdbType based on Integer32"""
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


_NsOspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_NsOspfAreaAggregateLsdbType_Object = MibTableColumn
nsOspfAreaAggregateLsdbType = _NsOspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 14, 1, 2),
    _NsOspfAreaAggregateLsdbType_Type()
)
nsOspfAreaAggregateLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAreaAggregateLsdbType.setStatus("deprecated")
_NsOspfAreaAggregateNet_Type = IpAddress
_NsOspfAreaAggregateNet_Object = MibTableColumn
nsOspfAreaAggregateNet = _NsOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 14, 1, 3),
    _NsOspfAreaAggregateNet_Type()
)
nsOspfAreaAggregateNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAreaAggregateNet.setStatus("deprecated")
_NsOspfAreaAggregateMask_Type = IpAddress
_NsOspfAreaAggregateMask_Object = MibTableColumn
nsOspfAreaAggregateMask = _NsOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 14, 1, 4),
    _NsOspfAreaAggregateMask_Type()
)
nsOspfAreaAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAreaAggregateMask.setStatus("deprecated")
_NsOspfAreaAggregateStatus_Type = RowStatus
_NsOspfAreaAggregateStatus_Object = MibTableColumn
nsOspfAreaAggregateStatus = _NsOspfAreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 14, 1, 5),
    _NsOspfAreaAggregateStatus_Type()
)
nsOspfAreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfAreaAggregateStatus.setStatus("deprecated")


class _NsOspfAreaAggregateEffect_Type(Integer32):
    """Custom type nsOspfAreaAggregateEffect based on Integer32"""
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


_NsOspfAreaAggregateEffect_Type.__name__ = "Integer32"
_NsOspfAreaAggregateEffect_Object = MibTableColumn
nsOspfAreaAggregateEffect = _NsOspfAreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 14, 1, 6),
    _NsOspfAreaAggregateEffect_Type()
)
nsOspfAreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsOspfAreaAggregateEffect.setStatus("deprecated")


class _NsOspfAreaAggregateVRID_Type(Integer32):
    """Custom type nsOspfAreaAggregateVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsOspfAreaAggregateVRID_Type.__name__ = "Integer32"
_NsOspfAreaAggregateVRID_Object = MibTableColumn
nsOspfAreaAggregateVRID = _NsOspfAreaAggregateVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 2, 14, 1, 7),
    _NsOspfAreaAggregateVRID_Type()
)
nsOspfAreaAggregateVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsOspfAreaAggregateVRID.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-OSPF-MIB",
    **{"AreaID": AreaID,
       "RouterID": RouterID,
       "Metric": Metric,
       "BigMetric": BigMetric,
       "Status": Status,
       "PositiveInteger": PositiveInteger,
       "HelloRange": HelloRange,
       "UpToMaxAge": UpToMaxAge,
       "InterfaceIndex": InterfaceIndex,
       "DesignatedRouterPriority": DesignatedRouterPriority,
       "TOSType": TOSType,
       "nsOspf": nsOspf,
       "nsOspfGeneralTable": nsOspfGeneralTable,
       "nsOspfGeneralEntry": nsOspfGeneralEntry,
       "nsOspfRouterId": nsOspfRouterId,
       "nsOspfAdminStat": nsOspfAdminStat,
       "nsOspfVersionNumber": nsOspfVersionNumber,
       "nsOspfAreaBdrRtrStatus": nsOspfAreaBdrRtrStatus,
       "nsOspfASBdrRtrStatus": nsOspfASBdrRtrStatus,
       "nsOspfExternLsaCount": nsOspfExternLsaCount,
       "nsOspfExternLsaCksumSum": nsOspfExternLsaCksumSum,
       "nsOspfTOSSupport": nsOspfTOSSupport,
       "nsOspfOriginateNewLsas": nsOspfOriginateNewLsas,
       "nsOspfRxNewLsas": nsOspfRxNewLsas,
       "nsOspfExtLsdbLimit": nsOspfExtLsdbLimit,
       "nsOspfMulticastExtensions": nsOspfMulticastExtensions,
       "nsOspfExitOverflowInterval": nsOspfExitOverflowInterval,
       "nsOspfDemandExtensions": nsOspfDemandExtensions,
       "nsOspfGeneralVRID": nsOspfGeneralVRID,
       "nsOspfAreaTable": nsOspfAreaTable,
       "nsOspfAreaEntry": nsOspfAreaEntry,
       "nsOspfAreaId": nsOspfAreaId,
       "nsOspfImportAsExtern": nsOspfImportAsExtern,
       "nsOspfSpfRuns": nsOspfSpfRuns,
       "nsOspfAreaBdrRtrCount": nsOspfAreaBdrRtrCount,
       "nsOspfAsBdrRtrCount": nsOspfAsBdrRtrCount,
       "nsOspfAreaLsaCount": nsOspfAreaLsaCount,
       "nsOspfAreaLsaCksumSum": nsOspfAreaLsaCksumSum,
       "nsOspfAreaSummary": nsOspfAreaSummary,
       "nsOspfAreaStatus": nsOspfAreaStatus,
       "nsOspfAreaVRID": nsOspfAreaVRID,
       "nsOspfStubAreaTable": nsOspfStubAreaTable,
       "nsOspfStubAreaEntry": nsOspfStubAreaEntry,
       "nsOspfStubAreaId": nsOspfStubAreaId,
       "nsOspfStubTOS": nsOspfStubTOS,
       "nsOspfStubMetric": nsOspfStubMetric,
       "nsOspfStubStatus": nsOspfStubStatus,
       "nsOspfStubMetricType": nsOspfStubMetricType,
       "nsOspfStubVRID": nsOspfStubVRID,
       "nsOspfLsdbTable": nsOspfLsdbTable,
       "nsOspfLsdbEntry": nsOspfLsdbEntry,
       "nsOspfLsdbAreaId": nsOspfLsdbAreaId,
       "nsOspfLsdbType": nsOspfLsdbType,
       "nsOspfLsdbLsid": nsOspfLsdbLsid,
       "nsOspfLsdbRouterId": nsOspfLsdbRouterId,
       "nsOspfLsdbSequence": nsOspfLsdbSequence,
       "nsOspfLsdbAge": nsOspfLsdbAge,
       "nsOspfLsdbChecksum": nsOspfLsdbChecksum,
       "nsOspfLsdbAdvertisement": nsOspfLsdbAdvertisement,
       "nsOspfLsdbVRID": nsOspfLsdbVRID,
       "nsOspfHostTable": nsOspfHostTable,
       "nsOspfHostEntry": nsOspfHostEntry,
       "nsOspfHostIpAddress": nsOspfHostIpAddress,
       "nsOspfHostTOS": nsOspfHostTOS,
       "nsOspfHostMetric": nsOspfHostMetric,
       "nsOspfHostStatus": nsOspfHostStatus,
       "nsOspfHostAreaID": nsOspfHostAreaID,
       "nsOspfHostVRID": nsOspfHostVRID,
       "nsOspfIfTable": nsOspfIfTable,
       "nsOspfIfEntry": nsOspfIfEntry,
       "nsOspfIfIpAddress": nsOspfIfIpAddress,
       "nsOspfAddressLessIf": nsOspfAddressLessIf,
       "nsOspfIfAreaId": nsOspfIfAreaId,
       "nsOspfIfType": nsOspfIfType,
       "nsOspfIfAdminStat": nsOspfIfAdminStat,
       "nsOspfIfRtrPriority": nsOspfIfRtrPriority,
       "nsOspfIfTransitDelay": nsOspfIfTransitDelay,
       "nsOspfIfRetransInterval": nsOspfIfRetransInterval,
       "nsOspfIfHelloInterval": nsOspfIfHelloInterval,
       "nsOspfIfRtrDeadInterval": nsOspfIfRtrDeadInterval,
       "nsOspfIfPollInterval": nsOspfIfPollInterval,
       "nsOspfIfState": nsOspfIfState,
       "nsOspfIfDesignatedRouter": nsOspfIfDesignatedRouter,
       "nsOspfIfBackupDesignatedRouter": nsOspfIfBackupDesignatedRouter,
       "nsOspfIfEvents": nsOspfIfEvents,
       "nsOspfIfAuthKey": nsOspfIfAuthKey,
       "nsOspfIfStatus": nsOspfIfStatus,
       "nsOspfIfMulticastForwarding": nsOspfIfMulticastForwarding,
       "nsOspfIfDemand": nsOspfIfDemand,
       "nsOspfIfAuthType": nsOspfIfAuthType,
       "nsOspfIfVRID": nsOspfIfVRID,
       "nsOspfIfMetricTable": nsOspfIfMetricTable,
       "nsOspfIfMetricEntry": nsOspfIfMetricEntry,
       "nsOspfIfMetricIpAddress": nsOspfIfMetricIpAddress,
       "nsOspfIfMetricAddressLessIf": nsOspfIfMetricAddressLessIf,
       "nsOspfIfMetricTOS": nsOspfIfMetricTOS,
       "nsOspfIfMetricValue": nsOspfIfMetricValue,
       "nsOspfIfMetricStatus": nsOspfIfMetricStatus,
       "nsOspfIfMetricVRID": nsOspfIfMetricVRID,
       "nsOspfVirtIfTable": nsOspfVirtIfTable,
       "nsOspfVirtIfEntry": nsOspfVirtIfEntry,
       "nsOspfVirtIfAreaId": nsOspfVirtIfAreaId,
       "nsOspfVirtIfNeighbor": nsOspfVirtIfNeighbor,
       "nsOspfVirtIfTransitDelay": nsOspfVirtIfTransitDelay,
       "nsOspfVirtIfRetransInterval": nsOspfVirtIfRetransInterval,
       "nsOspfVirtIfHelloInterval": nsOspfVirtIfHelloInterval,
       "nsOspfVirtIfRtrDeadInterval": nsOspfVirtIfRtrDeadInterval,
       "nsOspfVirtIfState": nsOspfVirtIfState,
       "nsOspfVirtIfEvents": nsOspfVirtIfEvents,
       "nsOspfVirtIfAuthKey": nsOspfVirtIfAuthKey,
       "nsOspfVirtIfStatus": nsOspfVirtIfStatus,
       "nsOspfVirtIfAuthType": nsOspfVirtIfAuthType,
       "nsOspfVirtIfVRID": nsOspfVirtIfVRID,
       "nsOspfNbrTable": nsOspfNbrTable,
       "nsOspfNbrEntry": nsOspfNbrEntry,
       "nsOspfNbrIpAddr": nsOspfNbrIpAddr,
       "nsOspfNbrAddressLessIndex": nsOspfNbrAddressLessIndex,
       "nsOspfNbrRtrId": nsOspfNbrRtrId,
       "nsOspfNbrOptions": nsOspfNbrOptions,
       "nsOspfNbrPriority": nsOspfNbrPriority,
       "nsOspfNbrState": nsOspfNbrState,
       "nsOspfNbrEvents": nsOspfNbrEvents,
       "nsOspfNbrLsRetransQLen": nsOspfNbrLsRetransQLen,
       "nsOspfNbmaNbrStatus": nsOspfNbmaNbrStatus,
       "nsOspfNbmaNbrPermanence": nsOspfNbmaNbrPermanence,
       "nsOspfNbrHelloSuppressed": nsOspfNbrHelloSuppressed,
       "nsOspfNbrVRID": nsOspfNbrVRID,
       "nsOspfVirtNbrTable": nsOspfVirtNbrTable,
       "nsOspfVirtNbrEntry": nsOspfVirtNbrEntry,
       "nsOspfVirtNbrArea": nsOspfVirtNbrArea,
       "nsOspfVirtNbrRtrId": nsOspfVirtNbrRtrId,
       "nsOspfVirtNbrIpAddr": nsOspfVirtNbrIpAddr,
       "nsOspfVirtNbrOptions": nsOspfVirtNbrOptions,
       "nsOspfVirtNbrState": nsOspfVirtNbrState,
       "nsOspfVirtNbrEvents": nsOspfVirtNbrEvents,
       "nsOspfVirtNbrLsRetransQLen": nsOspfVirtNbrLsRetransQLen,
       "nsOspfVirtNbrHelloSuppressed": nsOspfVirtNbrHelloSuppressed,
       "nsOspfVirtNbrVRID": nsOspfVirtNbrVRID,
       "nsOspfExtLsdbTable": nsOspfExtLsdbTable,
       "nsOspfExtLsdbEntry": nsOspfExtLsdbEntry,
       "nsOspfExtLsdbType": nsOspfExtLsdbType,
       "nsOspfExtLsdbLsid": nsOspfExtLsdbLsid,
       "nsOspfExtLsdbRouterId": nsOspfExtLsdbRouterId,
       "nsOspfExtLsdbSequence": nsOspfExtLsdbSequence,
       "nsOspfExtLsdbAge": nsOspfExtLsdbAge,
       "nsOspfExtLsdbChecksum": nsOspfExtLsdbChecksum,
       "nsOspfExtLsdbAdvertisement": nsOspfExtLsdbAdvertisement,
       "nsOspfExtLsdbVRID": nsOspfExtLsdbVRID,
       "nsOspfAreaAggregateTable": nsOspfAreaAggregateTable,
       "nsOspfAreaAggregateEntry": nsOspfAreaAggregateEntry,
       "nsOspfAreaAggregateAreaID": nsOspfAreaAggregateAreaID,
       "nsOspfAreaAggregateLsdbType": nsOspfAreaAggregateLsdbType,
       "nsOspfAreaAggregateNet": nsOspfAreaAggregateNet,
       "nsOspfAreaAggregateMask": nsOspfAreaAggregateMask,
       "nsOspfAreaAggregateStatus": nsOspfAreaAggregateStatus,
       "nsOspfAreaAggregateEffect": nsOspfAreaAggregateEffect,
       "nsOspfAreaAggregateVRID": nsOspfAreaAggregateVRID}
)

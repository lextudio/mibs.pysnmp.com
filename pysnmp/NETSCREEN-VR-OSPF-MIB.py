# SNMP MIB module (NETSCREEN-VR-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VR-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:09 2024
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

nsVrOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AreaID(IpAddress, TextualConvention):
    status = "current"


class RouterID(IpAddress, TextualConvention):
    status = "current"


class Metric(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BigMetric(Integer32, TextualConvention):
    status = "current"
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
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class HelloRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class UpToMaxAge(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"


class DesignatedRouterPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TOSType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )



# MIB Managed Objects in the order of their OIDs

_NsVrOspfGeneralTable_Object = MibTable
nsVrOspfGeneralTable = _NsVrOspfGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1)
)
if mibBuilder.loadTexts:
    nsVrOspfGeneralTable.setStatus("current")
_NsVrOspfGeneralEntry_Object = MibTableRow
nsVrOspfGeneralEntry = _NsVrOspfGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1)
)
nsVrOspfGeneralEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfGeneralVRID"),
)
if mibBuilder.loadTexts:
    nsVrOspfGeneralEntry.setStatus("current")
_NsVrOspfRouterId_Type = RouterID
_NsVrOspfRouterId_Object = MibTableColumn
nsVrOspfRouterId = _NsVrOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 1),
    _NsVrOspfRouterId_Type()
)
nsVrOspfRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfRouterId.setStatus("current")
_NsVrOspfAdminStat_Type = Status
_NsVrOspfAdminStat_Object = MibTableColumn
nsVrOspfAdminStat = _NsVrOspfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 2),
    _NsVrOspfAdminStat_Type()
)
nsVrOspfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAdminStat.setStatus("current")


class _NsVrOspfVersionNumber_Type(Integer32):
    """Custom type nsVrOspfVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("version2", 2)
    )


_NsVrOspfVersionNumber_Type.__name__ = "Integer32"
_NsVrOspfVersionNumber_Object = MibTableColumn
nsVrOspfVersionNumber = _NsVrOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 3),
    _NsVrOspfVersionNumber_Type()
)
nsVrOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVersionNumber.setStatus("current")
_NsVrOspfAreaBdrRtrStatus_Type = TruthValue
_NsVrOspfAreaBdrRtrStatus_Object = MibTableColumn
nsVrOspfAreaBdrRtrStatus = _NsVrOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 4),
    _NsVrOspfAreaBdrRtrStatus_Type()
)
nsVrOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAreaBdrRtrStatus.setStatus("current")
_NsVrOspfASBdrRtrStatus_Type = TruthValue
_NsVrOspfASBdrRtrStatus_Object = MibTableColumn
nsVrOspfASBdrRtrStatus = _NsVrOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 5),
    _NsVrOspfASBdrRtrStatus_Type()
)
nsVrOspfASBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfASBdrRtrStatus.setStatus("current")
_NsVrOspfExternLsaCount_Type = Gauge32
_NsVrOspfExternLsaCount_Object = MibTableColumn
nsVrOspfExternLsaCount = _NsVrOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 6),
    _NsVrOspfExternLsaCount_Type()
)
nsVrOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExternLsaCount.setStatus("current")
_NsVrOspfExternLsaCksumSum_Type = Integer32
_NsVrOspfExternLsaCksumSum_Object = MibTableColumn
nsVrOspfExternLsaCksumSum = _NsVrOspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 7),
    _NsVrOspfExternLsaCksumSum_Type()
)
nsVrOspfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExternLsaCksumSum.setStatus("current")
_NsVrOspfTOSSupport_Type = TruthValue
_NsVrOspfTOSSupport_Object = MibTableColumn
nsVrOspfTOSSupport = _NsVrOspfTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 8),
    _NsVrOspfTOSSupport_Type()
)
nsVrOspfTOSSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfTOSSupport.setStatus("current")
_NsVrOspfOriginateNewLsas_Type = Counter32
_NsVrOspfOriginateNewLsas_Object = MibTableColumn
nsVrOspfOriginateNewLsas = _NsVrOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 9),
    _NsVrOspfOriginateNewLsas_Type()
)
nsVrOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfOriginateNewLsas.setStatus("current")
_NsVrOspfRxNewLsas_Type = Counter32
_NsVrOspfRxNewLsas_Object = MibTableColumn
nsVrOspfRxNewLsas = _NsVrOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 10),
    _NsVrOspfRxNewLsas_Type()
)
nsVrOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfRxNewLsas.setStatus("current")


class _NsVrOspfExtLsdbLimit_Type(Integer32):
    """Custom type nsVrOspfExtLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_NsVrOspfExtLsdbLimit_Type.__name__ = "Integer32"
_NsVrOspfExtLsdbLimit_Object = MibTableColumn
nsVrOspfExtLsdbLimit = _NsVrOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 11),
    _NsVrOspfExtLsdbLimit_Type()
)
nsVrOspfExtLsdbLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExtLsdbLimit.setStatus("current")


class _NsVrOspfMulticastExtensions_Type(Integer32):
    """Custom type nsVrOspfMulticastExtensions based on Integer32"""
    defaultValue = 0


_NsVrOspfMulticastExtensions_Object = MibTableColumn
nsVrOspfMulticastExtensions = _NsVrOspfMulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 12),
    _NsVrOspfMulticastExtensions_Type()
)
nsVrOspfMulticastExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfMulticastExtensions.setStatus("current")


class _NsVrOspfExitOverflowInterval_Type(PositiveInteger):
    """Custom type nsVrOspfExitOverflowInterval based on PositiveInteger"""
    defaultValue = 0


_NsVrOspfExitOverflowInterval_Object = MibTableColumn
nsVrOspfExitOverflowInterval = _NsVrOspfExitOverflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 13),
    _NsVrOspfExitOverflowInterval_Type()
)
nsVrOspfExitOverflowInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExitOverflowInterval.setStatus("current")
_NsVrOspfDemandExtensions_Type = TruthValue
_NsVrOspfDemandExtensions_Object = MibTableColumn
nsVrOspfDemandExtensions = _NsVrOspfDemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 14),
    _NsVrOspfDemandExtensions_Type()
)
nsVrOspfDemandExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfDemandExtensions.setStatus("current")


class _NsVrOspfGeneralVRID_Type(Integer32):
    """Custom type nsVrOspfGeneralVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfGeneralVRID_Type.__name__ = "Integer32"
_NsVrOspfGeneralVRID_Object = MibTableColumn
nsVrOspfGeneralVRID = _NsVrOspfGeneralVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 1, 1, 15),
    _NsVrOspfGeneralVRID_Type()
)
nsVrOspfGeneralVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfGeneralVRID.setStatus("current")
_NsVrOspfAreaTable_Object = MibTable
nsVrOspfAreaTable = _NsVrOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2)
)
if mibBuilder.loadTexts:
    nsVrOspfAreaTable.setStatus("current")
_NsVrOspfAreaEntry_Object = MibTableRow
nsVrOspfAreaEntry = _NsVrOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2, 1)
)
nsVrOspfAreaEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfAreaVRID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfAreaId"),
)
if mibBuilder.loadTexts:
    nsVrOspfAreaEntry.setStatus("current")
_NsVrOspfAreaId_Type = AreaID
_NsVrOspfAreaId_Object = MibTableColumn
nsVrOspfAreaId = _NsVrOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2, 1, 1),
    _NsVrOspfAreaId_Type()
)
nsVrOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAreaId.setStatus("current")


class _NsVrOspfImportAsExtern_Type(Integer32):
    """Custom type nsVrOspfImportAsExtern based on Integer32"""
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


_NsVrOspfImportAsExtern_Type.__name__ = "Integer32"
_NsVrOspfImportAsExtern_Object = MibTableColumn
nsVrOspfImportAsExtern = _NsVrOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2, 1, 3),
    _NsVrOspfImportAsExtern_Type()
)
nsVrOspfImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfImportAsExtern.setStatus("current")
_NsVrOspfSpfRuns_Type = Counter32
_NsVrOspfSpfRuns_Object = MibTableColumn
nsVrOspfSpfRuns = _NsVrOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2, 1, 4),
    _NsVrOspfSpfRuns_Type()
)
nsVrOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfSpfRuns.setStatus("current")
_NsVrOspfAreaBdrRtrCount_Type = Gauge32
_NsVrOspfAreaBdrRtrCount_Object = MibTableColumn
nsVrOspfAreaBdrRtrCount = _NsVrOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2, 1, 5),
    _NsVrOspfAreaBdrRtrCount_Type()
)
nsVrOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAreaBdrRtrCount.setStatus("current")
_NsVrOspfAsBdrRtrCount_Type = Gauge32
_NsVrOspfAsBdrRtrCount_Object = MibTableColumn
nsVrOspfAsBdrRtrCount = _NsVrOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2, 1, 6),
    _NsVrOspfAsBdrRtrCount_Type()
)
nsVrOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAsBdrRtrCount.setStatus("current")
_NsVrOspfAreaLsaCount_Type = Gauge32
_NsVrOspfAreaLsaCount_Object = MibTableColumn
nsVrOspfAreaLsaCount = _NsVrOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2, 1, 7),
    _NsVrOspfAreaLsaCount_Type()
)
nsVrOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAreaLsaCount.setStatus("current")


class _NsVrOspfAreaLsaCksumSum_Type(Integer32):
    """Custom type nsVrOspfAreaLsaCksumSum based on Integer32"""
    defaultValue = 0


_NsVrOspfAreaLsaCksumSum_Object = MibTableColumn
nsVrOspfAreaLsaCksumSum = _NsVrOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2, 1, 8),
    _NsVrOspfAreaLsaCksumSum_Type()
)
nsVrOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAreaLsaCksumSum.setStatus("current")


class _NsVrOspfAreaSummary_Type(Integer32):
    """Custom type nsVrOspfAreaSummary based on Integer32"""
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


_NsVrOspfAreaSummary_Type.__name__ = "Integer32"
_NsVrOspfAreaSummary_Object = MibTableColumn
nsVrOspfAreaSummary = _NsVrOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2, 1, 9),
    _NsVrOspfAreaSummary_Type()
)
nsVrOspfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfAreaSummary.setStatus("current")
_NsVrOspfAreaStatus_Type = RowStatus
_NsVrOspfAreaStatus_Object = MibTableColumn
nsVrOspfAreaStatus = _NsVrOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2, 1, 10),
    _NsVrOspfAreaStatus_Type()
)
nsVrOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfAreaStatus.setStatus("current")


class _NsVrOspfAreaVRID_Type(Integer32):
    """Custom type nsVrOspfAreaVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfAreaVRID_Type.__name__ = "Integer32"
_NsVrOspfAreaVRID_Object = MibTableColumn
nsVrOspfAreaVRID = _NsVrOspfAreaVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 2, 1, 11),
    _NsVrOspfAreaVRID_Type()
)
nsVrOspfAreaVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAreaVRID.setStatus("current")
_NsVrOspfStubAreaTable_Object = MibTable
nsVrOspfStubAreaTable = _NsVrOspfStubAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 3)
)
if mibBuilder.loadTexts:
    nsVrOspfStubAreaTable.setStatus("current")
_NsVrOspfStubAreaEntry_Object = MibTableRow
nsVrOspfStubAreaEntry = _NsVrOspfStubAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 3, 1)
)
nsVrOspfStubAreaEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfStubVRID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfStubAreaId"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfStubTOS"),
)
if mibBuilder.loadTexts:
    nsVrOspfStubAreaEntry.setStatus("current")
_NsVrOspfStubAreaId_Type = AreaID
_NsVrOspfStubAreaId_Object = MibTableColumn
nsVrOspfStubAreaId = _NsVrOspfStubAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 3, 1, 1),
    _NsVrOspfStubAreaId_Type()
)
nsVrOspfStubAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfStubAreaId.setStatus("current")
_NsVrOspfStubTOS_Type = TOSType
_NsVrOspfStubTOS_Object = MibTableColumn
nsVrOspfStubTOS = _NsVrOspfStubTOS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 3, 1, 2),
    _NsVrOspfStubTOS_Type()
)
nsVrOspfStubTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfStubTOS.setStatus("current")
_NsVrOspfStubMetric_Type = BigMetric
_NsVrOspfStubMetric_Object = MibTableColumn
nsVrOspfStubMetric = _NsVrOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 3, 1, 3),
    _NsVrOspfStubMetric_Type()
)
nsVrOspfStubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfStubMetric.setStatus("current")
_NsVrOspfStubStatus_Type = RowStatus
_NsVrOspfStubStatus_Object = MibTableColumn
nsVrOspfStubStatus = _NsVrOspfStubStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 3, 1, 4),
    _NsVrOspfStubStatus_Type()
)
nsVrOspfStubStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfStubStatus.setStatus("current")


class _NsVrOspfStubMetricType_Type(Integer32):
    """Custom type nsVrOspfStubMetricType based on Integer32"""
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
          ("nsVrOspfMetric", 1))
    )


_NsVrOspfStubMetricType_Type.__name__ = "Integer32"
_NsVrOspfStubMetricType_Object = MibTableColumn
nsVrOspfStubMetricType = _NsVrOspfStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 3, 1, 5),
    _NsVrOspfStubMetricType_Type()
)
nsVrOspfStubMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfStubMetricType.setStatus("current")


class _NsVrOspfStubVRID_Type(Integer32):
    """Custom type nsVrOspfStubVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfStubVRID_Type.__name__ = "Integer32"
_NsVrOspfStubVRID_Object = MibTableColumn
nsVrOspfStubVRID = _NsVrOspfStubVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 3, 1, 6),
    _NsVrOspfStubVRID_Type()
)
nsVrOspfStubVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfStubVRID.setStatus("current")
_NsVrOspfLsdbTable_Object = MibTable
nsVrOspfLsdbTable = _NsVrOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 4)
)
if mibBuilder.loadTexts:
    nsVrOspfLsdbTable.setStatus("current")
_NsVrOspfLsdbEntry_Object = MibTableRow
nsVrOspfLsdbEntry = _NsVrOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 4, 1)
)
nsVrOspfLsdbEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfLsdbVRID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfLsdbAreaId"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfLsdbType"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfLsdbLsid"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    nsVrOspfLsdbEntry.setStatus("current")
_NsVrOspfLsdbAreaId_Type = AreaID
_NsVrOspfLsdbAreaId_Object = MibTableColumn
nsVrOspfLsdbAreaId = _NsVrOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 4, 1, 1),
    _NsVrOspfLsdbAreaId_Type()
)
nsVrOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfLsdbAreaId.setStatus("current")


class _NsVrOspfLsdbType_Type(Integer32):
    """Custom type nsVrOspfLsdbType based on Integer32"""
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


_NsVrOspfLsdbType_Type.__name__ = "Integer32"
_NsVrOspfLsdbType_Object = MibTableColumn
nsVrOspfLsdbType = _NsVrOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 4, 1, 2),
    _NsVrOspfLsdbType_Type()
)
nsVrOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfLsdbType.setStatus("current")
_NsVrOspfLsdbLsid_Type = IpAddress
_NsVrOspfLsdbLsid_Object = MibTableColumn
nsVrOspfLsdbLsid = _NsVrOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 4, 1, 3),
    _NsVrOspfLsdbLsid_Type()
)
nsVrOspfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfLsdbLsid.setStatus("current")
_NsVrOspfLsdbRouterId_Type = RouterID
_NsVrOspfLsdbRouterId_Object = MibTableColumn
nsVrOspfLsdbRouterId = _NsVrOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 4, 1, 4),
    _NsVrOspfLsdbRouterId_Type()
)
nsVrOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfLsdbRouterId.setStatus("current")
_NsVrOspfLsdbSequence_Type = Integer32
_NsVrOspfLsdbSequence_Object = MibTableColumn
nsVrOspfLsdbSequence = _NsVrOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 4, 1, 5),
    _NsVrOspfLsdbSequence_Type()
)
nsVrOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfLsdbSequence.setStatus("current")
_NsVrOspfLsdbAge_Type = Integer32
_NsVrOspfLsdbAge_Object = MibTableColumn
nsVrOspfLsdbAge = _NsVrOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 4, 1, 6),
    _NsVrOspfLsdbAge_Type()
)
nsVrOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfLsdbAge.setStatus("current")
_NsVrOspfLsdbChecksum_Type = Integer32
_NsVrOspfLsdbChecksum_Object = MibTableColumn
nsVrOspfLsdbChecksum = _NsVrOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 4, 1, 7),
    _NsVrOspfLsdbChecksum_Type()
)
nsVrOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfLsdbChecksum.setStatus("current")


class _NsVrOspfLsdbAdvertisement_Type(OctetString):
    """Custom type nsVrOspfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_NsVrOspfLsdbAdvertisement_Type.__name__ = "OctetString"
_NsVrOspfLsdbAdvertisement_Object = MibTableColumn
nsVrOspfLsdbAdvertisement = _NsVrOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 4, 1, 8),
    _NsVrOspfLsdbAdvertisement_Type()
)
nsVrOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfLsdbAdvertisement.setStatus("current")


class _NsVrOspfLsdbVRID_Type(Integer32):
    """Custom type nsVrOspfLsdbVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfLsdbVRID_Type.__name__ = "Integer32"
_NsVrOspfLsdbVRID_Object = MibTableColumn
nsVrOspfLsdbVRID = _NsVrOspfLsdbVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 4, 1, 9),
    _NsVrOspfLsdbVRID_Type()
)
nsVrOspfLsdbVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfLsdbVRID.setStatus("current")
_NsVrOspfHostTable_Object = MibTable
nsVrOspfHostTable = _NsVrOspfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 6)
)
if mibBuilder.loadTexts:
    nsVrOspfHostTable.setStatus("current")
_NsVrOspfHostEntry_Object = MibTableRow
nsVrOspfHostEntry = _NsVrOspfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 6, 1)
)
nsVrOspfHostEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfHostVRID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfHostIpAddress"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfHostTOS"),
)
if mibBuilder.loadTexts:
    nsVrOspfHostEntry.setStatus("current")
_NsVrOspfHostIpAddress_Type = IpAddress
_NsVrOspfHostIpAddress_Object = MibTableColumn
nsVrOspfHostIpAddress = _NsVrOspfHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 6, 1, 1),
    _NsVrOspfHostIpAddress_Type()
)
nsVrOspfHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfHostIpAddress.setStatus("current")
_NsVrOspfHostTOS_Type = TOSType
_NsVrOspfHostTOS_Object = MibTableColumn
nsVrOspfHostTOS = _NsVrOspfHostTOS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 6, 1, 2),
    _NsVrOspfHostTOS_Type()
)
nsVrOspfHostTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfHostTOS.setStatus("current")
_NsVrOspfHostMetric_Type = Metric
_NsVrOspfHostMetric_Object = MibTableColumn
nsVrOspfHostMetric = _NsVrOspfHostMetric_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 6, 1, 3),
    _NsVrOspfHostMetric_Type()
)
nsVrOspfHostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfHostMetric.setStatus("current")
_NsVrOspfHostStatus_Type = RowStatus
_NsVrOspfHostStatus_Object = MibTableColumn
nsVrOspfHostStatus = _NsVrOspfHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 6, 1, 4),
    _NsVrOspfHostStatus_Type()
)
nsVrOspfHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfHostStatus.setStatus("current")
_NsVrOspfHostAreaID_Type = AreaID
_NsVrOspfHostAreaID_Object = MibTableColumn
nsVrOspfHostAreaID = _NsVrOspfHostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 6, 1, 5),
    _NsVrOspfHostAreaID_Type()
)
nsVrOspfHostAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfHostAreaID.setStatus("current")


class _NsVrOspfHostVRID_Type(Integer32):
    """Custom type nsVrOspfHostVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfHostVRID_Type.__name__ = "Integer32"
_NsVrOspfHostVRID_Object = MibTableColumn
nsVrOspfHostVRID = _NsVrOspfHostVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 6, 1, 6),
    _NsVrOspfHostVRID_Type()
)
nsVrOspfHostVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfHostVRID.setStatus("current")
_NsVrOspfIfTable_Object = MibTable
nsVrOspfIfTable = _NsVrOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7)
)
if mibBuilder.loadTexts:
    nsVrOspfIfTable.setStatus("current")
_NsVrOspfIfEntry_Object = MibTableRow
nsVrOspfIfEntry = _NsVrOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1)
)
nsVrOspfIfEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfIfVRID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfIfIpAddress"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    nsVrOspfIfEntry.setStatus("current")
_NsVrOspfIfIpAddress_Type = IpAddress
_NsVrOspfIfIpAddress_Object = MibTableColumn
nsVrOspfIfIpAddress = _NsVrOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 1),
    _NsVrOspfIfIpAddress_Type()
)
nsVrOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfIfIpAddress.setStatus("current")
_NsVrOspfAddressLessIf_Type = Integer32
_NsVrOspfAddressLessIf_Object = MibTableColumn
nsVrOspfAddressLessIf = _NsVrOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 2),
    _NsVrOspfAddressLessIf_Type()
)
nsVrOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAddressLessIf.setStatus("current")


class _NsVrOspfIfAreaId_Type(AreaID):
    """Custom type nsVrOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_NsVrOspfIfAreaId_Object = MibTableColumn
nsVrOspfIfAreaId = _NsVrOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 3),
    _NsVrOspfIfAreaId_Type()
)
nsVrOspfIfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfAreaId.setStatus("current")


class _NsVrOspfIfType_Type(Integer32):
    """Custom type nsVrOspfIfType based on Integer32"""
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


_NsVrOspfIfType_Type.__name__ = "Integer32"
_NsVrOspfIfType_Object = MibTableColumn
nsVrOspfIfType = _NsVrOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 4),
    _NsVrOspfIfType_Type()
)
nsVrOspfIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfType.setStatus("current")


class _NsVrOspfIfAdminStat_Type(Status):
    """Custom type nsVrOspfIfAdminStat based on Status"""


_NsVrOspfIfAdminStat_Object = MibTableColumn
nsVrOspfIfAdminStat = _NsVrOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 5),
    _NsVrOspfIfAdminStat_Type()
)
nsVrOspfIfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfAdminStat.setStatus("current")


class _NsVrOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type nsVrOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_NsVrOspfIfRtrPriority_Object = MibTableColumn
nsVrOspfIfRtrPriority = _NsVrOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 6),
    _NsVrOspfIfRtrPriority_Type()
)
nsVrOspfIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfRtrPriority.setStatus("current")


class _NsVrOspfIfTransitDelay_Type(UpToMaxAge):
    """Custom type nsVrOspfIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_NsVrOspfIfTransitDelay_Object = MibTableColumn
nsVrOspfIfTransitDelay = _NsVrOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 7),
    _NsVrOspfIfTransitDelay_Type()
)
nsVrOspfIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfTransitDelay.setStatus("current")


class _NsVrOspfIfRetransInterval_Type(UpToMaxAge):
    """Custom type nsVrOspfIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_NsVrOspfIfRetransInterval_Object = MibTableColumn
nsVrOspfIfRetransInterval = _NsVrOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 8),
    _NsVrOspfIfRetransInterval_Type()
)
nsVrOspfIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfRetransInterval.setStatus("current")


class _NsVrOspfIfHelloInterval_Type(HelloRange):
    """Custom type nsVrOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_NsVrOspfIfHelloInterval_Object = MibTableColumn
nsVrOspfIfHelloInterval = _NsVrOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 9),
    _NsVrOspfIfHelloInterval_Type()
)
nsVrOspfIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfHelloInterval.setStatus("current")


class _NsVrOspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type nsVrOspfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_NsVrOspfIfRtrDeadInterval_Object = MibTableColumn
nsVrOspfIfRtrDeadInterval = _NsVrOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 10),
    _NsVrOspfIfRtrDeadInterval_Type()
)
nsVrOspfIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfRtrDeadInterval.setStatus("current")


class _NsVrOspfIfPollInterval_Type(PositiveInteger):
    """Custom type nsVrOspfIfPollInterval based on PositiveInteger"""
    defaultValue = 120


_NsVrOspfIfPollInterval_Object = MibTableColumn
nsVrOspfIfPollInterval = _NsVrOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 11),
    _NsVrOspfIfPollInterval_Type()
)
nsVrOspfIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfPollInterval.setStatus("current")


class _NsVrOspfIfState_Type(Integer32):
    """Custom type nsVrOspfIfState based on Integer32"""
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


_NsVrOspfIfState_Type.__name__ = "Integer32"
_NsVrOspfIfState_Object = MibTableColumn
nsVrOspfIfState = _NsVrOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 12),
    _NsVrOspfIfState_Type()
)
nsVrOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfIfState.setStatus("current")


class _NsVrOspfIfDesignatedRouter_Type(IpAddress):
    """Custom type nsVrOspfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_NsVrOspfIfDesignatedRouter_Object = MibTableColumn
nsVrOspfIfDesignatedRouter = _NsVrOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 13),
    _NsVrOspfIfDesignatedRouter_Type()
)
nsVrOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfIfDesignatedRouter.setStatus("current")


class _NsVrOspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type nsVrOspfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_NsVrOspfIfBackupDesignatedRouter_Object = MibTableColumn
nsVrOspfIfBackupDesignatedRouter = _NsVrOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 14),
    _NsVrOspfIfBackupDesignatedRouter_Type()
)
nsVrOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfIfBackupDesignatedRouter.setStatus("current")
_NsVrOspfIfEvents_Type = Counter32
_NsVrOspfIfEvents_Object = MibTableColumn
nsVrOspfIfEvents = _NsVrOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 15),
    _NsVrOspfIfEvents_Type()
)
nsVrOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfIfEvents.setStatus("current")


class _NsVrOspfIfAuthKey_Type(OctetString):
    """Custom type nsVrOspfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NsVrOspfIfAuthKey_Type.__name__ = "OctetString"
_NsVrOspfIfAuthKey_Object = MibTableColumn
nsVrOspfIfAuthKey = _NsVrOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 16),
    _NsVrOspfIfAuthKey_Type()
)
nsVrOspfIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfAuthKey.setStatus("current")
_NsVrOspfIfStatus_Type = RowStatus
_NsVrOspfIfStatus_Object = MibTableColumn
nsVrOspfIfStatus = _NsVrOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 17),
    _NsVrOspfIfStatus_Type()
)
nsVrOspfIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfStatus.setStatus("current")


class _NsVrOspfIfMulticastForwarding_Type(Integer32):
    """Custom type nsVrOspfIfMulticastForwarding based on Integer32"""
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


_NsVrOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_NsVrOspfIfMulticastForwarding_Object = MibTableColumn
nsVrOspfIfMulticastForwarding = _NsVrOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 18),
    _NsVrOspfIfMulticastForwarding_Type()
)
nsVrOspfIfMulticastForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfMulticastForwarding.setStatus("current")


class _NsVrOspfIfDemand_Type(TruthValue):
    """Custom type nsVrOspfIfDemand based on TruthValue"""


_NsVrOspfIfDemand_Object = MibTableColumn
nsVrOspfIfDemand = _NsVrOspfIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 19),
    _NsVrOspfIfDemand_Type()
)
nsVrOspfIfDemand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfDemand.setStatus("current")


class _NsVrOspfIfAuthType_Type(Integer32):
    """Custom type nsVrOspfIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NsVrOspfIfAuthType_Type.__name__ = "Integer32"
_NsVrOspfIfAuthType_Object = MibTableColumn
nsVrOspfIfAuthType = _NsVrOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 20),
    _NsVrOspfIfAuthType_Type()
)
nsVrOspfIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfAuthType.setStatus("current")


class _NsVrOspfIfVRID_Type(Integer32):
    """Custom type nsVrOspfIfVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfIfVRID_Type.__name__ = "Integer32"
_NsVrOspfIfVRID_Object = MibTableColumn
nsVrOspfIfVRID = _NsVrOspfIfVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 7, 1, 21),
    _NsVrOspfIfVRID_Type()
)
nsVrOspfIfVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfIfVRID.setStatus("current")
_NsVrOspfIfMetricTable_Object = MibTable
nsVrOspfIfMetricTable = _NsVrOspfIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 8)
)
if mibBuilder.loadTexts:
    nsVrOspfIfMetricTable.setStatus("current")
_NsVrOspfIfMetricEntry_Object = MibTableRow
nsVrOspfIfMetricEntry = _NsVrOspfIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 8, 1)
)
nsVrOspfIfMetricEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfIfMetricVRID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfIfMetricIpAddress"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfIfMetricAddressLessIf"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfIfMetricTOS"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfIfMetricVRID"),
)
if mibBuilder.loadTexts:
    nsVrOspfIfMetricEntry.setStatus("current")
_NsVrOspfIfMetricIpAddress_Type = IpAddress
_NsVrOspfIfMetricIpAddress_Object = MibTableColumn
nsVrOspfIfMetricIpAddress = _NsVrOspfIfMetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 8, 1, 1),
    _NsVrOspfIfMetricIpAddress_Type()
)
nsVrOspfIfMetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfIfMetricIpAddress.setStatus("current")
_NsVrOspfIfMetricAddressLessIf_Type = Integer32
_NsVrOspfIfMetricAddressLessIf_Object = MibTableColumn
nsVrOspfIfMetricAddressLessIf = _NsVrOspfIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 8, 1, 2),
    _NsVrOspfIfMetricAddressLessIf_Type()
)
nsVrOspfIfMetricAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfIfMetricAddressLessIf.setStatus("current")
_NsVrOspfIfMetricTOS_Type = TOSType
_NsVrOspfIfMetricTOS_Object = MibTableColumn
nsVrOspfIfMetricTOS = _NsVrOspfIfMetricTOS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 8, 1, 3),
    _NsVrOspfIfMetricTOS_Type()
)
nsVrOspfIfMetricTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfIfMetricTOS.setStatus("current")
_NsVrOspfIfMetricValue_Type = Metric
_NsVrOspfIfMetricValue_Object = MibTableColumn
nsVrOspfIfMetricValue = _NsVrOspfIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 8, 1, 4),
    _NsVrOspfIfMetricValue_Type()
)
nsVrOspfIfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfMetricValue.setStatus("current")
_NsVrOspfIfMetricStatus_Type = RowStatus
_NsVrOspfIfMetricStatus_Object = MibTableColumn
nsVrOspfIfMetricStatus = _NsVrOspfIfMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 8, 1, 5),
    _NsVrOspfIfMetricStatus_Type()
)
nsVrOspfIfMetricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfIfMetricStatus.setStatus("current")


class _NsVrOspfIfMetricVRID_Type(Integer32):
    """Custom type nsVrOspfIfMetricVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfIfMetricVRID_Type.__name__ = "Integer32"
_NsVrOspfIfMetricVRID_Object = MibTableColumn
nsVrOspfIfMetricVRID = _NsVrOspfIfMetricVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 8, 1, 6),
    _NsVrOspfIfMetricVRID_Type()
)
nsVrOspfIfMetricVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfIfMetricVRID.setStatus("current")
_NsVrOspfVirtIfTable_Object = MibTable
nsVrOspfVirtIfTable = _NsVrOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9)
)
if mibBuilder.loadTexts:
    nsVrOspfVirtIfTable.setStatus("current")
_NsVrOspfVirtIfEntry_Object = MibTableRow
nsVrOspfVirtIfEntry = _NsVrOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1)
)
nsVrOspfVirtIfEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfVirtIfVRID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfVirtIfAreaId"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    nsVrOspfVirtIfEntry.setStatus("current")
_NsVrOspfVirtIfAreaId_Type = AreaID
_NsVrOspfVirtIfAreaId_Object = MibTableColumn
nsVrOspfVirtIfAreaId = _NsVrOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 1),
    _NsVrOspfVirtIfAreaId_Type()
)
nsVrOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfAreaId.setStatus("current")
_NsVrOspfVirtIfNeighbor_Type = RouterID
_NsVrOspfVirtIfNeighbor_Object = MibTableColumn
nsVrOspfVirtIfNeighbor = _NsVrOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 2),
    _NsVrOspfVirtIfNeighbor_Type()
)
nsVrOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfNeighbor.setStatus("current")


class _NsVrOspfVirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type nsVrOspfVirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_NsVrOspfVirtIfTransitDelay_Object = MibTableColumn
nsVrOspfVirtIfTransitDelay = _NsVrOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 3),
    _NsVrOspfVirtIfTransitDelay_Type()
)
nsVrOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfTransitDelay.setStatus("current")


class _NsVrOspfVirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type nsVrOspfVirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_NsVrOspfVirtIfRetransInterval_Object = MibTableColumn
nsVrOspfVirtIfRetransInterval = _NsVrOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 4),
    _NsVrOspfVirtIfRetransInterval_Type()
)
nsVrOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfRetransInterval.setStatus("current")


class _NsVrOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type nsVrOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_NsVrOspfVirtIfHelloInterval_Object = MibTableColumn
nsVrOspfVirtIfHelloInterval = _NsVrOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 5),
    _NsVrOspfVirtIfHelloInterval_Type()
)
nsVrOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfHelloInterval.setStatus("current")


class _NsVrOspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type nsVrOspfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 60


_NsVrOspfVirtIfRtrDeadInterval_Object = MibTableColumn
nsVrOspfVirtIfRtrDeadInterval = _NsVrOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 6),
    _NsVrOspfVirtIfRtrDeadInterval_Type()
)
nsVrOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfRtrDeadInterval.setStatus("current")


class _NsVrOspfVirtIfState_Type(Integer32):
    """Custom type nsVrOspfVirtIfState based on Integer32"""
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


_NsVrOspfVirtIfState_Type.__name__ = "Integer32"
_NsVrOspfVirtIfState_Object = MibTableColumn
nsVrOspfVirtIfState = _NsVrOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 7),
    _NsVrOspfVirtIfState_Type()
)
nsVrOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfState.setStatus("current")
_NsVrOspfVirtIfEvents_Type = Counter32
_NsVrOspfVirtIfEvents_Object = MibTableColumn
nsVrOspfVirtIfEvents = _NsVrOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 8),
    _NsVrOspfVirtIfEvents_Type()
)
nsVrOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfEvents.setStatus("current")


class _NsVrOspfVirtIfAuthKey_Type(OctetString):
    """Custom type nsVrOspfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_NsVrOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_NsVrOspfVirtIfAuthKey_Object = MibTableColumn
nsVrOspfVirtIfAuthKey = _NsVrOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 9),
    _NsVrOspfVirtIfAuthKey_Type()
)
nsVrOspfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfAuthKey.setStatus("current")
_NsVrOspfVirtIfStatus_Type = RowStatus
_NsVrOspfVirtIfStatus_Object = MibTableColumn
nsVrOspfVirtIfStatus = _NsVrOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 10),
    _NsVrOspfVirtIfStatus_Type()
)
nsVrOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfStatus.setStatus("current")


class _NsVrOspfVirtIfAuthType_Type(Integer32):
    """Custom type nsVrOspfVirtIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NsVrOspfVirtIfAuthType_Type.__name__ = "Integer32"
_NsVrOspfVirtIfAuthType_Object = MibTableColumn
nsVrOspfVirtIfAuthType = _NsVrOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 11),
    _NsVrOspfVirtIfAuthType_Type()
)
nsVrOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfAuthType.setStatus("current")


class _NsVrOspfVirtIfVRID_Type(Integer32):
    """Custom type nsVrOspfVirtIfVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfVirtIfVRID_Type.__name__ = "Integer32"
_NsVrOspfVirtIfVRID_Object = MibTableColumn
nsVrOspfVirtIfVRID = _NsVrOspfVirtIfVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 9, 1, 12),
    _NsVrOspfVirtIfVRID_Type()
)
nsVrOspfVirtIfVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtIfVRID.setStatus("current")
_NsVrOspfNbrTable_Object = MibTable
nsVrOspfNbrTable = _NsVrOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10)
)
if mibBuilder.loadTexts:
    nsVrOspfNbrTable.setStatus("current")
_NsVrOspfNbrEntry_Object = MibTableRow
nsVrOspfNbrEntry = _NsVrOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1)
)
nsVrOspfNbrEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfNbrVRID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfNbrIpAddr"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    nsVrOspfNbrEntry.setStatus("current")
_NsVrOspfNbrIpAddr_Type = IpAddress
_NsVrOspfNbrIpAddr_Object = MibTableColumn
nsVrOspfNbrIpAddr = _NsVrOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 1),
    _NsVrOspfNbrIpAddr_Type()
)
nsVrOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfNbrIpAddr.setStatus("current")
_NsVrOspfNbrAddressLessIndex_Type = InterfaceIndex
_NsVrOspfNbrAddressLessIndex_Object = MibTableColumn
nsVrOspfNbrAddressLessIndex = _NsVrOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 2),
    _NsVrOspfNbrAddressLessIndex_Type()
)
nsVrOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfNbrAddressLessIndex.setStatus("current")


class _NsVrOspfNbrRtrId_Type(RouterID):
    """Custom type nsVrOspfNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_NsVrOspfNbrRtrId_Object = MibTableColumn
nsVrOspfNbrRtrId = _NsVrOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 3),
    _NsVrOspfNbrRtrId_Type()
)
nsVrOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfNbrRtrId.setStatus("current")


class _NsVrOspfNbrOptions_Type(Integer32):
    """Custom type nsVrOspfNbrOptions based on Integer32"""
    defaultValue = 0


_NsVrOspfNbrOptions_Object = MibTableColumn
nsVrOspfNbrOptions = _NsVrOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 4),
    _NsVrOspfNbrOptions_Type()
)
nsVrOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfNbrOptions.setStatus("current")


class _NsVrOspfNbrPriority_Type(DesignatedRouterPriority):
    """Custom type nsVrOspfNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_NsVrOspfNbrPriority_Object = MibTableColumn
nsVrOspfNbrPriority = _NsVrOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 5),
    _NsVrOspfNbrPriority_Type()
)
nsVrOspfNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfNbrPriority.setStatus("current")


class _NsVrOspfNbrState_Type(Integer32):
    """Custom type nsVrOspfNbrState based on Integer32"""
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


_NsVrOspfNbrState_Type.__name__ = "Integer32"
_NsVrOspfNbrState_Object = MibTableColumn
nsVrOspfNbrState = _NsVrOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 6),
    _NsVrOspfNbrState_Type()
)
nsVrOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfNbrState.setStatus("current")
_NsVrOspfNbrEvents_Type = Counter32
_NsVrOspfNbrEvents_Object = MibTableColumn
nsVrOspfNbrEvents = _NsVrOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 7),
    _NsVrOspfNbrEvents_Type()
)
nsVrOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfNbrEvents.setStatus("current")
_NsVrOspfNbrLsRetransQLen_Type = Gauge32
_NsVrOspfNbrLsRetransQLen_Object = MibTableColumn
nsVrOspfNbrLsRetransQLen = _NsVrOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 8),
    _NsVrOspfNbrLsRetransQLen_Type()
)
nsVrOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfNbrLsRetransQLen.setStatus("current")
_NsVrOspfNbmaNbrStatus_Type = RowStatus
_NsVrOspfNbmaNbrStatus_Object = MibTableColumn
nsVrOspfNbmaNbrStatus = _NsVrOspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 9),
    _NsVrOspfNbmaNbrStatus_Type()
)
nsVrOspfNbmaNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfNbmaNbrStatus.setStatus("current")


class _NsVrOspfNbmaNbrPermanence_Type(Integer32):
    """Custom type nsVrOspfNbmaNbrPermanence based on Integer32"""
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


_NsVrOspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_NsVrOspfNbmaNbrPermanence_Object = MibTableColumn
nsVrOspfNbmaNbrPermanence = _NsVrOspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 10),
    _NsVrOspfNbmaNbrPermanence_Type()
)
nsVrOspfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfNbmaNbrPermanence.setStatus("current")
_NsVrOspfNbrHelloSuppressed_Type = TruthValue
_NsVrOspfNbrHelloSuppressed_Object = MibTableColumn
nsVrOspfNbrHelloSuppressed = _NsVrOspfNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 11),
    _NsVrOspfNbrHelloSuppressed_Type()
)
nsVrOspfNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfNbrHelloSuppressed.setStatus("current")


class _NsVrOspfNbrVRID_Type(Integer32):
    """Custom type nsVrOspfNbrVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfNbrVRID_Type.__name__ = "Integer32"
_NsVrOspfNbrVRID_Object = MibTableColumn
nsVrOspfNbrVRID = _NsVrOspfNbrVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 10, 1, 12),
    _NsVrOspfNbrVRID_Type()
)
nsVrOspfNbrVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfNbrVRID.setStatus("current")
_NsVrOspfVirtNbrTable_Object = MibTable
nsVrOspfVirtNbrTable = _NsVrOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 11)
)
if mibBuilder.loadTexts:
    nsVrOspfVirtNbrTable.setStatus("current")
_NsVrOspfVirtNbrEntry_Object = MibTableRow
nsVrOspfVirtNbrEntry = _NsVrOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 11, 1)
)
nsVrOspfVirtNbrEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfVirtNbrVRID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfVirtNbrArea"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    nsVrOspfVirtNbrEntry.setStatus("current")
_NsVrOspfVirtNbrArea_Type = AreaID
_NsVrOspfVirtNbrArea_Object = MibTableColumn
nsVrOspfVirtNbrArea = _NsVrOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 11, 1, 1),
    _NsVrOspfVirtNbrArea_Type()
)
nsVrOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtNbrArea.setStatus("current")
_NsVrOspfVirtNbrRtrId_Type = RouterID
_NsVrOspfVirtNbrRtrId_Object = MibTableColumn
nsVrOspfVirtNbrRtrId = _NsVrOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 11, 1, 2),
    _NsVrOspfVirtNbrRtrId_Type()
)
nsVrOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtNbrRtrId.setStatus("current")
_NsVrOspfVirtNbrIpAddr_Type = IpAddress
_NsVrOspfVirtNbrIpAddr_Object = MibTableColumn
nsVrOspfVirtNbrIpAddr = _NsVrOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 11, 1, 3),
    _NsVrOspfVirtNbrIpAddr_Type()
)
nsVrOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtNbrIpAddr.setStatus("current")
_NsVrOspfVirtNbrOptions_Type = Integer32
_NsVrOspfVirtNbrOptions_Object = MibTableColumn
nsVrOspfVirtNbrOptions = _NsVrOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 11, 1, 4),
    _NsVrOspfVirtNbrOptions_Type()
)
nsVrOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtNbrOptions.setStatus("current")


class _NsVrOspfVirtNbrState_Type(Integer32):
    """Custom type nsVrOspfVirtNbrState based on Integer32"""
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


_NsVrOspfVirtNbrState_Type.__name__ = "Integer32"
_NsVrOspfVirtNbrState_Object = MibTableColumn
nsVrOspfVirtNbrState = _NsVrOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 11, 1, 5),
    _NsVrOspfVirtNbrState_Type()
)
nsVrOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtNbrState.setStatus("current")
_NsVrOspfVirtNbrEvents_Type = Counter32
_NsVrOspfVirtNbrEvents_Object = MibTableColumn
nsVrOspfVirtNbrEvents = _NsVrOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 11, 1, 6),
    _NsVrOspfVirtNbrEvents_Type()
)
nsVrOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtNbrEvents.setStatus("current")
_NsVrOspfVirtNbrLsRetransQLen_Type = Gauge32
_NsVrOspfVirtNbrLsRetransQLen_Object = MibTableColumn
nsVrOspfVirtNbrLsRetransQLen = _NsVrOspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 11, 1, 7),
    _NsVrOspfVirtNbrLsRetransQLen_Type()
)
nsVrOspfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtNbrLsRetransQLen.setStatus("current")
_NsVrOspfVirtNbrHelloSuppressed_Type = TruthValue
_NsVrOspfVirtNbrHelloSuppressed_Object = MibTableColumn
nsVrOspfVirtNbrHelloSuppressed = _NsVrOspfVirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 11, 1, 8),
    _NsVrOspfVirtNbrHelloSuppressed_Type()
)
nsVrOspfVirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtNbrHelloSuppressed.setStatus("current")


class _NsVrOspfVirtNbrVRID_Type(Integer32):
    """Custom type nsVrOspfVirtNbrVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfVirtNbrVRID_Type.__name__ = "Integer32"
_NsVrOspfVirtNbrVRID_Object = MibTableColumn
nsVrOspfVirtNbrVRID = _NsVrOspfVirtNbrVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 11, 1, 9),
    _NsVrOspfVirtNbrVRID_Type()
)
nsVrOspfVirtNbrVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfVirtNbrVRID.setStatus("current")
_NsVrOspfExtLsdbTable_Object = MibTable
nsVrOspfExtLsdbTable = _NsVrOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 12)
)
if mibBuilder.loadTexts:
    nsVrOspfExtLsdbTable.setStatus("current")
_NsVrOspfExtLsdbEntry_Object = MibTableRow
nsVrOspfExtLsdbEntry = _NsVrOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 12, 1)
)
nsVrOspfExtLsdbEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfExtLsdbVRID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfExtLsdbType"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfExtLsdbLsid"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    nsVrOspfExtLsdbEntry.setStatus("current")


class _NsVrOspfExtLsdbType_Type(Integer32):
    """Custom type nsVrOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_NsVrOspfExtLsdbType_Type.__name__ = "Integer32"
_NsVrOspfExtLsdbType_Object = MibTableColumn
nsVrOspfExtLsdbType = _NsVrOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 12, 1, 1),
    _NsVrOspfExtLsdbType_Type()
)
nsVrOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExtLsdbType.setStatus("current")
_NsVrOspfExtLsdbLsid_Type = IpAddress
_NsVrOspfExtLsdbLsid_Object = MibTableColumn
nsVrOspfExtLsdbLsid = _NsVrOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 12, 1, 2),
    _NsVrOspfExtLsdbLsid_Type()
)
nsVrOspfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExtLsdbLsid.setStatus("current")
_NsVrOspfExtLsdbRouterId_Type = RouterID
_NsVrOspfExtLsdbRouterId_Object = MibTableColumn
nsVrOspfExtLsdbRouterId = _NsVrOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 12, 1, 3),
    _NsVrOspfExtLsdbRouterId_Type()
)
nsVrOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExtLsdbRouterId.setStatus("current")
_NsVrOspfExtLsdbSequence_Type = Integer32
_NsVrOspfExtLsdbSequence_Object = MibTableColumn
nsVrOspfExtLsdbSequence = _NsVrOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 12, 1, 4),
    _NsVrOspfExtLsdbSequence_Type()
)
nsVrOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExtLsdbSequence.setStatus("current")
_NsVrOspfExtLsdbAge_Type = Integer32
_NsVrOspfExtLsdbAge_Object = MibTableColumn
nsVrOspfExtLsdbAge = _NsVrOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 12, 1, 5),
    _NsVrOspfExtLsdbAge_Type()
)
nsVrOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExtLsdbAge.setStatus("current")
_NsVrOspfExtLsdbChecksum_Type = Integer32
_NsVrOspfExtLsdbChecksum_Object = MibTableColumn
nsVrOspfExtLsdbChecksum = _NsVrOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 12, 1, 6),
    _NsVrOspfExtLsdbChecksum_Type()
)
nsVrOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExtLsdbChecksum.setStatus("current")


class _NsVrOspfExtLsdbAdvertisement_Type(OctetString):
    """Custom type nsVrOspfExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )


_NsVrOspfExtLsdbAdvertisement_Type.__name__ = "OctetString"
_NsVrOspfExtLsdbAdvertisement_Object = MibTableColumn
nsVrOspfExtLsdbAdvertisement = _NsVrOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 12, 1, 7),
    _NsVrOspfExtLsdbAdvertisement_Type()
)
nsVrOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExtLsdbAdvertisement.setStatus("current")


class _NsVrOspfExtLsdbVRID_Type(Integer32):
    """Custom type nsVrOspfExtLsdbVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfExtLsdbVRID_Type.__name__ = "Integer32"
_NsVrOspfExtLsdbVRID_Object = MibTableColumn
nsVrOspfExtLsdbVRID = _NsVrOspfExtLsdbVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 12, 1, 8),
    _NsVrOspfExtLsdbVRID_Type()
)
nsVrOspfExtLsdbVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfExtLsdbVRID.setStatus("current")
_NsVrOspfAreaAggregateTable_Object = MibTable
nsVrOspfAreaAggregateTable = _NsVrOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 14)
)
if mibBuilder.loadTexts:
    nsVrOspfAreaAggregateTable.setStatus("current")
_NsVrOspfAreaAggregateEntry_Object = MibTableRow
nsVrOspfAreaAggregateEntry = _NsVrOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 14, 1)
)
nsVrOspfAreaAggregateEntry.setIndexNames(
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfAreaAggregateVRID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfAreaAggregateAreaID"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfAreaAggregateLsdbType"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfAreaAggregateNet"),
    (0, "NETSCREEN-VR-OSPF-MIB", "nsVrOspfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    nsVrOspfAreaAggregateEntry.setStatus("current")
_NsVrOspfAreaAggregateAreaID_Type = AreaID
_NsVrOspfAreaAggregateAreaID_Object = MibTableColumn
nsVrOspfAreaAggregateAreaID = _NsVrOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 14, 1, 1),
    _NsVrOspfAreaAggregateAreaID_Type()
)
nsVrOspfAreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAreaAggregateAreaID.setStatus("current")


class _NsVrOspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type nsVrOspfAreaAggregateLsdbType based on Integer32"""
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


_NsVrOspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_NsVrOspfAreaAggregateLsdbType_Object = MibTableColumn
nsVrOspfAreaAggregateLsdbType = _NsVrOspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 14, 1, 2),
    _NsVrOspfAreaAggregateLsdbType_Type()
)
nsVrOspfAreaAggregateLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAreaAggregateLsdbType.setStatus("current")
_NsVrOspfAreaAggregateNet_Type = IpAddress
_NsVrOspfAreaAggregateNet_Object = MibTableColumn
nsVrOspfAreaAggregateNet = _NsVrOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 14, 1, 3),
    _NsVrOspfAreaAggregateNet_Type()
)
nsVrOspfAreaAggregateNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAreaAggregateNet.setStatus("current")
_NsVrOspfAreaAggregateMask_Type = IpAddress
_NsVrOspfAreaAggregateMask_Object = MibTableColumn
nsVrOspfAreaAggregateMask = _NsVrOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 14, 1, 4),
    _NsVrOspfAreaAggregateMask_Type()
)
nsVrOspfAreaAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAreaAggregateMask.setStatus("current")
_NsVrOspfAreaAggregateStatus_Type = RowStatus
_NsVrOspfAreaAggregateStatus_Object = MibTableColumn
nsVrOspfAreaAggregateStatus = _NsVrOspfAreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 14, 1, 5),
    _NsVrOspfAreaAggregateStatus_Type()
)
nsVrOspfAreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfAreaAggregateStatus.setStatus("current")


class _NsVrOspfAreaAggregateEffect_Type(Integer32):
    """Custom type nsVrOspfAreaAggregateEffect based on Integer32"""
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


_NsVrOspfAreaAggregateEffect_Type.__name__ = "Integer32"
_NsVrOspfAreaAggregateEffect_Object = MibTableColumn
nsVrOspfAreaAggregateEffect = _NsVrOspfAreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 14, 1, 6),
    _NsVrOspfAreaAggregateEffect_Type()
)
nsVrOspfAreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrOspfAreaAggregateEffect.setStatus("current")


class _NsVrOspfAreaAggregateVRID_Type(Integer32):
    """Custom type nsVrOspfAreaAggregateVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrOspfAreaAggregateVRID_Type.__name__ = "Integer32"
_NsVrOspfAreaAggregateVRID_Object = MibTableColumn
nsVrOspfAreaAggregateVRID = _NsVrOspfAreaAggregateVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 5, 14, 1, 7),
    _NsVrOspfAreaAggregateVRID_Type()
)
nsVrOspfAreaAggregateVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrOspfAreaAggregateVRID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VR-OSPF-MIB",
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
       "nsVrOspf": nsVrOspf,
       "nsVrOspfGeneralTable": nsVrOspfGeneralTable,
       "nsVrOspfGeneralEntry": nsVrOspfGeneralEntry,
       "nsVrOspfRouterId": nsVrOspfRouterId,
       "nsVrOspfAdminStat": nsVrOspfAdminStat,
       "nsVrOspfVersionNumber": nsVrOspfVersionNumber,
       "nsVrOspfAreaBdrRtrStatus": nsVrOspfAreaBdrRtrStatus,
       "nsVrOspfASBdrRtrStatus": nsVrOspfASBdrRtrStatus,
       "nsVrOspfExternLsaCount": nsVrOspfExternLsaCount,
       "nsVrOspfExternLsaCksumSum": nsVrOspfExternLsaCksumSum,
       "nsVrOspfTOSSupport": nsVrOspfTOSSupport,
       "nsVrOspfOriginateNewLsas": nsVrOspfOriginateNewLsas,
       "nsVrOspfRxNewLsas": nsVrOspfRxNewLsas,
       "nsVrOspfExtLsdbLimit": nsVrOspfExtLsdbLimit,
       "nsVrOspfMulticastExtensions": nsVrOspfMulticastExtensions,
       "nsVrOspfExitOverflowInterval": nsVrOspfExitOverflowInterval,
       "nsVrOspfDemandExtensions": nsVrOspfDemandExtensions,
       "nsVrOspfGeneralVRID": nsVrOspfGeneralVRID,
       "nsVrOspfAreaTable": nsVrOspfAreaTable,
       "nsVrOspfAreaEntry": nsVrOspfAreaEntry,
       "nsVrOspfAreaId": nsVrOspfAreaId,
       "nsVrOspfImportAsExtern": nsVrOspfImportAsExtern,
       "nsVrOspfSpfRuns": nsVrOspfSpfRuns,
       "nsVrOspfAreaBdrRtrCount": nsVrOspfAreaBdrRtrCount,
       "nsVrOspfAsBdrRtrCount": nsVrOspfAsBdrRtrCount,
       "nsVrOspfAreaLsaCount": nsVrOspfAreaLsaCount,
       "nsVrOspfAreaLsaCksumSum": nsVrOspfAreaLsaCksumSum,
       "nsVrOspfAreaSummary": nsVrOspfAreaSummary,
       "nsVrOspfAreaStatus": nsVrOspfAreaStatus,
       "nsVrOspfAreaVRID": nsVrOspfAreaVRID,
       "nsVrOspfStubAreaTable": nsVrOspfStubAreaTable,
       "nsVrOspfStubAreaEntry": nsVrOspfStubAreaEntry,
       "nsVrOspfStubAreaId": nsVrOspfStubAreaId,
       "nsVrOspfStubTOS": nsVrOspfStubTOS,
       "nsVrOspfStubMetric": nsVrOspfStubMetric,
       "nsVrOspfStubStatus": nsVrOspfStubStatus,
       "nsVrOspfStubMetricType": nsVrOspfStubMetricType,
       "nsVrOspfStubVRID": nsVrOspfStubVRID,
       "nsVrOspfLsdbTable": nsVrOspfLsdbTable,
       "nsVrOspfLsdbEntry": nsVrOspfLsdbEntry,
       "nsVrOspfLsdbAreaId": nsVrOspfLsdbAreaId,
       "nsVrOspfLsdbType": nsVrOspfLsdbType,
       "nsVrOspfLsdbLsid": nsVrOspfLsdbLsid,
       "nsVrOspfLsdbRouterId": nsVrOspfLsdbRouterId,
       "nsVrOspfLsdbSequence": nsVrOspfLsdbSequence,
       "nsVrOspfLsdbAge": nsVrOspfLsdbAge,
       "nsVrOspfLsdbChecksum": nsVrOspfLsdbChecksum,
       "nsVrOspfLsdbAdvertisement": nsVrOspfLsdbAdvertisement,
       "nsVrOspfLsdbVRID": nsVrOspfLsdbVRID,
       "nsVrOspfHostTable": nsVrOspfHostTable,
       "nsVrOspfHostEntry": nsVrOspfHostEntry,
       "nsVrOspfHostIpAddress": nsVrOspfHostIpAddress,
       "nsVrOspfHostTOS": nsVrOspfHostTOS,
       "nsVrOspfHostMetric": nsVrOspfHostMetric,
       "nsVrOspfHostStatus": nsVrOspfHostStatus,
       "nsVrOspfHostAreaID": nsVrOspfHostAreaID,
       "nsVrOspfHostVRID": nsVrOspfHostVRID,
       "nsVrOspfIfTable": nsVrOspfIfTable,
       "nsVrOspfIfEntry": nsVrOspfIfEntry,
       "nsVrOspfIfIpAddress": nsVrOspfIfIpAddress,
       "nsVrOspfAddressLessIf": nsVrOspfAddressLessIf,
       "nsVrOspfIfAreaId": nsVrOspfIfAreaId,
       "nsVrOspfIfType": nsVrOspfIfType,
       "nsVrOspfIfAdminStat": nsVrOspfIfAdminStat,
       "nsVrOspfIfRtrPriority": nsVrOspfIfRtrPriority,
       "nsVrOspfIfTransitDelay": nsVrOspfIfTransitDelay,
       "nsVrOspfIfRetransInterval": nsVrOspfIfRetransInterval,
       "nsVrOspfIfHelloInterval": nsVrOspfIfHelloInterval,
       "nsVrOspfIfRtrDeadInterval": nsVrOspfIfRtrDeadInterval,
       "nsVrOspfIfPollInterval": nsVrOspfIfPollInterval,
       "nsVrOspfIfState": nsVrOspfIfState,
       "nsVrOspfIfDesignatedRouter": nsVrOspfIfDesignatedRouter,
       "nsVrOspfIfBackupDesignatedRouter": nsVrOspfIfBackupDesignatedRouter,
       "nsVrOspfIfEvents": nsVrOspfIfEvents,
       "nsVrOspfIfAuthKey": nsVrOspfIfAuthKey,
       "nsVrOspfIfStatus": nsVrOspfIfStatus,
       "nsVrOspfIfMulticastForwarding": nsVrOspfIfMulticastForwarding,
       "nsVrOspfIfDemand": nsVrOspfIfDemand,
       "nsVrOspfIfAuthType": nsVrOspfIfAuthType,
       "nsVrOspfIfVRID": nsVrOspfIfVRID,
       "nsVrOspfIfMetricTable": nsVrOspfIfMetricTable,
       "nsVrOspfIfMetricEntry": nsVrOspfIfMetricEntry,
       "nsVrOspfIfMetricIpAddress": nsVrOspfIfMetricIpAddress,
       "nsVrOspfIfMetricAddressLessIf": nsVrOspfIfMetricAddressLessIf,
       "nsVrOspfIfMetricTOS": nsVrOspfIfMetricTOS,
       "nsVrOspfIfMetricValue": nsVrOspfIfMetricValue,
       "nsVrOspfIfMetricStatus": nsVrOspfIfMetricStatus,
       "nsVrOspfIfMetricVRID": nsVrOspfIfMetricVRID,
       "nsVrOspfVirtIfTable": nsVrOspfVirtIfTable,
       "nsVrOspfVirtIfEntry": nsVrOspfVirtIfEntry,
       "nsVrOspfVirtIfAreaId": nsVrOspfVirtIfAreaId,
       "nsVrOspfVirtIfNeighbor": nsVrOspfVirtIfNeighbor,
       "nsVrOspfVirtIfTransitDelay": nsVrOspfVirtIfTransitDelay,
       "nsVrOspfVirtIfRetransInterval": nsVrOspfVirtIfRetransInterval,
       "nsVrOspfVirtIfHelloInterval": nsVrOspfVirtIfHelloInterval,
       "nsVrOspfVirtIfRtrDeadInterval": nsVrOspfVirtIfRtrDeadInterval,
       "nsVrOspfVirtIfState": nsVrOspfVirtIfState,
       "nsVrOspfVirtIfEvents": nsVrOspfVirtIfEvents,
       "nsVrOspfVirtIfAuthKey": nsVrOspfVirtIfAuthKey,
       "nsVrOspfVirtIfStatus": nsVrOspfVirtIfStatus,
       "nsVrOspfVirtIfAuthType": nsVrOspfVirtIfAuthType,
       "nsVrOspfVirtIfVRID": nsVrOspfVirtIfVRID,
       "nsVrOspfNbrTable": nsVrOspfNbrTable,
       "nsVrOspfNbrEntry": nsVrOspfNbrEntry,
       "nsVrOspfNbrIpAddr": nsVrOspfNbrIpAddr,
       "nsVrOspfNbrAddressLessIndex": nsVrOspfNbrAddressLessIndex,
       "nsVrOspfNbrRtrId": nsVrOspfNbrRtrId,
       "nsVrOspfNbrOptions": nsVrOspfNbrOptions,
       "nsVrOspfNbrPriority": nsVrOspfNbrPriority,
       "nsVrOspfNbrState": nsVrOspfNbrState,
       "nsVrOspfNbrEvents": nsVrOspfNbrEvents,
       "nsVrOspfNbrLsRetransQLen": nsVrOspfNbrLsRetransQLen,
       "nsVrOspfNbmaNbrStatus": nsVrOspfNbmaNbrStatus,
       "nsVrOspfNbmaNbrPermanence": nsVrOspfNbmaNbrPermanence,
       "nsVrOspfNbrHelloSuppressed": nsVrOspfNbrHelloSuppressed,
       "nsVrOspfNbrVRID": nsVrOspfNbrVRID,
       "nsVrOspfVirtNbrTable": nsVrOspfVirtNbrTable,
       "nsVrOspfVirtNbrEntry": nsVrOspfVirtNbrEntry,
       "nsVrOspfVirtNbrArea": nsVrOspfVirtNbrArea,
       "nsVrOspfVirtNbrRtrId": nsVrOspfVirtNbrRtrId,
       "nsVrOspfVirtNbrIpAddr": nsVrOspfVirtNbrIpAddr,
       "nsVrOspfVirtNbrOptions": nsVrOspfVirtNbrOptions,
       "nsVrOspfVirtNbrState": nsVrOspfVirtNbrState,
       "nsVrOspfVirtNbrEvents": nsVrOspfVirtNbrEvents,
       "nsVrOspfVirtNbrLsRetransQLen": nsVrOspfVirtNbrLsRetransQLen,
       "nsVrOspfVirtNbrHelloSuppressed": nsVrOspfVirtNbrHelloSuppressed,
       "nsVrOspfVirtNbrVRID": nsVrOspfVirtNbrVRID,
       "nsVrOspfExtLsdbTable": nsVrOspfExtLsdbTable,
       "nsVrOspfExtLsdbEntry": nsVrOspfExtLsdbEntry,
       "nsVrOspfExtLsdbType": nsVrOspfExtLsdbType,
       "nsVrOspfExtLsdbLsid": nsVrOspfExtLsdbLsid,
       "nsVrOspfExtLsdbRouterId": nsVrOspfExtLsdbRouterId,
       "nsVrOspfExtLsdbSequence": nsVrOspfExtLsdbSequence,
       "nsVrOspfExtLsdbAge": nsVrOspfExtLsdbAge,
       "nsVrOspfExtLsdbChecksum": nsVrOspfExtLsdbChecksum,
       "nsVrOspfExtLsdbAdvertisement": nsVrOspfExtLsdbAdvertisement,
       "nsVrOspfExtLsdbVRID": nsVrOspfExtLsdbVRID,
       "nsVrOspfAreaAggregateTable": nsVrOspfAreaAggregateTable,
       "nsVrOspfAreaAggregateEntry": nsVrOspfAreaAggregateEntry,
       "nsVrOspfAreaAggregateAreaID": nsVrOspfAreaAggregateAreaID,
       "nsVrOspfAreaAggregateLsdbType": nsVrOspfAreaAggregateLsdbType,
       "nsVrOspfAreaAggregateNet": nsVrOspfAreaAggregateNet,
       "nsVrOspfAreaAggregateMask": nsVrOspfAreaAggregateMask,
       "nsVrOspfAreaAggregateStatus": nsVrOspfAreaAggregateStatus,
       "nsVrOspfAreaAggregateEffect": nsVrOspfAreaAggregateEffect,
       "nsVrOspfAreaAggregateVRID": nsVrOspfAreaAggregateVRID}
)

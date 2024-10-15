# SNMP MIB module (BAS-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:29 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basAliasOspf) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basAliasOspf")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

basOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1)
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

_BasOspfObjects_ObjectIdentity = ObjectIdentity
basOspfObjects = _BasOspfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1)
)
_BasOspfGeneralGroupTable_Object = MibTable
basOspfGeneralGroupTable = _BasOspfGeneralGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1)
)
if mibBuilder.loadTexts:
    basOspfGeneralGroupTable.setStatus("current")
_BasOspfGeneralGroupEntry_Object = MibTableRow
basOspfGeneralGroupEntry = _BasOspfGeneralGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1)
)
basOspfGeneralGroupEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfGeneralGroupChassis"),
    (0, "BAS-OSPF-MIB", "basOspfGeneralGroupSlot"),
    (0, "BAS-OSPF-MIB", "basOspfGeneralGroupIf"),
    (0, "BAS-OSPF-MIB", "basOspfGeneralGroupLPort"),
)
if mibBuilder.loadTexts:
    basOspfGeneralGroupEntry.setStatus("current")
_BasOspfRouterId_Type = RouterID
_BasOspfRouterId_Object = MibTableColumn
basOspfRouterId = _BasOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 1),
    _BasOspfRouterId_Type()
)
basOspfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basOspfRouterId.setStatus("current")
_BasOspfAdminStat_Type = Status
_BasOspfAdminStat_Object = MibTableColumn
basOspfAdminStat = _BasOspfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 2),
    _BasOspfAdminStat_Type()
)
basOspfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basOspfAdminStat.setStatus("current")


class _BasOspfVersionNumber_Type(Integer32):
    """Custom type basOspfVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("version2", 2)
    )


_BasOspfVersionNumber_Type.__name__ = "Integer32"
_BasOspfVersionNumber_Object = MibTableColumn
basOspfVersionNumber = _BasOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 3),
    _BasOspfVersionNumber_Type()
)
basOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVersionNumber.setStatus("current")
_BasOspfAreaBdrRtrStatus_Type = TruthValue
_BasOspfAreaBdrRtrStatus_Object = MibTableColumn
basOspfAreaBdrRtrStatus = _BasOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 4),
    _BasOspfAreaBdrRtrStatus_Type()
)
basOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfAreaBdrRtrStatus.setStatus("current")
_BasOspfASBdrRtrStatus_Type = TruthValue
_BasOspfASBdrRtrStatus_Object = MibTableColumn
basOspfASBdrRtrStatus = _BasOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 5),
    _BasOspfASBdrRtrStatus_Type()
)
basOspfASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basOspfASBdrRtrStatus.setStatus("current")
_BasOspfExternLsaCount_Type = Gauge32
_BasOspfExternLsaCount_Object = MibTableColumn
basOspfExternLsaCount = _BasOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 6),
    _BasOspfExternLsaCount_Type()
)
basOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfExternLsaCount.setStatus("current")
_BasOspfExternLsaCksumSum_Type = Integer32
_BasOspfExternLsaCksumSum_Object = MibTableColumn
basOspfExternLsaCksumSum = _BasOspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 7),
    _BasOspfExternLsaCksumSum_Type()
)
basOspfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfExternLsaCksumSum.setStatus("current")
_BasOspfTOSSupport_Type = TruthValue
_BasOspfTOSSupport_Object = MibTableColumn
basOspfTOSSupport = _BasOspfTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 8),
    _BasOspfTOSSupport_Type()
)
basOspfTOSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basOspfTOSSupport.setStatus("current")
_BasOspfOriginateNewLsas_Type = Counter32
_BasOspfOriginateNewLsas_Object = MibTableColumn
basOspfOriginateNewLsas = _BasOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 9),
    _BasOspfOriginateNewLsas_Type()
)
basOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfOriginateNewLsas.setStatus("current")
_BasOspfRxNewLsas_Type = Counter32
_BasOspfRxNewLsas_Object = MibTableColumn
basOspfRxNewLsas = _BasOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 10),
    _BasOspfRxNewLsas_Type()
)
basOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfRxNewLsas.setStatus("current")


class _BasOspfExtLsdbLimit_Type(Integer32):
    """Custom type basOspfExtLsdbLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_BasOspfExtLsdbLimit_Type.__name__ = "Integer32"
_BasOspfExtLsdbLimit_Object = MibTableColumn
basOspfExtLsdbLimit = _BasOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 11),
    _BasOspfExtLsdbLimit_Type()
)
basOspfExtLsdbLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basOspfExtLsdbLimit.setStatus("current")


class _BasOspfMulticastExtensions_Type(Integer32):
    """Custom type basOspfMulticastExtensions based on Integer32"""
    defaultValue = 0


_BasOspfMulticastExtensions_Object = MibTableColumn
basOspfMulticastExtensions = _BasOspfMulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 12),
    _BasOspfMulticastExtensions_Type()
)
basOspfMulticastExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basOspfMulticastExtensions.setStatus("current")


class _BasOspfExitOverflowInterval_Type(PositiveInteger):
    """Custom type basOspfExitOverflowInterval based on PositiveInteger"""
    defaultValue = 0


_BasOspfExitOverflowInterval_Object = MibTableColumn
basOspfExitOverflowInterval = _BasOspfExitOverflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 13),
    _BasOspfExitOverflowInterval_Type()
)
basOspfExitOverflowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basOspfExitOverflowInterval.setStatus("current")
_BasOspfDemandExtensions_Type = TruthValue
_BasOspfDemandExtensions_Object = MibTableColumn
basOspfDemandExtensions = _BasOspfDemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 14),
    _BasOspfDemandExtensions_Type()
)
basOspfDemandExtensions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basOspfDemandExtensions.setStatus("current")
_BasOspfGeneralGroupChassis_Type = BasChassisId
_BasOspfGeneralGroupChassis_Object = MibTableColumn
basOspfGeneralGroupChassis = _BasOspfGeneralGroupChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 15),
    _BasOspfGeneralGroupChassis_Type()
)
basOspfGeneralGroupChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfGeneralGroupChassis.setStatus("current")
_BasOspfGeneralGroupSlot_Type = BasSlotId
_BasOspfGeneralGroupSlot_Object = MibTableColumn
basOspfGeneralGroupSlot = _BasOspfGeneralGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 16),
    _BasOspfGeneralGroupSlot_Type()
)
basOspfGeneralGroupSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfGeneralGroupSlot.setStatus("current")
_BasOspfGeneralGroupIf_Type = BasInterfaceId
_BasOspfGeneralGroupIf_Object = MibTableColumn
basOspfGeneralGroupIf = _BasOspfGeneralGroupIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 17),
    _BasOspfGeneralGroupIf_Type()
)
basOspfGeneralGroupIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfGeneralGroupIf.setStatus("current")
_BasOspfGeneralGroupLPort_Type = BasLogicalPortId
_BasOspfGeneralGroupLPort_Object = MibTableColumn
basOspfGeneralGroupLPort = _BasOspfGeneralGroupLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 1, 1, 18),
    _BasOspfGeneralGroupLPort_Type()
)
basOspfGeneralGroupLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfGeneralGroupLPort.setStatus("current")
_BasOspfAreaTable_Object = MibTable
basOspfAreaTable = _BasOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2)
)
if mibBuilder.loadTexts:
    basOspfAreaTable.setStatus("current")
_BasOspfAreaEntry_Object = MibTableRow
basOspfAreaEntry = _BasOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1)
)
basOspfAreaEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfAreaChassis"),
    (0, "BAS-OSPF-MIB", "basOspfAreaSlot"),
    (0, "BAS-OSPF-MIB", "basOspfAreaIf"),
    (0, "BAS-OSPF-MIB", "basOspfAreaLPort"),
    (0, "BAS-OSPF-MIB", "basOspfAreaId"),
)
if mibBuilder.loadTexts:
    basOspfAreaEntry.setStatus("current")
_BasOspfAreaId_Type = AreaID
_BasOspfAreaId_Object = MibTableColumn
basOspfAreaId = _BasOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 1),
    _BasOspfAreaId_Type()
)
basOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfAreaId.setStatus("current")


class _BasOspfAuthType_Type(Integer32):
    """Custom type basOspfAuthType based on Integer32"""
    defaultValue = 0


_BasOspfAuthType_Object = MibTableColumn
basOspfAuthType = _BasOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 2),
    _BasOspfAuthType_Type()
)
basOspfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfAuthType.setStatus("obsolete")


class _BasOspfImportAsExtern_Type(Integer32):
    """Custom type basOspfImportAsExtern based on Integer32"""
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


_BasOspfImportAsExtern_Type.__name__ = "Integer32"
_BasOspfImportAsExtern_Object = MibTableColumn
basOspfImportAsExtern = _BasOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 3),
    _BasOspfImportAsExtern_Type()
)
basOspfImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfImportAsExtern.setStatus("current")
_BasOspfSpfRuns_Type = Counter32
_BasOspfSpfRuns_Object = MibTableColumn
basOspfSpfRuns = _BasOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 4),
    _BasOspfSpfRuns_Type()
)
basOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfSpfRuns.setStatus("current")
_BasOspfAreaBdrRtrCount_Type = Gauge32
_BasOspfAreaBdrRtrCount_Object = MibTableColumn
basOspfAreaBdrRtrCount = _BasOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 5),
    _BasOspfAreaBdrRtrCount_Type()
)
basOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfAreaBdrRtrCount.setStatus("current")
_BasOspfAsBdrRtrCount_Type = Gauge32
_BasOspfAsBdrRtrCount_Object = MibTableColumn
basOspfAsBdrRtrCount = _BasOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 6),
    _BasOspfAsBdrRtrCount_Type()
)
basOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfAsBdrRtrCount.setStatus("current")
_BasOspfAreaLsaCount_Type = Gauge32
_BasOspfAreaLsaCount_Object = MibTableColumn
basOspfAreaLsaCount = _BasOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 7),
    _BasOspfAreaLsaCount_Type()
)
basOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfAreaLsaCount.setStatus("current")


class _BasOspfAreaLsaCksumSum_Type(Integer32):
    """Custom type basOspfAreaLsaCksumSum based on Integer32"""
    defaultValue = 0


_BasOspfAreaLsaCksumSum_Object = MibTableColumn
basOspfAreaLsaCksumSum = _BasOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 8),
    _BasOspfAreaLsaCksumSum_Type()
)
basOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfAreaLsaCksumSum.setStatus("current")


class _BasOspfAreaSummary_Type(Integer32):
    """Custom type basOspfAreaSummary based on Integer32"""
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


_BasOspfAreaSummary_Type.__name__ = "Integer32"
_BasOspfAreaSummary_Object = MibTableColumn
basOspfAreaSummary = _BasOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 9),
    _BasOspfAreaSummary_Type()
)
basOspfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfAreaSummary.setStatus("current")
_BasOspfAreaStatus_Type = RowStatus
_BasOspfAreaStatus_Object = MibTableColumn
basOspfAreaStatus = _BasOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 10),
    _BasOspfAreaStatus_Type()
)
basOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfAreaStatus.setStatus("current")
_BasOspfAreaChassis_Type = BasChassisId
_BasOspfAreaChassis_Object = MibTableColumn
basOspfAreaChassis = _BasOspfAreaChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 11),
    _BasOspfAreaChassis_Type()
)
basOspfAreaChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfAreaChassis.setStatus("current")
_BasOspfAreaSlot_Type = BasSlotId
_BasOspfAreaSlot_Object = MibTableColumn
basOspfAreaSlot = _BasOspfAreaSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 12),
    _BasOspfAreaSlot_Type()
)
basOspfAreaSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfAreaSlot.setStatus("current")
_BasOspfAreaIf_Type = BasInterfaceId
_BasOspfAreaIf_Object = MibTableColumn
basOspfAreaIf = _BasOspfAreaIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 13),
    _BasOspfAreaIf_Type()
)
basOspfAreaIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfAreaIf.setStatus("current")
_BasOspfAreaLPort_Type = BasLogicalPortId
_BasOspfAreaLPort_Object = MibTableColumn
basOspfAreaLPort = _BasOspfAreaLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 2, 1, 14),
    _BasOspfAreaLPort_Type()
)
basOspfAreaLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfAreaLPort.setStatus("current")
_BasOspfStubAreaTable_Object = MibTable
basOspfStubAreaTable = _BasOspfStubAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 3)
)
if mibBuilder.loadTexts:
    basOspfStubAreaTable.setStatus("current")
_BasOspfStubAreaEntry_Object = MibTableRow
basOspfStubAreaEntry = _BasOspfStubAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 3, 1)
)
basOspfStubAreaEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfStubAreaChassis"),
    (0, "BAS-OSPF-MIB", "basOspfStubAreaSlot"),
    (0, "BAS-OSPF-MIB", "basOspfStubAreaIf"),
    (0, "BAS-OSPF-MIB", "basOspfStubAreaLPort"),
    (0, "BAS-OSPF-MIB", "basOspfStubAreaId"),
    (0, "BAS-OSPF-MIB", "basOspfStubTOS"),
)
if mibBuilder.loadTexts:
    basOspfStubAreaEntry.setStatus("current")
_BasOspfStubAreaId_Type = AreaID
_BasOspfStubAreaId_Object = MibTableColumn
basOspfStubAreaId = _BasOspfStubAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 3, 1, 1),
    _BasOspfStubAreaId_Type()
)
basOspfStubAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfStubAreaId.setStatus("current")
_BasOspfStubTOS_Type = TOSType
_BasOspfStubTOS_Object = MibTableColumn
basOspfStubTOS = _BasOspfStubTOS_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 3, 1, 2),
    _BasOspfStubTOS_Type()
)
basOspfStubTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfStubTOS.setStatus("current")
_BasOspfStubMetric_Type = BigMetric
_BasOspfStubMetric_Object = MibTableColumn
basOspfStubMetric = _BasOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 3, 1, 3),
    _BasOspfStubMetric_Type()
)
basOspfStubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfStubMetric.setStatus("current")
_BasOspfStubStatus_Type = RowStatus
_BasOspfStubStatus_Object = MibTableColumn
basOspfStubStatus = _BasOspfStubStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 3, 1, 4),
    _BasOspfStubStatus_Type()
)
basOspfStubStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfStubStatus.setStatus("current")


class _BasOspfStubMetricType_Type(Integer32):
    """Custom type basOspfStubMetricType based on Integer32"""
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


_BasOspfStubMetricType_Type.__name__ = "Integer32"
_BasOspfStubMetricType_Object = MibTableColumn
basOspfStubMetricType = _BasOspfStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 3, 1, 5),
    _BasOspfStubMetricType_Type()
)
basOspfStubMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfStubMetricType.setStatus("current")
_BasOspfStubAreaChassis_Type = BasChassisId
_BasOspfStubAreaChassis_Object = MibTableColumn
basOspfStubAreaChassis = _BasOspfStubAreaChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 3, 1, 6),
    _BasOspfStubAreaChassis_Type()
)
basOspfStubAreaChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfStubAreaChassis.setStatus("current")
_BasOspfStubAreaSlot_Type = BasSlotId
_BasOspfStubAreaSlot_Object = MibTableColumn
basOspfStubAreaSlot = _BasOspfStubAreaSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 3, 1, 7),
    _BasOspfStubAreaSlot_Type()
)
basOspfStubAreaSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfStubAreaSlot.setStatus("current")
_BasOspfStubAreaIf_Type = BasInterfaceId
_BasOspfStubAreaIf_Object = MibTableColumn
basOspfStubAreaIf = _BasOspfStubAreaIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 3, 1, 8),
    _BasOspfStubAreaIf_Type()
)
basOspfStubAreaIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfStubAreaIf.setStatus("current")
_BasOspfStubAreaLPort_Type = BasLogicalPortId
_BasOspfStubAreaLPort_Object = MibTableColumn
basOspfStubAreaLPort = _BasOspfStubAreaLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 3, 1, 9),
    _BasOspfStubAreaLPort_Type()
)
basOspfStubAreaLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfStubAreaLPort.setStatus("current")
_BasOspfLsdbTable_Object = MibTable
basOspfLsdbTable = _BasOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4)
)
if mibBuilder.loadTexts:
    basOspfLsdbTable.setStatus("current")
_BasOspfLsdbEntry_Object = MibTableRow
basOspfLsdbEntry = _BasOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1)
)
basOspfLsdbEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfLsdbChassis"),
    (0, "BAS-OSPF-MIB", "basOspfLsdbSlot"),
    (0, "BAS-OSPF-MIB", "basOspfLsdbIf"),
    (0, "BAS-OSPF-MIB", "basOspfLsdbLPort"),
    (0, "BAS-OSPF-MIB", "basOspfLsdbAreaId"),
    (0, "BAS-OSPF-MIB", "basOspfLsdbType"),
    (0, "BAS-OSPF-MIB", "basOspfLsdbLsid"),
    (0, "BAS-OSPF-MIB", "basOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    basOspfLsdbEntry.setStatus("current")
_BasOspfLsdbAreaId_Type = AreaID
_BasOspfLsdbAreaId_Object = MibTableColumn
basOspfLsdbAreaId = _BasOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 1),
    _BasOspfLsdbAreaId_Type()
)
basOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfLsdbAreaId.setStatus("current")


class _BasOspfLsdbType_Type(Integer32):
    """Custom type basOspfLsdbType based on Integer32"""
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


_BasOspfLsdbType_Type.__name__ = "Integer32"
_BasOspfLsdbType_Object = MibTableColumn
basOspfLsdbType = _BasOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 2),
    _BasOspfLsdbType_Type()
)
basOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfLsdbType.setStatus("current")
_BasOspfLsdbLsid_Type = IpAddress
_BasOspfLsdbLsid_Object = MibTableColumn
basOspfLsdbLsid = _BasOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 3),
    _BasOspfLsdbLsid_Type()
)
basOspfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfLsdbLsid.setStatus("current")
_BasOspfLsdbRouterId_Type = RouterID
_BasOspfLsdbRouterId_Object = MibTableColumn
basOspfLsdbRouterId = _BasOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 4),
    _BasOspfLsdbRouterId_Type()
)
basOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfLsdbRouterId.setStatus("current")
_BasOspfLsdbSequence_Type = Integer32
_BasOspfLsdbSequence_Object = MibTableColumn
basOspfLsdbSequence = _BasOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 5),
    _BasOspfLsdbSequence_Type()
)
basOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfLsdbSequence.setStatus("current")
_BasOspfLsdbAge_Type = Integer32
_BasOspfLsdbAge_Object = MibTableColumn
basOspfLsdbAge = _BasOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 6),
    _BasOspfLsdbAge_Type()
)
basOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfLsdbAge.setStatus("current")
_BasOspfLsdbChecksum_Type = Integer32
_BasOspfLsdbChecksum_Object = MibTableColumn
basOspfLsdbChecksum = _BasOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 7),
    _BasOspfLsdbChecksum_Type()
)
basOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfLsdbChecksum.setStatus("current")


class _BasOspfLsdbAdvertisement_Type(OctetString):
    """Custom type basOspfLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_BasOspfLsdbAdvertisement_Type.__name__ = "OctetString"
_BasOspfLsdbAdvertisement_Object = MibTableColumn
basOspfLsdbAdvertisement = _BasOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 8),
    _BasOspfLsdbAdvertisement_Type()
)
basOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfLsdbAdvertisement.setStatus("current")
_BasOspfLsdbChassis_Type = BasChassisId
_BasOspfLsdbChassis_Object = MibTableColumn
basOspfLsdbChassis = _BasOspfLsdbChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 9),
    _BasOspfLsdbChassis_Type()
)
basOspfLsdbChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfLsdbChassis.setStatus("current")
_BasOspfLsdbSlot_Type = BasSlotId
_BasOspfLsdbSlot_Object = MibTableColumn
basOspfLsdbSlot = _BasOspfLsdbSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 10),
    _BasOspfLsdbSlot_Type()
)
basOspfLsdbSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfLsdbSlot.setStatus("current")
_BasOspfLsdbIf_Type = BasInterfaceId
_BasOspfLsdbIf_Object = MibTableColumn
basOspfLsdbIf = _BasOspfLsdbIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 11),
    _BasOspfLsdbIf_Type()
)
basOspfLsdbIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfLsdbIf.setStatus("current")
_BasOspfLsdbLPort_Type = BasLogicalPortId
_BasOspfLsdbLPort_Object = MibTableColumn
basOspfLsdbLPort = _BasOspfLsdbLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 4, 1, 12),
    _BasOspfLsdbLPort_Type()
)
basOspfLsdbLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfLsdbLPort.setStatus("current")
_BasOspfHostTable_Object = MibTable
basOspfHostTable = _BasOspfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 6)
)
if mibBuilder.loadTexts:
    basOspfHostTable.setStatus("current")
_BasOspfHostEntry_Object = MibTableRow
basOspfHostEntry = _BasOspfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 6, 1)
)
basOspfHostEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfHostChassis"),
    (0, "BAS-OSPF-MIB", "basOspfHostSlot"),
    (0, "BAS-OSPF-MIB", "basOspfHostIf"),
    (0, "BAS-OSPF-MIB", "basOspfHostLPort"),
    (0, "BAS-OSPF-MIB", "basOspfHostIpAddress"),
    (0, "BAS-OSPF-MIB", "basOspfHostTOS"),
)
if mibBuilder.loadTexts:
    basOspfHostEntry.setStatus("current")
_BasOspfHostIpAddress_Type = IpAddress
_BasOspfHostIpAddress_Object = MibTableColumn
basOspfHostIpAddress = _BasOspfHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 6, 1, 1),
    _BasOspfHostIpAddress_Type()
)
basOspfHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfHostIpAddress.setStatus("current")
_BasOspfHostTOS_Type = TOSType
_BasOspfHostTOS_Object = MibTableColumn
basOspfHostTOS = _BasOspfHostTOS_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 6, 1, 2),
    _BasOspfHostTOS_Type()
)
basOspfHostTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfHostTOS.setStatus("current")
_BasOspfHostMetric_Type = Metric
_BasOspfHostMetric_Object = MibTableColumn
basOspfHostMetric = _BasOspfHostMetric_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 6, 1, 3),
    _BasOspfHostMetric_Type()
)
basOspfHostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfHostMetric.setStatus("current")
_BasOspfHostStatus_Type = RowStatus
_BasOspfHostStatus_Object = MibTableColumn
basOspfHostStatus = _BasOspfHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 6, 1, 4),
    _BasOspfHostStatus_Type()
)
basOspfHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfHostStatus.setStatus("current")
_BasOspfHostAreaID_Type = AreaID
_BasOspfHostAreaID_Object = MibTableColumn
basOspfHostAreaID = _BasOspfHostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 6, 1, 5),
    _BasOspfHostAreaID_Type()
)
basOspfHostAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfHostAreaID.setStatus("current")
_BasOspfHostChassis_Type = BasChassisId
_BasOspfHostChassis_Object = MibTableColumn
basOspfHostChassis = _BasOspfHostChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 6, 1, 6),
    _BasOspfHostChassis_Type()
)
basOspfHostChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfHostChassis.setStatus("current")
_BasOspfHostSlot_Type = BasSlotId
_BasOspfHostSlot_Object = MibTableColumn
basOspfHostSlot = _BasOspfHostSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 6, 1, 7),
    _BasOspfHostSlot_Type()
)
basOspfHostSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfHostSlot.setStatus("current")
_BasOspfHostIf_Type = BasInterfaceId
_BasOspfHostIf_Object = MibTableColumn
basOspfHostIf = _BasOspfHostIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 6, 1, 8),
    _BasOspfHostIf_Type()
)
basOspfHostIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfHostIf.setStatus("current")
_BasOspfHostLPort_Type = BasLogicalPortId
_BasOspfHostLPort_Object = MibTableColumn
basOspfHostLPort = _BasOspfHostLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 6, 1, 9),
    _BasOspfHostLPort_Type()
)
basOspfHostLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfHostLPort.setStatus("current")
_BasOspfIfTable_Object = MibTable
basOspfIfTable = _BasOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7)
)
if mibBuilder.loadTexts:
    basOspfIfTable.setStatus("current")
_BasOspfIfEntry_Object = MibTableRow
basOspfIfEntry = _BasOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1)
)
basOspfIfEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfIfChassis"),
    (0, "BAS-OSPF-MIB", "basOspfIfSlot"),
    (0, "BAS-OSPF-MIB", "basOspfIfIf"),
    (0, "BAS-OSPF-MIB", "basOspfIfLPort"),
    (0, "BAS-OSPF-MIB", "basOspfIfIpAddress"),
    (0, "BAS-OSPF-MIB", "basOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    basOspfIfEntry.setStatus("current")
_BasOspfIfIpAddress_Type = IpAddress
_BasOspfIfIpAddress_Object = MibTableColumn
basOspfIfIpAddress = _BasOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 1),
    _BasOspfIfIpAddress_Type()
)
basOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfIfIpAddress.setStatus("current")
_BasOspfAddressLessIf_Type = Integer32
_BasOspfAddressLessIf_Object = MibTableColumn
basOspfAddressLessIf = _BasOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 2),
    _BasOspfAddressLessIf_Type()
)
basOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfAddressLessIf.setStatus("current")


class _BasOspfIfAreaId_Type(AreaID):
    """Custom type basOspfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_BasOspfIfAreaId_Object = MibTableColumn
basOspfIfAreaId = _BasOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 3),
    _BasOspfIfAreaId_Type()
)
basOspfIfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfAreaId.setStatus("current")


class _BasOspfIfType_Type(Integer32):
    """Custom type basOspfIfType based on Integer32"""
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


_BasOspfIfType_Type.__name__ = "Integer32"
_BasOspfIfType_Object = MibTableColumn
basOspfIfType = _BasOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 4),
    _BasOspfIfType_Type()
)
basOspfIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfType.setStatus("current")


class _BasOspfIfAdminStat_Type(Status):
    """Custom type basOspfIfAdminStat based on Status"""


_BasOspfIfAdminStat_Object = MibTableColumn
basOspfIfAdminStat = _BasOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 5),
    _BasOspfIfAdminStat_Type()
)
basOspfIfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfAdminStat.setStatus("current")


class _BasOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type basOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_BasOspfIfRtrPriority_Object = MibTableColumn
basOspfIfRtrPriority = _BasOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 6),
    _BasOspfIfRtrPriority_Type()
)
basOspfIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfRtrPriority.setStatus("current")


class _BasOspfIfTransitDelay_Type(UpToMaxAge):
    """Custom type basOspfIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_BasOspfIfTransitDelay_Object = MibTableColumn
basOspfIfTransitDelay = _BasOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 7),
    _BasOspfIfTransitDelay_Type()
)
basOspfIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfTransitDelay.setStatus("current")


class _BasOspfIfRetransInterval_Type(UpToMaxAge):
    """Custom type basOspfIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_BasOspfIfRetransInterval_Object = MibTableColumn
basOspfIfRetransInterval = _BasOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 8),
    _BasOspfIfRetransInterval_Type()
)
basOspfIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfRetransInterval.setStatus("current")


class _BasOspfIfHelloInterval_Type(HelloRange):
    """Custom type basOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_BasOspfIfHelloInterval_Object = MibTableColumn
basOspfIfHelloInterval = _BasOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 9),
    _BasOspfIfHelloInterval_Type()
)
basOspfIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfHelloInterval.setStatus("current")


class _BasOspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type basOspfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_BasOspfIfRtrDeadInterval_Object = MibTableColumn
basOspfIfRtrDeadInterval = _BasOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 10),
    _BasOspfIfRtrDeadInterval_Type()
)
basOspfIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfRtrDeadInterval.setStatus("current")


class _BasOspfIfPollInterval_Type(PositiveInteger):
    """Custom type basOspfIfPollInterval based on PositiveInteger"""
    defaultValue = 120


_BasOspfIfPollInterval_Object = MibTableColumn
basOspfIfPollInterval = _BasOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 11),
    _BasOspfIfPollInterval_Type()
)
basOspfIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfPollInterval.setStatus("current")


class _BasOspfIfState_Type(Integer32):
    """Custom type basOspfIfState based on Integer32"""
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


_BasOspfIfState_Type.__name__ = "Integer32"
_BasOspfIfState_Object = MibTableColumn
basOspfIfState = _BasOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 12),
    _BasOspfIfState_Type()
)
basOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfIfState.setStatus("current")


class _BasOspfIfDesignatedRouter_Type(IpAddress):
    """Custom type basOspfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_BasOspfIfDesignatedRouter_Object = MibTableColumn
basOspfIfDesignatedRouter = _BasOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 13),
    _BasOspfIfDesignatedRouter_Type()
)
basOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfIfDesignatedRouter.setStatus("current")


class _BasOspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type basOspfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_BasOspfIfBackupDesignatedRouter_Object = MibTableColumn
basOspfIfBackupDesignatedRouter = _BasOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 14),
    _BasOspfIfBackupDesignatedRouter_Type()
)
basOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfIfBackupDesignatedRouter.setStatus("current")
_BasOspfIfEvents_Type = Counter32
_BasOspfIfEvents_Object = MibTableColumn
basOspfIfEvents = _BasOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 15),
    _BasOspfIfEvents_Type()
)
basOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfIfEvents.setStatus("current")


class _BasOspfIfAuthKey_Type(OctetString):
    """Custom type basOspfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_BasOspfIfAuthKey_Type.__name__ = "OctetString"
_BasOspfIfAuthKey_Object = MibTableColumn
basOspfIfAuthKey = _BasOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 16),
    _BasOspfIfAuthKey_Type()
)
basOspfIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfAuthKey.setStatus("current")
_BasOspfIfStatus_Type = RowStatus
_BasOspfIfStatus_Object = MibTableColumn
basOspfIfStatus = _BasOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 17),
    _BasOspfIfStatus_Type()
)
basOspfIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfStatus.setStatus("current")


class _BasOspfIfMulticastForwarding_Type(Integer32):
    """Custom type basOspfIfMulticastForwarding based on Integer32"""
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


_BasOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_BasOspfIfMulticastForwarding_Object = MibTableColumn
basOspfIfMulticastForwarding = _BasOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 18),
    _BasOspfIfMulticastForwarding_Type()
)
basOspfIfMulticastForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfMulticastForwarding.setStatus("current")


class _BasOspfIfDemand_Type(TruthValue):
    """Custom type basOspfIfDemand based on TruthValue"""


_BasOspfIfDemand_Object = MibTableColumn
basOspfIfDemand = _BasOspfIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 19),
    _BasOspfIfDemand_Type()
)
basOspfIfDemand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfDemand.setStatus("current")


class _BasOspfIfAuthType_Type(Integer32):
    """Custom type basOspfIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasOspfIfAuthType_Type.__name__ = "Integer32"
_BasOspfIfAuthType_Object = MibTableColumn
basOspfIfAuthType = _BasOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 20),
    _BasOspfIfAuthType_Type()
)
basOspfIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfAuthType.setStatus("current")
_BasOspfIfChassis_Type = BasChassisId
_BasOspfIfChassis_Object = MibTableColumn
basOspfIfChassis = _BasOspfIfChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 21),
    _BasOspfIfChassis_Type()
)
basOspfIfChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfIfChassis.setStatus("current")
_BasOspfIfSlot_Type = BasSlotId
_BasOspfIfSlot_Object = MibTableColumn
basOspfIfSlot = _BasOspfIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 22),
    _BasOspfIfSlot_Type()
)
basOspfIfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfIfSlot.setStatus("current")
_BasOspfIfIf_Type = BasInterfaceId
_BasOspfIfIf_Object = MibTableColumn
basOspfIfIf = _BasOspfIfIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 23),
    _BasOspfIfIf_Type()
)
basOspfIfIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfIfIf.setStatus("current")
_BasOspfIfLPort_Type = BasLogicalPortId
_BasOspfIfLPort_Object = MibTableColumn
basOspfIfLPort = _BasOspfIfLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 7, 1, 24),
    _BasOspfIfLPort_Type()
)
basOspfIfLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfIfLPort.setStatus("current")
_BasOspfIfMetricTable_Object = MibTable
basOspfIfMetricTable = _BasOspfIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 8)
)
if mibBuilder.loadTexts:
    basOspfIfMetricTable.setStatus("current")
_BasOspfIfMetricEntry_Object = MibTableRow
basOspfIfMetricEntry = _BasOspfIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 8, 1)
)
basOspfIfMetricEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfIfMetricChassis"),
    (0, "BAS-OSPF-MIB", "basOspfIfMetricSlot"),
    (0, "BAS-OSPF-MIB", "basOspfIfMetricIf"),
    (0, "BAS-OSPF-MIB", "basOspfIfMetricLPort"),
    (0, "BAS-OSPF-MIB", "basOspfIfMetricIpAddress"),
    (0, "BAS-OSPF-MIB", "basOspfIfMetricAddressLessIf"),
    (0, "BAS-OSPF-MIB", "basOspfIfMetricTOS"),
)
if mibBuilder.loadTexts:
    basOspfIfMetricEntry.setStatus("current")
_BasOspfIfMetricIpAddress_Type = IpAddress
_BasOspfIfMetricIpAddress_Object = MibTableColumn
basOspfIfMetricIpAddress = _BasOspfIfMetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 8, 1, 1),
    _BasOspfIfMetricIpAddress_Type()
)
basOspfIfMetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfIfMetricIpAddress.setStatus("current")
_BasOspfIfMetricAddressLessIf_Type = Integer32
_BasOspfIfMetricAddressLessIf_Object = MibTableColumn
basOspfIfMetricAddressLessIf = _BasOspfIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 8, 1, 2),
    _BasOspfIfMetricAddressLessIf_Type()
)
basOspfIfMetricAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfIfMetricAddressLessIf.setStatus("current")
_BasOspfIfMetricTOS_Type = TOSType
_BasOspfIfMetricTOS_Object = MibTableColumn
basOspfIfMetricTOS = _BasOspfIfMetricTOS_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 8, 1, 3),
    _BasOspfIfMetricTOS_Type()
)
basOspfIfMetricTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfIfMetricTOS.setStatus("current")
_BasOspfIfMetricValue_Type = Metric
_BasOspfIfMetricValue_Object = MibTableColumn
basOspfIfMetricValue = _BasOspfIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 8, 1, 4),
    _BasOspfIfMetricValue_Type()
)
basOspfIfMetricValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfMetricValue.setStatus("current")
_BasOspfIfMetricStatus_Type = RowStatus
_BasOspfIfMetricStatus_Object = MibTableColumn
basOspfIfMetricStatus = _BasOspfIfMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 8, 1, 5),
    _BasOspfIfMetricStatus_Type()
)
basOspfIfMetricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfIfMetricStatus.setStatus("current")
_BasOspfIfMetricChassis_Type = BasChassisId
_BasOspfIfMetricChassis_Object = MibTableColumn
basOspfIfMetricChassis = _BasOspfIfMetricChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 8, 1, 6),
    _BasOspfIfMetricChassis_Type()
)
basOspfIfMetricChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfIfMetricChassis.setStatus("current")
_BasOspfIfMetricSlot_Type = BasSlotId
_BasOspfIfMetricSlot_Object = MibTableColumn
basOspfIfMetricSlot = _BasOspfIfMetricSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 8, 1, 7),
    _BasOspfIfMetricSlot_Type()
)
basOspfIfMetricSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfIfMetricSlot.setStatus("current")
_BasOspfIfMetricIf_Type = BasInterfaceId
_BasOspfIfMetricIf_Object = MibTableColumn
basOspfIfMetricIf = _BasOspfIfMetricIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 8, 1, 8),
    _BasOspfIfMetricIf_Type()
)
basOspfIfMetricIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfIfMetricIf.setStatus("current")
_BasOspfIfMetricLPort_Type = BasLogicalPortId
_BasOspfIfMetricLPort_Object = MibTableColumn
basOspfIfMetricLPort = _BasOspfIfMetricLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 8, 1, 9),
    _BasOspfIfMetricLPort_Type()
)
basOspfIfMetricLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfIfMetricLPort.setStatus("current")
_BasOspfVirtIfTable_Object = MibTable
basOspfVirtIfTable = _BasOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9)
)
if mibBuilder.loadTexts:
    basOspfVirtIfTable.setStatus("current")
_BasOspfVirtIfEntry_Object = MibTableRow
basOspfVirtIfEntry = _BasOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1)
)
basOspfVirtIfEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfVirtIfChassis"),
    (0, "BAS-OSPF-MIB", "basOspfVirtIfSlot"),
    (0, "BAS-OSPF-MIB", "basOspfVirtIfIf"),
    (0, "BAS-OSPF-MIB", "basOspfVirtIfLPort"),
    (0, "BAS-OSPF-MIB", "basOspfVirtIfAreaId"),
    (0, "BAS-OSPF-MIB", "basOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    basOspfVirtIfEntry.setStatus("current")
_BasOspfVirtIfAreaId_Type = AreaID
_BasOspfVirtIfAreaId_Object = MibTableColumn
basOspfVirtIfAreaId = _BasOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 1),
    _BasOspfVirtIfAreaId_Type()
)
basOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtIfAreaId.setStatus("current")
_BasOspfVirtIfNeighbor_Type = RouterID
_BasOspfVirtIfNeighbor_Object = MibTableColumn
basOspfVirtIfNeighbor = _BasOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 2),
    _BasOspfVirtIfNeighbor_Type()
)
basOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtIfNeighbor.setStatus("current")


class _BasOspfVirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type basOspfVirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_BasOspfVirtIfTransitDelay_Object = MibTableColumn
basOspfVirtIfTransitDelay = _BasOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 3),
    _BasOspfVirtIfTransitDelay_Type()
)
basOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfVirtIfTransitDelay.setStatus("current")


class _BasOspfVirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type basOspfVirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_BasOspfVirtIfRetransInterval_Object = MibTableColumn
basOspfVirtIfRetransInterval = _BasOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 4),
    _BasOspfVirtIfRetransInterval_Type()
)
basOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfVirtIfRetransInterval.setStatus("current")


class _BasOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type basOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_BasOspfVirtIfHelloInterval_Object = MibTableColumn
basOspfVirtIfHelloInterval = _BasOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 5),
    _BasOspfVirtIfHelloInterval_Type()
)
basOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfVirtIfHelloInterval.setStatus("current")


class _BasOspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type basOspfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 60


_BasOspfVirtIfRtrDeadInterval_Object = MibTableColumn
basOspfVirtIfRtrDeadInterval = _BasOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 6),
    _BasOspfVirtIfRtrDeadInterval_Type()
)
basOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfVirtIfRtrDeadInterval.setStatus("current")


class _BasOspfVirtIfState_Type(Integer32):
    """Custom type basOspfVirtIfState based on Integer32"""
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


_BasOspfVirtIfState_Type.__name__ = "Integer32"
_BasOspfVirtIfState_Object = MibTableColumn
basOspfVirtIfState = _BasOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 7),
    _BasOspfVirtIfState_Type()
)
basOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtIfState.setStatus("current")
_BasOspfVirtIfEvents_Type = Counter32
_BasOspfVirtIfEvents_Object = MibTableColumn
basOspfVirtIfEvents = _BasOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 8),
    _BasOspfVirtIfEvents_Type()
)
basOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtIfEvents.setStatus("current")


class _BasOspfVirtIfAuthKey_Type(OctetString):
    """Custom type basOspfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_BasOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_BasOspfVirtIfAuthKey_Object = MibTableColumn
basOspfVirtIfAuthKey = _BasOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 9),
    _BasOspfVirtIfAuthKey_Type()
)
basOspfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfVirtIfAuthKey.setStatus("current")
_BasOspfVirtIfStatus_Type = RowStatus
_BasOspfVirtIfStatus_Object = MibTableColumn
basOspfVirtIfStatus = _BasOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 10),
    _BasOspfVirtIfStatus_Type()
)
basOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfVirtIfStatus.setStatus("current")


class _BasOspfVirtIfAuthType_Type(Integer32):
    """Custom type basOspfVirtIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasOspfVirtIfAuthType_Type.__name__ = "Integer32"
_BasOspfVirtIfAuthType_Object = MibTableColumn
basOspfVirtIfAuthType = _BasOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 11),
    _BasOspfVirtIfAuthType_Type()
)
basOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfVirtIfAuthType.setStatus("current")
_BasOspfVirtIfChassis_Type = BasChassisId
_BasOspfVirtIfChassis_Object = MibTableColumn
basOspfVirtIfChassis = _BasOspfVirtIfChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 12),
    _BasOspfVirtIfChassis_Type()
)
basOspfVirtIfChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfVirtIfChassis.setStatus("current")
_BasOspfVirtIfSlot_Type = BasSlotId
_BasOspfVirtIfSlot_Object = MibTableColumn
basOspfVirtIfSlot = _BasOspfVirtIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 13),
    _BasOspfVirtIfSlot_Type()
)
basOspfVirtIfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfVirtIfSlot.setStatus("current")
_BasOspfVirtIfIf_Type = BasInterfaceId
_BasOspfVirtIfIf_Object = MibTableColumn
basOspfVirtIfIf = _BasOspfVirtIfIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 14),
    _BasOspfVirtIfIf_Type()
)
basOspfVirtIfIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfVirtIfIf.setStatus("current")
_BasOspfVirtIfLPort_Type = BasLogicalPortId
_BasOspfVirtIfLPort_Object = MibTableColumn
basOspfVirtIfLPort = _BasOspfVirtIfLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 9, 1, 15),
    _BasOspfVirtIfLPort_Type()
)
basOspfVirtIfLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfVirtIfLPort.setStatus("current")
_BasOspfNbrTable_Object = MibTable
basOspfNbrTable = _BasOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10)
)
if mibBuilder.loadTexts:
    basOspfNbrTable.setStatus("current")
_BasOspfNbrEntry_Object = MibTableRow
basOspfNbrEntry = _BasOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1)
)
basOspfNbrEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfNbrChassis"),
    (0, "BAS-OSPF-MIB", "basOspfNbrSlot"),
    (0, "BAS-OSPF-MIB", "basOspfNbrIf"),
    (0, "BAS-OSPF-MIB", "basOspfNbrLPort"),
    (0, "BAS-OSPF-MIB", "basOspfNbrIpAddr"),
    (0, "BAS-OSPF-MIB", "basOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    basOspfNbrEntry.setStatus("current")
_BasOspfNbrIpAddr_Type = IpAddress
_BasOspfNbrIpAddr_Object = MibTableColumn
basOspfNbrIpAddr = _BasOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 1),
    _BasOspfNbrIpAddr_Type()
)
basOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfNbrIpAddr.setStatus("current")
_BasOspfNbrAddressLessIndex_Type = InterfaceIndex
_BasOspfNbrAddressLessIndex_Object = MibTableColumn
basOspfNbrAddressLessIndex = _BasOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 2),
    _BasOspfNbrAddressLessIndex_Type()
)
basOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfNbrAddressLessIndex.setStatus("current")


class _BasOspfNbrRtrId_Type(RouterID):
    """Custom type basOspfNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_BasOspfNbrRtrId_Object = MibTableColumn
basOspfNbrRtrId = _BasOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 3),
    _BasOspfNbrRtrId_Type()
)
basOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfNbrRtrId.setStatus("current")


class _BasOspfNbrOptions_Type(Integer32):
    """Custom type basOspfNbrOptions based on Integer32"""
    defaultValue = 0


_BasOspfNbrOptions_Object = MibTableColumn
basOspfNbrOptions = _BasOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 4),
    _BasOspfNbrOptions_Type()
)
basOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfNbrOptions.setStatus("current")


class _BasOspfNbrPriority_Type(DesignatedRouterPriority):
    """Custom type basOspfNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_BasOspfNbrPriority_Object = MibTableColumn
basOspfNbrPriority = _BasOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 5),
    _BasOspfNbrPriority_Type()
)
basOspfNbrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfNbrPriority.setStatus("current")


class _BasOspfNbrState_Type(Integer32):
    """Custom type basOspfNbrState based on Integer32"""
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


_BasOspfNbrState_Type.__name__ = "Integer32"
_BasOspfNbrState_Object = MibTableColumn
basOspfNbrState = _BasOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 6),
    _BasOspfNbrState_Type()
)
basOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfNbrState.setStatus("current")
_BasOspfNbrEvents_Type = Counter32
_BasOspfNbrEvents_Object = MibTableColumn
basOspfNbrEvents = _BasOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 7),
    _BasOspfNbrEvents_Type()
)
basOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfNbrEvents.setStatus("current")
_BasOspfNbrLsRetransQLen_Type = Gauge32
_BasOspfNbrLsRetransQLen_Object = MibTableColumn
basOspfNbrLsRetransQLen = _BasOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 8),
    _BasOspfNbrLsRetransQLen_Type()
)
basOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfNbrLsRetransQLen.setStatus("current")
_BasOspfNbmaNbrStatus_Type = RowStatus
_BasOspfNbmaNbrStatus_Object = MibTableColumn
basOspfNbmaNbrStatus = _BasOspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 9),
    _BasOspfNbmaNbrStatus_Type()
)
basOspfNbmaNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfNbmaNbrStatus.setStatus("current")


class _BasOspfNbmaNbrPermanence_Type(Integer32):
    """Custom type basOspfNbmaNbrPermanence based on Integer32"""
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


_BasOspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_BasOspfNbmaNbrPermanence_Object = MibTableColumn
basOspfNbmaNbrPermanence = _BasOspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 10),
    _BasOspfNbmaNbrPermanence_Type()
)
basOspfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfNbmaNbrPermanence.setStatus("current")
_BasOspfNbrHelloSuppressed_Type = TruthValue
_BasOspfNbrHelloSuppressed_Object = MibTableColumn
basOspfNbrHelloSuppressed = _BasOspfNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 11),
    _BasOspfNbrHelloSuppressed_Type()
)
basOspfNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfNbrHelloSuppressed.setStatus("current")
_BasOspfNbrChassis_Type = BasChassisId
_BasOspfNbrChassis_Object = MibTableColumn
basOspfNbrChassis = _BasOspfNbrChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 12),
    _BasOspfNbrChassis_Type()
)
basOspfNbrChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfNbrChassis.setStatus("current")
_BasOspfNbrSlot_Type = BasSlotId
_BasOspfNbrSlot_Object = MibTableColumn
basOspfNbrSlot = _BasOspfNbrSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 13),
    _BasOspfNbrSlot_Type()
)
basOspfNbrSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfNbrSlot.setStatus("current")
_BasOspfNbrIf_Type = BasInterfaceId
_BasOspfNbrIf_Object = MibTableColumn
basOspfNbrIf = _BasOspfNbrIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 14),
    _BasOspfNbrIf_Type()
)
basOspfNbrIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfNbrIf.setStatus("current")
_BasOspfNbrLPort_Type = BasLogicalPortId
_BasOspfNbrLPort_Object = MibTableColumn
basOspfNbrLPort = _BasOspfNbrLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 10, 1, 15),
    _BasOspfNbrLPort_Type()
)
basOspfNbrLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfNbrLPort.setStatus("current")
_BasOspfVirtNbrTable_Object = MibTable
basOspfVirtNbrTable = _BasOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11)
)
if mibBuilder.loadTexts:
    basOspfVirtNbrTable.setStatus("current")
_BasOspfVirtNbrEntry_Object = MibTableRow
basOspfVirtNbrEntry = _BasOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1)
)
basOspfVirtNbrEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfVirtNbrChassis"),
    (0, "BAS-OSPF-MIB", "basOspfVirtNbrSlot"),
    (0, "BAS-OSPF-MIB", "basOspfVirtNbrIf"),
    (0, "BAS-OSPF-MIB", "basOspfVirtNbrLPort"),
    (0, "BAS-OSPF-MIB", "basOspfVirtNbrArea"),
    (0, "BAS-OSPF-MIB", "basOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    basOspfVirtNbrEntry.setStatus("current")
_BasOspfVirtNbrArea_Type = AreaID
_BasOspfVirtNbrArea_Object = MibTableColumn
basOspfVirtNbrArea = _BasOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 1),
    _BasOspfVirtNbrArea_Type()
)
basOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtNbrArea.setStatus("current")
_BasOspfVirtNbrRtrId_Type = RouterID
_BasOspfVirtNbrRtrId_Object = MibTableColumn
basOspfVirtNbrRtrId = _BasOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 2),
    _BasOspfVirtNbrRtrId_Type()
)
basOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtNbrRtrId.setStatus("current")
_BasOspfVirtNbrIpAddr_Type = IpAddress
_BasOspfVirtNbrIpAddr_Object = MibTableColumn
basOspfVirtNbrIpAddr = _BasOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 3),
    _BasOspfVirtNbrIpAddr_Type()
)
basOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtNbrIpAddr.setStatus("current")
_BasOspfVirtNbrOptions_Type = Integer32
_BasOspfVirtNbrOptions_Object = MibTableColumn
basOspfVirtNbrOptions = _BasOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 4),
    _BasOspfVirtNbrOptions_Type()
)
basOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtNbrOptions.setStatus("current")


class _BasOspfVirtNbrState_Type(Integer32):
    """Custom type basOspfVirtNbrState based on Integer32"""
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


_BasOspfVirtNbrState_Type.__name__ = "Integer32"
_BasOspfVirtNbrState_Object = MibTableColumn
basOspfVirtNbrState = _BasOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 5),
    _BasOspfVirtNbrState_Type()
)
basOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtNbrState.setStatus("current")
_BasOspfVirtNbrEvents_Type = Counter32
_BasOspfVirtNbrEvents_Object = MibTableColumn
basOspfVirtNbrEvents = _BasOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 6),
    _BasOspfVirtNbrEvents_Type()
)
basOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtNbrEvents.setStatus("current")
_BasOspfVirtNbrLsRetransQLen_Type = Gauge32
_BasOspfVirtNbrLsRetransQLen_Object = MibTableColumn
basOspfVirtNbrLsRetransQLen = _BasOspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 7),
    _BasOspfVirtNbrLsRetransQLen_Type()
)
basOspfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtNbrLsRetransQLen.setStatus("current")
_BasOspfVirtNbrHelloSuppressed_Type = TruthValue
_BasOspfVirtNbrHelloSuppressed_Object = MibTableColumn
basOspfVirtNbrHelloSuppressed = _BasOspfVirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 8),
    _BasOspfVirtNbrHelloSuppressed_Type()
)
basOspfVirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfVirtNbrHelloSuppressed.setStatus("current")
_BasOspfVirtNbrChassis_Type = BasChassisId
_BasOspfVirtNbrChassis_Object = MibTableColumn
basOspfVirtNbrChassis = _BasOspfVirtNbrChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 9),
    _BasOspfVirtNbrChassis_Type()
)
basOspfVirtNbrChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfVirtNbrChassis.setStatus("current")
_BasOspfVirtNbrSlot_Type = BasSlotId
_BasOspfVirtNbrSlot_Object = MibTableColumn
basOspfVirtNbrSlot = _BasOspfVirtNbrSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 10),
    _BasOspfVirtNbrSlot_Type()
)
basOspfVirtNbrSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfVirtNbrSlot.setStatus("current")
_BasOspfVirtNbrIf_Type = BasInterfaceId
_BasOspfVirtNbrIf_Object = MibTableColumn
basOspfVirtNbrIf = _BasOspfVirtNbrIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 11),
    _BasOspfVirtNbrIf_Type()
)
basOspfVirtNbrIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfVirtNbrIf.setStatus("current")
_BasOspfVirtNbrLPort_Type = BasLogicalPortId
_BasOspfVirtNbrLPort_Object = MibTableColumn
basOspfVirtNbrLPort = _BasOspfVirtNbrLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 11, 1, 12),
    _BasOspfVirtNbrLPort_Type()
)
basOspfVirtNbrLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfVirtNbrLPort.setStatus("current")
_BasOspfExtLsdbTable_Object = MibTable
basOspfExtLsdbTable = _BasOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12)
)
if mibBuilder.loadTexts:
    basOspfExtLsdbTable.setStatus("current")
_BasOspfExtLsdbEntry_Object = MibTableRow
basOspfExtLsdbEntry = _BasOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1)
)
basOspfExtLsdbEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfExtLsdbChassis"),
    (0, "BAS-OSPF-MIB", "basOspfExtLsdbSlot"),
    (0, "BAS-OSPF-MIB", "basOspfExtLsdbIf"),
    (0, "BAS-OSPF-MIB", "basOspfExtLsdbLPort"),
    (0, "BAS-OSPF-MIB", "basOspfExtLsdbType"),
    (0, "BAS-OSPF-MIB", "basOspfExtLsdbLsid"),
    (0, "BAS-OSPF-MIB", "basOspfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    basOspfExtLsdbEntry.setStatus("current")


class _BasOspfExtLsdbType_Type(Integer32):
    """Custom type basOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_BasOspfExtLsdbType_Type.__name__ = "Integer32"
_BasOspfExtLsdbType_Object = MibTableColumn
basOspfExtLsdbType = _BasOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1, 1),
    _BasOspfExtLsdbType_Type()
)
basOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfExtLsdbType.setStatus("current")
_BasOspfExtLsdbLsid_Type = IpAddress
_BasOspfExtLsdbLsid_Object = MibTableColumn
basOspfExtLsdbLsid = _BasOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1, 2),
    _BasOspfExtLsdbLsid_Type()
)
basOspfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfExtLsdbLsid.setStatus("current")
_BasOspfExtLsdbRouterId_Type = RouterID
_BasOspfExtLsdbRouterId_Object = MibTableColumn
basOspfExtLsdbRouterId = _BasOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1, 3),
    _BasOspfExtLsdbRouterId_Type()
)
basOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfExtLsdbRouterId.setStatus("current")
_BasOspfExtLsdbSequence_Type = Integer32
_BasOspfExtLsdbSequence_Object = MibTableColumn
basOspfExtLsdbSequence = _BasOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1, 4),
    _BasOspfExtLsdbSequence_Type()
)
basOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfExtLsdbSequence.setStatus("current")
_BasOspfExtLsdbAge_Type = Integer32
_BasOspfExtLsdbAge_Object = MibTableColumn
basOspfExtLsdbAge = _BasOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1, 5),
    _BasOspfExtLsdbAge_Type()
)
basOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfExtLsdbAge.setStatus("current")
_BasOspfExtLsdbChecksum_Type = Integer32
_BasOspfExtLsdbChecksum_Object = MibTableColumn
basOspfExtLsdbChecksum = _BasOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1, 6),
    _BasOspfExtLsdbChecksum_Type()
)
basOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfExtLsdbChecksum.setStatus("current")


class _BasOspfExtLsdbAdvertisement_Type(OctetString):
    """Custom type basOspfExtLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )


_BasOspfExtLsdbAdvertisement_Type.__name__ = "OctetString"
_BasOspfExtLsdbAdvertisement_Object = MibTableColumn
basOspfExtLsdbAdvertisement = _BasOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1, 7),
    _BasOspfExtLsdbAdvertisement_Type()
)
basOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfExtLsdbAdvertisement.setStatus("current")
_BasOspfExtLsdbChassis_Type = BasChassisId
_BasOspfExtLsdbChassis_Object = MibTableColumn
basOspfExtLsdbChassis = _BasOspfExtLsdbChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1, 8),
    _BasOspfExtLsdbChassis_Type()
)
basOspfExtLsdbChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfExtLsdbChassis.setStatus("current")
_BasOspfExtLsdbSlot_Type = BasSlotId
_BasOspfExtLsdbSlot_Object = MibTableColumn
basOspfExtLsdbSlot = _BasOspfExtLsdbSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1, 9),
    _BasOspfExtLsdbSlot_Type()
)
basOspfExtLsdbSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfExtLsdbSlot.setStatus("current")
_BasOspfExtLsdbIf_Type = BasInterfaceId
_BasOspfExtLsdbIf_Object = MibTableColumn
basOspfExtLsdbIf = _BasOspfExtLsdbIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1, 10),
    _BasOspfExtLsdbIf_Type()
)
basOspfExtLsdbIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfExtLsdbIf.setStatus("current")
_BasOspfExtLsdbLPort_Type = BasLogicalPortId
_BasOspfExtLsdbLPort_Object = MibTableColumn
basOspfExtLsdbLPort = _BasOspfExtLsdbLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 12, 1, 11),
    _BasOspfExtLsdbLPort_Type()
)
basOspfExtLsdbLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfExtLsdbLPort.setStatus("current")
_BasOspfRouteGroup_ObjectIdentity = ObjectIdentity
basOspfRouteGroup = _BasOspfRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 13)
)
_BasOspfIntraArea_ObjectIdentity = ObjectIdentity
basOspfIntraArea = _BasOspfIntraArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 13, 1)
)
_BasOspfInterArea_ObjectIdentity = ObjectIdentity
basOspfInterArea = _BasOspfInterArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 13, 2)
)
_BasOspfExternalType1_ObjectIdentity = ObjectIdentity
basOspfExternalType1 = _BasOspfExternalType1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 13, 3)
)
_BasOspfExternalType2_ObjectIdentity = ObjectIdentity
basOspfExternalType2 = _BasOspfExternalType2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 13, 4)
)
_BasOspfAreaAggregateTable_Object = MibTable
basOspfAreaAggregateTable = _BasOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14)
)
if mibBuilder.loadTexts:
    basOspfAreaAggregateTable.setStatus("current")
_BasOspfAreaAggregateEntry_Object = MibTableRow
basOspfAreaAggregateEntry = _BasOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14, 1)
)
basOspfAreaAggregateEntry.setIndexNames(
    (0, "BAS-OSPF-MIB", "basOspfAreaAggregateChassis"),
    (0, "BAS-OSPF-MIB", "basOspfAreaAggregateSlot"),
    (0, "BAS-OSPF-MIB", "basOspfAreaAggregateIf"),
    (0, "BAS-OSPF-MIB", "basOspfAreaAggregateLPort"),
    (0, "BAS-OSPF-MIB", "basOspfAreaAggregateAreaID"),
    (0, "BAS-OSPF-MIB", "basOspfAreaAggregateLsdbType"),
    (0, "BAS-OSPF-MIB", "basOspfAreaAggregateNet"),
    (0, "BAS-OSPF-MIB", "basOspfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    basOspfAreaAggregateEntry.setStatus("current")
_BasOspfAreaAggregateAreaID_Type = AreaID
_BasOspfAreaAggregateAreaID_Object = MibTableColumn
basOspfAreaAggregateAreaID = _BasOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14, 1, 1),
    _BasOspfAreaAggregateAreaID_Type()
)
basOspfAreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfAreaAggregateAreaID.setStatus("current")


class _BasOspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type basOspfAreaAggregateLsdbType based on Integer32"""
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


_BasOspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_BasOspfAreaAggregateLsdbType_Object = MibTableColumn
basOspfAreaAggregateLsdbType = _BasOspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14, 1, 2),
    _BasOspfAreaAggregateLsdbType_Type()
)
basOspfAreaAggregateLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfAreaAggregateLsdbType.setStatus("current")
_BasOspfAreaAggregateNet_Type = IpAddress
_BasOspfAreaAggregateNet_Object = MibTableColumn
basOspfAreaAggregateNet = _BasOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14, 1, 3),
    _BasOspfAreaAggregateNet_Type()
)
basOspfAreaAggregateNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfAreaAggregateNet.setStatus("current")
_BasOspfAreaAggregateMask_Type = IpAddress
_BasOspfAreaAggregateMask_Object = MibTableColumn
basOspfAreaAggregateMask = _BasOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14, 1, 4),
    _BasOspfAreaAggregateMask_Type()
)
basOspfAreaAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basOspfAreaAggregateMask.setStatus("current")
_BasOspfAreaAggregateStatus_Type = RowStatus
_BasOspfAreaAggregateStatus_Object = MibTableColumn
basOspfAreaAggregateStatus = _BasOspfAreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14, 1, 5),
    _BasOspfAreaAggregateStatus_Type()
)
basOspfAreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfAreaAggregateStatus.setStatus("current")


class _BasOspfAreaAggregateEffect_Type(Integer32):
    """Custom type basOspfAreaAggregateEffect based on Integer32"""
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


_BasOspfAreaAggregateEffect_Type.__name__ = "Integer32"
_BasOspfAreaAggregateEffect_Object = MibTableColumn
basOspfAreaAggregateEffect = _BasOspfAreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14, 1, 6),
    _BasOspfAreaAggregateEffect_Type()
)
basOspfAreaAggregateEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basOspfAreaAggregateEffect.setStatus("current")
_BasOspfAreaAggregateChassis_Type = BasChassisId
_BasOspfAreaAggregateChassis_Object = MibTableColumn
basOspfAreaAggregateChassis = _BasOspfAreaAggregateChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14, 1, 7),
    _BasOspfAreaAggregateChassis_Type()
)
basOspfAreaAggregateChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfAreaAggregateChassis.setStatus("current")
_BasOspfAreaAggregateSlot_Type = BasSlotId
_BasOspfAreaAggregateSlot_Object = MibTableColumn
basOspfAreaAggregateSlot = _BasOspfAreaAggregateSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14, 1, 8),
    _BasOspfAreaAggregateSlot_Type()
)
basOspfAreaAggregateSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfAreaAggregateSlot.setStatus("current")
_BasOspfAreaAggregateIf_Type = BasInterfaceId
_BasOspfAreaAggregateIf_Object = MibTableColumn
basOspfAreaAggregateIf = _BasOspfAreaAggregateIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14, 1, 9),
    _BasOspfAreaAggregateIf_Type()
)
basOspfAreaAggregateIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfAreaAggregateIf.setStatus("current")
_BasOspfAreaAggregateLPort_Type = BasLogicalPortId
_BasOspfAreaAggregateLPort_Object = MibTableColumn
basOspfAreaAggregateLPort = _BasOspfAreaAggregateLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 7, 1, 14, 1, 10),
    _BasOspfAreaAggregateLPort_Type()
)
basOspfAreaAggregateLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basOspfAreaAggregateLPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-OSPF-MIB",
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
       "basOspf": basOspf,
       "basOspfObjects": basOspfObjects,
       "basOspfGeneralGroupTable": basOspfGeneralGroupTable,
       "basOspfGeneralGroupEntry": basOspfGeneralGroupEntry,
       "basOspfRouterId": basOspfRouterId,
       "basOspfAdminStat": basOspfAdminStat,
       "basOspfVersionNumber": basOspfVersionNumber,
       "basOspfAreaBdrRtrStatus": basOspfAreaBdrRtrStatus,
       "basOspfASBdrRtrStatus": basOspfASBdrRtrStatus,
       "basOspfExternLsaCount": basOspfExternLsaCount,
       "basOspfExternLsaCksumSum": basOspfExternLsaCksumSum,
       "basOspfTOSSupport": basOspfTOSSupport,
       "basOspfOriginateNewLsas": basOspfOriginateNewLsas,
       "basOspfRxNewLsas": basOspfRxNewLsas,
       "basOspfExtLsdbLimit": basOspfExtLsdbLimit,
       "basOspfMulticastExtensions": basOspfMulticastExtensions,
       "basOspfExitOverflowInterval": basOspfExitOverflowInterval,
       "basOspfDemandExtensions": basOspfDemandExtensions,
       "basOspfGeneralGroupChassis": basOspfGeneralGroupChassis,
       "basOspfGeneralGroupSlot": basOspfGeneralGroupSlot,
       "basOspfGeneralGroupIf": basOspfGeneralGroupIf,
       "basOspfGeneralGroupLPort": basOspfGeneralGroupLPort,
       "basOspfAreaTable": basOspfAreaTable,
       "basOspfAreaEntry": basOspfAreaEntry,
       "basOspfAreaId": basOspfAreaId,
       "basOspfAuthType": basOspfAuthType,
       "basOspfImportAsExtern": basOspfImportAsExtern,
       "basOspfSpfRuns": basOspfSpfRuns,
       "basOspfAreaBdrRtrCount": basOspfAreaBdrRtrCount,
       "basOspfAsBdrRtrCount": basOspfAsBdrRtrCount,
       "basOspfAreaLsaCount": basOspfAreaLsaCount,
       "basOspfAreaLsaCksumSum": basOspfAreaLsaCksumSum,
       "basOspfAreaSummary": basOspfAreaSummary,
       "basOspfAreaStatus": basOspfAreaStatus,
       "basOspfAreaChassis": basOspfAreaChassis,
       "basOspfAreaSlot": basOspfAreaSlot,
       "basOspfAreaIf": basOspfAreaIf,
       "basOspfAreaLPort": basOspfAreaLPort,
       "basOspfStubAreaTable": basOspfStubAreaTable,
       "basOspfStubAreaEntry": basOspfStubAreaEntry,
       "basOspfStubAreaId": basOspfStubAreaId,
       "basOspfStubTOS": basOspfStubTOS,
       "basOspfStubMetric": basOspfStubMetric,
       "basOspfStubStatus": basOspfStubStatus,
       "basOspfStubMetricType": basOspfStubMetricType,
       "basOspfStubAreaChassis": basOspfStubAreaChassis,
       "basOspfStubAreaSlot": basOspfStubAreaSlot,
       "basOspfStubAreaIf": basOspfStubAreaIf,
       "basOspfStubAreaLPort": basOspfStubAreaLPort,
       "basOspfLsdbTable": basOspfLsdbTable,
       "basOspfLsdbEntry": basOspfLsdbEntry,
       "basOspfLsdbAreaId": basOspfLsdbAreaId,
       "basOspfLsdbType": basOspfLsdbType,
       "basOspfLsdbLsid": basOspfLsdbLsid,
       "basOspfLsdbRouterId": basOspfLsdbRouterId,
       "basOspfLsdbSequence": basOspfLsdbSequence,
       "basOspfLsdbAge": basOspfLsdbAge,
       "basOspfLsdbChecksum": basOspfLsdbChecksum,
       "basOspfLsdbAdvertisement": basOspfLsdbAdvertisement,
       "basOspfLsdbChassis": basOspfLsdbChassis,
       "basOspfLsdbSlot": basOspfLsdbSlot,
       "basOspfLsdbIf": basOspfLsdbIf,
       "basOspfLsdbLPort": basOspfLsdbLPort,
       "basOspfHostTable": basOspfHostTable,
       "basOspfHostEntry": basOspfHostEntry,
       "basOspfHostIpAddress": basOspfHostIpAddress,
       "basOspfHostTOS": basOspfHostTOS,
       "basOspfHostMetric": basOspfHostMetric,
       "basOspfHostStatus": basOspfHostStatus,
       "basOspfHostAreaID": basOspfHostAreaID,
       "basOspfHostChassis": basOspfHostChassis,
       "basOspfHostSlot": basOspfHostSlot,
       "basOspfHostIf": basOspfHostIf,
       "basOspfHostLPort": basOspfHostLPort,
       "basOspfIfTable": basOspfIfTable,
       "basOspfIfEntry": basOspfIfEntry,
       "basOspfIfIpAddress": basOspfIfIpAddress,
       "basOspfAddressLessIf": basOspfAddressLessIf,
       "basOspfIfAreaId": basOspfIfAreaId,
       "basOspfIfType": basOspfIfType,
       "basOspfIfAdminStat": basOspfIfAdminStat,
       "basOspfIfRtrPriority": basOspfIfRtrPriority,
       "basOspfIfTransitDelay": basOspfIfTransitDelay,
       "basOspfIfRetransInterval": basOspfIfRetransInterval,
       "basOspfIfHelloInterval": basOspfIfHelloInterval,
       "basOspfIfRtrDeadInterval": basOspfIfRtrDeadInterval,
       "basOspfIfPollInterval": basOspfIfPollInterval,
       "basOspfIfState": basOspfIfState,
       "basOspfIfDesignatedRouter": basOspfIfDesignatedRouter,
       "basOspfIfBackupDesignatedRouter": basOspfIfBackupDesignatedRouter,
       "basOspfIfEvents": basOspfIfEvents,
       "basOspfIfAuthKey": basOspfIfAuthKey,
       "basOspfIfStatus": basOspfIfStatus,
       "basOspfIfMulticastForwarding": basOspfIfMulticastForwarding,
       "basOspfIfDemand": basOspfIfDemand,
       "basOspfIfAuthType": basOspfIfAuthType,
       "basOspfIfChassis": basOspfIfChassis,
       "basOspfIfSlot": basOspfIfSlot,
       "basOspfIfIf": basOspfIfIf,
       "basOspfIfLPort": basOspfIfLPort,
       "basOspfIfMetricTable": basOspfIfMetricTable,
       "basOspfIfMetricEntry": basOspfIfMetricEntry,
       "basOspfIfMetricIpAddress": basOspfIfMetricIpAddress,
       "basOspfIfMetricAddressLessIf": basOspfIfMetricAddressLessIf,
       "basOspfIfMetricTOS": basOspfIfMetricTOS,
       "basOspfIfMetricValue": basOspfIfMetricValue,
       "basOspfIfMetricStatus": basOspfIfMetricStatus,
       "basOspfIfMetricChassis": basOspfIfMetricChassis,
       "basOspfIfMetricSlot": basOspfIfMetricSlot,
       "basOspfIfMetricIf": basOspfIfMetricIf,
       "basOspfIfMetricLPort": basOspfIfMetricLPort,
       "basOspfVirtIfTable": basOspfVirtIfTable,
       "basOspfVirtIfEntry": basOspfVirtIfEntry,
       "basOspfVirtIfAreaId": basOspfVirtIfAreaId,
       "basOspfVirtIfNeighbor": basOspfVirtIfNeighbor,
       "basOspfVirtIfTransitDelay": basOspfVirtIfTransitDelay,
       "basOspfVirtIfRetransInterval": basOspfVirtIfRetransInterval,
       "basOspfVirtIfHelloInterval": basOspfVirtIfHelloInterval,
       "basOspfVirtIfRtrDeadInterval": basOspfVirtIfRtrDeadInterval,
       "basOspfVirtIfState": basOspfVirtIfState,
       "basOspfVirtIfEvents": basOspfVirtIfEvents,
       "basOspfVirtIfAuthKey": basOspfVirtIfAuthKey,
       "basOspfVirtIfStatus": basOspfVirtIfStatus,
       "basOspfVirtIfAuthType": basOspfVirtIfAuthType,
       "basOspfVirtIfChassis": basOspfVirtIfChassis,
       "basOspfVirtIfSlot": basOspfVirtIfSlot,
       "basOspfVirtIfIf": basOspfVirtIfIf,
       "basOspfVirtIfLPort": basOspfVirtIfLPort,
       "basOspfNbrTable": basOspfNbrTable,
       "basOspfNbrEntry": basOspfNbrEntry,
       "basOspfNbrIpAddr": basOspfNbrIpAddr,
       "basOspfNbrAddressLessIndex": basOspfNbrAddressLessIndex,
       "basOspfNbrRtrId": basOspfNbrRtrId,
       "basOspfNbrOptions": basOspfNbrOptions,
       "basOspfNbrPriority": basOspfNbrPriority,
       "basOspfNbrState": basOspfNbrState,
       "basOspfNbrEvents": basOspfNbrEvents,
       "basOspfNbrLsRetransQLen": basOspfNbrLsRetransQLen,
       "basOspfNbmaNbrStatus": basOspfNbmaNbrStatus,
       "basOspfNbmaNbrPermanence": basOspfNbmaNbrPermanence,
       "basOspfNbrHelloSuppressed": basOspfNbrHelloSuppressed,
       "basOspfNbrChassis": basOspfNbrChassis,
       "basOspfNbrSlot": basOspfNbrSlot,
       "basOspfNbrIf": basOspfNbrIf,
       "basOspfNbrLPort": basOspfNbrLPort,
       "basOspfVirtNbrTable": basOspfVirtNbrTable,
       "basOspfVirtNbrEntry": basOspfVirtNbrEntry,
       "basOspfVirtNbrArea": basOspfVirtNbrArea,
       "basOspfVirtNbrRtrId": basOspfVirtNbrRtrId,
       "basOspfVirtNbrIpAddr": basOspfVirtNbrIpAddr,
       "basOspfVirtNbrOptions": basOspfVirtNbrOptions,
       "basOspfVirtNbrState": basOspfVirtNbrState,
       "basOspfVirtNbrEvents": basOspfVirtNbrEvents,
       "basOspfVirtNbrLsRetransQLen": basOspfVirtNbrLsRetransQLen,
       "basOspfVirtNbrHelloSuppressed": basOspfVirtNbrHelloSuppressed,
       "basOspfVirtNbrChassis": basOspfVirtNbrChassis,
       "basOspfVirtNbrSlot": basOspfVirtNbrSlot,
       "basOspfVirtNbrIf": basOspfVirtNbrIf,
       "basOspfVirtNbrLPort": basOspfVirtNbrLPort,
       "basOspfExtLsdbTable": basOspfExtLsdbTable,
       "basOspfExtLsdbEntry": basOspfExtLsdbEntry,
       "basOspfExtLsdbType": basOspfExtLsdbType,
       "basOspfExtLsdbLsid": basOspfExtLsdbLsid,
       "basOspfExtLsdbRouterId": basOspfExtLsdbRouterId,
       "basOspfExtLsdbSequence": basOspfExtLsdbSequence,
       "basOspfExtLsdbAge": basOspfExtLsdbAge,
       "basOspfExtLsdbChecksum": basOspfExtLsdbChecksum,
       "basOspfExtLsdbAdvertisement": basOspfExtLsdbAdvertisement,
       "basOspfExtLsdbChassis": basOspfExtLsdbChassis,
       "basOspfExtLsdbSlot": basOspfExtLsdbSlot,
       "basOspfExtLsdbIf": basOspfExtLsdbIf,
       "basOspfExtLsdbLPort": basOspfExtLsdbLPort,
       "basOspfRouteGroup": basOspfRouteGroup,
       "basOspfIntraArea": basOspfIntraArea,
       "basOspfInterArea": basOspfInterArea,
       "basOspfExternalType1": basOspfExternalType1,
       "basOspfExternalType2": basOspfExternalType2,
       "basOspfAreaAggregateTable": basOspfAreaAggregateTable,
       "basOspfAreaAggregateEntry": basOspfAreaAggregateEntry,
       "basOspfAreaAggregateAreaID": basOspfAreaAggregateAreaID,
       "basOspfAreaAggregateLsdbType": basOspfAreaAggregateLsdbType,
       "basOspfAreaAggregateNet": basOspfAreaAggregateNet,
       "basOspfAreaAggregateMask": basOspfAreaAggregateMask,
       "basOspfAreaAggregateStatus": basOspfAreaAggregateStatus,
       "basOspfAreaAggregateEffect": basOspfAreaAggregateEffect,
       "basOspfAreaAggregateChassis": basOspfAreaAggregateChassis,
       "basOspfAreaAggregateSlot": basOspfAreaAggregateSlot,
       "basOspfAreaAggregateIf": basOspfAreaAggregateIf,
       "basOspfAreaAggregateLPort": basOspfAreaAggregateLPort}
)

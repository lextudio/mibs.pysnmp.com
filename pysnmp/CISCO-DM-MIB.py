# SNMP MIB module (CISCO-DM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:13 2024
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

(cffFcFeElementName,) = mibBuilder.importSymbols(
    "CISCO-FC-FE-MIB",
    "cffFcFeElementName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(DomainId,
 DomainIdOrZero,
 FcAddressId,
 FcNameId,
 FcNameIdOrZero) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "DomainId",
    "DomainIdOrZero",
    "FcAddressId",
    "FcNameId",
    "FcNameIdOrZero")

(notifyVsanIndex,
 vsanIndex) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "notifyVsanIndex",
    "vsanIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoDmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 302)
)
ciscoDmMIB.setRevisions(
        ("2003-09-22 00:00",
         "2003-06-20 00:00",
         "2003-02-27 00:00",
         "2003-02-21 00:00",
         "2003-01-28 00:00",
         "2003-01-02 00:00",
         "2002-10-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DomainPriority(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class DomainPriorityOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class DomainInterfaceRole(Integer32, TextualConvention):
    status = "current"
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
        *(("down", 5),
          ("isolated", 4),
          ("nonPrincipal", 1),
          ("principalDownsteam", 3),
          ("principalUpstream", 2),
          ("unknown", 6))
    )



class DmState(Integer32, TextualConvention):
    status = "current"
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("buildFabricPhase", 5),
          ("disabled", 11),
          ("domainIdDistribution", 4),
          ("noDomains", 10),
          ("principalSwitchSelection", 3),
          ("reconfigureFabricPhase", 6),
          ("stable", 7),
          ("stableWithDomainConfigured", 9),
          ("stableWithNoEports", 8),
          ("starting", 1),
          ("suspended", 12),
          ("unconfigured", 2),
          ("unknown", 13))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDmMIBObjects = _CiscoDmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1)
)
_DmConfiguration_ObjectIdentity = ObjectIdentity
dmConfiguration = _DmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1)
)
_DmTable_Object = MibTable
dmTable = _DmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dmTable.setStatus("current")
_DmEntry_Object = MibTableRow
dmEntry = _DmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1)
)
dmEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    dmEntry.setStatus("current")


class _DmConfigDomainId_Type(DomainIdOrZero):
    """Custom type dmConfigDomainId based on DomainIdOrZero"""
    defaultValue = 0


_DmConfigDomainId_Object = MibTableColumn
dmConfigDomainId = _DmConfigDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 1),
    _DmConfigDomainId_Type()
)
dmConfigDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmConfigDomainId.setStatus("current")


class _DmConfigDomainIdType_Type(Integer32):
    """Custom type dmConfigDomainIdType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preferred", 2),
          ("static", 1))
    )


_DmConfigDomainIdType_Type.__name__ = "Integer32"
_DmConfigDomainIdType_Object = MibTableColumn
dmConfigDomainIdType = _DmConfigDomainIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 2),
    _DmConfigDomainIdType_Type()
)
dmConfigDomainIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmConfigDomainIdType.setStatus("current")


class _DmEnable_Type(TruthValue):
    """Custom type dmEnable based on TruthValue"""


_DmEnable_Object = MibTableColumn
dmEnable = _DmEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 3),
    _DmEnable_Type()
)
dmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmEnable.setStatus("current")


class _DmAutoReconfigure_Type(TruthValue):
    """Custom type dmAutoReconfigure based on TruthValue"""


_DmAutoReconfigure_Object = MibTableColumn
dmAutoReconfigure = _DmAutoReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 4),
    _DmAutoReconfigure_Type()
)
dmAutoReconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmAutoReconfigure.setStatus("current")
_DmContiguousAllocation_Type = TruthValue
_DmContiguousAllocation_Object = MibTableColumn
dmContiguousAllocation = _DmContiguousAllocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 5),
    _DmContiguousAllocation_Type()
)
dmContiguousAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmContiguousAllocation.setStatus("current")
_DmPriority_Type = DomainPriority
_DmPriority_Object = MibTableColumn
dmPriority = _DmPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 6),
    _DmPriority_Type()
)
dmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmPriority.setStatus("current")


class _DmRestart_Type(Integer32):
    """Custom type dmRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disruptive", 2),
          ("noOp", 3),
          ("nonDisruptive", 1))
    )


_DmRestart_Type.__name__ = "Integer32"
_DmRestart_Object = MibTableColumn
dmRestart = _DmRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 7),
    _DmRestart_Type()
)
dmRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmRestart.setStatus("current")


class _DmFabricName_Type(FcNameIdOrZero):
    """Custom type dmFabricName based on FcNameIdOrZero"""
    defaultHexValue = "20010005300028df"


_DmFabricName_Object = MibTableColumn
dmFabricName = _DmFabricName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 8),
    _DmFabricName_Type()
)
dmFabricName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmFabricName.setStatus("current")


class _DmPrincipalSwitchWwn_Type(FcNameIdOrZero):
    """Custom type dmPrincipalSwitchWwn based on FcNameIdOrZero"""
    defaultHexValue = ""


_DmPrincipalSwitchWwn_Object = MibTableColumn
dmPrincipalSwitchWwn = _DmPrincipalSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 9),
    _DmPrincipalSwitchWwn_Type()
)
dmPrincipalSwitchWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmPrincipalSwitchWwn.setStatus("current")
_DmLocalSwitchWwn_Type = FcNameIdOrZero
_DmLocalSwitchWwn_Object = MibTableColumn
dmLocalSwitchWwn = _DmLocalSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 10),
    _DmLocalSwitchWwn_Type()
)
dmLocalSwitchWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmLocalSwitchWwn.setStatus("current")


class _DmAssignedAreaIdList_Type(OctetString):
    """Custom type dmAssignedAreaIdList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DmAssignedAreaIdList_Type.__name__ = "OctetString"
_DmAssignedAreaIdList_Object = MibTableColumn
dmAssignedAreaIdList = _DmAssignedAreaIdList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 11),
    _DmAssignedAreaIdList_Type()
)
dmAssignedAreaIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmAssignedAreaIdList.setStatus("current")
_DmFcIdsGranted_Type = Counter32
_DmFcIdsGranted_Object = MibTableColumn
dmFcIdsGranted = _DmFcIdsGranted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 12),
    _DmFcIdsGranted_Type()
)
dmFcIdsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmFcIdsGranted.setStatus("current")
_DmFcIdsRecovered_Type = Counter32
_DmFcIdsRecovered_Object = MibTableColumn
dmFcIdsRecovered = _DmFcIdsRecovered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 13),
    _DmFcIdsRecovered_Type()
)
dmFcIdsRecovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmFcIdsRecovered.setStatus("current")
_DmFreeFcIds_Type = Gauge32
_DmFreeFcIds_Object = MibTableColumn
dmFreeFcIds = _DmFreeFcIds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 14),
    _DmFreeFcIds_Type()
)
dmFreeFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmFreeFcIds.setStatus("current")
_DmAssignedFcIds_Type = Gauge32
_DmAssignedFcIds_Object = MibTableColumn
dmAssignedFcIds = _DmAssignedFcIds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 15),
    _DmAssignedFcIds_Type()
)
dmAssignedFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmAssignedFcIds.setStatus("current")
_DmReservedFcIds_Type = Gauge32
_DmReservedFcIds_Object = MibTableColumn
dmReservedFcIds = _DmReservedFcIds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 16),
    _DmReservedFcIds_Type()
)
dmReservedFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmReservedFcIds.setStatus("current")
_DmRunningPriority_Type = DomainPriority
_DmRunningPriority_Object = MibTableColumn
dmRunningPriority = _DmRunningPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 17),
    _DmRunningPriority_Type()
)
dmRunningPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmRunningPriority.setStatus("current")
_DmPrincSwRunningPriority_Type = DomainPriority
_DmPrincSwRunningPriority_Object = MibTableColumn
dmPrincSwRunningPriority = _DmPrincSwRunningPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 18),
    _DmPrincSwRunningPriority_Type()
)
dmPrincSwRunningPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmPrincSwRunningPriority.setStatus("current")
_DmState_Type = DmState
_DmState_Object = MibTableColumn
dmState = _DmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 19),
    _DmState_Type()
)
dmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmState.setStatus("current")
_DmPrincipalSwitchSelections_Type = Counter32
_DmPrincipalSwitchSelections_Object = MibTableColumn
dmPrincipalSwitchSelections = _DmPrincipalSwitchSelections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 20),
    _DmPrincipalSwitchSelections_Type()
)
dmPrincipalSwitchSelections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmPrincipalSwitchSelections.setStatus("current")
_DmBuildFabrics_Type = Counter32
_DmBuildFabrics_Object = MibTableColumn
dmBuildFabrics = _DmBuildFabrics_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 21),
    _DmBuildFabrics_Type()
)
dmBuildFabrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmBuildFabrics.setStatus("current")
_DmFabricReconfigures_Type = Counter32
_DmFabricReconfigures_Object = MibTableColumn
dmFabricReconfigures = _DmFabricReconfigures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 22),
    _DmFabricReconfigures_Type()
)
dmFabricReconfigures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmFabricReconfigures.setStatus("current")
_DmDomainId_Type = DomainIdOrZero
_DmDomainId_Object = MibTableColumn
dmDomainId = _DmDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 23),
    _DmDomainId_Type()
)
dmDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmDomainId.setStatus("current")
_DmLocalPrincipalSwitchSelctns_Type = Counter32
_DmLocalPrincipalSwitchSelctns_Object = MibTableColumn
dmLocalPrincipalSwitchSelctns = _DmLocalPrincipalSwitchSelctns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 24),
    _DmLocalPrincipalSwitchSelctns_Type()
)
dmLocalPrincipalSwitchSelctns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmLocalPrincipalSwitchSelctns.setStatus("current")


class _DmFcIdPersistency_Type(TruthValue):
    """Custom type dmFcIdPersistency based on TruthValue"""


_DmFcIdPersistency_Object = MibTableColumn
dmFcIdPersistency = _DmFcIdPersistency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 25),
    _DmFcIdPersistency_Type()
)
dmFcIdPersistency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmFcIdPersistency.setStatus("current")


class _DmFcIdPurge_Type(Integer32):
    """Custom type dmFcIdPurge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noOp", 1))
    )


_DmFcIdPurge_Type.__name__ = "Integer32"
_DmFcIdPurge_Object = MibTableColumn
dmFcIdPurge = _DmFcIdPurge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 1, 1, 26),
    _DmFcIdPurge_Type()
)
dmFcIdPurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmFcIdPurge.setStatus("current")
_DmIfTable_Object = MibTable
dmIfTable = _DmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dmIfTable.setStatus("current")
_DmIfEntry_Object = MibTableRow
dmIfEntry = _DmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 2, 1)
)
dmIfEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dmIfEntry.setStatus("current")


class _DmIfRcfReject_Type(TruthValue):
    """Custom type dmIfRcfReject based on TruthValue"""


_DmIfRcfReject_Object = MibTableColumn
dmIfRcfReject = _DmIfRcfReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 2, 1, 1),
    _DmIfRcfReject_Type()
)
dmIfRcfReject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dmIfRcfReject.setStatus("current")
_DmIfRole_Type = DomainInterfaceRole
_DmIfRole_Object = MibTableColumn
dmIfRole = _DmIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 2, 1, 2),
    _DmIfRole_Type()
)
dmIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmIfRole.setStatus("current")
_DmIfRowStatus_Type = RowStatus
_DmIfRowStatus_Object = MibTableColumn
dmIfRowStatus = _DmIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 2, 1, 3),
    _DmIfRowStatus_Type()
)
dmIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dmIfRowStatus.setStatus("current")


class _DmReConfFabricChangeNotifyEnable_Type(TruthValue):
    """Custom type dmReConfFabricChangeNotifyEnable based on TruthValue"""


_DmReConfFabricChangeNotifyEnable_Object = MibScalar
dmReConfFabricChangeNotifyEnable = _DmReConfFabricChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 3),
    _DmReConfFabricChangeNotifyEnable_Type()
)
dmReConfFabricChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmReConfFabricChangeNotifyEnable.setStatus("current")
_DmFcIdPersistencyTable_Object = MibTable
dmFcIdPersistencyTable = _DmFcIdPersistencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dmFcIdPersistencyTable.setStatus("current")
_DmFcIdPersistencyEntry_Object = MibTableRow
dmFcIdPersistencyEntry = _DmFcIdPersistencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1)
)
dmFcIdPersistencyEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-DM-MIB", "dmFcIdPersistencyWwn"),
)
if mibBuilder.loadTexts:
    dmFcIdPersistencyEntry.setStatus("current")
_DmFcIdPersistencyWwn_Type = FcNameId
_DmFcIdPersistencyWwn_Object = MibTableColumn
dmFcIdPersistencyWwn = _DmFcIdPersistencyWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 1),
    _DmFcIdPersistencyWwn_Type()
)
dmFcIdPersistencyWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dmFcIdPersistencyWwn.setStatus("current")
_DmFcIdPersistencyFcId_Type = FcAddressId
_DmFcIdPersistencyFcId_Object = MibTableColumn
dmFcIdPersistencyFcId = _DmFcIdPersistencyFcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 2),
    _DmFcIdPersistencyFcId_Type()
)
dmFcIdPersistencyFcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dmFcIdPersistencyFcId.setStatus("current")


class _DmFcIdPersistencyNum_Type(Integer32):
    """Custom type dmFcIdPersistencyNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("area", 2),
          ("one", 1))
    )


_DmFcIdPersistencyNum_Type.__name__ = "Integer32"
_DmFcIdPersistencyNum_Object = MibTableColumn
dmFcIdPersistencyNum = _DmFcIdPersistencyNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 3),
    _DmFcIdPersistencyNum_Type()
)
dmFcIdPersistencyNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dmFcIdPersistencyNum.setStatus("current")
_DmFcIdPersistencyUsed_Type = TruthValue
_DmFcIdPersistencyUsed_Object = MibTableColumn
dmFcIdPersistencyUsed = _DmFcIdPersistencyUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 4),
    _DmFcIdPersistencyUsed_Type()
)
dmFcIdPersistencyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmFcIdPersistencyUsed.setStatus("current")


class _DmFcIdPersistencyType_Type(Integer32):
    """Custom type dmFcIdPersistencyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_DmFcIdPersistencyType_Type.__name__ = "Integer32"
_DmFcIdPersistencyType_Object = MibTableColumn
dmFcIdPersistencyType = _DmFcIdPersistencyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 5),
    _DmFcIdPersistencyType_Type()
)
dmFcIdPersistencyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dmFcIdPersistencyType.setStatus("current")
_DmFcIdPersistencyRowStatus_Type = RowStatus
_DmFcIdPersistencyRowStatus_Object = MibTableColumn
dmFcIdPersistencyRowStatus = _DmFcIdPersistencyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 4, 1, 6),
    _DmFcIdPersistencyRowStatus_Type()
)
dmFcIdPersistencyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dmFcIdPersistencyRowStatus.setStatus("current")
_DmAllowedDomainIDListTable_Object = MibTable
dmAllowedDomainIDListTable = _DmAllowedDomainIDListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dmAllowedDomainIDListTable.setStatus("current")
_DmAllowedDomainIDListEntry_Object = MibTableRow
dmAllowedDomainIDListEntry = _DmAllowedDomainIDListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 5, 1)
)
dmAllowedDomainIDListEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-DM-MIB", "dmAllowedDomainIDListId"),
)
if mibBuilder.loadTexts:
    dmAllowedDomainIDListEntry.setStatus("current")


class _DmAllowedDomainIDListId_Type(Unsigned32):
    """Custom type dmAllowedDomainIDListId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DmAllowedDomainIDListId_Type.__name__ = "Unsigned32"
_DmAllowedDomainIDListId_Object = MibTableColumn
dmAllowedDomainIDListId = _DmAllowedDomainIDListId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 5, 1, 1),
    _DmAllowedDomainIDListId_Type()
)
dmAllowedDomainIDListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dmAllowedDomainIDListId.setStatus("current")


class _DmAllowedDomainIDList_Type(OctetString):
    """Custom type dmAllowedDomainIDList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DmAllowedDomainIDList_Type.__name__ = "OctetString"
_DmAllowedDomainIDList_Object = MibTableColumn
dmAllowedDomainIDList = _DmAllowedDomainIDList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 5, 1, 2),
    _DmAllowedDomainIDList_Type()
)
dmAllowedDomainIDList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmAllowedDomainIDList.setStatus("current")
_DmAllowedDomainIDListUser_Type = SnmpAdminString
_DmAllowedDomainIDListUser_Object = MibTableColumn
dmAllowedDomainIDListUser = _DmAllowedDomainIDListUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 1, 5, 1, 3),
    _DmAllowedDomainIDListUser_Type()
)
dmAllowedDomainIDListUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmAllowedDomainIDListUser.setStatus("current")
_DmInfo_ObjectIdentity = ObjectIdentity
dmInfo = _DmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2)
)
_DmAreaTable_Object = MibTable
dmAreaTable = _DmAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dmAreaTable.setStatus("current")
_DmAreaEntry_Object = MibTableRow
dmAreaEntry = _DmAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 1, 1)
)
dmAreaEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-DM-MIB", "dmAreaAreaId"),
)
if mibBuilder.loadTexts:
    dmAreaEntry.setStatus("current")


class _DmAreaAreaId_Type(Unsigned32):
    """Custom type dmAreaAreaId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DmAreaAreaId_Type.__name__ = "Unsigned32"
_DmAreaAreaId_Object = MibTableColumn
dmAreaAreaId = _DmAreaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 1, 1, 1),
    _DmAreaAreaId_Type()
)
dmAreaAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dmAreaAreaId.setStatus("current")


class _DmAreaAssignedPortIdList_Type(OctetString):
    """Custom type dmAreaAssignedPortIdList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DmAreaAssignedPortIdList_Type.__name__ = "OctetString"
_DmAreaAssignedPortIdList_Object = MibTableColumn
dmAreaAssignedPortIdList = _DmAreaAssignedPortIdList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 1, 1, 2),
    _DmAreaAssignedPortIdList_Type()
)
dmAreaAssignedPortIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmAreaAssignedPortIdList.setStatus("current")
_DmDatabaseTable_Object = MibTable
dmDatabaseTable = _DmDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dmDatabaseTable.setStatus("current")
_DmDatabaseEntry_Object = MibTableRow
dmDatabaseEntry = _DmDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 2, 1)
)
dmDatabaseEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-DM-MIB", "dmDatabaseDomainId"),
)
if mibBuilder.loadTexts:
    dmDatabaseEntry.setStatus("current")
_DmDatabaseDomainId_Type = DomainId
_DmDatabaseDomainId_Object = MibTableColumn
dmDatabaseDomainId = _DmDatabaseDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 2, 1, 1),
    _DmDatabaseDomainId_Type()
)
dmDatabaseDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dmDatabaseDomainId.setStatus("current")
_DmDatabaseSwitchWwn_Type = FcNameId
_DmDatabaseSwitchWwn_Object = MibTableColumn
dmDatabaseSwitchWwn = _DmDatabaseSwitchWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 2, 1, 2),
    _DmDatabaseSwitchWwn_Type()
)
dmDatabaseSwitchWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmDatabaseSwitchWwn.setStatus("current")


class _DmMaxFcIdCacheSize_Type(Unsigned32):
    """Custom type dmMaxFcIdCacheSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DmMaxFcIdCacheSize_Type.__name__ = "Unsigned32"
_DmMaxFcIdCacheSize_Object = MibScalar
dmMaxFcIdCacheSize = _DmMaxFcIdCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 3),
    _DmMaxFcIdCacheSize_Type()
)
dmMaxFcIdCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmMaxFcIdCacheSize.setStatus("current")
_DmFcIdCacheTable_Object = MibTable
dmFcIdCacheTable = _DmFcIdCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dmFcIdCacheTable.setStatus("current")
_DmFcIdCacheEntry_Object = MibTableRow
dmFcIdCacheEntry = _DmFcIdCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 4, 1)
)
dmFcIdCacheEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-DM-MIB", "dmFcIdCacheWwn"),
)
if mibBuilder.loadTexts:
    dmFcIdCacheEntry.setStatus("current")
_DmFcIdCacheWwn_Type = FcNameId
_DmFcIdCacheWwn_Object = MibTableColumn
dmFcIdCacheWwn = _DmFcIdCacheWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 4, 1, 1),
    _DmFcIdCacheWwn_Type()
)
dmFcIdCacheWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dmFcIdCacheWwn.setStatus("current")


class _DmFcIdCacheAreaIdPortId_Type(OctetString):
    """Custom type dmFcIdCacheAreaIdPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DmFcIdCacheAreaIdPortId_Type.__name__ = "OctetString"
_DmFcIdCacheAreaIdPortId_Object = MibTableColumn
dmFcIdCacheAreaIdPortId = _DmFcIdCacheAreaIdPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 4, 1, 2),
    _DmFcIdCacheAreaIdPortId_Type()
)
dmFcIdCacheAreaIdPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmFcIdCacheAreaIdPortId.setStatus("current")


class _DmFcIdCachePortIds_Type(Unsigned32):
    """Custom type dmFcIdCachePortIds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmFcIdCachePortIds_Type.__name__ = "Unsigned32"
_DmFcIdCachePortIds_Object = MibTableColumn
dmFcIdCachePortIds = _DmFcIdCachePortIds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 2, 4, 1, 3),
    _DmFcIdCachePortIds_Type()
)
dmFcIdCachePortIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmFcIdCachePortIds.setStatus("current")
_DmNotificationPrefix_ObjectIdentity = ObjectIdentity
dmNotificationPrefix = _DmNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 3)
)
_DmNotification_ObjectIdentity = ObjectIdentity
dmNotification = _DmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 3, 0)
)
_DmMIBConformance_ObjectIdentity = ObjectIdentity
dmMIBConformance = _DmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2)
)
_DmMIBCompliances_ObjectIdentity = ObjectIdentity
dmMIBCompliances = _DmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 1)
)
_DmMIBGroups_ObjectIdentity = ObjectIdentity
dmMIBGroups = _DmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2)
)

# Managed Objects groups

dmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 1)
)
dmGroup.setObjects(
      *(("CISCO-DM-MIB", "dmConfigDomainId"),
        ("CISCO-DM-MIB", "dmConfigDomainIdType"),
        ("CISCO-DM-MIB", "dmEnable"),
        ("CISCO-DM-MIB", "dmAutoReconfigure"),
        ("CISCO-DM-MIB", "dmContiguousAllocation"),
        ("CISCO-DM-MIB", "dmPriority"),
        ("CISCO-DM-MIB", "dmRestart"),
        ("CISCO-DM-MIB", "dmFabricName"),
        ("CISCO-DM-MIB", "dmPrincipalSwitchWwn"),
        ("CISCO-DM-MIB", "dmLocalSwitchWwn"),
        ("CISCO-DM-MIB", "dmAssignedAreaIdList"),
        ("CISCO-DM-MIB", "dmFcIdsGranted"),
        ("CISCO-DM-MIB", "dmFcIdsRecovered"),
        ("CISCO-DM-MIB", "dmFreeFcIds"),
        ("CISCO-DM-MIB", "dmAssignedFcIds"),
        ("CISCO-DM-MIB", "dmReservedFcIds"),
        ("CISCO-DM-MIB", "dmRunningPriority"),
        ("CISCO-DM-MIB", "dmPrincSwRunningPriority"),
        ("CISCO-DM-MIB", "dmState"),
        ("CISCO-DM-MIB", "dmPrincipalSwitchSelections"),
        ("CISCO-DM-MIB", "dmBuildFabrics"),
        ("CISCO-DM-MIB", "dmFabricReconfigures"),
        ("CISCO-DM-MIB", "dmDomainId"),
        ("CISCO-DM-MIB", "dmReConfFabricChangeNotifyEnable"),
        ("CISCO-DM-MIB", "dmIfRcfReject"),
        ("CISCO-DM-MIB", "dmIfRole"),
        ("CISCO-DM-MIB", "dmIfRowStatus"))
)
if mibBuilder.loadTexts:
    dmGroup.setStatus("deprecated")

dmDatabaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 2)
)
dmDatabaseGroup.setObjects(
    ("CISCO-DM-MIB", "dmDatabaseSwitchWwn")
)
if mibBuilder.loadTexts:
    dmDatabaseGroup.setStatus("current")

dmAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 3)
)
dmAreaGroup.setObjects(
    ("CISCO-DM-MIB", "dmAreaAssignedPortIdList")
)
if mibBuilder.loadTexts:
    dmAreaGroup.setStatus("current")

dmCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 4)
)
dmCacheGroup.setObjects(
      *(("CISCO-DM-MIB", "dmMaxFcIdCacheSize"),
        ("CISCO-DM-MIB", "dmFcIdCacheAreaIdPortId"),
        ("CISCO-DM-MIB", "dmFcIdCachePortIds"))
)
if mibBuilder.loadTexts:
    dmCacheGroup.setStatus("current")

dmGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 6)
)
dmGroupRev1.setObjects(
      *(("CISCO-DM-MIB", "dmConfigDomainId"),
        ("CISCO-DM-MIB", "dmConfigDomainIdType"),
        ("CISCO-DM-MIB", "dmEnable"),
        ("CISCO-DM-MIB", "dmAutoReconfigure"),
        ("CISCO-DM-MIB", "dmContiguousAllocation"),
        ("CISCO-DM-MIB", "dmPriority"),
        ("CISCO-DM-MIB", "dmRestart"),
        ("CISCO-DM-MIB", "dmFabricName"),
        ("CISCO-DM-MIB", "dmPrincipalSwitchWwn"),
        ("CISCO-DM-MIB", "dmLocalSwitchWwn"),
        ("CISCO-DM-MIB", "dmAssignedAreaIdList"),
        ("CISCO-DM-MIB", "dmFcIdsGranted"),
        ("CISCO-DM-MIB", "dmFcIdsRecovered"),
        ("CISCO-DM-MIB", "dmFreeFcIds"),
        ("CISCO-DM-MIB", "dmAssignedFcIds"),
        ("CISCO-DM-MIB", "dmReservedFcIds"),
        ("CISCO-DM-MIB", "dmRunningPriority"),
        ("CISCO-DM-MIB", "dmPrincSwRunningPriority"),
        ("CISCO-DM-MIB", "dmState"),
        ("CISCO-DM-MIB", "dmPrincipalSwitchSelections"),
        ("CISCO-DM-MIB", "dmBuildFabrics"),
        ("CISCO-DM-MIB", "dmFabricReconfigures"),
        ("CISCO-DM-MIB", "dmDomainId"),
        ("CISCO-DM-MIB", "dmLocalPrincipalSwitchSelctns"),
        ("CISCO-DM-MIB", "dmReConfFabricChangeNotifyEnable"),
        ("CISCO-DM-MIB", "dmIfRcfReject"),
        ("CISCO-DM-MIB", "dmIfRole"),
        ("CISCO-DM-MIB", "dmIfRowStatus"))
)
if mibBuilder.loadTexts:
    dmGroupRev1.setStatus("current")

dmFcIdPersistencyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 7)
)
dmFcIdPersistencyGroup.setObjects(
      *(("CISCO-DM-MIB", "dmFcIdPersistency"),
        ("CISCO-DM-MIB", "dmFcIdPurge"),
        ("CISCO-DM-MIB", "dmFcIdPersistencyFcId"),
        ("CISCO-DM-MIB", "dmFcIdPersistencyNum"),
        ("CISCO-DM-MIB", "dmFcIdPersistencyUsed"),
        ("CISCO-DM-MIB", "dmFcIdPersistencyType"),
        ("CISCO-DM-MIB", "dmFcIdPersistencyRowStatus"))
)
if mibBuilder.loadTexts:
    dmFcIdPersistencyGroup.setStatus("current")

dmDomainIDAllowedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 8)
)
dmDomainIDAllowedGroup.setObjects(
      *(("CISCO-DM-MIB", "dmAllowedDomainIDList"),
        ("CISCO-DM-MIB", "dmAllowedDomainIDListUser"))
)
if mibBuilder.loadTexts:
    dmDomainIDAllowedGroup.setStatus("current")


# Notification objects

dmDomainIdNotAssignedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 3, 0, 1)
)
dmDomainIdNotAssignedNotify.setObjects(
      *(("CISCO-VSAN-MIB", "notifyVsanIndex"),
        ("CISCO-FC-FE-MIB", "cffFcFeElementName"))
)
if mibBuilder.loadTexts:
    dmDomainIdNotAssignedNotify.setStatus(
        "current"
    )

dmNewPrincipalSwitchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 3, 0, 2)
)
dmNewPrincipalSwitchNotify.setObjects(
      *(("CISCO-VSAN-MIB", "notifyVsanIndex"),
        ("CISCO-FC-FE-MIB", "cffFcFeElementName"))
)
if mibBuilder.loadTexts:
    dmNewPrincipalSwitchNotify.setStatus(
        "current"
    )

dmFabricChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 1, 3, 0, 3)
)
dmFabricChangeNotify.setObjects(
    ("CISCO-VSAN-MIB", "notifyVsanIndex")
)
if mibBuilder.loadTexts:
    dmFabricChangeNotify.setStatus(
        "current"
    )


# Notifications groups

dmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 2, 5)
)
dmNotificationGroup.setObjects(
      *(("CISCO-DM-MIB", "dmDomainIdNotAssignedNotify"),
        ("CISCO-DM-MIB", "dmNewPrincipalSwitchNotify"),
        ("CISCO-DM-MIB", "dmFabricChangeNotify"))
)
if mibBuilder.loadTexts:
    dmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dmMIBCompliance.setStatus(
        "deprecated"
    )

dmMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 1, 2)
)
if mibBuilder.loadTexts:
    dmMIBCompliance1.setStatus(
        "deprecated"
    )

dmMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 302, 2, 1, 3)
)
if mibBuilder.loadTexts:
    dmMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DM-MIB",
    **{"DomainPriority": DomainPriority,
       "DomainPriorityOrZero": DomainPriorityOrZero,
       "DomainInterfaceRole": DomainInterfaceRole,
       "DmState": DmState,
       "ciscoDmMIB": ciscoDmMIB,
       "ciscoDmMIBObjects": ciscoDmMIBObjects,
       "dmConfiguration": dmConfiguration,
       "dmTable": dmTable,
       "dmEntry": dmEntry,
       "dmConfigDomainId": dmConfigDomainId,
       "dmConfigDomainIdType": dmConfigDomainIdType,
       "dmEnable": dmEnable,
       "dmAutoReconfigure": dmAutoReconfigure,
       "dmContiguousAllocation": dmContiguousAllocation,
       "dmPriority": dmPriority,
       "dmRestart": dmRestart,
       "dmFabricName": dmFabricName,
       "dmPrincipalSwitchWwn": dmPrincipalSwitchWwn,
       "dmLocalSwitchWwn": dmLocalSwitchWwn,
       "dmAssignedAreaIdList": dmAssignedAreaIdList,
       "dmFcIdsGranted": dmFcIdsGranted,
       "dmFcIdsRecovered": dmFcIdsRecovered,
       "dmFreeFcIds": dmFreeFcIds,
       "dmAssignedFcIds": dmAssignedFcIds,
       "dmReservedFcIds": dmReservedFcIds,
       "dmRunningPriority": dmRunningPriority,
       "dmPrincSwRunningPriority": dmPrincSwRunningPriority,
       "dmState": dmState,
       "dmPrincipalSwitchSelections": dmPrincipalSwitchSelections,
       "dmBuildFabrics": dmBuildFabrics,
       "dmFabricReconfigures": dmFabricReconfigures,
       "dmDomainId": dmDomainId,
       "dmLocalPrincipalSwitchSelctns": dmLocalPrincipalSwitchSelctns,
       "dmFcIdPersistency": dmFcIdPersistency,
       "dmFcIdPurge": dmFcIdPurge,
       "dmIfTable": dmIfTable,
       "dmIfEntry": dmIfEntry,
       "dmIfRcfReject": dmIfRcfReject,
       "dmIfRole": dmIfRole,
       "dmIfRowStatus": dmIfRowStatus,
       "dmReConfFabricChangeNotifyEnable": dmReConfFabricChangeNotifyEnable,
       "dmFcIdPersistencyTable": dmFcIdPersistencyTable,
       "dmFcIdPersistencyEntry": dmFcIdPersistencyEntry,
       "dmFcIdPersistencyWwn": dmFcIdPersistencyWwn,
       "dmFcIdPersistencyFcId": dmFcIdPersistencyFcId,
       "dmFcIdPersistencyNum": dmFcIdPersistencyNum,
       "dmFcIdPersistencyUsed": dmFcIdPersistencyUsed,
       "dmFcIdPersistencyType": dmFcIdPersistencyType,
       "dmFcIdPersistencyRowStatus": dmFcIdPersistencyRowStatus,
       "dmAllowedDomainIDListTable": dmAllowedDomainIDListTable,
       "dmAllowedDomainIDListEntry": dmAllowedDomainIDListEntry,
       "dmAllowedDomainIDListId": dmAllowedDomainIDListId,
       "dmAllowedDomainIDList": dmAllowedDomainIDList,
       "dmAllowedDomainIDListUser": dmAllowedDomainIDListUser,
       "dmInfo": dmInfo,
       "dmAreaTable": dmAreaTable,
       "dmAreaEntry": dmAreaEntry,
       "dmAreaAreaId": dmAreaAreaId,
       "dmAreaAssignedPortIdList": dmAreaAssignedPortIdList,
       "dmDatabaseTable": dmDatabaseTable,
       "dmDatabaseEntry": dmDatabaseEntry,
       "dmDatabaseDomainId": dmDatabaseDomainId,
       "dmDatabaseSwitchWwn": dmDatabaseSwitchWwn,
       "dmMaxFcIdCacheSize": dmMaxFcIdCacheSize,
       "dmFcIdCacheTable": dmFcIdCacheTable,
       "dmFcIdCacheEntry": dmFcIdCacheEntry,
       "dmFcIdCacheWwn": dmFcIdCacheWwn,
       "dmFcIdCacheAreaIdPortId": dmFcIdCacheAreaIdPortId,
       "dmFcIdCachePortIds": dmFcIdCachePortIds,
       "dmNotificationPrefix": dmNotificationPrefix,
       "dmNotification": dmNotification,
       "dmDomainIdNotAssignedNotify": dmDomainIdNotAssignedNotify,
       "dmNewPrincipalSwitchNotify": dmNewPrincipalSwitchNotify,
       "dmFabricChangeNotify": dmFabricChangeNotify,
       "dmMIBConformance": dmMIBConformance,
       "dmMIBCompliances": dmMIBCompliances,
       "dmMIBCompliance": dmMIBCompliance,
       "dmMIBCompliance1": dmMIBCompliance1,
       "dmMIBCompliance2": dmMIBCompliance2,
       "dmMIBGroups": dmMIBGroups,
       "dmGroup": dmGroup,
       "dmDatabaseGroup": dmDatabaseGroup,
       "dmAreaGroup": dmAreaGroup,
       "dmCacheGroup": dmCacheGroup,
       "dmNotificationGroup": dmNotificationGroup,
       "dmGroupRev1": dmGroupRev1,
       "dmFcIdPersistencyGroup": dmFcIdPersistencyGroup,
       "dmDomainIDAllowedGroup": dmDomainIDAllowedGroup}
)

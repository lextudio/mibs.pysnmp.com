# SNMP MIB module (T11-FC-FABRIC-ADDR-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-FABRIC-ADDR-MGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:21 2024
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

(FcDomainIdOrZero,
 FcNameIdOrZero,
 fcmInstanceIndex,
 fcmSwitchIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcDomainIdOrZero",
    "FcNameIdOrZero",
    "fcmInstanceIndex",
    "fcmSwitchIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11FcFabricAddrMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 137)
)
t11FcFabricAddrMgrMIB.setRevisions(
        ("2006-03-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class T11FamDomainPriority(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class T11FamDomainInterfaceRole(Integer32, TextualConvention):
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



class T11FamState(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("buildFabricPhase", 6),
          ("disabled", 11),
          ("domainIdDistribution", 5),
          ("noDomains", 10),
          ("other", 1),
          ("principalSwitchSelection", 4),
          ("reconfigureFabricPhase", 7),
          ("stable", 8),
          ("stableWithNoEports", 9),
          ("starting", 2),
          ("unconfigured", 3),
          ("unknown", 12))
    )



# MIB Managed Objects in the order of their OIDs

_T11FamNotifications_ObjectIdentity = ObjectIdentity
t11FamNotifications = _T11FamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 137, 0)
)
_T11FamMIBObjects_ObjectIdentity = ObjectIdentity
t11FamMIBObjects = _T11FamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 137, 1)
)
_T11FamConfiguration_ObjectIdentity = ObjectIdentity
t11FamConfiguration = _T11FamConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 137, 1, 1)
)
_T11FamTable_Object = MibTable
t11FamTable = _T11FamTable_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11FamTable.setStatus("current")
_T11FamEntry_Object = MibTableRow
t11FamEntry = _T11FamEntry_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1)
)
t11FamEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FamEntry.setStatus("current")
_T11FamFabricIndex_Type = T11FabricIndex
_T11FamFabricIndex_Object = MibTableColumn
t11FamFabricIndex = _T11FamFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 1),
    _T11FamFabricIndex_Type()
)
t11FamFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FamFabricIndex.setStatus("current")


class _T11FamConfigDomainId_Type(FcDomainIdOrZero):
    """Custom type t11FamConfigDomainId based on FcDomainIdOrZero"""
    defaultValue = 0


_T11FamConfigDomainId_Object = MibTableColumn
t11FamConfigDomainId = _T11FamConfigDomainId_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 2),
    _T11FamConfigDomainId_Type()
)
t11FamConfigDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FamConfigDomainId.setStatus("current")


class _T11FamConfigDomainIdType_Type(Integer32):
    """Custom type t11FamConfigDomainIdType based on Integer32"""
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
        *(("insistent", 2),
          ("preferred", 1),
          ("static", 3))
    )


_T11FamConfigDomainIdType_Type.__name__ = "Integer32"
_T11FamConfigDomainIdType_Object = MibTableColumn
t11FamConfigDomainIdType = _T11FamConfigDomainIdType_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 3),
    _T11FamConfigDomainIdType_Type()
)
t11FamConfigDomainIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FamConfigDomainIdType.setStatus("current")


class _T11FamAutoReconfigure_Type(TruthValue):
    """Custom type t11FamAutoReconfigure based on TruthValue"""


_T11FamAutoReconfigure_Object = MibTableColumn
t11FamAutoReconfigure = _T11FamAutoReconfigure_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 4),
    _T11FamAutoReconfigure_Type()
)
t11FamAutoReconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FamAutoReconfigure.setStatus("current")
_T11FamContiguousAllocation_Type = TruthValue
_T11FamContiguousAllocation_Object = MibTableColumn
t11FamContiguousAllocation = _T11FamContiguousAllocation_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 5),
    _T11FamContiguousAllocation_Type()
)
t11FamContiguousAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FamContiguousAllocation.setStatus("current")
_T11FamPriority_Type = T11FamDomainPriority
_T11FamPriority_Object = MibTableColumn
t11FamPriority = _T11FamPriority_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 6),
    _T11FamPriority_Type()
)
t11FamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FamPriority.setStatus("current")


class _T11FamPrincipalSwitchWwn_Type(FcNameIdOrZero):
    """Custom type t11FamPrincipalSwitchWwn based on FcNameIdOrZero"""
    defaultHexValue = ""


_T11FamPrincipalSwitchWwn_Object = MibTableColumn
t11FamPrincipalSwitchWwn = _T11FamPrincipalSwitchWwn_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 7),
    _T11FamPrincipalSwitchWwn_Type()
)
t11FamPrincipalSwitchWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamPrincipalSwitchWwn.setStatus("current")
_T11FamLocalSwitchWwn_Type = FcNameIdOrZero
_T11FamLocalSwitchWwn_Object = MibTableColumn
t11FamLocalSwitchWwn = _T11FamLocalSwitchWwn_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 8),
    _T11FamLocalSwitchWwn_Type()
)
t11FamLocalSwitchWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamLocalSwitchWwn.setStatus("current")


class _T11FamAssignedAreaIdList_Type(OctetString):
    """Custom type t11FamAssignedAreaIdList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_T11FamAssignedAreaIdList_Type.__name__ = "OctetString"
_T11FamAssignedAreaIdList_Object = MibTableColumn
t11FamAssignedAreaIdList = _T11FamAssignedAreaIdList_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 9),
    _T11FamAssignedAreaIdList_Type()
)
t11FamAssignedAreaIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamAssignedAreaIdList.setStatus("current")
_T11FamGrantedFcIds_Type = Counter32
_T11FamGrantedFcIds_Object = MibTableColumn
t11FamGrantedFcIds = _T11FamGrantedFcIds_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 10),
    _T11FamGrantedFcIds_Type()
)
t11FamGrantedFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamGrantedFcIds.setStatus("current")
_T11FamRecoveredFcIds_Type = Counter32
_T11FamRecoveredFcIds_Object = MibTableColumn
t11FamRecoveredFcIds = _T11FamRecoveredFcIds_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 11),
    _T11FamRecoveredFcIds_Type()
)
t11FamRecoveredFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamRecoveredFcIds.setStatus("current")
_T11FamFreeFcIds_Type = Gauge32
_T11FamFreeFcIds_Object = MibTableColumn
t11FamFreeFcIds = _T11FamFreeFcIds_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 12),
    _T11FamFreeFcIds_Type()
)
t11FamFreeFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamFreeFcIds.setStatus("current")
_T11FamAssignedFcIds_Type = Gauge32
_T11FamAssignedFcIds_Object = MibTableColumn
t11FamAssignedFcIds = _T11FamAssignedFcIds_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 13),
    _T11FamAssignedFcIds_Type()
)
t11FamAssignedFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamAssignedFcIds.setStatus("current")
_T11FamAvailableFcIds_Type = Gauge32
_T11FamAvailableFcIds_Object = MibTableColumn
t11FamAvailableFcIds = _T11FamAvailableFcIds_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 14),
    _T11FamAvailableFcIds_Type()
)
t11FamAvailableFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamAvailableFcIds.setStatus("current")
_T11FamRunningPriority_Type = T11FamDomainPriority
_T11FamRunningPriority_Object = MibTableColumn
t11FamRunningPriority = _T11FamRunningPriority_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 15),
    _T11FamRunningPriority_Type()
)
t11FamRunningPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamRunningPriority.setStatus("current")
_T11FamPrincSwRunningPriority_Type = T11FamDomainPriority
_T11FamPrincSwRunningPriority_Object = MibTableColumn
t11FamPrincSwRunningPriority = _T11FamPrincSwRunningPriority_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 16),
    _T11FamPrincSwRunningPriority_Type()
)
t11FamPrincSwRunningPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamPrincSwRunningPriority.setStatus("current")
_T11FamState_Type = T11FamState
_T11FamState_Object = MibTableColumn
t11FamState = _T11FamState_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 17),
    _T11FamState_Type()
)
t11FamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamState.setStatus("current")
_T11FamLocalPrincipalSwitchSlctns_Type = Counter32
_T11FamLocalPrincipalSwitchSlctns_Object = MibTableColumn
t11FamLocalPrincipalSwitchSlctns = _T11FamLocalPrincipalSwitchSlctns_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 18),
    _T11FamLocalPrincipalSwitchSlctns_Type()
)
t11FamLocalPrincipalSwitchSlctns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamLocalPrincipalSwitchSlctns.setStatus("current")
_T11FamPrincipalSwitchSelections_Type = Counter32
_T11FamPrincipalSwitchSelections_Object = MibTableColumn
t11FamPrincipalSwitchSelections = _T11FamPrincipalSwitchSelections_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 19),
    _T11FamPrincipalSwitchSelections_Type()
)
t11FamPrincipalSwitchSelections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamPrincipalSwitchSelections.setStatus("current")
_T11FamBuildFabrics_Type = Counter32
_T11FamBuildFabrics_Object = MibTableColumn
t11FamBuildFabrics = _T11FamBuildFabrics_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 20),
    _T11FamBuildFabrics_Type()
)
t11FamBuildFabrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamBuildFabrics.setStatus("current")
_T11FamFabricReconfigures_Type = Counter32
_T11FamFabricReconfigures_Object = MibTableColumn
t11FamFabricReconfigures = _T11FamFabricReconfigures_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 21),
    _T11FamFabricReconfigures_Type()
)
t11FamFabricReconfigures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamFabricReconfigures.setStatus("current")
_T11FamDomainId_Type = FcDomainIdOrZero
_T11FamDomainId_Object = MibTableColumn
t11FamDomainId = _T11FamDomainId_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 22),
    _T11FamDomainId_Type()
)
t11FamDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamDomainId.setStatus("current")
_T11FamSticky_Type = TruthValue
_T11FamSticky_Object = MibTableColumn
t11FamSticky = _T11FamSticky_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 23),
    _T11FamSticky_Type()
)
t11FamSticky.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamSticky.setStatus("current")


class _T11FamRestart_Type(Integer32):
    """Custom type t11FamRestart based on Integer32"""
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


_T11FamRestart_Type.__name__ = "Integer32"
_T11FamRestart_Object = MibTableColumn
t11FamRestart = _T11FamRestart_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 24),
    _T11FamRestart_Type()
)
t11FamRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FamRestart.setStatus("current")


class _T11FamRcFabricNotifyEnable_Type(TruthValue):
    """Custom type t11FamRcFabricNotifyEnable based on TruthValue"""


_T11FamRcFabricNotifyEnable_Object = MibTableColumn
t11FamRcFabricNotifyEnable = _T11FamRcFabricNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 25),
    _T11FamRcFabricNotifyEnable_Type()
)
t11FamRcFabricNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FamRcFabricNotifyEnable.setStatus("current")


class _T11FamEnable_Type(TruthValue):
    """Custom type t11FamEnable based on TruthValue"""


_T11FamEnable_Object = MibTableColumn
t11FamEnable = _T11FamEnable_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 26),
    _T11FamEnable_Type()
)
t11FamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FamEnable.setStatus("current")
_T11FamFabricName_Type = FcNameIdOrZero
_T11FamFabricName_Object = MibTableColumn
t11FamFabricName = _T11FamFabricName_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 27),
    _T11FamFabricName_Type()
)
t11FamFabricName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FamFabricName.setStatus("current")
_T11FamIfTable_Object = MibTable
t11FamIfTable = _T11FamIfTable_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 2)
)
if mibBuilder.loadTexts:
    t11FamIfTable.setStatus("current")
_T11FamIfEntry_Object = MibTableRow
t11FamIfEntry = _T11FamIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1)
)
t11FamIfEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    t11FamIfEntry.setStatus("current")


class _T11FamIfRcfReject_Type(TruthValue):
    """Custom type t11FamIfRcfReject based on TruthValue"""


_T11FamIfRcfReject_Object = MibTableColumn
t11FamIfRcfReject = _T11FamIfRcfReject_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1, 1),
    _T11FamIfRcfReject_Type()
)
t11FamIfRcfReject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FamIfRcfReject.setStatus("current")
_T11FamIfRole_Type = T11FamDomainInterfaceRole
_T11FamIfRole_Object = MibTableColumn
t11FamIfRole = _T11FamIfRole_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1, 2),
    _T11FamIfRole_Type()
)
t11FamIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamIfRole.setStatus("current")
_T11FamIfRowStatus_Type = RowStatus
_T11FamIfRowStatus_Object = MibTableColumn
t11FamIfRowStatus = _T11FamIfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1, 3),
    _T11FamIfRowStatus_Type()
)
t11FamIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FamIfRowStatus.setStatus("current")
_T11FamInfo_ObjectIdentity = ObjectIdentity
t11FamInfo = _T11FamInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 137, 1, 2)
)
_T11FamAreaTable_Object = MibTable
t11FamAreaTable = _T11FamAreaTable_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11FamAreaTable.setStatus("current")
_T11FamAreaEntry_Object = MibTableRow
t11FamAreaEntry = _T11FamAreaEntry_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 1, 1)
)
t11FamAreaEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricIndex"),
    (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAreaAreaId"),
)
if mibBuilder.loadTexts:
    t11FamAreaEntry.setStatus("current")


class _T11FamAreaAreaId_Type(Unsigned32):
    """Custom type t11FamAreaAreaId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_T11FamAreaAreaId_Type.__name__ = "Unsigned32"
_T11FamAreaAreaId_Object = MibTableColumn
t11FamAreaAreaId = _T11FamAreaAreaId_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 1, 1, 1),
    _T11FamAreaAreaId_Type()
)
t11FamAreaAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FamAreaAreaId.setStatus("current")


class _T11FamAreaAssignedPortIdList_Type(OctetString):
    """Custom type t11FamAreaAssignedPortIdList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_T11FamAreaAssignedPortIdList_Type.__name__ = "OctetString"
_T11FamAreaAssignedPortIdList_Object = MibTableColumn
t11FamAreaAssignedPortIdList = _T11FamAreaAssignedPortIdList_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 1, 1, 2),
    _T11FamAreaAssignedPortIdList_Type()
)
t11FamAreaAssignedPortIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamAreaAssignedPortIdList.setStatus("current")
_T11FamDatabaseTable_Object = MibTable
t11FamDatabaseTable = _T11FamDatabaseTable_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 2)
)
if mibBuilder.loadTexts:
    t11FamDatabaseTable.setStatus("current")
_T11FamDatabaseEntry_Object = MibTableRow
t11FamDatabaseEntry = _T11FamDatabaseEntry_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 2, 1)
)
t11FamDatabaseEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricIndex"),
    (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamDatabaseDomainId"),
)
if mibBuilder.loadTexts:
    t11FamDatabaseEntry.setStatus("current")


class _T11FamDatabaseDomainId_Type(FcDomainIdOrZero):
    """Custom type t11FamDatabaseDomainId based on FcDomainIdOrZero"""
    subtypeSpec = FcDomainIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 239),
    )


_T11FamDatabaseDomainId_Type.__name__ = "FcDomainIdOrZero"
_T11FamDatabaseDomainId_Object = MibTableColumn
t11FamDatabaseDomainId = _T11FamDatabaseDomainId_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 2, 1, 1),
    _T11FamDatabaseDomainId_Type()
)
t11FamDatabaseDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FamDatabaseDomainId.setStatus("current")
_T11FamDatabaseSwitchWwn_Type = FcNameIdOrZero
_T11FamDatabaseSwitchWwn_Object = MibTableColumn
t11FamDatabaseSwitchWwn = _T11FamDatabaseSwitchWwn_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 2, 1, 2),
    _T11FamDatabaseSwitchWwn_Type()
)
t11FamDatabaseSwitchWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamDatabaseSwitchWwn.setStatus("current")


class _T11FamMaxFcIdCacheSize_Type(Unsigned32):
    """Custom type t11FamMaxFcIdCacheSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_T11FamMaxFcIdCacheSize_Type.__name__ = "Unsigned32"
_T11FamMaxFcIdCacheSize_Object = MibScalar
t11FamMaxFcIdCacheSize = _T11FamMaxFcIdCacheSize_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 3),
    _T11FamMaxFcIdCacheSize_Type()
)
t11FamMaxFcIdCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamMaxFcIdCacheSize.setStatus("current")
_T11FamFcIdCacheTable_Object = MibTable
t11FamFcIdCacheTable = _T11FamFcIdCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 4)
)
if mibBuilder.loadTexts:
    t11FamFcIdCacheTable.setStatus("current")
_T11FamFcIdCacheEntry_Object = MibTableRow
t11FamFcIdCacheEntry = _T11FamFcIdCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1)
)
t11FamFcIdCacheEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricIndex"),
    (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFcIdCacheWwn"),
)
if mibBuilder.loadTexts:
    t11FamFcIdCacheEntry.setStatus("current")
_T11FamFcIdCacheWwn_Type = FcNameIdOrZero
_T11FamFcIdCacheWwn_Object = MibTableColumn
t11FamFcIdCacheWwn = _T11FamFcIdCacheWwn_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1, 1),
    _T11FamFcIdCacheWwn_Type()
)
t11FamFcIdCacheWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FamFcIdCacheWwn.setStatus("current")


class _T11FamFcIdCacheAreaIdPortId_Type(OctetString):
    """Custom type t11FamFcIdCacheAreaIdPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_T11FamFcIdCacheAreaIdPortId_Type.__name__ = "OctetString"
_T11FamFcIdCacheAreaIdPortId_Object = MibTableColumn
t11FamFcIdCacheAreaIdPortId = _T11FamFcIdCacheAreaIdPortId_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1, 2),
    _T11FamFcIdCacheAreaIdPortId_Type()
)
t11FamFcIdCacheAreaIdPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamFcIdCacheAreaIdPortId.setStatus("current")


class _T11FamFcIdCachePortIds_Type(Unsigned32):
    """Custom type t11FamFcIdCachePortIds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_T11FamFcIdCachePortIds_Type.__name__ = "Unsigned32"
_T11FamFcIdCachePortIds_Object = MibTableColumn
t11FamFcIdCachePortIds = _T11FamFcIdCachePortIds_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1, 3),
    _T11FamFcIdCachePortIds_Type()
)
t11FamFcIdCachePortIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FamFcIdCachePortIds.setStatus("current")
_T11FamNotifyControl_ObjectIdentity = ObjectIdentity
t11FamNotifyControl = _T11FamNotifyControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 137, 1, 3)
)
_T11FamNotifyFabricIndex_Type = T11FabricIndex
_T11FamNotifyFabricIndex_Object = MibScalar
t11FamNotifyFabricIndex = _T11FamNotifyFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 137, 1, 3, 1),
    _T11FamNotifyFabricIndex_Type()
)
t11FamNotifyFabricIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    t11FamNotifyFabricIndex.setStatus("current")
_T11FamMIBConformance_ObjectIdentity = ObjectIdentity
t11FamMIBConformance = _T11FamMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 137, 2)
)
_T11FamMIBCompliances_ObjectIdentity = ObjectIdentity
t11FamMIBCompliances = _T11FamMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 137, 2, 1)
)
_T11FamMIBGroups_ObjectIdentity = ObjectIdentity
t11FamMIBGroups = _T11FamMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 137, 2, 2)
)

# Managed Objects groups

t11FamGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 137, 2, 2, 1)
)
t11FamGroup.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamConfigDomainId"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamConfigDomainIdType"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAutoReconfigure"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamContiguousAllocation"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamPriority"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamPrincipalSwitchWwn"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAssignedAreaIdList"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamGrantedFcIds"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamRecoveredFcIds"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFreeFcIds"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAssignedFcIds"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAvailableFcIds"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamRunningPriority"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamPrincSwRunningPriority"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamState"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalPrincipalSwitchSlctns"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamPrincipalSwitchSelections"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamBuildFabrics"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricReconfigures"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamDomainId"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamSticky"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamRestart"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamRcFabricNotifyEnable"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamEnable"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricName"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamIfRcfReject"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamIfRole"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamIfRowStatus"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamNotifyFabricIndex"))
)
if mibBuilder.loadTexts:
    t11FamGroup.setStatus("current")

t11FamCommandGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 137, 2, 2, 2)
)
t11FamCommandGroup.setObjects(
    ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamRestart")
)
if mibBuilder.loadTexts:
    t11FamCommandGroup.setStatus("current")

t11FamDatabaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 137, 2, 2, 3)
)
t11FamDatabaseGroup.setObjects(
    ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamDatabaseSwitchWwn")
)
if mibBuilder.loadTexts:
    t11FamDatabaseGroup.setStatus("current")

t11FamAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 137, 2, 2, 4)
)
t11FamAreaGroup.setObjects(
    ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAreaAssignedPortIdList")
)
if mibBuilder.loadTexts:
    t11FamAreaGroup.setStatus("current")

t11FamCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 137, 2, 2, 5)
)
t11FamCacheGroup.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamMaxFcIdCacheSize"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFcIdCacheAreaIdPortId"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFcIdCachePortIds"))
)
if mibBuilder.loadTexts:
    t11FamCacheGroup.setStatus("current")


# Notification objects

t11FamDomainIdNotAssignedNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 137, 0, 1)
)
t11FamDomainIdNotAssignedNotify.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamNotifyFabricIndex"))
)
if mibBuilder.loadTexts:
    t11FamDomainIdNotAssignedNotify.setStatus(
        "current"
    )

t11FamNewPrincipalSwitchNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 137, 0, 2)
)
t11FamNewPrincipalSwitchNotify.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamNotifyFabricIndex"))
)
if mibBuilder.loadTexts:
    t11FamNewPrincipalSwitchNotify.setStatus(
        "current"
    )

t11FamFabricChangeNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 137, 0, 3)
)
t11FamFabricChangeNotify.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamNotifyFabricIndex"))
)
if mibBuilder.loadTexts:
    t11FamFabricChangeNotify.setStatus(
        "current"
    )


# Notifications groups

t11FamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 137, 2, 2, 6)
)
t11FamNotificationGroup.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamDomainIdNotAssignedNotify"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamNewPrincipalSwitchNotify"),
        ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricChangeNotify"))
)
if mibBuilder.loadTexts:
    t11FamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

t11FamMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 137, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11FamMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-FABRIC-ADDR-MGR-MIB",
    **{"T11FamDomainPriority": T11FamDomainPriority,
       "T11FamDomainInterfaceRole": T11FamDomainInterfaceRole,
       "T11FamState": T11FamState,
       "t11FcFabricAddrMgrMIB": t11FcFabricAddrMgrMIB,
       "t11FamNotifications": t11FamNotifications,
       "t11FamDomainIdNotAssignedNotify": t11FamDomainIdNotAssignedNotify,
       "t11FamNewPrincipalSwitchNotify": t11FamNewPrincipalSwitchNotify,
       "t11FamFabricChangeNotify": t11FamFabricChangeNotify,
       "t11FamMIBObjects": t11FamMIBObjects,
       "t11FamConfiguration": t11FamConfiguration,
       "t11FamTable": t11FamTable,
       "t11FamEntry": t11FamEntry,
       "t11FamFabricIndex": t11FamFabricIndex,
       "t11FamConfigDomainId": t11FamConfigDomainId,
       "t11FamConfigDomainIdType": t11FamConfigDomainIdType,
       "t11FamAutoReconfigure": t11FamAutoReconfigure,
       "t11FamContiguousAllocation": t11FamContiguousAllocation,
       "t11FamPriority": t11FamPriority,
       "t11FamPrincipalSwitchWwn": t11FamPrincipalSwitchWwn,
       "t11FamLocalSwitchWwn": t11FamLocalSwitchWwn,
       "t11FamAssignedAreaIdList": t11FamAssignedAreaIdList,
       "t11FamGrantedFcIds": t11FamGrantedFcIds,
       "t11FamRecoveredFcIds": t11FamRecoveredFcIds,
       "t11FamFreeFcIds": t11FamFreeFcIds,
       "t11FamAssignedFcIds": t11FamAssignedFcIds,
       "t11FamAvailableFcIds": t11FamAvailableFcIds,
       "t11FamRunningPriority": t11FamRunningPriority,
       "t11FamPrincSwRunningPriority": t11FamPrincSwRunningPriority,
       "t11FamState": t11FamState,
       "t11FamLocalPrincipalSwitchSlctns": t11FamLocalPrincipalSwitchSlctns,
       "t11FamPrincipalSwitchSelections": t11FamPrincipalSwitchSelections,
       "t11FamBuildFabrics": t11FamBuildFabrics,
       "t11FamFabricReconfigures": t11FamFabricReconfigures,
       "t11FamDomainId": t11FamDomainId,
       "t11FamSticky": t11FamSticky,
       "t11FamRestart": t11FamRestart,
       "t11FamRcFabricNotifyEnable": t11FamRcFabricNotifyEnable,
       "t11FamEnable": t11FamEnable,
       "t11FamFabricName": t11FamFabricName,
       "t11FamIfTable": t11FamIfTable,
       "t11FamIfEntry": t11FamIfEntry,
       "t11FamIfRcfReject": t11FamIfRcfReject,
       "t11FamIfRole": t11FamIfRole,
       "t11FamIfRowStatus": t11FamIfRowStatus,
       "t11FamInfo": t11FamInfo,
       "t11FamAreaTable": t11FamAreaTable,
       "t11FamAreaEntry": t11FamAreaEntry,
       "t11FamAreaAreaId": t11FamAreaAreaId,
       "t11FamAreaAssignedPortIdList": t11FamAreaAssignedPortIdList,
       "t11FamDatabaseTable": t11FamDatabaseTable,
       "t11FamDatabaseEntry": t11FamDatabaseEntry,
       "t11FamDatabaseDomainId": t11FamDatabaseDomainId,
       "t11FamDatabaseSwitchWwn": t11FamDatabaseSwitchWwn,
       "t11FamMaxFcIdCacheSize": t11FamMaxFcIdCacheSize,
       "t11FamFcIdCacheTable": t11FamFcIdCacheTable,
       "t11FamFcIdCacheEntry": t11FamFcIdCacheEntry,
       "t11FamFcIdCacheWwn": t11FamFcIdCacheWwn,
       "t11FamFcIdCacheAreaIdPortId": t11FamFcIdCacheAreaIdPortId,
       "t11FamFcIdCachePortIds": t11FamFcIdCachePortIds,
       "t11FamNotifyControl": t11FamNotifyControl,
       "t11FamNotifyFabricIndex": t11FamNotifyFabricIndex,
       "t11FamMIBConformance": t11FamMIBConformance,
       "t11FamMIBCompliances": t11FamMIBCompliances,
       "t11FamMIBCompliance": t11FamMIBCompliance,
       "t11FamMIBGroups": t11FamMIBGroups,
       "t11FamGroup": t11FamGroup,
       "t11FamCommandGroup": t11FamCommandGroup,
       "t11FamDatabaseGroup": t11FamDatabaseGroup,
       "t11FamAreaGroup": t11FamAreaGroup,
       "t11FamCacheGroup": t11FamCacheGroup,
       "t11FamNotificationGroup": t11FamNotificationGroup}
)

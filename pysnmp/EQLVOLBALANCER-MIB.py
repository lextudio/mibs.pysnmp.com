# SNMP MIB module (EQLVOLBALANCER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLVOLBALANCER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:14 2024
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

(UTFString,
 eqlGroupId) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "UTFString",
    "eqlGroupId")

(eqlMemberIndex,) = mibBuilder.importSymbols(
    "EQLMEMBER-MIB",
    "eqlMemberIndex")

(eqlRAIDDeviceLUNIndex,
 eqlRAIDDeviceUUID) = mibBuilder.importSymbols(
    "EQLRAID-MIB",
    "eqlRAIDDeviceLUNIndex",
    "eqlRAIDDeviceUUID")

(eqlStoragePoolIndex,) = mibBuilder.importSymbols(
    "EQLSTORAGEPOOL-MIB",
    "eqlStoragePoolIndex")

(eqliscsiLocalMemberId,
 eqliscsiVolumeIndex) = mibBuilder.importSymbols(
    "EQLVOLUME-MIB",
    "eqliscsiLocalMemberId",
    "eqliscsiVolumeIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eqlvolbalancerModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 14)
)
eqlvolbalancerModule.setRevisions(
        ("2004-01-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqlvolbalancerObjects_ObjectIdentity = ObjectIdentity
eqlvolbalancerObjects = _EqlvolbalancerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1)
)
_EqlvolbalancerConfigGroup_ObjectIdentity = ObjectIdentity
eqlvolbalancerConfigGroup = _EqlvolbalancerConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 1)
)


class _EqlvolbalancerConfigVolSliceCostFreq_Type(Unsigned32):
    """Custom type eqlvolbalancerConfigVolSliceCostFreq based on Unsigned32"""
    defaultValue = 15


_EqlvolbalancerConfigVolSliceCostFreq_Object = MibScalar
eqlvolbalancerConfigVolSliceCostFreq = _EqlvolbalancerConfigVolSliceCostFreq_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 1, 1),
    _EqlvolbalancerConfigVolSliceCostFreq_Type()
)
eqlvolbalancerConfigVolSliceCostFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlvolbalancerConfigVolSliceCostFreq.setStatus("deprecated")
if mibBuilder.loadTexts:
    eqlvolbalancerConfigVolSliceCostFreq.setUnits("minutes")


class _EqlvolbalancerConfigVolSliceRollupTime_Type(Unsigned32):
    """Custom type eqlvolbalancerConfigVolSliceRollupTime based on Unsigned32"""
    defaultValue = 60


_EqlvolbalancerConfigVolSliceRollupTime_Object = MibScalar
eqlvolbalancerConfigVolSliceRollupTime = _EqlvolbalancerConfigVolSliceRollupTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 1, 2),
    _EqlvolbalancerConfigVolSliceRollupTime_Type()
)
eqlvolbalancerConfigVolSliceRollupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlvolbalancerConfigVolSliceRollupTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    eqlvolbalancerConfigVolSliceRollupTime.setUnits("minutes")
_EqlvolbalancerVolumeSliceCostTable_Object = MibTable
eqlvolbalancerVolumeSliceCostTable = _EqlvolbalancerVolumeSliceCostTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 2)
)
if mibBuilder.loadTexts:
    eqlvolbalancerVolumeSliceCostTable.setStatus("deprecated")
_EqlvolbalancerVolumeSliceCostEntry_Object = MibTableRow
eqlvolbalancerVolumeSliceCostEntry = _EqlvolbalancerVolumeSliceCostEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 2, 1)
)
eqlvolbalancerVolumeSliceCostEntry.setIndexNames(
    (0, "EQLVOLBALANCER-MIB", "eqlvolbalancerVolumeSliceCostPsaId"),
    (0, "EQLVOLBALANCER-MIB", "eqlvolbalancerVolumeSliceCostTime"),
    (0, "EQLVOLBALANCER-MIB", "eqlvolbalancerVolumeSliceCostVolumeId"),
)
if mibBuilder.loadTexts:
    eqlvolbalancerVolumeSliceCostEntry.setStatus("deprecated")


class _EqlvolbalancerVolumeSliceCostPsaId_Type(OctetString):
    """Custom type eqlvolbalancerVolumeSliceCostPsaId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlvolbalancerVolumeSliceCostPsaId_Type.__name__ = "OctetString"
_EqlvolbalancerVolumeSliceCostPsaId_Object = MibTableColumn
eqlvolbalancerVolumeSliceCostPsaId = _EqlvolbalancerVolumeSliceCostPsaId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 2, 1, 1),
    _EqlvolbalancerVolumeSliceCostPsaId_Type()
)
eqlvolbalancerVolumeSliceCostPsaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlvolbalancerVolumeSliceCostPsaId.setStatus("deprecated")
_EqlvolbalancerVolumeSliceCostTime_Type = Unsigned32
_EqlvolbalancerVolumeSliceCostTime_Object = MibTableColumn
eqlvolbalancerVolumeSliceCostTime = _EqlvolbalancerVolumeSliceCostTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 2, 1, 2),
    _EqlvolbalancerVolumeSliceCostTime_Type()
)
eqlvolbalancerVolumeSliceCostTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlvolbalancerVolumeSliceCostTime.setStatus("deprecated")


class _EqlvolbalancerVolumeSliceCostVolumeId_Type(OctetString):
    """Custom type eqlvolbalancerVolumeSliceCostVolumeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlvolbalancerVolumeSliceCostVolumeId_Type.__name__ = "OctetString"
_EqlvolbalancerVolumeSliceCostVolumeId_Object = MibTableColumn
eqlvolbalancerVolumeSliceCostVolumeId = _EqlvolbalancerVolumeSliceCostVolumeId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 2, 1, 3),
    _EqlvolbalancerVolumeSliceCostVolumeId_Type()
)
eqlvolbalancerVolumeSliceCostVolumeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlvolbalancerVolumeSliceCostVolumeId.setStatus("deprecated")
_EqlvolbalancerVolumeSliceCostCost_Type = Unsigned32
_EqlvolbalancerVolumeSliceCostCost_Object = MibTableColumn
eqlvolbalancerVolumeSliceCostCost = _EqlvolbalancerVolumeSliceCostCost_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 2, 1, 4),
    _EqlvolbalancerVolumeSliceCostCost_Type()
)
eqlvolbalancerVolumeSliceCostCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlvolbalancerVolumeSliceCostCost.setStatus("deprecated")
_EqlvolbalancerVolumeSliceCostStatus_Type = RowStatus
_EqlvolbalancerVolumeSliceCostStatus_Object = MibTableColumn
eqlvolbalancerVolumeSliceCostStatus = _EqlvolbalancerVolumeSliceCostStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 2, 1, 5),
    _EqlvolbalancerVolumeSliceCostStatus_Type()
)
eqlvolbalancerVolumeSliceCostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlvolbalancerVolumeSliceCostStatus.setStatus("deprecated")
_EqlvolbalancerDailyVolumeCostTable_Object = MibTable
eqlvolbalancerDailyVolumeCostTable = _EqlvolbalancerDailyVolumeCostTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 3)
)
if mibBuilder.loadTexts:
    eqlvolbalancerDailyVolumeCostTable.setStatus("deprecated")
_EqlvolbalancerDailyVolumeCostEntry_Object = MibTableRow
eqlvolbalancerDailyVolumeCostEntry = _EqlvolbalancerDailyVolumeCostEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 3, 1)
)
eqlvolbalancerDailyVolumeCostEntry.setIndexNames(
    (0, "EQLVOLBALANCER-MIB", "eqlvolbalancerDailyVolumeCostDay"),
    (0, "EQLVOLBALANCER-MIB", "eqlvolbalancerDailyVolumeCostVolumeId"),
)
if mibBuilder.loadTexts:
    eqlvolbalancerDailyVolumeCostEntry.setStatus("deprecated")
_EqlvolbalancerDailyVolumeCostDay_Type = Unsigned32
_EqlvolbalancerDailyVolumeCostDay_Object = MibTableColumn
eqlvolbalancerDailyVolumeCostDay = _EqlvolbalancerDailyVolumeCostDay_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 3, 1, 1),
    _EqlvolbalancerDailyVolumeCostDay_Type()
)
eqlvolbalancerDailyVolumeCostDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlvolbalancerDailyVolumeCostDay.setStatus("deprecated")


class _EqlvolbalancerDailyVolumeCostVolumeId_Type(OctetString):
    """Custom type eqlvolbalancerDailyVolumeCostVolumeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlvolbalancerDailyVolumeCostVolumeId_Type.__name__ = "OctetString"
_EqlvolbalancerDailyVolumeCostVolumeId_Object = MibTableColumn
eqlvolbalancerDailyVolumeCostVolumeId = _EqlvolbalancerDailyVolumeCostVolumeId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 3, 1, 2),
    _EqlvolbalancerDailyVolumeCostVolumeId_Type()
)
eqlvolbalancerDailyVolumeCostVolumeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlvolbalancerDailyVolumeCostVolumeId.setStatus("deprecated")
_EqlvolbalancerDailyVolumeCostCost_Type = Unsigned32
_EqlvolbalancerDailyVolumeCostCost_Object = MibTableColumn
eqlvolbalancerDailyVolumeCostCost = _EqlvolbalancerDailyVolumeCostCost_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 3, 1, 3),
    _EqlvolbalancerDailyVolumeCostCost_Type()
)
eqlvolbalancerDailyVolumeCostCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlvolbalancerDailyVolumeCostCost.setStatus("deprecated")
_EqlvolbalancerDailyVolumeCostStatus_Type = RowStatus
_EqlvolbalancerDailyVolumeCostStatus_Object = MibTableColumn
eqlvolbalancerDailyVolumeCostStatus = _EqlvolbalancerDailyVolumeCostStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 3, 1, 4),
    _EqlvolbalancerDailyVolumeCostStatus_Type()
)
eqlvolbalancerDailyVolumeCostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlvolbalancerDailyVolumeCostStatus.setStatus("deprecated")
_EqlvolbalancerRecommendationTable_Object = MibTable
eqlvolbalancerRecommendationTable = _EqlvolbalancerRecommendationTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 4)
)
if mibBuilder.loadTexts:
    eqlvolbalancerRecommendationTable.setStatus("deprecated")
_EqlvolbalancerRecommendationEntry_Object = MibTableRow
eqlvolbalancerRecommendationEntry = _EqlvolbalancerRecommendationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 4, 1)
)
eqlvolbalancerRecommendationEntry.setIndexNames(
    (0, "EQLVOLBALANCER-MIB", "eqlvolbalancerRecommendationTime"),
    (0, "EQLVOLBALANCER-MIB", "eqlvolbalancerRecommendationVolumeId"),
    (0, "EQLVOLBALANCER-MIB", "eqlvolbalancerRecommendationSrcPsaId"),
)
if mibBuilder.loadTexts:
    eqlvolbalancerRecommendationEntry.setStatus("deprecated")
_EqlvolbalancerRecommendationTime_Type = Unsigned32
_EqlvolbalancerRecommendationTime_Object = MibTableColumn
eqlvolbalancerRecommendationTime = _EqlvolbalancerRecommendationTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 4, 1, 1),
    _EqlvolbalancerRecommendationTime_Type()
)
eqlvolbalancerRecommendationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlvolbalancerRecommendationTime.setStatus("deprecated")


class _EqlvolbalancerRecommendationVolumeId_Type(OctetString):
    """Custom type eqlvolbalancerRecommendationVolumeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlvolbalancerRecommendationVolumeId_Type.__name__ = "OctetString"
_EqlvolbalancerRecommendationVolumeId_Object = MibTableColumn
eqlvolbalancerRecommendationVolumeId = _EqlvolbalancerRecommendationVolumeId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 4, 1, 2),
    _EqlvolbalancerRecommendationVolumeId_Type()
)
eqlvolbalancerRecommendationVolumeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlvolbalancerRecommendationVolumeId.setStatus("deprecated")


class _EqlvolbalancerRecommendationSrcPsaId_Type(OctetString):
    """Custom type eqlvolbalancerRecommendationSrcPsaId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlvolbalancerRecommendationSrcPsaId_Type.__name__ = "OctetString"
_EqlvolbalancerRecommendationSrcPsaId_Object = MibTableColumn
eqlvolbalancerRecommendationSrcPsaId = _EqlvolbalancerRecommendationSrcPsaId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 4, 1, 3),
    _EqlvolbalancerRecommendationSrcPsaId_Type()
)
eqlvolbalancerRecommendationSrcPsaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlvolbalancerRecommendationSrcPsaId.setStatus("deprecated")


class _EqlvolbalancerRecommendationDstPsaId_Type(OctetString):
    """Custom type eqlvolbalancerRecommendationDstPsaId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlvolbalancerRecommendationDstPsaId_Type.__name__ = "OctetString"
_EqlvolbalancerRecommendationDstPsaId_Object = MibTableColumn
eqlvolbalancerRecommendationDstPsaId = _EqlvolbalancerRecommendationDstPsaId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 4, 1, 4),
    _EqlvolbalancerRecommendationDstPsaId_Type()
)
eqlvolbalancerRecommendationDstPsaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlvolbalancerRecommendationDstPsaId.setStatus("deprecated")
_EqlvolbalancerRecommendationComplete_Type = TruthValue
_EqlvolbalancerRecommendationComplete_Object = MibTableColumn
eqlvolbalancerRecommendationComplete = _EqlvolbalancerRecommendationComplete_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 4, 1, 5),
    _EqlvolbalancerRecommendationComplete_Type()
)
eqlvolbalancerRecommendationComplete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlvolbalancerRecommendationComplete.setStatus("deprecated")
_EqlvolbalancerRecommendationStatus_Type = RowStatus
_EqlvolbalancerRecommendationStatus_Object = MibTableColumn
eqlvolbalancerRecommendationStatus = _EqlvolbalancerRecommendationStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 4, 1, 6),
    _EqlvolbalancerRecommendationStatus_Type()
)
eqlvolbalancerRecommendationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlvolbalancerRecommendationStatus.setStatus("deprecated")
_EqlVolBalConfigTable_Object = MibTable
eqlVolBalConfigTable = _EqlVolBalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5)
)
if mibBuilder.loadTexts:
    eqlVolBalConfigTable.setStatus("current")
_EqlVolBalConfigEntry_Object = MibTableRow
eqlVolBalConfigEntry = _EqlVolBalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1)
)
eqlVolBalConfigEntry.setIndexNames(
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
)
if mibBuilder.loadTexts:
    eqlVolBalConfigEntry.setStatus("current")
_EqlVolBalConfigLastPlanIndex_Type = Counter32
_EqlVolBalConfigLastPlanIndex_Object = MibTableColumn
eqlVolBalConfigLastPlanIndex = _EqlVolBalConfigLastPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 1),
    _EqlVolBalConfigLastPlanIndex_Type()
)
eqlVolBalConfigLastPlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolBalConfigLastPlanIndex.setStatus("current")


class _EqlVolBalConfigEnabled_Type(Integer32):
    """Custom type eqlVolBalConfigEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("capacity-only", 2),
          ("disabled", 3),
          ("enabled", 1),
          ("performance", 4))
    )


_EqlVolBalConfigEnabled_Type.__name__ = "Integer32"
_EqlVolBalConfigEnabled_Object = MibTableColumn
eqlVolBalConfigEnabled = _EqlVolBalConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 2),
    _EqlVolBalConfigEnabled_Type()
)
eqlVolBalConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolBalConfigEnabled.setStatus("current")
_EqlVolBalConfigSenseFrequency_Type = Unsigned32
_EqlVolBalConfigSenseFrequency_Object = MibTableColumn
eqlVolBalConfigSenseFrequency = _EqlVolBalConfigSenseFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 3),
    _EqlVolBalConfigSenseFrequency_Type()
)
eqlVolBalConfigSenseFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigSenseFrequency.setStatus("current")
_EqlVolBalConfigImbalDetectFrequency_Type = Unsigned32
_EqlVolBalConfigImbalDetectFrequency_Object = MibTableColumn
eqlVolBalConfigImbalDetectFrequency = _EqlVolBalConfigImbalDetectFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 4),
    _EqlVolBalConfigImbalDetectFrequency_Type()
)
eqlVolBalConfigImbalDetectFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigImbalDetectFrequency.setStatus("current")
_EqlVolBalConfigVolumeDelFrequency_Type = Unsigned32
_EqlVolBalConfigVolumeDelFrequency_Object = MibTableColumn
eqlVolBalConfigVolumeDelFrequency = _EqlVolBalConfigVolumeDelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 5),
    _EqlVolBalConfigVolumeDelFrequency_Type()
)
eqlVolBalConfigVolumeDelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigVolumeDelFrequency.setStatus("current")
_EqlVolBalConfigVolumeBindFrequency_Type = Unsigned32
_EqlVolBalConfigVolumeBindFrequency_Object = MibTableColumn
eqlVolBalConfigVolumeBindFrequency = _EqlVolBalConfigVolumeBindFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 6),
    _EqlVolBalConfigVolumeBindFrequency_Type()
)
eqlVolBalConfigVolumeBindFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigVolumeBindFrequency.setStatus("current")
_EqlVolBalConfigRAIDSetFreeSpaceTroubleDelay_Type = Unsigned32
_EqlVolBalConfigRAIDSetFreeSpaceTroubleDelay_Object = MibTableColumn
eqlVolBalConfigRAIDSetFreeSpaceTroubleDelay = _EqlVolBalConfigRAIDSetFreeSpaceTroubleDelay_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 7),
    _EqlVolBalConfigRAIDSetFreeSpaceTroubleDelay_Type()
)
eqlVolBalConfigRAIDSetFreeSpaceTroubleDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigRAIDSetFreeSpaceTroubleDelay.setStatus("current")
_EqlVolBalConfigRAIDSetDeleteDelay_Type = Unsigned32
_EqlVolBalConfigRAIDSetDeleteDelay_Object = MibTableColumn
eqlVolBalConfigRAIDSetDeleteDelay = _EqlVolBalConfigRAIDSetDeleteDelay_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 8),
    _EqlVolBalConfigRAIDSetDeleteDelay_Type()
)
eqlVolBalConfigRAIDSetDeleteDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigRAIDSetDeleteDelay.setStatus("current")
_EqlVolBalConfigRAIDSetJoinDelay_Type = Unsigned32
_EqlVolBalConfigRAIDSetJoinDelay_Object = MibTableColumn
eqlVolBalConfigRAIDSetJoinDelay = _EqlVolBalConfigRAIDSetJoinDelay_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 9),
    _EqlVolBalConfigRAIDSetJoinDelay_Type()
)
eqlVolBalConfigRAIDSetJoinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigRAIDSetJoinDelay.setStatus("current")
_EqlVolBalConfigReamSize_Type = Unsigned32
_EqlVolBalConfigReamSize_Object = MibTableColumn
eqlVolBalConfigReamSize = _EqlVolBalConfigReamSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 10),
    _EqlVolBalConfigReamSize_Type()
)
eqlVolBalConfigReamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigReamSize.setStatus("current")
_EqlVolBalConfigHistoryRowMax_Type = Unsigned32
_EqlVolBalConfigHistoryRowMax_Object = MibTableColumn
eqlVolBalConfigHistoryRowMax = _EqlVolBalConfigHistoryRowMax_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 11),
    _EqlVolBalConfigHistoryRowMax_Type()
)
eqlVolBalConfigHistoryRowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigHistoryRowMax.setStatus("current")
_EqlVolBalConfigRAIDStatsRowMax_Type = Unsigned32
_EqlVolBalConfigRAIDStatsRowMax_Object = MibTableColumn
eqlVolBalConfigRAIDStatsRowMax = _EqlVolBalConfigRAIDStatsRowMax_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 12),
    _EqlVolBalConfigRAIDStatsRowMax_Type()
)
eqlVolBalConfigRAIDStatsRowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigRAIDStatsRowMax.setStatus("current")
_EqlVolBalConfigPoolThroughputRateMax_Type = Unsigned32
_EqlVolBalConfigPoolThroughputRateMax_Object = MibTableColumn
eqlVolBalConfigPoolThroughputRateMax = _EqlVolBalConfigPoolThroughputRateMax_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 13),
    _EqlVolBalConfigPoolThroughputRateMax_Type()
)
eqlVolBalConfigPoolThroughputRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigPoolThroughputRateMax.setStatus("current")


class _EqlVolBalConfigMinSpreadSize_Type(Unsigned32):
    """Custom type eqlVolBalConfigMinSpreadSize based on Unsigned32"""
    defaultValue = 1024


_EqlVolBalConfigMinSpreadSize_Object = MibTableColumn
eqlVolBalConfigMinSpreadSize = _EqlVolBalConfigMinSpreadSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 14),
    _EqlVolBalConfigMinSpreadSize_Type()
)
eqlVolBalConfigMinSpreadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigMinSpreadSize.setStatus("current")


class _EqlVolBalConfigPlacementThreshold_Type(Unsigned32):
    """Custom type eqlVolBalConfigPlacementThreshold based on Unsigned32"""
    defaultValue = 200


_EqlVolBalConfigPlacementThreshold_Object = MibTableColumn
eqlVolBalConfigPlacementThreshold = _EqlVolBalConfigPlacementThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 15),
    _EqlVolBalConfigPlacementThreshold_Type()
)
eqlVolBalConfigPlacementThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigPlacementThreshold.setStatus("current")


class _EqlVolBalConfigPreviousLeadUUID_Type(OctetString):
    """Custom type eqlVolBalConfigPreviousLeadUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalConfigPreviousLeadUUID_Type.__name__ = "OctetString"
_EqlVolBalConfigPreviousLeadUUID_Object = MibTableColumn
eqlVolBalConfigPreviousLeadUUID = _EqlVolBalConfigPreviousLeadUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 16),
    _EqlVolBalConfigPreviousLeadUUID_Type()
)
eqlVolBalConfigPreviousLeadUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigPreviousLeadUUID.setStatus("current")


class _EqlVolBalConfigFlags_Type(Bits):
    """Custom type eqlVolBalConfigFlags based on Bits"""
    namedValues = NamedValues(
        *(("enableRoutingTableChecker", 0),
          ("flag10", 10),
          ("flag11", 11),
          ("flag12", 12),
          ("flag13", 13),
          ("flag14", 14),
          ("flag15", 15),
          ("flag16", 16),
          ("flag17", 17),
          ("flag18", 18),
          ("flag19", 19),
          ("flag20", 20),
          ("flag21", 21),
          ("flag22", 22),
          ("flag23", 23),
          ("flag24", 24),
          ("flag25", 25),
          ("flag26", 26),
          ("flag27", 27),
          ("flag28", 28),
          ("flag29", 29),
          ("flag3", 3),
          ("flag30", 30),
          ("flag31", 31),
          ("flag4", 4),
          ("flag5", 5),
          ("flag6", 6),
          ("flag7", 7),
          ("flag8", 8),
          ("flag9", 9),
          ("routingTableCheckerCheckAllPages", 1),
          ("routingTableCheckerHaltGroup", 2))
    )

_EqlVolBalConfigFlags_Type.__name__ = "Bits"
_EqlVolBalConfigFlags_Object = MibTableColumn
eqlVolBalConfigFlags = _EqlVolBalConfigFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 17),
    _EqlVolBalConfigFlags_Type()
)
eqlVolBalConfigFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalConfigFlags.setStatus("current")


class _EqlVolBalConfigArchivalPlacementThreshold_Type(Unsigned32):
    """Custom type eqlVolBalConfigArchivalPlacementThreshold based on Unsigned32"""
    defaultValue = 50


_EqlVolBalConfigArchivalPlacementThreshold_Object = MibTableColumn
eqlVolBalConfigArchivalPlacementThreshold = _EqlVolBalConfigArchivalPlacementThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 18),
    _EqlVolBalConfigArchivalPlacementThreshold_Type()
)
eqlVolBalConfigArchivalPlacementThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalConfigArchivalPlacementThreshold.setStatus("current")


class _EqlVolBalConfigFreeSpaceTroubleEnabled_Type(Integer32):
    """Custom type eqlVolBalConfigFreeSpaceTroubleEnabled based on Integer32"""
    defaultValue = 1

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


_EqlVolBalConfigFreeSpaceTroubleEnabled_Type.__name__ = "Integer32"
_EqlVolBalConfigFreeSpaceTroubleEnabled_Object = MibTableColumn
eqlVolBalConfigFreeSpaceTroubleEnabled = _EqlVolBalConfigFreeSpaceTroubleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 19),
    _EqlVolBalConfigFreeSpaceTroubleEnabled_Type()
)
eqlVolBalConfigFreeSpaceTroubleEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolBalConfigFreeSpaceTroubleEnabled.setStatus("current")


class _EqlVolBalConfigPreferAutoRAIDPlacement_Type(Integer32):
    """Custom type eqlVolBalConfigPreferAutoRAIDPlacement based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EqlVolBalConfigPreferAutoRAIDPlacement_Type.__name__ = "Integer32"
_EqlVolBalConfigPreferAutoRAIDPlacement_Object = MibTableColumn
eqlVolBalConfigPreferAutoRAIDPlacement = _EqlVolBalConfigPreferAutoRAIDPlacement_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 20),
    _EqlVolBalConfigPreferAutoRAIDPlacement_Type()
)
eqlVolBalConfigPreferAutoRAIDPlacement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolBalConfigPreferAutoRAIDPlacement.setStatus("current")


class _EqlVolBalConfigHotColdPageSwapEnabled_Type(Integer32):
    """Custom type eqlVolBalConfigHotColdPageSwapEnabled based on Integer32"""
    defaultValue = 1

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


_EqlVolBalConfigHotColdPageSwapEnabled_Type.__name__ = "Integer32"
_EqlVolBalConfigHotColdPageSwapEnabled_Object = MibTableColumn
eqlVolBalConfigHotColdPageSwapEnabled = _EqlVolBalConfigHotColdPageSwapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 21),
    _EqlVolBalConfigHotColdPageSwapEnabled_Type()
)
eqlVolBalConfigHotColdPageSwapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolBalConfigHotColdPageSwapEnabled.setStatus("current")


class _EqlVolBalConfigArchiveEnabled_Type(Integer32):
    """Custom type eqlVolBalConfigArchiveEnabled based on Integer32"""
    defaultValue = 1

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


_EqlVolBalConfigArchiveEnabled_Type.__name__ = "Integer32"
_EqlVolBalConfigArchiveEnabled_Object = MibTableColumn
eqlVolBalConfigArchiveEnabled = _EqlVolBalConfigArchiveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 5, 1, 22),
    _EqlVolBalConfigArchiveEnabled_Type()
)
eqlVolBalConfigArchiveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolBalConfigArchiveEnabled.setStatus("current")
_EqlVolBalPlanTable_Object = MibTable
eqlVolBalPlanTable = _EqlVolBalPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6)
)
if mibBuilder.loadTexts:
    eqlVolBalPlanTable.setStatus("current")
_EqlVolBalPlanEntry_Object = MibTableRow
eqlVolBalPlanEntry = _EqlVolBalPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1)
)
eqlVolBalPlanEntry.setIndexNames(
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlVolBalPlanIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
)
if mibBuilder.loadTexts:
    eqlVolBalPlanEntry.setStatus("current")
_EqlVolBalPlanIndex_Type = Unsigned32
_EqlVolBalPlanIndex_Object = MibTableColumn
eqlVolBalPlanIndex = _EqlVolBalPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 1),
    _EqlVolBalPlanIndex_Type()
)
eqlVolBalPlanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalPlanIndex.setStatus("current")


class _EqlVolBalPlanReason_Type(Integer32):
    """Custom type eqlVolBalPlanReason based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("archive", 9),
          ("balance", 4),
          ("bind", 3),
          ("free-space-trouble", 1),
          ("move-site", 7),
          ("move-volume", 6),
          ("performance-trouble", 8),
          ("vacate", 2),
          ("vacate-pool", 5))
    )


_EqlVolBalPlanReason_Type.__name__ = "Integer32"
_EqlVolBalPlanReason_Object = MibTableColumn
eqlVolBalPlanReason = _EqlVolBalPlanReason_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 2),
    _EqlVolBalPlanReason_Type()
)
eqlVolBalPlanReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalPlanReason.setStatus("current")
_EqlVolBalPlanComplete_Type = TruthValue
_EqlVolBalPlanComplete_Object = MibTableColumn
eqlVolBalPlanComplete = _EqlVolBalPlanComplete_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 3),
    _EqlVolBalPlanComplete_Type()
)
eqlVolBalPlanComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanComplete.setStatus("current")
_EqlVolBalPlanStartTime_Type = Counter32
_EqlVolBalPlanStartTime_Object = MibTableColumn
eqlVolBalPlanStartTime = _EqlVolBalPlanStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 4),
    _EqlVolBalPlanStartTime_Type()
)
eqlVolBalPlanStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalPlanStartTime.setStatus("current")
_EqlVolBalPlanEndTime_Type = Counter32
_EqlVolBalPlanEndTime_Object = MibTableColumn
eqlVolBalPlanEndTime = _EqlVolBalPlanEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 5),
    _EqlVolBalPlanEndTime_Type()
)
eqlVolBalPlanEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalPlanEndTime.setStatus("current")


class _EqlVolBalPlanState_Type(Integer32):
    """Custom type eqlVolBalPlanState based on Integer32"""
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
        *(("cancelled", 6),
          ("finished", 7),
          ("invalid", 3),
          ("ready", 4),
          ("started", 5),
          ("writing", 1),
          ("written", 2))
    )


_EqlVolBalPlanState_Type.__name__ = "Integer32"
_EqlVolBalPlanState_Object = MibTableColumn
eqlVolBalPlanState = _EqlVolBalPlanState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 6),
    _EqlVolBalPlanState_Type()
)
eqlVolBalPlanState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalPlanState.setStatus("current")


class _EqlVolBalPlanVacatingMemberUUID_Type(OctetString):
    """Custom type eqlVolBalPlanVacatingMemberUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalPlanVacatingMemberUUID_Type.__name__ = "OctetString"
_EqlVolBalPlanVacatingMemberUUID_Object = MibTableColumn
eqlVolBalPlanVacatingMemberUUID = _EqlVolBalPlanVacatingMemberUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 7),
    _EqlVolBalPlanVacatingMemberUUID_Type()
)
eqlVolBalPlanVacatingMemberUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanVacatingMemberUUID.setStatus("current")
_EqlVolBalPlanTotalPages_Type = Counter64
_EqlVolBalPlanTotalPages_Object = MibTableColumn
eqlVolBalPlanTotalPages = _EqlVolBalPlanTotalPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 8),
    _EqlVolBalPlanTotalPages_Type()
)
eqlVolBalPlanTotalPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanTotalPages.setStatus("current")
_EqlVolBalPlanEntryStatus_Type = RowStatus
_EqlVolBalPlanEntryStatus_Object = MibTableColumn
eqlVolBalPlanEntryStatus = _EqlVolBalPlanEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 9),
    _EqlVolBalPlanEntryStatus_Type()
)
eqlVolBalPlanEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalPlanEntryStatus.setStatus("current")


class _EqlVolBalPlanFlags_Type(Integer32):
    """Custom type eqlVolBalPlanFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mixedModeBit", 1)
    )


_EqlVolBalPlanFlags_Type.__name__ = "Integer32"
_EqlVolBalPlanFlags_Object = MibTableColumn
eqlVolBalPlanFlags = _EqlVolBalPlanFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 10),
    _EqlVolBalPlanFlags_Type()
)
eqlVolBalPlanFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalPlanFlags.setStatus("current")
_EqlVolBalPlanTotalAllocatedPages_Type = Counter64
_EqlVolBalPlanTotalAllocatedPages_Object = MibTableColumn
eqlVolBalPlanTotalAllocatedPages = _EqlVolBalPlanTotalAllocatedPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 11),
    _EqlVolBalPlanTotalAllocatedPages_Type()
)
eqlVolBalPlanTotalAllocatedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanTotalAllocatedPages.setStatus("current")
_EqlVolBalPlanAllocatedPagesMoved_Type = Counter64
_EqlVolBalPlanAllocatedPagesMoved_Object = MibTableColumn
eqlVolBalPlanAllocatedPagesMoved = _EqlVolBalPlanAllocatedPagesMoved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 12),
    _EqlVolBalPlanAllocatedPagesMoved_Type()
)
eqlVolBalPlanAllocatedPagesMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanAllocatedPagesMoved.setStatus("current")
_EqlVolBalPlanAssignedPagesMoved_Type = Counter64
_EqlVolBalPlanAssignedPagesMoved_Object = MibTableColumn
eqlVolBalPlanAssignedPagesMoved = _EqlVolBalPlanAssignedPagesMoved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 13),
    _EqlVolBalPlanAssignedPagesMoved_Type()
)
eqlVolBalPlanAssignedPagesMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanAssignedPagesMoved.setStatus("current")
_EqlVolBalPlanHistoryTableIndex_Type = Unsigned32
_EqlVolBalPlanHistoryTableIndex_Object = MibTableColumn
eqlVolBalPlanHistoryTableIndex = _EqlVolBalPlanHistoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 14),
    _EqlVolBalPlanHistoryTableIndex_Type()
)
eqlVolBalPlanHistoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanHistoryTableIndex.setStatus("current")
_EqlVolBalPlanHistoryTableMemberIndex_Type = Unsigned32
_EqlVolBalPlanHistoryTableMemberIndex_Object = MibTableColumn
eqlVolBalPlanHistoryTableMemberIndex = _EqlVolBalPlanHistoryTableMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 15),
    _EqlVolBalPlanHistoryTableMemberIndex_Type()
)
eqlVolBalPlanHistoryTableMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanHistoryTableMemberIndex.setStatus("current")
_EqlVolBalPlanHistoryTableMemberCount_Type = Unsigned32
_EqlVolBalPlanHistoryTableMemberCount_Object = MibTableColumn
eqlVolBalPlanHistoryTableMemberCount = _EqlVolBalPlanHistoryTableMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 16),
    _EqlVolBalPlanHistoryTableMemberCount_Type()
)
eqlVolBalPlanHistoryTableMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanHistoryTableMemberCount.setStatus("current")


class _EqlVolBalPlanFirstAlternateDst_Type(OctetString):
    """Custom type eqlVolBalPlanFirstAlternateDst based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalPlanFirstAlternateDst_Type.__name__ = "OctetString"
_EqlVolBalPlanFirstAlternateDst_Object = MibTableColumn
eqlVolBalPlanFirstAlternateDst = _EqlVolBalPlanFirstAlternateDst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 17),
    _EqlVolBalPlanFirstAlternateDst_Type()
)
eqlVolBalPlanFirstAlternateDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanFirstAlternateDst.setStatus("current")


class _EqlVolBalPlanSecondAlternateDst_Type(OctetString):
    """Custom type eqlVolBalPlanSecondAlternateDst based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalPlanSecondAlternateDst_Type.__name__ = "OctetString"
_EqlVolBalPlanSecondAlternateDst_Object = MibTableColumn
eqlVolBalPlanSecondAlternateDst = _EqlVolBalPlanSecondAlternateDst_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 18),
    _EqlVolBalPlanSecondAlternateDst_Type()
)
eqlVolBalPlanSecondAlternateDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanSecondAlternateDst.setStatus("current")
_EqlVolBalPlanTotalSnapPages_Type = Counter64
_EqlVolBalPlanTotalSnapPages_Object = MibTableColumn
eqlVolBalPlanTotalSnapPages = _EqlVolBalPlanTotalSnapPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 19),
    _EqlVolBalPlanTotalSnapPages_Type()
)
eqlVolBalPlanTotalSnapPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanTotalSnapPages.setStatus("current")
_EqlVolBalPlanSnapPagesMoved_Type = Counter64
_EqlVolBalPlanSnapPagesMoved_Object = MibTableColumn
eqlVolBalPlanSnapPagesMoved = _EqlVolBalPlanSnapPagesMoved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 6, 1, 20),
    _EqlVolBalPlanSnapPagesMoved_Type()
)
eqlVolBalPlanSnapPagesMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalPlanSnapPagesMoved.setStatus("current")
_EqlVolBalTaskTable_Object = MibTable
eqlVolBalTaskTable = _EqlVolBalTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7)
)
if mibBuilder.loadTexts:
    eqlVolBalTaskTable.setStatus("current")
_EqlVolBalTaskEntry_Object = MibTableRow
eqlVolBalTaskEntry = _EqlVolBalTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1)
)
eqlVolBalTaskEntry.setIndexNames(
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlVolBalPlanIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlVolBalTaskIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
)
if mibBuilder.loadTexts:
    eqlVolBalTaskEntry.setStatus("current")
_EqlVolBalTaskIndex_Type = Unsigned32
_EqlVolBalTaskIndex_Object = MibTableColumn
eqlVolBalTaskIndex = _EqlVolBalTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 1),
    _EqlVolBalTaskIndex_Type()
)
eqlVolBalTaskIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskIndex.setStatus("current")


class _EqlVolBalTaskVolumePsvId_Type(OctetString):
    """Custom type eqlVolBalTaskVolumePsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalTaskVolumePsvId_Type.__name__ = "OctetString"
_EqlVolBalTaskVolumePsvId_Object = MibTableColumn
eqlVolBalTaskVolumePsvId = _EqlVolBalTaskVolumePsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 2),
    _EqlVolBalTaskVolumePsvId_Type()
)
eqlVolBalTaskVolumePsvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalTaskVolumePsvId.setStatus("current")


class _EqlVolBalTaskSrcDriveGroup_Type(OctetString):
    """Custom type eqlVolBalTaskSrcDriveGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalTaskSrcDriveGroup_Type.__name__ = "OctetString"
_EqlVolBalTaskSrcDriveGroup_Object = MibTableColumn
eqlVolBalTaskSrcDriveGroup = _EqlVolBalTaskSrcDriveGroup_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 3),
    _EqlVolBalTaskSrcDriveGroup_Type()
)
eqlVolBalTaskSrcDriveGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskSrcDriveGroup.setStatus("current")


class _EqlVolBalTaskSrcName_Type(DisplayString):
    """Custom type eqlVolBalTaskSrcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EqlVolBalTaskSrcName_Type.__name__ = "DisplayString"
_EqlVolBalTaskSrcName_Object = MibTableColumn
eqlVolBalTaskSrcName = _EqlVolBalTaskSrcName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 4),
    _EqlVolBalTaskSrcName_Type()
)
eqlVolBalTaskSrcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskSrcName.setStatus("current")


class _EqlVolBalTaskDstDriveGroup_Type(OctetString):
    """Custom type eqlVolBalTaskDstDriveGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalTaskDstDriveGroup_Type.__name__ = "OctetString"
_EqlVolBalTaskDstDriveGroup_Object = MibTableColumn
eqlVolBalTaskDstDriveGroup = _EqlVolBalTaskDstDriveGroup_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 5),
    _EqlVolBalTaskDstDriveGroup_Type()
)
eqlVolBalTaskDstDriveGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskDstDriveGroup.setStatus("current")


class _EqlVolBalTaskDstName_Type(DisplayString):
    """Custom type eqlVolBalTaskDstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EqlVolBalTaskDstName_Type.__name__ = "DisplayString"
_EqlVolBalTaskDstName_Object = MibTableColumn
eqlVolBalTaskDstName = _EqlVolBalTaskDstName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 6),
    _EqlVolBalTaskDstName_Type()
)
eqlVolBalTaskDstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskDstName.setStatus("current")
_EqlVolBalTaskSrcInitialPageCount_Type = Counter64
_EqlVolBalTaskSrcInitialPageCount_Object = MibTableColumn
eqlVolBalTaskSrcInitialPageCount = _EqlVolBalTaskSrcInitialPageCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 7),
    _EqlVolBalTaskSrcInitialPageCount_Type()
)
eqlVolBalTaskSrcInitialPageCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskSrcInitialPageCount.setStatus("current")
_EqlVolBalTaskNumPages_Type = Counter64
_EqlVolBalTaskNumPages_Object = MibTableColumn
eqlVolBalTaskNumPages = _EqlVolBalTaskNumPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 8),
    _EqlVolBalTaskNumPages_Type()
)
eqlVolBalTaskNumPages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskNumPages.setStatus("current")
_EqlVolBalTaskCoordinateWith_Type = Unsigned32
_EqlVolBalTaskCoordinateWith_Object = MibTableColumn
eqlVolBalTaskCoordinateWith = _EqlVolBalTaskCoordinateWith_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 9),
    _EqlVolBalTaskCoordinateWith_Type()
)
eqlVolBalTaskCoordinateWith.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolBalTaskCoordinateWith.setStatus("current")


class _EqlVolBalTaskType_Type(Integer32):
    """Custom type eqlVolBalTaskType based on Integer32"""
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
        *(("balance", 1),
          ("besteffort", 7),
          ("explicit", 3),
          ("movecold", 5),
          ("movehot", 4),
          ("movesingle", 6),
          ("moveslice", 2),
          ("movesliceuncompressed", 8))
    )


_EqlVolBalTaskType_Type.__name__ = "Integer32"
_EqlVolBalTaskType_Object = MibTableColumn
eqlVolBalTaskType = _EqlVolBalTaskType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 10),
    _EqlVolBalTaskType_Type()
)
eqlVolBalTaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskType.setStatus("current")


class _EqlVolBalTaskState_Type(Integer32):
    """Custom type eqlVolBalTaskState based on Integer32"""
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
        *(("active", 2),
          ("cancel", 3),
          ("done", 4),
          ("failed", 5),
          ("ready", 1))
    )


_EqlVolBalTaskState_Type.__name__ = "Integer32"
_EqlVolBalTaskState_Object = MibTableColumn
eqlVolBalTaskState = _EqlVolBalTaskState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 11),
    _EqlVolBalTaskState_Type()
)
eqlVolBalTaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskState.setStatus("current")
_EqlVolBalTaskEntryStatus_Type = RowStatus
_EqlVolBalTaskEntryStatus_Object = MibTableColumn
eqlVolBalTaskEntryStatus = _EqlVolBalTaskEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 12),
    _EqlVolBalTaskEntryStatus_Type()
)
eqlVolBalTaskEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskEntryStatus.setStatus("current")


class _EqlVolBalTaskVolLeader_Type(OctetString):
    """Custom type eqlVolBalTaskVolLeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalTaskVolLeader_Type.__name__ = "OctetString"
_EqlVolBalTaskVolLeader_Object = MibTableColumn
eqlVolBalTaskVolLeader = _EqlVolBalTaskVolLeader_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 13),
    _EqlVolBalTaskVolLeader_Type()
)
eqlVolBalTaskVolLeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskVolLeader.setStatus("current")
_EqlVolBalTaskNumAllocatedPages_Type = Counter64
_EqlVolBalTaskNumAllocatedPages_Object = MibTableColumn
eqlVolBalTaskNumAllocatedPages = _EqlVolBalTaskNumAllocatedPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 14),
    _EqlVolBalTaskNumAllocatedPages_Type()
)
eqlVolBalTaskNumAllocatedPages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskNumAllocatedPages.setStatus("current")
_EqlVolBalTaskNumSnapPages_Type = Counter64
_EqlVolBalTaskNumSnapPages_Object = MibTableColumn
eqlVolBalTaskNumSnapPages = _EqlVolBalTaskNumSnapPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 7, 1, 15),
    _EqlVolBalTaskNumSnapPages_Type()
)
eqlVolBalTaskNumSnapPages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskNumSnapPages.setStatus("current")
_EqlVolBalTaskPickedPagesTable_Object = MibTable
eqlVolBalTaskPickedPagesTable = _EqlVolBalTaskPickedPagesTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 8)
)
if mibBuilder.loadTexts:
    eqlVolBalTaskPickedPagesTable.setStatus("current")
_EqlVolBalTaskPickedPagesEntry_Object = MibTableRow
eqlVolBalTaskPickedPagesEntry = _EqlVolBalTaskPickedPagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 8, 1)
)
eqlVolBalTaskPickedPagesEntry.setIndexNames(
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlVolBalPlanIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlVolBalTaskIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
)
if mibBuilder.loadTexts:
    eqlVolBalTaskPickedPagesEntry.setStatus("current")
_EqlVolBalTaskPickedProgress_Type = Counter64
_EqlVolBalTaskPickedProgress_Object = MibTableColumn
eqlVolBalTaskPickedProgress = _EqlVolBalTaskPickedProgress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 8, 1, 1),
    _EqlVolBalTaskPickedProgress_Type()
)
eqlVolBalTaskPickedProgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskPickedProgress.setStatus("current")
_EqlVolBalTaskPickedPagesCount_Type = Unsigned32
_EqlVolBalTaskPickedPagesCount_Object = MibTableColumn
eqlVolBalTaskPickedPagesCount = _EqlVolBalTaskPickedPagesCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 8, 1, 2),
    _EqlVolBalTaskPickedPagesCount_Type()
)
eqlVolBalTaskPickedPagesCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskPickedPagesCount.setStatus("current")


class _EqlVolBalTaskPickedPagesContext_Type(OctetString):
    """Custom type eqlVolBalTaskPickedPagesContext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EqlVolBalTaskPickedPagesContext_Type.__name__ = "OctetString"
_EqlVolBalTaskPickedPagesContext_Object = MibTableColumn
eqlVolBalTaskPickedPagesContext = _EqlVolBalTaskPickedPagesContext_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 8, 1, 3),
    _EqlVolBalTaskPickedPagesContext_Type()
)
eqlVolBalTaskPickedPagesContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskPickedPagesContext.setStatus("current")
_EqlVolBalTaskPickedPagesRev_Type = Unsigned32
_EqlVolBalTaskPickedPagesRev_Object = MibTableColumn
eqlVolBalTaskPickedPagesRev = _EqlVolBalTaskPickedPagesRev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 8, 1, 4),
    _EqlVolBalTaskPickedPagesRev_Type()
)
eqlVolBalTaskPickedPagesRev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskPickedPagesRev.setStatus("current")
_EqlVolBalTaskPickedPagesFlags_Type = Unsigned32
_EqlVolBalTaskPickedPagesFlags_Object = MibTableColumn
eqlVolBalTaskPickedPagesFlags = _EqlVolBalTaskPickedPagesFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 8, 1, 5),
    _EqlVolBalTaskPickedPagesFlags_Type()
)
eqlVolBalTaskPickedPagesFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskPickedPagesFlags.setStatus("current")
_EqlVolBalTaskPickedPagesEntryStatus_Type = RowStatus
_EqlVolBalTaskPickedPagesEntryStatus_Object = MibTableColumn
eqlVolBalTaskPickedPagesEntryStatus = _EqlVolBalTaskPickedPagesEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 8, 1, 6),
    _EqlVolBalTaskPickedPagesEntryStatus_Type()
)
eqlVolBalTaskPickedPagesEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskPickedPagesEntryStatus.setStatus("current")


class _EqlVolBalTaskPickedPagesArray_Type(OctetString):
    """Custom type eqlVolBalTaskPickedPagesArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1200, 1200),
    )


_EqlVolBalTaskPickedPagesArray_Type.__name__ = "OctetString"
_EqlVolBalTaskPickedPagesArray_Object = MibTableColumn
eqlVolBalTaskPickedPagesArray = _EqlVolBalTaskPickedPagesArray_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 8, 1, 7),
    _EqlVolBalTaskPickedPagesArray_Type()
)
eqlVolBalTaskPickedPagesArray.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskPickedPagesArray.setStatus("current")
_EqlVolBalTaskPickedPagesAllocatedProgress_Type = Counter64
_EqlVolBalTaskPickedPagesAllocatedProgress_Object = MibTableColumn
eqlVolBalTaskPickedPagesAllocatedProgress = _EqlVolBalTaskPickedPagesAllocatedProgress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 8, 1, 8),
    _EqlVolBalTaskPickedPagesAllocatedProgress_Type()
)
eqlVolBalTaskPickedPagesAllocatedProgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalTaskPickedPagesAllocatedProgress.setStatus("current")
_EqlVolBalSliceStatsTable_Object = MibTable
eqlVolBalSliceStatsTable = _EqlVolBalSliceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 9)
)
if mibBuilder.loadTexts:
    eqlVolBalSliceStatsTable.setStatus("current")
_EqlVolBalSliceStatsEntry_Object = MibTableRow
eqlVolBalSliceStatsEntry = _EqlVolBalSliceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 9, 1)
)
eqlVolBalSliceStatsEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlVolBalSliceStatsEntry.setStatus("current")


class _EqlVolBalSliceMemberUUID_Type(OctetString):
    """Custom type eqlVolBalSliceMemberUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalSliceMemberUUID_Type.__name__ = "OctetString"
_EqlVolBalSliceMemberUUID_Object = MibTableColumn
eqlVolBalSliceMemberUUID = _EqlVolBalSliceMemberUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 9, 1, 1),
    _EqlVolBalSliceMemberUUID_Type()
)
eqlVolBalSliceMemberUUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalSliceMemberUUID.setStatus("current")


class _EqlVolBalSliceVolumeUUID_Type(OctetString):
    """Custom type eqlVolBalSliceVolumeUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalSliceVolumeUUID_Type.__name__ = "OctetString"
_EqlVolBalSliceVolumeUUID_Object = MibTableColumn
eqlVolBalSliceVolumeUUID = _EqlVolBalSliceVolumeUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 9, 1, 2),
    _EqlVolBalSliceVolumeUUID_Type()
)
eqlVolBalSliceVolumeUUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalSliceVolumeUUID.setStatus("current")
_EqlVolBalSliceTimeStamp_Type = Counter32
_EqlVolBalSliceTimeStamp_Object = MibTableColumn
eqlVolBalSliceTimeStamp = _EqlVolBalSliceTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 9, 1, 3),
    _EqlVolBalSliceTimeStamp_Type()
)
eqlVolBalSliceTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalSliceTimeStamp.setStatus("current")
_EqlVolBalSliceStatsRndRdRate_Type = Unsigned32
_EqlVolBalSliceStatsRndRdRate_Object = MibTableColumn
eqlVolBalSliceStatsRndRdRate = _EqlVolBalSliceStatsRndRdRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 9, 1, 7),
    _EqlVolBalSliceStatsRndRdRate_Type()
)
eqlVolBalSliceStatsRndRdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalSliceStatsRndRdRate.setStatus("current")
_EqlVolBalSliceStatsRndWrRate_Type = Unsigned32
_EqlVolBalSliceStatsRndWrRate_Object = MibTableColumn
eqlVolBalSliceStatsRndWrRate = _EqlVolBalSliceStatsRndWrRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 9, 1, 8),
    _EqlVolBalSliceStatsRndWrRate_Type()
)
eqlVolBalSliceStatsRndWrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalSliceStatsRndWrRate.setStatus("current")
_EqlVolBalSliceStatsSeqRdRate_Type = Unsigned32
_EqlVolBalSliceStatsSeqRdRate_Object = MibTableColumn
eqlVolBalSliceStatsSeqRdRate = _EqlVolBalSliceStatsSeqRdRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 9, 1, 9),
    _EqlVolBalSliceStatsSeqRdRate_Type()
)
eqlVolBalSliceStatsSeqRdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalSliceStatsSeqRdRate.setStatus("current")
_EqlVolBalSliceStatsSeqWrRate_Type = Unsigned32
_EqlVolBalSliceStatsSeqWrRate_Object = MibTableColumn
eqlVolBalSliceStatsSeqWrRate = _EqlVolBalSliceStatsSeqWrRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 9, 1, 10),
    _EqlVolBalSliceStatsSeqWrRate_Type()
)
eqlVolBalSliceStatsSeqWrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalSliceStatsSeqWrRate.setStatus("current")
_EqlVolBalSliceStatsPlacementScore_Type = Unsigned32
_EqlVolBalSliceStatsPlacementScore_Object = MibTableColumn
eqlVolBalSliceStatsPlacementScore = _EqlVolBalSliceStatsPlacementScore_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 9, 1, 11),
    _EqlVolBalSliceStatsPlacementScore_Type()
)
eqlVolBalSliceStatsPlacementScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalSliceStatsPlacementScore.setStatus("current")
_EqlVolBalMemberStatsTable_Object = MibTable
eqlVolBalMemberStatsTable = _EqlVolBalMemberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 10)
)
if mibBuilder.loadTexts:
    eqlVolBalMemberStatsTable.setStatus("current")
_EqlVolBalMemberStatsEntry_Object = MibTableRow
eqlVolBalMemberStatsEntry = _EqlVolBalMemberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 10, 1)
)
eqlVolBalMemberStatsEntry.setIndexNames(
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlVolBalMemberStatsEntry.setStatus("current")


class _EqlVolBalMemberUUID_Type(OctetString):
    """Custom type eqlVolBalMemberUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalMemberUUID_Type.__name__ = "OctetString"
_EqlVolBalMemberUUID_Object = MibTableColumn
eqlVolBalMemberUUID = _EqlVolBalMemberUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 10, 1, 1),
    _EqlVolBalMemberUUID_Type()
)
eqlVolBalMemberUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalMemberUUID.setStatus("current")
_EqlVolBalMemberTimeStamp_Type = Counter32
_EqlVolBalMemberTimeStamp_Object = MibTableColumn
eqlVolBalMemberTimeStamp = _EqlVolBalMemberTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 10, 1, 2),
    _EqlVolBalMemberTimeStamp_Type()
)
eqlVolBalMemberTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalMemberTimeStamp.setStatus("current")
_EqlVolBalMemberStatsAvgRespTime_Type = Unsigned32
_EqlVolBalMemberStatsAvgRespTime_Object = MibTableColumn
eqlVolBalMemberStatsAvgRespTime = _EqlVolBalMemberStatsAvgRespTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 10, 1, 4),
    _EqlVolBalMemberStatsAvgRespTime_Type()
)
eqlVolBalMemberStatsAvgRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalMemberStatsAvgRespTime.setStatus("current")
_EqlVolBalMemberStatsCPUUsage_Type = Unsigned32
_EqlVolBalMemberStatsCPUUsage_Object = MibTableColumn
eqlVolBalMemberStatsCPUUsage = _EqlVolBalMemberStatsCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 10, 1, 5),
    _EqlVolBalMemberStatsCPUUsage_Type()
)
eqlVolBalMemberStatsCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalMemberStatsCPUUsage.setStatus("current")
_EqlVolBalMemberStatsFreeSpace_Type = Unsigned32
_EqlVolBalMemberStatsFreeSpace_Object = MibTableColumn
eqlVolBalMemberStatsFreeSpace = _EqlVolBalMemberStatsFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 10, 1, 6),
    _EqlVolBalMemberStatsFreeSpace_Type()
)
eqlVolBalMemberStatsFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalMemberStatsFreeSpace.setStatus("current")
_EqlVolBalMemberStatsRndRdRate_Type = Unsigned32
_EqlVolBalMemberStatsRndRdRate_Object = MibTableColumn
eqlVolBalMemberStatsRndRdRate = _EqlVolBalMemberStatsRndRdRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 10, 1, 7),
    _EqlVolBalMemberStatsRndRdRate_Type()
)
eqlVolBalMemberStatsRndRdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalMemberStatsRndRdRate.setStatus("current")
_EqlVolBalMemberStatsRndWrRate_Type = Unsigned32
_EqlVolBalMemberStatsRndWrRate_Object = MibTableColumn
eqlVolBalMemberStatsRndWrRate = _EqlVolBalMemberStatsRndWrRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 10, 1, 8),
    _EqlVolBalMemberStatsRndWrRate_Type()
)
eqlVolBalMemberStatsRndWrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalMemberStatsRndWrRate.setStatus("current")
_EqlVolBalMemberStatsSeqRdRate_Type = Unsigned32
_EqlVolBalMemberStatsSeqRdRate_Object = MibTableColumn
eqlVolBalMemberStatsSeqRdRate = _EqlVolBalMemberStatsSeqRdRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 10, 1, 9),
    _EqlVolBalMemberStatsSeqRdRate_Type()
)
eqlVolBalMemberStatsSeqRdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalMemberStatsSeqRdRate.setStatus("current")
_EqlVolBalMemberStatsSeqWrRate_Type = Unsigned32
_EqlVolBalMemberStatsSeqWrRate_Object = MibTableColumn
eqlVolBalMemberStatsSeqWrRate = _EqlVolBalMemberStatsSeqWrRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 10, 1, 10),
    _EqlVolBalMemberStatsSeqWrRate_Type()
)
eqlVolBalMemberStatsSeqWrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalMemberStatsSeqWrRate.setStatus("current")
_EqlVolBalHistoryTable_Object = MibTable
eqlVolBalHistoryTable = _EqlVolBalHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 11)
)
if mibBuilder.loadTexts:
    eqlVolBalHistoryTable.setStatus("current")
_EqlVolBalHistoryEntry_Object = MibTableRow
eqlVolBalHistoryEntry = _EqlVolBalHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 11, 1)
)
eqlVolBalHistoryEntry.setIndexNames(
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlVolBalHistoryStop"),
)
if mibBuilder.loadTexts:
    eqlVolBalHistoryEntry.setStatus("current")
_EqlVolBalHistoryStop_Type = Unsigned32
_EqlVolBalHistoryStop_Object = MibTableColumn
eqlVolBalHistoryStop = _EqlVolBalHistoryStop_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 11, 1, 1),
    _EqlVolBalHistoryStop_Type()
)
eqlVolBalHistoryStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalHistoryStop.setStatus("current")
_EqlVolBalHistoryStart_Type = Unsigned32
_EqlVolBalHistoryStart_Object = MibTableColumn
eqlVolBalHistoryStart = _EqlVolBalHistoryStart_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 11, 1, 2),
    _EqlVolBalHistoryStart_Type()
)
eqlVolBalHistoryStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalHistoryStart.setStatus("current")
_EqlVolBalHistoryPagesMoved_Type = Unsigned32
_EqlVolBalHistoryPagesMoved_Object = MibTableColumn
eqlVolBalHistoryPagesMoved = _EqlVolBalHistoryPagesMoved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 11, 1, 3),
    _EqlVolBalHistoryPagesMoved_Type()
)
eqlVolBalHistoryPagesMoved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolBalHistoryPagesMoved.setStatus("current")
_EqlVolBalHistoryMembersInvolved_Type = Unsigned32
_EqlVolBalHistoryMembersInvolved_Object = MibTableColumn
eqlVolBalHistoryMembersInvolved = _EqlVolBalHistoryMembersInvolved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 11, 1, 4),
    _EqlVolBalHistoryMembersInvolved_Type()
)
eqlVolBalHistoryMembersInvolved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolBalHistoryMembersInvolved.setStatus("current")
_EqlVolBalHistorySlicesInvolved_Type = Unsigned32
_EqlVolBalHistorySlicesInvolved_Object = MibTableColumn
eqlVolBalHistorySlicesInvolved = _EqlVolBalHistorySlicesInvolved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 11, 1, 5),
    _EqlVolBalHistorySlicesInvolved_Type()
)
eqlVolBalHistorySlicesInvolved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolBalHistorySlicesInvolved.setStatus("current")
_EqlVolBalHistoryBalanceReason_Type = Unsigned32
_EqlVolBalHistoryBalanceReason_Object = MibTableColumn
eqlVolBalHistoryBalanceReason = _EqlVolBalHistoryBalanceReason_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 11, 1, 6),
    _EqlVolBalHistoryBalanceReason_Type()
)
eqlVolBalHistoryBalanceReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolBalHistoryBalanceReason.setStatus("current")
_EqlVolBalCommandTable_Object = MibTable
eqlVolBalCommandTable = _EqlVolBalCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13)
)
if mibBuilder.loadTexts:
    eqlVolBalCommandTable.setStatus("current")
_EqlVolBalCommandEntry_Object = MibTableRow
eqlVolBalCommandEntry = _EqlVolBalCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1)
)
eqlVolBalCommandEntry.setIndexNames(
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlVolBalCommandIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
)
if mibBuilder.loadTexts:
    eqlVolBalCommandEntry.setStatus("current")
_EqlVolBalCommandIndex_Type = Unsigned32
_EqlVolBalCommandIndex_Object = MibTableColumn
eqlVolBalCommandIndex = _EqlVolBalCommandIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 1),
    _EqlVolBalCommandIndex_Type()
)
eqlVolBalCommandIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalCommandIndex.setStatus("current")
_EqlVolBalCommandPlanIndex_Type = Unsigned32
_EqlVolBalCommandPlanIndex_Object = MibTableColumn
eqlVolBalCommandPlanIndex = _EqlVolBalCommandPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 2),
    _EqlVolBalCommandPlanIndex_Type()
)
eqlVolBalCommandPlanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalCommandPlanIndex.setStatus("current")


class _EqlVolBalCommandReason_Type(Integer32):
    """Custom type eqlVolBalCommandReason based on Integer32"""
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
        *(("archive", 10),
          ("balance", 6),
          ("bind", 5),
          ("delete-marshal", 7),
          ("free-space-trouble", 1),
          ("move-site-to-pool", 8),
          ("move-volume-to-pool", 4),
          ("performance-trouble", 9),
          ("vacate", 2),
          ("vacate-pool", 3))
    )


_EqlVolBalCommandReason_Type.__name__ = "Integer32"
_EqlVolBalCommandReason_Object = MibTableColumn
eqlVolBalCommandReason = _EqlVolBalCommandReason_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 3),
    _EqlVolBalCommandReason_Type()
)
eqlVolBalCommandReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalCommandReason.setStatus("current")
_EqlVolBalCommandRunning_Type = TruthValue
_EqlVolBalCommandRunning_Object = MibTableColumn
eqlVolBalCommandRunning = _EqlVolBalCommandRunning_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 4),
    _EqlVolBalCommandRunning_Type()
)
eqlVolBalCommandRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalCommandRunning.setStatus("current")
_EqlVolBalCommandCreateTime_Type = Counter32
_EqlVolBalCommandCreateTime_Object = MibTableColumn
eqlVolBalCommandCreateTime = _EqlVolBalCommandCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 5),
    _EqlVolBalCommandCreateTime_Type()
)
eqlVolBalCommandCreateTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalCommandCreateTime.setStatus("current")


class _EqlVolBalCommandState_Type(Integer32):
    """Custom type eqlVolBalCommandState based on Integer32"""
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
        *(("cancelled", 5),
          ("finished", 6),
          ("invalid", 2),
          ("ready", 3),
          ("started", 4),
          ("writing", 1))
    )


_EqlVolBalCommandState_Type.__name__ = "Integer32"
_EqlVolBalCommandState_Object = MibTableColumn
eqlVolBalCommandState = _EqlVolBalCommandState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 6),
    _EqlVolBalCommandState_Type()
)
eqlVolBalCommandState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalCommandState.setStatus("current")


class _EqlVolBalCommandMemberUUID_Type(OctetString):
    """Custom type eqlVolBalCommandMemberUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalCommandMemberUUID_Type.__name__ = "OctetString"
_EqlVolBalCommandMemberUUID_Object = MibTableColumn
eqlVolBalCommandMemberUUID = _EqlVolBalCommandMemberUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 7),
    _EqlVolBalCommandMemberUUID_Type()
)
eqlVolBalCommandMemberUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalCommandMemberUUID.setStatus("current")


class _EqlVolBalCommandVolumeId_Type(OctetString):
    """Custom type eqlVolBalCommandVolumeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolBalCommandVolumeId_Type.__name__ = "OctetString"
_EqlVolBalCommandVolumeId_Object = MibTableColumn
eqlVolBalCommandVolumeId = _EqlVolBalCommandVolumeId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 8),
    _EqlVolBalCommandVolumeId_Type()
)
eqlVolBalCommandVolumeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolBalCommandVolumeId.setStatus("current")
_EqlVolBalCommandFromPoolId_Type = Unsigned32
_EqlVolBalCommandFromPoolId_Object = MibTableColumn
eqlVolBalCommandFromPoolId = _EqlVolBalCommandFromPoolId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 9),
    _EqlVolBalCommandFromPoolId_Type()
)
eqlVolBalCommandFromPoolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlVolBalCommandFromPoolId.setStatus("current")
_EqlVolBalCommandToPoolId_Type = Unsigned32
_EqlVolBalCommandToPoolId_Object = MibTableColumn
eqlVolBalCommandToPoolId = _EqlVolBalCommandToPoolId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 10),
    _EqlVolBalCommandToPoolId_Type()
)
eqlVolBalCommandToPoolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlVolBalCommandToPoolId.setStatus("current")
_EqlVolBalCommandEntryStatus_Type = RowStatus
_EqlVolBalCommandEntryStatus_Object = MibTableColumn
eqlVolBalCommandEntryStatus = _EqlVolBalCommandEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 11),
    _EqlVolBalCommandEntryStatus_Type()
)
eqlVolBalCommandEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalCommandEntryStatus.setStatus("current")


class _EqlVolBalCommandFlags_Type(Integer32):
    """Custom type eqlVolBalCommandFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mixedModeBit", 1)
    )


_EqlVolBalCommandFlags_Type.__name__ = "Integer32"
_EqlVolBalCommandFlags_Object = MibTableColumn
eqlVolBalCommandFlags = _EqlVolBalCommandFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 12),
    _EqlVolBalCommandFlags_Type()
)
eqlVolBalCommandFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalCommandFlags.setStatus("current")
_EqlVolBalCommandSiteId_Type = Unsigned32
_EqlVolBalCommandSiteId_Object = MibTableColumn
eqlVolBalCommandSiteId = _EqlVolBalCommandSiteId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 13, 1, 13),
    _EqlVolBalCommandSiteId_Type()
)
eqlVolBalCommandSiteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolBalCommandSiteId.setStatus("current")
_EqlPropertiesTable_Object = MibTable
eqlPropertiesTable = _EqlPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 14)
)
if mibBuilder.loadTexts:
    eqlPropertiesTable.setStatus("current")
_EqlPropertiesEntry_Object = MibTableRow
eqlPropertiesEntry = _EqlPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 14, 1)
)
eqlPropertiesEntry.setIndexNames(
    (0, "EQLVOLBALANCER-MIB", "eqlPropertiesIndex"),
)
if mibBuilder.loadTexts:
    eqlPropertiesEntry.setStatus("current")
_EqlPropertiesIndex_Type = Unsigned32
_EqlPropertiesIndex_Object = MibTableColumn
eqlPropertiesIndex = _EqlPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 14, 1, 1),
    _EqlPropertiesIndex_Type()
)
eqlPropertiesIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPropertiesIndex.setStatus("current")


class _EqlPropertiesName_Type(DisplayString):
    """Custom type eqlPropertiesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlPropertiesName_Type.__name__ = "DisplayString"
_EqlPropertiesName_Object = MibTableColumn
eqlPropertiesName = _EqlPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 14, 1, 2),
    _EqlPropertiesName_Type()
)
eqlPropertiesName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPropertiesName.setStatus("current")


class _EqlPropertiesValue_Type(DisplayString):
    """Custom type eqlPropertiesValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlPropertiesValue_Type.__name__ = "DisplayString"
_EqlPropertiesValue_Object = MibTableColumn
eqlPropertiesValue = _EqlPropertiesValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 14, 1, 3),
    _EqlPropertiesValue_Type()
)
eqlPropertiesValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPropertiesValue.setStatus("current")
_EqlPageMoveHistoryTableFreeSlot_ObjectIdentity = ObjectIdentity
eqlPageMoveHistoryTableFreeSlot = _EqlPageMoveHistoryTableFreeSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 15)
)


class _EqlPageMoveHistoryTableNextFreeSlot_Type(Unsigned32):
    """Custom type eqlPageMoveHistoryTableNextFreeSlot based on Unsigned32"""
    defaultValue = 1


_EqlPageMoveHistoryTableNextFreeSlot_Object = MibScalar
eqlPageMoveHistoryTableNextFreeSlot = _EqlPageMoveHistoryTableNextFreeSlot_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 15, 1),
    _EqlPageMoveHistoryTableNextFreeSlot_Type()
)
eqlPageMoveHistoryTableNextFreeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryTableNextFreeSlot.setStatus("current")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryTableNextFreeSlot.setUnits("none")


class _EqlPageMoveHistoryTableMemberNextFreeSlot_Type(Unsigned32):
    """Custom type eqlPageMoveHistoryTableMemberNextFreeSlot based on Unsigned32"""
    defaultValue = 1


_EqlPageMoveHistoryTableMemberNextFreeSlot_Object = MibScalar
eqlPageMoveHistoryTableMemberNextFreeSlot = _EqlPageMoveHistoryTableMemberNextFreeSlot_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 15, 2),
    _EqlPageMoveHistoryTableMemberNextFreeSlot_Type()
)
eqlPageMoveHistoryTableMemberNextFreeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryTableMemberNextFreeSlot.setStatus("current")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryTableMemberNextFreeSlot.setUnits("none")
_EqlPageMoveHistoryTable_Object = MibTable
eqlPageMoveHistoryTable = _EqlPageMoveHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16)
)
if mibBuilder.loadTexts:
    eqlPageMoveHistoryTable.setStatus("current")
_EqlPageMoveHistoryEntry_Object = MibTableRow
eqlPageMoveHistoryEntry = _EqlPageMoveHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1)
)
eqlPageMoveHistoryEntry.setIndexNames(
    (0, "EQLVOLBALANCER-MIB", "eqlPageMoveHistoryIndex"),
)
if mibBuilder.loadTexts:
    eqlPageMoveHistoryEntry.setStatus("current")
_EqlPageMoveHistoryIndex_Type = Unsigned32
_EqlPageMoveHistoryIndex_Object = MibTableColumn
eqlPageMoveHistoryIndex = _EqlPageMoveHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 1),
    _EqlPageMoveHistoryIndex_Type()
)
eqlPageMoveHistoryIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryIndex.setStatus("current")
_EqlPageMoveHistoryPoolId_Type = Unsigned32
_EqlPageMoveHistoryPoolId_Object = MibTableColumn
eqlPageMoveHistoryPoolId = _EqlPageMoveHistoryPoolId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 2),
    _EqlPageMoveHistoryPoolId_Type()
)
eqlPageMoveHistoryPoolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryPoolId.setStatus("current")
_EqlPageMoveHistoryPlanId_Type = Unsigned32
_EqlPageMoveHistoryPlanId_Object = MibTableColumn
eqlPageMoveHistoryPlanId = _EqlPageMoveHistoryPlanId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 3),
    _EqlPageMoveHistoryPlanId_Type()
)
eqlPageMoveHistoryPlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryPlanId.setStatus("current")
_EqlPageMoveHistoryMemberId_Type = Unsigned32
_EqlPageMoveHistoryMemberId_Object = MibTableColumn
eqlPageMoveHistoryMemberId = _EqlPageMoveHistoryMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 4),
    _EqlPageMoveHistoryMemberId_Type()
)
eqlPageMoveHistoryMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberId.setStatus("current")


class _EqlPageMoveHistoryType_Type(Integer32):
    """Custom type eqlPageMoveHistoryType based on Integer32"""
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
        *(("balance", 4),
          ("bind", 3),
          ("free-space-trouble", 1),
          ("move-site", 7),
          ("move-volume", 6),
          ("performance-trouble", 8),
          ("vacate", 2),
          ("vacate-pool", 5))
    )


_EqlPageMoveHistoryType_Type.__name__ = "Integer32"
_EqlPageMoveHistoryType_Object = MibTableColumn
eqlPageMoveHistoryType = _EqlPageMoveHistoryType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 5),
    _EqlPageMoveHistoryType_Type()
)
eqlPageMoveHistoryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryType.setStatus("current")
_EqlPageMoveHistoryStartTime_Type = Counter32
_EqlPageMoveHistoryStartTime_Object = MibTableColumn
eqlPageMoveHistoryStartTime = _EqlPageMoveHistoryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 6),
    _EqlPageMoveHistoryStartTime_Type()
)
eqlPageMoveHistoryStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryStartTime.setStatus("current")
_EqlPageMoveHistoryEndTime_Type = Counter32
_EqlPageMoveHistoryEndTime_Object = MibTableColumn
eqlPageMoveHistoryEndTime = _EqlPageMoveHistoryEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 7),
    _EqlPageMoveHistoryEndTime_Type()
)
eqlPageMoveHistoryEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryEndTime.setStatus("current")
_EqlPageMoveHistoryTotalPages_Type = Counter64
_EqlPageMoveHistoryTotalPages_Object = MibTableColumn
eqlPageMoveHistoryTotalPages = _EqlPageMoveHistoryTotalPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 8),
    _EqlPageMoveHistoryTotalPages_Type()
)
eqlPageMoveHistoryTotalPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryTotalPages.setStatus("current")
_EqlPageMoveHistoryAllocatedPages_Type = Counter64
_EqlPageMoveHistoryAllocatedPages_Object = MibTableColumn
eqlPageMoveHistoryAllocatedPages = _EqlPageMoveHistoryAllocatedPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 9),
    _EqlPageMoveHistoryAllocatedPages_Type()
)
eqlPageMoveHistoryAllocatedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryAllocatedPages.setStatus("current")
_EqlPageMoveHistoryTotalPagesMoved_Type = Counter64
_EqlPageMoveHistoryTotalPagesMoved_Object = MibTableColumn
eqlPageMoveHistoryTotalPagesMoved = _EqlPageMoveHistoryTotalPagesMoved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 10),
    _EqlPageMoveHistoryTotalPagesMoved_Type()
)
eqlPageMoveHistoryTotalPagesMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryTotalPagesMoved.setStatus("current")
_EqlPageMoveHistoryAllocatedPagesMoved_Type = Counter64
_EqlPageMoveHistoryAllocatedPagesMoved_Object = MibTableColumn
eqlPageMoveHistoryAllocatedPagesMoved = _EqlPageMoveHistoryAllocatedPagesMoved_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 11),
    _EqlPageMoveHistoryAllocatedPagesMoved_Type()
)
eqlPageMoveHistoryAllocatedPagesMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryAllocatedPagesMoved.setStatus("current")


class _EqlPageMoveHistoryResult_Type(Integer32):
    """Custom type eqlPageMoveHistoryResult based on Integer32"""
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
        *(("aborted", 5),
          ("cancelled", 3),
          ("completed", 2),
          ("inprogress", 4),
          ("ready", 1))
    )


_EqlPageMoveHistoryResult_Type.__name__ = "Integer32"
_EqlPageMoveHistoryResult_Object = MibTableColumn
eqlPageMoveHistoryResult = _EqlPageMoveHistoryResult_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 12),
    _EqlPageMoveHistoryResult_Type()
)
eqlPageMoveHistoryResult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryResult.setStatus("current")
_EqlPageMoveHistoryMemberStartIndex_Type = Unsigned32
_EqlPageMoveHistoryMemberStartIndex_Object = MibTableColumn
eqlPageMoveHistoryMemberStartIndex = _EqlPageMoveHistoryMemberStartIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 13),
    _EqlPageMoveHistoryMemberStartIndex_Type()
)
eqlPageMoveHistoryMemberStartIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberStartIndex.setStatus("current")
_EqlPageMoveHistoryMemberCount_Type = Unsigned32
_EqlPageMoveHistoryMemberCount_Object = MibTableColumn
eqlPageMoveHistoryMemberCount = _EqlPageMoveHistoryMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 16, 1, 14),
    _EqlPageMoveHistoryMemberCount_Type()
)
eqlPageMoveHistoryMemberCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberCount.setStatus("current")
_EqlPageMoveHistoryMemberTable_Object = MibTable
eqlPageMoveHistoryMemberTable = _EqlPageMoveHistoryMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18)
)
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberTable.setStatus("current")
_EqlPageMoveHistoryMemberEntry_Object = MibTableRow
eqlPageMoveHistoryMemberEntry = _EqlPageMoveHistoryMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18, 1)
)
eqlPageMoveHistoryMemberEntry.setIndexNames(
    (0, "EQLVOLBALANCER-MIB", "eqlPageMoveHistoryMemberIndex"),
)
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberEntry.setStatus("current")
_EqlPageMoveHistoryMemberIndex_Type = Unsigned32
_EqlPageMoveHistoryMemberIndex_Object = MibTableColumn
eqlPageMoveHistoryMemberIndex = _EqlPageMoveHistoryMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18, 1, 1),
    _EqlPageMoveHistoryMemberIndex_Type()
)
eqlPageMoveHistoryMemberIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberIndex.setStatus("current")
_EqlPageMoveHistoryMemberParentIndex_Type = Unsigned32
_EqlPageMoveHistoryMemberParentIndex_Object = MibTableColumn
eqlPageMoveHistoryMemberParentIndex = _EqlPageMoveHistoryMemberParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18, 1, 2),
    _EqlPageMoveHistoryMemberParentIndex_Type()
)
eqlPageMoveHistoryMemberParentIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberParentIndex.setStatus("current")
_EqlPageMoveHistoryMemberPlanId_Type = Unsigned32
_EqlPageMoveHistoryMemberPlanId_Object = MibTableColumn
eqlPageMoveHistoryMemberPlanId = _EqlPageMoveHistoryMemberPlanId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18, 1, 3),
    _EqlPageMoveHistoryMemberPlanId_Type()
)
eqlPageMoveHistoryMemberPlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberPlanId.setStatus("current")


class _EqlPageMoveHistoryMemberUuid_Type(OctetString):
    """Custom type eqlPageMoveHistoryMemberUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlPageMoveHistoryMemberUuid_Type.__name__ = "OctetString"
_EqlPageMoveHistoryMemberUuid_Object = MibTableColumn
eqlPageMoveHistoryMemberUuid = _EqlPageMoveHistoryMemberUuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18, 1, 4),
    _EqlPageMoveHistoryMemberUuid_Type()
)
eqlPageMoveHistoryMemberUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberUuid.setStatus("current")
_EqlPageMoveHistoryMemberAddedPages_Type = Counter64
_EqlPageMoveHistoryMemberAddedPages_Object = MibTableColumn
eqlPageMoveHistoryMemberAddedPages = _EqlPageMoveHistoryMemberAddedPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18, 1, 5),
    _EqlPageMoveHistoryMemberAddedPages_Type()
)
eqlPageMoveHistoryMemberAddedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberAddedPages.setStatus("current")
_EqlPageMoveHistoryMemberAddedAllocatedPages_Type = Counter64
_EqlPageMoveHistoryMemberAddedAllocatedPages_Object = MibTableColumn
eqlPageMoveHistoryMemberAddedAllocatedPages = _EqlPageMoveHistoryMemberAddedAllocatedPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18, 1, 6),
    _EqlPageMoveHistoryMemberAddedAllocatedPages_Type()
)
eqlPageMoveHistoryMemberAddedAllocatedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberAddedAllocatedPages.setStatus("current")
_EqlPageMoveHistoryMemberRemovedPages_Type = Counter64
_EqlPageMoveHistoryMemberRemovedPages_Object = MibTableColumn
eqlPageMoveHistoryMemberRemovedPages = _EqlPageMoveHistoryMemberRemovedPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18, 1, 7),
    _EqlPageMoveHistoryMemberRemovedPages_Type()
)
eqlPageMoveHistoryMemberRemovedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberRemovedPages.setStatus("current")
_EqlPageMoveHistoryMemberRemovedAllocatedPages_Type = Counter64
_EqlPageMoveHistoryMemberRemovedAllocatedPages_Object = MibTableColumn
eqlPageMoveHistoryMemberRemovedAllocatedPages = _EqlPageMoveHistoryMemberRemovedAllocatedPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18, 1, 8),
    _EqlPageMoveHistoryMemberRemovedAllocatedPages_Type()
)
eqlPageMoveHistoryMemberRemovedAllocatedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberRemovedAllocatedPages.setStatus("current")
_EqlPageMoveHistoryMemberStartAUS_Type = Unsigned32
_EqlPageMoveHistoryMemberStartAUS_Object = MibTableColumn
eqlPageMoveHistoryMemberStartAUS = _EqlPageMoveHistoryMemberStartAUS_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18, 1, 9),
    _EqlPageMoveHistoryMemberStartAUS_Type()
)
eqlPageMoveHistoryMemberStartAUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberStartAUS.setStatus("current")
_EqlPageMoveHistoryMemberExpectedEndAUS_Type = Unsigned32
_EqlPageMoveHistoryMemberExpectedEndAUS_Object = MibTableColumn
eqlPageMoveHistoryMemberExpectedEndAUS = _EqlPageMoveHistoryMemberExpectedEndAUS_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 18, 1, 10),
    _EqlPageMoveHistoryMemberExpectedEndAUS_Type()
)
eqlPageMoveHistoryMemberExpectedEndAUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPageMoveHistoryMemberExpectedEndAUS.setStatus("current")
_EqlLocalIOCountsTableFreeSlot_ObjectIdentity = ObjectIdentity
eqlLocalIOCountsTableFreeSlot = _EqlLocalIOCountsTableFreeSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 19)
)


class _EqlLocalIOCountsTableNextFreeSlot_Type(Unsigned32):
    """Custom type eqlLocalIOCountsTableNextFreeSlot based on Unsigned32"""
    defaultValue = 1


_EqlLocalIOCountsTableNextFreeSlot_Object = MibScalar
eqlLocalIOCountsTableNextFreeSlot = _EqlLocalIOCountsTableNextFreeSlot_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 19, 1),
    _EqlLocalIOCountsTableNextFreeSlot_Type()
)
eqlLocalIOCountsTableNextFreeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlLocalIOCountsTableNextFreeSlot.setStatus("current")
if mibBuilder.loadTexts:
    eqlLocalIOCountsTableNextFreeSlot.setUnits("none")
_EqlLocalIOCountsTable_Object = MibTable
eqlLocalIOCountsTable = _EqlLocalIOCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20)
)
if mibBuilder.loadTexts:
    eqlLocalIOCountsTable.setStatus("current")
_EqlLocalIOCountsEntry_Object = MibTableRow
eqlLocalIOCountsEntry = _EqlLocalIOCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20, 1)
)
eqlLocalIOCountsEntry.setIndexNames(
    (0, "EQLVOLBALANCER-MIB", "eqlLocalIOCountsIndex"),
)
if mibBuilder.loadTexts:
    eqlLocalIOCountsEntry.setStatus("current")
_EqlLocalIOCountsIndex_Type = Unsigned32
_EqlLocalIOCountsIndex_Object = MibTableColumn
eqlLocalIOCountsIndex = _EqlLocalIOCountsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20, 1, 1),
    _EqlLocalIOCountsIndex_Type()
)
eqlLocalIOCountsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLocalIOCountsIndex.setStatus("current")
_EqlLocalIOCountsTimestamp_Type = Counter32
_EqlLocalIOCountsTimestamp_Object = MibTableColumn
eqlLocalIOCountsTimestamp = _EqlLocalIOCountsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20, 1, 2),
    _EqlLocalIOCountsTimestamp_Type()
)
eqlLocalIOCountsTimestamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLocalIOCountsTimestamp.setStatus("current")
_EqlLocalIOCountsReads_Type = Counter64
_EqlLocalIOCountsReads_Object = MibTableColumn
eqlLocalIOCountsReads = _EqlLocalIOCountsReads_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20, 1, 3),
    _EqlLocalIOCountsReads_Type()
)
eqlLocalIOCountsReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLocalIOCountsReads.setStatus("current")
_EqlLocalIOCountsReadBytes_Type = Counter64
_EqlLocalIOCountsReadBytes_Object = MibTableColumn
eqlLocalIOCountsReadBytes = _EqlLocalIOCountsReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20, 1, 4),
    _EqlLocalIOCountsReadBytes_Type()
)
eqlLocalIOCountsReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLocalIOCountsReadBytes.setStatus("current")
_EqlLocalIOCountsReadLatencyMs_Type = Counter64
_EqlLocalIOCountsReadLatencyMs_Object = MibTableColumn
eqlLocalIOCountsReadLatencyMs = _EqlLocalIOCountsReadLatencyMs_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20, 1, 5),
    _EqlLocalIOCountsReadLatencyMs_Type()
)
eqlLocalIOCountsReadLatencyMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLocalIOCountsReadLatencyMs.setStatus("current")
_EqlLocalIOCountsWrites_Type = Counter64
_EqlLocalIOCountsWrites_Object = MibTableColumn
eqlLocalIOCountsWrites = _EqlLocalIOCountsWrites_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20, 1, 6),
    _EqlLocalIOCountsWrites_Type()
)
eqlLocalIOCountsWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLocalIOCountsWrites.setStatus("current")
_EqlLocalIOCountsWriteBytes_Type = Counter64
_EqlLocalIOCountsWriteBytes_Object = MibTableColumn
eqlLocalIOCountsWriteBytes = _EqlLocalIOCountsWriteBytes_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20, 1, 7),
    _EqlLocalIOCountsWriteBytes_Type()
)
eqlLocalIOCountsWriteBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLocalIOCountsWriteBytes.setStatus("current")
_EqlLocalIOCountsWriteLatencyMs_Type = Counter64
_EqlLocalIOCountsWriteLatencyMs_Object = MibTableColumn
eqlLocalIOCountsWriteLatencyMs = _EqlLocalIOCountsWriteLatencyMs_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20, 1, 8),
    _EqlLocalIOCountsWriteLatencyMs_Type()
)
eqlLocalIOCountsWriteLatencyMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLocalIOCountsWriteLatencyMs.setStatus("current")
_EqlLocalIOCountsHeadroomPercent_Type = Unsigned32
_EqlLocalIOCountsHeadroomPercent_Object = MibTableColumn
eqlLocalIOCountsHeadroomPercent = _EqlLocalIOCountsHeadroomPercent_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20, 1, 9),
    _EqlLocalIOCountsHeadroomPercent_Type()
)
eqlLocalIOCountsHeadroomPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLocalIOCountsHeadroomPercent.setStatus("current")
_EqlLocalIOCountsWorstQueuingLatencyMs_Type = Counter64
_EqlLocalIOCountsWorstQueuingLatencyMs_Object = MibTableColumn
eqlLocalIOCountsWorstQueuingLatencyMs = _EqlLocalIOCountsWorstQueuingLatencyMs_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 20, 1, 10),
    _EqlLocalIOCountsWorstQueuingLatencyMs_Type()
)
eqlLocalIOCountsWorstQueuingLatencyMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLocalIOCountsWorstQueuingLatencyMs.setStatus("current")
_EqlPlanAUSTable_Object = MibTable
eqlPlanAUSTable = _EqlPlanAUSTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 21)
)
if mibBuilder.loadTexts:
    eqlPlanAUSTable.setStatus("current")
_EqlPlanAUSEntry_Object = MibTableRow
eqlPlanAUSEntry = _EqlPlanAUSEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 21, 1)
)
eqlPlanAUSEntry.setIndexNames(
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlVolBalPlanIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
)
if mibBuilder.loadTexts:
    eqlPlanAUSEntry.setStatus("current")
_EqlPlanAUSCount_Type = Unsigned32
_EqlPlanAUSCount_Object = MibTableColumn
eqlPlanAUSCount = _EqlPlanAUSCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 21, 1, 1),
    _EqlPlanAUSCount_Type()
)
eqlPlanAUSCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPlanAUSCount.setStatus("current")


class _EqlPlanAUSArray_Type(OctetString):
    """Custom type eqlPlanAUSArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1024, 1024),
    )


_EqlPlanAUSArray_Type.__name__ = "OctetString"
_EqlPlanAUSArray_Object = MibTableColumn
eqlPlanAUSArray = _EqlPlanAUSArray_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 21, 1, 2),
    _EqlPlanAUSArray_Type()
)
eqlPlanAUSArray.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPlanAUSArray.setStatus("current")
_EqlTaskLocalPickedPagesTable_Object = MibTable
eqlTaskLocalPickedPagesTable = _EqlTaskLocalPickedPagesTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 22)
)
if mibBuilder.loadTexts:
    eqlTaskLocalPickedPagesTable.setStatus("current")
_EqlTaskLocalPickedPagesEntry_Object = MibTableRow
eqlTaskLocalPickedPagesEntry = _EqlTaskLocalPickedPagesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 22, 1)
)
eqlTaskLocalPickedPagesEntry.setIndexNames(
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlVolBalPlanIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlVolBalTaskIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
)
if mibBuilder.loadTexts:
    eqlTaskLocalPickedPagesEntry.setStatus("current")
_EqlTaskLocalPickedProgress_Type = Counter64
_EqlTaskLocalPickedProgress_Object = MibTableColumn
eqlTaskLocalPickedProgress = _EqlTaskLocalPickedProgress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 22, 1, 1),
    _EqlTaskLocalPickedProgress_Type()
)
eqlTaskLocalPickedProgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlTaskLocalPickedProgress.setStatus("current")
_EqlTaskLocalPickedPagesCount_Type = Unsigned32
_EqlTaskLocalPickedPagesCount_Object = MibTableColumn
eqlTaskLocalPickedPagesCount = _EqlTaskLocalPickedPagesCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 22, 1, 2),
    _EqlTaskLocalPickedPagesCount_Type()
)
eqlTaskLocalPickedPagesCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlTaskLocalPickedPagesCount.setStatus("current")


class _EqlTaskLocalPickedPagesContext_Type(OctetString):
    """Custom type eqlTaskLocalPickedPagesContext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EqlTaskLocalPickedPagesContext_Type.__name__ = "OctetString"
_EqlTaskLocalPickedPagesContext_Object = MibTableColumn
eqlTaskLocalPickedPagesContext = _EqlTaskLocalPickedPagesContext_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 22, 1, 3),
    _EqlTaskLocalPickedPagesContext_Type()
)
eqlTaskLocalPickedPagesContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlTaskLocalPickedPagesContext.setStatus("current")
_EqlTaskLocalPickedPagesRev_Type = Unsigned32
_EqlTaskLocalPickedPagesRev_Object = MibTableColumn
eqlTaskLocalPickedPagesRev = _EqlTaskLocalPickedPagesRev_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 22, 1, 4),
    _EqlTaskLocalPickedPagesRev_Type()
)
eqlTaskLocalPickedPagesRev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlTaskLocalPickedPagesRev.setStatus("current")
_EqlTaskLocalPickedPagesFlags_Type = Unsigned32
_EqlTaskLocalPickedPagesFlags_Object = MibTableColumn
eqlTaskLocalPickedPagesFlags = _EqlTaskLocalPickedPagesFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 22, 1, 5),
    _EqlTaskLocalPickedPagesFlags_Type()
)
eqlTaskLocalPickedPagesFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlTaskLocalPickedPagesFlags.setStatus("current")
_EqlTaskLocalPickedPagesEntryStatus_Type = RowStatus
_EqlTaskLocalPickedPagesEntryStatus_Object = MibTableColumn
eqlTaskLocalPickedPagesEntryStatus = _EqlTaskLocalPickedPagesEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 22, 1, 6),
    _EqlTaskLocalPickedPagesEntryStatus_Type()
)
eqlTaskLocalPickedPagesEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlTaskLocalPickedPagesEntryStatus.setStatus("current")


class _EqlTaskLocalPickedPagesArray_Type(OctetString):
    """Custom type eqlTaskLocalPickedPagesArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1200, 1200),
    )


_EqlTaskLocalPickedPagesArray_Type.__name__ = "OctetString"
_EqlTaskLocalPickedPagesArray_Object = MibTableColumn
eqlTaskLocalPickedPagesArray = _EqlTaskLocalPickedPagesArray_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 22, 1, 7),
    _EqlTaskLocalPickedPagesArray_Type()
)
eqlTaskLocalPickedPagesArray.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlTaskLocalPickedPagesArray.setStatus("current")
_EqlTaskLocalPickedPagesAllocatedProgress_Type = Counter64
_EqlTaskLocalPickedPagesAllocatedProgress_Object = MibTableColumn
eqlTaskLocalPickedPagesAllocatedProgress = _EqlTaskLocalPickedPagesAllocatedProgress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 22, 1, 8),
    _EqlTaskLocalPickedPagesAllocatedProgress_Type()
)
eqlTaskLocalPickedPagesAllocatedProgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlTaskLocalPickedPagesAllocatedProgress.setStatus("current")


class _EqlTaskLocalPickedPagesStatus_Type(Integer32):
    """Custom type eqlTaskLocalPickedPagesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("finished", 2),
          ("started", 1))
    )


_EqlTaskLocalPickedPagesStatus_Type.__name__ = "Integer32"
_EqlTaskLocalPickedPagesStatus_Object = MibTableColumn
eqlTaskLocalPickedPagesStatus = _EqlTaskLocalPickedPagesStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 22, 1, 9),
    _EqlTaskLocalPickedPagesStatus_Type()
)
eqlTaskLocalPickedPagesStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlTaskLocalPickedPagesStatus.setStatus("current")
_EqlMemberCountersTable_Object = MibTable
eqlMemberCountersTable = _EqlMemberCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23)
)
if mibBuilder.loadTexts:
    eqlMemberCountersTable.setStatus("current")
_EqlMemberCountersEntry_Object = MibTableRow
eqlMemberCountersEntry = _EqlMemberCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1)
)
eqlMemberCountersEntry.setIndexNames(
    (0, "EQLVOLBALANCER-MIB", "eqlMemberCountersIndex"),
)
if mibBuilder.loadTexts:
    eqlMemberCountersEntry.setStatus("current")
_EqlMemberCountersIndex_Type = Unsigned32
_EqlMemberCountersIndex_Object = MibTableColumn
eqlMemberCountersIndex = _EqlMemberCountersIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1, 1),
    _EqlMemberCountersIndex_Type()
)
eqlMemberCountersIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberCountersIndex.setStatus("current")


class _EqlMemberCountersUuid_Type(OctetString):
    """Custom type eqlMemberCountersUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlMemberCountersUuid_Type.__name__ = "OctetString"
_EqlMemberCountersUuid_Object = MibTableColumn
eqlMemberCountersUuid = _EqlMemberCountersUuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1, 2),
    _EqlMemberCountersUuid_Type()
)
eqlMemberCountersUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCountersUuid.setStatus("current")
_EqlMemberCountersTimeStamp_Type = Counter32
_EqlMemberCountersTimeStamp_Object = MibTableColumn
eqlMemberCountersTimeStamp = _EqlMemberCountersTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1, 3),
    _EqlMemberCountersTimeStamp_Type()
)
eqlMemberCountersTimeStamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlMemberCountersTimeStamp.setStatus("current")
_EqlMemberCountersAddedPages_Type = Counter64
_EqlMemberCountersAddedPages_Object = MibTableColumn
eqlMemberCountersAddedPages = _EqlMemberCountersAddedPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1, 4),
    _EqlMemberCountersAddedPages_Type()
)
eqlMemberCountersAddedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCountersAddedPages.setStatus("current")
_EqlMemberCountersRemovedPages_Type = Counter64
_EqlMemberCountersRemovedPages_Object = MibTableColumn
eqlMemberCountersRemovedPages = _EqlMemberCountersRemovedPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1, 5),
    _EqlMemberCountersRemovedPages_Type()
)
eqlMemberCountersRemovedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCountersRemovedPages.setStatus("current")
_EqlMemberCountersAddedAllocatedPages_Type = Counter64
_EqlMemberCountersAddedAllocatedPages_Object = MibTableColumn
eqlMemberCountersAddedAllocatedPages = _EqlMemberCountersAddedAllocatedPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1, 6),
    _EqlMemberCountersAddedAllocatedPages_Type()
)
eqlMemberCountersAddedAllocatedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCountersAddedAllocatedPages.setStatus("current")
_EqlMemberCountersRemovedAllocatedPages_Type = Counter64
_EqlMemberCountersRemovedAllocatedPages_Object = MibTableColumn
eqlMemberCountersRemovedAllocatedPages = _EqlMemberCountersRemovedAllocatedPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1, 7),
    _EqlMemberCountersRemovedAllocatedPages_Type()
)
eqlMemberCountersRemovedAllocatedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCountersRemovedAllocatedPages.setStatus("current")
_EqlMemberCountersAddedHotPages_Type = Counter64
_EqlMemberCountersAddedHotPages_Object = MibTableColumn
eqlMemberCountersAddedHotPages = _EqlMemberCountersAddedHotPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1, 8),
    _EqlMemberCountersAddedHotPages_Type()
)
eqlMemberCountersAddedHotPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCountersAddedHotPages.setStatus("current")
_EqlMemberCountersRemovedHotPages_Type = Counter64
_EqlMemberCountersRemovedHotPages_Object = MibTableColumn
eqlMemberCountersRemovedHotPages = _EqlMemberCountersRemovedHotPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1, 9),
    _EqlMemberCountersRemovedHotPages_Type()
)
eqlMemberCountersRemovedHotPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCountersRemovedHotPages.setStatus("current")
_EqlMemberCountersAddedColdPages_Type = Counter64
_EqlMemberCountersAddedColdPages_Object = MibTableColumn
eqlMemberCountersAddedColdPages = _EqlMemberCountersAddedColdPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1, 10),
    _EqlMemberCountersAddedColdPages_Type()
)
eqlMemberCountersAddedColdPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCountersAddedColdPages.setStatus("current")
_EqlMemberCountersRemovedColdPages_Type = Counter64
_EqlMemberCountersRemovedColdPages_Object = MibTableColumn
eqlMemberCountersRemovedColdPages = _EqlMemberCountersRemovedColdPages_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 23, 1, 11),
    _EqlMemberCountersRemovedColdPages_Type()
)
eqlMemberCountersRemovedColdPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMemberCountersRemovedColdPages.setStatus("current")
_EqlArchiveTaskTable_Object = MibTable
eqlArchiveTaskTable = _EqlArchiveTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24)
)
if mibBuilder.loadTexts:
    eqlArchiveTaskTable.setStatus("current")
_EqlArchiveTaskEntry_Object = MibTableRow
eqlArchiveTaskEntry = _EqlArchiveTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1)
)
eqlArchiveTaskEntry.setIndexNames(
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlVolBalPlanIndex"),
    (0, "EQLVOLBALANCER-MIB", "eqlArchiveTaskIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
)
if mibBuilder.loadTexts:
    eqlArchiveTaskEntry.setStatus("current")
_EqlArchiveTaskIndex_Type = Unsigned32
_EqlArchiveTaskIndex_Object = MibTableColumn
eqlArchiveTaskIndex = _EqlArchiveTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 1),
    _EqlArchiveTaskIndex_Type()
)
eqlArchiveTaskIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskIndex.setStatus("current")
_EqlArchiveTaskMemberCount_Type = Unsigned32
_EqlArchiveTaskMemberCount_Object = MibTableColumn
eqlArchiveTaskMemberCount = _EqlArchiveTaskMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 2),
    _EqlArchiveTaskMemberCount_Type()
)
eqlArchiveTaskMemberCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMemberCount.setStatus("current")


class _EqlArchiveTaskType_Type(Integer32):
    """Custom type eqlArchiveTaskType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("compression", 1)
    )


_EqlArchiveTaskType_Type.__name__ = "Integer32"
_EqlArchiveTaskType_Object = MibTableColumn
eqlArchiveTaskType = _EqlArchiveTaskType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 3),
    _EqlArchiveTaskType_Type()
)
eqlArchiveTaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskType.setStatus("current")


class _EqlArchiveTaskState_Type(Integer32):
    """Custom type eqlArchiveTaskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("ready", 1))
    )


_EqlArchiveTaskState_Type.__name__ = "Integer32"
_EqlArchiveTaskState_Object = MibTableColumn
eqlArchiveTaskState = _EqlArchiveTaskState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 4),
    _EqlArchiveTaskState_Type()
)
eqlArchiveTaskState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskState.setStatus("current")
_EqlArchiveTaskEntryStatus_Type = RowStatus
_EqlArchiveTaskEntryStatus_Object = MibTableColumn
eqlArchiveTaskEntryStatus = _EqlArchiveTaskEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 5),
    _EqlArchiveTaskEntryStatus_Type()
)
eqlArchiveTaskEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskEntryStatus.setStatus("current")


class _EqlArchiveTaskMember1Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember1Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember1Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember1Uuid_Object = MibTableColumn
eqlArchiveTaskMember1Uuid = _EqlArchiveTaskMember1Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 6),
    _EqlArchiveTaskMember1Uuid_Type()
)
eqlArchiveTaskMember1Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember1Uuid.setStatus("current")
_EqlArchiveTaskMember1Flags_Type = Unsigned32
_EqlArchiveTaskMember1Flags_Object = MibTableColumn
eqlArchiveTaskMember1Flags = _EqlArchiveTaskMember1Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 7),
    _EqlArchiveTaskMember1Flags_Type()
)
eqlArchiveTaskMember1Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember1Flags.setStatus("current")


class _EqlArchiveTaskMember2Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember2Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember2Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember2Uuid_Object = MibTableColumn
eqlArchiveTaskMember2Uuid = _EqlArchiveTaskMember2Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 8),
    _EqlArchiveTaskMember2Uuid_Type()
)
eqlArchiveTaskMember2Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember2Uuid.setStatus("current")
_EqlArchiveTaskMember2Flags_Type = Unsigned32
_EqlArchiveTaskMember2Flags_Object = MibTableColumn
eqlArchiveTaskMember2Flags = _EqlArchiveTaskMember2Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 9),
    _EqlArchiveTaskMember2Flags_Type()
)
eqlArchiveTaskMember2Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember2Flags.setStatus("current")


class _EqlArchiveTaskMember3Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember3Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember3Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember3Uuid_Object = MibTableColumn
eqlArchiveTaskMember3Uuid = _EqlArchiveTaskMember3Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 10),
    _EqlArchiveTaskMember3Uuid_Type()
)
eqlArchiveTaskMember3Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember3Uuid.setStatus("current")
_EqlArchiveTaskMember3Flags_Type = Unsigned32
_EqlArchiveTaskMember3Flags_Object = MibTableColumn
eqlArchiveTaskMember3Flags = _EqlArchiveTaskMember3Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 11),
    _EqlArchiveTaskMember3Flags_Type()
)
eqlArchiveTaskMember3Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember3Flags.setStatus("current")


class _EqlArchiveTaskMember4Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember4Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember4Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember4Uuid_Object = MibTableColumn
eqlArchiveTaskMember4Uuid = _EqlArchiveTaskMember4Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 12),
    _EqlArchiveTaskMember4Uuid_Type()
)
eqlArchiveTaskMember4Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember4Uuid.setStatus("current")
_EqlArchiveTaskMember4Flags_Type = Unsigned32
_EqlArchiveTaskMember4Flags_Object = MibTableColumn
eqlArchiveTaskMember4Flags = _EqlArchiveTaskMember4Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 13),
    _EqlArchiveTaskMember4Flags_Type()
)
eqlArchiveTaskMember4Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember4Flags.setStatus("current")


class _EqlArchiveTaskMember5Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember5Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember5Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember5Uuid_Object = MibTableColumn
eqlArchiveTaskMember5Uuid = _EqlArchiveTaskMember5Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 14),
    _EqlArchiveTaskMember5Uuid_Type()
)
eqlArchiveTaskMember5Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember5Uuid.setStatus("current")
_EqlArchiveTaskMember5Flags_Type = Unsigned32
_EqlArchiveTaskMember5Flags_Object = MibTableColumn
eqlArchiveTaskMember5Flags = _EqlArchiveTaskMember5Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 15),
    _EqlArchiveTaskMember5Flags_Type()
)
eqlArchiveTaskMember5Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember5Flags.setStatus("current")


class _EqlArchiveTaskMember6Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember6Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember6Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember6Uuid_Object = MibTableColumn
eqlArchiveTaskMember6Uuid = _EqlArchiveTaskMember6Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 16),
    _EqlArchiveTaskMember6Uuid_Type()
)
eqlArchiveTaskMember6Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember6Uuid.setStatus("current")
_EqlArchiveTaskMember6Flags_Type = Unsigned32
_EqlArchiveTaskMember6Flags_Object = MibTableColumn
eqlArchiveTaskMember6Flags = _EqlArchiveTaskMember6Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 17),
    _EqlArchiveTaskMember6Flags_Type()
)
eqlArchiveTaskMember6Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember6Flags.setStatus("current")


class _EqlArchiveTaskMember7Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember7Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember7Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember7Uuid_Object = MibTableColumn
eqlArchiveTaskMember7Uuid = _EqlArchiveTaskMember7Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 18),
    _EqlArchiveTaskMember7Uuid_Type()
)
eqlArchiveTaskMember7Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember7Uuid.setStatus("current")
_EqlArchiveTaskMember7Flags_Type = Unsigned32
_EqlArchiveTaskMember7Flags_Object = MibTableColumn
eqlArchiveTaskMember7Flags = _EqlArchiveTaskMember7Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 19),
    _EqlArchiveTaskMember7Flags_Type()
)
eqlArchiveTaskMember7Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember7Flags.setStatus("current")


class _EqlArchiveTaskMember8Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember8Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember8Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember8Uuid_Object = MibTableColumn
eqlArchiveTaskMember8Uuid = _EqlArchiveTaskMember8Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 20),
    _EqlArchiveTaskMember8Uuid_Type()
)
eqlArchiveTaskMember8Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember8Uuid.setStatus("current")
_EqlArchiveTaskMember8Flags_Type = Unsigned32
_EqlArchiveTaskMember8Flags_Object = MibTableColumn
eqlArchiveTaskMember8Flags = _EqlArchiveTaskMember8Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 21),
    _EqlArchiveTaskMember8Flags_Type()
)
eqlArchiveTaskMember8Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember8Flags.setStatus("current")


class _EqlArchiveTaskMember9Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember9Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember9Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember9Uuid_Object = MibTableColumn
eqlArchiveTaskMember9Uuid = _EqlArchiveTaskMember9Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 22),
    _EqlArchiveTaskMember9Uuid_Type()
)
eqlArchiveTaskMember9Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember9Uuid.setStatus("current")
_EqlArchiveTaskMember9Flags_Type = Unsigned32
_EqlArchiveTaskMember9Flags_Object = MibTableColumn
eqlArchiveTaskMember9Flags = _EqlArchiveTaskMember9Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 23),
    _EqlArchiveTaskMember9Flags_Type()
)
eqlArchiveTaskMember9Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember9Flags.setStatus("current")


class _EqlArchiveTaskMember10Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember10Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember10Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember10Uuid_Object = MibTableColumn
eqlArchiveTaskMember10Uuid = _EqlArchiveTaskMember10Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 24),
    _EqlArchiveTaskMember10Uuid_Type()
)
eqlArchiveTaskMember10Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember10Uuid.setStatus("current")
_EqlArchiveTaskMember10Flags_Type = Unsigned32
_EqlArchiveTaskMember10Flags_Object = MibTableColumn
eqlArchiveTaskMember10Flags = _EqlArchiveTaskMember10Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 25),
    _EqlArchiveTaskMember10Flags_Type()
)
eqlArchiveTaskMember10Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember10Flags.setStatus("current")


class _EqlArchiveTaskMember11Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember11Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember11Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember11Uuid_Object = MibTableColumn
eqlArchiveTaskMember11Uuid = _EqlArchiveTaskMember11Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 26),
    _EqlArchiveTaskMember11Uuid_Type()
)
eqlArchiveTaskMember11Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember11Uuid.setStatus("current")
_EqlArchiveTaskMember11Flags_Type = Unsigned32
_EqlArchiveTaskMember11Flags_Object = MibTableColumn
eqlArchiveTaskMember11Flags = _EqlArchiveTaskMember11Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 27),
    _EqlArchiveTaskMember11Flags_Type()
)
eqlArchiveTaskMember11Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember11Flags.setStatus("current")


class _EqlArchiveTaskMember12Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember12Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember12Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember12Uuid_Object = MibTableColumn
eqlArchiveTaskMember12Uuid = _EqlArchiveTaskMember12Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 28),
    _EqlArchiveTaskMember12Uuid_Type()
)
eqlArchiveTaskMember12Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember12Uuid.setStatus("current")
_EqlArchiveTaskMember12Flags_Type = Unsigned32
_EqlArchiveTaskMember12Flags_Object = MibTableColumn
eqlArchiveTaskMember12Flags = _EqlArchiveTaskMember12Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 29),
    _EqlArchiveTaskMember12Flags_Type()
)
eqlArchiveTaskMember12Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember12Flags.setStatus("current")


class _EqlArchiveTaskMember13Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember13Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember13Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember13Uuid_Object = MibTableColumn
eqlArchiveTaskMember13Uuid = _EqlArchiveTaskMember13Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 30),
    _EqlArchiveTaskMember13Uuid_Type()
)
eqlArchiveTaskMember13Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember13Uuid.setStatus("current")
_EqlArchiveTaskMember13Flags_Type = Unsigned32
_EqlArchiveTaskMember13Flags_Object = MibTableColumn
eqlArchiveTaskMember13Flags = _EqlArchiveTaskMember13Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 31),
    _EqlArchiveTaskMember13Flags_Type()
)
eqlArchiveTaskMember13Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember13Flags.setStatus("current")


class _EqlArchiveTaskMember14Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember14Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember14Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember14Uuid_Object = MibTableColumn
eqlArchiveTaskMember14Uuid = _EqlArchiveTaskMember14Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 32),
    _EqlArchiveTaskMember14Uuid_Type()
)
eqlArchiveTaskMember14Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember14Uuid.setStatus("current")
_EqlArchiveTaskMember14Flags_Type = Unsigned32
_EqlArchiveTaskMember14Flags_Object = MibTableColumn
eqlArchiveTaskMember14Flags = _EqlArchiveTaskMember14Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 33),
    _EqlArchiveTaskMember14Flags_Type()
)
eqlArchiveTaskMember14Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember14Flags.setStatus("current")


class _EqlArchiveTaskMember15Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember15Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember15Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember15Uuid_Object = MibTableColumn
eqlArchiveTaskMember15Uuid = _EqlArchiveTaskMember15Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 34),
    _EqlArchiveTaskMember15Uuid_Type()
)
eqlArchiveTaskMember15Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember15Uuid.setStatus("current")
_EqlArchiveTaskMember15Flags_Type = Unsigned32
_EqlArchiveTaskMember15Flags_Object = MibTableColumn
eqlArchiveTaskMember15Flags = _EqlArchiveTaskMember15Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 35),
    _EqlArchiveTaskMember15Flags_Type()
)
eqlArchiveTaskMember15Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember15Flags.setStatus("current")


class _EqlArchiveTaskMember16Uuid_Type(OctetString):
    """Custom type eqlArchiveTaskMember16Uuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlArchiveTaskMember16Uuid_Type.__name__ = "OctetString"
_EqlArchiveTaskMember16Uuid_Object = MibTableColumn
eqlArchiveTaskMember16Uuid = _EqlArchiveTaskMember16Uuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 36),
    _EqlArchiveTaskMember16Uuid_Type()
)
eqlArchiveTaskMember16Uuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember16Uuid.setStatus("current")
_EqlArchiveTaskMember16Flags_Type = Unsigned32
_EqlArchiveTaskMember16Flags_Object = MibTableColumn
eqlArchiveTaskMember16Flags = _EqlArchiveTaskMember16Flags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 14, 1, 24, 1, 37),
    _EqlArchiveTaskMember16Flags_Type()
)
eqlArchiveTaskMember16Flags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlArchiveTaskMember16Flags.setStatus("current")
_EqlvolbalancerNotifications_ObjectIdentity = ObjectIdentity
eqlvolbalancerNotifications = _EqlvolbalancerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 14, 2)
)
_EqlvolbalancerConformance_ObjectIdentity = ObjectIdentity
eqlvolbalancerConformance = _EqlvolbalancerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 14, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLVOLBALANCER-MIB",
    **{"eqlvolbalancerModule": eqlvolbalancerModule,
       "eqlvolbalancerObjects": eqlvolbalancerObjects,
       "eqlvolbalancerConfigGroup": eqlvolbalancerConfigGroup,
       "eqlvolbalancerConfigVolSliceCostFreq": eqlvolbalancerConfigVolSliceCostFreq,
       "eqlvolbalancerConfigVolSliceRollupTime": eqlvolbalancerConfigVolSliceRollupTime,
       "eqlvolbalancerVolumeSliceCostTable": eqlvolbalancerVolumeSliceCostTable,
       "eqlvolbalancerVolumeSliceCostEntry": eqlvolbalancerVolumeSliceCostEntry,
       "eqlvolbalancerVolumeSliceCostPsaId": eqlvolbalancerVolumeSliceCostPsaId,
       "eqlvolbalancerVolumeSliceCostTime": eqlvolbalancerVolumeSliceCostTime,
       "eqlvolbalancerVolumeSliceCostVolumeId": eqlvolbalancerVolumeSliceCostVolumeId,
       "eqlvolbalancerVolumeSliceCostCost": eqlvolbalancerVolumeSliceCostCost,
       "eqlvolbalancerVolumeSliceCostStatus": eqlvolbalancerVolumeSliceCostStatus,
       "eqlvolbalancerDailyVolumeCostTable": eqlvolbalancerDailyVolumeCostTable,
       "eqlvolbalancerDailyVolumeCostEntry": eqlvolbalancerDailyVolumeCostEntry,
       "eqlvolbalancerDailyVolumeCostDay": eqlvolbalancerDailyVolumeCostDay,
       "eqlvolbalancerDailyVolumeCostVolumeId": eqlvolbalancerDailyVolumeCostVolumeId,
       "eqlvolbalancerDailyVolumeCostCost": eqlvolbalancerDailyVolumeCostCost,
       "eqlvolbalancerDailyVolumeCostStatus": eqlvolbalancerDailyVolumeCostStatus,
       "eqlvolbalancerRecommendationTable": eqlvolbalancerRecommendationTable,
       "eqlvolbalancerRecommendationEntry": eqlvolbalancerRecommendationEntry,
       "eqlvolbalancerRecommendationTime": eqlvolbalancerRecommendationTime,
       "eqlvolbalancerRecommendationVolumeId": eqlvolbalancerRecommendationVolumeId,
       "eqlvolbalancerRecommendationSrcPsaId": eqlvolbalancerRecommendationSrcPsaId,
       "eqlvolbalancerRecommendationDstPsaId": eqlvolbalancerRecommendationDstPsaId,
       "eqlvolbalancerRecommendationComplete": eqlvolbalancerRecommendationComplete,
       "eqlvolbalancerRecommendationStatus": eqlvolbalancerRecommendationStatus,
       "eqlVolBalConfigTable": eqlVolBalConfigTable,
       "eqlVolBalConfigEntry": eqlVolBalConfigEntry,
       "eqlVolBalConfigLastPlanIndex": eqlVolBalConfigLastPlanIndex,
       "eqlVolBalConfigEnabled": eqlVolBalConfigEnabled,
       "eqlVolBalConfigSenseFrequency": eqlVolBalConfigSenseFrequency,
       "eqlVolBalConfigImbalDetectFrequency": eqlVolBalConfigImbalDetectFrequency,
       "eqlVolBalConfigVolumeDelFrequency": eqlVolBalConfigVolumeDelFrequency,
       "eqlVolBalConfigVolumeBindFrequency": eqlVolBalConfigVolumeBindFrequency,
       "eqlVolBalConfigRAIDSetFreeSpaceTroubleDelay": eqlVolBalConfigRAIDSetFreeSpaceTroubleDelay,
       "eqlVolBalConfigRAIDSetDeleteDelay": eqlVolBalConfigRAIDSetDeleteDelay,
       "eqlVolBalConfigRAIDSetJoinDelay": eqlVolBalConfigRAIDSetJoinDelay,
       "eqlVolBalConfigReamSize": eqlVolBalConfigReamSize,
       "eqlVolBalConfigHistoryRowMax": eqlVolBalConfigHistoryRowMax,
       "eqlVolBalConfigRAIDStatsRowMax": eqlVolBalConfigRAIDStatsRowMax,
       "eqlVolBalConfigPoolThroughputRateMax": eqlVolBalConfigPoolThroughputRateMax,
       "eqlVolBalConfigMinSpreadSize": eqlVolBalConfigMinSpreadSize,
       "eqlVolBalConfigPlacementThreshold": eqlVolBalConfigPlacementThreshold,
       "eqlVolBalConfigPreviousLeadUUID": eqlVolBalConfigPreviousLeadUUID,
       "eqlVolBalConfigFlags": eqlVolBalConfigFlags,
       "eqlVolBalConfigArchivalPlacementThreshold": eqlVolBalConfigArchivalPlacementThreshold,
       "eqlVolBalConfigFreeSpaceTroubleEnabled": eqlVolBalConfigFreeSpaceTroubleEnabled,
       "eqlVolBalConfigPreferAutoRAIDPlacement": eqlVolBalConfigPreferAutoRAIDPlacement,
       "eqlVolBalConfigHotColdPageSwapEnabled": eqlVolBalConfigHotColdPageSwapEnabled,
       "eqlVolBalConfigArchiveEnabled": eqlVolBalConfigArchiveEnabled,
       "eqlVolBalPlanTable": eqlVolBalPlanTable,
       "eqlVolBalPlanEntry": eqlVolBalPlanEntry,
       "eqlVolBalPlanIndex": eqlVolBalPlanIndex,
       "eqlVolBalPlanReason": eqlVolBalPlanReason,
       "eqlVolBalPlanComplete": eqlVolBalPlanComplete,
       "eqlVolBalPlanStartTime": eqlVolBalPlanStartTime,
       "eqlVolBalPlanEndTime": eqlVolBalPlanEndTime,
       "eqlVolBalPlanState": eqlVolBalPlanState,
       "eqlVolBalPlanVacatingMemberUUID": eqlVolBalPlanVacatingMemberUUID,
       "eqlVolBalPlanTotalPages": eqlVolBalPlanTotalPages,
       "eqlVolBalPlanEntryStatus": eqlVolBalPlanEntryStatus,
       "eqlVolBalPlanFlags": eqlVolBalPlanFlags,
       "eqlVolBalPlanTotalAllocatedPages": eqlVolBalPlanTotalAllocatedPages,
       "eqlVolBalPlanAllocatedPagesMoved": eqlVolBalPlanAllocatedPagesMoved,
       "eqlVolBalPlanAssignedPagesMoved": eqlVolBalPlanAssignedPagesMoved,
       "eqlVolBalPlanHistoryTableIndex": eqlVolBalPlanHistoryTableIndex,
       "eqlVolBalPlanHistoryTableMemberIndex": eqlVolBalPlanHistoryTableMemberIndex,
       "eqlVolBalPlanHistoryTableMemberCount": eqlVolBalPlanHistoryTableMemberCount,
       "eqlVolBalPlanFirstAlternateDst": eqlVolBalPlanFirstAlternateDst,
       "eqlVolBalPlanSecondAlternateDst": eqlVolBalPlanSecondAlternateDst,
       "eqlVolBalPlanTotalSnapPages": eqlVolBalPlanTotalSnapPages,
       "eqlVolBalPlanSnapPagesMoved": eqlVolBalPlanSnapPagesMoved,
       "eqlVolBalTaskTable": eqlVolBalTaskTable,
       "eqlVolBalTaskEntry": eqlVolBalTaskEntry,
       "eqlVolBalTaskIndex": eqlVolBalTaskIndex,
       "eqlVolBalTaskVolumePsvId": eqlVolBalTaskVolumePsvId,
       "eqlVolBalTaskSrcDriveGroup": eqlVolBalTaskSrcDriveGroup,
       "eqlVolBalTaskSrcName": eqlVolBalTaskSrcName,
       "eqlVolBalTaskDstDriveGroup": eqlVolBalTaskDstDriveGroup,
       "eqlVolBalTaskDstName": eqlVolBalTaskDstName,
       "eqlVolBalTaskSrcInitialPageCount": eqlVolBalTaskSrcInitialPageCount,
       "eqlVolBalTaskNumPages": eqlVolBalTaskNumPages,
       "eqlVolBalTaskCoordinateWith": eqlVolBalTaskCoordinateWith,
       "eqlVolBalTaskType": eqlVolBalTaskType,
       "eqlVolBalTaskState": eqlVolBalTaskState,
       "eqlVolBalTaskEntryStatus": eqlVolBalTaskEntryStatus,
       "eqlVolBalTaskVolLeader": eqlVolBalTaskVolLeader,
       "eqlVolBalTaskNumAllocatedPages": eqlVolBalTaskNumAllocatedPages,
       "eqlVolBalTaskNumSnapPages": eqlVolBalTaskNumSnapPages,
       "eqlVolBalTaskPickedPagesTable": eqlVolBalTaskPickedPagesTable,
       "eqlVolBalTaskPickedPagesEntry": eqlVolBalTaskPickedPagesEntry,
       "eqlVolBalTaskPickedProgress": eqlVolBalTaskPickedProgress,
       "eqlVolBalTaskPickedPagesCount": eqlVolBalTaskPickedPagesCount,
       "eqlVolBalTaskPickedPagesContext": eqlVolBalTaskPickedPagesContext,
       "eqlVolBalTaskPickedPagesRev": eqlVolBalTaskPickedPagesRev,
       "eqlVolBalTaskPickedPagesFlags": eqlVolBalTaskPickedPagesFlags,
       "eqlVolBalTaskPickedPagesEntryStatus": eqlVolBalTaskPickedPagesEntryStatus,
       "eqlVolBalTaskPickedPagesArray": eqlVolBalTaskPickedPagesArray,
       "eqlVolBalTaskPickedPagesAllocatedProgress": eqlVolBalTaskPickedPagesAllocatedProgress,
       "eqlVolBalSliceStatsTable": eqlVolBalSliceStatsTable,
       "eqlVolBalSliceStatsEntry": eqlVolBalSliceStatsEntry,
       "eqlVolBalSliceMemberUUID": eqlVolBalSliceMemberUUID,
       "eqlVolBalSliceVolumeUUID": eqlVolBalSliceVolumeUUID,
       "eqlVolBalSliceTimeStamp": eqlVolBalSliceTimeStamp,
       "eqlVolBalSliceStatsRndRdRate": eqlVolBalSliceStatsRndRdRate,
       "eqlVolBalSliceStatsRndWrRate": eqlVolBalSliceStatsRndWrRate,
       "eqlVolBalSliceStatsSeqRdRate": eqlVolBalSliceStatsSeqRdRate,
       "eqlVolBalSliceStatsSeqWrRate": eqlVolBalSliceStatsSeqWrRate,
       "eqlVolBalSliceStatsPlacementScore": eqlVolBalSliceStatsPlacementScore,
       "eqlVolBalMemberStatsTable": eqlVolBalMemberStatsTable,
       "eqlVolBalMemberStatsEntry": eqlVolBalMemberStatsEntry,
       "eqlVolBalMemberUUID": eqlVolBalMemberUUID,
       "eqlVolBalMemberTimeStamp": eqlVolBalMemberTimeStamp,
       "eqlVolBalMemberStatsAvgRespTime": eqlVolBalMemberStatsAvgRespTime,
       "eqlVolBalMemberStatsCPUUsage": eqlVolBalMemberStatsCPUUsage,
       "eqlVolBalMemberStatsFreeSpace": eqlVolBalMemberStatsFreeSpace,
       "eqlVolBalMemberStatsRndRdRate": eqlVolBalMemberStatsRndRdRate,
       "eqlVolBalMemberStatsRndWrRate": eqlVolBalMemberStatsRndWrRate,
       "eqlVolBalMemberStatsSeqRdRate": eqlVolBalMemberStatsSeqRdRate,
       "eqlVolBalMemberStatsSeqWrRate": eqlVolBalMemberStatsSeqWrRate,
       "eqlVolBalHistoryTable": eqlVolBalHistoryTable,
       "eqlVolBalHistoryEntry": eqlVolBalHistoryEntry,
       "eqlVolBalHistoryStop": eqlVolBalHistoryStop,
       "eqlVolBalHistoryStart": eqlVolBalHistoryStart,
       "eqlVolBalHistoryPagesMoved": eqlVolBalHistoryPagesMoved,
       "eqlVolBalHistoryMembersInvolved": eqlVolBalHistoryMembersInvolved,
       "eqlVolBalHistorySlicesInvolved": eqlVolBalHistorySlicesInvolved,
       "eqlVolBalHistoryBalanceReason": eqlVolBalHistoryBalanceReason,
       "eqlVolBalCommandTable": eqlVolBalCommandTable,
       "eqlVolBalCommandEntry": eqlVolBalCommandEntry,
       "eqlVolBalCommandIndex": eqlVolBalCommandIndex,
       "eqlVolBalCommandPlanIndex": eqlVolBalCommandPlanIndex,
       "eqlVolBalCommandReason": eqlVolBalCommandReason,
       "eqlVolBalCommandRunning": eqlVolBalCommandRunning,
       "eqlVolBalCommandCreateTime": eqlVolBalCommandCreateTime,
       "eqlVolBalCommandState": eqlVolBalCommandState,
       "eqlVolBalCommandMemberUUID": eqlVolBalCommandMemberUUID,
       "eqlVolBalCommandVolumeId": eqlVolBalCommandVolumeId,
       "eqlVolBalCommandFromPoolId": eqlVolBalCommandFromPoolId,
       "eqlVolBalCommandToPoolId": eqlVolBalCommandToPoolId,
       "eqlVolBalCommandEntryStatus": eqlVolBalCommandEntryStatus,
       "eqlVolBalCommandFlags": eqlVolBalCommandFlags,
       "eqlVolBalCommandSiteId": eqlVolBalCommandSiteId,
       "eqlPropertiesTable": eqlPropertiesTable,
       "eqlPropertiesEntry": eqlPropertiesEntry,
       "eqlPropertiesIndex": eqlPropertiesIndex,
       "eqlPropertiesName": eqlPropertiesName,
       "eqlPropertiesValue": eqlPropertiesValue,
       "eqlPageMoveHistoryTableFreeSlot": eqlPageMoveHistoryTableFreeSlot,
       "eqlPageMoveHistoryTableNextFreeSlot": eqlPageMoveHistoryTableNextFreeSlot,
       "eqlPageMoveHistoryTableMemberNextFreeSlot": eqlPageMoveHistoryTableMemberNextFreeSlot,
       "eqlPageMoveHistoryTable": eqlPageMoveHistoryTable,
       "eqlPageMoveHistoryEntry": eqlPageMoveHistoryEntry,
       "eqlPageMoveHistoryIndex": eqlPageMoveHistoryIndex,
       "eqlPageMoveHistoryPoolId": eqlPageMoveHistoryPoolId,
       "eqlPageMoveHistoryPlanId": eqlPageMoveHistoryPlanId,
       "eqlPageMoveHistoryMemberId": eqlPageMoveHistoryMemberId,
       "eqlPageMoveHistoryType": eqlPageMoveHistoryType,
       "eqlPageMoveHistoryStartTime": eqlPageMoveHistoryStartTime,
       "eqlPageMoveHistoryEndTime": eqlPageMoveHistoryEndTime,
       "eqlPageMoveHistoryTotalPages": eqlPageMoveHistoryTotalPages,
       "eqlPageMoveHistoryAllocatedPages": eqlPageMoveHistoryAllocatedPages,
       "eqlPageMoveHistoryTotalPagesMoved": eqlPageMoveHistoryTotalPagesMoved,
       "eqlPageMoveHistoryAllocatedPagesMoved": eqlPageMoveHistoryAllocatedPagesMoved,
       "eqlPageMoveHistoryResult": eqlPageMoveHistoryResult,
       "eqlPageMoveHistoryMemberStartIndex": eqlPageMoveHistoryMemberStartIndex,
       "eqlPageMoveHistoryMemberCount": eqlPageMoveHistoryMemberCount,
       "eqlPageMoveHistoryMemberTable": eqlPageMoveHistoryMemberTable,
       "eqlPageMoveHistoryMemberEntry": eqlPageMoveHistoryMemberEntry,
       "eqlPageMoveHistoryMemberIndex": eqlPageMoveHistoryMemberIndex,
       "eqlPageMoveHistoryMemberParentIndex": eqlPageMoveHistoryMemberParentIndex,
       "eqlPageMoveHistoryMemberPlanId": eqlPageMoveHistoryMemberPlanId,
       "eqlPageMoveHistoryMemberUuid": eqlPageMoveHistoryMemberUuid,
       "eqlPageMoveHistoryMemberAddedPages": eqlPageMoveHistoryMemberAddedPages,
       "eqlPageMoveHistoryMemberAddedAllocatedPages": eqlPageMoveHistoryMemberAddedAllocatedPages,
       "eqlPageMoveHistoryMemberRemovedPages": eqlPageMoveHistoryMemberRemovedPages,
       "eqlPageMoveHistoryMemberRemovedAllocatedPages": eqlPageMoveHistoryMemberRemovedAllocatedPages,
       "eqlPageMoveHistoryMemberStartAUS": eqlPageMoveHistoryMemberStartAUS,
       "eqlPageMoveHistoryMemberExpectedEndAUS": eqlPageMoveHistoryMemberExpectedEndAUS,
       "eqlLocalIOCountsTableFreeSlot": eqlLocalIOCountsTableFreeSlot,
       "eqlLocalIOCountsTableNextFreeSlot": eqlLocalIOCountsTableNextFreeSlot,
       "eqlLocalIOCountsTable": eqlLocalIOCountsTable,
       "eqlLocalIOCountsEntry": eqlLocalIOCountsEntry,
       "eqlLocalIOCountsIndex": eqlLocalIOCountsIndex,
       "eqlLocalIOCountsTimestamp": eqlLocalIOCountsTimestamp,
       "eqlLocalIOCountsReads": eqlLocalIOCountsReads,
       "eqlLocalIOCountsReadBytes": eqlLocalIOCountsReadBytes,
       "eqlLocalIOCountsReadLatencyMs": eqlLocalIOCountsReadLatencyMs,
       "eqlLocalIOCountsWrites": eqlLocalIOCountsWrites,
       "eqlLocalIOCountsWriteBytes": eqlLocalIOCountsWriteBytes,
       "eqlLocalIOCountsWriteLatencyMs": eqlLocalIOCountsWriteLatencyMs,
       "eqlLocalIOCountsHeadroomPercent": eqlLocalIOCountsHeadroomPercent,
       "eqlLocalIOCountsWorstQueuingLatencyMs": eqlLocalIOCountsWorstQueuingLatencyMs,
       "eqlPlanAUSTable": eqlPlanAUSTable,
       "eqlPlanAUSEntry": eqlPlanAUSEntry,
       "eqlPlanAUSCount": eqlPlanAUSCount,
       "eqlPlanAUSArray": eqlPlanAUSArray,
       "eqlTaskLocalPickedPagesTable": eqlTaskLocalPickedPagesTable,
       "eqlTaskLocalPickedPagesEntry": eqlTaskLocalPickedPagesEntry,
       "eqlTaskLocalPickedProgress": eqlTaskLocalPickedProgress,
       "eqlTaskLocalPickedPagesCount": eqlTaskLocalPickedPagesCount,
       "eqlTaskLocalPickedPagesContext": eqlTaskLocalPickedPagesContext,
       "eqlTaskLocalPickedPagesRev": eqlTaskLocalPickedPagesRev,
       "eqlTaskLocalPickedPagesFlags": eqlTaskLocalPickedPagesFlags,
       "eqlTaskLocalPickedPagesEntryStatus": eqlTaskLocalPickedPagesEntryStatus,
       "eqlTaskLocalPickedPagesArray": eqlTaskLocalPickedPagesArray,
       "eqlTaskLocalPickedPagesAllocatedProgress": eqlTaskLocalPickedPagesAllocatedProgress,
       "eqlTaskLocalPickedPagesStatus": eqlTaskLocalPickedPagesStatus,
       "eqlMemberCountersTable": eqlMemberCountersTable,
       "eqlMemberCountersEntry": eqlMemberCountersEntry,
       "eqlMemberCountersIndex": eqlMemberCountersIndex,
       "eqlMemberCountersUuid": eqlMemberCountersUuid,
       "eqlMemberCountersTimeStamp": eqlMemberCountersTimeStamp,
       "eqlMemberCountersAddedPages": eqlMemberCountersAddedPages,
       "eqlMemberCountersRemovedPages": eqlMemberCountersRemovedPages,
       "eqlMemberCountersAddedAllocatedPages": eqlMemberCountersAddedAllocatedPages,
       "eqlMemberCountersRemovedAllocatedPages": eqlMemberCountersRemovedAllocatedPages,
       "eqlMemberCountersAddedHotPages": eqlMemberCountersAddedHotPages,
       "eqlMemberCountersRemovedHotPages": eqlMemberCountersRemovedHotPages,
       "eqlMemberCountersAddedColdPages": eqlMemberCountersAddedColdPages,
       "eqlMemberCountersRemovedColdPages": eqlMemberCountersRemovedColdPages,
       "eqlArchiveTaskTable": eqlArchiveTaskTable,
       "eqlArchiveTaskEntry": eqlArchiveTaskEntry,
       "eqlArchiveTaskIndex": eqlArchiveTaskIndex,
       "eqlArchiveTaskMemberCount": eqlArchiveTaskMemberCount,
       "eqlArchiveTaskType": eqlArchiveTaskType,
       "eqlArchiveTaskState": eqlArchiveTaskState,
       "eqlArchiveTaskEntryStatus": eqlArchiveTaskEntryStatus,
       "eqlArchiveTaskMember1Uuid": eqlArchiveTaskMember1Uuid,
       "eqlArchiveTaskMember1Flags": eqlArchiveTaskMember1Flags,
       "eqlArchiveTaskMember2Uuid": eqlArchiveTaskMember2Uuid,
       "eqlArchiveTaskMember2Flags": eqlArchiveTaskMember2Flags,
       "eqlArchiveTaskMember3Uuid": eqlArchiveTaskMember3Uuid,
       "eqlArchiveTaskMember3Flags": eqlArchiveTaskMember3Flags,
       "eqlArchiveTaskMember4Uuid": eqlArchiveTaskMember4Uuid,
       "eqlArchiveTaskMember4Flags": eqlArchiveTaskMember4Flags,
       "eqlArchiveTaskMember5Uuid": eqlArchiveTaskMember5Uuid,
       "eqlArchiveTaskMember5Flags": eqlArchiveTaskMember5Flags,
       "eqlArchiveTaskMember6Uuid": eqlArchiveTaskMember6Uuid,
       "eqlArchiveTaskMember6Flags": eqlArchiveTaskMember6Flags,
       "eqlArchiveTaskMember7Uuid": eqlArchiveTaskMember7Uuid,
       "eqlArchiveTaskMember7Flags": eqlArchiveTaskMember7Flags,
       "eqlArchiveTaskMember8Uuid": eqlArchiveTaskMember8Uuid,
       "eqlArchiveTaskMember8Flags": eqlArchiveTaskMember8Flags,
       "eqlArchiveTaskMember9Uuid": eqlArchiveTaskMember9Uuid,
       "eqlArchiveTaskMember9Flags": eqlArchiveTaskMember9Flags,
       "eqlArchiveTaskMember10Uuid": eqlArchiveTaskMember10Uuid,
       "eqlArchiveTaskMember10Flags": eqlArchiveTaskMember10Flags,
       "eqlArchiveTaskMember11Uuid": eqlArchiveTaskMember11Uuid,
       "eqlArchiveTaskMember11Flags": eqlArchiveTaskMember11Flags,
       "eqlArchiveTaskMember12Uuid": eqlArchiveTaskMember12Uuid,
       "eqlArchiveTaskMember12Flags": eqlArchiveTaskMember12Flags,
       "eqlArchiveTaskMember13Uuid": eqlArchiveTaskMember13Uuid,
       "eqlArchiveTaskMember13Flags": eqlArchiveTaskMember13Flags,
       "eqlArchiveTaskMember14Uuid": eqlArchiveTaskMember14Uuid,
       "eqlArchiveTaskMember14Flags": eqlArchiveTaskMember14Flags,
       "eqlArchiveTaskMember15Uuid": eqlArchiveTaskMember15Uuid,
       "eqlArchiveTaskMember15Flags": eqlArchiveTaskMember15Flags,
       "eqlArchiveTaskMember16Uuid": eqlArchiveTaskMember16Uuid,
       "eqlArchiveTaskMember16Flags": eqlArchiveTaskMember16Flags,
       "eqlvolbalancerNotifications": eqlvolbalancerNotifications,
       "eqlvolbalancerConformance": eqlvolbalancerConformance}
)

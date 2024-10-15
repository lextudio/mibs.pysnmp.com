# SNMP MIB module (Unisphere-Data-QoS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-QoS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:27 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57)
)
usdQosMIB.setRevisions(
        ("2002-05-10 17:25",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdQosObjects_ObjectIdentity = ObjectIdentity
usdQosObjects = _UsdQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1)
)
_UsdQosCapability_ObjectIdentity = ObjectIdentity
usdQosCapability = _UsdQosCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 1)
)
_UsdQosMaxTrafficClass_Type = Unsigned32
_UsdQosMaxTrafficClass_Object = MibScalar
usdQosMaxTrafficClass = _UsdQosMaxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 1, 1),
    _UsdQosMaxTrafficClass_Type()
)
usdQosMaxTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosMaxTrafficClass.setStatus("current")
_UsdQosMaxQueueLength_Type = Unsigned32
_UsdQosMaxQueueLength_Object = MibScalar
usdQosMaxQueueLength = _UsdQosMaxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 1, 2),
    _UsdQosMaxQueueLength_Type()
)
usdQosMaxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosMaxQueueLength.setStatus("current")
if mibBuilder.loadTexts:
    usdQosMaxQueueLength.setUnits("bytes")
_UsdQosMinSchedulerBurst_Type = Unsigned32
_UsdQosMinSchedulerBurst_Object = MibScalar
usdQosMinSchedulerBurst = _UsdQosMinSchedulerBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 1, 3),
    _UsdQosMinSchedulerBurst_Type()
)
usdQosMinSchedulerBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosMinSchedulerBurst.setStatus("current")
if mibBuilder.loadTexts:
    usdQosMinSchedulerBurst.setUnits("bytes")
_UsdQosMaxSchedulerBurst_Type = Unsigned32
_UsdQosMaxSchedulerBurst_Object = MibScalar
usdQosMaxSchedulerBurst = _UsdQosMaxSchedulerBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 1, 4),
    _UsdQosMaxSchedulerBurst_Type()
)
usdQosMaxSchedulerBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosMaxSchedulerBurst.setStatus("current")
if mibBuilder.loadTexts:
    usdQosMaxSchedulerBurst.setUnits("bytes")
_UsdQos_ObjectIdentity = ObjectIdentity
usdQos = _UsdQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2)
)
_UsdQosTrafficClassCount_Type = Gauge32
_UsdQosTrafficClassCount_Object = MibScalar
usdQosTrafficClassCount = _UsdQosTrafficClassCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 1),
    _UsdQosTrafficClassCount_Type()
)
usdQosTrafficClassCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosTrafficClassCount.setStatus("current")
_UsdQosQueueProfileCount_Type = Gauge32
_UsdQosQueueProfileCount_Object = MibScalar
usdQosQueueProfileCount = _UsdQosQueueProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 2),
    _UsdQosQueueProfileCount_Type()
)
usdQosQueueProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosQueueProfileCount.setStatus("current")
_UsdQosSchedulerProfileCount_Type = Gauge32
_UsdQosSchedulerProfileCount_Object = MibScalar
usdQosSchedulerProfileCount = _UsdQosSchedulerProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 3),
    _UsdQosSchedulerProfileCount_Type()
)
usdQosSchedulerProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileCount.setStatus("current")
_UsdQosProfileCount_Type = Gauge32
_UsdQosProfileCount_Object = MibScalar
usdQosProfileCount = _UsdQosProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 4),
    _UsdQosProfileCount_Type()
)
usdQosProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosProfileCount.setStatus("current")
_UsdQosInterfaceCount_Type = Gauge32
_UsdQosInterfaceCount_Object = MibScalar
usdQosInterfaceCount = _UsdQosInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 5),
    _UsdQosInterfaceCount_Type()
)
usdQosInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosInterfaceCount.setStatus("current")
_UsdQosQosPortTypeProfileCount_Type = Gauge32
_UsdQosQosPortTypeProfileCount_Object = MibScalar
usdQosQosPortTypeProfileCount = _UsdQosQosPortTypeProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 6),
    _UsdQosQosPortTypeProfileCount_Type()
)
usdQosQosPortTypeProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosQosPortTypeProfileCount.setStatus("current")
_UsdQosTrafficClassList_ObjectIdentity = ObjectIdentity
usdQosTrafficClassList = _UsdQosTrafficClassList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3)
)
_UsdQosTrafficClassNextIndex_Type = Unsigned32
_UsdQosTrafficClassNextIndex_Object = MibScalar
usdQosTrafficClassNextIndex = _UsdQosTrafficClassNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 1),
    _UsdQosTrafficClassNextIndex_Type()
)
usdQosTrafficClassNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosTrafficClassNextIndex.setStatus("current")
_UsdQosTrafficClassTable_Object = MibTable
usdQosTrafficClassTable = _UsdQosTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2)
)
if mibBuilder.loadTexts:
    usdQosTrafficClassTable.setStatus("current")
_UsdQosTrafficClassEntry_Object = MibTableRow
usdQosTrafficClassEntry = _UsdQosTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1)
)
usdQosTrafficClassEntry.setIndexNames(
    (0, "Unisphere-Data-QoS-MIB", "usdQosTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    usdQosTrafficClassEntry.setStatus("current")
_UsdQosTrafficClassIndex_Type = Unsigned32
_UsdQosTrafficClassIndex_Object = MibTableColumn
usdQosTrafficClassIndex = _UsdQosTrafficClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 1),
    _UsdQosTrafficClassIndex_Type()
)
usdQosTrafficClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdQosTrafficClassIndex.setStatus("current")
_UsdQosTrafficClassRowStatus_Type = RowStatus
_UsdQosTrafficClassRowStatus_Object = MibTableColumn
usdQosTrafficClassRowStatus = _UsdQosTrafficClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 2),
    _UsdQosTrafficClassRowStatus_Type()
)
usdQosTrafficClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosTrafficClassRowStatus.setStatus("current")


class _UsdQosTrafficClassName_Type(DisplayString):
    """Custom type usdQosTrafficClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UsdQosTrafficClassName_Type.__name__ = "DisplayString"
_UsdQosTrafficClassName_Object = MibTableColumn
usdQosTrafficClassName = _UsdQosTrafficClassName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 3),
    _UsdQosTrafficClassName_Type()
)
usdQosTrafficClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosTrafficClassName.setStatus("current")


class _UsdQosTrafficClassWeight_Type(Unsigned32):
    """Custom type usdQosTrafficClassWeight based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_UsdQosTrafficClassWeight_Type.__name__ = "Unsigned32"
_UsdQosTrafficClassWeight_Object = MibTableColumn
usdQosTrafficClassWeight = _UsdQosTrafficClassWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 4),
    _UsdQosTrafficClassWeight_Type()
)
usdQosTrafficClassWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosTrafficClassWeight.setStatus("current")


class _UsdQosTrafficClassStrictPriority_Type(TruthValue):
    """Custom type usdQosTrafficClassStrictPriority based on TruthValue"""


_UsdQosTrafficClassStrictPriority_Object = MibTableColumn
usdQosTrafficClassStrictPriority = _UsdQosTrafficClassStrictPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 5),
    _UsdQosTrafficClassStrictPriority_Type()
)
usdQosTrafficClassStrictPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosTrafficClassStrictPriority.setStatus("current")
_UsdQosTrafficClassUpdatePending_Type = TruthValue
_UsdQosTrafficClassUpdatePending_Object = MibTableColumn
usdQosTrafficClassUpdatePending = _UsdQosTrafficClassUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 6),
    _UsdQosTrafficClassUpdatePending_Type()
)
usdQosTrafficClassUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosTrafficClassUpdatePending.setStatus("current")
_UsdQosTrafficClassUpdateNow_Type = TruthValue
_UsdQosTrafficClassUpdateNow_Object = MibTableColumn
usdQosTrafficClassUpdateNow = _UsdQosTrafficClassUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 7),
    _UsdQosTrafficClassUpdateNow_Type()
)
usdQosTrafficClassUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosTrafficClassUpdateNow.setStatus("current")
_UsdQosTrafficClassIsReferencedByGroup_Type = TruthValue
_UsdQosTrafficClassIsReferencedByGroup_Object = MibTableColumn
usdQosTrafficClassIsReferencedByGroup = _UsdQosTrafficClassIsReferencedByGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 8),
    _UsdQosTrafficClassIsReferencedByGroup_Type()
)
usdQosTrafficClassIsReferencedByGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosTrafficClassIsReferencedByGroup.setStatus("current")
_UsdQosTrafficClassIsReferencedByQosProfile_Type = TruthValue
_UsdQosTrafficClassIsReferencedByQosProfile_Object = MibTableColumn
usdQosTrafficClassIsReferencedByQosProfile = _UsdQosTrafficClassIsReferencedByQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 9),
    _UsdQosTrafficClassIsReferencedByQosProfile_Type()
)
usdQosTrafficClassIsReferencedByQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosTrafficClassIsReferencedByQosProfile.setStatus("current")
_UsdQosTrafficClassGroupList_ObjectIdentity = ObjectIdentity
usdQosTrafficClassGroupList = _UsdQosTrafficClassGroupList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4)
)
_UsdQosTrafficClassGroupNextIndex_Type = Unsigned32
_UsdQosTrafficClassGroupNextIndex_Object = MibScalar
usdQosTrafficClassGroupNextIndex = _UsdQosTrafficClassGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 1),
    _UsdQosTrafficClassGroupNextIndex_Type()
)
usdQosTrafficClassGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupNextIndex.setStatus("current")
_UsdQosTrafficClassGroupTable_Object = MibTable
usdQosTrafficClassGroupTable = _UsdQosTrafficClassGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2)
)
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupTable.setStatus("current")
_UsdQosTrafficClassGroupEntry_Object = MibTableRow
usdQosTrafficClassGroupEntry = _UsdQosTrafficClassGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1)
)
usdQosTrafficClassGroupEntry.setIndexNames(
    (0, "Unisphere-Data-QoS-MIB", "usdQosTrafficClassGroupIndex"),
)
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupEntry.setStatus("current")
_UsdQosTrafficClassGroupIndex_Type = Unsigned32
_UsdQosTrafficClassGroupIndex_Object = MibTableColumn
usdQosTrafficClassGroupIndex = _UsdQosTrafficClassGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 1),
    _UsdQosTrafficClassGroupIndex_Type()
)
usdQosTrafficClassGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupIndex.setStatus("current")
_UsdQosTrafficClassGroupRowStatus_Type = RowStatus
_UsdQosTrafficClassGroupRowStatus_Object = MibTableColumn
usdQosTrafficClassGroupRowStatus = _UsdQosTrafficClassGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 2),
    _UsdQosTrafficClassGroupRowStatus_Type()
)
usdQosTrafficClassGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupRowStatus.setStatus("current")


class _UsdQosTrafficClassGroupName_Type(DisplayString):
    """Custom type usdQosTrafficClassGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UsdQosTrafficClassGroupName_Type.__name__ = "DisplayString"
_UsdQosTrafficClassGroupName_Object = MibTableColumn
usdQosTrafficClassGroupName = _UsdQosTrafficClassGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 3),
    _UsdQosTrafficClassGroupName_Type()
)
usdQosTrafficClassGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupName.setStatus("current")
_UsdQosTrafficClassGroupUpdatePending_Type = TruthValue
_UsdQosTrafficClassGroupUpdatePending_Object = MibTableColumn
usdQosTrafficClassGroupUpdatePending = _UsdQosTrafficClassGroupUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 4),
    _UsdQosTrafficClassGroupUpdatePending_Type()
)
usdQosTrafficClassGroupUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupUpdatePending.setStatus("current")
_UsdQosTrafficClassGroupUpdateNow_Type = TruthValue
_UsdQosTrafficClassGroupUpdateNow_Object = MibTableColumn
usdQosTrafficClassGroupUpdateNow = _UsdQosTrafficClassGroupUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 5),
    _UsdQosTrafficClassGroupUpdateNow_Type()
)
usdQosTrafficClassGroupUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupUpdateNow.setStatus("current")
_UsdQosTrafficClassGroupIsReferencedByQosProfile_Type = TruthValue
_UsdQosTrafficClassGroupIsReferencedByQosProfile_Object = MibTableColumn
usdQosTrafficClassGroupIsReferencedByQosProfile = _UsdQosTrafficClassGroupIsReferencedByQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 6),
    _UsdQosTrafficClassGroupIsReferencedByQosProfile_Type()
)
usdQosTrafficClassGroupIsReferencedByQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupIsReferencedByQosProfile.setStatus("current")
_UsdQosTrafficClassGroupEntryList_ObjectIdentity = ObjectIdentity
usdQosTrafficClassGroupEntryList = _UsdQosTrafficClassGroupEntryList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 5)
)
_UsdQosTrafficClassGroupEntryTable_Object = MibTable
usdQosTrafficClassGroupEntryTable = _UsdQosTrafficClassGroupEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 5, 1)
)
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupEntryTable.setStatus("current")
_UsdQosTrafficClassGroupEntryEntry_Object = MibTableRow
usdQosTrafficClassGroupEntryEntry = _UsdQosTrafficClassGroupEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 5, 1, 1)
)
usdQosTrafficClassGroupEntryEntry.setIndexNames(
    (0, "Unisphere-Data-QoS-MIB", "usdQosTrafficClassGroupIndex"),
    (0, "Unisphere-Data-QoS-MIB", "usdQosTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupEntryEntry.setStatus("current")
_UsdQosTrafficClassGroupEntryRowStatus_Type = RowStatus
_UsdQosTrafficClassGroupEntryRowStatus_Object = MibTableColumn
usdQosTrafficClassGroupEntryRowStatus = _UsdQosTrafficClassGroupEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 5, 1, 1, 1),
    _UsdQosTrafficClassGroupEntryRowStatus_Type()
)
usdQosTrafficClassGroupEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupEntryRowStatus.setStatus("current")
_UsdQosSchedulerProfileList_ObjectIdentity = ObjectIdentity
usdQosSchedulerProfileList = _UsdQosSchedulerProfileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6)
)
_UsdQosSchedulerProfileNextIndex_Type = Unsigned32
_UsdQosSchedulerProfileNextIndex_Object = MibScalar
usdQosSchedulerProfileNextIndex = _UsdQosSchedulerProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 1),
    _UsdQosSchedulerProfileNextIndex_Type()
)
usdQosSchedulerProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileNextIndex.setStatus("current")
_UsdQosSchedulerProfileTable_Object = MibTable
usdQosSchedulerProfileTable = _UsdQosSchedulerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2)
)
if mibBuilder.loadTexts:
    usdQosSchedulerProfileTable.setStatus("current")
_UsdQosSchedulerProfileEntry_Object = MibTableRow
usdQosSchedulerProfileEntry = _UsdQosSchedulerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1)
)
usdQosSchedulerProfileEntry.setIndexNames(
    (0, "Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileIndex"),
)
if mibBuilder.loadTexts:
    usdQosSchedulerProfileEntry.setStatus("current")
_UsdQosSchedulerProfileIndex_Type = Unsigned32
_UsdQosSchedulerProfileIndex_Object = MibTableColumn
usdQosSchedulerProfileIndex = _UsdQosSchedulerProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 1),
    _UsdQosSchedulerProfileIndex_Type()
)
usdQosSchedulerProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileIndex.setStatus("current")
_UsdQosSchedulerProfileRowStatus_Type = RowStatus
_UsdQosSchedulerProfileRowStatus_Object = MibTableColumn
usdQosSchedulerProfileRowStatus = _UsdQosSchedulerProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 2),
    _UsdQosSchedulerProfileRowStatus_Type()
)
usdQosSchedulerProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileRowStatus.setStatus("current")


class _UsdQosSchedulerProfileName_Type(DisplayString):
    """Custom type usdQosSchedulerProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UsdQosSchedulerProfileName_Type.__name__ = "DisplayString"
_UsdQosSchedulerProfileName_Object = MibTableColumn
usdQosSchedulerProfileName = _UsdQosSchedulerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 3),
    _UsdQosSchedulerProfileName_Type()
)
usdQosSchedulerProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileName.setStatus("current")


class _UsdQosSchedulerProfileShapingRate_Type(Unsigned32):
    """Custom type usdQosSchedulerProfileShapingRate based on Unsigned32"""
    defaultValue = 0


_UsdQosSchedulerProfileShapingRate_Object = MibTableColumn
usdQosSchedulerProfileShapingRate = _UsdQosSchedulerProfileShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 4),
    _UsdQosSchedulerProfileShapingRate_Type()
)
usdQosSchedulerProfileShapingRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileShapingRate.setStatus("current")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileShapingRate.setUnits("kbps")


class _UsdQosSchedulerProfileBurst_Type(Unsigned32):
    """Custom type usdQosSchedulerProfileBurst based on Unsigned32"""
    defaultValue = 32768


_UsdQosSchedulerProfileBurst_Object = MibTableColumn
usdQosSchedulerProfileBurst = _UsdQosSchedulerProfileBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 5),
    _UsdQosSchedulerProfileBurst_Type()
)
usdQosSchedulerProfileBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileBurst.setStatus("current")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileBurst.setUnits("bytes")


class _UsdQosSchedulerProfileWeight_Type(Unsigned32):
    """Custom type usdQosSchedulerProfileWeight based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_UsdQosSchedulerProfileWeight_Type.__name__ = "Unsigned32"
_UsdQosSchedulerProfileWeight_Object = MibTableColumn
usdQosSchedulerProfileWeight = _UsdQosSchedulerProfileWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 6),
    _UsdQosSchedulerProfileWeight_Type()
)
usdQosSchedulerProfileWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileWeight.setStatus("current")


class _UsdQosSchedulerProfileStrictPriority_Type(TruthValue):
    """Custom type usdQosSchedulerProfileStrictPriority based on TruthValue"""


_UsdQosSchedulerProfileStrictPriority_Object = MibTableColumn
usdQosSchedulerProfileStrictPriority = _UsdQosSchedulerProfileStrictPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 7),
    _UsdQosSchedulerProfileStrictPriority_Type()
)
usdQosSchedulerProfileStrictPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileStrictPriority.setStatus("current")
_UsdQosSchedulerProfileUpdatePending_Type = TruthValue
_UsdQosSchedulerProfileUpdatePending_Object = MibTableColumn
usdQosSchedulerProfileUpdatePending = _UsdQosSchedulerProfileUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 8),
    _UsdQosSchedulerProfileUpdatePending_Type()
)
usdQosSchedulerProfileUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileUpdatePending.setStatus("current")
_UsdQosSchedulerProfileUpdateNow_Type = TruthValue
_UsdQosSchedulerProfileUpdateNow_Object = MibTableColumn
usdQosSchedulerProfileUpdateNow = _UsdQosSchedulerProfileUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 9),
    _UsdQosSchedulerProfileUpdateNow_Type()
)
usdQosSchedulerProfileUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileUpdateNow.setStatus("current")
_UsdQosSchedulerProfileIsReferencedByQosProfile_Type = TruthValue
_UsdQosSchedulerProfileIsReferencedByQosProfile_Object = MibTableColumn
usdQosSchedulerProfileIsReferencedByQosProfile = _UsdQosSchedulerProfileIsReferencedByQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 10),
    _UsdQosSchedulerProfileIsReferencedByQosProfile_Type()
)
usdQosSchedulerProfileIsReferencedByQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosSchedulerProfileIsReferencedByQosProfile.setStatus("current")
_UsdQosQueueProfileList_ObjectIdentity = ObjectIdentity
usdQosQueueProfileList = _UsdQosQueueProfileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7)
)
_UsdQosQueueProfileNextIndex_Type = Unsigned32
_UsdQosQueueProfileNextIndex_Object = MibScalar
usdQosQueueProfileNextIndex = _UsdQosQueueProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 1),
    _UsdQosQueueProfileNextIndex_Type()
)
usdQosQueueProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosQueueProfileNextIndex.setStatus("current")
_UsdQosQueueProfileTable_Object = MibTable
usdQosQueueProfileTable = _UsdQosQueueProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2)
)
if mibBuilder.loadTexts:
    usdQosQueueProfileTable.setStatus("current")
_UsdQosQueueProfileEntry_Object = MibTableRow
usdQosQueueProfileEntry = _UsdQosQueueProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1)
)
usdQosQueueProfileEntry.setIndexNames(
    (0, "Unisphere-Data-QoS-MIB", "usdQosQueueProfileIndex"),
)
if mibBuilder.loadTexts:
    usdQosQueueProfileEntry.setStatus("current")
_UsdQosQueueProfileIndex_Type = Unsigned32
_UsdQosQueueProfileIndex_Object = MibTableColumn
usdQosQueueProfileIndex = _UsdQosQueueProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 1),
    _UsdQosQueueProfileIndex_Type()
)
usdQosQueueProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdQosQueueProfileIndex.setStatus("current")
_UsdQosQueueProfileRowStatus_Type = RowStatus
_UsdQosQueueProfileRowStatus_Object = MibTableColumn
usdQosQueueProfileRowStatus = _UsdQosQueueProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 2),
    _UsdQosQueueProfileRowStatus_Type()
)
usdQosQueueProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileRowStatus.setStatus("current")


class _UsdQosQueueProfileName_Type(DisplayString):
    """Custom type usdQosQueueProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UsdQosQueueProfileName_Type.__name__ = "DisplayString"
_UsdQosQueueProfileName_Object = MibTableColumn
usdQosQueueProfileName = _UsdQosQueueProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 3),
    _UsdQosQueueProfileName_Type()
)
usdQosQueueProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileName.setStatus("current")


class _UsdQosQueueProfileCommittedMinLength_Type(Unsigned32):
    """Custom type usdQosQueueProfileCommittedMinLength based on Unsigned32"""
    defaultValue = 0


_UsdQosQueueProfileCommittedMinLength_Object = MibTableColumn
usdQosQueueProfileCommittedMinLength = _UsdQosQueueProfileCommittedMinLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 4),
    _UsdQosQueueProfileCommittedMinLength_Type()
)
usdQosQueueProfileCommittedMinLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileCommittedMinLength.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileCommittedMinLength.setUnits("bytes")


class _UsdQosQueueProfileCommittedMaxLength_Type(Unsigned32):
    """Custom type usdQosQueueProfileCommittedMaxLength based on Unsigned32"""
    defaultValue = 1073741824


_UsdQosQueueProfileCommittedMaxLength_Object = MibTableColumn
usdQosQueueProfileCommittedMaxLength = _UsdQosQueueProfileCommittedMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 5),
    _UsdQosQueueProfileCommittedMaxLength_Type()
)
usdQosQueueProfileCommittedMaxLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileCommittedMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileCommittedMaxLength.setUnits("bytes")


class _UsdQosQueueProfileConformedMinLength_Type(Unsigned32):
    """Custom type usdQosQueueProfileConformedMinLength based on Unsigned32"""
    defaultValue = 0


_UsdQosQueueProfileConformedMinLength_Object = MibTableColumn
usdQosQueueProfileConformedMinLength = _UsdQosQueueProfileConformedMinLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 6),
    _UsdQosQueueProfileConformedMinLength_Type()
)
usdQosQueueProfileConformedMinLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileConformedMinLength.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileConformedMinLength.setUnits("bytes")


class _UsdQosQueueProfileConformedMaxLength_Type(Unsigned32):
    """Custom type usdQosQueueProfileConformedMaxLength based on Unsigned32"""
    defaultValue = 1073741824


_UsdQosQueueProfileConformedMaxLength_Object = MibTableColumn
usdQosQueueProfileConformedMaxLength = _UsdQosQueueProfileConformedMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 7),
    _UsdQosQueueProfileConformedMaxLength_Type()
)
usdQosQueueProfileConformedMaxLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileConformedMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileConformedMaxLength.setUnits("bytes")


class _UsdQosQueueProfileExceededMinLength_Type(Unsigned32):
    """Custom type usdQosQueueProfileExceededMinLength based on Unsigned32"""
    defaultValue = 0


_UsdQosQueueProfileExceededMinLength_Object = MibTableColumn
usdQosQueueProfileExceededMinLength = _UsdQosQueueProfileExceededMinLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 8),
    _UsdQosQueueProfileExceededMinLength_Type()
)
usdQosQueueProfileExceededMinLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileExceededMinLength.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileExceededMinLength.setUnits("bytes")


class _UsdQosQueueProfileExceededMaxLength_Type(Unsigned32):
    """Custom type usdQosQueueProfileExceededMaxLength based on Unsigned32"""
    defaultValue = 1073741824


_UsdQosQueueProfileExceededMaxLength_Object = MibTableColumn
usdQosQueueProfileExceededMaxLength = _UsdQosQueueProfileExceededMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 9),
    _UsdQosQueueProfileExceededMaxLength_Type()
)
usdQosQueueProfileExceededMaxLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileExceededMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileExceededMaxLength.setUnits("bytes")


class _UsdQosQueueProfileConformedFraction_Type(Unsigned32):
    """Custom type usdQosQueueProfileConformedFraction based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UsdQosQueueProfileConformedFraction_Type.__name__ = "Unsigned32"
_UsdQosQueueProfileConformedFraction_Object = MibTableColumn
usdQosQueueProfileConformedFraction = _UsdQosQueueProfileConformedFraction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 10),
    _UsdQosQueueProfileConformedFraction_Type()
)
usdQosQueueProfileConformedFraction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileConformedFraction.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileConformedFraction.setUnits("percent")


class _UsdQosQueueProfileExceededFraction_Type(Unsigned32):
    """Custom type usdQosQueueProfileExceededFraction based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UsdQosQueueProfileExceededFraction_Type.__name__ = "Unsigned32"
_UsdQosQueueProfileExceededFraction_Object = MibTableColumn
usdQosQueueProfileExceededFraction = _UsdQosQueueProfileExceededFraction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 11),
    _UsdQosQueueProfileExceededFraction_Type()
)
usdQosQueueProfileExceededFraction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileExceededFraction.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileExceededFraction.setUnits("percent")


class _UsdQosQueueProfileCommittedDropThreshold_Type(Unsigned32):
    """Custom type usdQosQueueProfileCommittedDropThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UsdQosQueueProfileCommittedDropThreshold_Type.__name__ = "Unsigned32"
_UsdQosQueueProfileCommittedDropThreshold_Object = MibTableColumn
usdQosQueueProfileCommittedDropThreshold = _UsdQosQueueProfileCommittedDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 12),
    _UsdQosQueueProfileCommittedDropThreshold_Type()
)
usdQosQueueProfileCommittedDropThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileCommittedDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileCommittedDropThreshold.setUnits("percent")


class _UsdQosQueueProfileCommittedDropRate_Type(Unsigned32):
    """Custom type usdQosQueueProfileCommittedDropRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UsdQosQueueProfileCommittedDropRate_Type.__name__ = "Unsigned32"
_UsdQosQueueProfileCommittedDropRate_Object = MibTableColumn
usdQosQueueProfileCommittedDropRate = _UsdQosQueueProfileCommittedDropRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 13),
    _UsdQosQueueProfileCommittedDropRate_Type()
)
usdQosQueueProfileCommittedDropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileCommittedDropRate.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileCommittedDropRate.setUnits("percent")


class _UsdQosQueueProfileConformedDropThreshold_Type(Unsigned32):
    """Custom type usdQosQueueProfileConformedDropThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UsdQosQueueProfileConformedDropThreshold_Type.__name__ = "Unsigned32"
_UsdQosQueueProfileConformedDropThreshold_Object = MibTableColumn
usdQosQueueProfileConformedDropThreshold = _UsdQosQueueProfileConformedDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 14),
    _UsdQosQueueProfileConformedDropThreshold_Type()
)
usdQosQueueProfileConformedDropThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileConformedDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileConformedDropThreshold.setUnits("percent")


class _UsdQosQueueProfileConformedDropRate_Type(Unsigned32):
    """Custom type usdQosQueueProfileConformedDropRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UsdQosQueueProfileConformedDropRate_Type.__name__ = "Unsigned32"
_UsdQosQueueProfileConformedDropRate_Object = MibTableColumn
usdQosQueueProfileConformedDropRate = _UsdQosQueueProfileConformedDropRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 15),
    _UsdQosQueueProfileConformedDropRate_Type()
)
usdQosQueueProfileConformedDropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileConformedDropRate.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileConformedDropRate.setUnits("percent")


class _UsdQosQueueProfileExceededDropThreshold_Type(Unsigned32):
    """Custom type usdQosQueueProfileExceededDropThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UsdQosQueueProfileExceededDropThreshold_Type.__name__ = "Unsigned32"
_UsdQosQueueProfileExceededDropThreshold_Object = MibTableColumn
usdQosQueueProfileExceededDropThreshold = _UsdQosQueueProfileExceededDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 16),
    _UsdQosQueueProfileExceededDropThreshold_Type()
)
usdQosQueueProfileExceededDropThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileExceededDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileExceededDropThreshold.setUnits("percent")


class _UsdQosQueueProfileExceededDropRate_Type(Unsigned32):
    """Custom type usdQosQueueProfileExceededDropRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UsdQosQueueProfileExceededDropRate_Type.__name__ = "Unsigned32"
_UsdQosQueueProfileExceededDropRate_Object = MibTableColumn
usdQosQueueProfileExceededDropRate = _UsdQosQueueProfileExceededDropRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 17),
    _UsdQosQueueProfileExceededDropRate_Type()
)
usdQosQueueProfileExceededDropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileExceededDropRate.setStatus("current")
if mibBuilder.loadTexts:
    usdQosQueueProfileExceededDropRate.setUnits("percent")


class _UsdQosQueueProfileBufferWeight_Type(Unsigned32):
    """Custom type usdQosQueueProfileBufferWeight based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_UsdQosQueueProfileBufferWeight_Type.__name__ = "Unsigned32"
_UsdQosQueueProfileBufferWeight_Object = MibTableColumn
usdQosQueueProfileBufferWeight = _UsdQosQueueProfileBufferWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 18),
    _UsdQosQueueProfileBufferWeight_Type()
)
usdQosQueueProfileBufferWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileBufferWeight.setStatus("current")
_UsdQosQueueProfileUpdatePending_Type = TruthValue
_UsdQosQueueProfileUpdatePending_Object = MibTableColumn
usdQosQueueProfileUpdatePending = _UsdQosQueueProfileUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 19),
    _UsdQosQueueProfileUpdatePending_Type()
)
usdQosQueueProfileUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosQueueProfileUpdatePending.setStatus("current")
_UsdQosQueueProfileUpdateNow_Type = TruthValue
_UsdQosQueueProfileUpdateNow_Object = MibTableColumn
usdQosQueueProfileUpdateNow = _UsdQosQueueProfileUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 20),
    _UsdQosQueueProfileUpdateNow_Type()
)
usdQosQueueProfileUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQueueProfileUpdateNow.setStatus("current")
_UsdQosQueueProfileIsReferencedByQosProfile_Type = TruthValue
_UsdQosQueueProfileIsReferencedByQosProfile_Object = MibTableColumn
usdQosQueueProfileIsReferencedByQosProfile = _UsdQosQueueProfileIsReferencedByQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 21),
    _UsdQosQueueProfileIsReferencedByQosProfile_Type()
)
usdQosQueueProfileIsReferencedByQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosQueueProfileIsReferencedByQosProfile.setStatus("current")
_UsdQosProfile_ObjectIdentity = ObjectIdentity
usdQosProfile = _UsdQosProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8)
)
_UsdQosProfileNextIndex_Type = Unsigned32
_UsdQosProfileNextIndex_Object = MibScalar
usdQosProfileNextIndex = _UsdQosProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 1),
    _UsdQosProfileNextIndex_Type()
)
usdQosProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosProfileNextIndex.setStatus("current")
_UsdQosProfileTable_Object = MibTable
usdQosProfileTable = _UsdQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2)
)
if mibBuilder.loadTexts:
    usdQosProfileTable.setStatus("current")
_UsdQosProfileEntry_Object = MibTableRow
usdQosProfileEntry = _UsdQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1)
)
usdQosProfileEntry.setIndexNames(
    (0, "Unisphere-Data-QoS-MIB", "usdQosProfileIndex"),
)
if mibBuilder.loadTexts:
    usdQosProfileEntry.setStatus("current")
_UsdQosProfileIndex_Type = Unsigned32
_UsdQosProfileIndex_Object = MibTableColumn
usdQosProfileIndex = _UsdQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 1),
    _UsdQosProfileIndex_Type()
)
usdQosProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdQosProfileIndex.setStatus("current")
_UsdQosProfileRowStatus_Type = RowStatus
_UsdQosProfileRowStatus_Object = MibTableColumn
usdQosProfileRowStatus = _UsdQosProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 2),
    _UsdQosProfileRowStatus_Type()
)
usdQosProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosProfileRowStatus.setStatus("current")


class _UsdQosProfileName_Type(DisplayString):
    """Custom type usdQosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UsdQosProfileName_Type.__name__ = "DisplayString"
_UsdQosProfileName_Object = MibTableColumn
usdQosProfileName = _UsdQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 3),
    _UsdQosProfileName_Type()
)
usdQosProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosProfileName.setStatus("current")
_UsdQosProfileUpdatePending_Type = TruthValue
_UsdQosProfileUpdatePending_Object = MibTableColumn
usdQosProfileUpdatePending = _UsdQosProfileUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 4),
    _UsdQosProfileUpdatePending_Type()
)
usdQosProfileUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosProfileUpdatePending.setStatus("current")
_UsdQosProfileUpdateNow_Type = TruthValue
_UsdQosProfileUpdateNow_Object = MibTableColumn
usdQosProfileUpdateNow = _UsdQosProfileUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 5),
    _UsdQosProfileUpdateNow_Type()
)
usdQosProfileUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosProfileUpdateNow.setStatus("current")
_UsdQosProfileIsReferencedByInterfaceQosAttachment_Type = TruthValue
_UsdQosProfileIsReferencedByInterfaceQosAttachment_Object = MibTableColumn
usdQosProfileIsReferencedByInterfaceQosAttachment = _UsdQosProfileIsReferencedByInterfaceQosAttachment_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 6),
    _UsdQosProfileIsReferencedByInterfaceQosAttachment_Type()
)
usdQosProfileIsReferencedByInterfaceQosAttachment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosProfileIsReferencedByInterfaceQosAttachment.setStatus("current")
_UsdQosProfileIsReferencedByQosPortTypeProfile_Type = TruthValue
_UsdQosProfileIsReferencedByQosPortTypeProfile_Object = MibTableColumn
usdQosProfileIsReferencedByQosPortTypeProfile = _UsdQosProfileIsReferencedByQosPortTypeProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 7),
    _UsdQosProfileIsReferencedByQosPortTypeProfile_Type()
)
usdQosProfileIsReferencedByQosPortTypeProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosProfileIsReferencedByQosPortTypeProfile.setStatus("current")
_UsdQosProfileElement_ObjectIdentity = ObjectIdentity
usdQosProfileElement = _UsdQosProfileElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9)
)
_UsdQosProfileElementTable_Object = MibTable
usdQosProfileElementTable = _UsdQosProfileElementTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1)
)
if mibBuilder.loadTexts:
    usdQosProfileElementTable.setStatus("current")
_UsdQosProfileElementEntry_Object = MibTableRow
usdQosProfileElementEntry = _UsdQosProfileElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1)
)
usdQosProfileElementEntry.setIndexNames(
    (0, "Unisphere-Data-QoS-MIB", "usdQosProfileIndex"),
    (0, "Unisphere-Data-QoS-MIB", "usdQosInterfaceType"),
    (0, "Unisphere-Data-QoS-MIB", "usdQosProfileEntryType"),
    (0, "Unisphere-Data-QoS-MIB", "usdQosTrafficClassIndex"),
    (0, "Unisphere-Data-QoS-MIB", "usdQosTrafficClassGroupIndex"),
)
if mibBuilder.loadTexts:
    usdQosProfileElementEntry.setStatus("current")
_UsdQosProfileElementEntryRowStatus_Type = RowStatus
_UsdQosProfileElementEntryRowStatus_Object = MibTableColumn
usdQosProfileElementEntryRowStatus = _UsdQosProfileElementEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 1),
    _UsdQosProfileElementEntryRowStatus_Type()
)
usdQosProfileElementEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosProfileElementEntryRowStatus.setStatus("current")
_UsdQosProfileElementEntryQueueProfile_Type = Unsigned32
_UsdQosProfileElementEntryQueueProfile_Object = MibTableColumn
usdQosProfileElementEntryQueueProfile = _UsdQosProfileElementEntryQueueProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 2),
    _UsdQosProfileElementEntryQueueProfile_Type()
)
usdQosProfileElementEntryQueueProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosProfileElementEntryQueueProfile.setStatus("current")
_UsdQosProfileElementEntrySchedulerProfile_Type = Unsigned32
_UsdQosProfileElementEntrySchedulerProfile_Object = MibTableColumn
usdQosProfileElementEntrySchedulerProfile = _UsdQosProfileElementEntrySchedulerProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 3),
    _UsdQosProfileElementEntrySchedulerProfile_Type()
)
usdQosProfileElementEntrySchedulerProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosProfileElementEntrySchedulerProfile.setStatus("current")


class _UsdQosInterfaceType_Type(Integer32):
    """Custom type usdQosInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              9,
              11,
              13,
              16,
              31,
              35,
              36,
              150,
              151)
        )
    )
    namedValues = NamedValues(
        *(("atm", 9),
          ("atmVc", 11),
          ("cbf", 36),
          ("ethernet", 6),
          ("frVc", 16),
          ("ip", 0),
          ("ipTunnel", 151),
          ("l2tpTunnel", 150),
          ("serial", 13),
          ("serverPort", 31),
          ("vlan", 35))
    )


_UsdQosInterfaceType_Type.__name__ = "Integer32"
_UsdQosInterfaceType_Object = MibTableColumn
usdQosInterfaceType = _UsdQosInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 4),
    _UsdQosInterfaceType_Type()
)
usdQosInterfaceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdQosInterfaceType.setStatus("current")


class _UsdQosProfileEntryType_Type(Integer32):
    """Custom type usdQosProfileEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("schedulerProfile", 2),
          ("trafficClass", 1),
          ("trafficClassGroup", 3))
    )


_UsdQosProfileEntryType_Type.__name__ = "Integer32"
_UsdQosProfileEntryType_Object = MibTableColumn
usdQosProfileEntryType = _UsdQosProfileEntryType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 5),
    _UsdQosProfileEntryType_Type()
)
usdQosProfileEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdQosProfileEntryType.setStatus("current")
_UsdQosIfAttach_ObjectIdentity = ObjectIdentity
usdQosIfAttach = _UsdQosIfAttach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10)
)
_UsdQosIfAttachTable_Object = MibTable
usdQosIfAttachTable = _UsdQosIfAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10, 1)
)
if mibBuilder.loadTexts:
    usdQosIfAttachTable.setStatus("current")
_UsdQosIfAttachEntry_Object = MibTableRow
usdQosIfAttachEntry = _UsdQosIfAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10, 1, 1)
)
usdQosIfAttachEntry.setIndexNames(
    (0, "Unisphere-Data-QoS-MIB", "usdQosIfAttachIndex"),
)
if mibBuilder.loadTexts:
    usdQosIfAttachEntry.setStatus("current")
_UsdQosIfAttachIndex_Type = Unsigned32
_UsdQosIfAttachIndex_Object = MibTableColumn
usdQosIfAttachIndex = _UsdQosIfAttachIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10, 1, 1, 1),
    _UsdQosIfAttachIndex_Type()
)
usdQosIfAttachIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdQosIfAttachIndex.setStatus("current")
_UsdQosIfAttachRowStatus_Type = RowStatus
_UsdQosIfAttachRowStatus_Object = MibTableColumn
usdQosIfAttachRowStatus = _UsdQosIfAttachRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10, 1, 1, 2),
    _UsdQosIfAttachRowStatus_Type()
)
usdQosIfAttachRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosIfAttachRowStatus.setStatus("current")
_UsdQosIfAttachQosProfileIndex_Type = Unsigned32
_UsdQosIfAttachQosProfileIndex_Object = MibTableColumn
usdQosIfAttachQosProfileIndex = _UsdQosIfAttachQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10, 1, 1, 3),
    _UsdQosIfAttachQosProfileIndex_Type()
)
usdQosIfAttachQosProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosIfAttachQosProfileIndex.setStatus("current")
_UsdQosQosPortTypeProfile_ObjectIdentity = ObjectIdentity
usdQosQosPortTypeProfile = _UsdQosQosPortTypeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11)
)
_UsdQosQosPortTypeProfileTable_Object = MibTable
usdQosQosPortTypeProfileTable = _UsdQosQosPortTypeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11, 1)
)
if mibBuilder.loadTexts:
    usdQosQosPortTypeProfileTable.setStatus("current")
_UsdQosQosPortTypeProfileEntry_Object = MibTableRow
usdQosQosPortTypeProfileEntry = _UsdQosQosPortTypeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11, 1, 1)
)
usdQosQosPortTypeProfileEntry.setIndexNames(
    (0, "Unisphere-Data-QoS-MIB", "usdQosQosPortTypeProfileIndex"),
)
if mibBuilder.loadTexts:
    usdQosQosPortTypeProfileEntry.setStatus("current")


class _UsdQosQosPortTypeProfileIndex_Type(Integer32):
    """Custom type usdQosQosPortTypeProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              9,
              13,
              31)
        )
    )
    namedValues = NamedValues(
        *(("atm", 9),
          ("ethernet", 6),
          ("serial", 13),
          ("serverPort", 31))
    )


_UsdQosQosPortTypeProfileIndex_Type.__name__ = "Integer32"
_UsdQosQosPortTypeProfileIndex_Object = MibTableColumn
usdQosQosPortTypeProfileIndex = _UsdQosQosPortTypeProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11, 1, 1, 1),
    _UsdQosQosPortTypeProfileIndex_Type()
)
usdQosQosPortTypeProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdQosQosPortTypeProfileIndex.setStatus("current")
_UsdQosQosPortTypeProfileRowStatus_Type = RowStatus
_UsdQosQosPortTypeProfileRowStatus_Object = MibTableColumn
usdQosQosPortTypeProfileRowStatus = _UsdQosQosPortTypeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11, 1, 1, 2),
    _UsdQosQosPortTypeProfileRowStatus_Type()
)
usdQosQosPortTypeProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQosPortTypeProfileRowStatus.setStatus("current")
_UsdQosQosPortTypeProfileQosProfileIndex_Type = Unsigned32
_UsdQosQosPortTypeProfileQosProfileIndex_Object = MibTableColumn
usdQosQosPortTypeProfileQosProfileIndex = _UsdQosQosPortTypeProfileQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11, 1, 1, 3),
    _UsdQosQosPortTypeProfileQosProfileIndex_Type()
)
usdQosQosPortTypeProfileQosProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdQosQosPortTypeProfileQosProfileIndex.setStatus("current")
_UsdQosQueueStatistics_ObjectIdentity = ObjectIdentity
usdQosQueueStatistics = _UsdQosQueueStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12)
)
_UsdQosQueueStatisticsTable_Object = MibTable
usdQosQueueStatisticsTable = _UsdQosQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1)
)
if mibBuilder.loadTexts:
    usdQosQueueStatisticsTable.setStatus("current")
_UsdQosQueueStatisticsEntry_Object = MibTableRow
usdQosQueueStatisticsEntry = _UsdQosQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1)
)
usdQosQueueStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Unisphere-Data-QoS-MIB", "usdQosTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    usdQosQueueStatisticsEntry.setStatus("current")
_UsdQosOutPacketForwarded_Type = Counter64
_UsdQosOutPacketForwarded_Object = MibTableColumn
usdQosOutPacketForwarded = _UsdQosOutPacketForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 1),
    _UsdQosOutPacketForwarded_Type()
)
usdQosOutPacketForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosOutPacketForwarded.setStatus("current")
if mibBuilder.loadTexts:
    usdQosOutPacketForwarded.setUnits("packets")
_UsdQosOutBytesForwarded_Type = Counter64
_UsdQosOutBytesForwarded_Object = MibTableColumn
usdQosOutBytesForwarded = _UsdQosOutBytesForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 2),
    _UsdQosOutBytesForwarded_Type()
)
usdQosOutBytesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosOutBytesForwarded.setStatus("current")
if mibBuilder.loadTexts:
    usdQosOutBytesForwarded.setUnits("bytes")
_UsdQosOutGreenPacketsSchedulerDrops_Type = Counter64
_UsdQosOutGreenPacketsSchedulerDrops_Object = MibTableColumn
usdQosOutGreenPacketsSchedulerDrops = _UsdQosOutGreenPacketsSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 3),
    _UsdQosOutGreenPacketsSchedulerDrops_Type()
)
usdQosOutGreenPacketsSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosOutGreenPacketsSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    usdQosOutGreenPacketsSchedulerDrops.setUnits("packets")
_UsdQosOutYellowPacketsSchedulerDrops_Type = Counter64
_UsdQosOutYellowPacketsSchedulerDrops_Object = MibTableColumn
usdQosOutYellowPacketsSchedulerDrops = _UsdQosOutYellowPacketsSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 4),
    _UsdQosOutYellowPacketsSchedulerDrops_Type()
)
usdQosOutYellowPacketsSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosOutYellowPacketsSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    usdQosOutYellowPacketsSchedulerDrops.setUnits("packets")
_UsdQosOutRedPacketsSchedulerDrops_Type = Counter64
_UsdQosOutRedPacketsSchedulerDrops_Object = MibTableColumn
usdQosOutRedPacketsSchedulerDrops = _UsdQosOutRedPacketsSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 5),
    _UsdQosOutRedPacketsSchedulerDrops_Type()
)
usdQosOutRedPacketsSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosOutRedPacketsSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    usdQosOutRedPacketsSchedulerDrops.setUnits("packets")
_UsdQosOutGreenBytesSchedulerDrops_Type = Counter64
_UsdQosOutGreenBytesSchedulerDrops_Object = MibTableColumn
usdQosOutGreenBytesSchedulerDrops = _UsdQosOutGreenBytesSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 6),
    _UsdQosOutGreenBytesSchedulerDrops_Type()
)
usdQosOutGreenBytesSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosOutGreenBytesSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    usdQosOutGreenBytesSchedulerDrops.setUnits("bytes")
_UsdQosOutYellowBytesSchedulerDrops_Type = Counter64
_UsdQosOutYellowBytesSchedulerDrops_Object = MibTableColumn
usdQosOutYellowBytesSchedulerDrops = _UsdQosOutYellowBytesSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 7),
    _UsdQosOutYellowBytesSchedulerDrops_Type()
)
usdQosOutYellowBytesSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosOutYellowBytesSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    usdQosOutYellowBytesSchedulerDrops.setUnits("bytes")
_UsdQosOutRedBytesSchedulerDrops_Type = Counter64
_UsdQosOutRedBytesSchedulerDrops_Object = MibTableColumn
usdQosOutRedBytesSchedulerDrops = _UsdQosOutRedBytesSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 8),
    _UsdQosOutRedBytesSchedulerDrops_Type()
)
usdQosOutRedBytesSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdQosOutRedBytesSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    usdQosOutRedBytesSchedulerDrops.setUnits("bytes")
_UsdQosConformance_ObjectIdentity = ObjectIdentity
usdQosConformance = _UsdQosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2)
)
_UsdQosCompliances_ObjectIdentity = ObjectIdentity
usdQosCompliances = _UsdQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 1)
)
_UsdQosGroups_ObjectIdentity = ObjectIdentity
usdQosGroups = _UsdQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2)
)

# Managed Objects groups

usdQosCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 1)
)
usdQosCapabilityGroup.setObjects(
      *(("Unisphere-Data-QoS-MIB", "usdQosMaxTrafficClass"),
        ("Unisphere-Data-QoS-MIB", "usdQosMaxQueueLength"),
        ("Unisphere-Data-QoS-MIB", "usdQosMinSchedulerBurst"),
        ("Unisphere-Data-QoS-MIB", "usdQosMaxSchedulerBurst"))
)
if mibBuilder.loadTexts:
    usdQosCapabilityGroup.setStatus("current")

usdQosScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 2)
)
usdQosScalarGroup.setObjects(
      *(("Unisphere-Data-QoS-MIB", "usdQosTrafficClassCount"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileCount"),
        ("Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileCount"),
        ("Unisphere-Data-QoS-MIB", "usdQosProfileCount"),
        ("Unisphere-Data-QoS-MIB", "usdQosInterfaceCount"),
        ("Unisphere-Data-QoS-MIB", "usdQosQosPortTypeProfileCount"))
)
if mibBuilder.loadTexts:
    usdQosScalarGroup.setStatus("current")

usdQosTrafficClassListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 3)
)
usdQosTrafficClassListGroup.setObjects(
      *(("Unisphere-Data-QoS-MIB", "usdQosTrafficClassNextIndex"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassRowStatus"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassName"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassWeight"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassStrictPriority"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassUpdatePending"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassUpdateNow"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassIsReferencedByGroup"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassIsReferencedByQosProfile"))
)
if mibBuilder.loadTexts:
    usdQosTrafficClassListGroup.setStatus("current")

usdQosTrafficClassGroupListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 4)
)
usdQosTrafficClassGroupListGroup.setObjects(
      *(("Unisphere-Data-QoS-MIB", "usdQosTrafficClassGroupNextIndex"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassGroupRowStatus"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassGroupName"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassGroupUpdatePending"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassGroupUpdateNow"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassGroupIsReferencedByQosProfile"),
        ("Unisphere-Data-QoS-MIB", "usdQosTrafficClassGroupEntryRowStatus"))
)
if mibBuilder.loadTexts:
    usdQosTrafficClassGroupListGroup.setStatus("current")

usdQosQueueProfileListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 5)
)
usdQosQueueProfileListGroup.setObjects(
      *(("Unisphere-Data-QoS-MIB", "usdQosQueueProfileNextIndex"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileRowStatus"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileName"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileCommittedMinLength"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileCommittedMaxLength"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileConformedMinLength"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileConformedMaxLength"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileExceededMinLength"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileExceededMaxLength"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileConformedFraction"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileExceededFraction"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileCommittedDropThreshold"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileCommittedDropRate"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileConformedDropThreshold"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileConformedDropRate"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileExceededDropThreshold"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileExceededDropRate"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileBufferWeight"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileUpdatePending"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileUpdateNow"),
        ("Unisphere-Data-QoS-MIB", "usdQosQueueProfileIsReferencedByQosProfile"))
)
if mibBuilder.loadTexts:
    usdQosQueueProfileListGroup.setStatus("current")

usdQosSchedulerProfileListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 6)
)
usdQosSchedulerProfileListGroup.setObjects(
      *(("Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileNextIndex"),
        ("Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileRowStatus"),
        ("Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileName"),
        ("Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileShapingRate"),
        ("Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileBurst"),
        ("Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileWeight"),
        ("Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileStrictPriority"),
        ("Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileUpdatePending"),
        ("Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileUpdateNow"),
        ("Unisphere-Data-QoS-MIB", "usdQosSchedulerProfileIsReferencedByQosProfile"))
)
if mibBuilder.loadTexts:
    usdQosSchedulerProfileListGroup.setStatus("current")

usdQosProfileListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 7)
)
usdQosProfileListGroup.setObjects(
      *(("Unisphere-Data-QoS-MIB", "usdQosProfileNextIndex"),
        ("Unisphere-Data-QoS-MIB", "usdQosProfileRowStatus"),
        ("Unisphere-Data-QoS-MIB", "usdQosProfileName"),
        ("Unisphere-Data-QoS-MIB", "usdQosProfileUpdatePending"),
        ("Unisphere-Data-QoS-MIB", "usdQosProfileUpdateNow"),
        ("Unisphere-Data-QoS-MIB", "usdQosProfileIsReferencedByInterfaceQosAttachment"),
        ("Unisphere-Data-QoS-MIB", "usdQosProfileIsReferencedByQosPortTypeProfile"))
)
if mibBuilder.loadTexts:
    usdQosProfileListGroup.setStatus("current")

usdQosProfileElementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 8)
)
usdQosProfileElementGroup.setObjects(
      *(("Unisphere-Data-QoS-MIB", "usdQosProfileElementEntryRowStatus"),
        ("Unisphere-Data-QoS-MIB", "usdQosProfileElementEntryQueueProfile"),
        ("Unisphere-Data-QoS-MIB", "usdQosProfileElementEntrySchedulerProfile"))
)
if mibBuilder.loadTexts:
    usdQosProfileElementGroup.setStatus("current")

usdQosIfAttachGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 9)
)
usdQosIfAttachGroup.setObjects(
      *(("Unisphere-Data-QoS-MIB", "usdQosIfAttachRowStatus"),
        ("Unisphere-Data-QoS-MIB", "usdQosIfAttachQosProfileIndex"))
)
if mibBuilder.loadTexts:
    usdQosIfAttachGroup.setStatus("current")

usdQosQosPortTypeProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 10)
)
usdQosQosPortTypeProfileGroup.setObjects(
      *(("Unisphere-Data-QoS-MIB", "usdQosQosPortTypeProfileRowStatus"),
        ("Unisphere-Data-QoS-MIB", "usdQosQosPortTypeProfileQosProfileIndex"))
)
if mibBuilder.loadTexts:
    usdQosQosPortTypeProfileGroup.setStatus("current")

usdQosQueueStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 11)
)
usdQosQueueStatisticsGroup.setObjects(
      *(("Unisphere-Data-QoS-MIB", "usdQosOutPacketForwarded"),
        ("Unisphere-Data-QoS-MIB", "usdQosOutBytesForwarded"),
        ("Unisphere-Data-QoS-MIB", "usdQosOutGreenPacketsSchedulerDrops"),
        ("Unisphere-Data-QoS-MIB", "usdQosOutYellowPacketsSchedulerDrops"),
        ("Unisphere-Data-QoS-MIB", "usdQosOutRedPacketsSchedulerDrops"),
        ("Unisphere-Data-QoS-MIB", "usdQosOutGreenBytesSchedulerDrops"),
        ("Unisphere-Data-QoS-MIB", "usdQosOutYellowBytesSchedulerDrops"),
        ("Unisphere-Data-QoS-MIB", "usdQosOutRedBytesSchedulerDrops"))
)
if mibBuilder.loadTexts:
    usdQosQueueStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdQosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-QoS-MIB",
    **{"usdQosMIB": usdQosMIB,
       "usdQosObjects": usdQosObjects,
       "usdQosCapability": usdQosCapability,
       "usdQosMaxTrafficClass": usdQosMaxTrafficClass,
       "usdQosMaxQueueLength": usdQosMaxQueueLength,
       "usdQosMinSchedulerBurst": usdQosMinSchedulerBurst,
       "usdQosMaxSchedulerBurst": usdQosMaxSchedulerBurst,
       "usdQos": usdQos,
       "usdQosTrafficClassCount": usdQosTrafficClassCount,
       "usdQosQueueProfileCount": usdQosQueueProfileCount,
       "usdQosSchedulerProfileCount": usdQosSchedulerProfileCount,
       "usdQosProfileCount": usdQosProfileCount,
       "usdQosInterfaceCount": usdQosInterfaceCount,
       "usdQosQosPortTypeProfileCount": usdQosQosPortTypeProfileCount,
       "usdQosTrafficClassList": usdQosTrafficClassList,
       "usdQosTrafficClassNextIndex": usdQosTrafficClassNextIndex,
       "usdQosTrafficClassTable": usdQosTrafficClassTable,
       "usdQosTrafficClassEntry": usdQosTrafficClassEntry,
       "usdQosTrafficClassIndex": usdQosTrafficClassIndex,
       "usdQosTrafficClassRowStatus": usdQosTrafficClassRowStatus,
       "usdQosTrafficClassName": usdQosTrafficClassName,
       "usdQosTrafficClassWeight": usdQosTrafficClassWeight,
       "usdQosTrafficClassStrictPriority": usdQosTrafficClassStrictPriority,
       "usdQosTrafficClassUpdatePending": usdQosTrafficClassUpdatePending,
       "usdQosTrafficClassUpdateNow": usdQosTrafficClassUpdateNow,
       "usdQosTrafficClassIsReferencedByGroup": usdQosTrafficClassIsReferencedByGroup,
       "usdQosTrafficClassIsReferencedByQosProfile": usdQosTrafficClassIsReferencedByQosProfile,
       "usdQosTrafficClassGroupList": usdQosTrafficClassGroupList,
       "usdQosTrafficClassGroupNextIndex": usdQosTrafficClassGroupNextIndex,
       "usdQosTrafficClassGroupTable": usdQosTrafficClassGroupTable,
       "usdQosTrafficClassGroupEntry": usdQosTrafficClassGroupEntry,
       "usdQosTrafficClassGroupIndex": usdQosTrafficClassGroupIndex,
       "usdQosTrafficClassGroupRowStatus": usdQosTrafficClassGroupRowStatus,
       "usdQosTrafficClassGroupName": usdQosTrafficClassGroupName,
       "usdQosTrafficClassGroupUpdatePending": usdQosTrafficClassGroupUpdatePending,
       "usdQosTrafficClassGroupUpdateNow": usdQosTrafficClassGroupUpdateNow,
       "usdQosTrafficClassGroupIsReferencedByQosProfile": usdQosTrafficClassGroupIsReferencedByQosProfile,
       "usdQosTrafficClassGroupEntryList": usdQosTrafficClassGroupEntryList,
       "usdQosTrafficClassGroupEntryTable": usdQosTrafficClassGroupEntryTable,
       "usdQosTrafficClassGroupEntryEntry": usdQosTrafficClassGroupEntryEntry,
       "usdQosTrafficClassGroupEntryRowStatus": usdQosTrafficClassGroupEntryRowStatus,
       "usdQosSchedulerProfileList": usdQosSchedulerProfileList,
       "usdQosSchedulerProfileNextIndex": usdQosSchedulerProfileNextIndex,
       "usdQosSchedulerProfileTable": usdQosSchedulerProfileTable,
       "usdQosSchedulerProfileEntry": usdQosSchedulerProfileEntry,
       "usdQosSchedulerProfileIndex": usdQosSchedulerProfileIndex,
       "usdQosSchedulerProfileRowStatus": usdQosSchedulerProfileRowStatus,
       "usdQosSchedulerProfileName": usdQosSchedulerProfileName,
       "usdQosSchedulerProfileShapingRate": usdQosSchedulerProfileShapingRate,
       "usdQosSchedulerProfileBurst": usdQosSchedulerProfileBurst,
       "usdQosSchedulerProfileWeight": usdQosSchedulerProfileWeight,
       "usdQosSchedulerProfileStrictPriority": usdQosSchedulerProfileStrictPriority,
       "usdQosSchedulerProfileUpdatePending": usdQosSchedulerProfileUpdatePending,
       "usdQosSchedulerProfileUpdateNow": usdQosSchedulerProfileUpdateNow,
       "usdQosSchedulerProfileIsReferencedByQosProfile": usdQosSchedulerProfileIsReferencedByQosProfile,
       "usdQosQueueProfileList": usdQosQueueProfileList,
       "usdQosQueueProfileNextIndex": usdQosQueueProfileNextIndex,
       "usdQosQueueProfileTable": usdQosQueueProfileTable,
       "usdQosQueueProfileEntry": usdQosQueueProfileEntry,
       "usdQosQueueProfileIndex": usdQosQueueProfileIndex,
       "usdQosQueueProfileRowStatus": usdQosQueueProfileRowStatus,
       "usdQosQueueProfileName": usdQosQueueProfileName,
       "usdQosQueueProfileCommittedMinLength": usdQosQueueProfileCommittedMinLength,
       "usdQosQueueProfileCommittedMaxLength": usdQosQueueProfileCommittedMaxLength,
       "usdQosQueueProfileConformedMinLength": usdQosQueueProfileConformedMinLength,
       "usdQosQueueProfileConformedMaxLength": usdQosQueueProfileConformedMaxLength,
       "usdQosQueueProfileExceededMinLength": usdQosQueueProfileExceededMinLength,
       "usdQosQueueProfileExceededMaxLength": usdQosQueueProfileExceededMaxLength,
       "usdQosQueueProfileConformedFraction": usdQosQueueProfileConformedFraction,
       "usdQosQueueProfileExceededFraction": usdQosQueueProfileExceededFraction,
       "usdQosQueueProfileCommittedDropThreshold": usdQosQueueProfileCommittedDropThreshold,
       "usdQosQueueProfileCommittedDropRate": usdQosQueueProfileCommittedDropRate,
       "usdQosQueueProfileConformedDropThreshold": usdQosQueueProfileConformedDropThreshold,
       "usdQosQueueProfileConformedDropRate": usdQosQueueProfileConformedDropRate,
       "usdQosQueueProfileExceededDropThreshold": usdQosQueueProfileExceededDropThreshold,
       "usdQosQueueProfileExceededDropRate": usdQosQueueProfileExceededDropRate,
       "usdQosQueueProfileBufferWeight": usdQosQueueProfileBufferWeight,
       "usdQosQueueProfileUpdatePending": usdQosQueueProfileUpdatePending,
       "usdQosQueueProfileUpdateNow": usdQosQueueProfileUpdateNow,
       "usdQosQueueProfileIsReferencedByQosProfile": usdQosQueueProfileIsReferencedByQosProfile,
       "usdQosProfile": usdQosProfile,
       "usdQosProfileNextIndex": usdQosProfileNextIndex,
       "usdQosProfileTable": usdQosProfileTable,
       "usdQosProfileEntry": usdQosProfileEntry,
       "usdQosProfileIndex": usdQosProfileIndex,
       "usdQosProfileRowStatus": usdQosProfileRowStatus,
       "usdQosProfileName": usdQosProfileName,
       "usdQosProfileUpdatePending": usdQosProfileUpdatePending,
       "usdQosProfileUpdateNow": usdQosProfileUpdateNow,
       "usdQosProfileIsReferencedByInterfaceQosAttachment": usdQosProfileIsReferencedByInterfaceQosAttachment,
       "usdQosProfileIsReferencedByQosPortTypeProfile": usdQosProfileIsReferencedByQosPortTypeProfile,
       "usdQosProfileElement": usdQosProfileElement,
       "usdQosProfileElementTable": usdQosProfileElementTable,
       "usdQosProfileElementEntry": usdQosProfileElementEntry,
       "usdQosProfileElementEntryRowStatus": usdQosProfileElementEntryRowStatus,
       "usdQosProfileElementEntryQueueProfile": usdQosProfileElementEntryQueueProfile,
       "usdQosProfileElementEntrySchedulerProfile": usdQosProfileElementEntrySchedulerProfile,
       "usdQosInterfaceType": usdQosInterfaceType,
       "usdQosProfileEntryType": usdQosProfileEntryType,
       "usdQosIfAttach": usdQosIfAttach,
       "usdQosIfAttachTable": usdQosIfAttachTable,
       "usdQosIfAttachEntry": usdQosIfAttachEntry,
       "usdQosIfAttachIndex": usdQosIfAttachIndex,
       "usdQosIfAttachRowStatus": usdQosIfAttachRowStatus,
       "usdQosIfAttachQosProfileIndex": usdQosIfAttachQosProfileIndex,
       "usdQosQosPortTypeProfile": usdQosQosPortTypeProfile,
       "usdQosQosPortTypeProfileTable": usdQosQosPortTypeProfileTable,
       "usdQosQosPortTypeProfileEntry": usdQosQosPortTypeProfileEntry,
       "usdQosQosPortTypeProfileIndex": usdQosQosPortTypeProfileIndex,
       "usdQosQosPortTypeProfileRowStatus": usdQosQosPortTypeProfileRowStatus,
       "usdQosQosPortTypeProfileQosProfileIndex": usdQosQosPortTypeProfileQosProfileIndex,
       "usdQosQueueStatistics": usdQosQueueStatistics,
       "usdQosQueueStatisticsTable": usdQosQueueStatisticsTable,
       "usdQosQueueStatisticsEntry": usdQosQueueStatisticsEntry,
       "usdQosOutPacketForwarded": usdQosOutPacketForwarded,
       "usdQosOutBytesForwarded": usdQosOutBytesForwarded,
       "usdQosOutGreenPacketsSchedulerDrops": usdQosOutGreenPacketsSchedulerDrops,
       "usdQosOutYellowPacketsSchedulerDrops": usdQosOutYellowPacketsSchedulerDrops,
       "usdQosOutRedPacketsSchedulerDrops": usdQosOutRedPacketsSchedulerDrops,
       "usdQosOutGreenBytesSchedulerDrops": usdQosOutGreenBytesSchedulerDrops,
       "usdQosOutYellowBytesSchedulerDrops": usdQosOutYellowBytesSchedulerDrops,
       "usdQosOutRedBytesSchedulerDrops": usdQosOutRedBytesSchedulerDrops,
       "usdQosConformance": usdQosConformance,
       "usdQosCompliances": usdQosCompliances,
       "usdQosCompliance": usdQosCompliance,
       "usdQosGroups": usdQosGroups,
       "usdQosCapabilityGroup": usdQosCapabilityGroup,
       "usdQosScalarGroup": usdQosScalarGroup,
       "usdQosTrafficClassListGroup": usdQosTrafficClassListGroup,
       "usdQosTrafficClassGroupListGroup": usdQosTrafficClassGroupListGroup,
       "usdQosQueueProfileListGroup": usdQosQueueProfileListGroup,
       "usdQosSchedulerProfileListGroup": usdQosSchedulerProfileListGroup,
       "usdQosProfileListGroup": usdQosProfileListGroup,
       "usdQosProfileElementGroup": usdQosProfileElementGroup,
       "usdQosIfAttachGroup": usdQosIfAttachGroup,
       "usdQosQosPortTypeProfileGroup": usdQosQosPortTypeProfileGroup,
       "usdQosQueueStatisticsGroup": usdQosQueueStatisticsGroup}
)

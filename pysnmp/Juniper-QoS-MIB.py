# SNMP MIB module (Juniper-QoS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-QoS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:07 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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

juniQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57)
)
juniQosMIB.setRevisions(
        ("2005-07-06 14:18",
         "2005-04-01 19:00",
         "2004-12-10 19:16",
         "2004-01-26 14:19",
         "2003-11-04 20:10",
         "2003-05-08 17:05",
         "2003-03-13 18:17",
         "2003-03-12 18:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniQosLogicalInterfaceType(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JuniQosObjects_ObjectIdentity = ObjectIdentity
juniQosObjects = _JuniQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1)
)
_JuniQosCapability_ObjectIdentity = ObjectIdentity
juniQosCapability = _JuniQosCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 1)
)
_JuniQosMaxTrafficClass_Type = Unsigned32
_JuniQosMaxTrafficClass_Object = MibScalar
juniQosMaxTrafficClass = _JuniQosMaxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 1, 1),
    _JuniQosMaxTrafficClass_Type()
)
juniQosMaxTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosMaxTrafficClass.setStatus("current")
_JuniQosMaxQueueLength_Type = Unsigned32
_JuniQosMaxQueueLength_Object = MibScalar
juniQosMaxQueueLength = _JuniQosMaxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 1, 2),
    _JuniQosMaxQueueLength_Type()
)
juniQosMaxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosMaxQueueLength.setStatus("current")
if mibBuilder.loadTexts:
    juniQosMaxQueueLength.setUnits("bytes")
_JuniQosMinSchedulerBurst_Type = Unsigned32
_JuniQosMinSchedulerBurst_Object = MibScalar
juniQosMinSchedulerBurst = _JuniQosMinSchedulerBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 1, 3),
    _JuniQosMinSchedulerBurst_Type()
)
juniQosMinSchedulerBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosMinSchedulerBurst.setStatus("current")
if mibBuilder.loadTexts:
    juniQosMinSchedulerBurst.setUnits("bytes")
_JuniQosMaxSchedulerBurst_Type = Unsigned32
_JuniQosMaxSchedulerBurst_Object = MibScalar
juniQosMaxSchedulerBurst = _JuniQosMaxSchedulerBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 1, 4),
    _JuniQosMaxSchedulerBurst_Type()
)
juniQosMaxSchedulerBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosMaxSchedulerBurst.setStatus("current")
if mibBuilder.loadTexts:
    juniQosMaxSchedulerBurst.setUnits("bytes")
_JuniQosMaxQosProfileRules_Type = Unsigned32
_JuniQosMaxQosProfileRules_Object = MibScalar
juniQosMaxQosProfileRules = _JuniQosMaxQosProfileRules_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 1, 5),
    _JuniQosMaxQosProfileRules_Type()
)
juniQosMaxQosProfileRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosMaxQosProfileRules.setStatus("current")
_JuniQos_ObjectIdentity = ObjectIdentity
juniQos = _JuniQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2)
)
_JuniQosTrafficClassCount_Type = Gauge32
_JuniQosTrafficClassCount_Object = MibScalar
juniQosTrafficClassCount = _JuniQosTrafficClassCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 1),
    _JuniQosTrafficClassCount_Type()
)
juniQosTrafficClassCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosTrafficClassCount.setStatus("current")
_JuniQosQueueProfileCount_Type = Gauge32
_JuniQosQueueProfileCount_Object = MibScalar
juniQosQueueProfileCount = _JuniQosQueueProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 2),
    _JuniQosQueueProfileCount_Type()
)
juniQosQueueProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosQueueProfileCount.setStatus("current")
_JuniQosSchedulerProfileCount_Type = Gauge32
_JuniQosSchedulerProfileCount_Object = MibScalar
juniQosSchedulerProfileCount = _JuniQosSchedulerProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 3),
    _JuniQosSchedulerProfileCount_Type()
)
juniQosSchedulerProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileCount.setStatus("current")
_JuniQosProfileCount_Type = Gauge32
_JuniQosProfileCount_Object = MibScalar
juniQosProfileCount = _JuniQosProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 4),
    _JuniQosProfileCount_Type()
)
juniQosProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosProfileCount.setStatus("current")
_JuniQosInterfaceCount_Type = Gauge32
_JuniQosInterfaceCount_Object = MibScalar
juniQosInterfaceCount = _JuniQosInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 5),
    _JuniQosInterfaceCount_Type()
)
juniQosInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosInterfaceCount.setStatus("current")
_JuniQosQosPortTypeProfileCount_Type = Gauge32
_JuniQosQosPortTypeProfileCount_Object = MibScalar
juniQosQosPortTypeProfileCount = _JuniQosQosPortTypeProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 6),
    _JuniQosQosPortTypeProfileCount_Type()
)
juniQosQosPortTypeProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosQosPortTypeProfileCount.setStatus("current")
_JuniQosDropProfileCount_Type = Gauge32
_JuniQosDropProfileCount_Object = MibScalar
juniQosDropProfileCount = _JuniQosDropProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 7),
    _JuniQosDropProfileCount_Type()
)
juniQosDropProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosDropProfileCount.setStatus("current")
_JuniQosStatisticsProfileCount_Type = Gauge32
_JuniQosStatisticsProfileCount_Object = MibScalar
juniQosStatisticsProfileCount = _JuniQosStatisticsProfileCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 2, 8),
    _JuniQosStatisticsProfileCount_Type()
)
juniQosStatisticsProfileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileCount.setStatus("current")
_JuniQosTrafficClassList_ObjectIdentity = ObjectIdentity
juniQosTrafficClassList = _JuniQosTrafficClassList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3)
)
_JuniQosTrafficClassNextIndex_Type = Unsigned32
_JuniQosTrafficClassNextIndex_Object = MibScalar
juniQosTrafficClassNextIndex = _JuniQosTrafficClassNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 1),
    _JuniQosTrafficClassNextIndex_Type()
)
juniQosTrafficClassNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosTrafficClassNextIndex.setStatus("current")
_JuniQosTrafficClassTable_Object = MibTable
juniQosTrafficClassTable = _JuniQosTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2)
)
if mibBuilder.loadTexts:
    juniQosTrafficClassTable.setStatus("current")
_JuniQosTrafficClassEntry_Object = MibTableRow
juniQosTrafficClassEntry = _JuniQosTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1)
)
juniQosTrafficClassEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    juniQosTrafficClassEntry.setStatus("current")
_JuniQosTrafficClassIndex_Type = Unsigned32
_JuniQosTrafficClassIndex_Object = MibTableColumn
juniQosTrafficClassIndex = _JuniQosTrafficClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 1),
    _JuniQosTrafficClassIndex_Type()
)
juniQosTrafficClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosTrafficClassIndex.setStatus("current")
_JuniQosTrafficClassRowStatus_Type = RowStatus
_JuniQosTrafficClassRowStatus_Object = MibTableColumn
juniQosTrafficClassRowStatus = _JuniQosTrafficClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 2),
    _JuniQosTrafficClassRowStatus_Type()
)
juniQosTrafficClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosTrafficClassRowStatus.setStatus("current")


class _JuniQosTrafficClassName_Type(DisplayString):
    """Custom type juniQosTrafficClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniQosTrafficClassName_Type.__name__ = "DisplayString"
_JuniQosTrafficClassName_Object = MibTableColumn
juniQosTrafficClassName = _JuniQosTrafficClassName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 3),
    _JuniQosTrafficClassName_Type()
)
juniQosTrafficClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosTrafficClassName.setStatus("current")


class _JuniQosTrafficClassWeight_Type(Unsigned32):
    """Custom type juniQosTrafficClassWeight based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_JuniQosTrafficClassWeight_Type.__name__ = "Unsigned32"
_JuniQosTrafficClassWeight_Object = MibTableColumn
juniQosTrafficClassWeight = _JuniQosTrafficClassWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 4),
    _JuniQosTrafficClassWeight_Type()
)
juniQosTrafficClassWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosTrafficClassWeight.setStatus("current")


class _JuniQosTrafficClassStrictPriority_Type(TruthValue):
    """Custom type juniQosTrafficClassStrictPriority based on TruthValue"""


_JuniQosTrafficClassStrictPriority_Object = MibTableColumn
juniQosTrafficClassStrictPriority = _JuniQosTrafficClassStrictPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 5),
    _JuniQosTrafficClassStrictPriority_Type()
)
juniQosTrafficClassStrictPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosTrafficClassStrictPriority.setStatus("current")
_JuniQosTrafficClassUpdatePending_Type = TruthValue
_JuniQosTrafficClassUpdatePending_Object = MibTableColumn
juniQosTrafficClassUpdatePending = _JuniQosTrafficClassUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 6),
    _JuniQosTrafficClassUpdatePending_Type()
)
juniQosTrafficClassUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosTrafficClassUpdatePending.setStatus("current")


class _JuniQosTrafficClassUpdateNow_Type(TruthValue):
    """Custom type juniQosTrafficClassUpdateNow based on TruthValue"""


_JuniQosTrafficClassUpdateNow_Object = MibTableColumn
juniQosTrafficClassUpdateNow = _JuniQosTrafficClassUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 7),
    _JuniQosTrafficClassUpdateNow_Type()
)
juniQosTrafficClassUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosTrafficClassUpdateNow.setStatus("current")
_JuniQosTrafficClassIsReferencedByGroup_Type = TruthValue
_JuniQosTrafficClassIsReferencedByGroup_Object = MibTableColumn
juniQosTrafficClassIsReferencedByGroup = _JuniQosTrafficClassIsReferencedByGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 8),
    _JuniQosTrafficClassIsReferencedByGroup_Type()
)
juniQosTrafficClassIsReferencedByGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosTrafficClassIsReferencedByGroup.setStatus("current")
_JuniQosTrafficClassIsReferencedByQosProfile_Type = TruthValue
_JuniQosTrafficClassIsReferencedByQosProfile_Object = MibTableColumn
juniQosTrafficClassIsReferencedByQosProfile = _JuniQosTrafficClassIsReferencedByQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 3, 2, 1, 9),
    _JuniQosTrafficClassIsReferencedByQosProfile_Type()
)
juniQosTrafficClassIsReferencedByQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosTrafficClassIsReferencedByQosProfile.setStatus("current")
_JuniQosTrafficClassGroupList_ObjectIdentity = ObjectIdentity
juniQosTrafficClassGroupList = _JuniQosTrafficClassGroupList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4)
)
_JuniQosTrafficClassGroupNextIndex_Type = Unsigned32
_JuniQosTrafficClassGroupNextIndex_Object = MibScalar
juniQosTrafficClassGroupNextIndex = _JuniQosTrafficClassGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 1),
    _JuniQosTrafficClassGroupNextIndex_Type()
)
juniQosTrafficClassGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupNextIndex.setStatus("current")
_JuniQosTrafficClassGroupTable_Object = MibTable
juniQosTrafficClassGroupTable = _JuniQosTrafficClassGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2)
)
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupTable.setStatus("current")
_JuniQosTrafficClassGroupEntry_Object = MibTableRow
juniQosTrafficClassGroupEntry = _JuniQosTrafficClassGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1)
)
juniQosTrafficClassGroupEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosTrafficClassGroupIndex"),
)
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupEntry.setStatus("current")
_JuniQosTrafficClassGroupIndex_Type = Unsigned32
_JuniQosTrafficClassGroupIndex_Object = MibTableColumn
juniQosTrafficClassGroupIndex = _JuniQosTrafficClassGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 1),
    _JuniQosTrafficClassGroupIndex_Type()
)
juniQosTrafficClassGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupIndex.setStatus("current")
_JuniQosTrafficClassGroupRowStatus_Type = RowStatus
_JuniQosTrafficClassGroupRowStatus_Object = MibTableColumn
juniQosTrafficClassGroupRowStatus = _JuniQosTrafficClassGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 2),
    _JuniQosTrafficClassGroupRowStatus_Type()
)
juniQosTrafficClassGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupRowStatus.setStatus("current")


class _JuniQosTrafficClassGroupName_Type(DisplayString):
    """Custom type juniQosTrafficClassGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniQosTrafficClassGroupName_Type.__name__ = "DisplayString"
_JuniQosTrafficClassGroupName_Object = MibTableColumn
juniQosTrafficClassGroupName = _JuniQosTrafficClassGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 3),
    _JuniQosTrafficClassGroupName_Type()
)
juniQosTrafficClassGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupName.setStatus("current")
_JuniQosTrafficClassGroupUpdatePending_Type = TruthValue
_JuniQosTrafficClassGroupUpdatePending_Object = MibTableColumn
juniQosTrafficClassGroupUpdatePending = _JuniQosTrafficClassGroupUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 4),
    _JuniQosTrafficClassGroupUpdatePending_Type()
)
juniQosTrafficClassGroupUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupUpdatePending.setStatus("current")


class _JuniQosTrafficClassGroupUpdateNow_Type(TruthValue):
    """Custom type juniQosTrafficClassGroupUpdateNow based on TruthValue"""


_JuniQosTrafficClassGroupUpdateNow_Object = MibTableColumn
juniQosTrafficClassGroupUpdateNow = _JuniQosTrafficClassGroupUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 5),
    _JuniQosTrafficClassGroupUpdateNow_Type()
)
juniQosTrafficClassGroupUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupUpdateNow.setStatus("current")
_JuniQosTrafficClassGroupIsReferencedByQosProfile_Type = TruthValue
_JuniQosTrafficClassGroupIsReferencedByQosProfile_Object = MibTableColumn
juniQosTrafficClassGroupIsReferencedByQosProfile = _JuniQosTrafficClassGroupIsReferencedByQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 6),
    _JuniQosTrafficClassGroupIsReferencedByQosProfile_Type()
)
juniQosTrafficClassGroupIsReferencedByQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupIsReferencedByQosProfile.setStatus("current")


class _JuniQosTrafficClassGroupSlotNumber_Type(Integer32):
    """Custom type juniQosTrafficClassGroupSlotNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_JuniQosTrafficClassGroupSlotNumber_Type.__name__ = "Integer32"
_JuniQosTrafficClassGroupSlotNumber_Object = MibTableColumn
juniQosTrafficClassGroupSlotNumber = _JuniQosTrafficClassGroupSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 7),
    _JuniQosTrafficClassGroupSlotNumber_Type()
)
juniQosTrafficClassGroupSlotNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupSlotNumber.setStatus("current")


class _JuniQosTrafficClassGroupExtendedGroup_Type(TruthValue):
    """Custom type juniQosTrafficClassGroupExtendedGroup based on TruthValue"""


_JuniQosTrafficClassGroupExtendedGroup_Object = MibTableColumn
juniQosTrafficClassGroupExtendedGroup = _JuniQosTrafficClassGroupExtendedGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 4, 2, 1, 8),
    _JuniQosTrafficClassGroupExtendedGroup_Type()
)
juniQosTrafficClassGroupExtendedGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupExtendedGroup.setStatus("current")
_JuniQosTrafficClassGroupEntryList_ObjectIdentity = ObjectIdentity
juniQosTrafficClassGroupEntryList = _JuniQosTrafficClassGroupEntryList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 5)
)
_JuniQosTrafficClassGroupEntryTable_Object = MibTable
juniQosTrafficClassGroupEntryTable = _JuniQosTrafficClassGroupEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 5, 1)
)
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupEntryTable.setStatus("current")
_JuniQosTrafficClassGroupEntryEntry_Object = MibTableRow
juniQosTrafficClassGroupEntryEntry = _JuniQosTrafficClassGroupEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 5, 1, 1)
)
juniQosTrafficClassGroupEntryEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosTrafficClassGroupIndex"),
    (0, "Juniper-QoS-MIB", "juniQosTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupEntryEntry.setStatus("current")
_JuniQosTrafficClassGroupEntryRowStatus_Type = RowStatus
_JuniQosTrafficClassGroupEntryRowStatus_Object = MibTableColumn
juniQosTrafficClassGroupEntryRowStatus = _JuniQosTrafficClassGroupEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 5, 1, 1, 1),
    _JuniQosTrafficClassGroupEntryRowStatus_Type()
)
juniQosTrafficClassGroupEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupEntryRowStatus.setStatus("current")
_JuniQosSchedulerProfileList_ObjectIdentity = ObjectIdentity
juniQosSchedulerProfileList = _JuniQosSchedulerProfileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6)
)
_JuniQosSchedulerProfileNextIndex_Type = Unsigned32
_JuniQosSchedulerProfileNextIndex_Object = MibScalar
juniQosSchedulerProfileNextIndex = _JuniQosSchedulerProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 1),
    _JuniQosSchedulerProfileNextIndex_Type()
)
juniQosSchedulerProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileNextIndex.setStatus("current")
_JuniQosSchedulerProfileTable_Object = MibTable
juniQosSchedulerProfileTable = _JuniQosSchedulerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2)
)
if mibBuilder.loadTexts:
    juniQosSchedulerProfileTable.setStatus("current")
_JuniQosSchedulerProfileEntry_Object = MibTableRow
juniQosSchedulerProfileEntry = _JuniQosSchedulerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1)
)
juniQosSchedulerProfileEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosSchedulerProfileIndex"),
)
if mibBuilder.loadTexts:
    juniQosSchedulerProfileEntry.setStatus("current")
_JuniQosSchedulerProfileIndex_Type = Unsigned32
_JuniQosSchedulerProfileIndex_Object = MibTableColumn
juniQosSchedulerProfileIndex = _JuniQosSchedulerProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 1),
    _JuniQosSchedulerProfileIndex_Type()
)
juniQosSchedulerProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileIndex.setStatus("current")
_JuniQosSchedulerProfileRowStatus_Type = RowStatus
_JuniQosSchedulerProfileRowStatus_Object = MibTableColumn
juniQosSchedulerProfileRowStatus = _JuniQosSchedulerProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 2),
    _JuniQosSchedulerProfileRowStatus_Type()
)
juniQosSchedulerProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileRowStatus.setStatus("current")


class _JuniQosSchedulerProfileName_Type(DisplayString):
    """Custom type juniQosSchedulerProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniQosSchedulerProfileName_Type.__name__ = "DisplayString"
_JuniQosSchedulerProfileName_Object = MibTableColumn
juniQosSchedulerProfileName = _JuniQosSchedulerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 3),
    _JuniQosSchedulerProfileName_Type()
)
juniQosSchedulerProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileName.setStatus("current")


class _JuniQosSchedulerProfileShapingRate_Type(Unsigned32):
    """Custom type juniQosSchedulerProfileShapingRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_JuniQosSchedulerProfileShapingRate_Type.__name__ = "Unsigned32"
_JuniQosSchedulerProfileShapingRate_Object = MibTableColumn
juniQosSchedulerProfileShapingRate = _JuniQosSchedulerProfileShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 4),
    _JuniQosSchedulerProfileShapingRate_Type()
)
juniQosSchedulerProfileShapingRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileShapingRate.setStatus("current")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileShapingRate.setUnits("bps")


class _JuniQosSchedulerProfileBurst_Type(Unsigned32):
    """Custom type juniQosSchedulerProfileBurst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 522240),
    )


_JuniQosSchedulerProfileBurst_Type.__name__ = "Unsigned32"
_JuniQosSchedulerProfileBurst_Object = MibTableColumn
juniQosSchedulerProfileBurst = _JuniQosSchedulerProfileBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 5),
    _JuniQosSchedulerProfileBurst_Type()
)
juniQosSchedulerProfileBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileBurst.setStatus("current")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileBurst.setUnits("bytes")


class _JuniQosSchedulerProfileWeight_Type(Unsigned32):
    """Custom type juniQosSchedulerProfileWeight based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4080),
    )


_JuniQosSchedulerProfileWeight_Type.__name__ = "Unsigned32"
_JuniQosSchedulerProfileWeight_Object = MibTableColumn
juniQosSchedulerProfileWeight = _JuniQosSchedulerProfileWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 6),
    _JuniQosSchedulerProfileWeight_Type()
)
juniQosSchedulerProfileWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileWeight.setStatus("current")


class _JuniQosSchedulerProfileStrictPriority_Type(TruthValue):
    """Custom type juniQosSchedulerProfileStrictPriority based on TruthValue"""


_JuniQosSchedulerProfileStrictPriority_Object = MibTableColumn
juniQosSchedulerProfileStrictPriority = _JuniQosSchedulerProfileStrictPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 7),
    _JuniQosSchedulerProfileStrictPriority_Type()
)
juniQosSchedulerProfileStrictPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileStrictPriority.setStatus("current")
_JuniQosSchedulerProfileUpdatePending_Type = TruthValue
_JuniQosSchedulerProfileUpdatePending_Object = MibTableColumn
juniQosSchedulerProfileUpdatePending = _JuniQosSchedulerProfileUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 8),
    _JuniQosSchedulerProfileUpdatePending_Type()
)
juniQosSchedulerProfileUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileUpdatePending.setStatus("current")


class _JuniQosSchedulerProfileUpdateNow_Type(TruthValue):
    """Custom type juniQosSchedulerProfileUpdateNow based on TruthValue"""


_JuniQosSchedulerProfileUpdateNow_Object = MibTableColumn
juniQosSchedulerProfileUpdateNow = _JuniQosSchedulerProfileUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 9),
    _JuniQosSchedulerProfileUpdateNow_Type()
)
juniQosSchedulerProfileUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileUpdateNow.setStatus("current")
_JuniQosSchedulerProfileIsReferencedByQosProfile_Type = TruthValue
_JuniQosSchedulerProfileIsReferencedByQosProfile_Object = MibTableColumn
juniQosSchedulerProfileIsReferencedByQosProfile = _JuniQosSchedulerProfileIsReferencedByQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 10),
    _JuniQosSchedulerProfileIsReferencedByQosProfile_Type()
)
juniQosSchedulerProfileIsReferencedByQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileIsReferencedByQosProfile.setStatus("current")


class _JuniQosSchedulerProfileAssuredRate_Type(Unsigned32):
    """Custom type juniQosSchedulerProfileAssuredRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(25000, 1000000000),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_JuniQosSchedulerProfileAssuredRate_Type.__name__ = "Unsigned32"
_JuniQosSchedulerProfileAssuredRate_Object = MibTableColumn
juniQosSchedulerProfileAssuredRate = _JuniQosSchedulerProfileAssuredRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 11),
    _JuniQosSchedulerProfileAssuredRate_Type()
)
juniQosSchedulerProfileAssuredRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileAssuredRate.setStatus("current")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileAssuredRate.setUnits("bps")


class _JuniQosSchedulerProfileSharedShapingRate_Type(Unsigned32):
    """Custom type juniQosSchedulerProfileSharedShapingRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_JuniQosSchedulerProfileSharedShapingRate_Type.__name__ = "Unsigned32"
_JuniQosSchedulerProfileSharedShapingRate_Object = MibTableColumn
juniQosSchedulerProfileSharedShapingRate = _JuniQosSchedulerProfileSharedShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 12),
    _JuniQosSchedulerProfileSharedShapingRate_Type()
)
juniQosSchedulerProfileSharedShapingRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileSharedShapingRate.setStatus("current")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileSharedShapingRate.setUnits("bps")


class _JuniQosSchedulerProfileSharedShapingBurstSize_Type(Unsigned32):
    """Custom type juniQosSchedulerProfileSharedShapingBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 522240),
    )


_JuniQosSchedulerProfileSharedShapingBurstSize_Type.__name__ = "Unsigned32"
_JuniQosSchedulerProfileSharedShapingBurstSize_Object = MibTableColumn
juniQosSchedulerProfileSharedShapingBurstSize = _JuniQosSchedulerProfileSharedShapingBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 13),
    _JuniQosSchedulerProfileSharedShapingBurstSize_Type()
)
juniQosSchedulerProfileSharedShapingBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileSharedShapingBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileSharedShapingBurstSize.setUnits("bytes")


class _JuniQosSchedulerProfileSharedShapingType_Type(Integer32):
    """Custom type juniQosSchedulerProfileSharedShapingType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("compound", 2),
          ("none", 0),
          ("simple", 1))
    )


_JuniQosSchedulerProfileSharedShapingType_Type.__name__ = "Integer32"
_JuniQosSchedulerProfileSharedShapingType_Object = MibTableColumn
juniQosSchedulerProfileSharedShapingType = _JuniQosSchedulerProfileSharedShapingType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 14),
    _JuniQosSchedulerProfileSharedShapingType_Type()
)
juniQosSchedulerProfileSharedShapingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileSharedShapingType.setStatus("current")


class _JuniQosSchedulerProfileSharedShapingExplicitConstituents_Type(TruthValue):
    """Custom type juniQosSchedulerProfileSharedShapingExplicitConstituents based on TruthValue"""


_JuniQosSchedulerProfileSharedShapingExplicitConstituents_Object = MibTableColumn
juniQosSchedulerProfileSharedShapingExplicitConstituents = _JuniQosSchedulerProfileSharedShapingExplicitConstituents_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 15),
    _JuniQosSchedulerProfileSharedShapingExplicitConstituents_Type()
)
juniQosSchedulerProfileSharedShapingExplicitConstituents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileSharedShapingExplicitConstituents.setStatus("current")


class _JuniQosSchedulerProfileSharedShapingPriority_Type(Integer32):
    """Custom type juniQosSchedulerProfileSharedShapingPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8),
    )


_JuniQosSchedulerProfileSharedShapingPriority_Type.__name__ = "Integer32"
_JuniQosSchedulerProfileSharedShapingPriority_Object = MibTableColumn
juniQosSchedulerProfileSharedShapingPriority = _JuniQosSchedulerProfileSharedShapingPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 16),
    _JuniQosSchedulerProfileSharedShapingPriority_Type()
)
juniQosSchedulerProfileSharedShapingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileSharedShapingPriority.setStatus("current")


class _JuniQosSchedulerProfileSharedShapingWeight_Type(Integer32):
    """Custom type juniQosSchedulerProfileSharedShapingWeight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31),
    )


_JuniQosSchedulerProfileSharedShapingWeight_Type.__name__ = "Integer32"
_JuniQosSchedulerProfileSharedShapingWeight_Object = MibTableColumn
juniQosSchedulerProfileSharedShapingWeight = _JuniQosSchedulerProfileSharedShapingWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 6, 2, 1, 17),
    _JuniQosSchedulerProfileSharedShapingWeight_Type()
)
juniQosSchedulerProfileSharedShapingWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosSchedulerProfileSharedShapingWeight.setStatus("current")
_JuniQosQueueProfileList_ObjectIdentity = ObjectIdentity
juniQosQueueProfileList = _JuniQosQueueProfileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7)
)
_JuniQosQueueProfileNextIndex_Type = Unsigned32
_JuniQosQueueProfileNextIndex_Object = MibScalar
juniQosQueueProfileNextIndex = _JuniQosQueueProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 1),
    _JuniQosQueueProfileNextIndex_Type()
)
juniQosQueueProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosQueueProfileNextIndex.setStatus("current")
_JuniQosQueueProfileTable_Object = MibTable
juniQosQueueProfileTable = _JuniQosQueueProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2)
)
if mibBuilder.loadTexts:
    juniQosQueueProfileTable.setStatus("current")
_JuniQosQueueProfileEntry_Object = MibTableRow
juniQosQueueProfileEntry = _JuniQosQueueProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1)
)
juniQosQueueProfileEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosQueueProfileIndex"),
)
if mibBuilder.loadTexts:
    juniQosQueueProfileEntry.setStatus("current")
_JuniQosQueueProfileIndex_Type = Unsigned32
_JuniQosQueueProfileIndex_Object = MibTableColumn
juniQosQueueProfileIndex = _JuniQosQueueProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 1),
    _JuniQosQueueProfileIndex_Type()
)
juniQosQueueProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosQueueProfileIndex.setStatus("current")
_JuniQosQueueProfileRowStatus_Type = RowStatus
_JuniQosQueueProfileRowStatus_Object = MibTableColumn
juniQosQueueProfileRowStatus = _JuniQosQueueProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 2),
    _JuniQosQueueProfileRowStatus_Type()
)
juniQosQueueProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileRowStatus.setStatus("current")


class _JuniQosQueueProfileName_Type(DisplayString):
    """Custom type juniQosQueueProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniQosQueueProfileName_Type.__name__ = "DisplayString"
_JuniQosQueueProfileName_Object = MibTableColumn
juniQosQueueProfileName = _JuniQosQueueProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 3),
    _JuniQosQueueProfileName_Type()
)
juniQosQueueProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileName.setStatus("current")


class _JuniQosQueueProfileCommittedMinLength_Type(Unsigned32):
    """Custom type juniQosQueueProfileCommittedMinLength based on Unsigned32"""
    defaultValue = 0


_JuniQosQueueProfileCommittedMinLength_Object = MibTableColumn
juniQosQueueProfileCommittedMinLength = _JuniQosQueueProfileCommittedMinLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 4),
    _JuniQosQueueProfileCommittedMinLength_Type()
)
juniQosQueueProfileCommittedMinLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileCommittedMinLength.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileCommittedMinLength.setUnits("bytes")


class _JuniQosQueueProfileCommittedMaxLength_Type(Unsigned32):
    """Custom type juniQosQueueProfileCommittedMaxLength based on Unsigned32"""
    defaultValue = 1073741824


_JuniQosQueueProfileCommittedMaxLength_Object = MibTableColumn
juniQosQueueProfileCommittedMaxLength = _JuniQosQueueProfileCommittedMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 5),
    _JuniQosQueueProfileCommittedMaxLength_Type()
)
juniQosQueueProfileCommittedMaxLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileCommittedMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileCommittedMaxLength.setUnits("bytes")


class _JuniQosQueueProfileConformedMinLength_Type(Unsigned32):
    """Custom type juniQosQueueProfileConformedMinLength based on Unsigned32"""
    defaultValue = 0


_JuniQosQueueProfileConformedMinLength_Object = MibTableColumn
juniQosQueueProfileConformedMinLength = _JuniQosQueueProfileConformedMinLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 6),
    _JuniQosQueueProfileConformedMinLength_Type()
)
juniQosQueueProfileConformedMinLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileConformedMinLength.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileConformedMinLength.setUnits("bytes")


class _JuniQosQueueProfileConformedMaxLength_Type(Unsigned32):
    """Custom type juniQosQueueProfileConformedMaxLength based on Unsigned32"""
    defaultValue = 1073741824


_JuniQosQueueProfileConformedMaxLength_Object = MibTableColumn
juniQosQueueProfileConformedMaxLength = _JuniQosQueueProfileConformedMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 7),
    _JuniQosQueueProfileConformedMaxLength_Type()
)
juniQosQueueProfileConformedMaxLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileConformedMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileConformedMaxLength.setUnits("bytes")


class _JuniQosQueueProfileExceededMinLength_Type(Unsigned32):
    """Custom type juniQosQueueProfileExceededMinLength based on Unsigned32"""
    defaultValue = 0


_JuniQosQueueProfileExceededMinLength_Object = MibTableColumn
juniQosQueueProfileExceededMinLength = _JuniQosQueueProfileExceededMinLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 8),
    _JuniQosQueueProfileExceededMinLength_Type()
)
juniQosQueueProfileExceededMinLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileExceededMinLength.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileExceededMinLength.setUnits("bytes")


class _JuniQosQueueProfileExceededMaxLength_Type(Unsigned32):
    """Custom type juniQosQueueProfileExceededMaxLength based on Unsigned32"""
    defaultValue = 1073741824


_JuniQosQueueProfileExceededMaxLength_Object = MibTableColumn
juniQosQueueProfileExceededMaxLength = _JuniQosQueueProfileExceededMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 9),
    _JuniQosQueueProfileExceededMaxLength_Type()
)
juniQosQueueProfileExceededMaxLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileExceededMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileExceededMaxLength.setUnits("bytes")


class _JuniQosQueueProfileConformedFraction_Type(Unsigned32):
    """Custom type juniQosQueueProfileConformedFraction based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniQosQueueProfileConformedFraction_Type.__name__ = "Unsigned32"
_JuniQosQueueProfileConformedFraction_Object = MibTableColumn
juniQosQueueProfileConformedFraction = _JuniQosQueueProfileConformedFraction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 10),
    _JuniQosQueueProfileConformedFraction_Type()
)
juniQosQueueProfileConformedFraction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileConformedFraction.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileConformedFraction.setUnits("percent")


class _JuniQosQueueProfileExceededFraction_Type(Unsigned32):
    """Custom type juniQosQueueProfileExceededFraction based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniQosQueueProfileExceededFraction_Type.__name__ = "Unsigned32"
_JuniQosQueueProfileExceededFraction_Object = MibTableColumn
juniQosQueueProfileExceededFraction = _JuniQosQueueProfileExceededFraction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 11),
    _JuniQosQueueProfileExceededFraction_Type()
)
juniQosQueueProfileExceededFraction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileExceededFraction.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileExceededFraction.setUnits("percent")


class _JuniQosQueueProfileCommittedDropThreshold_Type(Unsigned32):
    """Custom type juniQosQueueProfileCommittedDropThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniQosQueueProfileCommittedDropThreshold_Type.__name__ = "Unsigned32"
_JuniQosQueueProfileCommittedDropThreshold_Object = MibTableColumn
juniQosQueueProfileCommittedDropThreshold = _JuniQosQueueProfileCommittedDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 12),
    _JuniQosQueueProfileCommittedDropThreshold_Type()
)
juniQosQueueProfileCommittedDropThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileCommittedDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileCommittedDropThreshold.setUnits("percent")


class _JuniQosQueueProfileCommittedDropRate_Type(Unsigned32):
    """Custom type juniQosQueueProfileCommittedDropRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniQosQueueProfileCommittedDropRate_Type.__name__ = "Unsigned32"
_JuniQosQueueProfileCommittedDropRate_Object = MibTableColumn
juniQosQueueProfileCommittedDropRate = _JuniQosQueueProfileCommittedDropRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 13),
    _JuniQosQueueProfileCommittedDropRate_Type()
)
juniQosQueueProfileCommittedDropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileCommittedDropRate.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileCommittedDropRate.setUnits("percent")


class _JuniQosQueueProfileConformedDropThreshold_Type(Unsigned32):
    """Custom type juniQosQueueProfileConformedDropThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniQosQueueProfileConformedDropThreshold_Type.__name__ = "Unsigned32"
_JuniQosQueueProfileConformedDropThreshold_Object = MibTableColumn
juniQosQueueProfileConformedDropThreshold = _JuniQosQueueProfileConformedDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 14),
    _JuniQosQueueProfileConformedDropThreshold_Type()
)
juniQosQueueProfileConformedDropThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileConformedDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileConformedDropThreshold.setUnits("percent")


class _JuniQosQueueProfileConformedDropRate_Type(Unsigned32):
    """Custom type juniQosQueueProfileConformedDropRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniQosQueueProfileConformedDropRate_Type.__name__ = "Unsigned32"
_JuniQosQueueProfileConformedDropRate_Object = MibTableColumn
juniQosQueueProfileConformedDropRate = _JuniQosQueueProfileConformedDropRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 15),
    _JuniQosQueueProfileConformedDropRate_Type()
)
juniQosQueueProfileConformedDropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileConformedDropRate.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileConformedDropRate.setUnits("percent")


class _JuniQosQueueProfileExceededDropThreshold_Type(Unsigned32):
    """Custom type juniQosQueueProfileExceededDropThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniQosQueueProfileExceededDropThreshold_Type.__name__ = "Unsigned32"
_JuniQosQueueProfileExceededDropThreshold_Object = MibTableColumn
juniQosQueueProfileExceededDropThreshold = _JuniQosQueueProfileExceededDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 16),
    _JuniQosQueueProfileExceededDropThreshold_Type()
)
juniQosQueueProfileExceededDropThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileExceededDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileExceededDropThreshold.setUnits("percent")


class _JuniQosQueueProfileExceededDropRate_Type(Unsigned32):
    """Custom type juniQosQueueProfileExceededDropRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniQosQueueProfileExceededDropRate_Type.__name__ = "Unsigned32"
_JuniQosQueueProfileExceededDropRate_Object = MibTableColumn
juniQosQueueProfileExceededDropRate = _JuniQosQueueProfileExceededDropRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 17),
    _JuniQosQueueProfileExceededDropRate_Type()
)
juniQosQueueProfileExceededDropRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileExceededDropRate.setStatus("current")
if mibBuilder.loadTexts:
    juniQosQueueProfileExceededDropRate.setUnits("percent")


class _JuniQosQueueProfileBufferWeight_Type(Unsigned32):
    """Custom type juniQosQueueProfileBufferWeight based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_JuniQosQueueProfileBufferWeight_Type.__name__ = "Unsigned32"
_JuniQosQueueProfileBufferWeight_Object = MibTableColumn
juniQosQueueProfileBufferWeight = _JuniQosQueueProfileBufferWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 18),
    _JuniQosQueueProfileBufferWeight_Type()
)
juniQosQueueProfileBufferWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileBufferWeight.setStatus("current")
_JuniQosQueueProfileUpdatePending_Type = TruthValue
_JuniQosQueueProfileUpdatePending_Object = MibTableColumn
juniQosQueueProfileUpdatePending = _JuniQosQueueProfileUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 19),
    _JuniQosQueueProfileUpdatePending_Type()
)
juniQosQueueProfileUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosQueueProfileUpdatePending.setStatus("current")


class _JuniQosQueueProfileUpdateNow_Type(TruthValue):
    """Custom type juniQosQueueProfileUpdateNow based on TruthValue"""


_JuniQosQueueProfileUpdateNow_Object = MibTableColumn
juniQosQueueProfileUpdateNow = _JuniQosQueueProfileUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 20),
    _JuniQosQueueProfileUpdateNow_Type()
)
juniQosQueueProfileUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQueueProfileUpdateNow.setStatus("current")
_JuniQosQueueProfileIsReferencedByQosProfile_Type = TruthValue
_JuniQosQueueProfileIsReferencedByQosProfile_Object = MibTableColumn
juniQosQueueProfileIsReferencedByQosProfile = _JuniQosQueueProfileIsReferencedByQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 7, 2, 1, 21),
    _JuniQosQueueProfileIsReferencedByQosProfile_Type()
)
juniQosQueueProfileIsReferencedByQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosQueueProfileIsReferencedByQosProfile.setStatus("current")
_JuniQosProfile_ObjectIdentity = ObjectIdentity
juniQosProfile = _JuniQosProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8)
)
_JuniQosProfileNextIndex_Type = Unsigned32
_JuniQosProfileNextIndex_Object = MibScalar
juniQosProfileNextIndex = _JuniQosProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 1),
    _JuniQosProfileNextIndex_Type()
)
juniQosProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosProfileNextIndex.setStatus("current")
_JuniQosProfileTable_Object = MibTable
juniQosProfileTable = _JuniQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2)
)
if mibBuilder.loadTexts:
    juniQosProfileTable.setStatus("current")
_JuniQosProfileEntry_Object = MibTableRow
juniQosProfileEntry = _JuniQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1)
)
juniQosProfileEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosProfileIndex"),
)
if mibBuilder.loadTexts:
    juniQosProfileEntry.setStatus("current")
_JuniQosProfileIndex_Type = Unsigned32
_JuniQosProfileIndex_Object = MibTableColumn
juniQosProfileIndex = _JuniQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 1),
    _JuniQosProfileIndex_Type()
)
juniQosProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosProfileIndex.setStatus("current")
_JuniQosProfileRowStatus_Type = RowStatus
_JuniQosProfileRowStatus_Object = MibTableColumn
juniQosProfileRowStatus = _JuniQosProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 2),
    _JuniQosProfileRowStatus_Type()
)
juniQosProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosProfileRowStatus.setStatus("current")


class _JuniQosProfileName_Type(DisplayString):
    """Custom type juniQosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniQosProfileName_Type.__name__ = "DisplayString"
_JuniQosProfileName_Object = MibTableColumn
juniQosProfileName = _JuniQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 3),
    _JuniQosProfileName_Type()
)
juniQosProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosProfileName.setStatus("current")
_JuniQosProfileUpdatePending_Type = TruthValue
_JuniQosProfileUpdatePending_Object = MibTableColumn
juniQosProfileUpdatePending = _JuniQosProfileUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 4),
    _JuniQosProfileUpdatePending_Type()
)
juniQosProfileUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosProfileUpdatePending.setStatus("current")


class _JuniQosProfileUpdateNow_Type(TruthValue):
    """Custom type juniQosProfileUpdateNow based on TruthValue"""


_JuniQosProfileUpdateNow_Object = MibTableColumn
juniQosProfileUpdateNow = _JuniQosProfileUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 5),
    _JuniQosProfileUpdateNow_Type()
)
juniQosProfileUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosProfileUpdateNow.setStatus("current")
_JuniQosProfileIsReferencedByInterfaceQosAttachment_Type = TruthValue
_JuniQosProfileIsReferencedByInterfaceQosAttachment_Object = MibTableColumn
juniQosProfileIsReferencedByInterfaceQosAttachment = _JuniQosProfileIsReferencedByInterfaceQosAttachment_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 6),
    _JuniQosProfileIsReferencedByInterfaceQosAttachment_Type()
)
juniQosProfileIsReferencedByInterfaceQosAttachment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosProfileIsReferencedByInterfaceQosAttachment.setStatus("current")
_JuniQosProfileIsReferencedByQosPortTypeProfile_Type = TruthValue
_JuniQosProfileIsReferencedByQosPortTypeProfile_Object = MibTableColumn
juniQosProfileIsReferencedByQosPortTypeProfile = _JuniQosProfileIsReferencedByQosPortTypeProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 8, 2, 1, 7),
    _JuniQosProfileIsReferencedByQosPortTypeProfile_Type()
)
juniQosProfileIsReferencedByQosPortTypeProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosProfileIsReferencedByQosPortTypeProfile.setStatus("current")
_JuniQosProfileElement_ObjectIdentity = ObjectIdentity
juniQosProfileElement = _JuniQosProfileElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9)
)
_JuniQosProfileElementTable_Object = MibTable
juniQosProfileElementTable = _JuniQosProfileElementTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1)
)
if mibBuilder.loadTexts:
    juniQosProfileElementTable.setStatus("current")
_JuniQosProfileElementEntry_Object = MibTableRow
juniQosProfileElementEntry = _JuniQosProfileElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1)
)
juniQosProfileElementEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosProfileIndex"),
    (0, "Juniper-QoS-MIB", "juniQosInterfaceType"),
    (0, "Juniper-QoS-MIB", "juniQosProfileEntryType"),
    (0, "Juniper-QoS-MIB", "juniQosTrafficClassIndex"),
    (0, "Juniper-QoS-MIB", "juniQosTrafficClassGroupIndex"),
)
if mibBuilder.loadTexts:
    juniQosProfileElementEntry.setStatus("current")
_JuniQosProfileElementEntryRowStatus_Type = RowStatus
_JuniQosProfileElementEntryRowStatus_Object = MibTableColumn
juniQosProfileElementEntryRowStatus = _JuniQosProfileElementEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 1),
    _JuniQosProfileElementEntryRowStatus_Type()
)
juniQosProfileElementEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosProfileElementEntryRowStatus.setStatus("current")


class _JuniQosProfileElementEntryQueueProfile_Type(Unsigned32):
    """Custom type juniQosProfileElementEntryQueueProfile based on Unsigned32"""
    defaultValue = 1


_JuniQosProfileElementEntryQueueProfile_Object = MibTableColumn
juniQosProfileElementEntryQueueProfile = _JuniQosProfileElementEntryQueueProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 2),
    _JuniQosProfileElementEntryQueueProfile_Type()
)
juniQosProfileElementEntryQueueProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosProfileElementEntryQueueProfile.setStatus("current")


class _JuniQosProfileElementEntrySchedulerProfile_Type(Unsigned32):
    """Custom type juniQosProfileElementEntrySchedulerProfile based on Unsigned32"""
    defaultValue = 1


_JuniQosProfileElementEntrySchedulerProfile_Object = MibTableColumn
juniQosProfileElementEntrySchedulerProfile = _JuniQosProfileElementEntrySchedulerProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 3),
    _JuniQosProfileElementEntrySchedulerProfile_Type()
)
juniQosProfileElementEntrySchedulerProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosProfileElementEntrySchedulerProfile.setStatus("current")


class _JuniQosInterfaceType_Type(Integer32):
    """Custom type juniQosInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              9,
              11,
              13,
              16,
              21,
              31,
              35,
              36,
              50,
              150,
              151,
              163,
              174)
        )
    )
    namedValues = NamedValues(
        *(("atm", 9),
          ("atmVc", 11),
          ("atmVp", 163),
          ("cbf", 36),
          ("ethernet", 6),
          ("frVc", 16),
          ("ip", 0),
          ("ipTunnel", 151),
          ("ipv6", 50),
          ("l2tpSession", 21),
          ("l2tpTunnel", 150),
          ("serial", 13),
          ("serverPort", 31),
          ("svlan", 174),
          ("vlan", 35))
    )


_JuniQosInterfaceType_Type.__name__ = "Integer32"
_JuniQosInterfaceType_Object = MibTableColumn
juniQosInterfaceType = _JuniQosInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 4),
    _JuniQosInterfaceType_Type()
)
juniQosInterfaceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosInterfaceType.setStatus("current")


class _JuniQosProfileEntryType_Type(Integer32):
    """Custom type juniQosProfileEntryType based on Integer32"""
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
        *(("schedulerProfile", 2),
          ("shadowNode", 4),
          ("trafficClass", 1),
          ("trafficClassGroup", 3))
    )


_JuniQosProfileEntryType_Type.__name__ = "Integer32"
_JuniQosProfileEntryType_Object = MibTableColumn
juniQosProfileEntryType = _JuniQosProfileEntryType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 5),
    _JuniQosProfileEntryType_Type()
)
juniQosProfileEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosProfileEntryType.setStatus("current")


class _JuniQosProfileElementEntryDropProfile_Type(Unsigned32):
    """Custom type juniQosProfileElementEntryDropProfile based on Unsigned32"""
    defaultValue = 1


_JuniQosProfileElementEntryDropProfile_Object = MibTableColumn
juniQosProfileElementEntryDropProfile = _JuniQosProfileElementEntryDropProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 6),
    _JuniQosProfileElementEntryDropProfile_Type()
)
juniQosProfileElementEntryDropProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosProfileElementEntryDropProfile.setStatus("current")


class _JuniQosProfileElementEntryStatisticsProfile_Type(Unsigned32):
    """Custom type juniQosProfileElementEntryStatisticsProfile based on Unsigned32"""
    defaultValue = 1


_JuniQosProfileElementEntryStatisticsProfile_Object = MibTableColumn
juniQosProfileElementEntryStatisticsProfile = _JuniQosProfileElementEntryStatisticsProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 9, 1, 1, 7),
    _JuniQosProfileElementEntryStatisticsProfile_Type()
)
juniQosProfileElementEntryStatisticsProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosProfileElementEntryStatisticsProfile.setStatus("current")
_JuniQosIfAttach_ObjectIdentity = ObjectIdentity
juniQosIfAttach = _JuniQosIfAttach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10)
)
_JuniQosIfAttachTable_Object = MibTable
juniQosIfAttachTable = _JuniQosIfAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10, 1)
)
if mibBuilder.loadTexts:
    juniQosIfAttachTable.setStatus("current")
_JuniQosIfAttachEntry_Object = MibTableRow
juniQosIfAttachEntry = _JuniQosIfAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10, 1, 1)
)
juniQosIfAttachEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosIfAttachIndex"),
)
if mibBuilder.loadTexts:
    juniQosIfAttachEntry.setStatus("current")
_JuniQosIfAttachIndex_Type = Unsigned32
_JuniQosIfAttachIndex_Object = MibTableColumn
juniQosIfAttachIndex = _JuniQosIfAttachIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10, 1, 1, 1),
    _JuniQosIfAttachIndex_Type()
)
juniQosIfAttachIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosIfAttachIndex.setStatus("current")
_JuniQosIfAttachRowStatus_Type = RowStatus
_JuniQosIfAttachRowStatus_Object = MibTableColumn
juniQosIfAttachRowStatus = _JuniQosIfAttachRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10, 1, 1, 2),
    _JuniQosIfAttachRowStatus_Type()
)
juniQosIfAttachRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosIfAttachRowStatus.setStatus("current")
_JuniQosIfAttachQosProfileIndex_Type = Unsigned32
_JuniQosIfAttachQosProfileIndex_Object = MibTableColumn
juniQosIfAttachQosProfileIndex = _JuniQosIfAttachQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 10, 1, 1, 3),
    _JuniQosIfAttachQosProfileIndex_Type()
)
juniQosIfAttachQosProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosIfAttachQosProfileIndex.setStatus("current")
_JuniQosQosPortTypeProfile_ObjectIdentity = ObjectIdentity
juniQosQosPortTypeProfile = _JuniQosQosPortTypeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11)
)
_JuniQosQosPortTypeProfileTable_Object = MibTable
juniQosQosPortTypeProfileTable = _JuniQosQosPortTypeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11, 1)
)
if mibBuilder.loadTexts:
    juniQosQosPortTypeProfileTable.setStatus("current")
_JuniQosQosPortTypeProfileEntry_Object = MibTableRow
juniQosQosPortTypeProfileEntry = _JuniQosQosPortTypeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11, 1, 1)
)
juniQosQosPortTypeProfileEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosQosPortTypeProfileIndex"),
)
if mibBuilder.loadTexts:
    juniQosQosPortTypeProfileEntry.setStatus("current")


class _JuniQosQosPortTypeProfileIndex_Type(Integer32):
    """Custom type juniQosQosPortTypeProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              9,
              13,
              31,
              54)
        )
    )
    namedValues = NamedValues(
        *(("atm", 9),
          ("ethernet", 6),
          ("lag", 54),
          ("serial", 13),
          ("serverPort", 31))
    )


_JuniQosQosPortTypeProfileIndex_Type.__name__ = "Integer32"
_JuniQosQosPortTypeProfileIndex_Object = MibTableColumn
juniQosQosPortTypeProfileIndex = _JuniQosQosPortTypeProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11, 1, 1, 1),
    _JuniQosQosPortTypeProfileIndex_Type()
)
juniQosQosPortTypeProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosQosPortTypeProfileIndex.setStatus("current")
_JuniQosQosPortTypeProfileRowStatus_Type = RowStatus
_JuniQosQosPortTypeProfileRowStatus_Object = MibTableColumn
juniQosQosPortTypeProfileRowStatus = _JuniQosQosPortTypeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11, 1, 1, 2),
    _JuniQosQosPortTypeProfileRowStatus_Type()
)
juniQosQosPortTypeProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQosPortTypeProfileRowStatus.setStatus("current")
_JuniQosQosPortTypeProfileQosProfileIndex_Type = Unsigned32
_JuniQosQosPortTypeProfileQosProfileIndex_Object = MibTableColumn
juniQosQosPortTypeProfileQosProfileIndex = _JuniQosQosPortTypeProfileQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 11, 1, 1, 3),
    _JuniQosQosPortTypeProfileQosProfileIndex_Type()
)
juniQosQosPortTypeProfileQosProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQosPortTypeProfileQosProfileIndex.setStatus("current")
_JuniQosQueueStatistics_ObjectIdentity = ObjectIdentity
juniQosQueueStatistics = _JuniQosQueueStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12)
)
_JuniQosQueueStatisticsTable_Object = MibTable
juniQosQueueStatisticsTable = _JuniQosQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1)
)
if mibBuilder.loadTexts:
    juniQosQueueStatisticsTable.setStatus("current")
_JuniQosQueueStatisticsEntry_Object = MibTableRow
juniQosQueueStatisticsEntry = _JuniQosQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1)
)
juniQosQueueStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Juniper-QoS-MIB", "juniQosTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    juniQosQueueStatisticsEntry.setStatus("current")
_JuniQosOutPacketForwarded_Type = Counter64
_JuniQosOutPacketForwarded_Object = MibTableColumn
juniQosOutPacketForwarded = _JuniQosOutPacketForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 1),
    _JuniQosOutPacketForwarded_Type()
)
juniQosOutPacketForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosOutPacketForwarded.setStatus("current")
if mibBuilder.loadTexts:
    juniQosOutPacketForwarded.setUnits("packets")
_JuniQosOutBytesForwarded_Type = Counter64
_JuniQosOutBytesForwarded_Object = MibTableColumn
juniQosOutBytesForwarded = _JuniQosOutBytesForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 2),
    _JuniQosOutBytesForwarded_Type()
)
juniQosOutBytesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosOutBytesForwarded.setStatus("current")
if mibBuilder.loadTexts:
    juniQosOutBytesForwarded.setUnits("bytes")
_JuniQosOutGreenPacketsSchedulerDrops_Type = Counter64
_JuniQosOutGreenPacketsSchedulerDrops_Object = MibTableColumn
juniQosOutGreenPacketsSchedulerDrops = _JuniQosOutGreenPacketsSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 3),
    _JuniQosOutGreenPacketsSchedulerDrops_Type()
)
juniQosOutGreenPacketsSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosOutGreenPacketsSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    juniQosOutGreenPacketsSchedulerDrops.setUnits("packets")
_JuniQosOutYellowPacketsSchedulerDrops_Type = Counter64
_JuniQosOutYellowPacketsSchedulerDrops_Object = MibTableColumn
juniQosOutYellowPacketsSchedulerDrops = _JuniQosOutYellowPacketsSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 4),
    _JuniQosOutYellowPacketsSchedulerDrops_Type()
)
juniQosOutYellowPacketsSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosOutYellowPacketsSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    juniQosOutYellowPacketsSchedulerDrops.setUnits("packets")
_JuniQosOutRedPacketsSchedulerDrops_Type = Counter64
_JuniQosOutRedPacketsSchedulerDrops_Object = MibTableColumn
juniQosOutRedPacketsSchedulerDrops = _JuniQosOutRedPacketsSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 5),
    _JuniQosOutRedPacketsSchedulerDrops_Type()
)
juniQosOutRedPacketsSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosOutRedPacketsSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    juniQosOutRedPacketsSchedulerDrops.setUnits("packets")
_JuniQosOutGreenBytesSchedulerDrops_Type = Counter64
_JuniQosOutGreenBytesSchedulerDrops_Object = MibTableColumn
juniQosOutGreenBytesSchedulerDrops = _JuniQosOutGreenBytesSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 6),
    _JuniQosOutGreenBytesSchedulerDrops_Type()
)
juniQosOutGreenBytesSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosOutGreenBytesSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    juniQosOutGreenBytesSchedulerDrops.setUnits("bytes")
_JuniQosOutYellowBytesSchedulerDrops_Type = Counter64
_JuniQosOutYellowBytesSchedulerDrops_Object = MibTableColumn
juniQosOutYellowBytesSchedulerDrops = _JuniQosOutYellowBytesSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 7),
    _JuniQosOutYellowBytesSchedulerDrops_Type()
)
juniQosOutYellowBytesSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosOutYellowBytesSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    juniQosOutYellowBytesSchedulerDrops.setUnits("bytes")
_JuniQosOutRedBytesSchedulerDrops_Type = Counter64
_JuniQosOutRedBytesSchedulerDrops_Object = MibTableColumn
juniQosOutRedBytesSchedulerDrops = _JuniQosOutRedBytesSchedulerDrops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 12, 1, 1, 8),
    _JuniQosOutRedBytesSchedulerDrops_Type()
)
juniQosOutRedBytesSchedulerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosOutRedBytesSchedulerDrops.setStatus("current")
if mibBuilder.loadTexts:
    juniQosOutRedBytesSchedulerDrops.setUnits("bytes")
_JuniQosDropProfileList_ObjectIdentity = ObjectIdentity
juniQosDropProfileList = _JuniQosDropProfileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13)
)
_JuniQosDropProfileNextIndex_Type = Unsigned32
_JuniQosDropProfileNextIndex_Object = MibScalar
juniQosDropProfileNextIndex = _JuniQosDropProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 1),
    _JuniQosDropProfileNextIndex_Type()
)
juniQosDropProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosDropProfileNextIndex.setStatus("current")
_JuniQosDropProfileTable_Object = MibTable
juniQosDropProfileTable = _JuniQosDropProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2)
)
if mibBuilder.loadTexts:
    juniQosDropProfileTable.setStatus("current")
_JuniQosDropProfileEntry_Object = MibTableRow
juniQosDropProfileEntry = _JuniQosDropProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1)
)
juniQosDropProfileEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosDropProfileIndex"),
)
if mibBuilder.loadTexts:
    juniQosDropProfileEntry.setStatus("current")
_JuniQosDropProfileIndex_Type = Unsigned32
_JuniQosDropProfileIndex_Object = MibTableColumn
juniQosDropProfileIndex = _JuniQosDropProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 1),
    _JuniQosDropProfileIndex_Type()
)
juniQosDropProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosDropProfileIndex.setStatus("current")
_JuniQosDropProfileRowStatus_Type = RowStatus
_JuniQosDropProfileRowStatus_Object = MibTableColumn
juniQosDropProfileRowStatus = _JuniQosDropProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 2),
    _JuniQosDropProfileRowStatus_Type()
)
juniQosDropProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileRowStatus.setStatus("current")


class _JuniQosDropProfileName_Type(DisplayString):
    """Custom type juniQosDropProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniQosDropProfileName_Type.__name__ = "DisplayString"
_JuniQosDropProfileName_Object = MibTableColumn
juniQosDropProfileName = _JuniQosDropProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 3),
    _JuniQosDropProfileName_Type()
)
juniQosDropProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileName.setStatus("current")


class _JuniQosDropProfileAverageLengthExponent_Type(Unsigned32):
    """Custom type juniQosDropProfileAverageLengthExponent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_JuniQosDropProfileAverageLengthExponent_Type.__name__ = "Unsigned32"
_JuniQosDropProfileAverageLengthExponent_Object = MibTableColumn
juniQosDropProfileAverageLengthExponent = _JuniQosDropProfileAverageLengthExponent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 4),
    _JuniQosDropProfileAverageLengthExponent_Type()
)
juniQosDropProfileAverageLengthExponent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileAverageLengthExponent.setStatus("current")


class _JuniQosDropProfileCommittedThresholdUnits_Type(Integer32):
    """Custom type juniQosDropProfileCommittedThresholdUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 1),
          ("percent", 2))
    )


_JuniQosDropProfileCommittedThresholdUnits_Type.__name__ = "Integer32"
_JuniQosDropProfileCommittedThresholdUnits_Object = MibTableColumn
juniQosDropProfileCommittedThresholdUnits = _JuniQosDropProfileCommittedThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 5),
    _JuniQosDropProfileCommittedThresholdUnits_Type()
)
juniQosDropProfileCommittedThresholdUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileCommittedThresholdUnits.setStatus("current")


class _JuniQosDropProfileCommittedThresholdMinThreshold_Type(Unsigned32):
    """Custom type juniQosDropProfileCommittedThresholdMinThreshold based on Unsigned32"""
    defaultValue = 0


_JuniQosDropProfileCommittedThresholdMinThreshold_Object = MibTableColumn
juniQosDropProfileCommittedThresholdMinThreshold = _JuniQosDropProfileCommittedThresholdMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 6),
    _JuniQosDropProfileCommittedThresholdMinThreshold_Type()
)
juniQosDropProfileCommittedThresholdMinThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileCommittedThresholdMinThreshold.setStatus("current")


class _JuniQosDropProfileCommittedThresholdMaxThreshold_Type(Unsigned32):
    """Custom type juniQosDropProfileCommittedThresholdMaxThreshold based on Unsigned32"""
    defaultValue = 0


_JuniQosDropProfileCommittedThresholdMaxThreshold_Object = MibTableColumn
juniQosDropProfileCommittedThresholdMaxThreshold = _JuniQosDropProfileCommittedThresholdMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 7),
    _JuniQosDropProfileCommittedThresholdMaxThreshold_Type()
)
juniQosDropProfileCommittedThresholdMaxThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileCommittedThresholdMaxThreshold.setStatus("current")


class _JuniQosDropProfileCommittedThresholdMaxDropProbability_Type(Unsigned32):
    """Custom type juniQosDropProfileCommittedThresholdMaxDropProbability based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniQosDropProfileCommittedThresholdMaxDropProbability_Type.__name__ = "Unsigned32"
_JuniQosDropProfileCommittedThresholdMaxDropProbability_Object = MibTableColumn
juniQosDropProfileCommittedThresholdMaxDropProbability = _JuniQosDropProfileCommittedThresholdMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 8),
    _JuniQosDropProfileCommittedThresholdMaxDropProbability_Type()
)
juniQosDropProfileCommittedThresholdMaxDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileCommittedThresholdMaxDropProbability.setStatus("current")


class _JuniQosDropProfileConformedThresholdUnits_Type(Integer32):
    """Custom type juniQosDropProfileConformedThresholdUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 1),
          ("percent", 2))
    )


_JuniQosDropProfileConformedThresholdUnits_Type.__name__ = "Integer32"
_JuniQosDropProfileConformedThresholdUnits_Object = MibTableColumn
juniQosDropProfileConformedThresholdUnits = _JuniQosDropProfileConformedThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 9),
    _JuniQosDropProfileConformedThresholdUnits_Type()
)
juniQosDropProfileConformedThresholdUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileConformedThresholdUnits.setStatus("current")


class _JuniQosDropProfileConformedThresholdMinThreshold_Type(Unsigned32):
    """Custom type juniQosDropProfileConformedThresholdMinThreshold based on Unsigned32"""
    defaultValue = 0


_JuniQosDropProfileConformedThresholdMinThreshold_Object = MibTableColumn
juniQosDropProfileConformedThresholdMinThreshold = _JuniQosDropProfileConformedThresholdMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 10),
    _JuniQosDropProfileConformedThresholdMinThreshold_Type()
)
juniQosDropProfileConformedThresholdMinThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileConformedThresholdMinThreshold.setStatus("current")


class _JuniQosDropProfileConformedThresholdMaxThreshold_Type(Unsigned32):
    """Custom type juniQosDropProfileConformedThresholdMaxThreshold based on Unsigned32"""
    defaultValue = 0


_JuniQosDropProfileConformedThresholdMaxThreshold_Object = MibTableColumn
juniQosDropProfileConformedThresholdMaxThreshold = _JuniQosDropProfileConformedThresholdMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 11),
    _JuniQosDropProfileConformedThresholdMaxThreshold_Type()
)
juniQosDropProfileConformedThresholdMaxThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileConformedThresholdMaxThreshold.setStatus("current")


class _JuniQosDropProfileConformedThresholdMaxDropProbability_Type(Unsigned32):
    """Custom type juniQosDropProfileConformedThresholdMaxDropProbability based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniQosDropProfileConformedThresholdMaxDropProbability_Type.__name__ = "Unsigned32"
_JuniQosDropProfileConformedThresholdMaxDropProbability_Object = MibTableColumn
juniQosDropProfileConformedThresholdMaxDropProbability = _JuniQosDropProfileConformedThresholdMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 12),
    _JuniQosDropProfileConformedThresholdMaxDropProbability_Type()
)
juniQosDropProfileConformedThresholdMaxDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileConformedThresholdMaxDropProbability.setStatus("current")


class _JuniQosDropProfileExceededThresholdUnits_Type(Integer32):
    """Custom type juniQosDropProfileExceededThresholdUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 1),
          ("percent", 2))
    )


_JuniQosDropProfileExceededThresholdUnits_Type.__name__ = "Integer32"
_JuniQosDropProfileExceededThresholdUnits_Object = MibTableColumn
juniQosDropProfileExceededThresholdUnits = _JuniQosDropProfileExceededThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 13),
    _JuniQosDropProfileExceededThresholdUnits_Type()
)
juniQosDropProfileExceededThresholdUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileExceededThresholdUnits.setStatus("current")


class _JuniQosDropProfileExceededThresholdMinThreshold_Type(Unsigned32):
    """Custom type juniQosDropProfileExceededThresholdMinThreshold based on Unsigned32"""
    defaultValue = 0


_JuniQosDropProfileExceededThresholdMinThreshold_Object = MibTableColumn
juniQosDropProfileExceededThresholdMinThreshold = _JuniQosDropProfileExceededThresholdMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 14),
    _JuniQosDropProfileExceededThresholdMinThreshold_Type()
)
juniQosDropProfileExceededThresholdMinThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileExceededThresholdMinThreshold.setStatus("current")


class _JuniQosDropProfileExceededThresholdMaxThreshold_Type(Unsigned32):
    """Custom type juniQosDropProfileExceededThresholdMaxThreshold based on Unsigned32"""
    defaultValue = 0


_JuniQosDropProfileExceededThresholdMaxThreshold_Object = MibTableColumn
juniQosDropProfileExceededThresholdMaxThreshold = _JuniQosDropProfileExceededThresholdMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 15),
    _JuniQosDropProfileExceededThresholdMaxThreshold_Type()
)
juniQosDropProfileExceededThresholdMaxThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileExceededThresholdMaxThreshold.setStatus("current")


class _JuniQosDropProfileExceededThresholdMaxDropProbability_Type(Unsigned32):
    """Custom type juniQosDropProfileExceededThresholdMaxDropProbability based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniQosDropProfileExceededThresholdMaxDropProbability_Type.__name__ = "Unsigned32"
_JuniQosDropProfileExceededThresholdMaxDropProbability_Object = MibTableColumn
juniQosDropProfileExceededThresholdMaxDropProbability = _JuniQosDropProfileExceededThresholdMaxDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 16),
    _JuniQosDropProfileExceededThresholdMaxDropProbability_Type()
)
juniQosDropProfileExceededThresholdMaxDropProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileExceededThresholdMaxDropProbability.setStatus("current")
_JuniQosDropProfileUpdatePending_Type = TruthValue
_JuniQosDropProfileUpdatePending_Object = MibTableColumn
juniQosDropProfileUpdatePending = _JuniQosDropProfileUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 17),
    _JuniQosDropProfileUpdatePending_Type()
)
juniQosDropProfileUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosDropProfileUpdatePending.setStatus("current")


class _JuniQosDropProfileUpdateNow_Type(TruthValue):
    """Custom type juniQosDropProfileUpdateNow based on TruthValue"""


_JuniQosDropProfileUpdateNow_Object = MibTableColumn
juniQosDropProfileUpdateNow = _JuniQosDropProfileUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 18),
    _JuniQosDropProfileUpdateNow_Type()
)
juniQosDropProfileUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosDropProfileUpdateNow.setStatus("current")
_JuniQosDropProfileIsReferencedByQosProfile_Type = TruthValue
_JuniQosDropProfileIsReferencedByQosProfile_Object = MibTableColumn
juniQosDropProfileIsReferencedByQosProfile = _JuniQosDropProfileIsReferencedByQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 13, 2, 1, 19),
    _JuniQosDropProfileIsReferencedByQosProfile_Type()
)
juniQosDropProfileIsReferencedByQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosDropProfileIsReferencedByQosProfile.setStatus("current")
_JuniQosAtmVpUidSupport_ObjectIdentity = ObjectIdentity
juniQosAtmVpUidSupport = _JuniQosAtmVpUidSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 14)
)


class _JuniQosAtmVpUidValid_Type(Integer32):
    """Custom type juniQosAtmVpUidValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("badAtmVpUid", 3),
          ("badPath", 2),
          ("badPortInterfaceUid", 1),
          ("valid", 0))
    )


_JuniQosAtmVpUidValid_Type.__name__ = "Integer32"
_JuniQosAtmVpUidValid_Object = MibScalar
juniQosAtmVpUidValid = _JuniQosAtmVpUidValid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 14, 1),
    _JuniQosAtmVpUidValid_Type()
)
juniQosAtmVpUidValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosAtmVpUidValid.setStatus("current")
_JuniQosAtmVpAtmPortInterfaceUid_Type = Unsigned32
_JuniQosAtmVpAtmPortInterfaceUid_Object = MibScalar
juniQosAtmVpAtmPortInterfaceUid = _JuniQosAtmVpAtmPortInterfaceUid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 14, 2),
    _JuniQosAtmVpAtmPortInterfaceUid_Type()
)
juniQosAtmVpAtmPortInterfaceUid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniQosAtmVpAtmPortInterfaceUid.setStatus("current")


class _JuniQosAtmVpAtmPath_Type(Unsigned32):
    """Custom type juniQosAtmVpAtmPath based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniQosAtmVpAtmPath_Type.__name__ = "Unsigned32"
_JuniQosAtmVpAtmPath_Object = MibScalar
juniQosAtmVpAtmPath = _JuniQosAtmVpAtmPath_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 14, 3),
    _JuniQosAtmVpAtmPath_Type()
)
juniQosAtmVpAtmPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniQosAtmVpAtmPath.setStatus("current")
_JuniQosAtmVpUid_Type = Unsigned32
_JuniQosAtmVpUid_Object = MibScalar
juniQosAtmVpUid = _JuniQosAtmVpUid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 14, 4),
    _JuniQosAtmVpUid_Type()
)
juniQosAtmVpUid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniQosAtmVpUid.setStatus("current")
_JuniQosStatisticsProfileList_ObjectIdentity = ObjectIdentity
juniQosStatisticsProfileList = _JuniQosStatisticsProfileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15)
)
_JuniQosStatisticsProfileNextIndex_Type = Unsigned32
_JuniQosStatisticsProfileNextIndex_Object = MibScalar
juniQosStatisticsProfileNextIndex = _JuniQosStatisticsProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 1),
    _JuniQosStatisticsProfileNextIndex_Type()
)
juniQosStatisticsProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileNextIndex.setStatus("current")
_JuniQosStatisticsProfileTable_Object = MibTable
juniQosStatisticsProfileTable = _JuniQosStatisticsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2)
)
if mibBuilder.loadTexts:
    juniQosStatisticsProfileTable.setStatus("current")
_JuniQosStatisticsProfileEntry_Object = MibTableRow
juniQosStatisticsProfileEntry = _JuniQosStatisticsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1)
)
juniQosStatisticsProfileEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosStatisticsProfileIndex"),
)
if mibBuilder.loadTexts:
    juniQosStatisticsProfileEntry.setStatus("current")
_JuniQosStatisticsProfileIndex_Type = Unsigned32
_JuniQosStatisticsProfileIndex_Object = MibTableColumn
juniQosStatisticsProfileIndex = _JuniQosStatisticsProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1, 1),
    _JuniQosStatisticsProfileIndex_Type()
)
juniQosStatisticsProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileIndex.setStatus("current")
_JuniQosStatisticsProfileRowStatus_Type = RowStatus
_JuniQosStatisticsProfileRowStatus_Object = MibTableColumn
juniQosStatisticsProfileRowStatus = _JuniQosStatisticsProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1, 2),
    _JuniQosStatisticsProfileRowStatus_Type()
)
juniQosStatisticsProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileRowStatus.setStatus("current")


class _JuniQosStatisticsProfileName_Type(DisplayString):
    """Custom type juniQosStatisticsProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniQosStatisticsProfileName_Type.__name__ = "DisplayString"
_JuniQosStatisticsProfileName_Object = MibTableColumn
juniQosStatisticsProfileName = _JuniQosStatisticsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1, 3),
    _JuniQosStatisticsProfileName_Type()
)
juniQosStatisticsProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileName.setStatus("current")


class _JuniQosStatisticsProfileForwardingRateThreshold_Type(Unsigned32):
    """Custom type juniQosStatisticsProfileForwardingRateThreshold based on Unsigned32"""
    defaultValue = 0


_JuniQosStatisticsProfileForwardingRateThreshold_Object = MibTableColumn
juniQosStatisticsProfileForwardingRateThreshold = _JuniQosStatisticsProfileForwardingRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1, 4),
    _JuniQosStatisticsProfileForwardingRateThreshold_Type()
)
juniQosStatisticsProfileForwardingRateThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileForwardingRateThreshold.setStatus("current")


class _JuniQosStatisticsProfileCommittedDropThreshold_Type(Unsigned32):
    """Custom type juniQosStatisticsProfileCommittedDropThreshold based on Unsigned32"""
    defaultValue = 0


_JuniQosStatisticsProfileCommittedDropThreshold_Object = MibTableColumn
juniQosStatisticsProfileCommittedDropThreshold = _JuniQosStatisticsProfileCommittedDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1, 5),
    _JuniQosStatisticsProfileCommittedDropThreshold_Type()
)
juniQosStatisticsProfileCommittedDropThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileCommittedDropThreshold.setStatus("current")


class _JuniQosStatisticsProfileConformedDropThreshold_Type(Unsigned32):
    """Custom type juniQosStatisticsProfileConformedDropThreshold based on Unsigned32"""
    defaultValue = 0


_JuniQosStatisticsProfileConformedDropThreshold_Object = MibTableColumn
juniQosStatisticsProfileConformedDropThreshold = _JuniQosStatisticsProfileConformedDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1, 6),
    _JuniQosStatisticsProfileConformedDropThreshold_Type()
)
juniQosStatisticsProfileConformedDropThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileConformedDropThreshold.setStatus("current")


class _JuniQosStatisticsProfileExceededDropThreshold_Type(Unsigned32):
    """Custom type juniQosStatisticsProfileExceededDropThreshold based on Unsigned32"""
    defaultValue = 0


_JuniQosStatisticsProfileExceededDropThreshold_Object = MibTableColumn
juniQosStatisticsProfileExceededDropThreshold = _JuniQosStatisticsProfileExceededDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1, 7),
    _JuniQosStatisticsProfileExceededDropThreshold_Type()
)
juniQosStatisticsProfileExceededDropThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileExceededDropThreshold.setStatus("current")


class _JuniQosStatisticsProfileRatePeriod_Type(Unsigned32):
    """Custom type juniQosStatisticsProfileRatePeriod based on Unsigned32"""
    defaultValue = 0


_JuniQosStatisticsProfileRatePeriod_Object = MibTableColumn
juniQosStatisticsProfileRatePeriod = _JuniQosStatisticsProfileRatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1, 8),
    _JuniQosStatisticsProfileRatePeriod_Type()
)
juniQosStatisticsProfileRatePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileRatePeriod.setStatus("current")
_JuniQosStatisticsProfileUpdatePending_Type = TruthValue
_JuniQosStatisticsProfileUpdatePending_Object = MibTableColumn
juniQosStatisticsProfileUpdatePending = _JuniQosStatisticsProfileUpdatePending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1, 9),
    _JuniQosStatisticsProfileUpdatePending_Type()
)
juniQosStatisticsProfileUpdatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileUpdatePending.setStatus("current")


class _JuniQosStatisticsProfileUpdateNow_Type(TruthValue):
    """Custom type juniQosStatisticsProfileUpdateNow based on TruthValue"""


_JuniQosStatisticsProfileUpdateNow_Object = MibTableColumn
juniQosStatisticsProfileUpdateNow = _JuniQosStatisticsProfileUpdateNow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1, 10),
    _JuniQosStatisticsProfileUpdateNow_Type()
)
juniQosStatisticsProfileUpdateNow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileUpdateNow.setStatus("current")
_JuniQosStatisticsProfileIsReferencedByQosProfile_Type = TruthValue
_JuniQosStatisticsProfileIsReferencedByQosProfile_Object = MibTableColumn
juniQosStatisticsProfileIsReferencedByQosProfile = _JuniQosStatisticsProfileIsReferencedByQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 15, 2, 1, 11),
    _JuniQosStatisticsProfileIsReferencedByQosProfile_Type()
)
juniQosStatisticsProfileIsReferencedByQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosStatisticsProfileIsReferencedByQosProfile.setStatus("current")
_JuniQosQosModePortList_ObjectIdentity = ObjectIdentity
juniQosQosModePortList = _JuniQosQosModePortList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 16)
)
_JuniQosQosModePortTable_Object = MibTable
juniQosQosModePortTable = _JuniQosQosModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 16, 1)
)
if mibBuilder.loadTexts:
    juniQosQosModePortTable.setStatus("current")
_JuniQosQosModePortEntry_Object = MibTableRow
juniQosQosModePortEntry = _JuniQosQosModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 16, 1, 1)
)
juniQosQosModePortEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosQosModePortIndex"),
)
if mibBuilder.loadTexts:
    juniQosQosModePortEntry.setStatus("current")
_JuniQosQosModePortIndex_Type = Unsigned32
_JuniQosQosModePortIndex_Object = MibTableColumn
juniQosQosModePortIndex = _JuniQosQosModePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 16, 1, 1, 1),
    _JuniQosQosModePortIndex_Type()
)
juniQosQosModePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosQosModePortIndex.setStatus("current")
_JuniQosQosModePortRowStatus_Type = RowStatus
_JuniQosQosModePortRowStatus_Object = MibTableColumn
juniQosQosModePortRowStatus = _JuniQosQosModePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 16, 1, 1, 2),
    _JuniQosQosModePortRowStatus_Type()
)
juniQosQosModePortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQosModePortRowStatus.setStatus("current")


class _JuniQosQosModePortFrameMode_Type(Integer32):
    """Custom type juniQosQosModePortFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lowCdv", 0),
          ("lowLatency", 1))
    )


_JuniQosQosModePortFrameMode_Type.__name__ = "Integer32"
_JuniQosQosModePortFrameMode_Object = MibTableColumn
juniQosQosModePortFrameMode = _JuniQosQosModePortFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 16, 1, 1, 3),
    _JuniQosQosModePortFrameMode_Type()
)
juniQosQosModePortFrameMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQosModePortFrameMode.setStatus("current")
_JuniQosQosShapingModeList_ObjectIdentity = ObjectIdentity
juniQosQosShapingModeList = _JuniQosQosShapingModeList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 17)
)
_JuniQosQosShapingModeTable_Object = MibTable
juniQosQosShapingModeTable = _JuniQosQosShapingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 17, 1)
)
if mibBuilder.loadTexts:
    juniQosQosShapingModeTable.setStatus("current")
_JuniQosQosShapingModeEntry_Object = MibTableRow
juniQosQosShapingModeEntry = _JuniQosQosShapingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 17, 1, 1)
)
juniQosQosShapingModeEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosQosShapingModeIndex"),
)
if mibBuilder.loadTexts:
    juniQosQosShapingModeEntry.setStatus("current")
_JuniQosQosShapingModeIndex_Type = Unsigned32
_JuniQosQosShapingModeIndex_Object = MibTableColumn
juniQosQosShapingModeIndex = _JuniQosQosShapingModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 17, 1, 1, 1),
    _JuniQosQosShapingModeIndex_Type()
)
juniQosQosShapingModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosQosShapingModeIndex.setStatus("current")
_JuniQosQosShapingModeRowStatus_Type = RowStatus
_JuniQosQosShapingModeRowStatus_Object = MibTableColumn
juniQosQosShapingModeRowStatus = _JuniQosQosShapingModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 17, 1, 1, 2),
    _JuniQosQosShapingModeRowStatus_Type()
)
juniQosQosShapingModeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQosShapingModeRowStatus.setStatus("current")


class _JuniQosQosShapingModeShapingMode_Type(Integer32):
    """Custom type juniQosQosShapingModeShapingMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cell", 1),
          ("frame", 0))
    )


_JuniQosQosShapingModeShapingMode_Type.__name__ = "Integer32"
_JuniQosQosShapingModeShapingMode_Object = MibTableColumn
juniQosQosShapingModeShapingMode = _JuniQosQosShapingModeShapingMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 17, 1, 1, 3),
    _JuniQosQosShapingModeShapingMode_Type()
)
juniQosQosShapingModeShapingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniQosQosShapingModeShapingMode.setStatus("current")
_JuniQosSVlanUidSupport_ObjectIdentity = ObjectIdentity
juniQosSVlanUidSupport = _JuniQosSVlanUidSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 18)
)
_JuniQosSVlanUidTable_Object = MibTable
juniQosSVlanUidTable = _JuniQosSVlanUidTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 18, 1)
)
if mibBuilder.loadTexts:
    juniQosSVlanUidTable.setStatus("current")
_JuniQosSVlanUidTableEntry_Object = MibTableRow
juniQosSVlanUidTableEntry = _JuniQosSVlanUidTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 18, 1, 1)
)
juniQosSVlanUidTableEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosSVlanUidTablePortUid"),
    (0, "Juniper-QoS-MIB", "juniQosSVlanUidTableSVlanId"),
)
if mibBuilder.loadTexts:
    juniQosSVlanUidTableEntry.setStatus("current")
_JuniQosSVlanUidTablePortUid_Type = Unsigned32
_JuniQosSVlanUidTablePortUid_Object = MibTableColumn
juniQosSVlanUidTablePortUid = _JuniQosSVlanUidTablePortUid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 18, 1, 1, 1),
    _JuniQosSVlanUidTablePortUid_Type()
)
juniQosSVlanUidTablePortUid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosSVlanUidTablePortUid.setStatus("current")


class _JuniQosSVlanUidTableSVlanId_Type(Unsigned32):
    """Custom type juniQosSVlanUidTableSVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_JuniQosSVlanUidTableSVlanId_Type.__name__ = "Unsigned32"
_JuniQosSVlanUidTableSVlanId_Object = MibTableColumn
juniQosSVlanUidTableSVlanId = _JuniQosSVlanUidTableSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 18, 1, 1, 2),
    _JuniQosSVlanUidTableSVlanId_Type()
)
juniQosSVlanUidTableSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosSVlanUidTableSVlanId.setStatus("current")
_JuniQosSVlanUidTableSVlanUid_Type = Unsigned32
_JuniQosSVlanUidTableSVlanUid_Object = MibTableColumn
juniQosSVlanUidTableSVlanUid = _JuniQosSVlanUidTableSVlanUid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 18, 1, 1, 3),
    _JuniQosSVlanUidTableSVlanUid_Type()
)
juniQosSVlanUidTableSVlanUid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosSVlanUidTableSVlanUid.setStatus("current")
_JuniQosSVlanIdSupport_ObjectIdentity = ObjectIdentity
juniQosSVlanIdSupport = _JuniQosSVlanIdSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 19)
)
_JuniQosSVlanIdTable_Object = MibTable
juniQosSVlanIdTable = _JuniQosSVlanIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 19, 1)
)
if mibBuilder.loadTexts:
    juniQosSVlanIdTable.setStatus("current")
_JuniQosSVlanIdTableEntry_Object = MibTableRow
juniQosSVlanIdTableEntry = _JuniQosSVlanIdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 19, 1, 1)
)
juniQosSVlanIdTableEntry.setIndexNames(
    (0, "Juniper-QoS-MIB", "juniQosSVlanIdTableSVlanUid"),
)
if mibBuilder.loadTexts:
    juniQosSVlanIdTableEntry.setStatus("current")
_JuniQosSVlanIdTableSVlanUid_Type = Unsigned32
_JuniQosSVlanIdTableSVlanUid_Object = MibTableColumn
juniQosSVlanIdTableSVlanUid = _JuniQosSVlanIdTableSVlanUid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 19, 1, 1, 1),
    _JuniQosSVlanIdTableSVlanUid_Type()
)
juniQosSVlanIdTableSVlanUid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniQosSVlanIdTableSVlanUid.setStatus("current")
_JuniQosSVlanIdTablePortUid_Type = Unsigned32
_JuniQosSVlanIdTablePortUid_Object = MibTableColumn
juniQosSVlanIdTablePortUid = _JuniQosSVlanIdTablePortUid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 19, 1, 1, 2),
    _JuniQosSVlanIdTablePortUid_Type()
)
juniQosSVlanIdTablePortUid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosSVlanIdTablePortUid.setStatus("current")


class _JuniQosSVlanIdTableSVlanId_Type(Unsigned32):
    """Custom type juniQosSVlanIdTableSVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_JuniQosSVlanIdTableSVlanId_Type.__name__ = "Unsigned32"
_JuniQosSVlanIdTableSVlanId_Object = MibTableColumn
juniQosSVlanIdTableSVlanId = _JuniQosSVlanIdTableSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 1, 19, 1, 1, 3),
    _JuniQosSVlanIdTableSVlanId_Type()
)
juniQosSVlanIdTableSVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniQosSVlanIdTableSVlanId.setStatus("current")
_JuniQosConformance_ObjectIdentity = ObjectIdentity
juniQosConformance = _JuniQosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2)
)
_JuniQosCompliances_ObjectIdentity = ObjectIdentity
juniQosCompliances = _JuniQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 1)
)
_JuniQosGroups_ObjectIdentity = ObjectIdentity
juniQosGroups = _JuniQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2)
)

# Managed Objects groups

juniQosCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 1)
)
juniQosCapabilityGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosMaxTrafficClass"),
        ("Juniper-QoS-MIB", "juniQosMaxQueueLength"),
        ("Juniper-QoS-MIB", "juniQosMinSchedulerBurst"),
        ("Juniper-QoS-MIB", "juniQosMaxSchedulerBurst"),
        ("Juniper-QoS-MIB", "juniQosMaxQosProfileRules"))
)
if mibBuilder.loadTexts:
    juniQosCapabilityGroup.setStatus("current")

juniQosScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 2)
)
juniQosScalarGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosTrafficClassCount"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileCount"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileCount"),
        ("Juniper-QoS-MIB", "juniQosProfileCount"),
        ("Juniper-QoS-MIB", "juniQosInterfaceCount"),
        ("Juniper-QoS-MIB", "juniQosQosPortTypeProfileCount"))
)
if mibBuilder.loadTexts:
    juniQosScalarGroup.setStatus("obsolete")

juniQosTrafficClassListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 3)
)
juniQosTrafficClassListGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosTrafficClassNextIndex"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassRowStatus"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassName"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassWeight"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassStrictPriority"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassUpdatePending"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassUpdateNow"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassIsReferencedByGroup"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassIsReferencedByQosProfile"))
)
if mibBuilder.loadTexts:
    juniQosTrafficClassListGroup.setStatus("current")

juniQosTrafficClassGroupListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 4)
)
juniQosTrafficClassGroupListGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosTrafficClassGroupNextIndex"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupRowStatus"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupName"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupUpdatePending"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupUpdateNow"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupIsReferencedByQosProfile"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupEntryRowStatus"))
)
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupListGroup.setStatus("obsolete")

juniQosQueueProfileListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 5)
)
juniQosQueueProfileListGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosQueueProfileNextIndex"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileRowStatus"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileName"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileCommittedMinLength"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileCommittedMaxLength"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileConformedMinLength"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileConformedMaxLength"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileExceededMinLength"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileExceededMaxLength"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileConformedFraction"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileExceededFraction"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileCommittedDropThreshold"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileCommittedDropRate"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileConformedDropThreshold"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileConformedDropRate"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileExceededDropThreshold"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileExceededDropRate"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileBufferWeight"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileUpdatePending"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileUpdateNow"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileIsReferencedByQosProfile"))
)
if mibBuilder.loadTexts:
    juniQosQueueProfileListGroup.setStatus("current")

juniQosSchedulerProfileListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 6)
)
juniQosSchedulerProfileListGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosSchedulerProfileNextIndex"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileRowStatus"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileName"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileShapingRate"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileBurst"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileWeight"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileStrictPriority"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileUpdatePending"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileUpdateNow"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileIsReferencedByQosProfile"))
)
if mibBuilder.loadTexts:
    juniQosSchedulerProfileListGroup.setStatus("obsolete")

juniQosProfileListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 7)
)
juniQosProfileListGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosProfileNextIndex"),
        ("Juniper-QoS-MIB", "juniQosProfileRowStatus"),
        ("Juniper-QoS-MIB", "juniQosProfileName"),
        ("Juniper-QoS-MIB", "juniQosProfileUpdatePending"),
        ("Juniper-QoS-MIB", "juniQosProfileUpdateNow"),
        ("Juniper-QoS-MIB", "juniQosProfileIsReferencedByInterfaceQosAttachment"),
        ("Juniper-QoS-MIB", "juniQosProfileIsReferencedByQosPortTypeProfile"))
)
if mibBuilder.loadTexts:
    juniQosProfileListGroup.setStatus("current")

juniQosProfileElementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 8)
)
juniQosProfileElementGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosProfileElementEntryRowStatus"),
        ("Juniper-QoS-MIB", "juniQosProfileElementEntryQueueProfile"),
        ("Juniper-QoS-MIB", "juniQosProfileElementEntrySchedulerProfile"))
)
if mibBuilder.loadTexts:
    juniQosProfileElementGroup.setStatus("obsolete")

juniQosIfAttachGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 9)
)
juniQosIfAttachGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosIfAttachRowStatus"),
        ("Juniper-QoS-MIB", "juniQosIfAttachQosProfileIndex"))
)
if mibBuilder.loadTexts:
    juniQosIfAttachGroup.setStatus("current")

juniQosQosPortTypeProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 10)
)
juniQosQosPortTypeProfileGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosQosPortTypeProfileRowStatus"),
        ("Juniper-QoS-MIB", "juniQosQosPortTypeProfileQosProfileIndex"))
)
if mibBuilder.loadTexts:
    juniQosQosPortTypeProfileGroup.setStatus("current")

juniQosQueueStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 11)
)
juniQosQueueStatisticsGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosOutPacketForwarded"),
        ("Juniper-QoS-MIB", "juniQosOutBytesForwarded"),
        ("Juniper-QoS-MIB", "juniQosOutGreenPacketsSchedulerDrops"),
        ("Juniper-QoS-MIB", "juniQosOutYellowPacketsSchedulerDrops"),
        ("Juniper-QoS-MIB", "juniQosOutRedPacketsSchedulerDrops"),
        ("Juniper-QoS-MIB", "juniQosOutGreenBytesSchedulerDrops"),
        ("Juniper-QoS-MIB", "juniQosOutYellowBytesSchedulerDrops"),
        ("Juniper-QoS-MIB", "juniQosOutRedBytesSchedulerDrops"))
)
if mibBuilder.loadTexts:
    juniQosQueueStatisticsGroup.setStatus("current")

juniQosScalarGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 12)
)
juniQosScalarGroup2.setObjects(
      *(("Juniper-QoS-MIB", "juniQosTrafficClassCount"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileCount"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileCount"),
        ("Juniper-QoS-MIB", "juniQosProfileCount"),
        ("Juniper-QoS-MIB", "juniQosInterfaceCount"),
        ("Juniper-QoS-MIB", "juniQosQosPortTypeProfileCount"),
        ("Juniper-QoS-MIB", "juniQosDropProfileCount"))
)
if mibBuilder.loadTexts:
    juniQosScalarGroup2.setStatus("obsolete")

juniQosProfileElementGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 13)
)
juniQosProfileElementGroup2.setObjects(
      *(("Juniper-QoS-MIB", "juniQosProfileElementEntryRowStatus"),
        ("Juniper-QoS-MIB", "juniQosProfileElementEntryQueueProfile"),
        ("Juniper-QoS-MIB", "juniQosProfileElementEntrySchedulerProfile"),
        ("Juniper-QoS-MIB", "juniQosProfileElementEntryDropProfile"))
)
if mibBuilder.loadTexts:
    juniQosProfileElementGroup2.setStatus("obsolete")

juniQosDropProfileListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 14)
)
juniQosDropProfileListGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosDropProfileNextIndex"),
        ("Juniper-QoS-MIB", "juniQosDropProfileRowStatus"),
        ("Juniper-QoS-MIB", "juniQosDropProfileName"),
        ("Juniper-QoS-MIB", "juniQosDropProfileAverageLengthExponent"),
        ("Juniper-QoS-MIB", "juniQosDropProfileCommittedThresholdUnits"),
        ("Juniper-QoS-MIB", "juniQosDropProfileCommittedThresholdMinThreshold"),
        ("Juniper-QoS-MIB", "juniQosDropProfileCommittedThresholdMaxThreshold"),
        ("Juniper-QoS-MIB", "juniQosDropProfileCommittedThresholdMaxDropProbability"),
        ("Juniper-QoS-MIB", "juniQosDropProfileConformedThresholdUnits"),
        ("Juniper-QoS-MIB", "juniQosDropProfileConformedThresholdMinThreshold"),
        ("Juniper-QoS-MIB", "juniQosDropProfileConformedThresholdMaxThreshold"),
        ("Juniper-QoS-MIB", "juniQosDropProfileConformedThresholdMaxDropProbability"),
        ("Juniper-QoS-MIB", "juniQosDropProfileExceededThresholdUnits"),
        ("Juniper-QoS-MIB", "juniQosDropProfileExceededThresholdMinThreshold"),
        ("Juniper-QoS-MIB", "juniQosDropProfileExceededThresholdMaxThreshold"),
        ("Juniper-QoS-MIB", "juniQosDropProfileExceededThresholdMaxDropProbability"),
        ("Juniper-QoS-MIB", "juniQosDropProfileUpdatePending"),
        ("Juniper-QoS-MIB", "juniQosDropProfileUpdateNow"),
        ("Juniper-QoS-MIB", "juniQosDropProfileIsReferencedByQosProfile"))
)
if mibBuilder.loadTexts:
    juniQosDropProfileListGroup.setStatus("current")

juniQosAtmVpUidSupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 15)
)
juniQosAtmVpUidSupportGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosAtmVpUidValid"),
        ("Juniper-QoS-MIB", "juniQosAtmVpAtmPortInterfaceUid"),
        ("Juniper-QoS-MIB", "juniQosAtmVpAtmPath"),
        ("Juniper-QoS-MIB", "juniQosAtmVpUid"))
)
if mibBuilder.loadTexts:
    juniQosAtmVpUidSupportGroup.setStatus("current")

juniQosScalarGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 16)
)
juniQosScalarGroup3.setObjects(
      *(("Juniper-QoS-MIB", "juniQosTrafficClassCount"),
        ("Juniper-QoS-MIB", "juniQosQueueProfileCount"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileCount"),
        ("Juniper-QoS-MIB", "juniQosProfileCount"),
        ("Juniper-QoS-MIB", "juniQosInterfaceCount"),
        ("Juniper-QoS-MIB", "juniQosQosPortTypeProfileCount"),
        ("Juniper-QoS-MIB", "juniQosDropProfileCount"),
        ("Juniper-QoS-MIB", "juniQosStatisticsProfileCount"))
)
if mibBuilder.loadTexts:
    juniQosScalarGroup3.setStatus("current")

juniQosProfileElementGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 17)
)
juniQosProfileElementGroup3.setObjects(
      *(("Juniper-QoS-MIB", "juniQosProfileElementEntryRowStatus"),
        ("Juniper-QoS-MIB", "juniQosProfileElementEntryQueueProfile"),
        ("Juniper-QoS-MIB", "juniQosProfileElementEntrySchedulerProfile"),
        ("Juniper-QoS-MIB", "juniQosProfileElementEntryDropProfile"),
        ("Juniper-QoS-MIB", "juniQosProfileElementEntryStatisticsProfile"))
)
if mibBuilder.loadTexts:
    juniQosProfileElementGroup3.setStatus("current")

juniQosStatisticsProfileListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 18)
)
juniQosStatisticsProfileListGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosStatisticsProfileNextIndex"),
        ("Juniper-QoS-MIB", "juniQosStatisticsProfileRowStatus"),
        ("Juniper-QoS-MIB", "juniQosStatisticsProfileName"),
        ("Juniper-QoS-MIB", "juniQosStatisticsProfileForwardingRateThreshold"),
        ("Juniper-QoS-MIB", "juniQosStatisticsProfileCommittedDropThreshold"),
        ("Juniper-QoS-MIB", "juniQosStatisticsProfileConformedDropThreshold"),
        ("Juniper-QoS-MIB", "juniQosStatisticsProfileExceededDropThreshold"),
        ("Juniper-QoS-MIB", "juniQosStatisticsProfileRatePeriod"),
        ("Juniper-QoS-MIB", "juniQosStatisticsProfileUpdatePending"),
        ("Juniper-QoS-MIB", "juniQosStatisticsProfileUpdateNow"),
        ("Juniper-QoS-MIB", "juniQosStatisticsProfileIsReferencedByQosProfile"))
)
if mibBuilder.loadTexts:
    juniQosStatisticsProfileListGroup.setStatus("current")

juniQosSchedulerProfileListGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 19)
)
juniQosSchedulerProfileListGroup2.setObjects(
      *(("Juniper-QoS-MIB", "juniQosSchedulerProfileNextIndex"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileRowStatus"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileName"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileShapingRate"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileBurst"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileWeight"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileStrictPriority"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileUpdatePending"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileUpdateNow"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileIsReferencedByQosProfile"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileAssuredRate"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingRate"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingBurstSize"))
)
if mibBuilder.loadTexts:
    juniQosSchedulerProfileListGroup2.setStatus("current")

juniQosQosModePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 20)
)
juniQosQosModePortGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosQosModePortRowStatus"),
        ("Juniper-QoS-MIB", "juniQosQosModePortFrameMode"))
)
if mibBuilder.loadTexts:
    juniQosQosModePortGroup.setStatus("current")

juniQosQosShapingModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 21)
)
juniQosQosShapingModeGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosQosShapingModeRowStatus"),
        ("Juniper-QoS-MIB", "juniQosQosShapingModeShapingMode"))
)
if mibBuilder.loadTexts:
    juniQosQosShapingModeGroup.setStatus("current")

juniQosTrafficClassGroupListGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 22)
)
juniQosTrafficClassGroupListGroup2.setObjects(
      *(("Juniper-QoS-MIB", "juniQosTrafficClassGroupNextIndex"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupRowStatus"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupName"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupUpdatePending"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupUpdateNow"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupIsReferencedByQosProfile"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupSlotNumber"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupExtendedGroup"),
        ("Juniper-QoS-MIB", "juniQosTrafficClassGroupEntryRowStatus"))
)
if mibBuilder.loadTexts:
    juniQosTrafficClassGroupListGroup2.setStatus("current")

juniQosSchedulerProfileListGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 23)
)
juniQosSchedulerProfileListGroup3.setObjects(
      *(("Juniper-QoS-MIB", "juniQosSchedulerProfileNextIndex"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileRowStatus"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileName"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileShapingRate"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileBurst"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileWeight"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileStrictPriority"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileUpdatePending"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileUpdateNow"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileIsReferencedByQosProfile"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileAssuredRate"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingRate"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingBurstSize"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingType"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingExplicitConstituents"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingPriority"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingWeight"))
)
if mibBuilder.loadTexts:
    juniQosSchedulerProfileListGroup3.setStatus("current")

juniQosSchedulerProfileListGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 24)
)
juniQosSchedulerProfileListGroup4.setObjects(
      *(("Juniper-QoS-MIB", "juniQosSchedulerProfileNextIndex"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileRowStatus"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileName"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileShapingRate"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileBurst"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileWeight"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileStrictPriority"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileUpdatePending"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileUpdateNow"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileIsReferencedByQosProfile"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileAssuredRate"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingRate"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingBurstSize"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingType"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingExplicitConstituents"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingPriority"),
        ("Juniper-QoS-MIB", "juniQosSchedulerProfileSharedShapingWeight"))
)
if mibBuilder.loadTexts:
    juniQosSchedulerProfileListGroup4.setStatus("current")

juniQosSVlanUidSupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 25)
)
juniQosSVlanUidSupportGroup.setObjects(
    ("Juniper-QoS-MIB", "juniQosSVlanUidTableSVlanUid")
)
if mibBuilder.loadTexts:
    juniQosSVlanUidSupportGroup.setStatus("current")

juniQosSVlanIdSupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 2, 26)
)
juniQosSVlanIdSupportGroup.setObjects(
      *(("Juniper-QoS-MIB", "juniQosSVlanIdTablePortUid"),
        ("Juniper-QoS-MIB", "juniQosSVlanIdTableSVlanId"))
)
if mibBuilder.loadTexts:
    juniQosSVlanIdSupportGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniQosCompliance.setStatus(
        "obsolete"
    )

juniQosCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniQosCompliance2.setStatus(
        "obsolete"
    )

juniQosCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 1, 3)
)
if mibBuilder.loadTexts:
    juniQosCompliance3.setStatus(
        "obsolete"
    )

juniQosCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 1, 4)
)
if mibBuilder.loadTexts:
    juniQosCompliance4.setStatus(
        "obsolete"
    )

juniQosCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 1, 5)
)
if mibBuilder.loadTexts:
    juniQosCompliance5.setStatus(
        "current"
    )

juniQosCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57, 2, 1, 6)
)
if mibBuilder.loadTexts:
    juniQosCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-QoS-MIB",
    **{"JuniQosLogicalInterfaceType": JuniQosLogicalInterfaceType,
       "juniQosMIB": juniQosMIB,
       "juniQosObjects": juniQosObjects,
       "juniQosCapability": juniQosCapability,
       "juniQosMaxTrafficClass": juniQosMaxTrafficClass,
       "juniQosMaxQueueLength": juniQosMaxQueueLength,
       "juniQosMinSchedulerBurst": juniQosMinSchedulerBurst,
       "juniQosMaxSchedulerBurst": juniQosMaxSchedulerBurst,
       "juniQosMaxQosProfileRules": juniQosMaxQosProfileRules,
       "juniQos": juniQos,
       "juniQosTrafficClassCount": juniQosTrafficClassCount,
       "juniQosQueueProfileCount": juniQosQueueProfileCount,
       "juniQosSchedulerProfileCount": juniQosSchedulerProfileCount,
       "juniQosProfileCount": juniQosProfileCount,
       "juniQosInterfaceCount": juniQosInterfaceCount,
       "juniQosQosPortTypeProfileCount": juniQosQosPortTypeProfileCount,
       "juniQosDropProfileCount": juniQosDropProfileCount,
       "juniQosStatisticsProfileCount": juniQosStatisticsProfileCount,
       "juniQosTrafficClassList": juniQosTrafficClassList,
       "juniQosTrafficClassNextIndex": juniQosTrafficClassNextIndex,
       "juniQosTrafficClassTable": juniQosTrafficClassTable,
       "juniQosTrafficClassEntry": juniQosTrafficClassEntry,
       "juniQosTrafficClassIndex": juniQosTrafficClassIndex,
       "juniQosTrafficClassRowStatus": juniQosTrafficClassRowStatus,
       "juniQosTrafficClassName": juniQosTrafficClassName,
       "juniQosTrafficClassWeight": juniQosTrafficClassWeight,
       "juniQosTrafficClassStrictPriority": juniQosTrafficClassStrictPriority,
       "juniQosTrafficClassUpdatePending": juniQosTrafficClassUpdatePending,
       "juniQosTrafficClassUpdateNow": juniQosTrafficClassUpdateNow,
       "juniQosTrafficClassIsReferencedByGroup": juniQosTrafficClassIsReferencedByGroup,
       "juniQosTrafficClassIsReferencedByQosProfile": juniQosTrafficClassIsReferencedByQosProfile,
       "juniQosTrafficClassGroupList": juniQosTrafficClassGroupList,
       "juniQosTrafficClassGroupNextIndex": juniQosTrafficClassGroupNextIndex,
       "juniQosTrafficClassGroupTable": juniQosTrafficClassGroupTable,
       "juniQosTrafficClassGroupEntry": juniQosTrafficClassGroupEntry,
       "juniQosTrafficClassGroupIndex": juniQosTrafficClassGroupIndex,
       "juniQosTrafficClassGroupRowStatus": juniQosTrafficClassGroupRowStatus,
       "juniQosTrafficClassGroupName": juniQosTrafficClassGroupName,
       "juniQosTrafficClassGroupUpdatePending": juniQosTrafficClassGroupUpdatePending,
       "juniQosTrafficClassGroupUpdateNow": juniQosTrafficClassGroupUpdateNow,
       "juniQosTrafficClassGroupIsReferencedByQosProfile": juniQosTrafficClassGroupIsReferencedByQosProfile,
       "juniQosTrafficClassGroupSlotNumber": juniQosTrafficClassGroupSlotNumber,
       "juniQosTrafficClassGroupExtendedGroup": juniQosTrafficClassGroupExtendedGroup,
       "juniQosTrafficClassGroupEntryList": juniQosTrafficClassGroupEntryList,
       "juniQosTrafficClassGroupEntryTable": juniQosTrafficClassGroupEntryTable,
       "juniQosTrafficClassGroupEntryEntry": juniQosTrafficClassGroupEntryEntry,
       "juniQosTrafficClassGroupEntryRowStatus": juniQosTrafficClassGroupEntryRowStatus,
       "juniQosSchedulerProfileList": juniQosSchedulerProfileList,
       "juniQosSchedulerProfileNextIndex": juniQosSchedulerProfileNextIndex,
       "juniQosSchedulerProfileTable": juniQosSchedulerProfileTable,
       "juniQosSchedulerProfileEntry": juniQosSchedulerProfileEntry,
       "juniQosSchedulerProfileIndex": juniQosSchedulerProfileIndex,
       "juniQosSchedulerProfileRowStatus": juniQosSchedulerProfileRowStatus,
       "juniQosSchedulerProfileName": juniQosSchedulerProfileName,
       "juniQosSchedulerProfileShapingRate": juniQosSchedulerProfileShapingRate,
       "juniQosSchedulerProfileBurst": juniQosSchedulerProfileBurst,
       "juniQosSchedulerProfileWeight": juniQosSchedulerProfileWeight,
       "juniQosSchedulerProfileStrictPriority": juniQosSchedulerProfileStrictPriority,
       "juniQosSchedulerProfileUpdatePending": juniQosSchedulerProfileUpdatePending,
       "juniQosSchedulerProfileUpdateNow": juniQosSchedulerProfileUpdateNow,
       "juniQosSchedulerProfileIsReferencedByQosProfile": juniQosSchedulerProfileIsReferencedByQosProfile,
       "juniQosSchedulerProfileAssuredRate": juniQosSchedulerProfileAssuredRate,
       "juniQosSchedulerProfileSharedShapingRate": juniQosSchedulerProfileSharedShapingRate,
       "juniQosSchedulerProfileSharedShapingBurstSize": juniQosSchedulerProfileSharedShapingBurstSize,
       "juniQosSchedulerProfileSharedShapingType": juniQosSchedulerProfileSharedShapingType,
       "juniQosSchedulerProfileSharedShapingExplicitConstituents": juniQosSchedulerProfileSharedShapingExplicitConstituents,
       "juniQosSchedulerProfileSharedShapingPriority": juniQosSchedulerProfileSharedShapingPriority,
       "juniQosSchedulerProfileSharedShapingWeight": juniQosSchedulerProfileSharedShapingWeight,
       "juniQosQueueProfileList": juniQosQueueProfileList,
       "juniQosQueueProfileNextIndex": juniQosQueueProfileNextIndex,
       "juniQosQueueProfileTable": juniQosQueueProfileTable,
       "juniQosQueueProfileEntry": juniQosQueueProfileEntry,
       "juniQosQueueProfileIndex": juniQosQueueProfileIndex,
       "juniQosQueueProfileRowStatus": juniQosQueueProfileRowStatus,
       "juniQosQueueProfileName": juniQosQueueProfileName,
       "juniQosQueueProfileCommittedMinLength": juniQosQueueProfileCommittedMinLength,
       "juniQosQueueProfileCommittedMaxLength": juniQosQueueProfileCommittedMaxLength,
       "juniQosQueueProfileConformedMinLength": juniQosQueueProfileConformedMinLength,
       "juniQosQueueProfileConformedMaxLength": juniQosQueueProfileConformedMaxLength,
       "juniQosQueueProfileExceededMinLength": juniQosQueueProfileExceededMinLength,
       "juniQosQueueProfileExceededMaxLength": juniQosQueueProfileExceededMaxLength,
       "juniQosQueueProfileConformedFraction": juniQosQueueProfileConformedFraction,
       "juniQosQueueProfileExceededFraction": juniQosQueueProfileExceededFraction,
       "juniQosQueueProfileCommittedDropThreshold": juniQosQueueProfileCommittedDropThreshold,
       "juniQosQueueProfileCommittedDropRate": juniQosQueueProfileCommittedDropRate,
       "juniQosQueueProfileConformedDropThreshold": juniQosQueueProfileConformedDropThreshold,
       "juniQosQueueProfileConformedDropRate": juniQosQueueProfileConformedDropRate,
       "juniQosQueueProfileExceededDropThreshold": juniQosQueueProfileExceededDropThreshold,
       "juniQosQueueProfileExceededDropRate": juniQosQueueProfileExceededDropRate,
       "juniQosQueueProfileBufferWeight": juniQosQueueProfileBufferWeight,
       "juniQosQueueProfileUpdatePending": juniQosQueueProfileUpdatePending,
       "juniQosQueueProfileUpdateNow": juniQosQueueProfileUpdateNow,
       "juniQosQueueProfileIsReferencedByQosProfile": juniQosQueueProfileIsReferencedByQosProfile,
       "juniQosProfile": juniQosProfile,
       "juniQosProfileNextIndex": juniQosProfileNextIndex,
       "juniQosProfileTable": juniQosProfileTable,
       "juniQosProfileEntry": juniQosProfileEntry,
       "juniQosProfileIndex": juniQosProfileIndex,
       "juniQosProfileRowStatus": juniQosProfileRowStatus,
       "juniQosProfileName": juniQosProfileName,
       "juniQosProfileUpdatePending": juniQosProfileUpdatePending,
       "juniQosProfileUpdateNow": juniQosProfileUpdateNow,
       "juniQosProfileIsReferencedByInterfaceQosAttachment": juniQosProfileIsReferencedByInterfaceQosAttachment,
       "juniQosProfileIsReferencedByQosPortTypeProfile": juniQosProfileIsReferencedByQosPortTypeProfile,
       "juniQosProfileElement": juniQosProfileElement,
       "juniQosProfileElementTable": juniQosProfileElementTable,
       "juniQosProfileElementEntry": juniQosProfileElementEntry,
       "juniQosProfileElementEntryRowStatus": juniQosProfileElementEntryRowStatus,
       "juniQosProfileElementEntryQueueProfile": juniQosProfileElementEntryQueueProfile,
       "juniQosProfileElementEntrySchedulerProfile": juniQosProfileElementEntrySchedulerProfile,
       "juniQosInterfaceType": juniQosInterfaceType,
       "juniQosProfileEntryType": juniQosProfileEntryType,
       "juniQosProfileElementEntryDropProfile": juniQosProfileElementEntryDropProfile,
       "juniQosProfileElementEntryStatisticsProfile": juniQosProfileElementEntryStatisticsProfile,
       "juniQosIfAttach": juniQosIfAttach,
       "juniQosIfAttachTable": juniQosIfAttachTable,
       "juniQosIfAttachEntry": juniQosIfAttachEntry,
       "juniQosIfAttachIndex": juniQosIfAttachIndex,
       "juniQosIfAttachRowStatus": juniQosIfAttachRowStatus,
       "juniQosIfAttachQosProfileIndex": juniQosIfAttachQosProfileIndex,
       "juniQosQosPortTypeProfile": juniQosQosPortTypeProfile,
       "juniQosQosPortTypeProfileTable": juniQosQosPortTypeProfileTable,
       "juniQosQosPortTypeProfileEntry": juniQosQosPortTypeProfileEntry,
       "juniQosQosPortTypeProfileIndex": juniQosQosPortTypeProfileIndex,
       "juniQosQosPortTypeProfileRowStatus": juniQosQosPortTypeProfileRowStatus,
       "juniQosQosPortTypeProfileQosProfileIndex": juniQosQosPortTypeProfileQosProfileIndex,
       "juniQosQueueStatistics": juniQosQueueStatistics,
       "juniQosQueueStatisticsTable": juniQosQueueStatisticsTable,
       "juniQosQueueStatisticsEntry": juniQosQueueStatisticsEntry,
       "juniQosOutPacketForwarded": juniQosOutPacketForwarded,
       "juniQosOutBytesForwarded": juniQosOutBytesForwarded,
       "juniQosOutGreenPacketsSchedulerDrops": juniQosOutGreenPacketsSchedulerDrops,
       "juniQosOutYellowPacketsSchedulerDrops": juniQosOutYellowPacketsSchedulerDrops,
       "juniQosOutRedPacketsSchedulerDrops": juniQosOutRedPacketsSchedulerDrops,
       "juniQosOutGreenBytesSchedulerDrops": juniQosOutGreenBytesSchedulerDrops,
       "juniQosOutYellowBytesSchedulerDrops": juniQosOutYellowBytesSchedulerDrops,
       "juniQosOutRedBytesSchedulerDrops": juniQosOutRedBytesSchedulerDrops,
       "juniQosDropProfileList": juniQosDropProfileList,
       "juniQosDropProfileNextIndex": juniQosDropProfileNextIndex,
       "juniQosDropProfileTable": juniQosDropProfileTable,
       "juniQosDropProfileEntry": juniQosDropProfileEntry,
       "juniQosDropProfileIndex": juniQosDropProfileIndex,
       "juniQosDropProfileRowStatus": juniQosDropProfileRowStatus,
       "juniQosDropProfileName": juniQosDropProfileName,
       "juniQosDropProfileAverageLengthExponent": juniQosDropProfileAverageLengthExponent,
       "juniQosDropProfileCommittedThresholdUnits": juniQosDropProfileCommittedThresholdUnits,
       "juniQosDropProfileCommittedThresholdMinThreshold": juniQosDropProfileCommittedThresholdMinThreshold,
       "juniQosDropProfileCommittedThresholdMaxThreshold": juniQosDropProfileCommittedThresholdMaxThreshold,
       "juniQosDropProfileCommittedThresholdMaxDropProbability": juniQosDropProfileCommittedThresholdMaxDropProbability,
       "juniQosDropProfileConformedThresholdUnits": juniQosDropProfileConformedThresholdUnits,
       "juniQosDropProfileConformedThresholdMinThreshold": juniQosDropProfileConformedThresholdMinThreshold,
       "juniQosDropProfileConformedThresholdMaxThreshold": juniQosDropProfileConformedThresholdMaxThreshold,
       "juniQosDropProfileConformedThresholdMaxDropProbability": juniQosDropProfileConformedThresholdMaxDropProbability,
       "juniQosDropProfileExceededThresholdUnits": juniQosDropProfileExceededThresholdUnits,
       "juniQosDropProfileExceededThresholdMinThreshold": juniQosDropProfileExceededThresholdMinThreshold,
       "juniQosDropProfileExceededThresholdMaxThreshold": juniQosDropProfileExceededThresholdMaxThreshold,
       "juniQosDropProfileExceededThresholdMaxDropProbability": juniQosDropProfileExceededThresholdMaxDropProbability,
       "juniQosDropProfileUpdatePending": juniQosDropProfileUpdatePending,
       "juniQosDropProfileUpdateNow": juniQosDropProfileUpdateNow,
       "juniQosDropProfileIsReferencedByQosProfile": juniQosDropProfileIsReferencedByQosProfile,
       "juniQosAtmVpUidSupport": juniQosAtmVpUidSupport,
       "juniQosAtmVpUidValid": juniQosAtmVpUidValid,
       "juniQosAtmVpAtmPortInterfaceUid": juniQosAtmVpAtmPortInterfaceUid,
       "juniQosAtmVpAtmPath": juniQosAtmVpAtmPath,
       "juniQosAtmVpUid": juniQosAtmVpUid,
       "juniQosStatisticsProfileList": juniQosStatisticsProfileList,
       "juniQosStatisticsProfileNextIndex": juniQosStatisticsProfileNextIndex,
       "juniQosStatisticsProfileTable": juniQosStatisticsProfileTable,
       "juniQosStatisticsProfileEntry": juniQosStatisticsProfileEntry,
       "juniQosStatisticsProfileIndex": juniQosStatisticsProfileIndex,
       "juniQosStatisticsProfileRowStatus": juniQosStatisticsProfileRowStatus,
       "juniQosStatisticsProfileName": juniQosStatisticsProfileName,
       "juniQosStatisticsProfileForwardingRateThreshold": juniQosStatisticsProfileForwardingRateThreshold,
       "juniQosStatisticsProfileCommittedDropThreshold": juniQosStatisticsProfileCommittedDropThreshold,
       "juniQosStatisticsProfileConformedDropThreshold": juniQosStatisticsProfileConformedDropThreshold,
       "juniQosStatisticsProfileExceededDropThreshold": juniQosStatisticsProfileExceededDropThreshold,
       "juniQosStatisticsProfileRatePeriod": juniQosStatisticsProfileRatePeriod,
       "juniQosStatisticsProfileUpdatePending": juniQosStatisticsProfileUpdatePending,
       "juniQosStatisticsProfileUpdateNow": juniQosStatisticsProfileUpdateNow,
       "juniQosStatisticsProfileIsReferencedByQosProfile": juniQosStatisticsProfileIsReferencedByQosProfile,
       "juniQosQosModePortList": juniQosQosModePortList,
       "juniQosQosModePortTable": juniQosQosModePortTable,
       "juniQosQosModePortEntry": juniQosQosModePortEntry,
       "juniQosQosModePortIndex": juniQosQosModePortIndex,
       "juniQosQosModePortRowStatus": juniQosQosModePortRowStatus,
       "juniQosQosModePortFrameMode": juniQosQosModePortFrameMode,
       "juniQosQosShapingModeList": juniQosQosShapingModeList,
       "juniQosQosShapingModeTable": juniQosQosShapingModeTable,
       "juniQosQosShapingModeEntry": juniQosQosShapingModeEntry,
       "juniQosQosShapingModeIndex": juniQosQosShapingModeIndex,
       "juniQosQosShapingModeRowStatus": juniQosQosShapingModeRowStatus,
       "juniQosQosShapingModeShapingMode": juniQosQosShapingModeShapingMode,
       "juniQosSVlanUidSupport": juniQosSVlanUidSupport,
       "juniQosSVlanUidTable": juniQosSVlanUidTable,
       "juniQosSVlanUidTableEntry": juniQosSVlanUidTableEntry,
       "juniQosSVlanUidTablePortUid": juniQosSVlanUidTablePortUid,
       "juniQosSVlanUidTableSVlanId": juniQosSVlanUidTableSVlanId,
       "juniQosSVlanUidTableSVlanUid": juniQosSVlanUidTableSVlanUid,
       "juniQosSVlanIdSupport": juniQosSVlanIdSupport,
       "juniQosSVlanIdTable": juniQosSVlanIdTable,
       "juniQosSVlanIdTableEntry": juniQosSVlanIdTableEntry,
       "juniQosSVlanIdTableSVlanUid": juniQosSVlanIdTableSVlanUid,
       "juniQosSVlanIdTablePortUid": juniQosSVlanIdTablePortUid,
       "juniQosSVlanIdTableSVlanId": juniQosSVlanIdTableSVlanId,
       "juniQosConformance": juniQosConformance,
       "juniQosCompliances": juniQosCompliances,
       "juniQosCompliance": juniQosCompliance,
       "juniQosCompliance2": juniQosCompliance2,
       "juniQosCompliance3": juniQosCompliance3,
       "juniQosCompliance4": juniQosCompliance4,
       "juniQosCompliance5": juniQosCompliance5,
       "juniQosCompliance6": juniQosCompliance6,
       "juniQosGroups": juniQosGroups,
       "juniQosCapabilityGroup": juniQosCapabilityGroup,
       "juniQosScalarGroup": juniQosScalarGroup,
       "juniQosTrafficClassListGroup": juniQosTrafficClassListGroup,
       "juniQosTrafficClassGroupListGroup": juniQosTrafficClassGroupListGroup,
       "juniQosQueueProfileListGroup": juniQosQueueProfileListGroup,
       "juniQosSchedulerProfileListGroup": juniQosSchedulerProfileListGroup,
       "juniQosProfileListGroup": juniQosProfileListGroup,
       "juniQosProfileElementGroup": juniQosProfileElementGroup,
       "juniQosIfAttachGroup": juniQosIfAttachGroup,
       "juniQosQosPortTypeProfileGroup": juniQosQosPortTypeProfileGroup,
       "juniQosQueueStatisticsGroup": juniQosQueueStatisticsGroup,
       "juniQosScalarGroup2": juniQosScalarGroup2,
       "juniQosProfileElementGroup2": juniQosProfileElementGroup2,
       "juniQosDropProfileListGroup": juniQosDropProfileListGroup,
       "juniQosAtmVpUidSupportGroup": juniQosAtmVpUidSupportGroup,
       "juniQosScalarGroup3": juniQosScalarGroup3,
       "juniQosProfileElementGroup3": juniQosProfileElementGroup3,
       "juniQosStatisticsProfileListGroup": juniQosStatisticsProfileListGroup,
       "juniQosSchedulerProfileListGroup2": juniQosSchedulerProfileListGroup2,
       "juniQosQosModePortGroup": juniQosQosModePortGroup,
       "juniQosQosShapingModeGroup": juniQosQosShapingModeGroup,
       "juniQosTrafficClassGroupListGroup2": juniQosTrafficClassGroupListGroup2,
       "juniQosSchedulerProfileListGroup3": juniQosSchedulerProfileListGroup3,
       "juniQosSchedulerProfileListGroup4": juniQosSchedulerProfileListGroup4,
       "juniQosSVlanUidSupportGroup": juniQosSVlanUidSupportGroup,
       "juniQosSVlanIdSupportGroup": juniQosSVlanIdSupportGroup}
)

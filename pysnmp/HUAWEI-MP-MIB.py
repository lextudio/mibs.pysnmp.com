# SNMP MIB module (HUAWEI-MP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:04 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwMultilinkPPP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMpObjects_ObjectIdentity = ObjectIdentity
hwMpObjects = _HwMpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1)
)
_HwMpMultilinkTable_Object = MibTable
hwMpMultilinkTable = _HwMpMultilinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1)
)
if mibBuilder.loadTexts:
    hwMpMultilinkTable.setStatus("current")
_HwMpMultilinkEntry_Object = MibTableRow
hwMpMultilinkEntry = _HwMpMultilinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1)
)
hwMpMultilinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwMpMultilinkEntry.setStatus("current")
_HwMpMultilinkDescr_Type = DisplayString
_HwMpMultilinkDescr_Object = MibTableColumn
hwMpMultilinkDescr = _HwMpMultilinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 1),
    _HwMpMultilinkDescr_Type()
)
hwMpMultilinkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpMultilinkDescr.setStatus("current")
_HwMpBundleName_Type = DisplayString
_HwMpBundleName_Object = MibTableColumn
hwMpBundleName = _HwMpBundleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 2),
    _HwMpBundleName_Type()
)
hwMpBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpBundleName.setStatus("current")
_HwMpBundledSlot_Type = Integer32
_HwMpBundledSlot_Object = MibTableColumn
hwMpBundledSlot = _HwMpBundledSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 3),
    _HwMpBundledSlot_Type()
)
hwMpBundledSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpBundledSlot.setStatus("current")
_HwMpBundledMemberCnt_Type = Integer32
_HwMpBundledMemberCnt_Object = MibTableColumn
hwMpBundledMemberCnt = _HwMpBundledMemberCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 4),
    _HwMpBundledMemberCnt_Type()
)
hwMpBundledMemberCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpBundledMemberCnt.setStatus("current")
_HwMpLostFragments_Type = Counter32
_HwMpLostFragments_Object = MibTableColumn
hwMpLostFragments = _HwMpLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 5),
    _HwMpLostFragments_Type()
)
hwMpLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpLostFragments.setStatus("current")
_HwMpReorderedPkts_Type = Counter32
_HwMpReorderedPkts_Object = MibTableColumn
hwMpReorderedPkts = _HwMpReorderedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 6),
    _HwMpReorderedPkts_Type()
)
hwMpReorderedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpReorderedPkts.setStatus("current")
_HwMpUnassignedPkts_Type = Counter32
_HwMpUnassignedPkts_Object = MibTableColumn
hwMpUnassignedPkts = _HwMpUnassignedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 7),
    _HwMpUnassignedPkts_Type()
)
hwMpUnassignedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpUnassignedPkts.setStatus("current")
_HwMpInterleavedPkts_Type = Counter32
_HwMpInterleavedPkts_Object = MibTableColumn
hwMpInterleavedPkts = _HwMpInterleavedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 8),
    _HwMpInterleavedPkts_Type()
)
hwMpInterleavedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpInterleavedPkts.setStatus("current")
_HwMpRcvdSequence_Type = Integer32
_HwMpRcvdSequence_Object = MibTableColumn
hwMpRcvdSequence = _HwMpRcvdSequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 9),
    _HwMpRcvdSequence_Type()
)
hwMpRcvdSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpRcvdSequence.setStatus("current")
_HwMpSentSequence_Type = Integer32
_HwMpSentSequence_Object = MibTableColumn
hwMpSentSequence = _HwMpSentSequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 10),
    _HwMpSentSequence_Type()
)
hwMpSentSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpSentSequence.setStatus("current")


class _HwMpDetectTime_Type(Integer32):
    """Custom type hwMpDetectTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 3600),
    )


_HwMpDetectTime_Type.__name__ = "Integer32"
_HwMpDetectTime_Object = MibTableColumn
hwMpDetectTime = _HwMpDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 11),
    _HwMpDetectTime_Type()
)
hwMpDetectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMpDetectTime.setStatus("current")


class _HwMpFlappingCnt_Type(Integer32):
    """Custom type hwMpFlappingCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HwMpFlappingCnt_Type.__name__ = "Integer32"
_HwMpFlappingCnt_Object = MibTableColumn
hwMpFlappingCnt = _HwMpFlappingCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 12),
    _HwMpFlappingCnt_Type()
)
hwMpFlappingCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMpFlappingCnt.setStatus("current")


class _HwMpDampingTime_Type(Integer32):
    """Custom type hwMpDampingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 86400),
    )


_HwMpDampingTime_Type.__name__ = "Integer32"
_HwMpDampingTime_Object = MibTableColumn
hwMpDampingTime = _HwMpDampingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 13),
    _HwMpDampingTime_Type()
)
hwMpDampingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMpDampingTime.setStatus("current")


class _HwMpBundleThreshold_Type(Integer32):
    """Custom type hwMpBundleThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwMpBundleThreshold_Type.__name__ = "Integer32"
_HwMpBundleThreshold_Object = MibTableColumn
hwMpBundleThreshold = _HwMpBundleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 14),
    _HwMpBundleThreshold_Type()
)
hwMpBundleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMpBundleThreshold.setStatus("current")


class _HwMpSequenceReorder_Type(Integer32):
    """Custom type hwMpSequenceReorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwMpSequenceReorder_Type.__name__ = "Integer32"
_HwMpSequenceReorder_Object = MibTableColumn
hwMpSequenceReorder = _HwMpSequenceReorder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 1, 1, 15),
    _HwMpSequenceReorder_Type()
)
hwMpSequenceReorder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMpSequenceReorder.setStatus("current")
_HwMpMemberlinkTable_Object = MibTable
hwMpMemberlinkTable = _HwMpMemberlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 2)
)
if mibBuilder.loadTexts:
    hwMpMemberlinkTable.setStatus("current")
_HwMpMemberlinkEntry_Object = MibTableRow
hwMpMemberlinkEntry = _HwMpMemberlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 2, 1)
)
hwMpMemberlinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-MP-MIB", "hwMpMemberlinkSeqNumber"),
)
if mibBuilder.loadTexts:
    hwMpMemberlinkEntry.setStatus("current")
_HwMpMemberlinkSeqNumber_Type = Integer32
_HwMpMemberlinkSeqNumber_Object = MibTableColumn
hwMpMemberlinkSeqNumber = _HwMpMemberlinkSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 2, 1, 1),
    _HwMpMemberlinkSeqNumber_Type()
)
hwMpMemberlinkSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpMemberlinkSeqNumber.setStatus("current")
_HwMpMemberlinkIfIndex_Type = Integer32
_HwMpMemberlinkIfIndex_Object = MibTableColumn
hwMpMemberlinkIfIndex = _HwMpMemberlinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 2, 1, 2),
    _HwMpMemberlinkIfIndex_Type()
)
hwMpMemberlinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpMemberlinkIfIndex.setStatus("current")
_HwMpMemberlinkDescr_Type = DisplayString
_HwMpMemberlinkDescr_Object = MibTableColumn
hwMpMemberlinkDescr = _HwMpMemberlinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 2, 1, 3),
    _HwMpMemberlinkDescr_Type()
)
hwMpMemberlinkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpMemberlinkDescr.setStatus("current")
_HwMpMemberlinkMpStatus_Type = Integer32
_HwMpMemberlinkMpStatus_Object = MibTableColumn
hwMpMemberlinkMpStatus = _HwMpMemberlinkMpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 1, 2, 1, 4),
    _HwMpMemberlinkMpStatus_Type()
)
hwMpMemberlinkMpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMpMemberlinkMpStatus.setStatus("current")
_HwMpNotifications_ObjectIdentity = ObjectIdentity
hwMpNotifications = _HwMpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 2)
)
_HwMpTraps_ObjectIdentity = ObjectIdentity
hwMpTraps = _HwMpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 2, 1)
)
_HwMpConformance_ObjectIdentity = ObjectIdentity
hwMpConformance = _HwMpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 3)
)
_HwMpCompliances_ObjectIdentity = ObjectIdentity
hwMpCompliances = _HwMpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 3, 1)
)
_HwMpGroups_ObjectIdentity = ObjectIdentity
hwMpGroups = _HwMpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 3, 2)
)

# Managed Objects groups

hwMpMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 3, 2, 1)
)
hwMpMandatoryGroup.setObjects(
      *(("HUAWEI-MP-MIB", "hwMpBundledMemberCnt"),
        ("HUAWEI-MP-MIB", "hwMpMemberlinkSeqNumber"),
        ("HUAWEI-MP-MIB", "hwMpMemberlinkIfIndex"))
)
if mibBuilder.loadTexts:
    hwMpMandatoryGroup.setStatus("current")

hwMpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 3, 2, 2)
)
hwMpInfoGroup.setObjects(
      *(("HUAWEI-MP-MIB", "hwMpMultilinkDescr"),
        ("HUAWEI-MP-MIB", "hwMpBundleName"),
        ("HUAWEI-MP-MIB", "hwMpBundledSlot"),
        ("HUAWEI-MP-MIB", "hwMpBundledMemberCnt"),
        ("HUAWEI-MP-MIB", "hwMpLostFragments"),
        ("HUAWEI-MP-MIB", "hwMpReorderedPkts"),
        ("HUAWEI-MP-MIB", "hwMpUnassignedPkts"),
        ("HUAWEI-MP-MIB", "hwMpInterleavedPkts"),
        ("HUAWEI-MP-MIB", "hwMpRcvdSequence"),
        ("HUAWEI-MP-MIB", "hwMpSentSequence"),
        ("HUAWEI-MP-MIB", "hwMpDetectTime"),
        ("HUAWEI-MP-MIB", "hwMpFlappingCnt"),
        ("HUAWEI-MP-MIB", "hwMpDampingTime"),
        ("HUAWEI-MP-MIB", "hwMpBundleThreshold"),
        ("HUAWEI-MP-MIB", "hwMpSequenceReorder"),
        ("HUAWEI-MP-MIB", "hwMpMemberlinkDescr"),
        ("HUAWEI-MP-MIB", "hwMpMemberlinkMpStatus"))
)
if mibBuilder.loadTexts:
    hwMpInfoGroup.setStatus("current")


# Notification objects

hwMpSonChannelDampingDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 2, 1, 1)
)
hwMpSonChannelDampingDetect.setObjects(
    ("HUAWEI-MP-MIB", "hwMpMemberlinkIfIndex")
)
if mibBuilder.loadTexts:
    hwMpSonChannelDampingDetect.setStatus(
        "current"
    )

hwMpSonChannelDampingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 2, 1, 2)
)
hwMpSonChannelDampingResume.setObjects(
    ("HUAWEI-MP-MIB", "hwMpMemberlinkIfIndex")
)
if mibBuilder.loadTexts:
    hwMpSonChannelDampingResume.setStatus(
        "current"
    )

hwMpThresholdControlDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 2, 1, 3)
)
hwMpThresholdControlDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMpThresholdControlDetect.setStatus(
        "current"
    )

hwMpThresholdControlDetectClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 2, 1, 4)
)
hwMpThresholdControlDetectClear.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMpThresholdControlDetectClear.setStatus(
        "current"
    )


# Notifications groups

hwMpTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 3, 2, 3)
)
hwMpTrapGroup.setObjects(
      *(("HUAWEI-MP-MIB", "hwMpSonChannelDampingDetect"),
        ("HUAWEI-MP-MIB", "hwMpSonChannelDampingResume"),
        ("HUAWEI-MP-MIB", "hwMpThresholdControlDetect"),
        ("HUAWEI-MP-MIB", "hwMpThresholdControlDetectClear"))
)
if mibBuilder.loadTexts:
    hwMpTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 33, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwMpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MP-MIB",
    **{"hwMultilinkPPP": hwMultilinkPPP,
       "hwMpObjects": hwMpObjects,
       "hwMpMultilinkTable": hwMpMultilinkTable,
       "hwMpMultilinkEntry": hwMpMultilinkEntry,
       "hwMpMultilinkDescr": hwMpMultilinkDescr,
       "hwMpBundleName": hwMpBundleName,
       "hwMpBundledSlot": hwMpBundledSlot,
       "hwMpBundledMemberCnt": hwMpBundledMemberCnt,
       "hwMpLostFragments": hwMpLostFragments,
       "hwMpReorderedPkts": hwMpReorderedPkts,
       "hwMpUnassignedPkts": hwMpUnassignedPkts,
       "hwMpInterleavedPkts": hwMpInterleavedPkts,
       "hwMpRcvdSequence": hwMpRcvdSequence,
       "hwMpSentSequence": hwMpSentSequence,
       "hwMpDetectTime": hwMpDetectTime,
       "hwMpFlappingCnt": hwMpFlappingCnt,
       "hwMpDampingTime": hwMpDampingTime,
       "hwMpBundleThreshold": hwMpBundleThreshold,
       "hwMpSequenceReorder": hwMpSequenceReorder,
       "hwMpMemberlinkTable": hwMpMemberlinkTable,
       "hwMpMemberlinkEntry": hwMpMemberlinkEntry,
       "hwMpMemberlinkSeqNumber": hwMpMemberlinkSeqNumber,
       "hwMpMemberlinkIfIndex": hwMpMemberlinkIfIndex,
       "hwMpMemberlinkDescr": hwMpMemberlinkDescr,
       "hwMpMemberlinkMpStatus": hwMpMemberlinkMpStatus,
       "hwMpNotifications": hwMpNotifications,
       "hwMpTraps": hwMpTraps,
       "hwMpSonChannelDampingDetect": hwMpSonChannelDampingDetect,
       "hwMpSonChannelDampingResume": hwMpSonChannelDampingResume,
       "hwMpThresholdControlDetect": hwMpThresholdControlDetect,
       "hwMpThresholdControlDetectClear": hwMpThresholdControlDetectClear,
       "hwMpConformance": hwMpConformance,
       "hwMpCompliances": hwMpCompliances,
       "hwMpCompliance": hwMpCompliance,
       "hwMpGroups": hwMpGroups,
       "hwMpMandatoryGroup": hwMpMandatoryGroup,
       "hwMpInfoGroup": hwMpInfoGroup,
       "hwMpTrapGroup": hwMpTrapGroup}
)

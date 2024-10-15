# SNMP MIB module (Juniper-DOS-PROTECTION-PLATFORM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-DOS-PROTECTION-PLATFORM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:02 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(JuniDosProtectionPriorityType,
 JuniDosProtectionProtocolState,
 JuniDosProtectionProtocolType,
 JuniDosProtectionScfdsTableOverflowState) = mibBuilder.importSymbols(
    "Juniper-DOS-PROTECTION-MIB",
    "JuniDosProtectionPriorityType",
    "JuniDosProtectionProtocolState",
    "JuniDosProtectionProtocolType",
    "JuniDosProtectionScfdsTableOverflowState")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniDosProtectionPlatformMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81)
)
juniDosProtectionPlatformMIB.setRevisions(
        ("2006-07-01 00:00",
         "2006-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniDosProtectionPlatformTraps_ObjectIdentity = ObjectIdentity
juniDosProtectionPlatformTraps = _JuniDosProtectionPlatformTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0)
)
_JuniDosProtectionPlatformScfdsTraps_ObjectIdentity = ObjectIdentity
juniDosProtectionPlatformScfdsTraps = _JuniDosProtectionPlatformScfdsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0)
)
_JuniDosProtectionPlatformObjects_ObjectIdentity = ObjectIdentity
juniDosProtectionPlatformObjects = _JuniDosProtectionPlatformObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1)
)
_JuniDosProtectionPlatformScfdsGroup_ObjectIdentity = ObjectIdentity
juniDosProtectionPlatformScfdsGroup = _JuniDosProtectionPlatformScfdsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1)
)
_JuniDosProtectionScfdsSlotProtocolTable_Object = MibTable
juniDosProtectionScfdsSlotProtocolTable = _JuniDosProtectionScfdsSlotProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotProtocolTable.setStatus("current")
_JuniDosProtectionScfdsSlotProtocolEntry_Object = MibTableRow
juniDosProtectionScfdsSlotProtocolEntry = _JuniDosProtectionScfdsSlotProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 1, 1)
)
juniDosProtectionScfdsSlotProtocolEntry.setIndexNames(
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotProtocolSlot"),
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotProtocolIndex"),
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotProtocolEntry.setStatus("current")
_JuniDosProtectionScfdsSlotProtocolSlot_Type = Unsigned32
_JuniDosProtectionScfdsSlotProtocolSlot_Object = MibTableColumn
juniDosProtectionScfdsSlotProtocolSlot = _JuniDosProtectionScfdsSlotProtocolSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 1, 1, 1),
    _JuniDosProtectionScfdsSlotProtocolSlot_Type()
)
juniDosProtectionScfdsSlotProtocolSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotProtocolSlot.setStatus("current")
_JuniDosProtectionScfdsSlotProtocolIndex_Type = JuniDosProtectionProtocolType
_JuniDosProtectionScfdsSlotProtocolIndex_Object = MibTableColumn
juniDosProtectionScfdsSlotProtocolIndex = _JuniDosProtectionScfdsSlotProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 1, 1, 2),
    _JuniDosProtectionScfdsSlotProtocolIndex_Type()
)
juniDosProtectionScfdsSlotProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotProtocolIndex.setStatus("current")
_JuniDosProtectionScfdsSlotProtocolState_Type = JuniDosProtectionProtocolState
_JuniDosProtectionScfdsSlotProtocolState_Object = MibTableColumn
juniDosProtectionScfdsSlotProtocolState = _JuniDosProtectionScfdsSlotProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 1, 1, 3),
    _JuniDosProtectionScfdsSlotProtocolState_Type()
)
juniDosProtectionScfdsSlotProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotProtocolState.setStatus("current")
_JuniDosProtectionScfdsSlotProtocolTransitions_Type = Counter32
_JuniDosProtectionScfdsSlotProtocolTransitions_Object = MibTableColumn
juniDosProtectionScfdsSlotProtocolTransitions = _JuniDosProtectionScfdsSlotProtocolTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 1, 1, 4),
    _JuniDosProtectionScfdsSlotProtocolTransitions_Type()
)
juniDosProtectionScfdsSlotProtocolTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotProtocolTransitions.setStatus("current")
_JuniDosProtectionScfdsSlotFlowTable_Object = MibTable
juniDosProtectionScfdsSlotFlowTable = _JuniDosProtectionScfdsSlotFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowTable.setStatus("obsolete")
_JuniDosProtectionScfdsSlotFlowEntry_Object = MibTableRow
juniDosProtectionScfdsSlotFlowEntry = _JuniDosProtectionScfdsSlotFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2, 1)
)
juniDosProtectionScfdsSlotFlowEntry.setIndexNames(
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowSlot"),
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowIfIndex"),
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowGroupId"),
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowProtocol"),
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowEntry.setStatus("obsolete")
_JuniDosProtectionScfdsSlotFlowSlot_Type = Unsigned32
_JuniDosProtectionScfdsSlotFlowSlot_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowSlot = _JuniDosProtectionScfdsSlotFlowSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2, 1, 1),
    _JuniDosProtectionScfdsSlotFlowSlot_Type()
)
juniDosProtectionScfdsSlotFlowSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowSlot.setStatus("obsolete")
_JuniDosProtectionScfdsSlotFlowIfIndex_Type = InterfaceIndex
_JuniDosProtectionScfdsSlotFlowIfIndex_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowIfIndex = _JuniDosProtectionScfdsSlotFlowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2, 1, 2),
    _JuniDosProtectionScfdsSlotFlowIfIndex_Type()
)
juniDosProtectionScfdsSlotFlowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowIfIndex.setStatus("obsolete")


class _JuniDosProtectionScfdsSlotFlowGroupId_Type(Unsigned32):
    """Custom type juniDosProtectionScfdsSlotFlowGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_JuniDosProtectionScfdsSlotFlowGroupId_Type.__name__ = "Unsigned32"
_JuniDosProtectionScfdsSlotFlowGroupId_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowGroupId = _JuniDosProtectionScfdsSlotFlowGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2, 1, 3),
    _JuniDosProtectionScfdsSlotFlowGroupId_Type()
)
juniDosProtectionScfdsSlotFlowGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowGroupId.setStatus("obsolete")
_JuniDosProtectionScfdsSlotFlowProtocol_Type = JuniDosProtectionProtocolType
_JuniDosProtectionScfdsSlotFlowProtocol_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowProtocol = _JuniDosProtectionScfdsSlotFlowProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2, 1, 4),
    _JuniDosProtectionScfdsSlotFlowProtocol_Type()
)
juniDosProtectionScfdsSlotFlowProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowProtocol.setStatus("obsolete")
_JuniDosProtectionScfdsSlotFlowRate_Type = Unsigned32
_JuniDosProtectionScfdsSlotFlowRate_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowRate = _JuniDosProtectionScfdsSlotFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2, 1, 5),
    _JuniDosProtectionScfdsSlotFlowRate_Type()
)
juniDosProtectionScfdsSlotFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowRate.setStatus("obsolete")
_JuniDosProtectionScfdsSlotFlowPeakRate_Type = Unsigned32
_JuniDosProtectionScfdsSlotFlowPeakRate_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowPeakRate = _JuniDosProtectionScfdsSlotFlowPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2, 1, 6),
    _JuniDosProtectionScfdsSlotFlowPeakRate_Type()
)
juniDosProtectionScfdsSlotFlowPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowPeakRate.setStatus("obsolete")
_JuniDosProtectionScfdsSlotFlowTimeFlagged_Type = Unsigned32
_JuniDosProtectionScfdsSlotFlowTimeFlagged_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowTimeFlagged = _JuniDosProtectionScfdsSlotFlowTimeFlagged_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2, 1, 7),
    _JuniDosProtectionScfdsSlotFlowTimeFlagged_Type()
)
juniDosProtectionScfdsSlotFlowTimeFlagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowTimeFlagged.setStatus("obsolete")
_JuniDosProtectionScfdsSlotFlowIngressSlot_Type = Integer32
_JuniDosProtectionScfdsSlotFlowIngressSlot_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowIngressSlot = _JuniDosProtectionScfdsSlotFlowIngressSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2, 1, 8),
    _JuniDosProtectionScfdsSlotFlowIngressSlot_Type()
)
juniDosProtectionScfdsSlotFlowIngressSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowIngressSlot.setStatus("obsolete")
_JuniDosProtectionScfdsSlotFlowGroup_Type = TruthValue
_JuniDosProtectionScfdsSlotFlowGroup_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowGroup = _JuniDosProtectionScfdsSlotFlowGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2, 1, 9),
    _JuniDosProtectionScfdsSlotFlowGroup_Type()
)
juniDosProtectionScfdsSlotFlowGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowGroup.setStatus("obsolete")


class _JuniDosProtectionScfdsSlotFlowClearEntry_Type(Integer32):
    """Custom type juniDosProtectionScfdsSlotFlowClearEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 0))
    )


_JuniDosProtectionScfdsSlotFlowClearEntry_Type.__name__ = "Integer32"
_JuniDosProtectionScfdsSlotFlowClearEntry_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowClearEntry = _JuniDosProtectionScfdsSlotFlowClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 2, 1, 10),
    _JuniDosProtectionScfdsSlotFlowClearEntry_Type()
)
juniDosProtectionScfdsSlotFlowClearEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowClearEntry.setStatus("obsolete")
_JuniDosProtectionScfdsSlotTable_Object = MibTable
juniDosProtectionScfdsSlotTable = _JuniDosProtectionScfdsSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotTable.setStatus("current")
_JuniDosProtectionScfdsSlotEntry_Object = MibTableRow
juniDosProtectionScfdsSlotEntry = _JuniDosProtectionScfdsSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1)
)
juniDosProtectionScfdsSlotEntry.setIndexNames(
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowSlot"),
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotEntry.setStatus("current")
_JuniDosProtectionScfdsSlotSlot_Type = Unsigned32
_JuniDosProtectionScfdsSlotSlot_Object = MibTableColumn
juniDosProtectionScfdsSlotSlot = _JuniDosProtectionScfdsSlotSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1, 1),
    _JuniDosProtectionScfdsSlotSlot_Type()
)
juniDosProtectionScfdsSlotSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotSlot.setStatus("current")


class _JuniDosProtectionScfdsSlotClearAll_Type(Integer32):
    """Custom type juniDosProtectionScfdsSlotClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 0))
    )


_JuniDosProtectionScfdsSlotClearAll_Type.__name__ = "Integer32"
_JuniDosProtectionScfdsSlotClearAll_Object = MibTableColumn
juniDosProtectionScfdsSlotClearAll = _JuniDosProtectionScfdsSlotClearAll_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1, 2),
    _JuniDosProtectionScfdsSlotClearAll_Type()
)
juniDosProtectionScfdsSlotClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotClearAll.setStatus("current")
_JuniDosProtectionScfdsSlotDiscontinuityTime_Type = Unsigned32
_JuniDosProtectionScfdsSlotDiscontinuityTime_Object = MibTableColumn
juniDosProtectionScfdsSlotDiscontinuityTime = _JuniDosProtectionScfdsSlotDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1, 3),
    _JuniDosProtectionScfdsSlotDiscontinuityTime_Type()
)
juniDosProtectionScfdsSlotDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotDiscontinuityTime.setStatus("current")
_JuniDosProtectionScfdsSlotTableOverflowState_Type = JuniDosProtectionScfdsTableOverflowState
_JuniDosProtectionScfdsSlotTableOverflowState_Object = MibTableColumn
juniDosProtectionScfdsSlotTableOverflowState = _JuniDosProtectionScfdsSlotTableOverflowState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1, 4),
    _JuniDosProtectionScfdsSlotTableOverflowState_Type()
)
juniDosProtectionScfdsSlotTableOverflowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotTableOverflowState.setStatus("current")
_JuniDosProtectionScfdsSlotCurrentSuspiciousFlows_Type = Counter32
_JuniDosProtectionScfdsSlotCurrentSuspiciousFlows_Object = MibTableColumn
juniDosProtectionScfdsSlotCurrentSuspiciousFlows = _JuniDosProtectionScfdsSlotCurrentSuspiciousFlows_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1, 5),
    _JuniDosProtectionScfdsSlotCurrentSuspiciousFlows_Type()
)
juniDosProtectionScfdsSlotCurrentSuspiciousFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotCurrentSuspiciousFlows.setStatus("current")
_JuniDosProtectionScfdsSlotNumberSuspiciousFlows_Type = Counter32
_JuniDosProtectionScfdsSlotNumberSuspiciousFlows_Object = MibTableColumn
juniDosProtectionScfdsSlotNumberSuspiciousFlows = _JuniDosProtectionScfdsSlotNumberSuspiciousFlows_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1, 6),
    _JuniDosProtectionScfdsSlotNumberSuspiciousFlows_Type()
)
juniDosProtectionScfdsSlotNumberSuspiciousFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotNumberSuspiciousFlows.setStatus("current")
_JuniDosProtectionScfdsSlotNumberSuspiciousFlowGroups_Type = Counter32
_JuniDosProtectionScfdsSlotNumberSuspiciousFlowGroups_Object = MibTableColumn
juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups = _JuniDosProtectionScfdsSlotNumberSuspiciousFlowGroups_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1, 7),
    _JuniDosProtectionScfdsSlotNumberSuspiciousFlowGroups_Type()
)
juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups.setStatus("current")
_JuniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups_Type = Counter32
_JuniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups_Object = MibTableColumn
juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups = _JuniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1, 8),
    _JuniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups_Type()
)
juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups.setStatus("current")
_JuniDosProtectionScfdsSlotCurrentFalseNegativeFlows_Type = Counter32
_JuniDosProtectionScfdsSlotCurrentFalseNegativeFlows_Object = MibTableColumn
juniDosProtectionScfdsSlotCurrentFalseNegativeFlows = _JuniDosProtectionScfdsSlotCurrentFalseNegativeFlows_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1, 9),
    _JuniDosProtectionScfdsSlotCurrentFalseNegativeFlows_Type()
)
juniDosProtectionScfdsSlotCurrentFalseNegativeFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotCurrentFalseNegativeFlows.setStatus("current")
_JuniDosProtectionScfdsSlotNumberFalseNegativeFlows_Type = Counter32
_JuniDosProtectionScfdsSlotNumberFalseNegativeFlows_Object = MibTableColumn
juniDosProtectionScfdsSlotNumberFalseNegativeFlows = _JuniDosProtectionScfdsSlotNumberFalseNegativeFlows_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1, 10),
    _JuniDosProtectionScfdsSlotNumberFalseNegativeFlows_Type()
)
juniDosProtectionScfdsSlotNumberFalseNegativeFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotNumberFalseNegativeFlows.setStatus("current")
_JuniDosProtectionScfdsSlotOverflows_Type = Counter32
_JuniDosProtectionScfdsSlotOverflows_Object = MibTableColumn
juniDosProtectionScfdsSlotOverflows = _JuniDosProtectionScfdsSlotOverflows_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 3, 1, 11),
    _JuniDosProtectionScfdsSlotOverflows_Type()
)
juniDosProtectionScfdsSlotOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotOverflows.setStatus("current")
_JuniDosProtectionScfdsSlotFlowMacTable_Object = MibTable
juniDosProtectionScfdsSlotFlowMacTable = _JuniDosProtectionScfdsSlotFlowMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacTable.setStatus("current")
_JuniDosProtectionScfdsSlotFlowMacEntry_Object = MibTableRow
juniDosProtectionScfdsSlotFlowMacEntry = _JuniDosProtectionScfdsSlotFlowMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1)
)
juniDosProtectionScfdsSlotFlowMacEntry.setIndexNames(
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowMacSlot"),
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowMacIfIndex"),
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowMacGroupId"),
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowMacProtocol"),
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowMacSrcMac"),
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacEntry.setStatus("current")
_JuniDosProtectionScfdsSlotFlowMacSlot_Type = Unsigned32
_JuniDosProtectionScfdsSlotFlowMacSlot_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowMacSlot = _JuniDosProtectionScfdsSlotFlowMacSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1, 1),
    _JuniDosProtectionScfdsSlotFlowMacSlot_Type()
)
juniDosProtectionScfdsSlotFlowMacSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacSlot.setStatus("current")
_JuniDosProtectionScfdsSlotFlowMacIfIndex_Type = InterfaceIndex
_JuniDosProtectionScfdsSlotFlowMacIfIndex_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowMacIfIndex = _JuniDosProtectionScfdsSlotFlowMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1, 2),
    _JuniDosProtectionScfdsSlotFlowMacIfIndex_Type()
)
juniDosProtectionScfdsSlotFlowMacIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacIfIndex.setStatus("current")


class _JuniDosProtectionScfdsSlotFlowMacGroupId_Type(Unsigned32):
    """Custom type juniDosProtectionScfdsSlotFlowMacGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_JuniDosProtectionScfdsSlotFlowMacGroupId_Type.__name__ = "Unsigned32"
_JuniDosProtectionScfdsSlotFlowMacGroupId_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowMacGroupId = _JuniDosProtectionScfdsSlotFlowMacGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1, 3),
    _JuniDosProtectionScfdsSlotFlowMacGroupId_Type()
)
juniDosProtectionScfdsSlotFlowMacGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacGroupId.setStatus("current")
_JuniDosProtectionScfdsSlotFlowMacProtocol_Type = JuniDosProtectionProtocolType
_JuniDosProtectionScfdsSlotFlowMacProtocol_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowMacProtocol = _JuniDosProtectionScfdsSlotFlowMacProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1, 4),
    _JuniDosProtectionScfdsSlotFlowMacProtocol_Type()
)
juniDosProtectionScfdsSlotFlowMacProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacProtocol.setStatus("current")
_JuniDosProtectionScfdsSlotFlowMacSrcMac_Type = MacAddress
_JuniDosProtectionScfdsSlotFlowMacSrcMac_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowMacSrcMac = _JuniDosProtectionScfdsSlotFlowMacSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1, 5),
    _JuniDosProtectionScfdsSlotFlowMacSrcMac_Type()
)
juniDosProtectionScfdsSlotFlowMacSrcMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacSrcMac.setStatus("current")
_JuniDosProtectionScfdsSlotFlowMacRate_Type = Unsigned32
_JuniDosProtectionScfdsSlotFlowMacRate_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowMacRate = _JuniDosProtectionScfdsSlotFlowMacRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1, 6),
    _JuniDosProtectionScfdsSlotFlowMacRate_Type()
)
juniDosProtectionScfdsSlotFlowMacRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacRate.setStatus("current")
_JuniDosProtectionScfdsSlotFlowMacPeakRate_Type = Unsigned32
_JuniDosProtectionScfdsSlotFlowMacPeakRate_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowMacPeakRate = _JuniDosProtectionScfdsSlotFlowMacPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1, 7),
    _JuniDosProtectionScfdsSlotFlowMacPeakRate_Type()
)
juniDosProtectionScfdsSlotFlowMacPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacPeakRate.setStatus("current")
_JuniDosProtectionScfdsSlotFlowMacTimeFlagged_Type = Unsigned32
_JuniDosProtectionScfdsSlotFlowMacTimeFlagged_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowMacTimeFlagged = _JuniDosProtectionScfdsSlotFlowMacTimeFlagged_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1, 8),
    _JuniDosProtectionScfdsSlotFlowMacTimeFlagged_Type()
)
juniDosProtectionScfdsSlotFlowMacTimeFlagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacTimeFlagged.setStatus("current")
_JuniDosProtectionScfdsSlotFlowMacIngressSlot_Type = Integer32
_JuniDosProtectionScfdsSlotFlowMacIngressSlot_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowMacIngressSlot = _JuniDosProtectionScfdsSlotFlowMacIngressSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1, 9),
    _JuniDosProtectionScfdsSlotFlowMacIngressSlot_Type()
)
juniDosProtectionScfdsSlotFlowMacIngressSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacIngressSlot.setStatus("current")
_JuniDosProtectionScfdsSlotFlowMacGroup_Type = TruthValue
_JuniDosProtectionScfdsSlotFlowMacGroup_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowMacGroup = _JuniDosProtectionScfdsSlotFlowMacGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1, 10),
    _JuniDosProtectionScfdsSlotFlowMacGroup_Type()
)
juniDosProtectionScfdsSlotFlowMacGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacGroup.setStatus("current")


class _JuniDosProtectionScfdsSlotFlowMacClearEntry_Type(Integer32):
    """Custom type juniDosProtectionScfdsSlotFlowMacClearEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 0))
    )


_JuniDosProtectionScfdsSlotFlowMacClearEntry_Type.__name__ = "Integer32"
_JuniDosProtectionScfdsSlotFlowMacClearEntry_Object = MibTableColumn
juniDosProtectionScfdsSlotFlowMacClearEntry = _JuniDosProtectionScfdsSlotFlowMacClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 1, 4, 1, 11),
    _JuniDosProtectionScfdsSlotFlowMacClearEntry_Type()
)
juniDosProtectionScfdsSlotFlowMacClearEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlotFlowMacClearEntry.setStatus("current")
_JuniDosProtectionPlatformDpgGroup_ObjectIdentity = ObjectIdentity
juniDosProtectionPlatformDpgGroup = _JuniDosProtectionPlatformDpgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 2)
)
_JuniDosProtectionDpgSlotRateTable_Object = MibTable
juniDosProtectionDpgSlotRateTable = _JuniDosProtectionDpgSlotRateTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgSlotRateTable.setStatus("current")
_JuniDosProtectionDpgSlotRateEntry_Object = MibTableRow
juniDosProtectionDpgSlotRateEntry = _JuniDosProtectionDpgSlotRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 2, 1, 1)
)
juniDosProtectionDpgSlotRateEntry.setIndexNames(
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionDpgSlotRateSlot"),
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionDpgSlotRateDpgName"),
    (0, "Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionDpgSlotRateProtocol"),
)
if mibBuilder.loadTexts:
    juniDosProtectionDpgSlotRateEntry.setStatus("current")
_JuniDosProtectionDpgSlotRateSlot_Type = Unsigned32
_JuniDosProtectionDpgSlotRateSlot_Object = MibTableColumn
juniDosProtectionDpgSlotRateSlot = _JuniDosProtectionDpgSlotRateSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 2, 1, 1, 1),
    _JuniDosProtectionDpgSlotRateSlot_Type()
)
juniDosProtectionDpgSlotRateSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionDpgSlotRateSlot.setStatus("current")


class _JuniDosProtectionDpgSlotRateDpgName_Type(DisplayString):
    """Custom type juniDosProtectionDpgSlotRateDpgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniDosProtectionDpgSlotRateDpgName_Type.__name__ = "DisplayString"
_JuniDosProtectionDpgSlotRateDpgName_Object = MibTableColumn
juniDosProtectionDpgSlotRateDpgName = _JuniDosProtectionDpgSlotRateDpgName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 2, 1, 1, 2),
    _JuniDosProtectionDpgSlotRateDpgName_Type()
)
juniDosProtectionDpgSlotRateDpgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionDpgSlotRateDpgName.setStatus("current")
_JuniDosProtectionDpgSlotRateProtocol_Type = JuniDosProtectionProtocolType
_JuniDosProtectionDpgSlotRateProtocol_Object = MibTableColumn
juniDosProtectionDpgSlotRateProtocol = _JuniDosProtectionDpgSlotRateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 2, 1, 1, 3),
    _JuniDosProtectionDpgSlotRateProtocol_Type()
)
juniDosProtectionDpgSlotRateProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDosProtectionDpgSlotRateProtocol.setStatus("current")
_JuniDosProtectionDpgSlotRateMinRate_Type = Unsigned32
_JuniDosProtectionDpgSlotRateMinRate_Object = MibTableColumn
juniDosProtectionDpgSlotRateMinRate = _JuniDosProtectionDpgSlotRateMinRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 2, 1, 1, 4),
    _JuniDosProtectionDpgSlotRateMinRate_Type()
)
juniDosProtectionDpgSlotRateMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionDpgSlotRateMinRate.setStatus("current")
_JuniDosProtectionDpgSlotRateMaxRate_Type = Unsigned32
_JuniDosProtectionDpgSlotRateMaxRate_Object = MibTableColumn
juniDosProtectionDpgSlotRateMaxRate = _JuniDosProtectionDpgSlotRateMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 2, 1, 1, 5),
    _JuniDosProtectionDpgSlotRateMaxRate_Type()
)
juniDosProtectionDpgSlotRateMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionDpgSlotRateMaxRate.setStatus("current")
_JuniDosProtectionDpgSlotRateMinBurst_Type = Unsigned32
_JuniDosProtectionDpgSlotRateMinBurst_Object = MibTableColumn
juniDosProtectionDpgSlotRateMinBurst = _JuniDosProtectionDpgSlotRateMinBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 2, 1, 1, 6),
    _JuniDosProtectionDpgSlotRateMinBurst_Type()
)
juniDosProtectionDpgSlotRateMinBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionDpgSlotRateMinBurst.setStatus("current")
_JuniDosProtectionDpgSlotRateMaxBurst_Type = Unsigned32
_JuniDosProtectionDpgSlotRateMaxBurst_Object = MibTableColumn
juniDosProtectionDpgSlotRateMaxBurst = _JuniDosProtectionDpgSlotRateMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 1, 2, 1, 1, 7),
    _JuniDosProtectionDpgSlotRateMaxBurst_Type()
)
juniDosProtectionDpgSlotRateMaxBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDosProtectionDpgSlotRateMaxBurst.setStatus("current")
_JuniDosProtectionPlatformTrapControl_ObjectIdentity = ObjectIdentity
juniDosProtectionPlatformTrapControl = _JuniDosProtectionPlatformTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 2)
)
_JuniDosProtectionScfdsSlot_Type = Unsigned32
_JuniDosProtectionScfdsSlot_Object = MibScalar
juniDosProtectionScfdsSlot = _JuniDosProtectionScfdsSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 2, 1),
    _JuniDosProtectionScfdsSlot_Type()
)
juniDosProtectionScfdsSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSlot.setStatus("current")
_JuniDosProtectionPriority_Type = JuniDosProtectionPriorityType
_JuniDosProtectionPriority_Object = MibScalar
juniDosProtectionPriority = _JuniDosProtectionPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 2, 2),
    _JuniDosProtectionPriority_Type()
)
juniDosProtectionPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDosProtectionPriority.setStatus("current")
_JuniDosProtectionProtocol_Type = JuniDosProtectionProtocolType
_JuniDosProtectionProtocol_Object = MibScalar
juniDosProtectionProtocol = _JuniDosProtectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 2, 3),
    _JuniDosProtectionProtocol_Type()
)
juniDosProtectionProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDosProtectionProtocol.setStatus("current")
_JuniDosProtectionIfIndex_Type = InterfaceIndex
_JuniDosProtectionIfIndex_Object = MibScalar
juniDosProtectionIfIndex = _JuniDosProtectionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 2, 4),
    _JuniDosProtectionIfIndex_Type()
)
juniDosProtectionIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDosProtectionIfIndex.setStatus("current")
_JuniDosProtectionGroupId_Type = Unsigned32
_JuniDosProtectionGroupId_Object = MibScalar
juniDosProtectionGroupId = _JuniDosProtectionGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 2, 5),
    _JuniDosProtectionGroupId_Type()
)
juniDosProtectionGroupId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDosProtectionGroupId.setStatus("current")


class _JuniDosProtectionSrcPhysAddr_Type(MacAddress):
    """Custom type juniDosProtectionSrcPhysAddr based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_JuniDosProtectionSrcPhysAddr_Type.__name__ = "MacAddress"
_JuniDosProtectionSrcPhysAddr_Object = MibScalar
juniDosProtectionSrcPhysAddr = _JuniDosProtectionSrcPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 2, 6),
    _JuniDosProtectionSrcPhysAddr_Type()
)
juniDosProtectionSrcPhysAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDosProtectionSrcPhysAddr.setStatus("current")
_JuniDosProtectionScfdsFlowRate_Type = Unsigned32
_JuniDosProtectionScfdsFlowRate_Object = MibScalar
juniDosProtectionScfdsFlowRate = _JuniDosProtectionScfdsFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 2, 7),
    _JuniDosProtectionScfdsFlowRate_Type()
)
juniDosProtectionScfdsFlowRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDosProtectionScfdsFlowRate.setStatus("current")
_JuniDosProtectionPlatformMIBConformance_ObjectIdentity = ObjectIdentity
juniDosProtectionPlatformMIBConformance = _JuniDosProtectionPlatformMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 4)
)
_JuniDosProtectionPlatformMIBCompliances_ObjectIdentity = ObjectIdentity
juniDosProtectionPlatformMIBCompliances = _JuniDosProtectionPlatformMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 4, 1)
)
_JuniDosProtectionPlatformMIBGroups_ObjectIdentity = ObjectIdentity
juniDosProtectionPlatformMIBGroups = _JuniDosProtectionPlatformMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 4, 2)
)

# Managed Objects groups

juniDosProtectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 4, 2, 1)
)
juniDosProtectionGroup.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotProtocolState"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotProtocolTransitions"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowRate"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowPeakRate"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowTimeFlagged"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowClearEntry"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowIngressSlot"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowGroup"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotDiscontinuityTime"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotTableOverflowState"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotCurrentSuspiciousFlows"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotNumberSuspiciousFlows"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotCurrentFalseNegativeFlows"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotNumberFalseNegativeFlows"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotOverflows"))
)
if mibBuilder.loadTexts:
    juniDosProtectionGroup.setStatus("current")

juniDosProtectionGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 4, 2, 3)
)
juniDosProtectionGroup1.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotProtocolState"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotProtocolTransitions"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowMacRate"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowMacPeakRate"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowMacTimeFlagged"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowMacClearEntry"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowMacIngressSlot"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotFlowMacGroup"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotDiscontinuityTime"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotTableOverflowState"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotCurrentSuspiciousFlows"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotNumberSuspiciousFlows"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotCurrentFalseNegativeFlows"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotNumberFalseNegativeFlows"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlotOverflows"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionDpgSlotRateMinRate"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionDpgSlotRateMaxRate"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionDpgSlotRateMinBurst"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionDpgSlotRateMaxBurst"))
)
if mibBuilder.loadTexts:
    juniDosProtectionGroup1.setStatus("current")


# Notification objects

juniDosProtectionScfdsSuspiciousControlFlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 1)
)
juniDosProtectionScfdsSuspiciousControlFlow.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionIfIndex"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionProtocol"))
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSuspiciousControlFlow.setStatus(
        "obsolete"
    )

juniDosProtectionScfdsNonSuspiciousControlFlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 2)
)
juniDosProtectionScfdsNonSuspiciousControlFlow.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionIfIndex"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionProtocol"))
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsNonSuspiciousControlFlow.setStatus(
        "obsolete"
    )

juniDosProtectionScfdsSuspiciousControlFlowGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 3)
)
juniDosProtectionScfdsSuspiciousControlFlowGroup.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlot"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionGroupId"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionProtocol"))
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSuspiciousControlFlowGroup.setStatus(
        "current"
    )

juniDosProtectionScfdsNonSuspiciousControlFlowGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 4)
)
juniDosProtectionScfdsNonSuspiciousControlFlowGroup.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlot"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionGroupId"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionProtocol"))
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsNonSuspiciousControlFlowGroup.setStatus(
        "current"
    )

juniDosProtectionScfdsTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 5)
)
juniDosProtectionScfdsTableFull.setObjects(
    ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlot")
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsTableFull.setStatus(
        "current"
    )

juniDosProtectionScfdsTableNotFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 6)
)
juniDosProtectionScfdsTableNotFull.setObjects(
    ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlot")
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsTableNotFull.setStatus(
        "current"
    )

juniDosProtectionScfdsGroupingInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 7)
)
juniDosProtectionScfdsGroupingInUse.setObjects(
    ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlot")
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsGroupingInUse.setStatus(
        "current"
    )

juniDosProtectionScfdsSuspiciousProtocol = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 8)
)
juniDosProtectionScfdsSuspiciousProtocol.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlot"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionProtocol"))
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSuspiciousProtocol.setStatus(
        "current"
    )

juniDosProtectionScfdsNonSuspiciousProtocol = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 9)
)
juniDosProtectionScfdsNonSuspiciousProtocol.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlot"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionProtocol"))
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsNonSuspiciousProtocol.setStatus(
        "current"
    )

juniDosProtectionScfdsSuspiciousPriority = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 10)
)
juniDosProtectionScfdsSuspiciousPriority.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlot"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionPriority"))
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSuspiciousPriority.setStatus(
        "current"
    )

juniDosProtectionScfdsNonSuspiciousPriority = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 11)
)
juniDosProtectionScfdsNonSuspiciousPriority.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSlot"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionPriority"))
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsNonSuspiciousPriority.setStatus(
        "current"
    )

juniDosProtectionScfdsSuspiciousControlFlowMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 12)
)
juniDosProtectionScfdsSuspiciousControlFlowMac.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionIfIndex"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionProtocol"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionSrcPhysAddr"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsFlowRate"))
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsSuspiciousControlFlowMac.setStatus(
        "current"
    )

juniDosProtectionScfdsNonSuspiciousControlFlowMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 0, 0, 13)
)
juniDosProtectionScfdsNonSuspiciousControlFlowMac.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionIfIndex"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionProtocol"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionSrcPhysAddr"))
)
if mibBuilder.loadTexts:
    juniDosProtectionScfdsNonSuspiciousControlFlowMac.setStatus(
        "obsolete"
    )


# Notifications groups

juniDosProtectionNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 4, 2, 2)
)
juniDosProtectionNotificationGroup.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSuspiciousControlFlow"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsNonSuspiciousControlFlow"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSuspiciousControlFlowGroup"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsNonSuspiciousControlFlowGroup"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsTableFull"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsTableNotFull"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsGroupingInUse"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSuspiciousProtocol"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsNonSuspiciousProtocol"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSuspiciousPriority"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsNonSuspiciousPriority"))
)
if mibBuilder.loadTexts:
    juniDosProtectionNotificationGroup.setStatus(
        "current"
    )

juniDosProtectionNotificationGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 4, 2, 4)
)
juniDosProtectionNotificationGroup1.setObjects(
      *(("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSuspiciousControlFlowMac"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsNonSuspiciousControlFlowMac"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSuspiciousControlFlowGroup"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsNonSuspiciousControlFlowGroup"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsTableFull"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsTableNotFull"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsGroupingInUse"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSuspiciousProtocol"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsNonSuspiciousProtocol"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsSuspiciousPriority"),
        ("Juniper-DOS-PROTECTION-PLATFORM-MIB", "juniDosProtectionScfdsNonSuspiciousPriority"))
)
if mibBuilder.loadTexts:
    juniDosProtectionNotificationGroup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniDosProtectionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniDosProtectionCompliance.setStatus(
        "obsolete"
    )

juniDosProtectionCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 81, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniDosProtectionCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DOS-PROTECTION-PLATFORM-MIB",
    **{"juniDosProtectionPlatformMIB": juniDosProtectionPlatformMIB,
       "juniDosProtectionPlatformTraps": juniDosProtectionPlatformTraps,
       "juniDosProtectionPlatformScfdsTraps": juniDosProtectionPlatformScfdsTraps,
       "juniDosProtectionScfdsSuspiciousControlFlow": juniDosProtectionScfdsSuspiciousControlFlow,
       "juniDosProtectionScfdsNonSuspiciousControlFlow": juniDosProtectionScfdsNonSuspiciousControlFlow,
       "juniDosProtectionScfdsSuspiciousControlFlowGroup": juniDosProtectionScfdsSuspiciousControlFlowGroup,
       "juniDosProtectionScfdsNonSuspiciousControlFlowGroup": juniDosProtectionScfdsNonSuspiciousControlFlowGroup,
       "juniDosProtectionScfdsTableFull": juniDosProtectionScfdsTableFull,
       "juniDosProtectionScfdsTableNotFull": juniDosProtectionScfdsTableNotFull,
       "juniDosProtectionScfdsGroupingInUse": juniDosProtectionScfdsGroupingInUse,
       "juniDosProtectionScfdsSuspiciousProtocol": juniDosProtectionScfdsSuspiciousProtocol,
       "juniDosProtectionScfdsNonSuspiciousProtocol": juniDosProtectionScfdsNonSuspiciousProtocol,
       "juniDosProtectionScfdsSuspiciousPriority": juniDosProtectionScfdsSuspiciousPriority,
       "juniDosProtectionScfdsNonSuspiciousPriority": juniDosProtectionScfdsNonSuspiciousPriority,
       "juniDosProtectionScfdsSuspiciousControlFlowMac": juniDosProtectionScfdsSuspiciousControlFlowMac,
       "juniDosProtectionScfdsNonSuspiciousControlFlowMac": juniDosProtectionScfdsNonSuspiciousControlFlowMac,
       "juniDosProtectionPlatformObjects": juniDosProtectionPlatformObjects,
       "juniDosProtectionPlatformScfdsGroup": juniDosProtectionPlatformScfdsGroup,
       "juniDosProtectionScfdsSlotProtocolTable": juniDosProtectionScfdsSlotProtocolTable,
       "juniDosProtectionScfdsSlotProtocolEntry": juniDosProtectionScfdsSlotProtocolEntry,
       "juniDosProtectionScfdsSlotProtocolSlot": juniDosProtectionScfdsSlotProtocolSlot,
       "juniDosProtectionScfdsSlotProtocolIndex": juniDosProtectionScfdsSlotProtocolIndex,
       "juniDosProtectionScfdsSlotProtocolState": juniDosProtectionScfdsSlotProtocolState,
       "juniDosProtectionScfdsSlotProtocolTransitions": juniDosProtectionScfdsSlotProtocolTransitions,
       "juniDosProtectionScfdsSlotFlowTable": juniDosProtectionScfdsSlotFlowTable,
       "juniDosProtectionScfdsSlotFlowEntry": juniDosProtectionScfdsSlotFlowEntry,
       "juniDosProtectionScfdsSlotFlowSlot": juniDosProtectionScfdsSlotFlowSlot,
       "juniDosProtectionScfdsSlotFlowIfIndex": juniDosProtectionScfdsSlotFlowIfIndex,
       "juniDosProtectionScfdsSlotFlowGroupId": juniDosProtectionScfdsSlotFlowGroupId,
       "juniDosProtectionScfdsSlotFlowProtocol": juniDosProtectionScfdsSlotFlowProtocol,
       "juniDosProtectionScfdsSlotFlowRate": juniDosProtectionScfdsSlotFlowRate,
       "juniDosProtectionScfdsSlotFlowPeakRate": juniDosProtectionScfdsSlotFlowPeakRate,
       "juniDosProtectionScfdsSlotFlowTimeFlagged": juniDosProtectionScfdsSlotFlowTimeFlagged,
       "juniDosProtectionScfdsSlotFlowIngressSlot": juniDosProtectionScfdsSlotFlowIngressSlot,
       "juniDosProtectionScfdsSlotFlowGroup": juniDosProtectionScfdsSlotFlowGroup,
       "juniDosProtectionScfdsSlotFlowClearEntry": juniDosProtectionScfdsSlotFlowClearEntry,
       "juniDosProtectionScfdsSlotTable": juniDosProtectionScfdsSlotTable,
       "juniDosProtectionScfdsSlotEntry": juniDosProtectionScfdsSlotEntry,
       "juniDosProtectionScfdsSlotSlot": juniDosProtectionScfdsSlotSlot,
       "juniDosProtectionScfdsSlotClearAll": juniDosProtectionScfdsSlotClearAll,
       "juniDosProtectionScfdsSlotDiscontinuityTime": juniDosProtectionScfdsSlotDiscontinuityTime,
       "juniDosProtectionScfdsSlotTableOverflowState": juniDosProtectionScfdsSlotTableOverflowState,
       "juniDosProtectionScfdsSlotCurrentSuspiciousFlows": juniDosProtectionScfdsSlotCurrentSuspiciousFlows,
       "juniDosProtectionScfdsSlotNumberSuspiciousFlows": juniDosProtectionScfdsSlotNumberSuspiciousFlows,
       "juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups": juniDosProtectionScfdsSlotNumberSuspiciousFlowGroups,
       "juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups": juniDosProtectionScfdsSlotCurrentSuspiciousFlowGroups,
       "juniDosProtectionScfdsSlotCurrentFalseNegativeFlows": juniDosProtectionScfdsSlotCurrentFalseNegativeFlows,
       "juniDosProtectionScfdsSlotNumberFalseNegativeFlows": juniDosProtectionScfdsSlotNumberFalseNegativeFlows,
       "juniDosProtectionScfdsSlotOverflows": juniDosProtectionScfdsSlotOverflows,
       "juniDosProtectionScfdsSlotFlowMacTable": juniDosProtectionScfdsSlotFlowMacTable,
       "juniDosProtectionScfdsSlotFlowMacEntry": juniDosProtectionScfdsSlotFlowMacEntry,
       "juniDosProtectionScfdsSlotFlowMacSlot": juniDosProtectionScfdsSlotFlowMacSlot,
       "juniDosProtectionScfdsSlotFlowMacIfIndex": juniDosProtectionScfdsSlotFlowMacIfIndex,
       "juniDosProtectionScfdsSlotFlowMacGroupId": juniDosProtectionScfdsSlotFlowMacGroupId,
       "juniDosProtectionScfdsSlotFlowMacProtocol": juniDosProtectionScfdsSlotFlowMacProtocol,
       "juniDosProtectionScfdsSlotFlowMacSrcMac": juniDosProtectionScfdsSlotFlowMacSrcMac,
       "juniDosProtectionScfdsSlotFlowMacRate": juniDosProtectionScfdsSlotFlowMacRate,
       "juniDosProtectionScfdsSlotFlowMacPeakRate": juniDosProtectionScfdsSlotFlowMacPeakRate,
       "juniDosProtectionScfdsSlotFlowMacTimeFlagged": juniDosProtectionScfdsSlotFlowMacTimeFlagged,
       "juniDosProtectionScfdsSlotFlowMacIngressSlot": juniDosProtectionScfdsSlotFlowMacIngressSlot,
       "juniDosProtectionScfdsSlotFlowMacGroup": juniDosProtectionScfdsSlotFlowMacGroup,
       "juniDosProtectionScfdsSlotFlowMacClearEntry": juniDosProtectionScfdsSlotFlowMacClearEntry,
       "juniDosProtectionPlatformDpgGroup": juniDosProtectionPlatformDpgGroup,
       "juniDosProtectionDpgSlotRateTable": juniDosProtectionDpgSlotRateTable,
       "juniDosProtectionDpgSlotRateEntry": juniDosProtectionDpgSlotRateEntry,
       "juniDosProtectionDpgSlotRateSlot": juniDosProtectionDpgSlotRateSlot,
       "juniDosProtectionDpgSlotRateDpgName": juniDosProtectionDpgSlotRateDpgName,
       "juniDosProtectionDpgSlotRateProtocol": juniDosProtectionDpgSlotRateProtocol,
       "juniDosProtectionDpgSlotRateMinRate": juniDosProtectionDpgSlotRateMinRate,
       "juniDosProtectionDpgSlotRateMaxRate": juniDosProtectionDpgSlotRateMaxRate,
       "juniDosProtectionDpgSlotRateMinBurst": juniDosProtectionDpgSlotRateMinBurst,
       "juniDosProtectionDpgSlotRateMaxBurst": juniDosProtectionDpgSlotRateMaxBurst,
       "juniDosProtectionPlatformTrapControl": juniDosProtectionPlatformTrapControl,
       "juniDosProtectionScfdsSlot": juniDosProtectionScfdsSlot,
       "juniDosProtectionPriority": juniDosProtectionPriority,
       "juniDosProtectionProtocol": juniDosProtectionProtocol,
       "juniDosProtectionIfIndex": juniDosProtectionIfIndex,
       "juniDosProtectionGroupId": juniDosProtectionGroupId,
       "juniDosProtectionSrcPhysAddr": juniDosProtectionSrcPhysAddr,
       "juniDosProtectionScfdsFlowRate": juniDosProtectionScfdsFlowRate,
       "juniDosProtectionPlatformMIBConformance": juniDosProtectionPlatformMIBConformance,
       "juniDosProtectionPlatformMIBCompliances": juniDosProtectionPlatformMIBCompliances,
       "juniDosProtectionCompliance": juniDosProtectionCompliance,
       "juniDosProtectionCompliance2": juniDosProtectionCompliance2,
       "juniDosProtectionPlatformMIBGroups": juniDosProtectionPlatformMIBGroups,
       "juniDosProtectionGroup": juniDosProtectionGroup,
       "juniDosProtectionNotificationGroup": juniDosProtectionNotificationGroup,
       "juniDosProtectionGroup1": juniDosProtectionGroup1,
       "juniDosProtectionNotificationGroup1": juniDosProtectionNotificationGroup1}
)

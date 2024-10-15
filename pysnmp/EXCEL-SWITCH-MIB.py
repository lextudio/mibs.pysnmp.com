# SNMP MIB module (EXCEL-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXCEL-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:05 2024
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
 ObjectName,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "ObjectName",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

excel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67)
)


# Types definitions



class SlotsInNode(Integer32):
    """Custom type SlotsInNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )





class DSPFunctionTypes(Integer32):
    """Custom type DSPFunctionTypes based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("confMixed", 16),
          ("confMonitor", 17),
          ("confStandard", 15),
          ("genBongTone", 11),
          ("genCPT4", 14),
          ("genDTMF", 9),
          ("genMFR1", 10),
          ("genMFR2Backward", 13),
          ("genMFR2Forward", 12),
          ("other", 1),
          ("recCPA", 6),
          ("recDTMF", 2),
          ("recDTMFHighPassFilter", 3),
          ("recE1Pulse", 7),
          ("recEnergyDetection", 8),
          ("recMFR1", 4),
          ("recMFR2", 5),
          ("vras", 18))
    )





class CardOperState(Integer32):
    """Custom type CardOperState based on Integer32"""
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
        *(("generalHWFailure", 5),
          ("inService", 1),
          ("needsSystemSW", 6),
          ("oosByHost", 3),
          ("oosBySwitch", 2),
          ("other", 7),
          ("standbyByHost", 4))
    )





class SS7VariantsTypes(Integer32):
    """Custom type SS7VariantsTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 1),
          ("itu-ts", 2),
          ("none", 3))
    )





class PayloadTypes(Integer32):
    """Custom type PayloadTypes based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("g711aLaw", 1),
          ("g711uLaw", 2),
          ("g723-5-3", 16),
          ("g723-6-3", 17),
          ("g726-16", 3),
          ("g726-24", 4),
          ("g726-32", 5),
          ("g726-40", 6),
          ("g727-16", 7),
          ("g727-16-24", 8),
          ("g727-24", 9),
          ("g727-32", 12),
          ("g727-32-16", 10),
          ("g727-32-24", 11),
          ("g727-40-16", 13),
          ("g727-40-24", 14),
          ("g727-40-32", 15),
          ("g728", 19),
          ("g729", 18),
          ("netCoder-4-8", 21),
          ("netCoder-5-6", 22),
          ("netCoder-6-4", 23),
          ("netCoder-7-2", 24),
          ("netCoder-8-0", 25),
          ("netCoder-8-8", 26),
          ("netCoder-9-6", 27),
          ("transparentPCM", 20))
    )





class PacketDepth(Integer32):
    """Custom type PacketDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRedundancy", 1),
          ("redundancyLevelOne", 2),
          ("redundancyLevelTwo", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_ExcelTraps_ObjectIdentity = ObjectIdentity
excelTraps = _ExcelTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0)
)
_ExcelProducts_ObjectIdentity = ObjectIdentity
excelProducts = _ExcelProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2)
)
_ExcelSystem_ObjectIdentity = ObjectIdentity
excelSystem = _ExcelSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 1)
)
_ExcelNodeIdentifier_Type = DisplayString
_ExcelNodeIdentifier_Object = MibScalar
excelNodeIdentifier = _ExcelNodeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 1, 1),
    _ExcelNodeIdentifier_Type()
)
excelNodeIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelNodeIdentifier.setStatus("current")
_ExcelNodeLocationIdentifier_Type = DisplayString
_ExcelNodeLocationIdentifier_Object = MibScalar
excelNodeLocationIdentifier = _ExcelNodeLocationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 1, 2),
    _ExcelNodeLocationIdentifier_Type()
)
excelNodeLocationIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelNodeLocationIdentifier.setStatus("current")
_ExcelNodeCurrentTime_Type = DisplayString
_ExcelNodeCurrentTime_Object = MibScalar
excelNodeCurrentTime = _ExcelNodeCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 1, 3),
    _ExcelNodeCurrentTime_Type()
)
excelNodeCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelNodeCurrentTime.setStatus("current")
_ExcelSwitch_ObjectIdentity = ObjectIdentity
excelSwitch = _ExcelSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2)
)


class _ExcelCurrentNode_Type(Integer32):
    """Custom type excelCurrentNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelCurrentNode_Type.__name__ = "Integer32"
_ExcelCurrentNode_Object = MibScalar
excelCurrentNode = _ExcelCurrentNode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 1),
    _ExcelCurrentNode_Type()
)
excelCurrentNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelCurrentNode.setStatus("current")


class _ExcelNodes_Type(Integer32):
    """Custom type excelNodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ExcelNodes_Type.__name__ = "Integer32"
_ExcelNodes_Object = MibScalar
excelNodes = _ExcelNodes_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 2),
    _ExcelNodes_Type()
)
excelNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelNodes.setStatus("current")
_ExcelNodeTable_Object = MibTable
excelNodeTable = _ExcelNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 3)
)
if mibBuilder.loadTexts:
    excelNodeTable.setStatus("current")
_ExcelNodeEntry_Object = MibTableRow
excelNodeEntry = _ExcelNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 3, 1)
)
excelNodeEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelNodeIndex"),
)
if mibBuilder.loadTexts:
    excelNodeEntry.setStatus("current")


class _ExcelNodeIndex_Type(Integer32):
    """Custom type excelNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ExcelNodeIndex_Type.__name__ = "Integer32"
_ExcelNodeIndex_Object = MibTableColumn
excelNodeIndex = _ExcelNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 3, 1, 1),
    _ExcelNodeIndex_Type()
)
excelNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelNodeIndex.setStatus("current")


class _ExcelNodeLogicalID_Type(Integer32):
    """Custom type excelNodeLogicalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelNodeLogicalID_Type.__name__ = "Integer32"
_ExcelNodeLogicalID_Object = MibTableColumn
excelNodeLogicalID = _ExcelNodeLogicalID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 3, 1, 2),
    _ExcelNodeLogicalID_Type()
)
excelNodeLogicalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelNodeLogicalID.setStatus("current")


class _ExcelNodePhysicalID_Type(Integer32):
    """Custom type excelNodePhysicalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_ExcelNodePhysicalID_Type.__name__ = "Integer32"
_ExcelNodePhysicalID_Object = MibTableColumn
excelNodePhysicalID = _ExcelNodePhysicalID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 3, 1, 3),
    _ExcelNodePhysicalID_Type()
)
excelNodePhysicalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelNodePhysicalID.setStatus("current")


class _ExcelNodeType_Type(Integer32):
    """Custom type excelNodeType based on Integer32"""
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
        *(("csn", 3),
          ("exnetConnect", 5),
          ("lnx", 4),
          ("other", 1),
          ("pcx", 2))
    )


_ExcelNodeType_Type.__name__ = "Integer32"
_ExcelNodeType_Object = MibTableColumn
excelNodeType = _ExcelNodeType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 3, 1, 4),
    _ExcelNodeType_Type()
)
excelNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelNodeType.setStatus("current")
_ExcelNode_ObjectIdentity = ObjectIdentity
excelNode = _ExcelNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4)
)
_ExcelNodeHardware_ObjectIdentity = ObjectIdentity
excelNodeHardware = _ExcelNodeHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1)
)
_ExcelCommunicationEquipment_ObjectIdentity = ObjectIdentity
excelCommunicationEquipment = _ExcelCommunicationEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1)
)
_ExcelCommunicationCard_ObjectIdentity = ObjectIdentity
excelCommunicationCard = _ExcelCommunicationCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 1)
)
_ExcelCommCardTable_Object = MibTable
excelCommCardTable = _ExcelCommCardTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    excelCommCardTable.setStatus("current")
_ExcelCommCardEntry_Object = MibTableRow
excelCommCardEntry = _ExcelCommCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 1, 1, 1)
)
excelCommCardEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelCommCardSlotIndex"),
)
if mibBuilder.loadTexts:
    excelCommCardEntry.setStatus("current")
_ExcelCommCardSlotIndex_Type = SlotsInNode
_ExcelCommCardSlotIndex_Object = MibTableColumn
excelCommCardSlotIndex = _ExcelCommCardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 1, 1, 1, 1),
    _ExcelCommCardSlotIndex_Type()
)
excelCommCardSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelCommCardSlotIndex.setStatus("current")
_ExcelCommCardOperState_Type = CardOperState
_ExcelCommCardOperState_Object = MibTableColumn
excelCommCardOperState = _ExcelCommCardOperState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 1, 1, 1, 2),
    _ExcelCommCardOperState_Type()
)
excelCommCardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelCommCardOperState.setStatus("current")


class _ExcelCommCardResetReason_Type(Integer32):
    """Custom type excelCommCardResetReason based on Integer32"""
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
        *(("other", 1),
          ("powerUp", 3),
          ("resetButton", 4),
          ("unKnown", 2))
    )


_ExcelCommCardResetReason_Type.__name__ = "Integer32"
_ExcelCommCardResetReason_Object = MibTableColumn
excelCommCardResetReason = _ExcelCommCardResetReason_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 1, 1, 1, 3),
    _ExcelCommCardResetReason_Type()
)
excelCommCardResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelCommCardResetReason.setStatus("current")


class _ExcelCommCardConfigStatus_Type(Integer32):
    """Custom type excelCommCardConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("unknown", 3),
          ("valid", 2))
    )


_ExcelCommCardConfigStatus_Type.__name__ = "Integer32"
_ExcelCommCardConfigStatus_Object = MibTableColumn
excelCommCardConfigStatus = _ExcelCommCardConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 1, 1, 1, 4),
    _ExcelCommCardConfigStatus_Type()
)
excelCommCardConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelCommCardConfigStatus.setStatus("current")


class _ExcelCommCardConfidenceTest_Type(Integer32):
    """Custom type excelCommCardConfidenceTest based on Integer32"""
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
        *(("otherFailure", 2),
          ("passed", 1),
          ("ramFailure", 3),
          ("romFailure", 4))
    )


_ExcelCommCardConfidenceTest_Type.__name__ = "Integer32"
_ExcelCommCardConfidenceTest_Object = MibTableColumn
excelCommCardConfidenceTest = _ExcelCommCardConfidenceTest_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 1, 1, 1, 5),
    _ExcelCommCardConfidenceTest_Type()
)
excelCommCardConfidenceTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelCommCardConfidenceTest.setStatus("current")


class _ExcelCommCardAction_Type(Integer32):
    """Custom type excelCommCardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("shutdown", 3),
          ("unlocked", 2))
    )


_ExcelCommCardAction_Type.__name__ = "Integer32"
_ExcelCommCardAction_Object = MibTableColumn
excelCommCardAction = _ExcelCommCardAction_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 1, 1, 1, 6),
    _ExcelCommCardAction_Type()
)
excelCommCardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelCommCardAction.setStatus("current")
_ExcelCommCardActionTime_Type = DisplayString
_ExcelCommCardActionTime_Object = MibTableColumn
excelCommCardActionTime = _ExcelCommCardActionTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 1, 1, 1, 7),
    _ExcelCommCardActionTime_Type()
)
excelCommCardActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelCommCardActionTime.setStatus("current")
_ExcelDSP_ObjectIdentity = ObjectIdentity
excelDSP = _ExcelDSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2)
)
_ExcelVoipDsp_ObjectIdentity = ObjectIdentity
excelVoipDsp = _ExcelVoipDsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1)
)


class _ExcelVoipSlotNumber_Type(Integer32):
    """Custom type excelVoipSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ExcelVoipSlotNumber_Type.__name__ = "Integer32"
_ExcelVoipSlotNumber_Object = MibScalar
excelVoipSlotNumber = _ExcelVoipSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 1),
    _ExcelVoipSlotNumber_Type()
)
excelVoipSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelVoipSlotNumber.setStatus("current")
_ExcelVoipDspTable_Object = MibTable
excelVoipDspTable = _ExcelVoipDspTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    excelVoipDspTable.setStatus("current")
_ExcelVoipDspEntry_Object = MibTableRow
excelVoipDspEntry = _ExcelVoipDspEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1)
)
excelVoipDspEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelVoipDspIndex"),
)
if mibBuilder.loadTexts:
    excelVoipDspEntry.setStatus("current")


class _ExcelVoipDspIndex_Type(Integer32):
    """Custom type excelVoipDspIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ExcelVoipDspIndex_Type.__name__ = "Integer32"
_ExcelVoipDspIndex_Object = MibTableColumn
excelVoipDspIndex = _ExcelVoipDspIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1, 1),
    _ExcelVoipDspIndex_Type()
)
excelVoipDspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelVoipDspIndex.setStatus("current")


class _ExcelVoipDspInstalled_Type(Integer32):
    """Custom type excelVoipDspInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_ExcelVoipDspInstalled_Type.__name__ = "Integer32"
_ExcelVoipDspInstalled_Object = MibTableColumn
excelVoipDspInstalled = _ExcelVoipDspInstalled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1, 2),
    _ExcelVoipDspInstalled_Type()
)
excelVoipDspInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipDspInstalled.setStatus("current")


class _ExcelVoipDspNumChannelsSupported_Type(Integer32):
    """Custom type excelVoipDspNumChannelsSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_ExcelVoipDspNumChannelsSupported_Type.__name__ = "Integer32"
_ExcelVoipDspNumChannelsSupported_Object = MibTableColumn
excelVoipDspNumChannelsSupported = _ExcelVoipDspNumChannelsSupported_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1, 3),
    _ExcelVoipDspNumChannelsSupported_Type()
)
excelVoipDspNumChannelsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipDspNumChannelsSupported.setStatus("current")
_ExcelVoipDspOperState_Type = CardOperState
_ExcelVoipDspOperState_Object = MibTableColumn
excelVoipDspOperState = _ExcelVoipDspOperState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1, 4),
    _ExcelVoipDspOperState_Type()
)
excelVoipDspOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipDspOperState.setStatus("current")
_ExcelVoipDspArtworkRevision_Type = DisplayString
_ExcelVoipDspArtworkRevision_Object = MibTableColumn
excelVoipDspArtworkRevision = _ExcelVoipDspArtworkRevision_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1, 5),
    _ExcelVoipDspArtworkRevision_Type()
)
excelVoipDspArtworkRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipDspArtworkRevision.setStatus("current")


class _ExcelVoipDspFuncRevision_Type(Integer32):
    """Custom type excelVoipDspFuncRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_ExcelVoipDspFuncRevision_Type.__name__ = "Integer32"
_ExcelVoipDspFuncRevision_Object = MibTableColumn
excelVoipDspFuncRevision = _ExcelVoipDspFuncRevision_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1, 6),
    _ExcelVoipDspFuncRevision_Type()
)
excelVoipDspFuncRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipDspFuncRevision.setStatus("current")
_ExcelVoipDspHWRevision_Type = DisplayString
_ExcelVoipDspHWRevision_Object = MibTableColumn
excelVoipDspHWRevision = _ExcelVoipDspHWRevision_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1, 7),
    _ExcelVoipDspHWRevision_Type()
)
excelVoipDspHWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipDspHWRevision.setStatus("current")
_ExcelVoipDspSWRevision_Type = DisplayString
_ExcelVoipDspSWRevision_Object = MibTableColumn
excelVoipDspSWRevision = _ExcelVoipDspSWRevision_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1, 8),
    _ExcelVoipDspSWRevision_Type()
)
excelVoipDspSWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipDspSWRevision.setStatus("current")


class _ExcelVoipDspRamSize_Type(Integer32):
    """Custom type excelVoipDspRamSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_ExcelVoipDspRamSize_Type.__name__ = "Integer32"
_ExcelVoipDspRamSize_Object = MibTableColumn
excelVoipDspRamSize = _ExcelVoipDspRamSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1, 9),
    _ExcelVoipDspRamSize_Type()
)
excelVoipDspRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipDspRamSize.setStatus("current")


class _ExcelVoipDspSerialNum_Type(Integer32):
    """Custom type excelVoipDspSerialNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ExcelVoipDspSerialNum_Type.__name__ = "Integer32"
_ExcelVoipDspSerialNum_Object = MibTableColumn
excelVoipDspSerialNum = _ExcelVoipDspSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1, 10),
    _ExcelVoipDspSerialNum_Type()
)
excelVoipDspSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipDspSerialNum.setStatus("current")


class _ExcelVoipDspRamBuildNumber_Type(Integer32):
    """Custom type excelVoipDspRamBuildNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ExcelVoipDspRamBuildNumber_Type.__name__ = "Integer32"
_ExcelVoipDspRamBuildNumber_Object = MibTableColumn
excelVoipDspRamBuildNumber = _ExcelVoipDspRamBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 1, 2, 1, 2, 1, 11),
    _ExcelVoipDspRamBuildNumber_Type()
)
excelVoipDspRamBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipDspRamBuildNumber.setStatus("current")
_ExcelDeviceEquipment_ObjectIdentity = ObjectIdentity
excelDeviceEquipment = _ExcelDeviceEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2)
)
_ExcelDeviceCard_ObjectIdentity = ObjectIdentity
excelDeviceCard = _ExcelDeviceCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1)
)
_ExcelDeviceCardTable_Object = MibTable
excelDeviceCardTable = _ExcelDeviceCardTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    excelDeviceCardTable.setStatus("current")
_ExcelDeviceCardEntry_Object = MibTableRow
excelDeviceCardEntry = _ExcelDeviceCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1, 1)
)
excelDeviceCardEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
)
if mibBuilder.loadTexts:
    excelDeviceCardEntry.setStatus("current")
_ExcelDeviceCardSlotIndex_Type = SlotsInNode
_ExcelDeviceCardSlotIndex_Object = MibTableColumn
excelDeviceCardSlotIndex = _ExcelDeviceCardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1, 1, 1),
    _ExcelDeviceCardSlotIndex_Type()
)
excelDeviceCardSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelDeviceCardSlotIndex.setStatus("current")


class _ExcelDeviceCardType_Type(Integer32):
    """Custom type excelDeviceCardType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60)
        )
    )
    namedValues = NamedValues(
        *(("analogInterfaceIO", 33),
          ("dass2", 24),
          ("dead", 3),
          ("ds3LineCard", 56),
          ("embeddedHostCard", 44),
          ("empty", 2),
          ("exCPU1000", 8),
          ("exCPU2000", 7),
          ("exCpuHP", 54),
          ("exCpuIO", 30),
          ("exHost", 58),
          ("exNetIO", 31),
          ("exNetOne", 50),
          ("exnetConnect", 45),
          ("exnetController", 25),
          ("exsMTXCtrl1000", 60),
          ("exsMTXCtrlIO", 59),
          ("frontFanTray", 28),
          ("isdnPQ", 57),
          ("isdnPRIRedunIO", 40),
          ("isdnPri24", 18),
          ("isdnPri32", 19),
          ("mfDsp", 16),
          ("midplane", 29),
          ("openNetDSP", 17),
          ("openNetE1120OhmIO", 34),
          ("openNetE1120RedunIO", 43),
          ("openNetE116Span", 14),
          ("openNetE18Span", 13),
          ("openNetJ116Span", 49),
          ("openNetT1100RedunIO", 48),
          ("openNetT116Span", 47),
          ("openNetT18Span", 46),
          ("other", 1),
          ("powerSupply150", 6),
          ("powerSupply60", 4),
          ("powerSupply90", 5),
          ("rbiIO", 32),
          ("rearFanTray", 27),
          ("smartE1120OhmIO", 35),
          ("smartE14Span", 11),
          ("smartE175OhmIO", 36),
          ("smartE18Span", 12),
          ("smartJ1120OhmIO", 37),
          ("smartLineCardRedunIO", 42),
          ("smartT14Span", 9),
          ("smartT18Span", 10),
          ("smartT1IO", 38),
          ("smartfourSpanJ1", 15),
          ("ss7EightLink", 22),
          ("ss7FourLink", 21),
          ("ss7HP", 55),
          ("ss7PQ", 51),
          ("ss7RedunIO", 41),
          ("ss7SixteenLink", 23),
          ("ss7TwoLink", 20),
          ("standbyIO", 39),
          ("subrateController", 26),
          ("vdacVoIP", 52),
          ("vdacVoIPModule", 53))
    )


_ExcelDeviceCardType_Type.__name__ = "Integer32"
_ExcelDeviceCardType_Object = MibTableColumn
excelDeviceCardType = _ExcelDeviceCardType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1, 1, 2),
    _ExcelDeviceCardType_Type()
)
excelDeviceCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelDeviceCardType.setStatus("current")
_ExcelDeviceCardModelDescription_Type = DisplayString
_ExcelDeviceCardModelDescription_Object = MibTableColumn
excelDeviceCardModelDescription = _ExcelDeviceCardModelDescription_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1, 1, 3),
    _ExcelDeviceCardModelDescription_Type()
)
excelDeviceCardModelDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelDeviceCardModelDescription.setStatus("current")
_ExcelDeviceCardArtworkRevision_Type = DisplayString
_ExcelDeviceCardArtworkRevision_Object = MibTableColumn
excelDeviceCardArtworkRevision = _ExcelDeviceCardArtworkRevision_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1, 1, 4),
    _ExcelDeviceCardArtworkRevision_Type()
)
excelDeviceCardArtworkRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelDeviceCardArtworkRevision.setStatus("current")


class _ExcelDeviceCardFuncRevision_Type(Integer32):
    """Custom type excelDeviceCardFuncRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ExcelDeviceCardFuncRevision_Type.__name__ = "Integer32"
_ExcelDeviceCardFuncRevision_Object = MibTableColumn
excelDeviceCardFuncRevision = _ExcelDeviceCardFuncRevision_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1, 1, 5),
    _ExcelDeviceCardFuncRevision_Type()
)
excelDeviceCardFuncRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelDeviceCardFuncRevision.setStatus("current")
_ExcelDeviceCardHWRevision_Type = DisplayString
_ExcelDeviceCardHWRevision_Object = MibTableColumn
excelDeviceCardHWRevision = _ExcelDeviceCardHWRevision_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1, 1, 6),
    _ExcelDeviceCardHWRevision_Type()
)
excelDeviceCardHWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelDeviceCardHWRevision.setStatus("current")
_ExcelDeviceCardSWRevision_Type = DisplayString
_ExcelDeviceCardSWRevision_Object = MibTableColumn
excelDeviceCardSWRevision = _ExcelDeviceCardSWRevision_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1, 1, 7),
    _ExcelDeviceCardSWRevision_Type()
)
excelDeviceCardSWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelDeviceCardSWRevision.setStatus("current")


class _ExcelDeviceCardRamSize_Type(Integer32):
    """Custom type excelDeviceCardRamSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_ExcelDeviceCardRamSize_Type.__name__ = "Integer32"
_ExcelDeviceCardRamSize_Object = MibTableColumn
excelDeviceCardRamSize = _ExcelDeviceCardRamSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1, 1, 8),
    _ExcelDeviceCardRamSize_Type()
)
excelDeviceCardRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelDeviceCardRamSize.setStatus("current")


class _ExcelDeviceCardSerialNum_Type(Integer32):
    """Custom type excelDeviceCardSerialNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32565),
    )


_ExcelDeviceCardSerialNum_Type.__name__ = "Integer32"
_ExcelDeviceCardSerialNum_Object = MibTableColumn
excelDeviceCardSerialNum = _ExcelDeviceCardSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1, 1, 9),
    _ExcelDeviceCardSerialNum_Type()
)
excelDeviceCardSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelDeviceCardSerialNum.setStatus("current")


class _ExcelDeviceCardRAMBuildNum_Type(Integer32):
    """Custom type excelDeviceCardRAMBuildNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32565),
    )


_ExcelDeviceCardRAMBuildNum_Type.__name__ = "Integer32"
_ExcelDeviceCardRAMBuildNum_Object = MibTableColumn
excelDeviceCardRAMBuildNum = _ExcelDeviceCardRAMBuildNum_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 1, 1, 1, 10),
    _ExcelDeviceCardRAMBuildNum_Type()
)
excelDeviceCardRAMBuildNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelDeviceCardRAMBuildNum.setStatus("current")
_ExcelUtility_ObjectIdentity = ObjectIdentity
excelUtility = _ExcelUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 2, 2)
)
_ExcelResourceEquipment_ObjectIdentity = ObjectIdentity
excelResourceEquipment = _ExcelResourceEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3)
)
_ExcelResourceUtilization_ObjectIdentity = ObjectIdentity
excelResourceUtilization = _ExcelResourceUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1)
)


class _ExcelResourceSlotId_Type(Integer32):
    """Custom type excelResourceSlotId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ExcelResourceSlotId_Type.__name__ = "Integer32"
_ExcelResourceSlotId_Object = MibScalar
excelResourceSlotId = _ExcelResourceSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 1),
    _ExcelResourceSlotId_Type()
)
excelResourceSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelResourceSlotId.setStatus("obsolete")
_ExcelResourceUsageTable_Object = MibTable
excelResourceUsageTable = _ExcelResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    excelResourceUsageTable.setStatus("current")
_ExcelResourceUsageEntry_Object = MibTableRow
excelResourceUsageEntry = _ExcelResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 2, 1)
)
excelResourceUsageEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelCurrentNode"),
    (0, "EXCEL-SWITCH-MIB", "excelResourceUsageIndex"),
)
if mibBuilder.loadTexts:
    excelResourceUsageEntry.setStatus("current")


class _ExcelResourceUsageIndex_Type(Integer32):
    """Custom type excelResourceUsageIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ExcelResourceUsageIndex_Type.__name__ = "Integer32"
_ExcelResourceUsageIndex_Object = MibTableColumn
excelResourceUsageIndex = _ExcelResourceUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 2, 1, 1),
    _ExcelResourceUsageIndex_Type()
)
excelResourceUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelResourceUsageIndex.setStatus("current")


class _ExcelCpuTime_Type(Integer32):
    """Custom type excelCpuTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32565),
    )


_ExcelCpuTime_Type.__name__ = "Integer32"
_ExcelCpuTime_Object = MibTableColumn
excelCpuTime = _ExcelCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 2, 1, 2),
    _ExcelCpuTime_Type()
)
excelCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelCpuTime.setStatus("current")


class _ExcelMcbUsage_Type(Integer32):
    """Custom type excelMcbUsage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExcelMcbUsage_Type.__name__ = "Integer32"
_ExcelMcbUsage_Object = MibTableColumn
excelMcbUsage = _ExcelMcbUsage_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 2, 1, 3),
    _ExcelMcbUsage_Type()
)
excelMcbUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMcbUsage.setStatus("current")
_ExcelRegionTable_Object = MibTable
excelRegionTable = _ExcelRegionTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    excelRegionTable.setStatus("current")
_ExcelRegionEntry_Object = MibTableRow
excelRegionEntry = _ExcelRegionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 3, 1)
)
excelRegionEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelCurrentNode"),
    (0, "EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
    (0, "EXCEL-SWITCH-MIB", "excelRegionIndex"),
)
if mibBuilder.loadTexts:
    excelRegionEntry.setStatus("current")


class _ExcelRegionIndex_Type(Integer32):
    """Custom type excelRegionIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ExcelRegionIndex_Type.__name__ = "Integer32"
_ExcelRegionIndex_Object = MibTableColumn
excelRegionIndex = _ExcelRegionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 3, 1, 1),
    _ExcelRegionIndex_Type()
)
excelRegionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelRegionIndex.setStatus("current")


class _ExcelRegionId_Type(Integer32):
    """Custom type excelRegionId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ExcelRegionId_Type.__name__ = "Integer32"
_ExcelRegionId_Object = MibTableColumn
excelRegionId = _ExcelRegionId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 3, 1, 2),
    _ExcelRegionId_Type()
)
excelRegionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelRegionId.setStatus("current")


class _ExcelRegionSize_Type(Integer32):
    """Custom type excelRegionSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32565),
    )


_ExcelRegionSize_Type.__name__ = "Integer32"
_ExcelRegionSize_Object = MibTableColumn
excelRegionSize = _ExcelRegionSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 3, 1, 3),
    _ExcelRegionSize_Type()
)
excelRegionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelRegionSize.setStatus("current")


class _ExcelRegionUsed_Type(Integer32):
    """Custom type excelRegionUsed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32565),
    )


_ExcelRegionUsed_Type.__name__ = "Integer32"
_ExcelRegionUsed_Object = MibTableColumn
excelRegionUsed = _ExcelRegionUsed_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 3, 1, 4),
    _ExcelRegionUsed_Type()
)
excelRegionUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelRegionUsed.setStatus("current")
_ExcelPartitionTable_Object = MibTable
excelPartitionTable = _ExcelPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    excelPartitionTable.setStatus("current")
_ExcelPartitionEntry_Object = MibTableRow
excelPartitionEntry = _ExcelPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 4, 1)
)
excelPartitionEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelCurrentNode"),
    (0, "EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
    (0, "EXCEL-SWITCH-MIB", "excelPartitionIndex"),
)
if mibBuilder.loadTexts:
    excelPartitionEntry.setStatus("current")


class _ExcelPartitionIndex_Type(Integer32):
    """Custom type excelPartitionIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ExcelPartitionIndex_Type.__name__ = "Integer32"
_ExcelPartitionIndex_Object = MibTableColumn
excelPartitionIndex = _ExcelPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 4, 1, 1),
    _ExcelPartitionIndex_Type()
)
excelPartitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelPartitionIndex.setStatus("current")


class _ExcelPartitionId_Type(Integer32):
    """Custom type excelPartitionId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ExcelPartitionId_Type.__name__ = "Integer32"
_ExcelPartitionId_Object = MibTableColumn
excelPartitionId = _ExcelPartitionId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 4, 1, 2),
    _ExcelPartitionId_Type()
)
excelPartitionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelPartitionId.setStatus("current")


class _ExcelPartitionSize_Type(Integer32):
    """Custom type excelPartitionSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32565),
    )


_ExcelPartitionSize_Type.__name__ = "Integer32"
_ExcelPartitionSize_Object = MibTableColumn
excelPartitionSize = _ExcelPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 4, 1, 3),
    _ExcelPartitionSize_Type()
)
excelPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelPartitionSize.setStatus("current")


class _ExcelPartitionUsed_Type(Integer32):
    """Custom type excelPartitionUsed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32565),
    )


_ExcelPartitionUsed_Type.__name__ = "Integer32"
_ExcelPartitionUsed_Object = MibTableColumn
excelPartitionUsed = _ExcelPartitionUsed_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 4, 1, 4),
    _ExcelPartitionUsed_Type()
)
excelPartitionUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelPartitionUsed.setStatus("current")
_ExcelCpuUsageTable_Object = MibTable
excelCpuUsageTable = _ExcelCpuUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    excelCpuUsageTable.setStatus("current")
_ExcelCpuUsageEntry_Object = MibTableRow
excelCpuUsageEntry = _ExcelCpuUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 5, 1)
)
excelCpuUsageEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelCurrentNode"),
    (0, "EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
    (0, "EXCEL-SWITCH-MIB", "excelCpuUsageIndex"),
)
if mibBuilder.loadTexts:
    excelCpuUsageEntry.setStatus("current")


class _ExcelCpuUsageIndex_Type(Integer32):
    """Custom type excelCpuUsageIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ExcelCpuUsageIndex_Type.__name__ = "Integer32"
_ExcelCpuUsageIndex_Object = MibTableColumn
excelCpuUsageIndex = _ExcelCpuUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 5, 1, 1),
    _ExcelCpuUsageIndex_Type()
)
excelCpuUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelCpuUsageIndex.setStatus("current")


class _ExcelCpuUsageTaskId_Type(Integer32):
    """Custom type excelCpuUsageTaskId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ExcelCpuUsageTaskId_Type.__name__ = "Integer32"
_ExcelCpuUsageTaskId_Object = MibTableColumn
excelCpuUsageTaskId = _ExcelCpuUsageTaskId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 5, 1, 2),
    _ExcelCpuUsageTaskId_Type()
)
excelCpuUsageTaskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelCpuUsageTaskId.setStatus("current")


class _ExcelCpuUsageUsed_Type(Integer32):
    """Custom type excelCpuUsageUsed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ExcelCpuUsageUsed_Type.__name__ = "Integer32"
_ExcelCpuUsageUsed_Object = MibTableColumn
excelCpuUsageUsed = _ExcelCpuUsageUsed_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 1, 3, 1, 5, 1, 3),
    _ExcelCpuUsageUsed_Type()
)
excelCpuUsageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelCpuUsageUsed.setStatus("current")
_ExcelNodeSoftware_ObjectIdentity = ObjectIdentity
excelNodeSoftware = _ExcelNodeSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2)
)
_ExcelSystemSoftware_ObjectIdentity = ObjectIdentity
excelSystemSoftware = _ExcelSystemSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1)
)
_ExcelSystemConfig_ObjectIdentity = ObjectIdentity
excelSystemConfig = _ExcelSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 1)
)
_ExcelSystemAlarm_ObjectIdentity = ObjectIdentity
excelSystemAlarm = _ExcelSystemAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 2)
)


class _ExcelSysLastAlarmTrap_Type(Integer32):
    """Custom type excelSysLastAlarmTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ExcelSysLastAlarmTrap_Type.__name__ = "Integer32"
_ExcelSysLastAlarmTrap_Object = MibScalar
excelSysLastAlarmTrap = _ExcelSysLastAlarmTrap_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 2, 1),
    _ExcelSysLastAlarmTrap_Type()
)
excelSysLastAlarmTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSysLastAlarmTrap.setStatus("current")


class _ExcelSysLastAlarmSeverity_Type(Integer32):
    """Custom type excelSysLastAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informative", 1),
          ("major", 3),
          ("minor", 2))
    )


_ExcelSysLastAlarmSeverity_Type.__name__ = "Integer32"
_ExcelSysLastAlarmSeverity_Object = MibScalar
excelSysLastAlarmSeverity = _ExcelSysLastAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 2, 2),
    _ExcelSysLastAlarmSeverity_Type()
)
excelSysLastAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSysLastAlarmSeverity.setStatus("current")


class _ExcelSysLastAlarmNode_Type(Integer32):
    """Custom type excelSysLastAlarmNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSysLastAlarmNode_Type.__name__ = "Integer32"
_ExcelSysLastAlarmNode_Object = MibScalar
excelSysLastAlarmNode = _ExcelSysLastAlarmNode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 2, 3),
    _ExcelSysLastAlarmNode_Type()
)
excelSysLastAlarmNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSysLastAlarmNode.setStatus("current")


class _ExcelSysLastAlarmStatus_Type(Integer32):
    """Custom type excelSysLastAlarmStatus based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("cardActive", 8),
          ("cardAdded", 6),
          ("cardFail", 5),
          ("cardInService", 3),
          ("cardInServiceStandby", 4),
          ("cardOutOfService", 2),
          ("cardRemoved", 7),
          ("cardReset", 9),
          ("nodeDiscovered", 16),
          ("nodeDown", 19),
          ("nodeReady", 18),
          ("nodeUp", 17),
          ("other", 1),
          ("ringConnected", 11),
          ("ringInService", 12),
          ("ringInitializing", 10),
          ("ringOutOfService", 13),
          ("spanDegradedService", 15),
          ("spanLossOfService", 14))
    )


_ExcelSysLastAlarmStatus_Type.__name__ = "Integer32"
_ExcelSysLastAlarmStatus_Object = MibScalar
excelSysLastAlarmStatus = _ExcelSysLastAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 2, 4),
    _ExcelSysLastAlarmStatus_Type()
)
excelSysLastAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSysLastAlarmStatus.setStatus("current")
_ExcelSysLastAlarmDSPLastBlocked_Type = DSPFunctionTypes
_ExcelSysLastAlarmDSPLastBlocked_Object = MibScalar
excelSysLastAlarmDSPLastBlocked = _ExcelSysLastAlarmDSPLastBlocked_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 2, 5),
    _ExcelSysLastAlarmDSPLastBlocked_Type()
)
excelSysLastAlarmDSPLastBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSysLastAlarmDSPLastBlocked.setStatus("current")


class _ExcelSysLastAlarmRefClockSrc_Type(Integer32):
    """Custom type excelSysLastAlarmRefClockSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("refClock1", 2),
          ("refClock2", 3))
    )


_ExcelSysLastAlarmRefClockSrc_Type.__name__ = "Integer32"
_ExcelSysLastAlarmRefClockSrc_Object = MibScalar
excelSysLastAlarmRefClockSrc = _ExcelSysLastAlarmRefClockSrc_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 2, 6),
    _ExcelSysLastAlarmRefClockSrc_Type()
)
excelSysLastAlarmRefClockSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSysLastAlarmRefClockSrc.setStatus("current")
_ExcelRing_ObjectIdentity = ObjectIdentity
excelRing = _ExcelRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3)
)
_ExcelRingTable_Object = MibTable
excelRingTable = _ExcelRingTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    excelRingTable.setStatus("current")
_ExcelRingEntry_Object = MibTableRow
excelRingEntry = _ExcelRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3, 2, 1)
)
excelRingEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelRingLogicalIDIndex"),
)
if mibBuilder.loadTexts:
    excelRingEntry.setStatus("current")


class _ExcelRingLogicalIDIndex_Type(Integer32):
    """Custom type excelRingLogicalIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ExcelRingLogicalIDIndex_Type.__name__ = "Integer32"
_ExcelRingLogicalIDIndex_Object = MibTableColumn
excelRingLogicalIDIndex = _ExcelRingLogicalIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3, 2, 1, 1),
    _ExcelRingLogicalIDIndex_Type()
)
excelRingLogicalIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelRingLogicalIDIndex.setStatus("current")


class _ExcelRingStatus_Type(Integer32):
    """Custom type excelRingStatus based on Integer32"""
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
        *(("connected", 4),
          ("inService", 2),
          ("other", 1),
          ("outOfService", 5),
          ("ringInitializing", 3))
    )


_ExcelRingStatus_Type.__name__ = "Integer32"
_ExcelRingStatus_Object = MibTableColumn
excelRingStatus = _ExcelRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3, 2, 1, 2),
    _ExcelRingStatus_Type()
)
excelRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelRingStatus.setStatus("current")


class _ExcelRingOOSReason_Type(Integer32):
    """Custom type excelRingOOSReason based on Integer32"""
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
        *(("cardInFailedState", 3),
          ("cardIsolatedFromRing", 7),
          ("cardReset", 2),
          ("cardResetFailure", 4),
          ("cardResetTimeout", 5),
          ("cardTimeout", 6),
          ("other", 1),
          ("ringInternalOOS", 8),
          ("ringNotReceivingLight", 9),
          ("ringOOS", 10))
    )


_ExcelRingOOSReason_Type.__name__ = "Integer32"
_ExcelRingOOSReason_Object = MibTableColumn
excelRingOOSReason = _ExcelRingOOSReason_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3, 2, 1, 3),
    _ExcelRingOOSReason_Type()
)
excelRingOOSReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelRingOOSReason.setStatus("current")


class _ExcelRingTransmitMode_Type(Integer32):
    """Custom type excelRingTransmitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("receiveOnly", 1),
          ("transmitReceive", 2))
    )


_ExcelRingTransmitMode_Type.__name__ = "Integer32"
_ExcelRingTransmitMode_Object = MibTableColumn
excelRingTransmitMode = _ExcelRingTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3, 2, 1, 4),
    _ExcelRingTransmitMode_Type()
)
excelRingTransmitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelRingTransmitMode.setStatus("current")


class _ExcelRingNodeRole_Type(Integer32):
    """Custom type excelRingNodeRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("other", 3),
          ("slave", 1))
    )


_ExcelRingNodeRole_Type.__name__ = "Integer32"
_ExcelRingNodeRole_Object = MibTableColumn
excelRingNodeRole = _ExcelRingNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3, 2, 1, 5),
    _ExcelRingNodeRole_Type()
)
excelRingNodeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelRingNodeRole.setStatus("current")
_ExcelRingCtrlSlot_Type = SlotsInNode
_ExcelRingCtrlSlot_Object = MibTableColumn
excelRingCtrlSlot = _ExcelRingCtrlSlot_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3, 2, 1, 6),
    _ExcelRingCtrlSlot_Type()
)
excelRingCtrlSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelRingCtrlSlot.setStatus("current")


class _ExcelRingPortAStatus_Type(Integer32):
    """Custom type excelRingPortAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopBack", 3),
          ("normal", 2),
          ("other", 1))
    )


_ExcelRingPortAStatus_Type.__name__ = "Integer32"
_ExcelRingPortAStatus_Object = MibTableColumn
excelRingPortAStatus = _ExcelRingPortAStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3, 2, 1, 7),
    _ExcelRingPortAStatus_Type()
)
excelRingPortAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelRingPortAStatus.setStatus("current")


class _ExcelRingPortBStatus_Type(Integer32):
    """Custom type excelRingPortBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopBack", 3),
          ("normal", 2),
          ("other", 1))
    )


_ExcelRingPortBStatus_Type.__name__ = "Integer32"
_ExcelRingPortBStatus_Object = MibTableColumn
excelRingPortBStatus = _ExcelRingPortBStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3, 2, 1, 8),
    _ExcelRingPortBStatus_Type()
)
excelRingPortBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelRingPortBStatus.setStatus("current")


class _ExcelRingSourcePacketID_Type(Integer32):
    """Custom type excelRingSourcePacketID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_ExcelRingSourcePacketID_Type.__name__ = "Integer32"
_ExcelRingSourcePacketID_Object = MibTableColumn
excelRingSourcePacketID = _ExcelRingSourcePacketID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 3, 2, 1, 9),
    _ExcelRingSourcePacketID_Type()
)
excelRingSourcePacketID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelRingSourcePacketID.setStatus("current")
_ExcelRingNodeStatus_ObjectIdentity = ObjectIdentity
excelRingNodeStatus = _ExcelRingNodeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4)
)


class _RingID_Type(Integer32):
    """Custom type ringID based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingID_Type.__name__ = "Integer32"
_RingID_Object = MibScalar
ringID = _RingID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4, 1),
    _RingID_Type()
)
ringID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringID.setStatus("current")
_RingStatusTable_Object = MibTable
ringStatusTable = _RingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ringStatusTable.setStatus("current")
_RingStatusTableEntry_Object = MibTableRow
ringStatusTableEntry = _RingStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4, 2, 1)
)
ringStatusTableEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "ringStatusIndex"),
)
if mibBuilder.loadTexts:
    ringStatusTableEntry.setStatus("current")


class _RingStatusIndex_Type(Integer32):
    """Custom type ringStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingStatusIndex_Type.__name__ = "Integer32"
_RingStatusIndex_Object = MibTableColumn
ringStatusIndex = _RingStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4, 2, 1, 1),
    _RingStatusIndex_Type()
)
ringStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ringStatusIndex.setStatus("current")


class _RingStatusTransmitting_Type(Integer32):
    """Custom type ringStatusTransmitting based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receiveAndTransmit", 2),
          ("receiveOnly", 1))
    )


_RingStatusTransmitting_Type.__name__ = "Integer32"
_RingStatusTransmitting_Object = MibTableColumn
ringStatusTransmitting = _RingStatusTransmitting_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4, 2, 1, 2),
    _RingStatusTransmitting_Type()
)
ringStatusTransmitting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStatusTransmitting.setStatus("current")
_RingStatusIpAddress_Type = IpAddress
_RingStatusIpAddress_Object = MibTableColumn
ringStatusIpAddress = _RingStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4, 2, 1, 3),
    _RingStatusIpAddress_Type()
)
ringStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStatusIpAddress.setStatus("current")


class _RingStatusLogicalId_Type(Integer32):
    """Custom type ringStatusLogicalId based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32655),
    )


_RingStatusLogicalId_Type.__name__ = "Integer32"
_RingStatusLogicalId_Object = MibTableColumn
ringStatusLogicalId = _RingStatusLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4, 2, 1, 4),
    _RingStatusLogicalId_Type()
)
ringStatusLogicalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStatusLogicalId.setStatus("current")


class _RingStatusPhysicalId_Type(Integer32):
    """Custom type ringStatusPhysicalId based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32655),
    )


_RingStatusPhysicalId_Type.__name__ = "Integer32"
_RingStatusPhysicalId_Object = MibTableColumn
ringStatusPhysicalId = _RingStatusPhysicalId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4, 2, 1, 5),
    _RingStatusPhysicalId_Type()
)
ringStatusPhysicalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStatusPhysicalId.setStatus("current")


class _RingStatusLoadMajorRev_Type(Integer32):
    """Custom type ringStatusLoadMajorRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingStatusLoadMajorRev_Type.__name__ = "Integer32"
_RingStatusLoadMajorRev_Object = MibTableColumn
ringStatusLoadMajorRev = _RingStatusLoadMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4, 2, 1, 6),
    _RingStatusLoadMajorRev_Type()
)
ringStatusLoadMajorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStatusLoadMajorRev.setStatus("current")


class _RingStatusLoadMinorRev_Type(Integer32):
    """Custom type ringStatusLoadMinorRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingStatusLoadMinorRev_Type.__name__ = "Integer32"
_RingStatusLoadMinorRev_Object = MibTableColumn
ringStatusLoadMinorRev = _RingStatusLoadMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4, 2, 1, 7),
    _RingStatusLoadMinorRev_Type()
)
ringStatusLoadMinorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStatusLoadMinorRev.setStatus("current")


class _RingStatusLoadBuildNum_Type(Integer32):
    """Custom type ringStatusLoadBuildNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingStatusLoadBuildNum_Type.__name__ = "Integer32"
_RingStatusLoadBuildNum_Object = MibTableColumn
ringStatusLoadBuildNum = _RingStatusLoadBuildNum_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 1, 4, 2, 1, 8),
    _RingStatusLoadBuildNum_Type()
)
ringStatusLoadBuildNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringStatusLoadBuildNum.setStatus("current")
_ExcelCommunicationSoftware_ObjectIdentity = ObjectIdentity
excelCommunicationSoftware = _ExcelCommunicationSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2)
)
_ExcelMatrix_ObjectIdentity = ObjectIdentity
excelMatrix = _ExcelMatrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1)
)
_ExcelMtxTable_Object = MibTable
excelMtxTable = _ExcelMtxTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    excelMtxTable.setStatus("current")
_ExcelMtxEntry_Object = MibTableRow
excelMtxEntry = _ExcelMtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1)
)
excelMtxEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelMtxSlotIndex"),
)
if mibBuilder.loadTexts:
    excelMtxEntry.setStatus("current")
_ExcelMtxSlotIndex_Type = SlotsInNode
_ExcelMtxSlotIndex_Object = MibTableColumn
excelMtxSlotIndex = _ExcelMtxSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 1),
    _ExcelMtxSlotIndex_Type()
)
excelMtxSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelMtxSlotIndex.setStatus("current")


class _ExcelMtxPosition_Type(Integer32):
    """Custom type excelMtxPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("left", 1),
          ("other", 3),
          ("right", 2))
    )


_ExcelMtxPosition_Type.__name__ = "Integer32"
_ExcelMtxPosition_Object = MibTableColumn
excelMtxPosition = _ExcelMtxPosition_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 2),
    _ExcelMtxPosition_Type()
)
excelMtxPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxPosition.setStatus("current")


class _ExcelMtxType_Type(Integer32):
    """Custom type excelMtxType based on Integer32"""
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
        *(("csn", 3),
          ("exnetConnect", 5),
          ("lnx", 4),
          ("other", 1),
          ("pcx", 2))
    )


_ExcelMtxType_Type.__name__ = "Integer32"
_ExcelMtxType_Object = MibTableColumn
excelMtxType = _ExcelMtxType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 3),
    _ExcelMtxType_Type()
)
excelMtxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxType.setStatus("current")


class _ExcelMtxState_Type(Integer32):
    """Custom type excelMtxState based on Integer32"""
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
        *(("active", 5),
          ("booting", 1),
          ("disabled", 7),
          ("initializing", 2),
          ("other", 6),
          ("standby", 3),
          ("switchOver", 4))
    )


_ExcelMtxState_Type.__name__ = "Integer32"
_ExcelMtxState_Object = MibTableColumn
excelMtxState = _ExcelMtxState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 4),
    _ExcelMtxState_Type()
)
excelMtxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxState.setStatus("current")


class _ExcelMtxAdjacentMatrixStatus_Type(Integer32):
    """Custom type excelMtxAdjacentMatrixStatus based on Integer32"""
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
        *(("adjacentMatrixDetectedHostComms", 4),
          ("adjacentMatrixDetectedNoHost", 3),
          ("adjacentMatrixDetectedNoIMC", 2),
          ("noAdjacentMatrixDetected", 1),
          ("other", 5))
    )


_ExcelMtxAdjacentMatrixStatus_Type.__name__ = "Integer32"
_ExcelMtxAdjacentMatrixStatus_Object = MibTableColumn
excelMtxAdjacentMatrixStatus = _ExcelMtxAdjacentMatrixStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 5),
    _ExcelMtxAdjacentMatrixStatus_Type()
)
excelMtxAdjacentMatrixStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxAdjacentMatrixStatus.setStatus("current")


class _ExcelMtxHostLink_Type(Integer32):
    """Custom type excelMtxHostLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1))
    )


_ExcelMtxHostLink_Type.__name__ = "Integer32"
_ExcelMtxHostLink_Object = MibTableColumn
excelMtxHostLink = _ExcelMtxHostLink_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 6),
    _ExcelMtxHostLink_Type()
)
excelMtxHostLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxHostLink.setStatus("current")


class _ExcelMtxRamLoadPresent_Type(Integer32):
    """Custom type excelMtxRamLoadPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ExcelMtxRamLoadPresent_Type.__name__ = "Integer32"
_ExcelMtxRamLoadPresent_Object = MibTableColumn
excelMtxRamLoadPresent = _ExcelMtxRamLoadPresent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 7),
    _ExcelMtxRamLoadPresent_Type()
)
excelMtxRamLoadPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxRamLoadPresent.setStatus("current")


class _ExcelMtxReadyForConfiguration_Type(Integer32):
    """Custom type excelMtxReadyForConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ExcelMtxReadyForConfiguration_Type.__name__ = "Integer32"
_ExcelMtxReadyForConfiguration_Object = MibTableColumn
excelMtxReadyForConfiguration = _ExcelMtxReadyForConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 8),
    _ExcelMtxReadyForConfiguration_Type()
)
excelMtxReadyForConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxReadyForConfiguration.setStatus("current")
_ExcelMtxIpAddress_Type = IpAddress
_ExcelMtxIpAddress_Object = MibTableColumn
excelMtxIpAddress = _ExcelMtxIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 9),
    _ExcelMtxIpAddress_Type()
)
excelMtxIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxIpAddress.setStatus("current")
_ExcelMtxBootMajorVersion_Type = DisplayString
_ExcelMtxBootMajorVersion_Object = MibTableColumn
excelMtxBootMajorVersion = _ExcelMtxBootMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 10),
    _ExcelMtxBootMajorVersion_Type()
)
excelMtxBootMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxBootMajorVersion.setStatus("current")
_ExcelMtxBootMinorVersion_Type = DisplayString
_ExcelMtxBootMinorVersion_Object = MibTableColumn
excelMtxBootMinorVersion = _ExcelMtxBootMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 11),
    _ExcelMtxBootMinorVersion_Type()
)
excelMtxBootMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxBootMinorVersion.setStatus("current")
_ExcelMtxSystemSoftwareMajor_Type = DisplayString
_ExcelMtxSystemSoftwareMajor_Object = MibTableColumn
excelMtxSystemSoftwareMajor = _ExcelMtxSystemSoftwareMajor_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 12),
    _ExcelMtxSystemSoftwareMajor_Type()
)
excelMtxSystemSoftwareMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxSystemSoftwareMajor.setStatus("current")
_ExcelMtxSystemSoftwareMinor_Type = DisplayString
_ExcelMtxSystemSoftwareMinor_Object = MibTableColumn
excelMtxSystemSoftwareMinor = _ExcelMtxSystemSoftwareMinor_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 13),
    _ExcelMtxSystemSoftwareMinor_Type()
)
excelMtxSystemSoftwareMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxSystemSoftwareMinor.setStatus("current")
_ExcelMtxSystemSoftwareBuild_Type = DisplayString
_ExcelMtxSystemSoftwareBuild_Object = MibTableColumn
excelMtxSystemSoftwareBuild = _ExcelMtxSystemSoftwareBuild_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 14),
    _ExcelMtxSystemSoftwareBuild_Type()
)
excelMtxSystemSoftwareBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxSystemSoftwareBuild.setStatus("current")
_ExcelMtxSecIpAddress_Type = IpAddress
_ExcelMtxSecIpAddress_Object = MibTableColumn
excelMtxSecIpAddress = _ExcelMtxSecIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 1, 1, 15),
    _ExcelMtxSecIpAddress_Type()
)
excelMtxSecIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMtxSecIpAddress.setStatus("current")
_ExcelMatrixManagement_ObjectIdentity = ObjectIdentity
excelMatrixManagement = _ExcelMatrixManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 2)
)


class _ExcelMatrixSwitchOver_Type(Integer32):
    """Custom type excelMatrixSwitchOver based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("switchOver", 2))
    )


_ExcelMatrixSwitchOver_Type.__name__ = "Integer32"
_ExcelMatrixSwitchOver_Object = MibScalar
excelMatrixSwitchOver = _ExcelMatrixSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 2, 1),
    _ExcelMatrixSwitchOver_Type()
)
excelMatrixSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelMatrixSwitchOver.setStatus("current")
_ExcelMatrixSwitchOverTime_Type = DisplayString
_ExcelMatrixSwitchOverTime_Object = MibScalar
excelMatrixSwitchOverTime = _ExcelMatrixSwitchOverTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 1, 2, 2),
    _ExcelMatrixSwitchOverTime_Type()
)
excelMatrixSwitchOverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMatrixSwitchOverTime.setStatus("current")
_ExcelExnetConnect_ObjectIdentity = ObjectIdentity
excelExnetConnect = _ExcelExnetConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 2)
)
_ExcelExnetConnectTable_Object = MibTable
excelExnetConnectTable = _ExcelExnetConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    excelExnetConnectTable.setStatus("current")
_ExcelExnetConnectEntry_Object = MibTableRow
excelExnetConnectEntry = _ExcelExnetConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 2, 1, 1)
)
excelExnetConnectEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelExnetConnectLogicalNodeIDIndex"),
)
if mibBuilder.loadTexts:
    excelExnetConnectEntry.setStatus("current")


class _ExcelExnetConnectLogicalNodeIDIndex_Type(Integer32):
    """Custom type excelExnetConnectLogicalNodeIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelExnetConnectLogicalNodeIDIndex_Type.__name__ = "Integer32"
_ExcelExnetConnectLogicalNodeIDIndex_Object = MibTableColumn
excelExnetConnectLogicalNodeIDIndex = _ExcelExnetConnectLogicalNodeIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 2, 1, 1, 1),
    _ExcelExnetConnectLogicalNodeIDIndex_Type()
)
excelExnetConnectLogicalNodeIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelExnetConnectLogicalNodeIDIndex.setStatus("current")


class _ExcelExnetConnectClockMaster_Type(Integer32):
    """Custom type excelExnetConnectClockMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ExcelExnetConnectClockMaster_Type.__name__ = "Integer32"
_ExcelExnetConnectClockMaster_Object = MibTableColumn
excelExnetConnectClockMaster = _ExcelExnetConnectClockMaster_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 2, 1, 1, 2),
    _ExcelExnetConnectClockMaster_Type()
)
excelExnetConnectClockMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelExnetConnectClockMaster.setStatus("current")


class _ExcelExnetConnectClockSpeed_Type(Integer32):
    """Custom type excelExnetConnectClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMHz", 1),
          ("twoMHz", 2))
    )


_ExcelExnetConnectClockSpeed_Type.__name__ = "Integer32"
_ExcelExnetConnectClockSpeed_Object = MibTableColumn
excelExnetConnectClockSpeed = _ExcelExnetConnectClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 2, 1, 1, 3),
    _ExcelExnetConnectClockSpeed_Type()
)
excelExnetConnectClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelExnetConnectClockSpeed.setStatus("current")
_ExcelSpans_ObjectIdentity = ObjectIdentity
excelSpans = _ExcelSpans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3)
)
_ExcelGeneralSpan_ObjectIdentity = ObjectIdentity
excelGeneralSpan = _ExcelGeneralSpan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 1)
)
_ExcelSpanTable_Object = MibTable
excelSpanTable = _ExcelSpanTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    excelSpanTable.setStatus("current")
_ExcelSpanEntry_Object = MibTableRow
excelSpanEntry = _ExcelSpanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 1, 1, 1)
)
excelSpanEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelCurrentNode"),
    (0, "EXCEL-SWITCH-MIB", "excelLogicalSpanId"),
)
if mibBuilder.loadTexts:
    excelSpanEntry.setStatus("current")


class _ExcelSpanTableIndex_Type(Integer32):
    """Custom type excelSpanTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelSpanTableIndex_Type.__name__ = "Integer32"
_ExcelSpanTableIndex_Object = MibTableColumn
excelSpanTableIndex = _ExcelSpanTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 1, 1, 1, 1),
    _ExcelSpanTableIndex_Type()
)
excelSpanTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelSpanTableIndex.setStatus("current")


class _ExcelLogicalSpanId_Type(Integer32):
    """Custom type excelLogicalSpanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelLogicalSpanId_Type.__name__ = "Integer32"
_ExcelLogicalSpanId_Object = MibTableColumn
excelLogicalSpanId = _ExcelLogicalSpanId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 1, 1, 1, 2),
    _ExcelLogicalSpanId_Type()
)
excelLogicalSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelLogicalSpanId.setStatus("current")
_ExcelSpanBipolarViolation_Type = Counter32
_ExcelSpanBipolarViolation_Object = MibTableColumn
excelSpanBipolarViolation = _ExcelSpanBipolarViolation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 1, 1, 1, 3),
    _ExcelSpanBipolarViolation_Type()
)
excelSpanBipolarViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSpanBipolarViolation.setStatus("current")
_ExcelSpanFrameErrors_Type = Counter32
_ExcelSpanFrameErrors_Object = MibTableColumn
excelSpanFrameErrors = _ExcelSpanFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 1, 1, 1, 4),
    _ExcelSpanFrameErrors_Type()
)
excelSpanFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSpanFrameErrors.setStatus("current")
_ExcelSpanSlipErrors_Type = Counter32
_ExcelSpanSlipErrors_Object = MibTableColumn
excelSpanSlipErrors = _ExcelSpanSlipErrors_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 1, 1, 1, 5),
    _ExcelSpanSlipErrors_Type()
)
excelSpanSlipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSpanSlipErrors.setStatus("current")
_ExcelSpanLossofFrame_Type = Counter32
_ExcelSpanLossofFrame_Object = MibTableColumn
excelSpanLossofFrame = _ExcelSpanLossofFrame_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 1, 1, 1, 6),
    _ExcelSpanLossofFrame_Type()
)
excelSpanLossofFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSpanLossofFrame.setStatus("current")
_ExcelSpanManagement_ObjectIdentity = ObjectIdentity
excelSpanManagement = _ExcelSpanManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 2)
)


class _ExcelCurrentSpanId_Type(Integer32):
    """Custom type excelCurrentSpanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelCurrentSpanId_Type.__name__ = "Integer32"
_ExcelCurrentSpanId_Object = MibScalar
excelCurrentSpanId = _ExcelCurrentSpanId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 2, 1),
    _ExcelCurrentSpanId_Type()
)
excelCurrentSpanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelCurrentSpanId.setStatus("current")


class _ExcelSpanAction_Type(Integer32):
    """Custom type excelSpanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_ExcelSpanAction_Type.__name__ = "Integer32"
_ExcelSpanAction_Object = MibScalar
excelSpanAction = _ExcelSpanAction_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 2, 2),
    _ExcelSpanAction_Type()
)
excelSpanAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelSpanAction.setStatus("current")


class _ExcelChannelAction_Type(Integer32):
    """Custom type excelChannelAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_ExcelChannelAction_Type.__name__ = "Integer32"
_ExcelChannelAction_Object = MibScalar
excelChannelAction = _ExcelChannelAction_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 3, 2, 3),
    _ExcelChannelAction_Type()
)
excelChannelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelChannelAction.setStatus("current")
_ExcelSS7_ObjectIdentity = ObjectIdentity
excelSS7 = _ExcelSS7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4)
)
_ExcelSS7Config_ObjectIdentity = ObjectIdentity
excelSS7Config = _ExcelSS7Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1)
)
_ExcelSS7CardTable_Object = MibTable
excelSS7CardTable = _ExcelSS7CardTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    excelSS7CardTable.setStatus("current")
_ExcelSS7CardEntry_Object = MibTableRow
excelSS7CardEntry = _ExcelSS7CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1, 1)
)
excelSS7CardEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelSS7CardSlotNumberIndex"),
)
if mibBuilder.loadTexts:
    excelSS7CardEntry.setStatus("current")


class _ExcelSS7CardSlotNumberIndex_Type(Integer32):
    """Custom type excelSS7CardSlotNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ExcelSS7CardSlotNumberIndex_Type.__name__ = "Integer32"
_ExcelSS7CardSlotNumberIndex_Object = MibTableColumn
excelSS7CardSlotNumberIndex = _ExcelSS7CardSlotNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1, 1, 1),
    _ExcelSS7CardSlotNumberIndex_Type()
)
excelSS7CardSlotNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelSS7CardSlotNumberIndex.setStatus("current")


class _ExcelSS7CardRedundancyConfiguredRole_Type(Integer32):
    """Custom type excelSS7CardRedundancyConfiguredRole based on Integer32"""
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
        *(("notConfigured", 3),
          ("primary", 1),
          ("secondary", 2),
          ("unknown", 4))
    )


_ExcelSS7CardRedundancyConfiguredRole_Type.__name__ = "Integer32"
_ExcelSS7CardRedundancyConfiguredRole_Object = MibTableColumn
excelSS7CardRedundancyConfiguredRole = _ExcelSS7CardRedundancyConfiguredRole_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1, 1, 2),
    _ExcelSS7CardRedundancyConfiguredRole_Type()
)
excelSS7CardRedundancyConfiguredRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7CardRedundancyConfiguredRole.setStatus("current")


class _ExcelSS7CardRedundancyCurrentRole_Type(Integer32):
    """Custom type excelSS7CardRedundancyCurrentRole based on Integer32"""
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
        *(("active", 1),
          ("notConfigured", 3),
          ("standby", 2),
          ("unknown", 4))
    )


_ExcelSS7CardRedundancyCurrentRole_Type.__name__ = "Integer32"
_ExcelSS7CardRedundancyCurrentRole_Object = MibTableColumn
excelSS7CardRedundancyCurrentRole = _ExcelSS7CardRedundancyCurrentRole_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1, 1, 3),
    _ExcelSS7CardRedundancyCurrentRole_Type()
)
excelSS7CardRedundancyCurrentRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7CardRedundancyCurrentRole.setStatus("current")


class _ExcelSS7CardRedundancyMate_Type(Integer32):
    """Custom type excelSS7CardRedundancyMate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7CardRedundancyMate_Type.__name__ = "Integer32"
_ExcelSS7CardRedundancyMate_Object = MibTableColumn
excelSS7CardRedundancyMate = _ExcelSS7CardRedundancyMate_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1, 1, 4),
    _ExcelSS7CardRedundancyMate_Type()
)
excelSS7CardRedundancyMate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7CardRedundancyMate.setStatus("current")


class _ExcelSS7CardRedundancyStatus_Type(Integer32):
    """Custom type excelSS7CardRedundancyStatus based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("bothCardsActive-PrimaryReceiveFromMatrix", 3),
          ("bothCardsActive-PrimarySendToMatrix", 4),
          ("dualInternalRedundancyFailure", 16),
          ("notConfigured", 18),
          ("primaryCardLinkFailureDuringSynchronization", 12),
          ("primaryCardLinkToMateFailureInStableState", 14),
          ("primaryCardOutOfService", 5),
          ("primaryCardResetDuringSynchronization", 10),
          ("redundancyDisabled", 9),
          ("redundantIOCardRemoved", 7),
          ("secondaryCardLinkFailureDuringSynchronization", 13),
          ("secondaryCardLinkToMateFailureInStableState", 15),
          ("secondaryCardOutOfService", 6),
          ("secondaryCardResetDuringSynchronization", 11),
          ("synchronizationTimeOut", 8),
          ("synchronizing-PrimaryReceiveFromMatrix", 1),
          ("synchronizing-PrimarySendToMatrix", 2),
          ("unknown", 17))
    )


_ExcelSS7CardRedundancyStatus_Type.__name__ = "Integer32"
_ExcelSS7CardRedundancyStatus_Object = MibTableColumn
excelSS7CardRedundancyStatus = _ExcelSS7CardRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1, 1, 5),
    _ExcelSS7CardRedundancyStatus_Type()
)
excelSS7CardRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7CardRedundancyStatus.setStatus("current")


class _ExcelSS7CardStackID1_Type(Integer32):
    """Custom type excelSS7CardStackID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7CardStackID1_Type.__name__ = "Integer32"
_ExcelSS7CardStackID1_Object = MibTableColumn
excelSS7CardStackID1 = _ExcelSS7CardStackID1_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1, 1, 6),
    _ExcelSS7CardStackID1_Type()
)
excelSS7CardStackID1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7CardStackID1.setStatus("current")


class _ExcelSS7CardStackID2_Type(Integer32):
    """Custom type excelSS7CardStackID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7CardStackID2_Type.__name__ = "Integer32"
_ExcelSS7CardStackID2_Object = MibTableColumn
excelSS7CardStackID2 = _ExcelSS7CardStackID2_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1, 1, 7),
    _ExcelSS7CardStackID2_Type()
)
excelSS7CardStackID2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7CardStackID2.setStatus("current")


class _ExcelSS7CardStackID3_Type(Integer32):
    """Custom type excelSS7CardStackID3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7CardStackID3_Type.__name__ = "Integer32"
_ExcelSS7CardStackID3_Object = MibTableColumn
excelSS7CardStackID3 = _ExcelSS7CardStackID3_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1, 1, 8),
    _ExcelSS7CardStackID3_Type()
)
excelSS7CardStackID3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7CardStackID3.setStatus("current")


class _ExcelSS7CardStackID4_Type(Integer32):
    """Custom type excelSS7CardStackID4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7CardStackID4_Type.__name__ = "Integer32"
_ExcelSS7CardStackID4_Object = MibTableColumn
excelSS7CardStackID4 = _ExcelSS7CardStackID4_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1, 1, 9),
    _ExcelSS7CardStackID4_Type()
)
excelSS7CardStackID4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7CardStackID4.setStatus("current")


class _ExcelSS7CardMaximumLinks_Type(Integer32):
    """Custom type excelSS7CardMaximumLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7CardMaximumLinks_Type.__name__ = "Integer32"
_ExcelSS7CardMaximumLinks_Object = MibTableColumn
excelSS7CardMaximumLinks = _ExcelSS7CardMaximumLinks_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 1, 1, 10),
    _ExcelSS7CardMaximumLinks_Type()
)
excelSS7CardMaximumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7CardMaximumLinks.setStatus("current")
_ExcelSS7ConfigLinkTable_Object = MibTable
excelSS7ConfigLinkTable = _ExcelSS7ConfigLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    excelSS7ConfigLinkTable.setStatus("current")
_ExcelSS7LinkEntry_Object = MibTableRow
excelSS7LinkEntry = _ExcelSS7LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 2, 1)
)
excelSS7LinkEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelSS7LinkStackIndex"),
    (0, "EXCEL-SWITCH-MIB", "excelSS7LinkLinkIndex"),
    (0, "EXCEL-SWITCH-MIB", "excelSS7LinkLinkSetIndex"),
)
if mibBuilder.loadTexts:
    excelSS7LinkEntry.setStatus("current")


class _ExcelSS7LinkStackIndex_Type(Integer32):
    """Custom type excelSS7LinkStackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7LinkStackIndex_Type.__name__ = "Integer32"
_ExcelSS7LinkStackIndex_Object = MibTableColumn
excelSS7LinkStackIndex = _ExcelSS7LinkStackIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 2, 1, 1),
    _ExcelSS7LinkStackIndex_Type()
)
excelSS7LinkStackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelSS7LinkStackIndex.setStatus("current")


class _ExcelSS7LinkLinkIndex_Type(Integer32):
    """Custom type excelSS7LinkLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7LinkLinkIndex_Type.__name__ = "Integer32"
_ExcelSS7LinkLinkIndex_Object = MibTableColumn
excelSS7LinkLinkIndex = _ExcelSS7LinkLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 2, 1, 2),
    _ExcelSS7LinkLinkIndex_Type()
)
excelSS7LinkLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelSS7LinkLinkIndex.setStatus("current")


class _ExcelSS7LinkLinkSetIndex_Type(Integer32):
    """Custom type excelSS7LinkLinkSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7LinkLinkSetIndex_Type.__name__ = "Integer32"
_ExcelSS7LinkLinkSetIndex_Object = MibTableColumn
excelSS7LinkLinkSetIndex = _ExcelSS7LinkLinkSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 2, 1, 3),
    _ExcelSS7LinkLinkSetIndex_Type()
)
excelSS7LinkLinkSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelSS7LinkLinkSetIndex.setStatus("current")


class _ExcelSS7LinkStatus_Type(Integer32):
    """Custom type excelSS7LinkStatus based on Integer32"""
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
        *(("available", 1),
          ("failed", 2),
          ("inhibitLocally", 3),
          ("inhibitRemotely", 4),
          ("remoteBlocked", 5),
          ("reserved5", 6),
          ("reserved6", 7),
          ("reserved7", 8),
          ("unknown", 9))
    )


_ExcelSS7LinkStatus_Type.__name__ = "Integer32"
_ExcelSS7LinkStatus_Object = MibTableColumn
excelSS7LinkStatus = _ExcelSS7LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 2, 1, 4),
    _ExcelSS7LinkStatus_Type()
)
excelSS7LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7LinkStatus.setStatus("current")


class _ExcelSS7LinkSignalingLinkCode_Type(Integer32):
    """Custom type excelSS7LinkSignalingLinkCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ExcelSS7LinkSignalingLinkCode_Type.__name__ = "Integer32"
_ExcelSS7LinkSignalingLinkCode_Object = MibTableColumn
excelSS7LinkSignalingLinkCode = _ExcelSS7LinkSignalingLinkCode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 2, 1, 5),
    _ExcelSS7LinkSignalingLinkCode_Type()
)
excelSS7LinkSignalingLinkCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7LinkSignalingLinkCode.setStatus("current")


class _ExcelSS7LinkDataRate_Type(Integer32):
    """Custom type excelSS7LinkDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataRate56kbps", 2),
          ("dataRate64kbps", 1))
    )


_ExcelSS7LinkDataRate_Type.__name__ = "Integer32"
_ExcelSS7LinkDataRate_Object = MibTableColumn
excelSS7LinkDataRate = _ExcelSS7LinkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 2, 1, 6),
    _ExcelSS7LinkDataRate_Type()
)
excelSS7LinkDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7LinkDataRate.setStatus("current")


class _ExcelSS7LinkLogicalSpanID_Type(Integer32):
    """Custom type excelSS7LinkLogicalSpanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7LinkLogicalSpanID_Type.__name__ = "Integer32"
_ExcelSS7LinkLogicalSpanID_Object = MibTableColumn
excelSS7LinkLogicalSpanID = _ExcelSS7LinkLogicalSpanID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 2, 1, 7),
    _ExcelSS7LinkLogicalSpanID_Type()
)
excelSS7LinkLogicalSpanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7LinkLogicalSpanID.setStatus("current")


class _ExcelSS7Linkchannel_Type(Integer32):
    """Custom type excelSS7Linkchannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_ExcelSS7Linkchannel_Type.__name__ = "Integer32"
_ExcelSS7Linkchannel_Object = MibTableColumn
excelSS7Linkchannel = _ExcelSS7Linkchannel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 2, 1, 8),
    _ExcelSS7Linkchannel_Type()
)
excelSS7Linkchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7Linkchannel.setStatus("current")
_ExcelSS7StackTable_Object = MibTable
excelSS7StackTable = _ExcelSS7StackTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    excelSS7StackTable.setStatus("current")
_ExcelSS7StackEntry_Object = MibTableRow
excelSS7StackEntry = _ExcelSS7StackEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 3, 1)
)
excelSS7StackEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelSS7StackIDIndex"),
)
if mibBuilder.loadTexts:
    excelSS7StackEntry.setStatus("current")


class _ExcelSS7StackIDIndex_Type(Integer32):
    """Custom type excelSS7StackIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7StackIDIndex_Type.__name__ = "Integer32"
_ExcelSS7StackIDIndex_Object = MibTableColumn
excelSS7StackIDIndex = _ExcelSS7StackIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 3, 1, 1),
    _ExcelSS7StackIDIndex_Type()
)
excelSS7StackIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelSS7StackIDIndex.setStatus("current")
_ExcelSS7StackOPC_Type = DisplayString
_ExcelSS7StackOPC_Object = MibTableColumn
excelSS7StackOPC = _ExcelSS7StackOPC_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 3, 1, 2),
    _ExcelSS7StackOPC_Type()
)
excelSS7StackOPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7StackOPC.setStatus("current")
_ExcelSS7StackMTPVariant_Type = SS7VariantsTypes
_ExcelSS7StackMTPVariant_Object = MibTableColumn
excelSS7StackMTPVariant = _ExcelSS7StackMTPVariant_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 3, 1, 3),
    _ExcelSS7StackMTPVariant_Type()
)
excelSS7StackMTPVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7StackMTPVariant.setStatus("current")
_ExcelSS7StackISUPVariant_Type = SS7VariantsTypes
_ExcelSS7StackISUPVariant_Object = MibTableColumn
excelSS7StackISUPVariant = _ExcelSS7StackISUPVariant_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 3, 1, 4),
    _ExcelSS7StackISUPVariant_Type()
)
excelSS7StackISUPVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7StackISUPVariant.setStatus("current")
_ExcelSS7StackL3PVariant_Type = SS7VariantsTypes
_ExcelSS7StackL3PVariant_Object = MibTableColumn
excelSS7StackL3PVariant = _ExcelSS7StackL3PVariant_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 3, 1, 5),
    _ExcelSS7StackL3PVariant_Type()
)
excelSS7StackL3PVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7StackL3PVariant.setStatus("current")
_ExcelSS7StackTUPVariant_Type = SS7VariantsTypes
_ExcelSS7StackTUPVariant_Object = MibTableColumn
excelSS7StackTUPVariant = _ExcelSS7StackTUPVariant_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 3, 1, 6),
    _ExcelSS7StackTUPVariant_Type()
)
excelSS7StackTUPVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7StackTUPVariant.setStatus("current")
_ExcelSS7StackL3PTUPVariant_Type = SS7VariantsTypes
_ExcelSS7StackL3PTUPVariant_Object = MibTableColumn
excelSS7StackL3PTUPVariant = _ExcelSS7StackL3PTUPVariant_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 3, 1, 7),
    _ExcelSS7StackL3PTUPVariant_Type()
)
excelSS7StackL3PTUPVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7StackL3PTUPVariant.setStatus("current")
_ExcelSS7LinkSetTable_Object = MibTable
excelSS7LinkSetTable = _ExcelSS7LinkSetTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    excelSS7LinkSetTable.setStatus("current")
_ExcelSS7LinkSetEntry_Object = MibTableRow
excelSS7LinkSetEntry = _ExcelSS7LinkSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 4, 1)
)
excelSS7LinkSetEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelSS7LinkSetIDIndex"),
    (0, "EXCEL-SWITCH-MIB", "excelSS7LinkSetStackIDIndex"),
)
if mibBuilder.loadTexts:
    excelSS7LinkSetEntry.setStatus("current")


class _ExcelSS7LinkSetIDIndex_Type(Integer32):
    """Custom type excelSS7LinkSetIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelSS7LinkSetIDIndex_Type.__name__ = "Integer32"
_ExcelSS7LinkSetIDIndex_Object = MibTableColumn
excelSS7LinkSetIDIndex = _ExcelSS7LinkSetIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 4, 1, 1),
    _ExcelSS7LinkSetIDIndex_Type()
)
excelSS7LinkSetIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelSS7LinkSetIDIndex.setStatus("current")


class _ExcelSS7LinkSetStatus_Type(Integer32):
    """Custom type excelSS7LinkSetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2),
          ("unknown", 3))
    )


_ExcelSS7LinkSetStatus_Type.__name__ = "Integer32"
_ExcelSS7LinkSetStatus_Object = MibTableColumn
excelSS7LinkSetStatus = _ExcelSS7LinkSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 4, 1, 2),
    _ExcelSS7LinkSetStatus_Type()
)
excelSS7LinkSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7LinkSetStatus.setStatus("current")
_ExcelSS7LinkSetAPC_Type = DisplayString
_ExcelSS7LinkSetAPC_Object = MibTableColumn
excelSS7LinkSetAPC = _ExcelSS7LinkSetAPC_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 4, 1, 3),
    _ExcelSS7LinkSetAPC_Type()
)
excelSS7LinkSetAPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7LinkSetAPC.setStatus("current")


class _ExcelSS7LinkSetStackIDIndex_Type(Integer32):
    """Custom type excelSS7LinkSetStackIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ExcelSS7LinkSetStackIDIndex_Type.__name__ = "Integer32"
_ExcelSS7LinkSetStackIDIndex_Object = MibTableColumn
excelSS7LinkSetStackIDIndex = _ExcelSS7LinkSetStackIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 1, 4, 1, 4),
    _ExcelSS7LinkSetStackIDIndex_Type()
)
excelSS7LinkSetStackIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelSS7LinkSetStackIDIndex.setStatus("current")
_ExcelSS7Statistics_ObjectIdentity = ObjectIdentity
excelSS7Statistics = _ExcelSS7Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 4, 2)
)
_ExcelPPL_ObjectIdentity = ObjectIdentity
excelPPL = _ExcelPPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5)
)


class _ExcelPPLComponentId_Type(Integer32):
    """Custom type excelPPLComponentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExcelPPLComponentId_Type.__name__ = "Integer32"
_ExcelPPLComponentId_Object = MibScalar
excelPPLComponentId = _ExcelPPLComponentId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 1),
    _ExcelPPLComponentId_Type()
)
excelPPLComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelPPLComponentId.setStatus("current")
_ExcelPPLComponentStatistics_ObjectIdentity = ObjectIdentity
excelPPLComponentStatistics = _ExcelPPLComponentStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2)
)
_ExcelL3PCICTable_Object = MibTable
excelL3PCICTable = _ExcelL3PCICTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    excelL3PCICTable.setStatus("current")
_ExcelL3PCICEntry_Object = MibTableRow
excelL3PCICEntry = _ExcelL3PCICEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 1, 1)
)
excelL3PCICEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelL3PCICSpanID"),
    (0, "EXCEL-SWITCH-MIB", "excelL3PCICChannelID"),
    (0, "EXCEL-SWITCH-MIB", "excelL3PCICEventID"),
)
if mibBuilder.loadTexts:
    excelL3PCICEntry.setStatus("current")


class _ExcelL3PCICIndex_Type(Integer32):
    """Custom type excelL3PCICIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExcelL3PCICIndex_Type.__name__ = "Integer32"
_ExcelL3PCICIndex_Object = MibTableColumn
excelL3PCICIndex = _ExcelL3PCICIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 1, 1, 1),
    _ExcelL3PCICIndex_Type()
)
excelL3PCICIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelL3PCICIndex.setStatus("current")


class _ExcelL3PCICSpanID_Type(Integer32):
    """Custom type excelL3PCICSpanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelL3PCICSpanID_Type.__name__ = "Integer32"
_ExcelL3PCICSpanID_Object = MibTableColumn
excelL3PCICSpanID = _ExcelL3PCICSpanID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 1, 1, 2),
    _ExcelL3PCICSpanID_Type()
)
excelL3PCICSpanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PCICSpanID.setStatus("current")


class _ExcelL3PCICChannelID_Type(Integer32):
    """Custom type excelL3PCICChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ExcelL3PCICChannelID_Type.__name__ = "Integer32"
_ExcelL3PCICChannelID_Object = MibTableColumn
excelL3PCICChannelID = _ExcelL3PCICChannelID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 1, 1, 3),
    _ExcelL3PCICChannelID_Type()
)
excelL3PCICChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PCICChannelID.setStatus("current")


class _ExcelL3PCICEventID_Type(Integer32):
    """Custom type excelL3PCICEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExcelL3PCICEventID_Type.__name__ = "Integer32"
_ExcelL3PCICEventID_Object = MibTableColumn
excelL3PCICEventID = _ExcelL3PCICEventID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 1, 1, 4),
    _ExcelL3PCICEventID_Type()
)
excelL3PCICEventID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PCICEventID.setStatus("current")
_ExcelL3PCICTime_Type = DisplayString
_ExcelL3PCICTime_Object = MibTableColumn
excelL3PCICTime = _ExcelL3PCICTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 1, 1, 5),
    _ExcelL3PCICTime_Type()
)
excelL3PCICTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PCICTime.setStatus("current")


class _ExcelL3PCICCount_Type(Integer32):
    """Custom type excelL3PCICCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32656),
    )


_ExcelL3PCICCount_Type.__name__ = "Integer32"
_ExcelL3PCICCount_Object = MibTableColumn
excelL3PCICCount = _ExcelL3PCICCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 1, 1, 6),
    _ExcelL3PCICCount_Type()
)
excelL3PCICCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PCICCount.setStatus("current")
_ExcelL3PCICStatus_Type = RowStatus
_ExcelL3PCICStatus_Object = MibTableColumn
excelL3PCICStatus = _ExcelL3PCICStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 1, 1, 7),
    _ExcelL3PCICStatus_Type()
)
excelL3PCICStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PCICStatus.setStatus("current")
_ExcelL3PLinkTable_Object = MibTable
excelL3PLinkTable = _ExcelL3PLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    excelL3PLinkTable.setStatus("current")
_ExcelL3PLinkEntry_Object = MibTableRow
excelL3PLinkEntry = _ExcelL3PLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 2, 1)
)
excelL3PLinkEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelL3PLinkSpanID"),
    (0, "EXCEL-SWITCH-MIB", "excelL3PLinkChannelID"),
    (0, "EXCEL-SWITCH-MIB", "excelL3PLinkEventID"),
)
if mibBuilder.loadTexts:
    excelL3PLinkEntry.setStatus("current")


class _ExcelL3PLinkIndex_Type(Integer32):
    """Custom type excelL3PLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExcelL3PLinkIndex_Type.__name__ = "Integer32"
_ExcelL3PLinkIndex_Object = MibTableColumn
excelL3PLinkIndex = _ExcelL3PLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 2, 1, 1),
    _ExcelL3PLinkIndex_Type()
)
excelL3PLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelL3PLinkIndex.setStatus("current")


class _ExcelL3PLinkSpanID_Type(Integer32):
    """Custom type excelL3PLinkSpanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelL3PLinkSpanID_Type.__name__ = "Integer32"
_ExcelL3PLinkSpanID_Object = MibTableColumn
excelL3PLinkSpanID = _ExcelL3PLinkSpanID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 2, 1, 2),
    _ExcelL3PLinkSpanID_Type()
)
excelL3PLinkSpanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PLinkSpanID.setStatus("current")


class _ExcelL3PLinkChannelID_Type(Integer32):
    """Custom type excelL3PLinkChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ExcelL3PLinkChannelID_Type.__name__ = "Integer32"
_ExcelL3PLinkChannelID_Object = MibTableColumn
excelL3PLinkChannelID = _ExcelL3PLinkChannelID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 2, 1, 3),
    _ExcelL3PLinkChannelID_Type()
)
excelL3PLinkChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PLinkChannelID.setStatus("current")


class _ExcelL3PLinkEventID_Type(Integer32):
    """Custom type excelL3PLinkEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExcelL3PLinkEventID_Type.__name__ = "Integer32"
_ExcelL3PLinkEventID_Object = MibTableColumn
excelL3PLinkEventID = _ExcelL3PLinkEventID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 2, 1, 4),
    _ExcelL3PLinkEventID_Type()
)
excelL3PLinkEventID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PLinkEventID.setStatus("current")
_ExcelL3PLinkTime_Type = DisplayString
_ExcelL3PLinkTime_Object = MibTableColumn
excelL3PLinkTime = _ExcelL3PLinkTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 2, 1, 5),
    _ExcelL3PLinkTime_Type()
)
excelL3PLinkTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PLinkTime.setStatus("current")


class _ExcelL3PLinkCount_Type(Integer32):
    """Custom type excelL3PLinkCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32656),
    )


_ExcelL3PLinkCount_Type.__name__ = "Integer32"
_ExcelL3PLinkCount_Object = MibTableColumn
excelL3PLinkCount = _ExcelL3PLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 2, 1, 6),
    _ExcelL3PLinkCount_Type()
)
excelL3PLinkCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PLinkCount.setStatus("current")
_ExcelL3PLinkStatus_Type = RowStatus
_ExcelL3PLinkStatus_Object = MibTableColumn
excelL3PLinkStatus = _ExcelL3PLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 2, 1, 7),
    _ExcelL3PLinkStatus_Type()
)
excelL3PLinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelL3PLinkStatus.setStatus("current")
_ExcelCPCTable_Object = MibTable
excelCPCTable = _ExcelCPCTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 3)
)
if mibBuilder.loadTexts:
    excelCPCTable.setStatus("current")
_ExcelCPCEntry_Object = MibTableRow
excelCPCEntry = _ExcelCPCEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 3, 1)
)
excelCPCEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelCPCSpanID"),
    (0, "EXCEL-SWITCH-MIB", "excelCPCChannelID"),
    (0, "EXCEL-SWITCH-MIB", "excelCPCEventID"),
)
if mibBuilder.loadTexts:
    excelCPCEntry.setStatus("current")


class _ExcelCPCIndex_Type(Integer32):
    """Custom type excelCPCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExcelCPCIndex_Type.__name__ = "Integer32"
_ExcelCPCIndex_Object = MibTableColumn
excelCPCIndex = _ExcelCPCIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 3, 1, 1),
    _ExcelCPCIndex_Type()
)
excelCPCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelCPCIndex.setStatus("current")


class _ExcelCPCSpanID_Type(Integer32):
    """Custom type excelCPCSpanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelCPCSpanID_Type.__name__ = "Integer32"
_ExcelCPCSpanID_Object = MibTableColumn
excelCPCSpanID = _ExcelCPCSpanID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 3, 1, 2),
    _ExcelCPCSpanID_Type()
)
excelCPCSpanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCPCSpanID.setStatus("current")


class _ExcelCPCChannelID_Type(Integer32):
    """Custom type excelCPCChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ExcelCPCChannelID_Type.__name__ = "Integer32"
_ExcelCPCChannelID_Object = MibTableColumn
excelCPCChannelID = _ExcelCPCChannelID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 3, 1, 3),
    _ExcelCPCChannelID_Type()
)
excelCPCChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCPCChannelID.setStatus("current")


class _ExcelCPCEventID_Type(Integer32):
    """Custom type excelCPCEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExcelCPCEventID_Type.__name__ = "Integer32"
_ExcelCPCEventID_Object = MibTableColumn
excelCPCEventID = _ExcelCPCEventID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 3, 1, 4),
    _ExcelCPCEventID_Type()
)
excelCPCEventID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCPCEventID.setStatus("current")
_ExcelCPCTime_Type = DisplayString
_ExcelCPCTime_Object = MibTableColumn
excelCPCTime = _ExcelCPCTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 3, 1, 5),
    _ExcelCPCTime_Type()
)
excelCPCTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCPCTime.setStatus("current")


class _ExcelCPCCount_Type(Integer32):
    """Custom type excelCPCCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32656),
    )


_ExcelCPCCount_Type.__name__ = "Integer32"
_ExcelCPCCount_Object = MibTableColumn
excelCPCCount = _ExcelCPCCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 3, 1, 6),
    _ExcelCPCCount_Type()
)
excelCPCCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCPCCount.setStatus("current")
_ExcelCPCStatus_Type = RowStatus
_ExcelCPCStatus_Object = MibTableColumn
excelCPCStatus = _ExcelCPCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 3, 1, 7),
    _ExcelCPCStatus_Type()
)
excelCPCStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCPCStatus.setStatus("current")
_ExcelSPRCTable_Object = MibTable
excelSPRCTable = _ExcelSPRCTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 4)
)
if mibBuilder.loadTexts:
    excelSPRCTable.setStatus("current")
_ExcelSPRCEntry_Object = MibTableRow
excelSPRCEntry = _ExcelSPRCEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 4, 1)
)
excelSPRCEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelSPRCSpanID"),
    (0, "EXCEL-SWITCH-MIB", "excelSPRCChannelID"),
    (0, "EXCEL-SWITCH-MIB", "excelSPRCEventID"),
)
if mibBuilder.loadTexts:
    excelSPRCEntry.setStatus("current")


class _ExcelSPRCIndex_Type(Integer32):
    """Custom type excelSPRCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExcelSPRCIndex_Type.__name__ = "Integer32"
_ExcelSPRCIndex_Object = MibTableColumn
excelSPRCIndex = _ExcelSPRCIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 4, 1, 1),
    _ExcelSPRCIndex_Type()
)
excelSPRCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelSPRCIndex.setStatus("current")


class _ExcelSPRCSpanID_Type(Integer32):
    """Custom type excelSPRCSpanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelSPRCSpanID_Type.__name__ = "Integer32"
_ExcelSPRCSpanID_Object = MibTableColumn
excelSPRCSpanID = _ExcelSPRCSpanID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 4, 1, 2),
    _ExcelSPRCSpanID_Type()
)
excelSPRCSpanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelSPRCSpanID.setStatus("current")


class _ExcelSPRCChannelID_Type(Integer32):
    """Custom type excelSPRCChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ExcelSPRCChannelID_Type.__name__ = "Integer32"
_ExcelSPRCChannelID_Object = MibTableColumn
excelSPRCChannelID = _ExcelSPRCChannelID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 4, 1, 3),
    _ExcelSPRCChannelID_Type()
)
excelSPRCChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelSPRCChannelID.setStatus("current")


class _ExcelSPRCEventID_Type(Integer32):
    """Custom type excelSPRCEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExcelSPRCEventID_Type.__name__ = "Integer32"
_ExcelSPRCEventID_Object = MibTableColumn
excelSPRCEventID = _ExcelSPRCEventID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 4, 1, 4),
    _ExcelSPRCEventID_Type()
)
excelSPRCEventID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelSPRCEventID.setStatus("current")
_ExcelSPRCTime_Type = DisplayString
_ExcelSPRCTime_Object = MibTableColumn
excelSPRCTime = _ExcelSPRCTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 4, 1, 5),
    _ExcelSPRCTime_Type()
)
excelSPRCTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelSPRCTime.setStatus("current")


class _ExcelSPRCCount_Type(Integer32):
    """Custom type excelSPRCCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32656),
    )


_ExcelSPRCCount_Type.__name__ = "Integer32"
_ExcelSPRCCount_Object = MibTableColumn
excelSPRCCount = _ExcelSPRCCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 4, 1, 6),
    _ExcelSPRCCount_Type()
)
excelSPRCCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelSPRCCount.setStatus("current")
_ExcelSPRCStatus_Type = RowStatus
_ExcelSPRCStatus_Object = MibTableColumn
excelSPRCStatus = _ExcelSPRCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 4, 1, 7),
    _ExcelSPRCStatus_Type()
)
excelSPRCStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelSPRCStatus.setStatus("current")
_ExcelUCICTable_Object = MibTable
excelUCICTable = _ExcelUCICTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 5)
)
if mibBuilder.loadTexts:
    excelUCICTable.setStatus("current")
_ExcelUCICEntry_Object = MibTableRow
excelUCICEntry = _ExcelUCICEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 5, 1)
)
excelUCICEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelUCICSpanID"),
    (0, "EXCEL-SWITCH-MIB", "excelUCICChannelID"),
    (0, "EXCEL-SWITCH-MIB", "excelUCICEventID"),
)
if mibBuilder.loadTexts:
    excelUCICEntry.setStatus("current")


class _ExcelUCICIndex_Type(Integer32):
    """Custom type excelUCICIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExcelUCICIndex_Type.__name__ = "Integer32"
_ExcelUCICIndex_Object = MibTableColumn
excelUCICIndex = _ExcelUCICIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 5, 1, 1),
    _ExcelUCICIndex_Type()
)
excelUCICIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelUCICIndex.setStatus("current")


class _ExcelUCICSpanID_Type(Integer32):
    """Custom type excelUCICSpanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelUCICSpanID_Type.__name__ = "Integer32"
_ExcelUCICSpanID_Object = MibTableColumn
excelUCICSpanID = _ExcelUCICSpanID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 5, 1, 2),
    _ExcelUCICSpanID_Type()
)
excelUCICSpanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelUCICSpanID.setStatus("current")


class _ExcelUCICChannelID_Type(Integer32):
    """Custom type excelUCICChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ExcelUCICChannelID_Type.__name__ = "Integer32"
_ExcelUCICChannelID_Object = MibTableColumn
excelUCICChannelID = _ExcelUCICChannelID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 5, 1, 3),
    _ExcelUCICChannelID_Type()
)
excelUCICChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelUCICChannelID.setStatus("current")


class _ExcelUCICEventID_Type(Integer32):
    """Custom type excelUCICEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExcelUCICEventID_Type.__name__ = "Integer32"
_ExcelUCICEventID_Object = MibTableColumn
excelUCICEventID = _ExcelUCICEventID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 5, 1, 4),
    _ExcelUCICEventID_Type()
)
excelUCICEventID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelUCICEventID.setStatus("current")
_ExcelUCICTime_Type = DisplayString
_ExcelUCICTime_Object = MibTableColumn
excelUCICTime = _ExcelUCICTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 5, 1, 5),
    _ExcelUCICTime_Type()
)
excelUCICTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelUCICTime.setStatus("current")


class _ExcelUCICCount_Type(Integer32):
    """Custom type excelUCICCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32656),
    )


_ExcelUCICCount_Type.__name__ = "Integer32"
_ExcelUCICCount_Object = MibTableColumn
excelUCICCount = _ExcelUCICCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 5, 1, 6),
    _ExcelUCICCount_Type()
)
excelUCICCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelUCICCount.setStatus("current")
_ExcelUCICStatus_Type = RowStatus
_ExcelUCICStatus_Object = MibTableColumn
excelUCICStatus = _ExcelUCICStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 5, 1, 7),
    _ExcelUCICStatus_Type()
)
excelUCICStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelUCICStatus.setStatus("current")
_ExcelHMDTTable_Object = MibTable
excelHMDTTable = _ExcelHMDTTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 6)
)
if mibBuilder.loadTexts:
    excelHMDTTable.setStatus("current")
_ExcelHMDTEntry_Object = MibTableRow
excelHMDTEntry = _ExcelHMDTEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 6, 1)
)
excelHMDTEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelHMDTSpanID"),
    (0, "EXCEL-SWITCH-MIB", "excelHMDTChannelID"),
    (0, "EXCEL-SWITCH-MIB", "excelHMDTEventID"),
)
if mibBuilder.loadTexts:
    excelHMDTEntry.setStatus("current")


class _ExcelHMDTIndex_Type(Integer32):
    """Custom type excelHMDTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExcelHMDTIndex_Type.__name__ = "Integer32"
_ExcelHMDTIndex_Object = MibTableColumn
excelHMDTIndex = _ExcelHMDTIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 6, 1, 1),
    _ExcelHMDTIndex_Type()
)
excelHMDTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelHMDTIndex.setStatus("current")


class _ExcelHMDTSpanID_Type(Integer32):
    """Custom type excelHMDTSpanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelHMDTSpanID_Type.__name__ = "Integer32"
_ExcelHMDTSpanID_Object = MibTableColumn
excelHMDTSpanID = _ExcelHMDTSpanID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 6, 1, 2),
    _ExcelHMDTSpanID_Type()
)
excelHMDTSpanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelHMDTSpanID.setStatus("current")


class _ExcelHMDTChannelID_Type(Integer32):
    """Custom type excelHMDTChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ExcelHMDTChannelID_Type.__name__ = "Integer32"
_ExcelHMDTChannelID_Object = MibTableColumn
excelHMDTChannelID = _ExcelHMDTChannelID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 6, 1, 3),
    _ExcelHMDTChannelID_Type()
)
excelHMDTChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelHMDTChannelID.setStatus("current")


class _ExcelHMDTEventID_Type(Integer32):
    """Custom type excelHMDTEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExcelHMDTEventID_Type.__name__ = "Integer32"
_ExcelHMDTEventID_Object = MibTableColumn
excelHMDTEventID = _ExcelHMDTEventID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 6, 1, 4),
    _ExcelHMDTEventID_Type()
)
excelHMDTEventID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelHMDTEventID.setStatus("current")
_ExcelHMDTTime_Type = DisplayString
_ExcelHMDTTime_Object = MibTableColumn
excelHMDTTime = _ExcelHMDTTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 6, 1, 5),
    _ExcelHMDTTime_Type()
)
excelHMDTTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelHMDTTime.setStatus("current")


class _ExcelHMDTCount_Type(Integer32):
    """Custom type excelHMDTCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32656),
    )


_ExcelHMDTCount_Type.__name__ = "Integer32"
_ExcelHMDTCount_Object = MibTableColumn
excelHMDTCount = _ExcelHMDTCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 6, 1, 6),
    _ExcelHMDTCount_Type()
)
excelHMDTCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelHMDTCount.setStatus("current")
_ExcelHMDTStatus_Type = RowStatus
_ExcelHMDTStatus_Object = MibTableColumn
excelHMDTStatus = _ExcelHMDTStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 6, 1, 7),
    _ExcelHMDTStatus_Type()
)
excelHMDTStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelHMDTStatus.setStatus("current")
_ExcelLSACTable_Object = MibTable
excelLSACTable = _ExcelLSACTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 7)
)
if mibBuilder.loadTexts:
    excelLSACTable.setStatus("current")
_ExcelLSACEntry_Object = MibTableRow
excelLSACEntry = _ExcelLSACEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 7, 1)
)
excelLSACEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelLSACSpanID"),
    (0, "EXCEL-SWITCH-MIB", "excelLSACChannelID"),
    (0, "EXCEL-SWITCH-MIB", "excelLSACEventID"),
)
if mibBuilder.loadTexts:
    excelLSACEntry.setStatus("current")


class _ExcelLSACIndex_Type(Integer32):
    """Custom type excelLSACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExcelLSACIndex_Type.__name__ = "Integer32"
_ExcelLSACIndex_Object = MibTableColumn
excelLSACIndex = _ExcelLSACIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 7, 1, 1),
    _ExcelLSACIndex_Type()
)
excelLSACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelLSACIndex.setStatus("current")


class _ExcelLSACSpanID_Type(Integer32):
    """Custom type excelLSACSpanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelLSACSpanID_Type.__name__ = "Integer32"
_ExcelLSACSpanID_Object = MibTableColumn
excelLSACSpanID = _ExcelLSACSpanID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 7, 1, 2),
    _ExcelLSACSpanID_Type()
)
excelLSACSpanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelLSACSpanID.setStatus("current")


class _ExcelLSACChannelID_Type(Integer32):
    """Custom type excelLSACChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ExcelLSACChannelID_Type.__name__ = "Integer32"
_ExcelLSACChannelID_Object = MibTableColumn
excelLSACChannelID = _ExcelLSACChannelID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 7, 1, 3),
    _ExcelLSACChannelID_Type()
)
excelLSACChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelLSACChannelID.setStatus("current")


class _ExcelLSACEventID_Type(Integer32):
    """Custom type excelLSACEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExcelLSACEventID_Type.__name__ = "Integer32"
_ExcelLSACEventID_Object = MibTableColumn
excelLSACEventID = _ExcelLSACEventID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 7, 1, 4),
    _ExcelLSACEventID_Type()
)
excelLSACEventID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelLSACEventID.setStatus("current")
_ExcelLSACTime_Type = DisplayString
_ExcelLSACTime_Object = MibTableColumn
excelLSACTime = _ExcelLSACTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 7, 1, 5),
    _ExcelLSACTime_Type()
)
excelLSACTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelLSACTime.setStatus("current")


class _ExcelLSACCount_Type(Integer32):
    """Custom type excelLSACCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32656),
    )


_ExcelLSACCount_Type.__name__ = "Integer32"
_ExcelLSACCount_Object = MibTableColumn
excelLSACCount = _ExcelLSACCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 7, 1, 6),
    _ExcelLSACCount_Type()
)
excelLSACCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelLSACCount.setStatus("current")
_ExcelLSACStatus_Type = RowStatus
_ExcelLSACStatus_Object = MibTableColumn
excelLSACStatus = _ExcelLSACStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 7, 1, 7),
    _ExcelLSACStatus_Type()
)
excelLSACStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelLSACStatus.setStatus("current")
_ExcelTLACTable_Object = MibTable
excelTLACTable = _ExcelTLACTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 8)
)
if mibBuilder.loadTexts:
    excelTLACTable.setStatus("current")
_ExcelTLACEntry_Object = MibTableRow
excelTLACEntry = _ExcelTLACEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 8, 1)
)
excelTLACEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelTLACSpanID"),
    (0, "EXCEL-SWITCH-MIB", "excelTLACChannelID"),
    (0, "EXCEL-SWITCH-MIB", "excelTLACEventID"),
)
if mibBuilder.loadTexts:
    excelTLACEntry.setStatus("current")


class _ExcelTLACIndex_Type(Integer32):
    """Custom type excelTLACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExcelTLACIndex_Type.__name__ = "Integer32"
_ExcelTLACIndex_Object = MibTableColumn
excelTLACIndex = _ExcelTLACIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 8, 1, 1),
    _ExcelTLACIndex_Type()
)
excelTLACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelTLACIndex.setStatus("current")


class _ExcelTLACSpanID_Type(Integer32):
    """Custom type excelTLACSpanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelTLACSpanID_Type.__name__ = "Integer32"
_ExcelTLACSpanID_Object = MibTableColumn
excelTLACSpanID = _ExcelTLACSpanID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 8, 1, 2),
    _ExcelTLACSpanID_Type()
)
excelTLACSpanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTLACSpanID.setStatus("current")


class _ExcelTLACChannelID_Type(Integer32):
    """Custom type excelTLACChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ExcelTLACChannelID_Type.__name__ = "Integer32"
_ExcelTLACChannelID_Object = MibTableColumn
excelTLACChannelID = _ExcelTLACChannelID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 8, 1, 3),
    _ExcelTLACChannelID_Type()
)
excelTLACChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTLACChannelID.setStatus("current")


class _ExcelTLACEventID_Type(Integer32):
    """Custom type excelTLACEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExcelTLACEventID_Type.__name__ = "Integer32"
_ExcelTLACEventID_Object = MibTableColumn
excelTLACEventID = _ExcelTLACEventID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 8, 1, 4),
    _ExcelTLACEventID_Type()
)
excelTLACEventID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTLACEventID.setStatus("current")
_ExcelTLACTime_Type = DisplayString
_ExcelTLACTime_Object = MibTableColumn
excelTLACTime = _ExcelTLACTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 8, 1, 5),
    _ExcelTLACTime_Type()
)
excelTLACTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTLACTime.setStatus("current")


class _ExcelTLACCount_Type(Integer32):
    """Custom type excelTLACCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32656),
    )


_ExcelTLACCount_Type.__name__ = "Integer32"
_ExcelTLACCount_Object = MibTableColumn
excelTLACCount = _ExcelTLACCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 8, 1, 6),
    _ExcelTLACCount_Type()
)
excelTLACCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTLACCount.setStatus("current")
_ExcelTLACStatus_Type = RowStatus
_ExcelTLACStatus_Object = MibTableColumn
excelTLACStatus = _ExcelTLACStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 8, 1, 7),
    _ExcelTLACStatus_Type()
)
excelTLACStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTLACStatus.setStatus("current")
_ExcelTSFCTable_Object = MibTable
excelTSFCTable = _ExcelTSFCTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 9)
)
if mibBuilder.loadTexts:
    excelTSFCTable.setStatus("current")
_ExcelTSFCEntry_Object = MibTableRow
excelTSFCEntry = _ExcelTSFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 9, 1)
)
excelTSFCEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelTSFCSpanID"),
    (0, "EXCEL-SWITCH-MIB", "excelTSFCChannelID"),
    (0, "EXCEL-SWITCH-MIB", "excelTSFCEventID"),
)
if mibBuilder.loadTexts:
    excelTSFCEntry.setStatus("current")


class _ExcelTSFCIndex_Type(Integer32):
    """Custom type excelTSFCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExcelTSFCIndex_Type.__name__ = "Integer32"
_ExcelTSFCIndex_Object = MibTableColumn
excelTSFCIndex = _ExcelTSFCIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 9, 1, 1),
    _ExcelTSFCIndex_Type()
)
excelTSFCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelTSFCIndex.setStatus("current")


class _ExcelTSFCSpanID_Type(Integer32):
    """Custom type excelTSFCSpanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelTSFCSpanID_Type.__name__ = "Integer32"
_ExcelTSFCSpanID_Object = MibTableColumn
excelTSFCSpanID = _ExcelTSFCSpanID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 9, 1, 2),
    _ExcelTSFCSpanID_Type()
)
excelTSFCSpanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTSFCSpanID.setStatus("current")


class _ExcelTSFCChannelID_Type(Integer32):
    """Custom type excelTSFCChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ExcelTSFCChannelID_Type.__name__ = "Integer32"
_ExcelTSFCChannelID_Object = MibTableColumn
excelTSFCChannelID = _ExcelTSFCChannelID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 9, 1, 3),
    _ExcelTSFCChannelID_Type()
)
excelTSFCChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTSFCChannelID.setStatus("current")


class _ExcelTSFCEventID_Type(Integer32):
    """Custom type excelTSFCEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExcelTSFCEventID_Type.__name__ = "Integer32"
_ExcelTSFCEventID_Object = MibTableColumn
excelTSFCEventID = _ExcelTSFCEventID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 9, 1, 4),
    _ExcelTSFCEventID_Type()
)
excelTSFCEventID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTSFCEventID.setStatus("current")
_ExcelTSFCTime_Type = DisplayString
_ExcelTSFCTime_Object = MibTableColumn
excelTSFCTime = _ExcelTSFCTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 9, 1, 5),
    _ExcelTSFCTime_Type()
)
excelTSFCTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTSFCTime.setStatus("current")


class _ExcelTSFCCount_Type(Integer32):
    """Custom type excelTSFCCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32656),
    )


_ExcelTSFCCount_Type.__name__ = "Integer32"
_ExcelTSFCCount_Object = MibTableColumn
excelTSFCCount = _ExcelTSFCCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 9, 1, 6),
    _ExcelTSFCCount_Type()
)
excelTSFCCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTSFCCount.setStatus("current")
_ExcelTSFCStatus_Type = RowStatus
_ExcelTSFCStatus_Object = MibTableColumn
excelTSFCStatus = _ExcelTSFCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 9, 1, 7),
    _ExcelTSFCStatus_Type()
)
excelTSFCStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelTSFCStatus.setStatus("current")
_ExcelCROTable_Object = MibTable
excelCROTable = _ExcelCROTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 10)
)
if mibBuilder.loadTexts:
    excelCROTable.setStatus("current")
_ExcelCROEntry_Object = MibTableRow
excelCROEntry = _ExcelCROEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 10, 1)
)
excelCROEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelCROSpanID"),
    (0, "EXCEL-SWITCH-MIB", "excelCROChannelID"),
    (0, "EXCEL-SWITCH-MIB", "excelCROEventID"),
)
if mibBuilder.loadTexts:
    excelCROEntry.setStatus("current")


class _ExcelCROIndex_Type(Integer32):
    """Custom type excelCROIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExcelCROIndex_Type.__name__ = "Integer32"
_ExcelCROIndex_Object = MibTableColumn
excelCROIndex = _ExcelCROIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 10, 1, 1),
    _ExcelCROIndex_Type()
)
excelCROIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelCROIndex.setStatus("current")


class _ExcelCROSpanID_Type(Integer32):
    """Custom type excelCROSpanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ExcelCROSpanID_Type.__name__ = "Integer32"
_ExcelCROSpanID_Object = MibTableColumn
excelCROSpanID = _ExcelCROSpanID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 10, 1, 2),
    _ExcelCROSpanID_Type()
)
excelCROSpanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCROSpanID.setStatus("current")


class _ExcelCROChannelID_Type(Integer32):
    """Custom type excelCROChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ExcelCROChannelID_Type.__name__ = "Integer32"
_ExcelCROChannelID_Object = MibTableColumn
excelCROChannelID = _ExcelCROChannelID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 10, 1, 3),
    _ExcelCROChannelID_Type()
)
excelCROChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCROChannelID.setStatus("current")


class _ExcelCROEventID_Type(Integer32):
    """Custom type excelCROEventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ExcelCROEventID_Type.__name__ = "Integer32"
_ExcelCROEventID_Object = MibTableColumn
excelCROEventID = _ExcelCROEventID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 10, 1, 4),
    _ExcelCROEventID_Type()
)
excelCROEventID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCROEventID.setStatus("current")
_ExcelCROTime_Type = DisplayString
_ExcelCROTime_Object = MibTableColumn
excelCROTime = _ExcelCROTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 10, 1, 5),
    _ExcelCROTime_Type()
)
excelCROTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCROTime.setStatus("current")


class _ExcelCROCount_Type(Integer32):
    """Custom type excelCROCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32656),
    )


_ExcelCROCount_Type.__name__ = "Integer32"
_ExcelCROCount_Object = MibTableColumn
excelCROCount = _ExcelCROCount_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 10, 1, 6),
    _ExcelCROCount_Type()
)
excelCROCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCROCount.setStatus("current")
_ExcelCROStatus_Type = RowStatus
_ExcelCROStatus_Object = MibTableColumn
excelCROStatus = _ExcelCROStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 5, 2, 10, 1, 7),
    _ExcelCROStatus_Type()
)
excelCROStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    excelCROStatus.setStatus("current")
_ExcelISDN_ObjectIdentity = ObjectIdentity
excelISDN = _ExcelISDN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6)
)
_ExcelISDNConfig_ObjectIdentity = ObjectIdentity
excelISDNConfig = _ExcelISDNConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6, 1)
)
_ExcelISDNConfigDChanTable_Object = MibTable
excelISDNConfigDChanTable = _ExcelISDNConfigDChanTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    excelISDNConfigDChanTable.setStatus("current")
_ExcelISDNConfigDChanEntry_Object = MibTableRow
excelISDNConfigDChanEntry = _ExcelISDNConfigDChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6, 1, 1, 1)
)
excelISDNConfigDChanEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelISDNConfigDChanIndex"),
    (0, "EXCEL-SWITCH-MIB", "excelISDNConfigDChanSpanIndex"),
)
if mibBuilder.loadTexts:
    excelISDNConfigDChanEntry.setStatus("current")


class _ExcelISDNConfigDChanSpanIndex_Type(Integer32):
    """Custom type excelISDNConfigDChanSpanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelISDNConfigDChanSpanIndex_Type.__name__ = "Integer32"
_ExcelISDNConfigDChanSpanIndex_Object = MibTableColumn
excelISDNConfigDChanSpanIndex = _ExcelISDNConfigDChanSpanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6, 1, 1, 1, 1),
    _ExcelISDNConfigDChanSpanIndex_Type()
)
excelISDNConfigDChanSpanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelISDNConfigDChanSpanIndex.setStatus("current")


class _ExcelISDNConfigDChanIndex_Type(Integer32):
    """Custom type excelISDNConfigDChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelISDNConfigDChanIndex_Type.__name__ = "Integer32"
_ExcelISDNConfigDChanIndex_Object = MibTableColumn
excelISDNConfigDChanIndex = _ExcelISDNConfigDChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6, 1, 1, 1, 2),
    _ExcelISDNConfigDChanIndex_Type()
)
excelISDNConfigDChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelISDNConfigDChanIndex.setStatus("current")


class _ExcelISDNConfigDChanConnType_Type(Integer32):
    """Custom type excelISDNConfigDChanConnType based on Integer32"""
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
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("att4ESS", 2),
          ("att4ESS931PRI", 13),
          ("att5ESS", 3),
          ("att5ESS931PRI", 14),
          ("attISDNBri", 12),
          ("austel", 6),
          ("euro-ISDN", 11),
          ("euroIDSNNetwork", 17),
          ("euroISDN", 8),
          ("jate", 7),
          ("nortelDMS100", 4),
          ("nortelDMS100931PRI", 15),
          ("nortelDMS250", 5),
          ("nortelDMS250931PRI", 16),
          ("other", 1),
          ("ukDASS2", 10),
          ("ukDpnss", 9))
    )


_ExcelISDNConfigDChanConnType_Type.__name__ = "Integer32"
_ExcelISDNConfigDChanConnType_Object = MibTableColumn
excelISDNConfigDChanConnType = _ExcelISDNConfigDChanConnType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6, 1, 1, 1, 3),
    _ExcelISDNConfigDChanConnType_Type()
)
excelISDNConfigDChanConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelISDNConfigDChanConnType.setStatus("current")


class _ExcelISDNConfigDChanHDLCBitPol_Type(Integer32):
    """Custom type excelISDNConfigDChanHDLCBitPol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("normal", 1))
    )


_ExcelISDNConfigDChanHDLCBitPol_Type.__name__ = "Integer32"
_ExcelISDNConfigDChanHDLCBitPol_Object = MibTableColumn
excelISDNConfigDChanHDLCBitPol = _ExcelISDNConfigDChanHDLCBitPol_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6, 1, 1, 1, 4),
    _ExcelISDNConfigDChanHDLCBitPol_Type()
)
excelISDNConfigDChanHDLCBitPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelISDNConfigDChanHDLCBitPol.setStatus("current")


class _ExcelISDNConfigDChanBChanSelect_Type(Integer32):
    """Custom type excelISDNConfigDChanBChanSelect based on Integer32"""
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
        *(("circularClockwise", 4),
          ("circularCounterCwise", 5),
          ("disabled", 1),
          ("linearClockwise", 2),
          ("linearCounterCwise", 3))
    )


_ExcelISDNConfigDChanBChanSelect_Type.__name__ = "Integer32"
_ExcelISDNConfigDChanBChanSelect_Object = MibTableColumn
excelISDNConfigDChanBChanSelect = _ExcelISDNConfigDChanBChanSelect_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6, 1, 1, 1, 5),
    _ExcelISDNConfigDChanBChanSelect_Type()
)
excelISDNConfigDChanBChanSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelISDNConfigDChanBChanSelect.setStatus("current")


class _ExcelISDNConfigDChanBChanEncTrans_Type(Integer32):
    """Custom type excelISDNConfigDChanBChanEncTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channelNumber", 1),
          ("slotMap", 2))
    )


_ExcelISDNConfigDChanBChanEncTrans_Type.__name__ = "Integer32"
_ExcelISDNConfigDChanBChanEncTrans_Object = MibTableColumn
excelISDNConfigDChanBChanEncTrans = _ExcelISDNConfigDChanBChanEncTrans_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6, 1, 1, 1, 6),
    _ExcelISDNConfigDChanBChanEncTrans_Type()
)
excelISDNConfigDChanBChanEncTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelISDNConfigDChanBChanEncTrans.setStatus("current")


class _ExcelISDNConfigDChanLocation_Type(Integer32):
    """Custom type excelISDNConfigDChanLocation based on Integer32"""
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
        *(("beyondInternetworking", 9),
          ("international", 8),
          ("other", 1),
          ("privateLocal", 3),
          ("privateRemote", 7),
          ("publicLocal", 4),
          ("publicRemote", 6),
          ("transit", 5),
          ("user", 2))
    )


_ExcelISDNConfigDChanLocation_Type.__name__ = "Integer32"
_ExcelISDNConfigDChanLocation_Object = MibTableColumn
excelISDNConfigDChanLocation = _ExcelISDNConfigDChanLocation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6, 1, 1, 1, 7),
    _ExcelISDNConfigDChanLocation_Type()
)
excelISDNConfigDChanLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelISDNConfigDChanLocation.setStatus("current")


class _ExcelISDNConfigDChanPhysicalMedium_Type(Integer32):
    """Custom type excelISDNConfigDChanPhysicalMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps64", 2),
          ("other", 1))
    )


_ExcelISDNConfigDChanPhysicalMedium_Type.__name__ = "Integer32"
_ExcelISDNConfigDChanPhysicalMedium_Object = MibTableColumn
excelISDNConfigDChanPhysicalMedium = _ExcelISDNConfigDChanPhysicalMedium_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 6, 1, 1, 1, 8),
    _ExcelISDNConfigDChanPhysicalMedium_Type()
)
excelISDNConfigDChanPhysicalMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelISDNConfigDChanPhysicalMedium.setStatus("current")
_ExcelMediaGateway_ObjectIdentity = ObjectIdentity
excelMediaGateway = _ExcelMediaGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7)
)
_ExcelMGSystem_ObjectIdentity = ObjectIdentity
excelMGSystem = _ExcelMGSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 1)
)


class _ExcelMGActiveProtocol_Type(Integer32):
    """Custom type excelMGActiveProtocol based on Integer32"""
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
        *(("ipdc", 2),
          ("ipst", 4),
          ("mgcp", 3),
          ("other", 1))
    )


_ExcelMGActiveProtocol_Type.__name__ = "Integer32"
_ExcelMGActiveProtocol_Object = MibScalar
excelMGActiveProtocol = _ExcelMGActiveProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 1, 1),
    _ExcelMGActiveProtocol_Type()
)
excelMGActiveProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGActiveProtocol.setStatus("current")
_ExcelMGSystemName_Type = DisplayString
_ExcelMGSystemName_Object = MibScalar
excelMGSystemName = _ExcelMGSystemName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 1, 2),
    _ExcelMGSystemName_Type()
)
excelMGSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGSystemName.setStatus("current")
_ExcelMGNumSlots_Type = SlotsInNode
_ExcelMGNumSlots_Object = MibScalar
excelMGNumSlots = _ExcelMGNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 1, 3),
    _ExcelMGNumSlots_Type()
)
excelMGNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGNumSlots.setStatus("current")
_ExcelMGVoip_ObjectIdentity = ObjectIdentity
excelMGVoip = _ExcelMGVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2)
)
_ExcelVoipAddressTable_Object = MibTable
excelVoipAddressTable = _ExcelVoipAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    excelVoipAddressTable.setStatus("current")
_ExcelVoipAddressEntry_Object = MibTableRow
excelVoipAddressEntry = _ExcelVoipAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 1, 1)
)
excelVoipAddressEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelVoipAddressIndex"),
)
if mibBuilder.loadTexts:
    excelVoipAddressEntry.setStatus("current")


class _ExcelVoipAddressIndex_Type(Integer32):
    """Custom type excelVoipAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ExcelVoipAddressIndex_Type.__name__ = "Integer32"
_ExcelVoipAddressIndex_Object = MibTableColumn
excelVoipAddressIndex = _ExcelVoipAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 1, 1, 1),
    _ExcelVoipAddressIndex_Type()
)
excelVoipAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelVoipAddressIndex.setStatus("current")


class _ExcelVoipAddressEntityType_Type(Integer32):
    """Custom type excelVoipAddressEntityType based on Integer32"""
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
        *(("dspModuleFour", 5),
          ("dspModuleOne", 2),
          ("dspModuleThree", 4),
          ("dspModuleTwo", 3),
          ("motherBoard", 1))
    )


_ExcelVoipAddressEntityType_Type.__name__ = "Integer32"
_ExcelVoipAddressEntityType_Object = MibTableColumn
excelVoipAddressEntityType = _ExcelVoipAddressEntityType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 1, 1, 2),
    _ExcelVoipAddressEntityType_Type()
)
excelVoipAddressEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipAddressEntityType.setStatus("current")
_ExcelVoipIpAddress_Type = IpAddress
_ExcelVoipIpAddress_Object = MibTableColumn
excelVoipIpAddress = _ExcelVoipIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 1, 1, 3),
    _ExcelVoipIpAddress_Type()
)
excelVoipIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipIpAddress.setStatus("current")
_ExcelVoipSubNetMask_Type = IpAddress
_ExcelVoipSubNetMask_Object = MibTableColumn
excelVoipSubNetMask = _ExcelVoipSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 1, 1, 4),
    _ExcelVoipSubNetMask_Type()
)
excelVoipSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipSubNetMask.setStatus("current")
_ExcelVoipIpGateway_Type = IpAddress
_ExcelVoipIpGateway_Object = MibTableColumn
excelVoipIpGateway = _ExcelVoipIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 1, 1, 5),
    _ExcelVoipIpGateway_Type()
)
excelVoipIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipIpGateway.setStatus("current")


class _ExcelVoipResetIndicator_Type(Integer32):
    """Custom type excelVoipResetIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noResetNeeded", 1),
          ("resetNeeded", 2))
    )


_ExcelVoipResetIndicator_Type.__name__ = "Integer32"
_ExcelVoipResetIndicator_Object = MibTableColumn
excelVoipResetIndicator = _ExcelVoipResetIndicator_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 1, 1, 6),
    _ExcelVoipResetIndicator_Type()
)
excelVoipResetIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelVoipResetIndicator.setStatus("current")
_ExcelMGResAttrIpAddress_Type = IpAddress
_ExcelMGResAttrIpAddress_Object = MibScalar
excelMGResAttrIpAddress = _ExcelMGResAttrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 2),
    _ExcelMGResAttrIpAddress_Type()
)
excelMGResAttrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelMGResAttrIpAddress.setStatus("current")
_ExcelMGResourceAttributeTable_Object = MibTable
excelMGResourceAttributeTable = _ExcelMGResourceAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3)
)
if mibBuilder.loadTexts:
    excelMGResourceAttributeTable.setStatus("current")
_ExcelMGResourceAttributeEntry_Object = MibTableRow
excelMGResourceAttributeEntry = _ExcelMGResourceAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1)
)
excelMGResourceAttributeEntry.setIndexNames(
    (0, "EXCEL-SWITCH-MIB", "excelMGResAttrIndex"),
)
if mibBuilder.loadTexts:
    excelMGResourceAttributeEntry.setStatus("current")
_ExcelMGResAttrIndex_Type = SlotsInNode
_ExcelMGResAttrIndex_Object = MibTableColumn
excelMGResAttrIndex = _ExcelMGResAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 1),
    _ExcelMGResAttrIndex_Type()
)
excelMGResAttrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excelMGResAttrIndex.setStatus("current")
_ExcelMGPayloadType_Type = PayloadTypes
_ExcelMGPayloadType_Object = MibTableColumn
excelMGPayloadType = _ExcelMGPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 2),
    _ExcelMGPayloadType_Type()
)
excelMGPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGPayloadType.setStatus("current")


class _ExcelMGPayloadSize_Type(Integer32):
    """Custom type excelMGPayloadSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1517),
    )


_ExcelMGPayloadSize_Type.__name__ = "Integer32"
_ExcelMGPayloadSize_Object = MibTableColumn
excelMGPayloadSize = _ExcelMGPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 3),
    _ExcelMGPayloadSize_Type()
)
excelMGPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGPayloadSize.setStatus("current")


class _ExcelMGSilenceSupression_Type(Integer32):
    """Custom type excelMGSilenceSupression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ExcelMGSilenceSupression_Type.__name__ = "Integer32"
_ExcelMGSilenceSupression_Object = MibTableColumn
excelMGSilenceSupression = _ExcelMGSilenceSupression_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 4),
    _ExcelMGSilenceSupression_Type()
)
excelMGSilenceSupression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGSilenceSupression.setStatus("current")


class _ExcelMGEchoCancellation_Type(Integer32):
    """Custom type excelMGEchoCancellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ExcelMGEchoCancellation_Type.__name__ = "Integer32"
_ExcelMGEchoCancellation_Object = MibTableColumn
excelMGEchoCancellation = _ExcelMGEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 5),
    _ExcelMGEchoCancellation_Type()
)
excelMGEchoCancellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGEchoCancellation.setStatus("current")


class _ExcelMGMinDelayValue_Type(Integer32):
    """Custom type excelMGMinDelayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_ExcelMGMinDelayValue_Type.__name__ = "Integer32"
_ExcelMGMinDelayValue_Object = MibTableColumn
excelMGMinDelayValue = _ExcelMGMinDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 6),
    _ExcelMGMinDelayValue_Type()
)
excelMGMinDelayValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGMinDelayValue.setStatus("current")


class _ExcelMGMaxDelayValue_Type(Integer32):
    """Custom type excelMGMaxDelayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_ExcelMGMaxDelayValue_Type.__name__ = "Integer32"
_ExcelMGMaxDelayValue_Object = MibTableColumn
excelMGMaxDelayValue = _ExcelMGMaxDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 7),
    _ExcelMGMaxDelayValue_Type()
)
excelMGMaxDelayValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGMaxDelayValue.setStatus("current")


class _ExcelMGAdaptionRate_Type(Integer32):
    """Custom type excelMGAdaptionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ExcelMGAdaptionRate_Type.__name__ = "Integer32"
_ExcelMGAdaptionRate_Object = MibTableColumn
excelMGAdaptionRate = _ExcelMGAdaptionRate_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 8),
    _ExcelMGAdaptionRate_Type()
)
excelMGAdaptionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGAdaptionRate.setStatus("current")


class _ExcelMGFaxType_Type(Integer32):
    """Custom type excelMGFaxType based on Integer32"""
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
        *(("bypass", 3),
          ("disable", 1),
          ("relay", 2))
    )


_ExcelMGFaxType_Type.__name__ = "Integer32"
_ExcelMGFaxType_Object = MibTableColumn
excelMGFaxType = _ExcelMGFaxType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 9),
    _ExcelMGFaxType_Type()
)
excelMGFaxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGFaxType.setStatus("current")


class _ExcelMGModemEnableTransport_Type(Integer32):
    """Custom type excelMGModemEnableTransport based on Integer32"""
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
        *(("v22DisableBypassOnly", 2),
          ("v22EnableBypassOnly", 1),
          ("v23DisableBypassOnly", 4),
          ("v23EnableBypassOnly", 3),
          ("v32DisableBypass", 6),
          ("v32DisableRelay", 8),
          ("v32EnableBypass", 5),
          ("v32EnableRelay", 7),
          ("v34DisableBypass", 10),
          ("v34DisableRelay", 12),
          ("v34EnableBypass", 9),
          ("v34EnableRelayFallback", 11))
    )


_ExcelMGModemEnableTransport_Type.__name__ = "Integer32"
_ExcelMGModemEnableTransport_Object = MibTableColumn
excelMGModemEnableTransport = _ExcelMGModemEnableTransport_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 10),
    _ExcelMGModemEnableTransport_Type()
)
excelMGModemEnableTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGModemEnableTransport.setStatus("current")
_ExcelMGBypassCoderType_Type = PayloadTypes
_ExcelMGBypassCoderType_Object = MibTableColumn
excelMGBypassCoderType = _ExcelMGBypassCoderType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 11),
    _ExcelMGBypassCoderType_Type()
)
excelMGBypassCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGBypassCoderType.setStatus("current")


class _ExcelMGRtpPacketDepth_Type(PacketDepth):
    """Custom type excelMGRtpPacketDepth based on PacketDepth"""
    defaultValue = 1


_ExcelMGRtpPacketDepth_Object = MibTableColumn
excelMGRtpPacketDepth = _ExcelMGRtpPacketDepth_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 12),
    _ExcelMGRtpPacketDepth_Type()
)
excelMGRtpPacketDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGRtpPacketDepth.setStatus("current")


class _ExcelMGFaxPacketDepth_Type(PacketDepth):
    """Custom type excelMGFaxPacketDepth based on PacketDepth"""
    defaultValue = 1


_ExcelMGFaxPacketDepth_Object = MibTableColumn
excelMGFaxPacketDepth = _ExcelMGFaxPacketDepth_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 13),
    _ExcelMGFaxPacketDepth_Type()
)
excelMGFaxPacketDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGFaxPacketDepth.setStatus("current")


class _ExcelMGModemPacketDepth_Type(PacketDepth):
    """Custom type excelMGModemPacketDepth based on PacketDepth"""
    defaultValue = 1


_ExcelMGModemPacketDepth_Object = MibTableColumn
excelMGModemPacketDepth = _ExcelMGModemPacketDepth_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 14),
    _ExcelMGModemPacketDepth_Type()
)
excelMGModemPacketDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGModemPacketDepth.setStatus("current")


class _ExcelMGTypeOfServicePrecedence_Type(Integer32):
    """Custom type excelMGTypeOfServicePrecedence based on Integer32"""
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
        *(("criticEcp", 6),
          ("flash", 4),
          ("flashOverride", 5),
          ("immediate", 3),
          ("internetworkControl", 7),
          ("networkControl", 8),
          ("priority", 2),
          ("routine", 1))
    )


_ExcelMGTypeOfServicePrecedence_Type.__name__ = "Integer32"
_ExcelMGTypeOfServicePrecedence_Object = MibTableColumn
excelMGTypeOfServicePrecedence = _ExcelMGTypeOfServicePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 15),
    _ExcelMGTypeOfServicePrecedence_Type()
)
excelMGTypeOfServicePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGTypeOfServicePrecedence.setStatus("current")


class _ExcelMGTypeOServiceDelay_Type(Integer32):
    """Custom type excelMGTypeOServiceDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowDelay", 2),
          ("normalDelay", 1))
    )


_ExcelMGTypeOServiceDelay_Type.__name__ = "Integer32"
_ExcelMGTypeOServiceDelay_Object = MibTableColumn
excelMGTypeOServiceDelay = _ExcelMGTypeOServiceDelay_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 16),
    _ExcelMGTypeOServiceDelay_Type()
)
excelMGTypeOServiceDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGTypeOServiceDelay.setStatus("current")


class _ExcelMGTypeOfServiceThroughput_Type(Integer32):
    """Custom type excelMGTypeOfServiceThroughput based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highThroughput", 2),
          ("nomalThroughput", 1))
    )


_ExcelMGTypeOfServiceThroughput_Type.__name__ = "Integer32"
_ExcelMGTypeOfServiceThroughput_Object = MibTableColumn
excelMGTypeOfServiceThroughput = _ExcelMGTypeOfServiceThroughput_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 17),
    _ExcelMGTypeOfServiceThroughput_Type()
)
excelMGTypeOfServiceThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGTypeOfServiceThroughput.setStatus("current")


class _ExcelMGTypeOfServiceReliability_Type(Integer32):
    """Custom type excelMGTypeOfServiceReliability based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highReliability", 2),
          ("normalReliability", 1))
    )


_ExcelMGTypeOfServiceReliability_Type.__name__ = "Integer32"
_ExcelMGTypeOfServiceReliability_Object = MibTableColumn
excelMGTypeOfServiceReliability = _ExcelMGTypeOfServiceReliability_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 18),
    _ExcelMGTypeOfServiceReliability_Type()
)
excelMGTypeOfServiceReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGTypeOfServiceReliability.setStatus("current")


class _ExcelMGTypeOfServiceCost_Type(Integer32):
    """Custom type excelMGTypeOfServiceCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowCost", 2),
          ("normalCost", 1))
    )


_ExcelMGTypeOfServiceCost_Type.__name__ = "Integer32"
_ExcelMGTypeOfServiceCost_Object = MibTableColumn
excelMGTypeOfServiceCost = _ExcelMGTypeOfServiceCost_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 19),
    _ExcelMGTypeOfServiceCost_Type()
)
excelMGTypeOfServiceCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGTypeOfServiceCost.setStatus("current")


class _ExcelMGRtcpPortOffset_Type(Integer32):
    """Custom type excelMGRtcpPortOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 10000),
    )


_ExcelMGRtcpPortOffset_Type.__name__ = "Integer32"
_ExcelMGRtcpPortOffset_Object = MibTableColumn
excelMGRtcpPortOffset = _ExcelMGRtcpPortOffset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 20),
    _ExcelMGRtcpPortOffset_Type()
)
excelMGRtcpPortOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGRtcpPortOffset.setStatus("current")


class _ExcelMGT38PortOffset_Type(Integer32):
    """Custom type excelMGT38PortOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 10000),
    )


_ExcelMGT38PortOffset_Type.__name__ = "Integer32"
_ExcelMGT38PortOffset_Object = MibTableColumn
excelMGT38PortOffset = _ExcelMGT38PortOffset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 2, 3, 1, 21),
    _ExcelMGT38PortOffset_Type()
)
excelMGT38PortOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGT38PortOffset.setStatus("current")
_ExcelMGConfig_ObjectIdentity = ObjectIdentity
excelMGConfig = _ExcelMGConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 3)
)
_ExcelMGConfigPrimaryMGCAddress_Type = IpAddress
_ExcelMGConfigPrimaryMGCAddress_Object = MibScalar
excelMGConfigPrimaryMGCAddress = _ExcelMGConfigPrimaryMGCAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 3, 1),
    _ExcelMGConfigPrimaryMGCAddress_Type()
)
excelMGConfigPrimaryMGCAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGConfigPrimaryMGCAddress.setStatus("current")


class _ExcelMGConfigPrimaryPort_Type(Integer32):
    """Custom type excelMGConfigPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 32565),
    )


_ExcelMGConfigPrimaryPort_Type.__name__ = "Integer32"
_ExcelMGConfigPrimaryPort_Object = MibScalar
excelMGConfigPrimaryPort = _ExcelMGConfigPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 3, 2),
    _ExcelMGConfigPrimaryPort_Type()
)
excelMGConfigPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGConfigPrimaryPort.setStatus("current")
_ExcelMGConfigSecondaryMGCAddress_Type = IpAddress
_ExcelMGConfigSecondaryMGCAddress_Object = MibScalar
excelMGConfigSecondaryMGCAddress = _ExcelMGConfigSecondaryMGCAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 3, 3),
    _ExcelMGConfigSecondaryMGCAddress_Type()
)
excelMGConfigSecondaryMGCAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGConfigSecondaryMGCAddress.setStatus("current")


class _ExcelMGConfigSecondaryPort_Type(Integer32):
    """Custom type excelMGConfigSecondaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 32565),
    )


_ExcelMGConfigSecondaryPort_Type.__name__ = "Integer32"
_ExcelMGConfigSecondaryPort_Object = MibScalar
excelMGConfigSecondaryPort = _ExcelMGConfigSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 3, 4),
    _ExcelMGConfigSecondaryPort_Type()
)
excelMGConfigSecondaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGConfigSecondaryPort.setStatus("current")


class _ExcelMGConfigLocalPort_Type(Integer32):
    """Custom type excelMGConfigLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 32565),
    )


_ExcelMGConfigLocalPort_Type.__name__ = "Integer32"
_ExcelMGConfigLocalPort_Object = MibScalar
excelMGConfigLocalPort = _ExcelMGConfigLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 3, 5),
    _ExcelMGConfigLocalPort_Type()
)
excelMGConfigLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGConfigLocalPort.setStatus("current")
_ExcelMGConfigIpdc_ObjectIdentity = ObjectIdentity
excelMGConfigIpdc = _ExcelMGConfigIpdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 4)
)


class _ExcelMGConfigIpdcReconnectAttempts_Type(Integer32):
    """Custom type excelMGConfigIpdcReconnectAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelMGConfigIpdcReconnectAttempts_Type.__name__ = "Integer32"
_ExcelMGConfigIpdcReconnectAttempts_Object = MibScalar
excelMGConfigIpdcReconnectAttempts = _ExcelMGConfigIpdcReconnectAttempts_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 4, 1),
    _ExcelMGConfigIpdcReconnectAttempts_Type()
)
excelMGConfigIpdcReconnectAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelMGConfigIpdcReconnectAttempts.setStatus("current")
_ExcelMGConfigMgcp_ObjectIdentity = ObjectIdentity
excelMGConfigMgcp = _ExcelMGConfigMgcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 5)
)


class _ExcelConfigMgcpPriTransmitInterval_Type(Integer32):
    """Custom type excelConfigMgcpPriTransmitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelConfigMgcpPriTransmitInterval_Type.__name__ = "Integer32"
_ExcelConfigMgcpPriTransmitInterval_Object = MibScalar
excelConfigMgcpPriTransmitInterval = _ExcelConfigMgcpPriTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 5, 1),
    _ExcelConfigMgcpPriTransmitInterval_Type()
)
excelConfigMgcpPriTransmitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelConfigMgcpPriTransmitInterval.setStatus("current")


class _ExcelConfigMgcpSecTransmitInterval_Type(Integer32):
    """Custom type excelConfigMgcpSecTransmitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExcelConfigMgcpSecTransmitInterval_Type.__name__ = "Integer32"
_ExcelConfigMgcpSecTransmitInterval_Object = MibScalar
excelConfigMgcpSecTransmitInterval = _ExcelConfigMgcpSecTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 5, 2),
    _ExcelConfigMgcpSecTransmitInterval_Type()
)
excelConfigMgcpSecTransmitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelConfigMgcpSecTransmitInterval.setStatus("current")


class _ExcelConfigMgcpResponseInterval_Type(Integer32):
    """Custom type excelConfigMgcpResponseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_ExcelConfigMgcpResponseInterval_Type.__name__ = "Integer32"
_ExcelConfigMgcpResponseInterval_Object = MibScalar
excelConfigMgcpResponseInterval = _ExcelConfigMgcpResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 5, 3),
    _ExcelConfigMgcpResponseInterval_Type()
)
excelConfigMgcpResponseInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelConfigMgcpResponseInterval.setStatus("current")


class _ExcelConfigMgcpRetransmissionTime_Type(Integer32):
    """Custom type excelConfigMgcpRetransmissionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_ExcelConfigMgcpRetransmissionTime_Type.__name__ = "Integer32"
_ExcelConfigMgcpRetransmissionTime_Object = MibScalar
excelConfigMgcpRetransmissionTime = _ExcelConfigMgcpRetransmissionTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 2, 4, 2, 2, 7, 5, 4),
    _ExcelConfigMgcpRetransmissionTime_Type()
)
excelConfigMgcpRetransmissionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excelConfigMgcpRetransmissionTime.setStatus("current")
_ExcelOAMP_ObjectIdentity = ObjectIdentity
excelOAMP = _ExcelOAMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 3)
)


class _ExcelEXSAgentVerbose_Type(Integer32):
    """Custom type excelEXSAgentVerbose based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ExcelEXSAgentVerbose_Type.__name__ = "Integer32"
_ExcelEXSAgentVerbose_Object = MibScalar
excelEXSAgentVerbose = _ExcelEXSAgentVerbose_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 3, 1),
    _ExcelEXSAgentVerbose_Type()
)
excelEXSAgentVerbose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelEXSAgentVerbose.setStatus("current")


class _ExcelEXSEventManagerVerbose_Type(Integer32):
    """Custom type excelEXSEventManagerVerbose based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ExcelEXSEventManagerVerbose_Type.__name__ = "Integer32"
_ExcelEXSEventManagerVerbose_Object = MibScalar
excelEXSEventManagerVerbose = _ExcelEXSEventManagerVerbose_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 3, 2),
    _ExcelEXSEventManagerVerbose_Type()
)
excelEXSEventManagerVerbose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excelEXSEventManagerVerbose.setStatus("current")
_ExcelExtension_ObjectIdentity = ObjectIdentity
excelExtension = _ExcelExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 2, 4)
)

# Managed Objects groups


# Notification objects

excelCardUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 1)
)
excelCardUpTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmStatus"),
        ("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardUpTrap.setStatus(
        "obsolete"
    )

excelCardDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 2)
)
excelCardDownTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmStatus"),
        ("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardDownTrap.setStatus(
        "current"
    )

excelCardActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 3)
)
excelCardActiveTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmStatus"),
        ("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardActiveTrap.setStatus(
        "current"
    )

excelFaultLoggedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 4)
)
excelFaultLoggedTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelFaultLoggedTrap.setStatus(
        "current"
    )

excelRingUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 5)
)
excelRingUpTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmStatus"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelRingUpTrap.setStatus(
        "current"
    )

excelRingDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 6)
)
excelRingDownTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelRingDownTrap.setStatus(
        "current"
    )

excelSystemBusyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 7)
)
excelSystemBusyTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelSystemBusyTrap.setStatus(
        "current"
    )

excelSystemBusyWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 8)
)
excelSystemBusyWarningTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelSystemBusyWarningTrap.setStatus(
        "current"
    )

excelSystemBusyClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 9)
)
excelSystemBusyClearedTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelSystemBusyClearedTrap.setStatus(
        "current"
    )

excelClockModeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 10)
)
excelClockModeChangeTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelClockModeChangeTrap.setStatus(
        "current"
    )

excelDSPResourceBlockTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 11)
)
excelDSPResourceBlockTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmDSPLastBlocked"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelDSPResourceBlockTrap.setStatus(
        "current"
    )

excelDSPFuncNotCfgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 12)
)
excelDSPFuncNotCfgTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelDSPFuncNotCfgTrap.setStatus(
        "current"
    )

excelDSPMgmtInconsistentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 13)
)
excelDSPMgmtInconsistentTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelDSPMgmtInconsistentTrap.setStatus(
        "current"
    )

excelDldTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 14)
)
excelDldTimeoutTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelDldTimeoutTrap.setStatus(
        "current"
    )

excelRANUnAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 15)
)
excelRANUnAvailableTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelRANUnAvailableTrap.setStatus(
        "current"
    )

excelResourceUtilThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 16)
)
excelResourceUtilThreshTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelResourceUtilThreshTrap.setStatus(
        "current"
    )

excelCardNotSuppTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 17)
)
excelCardNotSuppTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardNotSuppTrap.setStatus(
        "current"
    )

excelCardDldCorruptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 18)
)
excelCardDldCorruptTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardDldCorruptTrap.setStatus(
        "current"
    )

excelCardNotRecTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 19)
)
excelCardNotRecTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardNotRecTrap.setStatus(
        "current"
    )

excelCardCfgResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 20)
)
excelCardCfgResetTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardCfgResetTrap.setStatus(
        "current"
    )

excelCardConnMapFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 21)
)
excelCardConnMapFailTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardConnMapFailTrap.setStatus(
        "current"
    )

excelCardNoSWTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 22)
)
excelCardNoSWTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardNoSWTrap.setStatus(
        "current"
    )

excelCardNoALawTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 23)
)
excelCardNoALawTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardNoALawTrap.setStatus(
        "current"
    )

excelCardRevNotSuppTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 24)
)
excelCardRevNotSuppTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardRevNotSuppTrap.setStatus(
        "current"
    )

excelEthernetErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 25)
)
excelEthernetErrTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelEthernetErrTrap.setStatus(
        "current"
    )

excelNoFanTrayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 26)
)
excelNoFanTrayTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelNoFanTrayTrap.setStatus(
        "current"
    )

excelExnetACommFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 27)
)
excelExnetACommFailTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelExnetACommFailTrap.setStatus(
        "current"
    )

excelExnetBCommFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 28)
)
excelExnetBCommFailTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelExnetBCommFailTrap.setStatus(
        "current"
    )

excelExnetAFiberFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 29)
)
excelExnetAFiberFailTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelExnetAFiberFailTrap.setStatus(
        "current"
    )

excelExnetBFiberFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 30)
)
excelExnetBFiberFailTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelExnetBFiberFailTrap.setStatus(
        "current"
    )

excelEXSAPITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 31)
)
excelEXSAPITrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelNodePhysicalID"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelEXSAPITrap.setStatus(
        "current"
    )

excelEXSConfTSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 32)
)
excelEXSConfTSTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelNodePhysicalID"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelEXSConfTSTrap.setStatus(
        "current"
    )

excelEXSSCbusMasterChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 33)
)
excelEXSSCbusMasterChangedTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelNodePhysicalID"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelEXSSCbusMasterChangedTrap.setStatus(
        "current"
    )

excelEXSSCbusFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 34)
)
excelEXSSCbusFailureTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelNodePhysicalID"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelEXSSCbusFailureTrap.setStatus(
        "current"
    )

excelSS7NetCongestionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 35)
)
excelSS7NetCongestionTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelSS7NetCongestionTrap.setStatus(
        "current"
    )

excelSS7RemISUPUnavailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 36)
)
excelSS7RemISUPUnavailTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelSS7RemISUPUnavailTrap.setStatus(
        "current"
    )

excelClockSourceLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 37)
)
excelClockSourceLostTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmRefClockSrc"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelClockSourceLostTrap.setStatus(
        "current"
    )

excelClockSourceLostClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 38)
)
excelClockSourceLostClearedTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmRefClockSrc"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelClockSourceLostClearedTrap.setStatus(
        "current"
    )

excelNoSupportDSPFuncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 39)
)
excelNoSupportDSPFuncTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelNoSupportDSPFuncTrap.setStatus(
        "current"
    )

excelPartialMessageReceivedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 40)
)
excelPartialMessageReceivedTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelPartialMessageReceivedTrap.setStatus(
        "current"
    )

excelUnackedMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 41)
)
excelUnackedMsgTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelUnackedMsgTrap.setStatus(
        "current"
    )

excelNodeIDAlreadyExistsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 42)
)
excelNodeIDAlreadyExistsTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelNodeIDAlreadyExistsTrap.setStatus(
        "current"
    )

excelInvalidMsgLenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 43)
)
excelInvalidMsgLenTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelInvalidMsgLenTrap.setStatus(
        "current"
    )

excelLogSpanIDExistsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 44)
)
excelLogSpanIDExistsTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelLogSpanIDExistsTrap.setStatus(
        "current"
    )

excelNodeUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 45)
)
excelNodeUpTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelNodePhysicalID"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelNodeUpTrap.setStatus(
        "current"
    )

excelNodeDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 46)
)
excelNodeDownTrap.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelNodePhysicalID"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelNodeDownTrap.setStatus(
        "current"
    )

excelSubagentConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 47)
)
excelSubagentConnect.setObjects(
    ("EXCEL-SWITCH-MIB", "excelNodeIdentifier")
)
if mibBuilder.loadTexts:
    excelSubagentConnect.setStatus(
        "current"
    )

excelSwitchConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 48)
)
excelSwitchConnect.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelCurrentNode"),
        ("EXCEL-SWITCH-MIB", "excelNodeIdentifier"))
)
if mibBuilder.loadTexts:
    excelSwitchConnect.setStatus(
        "current"
    )

excelSwitchLossConnectivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 49)
)
excelSwitchLossConnectivity.setObjects(
    ("EXCEL-SWITCH-MIB", "excelNodeIdentifier")
)
if mibBuilder.loadTexts:
    excelSwitchLossConnectivity.setStatus(
        "current"
    )

excelSpanCarrierGroupAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 50)
)
excelSpanCarrierGroupAlarm.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelLogicalSpanId"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelSpanCarrierGroupAlarm.setStatus(
        "current"
    )

excelSpanExcessiveSlips = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 51)
)
excelSpanExcessiveSlips.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelLogicalSpanId"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelSpanExcessiveSlips.setStatus(
        "current"
    )

excelSpanJ1Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 52)
)
excelSpanJ1Failure.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelSpanJ1Failure.setStatus(
        "current"
    )

excelLineCardBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 53)
)
if mibBuilder.loadTexts:
    excelLineCardBusy.setStatus(
        "current"
    )

excelLineCardApproachBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 54)
)
if mibBuilder.loadTexts:
    excelLineCardApproachBusy.setStatus(
        "current"
    )

excelLowMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 55)
)
if mibBuilder.loadTexts:
    excelLowMemory.setStatus(
        "current"
    )

excelCardStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 56)
)
excelCardStatusChange.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmStatus"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelCardStatusChange.setStatus(
        "current"
    )

excelLowMemoryCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 57)
)
if mibBuilder.loadTexts:
    excelLowMemoryCleared.setStatus(
        "current"
    )

excelGenericEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 58)
)
excelGenericEvent.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelGenericEvent.setStatus(
        "current"
    )

excelSubrateSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 59)
)
if mibBuilder.loadTexts:
    excelSubrateSwitchOver.setStatus(
        "current"
    )

excelSwitchOverInterrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 60)
)
if mibBuilder.loadTexts:
    excelSwitchOverInterrupt.setStatus(
        "current"
    )

excelSwitchOverSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 61)
)
if mibBuilder.loadTexts:
    excelSwitchOverSuccess.setStatus(
        "current"
    )

excelSwitchOverFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 62)
)
if mibBuilder.loadTexts:
    excelSwitchOverFailure.setStatus(
        "current"
    )

excelBackupDiagnostics = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 63)
)
if mibBuilder.loadTexts:
    excelBackupDiagnostics.setStatus(
        "current"
    )

excelSCbusMasterChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 64)
)
if mibBuilder.loadTexts:
    excelSCbusMasterChange.setStatus(
        "current"
    )

excelSCBusFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 65)
)
if mibBuilder.loadTexts:
    excelSCBusFail.setStatus(
        "current"
    )

excelGeneralSoftwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 66)
)
if mibBuilder.loadTexts:
    excelGeneralSoftwareError.setStatus(
        "current"
    )

excelRearSlotController = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 67)
)
excelRearSlotController.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelRearSlotController.setStatus(
        "current"
    )

excelFrontSlotController = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 68)
)
excelFrontSlotController.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelFrontSlotController.setStatus(
        "current"
    )

excelConnectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 69)
)
if mibBuilder.loadTexts:
    excelConnectNotification.setStatus(
        "current"
    )

excelRouteTableUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 70)
)
excelRouteTableUpdated.setObjects(
    ("EXCEL-SWITCH-MIB", "excelNodePhysicalID")
)
if mibBuilder.loadTexts:
    excelRouteTableUpdated.setStatus(
        "current"
    )

excelResourceGroupTableUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 71)
)
excelResourceGroupTableUpdated.setObjects(
    ("EXCEL-SWITCH-MIB", "excelNodePhysicalID")
)
if mibBuilder.loadTexts:
    excelResourceGroupTableUpdated.setStatus(
        "current"
    )

excelOldRouteTableDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 73)
)
excelOldRouteTableDeleted.setObjects(
    ("EXCEL-SWITCH-MIB", "excelNodePhysicalID")
)
if mibBuilder.loadTexts:
    excelOldRouteTableDeleted.setStatus(
        "current"
    )

excelRouteTableForcefullyDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 74)
)
excelRouteTableForcefullyDeleted.setObjects(
    ("EXCEL-SWITCH-MIB", "excelNodePhysicalID")
)
if mibBuilder.loadTexts:
    excelRouteTableForcefullyDeleted.setStatus(
        "current"
    )

excelResourceGroupTableForceDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 75)
)
excelResourceGroupTableForceDelete.setObjects(
    ("EXCEL-SWITCH-MIB", "excelNodePhysicalID")
)
if mibBuilder.loadTexts:
    excelResourceGroupTableForceDelete.setStatus(
        "current"
    )

excelLoadProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 76)
)
if mibBuilder.loadTexts:
    excelLoadProblem.setStatus(
        "current"
    )

excelTFTPFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 77)
)
excelTFTPFailure.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelTFTPFailure.setStatus(
        "current"
    )

excelPPLEventL3PCIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 78)
)
excelPPLEventL3PCIC.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventL3PCIC.setStatus(
        "current"
    )

excelPPLEventL3PLINK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 79)
)
excelPPLEventL3PLINK.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventL3PLINK.setStatus(
        "current"
    )

excelPPLEventCPC = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 80)
)
excelPPLEventCPC.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventCPC.setStatus(
        "current"
    )

excelPPLEventSPRC = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 81)
)
excelPPLEventSPRC.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventSPRC.setStatus(
        "current"
    )

excelPPLEventBLS = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 82)
)
excelPPLEventBLS.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventBLS.setStatus(
        "current"
    )

excelPPLEventBLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 83)
)
excelPPLEventBLR.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventBLR.setStatus(
        "current"
    )

excelPPLEventCRS = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 84)
)
excelPPLEventCRS.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventCRS.setStatus(
        "current"
    )

excelPPLEventCRR = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 85)
)
excelPPLEventCRR.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventCRR.setStatus(
        "current"
    )

excelPPLEventUCIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 86)
)
excelPPLEventUCIC.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventUCIC.setStatus(
        "current"
    )

excelPPLEventCGRS = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 87)
)
excelPPLEventCGRS.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventCGRS.setStatus(
        "current"
    )

excelPPLEventCGRR = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 88)
)
excelPPLEventCGRR.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventCGRR.setStatus(
        "current"
    )

excelPPLEventGBUS = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 89)
)
excelPPLEventGBUS.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventGBUS.setStatus(
        "current"
    )

excelPPLEventGBUR = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 90)
)
excelPPLEventGBUR.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventGBUR.setStatus(
        "current"
    )

excelPPLEventHGBR = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 91)
)
excelPPLEventHGBR.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventHGBR.setStatus(
        "current"
    )

excelPPLEventMTP3Hmdt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 92)
)
excelPPLEventMTP3Hmdt.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventMTP3Hmdt.setStatus(
        "current"
    )

excelPPLEventMTP3Lsac = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 93)
)
excelPPLEventMTP3Lsac.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventMTP3Lsac.setStatus(
        "current"
    )

excelPPLEventMTP3Tlac = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 94)
)
excelPPLEventMTP3Tlac.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventMTP3Tlac.setStatus(
        "current"
    )

excelPPLEventMTP3Tsfc = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 95)
)
excelPPLEventMTP3Tsfc.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventMTP3Tsfc.setStatus(
        "current"
    )

excelPPLEventISUPHlb = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 96)
)
excelPPLEventISUPHlb.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventISUPHlb.setStatus(
        "current"
    )

excelPPLEventCRCR = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 97)
)
excelPPLEventCRCR.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventCRCR.setStatus(
        "current"
    )

excelPPLEventMGBS = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 98)
)
excelPPLEventMGBS.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventMGBS.setStatus(
        "current"
    )

excelPPLEventHGBS = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 99)
)
excelPPLEventHGBS.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventHGBS.setStatus(
        "current"
    )

excelPPLEventCQS = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 100)
)
excelPPLEventCQS.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventCQS.setStatus(
        "current"
    )

excelPPLEventCVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 101)
)
excelPPLEventCVS.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventCVS.setStatus(
        "current"
    )

excelPPLEventCRCS = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 102)
)
excelPPLEventCRCS.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventCRCS.setStatus(
        "current"
    )

excelPPLEventCRO = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 103)
)
excelPPLEventCRO.setObjects(
    ("EXCEL-SWITCH-MIB", "excelPPLComponentId")
)
if mibBuilder.loadTexts:
    excelPPLEventCRO.setStatus(
        "current"
    )

excelDchannelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 104)
)
excelDchannelFailure.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelDchannelFailure.setStatus(
        "current"
    )

excelVoIPModuleOOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 105)
)
excelVoIPModuleOOS.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelVoIPModuleOOS.setStatus(
        "current"
    )

excelVoipModuleDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 106)
)
excelVoipModuleDead.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelVoipModuleDead.setStatus(
        "current"
    )

excelVoipModuleDspDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 107)
)
excelVoipModuleDspDead.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelVoipModuleDspDead.setStatus(
        "current"
    )

excelVoipModuleReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 108)
)
excelVoipModuleReset.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelVoipModuleReset.setStatus(
        "current"
    )

excelMatrixSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 67, 0, 109)
)
excelMatrixSwitchover.setObjects(
      *(("EXCEL-SWITCH-MIB", "excelSysLastAlarmStatus"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmNode"),
        ("EXCEL-SWITCH-MIB", "excelDeviceCardSlotIndex"),
        ("EXCEL-SWITCH-MIB", "excelSysLastAlarmSeverity"))
)
if mibBuilder.loadTexts:
    excelMatrixSwitchover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXCEL-SWITCH-MIB",
    **{"SlotsInNode": SlotsInNode,
       "DSPFunctionTypes": DSPFunctionTypes,
       "CardOperState": CardOperState,
       "SS7VariantsTypes": SS7VariantsTypes,
       "PayloadTypes": PayloadTypes,
       "PacketDepth": PacketDepth,
       "lucent": lucent,
       "products": products,
       "excel": excel,
       "excelTraps": excelTraps,
       "excelCardUpTrap": excelCardUpTrap,
       "excelCardDownTrap": excelCardDownTrap,
       "excelCardActiveTrap": excelCardActiveTrap,
       "excelFaultLoggedTrap": excelFaultLoggedTrap,
       "excelRingUpTrap": excelRingUpTrap,
       "excelRingDownTrap": excelRingDownTrap,
       "excelSystemBusyTrap": excelSystemBusyTrap,
       "excelSystemBusyWarningTrap": excelSystemBusyWarningTrap,
       "excelSystemBusyClearedTrap": excelSystemBusyClearedTrap,
       "excelClockModeChangeTrap": excelClockModeChangeTrap,
       "excelDSPResourceBlockTrap": excelDSPResourceBlockTrap,
       "excelDSPFuncNotCfgTrap": excelDSPFuncNotCfgTrap,
       "excelDSPMgmtInconsistentTrap": excelDSPMgmtInconsistentTrap,
       "excelDldTimeoutTrap": excelDldTimeoutTrap,
       "excelRANUnAvailableTrap": excelRANUnAvailableTrap,
       "excelResourceUtilThreshTrap": excelResourceUtilThreshTrap,
       "excelCardNotSuppTrap": excelCardNotSuppTrap,
       "excelCardDldCorruptTrap": excelCardDldCorruptTrap,
       "excelCardNotRecTrap": excelCardNotRecTrap,
       "excelCardCfgResetTrap": excelCardCfgResetTrap,
       "excelCardConnMapFailTrap": excelCardConnMapFailTrap,
       "excelCardNoSWTrap": excelCardNoSWTrap,
       "excelCardNoALawTrap": excelCardNoALawTrap,
       "excelCardRevNotSuppTrap": excelCardRevNotSuppTrap,
       "excelEthernetErrTrap": excelEthernetErrTrap,
       "excelNoFanTrayTrap": excelNoFanTrayTrap,
       "excelExnetACommFailTrap": excelExnetACommFailTrap,
       "excelExnetBCommFailTrap": excelExnetBCommFailTrap,
       "excelExnetAFiberFailTrap": excelExnetAFiberFailTrap,
       "excelExnetBFiberFailTrap": excelExnetBFiberFailTrap,
       "excelEXSAPITrap": excelEXSAPITrap,
       "excelEXSConfTSTrap": excelEXSConfTSTrap,
       "excelEXSSCbusMasterChangedTrap": excelEXSSCbusMasterChangedTrap,
       "excelEXSSCbusFailureTrap": excelEXSSCbusFailureTrap,
       "excelSS7NetCongestionTrap": excelSS7NetCongestionTrap,
       "excelSS7RemISUPUnavailTrap": excelSS7RemISUPUnavailTrap,
       "excelClockSourceLostTrap": excelClockSourceLostTrap,
       "excelClockSourceLostClearedTrap": excelClockSourceLostClearedTrap,
       "excelNoSupportDSPFuncTrap": excelNoSupportDSPFuncTrap,
       "excelPartialMessageReceivedTrap": excelPartialMessageReceivedTrap,
       "excelUnackedMsgTrap": excelUnackedMsgTrap,
       "excelNodeIDAlreadyExistsTrap": excelNodeIDAlreadyExistsTrap,
       "excelInvalidMsgLenTrap": excelInvalidMsgLenTrap,
       "excelLogSpanIDExistsTrap": excelLogSpanIDExistsTrap,
       "excelNodeUpTrap": excelNodeUpTrap,
       "excelNodeDownTrap": excelNodeDownTrap,
       "excelSubagentConnect": excelSubagentConnect,
       "excelSwitchConnect": excelSwitchConnect,
       "excelSwitchLossConnectivity": excelSwitchLossConnectivity,
       "excelSpanCarrierGroupAlarm": excelSpanCarrierGroupAlarm,
       "excelSpanExcessiveSlips": excelSpanExcessiveSlips,
       "excelSpanJ1Failure": excelSpanJ1Failure,
       "excelLineCardBusy": excelLineCardBusy,
       "excelLineCardApproachBusy": excelLineCardApproachBusy,
       "excelLowMemory": excelLowMemory,
       "excelCardStatusChange": excelCardStatusChange,
       "excelLowMemoryCleared": excelLowMemoryCleared,
       "excelGenericEvent": excelGenericEvent,
       "excelSubrateSwitchOver": excelSubrateSwitchOver,
       "excelSwitchOverInterrupt": excelSwitchOverInterrupt,
       "excelSwitchOverSuccess": excelSwitchOverSuccess,
       "excelSwitchOverFailure": excelSwitchOverFailure,
       "excelBackupDiagnostics": excelBackupDiagnostics,
       "excelSCbusMasterChange": excelSCbusMasterChange,
       "excelSCBusFail": excelSCBusFail,
       "excelGeneralSoftwareError": excelGeneralSoftwareError,
       "excelRearSlotController": excelRearSlotController,
       "excelFrontSlotController": excelFrontSlotController,
       "excelConnectNotification": excelConnectNotification,
       "excelRouteTableUpdated": excelRouteTableUpdated,
       "excelResourceGroupTableUpdated": excelResourceGroupTableUpdated,
       "excelOldRouteTableDeleted": excelOldRouteTableDeleted,
       "excelRouteTableForcefullyDeleted": excelRouteTableForcefullyDeleted,
       "excelResourceGroupTableForceDelete": excelResourceGroupTableForceDelete,
       "excelLoadProblem": excelLoadProblem,
       "excelTFTPFailure": excelTFTPFailure,
       "excelPPLEventL3PCIC": excelPPLEventL3PCIC,
       "excelPPLEventL3PLINK": excelPPLEventL3PLINK,
       "excelPPLEventCPC": excelPPLEventCPC,
       "excelPPLEventSPRC": excelPPLEventSPRC,
       "excelPPLEventBLS": excelPPLEventBLS,
       "excelPPLEventBLR": excelPPLEventBLR,
       "excelPPLEventCRS": excelPPLEventCRS,
       "excelPPLEventCRR": excelPPLEventCRR,
       "excelPPLEventUCIC": excelPPLEventUCIC,
       "excelPPLEventCGRS": excelPPLEventCGRS,
       "excelPPLEventCGRR": excelPPLEventCGRR,
       "excelPPLEventGBUS": excelPPLEventGBUS,
       "excelPPLEventGBUR": excelPPLEventGBUR,
       "excelPPLEventHGBR": excelPPLEventHGBR,
       "excelPPLEventMTP3Hmdt": excelPPLEventMTP3Hmdt,
       "excelPPLEventMTP3Lsac": excelPPLEventMTP3Lsac,
       "excelPPLEventMTP3Tlac": excelPPLEventMTP3Tlac,
       "excelPPLEventMTP3Tsfc": excelPPLEventMTP3Tsfc,
       "excelPPLEventISUPHlb": excelPPLEventISUPHlb,
       "excelPPLEventCRCR": excelPPLEventCRCR,
       "excelPPLEventMGBS": excelPPLEventMGBS,
       "excelPPLEventHGBS": excelPPLEventHGBS,
       "excelPPLEventCQS": excelPPLEventCQS,
       "excelPPLEventCVS": excelPPLEventCVS,
       "excelPPLEventCRCS": excelPPLEventCRCS,
       "excelPPLEventCRO": excelPPLEventCRO,
       "excelDchannelFailure": excelDchannelFailure,
       "excelVoIPModuleOOS": excelVoIPModuleOOS,
       "excelVoipModuleDead": excelVoipModuleDead,
       "excelVoipModuleDspDead": excelVoipModuleDspDead,
       "excelVoipModuleReset": excelVoipModuleReset,
       "excelMatrixSwitchover": excelMatrixSwitchover,
       "excelProducts": excelProducts,
       "excelSystem": excelSystem,
       "excelNodeIdentifier": excelNodeIdentifier,
       "excelNodeLocationIdentifier": excelNodeLocationIdentifier,
       "excelNodeCurrentTime": excelNodeCurrentTime,
       "excelSwitch": excelSwitch,
       "excelCurrentNode": excelCurrentNode,
       "excelNodes": excelNodes,
       "excelNodeTable": excelNodeTable,
       "excelNodeEntry": excelNodeEntry,
       "excelNodeIndex": excelNodeIndex,
       "excelNodeLogicalID": excelNodeLogicalID,
       "excelNodePhysicalID": excelNodePhysicalID,
       "excelNodeType": excelNodeType,
       "excelNode": excelNode,
       "excelNodeHardware": excelNodeHardware,
       "excelCommunicationEquipment": excelCommunicationEquipment,
       "excelCommunicationCard": excelCommunicationCard,
       "excelCommCardTable": excelCommCardTable,
       "excelCommCardEntry": excelCommCardEntry,
       "excelCommCardSlotIndex": excelCommCardSlotIndex,
       "excelCommCardOperState": excelCommCardOperState,
       "excelCommCardResetReason": excelCommCardResetReason,
       "excelCommCardConfigStatus": excelCommCardConfigStatus,
       "excelCommCardConfidenceTest": excelCommCardConfidenceTest,
       "excelCommCardAction": excelCommCardAction,
       "excelCommCardActionTime": excelCommCardActionTime,
       "excelDSP": excelDSP,
       "excelVoipDsp": excelVoipDsp,
       "excelVoipSlotNumber": excelVoipSlotNumber,
       "excelVoipDspTable": excelVoipDspTable,
       "excelVoipDspEntry": excelVoipDspEntry,
       "excelVoipDspIndex": excelVoipDspIndex,
       "excelVoipDspInstalled": excelVoipDspInstalled,
       "excelVoipDspNumChannelsSupported": excelVoipDspNumChannelsSupported,
       "excelVoipDspOperState": excelVoipDspOperState,
       "excelVoipDspArtworkRevision": excelVoipDspArtworkRevision,
       "excelVoipDspFuncRevision": excelVoipDspFuncRevision,
       "excelVoipDspHWRevision": excelVoipDspHWRevision,
       "excelVoipDspSWRevision": excelVoipDspSWRevision,
       "excelVoipDspRamSize": excelVoipDspRamSize,
       "excelVoipDspSerialNum": excelVoipDspSerialNum,
       "excelVoipDspRamBuildNumber": excelVoipDspRamBuildNumber,
       "excelDeviceEquipment": excelDeviceEquipment,
       "excelDeviceCard": excelDeviceCard,
       "excelDeviceCardTable": excelDeviceCardTable,
       "excelDeviceCardEntry": excelDeviceCardEntry,
       "excelDeviceCardSlotIndex": excelDeviceCardSlotIndex,
       "excelDeviceCardType": excelDeviceCardType,
       "excelDeviceCardModelDescription": excelDeviceCardModelDescription,
       "excelDeviceCardArtworkRevision": excelDeviceCardArtworkRevision,
       "excelDeviceCardFuncRevision": excelDeviceCardFuncRevision,
       "excelDeviceCardHWRevision": excelDeviceCardHWRevision,
       "excelDeviceCardSWRevision": excelDeviceCardSWRevision,
       "excelDeviceCardRamSize": excelDeviceCardRamSize,
       "excelDeviceCardSerialNum": excelDeviceCardSerialNum,
       "excelDeviceCardRAMBuildNum": excelDeviceCardRAMBuildNum,
       "excelUtility": excelUtility,
       "excelResourceEquipment": excelResourceEquipment,
       "excelResourceUtilization": excelResourceUtilization,
       "excelResourceSlotId": excelResourceSlotId,
       "excelResourceUsageTable": excelResourceUsageTable,
       "excelResourceUsageEntry": excelResourceUsageEntry,
       "excelResourceUsageIndex": excelResourceUsageIndex,
       "excelCpuTime": excelCpuTime,
       "excelMcbUsage": excelMcbUsage,
       "excelRegionTable": excelRegionTable,
       "excelRegionEntry": excelRegionEntry,
       "excelRegionIndex": excelRegionIndex,
       "excelRegionId": excelRegionId,
       "excelRegionSize": excelRegionSize,
       "excelRegionUsed": excelRegionUsed,
       "excelPartitionTable": excelPartitionTable,
       "excelPartitionEntry": excelPartitionEntry,
       "excelPartitionIndex": excelPartitionIndex,
       "excelPartitionId": excelPartitionId,
       "excelPartitionSize": excelPartitionSize,
       "excelPartitionUsed": excelPartitionUsed,
       "excelCpuUsageTable": excelCpuUsageTable,
       "excelCpuUsageEntry": excelCpuUsageEntry,
       "excelCpuUsageIndex": excelCpuUsageIndex,
       "excelCpuUsageTaskId": excelCpuUsageTaskId,
       "excelCpuUsageUsed": excelCpuUsageUsed,
       "excelNodeSoftware": excelNodeSoftware,
       "excelSystemSoftware": excelSystemSoftware,
       "excelSystemConfig": excelSystemConfig,
       "excelSystemAlarm": excelSystemAlarm,
       "excelSysLastAlarmTrap": excelSysLastAlarmTrap,
       "excelSysLastAlarmSeverity": excelSysLastAlarmSeverity,
       "excelSysLastAlarmNode": excelSysLastAlarmNode,
       "excelSysLastAlarmStatus": excelSysLastAlarmStatus,
       "excelSysLastAlarmDSPLastBlocked": excelSysLastAlarmDSPLastBlocked,
       "excelSysLastAlarmRefClockSrc": excelSysLastAlarmRefClockSrc,
       "excelRing": excelRing,
       "excelRingTable": excelRingTable,
       "excelRingEntry": excelRingEntry,
       "excelRingLogicalIDIndex": excelRingLogicalIDIndex,
       "excelRingStatus": excelRingStatus,
       "excelRingOOSReason": excelRingOOSReason,
       "excelRingTransmitMode": excelRingTransmitMode,
       "excelRingNodeRole": excelRingNodeRole,
       "excelRingCtrlSlot": excelRingCtrlSlot,
       "excelRingPortAStatus": excelRingPortAStatus,
       "excelRingPortBStatus": excelRingPortBStatus,
       "excelRingSourcePacketID": excelRingSourcePacketID,
       "excelRingNodeStatus": excelRingNodeStatus,
       "ringID": ringID,
       "ringStatusTable": ringStatusTable,
       "ringStatusTableEntry": ringStatusTableEntry,
       "ringStatusIndex": ringStatusIndex,
       "ringStatusTransmitting": ringStatusTransmitting,
       "ringStatusIpAddress": ringStatusIpAddress,
       "ringStatusLogicalId": ringStatusLogicalId,
       "ringStatusPhysicalId": ringStatusPhysicalId,
       "ringStatusLoadMajorRev": ringStatusLoadMajorRev,
       "ringStatusLoadMinorRev": ringStatusLoadMinorRev,
       "ringStatusLoadBuildNum": ringStatusLoadBuildNum,
       "excelCommunicationSoftware": excelCommunicationSoftware,
       "excelMatrix": excelMatrix,
       "excelMtxTable": excelMtxTable,
       "excelMtxEntry": excelMtxEntry,
       "excelMtxSlotIndex": excelMtxSlotIndex,
       "excelMtxPosition": excelMtxPosition,
       "excelMtxType": excelMtxType,
       "excelMtxState": excelMtxState,
       "excelMtxAdjacentMatrixStatus": excelMtxAdjacentMatrixStatus,
       "excelMtxHostLink": excelMtxHostLink,
       "excelMtxRamLoadPresent": excelMtxRamLoadPresent,
       "excelMtxReadyForConfiguration": excelMtxReadyForConfiguration,
       "excelMtxIpAddress": excelMtxIpAddress,
       "excelMtxBootMajorVersion": excelMtxBootMajorVersion,
       "excelMtxBootMinorVersion": excelMtxBootMinorVersion,
       "excelMtxSystemSoftwareMajor": excelMtxSystemSoftwareMajor,
       "excelMtxSystemSoftwareMinor": excelMtxSystemSoftwareMinor,
       "excelMtxSystemSoftwareBuild": excelMtxSystemSoftwareBuild,
       "excelMtxSecIpAddress": excelMtxSecIpAddress,
       "excelMatrixManagement": excelMatrixManagement,
       "excelMatrixSwitchOver": excelMatrixSwitchOver,
       "excelMatrixSwitchOverTime": excelMatrixSwitchOverTime,
       "excelExnetConnect": excelExnetConnect,
       "excelExnetConnectTable": excelExnetConnectTable,
       "excelExnetConnectEntry": excelExnetConnectEntry,
       "excelExnetConnectLogicalNodeIDIndex": excelExnetConnectLogicalNodeIDIndex,
       "excelExnetConnectClockMaster": excelExnetConnectClockMaster,
       "excelExnetConnectClockSpeed": excelExnetConnectClockSpeed,
       "excelSpans": excelSpans,
       "excelGeneralSpan": excelGeneralSpan,
       "excelSpanTable": excelSpanTable,
       "excelSpanEntry": excelSpanEntry,
       "excelSpanTableIndex": excelSpanTableIndex,
       "excelLogicalSpanId": excelLogicalSpanId,
       "excelSpanBipolarViolation": excelSpanBipolarViolation,
       "excelSpanFrameErrors": excelSpanFrameErrors,
       "excelSpanSlipErrors": excelSpanSlipErrors,
       "excelSpanLossofFrame": excelSpanLossofFrame,
       "excelSpanManagement": excelSpanManagement,
       "excelCurrentSpanId": excelCurrentSpanId,
       "excelSpanAction": excelSpanAction,
       "excelChannelAction": excelChannelAction,
       "excelSS7": excelSS7,
       "excelSS7Config": excelSS7Config,
       "excelSS7CardTable": excelSS7CardTable,
       "excelSS7CardEntry": excelSS7CardEntry,
       "excelSS7CardSlotNumberIndex": excelSS7CardSlotNumberIndex,
       "excelSS7CardRedundancyConfiguredRole": excelSS7CardRedundancyConfiguredRole,
       "excelSS7CardRedundancyCurrentRole": excelSS7CardRedundancyCurrentRole,
       "excelSS7CardRedundancyMate": excelSS7CardRedundancyMate,
       "excelSS7CardRedundancyStatus": excelSS7CardRedundancyStatus,
       "excelSS7CardStackID1": excelSS7CardStackID1,
       "excelSS7CardStackID2": excelSS7CardStackID2,
       "excelSS7CardStackID3": excelSS7CardStackID3,
       "excelSS7CardStackID4": excelSS7CardStackID4,
       "excelSS7CardMaximumLinks": excelSS7CardMaximumLinks,
       "excelSS7ConfigLinkTable": excelSS7ConfigLinkTable,
       "excelSS7LinkEntry": excelSS7LinkEntry,
       "excelSS7LinkStackIndex": excelSS7LinkStackIndex,
       "excelSS7LinkLinkIndex": excelSS7LinkLinkIndex,
       "excelSS7LinkLinkSetIndex": excelSS7LinkLinkSetIndex,
       "excelSS7LinkStatus": excelSS7LinkStatus,
       "excelSS7LinkSignalingLinkCode": excelSS7LinkSignalingLinkCode,
       "excelSS7LinkDataRate": excelSS7LinkDataRate,
       "excelSS7LinkLogicalSpanID": excelSS7LinkLogicalSpanID,
       "excelSS7Linkchannel": excelSS7Linkchannel,
       "excelSS7StackTable": excelSS7StackTable,
       "excelSS7StackEntry": excelSS7StackEntry,
       "excelSS7StackIDIndex": excelSS7StackIDIndex,
       "excelSS7StackOPC": excelSS7StackOPC,
       "excelSS7StackMTPVariant": excelSS7StackMTPVariant,
       "excelSS7StackISUPVariant": excelSS7StackISUPVariant,
       "excelSS7StackL3PVariant": excelSS7StackL3PVariant,
       "excelSS7StackTUPVariant": excelSS7StackTUPVariant,
       "excelSS7StackL3PTUPVariant": excelSS7StackL3PTUPVariant,
       "excelSS7LinkSetTable": excelSS7LinkSetTable,
       "excelSS7LinkSetEntry": excelSS7LinkSetEntry,
       "excelSS7LinkSetIDIndex": excelSS7LinkSetIDIndex,
       "excelSS7LinkSetStatus": excelSS7LinkSetStatus,
       "excelSS7LinkSetAPC": excelSS7LinkSetAPC,
       "excelSS7LinkSetStackIDIndex": excelSS7LinkSetStackIDIndex,
       "excelSS7Statistics": excelSS7Statistics,
       "excelPPL": excelPPL,
       "excelPPLComponentId": excelPPLComponentId,
       "excelPPLComponentStatistics": excelPPLComponentStatistics,
       "excelL3PCICTable": excelL3PCICTable,
       "excelL3PCICEntry": excelL3PCICEntry,
       "excelL3PCICIndex": excelL3PCICIndex,
       "excelL3PCICSpanID": excelL3PCICSpanID,
       "excelL3PCICChannelID": excelL3PCICChannelID,
       "excelL3PCICEventID": excelL3PCICEventID,
       "excelL3PCICTime": excelL3PCICTime,
       "excelL3PCICCount": excelL3PCICCount,
       "excelL3PCICStatus": excelL3PCICStatus,
       "excelL3PLinkTable": excelL3PLinkTable,
       "excelL3PLinkEntry": excelL3PLinkEntry,
       "excelL3PLinkIndex": excelL3PLinkIndex,
       "excelL3PLinkSpanID": excelL3PLinkSpanID,
       "excelL3PLinkChannelID": excelL3PLinkChannelID,
       "excelL3PLinkEventID": excelL3PLinkEventID,
       "excelL3PLinkTime": excelL3PLinkTime,
       "excelL3PLinkCount": excelL3PLinkCount,
       "excelL3PLinkStatus": excelL3PLinkStatus,
       "excelCPCTable": excelCPCTable,
       "excelCPCEntry": excelCPCEntry,
       "excelCPCIndex": excelCPCIndex,
       "excelCPCSpanID": excelCPCSpanID,
       "excelCPCChannelID": excelCPCChannelID,
       "excelCPCEventID": excelCPCEventID,
       "excelCPCTime": excelCPCTime,
       "excelCPCCount": excelCPCCount,
       "excelCPCStatus": excelCPCStatus,
       "excelSPRCTable": excelSPRCTable,
       "excelSPRCEntry": excelSPRCEntry,
       "excelSPRCIndex": excelSPRCIndex,
       "excelSPRCSpanID": excelSPRCSpanID,
       "excelSPRCChannelID": excelSPRCChannelID,
       "excelSPRCEventID": excelSPRCEventID,
       "excelSPRCTime": excelSPRCTime,
       "excelSPRCCount": excelSPRCCount,
       "excelSPRCStatus": excelSPRCStatus,
       "excelUCICTable": excelUCICTable,
       "excelUCICEntry": excelUCICEntry,
       "excelUCICIndex": excelUCICIndex,
       "excelUCICSpanID": excelUCICSpanID,
       "excelUCICChannelID": excelUCICChannelID,
       "excelUCICEventID": excelUCICEventID,
       "excelUCICTime": excelUCICTime,
       "excelUCICCount": excelUCICCount,
       "excelUCICStatus": excelUCICStatus,
       "excelHMDTTable": excelHMDTTable,
       "excelHMDTEntry": excelHMDTEntry,
       "excelHMDTIndex": excelHMDTIndex,
       "excelHMDTSpanID": excelHMDTSpanID,
       "excelHMDTChannelID": excelHMDTChannelID,
       "excelHMDTEventID": excelHMDTEventID,
       "excelHMDTTime": excelHMDTTime,
       "excelHMDTCount": excelHMDTCount,
       "excelHMDTStatus": excelHMDTStatus,
       "excelLSACTable": excelLSACTable,
       "excelLSACEntry": excelLSACEntry,
       "excelLSACIndex": excelLSACIndex,
       "excelLSACSpanID": excelLSACSpanID,
       "excelLSACChannelID": excelLSACChannelID,
       "excelLSACEventID": excelLSACEventID,
       "excelLSACTime": excelLSACTime,
       "excelLSACCount": excelLSACCount,
       "excelLSACStatus": excelLSACStatus,
       "excelTLACTable": excelTLACTable,
       "excelTLACEntry": excelTLACEntry,
       "excelTLACIndex": excelTLACIndex,
       "excelTLACSpanID": excelTLACSpanID,
       "excelTLACChannelID": excelTLACChannelID,
       "excelTLACEventID": excelTLACEventID,
       "excelTLACTime": excelTLACTime,
       "excelTLACCount": excelTLACCount,
       "excelTLACStatus": excelTLACStatus,
       "excelTSFCTable": excelTSFCTable,
       "excelTSFCEntry": excelTSFCEntry,
       "excelTSFCIndex": excelTSFCIndex,
       "excelTSFCSpanID": excelTSFCSpanID,
       "excelTSFCChannelID": excelTSFCChannelID,
       "excelTSFCEventID": excelTSFCEventID,
       "excelTSFCTime": excelTSFCTime,
       "excelTSFCCount": excelTSFCCount,
       "excelTSFCStatus": excelTSFCStatus,
       "excelCROTable": excelCROTable,
       "excelCROEntry": excelCROEntry,
       "excelCROIndex": excelCROIndex,
       "excelCROSpanID": excelCROSpanID,
       "excelCROChannelID": excelCROChannelID,
       "excelCROEventID": excelCROEventID,
       "excelCROTime": excelCROTime,
       "excelCROCount": excelCROCount,
       "excelCROStatus": excelCROStatus,
       "excelISDN": excelISDN,
       "excelISDNConfig": excelISDNConfig,
       "excelISDNConfigDChanTable": excelISDNConfigDChanTable,
       "excelISDNConfigDChanEntry": excelISDNConfigDChanEntry,
       "excelISDNConfigDChanSpanIndex": excelISDNConfigDChanSpanIndex,
       "excelISDNConfigDChanIndex": excelISDNConfigDChanIndex,
       "excelISDNConfigDChanConnType": excelISDNConfigDChanConnType,
       "excelISDNConfigDChanHDLCBitPol": excelISDNConfigDChanHDLCBitPol,
       "excelISDNConfigDChanBChanSelect": excelISDNConfigDChanBChanSelect,
       "excelISDNConfigDChanBChanEncTrans": excelISDNConfigDChanBChanEncTrans,
       "excelISDNConfigDChanLocation": excelISDNConfigDChanLocation,
       "excelISDNConfigDChanPhysicalMedium": excelISDNConfigDChanPhysicalMedium,
       "excelMediaGateway": excelMediaGateway,
       "excelMGSystem": excelMGSystem,
       "excelMGActiveProtocol": excelMGActiveProtocol,
       "excelMGSystemName": excelMGSystemName,
       "excelMGNumSlots": excelMGNumSlots,
       "excelMGVoip": excelMGVoip,
       "excelVoipAddressTable": excelVoipAddressTable,
       "excelVoipAddressEntry": excelVoipAddressEntry,
       "excelVoipAddressIndex": excelVoipAddressIndex,
       "excelVoipAddressEntityType": excelVoipAddressEntityType,
       "excelVoipIpAddress": excelVoipIpAddress,
       "excelVoipSubNetMask": excelVoipSubNetMask,
       "excelVoipIpGateway": excelVoipIpGateway,
       "excelVoipResetIndicator": excelVoipResetIndicator,
       "excelMGResAttrIpAddress": excelMGResAttrIpAddress,
       "excelMGResourceAttributeTable": excelMGResourceAttributeTable,
       "excelMGResourceAttributeEntry": excelMGResourceAttributeEntry,
       "excelMGResAttrIndex": excelMGResAttrIndex,
       "excelMGPayloadType": excelMGPayloadType,
       "excelMGPayloadSize": excelMGPayloadSize,
       "excelMGSilenceSupression": excelMGSilenceSupression,
       "excelMGEchoCancellation": excelMGEchoCancellation,
       "excelMGMinDelayValue": excelMGMinDelayValue,
       "excelMGMaxDelayValue": excelMGMaxDelayValue,
       "excelMGAdaptionRate": excelMGAdaptionRate,
       "excelMGFaxType": excelMGFaxType,
       "excelMGModemEnableTransport": excelMGModemEnableTransport,
       "excelMGBypassCoderType": excelMGBypassCoderType,
       "excelMGRtpPacketDepth": excelMGRtpPacketDepth,
       "excelMGFaxPacketDepth": excelMGFaxPacketDepth,
       "excelMGModemPacketDepth": excelMGModemPacketDepth,
       "excelMGTypeOfServicePrecedence": excelMGTypeOfServicePrecedence,
       "excelMGTypeOServiceDelay": excelMGTypeOServiceDelay,
       "excelMGTypeOfServiceThroughput": excelMGTypeOfServiceThroughput,
       "excelMGTypeOfServiceReliability": excelMGTypeOfServiceReliability,
       "excelMGTypeOfServiceCost": excelMGTypeOfServiceCost,
       "excelMGRtcpPortOffset": excelMGRtcpPortOffset,
       "excelMGT38PortOffset": excelMGT38PortOffset,
       "excelMGConfig": excelMGConfig,
       "excelMGConfigPrimaryMGCAddress": excelMGConfigPrimaryMGCAddress,
       "excelMGConfigPrimaryPort": excelMGConfigPrimaryPort,
       "excelMGConfigSecondaryMGCAddress": excelMGConfigSecondaryMGCAddress,
       "excelMGConfigSecondaryPort": excelMGConfigSecondaryPort,
       "excelMGConfigLocalPort": excelMGConfigLocalPort,
       "excelMGConfigIpdc": excelMGConfigIpdc,
       "excelMGConfigIpdcReconnectAttempts": excelMGConfigIpdcReconnectAttempts,
       "excelMGConfigMgcp": excelMGConfigMgcp,
       "excelConfigMgcpPriTransmitInterval": excelConfigMgcpPriTransmitInterval,
       "excelConfigMgcpSecTransmitInterval": excelConfigMgcpSecTransmitInterval,
       "excelConfigMgcpResponseInterval": excelConfigMgcpResponseInterval,
       "excelConfigMgcpRetransmissionTime": excelConfigMgcpRetransmissionTime,
       "excelOAMP": excelOAMP,
       "excelEXSAgentVerbose": excelEXSAgentVerbose,
       "excelEXSEventManagerVerbose": excelEXSEventManagerVerbose,
       "excelExtension": excelExtension}
)

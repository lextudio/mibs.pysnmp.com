# SNMP MIB module (LANOPTICS-HUB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANOPTICS-HUB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:14 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class BITMAP(Integer32):
    """Custom type BITMAP based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LanOptics_ObjectIdentity = ObjectIdentity
lanOptics = _LanOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224)
)
_LanOpticsHub_ObjectIdentity = ObjectIdentity
lanOpticsHub = _LanOpticsHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 1)
)


class _SnMaxSlots_Type(Integer32):
    """Custom type snMaxSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SnMaxSlots_Type.__name__ = "Integer32"
_SnMaxSlots_Object = MibScalar
snMaxSlots = _SnMaxSlots_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 1),
    _SnMaxSlots_Type()
)
snMaxSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMaxSlots.setStatus("mandatory")
_SnSlotsNum_Type = Integer32
_SnSlotsNum_Object = MibScalar
snSlotsNum = _SnSlotsNum_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 2),
    _SnSlotsNum_Type()
)
snSlotsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSlotsNum.setStatus("mandatory")
_SnConfig_Type = DisplayString
_SnConfig_Object = MibScalar
snConfig = _SnConfig_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 3),
    _SnConfig_Type()
)
snConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snConfig.setStatus("mandatory")


class _SnLLActiveNMS_Type(Integer32):
    """Custom type snLLActiveNMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_SnLLActiveNMS_Type.__name__ = "Integer32"
_SnLLActiveNMS_Object = MibScalar
snLLActiveNMS = _SnLLActiveNMS_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 4),
    _SnLLActiveNMS_Type()
)
snLLActiveNMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snLLActiveNMS.setStatus("mandatory")
_SnReset_Type = Integer32
_SnReset_Object = MibScalar
snReset = _SnReset_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 5),
    _SnReset_Type()
)
snReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snReset.setStatus("mandatory")
_SnInternalID_Type = DisplayString
_SnInternalID_Object = MibScalar
snInternalID = _SnInternalID_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 6),
    _SnInternalID_Type()
)
snInternalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snInternalID.setStatus("mandatory")
_SnDirtyBit_Type = BITMAP
_SnDirtyBit_Object = MibScalar
snDirtyBit = _SnDirtyBit_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 7),
    _SnDirtyBit_Type()
)
snDirtyBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snDirtyBit.setStatus("mandatory")
_SnSlotsTable_Object = MibTable
snSlotsTable = _SnSlotsTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8)
)
if mibBuilder.loadTexts:
    snSlotsTable.setStatus("mandatory")
_SnSlotsEntry_Object = MibTableRow
snSlotsEntry = _SnSlotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1)
)
snSlotsEntry.setIndexNames(
    (0, "LANOPTICS-HUB-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    snSlotsEntry.setStatus("mandatory")
_SnCardName_Type = DisplayString
_SnCardName_Object = MibTableColumn
snCardName = _SnCardName_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1, 1),
    _SnCardName_Type()
)
snCardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snCardName.setStatus("mandatory")
_SnCardDescr_Type = DisplayString
_SnCardDescr_Object = MibTableColumn
snCardDescr = _SnCardDescr_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1, 2),
    _SnCardDescr_Type()
)
snCardDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snCardDescr.setStatus("mandatory")
_SnLLHwRevision_Type = Integer32
_SnLLHwRevision_Object = MibTableColumn
snLLHwRevision = _SnLLHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1, 9),
    _SnLLHwRevision_Type()
)
snLLHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snLLHwRevision.setStatus("mandatory")
_SnLLSwRevision_Type = Integer32
_SnLLSwRevision_Object = MibTableColumn
snLLSwRevision = _SnLLSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1, 10),
    _SnLLSwRevision_Type()
)
snLLSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snLLSwRevision.setStatus("mandatory")
_SnLLControl0_Type = BITMAP
_SnLLControl0_Object = MibTableColumn
snLLControl0 = _SnLLControl0_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1, 14),
    _SnLLControl0_Type()
)
snLLControl0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snLLControl0.setStatus("mandatory")
_SnLLControl1_Type = BITMAP
_SnLLControl1_Object = MibTableColumn
snLLControl1 = _SnLLControl1_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1, 15),
    _SnLLControl1_Type()
)
snLLControl1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snLLControl1.setStatus("mandatory")
_SnPollInf_Type = OctetString
_SnPollInf_Object = MibTableColumn
snPollInf = _SnPollInf_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1, 29),
    _SnPollInf_Type()
)
snPollInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPollInf.setStatus("mandatory")
_SnResetSlot_Type = Integer32
_SnResetSlot_Object = MibTableColumn
snResetSlot = _SnResetSlot_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1, 38),
    _SnResetSlot_Type()
)
snResetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snResetSlot.setStatus("mandatory")
_SnPollInfCode_Type = OctetString
_SnPollInfCode_Object = MibTableColumn
snPollInfCode = _SnPollInfCode_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1, 41),
    _SnPollInfCode_Type()
)
snPollInfCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPollInfCode.setStatus("mandatory")
_SnAssCode_Type = OctetString
_SnAssCode_Object = MibTableColumn
snAssCode = _SnAssCode_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1, 42),
    _SnAssCode_Type()
)
snAssCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAssCode.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 8, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_SnPairAddress_Type = Integer32
_SnPairAddress_Object = MibScalar
snPairAddress = _SnPairAddress_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 9),
    _SnPairAddress_Type()
)
snPairAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPairAddress.setStatus("mandatory")
_SnPairData_Type = Integer32
_SnPairData_Object = MibScalar
snPairData = _SnPairData_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 10),
    _SnPairData_Type()
)
snPairData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPairData.setStatus("mandatory")
_SnHubSplitTable_Object = MibTable
snHubSplitTable = _SnHubSplitTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 11)
)
if mibBuilder.loadTexts:
    snHubSplitTable.setStatus("mandatory")
_SnHubSplitEntry_Object = MibTableRow
snHubSplitEntry = _SnHubSplitEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 11, 1)
)
snHubSplitEntry.setIndexNames(
    (0, "LANOPTICS-HUB-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    snHubSplitEntry.setStatus("mandatory")


class _SnHubSplitStatus_Type(Integer32):
    """Custom type snHubSplitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 2),
          ("splitted", 1))
    )


_SnHubSplitStatus_Type.__name__ = "Integer32"
_SnHubSplitStatus_Object = MibTableColumn
snHubSplitStatus = _SnHubSplitStatus_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 11, 1, 1),
    _SnHubSplitStatus_Type()
)
snHubSplitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snHubSplitStatus.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 11, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_SnHubPSTable_Object = MibTable
snHubPSTable = _SnHubPSTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 12)
)
if mibBuilder.loadTexts:
    snHubPSTable.setStatus("mandatory")
_SnHubPSEntry_Object = MibTableRow
snHubPSEntry = _SnHubPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 12, 1)
)
snHubPSEntry.setIndexNames(
    (0, "LANOPTICS-HUB-MIB", "pysmiFakeCol3"),
)
if mibBuilder.loadTexts:
    snHubPSEntry.setStatus("mandatory")


class _SnHubPSStatus_Type(Integer32):
    """Custom type snHubPSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("malfunctioning", 1),
          ("missing", 2))
    )


_SnHubPSStatus_Type.__name__ = "Integer32"
_SnHubPSStatus_Object = MibTableColumn
snHubPSStatus = _SnHubPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 12, 1, 1),
    _SnHubPSStatus_Type()
)
snHubPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snHubPSStatus.setStatus("mandatory")
_PysmiFakeCol3_Type = Integer32
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 12, 1, 4294967295),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")
_SnHubFanTable_Object = MibTable
snHubFanTable = _SnHubFanTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 13)
)
if mibBuilder.loadTexts:
    snHubFanTable.setStatus("mandatory")
_SnHubFanEntry_Object = MibTableRow
snHubFanEntry = _SnHubFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 13, 1)
)
snHubFanEntry.setIndexNames(
    (0, "LANOPTICS-HUB-MIB", "pysmiFakeCol4"),
)
if mibBuilder.loadTexts:
    snHubFanEntry.setStatus("mandatory")


class _SnHubFanStatus_Type(Integer32):
    """Custom type snHubFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("malfunctioning", 1),
          ("missing", 2))
    )


_SnHubFanStatus_Type.__name__ = "Integer32"
_SnHubFanStatus_Object = MibTableColumn
snHubFanStatus = _SnHubFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 13, 1, 1),
    _SnHubFanStatus_Type()
)
snHubFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snHubFanStatus.setStatus("mandatory")
_PysmiFakeCol4_Type = Integer32
_PysmiFakeCol4_Object = MibTableColumn
pysmiFakeCol4 = _PysmiFakeCol4_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 13, 1, 4294967295),
    _PysmiFakeCol4_Type()
)
pysmiFakeCol4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol4.setStatus("mandatory")
_SnHubSlotsTable_Object = MibTable
snHubSlotsTable = _SnHubSlotsTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 14)
)
if mibBuilder.loadTexts:
    snHubSlotsTable.setStatus("mandatory")
_SnHubSlotsEntry_Object = MibTableRow
snHubSlotsEntry = _SnHubSlotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 14, 1)
)
snHubSlotsEntry.setIndexNames(
    (0, "LANOPTICS-HUB-MIB", "pysmiFakeCol5"),
)
if mibBuilder.loadTexts:
    snHubSlotsEntry.setStatus("mandatory")


class _SnHubSlotConnected_Type(Integer32):
    """Custom type snHubSlotConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disconnected", 1)
    )


_SnHubSlotConnected_Type.__name__ = "Integer32"
_SnHubSlotConnected_Object = MibTableColumn
snHubSlotConnected = _SnHubSlotConnected_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 14, 1, 1),
    _SnHubSlotConnected_Type()
)
snHubSlotConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snHubSlotConnected.setStatus("mandatory")


class _SnHubSlotFreqError_Type(Integer32):
    """Custom type snHubSlotFreqError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("slot-16M", 16),
          ("slot-4M", 4))
    )


_SnHubSlotFreqError_Type.__name__ = "Integer32"
_SnHubSlotFreqError_Object = MibTableColumn
snHubSlotFreqError = _SnHubSlotFreqError_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 14, 1, 2),
    _SnHubSlotFreqError_Type()
)
snHubSlotFreqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snHubSlotFreqError.setStatus("mandatory")


class _SnHubSlotRevChanged_Type(Integer32):
    """Custom type snHubSlotRevChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unchanged", 1)
    )


_SnHubSlotRevChanged_Type.__name__ = "Integer32"
_SnHubSlotRevChanged_Object = MibTableColumn
snHubSlotRevChanged = _SnHubSlotRevChanged_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 14, 1, 3),
    _SnHubSlotRevChanged_Type()
)
snHubSlotRevChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snHubSlotRevChanged.setStatus("mandatory")
_PysmiFakeCol5_Type = Integer32
_PysmiFakeCol5_Object = MibTableColumn
pysmiFakeCol5 = _PysmiFakeCol5_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 14, 1, 4294967295),
    _PysmiFakeCol5_Type()
)
pysmiFakeCol5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol5.setStatus("mandatory")
_SnCompanionHW_Type = Integer32
_SnCompanionHW_Object = MibScalar
snCompanionHW = _SnCompanionHW_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 15),
    _SnCompanionHW_Type()
)
snCompanionHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCompanionHW.setStatus("mandatory")
_SnCompanionReset_Type = Integer32
_SnCompanionReset_Object = MibScalar
snCompanionReset = _SnCompanionReset_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 16),
    _SnCompanionReset_Type()
)
snCompanionReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snCompanionReset.setStatus("mandatory")
_SnCompanionStatus_Type = BITMAP
_SnCompanionStatus_Object = MibScalar
snCompanionStatus = _SnCompanionStatus_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 17),
    _SnCompanionStatus_Type()
)
snCompanionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCompanionStatus.setStatus("mandatory")
_SnGenPortsTable_Object = MibTable
snGenPortsTable = _SnGenPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 18)
)
if mibBuilder.loadTexts:
    snGenPortsTable.setStatus("mandatory")
_SnGenPortsEntry_Object = MibTableRow
snGenPortsEntry = _SnGenPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 18, 1)
)
snGenPortsEntry.setIndexNames(
    (0, "LANOPTICS-HUB-MIB", "pysmiFakeCol6"),
    (0, "LANOPTICS-HUB-MIB", "pysmiFakeCol7"),
)
if mibBuilder.loadTexts:
    snGenPortsEntry.setStatus("mandatory")
_SnPortValue_Type = BITMAP
_SnPortValue_Object = MibTableColumn
snPortValue = _SnPortValue_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 18, 1, 1),
    _SnPortValue_Type()
)
snPortValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPortValue.setStatus("mandatory")
_PysmiFakeCol7_Type = Integer32
_PysmiFakeCol7_Object = MibTableColumn
pysmiFakeCol7 = _PysmiFakeCol7_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 18, 1, 4294967294),
    _PysmiFakeCol7_Type()
)
pysmiFakeCol7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol7.setStatus("mandatory")
_PysmiFakeCol6_Type = Integer32
_PysmiFakeCol6_Object = MibTableColumn
pysmiFakeCol6 = _PysmiFakeCol6_Object(
    (1, 3, 6, 1, 4, 1, 224, 1, 18, 1, 4294967295),
    _PysmiFakeCol6_Type()
)
pysmiFakeCol6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol6.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANOPTICS-HUB-MIB",
    **{"BITMAP": BITMAP,
       "lanOptics": lanOptics,
       "lanOpticsHub": lanOpticsHub,
       "snMaxSlots": snMaxSlots,
       "snSlotsNum": snSlotsNum,
       "snConfig": snConfig,
       "snLLActiveNMS": snLLActiveNMS,
       "snReset": snReset,
       "snInternalID": snInternalID,
       "snDirtyBit": snDirtyBit,
       "snSlotsTable": snSlotsTable,
       "snSlotsEntry": snSlotsEntry,
       "snCardName": snCardName,
       "snCardDescr": snCardDescr,
       "snLLHwRevision": snLLHwRevision,
       "snLLSwRevision": snLLSwRevision,
       "snLLControl0": snLLControl0,
       "snLLControl1": snLLControl1,
       "snPollInf": snPollInf,
       "snResetSlot": snResetSlot,
       "snPollInfCode": snPollInfCode,
       "snAssCode": snAssCode,
       "pysmiFakeCol1": pysmiFakeCol1,
       "snPairAddress": snPairAddress,
       "snPairData": snPairData,
       "snHubSplitTable": snHubSplitTable,
       "snHubSplitEntry": snHubSplitEntry,
       "snHubSplitStatus": snHubSplitStatus,
       "pysmiFakeCol2": pysmiFakeCol2,
       "snHubPSTable": snHubPSTable,
       "snHubPSEntry": snHubPSEntry,
       "snHubPSStatus": snHubPSStatus,
       "pysmiFakeCol3": pysmiFakeCol3,
       "snHubFanTable": snHubFanTable,
       "snHubFanEntry": snHubFanEntry,
       "snHubFanStatus": snHubFanStatus,
       "pysmiFakeCol4": pysmiFakeCol4,
       "snHubSlotsTable": snHubSlotsTable,
       "snHubSlotsEntry": snHubSlotsEntry,
       "snHubSlotConnected": snHubSlotConnected,
       "snHubSlotFreqError": snHubSlotFreqError,
       "snHubSlotRevChanged": snHubSlotRevChanged,
       "pysmiFakeCol5": pysmiFakeCol5,
       "snCompanionHW": snCompanionHW,
       "snCompanionReset": snCompanionReset,
       "snCompanionStatus": snCompanionStatus,
       "snGenPortsTable": snGenPortsTable,
       "snGenPortsEntry": snGenPortsEntry,
       "snPortValue": snPortValue,
       "pysmiFakeCol7": pysmiFakeCol7,
       "pysmiFakeCol6": pysmiFakeCol6}
)

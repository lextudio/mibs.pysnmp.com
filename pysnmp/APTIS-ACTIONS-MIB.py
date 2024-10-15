# SNMP MIB module (APTIS-ACTIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APTIS-ACTIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:03 2024
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

(Boolean,
 aptis_actions) = mibBuilder.importSymbols(
    "APTIS-MIB",
    "Boolean",
    "aptis-actions")

(aptis_modules,) = mibBuilder.importSymbols(
    "APTIS-REG-MIB",
    "aptis-modules")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

aptisActionsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlotControlTable_Object = MibTable
slotControlTable = _SlotControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 203)
)
if mibBuilder.loadTexts:
    slotControlTable.setStatus("current")
_SlotControlEntry_Object = MibTableRow
slotControlEntry = _SlotControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 203, 1)
)
slotControlEntry.setIndexNames(
    (0, "APTIS-ACTIONS-MIB", "slotControlInstance"),
)
if mibBuilder.loadTexts:
    slotControlEntry.setStatus("current")


class _SlotControlInstance_Type(Integer32):
    """Custom type slotControlInstance based on Integer32"""
    defaultValue = 0


_SlotControlInstance_Object = MibTableColumn
slotControlInstance = _SlotControlInstance_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 203, 1, 1),
    _SlotControlInstance_Type()
)
slotControlInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slotControlInstance.setStatus("current")


class _SlotControlStatusGeneral_Type(Integer32):
    """Custom type slotControlStatusGeneral based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("errParam", 4),
          ("failed", 2),
          ("started", 0),
          ("succeeded", 1))
    )


_SlotControlStatusGeneral_Type.__name__ = "Integer32"
_SlotControlStatusGeneral_Object = MibTableColumn
slotControlStatusGeneral = _SlotControlStatusGeneral_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 203, 1, 2),
    _SlotControlStatusGeneral_Type()
)
slotControlStatusGeneral.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slotControlStatusGeneral.setStatus("current")


class _SlotControlStatusSpecific_Type(Integer32):
    """Custom type slotControlStatusSpecific based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("badSlot", 3),
          ("inUse", 4),
          ("inappropriate", 5),
          ("noCard", 1),
          ("notAllowed", 2),
          ("unknown", 0))
    )


_SlotControlStatusSpecific_Type.__name__ = "Integer32"
_SlotControlStatusSpecific_Object = MibTableColumn
slotControlStatusSpecific = _SlotControlStatusSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 203, 1, 3),
    _SlotControlStatusSpecific_Type()
)
slotControlStatusSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slotControlStatusSpecific.setStatus("current")


class _SlotControlSlotIndex_Type(Integer32):
    """Custom type slotControlSlotIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_SlotControlSlotIndex_Type.__name__ = "Integer32"
_SlotControlSlotIndex_Object = MibTableColumn
slotControlSlotIndex = _SlotControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 203, 1, 11),
    _SlotControlSlotIndex_Type()
)
slotControlSlotIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slotControlSlotIndex.setStatus("current")


class _SlotControlSlotAction_Type(Integer32):
    """Custom type slotControlSlotAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("slotAbortDry", 6),
          ("slotDown", 1),
          ("slotDownPend", 2),
          ("slotDownTimed", 5),
          ("slotNoChange", 0),
          ("slotReset", 4),
          ("slotUp", 3))
    )


_SlotControlSlotAction_Type.__name__ = "Integer32"
_SlotControlSlotAction_Object = MibTableColumn
slotControlSlotAction = _SlotControlSlotAction_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 203, 1, 12),
    _SlotControlSlotAction_Type()
)
slotControlSlotAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slotControlSlotAction.setStatus("current")
_SessionTerminateTable_Object = MibTable
sessionTerminateTable = _SessionTerminateTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 230)
)
if mibBuilder.loadTexts:
    sessionTerminateTable.setStatus("current")
_SessionTerminateEntry_Object = MibTableRow
sessionTerminateEntry = _SessionTerminateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 230, 1)
)
sessionTerminateEntry.setIndexNames(
    (0, "APTIS-ACTIONS-MIB", "sessionTerminateInstance"),
)
if mibBuilder.loadTexts:
    sessionTerminateEntry.setStatus("current")


class _SessionTerminateInstance_Type(Integer32):
    """Custom type sessionTerminateInstance based on Integer32"""
    defaultValue = 0


_SessionTerminateInstance_Object = MibTableColumn
sessionTerminateInstance = _SessionTerminateInstance_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 230, 1, 1),
    _SessionTerminateInstance_Type()
)
sessionTerminateInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sessionTerminateInstance.setStatus("current")


class _SessionTerminateStatusGeneral_Type(Integer32):
    """Custom type sessionTerminateStatusGeneral based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("errParam", 4),
          ("failed", 2),
          ("started", 0),
          ("succeeded", 1))
    )


_SessionTerminateStatusGeneral_Type.__name__ = "Integer32"
_SessionTerminateStatusGeneral_Object = MibTableColumn
sessionTerminateStatusGeneral = _SessionTerminateStatusGeneral_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 230, 1, 2),
    _SessionTerminateStatusGeneral_Type()
)
sessionTerminateStatusGeneral.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sessionTerminateStatusGeneral.setStatus("current")


class _SessionTerminateStatusSpecific_Type(Integer32):
    """Custom type sessionTerminateStatusSpecific based on Integer32"""
    defaultValue = 0

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
        *(("badSession", 2),
          ("badSignature", 1),
          ("genFail", 3),
          ("noError", 0))
    )


_SessionTerminateStatusSpecific_Type.__name__ = "Integer32"
_SessionTerminateStatusSpecific_Object = MibTableColumn
sessionTerminateStatusSpecific = _SessionTerminateStatusSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 230, 1, 3),
    _SessionTerminateStatusSpecific_Type()
)
sessionTerminateStatusSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sessionTerminateStatusSpecific.setStatus("current")


class _SessionTerminateBootEra_Type(Integer32):
    """Custom type sessionTerminateBootEra based on Integer32"""
    defaultValue = 0


_SessionTerminateBootEra_Object = MibTableColumn
sessionTerminateBootEra = _SessionTerminateBootEra_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 230, 1, 11),
    _SessionTerminateBootEra_Type()
)
sessionTerminateBootEra.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sessionTerminateBootEra.setStatus("current")


class _SessionTerminateSessionID_Type(Integer32):
    """Custom type sessionTerminateSessionID based on Integer32"""
    defaultValue = 0


_SessionTerminateSessionID_Object = MibTableColumn
sessionTerminateSessionID = _SessionTerminateSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 230, 1, 12),
    _SessionTerminateSessionID_Type()
)
sessionTerminateSessionID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sessionTerminateSessionID.setStatus("current")
_SessionTerminateSignature_Type = DisplayString
_SessionTerminateSignature_Object = MibTableColumn
sessionTerminateSignature = _SessionTerminateSignature_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 230, 1, 13),
    _SessionTerminateSignature_Type()
)
sessionTerminateSignature.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sessionTerminateSignature.setStatus("current")
_T1TestTable_Object = MibTable
t1TestTable = _T1TestTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 2106)
)
if mibBuilder.loadTexts:
    t1TestTable.setStatus("current")
_T1TestEntry_Object = MibTableRow
t1TestEntry = _T1TestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 2106, 1)
)
t1TestEntry.setIndexNames(
    (0, "APTIS-ACTIONS-MIB", "t1TestInstance"),
)
if mibBuilder.loadTexts:
    t1TestEntry.setStatus("current")


class _T1TestInstance_Type(Integer32):
    """Custom type t1TestInstance based on Integer32"""
    defaultValue = 0


_T1TestInstance_Object = MibTableColumn
t1TestInstance = _T1TestInstance_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 2106, 1, 1),
    _T1TestInstance_Type()
)
t1TestInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t1TestInstance.setStatus("current")


class _T1TestTestType_Type(Integer32):
    """Custom type t1TestTestType based on Integer32"""
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
        *(("fives", 3),
          ("ones", 1),
          ("qrss", 4),
          ("zeros", 2))
    )


_T1TestTestType_Type.__name__ = "Integer32"
_T1TestTestType_Object = MibTableColumn
t1TestTestType = _T1TestTestType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 2106, 1, 2),
    _T1TestTestType_Type()
)
t1TestTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t1TestTestType.setStatus("current")


class _T1TestSlotNumber_Type(Integer32):
    """Custom type t1TestSlotNumber based on Integer32"""
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
              8,
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
        *(("slot1", 1),
          ("slot11", 11),
          ("slot12", 12),
          ("slot13", 13),
          ("slot14", 14),
          ("slot15", 15),
          ("slot16", 16),
          ("slot17", 17),
          ("slot18", 18),
          ("slot2", 2),
          ("slot3", 3),
          ("slot4", 4),
          ("slot5", 5),
          ("slot6", 6),
          ("slot7", 7),
          ("slot8", 8))
    )


_T1TestSlotNumber_Type.__name__ = "Integer32"
_T1TestSlotNumber_Object = MibTableColumn
t1TestSlotNumber = _T1TestSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 2106, 1, 3),
    _T1TestSlotNumber_Type()
)
t1TestSlotNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t1TestSlotNumber.setStatus("current")


class _T1TestPortNumber_Type(Integer32):
    """Custom type t1TestPortNumber based on Integer32"""
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
              56)
        )
    )
    namedValues = NamedValues(
        *(("ds11", 1),
          ("ds110", 10),
          ("ds111", 11),
          ("ds112", 12),
          ("ds113", 13),
          ("ds114", 14),
          ("ds115", 15),
          ("ds116", 16),
          ("ds117", 17),
          ("ds118", 18),
          ("ds119", 19),
          ("ds12", 2),
          ("ds120", 20),
          ("ds121", 21),
          ("ds122", 22),
          ("ds123", 23),
          ("ds124", 24),
          ("ds125", 25),
          ("ds126", 26),
          ("ds127", 27),
          ("ds128", 28),
          ("ds129", 29),
          ("ds13", 3),
          ("ds130", 30),
          ("ds131", 31),
          ("ds132", 32),
          ("ds133", 33),
          ("ds134", 34),
          ("ds135", 35),
          ("ds136", 36),
          ("ds137", 37),
          ("ds138", 38),
          ("ds139", 39),
          ("ds14", 4),
          ("ds140", 40),
          ("ds141", 41),
          ("ds142", 42),
          ("ds143", 43),
          ("ds144", 44),
          ("ds145", 45),
          ("ds146", 46),
          ("ds147", 47),
          ("ds148", 48),
          ("ds149", 49),
          ("ds15", 5),
          ("ds150", 50),
          ("ds151", 51),
          ("ds152", 52),
          ("ds153", 53),
          ("ds154", 54),
          ("ds155", 55),
          ("ds156", 56),
          ("ds16", 6),
          ("ds17", 7),
          ("ds18", 8),
          ("ds19", 9))
    )


_T1TestPortNumber_Type.__name__ = "Integer32"
_T1TestPortNumber_Object = MibTableColumn
t1TestPortNumber = _T1TestPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 2106, 1, 4),
    _T1TestPortNumber_Type()
)
t1TestPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t1TestPortNumber.setStatus("current")


class _T1TestTestLength_Type(Integer32):
    """Custom type t1TestTestLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30000),
    )


_T1TestTestLength_Type.__name__ = "Integer32"
_T1TestTestLength_Object = MibTableColumn
t1TestTestLength = _T1TestTestLength_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 2106, 1, 5),
    _T1TestTestLength_Type()
)
t1TestTestLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t1TestTestLength.setStatus("current")


class _T1TestErrorRate_Type(Integer32):
    """Custom type t1TestErrorRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_T1TestErrorRate_Type.__name__ = "Integer32"
_T1TestErrorRate_Object = MibTableColumn
t1TestErrorRate = _T1TestErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 2106, 1, 6),
    _T1TestErrorRate_Type()
)
t1TestErrorRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t1TestErrorRate.setStatus("current")


class _T1TestState_Type(Integer32):
    """Custom type t1TestState based on Integer32"""
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
        *(("cancelled", 8),
          ("checkingResults", 4),
          ("complete", 6),
          ("failed", 7),
          ("initializing", 1),
          ("loopingDown", 5),
          ("loopingUp", 2),
          ("sendingData", 3))
    )


_T1TestState_Type.__name__ = "Integer32"
_T1TestState_Object = MibTableColumn
t1TestState = _T1TestState_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 2106, 1, 7),
    _T1TestState_Type()
)
t1TestState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t1TestState.setStatus("current")
_FlashWriteTable_Object = MibTable
flashWriteTable = _FlashWriteTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3501)
)
if mibBuilder.loadTexts:
    flashWriteTable.setStatus("current")
_FlashWriteEntry_Object = MibTableRow
flashWriteEntry = _FlashWriteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3501, 1)
)
flashWriteEntry.setIndexNames(
    (0, "APTIS-ACTIONS-MIB", "flashWriteInstance"),
)
if mibBuilder.loadTexts:
    flashWriteEntry.setStatus("current")


class _FlashWriteInstance_Type(Integer32):
    """Custom type flashWriteInstance based on Integer32"""
    defaultValue = 0


_FlashWriteInstance_Object = MibTableColumn
flashWriteInstance = _FlashWriteInstance_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3501, 1, 1),
    _FlashWriteInstance_Type()
)
flashWriteInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashWriteInstance.setStatus("current")


class _FlashWriteStatusGeneral_Type(Integer32):
    """Custom type flashWriteStatusGeneral based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("errParam", 4),
          ("failed", 2),
          ("started", 0),
          ("succeeded", 1))
    )


_FlashWriteStatusGeneral_Type.__name__ = "Integer32"
_FlashWriteStatusGeneral_Object = MibTableColumn
flashWriteStatusGeneral = _FlashWriteStatusGeneral_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3501, 1, 2),
    _FlashWriteStatusGeneral_Type()
)
flashWriteStatusGeneral.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashWriteStatusGeneral.setStatus("current")


class _FlashWriteStatusSpecific_Type(Integer32):
    """Custom type flashWriteStatusSpecific based on Integer32"""
    defaultValue = 0

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
        *(("badArgs", 1),
          ("genFail", 3),
          ("lackOfResources", 2),
          ("noError", 0))
    )


_FlashWriteStatusSpecific_Type.__name__ = "Integer32"
_FlashWriteStatusSpecific_Object = MibTableColumn
flashWriteStatusSpecific = _FlashWriteStatusSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3501, 1, 3),
    _FlashWriteStatusSpecific_Type()
)
flashWriteStatusSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashWriteStatusSpecific.setStatus("current")
_FlashWritePathString_Type = DisplayString
_FlashWritePathString_Object = MibTableColumn
flashWritePathString = _FlashWritePathString_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3501, 1, 11),
    _FlashWritePathString_Type()
)
flashWritePathString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashWritePathString.setStatus("current")


class _FlashWriteFileName_Type(DisplayString):
    """Custom type flashWriteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FlashWriteFileName_Type.__name__ = "DisplayString"
_FlashWriteFileName_Object = MibTableColumn
flashWriteFileName = _FlashWriteFileName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3501, 1, 12),
    _FlashWriteFileName_Type()
)
flashWriteFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashWriteFileName.setStatus("current")


class _FlashWriteBytesWritten_Type(Integer32):
    """Custom type flashWriteBytesWritten based on Integer32"""
    defaultValue = 0


_FlashWriteBytesWritten_Object = MibTableColumn
flashWriteBytesWritten = _FlashWriteBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3501, 1, 13),
    _FlashWriteBytesWritten_Type()
)
flashWriteBytesWritten.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashWriteBytesWritten.setStatus("current")


class _FlashWriteVerboseMode_Type(Boolean):
    """Custom type flashWriteVerboseMode based on Boolean"""


_FlashWriteVerboseMode_Object = MibTableColumn
flashWriteVerboseMode = _FlashWriteVerboseMode_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3501, 1, 14),
    _FlashWriteVerboseMode_Type()
)
flashWriteVerboseMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashWriteVerboseMode.setStatus("current")
_FlashReadTable_Object = MibTable
flashReadTable = _FlashReadTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3502)
)
if mibBuilder.loadTexts:
    flashReadTable.setStatus("current")
_FlashReadEntry_Object = MibTableRow
flashReadEntry = _FlashReadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3502, 1)
)
flashReadEntry.setIndexNames(
    (0, "APTIS-ACTIONS-MIB", "flashReadInstance"),
)
if mibBuilder.loadTexts:
    flashReadEntry.setStatus("current")


class _FlashReadInstance_Type(Integer32):
    """Custom type flashReadInstance based on Integer32"""
    defaultValue = 0


_FlashReadInstance_Object = MibTableColumn
flashReadInstance = _FlashReadInstance_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3502, 1, 1),
    _FlashReadInstance_Type()
)
flashReadInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashReadInstance.setStatus("current")


class _FlashReadStatusGeneral_Type(Integer32):
    """Custom type flashReadStatusGeneral based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("badFile", 4),
          ("failed", 2),
          ("genFail", 5),
          ("started", 0),
          ("succeeded", 1))
    )


_FlashReadStatusGeneral_Type.__name__ = "Integer32"
_FlashReadStatusGeneral_Object = MibTableColumn
flashReadStatusGeneral = _FlashReadStatusGeneral_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3502, 1, 2),
    _FlashReadStatusGeneral_Type()
)
flashReadStatusGeneral.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashReadStatusGeneral.setStatus("current")


class _FlashReadFileName_Type(DisplayString):
    """Custom type flashReadFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FlashReadFileName_Type.__name__ = "DisplayString"
_FlashReadFileName_Object = MibTableColumn
flashReadFileName = _FlashReadFileName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3502, 1, 12),
    _FlashReadFileName_Type()
)
flashReadFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashReadFileName.setStatus("current")


class _FlashReadLinesRead_Type(Integer32):
    """Custom type flashReadLinesRead based on Integer32"""
    defaultValue = 0


_FlashReadLinesRead_Object = MibTableColumn
flashReadLinesRead = _FlashReadLinesRead_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3502, 1, 13),
    _FlashReadLinesRead_Type()
)
flashReadLinesRead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashReadLinesRead.setStatus("current")
_FlashSaveTable_Object = MibTable
flashSaveTable = _FlashSaveTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3503)
)
if mibBuilder.loadTexts:
    flashSaveTable.setStatus("current")
_FlashSaveEntry_Object = MibTableRow
flashSaveEntry = _FlashSaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3503, 1)
)
flashSaveEntry.setIndexNames(
    (0, "APTIS-ACTIONS-MIB", "flashSaveInstance"),
)
if mibBuilder.loadTexts:
    flashSaveEntry.setStatus("current")


class _FlashSaveInstance_Type(Integer32):
    """Custom type flashSaveInstance based on Integer32"""
    defaultValue = 0


_FlashSaveInstance_Object = MibTableColumn
flashSaveInstance = _FlashSaveInstance_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3503, 1, 1),
    _FlashSaveInstance_Type()
)
flashSaveInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashSaveInstance.setStatus("current")


class _FlashSaveStatusGeneral_Type(Integer32):
    """Custom type flashSaveStatusGeneral based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("errParam", 4),
          ("failed", 2),
          ("started", 0),
          ("succeeded", 1))
    )


_FlashSaveStatusGeneral_Type.__name__ = "Integer32"
_FlashSaveStatusGeneral_Object = MibTableColumn
flashSaveStatusGeneral = _FlashSaveStatusGeneral_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3503, 1, 2),
    _FlashSaveStatusGeneral_Type()
)
flashSaveStatusGeneral.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashSaveStatusGeneral.setStatus("current")


class _FlashSaveStatusSpecific_Type(Integer32):
    """Custom type flashSaveStatusSpecific based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("genFail", 3),
          ("lackOfResources", 2),
          ("noError", 0))
    )


_FlashSaveStatusSpecific_Type.__name__ = "Integer32"
_FlashSaveStatusSpecific_Object = MibTableColumn
flashSaveStatusSpecific = _FlashSaveStatusSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3503, 1, 3),
    _FlashSaveStatusSpecific_Type()
)
flashSaveStatusSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flashSaveStatusSpecific.setStatus("current")
_ResetTable_Object = MibTable
resetTable = _ResetTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3510)
)
if mibBuilder.loadTexts:
    resetTable.setStatus("current")
_ResetEntry_Object = MibTableRow
resetEntry = _ResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3510, 1)
)
resetEntry.setIndexNames(
    (0, "APTIS-ACTIONS-MIB", "resetInstance"),
)
if mibBuilder.loadTexts:
    resetEntry.setStatus("current")


class _ResetInstance_Type(Integer32):
    """Custom type resetInstance based on Integer32"""
    defaultValue = 0


_ResetInstance_Object = MibTableColumn
resetInstance = _ResetInstance_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3510, 1, 1),
    _ResetInstance_Type()
)
resetInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    resetInstance.setStatus("current")


class _ResetStatusGeneral_Type(Integer32):
    """Custom type resetStatusGeneral based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("errParam", 4),
          ("failed", 2),
          ("started", 0),
          ("succeeded", 1))
    )


_ResetStatusGeneral_Type.__name__ = "Integer32"
_ResetStatusGeneral_Object = MibTableColumn
resetStatusGeneral = _ResetStatusGeneral_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3510, 1, 2),
    _ResetStatusGeneral_Type()
)
resetStatusGeneral.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    resetStatusGeneral.setStatus("current")


class _ResetResetType_Type(Integer32):
    """Custom type resetResetType based on Integer32"""
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
        *(("cold", 2),
          ("hard", 1),
          ("warm", 3))
    )


_ResetResetType_Type.__name__ = "Integer32"
_ResetResetType_Object = MibTableColumn
resetResetType = _ResetResetType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 3, 3510, 1, 11),
    _ResetResetType_Type()
)
resetResetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    resetResetType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APTIS-ACTIONS-MIB",
    **{"aptisActionsModule": aptisActionsModule,
       "slotControlTable": slotControlTable,
       "slotControlEntry": slotControlEntry,
       "slotControlInstance": slotControlInstance,
       "slotControlStatusGeneral": slotControlStatusGeneral,
       "slotControlStatusSpecific": slotControlStatusSpecific,
       "slotControlSlotIndex": slotControlSlotIndex,
       "slotControlSlotAction": slotControlSlotAction,
       "sessionTerminateTable": sessionTerminateTable,
       "sessionTerminateEntry": sessionTerminateEntry,
       "sessionTerminateInstance": sessionTerminateInstance,
       "sessionTerminateStatusGeneral": sessionTerminateStatusGeneral,
       "sessionTerminateStatusSpecific": sessionTerminateStatusSpecific,
       "sessionTerminateBootEra": sessionTerminateBootEra,
       "sessionTerminateSessionID": sessionTerminateSessionID,
       "sessionTerminateSignature": sessionTerminateSignature,
       "t1TestTable": t1TestTable,
       "t1TestEntry": t1TestEntry,
       "t1TestInstance": t1TestInstance,
       "t1TestTestType": t1TestTestType,
       "t1TestSlotNumber": t1TestSlotNumber,
       "t1TestPortNumber": t1TestPortNumber,
       "t1TestTestLength": t1TestTestLength,
       "t1TestErrorRate": t1TestErrorRate,
       "t1TestState": t1TestState,
       "flashWriteTable": flashWriteTable,
       "flashWriteEntry": flashWriteEntry,
       "flashWriteInstance": flashWriteInstance,
       "flashWriteStatusGeneral": flashWriteStatusGeneral,
       "flashWriteStatusSpecific": flashWriteStatusSpecific,
       "flashWritePathString": flashWritePathString,
       "flashWriteFileName": flashWriteFileName,
       "flashWriteBytesWritten": flashWriteBytesWritten,
       "flashWriteVerboseMode": flashWriteVerboseMode,
       "flashReadTable": flashReadTable,
       "flashReadEntry": flashReadEntry,
       "flashReadInstance": flashReadInstance,
       "flashReadStatusGeneral": flashReadStatusGeneral,
       "flashReadFileName": flashReadFileName,
       "flashReadLinesRead": flashReadLinesRead,
       "flashSaveTable": flashSaveTable,
       "flashSaveEntry": flashSaveEntry,
       "flashSaveInstance": flashSaveInstance,
       "flashSaveStatusGeneral": flashSaveStatusGeneral,
       "flashSaveStatusSpecific": flashSaveStatusSpecific,
       "resetTable": resetTable,
       "resetEntry": resetEntry,
       "resetInstance": resetInstance,
       "resetStatusGeneral": resetStatusGeneral,
       "resetResetType": resetResetType}
)

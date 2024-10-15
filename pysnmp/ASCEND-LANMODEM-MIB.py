# SNMP MIB module (ASCEND-LANMODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-LANMODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:59 2024
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

(lanModemGroup,
 slots) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "lanModemGroup",
    "slots")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class ModemSpeedType(Integer32):
    """Custom type ModemSpeedType based on Integer32"""
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
              45)
        )
    )
    namedValues = NamedValues(
        *(("baud1200", 3),
          ("baud12000", 7),
          ("baud14400", 8),
          ("baud16800", 10),
          ("baud19200", 11),
          ("baud21600", 12),
          ("baud2400", 4),
          ("baud24000", 13),
          ("baud26400", 14),
          ("baud28000", 31),
          ("baud28800", 15),
          ("baud29333", 32),
          ("baud300", 1),
          ("baud30667", 33),
          ("baud31200", 16),
          ("baud32000", 18),
          ("baud33333", 34),
          ("baud33600", 17),
          ("baud34000", 19),
          ("baud34667", 35),
          ("baud36000", 20),
          ("baud37333", 36),
          ("baud38000", 21),
          ("baud38667", 37),
          ("baud40000", 22),
          ("baud41333", 38),
          ("baud42000", 23),
          ("baud42667", 39),
          ("baud44000", 24),
          ("baud45333", 40),
          ("baud46000", 25),
          ("baud46667", 41),
          ("baud4800", 5),
          ("baud48000", 26),
          ("baud49333", 42),
          ("baud50000", 27),
          ("baud50667", 43),
          ("baud52000", 28),
          ("baud53333", 44),
          ("baud54000", 29),
          ("baud54667", 45),
          ("baud56000", 30),
          ("baud600", 2),
          ("baud7200", 9),
          ("baud9600", 6))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlotMdmTable_Object = MibTable
slotMdmTable = _SlotMdmTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 5)
)
if mibBuilder.loadTexts:
    slotMdmTable.setStatus("mandatory")
_SlotMdmEntry_Object = MibTableRow
slotMdmEntry = _SlotMdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 5, 1)
)
slotMdmEntry.setIndexNames(
    (0, "ASCEND-LANMODEM-MIB", "slotMdmIndex"),
)
if mibBuilder.loadTexts:
    slotMdmEntry.setStatus("mandatory")
_SlotMdmIndex_Type = Integer32
_SlotMdmIndex_Object = MibTableColumn
slotMdmIndex = _SlotMdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 1),
    _SlotMdmIndex_Type()
)
slotMdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMdmIndex.setStatus("mandatory")
_SlotMdmSlotIndex_Type = Integer32
_SlotMdmSlotIndex_Object = MibTableColumn
slotMdmSlotIndex = _SlotMdmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 2),
    _SlotMdmSlotIndex_Type()
)
slotMdmSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMdmSlotIndex.setStatus("mandatory")
_SlotMdmItemIndex_Type = Integer32
_SlotMdmItemIndex_Object = MibTableColumn
slotMdmItemIndex = _SlotMdmItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 3),
    _SlotMdmItemIndex_Type()
)
slotMdmItemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMdmItemIndex.setStatus("mandatory")


class _SlotMdmItemStatus_Type(Integer32):
    """Custom type slotMdmItemStatus based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("modemStateAwaitingCodes", 5),
          ("modemStateAwaitingRlsd", 4),
          ("modemStateCsmxExtraDelay", 21),
          ("modemStateCsum", 19),
          ("modemStateDiag", 16),
          ("modemStateDisabled", 13),
          ("modemStateDisabledChan", 14),
          ("modemStateDtrDrop", 15),
          ("modemStateFailPost", 2),
          ("modemStateIdle", 3),
          ("modemStateInit", 7),
          ("modemStateInitDialstr2", 10),
          ("modemStateInitDialstr3", 11),
          ("modemStateInitDialstr4", 18),
          ("modemStateInitOpenQueued", 8),
          ("modemStateInitOpenQueuedVc", 9),
          ("modemStateNonExist", 1),
          ("modemStateOnline", 6),
          ("modemStateRedownloadFailed", 20),
          ("modemStateVcInitStr", 17),
          ("modemStateVirtualConnect", 12))
    )


_SlotMdmItemStatus_Type.__name__ = "Integer32"
_SlotMdmItemStatus_Object = MibTableColumn
slotMdmItemStatus = _SlotMdmItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 4),
    _SlotMdmItemStatus_Type()
)
slotMdmItemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMdmItemStatus.setStatus("mandatory")
_SlotMdmItemStatusChar_Type = DisplayString
_SlotMdmItemStatusChar_Object = MibTableColumn
slotMdmItemStatusChar = _SlotMdmItemStatusChar_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 5),
    _SlotMdmItemStatusChar_Type()
)
slotMdmItemStatusChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotMdmItemStatusChar.setStatus("mandatory")


class _SlotMdmItemConfig_Type(Integer32):
    """Custom type slotMdmItemConfig based on Integer32"""
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
        *(("disable", 3),
          ("disableAndChannel", 4),
          ("enable", 2),
          ("other", 1))
    )


_SlotMdmItemConfig_Type.__name__ = "Integer32"
_SlotMdmItemConfig_Object = MibTableColumn
slotMdmItemConfig = _SlotMdmItemConfig_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 5, 1, 6),
    _SlotMdmItemConfig_Type()
)
slotMdmItemConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotMdmItemConfig.setStatus("mandatory")
_AvailLanModem_Type = Integer32
_AvailLanModem_Object = MibScalar
availLanModem = _AvailLanModem_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 1),
    _AvailLanModem_Type()
)
availLanModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availLanModem.setStatus("mandatory")
_AvailLanModemTable_Object = MibTable
availLanModemTable = _AvailLanModemTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 2)
)
if mibBuilder.loadTexts:
    availLanModemTable.setStatus("mandatory")
_AvailLanModemEntry_Object = MibTableRow
availLanModemEntry = _AvailLanModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 2, 1)
)
availLanModemEntry.setIndexNames(
    (0, "ASCEND-LANMODEM-MIB", "availLanModemSlotIndex"),
    (0, "ASCEND-LANMODEM-MIB", "availLanModemPortIndex"),
)
if mibBuilder.loadTexts:
    availLanModemEntry.setStatus("mandatory")
_AvailLanModemSlotIndex_Type = Integer32
_AvailLanModemSlotIndex_Object = MibTableColumn
availLanModemSlotIndex = _AvailLanModemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 2, 1, 1),
    _AvailLanModemSlotIndex_Type()
)
availLanModemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availLanModemSlotIndex.setStatus("mandatory")
_AvailLanModemPortIndex_Type = Integer32
_AvailLanModemPortIndex_Object = MibTableColumn
availLanModemPortIndex = _AvailLanModemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 2, 1, 2),
    _AvailLanModemPortIndex_Type()
)
availLanModemPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availLanModemPortIndex.setStatus("mandatory")
_AvailLanModemUsedCount_Type = Counter32
_AvailLanModemUsedCount_Object = MibTableColumn
availLanModemUsedCount = _AvailLanModemUsedCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 2, 1, 3),
    _AvailLanModemUsedCount_Type()
)
availLanModemUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availLanModemUsedCount.setStatus("mandatory")
_AvailLanModemBadCount_Type = Counter32
_AvailLanModemBadCount_Object = MibTableColumn
availLanModemBadCount = _AvailLanModemBadCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 2, 1, 4),
    _AvailLanModemBadCount_Type()
)
availLanModemBadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availLanModemBadCount.setStatus("mandatory")
_AvailLanModemLast32_Type = Integer32
_AvailLanModemLast32_Object = MibTableColumn
availLanModemLast32 = _AvailLanModemLast32_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 2, 1, 5),
    _AvailLanModemLast32_Type()
)
availLanModemLast32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availLanModemLast32.setStatus("mandatory")
_SuspectLanModem_Type = Integer32
_SuspectLanModem_Object = MibScalar
suspectLanModem = _SuspectLanModem_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 3),
    _SuspectLanModem_Type()
)
suspectLanModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suspectLanModem.setStatus("mandatory")
_SuspectLanModemTable_Object = MibTable
suspectLanModemTable = _SuspectLanModemTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 4)
)
if mibBuilder.loadTexts:
    suspectLanModemTable.setStatus("mandatory")
_SuspectLanModemEntry_Object = MibTableRow
suspectLanModemEntry = _SuspectLanModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 4, 1)
)
suspectLanModemEntry.setIndexNames(
    (0, "ASCEND-LANMODEM-MIB", "suspectLanModemSlotIndex"),
    (0, "ASCEND-LANMODEM-MIB", "suspectLanModemPortIndex"),
)
if mibBuilder.loadTexts:
    suspectLanModemEntry.setStatus("mandatory")
_SuspectLanModemSlotIndex_Type = Integer32
_SuspectLanModemSlotIndex_Object = MibTableColumn
suspectLanModemSlotIndex = _SuspectLanModemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 4, 1, 1),
    _SuspectLanModemSlotIndex_Type()
)
suspectLanModemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suspectLanModemSlotIndex.setStatus("mandatory")
_SuspectLanModemPortIndex_Type = Integer32
_SuspectLanModemPortIndex_Object = MibTableColumn
suspectLanModemPortIndex = _SuspectLanModemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 4, 1, 2),
    _SuspectLanModemPortIndex_Type()
)
suspectLanModemPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suspectLanModemPortIndex.setStatus("mandatory")
_SuspectLanModemUsedCount_Type = Counter32
_SuspectLanModemUsedCount_Object = MibTableColumn
suspectLanModemUsedCount = _SuspectLanModemUsedCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 4, 1, 3),
    _SuspectLanModemUsedCount_Type()
)
suspectLanModemUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suspectLanModemUsedCount.setStatus("mandatory")
_SuspectLanModemBadCount_Type = Counter32
_SuspectLanModemBadCount_Object = MibTableColumn
suspectLanModemBadCount = _SuspectLanModemBadCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 4, 1, 4),
    _SuspectLanModemBadCount_Type()
)
suspectLanModemBadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suspectLanModemBadCount.setStatus("mandatory")
_SuspectLanModemLast32_Type = Integer32
_SuspectLanModemLast32_Object = MibTableColumn
suspectLanModemLast32 = _SuspectLanModemLast32_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 4, 1, 5),
    _SuspectLanModemLast32_Type()
)
suspectLanModemLast32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suspectLanModemLast32.setStatus("mandatory")
_DisabledLanModem_Type = Integer32
_DisabledLanModem_Object = MibScalar
disabledLanModem = _DisabledLanModem_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 5),
    _DisabledLanModem_Type()
)
disabledLanModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disabledLanModem.setStatus("mandatory")
_DisabledLanModemTable_Object = MibTable
disabledLanModemTable = _DisabledLanModemTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 6)
)
if mibBuilder.loadTexts:
    disabledLanModemTable.setStatus("mandatory")
_DisabledLanModemEntry_Object = MibTableRow
disabledLanModemEntry = _DisabledLanModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 6, 1)
)
disabledLanModemEntry.setIndexNames(
    (0, "ASCEND-LANMODEM-MIB", "disabledLanModemSlotIndex"),
    (0, "ASCEND-LANMODEM-MIB", "disabledLanModemPortIndex"),
)
if mibBuilder.loadTexts:
    disabledLanModemEntry.setStatus("mandatory")
_DisabledLanModemSlotIndex_Type = Integer32
_DisabledLanModemSlotIndex_Object = MibTableColumn
disabledLanModemSlotIndex = _DisabledLanModemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 6, 1, 1),
    _DisabledLanModemSlotIndex_Type()
)
disabledLanModemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disabledLanModemSlotIndex.setStatus("mandatory")
_DisabledLanModemPortIndex_Type = Integer32
_DisabledLanModemPortIndex_Object = MibTableColumn
disabledLanModemPortIndex = _DisabledLanModemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 6, 1, 2),
    _DisabledLanModemPortIndex_Type()
)
disabledLanModemPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disabledLanModemPortIndex.setStatus("mandatory")
_DisabledLanModemUsedCount_Type = Counter32
_DisabledLanModemUsedCount_Object = MibTableColumn
disabledLanModemUsedCount = _DisabledLanModemUsedCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 6, 1, 3),
    _DisabledLanModemUsedCount_Type()
)
disabledLanModemUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disabledLanModemUsedCount.setStatus("mandatory")
_DisabledLanModemBadCount_Type = Counter32
_DisabledLanModemBadCount_Object = MibTableColumn
disabledLanModemBadCount = _DisabledLanModemBadCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 6, 1, 4),
    _DisabledLanModemBadCount_Type()
)
disabledLanModemBadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disabledLanModemBadCount.setStatus("mandatory")
_DisabledLanModemLast32_Type = Integer32
_DisabledLanModemLast32_Object = MibTableColumn
disabledLanModemLast32 = _DisabledLanModemLast32_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 6, 1, 5),
    _DisabledLanModemLast32_Type()
)
disabledLanModemLast32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disabledLanModemLast32.setStatus("mandatory")
_DeadLanModem_Type = Integer32
_DeadLanModem_Object = MibScalar
deadLanModem = _DeadLanModem_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 7),
    _DeadLanModem_Type()
)
deadLanModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deadLanModem.setStatus("mandatory")
_DeadLanModemTable_Object = MibTable
deadLanModemTable = _DeadLanModemTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 8)
)
if mibBuilder.loadTexts:
    deadLanModemTable.setStatus("mandatory")
_DeadLanModemEntry_Object = MibTableRow
deadLanModemEntry = _DeadLanModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 8, 1)
)
deadLanModemEntry.setIndexNames(
    (0, "ASCEND-LANMODEM-MIB", "deadLanModemSlotIndex"),
    (0, "ASCEND-LANMODEM-MIB", "deadLanModemPortIndex"),
)
if mibBuilder.loadTexts:
    deadLanModemEntry.setStatus("mandatory")
_DeadLanModemSlotIndex_Type = Integer32
_DeadLanModemSlotIndex_Object = MibTableColumn
deadLanModemSlotIndex = _DeadLanModemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 8, 1, 1),
    _DeadLanModemSlotIndex_Type()
)
deadLanModemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deadLanModemSlotIndex.setStatus("mandatory")
_DeadLanModemPortIndex_Type = Integer32
_DeadLanModemPortIndex_Object = MibTableColumn
deadLanModemPortIndex = _DeadLanModemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 8, 1, 2),
    _DeadLanModemPortIndex_Type()
)
deadLanModemPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deadLanModemPortIndex.setStatus("mandatory")


class _DeadLanModemState_Type(Integer32):
    """Custom type deadLanModemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failedPost", 2),
          ("nonExistent", 3),
          ("other", 1))
    )


_DeadLanModemState_Type.__name__ = "Integer32"
_DeadLanModemState_Object = MibTableColumn
deadLanModemState = _DeadLanModemState_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 8, 1, 3),
    _DeadLanModemState_Type()
)
deadLanModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deadLanModemState.setStatus("mandatory")
_BusyLanModem_Type = Integer32
_BusyLanModem_Object = MibScalar
busyLanModem = _BusyLanModem_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 9),
    _BusyLanModem_Type()
)
busyLanModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyLanModem.setStatus("mandatory")
_BusyLanModemTable_Object = MibTable
busyLanModemTable = _BusyLanModemTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 10)
)
if mibBuilder.loadTexts:
    busyLanModemTable.setStatus("mandatory")
_BusyLanModemEntry_Object = MibTableRow
busyLanModemEntry = _BusyLanModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 10, 1)
)
busyLanModemEntry.setIndexNames(
    (0, "ASCEND-LANMODEM-MIB", "busyLanModemSlotIndex"),
    (0, "ASCEND-LANMODEM-MIB", "busyLanModemPortIndex"),
)
if mibBuilder.loadTexts:
    busyLanModemEntry.setStatus("mandatory")
_BusyLanModemSlotIndex_Type = Integer32
_BusyLanModemSlotIndex_Object = MibTableColumn
busyLanModemSlotIndex = _BusyLanModemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 1),
    _BusyLanModemSlotIndex_Type()
)
busyLanModemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyLanModemSlotIndex.setStatus("mandatory")
_BusyLanModemPortIndex_Type = Integer32
_BusyLanModemPortIndex_Object = MibTableColumn
busyLanModemPortIndex = _BusyLanModemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 2),
    _BusyLanModemPortIndex_Type()
)
busyLanModemPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyLanModemPortIndex.setStatus("mandatory")
_BusyLanModemUsedCount_Type = Counter32
_BusyLanModemUsedCount_Object = MibTableColumn
busyLanModemUsedCount = _BusyLanModemUsedCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 3),
    _BusyLanModemUsedCount_Type()
)
busyLanModemUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyLanModemUsedCount.setStatus("mandatory")
_BusyLanModemBadCount_Type = Counter32
_BusyLanModemBadCount_Object = MibTableColumn
busyLanModemBadCount = _BusyLanModemBadCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 4),
    _BusyLanModemBadCount_Type()
)
busyLanModemBadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyLanModemBadCount.setStatus("mandatory")
_BusyLanModemLast32_Type = Integer32
_BusyLanModemLast32_Object = MibTableColumn
busyLanModemLast32 = _BusyLanModemLast32_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 5),
    _BusyLanModemLast32_Type()
)
busyLanModemLast32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyLanModemLast32.setStatus("mandatory")


class _BusyDirection_Type(Integer32):
    """Custom type busyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("callAnswered", 3),
          ("callOriginated", 2),
          ("callUnknown", 1))
    )


_BusyDirection_Type.__name__ = "Integer32"
_BusyDirection_Object = MibTableColumn
busyDirection = _BusyDirection_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 10, 1, 6),
    _BusyDirection_Type()
)
busyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyDirection.setStatus("mandatory")


class _SuspectTrapState_Type(Integer32):
    """Custom type suspectTrapState based on Integer32"""
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


_SuspectTrapState_Type.__name__ = "Integer32"
_SuspectTrapState_Object = MibScalar
suspectTrapState = _SuspectTrapState_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 11),
    _SuspectTrapState_Type()
)
suspectTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    suspectTrapState.setStatus("mandatory")


class _CsmLanMdmDiagAdminStatus_Type(Integer32):
    """Custom type csmLanMdmDiagAdminStatus based on Integer32"""
    defaultValue = 2

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


_CsmLanMdmDiagAdminStatus_Type.__name__ = "Integer32"
_CsmLanMdmDiagAdminStatus_Object = MibScalar
csmLanMdmDiagAdminStatus = _CsmLanMdmDiagAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 12),
    _CsmLanMdmDiagAdminStatus_Type()
)
csmLanMdmDiagAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csmLanMdmDiagAdminStatus.setStatus("mandatory")
_CsmLanMdmDiagMaxNumberOfDiagEntries_Type = Integer32
_CsmLanMdmDiagMaxNumberOfDiagEntries_Object = MibScalar
csmLanMdmDiagMaxNumberOfDiagEntries = _CsmLanMdmDiagMaxNumberOfDiagEntries_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 13),
    _CsmLanMdmDiagMaxNumberOfDiagEntries_Type()
)
csmLanMdmDiagMaxNumberOfDiagEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagMaxNumberOfDiagEntries.setStatus("mandatory")
_CsmLanMdmDiagFirstIndexNumber_Type = Integer32
_CsmLanMdmDiagFirstIndexNumber_Object = MibScalar
csmLanMdmDiagFirstIndexNumber = _CsmLanMdmDiagFirstIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 14),
    _CsmLanMdmDiagFirstIndexNumber_Type()
)
csmLanMdmDiagFirstIndexNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagFirstIndexNumber.setStatus("mandatory")
_CsmLanMdmDiagLastIndexNumber_Type = Integer32
_CsmLanMdmDiagLastIndexNumber_Object = MibScalar
csmLanMdmDiagLastIndexNumber = _CsmLanMdmDiagLastIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 15),
    _CsmLanMdmDiagLastIndexNumber_Type()
)
csmLanMdmDiagLastIndexNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagLastIndexNumber.setStatus("mandatory")
_CsmLanMdmDiagTable_Object = MibTable
csmLanMdmDiagTable = _CsmLanMdmDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16)
)
if mibBuilder.loadTexts:
    csmLanMdmDiagTable.setStatus("mandatory")
_CsmLanMdmDiagEntry_Object = MibTableRow
csmLanMdmDiagEntry = _CsmLanMdmDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1)
)
csmLanMdmDiagEntry.setIndexNames(
    (0, "ASCEND-LANMODEM-MIB", "csmLanMdmDiagIndexNumber"),
)
if mibBuilder.loadTexts:
    csmLanMdmDiagEntry.setStatus("mandatory")
_CsmLanMdmDiagIndexNumber_Type = Integer32
_CsmLanMdmDiagIndexNumber_Object = MibTableColumn
csmLanMdmDiagIndexNumber = _CsmLanMdmDiagIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 1),
    _CsmLanMdmDiagIndexNumber_Type()
)
csmLanMdmDiagIndexNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagIndexNumber.setStatus("mandatory")
_CsmLanMdmDiagCallReferenceNum_Type = Integer32
_CsmLanMdmDiagCallReferenceNum_Object = MibTableColumn
csmLanMdmDiagCallReferenceNum = _CsmLanMdmDiagCallReferenceNum_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 2),
    _CsmLanMdmDiagCallReferenceNum_Type()
)
csmLanMdmDiagCallReferenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagCallReferenceNum.setStatus("mandatory")
_CsmLanMdmDiagSlotIndex_Type = Integer32
_CsmLanMdmDiagSlotIndex_Object = MibTableColumn
csmLanMdmDiagSlotIndex = _CsmLanMdmDiagSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 3),
    _CsmLanMdmDiagSlotIndex_Type()
)
csmLanMdmDiagSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagSlotIndex.setStatus("mandatory")
_CsmLanMdmDiagPortIndex_Type = Integer32
_CsmLanMdmDiagPortIndex_Object = MibTableColumn
csmLanMdmDiagPortIndex = _CsmLanMdmDiagPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 4),
    _CsmLanMdmDiagPortIndex_Type()
)
csmLanMdmDiagPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagPortIndex.setStatus("mandatory")
_CsmLanMdmDiagCurrentXmitRate_Type = ModemSpeedType
_CsmLanMdmDiagCurrentXmitRate_Object = MibTableColumn
csmLanMdmDiagCurrentXmitRate = _CsmLanMdmDiagCurrentXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 5),
    _CsmLanMdmDiagCurrentXmitRate_Type()
)
csmLanMdmDiagCurrentXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagCurrentXmitRate.setStatus("mandatory")
_CsmLanMdmDiagMinXmitRate_Type = ModemSpeedType
_CsmLanMdmDiagMinXmitRate_Object = MibTableColumn
csmLanMdmDiagMinXmitRate = _CsmLanMdmDiagMinXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 6),
    _CsmLanMdmDiagMinXmitRate_Type()
)
csmLanMdmDiagMinXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagMinXmitRate.setStatus("mandatory")
_CsmLanMdmDiagMaxXmitRate_Type = ModemSpeedType
_CsmLanMdmDiagMaxXmitRate_Object = MibTableColumn
csmLanMdmDiagMaxXmitRate = _CsmLanMdmDiagMaxXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 7),
    _CsmLanMdmDiagMaxXmitRate_Type()
)
csmLanMdmDiagMaxXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagMaxXmitRate.setStatus("mandatory")
_CsmLanMdmDiagCurrentRecvRate_Type = ModemSpeedType
_CsmLanMdmDiagCurrentRecvRate_Object = MibTableColumn
csmLanMdmDiagCurrentRecvRate = _CsmLanMdmDiagCurrentRecvRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 8),
    _CsmLanMdmDiagCurrentRecvRate_Type()
)
csmLanMdmDiagCurrentRecvRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagCurrentRecvRate.setStatus("mandatory")
_CsmLanMdmDiagMinRcvRate_Type = ModemSpeedType
_CsmLanMdmDiagMinRcvRate_Object = MibTableColumn
csmLanMdmDiagMinRcvRate = _CsmLanMdmDiagMinRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 9),
    _CsmLanMdmDiagMinRcvRate_Type()
)
csmLanMdmDiagMinRcvRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagMinRcvRate.setStatus("mandatory")
_CsmLanMdmDiagMaxRcvRate_Type = ModemSpeedType
_CsmLanMdmDiagMaxRcvRate_Object = MibTableColumn
csmLanMdmDiagMaxRcvRate = _CsmLanMdmDiagMaxRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 10),
    _CsmLanMdmDiagMaxRcvRate_Type()
)
csmLanMdmDiagMaxRcvRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagMaxRcvRate.setStatus("mandatory")


class _CsmLanMdmDiagProtocol_Type(Integer32):
    """Custom type csmLanMdmDiagProtocol based on Integer32"""
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
        *(("lap-m", 2),
          ("mnp10", 4),
          ("mnp4", 3),
          ("none", 1))
    )


_CsmLanMdmDiagProtocol_Type.__name__ = "Integer32"
_CsmLanMdmDiagProtocol_Object = MibTableColumn
csmLanMdmDiagProtocol = _CsmLanMdmDiagProtocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 11),
    _CsmLanMdmDiagProtocol_Type()
)
csmLanMdmDiagProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagProtocol.setStatus("mandatory")


class _CsmLanMdmDiagCompression_Type(Integer32):
    """Custom type csmLanMdmDiagCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mnp5", 2),
          ("none", 1),
          ("v42bis", 3))
    )


_CsmLanMdmDiagCompression_Type.__name__ = "Integer32"
_CsmLanMdmDiagCompression_Object = MibTableColumn
csmLanMdmDiagCompression = _CsmLanMdmDiagCompression_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 12),
    _CsmLanMdmDiagCompression_Type()
)
csmLanMdmDiagCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagCompression.setStatus("mandatory")


class _CsmLanMdmDiagModulation_Type(Integer32):
    """Custom type csmLanMdmDiagModulation based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("bell103", 10),
          ("bell208", 14),
          ("bell212", 9),
          ("k56flex", 6),
          ("v17", 3),
          ("v21", 5),
          ("v22", 11),
          ("v22bis", 7),
          ("v23", 4),
          ("v27", 16),
          ("v29", 15),
          ("v32", 8),
          ("v33", 13),
          ("v34", 2),
          ("v90", 1),
          ("vFC", 12))
    )


_CsmLanMdmDiagModulation_Type.__name__ = "Integer32"
_CsmLanMdmDiagModulation_Object = MibTableColumn
csmLanMdmDiagModulation = _CsmLanMdmDiagModulation_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 13),
    _CsmLanMdmDiagModulation_Type()
)
csmLanMdmDiagModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagModulation.setStatus("mandatory")


class _CsmLanMdmDiagSymbolRate_Type(Integer32):
    """Custom type csmLanMdmDiagSymbolRate based on Integer32"""
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
        *(("notApplicable", 1),
          ("sym2400", 2),
          ("sym2800", 3),
          ("sym3000", 4),
          ("sym3200", 5),
          ("sym3429", 6))
    )


_CsmLanMdmDiagSymbolRate_Type.__name__ = "Integer32"
_CsmLanMdmDiagSymbolRate_Object = MibTableColumn
csmLanMdmDiagSymbolRate = _CsmLanMdmDiagSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 14),
    _CsmLanMdmDiagSymbolRate_Type()
)
csmLanMdmDiagSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagSymbolRate.setStatus("mandatory")
_CsmLanMdmDiagCurrentRcvLevel_Type = Integer32
_CsmLanMdmDiagCurrentRcvLevel_Object = MibTableColumn
csmLanMdmDiagCurrentRcvLevel = _CsmLanMdmDiagCurrentRcvLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 15),
    _CsmLanMdmDiagCurrentRcvLevel_Type()
)
csmLanMdmDiagCurrentRcvLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagCurrentRcvLevel.setStatus("mandatory")
_CsmLanMdmDiagCurrentXmitLevel_Type = Integer32
_CsmLanMdmDiagCurrentXmitLevel_Object = MibTableColumn
csmLanMdmDiagCurrentXmitLevel = _CsmLanMdmDiagCurrentXmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 16),
    _CsmLanMdmDiagCurrentXmitLevel_Type()
)
csmLanMdmDiagCurrentXmitLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagCurrentXmitLevel.setStatus("mandatory")
_CsmLanMdmDiagCurrentLineQuality_Type = Integer32
_CsmLanMdmDiagCurrentLineQuality_Object = MibTableColumn
csmLanMdmDiagCurrentLineQuality = _CsmLanMdmDiagCurrentLineQuality_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 17),
    _CsmLanMdmDiagCurrentLineQuality_Type()
)
csmLanMdmDiagCurrentLineQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagCurrentLineQuality.setStatus("mandatory")
_CsmLanMdmDiagCurrentSNR_Type = Integer32
_CsmLanMdmDiagCurrentSNR_Object = MibTableColumn
csmLanMdmDiagCurrentSNR = _CsmLanMdmDiagCurrentSNR_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 18),
    _CsmLanMdmDiagCurrentSNR_Type()
)
csmLanMdmDiagCurrentSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagCurrentSNR.setStatus("mandatory")
_CsmLanMdmDiagSNRMinimum_Type = Integer32
_CsmLanMdmDiagSNRMinimum_Object = MibTableColumn
csmLanMdmDiagSNRMinimum = _CsmLanMdmDiagSNRMinimum_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 19),
    _CsmLanMdmDiagSNRMinimum_Type()
)
csmLanMdmDiagSNRMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagSNRMinimum.setStatus("mandatory")
_CsmLanMdmDiagSNRMaximum_Type = Integer32
_CsmLanMdmDiagSNRMaximum_Object = MibTableColumn
csmLanMdmDiagSNRMaximum = _CsmLanMdmDiagSNRMaximum_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 20),
    _CsmLanMdmDiagSNRMaximum_Type()
)
csmLanMdmDiagSNRMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagSNRMaximum.setStatus("mandatory")
_CsmLanMdmDiagLocalRetrainRequested_Type = Integer32
_CsmLanMdmDiagLocalRetrainRequested_Object = MibTableColumn
csmLanMdmDiagLocalRetrainRequested = _CsmLanMdmDiagLocalRetrainRequested_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 21),
    _CsmLanMdmDiagLocalRetrainRequested_Type()
)
csmLanMdmDiagLocalRetrainRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagLocalRetrainRequested.setStatus("mandatory")
_CsmLanMdmDiagRemoteRetrainRequested_Type = Integer32
_CsmLanMdmDiagRemoteRetrainRequested_Object = MibTableColumn
csmLanMdmDiagRemoteRetrainRequested = _CsmLanMdmDiagRemoteRetrainRequested_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 22),
    _CsmLanMdmDiagRemoteRetrainRequested_Type()
)
csmLanMdmDiagRemoteRetrainRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagRemoteRetrainRequested.setStatus("mandatory")
_CsmLanMdmDiagHighestSPXRcvState_Type = Integer32
_CsmLanMdmDiagHighestSPXRcvState_Object = MibTableColumn
csmLanMdmDiagHighestSPXRcvState = _CsmLanMdmDiagHighestSPXRcvState_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 23),
    _CsmLanMdmDiagHighestSPXRcvState_Type()
)
csmLanMdmDiagHighestSPXRcvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagHighestSPXRcvState.setStatus("mandatory")
_CsmLanMdmDiagHighestSPXTxState_Type = Integer32
_CsmLanMdmDiagHighestSPXTxState_Object = MibTableColumn
csmLanMdmDiagHighestSPXTxState = _CsmLanMdmDiagHighestSPXTxState_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 24),
    _CsmLanMdmDiagHighestSPXTxState_Type()
)
csmLanMdmDiagHighestSPXTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagHighestSPXTxState.setStatus("mandatory")


class _CsmLanMdmDiagNonlinearEncode_Type(Integer32):
    """Custom type csmLanMdmDiagNonlinearEncode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CsmLanMdmDiagNonlinearEncode_Type.__name__ = "Integer32"
_CsmLanMdmDiagNonlinearEncode_Object = MibTableColumn
csmLanMdmDiagNonlinearEncode = _CsmLanMdmDiagNonlinearEncode_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 25),
    _CsmLanMdmDiagNonlinearEncode_Type()
)
csmLanMdmDiagNonlinearEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagNonlinearEncode.setStatus("mandatory")


class _CsmLanMdmDiagPrecode_Type(Integer32):
    """Custom type csmLanMdmDiagPrecode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CsmLanMdmDiagPrecode_Type.__name__ = "Integer32"
_CsmLanMdmDiagPrecode_Object = MibTableColumn
csmLanMdmDiagPrecode = _CsmLanMdmDiagPrecode_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 26),
    _CsmLanMdmDiagPrecode_Type()
)
csmLanMdmDiagPrecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagPrecode.setStatus("mandatory")


class _CsmLanMdmDiagShaping_Type(Integer32):
    """Custom type csmLanMdmDiagShaping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CsmLanMdmDiagShaping_Type.__name__ = "Integer32"
_CsmLanMdmDiagShaping_Object = MibTableColumn
csmLanMdmDiagShaping = _CsmLanMdmDiagShaping_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 27),
    _CsmLanMdmDiagShaping_Type()
)
csmLanMdmDiagShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagShaping.setStatus("mandatory")
_CsmLanMdmDiagConnectionTime_Type = Integer32
_CsmLanMdmDiagConnectionTime_Object = MibTableColumn
csmLanMdmDiagConnectionTime = _CsmLanMdmDiagConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 28),
    _CsmLanMdmDiagConnectionTime_Type()
)
csmLanMdmDiagConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagConnectionTime.setStatus("mandatory")


class _CsmLanMdmDiagDisconnectReason_Type(Integer32):
    """Custom type csmLanMdmDiagDisconnectReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              12,
              13,
              15,
              16,
              17,
              18,
              19,
              20,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("breakDisconnect", 19),
          ("callWaiting", 3),
          ("carrierLost", 4),
          ("excessiveRetransmissions", 13),
          ("gstnCleardown", 16),
          ("inactivityTimer", 17),
          ("incompatibleProtocol", 7),
          ("incompatibleSpeeds", 18),
          ("keyAbort", 20),
          ("linkDisconnect", 12),
          ("localRequest", 2),
          ("noConnect", 22),
          ("noErrorCorrection", 6),
          ("noRemoteResponse", 15),
          ("none", 1),
          ("retrainFailure", 23))
    )


_CsmLanMdmDiagDisconnectReason_Type.__name__ = "Integer32"
_CsmLanMdmDiagDisconnectReason_Object = MibTableColumn
csmLanMdmDiagDisconnectReason = _CsmLanMdmDiagDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 29),
    _CsmLanMdmDiagDisconnectReason_Type()
)
csmLanMdmDiagDisconnectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagDisconnectReason.setStatus("mandatory")


class _CsmLanMdmDiagRetrainReason_Type(Integer32):
    """Custom type csmLanMdmDiagRetrainReason based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("carrierLostButLineActive", 8),
          ("fallbackToV34", 10),
          ("localRateRenegDueToHiEQM", 5),
          ("localRateRenegDueToLowEQM", 6),
          ("localRateRenegDueToMN10", 11),
          ("localRetrainDueTo2RateRenegs", 7),
          ("localRetrainDueToATO1", 3),
          ("localRetrainDueToHiEQM", 4),
          ("localRetrainDueToMN10", 12),
          ("lostConnection", 9),
          ("none", 1),
          ("remoteRateReneg", 14),
          ("remoteRetrain", 13),
          ("retrainOrRateRenegSuccess", 2),
          ("v34RetrainAt24K", 15),
          ("v42RetrainDueToExcessiveReTx", 16))
    )


_CsmLanMdmDiagRetrainReason_Type.__name__ = "Integer32"
_CsmLanMdmDiagRetrainReason_Object = MibTableColumn
csmLanMdmDiagRetrainReason = _CsmLanMdmDiagRetrainReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 15, 16, 1, 30),
    _CsmLanMdmDiagRetrainReason_Type()
)
csmLanMdmDiagRetrainReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csmLanMdmDiagRetrainReason.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-LANMODEM-MIB",
    **{"DisplayString": DisplayString,
       "ModemSpeedType": ModemSpeedType,
       "slotMdmTable": slotMdmTable,
       "slotMdmEntry": slotMdmEntry,
       "slotMdmIndex": slotMdmIndex,
       "slotMdmSlotIndex": slotMdmSlotIndex,
       "slotMdmItemIndex": slotMdmItemIndex,
       "slotMdmItemStatus": slotMdmItemStatus,
       "slotMdmItemStatusChar": slotMdmItemStatusChar,
       "slotMdmItemConfig": slotMdmItemConfig,
       "availLanModem": availLanModem,
       "availLanModemTable": availLanModemTable,
       "availLanModemEntry": availLanModemEntry,
       "availLanModemSlotIndex": availLanModemSlotIndex,
       "availLanModemPortIndex": availLanModemPortIndex,
       "availLanModemUsedCount": availLanModemUsedCount,
       "availLanModemBadCount": availLanModemBadCount,
       "availLanModemLast32": availLanModemLast32,
       "suspectLanModem": suspectLanModem,
       "suspectLanModemTable": suspectLanModemTable,
       "suspectLanModemEntry": suspectLanModemEntry,
       "suspectLanModemSlotIndex": suspectLanModemSlotIndex,
       "suspectLanModemPortIndex": suspectLanModemPortIndex,
       "suspectLanModemUsedCount": suspectLanModemUsedCount,
       "suspectLanModemBadCount": suspectLanModemBadCount,
       "suspectLanModemLast32": suspectLanModemLast32,
       "disabledLanModem": disabledLanModem,
       "disabledLanModemTable": disabledLanModemTable,
       "disabledLanModemEntry": disabledLanModemEntry,
       "disabledLanModemSlotIndex": disabledLanModemSlotIndex,
       "disabledLanModemPortIndex": disabledLanModemPortIndex,
       "disabledLanModemUsedCount": disabledLanModemUsedCount,
       "disabledLanModemBadCount": disabledLanModemBadCount,
       "disabledLanModemLast32": disabledLanModemLast32,
       "deadLanModem": deadLanModem,
       "deadLanModemTable": deadLanModemTable,
       "deadLanModemEntry": deadLanModemEntry,
       "deadLanModemSlotIndex": deadLanModemSlotIndex,
       "deadLanModemPortIndex": deadLanModemPortIndex,
       "deadLanModemState": deadLanModemState,
       "busyLanModem": busyLanModem,
       "busyLanModemTable": busyLanModemTable,
       "busyLanModemEntry": busyLanModemEntry,
       "busyLanModemSlotIndex": busyLanModemSlotIndex,
       "busyLanModemPortIndex": busyLanModemPortIndex,
       "busyLanModemUsedCount": busyLanModemUsedCount,
       "busyLanModemBadCount": busyLanModemBadCount,
       "busyLanModemLast32": busyLanModemLast32,
       "busyDirection": busyDirection,
       "suspectTrapState": suspectTrapState,
       "csmLanMdmDiagAdminStatus": csmLanMdmDiagAdminStatus,
       "csmLanMdmDiagMaxNumberOfDiagEntries": csmLanMdmDiagMaxNumberOfDiagEntries,
       "csmLanMdmDiagFirstIndexNumber": csmLanMdmDiagFirstIndexNumber,
       "csmLanMdmDiagLastIndexNumber": csmLanMdmDiagLastIndexNumber,
       "csmLanMdmDiagTable": csmLanMdmDiagTable,
       "csmLanMdmDiagEntry": csmLanMdmDiagEntry,
       "csmLanMdmDiagIndexNumber": csmLanMdmDiagIndexNumber,
       "csmLanMdmDiagCallReferenceNum": csmLanMdmDiagCallReferenceNum,
       "csmLanMdmDiagSlotIndex": csmLanMdmDiagSlotIndex,
       "csmLanMdmDiagPortIndex": csmLanMdmDiagPortIndex,
       "csmLanMdmDiagCurrentXmitRate": csmLanMdmDiagCurrentXmitRate,
       "csmLanMdmDiagMinXmitRate": csmLanMdmDiagMinXmitRate,
       "csmLanMdmDiagMaxXmitRate": csmLanMdmDiagMaxXmitRate,
       "csmLanMdmDiagCurrentRecvRate": csmLanMdmDiagCurrentRecvRate,
       "csmLanMdmDiagMinRcvRate": csmLanMdmDiagMinRcvRate,
       "csmLanMdmDiagMaxRcvRate": csmLanMdmDiagMaxRcvRate,
       "csmLanMdmDiagProtocol": csmLanMdmDiagProtocol,
       "csmLanMdmDiagCompression": csmLanMdmDiagCompression,
       "csmLanMdmDiagModulation": csmLanMdmDiagModulation,
       "csmLanMdmDiagSymbolRate": csmLanMdmDiagSymbolRate,
       "csmLanMdmDiagCurrentRcvLevel": csmLanMdmDiagCurrentRcvLevel,
       "csmLanMdmDiagCurrentXmitLevel": csmLanMdmDiagCurrentXmitLevel,
       "csmLanMdmDiagCurrentLineQuality": csmLanMdmDiagCurrentLineQuality,
       "csmLanMdmDiagCurrentSNR": csmLanMdmDiagCurrentSNR,
       "csmLanMdmDiagSNRMinimum": csmLanMdmDiagSNRMinimum,
       "csmLanMdmDiagSNRMaximum": csmLanMdmDiagSNRMaximum,
       "csmLanMdmDiagLocalRetrainRequested": csmLanMdmDiagLocalRetrainRequested,
       "csmLanMdmDiagRemoteRetrainRequested": csmLanMdmDiagRemoteRetrainRequested,
       "csmLanMdmDiagHighestSPXRcvState": csmLanMdmDiagHighestSPXRcvState,
       "csmLanMdmDiagHighestSPXTxState": csmLanMdmDiagHighestSPXTxState,
       "csmLanMdmDiagNonlinearEncode": csmLanMdmDiagNonlinearEncode,
       "csmLanMdmDiagPrecode": csmLanMdmDiagPrecode,
       "csmLanMdmDiagShaping": csmLanMdmDiagShaping,
       "csmLanMdmDiagConnectionTime": csmLanMdmDiagConnectionTime,
       "csmLanMdmDiagDisconnectReason": csmLanMdmDiagDisconnectReason,
       "csmLanMdmDiagRetrainReason": csmLanMdmDiagRetrainReason}
)

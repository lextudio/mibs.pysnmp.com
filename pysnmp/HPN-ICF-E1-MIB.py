# SNMP MIB module (HPN-ICF-E1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-E1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:01 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfE1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28)
)
hpnicfE1.setRevisions(
        ("2012-07-16 17:41",
         "2010-04-08 18:55",
         "2009-06-08 17:41",
         "2004-12-01 14:36")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfE1TimeSlot(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_Hpnicfe1InterfaceStatusTable_Object = MibTable
hpnicfe1InterfaceStatusTable = _Hpnicfe1InterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1)
)
if mibBuilder.loadTexts:
    hpnicfe1InterfaceStatusTable.setStatus("current")
_Hpnicfe1InterfaceStatusEntry_Object = MibTableRow
hpnicfe1InterfaceStatusEntry = _Hpnicfe1InterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1)
)
hpnicfe1InterfaceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfe1InterfaceStatusEntry.setStatus("current")
_Hpnicfe1InterfaceInErrs_Type = Counter32
_Hpnicfe1InterfaceInErrs_Object = MibTableColumn
hpnicfe1InterfaceInErrs = _Hpnicfe1InterfaceInErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 1),
    _Hpnicfe1InterfaceInErrs_Type()
)
hpnicfe1InterfaceInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceInErrs.setStatus("current")
_Hpnicfe1InterfaceInRuntsErrs_Type = Counter32
_Hpnicfe1InterfaceInRuntsErrs_Object = MibTableColumn
hpnicfe1InterfaceInRuntsErrs = _Hpnicfe1InterfaceInRuntsErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 2),
    _Hpnicfe1InterfaceInRuntsErrs_Type()
)
hpnicfe1InterfaceInRuntsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceInRuntsErrs.setStatus("current")
_Hpnicfe1InterfaceInGiantsErrs_Type = Counter32
_Hpnicfe1InterfaceInGiantsErrs_Object = MibTableColumn
hpnicfe1InterfaceInGiantsErrs = _Hpnicfe1InterfaceInGiantsErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 3),
    _Hpnicfe1InterfaceInGiantsErrs_Type()
)
hpnicfe1InterfaceInGiantsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceInGiantsErrs.setStatus("current")
_Hpnicfe1InterfaceInCrcErrs_Type = Counter32
_Hpnicfe1InterfaceInCrcErrs_Object = MibTableColumn
hpnicfe1InterfaceInCrcErrs = _Hpnicfe1InterfaceInCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 4),
    _Hpnicfe1InterfaceInCrcErrs_Type()
)
hpnicfe1InterfaceInCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceInCrcErrs.setStatus("current")
_Hpnicfe1InterfaceInAlignErrs_Type = Counter32
_Hpnicfe1InterfaceInAlignErrs_Object = MibTableColumn
hpnicfe1InterfaceInAlignErrs = _Hpnicfe1InterfaceInAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 5),
    _Hpnicfe1InterfaceInAlignErrs_Type()
)
hpnicfe1InterfaceInAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceInAlignErrs.setStatus("current")
_Hpnicfe1InterfaceInOverRunsErrs_Type = Counter32
_Hpnicfe1InterfaceInOverRunsErrs_Object = MibTableColumn
hpnicfe1InterfaceInOverRunsErrs = _Hpnicfe1InterfaceInOverRunsErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 6),
    _Hpnicfe1InterfaceInOverRunsErrs_Type()
)
hpnicfe1InterfaceInOverRunsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceInOverRunsErrs.setStatus("current")
_Hpnicfe1InterfaceInDribblesErrs_Type = Counter32
_Hpnicfe1InterfaceInDribblesErrs_Object = MibTableColumn
hpnicfe1InterfaceInDribblesErrs = _Hpnicfe1InterfaceInDribblesErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 7),
    _Hpnicfe1InterfaceInDribblesErrs_Type()
)
hpnicfe1InterfaceInDribblesErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceInDribblesErrs.setStatus("current")
_Hpnicfe1InterfaceInAbortedSeqErrs_Type = Counter32
_Hpnicfe1InterfaceInAbortedSeqErrs_Object = MibTableColumn
hpnicfe1InterfaceInAbortedSeqErrs = _Hpnicfe1InterfaceInAbortedSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 8),
    _Hpnicfe1InterfaceInAbortedSeqErrs_Type()
)
hpnicfe1InterfaceInAbortedSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceInAbortedSeqErrs.setStatus("current")
_Hpnicfe1InterfaceInNoBufferErrs_Type = Counter32
_Hpnicfe1InterfaceInNoBufferErrs_Object = MibTableColumn
hpnicfe1InterfaceInNoBufferErrs = _Hpnicfe1InterfaceInNoBufferErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 9),
    _Hpnicfe1InterfaceInNoBufferErrs_Type()
)
hpnicfe1InterfaceInNoBufferErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceInNoBufferErrs.setStatus("current")
_Hpnicfe1InterfaceInFramingErrs_Type = Counter32
_Hpnicfe1InterfaceInFramingErrs_Object = MibTableColumn
hpnicfe1InterfaceInFramingErrs = _Hpnicfe1InterfaceInFramingErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 10),
    _Hpnicfe1InterfaceInFramingErrs_Type()
)
hpnicfe1InterfaceInFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceInFramingErrs.setStatus("current")
_Hpnicfe1InterfaceOutputErrs_Type = Counter32
_Hpnicfe1InterfaceOutputErrs_Object = MibTableColumn
hpnicfe1InterfaceOutputErrs = _Hpnicfe1InterfaceOutputErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 11),
    _Hpnicfe1InterfaceOutputErrs_Type()
)
hpnicfe1InterfaceOutputErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceOutputErrs.setStatus("current")
_Hpnicfe1InterfaceOutUnderRunErrs_Type = Counter32
_Hpnicfe1InterfaceOutUnderRunErrs_Object = MibTableColumn
hpnicfe1InterfaceOutUnderRunErrs = _Hpnicfe1InterfaceOutUnderRunErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 12),
    _Hpnicfe1InterfaceOutUnderRunErrs_Type()
)
hpnicfe1InterfaceOutUnderRunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceOutUnderRunErrs.setStatus("current")
_Hpnicfe1InterfaceOutCollisonsErrs_Type = Counter32
_Hpnicfe1InterfaceOutCollisonsErrs_Object = MibTableColumn
hpnicfe1InterfaceOutCollisonsErrs = _Hpnicfe1InterfaceOutCollisonsErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 13),
    _Hpnicfe1InterfaceOutCollisonsErrs_Type()
)
hpnicfe1InterfaceOutCollisonsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceOutCollisonsErrs.setStatus("current")
_Hpnicfe1InterfaceOutDeferedErrs_Type = Counter32
_Hpnicfe1InterfaceOutDeferedErrs_Object = MibTableColumn
hpnicfe1InterfaceOutDeferedErrs = _Hpnicfe1InterfaceOutDeferedErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 14),
    _Hpnicfe1InterfaceOutDeferedErrs_Type()
)
hpnicfe1InterfaceOutDeferedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1InterfaceOutDeferedErrs.setStatus("current")
_Hpnicfe1Table_Object = MibTable
hpnicfe1Table = _Hpnicfe1Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2)
)
if mibBuilder.loadTexts:
    hpnicfe1Table.setStatus("current")
_Hpnicfe1Entry_Object = MibTableRow
hpnicfe1Entry = _Hpnicfe1Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1)
)
hpnicfe1Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfe1Entry.setStatus("current")


class _Hpnicfe1Type_Type(Bits):
    """Custom type hpnicfe1Type based on Bits"""
    namedValues = NamedValues(
        *(("pos", 1),
          ("voice", 0))
    )

_Hpnicfe1Type_Type.__name__ = "Bits"
_Hpnicfe1Type_Object = MibTableColumn
hpnicfe1Type = _Hpnicfe1Type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 1),
    _Hpnicfe1Type_Type()
)
hpnicfe1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1Type.setStatus("current")


class _Hpnicfe1Clock_Type(Integer32):
    """Custom type hpnicfe1Clock based on Integer32"""
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
        *(("internal", 3),
          ("line", 4),
          ("linePri", 5),
          ("master", 2),
          ("slave", 1))
    )


_Hpnicfe1Clock_Type.__name__ = "Integer32"
_Hpnicfe1Clock_Object = MibTableColumn
hpnicfe1Clock = _Hpnicfe1Clock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 2),
    _Hpnicfe1Clock_Type()
)
hpnicfe1Clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfe1Clock.setStatus("current")


class _Hpnicfe1FrameFormat_Type(Integer32):
    """Custom type hpnicfe1FrameFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc4", 1),
          ("nocrc4", 2))
    )


_Hpnicfe1FrameFormat_Type.__name__ = "Integer32"
_Hpnicfe1FrameFormat_Object = MibTableColumn
hpnicfe1FrameFormat = _Hpnicfe1FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 3),
    _Hpnicfe1FrameFormat_Type()
)
hpnicfe1FrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfe1FrameFormat.setStatus("current")


class _Hpnicfe1LineCode_Type(Integer32):
    """Custom type hpnicfe1LineCode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("hdb3", 3))
    )


_Hpnicfe1LineCode_Type.__name__ = "Integer32"
_Hpnicfe1LineCode_Object = MibTableColumn
hpnicfe1LineCode = _Hpnicfe1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 4),
    _Hpnicfe1LineCode_Type()
)
hpnicfe1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfe1LineCode.setStatus("current")
_Hpnicfe1PriSetTimeSlot_Type = HpnicfE1TimeSlot
_Hpnicfe1PriSetTimeSlot_Object = MibTableColumn
hpnicfe1PriSetTimeSlot = _Hpnicfe1PriSetTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 5),
    _Hpnicfe1PriSetTimeSlot_Type()
)
hpnicfe1PriSetTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfe1PriSetTimeSlot.setStatus("current")
_Hpnicfe1DChannelIndex_Type = Integer32
_Hpnicfe1DChannelIndex_Object = MibTableColumn
hpnicfe1DChannelIndex = _Hpnicfe1DChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 6),
    _Hpnicfe1DChannelIndex_Type()
)
hpnicfe1DChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1DChannelIndex.setStatus("current")
_Hpnicfe1SubScribLineChannelIndex_Type = Integer32
_Hpnicfe1SubScribLineChannelIndex_Object = MibTableColumn
hpnicfe1SubScribLineChannelIndex = _Hpnicfe1SubScribLineChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 7),
    _Hpnicfe1SubScribLineChannelIndex_Type()
)
hpnicfe1SubScribLineChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1SubScribLineChannelIndex.setStatus("current")
_Hpnicfe1FcmChannelIndex_Type = Integer32
_Hpnicfe1FcmChannelIndex_Object = MibTableColumn
hpnicfe1FcmChannelIndex = _Hpnicfe1FcmChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 8),
    _Hpnicfe1FcmChannelIndex_Type()
)
hpnicfe1FcmChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1FcmChannelIndex.setStatus("current")
_Hpnicfe1InterfaceTable_Object = MibTable
hpnicfe1InterfaceTable = _Hpnicfe1InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 3)
)
if mibBuilder.loadTexts:
    hpnicfe1InterfaceTable.setStatus("current")
_Hpnicfe1InterfaceEntry_Object = MibTableRow
hpnicfe1InterfaceEntry = _Hpnicfe1InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 3, 1)
)
hpnicfe1InterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfe1InterfaceEntry.setStatus("current")
_Hpnicfe1ControllerIndex_Type = Integer32
_Hpnicfe1ControllerIndex_Object = MibTableColumn
hpnicfe1ControllerIndex = _Hpnicfe1ControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 3, 1, 1),
    _Hpnicfe1ControllerIndex_Type()
)
hpnicfe1ControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfe1ControllerIndex.setStatus("current")
_Hpnicfe1TimeSlotSetTable_Object = MibTable
hpnicfe1TimeSlotSetTable = _Hpnicfe1TimeSlotSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4)
)
if mibBuilder.loadTexts:
    hpnicfe1TimeSlotSetTable.setStatus("current")
_Hpnicfe1TimeSlotSetEntry_Object = MibTableRow
hpnicfe1TimeSlotSetEntry = _Hpnicfe1TimeSlotSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4, 1)
)
hpnicfe1TimeSlotSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfe1TimeSlotSetEntry.setStatus("current")


class _Hpnicfe1TimeSlotSetGroupId_Type(Integer32):
    """Custom type hpnicfe1TimeSlotSetGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Hpnicfe1TimeSlotSetGroupId_Type.__name__ = "Integer32"
_Hpnicfe1TimeSlotSetGroupId_Object = MibTableColumn
hpnicfe1TimeSlotSetGroupId = _Hpnicfe1TimeSlotSetGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4, 1, 1),
    _Hpnicfe1TimeSlotSetGroupId_Type()
)
hpnicfe1TimeSlotSetGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfe1TimeSlotSetGroupId.setStatus("current")


class _Hpnicfe1TimeSlotSetSignalType_Type(Integer32):
    """Custom type hpnicfe1TimeSlotSetSignalType based on Integer32"""
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
        *(("em-delay", 2),
          ("em-immediate", 3),
          ("em-wink", 4),
          ("fxo-ground", 5),
          ("fxo-loop", 6),
          ("fxs-ground", 7),
          ("fxs-loop", 8),
          ("r2", 9),
          ("unkown", 1))
    )


_Hpnicfe1TimeSlotSetSignalType_Type.__name__ = "Integer32"
_Hpnicfe1TimeSlotSetSignalType_Object = MibTableColumn
hpnicfe1TimeSlotSetSignalType = _Hpnicfe1TimeSlotSetSignalType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4, 1, 2),
    _Hpnicfe1TimeSlotSetSignalType_Type()
)
hpnicfe1TimeSlotSetSignalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfe1TimeSlotSetSignalType.setStatus("current")
_Hpnicfe1TimeSlotSetList_Type = HpnicfE1TimeSlot
_Hpnicfe1TimeSlotSetList_Object = MibTableColumn
hpnicfe1TimeSlotSetList = _Hpnicfe1TimeSlotSetList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4, 1, 3),
    _Hpnicfe1TimeSlotSetList_Type()
)
hpnicfe1TimeSlotSetList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfe1TimeSlotSetList.setStatus("current")
_Hpnicfe1TimeSlotSetRowStatus_Type = RowStatus
_Hpnicfe1TimeSlotSetRowStatus_Object = MibTableColumn
hpnicfe1TimeSlotSetRowStatus = _Hpnicfe1TimeSlotSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4, 1, 4),
    _Hpnicfe1TimeSlotSetRowStatus_Type()
)
hpnicfe1TimeSlotSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfe1TimeSlotSetRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-E1-MIB",
    **{"HpnicfE1TimeSlot": HpnicfE1TimeSlot,
       "hpnicfE1": hpnicfE1,
       "hpnicfe1InterfaceStatusTable": hpnicfe1InterfaceStatusTable,
       "hpnicfe1InterfaceStatusEntry": hpnicfe1InterfaceStatusEntry,
       "hpnicfe1InterfaceInErrs": hpnicfe1InterfaceInErrs,
       "hpnicfe1InterfaceInRuntsErrs": hpnicfe1InterfaceInRuntsErrs,
       "hpnicfe1InterfaceInGiantsErrs": hpnicfe1InterfaceInGiantsErrs,
       "hpnicfe1InterfaceInCrcErrs": hpnicfe1InterfaceInCrcErrs,
       "hpnicfe1InterfaceInAlignErrs": hpnicfe1InterfaceInAlignErrs,
       "hpnicfe1InterfaceInOverRunsErrs": hpnicfe1InterfaceInOverRunsErrs,
       "hpnicfe1InterfaceInDribblesErrs": hpnicfe1InterfaceInDribblesErrs,
       "hpnicfe1InterfaceInAbortedSeqErrs": hpnicfe1InterfaceInAbortedSeqErrs,
       "hpnicfe1InterfaceInNoBufferErrs": hpnicfe1InterfaceInNoBufferErrs,
       "hpnicfe1InterfaceInFramingErrs": hpnicfe1InterfaceInFramingErrs,
       "hpnicfe1InterfaceOutputErrs": hpnicfe1InterfaceOutputErrs,
       "hpnicfe1InterfaceOutUnderRunErrs": hpnicfe1InterfaceOutUnderRunErrs,
       "hpnicfe1InterfaceOutCollisonsErrs": hpnicfe1InterfaceOutCollisonsErrs,
       "hpnicfe1InterfaceOutDeferedErrs": hpnicfe1InterfaceOutDeferedErrs,
       "hpnicfe1Table": hpnicfe1Table,
       "hpnicfe1Entry": hpnicfe1Entry,
       "hpnicfe1Type": hpnicfe1Type,
       "hpnicfe1Clock": hpnicfe1Clock,
       "hpnicfe1FrameFormat": hpnicfe1FrameFormat,
       "hpnicfe1LineCode": hpnicfe1LineCode,
       "hpnicfe1PriSetTimeSlot": hpnicfe1PriSetTimeSlot,
       "hpnicfe1DChannelIndex": hpnicfe1DChannelIndex,
       "hpnicfe1SubScribLineChannelIndex": hpnicfe1SubScribLineChannelIndex,
       "hpnicfe1FcmChannelIndex": hpnicfe1FcmChannelIndex,
       "hpnicfe1InterfaceTable": hpnicfe1InterfaceTable,
       "hpnicfe1InterfaceEntry": hpnicfe1InterfaceEntry,
       "hpnicfe1ControllerIndex": hpnicfe1ControllerIndex,
       "hpnicfe1TimeSlotSetTable": hpnicfe1TimeSlotSetTable,
       "hpnicfe1TimeSlotSetEntry": hpnicfe1TimeSlotSetEntry,
       "hpnicfe1TimeSlotSetGroupId": hpnicfe1TimeSlotSetGroupId,
       "hpnicfe1TimeSlotSetSignalType": hpnicfe1TimeSlotSetSignalType,
       "hpnicfe1TimeSlotSetList": hpnicfe1TimeSlotSetList,
       "hpnicfe1TimeSlotSetRowStatus": hpnicfe1TimeSlotSetRowStatus}
)

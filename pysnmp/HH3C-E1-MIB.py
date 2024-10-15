# SNMP MIB module (HH3C-E1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-E1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:02 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cE1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28)
)
hh3cE1.setRevisions(
        ("2012-07-16 17:41",
         "2010-04-08 18:55",
         "2009-06-08 17:41",
         "2004-12-01 14:36")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cE1TimeSlot(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3ce1InterfaceStatusTable_Object = MibTable
hh3ce1InterfaceStatusTable = _Hh3ce1InterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1)
)
if mibBuilder.loadTexts:
    hh3ce1InterfaceStatusTable.setStatus("current")
_Hh3ce1InterfaceStatusEntry_Object = MibTableRow
hh3ce1InterfaceStatusEntry = _Hh3ce1InterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1)
)
hh3ce1InterfaceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3ce1InterfaceStatusEntry.setStatus("current")
_Hh3ce1InterfaceInErrs_Type = Counter32
_Hh3ce1InterfaceInErrs_Object = MibTableColumn
hh3ce1InterfaceInErrs = _Hh3ce1InterfaceInErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 1),
    _Hh3ce1InterfaceInErrs_Type()
)
hh3ce1InterfaceInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceInErrs.setStatus("current")
_Hh3ce1InterfaceInRuntsErrs_Type = Counter32
_Hh3ce1InterfaceInRuntsErrs_Object = MibTableColumn
hh3ce1InterfaceInRuntsErrs = _Hh3ce1InterfaceInRuntsErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 2),
    _Hh3ce1InterfaceInRuntsErrs_Type()
)
hh3ce1InterfaceInRuntsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceInRuntsErrs.setStatus("current")
_Hh3ce1InterfaceInGiantsErrs_Type = Counter32
_Hh3ce1InterfaceInGiantsErrs_Object = MibTableColumn
hh3ce1InterfaceInGiantsErrs = _Hh3ce1InterfaceInGiantsErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 3),
    _Hh3ce1InterfaceInGiantsErrs_Type()
)
hh3ce1InterfaceInGiantsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceInGiantsErrs.setStatus("current")
_Hh3ce1InterfaceInCrcErrs_Type = Counter32
_Hh3ce1InterfaceInCrcErrs_Object = MibTableColumn
hh3ce1InterfaceInCrcErrs = _Hh3ce1InterfaceInCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 4),
    _Hh3ce1InterfaceInCrcErrs_Type()
)
hh3ce1InterfaceInCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceInCrcErrs.setStatus("current")
_Hh3ce1InterfaceInAlignErrs_Type = Counter32
_Hh3ce1InterfaceInAlignErrs_Object = MibTableColumn
hh3ce1InterfaceInAlignErrs = _Hh3ce1InterfaceInAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 5),
    _Hh3ce1InterfaceInAlignErrs_Type()
)
hh3ce1InterfaceInAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceInAlignErrs.setStatus("current")
_Hh3ce1InterfaceInOverRunsErrs_Type = Counter32
_Hh3ce1InterfaceInOverRunsErrs_Object = MibTableColumn
hh3ce1InterfaceInOverRunsErrs = _Hh3ce1InterfaceInOverRunsErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 6),
    _Hh3ce1InterfaceInOverRunsErrs_Type()
)
hh3ce1InterfaceInOverRunsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceInOverRunsErrs.setStatus("current")
_Hh3ce1InterfaceInDribblesErrs_Type = Counter32
_Hh3ce1InterfaceInDribblesErrs_Object = MibTableColumn
hh3ce1InterfaceInDribblesErrs = _Hh3ce1InterfaceInDribblesErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 7),
    _Hh3ce1InterfaceInDribblesErrs_Type()
)
hh3ce1InterfaceInDribblesErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceInDribblesErrs.setStatus("current")
_Hh3ce1InterfaceInAbortedSeqErrs_Type = Counter32
_Hh3ce1InterfaceInAbortedSeqErrs_Object = MibTableColumn
hh3ce1InterfaceInAbortedSeqErrs = _Hh3ce1InterfaceInAbortedSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 8),
    _Hh3ce1InterfaceInAbortedSeqErrs_Type()
)
hh3ce1InterfaceInAbortedSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceInAbortedSeqErrs.setStatus("current")
_Hh3ce1InterfaceInNoBufferErrs_Type = Counter32
_Hh3ce1InterfaceInNoBufferErrs_Object = MibTableColumn
hh3ce1InterfaceInNoBufferErrs = _Hh3ce1InterfaceInNoBufferErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 9),
    _Hh3ce1InterfaceInNoBufferErrs_Type()
)
hh3ce1InterfaceInNoBufferErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceInNoBufferErrs.setStatus("current")
_Hh3ce1InterfaceInFramingErrs_Type = Counter32
_Hh3ce1InterfaceInFramingErrs_Object = MibTableColumn
hh3ce1InterfaceInFramingErrs = _Hh3ce1InterfaceInFramingErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 10),
    _Hh3ce1InterfaceInFramingErrs_Type()
)
hh3ce1InterfaceInFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceInFramingErrs.setStatus("current")
_Hh3ce1InterfaceOutputErrs_Type = Counter32
_Hh3ce1InterfaceOutputErrs_Object = MibTableColumn
hh3ce1InterfaceOutputErrs = _Hh3ce1InterfaceOutputErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 11),
    _Hh3ce1InterfaceOutputErrs_Type()
)
hh3ce1InterfaceOutputErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceOutputErrs.setStatus("current")
_Hh3ce1InterfaceOutUnderRunErrs_Type = Counter32
_Hh3ce1InterfaceOutUnderRunErrs_Object = MibTableColumn
hh3ce1InterfaceOutUnderRunErrs = _Hh3ce1InterfaceOutUnderRunErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 12),
    _Hh3ce1InterfaceOutUnderRunErrs_Type()
)
hh3ce1InterfaceOutUnderRunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceOutUnderRunErrs.setStatus("current")
_Hh3ce1InterfaceOutCollisonsErrs_Type = Counter32
_Hh3ce1InterfaceOutCollisonsErrs_Object = MibTableColumn
hh3ce1InterfaceOutCollisonsErrs = _Hh3ce1InterfaceOutCollisonsErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 13),
    _Hh3ce1InterfaceOutCollisonsErrs_Type()
)
hh3ce1InterfaceOutCollisonsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceOutCollisonsErrs.setStatus("current")
_Hh3ce1InterfaceOutDeferedErrs_Type = Counter32
_Hh3ce1InterfaceOutDeferedErrs_Object = MibTableColumn
hh3ce1InterfaceOutDeferedErrs = _Hh3ce1InterfaceOutDeferedErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 1, 1, 14),
    _Hh3ce1InterfaceOutDeferedErrs_Type()
)
hh3ce1InterfaceOutDeferedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1InterfaceOutDeferedErrs.setStatus("current")
_Hh3ce1Table_Object = MibTable
hh3ce1Table = _Hh3ce1Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 2)
)
if mibBuilder.loadTexts:
    hh3ce1Table.setStatus("current")
_Hh3ce1Entry_Object = MibTableRow
hh3ce1Entry = _Hh3ce1Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 2, 1)
)
hh3ce1Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3ce1Entry.setStatus("current")


class _Hh3ce1Type_Type(Bits):
    """Custom type hh3ce1Type based on Bits"""
    namedValues = NamedValues(
        *(("pos", 1),
          ("voice", 0))
    )

_Hh3ce1Type_Type.__name__ = "Bits"
_Hh3ce1Type_Object = MibTableColumn
hh3ce1Type = _Hh3ce1Type_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 2, 1, 1),
    _Hh3ce1Type_Type()
)
hh3ce1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1Type.setStatus("current")


class _Hh3ce1Clock_Type(Integer32):
    """Custom type hh3ce1Clock based on Integer32"""
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


_Hh3ce1Clock_Type.__name__ = "Integer32"
_Hh3ce1Clock_Object = MibTableColumn
hh3ce1Clock = _Hh3ce1Clock_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 2, 1, 2),
    _Hh3ce1Clock_Type()
)
hh3ce1Clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3ce1Clock.setStatus("current")


class _Hh3ce1FrameFormat_Type(Integer32):
    """Custom type hh3ce1FrameFormat based on Integer32"""
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


_Hh3ce1FrameFormat_Type.__name__ = "Integer32"
_Hh3ce1FrameFormat_Object = MibTableColumn
hh3ce1FrameFormat = _Hh3ce1FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 2, 1, 3),
    _Hh3ce1FrameFormat_Type()
)
hh3ce1FrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3ce1FrameFormat.setStatus("current")


class _Hh3ce1LineCode_Type(Integer32):
    """Custom type hh3ce1LineCode based on Integer32"""
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


_Hh3ce1LineCode_Type.__name__ = "Integer32"
_Hh3ce1LineCode_Object = MibTableColumn
hh3ce1LineCode = _Hh3ce1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 2, 1, 4),
    _Hh3ce1LineCode_Type()
)
hh3ce1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3ce1LineCode.setStatus("current")
_Hh3ce1PriSetTimeSlot_Type = Hh3cE1TimeSlot
_Hh3ce1PriSetTimeSlot_Object = MibTableColumn
hh3ce1PriSetTimeSlot = _Hh3ce1PriSetTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 2, 1, 5),
    _Hh3ce1PriSetTimeSlot_Type()
)
hh3ce1PriSetTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3ce1PriSetTimeSlot.setStatus("current")
_Hh3ce1DChannelIndex_Type = Integer32
_Hh3ce1DChannelIndex_Object = MibTableColumn
hh3ce1DChannelIndex = _Hh3ce1DChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 2, 1, 6),
    _Hh3ce1DChannelIndex_Type()
)
hh3ce1DChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1DChannelIndex.setStatus("current")
_Hh3ce1SubScribLineChannelIndex_Type = Integer32
_Hh3ce1SubScribLineChannelIndex_Object = MibTableColumn
hh3ce1SubScribLineChannelIndex = _Hh3ce1SubScribLineChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 2, 1, 7),
    _Hh3ce1SubScribLineChannelIndex_Type()
)
hh3ce1SubScribLineChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1SubScribLineChannelIndex.setStatus("current")
_Hh3ce1FcmChannelIndex_Type = Integer32
_Hh3ce1FcmChannelIndex_Object = MibTableColumn
hh3ce1FcmChannelIndex = _Hh3ce1FcmChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 2, 1, 8),
    _Hh3ce1FcmChannelIndex_Type()
)
hh3ce1FcmChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1FcmChannelIndex.setStatus("current")
_Hh3ce1InterfaceTable_Object = MibTable
hh3ce1InterfaceTable = _Hh3ce1InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 3)
)
if mibBuilder.loadTexts:
    hh3ce1InterfaceTable.setStatus("current")
_Hh3ce1InterfaceEntry_Object = MibTableRow
hh3ce1InterfaceEntry = _Hh3ce1InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 3, 1)
)
hh3ce1InterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3ce1InterfaceEntry.setStatus("current")
_Hh3ce1ControllerIndex_Type = Integer32
_Hh3ce1ControllerIndex_Object = MibTableColumn
hh3ce1ControllerIndex = _Hh3ce1ControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 3, 1, 1),
    _Hh3ce1ControllerIndex_Type()
)
hh3ce1ControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ce1ControllerIndex.setStatus("current")
_Hh3ce1TimeSlotSetTable_Object = MibTable
hh3ce1TimeSlotSetTable = _Hh3ce1TimeSlotSetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 4)
)
if mibBuilder.loadTexts:
    hh3ce1TimeSlotSetTable.setStatus("current")
_Hh3ce1TimeSlotSetEntry_Object = MibTableRow
hh3ce1TimeSlotSetEntry = _Hh3ce1TimeSlotSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 4, 1)
)
hh3ce1TimeSlotSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3ce1TimeSlotSetEntry.setStatus("current")


class _Hh3ce1TimeSlotSetGroupId_Type(Integer32):
    """Custom type hh3ce1TimeSlotSetGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Hh3ce1TimeSlotSetGroupId_Type.__name__ = "Integer32"
_Hh3ce1TimeSlotSetGroupId_Object = MibTableColumn
hh3ce1TimeSlotSetGroupId = _Hh3ce1TimeSlotSetGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 4, 1, 1),
    _Hh3ce1TimeSlotSetGroupId_Type()
)
hh3ce1TimeSlotSetGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3ce1TimeSlotSetGroupId.setStatus("current")


class _Hh3ce1TimeSlotSetSignalType_Type(Integer32):
    """Custom type hh3ce1TimeSlotSetSignalType based on Integer32"""
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


_Hh3ce1TimeSlotSetSignalType_Type.__name__ = "Integer32"
_Hh3ce1TimeSlotSetSignalType_Object = MibTableColumn
hh3ce1TimeSlotSetSignalType = _Hh3ce1TimeSlotSetSignalType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 4, 1, 2),
    _Hh3ce1TimeSlotSetSignalType_Type()
)
hh3ce1TimeSlotSetSignalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3ce1TimeSlotSetSignalType.setStatus("current")
_Hh3ce1TimeSlotSetList_Type = Hh3cE1TimeSlot
_Hh3ce1TimeSlotSetList_Object = MibTableColumn
hh3ce1TimeSlotSetList = _Hh3ce1TimeSlotSetList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 4, 1, 3),
    _Hh3ce1TimeSlotSetList_Type()
)
hh3ce1TimeSlotSetList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3ce1TimeSlotSetList.setStatus("current")
_Hh3ce1TimeSlotSetRowStatus_Type = RowStatus
_Hh3ce1TimeSlotSetRowStatus_Object = MibTableColumn
hh3ce1TimeSlotSetRowStatus = _Hh3ce1TimeSlotSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28, 4, 1, 4),
    _Hh3ce1TimeSlotSetRowStatus_Type()
)
hh3ce1TimeSlotSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3ce1TimeSlotSetRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-E1-MIB",
    **{"Hh3cE1TimeSlot": Hh3cE1TimeSlot,
       "hh3cE1": hh3cE1,
       "hh3ce1InterfaceStatusTable": hh3ce1InterfaceStatusTable,
       "hh3ce1InterfaceStatusEntry": hh3ce1InterfaceStatusEntry,
       "hh3ce1InterfaceInErrs": hh3ce1InterfaceInErrs,
       "hh3ce1InterfaceInRuntsErrs": hh3ce1InterfaceInRuntsErrs,
       "hh3ce1InterfaceInGiantsErrs": hh3ce1InterfaceInGiantsErrs,
       "hh3ce1InterfaceInCrcErrs": hh3ce1InterfaceInCrcErrs,
       "hh3ce1InterfaceInAlignErrs": hh3ce1InterfaceInAlignErrs,
       "hh3ce1InterfaceInOverRunsErrs": hh3ce1InterfaceInOverRunsErrs,
       "hh3ce1InterfaceInDribblesErrs": hh3ce1InterfaceInDribblesErrs,
       "hh3ce1InterfaceInAbortedSeqErrs": hh3ce1InterfaceInAbortedSeqErrs,
       "hh3ce1InterfaceInNoBufferErrs": hh3ce1InterfaceInNoBufferErrs,
       "hh3ce1InterfaceInFramingErrs": hh3ce1InterfaceInFramingErrs,
       "hh3ce1InterfaceOutputErrs": hh3ce1InterfaceOutputErrs,
       "hh3ce1InterfaceOutUnderRunErrs": hh3ce1InterfaceOutUnderRunErrs,
       "hh3ce1InterfaceOutCollisonsErrs": hh3ce1InterfaceOutCollisonsErrs,
       "hh3ce1InterfaceOutDeferedErrs": hh3ce1InterfaceOutDeferedErrs,
       "hh3ce1Table": hh3ce1Table,
       "hh3ce1Entry": hh3ce1Entry,
       "hh3ce1Type": hh3ce1Type,
       "hh3ce1Clock": hh3ce1Clock,
       "hh3ce1FrameFormat": hh3ce1FrameFormat,
       "hh3ce1LineCode": hh3ce1LineCode,
       "hh3ce1PriSetTimeSlot": hh3ce1PriSetTimeSlot,
       "hh3ce1DChannelIndex": hh3ce1DChannelIndex,
       "hh3ce1SubScribLineChannelIndex": hh3ce1SubScribLineChannelIndex,
       "hh3ce1FcmChannelIndex": hh3ce1FcmChannelIndex,
       "hh3ce1InterfaceTable": hh3ce1InterfaceTable,
       "hh3ce1InterfaceEntry": hh3ce1InterfaceEntry,
       "hh3ce1ControllerIndex": hh3ce1ControllerIndex,
       "hh3ce1TimeSlotSetTable": hh3ce1TimeSlotSetTable,
       "hh3ce1TimeSlotSetEntry": hh3ce1TimeSlotSetEntry,
       "hh3ce1TimeSlotSetGroupId": hh3ce1TimeSlotSetGroupId,
       "hh3ce1TimeSlotSetSignalType": hh3ce1TimeSlotSetSignalType,
       "hh3ce1TimeSlotSetList": hh3ce1TimeSlotSetList,
       "hh3ce1TimeSlotSetRowStatus": hh3ce1TimeSlotSetRowStatus}
)

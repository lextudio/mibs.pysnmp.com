# SNMP MIB module (HH3C-T1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-T1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:05 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hh3cT1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29)
)
hh3cT1.setRevisions(
        ("2012-07-16 17:41",
         "2009-06-08 17:41",
         "2004-12-01 14:36")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cT1TimeSlot(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3ct1InterfaceStatusTable_Object = MibTable
hh3ct1InterfaceStatusTable = _Hh3ct1InterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1)
)
if mibBuilder.loadTexts:
    hh3ct1InterfaceStatusTable.setStatus("current")
_Hh3ct1InterfaceStatusEntry_Object = MibTableRow
hh3ct1InterfaceStatusEntry = _Hh3ct1InterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1)
)
hh3ct1InterfaceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3ct1InterfaceStatusEntry.setStatus("current")
_Hh3ct1InterfaceInErrs_Type = Counter32
_Hh3ct1InterfaceInErrs_Object = MibTableColumn
hh3ct1InterfaceInErrs = _Hh3ct1InterfaceInErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 1),
    _Hh3ct1InterfaceInErrs_Type()
)
hh3ct1InterfaceInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceInErrs.setStatus("current")
_Hh3ct1InterfaceInRuntsErrs_Type = Counter32
_Hh3ct1InterfaceInRuntsErrs_Object = MibTableColumn
hh3ct1InterfaceInRuntsErrs = _Hh3ct1InterfaceInRuntsErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 2),
    _Hh3ct1InterfaceInRuntsErrs_Type()
)
hh3ct1InterfaceInRuntsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceInRuntsErrs.setStatus("current")
_Hh3ct1InterfaceInGiantsErrs_Type = Counter32
_Hh3ct1InterfaceInGiantsErrs_Object = MibTableColumn
hh3ct1InterfaceInGiantsErrs = _Hh3ct1InterfaceInGiantsErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 3),
    _Hh3ct1InterfaceInGiantsErrs_Type()
)
hh3ct1InterfaceInGiantsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceInGiantsErrs.setStatus("current")
_Hh3ct1InterfaceInCrcErrs_Type = Counter32
_Hh3ct1InterfaceInCrcErrs_Object = MibTableColumn
hh3ct1InterfaceInCrcErrs = _Hh3ct1InterfaceInCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 4),
    _Hh3ct1InterfaceInCrcErrs_Type()
)
hh3ct1InterfaceInCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceInCrcErrs.setStatus("current")
_Hh3ct1InterfaceInAlignErrs_Type = Counter32
_Hh3ct1InterfaceInAlignErrs_Object = MibTableColumn
hh3ct1InterfaceInAlignErrs = _Hh3ct1InterfaceInAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 5),
    _Hh3ct1InterfaceInAlignErrs_Type()
)
hh3ct1InterfaceInAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceInAlignErrs.setStatus("current")
_Hh3ct1InterfaceInOverRunsErrs_Type = Counter32
_Hh3ct1InterfaceInOverRunsErrs_Object = MibTableColumn
hh3ct1InterfaceInOverRunsErrs = _Hh3ct1InterfaceInOverRunsErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 6),
    _Hh3ct1InterfaceInOverRunsErrs_Type()
)
hh3ct1InterfaceInOverRunsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceInOverRunsErrs.setStatus("current")
_Hh3ct1InterfaceInDribblesErrs_Type = Counter32
_Hh3ct1InterfaceInDribblesErrs_Object = MibTableColumn
hh3ct1InterfaceInDribblesErrs = _Hh3ct1InterfaceInDribblesErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 7),
    _Hh3ct1InterfaceInDribblesErrs_Type()
)
hh3ct1InterfaceInDribblesErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceInDribblesErrs.setStatus("current")
_Hh3ct1InterfaceInAbortedSeqErrs_Type = Counter32
_Hh3ct1InterfaceInAbortedSeqErrs_Object = MibTableColumn
hh3ct1InterfaceInAbortedSeqErrs = _Hh3ct1InterfaceInAbortedSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 8),
    _Hh3ct1InterfaceInAbortedSeqErrs_Type()
)
hh3ct1InterfaceInAbortedSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceInAbortedSeqErrs.setStatus("current")
_Hh3ct1InterfaceInNoBufferErrs_Type = Counter32
_Hh3ct1InterfaceInNoBufferErrs_Object = MibTableColumn
hh3ct1InterfaceInNoBufferErrs = _Hh3ct1InterfaceInNoBufferErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 9),
    _Hh3ct1InterfaceInNoBufferErrs_Type()
)
hh3ct1InterfaceInNoBufferErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceInNoBufferErrs.setStatus("current")
_Hh3ct1InterfaceInFramingErrs_Type = Counter32
_Hh3ct1InterfaceInFramingErrs_Object = MibTableColumn
hh3ct1InterfaceInFramingErrs = _Hh3ct1InterfaceInFramingErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 10),
    _Hh3ct1InterfaceInFramingErrs_Type()
)
hh3ct1InterfaceInFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceInFramingErrs.setStatus("current")
_Hh3ct1InterfaceOutputErrs_Type = Counter32
_Hh3ct1InterfaceOutputErrs_Object = MibTableColumn
hh3ct1InterfaceOutputErrs = _Hh3ct1InterfaceOutputErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 11),
    _Hh3ct1InterfaceOutputErrs_Type()
)
hh3ct1InterfaceOutputErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceOutputErrs.setStatus("current")
_Hh3ct1InterfaceOutUnderRunErrs_Type = Counter32
_Hh3ct1InterfaceOutUnderRunErrs_Object = MibTableColumn
hh3ct1InterfaceOutUnderRunErrs = _Hh3ct1InterfaceOutUnderRunErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 12),
    _Hh3ct1InterfaceOutUnderRunErrs_Type()
)
hh3ct1InterfaceOutUnderRunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceOutUnderRunErrs.setStatus("current")
_Hh3ct1InterfaceOutCollisonsErrs_Type = Counter32
_Hh3ct1InterfaceOutCollisonsErrs_Object = MibTableColumn
hh3ct1InterfaceOutCollisonsErrs = _Hh3ct1InterfaceOutCollisonsErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 13),
    _Hh3ct1InterfaceOutCollisonsErrs_Type()
)
hh3ct1InterfaceOutCollisonsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceOutCollisonsErrs.setStatus("current")
_Hh3ct1InterfaceOutDeferedErrs_Type = Counter32
_Hh3ct1InterfaceOutDeferedErrs_Object = MibTableColumn
hh3ct1InterfaceOutDeferedErrs = _Hh3ct1InterfaceOutDeferedErrs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 1, 1, 14),
    _Hh3ct1InterfaceOutDeferedErrs_Type()
)
hh3ct1InterfaceOutDeferedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1InterfaceOutDeferedErrs.setStatus("current")
_Hh3ct1Table_Object = MibTable
hh3ct1Table = _Hh3ct1Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 2)
)
if mibBuilder.loadTexts:
    hh3ct1Table.setStatus("current")
_Hh3ct1Entry_Object = MibTableRow
hh3ct1Entry = _Hh3ct1Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 2, 1)
)
hh3ct1Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3ct1Entry.setStatus("current")


class _Hh3ct1Type_Type(Bits):
    """Custom type hh3ct1Type based on Bits"""
    namedValues = NamedValues(
        ("voice", 0)
    )

_Hh3ct1Type_Type.__name__ = "Bits"
_Hh3ct1Type_Object = MibTableColumn
hh3ct1Type = _Hh3ct1Type_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 2, 1, 1),
    _Hh3ct1Type_Type()
)
hh3ct1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1Type.setStatus("current")


class _Hh3ct1Clock_Type(Integer32):
    """Custom type hh3ct1Clock based on Integer32"""
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


_Hh3ct1Clock_Type.__name__ = "Integer32"
_Hh3ct1Clock_Object = MibTableColumn
hh3ct1Clock = _Hh3ct1Clock_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 2, 1, 2),
    _Hh3ct1Clock_Type()
)
hh3ct1Clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3ct1Clock.setStatus("current")


class _Hh3ct1FrameFormat_Type(Integer32):
    """Custom type hh3ct1FrameFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("esf", 2),
          ("sf", 1))
    )


_Hh3ct1FrameFormat_Type.__name__ = "Integer32"
_Hh3ct1FrameFormat_Object = MibTableColumn
hh3ct1FrameFormat = _Hh3ct1FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 2, 1, 3),
    _Hh3ct1FrameFormat_Type()
)
hh3ct1FrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3ct1FrameFormat.setStatus("current")


class _Hh3ct1LineCode_Type(Integer32):
    """Custom type hh3ct1LineCode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2))
    )


_Hh3ct1LineCode_Type.__name__ = "Integer32"
_Hh3ct1LineCode_Object = MibTableColumn
hh3ct1LineCode = _Hh3ct1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 2, 1, 4),
    _Hh3ct1LineCode_Type()
)
hh3ct1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3ct1LineCode.setStatus("current")
_Hh3ct1PriSetTimeSlot_Type = Hh3cT1TimeSlot
_Hh3ct1PriSetTimeSlot_Object = MibTableColumn
hh3ct1PriSetTimeSlot = _Hh3ct1PriSetTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 2, 1, 5),
    _Hh3ct1PriSetTimeSlot_Type()
)
hh3ct1PriSetTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3ct1PriSetTimeSlot.setStatus("current")
_Hh3ct1DChannelIndex_Type = Integer32
_Hh3ct1DChannelIndex_Object = MibTableColumn
hh3ct1DChannelIndex = _Hh3ct1DChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 2, 1, 6),
    _Hh3ct1DChannelIndex_Type()
)
hh3ct1DChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1DChannelIndex.setStatus("current")
_Hh3ct1SubScribLineChannelIndex_Type = Integer32
_Hh3ct1SubScribLineChannelIndex_Object = MibTableColumn
hh3ct1SubScribLineChannelIndex = _Hh3ct1SubScribLineChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 2, 1, 7),
    _Hh3ct1SubScribLineChannelIndex_Type()
)
hh3ct1SubScribLineChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1SubScribLineChannelIndex.setStatus("current")
_Hh3ct1InterfaceTable_Object = MibTable
hh3ct1InterfaceTable = _Hh3ct1InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 3)
)
if mibBuilder.loadTexts:
    hh3ct1InterfaceTable.setStatus("current")
_Hh3ct1InterfaceEntry_Object = MibTableRow
hh3ct1InterfaceEntry = _Hh3ct1InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 3, 1)
)
hh3ct1InterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3ct1InterfaceEntry.setStatus("current")
_Hh3ct1ControllerIndex_Type = Integer32
_Hh3ct1ControllerIndex_Object = MibTableColumn
hh3ct1ControllerIndex = _Hh3ct1ControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29, 3, 1, 1),
    _Hh3ct1ControllerIndex_Type()
)
hh3ct1ControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3ct1ControllerIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-T1-MIB",
    **{"Hh3cT1TimeSlot": Hh3cT1TimeSlot,
       "hh3cT1": hh3cT1,
       "hh3ct1InterfaceStatusTable": hh3ct1InterfaceStatusTable,
       "hh3ct1InterfaceStatusEntry": hh3ct1InterfaceStatusEntry,
       "hh3ct1InterfaceInErrs": hh3ct1InterfaceInErrs,
       "hh3ct1InterfaceInRuntsErrs": hh3ct1InterfaceInRuntsErrs,
       "hh3ct1InterfaceInGiantsErrs": hh3ct1InterfaceInGiantsErrs,
       "hh3ct1InterfaceInCrcErrs": hh3ct1InterfaceInCrcErrs,
       "hh3ct1InterfaceInAlignErrs": hh3ct1InterfaceInAlignErrs,
       "hh3ct1InterfaceInOverRunsErrs": hh3ct1InterfaceInOverRunsErrs,
       "hh3ct1InterfaceInDribblesErrs": hh3ct1InterfaceInDribblesErrs,
       "hh3ct1InterfaceInAbortedSeqErrs": hh3ct1InterfaceInAbortedSeqErrs,
       "hh3ct1InterfaceInNoBufferErrs": hh3ct1InterfaceInNoBufferErrs,
       "hh3ct1InterfaceInFramingErrs": hh3ct1InterfaceInFramingErrs,
       "hh3ct1InterfaceOutputErrs": hh3ct1InterfaceOutputErrs,
       "hh3ct1InterfaceOutUnderRunErrs": hh3ct1InterfaceOutUnderRunErrs,
       "hh3ct1InterfaceOutCollisonsErrs": hh3ct1InterfaceOutCollisonsErrs,
       "hh3ct1InterfaceOutDeferedErrs": hh3ct1InterfaceOutDeferedErrs,
       "hh3ct1Table": hh3ct1Table,
       "hh3ct1Entry": hh3ct1Entry,
       "hh3ct1Type": hh3ct1Type,
       "hh3ct1Clock": hh3ct1Clock,
       "hh3ct1FrameFormat": hh3ct1FrameFormat,
       "hh3ct1LineCode": hh3ct1LineCode,
       "hh3ct1PriSetTimeSlot": hh3ct1PriSetTimeSlot,
       "hh3ct1DChannelIndex": hh3ct1DChannelIndex,
       "hh3ct1SubScribLineChannelIndex": hh3ct1SubScribLineChannelIndex,
       "hh3ct1InterfaceTable": hh3ct1InterfaceTable,
       "hh3ct1InterfaceEntry": hh3ct1InterfaceEntry,
       "hh3ct1ControllerIndex": hh3ct1ControllerIndex}
)

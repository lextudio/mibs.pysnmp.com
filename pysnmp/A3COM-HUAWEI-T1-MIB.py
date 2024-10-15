# SNMP MIB module (A3COM-HUAWEI-T1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-T1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:10 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cT1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29)
)
h3cT1.setRevisions(
        ("2009-06-08 17:41",
         "2004-12-01 14:36")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cT1TimeSlot(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



# MIB Managed Objects in the order of their OIDs

_T1InterfaceStatusTable_Object = MibTable
t1InterfaceStatusTable = _T1InterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1)
)
if mibBuilder.loadTexts:
    t1InterfaceStatusTable.setStatus("current")
_T1InterfaceStatusEntry_Object = MibTableRow
t1InterfaceStatusEntry = _T1InterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1)
)
t1InterfaceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    t1InterfaceStatusEntry.setStatus("current")
_T1InterfaceInErrs_Type = Counter32
_T1InterfaceInErrs_Object = MibTableColumn
t1InterfaceInErrs = _T1InterfaceInErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 1),
    _T1InterfaceInErrs_Type()
)
t1InterfaceInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceInErrs.setStatus("current")
_T1InterfaceInRuntsErrs_Type = Counter32
_T1InterfaceInRuntsErrs_Object = MibTableColumn
t1InterfaceInRuntsErrs = _T1InterfaceInRuntsErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 2),
    _T1InterfaceInRuntsErrs_Type()
)
t1InterfaceInRuntsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceInRuntsErrs.setStatus("current")
_T1InterfaceInGiantsErrs_Type = Counter32
_T1InterfaceInGiantsErrs_Object = MibTableColumn
t1InterfaceInGiantsErrs = _T1InterfaceInGiantsErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 3),
    _T1InterfaceInGiantsErrs_Type()
)
t1InterfaceInGiantsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceInGiantsErrs.setStatus("current")
_T1InterfaceInCrcErrs_Type = Counter32
_T1InterfaceInCrcErrs_Object = MibTableColumn
t1InterfaceInCrcErrs = _T1InterfaceInCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 4),
    _T1InterfaceInCrcErrs_Type()
)
t1InterfaceInCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceInCrcErrs.setStatus("current")
_T1InterfaceInAlignErrs_Type = Counter32
_T1InterfaceInAlignErrs_Object = MibTableColumn
t1InterfaceInAlignErrs = _T1InterfaceInAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 5),
    _T1InterfaceInAlignErrs_Type()
)
t1InterfaceInAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceInAlignErrs.setStatus("current")
_T1InterfaceInOverRunsErrs_Type = Counter32
_T1InterfaceInOverRunsErrs_Object = MibTableColumn
t1InterfaceInOverRunsErrs = _T1InterfaceInOverRunsErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 6),
    _T1InterfaceInOverRunsErrs_Type()
)
t1InterfaceInOverRunsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceInOverRunsErrs.setStatus("current")
_T1InterfaceInDribblesErrs_Type = Counter32
_T1InterfaceInDribblesErrs_Object = MibTableColumn
t1InterfaceInDribblesErrs = _T1InterfaceInDribblesErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 7),
    _T1InterfaceInDribblesErrs_Type()
)
t1InterfaceInDribblesErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceInDribblesErrs.setStatus("current")
_T1InterfaceInAbortedSeqErrs_Type = Counter32
_T1InterfaceInAbortedSeqErrs_Object = MibTableColumn
t1InterfaceInAbortedSeqErrs = _T1InterfaceInAbortedSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 8),
    _T1InterfaceInAbortedSeqErrs_Type()
)
t1InterfaceInAbortedSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceInAbortedSeqErrs.setStatus("current")
_T1InterfaceInNoBufferErrs_Type = Counter32
_T1InterfaceInNoBufferErrs_Object = MibTableColumn
t1InterfaceInNoBufferErrs = _T1InterfaceInNoBufferErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 9),
    _T1InterfaceInNoBufferErrs_Type()
)
t1InterfaceInNoBufferErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceInNoBufferErrs.setStatus("current")
_T1InterfaceInFramingErrs_Type = Counter32
_T1InterfaceInFramingErrs_Object = MibTableColumn
t1InterfaceInFramingErrs = _T1InterfaceInFramingErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 10),
    _T1InterfaceInFramingErrs_Type()
)
t1InterfaceInFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceInFramingErrs.setStatus("current")
_T1InterfaceOutputErrs_Type = Counter32
_T1InterfaceOutputErrs_Object = MibTableColumn
t1InterfaceOutputErrs = _T1InterfaceOutputErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 11),
    _T1InterfaceOutputErrs_Type()
)
t1InterfaceOutputErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceOutputErrs.setStatus("current")
_T1InterfaceOutUnderRunErrs_Type = Counter32
_T1InterfaceOutUnderRunErrs_Object = MibTableColumn
t1InterfaceOutUnderRunErrs = _T1InterfaceOutUnderRunErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 12),
    _T1InterfaceOutUnderRunErrs_Type()
)
t1InterfaceOutUnderRunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceOutUnderRunErrs.setStatus("current")
_T1InterfaceOutCollisonsErrs_Type = Counter32
_T1InterfaceOutCollisonsErrs_Object = MibTableColumn
t1InterfaceOutCollisonsErrs = _T1InterfaceOutCollisonsErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 13),
    _T1InterfaceOutCollisonsErrs_Type()
)
t1InterfaceOutCollisonsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceOutCollisonsErrs.setStatus("current")
_T1InterfaceOutDeferedErrs_Type = Counter32
_T1InterfaceOutDeferedErrs_Object = MibTableColumn
t1InterfaceOutDeferedErrs = _T1InterfaceOutDeferedErrs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 1, 1, 14),
    _T1InterfaceOutDeferedErrs_Type()
)
t1InterfaceOutDeferedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1InterfaceOutDeferedErrs.setStatus("current")
_H3ct1Table_Object = MibTable
h3ct1Table = _H3ct1Table_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 2)
)
if mibBuilder.loadTexts:
    h3ct1Table.setStatus("current")
_H3ct1Entry_Object = MibTableRow
h3ct1Entry = _H3ct1Entry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 2, 1)
)
h3ct1Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3ct1Entry.setStatus("current")


class _H3ct1Type_Type(Bits):
    """Custom type h3ct1Type based on Bits"""
    namedValues = NamedValues(
        ("voice", 0)
    )

_H3ct1Type_Type.__name__ = "Bits"
_H3ct1Type_Object = MibTableColumn
h3ct1Type = _H3ct1Type_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 2, 1, 1),
    _H3ct1Type_Type()
)
h3ct1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3ct1Type.setStatus("current")


class _H3ct1Clock_Type(Integer32):
    """Custom type h3ct1Clock based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1))
    )


_H3ct1Clock_Type.__name__ = "Integer32"
_H3ct1Clock_Object = MibTableColumn
h3ct1Clock = _H3ct1Clock_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 2, 1, 2),
    _H3ct1Clock_Type()
)
h3ct1Clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3ct1Clock.setStatus("current")


class _H3ct1FrameFormat_Type(Integer32):
    """Custom type h3ct1FrameFormat based on Integer32"""
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


_H3ct1FrameFormat_Type.__name__ = "Integer32"
_H3ct1FrameFormat_Object = MibTableColumn
h3ct1FrameFormat = _H3ct1FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 2, 1, 3),
    _H3ct1FrameFormat_Type()
)
h3ct1FrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3ct1FrameFormat.setStatus("current")


class _H3ct1LineCode_Type(Integer32):
    """Custom type h3ct1LineCode based on Integer32"""
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


_H3ct1LineCode_Type.__name__ = "Integer32"
_H3ct1LineCode_Object = MibTableColumn
h3ct1LineCode = _H3ct1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 2, 1, 4),
    _H3ct1LineCode_Type()
)
h3ct1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3ct1LineCode.setStatus("current")
_H3ct1PriSetTimeSlot_Type = H3cT1TimeSlot
_H3ct1PriSetTimeSlot_Object = MibTableColumn
h3ct1PriSetTimeSlot = _H3ct1PriSetTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 2, 1, 5),
    _H3ct1PriSetTimeSlot_Type()
)
h3ct1PriSetTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3ct1PriSetTimeSlot.setStatus("current")
_H3ct1DChannelIndex_Type = Integer32
_H3ct1DChannelIndex_Object = MibTableColumn
h3ct1DChannelIndex = _H3ct1DChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 2, 1, 6),
    _H3ct1DChannelIndex_Type()
)
h3ct1DChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3ct1DChannelIndex.setStatus("current")
_H3ct1SubScribLineChannelIndex_Type = Integer32
_H3ct1SubScribLineChannelIndex_Object = MibTableColumn
h3ct1SubScribLineChannelIndex = _H3ct1SubScribLineChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 2, 1, 7),
    _H3ct1SubScribLineChannelIndex_Type()
)
h3ct1SubScribLineChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3ct1SubScribLineChannelIndex.setStatus("current")
_H3ct1InterfaceTable_Object = MibTable
h3ct1InterfaceTable = _H3ct1InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 3)
)
if mibBuilder.loadTexts:
    h3ct1InterfaceTable.setStatus("current")
_H3ct1InterfaceEntry_Object = MibTableRow
h3ct1InterfaceEntry = _H3ct1InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 3, 1)
)
h3ct1InterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3ct1InterfaceEntry.setStatus("current")
_H3ct1ControllerIndex_Type = Integer32
_H3ct1ControllerIndex_Object = MibTableColumn
h3ct1ControllerIndex = _H3ct1ControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 29, 3, 1, 1),
    _H3ct1ControllerIndex_Type()
)
h3ct1ControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3ct1ControllerIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-T1-MIB",
    **{"H3cT1TimeSlot": H3cT1TimeSlot,
       "h3cT1": h3cT1,
       "t1InterfaceStatusTable": t1InterfaceStatusTable,
       "t1InterfaceStatusEntry": t1InterfaceStatusEntry,
       "t1InterfaceInErrs": t1InterfaceInErrs,
       "t1InterfaceInRuntsErrs": t1InterfaceInRuntsErrs,
       "t1InterfaceInGiantsErrs": t1InterfaceInGiantsErrs,
       "t1InterfaceInCrcErrs": t1InterfaceInCrcErrs,
       "t1InterfaceInAlignErrs": t1InterfaceInAlignErrs,
       "t1InterfaceInOverRunsErrs": t1InterfaceInOverRunsErrs,
       "t1InterfaceInDribblesErrs": t1InterfaceInDribblesErrs,
       "t1InterfaceInAbortedSeqErrs": t1InterfaceInAbortedSeqErrs,
       "t1InterfaceInNoBufferErrs": t1InterfaceInNoBufferErrs,
       "t1InterfaceInFramingErrs": t1InterfaceInFramingErrs,
       "t1InterfaceOutputErrs": t1InterfaceOutputErrs,
       "t1InterfaceOutUnderRunErrs": t1InterfaceOutUnderRunErrs,
       "t1InterfaceOutCollisonsErrs": t1InterfaceOutCollisonsErrs,
       "t1InterfaceOutDeferedErrs": t1InterfaceOutDeferedErrs,
       "h3ct1Table": h3ct1Table,
       "h3ct1Entry": h3ct1Entry,
       "h3ct1Type": h3ct1Type,
       "h3ct1Clock": h3ct1Clock,
       "h3ct1FrameFormat": h3ct1FrameFormat,
       "h3ct1LineCode": h3ct1LineCode,
       "h3ct1PriSetTimeSlot": h3ct1PriSetTimeSlot,
       "h3ct1DChannelIndex": h3ct1DChannelIndex,
       "h3ct1SubScribLineChannelIndex": h3ct1SubScribLineChannelIndex,
       "h3ct1InterfaceTable": h3ct1InterfaceTable,
       "h3ct1InterfaceEntry": h3ct1InterfaceEntry,
       "h3ct1ControllerIndex": h3ct1ControllerIndex}
)

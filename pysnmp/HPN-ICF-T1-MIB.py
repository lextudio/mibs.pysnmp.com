# SNMP MIB module (HPN-ICF-T1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-T1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:58 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfT1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29)
)
hpnicfT1.setRevisions(
        ("2012-07-16 17:41",
         "2009-06-08 17:41",
         "2004-12-01 14:36")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfT1TimeSlot(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



# MIB Managed Objects in the order of their OIDs

_Hpnicft1InterfaceStatusTable_Object = MibTable
hpnicft1InterfaceStatusTable = _Hpnicft1InterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1)
)
if mibBuilder.loadTexts:
    hpnicft1InterfaceStatusTable.setStatus("current")
_Hpnicft1InterfaceStatusEntry_Object = MibTableRow
hpnicft1InterfaceStatusEntry = _Hpnicft1InterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1)
)
hpnicft1InterfaceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicft1InterfaceStatusEntry.setStatus("current")
_Hpnicft1InterfaceInErrs_Type = Counter32
_Hpnicft1InterfaceInErrs_Object = MibTableColumn
hpnicft1InterfaceInErrs = _Hpnicft1InterfaceInErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 1),
    _Hpnicft1InterfaceInErrs_Type()
)
hpnicft1InterfaceInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceInErrs.setStatus("current")
_Hpnicft1InterfaceInRuntsErrs_Type = Counter32
_Hpnicft1InterfaceInRuntsErrs_Object = MibTableColumn
hpnicft1InterfaceInRuntsErrs = _Hpnicft1InterfaceInRuntsErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 2),
    _Hpnicft1InterfaceInRuntsErrs_Type()
)
hpnicft1InterfaceInRuntsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceInRuntsErrs.setStatus("current")
_Hpnicft1InterfaceInGiantsErrs_Type = Counter32
_Hpnicft1InterfaceInGiantsErrs_Object = MibTableColumn
hpnicft1InterfaceInGiantsErrs = _Hpnicft1InterfaceInGiantsErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 3),
    _Hpnicft1InterfaceInGiantsErrs_Type()
)
hpnicft1InterfaceInGiantsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceInGiantsErrs.setStatus("current")
_Hpnicft1InterfaceInCrcErrs_Type = Counter32
_Hpnicft1InterfaceInCrcErrs_Object = MibTableColumn
hpnicft1InterfaceInCrcErrs = _Hpnicft1InterfaceInCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 4),
    _Hpnicft1InterfaceInCrcErrs_Type()
)
hpnicft1InterfaceInCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceInCrcErrs.setStatus("current")
_Hpnicft1InterfaceInAlignErrs_Type = Counter32
_Hpnicft1InterfaceInAlignErrs_Object = MibTableColumn
hpnicft1InterfaceInAlignErrs = _Hpnicft1InterfaceInAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 5),
    _Hpnicft1InterfaceInAlignErrs_Type()
)
hpnicft1InterfaceInAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceInAlignErrs.setStatus("current")
_Hpnicft1InterfaceInOverRunsErrs_Type = Counter32
_Hpnicft1InterfaceInOverRunsErrs_Object = MibTableColumn
hpnicft1InterfaceInOverRunsErrs = _Hpnicft1InterfaceInOverRunsErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 6),
    _Hpnicft1InterfaceInOverRunsErrs_Type()
)
hpnicft1InterfaceInOverRunsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceInOverRunsErrs.setStatus("current")
_Hpnicft1InterfaceInDribblesErrs_Type = Counter32
_Hpnicft1InterfaceInDribblesErrs_Object = MibTableColumn
hpnicft1InterfaceInDribblesErrs = _Hpnicft1InterfaceInDribblesErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 7),
    _Hpnicft1InterfaceInDribblesErrs_Type()
)
hpnicft1InterfaceInDribblesErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceInDribblesErrs.setStatus("current")
_Hpnicft1InterfaceInAbortedSeqErrs_Type = Counter32
_Hpnicft1InterfaceInAbortedSeqErrs_Object = MibTableColumn
hpnicft1InterfaceInAbortedSeqErrs = _Hpnicft1InterfaceInAbortedSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 8),
    _Hpnicft1InterfaceInAbortedSeqErrs_Type()
)
hpnicft1InterfaceInAbortedSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceInAbortedSeqErrs.setStatus("current")
_Hpnicft1InterfaceInNoBufferErrs_Type = Counter32
_Hpnicft1InterfaceInNoBufferErrs_Object = MibTableColumn
hpnicft1InterfaceInNoBufferErrs = _Hpnicft1InterfaceInNoBufferErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 9),
    _Hpnicft1InterfaceInNoBufferErrs_Type()
)
hpnicft1InterfaceInNoBufferErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceInNoBufferErrs.setStatus("current")
_Hpnicft1InterfaceInFramingErrs_Type = Counter32
_Hpnicft1InterfaceInFramingErrs_Object = MibTableColumn
hpnicft1InterfaceInFramingErrs = _Hpnicft1InterfaceInFramingErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 10),
    _Hpnicft1InterfaceInFramingErrs_Type()
)
hpnicft1InterfaceInFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceInFramingErrs.setStatus("current")
_Hpnicft1InterfaceOutputErrs_Type = Counter32
_Hpnicft1InterfaceOutputErrs_Object = MibTableColumn
hpnicft1InterfaceOutputErrs = _Hpnicft1InterfaceOutputErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 11),
    _Hpnicft1InterfaceOutputErrs_Type()
)
hpnicft1InterfaceOutputErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceOutputErrs.setStatus("current")
_Hpnicft1InterfaceOutUnderRunErrs_Type = Counter32
_Hpnicft1InterfaceOutUnderRunErrs_Object = MibTableColumn
hpnicft1InterfaceOutUnderRunErrs = _Hpnicft1InterfaceOutUnderRunErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 12),
    _Hpnicft1InterfaceOutUnderRunErrs_Type()
)
hpnicft1InterfaceOutUnderRunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceOutUnderRunErrs.setStatus("current")
_Hpnicft1InterfaceOutCollisonsErrs_Type = Counter32
_Hpnicft1InterfaceOutCollisonsErrs_Object = MibTableColumn
hpnicft1InterfaceOutCollisonsErrs = _Hpnicft1InterfaceOutCollisonsErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 13),
    _Hpnicft1InterfaceOutCollisonsErrs_Type()
)
hpnicft1InterfaceOutCollisonsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceOutCollisonsErrs.setStatus("current")
_Hpnicft1InterfaceOutDeferedErrs_Type = Counter32
_Hpnicft1InterfaceOutDeferedErrs_Object = MibTableColumn
hpnicft1InterfaceOutDeferedErrs = _Hpnicft1InterfaceOutDeferedErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 1, 1, 14),
    _Hpnicft1InterfaceOutDeferedErrs_Type()
)
hpnicft1InterfaceOutDeferedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1InterfaceOutDeferedErrs.setStatus("current")
_Hpnicft1Table_Object = MibTable
hpnicft1Table = _Hpnicft1Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2)
)
if mibBuilder.loadTexts:
    hpnicft1Table.setStatus("current")
_Hpnicft1Entry_Object = MibTableRow
hpnicft1Entry = _Hpnicft1Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1)
)
hpnicft1Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicft1Entry.setStatus("current")


class _Hpnicft1Type_Type(Bits):
    """Custom type hpnicft1Type based on Bits"""
    namedValues = NamedValues(
        ("voice", 0)
    )

_Hpnicft1Type_Type.__name__ = "Bits"
_Hpnicft1Type_Object = MibTableColumn
hpnicft1Type = _Hpnicft1Type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 1),
    _Hpnicft1Type_Type()
)
hpnicft1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1Type.setStatus("current")


class _Hpnicft1Clock_Type(Integer32):
    """Custom type hpnicft1Clock based on Integer32"""
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


_Hpnicft1Clock_Type.__name__ = "Integer32"
_Hpnicft1Clock_Object = MibTableColumn
hpnicft1Clock = _Hpnicft1Clock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 2),
    _Hpnicft1Clock_Type()
)
hpnicft1Clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicft1Clock.setStatus("current")


class _Hpnicft1FrameFormat_Type(Integer32):
    """Custom type hpnicft1FrameFormat based on Integer32"""
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


_Hpnicft1FrameFormat_Type.__name__ = "Integer32"
_Hpnicft1FrameFormat_Object = MibTableColumn
hpnicft1FrameFormat = _Hpnicft1FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 3),
    _Hpnicft1FrameFormat_Type()
)
hpnicft1FrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicft1FrameFormat.setStatus("current")


class _Hpnicft1LineCode_Type(Integer32):
    """Custom type hpnicft1LineCode based on Integer32"""
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


_Hpnicft1LineCode_Type.__name__ = "Integer32"
_Hpnicft1LineCode_Object = MibTableColumn
hpnicft1LineCode = _Hpnicft1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 4),
    _Hpnicft1LineCode_Type()
)
hpnicft1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicft1LineCode.setStatus("current")
_Hpnicft1PriSetTimeSlot_Type = HpnicfT1TimeSlot
_Hpnicft1PriSetTimeSlot_Object = MibTableColumn
hpnicft1PriSetTimeSlot = _Hpnicft1PriSetTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 5),
    _Hpnicft1PriSetTimeSlot_Type()
)
hpnicft1PriSetTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicft1PriSetTimeSlot.setStatus("current")
_Hpnicft1DChannelIndex_Type = Integer32
_Hpnicft1DChannelIndex_Object = MibTableColumn
hpnicft1DChannelIndex = _Hpnicft1DChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 6),
    _Hpnicft1DChannelIndex_Type()
)
hpnicft1DChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1DChannelIndex.setStatus("current")
_Hpnicft1SubScribLineChannelIndex_Type = Integer32
_Hpnicft1SubScribLineChannelIndex_Object = MibTableColumn
hpnicft1SubScribLineChannelIndex = _Hpnicft1SubScribLineChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 2, 1, 7),
    _Hpnicft1SubScribLineChannelIndex_Type()
)
hpnicft1SubScribLineChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1SubScribLineChannelIndex.setStatus("current")
_Hpnicft1InterfaceTable_Object = MibTable
hpnicft1InterfaceTable = _Hpnicft1InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 3)
)
if mibBuilder.loadTexts:
    hpnicft1InterfaceTable.setStatus("current")
_Hpnicft1InterfaceEntry_Object = MibTableRow
hpnicft1InterfaceEntry = _Hpnicft1InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 3, 1)
)
hpnicft1InterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicft1InterfaceEntry.setStatus("current")
_Hpnicft1ControllerIndex_Type = Integer32
_Hpnicft1ControllerIndex_Object = MibTableColumn
hpnicft1ControllerIndex = _Hpnicft1ControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29, 3, 1, 1),
    _Hpnicft1ControllerIndex_Type()
)
hpnicft1ControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicft1ControllerIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-T1-MIB",
    **{"HpnicfT1TimeSlot": HpnicfT1TimeSlot,
       "hpnicfT1": hpnicfT1,
       "hpnicft1InterfaceStatusTable": hpnicft1InterfaceStatusTable,
       "hpnicft1InterfaceStatusEntry": hpnicft1InterfaceStatusEntry,
       "hpnicft1InterfaceInErrs": hpnicft1InterfaceInErrs,
       "hpnicft1InterfaceInRuntsErrs": hpnicft1InterfaceInRuntsErrs,
       "hpnicft1InterfaceInGiantsErrs": hpnicft1InterfaceInGiantsErrs,
       "hpnicft1InterfaceInCrcErrs": hpnicft1InterfaceInCrcErrs,
       "hpnicft1InterfaceInAlignErrs": hpnicft1InterfaceInAlignErrs,
       "hpnicft1InterfaceInOverRunsErrs": hpnicft1InterfaceInOverRunsErrs,
       "hpnicft1InterfaceInDribblesErrs": hpnicft1InterfaceInDribblesErrs,
       "hpnicft1InterfaceInAbortedSeqErrs": hpnicft1InterfaceInAbortedSeqErrs,
       "hpnicft1InterfaceInNoBufferErrs": hpnicft1InterfaceInNoBufferErrs,
       "hpnicft1InterfaceInFramingErrs": hpnicft1InterfaceInFramingErrs,
       "hpnicft1InterfaceOutputErrs": hpnicft1InterfaceOutputErrs,
       "hpnicft1InterfaceOutUnderRunErrs": hpnicft1InterfaceOutUnderRunErrs,
       "hpnicft1InterfaceOutCollisonsErrs": hpnicft1InterfaceOutCollisonsErrs,
       "hpnicft1InterfaceOutDeferedErrs": hpnicft1InterfaceOutDeferedErrs,
       "hpnicft1Table": hpnicft1Table,
       "hpnicft1Entry": hpnicft1Entry,
       "hpnicft1Type": hpnicft1Type,
       "hpnicft1Clock": hpnicft1Clock,
       "hpnicft1FrameFormat": hpnicft1FrameFormat,
       "hpnicft1LineCode": hpnicft1LineCode,
       "hpnicft1PriSetTimeSlot": hpnicft1PriSetTimeSlot,
       "hpnicft1DChannelIndex": hpnicft1DChannelIndex,
       "hpnicft1SubScribLineChannelIndex": hpnicft1SubScribLineChannelIndex,
       "hpnicft1InterfaceTable": hpnicft1InterfaceTable,
       "hpnicft1InterfaceEntry": hpnicft1InterfaceEntry,
       "hpnicft1ControllerIndex": hpnicft1ControllerIndex}
)

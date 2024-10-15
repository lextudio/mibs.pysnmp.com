# SNMP MIB module (Wellfleet-PCAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-PCAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:52 2024
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

(wfPktCaptureGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfPktCaptureGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfPktCaptureTable_Object = MibTable
wfPktCaptureTable = _WfPktCaptureTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1)
)
if mibBuilder.loadTexts:
    wfPktCaptureTable.setStatus("mandatory")
_WfPktCaptureEntry_Object = MibTableRow
wfPktCaptureEntry = _WfPktCaptureEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1)
)
wfPktCaptureEntry.setIndexNames(
    (0, "Wellfleet-PCAP-MIB", "wfPktCaptureLineNumber"),
)
if mibBuilder.loadTexts:
    wfPktCaptureEntry.setStatus("mandatory")


class _WfPktCaptureDelete_Type(Integer32):
    """Custom type wfPktCaptureDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfPktCaptureDelete_Type.__name__ = "Integer32"
_WfPktCaptureDelete_Object = MibTableColumn
wfPktCaptureDelete = _WfPktCaptureDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 1),
    _WfPktCaptureDelete_Type()
)
wfPktCaptureDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureDelete.setStatus("mandatory")


class _WfPktCaptureDisable_Type(Integer32):
    """Custom type wfPktCaptureDisable based on Integer32"""
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


_WfPktCaptureDisable_Type.__name__ = "Integer32"
_WfPktCaptureDisable_Object = MibTableColumn
wfPktCaptureDisable = _WfPktCaptureDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 2),
    _WfPktCaptureDisable_Type()
)
wfPktCaptureDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureDisable.setStatus("mandatory")


class _WfPktCaptureState_Type(Integer32):
    """Custom type wfPktCaptureState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfPktCaptureState_Type.__name__ = "Integer32"
_WfPktCaptureState_Object = MibTableColumn
wfPktCaptureState = _WfPktCaptureState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 3),
    _WfPktCaptureState_Type()
)
wfPktCaptureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPktCaptureState.setStatus("mandatory")
_WfPktCaptureFname_Type = DisplayString
_WfPktCaptureFname_Object = MibTableColumn
wfPktCaptureFname = _WfPktCaptureFname_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 4),
    _WfPktCaptureFname_Type()
)
wfPktCaptureFname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPktCaptureFname.setStatus("mandatory")


class _WfPktCaptureControl_Type(Integer32):
    """Custom type wfPktCaptureControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_WfPktCaptureControl_Type.__name__ = "Integer32"
_WfPktCaptureControl_Object = MibTableColumn
wfPktCaptureControl = _WfPktCaptureControl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 5),
    _WfPktCaptureControl_Type()
)
wfPktCaptureControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureControl.setStatus("mandatory")


class _WfPktCaptureCapture_Type(Integer32):
    """Custom type wfPktCaptureCapture based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("started", 1),
          ("stopped", 2))
    )


_WfPktCaptureCapture_Type.__name__ = "Integer32"
_WfPktCaptureCapture_Object = MibTableColumn
wfPktCaptureCapture = _WfPktCaptureCapture_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 6),
    _WfPktCaptureCapture_Type()
)
wfPktCaptureCapture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPktCaptureCapture.setStatus("mandatory")
_WfPktCaptureLineNumber_Type = Integer32
_WfPktCaptureLineNumber_Object = MibTableColumn
wfPktCaptureLineNumber = _WfPktCaptureLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 7),
    _WfPktCaptureLineNumber_Type()
)
wfPktCaptureLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPktCaptureLineNumber.setStatus("mandatory")
_WfPktCaptureBufSize_Type = Integer32
_WfPktCaptureBufSize_Object = MibTableColumn
wfPktCaptureBufSize = _WfPktCaptureBufSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 8),
    _WfPktCaptureBufSize_Type()
)
wfPktCaptureBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureBufSize.setStatus("mandatory")
_WfPktCapturePktSize_Type = Integer32
_WfPktCapturePktSize_Object = MibTableColumn
wfPktCapturePktSize = _WfPktCapturePktSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 9),
    _WfPktCapturePktSize_Type()
)
wfPktCapturePktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCapturePktSize.setStatus("mandatory")


class _WfPktCaptureDirection_Type(Integer32):
    """Custom type wfPktCaptureDirection based on Integer32"""
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
        *(("both", 3),
          ("rx", 1),
          ("tx", 2))
    )


_WfPktCaptureDirection_Type.__name__ = "Integer32"
_WfPktCaptureDirection_Object = MibTableColumn
wfPktCaptureDirection = _WfPktCaptureDirection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 10),
    _WfPktCaptureDirection_Type()
)
wfPktCaptureDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureDirection.setStatus("mandatory")
_WfPktCaptureCount_Type = Gauge32
_WfPktCaptureCount_Object = MibTableColumn
wfPktCaptureCount = _WfPktCaptureCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 11),
    _WfPktCaptureCount_Type()
)
wfPktCaptureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPktCaptureCount.setStatus("mandatory")


class _WfPktCaptureRxTrigger_Type(Integer32):
    """Custom type wfPktCaptureRxTrigger based on Integer32"""
    defaultValue = 4

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
        *(("full", 1),
          ("match1", 2),
          ("match2", 3),
          ("notused", 4))
    )


_WfPktCaptureRxTrigger_Type.__name__ = "Integer32"
_WfPktCaptureRxTrigger_Object = MibTableColumn
wfPktCaptureRxTrigger = _WfPktCaptureRxTrigger_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 12),
    _WfPktCaptureRxTrigger_Type()
)
wfPktCaptureRxTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxTrigger.setStatus("mandatory")


class _WfPktCaptureTxTrigger_Type(Integer32):
    """Custom type wfPktCaptureTxTrigger based on Integer32"""
    defaultValue = 4

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
        *(("full", 1),
          ("match1", 2),
          ("match2", 3),
          ("notused", 4))
    )


_WfPktCaptureTxTrigger_Type.__name__ = "Integer32"
_WfPktCaptureTxTrigger_Object = MibTableColumn
wfPktCaptureTxTrigger = _WfPktCaptureTxTrigger_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 13),
    _WfPktCaptureTxTrigger_Type()
)
wfPktCaptureTxTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxTrigger.setStatus("mandatory")


class _WfPktCaptureRxFltr1Type_Type(Integer32):
    """Custom type wfPktCaptureRxFltr1Type based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("capture", 1),
          ("notused", 3),
          ("trigger", 2))
    )


_WfPktCaptureRxFltr1Type_Type.__name__ = "Integer32"
_WfPktCaptureRxFltr1Type_Object = MibTableColumn
wfPktCaptureRxFltr1Type = _WfPktCaptureRxFltr1Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 14),
    _WfPktCaptureRxFltr1Type_Type()
)
wfPktCaptureRxFltr1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxFltr1Type.setStatus("mandatory")
_WfPktCaptureRxFltr1Offset_Type = Integer32
_WfPktCaptureRxFltr1Offset_Object = MibTableColumn
wfPktCaptureRxFltr1Offset = _WfPktCaptureRxFltr1Offset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 15),
    _WfPktCaptureRxFltr1Offset_Type()
)
wfPktCaptureRxFltr1Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxFltr1Offset.setStatus("mandatory")


class _WfPktCaptureRxFltr1Ref_Type(Integer32):
    """Custom type wfPktCaptureRxFltr1Ref based on Integer32"""
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
        *(("dl", 2),
          ("mac", 1),
          ("mcast", 3))
    )


_WfPktCaptureRxFltr1Ref_Type.__name__ = "Integer32"
_WfPktCaptureRxFltr1Ref_Object = MibTableColumn
wfPktCaptureRxFltr1Ref = _WfPktCaptureRxFltr1Ref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 16),
    _WfPktCaptureRxFltr1Ref_Type()
)
wfPktCaptureRxFltr1Ref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxFltr1Ref.setStatus("mandatory")
_WfPktCaptureRxFltr1Size_Type = Integer32
_WfPktCaptureRxFltr1Size_Object = MibTableColumn
wfPktCaptureRxFltr1Size = _WfPktCaptureRxFltr1Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 17),
    _WfPktCaptureRxFltr1Size_Type()
)
wfPktCaptureRxFltr1Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxFltr1Size.setStatus("mandatory")
_WfPktCaptureRxFltr1Match_Type = OctetString
_WfPktCaptureRxFltr1Match_Object = MibTableColumn
wfPktCaptureRxFltr1Match = _WfPktCaptureRxFltr1Match_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 18),
    _WfPktCaptureRxFltr1Match_Type()
)
wfPktCaptureRxFltr1Match.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxFltr1Match.setStatus("mandatory")


class _WfPktCaptureTxFltr1Type_Type(Integer32):
    """Custom type wfPktCaptureTxFltr1Type based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("capture", 1),
          ("notused", 3),
          ("trigger", 2))
    )


_WfPktCaptureTxFltr1Type_Type.__name__ = "Integer32"
_WfPktCaptureTxFltr1Type_Object = MibTableColumn
wfPktCaptureTxFltr1Type = _WfPktCaptureTxFltr1Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 19),
    _WfPktCaptureTxFltr1Type_Type()
)
wfPktCaptureTxFltr1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxFltr1Type.setStatus("mandatory")
_WfPktCaptureTxFltr1Offset_Type = Integer32
_WfPktCaptureTxFltr1Offset_Object = MibTableColumn
wfPktCaptureTxFltr1Offset = _WfPktCaptureTxFltr1Offset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 20),
    _WfPktCaptureTxFltr1Offset_Type()
)
wfPktCaptureTxFltr1Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxFltr1Offset.setStatus("mandatory")


class _WfPktCaptureTxFltr1Ref_Type(Integer32):
    """Custom type wfPktCaptureTxFltr1Ref based on Integer32"""
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
        *(("dl", 2),
          ("mac", 1),
          ("mcast", 3))
    )


_WfPktCaptureTxFltr1Ref_Type.__name__ = "Integer32"
_WfPktCaptureTxFltr1Ref_Object = MibTableColumn
wfPktCaptureTxFltr1Ref = _WfPktCaptureTxFltr1Ref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 21),
    _WfPktCaptureTxFltr1Ref_Type()
)
wfPktCaptureTxFltr1Ref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxFltr1Ref.setStatus("mandatory")
_WfPktCaptureTxFltr1Size_Type = Integer32
_WfPktCaptureTxFltr1Size_Object = MibTableColumn
wfPktCaptureTxFltr1Size = _WfPktCaptureTxFltr1Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 22),
    _WfPktCaptureTxFltr1Size_Type()
)
wfPktCaptureTxFltr1Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxFltr1Size.setStatus("mandatory")
_WfPktCaptureTxFltr1Match_Type = OctetString
_WfPktCaptureTxFltr1Match_Object = MibTableColumn
wfPktCaptureTxFltr1Match = _WfPktCaptureTxFltr1Match_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 23),
    _WfPktCaptureTxFltr1Match_Type()
)
wfPktCaptureTxFltr1Match.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxFltr1Match.setStatus("mandatory")


class _WfPktCaptureRxFltr2Type_Type(Integer32):
    """Custom type wfPktCaptureRxFltr2Type based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("capture", 1),
          ("notused", 3),
          ("trigger", 2))
    )


_WfPktCaptureRxFltr2Type_Type.__name__ = "Integer32"
_WfPktCaptureRxFltr2Type_Object = MibTableColumn
wfPktCaptureRxFltr2Type = _WfPktCaptureRxFltr2Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 24),
    _WfPktCaptureRxFltr2Type_Type()
)
wfPktCaptureRxFltr2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxFltr2Type.setStatus("mandatory")
_WfPktCaptureRxFltr2Offset_Type = Integer32
_WfPktCaptureRxFltr2Offset_Object = MibTableColumn
wfPktCaptureRxFltr2Offset = _WfPktCaptureRxFltr2Offset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 25),
    _WfPktCaptureRxFltr2Offset_Type()
)
wfPktCaptureRxFltr2Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxFltr2Offset.setStatus("mandatory")


class _WfPktCaptureRxFltr2Ref_Type(Integer32):
    """Custom type wfPktCaptureRxFltr2Ref based on Integer32"""
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
        *(("dl", 2),
          ("mac", 1),
          ("mcast", 3))
    )


_WfPktCaptureRxFltr2Ref_Type.__name__ = "Integer32"
_WfPktCaptureRxFltr2Ref_Object = MibTableColumn
wfPktCaptureRxFltr2Ref = _WfPktCaptureRxFltr2Ref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 26),
    _WfPktCaptureRxFltr2Ref_Type()
)
wfPktCaptureRxFltr2Ref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxFltr2Ref.setStatus("mandatory")
_WfPktCaptureRxFltr2Size_Type = Integer32
_WfPktCaptureRxFltr2Size_Object = MibTableColumn
wfPktCaptureRxFltr2Size = _WfPktCaptureRxFltr2Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 27),
    _WfPktCaptureRxFltr2Size_Type()
)
wfPktCaptureRxFltr2Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxFltr2Size.setStatus("mandatory")
_WfPktCaptureRxFltr2Match_Type = OctetString
_WfPktCaptureRxFltr2Match_Object = MibTableColumn
wfPktCaptureRxFltr2Match = _WfPktCaptureRxFltr2Match_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 28),
    _WfPktCaptureRxFltr2Match_Type()
)
wfPktCaptureRxFltr2Match.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxFltr2Match.setStatus("mandatory")


class _WfPktCaptureRxFltr2Group_Type(Integer32):
    """Custom type wfPktCaptureRxFltr2Group based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("and", 2),
          ("or", 1))
    )


_WfPktCaptureRxFltr2Group_Type.__name__ = "Integer32"
_WfPktCaptureRxFltr2Group_Object = MibTableColumn
wfPktCaptureRxFltr2Group = _WfPktCaptureRxFltr2Group_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 29),
    _WfPktCaptureRxFltr2Group_Type()
)
wfPktCaptureRxFltr2Group.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureRxFltr2Group.setStatus("mandatory")


class _WfPktCaptureTxFltr2Type_Type(Integer32):
    """Custom type wfPktCaptureTxFltr2Type based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("capture", 1),
          ("notused", 3),
          ("trigger", 2))
    )


_WfPktCaptureTxFltr2Type_Type.__name__ = "Integer32"
_WfPktCaptureTxFltr2Type_Object = MibTableColumn
wfPktCaptureTxFltr2Type = _WfPktCaptureTxFltr2Type_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 30),
    _WfPktCaptureTxFltr2Type_Type()
)
wfPktCaptureTxFltr2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxFltr2Type.setStatus("mandatory")
_WfPktCaptureTxFltr2Offset_Type = Integer32
_WfPktCaptureTxFltr2Offset_Object = MibTableColumn
wfPktCaptureTxFltr2Offset = _WfPktCaptureTxFltr2Offset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 31),
    _WfPktCaptureTxFltr2Offset_Type()
)
wfPktCaptureTxFltr2Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxFltr2Offset.setStatus("mandatory")


class _WfPktCaptureTxFltr2Ref_Type(Integer32):
    """Custom type wfPktCaptureTxFltr2Ref based on Integer32"""
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
        *(("dl", 2),
          ("mac", 1),
          ("mcast", 3))
    )


_WfPktCaptureTxFltr2Ref_Type.__name__ = "Integer32"
_WfPktCaptureTxFltr2Ref_Object = MibTableColumn
wfPktCaptureTxFltr2Ref = _WfPktCaptureTxFltr2Ref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 32),
    _WfPktCaptureTxFltr2Ref_Type()
)
wfPktCaptureTxFltr2Ref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxFltr2Ref.setStatus("mandatory")
_WfPktCaptureTxFltr2Size_Type = Integer32
_WfPktCaptureTxFltr2Size_Object = MibTableColumn
wfPktCaptureTxFltr2Size = _WfPktCaptureTxFltr2Size_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 33),
    _WfPktCaptureTxFltr2Size_Type()
)
wfPktCaptureTxFltr2Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxFltr2Size.setStatus("mandatory")
_WfPktCaptureTxFltr2Match_Type = OctetString
_WfPktCaptureTxFltr2Match_Object = MibTableColumn
wfPktCaptureTxFltr2Match = _WfPktCaptureTxFltr2Match_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 34),
    _WfPktCaptureTxFltr2Match_Type()
)
wfPktCaptureTxFltr2Match.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxFltr2Match.setStatus("mandatory")


class _WfPktCaptureTxFltr2Group_Type(Integer32):
    """Custom type wfPktCaptureTxFltr2Group based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("and", 2),
          ("or", 1))
    )


_WfPktCaptureTxFltr2Group_Type.__name__ = "Integer32"
_WfPktCaptureTxFltr2Group_Object = MibTableColumn
wfPktCaptureTxFltr2Group = _WfPktCaptureTxFltr2Group_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 35),
    _WfPktCaptureTxFltr2Group_Type()
)
wfPktCaptureTxFltr2Group.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureTxFltr2Group.setStatus("mandatory")
_WfPktCaptureAtmVpi_Type = Integer32
_WfPktCaptureAtmVpi_Object = MibTableColumn
wfPktCaptureAtmVpi = _WfPktCaptureAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 36),
    _WfPktCaptureAtmVpi_Type()
)
wfPktCaptureAtmVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureAtmVpi.setStatus("mandatory")
_WfPktCaptureAtmVci_Type = Integer32
_WfPktCaptureAtmVci_Object = MibTableColumn
wfPktCaptureAtmVci = _WfPktCaptureAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 21, 1, 1, 37),
    _WfPktCaptureAtmVci_Type()
)
wfPktCaptureAtmVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPktCaptureAtmVci.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-PCAP-MIB",
    **{"wfPktCaptureTable": wfPktCaptureTable,
       "wfPktCaptureEntry": wfPktCaptureEntry,
       "wfPktCaptureDelete": wfPktCaptureDelete,
       "wfPktCaptureDisable": wfPktCaptureDisable,
       "wfPktCaptureState": wfPktCaptureState,
       "wfPktCaptureFname": wfPktCaptureFname,
       "wfPktCaptureControl": wfPktCaptureControl,
       "wfPktCaptureCapture": wfPktCaptureCapture,
       "wfPktCaptureLineNumber": wfPktCaptureLineNumber,
       "wfPktCaptureBufSize": wfPktCaptureBufSize,
       "wfPktCapturePktSize": wfPktCapturePktSize,
       "wfPktCaptureDirection": wfPktCaptureDirection,
       "wfPktCaptureCount": wfPktCaptureCount,
       "wfPktCaptureRxTrigger": wfPktCaptureRxTrigger,
       "wfPktCaptureTxTrigger": wfPktCaptureTxTrigger,
       "wfPktCaptureRxFltr1Type": wfPktCaptureRxFltr1Type,
       "wfPktCaptureRxFltr1Offset": wfPktCaptureRxFltr1Offset,
       "wfPktCaptureRxFltr1Ref": wfPktCaptureRxFltr1Ref,
       "wfPktCaptureRxFltr1Size": wfPktCaptureRxFltr1Size,
       "wfPktCaptureRxFltr1Match": wfPktCaptureRxFltr1Match,
       "wfPktCaptureTxFltr1Type": wfPktCaptureTxFltr1Type,
       "wfPktCaptureTxFltr1Offset": wfPktCaptureTxFltr1Offset,
       "wfPktCaptureTxFltr1Ref": wfPktCaptureTxFltr1Ref,
       "wfPktCaptureTxFltr1Size": wfPktCaptureTxFltr1Size,
       "wfPktCaptureTxFltr1Match": wfPktCaptureTxFltr1Match,
       "wfPktCaptureRxFltr2Type": wfPktCaptureRxFltr2Type,
       "wfPktCaptureRxFltr2Offset": wfPktCaptureRxFltr2Offset,
       "wfPktCaptureRxFltr2Ref": wfPktCaptureRxFltr2Ref,
       "wfPktCaptureRxFltr2Size": wfPktCaptureRxFltr2Size,
       "wfPktCaptureRxFltr2Match": wfPktCaptureRxFltr2Match,
       "wfPktCaptureRxFltr2Group": wfPktCaptureRxFltr2Group,
       "wfPktCaptureTxFltr2Type": wfPktCaptureTxFltr2Type,
       "wfPktCaptureTxFltr2Offset": wfPktCaptureTxFltr2Offset,
       "wfPktCaptureTxFltr2Ref": wfPktCaptureTxFltr2Ref,
       "wfPktCaptureTxFltr2Size": wfPktCaptureTxFltr2Size,
       "wfPktCaptureTxFltr2Match": wfPktCaptureTxFltr2Match,
       "wfPktCaptureTxFltr2Group": wfPktCaptureTxFltr2Group,
       "wfPktCaptureAtmVpi": wfPktCaptureAtmVpi,
       "wfPktCaptureAtmVci": wfPktCaptureAtmVci}
)

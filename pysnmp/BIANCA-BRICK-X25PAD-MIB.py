# SNMP MIB module (BIANCA-BRICK-X25PAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-X25PAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:52 2024
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


# MODULE-IDENTITY


# Types definitions



class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""




class Date(Integer32):
    """Custom type Date based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_X25_ObjectIdentity = ObjectIdentity
x25 = _X25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 6)
)
_X25PadProfileTable_Object = MibTable
x25PadProfileTable = _X25PadProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8)
)
if mibBuilder.loadTexts:
    x25PadProfileTable.setStatus("mandatory")
_X25PadProfileEntry_Object = MibTableRow
x25PadProfileEntry = _X25PadProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1)
)
x25PadProfileEntry.setIndexNames(
    (0, "BIANCA-BRICK-X25PAD-MIB", "x25PadProNumber"),
)
if mibBuilder.loadTexts:
    x25PadProfileEntry.setStatus("mandatory")


class _X25PadProNumber_Type(Integer32):
    """Custom type x25PadProNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_X25PadProNumber_Type.__name__ = "Integer32"
_X25PadProNumber_Object = MibTableColumn
x25PadProNumber = _X25PadProNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 1),
    _X25PadProNumber_Type()
)
x25PadProNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProNumber.setStatus("mandatory")


class _X25PadProState_Type(Integer32):
    """Custom type x25PadProState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("valid", 1))
    )


_X25PadProState_Type.__name__ = "Integer32"
_X25PadProState_Object = MibTableColumn
x25PadProState = _X25PadProState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 2),
    _X25PadProState_Type()
)
x25PadProState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProState.setStatus("mandatory")
_X25PadProAutoCallDstAddr_Type = DisplayString
_X25PadProAutoCallDstAddr_Object = MibTableColumn
x25PadProAutoCallDstAddr = _X25PadProAutoCallDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 3),
    _X25PadProAutoCallDstAddr_Type()
)
x25PadProAutoCallDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProAutoCallDstAddr.setStatus("mandatory")


class _X25PadProEscape_Type(Integer32):
    """Custom type x25PadProEscape based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_X25PadProEscape_Type.__name__ = "Integer32"
_X25PadProEscape_Object = MibTableColumn
x25PadProEscape = _X25PadProEscape_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 4),
    _X25PadProEscape_Type()
)
x25PadProEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProEscape.setStatus("mandatory")


class _X25PadProEcho_Type(Integer32):
    """Custom type x25PadProEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              256)
        )
    )
    namedValues = NamedValues(
        *(("echo", 1),
          ("no-echo", 256))
    )


_X25PadProEcho_Type.__name__ = "Integer32"
_X25PadProEcho_Object = MibTableColumn
x25PadProEcho = _X25PadProEcho_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 5),
    _X25PadProEcho_Type()
)
x25PadProEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProEcho.setStatus("mandatory")


class _X25PadProForwardChar_Type(Integer32):
    """Custom type x25PadProForwardChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_X25PadProForwardChar_Type.__name__ = "Integer32"
_X25PadProForwardChar_Object = MibTableColumn
x25PadProForwardChar = _X25PadProForwardChar_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 6),
    _X25PadProForwardChar_Type()
)
x25PadProForwardChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProForwardChar.setStatus("mandatory")


class _X25PadProIdleTimer_Type(Integer32):
    """Custom type x25PadProIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25PadProIdleTimer_Type.__name__ = "Integer32"
_X25PadProIdleTimer_Object = MibTableColumn
x25PadProIdleTimer = _X25PadProIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 7),
    _X25PadProIdleTimer_Type()
)
x25PadProIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProIdleTimer.setStatus("mandatory")


class _X25PadProDevControl_Type(Integer32):
    """Custom type x25PadProDevControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              256)
        )
    )
    namedValues = NamedValues(
        *(("no-use", 256),
          ("use", 2),
          ("use-only-data-transfer", 1))
    )


_X25PadProDevControl_Type.__name__ = "Integer32"
_X25PadProDevControl_Object = MibTableColumn
x25PadProDevControl = _X25PadProDevControl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 8),
    _X25PadProDevControl_Type()
)
x25PadProDevControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProDevControl.setStatus("mandatory")


class _X25PadProSigControl_Type(Integer32):
    """Custom type x25PadProSigControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_X25PadProSigControl_Type.__name__ = "Integer32"
_X25PadProSigControl_Object = MibTableColumn
x25PadProSigControl = _X25PadProSigControl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 9),
    _X25PadProSigControl_Type()
)
x25PadProSigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProSigControl.setStatus("mandatory")


class _X25PadProBrkControl_Type(Integer32):
    """Custom type x25PadProBrkControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_X25PadProBrkControl_Type.__name__ = "Integer32"
_X25PadProBrkControl_Object = MibTableColumn
x25PadProBrkControl = _X25PadProBrkControl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 10),
    _X25PadProBrkControl_Type()
)
x25PadProBrkControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProBrkControl.setStatus("mandatory")


class _X25PadProDiscard_Type(Integer32):
    """Custom type x25PadProDiscard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              256)
        )
    )
    namedValues = NamedValues(
        *(("discard-output", 1),
          ("normal-data-delivery", 256))
    )


_X25PadProDiscard_Type.__name__ = "Integer32"
_X25PadProDiscard_Object = MibTableColumn
x25PadProDiscard = _X25PadProDiscard_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 11),
    _X25PadProDiscard_Type()
)
x25PadProDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProDiscard.setStatus("mandatory")


class _X25PadProCRPadding_Type(Integer32):
    """Custom type x25PadProCRPadding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25PadProCRPadding_Type.__name__ = "Integer32"
_X25PadProCRPadding_Object = MibTableColumn
x25PadProCRPadding = _X25PadProCRPadding_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 12),
    _X25PadProCRPadding_Type()
)
x25PadProCRPadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProCRPadding.setStatus("mandatory")


class _X25PadProLineFold_Type(Integer32):
    """Custom type x25PadProLineFold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25PadProLineFold_Type.__name__ = "Integer32"
_X25PadProLineFold_Object = MibTableColumn
x25PadProLineFold = _X25PadProLineFold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 13),
    _X25PadProLineFold_Type()
)
x25PadProLineFold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProLineFold.setStatus("mandatory")


class _X25PadProFlowControl_Type(Integer32):
    """Custom type x25PadProFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              256)
        )
    )
    namedValues = NamedValues(
        *(("no-use-DC1-DC3", 256),
          ("use-DC1-DC3", 1))
    )


_X25PadProFlowControl_Type.__name__ = "Integer32"
_X25PadProFlowControl_Object = MibTableColumn
x25PadProFlowControl = _X25PadProFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 14),
    _X25PadProFlowControl_Type()
)
x25PadProFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProFlowControl.setStatus("mandatory")


class _X25PadProLFInsert_Type(Integer32):
    """Custom type x25PadProLFInsert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_X25PadProLFInsert_Type.__name__ = "Integer32"
_X25PadProLFInsert_Object = MibTableColumn
x25PadProLFInsert = _X25PadProLFInsert_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 15),
    _X25PadProLFInsert_Type()
)
x25PadProLFInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProLFInsert.setStatus("mandatory")


class _X25PadProLFPadding_Type(Integer32):
    """Custom type x25PadProLFPadding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25PadProLFPadding_Type.__name__ = "Integer32"
_X25PadProLFPadding_Object = MibTableColumn
x25PadProLFPadding = _X25PadProLFPadding_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 16),
    _X25PadProLFPadding_Type()
)
x25PadProLFPadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProLFPadding.setStatus("mandatory")


class _X25PadProEdit_Type(Integer32):
    """Custom type x25PadProEdit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              256)
        )
    )
    namedValues = NamedValues(
        *(("editing-user-data", 1),
          ("no-editing-user-data", 256))
    )


_X25PadProEdit_Type.__name__ = "Integer32"
_X25PadProEdit_Object = MibTableColumn
x25PadProEdit = _X25PadProEdit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 17),
    _X25PadProEdit_Type()
)
x25PadProEdit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProEdit.setStatus("mandatory")


class _X25PadProCharDel_Type(Integer32):
    """Custom type x25PadProCharDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25PadProCharDel_Type.__name__ = "Integer32"
_X25PadProCharDel_Object = MibTableColumn
x25PadProCharDel = _X25PadProCharDel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 18),
    _X25PadProCharDel_Type()
)
x25PadProCharDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProCharDel.setStatus("mandatory")


class _X25PadProLineDel_Type(Integer32):
    """Custom type x25PadProLineDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25PadProLineDel_Type.__name__ = "Integer32"
_X25PadProLineDel_Object = MibTableColumn
x25PadProLineDel = _X25PadProLineDel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 19),
    _X25PadProLineDel_Type()
)
x25PadProLineDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProLineDel.setStatus("mandatory")


class _X25PadProLineDisp_Type(Integer32):
    """Custom type x25PadProLineDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25PadProLineDisp_Type.__name__ = "Integer32"
_X25PadProLineDisp_Object = MibTableColumn
x25PadProLineDisp = _X25PadProLineDisp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 20),
    _X25PadProLineDisp_Type()
)
x25PadProLineDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProLineDisp.setStatus("mandatory")


class _X25PadProSigEdit_Type(Integer32):
    """Custom type x25PadProSigEdit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_X25PadProSigEdit_Type.__name__ = "Integer32"
_X25PadProSigEdit_Object = MibTableColumn
x25PadProSigEdit = _X25PadProSigEdit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 21),
    _X25PadProSigEdit_Type()
)
x25PadProSigEdit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProSigEdit.setStatus("mandatory")


class _X25PadProEchoMask_Type(Integer32):
    """Custom type x25PadProEchoMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_X25PadProEchoMask_Type.__name__ = "Integer32"
_X25PadProEchoMask_Object = MibTableColumn
x25PadProEchoMask = _X25PadProEchoMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 22),
    _X25PadProEchoMask_Type()
)
x25PadProEchoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProEchoMask.setStatus("mandatory")


class _X25PadProParity_Type(Integer32):
    """Custom type x25PadProParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              256)
        )
    )
    namedValues = NamedValues(
        *(("no-parity", 256),
          ("parity-checking", 1),
          ("parity-checking-generation", 3),
          ("parity-generation", 2))
    )


_X25PadProParity_Type.__name__ = "Integer32"
_X25PadProParity_Object = MibTableColumn
x25PadProParity = _X25PadProParity_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 23),
    _X25PadProParity_Type()
)
x25PadProParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProParity.setStatus("mandatory")


class _X25PadProPageWait_Type(Integer32):
    """Custom type x25PadProPageWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25PadProPageWait_Type.__name__ = "Integer32"
_X25PadProPageWait_Object = MibTableColumn
x25PadProPageWait = _X25PadProPageWait_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 24),
    _X25PadProPageWait_Type()
)
x25PadProPageWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProPageWait.setStatus("mandatory")


class _X25PadProXCharDel_Type(Integer32):
    """Custom type x25PadProXCharDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25PadProXCharDel_Type.__name__ = "Integer32"
_X25PadProXCharDel_Object = MibTableColumn
x25PadProXCharDel = _X25PadProXCharDel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 25),
    _X25PadProXCharDel_Type()
)
x25PadProXCharDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProXCharDel.setStatus("mandatory")


class _X25PadProXLineDel_Type(Integer32):
    """Custom type x25PadProXLineDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25PadProXLineDel_Type.__name__ = "Integer32"
_X25PadProXLineDel_Object = MibTableColumn
x25PadProXLineDel = _X25PadProXLineDel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 26),
    _X25PadProXLineDel_Type()
)
x25PadProXLineDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProXLineDel.setStatus("mandatory")


class _X25PadProXLineDisp_Type(Integer32):
    """Custom type x25PadProXLineDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25PadProXLineDisp_Type.__name__ = "Integer32"
_X25PadProXLineDisp_Object = MibTableColumn
x25PadProXLineDisp = _X25PadProXLineDisp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 27),
    _X25PadProXLineDisp_Type()
)
x25PadProXLineDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProXLineDisp.setStatus("mandatory")


class _X25PadProXForwardChar1_Type(Integer32):
    """Custom type x25PadProXForwardChar1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_X25PadProXForwardChar1_Type.__name__ = "Integer32"
_X25PadProXForwardChar1_Object = MibTableColumn
x25PadProXForwardChar1 = _X25PadProXForwardChar1_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 28),
    _X25PadProXForwardChar1_Type()
)
x25PadProXForwardChar1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProXForwardChar1.setStatus("mandatory")


class _X25PadProXForwardChar2_Type(Integer32):
    """Custom type x25PadProXForwardChar2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_X25PadProXForwardChar2_Type.__name__ = "Integer32"
_X25PadProXForwardChar2_Object = MibTableColumn
x25PadProXForwardChar2 = _X25PadProXForwardChar2_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 29),
    _X25PadProXForwardChar2_Type()
)
x25PadProXForwardChar2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProXForwardChar2.setStatus("mandatory")


class _X25PadProXParity_Type(Integer32):
    """Custom type x25PadProXParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              256)
        )
    )
    namedValues = NamedValues(
        *(("no-parity", 256),
          ("parity-checking", 3),
          ("parity-checking-generation", 1),
          ("parity-generation", 2))
    )


_X25PadProXParity_Type.__name__ = "Integer32"
_X25PadProXParity_Object = MibTableColumn
x25PadProXParity = _X25PadProXParity_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 30),
    _X25PadProXParity_Type()
)
x25PadProXParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProXParity.setStatus("mandatory")


class _X25PadProXDelay_Type(Integer32):
    """Custom type x25PadProXDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25PadProXDelay_Type.__name__ = "Integer32"
_X25PadProXDelay_Object = MibTableColumn
x25PadProXDelay = _X25PadProXDelay_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 31),
    _X25PadProXDelay_Type()
)
x25PadProXDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProXDelay.setStatus("mandatory")


class _X25PadProXLFInsert_Type(Integer32):
    """Custom type x25PadProXLFInsert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_X25PadProXLFInsert_Type.__name__ = "Integer32"
_X25PadProXLFInsert_Object = MibTableColumn
x25PadProXLFInsert = _X25PadProXLFInsert_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 8, 1, 32),
    _X25PadProXLFInsert_Type()
)
x25PadProXLFInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25PadProXLFInsert.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-X25PAD-MIB",
    **{"HexValue": HexValue,
       "Date": Date,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "x25": x25,
       "x25PadProfileTable": x25PadProfileTable,
       "x25PadProfileEntry": x25PadProfileEntry,
       "x25PadProNumber": x25PadProNumber,
       "x25PadProState": x25PadProState,
       "x25PadProAutoCallDstAddr": x25PadProAutoCallDstAddr,
       "x25PadProEscape": x25PadProEscape,
       "x25PadProEcho": x25PadProEcho,
       "x25PadProForwardChar": x25PadProForwardChar,
       "x25PadProIdleTimer": x25PadProIdleTimer,
       "x25PadProDevControl": x25PadProDevControl,
       "x25PadProSigControl": x25PadProSigControl,
       "x25PadProBrkControl": x25PadProBrkControl,
       "x25PadProDiscard": x25PadProDiscard,
       "x25PadProCRPadding": x25PadProCRPadding,
       "x25PadProLineFold": x25PadProLineFold,
       "x25PadProFlowControl": x25PadProFlowControl,
       "x25PadProLFInsert": x25PadProLFInsert,
       "x25PadProLFPadding": x25PadProLFPadding,
       "x25PadProEdit": x25PadProEdit,
       "x25PadProCharDel": x25PadProCharDel,
       "x25PadProLineDel": x25PadProLineDel,
       "x25PadProLineDisp": x25PadProLineDisp,
       "x25PadProSigEdit": x25PadProSigEdit,
       "x25PadProEchoMask": x25PadProEchoMask,
       "x25PadProParity": x25PadProParity,
       "x25PadProPageWait": x25PadProPageWait,
       "x25PadProXCharDel": x25PadProXCharDel,
       "x25PadProXLineDel": x25PadProXLineDel,
       "x25PadProXLineDisp": x25PadProXLineDisp,
       "x25PadProXForwardChar1": x25PadProXForwardChar1,
       "x25PadProXForwardChar2": x25PadProXForwardChar2,
       "x25PadProXParity": x25PadProXParity,
       "x25PadProXDelay": x25PadProXDelay,
       "x25PadProXLFInsert": x25PadProXLFInsert}
)

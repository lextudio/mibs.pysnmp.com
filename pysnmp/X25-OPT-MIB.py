# SNMP MIB module (X25-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/X25-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:37 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class Counter16(Integer32):
    """Custom type Counter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PPCTX25PortTable_Object = MibTable
cdx6500PPCTX25PortTable = _Cdx6500PPCTX25PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdx6500PPCTX25PortTable.setStatus("mandatory")
_Cdx6500PPCTX25PortEntry_Object = MibTableRow
cdx6500PPCTX25PortEntry = _Cdx6500PPCTX25PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1)
)
cdx6500PPCTX25PortEntry.setIndexNames(
    (0, "X25-OPT-MIB", "cdx6500X25CfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTX25PortEntry.setStatus("mandatory")


class _Cdx6500X25CfgPortNumber_Type(Integer32):
    """Custom type cdx6500X25CfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500X25CfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500X25CfgPortNumber_Object = MibTableColumn
cdx6500X25CfgPortNumber = _Cdx6500X25CfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 1),
    _Cdx6500X25CfgPortNumber_Type()
)
cdx6500X25CfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25CfgPortNumber.setStatus("mandatory")


class _Cdx6500X25CfgConnType_Type(Integer32):
    """Custom type cdx6500X25CfgConnType based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("dimo", 6),
          ("dimoa", 7),
          ("dimob", 8),
          ("dimov", 11),
          ("dtr", 2),
          ("dtrd", 3),
          ("emdc", 5),
          ("emri", 4),
          ("simp", 1),
          ("simpb", 21),
          ("simpv", 12))
    )


_Cdx6500X25CfgConnType_Type.__name__ = "Integer32"
_Cdx6500X25CfgConnType_Object = MibTableColumn
cdx6500X25CfgConnType = _Cdx6500X25CfgConnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 2),
    _Cdx6500X25CfgConnType_Type()
)
cdx6500X25CfgConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgConnType.setStatus("mandatory")


class _Cdx6500X25CfgPortCont_Type(DisplayString):
    """Custom type cdx6500X25CfgPortCont based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 7),
    )


_Cdx6500X25CfgPortCont_Type.__name__ = "DisplayString"
_Cdx6500X25CfgPortCont_Object = MibTableColumn
cdx6500X25CfgPortCont = _Cdx6500X25CfgPortCont_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 3),
    _Cdx6500X25CfgPortCont_Type()
)
cdx6500X25CfgPortCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgPortCont.setStatus("mandatory")


class _Cdx6500X25CfgClockSource_Type(Integer32):
    """Custom type cdx6500X25CfgClockSource based on Integer32"""
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
        *(("ext", 2),
          ("extint", 3),
          ("extlp", 4),
          ("int", 1))
    )


_Cdx6500X25CfgClockSource_Type.__name__ = "Integer32"
_Cdx6500X25CfgClockSource_Object = MibTableColumn
cdx6500X25CfgClockSource = _Cdx6500X25CfgClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 4),
    _Cdx6500X25CfgClockSource_Type()
)
cdx6500X25CfgClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgClockSource.setStatus("mandatory")


class _Cdx6500X25CfgClockSpeed_Type(Integer32):
    """Custom type cdx6500X25CfgClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 384000),
    )


_Cdx6500X25CfgClockSpeed_Type.__name__ = "Integer32"
_Cdx6500X25CfgClockSpeed_Object = MibTableColumn
cdx6500X25CfgClockSpeed = _Cdx6500X25CfgClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 5),
    _Cdx6500X25CfgClockSpeed_Type()
)
cdx6500X25CfgClockSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgClockSpeed.setStatus("mandatory")


class _Cdx6500X25CfgAdmnInterfaceMode_Type(Integer32):
    """Custom type cdx6500X25CfgAdmnInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1),
          ("negotiate", 3))
    )


_Cdx6500X25CfgAdmnInterfaceMode_Type.__name__ = "Integer32"
_Cdx6500X25CfgAdmnInterfaceMode_Object = MibTableColumn
cdx6500X25CfgAdmnInterfaceMode = _Cdx6500X25CfgAdmnInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 6),
    _Cdx6500X25CfgAdmnInterfaceMode_Type()
)
cdx6500X25CfgAdmnInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgAdmnInterfaceMode.setStatus("mandatory")


class _Cdx6500X25CfgAdmnNumberPVCs_Type(Integer32):
    """Custom type cdx6500X25CfgAdmnNumberPVCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Cdx6500X25CfgAdmnNumberPVCs_Type.__name__ = "Integer32"
_Cdx6500X25CfgAdmnNumberPVCs_Object = MibTableColumn
cdx6500X25CfgAdmnNumberPVCs = _Cdx6500X25CfgAdmnNumberPVCs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 7),
    _Cdx6500X25CfgAdmnNumberPVCs_Type()
)
cdx6500X25CfgAdmnNumberPVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgAdmnNumberPVCs.setStatus("mandatory")


class _Cdx6500X25CfgStartPVCChanNum_Type(Integer32):
    """Custom type cdx6500X25CfgStartPVCChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Cdx6500X25CfgStartPVCChanNum_Type.__name__ = "Integer32"
_Cdx6500X25CfgStartPVCChanNum_Object = MibTableColumn
cdx6500X25CfgStartPVCChanNum = _Cdx6500X25CfgStartPVCChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 8),
    _Cdx6500X25CfgStartPVCChanNum_Type()
)
cdx6500X25CfgStartPVCChanNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgStartPVCChanNum.setStatus("mandatory")


class _Cdx6500X25CfgNumberSVCs_Type(Integer32):
    """Custom type cdx6500X25CfgNumberSVCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Cdx6500X25CfgNumberSVCs_Type.__name__ = "Integer32"
_Cdx6500X25CfgNumberSVCs_Object = MibTableColumn
cdx6500X25CfgNumberSVCs = _Cdx6500X25CfgNumberSVCs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 9),
    _Cdx6500X25CfgNumberSVCs_Type()
)
cdx6500X25CfgNumberSVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgNumberSVCs.setStatus("mandatory")


class _Cdx6500X25CfgStartSVCChanNum_Type(Integer32):
    """Custom type cdx6500X25CfgStartSVCChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Cdx6500X25CfgStartSVCChanNum_Type.__name__ = "Integer32"
_Cdx6500X25CfgStartSVCChanNum_Object = MibTableColumn
cdx6500X25CfgStartSVCChanNum = _Cdx6500X25CfgStartSVCChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 10),
    _Cdx6500X25CfgStartSVCChanNum_Type()
)
cdx6500X25CfgStartSVCChanNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgStartSVCChanNum.setStatus("mandatory")


class _Cdx6500X25CfgInitFrame_Type(Integer32):
    """Custom type cdx6500X25CfgInitFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disc", 2),
          ("none", 3),
          ("sabm", 1))
    )


_Cdx6500X25CfgInitFrame_Type.__name__ = "Integer32"
_Cdx6500X25CfgInitFrame_Object = MibTableColumn
cdx6500X25CfgInitFrame = _Cdx6500X25CfgInitFrame_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 11),
    _Cdx6500X25CfgInitFrame_Type()
)
cdx6500X25CfgInitFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgInitFrame.setStatus("mandatory")


class _Cdx6500X25CfgT1RetryTimer_Type(Integer32):
    """Custom type cdx6500X25CfgT1RetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Cdx6500X25CfgT1RetryTimer_Type.__name__ = "Integer32"
_Cdx6500X25CfgT1RetryTimer_Object = MibTableColumn
cdx6500X25CfgT1RetryTimer = _Cdx6500X25CfgT1RetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 12),
    _Cdx6500X25CfgT1RetryTimer_Type()
)
cdx6500X25CfgT1RetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgT1RetryTimer.setStatus("mandatory")


class _Cdx6500X25CfgT4PollTimer_Type(Integer32):
    """Custom type cdx6500X25CfgT4PollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500X25CfgT4PollTimer_Type.__name__ = "Integer32"
_Cdx6500X25CfgT4PollTimer_Object = MibTableColumn
cdx6500X25CfgT4PollTimer = _Cdx6500X25CfgT4PollTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 13),
    _Cdx6500X25CfgT4PollTimer_Type()
)
cdx6500X25CfgT4PollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgT4PollTimer.setStatus("mandatory")


class _Cdx6500X25CfgN2TransTries_Type(Integer32):
    """Custom type cdx6500X25CfgN2TransTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Cdx6500X25CfgN2TransTries_Type.__name__ = "Integer32"
_Cdx6500X25CfgN2TransTries_Object = MibTableColumn
cdx6500X25CfgN2TransTries = _Cdx6500X25CfgN2TransTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 14),
    _Cdx6500X25CfgN2TransTries_Type()
)
cdx6500X25CfgN2TransTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgN2TransTries.setStatus("mandatory")


class _Cdx6500X25CfgFrameSeqCounting_Type(Integer32):
    """Custom type cdx6500X25CfgFrameSeqCounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ext", 2),
          ("norm", 1))
    )


_Cdx6500X25CfgFrameSeqCounting_Type.__name__ = "Integer32"
_Cdx6500X25CfgFrameSeqCounting_Object = MibTableColumn
cdx6500X25CfgFrameSeqCounting = _Cdx6500X25CfgFrameSeqCounting_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 15),
    _Cdx6500X25CfgFrameSeqCounting_Type()
)
cdx6500X25CfgFrameSeqCounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgFrameSeqCounting.setStatus("mandatory")


class _Cdx6500X25CfgKFrameWindow_Type(Integer32):
    """Custom type cdx6500X25CfgKFrameWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Cdx6500X25CfgKFrameWindow_Type.__name__ = "Integer32"
_Cdx6500X25CfgKFrameWindow_Object = MibTableColumn
cdx6500X25CfgKFrameWindow = _Cdx6500X25CfgKFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 16),
    _Cdx6500X25CfgKFrameWindow_Type()
)
cdx6500X25CfgKFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgKFrameWindow.setStatus("mandatory")


class _Cdx6500X25CfgAdmnPacketSequencing_Type(Integer32):
    """Custom type cdx6500X25CfgAdmnPacketSequencing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ext", 2),
          ("norm", 1))
    )


_Cdx6500X25CfgAdmnPacketSequencing_Type.__name__ = "Integer32"
_Cdx6500X25CfgAdmnPacketSequencing_Object = MibTableColumn
cdx6500X25CfgAdmnPacketSequencing = _Cdx6500X25CfgAdmnPacketSequencing_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 17),
    _Cdx6500X25CfgAdmnPacketSequencing_Type()
)
cdx6500X25CfgAdmnPacketSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgAdmnPacketSequencing.setStatus("mandatory")


class _Cdx6500X25CfgWPacketWindow_Type(Integer32):
    """Custom type cdx6500X25CfgWPacketWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Cdx6500X25CfgWPacketWindow_Type.__name__ = "Integer32"
_Cdx6500X25CfgWPacketWindow_Object = MibTableColumn
cdx6500X25CfgWPacketWindow = _Cdx6500X25CfgWPacketWindow_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 18),
    _Cdx6500X25CfgWPacketWindow_Type()
)
cdx6500X25CfgWPacketWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgWPacketWindow.setStatus("mandatory")


class _Cdx6500X25CfgPPacketSize_Type(Integer32):
    """Custom type cdx6500X25CfgPPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("bytes1024", 10),
          ("bytes128", 7),
          ("bytes256", 8),
          ("bytes512", 9))
    )


_Cdx6500X25CfgPPacketSize_Type.__name__ = "Integer32"
_Cdx6500X25CfgPPacketSize_Object = MibTableColumn
cdx6500X25CfgPPacketSize = _Cdx6500X25CfgPPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 19),
    _Cdx6500X25CfgPPacketSize_Type()
)
cdx6500X25CfgPPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgPPacketSize.setStatus("mandatory")


class _Cdx6500X25CfgMaxNegotPacketSize_Type(Integer32):
    """Custom type cdx6500X25CfgMaxNegotPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("bytes1024", 10),
          ("bytes128", 7),
          ("bytes256", 8),
          ("bytes512", 9))
    )


_Cdx6500X25CfgMaxNegotPacketSize_Type.__name__ = "Integer32"
_Cdx6500X25CfgMaxNegotPacketSize_Object = MibTableColumn
cdx6500X25CfgMaxNegotPacketSize = _Cdx6500X25CfgMaxNegotPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 20),
    _Cdx6500X25CfgMaxNegotPacketSize_Type()
)
cdx6500X25CfgMaxNegotPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgMaxNegotPacketSize.setStatus("mandatory")


class _Cdx6500X25CfgDataQueueUpper_Type(Integer32):
    """Custom type cdx6500X25CfgDataQueueUpper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Cdx6500X25CfgDataQueueUpper_Type.__name__ = "Integer32"
_Cdx6500X25CfgDataQueueUpper_Object = MibTableColumn
cdx6500X25CfgDataQueueUpper = _Cdx6500X25CfgDataQueueUpper_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 21),
    _Cdx6500X25CfgDataQueueUpper_Type()
)
cdx6500X25CfgDataQueueUpper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgDataQueueUpper.setStatus("mandatory")


class _Cdx6500X25CfgDataQueueLower_Type(Integer32):
    """Custom type cdx6500X25CfgDataQueueLower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Cdx6500X25CfgDataQueueLower_Type.__name__ = "Integer32"
_Cdx6500X25CfgDataQueueLower_Object = MibTableColumn
cdx6500X25CfgDataQueueLower = _Cdx6500X25CfgDataQueueLower_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 22),
    _Cdx6500X25CfgDataQueueLower_Type()
)
cdx6500X25CfgDataQueueLower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgDataQueueLower.setStatus("mandatory")


class _Cdx6500X25CfgAdmnRestartTimer_Type(Integer32):
    """Custom type cdx6500X25CfgAdmnRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500X25CfgAdmnRestartTimer_Type.__name__ = "Integer32"
_Cdx6500X25CfgAdmnRestartTimer_Object = MibTableColumn
cdx6500X25CfgAdmnRestartTimer = _Cdx6500X25CfgAdmnRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 23),
    _Cdx6500X25CfgAdmnRestartTimer_Type()
)
cdx6500X25CfgAdmnRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgAdmnRestartTimer.setStatus("mandatory")


class _Cdx6500X25CfgAdmnResetTimer_Type(Integer32):
    """Custom type cdx6500X25CfgAdmnResetTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 180),
    )


_Cdx6500X25CfgAdmnResetTimer_Type.__name__ = "Integer32"
_Cdx6500X25CfgAdmnResetTimer_Object = MibTableColumn
cdx6500X25CfgAdmnResetTimer = _Cdx6500X25CfgAdmnResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 24),
    _Cdx6500X25CfgAdmnResetTimer_Type()
)
cdx6500X25CfgAdmnResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgAdmnResetTimer.setStatus("mandatory")


class _Cdx6500X25CfgAdmnCallTimer_Type(Integer32):
    """Custom type cdx6500X25CfgAdmnCallTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500X25CfgAdmnCallTimer_Type.__name__ = "Integer32"
_Cdx6500X25CfgAdmnCallTimer_Object = MibTableColumn
cdx6500X25CfgAdmnCallTimer = _Cdx6500X25CfgAdmnCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 25),
    _Cdx6500X25CfgAdmnCallTimer_Type()
)
cdx6500X25CfgAdmnCallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgAdmnCallTimer.setStatus("mandatory")


class _Cdx6500X25CfgAdmnClearTimer_Type(Integer32):
    """Custom type cdx6500X25CfgAdmnClearTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500X25CfgAdmnClearTimer_Type.__name__ = "Integer32"
_Cdx6500X25CfgAdmnClearTimer_Object = MibTableColumn
cdx6500X25CfgAdmnClearTimer = _Cdx6500X25CfgAdmnClearTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 26),
    _Cdx6500X25CfgAdmnClearTimer_Type()
)
cdx6500X25CfgAdmnClearTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgAdmnClearTimer.setStatus("mandatory")


class _Cdx6500X25CfgOutDelFacilities_Type(DisplayString):
    """Custom type cdx6500X25CfgOutDelFacilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_Cdx6500X25CfgOutDelFacilities_Type.__name__ = "DisplayString"
_Cdx6500X25CfgOutDelFacilities_Object = MibTableColumn
cdx6500X25CfgOutDelFacilities = _Cdx6500X25CfgOutDelFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 27),
    _Cdx6500X25CfgOutDelFacilities_Type()
)
cdx6500X25CfgOutDelFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgOutDelFacilities.setStatus("mandatory")


class _Cdx6500X25CfgOutAddFacilities_Type(DisplayString):
    """Custom type cdx6500X25CfgOutAddFacilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 18),
    )


_Cdx6500X25CfgOutAddFacilities_Type.__name__ = "DisplayString"
_Cdx6500X25CfgOutAddFacilities_Object = MibTableColumn
cdx6500X25CfgOutAddFacilities = _Cdx6500X25CfgOutAddFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 28),
    _Cdx6500X25CfgOutAddFacilities_Type()
)
cdx6500X25CfgOutAddFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgOutAddFacilities.setStatus("mandatory")


class _Cdx6500X25CfgOutBarFacilities_Type(DisplayString):
    """Custom type cdx6500X25CfgOutBarFacilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 24),
    )


_Cdx6500X25CfgOutBarFacilities_Type.__name__ = "DisplayString"
_Cdx6500X25CfgOutBarFacilities_Object = MibTableColumn
cdx6500X25CfgOutBarFacilities = _Cdx6500X25CfgOutBarFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 29),
    _Cdx6500X25CfgOutBarFacilities_Type()
)
cdx6500X25CfgOutBarFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgOutBarFacilities.setStatus("mandatory")


class _Cdx6500X25CfgInBarFacilities_Type(DisplayString):
    """Custom type cdx6500X25CfgInBarFacilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 19),
    )


_Cdx6500X25CfgInBarFacilities_Type.__name__ = "DisplayString"
_Cdx6500X25CfgInBarFacilities_Object = MibTableColumn
cdx6500X25CfgInBarFacilities = _Cdx6500X25CfgInBarFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 30),
    _Cdx6500X25CfgInBarFacilities_Type()
)
cdx6500X25CfgInBarFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgInBarFacilities.setStatus("mandatory")


class _Cdx6500X25CfgOptions_Type(DisplayString):
    """Custom type cdx6500X25CfgOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 107),
    )


_Cdx6500X25CfgOptions_Type.__name__ = "DisplayString"
_Cdx6500X25CfgOptions_Object = MibTableColumn
cdx6500X25CfgOptions = _Cdx6500X25CfgOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 31),
    _Cdx6500X25CfgOptions_Type()
)
cdx6500X25CfgOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgOptions.setStatus("mandatory")


class _Cdx6500X25CfgNumRoutDigits_Type(Integer32):
    """Custom type cdx6500X25CfgNumRoutDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Cdx6500X25CfgNumRoutDigits_Type.__name__ = "Integer32"
_Cdx6500X25CfgNumRoutDigits_Object = MibTableColumn
cdx6500X25CfgNumRoutDigits = _Cdx6500X25CfgNumRoutDigits_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 32),
    _Cdx6500X25CfgNumRoutDigits_Type()
)
cdx6500X25CfgNumRoutDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgNumRoutDigits.setStatus("mandatory")


class _Cdx6500X25CfgPortDigitsToStrip_Type(Integer32):
    """Custom type cdx6500X25CfgPortDigitsToStrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_Cdx6500X25CfgPortDigitsToStrip_Type.__name__ = "Integer32"
_Cdx6500X25CfgPortDigitsToStrip_Object = MibTableColumn
cdx6500X25CfgPortDigitsToStrip = _Cdx6500X25CfgPortDigitsToStrip_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 33),
    _Cdx6500X25CfgPortDigitsToStrip_Type()
)
cdx6500X25CfgPortDigitsToStrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgPortDigitsToStrip.setStatus("mandatory")


class _Cdx6500X25CfgInDigitsToStrip_Type(Integer32):
    """Custom type cdx6500X25CfgInDigitsToStrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500X25CfgInDigitsToStrip_Type.__name__ = "Integer32"
_Cdx6500X25CfgInDigitsToStrip_Object = MibTableColumn
cdx6500X25CfgInDigitsToStrip = _Cdx6500X25CfgInDigitsToStrip_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 34),
    _Cdx6500X25CfgInDigitsToStrip_Type()
)
cdx6500X25CfgInDigitsToStrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgInDigitsToStrip.setStatus("mandatory")


class _Cdx6500X25CfgRestrictConn_Type(DisplayString):
    """Custom type cdx6500X25CfgRestrictConn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500X25CfgRestrictConn_Type.__name__ = "DisplayString"
_Cdx6500X25CfgRestrictConn_Object = MibTableColumn
cdx6500X25CfgRestrictConn = _Cdx6500X25CfgRestrictConn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 35),
    _Cdx6500X25CfgRestrictConn_Type()
)
cdx6500X25CfgRestrictConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgRestrictConn.setStatus("mandatory")


class _Cdx6500X25CfgPortAddress_Type(DisplayString):
    """Custom type cdx6500X25CfgPortAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500X25CfgPortAddress_Type.__name__ = "DisplayString"
_Cdx6500X25CfgPortAddress_Object = MibTableColumn
cdx6500X25CfgPortAddress = _Cdx6500X25CfgPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 36),
    _Cdx6500X25CfgPortAddress_Type()
)
cdx6500X25CfgPortAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgPortAddress.setStatus("mandatory")


class _Cdx6500X25CfgCUGMember_Type(DisplayString):
    """Custom type cdx6500X25CfgCUGMember based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_Cdx6500X25CfgCUGMember_Type.__name__ = "DisplayString"
_Cdx6500X25CfgCUGMember_Object = MibTableColumn
cdx6500X25CfgCUGMember = _Cdx6500X25CfgCUGMember_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 37),
    _Cdx6500X25CfgCUGMember_Type()
)
cdx6500X25CfgCUGMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgCUGMember.setStatus("mandatory")


class _Cdx6500X25CfgBillRec_Type(Integer32):
    """Custom type cdx6500X25CfgBillRec based on Integer32"""
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


_Cdx6500X25CfgBillRec_Type.__name__ = "Integer32"
_Cdx6500X25CfgBillRec_Object = MibTableColumn
cdx6500X25CfgBillRec = _Cdx6500X25CfgBillRec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 38),
    _Cdx6500X25CfgBillRec_Type()
)
cdx6500X25CfgBillRec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgBillRec.setStatus("mandatory")


class _Cdx6500X25CfgSubAddrSize_Type(Integer32):
    """Custom type cdx6500X25CfgSubAddrSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cdx6500X25CfgSubAddrSize_Type.__name__ = "Integer32"
_Cdx6500X25CfgSubAddrSize_Object = MibTableColumn
cdx6500X25CfgSubAddrSize = _Cdx6500X25CfgSubAddrSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 39),
    _Cdx6500X25CfgSubAddrSize_Type()
)
cdx6500X25CfgSubAddrSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgSubAddrSize.setStatus("mandatory")


class _Cdx6500X25CfgIdleDiscTimer_Type(Integer32):
    """Custom type cdx6500X25CfgIdleDiscTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_Cdx6500X25CfgIdleDiscTimer_Type.__name__ = "Integer32"
_Cdx6500X25CfgIdleDiscTimer_Object = MibTableColumn
cdx6500X25CfgIdleDiscTimer = _Cdx6500X25CfgIdleDiscTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 40),
    _Cdx6500X25CfgIdleDiscTimer_Type()
)
cdx6500X25CfgIdleDiscTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgIdleDiscTimer.setStatus("mandatory")


class _Cdx6500X25CfgCallSecurity_Type(Integer32):
    """Custom type cdx6500X25CfgCallSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Cdx6500X25CfgCallSecurity_Type.__name__ = "Integer32"
_Cdx6500X25CfgCallSecurity_Object = MibTableColumn
cdx6500X25CfgCallSecurity = _Cdx6500X25CfgCallSecurity_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 41),
    _Cdx6500X25CfgCallSecurity_Type()
)
cdx6500X25CfgCallSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgCallSecurity.setStatus("mandatory")


class _Cdx6500X25CfgProtectLevel_Type(Integer32):
    """Custom type cdx6500X25CfgProtectLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpOnly", 2),
          ("fullDcp", 3),
          ("none", 1))
    )


_Cdx6500X25CfgProtectLevel_Type.__name__ = "Integer32"
_Cdx6500X25CfgProtectLevel_Object = MibTableColumn
cdx6500X25CfgProtectLevel = _Cdx6500X25CfgProtectLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 42),
    _Cdx6500X25CfgProtectLevel_Type()
)
cdx6500X25CfgProtectLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgProtectLevel.setStatus("mandatory")


class _Cdx6500X25CfgReconnTimeout_Type(Integer32):
    """Custom type cdx6500X25CfgReconnTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Cdx6500X25CfgReconnTimeout_Type.__name__ = "Integer32"
_Cdx6500X25CfgReconnTimeout_Object = MibTableColumn
cdx6500X25CfgReconnTimeout = _Cdx6500X25CfgReconnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 43),
    _Cdx6500X25CfgReconnTimeout_Type()
)
cdx6500X25CfgReconnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgReconnTimeout.setStatus("mandatory")


class _Cdx6500X25CfgReconnTriesLimit_Type(Integer32):
    """Custom type cdx6500X25CfgReconnTriesLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500X25CfgReconnTriesLimit_Type.__name__ = "Integer32"
_Cdx6500X25CfgReconnTriesLimit_Object = MibTableColumn
cdx6500X25CfgReconnTriesLimit = _Cdx6500X25CfgReconnTriesLimit_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 44),
    _Cdx6500X25CfgReconnTriesLimit_Type()
)
cdx6500X25CfgReconnTriesLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgReconnTriesLimit.setStatus("mandatory")


class _Cdx6500X25CfgFacilSubscripCont_Type(DisplayString):
    """Custom type cdx6500X25CfgFacilSubscripCont based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 34),
    )


_Cdx6500X25CfgFacilSubscripCont_Type.__name__ = "DisplayString"
_Cdx6500X25CfgFacilSubscripCont_Object = MibTableColumn
cdx6500X25CfgFacilSubscripCont = _Cdx6500X25CfgFacilSubscripCont_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 45),
    _Cdx6500X25CfgFacilSubscripCont_Type()
)
cdx6500X25CfgFacilSubscripCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25CfgFacilSubscripCont.setStatus("mandatory")


class _Cdx6500X25CfgAlarmPriority_Type(Integer32):
    """Custom type cdx6500X25CfgAlarmPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("network", 1))
    )


_Cdx6500X25CfgAlarmPriority_Type.__name__ = "Integer32"
_Cdx6500X25CfgAlarmPriority_Object = MibTableColumn
cdx6500X25CfgAlarmPriority = _Cdx6500X25CfgAlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 46),
    _Cdx6500X25CfgAlarmPriority_Type()
)
cdx6500X25CfgAlarmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgAlarmPriority.setStatus("mandatory")


class _Cdx6500X25CfgAddrTrans_Type(DisplayString):
    """Custom type cdx6500X25CfgAddrTrans based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 107),
    )


_Cdx6500X25CfgAddrTrans_Type.__name__ = "DisplayString"
_Cdx6500X25CfgAddrTrans_Object = MibTableColumn
cdx6500X25CfgAddrTrans = _Cdx6500X25CfgAddrTrans_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 47),
    _Cdx6500X25CfgAddrTrans_Type()
)
cdx6500X25CfgAddrTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgAddrTrans.setStatus("mandatory")


class _Cdx6500X25CfgNumberInSVCs_Type(Integer32):
    """Custom type cdx6500X25CfgNumberInSVCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Cdx6500X25CfgNumberInSVCs_Type.__name__ = "Integer32"
_Cdx6500X25CfgNumberInSVCs_Object = MibTableColumn
cdx6500X25CfgNumberInSVCs = _Cdx6500X25CfgNumberInSVCs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 48),
    _Cdx6500X25CfgNumberInSVCs_Type()
)
cdx6500X25CfgNumberInSVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgNumberInSVCs.setStatus("mandatory")


class _Cdx6500X25CfgStartInSVCChanNum_Type(Integer32):
    """Custom type cdx6500X25CfgStartInSVCChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Cdx6500X25CfgStartInSVCChanNum_Type.__name__ = "Integer32"
_Cdx6500X25CfgStartInSVCChanNum_Object = MibTableColumn
cdx6500X25CfgStartInSVCChanNum = _Cdx6500X25CfgStartInSVCChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 49),
    _Cdx6500X25CfgStartInSVCChanNum_Type()
)
cdx6500X25CfgStartInSVCChanNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgStartInSVCChanNum.setStatus("mandatory")


class _Cdx6500X25CfgNumberOutSVCs_Type(Integer32):
    """Custom type cdx6500X25CfgNumberOutSVCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Cdx6500X25CfgNumberOutSVCs_Type.__name__ = "Integer32"
_Cdx6500X25CfgNumberOutSVCs_Object = MibTableColumn
cdx6500X25CfgNumberOutSVCs = _Cdx6500X25CfgNumberOutSVCs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 50),
    _Cdx6500X25CfgNumberOutSVCs_Type()
)
cdx6500X25CfgNumberOutSVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgNumberOutSVCs.setStatus("mandatory")


class _Cdx6500X25CfgStartOutSVCChanNum_Type(Integer32):
    """Custom type cdx6500X25CfgStartOutSVCChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Cdx6500X25CfgStartOutSVCChanNum_Type.__name__ = "Integer32"
_Cdx6500X25CfgStartOutSVCChanNum_Object = MibTableColumn
cdx6500X25CfgStartOutSVCChanNum = _Cdx6500X25CfgStartOutSVCChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 51),
    _Cdx6500X25CfgStartOutSVCChanNum_Type()
)
cdx6500X25CfgStartOutSVCChanNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgStartOutSVCChanNum.setStatus("mandatory")


class _Cdx6500X25CfgChargeInfoReq_Type(Integer32):
    """Custom type cdx6500X25CfgChargeInfoReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Cdx6500X25CfgChargeInfoReq_Type.__name__ = "Integer32"
_Cdx6500X25CfgChargeInfoReq_Object = MibTableColumn
cdx6500X25CfgChargeInfoReq = _Cdx6500X25CfgChargeInfoReq_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 52),
    _Cdx6500X25CfgChargeInfoReq_Type()
)
cdx6500X25CfgChargeInfoReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgChargeInfoReq.setStatus("mandatory")


class _Cdx6500X25CfgVerfnTimer_Type(Integer32):
    """Custom type cdx6500X25CfgVerfnTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 180),
    )


_Cdx6500X25CfgVerfnTimer_Type.__name__ = "Integer32"
_Cdx6500X25CfgVerfnTimer_Object = MibTableColumn
cdx6500X25CfgVerfnTimer = _Cdx6500X25CfgVerfnTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 53),
    _Cdx6500X25CfgVerfnTimer_Type()
)
cdx6500X25CfgVerfnTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgVerfnTimer.setStatus("mandatory")


class _Cdx6500X25CfgValdFailures_Type(Integer32):
    """Custom type cdx6500X25CfgValdFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500X25CfgValdFailures_Type.__name__ = "Integer32"
_Cdx6500X25CfgValdFailures_Object = MibTableColumn
cdx6500X25CfgValdFailures = _Cdx6500X25CfgValdFailures_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 54),
    _Cdx6500X25CfgValdFailures_Type()
)
cdx6500X25CfgValdFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgValdFailures.setStatus("mandatory")


class _Cdx6500X25CfgActionType_Type(Integer32):
    """Custom type cdx6500X25CfgActionType based on Integer32"""
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
        *(("degr", 3),
          ("disc", 2),
          ("lock", 4),
          ("none", 1))
    )


_Cdx6500X25CfgActionType_Type.__name__ = "Integer32"
_Cdx6500X25CfgActionType_Object = MibTableColumn
cdx6500X25CfgActionType = _Cdx6500X25CfgActionType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 55),
    _Cdx6500X25CfgActionType_Type()
)
cdx6500X25CfgActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgActionType.setStatus("mandatory")


class _Cdx6500X25CfgLineIdleMode_Type(Integer32):
    """Custom type cdx6500X25CfgLineIdleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flag", 1),
          ("mark", 2))
    )


_Cdx6500X25CfgLineIdleMode_Type.__name__ = "Integer32"
_Cdx6500X25CfgLineIdleMode_Object = MibTableColumn
cdx6500X25CfgLineIdleMode = _Cdx6500X25CfgLineIdleMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 56),
    _Cdx6500X25CfgLineIdleMode_Type()
)
cdx6500X25CfgLineIdleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgLineIdleMode.setStatus("mandatory")


class _Cdx6500X25CfgConfOption_Type(DisplayString):
    """Custom type cdx6500X25CfgConfOption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 34),
    )


_Cdx6500X25CfgConfOption_Type.__name__ = "DisplayString"
_Cdx6500X25CfgConfOption_Object = MibTableColumn
cdx6500X25CfgConfOption = _Cdx6500X25CfgConfOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 57),
    _Cdx6500X25CfgConfOption_Type()
)
cdx6500X25CfgConfOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgConfOption.setStatus("mandatory")


class _Cdx6500X25CfgInvertTxClk_Type(Integer32):
    """Custom type cdx6500X25CfgInvertTxClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Cdx6500X25CfgInvertTxClk_Type.__name__ = "Integer32"
_Cdx6500X25CfgInvertTxClk_Object = MibTableColumn
cdx6500X25CfgInvertTxClk = _Cdx6500X25CfgInvertTxClk_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 58),
    _Cdx6500X25CfgInvertTxClk_Type()
)
cdx6500X25CfgInvertTxClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgInvertTxClk.setStatus("mandatory")


class _Cdx6500X25CfgDimType_Type(Integer32):
    """Custom type cdx6500X25CfgDimType based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("dim-not-supported", 16),
          ("dim-type-dsu", 9),
          ("dim-type-eia-232-d", 3),
          ("dim-type-eia-530", 8),
          ("dim-type-future-use", 15),
          ("dim-type-i430", 12),
          ("dim-type-isdn", 10),
          ("dim-type-none", 1),
          ("dim-type-not-installed", 2),
          ("dim-type-t1e1", 14),
          ("dim-type-v11", 7),
          ("dim-type-v35", 5),
          ("dim-type-v36", 6),
          ("dim-type-vrdc", 11),
          ("dim-type-vrdc-2em", 17),
          ("dim-type-vrdc-2fxs", 13),
          ("dim-type-vrdc-bri", 18),
          ("dim-type-x21", 4))
    )


_Cdx6500X25CfgDimType_Type.__name__ = "Integer32"
_Cdx6500X25CfgDimType_Object = MibTableColumn
cdx6500X25CfgDimType = _Cdx6500X25CfgDimType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 59),
    _Cdx6500X25CfgDimType_Type()
)
cdx6500X25CfgDimType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgDimType.setStatus("mandatory")


class _Cdx6500X25CfgMoreOptions_Type(DisplayString):
    """Custom type cdx6500X25CfgMoreOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 9),
    )


_Cdx6500X25CfgMoreOptions_Type.__name__ = "DisplayString"
_Cdx6500X25CfgMoreOptions_Object = MibTableColumn
cdx6500X25CfgMoreOptions = _Cdx6500X25CfgMoreOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 60),
    _Cdx6500X25CfgMoreOptions_Type()
)
cdx6500X25CfgMoreOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgMoreOptions.setStatus("mandatory")


class _Cdx6500X25CfgPsfFlag_Type(Integer32):
    """Custom type cdx6500X25CfgPsfFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psf-disabled", 1),
          ("psf-enabled", 2))
    )


_Cdx6500X25CfgPsfFlag_Type.__name__ = "Integer32"
_Cdx6500X25CfgPsfFlag_Object = MibTableColumn
cdx6500X25CfgPsfFlag = _Cdx6500X25CfgPsfFlag_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 61),
    _Cdx6500X25CfgPsfFlag_Type()
)
cdx6500X25CfgPsfFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgPsfFlag.setStatus("mandatory")


class _Cdx6500X25CfgElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500X25CfgElectricalInterfaceType based on Integer32"""
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
        *(("none", 5),
          ("v24", 1),
          ("v35", 2),
          ("v36", 3),
          ("x21", 4))
    )


_Cdx6500X25CfgElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500X25CfgElectricalInterfaceType_Object = MibTableColumn
cdx6500X25CfgElectricalInterfaceType = _Cdx6500X25CfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 62),
    _Cdx6500X25CfgElectricalInterfaceType_Type()
)
cdx6500X25CfgElectricalInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500X25CfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500X25CfgV24ElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ri", 1),
          ("tm", 2))
    )


_Cdx6500X25CfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500X25CfgV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500X25CfgV24ElectricalInterfaceOption = _Cdx6500X25CfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 63),
    _Cdx6500X25CfgV24ElectricalInterfaceOption_Type()
)
cdx6500X25CfgV24ElectricalInterfaceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500X25CfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500X25CfgHighSpeedElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("xover", 2))
    )


_Cdx6500X25CfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500X25CfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500X25CfgHighSpeedElectricalInterfaceOption = _Cdx6500X25CfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 2, 1, 64),
    _Cdx6500X25CfgHighSpeedElectricalInterfaceOption_Type()
)
cdx6500X25CfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500X25CfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500CGTInboundCallTranTable_Object = MibTable
cdx6500CGTInboundCallTranTable = _Cdx6500CGTInboundCallTranTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cdx6500CGTInboundCallTranTable.setStatus("mandatory")
_Cdx6500CGTInboundCallTranEntry_Object = MibTableRow
cdx6500CGTInboundCallTranEntry = _Cdx6500CGTInboundCallTranEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 2, 1)
)
cdx6500CGTInboundCallTranEntry.setIndexNames(
    (0, "X25-OPT-MIB", "cdx6500InCallTranEntryNum"),
)
if mibBuilder.loadTexts:
    cdx6500CGTInboundCallTranEntry.setStatus("mandatory")


class _Cdx6500InCallTranEntryNum_Type(Integer32):
    """Custom type cdx6500InCallTranEntryNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Cdx6500InCallTranEntryNum_Type.__name__ = "Integer32"
_Cdx6500InCallTranEntryNum_Object = MibTableColumn
cdx6500InCallTranEntryNum = _Cdx6500InCallTranEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 2, 1, 1),
    _Cdx6500InCallTranEntryNum_Type()
)
cdx6500InCallTranEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500InCallTranEntryNum.setStatus("mandatory")


class _Cdx6500InCallTranInSubAddr_Type(DisplayString):
    """Custom type cdx6500InCallTranInSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500InCallTranInSubAddr_Type.__name__ = "DisplayString"
_Cdx6500InCallTranInSubAddr_Object = MibTableColumn
cdx6500InCallTranInSubAddr = _Cdx6500InCallTranInSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 2, 1, 2),
    _Cdx6500InCallTranInSubAddr_Type()
)
cdx6500InCallTranInSubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500InCallTranInSubAddr.setStatus("mandatory")


class _Cdx6500InCallTranPrivNetAddr_Type(DisplayString):
    """Custom type cdx6500InCallTranPrivNetAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500InCallTranPrivNetAddr_Type.__name__ = "DisplayString"
_Cdx6500InCallTranPrivNetAddr_Object = MibTableColumn
cdx6500InCallTranPrivNetAddr = _Cdx6500InCallTranPrivNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 2, 1, 3),
    _Cdx6500InCallTranPrivNetAddr_Type()
)
cdx6500InCallTranPrivNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500InCallTranPrivNetAddr.setStatus("mandatory")
_Cdx6500CGTOutboundCallTranTable_Object = MibTable
cdx6500CGTOutboundCallTranTable = _Cdx6500CGTOutboundCallTranTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cdx6500CGTOutboundCallTranTable.setStatus("mandatory")
_Cdx6500CGTOutboundCallTranEntry_Object = MibTableRow
cdx6500CGTOutboundCallTranEntry = _Cdx6500CGTOutboundCallTranEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 3, 1)
)
cdx6500CGTOutboundCallTranEntry.setIndexNames(
    (0, "X25-OPT-MIB", "cdx6500OutCallTranEntryNum"),
)
if mibBuilder.loadTexts:
    cdx6500CGTOutboundCallTranEntry.setStatus("mandatory")


class _Cdx6500OutCallTranEntryNum_Type(Integer32):
    """Custom type cdx6500OutCallTranEntryNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1600),
    )


_Cdx6500OutCallTranEntryNum_Type.__name__ = "Integer32"
_Cdx6500OutCallTranEntryNum_Object = MibTableColumn
cdx6500OutCallTranEntryNum = _Cdx6500OutCallTranEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 3, 1, 1),
    _Cdx6500OutCallTranEntryNum_Type()
)
cdx6500OutCallTranEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500OutCallTranEntryNum.setStatus("mandatory")


class _Cdx6500OutCallTranPrivNetAddr_Type(DisplayString):
    """Custom type cdx6500OutCallTranPrivNetAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500OutCallTranPrivNetAddr_Type.__name__ = "DisplayString"
_Cdx6500OutCallTranPrivNetAddr_Object = MibTableColumn
cdx6500OutCallTranPrivNetAddr = _Cdx6500OutCallTranPrivNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 3, 1, 2),
    _Cdx6500OutCallTranPrivNetAddr_Type()
)
cdx6500OutCallTranPrivNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500OutCallTranPrivNetAddr.setStatus("mandatory")


class _Cdx6500OutCallTranOutNetAddr_Type(DisplayString):
    """Custom type cdx6500OutCallTranOutNetAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500OutCallTranOutNetAddr_Type.__name__ = "DisplayString"
_Cdx6500OutCallTranOutNetAddr_Object = MibTableColumn
cdx6500OutCallTranOutNetAddr = _Cdx6500OutCallTranOutNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 3, 1, 3),
    _Cdx6500OutCallTranOutNetAddr_Type()
)
cdx6500OutCallTranOutNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500OutCallTranOutNetAddr.setStatus("mandatory")


class _Cdx6500OutCallTranOptions_Type(Integer32):
    """Custom type cdx6500OutCallTranOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalNone", 50),
          ("none", 0),
          ("olda", 1))
    )


_Cdx6500OutCallTranOptions_Type.__name__ = "Integer32"
_Cdx6500OutCallTranOptions_Object = MibTableColumn
cdx6500OutCallTranOptions = _Cdx6500OutCallTranOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 3, 1, 4),
    _Cdx6500OutCallTranOptions_Type()
)
cdx6500OutCallTranOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500OutCallTranOptions.setStatus("mandatory")
_Cdx6500CGTCallingAddrTranTable_Object = MibTable
cdx6500CGTCallingAddrTranTable = _Cdx6500CGTCallingAddrTranTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 13)
)
if mibBuilder.loadTexts:
    cdx6500CGTCallingAddrTranTable.setStatus("mandatory")
_Cdx6500CGTCallingAddrTranEntry_Object = MibTableRow
cdx6500CGTCallingAddrTranEntry = _Cdx6500CGTCallingAddrTranEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 13, 1)
)
cdx6500CGTCallingAddrTranEntry.setIndexNames(
    (0, "X25-OPT-MIB", "cdx6500CalladdrtranEntryNum"),
)
if mibBuilder.loadTexts:
    cdx6500CGTCallingAddrTranEntry.setStatus("mandatory")


class _Cdx6500CalladdrtranEntryNum_Type(Integer32):
    """Custom type cdx6500CalladdrtranEntryNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Cdx6500CalladdrtranEntryNum_Type.__name__ = "Integer32"
_Cdx6500CalladdrtranEntryNum_Object = MibTableColumn
cdx6500CalladdrtranEntryNum = _Cdx6500CalladdrtranEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 13, 1, 1),
    _Cdx6500CalladdrtranEntryNum_Type()
)
cdx6500CalladdrtranEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CalladdrtranEntryNum.setStatus("mandatory")


class _Cdx6500CalladdrtranInCallAddr_Type(DisplayString):
    """Custom type cdx6500CalladdrtranInCallAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500CalladdrtranInCallAddr_Type.__name__ = "DisplayString"
_Cdx6500CalladdrtranInCallAddr_Object = MibTableColumn
cdx6500CalladdrtranInCallAddr = _Cdx6500CalladdrtranInCallAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 13, 1, 2),
    _Cdx6500CalladdrtranInCallAddr_Type()
)
cdx6500CalladdrtranInCallAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500CalladdrtranInCallAddr.setStatus("mandatory")


class _Cdx6500CalladdrtranPrivNetAddr_Type(DisplayString):
    """Custom type cdx6500CalladdrtranPrivNetAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500CalladdrtranPrivNetAddr_Type.__name__ = "DisplayString"
_Cdx6500CalladdrtranPrivNetAddr_Object = MibTableColumn
cdx6500CalladdrtranPrivNetAddr = _Cdx6500CalladdrtranPrivNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 13, 1, 3),
    _Cdx6500CalladdrtranPrivNetAddr_Type()
)
cdx6500CalladdrtranPrivNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500CalladdrtranPrivNetAddr.setStatus("mandatory")
_Cdx6500CGTCudBaseAddrTranTable_Object = MibTable
cdx6500CGTCudBaseAddrTranTable = _Cdx6500CGTCudBaseAddrTranTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 23)
)
if mibBuilder.loadTexts:
    cdx6500CGTCudBaseAddrTranTable.setStatus("mandatory")
_Cdx6500CGTCudBaseAddrTranEntry_Object = MibTableRow
cdx6500CGTCudBaseAddrTranEntry = _Cdx6500CGTCudBaseAddrTranEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 23, 1)
)
cdx6500CGTCudBaseAddrTranEntry.setIndexNames(
    (0, "X25-OPT-MIB", "cdx6500CudBaseaddrtranEntryNum"),
)
if mibBuilder.loadTexts:
    cdx6500CGTCudBaseAddrTranEntry.setStatus("mandatory")


class _Cdx6500CudBaseaddrtranEntryNum_Type(Integer32):
    """Custom type cdx6500CudBaseaddrtranEntryNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Cdx6500CudBaseaddrtranEntryNum_Type.__name__ = "Integer32"
_Cdx6500CudBaseaddrtranEntryNum_Object = MibTableColumn
cdx6500CudBaseaddrtranEntryNum = _Cdx6500CudBaseaddrtranEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 23, 1, 1),
    _Cdx6500CudBaseaddrtranEntryNum_Type()
)
cdx6500CudBaseaddrtranEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500CudBaseaddrtranEntryNum.setStatus("mandatory")


class _Cdx6500CudBaseStr_Type(DisplayString):
    """Custom type cdx6500CudBaseStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cdx6500CudBaseStr_Type.__name__ = "DisplayString"
_Cdx6500CudBaseStr_Object = MibTableColumn
cdx6500CudBaseStr = _Cdx6500CudBaseStr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 23, 1, 2),
    _Cdx6500CudBaseStr_Type()
)
cdx6500CudBaseStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500CudBaseStr.setStatus("mandatory")


class _Cdx6500CudBaseAddr_Type(DisplayString):
    """Custom type cdx6500CudBaseAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500CudBaseAddr_Type.__name__ = "DisplayString"
_Cdx6500CudBaseAddr_Object = MibTableColumn
cdx6500CudBaseAddr = _Cdx6500CudBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 23, 1, 3),
    _Cdx6500CudBaseAddr_Type()
)
cdx6500CudBaseAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500CudBaseAddr.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PPSTX25PortTable_Object = MibTable
cdx6500PPSTX25PortTable = _Cdx6500PPSTX25PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdx6500PPSTX25PortTable.setStatus("mandatory")
_Cdx6500PPSTX25PortEntry_Object = MibTableRow
cdx6500PPSTX25PortEntry = _Cdx6500PPSTX25PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1)
)
cdx6500PPSTX25PortEntry.setIndexNames(
    (0, "X25-OPT-MIB", "cdx6500X25StatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTX25PortEntry.setStatus("mandatory")


class _Cdx6500X25StatPortNumber_Type(Integer32):
    """Custom type cdx6500X25StatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500X25StatPortNumber_Type.__name__ = "Integer32"
_Cdx6500X25StatPortNumber_Object = MibTableColumn
cdx6500X25StatPortNumber = _Cdx6500X25StatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 1),
    _Cdx6500X25StatPortNumber_Type()
)
cdx6500X25StatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatPortNumber.setStatus("mandatory")


class _Cdx6500X25StatPortStatus_Type(DisplayString):
    """Custom type cdx6500X25StatPortStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_Cdx6500X25StatPortStatus_Type.__name__ = "DisplayString"
_Cdx6500X25StatPortStatus_Object = MibTableColumn
cdx6500X25StatPortStatus = _Cdx6500X25StatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 2),
    _Cdx6500X25StatPortStatus_Type()
)
cdx6500X25StatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatPortStatus.setStatus("mandatory")


class _Cdx6500X25StatPortState_Type(Integer32):
    """Custom type cdx6500X25StatPortState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("discPhase", 1),
          ("frameReject", 5),
          ("linkDisk", 2),
          ("linkSetup", 3),
          ("normal", 6),
          ("rbSr", 10),
          ("remoteBusy", 7),
          ("reset", 8),
          ("sabmColl", 4),
          ("sendReject", 9))
    )


_Cdx6500X25StatPortState_Type.__name__ = "Integer32"
_Cdx6500X25StatPortState_Object = MibTableColumn
cdx6500X25StatPortState = _Cdx6500X25StatPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 3),
    _Cdx6500X25StatPortState_Type()
)
cdx6500X25StatPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatPortState.setStatus("mandatory")
_Cdx6500X25StatActualPortSpeed_Type = Integer32
_Cdx6500X25StatActualPortSpeed_Object = MibTableColumn
cdx6500X25StatActualPortSpeed = _Cdx6500X25StatActualPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 4),
    _Cdx6500X25StatActualPortSpeed_Type()
)
cdx6500X25StatActualPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatActualPortSpeed.setStatus("mandatory")


class _Cdx6500X25StatPortUtilIn_Type(Integer32):
    """Custom type cdx6500X25StatPortUtilIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500X25StatPortUtilIn_Type.__name__ = "Integer32"
_Cdx6500X25StatPortUtilIn_Object = MibTableColumn
cdx6500X25StatPortUtilIn = _Cdx6500X25StatPortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 5),
    _Cdx6500X25StatPortUtilIn_Type()
)
cdx6500X25StatPortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatPortUtilIn.setStatus("mandatory")


class _Cdx6500X25StatPortUtilOut_Type(Integer32):
    """Custom type cdx6500X25StatPortUtilOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500X25StatPortUtilOut_Type.__name__ = "Integer32"
_Cdx6500X25StatPortUtilOut_Object = MibTableColumn
cdx6500X25StatPortUtilOut = _Cdx6500X25StatPortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 6),
    _Cdx6500X25StatPortUtilOut_Type()
)
cdx6500X25StatPortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatPortUtilOut.setStatus("mandatory")
_Cdx6500X25StatMaxSVCCount_Type = Gauge32
_Cdx6500X25StatMaxSVCCount_Object = MibTableColumn
cdx6500X25StatMaxSVCCount = _Cdx6500X25StatMaxSVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 7),
    _Cdx6500X25StatMaxSVCCount_Type()
)
cdx6500X25StatMaxSVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatMaxSVCCount.setStatus("mandatory")


class _Cdx6500X25StatCurrSVCCount_Type(Integer32):
    """Custom type cdx6500X25StatCurrSVCCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Cdx6500X25StatCurrSVCCount_Type.__name__ = "Integer32"
_Cdx6500X25StatCurrSVCCount_Object = MibTableColumn
cdx6500X25StatCurrSVCCount = _Cdx6500X25StatCurrSVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 8),
    _Cdx6500X25StatCurrSVCCount_Type()
)
cdx6500X25StatCurrSVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatCurrSVCCount.setStatus("mandatory")
_Cdx6500X25StatInChars_Type = Counter32
_Cdx6500X25StatInChars_Object = MibTableColumn
cdx6500X25StatInChars = _Cdx6500X25StatInChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 9),
    _Cdx6500X25StatInChars_Type()
)
cdx6500X25StatInChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatInChars.setStatus("mandatory")
_Cdx6500X25StatOutChars_Type = Counter32
_Cdx6500X25StatOutChars_Object = MibTableColumn
cdx6500X25StatOutChars = _Cdx6500X25StatOutChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 10),
    _Cdx6500X25StatOutChars_Type()
)
cdx6500X25StatOutChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatOutChars.setStatus("mandatory")
_Cdx6500X25StatInPkts_Type = Counter32
_Cdx6500X25StatInPkts_Object = MibTableColumn
cdx6500X25StatInPkts = _Cdx6500X25StatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 11),
    _Cdx6500X25StatInPkts_Type()
)
cdx6500X25StatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatInPkts.setStatus("mandatory")
_Cdx6500X25StatOutPkts_Type = Counter32
_Cdx6500X25StatOutPkts_Object = MibTableColumn
cdx6500X25StatOutPkts = _Cdx6500X25StatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 12),
    _Cdx6500X25StatOutPkts_Type()
)
cdx6500X25StatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatOutPkts.setStatus("mandatory")
_Cdx6500X25StatInDataFrames_Type = Counter32
_Cdx6500X25StatInDataFrames_Object = MibTableColumn
cdx6500X25StatInDataFrames = _Cdx6500X25StatInDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 13),
    _Cdx6500X25StatInDataFrames_Type()
)
cdx6500X25StatInDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatInDataFrames.setStatus("mandatory")
_Cdx6500X25StatOutDataFrames_Type = Counter32
_Cdx6500X25StatOutDataFrames_Object = MibTableColumn
cdx6500X25StatOutDataFrames = _Cdx6500X25StatOutDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 14),
    _Cdx6500X25StatOutDataFrames_Type()
)
cdx6500X25StatOutDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatOutDataFrames.setStatus("mandatory")
_Cdx6500X25StatNumPktsQueued_Type = Integer32
_Cdx6500X25StatNumPktsQueued_Object = MibTableColumn
cdx6500X25StatNumPktsQueued = _Cdx6500X25StatNumPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 15),
    _Cdx6500X25StatNumPktsQueued_Type()
)
cdx6500X25StatNumPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatNumPktsQueued.setStatus("mandatory")
_Cdx6500X25StatCharRateIn_Type = Integer32
_Cdx6500X25StatCharRateIn_Object = MibTableColumn
cdx6500X25StatCharRateIn = _Cdx6500X25StatCharRateIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 16),
    _Cdx6500X25StatCharRateIn_Type()
)
cdx6500X25StatCharRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatCharRateIn.setStatus("mandatory")
_Cdx6500X25StatCharRateOut_Type = Integer32
_Cdx6500X25StatCharRateOut_Object = MibTableColumn
cdx6500X25StatCharRateOut = _Cdx6500X25StatCharRateOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 17),
    _Cdx6500X25StatCharRateOut_Type()
)
cdx6500X25StatCharRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatCharRateOut.setStatus("mandatory")
_Cdx6500X25StatPktRateIn_Type = Integer32
_Cdx6500X25StatPktRateIn_Object = MibTableColumn
cdx6500X25StatPktRateIn = _Cdx6500X25StatPktRateIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 18),
    _Cdx6500X25StatPktRateIn_Type()
)
cdx6500X25StatPktRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatPktRateIn.setStatus("mandatory")
_Cdx6500X25StatPktRateOut_Type = Integer32
_Cdx6500X25StatPktRateOut_Object = MibTableColumn
cdx6500X25StatPktRateOut = _Cdx6500X25StatPktRateOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 19),
    _Cdx6500X25StatPktRateOut_Type()
)
cdx6500X25StatPktRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatPktRateOut.setStatus("mandatory")
_Cdx6500X25StatFrameRateIn_Type = Integer32
_Cdx6500X25StatFrameRateIn_Object = MibTableColumn
cdx6500X25StatFrameRateIn = _Cdx6500X25StatFrameRateIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 20),
    _Cdx6500X25StatFrameRateIn_Type()
)
cdx6500X25StatFrameRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatFrameRateIn.setStatus("mandatory")
_Cdx6500X25StatFrameRateOut_Type = Integer32
_Cdx6500X25StatFrameRateOut_Object = MibTableColumn
cdx6500X25StatFrameRateOut = _Cdx6500X25StatFrameRateOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 21),
    _Cdx6500X25StatFrameRateOut_Type()
)
cdx6500X25StatFrameRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatFrameRateOut.setStatus("mandatory")
_Cdx6500X25StatOverrunErrs_Type = Counter16
_Cdx6500X25StatOverrunErrs_Object = MibTableColumn
cdx6500X25StatOverrunErrs = _Cdx6500X25StatOverrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 22),
    _Cdx6500X25StatOverrunErrs_Type()
)
cdx6500X25StatOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatOverrunErrs.setStatus("mandatory")
_Cdx6500X25StatUnderrunErrs_Type = Counter16
_Cdx6500X25StatUnderrunErrs_Object = MibTableColumn
cdx6500X25StatUnderrunErrs = _Cdx6500X25StatUnderrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 23),
    _Cdx6500X25StatUnderrunErrs_Type()
)
cdx6500X25StatUnderrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatUnderrunErrs.setStatus("mandatory")
_Cdx6500X25StatCRCErrs_Type = Counter16
_Cdx6500X25StatCRCErrs_Object = MibTableColumn
cdx6500X25StatCRCErrs = _Cdx6500X25StatCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 24),
    _Cdx6500X25StatCRCErrs_Type()
)
cdx6500X25StatCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatCRCErrs.setStatus("mandatory")
_Cdx6500X25StatInInfoFrames_Type = Counter32
_Cdx6500X25StatInInfoFrames_Object = MibTableColumn
cdx6500X25StatInInfoFrames = _Cdx6500X25StatInInfoFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 25),
    _Cdx6500X25StatInInfoFrames_Type()
)
cdx6500X25StatInInfoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatInInfoFrames.setStatus("mandatory")
_Cdx6500X25StatOutInfoFrames_Type = Counter32
_Cdx6500X25StatOutInfoFrames_Object = MibTableColumn
cdx6500X25StatOutInfoFrames = _Cdx6500X25StatOutInfoFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 26),
    _Cdx6500X25StatOutInfoFrames_Type()
)
cdx6500X25StatOutInfoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatOutInfoFrames.setStatus("mandatory")
_Cdx6500X25StatInRNRFrames_Type = Counter32
_Cdx6500X25StatInRNRFrames_Object = MibTableColumn
cdx6500X25StatInRNRFrames = _Cdx6500X25StatInRNRFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 27),
    _Cdx6500X25StatInRNRFrames_Type()
)
cdx6500X25StatInRNRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatInRNRFrames.setStatus("mandatory")
_Cdx6500X25StatOutRNRFrames_Type = Counter32
_Cdx6500X25StatOutRNRFrames_Object = MibTableColumn
cdx6500X25StatOutRNRFrames = _Cdx6500X25StatOutRNRFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 28),
    _Cdx6500X25StatOutRNRFrames_Type()
)
cdx6500X25StatOutRNRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatOutRNRFrames.setStatus("mandatory")
_Cdx6500X25StatInRRFrames_Type = Counter32
_Cdx6500X25StatInRRFrames_Object = MibTableColumn
cdx6500X25StatInRRFrames = _Cdx6500X25StatInRRFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 29),
    _Cdx6500X25StatInRRFrames_Type()
)
cdx6500X25StatInRRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatInRRFrames.setStatus("mandatory")
_Cdx6500X25StatOutRRFrames_Type = Counter32
_Cdx6500X25StatOutRRFrames_Object = MibTableColumn
cdx6500X25StatOutRRFrames = _Cdx6500X25StatOutRRFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 30),
    _Cdx6500X25StatOutRRFrames_Type()
)
cdx6500X25StatOutRRFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatOutRRFrames.setStatus("mandatory")
_Cdx6500X25StatInREJFrames_Type = Counter32
_Cdx6500X25StatInREJFrames_Object = MibTableColumn
cdx6500X25StatInREJFrames = _Cdx6500X25StatInREJFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 31),
    _Cdx6500X25StatInREJFrames_Type()
)
cdx6500X25StatInREJFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatInREJFrames.setStatus("mandatory")
_Cdx6500X25StatOutREJFrames_Type = Counter32
_Cdx6500X25StatOutREJFrames_Object = MibTableColumn
cdx6500X25StatOutREJFrames = _Cdx6500X25StatOutREJFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 32),
    _Cdx6500X25StatOutREJFrames_Type()
)
cdx6500X25StatOutREJFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatOutREJFrames.setStatus("mandatory")
_Cdx6500X25StatInDataPkts_Type = Counter32
_Cdx6500X25StatInDataPkts_Object = MibTableColumn
cdx6500X25StatInDataPkts = _Cdx6500X25StatInDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 33),
    _Cdx6500X25StatInDataPkts_Type()
)
cdx6500X25StatInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatInDataPkts.setStatus("mandatory")
_Cdx6500X25StatOutDataPkts_Type = Counter32
_Cdx6500X25StatOutDataPkts_Object = MibTableColumn
cdx6500X25StatOutDataPkts = _Cdx6500X25StatOutDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 34),
    _Cdx6500X25StatOutDataPkts_Type()
)
cdx6500X25StatOutDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatOutDataPkts.setStatus("mandatory")
_Cdx6500X25StatNumRxCallsSinceLastReset_Type = Integer32
_Cdx6500X25StatNumRxCallsSinceLastReset_Object = MibTableColumn
cdx6500X25StatNumRxCallsSinceLastReset = _Cdx6500X25StatNumRxCallsSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 35),
    _Cdx6500X25StatNumRxCallsSinceLastReset_Type()
)
cdx6500X25StatNumRxCallsSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatNumRxCallsSinceLastReset.setStatus("mandatory")
_Cdx6500X25StatNumRxCallsRejected_Type = Integer32
_Cdx6500X25StatNumRxCallsRejected_Object = MibTableColumn
cdx6500X25StatNumRxCallsRejected = _Cdx6500X25StatNumRxCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 36),
    _Cdx6500X25StatNumRxCallsRejected_Type()
)
cdx6500X25StatNumRxCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatNumRxCallsRejected.setStatus("mandatory")


class _Cdx6500X25StatRxLastCallFailureCause_Type(Integer32):
    """Custom type cdx6500X25StatRxLastCallFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("callCollision", 200),
          ("callRejected", 197),
          ("failureNotSupported", 203),
          ("invalidConfiguration", 202),
          ("invalidPhoneNumber", 198),
          ("noAvailableVirtualPort", 194),
          ("noFailureReported", 193),
          ("noResourcesAvailable", 196),
          ("notAvailable", 100),
          ("outgoingCallRequestTimeout", 199),
          ("securityViolation", 195),
          ("virtualPortNotAvailable", 201))
    )


_Cdx6500X25StatRxLastCallFailureCause_Type.__name__ = "Integer32"
_Cdx6500X25StatRxLastCallFailureCause_Object = MibTableColumn
cdx6500X25StatRxLastCallFailureCause = _Cdx6500X25StatRxLastCallFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 37),
    _Cdx6500X25StatRxLastCallFailureCause_Type()
)
cdx6500X25StatRxLastCallFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatRxLastCallFailureCause.setStatus("mandatory")


class _Cdx6500X25StatRxLastCalledNumber_Type(DisplayString):
    """Custom type cdx6500X25StatRxLastCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500X25StatRxLastCalledNumber_Type.__name__ = "DisplayString"
_Cdx6500X25StatRxLastCalledNumber_Object = MibTableColumn
cdx6500X25StatRxLastCalledNumber = _Cdx6500X25StatRxLastCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 38),
    _Cdx6500X25StatRxLastCalledNumber_Type()
)
cdx6500X25StatRxLastCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatRxLastCalledNumber.setStatus("mandatory")


class _Cdx6500X25StatRxLastCallingNumber_Type(DisplayString):
    """Custom type cdx6500X25StatRxLastCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500X25StatRxLastCallingNumber_Type.__name__ = "DisplayString"
_Cdx6500X25StatRxLastCallingNumber_Object = MibTableColumn
cdx6500X25StatRxLastCallingNumber = _Cdx6500X25StatRxLastCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 39),
    _Cdx6500X25StatRxLastCallingNumber_Type()
)
cdx6500X25StatRxLastCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatRxLastCallingNumber.setStatus("mandatory")
_Cdx6500X25StatRxMinCallDuration_Type = DisplayString
_Cdx6500X25StatRxMinCallDuration_Object = MibTableColumn
cdx6500X25StatRxMinCallDuration = _Cdx6500X25StatRxMinCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 40),
    _Cdx6500X25StatRxMinCallDuration_Type()
)
cdx6500X25StatRxMinCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatRxMinCallDuration.setStatus("mandatory")
_Cdx6500X25StatRxMaxCallDuration_Type = DisplayString
_Cdx6500X25StatRxMaxCallDuration_Object = MibTableColumn
cdx6500X25StatRxMaxCallDuration = _Cdx6500X25StatRxMaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 41),
    _Cdx6500X25StatRxMaxCallDuration_Type()
)
cdx6500X25StatRxMaxCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatRxMaxCallDuration.setStatus("mandatory")
_Cdx6500X25StatRxAvgCallDuration_Type = DisplayString
_Cdx6500X25StatRxAvgCallDuration_Object = MibTableColumn
cdx6500X25StatRxAvgCallDuration = _Cdx6500X25StatRxAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 42),
    _Cdx6500X25StatRxAvgCallDuration_Type()
)
cdx6500X25StatRxAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatRxAvgCallDuration.setStatus("mandatory")
_Cdx6500X25StatNumTxCallsSinceLastReset_Type = Integer32
_Cdx6500X25StatNumTxCallsSinceLastReset_Object = MibTableColumn
cdx6500X25StatNumTxCallsSinceLastReset = _Cdx6500X25StatNumTxCallsSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 43),
    _Cdx6500X25StatNumTxCallsSinceLastReset_Type()
)
cdx6500X25StatNumTxCallsSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatNumTxCallsSinceLastReset.setStatus("mandatory")
_Cdx6500X25StatNumTxCallsRejected_Type = Integer32
_Cdx6500X25StatNumTxCallsRejected_Object = MibTableColumn
cdx6500X25StatNumTxCallsRejected = _Cdx6500X25StatNumTxCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 44),
    _Cdx6500X25StatNumTxCallsRejected_Type()
)
cdx6500X25StatNumTxCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatNumTxCallsRejected.setStatus("mandatory")


class _Cdx6500X25StatTxLastCallFailureCause_Type(Integer32):
    """Custom type cdx6500X25StatTxLastCallFailureCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("callCollision", 200),
          ("callRejected", 197),
          ("failureNotSupported", 203),
          ("invalidConfiguration", 202),
          ("invalidPhoneNumber", 198),
          ("noAvailableVirtualPort", 194),
          ("noFailureReported", 193),
          ("noResourcesAvailable", 196),
          ("notAvailable", 100),
          ("outgoingCallRequestTimeout", 199),
          ("securityViolation", 195),
          ("virtualPortNotAvailable", 201))
    )


_Cdx6500X25StatTxLastCallFailureCause_Type.__name__ = "Integer32"
_Cdx6500X25StatTxLastCallFailureCause_Object = MibTableColumn
cdx6500X25StatTxLastCallFailureCause = _Cdx6500X25StatTxLastCallFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 45),
    _Cdx6500X25StatTxLastCallFailureCause_Type()
)
cdx6500X25StatTxLastCallFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatTxLastCallFailureCause.setStatus("mandatory")


class _Cdx6500X25StatTxLastCalledNumber_Type(DisplayString):
    """Custom type cdx6500X25StatTxLastCalledNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500X25StatTxLastCalledNumber_Type.__name__ = "DisplayString"
_Cdx6500X25StatTxLastCalledNumber_Object = MibTableColumn
cdx6500X25StatTxLastCalledNumber = _Cdx6500X25StatTxLastCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 46),
    _Cdx6500X25StatTxLastCalledNumber_Type()
)
cdx6500X25StatTxLastCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatTxLastCalledNumber.setStatus("mandatory")


class _Cdx6500X25StatTxLastCallingNumber_Type(DisplayString):
    """Custom type cdx6500X25StatTxLastCallingNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500X25StatTxLastCallingNumber_Type.__name__ = "DisplayString"
_Cdx6500X25StatTxLastCallingNumber_Object = MibTableColumn
cdx6500X25StatTxLastCallingNumber = _Cdx6500X25StatTxLastCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 47),
    _Cdx6500X25StatTxLastCallingNumber_Type()
)
cdx6500X25StatTxLastCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatTxLastCallingNumber.setStatus("mandatory")
_Cdx6500X25StatTxMinCallDuration_Type = DisplayString
_Cdx6500X25StatTxMinCallDuration_Object = MibTableColumn
cdx6500X25StatTxMinCallDuration = _Cdx6500X25StatTxMinCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 48),
    _Cdx6500X25StatTxMinCallDuration_Type()
)
cdx6500X25StatTxMinCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatTxMinCallDuration.setStatus("mandatory")
_Cdx6500X25StatTxMaxCallDuration_Type = DisplayString
_Cdx6500X25StatTxMaxCallDuration_Object = MibTableColumn
cdx6500X25StatTxMaxCallDuration = _Cdx6500X25StatTxMaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 49),
    _Cdx6500X25StatTxMaxCallDuration_Type()
)
cdx6500X25StatTxMaxCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatTxMaxCallDuration.setStatus("mandatory")
_Cdx6500X25StatTxAvgCallDuration_Type = DisplayString
_Cdx6500X25StatTxAvgCallDuration_Object = MibTableColumn
cdx6500X25StatTxAvgCallDuration = _Cdx6500X25StatTxAvgCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 50),
    _Cdx6500X25StatTxAvgCallDuration_Type()
)
cdx6500X25StatTxAvgCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatTxAvgCallDuration.setStatus("mandatory")


class _Cdx6500X25StatSignalingState_Type(Integer32):
    """Custom type cdx6500X25StatSignalingState based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("congested", 4),
          ("connected", 3),
          ("dChannelDown", 6),
          ("disabled", 5),
          ("disabledDChannelDown", 7),
          ("disconnecting", 8),
          ("idle", 1),
          ("notAvailable", 100),
          ("ringing", 2))
    )


_Cdx6500X25StatSignalingState_Type.__name__ = "Integer32"
_Cdx6500X25StatSignalingState_Object = MibTableColumn
cdx6500X25StatSignalingState = _Cdx6500X25StatSignalingState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 51),
    _Cdx6500X25StatSignalingState_Type()
)
cdx6500X25StatSignalingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatSignalingState.setStatus("mandatory")


class _Cdx6500X25StatMaxPortUtilIn_Type(Integer32):
    """Custom type cdx6500X25StatMaxPortUtilIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500X25StatMaxPortUtilIn_Type.__name__ = "Integer32"
_Cdx6500X25StatMaxPortUtilIn_Object = MibTableColumn
cdx6500X25StatMaxPortUtilIn = _Cdx6500X25StatMaxPortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 52),
    _Cdx6500X25StatMaxPortUtilIn_Type()
)
cdx6500X25StatMaxPortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatMaxPortUtilIn.setStatus("mandatory")


class _Cdx6500X25StatMaxPortUtilOut_Type(Integer32):
    """Custom type cdx6500X25StatMaxPortUtilOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500X25StatMaxPortUtilOut_Type.__name__ = "Integer32"
_Cdx6500X25StatMaxPortUtilOut_Object = MibTableColumn
cdx6500X25StatMaxPortUtilOut = _Cdx6500X25StatMaxPortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 53),
    _Cdx6500X25StatMaxPortUtilOut_Type()
)
cdx6500X25StatMaxPortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatMaxPortUtilOut.setStatus("mandatory")
_Cdx6500X25StatMaxPortUtilInTime_Type = DisplayString
_Cdx6500X25StatMaxPortUtilInTime_Object = MibTableColumn
cdx6500X25StatMaxPortUtilInTime = _Cdx6500X25StatMaxPortUtilInTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 54),
    _Cdx6500X25StatMaxPortUtilInTime_Type()
)
cdx6500X25StatMaxPortUtilInTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatMaxPortUtilInTime.setStatus("mandatory")
_Cdx6500X25StatMaxPortUtilOutTime_Type = DisplayString
_Cdx6500X25StatMaxPortUtilOutTime_Object = MibTableColumn
cdx6500X25StatMaxPortUtilOutTime = _Cdx6500X25StatMaxPortUtilOutTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 55),
    _Cdx6500X25StatMaxPortUtilOutTime_Type()
)
cdx6500X25StatMaxPortUtilOutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatMaxPortUtilOutTime.setStatus("mandatory")
_Cdx6500X25StatMaxSVCCountTime_Type = DisplayString
_Cdx6500X25StatMaxSVCCountTime_Object = MibTableColumn
cdx6500X25StatMaxSVCCountTime = _Cdx6500X25StatMaxSVCCountTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 2, 1, 56),
    _Cdx6500X25StatMaxSVCCountTime_Type()
)
cdx6500X25StatMaxSVCCountTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500X25StatMaxSVCCountTime.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "X25-OPT-MIB",
    **{"DisplayString": DisplayString,
       "Counter16": Counter16,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTX25PortTable": cdx6500PPCTX25PortTable,
       "cdx6500PPCTX25PortEntry": cdx6500PPCTX25PortEntry,
       "cdx6500X25CfgPortNumber": cdx6500X25CfgPortNumber,
       "cdx6500X25CfgConnType": cdx6500X25CfgConnType,
       "cdx6500X25CfgPortCont": cdx6500X25CfgPortCont,
       "cdx6500X25CfgClockSource": cdx6500X25CfgClockSource,
       "cdx6500X25CfgClockSpeed": cdx6500X25CfgClockSpeed,
       "cdx6500X25CfgAdmnInterfaceMode": cdx6500X25CfgAdmnInterfaceMode,
       "cdx6500X25CfgAdmnNumberPVCs": cdx6500X25CfgAdmnNumberPVCs,
       "cdx6500X25CfgStartPVCChanNum": cdx6500X25CfgStartPVCChanNum,
       "cdx6500X25CfgNumberSVCs": cdx6500X25CfgNumberSVCs,
       "cdx6500X25CfgStartSVCChanNum": cdx6500X25CfgStartSVCChanNum,
       "cdx6500X25CfgInitFrame": cdx6500X25CfgInitFrame,
       "cdx6500X25CfgT1RetryTimer": cdx6500X25CfgT1RetryTimer,
       "cdx6500X25CfgT4PollTimer": cdx6500X25CfgT4PollTimer,
       "cdx6500X25CfgN2TransTries": cdx6500X25CfgN2TransTries,
       "cdx6500X25CfgFrameSeqCounting": cdx6500X25CfgFrameSeqCounting,
       "cdx6500X25CfgKFrameWindow": cdx6500X25CfgKFrameWindow,
       "cdx6500X25CfgAdmnPacketSequencing": cdx6500X25CfgAdmnPacketSequencing,
       "cdx6500X25CfgWPacketWindow": cdx6500X25CfgWPacketWindow,
       "cdx6500X25CfgPPacketSize": cdx6500X25CfgPPacketSize,
       "cdx6500X25CfgMaxNegotPacketSize": cdx6500X25CfgMaxNegotPacketSize,
       "cdx6500X25CfgDataQueueUpper": cdx6500X25CfgDataQueueUpper,
       "cdx6500X25CfgDataQueueLower": cdx6500X25CfgDataQueueLower,
       "cdx6500X25CfgAdmnRestartTimer": cdx6500X25CfgAdmnRestartTimer,
       "cdx6500X25CfgAdmnResetTimer": cdx6500X25CfgAdmnResetTimer,
       "cdx6500X25CfgAdmnCallTimer": cdx6500X25CfgAdmnCallTimer,
       "cdx6500X25CfgAdmnClearTimer": cdx6500X25CfgAdmnClearTimer,
       "cdx6500X25CfgOutDelFacilities": cdx6500X25CfgOutDelFacilities,
       "cdx6500X25CfgOutAddFacilities": cdx6500X25CfgOutAddFacilities,
       "cdx6500X25CfgOutBarFacilities": cdx6500X25CfgOutBarFacilities,
       "cdx6500X25CfgInBarFacilities": cdx6500X25CfgInBarFacilities,
       "cdx6500X25CfgOptions": cdx6500X25CfgOptions,
       "cdx6500X25CfgNumRoutDigits": cdx6500X25CfgNumRoutDigits,
       "cdx6500X25CfgPortDigitsToStrip": cdx6500X25CfgPortDigitsToStrip,
       "cdx6500X25CfgInDigitsToStrip": cdx6500X25CfgInDigitsToStrip,
       "cdx6500X25CfgRestrictConn": cdx6500X25CfgRestrictConn,
       "cdx6500X25CfgPortAddress": cdx6500X25CfgPortAddress,
       "cdx6500X25CfgCUGMember": cdx6500X25CfgCUGMember,
       "cdx6500X25CfgBillRec": cdx6500X25CfgBillRec,
       "cdx6500X25CfgSubAddrSize": cdx6500X25CfgSubAddrSize,
       "cdx6500X25CfgIdleDiscTimer": cdx6500X25CfgIdleDiscTimer,
       "cdx6500X25CfgCallSecurity": cdx6500X25CfgCallSecurity,
       "cdx6500X25CfgProtectLevel": cdx6500X25CfgProtectLevel,
       "cdx6500X25CfgReconnTimeout": cdx6500X25CfgReconnTimeout,
       "cdx6500X25CfgReconnTriesLimit": cdx6500X25CfgReconnTriesLimit,
       "cdx6500X25CfgFacilSubscripCont": cdx6500X25CfgFacilSubscripCont,
       "cdx6500X25CfgAlarmPriority": cdx6500X25CfgAlarmPriority,
       "cdx6500X25CfgAddrTrans": cdx6500X25CfgAddrTrans,
       "cdx6500X25CfgNumberInSVCs": cdx6500X25CfgNumberInSVCs,
       "cdx6500X25CfgStartInSVCChanNum": cdx6500X25CfgStartInSVCChanNum,
       "cdx6500X25CfgNumberOutSVCs": cdx6500X25CfgNumberOutSVCs,
       "cdx6500X25CfgStartOutSVCChanNum": cdx6500X25CfgStartOutSVCChanNum,
       "cdx6500X25CfgChargeInfoReq": cdx6500X25CfgChargeInfoReq,
       "cdx6500X25CfgVerfnTimer": cdx6500X25CfgVerfnTimer,
       "cdx6500X25CfgValdFailures": cdx6500X25CfgValdFailures,
       "cdx6500X25CfgActionType": cdx6500X25CfgActionType,
       "cdx6500X25CfgLineIdleMode": cdx6500X25CfgLineIdleMode,
       "cdx6500X25CfgConfOption": cdx6500X25CfgConfOption,
       "cdx6500X25CfgInvertTxClk": cdx6500X25CfgInvertTxClk,
       "cdx6500X25CfgDimType": cdx6500X25CfgDimType,
       "cdx6500X25CfgMoreOptions": cdx6500X25CfgMoreOptions,
       "cdx6500X25CfgPsfFlag": cdx6500X25CfgPsfFlag,
       "cdx6500X25CfgElectricalInterfaceType": cdx6500X25CfgElectricalInterfaceType,
       "cdx6500X25CfgV24ElectricalInterfaceOption": cdx6500X25CfgV24ElectricalInterfaceOption,
       "cdx6500X25CfgHighSpeedElectricalInterfaceOption": cdx6500X25CfgHighSpeedElectricalInterfaceOption,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500CGTInboundCallTranTable": cdx6500CGTInboundCallTranTable,
       "cdx6500CGTInboundCallTranEntry": cdx6500CGTInboundCallTranEntry,
       "cdx6500InCallTranEntryNum": cdx6500InCallTranEntryNum,
       "cdx6500InCallTranInSubAddr": cdx6500InCallTranInSubAddr,
       "cdx6500InCallTranPrivNetAddr": cdx6500InCallTranPrivNetAddr,
       "cdx6500CGTOutboundCallTranTable": cdx6500CGTOutboundCallTranTable,
       "cdx6500CGTOutboundCallTranEntry": cdx6500CGTOutboundCallTranEntry,
       "cdx6500OutCallTranEntryNum": cdx6500OutCallTranEntryNum,
       "cdx6500OutCallTranPrivNetAddr": cdx6500OutCallTranPrivNetAddr,
       "cdx6500OutCallTranOutNetAddr": cdx6500OutCallTranOutNetAddr,
       "cdx6500OutCallTranOptions": cdx6500OutCallTranOptions,
       "cdx6500CGTCallingAddrTranTable": cdx6500CGTCallingAddrTranTable,
       "cdx6500CGTCallingAddrTranEntry": cdx6500CGTCallingAddrTranEntry,
       "cdx6500CalladdrtranEntryNum": cdx6500CalladdrtranEntryNum,
       "cdx6500CalladdrtranInCallAddr": cdx6500CalladdrtranInCallAddr,
       "cdx6500CalladdrtranPrivNetAddr": cdx6500CalladdrtranPrivNetAddr,
       "cdx6500CGTCudBaseAddrTranTable": cdx6500CGTCudBaseAddrTranTable,
       "cdx6500CGTCudBaseAddrTranEntry": cdx6500CGTCudBaseAddrTranEntry,
       "cdx6500CudBaseaddrtranEntryNum": cdx6500CudBaseaddrtranEntryNum,
       "cdx6500CudBaseStr": cdx6500CudBaseStr,
       "cdx6500CudBaseAddr": cdx6500CudBaseAddr,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTX25PortTable": cdx6500PPSTX25PortTable,
       "cdx6500PPSTX25PortEntry": cdx6500PPSTX25PortEntry,
       "cdx6500X25StatPortNumber": cdx6500X25StatPortNumber,
       "cdx6500X25StatPortStatus": cdx6500X25StatPortStatus,
       "cdx6500X25StatPortState": cdx6500X25StatPortState,
       "cdx6500X25StatActualPortSpeed": cdx6500X25StatActualPortSpeed,
       "cdx6500X25StatPortUtilIn": cdx6500X25StatPortUtilIn,
       "cdx6500X25StatPortUtilOut": cdx6500X25StatPortUtilOut,
       "cdx6500X25StatMaxSVCCount": cdx6500X25StatMaxSVCCount,
       "cdx6500X25StatCurrSVCCount": cdx6500X25StatCurrSVCCount,
       "cdx6500X25StatInChars": cdx6500X25StatInChars,
       "cdx6500X25StatOutChars": cdx6500X25StatOutChars,
       "cdx6500X25StatInPkts": cdx6500X25StatInPkts,
       "cdx6500X25StatOutPkts": cdx6500X25StatOutPkts,
       "cdx6500X25StatInDataFrames": cdx6500X25StatInDataFrames,
       "cdx6500X25StatOutDataFrames": cdx6500X25StatOutDataFrames,
       "cdx6500X25StatNumPktsQueued": cdx6500X25StatNumPktsQueued,
       "cdx6500X25StatCharRateIn": cdx6500X25StatCharRateIn,
       "cdx6500X25StatCharRateOut": cdx6500X25StatCharRateOut,
       "cdx6500X25StatPktRateIn": cdx6500X25StatPktRateIn,
       "cdx6500X25StatPktRateOut": cdx6500X25StatPktRateOut,
       "cdx6500X25StatFrameRateIn": cdx6500X25StatFrameRateIn,
       "cdx6500X25StatFrameRateOut": cdx6500X25StatFrameRateOut,
       "cdx6500X25StatOverrunErrs": cdx6500X25StatOverrunErrs,
       "cdx6500X25StatUnderrunErrs": cdx6500X25StatUnderrunErrs,
       "cdx6500X25StatCRCErrs": cdx6500X25StatCRCErrs,
       "cdx6500X25StatInInfoFrames": cdx6500X25StatInInfoFrames,
       "cdx6500X25StatOutInfoFrames": cdx6500X25StatOutInfoFrames,
       "cdx6500X25StatInRNRFrames": cdx6500X25StatInRNRFrames,
       "cdx6500X25StatOutRNRFrames": cdx6500X25StatOutRNRFrames,
       "cdx6500X25StatInRRFrames": cdx6500X25StatInRRFrames,
       "cdx6500X25StatOutRRFrames": cdx6500X25StatOutRRFrames,
       "cdx6500X25StatInREJFrames": cdx6500X25StatInREJFrames,
       "cdx6500X25StatOutREJFrames": cdx6500X25StatOutREJFrames,
       "cdx6500X25StatInDataPkts": cdx6500X25StatInDataPkts,
       "cdx6500X25StatOutDataPkts": cdx6500X25StatOutDataPkts,
       "cdx6500X25StatNumRxCallsSinceLastReset": cdx6500X25StatNumRxCallsSinceLastReset,
       "cdx6500X25StatNumRxCallsRejected": cdx6500X25StatNumRxCallsRejected,
       "cdx6500X25StatRxLastCallFailureCause": cdx6500X25StatRxLastCallFailureCause,
       "cdx6500X25StatRxLastCalledNumber": cdx6500X25StatRxLastCalledNumber,
       "cdx6500X25StatRxLastCallingNumber": cdx6500X25StatRxLastCallingNumber,
       "cdx6500X25StatRxMinCallDuration": cdx6500X25StatRxMinCallDuration,
       "cdx6500X25StatRxMaxCallDuration": cdx6500X25StatRxMaxCallDuration,
       "cdx6500X25StatRxAvgCallDuration": cdx6500X25StatRxAvgCallDuration,
       "cdx6500X25StatNumTxCallsSinceLastReset": cdx6500X25StatNumTxCallsSinceLastReset,
       "cdx6500X25StatNumTxCallsRejected": cdx6500X25StatNumTxCallsRejected,
       "cdx6500X25StatTxLastCallFailureCause": cdx6500X25StatTxLastCallFailureCause,
       "cdx6500X25StatTxLastCalledNumber": cdx6500X25StatTxLastCalledNumber,
       "cdx6500X25StatTxLastCallingNumber": cdx6500X25StatTxLastCallingNumber,
       "cdx6500X25StatTxMinCallDuration": cdx6500X25StatTxMinCallDuration,
       "cdx6500X25StatTxMaxCallDuration": cdx6500X25StatTxMaxCallDuration,
       "cdx6500X25StatTxAvgCallDuration": cdx6500X25StatTxAvgCallDuration,
       "cdx6500X25StatSignalingState": cdx6500X25StatSignalingState,
       "cdx6500X25StatMaxPortUtilIn": cdx6500X25StatMaxPortUtilIn,
       "cdx6500X25StatMaxPortUtilOut": cdx6500X25StatMaxPortUtilOut,
       "cdx6500X25StatMaxPortUtilInTime": cdx6500X25StatMaxPortUtilInTime,
       "cdx6500X25StatMaxPortUtilOutTime": cdx6500X25StatMaxPortUtilOutTime,
       "cdx6500X25StatMaxSVCCountTime": cdx6500X25StatMaxSVCCountTime,
       "cdx6500Controls": cdx6500Controls}
)

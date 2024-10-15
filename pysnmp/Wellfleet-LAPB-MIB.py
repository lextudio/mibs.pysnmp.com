# SNMP MIB module (Wellfleet-LAPB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-LAPB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:35 2024
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

(wfDataLink,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDataLink")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfLapbTable_Object = MibTable
wfLapbTable = _WfLapbTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8)
)
if mibBuilder.loadTexts:
    wfLapbTable.setStatus("mandatory")
_WfLapbEntry_Object = MibTableRow
wfLapbEntry = _WfLapbEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1)
)
wfLapbEntry.setIndexNames(
    (0, "Wellfleet-LAPB-MIB", "wfLapbLineNumber"),
    (0, "Wellfleet-LAPB-MIB", "wfLapbLLIndex"),
)
if mibBuilder.loadTexts:
    wfLapbEntry.setStatus("mandatory")


class _WfLapbDelete_Type(Integer32):
    """Custom type wfLapbDelete based on Integer32"""
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


_WfLapbDelete_Type.__name__ = "Integer32"
_WfLapbDelete_Object = MibTableColumn
wfLapbDelete = _WfLapbDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 1),
    _WfLapbDelete_Type()
)
wfLapbDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbDelete.setStatus("mandatory")


class _WfLapbDisable_Type(Integer32):
    """Custom type wfLapbDisable based on Integer32"""
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


_WfLapbDisable_Type.__name__ = "Integer32"
_WfLapbDisable_Object = MibTableColumn
wfLapbDisable = _WfLapbDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 2),
    _WfLapbDisable_Type()
)
wfLapbDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbDisable.setStatus("mandatory")


class _WfLapbState_Type(Integer32):
    """Custom type wfLapbState based on Integer32"""
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


_WfLapbState_Type.__name__ = "Integer32"
_WfLapbState_Object = MibTableColumn
wfLapbState = _WfLapbState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 3),
    _WfLapbState_Type()
)
wfLapbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbState.setStatus("mandatory")
_WfLapbLineNumber_Type = Integer32
_WfLapbLineNumber_Object = MibTableColumn
wfLapbLineNumber = _WfLapbLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 4),
    _WfLapbLineNumber_Type()
)
wfLapbLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbLineNumber.setStatus("mandatory")
_WfLapbLLIndex_Type = Integer32
_WfLapbLLIndex_Object = MibTableColumn
wfLapbLLIndex = _WfLapbLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 5),
    _WfLapbLLIndex_Type()
)
wfLapbLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbLLIndex.setStatus("mandatory")
_WfLapbCct_Type = Integer32
_WfLapbCct_Object = MibTableColumn
wfLapbCct = _WfLapbCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 6),
    _WfLapbCct_Type()
)
wfLapbCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbCct.setStatus("mandatory")


class _WfLapbStationType_Type(Integer32):
    """Custom type wfLapbStationType based on Integer32"""
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
        *(("dce", 2),
          ("dte", 1),
          ("dxe", 3))
    )


_WfLapbStationType_Type.__name__ = "Integer32"
_WfLapbStationType_Object = MibTableColumn
wfLapbStationType = _WfLapbStationType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 7),
    _WfLapbStationType_Type()
)
wfLapbStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbStationType.setStatus("mandatory")


class _WfLapbControlField_Type(Integer32):
    """Custom type wfLapbControlField based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_WfLapbControlField_Type.__name__ = "Integer32"
_WfLapbControlField_Object = MibTableColumn
wfLapbControlField = _WfLapbControlField_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 8),
    _WfLapbControlField_Type()
)
wfLapbControlField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbControlField.setStatus("mandatory")


class _WfLapbN1FrameSize_Type(Integer32):
    """Custom type wfLapbN1FrameSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4500),
    )


_WfLapbN1FrameSize_Type.__name__ = "Integer32"
_WfLapbN1FrameSize_Object = MibTableColumn
wfLapbN1FrameSize = _WfLapbN1FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 9),
    _WfLapbN1FrameSize_Type()
)
wfLapbN1FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbN1FrameSize.setStatus("mandatory")


class _WfLapbKWindowSize_Type(Integer32):
    """Custom type wfLapbKWindowSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfLapbKWindowSize_Type.__name__ = "Integer32"
_WfLapbKWindowSize_Object = MibTableColumn
wfLapbKWindowSize = _WfLapbKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 10),
    _WfLapbKWindowSize_Type()
)
wfLapbKWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbKWindowSize.setStatus("mandatory")


class _WfLapbN2RxmitCount_Type(Integer32):
    """Custom type wfLapbN2RxmitCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WfLapbN2RxmitCount_Type.__name__ = "Integer32"
_WfLapbN2RxmitCount_Object = MibTableColumn
wfLapbN2RxmitCount = _WfLapbN2RxmitCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 11),
    _WfLapbN2RxmitCount_Type()
)
wfLapbN2RxmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbN2RxmitCount.setStatus("mandatory")


class _WfLapbT1AckTimer_Type(Integer32):
    """Custom type wfLapbT1AckTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_WfLapbT1AckTimer_Type.__name__ = "Integer32"
_WfLapbT1AckTimer_Object = MibTableColumn
wfLapbT1AckTimer = _WfLapbT1AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 12),
    _WfLapbT1AckTimer_Type()
)
wfLapbT1AckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbT1AckTimer.setStatus("mandatory")


class _WfLapbT2AckDelayTimer_Type(Integer32):
    """Custom type wfLapbT2AckDelayTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_WfLapbT2AckDelayTimer_Type.__name__ = "Integer32"
_WfLapbT2AckDelayTimer_Object = MibTableColumn
wfLapbT2AckDelayTimer = _WfLapbT2AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 13),
    _WfLapbT2AckDelayTimer_Type()
)
wfLapbT2AckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbT2AckDelayTimer.setStatus("mandatory")


class _WfLapbT3DisconnectTimer_Type(Integer32):
    """Custom type wfLapbT3DisconnectTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_WfLapbT3DisconnectTimer_Type.__name__ = "Integer32"
_WfLapbT3DisconnectTimer_Object = MibTableColumn
wfLapbT3DisconnectTimer = _WfLapbT3DisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 14),
    _WfLapbT3DisconnectTimer_Type()
)
wfLapbT3DisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbT3DisconnectTimer.setStatus("mandatory")


class _WfLapbT4IdleTimer_Type(Integer32):
    """Custom type wfLapbT4IdleTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_WfLapbT4IdleTimer_Type.__name__ = "Integer32"
_WfLapbT4IdleTimer_Object = MibTableColumn
wfLapbT4IdleTimer = _WfLapbT4IdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 15),
    _WfLapbT4IdleTimer_Type()
)
wfLapbT4IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbT4IdleTimer.setStatus("mandatory")


class _WfLapbActionInitiate_Type(Integer32):
    """Custom type wfLapbActionInitiate based on Integer32"""
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
        *(("active", 1),
          ("activeDisc", 3),
          ("passive", 2))
    )


_WfLapbActionInitiate_Type.__name__ = "Integer32"
_WfLapbActionInitiate_Object = MibTableColumn
wfLapbActionInitiate = _WfLapbActionInitiate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 16),
    _WfLapbActionInitiate_Type()
)
wfLapbActionInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbActionInitiate.setStatus("mandatory")


class _WfLapbXidDisable_Type(Integer32):
    """Custom type wfLapbXidDisable based on Integer32"""
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


_WfLapbXidDisable_Type.__name__ = "Integer32"
_WfLapbXidDisable_Object = MibTableColumn
wfLapbXidDisable = _WfLapbXidDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 17),
    _WfLapbXidDisable_Type()
)
wfLapbXidDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbXidDisable.setStatus("mandatory")


class _WfLapbCommandAddress_Type(Integer32):
    """Custom type wfLapbCommandAddress based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 3),
          ("dte", 1))
    )


_WfLapbCommandAddress_Type.__name__ = "Integer32"
_WfLapbCommandAddress_Object = MibTableColumn
wfLapbCommandAddress = _WfLapbCommandAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 18),
    _WfLapbCommandAddress_Type()
)
wfLapbCommandAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbCommandAddress.setStatus("mandatory")


class _WfLapbResponseAddress_Type(Integer32):
    """Custom type wfLapbResponseAddress based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 3))
    )


_WfLapbResponseAddress_Type.__name__ = "Integer32"
_WfLapbResponseAddress_Object = MibTableColumn
wfLapbResponseAddress = _WfLapbResponseAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 19),
    _WfLapbResponseAddress_Type()
)
wfLapbResponseAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbResponseAddress.setStatus("mandatory")


class _WfLapbWanProtocol_Type(Integer32):
    """Custom type wfLapbWanProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("lapb", 7),
          ("standard", 1),
          ("x25", 6))
    )


_WfLapbWanProtocol_Type.__name__ = "Integer32"
_WfLapbWanProtocol_Object = MibTableColumn
wfLapbWanProtocol = _WfLapbWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 20),
    _WfLapbWanProtocol_Type()
)
wfLapbWanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbWanProtocol.setStatus("mandatory")
_WfLapbRxOctets_Type = Counter32
_WfLapbRxOctets_Object = MibTableColumn
wfLapbRxOctets = _WfLapbRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 21),
    _WfLapbRxOctets_Type()
)
wfLapbRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbRxOctets.setStatus("mandatory")
_WfLapbRxFrames_Type = Counter32
_WfLapbRxFrames_Object = MibTableColumn
wfLapbRxFrames = _WfLapbRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 22),
    _WfLapbRxFrames_Type()
)
wfLapbRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbRxFrames.setStatus("mandatory")
_WfLapbTxOctets_Type = Counter32
_WfLapbTxOctets_Object = MibTableColumn
wfLapbTxOctets = _WfLapbTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 23),
    _WfLapbTxOctets_Type()
)
wfLapbTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbTxOctets.setStatus("mandatory")
_WfLapbTxFrames_Type = Counter32
_WfLapbTxFrames_Object = MibTableColumn
wfLapbTxFrames = _WfLapbTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 24),
    _WfLapbTxFrames_Type()
)
wfLapbTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbTxFrames.setStatus("mandatory")
_WfLapbReXmits_Type = Counter32
_WfLapbReXmits_Object = MibTableColumn
wfLapbReXmits = _WfLapbReXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 25),
    _WfLapbReXmits_Type()
)
wfLapbReXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbReXmits.setStatus("mandatory")
_WfLapbRejectsTx_Type = Counter32
_WfLapbRejectsTx_Object = MibTableColumn
wfLapbRejectsTx = _WfLapbRejectsTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 26),
    _WfLapbRejectsTx_Type()
)
wfLapbRejectsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbRejectsTx.setStatus("mandatory")
_WfLapbRejectsRx_Type = Counter32
_WfLapbRejectsRx_Object = MibTableColumn
wfLapbRejectsRx = _WfLapbRejectsRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 27),
    _WfLapbRejectsRx_Type()
)
wfLapbRejectsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbRejectsRx.setStatus("mandatory")
_WfLapbFrameRejectsTx_Type = Counter32
_WfLapbFrameRejectsTx_Object = MibTableColumn
wfLapbFrameRejectsTx = _WfLapbFrameRejectsTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 28),
    _WfLapbFrameRejectsTx_Type()
)
wfLapbFrameRejectsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbFrameRejectsTx.setStatus("mandatory")
_WfLapbFrameRejectsRx_Type = Counter32
_WfLapbFrameRejectsRx_Object = MibTableColumn
wfLapbFrameRejectsRx = _WfLapbFrameRejectsRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 29),
    _WfLapbFrameRejectsRx_Type()
)
wfLapbFrameRejectsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbFrameRejectsRx.setStatus("mandatory")
_WfLapbRRsTx_Type = Counter32
_WfLapbRRsTx_Object = MibTableColumn
wfLapbRRsTx = _WfLapbRRsTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 30),
    _WfLapbRRsTx_Type()
)
wfLapbRRsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbRRsTx.setStatus("mandatory")
_WfLapbRRsRx_Type = Counter32
_WfLapbRRsRx_Object = MibTableColumn
wfLapbRRsRx = _WfLapbRRsRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 31),
    _WfLapbRRsRx_Type()
)
wfLapbRRsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbRRsRx.setStatus("mandatory")
_WfLapbRNRsTx_Type = Counter32
_WfLapbRNRsTx_Object = MibTableColumn
wfLapbRNRsTx = _WfLapbRNRsTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 32),
    _WfLapbRNRsTx_Type()
)
wfLapbRNRsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbRNRsTx.setStatus("mandatory")
_WfLapbRNRsRx_Type = Counter32
_WfLapbRNRsRx_Object = MibTableColumn
wfLapbRNRsRx = _WfLapbRNRsRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 33),
    _WfLapbRNRsRx_Type()
)
wfLapbRNRsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbRNRsRx.setStatus("mandatory")
_WfLapbResets_Type = Counter32
_WfLapbResets_Object = MibTableColumn
wfLapbResets = _WfLapbResets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 34),
    _WfLapbResets_Type()
)
wfLapbResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbResets.setStatus("mandatory")
_WfLapbNormalDisc_Type = Counter32
_WfLapbNormalDisc_Object = MibTableColumn
wfLapbNormalDisc = _WfLapbNormalDisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 35),
    _WfLapbNormalDisc_Type()
)
wfLapbNormalDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbNormalDisc.setStatus("mandatory")
_WfLapbAbnormalDisc_Type = Counter32
_WfLapbAbnormalDisc_Object = MibTableColumn
wfLapbAbnormalDisc = _WfLapbAbnormalDisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 36),
    _WfLapbAbnormalDisc_Type()
)
wfLapbAbnormalDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbAbnormalDisc.setStatus("mandatory")
_WfLapbSetupAllowed_Type = Counter32
_WfLapbSetupAllowed_Object = MibTableColumn
wfLapbSetupAllowed = _WfLapbSetupAllowed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 37),
    _WfLapbSetupAllowed_Type()
)
wfLapbSetupAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbSetupAllowed.setStatus("mandatory")
_WfLapbSetupRefused_Type = Counter32
_WfLapbSetupRefused_Object = MibTableColumn
wfLapbSetupRefused = _WfLapbSetupRefused_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 38),
    _WfLapbSetupRefused_Type()
)
wfLapbSetupRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapbSetupRefused.setStatus("mandatory")


class _WfLapbNetworkType_Type(Integer32):
    """Custom type wfLapbNetworkType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gosip", 1),
          ("net2", 2))
    )


_WfLapbNetworkType_Type.__name__ = "Integer32"
_WfLapbNetworkType_Object = MibTableColumn
wfLapbNetworkType = _WfLapbNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 39),
    _WfLapbNetworkType_Type()
)
wfLapbNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbNetworkType.setStatus("mandatory")


class _WfLapbIdleRRFrames_Type(Integer32):
    """Custom type wfLapbIdleRRFrames based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfLapbIdleRRFrames_Type.__name__ = "Integer32"
_WfLapbIdleRRFrames_Object = MibTableColumn
wfLapbIdleRRFrames = _WfLapbIdleRRFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 40),
    _WfLapbIdleRRFrames_Type()
)
wfLapbIdleRRFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbIdleRRFrames.setStatus("mandatory")


class _WfLapbClientType_Type(Integer32):
    """Custom type wfLapbClientType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipex", 3),
          ("none", 1),
          ("x25", 2))
    )


_WfLapbClientType_Type.__name__ = "Integer32"
_WfLapbClientType_Object = MibTableColumn
wfLapbClientType = _WfLapbClientType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 41),
    _WfLapbClientType_Type()
)
wfLapbClientType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbClientType.setStatus("mandatory")


class _WfLapbRetransmitTimer_Type(Integer32):
    """Custom type wfLapbRetransmitTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfLapbRetransmitTimer_Type.__name__ = "Integer32"
_WfLapbRetransmitTimer_Object = MibTableColumn
wfLapbRetransmitTimer = _WfLapbRetransmitTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 8, 1, 42),
    _WfLapbRetransmitTimer_Type()
)
wfLapbRetransmitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapbRetransmitTimer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-LAPB-MIB",
    **{"wfLapbTable": wfLapbTable,
       "wfLapbEntry": wfLapbEntry,
       "wfLapbDelete": wfLapbDelete,
       "wfLapbDisable": wfLapbDisable,
       "wfLapbState": wfLapbState,
       "wfLapbLineNumber": wfLapbLineNumber,
       "wfLapbLLIndex": wfLapbLLIndex,
       "wfLapbCct": wfLapbCct,
       "wfLapbStationType": wfLapbStationType,
       "wfLapbControlField": wfLapbControlField,
       "wfLapbN1FrameSize": wfLapbN1FrameSize,
       "wfLapbKWindowSize": wfLapbKWindowSize,
       "wfLapbN2RxmitCount": wfLapbN2RxmitCount,
       "wfLapbT1AckTimer": wfLapbT1AckTimer,
       "wfLapbT2AckDelayTimer": wfLapbT2AckDelayTimer,
       "wfLapbT3DisconnectTimer": wfLapbT3DisconnectTimer,
       "wfLapbT4IdleTimer": wfLapbT4IdleTimer,
       "wfLapbActionInitiate": wfLapbActionInitiate,
       "wfLapbXidDisable": wfLapbXidDisable,
       "wfLapbCommandAddress": wfLapbCommandAddress,
       "wfLapbResponseAddress": wfLapbResponseAddress,
       "wfLapbWanProtocol": wfLapbWanProtocol,
       "wfLapbRxOctets": wfLapbRxOctets,
       "wfLapbRxFrames": wfLapbRxFrames,
       "wfLapbTxOctets": wfLapbTxOctets,
       "wfLapbTxFrames": wfLapbTxFrames,
       "wfLapbReXmits": wfLapbReXmits,
       "wfLapbRejectsTx": wfLapbRejectsTx,
       "wfLapbRejectsRx": wfLapbRejectsRx,
       "wfLapbFrameRejectsTx": wfLapbFrameRejectsTx,
       "wfLapbFrameRejectsRx": wfLapbFrameRejectsRx,
       "wfLapbRRsTx": wfLapbRRsTx,
       "wfLapbRRsRx": wfLapbRRsRx,
       "wfLapbRNRsTx": wfLapbRNRsTx,
       "wfLapbRNRsRx": wfLapbRNRsRx,
       "wfLapbResets": wfLapbResets,
       "wfLapbNormalDisc": wfLapbNormalDisc,
       "wfLapbAbnormalDisc": wfLapbAbnormalDisc,
       "wfLapbSetupAllowed": wfLapbSetupAllowed,
       "wfLapbSetupRefused": wfLapbSetupRefused,
       "wfLapbNetworkType": wfLapbNetworkType,
       "wfLapbIdleRRFrames": wfLapbIdleRRFrames,
       "wfLapbClientType": wfLapbClientType,
       "wfLapbRetransmitTimer": wfLapbRetransmitTimer}
)

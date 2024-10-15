# SNMP MIB module (Wellfleet-CSMACD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-CSMACD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:59 2024
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

(wfCSMACDAutoNegGroup,
 wfLine) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfCSMACDAutoNegGroup",
    "wfLine")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfCSMACDTable_Object = MibTable
wfCSMACDTable = _WfCSMACDTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1)
)
if mibBuilder.loadTexts:
    wfCSMACDTable.setStatus("mandatory")
_WfCSMACDEntry_Object = MibTableRow
wfCSMACDEntry = _WfCSMACDEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1)
)
wfCSMACDEntry.setIndexNames(
    (0, "Wellfleet-CSMACD-MIB", "wfCSMACDSlot"),
    (0, "Wellfleet-CSMACD-MIB", "wfCSMACDConnector"),
)
if mibBuilder.loadTexts:
    wfCSMACDEntry.setStatus("mandatory")


class _WfCSMACDDelete_Type(Integer32):
    """Custom type wfCSMACDDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfCSMACDDelete_Type.__name__ = "Integer32"
_WfCSMACDDelete_Object = MibTableColumn
wfCSMACDDelete = _WfCSMACDDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 1),
    _WfCSMACDDelete_Type()
)
wfCSMACDDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDDelete.setStatus("mandatory")


class _WfCSMACDEnable_Type(Integer32):
    """Custom type wfCSMACDEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfCSMACDEnable_Type.__name__ = "Integer32"
_WfCSMACDEnable_Object = MibTableColumn
wfCSMACDEnable = _WfCSMACDEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 2),
    _WfCSMACDEnable_Type()
)
wfCSMACDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDEnable.setStatus("mandatory")


class _WfCSMACDState_Type(Integer32):
    """Custom type wfCSMACDState based on Integer32"""
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


_WfCSMACDState_Type.__name__ = "Integer32"
_WfCSMACDState_Object = MibTableColumn
wfCSMACDState = _WfCSMACDState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 3),
    _WfCSMACDState_Type()
)
wfCSMACDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDState.setStatus("mandatory")


class _WfCSMACDSlot_Type(Integer32):
    """Custom type wfCSMACDSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfCSMACDSlot_Type.__name__ = "Integer32"
_WfCSMACDSlot_Object = MibTableColumn
wfCSMACDSlot = _WfCSMACDSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 4),
    _WfCSMACDSlot_Type()
)
wfCSMACDSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDSlot.setStatus("mandatory")


class _WfCSMACDConnector_Type(Integer32):
    """Custom type wfCSMACDConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44),
    )


_WfCSMACDConnector_Type.__name__ = "Integer32"
_WfCSMACDConnector_Object = MibTableColumn
wfCSMACDConnector = _WfCSMACDConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 5),
    _WfCSMACDConnector_Type()
)
wfCSMACDConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDConnector.setStatus("mandatory")


class _WfCSMACDCct_Type(Integer32):
    """Custom type wfCSMACDCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfCSMACDCct_Type.__name__ = "Integer32"
_WfCSMACDCct_Object = MibTableColumn
wfCSMACDCct = _WfCSMACDCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 6),
    _WfCSMACDCct_Type()
)
wfCSMACDCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDCct.setStatus("mandatory")


class _WfCSMACDBofl_Type(Integer32):
    """Custom type wfCSMACDBofl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfCSMACDBofl_Type.__name__ = "Integer32"
_WfCSMACDBofl_Object = MibTableColumn
wfCSMACDBofl = _WfCSMACDBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 7),
    _WfCSMACDBofl_Type()
)
wfCSMACDBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDBofl.setStatus("mandatory")


class _WfCSMACDBoflTmo_Type(Integer32):
    """Custom type wfCSMACDBoflTmo based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_WfCSMACDBoflTmo_Type.__name__ = "Integer32"
_WfCSMACDBoflTmo_Object = MibTableColumn
wfCSMACDBoflTmo = _WfCSMACDBoflTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 8),
    _WfCSMACDBoflTmo_Type()
)
wfCSMACDBoflTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDBoflTmo.setStatus("mandatory")


class _WfCSMACDMtu_Type(Integer32):
    """Custom type wfCSMACDMtu based on Integer32"""
    defaultValue = 1518

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1518
        )
    )
    namedValues = NamedValues(
        ("default", 1518)
    )


_WfCSMACDMtu_Type.__name__ = "Integer32"
_WfCSMACDMtu_Object = MibTableColumn
wfCSMACDMtu = _WfCSMACDMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 9),
    _WfCSMACDMtu_Type()
)
wfCSMACDMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDMtu.setStatus("mandatory")
_WfCSMACDMadr_Type = OctetString
_WfCSMACDMadr_Object = MibTableColumn
wfCSMACDMadr = _WfCSMACDMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 10),
    _WfCSMACDMadr_Type()
)
wfCSMACDMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDMadr.setStatus("mandatory")
_WfCSMACDOctetsRxOk_Type = Counter32
_WfCSMACDOctetsRxOk_Object = MibTableColumn
wfCSMACDOctetsRxOk = _WfCSMACDOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 11),
    _WfCSMACDOctetsRxOk_Type()
)
wfCSMACDOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDOctetsRxOk.setStatus("mandatory")
_WfCSMACDFramesRxOk_Type = Counter32
_WfCSMACDFramesRxOk_Object = MibTableColumn
wfCSMACDFramesRxOk = _WfCSMACDFramesRxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 12),
    _WfCSMACDFramesRxOk_Type()
)
wfCSMACDFramesRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDFramesRxOk.setStatus("mandatory")
_WfCSMACDOctetsTxOk_Type = Counter32
_WfCSMACDOctetsTxOk_Object = MibTableColumn
wfCSMACDOctetsTxOk = _WfCSMACDOctetsTxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 13),
    _WfCSMACDOctetsTxOk_Type()
)
wfCSMACDOctetsTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDOctetsTxOk.setStatus("mandatory")
_WfCSMACDFramesTxOk_Type = Counter32
_WfCSMACDFramesTxOk_Object = MibTableColumn
wfCSMACDFramesTxOk = _WfCSMACDFramesTxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 14),
    _WfCSMACDFramesTxOk_Type()
)
wfCSMACDFramesTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDFramesTxOk.setStatus("mandatory")
_WfCSMACDDeferredTx_Type = Counter32
_WfCSMACDDeferredTx_Object = MibTableColumn
wfCSMACDDeferredTx = _WfCSMACDDeferredTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 15),
    _WfCSMACDDeferredTx_Type()
)
wfCSMACDDeferredTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDDeferredTx.setStatus("mandatory")
_WfCSMACDLateCollnTx_Type = Counter32
_WfCSMACDLateCollnTx_Object = MibTableColumn
wfCSMACDLateCollnTx = _WfCSMACDLateCollnTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 16),
    _WfCSMACDLateCollnTx_Type()
)
wfCSMACDLateCollnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDLateCollnTx.setStatus("mandatory")
_WfCSMACDExcessvCollnTx_Type = Counter32
_WfCSMACDExcessvCollnTx_Object = MibTableColumn
wfCSMACDExcessvCollnTx = _WfCSMACDExcessvCollnTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 17),
    _WfCSMACDExcessvCollnTx_Type()
)
wfCSMACDExcessvCollnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDExcessvCollnTx.setStatus("mandatory")
_WfCSMACDBablErrorTx_Type = Counter32
_WfCSMACDBablErrorTx_Object = MibTableColumn
wfCSMACDBablErrorTx = _WfCSMACDBablErrorTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 18),
    _WfCSMACDBablErrorTx_Type()
)
wfCSMACDBablErrorTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDBablErrorTx.setStatus("mandatory")
_WfCSMACDBufErrorTx_Type = Counter32
_WfCSMACDBufErrorTx_Object = MibTableColumn
wfCSMACDBufErrorTx = _WfCSMACDBufErrorTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 19),
    _WfCSMACDBufErrorTx_Type()
)
wfCSMACDBufErrorTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDBufErrorTx.setStatus("mandatory")
_WfCSMACDLcarTx_Type = Counter32
_WfCSMACDLcarTx_Object = MibTableColumn
wfCSMACDLcarTx = _WfCSMACDLcarTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 20),
    _WfCSMACDLcarTx_Type()
)
wfCSMACDLcarTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDLcarTx.setStatus("mandatory")
_WfCSMACDUfloTx_Type = Counter32
_WfCSMACDUfloTx_Object = MibTableColumn
wfCSMACDUfloTx = _WfCSMACDUfloTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 21),
    _WfCSMACDUfloTx_Type()
)
wfCSMACDUfloTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDUfloTx.setStatus("mandatory")
_WfCSMACDFcsErrorRx_Type = Counter32
_WfCSMACDFcsErrorRx_Object = MibTableColumn
wfCSMACDFcsErrorRx = _WfCSMACDFcsErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 22),
    _WfCSMACDFcsErrorRx_Type()
)
wfCSMACDFcsErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDFcsErrorRx.setStatus("mandatory")
_WfCSMACDAlignErrorRx_Type = Counter32
_WfCSMACDAlignErrorRx_Object = MibTableColumn
wfCSMACDAlignErrorRx = _WfCSMACDAlignErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 23),
    _WfCSMACDAlignErrorRx_Type()
)
wfCSMACDAlignErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDAlignErrorRx.setStatus("mandatory")
_WfCSMACDLackRescErrorRx_Type = Counter32
_WfCSMACDLackRescErrorRx_Object = MibTableColumn
wfCSMACDLackRescErrorRx = _WfCSMACDLackRescErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 24),
    _WfCSMACDLackRescErrorRx_Type()
)
wfCSMACDLackRescErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDLackRescErrorRx.setStatus("mandatory")
_WfCSMACDTooLongErrorRx_Type = Counter32
_WfCSMACDTooLongErrorRx_Object = MibTableColumn
wfCSMACDTooLongErrorRx = _WfCSMACDTooLongErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 25),
    _WfCSMACDTooLongErrorRx_Type()
)
wfCSMACDTooLongErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDTooLongErrorRx.setStatus("mandatory")
_WfCSMACDOfloRx_Type = Counter32
_WfCSMACDOfloRx_Object = MibTableColumn
wfCSMACDOfloRx = _WfCSMACDOfloRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 26),
    _WfCSMACDOfloRx_Type()
)
wfCSMACDOfloRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDOfloRx.setStatus("mandatory")
_WfCSMACDMerr_Type = Counter32
_WfCSMACDMerr_Object = MibTableColumn
wfCSMACDMerr = _WfCSMACDMerr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 27),
    _WfCSMACDMerr_Type()
)
wfCSMACDMerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDMerr.setStatus("mandatory")
_WfCSMACDCerr_Type = Counter32
_WfCSMACDCerr_Object = MibTableColumn
wfCSMACDCerr = _WfCSMACDCerr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 28),
    _WfCSMACDCerr_Type()
)
wfCSMACDCerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDCerr.setStatus("mandatory")


class _WfCSMACDHardwareFilter_Type(Integer32):
    """Custom type wfCSMACDHardwareFilter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfCSMACDHardwareFilter_Type.__name__ = "Integer32"
_WfCSMACDHardwareFilter_Object = MibTableColumn
wfCSMACDHardwareFilter = _WfCSMACDHardwareFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 29),
    _WfCSMACDHardwareFilter_Type()
)
wfCSMACDHardwareFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDHardwareFilter.setStatus("mandatory")
_WfCSMACDTxQueueLength_Type = Integer32
_WfCSMACDTxQueueLength_Object = MibTableColumn
wfCSMACDTxQueueLength = _WfCSMACDTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 30),
    _WfCSMACDTxQueueLength_Type()
)
wfCSMACDTxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDTxQueueLength.setStatus("mandatory")
_WfCSMACDRxQueueLength_Type = Integer32
_WfCSMACDRxQueueLength_Object = MibTableColumn
wfCSMACDRxQueueLength = _WfCSMACDRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 31),
    _WfCSMACDRxQueueLength_Type()
)
wfCSMACDRxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDRxQueueLength.setStatus("mandatory")
_WfCSMACDTxClipFrames_Type = Counter32
_WfCSMACDTxClipFrames_Object = MibTableColumn
wfCSMACDTxClipFrames = _WfCSMACDTxClipFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 32),
    _WfCSMACDTxClipFrames_Type()
)
wfCSMACDTxClipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDTxClipFrames.setStatus("mandatory")
_WfCSMACDRxReplenMisses_Type = Counter32
_WfCSMACDRxReplenMisses_Object = MibTableColumn
wfCSMACDRxReplenMisses = _WfCSMACDRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 33),
    _WfCSMACDRxReplenMisses_Type()
)
wfCSMACDRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDRxReplenMisses.setStatus("mandatory")


class _WfCSMACDCfgTxQueueLength_Type(Integer32):
    """Custom type wfCSMACDCfgTxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfCSMACDCfgTxQueueLength_Type.__name__ = "Integer32"
_WfCSMACDCfgTxQueueLength_Object = MibTableColumn
wfCSMACDCfgTxQueueLength = _WfCSMACDCfgTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 34),
    _WfCSMACDCfgTxQueueLength_Type()
)
wfCSMACDCfgTxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDCfgTxQueueLength.setStatus("mandatory")


class _WfCSMACDCfgRxQueueLength_Type(Integer32):
    """Custom type wfCSMACDCfgRxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfCSMACDCfgRxQueueLength_Type.__name__ = "Integer32"
_WfCSMACDCfgRxQueueLength_Object = MibTableColumn
wfCSMACDCfgRxQueueLength = _WfCSMACDCfgRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 35),
    _WfCSMACDCfgRxQueueLength_Type()
)
wfCSMACDCfgRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDCfgRxQueueLength.setStatus("mandatory")


class _WfCSMACDAlignmentMode_Type(Integer32):
    """Custom type wfCSMACDAlignmentMode based on Integer32"""
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
        *(("all", 1),
          ("bytes", 2),
          ("disabled", 3))
    )


_WfCSMACDAlignmentMode_Type.__name__ = "Integer32"
_WfCSMACDAlignmentMode_Object = MibTableColumn
wfCSMACDAlignmentMode = _WfCSMACDAlignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 36),
    _WfCSMACDAlignmentMode_Type()
)
wfCSMACDAlignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDAlignmentMode.setStatus("mandatory")
_WfCSMACDUnAlignedFrames_Type = Counter32
_WfCSMACDUnAlignedFrames_Object = MibTableColumn
wfCSMACDUnAlignedFrames = _WfCSMACDUnAlignedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 37),
    _WfCSMACDUnAlignedFrames_Type()
)
wfCSMACDUnAlignedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDUnAlignedFrames.setStatus("mandatory")
_WfCSMACDLineNumber_Type = Integer32
_WfCSMACDLineNumber_Object = MibTableColumn
wfCSMACDLineNumber = _WfCSMACDLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 38),
    _WfCSMACDLineNumber_Type()
)
wfCSMACDLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDLineNumber.setStatus("mandatory")
_WfCSMACDLateCollnRx_Type = Counter32
_WfCSMACDLateCollnRx_Object = MibTableColumn
wfCSMACDLateCollnRx = _WfCSMACDLateCollnRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 39),
    _WfCSMACDLateCollnRx_Type()
)
wfCSMACDLateCollnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDLateCollnRx.setStatus("mandatory")


class _WfCSMACDModule_Type(Integer32):
    """Custom type wfCSMACDModule based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfCSMACDModule_Type.__name__ = "Integer32"
_WfCSMACDModule_Object = MibTableColumn
wfCSMACDModule = _WfCSMACDModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 40),
    _WfCSMACDModule_Type()
)
wfCSMACDModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDModule.setStatus("mandatory")


class _WfCSMACDActualConnector_Type(Integer32):
    """Custom type wfCSMACDActualConnector based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfCSMACDActualConnector_Type.__name__ = "Integer32"
_WfCSMACDActualConnector_Object = MibTableColumn
wfCSMACDActualConnector = _WfCSMACDActualConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 41),
    _WfCSMACDActualConnector_Type()
)
wfCSMACDActualConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDActualConnector.setStatus("mandatory")
_WfCSMACDLastChange_Type = TimeTicks
_WfCSMACDLastChange_Object = MibTableColumn
wfCSMACDLastChange = _WfCSMACDLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 42),
    _WfCSMACDLastChange_Type()
)
wfCSMACDLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDLastChange.setStatus("mandatory")
_WfCSMACDOutQLen_Type = Gauge32
_WfCSMACDOutQLen_Object = MibTableColumn
wfCSMACDOutQLen = _WfCSMACDOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 43),
    _WfCSMACDOutQLen_Type()
)
wfCSMACDOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDOutQLen.setStatus("mandatory")
_WfCSMACDIntProcessings_Type = Counter32
_WfCSMACDIntProcessings_Object = MibTableColumn
wfCSMACDIntProcessings = _WfCSMACDIntProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 44),
    _WfCSMACDIntProcessings_Type()
)
wfCSMACDIntProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDIntProcessings.setStatus("mandatory")
_WfCSMACDTxProcessings_Type = Counter32
_WfCSMACDTxProcessings_Object = MibTableColumn
wfCSMACDTxProcessings = _WfCSMACDTxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 45),
    _WfCSMACDTxProcessings_Type()
)
wfCSMACDTxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDTxProcessings.setStatus("mandatory")
_WfCSMACDRxProcessings_Type = Counter32
_WfCSMACDRxProcessings_Object = MibTableColumn
wfCSMACDRxProcessings = _WfCSMACDRxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 46),
    _WfCSMACDRxProcessings_Type()
)
wfCSMACDRxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDRxProcessings.setStatus("mandatory")
_WfCSMACDTxCmplProcessings_Type = Counter32
_WfCSMACDTxCmplProcessings_Object = MibTableColumn
wfCSMACDTxCmplProcessings = _WfCSMACDTxCmplProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 47),
    _WfCSMACDTxCmplProcessings_Type()
)
wfCSMACDTxCmplProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDTxCmplProcessings.setStatus("mandatory")
_WfCSMACDTxQueueReductions_Type = Counter32
_WfCSMACDTxQueueReductions_Object = MibTableColumn
wfCSMACDTxQueueReductions = _WfCSMACDTxQueueReductions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 48),
    _WfCSMACDTxQueueReductions_Type()
)
wfCSMACDTxQueueReductions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDTxQueueReductions.setStatus("mandatory")
_WfCSMACDSingleCollisionFrames_Type = Counter32
_WfCSMACDSingleCollisionFrames_Object = MibTableColumn
wfCSMACDSingleCollisionFrames = _WfCSMACDSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 49),
    _WfCSMACDSingleCollisionFrames_Type()
)
wfCSMACDSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDSingleCollisionFrames.setStatus("mandatory")
_WfCSMACDMultipleCollisionFrames_Type = Counter32
_WfCSMACDMultipleCollisionFrames_Object = MibTableColumn
wfCSMACDMultipleCollisionFrames = _WfCSMACDMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 50),
    _WfCSMACDMultipleCollisionFrames_Type()
)
wfCSMACDMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDMultipleCollisionFrames.setStatus("mandatory")
_WfCSMACDInternalMacTxErrors_Type = Counter32
_WfCSMACDInternalMacTxErrors_Object = MibTableColumn
wfCSMACDInternalMacTxErrors = _WfCSMACDInternalMacTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 51),
    _WfCSMACDInternalMacTxErrors_Type()
)
wfCSMACDInternalMacTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDInternalMacTxErrors.setStatus("mandatory")


class _WfCSMACDLineCapability_Type(Integer32):
    """Custom type wfCSMACDLineCapability based on Integer32"""
    defaultValue = 1

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
        *(("gigabitduplex", 8),
          ("gigabitduplexflowctrl", 9),
          ("hundredbaset4", 5),
          ("hundredbasetx", 3),
          ("hundredbasetxduplex", 4),
          ("hundredbasetxduplexcongctrl", 7),
          ("tenbaset", 1),
          ("tenbasetduplex", 2),
          ("tenbasetduplexcongctrl", 6))
    )


_WfCSMACDLineCapability_Type.__name__ = "Integer32"
_WfCSMACDLineCapability_Object = MibTableColumn
wfCSMACDLineCapability = _WfCSMACDLineCapability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 52),
    _WfCSMACDLineCapability_Type()
)
wfCSMACDLineCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDLineCapability.setStatus("mandatory")
_WfCSMACDEtherChipSet_Type = ObjectIdentifier
_WfCSMACDEtherChipSet_Object = MibTableColumn
wfCSMACDEtherChipSet = _WfCSMACDEtherChipSet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 53),
    _WfCSMACDEtherChipSet_Type()
)
wfCSMACDEtherChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDEtherChipSet.setStatus("mandatory")
_WfCSMACDRxSymbolErrors_Type = Counter32
_WfCSMACDRxSymbolErrors_Object = MibTableColumn
wfCSMACDRxSymbolErrors = _WfCSMACDRxSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 54),
    _WfCSMACDRxSymbolErrors_Type()
)
wfCSMACDRxSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDRxSymbolErrors.setStatus("mandatory")
_WfCSMACDInternalMacRxErrors_Type = Counter32
_WfCSMACDInternalMacRxErrors_Object = MibTableColumn
wfCSMACDInternalMacRxErrors = _WfCSMACDInternalMacRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 55),
    _WfCSMACDInternalMacRxErrors_Type()
)
wfCSMACDInternalMacRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDInternalMacRxErrors.setStatus("mandatory")


class _WfCSMACDConfigurableSpeed_Type(Integer32):
    """Custom type wfCSMACDConfigurableSpeed based on Integer32"""
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


_WfCSMACDConfigurableSpeed_Type.__name__ = "Integer32"
_WfCSMACDConfigurableSpeed_Object = MibTableColumn
wfCSMACDConfigurableSpeed = _WfCSMACDConfigurableSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 56),
    _WfCSMACDConfigurableSpeed_Type()
)
wfCSMACDConfigurableSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDConfigurableSpeed.setStatus("mandatory")
_WfCSMACDRxFlushes_Type = Counter32
_WfCSMACDRxFlushes_Object = MibTableColumn
wfCSMACDRxFlushes = _WfCSMACDRxFlushes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 57),
    _WfCSMACDRxFlushes_Type()
)
wfCSMACDRxFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDRxFlushes.setStatus("mandatory")
_WfCSMACDTxDeadlocks_Type = Counter32
_WfCSMACDTxDeadlocks_Object = MibTableColumn
wfCSMACDTxDeadlocks = _WfCSMACDTxDeadlocks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 58),
    _WfCSMACDTxDeadlocks_Type()
)
wfCSMACDTxDeadlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDTxDeadlocks.setStatus("mandatory")


class _WfCSMACDBoflRetries_Type(Integer32):
    """Custom type wfCSMACDBoflRetries based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfCSMACDBoflRetries_Type.__name__ = "Integer32"
_WfCSMACDBoflRetries_Object = MibTableColumn
wfCSMACDBoflRetries = _WfCSMACDBoflRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 59),
    _WfCSMACDBoflRetries_Type()
)
wfCSMACDBoflRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDBoflRetries.setStatus("mandatory")


class _WfCSMACDBoflTmoDivisor_Type(Integer32):
    """Custom type wfCSMACDBoflTmoDivisor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfCSMACDBoflTmoDivisor_Type.__name__ = "Integer32"
_WfCSMACDBoflTmoDivisor_Object = MibTableColumn
wfCSMACDBoflTmoDivisor = _WfCSMACDBoflTmoDivisor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 60),
    _WfCSMACDBoflTmoDivisor_Type()
)
wfCSMACDBoflTmoDivisor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDBoflTmoDivisor.setStatus("mandatory")


class _WfCSMACDTurboBoflDebug_Type(Integer32):
    """Custom type wfCSMACDTurboBoflDebug based on Integer32"""
    defaultValue = 0


_WfCSMACDTurboBoflDebug_Object = MibTableColumn
wfCSMACDTurboBoflDebug = _WfCSMACDTurboBoflDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 61),
    _WfCSMACDTurboBoflDebug_Type()
)
wfCSMACDTurboBoflDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDTurboBoflDebug.setStatus("mandatory")
_WfCSMACDIfIndex_Type = Integer32
_WfCSMACDIfIndex_Object = MibTableColumn
wfCSMACDIfIndex = _WfCSMACDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 62),
    _WfCSMACDIfIndex_Type()
)
wfCSMACDIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDIfIndex.setStatus("mandatory")
_WfCSMACDTxFlowControlPauseFrames_Type = Counter32
_WfCSMACDTxFlowControlPauseFrames_Object = MibTableColumn
wfCSMACDTxFlowControlPauseFrames = _WfCSMACDTxFlowControlPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 63),
    _WfCSMACDTxFlowControlPauseFrames_Type()
)
wfCSMACDTxFlowControlPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDTxFlowControlPauseFrames.setStatus("mandatory")
_WfCSMACDRxFlowControlPauseFrames_Type = Counter32
_WfCSMACDRxFlowControlPauseFrames_Object = MibTableColumn
wfCSMACDRxFlowControlPauseFrames = _WfCSMACDRxFlowControlPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 64),
    _WfCSMACDRxFlowControlPauseFrames_Type()
)
wfCSMACDRxFlowControlPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDRxFlowControlPauseFrames.setStatus("mandatory")
_WfCSMACDRxUnsupportedOpcodes_Type = Counter32
_WfCSMACDRxUnsupportedOpcodes_Object = MibTableColumn
wfCSMACDRxUnsupportedOpcodes = _WfCSMACDRxUnsupportedOpcodes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 65),
    _WfCSMACDRxUnsupportedOpcodes_Type()
)
wfCSMACDRxUnsupportedOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDRxUnsupportedOpcodes.setStatus("mandatory")


class _WfCSMACDFlowControlEnable_Type(Integer32):
    """Custom type wfCSMACDFlowControlEnable based on Integer32"""
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


_WfCSMACDFlowControlEnable_Type.__name__ = "Integer32"
_WfCSMACDFlowControlEnable_Object = MibTableColumn
wfCSMACDFlowControlEnable = _WfCSMACDFlowControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 66),
    _WfCSMACDFlowControlEnable_Type()
)
wfCSMACDFlowControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDFlowControlEnable.setStatus("mandatory")


class _WfCSMACDTxFlowControlPauseTime_Type(Integer32):
    """Custom type wfCSMACDTxFlowControlPauseTime based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfCSMACDTxFlowControlPauseTime_Type.__name__ = "Integer32"
_WfCSMACDTxFlowControlPauseTime_Object = MibTableColumn
wfCSMACDTxFlowControlPauseTime = _WfCSMACDTxFlowControlPauseTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 67),
    _WfCSMACDTxFlowControlPauseTime_Type()
)
wfCSMACDTxFlowControlPauseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDTxFlowControlPauseTime.setStatus("mandatory")


class _WfCSMACDTxFlowControlPauseZeroEnable_Type(Integer32):
    """Custom type wfCSMACDTxFlowControlPauseZeroEnable based on Integer32"""
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


_WfCSMACDTxFlowControlPauseZeroEnable_Type.__name__ = "Integer32"
_WfCSMACDTxFlowControlPauseZeroEnable_Object = MibTableColumn
wfCSMACDTxFlowControlPauseZeroEnable = _WfCSMACDTxFlowControlPauseZeroEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 68),
    _WfCSMACDTxFlowControlPauseZeroEnable_Type()
)
wfCSMACDTxFlowControlPauseZeroEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDTxFlowControlPauseZeroEnable.setStatus("mandatory")


class _WfCSMACDDsqmsLineSpeed_Type(Integer32):
    """Custom type wfCSMACDDsqmsLineSpeed based on Integer32"""
    defaultValue = 1250000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000000),
    )


_WfCSMACDDsqmsLineSpeed_Type.__name__ = "Integer32"
_WfCSMACDDsqmsLineSpeed_Object = MibTableColumn
wfCSMACDDsqmsLineSpeed = _WfCSMACDDsqmsLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 1, 1, 69),
    _WfCSMACDDsqmsLineSpeed_Type()
)
wfCSMACDDsqmsLineSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDDsqmsLineSpeed.setStatus("mandatory")
_WfCSMACDAutoNegTable_Object = MibTable
wfCSMACDAutoNegTable = _WfCSMACDAutoNegTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1)
)
if mibBuilder.loadTexts:
    wfCSMACDAutoNegTable.setStatus("mandatory")
_WfCSMACDAutoNegEntry_Object = MibTableRow
wfCSMACDAutoNegEntry = _WfCSMACDAutoNegEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1, 1)
)
wfCSMACDAutoNegEntry.setIndexNames(
    (0, "Wellfleet-CSMACD-MIB", "wfCSMACDAutoNegSlot"),
    (0, "Wellfleet-CSMACD-MIB", "wfCSMACDAutoNegConnector"),
)
if mibBuilder.loadTexts:
    wfCSMACDAutoNegEntry.setStatus("mandatory")


class _WfCSMACDAutoNegDelete_Type(Integer32):
    """Custom type wfCSMACDAutoNegDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfCSMACDAutoNegDelete_Type.__name__ = "Integer32"
_WfCSMACDAutoNegDelete_Object = MibTableColumn
wfCSMACDAutoNegDelete = _WfCSMACDAutoNegDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1, 1, 1),
    _WfCSMACDAutoNegDelete_Type()
)
wfCSMACDAutoNegDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDAutoNegDelete.setStatus("mandatory")


class _WfCSMACDAutoNegSlot_Type(Integer32):
    """Custom type wfCSMACDAutoNegSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfCSMACDAutoNegSlot_Type.__name__ = "Integer32"
_WfCSMACDAutoNegSlot_Object = MibTableColumn
wfCSMACDAutoNegSlot = _WfCSMACDAutoNegSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1, 1, 2),
    _WfCSMACDAutoNegSlot_Type()
)
wfCSMACDAutoNegSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDAutoNegSlot.setStatus("mandatory")


class _WfCSMACDAutoNegConnector_Type(Integer32):
    """Custom type wfCSMACDAutoNegConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44),
    )


_WfCSMACDAutoNegConnector_Type.__name__ = "Integer32"
_WfCSMACDAutoNegConnector_Object = MibTableColumn
wfCSMACDAutoNegConnector = _WfCSMACDAutoNegConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1, 1, 3),
    _WfCSMACDAutoNegConnector_Type()
)
wfCSMACDAutoNegConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDAutoNegConnector.setStatus("mandatory")


class _WfCSMACDAutoNegSpeedSelect_Type(Integer32):
    """Custom type wfCSMACDAutoNegSpeedSelect based on Integer32"""
    defaultValue = 4

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
              13)
        )
    )
    namedValues = NamedValues(
        *(("gigabitduplex", 12),
          ("gigabitduplexflowctrl", 13),
          ("hundredbaset4", 6),
          ("hundredbasetx", 4),
          ("hundredbasetxduplex", 5),
          ("hundredbasetxduplexcongctrl", 11),
          ("macloopback", 7),
          ("nway", 1),
          ("phyloopback", 8),
          ("tenbaset", 2),
          ("tenbasetduplex", 3),
          ("tenbasetduplexcongctrl", 10),
          ("twisterloopback", 9))
    )


_WfCSMACDAutoNegSpeedSelect_Type.__name__ = "Integer32"
_WfCSMACDAutoNegSpeedSelect_Object = MibTableColumn
wfCSMACDAutoNegSpeedSelect = _WfCSMACDAutoNegSpeedSelect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1, 1, 4),
    _WfCSMACDAutoNegSpeedSelect_Type()
)
wfCSMACDAutoNegSpeedSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDAutoNegSpeedSelect.setStatus("mandatory")


class _WfCSMACDAutoNegRemoteSignaling_Type(Integer32):
    """Custom type wfCSMACDAutoNegRemoteSignaling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("notdetected", 2))
    )


_WfCSMACDAutoNegRemoteSignaling_Type.__name__ = "Integer32"
_WfCSMACDAutoNegRemoteSignaling_Object = MibTableColumn
wfCSMACDAutoNegRemoteSignaling = _WfCSMACDAutoNegRemoteSignaling_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1, 1, 5),
    _WfCSMACDAutoNegRemoteSignaling_Type()
)
wfCSMACDAutoNegRemoteSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDAutoNegRemoteSignaling.setStatus("mandatory")


class _WfCSMACDAutoNegState_Type(Integer32):
    """Custom type wfCSMACDAutoNegState based on Integer32"""
    defaultValue = 1

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
        *(("complete", 3),
          ("configuring", 2),
          ("disabled", 1),
          ("paralleldetectfail", 4))
    )


_WfCSMACDAutoNegState_Type.__name__ = "Integer32"
_WfCSMACDAutoNegState_Object = MibTableColumn
wfCSMACDAutoNegState = _WfCSMACDAutoNegState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1, 1, 6),
    _WfCSMACDAutoNegState_Type()
)
wfCSMACDAutoNegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDAutoNegState.setStatus("mandatory")
_WfCSMACDAutoNegRestartAutoConfig_Type = Integer32
_WfCSMACDAutoNegRestartAutoConfig_Object = MibTableColumn
wfCSMACDAutoNegRestartAutoConfig = _WfCSMACDAutoNegRestartAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1, 1, 7),
    _WfCSMACDAutoNegRestartAutoConfig_Type()
)
wfCSMACDAutoNegRestartAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDAutoNegRestartAutoConfig.setStatus("mandatory")
_WfCSMACDAutoNegLocalCapability_Type = Gauge32
_WfCSMACDAutoNegLocalCapability_Object = MibTableColumn
wfCSMACDAutoNegLocalCapability = _WfCSMACDAutoNegLocalCapability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1, 1, 8),
    _WfCSMACDAutoNegLocalCapability_Type()
)
wfCSMACDAutoNegLocalCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDAutoNegLocalCapability.setStatus("mandatory")
_WfCSMACDAutoNegAdvertisedCapability_Type = Gauge32
_WfCSMACDAutoNegAdvertisedCapability_Object = MibTableColumn
wfCSMACDAutoNegAdvertisedCapability = _WfCSMACDAutoNegAdvertisedCapability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1, 1, 9),
    _WfCSMACDAutoNegAdvertisedCapability_Type()
)
wfCSMACDAutoNegAdvertisedCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCSMACDAutoNegAdvertisedCapability.setStatus("mandatory")
_WfCSMACDAutoNegReceivedCapability_Type = Gauge32
_WfCSMACDAutoNegReceivedCapability_Object = MibTableColumn
wfCSMACDAutoNegReceivedCapability = _WfCSMACDAutoNegReceivedCapability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 16, 1, 1, 10),
    _WfCSMACDAutoNegReceivedCapability_Type()
)
wfCSMACDAutoNegReceivedCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCSMACDAutoNegReceivedCapability.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-CSMACD-MIB",
    **{"wfCSMACDTable": wfCSMACDTable,
       "wfCSMACDEntry": wfCSMACDEntry,
       "wfCSMACDDelete": wfCSMACDDelete,
       "wfCSMACDEnable": wfCSMACDEnable,
       "wfCSMACDState": wfCSMACDState,
       "wfCSMACDSlot": wfCSMACDSlot,
       "wfCSMACDConnector": wfCSMACDConnector,
       "wfCSMACDCct": wfCSMACDCct,
       "wfCSMACDBofl": wfCSMACDBofl,
       "wfCSMACDBoflTmo": wfCSMACDBoflTmo,
       "wfCSMACDMtu": wfCSMACDMtu,
       "wfCSMACDMadr": wfCSMACDMadr,
       "wfCSMACDOctetsRxOk": wfCSMACDOctetsRxOk,
       "wfCSMACDFramesRxOk": wfCSMACDFramesRxOk,
       "wfCSMACDOctetsTxOk": wfCSMACDOctetsTxOk,
       "wfCSMACDFramesTxOk": wfCSMACDFramesTxOk,
       "wfCSMACDDeferredTx": wfCSMACDDeferredTx,
       "wfCSMACDLateCollnTx": wfCSMACDLateCollnTx,
       "wfCSMACDExcessvCollnTx": wfCSMACDExcessvCollnTx,
       "wfCSMACDBablErrorTx": wfCSMACDBablErrorTx,
       "wfCSMACDBufErrorTx": wfCSMACDBufErrorTx,
       "wfCSMACDLcarTx": wfCSMACDLcarTx,
       "wfCSMACDUfloTx": wfCSMACDUfloTx,
       "wfCSMACDFcsErrorRx": wfCSMACDFcsErrorRx,
       "wfCSMACDAlignErrorRx": wfCSMACDAlignErrorRx,
       "wfCSMACDLackRescErrorRx": wfCSMACDLackRescErrorRx,
       "wfCSMACDTooLongErrorRx": wfCSMACDTooLongErrorRx,
       "wfCSMACDOfloRx": wfCSMACDOfloRx,
       "wfCSMACDMerr": wfCSMACDMerr,
       "wfCSMACDCerr": wfCSMACDCerr,
       "wfCSMACDHardwareFilter": wfCSMACDHardwareFilter,
       "wfCSMACDTxQueueLength": wfCSMACDTxQueueLength,
       "wfCSMACDRxQueueLength": wfCSMACDRxQueueLength,
       "wfCSMACDTxClipFrames": wfCSMACDTxClipFrames,
       "wfCSMACDRxReplenMisses": wfCSMACDRxReplenMisses,
       "wfCSMACDCfgTxQueueLength": wfCSMACDCfgTxQueueLength,
       "wfCSMACDCfgRxQueueLength": wfCSMACDCfgRxQueueLength,
       "wfCSMACDAlignmentMode": wfCSMACDAlignmentMode,
       "wfCSMACDUnAlignedFrames": wfCSMACDUnAlignedFrames,
       "wfCSMACDLineNumber": wfCSMACDLineNumber,
       "wfCSMACDLateCollnRx": wfCSMACDLateCollnRx,
       "wfCSMACDModule": wfCSMACDModule,
       "wfCSMACDActualConnector": wfCSMACDActualConnector,
       "wfCSMACDLastChange": wfCSMACDLastChange,
       "wfCSMACDOutQLen": wfCSMACDOutQLen,
       "wfCSMACDIntProcessings": wfCSMACDIntProcessings,
       "wfCSMACDTxProcessings": wfCSMACDTxProcessings,
       "wfCSMACDRxProcessings": wfCSMACDRxProcessings,
       "wfCSMACDTxCmplProcessings": wfCSMACDTxCmplProcessings,
       "wfCSMACDTxQueueReductions": wfCSMACDTxQueueReductions,
       "wfCSMACDSingleCollisionFrames": wfCSMACDSingleCollisionFrames,
       "wfCSMACDMultipleCollisionFrames": wfCSMACDMultipleCollisionFrames,
       "wfCSMACDInternalMacTxErrors": wfCSMACDInternalMacTxErrors,
       "wfCSMACDLineCapability": wfCSMACDLineCapability,
       "wfCSMACDEtherChipSet": wfCSMACDEtherChipSet,
       "wfCSMACDRxSymbolErrors": wfCSMACDRxSymbolErrors,
       "wfCSMACDInternalMacRxErrors": wfCSMACDInternalMacRxErrors,
       "wfCSMACDConfigurableSpeed": wfCSMACDConfigurableSpeed,
       "wfCSMACDRxFlushes": wfCSMACDRxFlushes,
       "wfCSMACDTxDeadlocks": wfCSMACDTxDeadlocks,
       "wfCSMACDBoflRetries": wfCSMACDBoflRetries,
       "wfCSMACDBoflTmoDivisor": wfCSMACDBoflTmoDivisor,
       "wfCSMACDTurboBoflDebug": wfCSMACDTurboBoflDebug,
       "wfCSMACDIfIndex": wfCSMACDIfIndex,
       "wfCSMACDTxFlowControlPauseFrames": wfCSMACDTxFlowControlPauseFrames,
       "wfCSMACDRxFlowControlPauseFrames": wfCSMACDRxFlowControlPauseFrames,
       "wfCSMACDRxUnsupportedOpcodes": wfCSMACDRxUnsupportedOpcodes,
       "wfCSMACDFlowControlEnable": wfCSMACDFlowControlEnable,
       "wfCSMACDTxFlowControlPauseTime": wfCSMACDTxFlowControlPauseTime,
       "wfCSMACDTxFlowControlPauseZeroEnable": wfCSMACDTxFlowControlPauseZeroEnable,
       "wfCSMACDDsqmsLineSpeed": wfCSMACDDsqmsLineSpeed,
       "wfCSMACDAutoNegTable": wfCSMACDAutoNegTable,
       "wfCSMACDAutoNegEntry": wfCSMACDAutoNegEntry,
       "wfCSMACDAutoNegDelete": wfCSMACDAutoNegDelete,
       "wfCSMACDAutoNegSlot": wfCSMACDAutoNegSlot,
       "wfCSMACDAutoNegConnector": wfCSMACDAutoNegConnector,
       "wfCSMACDAutoNegSpeedSelect": wfCSMACDAutoNegSpeedSelect,
       "wfCSMACDAutoNegRemoteSignaling": wfCSMACDAutoNegRemoteSignaling,
       "wfCSMACDAutoNegState": wfCSMACDAutoNegState,
       "wfCSMACDAutoNegRestartAutoConfig": wfCSMACDAutoNegRestartAutoConfig,
       "wfCSMACDAutoNegLocalCapability": wfCSMACDAutoNegLocalCapability,
       "wfCSMACDAutoNegAdvertisedCapability": wfCSMACDAutoNegAdvertisedCapability,
       "wfCSMACDAutoNegReceivedCapability": wfCSMACDAutoNegReceivedCapability}
)

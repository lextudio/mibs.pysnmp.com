# SNMP MIB module (Wellfleet-BISYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-BISYNC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:52 2024
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

(wfBisyncGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfBisyncGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfBisyncTable_Object = MibTable
wfBisyncTable = _WfBisyncTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1)
)
if mibBuilder.loadTexts:
    wfBisyncTable.setStatus("mandatory")
_WfBisyncEntry_Object = MibTableRow
wfBisyncEntry = _WfBisyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1)
)
wfBisyncEntry.setIndexNames(
    (0, "Wellfleet-BISYNC-MIB", "wfBisyncSlot"),
    (0, "Wellfleet-BISYNC-MIB", "wfBisyncConnector"),
)
if mibBuilder.loadTexts:
    wfBisyncEntry.setStatus("mandatory")


class _WfBisyncDelete_Type(Integer32):
    """Custom type wfBisyncDelete based on Integer32"""
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


_WfBisyncDelete_Type.__name__ = "Integer32"
_WfBisyncDelete_Object = MibTableColumn
wfBisyncDelete = _WfBisyncDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 1),
    _WfBisyncDelete_Type()
)
wfBisyncDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncDelete.setStatus("mandatory")


class _WfBisyncDisable_Type(Integer32):
    """Custom type wfBisyncDisable based on Integer32"""
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


_WfBisyncDisable_Type.__name__ = "Integer32"
_WfBisyncDisable_Object = MibTableColumn
wfBisyncDisable = _WfBisyncDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 2),
    _WfBisyncDisable_Type()
)
wfBisyncDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncDisable.setStatus("mandatory")


class _WfBisyncCct_Type(Integer32):
    """Custom type wfBisyncCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfBisyncCct_Type.__name__ = "Integer32"
_WfBisyncCct_Object = MibTableColumn
wfBisyncCct = _WfBisyncCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 3),
    _WfBisyncCct_Type()
)
wfBisyncCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncCct.setStatus("mandatory")


class _WfBisyncMtu_Type(Integer32):
    """Custom type wfBisyncMtu based on Integer32"""
    defaultValue = 1580

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4568),
    )


_WfBisyncMtu_Type.__name__ = "Integer32"
_WfBisyncMtu_Object = MibTableColumn
wfBisyncMtu = _WfBisyncMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 4),
    _WfBisyncMtu_Type()
)
wfBisyncMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncMtu.setStatus("mandatory")


class _WfBisyncMediaType_Type(Integer32):
    """Custom type wfBisyncMediaType based on Integer32"""
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
        *(("default", 1),
          ("raisedtr", 2),
          ("v25bis", 3))
    )


_WfBisyncMediaType_Type.__name__ = "Integer32"
_WfBisyncMediaType_Object = MibTableColumn
wfBisyncMediaType = _WfBisyncMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 5),
    _WfBisyncMediaType_Type()
)
wfBisyncMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncMediaType.setStatus("mandatory")


class _WfBisyncCableType_Type(Integer32):
    """Custom type wfBisyncCableType based on Integer32"""
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
        *(("rs232", 1),
          ("rs422", 2),
          ("v35", 3),
          ("x21", 4))
    )


_WfBisyncCableType_Type.__name__ = "Integer32"
_WfBisyncCableType_Object = MibTableColumn
wfBisyncCableType = _WfBisyncCableType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 6),
    _WfBisyncCableType_Type()
)
wfBisyncCableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncCableType.setStatus("mandatory")


class _WfBisyncClkSource_Type(Integer32):
    """Custom type wfBisyncClkSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_WfBisyncClkSource_Type.__name__ = "Integer32"
_WfBisyncClkSource_Object = MibTableColumn
wfBisyncClkSource = _WfBisyncClkSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 7),
    _WfBisyncClkSource_Type()
)
wfBisyncClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncClkSource.setStatus("mandatory")


class _WfBisyncClkSpeed_Type(Integer32):
    """Custom type wfBisyncClkSpeed based on Integer32"""
    defaultValue = 9615

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2401,
              4807,
              7204,
              9615,
              19230)
        )
    )
    namedValues = NamedValues(
        *(("clk1200b", 1200),
          ("clk19200b", 19230),
          ("clk2400b", 2401),
          ("clk4800b", 4807),
          ("clk7200b", 7204),
          ("clk9600b", 9615))
    )


_WfBisyncClkSpeed_Type.__name__ = "Integer32"
_WfBisyncClkSpeed_Object = MibTableColumn
wfBisyncClkSpeed = _WfBisyncClkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 8),
    _WfBisyncClkSpeed_Type()
)
wfBisyncClkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncClkSpeed.setStatus("mandatory")


class _WfBisyncService_Type(Integer32):
    """Custom type wfBisyncService based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dlsw", 1),
          ("tunneling", 2))
    )


_WfBisyncService_Type.__name__ = "Integer32"
_WfBisyncService_Object = MibTableColumn
wfBisyncService = _WfBisyncService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 9),
    _WfBisyncService_Type()
)
wfBisyncService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncService.setStatus("mandatory")


class _WfBisyncCfgTxQueueLength_Type(Integer32):
    """Custom type wfBisyncCfgTxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfBisyncCfgTxQueueLength_Type.__name__ = "Integer32"
_WfBisyncCfgTxQueueLength_Object = MibTableColumn
wfBisyncCfgTxQueueLength = _WfBisyncCfgTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 10),
    _WfBisyncCfgTxQueueLength_Type()
)
wfBisyncCfgTxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncCfgTxQueueLength.setStatus("mandatory")


class _WfBisyncCfgRxQueueLength_Type(Integer32):
    """Custom type wfBisyncCfgRxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfBisyncCfgRxQueueLength_Type.__name__ = "Integer32"
_WfBisyncCfgRxQueueLength_Object = MibTableColumn
wfBisyncCfgRxQueueLength = _WfBisyncCfgRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 11),
    _WfBisyncCfgRxQueueLength_Type()
)
wfBisyncCfgRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncCfgRxQueueLength.setStatus("mandatory")


class _WfBisyncCharMode_Type(Integer32):
    """Custom type wfBisyncCharMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("ebcdic", 1))
    )


_WfBisyncCharMode_Type.__name__ = "Integer32"
_WfBisyncCharMode_Object = MibTableColumn
wfBisyncCharMode = _WfBisyncCharMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 12),
    _WfBisyncCharMode_Type()
)
wfBisyncCharMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncCharMode.setStatus("mandatory")
_WfBisyncLineNumber_Type = Integer32
_WfBisyncLineNumber_Object = MibTableColumn
wfBisyncLineNumber = _WfBisyncLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 13),
    _WfBisyncLineNumber_Type()
)
wfBisyncLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncLineNumber.setStatus("mandatory")


class _WfBisyncRtsEnable_Type(Integer32):
    """Custom type wfBisyncRtsEnable based on Integer32"""
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


_WfBisyncRtsEnable_Type.__name__ = "Integer32"
_WfBisyncRtsEnable_Object = MibTableColumn
wfBisyncRtsEnable = _WfBisyncRtsEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 14),
    _WfBisyncRtsEnable_Type()
)
wfBisyncRtsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncRtsEnable.setStatus("mandatory")


class _WfBisyncExternalClkSpeed_Type(Integer32):
    """Custom type wfBisyncExternalClkSpeed based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 19200),
    )


_WfBisyncExternalClkSpeed_Type.__name__ = "Integer32"
_WfBisyncExternalClkSpeed_Object = MibTableColumn
wfBisyncExternalClkSpeed = _WfBisyncExternalClkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 15),
    _WfBisyncExternalClkSpeed_Type()
)
wfBisyncExternalClkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncExternalClkSpeed.setStatus("mandatory")


class _WfBisyncModule_Type(Integer32):
    """Custom type wfBisyncModule based on Integer32"""
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


_WfBisyncModule_Type.__name__ = "Integer32"
_WfBisyncModule_Object = MibTableColumn
wfBisyncModule = _WfBisyncModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 16),
    _WfBisyncModule_Type()
)
wfBisyncModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncModule.setStatus("mandatory")


class _WfBisyncActualConnector_Type(Integer32):
    """Custom type wfBisyncActualConnector based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("three", 3),
          ("two", 2))
    )


_WfBisyncActualConnector_Type.__name__ = "Integer32"
_WfBisyncActualConnector_Object = MibTableColumn
wfBisyncActualConnector = _WfBisyncActualConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 17),
    _WfBisyncActualConnector_Type()
)
wfBisyncActualConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncActualConnector.setStatus("mandatory")


class _WfBisyncConnector_Type(Integer32):
    """Custom type wfBisyncConnector based on Integer32"""
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


_WfBisyncConnector_Type.__name__ = "Integer32"
_WfBisyncConnector_Object = MibTableColumn
wfBisyncConnector = _WfBisyncConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 18),
    _WfBisyncConnector_Type()
)
wfBisyncConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncConnector.setStatus("mandatory")
_WfBisyncSlot_Type = Integer32
_WfBisyncSlot_Object = MibTableColumn
wfBisyncSlot = _WfBisyncSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 19),
    _WfBisyncSlot_Type()
)
wfBisyncSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncSlot.setStatus("mandatory")


class _WfBisyncActiveCct_Type(Integer32):
    """Custom type wfBisyncActiveCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfBisyncActiveCct_Type.__name__ = "Integer32"
_WfBisyncActiveCct_Object = MibTableColumn
wfBisyncActiveCct = _WfBisyncActiveCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 20),
    _WfBisyncActiveCct_Type()
)
wfBisyncActiveCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncActiveCct.setStatus("mandatory")


class _WfBisyncState_Type(Integer32):
    """Custom type wfBisyncState based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              20)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("dsrwait", 4),
          ("init", 3),
          ("notpresent", 20),
          ("up", 1))
    )


_WfBisyncState_Type.__name__ = "Integer32"
_WfBisyncState_Object = MibTableColumn
wfBisyncState = _WfBisyncState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 21),
    _WfBisyncState_Type()
)
wfBisyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncState.setStatus("mandatory")


class _WfBisyncLastState_Type(Integer32):
    """Custom type wfBisyncLastState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              20)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("dsrwait", 4),
          ("init", 3),
          ("notpresent", 20),
          ("up", 1))
    )


_WfBisyncLastState_Type.__name__ = "Integer32"
_WfBisyncLastState_Object = MibTableColumn
wfBisyncLastState = _WfBisyncLastState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 22),
    _WfBisyncLastState_Type()
)
wfBisyncLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncLastState.setStatus("mandatory")
_WfBisyncRxOctets_Type = Counter32
_WfBisyncRxOctets_Object = MibTableColumn
wfBisyncRxOctets = _WfBisyncRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 23),
    _WfBisyncRxOctets_Type()
)
wfBisyncRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncRxOctets.setStatus("mandatory")
_WfBisyncTxOctets_Type = Counter32
_WfBisyncTxOctets_Object = MibTableColumn
wfBisyncTxOctets = _WfBisyncTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 24),
    _WfBisyncTxOctets_Type()
)
wfBisyncTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncTxOctets.setStatus("mandatory")
_WfBisyncRxFrames_Type = Counter32
_WfBisyncRxFrames_Object = MibTableColumn
wfBisyncRxFrames = _WfBisyncRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 25),
    _WfBisyncRxFrames_Type()
)
wfBisyncRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncRxFrames.setStatus("mandatory")
_WfBisyncTxFrames_Type = Counter32
_WfBisyncTxFrames_Object = MibTableColumn
wfBisyncTxFrames = _WfBisyncTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 26),
    _WfBisyncTxFrames_Type()
)
wfBisyncTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncTxFrames.setStatus("mandatory")
_WfBisyncRxErrors_Type = Counter32
_WfBisyncRxErrors_Object = MibTableColumn
wfBisyncRxErrors = _WfBisyncRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 27),
    _WfBisyncRxErrors_Type()
)
wfBisyncRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncRxErrors.setStatus("mandatory")
_WfBisyncTxErrors_Type = Counter32
_WfBisyncTxErrors_Object = MibTableColumn
wfBisyncTxErrors = _WfBisyncTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 28),
    _WfBisyncTxErrors_Type()
)
wfBisyncTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncTxErrors.setStatus("mandatory")
_WfBisyncTxLackRescs_Type = Counter32
_WfBisyncTxLackRescs_Object = MibTableColumn
wfBisyncTxLackRescs = _WfBisyncTxLackRescs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 29),
    _WfBisyncTxLackRescs_Type()
)
wfBisyncTxLackRescs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncTxLackRescs.setStatus("mandatory")
_WfBisyncTxUnderFlows_Type = Counter32
_WfBisyncTxUnderFlows_Object = MibTableColumn
wfBisyncTxUnderFlows = _WfBisyncTxUnderFlows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 30),
    _WfBisyncTxUnderFlows_Type()
)
wfBisyncTxUnderFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncTxUnderFlows.setStatus("mandatory")
_WfBisyncRxOverFlows_Type = Counter32
_WfBisyncRxOverFlows_Object = MibTableColumn
wfBisyncRxOverFlows = _WfBisyncRxOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 31),
    _WfBisyncRxOverFlows_Type()
)
wfBisyncRxOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncRxOverFlows.setStatus("mandatory")
_WfBisyncRxBadFrames_Type = Counter32
_WfBisyncRxBadFrames_Object = MibTableColumn
wfBisyncRxBadFrames = _WfBisyncRxBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 32),
    _WfBisyncRxBadFrames_Type()
)
wfBisyncRxBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncRxBadFrames.setStatus("mandatory")
_WfBisyncRxRunts_Type = Counter32
_WfBisyncRxRunts_Object = MibTableColumn
wfBisyncRxRunts = _WfBisyncRxRunts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 33),
    _WfBisyncRxRunts_Type()
)
wfBisyncRxRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncRxRunts.setStatus("mandatory")
_WfBisyncTxQueueLength_Type = Integer32
_WfBisyncTxQueueLength_Object = MibTableColumn
wfBisyncTxQueueLength = _WfBisyncTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 34),
    _WfBisyncTxQueueLength_Type()
)
wfBisyncTxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncTxQueueLength.setStatus("mandatory")
_WfBisyncRxQueueLength_Type = Integer32
_WfBisyncRxQueueLength_Object = MibTableColumn
wfBisyncRxQueueLength = _WfBisyncRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 35),
    _WfBisyncRxQueueLength_Type()
)
wfBisyncRxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncRxQueueLength.setStatus("mandatory")
_WfBisyncRxReplenMisses_Type = Counter32
_WfBisyncRxReplenMisses_Object = MibTableColumn
wfBisyncRxReplenMisses = _WfBisyncRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 36),
    _WfBisyncRxReplenMisses_Type()
)
wfBisyncRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncRxReplenMisses.setStatus("mandatory")
_WfBisyncLastChange_Type = TimeTicks
_WfBisyncLastChange_Object = MibTableColumn
wfBisyncLastChange = _WfBisyncLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 37),
    _WfBisyncLastChange_Type()
)
wfBisyncLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncLastChange.setStatus("mandatory")
_WfBisyncOutQLen_Type = Gauge32
_WfBisyncOutQLen_Object = MibTableColumn
wfBisyncOutQLen = _WfBisyncOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 38),
    _WfBisyncOutQLen_Type()
)
wfBisyncOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncOutQLen.setStatus("mandatory")
_WfBisyncRxLackRescsChar_Type = Counter32
_WfBisyncRxLackRescsChar_Object = MibTableColumn
wfBisyncRxLackRescsChar = _WfBisyncRxLackRescsChar_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 39),
    _WfBisyncRxLackRescsChar_Type()
)
wfBisyncRxLackRescsChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncRxLackRescsChar.setStatus("mandatory")
_WfBisyncIsrBCZero_Type = Counter32
_WfBisyncIsrBCZero_Object = MibTableColumn
wfBisyncIsrBCZero = _WfBisyncIsrBCZero_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 40),
    _WfBisyncIsrBCZero_Type()
)
wfBisyncIsrBCZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncIsrBCZero.setStatus("mandatory")
_WfBisyncIsrBCSix_Type = Counter32
_WfBisyncIsrBCSix_Object = MibTableColumn
wfBisyncIsrBCSix = _WfBisyncIsrBCSix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 41),
    _WfBisyncIsrBCSix_Type()
)
wfBisyncIsrBCSix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncIsrBCSix.setStatus("mandatory")
_WfBisyncIsrBCInvalid_Type = Counter32
_WfBisyncIsrBCInvalid_Object = MibTableColumn
wfBisyncIsrBCInvalid = _WfBisyncIsrBCInvalid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 42),
    _WfBisyncIsrBCInvalid_Type()
)
wfBisyncIsrBCInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncIsrBCInvalid.setStatus("mandatory")
_WfBisyncIsrBCErrors_Type = Counter32
_WfBisyncIsrBCErrors_Object = MibTableColumn
wfBisyncIsrBCErrors = _WfBisyncIsrBCErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 43),
    _WfBisyncIsrBCErrors_Type()
)
wfBisyncIsrBCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncIsrBCErrors.setStatus("mandatory")


class _WfBisyncLocalConnectionState_Type(Integer32):
    """Custom type wfBisyncLocalConnectionState based on Integer32"""
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
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_WfBisyncLocalConnectionState_Type.__name__ = "Integer32"
_WfBisyncLocalConnectionState_Object = MibTableColumn
wfBisyncLocalConnectionState = _WfBisyncLocalConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 44),
    _WfBisyncLocalConnectionState_Type()
)
wfBisyncLocalConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncLocalConnectionState.setStatus("mandatory")


class _WfBisyncRemoteConnectionState_Type(Integer32):
    """Custom type wfBisyncRemoteConnectionState based on Integer32"""
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
        *(("devicestreaming", 3),
          ("down", 2),
          ("unknown", 4),
          ("up", 1))
    )


_WfBisyncRemoteConnectionState_Type.__name__ = "Integer32"
_WfBisyncRemoteConnectionState_Object = MibTableColumn
wfBisyncRemoteConnectionState = _WfBisyncRemoteConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 45),
    _WfBisyncRemoteConnectionState_Type()
)
wfBisyncRemoteConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBisyncRemoteConnectionState.setStatus("mandatory")


class _WfBisyncAdditionalSyncPairs_Type(Integer32):
    """Custom type wfBisyncAdditionalSyncPairs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfBisyncAdditionalSyncPairs_Type.__name__ = "Integer32"
_WfBisyncAdditionalSyncPairs_Object = MibTableColumn
wfBisyncAdditionalSyncPairs = _WfBisyncAdditionalSyncPairs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 27, 1, 1, 46),
    _WfBisyncAdditionalSyncPairs_Type()
)
wfBisyncAdditionalSyncPairs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBisyncAdditionalSyncPairs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-BISYNC-MIB",
    **{"wfBisyncTable": wfBisyncTable,
       "wfBisyncEntry": wfBisyncEntry,
       "wfBisyncDelete": wfBisyncDelete,
       "wfBisyncDisable": wfBisyncDisable,
       "wfBisyncCct": wfBisyncCct,
       "wfBisyncMtu": wfBisyncMtu,
       "wfBisyncMediaType": wfBisyncMediaType,
       "wfBisyncCableType": wfBisyncCableType,
       "wfBisyncClkSource": wfBisyncClkSource,
       "wfBisyncClkSpeed": wfBisyncClkSpeed,
       "wfBisyncService": wfBisyncService,
       "wfBisyncCfgTxQueueLength": wfBisyncCfgTxQueueLength,
       "wfBisyncCfgRxQueueLength": wfBisyncCfgRxQueueLength,
       "wfBisyncCharMode": wfBisyncCharMode,
       "wfBisyncLineNumber": wfBisyncLineNumber,
       "wfBisyncRtsEnable": wfBisyncRtsEnable,
       "wfBisyncExternalClkSpeed": wfBisyncExternalClkSpeed,
       "wfBisyncModule": wfBisyncModule,
       "wfBisyncActualConnector": wfBisyncActualConnector,
       "wfBisyncConnector": wfBisyncConnector,
       "wfBisyncSlot": wfBisyncSlot,
       "wfBisyncActiveCct": wfBisyncActiveCct,
       "wfBisyncState": wfBisyncState,
       "wfBisyncLastState": wfBisyncLastState,
       "wfBisyncRxOctets": wfBisyncRxOctets,
       "wfBisyncTxOctets": wfBisyncTxOctets,
       "wfBisyncRxFrames": wfBisyncRxFrames,
       "wfBisyncTxFrames": wfBisyncTxFrames,
       "wfBisyncRxErrors": wfBisyncRxErrors,
       "wfBisyncTxErrors": wfBisyncTxErrors,
       "wfBisyncTxLackRescs": wfBisyncTxLackRescs,
       "wfBisyncTxUnderFlows": wfBisyncTxUnderFlows,
       "wfBisyncRxOverFlows": wfBisyncRxOverFlows,
       "wfBisyncRxBadFrames": wfBisyncRxBadFrames,
       "wfBisyncRxRunts": wfBisyncRxRunts,
       "wfBisyncTxQueueLength": wfBisyncTxQueueLength,
       "wfBisyncRxQueueLength": wfBisyncRxQueueLength,
       "wfBisyncRxReplenMisses": wfBisyncRxReplenMisses,
       "wfBisyncLastChange": wfBisyncLastChange,
       "wfBisyncOutQLen": wfBisyncOutQLen,
       "wfBisyncRxLackRescsChar": wfBisyncRxLackRescsChar,
       "wfBisyncIsrBCZero": wfBisyncIsrBCZero,
       "wfBisyncIsrBCSix": wfBisyncIsrBCSix,
       "wfBisyncIsrBCInvalid": wfBisyncIsrBCInvalid,
       "wfBisyncIsrBCErrors": wfBisyncIsrBCErrors,
       "wfBisyncLocalConnectionState": wfBisyncLocalConnectionState,
       "wfBisyncRemoteConnectionState": wfBisyncRemoteConnectionState,
       "wfBisyncAdditionalSyncPairs": wfBisyncAdditionalSyncPairs}
)

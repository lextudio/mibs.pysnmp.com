# SNMP MIB module (Wellfleet-SYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-SYNC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:11 2024
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

(wfLine,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfLine")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfSyncTable_Object = MibTable
wfSyncTable = _WfSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5)
)
if mibBuilder.loadTexts:
    wfSyncTable.setStatus("mandatory")
_WfSyncEntry_Object = MibTableRow
wfSyncEntry = _WfSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1)
)
wfSyncEntry.setIndexNames(
    (0, "Wellfleet-SYNC-MIB", "wfSyncSlot"),
    (0, "Wellfleet-SYNC-MIB", "wfSyncConnector"),
)
if mibBuilder.loadTexts:
    wfSyncEntry.setStatus("mandatory")


class _WfSyncDelete_Type(Integer32):
    """Custom type wfSyncDelete based on Integer32"""
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


_WfSyncDelete_Type.__name__ = "Integer32"
_WfSyncDelete_Object = MibTableColumn
wfSyncDelete = _WfSyncDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 1),
    _WfSyncDelete_Type()
)
wfSyncDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncDelete.setStatus("mandatory")


class _WfSyncDisable_Type(Integer32):
    """Custom type wfSyncDisable based on Integer32"""
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


_WfSyncDisable_Type.__name__ = "Integer32"
_WfSyncDisable_Object = MibTableColumn
wfSyncDisable = _WfSyncDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 2),
    _WfSyncDisable_Type()
)
wfSyncDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncDisable.setStatus("mandatory")


class _WfSyncState_Type(Integer32):
    """Custom type wfSyncState based on Integer32"""
    defaultValue = 20

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
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("dsrwait", 6),
          ("holddown", 7),
          ("init", 3),
          ("lineloopbofltest", 19),
          ("notpres", 20),
          ("notpresent", 5),
          ("remoteloop", 8),
          ("up", 1),
          ("wait", 4))
    )


_WfSyncState_Type.__name__ = "Integer32"
_WfSyncState_Object = MibTableColumn
wfSyncState = _WfSyncState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 3),
    _WfSyncState_Type()
)
wfSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncState.setStatus("mandatory")
_WfSyncSlot_Type = Integer32
_WfSyncSlot_Object = MibTableColumn
wfSyncSlot = _WfSyncSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 4),
    _WfSyncSlot_Type()
)
wfSyncSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncSlot.setStatus("mandatory")
_WfSyncConnector_Type = Integer32
_WfSyncConnector_Object = MibTableColumn
wfSyncConnector = _WfSyncConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 5),
    _WfSyncConnector_Type()
)
wfSyncConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncConnector.setStatus("mandatory")


class _WfSyncCct_Type(Integer32):
    """Custom type wfSyncCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfSyncCct_Type.__name__ = "Integer32"
_WfSyncCct_Object = MibTableColumn
wfSyncCct = _WfSyncCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 6),
    _WfSyncCct_Type()
)
wfSyncCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncCct.setStatus("mandatory")


class _WfSyncBofl_Type(Integer32):
    """Custom type wfSyncBofl based on Integer32"""
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


_WfSyncBofl_Type.__name__ = "Integer32"
_WfSyncBofl_Object = MibTableColumn
wfSyncBofl = _WfSyncBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 7),
    _WfSyncBofl_Type()
)
wfSyncBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBofl.setStatus("mandatory")


class _WfSyncBoflTmo_Type(Integer32):
    """Custom type wfSyncBoflTmo based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfSyncBoflTmo_Type.__name__ = "Integer32"
_WfSyncBoflTmo_Object = MibTableColumn
wfSyncBoflTmo = _WfSyncBoflTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 8),
    _WfSyncBoflTmo_Type()
)
wfSyncBoflTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBoflTmo.setStatus("mandatory")


class _WfSyncMtu_Type(Integer32):
    """Custom type wfSyncMtu based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4608),
    )


_WfSyncMtu_Type.__name__ = "Integer32"
_WfSyncMtu_Object = MibTableColumn
wfSyncMtu = _WfSyncMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 9),
    _WfSyncMtu_Type()
)
wfSyncMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncMtu.setStatus("mandatory")
_WfSyncMadr_Type = OctetString
_WfSyncMadr_Object = MibTableColumn
wfSyncMadr = _WfSyncMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 10),
    _WfSyncMadr_Type()
)
wfSyncMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncMadr.setStatus("mandatory")


class _WfSyncPromiscuous_Type(Integer32):
    """Custom type wfSyncPromiscuous based on Integer32"""
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


_WfSyncPromiscuous_Type.__name__ = "Integer32"
_WfSyncPromiscuous_Object = MibTableColumn
wfSyncPromiscuous = _WfSyncPromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 11),
    _WfSyncPromiscuous_Type()
)
wfSyncPromiscuous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPromiscuous.setStatus("mandatory")


class _WfSyncXid_Type(Integer32):
    """Custom type wfSyncXid based on Integer32"""
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


_WfSyncXid_Type.__name__ = "Integer32"
_WfSyncXid_Object = MibTableColumn
wfSyncXid = _WfSyncXid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 12),
    _WfSyncXid_Type()
)
wfSyncXid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncXid.setStatus("mandatory")


class _WfSyncClkSource_Type(Integer32):
    """Custom type wfSyncClkSource based on Integer32"""
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


_WfSyncClkSource_Type.__name__ = "Integer32"
_WfSyncClkSource_Object = MibTableColumn
wfSyncClkSource = _WfSyncClkSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 13),
    _WfSyncClkSource_Type()
)
wfSyncClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncClkSource.setStatus("mandatory")


class _WfSyncClkSpeed_Type(Integer32):
    """Custom type wfSyncClkSpeed based on Integer32"""
    defaultValue = 64102

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2401,
              4807,
              7204,
              9615,
              19230,
              32051,
              38461,
              56818,
              64102,
              125000,
              227272,
              416666,
              625000,
              833333,
              1250000,
              2500000,
              5000000)
        )
    )
    namedValues = NamedValues(
        *(("clk1200b", 1200),
          ("clk125k", 125000),
          ("clk19200b", 19230),
          ("clk1mb", 1250000),
          ("clk230k", 227272),
          ("clk2400b", 2401),
          ("clk2mb", 2500000),
          ("clk32000b", 32051),
          ("clk38400b", 38461),
          ("clk420k", 416666),
          ("clk4800b", 4807),
          ("clk56k", 56818),
          ("clk5mb", 5000000),
          ("clk625k", 625000),
          ("clk64k", 64102),
          ("clk7200b", 7204),
          ("clk833k", 833333),
          ("clk9600b", 9615))
    )


_WfSyncClkSpeed_Type.__name__ = "Integer32"
_WfSyncClkSpeed_Object = MibTableColumn
wfSyncClkSpeed = _WfSyncClkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 14),
    _WfSyncClkSpeed_Type()
)
wfSyncClkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncClkSpeed.setStatus("mandatory")


class _WfSyncSignalMode_Type(Integer32):
    """Custom type wfSyncSignalMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("balanced", 1),
          ("unbalanced", 2))
    )


_WfSyncSignalMode_Type.__name__ = "Integer32"
_WfSyncSignalMode_Object = MibTableColumn
wfSyncSignalMode = _WfSyncSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 15),
    _WfSyncSignalMode_Type()
)
wfSyncSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncSignalMode.setStatus("mandatory")


class _WfSyncRtsEnable_Type(Integer32):
    """Custom type wfSyncRtsEnable based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("kg84aenabled", 3))
    )


_WfSyncRtsEnable_Type.__name__ = "Integer32"
_WfSyncRtsEnable_Object = MibTableColumn
wfSyncRtsEnable = _WfSyncRtsEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 16),
    _WfSyncRtsEnable_Type()
)
wfSyncRtsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncRtsEnable.setStatus("mandatory")


class _WfSyncBurstCount_Type(Integer32):
    """Custom type wfSyncBurstCount based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("unlimited", 3))
    )


_WfSyncBurstCount_Type.__name__ = "Integer32"
_WfSyncBurstCount_Object = MibTableColumn
wfSyncBurstCount = _WfSyncBurstCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 17),
    _WfSyncBurstCount_Type()
)
wfSyncBurstCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBurstCount.setStatus("mandatory")


class _WfSyncService_Type(Integer32):
    """Custom type wfSyncService based on Integer32"""
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
        *(("llc1", 2),
          ("llc2", 3),
          ("transparent", 1))
    )


_WfSyncService_Type.__name__ = "Integer32"
_WfSyncService_Object = MibTableColumn
wfSyncService = _WfSyncService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 18),
    _WfSyncService_Type()
)
wfSyncService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncService.setStatus("mandatory")


class _WfSyncRetryCount_Type(Integer32):
    """Custom type wfSyncRetryCount based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WfSyncRetryCount_Type.__name__ = "Integer32"
_WfSyncRetryCount_Object = MibTableColumn
wfSyncRetryCount = _WfSyncRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 19),
    _WfSyncRetryCount_Type()
)
wfSyncRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncRetryCount.setStatus("mandatory")


class _WfSyncLinkIdleTimer_Type(Integer32):
    """Custom type wfSyncLinkIdleTimer based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_WfSyncLinkIdleTimer_Type.__name__ = "Integer32"
_WfSyncLinkIdleTimer_Object = MibTableColumn
wfSyncLinkIdleTimer = _WfSyncLinkIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 20),
    _WfSyncLinkIdleTimer_Type()
)
wfSyncLinkIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncLinkIdleTimer.setStatus("mandatory")


class _WfSyncRetryTimer_Type(Integer32):
    """Custom type wfSyncRetryTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_WfSyncRetryTimer_Type.__name__ = "Integer32"
_WfSyncRetryTimer_Object = MibTableColumn
wfSyncRetryTimer = _WfSyncRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 21),
    _WfSyncRetryTimer_Type()
)
wfSyncRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncRetryTimer.setStatus("mandatory")


class _WfSyncExtendedAddress_Type(Integer32):
    """Custom type wfSyncExtendedAddress based on Integer32"""
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


_WfSyncExtendedAddress_Type.__name__ = "Integer32"
_WfSyncExtendedAddress_Object = MibTableColumn
wfSyncExtendedAddress = _WfSyncExtendedAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 22),
    _WfSyncExtendedAddress_Type()
)
wfSyncExtendedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncExtendedAddress.setStatus("mandatory")


class _WfSyncExtendedAddressForce_Type(Integer32):
    """Custom type wfSyncExtendedAddressForce based on Integer32"""
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


_WfSyncExtendedAddressForce_Type.__name__ = "Integer32"
_WfSyncExtendedAddressForce_Object = MibTableColumn
wfSyncExtendedAddressForce = _WfSyncExtendedAddressForce_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 23),
    _WfSyncExtendedAddressForce_Type()
)
wfSyncExtendedAddressForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncExtendedAddressForce.setStatus("mandatory")


class _WfSyncExtendedControl_Type(Integer32):
    """Custom type wfSyncExtendedControl based on Integer32"""
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


_WfSyncExtendedControl_Type.__name__ = "Integer32"
_WfSyncExtendedControl_Object = MibTableColumn
wfSyncExtendedControl = _WfSyncExtendedControl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 24),
    _WfSyncExtendedControl_Type()
)
wfSyncExtendedControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncExtendedControl.setStatus("mandatory")


class _WfSyncExtendedControlForce_Type(Integer32):
    """Custom type wfSyncExtendedControlForce based on Integer32"""
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


_WfSyncExtendedControlForce_Type.__name__ = "Integer32"
_WfSyncExtendedControlForce_Object = MibTableColumn
wfSyncExtendedControlForce = _WfSyncExtendedControlForce_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 25),
    _WfSyncExtendedControlForce_Type()
)
wfSyncExtendedControlForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncExtendedControlForce.setStatus("mandatory")


class _WfSyncConnectAttempts_Type(Integer32):
    """Custom type wfSyncConnectAttempts based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_WfSyncConnectAttempts_Type.__name__ = "Integer32"
_WfSyncConnectAttempts_Object = MibTableColumn
wfSyncConnectAttempts = _WfSyncConnectAttempts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 26),
    _WfSyncConnectAttempts_Type()
)
wfSyncConnectAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncConnectAttempts.setStatus("mandatory")


class _WfSyncWindowSizeTx_Type(Integer32):
    """Custom type wfSyncWindowSizeTx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_WfSyncWindowSizeTx_Type.__name__ = "Integer32"
_WfSyncWindowSizeTx_Object = MibTableColumn
wfSyncWindowSizeTx = _WfSyncWindowSizeTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 27),
    _WfSyncWindowSizeTx_Type()
)
wfSyncWindowSizeTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncWindowSizeTx.setStatus("mandatory")


class _WfSyncWindowSizeTxExtc_Type(Integer32):
    """Custom type wfSyncWindowSizeTxExtc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_WfSyncWindowSizeTxExtc_Type.__name__ = "Integer32"
_WfSyncWindowSizeTxExtc_Object = MibTableColumn
wfSyncWindowSizeTxExtc = _WfSyncWindowSizeTxExtc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 28),
    _WfSyncWindowSizeTxExtc_Type()
)
wfSyncWindowSizeTxExtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncWindowSizeTxExtc.setStatus("mandatory")


class _WfSyncMinFrameSpace_Type(Integer32):
    """Custom type wfSyncMinFrameSpace based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WfSyncMinFrameSpace_Type.__name__ = "Integer32"
_WfSyncMinFrameSpace_Object = MibTableColumn
wfSyncMinFrameSpace = _WfSyncMinFrameSpace_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 29),
    _WfSyncMinFrameSpace_Type()
)
wfSyncMinFrameSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncMinFrameSpace.setStatus("mandatory")


class _WfSyncLocalAddress_Type(Integer32):
    """Custom type wfSyncLocalAddress based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("addressdce", 1),
          ("addressdte", 3),
          ("addressexplicit", 7))
    )


_WfSyncLocalAddress_Type.__name__ = "Integer32"
_WfSyncLocalAddress_Object = MibTableColumn
wfSyncLocalAddress = _WfSyncLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 30),
    _WfSyncLocalAddress_Type()
)
wfSyncLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncLocalAddress.setStatus("mandatory")


class _WfSyncRemoteAddress_Type(Integer32):
    """Custom type wfSyncRemoteAddress based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("addressdce", 1),
          ("addressdte", 3),
          ("addressexplicit", 7))
    )


_WfSyncRemoteAddress_Type.__name__ = "Integer32"
_WfSyncRemoteAddress_Object = MibTableColumn
wfSyncRemoteAddress = _WfSyncRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 31),
    _WfSyncRemoteAddress_Type()
)
wfSyncRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncRemoteAddress.setStatus("mandatory")
_WfSyncPassThruLocalMadr_Type = OctetString
_WfSyncPassThruLocalMadr_Object = MibTableColumn
wfSyncPassThruLocalMadr = _WfSyncPassThruLocalMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 32),
    _WfSyncPassThruLocalMadr_Type()
)
wfSyncPassThruLocalMadr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPassThruLocalMadr.setStatus("mandatory")
_WfSyncPassThruRemoteMadr_Type = OctetString
_WfSyncPassThruRemoteMadr_Object = MibTableColumn
wfSyncPassThruRemoteMadr = _WfSyncPassThruRemoteMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 33),
    _WfSyncPassThruRemoteMadr_Type()
)
wfSyncPassThruRemoteMadr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPassThruRemoteMadr.setStatus("mandatory")


class _WfSyncWanProtocol_Type(Integer32):
    """Custom type wfSyncWanProtocol based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("aot", 12),
          ("atm", 9),
          ("framerelay", 5),
          ("lapb", 10),
          ("passthru", 2),
          ("ppp", 3),
          ("sdlc", 11),
          ("smds", 4),
          ("standard", 1),
          ("sw", 8),
          ("switch", 7),
          ("x25", 6))
    )


_WfSyncWanProtocol_Type.__name__ = "Integer32"
_WfSyncWanProtocol_Object = MibTableColumn
wfSyncWanProtocol = _WfSyncWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 34),
    _WfSyncWanProtocol_Type()
)
wfSyncWanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncWanProtocol.setStatus("mandatory")


class _WfSyncCrcSize_Type(Integer32):
    """Custom type wfSyncCrcSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16bit", 1),
          ("crc32bit", 2))
    )


_WfSyncCrcSize_Type.__name__ = "Integer32"
_WfSyncCrcSize_Object = MibTableColumn
wfSyncCrcSize = _WfSyncCrcSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 35),
    _WfSyncCrcSize_Type()
)
wfSyncCrcSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncCrcSize.setStatus("mandatory")
_WfSyncRxOctets_Type = Counter32
_WfSyncRxOctets_Object = MibTableColumn
wfSyncRxOctets = _WfSyncRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 36),
    _WfSyncRxOctets_Type()
)
wfSyncRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRxOctets.setStatus("mandatory")
_WfSyncRxFrames_Type = Counter32
_WfSyncRxFrames_Object = MibTableColumn
wfSyncRxFrames = _WfSyncRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 37),
    _WfSyncRxFrames_Type()
)
wfSyncRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRxFrames.setStatus("mandatory")
_WfSyncTxOctets_Type = Counter32
_WfSyncTxOctets_Object = MibTableColumn
wfSyncTxOctets = _WfSyncTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 38),
    _WfSyncTxOctets_Type()
)
wfSyncTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncTxOctets.setStatus("mandatory")
_WfSyncTxFrames_Type = Counter32
_WfSyncTxFrames_Object = MibTableColumn
wfSyncTxFrames = _WfSyncTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 39),
    _WfSyncTxFrames_Type()
)
wfSyncTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncTxFrames.setStatus("mandatory")
_WfSyncRxErrors_Type = Counter32
_WfSyncRxErrors_Object = MibTableColumn
wfSyncRxErrors = _WfSyncRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 40),
    _WfSyncRxErrors_Type()
)
wfSyncRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRxErrors.setStatus("mandatory")
_WfSyncTxErrors_Type = Counter32
_WfSyncTxErrors_Object = MibTableColumn
wfSyncTxErrors = _WfSyncTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 41),
    _WfSyncTxErrors_Type()
)
wfSyncTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncTxErrors.setStatus("mandatory")
_WfSyncLackRescRx_Type = Counter32
_WfSyncLackRescRx_Object = MibTableColumn
wfSyncLackRescRx = _WfSyncLackRescRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 42),
    _WfSyncLackRescRx_Type()
)
wfSyncLackRescRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncLackRescRx.setStatus("mandatory")
_WfSyncLackRescTx_Type = Counter32
_WfSyncLackRescTx_Object = MibTableColumn
wfSyncLackRescTx = _WfSyncLackRescTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 43),
    _WfSyncLackRescTx_Type()
)
wfSyncLackRescTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncLackRescTx.setStatus("mandatory")
_WfSyncUnderFlowTx_Type = Counter32
_WfSyncUnderFlowTx_Object = MibTableColumn
wfSyncUnderFlowTx = _WfSyncUnderFlowTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 44),
    _WfSyncUnderFlowTx_Type()
)
wfSyncUnderFlowTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncUnderFlowTx.setStatus("mandatory")
_WfSyncRejectsTx_Type = Counter32
_WfSyncRejectsTx_Object = MibTableColumn
wfSyncRejectsTx = _WfSyncRejectsTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 45),
    _WfSyncRejectsTx_Type()
)
wfSyncRejectsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRejectsTx.setStatus("mandatory")
_WfSyncRejectsRx_Type = Counter32
_WfSyncRejectsRx_Object = MibTableColumn
wfSyncRejectsRx = _WfSyncRejectsRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 46),
    _WfSyncRejectsRx_Type()
)
wfSyncRejectsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRejectsRx.setStatus("mandatory")
_WfSyncOverFlowRx_Type = Counter32
_WfSyncOverFlowRx_Object = MibTableColumn
wfSyncOverFlowRx = _WfSyncOverFlowRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 47),
    _WfSyncOverFlowRx_Type()
)
wfSyncOverFlowRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncOverFlowRx.setStatus("mandatory")
_WfSyncFramesIncompRx_Type = Counter32
_WfSyncFramesIncompRx_Object = MibTableColumn
wfSyncFramesIncompRx = _WfSyncFramesIncompRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 48),
    _WfSyncFramesIncompRx_Type()
)
wfSyncFramesIncompRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncFramesIncompRx.setStatus("mandatory")
_WfSyncBadFramesRx_Type = Counter32
_WfSyncBadFramesRx_Object = MibTableColumn
wfSyncBadFramesRx = _WfSyncBadFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 49),
    _WfSyncBadFramesRx_Type()
)
wfSyncBadFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncBadFramesRx.setStatus("mandatory")
_WfSyncFrameRejectsRx_Type = Counter32
_WfSyncFrameRejectsRx_Object = MibTableColumn
wfSyncFrameRejectsRx = _WfSyncFrameRejectsRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 50),
    _WfSyncFrameRejectsRx_Type()
)
wfSyncFrameRejectsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncFrameRejectsRx.setStatus("mandatory")
_WfSyncRuntsRx_Type = Counter32
_WfSyncRuntsRx_Object = MibTableColumn
wfSyncRuntsRx = _WfSyncRuntsRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 51),
    _WfSyncRuntsRx_Type()
)
wfSyncRuntsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRuntsRx.setStatus("mandatory")
_WfSyncT1Timeouts_Type = Counter32
_WfSyncT1Timeouts_Object = MibTableColumn
wfSyncT1Timeouts = _WfSyncT1Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 52),
    _WfSyncT1Timeouts_Type()
)
wfSyncT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncT1Timeouts.setStatus("mandatory")
_WfSyncMemoryErrors_Type = Counter32
_WfSyncMemoryErrors_Object = MibTableColumn
wfSyncMemoryErrors = _WfSyncMemoryErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 53),
    _WfSyncMemoryErrors_Type()
)
wfSyncMemoryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncMemoryErrors.setStatus("mandatory")


class _WfSyncMediaType_Type(Integer32):
    """Custom type wfSyncMediaType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("bri", 6),
          ("default", 1),
          ("e1", 3),
          ("hayes", 8),
          ("isdnleased", 7),
          ("raisedtr", 4),
          ("t1", 2),
          ("v25bis", 5))
    )


_WfSyncMediaType_Type.__name__ = "Integer32"
_WfSyncMediaType_Object = MibTableColumn
wfSyncMediaType = _WfSyncMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 54),
    _WfSyncMediaType_Type()
)
wfSyncMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncMediaType.setStatus("mandatory")


class _WfSyncCfgTxQueueLength_Type(Integer32):
    """Custom type wfSyncCfgTxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfSyncCfgTxQueueLength_Type.__name__ = "Integer32"
_WfSyncCfgTxQueueLength_Object = MibTableColumn
wfSyncCfgTxQueueLength = _WfSyncCfgTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 55),
    _WfSyncCfgTxQueueLength_Type()
)
wfSyncCfgTxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncCfgTxQueueLength.setStatus("mandatory")


class _WfSyncCfgRxQueueLength_Type(Integer32):
    """Custom type wfSyncCfgRxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfSyncCfgRxQueueLength_Type.__name__ = "Integer32"
_WfSyncCfgRxQueueLength_Object = MibTableColumn
wfSyncCfgRxQueueLength = _WfSyncCfgRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 56),
    _WfSyncCfgRxQueueLength_Type()
)
wfSyncCfgRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncCfgRxQueueLength.setStatus("mandatory")
_WfSyncTxQueueLength_Type = Integer32
_WfSyncTxQueueLength_Object = MibTableColumn
wfSyncTxQueueLength = _WfSyncTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 57),
    _WfSyncTxQueueLength_Type()
)
wfSyncTxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncTxQueueLength.setStatus("mandatory")
_WfSyncRxQueueLength_Type = Integer32
_WfSyncRxQueueLength_Object = MibTableColumn
wfSyncRxQueueLength = _WfSyncRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 58),
    _WfSyncRxQueueLength_Type()
)
wfSyncRxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRxQueueLength.setStatus("mandatory")
_WfSyncRxReplenMisses_Type = Counter32
_WfSyncRxReplenMisses_Object = MibTableColumn
wfSyncRxReplenMisses = _WfSyncRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 59),
    _WfSyncRxReplenMisses_Type()
)
wfSyncRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRxReplenMisses.setStatus("mandatory")


class _WfSyncStartUpMode_Type(Integer32):
    """Custom type wfSyncStartUpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_WfSyncStartUpMode_Type.__name__ = "Integer32"
_WfSyncStartUpMode_Object = MibTableColumn
wfSyncStartUpMode = _WfSyncStartUpMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 60),
    _WfSyncStartUpMode_Type()
)
wfSyncStartUpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncStartUpMode.setStatus("mandatory")


class _WfSyncIdleRRFrames_Type(Integer32):
    """Custom type wfSyncIdleRRFrames based on Integer32"""
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


_WfSyncIdleRRFrames_Type.__name__ = "Integer32"
_WfSyncIdleRRFrames_Object = MibTableColumn
wfSyncIdleRRFrames = _WfSyncIdleRRFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 61),
    _WfSyncIdleRRFrames_Type()
)
wfSyncIdleRRFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncIdleRRFrames.setStatus("mandatory")


class _WfSyncMultilineMode_Type(Integer32):
    """Custom type wfSyncMultilineMode based on Integer32"""
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
        *(("monitor", 2),
          ("primary", 3),
          ("secondary", 4),
          ("standard", 1))
    )


_WfSyncMultilineMode_Type.__name__ = "Integer32"
_WfSyncMultilineMode_Object = MibTableColumn
wfSyncMultilineMode = _WfSyncMultilineMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 62),
    _WfSyncMultilineMode_Type()
)
wfSyncMultilineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncMultilineMode.setStatus("mandatory")


class _WfSyncBODExamPeriod_Type(Integer32):
    """Custom type wfSyncBODExamPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200),
    )


_WfSyncBODExamPeriod_Type.__name__ = "Integer32"
_WfSyncBODExamPeriod_Object = MibTableColumn
wfSyncBODExamPeriod = _WfSyncBODExamPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 63),
    _WfSyncBODExamPeriod_Type()
)
wfSyncBODExamPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBODExamPeriod.setStatus("mandatory")


class _WfSyncBODFullThreshold_Type(Integer32):
    """Custom type wfSyncBODFullThreshold based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_WfSyncBODFullThreshold_Type.__name__ = "Integer32"
_WfSyncBODFullThreshold_Object = MibTableColumn
wfSyncBODFullThreshold = _WfSyncBODFullThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 64),
    _WfSyncBODFullThreshold_Type()
)
wfSyncBODFullThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBODFullThreshold.setStatus("mandatory")


class _WfSyncBODRecoverThreshold_Type(Integer32):
    """Custom type wfSyncBODRecoverThreshold based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_WfSyncBODRecoverThreshold_Type.__name__ = "Integer32"
_WfSyncBODRecoverThreshold_Object = MibTableColumn
wfSyncBODRecoverThreshold = _WfSyncBODRecoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 65),
    _WfSyncBODRecoverThreshold_Type()
)
wfSyncBODRecoverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBODRecoverThreshold.setStatus("mandatory")


class _WfSyncBODPeriodsToFail_Type(Integer32):
    """Custom type wfSyncBODPeriodsToFail based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfSyncBODPeriodsToFail_Type.__name__ = "Integer32"
_WfSyncBODPeriodsToFail_Object = MibTableColumn
wfSyncBODPeriodsToFail = _WfSyncBODPeriodsToFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 66),
    _WfSyncBODPeriodsToFail_Type()
)
wfSyncBODPeriodsToFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBODPeriodsToFail.setStatus("mandatory")


class _WfSyncKG84ACycle_Type(Integer32):
    """Custom type wfSyncKG84ACycle based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              25,
              50,
              100,
              200,
              500)
        )
    )
    namedValues = NamedValues(
        *(("cycle100ms", 100),
          ("cycle10ms", 10),
          ("cycle200ms", 200),
          ("cycle25ms", 25),
          ("cycle500ms", 500),
          ("cycle50ms", 50),
          ("cycle5ms", 5))
    )


_WfSyncKG84ACycle_Type.__name__ = "Integer32"
_WfSyncKG84ACycle_Object = MibTableColumn
wfSyncKG84ACycle = _WfSyncKG84ACycle_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 67),
    _WfSyncKG84ACycle_Type()
)
wfSyncKG84ACycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncKG84ACycle.setStatus("mandatory")


class _WfSyncKG84ASyncLossInterval_Type(Integer32):
    """Custom type wfSyncKG84ASyncLossInterval based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              10,
              25,
              50,
              100,
              200,
              500)
        )
    )
    namedValues = NamedValues(
        *(("num100cycles", 100),
          ("num10cycles", 10),
          ("num200cycles", 200),
          ("num25cycles", 25),
          ("num2cycles", 2),
          ("num500cycles", 500),
          ("num50cycles", 50),
          ("num5cycles", 5))
    )


_WfSyncKG84ASyncLossInterval_Type.__name__ = "Integer32"
_WfSyncKG84ASyncLossInterval_Object = MibTableColumn
wfSyncKG84ASyncLossInterval = _WfSyncKG84ASyncLossInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 68),
    _WfSyncKG84ASyncLossInterval_Type()
)
wfSyncKG84ASyncLossInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncKG84ASyncLossInterval.setStatus("mandatory")


class _WfSyncKG84ARemoteResyncWait_Type(Integer32):
    """Custom type wfSyncKG84ARemoteResyncWait based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              10,
              25,
              50,
              100,
              200,
              500)
        )
    )
    namedValues = NamedValues(
        *(("num100cycles", 100),
          ("num10cycles", 10),
          ("num200cycles", 200),
          ("num25cycles", 25),
          ("num2cycles", 2),
          ("num500cycles", 500),
          ("num50cycles", 50),
          ("num5cycles", 5))
    )


_WfSyncKG84ARemoteResyncWait_Type.__name__ = "Integer32"
_WfSyncKG84ARemoteResyncWait_Object = MibTableColumn
wfSyncKG84ARemoteResyncWait = _WfSyncKG84ARemoteResyncWait_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 69),
    _WfSyncKG84ARemoteResyncWait_Type()
)
wfSyncKG84ARemoteResyncWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncKG84ARemoteResyncWait.setStatus("mandatory")


class _WfSyncKG84ASyncPulse_Type(Integer32):
    """Custom type wfSyncKG84ASyncPulse based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_WfSyncKG84ASyncPulse_Type.__name__ = "Integer32"
_WfSyncKG84ASyncPulse_Object = MibTableColumn
wfSyncKG84ASyncPulse = _WfSyncKG84ASyncPulse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 70),
    _WfSyncKG84ASyncPulse_Type()
)
wfSyncKG84ASyncPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncKG84ASyncPulse.setStatus("mandatory")
_WfSyncKG84AResyncs_Type = Integer32
_WfSyncKG84AResyncs_Object = MibTableColumn
wfSyncKG84AResyncs = _WfSyncKG84AResyncs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 71),
    _WfSyncKG84AResyncs_Type()
)
wfSyncKG84AResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncKG84AResyncs.setStatus("mandatory")
_WfSyncKG84AResyncsDetected_Type = Integer32
_WfSyncKG84AResyncsDetected_Object = MibTableColumn
wfSyncKG84AResyncsDetected = _WfSyncKG84AResyncsDetected_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 72),
    _WfSyncKG84AResyncsDetected_Type()
)
wfSyncKG84AResyncsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncKG84AResyncsDetected.setStatus("mandatory")
_WfSyncKG84ABsu_Type = Integer32
_WfSyncKG84ABsu_Object = MibTableColumn
wfSyncKG84ABsu = _WfSyncKG84ABsu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 73),
    _WfSyncKG84ABsu_Type()
)
wfSyncKG84ABsu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncKG84ABsu.setStatus("mandatory")


class _WfSyncKG84AState_Type(Integer32):
    """Custom type wfSyncKG84AState based on Integer32"""
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
        *(("idle", 1),
          ("local", 2),
          ("remote", 3),
          ("sync", 4))
    )


_WfSyncKG84AState_Type.__name__ = "Integer32"
_WfSyncKG84AState_Object = MibTableColumn
wfSyncKG84AState = _WfSyncKG84AState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 74),
    _WfSyncKG84AState_Type()
)
wfSyncKG84AState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncKG84AState.setStatus("mandatory")
_WfSyncKG84AOkFrames_Type = Integer32
_WfSyncKG84AOkFrames_Object = MibTableColumn
wfSyncKG84AOkFrames = _WfSyncKG84AOkFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 75),
    _WfSyncKG84AOkFrames_Type()
)
wfSyncKG84AOkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncKG84AOkFrames.setStatus("mandatory")


class _WfSyncPollingEnable_Type(Integer32):
    """Custom type wfSyncPollingEnable based on Integer32"""
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


_WfSyncPollingEnable_Type.__name__ = "Integer32"
_WfSyncPollingEnable_Object = MibTableColumn
wfSyncPollingEnable = _WfSyncPollingEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 76),
    _WfSyncPollingEnable_Type()
)
wfSyncPollingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPollingEnable.setStatus("mandatory")


class _WfSyncBackupPool_Type(Integer32):
    """Custom type wfSyncBackupPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfSyncBackupPool_Type.__name__ = "Integer32"
_WfSyncBackupPool_Object = MibTableColumn
wfSyncBackupPool = _WfSyncBackupPool_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 77),
    _WfSyncBackupPool_Type()
)
wfSyncBackupPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBackupPool.setStatus("mandatory")


class _WfSyncDemandPool_Type(Integer32):
    """Custom type wfSyncDemandPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfSyncDemandPool_Type.__name__ = "Integer32"
_WfSyncDemandPool_Object = MibTableColumn
wfSyncDemandPool = _WfSyncDemandPool_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 78),
    _WfSyncDemandPool_Type()
)
wfSyncDemandPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncDemandPool.setStatus("mandatory")
_WfSyncLineNumber_Type = Integer32
_WfSyncLineNumber_Object = MibTableColumn
wfSyncLineNumber = _WfSyncLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 79),
    _WfSyncLineNumber_Type()
)
wfSyncLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncLineNumber.setStatus("mandatory")
_WfSyncHoldDownTime_Type = Integer32
_WfSyncHoldDownTime_Object = MibTableColumn
wfSyncHoldDownTime = _WfSyncHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 80),
    _WfSyncHoldDownTime_Type()
)
wfSyncHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncHoldDownTime.setStatus("mandatory")


class _WfSyncNetworkType_Type(Integer32):
    """Custom type wfSyncNetworkType based on Integer32"""
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
        *(("c03", 3),
          ("gosip", 1),
          ("net2", 2))
    )


_WfSyncNetworkType_Type.__name__ = "Integer32"
_WfSyncNetworkType_Object = MibTableColumn
wfSyncNetworkType = _WfSyncNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 81),
    _WfSyncNetworkType_Type()
)
wfSyncNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncNetworkType.setStatus("mandatory")


class _WfSyncActiveCct_Type(Integer32):
    """Custom type wfSyncActiveCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfSyncActiveCct_Type.__name__ = "Integer32"
_WfSyncActiveCct_Object = MibTableColumn
wfSyncActiveCct = _WfSyncActiveCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 82),
    _WfSyncActiveCct_Type()
)
wfSyncActiveCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncActiveCct.setStatus("mandatory")


class _WfSyncCableType_Type(Integer32):
    """Custom type wfSyncCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_WfSyncCableType_Type.__name__ = "Integer32"
_WfSyncCableType_Object = MibTableColumn
wfSyncCableType = _WfSyncCableType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 83),
    _WfSyncCableType_Type()
)
wfSyncCableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncCableType.setStatus("mandatory")
_WfSyncRxDropPackets_Type = Counter32
_WfSyncRxDropPackets_Object = MibTableColumn
wfSyncRxDropPackets = _WfSyncRxDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 84),
    _WfSyncRxDropPackets_Type()
)
wfSyncRxDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRxDropPackets.setStatus("mandatory")
_WfSyncTxDropPackets_Type = Counter32
_WfSyncTxDropPackets_Object = MibTableColumn
wfSyncTxDropPackets = _WfSyncTxDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 85),
    _WfSyncTxDropPackets_Type()
)
wfSyncTxDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncTxDropPackets.setStatus("mandatory")


class _WfSyncModule_Type(Integer32):
    """Custom type wfSyncModule based on Integer32"""
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


_WfSyncModule_Type.__name__ = "Integer32"
_WfSyncModule_Object = MibTableColumn
wfSyncModule = _WfSyncModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 86),
    _WfSyncModule_Type()
)
wfSyncModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncModule.setStatus("mandatory")


class _WfSyncActualConnector_Type(Integer32):
    """Custom type wfSyncActualConnector based on Integer32"""
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


_WfSyncActualConnector_Type.__name__ = "Integer32"
_WfSyncActualConnector_Object = MibTableColumn
wfSyncActualConnector = _WfSyncActualConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 87),
    _WfSyncActualConnector_Type()
)
wfSyncActualConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncActualConnector.setStatus("mandatory")


class _WfSyncLineCoding_Type(Integer32):
    """Custom type wfSyncLineCoding based on Integer32"""
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
        *(("nrz", 1),
          ("nrzi", 2),
          ("nrzimark", 3))
    )


_WfSyncLineCoding_Type.__name__ = "Integer32"
_WfSyncLineCoding_Object = MibTableColumn
wfSyncLineCoding = _WfSyncLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 88),
    _WfSyncLineCoding_Type()
)
wfSyncLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncLineCoding.setStatus("mandatory")
_WfSyncLastChange_Type = TimeTicks
_WfSyncLastChange_Object = MibTableColumn
wfSyncLastChange = _WfSyncLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 89),
    _WfSyncLastChange_Type()
)
wfSyncLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncLastChange.setStatus("mandatory")
_WfSyncOutQLen_Type = Gauge32
_WfSyncOutQLen_Object = MibTableColumn
wfSyncOutQLen = _WfSyncOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 90),
    _WfSyncOutQLen_Type()
)
wfSyncOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncOutQLen.setStatus("mandatory")


class _WfSyncRemoteLpbkDetection_Type(Integer32):
    """Custom type wfSyncRemoteLpbkDetection based on Integer32"""
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


_WfSyncRemoteLpbkDetection_Type.__name__ = "Integer32"
_WfSyncRemoteLpbkDetection_Object = MibTableColumn
wfSyncRemoteLpbkDetection = _WfSyncRemoteLpbkDetection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 91),
    _WfSyncRemoteLpbkDetection_Type()
)
wfSyncRemoteLpbkDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncRemoteLpbkDetection.setStatus("mandatory")


class _WfSyncLastState_Type(Integer32):
    """Custom type wfSyncLastState based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("dsrwait", 6),
          ("holddown", 7),
          ("init", 3),
          ("notpres", 20),
          ("notpresent", 5),
          ("remoteloop", 8),
          ("up", 1),
          ("wait", 4))
    )


_WfSyncLastState_Type.__name__ = "Integer32"
_WfSyncLastState_Object = MibTableColumn
wfSyncLastState = _WfSyncLastState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 92),
    _WfSyncLastState_Type()
)
wfSyncLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncLastState.setStatus("mandatory")


class _WfSyncExternalClkSpeed_Type(Integer32):
    """Custom type wfSyncExternalClkSpeed based on Integer32"""
    defaultValue = 64102

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 6000000),
    )


_WfSyncExternalClkSpeed_Type.__name__ = "Integer32"
_WfSyncExternalClkSpeed_Object = MibTableColumn
wfSyncExternalClkSpeed = _WfSyncExternalClkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 93),
    _WfSyncExternalClkSpeed_Type()
)
wfSyncExternalClkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncExternalClkSpeed.setStatus("mandatory")


class _WfSyncBChannelOverride_Type(Integer32):
    """Custom type wfSyncBChannelOverride based on Integer32"""
    defaultValue = 3

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
        *(("bchannel1", 1),
          ("bchannel2", 2),
          ("default", 3),
          ("floatingb", 4))
    )


_WfSyncBChannelOverride_Type.__name__ = "Integer32"
_WfSyncBChannelOverride_Object = MibTableColumn
wfSyncBChannelOverride = _WfSyncBChannelOverride_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 94),
    _WfSyncBChannelOverride_Type()
)
wfSyncBChannelOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBChannelOverride.setStatus("mandatory")


class _WfSyncBChannel_Type(Integer32):
    """Custom type wfSyncBChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bchannel1", 1),
          ("bchannel2", 2))
    )


_WfSyncBChannel_Type.__name__ = "Integer32"
_WfSyncBChannel_Object = MibTableColumn
wfSyncBChannel = _WfSyncBChannel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 95),
    _WfSyncBChannel_Type()
)
wfSyncBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncBChannel.setStatus("mandatory")


class _WfSyncForceIFTF_Type(Integer32):
    """Custom type wfSyncForceIFTF based on Integer32"""
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
        *(("default", 1),
          ("flagstreaming", 4),
          ("forcehdlcflags", 2),
          ("forceidles", 3))
    )


_WfSyncForceIFTF_Type.__name__ = "Integer32"
_WfSyncForceIFTF_Object = MibTableColumn
wfSyncForceIFTF = _WfSyncForceIFTF_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 96),
    _WfSyncForceIFTF_Type()
)
wfSyncForceIFTF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncForceIFTF.setStatus("mandatory")


class _WfSyncPriority_Type(Integer32):
    """Custom type wfSyncPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_WfSyncPriority_Type.__name__ = "Integer32"
_WfSyncPriority_Object = MibTableColumn
wfSyncPriority = _WfSyncPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 97),
    _WfSyncPriority_Type()
)
wfSyncPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPriority.setStatus("mandatory")


class _WfSyncTurboBofl_Type(Integer32):
    """Custom type wfSyncTurboBofl based on Integer32"""
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


_WfSyncTurboBofl_Type.__name__ = "Integer32"
_WfSyncTurboBofl_Object = MibTableColumn
wfSyncTurboBofl = _WfSyncTurboBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 98),
    _WfSyncTurboBofl_Type()
)
wfSyncTurboBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncTurboBofl.setStatus("mandatory")


class _WfSyncBoflNum_Type(Integer32):
    """Custom type wfSyncBoflNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfSyncBoflNum_Type.__name__ = "Integer32"
_WfSyncBoflNum_Object = MibTableColumn
wfSyncBoflNum = _WfSyncBoflNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 99),
    _WfSyncBoflNum_Type()
)
wfSyncBoflNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBoflNum.setStatus("mandatory")


class _WfSyncBoflLen_Type(Integer32):
    """Custom type wfSyncBoflLen based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 4450),
    )


_WfSyncBoflLen_Type.__name__ = "Integer32"
_WfSyncBoflLen_Object = MibTableColumn
wfSyncBoflLen = _WfSyncBoflLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 100),
    _WfSyncBoflLen_Type()
)
wfSyncBoflLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBoflLen.setStatus("mandatory")
_WfSyncTurboBoflMisses_Type = Integer32
_WfSyncTurboBoflMisses_Object = MibTableColumn
wfSyncTurboBoflMisses = _WfSyncTurboBoflMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 101),
    _WfSyncTurboBoflMisses_Type()
)
wfSyncTurboBoflMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncTurboBoflMisses.setStatus("mandatory")
_WfSyncTurboBoflInvocations_Type = Integer32
_WfSyncTurboBoflInvocations_Object = MibTableColumn
wfSyncTurboBoflInvocations = _WfSyncTurboBoflInvocations_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 102),
    _WfSyncTurboBoflInvocations_Type()
)
wfSyncTurboBoflInvocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncTurboBoflInvocations.setStatus("mandatory")


class _WfSyncBandwidthOnDemandPool_Type(Integer32):
    """Custom type wfSyncBandwidthOnDemandPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfSyncBandwidthOnDemandPool_Type.__name__ = "Integer32"
_WfSyncBandwidthOnDemandPool_Object = MibTableColumn
wfSyncBandwidthOnDemandPool = _WfSyncBandwidthOnDemandPool_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 103),
    _WfSyncBandwidthOnDemandPool_Type()
)
wfSyncBandwidthOnDemandPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBandwidthOnDemandPool.setStatus("mandatory")


class _WfSyncBODRecoverPeriodsToPass_Type(Integer32):
    """Custom type wfSyncBODRecoverPeriodsToPass based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfSyncBODRecoverPeriodsToPass_Type.__name__ = "Integer32"
_WfSyncBODRecoverPeriodsToPass_Object = MibTableColumn
wfSyncBODRecoverPeriodsToPass = _WfSyncBODRecoverPeriodsToPass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 104),
    _WfSyncBODRecoverPeriodsToPass_Type()
)
wfSyncBODRecoverPeriodsToPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBODRecoverPeriodsToPass.setStatus("mandatory")
_WfSyncBODHistory_Type = DisplayString
_WfSyncBODHistory_Object = MibTableColumn
wfSyncBODHistory = _WfSyncBODHistory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 105),
    _WfSyncBODHistory_Type()
)
wfSyncBODHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncBODHistory.setStatus("mandatory")
_WfSyncBODDebugFlag_Type = Integer32
_WfSyncBODDebugFlag_Object = MibTableColumn
wfSyncBODDebugFlag = _WfSyncBODDebugFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 106),
    _WfSyncBODDebugFlag_Type()
)
wfSyncBODDebugFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBODDebugFlag.setStatus("mandatory")


class _WfSyncBChRateAdaption_Type(Integer32):
    """Custom type wfSyncBChRateAdaption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaption128k", 2),
          ("adaption64k", 1))
    )


_WfSyncBChRateAdaption_Type.__name__ = "Integer32"
_WfSyncBChRateAdaption_Object = MibTableColumn
wfSyncBChRateAdaption = _WfSyncBChRateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 107),
    _WfSyncBChRateAdaption_Type()
)
wfSyncBChRateAdaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncBChRateAdaption.setStatus("mandatory")


class _WfSyncBChActualRateAdaption_Type(Integer32):
    """Custom type wfSyncBChActualRateAdaption based on Integer32"""
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
        *(("adaption128k", 2),
          ("adaption56klsb", 4),
          ("adaption56kmsb", 3),
          ("adaption64k", 1))
    )


_WfSyncBChActualRateAdaption_Type.__name__ = "Integer32"
_WfSyncBChActualRateAdaption_Object = MibTableColumn
wfSyncBChActualRateAdaption = _WfSyncBChActualRateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 108),
    _WfSyncBChActualRateAdaption_Type()
)
wfSyncBChActualRateAdaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncBChActualRateAdaption.setStatus("mandatory")


class _WfSyncWanType_Type(Integer32):
    """Custom type wfSyncWanType based on Integer32"""
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
        *(("asynchronous", 2),
          ("pasynchronous", 3),
          ("synchronous", 1))
    )


_WfSyncWanType_Type.__name__ = "Integer32"
_WfSyncWanType_Object = MibTableColumn
wfSyncWanType = _WfSyncWanType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 109),
    _WfSyncWanType_Type()
)
wfSyncWanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncWanType.setStatus("mandatory")


class _WfSyncAsyncBaudRate_Type(Integer32):
    """Custom type wfSyncAsyncBaudRate based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2400,
              4800,
              7200,
              9600,
              12000,
              14400,
              19200,
              28800,
              38400,
              57600,
              64000,
              76800,
              96000,
              115200)
        )
    )
    namedValues = NamedValues(
        *(("baudrate115k", 115200),
          ("baudrate12000b", 12000),
          ("baudrate1200b", 1200),
          ("baudrate14400b", 14400),
          ("baudrate19200b", 19200),
          ("baudrate2400b", 2400),
          ("baudrate28800b", 28800),
          ("baudrate38k", 38400),
          ("baudrate4800b", 4800),
          ("baudrate56k", 57600),
          ("baudrate64k", 64000),
          ("baudrate7200b", 7200),
          ("baudrate76k", 76800),
          ("baudrate9600b", 9600),
          ("baudrate96k", 96000))
    )


_WfSyncAsyncBaudRate_Type.__name__ = "Integer32"
_WfSyncAsyncBaudRate_Object = MibTableColumn
wfSyncAsyncBaudRate = _WfSyncAsyncBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 110),
    _WfSyncAsyncBaudRate_Type()
)
wfSyncAsyncBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncAsyncBaudRate.setStatus("mandatory")


class _WfSyncCfgAsyncCmndMaxIdles_Type(Integer32):
    """Custom type wfSyncCfgAsyncCmndMaxIdles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_WfSyncCfgAsyncCmndMaxIdles_Type.__name__ = "Integer32"
_WfSyncCfgAsyncCmndMaxIdles_Object = MibTableColumn
wfSyncCfgAsyncCmndMaxIdles = _WfSyncCfgAsyncCmndMaxIdles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 111),
    _WfSyncCfgAsyncCmndMaxIdles_Type()
)
wfSyncCfgAsyncCmndMaxIdles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncCfgAsyncCmndMaxIdles.setStatus("mandatory")
_WfSyncAsyncCmndMaxIdles_Type = Integer32
_WfSyncAsyncCmndMaxIdles_Object = MibTableColumn
wfSyncAsyncCmndMaxIdles = _WfSyncAsyncCmndMaxIdles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 112),
    _WfSyncAsyncCmndMaxIdles_Type()
)
wfSyncAsyncCmndMaxIdles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncAsyncCmndMaxIdles.setStatus("mandatory")


class _WfSyncCfgAsyncDataMaxIdles_Type(Integer32):
    """Custom type wfSyncCfgAsyncDataMaxIdles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_WfSyncCfgAsyncDataMaxIdles_Type.__name__ = "Integer32"
_WfSyncCfgAsyncDataMaxIdles_Object = MibTableColumn
wfSyncCfgAsyncDataMaxIdles = _WfSyncCfgAsyncDataMaxIdles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 113),
    _WfSyncCfgAsyncDataMaxIdles_Type()
)
wfSyncCfgAsyncDataMaxIdles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncCfgAsyncDataMaxIdles.setStatus("mandatory")
_WfSyncAsyncDataMaxIdles_Type = Integer32
_WfSyncAsyncDataMaxIdles_Object = MibTableColumn
wfSyncAsyncDataMaxIdles = _WfSyncAsyncDataMaxIdles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 114),
    _WfSyncAsyncDataMaxIdles_Type()
)
wfSyncAsyncDataMaxIdles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncAsyncDataMaxIdles.setStatus("mandatory")
_WfSyncFramesAbortTx_Type = Counter32
_WfSyncFramesAbortTx_Object = MibTableColumn
wfSyncFramesAbortTx = _WfSyncFramesAbortTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 115),
    _WfSyncFramesAbortTx_Type()
)
wfSyncFramesAbortTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncFramesAbortTx.setStatus("mandatory")


class _WfSyncPasyncParityType_Type(Integer32):
    """Custom type wfSyncPasyncParityType based on Integer32"""
    defaultValue = 2

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
        *(("even", 2),
          ("high", 3),
          ("low", 4),
          ("none", 5),
          ("odd", 1))
    )


_WfSyncPasyncParityType_Type.__name__ = "Integer32"
_WfSyncPasyncParityType_Object = MibTableColumn
wfSyncPasyncParityType = _WfSyncPasyncParityType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 116),
    _WfSyncPasyncParityType_Type()
)
wfSyncPasyncParityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPasyncParityType.setStatus("mandatory")


class _WfSyncPasyncCharacterLength_Type(Integer32):
    """Custom type wfSyncPasyncCharacterLength based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("seven", 7),
          ("six", 6))
    )


_WfSyncPasyncCharacterLength_Type.__name__ = "Integer32"
_WfSyncPasyncCharacterLength_Object = MibTableColumn
wfSyncPasyncCharacterLength = _WfSyncPasyncCharacterLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 117),
    _WfSyncPasyncCharacterLength_Type()
)
wfSyncPasyncCharacterLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPasyncCharacterLength.setStatus("mandatory")


class _WfSyncPasyncStopLength_Type(Integer32):
    """Custom type wfSyncPasyncStopLength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfSyncPasyncStopLength_Type.__name__ = "Integer32"
_WfSyncPasyncStopLength_Object = MibTableColumn
wfSyncPasyncStopLength = _WfSyncPasyncStopLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 118),
    _WfSyncPasyncStopLength_Type()
)
wfSyncPasyncStopLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPasyncStopLength.setStatus("mandatory")


class _WfSyncPasyncBaudRate_Type(Integer32):
    """Custom type wfSyncPasyncBaudRate based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(150,
              300,
              600,
              1200,
              2400,
              4800,
              7200,
              9600,
              12000,
              14400,
              19200,
              28800,
              38400,
              57600,
              64000,
              76800,
              96000,
              115200)
        )
    )
    namedValues = NamedValues(
        *(("baudrate115k", 115200),
          ("baudrate12000b", 12000),
          ("baudrate1200b", 1200),
          ("baudrate14400b", 14400),
          ("baudrate150b", 150),
          ("baudrate19200b", 19200),
          ("baudrate2400b", 2400),
          ("baudrate28800b", 28800),
          ("baudrate300b", 300),
          ("baudrate38k", 38400),
          ("baudrate4800b", 4800),
          ("baudrate56k", 57600),
          ("baudrate600b", 600),
          ("baudrate64k", 64000),
          ("baudrate7200b", 7200),
          ("baudrate76k", 76800),
          ("baudrate9600b", 9600),
          ("baudrate96k", 96000))
    )


_WfSyncPasyncBaudRate_Type.__name__ = "Integer32"
_WfSyncPasyncBaudRate_Object = MibTableColumn
wfSyncPasyncBaudRate = _WfSyncPasyncBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 119),
    _WfSyncPasyncBaudRate_Type()
)
wfSyncPasyncBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncPasyncBaudRate.setStatus("mandatory")


class _WfSyncLocalConnectionState_Type(Integer32):
    """Custom type wfSyncLocalConnectionState based on Integer32"""
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


_WfSyncLocalConnectionState_Type.__name__ = "Integer32"
_WfSyncLocalConnectionState_Object = MibTableColumn
wfSyncLocalConnectionState = _WfSyncLocalConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 120),
    _WfSyncLocalConnectionState_Type()
)
wfSyncLocalConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncLocalConnectionState.setStatus("mandatory")


class _WfSyncRemoteConnectionState_Type(Integer32):
    """Custom type wfSyncRemoteConnectionState based on Integer32"""
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


_WfSyncRemoteConnectionState_Type.__name__ = "Integer32"
_WfSyncRemoteConnectionState_Object = MibTableColumn
wfSyncRemoteConnectionState = _WfSyncRemoteConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 121),
    _WfSyncRemoteConnectionState_Type()
)
wfSyncRemoteConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncRemoteConnectionState.setStatus("mandatory")
_WfSyncTimeSlotAssignment_Type = DisplayString
_WfSyncTimeSlotAssignment_Object = MibTableColumn
wfSyncTimeSlotAssignment = _WfSyncTimeSlotAssignment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 122),
    _WfSyncTimeSlotAssignment_Type()
)
wfSyncTimeSlotAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncTimeSlotAssignment.setStatus("mandatory")


class _WfSyncEiaStatus_Type(Integer32):
    """Custom type wfSyncEiaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              65536,
              131072,
              262144,
              524288,
              1048576,
              2097152,
              4194304,
              8388608,
              16777216)
        )
    )
    namedValues = NamedValues(
        *(("cts", 8),
          ("ctsToggled", 524288),
          ("dcd", 32),
          ("dcdToggled", 2097152),
          ("dsr", 16),
          ("dsrToggled", 1048576),
          ("dtr", 256),
          ("dtrToggled", 16777216),
          ("rts", 4),
          ("rtsToggled", 262144),
          ("rxc", 128),
          ("rxcToggled", 8388608),
          ("rxd", 2),
          ("rxdToggled", 131072),
          ("txc", 64),
          ("txcToggled", 4194304),
          ("txd", 1),
          ("txdToggled", 65536))
    )


_WfSyncEiaStatus_Type.__name__ = "Integer32"
_WfSyncEiaStatus_Object = MibTableColumn
wfSyncEiaStatus = _WfSyncEiaStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 123),
    _WfSyncEiaStatus_Type()
)
wfSyncEiaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSyncEiaStatus.setStatus("mandatory")


class _WfSyncEiaStatusReset_Type(Integer32):
    """Custom type wfSyncEiaStatusReset based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              21)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 21),
          ("reset", 1))
    )


_WfSyncEiaStatusReset_Type.__name__ = "Integer32"
_WfSyncEiaStatusReset_Object = MibTableColumn
wfSyncEiaStatusReset = _WfSyncEiaStatusReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 124),
    _WfSyncEiaStatusReset_Type()
)
wfSyncEiaStatusReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncEiaStatusReset.setStatus("mandatory")


class _WfSyncUcastMap_Type(Integer32):
    """Custom type wfSyncUcastMap based on Integer32"""
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


_WfSyncUcastMap_Type.__name__ = "Integer32"
_WfSyncUcastMap_Object = MibTableColumn
wfSyncUcastMap = _WfSyncUcastMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 125),
    _WfSyncUcastMap_Type()
)
wfSyncUcastMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncUcastMap.setStatus("mandatory")


class _WfSyncAsyncCfgMaxIdleTimer_Type(Integer32):
    """Custom type wfSyncAsyncCfgMaxIdleTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("baudrate", 1),
          ("threechars", 2))
    )


_WfSyncAsyncCfgMaxIdleTimer_Type.__name__ = "Integer32"
_WfSyncAsyncCfgMaxIdleTimer_Object = MibTableColumn
wfSyncAsyncCfgMaxIdleTimer = _WfSyncAsyncCfgMaxIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 5, 1, 126),
    _WfSyncAsyncCfgMaxIdleTimer_Type()
)
wfSyncAsyncCfgMaxIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSyncAsyncCfgMaxIdleTimer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-SYNC-MIB",
    **{"wfSyncTable": wfSyncTable,
       "wfSyncEntry": wfSyncEntry,
       "wfSyncDelete": wfSyncDelete,
       "wfSyncDisable": wfSyncDisable,
       "wfSyncState": wfSyncState,
       "wfSyncSlot": wfSyncSlot,
       "wfSyncConnector": wfSyncConnector,
       "wfSyncCct": wfSyncCct,
       "wfSyncBofl": wfSyncBofl,
       "wfSyncBoflTmo": wfSyncBoflTmo,
       "wfSyncMtu": wfSyncMtu,
       "wfSyncMadr": wfSyncMadr,
       "wfSyncPromiscuous": wfSyncPromiscuous,
       "wfSyncXid": wfSyncXid,
       "wfSyncClkSource": wfSyncClkSource,
       "wfSyncClkSpeed": wfSyncClkSpeed,
       "wfSyncSignalMode": wfSyncSignalMode,
       "wfSyncRtsEnable": wfSyncRtsEnable,
       "wfSyncBurstCount": wfSyncBurstCount,
       "wfSyncService": wfSyncService,
       "wfSyncRetryCount": wfSyncRetryCount,
       "wfSyncLinkIdleTimer": wfSyncLinkIdleTimer,
       "wfSyncRetryTimer": wfSyncRetryTimer,
       "wfSyncExtendedAddress": wfSyncExtendedAddress,
       "wfSyncExtendedAddressForce": wfSyncExtendedAddressForce,
       "wfSyncExtendedControl": wfSyncExtendedControl,
       "wfSyncExtendedControlForce": wfSyncExtendedControlForce,
       "wfSyncConnectAttempts": wfSyncConnectAttempts,
       "wfSyncWindowSizeTx": wfSyncWindowSizeTx,
       "wfSyncWindowSizeTxExtc": wfSyncWindowSizeTxExtc,
       "wfSyncMinFrameSpace": wfSyncMinFrameSpace,
       "wfSyncLocalAddress": wfSyncLocalAddress,
       "wfSyncRemoteAddress": wfSyncRemoteAddress,
       "wfSyncPassThruLocalMadr": wfSyncPassThruLocalMadr,
       "wfSyncPassThruRemoteMadr": wfSyncPassThruRemoteMadr,
       "wfSyncWanProtocol": wfSyncWanProtocol,
       "wfSyncCrcSize": wfSyncCrcSize,
       "wfSyncRxOctets": wfSyncRxOctets,
       "wfSyncRxFrames": wfSyncRxFrames,
       "wfSyncTxOctets": wfSyncTxOctets,
       "wfSyncTxFrames": wfSyncTxFrames,
       "wfSyncRxErrors": wfSyncRxErrors,
       "wfSyncTxErrors": wfSyncTxErrors,
       "wfSyncLackRescRx": wfSyncLackRescRx,
       "wfSyncLackRescTx": wfSyncLackRescTx,
       "wfSyncUnderFlowTx": wfSyncUnderFlowTx,
       "wfSyncRejectsTx": wfSyncRejectsTx,
       "wfSyncRejectsRx": wfSyncRejectsRx,
       "wfSyncOverFlowRx": wfSyncOverFlowRx,
       "wfSyncFramesIncompRx": wfSyncFramesIncompRx,
       "wfSyncBadFramesRx": wfSyncBadFramesRx,
       "wfSyncFrameRejectsRx": wfSyncFrameRejectsRx,
       "wfSyncRuntsRx": wfSyncRuntsRx,
       "wfSyncT1Timeouts": wfSyncT1Timeouts,
       "wfSyncMemoryErrors": wfSyncMemoryErrors,
       "wfSyncMediaType": wfSyncMediaType,
       "wfSyncCfgTxQueueLength": wfSyncCfgTxQueueLength,
       "wfSyncCfgRxQueueLength": wfSyncCfgRxQueueLength,
       "wfSyncTxQueueLength": wfSyncTxQueueLength,
       "wfSyncRxQueueLength": wfSyncRxQueueLength,
       "wfSyncRxReplenMisses": wfSyncRxReplenMisses,
       "wfSyncStartUpMode": wfSyncStartUpMode,
       "wfSyncIdleRRFrames": wfSyncIdleRRFrames,
       "wfSyncMultilineMode": wfSyncMultilineMode,
       "wfSyncBODExamPeriod": wfSyncBODExamPeriod,
       "wfSyncBODFullThreshold": wfSyncBODFullThreshold,
       "wfSyncBODRecoverThreshold": wfSyncBODRecoverThreshold,
       "wfSyncBODPeriodsToFail": wfSyncBODPeriodsToFail,
       "wfSyncKG84ACycle": wfSyncKG84ACycle,
       "wfSyncKG84ASyncLossInterval": wfSyncKG84ASyncLossInterval,
       "wfSyncKG84ARemoteResyncWait": wfSyncKG84ARemoteResyncWait,
       "wfSyncKG84ASyncPulse": wfSyncKG84ASyncPulse,
       "wfSyncKG84AResyncs": wfSyncKG84AResyncs,
       "wfSyncKG84AResyncsDetected": wfSyncKG84AResyncsDetected,
       "wfSyncKG84ABsu": wfSyncKG84ABsu,
       "wfSyncKG84AState": wfSyncKG84AState,
       "wfSyncKG84AOkFrames": wfSyncKG84AOkFrames,
       "wfSyncPollingEnable": wfSyncPollingEnable,
       "wfSyncBackupPool": wfSyncBackupPool,
       "wfSyncDemandPool": wfSyncDemandPool,
       "wfSyncLineNumber": wfSyncLineNumber,
       "wfSyncHoldDownTime": wfSyncHoldDownTime,
       "wfSyncNetworkType": wfSyncNetworkType,
       "wfSyncActiveCct": wfSyncActiveCct,
       "wfSyncCableType": wfSyncCableType,
       "wfSyncRxDropPackets": wfSyncRxDropPackets,
       "wfSyncTxDropPackets": wfSyncTxDropPackets,
       "wfSyncModule": wfSyncModule,
       "wfSyncActualConnector": wfSyncActualConnector,
       "wfSyncLineCoding": wfSyncLineCoding,
       "wfSyncLastChange": wfSyncLastChange,
       "wfSyncOutQLen": wfSyncOutQLen,
       "wfSyncRemoteLpbkDetection": wfSyncRemoteLpbkDetection,
       "wfSyncLastState": wfSyncLastState,
       "wfSyncExternalClkSpeed": wfSyncExternalClkSpeed,
       "wfSyncBChannelOverride": wfSyncBChannelOverride,
       "wfSyncBChannel": wfSyncBChannel,
       "wfSyncForceIFTF": wfSyncForceIFTF,
       "wfSyncPriority": wfSyncPriority,
       "wfSyncTurboBofl": wfSyncTurboBofl,
       "wfSyncBoflNum": wfSyncBoflNum,
       "wfSyncBoflLen": wfSyncBoflLen,
       "wfSyncTurboBoflMisses": wfSyncTurboBoflMisses,
       "wfSyncTurboBoflInvocations": wfSyncTurboBoflInvocations,
       "wfSyncBandwidthOnDemandPool": wfSyncBandwidthOnDemandPool,
       "wfSyncBODRecoverPeriodsToPass": wfSyncBODRecoverPeriodsToPass,
       "wfSyncBODHistory": wfSyncBODHistory,
       "wfSyncBODDebugFlag": wfSyncBODDebugFlag,
       "wfSyncBChRateAdaption": wfSyncBChRateAdaption,
       "wfSyncBChActualRateAdaption": wfSyncBChActualRateAdaption,
       "wfSyncWanType": wfSyncWanType,
       "wfSyncAsyncBaudRate": wfSyncAsyncBaudRate,
       "wfSyncCfgAsyncCmndMaxIdles": wfSyncCfgAsyncCmndMaxIdles,
       "wfSyncAsyncCmndMaxIdles": wfSyncAsyncCmndMaxIdles,
       "wfSyncCfgAsyncDataMaxIdles": wfSyncCfgAsyncDataMaxIdles,
       "wfSyncAsyncDataMaxIdles": wfSyncAsyncDataMaxIdles,
       "wfSyncFramesAbortTx": wfSyncFramesAbortTx,
       "wfSyncPasyncParityType": wfSyncPasyncParityType,
       "wfSyncPasyncCharacterLength": wfSyncPasyncCharacterLength,
       "wfSyncPasyncStopLength": wfSyncPasyncStopLength,
       "wfSyncPasyncBaudRate": wfSyncPasyncBaudRate,
       "wfSyncLocalConnectionState": wfSyncLocalConnectionState,
       "wfSyncRemoteConnectionState": wfSyncRemoteConnectionState,
       "wfSyncTimeSlotAssignment": wfSyncTimeSlotAssignment,
       "wfSyncEiaStatus": wfSyncEiaStatus,
       "wfSyncEiaStatusReset": wfSyncEiaStatusReset,
       "wfSyncUcastMap": wfSyncUcastMap,
       "wfSyncAsyncCfgMaxIdleTimer": wfSyncAsyncCfgMaxIdleTimer}
)

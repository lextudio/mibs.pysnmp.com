# SNMP MIB module (Wellfleet-ASYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-ASYNC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:47 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

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

_WfAsyncTable_Object = MibTable
wfAsyncTable = _WfAsyncTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3)
)
if mibBuilder.loadTexts:
    wfAsyncTable.setStatus("mandatory")
_WfAsyncEntry_Object = MibTableRow
wfAsyncEntry = _WfAsyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1)
)
wfAsyncEntry.setIndexNames(
    (0, "Wellfleet-ASYNC-MIB", "wfAsyncSlot"),
    (0, "Wellfleet-ASYNC-MIB", "wfAsyncConnector"),
)
if mibBuilder.loadTexts:
    wfAsyncEntry.setStatus("mandatory")


class _WfAsyncDelete_Type(Integer32):
    """Custom type wfAsyncDelete based on Integer32"""
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


_WfAsyncDelete_Type.__name__ = "Integer32"
_WfAsyncDelete_Object = MibTableColumn
wfAsyncDelete = _WfAsyncDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 1),
    _WfAsyncDelete_Type()
)
wfAsyncDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncDelete.setStatus("mandatory")


class _WfAsyncDisable_Type(Integer32):
    """Custom type wfAsyncDisable based on Integer32"""
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


_WfAsyncDisable_Type.__name__ = "Integer32"
_WfAsyncDisable_Object = MibTableColumn
wfAsyncDisable = _WfAsyncDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 2),
    _WfAsyncDisable_Type()
)
wfAsyncDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncDisable.setStatus("mandatory")


class _WfAsyncState_Type(Integer32):
    """Custom type wfAsyncState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("dsrwait", 5),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfAsyncState_Type.__name__ = "Integer32"
_WfAsyncState_Object = MibTableColumn
wfAsyncState = _WfAsyncState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 3),
    _WfAsyncState_Type()
)
wfAsyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncState.setStatus("mandatory")
_WfAsyncSlot_Type = Integer32
_WfAsyncSlot_Object = MibTableColumn
wfAsyncSlot = _WfAsyncSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 4),
    _WfAsyncSlot_Type()
)
wfAsyncSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncSlot.setStatus("mandatory")


class _WfAsyncConnector_Type(Integer32):
    """Custom type wfAsyncConnector based on Integer32"""
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


_WfAsyncConnector_Type.__name__ = "Integer32"
_WfAsyncConnector_Object = MibTableColumn
wfAsyncConnector = _WfAsyncConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 5),
    _WfAsyncConnector_Type()
)
wfAsyncConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncConnector.setStatus("mandatory")


class _WfAsyncCct_Type(Integer32):
    """Custom type wfAsyncCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfAsyncCct_Type.__name__ = "Integer32"
_WfAsyncCct_Object = MibTableColumn
wfAsyncCct = _WfAsyncCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 6),
    _WfAsyncCct_Type()
)
wfAsyncCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncCct.setStatus("mandatory")


class _WfAsyncMtu_Type(Integer32):
    """Custom type wfAsyncMtu based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1580),
    )


_WfAsyncMtu_Type.__name__ = "Integer32"
_WfAsyncMtu_Object = MibTableColumn
wfAsyncMtu = _WfAsyncMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 7),
    _WfAsyncMtu_Type()
)
wfAsyncMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncMtu.setStatus("mandatory")
_WfAsyncMadr_Type = OctetString
_WfAsyncMadr_Object = MibTableColumn
wfAsyncMadr = _WfAsyncMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 8),
    _WfAsyncMadr_Type()
)
wfAsyncMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncMadr.setStatus("mandatory")


class _WfAsyncStartProtocol_Type(Integer32):
    """Custom type wfAsyncStartProtocol based on Integer32"""
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
        *(("answer", 3),
          ("loop", 1),
          ("originate", 2))
    )


_WfAsyncStartProtocol_Type.__name__ = "Integer32"
_WfAsyncStartProtocol_Object = MibTableColumn
wfAsyncStartProtocol = _WfAsyncStartProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 9),
    _WfAsyncStartProtocol_Type()
)
wfAsyncStartProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncStartProtocol.setStatus("mandatory")
_WfAsyncRxOctets_Type = Counter32
_WfAsyncRxOctets_Object = MibTableColumn
wfAsyncRxOctets = _WfAsyncRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 10),
    _WfAsyncRxOctets_Type()
)
wfAsyncRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncRxOctets.setStatus("mandatory")
_WfAsyncTxOctets_Type = Counter32
_WfAsyncTxOctets_Object = MibTableColumn
wfAsyncTxOctets = _WfAsyncTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 11),
    _WfAsyncTxOctets_Type()
)
wfAsyncTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncTxOctets.setStatus("mandatory")
_WfAsyncRxErrors_Type = Counter32
_WfAsyncRxErrors_Object = MibTableColumn
wfAsyncRxErrors = _WfAsyncRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 12),
    _WfAsyncRxErrors_Type()
)
wfAsyncRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncRxErrors.setStatus("mandatory")
_WfAsyncTxErrors_Type = Counter32
_WfAsyncTxErrors_Object = MibTableColumn
wfAsyncTxErrors = _WfAsyncTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 13),
    _WfAsyncTxErrors_Type()
)
wfAsyncTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncTxErrors.setStatus("mandatory")
_WfAsyncRxLackRescs_Type = Counter32
_WfAsyncRxLackRescs_Object = MibTableColumn
wfAsyncRxLackRescs = _WfAsyncRxLackRescs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 14),
    _WfAsyncRxLackRescs_Type()
)
wfAsyncRxLackRescs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncRxLackRescs.setStatus("mandatory")
_WfAsyncTxLackRescs_Type = Counter32
_WfAsyncTxLackRescs_Object = MibTableColumn
wfAsyncTxLackRescs = _WfAsyncTxLackRescs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 15),
    _WfAsyncTxLackRescs_Type()
)
wfAsyncTxLackRescs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncTxLackRescs.setStatus("mandatory")
_WfAsyncTxUnderFlows_Type = Counter32
_WfAsyncTxUnderFlows_Object = MibTableColumn
wfAsyncTxUnderFlows = _WfAsyncTxUnderFlows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 16),
    _WfAsyncTxUnderFlows_Type()
)
wfAsyncTxUnderFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncTxUnderFlows.setStatus("mandatory")
_WfAsyncTxRejects_Type = Counter32
_WfAsyncTxRejects_Object = MibTableColumn
wfAsyncTxRejects = _WfAsyncTxRejects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 17),
    _WfAsyncTxRejects_Type()
)
wfAsyncTxRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncTxRejects.setStatus("mandatory")
_WfAsyncRxRejects_Type = Counter32
_WfAsyncRxRejects_Object = MibTableColumn
wfAsyncRxRejects = _WfAsyncRxRejects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 18),
    _WfAsyncRxRejects_Type()
)
wfAsyncRxRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncRxRejects.setStatus("mandatory")
_WfAsyncRxOverFlows_Type = Counter32
_WfAsyncRxOverFlows_Object = MibTableColumn
wfAsyncRxOverFlows = _WfAsyncRxOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 19),
    _WfAsyncRxOverFlows_Type()
)
wfAsyncRxOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncRxOverFlows.setStatus("mandatory")
_WfAsyncRxBadOctets_Type = Counter32
_WfAsyncRxBadOctets_Object = MibTableColumn
wfAsyncRxBadOctets = _WfAsyncRxBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 20),
    _WfAsyncRxBadOctets_Type()
)
wfAsyncRxBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncRxBadOctets.setStatus("mandatory")
_WfAsyncRxRunts_Type = Counter32
_WfAsyncRxRunts_Object = MibTableColumn
wfAsyncRxRunts = _WfAsyncRxRunts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 21),
    _WfAsyncRxRunts_Type()
)
wfAsyncRxRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncRxRunts.setStatus("mandatory")
_WfAsyncTxQueueLength_Type = Integer32
_WfAsyncTxQueueLength_Object = MibTableColumn
wfAsyncTxQueueLength = _WfAsyncTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 22),
    _WfAsyncTxQueueLength_Type()
)
wfAsyncTxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncTxQueueLength.setStatus("mandatory")
_WfAsyncRxQueueLength_Type = Integer32
_WfAsyncRxQueueLength_Object = MibTableColumn
wfAsyncRxQueueLength = _WfAsyncRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 23),
    _WfAsyncRxQueueLength_Type()
)
wfAsyncRxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncRxQueueLength.setStatus("mandatory")
_WfAsyncRxReplenMisses_Type = Counter32
_WfAsyncRxReplenMisses_Object = MibTableColumn
wfAsyncRxReplenMisses = _WfAsyncRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 24),
    _WfAsyncRxReplenMisses_Type()
)
wfAsyncRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncRxReplenMisses.setStatus("mandatory")
_WfAsyncLineNumber_Type = Integer32
_WfAsyncLineNumber_Object = MibTableColumn
wfAsyncLineNumber = _WfAsyncLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 25),
    _WfAsyncLineNumber_Type()
)
wfAsyncLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncLineNumber.setStatus("mandatory")
_WfAsyncRemoteAddress_Type = IpAddress
_WfAsyncRemoteAddress_Object = MibTableColumn
wfAsyncRemoteAddress = _WfAsyncRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 26),
    _WfAsyncRemoteAddress_Type()
)
wfAsyncRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncRemoteAddress.setStatus("mandatory")


class _WfAsyncRemotePort_Type(Integer32):
    """Custom type wfAsyncRemotePort based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("port", 7)
    )


_WfAsyncRemotePort_Type.__name__ = "Integer32"
_WfAsyncRemotePort_Object = MibTableColumn
wfAsyncRemotePort = _WfAsyncRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 27),
    _WfAsyncRemotePort_Type()
)
wfAsyncRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncRemotePort.setStatus("mandatory")


class _WfAsyncLocalPort_Type(Integer32):
    """Custom type wfAsyncLocalPort based on Integer32"""
    defaultValue = 2100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2100
        )
    )
    namedValues = NamedValues(
        ("default", 2100)
    )


_WfAsyncLocalPort_Type.__name__ = "Integer32"
_WfAsyncLocalPort_Object = MibTableColumn
wfAsyncLocalPort = _WfAsyncLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 28),
    _WfAsyncLocalPort_Type()
)
wfAsyncLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncLocalPort.setStatus("mandatory")


class _WfAsyncBaud_Type(Integer32):
    """Custom type wfAsyncBaud based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("r1200", 1200),
          ("r19200", 19200),
          ("r2400", 2400),
          ("r300", 300),
          ("r4800", 4800),
          ("r9600", 9600))
    )


_WfAsyncBaud_Type.__name__ = "Integer32"
_WfAsyncBaud_Object = MibTableColumn
wfAsyncBaud = _WfAsyncBaud_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 29),
    _WfAsyncBaud_Type()
)
wfAsyncBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncBaud.setStatus("mandatory")


class _WfAsyncIdleTimer_Type(Integer32):
    """Custom type wfAsyncIdleTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_WfAsyncIdleTimer_Type.__name__ = "Integer32"
_WfAsyncIdleTimer_Object = MibTableColumn
wfAsyncIdleTimer = _WfAsyncIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 30),
    _WfAsyncIdleTimer_Type()
)
wfAsyncIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncIdleTimer.setStatus("mandatory")


class _WfAsyncRxWindow_Type(Integer32):
    """Custom type wfAsyncRxWindow based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 65535),
    )


_WfAsyncRxWindow_Type.__name__ = "Integer32"
_WfAsyncRxWindow_Object = MibTableColumn
wfAsyncRxWindow = _WfAsyncRxWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 31),
    _WfAsyncRxWindow_Type()
)
wfAsyncRxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncRxWindow.setStatus("mandatory")
_WfAsyncMinRxWindows_Type = Counter32
_WfAsyncMinRxWindows_Object = MibTableColumn
wfAsyncMinRxWindows = _WfAsyncMinRxWindows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 32),
    _WfAsyncMinRxWindows_Type()
)
wfAsyncMinRxWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAsyncMinRxWindows.setStatus("mandatory")
_WfASyncSecTxQmaxs_Type = Counter32
_WfASyncSecTxQmaxs_Object = MibTableColumn
wfASyncSecTxQmaxs = _WfASyncSecTxQmaxs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 33),
    _WfASyncSecTxQmaxs_Type()
)
wfASyncSecTxQmaxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfASyncSecTxQmaxs.setStatus("mandatory")
_WfASyncSecTxQlens_Type = Counter32
_WfASyncSecTxQlens_Object = MibTableColumn
wfASyncSecTxQlens = _WfASyncSecTxQlens_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 34),
    _WfASyncSecTxQlens_Type()
)
wfASyncSecTxQlens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfASyncSecTxQlens.setStatus("mandatory")


class _WfAsyncTCPKeepalive_Type(Integer32):
    """Custom type wfAsyncTCPKeepalive based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 180),
    )


_WfAsyncTCPKeepalive_Type.__name__ = "Integer32"
_WfAsyncTCPKeepalive_Object = MibTableColumn
wfAsyncTCPKeepalive = _WfAsyncTCPKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 35),
    _WfAsyncTCPKeepalive_Type()
)
wfAsyncTCPKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncTCPKeepalive.setStatus("mandatory")


class _WfAsyncTCPInactivityLimit_Type(Integer32):
    """Custom type wfAsyncTCPInactivityLimit based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_WfAsyncTCPInactivityLimit_Type.__name__ = "Integer32"
_WfAsyncTCPInactivityLimit_Object = MibTableColumn
wfAsyncTCPInactivityLimit = _WfAsyncTCPInactivityLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 36),
    _WfAsyncTCPInactivityLimit_Type()
)
wfAsyncTCPInactivityLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncTCPInactivityLimit.setStatus("mandatory")


class _WfAsyncCfgTxQueueLength_Type(Integer32):
    """Custom type wfAsyncCfgTxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAsyncCfgTxQueueLength_Type.__name__ = "Integer32"
_WfAsyncCfgTxQueueLength_Object = MibTableColumn
wfAsyncCfgTxQueueLength = _WfAsyncCfgTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 37),
    _WfAsyncCfgTxQueueLength_Type()
)
wfAsyncCfgTxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncCfgTxQueueLength.setStatus("mandatory")


class _WfAsyncCfgRxQueueLength_Type(Integer32):
    """Custom type wfAsyncCfgRxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAsyncCfgRxQueueLength_Type.__name__ = "Integer32"
_WfAsyncCfgRxQueueLength_Object = MibTableColumn
wfAsyncCfgRxQueueLength = _WfAsyncCfgRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 38),
    _WfAsyncCfgRxQueueLength_Type()
)
wfAsyncCfgRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAsyncCfgRxQueueLength.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-ASYNC-MIB",
    **{"wfAsyncTable": wfAsyncTable,
       "wfAsyncEntry": wfAsyncEntry,
       "wfAsyncDelete": wfAsyncDelete,
       "wfAsyncDisable": wfAsyncDisable,
       "wfAsyncState": wfAsyncState,
       "wfAsyncSlot": wfAsyncSlot,
       "wfAsyncConnector": wfAsyncConnector,
       "wfAsyncCct": wfAsyncCct,
       "wfAsyncMtu": wfAsyncMtu,
       "wfAsyncMadr": wfAsyncMadr,
       "wfAsyncStartProtocol": wfAsyncStartProtocol,
       "wfAsyncRxOctets": wfAsyncRxOctets,
       "wfAsyncTxOctets": wfAsyncTxOctets,
       "wfAsyncRxErrors": wfAsyncRxErrors,
       "wfAsyncTxErrors": wfAsyncTxErrors,
       "wfAsyncRxLackRescs": wfAsyncRxLackRescs,
       "wfAsyncTxLackRescs": wfAsyncTxLackRescs,
       "wfAsyncTxUnderFlows": wfAsyncTxUnderFlows,
       "wfAsyncTxRejects": wfAsyncTxRejects,
       "wfAsyncRxRejects": wfAsyncRxRejects,
       "wfAsyncRxOverFlows": wfAsyncRxOverFlows,
       "wfAsyncRxBadOctets": wfAsyncRxBadOctets,
       "wfAsyncRxRunts": wfAsyncRxRunts,
       "wfAsyncTxQueueLength": wfAsyncTxQueueLength,
       "wfAsyncRxQueueLength": wfAsyncRxQueueLength,
       "wfAsyncRxReplenMisses": wfAsyncRxReplenMisses,
       "wfAsyncLineNumber": wfAsyncLineNumber,
       "wfAsyncRemoteAddress": wfAsyncRemoteAddress,
       "wfAsyncRemotePort": wfAsyncRemotePort,
       "wfAsyncLocalPort": wfAsyncLocalPort,
       "wfAsyncBaud": wfAsyncBaud,
       "wfAsyncIdleTimer": wfAsyncIdleTimer,
       "wfAsyncRxWindow": wfAsyncRxWindow,
       "wfAsyncMinRxWindows": wfAsyncMinRxWindows,
       "wfASyncSecTxQmaxs": wfASyncSecTxQmaxs,
       "wfASyncSecTxQlens": wfASyncSecTxQlens,
       "wfAsyncTCPKeepalive": wfAsyncTCPKeepalive,
       "wfAsyncTCPInactivityLimit": wfAsyncTCPInactivityLimit,
       "wfAsyncCfgTxQueueLength": wfAsyncCfgTxQueueLength,
       "wfAsyncCfgRxQueueLength": wfAsyncCfgRxQueueLength}
)

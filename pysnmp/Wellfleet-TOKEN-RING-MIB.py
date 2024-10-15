# SNMP MIB module (Wellfleet-TOKEN-RING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-TOKEN-RING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:21 2024
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

_WfTokenRingTable_Object = MibTable
wfTokenRingTable = _WfTokenRingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2)
)
if mibBuilder.loadTexts:
    wfTokenRingTable.setStatus("mandatory")
_WfTokenRingEntry_Object = MibTableRow
wfTokenRingEntry = _WfTokenRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1)
)
wfTokenRingEntry.setIndexNames(
    (0, "Wellfleet-TOKEN-RING-MIB", "wfTokenRingSlot"),
    (0, "Wellfleet-TOKEN-RING-MIB", "wfTokenRingConnector"),
)
if mibBuilder.loadTexts:
    wfTokenRingEntry.setStatus("mandatory")


class _WfTokenRingDelete_Type(Integer32):
    """Custom type wfTokenRingDelete based on Integer32"""
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


_WfTokenRingDelete_Type.__name__ = "Integer32"
_WfTokenRingDelete_Object = MibTableColumn
wfTokenRingDelete = _WfTokenRingDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 1),
    _WfTokenRingDelete_Type()
)
wfTokenRingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingDelete.setStatus("mandatory")


class _WfTokenRingDisable_Type(Integer32):
    """Custom type wfTokenRingDisable based on Integer32"""
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


_WfTokenRingDisable_Type.__name__ = "Integer32"
_WfTokenRingDisable_Object = MibTableColumn
wfTokenRingDisable = _WfTokenRingDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 2),
    _WfTokenRingDisable_Type()
)
wfTokenRingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingDisable.setStatus("mandatory")


class _WfTokenRingState_Type(Integer32):
    """Custom type wfTokenRingState based on Integer32"""
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


_WfTokenRingState_Type.__name__ = "Integer32"
_WfTokenRingState_Object = MibTableColumn
wfTokenRingState = _WfTokenRingState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 3),
    _WfTokenRingState_Type()
)
wfTokenRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingState.setStatus("mandatory")
_WfTokenRingSlot_Type = Integer32
_WfTokenRingSlot_Object = MibTableColumn
wfTokenRingSlot = _WfTokenRingSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 4),
    _WfTokenRingSlot_Type()
)
wfTokenRingSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingSlot.setStatus("mandatory")
_WfTokenRingConnector_Type = Integer32
_WfTokenRingConnector_Object = MibTableColumn
wfTokenRingConnector = _WfTokenRingConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 5),
    _WfTokenRingConnector_Type()
)
wfTokenRingConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingConnector.setStatus("mandatory")


class _WfTokenRingCct_Type(Integer32):
    """Custom type wfTokenRingCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfTokenRingCct_Type.__name__ = "Integer32"
_WfTokenRingCct_Object = MibTableColumn
wfTokenRingCct = _WfTokenRingCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 6),
    _WfTokenRingCct_Type()
)
wfTokenRingCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingCct.setStatus("mandatory")


class _WfTokenRingMtu_Type(Integer32):
    """Custom type wfTokenRingMtu based on Integer32"""
    defaultValue = 4568

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4568
        )
    )
    namedValues = NamedValues(
        ("default", 4568)
    )


_WfTokenRingMtu_Type.__name__ = "Integer32"
_WfTokenRingMtu_Object = MibTableColumn
wfTokenRingMtu = _WfTokenRingMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 7),
    _WfTokenRingMtu_Type()
)
wfTokenRingMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingMtu.setStatus("mandatory")
_WfTokenRingMadr_Type = OctetString
_WfTokenRingMadr_Object = MibTableColumn
wfTokenRingMadr = _WfTokenRingMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 8),
    _WfTokenRingMadr_Type()
)
wfTokenRingMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingMadr.setStatus("mandatory")
_WfTokenRingCfgMadr_Type = OctetString
_WfTokenRingCfgMadr_Object = MibTableColumn
wfTokenRingCfgMadr = _WfTokenRingCfgMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 9),
    _WfTokenRingCfgMadr_Type()
)
wfTokenRingCfgMadr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingCfgMadr.setStatus("mandatory")


class _WfTokenRingMadrSelect_Type(Integer32):
    """Custom type wfTokenRingMadrSelect based on Integer32"""
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
        *(("boxwide", 1),
          ("cnfg", 3),
          ("prom", 2))
    )


_WfTokenRingMadrSelect_Type.__name__ = "Integer32"
_WfTokenRingMadrSelect_Object = MibTableColumn
wfTokenRingMadrSelect = _WfTokenRingMadrSelect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 10),
    _WfTokenRingMadrSelect_Type()
)
wfTokenRingMadrSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingMadrSelect.setStatus("mandatory")


class _WfTokenRingSpeed_Type(Integer32):
    """Custom type wfTokenRingSpeed based on Integer32"""
    defaultValue = 16777216

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4194304,
              16777216)
        )
    )
    namedValues = NamedValues(
        *(("mbps16", 16777216),
          ("mbps4", 4194304))
    )


_WfTokenRingSpeed_Type.__name__ = "Integer32"
_WfTokenRingSpeed_Object = MibTableColumn
wfTokenRingSpeed = _WfTokenRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 11),
    _WfTokenRingSpeed_Type()
)
wfTokenRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingSpeed.setStatus("mandatory")


class _WfTokenRingEarlyTokenRelease_Type(Integer32):
    """Custom type wfTokenRingEarlyTokenRelease based on Integer32"""
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


_WfTokenRingEarlyTokenRelease_Type.__name__ = "Integer32"
_WfTokenRingEarlyTokenRelease_Object = MibTableColumn
wfTokenRingEarlyTokenRelease = _WfTokenRingEarlyTokenRelease_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 12),
    _WfTokenRingEarlyTokenRelease_Type()
)
wfTokenRingEarlyTokenRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingEarlyTokenRelease.setStatus("mandatory")
_WfTokenRingStatus_Type = Integer32
_WfTokenRingStatus_Object = MibTableColumn
wfTokenRingStatus = _WfTokenRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 13),
    _WfTokenRingStatus_Type()
)
wfTokenRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingStatus.setStatus("mandatory")


class _WfTokenRingOpenState_Type(Integer32):
    """Custom type wfTokenRingOpenState based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("closed", 6),
          ("closing", 3),
          ("opened", 1),
          ("openfailure", 4),
          ("opening", 2),
          ("ringfailure", 5))
    )


_WfTokenRingOpenState_Type.__name__ = "Integer32"
_WfTokenRingOpenState_Object = MibTableColumn
wfTokenRingOpenState = _WfTokenRingOpenState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 14),
    _WfTokenRingOpenState_Type()
)
wfTokenRingOpenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingOpenState.setStatus("mandatory")


class _WfTokenRingOpenStatus_Type(Integer32):
    """Custom type wfTokenRingOpenStatus based on Integer32"""
    defaultValue = 12

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
        *(("badparam", 2),
          ("beaconing", 7),
          ("duplicatemac", 8),
          ("insertiontimeout", 5),
          ("lobefailed", 3),
          ("noopen", 12),
          ("open", 1),
          ("removereceived", 10),
          ("requestfailed", 9),
          ("ringfailed", 6),
          ("signalloss", 4),
          ("unkerror", 11))
    )


_WfTokenRingOpenStatus_Type.__name__ = "Integer32"
_WfTokenRingOpenStatus_Object = MibTableColumn
wfTokenRingOpenStatus = _WfTokenRingOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 15),
    _WfTokenRingOpenStatus_Type()
)
wfTokenRingOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingOpenStatus.setStatus("mandatory")
_WfTokenRingUpStream_Type = OctetString
_WfTokenRingUpStream_Object = MibTableColumn
wfTokenRingUpStream = _WfTokenRingUpStream_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 16),
    _WfTokenRingUpStream_Type()
)
wfTokenRingUpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingUpStream.setStatus("mandatory")
_WfTokenRingRxOctets_Type = Counter32
_WfTokenRingRxOctets_Object = MibTableColumn
wfTokenRingRxOctets = _WfTokenRingRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 17),
    _WfTokenRingRxOctets_Type()
)
wfTokenRingRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxOctets.setStatus("mandatory")
_WfTokenRingRxFrames_Type = Counter32
_WfTokenRingRxFrames_Object = MibTableColumn
wfTokenRingRxFrames = _WfTokenRingRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 18),
    _WfTokenRingRxFrames_Type()
)
wfTokenRingRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxFrames.setStatus("mandatory")
_WfTokenRingTxOctets_Type = Counter32
_WfTokenRingTxOctets_Object = MibTableColumn
wfTokenRingTxOctets = _WfTokenRingTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 19),
    _WfTokenRingTxOctets_Type()
)
wfTokenRingTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTxOctets.setStatus("mandatory")
_WfTokenRingTxFrames_Type = Counter32
_WfTokenRingTxFrames_Object = MibTableColumn
wfTokenRingTxFrames = _WfTokenRingTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 20),
    _WfTokenRingTxFrames_Type()
)
wfTokenRingTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTxFrames.setStatus("mandatory")
_WfTokenRingInDiscards_Type = Counter32
_WfTokenRingInDiscards_Object = MibTableColumn
wfTokenRingInDiscards = _WfTokenRingInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 21),
    _WfTokenRingInDiscards_Type()
)
wfTokenRingInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingInDiscards.setStatus("mandatory")
_WfTokenRingInErrors_Type = Counter32
_WfTokenRingInErrors_Object = MibTableColumn
wfTokenRingInErrors = _WfTokenRingInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 22),
    _WfTokenRingInErrors_Type()
)
wfTokenRingInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingInErrors.setStatus("mandatory")
_WfTokenRingOutDiscards_Type = Counter32
_WfTokenRingOutDiscards_Object = MibTableColumn
wfTokenRingOutDiscards = _WfTokenRingOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 23),
    _WfTokenRingOutDiscards_Type()
)
wfTokenRingOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingOutDiscards.setStatus("mandatory")
_WfTokenRingOutErrors_Type = Counter32
_WfTokenRingOutErrors_Object = MibTableColumn
wfTokenRingOutErrors = _WfTokenRingOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 24),
    _WfTokenRingOutErrors_Type()
)
wfTokenRingOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingOutErrors.setStatus("mandatory")
_WfTokenRingTxClipFrames_Type = Counter32
_WfTokenRingTxClipFrames_Object = MibTableColumn
wfTokenRingTxClipFrames = _WfTokenRingTxClipFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 25),
    _WfTokenRingTxClipFrames_Type()
)
wfTokenRingTxClipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTxClipFrames.setStatus("mandatory")
_WfTokenRingRxReplenMisses_Type = Counter32
_WfTokenRingRxReplenMisses_Object = MibTableColumn
wfTokenRingRxReplenMisses = _WfTokenRingRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 26),
    _WfTokenRingRxReplenMisses_Type()
)
wfTokenRingRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxReplenMisses.setStatus("mandatory")
_WfTokenRingSignalLosses_Type = Counter32
_WfTokenRingSignalLosses_Object = MibTableColumn
wfTokenRingSignalLosses = _WfTokenRingSignalLosses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 27),
    _WfTokenRingSignalLosses_Type()
)
wfTokenRingSignalLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingSignalLosses.setStatus("mandatory")
_WfTokenRingHardErrors_Type = Counter32
_WfTokenRingHardErrors_Object = MibTableColumn
wfTokenRingHardErrors = _WfTokenRingHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 28),
    _WfTokenRingHardErrors_Type()
)
wfTokenRingHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingHardErrors.setStatus("mandatory")
_WfTokenRingSoftErrors_Type = Counter32
_WfTokenRingSoftErrors_Object = MibTableColumn
wfTokenRingSoftErrors = _WfTokenRingSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 29),
    _WfTokenRingSoftErrors_Type()
)
wfTokenRingSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingSoftErrors.setStatus("mandatory")
_WfTokenRingTransmitBeacons_Type = Counter32
_WfTokenRingTransmitBeacons_Object = MibTableColumn
wfTokenRingTransmitBeacons = _WfTokenRingTransmitBeacons_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 30),
    _WfTokenRingTransmitBeacons_Type()
)
wfTokenRingTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTransmitBeacons.setStatus("mandatory")
_WfTokenRingLobeWireFaults_Type = Counter32
_WfTokenRingLobeWireFaults_Object = MibTableColumn
wfTokenRingLobeWireFaults = _WfTokenRingLobeWireFaults_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 31),
    _WfTokenRingLobeWireFaults_Type()
)
wfTokenRingLobeWireFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingLobeWireFaults.setStatus("mandatory")
_WfTokenRingAutoRemovalErrors_Type = Counter32
_WfTokenRingAutoRemovalErrors_Object = MibTableColumn
wfTokenRingAutoRemovalErrors = _WfTokenRingAutoRemovalErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 32),
    _WfTokenRingAutoRemovalErrors_Type()
)
wfTokenRingAutoRemovalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingAutoRemovalErrors.setStatus("mandatory")
_WfTokenRingRequestRemoves_Type = Counter32
_WfTokenRingRequestRemoves_Object = MibTableColumn
wfTokenRingRequestRemoves = _WfTokenRingRequestRemoves_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 33),
    _WfTokenRingRequestRemoves_Type()
)
wfTokenRingRequestRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRequestRemoves.setStatus("mandatory")
_WfTokenRingCounterOverflows_Type = Counter32
_WfTokenRingCounterOverflows_Object = MibTableColumn
wfTokenRingCounterOverflows = _WfTokenRingCounterOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 34),
    _WfTokenRingCounterOverflows_Type()
)
wfTokenRingCounterOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingCounterOverflows.setStatus("mandatory")
_WfTokenRingSingleStations_Type = Counter32
_WfTokenRingSingleStations_Object = MibTableColumn
wfTokenRingSingleStations = _WfTokenRingSingleStations_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 35),
    _WfTokenRingSingleStations_Type()
)
wfTokenRingSingleStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingSingleStations.setStatus("mandatory")
_WfTokenRingRingRecoveries_Type = Counter32
_WfTokenRingRingRecoveries_Object = MibTableColumn
wfTokenRingRingRecoveries = _WfTokenRingRingRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 36),
    _WfTokenRingRingRecoveries_Type()
)
wfTokenRingRingRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRingRecoveries.setStatus("mandatory")
_WfTokenRingAdapterChecks_Type = Counter32
_WfTokenRingAdapterChecks_Object = MibTableColumn
wfTokenRingAdapterChecks = _WfTokenRingAdapterChecks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 37),
    _WfTokenRingAdapterChecks_Type()
)
wfTokenRingAdapterChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingAdapterChecks.setStatus("mandatory")
_WfTokenRingFirstAdapterCheckCode_Type = Integer32
_WfTokenRingFirstAdapterCheckCode_Object = MibTableColumn
wfTokenRingFirstAdapterCheckCode = _WfTokenRingFirstAdapterCheckCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 38),
    _WfTokenRingFirstAdapterCheckCode_Type()
)
wfTokenRingFirstAdapterCheckCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingFirstAdapterCheckCode.setStatus("mandatory")
_WfTokenRingLastAdapterCheckCode_Type = Integer32
_WfTokenRingLastAdapterCheckCode_Object = MibTableColumn
wfTokenRingLastAdapterCheckCode = _WfTokenRingLastAdapterCheckCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 39),
    _WfTokenRingLastAdapterCheckCode_Type()
)
wfTokenRingLastAdapterCheckCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingLastAdapterCheckCode.setStatus("mandatory")
_WfTokenRingLineErrors_Type = Counter32
_WfTokenRingLineErrors_Object = MibTableColumn
wfTokenRingLineErrors = _WfTokenRingLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 40),
    _WfTokenRingLineErrors_Type()
)
wfTokenRingLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingLineErrors.setStatus("mandatory")
_WfTokenRingBurstErrors_Type = Counter32
_WfTokenRingBurstErrors_Object = MibTableColumn
wfTokenRingBurstErrors = _WfTokenRingBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 41),
    _WfTokenRingBurstErrors_Type()
)
wfTokenRingBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingBurstErrors.setStatus("mandatory")
_WfTokenRingAriFciErrors_Type = Counter32
_WfTokenRingAriFciErrors_Object = MibTableColumn
wfTokenRingAriFciErrors = _WfTokenRingAriFciErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 42),
    _WfTokenRingAriFciErrors_Type()
)
wfTokenRingAriFciErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingAriFciErrors.setStatus("mandatory")
_WfTokenRingLostFrameErrors_Type = Counter32
_WfTokenRingLostFrameErrors_Object = MibTableColumn
wfTokenRingLostFrameErrors = _WfTokenRingLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 43),
    _WfTokenRingLostFrameErrors_Type()
)
wfTokenRingLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingLostFrameErrors.setStatus("mandatory")
_WfTokenRingRxCongestionErrors_Type = Counter32
_WfTokenRingRxCongestionErrors_Object = MibTableColumn
wfTokenRingRxCongestionErrors = _WfTokenRingRxCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 44),
    _WfTokenRingRxCongestionErrors_Type()
)
wfTokenRingRxCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxCongestionErrors.setStatus("mandatory")
_WfTokenRingFrameCopiedErrors_Type = Counter32
_WfTokenRingFrameCopiedErrors_Object = MibTableColumn
wfTokenRingFrameCopiedErrors = _WfTokenRingFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 45),
    _WfTokenRingFrameCopiedErrors_Type()
)
wfTokenRingFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingFrameCopiedErrors.setStatus("mandatory")
_WfTokenRingTokenErrors_Type = Counter32
_WfTokenRingTokenErrors_Object = MibTableColumn
wfTokenRingTokenErrors = _WfTokenRingTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 46),
    _WfTokenRingTokenErrors_Type()
)
wfTokenRingTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTokenErrors.setStatus("mandatory")
_WfTokenRingDmaBusErrors_Type = Counter32
_WfTokenRingDmaBusErrors_Object = MibTableColumn
wfTokenRingDmaBusErrors = _WfTokenRingDmaBusErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 47),
    _WfTokenRingDmaBusErrors_Type()
)
wfTokenRingDmaBusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingDmaBusErrors.setStatus("mandatory")
_WfTokenRingDmaParityErrors_Type = Counter32
_WfTokenRingDmaParityErrors_Object = MibTableColumn
wfTokenRingDmaParityErrors = _WfTokenRingDmaParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 48),
    _WfTokenRingDmaParityErrors_Type()
)
wfTokenRingDmaParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingDmaParityErrors.setStatus("mandatory")
_WfTokenRingSrbNotFreeCmdAborts_Type = Counter32
_WfTokenRingSrbNotFreeCmdAborts_Object = MibTableColumn
wfTokenRingSrbNotFreeCmdAborts = _WfTokenRingSrbNotFreeCmdAborts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 49),
    _WfTokenRingSrbNotFreeCmdAborts_Type()
)
wfTokenRingSrbNotFreeCmdAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingSrbNotFreeCmdAborts.setStatus("mandatory")
_WfTokenRingRxProcessings_Type = Counter32
_WfTokenRingRxProcessings_Object = MibTableColumn
wfTokenRingRxProcessings = _WfTokenRingRxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 50),
    _WfTokenRingRxProcessings_Type()
)
wfTokenRingRxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxProcessings.setStatus("mandatory")
_WfTokenRingTxProcessings_Type = Counter32
_WfTokenRingTxProcessings_Object = MibTableColumn
wfTokenRingTxProcessings = _WfTokenRingTxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 51),
    _WfTokenRingTxProcessings_Type()
)
wfTokenRingTxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTxProcessings.setStatus("mandatory")
_WfTokenRingTxCmplProcessings_Type = Counter32
_WfTokenRingTxCmplProcessings_Object = MibTableColumn
wfTokenRingTxCmplProcessings = _WfTokenRingTxCmplProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 52),
    _WfTokenRingTxCmplProcessings_Type()
)
wfTokenRingTxCmplProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTxCmplProcessings.setStatus("mandatory")
_WfTokenRingRxTimeouts_Type = Counter32
_WfTokenRingRxTimeouts_Object = MibTableColumn
wfTokenRingRxTimeouts = _WfTokenRingRxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 53),
    _WfTokenRingRxTimeouts_Type()
)
wfTokenRingRxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxTimeouts.setStatus("mandatory")
_WfTokenRingCmdTimeouts_Type = Counter32
_WfTokenRingCmdTimeouts_Object = MibTableColumn
wfTokenRingCmdTimeouts = _WfTokenRingCmdTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 54),
    _WfTokenRingCmdTimeouts_Type()
)
wfTokenRingCmdTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingCmdTimeouts.setStatus("mandatory")
_WfTokenRingRxHostIntErrors_Type = Counter32
_WfTokenRingRxHostIntErrors_Object = MibTableColumn
wfTokenRingRxHostIntErrors = _WfTokenRingRxHostIntErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 55),
    _WfTokenRingRxHostIntErrors_Type()
)
wfTokenRingRxHostIntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxHostIntErrors.setStatus("mandatory")
_WfTokenRingRxTxBufferSize_Type = Integer32
_WfTokenRingRxTxBufferSize_Object = MibTableColumn
wfTokenRingRxTxBufferSize = _WfTokenRingRxTxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 56),
    _WfTokenRingRxTxBufferSize_Type()
)
wfTokenRingRxTxBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxTxBufferSize.setStatus("mandatory")


class _WfTokenRingCfgTxQueueLength_Type(Integer32):
    """Custom type wfTokenRingCfgTxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfTokenRingCfgTxQueueLength_Type.__name__ = "Integer32"
_WfTokenRingCfgTxQueueLength_Object = MibTableColumn
wfTokenRingCfgTxQueueLength = _WfTokenRingCfgTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 57),
    _WfTokenRingCfgTxQueueLength_Type()
)
wfTokenRingCfgTxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingCfgTxQueueLength.setStatus("mandatory")


class _WfTokenRingCfgRxQueueLength_Type(Integer32):
    """Custom type wfTokenRingCfgRxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfTokenRingCfgRxQueueLength_Type.__name__ = "Integer32"
_WfTokenRingCfgRxQueueLength_Object = MibTableColumn
wfTokenRingCfgRxQueueLength = _WfTokenRingCfgRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 58),
    _WfTokenRingCfgRxQueueLength_Type()
)
wfTokenRingCfgRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingCfgRxQueueLength.setStatus("mandatory")
_WfTokenRingTxQueueLength_Type = Integer32
_WfTokenRingTxQueueLength_Object = MibTableColumn
wfTokenRingTxQueueLength = _WfTokenRingTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 59),
    _WfTokenRingTxQueueLength_Type()
)
wfTokenRingTxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingTxQueueLength.setStatus("mandatory")
_WfTokenRingRxQueueLength_Type = Integer32
_WfTokenRingRxQueueLength_Object = MibTableColumn
wfTokenRingRxQueueLength = _WfTokenRingRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 60),
    _WfTokenRingRxQueueLength_Type()
)
wfTokenRingRxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingRxQueueLength.setStatus("mandatory")
_WfTokenRingMacRxOctets_Type = Counter32
_WfTokenRingMacRxOctets_Object = MibTableColumn
wfTokenRingMacRxOctets = _WfTokenRingMacRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 61),
    _WfTokenRingMacRxOctets_Type()
)
wfTokenRingMacRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingMacRxOctets.setStatus("mandatory")
_WfTokenRingMacRxFrames_Type = Counter32
_WfTokenRingMacRxFrames_Object = MibTableColumn
wfTokenRingMacRxFrames = _WfTokenRingMacRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 62),
    _WfTokenRingMacRxFrames_Type()
)
wfTokenRingMacRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingMacRxFrames.setStatus("mandatory")


class _WfTokenRingCfgFunctionalAddress_Type(Integer32):
    """Custom type wfTokenRingCfgFunctionalAddress based on Integer32"""
    defaultValue = 2147467520

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2147467520
        )
    )
    namedValues = NamedValues(
        ("mask", 2147467520)
    )


_WfTokenRingCfgFunctionalAddress_Type.__name__ = "Integer32"
_WfTokenRingCfgFunctionalAddress_Object = MibTableColumn
wfTokenRingCfgFunctionalAddress = _WfTokenRingCfgFunctionalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 63),
    _WfTokenRingCfgFunctionalAddress_Type()
)
wfTokenRingCfgFunctionalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingCfgFunctionalAddress.setStatus("mandatory")
_WfTokenRingFunctionalAddress_Type = Integer32
_WfTokenRingFunctionalAddress_Object = MibTableColumn
wfTokenRingFunctionalAddress = _WfTokenRingFunctionalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 64),
    _WfTokenRingFunctionalAddress_Type()
)
wfTokenRingFunctionalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingFunctionalAddress.setStatus("mandatory")
_WfTokenRingGroupAddress_Type = Integer32
_WfTokenRingGroupAddress_Object = MibTableColumn
wfTokenRingGroupAddress = _WfTokenRingGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 65),
    _WfTokenRingGroupAddress_Type()
)
wfTokenRingGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingGroupAddress.setStatus("mandatory")
_WfTokenRingLineNumber_Type = Integer32
_WfTokenRingLineNumber_Object = MibTableColumn
wfTokenRingLineNumber = _WfTokenRingLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 66),
    _WfTokenRingLineNumber_Type()
)
wfTokenRingLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingLineNumber.setStatus("mandatory")
_WfTokenRingMacCode_Type = DisplayString
_WfTokenRingMacCode_Object = MibTableColumn
wfTokenRingMacCode = _WfTokenRingMacCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 67),
    _WfTokenRingMacCode_Type()
)
wfTokenRingMacCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingMacCode.setStatus("mandatory")


class _WfTokenRingModule_Type(Integer32):
    """Custom type wfTokenRingModule based on Integer32"""
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


_WfTokenRingModule_Type.__name__ = "Integer32"
_WfTokenRingModule_Object = MibTableColumn
wfTokenRingModule = _WfTokenRingModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 68),
    _WfTokenRingModule_Type()
)
wfTokenRingModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingModule.setStatus("mandatory")


class _WfTokenRingActualConnector_Type(Integer32):
    """Custom type wfTokenRingActualConnector based on Integer32"""
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


_WfTokenRingActualConnector_Type.__name__ = "Integer32"
_WfTokenRingActualConnector_Object = MibTableColumn
wfTokenRingActualConnector = _WfTokenRingActualConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 69),
    _WfTokenRingActualConnector_Type()
)
wfTokenRingActualConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingActualConnector.setStatus("mandatory")
_WfTokenRingLastChange_Type = TimeTicks
_WfTokenRingLastChange_Object = MibTableColumn
wfTokenRingLastChange = _WfTokenRingLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 70),
    _WfTokenRingLastChange_Type()
)
wfTokenRingLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingLastChange.setStatus("mandatory")
_WfTokenRingOutQLen_Type = Gauge32
_WfTokenRingOutQLen_Object = MibTableColumn
wfTokenRingOutQLen = _WfTokenRingOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 71),
    _WfTokenRingOutQLen_Type()
)
wfTokenRingOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingOutQLen.setStatus("mandatory")


class _WfTokenRingForceMacCode_Type(Integer32):
    """Custom type wfTokenRingForceMacCode based on Integer32"""
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
        *(("fastmac", 2),
          ("fastmacplus", 3),
          ("fastmacplusb", 4),
          ("timac", 1))
    )


_WfTokenRingForceMacCode_Type.__name__ = "Integer32"
_WfTokenRingForceMacCode_Object = MibTableColumn
wfTokenRingForceMacCode = _WfTokenRingForceMacCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 72),
    _WfTokenRingForceMacCode_Type()
)
wfTokenRingForceMacCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingForceMacCode.setStatus("mandatory")
_WfTokenRingMSBMadr_Type = OctetString
_WfTokenRingMSBMadr_Object = MibTableColumn
wfTokenRingMSBMadr = _WfTokenRingMSBMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 73),
    _WfTokenRingMSBMadr_Type()
)
wfTokenRingMSBMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTokenRingMSBMadr.setStatus("mandatory")


class _WfTokenRingTurboBoflDebug_Type(Integer32):
    """Custom type wfTokenRingTurboBoflDebug based on Integer32"""
    defaultValue = 0


_WfTokenRingTurboBoflDebug_Object = MibTableColumn
wfTokenRingTurboBoflDebug = _WfTokenRingTurboBoflDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 74),
    _WfTokenRingTurboBoflDebug_Type()
)
wfTokenRingTurboBoflDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingTurboBoflDebug.setStatus("mandatory")


class _WfTokenRingSingleStatDis_Type(Integer32):
    """Custom type wfTokenRingSingleStatDis based on Integer32"""
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


_WfTokenRingSingleStatDis_Type.__name__ = "Integer32"
_WfTokenRingSingleStatDis_Object = MibTableColumn
wfTokenRingSingleStatDis = _WfTokenRingSingleStatDis_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 2, 1, 75),
    _WfTokenRingSingleStatDis_Type()
)
wfTokenRingSingleStatDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTokenRingSingleStatDis.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-TOKEN-RING-MIB",
    **{"wfTokenRingTable": wfTokenRingTable,
       "wfTokenRingEntry": wfTokenRingEntry,
       "wfTokenRingDelete": wfTokenRingDelete,
       "wfTokenRingDisable": wfTokenRingDisable,
       "wfTokenRingState": wfTokenRingState,
       "wfTokenRingSlot": wfTokenRingSlot,
       "wfTokenRingConnector": wfTokenRingConnector,
       "wfTokenRingCct": wfTokenRingCct,
       "wfTokenRingMtu": wfTokenRingMtu,
       "wfTokenRingMadr": wfTokenRingMadr,
       "wfTokenRingCfgMadr": wfTokenRingCfgMadr,
       "wfTokenRingMadrSelect": wfTokenRingMadrSelect,
       "wfTokenRingSpeed": wfTokenRingSpeed,
       "wfTokenRingEarlyTokenRelease": wfTokenRingEarlyTokenRelease,
       "wfTokenRingStatus": wfTokenRingStatus,
       "wfTokenRingOpenState": wfTokenRingOpenState,
       "wfTokenRingOpenStatus": wfTokenRingOpenStatus,
       "wfTokenRingUpStream": wfTokenRingUpStream,
       "wfTokenRingRxOctets": wfTokenRingRxOctets,
       "wfTokenRingRxFrames": wfTokenRingRxFrames,
       "wfTokenRingTxOctets": wfTokenRingTxOctets,
       "wfTokenRingTxFrames": wfTokenRingTxFrames,
       "wfTokenRingInDiscards": wfTokenRingInDiscards,
       "wfTokenRingInErrors": wfTokenRingInErrors,
       "wfTokenRingOutDiscards": wfTokenRingOutDiscards,
       "wfTokenRingOutErrors": wfTokenRingOutErrors,
       "wfTokenRingTxClipFrames": wfTokenRingTxClipFrames,
       "wfTokenRingRxReplenMisses": wfTokenRingRxReplenMisses,
       "wfTokenRingSignalLosses": wfTokenRingSignalLosses,
       "wfTokenRingHardErrors": wfTokenRingHardErrors,
       "wfTokenRingSoftErrors": wfTokenRingSoftErrors,
       "wfTokenRingTransmitBeacons": wfTokenRingTransmitBeacons,
       "wfTokenRingLobeWireFaults": wfTokenRingLobeWireFaults,
       "wfTokenRingAutoRemovalErrors": wfTokenRingAutoRemovalErrors,
       "wfTokenRingRequestRemoves": wfTokenRingRequestRemoves,
       "wfTokenRingCounterOverflows": wfTokenRingCounterOverflows,
       "wfTokenRingSingleStations": wfTokenRingSingleStations,
       "wfTokenRingRingRecoveries": wfTokenRingRingRecoveries,
       "wfTokenRingAdapterChecks": wfTokenRingAdapterChecks,
       "wfTokenRingFirstAdapterCheckCode": wfTokenRingFirstAdapterCheckCode,
       "wfTokenRingLastAdapterCheckCode": wfTokenRingLastAdapterCheckCode,
       "wfTokenRingLineErrors": wfTokenRingLineErrors,
       "wfTokenRingBurstErrors": wfTokenRingBurstErrors,
       "wfTokenRingAriFciErrors": wfTokenRingAriFciErrors,
       "wfTokenRingLostFrameErrors": wfTokenRingLostFrameErrors,
       "wfTokenRingRxCongestionErrors": wfTokenRingRxCongestionErrors,
       "wfTokenRingFrameCopiedErrors": wfTokenRingFrameCopiedErrors,
       "wfTokenRingTokenErrors": wfTokenRingTokenErrors,
       "wfTokenRingDmaBusErrors": wfTokenRingDmaBusErrors,
       "wfTokenRingDmaParityErrors": wfTokenRingDmaParityErrors,
       "wfTokenRingSrbNotFreeCmdAborts": wfTokenRingSrbNotFreeCmdAborts,
       "wfTokenRingRxProcessings": wfTokenRingRxProcessings,
       "wfTokenRingTxProcessings": wfTokenRingTxProcessings,
       "wfTokenRingTxCmplProcessings": wfTokenRingTxCmplProcessings,
       "wfTokenRingRxTimeouts": wfTokenRingRxTimeouts,
       "wfTokenRingCmdTimeouts": wfTokenRingCmdTimeouts,
       "wfTokenRingRxHostIntErrors": wfTokenRingRxHostIntErrors,
       "wfTokenRingRxTxBufferSize": wfTokenRingRxTxBufferSize,
       "wfTokenRingCfgTxQueueLength": wfTokenRingCfgTxQueueLength,
       "wfTokenRingCfgRxQueueLength": wfTokenRingCfgRxQueueLength,
       "wfTokenRingTxQueueLength": wfTokenRingTxQueueLength,
       "wfTokenRingRxQueueLength": wfTokenRingRxQueueLength,
       "wfTokenRingMacRxOctets": wfTokenRingMacRxOctets,
       "wfTokenRingMacRxFrames": wfTokenRingMacRxFrames,
       "wfTokenRingCfgFunctionalAddress": wfTokenRingCfgFunctionalAddress,
       "wfTokenRingFunctionalAddress": wfTokenRingFunctionalAddress,
       "wfTokenRingGroupAddress": wfTokenRingGroupAddress,
       "wfTokenRingLineNumber": wfTokenRingLineNumber,
       "wfTokenRingMacCode": wfTokenRingMacCode,
       "wfTokenRingModule": wfTokenRingModule,
       "wfTokenRingActualConnector": wfTokenRingActualConnector,
       "wfTokenRingLastChange": wfTokenRingLastChange,
       "wfTokenRingOutQLen": wfTokenRingOutQLen,
       "wfTokenRingForceMacCode": wfTokenRingForceMacCode,
       "wfTokenRingMSBMadr": wfTokenRingMSBMadr,
       "wfTokenRingTurboBoflDebug": wfTokenRingTurboBoflDebug,
       "wfTokenRingSingleStatDis": wfTokenRingSingleStatDis}
)

# SNMP MIB module (Wellfleet-FNTS-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-FNTS-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:13 2024
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

(wfFntsAtmGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfFntsAtmGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfFntsAtmTable_Object = MibTable
wfFntsAtmTable = _WfFntsAtmTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1)
)
if mibBuilder.loadTexts:
    wfFntsAtmTable.setStatus("mandatory")
_WfFntsAtmEntry_Object = MibTableRow
wfFntsAtmEntry = _WfFntsAtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1)
)
wfFntsAtmEntry.setIndexNames(
    (0, "Wellfleet-FNTS-ATM-MIB", "wfFntsAtmSlot"),
    (0, "Wellfleet-FNTS-ATM-MIB", "wfFntsAtmConnector"),
)
if mibBuilder.loadTexts:
    wfFntsAtmEntry.setStatus("mandatory")


class _WfFntsAtmDelete_Type(Integer32):
    """Custom type wfFntsAtmDelete based on Integer32"""
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


_WfFntsAtmDelete_Type.__name__ = "Integer32"
_WfFntsAtmDelete_Object = MibTableColumn
wfFntsAtmDelete = _WfFntsAtmDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 1),
    _WfFntsAtmDelete_Type()
)
wfFntsAtmDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFntsAtmDelete.setStatus("mandatory")


class _WfFntsAtmDisable_Type(Integer32):
    """Custom type wfFntsAtmDisable based on Integer32"""
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


_WfFntsAtmDisable_Type.__name__ = "Integer32"
_WfFntsAtmDisable_Object = MibTableColumn
wfFntsAtmDisable = _WfFntsAtmDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 2),
    _WfFntsAtmDisable_Type()
)
wfFntsAtmDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFntsAtmDisable.setStatus("mandatory")


class _WfFntsAtmState_Type(Integer32):
    """Custom type wfFntsAtmState based on Integer32"""
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


_WfFntsAtmState_Type.__name__ = "Integer32"
_WfFntsAtmState_Object = MibTableColumn
wfFntsAtmState = _WfFntsAtmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 3),
    _WfFntsAtmState_Type()
)
wfFntsAtmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmState.setStatus("mandatory")


class _WfFntsAtmSlot_Type(Integer32):
    """Custom type wfFntsAtmSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfFntsAtmSlot_Type.__name__ = "Integer32"
_WfFntsAtmSlot_Object = MibTableColumn
wfFntsAtmSlot = _WfFntsAtmSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 4),
    _WfFntsAtmSlot_Type()
)
wfFntsAtmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmSlot.setStatus("mandatory")


class _WfFntsAtmConnector_Type(Integer32):
    """Custom type wfFntsAtmConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44),
    )


_WfFntsAtmConnector_Type.__name__ = "Integer32"
_WfFntsAtmConnector_Object = MibTableColumn
wfFntsAtmConnector = _WfFntsAtmConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 5),
    _WfFntsAtmConnector_Type()
)
wfFntsAtmConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmConnector.setStatus("mandatory")


class _WfFntsAtmCct_Type(Integer32):
    """Custom type wfFntsAtmCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfFntsAtmCct_Type.__name__ = "Integer32"
_WfFntsAtmCct_Object = MibTableColumn
wfFntsAtmCct = _WfFntsAtmCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 6),
    _WfFntsAtmCct_Type()
)
wfFntsAtmCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFntsAtmCct.setStatus("mandatory")


class _WfFntsAtmMtu_Type(Integer32):
    """Custom type wfFntsAtmMtu based on Integer32"""
    defaultValue = 4508

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4508
        )
    )
    namedValues = NamedValues(
        ("default", 4508)
    )


_WfFntsAtmMtu_Type.__name__ = "Integer32"
_WfFntsAtmMtu_Object = MibTableColumn
wfFntsAtmMtu = _WfFntsAtmMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 7),
    _WfFntsAtmMtu_Type()
)
wfFntsAtmMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFntsAtmMtu.setStatus("mandatory")
_WfFntsAtmMadr_Type = OctetString
_WfFntsAtmMadr_Object = MibTableColumn
wfFntsAtmMadr = _WfFntsAtmMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 8),
    _WfFntsAtmMadr_Type()
)
wfFntsAtmMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmMadr.setStatus("mandatory")
_WfFntsAtmIpAdr_Type = IpAddress
_WfFntsAtmIpAdr_Object = MibTableColumn
wfFntsAtmIpAdr = _WfFntsAtmIpAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 9),
    _WfFntsAtmIpAdr_Type()
)
wfFntsAtmIpAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmIpAdr.setStatus("mandatory")


class _WfFntsAtmAtmState_Type(Integer32):
    """Custom type wfFntsAtmAtmState based on Integer32"""
    defaultValue = 9

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("down", 6),
          ("extloop", 4),
          ("init", 2),
          ("intloop", 3),
          ("notpresent", 9),
          ("notready", 1),
          ("reset", 5),
          ("up", 7))
    )


_WfFntsAtmAtmState_Type.__name__ = "Integer32"
_WfFntsAtmAtmState_Object = MibTableColumn
wfFntsAtmAtmState = _WfFntsAtmAtmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 10),
    _WfFntsAtmAtmState_Type()
)
wfFntsAtmAtmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmAtmState.setStatus("mandatory")


class _WfFntsAtmSpeed_Type(Integer32):
    """Custom type wfFntsAtmSpeed based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            50
        )
    )
    namedValues = NamedValues(
        ("default", 50)
    )


_WfFntsAtmSpeed_Type.__name__ = "Integer32"
_WfFntsAtmSpeed_Object = MibTableColumn
wfFntsAtmSpeed = _WfFntsAtmSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 11),
    _WfFntsAtmSpeed_Type()
)
wfFntsAtmSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmSpeed.setStatus("mandatory")
_WfFntsAtmRxOctets_Type = Counter32
_WfFntsAtmRxOctets_Object = MibTableColumn
wfFntsAtmRxOctets = _WfFntsAtmRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 12),
    _WfFntsAtmRxOctets_Type()
)
wfFntsAtmRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmRxOctets.setStatus("mandatory")
_WfFntsAtmRxFrames_Type = Counter32
_WfFntsAtmRxFrames_Object = MibTableColumn
wfFntsAtmRxFrames = _WfFntsAtmRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 13),
    _WfFntsAtmRxFrames_Type()
)
wfFntsAtmRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmRxFrames.setStatus("mandatory")
_WfFntsAtmTxOctets_Type = Counter32
_WfFntsAtmTxOctets_Object = MibTableColumn
wfFntsAtmTxOctets = _WfFntsAtmTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 14),
    _WfFntsAtmTxOctets_Type()
)
wfFntsAtmTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmTxOctets.setStatus("mandatory")
_WfFntsAtmTxFrames_Type = Counter32
_WfFntsAtmTxFrames_Object = MibTableColumn
wfFntsAtmTxFrames = _WfFntsAtmTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 15),
    _WfFntsAtmTxFrames_Type()
)
wfFntsAtmTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmTxFrames.setStatus("mandatory")
_WfFntsAtmLackRescErrorRx_Type = Counter32
_WfFntsAtmLackRescErrorRx_Object = MibTableColumn
wfFntsAtmLackRescErrorRx = _WfFntsAtmLackRescErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 16),
    _WfFntsAtmLackRescErrorRx_Type()
)
wfFntsAtmLackRescErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmLackRescErrorRx.setStatus("mandatory")
_WfFntsAtmInErrors_Type = Counter32
_WfFntsAtmInErrors_Object = MibTableColumn
wfFntsAtmInErrors = _WfFntsAtmInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 17),
    _WfFntsAtmInErrors_Type()
)
wfFntsAtmInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmInErrors.setStatus("mandatory")
_WfFntsAtmOutErrors_Type = Counter32
_WfFntsAtmOutErrors_Object = MibTableColumn
wfFntsAtmOutErrors = _WfFntsAtmOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 18),
    _WfFntsAtmOutErrors_Type()
)
wfFntsAtmOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmOutErrors.setStatus("mandatory")
_WfFntsAtmRxLongFrames_Type = Counter32
_WfFntsAtmRxLongFrames_Object = MibTableColumn
wfFntsAtmRxLongFrames = _WfFntsAtmRxLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 19),
    _WfFntsAtmRxLongFrames_Type()
)
wfFntsAtmRxLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmRxLongFrames.setStatus("mandatory")
_WfFntsAtmTxClipFrames_Type = Counter32
_WfFntsAtmTxClipFrames_Object = MibTableColumn
wfFntsAtmTxClipFrames = _WfFntsAtmTxClipFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 20),
    _WfFntsAtmTxClipFrames_Type()
)
wfFntsAtmTxClipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmTxClipFrames.setStatus("mandatory")
_WfFntsAtmRxReplenMisses_Type = Counter32
_WfFntsAtmRxReplenMisses_Object = MibTableColumn
wfFntsAtmRxReplenMisses = _WfFntsAtmRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 21),
    _WfFntsAtmRxReplenMisses_Type()
)
wfFntsAtmRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmRxReplenMisses.setStatus("mandatory")
_WfFntsAtmRxOverruns_Type = Counter32
_WfFntsAtmRxOverruns_Object = MibTableColumn
wfFntsAtmRxOverruns = _WfFntsAtmRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 22),
    _WfFntsAtmRxOverruns_Type()
)
wfFntsAtmRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmRxOverruns.setStatus("mandatory")
_WfFntsAtmRxRingErrors_Type = Counter32
_WfFntsAtmRxRingErrors_Object = MibTableColumn
wfFntsAtmRxRingErrors = _WfFntsAtmRxRingErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 23),
    _WfFntsAtmRxRingErrors_Type()
)
wfFntsAtmRxRingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmRxRingErrors.setStatus("mandatory")
_WfFntsAtmTxRingErrors_Type = Counter32
_WfFntsAtmTxRingErrors_Object = MibTableColumn
wfFntsAtmTxRingErrors = _WfFntsAtmTxRingErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 24),
    _WfFntsAtmTxRingErrors_Type()
)
wfFntsAtmTxRingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmTxRingErrors.setStatus("mandatory")
_WfFntsAtmOpErrors_Type = Counter32
_WfFntsAtmOpErrors_Object = MibTableColumn
wfFntsAtmOpErrors = _WfFntsAtmOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 25),
    _WfFntsAtmOpErrors_Type()
)
wfFntsAtmOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmOpErrors.setStatus("mandatory")
_WfFntsAtmRxProcessings_Type = Counter32
_WfFntsAtmRxProcessings_Object = MibTableColumn
wfFntsAtmRxProcessings = _WfFntsAtmRxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 26),
    _WfFntsAtmRxProcessings_Type()
)
wfFntsAtmRxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmRxProcessings.setStatus("mandatory")
_WfFntsAtmTxProcessings_Type = Counter32
_WfFntsAtmTxProcessings_Object = MibTableColumn
wfFntsAtmTxProcessings = _WfFntsAtmTxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 27),
    _WfFntsAtmTxProcessings_Type()
)
wfFntsAtmTxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmTxProcessings.setStatus("mandatory")
_WfFntsAtmTxCmplProcessings_Type = Counter32
_WfFntsAtmTxCmplProcessings_Object = MibTableColumn
wfFntsAtmTxCmplProcessings = _WfFntsAtmTxCmplProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 28),
    _WfFntsAtmTxCmplProcessings_Type()
)
wfFntsAtmTxCmplProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmTxCmplProcessings.setStatus("mandatory")
_WfFntsAtmIntrProcessings_Type = Counter32
_WfFntsAtmIntrProcessings_Object = MibTableColumn
wfFntsAtmIntrProcessings = _WfFntsAtmIntrProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 29),
    _WfFntsAtmIntrProcessings_Type()
)
wfFntsAtmIntrProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmIntrProcessings.setStatus("mandatory")
_WfFntsAtmSintProcessings_Type = Counter32
_WfFntsAtmSintProcessings_Object = MibTableColumn
wfFntsAtmSintProcessings = _WfFntsAtmSintProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 30),
    _WfFntsAtmSintProcessings_Type()
)
wfFntsAtmSintProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmSintProcessings.setStatus("mandatory")
_WfFntsAtmPintProcessings_Type = Counter32
_WfFntsAtmPintProcessings_Object = MibTableColumn
wfFntsAtmPintProcessings = _WfFntsAtmPintProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 31),
    _WfFntsAtmPintProcessings_Type()
)
wfFntsAtmPintProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFntsAtmPintProcessings.setStatus("mandatory")


class _WfFntsAtmRxRingLength_Type(Integer32):
    """Custom type wfFntsAtmRxRingLength based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            63
        )
    )
    namedValues = NamedValues(
        ("default", 63)
    )


_WfFntsAtmRxRingLength_Type.__name__ = "Integer32"
_WfFntsAtmRxRingLength_Object = MibTableColumn
wfFntsAtmRxRingLength = _WfFntsAtmRxRingLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 32),
    _WfFntsAtmRxRingLength_Type()
)
wfFntsAtmRxRingLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFntsAtmRxRingLength.setStatus("mandatory")


class _WfFntsAtmTxRingLength_Type(Integer32):
    """Custom type wfFntsAtmTxRingLength based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            63
        )
    )
    namedValues = NamedValues(
        ("default", 63)
    )


_WfFntsAtmTxRingLength_Type.__name__ = "Integer32"
_WfFntsAtmTxRingLength_Object = MibTableColumn
wfFntsAtmTxRingLength = _WfFntsAtmTxRingLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 33),
    _WfFntsAtmTxRingLength_Type()
)
wfFntsAtmTxRingLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFntsAtmTxRingLength.setStatus("mandatory")


class _WfFntsAtmCfgRxQueueLength_Type(Integer32):
    """Custom type wfFntsAtmCfgRxQueueLength based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            127
        )
    )
    namedValues = NamedValues(
        ("default", 127)
    )


_WfFntsAtmCfgRxQueueLength_Type.__name__ = "Integer32"
_WfFntsAtmCfgRxQueueLength_Object = MibTableColumn
wfFntsAtmCfgRxQueueLength = _WfFntsAtmCfgRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 34),
    _WfFntsAtmCfgRxQueueLength_Type()
)
wfFntsAtmCfgRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFntsAtmCfgRxQueueLength.setStatus("mandatory")


class _WfFntsAtmCfgTxQueueLength_Type(Integer32):
    """Custom type wfFntsAtmCfgTxQueueLength based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            127
        )
    )
    namedValues = NamedValues(
        ("default", 127)
    )


_WfFntsAtmCfgTxQueueLength_Type.__name__ = "Integer32"
_WfFntsAtmCfgTxQueueLength_Object = MibTableColumn
wfFntsAtmCfgTxQueueLength = _WfFntsAtmCfgTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 35),
    _WfFntsAtmCfgTxQueueLength_Type()
)
wfFntsAtmCfgTxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFntsAtmCfgTxQueueLength.setStatus("mandatory")
_WfFntsAtmLineNumber_Type = Integer32
_WfFntsAtmLineNumber_Object = MibTableColumn
wfFntsAtmLineNumber = _WfFntsAtmLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 32, 1, 1, 36),
    _WfFntsAtmLineNumber_Type()
)
wfFntsAtmLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFntsAtmLineNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-FNTS-ATM-MIB",
    **{"wfFntsAtmTable": wfFntsAtmTable,
       "wfFntsAtmEntry": wfFntsAtmEntry,
       "wfFntsAtmDelete": wfFntsAtmDelete,
       "wfFntsAtmDisable": wfFntsAtmDisable,
       "wfFntsAtmState": wfFntsAtmState,
       "wfFntsAtmSlot": wfFntsAtmSlot,
       "wfFntsAtmConnector": wfFntsAtmConnector,
       "wfFntsAtmCct": wfFntsAtmCct,
       "wfFntsAtmMtu": wfFntsAtmMtu,
       "wfFntsAtmMadr": wfFntsAtmMadr,
       "wfFntsAtmIpAdr": wfFntsAtmIpAdr,
       "wfFntsAtmAtmState": wfFntsAtmAtmState,
       "wfFntsAtmSpeed": wfFntsAtmSpeed,
       "wfFntsAtmRxOctets": wfFntsAtmRxOctets,
       "wfFntsAtmRxFrames": wfFntsAtmRxFrames,
       "wfFntsAtmTxOctets": wfFntsAtmTxOctets,
       "wfFntsAtmTxFrames": wfFntsAtmTxFrames,
       "wfFntsAtmLackRescErrorRx": wfFntsAtmLackRescErrorRx,
       "wfFntsAtmInErrors": wfFntsAtmInErrors,
       "wfFntsAtmOutErrors": wfFntsAtmOutErrors,
       "wfFntsAtmRxLongFrames": wfFntsAtmRxLongFrames,
       "wfFntsAtmTxClipFrames": wfFntsAtmTxClipFrames,
       "wfFntsAtmRxReplenMisses": wfFntsAtmRxReplenMisses,
       "wfFntsAtmRxOverruns": wfFntsAtmRxOverruns,
       "wfFntsAtmRxRingErrors": wfFntsAtmRxRingErrors,
       "wfFntsAtmTxRingErrors": wfFntsAtmTxRingErrors,
       "wfFntsAtmOpErrors": wfFntsAtmOpErrors,
       "wfFntsAtmRxProcessings": wfFntsAtmRxProcessings,
       "wfFntsAtmTxProcessings": wfFntsAtmTxProcessings,
       "wfFntsAtmTxCmplProcessings": wfFntsAtmTxCmplProcessings,
       "wfFntsAtmIntrProcessings": wfFntsAtmIntrProcessings,
       "wfFntsAtmSintProcessings": wfFntsAtmSintProcessings,
       "wfFntsAtmPintProcessings": wfFntsAtmPintProcessings,
       "wfFntsAtmRxRingLength": wfFntsAtmRxRingLength,
       "wfFntsAtmTxRingLength": wfFntsAtmTxRingLength,
       "wfFntsAtmCfgRxQueueLength": wfFntsAtmCfgRxQueueLength,
       "wfFntsAtmCfgTxQueueLength": wfFntsAtmCfgTxQueueLength,
       "wfFntsAtmLineNumber": wfFntsAtmLineNumber}
)

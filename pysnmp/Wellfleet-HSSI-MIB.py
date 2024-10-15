# SNMP MIB module (Wellfleet-HSSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-HSSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:20 2024
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

_WfHssiTable_Object = MibTable
wfHssiTable = _WfHssiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7)
)
if mibBuilder.loadTexts:
    wfHssiTable.setStatus("mandatory")
_WfHssiEntry_Object = MibTableRow
wfHssiEntry = _WfHssiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1)
)
wfHssiEntry.setIndexNames(
    (0, "Wellfleet-HSSI-MIB", "wfHssiSlot"),
    (0, "Wellfleet-HSSI-MIB", "wfHssiConnector"),
)
if mibBuilder.loadTexts:
    wfHssiEntry.setStatus("mandatory")


class _WfHssiDelete_Type(Integer32):
    """Custom type wfHssiDelete based on Integer32"""
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


_WfHssiDelete_Type.__name__ = "Integer32"
_WfHssiDelete_Object = MibTableColumn
wfHssiDelete = _WfHssiDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 1),
    _WfHssiDelete_Type()
)
wfHssiDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiDelete.setStatus("mandatory")


class _WfHssiDisable_Type(Integer32):
    """Custom type wfHssiDisable based on Integer32"""
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


_WfHssiDisable_Type.__name__ = "Integer32"
_WfHssiDisable_Object = MibTableColumn
wfHssiDisable = _WfHssiDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 2),
    _WfHssiDisable_Type()
)
wfHssiDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiDisable.setStatus("mandatory")


class _WfHssiState_Type(Integer32):
    """Custom type wfHssiState based on Integer32"""
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
              9,
              10,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("boflwait", 3),
          ("cawait", 4),
          ("dceloopback", 8),
          ("dceloopbacktmo", 10),
          ("dceloopbackwait", 9),
          ("dteloopback", 7),
          ("init", 5),
          ("lineloopbofltest", 19),
          ("lmiwait", 2),
          ("notpres", 20),
          ("notpresent", 6),
          ("up", 1))
    )


_WfHssiState_Type.__name__ = "Integer32"
_WfHssiState_Object = MibTableColumn
wfHssiState = _WfHssiState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 3),
    _WfHssiState_Type()
)
wfHssiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiState.setStatus("mandatory")


class _WfHssiSlot_Type(Integer32):
    """Custom type wfHssiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfHssiSlot_Type.__name__ = "Integer32"
_WfHssiSlot_Object = MibTableColumn
wfHssiSlot = _WfHssiSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 4),
    _WfHssiSlot_Type()
)
wfHssiSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiSlot.setStatus("mandatory")


class _WfHssiConnector_Type(Integer32):
    """Custom type wfHssiConnector based on Integer32"""
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


_WfHssiConnector_Type.__name__ = "Integer32"
_WfHssiConnector_Object = MibTableColumn
wfHssiConnector = _WfHssiConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 5),
    _WfHssiConnector_Type()
)
wfHssiConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiConnector.setStatus("mandatory")


class _WfHssiCct_Type(Integer32):
    """Custom type wfHssiCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfHssiCct_Type.__name__ = "Integer32"
_WfHssiCct_Object = MibTableColumn
wfHssiCct = _WfHssiCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 6),
    _WfHssiCct_Type()
)
wfHssiCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiCct.setStatus("mandatory")


class _WfHssiBofl_Type(Integer32):
    """Custom type wfHssiBofl based on Integer32"""
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


_WfHssiBofl_Type.__name__ = "Integer32"
_WfHssiBofl_Object = MibTableColumn
wfHssiBofl = _WfHssiBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 7),
    _WfHssiBofl_Type()
)
wfHssiBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiBofl.setStatus("mandatory")


class _WfHssiBoflTmo_Type(Integer32):
    """Custom type wfHssiBoflTmo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfHssiBoflTmo_Type.__name__ = "Integer32"
_WfHssiBoflTmo_Object = MibTableColumn
wfHssiBoflTmo = _WfHssiBoflTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 8),
    _WfHssiBoflTmo_Type()
)
wfHssiBoflTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiBoflTmo.setStatus("mandatory")


class _WfHssiMtu_Type(Integer32):
    """Custom type wfHssiMtu based on Integer32"""
    defaultValue = 4608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4608),
    )


_WfHssiMtu_Type.__name__ = "Integer32"
_WfHssiMtu_Object = MibTableColumn
wfHssiMtu = _WfHssiMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 9),
    _WfHssiMtu_Type()
)
wfHssiMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiMtu.setStatus("mandatory")
_WfHssiMadr_Type = OctetString
_WfHssiMadr_Object = MibTableColumn
wfHssiMadr = _WfHssiMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 10),
    _WfHssiMadr_Type()
)
wfHssiMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiMadr.setStatus("mandatory")


class _WfHssiService_Type(Integer32):
    """Custom type wfHssiService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("undefined", 2))
    )


_WfHssiService_Type.__name__ = "Integer32"
_WfHssiService_Object = MibTableColumn
wfHssiService = _WfHssiService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 11),
    _WfHssiService_Type()
)
wfHssiService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiService.setStatus("mandatory")


class _WfHssiWanProtocol_Type(Integer32):
    """Custom type wfHssiWanProtocol based on Integer32"""
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
        *(("atm", 6),
          ("framerelay", 5),
          ("passthru", 2),
          ("ppp", 3),
          ("smds", 4),
          ("standard", 1),
          ("sw", 7),
          ("switch", 8))
    )


_WfHssiWanProtocol_Type.__name__ = "Integer32"
_WfHssiWanProtocol_Object = MibTableColumn
wfHssiWanProtocol = _WfHssiWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 12),
    _WfHssiWanProtocol_Type()
)
wfHssiWanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiWanProtocol.setStatus("mandatory")


class _WfHssiTransmissionInterface_Type(Integer32):
    """Custom type wfHssiTransmissionInterface based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsone", 1),
          ("dsthree", 3))
    )


_WfHssiTransmissionInterface_Type.__name__ = "Integer32"
_WfHssiTransmissionInterface_Object = MibTableColumn
wfHssiTransmissionInterface = _WfHssiTransmissionInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 13),
    _WfHssiTransmissionInterface_Type()
)
wfHssiTransmissionInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiTransmissionInterface.setStatus("mandatory")


class _WfHssiExternalClkSpeed_Type(Integer32):
    """Custom type wfHssiExternalClkSpeed based on Integer32"""
    defaultValue = 46359642

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(307200, 52638515),
    )


_WfHssiExternalClkSpeed_Type.__name__ = "Integer32"
_WfHssiExternalClkSpeed_Object = MibTableColumn
wfHssiExternalClkSpeed = _WfHssiExternalClkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 14),
    _WfHssiExternalClkSpeed_Type()
)
wfHssiExternalClkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiExternalClkSpeed.setStatus("mandatory")


class _WfHssiCrcSize_Type(Integer32):
    """Custom type wfHssiCrcSize based on Integer32"""
    defaultValue = 2

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


_WfHssiCrcSize_Type.__name__ = "Integer32"
_WfHssiCrcSize_Object = MibTableColumn
wfHssiCrcSize = _WfHssiCrcSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 15),
    _WfHssiCrcSize_Type()
)
wfHssiCrcSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiCrcSize.setStatus("mandatory")


class _WfHssiInternalClkTestMode_Type(Integer32):
    """Custom type wfHssiInternalClkTestMode based on Integer32"""
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


_WfHssiInternalClkTestMode_Type.__name__ = "Integer32"
_WfHssiInternalClkTestMode_Object = MibTableColumn
wfHssiInternalClkTestMode = _WfHssiInternalClkTestMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 16),
    _WfHssiInternalClkTestMode_Type()
)
wfHssiInternalClkTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiInternalClkTestMode.setStatus("mandatory")
_WfHssiRxOctets_Type = Counter32
_WfHssiRxOctets_Object = MibTableColumn
wfHssiRxOctets = _WfHssiRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 17),
    _WfHssiRxOctets_Type()
)
wfHssiRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxOctets.setStatus("mandatory")
_WfHssiRxFrames_Type = Counter32
_WfHssiRxFrames_Object = MibTableColumn
wfHssiRxFrames = _WfHssiRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 18),
    _WfHssiRxFrames_Type()
)
wfHssiRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxFrames.setStatus("mandatory")
_WfHssiTxOctets_Type = Counter32
_WfHssiTxOctets_Object = MibTableColumn
wfHssiTxOctets = _WfHssiTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 19),
    _WfHssiTxOctets_Type()
)
wfHssiTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxOctets.setStatus("mandatory")
_WfHssiTxFrames_Type = Counter32
_WfHssiTxFrames_Object = MibTableColumn
wfHssiTxFrames = _WfHssiTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 20),
    _WfHssiTxFrames_Type()
)
wfHssiTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxFrames.setStatus("mandatory")
_WfHssiInDiscards_Type = Counter32
_WfHssiInDiscards_Object = MibTableColumn
wfHssiInDiscards = _WfHssiInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 21),
    _WfHssiInDiscards_Type()
)
wfHssiInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiInDiscards.setStatus("mandatory")
_WfHssiInErrors_Type = Counter32
_WfHssiInErrors_Object = MibTableColumn
wfHssiInErrors = _WfHssiInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 22),
    _WfHssiInErrors_Type()
)
wfHssiInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiInErrors.setStatus("mandatory")
_WfHssiOutDiscards_Type = Counter32
_WfHssiOutDiscards_Object = MibTableColumn
wfHssiOutDiscards = _WfHssiOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 23),
    _WfHssiOutDiscards_Type()
)
wfHssiOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiOutDiscards.setStatus("mandatory")
_WfHssiOutErrors_Type = Counter32
_WfHssiOutErrors_Object = MibTableColumn
wfHssiOutErrors = _WfHssiOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 24),
    _WfHssiOutErrors_Type()
)
wfHssiOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiOutErrors.setStatus("mandatory")
_WfHssiRxLongFrames_Type = Counter32
_WfHssiRxLongFrames_Object = MibTableColumn
wfHssiRxLongFrames = _WfHssiRxLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 25),
    _WfHssiRxLongFrames_Type()
)
wfHssiRxLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxLongFrames.setStatus("mandatory")
_WfHssiTxClipFrames_Type = Counter32
_WfHssiTxClipFrames_Object = MibTableColumn
wfHssiTxClipFrames = _WfHssiTxClipFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 26),
    _WfHssiTxClipFrames_Type()
)
wfHssiTxClipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxClipFrames.setStatus("mandatory")
_WfHssiRxReplenMisses_Type = Counter32
_WfHssiRxReplenMisses_Object = MibTableColumn
wfHssiRxReplenMisses = _WfHssiRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 27),
    _WfHssiRxReplenMisses_Type()
)
wfHssiRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxReplenMisses.setStatus("mandatory")
_WfHssiLastRxErrorCtrl_Type = Integer32
_WfHssiLastRxErrorCtrl_Object = MibTableColumn
wfHssiLastRxErrorCtrl = _WfHssiLastRxErrorCtrl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 28),
    _WfHssiLastRxErrorCtrl_Type()
)
wfHssiLastRxErrorCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiLastRxErrorCtrl.setStatus("mandatory")
_WfHssiRxCrcErrors_Type = Counter32
_WfHssiRxCrcErrors_Object = MibTableColumn
wfHssiRxCrcErrors = _WfHssiRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 29),
    _WfHssiRxCrcErrors_Type()
)
wfHssiRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxCrcErrors.setStatus("mandatory")
_WfHssiRxOverruns_Type = Counter32
_WfHssiRxOverruns_Object = MibTableColumn
wfHssiRxOverruns = _WfHssiRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 30),
    _WfHssiRxOverruns_Type()
)
wfHssiRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxOverruns.setStatus("mandatory")
_WfHssiRxAborts_Type = Counter32
_WfHssiRxAborts_Object = MibTableColumn
wfHssiRxAborts = _WfHssiRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 31),
    _WfHssiRxAborts_Type()
)
wfHssiRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxAborts.setStatus("mandatory")
_WfHssiLastTxErrorCtrl_Type = Integer32
_WfHssiLastTxErrorCtrl_Object = MibTableColumn
wfHssiLastTxErrorCtrl = _WfHssiLastTxErrorCtrl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 32),
    _WfHssiLastTxErrorCtrl_Type()
)
wfHssiLastTxErrorCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiLastTxErrorCtrl.setStatus("mandatory")
_WfHssiTxAborts_Type = Counter32
_WfHssiTxAborts_Object = MibTableColumn
wfHssiTxAborts = _WfHssiTxAborts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 33),
    _WfHssiTxAborts_Type()
)
wfHssiTxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxAborts.setStatus("mandatory")
_WfHssiTxUnderruns_Type = Counter32
_WfHssiTxUnderruns_Object = MibTableColumn
wfHssiTxUnderruns = _WfHssiTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 34),
    _WfHssiTxUnderruns_Type()
)
wfHssiTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxUnderruns.setStatus("mandatory")
_WfHssiRxRingErrors_Type = Counter32
_WfHssiRxRingErrors_Object = MibTableColumn
wfHssiRxRingErrors = _WfHssiRxRingErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 35),
    _WfHssiRxRingErrors_Type()
)
wfHssiRxRingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxRingErrors.setStatus("mandatory")
_WfHssiLastRxRingState_Type = Integer32
_WfHssiLastRxRingState_Object = MibTableColumn
wfHssiLastRxRingState = _WfHssiLastRxRingState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 36),
    _WfHssiLastRxRingState_Type()
)
wfHssiLastRxRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiLastRxRingState.setStatus("mandatory")
_WfHssiRxRingOverruns_Type = Counter32
_WfHssiRxRingOverruns_Object = MibTableColumn
wfHssiRxRingOverruns = _WfHssiRxRingOverruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 37),
    _WfHssiRxRingOverruns_Type()
)
wfHssiRxRingOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxRingOverruns.setStatus("mandatory")
_WfHssiTxRingErrors_Type = Counter32
_WfHssiTxRingErrors_Object = MibTableColumn
wfHssiTxRingErrors = _WfHssiTxRingErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 38),
    _WfHssiTxRingErrors_Type()
)
wfHssiTxRingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxRingErrors.setStatus("mandatory")
_WfHssiLastTxRingState_Type = Integer32
_WfHssiLastTxRingState_Object = MibTableColumn
wfHssiLastTxRingState = _WfHssiLastTxRingState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 39),
    _WfHssiLastTxRingState_Type()
)
wfHssiLastTxRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiLastTxRingState.setStatus("mandatory")
_WfHssiPortOpErrors_Type = Counter32
_WfHssiPortOpErrors_Object = MibTableColumn
wfHssiPortOpErrors = _WfHssiPortOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 40),
    _WfHssiPortOpErrors_Type()
)
wfHssiPortOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiPortOpErrors.setStatus("mandatory")
_WfHssiInternOpErrors_Type = Counter32
_WfHssiInternOpErrors_Object = MibTableColumn
wfHssiInternOpErrors = _WfHssiInternOpErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 41),
    _WfHssiInternOpErrors_Type()
)
wfHssiInternOpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiInternOpErrors.setStatus("mandatory")
_WfHssiHostErrors_Type = Counter32
_WfHssiHostErrors_Object = MibTableColumn
wfHssiHostErrors = _WfHssiHostErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 42),
    _WfHssiHostErrors_Type()
)
wfHssiHostErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiHostErrors.setStatus("mandatory")
_WfHssiRxProcessings_Type = Counter32
_WfHssiRxProcessings_Object = MibTableColumn
wfHssiRxProcessings = _WfHssiRxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 43),
    _WfHssiRxProcessings_Type()
)
wfHssiRxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxProcessings.setStatus("mandatory")
_WfHssiTxProcessings_Type = Counter32
_WfHssiTxProcessings_Object = MibTableColumn
wfHssiTxProcessings = _WfHssiTxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 44),
    _WfHssiTxProcessings_Type()
)
wfHssiTxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxProcessings.setStatus("mandatory")
_WfHssiTxCmplProcessings_Type = Counter32
_WfHssiTxCmplProcessings_Object = MibTableColumn
wfHssiTxCmplProcessings = _WfHssiTxCmplProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 45),
    _WfHssiTxCmplProcessings_Type()
)
wfHssiTxCmplProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxCmplProcessings.setStatus("mandatory")
_WfHssiIntrProcessings_Type = Counter32
_WfHssiIntrProcessings_Object = MibTableColumn
wfHssiIntrProcessings = _WfHssiIntrProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 46),
    _WfHssiIntrProcessings_Type()
)
wfHssiIntrProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiIntrProcessings.setStatus("mandatory")


class _WfHssiBoflNum_Type(Integer32):
    """Custom type wfHssiBoflNum based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfHssiBoflNum_Type.__name__ = "Integer32"
_WfHssiBoflNum_Object = MibTableColumn
wfHssiBoflNum = _WfHssiBoflNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 47),
    _WfHssiBoflNum_Type()
)
wfHssiBoflNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiBoflNum.setStatus("mandatory")


class _WfHssiBoflLen_Type(Integer32):
    """Custom type wfHssiBoflLen based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 4450),
    )


_WfHssiBoflLen_Type.__name__ = "Integer32"
_WfHssiBoflLen_Object = MibTableColumn
wfHssiBoflLen = _WfHssiBoflLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 48),
    _WfHssiBoflLen_Type()
)
wfHssiBoflLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiBoflLen.setStatus("mandatory")


class _WfHssiRxBufferLength_Type(Integer32):
    """Custom type wfHssiRxBufferLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("length4k", 64),
          ("length8k", 128))
    )


_WfHssiRxBufferLength_Type.__name__ = "Integer32"
_WfHssiRxBufferLength_Object = MibTableColumn
wfHssiRxBufferLength = _WfHssiRxBufferLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 49),
    _WfHssiRxBufferLength_Type()
)
wfHssiRxBufferLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiRxBufferLength.setStatus("mandatory")


class _WfHssiMemPageLength_Type(Integer32):
    """Custom type wfHssiMemPageLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("length256", 3),
          ("length32", 1))
    )


_WfHssiMemPageLength_Type.__name__ = "Integer32"
_WfHssiMemPageLength_Object = MibTableColumn
wfHssiMemPageLength = _WfHssiMemPageLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 50),
    _WfHssiMemPageLength_Type()
)
wfHssiMemPageLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiMemPageLength.setStatus("mandatory")
_WfHssiRxRingLength_Type = Integer32
_WfHssiRxRingLength_Object = MibTableColumn
wfHssiRxRingLength = _WfHssiRxRingLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 51),
    _WfHssiRxRingLength_Type()
)
wfHssiRxRingLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiRxRingLength.setStatus("mandatory")
_WfHssiTxRingLength_Type = Integer32
_WfHssiTxRingLength_Object = MibTableColumn
wfHssiTxRingLength = _WfHssiTxRingLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 52),
    _WfHssiTxRingLength_Type()
)
wfHssiTxRingLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiTxRingLength.setStatus("mandatory")


class _WfHssiRxFifoWatermark_Type(Integer32):
    """Custom type wfHssiRxFifoWatermark based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_WfHssiRxFifoWatermark_Type.__name__ = "Integer32"
_WfHssiRxFifoWatermark_Object = MibTableColumn
wfHssiRxFifoWatermark = _WfHssiRxFifoWatermark_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 53),
    _WfHssiRxFifoWatermark_Type()
)
wfHssiRxFifoWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiRxFifoWatermark.setStatus("mandatory")


class _WfHssiTxFifoWatermark_Type(Integer32):
    """Custom type wfHssiTxFifoWatermark based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_WfHssiTxFifoWatermark_Type.__name__ = "Integer32"
_WfHssiTxFifoWatermark_Object = MibTableColumn
wfHssiTxFifoWatermark = _WfHssiTxFifoWatermark_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 54),
    _WfHssiTxFifoWatermark_Type()
)
wfHssiTxFifoWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiTxFifoWatermark.setStatus("mandatory")


class _WfHssiMaxRxMemory_Type(Integer32):
    """Custom type wfHssiMaxRxMemory based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfHssiMaxRxMemory_Type.__name__ = "Integer32"
_WfHssiMaxRxMemory_Object = MibTableColumn
wfHssiMaxRxMemory = _WfHssiMaxRxMemory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 55),
    _WfHssiMaxRxMemory_Type()
)
wfHssiMaxRxMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiMaxRxMemory.setStatus("mandatory")


class _WfHssiLinkInterface_Type(Integer32):
    """Custom type wfHssiLinkInterface based on Integer32"""
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
        *(("ace25", 2),
          ("ace32", 3),
          ("default", 1))
    )


_WfHssiLinkInterface_Type.__name__ = "Integer32"
_WfHssiLinkInterface_Object = MibTableColumn
wfHssiLinkInterface = _WfHssiLinkInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 56),
    _WfHssiLinkInterface_Type()
)
wfHssiLinkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiLinkInterface.setStatus("mandatory")


class _WfHssiTurboBofl_Type(Integer32):
    """Custom type wfHssiTurboBofl based on Integer32"""
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


_WfHssiTurboBofl_Type.__name__ = "Integer32"
_WfHssiTurboBofl_Object = MibTableColumn
wfHssiTurboBofl = _WfHssiTurboBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 57),
    _WfHssiTurboBofl_Type()
)
wfHssiTurboBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiTurboBofl.setStatus("mandatory")


class _WfHssiCfgRxQueueLength_Type(Integer32):
    """Custom type wfHssiCfgRxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfHssiCfgRxQueueLength_Type.__name__ = "Integer32"
_WfHssiCfgRxQueueLength_Object = MibTableColumn
wfHssiCfgRxQueueLength = _WfHssiCfgRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 58),
    _WfHssiCfgRxQueueLength_Type()
)
wfHssiCfgRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiCfgRxQueueLength.setStatus("mandatory")


class _WfHssiCfgTxQueueLength_Type(Integer32):
    """Custom type wfHssiCfgTxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfHssiCfgTxQueueLength_Type.__name__ = "Integer32"
_WfHssiCfgTxQueueLength_Object = MibTableColumn
wfHssiCfgTxQueueLength = _WfHssiCfgTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 59),
    _WfHssiCfgTxQueueLength_Type()
)
wfHssiCfgTxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiCfgTxQueueLength.setStatus("mandatory")
_WfHssiLineNumber_Type = Integer32
_WfHssiLineNumber_Object = MibTableColumn
wfHssiLineNumber = _WfHssiLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 60),
    _WfHssiLineNumber_Type()
)
wfHssiLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiLineNumber.setStatus("mandatory")


class _WfHssiCfgCngstCtlEnable_Type(Integer32):
    """Custom type wfHssiCfgCngstCtlEnable based on Integer32"""
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


_WfHssiCfgCngstCtlEnable_Type.__name__ = "Integer32"
_WfHssiCfgCngstCtlEnable_Object = MibTableColumn
wfHssiCfgCngstCtlEnable = _WfHssiCfgCngstCtlEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 61),
    _WfHssiCfgCngstCtlEnable_Type()
)
wfHssiCfgCngstCtlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiCfgCngstCtlEnable.setStatus("mandatory")
_WfHssiLastChange_Type = TimeTicks
_WfHssiLastChange_Object = MibTableColumn
wfHssiLastChange = _WfHssiLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 62),
    _WfHssiLastChange_Type()
)
wfHssiLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiLastChange.setStatus("mandatory")
_WfHssiOutQLen_Type = Gauge32
_WfHssiOutQLen_Object = MibTableColumn
wfHssiOutQLen = _WfHssiOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 63),
    _WfHssiOutQLen_Type()
)
wfHssiOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiOutQLen.setStatus("mandatory")


class _WfHssiCarrLossDebounceTmo_Type(Integer32):
    """Custom type wfHssiCarrLossDebounceTmo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfHssiCarrLossDebounceTmo_Type.__name__ = "Integer32"
_WfHssiCarrLossDebounceTmo_Object = MibTableColumn
wfHssiCarrLossDebounceTmo = _WfHssiCarrLossDebounceTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 64),
    _WfHssiCarrLossDebounceTmo_Type()
)
wfHssiCarrLossDebounceTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiCarrLossDebounceTmo.setStatus("mandatory")


class _WfHssiModule_Type(Integer32):
    """Custom type wfHssiModule based on Integer32"""
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


_WfHssiModule_Type.__name__ = "Integer32"
_WfHssiModule_Object = MibTableColumn
wfHssiModule = _WfHssiModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 65),
    _WfHssiModule_Type()
)
wfHssiModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiModule.setStatus("mandatory")


class _WfHssiActualConnector_Type(Integer32):
    """Custom type wfHssiActualConnector based on Integer32"""
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


_WfHssiActualConnector_Type.__name__ = "Integer32"
_WfHssiActualConnector_Object = MibTableColumn
wfHssiActualConnector = _WfHssiActualConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 66),
    _WfHssiActualConnector_Type()
)
wfHssiActualConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHssiActualConnector.setStatus("mandatory")


class _WfHssiLoopback_Type(Integer32):
    """Custom type wfHssiLoopback based on Integer32"""
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
        *(("localdigital", 2),
          ("localline", 3),
          ("none", 1),
          ("remoteline", 4))
    )


_WfHssiLoopback_Type.__name__ = "Integer32"
_WfHssiLoopback_Object = MibTableColumn
wfHssiLoopback = _WfHssiLoopback_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 67),
    _WfHssiLoopback_Type()
)
wfHssiLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiLoopback.setStatus("mandatory")


class _WfHssiReceiveAllFrames_Type(Integer32):
    """Custom type wfHssiReceiveAllFrames based on Integer32"""
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


_WfHssiReceiveAllFrames_Type.__name__ = "Integer32"
_WfHssiReceiveAllFrames_Object = MibTableColumn
wfHssiReceiveAllFrames = _WfHssiReceiveAllFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 7, 1, 68),
    _WfHssiReceiveAllFrames_Type()
)
wfHssiReceiveAllFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHssiReceiveAllFrames.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-HSSI-MIB",
    **{"wfHssiTable": wfHssiTable,
       "wfHssiEntry": wfHssiEntry,
       "wfHssiDelete": wfHssiDelete,
       "wfHssiDisable": wfHssiDisable,
       "wfHssiState": wfHssiState,
       "wfHssiSlot": wfHssiSlot,
       "wfHssiConnector": wfHssiConnector,
       "wfHssiCct": wfHssiCct,
       "wfHssiBofl": wfHssiBofl,
       "wfHssiBoflTmo": wfHssiBoflTmo,
       "wfHssiMtu": wfHssiMtu,
       "wfHssiMadr": wfHssiMadr,
       "wfHssiService": wfHssiService,
       "wfHssiWanProtocol": wfHssiWanProtocol,
       "wfHssiTransmissionInterface": wfHssiTransmissionInterface,
       "wfHssiExternalClkSpeed": wfHssiExternalClkSpeed,
       "wfHssiCrcSize": wfHssiCrcSize,
       "wfHssiInternalClkTestMode": wfHssiInternalClkTestMode,
       "wfHssiRxOctets": wfHssiRxOctets,
       "wfHssiRxFrames": wfHssiRxFrames,
       "wfHssiTxOctets": wfHssiTxOctets,
       "wfHssiTxFrames": wfHssiTxFrames,
       "wfHssiInDiscards": wfHssiInDiscards,
       "wfHssiInErrors": wfHssiInErrors,
       "wfHssiOutDiscards": wfHssiOutDiscards,
       "wfHssiOutErrors": wfHssiOutErrors,
       "wfHssiRxLongFrames": wfHssiRxLongFrames,
       "wfHssiTxClipFrames": wfHssiTxClipFrames,
       "wfHssiRxReplenMisses": wfHssiRxReplenMisses,
       "wfHssiLastRxErrorCtrl": wfHssiLastRxErrorCtrl,
       "wfHssiRxCrcErrors": wfHssiRxCrcErrors,
       "wfHssiRxOverruns": wfHssiRxOverruns,
       "wfHssiRxAborts": wfHssiRxAborts,
       "wfHssiLastTxErrorCtrl": wfHssiLastTxErrorCtrl,
       "wfHssiTxAborts": wfHssiTxAborts,
       "wfHssiTxUnderruns": wfHssiTxUnderruns,
       "wfHssiRxRingErrors": wfHssiRxRingErrors,
       "wfHssiLastRxRingState": wfHssiLastRxRingState,
       "wfHssiRxRingOverruns": wfHssiRxRingOverruns,
       "wfHssiTxRingErrors": wfHssiTxRingErrors,
       "wfHssiLastTxRingState": wfHssiLastTxRingState,
       "wfHssiPortOpErrors": wfHssiPortOpErrors,
       "wfHssiInternOpErrors": wfHssiInternOpErrors,
       "wfHssiHostErrors": wfHssiHostErrors,
       "wfHssiRxProcessings": wfHssiRxProcessings,
       "wfHssiTxProcessings": wfHssiTxProcessings,
       "wfHssiTxCmplProcessings": wfHssiTxCmplProcessings,
       "wfHssiIntrProcessings": wfHssiIntrProcessings,
       "wfHssiBoflNum": wfHssiBoflNum,
       "wfHssiBoflLen": wfHssiBoflLen,
       "wfHssiRxBufferLength": wfHssiRxBufferLength,
       "wfHssiMemPageLength": wfHssiMemPageLength,
       "wfHssiRxRingLength": wfHssiRxRingLength,
       "wfHssiTxRingLength": wfHssiTxRingLength,
       "wfHssiRxFifoWatermark": wfHssiRxFifoWatermark,
       "wfHssiTxFifoWatermark": wfHssiTxFifoWatermark,
       "wfHssiMaxRxMemory": wfHssiMaxRxMemory,
       "wfHssiLinkInterface": wfHssiLinkInterface,
       "wfHssiTurboBofl": wfHssiTurboBofl,
       "wfHssiCfgRxQueueLength": wfHssiCfgRxQueueLength,
       "wfHssiCfgTxQueueLength": wfHssiCfgTxQueueLength,
       "wfHssiLineNumber": wfHssiLineNumber,
       "wfHssiCfgCngstCtlEnable": wfHssiCfgCngstCtlEnable,
       "wfHssiLastChange": wfHssiLastChange,
       "wfHssiOutQLen": wfHssiOutQLen,
       "wfHssiCarrLossDebounceTmo": wfHssiCarrLossDebounceTmo,
       "wfHssiModule": wfHssiModule,
       "wfHssiActualConnector": wfHssiActualConnector,
       "wfHssiLoopback": wfHssiLoopback,
       "wfHssiReceiveAllFrames": wfHssiReceiveAllFrames}
)

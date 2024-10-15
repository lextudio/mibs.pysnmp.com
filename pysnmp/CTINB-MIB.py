# SNMP MIB module (CTINB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTINB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:27 2024
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

(ctINBinfo,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctINBinfo")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InbMonarchSystem_ObjectIdentity = ObjectIdentity
inbMonarchSystem = _InbMonarchSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1)
)
_InbMonarchSystemTable_Object = MibTable
inbMonarchSystemTable = _InbMonarchSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    inbMonarchSystemTable.setStatus("mandatory")
_InbMonarchSystemEntry_Object = MibTableRow
inbMonarchSystemEntry = _InbMonarchSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1)
)
inbMonarchSystemEntry.setIndexNames(
    (0, "CTINB-MIB", "inbMonarchINB"),
)
if mibBuilder.loadTexts:
    inbMonarchSystemEntry.setStatus("mandatory")


class _InbMonarchSystemINB_Type(Integer32):
    """Custom type inbMonarchSystemINB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbA", 1),
          ("inbB", 2))
    )


_InbMonarchSystemINB_Type.__name__ = "Integer32"
_InbMonarchSystemINB_Object = MibTableColumn
inbMonarchSystemINB = _InbMonarchSystemINB_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 1),
    _InbMonarchSystemINB_Type()
)
inbMonarchSystemINB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchSystemINB.setStatus("mandatory")
_InbMonarchStatusTimeStamp_Type = TimeTicks
_InbMonarchStatusTimeStamp_Object = MibTableColumn
inbMonarchStatusTimeStamp = _InbMonarchStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 2),
    _InbMonarchStatusTimeStamp_Type()
)
inbMonarchStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchStatusTimeStamp.setStatus("mandatory")
_InbMonarchBandwidth_Type = Integer32
_InbMonarchBandwidth_Object = MibTableColumn
inbMonarchBandwidth = _InbMonarchBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 3),
    _InbMonarchBandwidth_Type()
)
inbMonarchBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchBandwidth.setStatus("mandatory")


class _InbMonarchTDMSlotMode_Type(Integer32):
    """Custom type inbMonarchTDMSlotMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("userPolicy", 2))
    )


_InbMonarchTDMSlotMode_Type.__name__ = "Integer32"
_InbMonarchTDMSlotMode_Object = MibTableColumn
inbMonarchTDMSlotMode = _InbMonarchTDMSlotMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 4),
    _InbMonarchTDMSlotMode_Type()
)
inbMonarchTDMSlotMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbMonarchTDMSlotMode.setStatus("mandatory")
_InbMonarchTDMSlotTotal_Type = Integer32
_InbMonarchTDMSlotTotal_Object = MibTableColumn
inbMonarchTDMSlotTotal = _InbMonarchTDMSlotTotal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 5),
    _InbMonarchTDMSlotTotal_Type()
)
inbMonarchTDMSlotTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchTDMSlotTotal.setStatus("mandatory")
_InbMonarchSystemTDMSlotActual_Type = Integer32
_InbMonarchSystemTDMSlotActual_Object = MibTableColumn
inbMonarchSystemTDMSlotActual = _InbMonarchSystemTDMSlotActual_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 6),
    _InbMonarchSystemTDMSlotActual_Type()
)
inbMonarchSystemTDMSlotActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchSystemTDMSlotActual.setStatus("mandatory")
_InbMonarchTDMSlotbandwidth_Type = Integer32
_InbMonarchTDMSlotbandwidth_Object = MibTableColumn
inbMonarchTDMSlotbandwidth = _InbMonarchTDMSlotbandwidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 7),
    _InbMonarchTDMSlotbandwidth_Type()
)
inbMonarchTDMSlotbandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchTDMSlotbandwidth.setStatus("mandatory")
_InbMonarch_ObjectIdentity = ObjectIdentity
inbMonarch = _InbMonarch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2)
)
_InbMonarchTable_Object = MibTable
inbMonarchTable = _InbMonarchTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    inbMonarchTable.setStatus("mandatory")
_InbMonarchEntry_Object = MibTableRow
inbMonarchEntry = _InbMonarchEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1)
)
inbMonarchEntry.setIndexNames(
    (0, "CTINB-MIB", "inbMonarchSlot"),
    (0, "CTINB-MIB", "inbMonarchINB"),
)
if mibBuilder.loadTexts:
    inbMonarchEntry.setStatus("mandatory")
_InbMonarchSlot_Type = Integer32
_InbMonarchSlot_Object = MibTableColumn
inbMonarchSlot = _InbMonarchSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 1),
    _InbMonarchSlot_Type()
)
inbMonarchSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchSlot.setStatus("mandatory")


class _InbMonarchINB_Type(Integer32):
    """Custom type inbMonarchINB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbA", 1),
          ("inbB", 2))
    )


_InbMonarchINB_Type.__name__ = "Integer32"
_InbMonarchINB_Object = MibTableColumn
inbMonarchINB = _InbMonarchINB_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 2),
    _InbMonarchINB_Type()
)
inbMonarchINB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchINB.setStatus("mandatory")


class _InbMonarchStatus_Type(Integer32):
    """Custom type inbMonarchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operational", 3),
          ("standBy", 1),
          ("sysUndefined", 2))
    )


_InbMonarchStatus_Type.__name__ = "Integer32"
_InbMonarchStatus_Object = MibTableColumn
inbMonarchStatus = _InbMonarchStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 3),
    _InbMonarchStatus_Type()
)
inbMonarchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchStatus.setStatus("mandatory")


class _InbMonarchLinkStatus_Type(Integer32):
    """Custom type inbMonarchLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1))
    )


_InbMonarchLinkStatus_Type.__name__ = "Integer32"
_InbMonarchLinkStatus_Object = MibTableColumn
inbMonarchLinkStatus = _InbMonarchLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 4),
    _InbMonarchLinkStatus_Type()
)
inbMonarchLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchLinkStatus.setStatus("mandatory")
_InbMonarchLinkCapacity_Type = Integer32
_InbMonarchLinkCapacity_Object = MibTableColumn
inbMonarchLinkCapacity = _InbMonarchLinkCapacity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 5),
    _InbMonarchLinkCapacity_Type()
)
inbMonarchLinkCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchLinkCapacity.setStatus("mandatory")
_InbMonarchTDMSlotRequest_Type = Integer32
_InbMonarchTDMSlotRequest_Object = MibTableColumn
inbMonarchTDMSlotRequest = _InbMonarchTDMSlotRequest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 6),
    _InbMonarchTDMSlotRequest_Type()
)
inbMonarchTDMSlotRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbMonarchTDMSlotRequest.setStatus("mandatory")
_InbMonarchTDMSlotActual_Type = Integer32
_InbMonarchTDMSlotActual_Object = MibTableColumn
inbMonarchTDMSlotActual = _InbMonarchTDMSlotActual_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 7),
    _InbMonarchTDMSlotActual_Type()
)
inbMonarchTDMSlotActual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbMonarchTDMSlotActual.setStatus("mandatory")


class _InbMonarchRoundRobinControl_Type(Integer32):
    """Custom type inbMonarchRoundRobinControl based on Integer32"""
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


_InbMonarchRoundRobinControl_Type.__name__ = "Integer32"
_InbMonarchRoundRobinControl_Object = MibTableColumn
inbMonarchRoundRobinControl = _InbMonarchRoundRobinControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 8),
    _InbMonarchRoundRobinControl_Type()
)
inbMonarchRoundRobinControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbMonarchRoundRobinControl.setStatus("mandatory")
_InbStats_ObjectIdentity = ObjectIdentity
inbStats = _InbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3)
)
_InbStatsTable_Object = MibTable
inbStatsTable = _InbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    inbStatsTable.setStatus("mandatory")
_InbStatsEntry_Object = MibTableRow
inbStatsEntry = _InbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1)
)
inbStatsEntry.setIndexNames(
    (0, "CTINB-MIB", "inbStatsSlot"),
    (0, "CTINB-MIB", "inbStatsINB"),
)
if mibBuilder.loadTexts:
    inbStatsEntry.setStatus("mandatory")
_InbStatsSlot_Type = Integer32
_InbStatsSlot_Object = MibTableColumn
inbStatsSlot = _InbStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 1),
    _InbStatsSlot_Type()
)
inbStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsSlot.setStatus("mandatory")


class _InbStatsINB_Type(Integer32):
    """Custom type inbStatsINB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbA", 1),
          ("inbB", 2))
    )


_InbStatsINB_Type.__name__ = "Integer32"
_InbStatsINB_Object = MibTableColumn
inbStatsINB = _InbStatsINB_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 2),
    _InbStatsINB_Type()
)
inbStatsINB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsINB.setStatus("mandatory")
_InbStatsIfindex_Type = Integer32
_InbStatsIfindex_Object = MibTableColumn
inbStatsIfindex = _InbStatsIfindex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 3),
    _InbStatsIfindex_Type()
)
inbStatsIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsIfindex.setStatus("mandatory")
_InbStatsUniCastCells_Type = Counter32
_InbStatsUniCastCells_Object = MibTableColumn
inbStatsUniCastCells = _InbStatsUniCastCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 4),
    _InbStatsUniCastCells_Type()
)
inbStatsUniCastCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsUniCastCells.setStatus("mandatory")
_InbStatsMultiCastCells_Type = Counter32
_InbStatsMultiCastCells_Object = MibTableColumn
inbStatsMultiCastCells = _InbStatsMultiCastCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 5),
    _InbStatsMultiCastCells_Type()
)
inbStatsMultiCastCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsMultiCastCells.setStatus("mandatory")
_InbStatsBroadCastCells_Type = Counter32
_InbStatsBroadCastCells_Object = MibTableColumn
inbStatsBroadCastCells = _InbStatsBroadCastCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 6),
    _InbStatsBroadCastCells_Type()
)
inbStatsBroadCastCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsBroadCastCells.setStatus("mandatory")
_InbStatsXmitCells_Type = Counter32
_InbStatsXmitCells_Object = MibTableColumn
inbStatsXmitCells = _InbStatsXmitCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 7),
    _InbStatsXmitCells_Type()
)
inbStatsXmitCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsXmitCells.setStatus("mandatory")
_InbStatsRecvSeqErrs_Type = Counter32
_InbStatsRecvSeqErrs_Object = MibTableColumn
inbStatsRecvSeqErrs = _InbStatsRecvSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 8),
    _InbStatsRecvSeqErrs_Type()
)
inbStatsRecvSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsRecvSeqErrs.setStatus("mandatory")
_InbStatsRecvChksumErrs_Type = Counter32
_InbStatsRecvChksumErrs_Object = MibTableColumn
inbStatsRecvChksumErrs = _InbStatsRecvChksumErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 9),
    _InbStatsRecvChksumErrs_Type()
)
inbStatsRecvChksumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsRecvChksumErrs.setStatus("mandatory")
_InbStatsxmitToFps_Type = Counter32
_InbStatsxmitToFps_Object = MibTableColumn
inbStatsxmitToFps = _InbStatsxmitToFps_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 10),
    _InbStatsxmitToFps_Type()
)
inbStatsxmitToFps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsxmitToFps.setStatus("mandatory")
_InbStatsToFpsDrops_Type = Counter32
_InbStatsToFpsDrops_Object = MibTableColumn
inbStatsToFpsDrops = _InbStatsToFpsDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 11),
    _InbStatsToFpsDrops_Type()
)
inbStatsToFpsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsToFpsDrops.setStatus("mandatory")
_InbStatsFromInbErrs_Type = Counter32
_InbStatsFromInbErrs_Object = MibTableColumn
inbStatsFromInbErrs = _InbStatsFromInbErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 12),
    _InbStatsFromInbErrs_Type()
)
inbStatsFromInbErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsFromInbErrs.setStatus("mandatory")
_InbStatsToINBDrops_Type = Counter32
_InbStatsToINBDrops_Object = MibTableColumn
inbStatsToINBDrops = _InbStatsToINBDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 13),
    _InbStatsToINBDrops_Type()
)
inbStatsToINBDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsToINBDrops.setStatus("mandatory")
_InbStatsToInbErrs_Type = Counter32
_InbStatsToInbErrs_Object = MibTableColumn
inbStatsToInbErrs = _InbStatsToInbErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 14),
    _InbStatsToInbErrs_Type()
)
inbStatsToInbErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbStatsToInbErrs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTINB-MIB",
    **{"inbMonarchSystem": inbMonarchSystem,
       "inbMonarchSystemTable": inbMonarchSystemTable,
       "inbMonarchSystemEntry": inbMonarchSystemEntry,
       "inbMonarchSystemINB": inbMonarchSystemINB,
       "inbMonarchStatusTimeStamp": inbMonarchStatusTimeStamp,
       "inbMonarchBandwidth": inbMonarchBandwidth,
       "inbMonarchTDMSlotMode": inbMonarchTDMSlotMode,
       "inbMonarchTDMSlotTotal": inbMonarchTDMSlotTotal,
       "inbMonarchSystemTDMSlotActual": inbMonarchSystemTDMSlotActual,
       "inbMonarchTDMSlotbandwidth": inbMonarchTDMSlotbandwidth,
       "inbMonarch": inbMonarch,
       "inbMonarchTable": inbMonarchTable,
       "inbMonarchEntry": inbMonarchEntry,
       "inbMonarchSlot": inbMonarchSlot,
       "inbMonarchINB": inbMonarchINB,
       "inbMonarchStatus": inbMonarchStatus,
       "inbMonarchLinkStatus": inbMonarchLinkStatus,
       "inbMonarchLinkCapacity": inbMonarchLinkCapacity,
       "inbMonarchTDMSlotRequest": inbMonarchTDMSlotRequest,
       "inbMonarchTDMSlotActual": inbMonarchTDMSlotActual,
       "inbMonarchRoundRobinControl": inbMonarchRoundRobinControl,
       "inbStats": inbStats,
       "inbStatsTable": inbStatsTable,
       "inbStatsEntry": inbStatsEntry,
       "inbStatsSlot": inbStatsSlot,
       "inbStatsINB": inbStatsINB,
       "inbStatsIfindex": inbStatsIfindex,
       "inbStatsUniCastCells": inbStatsUniCastCells,
       "inbStatsMultiCastCells": inbStatsMultiCastCells,
       "inbStatsBroadCastCells": inbStatsBroadCastCells,
       "inbStatsXmitCells": inbStatsXmitCells,
       "inbStatsRecvSeqErrs": inbStatsRecvSeqErrs,
       "inbStatsRecvChksumErrs": inbStatsRecvChksumErrs,
       "inbStatsxmitToFps": inbStatsxmitToFps,
       "inbStatsToFpsDrops": inbStatsToFpsDrops,
       "inbStatsFromInbErrs": inbStatsFromInbErrs,
       "inbStatsToINBDrops": inbStatsToINBDrops,
       "inbStatsToInbErrs": inbStatsToInbErrs}
)

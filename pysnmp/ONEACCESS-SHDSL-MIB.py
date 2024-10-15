# SNMP MIB module (ONEACCESS-SHDSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-SHDSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:03 2024
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

(hdsl2ShdslEndpointCurrEntry,
 hdsl2ShdslSpanConfProfileEntry,
 hdsl2ShdslSpanStatusEntry) = mibBuilder.importSymbols(
    "HDSL2-SHDSL-LINE-MIB",
    "hdsl2ShdslEndpointCurrEntry",
    "hdsl2ShdslSpanConfProfileEntry",
    "hdsl2ShdslSpanStatusEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(oacExpIMSystem,) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMSystem")

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

oacSHDSLMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3)
)
oacSHDSLMIBModule.setRevisions(
        ("2011-06-15 00:00",
         "2010-08-20 00:01",
         "2010-07-30 00:01",
         "2010-07-08 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacSHDSLObjects_ObjectIdentity = ObjectIdentity
oacSHDSLObjects = _OacSHDSLObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1)
)
_OacSHDSLSpanStatusTable_Object = MibTable
oacSHDSLSpanStatusTable = _OacSHDSLSpanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusTable.setStatus("current")
_OacSHDSLSpanStatusEntry_Object = MibTableRow
oacSHDSLSpanStatusEntry = _OacSHDSLSpanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusEntry.setStatus("current")
_OacSHDSLSpanStatusUpDown_Type = Counter32
_OacSHDSLSpanStatusUpDown_Object = MibTableColumn
oacSHDSLSpanStatusUpDown = _OacSHDSLSpanStatusUpDown_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 1),
    _OacSHDSLSpanStatusUpDown_Type()
)
oacSHDSLSpanStatusUpDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusUpDown.setStatus("current")


class _OacSHDSLSpanStatusCurrStatus_Type(OctetString):
    """Custom type oacSHDSLSpanStatusCurrStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_OacSHDSLSpanStatusCurrStatus_Type.__name__ = "OctetString"
_OacSHDSLSpanStatusCurrStatus_Object = MibTableColumn
oacSHDSLSpanStatusCurrStatus = _OacSHDSLSpanStatusCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 2),
    _OacSHDSLSpanStatusCurrStatus_Type()
)
oacSHDSLSpanStatusCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrStatus.setStatus("current")
_OacSHDSLSpanStatusCurrShowtimeStart_Type = Counter32
_OacSHDSLSpanStatusCurrShowtimeStart_Object = MibTableColumn
oacSHDSLSpanStatusCurrShowtimeStart = _OacSHDSLSpanStatusCurrShowtimeStart_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 3),
    _OacSHDSLSpanStatusCurrShowtimeStart_Type()
)
oacSHDSLSpanStatusCurrShowtimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrShowtimeStart.setStatus("current")
_OacSHDSLSpanStatusCurrCellDelin_Type = Counter32
_OacSHDSLSpanStatusCurrCellDelin_Object = MibTableColumn
oacSHDSLSpanStatusCurrCellDelin = _OacSHDSLSpanStatusCurrCellDelin_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 4),
    _OacSHDSLSpanStatusCurrCellDelin_Type()
)
oacSHDSLSpanStatusCurrCellDelin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrCellDelin.setStatus("current")
_OacSHDSLSpanStatusCurrCRCanomalies_Type = Counter32
_OacSHDSLSpanStatusCurrCRCanomalies_Object = MibTableColumn
oacSHDSLSpanStatusCurrCRCanomalies = _OacSHDSLSpanStatusCurrCRCanomalies_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 5),
    _OacSHDSLSpanStatusCurrCRCanomalies_Type()
)
oacSHDSLSpanStatusCurrCRCanomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrCRCanomalies.setStatus("current")
_OacSHDSLSpanStatusCurrHECErrors_Type = Counter32
_OacSHDSLSpanStatusCurrHECErrors_Object = MibTableColumn
oacSHDSLSpanStatusCurrHECErrors = _OacSHDSLSpanStatusCurrHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 6),
    _OacSHDSLSpanStatusCurrHECErrors_Type()
)
oacSHDSLSpanStatusCurrHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrHECErrors.setStatus("current")
_OacSHDSLSpanStatusCurrRxCells_Type = Counter32
_OacSHDSLSpanStatusCurrRxCells_Object = MibTableColumn
oacSHDSLSpanStatusCurrRxCells = _OacSHDSLSpanStatusCurrRxCells_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 7),
    _OacSHDSLSpanStatusCurrRxCells_Type()
)
oacSHDSLSpanStatusCurrRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrRxCells.setStatus("current")
_OacSHDSLSpanStatusCurrTxCells_Type = Counter32
_OacSHDSLSpanStatusCurrTxCells_Object = MibTableColumn
oacSHDSLSpanStatusCurrTxCells = _OacSHDSLSpanStatusCurrTxCells_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 8),
    _OacSHDSLSpanStatusCurrTxCells_Type()
)
oacSHDSLSpanStatusCurrTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrTxCells.setStatus("current")
_OacSHDSLSpanStatusCurrRxDrops_Type = Counter32
_OacSHDSLSpanStatusCurrRxDrops_Object = MibTableColumn
oacSHDSLSpanStatusCurrRxDrops = _OacSHDSLSpanStatusCurrRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 9),
    _OacSHDSLSpanStatusCurrRxDrops_Type()
)
oacSHDSLSpanStatusCurrRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrRxDrops.setStatus("current")
_OacSHDSLSpanStatusCurrES_Type = Counter32
_OacSHDSLSpanStatusCurrES_Object = MibTableColumn
oacSHDSLSpanStatusCurrES = _OacSHDSLSpanStatusCurrES_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 10),
    _OacSHDSLSpanStatusCurrES_Type()
)
oacSHDSLSpanStatusCurrES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrES.setStatus("current")
_OacSHDSLSpanStatusCurrSES_Type = Counter32
_OacSHDSLSpanStatusCurrSES_Object = MibTableColumn
oacSHDSLSpanStatusCurrSES = _OacSHDSLSpanStatusCurrSES_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 11),
    _OacSHDSLSpanStatusCurrSES_Type()
)
oacSHDSLSpanStatusCurrSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrSES.setStatus("current")
_OacSHDSLSpanStatusCurrLOSWS_Type = Counter32
_OacSHDSLSpanStatusCurrLOSWS_Object = MibTableColumn
oacSHDSLSpanStatusCurrLOSWS = _OacSHDSLSpanStatusCurrLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 12),
    _OacSHDSLSpanStatusCurrLOSWS_Type()
)
oacSHDSLSpanStatusCurrLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrLOSWS.setStatus("current")
_OacSHDSLSpanStatusCurrUAS_Type = Counter32
_OacSHDSLSpanStatusCurrUAS_Object = MibTableColumn
oacSHDSLSpanStatusCurrUAS = _OacSHDSLSpanStatusCurrUAS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 13),
    _OacSHDSLSpanStatusCurrUAS_Type()
)
oacSHDSLSpanStatusCurrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrUAS.setStatus("current")


class _OacSHDSLSpanStatusCurrConstellation_Type(Integer32):
    """Custom type oacSHDSLSpanStatusCurrConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcPam16", 2),
          ("tcPam32", 3))
    )


_OacSHDSLSpanStatusCurrConstellation_Type.__name__ = "Integer32"
_OacSHDSLSpanStatusCurrConstellation_Object = MibTableColumn
oacSHDSLSpanStatusCurrConstellation = _OacSHDSLSpanStatusCurrConstellation_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 14),
    _OacSHDSLSpanStatusCurrConstellation_Type()
)
oacSHDSLSpanStatusCurrConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanStatusCurrConstellation.setStatus("current")
_OacSHDSLEndpointCurrTable_Object = MibTable
oacSHDSLEndpointCurrTable = _OacSHDSLEndpointCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5)
)
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrTable.setStatus("current")
_OacSHDSLEndpointCurrEntry_Object = MibTableRow
oacSHDSLEndpointCurrEntry = _OacSHDSLEndpointCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrEntry.setStatus("current")


class _OacSHDSLEndpointCurrAtn_Type(Integer32):
    """Custom type oacSHDSLEndpointCurrAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1270, 1280),
    )


_OacSHDSLEndpointCurrAtn_Type.__name__ = "Integer32"
_OacSHDSLEndpointCurrAtn_Object = MibTableColumn
oacSHDSLEndpointCurrAtn = _OacSHDSLEndpointCurrAtn_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 1),
    _OacSHDSLEndpointCurrAtn_Type()
)
oacSHDSLEndpointCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrAtn.setUnits("dB/10")


class _OacSHDSLEndpointCurrSnrMgn_Type(Integer32):
    """Custom type oacSHDSLEndpointCurrSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1270, 1280),
    )


_OacSHDSLEndpointCurrSnrMgn_Type.__name__ = "Integer32"
_OacSHDSLEndpointCurrSnrMgn_Object = MibTableColumn
oacSHDSLEndpointCurrSnrMgn = _OacSHDSLEndpointCurrSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 2),
    _OacSHDSLEndpointCurrSnrMgn_Type()
)
oacSHDSLEndpointCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrSnrMgn.setUnits("dB/10")
_OacSHDSLEndpointCurrTxPwr_Type = Integer32
_OacSHDSLEndpointCurrTxPwr_Object = MibTableColumn
oacSHDSLEndpointCurrTxPwr = _OacSHDSLEndpointCurrTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 3),
    _OacSHDSLEndpointCurrTxPwr_Type()
)
oacSHDSLEndpointCurrTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrTxPwr.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrTxPwr.setUnits("dB/10")
_OacSHDSLEndpointCurrRxGain_Type = Integer32
_OacSHDSLEndpointCurrRxGain_Object = MibTableColumn
oacSHDSLEndpointCurrRxGain = _OacSHDSLEndpointCurrRxGain_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 4),
    _OacSHDSLEndpointCurrRxGain_Type()
)
oacSHDSLEndpointCurrRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrRxGain.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrRxGain.setUnits("dB/10")
_OacSHDSLEndpointCurrMaxAttainableLineRate_Type = Integer32
_OacSHDSLEndpointCurrMaxAttainableLineRate_Object = MibTableColumn
oacSHDSLEndpointCurrMaxAttainableLineRate = _OacSHDSLEndpointCurrMaxAttainableLineRate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 5),
    _OacSHDSLEndpointCurrMaxAttainableLineRate_Type()
)
oacSHDSLEndpointCurrMaxAttainableLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrMaxAttainableLineRate.setStatus("current")
_OacSHDSLEndpointCurrCommands_Type = Integer32
_OacSHDSLEndpointCurrCommands_Object = MibTableColumn
oacSHDSLEndpointCurrCommands = _OacSHDSLEndpointCurrCommands_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 6),
    _OacSHDSLEndpointCurrCommands_Type()
)
oacSHDSLEndpointCurrCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrCommands.setStatus("current")
_OacSHDSLEndpointCurrResponses_Type = Integer32
_OacSHDSLEndpointCurrResponses_Object = MibTableColumn
oacSHDSLEndpointCurrResponses = _OacSHDSLEndpointCurrResponses_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 7),
    _OacSHDSLEndpointCurrResponses_Type()
)
oacSHDSLEndpointCurrResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrResponses.setStatus("current")
_OacSHDSLEndpointCurrdiscardedCommands_Type = Integer32
_OacSHDSLEndpointCurrdiscardedCommands_Object = MibTableColumn
oacSHDSLEndpointCurrdiscardedCommands = _OacSHDSLEndpointCurrdiscardedCommands_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 8),
    _OacSHDSLEndpointCurrdiscardedCommands_Type()
)
oacSHDSLEndpointCurrdiscardedCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrdiscardedCommands.setStatus("current")
_OacSHDSLEndpointCurrerroredCommands_Type = Integer32
_OacSHDSLEndpointCurrerroredCommands_Object = MibTableColumn
oacSHDSLEndpointCurrerroredCommands = _OacSHDSLEndpointCurrerroredCommands_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 9),
    _OacSHDSLEndpointCurrerroredCommands_Type()
)
oacSHDSLEndpointCurrerroredCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrerroredCommands.setStatus("current")
_OacSHDSLEndpointCurrReceivedFrames_Type = Integer32
_OacSHDSLEndpointCurrReceivedFrames_Object = MibTableColumn
oacSHDSLEndpointCurrReceivedFrames = _OacSHDSLEndpointCurrReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 10),
    _OacSHDSLEndpointCurrReceivedFrames_Type()
)
oacSHDSLEndpointCurrReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrReceivedFrames.setStatus("current")
_OacSHDSLEndpointCurrBadTransparency_Type = Integer32
_OacSHDSLEndpointCurrBadTransparency_Object = MibTableColumn
oacSHDSLEndpointCurrBadTransparency = _OacSHDSLEndpointCurrBadTransparency_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 11),
    _OacSHDSLEndpointCurrBadTransparency_Type()
)
oacSHDSLEndpointCurrBadTransparency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrBadTransparency.setStatus("current")
_OacSHDSLEndpointCurrBadFCS_Type = Integer32
_OacSHDSLEndpointCurrBadFCS_Object = MibTableColumn
oacSHDSLEndpointCurrBadFCS = _OacSHDSLEndpointCurrBadFCS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 12),
    _OacSHDSLEndpointCurrBadFCS_Type()
)
oacSHDSLEndpointCurrBadFCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrBadFCS.setStatus("current")


class _OacSHDSLEndpointCurrEOCStatus_Type(OctetString):
    """Custom type oacSHDSLEndpointCurrEOCStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )


_OacSHDSLEndpointCurrEOCStatus_Type.__name__ = "OctetString"
_OacSHDSLEndpointCurrEOCStatus_Object = MibTableColumn
oacSHDSLEndpointCurrEOCStatus = _OacSHDSLEndpointCurrEOCStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 13),
    _OacSHDSLEndpointCurrEOCStatus_Type()
)
oacSHDSLEndpointCurrEOCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrEOCStatus.setStatus("current")
_OacSHDSLEndpointCurrretrainTable_Object = MibTable
oacSHDSLEndpointCurrretrainTable = _OacSHDSLEndpointCurrretrainTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7)
)
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainTable.setStatus("current")
_OacSHDSLEndpointCurrretrainEntry_Object = MibTableRow
oacSHDSLEndpointCurrretrainEntry = _OacSHDSLEndpointCurrretrainEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainEntry.setStatus("current")
_OacSHDSLEndpointCurrretrainSQPAIR_Type = Integer32
_OacSHDSLEndpointCurrretrainSQPAIR_Object = MibTableColumn
oacSHDSLEndpointCurrretrainSQPAIR = _OacSHDSLEndpointCurrretrainSQPAIR_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 1),
    _OacSHDSLEndpointCurrretrainSQPAIR_Type()
)
oacSHDSLEndpointCurrretrainSQPAIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainSQPAIR.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainSQPAIR.setUnits("SQPAIR")
_OacSHDSLEndpointCurrretrainSQLINE_Type = Integer32
_OacSHDSLEndpointCurrretrainSQLINE_Object = MibTableColumn
oacSHDSLEndpointCurrretrainSQLINE = _OacSHDSLEndpointCurrretrainSQLINE_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 2),
    _OacSHDSLEndpointCurrretrainSQLINE_Type()
)
oacSHDSLEndpointCurrretrainSQLINE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainSQLINE.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainSQLINE.setUnits("SQLINE")
_OacSHDSLEndpointCurrretrainCRCPAIR_Type = Integer32
_OacSHDSLEndpointCurrretrainCRCPAIR_Object = MibTableColumn
oacSHDSLEndpointCurrretrainCRCPAIR = _OacSHDSLEndpointCurrretrainCRCPAIR_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 3),
    _OacSHDSLEndpointCurrretrainCRCPAIR_Type()
)
oacSHDSLEndpointCurrretrainCRCPAIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainCRCPAIR.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainCRCPAIR.setUnits("CRCPAIR")
_OacSHDSLEndpointCurrretrainCRCLINE_Type = Integer32
_OacSHDSLEndpointCurrretrainCRCLINE_Object = MibTableColumn
oacSHDSLEndpointCurrretrainCRCLINE = _OacSHDSLEndpointCurrretrainCRCLINE_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 4),
    _OacSHDSLEndpointCurrretrainCRCLINE_Type()
)
oacSHDSLEndpointCurrretrainCRCLINE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainCRCLINE.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainCRCLINE.setUnits("CRCLINE")
_OacSHDSLEndpointCurrretrainFsyncPAIR_Type = Integer32
_OacSHDSLEndpointCurrretrainFsyncPAIR_Object = MibTableColumn
oacSHDSLEndpointCurrretrainFsyncPAIR = _OacSHDSLEndpointCurrretrainFsyncPAIR_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 5),
    _OacSHDSLEndpointCurrretrainFsyncPAIR_Type()
)
oacSHDSLEndpointCurrretrainFsyncPAIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainFsyncPAIR.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainFsyncPAIR.setUnits("FsyncPAIR")
_OacSHDSLEndpointCurrretrainFsyncLINE_Type = Integer32
_OacSHDSLEndpointCurrretrainFsyncLINE_Object = MibTableColumn
oacSHDSLEndpointCurrretrainFsyncLINE = _OacSHDSLEndpointCurrretrainFsyncLINE_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 6),
    _OacSHDSLEndpointCurrretrainFsyncLINE_Type()
)
oacSHDSLEndpointCurrretrainFsyncLINE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainFsyncLINE.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainFsyncLINE.setUnits("FsyncLINE")
_OacSHDSLEndpointCurrretrainFSyncSQPAIR_Type = Integer32
_OacSHDSLEndpointCurrretrainFSyncSQPAIR_Object = MibTableColumn
oacSHDSLEndpointCurrretrainFSyncSQPAIR = _OacSHDSLEndpointCurrretrainFSyncSQPAIR_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 7),
    _OacSHDSLEndpointCurrretrainFSyncSQPAIR_Type()
)
oacSHDSLEndpointCurrretrainFSyncSQPAIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainFSyncSQPAIR.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainFSyncSQPAIR.setUnits("FSync&SQPAIR")
_OacSHDSLEndpointCurrretrainFSyncSQLINE_Type = Integer32
_OacSHDSLEndpointCurrretrainFSyncSQLINE_Object = MibTableColumn
oacSHDSLEndpointCurrretrainFSyncSQLINE = _OacSHDSLEndpointCurrretrainFSyncSQLINE_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 8),
    _OacSHDSLEndpointCurrretrainFSyncSQLINE_Type()
)
oacSHDSLEndpointCurrretrainFSyncSQLINE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainFSyncSQLINE.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLEndpointCurrretrainFSyncSQLINE.setUnits("FSync&SQLINE")
_OacSHDSLSpanConfProfileTable_Object = MibTable
oacSHDSLSpanConfProfileTable = _OacSHDSLSpanConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10)
)
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileTable.setStatus("current")
_OacSHDSLSpanConfProfileEntry_Object = MibTableRow
oacSHDSLSpanConfProfileEntry = _OacSHDSLSpanConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1)
)
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileEntry.setStatus("current")


class _OacSHDSLSpanConfProfileConstellation_Type(Integer32):
    """Custom type oacSHDSLSpanConfProfileConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("tcPam16", 2),
          ("tcPam32", 3))
    )


_OacSHDSLSpanConfProfileConstellation_Type.__name__ = "Integer32"
_OacSHDSLSpanConfProfileConstellation_Object = MibTableColumn
oacSHDSLSpanConfProfileConstellation = _OacSHDSLSpanConfProfileConstellation_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 1),
    _OacSHDSLSpanConfProfileConstellation_Type()
)
oacSHDSLSpanConfProfileConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileConstellation.setStatus("current")


class _OacSHDSLSpanConfProfileAutoConfig_Type(Integer32):
    """Custom type oacSHDSLSpanConfProfileAutoConfig based on Integer32"""
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


_OacSHDSLSpanConfProfileAutoConfig_Type.__name__ = "Integer32"
_OacSHDSLSpanConfProfileAutoConfig_Object = MibTableColumn
oacSHDSLSpanConfProfileAutoConfig = _OacSHDSLSpanConfProfileAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 2),
    _OacSHDSLSpanConfProfileAutoConfig_Type()
)
oacSHDSLSpanConfProfileAutoConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileAutoConfig.setStatus("current")


class _OacSHDSLSpanConfProfileCaplist_Type(Integer32):
    """Custom type oacSHDSLSpanConfProfileCaplist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("newstyle", 1),
          ("oldstyle", 2))
    )


_OacSHDSLSpanConfProfileCaplist_Type.__name__ = "Integer32"
_OacSHDSLSpanConfProfileCaplist_Object = MibTableColumn
oacSHDSLSpanConfProfileCaplist = _OacSHDSLSpanConfProfileCaplist_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 3),
    _OacSHDSLSpanConfProfileCaplist_Type()
)
oacSHDSLSpanConfProfileCaplist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileCaplist.setStatus("current")


class _OacSHDSLSpanConfProfileEfmAggregation_Type(Integer32):
    """Custom type oacSHDSLSpanConfProfileEfmAggregation based on Integer32"""
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
        *(("auto", 2),
          ("disabled", 1),
          ("negotiated", 3),
          ("static", 4))
    )


_OacSHDSLSpanConfProfileEfmAggregation_Type.__name__ = "Integer32"
_OacSHDSLSpanConfProfileEfmAggregation_Object = MibTableColumn
oacSHDSLSpanConfProfileEfmAggregation = _OacSHDSLSpanConfProfileEfmAggregation_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 4),
    _OacSHDSLSpanConfProfileEfmAggregation_Type()
)
oacSHDSLSpanConfProfileEfmAggregation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileEfmAggregation.setStatus("current")


class _OacSHDSLSpanConfProfileCrcCheck_Type(Integer32):
    """Custom type oacSHDSLSpanConfProfileCrcCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_OacSHDSLSpanConfProfileCrcCheck_Type.__name__ = "Integer32"
_OacSHDSLSpanConfProfileCrcCheck_Object = MibTableColumn
oacSHDSLSpanConfProfileCrcCheck = _OacSHDSLSpanConfProfileCrcCheck_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 5),
    _OacSHDSLSpanConfProfileCrcCheck_Type()
)
oacSHDSLSpanConfProfileCrcCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileCrcCheck.setStatus("current")


class _OacSHDSLSpanConfProfileMeansqCheck_Type(Integer32):
    """Custom type oacSHDSLSpanConfProfileMeansqCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_OacSHDSLSpanConfProfileMeansqCheck_Type.__name__ = "Integer32"
_OacSHDSLSpanConfProfileMeansqCheck_Object = MibTableColumn
oacSHDSLSpanConfProfileMeansqCheck = _OacSHDSLSpanConfProfileMeansqCheck_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 6),
    _OacSHDSLSpanConfProfileMeansqCheck_Type()
)
oacSHDSLSpanConfProfileMeansqCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileMeansqCheck.setStatus("current")


class _OacSHDSLSpanConfProfileMeansqThreshold_Type(Integer32):
    """Custom type oacSHDSLSpanConfProfileMeansqThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 10),
    )


_OacSHDSLSpanConfProfileMeansqThreshold_Type.__name__ = "Integer32"
_OacSHDSLSpanConfProfileMeansqThreshold_Object = MibTableColumn
oacSHDSLSpanConfProfileMeansqThreshold = _OacSHDSLSpanConfProfileMeansqThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 7),
    _OacSHDSLSpanConfProfileMeansqThreshold_Type()
)
oacSHDSLSpanConfProfileMeansqThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileMeansqThreshold.setStatus("current")


class _OacSHDSLSpanConfProfileLineProbing_Type(Integer32):
    """Custom type oacSHDSLSpanConfProfileLineProbing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 1),
          ("normal", 2))
    )


_OacSHDSLSpanConfProfileLineProbing_Type.__name__ = "Integer32"
_OacSHDSLSpanConfProfileLineProbing_Object = MibTableColumn
oacSHDSLSpanConfProfileLineProbing = _OacSHDSLSpanConfProfileLineProbing_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 8),
    _OacSHDSLSpanConfProfileLineProbing_Type()
)
oacSHDSLSpanConfProfileLineProbing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileLineProbing.setStatus("current")


class _OacSHDSLSpanConfProfileEocManagement_Type(Integer32):
    """Custom type oacSHDSLSpanConfProfileEocManagement based on Integer32"""
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


_OacSHDSLSpanConfProfileEocManagement_Type.__name__ = "Integer32"
_OacSHDSLSpanConfProfileEocManagement_Object = MibTableColumn
oacSHDSLSpanConfProfileEocManagement = _OacSHDSLSpanConfProfileEocManagement_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 9),
    _OacSHDSLSpanConfProfileEocManagement_Type()
)
oacSHDSLSpanConfProfileEocManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileEocManagement.setStatus("current")


class _OacSHDSLSpanConfProfileEocStatusPollDelay_Type(Integer32):
    """Custom type oacSHDSLSpanConfProfileEocStatusPollDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_OacSHDSLSpanConfProfileEocStatusPollDelay_Type.__name__ = "Integer32"
_OacSHDSLSpanConfProfileEocStatusPollDelay_Object = MibTableColumn
oacSHDSLSpanConfProfileEocStatusPollDelay = _OacSHDSLSpanConfProfileEocStatusPollDelay_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 10),
    _OacSHDSLSpanConfProfileEocStatusPollDelay_Type()
)
oacSHDSLSpanConfProfileEocStatusPollDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileEocStatusPollDelay.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileEocStatusPollDelay.setUnits("seconds")


class _OacSHDSLSpanConfProfileEocStatusPollInterval_Type(Integer32):
    """Custom type oacSHDSLSpanConfProfileEocStatusPollInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(120, 120),
    )


_OacSHDSLSpanConfProfileEocStatusPollInterval_Type.__name__ = "Integer32"
_OacSHDSLSpanConfProfileEocStatusPollInterval_Object = MibTableColumn
oacSHDSLSpanConfProfileEocStatusPollInterval = _OacSHDSLSpanConfProfileEocStatusPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 11),
    _OacSHDSLSpanConfProfileEocStatusPollInterval_Type()
)
oacSHDSLSpanConfProfileEocStatusPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileEocStatusPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    oacSHDSLSpanConfProfileEocStatusPollInterval.setUnits("seconds")
_OacSHDSLTraps_ObjectIdentity = ObjectIdentity
oacSHDSLTraps = _OacSHDSLTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 2)
)
_OacSHDSLTrapPrefix_ObjectIdentity = ObjectIdentity
oacSHDSLTrapPrefix = _OacSHDSLTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 2, 0)
)
hdsl2ShdslSpanStatusEntry.registerAugmentions(
    ("ONEACCESS-SHDSL-MIB",
     "oacSHDSLSpanStatusEntry")
)
oacSHDSLSpanStatusEntry.setIndexNames(*hdsl2ShdslSpanStatusEntry.getIndexNames())
hdsl2ShdslEndpointCurrEntry.registerAugmentions(
    ("ONEACCESS-SHDSL-MIB",
     "oacSHDSLEndpointCurrEntry")
)
oacSHDSLEndpointCurrEntry.setIndexNames(*hdsl2ShdslEndpointCurrEntry.getIndexNames())
hdsl2ShdslEndpointCurrEntry.registerAugmentions(
    ("ONEACCESS-SHDSL-MIB",
     "oacSHDSLEndpointCurrretrainEntry")
)
oacSHDSLEndpointCurrretrainEntry.setIndexNames(*hdsl2ShdslEndpointCurrEntry.getIndexNames())
hdsl2ShdslSpanConfProfileEntry.registerAugmentions(
    ("ONEACCESS-SHDSL-MIB",
     "oacSHDSLSpanConfProfileEntry")
)
oacSHDSLSpanConfProfileEntry.setIndexNames(*hdsl2ShdslSpanConfProfileEntry.getIndexNames())

# Managed Objects groups


# Notification objects

oacSHDSLHardDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 2, 0, 1)
)
if mibBuilder.loadTexts:
    oacSHDSLHardDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-SHDSL-MIB",
    **{"oacSHDSLMIBModule": oacSHDSLMIBModule,
       "oacSHDSLObjects": oacSHDSLObjects,
       "oacSHDSLSpanStatusTable": oacSHDSLSpanStatusTable,
       "oacSHDSLSpanStatusEntry": oacSHDSLSpanStatusEntry,
       "oacSHDSLSpanStatusUpDown": oacSHDSLSpanStatusUpDown,
       "oacSHDSLSpanStatusCurrStatus": oacSHDSLSpanStatusCurrStatus,
       "oacSHDSLSpanStatusCurrShowtimeStart": oacSHDSLSpanStatusCurrShowtimeStart,
       "oacSHDSLSpanStatusCurrCellDelin": oacSHDSLSpanStatusCurrCellDelin,
       "oacSHDSLSpanStatusCurrCRCanomalies": oacSHDSLSpanStatusCurrCRCanomalies,
       "oacSHDSLSpanStatusCurrHECErrors": oacSHDSLSpanStatusCurrHECErrors,
       "oacSHDSLSpanStatusCurrRxCells": oacSHDSLSpanStatusCurrRxCells,
       "oacSHDSLSpanStatusCurrTxCells": oacSHDSLSpanStatusCurrTxCells,
       "oacSHDSLSpanStatusCurrRxDrops": oacSHDSLSpanStatusCurrRxDrops,
       "oacSHDSLSpanStatusCurrES": oacSHDSLSpanStatusCurrES,
       "oacSHDSLSpanStatusCurrSES": oacSHDSLSpanStatusCurrSES,
       "oacSHDSLSpanStatusCurrLOSWS": oacSHDSLSpanStatusCurrLOSWS,
       "oacSHDSLSpanStatusCurrUAS": oacSHDSLSpanStatusCurrUAS,
       "oacSHDSLSpanStatusCurrConstellation": oacSHDSLSpanStatusCurrConstellation,
       "oacSHDSLEndpointCurrTable": oacSHDSLEndpointCurrTable,
       "oacSHDSLEndpointCurrEntry": oacSHDSLEndpointCurrEntry,
       "oacSHDSLEndpointCurrAtn": oacSHDSLEndpointCurrAtn,
       "oacSHDSLEndpointCurrSnrMgn": oacSHDSLEndpointCurrSnrMgn,
       "oacSHDSLEndpointCurrTxPwr": oacSHDSLEndpointCurrTxPwr,
       "oacSHDSLEndpointCurrRxGain": oacSHDSLEndpointCurrRxGain,
       "oacSHDSLEndpointCurrMaxAttainableLineRate": oacSHDSLEndpointCurrMaxAttainableLineRate,
       "oacSHDSLEndpointCurrCommands": oacSHDSLEndpointCurrCommands,
       "oacSHDSLEndpointCurrResponses": oacSHDSLEndpointCurrResponses,
       "oacSHDSLEndpointCurrdiscardedCommands": oacSHDSLEndpointCurrdiscardedCommands,
       "oacSHDSLEndpointCurrerroredCommands": oacSHDSLEndpointCurrerroredCommands,
       "oacSHDSLEndpointCurrReceivedFrames": oacSHDSLEndpointCurrReceivedFrames,
       "oacSHDSLEndpointCurrBadTransparency": oacSHDSLEndpointCurrBadTransparency,
       "oacSHDSLEndpointCurrBadFCS": oacSHDSLEndpointCurrBadFCS,
       "oacSHDSLEndpointCurrEOCStatus": oacSHDSLEndpointCurrEOCStatus,
       "oacSHDSLEndpointCurrretrainTable": oacSHDSLEndpointCurrretrainTable,
       "oacSHDSLEndpointCurrretrainEntry": oacSHDSLEndpointCurrretrainEntry,
       "oacSHDSLEndpointCurrretrainSQPAIR": oacSHDSLEndpointCurrretrainSQPAIR,
       "oacSHDSLEndpointCurrretrainSQLINE": oacSHDSLEndpointCurrretrainSQLINE,
       "oacSHDSLEndpointCurrretrainCRCPAIR": oacSHDSLEndpointCurrretrainCRCPAIR,
       "oacSHDSLEndpointCurrretrainCRCLINE": oacSHDSLEndpointCurrretrainCRCLINE,
       "oacSHDSLEndpointCurrretrainFsyncPAIR": oacSHDSLEndpointCurrretrainFsyncPAIR,
       "oacSHDSLEndpointCurrretrainFsyncLINE": oacSHDSLEndpointCurrretrainFsyncLINE,
       "oacSHDSLEndpointCurrretrainFSyncSQPAIR": oacSHDSLEndpointCurrretrainFSyncSQPAIR,
       "oacSHDSLEndpointCurrretrainFSyncSQLINE": oacSHDSLEndpointCurrretrainFSyncSQLINE,
       "oacSHDSLSpanConfProfileTable": oacSHDSLSpanConfProfileTable,
       "oacSHDSLSpanConfProfileEntry": oacSHDSLSpanConfProfileEntry,
       "oacSHDSLSpanConfProfileConstellation": oacSHDSLSpanConfProfileConstellation,
       "oacSHDSLSpanConfProfileAutoConfig": oacSHDSLSpanConfProfileAutoConfig,
       "oacSHDSLSpanConfProfileCaplist": oacSHDSLSpanConfProfileCaplist,
       "oacSHDSLSpanConfProfileEfmAggregation": oacSHDSLSpanConfProfileEfmAggregation,
       "oacSHDSLSpanConfProfileCrcCheck": oacSHDSLSpanConfProfileCrcCheck,
       "oacSHDSLSpanConfProfileMeansqCheck": oacSHDSLSpanConfProfileMeansqCheck,
       "oacSHDSLSpanConfProfileMeansqThreshold": oacSHDSLSpanConfProfileMeansqThreshold,
       "oacSHDSLSpanConfProfileLineProbing": oacSHDSLSpanConfProfileLineProbing,
       "oacSHDSLSpanConfProfileEocManagement": oacSHDSLSpanConfProfileEocManagement,
       "oacSHDSLSpanConfProfileEocStatusPollDelay": oacSHDSLSpanConfProfileEocStatusPollDelay,
       "oacSHDSLSpanConfProfileEocStatusPollInterval": oacSHDSLSpanConfProfileEocStatusPollInterval,
       "oacSHDSLTraps": oacSHDSLTraps,
       "oacSHDSLTrapPrefix": oacSHDSLTrapPrefix,
       "oacSHDSLHardDownTrap": oacSHDSLHardDownTrap}
)

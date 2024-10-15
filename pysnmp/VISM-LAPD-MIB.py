# SNMP MIB module (VISM-LAPD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VISM-LAPD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:38 2024
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

(voice,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "voice")

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

_VismLapdGrp_ObjectIdentity = ObjectIdentity
vismLapdGrp = _VismLapdGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12)
)
_VismLapdTable_Object = MibTable
vismLapdTable = _VismLapdTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1)
)
if mibBuilder.loadTexts:
    vismLapdTable.setStatus("mandatory")
_VismLapdEntry_Object = MibTableRow
vismLapdEntry = _VismLapdEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1)
)
vismLapdEntry.setIndexNames(
    (0, "VISM-LAPD-MIB", "vismLapdIndex"),
)
if mibBuilder.loadTexts:
    vismLapdEntry.setStatus("mandatory")


class _VismLapdIndex_Type(Integer32):
    """Custom type vismLapdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VismLapdIndex_Type.__name__ = "Integer32"
_VismLapdIndex_Object = MibTableColumn
vismLapdIndex = _VismLapdIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 1),
    _VismLapdIndex_Type()
)
vismLapdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdIndex.setStatus("mandatory")


class _VismLapdAppType_Type(Integer32):
    """Custom type vismLapdAppType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gr-303", 2),
          ("pri", 1))
    )


_VismLapdAppType_Type.__name__ = "Integer32"
_VismLapdAppType_Object = MibTableColumn
vismLapdAppType = _VismLapdAppType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 2),
    _VismLapdAppType_Type()
)
vismLapdAppType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismLapdAppType.setStatus("mandatory")


class _VismLapdWinSize_Type(Integer32):
    """Custom type vismLapdWinSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VismLapdWinSize_Type.__name__ = "Integer32"
_VismLapdWinSize_Object = MibTableColumn
vismLapdWinSize = _VismLapdWinSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 3),
    _VismLapdWinSize_Type()
)
vismLapdWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismLapdWinSize.setStatus("mandatory")


class _VismLapdN200_Type(Integer32):
    """Custom type vismLapdN200 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VismLapdN200_Type.__name__ = "Integer32"
_VismLapdN200_Object = MibTableColumn
vismLapdN200 = _VismLapdN200_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 4),
    _VismLapdN200_Type()
)
vismLapdN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismLapdN200.setStatus("mandatory")


class _VismLapdT200_Type(Integer32):
    """Custom type vismLapdT200 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1023000),
    )


_VismLapdT200_Type.__name__ = "Integer32"
_VismLapdT200_Object = MibTableColumn
vismLapdT200 = _VismLapdT200_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 5),
    _VismLapdT200_Type()
)
vismLapdT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismLapdT200.setStatus("mandatory")


class _VismLapdT203_Type(Integer32):
    """Custom type vismLapdT203 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1023000),
    )


_VismLapdT203_Type.__name__ = "Integer32"
_VismLapdT203_Object = MibTableColumn
vismLapdT203 = _VismLapdT203_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 6),
    _VismLapdT203_Type()
)
vismLapdT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismLapdT203.setStatus("mandatory")


class _VismLapdType_Type(Integer32):
    """Custom type vismLapdType based on Integer32"""
    defaultValue = 19

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("att4Ess", 4),
          ("att5EssPRA", 3),
          ("ausp", 12),
          ("bc303CSC", 16),
          ("bc303TMC", 15),
          ("bellcore", 18),
          ("ccitt", 1),
          ("etsi", 14),
          ("insNet", 8),
          ("ni1", 13),
          ("ni2", 19),
          ("ntDMS100PRA", 6),
          ("ntDMS250", 17),
          ("tr6MPC", 9),
          ("tr6PBX", 10),
          ("vn2or3", 7))
    )


_VismLapdType_Type.__name__ = "Integer32"
_VismLapdType_Object = MibTableColumn
vismLapdType = _VismLapdType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 7),
    _VismLapdType_Type()
)
vismLapdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismLapdType.setStatus("mandatory")


class _VismLapdRowStatus_Type(Integer32):
    """Custom type vismLapdRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_VismLapdRowStatus_Type.__name__ = "Integer32"
_VismLapdRowStatus_Object = MibTableColumn
vismLapdRowStatus = _VismLapdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 8),
    _VismLapdRowStatus_Type()
)
vismLapdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismLapdRowStatus.setStatus("mandatory")


class _VismLapdSide_Type(Integer32):
    """Custom type vismLapdSide based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("user", 2))
    )


_VismLapdSide_Type.__name__ = "Integer32"
_VismLapdSide_Object = MibTableColumn
vismLapdSide = _VismLapdSide_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 9),
    _VismLapdSide_Type()
)
vismLapdSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismLapdSide.setStatus("mandatory")


class _VismLapdTrunkType_Type(Integer32):
    """Custom type vismLapdTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backhaul", 1),
          ("lapdTrunking", 2))
    )


_VismLapdTrunkType_Type.__name__ = "Integer32"
_VismLapdTrunkType_Object = MibTableColumn
vismLapdTrunkType = _VismLapdTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 10),
    _VismLapdTrunkType_Type()
)
vismLapdTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTrunkType.setStatus("mandatory")
_VismLapdStatsTable_Object = MibTable
vismLapdStatsTable = _VismLapdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2)
)
if mibBuilder.loadTexts:
    vismLapdStatsTable.setStatus("mandatory")
_VismLapdStatsEntry_Object = MibTableRow
vismLapdStatsEntry = _VismLapdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1)
)
vismLapdStatsEntry.setIndexNames(
    (0, "VISM-LAPD-MIB", "vismLapdStatsIndex"),
)
if mibBuilder.loadTexts:
    vismLapdStatsEntry.setStatus("mandatory")


class _VismLapdStatsIndex_Type(Integer32):
    """Custom type vismLapdStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_VismLapdStatsIndex_Type.__name__ = "Integer32"
_VismLapdStatsIndex_Object = MibTableColumn
vismLapdStatsIndex = _VismLapdStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 1),
    _VismLapdStatsIndex_Type()
)
vismLapdStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdStatsIndex.setStatus("mandatory")
_VismLapdRxInfoFrames_Type = Counter32
_VismLapdRxInfoFrames_Object = MibTableColumn
vismLapdRxInfoFrames = _VismLapdRxInfoFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 2),
    _VismLapdRxInfoFrames_Type()
)
vismLapdRxInfoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxInfoFrames.setStatus("mandatory")
_VismLapdTxInfoFrames_Type = Counter32
_VismLapdTxInfoFrames_Object = MibTableColumn
vismLapdTxInfoFrames = _VismLapdTxInfoFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 3),
    _VismLapdTxInfoFrames_Type()
)
vismLapdTxInfoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxInfoFrames.setStatus("mandatory")
_VismLapdRxReadyFrames_Type = Counter32
_VismLapdRxReadyFrames_Object = MibTableColumn
vismLapdRxReadyFrames = _VismLapdRxReadyFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 4),
    _VismLapdRxReadyFrames_Type()
)
vismLapdRxReadyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxReadyFrames.setStatus("mandatory")
_VismLapdTxReadyFrames_Type = Counter32
_VismLapdTxReadyFrames_Object = MibTableColumn
vismLapdTxReadyFrames = _VismLapdTxReadyFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 5),
    _VismLapdTxReadyFrames_Type()
)
vismLapdTxReadyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxReadyFrames.setStatus("mandatory")
_VismLapdRxNotReadyFrames_Type = Counter32
_VismLapdRxNotReadyFrames_Object = MibTableColumn
vismLapdRxNotReadyFrames = _VismLapdRxNotReadyFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 6),
    _VismLapdRxNotReadyFrames_Type()
)
vismLapdRxNotReadyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxNotReadyFrames.setStatus("mandatory")
_VismLapdTxNotReadyFrames_Type = Counter32
_VismLapdTxNotReadyFrames_Object = MibTableColumn
vismLapdTxNotReadyFrames = _VismLapdTxNotReadyFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 7),
    _VismLapdTxNotReadyFrames_Type()
)
vismLapdTxNotReadyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxNotReadyFrames.setStatus("mandatory")
_VismLapdRxSABMFrames_Type = Counter32
_VismLapdRxSABMFrames_Object = MibTableColumn
vismLapdRxSABMFrames = _VismLapdRxSABMFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 8),
    _VismLapdRxSABMFrames_Type()
)
vismLapdRxSABMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxSABMFrames.setStatus("mandatory")
_VismLapdTxSABMFrames_Type = Counter32
_VismLapdTxSABMFrames_Object = MibTableColumn
vismLapdTxSABMFrames = _VismLapdTxSABMFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 9),
    _VismLapdTxSABMFrames_Type()
)
vismLapdTxSABMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxSABMFrames.setStatus("mandatory")
_VismLapdRxDisconFrames_Type = Counter32
_VismLapdRxDisconFrames_Object = MibTableColumn
vismLapdRxDisconFrames = _VismLapdRxDisconFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 10),
    _VismLapdRxDisconFrames_Type()
)
vismLapdRxDisconFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxDisconFrames.setStatus("mandatory")
_VismLapdTxDisconFrames_Type = Counter32
_VismLapdTxDisconFrames_Object = MibTableColumn
vismLapdTxDisconFrames = _VismLapdTxDisconFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 11),
    _VismLapdTxDisconFrames_Type()
)
vismLapdTxDisconFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxDisconFrames.setStatus("mandatory")
_VismLapdRxUAFrames_Type = Counter32
_VismLapdRxUAFrames_Object = MibTableColumn
vismLapdRxUAFrames = _VismLapdRxUAFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 12),
    _VismLapdRxUAFrames_Type()
)
vismLapdRxUAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxUAFrames.setStatus("mandatory")
_VismLapdTxUAFrames_Type = Counter32
_VismLapdTxUAFrames_Object = MibTableColumn
vismLapdTxUAFrames = _VismLapdTxUAFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 13),
    _VismLapdTxUAFrames_Type()
)
vismLapdTxUAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxUAFrames.setStatus("mandatory")
_VismLapdRxDiscModeFrames_Type = Counter32
_VismLapdRxDiscModeFrames_Object = MibTableColumn
vismLapdRxDiscModeFrames = _VismLapdRxDiscModeFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 14),
    _VismLapdRxDiscModeFrames_Type()
)
vismLapdRxDiscModeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxDiscModeFrames.setStatus("mandatory")
_VismLapdTxDiscModeFrames_Type = Counter32
_VismLapdTxDiscModeFrames_Object = MibTableColumn
vismLapdTxDiscModeFrames = _VismLapdTxDiscModeFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 15),
    _VismLapdTxDiscModeFrames_Type()
)
vismLapdTxDiscModeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxDiscModeFrames.setStatus("mandatory")
_VismLapdRxFrmRejectFrames_Type = Counter32
_VismLapdRxFrmRejectFrames_Object = MibTableColumn
vismLapdRxFrmRejectFrames = _VismLapdRxFrmRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 16),
    _VismLapdRxFrmRejectFrames_Type()
)
vismLapdRxFrmRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxFrmRejectFrames.setStatus("mandatory")
_VismLapdTxFrmRejectFrames_Type = Counter32
_VismLapdTxFrmRejectFrames_Object = MibTableColumn
vismLapdTxFrmRejectFrames = _VismLapdTxFrmRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 17),
    _VismLapdTxFrmRejectFrames_Type()
)
vismLapdTxFrmRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxFrmRejectFrames.setStatus("mandatory")
_VismLapdRxExchIdFrames_Type = Counter32
_VismLapdRxExchIdFrames_Object = MibTableColumn
vismLapdRxExchIdFrames = _VismLapdRxExchIdFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 18),
    _VismLapdRxExchIdFrames_Type()
)
vismLapdRxExchIdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxExchIdFrames.setStatus("mandatory")
_VismLapdTxExchIdFrames_Type = Counter32
_VismLapdTxExchIdFrames_Object = MibTableColumn
vismLapdTxExchIdFrames = _VismLapdTxExchIdFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 19),
    _VismLapdTxExchIdFrames_Type()
)
vismLapdTxExchIdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxExchIdFrames.setStatus("mandatory")
_VismLapdRxUnumInfoFrames_Type = Counter32
_VismLapdRxUnumInfoFrames_Object = MibTableColumn
vismLapdRxUnumInfoFrames = _VismLapdRxUnumInfoFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 20),
    _VismLapdRxUnumInfoFrames_Type()
)
vismLapdRxUnumInfoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxUnumInfoFrames.setStatus("mandatory")
_VismLapdTxUnumInfoFrames_Type = Counter32
_VismLapdTxUnumInfoFrames_Object = MibTableColumn
vismLapdTxUnumInfoFrames = _VismLapdTxUnumInfoFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 21),
    _VismLapdTxUnumInfoFrames_Type()
)
vismLapdTxUnumInfoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxUnumInfoFrames.setStatus("mandatory")
_VismLapdRxRejectFrames_Type = Counter32
_VismLapdRxRejectFrames_Object = MibTableColumn
vismLapdRxRejectFrames = _VismLapdRxRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 22),
    _VismLapdRxRejectFrames_Type()
)
vismLapdRxRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxRejectFrames.setStatus("mandatory")
_VismLapdTxRejectFrames_Type = Counter32
_VismLapdTxRejectFrames_Object = MibTableColumn
vismLapdTxRejectFrames = _VismLapdTxRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 23),
    _VismLapdTxRejectFrames_Type()
)
vismLapdTxRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxRejectFrames.setStatus("mandatory")
_VismLapdRxInvalidFrames_Type = Counter32
_VismLapdRxInvalidFrames_Object = MibTableColumn
vismLapdRxInvalidFrames = _VismLapdRxInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 24),
    _VismLapdRxInvalidFrames_Type()
)
vismLapdRxInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxInvalidFrames.setStatus("mandatory")
_VismLapdDlcTable_Object = MibTable
vismLapdDlcTable = _VismLapdDlcTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 3)
)
if mibBuilder.loadTexts:
    vismLapdDlcTable.setStatus("mandatory")
_VismLapdDlcEntry_Object = MibTableRow
vismLapdDlcEntry = _VismLapdDlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 3, 1)
)
vismLapdDlcEntry.setIndexNames(
    (0, "VISM-LAPD-MIB", "vismLapdDlcIndex"),
    (0, "VISM-LAPD-MIB", "vismLapdDlcSapi"),
    (0, "VISM-LAPD-MIB", "vismLapdDlcTei"),
)
if mibBuilder.loadTexts:
    vismLapdDlcEntry.setStatus("mandatory")


class _VismLapdDlcIndex_Type(Integer32):
    """Custom type vismLapdDlcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_VismLapdDlcIndex_Type.__name__ = "Integer32"
_VismLapdDlcIndex_Object = MibTableColumn
vismLapdDlcIndex = _VismLapdDlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 3, 1, 1),
    _VismLapdDlcIndex_Type()
)
vismLapdDlcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdDlcIndex.setStatus("mandatory")
_VismLapdDlcSapi_Type = Integer32
_VismLapdDlcSapi_Object = MibTableColumn
vismLapdDlcSapi = _VismLapdDlcSapi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 3, 1, 2),
    _VismLapdDlcSapi_Type()
)
vismLapdDlcSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdDlcSapi.setStatus("mandatory")
_VismLapdDlcTei_Type = Integer32
_VismLapdDlcTei_Object = MibTableColumn
vismLapdDlcTei = _VismLapdDlcTei_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 3, 1, 3),
    _VismLapdDlcTei_Type()
)
vismLapdDlcTei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdDlcTei.setStatus("mandatory")


class _VismLapdDlcLinkState_Type(Integer32):
    """Custom type vismLapdDlcLinkState based on Integer32"""
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


_VismLapdDlcLinkState_Type.__name__ = "Integer32"
_VismLapdDlcLinkState_Object = MibTableColumn
vismLapdDlcLinkState = _VismLapdDlcLinkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 3, 1, 4),
    _VismLapdDlcLinkState_Type()
)
vismLapdDlcLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdDlcLinkState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VISM-LAPD-MIB",
    **{"vismLapdGrp": vismLapdGrp,
       "vismLapdTable": vismLapdTable,
       "vismLapdEntry": vismLapdEntry,
       "vismLapdIndex": vismLapdIndex,
       "vismLapdAppType": vismLapdAppType,
       "vismLapdWinSize": vismLapdWinSize,
       "vismLapdN200": vismLapdN200,
       "vismLapdT200": vismLapdT200,
       "vismLapdT203": vismLapdT203,
       "vismLapdType": vismLapdType,
       "vismLapdRowStatus": vismLapdRowStatus,
       "vismLapdSide": vismLapdSide,
       "vismLapdTrunkType": vismLapdTrunkType,
       "vismLapdStatsTable": vismLapdStatsTable,
       "vismLapdStatsEntry": vismLapdStatsEntry,
       "vismLapdStatsIndex": vismLapdStatsIndex,
       "vismLapdRxInfoFrames": vismLapdRxInfoFrames,
       "vismLapdTxInfoFrames": vismLapdTxInfoFrames,
       "vismLapdRxReadyFrames": vismLapdRxReadyFrames,
       "vismLapdTxReadyFrames": vismLapdTxReadyFrames,
       "vismLapdRxNotReadyFrames": vismLapdRxNotReadyFrames,
       "vismLapdTxNotReadyFrames": vismLapdTxNotReadyFrames,
       "vismLapdRxSABMFrames": vismLapdRxSABMFrames,
       "vismLapdTxSABMFrames": vismLapdTxSABMFrames,
       "vismLapdRxDisconFrames": vismLapdRxDisconFrames,
       "vismLapdTxDisconFrames": vismLapdTxDisconFrames,
       "vismLapdRxUAFrames": vismLapdRxUAFrames,
       "vismLapdTxUAFrames": vismLapdTxUAFrames,
       "vismLapdRxDiscModeFrames": vismLapdRxDiscModeFrames,
       "vismLapdTxDiscModeFrames": vismLapdTxDiscModeFrames,
       "vismLapdRxFrmRejectFrames": vismLapdRxFrmRejectFrames,
       "vismLapdTxFrmRejectFrames": vismLapdTxFrmRejectFrames,
       "vismLapdRxExchIdFrames": vismLapdRxExchIdFrames,
       "vismLapdTxExchIdFrames": vismLapdTxExchIdFrames,
       "vismLapdRxUnumInfoFrames": vismLapdRxUnumInfoFrames,
       "vismLapdTxUnumInfoFrames": vismLapdTxUnumInfoFrames,
       "vismLapdRxRejectFrames": vismLapdRxRejectFrames,
       "vismLapdTxRejectFrames": vismLapdTxRejectFrames,
       "vismLapdRxInvalidFrames": vismLapdRxInvalidFrames,
       "vismLapdDlcTable": vismLapdDlcTable,
       "vismLapdDlcEntry": vismLapdDlcEntry,
       "vismLapdDlcIndex": vismLapdDlcIndex,
       "vismLapdDlcSapi": vismLapdDlcSapi,
       "vismLapdDlcTei": vismLapdDlcTei,
       "vismLapdDlcLinkState": vismLapdDlcLinkState}
)

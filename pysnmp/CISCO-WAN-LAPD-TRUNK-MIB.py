# SNMP MIB module (CISCO-WAN-LAPD-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-LAPD-TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:59 2024
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWanLapdTrunkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 23)
)
ciscoWanLapdTrunkMIB.setRevisions(
        ("2003-12-11 00:00",
         "2003-07-17 00:00",
         "2003-07-11 00:00")
)


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
    vismLapdTable.setStatus("current")
_VismLapdEntry_Object = MibTableRow
vismLapdEntry = _VismLapdEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1)
)
vismLapdEntry.setIndexNames(
    (0, "CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdIndex"),
)
if mibBuilder.loadTexts:
    vismLapdEntry.setStatus("current")


class _VismLapdIndex_Type(Integer32):
    """Custom type vismLapdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_VismLapdIndex_Type.__name__ = "Integer32"
_VismLapdIndex_Object = MibTableColumn
vismLapdIndex = _VismLapdIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 1),
    _VismLapdIndex_Type()
)
vismLapdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdIndex.setStatus("current")


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
vismLapdAppType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismLapdAppType.setStatus("current")


class _VismLapdWinSize_Type(Integer32):
    """Custom type vismLapdWinSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_VismLapdWinSize_Type.__name__ = "Integer32"
_VismLapdWinSize_Object = MibTableColumn
vismLapdWinSize = _VismLapdWinSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 3),
    _VismLapdWinSize_Type()
)
vismLapdWinSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismLapdWinSize.setStatus("current")


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
vismLapdN200.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismLapdN200.setStatus("current")


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
vismLapdT200.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismLapdT200.setStatus("current")
if mibBuilder.loadTexts:
    vismLapdT200.setUnits("milliseconds")


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
vismLapdT203.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismLapdT203.setStatus("current")
if mibBuilder.loadTexts:
    vismLapdT203.setUnits("milliseconds")


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
vismLapdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismLapdType.setStatus("current")
_VismLapdRowStatus_Type = RowStatus
_VismLapdRowStatus_Object = MibTableColumn
vismLapdRowStatus = _VismLapdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 1, 1, 8),
    _VismLapdRowStatus_Type()
)
vismLapdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismLapdRowStatus.setStatus("current")


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
vismLapdSide.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismLapdSide.setStatus("current")


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
    vismLapdTrunkType.setStatus("current")
_VismLapdStatsTable_Object = MibTable
vismLapdStatsTable = _VismLapdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2)
)
if mibBuilder.loadTexts:
    vismLapdStatsTable.setStatus("current")
_VismLapdStatsEntry_Object = MibTableRow
vismLapdStatsEntry = _VismLapdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1)
)
vismLapdStatsEntry.setIndexNames(
    (0, "CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdStatsIndex"),
)
if mibBuilder.loadTexts:
    vismLapdStatsEntry.setStatus("current")


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
    vismLapdStatsIndex.setStatus("current")
_VismLapdRxInfoFrames_Type = Counter32
_VismLapdRxInfoFrames_Object = MibTableColumn
vismLapdRxInfoFrames = _VismLapdRxInfoFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 2),
    _VismLapdRxInfoFrames_Type()
)
vismLapdRxInfoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxInfoFrames.setStatus("current")
_VismLapdTxInfoFrames_Type = Counter32
_VismLapdTxInfoFrames_Object = MibTableColumn
vismLapdTxInfoFrames = _VismLapdTxInfoFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 3),
    _VismLapdTxInfoFrames_Type()
)
vismLapdTxInfoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxInfoFrames.setStatus("current")
_VismLapdRxReadyFrames_Type = Counter32
_VismLapdRxReadyFrames_Object = MibTableColumn
vismLapdRxReadyFrames = _VismLapdRxReadyFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 4),
    _VismLapdRxReadyFrames_Type()
)
vismLapdRxReadyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxReadyFrames.setStatus("current")
_VismLapdTxReadyFrames_Type = Counter32
_VismLapdTxReadyFrames_Object = MibTableColumn
vismLapdTxReadyFrames = _VismLapdTxReadyFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 5),
    _VismLapdTxReadyFrames_Type()
)
vismLapdTxReadyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxReadyFrames.setStatus("current")
_VismLapdRxNotReadyFrames_Type = Counter32
_VismLapdRxNotReadyFrames_Object = MibTableColumn
vismLapdRxNotReadyFrames = _VismLapdRxNotReadyFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 6),
    _VismLapdRxNotReadyFrames_Type()
)
vismLapdRxNotReadyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxNotReadyFrames.setStatus("current")
_VismLapdTxNotReadyFrames_Type = Counter32
_VismLapdTxNotReadyFrames_Object = MibTableColumn
vismLapdTxNotReadyFrames = _VismLapdTxNotReadyFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 7),
    _VismLapdTxNotReadyFrames_Type()
)
vismLapdTxNotReadyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxNotReadyFrames.setStatus("current")
_VismLapdRxSABMFrames_Type = Counter32
_VismLapdRxSABMFrames_Object = MibTableColumn
vismLapdRxSABMFrames = _VismLapdRxSABMFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 8),
    _VismLapdRxSABMFrames_Type()
)
vismLapdRxSABMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxSABMFrames.setStatus("current")
_VismLapdTxSABMFrames_Type = Counter32
_VismLapdTxSABMFrames_Object = MibTableColumn
vismLapdTxSABMFrames = _VismLapdTxSABMFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 9),
    _VismLapdTxSABMFrames_Type()
)
vismLapdTxSABMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxSABMFrames.setStatus("current")
_VismLapdRxDisconFrames_Type = Counter32
_VismLapdRxDisconFrames_Object = MibTableColumn
vismLapdRxDisconFrames = _VismLapdRxDisconFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 10),
    _VismLapdRxDisconFrames_Type()
)
vismLapdRxDisconFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxDisconFrames.setStatus("current")
_VismLapdTxDisconFrames_Type = Counter32
_VismLapdTxDisconFrames_Object = MibTableColumn
vismLapdTxDisconFrames = _VismLapdTxDisconFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 11),
    _VismLapdTxDisconFrames_Type()
)
vismLapdTxDisconFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxDisconFrames.setStatus("current")
_VismLapdRxUAFrames_Type = Counter32
_VismLapdRxUAFrames_Object = MibTableColumn
vismLapdRxUAFrames = _VismLapdRxUAFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 12),
    _VismLapdRxUAFrames_Type()
)
vismLapdRxUAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxUAFrames.setStatus("current")
_VismLapdTxUAFrames_Type = Counter32
_VismLapdTxUAFrames_Object = MibTableColumn
vismLapdTxUAFrames = _VismLapdTxUAFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 13),
    _VismLapdTxUAFrames_Type()
)
vismLapdTxUAFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxUAFrames.setStatus("current")
_VismLapdRxDiscModeFrames_Type = Counter32
_VismLapdRxDiscModeFrames_Object = MibTableColumn
vismLapdRxDiscModeFrames = _VismLapdRxDiscModeFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 14),
    _VismLapdRxDiscModeFrames_Type()
)
vismLapdRxDiscModeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxDiscModeFrames.setStatus("current")
_VismLapdTxDiscModeFrames_Type = Counter32
_VismLapdTxDiscModeFrames_Object = MibTableColumn
vismLapdTxDiscModeFrames = _VismLapdTxDiscModeFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 15),
    _VismLapdTxDiscModeFrames_Type()
)
vismLapdTxDiscModeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxDiscModeFrames.setStatus("current")
_VismLapdRxFrmRejectFrames_Type = Counter32
_VismLapdRxFrmRejectFrames_Object = MibTableColumn
vismLapdRxFrmRejectFrames = _VismLapdRxFrmRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 16),
    _VismLapdRxFrmRejectFrames_Type()
)
vismLapdRxFrmRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxFrmRejectFrames.setStatus("current")
_VismLapdTxFrmRejectFrames_Type = Counter32
_VismLapdTxFrmRejectFrames_Object = MibTableColumn
vismLapdTxFrmRejectFrames = _VismLapdTxFrmRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 17),
    _VismLapdTxFrmRejectFrames_Type()
)
vismLapdTxFrmRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxFrmRejectFrames.setStatus("current")
_VismLapdRxExchIdFrames_Type = Counter32
_VismLapdRxExchIdFrames_Object = MibTableColumn
vismLapdRxExchIdFrames = _VismLapdRxExchIdFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 18),
    _VismLapdRxExchIdFrames_Type()
)
vismLapdRxExchIdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxExchIdFrames.setStatus("current")
_VismLapdTxExchIdFrames_Type = Counter32
_VismLapdTxExchIdFrames_Object = MibTableColumn
vismLapdTxExchIdFrames = _VismLapdTxExchIdFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 19),
    _VismLapdTxExchIdFrames_Type()
)
vismLapdTxExchIdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxExchIdFrames.setStatus("current")
_VismLapdRxUnumInfoFrames_Type = Counter32
_VismLapdRxUnumInfoFrames_Object = MibTableColumn
vismLapdRxUnumInfoFrames = _VismLapdRxUnumInfoFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 20),
    _VismLapdRxUnumInfoFrames_Type()
)
vismLapdRxUnumInfoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxUnumInfoFrames.setStatus("current")
_VismLapdTxUnumInfoFrames_Type = Counter32
_VismLapdTxUnumInfoFrames_Object = MibTableColumn
vismLapdTxUnumInfoFrames = _VismLapdTxUnumInfoFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 21),
    _VismLapdTxUnumInfoFrames_Type()
)
vismLapdTxUnumInfoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxUnumInfoFrames.setStatus("current")
_VismLapdRxRejectFrames_Type = Counter32
_VismLapdRxRejectFrames_Object = MibTableColumn
vismLapdRxRejectFrames = _VismLapdRxRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 22),
    _VismLapdRxRejectFrames_Type()
)
vismLapdRxRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxRejectFrames.setStatus("current")
_VismLapdTxRejectFrames_Type = Counter32
_VismLapdTxRejectFrames_Object = MibTableColumn
vismLapdTxRejectFrames = _VismLapdTxRejectFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 23),
    _VismLapdTxRejectFrames_Type()
)
vismLapdTxRejectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTxRejectFrames.setStatus("current")
_VismLapdRxInvalidFrames_Type = Counter32
_VismLapdRxInvalidFrames_Object = MibTableColumn
vismLapdRxInvalidFrames = _VismLapdRxInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 2, 1, 24),
    _VismLapdRxInvalidFrames_Type()
)
vismLapdRxInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdRxInvalidFrames.setStatus("current")
_VismLapdDlcTable_Object = MibTable
vismLapdDlcTable = _VismLapdDlcTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 3)
)
if mibBuilder.loadTexts:
    vismLapdDlcTable.setStatus("current")
_VismLapdDlcEntry_Object = MibTableRow
vismLapdDlcEntry = _VismLapdDlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 3, 1)
)
vismLapdDlcEntry.setIndexNames(
    (0, "CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdDlcIndex"),
    (0, "CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdDlcSapi"),
    (0, "CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdDlcTei"),
)
if mibBuilder.loadTexts:
    vismLapdDlcEntry.setStatus("current")


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
    vismLapdDlcIndex.setStatus("current")


class _VismLapdDlcSapi_Type(Integer32):
    """Custom type vismLapdDlcSapi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismLapdDlcSapi_Type.__name__ = "Integer32"
_VismLapdDlcSapi_Object = MibTableColumn
vismLapdDlcSapi = _VismLapdDlcSapi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 3, 1, 2),
    _VismLapdDlcSapi_Type()
)
vismLapdDlcSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdDlcSapi.setStatus("current")


class _VismLapdDlcTei_Type(Integer32):
    """Custom type vismLapdDlcTei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismLapdDlcTei_Type.__name__ = "Integer32"
_VismLapdDlcTei_Object = MibTableColumn
vismLapdDlcTei = _VismLapdDlcTei_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 12, 3, 1, 3),
    _VismLapdDlcTei_Type()
)
vismLapdDlcTei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdDlcTei.setStatus("current")


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
    vismLapdDlcLinkState.setStatus("current")
_CiscoWanLapdTrunkMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanLapdTrunkMIBObjects = _CiscoWanLapdTrunkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 1)
)
_VismLapdTrunkGrp_ObjectIdentity = ObjectIdentity
vismLapdTrunkGrp = _VismLapdTrunkGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 1, 1)
)
_VismLapdTrunkGrpTable_Object = MibTable
vismLapdTrunkGrpTable = _VismLapdTrunkGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vismLapdTrunkGrpTable.setStatus("current")
_VismLapdTrunkGrpEntry_Object = MibTableRow
vismLapdTrunkGrpEntry = _VismLapdTrunkGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 1, 1, 1, 1)
)
vismLapdTrunkGrpEntry.setIndexNames(
    (0, "CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTrunkNum"),
)
if mibBuilder.loadTexts:
    vismLapdTrunkGrpEntry.setStatus("current")


class _VismLapdTrunkNum_Type(Integer32):
    """Custom type vismLapdTrunkNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismLapdTrunkNum_Type.__name__ = "Integer32"
_VismLapdTrunkNum_Object = MibTableColumn
vismLapdTrunkNum = _VismLapdTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 1, 1, 1, 1, 1),
    _VismLapdTrunkNum_Type()
)
vismLapdTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vismLapdTrunkNum.setStatus("current")


class _VismLapdTrunkState_Type(Integer32):
    """Custom type vismLapdTrunkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("is", 2),
          ("oos", 1),
          ("unknown", 3))
    )


_VismLapdTrunkState_Type.__name__ = "Integer32"
_VismLapdTrunkState_Object = MibTableColumn
vismLapdTrunkState = _VismLapdTrunkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 1, 1, 1, 1, 2),
    _VismLapdTrunkState_Type()
)
vismLapdTrunkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLapdTrunkState.setStatus("current")


class _VismLapdTrunkRudpIndex_Type(Integer32):
    """Custom type vismLapdTrunkRudpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismLapdTrunkRudpIndex_Type.__name__ = "Integer32"
_VismLapdTrunkRudpIndex_Object = MibTableColumn
vismLapdTrunkRudpIndex = _VismLapdTrunkRudpIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 1, 1, 1, 1, 3),
    _VismLapdTrunkRudpIndex_Type()
)
vismLapdTrunkRudpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismLapdTrunkRudpIndex.setStatus("current")
_VismLapdTrunkRowStatus_Type = RowStatus
_VismLapdTrunkRowStatus_Object = MibTableColumn
vismLapdTrunkRowStatus = _VismLapdTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 1, 1, 1, 1, 4),
    _VismLapdTrunkRowStatus_Type()
)
vismLapdTrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismLapdTrunkRowStatus.setStatus("current")
_VismLapdTrunkNotificationPrefix_ObjectIdentity = ObjectIdentity
vismLapdTrunkNotificationPrefix = _VismLapdTrunkNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 2)
)
_VismLapdTrunkNotifications_ObjectIdentity = ObjectIdentity
vismLapdTrunkNotifications = _VismLapdTrunkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 2, 0)
)
_VismLapdTrunkMIBConformance_ObjectIdentity = ObjectIdentity
vismLapdTrunkMIBConformance = _VismLapdTrunkMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 3)
)
_VismLapdTrunkMIBCompliances_ObjectIdentity = ObjectIdentity
vismLapdTrunkMIBCompliances = _VismLapdTrunkMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 3, 1)
)
_VismLapdTrunkMIBGroups_ObjectIdentity = ObjectIdentity
vismLapdTrunkMIBGroups = _VismLapdTrunkMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 3, 2)
)

# Managed Objects groups

vismLapdTrunkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 3, 2, 1)
)
vismLapdTrunkGroup.setObjects(
      *(("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTrunkState"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTrunkRudpIndex"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTrunkRowStatus"))
)
if mibBuilder.loadTexts:
    vismLapdTrunkGroup.setStatus("current")

ciscoVismLapdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 3, 2, 2)
)
ciscoVismLapdGroup.setObjects(
      *(("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdIndex"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdAppType"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdWinSize"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdN200"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdT200"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdT203"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdType"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRowStatus"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdSide"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTrunkType"))
)
if mibBuilder.loadTexts:
    ciscoVismLapdGroup.setStatus("current")

ciscoVismLapdStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 3, 2, 3)
)
ciscoVismLapdStatsGroup.setObjects(
      *(("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdStatsIndex"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxInfoFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTxInfoFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxReadyFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTxReadyFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxNotReadyFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTxNotReadyFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxSABMFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTxSABMFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxDisconFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTxDisconFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxUAFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTxUAFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxDiscModeFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTxDiscModeFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxFrmRejectFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTxFrmRejectFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxExchIdFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTxExchIdFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxUnumInfoFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTxUnumInfoFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxRejectFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdTxRejectFrames"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdRxInvalidFrames"))
)
if mibBuilder.loadTexts:
    ciscoVismLapdStatsGroup.setStatus("current")

ciscoVismLapdDlcTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 3, 2, 4)
)
ciscoVismLapdDlcTable.setObjects(
      *(("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdDlcIndex"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdDlcSapi"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdDlcTei"),
        ("CISCO-WAN-LAPD-TRUNK-MIB", "vismLapdDlcLinkState"))
)
if mibBuilder.loadTexts:
    ciscoVismLapdDlcTable.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vismLapdTrunkMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 23, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vismLapdTrunkMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-LAPD-TRUNK-MIB",
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
       "vismLapdDlcLinkState": vismLapdDlcLinkState,
       "ciscoWanLapdTrunkMIB": ciscoWanLapdTrunkMIB,
       "ciscoWanLapdTrunkMIBObjects": ciscoWanLapdTrunkMIBObjects,
       "vismLapdTrunkGrp": vismLapdTrunkGrp,
       "vismLapdTrunkGrpTable": vismLapdTrunkGrpTable,
       "vismLapdTrunkGrpEntry": vismLapdTrunkGrpEntry,
       "vismLapdTrunkNum": vismLapdTrunkNum,
       "vismLapdTrunkState": vismLapdTrunkState,
       "vismLapdTrunkRudpIndex": vismLapdTrunkRudpIndex,
       "vismLapdTrunkRowStatus": vismLapdTrunkRowStatus,
       "vismLapdTrunkNotificationPrefix": vismLapdTrunkNotificationPrefix,
       "vismLapdTrunkNotifications": vismLapdTrunkNotifications,
       "vismLapdTrunkMIBConformance": vismLapdTrunkMIBConformance,
       "vismLapdTrunkMIBCompliances": vismLapdTrunkMIBCompliances,
       "vismLapdTrunkMIBCompliance": vismLapdTrunkMIBCompliance,
       "vismLapdTrunkMIBGroups": vismLapdTrunkMIBGroups,
       "vismLapdTrunkGroup": vismLapdTrunkGroup,
       "ciscoVismLapdGroup": ciscoVismLapdGroup,
       "ciscoVismLapdStatsGroup": ciscoVismLapdStatsGroup,
       "ciscoVismLapdDlcTable": ciscoVismLapdDlcTable}
)

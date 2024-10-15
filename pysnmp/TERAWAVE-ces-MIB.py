# SNMP MIB module (TERAWAVE-ces-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-ces-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:11 2024
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
 enterprises,
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
    "enterprises",
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

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagment_ObjectIdentity = ObjectIdentity
atmForumNetworkManagment = _AtmForumNetworkManagment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfCESmib_ObjectIdentity = ObjectIdentity
atmfCESmib = _AtmfCESmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 2)
)
_AtmfCES_ObjectIdentity = ObjectIdentity
atmfCES = _AtmfCES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2)
)
_AtmfCESObjects_ObjectIdentity = ObjectIdentity
atmfCESObjects = _AtmfCESObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1)
)
_AtmfCESConTable_Object = MibTable
atmfCESConTable = _AtmfCESConTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmfCESConTable.setStatus("mandatory")
_AtmfCESConTableEntry_Object = MibTableRow
atmfCESConTableEntry = _AtmfCESConTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1)
)
atmfCESConTableEntry.setIndexNames(
    (0, "TERAWAVE-ces-MIB", "atmfCESCbrIndex"),
)
if mibBuilder.loadTexts:
    atmfCESConTableEntry.setStatus("mandatory")
_AtmfCESCbrIndex_Type = Integer32
_AtmfCESCbrIndex_Object = MibTableColumn
atmfCESCbrIndex = _AtmfCESCbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 1),
    _AtmfCESCbrIndex_Type()
)
atmfCESCbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESCbrIndex.setStatus("mandatory")
_AtmfCESAtmIndex_Type = Integer32
_AtmfCESAtmIndex_Object = MibTableColumn
atmfCESAtmIndex = _AtmfCESAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 2),
    _AtmfCESAtmIndex_Type()
)
atmfCESAtmIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESAtmIndex.setStatus("mandatory")


class _AtmfCESAtmVpi_Type(Integer32):
    """Custom type atmfCESAtmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmfCESAtmVpi_Type.__name__ = "Integer32"
_AtmfCESAtmVpi_Object = MibTableColumn
atmfCESAtmVpi = _AtmfCESAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 3),
    _AtmfCESAtmVpi_Type()
)
atmfCESAtmVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESAtmVpi.setStatus("mandatory")


class _AtmfCESAtmVci_Type(Integer32):
    """Custom type atmfCESAtmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmfCESAtmVci_Type.__name__ = "Integer32"
_AtmfCESAtmVci_Object = MibTableColumn
atmfCESAtmVci = _AtmfCESAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 4),
    _AtmfCESAtmVci_Type()
)
atmfCESAtmVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESAtmVci.setStatus("mandatory")


class _AtmfCESCbrService_Type(Integer32):
    """Custom type atmfCESCbrService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("structured", 2),
          ("unstructured", 1))
    )


_AtmfCESCbrService_Type.__name__ = "Integer32"
_AtmfCESCbrService_Object = MibTableColumn
atmfCESCbrService = _AtmfCESCbrService_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 5),
    _AtmfCESCbrService_Type()
)
atmfCESCbrService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESCbrService.setStatus("mandatory")


class _AtmfCESCbrClockMode_Type(Integer32):
    """Custom type atmfCESCbrClockMode based on Integer32"""
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
        *(("adaptive", 3),
          ("looped", 4),
          ("srts", 2),
          ("synchronous", 1))
    )


_AtmfCESCbrClockMode_Type.__name__ = "Integer32"
_AtmfCESCbrClockMode_Object = MibTableColumn
atmfCESCbrClockMode = _AtmfCESCbrClockMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 6),
    _AtmfCESCbrClockMode_Type()
)
atmfCESCbrClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESCbrClockMode.setStatus("mandatory")


class _AtmfCESCas_Type(Integer32):
    """Custom type atmfCESCas based on Integer32"""
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
        *(("basic", 1),
          ("ds1EsfCas", 4),
          ("ds1SfCas", 3),
          ("e1Cas", 2),
          ("j2Cas", 5))
    )


_AtmfCESCas_Type.__name__ = "Integer32"
_AtmfCESCas_Object = MibTableColumn
atmfCESCas = _AtmfCESCas_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 7),
    _AtmfCESCas_Type()
)
atmfCESCas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESCas.setStatus("mandatory")


class _AtmfCESPartialFill_Type(Integer32):
    """Custom type atmfCESPartialFill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_AtmfCESPartialFill_Type.__name__ = "Integer32"
_AtmfCESPartialFill_Object = MibTableColumn
atmfCESPartialFill = _AtmfCESPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 8),
    _AtmfCESPartialFill_Type()
)
atmfCESPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESPartialFill.setStatus("mandatory")


class _AtmfCESBufMaxSize_Type(Integer32):
    """Custom type atmfCESBufMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 510),
    )


_AtmfCESBufMaxSize_Type.__name__ = "Integer32"
_AtmfCESBufMaxSize_Object = MibTableColumn
atmfCESBufMaxSize = _AtmfCESBufMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 9),
    _AtmfCESBufMaxSize_Type()
)
atmfCESBufMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESBufMaxSize.setStatus("mandatory")


class _AtmfCESCdvtRxT_Type(Integer32):
    """Custom type atmfCESCdvtRxT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmfCESCdvtRxT_Type.__name__ = "Integer32"
_AtmfCESCdvtRxT_Object = MibTableColumn
atmfCESCdvtRxT = _AtmfCESCdvtRxT_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 10),
    _AtmfCESCdvtRxT_Type()
)
atmfCESCdvtRxT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESCdvtRxT.setStatus("mandatory")


class _AtmfCESCellLossIntegrationPeriod_Type(Integer32):
    """Custom type atmfCESCellLossIntegrationPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_AtmfCESCellLossIntegrationPeriod_Type.__name__ = "Integer32"
_AtmfCESCellLossIntegrationPeriod_Object = MibTableColumn
atmfCESCellLossIntegrationPeriod = _AtmfCESCellLossIntegrationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 11),
    _AtmfCESCellLossIntegrationPeriod_Type()
)
atmfCESCellLossIntegrationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESCellLossIntegrationPeriod.setStatus("mandatory")


class _AtmfCESConnType_Type(Integer32):
    """Custom type atmfCESConnType based on Integer32"""
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
        *(("activeSvc", 3),
          ("other", 1),
          ("passiveSvc", 4),
          ("pvc", 2))
    )


_AtmfCESConnType_Type.__name__ = "Integer32"
_AtmfCESConnType_Object = MibTableColumn
atmfCESConnType = _AtmfCESConnType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 12),
    _AtmfCESConnType_Type()
)
atmfCESConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESConnType.setStatus("mandatory")
_AtmfCESLocalAddr_Type = OctetString
_AtmfCESLocalAddr_Object = MibTableColumn
atmfCESLocalAddr = _AtmfCESLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 13),
    _AtmfCESLocalAddr_Type()
)
atmfCESLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESLocalAddr.setStatus("mandatory")


class _AtmfCESAdminStatus_Type(Integer32):
    """Custom type atmfCESAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AtmfCESAdminStatus_Type.__name__ = "Integer32"
_AtmfCESAdminStatus_Object = MibTableColumn
atmfCESAdminStatus = _AtmfCESAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 14),
    _AtmfCESAdminStatus_Type()
)
atmfCESAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESAdminStatus.setStatus("mandatory")


class _AtmfCESOperStatus_Type(Integer32):
    """Custom type atmfCESOperStatus based on Integer32"""
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


_AtmfCESOperStatus_Type.__name__ = "Integer32"
_AtmfCESOperStatus_Object = MibTableColumn
atmfCESOperStatus = _AtmfCESOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 15),
    _AtmfCESOperStatus_Type()
)
atmfCESOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESOperStatus.setStatus("mandatory")


class _AtmCESConfRowStatus_Type(Integer32):
    """Custom type atmCESConfRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_AtmCESConfRowStatus_Type.__name__ = "Integer32"
_AtmCESConfRowStatus_Object = MibTableColumn
atmCESConfRowStatus = _AtmCESConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 16),
    _AtmCESConfRowStatus_Type()
)
atmCESConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCESConfRowStatus.setStatus("mandatory")
_AtmfCESMappingTable_Object = MibTable
atmfCESMappingTable = _AtmfCESMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    atmfCESMappingTable.setStatus("mandatory")
_AtmfCESMappingTableEntry_Object = MibTableRow
atmfCESMappingTableEntry = _AtmfCESMappingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 2, 1)
)
atmfCESMappingTableEntry.setIndexNames(
    (0, "TERAWAVE-ces-MIB", "atmfCESAtmIndex"),
    (0, "TERAWAVE-ces-MIB", "atmfCESAtmVpi"),
    (0, "TERAWAVE-ces-MIB", "atmfCESAtmVci"),
)
if mibBuilder.loadTexts:
    atmfCESMappingTableEntry.setStatus("mandatory")
_AtmfCESMappingCbrIndex_Type = Integer32
_AtmfCESMappingCbrIndex_Object = MibTableColumn
atmfCESMappingCbrIndex = _AtmfCESMappingCbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 2, 1, 1),
    _AtmfCESMappingCbrIndex_Type()
)
atmfCESMappingCbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESMappingCbrIndex.setStatus("mandatory")
_AtmfCESStatsTable_Object = MibTable
atmfCESStatsTable = _AtmfCESStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    atmfCESStatsTable.setStatus("mandatory")
_AtmfCESStatsTableEntry_Object = MibTableRow
atmfCESStatsTableEntry = _AtmfCESStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1)
)
atmfCESStatsTableEntry.setIndexNames(
    (0, "TERAWAVE-ces-MIB", "atmfCESCbrIndex"),
)
if mibBuilder.loadTexts:
    atmfCESStatsTableEntry.setStatus("mandatory")
_AtmfCESReassCells_Type = Counter32
_AtmfCESReassCells_Object = MibTableColumn
atmfCESReassCells = _AtmfCESReassCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 1),
    _AtmfCESReassCells_Type()
)
atmfCESReassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESReassCells.setStatus("mandatory")
_AtmfCESHdrErrors_Type = Counter32
_AtmfCESHdrErrors_Object = MibTableColumn
atmfCESHdrErrors = _AtmfCESHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 2),
    _AtmfCESHdrErrors_Type()
)
atmfCESHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESHdrErrors.setStatus("mandatory")
_AtmfCESPointerReframes_Type = Counter32
_AtmfCESPointerReframes_Object = MibTableColumn
atmfCESPointerReframes = _AtmfCESPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 3),
    _AtmfCESPointerReframes_Type()
)
atmfCESPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESPointerReframes.setStatus("mandatory")
_AtmfCESPointerParityErrors_Type = Counter32
_AtmfCESPointerParityErrors_Object = MibTableColumn
atmfCESPointerParityErrors = _AtmfCESPointerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 4),
    _AtmfCESPointerParityErrors_Type()
)
atmfCESPointerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESPointerParityErrors.setStatus("mandatory")
_AtmfCESAal1SeqErrors_Type = Counter32
_AtmfCESAal1SeqErrors_Object = MibTableColumn
atmfCESAal1SeqErrors = _AtmfCESAal1SeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 5),
    _AtmfCESAal1SeqErrors_Type()
)
atmfCESAal1SeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESAal1SeqErrors.setStatus("mandatory")
_AtmfCESLostCells_Type = Counter32
_AtmfCESLostCells_Object = MibTableColumn
atmfCESLostCells = _AtmfCESLostCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 6),
    _AtmfCESLostCells_Type()
)
atmfCESLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESLostCells.setStatus("mandatory")
_AtmfCESMisinsertedCells_Type = Counter32
_AtmfCESMisinsertedCells_Object = MibTableColumn
atmfCESMisinsertedCells = _AtmfCESMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 7),
    _AtmfCESMisinsertedCells_Type()
)
atmfCESMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESMisinsertedCells.setStatus("mandatory")
_AtmfCESBufUnderflows_Type = Counter32
_AtmfCESBufUnderflows_Object = MibTableColumn
atmfCESBufUnderflows = _AtmfCESBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 8),
    _AtmfCESBufUnderflows_Type()
)
atmfCESBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESBufUnderflows.setStatus("mandatory")
_AtmfCESBufOverflows_Type = Counter32
_AtmfCESBufOverflows_Object = MibTableColumn
atmfCESBufOverflows = _AtmfCESBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 9),
    _AtmfCESBufOverflows_Type()
)
atmfCESBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESBufOverflows.setStatus("mandatory")


class _AtmfCESCellLossStatus_Type(Integer32):
    """Custom type atmfCESCellLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loss", 2),
          ("noloss", 1))
    )


_AtmfCESCellLossStatus_Type.__name__ = "Integer32"
_AtmfCESCellLossStatus_Object = MibTableColumn
atmfCESCellLossStatus = _AtmfCESCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 10),
    _AtmfCESCellLossStatus_Type()
)
atmfCESCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESCellLossStatus.setStatus("mandatory")
_AtmfCESActiveSvcTable_Object = MibTable
atmfCESActiveSvcTable = _AtmfCESActiveSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    atmfCESActiveSvcTable.setStatus("mandatory")
_AtmfCESActiveSvcTableEntry_Object = MibTableRow
atmfCESActiveSvcTableEntry = _AtmfCESActiveSvcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1)
)
atmfCESActiveSvcTableEntry.setIndexNames(
    (0, "TERAWAVE-ces-MIB", "atmfCESCbrIndex"),
)
if mibBuilder.loadTexts:
    atmfCESActiveSvcTableEntry.setStatus("mandatory")
_AtmfCESRemoteAddr_Type = OctetString
_AtmfCESRemoteAddr_Object = MibTableColumn
atmfCESRemoteAddr = _AtmfCESRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 1),
    _AtmfCESRemoteAddr_Type()
)
atmfCESRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESRemoteAddr.setStatus("mandatory")


class _AtmfCESFirstRetryInterval_Type(Integer32):
    """Custom type atmfCESFirstRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AtmfCESFirstRetryInterval_Type.__name__ = "Integer32"
_AtmfCESFirstRetryInterval_Object = MibTableColumn
atmfCESFirstRetryInterval = _AtmfCESFirstRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 2),
    _AtmfCESFirstRetryInterval_Type()
)
atmfCESFirstRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESFirstRetryInterval.setStatus("mandatory")


class _AtmfCESRetryTimer_Type(Integer32):
    """Custom type atmfCESRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AtmfCESRetryTimer_Type.__name__ = "Integer32"
_AtmfCESRetryTimer_Object = MibTableColumn
atmfCESRetryTimer = _AtmfCESRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 3),
    _AtmfCESRetryTimer_Type()
)
atmfCESRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESRetryTimer.setStatus("mandatory")


class _AtmfCESRetryLimit_Type(Integer32):
    """Custom type atmfCESRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmfCESRetryLimit_Type.__name__ = "Integer32"
_AtmfCESRetryLimit_Object = MibTableColumn
atmfCESRetryLimit = _AtmfCESRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 4),
    _AtmfCESRetryLimit_Type()
)
atmfCESRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESRetryLimit.setStatus("mandatory")
_AtmfCESRetryFailures_Type = Gauge32
_AtmfCESRetryFailures_Object = MibTableColumn
atmfCESRetryFailures = _AtmfCESRetryFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 5),
    _AtmfCESRetryFailures_Type()
)
atmfCESRetryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESRetryFailures.setStatus("mandatory")


class _AtmfCESActiveSvcRestart_Type(Integer32):
    """Custom type atmfCESActiveSvcRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("restart", 1))
    )


_AtmfCESActiveSvcRestart_Type.__name__ = "Integer32"
_AtmfCESActiveSvcRestart_Object = MibTableColumn
atmfCESActiveSvcRestart = _AtmfCESActiveSvcRestart_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 6),
    _AtmfCESActiveSvcRestart_Type()
)
atmfCESActiveSvcRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESActiveSvcRestart.setStatus("mandatory")
_AtmfCESActiveSvcOperStatus_Type = Integer32
_AtmfCESActiveSvcOperStatus_Object = MibTableColumn
atmfCESActiveSvcOperStatus = _AtmfCESActiveSvcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 7),
    _AtmfCESActiveSvcOperStatus_Type()
)
atmfCESActiveSvcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESActiveSvcOperStatus.setStatus("mandatory")


class _AtmfCESLastReleaseCause_Type(Integer32):
    """Custom type atmfCESLastReleaseCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AtmfCESLastReleaseCause_Type.__name__ = "Integer32"
_AtmfCESLastReleaseCause_Object = MibTableColumn
atmfCESLastReleaseCause = _AtmfCESLastReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 8),
    _AtmfCESLastReleaseCause_Type()
)
atmfCESLastReleaseCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESLastReleaseCause.setStatus("mandatory")
_AtmfCESLastReleaseDiagnostics_Type = OctetString
_AtmfCESLastReleaseDiagnostics_Object = MibTableColumn
atmfCESLastReleaseDiagnostics = _AtmfCESLastReleaseDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 9),
    _AtmfCESLastReleaseDiagnostics_Type()
)
atmfCESLastReleaseDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESLastReleaseDiagnostics.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-ces-MIB",
    **{"atmForum": atmForum,
       "atmForumNetworkManagment": atmForumNetworkManagment,
       "atmfCESmib": atmfCESmib,
       "atmfCES": atmfCES,
       "atmfCESObjects": atmfCESObjects,
       "atmfCESConTable": atmfCESConTable,
       "atmfCESConTableEntry": atmfCESConTableEntry,
       "atmfCESCbrIndex": atmfCESCbrIndex,
       "atmfCESAtmIndex": atmfCESAtmIndex,
       "atmfCESAtmVpi": atmfCESAtmVpi,
       "atmfCESAtmVci": atmfCESAtmVci,
       "atmfCESCbrService": atmfCESCbrService,
       "atmfCESCbrClockMode": atmfCESCbrClockMode,
       "atmfCESCas": atmfCESCas,
       "atmfCESPartialFill": atmfCESPartialFill,
       "atmfCESBufMaxSize": atmfCESBufMaxSize,
       "atmfCESCdvtRxT": atmfCESCdvtRxT,
       "atmfCESCellLossIntegrationPeriod": atmfCESCellLossIntegrationPeriod,
       "atmfCESConnType": atmfCESConnType,
       "atmfCESLocalAddr": atmfCESLocalAddr,
       "atmfCESAdminStatus": atmfCESAdminStatus,
       "atmfCESOperStatus": atmfCESOperStatus,
       "atmCESConfRowStatus": atmCESConfRowStatus,
       "atmfCESMappingTable": atmfCESMappingTable,
       "atmfCESMappingTableEntry": atmfCESMappingTableEntry,
       "atmfCESMappingCbrIndex": atmfCESMappingCbrIndex,
       "atmfCESStatsTable": atmfCESStatsTable,
       "atmfCESStatsTableEntry": atmfCESStatsTableEntry,
       "atmfCESReassCells": atmfCESReassCells,
       "atmfCESHdrErrors": atmfCESHdrErrors,
       "atmfCESPointerReframes": atmfCESPointerReframes,
       "atmfCESPointerParityErrors": atmfCESPointerParityErrors,
       "atmfCESAal1SeqErrors": atmfCESAal1SeqErrors,
       "atmfCESLostCells": atmfCESLostCells,
       "atmfCESMisinsertedCells": atmfCESMisinsertedCells,
       "atmfCESBufUnderflows": atmfCESBufUnderflows,
       "atmfCESBufOverflows": atmfCESBufOverflows,
       "atmfCESCellLossStatus": atmfCESCellLossStatus,
       "atmfCESActiveSvcTable": atmfCESActiveSvcTable,
       "atmfCESActiveSvcTableEntry": atmfCESActiveSvcTableEntry,
       "atmfCESRemoteAddr": atmfCESRemoteAddr,
       "atmfCESFirstRetryInterval": atmfCESFirstRetryInterval,
       "atmfCESRetryTimer": atmfCESRetryTimer,
       "atmfCESRetryLimit": atmfCESRetryLimit,
       "atmfCESRetryFailures": atmfCESRetryFailures,
       "atmfCESActiveSvcRestart": atmfCESActiveSvcRestart,
       "atmfCESActiveSvcOperStatus": atmfCESActiveSvcOperStatus,
       "atmfCESLastReleaseCause": atmfCESLastReleaseCause,
       "atmfCESLastReleaseDiagnostics": atmfCESLastReleaseDiagnostics}
)

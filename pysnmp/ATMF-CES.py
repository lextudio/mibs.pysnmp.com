# SNMP MIB module (ATMF-CES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATMF-CES
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:10 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

atmfCES = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2)
)
atmfCES.setRevisions(
        ("1995-02-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VpiInteger(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class VciInteger(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CESConnectionPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class AtmAddr(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(20, 20),
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfCESmib_ObjectIdentity = ObjectIdentity
atmfCESmib = _AtmfCESmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 2)
)
_AtmfCESObjects_ObjectIdentity = ObjectIdentity
atmfCESObjects = _AtmfCESObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1)
)
_AtmfCESConfTable_Object = MibTable
atmfCESConfTable = _AtmfCESConfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    atmfCESConfTable.setStatus("current")
_AtmfCESConfEntry_Object = MibTableRow
atmfCESConfEntry = _AtmfCESConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1)
)
atmfCESConfEntry.setIndexNames(
    (0, "ATMF-CES", "atmfCESCbrIndex"),
)
if mibBuilder.loadTexts:
    atmfCESConfEntry.setStatus("current")
_AtmfCESCbrIndex_Type = InterfaceIndex
_AtmfCESCbrIndex_Object = MibTableColumn
atmfCESCbrIndex = _AtmfCESCbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 1),
    _AtmfCESCbrIndex_Type()
)
atmfCESCbrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmfCESCbrIndex.setStatus("current")
_AtmfCESAtmIndex_Type = CESConnectionPort
_AtmfCESAtmIndex_Object = MibTableColumn
atmfCESAtmIndex = _AtmfCESAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 2),
    _AtmfCESAtmIndex_Type()
)
atmfCESAtmIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESAtmIndex.setStatus("current")
_AtmfCESAtmVpi_Type = VpiInteger
_AtmfCESAtmVpi_Object = MibTableColumn
atmfCESAtmVpi = _AtmfCESAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 3),
    _AtmfCESAtmVpi_Type()
)
atmfCESAtmVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESAtmVpi.setStatus("current")
_AtmfCESAtmVci_Type = VciInteger
_AtmfCESAtmVci_Object = MibTableColumn
atmfCESAtmVci = _AtmfCESAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 4),
    _AtmfCESAtmVci_Type()
)
atmfCESAtmVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESAtmVci.setStatus("current")


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
atmfCESCbrService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESCbrService.setStatus("current")


class _AtmfCESCbrClockMode_Type(Integer32):
    """Custom type atmfCESCbrClockMode based on Integer32"""
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
        *(("adaptive", 3),
          ("srts", 2),
          ("synchronous", 1))
    )


_AtmfCESCbrClockMode_Type.__name__ = "Integer32"
_AtmfCESCbrClockMode_Object = MibTableColumn
atmfCESCbrClockMode = _AtmfCESCbrClockMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 6),
    _AtmfCESCbrClockMode_Type()
)
atmfCESCbrClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESCbrClockMode.setStatus("current")


class _AtmfCESCas_Type(Integer32):
    """Custom type atmfCESCas based on Integer32"""
    defaultValue = 1

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
atmfCESCas.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESCas.setStatus("current")


class _AtmfCESPartialFill_Type(Integer32):
    """Custom type atmfCESPartialFill based on Integer32"""
    defaultValue = 0

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
atmfCESPartialFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESPartialFill.setStatus("current")


class _AtmfCESBufMaxSize_Type(Integer32):
    """Custom type atmfCESBufMaxSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_AtmfCESBufMaxSize_Type.__name__ = "Integer32"
_AtmfCESBufMaxSize_Object = MibTableColumn
atmfCESBufMaxSize = _AtmfCESBufMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 9),
    _AtmfCESBufMaxSize_Type()
)
atmfCESBufMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESBufMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    atmfCESBufMaxSize.setUnits("10 usec")


class _AtmfCESCdvRxT_Type(Integer32):
    """Custom type atmfCESCdvRxT based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmfCESCdvRxT_Type.__name__ = "Integer32"
_AtmfCESCdvRxT_Object = MibTableColumn
atmfCESCdvRxT = _AtmfCESCdvRxT_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 10),
    _AtmfCESCdvRxT_Type()
)
atmfCESCdvRxT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESCdvRxT.setStatus("current")
if mibBuilder.loadTexts:
    atmfCESCdvRxT.setUnits("10 usec")


class _AtmfCESCellLossIntegrationPeriod_Type(Integer32):
    """Custom type atmfCESCellLossIntegrationPeriod based on Integer32"""
    defaultValue = 2500

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
atmfCESCellLossIntegrationPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESCellLossIntegrationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    atmfCESCellLossIntegrationPeriod.setUnits("msec")


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
atmfCESConnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESConnType.setStatus("current")
_AtmfCESLocalAddr_Type = AtmAddr
_AtmfCESLocalAddr_Object = MibTableColumn
atmfCESLocalAddr = _AtmfCESLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 13),
    _AtmfCESLocalAddr_Type()
)
atmfCESLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESLocalAddr.setStatus("current")


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
atmfCESAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESAdminStatus.setStatus("current")


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
    atmfCESOperStatus.setStatus("current")
_AtmfCESConfRowStatus_Type = RowStatus
_AtmfCESConfRowStatus_Object = MibTableColumn
atmfCESConfRowStatus = _AtmfCESConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 1, 1, 16),
    _AtmfCESConfRowStatus_Type()
)
atmfCESConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmfCESConfRowStatus.setStatus("current")
_AtmfCESMappingTable_Object = MibTable
atmfCESMappingTable = _AtmfCESMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    atmfCESMappingTable.setStatus("current")
_AtmfCESMappingEntry_Object = MibTableRow
atmfCESMappingEntry = _AtmfCESMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 2, 1)
)
atmfCESMappingEntry.setIndexNames(
    (0, "ATMF-CES", "atmfCESAtmIndex"),
    (0, "ATMF-CES", "atmfCESAtmVpi"),
    (0, "ATMF-CES", "atmfCESAtmVci"),
)
if mibBuilder.loadTexts:
    atmfCESMappingEntry.setStatus("current")
_AtmfCESMappingCbrIndex_Type = InterfaceIndex
_AtmfCESMappingCbrIndex_Object = MibTableColumn
atmfCESMappingCbrIndex = _AtmfCESMappingCbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 2, 1, 1),
    _AtmfCESMappingCbrIndex_Type()
)
atmfCESMappingCbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESMappingCbrIndex.setStatus("current")
_AtmfCESStatsTable_Object = MibTable
atmfCESStatsTable = _AtmfCESStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    atmfCESStatsTable.setStatus("current")
_AtmfCESStatsEntry_Object = MibTableRow
atmfCESStatsEntry = _AtmfCESStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atmfCESStatsEntry.setStatus("current")
_AtmfCESReassCells_Type = Counter32
_AtmfCESReassCells_Object = MibTableColumn
atmfCESReassCells = _AtmfCESReassCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 1),
    _AtmfCESReassCells_Type()
)
atmfCESReassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESReassCells.setStatus("current")
_AtmfCESHdrErrors_Type = Counter32
_AtmfCESHdrErrors_Object = MibTableColumn
atmfCESHdrErrors = _AtmfCESHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 2),
    _AtmfCESHdrErrors_Type()
)
atmfCESHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESHdrErrors.setStatus("current")
_AtmfCESPointerReframes_Type = Counter32
_AtmfCESPointerReframes_Object = MibTableColumn
atmfCESPointerReframes = _AtmfCESPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 3),
    _AtmfCESPointerReframes_Type()
)
atmfCESPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESPointerReframes.setStatus("current")
_AtmfCESPointerParityErrors_Type = Counter32
_AtmfCESPointerParityErrors_Object = MibTableColumn
atmfCESPointerParityErrors = _AtmfCESPointerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 4),
    _AtmfCESPointerParityErrors_Type()
)
atmfCESPointerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESPointerParityErrors.setStatus("current")
_AtmfCESAal1SeqErrors_Type = Counter32
_AtmfCESAal1SeqErrors_Object = MibTableColumn
atmfCESAal1SeqErrors = _AtmfCESAal1SeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 5),
    _AtmfCESAal1SeqErrors_Type()
)
atmfCESAal1SeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESAal1SeqErrors.setStatus("current")
_AtmfCESLostCells_Type = Counter32
_AtmfCESLostCells_Object = MibTableColumn
atmfCESLostCells = _AtmfCESLostCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 6),
    _AtmfCESLostCells_Type()
)
atmfCESLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESLostCells.setStatus("current")
_AtmfCESMisinsertedCells_Type = Counter32
_AtmfCESMisinsertedCells_Object = MibTableColumn
atmfCESMisinsertedCells = _AtmfCESMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 7),
    _AtmfCESMisinsertedCells_Type()
)
atmfCESMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESMisinsertedCells.setStatus("current")
_AtmfCESBufUnderflows_Type = Counter32
_AtmfCESBufUnderflows_Object = MibTableColumn
atmfCESBufUnderflows = _AtmfCESBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 8),
    _AtmfCESBufUnderflows_Type()
)
atmfCESBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESBufUnderflows.setStatus("current")
_AtmfCESBufOverflows_Type = Counter32
_AtmfCESBufOverflows_Object = MibTableColumn
atmfCESBufOverflows = _AtmfCESBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 9),
    _AtmfCESBufOverflows_Type()
)
atmfCESBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESBufOverflows.setStatus("current")


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
          ("noLoss", 1))
    )


_AtmfCESCellLossStatus_Type.__name__ = "Integer32"
_AtmfCESCellLossStatus_Object = MibTableColumn
atmfCESCellLossStatus = _AtmfCESCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 3, 1, 10),
    _AtmfCESCellLossStatus_Type()
)
atmfCESCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESCellLossStatus.setStatus("current")
_AtmfCESActiveSvcTable_Object = MibTable
atmfCESActiveSvcTable = _AtmfCESActiveSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    atmfCESActiveSvcTable.setStatus("current")
_AtmfCESActiveSvcEntry_Object = MibTableRow
atmfCESActiveSvcEntry = _AtmfCESActiveSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1)
)
atmfCESActiveSvcEntry.setIndexNames(
    (0, "ATMF-CES", "atmfCESCbrIndex"),
)
if mibBuilder.loadTexts:
    atmfCESActiveSvcEntry.setStatus("current")
_AtmfCESRemoteAddr_Type = AtmAddr
_AtmfCESRemoteAddr_Object = MibTableColumn
atmfCESRemoteAddr = _AtmfCESRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 1),
    _AtmfCESRemoteAddr_Type()
)
atmfCESRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmfCESRemoteAddr.setStatus("current")


class _AtmfCESFirstRetryInterval_Type(Integer32):
    """Custom type atmfCESFirstRetryInterval based on Integer32"""
    defaultValue = 10

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
    atmfCESFirstRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    atmfCESFirstRetryInterval.setUnits("seconds")


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
    atmfCESRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    atmfCESRetryTimer.setUnits("seconds")


class _AtmfCESRetryLimit_Type(Integer32):
    """Custom type atmfCESRetryLimit based on Integer32"""
    defaultValue = 0

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
    atmfCESRetryLimit.setStatus("current")
_AtmfCESRetryFailures_Type = Gauge32
_AtmfCESRetryFailures_Object = MibTableColumn
atmfCESRetryFailures = _AtmfCESRetryFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 5),
    _AtmfCESRetryFailures_Type()
)
atmfCESRetryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESRetryFailures.setStatus("current")


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
    atmfCESActiveSvcRestart.setStatus("current")


class _AtmfCESActiveSvcOperStatus_Type(Integer32):
    """Custom type atmfCESActiveSvcOperStatus based on Integer32"""
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
        *(("connected", 3),
          ("establishmentInProgress", 2),
          ("lowerLayerDown", 6),
          ("noAddressSupplied", 5),
          ("other", 1),
          ("retriesExhausted", 4))
    )


_AtmfCESActiveSvcOperStatus_Type.__name__ = "Integer32"
_AtmfCESActiveSvcOperStatus_Object = MibTableColumn
atmfCESActiveSvcOperStatus = _AtmfCESActiveSvcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 7),
    _AtmfCESActiveSvcOperStatus_Type()
)
atmfCESActiveSvcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESActiveSvcOperStatus.setStatus("current")


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
    atmfCESLastReleaseCause.setStatus("current")


class _AtmfCESLastReleaseDiagnostics_Type(OctetString):
    """Custom type atmfCESLastReleaseDiagnostics based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtmfCESLastReleaseDiagnostics_Type.__name__ = "OctetString"
_AtmfCESLastReleaseDiagnostics_Object = MibTableColumn
atmfCESLastReleaseDiagnostics = _AtmfCESLastReleaseDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 1, 4, 1, 9),
    _AtmfCESLastReleaseDiagnostics_Type()
)
atmfCESLastReleaseDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfCESLastReleaseDiagnostics.setStatus("current")
_AtmfCESConformance_ObjectIdentity = ObjectIdentity
atmfCESConformance = _AtmfCESConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2)
)
_AtmfCESGroups_ObjectIdentity = ObjectIdentity
atmfCESGroups = _AtmfCESGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 1)
)
_AtmfCESCompliances_ObjectIdentity = ObjectIdentity
atmfCESCompliances = _AtmfCESCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 2)
)
atmfCESConfEntry.registerAugmentions(
    ("ATMF-CES",
     "atmfCESStatsEntry")
)
atmfCESStatsEntry.setIndexNames(*atmfCESConfEntry.getIndexNames())

# Managed Objects groups

atmfCESBasicConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 1, 1)
)
atmfCESBasicConfigGroup.setObjects(
      *(("ATMF-CES", "atmfCESAtmIndex"),
        ("ATMF-CES", "atmfCESAtmVpi"),
        ("ATMF-CES", "atmfCESAtmVci"),
        ("ATMF-CES", "atmfCESCbrService"),
        ("ATMF-CES", "atmfCESCbrClockMode"),
        ("ATMF-CES", "atmfCESBufMaxSize"),
        ("ATMF-CES", "atmfCESCdvRxT"),
        ("ATMF-CES", "atmfCESCellLossIntegrationPeriod"),
        ("ATMF-CES", "atmfCESConnType"),
        ("ATMF-CES", "atmfCESConfRowStatus"))
)
if mibBuilder.loadTexts:
    atmfCESBasicConfigGroup.setStatus("current")

atmfCESOptionalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 1, 2)
)
atmfCESOptionalConfigGroup.setObjects(
      *(("ATMF-CES", "atmfCESAdminStatus"),
        ("ATMF-CES", "atmfCESOperStatus"))
)
if mibBuilder.loadTexts:
    atmfCESOptionalConfigGroup.setStatus("current")

atmfCESBasicStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 1, 3)
)
atmfCESBasicStatsGroup.setObjects(
      *(("ATMF-CES", "atmfCESReassCells"),
        ("ATMF-CES", "atmfCESHdrErrors"),
        ("ATMF-CES", "atmfCESBufUnderflows"),
        ("ATMF-CES", "atmfCESBufOverflows"),
        ("ATMF-CES", "atmfCESCellLossStatus"))
)
if mibBuilder.loadTexts:
    atmfCESBasicStatsGroup.setStatus("current")

atmfCESOptionalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 1, 4)
)
atmfCESOptionalStatsGroup.setObjects(
      *(("ATMF-CES", "atmfCESAal1SeqErrors"),
        ("ATMF-CES", "atmfCESLostCells"),
        ("ATMF-CES", "atmfCESMisinsertedCells"))
)
if mibBuilder.loadTexts:
    atmfCESOptionalStatsGroup.setStatus("current")

atmfCESStructConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 1, 5)
)
atmfCESStructConfigGroup.setObjects(
      *(("ATMF-CES", "atmfCESCas"),
        ("ATMF-CES", "atmfCESPartialFill"))
)
if mibBuilder.loadTexts:
    atmfCESStructConfigGroup.setStatus("current")

atmfCESStructStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 1, 6)
)
atmfCESStructStatsGroup.setObjects(
    ("ATMF-CES", "atmfCESPointerReframes")
)
if mibBuilder.loadTexts:
    atmfCESStructStatsGroup.setStatus("current")

atmfCESOptionalStructStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 1, 7)
)
atmfCESOptionalStructStatsGroup.setObjects(
    ("ATMF-CES", "atmfCESPointerParityErrors")
)
if mibBuilder.loadTexts:
    atmfCESOptionalStructStatsGroup.setStatus("current")

atmfCESMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 1, 8)
)
atmfCESMappingGroup.setObjects(
    ("ATMF-CES", "atmfCESMappingCbrIndex")
)
if mibBuilder.loadTexts:
    atmfCESMappingGroup.setStatus("current")

atmfCESSvcConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 1, 9)
)
atmfCESSvcConfigGroup.setObjects(
      *(("ATMF-CES", "atmfCESLocalAddr"),
        ("ATMF-CES", "atmfCESRemoteAddr"),
        ("ATMF-CES", "atmfCESFirstRetryInterval"),
        ("ATMF-CES", "atmfCESRetryTimer"),
        ("ATMF-CES", "atmfCESRetryFailures"),
        ("ATMF-CES", "atmfCESActiveSvcRestart"),
        ("ATMF-CES", "atmfCESActiveSvcOperStatus"))
)
if mibBuilder.loadTexts:
    atmfCESSvcConfigGroup.setStatus("current")

atmfCESOptionalSvcConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 1, 10)
)
atmfCESOptionalSvcConfigGroup.setObjects(
      *(("ATMF-CES", "atmfCESRetryLimit"),
        ("ATMF-CES", "atmfCESLastReleaseCause"),
        ("ATMF-CES", "atmfCESLastReleaseDiagnostics"))
)
if mibBuilder.loadTexts:
    atmfCESOptionalSvcConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

atmfCESCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmfCESCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATMF-CES",
    **{"VpiInteger": VpiInteger,
       "VciInteger": VciInteger,
       "CESConnectionPort": CESConnectionPort,
       "AtmAddr": AtmAddr,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfCESmib": atmfCESmib,
       "atmfCES": atmfCES,
       "atmfCESObjects": atmfCESObjects,
       "atmfCESConfTable": atmfCESConfTable,
       "atmfCESConfEntry": atmfCESConfEntry,
       "atmfCESCbrIndex": atmfCESCbrIndex,
       "atmfCESAtmIndex": atmfCESAtmIndex,
       "atmfCESAtmVpi": atmfCESAtmVpi,
       "atmfCESAtmVci": atmfCESAtmVci,
       "atmfCESCbrService": atmfCESCbrService,
       "atmfCESCbrClockMode": atmfCESCbrClockMode,
       "atmfCESCas": atmfCESCas,
       "atmfCESPartialFill": atmfCESPartialFill,
       "atmfCESBufMaxSize": atmfCESBufMaxSize,
       "atmfCESCdvRxT": atmfCESCdvRxT,
       "atmfCESCellLossIntegrationPeriod": atmfCESCellLossIntegrationPeriod,
       "atmfCESConnType": atmfCESConnType,
       "atmfCESLocalAddr": atmfCESLocalAddr,
       "atmfCESAdminStatus": atmfCESAdminStatus,
       "atmfCESOperStatus": atmfCESOperStatus,
       "atmfCESConfRowStatus": atmfCESConfRowStatus,
       "atmfCESMappingTable": atmfCESMappingTable,
       "atmfCESMappingEntry": atmfCESMappingEntry,
       "atmfCESMappingCbrIndex": atmfCESMappingCbrIndex,
       "atmfCESStatsTable": atmfCESStatsTable,
       "atmfCESStatsEntry": atmfCESStatsEntry,
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
       "atmfCESActiveSvcEntry": atmfCESActiveSvcEntry,
       "atmfCESRemoteAddr": atmfCESRemoteAddr,
       "atmfCESFirstRetryInterval": atmfCESFirstRetryInterval,
       "atmfCESRetryTimer": atmfCESRetryTimer,
       "atmfCESRetryLimit": atmfCESRetryLimit,
       "atmfCESRetryFailures": atmfCESRetryFailures,
       "atmfCESActiveSvcRestart": atmfCESActiveSvcRestart,
       "atmfCESActiveSvcOperStatus": atmfCESActiveSvcOperStatus,
       "atmfCESLastReleaseCause": atmfCESLastReleaseCause,
       "atmfCESLastReleaseDiagnostics": atmfCESLastReleaseDiagnostics,
       "atmfCESConformance": atmfCESConformance,
       "atmfCESGroups": atmfCESGroups,
       "atmfCESBasicConfigGroup": atmfCESBasicConfigGroup,
       "atmfCESOptionalConfigGroup": atmfCESOptionalConfigGroup,
       "atmfCESBasicStatsGroup": atmfCESBasicStatsGroup,
       "atmfCESOptionalStatsGroup": atmfCESOptionalStatsGroup,
       "atmfCESStructConfigGroup": atmfCESStructConfigGroup,
       "atmfCESStructStatsGroup": atmfCESStructStatsGroup,
       "atmfCESOptionalStructStatsGroup": atmfCESOptionalStructStatsGroup,
       "atmfCESMappingGroup": atmfCESMappingGroup,
       "atmfCESSvcConfigGroup": atmfCESSvcConfigGroup,
       "atmfCESOptionalSvcConfigGroup": atmfCESOptionalSvcConfigGroup,
       "atmfCESCompliances": atmfCESCompliances,
       "atmfCESCompliance": atmfCESCompliance}
)

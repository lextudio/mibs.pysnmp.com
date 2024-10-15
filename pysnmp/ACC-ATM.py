# SNMP MIB module (ACC-ATM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-ATM
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:49 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccAtm_ObjectIdentity = ObjectIdentity
accAtm = _AccAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77)
)
_AtmStatsGrp_ObjectIdentity = ObjectIdentity
atmStatsGrp = _AtmStatsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1)
)
_AtmStatsAtmLayerTable_Object = MibTable
atmStatsAtmLayerTable = _AtmStatsAtmLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 1)
)
if mibBuilder.loadTexts:
    atmStatsAtmLayerTable.setStatus("mandatory")
_AtmStatsAtmLayerEntry_Object = MibTableRow
atmStatsAtmLayerEntry = _AtmStatsAtmLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 1, 1)
)
atmStatsAtmLayerEntry.setIndexNames(
    (0, "ACC-ATM", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmStatsAtmLayerEntry.setStatus("mandatory")
_AtmStatsAtmLayerRxCells_Type = Counter32
_AtmStatsAtmLayerRxCells_Object = MibTableColumn
atmStatsAtmLayerRxCells = _AtmStatsAtmLayerRxCells_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 1, 1, 1),
    _AtmStatsAtmLayerRxCells_Type()
)
atmStatsAtmLayerRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsAtmLayerRxCells.setStatus("mandatory")
_AtmStatsAtmLayerTxCells_Type = Counter32
_AtmStatsAtmLayerTxCells_Object = MibTableColumn
atmStatsAtmLayerTxCells = _AtmStatsAtmLayerTxCells_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 1, 1, 2),
    _AtmStatsAtmLayerTxCells_Type()
)
atmStatsAtmLayerTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsAtmLayerTxCells.setStatus("mandatory")
_AtmStatsAtmLayerDiscCells_Type = Counter32
_AtmStatsAtmLayerDiscCells_Object = MibTableColumn
atmStatsAtmLayerDiscCells = _AtmStatsAtmLayerDiscCells_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 1, 1, 3),
    _AtmStatsAtmLayerDiscCells_Type()
)
atmStatsAtmLayerDiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsAtmLayerDiscCells.setStatus("mandatory")
_AtmStatsAtmLayerDropCells_Type = Counter32
_AtmStatsAtmLayerDropCells_Object = MibTableColumn
atmStatsAtmLayerDropCells = _AtmStatsAtmLayerDropCells_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 1, 1, 4),
    _AtmStatsAtmLayerDropCells_Type()
)
atmStatsAtmLayerDropCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsAtmLayerDropCells.setStatus("mandatory")
_AtmStatsCallTable_Object = MibTable
atmStatsCallTable = _AtmStatsCallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 2)
)
if mibBuilder.loadTexts:
    atmStatsCallTable.setStatus("mandatory")
_AtmStatsCallEntry_Object = MibTableRow
atmStatsCallEntry = _AtmStatsCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 2, 1)
)
atmStatsCallEntry.setIndexNames(
    (0, "ACC-ATM", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmStatsCallEntry.setStatus("mandatory")
_AtmStatsCallOrigCalls_Type = Counter32
_AtmStatsCallOrigCalls_Object = MibTableColumn
atmStatsCallOrigCalls = _AtmStatsCallOrigCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 2, 1, 1),
    _AtmStatsCallOrigCalls_Type()
)
atmStatsCallOrigCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsCallOrigCalls.setStatus("mandatory")
_AtmStatsCallOffCalls_Type = Counter32
_AtmStatsCallOffCalls_Object = MibTableColumn
atmStatsCallOffCalls = _AtmStatsCallOffCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 2, 1, 2),
    _AtmStatsCallOffCalls_Type()
)
atmStatsCallOffCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsCallOffCalls.setStatus("mandatory")
_AtmStatsCallAccCalls_Type = Counter32
_AtmStatsCallAccCalls_Object = MibTableColumn
atmStatsCallAccCalls = _AtmStatsCallAccCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 2, 1, 3),
    _AtmStatsCallAccCalls_Type()
)
atmStatsCallAccCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsCallAccCalls.setStatus("mandatory")
_AtmStatsCallCompCalls_Type = Counter32
_AtmStatsCallCompCalls_Object = MibTableColumn
atmStatsCallCompCalls = _AtmStatsCallCompCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 2, 1, 4),
    _AtmStatsCallCompCalls_Type()
)
atmStatsCallCompCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsCallCompCalls.setStatus("mandatory")
_AtmStatsCallClrCalls_Type = Counter32
_AtmStatsCallClrCalls_Object = MibTableColumn
atmStatsCallClrCalls = _AtmStatsCallClrCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 1, 2, 1, 5),
    _AtmStatsCallClrCalls_Type()
)
atmStatsCallClrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmStatsCallClrCalls.setStatus("mandatory")
_AtmOamGrp_ObjectIdentity = ObjectIdentity
atmOamGrp = _AtmOamGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5)
)
_AtmOamConfTable_Object = MibTable
atmOamConfTable = _AtmOamConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 1)
)
if mibBuilder.loadTexts:
    atmOamConfTable.setStatus("mandatory")
_AtmOamConfEntry_Object = MibTableRow
atmOamConfEntry = _AtmOamConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 1, 1)
)
atmOamConfEntry.setIndexNames(
    (0, "ACC-ATM", "atmOamIndex"),
)
if mibBuilder.loadTexts:
    atmOamConfEntry.setStatus("mandatory")
_AtmOamIndex_Type = IfIndex
_AtmOamIndex_Object = MibTableColumn
atmOamIndex = _AtmOamIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 1, 1, 1),
    _AtmOamIndex_Type()
)
atmOamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamIndex.setStatus("mandatory")


class _AtmOamPhyFlowType_Type(Integer32):
    """Custom type atmOamPhyFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("f1", 1),
          ("f2", 2),
          ("f3", 3))
    )


_AtmOamPhyFlowType_Type.__name__ = "Integer32"
_AtmOamPhyFlowType_Object = MibTableColumn
atmOamPhyFlowType = _AtmOamPhyFlowType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 1, 1, 2),
    _AtmOamPhyFlowType_Type()
)
atmOamPhyFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamPhyFlowType.setStatus("mandatory")


class _AtmOamFlowState_Type(Integer32):
    """Custom type atmOamFlowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AtmOamFlowState_Type.__name__ = "Integer32"
_AtmOamFlowState_Object = MibTableColumn
atmOamFlowState = _AtmOamFlowState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 1, 1, 3),
    _AtmOamFlowState_Type()
)
atmOamFlowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamFlowState.setStatus("mandatory")
_AtmOamVpcTable_Object = MibTable
atmOamVpcTable = _AtmOamVpcTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 2)
)
if mibBuilder.loadTexts:
    atmOamVpcTable.setStatus("mandatory")
_AtmOamVpcEntry_Object = MibTableRow
atmOamVpcEntry = _AtmOamVpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 2, 1)
)
atmOamVpcEntry.setIndexNames(
    (0, "ACC-ATM", "atmOamVpcIndex"),
    (0, "ACC-ATM", "atmOamVpcVpi"),
)
if mibBuilder.loadTexts:
    atmOamVpcEntry.setStatus("mandatory")
_AtmOamVpcIndex_Type = IfIndex
_AtmOamVpcIndex_Object = MibTableColumn
atmOamVpcIndex = _AtmOamVpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 2, 1, 1),
    _AtmOamVpcIndex_Type()
)
atmOamVpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamVpcIndex.setStatus("mandatory")


class _AtmOamVpcVpi_Type(Integer32):
    """Custom type atmOamVpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmOamVpcVpi_Type.__name__ = "Integer32"
_AtmOamVpcVpi_Object = MibTableColumn
atmOamVpcVpi = _AtmOamVpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 2, 1, 2),
    _AtmOamVpcVpi_Type()
)
atmOamVpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamVpcVpi.setStatus("mandatory")


class _AtmOamVpcFlowType_Type(Integer32):
    """Custom type atmOamVpcFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end2end", 1),
          ("segment", 2))
    )


_AtmOamVpcFlowType_Type.__name__ = "Integer32"
_AtmOamVpcFlowType_Object = MibTableColumn
atmOamVpcFlowType = _AtmOamVpcFlowType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 2, 1, 3),
    _AtmOamVpcFlowType_Type()
)
atmOamVpcFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamVpcFlowType.setStatus("mandatory")
_AtmOamVpcRowStatus_Type = RowStatus
_AtmOamVpcRowStatus_Object = MibTableColumn
atmOamVpcRowStatus = _AtmOamVpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 2, 1, 4),
    _AtmOamVpcRowStatus_Type()
)
atmOamVpcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamVpcRowStatus.setStatus("mandatory")
_AtmOamVccTable_Object = MibTable
atmOamVccTable = _AtmOamVccTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 3)
)
if mibBuilder.loadTexts:
    atmOamVccTable.setStatus("mandatory")
_AtmOamVccEntry_Object = MibTableRow
atmOamVccEntry = _AtmOamVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 3, 1)
)
atmOamVccEntry.setIndexNames(
    (0, "ACC-ATM", "atmOamVccIndex"),
    (0, "ACC-ATM", "atmOamVccVpi"),
    (0, "ACC-ATM", "atmOamVccVci"),
)
if mibBuilder.loadTexts:
    atmOamVccEntry.setStatus("mandatory")
_AtmOamVccIndex_Type = IfIndex
_AtmOamVccIndex_Object = MibTableColumn
atmOamVccIndex = _AtmOamVccIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 3, 1, 1),
    _AtmOamVccIndex_Type()
)
atmOamVccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamVccIndex.setStatus("mandatory")


class _AtmOamVccVpi_Type(Integer32):
    """Custom type atmOamVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmOamVccVpi_Type.__name__ = "Integer32"
_AtmOamVccVpi_Object = MibTableColumn
atmOamVccVpi = _AtmOamVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 3, 1, 2),
    _AtmOamVccVpi_Type()
)
atmOamVccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamVccVpi.setStatus("mandatory")


class _AtmOamVccVci_Type(Integer32):
    """Custom type atmOamVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmOamVccVci_Type.__name__ = "Integer32"
_AtmOamVccVci_Object = MibTableColumn
atmOamVccVci = _AtmOamVccVci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 3, 1, 3),
    _AtmOamVccVci_Type()
)
atmOamVccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOamVccVci.setStatus("mandatory")


class _AtmOamVccFlowType_Type(Integer32):
    """Custom type atmOamVccFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end2end", 1),
          ("segment", 2))
    )


_AtmOamVccFlowType_Type.__name__ = "Integer32"
_AtmOamVccFlowType_Object = MibTableColumn
atmOamVccFlowType = _AtmOamVccFlowType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 3, 1, 4),
    _AtmOamVccFlowType_Type()
)
atmOamVccFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamVccFlowType.setStatus("mandatory")
_AtmOamVccRowStatus_Type = RowStatus
_AtmOamVccRowStatus_Object = MibTableColumn
atmOamVccRowStatus = _AtmOamVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 5, 3, 1, 5),
    _AtmOamVccRowStatus_Type()
)
atmOamVccRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOamVccRowStatus.setStatus("mandatory")
_AtmIlmiGrp_ObjectIdentity = ObjectIdentity
atmIlmiGrp = _AtmIlmiGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 6)
)
_AtmIlmiConfTable_Object = MibTable
atmIlmiConfTable = _AtmIlmiConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 6, 1)
)
if mibBuilder.loadTexts:
    atmIlmiConfTable.setStatus("mandatory")
_AtmIlmiConfEntry_Object = MibTableRow
atmIlmiConfEntry = _AtmIlmiConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 6, 1, 1)
)
atmIlmiConfEntry.setIndexNames(
    (0, "ACC-ATM", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmIlmiConfEntry.setStatus("mandatory")


class _AtmIlmiImeType_Type(Integer32):
    """Custom type atmIlmiImeType based on Integer32"""
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
        *(("network", 1),
          ("symmetric", 3),
          ("user", 2))
    )


_AtmIlmiImeType_Type.__name__ = "Integer32"
_AtmIlmiImeType_Object = MibTableColumn
atmIlmiImeType = _AtmIlmiImeType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 6, 1, 1, 1),
    _AtmIlmiImeType_Type()
)
atmIlmiImeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIlmiImeType.setStatus("mandatory")


class _AtmIlmiUniType_Type(Integer32):
    """Custom type atmIlmiUniType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_AtmIlmiUniType_Type.__name__ = "Integer32"
_AtmIlmiUniType_Object = MibTableColumn
atmIlmiUniType = _AtmIlmiUniType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 6, 1, 1, 2),
    _AtmIlmiUniType_Type()
)
atmIlmiUniType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIlmiUniType.setStatus("mandatory")
_AtmIlmiCommStrTable_Object = MibTable
atmIlmiCommStrTable = _AtmIlmiCommStrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 6, 2)
)
if mibBuilder.loadTexts:
    atmIlmiCommStrTable.setStatus("mandatory")
_AtmIlmiCommStrEntry_Object = MibTableRow
atmIlmiCommStrEntry = _AtmIlmiCommStrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 6, 2, 1)
)
atmIlmiCommStrEntry.setIndexNames(
    (0, "ACC-ATM", "atmIlmiCommStrIndex"),
    (0, "ACC-ATM", "atmIlmiCommStr"),
)
if mibBuilder.loadTexts:
    atmIlmiCommStrEntry.setStatus("mandatory")
_AtmIlmiCommStrIndex_Type = IfIndex
_AtmIlmiCommStrIndex_Object = MibTableColumn
atmIlmiCommStrIndex = _AtmIlmiCommStrIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 6, 2, 1, 1),
    _AtmIlmiCommStrIndex_Type()
)
atmIlmiCommStrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIlmiCommStrIndex.setStatus("mandatory")


class _AtmIlmiCommStr_Type(OctetString):
    """Custom type atmIlmiCommStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtmIlmiCommStr_Type.__name__ = "OctetString"
_AtmIlmiCommStr_Object = MibTableColumn
atmIlmiCommStr = _AtmIlmiCommStr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 6, 2, 1, 2),
    _AtmIlmiCommStr_Type()
)
atmIlmiCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIlmiCommStr.setStatus("mandatory")
_AtmIlmiCommStrStatus_Type = RowStatus
_AtmIlmiCommStrStatus_Object = MibTableColumn
atmIlmiCommStrStatus = _AtmIlmiCommStrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 6, 2, 1, 3),
    _AtmIlmiCommStrStatus_Type()
)
atmIlmiCommStrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIlmiCommStrStatus.setStatus("mandatory")
_AtmInstGrp_ObjectIdentity = ObjectIdentity
atmInstGrp = _AtmInstGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9)
)
_AccAtmIfTable_Object = MibTable
accAtmIfTable = _AccAtmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 1)
)
if mibBuilder.loadTexts:
    accAtmIfTable.setStatus("mandatory")
_AccAtmIfEntry_Object = MibTableRow
accAtmIfEntry = _AccAtmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 1, 1)
)
accAtmIfEntry.setIndexNames(
    (0, "ACC-ATM", "accAtmIfIndex"),
)
if mibBuilder.loadTexts:
    accAtmIfEntry.setStatus("mandatory")
_AccAtmIfIndex_Type = IfIndex
_AccAtmIfIndex_Object = MibTableColumn
accAtmIfIndex = _AccAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 1, 1, 1),
    _AccAtmIfIndex_Type()
)
accAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtmIfIndex.setStatus("mandatory")
_AccAtmVplTable_Object = MibTable
accAtmVplTable = _AccAtmVplTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 2)
)
if mibBuilder.loadTexts:
    accAtmVplTable.setStatus("mandatory")
_AccAtmVplEntry_Object = MibTableRow
accAtmVplEntry = _AccAtmVplEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 2, 1)
)
accAtmVplEntry.setIndexNames(
    (0, "ACC-ATM", "accAtmVplIndex"),
    (0, "ACC-ATM", "accAtmVplVpi"),
)
if mibBuilder.loadTexts:
    accAtmVplEntry.setStatus("mandatory")
_AccAtmVplIndex_Type = IfIndex
_AccAtmVplIndex_Object = MibTableColumn
accAtmVplIndex = _AccAtmVplIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 2, 1, 1),
    _AccAtmVplIndex_Type()
)
accAtmVplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtmVplIndex.setStatus("mandatory")


class _AccAtmVplVpi_Type(Integer32):
    """Custom type accAtmVplVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AccAtmVplVpi_Type.__name__ = "Integer32"
_AccAtmVplVpi_Object = MibTableColumn
accAtmVplVpi = _AccAtmVplVpi_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 2, 1, 2),
    _AccAtmVplVpi_Type()
)
accAtmVplVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtmVplVpi.setStatus("mandatory")
_AccAtmVclTable_Object = MibTable
accAtmVclTable = _AccAtmVclTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 3)
)
if mibBuilder.loadTexts:
    accAtmVclTable.setStatus("mandatory")
_AccAtmVclEntry_Object = MibTableRow
accAtmVclEntry = _AccAtmVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 3, 1)
)
accAtmVclEntry.setIndexNames(
    (0, "ACC-ATM", "accAtmVclIndex"),
    (0, "ACC-ATM", "accAtmVclVpi"),
    (0, "ACC-ATM", "accAtmVclVci"),
)
if mibBuilder.loadTexts:
    accAtmVclEntry.setStatus("mandatory")
_AccAtmVclIndex_Type = IfIndex
_AccAtmVclIndex_Object = MibTableColumn
accAtmVclIndex = _AccAtmVclIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 3, 1, 1),
    _AccAtmVclIndex_Type()
)
accAtmVclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtmVclIndex.setStatus("mandatory")


class _AccAtmVclVpi_Type(Integer32):
    """Custom type accAtmVclVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AccAtmVclVpi_Type.__name__ = "Integer32"
_AccAtmVclVpi_Object = MibTableColumn
accAtmVclVpi = _AccAtmVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 3, 1, 2),
    _AccAtmVclVpi_Type()
)
accAtmVclVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtmVclVpi.setStatus("mandatory")


class _AccAtmVclVci_Type(Integer32):
    """Custom type accAtmVclVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccAtmVclVci_Type.__name__ = "Integer32"
_AccAtmVclVci_Object = MibTableColumn
accAtmVclVci = _AccAtmVclVci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 3, 1, 3),
    _AccAtmVclVci_Type()
)
accAtmVclVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtmVclVci.setStatus("mandatory")
_AccAtmClockTable_Object = MibTable
accAtmClockTable = _AccAtmClockTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 4)
)
if mibBuilder.loadTexts:
    accAtmClockTable.setStatus("mandatory")
_AccAtmClockEntry_Object = MibTableRow
accAtmClockEntry = _AccAtmClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 4, 1)
)
accAtmClockEntry.setIndexNames(
    (0, "ACC-ATM", "accAtmClockIndex"),
    (0, "ACC-ATM", "accAtmClockType"),
)
if mibBuilder.loadTexts:
    accAtmClockEntry.setStatus("mandatory")
_AccAtmClockIndex_Type = IfIndex
_AccAtmClockIndex_Object = MibTableColumn
accAtmClockIndex = _AccAtmClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 4, 1, 1),
    _AccAtmClockIndex_Type()
)
accAtmClockIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtmClockIndex.setStatus("mandatory")


class _AccAtmClockType_Type(Integer32):
    """Custom type accAtmClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_AccAtmClockType_Type.__name__ = "Integer32"
_AccAtmClockType_Object = MibTableColumn
accAtmClockType = _AccAtmClockType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 77, 9, 4, 1, 2),
    _AccAtmClockType_Type()
)
accAtmClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtmClockType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-ATM",
    **{"accAtm": accAtm,
       "atmStatsGrp": atmStatsGrp,
       "atmStatsAtmLayerTable": atmStatsAtmLayerTable,
       "atmStatsAtmLayerEntry": atmStatsAtmLayerEntry,
       "atmStatsAtmLayerRxCells": atmStatsAtmLayerRxCells,
       "atmStatsAtmLayerTxCells": atmStatsAtmLayerTxCells,
       "atmStatsAtmLayerDiscCells": atmStatsAtmLayerDiscCells,
       "atmStatsAtmLayerDropCells": atmStatsAtmLayerDropCells,
       "atmStatsCallTable": atmStatsCallTable,
       "atmStatsCallEntry": atmStatsCallEntry,
       "atmStatsCallOrigCalls": atmStatsCallOrigCalls,
       "atmStatsCallOffCalls": atmStatsCallOffCalls,
       "atmStatsCallAccCalls": atmStatsCallAccCalls,
       "atmStatsCallCompCalls": atmStatsCallCompCalls,
       "atmStatsCallClrCalls": atmStatsCallClrCalls,
       "atmOamGrp": atmOamGrp,
       "atmOamConfTable": atmOamConfTable,
       "atmOamConfEntry": atmOamConfEntry,
       "atmOamIndex": atmOamIndex,
       "atmOamPhyFlowType": atmOamPhyFlowType,
       "atmOamFlowState": atmOamFlowState,
       "atmOamVpcTable": atmOamVpcTable,
       "atmOamVpcEntry": atmOamVpcEntry,
       "atmOamVpcIndex": atmOamVpcIndex,
       "atmOamVpcVpi": atmOamVpcVpi,
       "atmOamVpcFlowType": atmOamVpcFlowType,
       "atmOamVpcRowStatus": atmOamVpcRowStatus,
       "atmOamVccTable": atmOamVccTable,
       "atmOamVccEntry": atmOamVccEntry,
       "atmOamVccIndex": atmOamVccIndex,
       "atmOamVccVpi": atmOamVccVpi,
       "atmOamVccVci": atmOamVccVci,
       "atmOamVccFlowType": atmOamVccFlowType,
       "atmOamVccRowStatus": atmOamVccRowStatus,
       "atmIlmiGrp": atmIlmiGrp,
       "atmIlmiConfTable": atmIlmiConfTable,
       "atmIlmiConfEntry": atmIlmiConfEntry,
       "atmIlmiImeType": atmIlmiImeType,
       "atmIlmiUniType": atmIlmiUniType,
       "atmIlmiCommStrTable": atmIlmiCommStrTable,
       "atmIlmiCommStrEntry": atmIlmiCommStrEntry,
       "atmIlmiCommStrIndex": atmIlmiCommStrIndex,
       "atmIlmiCommStr": atmIlmiCommStr,
       "atmIlmiCommStrStatus": atmIlmiCommStrStatus,
       "atmInstGrp": atmInstGrp,
       "accAtmIfTable": accAtmIfTable,
       "accAtmIfEntry": accAtmIfEntry,
       "accAtmIfIndex": accAtmIfIndex,
       "accAtmVplTable": accAtmVplTable,
       "accAtmVplEntry": accAtmVplEntry,
       "accAtmVplIndex": accAtmVplIndex,
       "accAtmVplVpi": accAtmVplVpi,
       "accAtmVclTable": accAtmVclTable,
       "accAtmVclEntry": accAtmVclEntry,
       "accAtmVclIndex": accAtmVclIndex,
       "accAtmVclVpi": accAtmVclVpi,
       "accAtmVclVci": accAtmVclVci,
       "accAtmClockTable": accAtmClockTable,
       "accAtmClockEntry": accAtmClockEntry,
       "accAtmClockIndex": accAtmClockIndex,
       "accAtmClockType": accAtmClockType}
)

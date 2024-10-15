# SNMP MIB module (Fore-DSX1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-DSX1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:55 2024
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

(asx,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asx")

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

foreDsx1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx1ForeConfGroup_ObjectIdentity = ObjectIdentity
dsx1ForeConfGroup = _Dsx1ForeConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1)
)
_Dsx1ForeConfTable_Object = MibTable
dsx1ForeConfTable = _Dsx1ForeConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    dsx1ForeConfTable.setStatus("current")
_Dsx1ForeConfEntry_Object = MibTableRow
dsx1ForeConfEntry = _Dsx1ForeConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1)
)
dsx1ForeConfEntry.setIndexNames(
    (0, "Fore-DSX1-MIB", "dsx1ForeLineIndex"),
)
if mibBuilder.loadTexts:
    dsx1ForeConfEntry.setStatus("current")


class _Dsx1ForeLineIndex_Type(Integer32):
    """Custom type dsx1ForeLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dsx1ForeLineIndex_Type.__name__ = "Integer32"
_Dsx1ForeLineIndex_Object = MibTableColumn
dsx1ForeLineIndex = _Dsx1ForeLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 1),
    _Dsx1ForeLineIndex_Type()
)
dsx1ForeLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeLineIndex.setStatus("current")


class _Dsx1ForeReceiveCode_Type(Integer32):
    """Custom type dsx1ForeReceiveCode based on Integer32"""
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
        *(("dsx1Receive3in24Pattern", 7),
          ("dsx1Receive511Pattern", 6),
          ("dsx1ReceiveLineCode", 2),
          ("dsx1ReceiveNoCode", 1),
          ("dsx1ReceiveOtherTestPattern", 8),
          ("dsx1ReceivePayloadCode", 3),
          ("dsx1ReceiveQRS", 5),
          ("dsx1ReceiveResetCode", 4))
    )


_Dsx1ForeReceiveCode_Type.__name__ = "Integer32"
_Dsx1ForeReceiveCode_Object = MibTableColumn
dsx1ForeReceiveCode = _Dsx1ForeReceiveCode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 2),
    _Dsx1ForeReceiveCode_Type()
)
dsx1ForeReceiveCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeReceiveCode.setStatus("current")


class _Dsx1ForeLineLength_Type(Integer32):
    """Custom type dsx1ForeLineLength based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dsx1Line120-160", 4),
          ("dsx1Line160-200", 5),
          ("dsx1Line40-80", 2),
          ("dsx1Line80-120", 3),
          ("dsx1LineE1Coax", 6),
          ("dsx1LineLt40", 1),
          ("dsx1LineTwistedPair", 7))
    )


_Dsx1ForeLineLength_Type.__name__ = "Integer32"
_Dsx1ForeLineLength_Object = MibTableColumn
dsx1ForeLineLength = _Dsx1ForeLineLength_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 3),
    _Dsx1ForeLineLength_Type()
)
dsx1ForeLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ForeLineLength.setStatus("current")


class _Dsx1ForeFdlConfiguration_Type(Integer32):
    """Custom type dsx1ForeFdlConfiguration based on Integer32"""
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


_Dsx1ForeFdlConfiguration_Type.__name__ = "Integer32"
_Dsx1ForeFdlConfiguration_Object = MibTableColumn
dsx1ForeFdlConfiguration = _Dsx1ForeFdlConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 4),
    _Dsx1ForeFdlConfiguration_Type()
)
dsx1ForeFdlConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ForeFdlConfiguration.setStatus("current")


class _Dsx1ForeLineImpedance_Type(Integer32):
    """Custom type dsx1ForeLineImpedance based on Integer32"""
    defaultValue = 75


_Dsx1ForeLineImpedance_Object = MibTableColumn
dsx1ForeLineImpedance = _Dsx1ForeLineImpedance_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 5),
    _Dsx1ForeLineImpedance_Type()
)
dsx1ForeLineImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ForeLineImpedance.setStatus("deprecated")


class _Dsx1ForeFdlPerfConf_Type(Integer32):
    """Custom type dsx1ForeFdlPerfConf based on Integer32"""
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


_Dsx1ForeFdlPerfConf_Type.__name__ = "Integer32"
_Dsx1ForeFdlPerfConf_Object = MibTableColumn
dsx1ForeFdlPerfConf = _Dsx1ForeFdlPerfConf_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 6),
    _Dsx1ForeFdlPerfConf_Type()
)
dsx1ForeFdlPerfConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ForeFdlPerfConf.setStatus("current")


class _Dsx1ForeFdlBomConf_Type(Integer32):
    """Custom type dsx1ForeFdlBomConf based on Integer32"""
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


_Dsx1ForeFdlBomConf_Type.__name__ = "Integer32"
_Dsx1ForeFdlBomConf_Object = MibTableColumn
dsx1ForeFdlBomConf = _Dsx1ForeFdlBomConf_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 7),
    _Dsx1ForeFdlBomConf_Type()
)
dsx1ForeFdlBomConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ForeFdlBomConf.setStatus("current")


class _Dsx1ForeUpStreamAIS_Type(Integer32):
    """Custom type dsx1ForeUpStreamAIS based on Integer32"""
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


_Dsx1ForeUpStreamAIS_Type.__name__ = "Integer32"
_Dsx1ForeUpStreamAIS_Object = MibTableColumn
dsx1ForeUpStreamAIS = _Dsx1ForeUpStreamAIS_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 8),
    _Dsx1ForeUpStreamAIS_Type()
)
dsx1ForeUpStreamAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ForeUpStreamAIS.setStatus("current")
_Dsx1ForePortModel_Type = Integer32
_Dsx1ForePortModel_Object = MibTableColumn
dsx1ForePortModel = _Dsx1ForePortModel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 9),
    _Dsx1ForePortModel_Type()
)
dsx1ForePortModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForePortModel.setStatus("current")


class _Dsx1ForeAdminStatus_Type(Integer32):
    """Custom type dsx1ForeAdminStatus based on Integer32"""
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
          ("testing", 3),
          ("up", 1))
    )


_Dsx1ForeAdminStatus_Type.__name__ = "Integer32"
_Dsx1ForeAdminStatus_Object = MibTableColumn
dsx1ForeAdminStatus = _Dsx1ForeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 1, 1, 1, 10),
    _Dsx1ForeAdminStatus_Type()
)
dsx1ForeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ForeAdminStatus.setStatus("current")
_Dsx1ForeStatsGroup_ObjectIdentity = ObjectIdentity
dsx1ForeStatsGroup = _Dsx1ForeStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2)
)
_Dsx1ForeFramingTable_Object = MibTable
dsx1ForeFramingTable = _Dsx1ForeFramingTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    dsx1ForeFramingTable.setStatus("current")
_Dsx1ForeFramingEntry_Object = MibTableRow
dsx1ForeFramingEntry = _Dsx1ForeFramingEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1)
)
dsx1ForeFramingEntry.setIndexNames(
    (0, "Fore-DSX1-MIB", "dsx1ForeFramingIndex"),
)
if mibBuilder.loadTexts:
    dsx1ForeFramingEntry.setStatus("current")
_Dsx1ForeFramingIndex_Type = Integer32
_Dsx1ForeFramingIndex_Object = MibTableColumn
dsx1ForeFramingIndex = _Dsx1ForeFramingIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 1),
    _Dsx1ForeFramingIndex_Type()
)
dsx1ForeFramingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFramingIndex.setStatus("current")
_Dsx1ForeFramingLOSs_Type = Counter32
_Dsx1ForeFramingLOSs_Object = MibTableColumn
dsx1ForeFramingLOSs = _Dsx1ForeFramingLOSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 2),
    _Dsx1ForeFramingLOSs_Type()
)
dsx1ForeFramingLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFramingLOSs.setStatus("current")
_Dsx1ForeFramingLCVs_Type = Counter32
_Dsx1ForeFramingLCVs_Object = MibTableColumn
dsx1ForeFramingLCVs = _Dsx1ForeFramingLCVs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 3),
    _Dsx1ForeFramingLCVs_Type()
)
dsx1ForeFramingLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFramingLCVs.setStatus("current")
_Dsx1ForeFramingFERRs_Type = Counter32
_Dsx1ForeFramingFERRs_Object = MibTableColumn
dsx1ForeFramingFERRs = _Dsx1ForeFramingFERRs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 4),
    _Dsx1ForeFramingFERRs_Type()
)
dsx1ForeFramingFERRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFramingFERRs.setStatus("current")
_Dsx1ForeFramingOOFs_Type = Counter32
_Dsx1ForeFramingOOFs_Object = MibTableColumn
dsx1ForeFramingOOFs = _Dsx1ForeFramingOOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 5),
    _Dsx1ForeFramingOOFs_Type()
)
dsx1ForeFramingOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFramingOOFs.setStatus("current")
_Dsx1ForeFramingAISs_Type = Counter32
_Dsx1ForeFramingAISs_Object = MibTableColumn
dsx1ForeFramingAISs = _Dsx1ForeFramingAISs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 6),
    _Dsx1ForeFramingAISs_Type()
)
dsx1ForeFramingAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFramingAISs.setStatus("current")
_Dsx1ForeFramingB8ZSPatterns_Type = Counter32
_Dsx1ForeFramingB8ZSPatterns_Object = MibTableColumn
dsx1ForeFramingB8ZSPatterns = _Dsx1ForeFramingB8ZSPatterns_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 7),
    _Dsx1ForeFramingB8ZSPatterns_Type()
)
dsx1ForeFramingB8ZSPatterns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFramingB8ZSPatterns.setStatus("current")
_Dsx1ForeFraming8Zeros_Type = Counter32
_Dsx1ForeFraming8Zeros_Object = MibTableColumn
dsx1ForeFraming8Zeros = _Dsx1ForeFraming8Zeros_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 8),
    _Dsx1ForeFraming8Zeros_Type()
)
dsx1ForeFraming8Zeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFraming8Zeros.setStatus("current")
_Dsx1ForeFraming16Zeros_Type = Counter32
_Dsx1ForeFraming16Zeros_Object = MibTableColumn
dsx1ForeFraming16Zeros = _Dsx1ForeFraming16Zeros_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 9),
    _Dsx1ForeFraming16Zeros_Type()
)
dsx1ForeFraming16Zeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFraming16Zeros.setStatus("current")
_Dsx1ForeFramingYellowAlarms_Type = Counter32
_Dsx1ForeFramingYellowAlarms_Object = MibTableColumn
dsx1ForeFramingYellowAlarms = _Dsx1ForeFramingYellowAlarms_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 10),
    _Dsx1ForeFramingYellowAlarms_Type()
)
dsx1ForeFramingYellowAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFramingYellowAlarms.setStatus("current")
_Dsx1ForeFramingRedAlarms_Type = Counter32
_Dsx1ForeFramingRedAlarms_Object = MibTableColumn
dsx1ForeFramingRedAlarms = _Dsx1ForeFramingRedAlarms_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 11),
    _Dsx1ForeFramingRedAlarms_Type()
)
dsx1ForeFramingRedAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFramingRedAlarms.setStatus("current")
_Dsx1ForeFramingBEEs_Type = Counter32
_Dsx1ForeFramingBEEs_Object = MibTableColumn
dsx1ForeFramingBEEs = _Dsx1ForeFramingBEEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 1, 1, 12),
    _Dsx1ForeFramingBEEs_Type()
)
dsx1ForeFramingBEEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeFramingBEEs.setStatus("current")
_Dsx1ForeAtmTable_Object = MibTable
dsx1ForeAtmTable = _Dsx1ForeAtmTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 2)
)
if mibBuilder.loadTexts:
    dsx1ForeAtmTable.setStatus("current")
_Dsx1ForeAtmEntry_Object = MibTableRow
dsx1ForeAtmEntry = _Dsx1ForeAtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 2, 1)
)
dsx1ForeAtmEntry.setIndexNames(
    (0, "Fore-DSX1-MIB", "dsx1ForeAtmIndex"),
)
if mibBuilder.loadTexts:
    dsx1ForeAtmEntry.setStatus("current")
_Dsx1ForeAtmIndex_Type = Integer32
_Dsx1ForeAtmIndex_Object = MibTableColumn
dsx1ForeAtmIndex = _Dsx1ForeAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 2, 1, 1),
    _Dsx1ForeAtmIndex_Type()
)
dsx1ForeAtmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeAtmIndex.setStatus("current")
_Dsx1ForeAtmRxCells_Type = Counter32
_Dsx1ForeAtmRxCells_Object = MibTableColumn
dsx1ForeAtmRxCells = _Dsx1ForeAtmRxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 2, 1, 2),
    _Dsx1ForeAtmRxCells_Type()
)
dsx1ForeAtmRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeAtmRxCells.setStatus("current")
_Dsx1ForeAtmTxCells_Type = Counter32
_Dsx1ForeAtmTxCells_Object = MibTableColumn
dsx1ForeAtmTxCells = _Dsx1ForeAtmTxCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 10, 2, 2, 1, 3),
    _Dsx1ForeAtmTxCells_Type()
)
dsx1ForeAtmTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ForeAtmTxCells.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-DSX1-MIB",
    **{"foreDsx1": foreDsx1,
       "dsx1ForeConfGroup": dsx1ForeConfGroup,
       "dsx1ForeConfTable": dsx1ForeConfTable,
       "dsx1ForeConfEntry": dsx1ForeConfEntry,
       "dsx1ForeLineIndex": dsx1ForeLineIndex,
       "dsx1ForeReceiveCode": dsx1ForeReceiveCode,
       "dsx1ForeLineLength": dsx1ForeLineLength,
       "dsx1ForeFdlConfiguration": dsx1ForeFdlConfiguration,
       "dsx1ForeLineImpedance": dsx1ForeLineImpedance,
       "dsx1ForeFdlPerfConf": dsx1ForeFdlPerfConf,
       "dsx1ForeFdlBomConf": dsx1ForeFdlBomConf,
       "dsx1ForeUpStreamAIS": dsx1ForeUpStreamAIS,
       "dsx1ForePortModel": dsx1ForePortModel,
       "dsx1ForeAdminStatus": dsx1ForeAdminStatus,
       "dsx1ForeStatsGroup": dsx1ForeStatsGroup,
       "dsx1ForeFramingTable": dsx1ForeFramingTable,
       "dsx1ForeFramingEntry": dsx1ForeFramingEntry,
       "dsx1ForeFramingIndex": dsx1ForeFramingIndex,
       "dsx1ForeFramingLOSs": dsx1ForeFramingLOSs,
       "dsx1ForeFramingLCVs": dsx1ForeFramingLCVs,
       "dsx1ForeFramingFERRs": dsx1ForeFramingFERRs,
       "dsx1ForeFramingOOFs": dsx1ForeFramingOOFs,
       "dsx1ForeFramingAISs": dsx1ForeFramingAISs,
       "dsx1ForeFramingB8ZSPatterns": dsx1ForeFramingB8ZSPatterns,
       "dsx1ForeFraming8Zeros": dsx1ForeFraming8Zeros,
       "dsx1ForeFraming16Zeros": dsx1ForeFraming16Zeros,
       "dsx1ForeFramingYellowAlarms": dsx1ForeFramingYellowAlarms,
       "dsx1ForeFramingRedAlarms": dsx1ForeFramingRedAlarms,
       "dsx1ForeFramingBEEs": dsx1ForeFramingBEEs,
       "dsx1ForeAtmTable": dsx1ForeAtmTable,
       "dsx1ForeAtmEntry": dsx1ForeAtmEntry,
       "dsx1ForeAtmIndex": dsx1ForeAtmIndex,
       "dsx1ForeAtmRxCells": dsx1ForeAtmRxCells,
       "dsx1ForeAtmTxCells": dsx1ForeAtmTxCells}
)

# SNMP MIB module (FRAMEVISIONFPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FRAMEVISIONFPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:20 2024
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



class FribDLCI(Integer32):
    """Custom type FribDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483646),
    )





class Counter32(Counter32):
    """Custom type Counter32 based on Counter32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Framevisionfping_ObjectIdentity = ObjectIdentity
framevisionfping = _Framevisionfping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 100, 2)
)
_FpingMib_ObjectIdentity = ObjectIdentity
fpingMib = _FpingMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 1)
)


class _FpingMibVersion_Type(Integer32):
    """Custom type fpingMibVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_FpingMibVersion_Type.__name__ = "Integer32"
_FpingMibVersion_Object = MibScalar
fpingMibVersion = _FpingMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 1, 1),
    _FpingMibVersion_Type()
)
fpingMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingMibVersion.setStatus("mandatory")
_FpingMibLastChange_Type = TimeTicks
_FpingMibLastChange_Object = MibScalar
fpingMibLastChange = _FpingMibLastChange_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 1, 2),
    _FpingMibLastChange_Type()
)
fpingMibLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingMibLastChange.setStatus("mandatory")
_FpingAuto_ObjectIdentity = ObjectIdentity
fpingAuto = _FpingAuto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2)
)
_FpingAutoCfgTable_Object = MibTable
fpingAutoCfgTable = _FpingAutoCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fpingAutoCfgTable.setStatus("mandatory")
_FpingAutoCfgEntry_Object = MibTableRow
fpingAutoCfgEntry = _FpingAutoCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1)
)
fpingAutoCfgEntry.setIndexNames(
    (0, "FRAMEVISIONFPING-MIB", "fpingAutoCfgIfIndex"),
)
if mibBuilder.loadTexts:
    fpingAutoCfgEntry.setStatus("mandatory")
_FpingAutoCfgIfIndex_Type = Integer32
_FpingAutoCfgIfIndex_Object = MibTableColumn
fpingAutoCfgIfIndex = _FpingAutoCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1, 1),
    _FpingAutoCfgIfIndex_Type()
)
fpingAutoCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoCfgIfIndex.setStatus("mandatory")
_FpingAutoCfgLastChange_Type = TimeTicks
_FpingAutoCfgLastChange_Object = MibTableColumn
fpingAutoCfgLastChange = _FpingAutoCfgLastChange_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1, 2),
    _FpingAutoCfgLastChange_Type()
)
fpingAutoCfgLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoCfgLastChange.setStatus("mandatory")
_FpingAutoCfgGen_Type = Integer32
_FpingAutoCfgGen_Object = MibTableColumn
fpingAutoCfgGen = _FpingAutoCfgGen_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1, 3),
    _FpingAutoCfgGen_Type()
)
fpingAutoCfgGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpingAutoCfgGen.setStatus("mandatory")
_FpingAutoCfgThresh_Type = Integer32
_FpingAutoCfgThresh_Object = MibTableColumn
fpingAutoCfgThresh = _FpingAutoCfgThresh_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1, 4),
    _FpingAutoCfgThresh_Type()
)
fpingAutoCfgThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpingAutoCfgThresh.setStatus("mandatory")


class _FpingAutoCfgReset_Type(Integer32):
    """Custom type fpingAutoCfgReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fpingResetIdle", 1),
          ("fpingResetStart", 2))
    )


_FpingAutoCfgReset_Type.__name__ = "Integer32"
_FpingAutoCfgReset_Object = MibTableColumn
fpingAutoCfgReset = _FpingAutoCfgReset_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 1, 1, 5),
    _FpingAutoCfgReset_Type()
)
fpingAutoCfgReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpingAutoCfgReset.setStatus("mandatory")
_FpingAutoDuration_Type = TimeTicks
_FpingAutoDuration_Object = MibScalar
fpingAutoDuration = _FpingAutoDuration_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 2),
    _FpingAutoDuration_Type()
)
fpingAutoDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoDuration.setStatus("mandatory")


class _FpingAutoClearData_Type(Integer32):
    """Custom type fpingAutoClearData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearDataIdle", 1),
          ("clearDataStart", 2))
    )


_FpingAutoClearData_Type.__name__ = "Integer32"
_FpingAutoClearData_Object = MibScalar
fpingAutoClearData = _FpingAutoClearData_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 3),
    _FpingAutoClearData_Type()
)
fpingAutoClearData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpingAutoClearData.setStatus("mandatory")
_FpingAutoTable_Object = MibTable
fpingAutoTable = _FpingAutoTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4)
)
if mibBuilder.loadTexts:
    fpingAutoTable.setStatus("mandatory")
_FpingAutoEntry_Object = MibTableRow
fpingAutoEntry = _FpingAutoEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1)
)
fpingAutoEntry.setIndexNames(
    (0, "FRAMEVISIONFPING-MIB", "fpingAutoIfIndex"),
    (0, "FRAMEVISIONFPING-MIB", "fpingAutoDLCI"),
)
if mibBuilder.loadTexts:
    fpingAutoEntry.setStatus("mandatory")
_FpingAutoIfIndex_Type = Integer32
_FpingAutoIfIndex_Object = MibTableColumn
fpingAutoIfIndex = _FpingAutoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 1),
    _FpingAutoIfIndex_Type()
)
fpingAutoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoIfIndex.setStatus("mandatory")
_FpingAutoDLCI_Type = FribDLCI
_FpingAutoDLCI_Object = MibTableColumn
fpingAutoDLCI = _FpingAutoDLCI_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 2),
    _FpingAutoDLCI_Type()
)
fpingAutoDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoDLCI.setStatus("mandatory")
_FpingAutoDelayMin_Type = Integer32
_FpingAutoDelayMin_Object = MibTableColumn
fpingAutoDelayMin = _FpingAutoDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 3),
    _FpingAutoDelayMin_Type()
)
fpingAutoDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoDelayMin.setStatus("mandatory")
_FpingAutoDelayMax_Type = Integer32
_FpingAutoDelayMax_Object = MibTableColumn
fpingAutoDelayMax = _FpingAutoDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 4),
    _FpingAutoDelayMax_Type()
)
fpingAutoDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoDelayMax.setStatus("mandatory")
_FpingAutoDelayAvg_Type = Integer32
_FpingAutoDelayAvg_Object = MibTableColumn
fpingAutoDelayAvg = _FpingAutoDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 5),
    _FpingAutoDelayAvg_Type()
)
fpingAutoDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoDelayAvg.setStatus("mandatory")
_FpingAutoLost_Type = Counter32
_FpingAutoLost_Object = MibTableColumn
fpingAutoLost = _FpingAutoLost_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 6),
    _FpingAutoLost_Type()
)
fpingAutoLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoLost.setStatus("mandatory")
_FpingAutoTotal_Type = Counter32
_FpingAutoTotal_Object = MibTableColumn
fpingAutoTotal = _FpingAutoTotal_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 7),
    _FpingAutoTotal_Type()
)
fpingAutoTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoTotal.setStatus("mandatory")
_FpingAutoThreshExceeded_Type = Counter32
_FpingAutoThreshExceeded_Object = MibTableColumn
fpingAutoThreshExceeded = _FpingAutoThreshExceeded_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 8),
    _FpingAutoThreshExceeded_Type()
)
fpingAutoThreshExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoThreshExceeded.setStatus("mandatory")
_FpingAutoRmtDLCI_Type = FribDLCI
_FpingAutoRmtDLCI_Object = MibTableColumn
fpingAutoRmtDLCI = _FpingAutoRmtDLCI_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 9),
    _FpingAutoRmtDLCI_Type()
)
fpingAutoRmtDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoRmtDLCI.setStatus("mandatory")
_FpingAutoRmtIpaddr_Type = IpAddress
_FpingAutoRmtIpaddr_Object = MibTableColumn
fpingAutoRmtIpaddr = _FpingAutoRmtIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 10),
    _FpingAutoRmtIpaddr_Type()
)
fpingAutoRmtIpaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoRmtIpaddr.setStatus("mandatory")
_FpingAutoTotalPktsLocalTx_Type = Counter32
_FpingAutoTotalPktsLocalTx_Object = MibTableColumn
fpingAutoTotalPktsLocalTx = _FpingAutoTotalPktsLocalTx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 11),
    _FpingAutoTotalPktsLocalTx_Type()
)
fpingAutoTotalPktsLocalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoTotalPktsLocalTx.setStatus("mandatory")
_FpingAutoTotalPktsLocalRx_Type = Counter32
_FpingAutoTotalPktsLocalRx_Object = MibTableColumn
fpingAutoTotalPktsLocalRx = _FpingAutoTotalPktsLocalRx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 12),
    _FpingAutoTotalPktsLocalRx_Type()
)
fpingAutoTotalPktsLocalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoTotalPktsLocalRx.setStatus("mandatory")
_FpingAutoTotalPktsRmtTx_Type = Counter32
_FpingAutoTotalPktsRmtTx_Object = MibTableColumn
fpingAutoTotalPktsRmtTx = _FpingAutoTotalPktsRmtTx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 13),
    _FpingAutoTotalPktsRmtTx_Type()
)
fpingAutoTotalPktsRmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoTotalPktsRmtTx.setStatus("mandatory")
_FpingAutoTotalPktsRmtRx_Type = Counter32
_FpingAutoTotalPktsRmtRx_Object = MibTableColumn
fpingAutoTotalPktsRmtRx = _FpingAutoTotalPktsRmtRx_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 14),
    _FpingAutoTotalPktsRmtRx_Type()
)
fpingAutoTotalPktsRmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoTotalPktsRmtRx.setStatus("mandatory")


class _FpingAutoStatus_Type(Integer32):
    """Custom type fpingAutoStatus based on Integer32"""
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
        *(("fpingDisabled", 1),
          ("lastFpingFailed", 3),
          ("lastFpingSucceeded", 2),
          ("notMonitoringFping", 4),
          ("waitingToStartFping", 5))
    )


_FpingAutoStatus_Type.__name__ = "Integer32"
_FpingAutoStatus_Object = MibTableColumn
fpingAutoStatus = _FpingAutoStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 15),
    _FpingAutoStatus_Type()
)
fpingAutoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoStatus.setStatus("mandatory")
_FpingAutoFailedEvents_Type = Counter32
_FpingAutoFailedEvents_Object = MibTableColumn
fpingAutoFailedEvents = _FpingAutoFailedEvents_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 2, 4, 1, 16),
    _FpingAutoFailedEvents_Type()
)
fpingAutoFailedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingAutoFailedEvents.setStatus("mandatory")
_FpingManual_ObjectIdentity = ObjectIdentity
fpingManual = _FpingManual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3)
)
_FpingManualTable_Object = MibTable
fpingManualTable = _FpingManualTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fpingManualTable.setStatus("mandatory")
_FpingManualEntry_Object = MibTableRow
fpingManualEntry = _FpingManualEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1)
)
fpingManualEntry.setIndexNames(
    (0, "FRAMEVISIONFPING-MIB", "fpingManualIfIndex"),
    (0, "FRAMEVISIONFPING-MIB", "fpingManualDLCI"),
)
if mibBuilder.loadTexts:
    fpingManualEntry.setStatus("mandatory")
_FpingManualIfIndex_Type = Integer32
_FpingManualIfIndex_Object = MibTableColumn
fpingManualIfIndex = _FpingManualIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 1),
    _FpingManualIfIndex_Type()
)
fpingManualIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingManualIfIndex.setStatus("mandatory")
_FpingManualDLCI_Type = FribDLCI
_FpingManualDLCI_Object = MibTableColumn
fpingManualDLCI = _FpingManualDLCI_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 2),
    _FpingManualDLCI_Type()
)
fpingManualDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpingManualDLCI.setStatus("mandatory")


class _FpingManualAction_Type(Integer32):
    """Custom type fpingManualAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fpingManualActionStart", 1),
          ("fpingManualActionStop", 2))
    )


_FpingManualAction_Type.__name__ = "Integer32"
_FpingManualAction_Object = MibTableColumn
fpingManualAction = _FpingManualAction_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 3),
    _FpingManualAction_Type()
)
fpingManualAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpingManualAction.setStatus("mandatory")


class _FpingManualState_Type(Integer32):
    """Custom type fpingManualState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fpingManualStarteRunning", 3),
          ("fpingManualStateIdle", 1),
          ("fpingManualStateOtherStart", 2))
    )


_FpingManualState_Type.__name__ = "Integer32"
_FpingManualState_Object = MibTableColumn
fpingManualState = _FpingManualState_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 4),
    _FpingManualState_Type()
)
fpingManualState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingManualState.setStatus("mandatory")
_FpingManualFreq_Type = Integer32
_FpingManualFreq_Object = MibTableColumn
fpingManualFreq = _FpingManualFreq_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 5),
    _FpingManualFreq_Type()
)
fpingManualFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpingManualFreq.setStatus("mandatory")
_FpingManualLen_Type = Integer32
_FpingManualLen_Object = MibTableColumn
fpingManualLen = _FpingManualLen_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 6),
    _FpingManualLen_Type()
)
fpingManualLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpingManualLen.setStatus("mandatory")
_FpingManualCur_Type = Integer32
_FpingManualCur_Object = MibTableColumn
fpingManualCur = _FpingManualCur_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 7),
    _FpingManualCur_Type()
)
fpingManualCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingManualCur.setStatus("mandatory")
_FpingManualMin_Type = Integer32
_FpingManualMin_Object = MibTableColumn
fpingManualMin = _FpingManualMin_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 8),
    _FpingManualMin_Type()
)
fpingManualMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingManualMin.setStatus("mandatory")
_FpingManualMax_Type = Integer32
_FpingManualMax_Object = MibTableColumn
fpingManualMax = _FpingManualMax_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 9),
    _FpingManualMax_Type()
)
fpingManualMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingManualMax.setStatus("mandatory")
_FpingManualAvg_Type = Integer32
_FpingManualAvg_Object = MibTableColumn
fpingManualAvg = _FpingManualAvg_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 10),
    _FpingManualAvg_Type()
)
fpingManualAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingManualAvg.setStatus("mandatory")
_FpingManualLost_Type = Integer32
_FpingManualLost_Object = MibTableColumn
fpingManualLost = _FpingManualLost_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 11),
    _FpingManualLost_Type()
)
fpingManualLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingManualLost.setStatus("mandatory")
_FpingManualTotal_Type = Integer32
_FpingManualTotal_Object = MibTableColumn
fpingManualTotal = _FpingManualTotal_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 12),
    _FpingManualTotal_Type()
)
fpingManualTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingManualTotal.setStatus("mandatory")
_FpingManualRmtDLCI_Type = FribDLCI
_FpingManualRmtDLCI_Object = MibTableColumn
fpingManualRmtDLCI = _FpingManualRmtDLCI_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 13),
    _FpingManualRmtDLCI_Type()
)
fpingManualRmtDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingManualRmtDLCI.setStatus("mandatory")
_FpingManualRmtIpaddr_Type = IpAddress
_FpingManualRmtIpaddr_Object = MibTableColumn
fpingManualRmtIpaddr = _FpingManualRmtIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 181, 100, 2, 3, 1, 1, 14),
    _FpingManualRmtIpaddr_Type()
)
fpingManualRmtIpaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpingManualRmtIpaddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FRAMEVISIONFPING-MIB",
    **{"FribDLCI": FribDLCI,
       "Counter32": Counter32,
       "framevisionfping": framevisionfping,
       "fpingMib": fpingMib,
       "fpingMibVersion": fpingMibVersion,
       "fpingMibLastChange": fpingMibLastChange,
       "fpingAuto": fpingAuto,
       "fpingAutoCfgTable": fpingAutoCfgTable,
       "fpingAutoCfgEntry": fpingAutoCfgEntry,
       "fpingAutoCfgIfIndex": fpingAutoCfgIfIndex,
       "fpingAutoCfgLastChange": fpingAutoCfgLastChange,
       "fpingAutoCfgGen": fpingAutoCfgGen,
       "fpingAutoCfgThresh": fpingAutoCfgThresh,
       "fpingAutoCfgReset": fpingAutoCfgReset,
       "fpingAutoDuration": fpingAutoDuration,
       "fpingAutoClearData": fpingAutoClearData,
       "fpingAutoTable": fpingAutoTable,
       "fpingAutoEntry": fpingAutoEntry,
       "fpingAutoIfIndex": fpingAutoIfIndex,
       "fpingAutoDLCI": fpingAutoDLCI,
       "fpingAutoDelayMin": fpingAutoDelayMin,
       "fpingAutoDelayMax": fpingAutoDelayMax,
       "fpingAutoDelayAvg": fpingAutoDelayAvg,
       "fpingAutoLost": fpingAutoLost,
       "fpingAutoTotal": fpingAutoTotal,
       "fpingAutoThreshExceeded": fpingAutoThreshExceeded,
       "fpingAutoRmtDLCI": fpingAutoRmtDLCI,
       "fpingAutoRmtIpaddr": fpingAutoRmtIpaddr,
       "fpingAutoTotalPktsLocalTx": fpingAutoTotalPktsLocalTx,
       "fpingAutoTotalPktsLocalRx": fpingAutoTotalPktsLocalRx,
       "fpingAutoTotalPktsRmtTx": fpingAutoTotalPktsRmtTx,
       "fpingAutoTotalPktsRmtRx": fpingAutoTotalPktsRmtRx,
       "fpingAutoStatus": fpingAutoStatus,
       "fpingAutoFailedEvents": fpingAutoFailedEvents,
       "fpingManual": fpingManual,
       "fpingManualTable": fpingManualTable,
       "fpingManualEntry": fpingManualEntry,
       "fpingManualIfIndex": fpingManualIfIndex,
       "fpingManualDLCI": fpingManualDLCI,
       "fpingManualAction": fpingManualAction,
       "fpingManualState": fpingManualState,
       "fpingManualFreq": fpingManualFreq,
       "fpingManualLen": fpingManualLen,
       "fpingManualCur": fpingManualCur,
       "fpingManualMin": fpingManualMin,
       "fpingManualMax": fpingManualMax,
       "fpingManualAvg": fpingManualAvg,
       "fpingManualLost": fpingManualLost,
       "fpingManualTotal": fpingManualTotal,
       "fpingManualRmtDLCI": fpingManualRmtDLCI,
       "fpingManualRmtIpaddr": fpingManualRmtIpaddr}
)

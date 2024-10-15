# SNMP MIB module (COM21-HCXRX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCXRX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:36 2024
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

(com21,
 com21Hcx,
 com21Traps) = mibBuilder.importSymbols(
    "COM21-HCX-MIB",
    "com21",
    "com21Hcx",
    "com21Traps")

(hcxAlmSeverity,
 hcxEventLogTime) = mibBuilder.importSymbols(
    "COM21-HCXALM-MIB",
    "hcxAlmSeverity",
    "hcxEventLogTime")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

com21HcxRx = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 30)
)


# Types definitions



class UpstrmFreqKhz(Integer32):
    """Custom type UpstrmFreqKhz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 40000),
    )





class PrimServiceState(Integer32):
    """Custom type PrimServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2))
    )





class RfAnalysisdBmv(Integer32):
    """Custom type RfAnalysisdBmv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, -5),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21HcxUpstrmPortGroup_ObjectIdentity = ObjectIdentity
com21HcxUpstrmPortGroup = _Com21HcxUpstrmPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31)
)
_Com21HcxUpstrmPortTable_Object = MibTable
com21HcxUpstrmPortTable = _Com21HcxUpstrmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1)
)
if mibBuilder.loadTexts:
    com21HcxUpstrmPortTable.setStatus("current")
_Com21HcxUpstrmPortEntry_Object = MibTableRow
com21HcxUpstrmPortEntry = _Com21HcxUpstrmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1)
)
com21HcxUpstrmPortEntry.setIndexNames(
    (0, "COM21-HCXRX-MIB", "hcxUpstrmPortShelfId"),
    (0, "COM21-HCXRX-MIB", "hcxUpstrmPortSlotId"),
    (0, "COM21-HCXRX-MIB", "hcxUpstreamPortId"),
)
if mibBuilder.loadTexts:
    com21HcxUpstrmPortEntry.setStatus("current")


class _HcxUpstrmPortShelfId_Type(Integer32):
    """Custom type hcxUpstrmPortShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxUpstrmPortShelfId_Type.__name__ = "Integer32"
_HcxUpstrmPortShelfId_Object = MibTableColumn
hcxUpstrmPortShelfId = _HcxUpstrmPortShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 1),
    _HcxUpstrmPortShelfId_Type()
)
hcxUpstrmPortShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstrmPortShelfId.setStatus("current")
_HcxUpstrmPortSlotId_Type = Integer32
_HcxUpstrmPortSlotId_Object = MibTableColumn
hcxUpstrmPortSlotId = _HcxUpstrmPortSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 2),
    _HcxUpstrmPortSlotId_Type()
)
hcxUpstrmPortSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstrmPortSlotId.setStatus("current")
_HcxUpstreamPortId_Type = Integer32
_HcxUpstreamPortId_Object = MibTableColumn
hcxUpstreamPortId = _HcxUpstreamPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 3),
    _HcxUpstreamPortId_Type()
)
hcxUpstreamPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstreamPortId.setStatus("current")
_HcxRecvFrequency_Type = UpstrmFreqKhz
_HcxRecvFrequency_Object = MibTableColumn
hcxRecvFrequency = _HcxRecvFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 4),
    _HcxRecvFrequency_Type()
)
hcxRecvFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRecvFrequency.setStatus("current")


class _HcxRecvPower_Type(Integer32):
    """Custom type hcxRecvPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 15),
    )


_HcxRecvPower_Type.__name__ = "Integer32"
_HcxRecvPower_Object = MibTableColumn
hcxRecvPower = _HcxRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 5),
    _HcxRecvPower_Type()
)
hcxRecvPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRecvPower.setStatus("current")
_HcxUpstrmAggrStuCbrRate_Type = Integer32
_HcxUpstrmAggrStuCbrRate_Object = MibTableColumn
hcxUpstrmAggrStuCbrRate = _HcxUpstrmAggrStuCbrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 6),
    _HcxUpstrmAggrStuCbrRate_Type()
)
hcxUpstrmAggrStuCbrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstrmAggrStuCbrRate.setStatus("current")
_HcxUpstrmAggrStuMinRate_Type = Integer32
_HcxUpstrmAggrStuMinRate_Object = MibTableColumn
hcxUpstrmAggrStuMinRate = _HcxUpstrmAggrStuMinRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 7),
    _HcxUpstrmAggrStuMinRate_Type()
)
hcxUpstrmAggrStuMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstrmAggrStuMinRate.setStatus("current")
_HcxUpstrmAggrStuMaxRate_Type = Integer32
_HcxUpstrmAggrStuMaxRate_Object = MibTableColumn
hcxUpstrmAggrStuMaxRate = _HcxUpstrmAggrStuMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 8),
    _HcxUpstrmAggrStuMaxRate_Type()
)
hcxUpstrmAggrStuMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstrmAggrStuMaxRate.setStatus("current")


class _HcxUpstrmFreqHopping_Type(Integer32):
    """Custom type hcxUpstrmFreqHopping based on Integer32"""
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


_HcxUpstrmFreqHopping_Type.__name__ = "Integer32"
_HcxUpstrmFreqHopping_Object = MibTableColumn
hcxUpstrmFreqHopping = _HcxUpstrmFreqHopping_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 9),
    _HcxUpstrmFreqHopping_Type()
)
hcxUpstrmFreqHopping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUpstrmFreqHopping.setStatus("current")


class _HcxUpstrmAltFreqA_Type(Integer32):
    """Custom type hcxUpstrmAltFreqA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000),
    )


_HcxUpstrmAltFreqA_Type.__name__ = "Integer32"
_HcxUpstrmAltFreqA_Object = MibTableColumn
hcxUpstrmAltFreqA = _HcxUpstrmAltFreqA_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 10),
    _HcxUpstrmAltFreqA_Type()
)
hcxUpstrmAltFreqA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUpstrmAltFreqA.setStatus("current")


class _HcxUpstrmAltFreqB_Type(Integer32):
    """Custom type hcxUpstrmAltFreqB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000),
    )


_HcxUpstrmAltFreqB_Type.__name__ = "Integer32"
_HcxUpstrmAltFreqB_Object = MibTableColumn
hcxUpstrmAltFreqB = _HcxUpstrmAltFreqB_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 11),
    _HcxUpstrmAltFreqB_Type()
)
hcxUpstrmAltFreqB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUpstrmAltFreqB.setStatus("current")
_HcxUpstrmActiveFreq_Type = UpstrmFreqKhz
_HcxUpstrmActiveFreq_Object = MibTableColumn
hcxUpstrmActiveFreq = _HcxUpstrmActiveFreq_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 12),
    _HcxUpstrmActiveFreq_Type()
)
hcxUpstrmActiveFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstrmActiveFreq.setStatus("current")


class _HcxUpstrmRpmControl_Type(Integer32):
    """Custom type hcxUpstrmRpmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable4Port", 2),
          ("enable8Port", 3),
          ("notSupported", 1))
    )


_HcxUpstrmRpmControl_Type.__name__ = "Integer32"
_HcxUpstrmRpmControl_Object = MibTableColumn
hcxUpstrmRpmControl = _HcxUpstrmRpmControl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 13),
    _HcxUpstrmRpmControl_Type()
)
hcxUpstrmRpmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUpstrmRpmControl.setStatus("current")
_HcxUpstrmRpmPrimServState_Type = PrimServiceState
_HcxUpstrmRpmPrimServState_Object = MibTableColumn
hcxUpstrmRpmPrimServState = _HcxUpstrmRpmPrimServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 14),
    _HcxUpstrmRpmPrimServState_Type()
)
hcxUpstrmRpmPrimServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstrmRpmPrimServState.setStatus("current")


class _HcxUpstrmRpmSecServState_Type(DisplayString):
    """Custom type hcxUpstrmRpmSecServState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxUpstrmRpmSecServState_Type.__name__ = "DisplayString"
_HcxUpstrmRpmSecServState_Object = MibTableColumn
hcxUpstrmRpmSecServState = _HcxUpstrmRpmSecServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 15),
    _HcxUpstrmRpmSecServState_Type()
)
hcxUpstrmRpmSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstrmRpmSecServState.setStatus("current")


class _HcxUpstrmRpmConnType_Type(Integer32):
    """Custom type hcxUpstrmRpmConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 3),
          ("unconnected", 1))
    )


_HcxUpstrmRpmConnType_Type.__name__ = "Integer32"
_HcxUpstrmRpmConnType_Object = MibTableColumn
hcxUpstrmRpmConnType = _HcxUpstrmRpmConnType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 16),
    _HcxUpstrmRpmConnType_Type()
)
hcxUpstrmRpmConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstrmRpmConnType.setStatus("current")
_HcxUpstrmAggrStuVoiceRate_Type = Integer32
_HcxUpstrmAggrStuVoiceRate_Object = MibTableColumn
hcxUpstrmAggrStuVoiceRate = _HcxUpstrmAggrStuVoiceRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 31, 1, 1, 17),
    _HcxUpstrmAggrStuVoiceRate_Type()
)
hcxUpstrmAggrStuVoiceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstrmAggrStuVoiceRate.setStatus("current")
_Com21HcxUpstrmStatsGroup_ObjectIdentity = ObjectIdentity
com21HcxUpstrmStatsGroup = _Com21HcxUpstrmStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32)
)
_Com21HcxUpstrmStatsTable_Object = MibTable
com21HcxUpstrmStatsTable = _Com21HcxUpstrmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1)
)
if mibBuilder.loadTexts:
    com21HcxUpstrmStatsTable.setStatus("current")
_Com21HcxUpstrmStatsEntry_Object = MibTableRow
com21HcxUpstrmStatsEntry = _Com21HcxUpstrmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1)
)
com21HcxUpstrmStatsEntry.setIndexNames(
    (0, "COM21-HCXRX-MIB", "hcxStatsUpstreamShelfId"),
    (0, "COM21-HCXRX-MIB", "hcxStatsUpstreamSlotId"),
    (0, "COM21-HCXRX-MIB", "hcxStatsUpstreamPortId"),
)
if mibBuilder.loadTexts:
    com21HcxUpstrmStatsEntry.setStatus("current")


class _HcxStatsUpstreamShelfId_Type(Integer32):
    """Custom type hcxStatsUpstreamShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxStatsUpstreamShelfId_Type.__name__ = "Integer32"
_HcxStatsUpstreamShelfId_Object = MibTableColumn
hcxStatsUpstreamShelfId = _HcxStatsUpstreamShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 1),
    _HcxStatsUpstreamShelfId_Type()
)
hcxStatsUpstreamShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsUpstreamShelfId.setStatus("current")
_HcxStatsUpstreamSlotId_Type = Integer32
_HcxStatsUpstreamSlotId_Object = MibTableColumn
hcxStatsUpstreamSlotId = _HcxStatsUpstreamSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 2),
    _HcxStatsUpstreamSlotId_Type()
)
hcxStatsUpstreamSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsUpstreamSlotId.setStatus("current")
_HcxStatsUpstreamPortId_Type = Integer32
_HcxStatsUpstreamPortId_Object = MibTableColumn
hcxStatsUpstreamPortId = _HcxStatsUpstreamPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 3),
    _HcxStatsUpstreamPortId_Type()
)
hcxStatsUpstreamPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsUpstreamPortId.setStatus("current")
_HcxPortCurrMinRxCells_Type = Gauge32
_HcxPortCurrMinRxCells_Object = MibTableColumn
hcxPortCurrMinRxCells = _HcxPortCurrMinRxCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 4),
    _HcxPortCurrMinRxCells_Type()
)
hcxPortCurrMinRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortCurrMinRxCells.setStatus("current")
_HcxPortCurrMinRxNullCells_Type = Gauge32
_HcxPortCurrMinRxNullCells_Object = MibTableColumn
hcxPortCurrMinRxNullCells = _HcxPortCurrMinRxNullCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 5),
    _HcxPortCurrMinRxNullCells_Type()
)
hcxPortCurrMinRxNullCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortCurrMinRxNullCells.setStatus("current")
_HcxPortCurrMinUncorrFecHecCells_Type = Gauge32
_HcxPortCurrMinUncorrFecHecCells_Object = MibTableColumn
hcxPortCurrMinUncorrFecHecCells = _HcxPortCurrMinUncorrFecHecCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 6),
    _HcxPortCurrMinUncorrFecHecCells_Type()
)
hcxPortCurrMinUncorrFecHecCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortCurrMinUncorrFecHecCells.setStatus("current")
_HcxPortCurrMinCorrectedFec_Type = Gauge32
_HcxPortCurrMinCorrectedFec_Object = MibTableColumn
hcxPortCurrMinCorrectedFec = _HcxPortCurrMinCorrectedFec_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 8),
    _HcxPortCurrMinCorrectedFec_Type()
)
hcxPortCurrMinCorrectedFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortCurrMinCorrectedFec.setStatus("current")
_HcxPortCurrMinOverSubPeriods_Type = Gauge32
_HcxPortCurrMinOverSubPeriods_Object = MibTableColumn
hcxPortCurrMinOverSubPeriods = _HcxPortCurrMinOverSubPeriods_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 9),
    _HcxPortCurrMinOverSubPeriods_Type()
)
hcxPortCurrMinOverSubPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortCurrMinOverSubPeriods.setStatus("current")
_HcxPortPrevMinRxCells_Type = Gauge32
_HcxPortPrevMinRxCells_Object = MibTableColumn
hcxPortPrevMinRxCells = _HcxPortPrevMinRxCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 10),
    _HcxPortPrevMinRxCells_Type()
)
hcxPortPrevMinRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortPrevMinRxCells.setStatus("current")
_HcxPortPrevMinRxNullCells_Type = Gauge32
_HcxPortPrevMinRxNullCells_Object = MibTableColumn
hcxPortPrevMinRxNullCells = _HcxPortPrevMinRxNullCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 11),
    _HcxPortPrevMinRxNullCells_Type()
)
hcxPortPrevMinRxNullCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortPrevMinRxNullCells.setStatus("current")
_HcxPortPrevMinUncorrFecHecCells_Type = Gauge32
_HcxPortPrevMinUncorrFecHecCells_Object = MibTableColumn
hcxPortPrevMinUncorrFecHecCells = _HcxPortPrevMinUncorrFecHecCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 12),
    _HcxPortPrevMinUncorrFecHecCells_Type()
)
hcxPortPrevMinUncorrFecHecCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortPrevMinUncorrFecHecCells.setStatus("current")
_HcxPortPrevMinCorrectedFec_Type = Gauge32
_HcxPortPrevMinCorrectedFec_Object = MibTableColumn
hcxPortPrevMinCorrectedFec = _HcxPortPrevMinCorrectedFec_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 14),
    _HcxPortPrevMinCorrectedFec_Type()
)
hcxPortPrevMinCorrectedFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortPrevMinCorrectedFec.setStatus("current")
_HcxPortPrevMinOverSubPeriods_Type = Gauge32
_HcxPortPrevMinOverSubPeriods_Object = MibTableColumn
hcxPortPrevMinOverSubPeriods = _HcxPortPrevMinOverSubPeriods_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 15),
    _HcxPortPrevMinOverSubPeriods_Type()
)
hcxPortPrevMinOverSubPeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortPrevMinOverSubPeriods.setStatus("current")


class _HcxPortUpstreamUtil_Type(Integer32):
    """Custom type hcxPortUpstreamUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HcxPortUpstreamUtil_Type.__name__ = "Integer32"
_HcxPortUpstreamUtil_Object = MibTableColumn
hcxPortUpstreamUtil = _HcxPortUpstreamUtil_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 16),
    _HcxPortUpstreamUtil_Type()
)
hcxPortUpstreamUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortUpstreamUtil.setStatus("current")
_HcxPortCurrMeanNoise_Type = Integer32
_HcxPortCurrMeanNoise_Object = MibTableColumn
hcxPortCurrMeanNoise = _HcxPortCurrMeanNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 17),
    _HcxPortCurrMeanNoise_Type()
)
hcxPortCurrMeanNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortCurrMeanNoise.setStatus("current")
_HcxPortPrevMeanNoise_Type = Integer32
_HcxPortPrevMeanNoise_Object = MibTableColumn
hcxPortPrevMeanNoise = _HcxPortPrevMeanNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 18),
    _HcxPortPrevMeanNoise_Type()
)
hcxPortPrevMeanNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortPrevMeanNoise.setStatus("current")


class _HcxPortCorrFecRatioThres_Type(Integer32):
    """Custom type hcxPortCorrFecRatioThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HcxPortCorrFecRatioThres_Type.__name__ = "Integer32"
_HcxPortCorrFecRatioThres_Object = MibTableColumn
hcxPortCorrFecRatioThres = _HcxPortCorrFecRatioThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 19),
    _HcxPortCorrFecRatioThres_Type()
)
hcxPortCorrFecRatioThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxPortCorrFecRatioThres.setStatus("current")


class _HcxPortCellErrRatioThres_Type(Integer32):
    """Custom type hcxPortCellErrRatioThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HcxPortCellErrRatioThres_Type.__name__ = "Integer32"
_HcxPortCellErrRatioThres_Object = MibTableColumn
hcxPortCellErrRatioThres = _HcxPortCellErrRatioThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 20),
    _HcxPortCellErrRatioThres_Type()
)
hcxPortCellErrRatioThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxPortCellErrRatioThres.setStatus("current")


class _HcxPortRatioThresPeriod_Type(Integer32):
    """Custom type hcxPortRatioThresPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_HcxPortRatioThresPeriod_Type.__name__ = "Integer32"
_HcxPortRatioThresPeriod_Object = MibTableColumn
hcxPortRatioThresPeriod = _HcxPortRatioThresPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 21),
    _HcxPortRatioThresPeriod_Type()
)
hcxPortRatioThresPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxPortRatioThresPeriod.setStatus("current")


class _HcxPortMinErrRatioCells_Type(Integer32):
    """Custom type hcxPortMinErrRatioCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2500),
    )


_HcxPortMinErrRatioCells_Type.__name__ = "Integer32"
_HcxPortMinErrRatioCells_Object = MibTableColumn
hcxPortMinErrRatioCells = _HcxPortMinErrRatioCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 22),
    _HcxPortMinErrRatioCells_Type()
)
hcxPortMinErrRatioCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxPortMinErrRatioCells.setStatus("current")


class _HcxPortCnrThres_Type(Integer32):
    """Custom type hcxPortCnrThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 16),
    )


_HcxPortCnrThres_Type.__name__ = "Integer32"
_HcxPortCnrThres_Object = MibTableColumn
hcxPortCnrThres = _HcxPortCnrThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 23),
    _HcxPortCnrThres_Type()
)
hcxPortCnrThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxPortCnrThres.setStatus("current")
_HcxPortCurrMinNoise_Type = Integer32
_HcxPortCurrMinNoise_Object = MibTableColumn
hcxPortCurrMinNoise = _HcxPortCurrMinNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 24),
    _HcxPortCurrMinNoise_Type()
)
hcxPortCurrMinNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortCurrMinNoise.setStatus("current")
_HcxPortCurrMaxNoise_Type = Integer32
_HcxPortCurrMaxNoise_Object = MibTableColumn
hcxPortCurrMaxNoise = _HcxPortCurrMaxNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 25),
    _HcxPortCurrMaxNoise_Type()
)
hcxPortCurrMaxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortCurrMaxNoise.setStatus("current")
_HcxPortPrevMinNoise_Type = Integer32
_HcxPortPrevMinNoise_Object = MibTableColumn
hcxPortPrevMinNoise = _HcxPortPrevMinNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 26),
    _HcxPortPrevMinNoise_Type()
)
hcxPortPrevMinNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortPrevMinNoise.setStatus("current")
_HcxPortPrevMaxNoise_Type = Integer32
_HcxPortPrevMaxNoise_Object = MibTableColumn
hcxPortPrevMaxNoise = _HcxPortPrevMaxNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 27),
    _HcxPortPrevMaxNoise_Type()
)
hcxPortPrevMaxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortPrevMaxNoise.setStatus("current")
_HcxPortRealTimeMeanNoise_Type = Integer32
_HcxPortRealTimeMeanNoise_Object = MibTableColumn
hcxPortRealTimeMeanNoise = _HcxPortRealTimeMeanNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 28),
    _HcxPortRealTimeMeanNoise_Type()
)
hcxPortRealTimeMeanNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortRealTimeMeanNoise.setStatus("current")
_HcxPortRealTimeMinNoise_Type = Integer32
_HcxPortRealTimeMinNoise_Object = MibTableColumn
hcxPortRealTimeMinNoise = _HcxPortRealTimeMinNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 29),
    _HcxPortRealTimeMinNoise_Type()
)
hcxPortRealTimeMinNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortRealTimeMinNoise.setStatus("current")
_HcxPortRealTimeMaxNoise_Type = Integer32
_HcxPortRealTimeMaxNoise_Object = MibTableColumn
hcxPortRealTimeMaxNoise = _HcxPortRealTimeMaxNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 30),
    _HcxPortRealTimeMaxNoise_Type()
)
hcxPortRealTimeMaxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPortRealTimeMaxNoise.setStatus("current")


class _HcxPortClearStats_Type(Integer32):
    """Custom type hcxPortClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_HcxPortClearStats_Type.__name__ = "Integer32"
_HcxPortClearStats_Object = MibTableColumn
hcxPortClearStats = _HcxPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 32, 1, 1, 31),
    _HcxPortClearStats_Type()
)
hcxPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxPortClearStats.setStatus("current")
_Com21HcxUpstrmUnitGroup_ObjectIdentity = ObjectIdentity
com21HcxUpstrmUnitGroup = _Com21HcxUpstrmUnitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33)
)
_Com21HcxUpstrmUnitTable_Object = MibTable
com21HcxUpstrmUnitTable = _Com21HcxUpstrmUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1)
)
if mibBuilder.loadTexts:
    com21HcxUpstrmUnitTable.setStatus("current")
_Com21HcxUpstrmUnitEntry_Object = MibTableRow
com21HcxUpstrmUnitEntry = _Com21HcxUpstrmUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1)
)
com21HcxUpstrmUnitEntry.setIndexNames(
    (0, "COM21-HCXRX-MIB", "hcxUpstreamShelfId"),
    (0, "COM21-HCXRX-MIB", "hcxUpstreamSlotId"),
)
if mibBuilder.loadTexts:
    com21HcxUpstrmUnitEntry.setStatus("current")


class _HcxUpstreamShelfId_Type(Integer32):
    """Custom type hcxUpstreamShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxUpstreamShelfId_Type.__name__ = "Integer32"
_HcxUpstreamShelfId_Object = MibTableColumn
hcxUpstreamShelfId = _HcxUpstreamShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 1),
    _HcxUpstreamShelfId_Type()
)
hcxUpstreamShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstreamShelfId.setStatus("current")
_HcxUpstreamSlotId_Type = Integer32
_HcxUpstreamSlotId_Object = MibTableColumn
hcxUpstreamSlotId = _HcxUpstreamSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 2),
    _HcxUpstreamSlotId_Type()
)
hcxUpstreamSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstreamSlotId.setStatus("current")


class _HcxUpstreamHardwareVersion_Type(DisplayString):
    """Custom type hcxUpstreamHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxUpstreamHardwareVersion_Type.__name__ = "DisplayString"
_HcxUpstreamHardwareVersion_Object = MibTableColumn
hcxUpstreamHardwareVersion = _HcxUpstreamHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 3),
    _HcxUpstreamHardwareVersion_Type()
)
hcxUpstreamHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstreamHardwareVersion.setStatus("current")


class _HcxUpstreamBootVersion_Type(DisplayString):
    """Custom type hcxUpstreamBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxUpstreamBootVersion_Type.__name__ = "DisplayString"
_HcxUpstreamBootVersion_Object = MibTableColumn
hcxUpstreamBootVersion = _HcxUpstreamBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 4),
    _HcxUpstreamBootVersion_Type()
)
hcxUpstreamBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstreamBootVersion.setStatus("current")
_HcxUpstreamUnitPrimServState_Type = PrimServiceState
_HcxUpstreamUnitPrimServState_Object = MibTableColumn
hcxUpstreamUnitPrimServState = _HcxUpstreamUnitPrimServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 5),
    _HcxUpstreamUnitPrimServState_Type()
)
hcxUpstreamUnitPrimServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstreamUnitPrimServState.setStatus("current")


class _HcxUpstreamUnitSecServState_Type(DisplayString):
    """Custom type hcxUpstreamUnitSecServState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxUpstreamUnitSecServState_Type.__name__ = "DisplayString"
_HcxUpstreamUnitSecServState_Object = MibTableColumn
hcxUpstreamUnitSecServState = _HcxUpstreamUnitSecServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 6),
    _HcxUpstreamUnitSecServState_Type()
)
hcxUpstreamUnitSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstreamUnitSecServState.setStatus("current")


class _HcxUpstreamUnitConfigState_Type(Integer32):
    """Custom type hcxUpstreamUnitConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2000,
              2001,
              2002)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2000),
          ("online", 2001),
          ("test", 2002))
    )


_HcxUpstreamUnitConfigState_Type.__name__ = "Integer32"
_HcxUpstreamUnitConfigState_Object = MibTableColumn
hcxUpstreamUnitConfigState = _HcxUpstreamUnitConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 7),
    _HcxUpstreamUnitConfigState_Type()
)
hcxUpstreamUnitConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUpstreamUnitConfigState.setStatus("current")


class _HcxUpstreamUnitRestartAction_Type(Integer32):
    """Custom type hcxUpstreamUnitRestartAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nil", 1),
          ("restart", 2))
    )


_HcxUpstreamUnitRestartAction_Type.__name__ = "Integer32"
_HcxUpstreamUnitRestartAction_Object = MibTableColumn
hcxUpstreamUnitRestartAction = _HcxUpstreamUnitRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 8),
    _HcxUpstreamUnitRestartAction_Type()
)
hcxUpstreamUnitRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUpstreamUnitRestartAction.setStatus("current")


class _HcxUpstreamGroupId_Type(Integer32):
    """Custom type hcxUpstreamGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HcxUpstreamGroupId_Type.__name__ = "Integer32"
_HcxUpstreamGroupId_Object = MibTableColumn
hcxUpstreamGroupId = _HcxUpstreamGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 9),
    _HcxUpstreamGroupId_Type()
)
hcxUpstreamGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUpstreamGroupId.setStatus("current")


class _HcxAcquisitionEnable_Type(Integer32):
    """Custom type hcxAcquisitionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxAcquisitionEnable_Type.__name__ = "Integer32"
_HcxAcquisitionEnable_Object = MibTableColumn
hcxAcquisitionEnable = _HcxAcquisitionEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 10),
    _HcxAcquisitionEnable_Type()
)
hcxAcquisitionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxAcquisitionEnable.setStatus("current")


class _HcxUpDiagTestAction_Type(Integer32):
    """Custom type hcxUpDiagTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("nil", 1))
    )


_HcxUpDiagTestAction_Type.__name__ = "Integer32"
_HcxUpDiagTestAction_Object = MibTableColumn
hcxUpDiagTestAction = _HcxUpDiagTestAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 11),
    _HcxUpDiagTestAction_Type()
)
hcxUpDiagTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUpDiagTestAction.setStatus("current")


class _HcxUpDiagTestResult_Type(Integer32):
    """Custom type hcxUpDiagTestResult based on Integer32"""
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
        *(("failure", 3),
          ("inprogress", 1),
          ("invalidState", 4),
          ("success", 2))
    )


_HcxUpDiagTestResult_Type.__name__ = "Integer32"
_HcxUpDiagTestResult_Object = MibTableColumn
hcxUpDiagTestResult = _HcxUpDiagTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 12),
    _HcxUpDiagTestResult_Type()
)
hcxUpDiagTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpDiagTestResult.setStatus("current")


class _HcxUpTestStatusLed_Type(Integer32):
    """Custom type hcxUpTestStatusLed based on Integer32"""
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


_HcxUpTestStatusLed_Type.__name__ = "Integer32"
_HcxUpTestStatusLed_Object = MibTableColumn
hcxUpTestStatusLed = _HcxUpTestStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 13),
    _HcxUpTestStatusLed_Type()
)
hcxUpTestStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpTestStatusLed.setStatus("current")


class _HcxUpFaultStatusLed_Type(Integer32):
    """Custom type hcxUpFaultStatusLed based on Integer32"""
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


_HcxUpFaultStatusLed_Type.__name__ = "Integer32"
_HcxUpFaultStatusLed_Object = MibTableColumn
hcxUpFaultStatusLed = _HcxUpFaultStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 14),
    _HcxUpFaultStatusLed_Type()
)
hcxUpFaultStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpFaultStatusLed.setStatus("current")


class _HcxUpstreamSerialNumber_Type(DisplayString):
    """Custom type hcxUpstreamSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxUpstreamSerialNumber_Type.__name__ = "DisplayString"
_HcxUpstreamSerialNumber_Object = MibTableColumn
hcxUpstreamSerialNumber = _HcxUpstreamSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 33, 1, 1, 15),
    _HcxUpstreamSerialNumber_Type()
)
hcxUpstreamSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxUpstreamSerialNumber.setStatus("current")
_Com21HcxVciStatsGroup_ObjectIdentity = ObjectIdentity
com21HcxVciStatsGroup = _Com21HcxVciStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34)
)
_Com21HcxVciStatsTable_Object = MibTable
com21HcxVciStatsTable = _Com21HcxVciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1)
)
if mibBuilder.loadTexts:
    com21HcxVciStatsTable.setStatus("current")
_Com21HcxVciStatsEntry_Object = MibTableRow
com21HcxVciStatsEntry = _Com21HcxVciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1)
)
com21HcxVciStatsEntry.setIndexNames(
    (0, "COM21-HCXRX-MIB", "hcxStuStatsMacAddr"),
)
if mibBuilder.loadTexts:
    com21HcxVciStatsEntry.setStatus("current")
_HcxStuStatsMacAddr_Type = MacAddress
_HcxStuStatsMacAddr_Object = MibTableColumn
hcxStuStatsMacAddr = _HcxStuStatsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 1),
    _HcxStuStatsMacAddr_Type()
)
hcxStuStatsMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuStatsMacAddr.setStatus("current")
_HcxStatsCurrMinRxCells_Type = Gauge32
_HcxStatsCurrMinRxCells_Object = MibTableColumn
hcxStatsCurrMinRxCells = _HcxStatsCurrMinRxCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 2),
    _HcxStatsCurrMinRxCells_Type()
)
hcxStatsCurrMinRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsCurrMinRxCells.setStatus("current")
_HcxStatsCurrMinRxNullCells_Type = Gauge32
_HcxStatsCurrMinRxNullCells_Object = MibTableColumn
hcxStatsCurrMinRxNullCells = _HcxStatsCurrMinRxNullCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 3),
    _HcxStatsCurrMinRxNullCells_Type()
)
hcxStatsCurrMinRxNullCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsCurrMinRxNullCells.setStatus("current")
_HcxStatsCurrMinUncorFecHec_Type = Gauge32
_HcxStatsCurrMinUncorFecHec_Object = MibTableColumn
hcxStatsCurrMinUncorFecHec = _HcxStatsCurrMinUncorFecHec_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 6),
    _HcxStatsCurrMinUncorFecHec_Type()
)
hcxStatsCurrMinUncorFecHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsCurrMinUncorFecHec.setStatus("current")
_HcxStatsCurrMinUncorFecThres_Type = Integer32
_HcxStatsCurrMinUncorFecThres_Object = MibTableColumn
hcxStatsCurrMinUncorFecThres = _HcxStatsCurrMinUncorFecThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 7),
    _HcxStatsCurrMinUncorFecThres_Type()
)
hcxStatsCurrMinUncorFecThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStatsCurrMinUncorFecThres.setStatus("current")
_HcxStatsCurrMinCorrectedFec_Type = Gauge32
_HcxStatsCurrMinCorrectedFec_Object = MibTableColumn
hcxStatsCurrMinCorrectedFec = _HcxStatsCurrMinCorrectedFec_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 8),
    _HcxStatsCurrMinCorrectedFec_Type()
)
hcxStatsCurrMinCorrectedFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsCurrMinCorrectedFec.setStatus("current")
_HcxStatsCurrMinCorFecThres_Type = Integer32
_HcxStatsCurrMinCorFecThres_Object = MibTableColumn
hcxStatsCurrMinCorFecThres = _HcxStatsCurrMinCorFecThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 9),
    _HcxStatsCurrMinCorFecThres_Type()
)
hcxStatsCurrMinCorFecThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStatsCurrMinCorFecThres.setStatus("current")
_HcxStatsPrevMinRxCells_Type = Gauge32
_HcxStatsPrevMinRxCells_Object = MibTableColumn
hcxStatsPrevMinRxCells = _HcxStatsPrevMinRxCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 10),
    _HcxStatsPrevMinRxCells_Type()
)
hcxStatsPrevMinRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsPrevMinRxCells.setStatus("current")
_HcxStatsPrevMinRxNullCells_Type = Gauge32
_HcxStatsPrevMinRxNullCells_Object = MibTableColumn
hcxStatsPrevMinRxNullCells = _HcxStatsPrevMinRxNullCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 11),
    _HcxStatsPrevMinRxNullCells_Type()
)
hcxStatsPrevMinRxNullCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsPrevMinRxNullCells.setStatus("current")
_HcxStatsPrevMinUncorFecHec_Type = Gauge32
_HcxStatsPrevMinUncorFecHec_Object = MibTableColumn
hcxStatsPrevMinUncorFecHec = _HcxStatsPrevMinUncorFecHec_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 13),
    _HcxStatsPrevMinUncorFecHec_Type()
)
hcxStatsPrevMinUncorFecHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsPrevMinUncorFecHec.setStatus("current")
_HcxStatsPrevMinCorrectedFec_Type = Gauge32
_HcxStatsPrevMinCorrectedFec_Object = MibTableColumn
hcxStatsPrevMinCorrectedFec = _HcxStatsPrevMinCorrectedFec_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 14),
    _HcxStatsPrevMinCorrectedFec_Type()
)
hcxStatsPrevMinCorrectedFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsPrevMinCorrectedFec.setStatus("current")
_HcxStatsCurrMinMeanSignal_Type = Integer32
_HcxStatsCurrMinMeanSignal_Object = MibTableColumn
hcxStatsCurrMinMeanSignal = _HcxStatsCurrMinMeanSignal_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 15),
    _HcxStatsCurrMinMeanSignal_Type()
)
hcxStatsCurrMinMeanSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsCurrMinMeanSignal.setStatus("current")
_HcxStatsPrevMinMeanSignal_Type = Integer32
_HcxStatsPrevMinMeanSignal_Object = MibTableColumn
hcxStatsPrevMinMeanSignal = _HcxStatsPrevMinMeanSignal_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 16),
    _HcxStatsPrevMinMeanSignal_Type()
)
hcxStatsPrevMinMeanSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsPrevMinMeanSignal.setStatus("current")


class _HcxStatsClearStats_Type(Integer32):
    """Custom type hcxStatsClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_HcxStatsClearStats_Type.__name__ = "Integer32"
_HcxStatsClearStats_Object = MibTableColumn
hcxStatsClearStats = _HcxStatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 34, 1, 1, 17),
    _HcxStatsClearStats_Type()
)
hcxStatsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStatsClearStats.setStatus("current")
_Com21HcxRpmIPortGroup_ObjectIdentity = ObjectIdentity
com21HcxRpmIPortGroup = _Com21HcxRpmIPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 35)
)
_Com21HcxRpmIPortTable_Object = MibTable
com21HcxRpmIPortTable = _Com21HcxRpmIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 35, 1)
)
if mibBuilder.loadTexts:
    com21HcxRpmIPortTable.setStatus("current")
_Com21HcxRpmIPortEntry_Object = MibTableRow
com21HcxRpmIPortEntry = _Com21HcxRpmIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 35, 1, 1)
)
com21HcxRpmIPortEntry.setIndexNames(
    (0, "COM21-HCXRX-MIB", "hcxRpmIPortShelfId"),
    (0, "COM21-HCXRX-MIB", "hcxRpmIPortSlotId"),
    (0, "COM21-HCXRX-MIB", "hcxRpmRxPortId"),
    (0, "COM21-HCXRX-MIB", "hcxRpmIPortId"),
)
if mibBuilder.loadTexts:
    com21HcxRpmIPortEntry.setStatus("current")


class _HcxRpmIPortShelfId_Type(Integer32):
    """Custom type hcxRpmIPortShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxRpmIPortShelfId_Type.__name__ = "Integer32"
_HcxRpmIPortShelfId_Object = MibTableColumn
hcxRpmIPortShelfId = _HcxRpmIPortShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 35, 1, 1, 1),
    _HcxRpmIPortShelfId_Type()
)
hcxRpmIPortShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmIPortShelfId.setStatus("current")
_HcxRpmIPortSlotId_Type = Integer32
_HcxRpmIPortSlotId_Object = MibTableColumn
hcxRpmIPortSlotId = _HcxRpmIPortSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 35, 1, 1, 2),
    _HcxRpmIPortSlotId_Type()
)
hcxRpmIPortSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmIPortSlotId.setStatus("current")
_HcxRpmRxPortId_Type = Integer32
_HcxRpmRxPortId_Object = MibTableColumn
hcxRpmRxPortId = _HcxRpmRxPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 35, 1, 1, 3),
    _HcxRpmRxPortId_Type()
)
hcxRpmRxPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmRxPortId.setStatus("current")


class _HcxRpmIPortId_Type(Integer32):
    """Custom type hcxRpmIPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HcxRpmIPortId_Type.__name__ = "Integer32"
_HcxRpmIPortId_Object = MibTableColumn
hcxRpmIPortId = _HcxRpmIPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 35, 1, 1, 4),
    _HcxRpmIPortId_Type()
)
hcxRpmIPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmIPortId.setStatus("current")


class _HcxRpmIPortRecvPower_Type(Integer32):
    """Custom type hcxRpmIPortRecvPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 15),
    )


_HcxRpmIPortRecvPower_Type.__name__ = "Integer32"
_HcxRpmIPortRecvPower_Object = MibTableColumn
hcxRpmIPortRecvPower = _HcxRpmIPortRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 35, 1, 1, 5),
    _HcxRpmIPortRecvPower_Type()
)
hcxRpmIPortRecvPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRpmIPortRecvPower.setStatus("current")


class _HcxRpmIPortConfigState_Type(Integer32):
    """Custom type hcxRpmIPortConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HcxRpmIPortConfigState_Type.__name__ = "Integer32"
_HcxRpmIPortConfigState_Object = MibTableColumn
hcxRpmIPortConfigState = _HcxRpmIPortConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 35, 1, 1, 6),
    _HcxRpmIPortConfigState_Type()
)
hcxRpmIPortConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRpmIPortConfigState.setStatus("current")


class _HcxRpmIPortContSchedType_Type(Integer32):
    """Custom type hcxRpmIPortContSchedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundRobinOperation", 1),
          ("simultaneousOperation", 2))
    )


_HcxRpmIPortContSchedType_Type.__name__ = "Integer32"
_HcxRpmIPortContSchedType_Object = MibTableColumn
hcxRpmIPortContSchedType = _HcxRpmIPortContSchedType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 35, 1, 1, 7),
    _HcxRpmIPortContSchedType_Type()
)
hcxRpmIPortContSchedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRpmIPortContSchedType.setStatus("current")
_Com21HcxRpmStatsGroup_ObjectIdentity = ObjectIdentity
com21HcxRpmStatsGroup = _Com21HcxRpmStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36)
)
_Com21HcxRpmStatsTable_Object = MibTable
com21HcxRpmStatsTable = _Com21HcxRpmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1)
)
if mibBuilder.loadTexts:
    com21HcxRpmStatsTable.setStatus("current")
_Com21HcxRpmStatsEntry_Object = MibTableRow
com21HcxRpmStatsEntry = _Com21HcxRpmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1)
)
com21HcxRpmStatsEntry.setIndexNames(
    (0, "COM21-HCXRX-MIB", "hcxStatsRpmShelfId"),
    (0, "COM21-HCXRX-MIB", "hcxStatsRpmSlotId"),
    (0, "COM21-HCXRX-MIB", "hcxStatsRxPortId"),
    (0, "COM21-HCXRX-MIB", "hcxStatsRpmIPortId"),
)
if mibBuilder.loadTexts:
    com21HcxRpmStatsEntry.setStatus("current")


class _HcxStatsRpmShelfId_Type(Integer32):
    """Custom type hcxStatsRpmShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxStatsRpmShelfId_Type.__name__ = "Integer32"
_HcxStatsRpmShelfId_Object = MibTableColumn
hcxStatsRpmShelfId = _HcxStatsRpmShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 1),
    _HcxStatsRpmShelfId_Type()
)
hcxStatsRpmShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsRpmShelfId.setStatus("current")
_HcxStatsRpmSlotId_Type = Integer32
_HcxStatsRpmSlotId_Object = MibTableColumn
hcxStatsRpmSlotId = _HcxStatsRpmSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 2),
    _HcxStatsRpmSlotId_Type()
)
hcxStatsRpmSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsRpmSlotId.setStatus("current")
_HcxStatsRxPortId_Type = Integer32
_HcxStatsRxPortId_Object = MibTableColumn
hcxStatsRxPortId = _HcxStatsRxPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 3),
    _HcxStatsRxPortId_Type()
)
hcxStatsRxPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsRxPortId.setStatus("current")


class _HcxStatsRpmIPortId_Type(Integer32):
    """Custom type hcxStatsRpmIPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HcxStatsRpmIPortId_Type.__name__ = "Integer32"
_HcxStatsRpmIPortId_Object = MibTableColumn
hcxStatsRpmIPortId = _HcxStatsRpmIPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 4),
    _HcxStatsRpmIPortId_Type()
)
hcxStatsRpmIPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsRpmIPortId.setStatus("current")
_HcxRpmCurrMinRxCells_Type = Gauge32
_HcxRpmCurrMinRxCells_Object = MibTableColumn
hcxRpmCurrMinRxCells = _HcxRpmCurrMinRxCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 5),
    _HcxRpmCurrMinRxCells_Type()
)
hcxRpmCurrMinRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmCurrMinRxCells.setStatus("current")
_HcxRpmCurrMinRxNullCells_Type = Gauge32
_HcxRpmCurrMinRxNullCells_Object = MibTableColumn
hcxRpmCurrMinRxNullCells = _HcxRpmCurrMinRxNullCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 6),
    _HcxRpmCurrMinRxNullCells_Type()
)
hcxRpmCurrMinRxNullCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmCurrMinRxNullCells.setStatus("current")
_HcxRpmCurrMinUncorFecHecCells_Type = Gauge32
_HcxRpmCurrMinUncorFecHecCells_Object = MibTableColumn
hcxRpmCurrMinUncorFecHecCells = _HcxRpmCurrMinUncorFecHecCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 7),
    _HcxRpmCurrMinUncorFecHecCells_Type()
)
hcxRpmCurrMinUncorFecHecCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmCurrMinUncorFecHecCells.setStatus("current")
_HcxRpmCurrMinCorrectedFec_Type = Gauge32
_HcxRpmCurrMinCorrectedFec_Object = MibTableColumn
hcxRpmCurrMinCorrectedFec = _HcxRpmCurrMinCorrectedFec_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 8),
    _HcxRpmCurrMinCorrectedFec_Type()
)
hcxRpmCurrMinCorrectedFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmCurrMinCorrectedFec.setStatus("current")
_HcxRpmCurrMeanNoise_Type = Integer32
_HcxRpmCurrMeanNoise_Object = MibTableColumn
hcxRpmCurrMeanNoise = _HcxRpmCurrMeanNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 9),
    _HcxRpmCurrMeanNoise_Type()
)
hcxRpmCurrMeanNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmCurrMeanNoise.setStatus("current")
_HcxRpmCurrMinNoise_Type = Integer32
_HcxRpmCurrMinNoise_Object = MibTableColumn
hcxRpmCurrMinNoise = _HcxRpmCurrMinNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 10),
    _HcxRpmCurrMinNoise_Type()
)
hcxRpmCurrMinNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmCurrMinNoise.setStatus("current")
_HcxRpmCurrMaxNoise_Type = Integer32
_HcxRpmCurrMaxNoise_Object = MibTableColumn
hcxRpmCurrMaxNoise = _HcxRpmCurrMaxNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 11),
    _HcxRpmCurrMaxNoise_Type()
)
hcxRpmCurrMaxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmCurrMaxNoise.setStatus("current")
_HcxRpmRealTimeMeanNoise_Type = Integer32
_HcxRpmRealTimeMeanNoise_Object = MibTableColumn
hcxRpmRealTimeMeanNoise = _HcxRpmRealTimeMeanNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 12),
    _HcxRpmRealTimeMeanNoise_Type()
)
hcxRpmRealTimeMeanNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmRealTimeMeanNoise.setStatus("current")
_HcxRpmRealTimeMinNoise_Type = Integer32
_HcxRpmRealTimeMinNoise_Object = MibTableColumn
hcxRpmRealTimeMinNoise = _HcxRpmRealTimeMinNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 13),
    _HcxRpmRealTimeMinNoise_Type()
)
hcxRpmRealTimeMinNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmRealTimeMinNoise.setStatus("current")
_HcxRpmRealTimeMaxNoise_Type = Integer32
_HcxRpmRealTimeMaxNoise_Object = MibTableColumn
hcxRpmRealTimeMaxNoise = _HcxRpmRealTimeMaxNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 14),
    _HcxRpmRealTimeMaxNoise_Type()
)
hcxRpmRealTimeMaxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmRealTimeMaxNoise.setStatus("current")
_HcxRpmPrevMinRxCells_Type = Gauge32
_HcxRpmPrevMinRxCells_Object = MibTableColumn
hcxRpmPrevMinRxCells = _HcxRpmPrevMinRxCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 15),
    _HcxRpmPrevMinRxCells_Type()
)
hcxRpmPrevMinRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmPrevMinRxCells.setStatus("current")
_HcxRpmPrevMinRxNullCells_Type = Gauge32
_HcxRpmPrevMinRxNullCells_Object = MibTableColumn
hcxRpmPrevMinRxNullCells = _HcxRpmPrevMinRxNullCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 16),
    _HcxRpmPrevMinRxNullCells_Type()
)
hcxRpmPrevMinRxNullCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmPrevMinRxNullCells.setStatus("current")
_HcxRpmPrevMinUncorFecHecCells_Type = Gauge32
_HcxRpmPrevMinUncorFecHecCells_Object = MibTableColumn
hcxRpmPrevMinUncorFecHecCells = _HcxRpmPrevMinUncorFecHecCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 17),
    _HcxRpmPrevMinUncorFecHecCells_Type()
)
hcxRpmPrevMinUncorFecHecCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmPrevMinUncorFecHecCells.setStatus("current")
_HcxRpmPrevMinCorrectedFec_Type = Gauge32
_HcxRpmPrevMinCorrectedFec_Object = MibTableColumn
hcxRpmPrevMinCorrectedFec = _HcxRpmPrevMinCorrectedFec_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 18),
    _HcxRpmPrevMinCorrectedFec_Type()
)
hcxRpmPrevMinCorrectedFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmPrevMinCorrectedFec.setStatus("current")
_HcxRpmPrevMeanNoise_Type = Integer32
_HcxRpmPrevMeanNoise_Object = MibTableColumn
hcxRpmPrevMeanNoise = _HcxRpmPrevMeanNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 19),
    _HcxRpmPrevMeanNoise_Type()
)
hcxRpmPrevMeanNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmPrevMeanNoise.setStatus("current")
_HcxRpmPrevMinNoise_Type = Integer32
_HcxRpmPrevMinNoise_Object = MibTableColumn
hcxRpmPrevMinNoise = _HcxRpmPrevMinNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 20),
    _HcxRpmPrevMinNoise_Type()
)
hcxRpmPrevMinNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmPrevMinNoise.setStatus("current")
_HcxRpmPrevMaxNoise_Type = Integer32
_HcxRpmPrevMaxNoise_Object = MibTableColumn
hcxRpmPrevMaxNoise = _HcxRpmPrevMaxNoise_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 21),
    _HcxRpmPrevMaxNoise_Type()
)
hcxRpmPrevMaxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRpmPrevMaxNoise.setStatus("current")


class _HcxRpmCorrFecRatioThres_Type(Integer32):
    """Custom type hcxRpmCorrFecRatioThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HcxRpmCorrFecRatioThres_Type.__name__ = "Integer32"
_HcxRpmCorrFecRatioThres_Object = MibTableColumn
hcxRpmCorrFecRatioThres = _HcxRpmCorrFecRatioThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 22),
    _HcxRpmCorrFecRatioThres_Type()
)
hcxRpmCorrFecRatioThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRpmCorrFecRatioThres.setStatus("current")


class _HcxRpmCellErrRatioThres_Type(Integer32):
    """Custom type hcxRpmCellErrRatioThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HcxRpmCellErrRatioThres_Type.__name__ = "Integer32"
_HcxRpmCellErrRatioThres_Object = MibTableColumn
hcxRpmCellErrRatioThres = _HcxRpmCellErrRatioThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 23),
    _HcxRpmCellErrRatioThres_Type()
)
hcxRpmCellErrRatioThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRpmCellErrRatioThres.setStatus("current")


class _HcxRpmRatioThresPeriod_Type(Integer32):
    """Custom type hcxRpmRatioThresPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_HcxRpmRatioThresPeriod_Type.__name__ = "Integer32"
_HcxRpmRatioThresPeriod_Object = MibTableColumn
hcxRpmRatioThresPeriod = _HcxRpmRatioThresPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 24),
    _HcxRpmRatioThresPeriod_Type()
)
hcxRpmRatioThresPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRpmRatioThresPeriod.setStatus("current")


class _HcxRpmMinErrRatioCells_Type(Integer32):
    """Custom type hcxRpmMinErrRatioCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2500),
    )


_HcxRpmMinErrRatioCells_Type.__name__ = "Integer32"
_HcxRpmMinErrRatioCells_Object = MibTableColumn
hcxRpmMinErrRatioCells = _HcxRpmMinErrRatioCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 25),
    _HcxRpmMinErrRatioCells_Type()
)
hcxRpmMinErrRatioCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRpmMinErrRatioCells.setStatus("current")


class _HcxRpmCnrThres_Type(Integer32):
    """Custom type hcxRpmCnrThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 16),
    )


_HcxRpmCnrThres_Type.__name__ = "Integer32"
_HcxRpmCnrThres_Object = MibTableColumn
hcxRpmCnrThres = _HcxRpmCnrThres_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 26),
    _HcxRpmCnrThres_Type()
)
hcxRpmCnrThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRpmCnrThres.setStatus("current")


class _HcxRpmClearStats_Type(Integer32):
    """Custom type hcxRpmClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_HcxRpmClearStats_Type.__name__ = "Integer32"
_HcxRpmClearStats_Object = MibTableColumn
hcxRpmClearStats = _HcxRpmClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 36, 1, 1, 27),
    _HcxRpmClearStats_Type()
)
hcxRpmClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRpmClearStats.setStatus("current")
_Com21HcxRfAnalysisGroup_ObjectIdentity = ObjectIdentity
com21HcxRfAnalysisGroup = _Com21HcxRfAnalysisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37)
)
_Com21HcxRfAnalysisTable_Object = MibTable
com21HcxRfAnalysisTable = _Com21HcxRfAnalysisTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1)
)
if mibBuilder.loadTexts:
    com21HcxRfAnalysisTable.setStatus("current")
_Com21HcxRfAnalysisEntry_Object = MibTableRow
com21HcxRfAnalysisEntry = _Com21HcxRfAnalysisEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1)
)
com21HcxRfAnalysisEntry.setIndexNames(
    (0, "COM21-HCXRX-MIB", "hcxRfAnalysisShelfId"),
    (0, "COM21-HCXRX-MIB", "hcxRfAnalysisSlotId"),
    (0, "COM21-HCXRX-MIB", "hcxRfAnalysisPortId"),
    (0, "COM21-HCXRX-MIB", "hcxRfAnalysisRpmPortId"),
)
if mibBuilder.loadTexts:
    com21HcxRfAnalysisEntry.setStatus("current")


class _HcxRfAnalysisShelfId_Type(Integer32):
    """Custom type hcxRfAnalysisShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxRfAnalysisShelfId_Type.__name__ = "Integer32"
_HcxRfAnalysisShelfId_Object = MibTableColumn
hcxRfAnalysisShelfId = _HcxRfAnalysisShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 1),
    _HcxRfAnalysisShelfId_Type()
)
hcxRfAnalysisShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRfAnalysisShelfId.setStatus("current")
_HcxRfAnalysisSlotId_Type = Integer32
_HcxRfAnalysisSlotId_Object = MibTableColumn
hcxRfAnalysisSlotId = _HcxRfAnalysisSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 2),
    _HcxRfAnalysisSlotId_Type()
)
hcxRfAnalysisSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRfAnalysisSlotId.setStatus("current")
_HcxRfAnalysisPortId_Type = Integer32
_HcxRfAnalysisPortId_Object = MibTableColumn
hcxRfAnalysisPortId = _HcxRfAnalysisPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 3),
    _HcxRfAnalysisPortId_Type()
)
hcxRfAnalysisPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRfAnalysisPortId.setStatus("current")


class _HcxRfAnalysisRpmPortId_Type(Integer32):
    """Custom type hcxRfAnalysisRpmPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HcxRfAnalysisRpmPortId_Type.__name__ = "Integer32"
_HcxRfAnalysisRpmPortId_Object = MibTableColumn
hcxRfAnalysisRpmPortId = _HcxRfAnalysisRpmPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 4),
    _HcxRfAnalysisRpmPortId_Type()
)
hcxRfAnalysisRpmPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRfAnalysisRpmPortId.setStatus("current")


class _HcxRfAnalysisControl_Type(Integer32):
    """Custom type hcxRfAnalysisControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HcxRfAnalysisControl_Type.__name__ = "Integer32"
_HcxRfAnalysisControl_Object = MibTableColumn
hcxRfAnalysisControl = _HcxRfAnalysisControl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 5),
    _HcxRfAnalysisControl_Type()
)
hcxRfAnalysisControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRfAnalysisControl.setStatus("current")
_HcxRfAnalysisPoint1_Type = RfAnalysisdBmv
_HcxRfAnalysisPoint1_Object = MibTableColumn
hcxRfAnalysisPoint1 = _HcxRfAnalysisPoint1_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 6),
    _HcxRfAnalysisPoint1_Type()
)
hcxRfAnalysisPoint1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRfAnalysisPoint1.setStatus("current")
_HcxRfAnalysisPoint2_Type = RfAnalysisdBmv
_HcxRfAnalysisPoint2_Object = MibTableColumn
hcxRfAnalysisPoint2 = _HcxRfAnalysisPoint2_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 7),
    _HcxRfAnalysisPoint2_Type()
)
hcxRfAnalysisPoint2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRfAnalysisPoint2.setStatus("current")
_HcxRfAnalysisPoint3_Type = RfAnalysisdBmv
_HcxRfAnalysisPoint3_Object = MibTableColumn
hcxRfAnalysisPoint3 = _HcxRfAnalysisPoint3_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 8),
    _HcxRfAnalysisPoint3_Type()
)
hcxRfAnalysisPoint3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRfAnalysisPoint3.setStatus("current")
_HcxRfAnalysisPoint4_Type = RfAnalysisdBmv
_HcxRfAnalysisPoint4_Object = MibTableColumn
hcxRfAnalysisPoint4 = _HcxRfAnalysisPoint4_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 9),
    _HcxRfAnalysisPoint4_Type()
)
hcxRfAnalysisPoint4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRfAnalysisPoint4.setStatus("current")
_HcxRfAnalysisBin1Count_Type = Gauge32
_HcxRfAnalysisBin1Count_Object = MibTableColumn
hcxRfAnalysisBin1Count = _HcxRfAnalysisBin1Count_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 10),
    _HcxRfAnalysisBin1Count_Type()
)
hcxRfAnalysisBin1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRfAnalysisBin1Count.setStatus("current")
_HcxRfAnalysisBin2Count_Type = Gauge32
_HcxRfAnalysisBin2Count_Object = MibTableColumn
hcxRfAnalysisBin2Count = _HcxRfAnalysisBin2Count_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 11),
    _HcxRfAnalysisBin2Count_Type()
)
hcxRfAnalysisBin2Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRfAnalysisBin2Count.setStatus("current")
_HcxRfAnalysisBin3Count_Type = Gauge32
_HcxRfAnalysisBin3Count_Object = MibTableColumn
hcxRfAnalysisBin3Count = _HcxRfAnalysisBin3Count_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 12),
    _HcxRfAnalysisBin3Count_Type()
)
hcxRfAnalysisBin3Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxRfAnalysisBin3Count.setStatus("current")


class _HcxRfAnalysisClearCount_Type(Integer32):
    """Custom type hcxRfAnalysisClearCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_HcxRfAnalysisClearCount_Type.__name__ = "Integer32"
_HcxRfAnalysisClearCount_Object = MibTableColumn
hcxRfAnalysisClearCount = _HcxRfAnalysisClearCount_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 37, 1, 1, 13),
    _HcxRfAnalysisClearCount_Type()
)
hcxRfAnalysisClearCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRfAnalysisClearCount.setStatus("current")

# Managed Objects groups


# Notification objects

hcxUpstreamUnitPrimStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 30)
)
hcxUpstreamUnitPrimStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstreamShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamUnitPrimServState"))
)
if mibBuilder.loadTexts:
    hcxUpstreamUnitPrimStateChange.setStatus(
        "current"
    )

hcxUpstreamUnitSecStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 31)
)
hcxUpstreamUnitSecStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstreamShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamUnitSecServState"))
)
if mibBuilder.loadTexts:
    hcxUpstreamUnitSecStateChange.setStatus(
        "current"
    )

hcxUpDiagTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 32)
)
hcxUpDiagTestComplete.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstreamShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpDiagTestResult"))
)
if mibBuilder.loadTexts:
    hcxUpDiagTestComplete.setStatus(
        "current"
    )

hcxUpTestStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 33)
)
hcxUpTestStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstreamShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpTestStatusLed"))
)
if mibBuilder.loadTexts:
    hcxUpTestStatusLedChange.setStatus(
        "current"
    )

hcxUpFaultStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 34)
)
hcxUpFaultStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstreamShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpFaultStatusLed"))
)
if mibBuilder.loadTexts:
    hcxUpFaultStatusLedChange.setStatus(
        "current"
    )

hcxUpOperationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 35)
)
hcxUpOperationFailure.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstreamShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamSlotId"))
)
if mibBuilder.loadTexts:
    hcxUpOperationFailure.setStatus(
        "current"
    )

hcxUncorFecHecMinThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 37)
)
hcxUncorFecHecMinThres.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxStuStatsMacAddr"),
        ("COM21-HCXRX-MIB", "hcxStatsCurrMinUncorFecThres"),
        ("COM21-HCXRX-MIB", "hcxStatsCurrMinUncorFecHec"))
)
if mibBuilder.loadTexts:
    hcxUncorFecHecMinThres.setStatus(
        "current"
    )

hcxCorrectedFecMinThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 38)
)
hcxCorrectedFecMinThres.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxStuStatsMacAddr"),
        ("COM21-HCXRX-MIB", "hcxStatsCurrMinCorFecThres"),
        ("COM21-HCXRX-MIB", "hcxStatsCurrMinCorrectedFec"))
)
if mibBuilder.loadTexts:
    hcxCorrectedFecMinThres.setStatus(
        "current"
    )

hcxCorrFecRatioThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 80)
)
hcxCorrFecRatioThres.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxStatsUpstreamShelfId"),
        ("COM21-HCXRX-MIB", "hcxStatsUpstreamSlotId"),
        ("COM21-HCXRX-MIB", "hcxStatsUpstreamPortId"),
        ("COM21-HCXRX-MIB", "hcxPortCorrFecRatioThres"))
)
if mibBuilder.loadTexts:
    hcxCorrFecRatioThres.setStatus(
        "current"
    )

hcxCellErrRatioThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 81)
)
hcxCellErrRatioThres.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxStatsUpstreamShelfId"),
        ("COM21-HCXRX-MIB", "hcxStatsUpstreamSlotId"),
        ("COM21-HCXRX-MIB", "hcxStatsUpstreamPortId"),
        ("COM21-HCXRX-MIB", "hcxPortCellErrRatioThres"))
)
if mibBuilder.loadTexts:
    hcxCellErrRatioThres.setStatus(
        "current"
    )

hcxRxFreqHop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 82)
)
hcxRxFreqHop.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamPortId"),
        ("COM21-HCXRX-MIB", "hcxUpstrmActiveFreq"))
)
if mibBuilder.loadTexts:
    hcxRxFreqHop.setStatus(
        "current"
    )

hcxCnrThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 83)
)
hcxCnrThres.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxStatsUpstreamShelfId"),
        ("COM21-HCXRX-MIB", "hcxStatsUpstreamSlotId"),
        ("COM21-HCXRX-MIB", "hcxStatsUpstreamPortId"),
        ("COM21-HCXRX-MIB", "hcxPortCnrThres"))
)
if mibBuilder.loadTexts:
    hcxCnrThres.setStatus(
        "current"
    )

hcxRpmFecRatioThres = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 84)
)
hcxRpmFecRatioThres.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxStatsRpmShelfId"),
        ("COM21-HCXRX-MIB", "hcxStatsRpmSlotId"),
        ("COM21-HCXRX-MIB", "hcxStatsRxPortId"),
        ("COM21-HCXRX-MIB", "hcxStatsRpmIPortId"),
        ("COM21-HCXRX-MIB", "hcxRpmCorrFecRatioThres"))
)
if mibBuilder.loadTexts:
    hcxRpmFecRatioThres.setStatus(
        "current"
    )

hcxRpmCellErrRatioThresTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 85)
)
hcxRpmCellErrRatioThresTrap.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxStatsRpmShelfId"),
        ("COM21-HCXRX-MIB", "hcxStatsRpmSlotId"),
        ("COM21-HCXRX-MIB", "hcxStatsRxPortId"),
        ("COM21-HCXRX-MIB", "hcxStatsRpmIPortId"),
        ("COM21-HCXRX-MIB", "hcxRpmCellErrRatioThres"))
)
if mibBuilder.loadTexts:
    hcxRpmCellErrRatioThresTrap.setStatus(
        "current"
    )

hcxRpmCnrThresTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 86)
)
hcxRpmCnrThresTrap.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxStatsRpmShelfId"),
        ("COM21-HCXRX-MIB", "hcxStatsRpmSlotId"),
        ("COM21-HCXRX-MIB", "hcxStatsRxPortId"),
        ("COM21-HCXRX-MIB", "hcxStatsRpmIPortId"),
        ("COM21-HCXRX-MIB", "hcxRpmCnrThres"))
)
if mibBuilder.loadTexts:
    hcxRpmCnrThresTrap.setStatus(
        "current"
    )

hcxRpmInvalidPhyConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 87)
)
hcxRpmInvalidPhyConfig.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamPortId"))
)
if mibBuilder.loadTexts:
    hcxRpmInvalidPhyConfig.setStatus(
        "current"
    )

hcxRpmInvalidConfClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 88)
)
hcxRpmInvalidConfClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamPortId"))
)
if mibBuilder.loadTexts:
    hcxRpmInvalidConfClear.setStatus(
        "current"
    )

hcxRpmTimingFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 89)
)
hcxRpmTimingFault.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamPortId"))
)
if mibBuilder.loadTexts:
    hcxRpmTimingFault.setStatus(
        "current"
    )

hcxRpmTimingFaultClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 130)
)
hcxRpmTimingFaultClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamPortId"))
)
if mibBuilder.loadTexts:
    hcxRpmTimingFaultClear.setStatus(
        "current"
    )

hcxRpmLinkError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 131)
)
hcxRpmLinkError.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamPortId"))
)
if mibBuilder.loadTexts:
    hcxRpmLinkError.setStatus(
        "current"
    )

hcxRpmLinkErrClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 132)
)
hcxRpmLinkErrClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamPortId"))
)
if mibBuilder.loadTexts:
    hcxRpmLinkErrClear.setStatus(
        "current"
    )

hcxUpstrmRpmPrimStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 133)
)
hcxUpstrmRpmPrimStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortShelfId"),
        ("COM21-HCXRX-MIB", "hcxUpstrmPortSlotId"),
        ("COM21-HCXRX-MIB", "hcxUpstreamPortId"),
        ("COM21-HCXRX-MIB", "hcxUpstrmRpmPrimServState"))
)
if mibBuilder.loadTexts:
    hcxUpstrmRpmPrimStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCXRX-MIB",
    **{"UpstrmFreqKhz": UpstrmFreqKhz,
       "PrimServiceState": PrimServiceState,
       "RfAnalysisdBmv": RfAnalysisdBmv,
       "com21HcxRx": com21HcxRx,
       "com21HcxUpstrmPortGroup": com21HcxUpstrmPortGroup,
       "com21HcxUpstrmPortTable": com21HcxUpstrmPortTable,
       "com21HcxUpstrmPortEntry": com21HcxUpstrmPortEntry,
       "hcxUpstrmPortShelfId": hcxUpstrmPortShelfId,
       "hcxUpstrmPortSlotId": hcxUpstrmPortSlotId,
       "hcxUpstreamPortId": hcxUpstreamPortId,
       "hcxRecvFrequency": hcxRecvFrequency,
       "hcxRecvPower": hcxRecvPower,
       "hcxUpstrmAggrStuCbrRate": hcxUpstrmAggrStuCbrRate,
       "hcxUpstrmAggrStuMinRate": hcxUpstrmAggrStuMinRate,
       "hcxUpstrmAggrStuMaxRate": hcxUpstrmAggrStuMaxRate,
       "hcxUpstrmFreqHopping": hcxUpstrmFreqHopping,
       "hcxUpstrmAltFreqA": hcxUpstrmAltFreqA,
       "hcxUpstrmAltFreqB": hcxUpstrmAltFreqB,
       "hcxUpstrmActiveFreq": hcxUpstrmActiveFreq,
       "hcxUpstrmRpmControl": hcxUpstrmRpmControl,
       "hcxUpstrmRpmPrimServState": hcxUpstrmRpmPrimServState,
       "hcxUpstrmRpmSecServState": hcxUpstrmRpmSecServState,
       "hcxUpstrmRpmConnType": hcxUpstrmRpmConnType,
       "hcxUpstrmAggrStuVoiceRate": hcxUpstrmAggrStuVoiceRate,
       "com21HcxUpstrmStatsGroup": com21HcxUpstrmStatsGroup,
       "com21HcxUpstrmStatsTable": com21HcxUpstrmStatsTable,
       "com21HcxUpstrmStatsEntry": com21HcxUpstrmStatsEntry,
       "hcxStatsUpstreamShelfId": hcxStatsUpstreamShelfId,
       "hcxStatsUpstreamSlotId": hcxStatsUpstreamSlotId,
       "hcxStatsUpstreamPortId": hcxStatsUpstreamPortId,
       "hcxPortCurrMinRxCells": hcxPortCurrMinRxCells,
       "hcxPortCurrMinRxNullCells": hcxPortCurrMinRxNullCells,
       "hcxPortCurrMinUncorrFecHecCells": hcxPortCurrMinUncorrFecHecCells,
       "hcxPortCurrMinCorrectedFec": hcxPortCurrMinCorrectedFec,
       "hcxPortCurrMinOverSubPeriods": hcxPortCurrMinOverSubPeriods,
       "hcxPortPrevMinRxCells": hcxPortPrevMinRxCells,
       "hcxPortPrevMinRxNullCells": hcxPortPrevMinRxNullCells,
       "hcxPortPrevMinUncorrFecHecCells": hcxPortPrevMinUncorrFecHecCells,
       "hcxPortPrevMinCorrectedFec": hcxPortPrevMinCorrectedFec,
       "hcxPortPrevMinOverSubPeriods": hcxPortPrevMinOverSubPeriods,
       "hcxPortUpstreamUtil": hcxPortUpstreamUtil,
       "hcxPortCurrMeanNoise": hcxPortCurrMeanNoise,
       "hcxPortPrevMeanNoise": hcxPortPrevMeanNoise,
       "hcxPortCorrFecRatioThres": hcxPortCorrFecRatioThres,
       "hcxPortCellErrRatioThres": hcxPortCellErrRatioThres,
       "hcxPortRatioThresPeriod": hcxPortRatioThresPeriod,
       "hcxPortMinErrRatioCells": hcxPortMinErrRatioCells,
       "hcxPortCnrThres": hcxPortCnrThres,
       "hcxPortCurrMinNoise": hcxPortCurrMinNoise,
       "hcxPortCurrMaxNoise": hcxPortCurrMaxNoise,
       "hcxPortPrevMinNoise": hcxPortPrevMinNoise,
       "hcxPortPrevMaxNoise": hcxPortPrevMaxNoise,
       "hcxPortRealTimeMeanNoise": hcxPortRealTimeMeanNoise,
       "hcxPortRealTimeMinNoise": hcxPortRealTimeMinNoise,
       "hcxPortRealTimeMaxNoise": hcxPortRealTimeMaxNoise,
       "hcxPortClearStats": hcxPortClearStats,
       "com21HcxUpstrmUnitGroup": com21HcxUpstrmUnitGroup,
       "com21HcxUpstrmUnitTable": com21HcxUpstrmUnitTable,
       "com21HcxUpstrmUnitEntry": com21HcxUpstrmUnitEntry,
       "hcxUpstreamShelfId": hcxUpstreamShelfId,
       "hcxUpstreamSlotId": hcxUpstreamSlotId,
       "hcxUpstreamHardwareVersion": hcxUpstreamHardwareVersion,
       "hcxUpstreamBootVersion": hcxUpstreamBootVersion,
       "hcxUpstreamUnitPrimServState": hcxUpstreamUnitPrimServState,
       "hcxUpstreamUnitSecServState": hcxUpstreamUnitSecServState,
       "hcxUpstreamUnitConfigState": hcxUpstreamUnitConfigState,
       "hcxUpstreamUnitRestartAction": hcxUpstreamUnitRestartAction,
       "hcxUpstreamGroupId": hcxUpstreamGroupId,
       "hcxAcquisitionEnable": hcxAcquisitionEnable,
       "hcxUpDiagTestAction": hcxUpDiagTestAction,
       "hcxUpDiagTestResult": hcxUpDiagTestResult,
       "hcxUpTestStatusLed": hcxUpTestStatusLed,
       "hcxUpFaultStatusLed": hcxUpFaultStatusLed,
       "hcxUpstreamSerialNumber": hcxUpstreamSerialNumber,
       "com21HcxVciStatsGroup": com21HcxVciStatsGroup,
       "com21HcxVciStatsTable": com21HcxVciStatsTable,
       "com21HcxVciStatsEntry": com21HcxVciStatsEntry,
       "hcxStuStatsMacAddr": hcxStuStatsMacAddr,
       "hcxStatsCurrMinRxCells": hcxStatsCurrMinRxCells,
       "hcxStatsCurrMinRxNullCells": hcxStatsCurrMinRxNullCells,
       "hcxStatsCurrMinUncorFecHec": hcxStatsCurrMinUncorFecHec,
       "hcxStatsCurrMinUncorFecThres": hcxStatsCurrMinUncorFecThres,
       "hcxStatsCurrMinCorrectedFec": hcxStatsCurrMinCorrectedFec,
       "hcxStatsCurrMinCorFecThres": hcxStatsCurrMinCorFecThres,
       "hcxStatsPrevMinRxCells": hcxStatsPrevMinRxCells,
       "hcxStatsPrevMinRxNullCells": hcxStatsPrevMinRxNullCells,
       "hcxStatsPrevMinUncorFecHec": hcxStatsPrevMinUncorFecHec,
       "hcxStatsPrevMinCorrectedFec": hcxStatsPrevMinCorrectedFec,
       "hcxStatsCurrMinMeanSignal": hcxStatsCurrMinMeanSignal,
       "hcxStatsPrevMinMeanSignal": hcxStatsPrevMinMeanSignal,
       "hcxStatsClearStats": hcxStatsClearStats,
       "com21HcxRpmIPortGroup": com21HcxRpmIPortGroup,
       "com21HcxRpmIPortTable": com21HcxRpmIPortTable,
       "com21HcxRpmIPortEntry": com21HcxRpmIPortEntry,
       "hcxRpmIPortShelfId": hcxRpmIPortShelfId,
       "hcxRpmIPortSlotId": hcxRpmIPortSlotId,
       "hcxRpmRxPortId": hcxRpmRxPortId,
       "hcxRpmIPortId": hcxRpmIPortId,
       "hcxRpmIPortRecvPower": hcxRpmIPortRecvPower,
       "hcxRpmIPortConfigState": hcxRpmIPortConfigState,
       "hcxRpmIPortContSchedType": hcxRpmIPortContSchedType,
       "com21HcxRpmStatsGroup": com21HcxRpmStatsGroup,
       "com21HcxRpmStatsTable": com21HcxRpmStatsTable,
       "com21HcxRpmStatsEntry": com21HcxRpmStatsEntry,
       "hcxStatsRpmShelfId": hcxStatsRpmShelfId,
       "hcxStatsRpmSlotId": hcxStatsRpmSlotId,
       "hcxStatsRxPortId": hcxStatsRxPortId,
       "hcxStatsRpmIPortId": hcxStatsRpmIPortId,
       "hcxRpmCurrMinRxCells": hcxRpmCurrMinRxCells,
       "hcxRpmCurrMinRxNullCells": hcxRpmCurrMinRxNullCells,
       "hcxRpmCurrMinUncorFecHecCells": hcxRpmCurrMinUncorFecHecCells,
       "hcxRpmCurrMinCorrectedFec": hcxRpmCurrMinCorrectedFec,
       "hcxRpmCurrMeanNoise": hcxRpmCurrMeanNoise,
       "hcxRpmCurrMinNoise": hcxRpmCurrMinNoise,
       "hcxRpmCurrMaxNoise": hcxRpmCurrMaxNoise,
       "hcxRpmRealTimeMeanNoise": hcxRpmRealTimeMeanNoise,
       "hcxRpmRealTimeMinNoise": hcxRpmRealTimeMinNoise,
       "hcxRpmRealTimeMaxNoise": hcxRpmRealTimeMaxNoise,
       "hcxRpmPrevMinRxCells": hcxRpmPrevMinRxCells,
       "hcxRpmPrevMinRxNullCells": hcxRpmPrevMinRxNullCells,
       "hcxRpmPrevMinUncorFecHecCells": hcxRpmPrevMinUncorFecHecCells,
       "hcxRpmPrevMinCorrectedFec": hcxRpmPrevMinCorrectedFec,
       "hcxRpmPrevMeanNoise": hcxRpmPrevMeanNoise,
       "hcxRpmPrevMinNoise": hcxRpmPrevMinNoise,
       "hcxRpmPrevMaxNoise": hcxRpmPrevMaxNoise,
       "hcxRpmCorrFecRatioThres": hcxRpmCorrFecRatioThres,
       "hcxRpmCellErrRatioThres": hcxRpmCellErrRatioThres,
       "hcxRpmRatioThresPeriod": hcxRpmRatioThresPeriod,
       "hcxRpmMinErrRatioCells": hcxRpmMinErrRatioCells,
       "hcxRpmCnrThres": hcxRpmCnrThres,
       "hcxRpmClearStats": hcxRpmClearStats,
       "com21HcxRfAnalysisGroup": com21HcxRfAnalysisGroup,
       "com21HcxRfAnalysisTable": com21HcxRfAnalysisTable,
       "com21HcxRfAnalysisEntry": com21HcxRfAnalysisEntry,
       "hcxRfAnalysisShelfId": hcxRfAnalysisShelfId,
       "hcxRfAnalysisSlotId": hcxRfAnalysisSlotId,
       "hcxRfAnalysisPortId": hcxRfAnalysisPortId,
       "hcxRfAnalysisRpmPortId": hcxRfAnalysisRpmPortId,
       "hcxRfAnalysisControl": hcxRfAnalysisControl,
       "hcxRfAnalysisPoint1": hcxRfAnalysisPoint1,
       "hcxRfAnalysisPoint2": hcxRfAnalysisPoint2,
       "hcxRfAnalysisPoint3": hcxRfAnalysisPoint3,
       "hcxRfAnalysisPoint4": hcxRfAnalysisPoint4,
       "hcxRfAnalysisBin1Count": hcxRfAnalysisBin1Count,
       "hcxRfAnalysisBin2Count": hcxRfAnalysisBin2Count,
       "hcxRfAnalysisBin3Count": hcxRfAnalysisBin3Count,
       "hcxRfAnalysisClearCount": hcxRfAnalysisClearCount,
       "hcxUpstreamUnitPrimStateChange": hcxUpstreamUnitPrimStateChange,
       "hcxUpstreamUnitSecStateChange": hcxUpstreamUnitSecStateChange,
       "hcxUpDiagTestComplete": hcxUpDiagTestComplete,
       "hcxUpTestStatusLedChange": hcxUpTestStatusLedChange,
       "hcxUpFaultStatusLedChange": hcxUpFaultStatusLedChange,
       "hcxUpOperationFailure": hcxUpOperationFailure,
       "hcxUncorFecHecMinThres": hcxUncorFecHecMinThres,
       "hcxCorrectedFecMinThres": hcxCorrectedFecMinThres,
       "hcxCorrFecRatioThres": hcxCorrFecRatioThres,
       "hcxCellErrRatioThres": hcxCellErrRatioThres,
       "hcxRxFreqHop": hcxRxFreqHop,
       "hcxCnrThres": hcxCnrThres,
       "hcxRpmFecRatioThres": hcxRpmFecRatioThres,
       "hcxRpmCellErrRatioThresTrap": hcxRpmCellErrRatioThresTrap,
       "hcxRpmCnrThresTrap": hcxRpmCnrThresTrap,
       "hcxRpmInvalidPhyConfig": hcxRpmInvalidPhyConfig,
       "hcxRpmInvalidConfClear": hcxRpmInvalidConfClear,
       "hcxRpmTimingFault": hcxRpmTimingFault,
       "hcxRpmTimingFaultClear": hcxRpmTimingFaultClear,
       "hcxRpmLinkError": hcxRpmLinkError,
       "hcxRpmLinkErrClear": hcxRpmLinkErrClear,
       "hcxUpstrmRpmPrimStateChange": hcxUpstrmRpmPrimStateChange}
)

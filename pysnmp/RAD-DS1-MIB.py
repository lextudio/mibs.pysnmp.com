# SNMP MIB module (RAD-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAD-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:12 2024
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

(ifAlias,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(alarmSeverity,
 alarmState,
 diverseIfWanGen) = mibBuilder.importSymbols(
    "RAD-MIB",
    "alarmSeverity",
    "alarmState",
    "diverseIfWanGen")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ds1Interface_ObjectIdentity = ObjectIdentity
ds1Interface = _Ds1Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4)
)
_PrtDS1Events_ObjectIdentity = ObjectIdentity
prtDS1Events = _PrtDS1Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0)
)
_PrtDs1PerfHistory_ObjectIdentity = ObjectIdentity
prtDs1PerfHistory = _PrtDs1PerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1)
)
_Dsx1XCurrentTable_Object = MibTable
dsx1XCurrentTable = _Dsx1XCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    dsx1XCurrentTable.setStatus("current")
_Dsx1XCurrentEntry_Object = MibTableRow
dsx1XCurrentEntry = _Dsx1XCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1)
)
dsx1XCurrentEntry.setIndexNames(
    (0, "RAD-DS1-MIB", "dsx1CurrentIndex"),
)
if mibBuilder.loadTexts:
    dsx1XCurrentEntry.setStatus("current")
_Dsx1CurrentLOS_Type = PerfCurrentCount
_Dsx1CurrentLOS_Object = MibTableColumn
dsx1CurrentLOS = _Dsx1CurrentLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 1),
    _Dsx1CurrentLOS_Type()
)
dsx1CurrentLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOS.setStatus("current")
_Dsx1CurrentLOF_Type = PerfCurrentCount
_Dsx1CurrentLOF_Object = MibTableColumn
dsx1CurrentLOF = _Dsx1CurrentLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 2),
    _Dsx1CurrentLOF_Type()
)
dsx1CurrentLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOF.setStatus("current")
_Dsx1CurrentLOC_Type = PerfCurrentCount
_Dsx1CurrentLOC_Object = MibTableColumn
dsx1CurrentLOC = _Dsx1CurrentLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 3),
    _Dsx1CurrentLOC_Type()
)
dsx1CurrentLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOC.setStatus("current")
_Dsx1CurrentAIS_Type = PerfCurrentCount
_Dsx1CurrentAIS_Object = MibTableColumn
dsx1CurrentAIS = _Dsx1CurrentAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 4),
    _Dsx1CurrentAIS_Type()
)
dsx1CurrentAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentAIS.setStatus("current")
_Dsx1CurrentRAI_Type = PerfCurrentCount
_Dsx1CurrentRAI_Object = MibTableColumn
dsx1CurrentRAI = _Dsx1CurrentRAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 5),
    _Dsx1CurrentRAI_Type()
)
dsx1CurrentRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentRAI.setStatus("current")
_Dsx1CurrentLOMF_Type = PerfCurrentCount
_Dsx1CurrentLOMF_Object = MibTableColumn
dsx1CurrentLOMF = _Dsx1CurrentLOMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 6),
    _Dsx1CurrentLOMF_Type()
)
dsx1CurrentLOMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOMF.setStatus("current")
_Dsx1CurrentFEBE_Type = PerfCurrentCount
_Dsx1CurrentFEBE_Object = MibTableColumn
dsx1CurrentFEBE = _Dsx1CurrentFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 7),
    _Dsx1CurrentFEBE_Type()
)
dsx1CurrentFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentFEBE.setStatus("current")


class _Dsx1CurrentStatus_Type(OctetString):
    """Custom type dsx1CurrentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dsx1CurrentStatus_Type.__name__ = "OctetString"
_Dsx1CurrentStatus_Object = MibTableColumn
dsx1CurrentStatus = _Dsx1CurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 8),
    _Dsx1CurrentStatus_Type()
)
dsx1CurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentStatus.setStatus("current")
_Dsx1CurrentBPV_Type = PerfCurrentCount
_Dsx1CurrentBPV_Object = MibTableColumn
dsx1CurrentBPV = _Dsx1CurrentBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 9),
    _Dsx1CurrentBPV_Type()
)
dsx1CurrentBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentBPV.setStatus("current")
_Dsx1CurrentLOCRCMF_Type = PerfCurrentCount
_Dsx1CurrentLOCRCMF_Object = MibTableColumn
dsx1CurrentLOCRCMF = _Dsx1CurrentLOCRCMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 10),
    _Dsx1CurrentLOCRCMF_Type()
)
dsx1CurrentLOCRCMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOCRCMF.setStatus("current")
_Dsx1CurrentLOFC_Type = PerfCurrentCount
_Dsx1CurrentLOFC_Object = MibTableColumn
dsx1CurrentLOFC = _Dsx1CurrentLOFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 11),
    _Dsx1CurrentLOFC_Type()
)
dsx1CurrentLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOFC.setStatus("current")
_Dsx1CurrentCRCErrors_Type = PerfCurrentCount
_Dsx1CurrentCRCErrors_Object = MibTableColumn
dsx1CurrentCRCErrors = _Dsx1CurrentCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 12),
    _Dsx1CurrentCRCErrors_Type()
)
dsx1CurrentCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentCRCErrors.setStatus("current")
_Dsx1XIntervalTable_Object = MibTable
dsx1XIntervalTable = _Dsx1XIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3)
)
if mibBuilder.loadTexts:
    dsx1XIntervalTable.setStatus("current")
_Dsx1XIntervalEntry_Object = MibTableRow
dsx1XIntervalEntry = _Dsx1XIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1)
)
dsx1XIntervalEntry.setIndexNames(
    (0, "RAD-DS1-MIB", "dsx1IntervalIndex"),
    (0, "RAD-DS1-MIB", "dsx1IntervalNumber"),
)
if mibBuilder.loadTexts:
    dsx1XIntervalEntry.setStatus("current")
_Dsx1IntervalLOS_Type = PerfIntervalCount
_Dsx1IntervalLOS_Object = MibTableColumn
dsx1IntervalLOS = _Dsx1IntervalLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 1),
    _Dsx1IntervalLOS_Type()
)
dsx1IntervalLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOS.setStatus("current")
_Dsx1IntervalLOF_Type = PerfIntervalCount
_Dsx1IntervalLOF_Object = MibTableColumn
dsx1IntervalLOF = _Dsx1IntervalLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 2),
    _Dsx1IntervalLOF_Type()
)
dsx1IntervalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOF.setStatus("current")
_Dsx1IntervalLOC_Type = PerfIntervalCount
_Dsx1IntervalLOC_Object = MibTableColumn
dsx1IntervalLOC = _Dsx1IntervalLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 3),
    _Dsx1IntervalLOC_Type()
)
dsx1IntervalLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOC.setStatus("current")
_Dsx1IntervalAIS_Type = PerfIntervalCount
_Dsx1IntervalAIS_Object = MibTableColumn
dsx1IntervalAIS = _Dsx1IntervalAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 4),
    _Dsx1IntervalAIS_Type()
)
dsx1IntervalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalAIS.setStatus("current")
_Dsx1IntervalRAI_Type = PerfIntervalCount
_Dsx1IntervalRAI_Object = MibTableColumn
dsx1IntervalRAI = _Dsx1IntervalRAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 5),
    _Dsx1IntervalRAI_Type()
)
dsx1IntervalRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalRAI.setStatus("current")
_Dsx1IntervalLOMF_Type = PerfIntervalCount
_Dsx1IntervalLOMF_Object = MibTableColumn
dsx1IntervalLOMF = _Dsx1IntervalLOMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 6),
    _Dsx1IntervalLOMF_Type()
)
dsx1IntervalLOMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOMF.setStatus("current")
_Dsx1IntervalFEBE_Type = PerfIntervalCount
_Dsx1IntervalFEBE_Object = MibTableColumn
dsx1IntervalFEBE = _Dsx1IntervalFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 7),
    _Dsx1IntervalFEBE_Type()
)
dsx1IntervalFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalFEBE.setStatus("current")


class _Dsx1IntervalStatus_Type(OctetString):
    """Custom type dsx1IntervalStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dsx1IntervalStatus_Type.__name__ = "OctetString"
_Dsx1IntervalStatus_Object = MibTableColumn
dsx1IntervalStatus = _Dsx1IntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 8),
    _Dsx1IntervalStatus_Type()
)
dsx1IntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalStatus.setStatus("current")
_Dsx1IntervalBPV_Type = PerfIntervalCount
_Dsx1IntervalBPV_Object = MibTableColumn
dsx1IntervalBPV = _Dsx1IntervalBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 9),
    _Dsx1IntervalBPV_Type()
)
dsx1IntervalBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalBPV.setStatus("current")
_Dsx1IntervalLOCRCMF_Type = PerfIntervalCount
_Dsx1IntervalLOCRCMF_Object = MibTableColumn
dsx1IntervalLOCRCMF = _Dsx1IntervalLOCRCMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 10),
    _Dsx1IntervalLOCRCMF_Type()
)
dsx1IntervalLOCRCMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOCRCMF.setStatus("current")
_Dsx1IntervalLOFC_Type = PerfIntervalCount
_Dsx1IntervalLOFC_Object = MibTableColumn
dsx1IntervalLOFC = _Dsx1IntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 11),
    _Dsx1IntervalLOFC_Type()
)
dsx1IntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOFC.setStatus("current")
_Dsx1XTotalTable_Object = MibTable
dsx1XTotalTable = _Dsx1XTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4)
)
if mibBuilder.loadTexts:
    dsx1XTotalTable.setStatus("current")
_Dsx1XTotalEntry_Object = MibTableRow
dsx1XTotalEntry = _Dsx1XTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1)
)
dsx1XTotalEntry.setIndexNames(
    (0, "RAD-DS1-MIB", "dsx1TotalIndex"),
)
if mibBuilder.loadTexts:
    dsx1XTotalEntry.setStatus("current")
_Dsx1TotalLOS_Type = PerfTotalCount
_Dsx1TotalLOS_Object = MibTableColumn
dsx1TotalLOS = _Dsx1TotalLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 1),
    _Dsx1TotalLOS_Type()
)
dsx1TotalLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalLOS.setStatus("current")
_Dsx1TotalBPV_Type = PerfTotalCount
_Dsx1TotalBPV_Object = MibTableColumn
dsx1TotalBPV = _Dsx1TotalBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 9),
    _Dsx1TotalBPV_Type()
)
dsx1TotalBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalBPV.setStatus("current")
_Dsx1TotalLOFC_Type = PerfTotalCount
_Dsx1TotalLOFC_Object = MibTableColumn
dsx1TotalLOFC = _Dsx1TotalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 11),
    _Dsx1TotalLOFC_Type()
)
dsx1TotalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalLOFC.setStatus("current")
_Dsx1DataStreamStatTable_Object = MibTable
dsx1DataStreamStatTable = _Dsx1DataStreamStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5)
)
if mibBuilder.loadTexts:
    dsx1DataStreamStatTable.setStatus("current")
_Dsx1DataStreamStatEntry_Object = MibTableRow
dsx1DataStreamStatEntry = _Dsx1DataStreamStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1)
)
dsx1DataStreamStatEntry.setIndexNames(
    (0, "RAD-DS1-MIB", "dsx1DataStreamStatIfIndex"),
    (0, "RAD-DS1-MIB", "dsx1DataStreamStatIndex"),
)
if mibBuilder.loadTexts:
    dsx1DataStreamStatEntry.setStatus("current")
_Dsx1DataStreamStatIfIndex_Type = Integer32
_Dsx1DataStreamStatIfIndex_Object = MibTableColumn
dsx1DataStreamStatIfIndex = _Dsx1DataStreamStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 1),
    _Dsx1DataStreamStatIfIndex_Type()
)
dsx1DataStreamStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsx1DataStreamStatIfIndex.setStatus("current")
_Dsx1DataStreamStatIndex_Type = Integer32
_Dsx1DataStreamStatIndex_Object = MibTableColumn
dsx1DataStreamStatIndex = _Dsx1DataStreamStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 2),
    _Dsx1DataStreamStatIndex_Type()
)
dsx1DataStreamStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsx1DataStreamStatIndex.setStatus("current")
_Dsx1DataStreamStatValid_Type = TruthValue
_Dsx1DataStreamStatValid_Object = MibTableColumn
dsx1DataStreamStatValid = _Dsx1DataStreamStatValid_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 3),
    _Dsx1DataStreamStatValid_Type()
)
dsx1DataStreamStatValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatValid.setStatus("current")
_Dsx1DataStreamStatInFrames_Type = Counter32
_Dsx1DataStreamStatInFrames_Object = MibTableColumn
dsx1DataStreamStatInFrames = _Dsx1DataStreamStatInFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 4),
    _Dsx1DataStreamStatInFrames_Type()
)
dsx1DataStreamStatInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatInFrames.setStatus("current")
_Dsx1DataStreamStatInBytes_Type = Counter32
_Dsx1DataStreamStatInBytes_Object = MibTableColumn
dsx1DataStreamStatInBytes = _Dsx1DataStreamStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 5),
    _Dsx1DataStreamStatInBytes_Type()
)
dsx1DataStreamStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatInBytes.setStatus("current")
_Dsx1DataStreamStatInDiscards_Type = Counter32
_Dsx1DataStreamStatInDiscards_Object = MibTableColumn
dsx1DataStreamStatInDiscards = _Dsx1DataStreamStatInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 6),
    _Dsx1DataStreamStatInDiscards_Type()
)
dsx1DataStreamStatInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatInDiscards.setStatus("current")
_Dsx1DataStreamStatInErrors_Type = Counter32
_Dsx1DataStreamStatInErrors_Object = MibTableColumn
dsx1DataStreamStatInErrors = _Dsx1DataStreamStatInErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 7),
    _Dsx1DataStreamStatInErrors_Type()
)
dsx1DataStreamStatInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatInErrors.setStatus("current")
_Dsx1DataStreamStatOutFrames_Type = Counter32
_Dsx1DataStreamStatOutFrames_Object = MibTableColumn
dsx1DataStreamStatOutFrames = _Dsx1DataStreamStatOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 8),
    _Dsx1DataStreamStatOutFrames_Type()
)
dsx1DataStreamStatOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatOutFrames.setStatus("current")
_Dsx1DataStreamStatOutBytes_Type = Counter32
_Dsx1DataStreamStatOutBytes_Object = MibTableColumn
dsx1DataStreamStatOutBytes = _Dsx1DataStreamStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 9),
    _Dsx1DataStreamStatOutBytes_Type()
)
dsx1DataStreamStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatOutBytes.setStatus("current")
_Dsx1DataStreamStatOutDiscards_Type = Counter32
_Dsx1DataStreamStatOutDiscards_Object = MibTableColumn
dsx1DataStreamStatOutDiscards = _Dsx1DataStreamStatOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 10),
    _Dsx1DataStreamStatOutDiscards_Type()
)
dsx1DataStreamStatOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatOutDiscards.setStatus("current")
_Dsx1XConfigTable_Object = MibTable
dsx1XConfigTable = _Dsx1XConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    dsx1XConfigTable.setStatus("current")
_Dsx1XConfigEntry_Object = MibTableRow
dsx1XConfigEntry = _Dsx1XConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1)
)
dsx1XConfigEntry.setIndexNames(
    (0, "RAD-DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    dsx1XConfigEntry.setStatus("current")
_Dsx1IdleCode_Type = Integer32
_Dsx1IdleCode_Object = MibTableColumn
dsx1IdleCode = _Dsx1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 1),
    _Dsx1IdleCode_Type()
)
dsx1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1IdleCode.setStatus("current")


class _Dsx1LineMode_Type(Integer32):
    """Custom type dsx1LineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csu", 1),
          ("dsu", 2))
    )


_Dsx1LineMode_Type.__name__ = "Integer32"
_Dsx1LineMode_Object = MibTableColumn
dsx1LineMode = _Dsx1LineMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 2),
    _Dsx1LineMode_Type()
)
dsx1LineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LineMode.setStatus("current")


class _Dsx1dBTxGain_Type(Integer32):
    """Custom type dsx1dBTxGain based on Integer32"""
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
        *(("neg15dB", 3),
          ("neg225dB", 4),
          ("neg75dB", 2),
          ("notApplicable", 1),
          ("zerodB", 5))
    )


_Dsx1dBTxGain_Type.__name__ = "Integer32"
_Dsx1dBTxGain_Object = MibTableColumn
dsx1dBTxGain = _Dsx1dBTxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 3),
    _Dsx1dBTxGain_Type()
)
dsx1dBTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1dBTxGain.setStatus("current")


class _Dsx1RxSensitivity_Type(Integer32):
    """Custom type dsx1RxSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("neg10dB", 2),
          ("neg32dB", 3),
          ("notApplicable", 1))
    )


_Dsx1RxSensitivity_Type.__name__ = "Integer32"
_Dsx1RxSensitivity_Object = MibTableColumn
dsx1RxSensitivity = _Dsx1RxSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 4),
    _Dsx1RxSensitivity_Type()
)
dsx1RxSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1RxSensitivity.setStatus("current")


class _Dsx1RestoreTime_Type(Integer32):
    """Custom type dsx1RestoreTime based on Integer32"""
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
        *(("immediate", 4),
          ("other", 1),
          ("sec1", 2),
          ("sec10", 3))
    )


_Dsx1RestoreTime_Type.__name__ = "Integer32"
_Dsx1RestoreTime_Object = MibTableColumn
dsx1RestoreTime = _Dsx1RestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 5),
    _Dsx1RestoreTime_Type()
)
dsx1RestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1RestoreTime.setStatus("current")
_Dsx1TcFirstSignal_Type = Integer32
_Dsx1TcFirstSignal_Object = MibTableColumn
dsx1TcFirstSignal = _Dsx1TcFirstSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 6),
    _Dsx1TcFirstSignal_Type()
)
dsx1TcFirstSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TcFirstSignal.setStatus("current")
_Dsx1TcSignal_Type = Integer32
_Dsx1TcSignal_Object = MibTableColumn
dsx1TcSignal = _Dsx1TcSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 7),
    _Dsx1TcSignal_Type()
)
dsx1TcSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TcSignal.setStatus("current")
_Dsx1TcPattern_Type = Integer32
_Dsx1TcPattern_Object = MibTableColumn
dsx1TcPattern = _Dsx1TcPattern_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 8),
    _Dsx1TcPattern_Type()
)
dsx1TcPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TcPattern.setStatus("current")


class _Dsx1Scramble_Type(Integer32):
    """Custom type dsx1Scramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("notActive", 2),
          ("notApplicable", 1))
    )


_Dsx1Scramble_Type.__name__ = "Integer32"
_Dsx1Scramble_Object = MibTableColumn
dsx1Scramble = _Dsx1Scramble_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 9),
    _Dsx1Scramble_Type()
)
dsx1Scramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1Scramble.setStatus("current")


class _Dsx1LineAdaptiveTimingMode_Type(Integer32):
    """Custom type dsx1LineAdaptiveTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Dsx1LineAdaptiveTimingMode_Type.__name__ = "Integer32"
_Dsx1LineAdaptiveTimingMode_Object = MibTableColumn
dsx1LineAdaptiveTimingMode = _Dsx1LineAdaptiveTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 10),
    _Dsx1LineAdaptiveTimingMode_Type()
)
dsx1LineAdaptiveTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LineAdaptiveTimingMode.setStatus("current")


class _Dsx1TxClockSource_Type(Integer32):
    """Custom type dsx1TxClockSource based on Integer32"""
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
        *(("adaptive", 4),
          ("localTiming", 2),
          ("loopTiming", 1),
          ("throughTiming", 3))
    )


_Dsx1TxClockSource_Type.__name__ = "Integer32"
_Dsx1TxClockSource_Object = MibTableColumn
dsx1TxClockSource = _Dsx1TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 11),
    _Dsx1TxClockSource_Type()
)
dsx1TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TxClockSource.setStatus("current")


class _Dsx1AisEnable_Type(Integer32):
    """Custom type dsx1AisEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("notApplicable", 1))
    )


_Dsx1AisEnable_Type.__name__ = "Integer32"
_Dsx1AisEnable_Object = MibTableColumn
dsx1AisEnable = _Dsx1AisEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 12),
    _Dsx1AisEnable_Type()
)
dsx1AisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1AisEnable.setStatus("current")


class _Dsx1TsEchoCancel_Type(OctetString):
    """Custom type dsx1TsEchoCancel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Dsx1TsEchoCancel_Type.__name__ = "OctetString"
_Dsx1TsEchoCancel_Object = MibTableColumn
dsx1TsEchoCancel = _Dsx1TsEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 13),
    _Dsx1TsEchoCancel_Type()
)
dsx1TsEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TsEchoCancel.setStatus("current")


class _Dsx1EchoCancelerModule_Type(Integer32):
    """Custom type dsx1EchoCancelerModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exist", 3),
          ("notExist", 2))
    )


_Dsx1EchoCancelerModule_Type.__name__ = "Integer32"
_Dsx1EchoCancelerModule_Object = MibTableColumn
dsx1EchoCancelerModule = _Dsx1EchoCancelerModule_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 14),
    _Dsx1EchoCancelerModule_Type()
)
dsx1EchoCancelerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EchoCancelerModule.setStatus("current")


class _Dsx1PortFunction_Type(Integer32):
    """Custom type dsx1PortFunction based on Integer32"""
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
        *(("ces", 3),
          ("ima", 4),
          ("notApplicable", 1),
          ("uni", 2))
    )


_Dsx1PortFunction_Type.__name__ = "Integer32"
_Dsx1PortFunction_Object = MibTableColumn
dsx1PortFunction = _Dsx1PortFunction_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 15),
    _Dsx1PortFunction_Type()
)
dsx1PortFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PortFunction.setStatus("current")


class _Dsx1PortMultiplier_Type(Integer32):
    """Custom type dsx1PortMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("r56", 2),
          ("r64", 3))
    )


_Dsx1PortMultiplier_Type.__name__ = "Integer32"
_Dsx1PortMultiplier_Object = MibTableColumn
dsx1PortMultiplier = _Dsx1PortMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 16),
    _Dsx1PortMultiplier_Type()
)
dsx1PortMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PortMultiplier.setStatus("current")


class _Dsx1LeasedLine_Type(Integer32):
    """Custom type dsx1LeasedLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("notApplicable", 1))
    )


_Dsx1LeasedLine_Type.__name__ = "Integer32"
_Dsx1LeasedLine_Object = MibTableColumn
dsx1LeasedLine = _Dsx1LeasedLine_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 17),
    _Dsx1LeasedLine_Type()
)
dsx1LeasedLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LeasedLine.setStatus("current")


class _Dsx1CsuLoop_Type(Integer32):
    """Custom type dsx1CsuLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("notApplicable", 1),
          ("transparent", 3))
    )


_Dsx1CsuLoop_Type.__name__ = "Integer32"
_Dsx1CsuLoop_Object = MibTableColumn
dsx1CsuLoop = _Dsx1CsuLoop_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 18),
    _Dsx1CsuLoop_Type()
)
dsx1CsuLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1CsuLoop.setStatus("current")
_Dsx1ClockSource_Type = Integer32
_Dsx1ClockSource_Object = MibTableColumn
dsx1ClockSource = _Dsx1ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 19),
    _Dsx1ClockSource_Type()
)
dsx1ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ClockSource.setStatus("current")


class _Dsx1OosSignal_Type(Integer32):
    """Custom type dsx1OosSignal based on Integer32"""
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
        *(("mark", 3),
          ("markSpace", 5),
          ("notApplicable", 1),
          ("space", 2),
          ("spaceMark", 4))
    )


_Dsx1OosSignal_Type.__name__ = "Integer32"
_Dsx1OosSignal_Object = MibTableColumn
dsx1OosSignal = _Dsx1OosSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 20),
    _Dsx1OosSignal_Type()
)
dsx1OosSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1OosSignal.setStatus("current")

# Managed Objects groups


# Notification objects

ds1LocalMultiframeAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 1)
)
ds1LocalMultiframeAlarmTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1LocalMultiframeAlarmTrap.setStatus(
        "current"
    )

ds1RemoteMultiframeAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 2)
)
ds1RemoteMultiframeAlarmTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1RemoteMultiframeAlarmTrap.setStatus(
        "current"
    )

ds1LinkFrameSlipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 3)
)
ds1LinkFrameSlipTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1LinkFrameSlipTrap.setStatus(
        "current"
    )

ds1BpvErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 4)
)
ds1BpvErrorTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1BpvErrorTrap.setStatus(
        "current"
    )

ds1ExcessiveBpvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 5)
)
ds1ExcessiveBpvTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveBpvTrap.setStatus(
        "current"
    )

ds1Crc4ErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 6)
)
ds1Crc4ErrorTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1Crc4ErrorTrap.setStatus(
        "current"
    )

ds1ExcessiveErrorRatioTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 7)
)
ds1ExcessiveErrorRatioTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveErrorRatioTrap.setStatus(
        "current"
    )

ds1RemoteSyncLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 8)
)
ds1RemoteSyncLossTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1RemoteSyncLossTrap.setStatus(
        "current"
    )

ds1LocalSyncLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 9)
)
ds1LocalSyncLossTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1LocalSyncLossTrap.setStatus(
        "current"
    )

ds1AisSyncLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 10)
)
ds1AisSyncLossTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1AisSyncLossTrap.setStatus(
        "current"
    )

ds1AisTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 11)
)
ds1AisTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1AisTrap.setStatus(
        "current"
    )

ds1NetworkRemoteLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 12)
)
ds1NetworkRemoteLoopTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1NetworkRemoteLoopTrap.setStatus(
        "current"
    )

ds1RemoteLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 13)
)
ds1RemoteLoopTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1RemoteLoopTrap.setStatus(
        "current"
    )

ds1LocalLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 14)
)
ds1LocalLoopTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1LocalLoopTrap.setStatus(
        "current"
    )

ds1ExcessiveFrameSlipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 15)
)
ds1ExcessiveFrameSlipTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveFrameSlipTrap.setStatus(
        "current"
    )

ds1ExcessiveCrc4ErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 16)
)
ds1ExcessiveCrc4ErrorTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveCrc4ErrorTrap.setStatus(
        "current"
    )

ds1ExcessiveLocalMfAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 17)
)
ds1ExcessiveLocalMfAlarmTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveLocalMfAlarmTrap.setStatus(
        "current"
    )

ds1ExcessiveRemoteMfAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 18)
)
ds1ExcessiveRemoteMfAlarmTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveRemoteMfAlarmTrap.setStatus(
        "current"
    )

ds1ExcessiveRemoteSyncLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 19)
)
ds1ExcessiveRemoteSyncLossTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveRemoteSyncLossTrap.setStatus(
        "current"
    )

ds1ExcessiveLocalSyncLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 20)
)
ds1ExcessiveLocalSyncLossTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveLocalSyncLossTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-DS1-MIB",
    **{"ds1Interface": ds1Interface,
       "prtDS1Events": prtDS1Events,
       "ds1LocalMultiframeAlarmTrap": ds1LocalMultiframeAlarmTrap,
       "ds1RemoteMultiframeAlarmTrap": ds1RemoteMultiframeAlarmTrap,
       "ds1LinkFrameSlipTrap": ds1LinkFrameSlipTrap,
       "ds1BpvErrorTrap": ds1BpvErrorTrap,
       "ds1ExcessiveBpvTrap": ds1ExcessiveBpvTrap,
       "ds1Crc4ErrorTrap": ds1Crc4ErrorTrap,
       "ds1ExcessiveErrorRatioTrap": ds1ExcessiveErrorRatioTrap,
       "ds1RemoteSyncLossTrap": ds1RemoteSyncLossTrap,
       "ds1LocalSyncLossTrap": ds1LocalSyncLossTrap,
       "ds1AisSyncLossTrap": ds1AisSyncLossTrap,
       "ds1AisTrap": ds1AisTrap,
       "ds1NetworkRemoteLoopTrap": ds1NetworkRemoteLoopTrap,
       "ds1RemoteLoopTrap": ds1RemoteLoopTrap,
       "ds1LocalLoopTrap": ds1LocalLoopTrap,
       "ds1ExcessiveFrameSlipTrap": ds1ExcessiveFrameSlipTrap,
       "ds1ExcessiveCrc4ErrorTrap": ds1ExcessiveCrc4ErrorTrap,
       "ds1ExcessiveLocalMfAlarmTrap": ds1ExcessiveLocalMfAlarmTrap,
       "ds1ExcessiveRemoteMfAlarmTrap": ds1ExcessiveRemoteMfAlarmTrap,
       "ds1ExcessiveRemoteSyncLossTrap": ds1ExcessiveRemoteSyncLossTrap,
       "ds1ExcessiveLocalSyncLossTrap": ds1ExcessiveLocalSyncLossTrap,
       "prtDs1PerfHistory": prtDs1PerfHistory,
       "dsx1XCurrentTable": dsx1XCurrentTable,
       "dsx1XCurrentEntry": dsx1XCurrentEntry,
       "dsx1CurrentLOS": dsx1CurrentLOS,
       "dsx1CurrentLOF": dsx1CurrentLOF,
       "dsx1CurrentLOC": dsx1CurrentLOC,
       "dsx1CurrentAIS": dsx1CurrentAIS,
       "dsx1CurrentRAI": dsx1CurrentRAI,
       "dsx1CurrentLOMF": dsx1CurrentLOMF,
       "dsx1CurrentFEBE": dsx1CurrentFEBE,
       "dsx1CurrentStatus": dsx1CurrentStatus,
       "dsx1CurrentBPV": dsx1CurrentBPV,
       "dsx1CurrentLOCRCMF": dsx1CurrentLOCRCMF,
       "dsx1CurrentLOFC": dsx1CurrentLOFC,
       "dsx1CurrentCRCErrors": dsx1CurrentCRCErrors,
       "dsx1XIntervalTable": dsx1XIntervalTable,
       "dsx1XIntervalEntry": dsx1XIntervalEntry,
       "dsx1IntervalLOS": dsx1IntervalLOS,
       "dsx1IntervalLOF": dsx1IntervalLOF,
       "dsx1IntervalLOC": dsx1IntervalLOC,
       "dsx1IntervalAIS": dsx1IntervalAIS,
       "dsx1IntervalRAI": dsx1IntervalRAI,
       "dsx1IntervalLOMF": dsx1IntervalLOMF,
       "dsx1IntervalFEBE": dsx1IntervalFEBE,
       "dsx1IntervalStatus": dsx1IntervalStatus,
       "dsx1IntervalBPV": dsx1IntervalBPV,
       "dsx1IntervalLOCRCMF": dsx1IntervalLOCRCMF,
       "dsx1IntervalLOFC": dsx1IntervalLOFC,
       "dsx1XTotalTable": dsx1XTotalTable,
       "dsx1XTotalEntry": dsx1XTotalEntry,
       "dsx1TotalLOS": dsx1TotalLOS,
       "dsx1TotalBPV": dsx1TotalBPV,
       "dsx1TotalLOFC": dsx1TotalLOFC,
       "dsx1DataStreamStatTable": dsx1DataStreamStatTable,
       "dsx1DataStreamStatEntry": dsx1DataStreamStatEntry,
       "dsx1DataStreamStatIfIndex": dsx1DataStreamStatIfIndex,
       "dsx1DataStreamStatIndex": dsx1DataStreamStatIndex,
       "dsx1DataStreamStatValid": dsx1DataStreamStatValid,
       "dsx1DataStreamStatInFrames": dsx1DataStreamStatInFrames,
       "dsx1DataStreamStatInBytes": dsx1DataStreamStatInBytes,
       "dsx1DataStreamStatInDiscards": dsx1DataStreamStatInDiscards,
       "dsx1DataStreamStatInErrors": dsx1DataStreamStatInErrors,
       "dsx1DataStreamStatOutFrames": dsx1DataStreamStatOutFrames,
       "dsx1DataStreamStatOutBytes": dsx1DataStreamStatOutBytes,
       "dsx1DataStreamStatOutDiscards": dsx1DataStreamStatOutDiscards,
       "dsx1XConfigTable": dsx1XConfigTable,
       "dsx1XConfigEntry": dsx1XConfigEntry,
       "dsx1IdleCode": dsx1IdleCode,
       "dsx1LineMode": dsx1LineMode,
       "dsx1dBTxGain": dsx1dBTxGain,
       "dsx1RxSensitivity": dsx1RxSensitivity,
       "dsx1RestoreTime": dsx1RestoreTime,
       "dsx1TcFirstSignal": dsx1TcFirstSignal,
       "dsx1TcSignal": dsx1TcSignal,
       "dsx1TcPattern": dsx1TcPattern,
       "dsx1Scramble": dsx1Scramble,
       "dsx1LineAdaptiveTimingMode": dsx1LineAdaptiveTimingMode,
       "dsx1TxClockSource": dsx1TxClockSource,
       "dsx1AisEnable": dsx1AisEnable,
       "dsx1TsEchoCancel": dsx1TsEchoCancel,
       "dsx1EchoCancelerModule": dsx1EchoCancelerModule,
       "dsx1PortFunction": dsx1PortFunction,
       "dsx1PortMultiplier": dsx1PortMultiplier,
       "dsx1LeasedLine": dsx1LeasedLine,
       "dsx1CsuLoop": dsx1CsuLoop,
       "dsx1ClockSource": dsx1ClockSource,
       "dsx1OosSignal": dsx1OosSignal}
)

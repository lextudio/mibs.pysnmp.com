# SNMP MIB module (SPC200) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SPC200
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:19 2024
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

(ifIndex,
 interfaces) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "interfaces")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(spidcom,) = mibBuilder.importSymbols(
    "SPIDCOM-MIB",
    "spidcom")


# MODULE-IDENTITY

spc200MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1)
)
spc200MIB.setRevisions(
        ("2004-12-17 12:30",
         "2004-11-16 12:30",
         "2004-09-21 12:00",
         "2004-09-13 12:00",
         "2004-07-22 12:00",
         "2004-07-01 17:57")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ModulationValue(Integer32, TextualConvention):
    status = "current"
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
        *(("bpsk", 2),
          ("none", 1),
          ("qam16", 4),
          ("qam256", 6),
          ("qam64", 5),
          ("qpsk", 3))
    )



class CarrierValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class PilotValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



class BandValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )



class PlcChannelType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("rxLast", 2),
          ("tx", 3))
    )



class EstimationMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )



class GroupValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class ResultValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("success", 1))
    )



class AdaptValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )



class ChannelBandwidthValue(Integer32, TextualConvention):
    status = "current"


class SoftwareIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )



class SoftwareActionResultValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fileNotExist", 2),
          ("flashCorrupted", 4),
          ("flashExhausted", 3),
          ("genericError", 7),
          ("invalidParameter", 6),
          ("notEnoughMemory", 5),
          ("on-going", 1),
          ("success", 0))
    )



class SoftwareActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remove", 2),
          ("switch", 1))
    )



class PlcModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ad-hoc", 0),
          ("master", 2),
          ("slave", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Plc_ObjectIdentity = ObjectIdentity
plc = _Plc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1)
)
_Stats_ObjectIdentity = ObjectIdentity
stats = _Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1)
)
_PortStatsTable_Object = MibTable
portStatsTable = _PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    portStatsTable.setStatus("current")
_PortStatsEntry_Object = MibTableRow
portStatsEntry = _PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 2, 1)
)
portStatsEntry.setIndexNames(
    (0, "SPC200", "plcBasePortIndex"),
    (0, "SPC200", "portStatsBandIndex"),
    (0, "SPC200", "portStatsGroupIndex"),
    (0, "SPC200", "portStatsCarrierIndex"),
)
if mibBuilder.loadTexts:
    portStatsEntry.setStatus("current")
_PortStatsBandIndex_Type = BandValue
_PortStatsBandIndex_Object = MibTableColumn
portStatsBandIndex = _PortStatsBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 2, 1, 1),
    _PortStatsBandIndex_Type()
)
portStatsBandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portStatsBandIndex.setStatus("current")
_PortStatsGroupIndex_Type = GroupValue
_PortStatsGroupIndex_Object = MibTableColumn
portStatsGroupIndex = _PortStatsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 2, 1, 2),
    _PortStatsGroupIndex_Type()
)
portStatsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portStatsGroupIndex.setStatus("current")
_PortStatsCarrierIndex_Type = CarrierValue
_PortStatsCarrierIndex_Object = MibTableColumn
portStatsCarrierIndex = _PortStatsCarrierIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 2, 1, 3),
    _PortStatsCarrierIndex_Type()
)
portStatsCarrierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portStatsCarrierIndex.setStatus("current")
_PortStatsSignal_Type = Counter32
_PortStatsSignal_Object = MibTableColumn
portStatsSignal = _PortStatsSignal_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 2, 1, 4),
    _PortStatsSignal_Type()
)
portStatsSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsSignal.setStatus("current")
_PortStatsNoise_Type = Counter32
_PortStatsNoise_Object = MibTableColumn
portStatsNoise = _PortStatsNoise_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 2, 1, 5),
    _PortStatsNoise_Type()
)
portStatsNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsNoise.setStatus("current")
_PortStats2Table_Object = MibTable
portStats2Table = _PortStats2Table_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    portStats2Table.setStatus("current")
_PortStats2Entry_Object = MibTableRow
portStats2Entry = _PortStats2Entry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 3, 1)
)
portStats2Entry.setIndexNames(
    (0, "SPC200", "plcBasePortIndex"),
    (0, "SPC200", "plcModBandIndex"),
)
if mibBuilder.loadTexts:
    portStats2Entry.setStatus("current")
_PortStats2Signal_Type = OctetString
_PortStats2Signal_Object = MibTableColumn
portStats2Signal = _PortStats2Signal_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 3, 1, 1),
    _PortStats2Signal_Type()
)
portStats2Signal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStats2Signal.setStatus("current")
_PortStats2Noise_Type = OctetString
_PortStats2Noise_Object = MibTableColumn
portStats2Noise = _PortStats2Noise_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 3, 1, 2),
    _PortStats2Noise_Type()
)
portStats2Noise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStats2Noise.setStatus("current")
_PortStats2AvgBandAtt_Type = Counter32
_PortStats2AvgBandAtt_Object = MibTableColumn
portStats2AvgBandAtt = _PortStats2AvgBandAtt_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 3, 1, 3),
    _PortStats2AvgBandAtt_Type()
)
portStats2AvgBandAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStats2AvgBandAtt.setStatus("current")
_PortStats2AvgBandSNR_Type = Counter32
_PortStats2AvgBandSNR_Object = MibTableColumn
portStats2AvgBandSNR = _PortStats2AvgBandSNR_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 3, 1, 4),
    _PortStats2AvgBandSNR_Type()
)
portStats2AvgBandSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStats2AvgBandSNR.setStatus("current")
_PortStats3Table_Object = MibTable
portStats3Table = _PortStats3Table_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    portStats3Table.setStatus("current")
_PortStats3Entry_Object = MibTableRow
portStats3Entry = _PortStats3Entry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 4, 1)
)
portStats3Entry.setIndexNames(
    (0, "SPC200", "plcBasePortIndex"),
)
if mibBuilder.loadTexts:
    portStats3Entry.setStatus("current")
_PortStats3AvgAtt_Type = Counter32
_PortStats3AvgAtt_Object = MibTableColumn
portStats3AvgAtt = _PortStats3AvgAtt_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 4, 1, 1),
    _PortStats3AvgAtt_Type()
)
portStats3AvgAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStats3AvgAtt.setStatus("current")
_PortStats3AvgSNR_Type = Counter32
_PortStats3AvgSNR_Object = MibTableColumn
portStats3AvgSNR = _PortStats3AvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 4, 1, 2),
    _PortStats3AvgSNR_Type()
)
portStats3AvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStats3AvgSNR.setStatus("current")
_Bootstats_ObjectIdentity = ObjectIdentity
bootstats = _Bootstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    bootstats.setStatus("current")
_BootstatsBoot_Type = Counter32
_BootstatsBoot_Object = MibScalar
bootstatsBoot = _BootstatsBoot_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 5, 1),
    _BootstatsBoot_Type()
)
bootstatsBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootstatsBoot.setStatus("current")
_BootstatsManualReset_Type = Counter32
_BootstatsManualReset_Object = MibScalar
bootstatsManualReset = _BootstatsManualReset_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 5, 2),
    _BootstatsManualReset_Type()
)
bootstatsManualReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootstatsManualReset.setStatus("current")
_BootstatsFailureReset_Type = Counter32
_BootstatsFailureReset_Object = MibScalar
bootstatsFailureReset = _BootstatsFailureReset_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 1, 5, 3),
    _BootstatsFailureReset_Type()
)
bootstatsFailureReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootstatsFailureReset.setStatus("current")
_PlcObjects_ObjectIdentity = ObjectIdentity
plcObjects = _PlcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2)
)
_PlcMode_Type = PlcModeType
_PlcMode_Object = MibScalar
plcMode = _PlcMode_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 1),
    _PlcMode_Type()
)
plcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcMode.setStatus("current")
_PlcTopo_ObjectIdentity = ObjectIdentity
plcTopo = _PlcTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2)
)
_PlcTopoChanges_Type = Counter32
_PlcTopoChanges_Object = MibScalar
plcTopoChanges = _PlcTopoChanges_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 1),
    _PlcTopoChanges_Type()
)
plcTopoChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcTopoChanges.setStatus("current")
_PlcBasePortTable_Object = MibTable
plcBasePortTable = _PlcBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    plcBasePortTable.setStatus("current")
_PlcBasePortEntry_Object = MibTableRow
plcBasePortEntry = _PlcBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 2, 1)
)
plcBasePortEntry.setIndexNames(
    (0, "SPC200", "plcBasePortIndex"),
)
if mibBuilder.loadTexts:
    plcBasePortEntry.setStatus("current")
_PlcBasePortIndex_Type = MacAddress
_PlcBasePortIndex_Object = MibTableColumn
plcBasePortIndex = _PlcBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 2, 1, 1),
    _PlcBasePortIndex_Type()
)
plcBasePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plcBasePortIndex.setStatus("current")
_PlcBasePortAddress_Type = MacAddress
_PlcBasePortAddress_Object = MibTableColumn
plcBasePortAddress = _PlcBasePortAddress_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 2, 1, 2),
    _PlcBasePortAddress_Type()
)
plcBasePortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcBasePortAddress.setStatus("current")
_PlcBasePortChannelEstimation_Type = EstimationMode
_PlcBasePortChannelEstimation_Object = MibTableColumn
plcBasePortChannelEstimation = _PlcBasePortChannelEstimation_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 2, 1, 3),
    _PlcBasePortChannelEstimation_Type()
)
plcBasePortChannelEstimation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcBasePortChannelEstimation.setStatus("current")
_PlcBasePortAttenuation_Type = Counter32
_PlcBasePortAttenuation_Object = MibTableColumn
plcBasePortAttenuation = _PlcBasePortAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 2, 1, 4),
    _PlcBasePortAttenuation_Type()
)
plcBasePortAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcBasePortAttenuation.setStatus("current")
_PlcChannelModulationStringTable_Object = MibTable
plcChannelModulationStringTable = _PlcChannelModulationStringTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    plcChannelModulationStringTable.setStatus("current")
_PlcChannelModulationStringEntry_Object = MibTableRow
plcChannelModulationStringEntry = _PlcChannelModulationStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 3, 1)
)
plcChannelModulationStringEntry.setIndexNames(
    (0, "SPC200", "plcBasePortIndex"),
)
if mibBuilder.loadTexts:
    plcChannelModulationStringEntry.setStatus("current")
_PlcRxChannelModulation_Type = OctetString
_PlcRxChannelModulation_Object = MibTableColumn
plcRxChannelModulation = _PlcRxChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 3, 1, 1),
    _PlcRxChannelModulation_Type()
)
plcRxChannelModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcRxChannelModulation.setStatus("current")
_PlcRxLastChannelModulation_Type = OctetString
_PlcRxLastChannelModulation_Object = MibTableColumn
plcRxLastChannelModulation = _PlcRxLastChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 3, 1, 2),
    _PlcRxLastChannelModulation_Type()
)
plcRxLastChannelModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcRxLastChannelModulation.setStatus("current")
_PlcTxChannelModulation_Type = OctetString
_PlcTxChannelModulation_Object = MibTableColumn
plcTxChannelModulation = _PlcTxChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 3, 1, 3),
    _PlcTxChannelModulation_Type()
)
plcTxChannelModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcTxChannelModulation.setStatus("current")
_PlcChannelModulationTable_Object = MibTable
plcChannelModulationTable = _PlcChannelModulationTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    plcChannelModulationTable.setStatus("current")
_PlcChannelModulationEntry_Object = MibTableRow
plcChannelModulationEntry = _PlcChannelModulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1)
)
plcChannelModulationEntry.setIndexNames(
    (0, "SPC200", "plcBasePortIndex"),
    (0, "SPC200", "plcPortChannelIndex"),
    (0, "SPC200", "plcModBandIndex"),
)
if mibBuilder.loadTexts:
    plcChannelModulationEntry.setStatus("current")
_PlcModBandIndex_Type = BandValue
_PlcModBandIndex_Object = MibTableColumn
plcModBandIndex = _PlcModBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 1),
    _PlcModBandIndex_Type()
)
plcModBandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plcModBandIndex.setStatus("current")
_PlcModGroup1_Type = ModulationValue
_PlcModGroup1_Object = MibTableColumn
plcModGroup1 = _PlcModGroup1_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 2),
    _PlcModGroup1_Type()
)
plcModGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup1.setStatus("current")
_PlcModGroup2_Type = ModulationValue
_PlcModGroup2_Object = MibTableColumn
plcModGroup2 = _PlcModGroup2_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 3),
    _PlcModGroup2_Type()
)
plcModGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup2.setStatus("current")
_PlcModGroup3_Type = ModulationValue
_PlcModGroup3_Object = MibTableColumn
plcModGroup3 = _PlcModGroup3_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 4),
    _PlcModGroup3_Type()
)
plcModGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup3.setStatus("current")
_PlcModGroup4_Type = ModulationValue
_PlcModGroup4_Object = MibTableColumn
plcModGroup4 = _PlcModGroup4_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 5),
    _PlcModGroup4_Type()
)
plcModGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup4.setStatus("current")
_PlcModGroup5_Type = ModulationValue
_PlcModGroup5_Object = MibTableColumn
plcModGroup5 = _PlcModGroup5_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 6),
    _PlcModGroup5_Type()
)
plcModGroup5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup5.setStatus("current")
_PlcModGroup6_Type = ModulationValue
_PlcModGroup6_Object = MibTableColumn
plcModGroup6 = _PlcModGroup6_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 7),
    _PlcModGroup6_Type()
)
plcModGroup6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup6.setStatus("current")
_PlcModGroup7_Type = ModulationValue
_PlcModGroup7_Object = MibTableColumn
plcModGroup7 = _PlcModGroup7_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 8),
    _PlcModGroup7_Type()
)
plcModGroup7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup7.setStatus("current")
_PlcModGroup8_Type = ModulationValue
_PlcModGroup8_Object = MibTableColumn
plcModGroup8 = _PlcModGroup8_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 9),
    _PlcModGroup8_Type()
)
plcModGroup8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup8.setStatus("current")
_PlcModGroup9_Type = ModulationValue
_PlcModGroup9_Object = MibTableColumn
plcModGroup9 = _PlcModGroup9_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 10),
    _PlcModGroup9_Type()
)
plcModGroup9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup9.setStatus("current")
_PlcModGroup10_Type = ModulationValue
_PlcModGroup10_Object = MibTableColumn
plcModGroup10 = _PlcModGroup10_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 11),
    _PlcModGroup10_Type()
)
plcModGroup10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup10.setStatus("current")
_PlcModGroup11_Type = ModulationValue
_PlcModGroup11_Object = MibTableColumn
plcModGroup11 = _PlcModGroup11_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 12),
    _PlcModGroup11_Type()
)
plcModGroup11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup11.setStatus("current")
_PlcModGroup12_Type = ModulationValue
_PlcModGroup12_Object = MibTableColumn
plcModGroup12 = _PlcModGroup12_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 13),
    _PlcModGroup12_Type()
)
plcModGroup12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup12.setStatus("current")
_PlcModGroup13_Type = ModulationValue
_PlcModGroup13_Object = MibTableColumn
plcModGroup13 = _PlcModGroup13_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 14),
    _PlcModGroup13_Type()
)
plcModGroup13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup13.setStatus("current")
_PlcModGroup14_Type = ModulationValue
_PlcModGroup14_Object = MibTableColumn
plcModGroup14 = _PlcModGroup14_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 15),
    _PlcModGroup14_Type()
)
plcModGroup14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup14.setStatus("current")
_PlcModGroup15_Type = ModulationValue
_PlcModGroup15_Object = MibTableColumn
plcModGroup15 = _PlcModGroup15_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 16),
    _PlcModGroup15_Type()
)
plcModGroup15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup15.setStatus("current")
_PlcModGroup16_Type = ModulationValue
_PlcModGroup16_Object = MibTableColumn
plcModGroup16 = _PlcModGroup16_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 4, 1, 17),
    _PlcModGroup16_Type()
)
plcModGroup16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModGroup16.setStatus("current")
_PlcChannelModulationInput_ObjectIdentity = ObjectIdentity
plcChannelModulationInput = _PlcChannelModulationInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5)
)
_PlcModulationInputAddr_Type = MacAddress
_PlcModulationInputAddr_Object = MibScalar
plcModulationInputAddr = _PlcModulationInputAddr_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 1),
    _PlcModulationInputAddr_Type()
)
plcModulationInputAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcModulationInputAddr.setStatus("current")
_PlcModulationInputChannel_Type = PlcChannelType
_PlcModulationInputChannel_Object = MibScalar
plcModulationInputChannel = _PlcModulationInputChannel_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 2),
    _PlcModulationInputChannel_Type()
)
plcModulationInputChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcModulationInputChannel.setStatus("current")
_PlcModulationInputBand_Type = BandValue
_PlcModulationInputBand_Object = MibScalar
plcModulationInputBand = _PlcModulationInputBand_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 3),
    _PlcModulationInputBand_Type()
)
plcModulationInputBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcModulationInputBand.setStatus("current")
_PlcInputModulationGroup1_Type = ModulationValue
_PlcInputModulationGroup1_Object = MibScalar
plcInputModulationGroup1 = _PlcInputModulationGroup1_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 4),
    _PlcInputModulationGroup1_Type()
)
plcInputModulationGroup1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup1.setStatus("current")
_PlcInputModulationGroup2_Type = ModulationValue
_PlcInputModulationGroup2_Object = MibScalar
plcInputModulationGroup2 = _PlcInputModulationGroup2_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 5),
    _PlcInputModulationGroup2_Type()
)
plcInputModulationGroup2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup2.setStatus("current")
_PlcInputModulationGroup3_Type = ModulationValue
_PlcInputModulationGroup3_Object = MibScalar
plcInputModulationGroup3 = _PlcInputModulationGroup3_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 6),
    _PlcInputModulationGroup3_Type()
)
plcInputModulationGroup3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup3.setStatus("current")
_PlcInputModulationGroup4_Type = ModulationValue
_PlcInputModulationGroup4_Object = MibScalar
plcInputModulationGroup4 = _PlcInputModulationGroup4_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 7),
    _PlcInputModulationGroup4_Type()
)
plcInputModulationGroup4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup4.setStatus("current")
_PlcInputModulationGroup5_Type = ModulationValue
_PlcInputModulationGroup5_Object = MibScalar
plcInputModulationGroup5 = _PlcInputModulationGroup5_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 8),
    _PlcInputModulationGroup5_Type()
)
plcInputModulationGroup5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup5.setStatus("current")
_PlcInputModulationGroup6_Type = ModulationValue
_PlcInputModulationGroup6_Object = MibScalar
plcInputModulationGroup6 = _PlcInputModulationGroup6_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 9),
    _PlcInputModulationGroup6_Type()
)
plcInputModulationGroup6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup6.setStatus("current")
_PlcInputModulationGroup7_Type = ModulationValue
_PlcInputModulationGroup7_Object = MibScalar
plcInputModulationGroup7 = _PlcInputModulationGroup7_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 10),
    _PlcInputModulationGroup7_Type()
)
plcInputModulationGroup7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup7.setStatus("current")
_PlcInputModulationGroup8_Type = ModulationValue
_PlcInputModulationGroup8_Object = MibScalar
plcInputModulationGroup8 = _PlcInputModulationGroup8_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 11),
    _PlcInputModulationGroup8_Type()
)
plcInputModulationGroup8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup8.setStatus("current")
_PlcInputModulationGroup9_Type = ModulationValue
_PlcInputModulationGroup9_Object = MibScalar
plcInputModulationGroup9 = _PlcInputModulationGroup9_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 12),
    _PlcInputModulationGroup9_Type()
)
plcInputModulationGroup9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup9.setStatus("current")
_PlcInputModulationGroup10_Type = ModulationValue
_PlcInputModulationGroup10_Object = MibScalar
plcInputModulationGroup10 = _PlcInputModulationGroup10_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 13),
    _PlcInputModulationGroup10_Type()
)
plcInputModulationGroup10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup10.setStatus("current")
_PlcInputModulationGroup11_Type = ModulationValue
_PlcInputModulationGroup11_Object = MibScalar
plcInputModulationGroup11 = _PlcInputModulationGroup11_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 14),
    _PlcInputModulationGroup11_Type()
)
plcInputModulationGroup11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup11.setStatus("current")
_PlcInputModulationGroup12_Type = ModulationValue
_PlcInputModulationGroup12_Object = MibScalar
plcInputModulationGroup12 = _PlcInputModulationGroup12_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 15),
    _PlcInputModulationGroup12_Type()
)
plcInputModulationGroup12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup12.setStatus("current")
_PlcInputModulationGroup13_Type = ModulationValue
_PlcInputModulationGroup13_Object = MibScalar
plcInputModulationGroup13 = _PlcInputModulationGroup13_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 16),
    _PlcInputModulationGroup13_Type()
)
plcInputModulationGroup13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup13.setStatus("current")
_PlcInputModulationGroup14_Type = ModulationValue
_PlcInputModulationGroup14_Object = MibScalar
plcInputModulationGroup14 = _PlcInputModulationGroup14_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 17),
    _PlcInputModulationGroup14_Type()
)
plcInputModulationGroup14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup14.setStatus("current")
_PlcInputModulationGroup15_Type = ModulationValue
_PlcInputModulationGroup15_Object = MibScalar
plcInputModulationGroup15 = _PlcInputModulationGroup15_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 18),
    _PlcInputModulationGroup15_Type()
)
plcInputModulationGroup15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup15.setStatus("current")
_PlcInputModulationGroup16_Type = ModulationValue
_PlcInputModulationGroup16_Object = MibScalar
plcInputModulationGroup16 = _PlcInputModulationGroup16_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 19),
    _PlcInputModulationGroup16_Type()
)
plcInputModulationGroup16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputModulationGroup16.setStatus("current")
_PlcModulationInputProceed_Type = TruthValue
_PlcModulationInputProceed_Object = MibScalar
plcModulationInputProceed = _PlcModulationInputProceed_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 20),
    _PlcModulationInputProceed_Type()
)
plcModulationInputProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcModulationInputProceed.setStatus("current")
_PlcModulationInputResult_Type = ResultValue
_PlcModulationInputResult_Object = MibScalar
plcModulationInputResult = _PlcModulationInputResult_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 5, 21),
    _PlcModulationInputResult_Type()
)
plcModulationInputResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcModulationInputResult.setStatus("current")
_PlcPortChannelTable_Object = MibTable
plcPortChannelTable = _PlcPortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    plcPortChannelTable.setStatus("current")
_PlcPortChannelEntry_Object = MibTableRow
plcPortChannelEntry = _PlcPortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 6, 1)
)
plcPortChannelEntry.setIndexNames(
    (0, "SPC200", "plcBasePortIndex"),
    (0, "SPC200", "plcPortChannelIndex"),
)
if mibBuilder.loadTexts:
    plcPortChannelEntry.setStatus("current")
_PlcPortChannelIndex_Type = Unsigned32
_PlcPortChannelIndex_Object = MibTableColumn
plcPortChannelIndex = _PlcPortChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 6, 1, 1),
    _PlcPortChannelIndex_Type()
)
plcPortChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plcPortChannelIndex.setStatus("current")
_PlcPortChannelType_Type = PlcChannelType
_PlcPortChannelType_Object = MibTableColumn
plcPortChannelType = _PlcPortChannelType_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 6, 1, 2),
    _PlcPortChannelType_Type()
)
plcPortChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcPortChannelType.setStatus("current")
_PlcPortChannelGain_Type = Integer32
_PlcPortChannelGain_Object = MibTableColumn
plcPortChannelGain = _PlcPortChannelGain_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 6, 1, 3),
    _PlcPortChannelGain_Type()
)
plcPortChannelGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcPortChannelGain.setStatus("current")
_PlcPortChannelBandwidth_Type = ChannelBandwidthValue
_PlcPortChannelBandwidth_Object = MibTableColumn
plcPortChannelBandwidth = _PlcPortChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 6, 1, 4),
    _PlcPortChannelBandwidth_Type()
)
plcPortChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcPortChannelBandwidth.setStatus("current")
_PlcPortChannelMaxBandwidth_Type = ChannelBandwidthValue
_PlcPortChannelMaxBandwidth_Object = MibTableColumn
plcPortChannelMaxBandwidth = _PlcPortChannelMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 6, 1, 5),
    _PlcPortChannelMaxBandwidth_Type()
)
plcPortChannelMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcPortChannelMaxBandwidth.setStatus("current")
_PlcPortChannelSynchronizationBand_Type = BandValue
_PlcPortChannelSynchronizationBand_Object = MibTableColumn
plcPortChannelSynchronizationBand = _PlcPortChannelSynchronizationBand_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 6, 1, 6),
    _PlcPortChannelSynchronizationBand_Type()
)
plcPortChannelSynchronizationBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcPortChannelSynchronizationBand.setStatus("current")
_PlcChannelPilotStringTable_Object = MibTable
plcChannelPilotStringTable = _PlcChannelPilotStringTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    plcChannelPilotStringTable.setStatus("current")
_PlcChannelPilotStringEntry_Object = MibTableRow
plcChannelPilotStringEntry = _PlcChannelPilotStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 7, 1)
)
plcChannelPilotStringEntry.setIndexNames(
    (0, "SPC200", "plcBasePortIndex"),
)
if mibBuilder.loadTexts:
    plcChannelPilotStringEntry.setStatus("current")
_PlcRxChannelPilots_Type = OctetString
_PlcRxChannelPilots_Object = MibTableColumn
plcRxChannelPilots = _PlcRxChannelPilots_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 7, 1, 1),
    _PlcRxChannelPilots_Type()
)
plcRxChannelPilots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcRxChannelPilots.setStatus("current")
_PlcRxLastChannelPilots_Type = OctetString
_PlcRxLastChannelPilots_Object = MibTableColumn
plcRxLastChannelPilots = _PlcRxLastChannelPilots_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 7, 1, 2),
    _PlcRxLastChannelPilots_Type()
)
plcRxLastChannelPilots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcRxLastChannelPilots.setStatus("current")
_PlcTxChannelPilots_Type = OctetString
_PlcTxChannelPilots_Object = MibTableColumn
plcTxChannelPilots = _PlcTxChannelPilots_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 7, 1, 3),
    _PlcTxChannelPilots_Type()
)
plcTxChannelPilots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcTxChannelPilots.setStatus("current")
_PlcChannelPilotsTable_Object = MibTable
plcChannelPilotsTable = _PlcChannelPilotsTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    plcChannelPilotsTable.setStatus("current")
_PlcChannelPilotsEntry_Object = MibTableRow
plcChannelPilotsEntry = _PlcChannelPilotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 8, 1)
)
plcChannelPilotsEntry.setIndexNames(
    (0, "SPC200", "plcBasePortIndex"),
    (0, "SPC200", "plcPortChannelIndex"),
    (0, "SPC200", "plcChannelPilotBandIndex"),
)
if mibBuilder.loadTexts:
    plcChannelPilotsEntry.setStatus("current")
_PlcChannelPilotBandIndex_Type = BandValue
_PlcChannelPilotBandIndex_Object = MibTableColumn
plcChannelPilotBandIndex = _PlcChannelPilotBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 8, 1, 1),
    _PlcChannelPilotBandIndex_Type()
)
plcChannelPilotBandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plcChannelPilotBandIndex.setStatus("current")
_PlcChannelPilot1_Type = PilotValue
_PlcChannelPilot1_Object = MibTableColumn
plcChannelPilot1 = _PlcChannelPilot1_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 8, 1, 2),
    _PlcChannelPilot1_Type()
)
plcChannelPilot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcChannelPilot1.setStatus("current")
_PlcChannePilot2_Type = PilotValue
_PlcChannePilot2_Object = MibTableColumn
plcChannePilot2 = _PlcChannePilot2_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 8, 1, 3),
    _PlcChannePilot2_Type()
)
plcChannePilot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcChannePilot2.setStatus("current")
_PlcChannelPilotsInput_ObjectIdentity = ObjectIdentity
plcChannelPilotsInput = _PlcChannelPilotsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 9)
)
_PlcPilotsInputAddr_Type = MacAddress
_PlcPilotsInputAddr_Object = MibScalar
plcPilotsInputAddr = _PlcPilotsInputAddr_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 9, 1),
    _PlcPilotsInputAddr_Type()
)
plcPilotsInputAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcPilotsInputAddr.setStatus("current")
_PlcPilotsInputChannel_Type = PlcChannelType
_PlcPilotsInputChannel_Object = MibScalar
plcPilotsInputChannel = _PlcPilotsInputChannel_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 9, 2),
    _PlcPilotsInputChannel_Type()
)
plcPilotsInputChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcPilotsInputChannel.setStatus("current")
_PlcPilotsInputBand_Type = BandValue
_PlcPilotsInputBand_Object = MibScalar
plcPilotsInputBand = _PlcPilotsInputBand_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 9, 3),
    _PlcPilotsInputBand_Type()
)
plcPilotsInputBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcPilotsInputBand.setStatus("current")
_PlcInputChannelPilot1_Type = PilotValue
_PlcInputChannelPilot1_Object = MibScalar
plcInputChannelPilot1 = _PlcInputChannelPilot1_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 9, 4),
    _PlcInputChannelPilot1_Type()
)
plcInputChannelPilot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputChannelPilot1.setStatus("current")
_PlcInputChannelPilot2_Type = PilotValue
_PlcInputChannelPilot2_Object = MibScalar
plcInputChannelPilot2 = _PlcInputChannelPilot2_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 9, 5),
    _PlcInputChannelPilot2_Type()
)
plcInputChannelPilot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputChannelPilot2.setStatus("current")
_PlcPilotsInputProceed_Type = TruthValue
_PlcPilotsInputProceed_Object = MibScalar
plcPilotsInputProceed = _PlcPilotsInputProceed_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 9, 6),
    _PlcPilotsInputProceed_Type()
)
plcPilotsInputProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcPilotsInputProceed.setStatus("current")
_PlcPilotsInputResult_Type = ResultValue
_PlcPilotsInputResult_Object = MibScalar
plcPilotsInputResult = _PlcPilotsInputResult_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 2, 9, 7),
    _PlcPilotsInputResult_Type()
)
plcPilotsInputResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcPilotsInputResult.setStatus("current")
_PlcNodeConfiguration_ObjectIdentity = ObjectIdentity
plcNodeConfiguration = _PlcNodeConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3)
)
_PlcNodeNotches_Type = OctetString
_PlcNodeNotches_Object = MibScalar
plcNodeNotches = _PlcNodeNotches_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 1),
    _PlcNodeNotches_Type()
)
plcNodeNotches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeNotches.setStatus("current")
_PlcNodeNotchesTable_Object = MibTable
plcNodeNotchesTable = _PlcNodeNotchesTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    plcNodeNotchesTable.setStatus("current")
_PlcNodeNotchesEntry_Object = MibTableRow
plcNodeNotchesEntry = _PlcNodeNotchesEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2, 1)
)
plcNodeNotchesEntry.setIndexNames(
    (0, "SPC200", "plcNodeNotchesBandIndex"),
    (0, "SPC200", "plcNodeNotchesGroupIndex"),
)
if mibBuilder.loadTexts:
    plcNodeNotchesEntry.setStatus("current")
_PlcNodeNotchesBandIndex_Type = BandValue
_PlcNodeNotchesBandIndex_Object = MibTableColumn
plcNodeNotchesBandIndex = _PlcNodeNotchesBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2, 1, 1),
    _PlcNodeNotchesBandIndex_Type()
)
plcNodeNotchesBandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plcNodeNotchesBandIndex.setStatus("current")
_PlcNodeNotchesGroupIndex_Type = GroupValue
_PlcNodeNotchesGroupIndex_Object = MibTableColumn
plcNodeNotchesGroupIndex = _PlcNodeNotchesGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2, 1, 2),
    _PlcNodeNotchesGroupIndex_Type()
)
plcNodeNotchesGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plcNodeNotchesGroupIndex.setStatus("current")
_PlcNodeNotchesCarrier1_Type = TruthValue
_PlcNodeNotchesCarrier1_Object = MibTableColumn
plcNodeNotchesCarrier1 = _PlcNodeNotchesCarrier1_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2, 1, 3),
    _PlcNodeNotchesCarrier1_Type()
)
plcNodeNotchesCarrier1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeNotchesCarrier1.setStatus("current")
_PlcNodeNotchesCarrier2_Type = TruthValue
_PlcNodeNotchesCarrier2_Object = MibTableColumn
plcNodeNotchesCarrier2 = _PlcNodeNotchesCarrier2_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2, 1, 4),
    _PlcNodeNotchesCarrier2_Type()
)
plcNodeNotchesCarrier2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeNotchesCarrier2.setStatus("current")
_PlcNodeNotchesCarrier3_Type = TruthValue
_PlcNodeNotchesCarrier3_Object = MibTableColumn
plcNodeNotchesCarrier3 = _PlcNodeNotchesCarrier3_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2, 1, 5),
    _PlcNodeNotchesCarrier3_Type()
)
plcNodeNotchesCarrier3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeNotchesCarrier3.setStatus("current")
_PlcNodeNotchesCarrier4_Type = TruthValue
_PlcNodeNotchesCarrier4_Object = MibTableColumn
plcNodeNotchesCarrier4 = _PlcNodeNotchesCarrier4_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2, 1, 6),
    _PlcNodeNotchesCarrier4_Type()
)
plcNodeNotchesCarrier4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeNotchesCarrier4.setStatus("current")
_PlcNodeNotchesCarrier5_Type = TruthValue
_PlcNodeNotchesCarrier5_Object = MibTableColumn
plcNodeNotchesCarrier5 = _PlcNodeNotchesCarrier5_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2, 1, 7),
    _PlcNodeNotchesCarrier5_Type()
)
plcNodeNotchesCarrier5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeNotchesCarrier5.setStatus("current")
_PlcNodeNotchesCarrier6_Type = TruthValue
_PlcNodeNotchesCarrier6_Object = MibTableColumn
plcNodeNotchesCarrier6 = _PlcNodeNotchesCarrier6_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2, 1, 8),
    _PlcNodeNotchesCarrier6_Type()
)
plcNodeNotchesCarrier6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeNotchesCarrier6.setStatus("current")
_PlcNodeNotchesCarrier7_Type = TruthValue
_PlcNodeNotchesCarrier7_Object = MibTableColumn
plcNodeNotchesCarrier7 = _PlcNodeNotchesCarrier7_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2, 1, 9),
    _PlcNodeNotchesCarrier7_Type()
)
plcNodeNotchesCarrier7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeNotchesCarrier7.setStatus("current")
_PlcNodeNotchesCarrier8_Type = TruthValue
_PlcNodeNotchesCarrier8_Object = MibTableColumn
plcNodeNotchesCarrier8 = _PlcNodeNotchesCarrier8_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 2, 1, 10),
    _PlcNodeNotchesCarrier8_Type()
)
plcNodeNotchesCarrier8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeNotchesCarrier8.setStatus("current")
_PlcNodeNotchesInput_ObjectIdentity = ObjectIdentity
plcNodeNotchesInput = _PlcNodeNotchesInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3)
)
_PlcNodeNotchesInputBand_Type = BandValue
_PlcNodeNotchesInputBand_Object = MibScalar
plcNodeNotchesInputBand = _PlcNodeNotchesInputBand_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 1),
    _PlcNodeNotchesInputBand_Type()
)
plcNodeNotchesInputBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNotchesInputBand.setStatus("current")
_PlcNodeNotchesInputGroup_Type = GroupValue
_PlcNodeNotchesInputGroup_Object = MibScalar
plcNodeNotchesInputGroup = _PlcNodeNotchesInputGroup_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 2),
    _PlcNodeNotchesInputGroup_Type()
)
plcNodeNotchesInputGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNotchesInputGroup.setStatus("current")
_PlcNodeNotchesInputCarrier1_Type = TruthValue
_PlcNodeNotchesInputCarrier1_Object = MibScalar
plcNodeNotchesInputCarrier1 = _PlcNodeNotchesInputCarrier1_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 3),
    _PlcNodeNotchesInputCarrier1_Type()
)
plcNodeNotchesInputCarrier1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNotchesInputCarrier1.setStatus("current")
_PlcNodeNotchesInputCarrier2_Type = TruthValue
_PlcNodeNotchesInputCarrier2_Object = MibScalar
plcNodeNotchesInputCarrier2 = _PlcNodeNotchesInputCarrier2_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 4),
    _PlcNodeNotchesInputCarrier2_Type()
)
plcNodeNotchesInputCarrier2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNotchesInputCarrier2.setStatus("current")
_PlcNodeNotchesInputCarrier3_Type = TruthValue
_PlcNodeNotchesInputCarrier3_Object = MibScalar
plcNodeNotchesInputCarrier3 = _PlcNodeNotchesInputCarrier3_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 5),
    _PlcNodeNotchesInputCarrier3_Type()
)
plcNodeNotchesInputCarrier3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNotchesInputCarrier3.setStatus("current")
_PlcNodeNotchesInputCarrier4_Type = TruthValue
_PlcNodeNotchesInputCarrier4_Object = MibScalar
plcNodeNotchesInputCarrier4 = _PlcNodeNotchesInputCarrier4_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 6),
    _PlcNodeNotchesInputCarrier4_Type()
)
plcNodeNotchesInputCarrier4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNotchesInputCarrier4.setStatus("current")
_PlcNodeNotchesInputCarrier5_Type = TruthValue
_PlcNodeNotchesInputCarrier5_Object = MibScalar
plcNodeNotchesInputCarrier5 = _PlcNodeNotchesInputCarrier5_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 7),
    _PlcNodeNotchesInputCarrier5_Type()
)
plcNodeNotchesInputCarrier5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNotchesInputCarrier5.setStatus("current")
_PlcNodeNotchesInputCarrier6_Type = TruthValue
_PlcNodeNotchesInputCarrier6_Object = MibScalar
plcNodeNotchesInputCarrier6 = _PlcNodeNotchesInputCarrier6_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 8),
    _PlcNodeNotchesInputCarrier6_Type()
)
plcNodeNotchesInputCarrier6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNotchesInputCarrier6.setStatus("current")
_PlcNodeNotchesInputCarrier7_Type = TruthValue
_PlcNodeNotchesInputCarrier7_Object = MibScalar
plcNodeNotchesInputCarrier7 = _PlcNodeNotchesInputCarrier7_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 9),
    _PlcNodeNotchesInputCarrier7_Type()
)
plcNodeNotchesInputCarrier7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNotchesInputCarrier7.setStatus("current")
_PlcNodeNotchesInputCarrier8_Type = TruthValue
_PlcNodeNotchesInputCarrier8_Object = MibScalar
plcNodeNotchesInputCarrier8 = _PlcNodeNotchesInputCarrier8_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 10),
    _PlcNodeNotchesInputCarrier8_Type()
)
plcNodeNotchesInputCarrier8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNotchesInputCarrier8.setStatus("current")
_PlcNodeNotchesInputProceed_Type = TruthValue
_PlcNodeNotchesInputProceed_Object = MibScalar
plcNodeNotchesInputProceed = _PlcNodeNotchesInputProceed_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 11),
    _PlcNodeNotchesInputProceed_Type()
)
plcNodeNotchesInputProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNotchesInputProceed.setStatus("current")
_PlcNodeNotchesInputResult_Type = ResultValue
_PlcNodeNotchesInputResult_Object = MibScalar
plcNodeNotchesInputResult = _PlcNodeNotchesInputResult_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 3, 12),
    _PlcNodeNotchesInputResult_Type()
)
plcNodeNotchesInputResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeNotchesInputResult.setStatus("current")
_PlcNodePilots_Type = OctetString
_PlcNodePilots_Object = MibScalar
plcNodePilots = _PlcNodePilots_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 4),
    _PlcNodePilots_Type()
)
plcNodePilots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodePilots.setStatus("current")
_PlcNodePilotsTable_Object = MibTable
plcNodePilotsTable = _PlcNodePilotsTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    plcNodePilotsTable.setStatus("current")
_PlcNodePilotsEntry_Object = MibTableRow
plcNodePilotsEntry = _PlcNodePilotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 5, 1)
)
plcNodePilotsEntry.setIndexNames(
    (0, "SPC200", "plcNodePilotsBandIndex"),
)
if mibBuilder.loadTexts:
    plcNodePilotsEntry.setStatus("current")
_PlcNodePilotsBandIndex_Type = BandValue
_PlcNodePilotsBandIndex_Object = MibTableColumn
plcNodePilotsBandIndex = _PlcNodePilotsBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 5, 1, 1),
    _PlcNodePilotsBandIndex_Type()
)
plcNodePilotsBandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plcNodePilotsBandIndex.setStatus("current")
_PlcNodePilot1_Type = PilotValue
_PlcNodePilot1_Object = MibTableColumn
plcNodePilot1 = _PlcNodePilot1_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 5, 1, 2),
    _PlcNodePilot1_Type()
)
plcNodePilot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodePilot1.setStatus("current")
_PlcNodePilot2_Type = PilotValue
_PlcNodePilot2_Object = MibTableColumn
plcNodePilot2 = _PlcNodePilot2_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 5, 1, 3),
    _PlcNodePilot2_Type()
)
plcNodePilot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodePilot2.setStatus("current")
_PlcNodePilotsInput_ObjectIdentity = ObjectIdentity
plcNodePilotsInput = _PlcNodePilotsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 6)
)
_PlcNodePilotsInputBand_Type = BandValue
_PlcNodePilotsInputBand_Object = MibScalar
plcNodePilotsInputBand = _PlcNodePilotsInputBand_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 6, 1),
    _PlcNodePilotsInputBand_Type()
)
plcNodePilotsInputBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodePilotsInputBand.setStatus("current")
_PlcInputNodePilot1_Type = PilotValue
_PlcInputNodePilot1_Object = MibScalar
plcInputNodePilot1 = _PlcInputNodePilot1_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 6, 2),
    _PlcInputNodePilot1_Type()
)
plcInputNodePilot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputNodePilot1.setStatus("current")
_PlcInputNodePilot2_Type = PilotValue
_PlcInputNodePilot2_Object = MibScalar
plcInputNodePilot2 = _PlcInputNodePilot2_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 6, 3),
    _PlcInputNodePilot2_Type()
)
plcInputNodePilot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcInputNodePilot2.setStatus("current")
_PlcNodePilotsInputProceed_Type = TruthValue
_PlcNodePilotsInputProceed_Object = MibScalar
plcNodePilotsInputProceed = _PlcNodePilotsInputProceed_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 6, 4),
    _PlcNodePilotsInputProceed_Type()
)
plcNodePilotsInputProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodePilotsInputProceed.setStatus("current")
_PlcNodePilotsInputResult_Type = ResultValue
_PlcNodePilotsInputResult_Object = MibScalar
plcNodePilotsInputResult = _PlcNodePilotsInputResult_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 6, 5),
    _PlcNodePilotsInputResult_Type()
)
plcNodePilotsInputResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodePilotsInputResult.setStatus("current")
_PlcNodeAdaptsStringTable_Object = MibTable
plcNodeAdaptsStringTable = _PlcNodeAdaptsStringTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 7)
)
if mibBuilder.loadTexts:
    plcNodeAdaptsStringTable.setStatus("current")
_PlcNodeAdaptsStringEntry_Object = MibTableRow
plcNodeAdaptsStringEntry = _PlcNodeAdaptsStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 7, 1)
)
plcNodeAdaptsStringEntry.setIndexNames(
    (0, "SPC200", "plcBasePortIndex"),
    (0, "SPC200", "plcNodeAdaptsStringBandIndex"),
)
if mibBuilder.loadTexts:
    plcNodeAdaptsStringEntry.setStatus("current")
_PlcNodeAdaptsStringBandIndex_Type = BandValue
_PlcNodeAdaptsStringBandIndex_Object = MibTableColumn
plcNodeAdaptsStringBandIndex = _PlcNodeAdaptsStringBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 7, 1, 1),
    _PlcNodeAdaptsStringBandIndex_Type()
)
plcNodeAdaptsStringBandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plcNodeAdaptsStringBandIndex.setStatus("current")
_PlcNodeAdaptsStringBand_Type = OctetString
_PlcNodeAdaptsStringBand_Object = MibTableColumn
plcNodeAdaptsStringBand = _PlcNodeAdaptsStringBand_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 7, 1, 2),
    _PlcNodeAdaptsStringBand_Type()
)
plcNodeAdaptsStringBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeAdaptsStringBand.setStatus("current")
_PlcNodeAdaptsTable_Object = MibTable
plcNodeAdaptsTable = _PlcNodeAdaptsTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8)
)
if mibBuilder.loadTexts:
    plcNodeAdaptsTable.setStatus("current")
_PlcNodeAdaptsEntry_Object = MibTableRow
plcNodeAdaptsEntry = _PlcNodeAdaptsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8, 1)
)
plcNodeAdaptsEntry.setIndexNames(
    (0, "SPC200", "plcNodeAdaptsBandIndex"),
    (0, "SPC200", "plcNodeAdaptsGroupIndex"),
)
if mibBuilder.loadTexts:
    plcNodeAdaptsEntry.setStatus("current")
_PlcNodeAdaptsBandIndex_Type = BandValue
_PlcNodeAdaptsBandIndex_Object = MibTableColumn
plcNodeAdaptsBandIndex = _PlcNodeAdaptsBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8, 1, 1),
    _PlcNodeAdaptsBandIndex_Type()
)
plcNodeAdaptsBandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plcNodeAdaptsBandIndex.setStatus("current")
_PlcNodeAdaptsGroupIndex_Type = GroupValue
_PlcNodeAdaptsGroupIndex_Object = MibTableColumn
plcNodeAdaptsGroupIndex = _PlcNodeAdaptsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8, 1, 2),
    _PlcNodeAdaptsGroupIndex_Type()
)
plcNodeAdaptsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    plcNodeAdaptsGroupIndex.setStatus("current")
_PlcNodeAdaptsCarrier1_Type = AdaptValue
_PlcNodeAdaptsCarrier1_Object = MibTableColumn
plcNodeAdaptsCarrier1 = _PlcNodeAdaptsCarrier1_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8, 1, 3),
    _PlcNodeAdaptsCarrier1_Type()
)
plcNodeAdaptsCarrier1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeAdaptsCarrier1.setStatus("current")
_PlcNodeAdaptsCarrier2_Type = AdaptValue
_PlcNodeAdaptsCarrier2_Object = MibTableColumn
plcNodeAdaptsCarrier2 = _PlcNodeAdaptsCarrier2_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8, 1, 4),
    _PlcNodeAdaptsCarrier2_Type()
)
plcNodeAdaptsCarrier2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeAdaptsCarrier2.setStatus("current")
_PlcNodeAdaptsCarrier3_Type = AdaptValue
_PlcNodeAdaptsCarrier3_Object = MibTableColumn
plcNodeAdaptsCarrier3 = _PlcNodeAdaptsCarrier3_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8, 1, 5),
    _PlcNodeAdaptsCarrier3_Type()
)
plcNodeAdaptsCarrier3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeAdaptsCarrier3.setStatus("current")
_PlcNodeAdaptsCarrier4_Type = AdaptValue
_PlcNodeAdaptsCarrier4_Object = MibTableColumn
plcNodeAdaptsCarrier4 = _PlcNodeAdaptsCarrier4_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8, 1, 6),
    _PlcNodeAdaptsCarrier4_Type()
)
plcNodeAdaptsCarrier4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeAdaptsCarrier4.setStatus("current")
_PlcNodeAdaptsCarrier5_Type = AdaptValue
_PlcNodeAdaptsCarrier5_Object = MibTableColumn
plcNodeAdaptsCarrier5 = _PlcNodeAdaptsCarrier5_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8, 1, 7),
    _PlcNodeAdaptsCarrier5_Type()
)
plcNodeAdaptsCarrier5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeAdaptsCarrier5.setStatus("current")
_PlcNodeAdaptsCarrier6_Type = AdaptValue
_PlcNodeAdaptsCarrier6_Object = MibTableColumn
plcNodeAdaptsCarrier6 = _PlcNodeAdaptsCarrier6_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8, 1, 8),
    _PlcNodeAdaptsCarrier6_Type()
)
plcNodeAdaptsCarrier6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeAdaptsCarrier6.setStatus("current")
_PlcNodeAdaptsCarrier7_Type = AdaptValue
_PlcNodeAdaptsCarrier7_Object = MibTableColumn
plcNodeAdaptsCarrier7 = _PlcNodeAdaptsCarrier7_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8, 1, 9),
    _PlcNodeAdaptsCarrier7_Type()
)
plcNodeAdaptsCarrier7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeAdaptsCarrier7.setStatus("current")
_PlcNodeAdaptsCarrier8_Type = AdaptValue
_PlcNodeAdaptsCarrier8_Object = MibTableColumn
plcNodeAdaptsCarrier8 = _PlcNodeAdaptsCarrier8_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 8, 1, 10),
    _PlcNodeAdaptsCarrier8_Type()
)
plcNodeAdaptsCarrier8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeAdaptsCarrier8.setStatus("current")
_PlcNodeAdaptsInput_ObjectIdentity = ObjectIdentity
plcNodeAdaptsInput = _PlcNodeAdaptsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9)
)
_PlcNodeAdaptsInputBand_Type = BandValue
_PlcNodeAdaptsInputBand_Object = MibScalar
plcNodeAdaptsInputBand = _PlcNodeAdaptsInputBand_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 1),
    _PlcNodeAdaptsInputBand_Type()
)
plcNodeAdaptsInputBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputBand.setStatus("current")
_PlcNodeAdaptsInputGroup_Type = GroupValue
_PlcNodeAdaptsInputGroup_Object = MibScalar
plcNodeAdaptsInputGroup = _PlcNodeAdaptsInputGroup_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 2),
    _PlcNodeAdaptsInputGroup_Type()
)
plcNodeAdaptsInputGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputGroup.setStatus("current")
_PlcNodeAdaptsInputCarrier1_Type = AdaptValue
_PlcNodeAdaptsInputCarrier1_Object = MibScalar
plcNodeAdaptsInputCarrier1 = _PlcNodeAdaptsInputCarrier1_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 3),
    _PlcNodeAdaptsInputCarrier1_Type()
)
plcNodeAdaptsInputCarrier1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputCarrier1.setStatus("current")
_PlcNodeAdaptsInputCarrier2_Type = AdaptValue
_PlcNodeAdaptsInputCarrier2_Object = MibScalar
plcNodeAdaptsInputCarrier2 = _PlcNodeAdaptsInputCarrier2_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 4),
    _PlcNodeAdaptsInputCarrier2_Type()
)
plcNodeAdaptsInputCarrier2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputCarrier2.setStatus("current")
_PlcNodeAdaptsInputCarrier3_Type = AdaptValue
_PlcNodeAdaptsInputCarrier3_Object = MibScalar
plcNodeAdaptsInputCarrier3 = _PlcNodeAdaptsInputCarrier3_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 5),
    _PlcNodeAdaptsInputCarrier3_Type()
)
plcNodeAdaptsInputCarrier3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputCarrier3.setStatus("current")
_PlcNodeAdaptsInputCarrier4_Type = AdaptValue
_PlcNodeAdaptsInputCarrier4_Object = MibScalar
plcNodeAdaptsInputCarrier4 = _PlcNodeAdaptsInputCarrier4_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 6),
    _PlcNodeAdaptsInputCarrier4_Type()
)
plcNodeAdaptsInputCarrier4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputCarrier4.setStatus("current")
_PlcNodeAdaptsInputCarrier5_Type = AdaptValue
_PlcNodeAdaptsInputCarrier5_Object = MibScalar
plcNodeAdaptsInputCarrier5 = _PlcNodeAdaptsInputCarrier5_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 7),
    _PlcNodeAdaptsInputCarrier5_Type()
)
plcNodeAdaptsInputCarrier5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputCarrier5.setStatus("current")
_PlcNodeAdaptsInputCarrier6_Type = AdaptValue
_PlcNodeAdaptsInputCarrier6_Object = MibScalar
plcNodeAdaptsInputCarrier6 = _PlcNodeAdaptsInputCarrier6_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 8),
    _PlcNodeAdaptsInputCarrier6_Type()
)
plcNodeAdaptsInputCarrier6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputCarrier6.setStatus("current")
_PlcNodeAdaptsInputCarrier7_Type = AdaptValue
_PlcNodeAdaptsInputCarrier7_Object = MibScalar
plcNodeAdaptsInputCarrier7 = _PlcNodeAdaptsInputCarrier7_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 9),
    _PlcNodeAdaptsInputCarrier7_Type()
)
plcNodeAdaptsInputCarrier7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputCarrier7.setStatus("current")
_PlcNodeAdaptsInputCarrier8_Type = AdaptValue
_PlcNodeAdaptsInputCarrier8_Object = MibScalar
plcNodeAdaptsInputCarrier8 = _PlcNodeAdaptsInputCarrier8_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 10),
    _PlcNodeAdaptsInputCarrier8_Type()
)
plcNodeAdaptsInputCarrier8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputCarrier8.setStatus("current")
_PlcNodeAdaptsInputProceed_Type = TruthValue
_PlcNodeAdaptsInputProceed_Object = MibScalar
plcNodeAdaptsInputProceed = _PlcNodeAdaptsInputProceed_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 11),
    _PlcNodeAdaptsInputProceed_Type()
)
plcNodeAdaptsInputProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputProceed.setStatus("current")
_PlcNodeAdaptsInputResult_Type = ResultValue
_PlcNodeAdaptsInputResult_Object = MibScalar
plcNodeAdaptsInputResult = _PlcNodeAdaptsInputResult_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 9, 12),
    _PlcNodeAdaptsInputResult_Type()
)
plcNodeAdaptsInputResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeAdaptsInputResult.setStatus("current")
_PlcNodeNetConfigTable_Object = MibTable
plcNodeNetConfigTable = _PlcNodeNetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 10)
)
if mibBuilder.loadTexts:
    plcNodeNetConfigTable.setStatus("current")
_PlcNodeNetConfigEntry_Object = MibTableRow
plcNodeNetConfigEntry = _PlcNodeNetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 10, 1)
)
plcNodeNetConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    plcNodeNetConfigEntry.setStatus("current")
_PlcNodeIpAddr_Type = IpAddress
_PlcNodeIpAddr_Object = MibTableColumn
plcNodeIpAddr = _PlcNodeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 10, 1, 1),
    _PlcNodeIpAddr_Type()
)
plcNodeIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeIpAddr.setStatus("current")
_PlcNodeNetMask_Type = IpAddress
_PlcNodeNetMask_Object = MibTableColumn
plcNodeNetMask = _PlcNodeNetMask_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 10, 1, 2),
    _PlcNodeNetMask_Type()
)
plcNodeNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeNetMask.setStatus("current")
_PlcNodeMacAddr_Type = MacAddress
_PlcNodeMacAddr_Object = MibTableColumn
plcNodeMacAddr = _PlcNodeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 10, 1, 3),
    _PlcNodeMacAddr_Type()
)
plcNodeMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeMacAddr.setStatus("current")
_PlcNodeGateway_Type = IpAddress
_PlcNodeGateway_Object = MibTableColumn
plcNodeGateway = _PlcNodeGateway_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 10, 1, 4),
    _PlcNodeGateway_Type()
)
plcNodeGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeGateway.setStatus("current")
_PlcNodeActions_ObjectIdentity = ObjectIdentity
plcNodeActions = _PlcNodeActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 11)
)
_PlcNodeActionsCommit_ObjectIdentity = ObjectIdentity
plcNodeActionsCommit = _PlcNodeActionsCommit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 11, 1)
)
_PlcNodeActionsCommitProceed_Type = TruthValue
_PlcNodeActionsCommitProceed_Object = MibScalar
plcNodeActionsCommitProceed = _PlcNodeActionsCommitProceed_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 11, 1, 1),
    _PlcNodeActionsCommitProceed_Type()
)
plcNodeActionsCommitProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeActionsCommitProceed.setStatus("current")
_PlcNodeActionsCommitResult_Type = ResultValue
_PlcNodeActionsCommitResult_Object = MibScalar
plcNodeActionsCommitResult = _PlcNodeActionsCommitResult_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 11, 1, 2),
    _PlcNodeActionsCommitResult_Type()
)
plcNodeActionsCommitResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcNodeActionsCommitResult.setStatus("current")
_PlcNodeActionsReset_ObjectIdentity = ObjectIdentity
plcNodeActionsReset = _PlcNodeActionsReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 11, 2)
)
_PlcNodeActionsResetProceed_Type = TruthValue
_PlcNodeActionsResetProceed_Object = MibScalar
plcNodeActionsResetProceed = _PlcNodeActionsResetProceed_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 11, 2, 1),
    _PlcNodeActionsResetProceed_Type()
)
plcNodeActionsResetProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeActionsResetProceed.setStatus("current")
_PlcNodeActionsCarrier_ObjectIdentity = ObjectIdentity
plcNodeActionsCarrier = _PlcNodeActionsCarrier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 11, 3)
)
_PlcNodeActionsCarrierFlatProceed_Type = TruthValue
_PlcNodeActionsCarrierFlatProceed_Object = MibScalar
plcNodeActionsCarrierFlatProceed = _PlcNodeActionsCarrierFlatProceed_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 3, 11, 3, 1),
    _PlcNodeActionsCarrierFlatProceed_Type()
)
plcNodeActionsCarrierFlatProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcNodeActionsCarrierFlatProceed.setStatus("current")
_PlcSNAnalyser_ObjectIdentity = ObjectIdentity
plcSNAnalyser = _PlcSNAnalyser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 4)
)


class _PlcSNAnalyserEnable_Type(Integer32):
    """Custom type plcSNAnalyserEnable based on Integer32"""
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


_PlcSNAnalyserEnable_Type.__name__ = "Integer32"
_PlcSNAnalyserEnable_Object = MibScalar
plcSNAnalyserEnable = _PlcSNAnalyserEnable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 4, 1),
    _PlcSNAnalyserEnable_Type()
)
plcSNAnalyserEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcSNAnalyserEnable.setStatus("current")
_PlcSNAnalyserTable_Object = MibTable
plcSNAnalyserTable = _PlcSNAnalyserTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    plcSNAnalyserTable.setStatus("current")
_PlcSNAnalyserEntry_Object = MibTableRow
plcSNAnalyserEntry = _PlcSNAnalyserEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 4, 2, 1)
)
plcSNAnalyserEntry.setIndexNames(
    (0, "SPC200", "plcModBandIndex"),
)
if mibBuilder.loadTexts:
    plcSNAnalyserEntry.setStatus("current")
_PlcSNAnalyserMinSignal_Type = OctetString
_PlcSNAnalyserMinSignal_Object = MibTableColumn
plcSNAnalyserMinSignal = _PlcSNAnalyserMinSignal_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 4, 2, 1, 1),
    _PlcSNAnalyserMinSignal_Type()
)
plcSNAnalyserMinSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcSNAnalyserMinSignal.setStatus("current")
_PlcSNAnalyserMaxSignal_Type = OctetString
_PlcSNAnalyserMaxSignal_Object = MibTableColumn
plcSNAnalyserMaxSignal = _PlcSNAnalyserMaxSignal_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 4, 2, 1, 2),
    _PlcSNAnalyserMaxSignal_Type()
)
plcSNAnalyserMaxSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcSNAnalyserMaxSignal.setStatus("current")
_PlcSNAnalyserAvgSignal_Type = OctetString
_PlcSNAnalyserAvgSignal_Object = MibTableColumn
plcSNAnalyserAvgSignal = _PlcSNAnalyserAvgSignal_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 4, 2, 1, 3),
    _PlcSNAnalyserAvgSignal_Type()
)
plcSNAnalyserAvgSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcSNAnalyserAvgSignal.setStatus("current")
_PlcSNAnalyserLastSignal_Type = OctetString
_PlcSNAnalyserLastSignal_Object = MibTableColumn
plcSNAnalyserLastSignal = _PlcSNAnalyserLastSignal_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 4, 2, 1, 4),
    _PlcSNAnalyserLastSignal_Type()
)
plcSNAnalyserLastSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcSNAnalyserLastSignal.setStatus("current")
_PlcSNAnalyserFFTDiv_Type = Counter32
_PlcSNAnalyserFFTDiv_Object = MibTableColumn
plcSNAnalyserFFTDiv = _PlcSNAnalyserFFTDiv_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 4, 2, 1, 5),
    _PlcSNAnalyserFFTDiv_Type()
)
plcSNAnalyserFFTDiv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcSNAnalyserFFTDiv.setStatus("current")


class _PlcSNAnalyserAGC_Type(Integer32):
    """Custom type plcSNAnalyserAGC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PlcSNAnalyserAGC_Type.__name__ = "Integer32"
_PlcSNAnalyserAGC_Object = MibScalar
plcSNAnalyserAGC = _PlcSNAnalyserAGC_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 4, 3),
    _PlcSNAnalyserAGC_Type()
)
plcSNAnalyserAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcSNAnalyserAGC.setStatus("current")
_PlcAGCAnalyser_ObjectIdentity = ObjectIdentity
plcAGCAnalyser = _PlcAGCAnalyser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 5)
)


class _PlcAGCAnalyserEnable_Type(Integer32):
    """Custom type plcAGCAnalyserEnable based on Integer32"""
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


_PlcAGCAnalyserEnable_Type.__name__ = "Integer32"
_PlcAGCAnalyserEnable_Object = MibScalar
plcAGCAnalyserEnable = _PlcAGCAnalyserEnable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 5, 1),
    _PlcAGCAnalyserEnable_Type()
)
plcAGCAnalyserEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcAGCAnalyserEnable.setStatus("current")
_PlcAGCAnalyserSamplesPart1_Type = OctetString
_PlcAGCAnalyserSamplesPart1_Object = MibScalar
plcAGCAnalyserSamplesPart1 = _PlcAGCAnalyserSamplesPart1_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 5, 2),
    _PlcAGCAnalyserSamplesPart1_Type()
)
plcAGCAnalyserSamplesPart1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcAGCAnalyserSamplesPart1.setStatus("current")
_PlcAGCAnalyserSamplesPart2_Type = OctetString
_PlcAGCAnalyserSamplesPart2_Object = MibScalar
plcAGCAnalyserSamplesPart2 = _PlcAGCAnalyserSamplesPart2_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 5, 3),
    _PlcAGCAnalyserSamplesPart2_Type()
)
plcAGCAnalyserSamplesPart2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plcAGCAnalyserSamplesPart2.setStatus("current")
_PlcBssId_ObjectIdentity = ObjectIdentity
plcBssId = _PlcBssId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 6)
)


class _PlcMasterBssId_Type(Integer32):
    """Custom type plcMasterBssId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_PlcMasterBssId_Type.__name__ = "Integer32"
_PlcMasterBssId_Object = MibScalar
plcMasterBssId = _PlcMasterBssId_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 6, 1),
    _PlcMasterBssId_Type()
)
plcMasterBssId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcMasterBssId.setStatus("current")


class _PlcSlaveBssId_Type(Integer32):
    """Custom type plcSlaveBssId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_PlcSlaveBssId_Type.__name__ = "Integer32"
_PlcSlaveBssId_Object = MibScalar
plcSlaveBssId = _PlcSlaveBssId_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 6, 2),
    _PlcSlaveBssId_Type()
)
plcSlaveBssId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcSlaveBssId.setStatus("current")
_PlcSpy_ObjectIdentity = ObjectIdentity
plcSpy = _PlcSpy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 7)
)
_PlcSpyIsDynamic_Type = TruthValue
_PlcSpyIsDynamic_Object = MibScalar
plcSpyIsDynamic = _PlcSpyIsDynamic_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 7, 1),
    _PlcSpyIsDynamic_Type()
)
plcSpyIsDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcSpyIsDynamic.setStatus("current")
_PlcStaticSpySynchBandNb_Type = BandValue
_PlcStaticSpySynchBandNb_Object = MibScalar
plcStaticSpySynchBandNb = _PlcStaticSpySynchBandNb_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 2, 7, 2),
    _PlcStaticSpySynchBandNb_Type()
)
plcStaticSpySynchBandNb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plcStaticSpySynchBandNb.setStatus("current")
_SoftwareMgnt_ObjectIdentity = ObjectIdentity
softwareMgnt = _SoftwareMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3)
)


class _CurrentSoftwareVersion_Type(DisplayString):
    """Custom type currentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentSoftwareVersion_Type.__name__ = "DisplayString"
_CurrentSoftwareVersion_Object = MibScalar
currentSoftwareVersion = _CurrentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 1),
    _CurrentSoftwareVersion_Type()
)
currentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSoftwareVersion.setStatus("current")


class _CurrentSoftwareBoardVersion_Type(DisplayString):
    """Custom type currentSoftwareBoardVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentSoftwareBoardVersion_Type.__name__ = "DisplayString"
_CurrentSoftwareBoardVersion_Object = MibScalar
currentSoftwareBoardVersion = _CurrentSoftwareBoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 2),
    _CurrentSoftwareBoardVersion_Type()
)
currentSoftwareBoardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSoftwareBoardVersion.setStatus("current")


class _CurrentSoftwareAFEVersion_Type(DisplayString):
    """Custom type currentSoftwareAFEVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentSoftwareAFEVersion_Type.__name__ = "DisplayString"
_CurrentSoftwareAFEVersion_Object = MibScalar
currentSoftwareAFEVersion = _CurrentSoftwareAFEVersion_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 3),
    _CurrentSoftwareAFEVersion_Type()
)
currentSoftwareAFEVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSoftwareAFEVersion.setStatus("current")
_SoftwareTable_Object = MibTable
softwareTable = _SoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    softwareTable.setStatus("current")
_SoftwareEntry_Object = MibTableRow
softwareEntry = _SoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 4, 1)
)
softwareEntry.setIndexNames(
    (0, "SPC200", "softwareIndex"),
)
if mibBuilder.loadTexts:
    softwareEntry.setStatus("current")
_SoftwareIndex_Type = SoftwareIndex
_SoftwareIndex_Object = MibTableColumn
softwareIndex = _SoftwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 4, 1, 1),
    _SoftwareIndex_Type()
)
softwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    softwareIndex.setStatus("current")


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibTableColumn
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 4, 1, 2),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_SoftwareUpload_ObjectIdentity = ObjectIdentity
softwareUpload = _SoftwareUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 5)
)
_SoftwareUploadTFTPServerIP_Type = IpAddress
_SoftwareUploadTFTPServerIP_Object = MibScalar
softwareUploadTFTPServerIP = _SoftwareUploadTFTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 5, 1),
    _SoftwareUploadTFTPServerIP_Type()
)
softwareUploadTFTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareUploadTFTPServerIP.setStatus("current")


class _SoftwareUploadLogin_Type(DisplayString):
    """Custom type softwareUploadLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SoftwareUploadLogin_Type.__name__ = "DisplayString"
_SoftwareUploadLogin_Object = MibScalar
softwareUploadLogin = _SoftwareUploadLogin_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 5, 2),
    _SoftwareUploadLogin_Type()
)
softwareUploadLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareUploadLogin.setStatus("current")


class _SoftwareUploadPassword_Type(DisplayString):
    """Custom type softwareUploadPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SoftwareUploadPassword_Type.__name__ = "DisplayString"
_SoftwareUploadPassword_Object = MibScalar
softwareUploadPassword = _SoftwareUploadPassword_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 5, 3),
    _SoftwareUploadPassword_Type()
)
softwareUploadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareUploadPassword.setStatus("current")


class _SoftwareUploadFileName_Type(DisplayString):
    """Custom type softwareUploadFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareUploadFileName_Type.__name__ = "DisplayString"
_SoftwareUploadFileName_Object = MibScalar
softwareUploadFileName = _SoftwareUploadFileName_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 5, 4),
    _SoftwareUploadFileName_Type()
)
softwareUploadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareUploadFileName.setStatus("current")
_SoftwareUploadProceed_Type = TruthValue
_SoftwareUploadProceed_Object = MibScalar
softwareUploadProceed = _SoftwareUploadProceed_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 5, 5),
    _SoftwareUploadProceed_Type()
)
softwareUploadProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareUploadProceed.setStatus("current")
_SoftwareUploadResult_Type = SoftwareActionResultValue
_SoftwareUploadResult_Object = MibScalar
softwareUploadResult = _SoftwareUploadResult_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 5, 6),
    _SoftwareUploadResult_Type()
)
softwareUploadResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareUploadResult.setStatus("current")


class _SoftwareUploadTFTPServerPort_Type(Integer32):
    """Custom type softwareUploadTFTPServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SoftwareUploadTFTPServerPort_Type.__name__ = "Integer32"
_SoftwareUploadTFTPServerPort_Object = MibScalar
softwareUploadTFTPServerPort = _SoftwareUploadTFTPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 5, 7),
    _SoftwareUploadTFTPServerPort_Type()
)
softwareUploadTFTPServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareUploadTFTPServerPort.setStatus("current")
_SoftwareAction_ObjectIdentity = ObjectIdentity
softwareAction = _SoftwareAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 6)
)
_SoftwareActionIndex_Type = SoftwareIndex
_SoftwareActionIndex_Object = MibScalar
softwareActionIndex = _SoftwareActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 6, 1),
    _SoftwareActionIndex_Type()
)
softwareActionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareActionIndex.setStatus("current")
_SoftwareActionType_Type = SoftwareActionType
_SoftwareActionType_Object = MibScalar
softwareActionType = _SoftwareActionType_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 6, 2),
    _SoftwareActionType_Type()
)
softwareActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareActionType.setStatus("current")
_SoftwareActionProceed_Type = TruthValue
_SoftwareActionProceed_Object = MibScalar
softwareActionProceed = _SoftwareActionProceed_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 6, 3),
    _SoftwareActionProceed_Type()
)
softwareActionProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareActionProceed.setStatus("current")
_SoftwareActionResult_Type = SoftwareActionResultValue
_SoftwareActionResult_Object = MibScalar
softwareActionResult = _SoftwareActionResult_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 3, 6, 4),
    _SoftwareActionResult_Type()
)
softwareActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareActionResult.setStatus("current")
_PlcConformance_ObjectIdentity = ObjectIdentity
plcConformance = _PlcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4)
)
_PlcCompliances_ObjectIdentity = ObjectIdentity
plcCompliances = _PlcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4, 1)
)
_PlcGroups_ObjectIdentity = ObjectIdentity
plcGroups = _PlcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4, 2)
)
_IpExt_ObjectIdentity = ObjectIdentity
ipExt = _IpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22764, 1, 4)
)
if mibBuilder.loadTexts:
    ipExt.setStatus("current")
_IpDynamic_Type = TruthValue
_IpDynamic_Object = MibScalar
ipDynamic = _IpDynamic_Object(
    (1, 3, 6, 1, 4, 1, 22764, 1, 4, 1),
    _IpDynamic_Type()
)
ipDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDynamic.setStatus("current")

# Managed Objects groups

nodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4, 2, 1)
)
nodeGroup.setObjects(
      *(("SPC200", "plcNodeNotches"),
        ("SPC200", "plcMode"),
        ("SPC200", "plcNodeNotchesCarrier1"),
        ("SPC200", "plcNodeNotchesCarrier2"),
        ("SPC200", "plcNodeNotchesCarrier3"),
        ("SPC200", "plcNodeNotchesCarrier4"),
        ("SPC200", "plcNodeNotchesCarrier5"),
        ("SPC200", "plcNodeNotchesCarrier6"),
        ("SPC200", "plcNodeNotchesCarrier7"),
        ("SPC200", "plcNodeNotchesCarrier8"),
        ("SPC200", "plcNodePilots"),
        ("SPC200", "plcNodePilot1"),
        ("SPC200", "plcNodePilot2"),
        ("SPC200", "plcNodeAdaptsStringBand"),
        ("SPC200", "plcNodeAdaptsCarrier1"),
        ("SPC200", "plcNodeAdaptsCarrier2"),
        ("SPC200", "plcNodeAdaptsCarrier3"),
        ("SPC200", "plcNodeAdaptsCarrier4"),
        ("SPC200", "plcNodeAdaptsCarrier5"),
        ("SPC200", "plcNodeAdaptsCarrier6"),
        ("SPC200", "plcNodeAdaptsCarrier7"),
        ("SPC200", "plcNodeAdaptsCarrier8"),
        ("SPC200", "plcNodeIpAddr"),
        ("SPC200", "plcNodeNetMask"),
        ("SPC200", "plcNodeMacAddr"),
        ("SPC200", "plcNodeGateway"),
        ("SPC200", "plcMasterBssId"),
        ("SPC200", "plcSlaveBssId"),
        ("SPC200", "plcSpyIsDynamic"),
        ("SPC200", "plcStaticSpySynchBandNb"))
)
if mibBuilder.loadTexts:
    nodeGroup.setStatus("current")

inputNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4, 2, 2)
)
inputNodeGroup.setObjects(
      *(("SPC200", "plcNodeNotchesInputBand"),
        ("SPC200", "plcNodeNotchesInputGroup"),
        ("SPC200", "plcNodeNotchesInputCarrier1"),
        ("SPC200", "plcNodeNotchesInputCarrier2"),
        ("SPC200", "plcNodeNotchesInputCarrier3"),
        ("SPC200", "plcNodeNotchesInputCarrier4"),
        ("SPC200", "plcNodeNotchesInputCarrier5"),
        ("SPC200", "plcNodeNotchesInputCarrier6"),
        ("SPC200", "plcNodeNotchesInputCarrier7"),
        ("SPC200", "plcNodeNotchesInputCarrier8"),
        ("SPC200", "plcNodeNotchesInputProceed"),
        ("SPC200", "plcNodeNotchesInputResult"),
        ("SPC200", "plcNodePilotsInputBand"),
        ("SPC200", "plcInputNodePilot1"),
        ("SPC200", "plcInputNodePilot2"),
        ("SPC200", "plcNodePilotsInputProceed"),
        ("SPC200", "plcNodePilotsInputResult"),
        ("SPC200", "plcNodeAdaptsInputBand"),
        ("SPC200", "plcNodeAdaptsInputGroup"),
        ("SPC200", "plcNodeAdaptsInputCarrier1"),
        ("SPC200", "plcNodeAdaptsInputCarrier2"),
        ("SPC200", "plcNodeAdaptsInputCarrier3"),
        ("SPC200", "plcNodeAdaptsInputCarrier4"),
        ("SPC200", "plcNodeAdaptsInputCarrier5"),
        ("SPC200", "plcNodeAdaptsInputCarrier6"),
        ("SPC200", "plcNodeAdaptsInputCarrier7"),
        ("SPC200", "plcNodeAdaptsInputCarrier8"),
        ("SPC200", "plcNodeAdaptsInputProceed"),
        ("SPC200", "plcNodeAdaptsInputResult"),
        ("SPC200", "plcNodeActionsCommitProceed"),
        ("SPC200", "plcNodeActionsCommitResult"),
        ("SPC200", "plcNodeActionsResetProceed"),
        ("SPC200", "plcNodeActionsCarrierFlatProceed"))
)
if mibBuilder.loadTexts:
    inputNodeGroup.setStatus("current")

topologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4, 2, 3)
)
topologyGroup.setObjects(
      *(("SPC200", "plcBasePortAddress"),
        ("SPC200", "plcBasePortChannelEstimation"),
        ("SPC200", "plcBasePortAttenuation"),
        ("SPC200", "plcChannePilot2"),
        ("SPC200", "plcChannelPilot1"),
        ("SPC200", "plcRxChannelPilots"),
        ("SPC200", "plcRxLastChannelPilots"),
        ("SPC200", "plcTxChannelPilots"),
        ("SPC200", "plcRxChannelModulation"),
        ("SPC200", "plcRxLastChannelModulation"),
        ("SPC200", "plcTxChannelModulation"),
        ("SPC200", "plcModGroup1"),
        ("SPC200", "plcModGroup10"),
        ("SPC200", "plcModGroup11"),
        ("SPC200", "plcModGroup12"),
        ("SPC200", "plcModGroup13"),
        ("SPC200", "plcModGroup14"),
        ("SPC200", "plcModGroup15"),
        ("SPC200", "plcModGroup16"),
        ("SPC200", "plcModGroup2"),
        ("SPC200", "plcModGroup3"),
        ("SPC200", "plcModGroup4"),
        ("SPC200", "plcModGroup5"),
        ("SPC200", "plcModGroup6"),
        ("SPC200", "plcModGroup7"),
        ("SPC200", "plcModGroup8"),
        ("SPC200", "plcModGroup9"),
        ("SPC200", "plcPortChannelGain"),
        ("SPC200", "plcPortChannelBandwidth"),
        ("SPC200", "plcPortChannelMaxBandwidth"),
        ("SPC200", "plcPortChannelSynchronizationBand"),
        ("SPC200", "plcPortChannelType"),
        ("SPC200", "plcTopoChanges"))
)
if mibBuilder.loadTexts:
    topologyGroup.setStatus("current")

inputTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4, 2, 4)
)
inputTopologyGroup.setObjects(
      *(("SPC200", "plcModulationInputAddr"),
        ("SPC200", "plcModulationInputChannel"),
        ("SPC200", "plcModulationInputBand"),
        ("SPC200", "plcInputModulationGroup1"),
        ("SPC200", "plcInputModulationGroup2"),
        ("SPC200", "plcInputModulationGroup3"),
        ("SPC200", "plcInputModulationGroup4"),
        ("SPC200", "plcInputModulationGroup5"),
        ("SPC200", "plcInputModulationGroup6"),
        ("SPC200", "plcInputModulationGroup7"),
        ("SPC200", "plcInputModulationGroup8"),
        ("SPC200", "plcInputModulationGroup9"),
        ("SPC200", "plcInputModulationGroup10"),
        ("SPC200", "plcInputModulationGroup11"),
        ("SPC200", "plcInputModulationGroup12"),
        ("SPC200", "plcInputModulationGroup13"),
        ("SPC200", "plcInputModulationGroup14"),
        ("SPC200", "plcInputModulationGroup15"),
        ("SPC200", "plcInputModulationGroup16"),
        ("SPC200", "plcModulationInputProceed"),
        ("SPC200", "plcModulationInputResult"),
        ("SPC200", "plcPilotsInputAddr"),
        ("SPC200", "plcPilotsInputChannel"),
        ("SPC200", "plcPilotsInputBand"),
        ("SPC200", "plcInputChannelPilot1"),
        ("SPC200", "plcInputChannelPilot2"),
        ("SPC200", "plcPilotsInputProceed"),
        ("SPC200", "plcPilotsInputResult"))
)
if mibBuilder.loadTexts:
    inputTopologyGroup.setStatus("current")

statisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4, 2, 5)
)
statisticGroup.setObjects(
      *(("SPC200", "portStats2AvgBandAtt"),
        ("SPC200", "portStats2AvgBandSNR"),
        ("SPC200", "portStats2Noise"),
        ("SPC200", "portStats2Signal"),
        ("SPC200", "portStatsNoise"),
        ("SPC200", "portStatsSignal"),
        ("SPC200", "portStats3AvgAtt"),
        ("SPC200", "portStats3AvgSNR"),
        ("SPC200", "bootstatsBoot"),
        ("SPC200", "bootstatsManualReset"),
        ("SPC200", "bootstatsFailureReset"))
)
if mibBuilder.loadTexts:
    statisticGroup.setStatus("current")

softwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4, 2, 6)
)
softwareGroup.setObjects(
      *(("SPC200", "currentSoftwareVersion"),
        ("SPC200", "currentSoftwareBoardVersion"),
        ("SPC200", "currentSoftwareAFEVersion"),
        ("SPC200", "softwareVersion"),
        ("SPC200", "softwareUploadTFTPServerIP"),
        ("SPC200", "softwareUploadLogin"),
        ("SPC200", "softwareUploadPassword"),
        ("SPC200", "softwareUploadFileName"),
        ("SPC200", "softwareUploadProceed"),
        ("SPC200", "softwareUploadResult"),
        ("SPC200", "softwareUploadTFTPServerPort"),
        ("SPC200", "softwareActionIndex"),
        ("SPC200", "softwareActionType"),
        ("SPC200", "softwareActionProceed"),
        ("SPC200", "softwareActionResult"))
)
if mibBuilder.loadTexts:
    softwareGroup.setStatus("current")

analyserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4, 2, 7)
)
analyserGroup.setObjects(
      *(("SPC200", "plcSNAnalyserAGC"),
        ("SPC200", "plcSNAnalyserEnable"),
        ("SPC200", "plcSNAnalyserMinSignal"),
        ("SPC200", "plcSNAnalyserMaxSignal"),
        ("SPC200", "plcSNAnalyserAvgSignal"),
        ("SPC200", "plcSNAnalyserLastSignal"),
        ("SPC200", "plcSNAnalyserFFTDiv"),
        ("SPC200", "plcAGCAnalyserEnable"),
        ("SPC200", "plcAGCAnalyserSamplesPart1"),
        ("SPC200", "plcAGCAnalyserSamplesPart2"))
)
if mibBuilder.loadTexts:
    analyserGroup.setStatus("current")

ipExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22764, 1, 4, 2)
)
ipExtGroup.setObjects(
    ("SPC200", "ipDynamic")
)
if mibBuilder.loadTexts:
    ipExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities

agentCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    agentCapabilities.setProductRelease("Product-Release")
if mibBuilder.loadTexts:
    agentCapabilities.setStatus(
        "current"
    )


# Module compliance

plcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22764, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    plcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPC200",
    **{"ModulationValue": ModulationValue,
       "CarrierValue": CarrierValue,
       "PilotValue": PilotValue,
       "BandValue": BandValue,
       "PlcChannelType": PlcChannelType,
       "EstimationMode": EstimationMode,
       "GroupValue": GroupValue,
       "ResultValue": ResultValue,
       "AdaptValue": AdaptValue,
       "ChannelBandwidthValue": ChannelBandwidthValue,
       "SoftwareIndex": SoftwareIndex,
       "SoftwareActionResultValue": SoftwareActionResultValue,
       "SoftwareActionType": SoftwareActionType,
       "PlcModeType": PlcModeType,
       "spc200MIB": spc200MIB,
       "plc": plc,
       "stats": stats,
       "portStatsTable": portStatsTable,
       "portStatsEntry": portStatsEntry,
       "portStatsBandIndex": portStatsBandIndex,
       "portStatsGroupIndex": portStatsGroupIndex,
       "portStatsCarrierIndex": portStatsCarrierIndex,
       "portStatsSignal": portStatsSignal,
       "portStatsNoise": portStatsNoise,
       "portStats2Table": portStats2Table,
       "portStats2Entry": portStats2Entry,
       "portStats2Signal": portStats2Signal,
       "portStats2Noise": portStats2Noise,
       "portStats2AvgBandAtt": portStats2AvgBandAtt,
       "portStats2AvgBandSNR": portStats2AvgBandSNR,
       "portStats3Table": portStats3Table,
       "portStats3Entry": portStats3Entry,
       "portStats3AvgAtt": portStats3AvgAtt,
       "portStats3AvgSNR": portStats3AvgSNR,
       "bootstats": bootstats,
       "bootstatsBoot": bootstatsBoot,
       "bootstatsManualReset": bootstatsManualReset,
       "bootstatsFailureReset": bootstatsFailureReset,
       "plcObjects": plcObjects,
       "plcMode": plcMode,
       "plcTopo": plcTopo,
       "plcTopoChanges": plcTopoChanges,
       "plcBasePortTable": plcBasePortTable,
       "plcBasePortEntry": plcBasePortEntry,
       "plcBasePortIndex": plcBasePortIndex,
       "plcBasePortAddress": plcBasePortAddress,
       "plcBasePortChannelEstimation": plcBasePortChannelEstimation,
       "plcBasePortAttenuation": plcBasePortAttenuation,
       "plcChannelModulationStringTable": plcChannelModulationStringTable,
       "plcChannelModulationStringEntry": plcChannelModulationStringEntry,
       "plcRxChannelModulation": plcRxChannelModulation,
       "plcRxLastChannelModulation": plcRxLastChannelModulation,
       "plcTxChannelModulation": plcTxChannelModulation,
       "plcChannelModulationTable": plcChannelModulationTable,
       "plcChannelModulationEntry": plcChannelModulationEntry,
       "plcModBandIndex": plcModBandIndex,
       "plcModGroup1": plcModGroup1,
       "plcModGroup2": plcModGroup2,
       "plcModGroup3": plcModGroup3,
       "plcModGroup4": plcModGroup4,
       "plcModGroup5": plcModGroup5,
       "plcModGroup6": plcModGroup6,
       "plcModGroup7": plcModGroup7,
       "plcModGroup8": plcModGroup8,
       "plcModGroup9": plcModGroup9,
       "plcModGroup10": plcModGroup10,
       "plcModGroup11": plcModGroup11,
       "plcModGroup12": plcModGroup12,
       "plcModGroup13": plcModGroup13,
       "plcModGroup14": plcModGroup14,
       "plcModGroup15": plcModGroup15,
       "plcModGroup16": plcModGroup16,
       "plcChannelModulationInput": plcChannelModulationInput,
       "plcModulationInputAddr": plcModulationInputAddr,
       "plcModulationInputChannel": plcModulationInputChannel,
       "plcModulationInputBand": plcModulationInputBand,
       "plcInputModulationGroup1": plcInputModulationGroup1,
       "plcInputModulationGroup2": plcInputModulationGroup2,
       "plcInputModulationGroup3": plcInputModulationGroup3,
       "plcInputModulationGroup4": plcInputModulationGroup4,
       "plcInputModulationGroup5": plcInputModulationGroup5,
       "plcInputModulationGroup6": plcInputModulationGroup6,
       "plcInputModulationGroup7": plcInputModulationGroup7,
       "plcInputModulationGroup8": plcInputModulationGroup8,
       "plcInputModulationGroup9": plcInputModulationGroup9,
       "plcInputModulationGroup10": plcInputModulationGroup10,
       "plcInputModulationGroup11": plcInputModulationGroup11,
       "plcInputModulationGroup12": plcInputModulationGroup12,
       "plcInputModulationGroup13": plcInputModulationGroup13,
       "plcInputModulationGroup14": plcInputModulationGroup14,
       "plcInputModulationGroup15": plcInputModulationGroup15,
       "plcInputModulationGroup16": plcInputModulationGroup16,
       "plcModulationInputProceed": plcModulationInputProceed,
       "plcModulationInputResult": plcModulationInputResult,
       "plcPortChannelTable": plcPortChannelTable,
       "plcPortChannelEntry": plcPortChannelEntry,
       "plcPortChannelIndex": plcPortChannelIndex,
       "plcPortChannelType": plcPortChannelType,
       "plcPortChannelGain": plcPortChannelGain,
       "plcPortChannelBandwidth": plcPortChannelBandwidth,
       "plcPortChannelMaxBandwidth": plcPortChannelMaxBandwidth,
       "plcPortChannelSynchronizationBand": plcPortChannelSynchronizationBand,
       "plcChannelPilotStringTable": plcChannelPilotStringTable,
       "plcChannelPilotStringEntry": plcChannelPilotStringEntry,
       "plcRxChannelPilots": plcRxChannelPilots,
       "plcRxLastChannelPilots": plcRxLastChannelPilots,
       "plcTxChannelPilots": plcTxChannelPilots,
       "plcChannelPilotsTable": plcChannelPilotsTable,
       "plcChannelPilotsEntry": plcChannelPilotsEntry,
       "plcChannelPilotBandIndex": plcChannelPilotBandIndex,
       "plcChannelPilot1": plcChannelPilot1,
       "plcChannePilot2": plcChannePilot2,
       "plcChannelPilotsInput": plcChannelPilotsInput,
       "plcPilotsInputAddr": plcPilotsInputAddr,
       "plcPilotsInputChannel": plcPilotsInputChannel,
       "plcPilotsInputBand": plcPilotsInputBand,
       "plcInputChannelPilot1": plcInputChannelPilot1,
       "plcInputChannelPilot2": plcInputChannelPilot2,
       "plcPilotsInputProceed": plcPilotsInputProceed,
       "plcPilotsInputResult": plcPilotsInputResult,
       "plcNodeConfiguration": plcNodeConfiguration,
       "plcNodeNotches": plcNodeNotches,
       "plcNodeNotchesTable": plcNodeNotchesTable,
       "plcNodeNotchesEntry": plcNodeNotchesEntry,
       "plcNodeNotchesBandIndex": plcNodeNotchesBandIndex,
       "plcNodeNotchesGroupIndex": plcNodeNotchesGroupIndex,
       "plcNodeNotchesCarrier1": plcNodeNotchesCarrier1,
       "plcNodeNotchesCarrier2": plcNodeNotchesCarrier2,
       "plcNodeNotchesCarrier3": plcNodeNotchesCarrier3,
       "plcNodeNotchesCarrier4": plcNodeNotchesCarrier4,
       "plcNodeNotchesCarrier5": plcNodeNotchesCarrier5,
       "plcNodeNotchesCarrier6": plcNodeNotchesCarrier6,
       "plcNodeNotchesCarrier7": plcNodeNotchesCarrier7,
       "plcNodeNotchesCarrier8": plcNodeNotchesCarrier8,
       "plcNodeNotchesInput": plcNodeNotchesInput,
       "plcNodeNotchesInputBand": plcNodeNotchesInputBand,
       "plcNodeNotchesInputGroup": plcNodeNotchesInputGroup,
       "plcNodeNotchesInputCarrier1": plcNodeNotchesInputCarrier1,
       "plcNodeNotchesInputCarrier2": plcNodeNotchesInputCarrier2,
       "plcNodeNotchesInputCarrier3": plcNodeNotchesInputCarrier3,
       "plcNodeNotchesInputCarrier4": plcNodeNotchesInputCarrier4,
       "plcNodeNotchesInputCarrier5": plcNodeNotchesInputCarrier5,
       "plcNodeNotchesInputCarrier6": plcNodeNotchesInputCarrier6,
       "plcNodeNotchesInputCarrier7": plcNodeNotchesInputCarrier7,
       "plcNodeNotchesInputCarrier8": plcNodeNotchesInputCarrier8,
       "plcNodeNotchesInputProceed": plcNodeNotchesInputProceed,
       "plcNodeNotchesInputResult": plcNodeNotchesInputResult,
       "plcNodePilots": plcNodePilots,
       "plcNodePilotsTable": plcNodePilotsTable,
       "plcNodePilotsEntry": plcNodePilotsEntry,
       "plcNodePilotsBandIndex": plcNodePilotsBandIndex,
       "plcNodePilot1": plcNodePilot1,
       "plcNodePilot2": plcNodePilot2,
       "plcNodePilotsInput": plcNodePilotsInput,
       "plcNodePilotsInputBand": plcNodePilotsInputBand,
       "plcInputNodePilot1": plcInputNodePilot1,
       "plcInputNodePilot2": plcInputNodePilot2,
       "plcNodePilotsInputProceed": plcNodePilotsInputProceed,
       "plcNodePilotsInputResult": plcNodePilotsInputResult,
       "plcNodeAdaptsStringTable": plcNodeAdaptsStringTable,
       "plcNodeAdaptsStringEntry": plcNodeAdaptsStringEntry,
       "plcNodeAdaptsStringBandIndex": plcNodeAdaptsStringBandIndex,
       "plcNodeAdaptsStringBand": plcNodeAdaptsStringBand,
       "plcNodeAdaptsTable": plcNodeAdaptsTable,
       "plcNodeAdaptsEntry": plcNodeAdaptsEntry,
       "plcNodeAdaptsBandIndex": plcNodeAdaptsBandIndex,
       "plcNodeAdaptsGroupIndex": plcNodeAdaptsGroupIndex,
       "plcNodeAdaptsCarrier1": plcNodeAdaptsCarrier1,
       "plcNodeAdaptsCarrier2": plcNodeAdaptsCarrier2,
       "plcNodeAdaptsCarrier3": plcNodeAdaptsCarrier3,
       "plcNodeAdaptsCarrier4": plcNodeAdaptsCarrier4,
       "plcNodeAdaptsCarrier5": plcNodeAdaptsCarrier5,
       "plcNodeAdaptsCarrier6": plcNodeAdaptsCarrier6,
       "plcNodeAdaptsCarrier7": plcNodeAdaptsCarrier7,
       "plcNodeAdaptsCarrier8": plcNodeAdaptsCarrier8,
       "plcNodeAdaptsInput": plcNodeAdaptsInput,
       "plcNodeAdaptsInputBand": plcNodeAdaptsInputBand,
       "plcNodeAdaptsInputGroup": plcNodeAdaptsInputGroup,
       "plcNodeAdaptsInputCarrier1": plcNodeAdaptsInputCarrier1,
       "plcNodeAdaptsInputCarrier2": plcNodeAdaptsInputCarrier2,
       "plcNodeAdaptsInputCarrier3": plcNodeAdaptsInputCarrier3,
       "plcNodeAdaptsInputCarrier4": plcNodeAdaptsInputCarrier4,
       "plcNodeAdaptsInputCarrier5": plcNodeAdaptsInputCarrier5,
       "plcNodeAdaptsInputCarrier6": plcNodeAdaptsInputCarrier6,
       "plcNodeAdaptsInputCarrier7": plcNodeAdaptsInputCarrier7,
       "plcNodeAdaptsInputCarrier8": plcNodeAdaptsInputCarrier8,
       "plcNodeAdaptsInputProceed": plcNodeAdaptsInputProceed,
       "plcNodeAdaptsInputResult": plcNodeAdaptsInputResult,
       "plcNodeNetConfigTable": plcNodeNetConfigTable,
       "plcNodeNetConfigEntry": plcNodeNetConfigEntry,
       "plcNodeIpAddr": plcNodeIpAddr,
       "plcNodeNetMask": plcNodeNetMask,
       "plcNodeMacAddr": plcNodeMacAddr,
       "plcNodeGateway": plcNodeGateway,
       "plcNodeActions": plcNodeActions,
       "plcNodeActionsCommit": plcNodeActionsCommit,
       "plcNodeActionsCommitProceed": plcNodeActionsCommitProceed,
       "plcNodeActionsCommitResult": plcNodeActionsCommitResult,
       "plcNodeActionsReset": plcNodeActionsReset,
       "plcNodeActionsResetProceed": plcNodeActionsResetProceed,
       "plcNodeActionsCarrier": plcNodeActionsCarrier,
       "plcNodeActionsCarrierFlatProceed": plcNodeActionsCarrierFlatProceed,
       "plcSNAnalyser": plcSNAnalyser,
       "plcSNAnalyserEnable": plcSNAnalyserEnable,
       "plcSNAnalyserTable": plcSNAnalyserTable,
       "plcSNAnalyserEntry": plcSNAnalyserEntry,
       "plcSNAnalyserMinSignal": plcSNAnalyserMinSignal,
       "plcSNAnalyserMaxSignal": plcSNAnalyserMaxSignal,
       "plcSNAnalyserAvgSignal": plcSNAnalyserAvgSignal,
       "plcSNAnalyserLastSignal": plcSNAnalyserLastSignal,
       "plcSNAnalyserFFTDiv": plcSNAnalyserFFTDiv,
       "plcSNAnalyserAGC": plcSNAnalyserAGC,
       "plcAGCAnalyser": plcAGCAnalyser,
       "plcAGCAnalyserEnable": plcAGCAnalyserEnable,
       "plcAGCAnalyserSamplesPart1": plcAGCAnalyserSamplesPart1,
       "plcAGCAnalyserSamplesPart2": plcAGCAnalyserSamplesPart2,
       "plcBssId": plcBssId,
       "plcMasterBssId": plcMasterBssId,
       "plcSlaveBssId": plcSlaveBssId,
       "plcSpy": plcSpy,
       "plcSpyIsDynamic": plcSpyIsDynamic,
       "plcStaticSpySynchBandNb": plcStaticSpySynchBandNb,
       "softwareMgnt": softwareMgnt,
       "currentSoftwareVersion": currentSoftwareVersion,
       "currentSoftwareBoardVersion": currentSoftwareBoardVersion,
       "currentSoftwareAFEVersion": currentSoftwareAFEVersion,
       "softwareTable": softwareTable,
       "softwareEntry": softwareEntry,
       "softwareIndex": softwareIndex,
       "softwareVersion": softwareVersion,
       "softwareUpload": softwareUpload,
       "softwareUploadTFTPServerIP": softwareUploadTFTPServerIP,
       "softwareUploadLogin": softwareUploadLogin,
       "softwareUploadPassword": softwareUploadPassword,
       "softwareUploadFileName": softwareUploadFileName,
       "softwareUploadProceed": softwareUploadProceed,
       "softwareUploadResult": softwareUploadResult,
       "softwareUploadTFTPServerPort": softwareUploadTFTPServerPort,
       "softwareAction": softwareAction,
       "softwareActionIndex": softwareActionIndex,
       "softwareActionType": softwareActionType,
       "softwareActionProceed": softwareActionProceed,
       "softwareActionResult": softwareActionResult,
       "plcConformance": plcConformance,
       "plcCompliances": plcCompliances,
       "plcCompliance": plcCompliance,
       "plcGroups": plcGroups,
       "nodeGroup": nodeGroup,
       "inputNodeGroup": inputNodeGroup,
       "topologyGroup": topologyGroup,
       "inputTopologyGroup": inputTopologyGroup,
       "statisticGroup": statisticGroup,
       "softwareGroup": softwareGroup,
       "analyserGroup": analyserGroup,
       "agentCapabilities": agentCapabilities,
       "ipExt": ipExt,
       "ipDynamic": ipDynamic,
       "ipExtGroup": ipExtGroup}
)

# SNMP MIB module (TPT-NPSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-NPSTATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:05 2024
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

(tpt_tpa_objs,) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-objs")


# MODULE-IDENTITY

tpt_npstats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10)
)
tpt_npstats.setRevisions(
        ("2016-05-25 18:54",
         "2016-05-03 17:26")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NpstatsRulesTable_Object = MibTable
npstatsRulesTable = _NpstatsRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 1)
)
if mibBuilder.loadTexts:
    npstatsRulesTable.setStatus("current")
_NpstatsRulesEntry_Object = MibTableRow
npstatsRulesEntry = _NpstatsRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 1, 1)
)
npstatsRulesEntry.setIndexNames(
    (0, "TPT-NPSTATS-MIB", "npstatsRulesRank"),
)
if mibBuilder.loadTexts:
    npstatsRulesEntry.setStatus("current")
_NpstatsRulesRank_Type = Unsigned32
_NpstatsRulesRank_Object = MibTableColumn
npstatsRulesRank = _NpstatsRulesRank_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 1, 1, 1),
    _NpstatsRulesRank_Type()
)
npstatsRulesRank.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    npstatsRulesRank.setStatus("current")
_NpstatsRulesFilter_Type = Unsigned32
_NpstatsRulesFilter_Object = MibTableColumn
npstatsRulesFilter = _NpstatsRulesFilter_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 1, 1, 2),
    _NpstatsRulesFilter_Type()
)
npstatsRulesFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsRulesFilter.setStatus("current")
_NpstatsRulesFlows_Type = Unsigned32
_NpstatsRulesFlows_Object = MibTableColumn
npstatsRulesFlows = _NpstatsRulesFlows_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 1, 1, 3),
    _NpstatsRulesFlows_Type()
)
npstatsRulesFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsRulesFlows.setStatus("current")
_NpstatsRulesSuccess_Type = Unsigned32
_NpstatsRulesSuccess_Object = MibTableColumn
npstatsRulesSuccess = _NpstatsRulesSuccess_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 1, 1, 4),
    _NpstatsRulesSuccess_Type()
)
npstatsRulesSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsRulesSuccess.setStatus("current")
_NpstatsRulesTotalPercent_Type = Unsigned32
_NpstatsRulesTotalPercent_Object = MibTableColumn
npstatsRulesTotalPercent = _NpstatsRulesTotalPercent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 1, 1, 5),
    _NpstatsRulesTotalPercent_Type()
)
npstatsRulesTotalPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsRulesTotalPercent.setStatus("current")
_NpstatsRulesSuccessPer10K_Type = Unsigned32
_NpstatsRulesSuccessPer10K_Object = MibTableColumn
npstatsRulesSuccessPer10K = _NpstatsRulesSuccessPer10K_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 1, 1, 6),
    _NpstatsRulesSuccessPer10K_Type()
)
npstatsRulesSuccessPer10K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsRulesSuccessPer10K.setStatus("current")
_NpstatsTiersTable_Object = MibTable
npstatsTiersTable = _NpstatsTiersTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2)
)
if mibBuilder.loadTexts:
    npstatsTiersTable.setStatus("current")
_NpstatsTiersEntry_Object = MibTableRow
npstatsTiersEntry = _NpstatsTiersEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1)
)
npstatsTiersEntry.setIndexNames(
    (0, "TPT-NPSTATS-MIB", "npstatsTierNumber"),
)
if mibBuilder.loadTexts:
    npstatsTiersEntry.setStatus("current")
_NpstatsTierNumber_Type = Unsigned32
_NpstatsTierNumber_Object = MibTableColumn
npstatsTierNumber = _NpstatsTierNumber_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 1),
    _NpstatsTierNumber_Type()
)
npstatsTierNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    npstatsTierNumber.setStatus("current")
_NpstatsTiersReceiveMbps_Type = Unsigned32
_NpstatsTiersReceiveMbps_Object = MibTableColumn
npstatsTiersReceiveMbps = _NpstatsTiersReceiveMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 2),
    _NpstatsTiersReceiveMbps_Type()
)
npstatsTiersReceiveMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTiersReceiveMbps.setStatus("current")
_NpstatsTiersTransmitMbps_Type = Unsigned32
_NpstatsTiersTransmitMbps_Object = MibTableColumn
npstatsTiersTransmitMbps = _NpstatsTiersTransmitMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 3),
    _NpstatsTiersTransmitMbps_Type()
)
npstatsTiersTransmitMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTiersTransmitMbps.setStatus("current")
_NpstatsTiersRxPktsPerSec_Type = Unsigned32
_NpstatsTiersRxPktsPerSec_Object = MibTableColumn
npstatsTiersRxPktsPerSec = _NpstatsTiersRxPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 4),
    _NpstatsTiersRxPktsPerSec_Type()
)
npstatsTiersRxPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTiersRxPktsPerSec.setStatus("current")
_NpstatsTiersMaxPktsPerSec_Type = Unsigned32
_NpstatsTiersMaxPktsPerSec_Object = MibTableColumn
npstatsTiersMaxPktsPerSec = _NpstatsTiersMaxPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 5),
    _NpstatsTiersMaxPktsPerSec_Type()
)
npstatsTiersMaxPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTiersMaxPktsPerSec.setStatus("current")
_NpstatsTiersAvgBytesPerPkt_Type = Unsigned32
_NpstatsTiersAvgBytesPerPkt_Object = MibTableColumn
npstatsTiersAvgBytesPerPkt = _NpstatsTiersAvgBytesPerPkt_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 6),
    _NpstatsTiersAvgBytesPerPkt_Type()
)
npstatsTiersAvgBytesPerPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTiersAvgBytesPerPkt.setStatus("current")
_NpstatsTiersUtilizationPercent_Type = Integer32
_NpstatsTiersUtilizationPercent_Object = MibTableColumn
npstatsTiersUtilizationPercent = _NpstatsTiersUtilizationPercent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 7),
    _NpstatsTiersUtilizationPercent_Type()
)
npstatsTiersUtilizationPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTiersUtilizationPercent.setStatus("current")
_NpstatsTiersRatioToNextPer10K_Type = Unsigned32
_NpstatsTiersRatioToNextPer10K_Object = MibTableColumn
npstatsTiersRatioToNextPer10K = _NpstatsTiersRatioToNextPer10K_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 8),
    _NpstatsTiersRatioToNextPer10K_Type()
)
npstatsTiersRatioToNextPer10K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTiersRatioToNextPer10K.setStatus("current")
_NpstatsTiersMaxReceiveMbps_Type = Unsigned32
_NpstatsTiersMaxReceiveMbps_Object = MibTableColumn
npstatsTiersMaxReceiveMbps = _NpstatsTiersMaxReceiveMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 9),
    _NpstatsTiersMaxReceiveMbps_Type()
)
npstatsTiersMaxReceiveMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTiersMaxReceiveMbps.setStatus("current")
_NpstatsTiersMaxTransmitMbps_Type = Unsigned32
_NpstatsTiersMaxTransmitMbps_Object = MibTableColumn
npstatsTiersMaxTransmitMbps = _NpstatsTiersMaxTransmitMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 10),
    _NpstatsTiersMaxTransmitMbps_Type()
)
npstatsTiersMaxTransmitMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTiersMaxTransmitMbps.setStatus("current")
_NpstatsTiersMaxUtilizationPercent_Type = Integer32
_NpstatsTiersMaxUtilizationPercent_Object = MibTableColumn
npstatsTiersMaxUtilizationPercent = _NpstatsTiersMaxUtilizationPercent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 11),
    _NpstatsTiersMaxUtilizationPercent_Type()
)
npstatsTiersMaxUtilizationPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTiersMaxUtilizationPercent.setStatus("current")
_NpstatsTiersMaxRatioToNextPer10K_Type = Unsigned32
_NpstatsTiersMaxRatioToNextPer10K_Object = MibTableColumn
npstatsTiersMaxRatioToNextPer10K = _NpstatsTiersMaxRatioToNextPer10K_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 2, 1, 12),
    _NpstatsTiersMaxRatioToNextPer10K_Type()
)
npstatsTiersMaxRatioToNextPer10K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTiersMaxRatioToNextPer10K.setStatus("current")
_NpstatsTiersExtra_ObjectIdentity = ObjectIdentity
npstatsTiersExtra = _NpstatsTiersExtra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3)
)
if mibBuilder.loadTexts:
    npstatsTiersExtra.setStatus("current")
_NpstatsTier1BypassMbps_Type = Unsigned32
_NpstatsTier1BypassMbps_Object = MibScalar
npstatsTier1BypassMbps = _NpstatsTier1BypassMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 1),
    _NpstatsTier1BypassMbps_Type()
)
npstatsTier1BypassMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1BypassMbps.setStatus("current")
_NpstatsTier1Balance_Type = Unsigned32
_NpstatsTier1Balance_Object = MibScalar
npstatsTier1Balance = _NpstatsTier1Balance_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 2),
    _NpstatsTier1Balance_Type()
)
npstatsTier1Balance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1Balance.setStatus("current")
_NpstatsTier1MaxPktsPerSecA_Type = Unsigned32
_NpstatsTier1MaxPktsPerSecA_Object = MibScalar
npstatsTier1MaxPktsPerSecA = _NpstatsTier1MaxPktsPerSecA_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 3),
    _NpstatsTier1MaxPktsPerSecA_Type()
)
npstatsTier1MaxPktsPerSecA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1MaxPktsPerSecA.setStatus("current")
_NpstatsTier1MaxPktsPerSecB_Type = Unsigned32
_NpstatsTier1MaxPktsPerSecB_Object = MibScalar
npstatsTier1MaxPktsPerSecB = _NpstatsTier1MaxPktsPerSecB_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 4),
    _NpstatsTier1MaxPktsPerSecB_Type()
)
npstatsTier1MaxPktsPerSecB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1MaxPktsPerSecB.setStatus("current")
_NpstatsTier4TriggerMatchPer1000_Type = Unsigned32
_NpstatsTier4TriggerMatchPer1000_Object = MibScalar
npstatsTier4TriggerMatchPer1000 = _NpstatsTier4TriggerMatchPer1000_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 5),
    _NpstatsTier4TriggerMatchPer1000_Type()
)
npstatsTier4TriggerMatchPer1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier4TriggerMatchPer1000.setStatus("current")
_NpstatsTier4ReroutePer1000_Type = Unsigned32
_NpstatsTier4ReroutePer1000_Object = MibScalar
npstatsTier4ReroutePer1000 = _NpstatsTier4ReroutePer1000_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 6),
    _NpstatsTier4ReroutePer1000_Type()
)
npstatsTier4ReroutePer1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier4ReroutePer1000.setStatus("current")
_NpstatsTier4TcpSequencePer1000_Type = Unsigned32
_NpstatsTier4TcpSequencePer1000_Object = MibScalar
npstatsTier4TcpSequencePer1000 = _NpstatsTier4TcpSequencePer1000_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 7),
    _NpstatsTier4TcpSequencePer1000_Type()
)
npstatsTier4TcpSequencePer1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier4TcpSequencePer1000.setStatus("current")
_NpstatsTier1TxPktsPerSec_Type = Unsigned32
_NpstatsTier1TxPktsPerSec_Object = MibScalar
npstatsTier1TxPktsPerSec = _NpstatsTier1TxPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 8),
    _NpstatsTier1TxPktsPerSec_Type()
)
npstatsTier1TxPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1TxPktsPerSec.setStatus("current")
_NpstatsTier1MaxTxPktsPerSec_Type = Unsigned32
_NpstatsTier1MaxTxPktsPerSec_Object = MibScalar
npstatsTier1MaxTxPktsPerSec = _NpstatsTier1MaxTxPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 9),
    _NpstatsTier1MaxTxPktsPerSec_Type()
)
npstatsTier1MaxTxPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1MaxTxPktsPerSec.setStatus("current")
_NpstatsTier1MaxPktsPerSecC_Type = Unsigned32
_NpstatsTier1MaxPktsPerSecC_Object = MibScalar
npstatsTier1MaxPktsPerSecC = _NpstatsTier1MaxPktsPerSecC_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 10),
    _NpstatsTier1MaxPktsPerSecC_Type()
)
npstatsTier1MaxPktsPerSecC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1MaxPktsPerSecC.setStatus("current")
_NpstatsTier4ProtoDcdPer1000_Type = Unsigned32
_NpstatsTier4ProtoDcdPer1000_Object = MibScalar
npstatsTier4ProtoDcdPer1000 = _NpstatsTier4ProtoDcdPer1000_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 11),
    _NpstatsTier4ProtoDcdPer1000_Type()
)
npstatsTier4ProtoDcdPer1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier4ProtoDcdPer1000.setStatus("current")
_NpstatsTier2TxTrustedPktsPerSec_Type = Unsigned32
_NpstatsTier2TxTrustedPktsPerSec_Object = MibScalar
npstatsTier2TxTrustedPktsPerSec = _NpstatsTier2TxTrustedPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 12),
    _NpstatsTier2TxTrustedPktsPerSec_Type()
)
npstatsTier2TxTrustedPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier2TxTrustedPktsPerSec.setStatus("current")
_NpstatsTier3TxTrustedPktsPerSec_Type = Unsigned32
_NpstatsTier3TxTrustedPktsPerSec_Object = MibScalar
npstatsTier3TxTrustedPktsPerSec = _NpstatsTier3TxTrustedPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 13),
    _NpstatsTier3TxTrustedPktsPerSec_Type()
)
npstatsTier3TxTrustedPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier3TxTrustedPktsPerSec.setStatus("current")
_NpstatsTier4TxTrustedPktsPerSec_Type = Unsigned32
_NpstatsTier4TxTrustedPktsPerSec_Object = MibScalar
npstatsTier4TxTrustedPktsPerSec = _NpstatsTier4TxTrustedPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 14),
    _NpstatsTier4TxTrustedPktsPerSec_Type()
)
npstatsTier4TxTrustedPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier4TxTrustedPktsPerSec.setStatus("current")
_NpstatsTier1BypassPktsPerSec_Type = Unsigned32
_NpstatsTier1BypassPktsPerSec_Object = MibScalar
npstatsTier1BypassPktsPerSec = _NpstatsTier1BypassPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 15),
    _NpstatsTier1BypassPktsPerSec_Type()
)
npstatsTier1BypassPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1BypassPktsPerSec.setStatus("current")
_NpstatsTier1MaxBypassPktsPerSec_Type = Unsigned32
_NpstatsTier1MaxBypassPktsPerSec_Object = MibScalar
npstatsTier1MaxBypassPktsPerSec = _NpstatsTier1MaxBypassPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 16),
    _NpstatsTier1MaxBypassPktsPerSec_Type()
)
npstatsTier1MaxBypassPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1MaxBypassPktsPerSec.setStatus("current")
_NpstatsTier1BypassToRxPktsPerSecRatio_Type = Unsigned32
_NpstatsTier1BypassToRxPktsPerSecRatio_Object = MibScalar
npstatsTier1BypassToRxPktsPerSecRatio = _NpstatsTier1BypassToRxPktsPerSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 17),
    _NpstatsTier1BypassToRxPktsPerSecRatio_Type()
)
npstatsTier1BypassToRxPktsPerSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1BypassToRxPktsPerSecRatio.setStatus("current")
_NpstatsTier1VlanTransPktsPerSec_Type = Unsigned32
_NpstatsTier1VlanTransPktsPerSec_Object = MibScalar
npstatsTier1VlanTransPktsPerSec = _NpstatsTier1VlanTransPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 18),
    _NpstatsTier1VlanTransPktsPerSec_Type()
)
npstatsTier1VlanTransPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1VlanTransPktsPerSec.setStatus("current")
_NpstatsTier1MaxVlanTransPktsPerSec_Type = Unsigned32
_NpstatsTier1MaxVlanTransPktsPerSec_Object = MibScalar
npstatsTier1MaxVlanTransPktsPerSec = _NpstatsTier1MaxVlanTransPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 19),
    _NpstatsTier1MaxVlanTransPktsPerSec_Type()
)
npstatsTier1MaxVlanTransPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1MaxVlanTransPktsPerSec.setStatus("current")
_NpstatsTier1VlanTransToRxPktsPerSecRatio_Type = Unsigned32
_NpstatsTier1VlanTransToRxPktsPerSecRatio_Object = MibScalar
npstatsTier1VlanTransToRxPktsPerSecRatio = _NpstatsTier1VlanTransToRxPktsPerSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 20),
    _NpstatsTier1VlanTransToRxPktsPerSecRatio_Type()
)
npstatsTier1VlanTransToRxPktsPerSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1VlanTransToRxPktsPerSecRatio.setStatus("current")
_NpstatsTier1PatternMatchToRxPktsPerSecRatio_Type = Unsigned32
_NpstatsTier1PatternMatchToRxPktsPerSecRatio_Object = MibScalar
npstatsTier1PatternMatchToRxPktsPerSecRatio = _NpstatsTier1PatternMatchToRxPktsPerSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 21),
    _NpstatsTier1PatternMatchToRxPktsPerSecRatio_Type()
)
npstatsTier1PatternMatchToRxPktsPerSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1PatternMatchToRxPktsPerSecRatio.setStatus("current")
_NpstatsTier1MaxPatternMatchToRxPktsPerSecRatio_Type = Unsigned32
_NpstatsTier1MaxPatternMatchToRxPktsPerSecRatio_Object = MibScalar
npstatsTier1MaxPatternMatchToRxPktsPerSecRatio = _NpstatsTier1MaxPatternMatchToRxPktsPerSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 22),
    _NpstatsTier1MaxPatternMatchToRxPktsPerSecRatio_Type()
)
npstatsTier1MaxPatternMatchToRxPktsPerSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier1MaxPatternMatchToRxPktsPerSecRatio.setStatus("current")
_NpstatsTier2MaxTxTrustedPktsPerSec_Type = Unsigned32
_NpstatsTier2MaxTxTrustedPktsPerSec_Object = MibScalar
npstatsTier2MaxTxTrustedPktsPerSec = _NpstatsTier2MaxTxTrustedPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 23),
    _NpstatsTier2MaxTxTrustedPktsPerSec_Type()
)
npstatsTier2MaxTxTrustedPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier2MaxTxTrustedPktsPerSec.setStatus("current")
_NpstatsTier3MaxTxTrustedPktsPerSec_Type = Unsigned32
_NpstatsTier3MaxTxTrustedPktsPerSec_Object = MibScalar
npstatsTier3MaxTxTrustedPktsPerSec = _NpstatsTier3MaxTxTrustedPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 24),
    _NpstatsTier3MaxTxTrustedPktsPerSec_Type()
)
npstatsTier3MaxTxTrustedPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier3MaxTxTrustedPktsPerSec.setStatus("current")
_NpstatsTier4MaxTxTrustedPktsPerSec_Type = Unsigned32
_NpstatsTier4MaxTxTrustedPktsPerSec_Object = MibScalar
npstatsTier4MaxTxTrustedPktsPerSec = _NpstatsTier4MaxTxTrustedPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 25),
    _NpstatsTier4MaxTxTrustedPktsPerSec_Type()
)
npstatsTier4MaxTxTrustedPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier4MaxTxTrustedPktsPerSec.setStatus("current")
_NpstatsTier4MaxTriggerMatchPer1000_Type = Unsigned32
_NpstatsTier4MaxTriggerMatchPer1000_Object = MibScalar
npstatsTier4MaxTriggerMatchPer1000 = _NpstatsTier4MaxTriggerMatchPer1000_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 26),
    _NpstatsTier4MaxTriggerMatchPer1000_Type()
)
npstatsTier4MaxTriggerMatchPer1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier4MaxTriggerMatchPer1000.setStatus("current")
_NpstatsTier4MaxReroutePer1000_Type = Unsigned32
_NpstatsTier4MaxReroutePer1000_Object = MibScalar
npstatsTier4MaxReroutePer1000 = _NpstatsTier4MaxReroutePer1000_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 27),
    _NpstatsTier4MaxReroutePer1000_Type()
)
npstatsTier4MaxReroutePer1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier4MaxReroutePer1000.setStatus("current")
_NpstatsTier4MaxTcpSequencePer1000_Type = Unsigned32
_NpstatsTier4MaxTcpSequencePer1000_Object = MibScalar
npstatsTier4MaxTcpSequencePer1000 = _NpstatsTier4MaxTcpSequencePer1000_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 28),
    _NpstatsTier4MaxTcpSequencePer1000_Type()
)
npstatsTier4MaxTcpSequencePer1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier4MaxTcpSequencePer1000.setStatus("current")
_NpstatsTier4MaxProtoDcdPer1000_Type = Unsigned32
_NpstatsTier4MaxProtoDcdPer1000_Object = MibScalar
npstatsTier4MaxProtoDcdPer1000 = _NpstatsTier4MaxProtoDcdPer1000_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 3, 29),
    _NpstatsTier4MaxProtoDcdPer1000_Type()
)
npstatsTier4MaxProtoDcdPer1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsTier4MaxProtoDcdPer1000.setStatus("current")
_NpstatsMisc_ObjectIdentity = ObjectIdentity
npstatsMisc = _NpstatsMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 4)
)
if mibBuilder.loadTexts:
    npstatsMisc.setStatus("current")
_NpstatsMiscTxPktsBestEffort_Type = Counter64
_NpstatsMiscTxPktsBestEffort_Object = MibScalar
npstatsMiscTxPktsBestEffort = _NpstatsMiscTxPktsBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 4, 1),
    _NpstatsMiscTxPktsBestEffort_Type()
)
npstatsMiscTxPktsBestEffort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsMiscTxPktsBestEffort.setStatus("current")
_NpstatsSslInsp_ObjectIdentity = ObjectIdentity
npstatsSslInsp = _NpstatsSslInsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 5)
)
if mibBuilder.loadTexts:
    npstatsSslInsp.setStatus("current")
_NpstatsSslInspCurrentSessions_Type = Counter64
_NpstatsSslInspCurrentSessions_Object = MibScalar
npstatsSslInspCurrentSessions = _NpstatsSslInspCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 5, 1),
    _NpstatsSslInspCurrentSessions_Type()
)
npstatsSslInspCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsSslInspCurrentSessions.setStatus("current")


class _NpstatsSslInspConnectionRate_Type(DisplayString):
    """Custom type npstatsSslInspConnectionRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_NpstatsSslInspConnectionRate_Type.__name__ = "DisplayString"
_NpstatsSslInspConnectionRate_Object = MibScalar
npstatsSslInspConnectionRate = _NpstatsSslInspConnectionRate_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 5, 2),
    _NpstatsSslInspConnectionRate_Type()
)
npstatsSslInspConnectionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsSslInspConnectionRate.setStatus("current")
_NpstatsSslInspBlockedMaxConns_Type = Counter64
_NpstatsSslInspBlockedMaxConns_Object = MibScalar
npstatsSslInspBlockedMaxConns = _NpstatsSslInspBlockedMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 5, 3),
    _NpstatsSslInspBlockedMaxConns_Type()
)
npstatsSslInspBlockedMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsSslInspBlockedMaxConns.setStatus("current")
_NpstatsSslInspPassedMaxConns_Type = Counter64
_NpstatsSslInspPassedMaxConns_Object = MibScalar
npstatsSslInspPassedMaxConns = _NpstatsSslInspPassedMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 5, 4),
    _NpstatsSslInspPassedMaxConns_Type()
)
npstatsSslInspPassedMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsSslInspPassedMaxConns.setStatus("current")
_NpstatsSslInspTotalBytesIn_Type = Counter64
_NpstatsSslInspTotalBytesIn_Object = MibScalar
npstatsSslInspTotalBytesIn = _NpstatsSslInspTotalBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 5, 5),
    _NpstatsSslInspTotalBytesIn_Type()
)
npstatsSslInspTotalBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsSslInspTotalBytesIn.setStatus("current")
_NpstatsSslInspTotalBytesOut_Type = Counter64
_NpstatsSslInspTotalBytesOut_Object = MibScalar
npstatsSslInspTotalBytesOut = _NpstatsSslInspTotalBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 5, 6),
    _NpstatsSslInspTotalBytesOut_Type()
)
npstatsSslInspTotalBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsSslInspTotalBytesOut.setStatus("current")
_NpstatsStackSegmentPorts_ObjectIdentity = ObjectIdentity
npstatsStackSegmentPorts = _NpstatsStackSegmentPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10)
)
if mibBuilder.loadTexts:
    npstatsStackSegmentPorts.setStatus("current")
_NpstatsStackSegmentRecieveMbps_Type = Unsigned32
_NpstatsStackSegmentRecieveMbps_Object = MibScalar
npstatsStackSegmentRecieveMbps = _NpstatsStackSegmentRecieveMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 1),
    _NpstatsStackSegmentRecieveMbps_Type()
)
npstatsStackSegmentRecieveMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackSegmentRecieveMbps.setStatus("current")
_NpstatsStackSegmentMaxRecieveMbps_Type = Unsigned32
_NpstatsStackSegmentMaxRecieveMbps_Object = MibScalar
npstatsStackSegmentMaxRecieveMbps = _NpstatsStackSegmentMaxRecieveMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 2),
    _NpstatsStackSegmentMaxRecieveMbps_Type()
)
npstatsStackSegmentMaxRecieveMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackSegmentMaxRecieveMbps.setStatus("current")
_NpstatsStackSegmentTransmitMbps_Type = Unsigned32
_NpstatsStackSegmentTransmitMbps_Object = MibScalar
npstatsStackSegmentTransmitMbps = _NpstatsStackSegmentTransmitMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 3),
    _NpstatsStackSegmentTransmitMbps_Type()
)
npstatsStackSegmentTransmitMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackSegmentTransmitMbps.setStatus("current")
_NpstatsStackSegmentMaxTransmitMbps_Type = Unsigned32
_NpstatsStackSegmentMaxTransmitMbps_Object = MibScalar
npstatsStackSegmentMaxTransmitMbps = _NpstatsStackSegmentMaxTransmitMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 4),
    _NpstatsStackSegmentMaxTransmitMbps_Type()
)
npstatsStackSegmentMaxTransmitMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackSegmentMaxTransmitMbps.setStatus("current")
_NpstatsStackBalance_Type = Unsigned32
_NpstatsStackBalance_Object = MibScalar
npstatsStackBalance = _NpstatsStackBalance_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 5),
    _NpstatsStackBalance_Type()
)
npstatsStackBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackBalance.setStatus("current")
_NpstatsStackMinBalance_Type = Unsigned32
_NpstatsStackMinBalance_Object = MibScalar
npstatsStackMinBalance = _NpstatsStackMinBalance_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 6),
    _NpstatsStackMinBalance_Type()
)
npstatsStackMinBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackMinBalance.setStatus("current")
_NpstatsStackSegmentRatioToTier1Per10K_Type = Unsigned32
_NpstatsStackSegmentRatioToTier1Per10K_Object = MibScalar
npstatsStackSegmentRatioToTier1Per10K = _NpstatsStackSegmentRatioToTier1Per10K_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 7),
    _NpstatsStackSegmentRatioToTier1Per10K_Type()
)
npstatsStackSegmentRatioToTier1Per10K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackSegmentRatioToTier1Per10K.setStatus("current")
_NpstatsStackSegmentMaxRatioToTier1Per10K_Type = Unsigned32
_NpstatsStackSegmentMaxRatioToTier1Per10K_Object = MibScalar
npstatsStackSegmentMaxRatioToTier1Per10K = _NpstatsStackSegmentMaxRatioToTier1Per10K_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 8),
    _NpstatsStackSegmentMaxRatioToTier1Per10K_Type()
)
npstatsStackSegmentMaxRatioToTier1Per10K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackSegmentMaxRatioToTier1Per10K.setStatus("current")
_NpstatsStackSegmentPortTable_Object = MibTable
npstatsStackSegmentPortTable = _NpstatsStackSegmentPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 9)
)
if mibBuilder.loadTexts:
    npstatsStackSegmentPortTable.setStatus("current")
_NpstatsStackSegmentPortEntry_Object = MibTableRow
npstatsStackSegmentPortEntry = _NpstatsStackSegmentPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 9, 1)
)
npstatsStackSegmentPortEntry.setIndexNames(
    (0, "TPT-NPSTATS-MIB", "npstatsStackMemberIndex"),
)
if mibBuilder.loadTexts:
    npstatsStackSegmentPortEntry.setStatus("current")
_NpstatsStackMemberIndex_Type = Unsigned32
_NpstatsStackMemberIndex_Object = MibTableColumn
npstatsStackMemberIndex = _NpstatsStackMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 9, 1, 1),
    _NpstatsStackMemberIndex_Type()
)
npstatsStackMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackMemberIndex.setStatus("current")


class _NpstatsStackMemberKey_Type(OctetString):
    """Custom type npstatsStackMemberKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NpstatsStackMemberKey_Type.__name__ = "OctetString"
_NpstatsStackMemberKey_Object = MibTableColumn
npstatsStackMemberKey = _NpstatsStackMemberKey_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 9, 1, 2),
    _NpstatsStackMemberKey_Type()
)
npstatsStackMemberKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackMemberKey.setStatus("current")


class _NpstatsStackMemberHostname_Type(OctetString):
    """Custom type npstatsStackMemberHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NpstatsStackMemberHostname_Type.__name__ = "OctetString"
_NpstatsStackMemberHostname_Object = MibTableColumn
npstatsStackMemberHostname = _NpstatsStackMemberHostname_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 9, 1, 3),
    _NpstatsStackMemberHostname_Type()
)
npstatsStackMemberHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackMemberHostname.setStatus("current")
_NpstatsStackMemberSegmentReceiveMbps_Type = Unsigned32
_NpstatsStackMemberSegmentReceiveMbps_Object = MibTableColumn
npstatsStackMemberSegmentReceiveMbps = _NpstatsStackMemberSegmentReceiveMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 9, 1, 4),
    _NpstatsStackMemberSegmentReceiveMbps_Type()
)
npstatsStackMemberSegmentReceiveMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackMemberSegmentReceiveMbps.setStatus("current")
_NpstatsStackMemberMaxSegmentReceiveMbps_Type = Unsigned32
_NpstatsStackMemberMaxSegmentReceiveMbps_Object = MibTableColumn
npstatsStackMemberMaxSegmentReceiveMbps = _NpstatsStackMemberMaxSegmentReceiveMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 10, 9, 1, 5),
    _NpstatsStackMemberMaxSegmentReceiveMbps_Type()
)
npstatsStackMemberMaxSegmentReceiveMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackMemberMaxSegmentReceiveMbps.setStatus("current")
_NpstatsStackPorts_ObjectIdentity = ObjectIdentity
npstatsStackPorts = _NpstatsStackPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 11)
)
if mibBuilder.loadTexts:
    npstatsStackPorts.setStatus("current")
_NpstatsStackPortsRecieveMbps_Type = Unsigned32
_NpstatsStackPortsRecieveMbps_Object = MibScalar
npstatsStackPortsRecieveMbps = _NpstatsStackPortsRecieveMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 11, 1),
    _NpstatsStackPortsRecieveMbps_Type()
)
npstatsStackPortsRecieveMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackPortsRecieveMbps.setStatus("current")
_NpstatsStackPortsMaxRecieveMbps_Type = Unsigned32
_NpstatsStackPortsMaxRecieveMbps_Object = MibScalar
npstatsStackPortsMaxRecieveMbps = _NpstatsStackPortsMaxRecieveMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 11, 2),
    _NpstatsStackPortsMaxRecieveMbps_Type()
)
npstatsStackPortsMaxRecieveMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackPortsMaxRecieveMbps.setStatus("current")
_NpstatsStackPortsTransmitMbps_Type = Unsigned32
_NpstatsStackPortsTransmitMbps_Object = MibScalar
npstatsStackPortsTransmitMbps = _NpstatsStackPortsTransmitMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 11, 3),
    _NpstatsStackPortsTransmitMbps_Type()
)
npstatsStackPortsTransmitMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackPortsTransmitMbps.setStatus("current")
_NpstatsStackPortsMaxTransmitMbps_Type = Unsigned32
_NpstatsStackPortsMaxTransmitMbps_Object = MibScalar
npstatsStackPortsMaxTransmitMbps = _NpstatsStackPortsMaxTransmitMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 11, 4),
    _NpstatsStackPortsMaxTransmitMbps_Type()
)
npstatsStackPortsMaxTransmitMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackPortsMaxTransmitMbps.setStatus("current")
_NpstatsStackRxToStackTxMbps_Type = Unsigned32
_NpstatsStackRxToStackTxMbps_Object = MibScalar
npstatsStackRxToStackTxMbps = _NpstatsStackRxToStackTxMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 11, 5),
    _NpstatsStackRxToStackTxMbps_Type()
)
npstatsStackRxToStackTxMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackRxToStackTxMbps.setStatus("current")
_NpstatsStackMaxRxToStackTxMbps_Type = Unsigned32
_NpstatsStackMaxRxToStackTxMbps_Object = MibScalar
npstatsStackMaxRxToStackTxMbps = _NpstatsStackMaxRxToStackTxMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 11, 6),
    _NpstatsStackMaxRxToStackTxMbps_Type()
)
npstatsStackMaxRxToStackTxMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackMaxRxToStackTxMbps.setStatus("current")
_NpstatsStackRxToSegmentTxMbps_Type = Unsigned32
_NpstatsStackRxToSegmentTxMbps_Object = MibScalar
npstatsStackRxToSegmentTxMbps = _NpstatsStackRxToSegmentTxMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 11, 7),
    _NpstatsStackRxToSegmentTxMbps_Type()
)
npstatsStackRxToSegmentTxMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackRxToSegmentTxMbps.setStatus("current")
_NpstatsStackMaxRxToSegmentTxMbps_Type = Unsigned32
_NpstatsStackMaxRxToSegmentTxMbps_Object = MibScalar
npstatsStackMaxRxToSegmentTxMbps = _NpstatsStackMaxRxToSegmentTxMbps_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 11, 8),
    _NpstatsStackMaxRxToSegmentTxMbps_Type()
)
npstatsStackMaxRxToSegmentTxMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackMaxRxToSegmentTxMbps.setStatus("current")
_NpstatsStackRxToTier1_Type = Unsigned32
_NpstatsStackRxToTier1_Object = MibScalar
npstatsStackRxToTier1 = _NpstatsStackRxToTier1_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 11, 9),
    _NpstatsStackRxToTier1_Type()
)
npstatsStackRxToTier1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackRxToTier1.setStatus("current")
_NpstatsStackMaxRxToTier1_Type = Unsigned32
_NpstatsStackMaxRxToTier1_Object = MibScalar
npstatsStackMaxRxToTier1 = _NpstatsStackMaxRxToTier1_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 10, 11, 10),
    _NpstatsStackMaxRxToTier1_Type()
)
npstatsStackMaxRxToTier1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npstatsStackMaxRxToTier1.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-NPSTATS-MIB",
    **{"tpt-npstats": tpt_npstats,
       "npstatsRulesTable": npstatsRulesTable,
       "npstatsRulesEntry": npstatsRulesEntry,
       "npstatsRulesRank": npstatsRulesRank,
       "npstatsRulesFilter": npstatsRulesFilter,
       "npstatsRulesFlows": npstatsRulesFlows,
       "npstatsRulesSuccess": npstatsRulesSuccess,
       "npstatsRulesTotalPercent": npstatsRulesTotalPercent,
       "npstatsRulesSuccessPer10K": npstatsRulesSuccessPer10K,
       "npstatsTiersTable": npstatsTiersTable,
       "npstatsTiersEntry": npstatsTiersEntry,
       "npstatsTierNumber": npstatsTierNumber,
       "npstatsTiersReceiveMbps": npstatsTiersReceiveMbps,
       "npstatsTiersTransmitMbps": npstatsTiersTransmitMbps,
       "npstatsTiersRxPktsPerSec": npstatsTiersRxPktsPerSec,
       "npstatsTiersMaxPktsPerSec": npstatsTiersMaxPktsPerSec,
       "npstatsTiersAvgBytesPerPkt": npstatsTiersAvgBytesPerPkt,
       "npstatsTiersUtilizationPercent": npstatsTiersUtilizationPercent,
       "npstatsTiersRatioToNextPer10K": npstatsTiersRatioToNextPer10K,
       "npstatsTiersMaxReceiveMbps": npstatsTiersMaxReceiveMbps,
       "npstatsTiersMaxTransmitMbps": npstatsTiersMaxTransmitMbps,
       "npstatsTiersMaxUtilizationPercent": npstatsTiersMaxUtilizationPercent,
       "npstatsTiersMaxRatioToNextPer10K": npstatsTiersMaxRatioToNextPer10K,
       "npstatsTiersExtra": npstatsTiersExtra,
       "npstatsTier1BypassMbps": npstatsTier1BypassMbps,
       "npstatsTier1Balance": npstatsTier1Balance,
       "npstatsTier1MaxPktsPerSecA": npstatsTier1MaxPktsPerSecA,
       "npstatsTier1MaxPktsPerSecB": npstatsTier1MaxPktsPerSecB,
       "npstatsTier4TriggerMatchPer1000": npstatsTier4TriggerMatchPer1000,
       "npstatsTier4ReroutePer1000": npstatsTier4ReroutePer1000,
       "npstatsTier4TcpSequencePer1000": npstatsTier4TcpSequencePer1000,
       "npstatsTier1TxPktsPerSec": npstatsTier1TxPktsPerSec,
       "npstatsTier1MaxTxPktsPerSec": npstatsTier1MaxTxPktsPerSec,
       "npstatsTier1MaxPktsPerSecC": npstatsTier1MaxPktsPerSecC,
       "npstatsTier4ProtoDcdPer1000": npstatsTier4ProtoDcdPer1000,
       "npstatsTier2TxTrustedPktsPerSec": npstatsTier2TxTrustedPktsPerSec,
       "npstatsTier3TxTrustedPktsPerSec": npstatsTier3TxTrustedPktsPerSec,
       "npstatsTier4TxTrustedPktsPerSec": npstatsTier4TxTrustedPktsPerSec,
       "npstatsTier1BypassPktsPerSec": npstatsTier1BypassPktsPerSec,
       "npstatsTier1MaxBypassPktsPerSec": npstatsTier1MaxBypassPktsPerSec,
       "npstatsTier1BypassToRxPktsPerSecRatio": npstatsTier1BypassToRxPktsPerSecRatio,
       "npstatsTier1VlanTransPktsPerSec": npstatsTier1VlanTransPktsPerSec,
       "npstatsTier1MaxVlanTransPktsPerSec": npstatsTier1MaxVlanTransPktsPerSec,
       "npstatsTier1VlanTransToRxPktsPerSecRatio": npstatsTier1VlanTransToRxPktsPerSecRatio,
       "npstatsTier1PatternMatchToRxPktsPerSecRatio": npstatsTier1PatternMatchToRxPktsPerSecRatio,
       "npstatsTier1MaxPatternMatchToRxPktsPerSecRatio": npstatsTier1MaxPatternMatchToRxPktsPerSecRatio,
       "npstatsTier2MaxTxTrustedPktsPerSec": npstatsTier2MaxTxTrustedPktsPerSec,
       "npstatsTier3MaxTxTrustedPktsPerSec": npstatsTier3MaxTxTrustedPktsPerSec,
       "npstatsTier4MaxTxTrustedPktsPerSec": npstatsTier4MaxTxTrustedPktsPerSec,
       "npstatsTier4MaxTriggerMatchPer1000": npstatsTier4MaxTriggerMatchPer1000,
       "npstatsTier4MaxReroutePer1000": npstatsTier4MaxReroutePer1000,
       "npstatsTier4MaxTcpSequencePer1000": npstatsTier4MaxTcpSequencePer1000,
       "npstatsTier4MaxProtoDcdPer1000": npstatsTier4MaxProtoDcdPer1000,
       "npstatsMisc": npstatsMisc,
       "npstatsMiscTxPktsBestEffort": npstatsMiscTxPktsBestEffort,
       "npstatsSslInsp": npstatsSslInsp,
       "npstatsSslInspCurrentSessions": npstatsSslInspCurrentSessions,
       "npstatsSslInspConnectionRate": npstatsSslInspConnectionRate,
       "npstatsSslInspBlockedMaxConns": npstatsSslInspBlockedMaxConns,
       "npstatsSslInspPassedMaxConns": npstatsSslInspPassedMaxConns,
       "npstatsSslInspTotalBytesIn": npstatsSslInspTotalBytesIn,
       "npstatsSslInspTotalBytesOut": npstatsSslInspTotalBytesOut,
       "npstatsStackSegmentPorts": npstatsStackSegmentPorts,
       "npstatsStackSegmentRecieveMbps": npstatsStackSegmentRecieveMbps,
       "npstatsStackSegmentMaxRecieveMbps": npstatsStackSegmentMaxRecieveMbps,
       "npstatsStackSegmentTransmitMbps": npstatsStackSegmentTransmitMbps,
       "npstatsStackSegmentMaxTransmitMbps": npstatsStackSegmentMaxTransmitMbps,
       "npstatsStackBalance": npstatsStackBalance,
       "npstatsStackMinBalance": npstatsStackMinBalance,
       "npstatsStackSegmentRatioToTier1Per10K": npstatsStackSegmentRatioToTier1Per10K,
       "npstatsStackSegmentMaxRatioToTier1Per10K": npstatsStackSegmentMaxRatioToTier1Per10K,
       "npstatsStackSegmentPortTable": npstatsStackSegmentPortTable,
       "npstatsStackSegmentPortEntry": npstatsStackSegmentPortEntry,
       "npstatsStackMemberIndex": npstatsStackMemberIndex,
       "npstatsStackMemberKey": npstatsStackMemberKey,
       "npstatsStackMemberHostname": npstatsStackMemberHostname,
       "npstatsStackMemberSegmentReceiveMbps": npstatsStackMemberSegmentReceiveMbps,
       "npstatsStackMemberMaxSegmentReceiveMbps": npstatsStackMemberMaxSegmentReceiveMbps,
       "npstatsStackPorts": npstatsStackPorts,
       "npstatsStackPortsRecieveMbps": npstatsStackPortsRecieveMbps,
       "npstatsStackPortsMaxRecieveMbps": npstatsStackPortsMaxRecieveMbps,
       "npstatsStackPortsTransmitMbps": npstatsStackPortsTransmitMbps,
       "npstatsStackPortsMaxTransmitMbps": npstatsStackPortsMaxTransmitMbps,
       "npstatsStackRxToStackTxMbps": npstatsStackRxToStackTxMbps,
       "npstatsStackMaxRxToStackTxMbps": npstatsStackMaxRxToStackTxMbps,
       "npstatsStackRxToSegmentTxMbps": npstatsStackRxToSegmentTxMbps,
       "npstatsStackMaxRxToSegmentTxMbps": npstatsStackMaxRxToSegmentTxMbps,
       "npstatsStackRxToTier1": npstatsStackRxToTier1,
       "npstatsStackMaxRxToTier1": npstatsStackMaxRxToTier1}
)

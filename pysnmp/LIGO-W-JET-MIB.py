# SNMP MIB module (LIGO-W-JET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIGO-W-JET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:12 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ligoMgmt,) = mibBuilder.importSymbols(
    "LIGOWAVE-MIB",
    "ligoMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ligoWJetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6)
)
ligoWJetMIB.setRevisions(
        ("2009-07-16 00:00",
         "2008-11-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LigoWJetMIBObjects_ObjectIdentity = ObjectIdentity
ligoWJetMIBObjects = _LigoWJetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1)
)
_LigoWJetNotifs_ObjectIdentity = ObjectIdentity
ligoWJetNotifs = _LigoWJetNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 0)
)
_LigoWJetInfo_ObjectIdentity = ObjectIdentity
ligoWJetInfo = _LigoWJetInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 1)
)
_LigoWJetConf_ObjectIdentity = ObjectIdentity
ligoWJetConf = _LigoWJetConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2)
)
_WJetWrlssIfConfTable_Object = MibTable
wJetWrlssIfConfTable = _WJetWrlssIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wJetWrlssIfConfTable.setStatus("current")
_WJetWrlssIfConfEntry_Object = MibTableRow
wJetWrlssIfConfEntry = _WJetWrlssIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1, 1)
)
wJetWrlssIfConfEntry.setIndexNames(
    (0, "LIGO-W-JET-MIB", "wJetIfIndex"),
)
if mibBuilder.loadTexts:
    wJetWrlssIfConfEntry.setStatus("current")
_WJetIfIndex_Type = InterfaceIndex
_WJetIfIndex_Object = MibTableColumn
wJetIfIndex = _WJetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1, 1, 1),
    _WJetIfIndex_Type()
)
wJetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wJetIfIndex.setStatus("current")
_WJetIfProtoEnabled_Type = TruthValue
_WJetIfProtoEnabled_Object = MibTableColumn
wJetIfProtoEnabled = _WJetIfProtoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1, 1, 2),
    _WJetIfProtoEnabled_Type()
)
wJetIfProtoEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetIfProtoEnabled.setStatus("current")
_WJetIfDataRate_Type = Integer32
_WJetIfDataRate_Object = MibTableColumn
wJetIfDataRate = _WJetIfDataRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1, 1, 3),
    _WJetIfDataRate_Type()
)
wJetIfDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetIfDataRate.setStatus("current")
if mibBuilder.loadTexts:
    wJetIfDataRate.setUnits("kbit/s")
_WJetIfAckRate_Type = Integer32
_WJetIfAckRate_Object = MibTableColumn
wJetIfAckRate = _WJetIfAckRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1, 1, 4),
    _WJetIfAckRate_Type()
)
wJetIfAckRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetIfAckRate.setStatus("current")
if mibBuilder.loadTexts:
    wJetIfAckRate.setUnits("kbit/s")
_WJetIfAckTimeout_Type = Integer32
_WJetIfAckTimeout_Object = MibTableColumn
wJetIfAckTimeout = _WJetIfAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1, 1, 5),
    _WJetIfAckTimeout_Type()
)
wJetIfAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetIfAckTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wJetIfAckTimeout.setUnits("microseconds")
_WJetIfTxQueueMaxLength_Type = Integer32
_WJetIfTxQueueMaxLength_Object = MibTableColumn
wJetIfTxQueueMaxLength = _WJetIfTxQueueMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1, 1, 6),
    _WJetIfTxQueueMaxLength_Type()
)
wJetIfTxQueueMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetIfTxQueueMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    wJetIfTxQueueMaxLength.setUnits("frames")
_WJetIfRxTimeout_Type = Integer32
_WJetIfRxTimeout_Object = MibTableColumn
wJetIfRxTimeout = _WJetIfRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1, 1, 7),
    _WJetIfRxTimeout_Type()
)
wJetIfRxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetIfRxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wJetIfRxTimeout.setUnits("microseconds")
_WJetIfMaxAggregBytes_Type = Integer32
_WJetIfMaxAggregBytes_Object = MibTableColumn
wJetIfMaxAggregBytes = _WJetIfMaxAggregBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1, 1, 8),
    _WJetIfMaxAggregBytes_Type()
)
wJetIfMaxAggregBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetIfMaxAggregBytes.setStatus("current")
if mibBuilder.loadTexts:
    wJetIfMaxAggregBytes.setUnits("bytes")
_WJetIfMaxAggregPackets_Type = Integer32
_WJetIfMaxAggregPackets_Object = MibTableColumn
wJetIfMaxAggregPackets = _WJetIfMaxAggregPackets_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1, 1, 9),
    _WJetIfMaxAggregPackets_Type()
)
wJetIfMaxAggregPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetIfMaxAggregPackets.setStatus("current")
if mibBuilder.loadTexts:
    wJetIfMaxAggregPackets.setUnits("packets")
_WJetIfCcaThreshold_Type = Integer32
_WJetIfCcaThreshold_Object = MibTableColumn
wJetIfCcaThreshold = _WJetIfCcaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 2, 1, 1, 10),
    _WJetIfCcaThreshold_Type()
)
wJetIfCcaThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetIfCcaThreshold.setStatus("current")
_LigoWJetStats_ObjectIdentity = ObjectIdentity
ligoWJetStats = _LigoWJetStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3)
)
_WJetP2pEndpStatsTable_Object = MibTable
wJetP2pEndpStatsTable = _WJetP2pEndpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wJetP2pEndpStatsTable.setStatus("current")
_WJetP2pEndpStatsEntry_Object = MibTableRow
wJetP2pEndpStatsEntry = _WJetP2pEndpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1)
)
wJetP2pEndpStatsEntry.setIndexNames(
    (0, "LIGO-W-JET-MIB", "wJetP2pLocalIfIndex"),
    (0, "LIGO-W-JET-MIB", "wJetP2pEndpointType"),
)
if mibBuilder.loadTexts:
    wJetP2pEndpStatsEntry.setStatus("current")
_WJetP2pLocalIfIndex_Type = InterfaceIndex
_WJetP2pLocalIfIndex_Object = MibTableColumn
wJetP2pLocalIfIndex = _WJetP2pLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 1),
    _WJetP2pLocalIfIndex_Type()
)
wJetP2pLocalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wJetP2pLocalIfIndex.setStatus("current")


class _WJetP2pEndpointType_Type(Integer32):
    """Custom type wJetP2pEndpointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )


_WJetP2pEndpointType_Type.__name__ = "Integer32"
_WJetP2pEndpointType_Object = MibTableColumn
wJetP2pEndpointType = _WJetP2pEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 2),
    _WJetP2pEndpointType_Type()
)
wJetP2pEndpointType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wJetP2pEndpointType.setStatus("current")
_WJetP2pMacAddress_Type = MacAddress
_WJetP2pMacAddress_Object = MibTableColumn
wJetP2pMacAddress = _WJetP2pMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 3),
    _WJetP2pMacAddress_Type()
)
wJetP2pMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pMacAddress.setStatus("current")
_WJetP2pRssi_Type = Gauge32
_WJetP2pRssi_Object = MibTableColumn
wJetP2pRssi = _WJetP2pRssi_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 4),
    _WJetP2pRssi_Type()
)
wJetP2pRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRssi.setStatus("current")
_WJetP2pMaxRssi_Type = Gauge32
_WJetP2pMaxRssi_Object = MibTableColumn
wJetP2pMaxRssi = _WJetP2pMaxRssi_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 5),
    _WJetP2pMaxRssi_Type()
)
wJetP2pMaxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pMaxRssi.setStatus("current")
_WJetP2pSignalLevel_Type = Integer32
_WJetP2pSignalLevel_Object = MibTableColumn
wJetP2pSignalLevel = _WJetP2pSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 6),
    _WJetP2pSignalLevel_Type()
)
wJetP2pSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pSignalLevel.setUnits("dBm")
_WJetP2pNoiseLevel_Type = Integer32
_WJetP2pNoiseLevel_Object = MibTableColumn
wJetP2pNoiseLevel = _WJetP2pNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 7),
    _WJetP2pNoiseLevel_Type()
)
wJetP2pNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pNoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pNoiseLevel.setUnits("dBm")
_WJetP2pTxPower_Type = Gauge32
_WJetP2pTxPower_Object = MibTableColumn
wJetP2pTxPower = _WJetP2pTxPower_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 8),
    _WJetP2pTxPower_Type()
)
wJetP2pTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTxPower.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTxPower.setUnits("dBm")
_WJetP2pRxStart_Type = Counter32
_WJetP2pRxStart_Object = MibTableColumn
wJetP2pRxStart = _WJetP2pRxStart_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 9),
    _WJetP2pRxStart_Type()
)
wJetP2pRxStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRxStart.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pRxStart.setUnits("packets")
_WJetP2pTxStart_Type = Counter32
_WJetP2pTxStart_Object = MibTableColumn
wJetP2pTxStart = _WJetP2pTxStart_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 10),
    _WJetP2pTxStart_Type()
)
wJetP2pTxStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTxStart.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTxStart.setUnits("packets")
_WJetP2pRxStop_Type = Counter32
_WJetP2pRxStop_Object = MibTableColumn
wJetP2pRxStop = _WJetP2pRxStop_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 11),
    _WJetP2pRxStop_Type()
)
wJetP2pRxStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRxStop.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pRxStop.setUnits("packets")
_WJetP2pRxBytes_Type = Counter32
_WJetP2pRxBytes_Object = MibTableColumn
wJetP2pRxBytes = _WJetP2pRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 12),
    _WJetP2pRxBytes_Type()
)
wJetP2pRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pRxBytes.setUnits("bytes")
_WJetP2pTxBytes_Type = Counter32
_WJetP2pTxBytes_Object = MibTableColumn
wJetP2pTxBytes = _WJetP2pTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 13),
    _WJetP2pTxBytes_Type()
)
wJetP2pTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTxBytes.setUnits("bytes")
_WJetP2pRxPackets_Type = Counter32
_WJetP2pRxPackets_Object = MibTableColumn
wJetP2pRxPackets = _WJetP2pRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 14),
    _WJetP2pRxPackets_Type()
)
wJetP2pRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRxPackets.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pRxPackets.setUnits("packets")
_WJetP2pTxPackets_Type = Counter32
_WJetP2pTxPackets_Object = MibTableColumn
wJetP2pTxPackets = _WJetP2pTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 15),
    _WJetP2pTxPackets_Type()
)
wJetP2pTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTxPackets.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTxPackets.setUnits("packets")
_WJetP2pTxAcked_Type = Counter32
_WJetP2pTxAcked_Object = MibTableColumn
wJetP2pTxAcked = _WJetP2pTxAcked_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 16),
    _WJetP2pTxAcked_Type()
)
wJetP2pTxAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTxAcked.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTxAcked.setUnits("packets")
_WJetP2pRxDuplicated_Type = Counter32
_WJetP2pRxDuplicated_Object = MibTableColumn
wJetP2pRxDuplicated = _WJetP2pRxDuplicated_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 17),
    _WJetP2pRxDuplicated_Type()
)
wJetP2pRxDuplicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRxDuplicated.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pRxDuplicated.setUnits("packets")
_WJetP2pRxDropped_Type = Counter32
_WJetP2pRxDropped_Object = MibTableColumn
wJetP2pRxDropped = _WJetP2pRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 18),
    _WJetP2pRxDropped_Type()
)
wJetP2pRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRxDropped.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pRxDropped.setUnits("packets")
_WJetP2pRxTimeouts_Type = Counter32
_WJetP2pRxTimeouts_Object = MibTableColumn
wJetP2pRxTimeouts = _WJetP2pRxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 19),
    _WJetP2pRxTimeouts_Type()
)
wJetP2pRxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRxTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pRxTimeouts.setUnits("timeouts")
_WJetP2pTxTimeouts_Type = Counter32
_WJetP2pTxTimeouts_Object = MibTableColumn
wJetP2pTxTimeouts = _WJetP2pTxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 20),
    _WJetP2pTxTimeouts_Type()
)
wJetP2pTxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTxTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTxTimeouts.setUnits("timeouts")
_WJetP2pRxNoRetries_Type = Counter32
_WJetP2pRxNoRetries_Object = MibTableColumn
wJetP2pRxNoRetries = _WJetP2pRxNoRetries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 21),
    _WJetP2pRxNoRetries_Type()
)
wJetP2pRxNoRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRxNoRetries.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pRxNoRetries.setUnits("packets")
_WJetP2pTxNoRetries_Type = Counter32
_WJetP2pTxNoRetries_Object = MibTableColumn
wJetP2pTxNoRetries = _WJetP2pTxNoRetries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 22),
    _WJetP2pTxNoRetries_Type()
)
wJetP2pTxNoRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTxNoRetries.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTxNoRetries.setUnits("packets")
_WJetP2pRx1Retry_Type = Counter32
_WJetP2pRx1Retry_Object = MibTableColumn
wJetP2pRx1Retry = _WJetP2pRx1Retry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 23),
    _WJetP2pRx1Retry_Type()
)
wJetP2pRx1Retry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRx1Retry.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pRx1Retry.setUnits("packets")
_WJetP2pTx1Retry_Type = Counter32
_WJetP2pTx1Retry_Object = MibTableColumn
wJetP2pTx1Retry = _WJetP2pTx1Retry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 24),
    _WJetP2pTx1Retry_Type()
)
wJetP2pTx1Retry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTx1Retry.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTx1Retry.setUnits("packets")
_WJetP2pRx2Retries_Type = Counter32
_WJetP2pRx2Retries_Object = MibTableColumn
wJetP2pRx2Retries = _WJetP2pRx2Retries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 25),
    _WJetP2pRx2Retries_Type()
)
wJetP2pRx2Retries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRx2Retries.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pRx2Retries.setUnits("packets")
_WJetP2pTx2Retries_Type = Counter32
_WJetP2pTx2Retries_Object = MibTableColumn
wJetP2pTx2Retries = _WJetP2pTx2Retries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 26),
    _WJetP2pTx2Retries_Type()
)
wJetP2pTx2Retries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTx2Retries.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTx2Retries.setUnits("packets")
_WJetP2pRx3Retries_Type = Counter32
_WJetP2pRx3Retries_Object = MibTableColumn
wJetP2pRx3Retries = _WJetP2pRx3Retries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 27),
    _WJetP2pRx3Retries_Type()
)
wJetP2pRx3Retries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pRx3Retries.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pRx3Retries.setUnits("packets")
_WJetP2pTx3Retries_Type = Counter32
_WJetP2pTx3Retries_Object = MibTableColumn
wJetP2pTx3Retries = _WJetP2pTx3Retries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 28),
    _WJetP2pTx3Retries_Type()
)
wJetP2pTx3Retries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTx3Retries.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTx3Retries.setUnits("packets")
_WJetP2pTxTotalRetries_Type = Counter32
_WJetP2pTxTotalRetries_Object = MibTableColumn
wJetP2pTxTotalRetries = _WJetP2pTxTotalRetries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 29),
    _WJetP2pTxTotalRetries_Type()
)
wJetP2pTxTotalRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTxTotalRetries.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTxTotalRetries.setUnits("retries")
_WJetP2pTxMaxRetries_Type = Counter32
_WJetP2pTxMaxRetries_Object = MibTableColumn
wJetP2pTxMaxRetries = _WJetP2pTxMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 30),
    _WJetP2pTxMaxRetries_Type()
)
wJetP2pTxMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pTxMaxRetries.setStatus("current")
if mibBuilder.loadTexts:
    wJetP2pTxMaxRetries.setUnits("retries")
_WJetP2pIpAddress_Type = IpAddress
_WJetP2pIpAddress_Object = MibTableColumn
wJetP2pIpAddress = _WJetP2pIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 3, 1, 1, 31),
    _WJetP2pIpAddress_Type()
)
wJetP2pIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wJetP2pIpAddress.setStatus("current")

# Managed Objects groups


# Notification objects

wJetNodeConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 0, 1)
)
wJetNodeConnected.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-W-JET-MIB", "wJetP2pMacAddress"))
)
if mibBuilder.loadTexts:
    wJetNodeConnected.setStatus(
        "current"
    )

wJetNodeDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 0, 2)
)
wJetNodeDisconnected.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-W-JET-MIB", "wJetP2pMacAddress"))
)
if mibBuilder.loadTexts:
    wJetNodeDisconnected.setStatus(
        "current"
    )

wJetLowSignalStrength = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 0, 3)
)
wJetLowSignalStrength.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-W-JET-MIB", "wJetP2pMacAddress"),
        ("LIGO-W-JET-MIB", "wJetP2pRssi"))
)
if mibBuilder.loadTexts:
    wJetLowSignalStrength.setStatus(
        "current"
    )

wJetRxDroppedThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 0, 4)
)
wJetRxDroppedThresholdReached.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-W-JET-MIB", "wJetP2pMacAddress"),
        ("LIGO-W-JET-MIB", "wJetP2pRxDropped"))
)
if mibBuilder.loadTexts:
    wJetRxDroppedThresholdReached.setStatus(
        "current"
    )

wJetTxRetriesThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 6, 1, 0, 5)
)
wJetTxRetriesThresholdReached.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-W-JET-MIB", "wJetP2pMacAddress"),
        ("LIGO-W-JET-MIB", "wJetP2pTxTotalRetries"))
)
if mibBuilder.loadTexts:
    wJetTxRetriesThresholdReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIGO-W-JET-MIB",
    **{"ligoWJetMIB": ligoWJetMIB,
       "ligoWJetMIBObjects": ligoWJetMIBObjects,
       "ligoWJetNotifs": ligoWJetNotifs,
       "wJetNodeConnected": wJetNodeConnected,
       "wJetNodeDisconnected": wJetNodeDisconnected,
       "wJetLowSignalStrength": wJetLowSignalStrength,
       "wJetRxDroppedThresholdReached": wJetRxDroppedThresholdReached,
       "wJetTxRetriesThresholdReached": wJetTxRetriesThresholdReached,
       "ligoWJetInfo": ligoWJetInfo,
       "ligoWJetConf": ligoWJetConf,
       "wJetWrlssIfConfTable": wJetWrlssIfConfTable,
       "wJetWrlssIfConfEntry": wJetWrlssIfConfEntry,
       "wJetIfIndex": wJetIfIndex,
       "wJetIfProtoEnabled": wJetIfProtoEnabled,
       "wJetIfDataRate": wJetIfDataRate,
       "wJetIfAckRate": wJetIfAckRate,
       "wJetIfAckTimeout": wJetIfAckTimeout,
       "wJetIfTxQueueMaxLength": wJetIfTxQueueMaxLength,
       "wJetIfRxTimeout": wJetIfRxTimeout,
       "wJetIfMaxAggregBytes": wJetIfMaxAggregBytes,
       "wJetIfMaxAggregPackets": wJetIfMaxAggregPackets,
       "wJetIfCcaThreshold": wJetIfCcaThreshold,
       "ligoWJetStats": ligoWJetStats,
       "wJetP2pEndpStatsTable": wJetP2pEndpStatsTable,
       "wJetP2pEndpStatsEntry": wJetP2pEndpStatsEntry,
       "wJetP2pLocalIfIndex": wJetP2pLocalIfIndex,
       "wJetP2pEndpointType": wJetP2pEndpointType,
       "wJetP2pMacAddress": wJetP2pMacAddress,
       "wJetP2pRssi": wJetP2pRssi,
       "wJetP2pMaxRssi": wJetP2pMaxRssi,
       "wJetP2pSignalLevel": wJetP2pSignalLevel,
       "wJetP2pNoiseLevel": wJetP2pNoiseLevel,
       "wJetP2pTxPower": wJetP2pTxPower,
       "wJetP2pRxStart": wJetP2pRxStart,
       "wJetP2pTxStart": wJetP2pTxStart,
       "wJetP2pRxStop": wJetP2pRxStop,
       "wJetP2pRxBytes": wJetP2pRxBytes,
       "wJetP2pTxBytes": wJetP2pTxBytes,
       "wJetP2pRxPackets": wJetP2pRxPackets,
       "wJetP2pTxPackets": wJetP2pTxPackets,
       "wJetP2pTxAcked": wJetP2pTxAcked,
       "wJetP2pRxDuplicated": wJetP2pRxDuplicated,
       "wJetP2pRxDropped": wJetP2pRxDropped,
       "wJetP2pRxTimeouts": wJetP2pRxTimeouts,
       "wJetP2pTxTimeouts": wJetP2pTxTimeouts,
       "wJetP2pRxNoRetries": wJetP2pRxNoRetries,
       "wJetP2pTxNoRetries": wJetP2pTxNoRetries,
       "wJetP2pRx1Retry": wJetP2pRx1Retry,
       "wJetP2pTx1Retry": wJetP2pTx1Retry,
       "wJetP2pRx2Retries": wJetP2pRx2Retries,
       "wJetP2pTx2Retries": wJetP2pTx2Retries,
       "wJetP2pRx3Retries": wJetP2pRx3Retries,
       "wJetP2pTx3Retries": wJetP2pTx3Retries,
       "wJetP2pTxTotalRetries": wJetP2pTxTotalRetries,
       "wJetP2pTxMaxRetries": wJetP2pTxMaxRetries,
       "wJetP2pIpAddress": wJetP2pIpAddress}
)

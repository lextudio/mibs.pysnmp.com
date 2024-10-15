# SNMP MIB module (CISCO-ENHANCED-IPSEC-FLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENHANCED-IPSEC-FLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:23 2024
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

(CIPsecAuthAlgorithm,
 CIPsecCompAlgorithm,
 CIPsecControlProtocol,
 CIPsecDiffHellmanGrp,
 CIPsecEncapMode,
 CIPsecEncryptAlgorithm,
 CIPsecEncryptionKeySize,
 CIPsecEndPtType,
 CIPsecNATTraversalMode,
 CIPsecPhase1TunnelIndexOrZero,
 CIPsecPhase2SaDirection,
 CIPsecPhase2TunnelIndex,
 CIPsecPmtu,
 CIPsecProtocol,
 CIPsecSpi,
 CIPsecTunnelStatus) = mibBuilder.importSymbols(
    "CISCO-IPSEC-TC",
    "CIPsecAuthAlgorithm",
    "CIPsecCompAlgorithm",
    "CIPsecControlProtocol",
    "CIPsecDiffHellmanGrp",
    "CIPsecEncapMode",
    "CIPsecEncryptAlgorithm",
    "CIPsecEncryptionKeySize",
    "CIPsecEndPtType",
    "CIPsecNATTraversalMode",
    "CIPsecPhase1TunnelIndexOrZero",
    "CIPsecPhase2SaDirection",
    "CIPsecPhase2TunnelIndex",
    "CIPsecPmtu",
    "CIPsecProtocol",
    "CIPsecSpi",
    "CIPsecTunnelStatus")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoIpProtocol,
 CiscoPort) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoIpProtocol",
    "CiscoPort")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoEnhancedIpsecFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432)
)
ciscoEnhancedIpsecFlowMIB.setRevisions(
        ("2013-06-28 00:00",
         "2011-07-19 00:00",
         "2005-01-12 00:00",
         "2004-08-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoEnhancedIpsecFlowMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEnhancedIpsecFlowMIBNotifs = _CiscoEnhancedIpsecFlowMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 0)
)
_CiscoEnhancedIpsecFlowMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEnhancedIpsecFlowMIBObjects = _CiscoEnhancedIpsecFlowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1)
)
_CeipSecPhaseTwo_ObjectIdentity = ObjectIdentity
ceipSecPhaseTwo = _CeipSecPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1)
)
_CeipSecGlobalStats_ObjectIdentity = ObjectIdentity
ceipSecGlobalStats = _CeipSecGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1)
)
_CeipSecGlobalActiveTunnels_Type = Gauge32
_CeipSecGlobalActiveTunnels_Object = MibScalar
ceipSecGlobalActiveTunnels = _CeipSecGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 1),
    _CeipSecGlobalActiveTunnels_Type()
)
ceipSecGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalActiveTunnels.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalActiveTunnels.setUnits("Tunnels")
_CeipSecGlobalPreviousTunnels_Type = Counter64
_CeipSecGlobalPreviousTunnels_Object = MibScalar
ceipSecGlobalPreviousTunnels = _CeipSecGlobalPreviousTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 2),
    _CeipSecGlobalPreviousTunnels_Type()
)
ceipSecGlobalPreviousTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalPreviousTunnels.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalPreviousTunnels.setUnits("Tunnels")
_CeipSecGlobalInOctets_Type = Counter64
_CeipSecGlobalInOctets_Object = MibScalar
ceipSecGlobalInOctets = _CeipSecGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 3),
    _CeipSecGlobalInOctets_Type()
)
ceipSecGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalInOctets.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalInOctets.setUnits("Octets")
_CeipSecGlobalInDecompOctets_Type = Counter64
_CeipSecGlobalInDecompOctets_Object = MibScalar
ceipSecGlobalInDecompOctets = _CeipSecGlobalInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 4),
    _CeipSecGlobalInDecompOctets_Type()
)
ceipSecGlobalInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalInDecompOctets.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalInDecompOctets.setUnits("Octets")
_CeipSecGlobalInPkts_Type = Counter64
_CeipSecGlobalInPkts_Object = MibScalar
ceipSecGlobalInPkts = _CeipSecGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 5),
    _CeipSecGlobalInPkts_Type()
)
ceipSecGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalInPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalInPkts.setUnits("Packets")
_CeipSecGlobalInDrops_Type = Counter64
_CeipSecGlobalInDrops_Object = MibScalar
ceipSecGlobalInDrops = _CeipSecGlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 6),
    _CeipSecGlobalInDrops_Type()
)
ceipSecGlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalInDrops.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalInDrops.setUnits("Packets")
_CeipSecGlobalInReplayDrops_Type = Counter64
_CeipSecGlobalInReplayDrops_Object = MibScalar
ceipSecGlobalInReplayDrops = _CeipSecGlobalInReplayDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 7),
    _CeipSecGlobalInReplayDrops_Type()
)
ceipSecGlobalInReplayDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalInReplayDrops.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalInReplayDrops.setUnits("Packets")
_CeipSecGlobalInAuths_Type = Counter64
_CeipSecGlobalInAuths_Object = MibScalar
ceipSecGlobalInAuths = _CeipSecGlobalInAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 8),
    _CeipSecGlobalInAuths_Type()
)
ceipSecGlobalInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalInAuths.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalInAuths.setUnits("Events")
_CeipSecGlobalInAuthFails_Type = Counter64
_CeipSecGlobalInAuthFails_Object = MibScalar
ceipSecGlobalInAuthFails = _CeipSecGlobalInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 9),
    _CeipSecGlobalInAuthFails_Type()
)
ceipSecGlobalInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalInAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalInAuthFails.setUnits("Failures")
_CeipSecGlobalInDecrypts_Type = Counter64
_CeipSecGlobalInDecrypts_Object = MibScalar
ceipSecGlobalInDecrypts = _CeipSecGlobalInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 10),
    _CeipSecGlobalInDecrypts_Type()
)
ceipSecGlobalInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalInDecrypts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalInDecrypts.setUnits("Packets")
_CeipSecGlobalInDecryptFails_Type = Counter64
_CeipSecGlobalInDecryptFails_Object = MibScalar
ceipSecGlobalInDecryptFails = _CeipSecGlobalInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 11),
    _CeipSecGlobalInDecryptFails_Type()
)
ceipSecGlobalInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalInDecryptFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalInDecryptFails.setUnits("Failures")
_CeipSecGlobalOutOctets_Type = Counter64
_CeipSecGlobalOutOctets_Object = MibScalar
ceipSecGlobalOutOctets = _CeipSecGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 12),
    _CeipSecGlobalOutOctets_Type()
)
ceipSecGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutOctets.setUnits("Octets")
_CeipSecGlobalOutUncompOctets_Type = Counter64
_CeipSecGlobalOutUncompOctets_Object = MibScalar
ceipSecGlobalOutUncompOctets = _CeipSecGlobalOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 13),
    _CeipSecGlobalOutUncompOctets_Type()
)
ceipSecGlobalOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutUncompOctets.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutUncompOctets.setUnits("Octets")
_CeipSecGlobalOutPkts_Type = Counter64
_CeipSecGlobalOutPkts_Object = MibScalar
ceipSecGlobalOutPkts = _CeipSecGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 14),
    _CeipSecGlobalOutPkts_Type()
)
ceipSecGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutPkts.setUnits("Packets")
_CeipSecGlobalOutDrops_Type = Counter64
_CeipSecGlobalOutDrops_Object = MibScalar
ceipSecGlobalOutDrops = _CeipSecGlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 15),
    _CeipSecGlobalOutDrops_Type()
)
ceipSecGlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutDrops.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutDrops.setUnits("Packets")
_CeipSecGlobalOutAuths_Type = Counter64
_CeipSecGlobalOutAuths_Object = MibScalar
ceipSecGlobalOutAuths = _CeipSecGlobalOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 16),
    _CeipSecGlobalOutAuths_Type()
)
ceipSecGlobalOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutAuths.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutAuths.setUnits("Events")
_CeipSecGlobalOutAuthFails_Type = Counter64
_CeipSecGlobalOutAuthFails_Object = MibScalar
ceipSecGlobalOutAuthFails = _CeipSecGlobalOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 17),
    _CeipSecGlobalOutAuthFails_Type()
)
ceipSecGlobalOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutAuthFails.setUnits("Failures")
_CeipSecGlobalOutEncrypts_Type = Counter64
_CeipSecGlobalOutEncrypts_Object = MibScalar
ceipSecGlobalOutEncrypts = _CeipSecGlobalOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 18),
    _CeipSecGlobalOutEncrypts_Type()
)
ceipSecGlobalOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutEncrypts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutEncrypts.setUnits("Packets")
_CeipSecGlobalOutEncryptFails_Type = Counter64
_CeipSecGlobalOutEncryptFails_Object = MibScalar
ceipSecGlobalOutEncryptFails = _CeipSecGlobalOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 19),
    _CeipSecGlobalOutEncryptFails_Type()
)
ceipSecGlobalOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutEncryptFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutEncryptFails.setUnits("Failures")
_CeipSecGlobalProtocolUseFails_Type = Counter64
_CeipSecGlobalProtocolUseFails_Object = MibScalar
ceipSecGlobalProtocolUseFails = _CeipSecGlobalProtocolUseFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 20),
    _CeipSecGlobalProtocolUseFails_Type()
)
ceipSecGlobalProtocolUseFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalProtocolUseFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalProtocolUseFails.setUnits("Failures")
_CeipSecGlobalNoSaFails_Type = Counter64
_CeipSecGlobalNoSaFails_Object = MibScalar
ceipSecGlobalNoSaFails = _CeipSecGlobalNoSaFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 21),
    _CeipSecGlobalNoSaFails_Type()
)
ceipSecGlobalNoSaFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalNoSaFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalNoSaFails.setUnits("Failures")
_CeipSecGlobalSysCapFails_Type = Counter64
_CeipSecGlobalSysCapFails_Object = MibScalar
ceipSecGlobalSysCapFails = _CeipSecGlobalSysCapFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 22),
    _CeipSecGlobalSysCapFails_Type()
)
ceipSecGlobalSysCapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalSysCapFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalSysCapFails.setUnits("Failures")
_CeipSecGlobalOutCompressedPkts_Type = Counter64
_CeipSecGlobalOutCompressedPkts_Object = MibScalar
ceipSecGlobalOutCompressedPkts = _CeipSecGlobalOutCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 23),
    _CeipSecGlobalOutCompressedPkts_Type()
)
ceipSecGlobalOutCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutCompressedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutCompressedPkts.setUnits("Packets")
_CeipSecGlobalOutCompSkippedPkts_Type = Counter64
_CeipSecGlobalOutCompSkippedPkts_Object = MibScalar
ceipSecGlobalOutCompSkippedPkts = _CeipSecGlobalOutCompSkippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 24),
    _CeipSecGlobalOutCompSkippedPkts_Type()
)
ceipSecGlobalOutCompSkippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutCompSkippedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutCompSkippedPkts.setUnits("Packets")
_CeipSecGlobalOutCompFailPkts_Type = Counter64
_CeipSecGlobalOutCompFailPkts_Object = MibScalar
ceipSecGlobalOutCompFailPkts = _CeipSecGlobalOutCompFailPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 25),
    _CeipSecGlobalOutCompFailPkts_Type()
)
ceipSecGlobalOutCompFailPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutCompFailPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutCompFailPkts.setUnits("Packets")
_CeipSecGlobalOutCompTooSmallPkts_Type = Counter64
_CeipSecGlobalOutCompTooSmallPkts_Object = MibScalar
ceipSecGlobalOutCompTooSmallPkts = _CeipSecGlobalOutCompTooSmallPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 26),
    _CeipSecGlobalOutCompTooSmallPkts_Type()
)
ceipSecGlobalOutCompTooSmallPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalOutCompTooSmallPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalOutCompTooSmallPkts.setUnits("Packets")
_CeipSecGlobalThroughputUtilizatioinTimeInterval_Type = Unsigned32
_CeipSecGlobalThroughputUtilizatioinTimeInterval_Object = MibScalar
ceipSecGlobalThroughputUtilizatioinTimeInterval = _CeipSecGlobalThroughputUtilizatioinTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 27),
    _CeipSecGlobalThroughputUtilizatioinTimeInterval_Type()
)
ceipSecGlobalThroughputUtilizatioinTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalThroughputUtilizatioinTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalThroughputUtilizatioinTimeInterval.setUnits("Seconds")
_CeipSecGlobalThroughputLastUpdatedTime_Type = TimeStamp
_CeipSecGlobalThroughputLastUpdatedTime_Object = MibScalar
ceipSecGlobalThroughputLastUpdatedTime = _CeipSecGlobalThroughputLastUpdatedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 28),
    _CeipSecGlobalThroughputLastUpdatedTime_Type()
)
ceipSecGlobalThroughputLastUpdatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalThroughputLastUpdatedTime.setStatus("current")
_CeipSecGlobalLastAveragePacketSize_Type = Unsigned32
_CeipSecGlobalLastAveragePacketSize_Object = MibScalar
ceipSecGlobalLastAveragePacketSize = _CeipSecGlobalLastAveragePacketSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 29),
    _CeipSecGlobalLastAveragePacketSize_Type()
)
ceipSecGlobalLastAveragePacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalLastAveragePacketSize.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalLastAveragePacketSize.setUnits("bytes")
_CeipSecGlobalLastThroughputInMbps_Type = Unsigned32
_CeipSecGlobalLastThroughputInMbps_Object = MibScalar
ceipSecGlobalLastThroughputInMbps = _CeipSecGlobalLastThroughputInMbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 30),
    _CeipSecGlobalLastThroughputInMbps_Type()
)
ceipSecGlobalLastThroughputInMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalLastThroughputInMbps.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalLastThroughputInMbps.setUnits("Mbps")
_CeipSecGlobalLastThroughputInKpps_Type = Unsigned32
_CeipSecGlobalLastThroughputInKpps_Object = MibScalar
ceipSecGlobalLastThroughputInKpps = _CeipSecGlobalLastThroughputInKpps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 31),
    _CeipSecGlobalLastThroughputInKpps_Type()
)
ceipSecGlobalLastThroughputInKpps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalLastThroughputInKpps.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalLastThroughputInKpps.setUnits("Kpps")
_CeipSecGlobalLastThroughputUtilization_Type = Unsigned32
_CeipSecGlobalLastThroughputUtilization_Object = MibScalar
ceipSecGlobalLastThroughputUtilization = _CeipSecGlobalLastThroughputUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 32),
    _CeipSecGlobalLastThroughputUtilization_Type()
)
ceipSecGlobalLastThroughputUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalLastThroughputUtilization.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalLastThroughputUtilization.setUnits("Percent")
_CeipSecGlobalPeakThroughputUtilization_Type = Unsigned32
_CeipSecGlobalPeakThroughputUtilization_Object = MibScalar
ceipSecGlobalPeakThroughputUtilization = _CeipSecGlobalPeakThroughputUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 33),
    _CeipSecGlobalPeakThroughputUtilization_Type()
)
ceipSecGlobalPeakThroughputUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalPeakThroughputUtilization.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalPeakThroughputUtilization.setUnits("Percent")
_CeipSecGlobalPeakThroughputDateAndTime_Type = DateAndTime
_CeipSecGlobalPeakThroughputDateAndTime_Object = MibScalar
ceipSecGlobalPeakThroughputDateAndTime = _CeipSecGlobalPeakThroughputDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 34),
    _CeipSecGlobalPeakThroughputDateAndTime_Type()
)
ceipSecGlobalPeakThroughputDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalPeakThroughputDateAndTime.setStatus("current")
_CeipSecGlobalPeakThroughputInMbps_Type = Unsigned32
_CeipSecGlobalPeakThroughputInMbps_Object = MibScalar
ceipSecGlobalPeakThroughputInMbps = _CeipSecGlobalPeakThroughputInMbps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 35),
    _CeipSecGlobalPeakThroughputInMbps_Type()
)
ceipSecGlobalPeakThroughputInMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalPeakThroughputInMbps.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalPeakThroughputInMbps.setUnits("Mbps")
_CeipSecGlobalPeakAvgPacketSize_Type = Unsigned32
_CeipSecGlobalPeakAvgPacketSize_Object = MibScalar
ceipSecGlobalPeakAvgPacketSize = _CeipSecGlobalPeakAvgPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 1, 36),
    _CeipSecGlobalPeakAvgPacketSize_Type()
)
ceipSecGlobalPeakAvgPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecGlobalPeakAvgPacketSize.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecGlobalPeakAvgPacketSize.setUnits("bytes")
_CeipSecTunnelTable_Object = MibTable
ceipSecTunnelTable = _CeipSecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ceipSecTunnelTable.setStatus("current")
_CeipSecTunnelEntry_Object = MibTableRow
ceipSecTunnelEntry = _CeipSecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1)
)
ceipSecTunnelEntry.setIndexNames(
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunIndex"),
)
if mibBuilder.loadTexts:
    ceipSecTunnelEntry.setStatus("current")
_CeipSecTunIndex_Type = CIPsecPhase2TunnelIndex
_CeipSecTunIndex_Object = MibTableColumn
ceipSecTunIndex = _CeipSecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 1),
    _CeipSecTunIndex_Type()
)
ceipSecTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceipSecTunIndex.setStatus("current")
_CeipSecTunLocalAddressType_Type = InetAddressType
_CeipSecTunLocalAddressType_Object = MibTableColumn
ceipSecTunLocalAddressType = _CeipSecTunLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 2),
    _CeipSecTunLocalAddressType_Type()
)
ceipSecTunLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunLocalAddressType.setStatus("current")
_CeipSecTunLocalAddress_Type = InetAddress
_CeipSecTunLocalAddress_Object = MibTableColumn
ceipSecTunLocalAddress = _CeipSecTunLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 3),
    _CeipSecTunLocalAddress_Type()
)
ceipSecTunLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunLocalAddress.setStatus("current")
_CeipSecTunRemoteAddressType_Type = InetAddressType
_CeipSecTunRemoteAddressType_Object = MibTableColumn
ceipSecTunRemoteAddressType = _CeipSecTunRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 4),
    _CeipSecTunRemoteAddressType_Type()
)
ceipSecTunRemoteAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunRemoteAddressType.setStatus("current")
_CeipSecTunRemoteAddress_Type = InetAddress
_CeipSecTunRemoteAddress_Object = MibTableColumn
ceipSecTunRemoteAddress = _CeipSecTunRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 5),
    _CeipSecTunRemoteAddress_Type()
)
ceipSecTunRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunRemoteAddress.setStatus("current")
_CeipSecTunControlProtocol_Type = CIPsecControlProtocol
_CeipSecTunControlProtocol_Object = MibTableColumn
ceipSecTunControlProtocol = _CeipSecTunControlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 6),
    _CeipSecTunControlProtocol_Type()
)
ceipSecTunControlProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunControlProtocol.setStatus("current")
_CeipSecTunControlTunnelIndex_Type = CIPsecPhase1TunnelIndexOrZero
_CeipSecTunControlTunnelIndex_Object = MibTableColumn
ceipSecTunControlTunnelIndex = _CeipSecTunControlTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 7),
    _CeipSecTunControlTunnelIndex_Type()
)
ceipSecTunControlTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunControlTunnelIndex.setStatus("current")
_CeipSecTunControlTunnelAlive_Type = TruthValue
_CeipSecTunControlTunnelAlive_Object = MibTableColumn
ceipSecTunControlTunnelAlive = _CeipSecTunControlTunnelAlive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 8),
    _CeipSecTunControlTunnelAlive_Type()
)
ceipSecTunControlTunnelAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunControlTunnelAlive.setStatus("current")
_CeipSecTunEncapMode_Type = CIPsecEncapMode
_CeipSecTunEncapMode_Object = MibTableColumn
ceipSecTunEncapMode = _CeipSecTunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 9),
    _CeipSecTunEncapMode_Type()
)
ceipSecTunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunEncapMode.setStatus("current")
_CeipSecTunNATTraversalMode_Type = CIPsecNATTraversalMode
_CeipSecTunNATTraversalMode_Object = MibTableColumn
ceipSecTunNATTraversalMode = _CeipSecTunNATTraversalMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 10),
    _CeipSecTunNATTraversalMode_Type()
)
ceipSecTunNATTraversalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunNATTraversalMode.setStatus("current")


class _CeipSecTunLifeSize_Type(Unsigned32):
    """Custom type ceipSecTunLifeSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeipSecTunLifeSize_Type.__name__ = "Unsigned32"
_CeipSecTunLifeSize_Object = MibTableColumn
ceipSecTunLifeSize = _CeipSecTunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 11),
    _CeipSecTunLifeSize_Type()
)
ceipSecTunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunLifeSize.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunLifeSize.setUnits("KBytes")
_CeipSecTunLifeTime_Type = Unsigned32
_CeipSecTunLifeTime_Object = MibTableColumn
ceipSecTunLifeTime = _CeipSecTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 12),
    _CeipSecTunLifeTime_Type()
)
ceipSecTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunLifeTime.setUnits("Seconds")
_CeipSecTunActiveTime_Type = TimeInterval
_CeipSecTunActiveTime_Object = MibTableColumn
ceipSecTunActiveTime = _CeipSecTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 13),
    _CeipSecTunActiveTime_Type()
)
ceipSecTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunActiveTime.setStatus("current")
_CeipSecTunSaLifeSizeThreshold_Type = Unsigned32
_CeipSecTunSaLifeSizeThreshold_Object = MibTableColumn
ceipSecTunSaLifeSizeThreshold = _CeipSecTunSaLifeSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 14),
    _CeipSecTunSaLifeSizeThreshold_Type()
)
ceipSecTunSaLifeSizeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaLifeSizeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunSaLifeSizeThreshold.setUnits("KBytes")
_CeipSecTunSaLifeTimeThreshold_Type = Unsigned32
_CeipSecTunSaLifeTimeThreshold_Object = MibTableColumn
ceipSecTunSaLifeTimeThreshold = _CeipSecTunSaLifeTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 15),
    _CeipSecTunSaLifeTimeThreshold_Type()
)
ceipSecTunSaLifeTimeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaLifeTimeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunSaLifeTimeThreshold.setUnits("Seconds")
_CeipSecTunTotalRefreshes_Type = Counter32
_CeipSecTunTotalRefreshes_Object = MibTableColumn
ceipSecTunTotalRefreshes = _CeipSecTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 16),
    _CeipSecTunTotalRefreshes_Type()
)
ceipSecTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunTotalRefreshes.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunTotalRefreshes.setUnits("QM Exchanges")
_CeipSecTunExpiredSaInstances_Type = Counter32
_CeipSecTunExpiredSaInstances_Object = MibTableColumn
ceipSecTunExpiredSaInstances = _CeipSecTunExpiredSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 17),
    _CeipSecTunExpiredSaInstances_Type()
)
ceipSecTunExpiredSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunExpiredSaInstances.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunExpiredSaInstances.setUnits("SAs")
_CeipSecTunCurrentSaInstances_Type = Gauge32
_CeipSecTunCurrentSaInstances_Object = MibTableColumn
ceipSecTunCurrentSaInstances = _CeipSecTunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 18),
    _CeipSecTunCurrentSaInstances_Type()
)
ceipSecTunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunCurrentSaInstances.setStatus("current")
_CeipSecTunInSaDHGrp_Type = CIPsecDiffHellmanGrp
_CeipSecTunInSaDHGrp_Object = MibTableColumn
ceipSecTunInSaDHGrp = _CeipSecTunInSaDHGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 19),
    _CeipSecTunInSaDHGrp_Type()
)
ceipSecTunInSaDHGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInSaDHGrp.setStatus("current")
_CeipSecTunInSaEncryptAlgo_Type = CIPsecEncryptAlgorithm
_CeipSecTunInSaEncryptAlgo_Object = MibTableColumn
ceipSecTunInSaEncryptAlgo = _CeipSecTunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 20),
    _CeipSecTunInSaEncryptAlgo_Type()
)
ceipSecTunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInSaEncryptAlgo.setStatus("current")
_CeipSecTunInSaEncryptKeySize_Type = CIPsecEncryptionKeySize
_CeipSecTunInSaEncryptKeySize_Object = MibTableColumn
ceipSecTunInSaEncryptKeySize = _CeipSecTunInSaEncryptKeySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 21),
    _CeipSecTunInSaEncryptKeySize_Type()
)
ceipSecTunInSaEncryptKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInSaEncryptKeySize.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunInSaEncryptKeySize.setUnits("Bits")
_CeipSecTunInSaAhAuthAlgo_Type = CIPsecAuthAlgorithm
_CeipSecTunInSaAhAuthAlgo_Object = MibTableColumn
ceipSecTunInSaAhAuthAlgo = _CeipSecTunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 22),
    _CeipSecTunInSaAhAuthAlgo_Type()
)
ceipSecTunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInSaAhAuthAlgo.setStatus("current")
_CeipSecTunInSaEspAuthAlgo_Type = CIPsecAuthAlgorithm
_CeipSecTunInSaEspAuthAlgo_Object = MibTableColumn
ceipSecTunInSaEspAuthAlgo = _CeipSecTunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 23),
    _CeipSecTunInSaEspAuthAlgo_Type()
)
ceipSecTunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInSaEspAuthAlgo.setStatus("current")
_CeipSecTunInSaDecompAlgo_Type = CIPsecCompAlgorithm
_CeipSecTunInSaDecompAlgo_Object = MibTableColumn
ceipSecTunInSaDecompAlgo = _CeipSecTunInSaDecompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 24),
    _CeipSecTunInSaDecompAlgo_Type()
)
ceipSecTunInSaDecompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInSaDecompAlgo.setStatus("current")
_CeipSecTunOutSaDHGrp_Type = CIPsecDiffHellmanGrp
_CeipSecTunOutSaDHGrp_Object = MibTableColumn
ceipSecTunOutSaDHGrp = _CeipSecTunOutSaDHGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 25),
    _CeipSecTunOutSaDHGrp_Type()
)
ceipSecTunOutSaDHGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutSaDHGrp.setStatus("current")
_CeipSecTunOutSaEncryptAlgo_Type = CIPsecEncryptAlgorithm
_CeipSecTunOutSaEncryptAlgo_Object = MibTableColumn
ceipSecTunOutSaEncryptAlgo = _CeipSecTunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 26),
    _CeipSecTunOutSaEncryptAlgo_Type()
)
ceipSecTunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutSaEncryptAlgo.setStatus("current")
_CeipSecTunOutSaEncryptKeySize_Type = CIPsecEncryptionKeySize
_CeipSecTunOutSaEncryptKeySize_Object = MibTableColumn
ceipSecTunOutSaEncryptKeySize = _CeipSecTunOutSaEncryptKeySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 27),
    _CeipSecTunOutSaEncryptKeySize_Type()
)
ceipSecTunOutSaEncryptKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutSaEncryptKeySize.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunOutSaEncryptKeySize.setUnits("Bits")
_CeipSecTunOutSaAhAuthAlgo_Type = CIPsecAuthAlgorithm
_CeipSecTunOutSaAhAuthAlgo_Object = MibTableColumn
ceipSecTunOutSaAhAuthAlgo = _CeipSecTunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 28),
    _CeipSecTunOutSaAhAuthAlgo_Type()
)
ceipSecTunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutSaAhAuthAlgo.setStatus("current")
_CeipSecTunOutSaEspAuthAlgo_Type = CIPsecAuthAlgorithm
_CeipSecTunOutSaEspAuthAlgo_Object = MibTableColumn
ceipSecTunOutSaEspAuthAlgo = _CeipSecTunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 29),
    _CeipSecTunOutSaEspAuthAlgo_Type()
)
ceipSecTunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutSaEspAuthAlgo.setStatus("current")
_CeipSecTunOutSaCompAlgo_Type = CIPsecCompAlgorithm
_CeipSecTunOutSaCompAlgo_Object = MibTableColumn
ceipSecTunOutSaCompAlgo = _CeipSecTunOutSaCompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 30),
    _CeipSecTunOutSaCompAlgo_Type()
)
ceipSecTunOutSaCompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutSaCompAlgo.setStatus("current")
_CeipSecTunPmtu_Type = CIPsecPmtu
_CeipSecTunPmtu_Object = MibTableColumn
ceipSecTunPmtu = _CeipSecTunPmtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 31),
    _CeipSecTunPmtu_Type()
)
ceipSecTunPmtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunPmtu.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunPmtu.setUnits("Octets")
_CeipSecTunInOctets_Type = Counter64
_CeipSecTunInOctets_Object = MibTableColumn
ceipSecTunInOctets = _CeipSecTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 32),
    _CeipSecTunInOctets_Type()
)
ceipSecTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInOctets.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunInOctets.setUnits("Octets")
_CeipSecTunInDecompOctets_Type = Counter64
_CeipSecTunInDecompOctets_Object = MibTableColumn
ceipSecTunInDecompOctets = _CeipSecTunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 33),
    _CeipSecTunInDecompOctets_Type()
)
ceipSecTunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInDecompOctets.setStatus("current")
_CeipSecTunInPkts_Type = Counter32
_CeipSecTunInPkts_Object = MibTableColumn
ceipSecTunInPkts = _CeipSecTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 34),
    _CeipSecTunInPkts_Type()
)
ceipSecTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunInPkts.setUnits("Packets")
_CeipSecTunInDropPkts_Type = Counter32
_CeipSecTunInDropPkts_Object = MibTableColumn
ceipSecTunInDropPkts = _CeipSecTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 35),
    _CeipSecTunInDropPkts_Type()
)
ceipSecTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunInDropPkts.setUnits("Packets")
_CeipSecTunInReplayDropPkts_Type = Counter32
_CeipSecTunInReplayDropPkts_Object = MibTableColumn
ceipSecTunInReplayDropPkts = _CeipSecTunInReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 36),
    _CeipSecTunInReplayDropPkts_Type()
)
ceipSecTunInReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInReplayDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunInReplayDropPkts.setUnits("Packets")
_CeipSecTunInAuths_Type = Counter32
_CeipSecTunInAuths_Object = MibTableColumn
ceipSecTunInAuths = _CeipSecTunInAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 37),
    _CeipSecTunInAuths_Type()
)
ceipSecTunInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInAuths.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunInAuths.setUnits("Events")
_CeipSecTunInAuthFails_Type = Counter32
_CeipSecTunInAuthFails_Object = MibTableColumn
ceipSecTunInAuthFails = _CeipSecTunInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 38),
    _CeipSecTunInAuthFails_Type()
)
ceipSecTunInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunInAuthFails.setUnits("Failures")
_CeipSecTunInDecrypts_Type = Counter32
_CeipSecTunInDecrypts_Object = MibTableColumn
ceipSecTunInDecrypts = _CeipSecTunInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 39),
    _CeipSecTunInDecrypts_Type()
)
ceipSecTunInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInDecrypts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunInDecrypts.setUnits("Packets")
_CeipSecTunInDecryptFails_Type = Counter32
_CeipSecTunInDecryptFails_Object = MibTableColumn
ceipSecTunInDecryptFails = _CeipSecTunInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 40),
    _CeipSecTunInDecryptFails_Type()
)
ceipSecTunInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunInDecryptFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunInDecryptFails.setUnits("Failures")
_CeipSecTunOutOctets_Type = Counter64
_CeipSecTunOutOctets_Object = MibTableColumn
ceipSecTunOutOctets = _CeipSecTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 41),
    _CeipSecTunOutOctets_Type()
)
ceipSecTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutOctets.setStatus("current")
_CeipSecTunOutUncompOctets_Type = Counter64
_CeipSecTunOutUncompOctets_Object = MibTableColumn
ceipSecTunOutUncompOctets = _CeipSecTunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 42),
    _CeipSecTunOutUncompOctets_Type()
)
ceipSecTunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutUncompOctets.setStatus("current")
_CeipSecTunOutPkts_Type = Counter32
_CeipSecTunOutPkts_Object = MibTableColumn
ceipSecTunOutPkts = _CeipSecTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 43),
    _CeipSecTunOutPkts_Type()
)
ceipSecTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunOutPkts.setUnits("Packets")
_CeipSecTunOutDropPkts_Type = Counter32
_CeipSecTunOutDropPkts_Object = MibTableColumn
ceipSecTunOutDropPkts = _CeipSecTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 44),
    _CeipSecTunOutDropPkts_Type()
)
ceipSecTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunOutDropPkts.setUnits("Packets")
_CeipSecTunOutAuths_Type = Counter32
_CeipSecTunOutAuths_Object = MibTableColumn
ceipSecTunOutAuths = _CeipSecTunOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 45),
    _CeipSecTunOutAuths_Type()
)
ceipSecTunOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutAuths.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunOutAuths.setUnits("Events")
_CeipSecTunOutAuthFails_Type = Counter32
_CeipSecTunOutAuthFails_Object = MibTableColumn
ceipSecTunOutAuthFails = _CeipSecTunOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 46),
    _CeipSecTunOutAuthFails_Type()
)
ceipSecTunOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunOutAuthFails.setUnits("Failures")
_CeipSecTunOutEncrypts_Type = Counter32
_CeipSecTunOutEncrypts_Object = MibTableColumn
ceipSecTunOutEncrypts = _CeipSecTunOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 47),
    _CeipSecTunOutEncrypts_Type()
)
ceipSecTunOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutEncrypts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunOutEncrypts.setUnits("Packets")
_CeipSecTunOutEncryptFails_Type = Counter32
_CeipSecTunOutEncryptFails_Object = MibTableColumn
ceipSecTunOutEncryptFails = _CeipSecTunOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 48),
    _CeipSecTunOutEncryptFails_Type()
)
ceipSecTunOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutEncryptFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunOutEncryptFails.setUnits("Failures")
_CeipSecTunOutCompressedPkts_Type = Counter32
_CeipSecTunOutCompressedPkts_Object = MibTableColumn
ceipSecTunOutCompressedPkts = _CeipSecTunOutCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 49),
    _CeipSecTunOutCompressedPkts_Type()
)
ceipSecTunOutCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutCompressedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunOutCompressedPkts.setUnits("Packets")
_CeipSecTunOutCompSkippedPkts_Type = Counter32
_CeipSecTunOutCompSkippedPkts_Object = MibTableColumn
ceipSecTunOutCompSkippedPkts = _CeipSecTunOutCompSkippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 50),
    _CeipSecTunOutCompSkippedPkts_Type()
)
ceipSecTunOutCompSkippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutCompSkippedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunOutCompSkippedPkts.setUnits("Packets")
_CeipSecTunOutCompFailPkts_Type = Counter32
_CeipSecTunOutCompFailPkts_Object = MibTableColumn
ceipSecTunOutCompFailPkts = _CeipSecTunOutCompFailPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 51),
    _CeipSecTunOutCompFailPkts_Type()
)
ceipSecTunOutCompFailPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutCompFailPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunOutCompFailPkts.setUnits("Packets")
_CeipSecTunOutCompTooSmallPkts_Type = Counter32
_CeipSecTunOutCompTooSmallPkts_Object = MibTableColumn
ceipSecTunOutCompTooSmallPkts = _CeipSecTunOutCompTooSmallPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 52),
    _CeipSecTunOutCompTooSmallPkts_Type()
)
ceipSecTunOutCompTooSmallPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunOutCompTooSmallPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunOutCompTooSmallPkts.setUnits("Packets")
_CeipSecIfIndex_Type = InterfaceIndex
_CeipSecIfIndex_Object = MibTableColumn
ceipSecIfIndex = _CeipSecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 53),
    _CeipSecIfIndex_Type()
)
ceipSecIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecIfIndex.setStatus("current")
_CeipSecTunStatus_Type = CIPsecTunnelStatus
_CeipSecTunStatus_Object = MibTableColumn
ceipSecTunStatus = _CeipSecTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 2, 1, 54),
    _CeipSecTunStatus_Type()
)
ceipSecTunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceipSecTunStatus.setStatus("current")
_CeipSecEndPtTable_Object = MibTable
ceipSecEndPtTable = _CeipSecEndPtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ceipSecEndPtTable.setStatus("current")
_CeipSecEndPtEntry_Object = MibTableRow
ceipSecEndPtEntry = _CeipSecEndPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1)
)
ceipSecEndPtEntry.setIndexNames(
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunIndex"),
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtIndex"),
)
if mibBuilder.loadTexts:
    ceipSecEndPtEntry.setStatus("current")


class _CeipSecEndPtIndex_Type(Unsigned32):
    """Custom type ceipSecEndPtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeipSecEndPtIndex_Type.__name__ = "Unsigned32"
_CeipSecEndPtIndex_Object = MibTableColumn
ceipSecEndPtIndex = _CeipSecEndPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 1),
    _CeipSecEndPtIndex_Type()
)
ceipSecEndPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceipSecEndPtIndex.setStatus("current")
_CeipSecEndPtLocalName_Type = SnmpAdminString
_CeipSecEndPtLocalName_Object = MibTableColumn
ceipSecEndPtLocalName = _CeipSecEndPtLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 2),
    _CeipSecEndPtLocalName_Type()
)
ceipSecEndPtLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtLocalName.setStatus("current")
_CeipSecEndPtLocalType_Type = CIPsecEndPtType
_CeipSecEndPtLocalType_Object = MibTableColumn
ceipSecEndPtLocalType = _CeipSecEndPtLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 3),
    _CeipSecEndPtLocalType_Type()
)
ceipSecEndPtLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtLocalType.setStatus("current")
_CeipSecEndPtLocalAddrType1_Type = InetAddressType
_CeipSecEndPtLocalAddrType1_Object = MibTableColumn
ceipSecEndPtLocalAddrType1 = _CeipSecEndPtLocalAddrType1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 4),
    _CeipSecEndPtLocalAddrType1_Type()
)
ceipSecEndPtLocalAddrType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtLocalAddrType1.setStatus("current")
_CeipSecEndPtLocalAddr1_Type = InetAddress
_CeipSecEndPtLocalAddr1_Object = MibTableColumn
ceipSecEndPtLocalAddr1 = _CeipSecEndPtLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 5),
    _CeipSecEndPtLocalAddr1_Type()
)
ceipSecEndPtLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtLocalAddr1.setStatus("current")
_CeipSecEndPtLocalAddrType2_Type = InetAddressType
_CeipSecEndPtLocalAddrType2_Object = MibTableColumn
ceipSecEndPtLocalAddrType2 = _CeipSecEndPtLocalAddrType2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 6),
    _CeipSecEndPtLocalAddrType2_Type()
)
ceipSecEndPtLocalAddrType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtLocalAddrType2.setStatus("current")
_CeipSecEndPtLocalAddr2_Type = InetAddress
_CeipSecEndPtLocalAddr2_Object = MibTableColumn
ceipSecEndPtLocalAddr2 = _CeipSecEndPtLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 7),
    _CeipSecEndPtLocalAddr2_Type()
)
ceipSecEndPtLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtLocalAddr2.setStatus("current")
_CeipSecEndPtLocalProtocol_Type = CiscoIpProtocol
_CeipSecEndPtLocalProtocol_Object = MibTableColumn
ceipSecEndPtLocalProtocol = _CeipSecEndPtLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 8),
    _CeipSecEndPtLocalProtocol_Type()
)
ceipSecEndPtLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtLocalProtocol.setStatus("current")
_CeipSecEndPtLocalPort_Type = CiscoPort
_CeipSecEndPtLocalPort_Object = MibTableColumn
ceipSecEndPtLocalPort = _CeipSecEndPtLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 9),
    _CeipSecEndPtLocalPort_Type()
)
ceipSecEndPtLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtLocalPort.setStatus("current")
_CeipSecEndPtRemoteName_Type = SnmpAdminString
_CeipSecEndPtRemoteName_Object = MibTableColumn
ceipSecEndPtRemoteName = _CeipSecEndPtRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 10),
    _CeipSecEndPtRemoteName_Type()
)
ceipSecEndPtRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtRemoteName.setStatus("current")
_CeipSecEndPtRemoteType_Type = CIPsecEndPtType
_CeipSecEndPtRemoteType_Object = MibTableColumn
ceipSecEndPtRemoteType = _CeipSecEndPtRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 11),
    _CeipSecEndPtRemoteType_Type()
)
ceipSecEndPtRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtRemoteType.setStatus("current")
_CeipSecEndPtRemoteAddrType1_Type = InetAddressType
_CeipSecEndPtRemoteAddrType1_Object = MibTableColumn
ceipSecEndPtRemoteAddrType1 = _CeipSecEndPtRemoteAddrType1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 12),
    _CeipSecEndPtRemoteAddrType1_Type()
)
ceipSecEndPtRemoteAddrType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtRemoteAddrType1.setStatus("current")
_CeipSecEndPtRemoteAddr1_Type = InetAddress
_CeipSecEndPtRemoteAddr1_Object = MibTableColumn
ceipSecEndPtRemoteAddr1 = _CeipSecEndPtRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 13),
    _CeipSecEndPtRemoteAddr1_Type()
)
ceipSecEndPtRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtRemoteAddr1.setStatus("current")
_CeipSecEndPtRemoteAddrType2_Type = InetAddressType
_CeipSecEndPtRemoteAddrType2_Object = MibTableColumn
ceipSecEndPtRemoteAddrType2 = _CeipSecEndPtRemoteAddrType2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 14),
    _CeipSecEndPtRemoteAddrType2_Type()
)
ceipSecEndPtRemoteAddrType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtRemoteAddrType2.setStatus("current")
_CeipSecEndPtRemoteAddr2_Type = InetAddress
_CeipSecEndPtRemoteAddr2_Object = MibTableColumn
ceipSecEndPtRemoteAddr2 = _CeipSecEndPtRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 15),
    _CeipSecEndPtRemoteAddr2_Type()
)
ceipSecEndPtRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtRemoteAddr2.setStatus("current")
_CeipSecEndPtRemoteProtocol_Type = CiscoIpProtocol
_CeipSecEndPtRemoteProtocol_Object = MibTableColumn
ceipSecEndPtRemoteProtocol = _CeipSecEndPtRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 16),
    _CeipSecEndPtRemoteProtocol_Type()
)
ceipSecEndPtRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtRemoteProtocol.setStatus("current")
_CeipSecEndPtRemotePort_Type = CiscoPort
_CeipSecEndPtRemotePort_Object = MibTableColumn
ceipSecEndPtRemotePort = _CeipSecEndPtRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 3, 1, 17),
    _CeipSecEndPtRemotePort_Type()
)
ceipSecEndPtRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtRemotePort.setStatus("current")
_CeipSecSaTable_Object = MibTable
ceipSecSaTable = _CeipSecSaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ceipSecSaTable.setStatus("current")
_CeipSecSaEntry_Object = MibTableRow
ceipSecSaEntry = _CeipSecSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 4, 1)
)
ceipSecSaEntry.setIndexNames(
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunIndex"),
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecSaProtocol"),
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecSaIndex"),
)
if mibBuilder.loadTexts:
    ceipSecSaEntry.setStatus("current")
_CeipSecSaProtocol_Type = CIPsecProtocol
_CeipSecSaProtocol_Object = MibTableColumn
ceipSecSaProtocol = _CeipSecSaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 4, 1, 1),
    _CeipSecSaProtocol_Type()
)
ceipSecSaProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceipSecSaProtocol.setStatus("current")


class _CeipSecSaIndex_Type(Unsigned32):
    """Custom type ceipSecSaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeipSecSaIndex_Type.__name__ = "Unsigned32"
_CeipSecSaIndex_Object = MibTableColumn
ceipSecSaIndex = _CeipSecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 4, 1, 2),
    _CeipSecSaIndex_Type()
)
ceipSecSaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceipSecSaIndex.setStatus("current")
_CeipSecSaDirection_Type = CIPsecPhase2SaDirection
_CeipSecSaDirection_Object = MibTableColumn
ceipSecSaDirection = _CeipSecSaDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 4, 1, 3),
    _CeipSecSaDirection_Type()
)
ceipSecSaDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecSaDirection.setStatus("current")
_CeipSecSaValue_Type = CIPsecSpi
_CeipSecSaValue_Object = MibTableColumn
ceipSecSaValue = _CeipSecSaValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 4, 1, 4),
    _CeipSecSaValue_Type()
)
ceipSecSaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecSaValue.setStatus("current")


class _CeipSecSaStatus_Type(Integer32):
    """Custom type ceipSecSaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("expiring", 3),
          ("unknown", 1))
    )


_CeipSecSaStatus_Type.__name__ = "Integer32"
_CeipSecSaStatus_Object = MibTableColumn
ceipSecSaStatus = _CeipSecSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 4, 1, 5),
    _CeipSecSaStatus_Type()
)
ceipSecSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecSaStatus.setStatus("current")
_CeipSecTunnelSaTable_Object = MibTable
ceipSecTunnelSaTable = _CeipSecTunnelSaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ceipSecTunnelSaTable.setStatus("current")
_CeipSecTunnelSaEntry_Object = MibTableRow
ceipSecTunnelSaEntry = _CeipSecTunnelSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1)
)
ceipSecTunnelSaEntry.setIndexNames(
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunIndex"),
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaProtocol"),
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaIndex"),
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaDirection"),
)
if mibBuilder.loadTexts:
    ceipSecTunnelSaEntry.setStatus("current")
_CeipSecTunSaProtocol_Type = CIPsecProtocol
_CeipSecTunSaProtocol_Object = MibTableColumn
ceipSecTunSaProtocol = _CeipSecTunSaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 1),
    _CeipSecTunSaProtocol_Type()
)
ceipSecTunSaProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceipSecTunSaProtocol.setStatus("current")


class _CeipSecTunSaIndex_Type(Unsigned32):
    """Custom type ceipSecTunSaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeipSecTunSaIndex_Type.__name__ = "Unsigned32"
_CeipSecTunSaIndex_Object = MibTableColumn
ceipSecTunSaIndex = _CeipSecTunSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 2),
    _CeipSecTunSaIndex_Type()
)
ceipSecTunSaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceipSecTunSaIndex.setStatus("current")
_CeipSecTunSaDirection_Type = CIPsecPhase2SaDirection
_CeipSecTunSaDirection_Object = MibTableColumn
ceipSecTunSaDirection = _CeipSecTunSaDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 3),
    _CeipSecTunSaDirection_Type()
)
ceipSecTunSaDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceipSecTunSaDirection.setStatus("current")
_CeipSecTunSaValue_Type = CIPsecSpi
_CeipSecTunSaValue_Object = MibTableColumn
ceipSecTunSaValue = _CeipSecTunSaValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 4),
    _CeipSecTunSaValue_Type()
)
ceipSecTunSaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaValue.setStatus("current")
_CeipSecTunSaIfIndex_Type = InterfaceIndex
_CeipSecTunSaIfIndex_Object = MibTableColumn
ceipSecTunSaIfIndex = _CeipSecTunSaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 5),
    _CeipSecTunSaIfIndex_Type()
)
ceipSecTunSaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaIfIndex.setStatus("current")
_CeipSecTunSaInOctets_Type = Counter64
_CeipSecTunSaInOctets_Object = MibTableColumn
ceipSecTunSaInOctets = _CeipSecTunSaInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 6),
    _CeipSecTunSaInOctets_Type()
)
ceipSecTunSaInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaInOctets.setStatus("current")
_CeipSecTunSaInDecompOctets_Type = Counter64
_CeipSecTunSaInDecompOctets_Object = MibTableColumn
ceipSecTunSaInDecompOctets = _CeipSecTunSaInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 7),
    _CeipSecTunSaInDecompOctets_Type()
)
ceipSecTunSaInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaInDecompOctets.setStatus("current")
_CeipSecTunSaInPkts_Type = Counter64
_CeipSecTunSaInPkts_Object = MibTableColumn
ceipSecTunSaInPkts = _CeipSecTunSaInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 8),
    _CeipSecTunSaInPkts_Type()
)
ceipSecTunSaInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaInPkts.setStatus("current")
_CeipSecTunSaInDropPkts_Type = Counter64
_CeipSecTunSaInDropPkts_Object = MibTableColumn
ceipSecTunSaInDropPkts = _CeipSecTunSaInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 9),
    _CeipSecTunSaInDropPkts_Type()
)
ceipSecTunSaInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaInDropPkts.setStatus("current")
_CeipSecTunSaInReplayDropPkts_Type = Counter64
_CeipSecTunSaInReplayDropPkts_Object = MibTableColumn
ceipSecTunSaInReplayDropPkts = _CeipSecTunSaInReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 10),
    _CeipSecTunSaInReplayDropPkts_Type()
)
ceipSecTunSaInReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaInReplayDropPkts.setStatus("current")
_CeipSecTunSaInAuths_Type = Counter64
_CeipSecTunSaInAuths_Object = MibTableColumn
ceipSecTunSaInAuths = _CeipSecTunSaInAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 11),
    _CeipSecTunSaInAuths_Type()
)
ceipSecTunSaInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaInAuths.setStatus("current")
_CeipSecTunSaInAuthFails_Type = Counter64
_CeipSecTunSaInAuthFails_Object = MibTableColumn
ceipSecTunSaInAuthFails = _CeipSecTunSaInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 12),
    _CeipSecTunSaInAuthFails_Type()
)
ceipSecTunSaInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaInAuthFails.setStatus("current")
_CeipSecTunSaInDecrypts_Type = Counter64
_CeipSecTunSaInDecrypts_Object = MibTableColumn
ceipSecTunSaInDecrypts = _CeipSecTunSaInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 13),
    _CeipSecTunSaInDecrypts_Type()
)
ceipSecTunSaInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaInDecrypts.setStatus("current")
_CeipSecTunSaInDecryptFails_Type = Counter64
_CeipSecTunSaInDecryptFails_Object = MibTableColumn
ceipSecTunSaInDecryptFails = _CeipSecTunSaInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 14),
    _CeipSecTunSaInDecryptFails_Type()
)
ceipSecTunSaInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaInDecryptFails.setStatus("current")
_CeipSecTunSaOutOctets_Type = Counter64
_CeipSecTunSaOutOctets_Object = MibTableColumn
ceipSecTunSaOutOctets = _CeipSecTunSaOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 15),
    _CeipSecTunSaOutOctets_Type()
)
ceipSecTunSaOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutOctets.setStatus("current")
_CeipSecTunSaOutUncompOctets_Type = Counter64
_CeipSecTunSaOutUncompOctets_Object = MibTableColumn
ceipSecTunSaOutUncompOctets = _CeipSecTunSaOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 16),
    _CeipSecTunSaOutUncompOctets_Type()
)
ceipSecTunSaOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutUncompOctets.setStatus("current")
_CeipSecTunSaOutPkts_Type = Counter64
_CeipSecTunSaOutPkts_Object = MibTableColumn
ceipSecTunSaOutPkts = _CeipSecTunSaOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 17),
    _CeipSecTunSaOutPkts_Type()
)
ceipSecTunSaOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutPkts.setStatus("current")
_CeipSecTunSaOutDropPkts_Type = Counter64
_CeipSecTunSaOutDropPkts_Object = MibTableColumn
ceipSecTunSaOutDropPkts = _CeipSecTunSaOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 18),
    _CeipSecTunSaOutDropPkts_Type()
)
ceipSecTunSaOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutDropPkts.setStatus("current")
_CeipSecTunSaOutAuths_Type = Counter64
_CeipSecTunSaOutAuths_Object = MibTableColumn
ceipSecTunSaOutAuths = _CeipSecTunSaOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 19),
    _CeipSecTunSaOutAuths_Type()
)
ceipSecTunSaOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutAuths.setStatus("current")
_CeipSecTunSaOutAuthFails_Type = Counter64
_CeipSecTunSaOutAuthFails_Object = MibTableColumn
ceipSecTunSaOutAuthFails = _CeipSecTunSaOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 20),
    _CeipSecTunSaOutAuthFails_Type()
)
ceipSecTunSaOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutAuthFails.setStatus("current")
_CeipSecTunSaOutEncrypts_Type = Counter64
_CeipSecTunSaOutEncrypts_Object = MibTableColumn
ceipSecTunSaOutEncrypts = _CeipSecTunSaOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 21),
    _CeipSecTunSaOutEncrypts_Type()
)
ceipSecTunSaOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutEncrypts.setStatus("current")
_CeipSecTunSaOutEncryptFails_Type = Counter64
_CeipSecTunSaOutEncryptFails_Object = MibTableColumn
ceipSecTunSaOutEncryptFails = _CeipSecTunSaOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 22),
    _CeipSecTunSaOutEncryptFails_Type()
)
ceipSecTunSaOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutEncryptFails.setStatus("current")
_CeipSecTunSaOutCompressedPkts_Type = Counter64
_CeipSecTunSaOutCompressedPkts_Object = MibTableColumn
ceipSecTunSaOutCompressedPkts = _CeipSecTunSaOutCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 23),
    _CeipSecTunSaOutCompressedPkts_Type()
)
ceipSecTunSaOutCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutCompressedPkts.setStatus("current")
_CeipSecTunSaOutCompSkippedPkts_Type = Counter64
_CeipSecTunSaOutCompSkippedPkts_Object = MibTableColumn
ceipSecTunSaOutCompSkippedPkts = _CeipSecTunSaOutCompSkippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 24),
    _CeipSecTunSaOutCompSkippedPkts_Type()
)
ceipSecTunSaOutCompSkippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutCompSkippedPkts.setStatus("current")
_CeipSecTunSaOutCompFailPkts_Type = Counter64
_CeipSecTunSaOutCompFailPkts_Object = MibTableColumn
ceipSecTunSaOutCompFailPkts = _CeipSecTunSaOutCompFailPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 25),
    _CeipSecTunSaOutCompFailPkts_Type()
)
ceipSecTunSaOutCompFailPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutCompFailPkts.setStatus("current")
_CeipSecTunSaOutCompTooSmallPkts_Type = Counter64
_CeipSecTunSaOutCompTooSmallPkts_Object = MibTableColumn
ceipSecTunSaOutCompTooSmallPkts = _CeipSecTunSaOutCompTooSmallPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 26),
    _CeipSecTunSaOutCompTooSmallPkts_Type()
)
ceipSecTunSaOutCompTooSmallPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaOutCompTooSmallPkts.setStatus("current")


class _CeipSecTunSaStatus_Type(Integer32):
    """Custom type ceipSecTunSaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("expiring", 3),
          ("unknown", 1))
    )


_CeipSecTunSaStatus_Type.__name__ = "Integer32"
_CeipSecTunSaStatus_Object = MibTableColumn
ceipSecTunSaStatus = _CeipSecTunSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 5, 1, 27),
    _CeipSecTunSaStatus_Type()
)
ceipSecTunSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunSaStatus.setStatus("current")
_CeipSecIfTunnelTable_Object = MibTable
ceipSecIfTunnelTable = _CeipSecIfTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ceipSecIfTunnelTable.setStatus("current")
_CeipSecIfTunnelEntry_Object = MibTableRow
ceipSecIfTunnelEntry = _CeipSecIfTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 6, 1)
)
ceipSecIfTunnelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunIndex"),
)
if mibBuilder.loadTexts:
    ceipSecIfTunnelEntry.setStatus("current")
_CeipSecIfTunnelStatus_Type = CIPsecTunnelStatus
_CeipSecIfTunnelStatus_Object = MibTableColumn
ceipSecIfTunnelStatus = _CeipSecIfTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 1, 6, 1, 1),
    _CeipSecIfTunnelStatus_Type()
)
ceipSecIfTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecIfTunnelStatus.setStatus("current")
_CeipSecHistory_ObjectIdentity = ObjectIdentity
ceipSecHistory = _CeipSecHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2)
)
_CeipSecHistGlobal_ObjectIdentity = ObjectIdentity
ceipSecHistGlobal = _CeipSecHistGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 1)
)
_CeipSecHistGlobalCntl_ObjectIdentity = ObjectIdentity
ceipSecHistGlobalCntl = _CeipSecHistGlobalCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 1, 1)
)
_CeipSecHistTableSize_Type = Unsigned32
_CeipSecHistTableSize_Object = MibScalar
ceipSecHistTableSize = _CeipSecHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 1, 1, 1),
    _CeipSecHistTableSize_Type()
)
ceipSecHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceipSecHistTableSize.setStatus("current")
_CeipSecTunnelHistTable_Object = MibTable
ceipSecTunnelHistTable = _CeipSecTunnelHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ceipSecTunnelHistTable.setStatus("current")
_CeipSecTunnelHistEntry_Object = MibTableRow
ceipSecTunnelHistEntry = _CeipSecTunnelHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1)
)
ceipSecTunnelHistEntry.setIndexNames(
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistIndex"),
)
if mibBuilder.loadTexts:
    ceipSecTunnelHistEntry.setStatus("current")


class _CeipSecTunHistIndex_Type(Unsigned32):
    """Custom type ceipSecTunHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeipSecTunHistIndex_Type.__name__ = "Unsigned32"
_CeipSecTunHistIndex_Object = MibTableColumn
ceipSecTunHistIndex = _CeipSecTunHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 1),
    _CeipSecTunHistIndex_Type()
)
ceipSecTunHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceipSecTunHistIndex.setStatus("current")


class _CeipSecTunHistTermReason_Type(Integer32):
    """Custom type ceipSecTunHistTermReason based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("applicationInitiated", 6),
          ("checkPointReq", 9),
          ("normal", 2),
          ("operRequest", 3),
          ("other", 1),
          ("peerDelRequest", 4),
          ("peerLost", 5),
          ("seqNumRollOver", 8),
          ("xauthFailure", 7))
    )


_CeipSecTunHistTermReason_Type.__name__ = "Integer32"
_CeipSecTunHistTermReason_Object = MibTableColumn
ceipSecTunHistTermReason = _CeipSecTunHistTermReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 2),
    _CeipSecTunHistTermReason_Type()
)
ceipSecTunHistTermReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistTermReason.setStatus("current")
_CeipSecTunHistActiveIndex_Type = CIPsecPhase2TunnelIndex
_CeipSecTunHistActiveIndex_Object = MibTableColumn
ceipSecTunHistActiveIndex = _CeipSecTunHistActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 3),
    _CeipSecTunHistActiveIndex_Type()
)
ceipSecTunHistActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistActiveIndex.setStatus("current")
_CeipSecTunHistLocalAddressType_Type = InetAddressType
_CeipSecTunHistLocalAddressType_Object = MibTableColumn
ceipSecTunHistLocalAddressType = _CeipSecTunHistLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 4),
    _CeipSecTunHistLocalAddressType_Type()
)
ceipSecTunHistLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistLocalAddressType.setStatus("current")
_CeipSecTunHistLocalAddress_Type = InetAddress
_CeipSecTunHistLocalAddress_Object = MibTableColumn
ceipSecTunHistLocalAddress = _CeipSecTunHistLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 5),
    _CeipSecTunHistLocalAddress_Type()
)
ceipSecTunHistLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistLocalAddress.setStatus("current")
_CeipSecTunHistRemoteAddressType_Type = InetAddressType
_CeipSecTunHistRemoteAddressType_Object = MibTableColumn
ceipSecTunHistRemoteAddressType = _CeipSecTunHistRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 6),
    _CeipSecTunHistRemoteAddressType_Type()
)
ceipSecTunHistRemoteAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistRemoteAddressType.setStatus("current")
_CeipSecTunHistRemoteAddress_Type = InetAddress
_CeipSecTunHistRemoteAddress_Object = MibTableColumn
ceipSecTunHistRemoteAddress = _CeipSecTunHistRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 7),
    _CeipSecTunHistRemoteAddress_Type()
)
ceipSecTunHistRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistRemoteAddress.setStatus("current")
_CeipSecTunHistControlProtocol_Type = CIPsecControlProtocol
_CeipSecTunHistControlProtocol_Object = MibTableColumn
ceipSecTunHistControlProtocol = _CeipSecTunHistControlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 8),
    _CeipSecTunHistControlProtocol_Type()
)
ceipSecTunHistControlProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistControlProtocol.setStatus("current")
_CeipSecTunHistControlTunnelIndex_Type = CIPsecPhase1TunnelIndexOrZero
_CeipSecTunHistControlTunnelIndex_Object = MibTableColumn
ceipSecTunHistControlTunnelIndex = _CeipSecTunHistControlTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 9),
    _CeipSecTunHistControlTunnelIndex_Type()
)
ceipSecTunHistControlTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistControlTunnelIndex.setStatus("current")
_CeipSecTunHistEncapMode_Type = CIPsecEncapMode
_CeipSecTunHistEncapMode_Object = MibTableColumn
ceipSecTunHistEncapMode = _CeipSecTunHistEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 10),
    _CeipSecTunHistEncapMode_Type()
)
ceipSecTunHistEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistEncapMode.setStatus("current")
_CeipSecTunHistNATTraversalMode_Type = CIPsecNATTraversalMode
_CeipSecTunHistNATTraversalMode_Object = MibTableColumn
ceipSecTunHistNATTraversalMode = _CeipSecTunHistNATTraversalMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 11),
    _CeipSecTunHistNATTraversalMode_Type()
)
ceipSecTunHistNATTraversalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistNATTraversalMode.setStatus("current")


class _CeipSecTunHistLifeSize_Type(Unsigned32):
    """Custom type ceipSecTunHistLifeSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeipSecTunHistLifeSize_Type.__name__ = "Unsigned32"
_CeipSecTunHistLifeSize_Object = MibTableColumn
ceipSecTunHistLifeSize = _CeipSecTunHistLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 12),
    _CeipSecTunHistLifeSize_Type()
)
ceipSecTunHistLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistLifeSize.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistLifeSize.setUnits("KBytes")


class _CeipSecTunHistLifeTime_Type(Unsigned32):
    """Custom type ceipSecTunHistLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeipSecTunHistLifeTime_Type.__name__ = "Unsigned32"
_CeipSecTunHistLifeTime_Object = MibTableColumn
ceipSecTunHistLifeTime = _CeipSecTunHistLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 13),
    _CeipSecTunHistLifeTime_Type()
)
ceipSecTunHistLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistLifeTime.setUnits("Seconds")
_CeipSecTunHistStartTime_Type = TimeStamp
_CeipSecTunHistStartTime_Object = MibTableColumn
ceipSecTunHistStartTime = _CeipSecTunHistStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 14),
    _CeipSecTunHistStartTime_Type()
)
ceipSecTunHistStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistStartTime.setStatus("current")
_CeipSecTunHistActiveTime_Type = TimeInterval
_CeipSecTunHistActiveTime_Object = MibTableColumn
ceipSecTunHistActiveTime = _CeipSecTunHistActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 15),
    _CeipSecTunHistActiveTime_Type()
)
ceipSecTunHistActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistActiveTime.setStatus("current")
_CeipSecTunHistTotalRefreshes_Type = Counter32
_CeipSecTunHistTotalRefreshes_Object = MibTableColumn
ceipSecTunHistTotalRefreshes = _CeipSecTunHistTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 16),
    _CeipSecTunHistTotalRefreshes_Type()
)
ceipSecTunHistTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistTotalRefreshes.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistTotalRefreshes.setUnits("QM Exchanges")
_CeipSecTunHistTotalSas_Type = Counter32
_CeipSecTunHistTotalSas_Object = MibTableColumn
ceipSecTunHistTotalSas = _CeipSecTunHistTotalSas_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 17),
    _CeipSecTunHistTotalSas_Type()
)
ceipSecTunHistTotalSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistTotalSas.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistTotalSas.setUnits("SAs")
_CeipSecTunHistInSaDHGrp_Type = CIPsecDiffHellmanGrp
_CeipSecTunHistInSaDHGrp_Object = MibTableColumn
ceipSecTunHistInSaDHGrp = _CeipSecTunHistInSaDHGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 18),
    _CeipSecTunHistInSaDHGrp_Type()
)
ceipSecTunHistInSaDHGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInSaDHGrp.setStatus("current")
_CeipSecTunHistInSaEncryptAlgo_Type = CIPsecEncryptAlgorithm
_CeipSecTunHistInSaEncryptAlgo_Object = MibTableColumn
ceipSecTunHistInSaEncryptAlgo = _CeipSecTunHistInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 19),
    _CeipSecTunHistInSaEncryptAlgo_Type()
)
ceipSecTunHistInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInSaEncryptAlgo.setStatus("current")
_CeipSecTunHistInSaEncryptKeySize_Type = CIPsecEncryptionKeySize
_CeipSecTunHistInSaEncryptKeySize_Object = MibTableColumn
ceipSecTunHistInSaEncryptKeySize = _CeipSecTunHistInSaEncryptKeySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 20),
    _CeipSecTunHistInSaEncryptKeySize_Type()
)
ceipSecTunHistInSaEncryptKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInSaEncryptKeySize.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistInSaEncryptKeySize.setUnits("Bits")
_CeipSecTunHistInSaAhAuthAlgo_Type = CIPsecAuthAlgorithm
_CeipSecTunHistInSaAhAuthAlgo_Object = MibTableColumn
ceipSecTunHistInSaAhAuthAlgo = _CeipSecTunHistInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 21),
    _CeipSecTunHistInSaAhAuthAlgo_Type()
)
ceipSecTunHistInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInSaAhAuthAlgo.setStatus("current")
_CeipSecTunHistInSaEspAuthAlgo_Type = CIPsecAuthAlgorithm
_CeipSecTunHistInSaEspAuthAlgo_Object = MibTableColumn
ceipSecTunHistInSaEspAuthAlgo = _CeipSecTunHistInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 22),
    _CeipSecTunHistInSaEspAuthAlgo_Type()
)
ceipSecTunHistInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInSaEspAuthAlgo.setStatus("current")
_CeipSecTunHistInSaDecompAlgo_Type = CIPsecCompAlgorithm
_CeipSecTunHistInSaDecompAlgo_Object = MibTableColumn
ceipSecTunHistInSaDecompAlgo = _CeipSecTunHistInSaDecompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 23),
    _CeipSecTunHistInSaDecompAlgo_Type()
)
ceipSecTunHistInSaDecompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInSaDecompAlgo.setStatus("current")
_CeipSecTunHistOutSaDHGrp_Type = CIPsecDiffHellmanGrp
_CeipSecTunHistOutSaDHGrp_Object = MibTableColumn
ceipSecTunHistOutSaDHGrp = _CeipSecTunHistOutSaDHGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 24),
    _CeipSecTunHistOutSaDHGrp_Type()
)
ceipSecTunHistOutSaDHGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutSaDHGrp.setStatus("current")
_CeipSecTunHistOutSaEncryptAlgo_Type = CIPsecEncryptAlgorithm
_CeipSecTunHistOutSaEncryptAlgo_Object = MibTableColumn
ceipSecTunHistOutSaEncryptAlgo = _CeipSecTunHistOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 25),
    _CeipSecTunHistOutSaEncryptAlgo_Type()
)
ceipSecTunHistOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutSaEncryptAlgo.setStatus("current")
_CeipSecTunHistOutSaEncryptKeySz_Type = CIPsecEncryptionKeySize
_CeipSecTunHistOutSaEncryptKeySz_Object = MibTableColumn
ceipSecTunHistOutSaEncryptKeySz = _CeipSecTunHistOutSaEncryptKeySz_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 26),
    _CeipSecTunHistOutSaEncryptKeySz_Type()
)
ceipSecTunHistOutSaEncryptKeySz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutSaEncryptKeySz.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutSaEncryptKeySz.setUnits("Bits")
_CeipSecTunHistOutSaAhAuthAlgo_Type = CIPsecAuthAlgorithm
_CeipSecTunHistOutSaAhAuthAlgo_Object = MibTableColumn
ceipSecTunHistOutSaAhAuthAlgo = _CeipSecTunHistOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 27),
    _CeipSecTunHistOutSaAhAuthAlgo_Type()
)
ceipSecTunHistOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutSaAhAuthAlgo.setStatus("current")
_CeipSecTunHistOutSaEspAuthAlgo_Type = CIPsecAuthAlgorithm
_CeipSecTunHistOutSaEspAuthAlgo_Object = MibTableColumn
ceipSecTunHistOutSaEspAuthAlgo = _CeipSecTunHistOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 28),
    _CeipSecTunHistOutSaEspAuthAlgo_Type()
)
ceipSecTunHistOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutSaEspAuthAlgo.setStatus("current")
_CeipSecTunHistOutSaCompAlgo_Type = CIPsecCompAlgorithm
_CeipSecTunHistOutSaCompAlgo_Object = MibTableColumn
ceipSecTunHistOutSaCompAlgo = _CeipSecTunHistOutSaCompAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 29),
    _CeipSecTunHistOutSaCompAlgo_Type()
)
ceipSecTunHistOutSaCompAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutSaCompAlgo.setStatus("current")
_CeipSecTunHistPmtu_Type = CIPsecPmtu
_CeipSecTunHistPmtu_Object = MibTableColumn
ceipSecTunHistPmtu = _CeipSecTunHistPmtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 30),
    _CeipSecTunHistPmtu_Type()
)
ceipSecTunHistPmtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistPmtu.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistPmtu.setUnits("Octets")
_CeipSecTunHistInOctets_Type = Counter64
_CeipSecTunHistInOctets_Object = MibTableColumn
ceipSecTunHistInOctets = _CeipSecTunHistInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 31),
    _CeipSecTunHistInOctets_Type()
)
ceipSecTunHistInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInOctets.setStatus("current")
_CeipSecTunHistInDecompOctets_Type = Counter64
_CeipSecTunHistInDecompOctets_Object = MibTableColumn
ceipSecTunHistInDecompOctets = _CeipSecTunHistInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 32),
    _CeipSecTunHistInDecompOctets_Type()
)
ceipSecTunHistInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInDecompOctets.setStatus("current")
_CeipSecTunHistInPkts_Type = Counter32
_CeipSecTunHistInPkts_Object = MibTableColumn
ceipSecTunHistInPkts = _CeipSecTunHistInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 33),
    _CeipSecTunHistInPkts_Type()
)
ceipSecTunHistInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistInPkts.setUnits("Packets")
_CeipSecTunHistInDropPkts_Type = Counter32
_CeipSecTunHistInDropPkts_Object = MibTableColumn
ceipSecTunHistInDropPkts = _CeipSecTunHistInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 34),
    _CeipSecTunHistInDropPkts_Type()
)
ceipSecTunHistInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistInDropPkts.setUnits("Packets")
_CeipSecTunHistInReplayDropPkts_Type = Counter32
_CeipSecTunHistInReplayDropPkts_Object = MibTableColumn
ceipSecTunHistInReplayDropPkts = _CeipSecTunHistInReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 35),
    _CeipSecTunHistInReplayDropPkts_Type()
)
ceipSecTunHistInReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInReplayDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistInReplayDropPkts.setUnits("Packets")
_CeipSecTunHistInAuths_Type = Counter32
_CeipSecTunHistInAuths_Object = MibTableColumn
ceipSecTunHistInAuths = _CeipSecTunHistInAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 36),
    _CeipSecTunHistInAuths_Type()
)
ceipSecTunHistInAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInAuths.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistInAuths.setUnits("Events")
_CeipSecTunHistInAuthFails_Type = Counter32
_CeipSecTunHistInAuthFails_Object = MibTableColumn
ceipSecTunHistInAuthFails = _CeipSecTunHistInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 37),
    _CeipSecTunHistInAuthFails_Type()
)
ceipSecTunHistInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistInAuthFails.setUnits("Failures")
_CeipSecTunHistInDecrypts_Type = Counter32
_CeipSecTunHistInDecrypts_Object = MibTableColumn
ceipSecTunHistInDecrypts = _CeipSecTunHistInDecrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 38),
    _CeipSecTunHistInDecrypts_Type()
)
ceipSecTunHistInDecrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInDecrypts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistInDecrypts.setUnits("Packets")
_CeipSecTunHistInDecryptFails_Type = Counter32
_CeipSecTunHistInDecryptFails_Object = MibTableColumn
ceipSecTunHistInDecryptFails = _CeipSecTunHistInDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 39),
    _CeipSecTunHistInDecryptFails_Type()
)
ceipSecTunHistInDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistInDecryptFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistInDecryptFails.setUnits("Failures")
_CeipSecTunHistOutOctets_Type = Counter64
_CeipSecTunHistOutOctets_Object = MibTableColumn
ceipSecTunHistOutOctets = _CeipSecTunHistOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 40),
    _CeipSecTunHistOutOctets_Type()
)
ceipSecTunHistOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutOctets.setStatus("current")
_CeipSecTunHistOutUncompOctets_Type = Counter64
_CeipSecTunHistOutUncompOctets_Object = MibTableColumn
ceipSecTunHistOutUncompOctets = _CeipSecTunHistOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 41),
    _CeipSecTunHistOutUncompOctets_Type()
)
ceipSecTunHistOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutUncompOctets.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutUncompOctets.setUnits("Octets")
_CeipSecTunHistOutPkts_Type = Counter32
_CeipSecTunHistOutPkts_Object = MibTableColumn
ceipSecTunHistOutPkts = _CeipSecTunHistOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 42),
    _CeipSecTunHistOutPkts_Type()
)
ceipSecTunHistOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutPkts.setUnits("Packets")
_CeipSecTunHistOutDropPkts_Type = Counter32
_CeipSecTunHistOutDropPkts_Object = MibTableColumn
ceipSecTunHistOutDropPkts = _CeipSecTunHistOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 43),
    _CeipSecTunHistOutDropPkts_Type()
)
ceipSecTunHistOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutDropPkts.setUnits("Packets")
_CeipSecTunHistOutAuths_Type = Counter32
_CeipSecTunHistOutAuths_Object = MibTableColumn
ceipSecTunHistOutAuths = _CeipSecTunHistOutAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 44),
    _CeipSecTunHistOutAuths_Type()
)
ceipSecTunHistOutAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutAuths.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutAuths.setUnits("Events")
_CeipSecTunHistOutAuthFails_Type = Counter32
_CeipSecTunHistOutAuthFails_Object = MibTableColumn
ceipSecTunHistOutAuthFails = _CeipSecTunHistOutAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 45),
    _CeipSecTunHistOutAuthFails_Type()
)
ceipSecTunHistOutAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutAuthFails.setUnits("Failures")
_CeipSecTunHistOutEncrypts_Type = Counter32
_CeipSecTunHistOutEncrypts_Object = MibTableColumn
ceipSecTunHistOutEncrypts = _CeipSecTunHistOutEncrypts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 46),
    _CeipSecTunHistOutEncrypts_Type()
)
ceipSecTunHistOutEncrypts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutEncrypts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutEncrypts.setUnits("Packets")
_CeipSecTunHistOutEncryptFails_Type = Counter32
_CeipSecTunHistOutEncryptFails_Object = MibTableColumn
ceipSecTunHistOutEncryptFails = _CeipSecTunHistOutEncryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 47),
    _CeipSecTunHistOutEncryptFails_Type()
)
ceipSecTunHistOutEncryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutEncryptFails.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutEncryptFails.setUnits("Failures")
_CeipSecTunHistOutCompressedPkts_Type = Counter32
_CeipSecTunHistOutCompressedPkts_Object = MibTableColumn
ceipSecTunHistOutCompressedPkts = _CeipSecTunHistOutCompressedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 48),
    _CeipSecTunHistOutCompressedPkts_Type()
)
ceipSecTunHistOutCompressedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutCompressedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutCompressedPkts.setUnits("Packets")
_CeipSecTunHistOutCompSkippedPkts_Type = Counter32
_CeipSecTunHistOutCompSkippedPkts_Object = MibTableColumn
ceipSecTunHistOutCompSkippedPkts = _CeipSecTunHistOutCompSkippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 49),
    _CeipSecTunHistOutCompSkippedPkts_Type()
)
ceipSecTunHistOutCompSkippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutCompSkippedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutCompSkippedPkts.setUnits("Packets")
_CeipSecTunHistOutCompFailPkts_Type = Counter32
_CeipSecTunHistOutCompFailPkts_Object = MibTableColumn
ceipSecTunHistOutCompFailPkts = _CeipSecTunHistOutCompFailPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 50),
    _CeipSecTunHistOutCompFailPkts_Type()
)
ceipSecTunHistOutCompFailPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutCompFailPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutCompFailPkts.setUnits("Packets")
_CeipSecTunHistOutCompSmallPkts_Type = Counter32
_CeipSecTunHistOutCompSmallPkts_Object = MibTableColumn
ceipSecTunHistOutCompSmallPkts = _CeipSecTunHistOutCompSmallPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 2, 1, 51),
    _CeipSecTunHistOutCompSmallPkts_Type()
)
ceipSecTunHistOutCompSmallPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecTunHistOutCompSmallPkts.setStatus("current")
if mibBuilder.loadTexts:
    ceipSecTunHistOutCompSmallPkts.setUnits("Packets")
_CeipSecEndPtHistTable_Object = MibTable
ceipSecEndPtHistTable = _CeipSecEndPtHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ceipSecEndPtHistTable.setStatus("current")
_CeipSecEndPtHistEntry_Object = MibTableRow
ceipSecEndPtHistEntry = _CeipSecEndPtHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1)
)
ceipSecEndPtHistEntry.setIndexNames(
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistIndex"),
)
if mibBuilder.loadTexts:
    ceipSecEndPtHistEntry.setStatus("current")


class _CeipSecEndPtHistIndex_Type(Unsigned32):
    """Custom type ceipSecEndPtHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeipSecEndPtHistIndex_Type.__name__ = "Unsigned32"
_CeipSecEndPtHistIndex_Object = MibTableColumn
ceipSecEndPtHistIndex = _CeipSecEndPtHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 1),
    _CeipSecEndPtHistIndex_Type()
)
ceipSecEndPtHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceipSecEndPtHistIndex.setStatus("current")


class _CeipSecEndPtHistTunIndex_Type(Unsigned32):
    """Custom type ceipSecEndPtHistTunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeipSecEndPtHistTunIndex_Type.__name__ = "Unsigned32"
_CeipSecEndPtHistTunIndex_Object = MibTableColumn
ceipSecEndPtHistTunIndex = _CeipSecEndPtHistTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 2),
    _CeipSecEndPtHistTunIndex_Type()
)
ceipSecEndPtHistTunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistTunIndex.setStatus("current")


class _CeipSecEndPtHistActiveIndex_Type(Unsigned32):
    """Custom type ceipSecEndPtHistActiveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeipSecEndPtHistActiveIndex_Type.__name__ = "Unsigned32"
_CeipSecEndPtHistActiveIndex_Object = MibTableColumn
ceipSecEndPtHistActiveIndex = _CeipSecEndPtHistActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 3),
    _CeipSecEndPtHistActiveIndex_Type()
)
ceipSecEndPtHistActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistActiveIndex.setStatus("current")
_CeipSecEndPtHistLocalName_Type = SnmpAdminString
_CeipSecEndPtHistLocalName_Object = MibTableColumn
ceipSecEndPtHistLocalName = _CeipSecEndPtHistLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 4),
    _CeipSecEndPtHistLocalName_Type()
)
ceipSecEndPtHistLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistLocalName.setStatus("current")
_CeipSecEndPtHistLocalType_Type = CIPsecEndPtType
_CeipSecEndPtHistLocalType_Object = MibTableColumn
ceipSecEndPtHistLocalType = _CeipSecEndPtHistLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 5),
    _CeipSecEndPtHistLocalType_Type()
)
ceipSecEndPtHistLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistLocalType.setStatus("current")
_CeipSecEndPtHistLocalAddrType1_Type = InetAddressType
_CeipSecEndPtHistLocalAddrType1_Object = MibTableColumn
ceipSecEndPtHistLocalAddrType1 = _CeipSecEndPtHistLocalAddrType1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 6),
    _CeipSecEndPtHistLocalAddrType1_Type()
)
ceipSecEndPtHistLocalAddrType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistLocalAddrType1.setStatus("current")
_CeipSecEndPtHistLocalAddr1_Type = InetAddress
_CeipSecEndPtHistLocalAddr1_Object = MibTableColumn
ceipSecEndPtHistLocalAddr1 = _CeipSecEndPtHistLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 7),
    _CeipSecEndPtHistLocalAddr1_Type()
)
ceipSecEndPtHistLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistLocalAddr1.setStatus("current")
_CeipSecEndPtHistLocalAddrType2_Type = InetAddressType
_CeipSecEndPtHistLocalAddrType2_Object = MibTableColumn
ceipSecEndPtHistLocalAddrType2 = _CeipSecEndPtHistLocalAddrType2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 8),
    _CeipSecEndPtHistLocalAddrType2_Type()
)
ceipSecEndPtHistLocalAddrType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistLocalAddrType2.setStatus("current")
_CeipSecEndPtHistLocalAddr2_Type = InetAddress
_CeipSecEndPtHistLocalAddr2_Object = MibTableColumn
ceipSecEndPtHistLocalAddr2 = _CeipSecEndPtHistLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 9),
    _CeipSecEndPtHistLocalAddr2_Type()
)
ceipSecEndPtHistLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistLocalAddr2.setStatus("current")
_CeipSecEndPtHistLocalProtocol_Type = CiscoIpProtocol
_CeipSecEndPtHistLocalProtocol_Object = MibTableColumn
ceipSecEndPtHistLocalProtocol = _CeipSecEndPtHistLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 10),
    _CeipSecEndPtHistLocalProtocol_Type()
)
ceipSecEndPtHistLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistLocalProtocol.setStatus("current")
_CeipSecEndPtHistLocalPort_Type = CiscoPort
_CeipSecEndPtHistLocalPort_Object = MibTableColumn
ceipSecEndPtHistLocalPort = _CeipSecEndPtHistLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 11),
    _CeipSecEndPtHistLocalPort_Type()
)
ceipSecEndPtHistLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistLocalPort.setStatus("current")
_CeipSecEndPtHistRemoteName_Type = SnmpAdminString
_CeipSecEndPtHistRemoteName_Object = MibTableColumn
ceipSecEndPtHistRemoteName = _CeipSecEndPtHistRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 12),
    _CeipSecEndPtHistRemoteName_Type()
)
ceipSecEndPtHistRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistRemoteName.setStatus("current")
_CeipSecEndPtHistRemoteType_Type = CIPsecEndPtType
_CeipSecEndPtHistRemoteType_Object = MibTableColumn
ceipSecEndPtHistRemoteType = _CeipSecEndPtHistRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 13),
    _CeipSecEndPtHistRemoteType_Type()
)
ceipSecEndPtHistRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistRemoteType.setStatus("current")
_CeipSecEndPtHistRemoteAddrType1_Type = InetAddressType
_CeipSecEndPtHistRemoteAddrType1_Object = MibTableColumn
ceipSecEndPtHistRemoteAddrType1 = _CeipSecEndPtHistRemoteAddrType1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 14),
    _CeipSecEndPtHistRemoteAddrType1_Type()
)
ceipSecEndPtHistRemoteAddrType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistRemoteAddrType1.setStatus("current")
_CeipSecEndPtHistRemoteAddr1_Type = InetAddress
_CeipSecEndPtHistRemoteAddr1_Object = MibTableColumn
ceipSecEndPtHistRemoteAddr1 = _CeipSecEndPtHistRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 15),
    _CeipSecEndPtHistRemoteAddr1_Type()
)
ceipSecEndPtHistRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistRemoteAddr1.setStatus("current")
_CeipSecEndPtHistRemoteAddrType2_Type = InetAddressType
_CeipSecEndPtHistRemoteAddrType2_Object = MibTableColumn
ceipSecEndPtHistRemoteAddrType2 = _CeipSecEndPtHistRemoteAddrType2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 16),
    _CeipSecEndPtHistRemoteAddrType2_Type()
)
ceipSecEndPtHistRemoteAddrType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistRemoteAddrType2.setStatus("current")
_CeipSecEndPtHistRemoteAddr2_Type = InetAddress
_CeipSecEndPtHistRemoteAddr2_Object = MibTableColumn
ceipSecEndPtHistRemoteAddr2 = _CeipSecEndPtHistRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 17),
    _CeipSecEndPtHistRemoteAddr2_Type()
)
ceipSecEndPtHistRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistRemoteAddr2.setStatus("current")
_CeipSecEndPtHistRemoteProtocol_Type = CiscoIpProtocol
_CeipSecEndPtHistRemoteProtocol_Object = MibTableColumn
ceipSecEndPtHistRemoteProtocol = _CeipSecEndPtHistRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 18),
    _CeipSecEndPtHistRemoteProtocol_Type()
)
ceipSecEndPtHistRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistRemoteProtocol.setStatus("current")
_CeipSecEndPtHistRemotePort_Type = CiscoPort
_CeipSecEndPtHistRemotePort_Object = MibTableColumn
ceipSecEndPtHistRemotePort = _CeipSecEndPtHistRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 2, 3, 1, 19),
    _CeipSecEndPtHistRemotePort_Type()
)
ceipSecEndPtHistRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecEndPtHistRemotePort.setStatus("current")
_CeipSecFailures_ObjectIdentity = ObjectIdentity
ceipSecFailures = _CeipSecFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3)
)
_CeipSecFailGlobal_ObjectIdentity = ObjectIdentity
ceipSecFailGlobal = _CeipSecFailGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 1)
)
_CeipSecFailGlobalCntl_ObjectIdentity = ObjectIdentity
ceipSecFailGlobalCntl = _CeipSecFailGlobalCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 1, 1)
)
_CeipSecFailTableSize_Type = Unsigned32
_CeipSecFailTableSize_Object = MibScalar
ceipSecFailTableSize = _CeipSecFailTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 1, 1, 1),
    _CeipSecFailTableSize_Type()
)
ceipSecFailTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceipSecFailTableSize.setStatus("current")
_CeipSecFailTable_Object = MibTable
ceipSecFailTable = _CeipSecFailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ceipSecFailTable.setStatus("current")
_CeipSecFailEntry_Object = MibTableRow
ceipSecFailEntry = _CeipSecFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 2, 1)
)
ceipSecFailEntry.setIndexNames(
    (0, "CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailIndex"),
)
if mibBuilder.loadTexts:
    ceipSecFailEntry.setStatus("current")


class _CeipSecFailIndex_Type(Unsigned32):
    """Custom type ceipSecFailIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CeipSecFailIndex_Type.__name__ = "Unsigned32"
_CeipSecFailIndex_Object = MibTableColumn
ceipSecFailIndex = _CeipSecFailIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 2, 1, 1),
    _CeipSecFailIndex_Type()
)
ceipSecFailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceipSecFailIndex.setStatus("current")


class _CeipSecFailReason_Type(Integer32):
    """Custom type ceipSecFailReason based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("compression", 11),
          ("decryptFailure", 7),
          ("encryptFailure", 8),
          ("inAuthFailure", 9),
          ("internalError", 2),
          ("nonExistentSa", 6),
          ("operRequest", 16),
          ("other", 1),
          ("outAuthFailure", 10),
          ("peerDelRequest", 13),
          ("peerEncodingError", 3),
          ("peerLost", 14),
          ("performanceUtilization", 17),
          ("proposalFailure", 4),
          ("protocolUseFail", 5),
          ("seqNumRollOver", 15),
          ("sysCapExceeded", 12))
    )


_CeipSecFailReason_Type.__name__ = "Integer32"
_CeipSecFailReason_Object = MibTableColumn
ceipSecFailReason = _CeipSecFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 2, 1, 2),
    _CeipSecFailReason_Type()
)
ceipSecFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecFailReason.setStatus("current")
_CeipSecFailTime_Type = TimeStamp
_CeipSecFailTime_Object = MibTableColumn
ceipSecFailTime = _CeipSecFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 2, 1, 3),
    _CeipSecFailTime_Type()
)
ceipSecFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecFailTime.setStatus("current")
_CeipSecFailTunnelIndex_Type = CIPsecPhase2TunnelIndex
_CeipSecFailTunnelIndex_Object = MibTableColumn
ceipSecFailTunnelIndex = _CeipSecFailTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 2, 1, 4),
    _CeipSecFailTunnelIndex_Type()
)
ceipSecFailTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecFailTunnelIndex.setStatus("current")
_CeipSecFailSaSpi_Type = CIPsecSpi
_CeipSecFailSaSpi_Object = MibTableColumn
ceipSecFailSaSpi = _CeipSecFailSaSpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 2, 1, 5),
    _CeipSecFailSaSpi_Type()
)
ceipSecFailSaSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecFailSaSpi.setStatus("current")
_CeipSecFailPktSrcAddressType_Type = InetAddressType
_CeipSecFailPktSrcAddressType_Object = MibTableColumn
ceipSecFailPktSrcAddressType = _CeipSecFailPktSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 2, 1, 6),
    _CeipSecFailPktSrcAddressType_Type()
)
ceipSecFailPktSrcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecFailPktSrcAddressType.setStatus("current")
_CeipSecFailPktSrcAddress_Type = InetAddress
_CeipSecFailPktSrcAddress_Object = MibTableColumn
ceipSecFailPktSrcAddress = _CeipSecFailPktSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 2, 1, 7),
    _CeipSecFailPktSrcAddress_Type()
)
ceipSecFailPktSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecFailPktSrcAddress.setStatus("current")
_CeipSecFailPktDstAddressType_Type = InetAddressType
_CeipSecFailPktDstAddressType_Object = MibTableColumn
ceipSecFailPktDstAddressType = _CeipSecFailPktDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 2, 1, 8),
    _CeipSecFailPktDstAddressType_Type()
)
ceipSecFailPktDstAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecFailPktDstAddressType.setStatus("current")
_CeipSecFailPktDstAddress_Type = InetAddress
_CeipSecFailPktDstAddress_Object = MibTableColumn
ceipSecFailPktDstAddress = _CeipSecFailPktDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 3, 2, 1, 9),
    _CeipSecFailPktDstAddress_Type()
)
ceipSecFailPktDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecFailPktDstAddress.setStatus("current")
_CeipSecNotificationCntl_ObjectIdentity = ObjectIdentity
ceipSecNotificationCntl = _CeipSecNotificationCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 5)
)


class _CeipSecNotiCntlIpSecAllNotifs_Type(TruthValue):
    """Custom type ceipSecNotiCntlIpSecAllNotifs based on TruthValue"""


_CeipSecNotiCntlIpSecAllNotifs_Object = MibScalar
ceipSecNotiCntlIpSecAllNotifs = _CeipSecNotiCntlIpSecAllNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 5, 1),
    _CeipSecNotiCntlIpSecAllNotifs_Type()
)
ceipSecNotiCntlIpSecAllNotifs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceipSecNotiCntlIpSecAllNotifs.setStatus("current")


class _CeipSecNotifCntlIpSecTunnelStart_Type(TruthValue):
    """Custom type ceipSecNotifCntlIpSecTunnelStart based on TruthValue"""


_CeipSecNotifCntlIpSecTunnelStart_Object = MibScalar
ceipSecNotifCntlIpSecTunnelStart = _CeipSecNotifCntlIpSecTunnelStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 5, 2),
    _CeipSecNotifCntlIpSecTunnelStart_Type()
)
ceipSecNotifCntlIpSecTunnelStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceipSecNotifCntlIpSecTunnelStart.setStatus("current")


class _CeipSecNotifCntlIpSecTunnelStop_Type(TruthValue):
    """Custom type ceipSecNotifCntlIpSecTunnelStop based on TruthValue"""


_CeipSecNotifCntlIpSecTunnelStop_Object = MibScalar
ceipSecNotifCntlIpSecTunnelStop = _CeipSecNotifCntlIpSecTunnelStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 5, 3),
    _CeipSecNotifCntlIpSecTunnelStop_Type()
)
ceipSecNotifCntlIpSecTunnelStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceipSecNotifCntlIpSecTunnelStop.setStatus("current")


class _CeipSecNotifCntlIpSecSysFailure_Type(TruthValue):
    """Custom type ceipSecNotifCntlIpSecSysFailure based on TruthValue"""


_CeipSecNotifCntlIpSecSysFailure_Object = MibScalar
ceipSecNotifCntlIpSecSysFailure = _CeipSecNotifCntlIpSecSysFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 5, 4),
    _CeipSecNotifCntlIpSecSysFailure_Type()
)
ceipSecNotifCntlIpSecSysFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceipSecNotifCntlIpSecSysFailure.setStatus("current")


class _CeipSecNotifCntlIpSecSetUpFail_Type(TruthValue):
    """Custom type ceipSecNotifCntlIpSecSetUpFail based on TruthValue"""


_CeipSecNotifCntlIpSecSetUpFail_Object = MibScalar
ceipSecNotifCntlIpSecSetUpFail = _CeipSecNotifCntlIpSecSetUpFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 5, 5),
    _CeipSecNotifCntlIpSecSetUpFail_Type()
)
ceipSecNotifCntlIpSecSetUpFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceipSecNotifCntlIpSecSetUpFail.setStatus("current")


class _CeipSecNotifCntlIpSecBadSa_Type(TruthValue):
    """Custom type ceipSecNotifCntlIpSecBadSa based on TruthValue"""


_CeipSecNotifCntlIpSecBadSa_Object = MibScalar
ceipSecNotifCntlIpSecBadSa = _CeipSecNotifCntlIpSecBadSa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 5, 6),
    _CeipSecNotifCntlIpSecBadSa_Type()
)
ceipSecNotifCntlIpSecBadSa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceipSecNotifCntlIpSecBadSa.setStatus("current")


class _CeipSecNotifCntlCertExpiry_Type(TruthValue):
    """Custom type ceipSecNotifCntlCertExpiry based on TruthValue"""


_CeipSecNotifCntlCertExpiry_Object = MibScalar
ceipSecNotifCntlCertExpiry = _CeipSecNotifCntlCertExpiry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 5, 7),
    _CeipSecNotifCntlCertExpiry_Type()
)
ceipSecNotifCntlCertExpiry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceipSecNotifCntlCertExpiry.setStatus("current")


class _CeipSecNotifCntlCertRenewal_Type(TruthValue):
    """Custom type ceipSecNotifCntlCertRenewal based on TruthValue"""


_CeipSecNotifCntlCertRenewal_Object = MibScalar
ceipSecNotifCntlCertRenewal = _CeipSecNotifCntlCertRenewal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 5, 8),
    _CeipSecNotifCntlCertRenewal_Type()
)
ceipSecNotifCntlCertRenewal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceipSecNotifCntlCertRenewal.setStatus("current")
_CeipSecCertNotification_ObjectIdentity = ObjectIdentity
ceipSecCertNotification = _CeipSecCertNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 6)
)
_CeipSecCertSubjectName_Type = SnmpAdminString
_CeipSecCertSubjectName_Object = MibScalar
ceipSecCertSubjectName = _CeipSecCertSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 6, 1),
    _CeipSecCertSubjectName_Type()
)
ceipSecCertSubjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecCertSubjectName.setStatus("current")
_CeipSecCertSerialNumber_Type = SnmpAdminString
_CeipSecCertSerialNumber_Object = MibScalar
ceipSecCertSerialNumber = _CeipSecCertSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 6, 2),
    _CeipSecCertSerialNumber_Type()
)
ceipSecCertSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecCertSerialNumber.setStatus("current")
_CeipSecCertIssuerName_Type = SnmpAdminString
_CeipSecCertIssuerName_Object = MibScalar
ceipSecCertIssuerName = _CeipSecCertIssuerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 6, 3),
    _CeipSecCertIssuerName_Type()
)
ceipSecCertIssuerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecCertIssuerName.setStatus("current")
_CeipSecCertExpiryTime_Type = SnmpAdminString
_CeipSecCertExpiryTime_Object = MibScalar
ceipSecCertExpiryTime = _CeipSecCertExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 6, 4),
    _CeipSecCertExpiryTime_Type()
)
ceipSecCertExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecCertExpiryTime.setStatus("current")


class _CeipSecCertRenewalStatus_Type(Integer32):
    """Custom type ceipSecCertRenewalStatus based on Integer32"""
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
        *(("renewalFailedExpired", 6),
          ("renewalFailedUpdate", 5),
          ("renewalNotNeeded", 1),
          ("renewalRequestNeeded", 2),
          ("renewalRequested", 3),
          ("renewalSuccess", 4))
    )


_CeipSecCertRenewalStatus_Type.__name__ = "Integer32"
_CeipSecCertRenewalStatus_Object = MibScalar
ceipSecCertRenewalStatus = _CeipSecCertRenewalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 6, 5),
    _CeipSecCertRenewalStatus_Type()
)
ceipSecCertRenewalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecCertRenewalStatus.setStatus("current")


class _CeipSecCertExpiryStatus_Type(Integer32):
    """Custom type ceipSecCertExpiryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("certExpired", 3),
          ("certGoingExpired", 2),
          ("certOK", 1))
    )


_CeipSecCertExpiryStatus_Type.__name__ = "Integer32"
_CeipSecCertExpiryStatus_Object = MibScalar
ceipSecCertExpiryStatus = _CeipSecCertExpiryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 1, 6, 6),
    _CeipSecCertExpiryStatus_Type()
)
ceipSecCertExpiryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceipSecCertExpiryStatus.setStatus("current")
_CiscoEnhancedIpsecFlowMIBConform_ObjectIdentity = ObjectIdentity
ciscoEnhancedIpsecFlowMIBConform = _CiscoEnhancedIpsecFlowMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2)
)
_CiscoEnhIPsecFlowMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEnhIPsecFlowMIBCompliances = _CiscoEnhIPsecFlowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 1)
)
_CiscoIPsecFlowMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIPsecFlowMIBGroups = _CiscoIPsecFlowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2)
)

# Managed Objects groups

ciscoEnhIPsecFlowActivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 1)
)
ciscoEnhIPsecFlowActivityGroup.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalActiveTunnels"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalPreviousTunnels"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalInOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalInDecompOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalInPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalInDrops"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalInReplayDrops"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalInAuths"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalInAuthFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalInDecrypts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalInDecryptFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutUncompOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutDrops"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutAuths"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutAuthFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutEncrypts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutEncryptFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalProtocolUseFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalNoSaFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalSysCapFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutCompressedPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutCompSkippedPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutCompFailPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalOutCompTooSmallPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunEncapMode"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunLifeSize"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunLifeTime"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunActiveTime"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaLifeSizeThreshold"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaLifeTimeThreshold"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunTotalRefreshes"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunExpiredSaInstances"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunCurrentSaInstances"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInSaDHGrp"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInSaEncryptAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInSaAhAuthAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInSaEspAuthAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInSaDecompAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutSaDHGrp"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutSaEncryptAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutSaAhAuthAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutSaEspAuthAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutSaCompAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunPmtu"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInDecompOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInDropPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInReplayDropPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInAuths"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInAuthFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInDecrypts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInDecryptFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutUncompOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutDropPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutAuths"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutAuthFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutEncrypts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutEncryptFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutCompressedPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutCompSkippedPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutCompFailPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutCompTooSmallPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecIfIndex"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunStatus"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunControlTunnelIndex"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunControlProtocol"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunControlTunnelAlive"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunInSaEncryptKeySize"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunOutSaEncryptKeySize"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunLocalAddressType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunLocalAddress"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunRemoteAddressType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunRemoteAddress"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunNATTraversalMode"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtLocalName"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtLocalType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtLocalAddrType1"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtLocalAddr1"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtLocalAddrType2"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtLocalAddr2"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtLocalProtocol"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtLocalPort"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtRemoteName"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtRemoteType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtRemoteAddrType1"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtRemoteAddr1"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtRemoteAddrType2"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtRemoteAddr2"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtRemoteProtocol"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtRemotePort"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecSaDirection"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecSaValue"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecSaStatus"))
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowActivityGroup.setStatus("current")

ciscoEnhIPsecFlowCoreHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 2)
)
ciscoEnhIPsecFlowCoreHistGroup.setObjects(
    ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecHistTableSize")
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowCoreHistGroup.setStatus("current")

ciscoEnhIPsecFlowHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 3)
)
ciscoEnhIPsecFlowHistoryGroup.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistTermReason"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistActiveIndex"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistEncapMode"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistLifeSize"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistLifeTime"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistStartTime"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistActiveTime"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistTotalRefreshes"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistTotalSas"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInSaDHGrp"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInSaEncryptAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInSaAhAuthAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInSaEspAuthAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInSaDecompAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutSaDHGrp"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutSaEncryptAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutSaAhAuthAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutSaEspAuthAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutSaCompAlgo"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistPmtu"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInDecompOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInDropPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInReplayDropPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInAuths"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInAuthFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInDecrypts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInDecryptFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutUncompOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutDropPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutAuths"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutAuthFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutEncrypts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutEncryptFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutCompressedPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutCompSkippedPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutCompFailPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutCompSmallPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistControlProtocol"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistControlTunnelIndex"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistInSaEncryptKeySize"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistOutSaEncryptKeySz"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistLocalAddressType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistLocalAddress"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistRemoteAddressType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistRemoteAddress"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistNATTraversalMode"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistTunIndex"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistActiveIndex"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistLocalName"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistLocalType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistLocalAddrType1"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistLocalAddr1"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistLocalAddrType2"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistLocalAddr2"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistLocalProtocol"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistLocalPort"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistRemoteName"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistRemoteType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistRemoteAddrType1"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistRemoteAddr1"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistRemoteAddrType2"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistRemoteAddr2"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistRemoteProtocol"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecEndPtHistRemotePort"))
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowHistoryGroup.setStatus("current")

ciscoEnhIPsecFlowCoreFailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 4)
)
ciscoEnhIPsecFlowCoreFailGroup.setObjects(
    ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailTableSize")
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowCoreFailGroup.setStatus("current")

ciscoEnhIPsecFlowFailureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 5)
)
ciscoEnhIPsecFlowFailureGroup.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailReason"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailTime"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailTunnelIndex"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailSaSpi"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktSrcAddressType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktSrcAddress"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktDstAddressType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktDstAddress"))
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowFailureGroup.setStatus("current")

ciscoEnhIPsecFlowNotifCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 6)
)
ciscoEnhIPsecFlowNotifCntlGroup.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecNotiCntlIpSecAllNotifs"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecNotifCntlIpSecTunnelStart"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecNotifCntlIpSecTunnelStop"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecNotifCntlIpSecSysFailure"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecNotifCntlIpSecSetUpFail"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecNotifCntlIpSecBadSa"))
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowNotifCntlGroup.setStatus("current")

ciscoEnhIPsecFlowTunnelSaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 8)
)
ciscoEnhIPsecFlowTunnelSaGroup.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaValue"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaIfIndex"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaInOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaInDecompOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaInPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaInDropPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaInReplayDropPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaInAuths"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaInAuthFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaInDecrypts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaInDecryptFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutUncompOctets"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutDropPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutAuths"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutAuthFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutEncrypts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutEncryptFails"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutCompressedPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutCompSkippedPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutCompFailPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaOutCompTooSmallPkts"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunSaStatus"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecIfTunnelStatus"))
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowTunnelSaGroup.setStatus("current")

ciscoEnhIPsecFlowNotifCntlGroupSup01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 9)
)
ciscoEnhIPsecFlowNotifCntlGroupSup01.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecNotifCntlCertExpiry"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecNotifCntlCertRenewal"))
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowNotifCntlGroupSup01.setStatus("current")

ciscoEnhIPsecFlowCertObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 11)
)
ciscoEnhIPsecFlowCertObjectGroup.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertSubjectName"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertSerialNumber"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertIssuerName"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertExpiryTime"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertRenewalStatus"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertExpiryStatus"))
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowCertObjectGroup.setStatus("current")

ciscoEnhIPsecFlowPerformanceThroughputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 12)
)
ciscoEnhIPsecFlowPerformanceThroughputGroup.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalThroughputUtilizatioinTimeInterval"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalThroughputLastUpdatedTime"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalLastAveragePacketSize"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalLastThroughputInMbps"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalLastThroughputInKpps"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalLastThroughputUtilization"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalPeakThroughputUtilization"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalPeakThroughputDateAndTime"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalPeakThroughputInMbps"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecGlobalPeakAvgPacketSize"))
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowPerformanceThroughputGroup.setStatus("current")


# Notification objects

ciscoEnhIpsecFlowTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 0, 1)
)
ciscoEnhIpsecFlowTunnelStart.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunLifeTime"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunLifeSize"))
)
if mibBuilder.loadTexts:
    ciscoEnhIpsecFlowTunnelStart.setStatus(
        "current"
    )

ciscoEnhIpsecFlowTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 0, 2)
)
ciscoEnhIpsecFlowTunnelStop.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunHistTermReason"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecTunActiveTime"))
)
if mibBuilder.loadTexts:
    ciscoEnhIpsecFlowTunnelStop.setStatus(
        "current"
    )

ciscoEnhIpsecFlowSysFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 0, 3)
)
ciscoEnhIpsecFlowSysFailure.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailReason"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktSrcAddressType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktSrcAddress"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktDstAddressType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktDstAddress"))
)
if mibBuilder.loadTexts:
    ciscoEnhIpsecFlowSysFailure.setStatus(
        "current"
    )

ciscoEnhIpsecFlowSetupFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 0, 4)
)
ciscoEnhIpsecFlowSetupFail.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailReason"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktSrcAddressType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktSrcAddress"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktDstAddressType"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailPktDstAddress"))
)
if mibBuilder.loadTexts:
    ciscoEnhIpsecFlowSetupFail.setStatus(
        "current"
    )

ciscoEnhIpsecFlowBadSa = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 0, 5)
)
ciscoEnhIpsecFlowBadSa.setObjects(
    ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecFailSaSpi")
)
if mibBuilder.loadTexts:
    ciscoEnhIpsecFlowBadSa.setStatus(
        "current"
    )

ciscoEnhIpsecFlowCertExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 0, 6)
)
ciscoEnhIpsecFlowCertExpiry.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertSubjectName"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertSerialNumber"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertIssuerName"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertExpiryTime"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertExpiryStatus"))
)
if mibBuilder.loadTexts:
    ciscoEnhIpsecFlowCertExpiry.setStatus(
        "current"
    )

ciscoEnhIpsecFlowCertRenewal = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 0, 7)
)
ciscoEnhIpsecFlowCertRenewal.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertSubjectName"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertSerialNumber"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertIssuerName"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertRenewalStatus"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ceipSecCertExpiryTime"))
)
if mibBuilder.loadTexts:
    ciscoEnhIpsecFlowCertRenewal.setStatus(
        "current"
    )


# Notifications groups

ciscoEnhIPsecFlowNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 7)
)
ciscoEnhIPsecFlowNotifGroup.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ciscoEnhIpsecFlowTunnelStart"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ciscoEnhIpsecFlowTunnelStop"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ciscoEnhIpsecFlowSysFailure"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ciscoEnhIpsecFlowSetupFail"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ciscoEnhIpsecFlowBadSa"))
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowNotifGroup.setStatus(
        "current"
    )

ciscoEnhIPsecFlowNotifGroupSup01 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 2, 10)
)
ciscoEnhIPsecFlowNotifGroupSup01.setObjects(
      *(("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ciscoEnhIpsecFlowCertExpiry"),
        ("CISCO-ENHANCED-IPSEC-FLOW-MIB", "ciscoEnhIpsecFlowCertRenewal"))
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowNotifGroupSup01.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEnhIPsecFlowMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowMIBCompliance.setStatus(
        "deprecated"
    )

ciscoEnhIPsecFlowMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoEnhIPsecFlowMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 432, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoEnhIPsecFlowMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENHANCED-IPSEC-FLOW-MIB",
    **{"ciscoEnhancedIpsecFlowMIB": ciscoEnhancedIpsecFlowMIB,
       "ciscoEnhancedIpsecFlowMIBNotifs": ciscoEnhancedIpsecFlowMIBNotifs,
       "ciscoEnhIpsecFlowTunnelStart": ciscoEnhIpsecFlowTunnelStart,
       "ciscoEnhIpsecFlowTunnelStop": ciscoEnhIpsecFlowTunnelStop,
       "ciscoEnhIpsecFlowSysFailure": ciscoEnhIpsecFlowSysFailure,
       "ciscoEnhIpsecFlowSetupFail": ciscoEnhIpsecFlowSetupFail,
       "ciscoEnhIpsecFlowBadSa": ciscoEnhIpsecFlowBadSa,
       "ciscoEnhIpsecFlowCertExpiry": ciscoEnhIpsecFlowCertExpiry,
       "ciscoEnhIpsecFlowCertRenewal": ciscoEnhIpsecFlowCertRenewal,
       "ciscoEnhancedIpsecFlowMIBObjects": ciscoEnhancedIpsecFlowMIBObjects,
       "ceipSecPhaseTwo": ceipSecPhaseTwo,
       "ceipSecGlobalStats": ceipSecGlobalStats,
       "ceipSecGlobalActiveTunnels": ceipSecGlobalActiveTunnels,
       "ceipSecGlobalPreviousTunnels": ceipSecGlobalPreviousTunnels,
       "ceipSecGlobalInOctets": ceipSecGlobalInOctets,
       "ceipSecGlobalInDecompOctets": ceipSecGlobalInDecompOctets,
       "ceipSecGlobalInPkts": ceipSecGlobalInPkts,
       "ceipSecGlobalInDrops": ceipSecGlobalInDrops,
       "ceipSecGlobalInReplayDrops": ceipSecGlobalInReplayDrops,
       "ceipSecGlobalInAuths": ceipSecGlobalInAuths,
       "ceipSecGlobalInAuthFails": ceipSecGlobalInAuthFails,
       "ceipSecGlobalInDecrypts": ceipSecGlobalInDecrypts,
       "ceipSecGlobalInDecryptFails": ceipSecGlobalInDecryptFails,
       "ceipSecGlobalOutOctets": ceipSecGlobalOutOctets,
       "ceipSecGlobalOutUncompOctets": ceipSecGlobalOutUncompOctets,
       "ceipSecGlobalOutPkts": ceipSecGlobalOutPkts,
       "ceipSecGlobalOutDrops": ceipSecGlobalOutDrops,
       "ceipSecGlobalOutAuths": ceipSecGlobalOutAuths,
       "ceipSecGlobalOutAuthFails": ceipSecGlobalOutAuthFails,
       "ceipSecGlobalOutEncrypts": ceipSecGlobalOutEncrypts,
       "ceipSecGlobalOutEncryptFails": ceipSecGlobalOutEncryptFails,
       "ceipSecGlobalProtocolUseFails": ceipSecGlobalProtocolUseFails,
       "ceipSecGlobalNoSaFails": ceipSecGlobalNoSaFails,
       "ceipSecGlobalSysCapFails": ceipSecGlobalSysCapFails,
       "ceipSecGlobalOutCompressedPkts": ceipSecGlobalOutCompressedPkts,
       "ceipSecGlobalOutCompSkippedPkts": ceipSecGlobalOutCompSkippedPkts,
       "ceipSecGlobalOutCompFailPkts": ceipSecGlobalOutCompFailPkts,
       "ceipSecGlobalOutCompTooSmallPkts": ceipSecGlobalOutCompTooSmallPkts,
       "ceipSecGlobalThroughputUtilizatioinTimeInterval": ceipSecGlobalThroughputUtilizatioinTimeInterval,
       "ceipSecGlobalThroughputLastUpdatedTime": ceipSecGlobalThroughputLastUpdatedTime,
       "ceipSecGlobalLastAveragePacketSize": ceipSecGlobalLastAveragePacketSize,
       "ceipSecGlobalLastThroughputInMbps": ceipSecGlobalLastThroughputInMbps,
       "ceipSecGlobalLastThroughputInKpps": ceipSecGlobalLastThroughputInKpps,
       "ceipSecGlobalLastThroughputUtilization": ceipSecGlobalLastThroughputUtilization,
       "ceipSecGlobalPeakThroughputUtilization": ceipSecGlobalPeakThroughputUtilization,
       "ceipSecGlobalPeakThroughputDateAndTime": ceipSecGlobalPeakThroughputDateAndTime,
       "ceipSecGlobalPeakThroughputInMbps": ceipSecGlobalPeakThroughputInMbps,
       "ceipSecGlobalPeakAvgPacketSize": ceipSecGlobalPeakAvgPacketSize,
       "ceipSecTunnelTable": ceipSecTunnelTable,
       "ceipSecTunnelEntry": ceipSecTunnelEntry,
       "ceipSecTunIndex": ceipSecTunIndex,
       "ceipSecTunLocalAddressType": ceipSecTunLocalAddressType,
       "ceipSecTunLocalAddress": ceipSecTunLocalAddress,
       "ceipSecTunRemoteAddressType": ceipSecTunRemoteAddressType,
       "ceipSecTunRemoteAddress": ceipSecTunRemoteAddress,
       "ceipSecTunControlProtocol": ceipSecTunControlProtocol,
       "ceipSecTunControlTunnelIndex": ceipSecTunControlTunnelIndex,
       "ceipSecTunControlTunnelAlive": ceipSecTunControlTunnelAlive,
       "ceipSecTunEncapMode": ceipSecTunEncapMode,
       "ceipSecTunNATTraversalMode": ceipSecTunNATTraversalMode,
       "ceipSecTunLifeSize": ceipSecTunLifeSize,
       "ceipSecTunLifeTime": ceipSecTunLifeTime,
       "ceipSecTunActiveTime": ceipSecTunActiveTime,
       "ceipSecTunSaLifeSizeThreshold": ceipSecTunSaLifeSizeThreshold,
       "ceipSecTunSaLifeTimeThreshold": ceipSecTunSaLifeTimeThreshold,
       "ceipSecTunTotalRefreshes": ceipSecTunTotalRefreshes,
       "ceipSecTunExpiredSaInstances": ceipSecTunExpiredSaInstances,
       "ceipSecTunCurrentSaInstances": ceipSecTunCurrentSaInstances,
       "ceipSecTunInSaDHGrp": ceipSecTunInSaDHGrp,
       "ceipSecTunInSaEncryptAlgo": ceipSecTunInSaEncryptAlgo,
       "ceipSecTunInSaEncryptKeySize": ceipSecTunInSaEncryptKeySize,
       "ceipSecTunInSaAhAuthAlgo": ceipSecTunInSaAhAuthAlgo,
       "ceipSecTunInSaEspAuthAlgo": ceipSecTunInSaEspAuthAlgo,
       "ceipSecTunInSaDecompAlgo": ceipSecTunInSaDecompAlgo,
       "ceipSecTunOutSaDHGrp": ceipSecTunOutSaDHGrp,
       "ceipSecTunOutSaEncryptAlgo": ceipSecTunOutSaEncryptAlgo,
       "ceipSecTunOutSaEncryptKeySize": ceipSecTunOutSaEncryptKeySize,
       "ceipSecTunOutSaAhAuthAlgo": ceipSecTunOutSaAhAuthAlgo,
       "ceipSecTunOutSaEspAuthAlgo": ceipSecTunOutSaEspAuthAlgo,
       "ceipSecTunOutSaCompAlgo": ceipSecTunOutSaCompAlgo,
       "ceipSecTunPmtu": ceipSecTunPmtu,
       "ceipSecTunInOctets": ceipSecTunInOctets,
       "ceipSecTunInDecompOctets": ceipSecTunInDecompOctets,
       "ceipSecTunInPkts": ceipSecTunInPkts,
       "ceipSecTunInDropPkts": ceipSecTunInDropPkts,
       "ceipSecTunInReplayDropPkts": ceipSecTunInReplayDropPkts,
       "ceipSecTunInAuths": ceipSecTunInAuths,
       "ceipSecTunInAuthFails": ceipSecTunInAuthFails,
       "ceipSecTunInDecrypts": ceipSecTunInDecrypts,
       "ceipSecTunInDecryptFails": ceipSecTunInDecryptFails,
       "ceipSecTunOutOctets": ceipSecTunOutOctets,
       "ceipSecTunOutUncompOctets": ceipSecTunOutUncompOctets,
       "ceipSecTunOutPkts": ceipSecTunOutPkts,
       "ceipSecTunOutDropPkts": ceipSecTunOutDropPkts,
       "ceipSecTunOutAuths": ceipSecTunOutAuths,
       "ceipSecTunOutAuthFails": ceipSecTunOutAuthFails,
       "ceipSecTunOutEncrypts": ceipSecTunOutEncrypts,
       "ceipSecTunOutEncryptFails": ceipSecTunOutEncryptFails,
       "ceipSecTunOutCompressedPkts": ceipSecTunOutCompressedPkts,
       "ceipSecTunOutCompSkippedPkts": ceipSecTunOutCompSkippedPkts,
       "ceipSecTunOutCompFailPkts": ceipSecTunOutCompFailPkts,
       "ceipSecTunOutCompTooSmallPkts": ceipSecTunOutCompTooSmallPkts,
       "ceipSecIfIndex": ceipSecIfIndex,
       "ceipSecTunStatus": ceipSecTunStatus,
       "ceipSecEndPtTable": ceipSecEndPtTable,
       "ceipSecEndPtEntry": ceipSecEndPtEntry,
       "ceipSecEndPtIndex": ceipSecEndPtIndex,
       "ceipSecEndPtLocalName": ceipSecEndPtLocalName,
       "ceipSecEndPtLocalType": ceipSecEndPtLocalType,
       "ceipSecEndPtLocalAddrType1": ceipSecEndPtLocalAddrType1,
       "ceipSecEndPtLocalAddr1": ceipSecEndPtLocalAddr1,
       "ceipSecEndPtLocalAddrType2": ceipSecEndPtLocalAddrType2,
       "ceipSecEndPtLocalAddr2": ceipSecEndPtLocalAddr2,
       "ceipSecEndPtLocalProtocol": ceipSecEndPtLocalProtocol,
       "ceipSecEndPtLocalPort": ceipSecEndPtLocalPort,
       "ceipSecEndPtRemoteName": ceipSecEndPtRemoteName,
       "ceipSecEndPtRemoteType": ceipSecEndPtRemoteType,
       "ceipSecEndPtRemoteAddrType1": ceipSecEndPtRemoteAddrType1,
       "ceipSecEndPtRemoteAddr1": ceipSecEndPtRemoteAddr1,
       "ceipSecEndPtRemoteAddrType2": ceipSecEndPtRemoteAddrType2,
       "ceipSecEndPtRemoteAddr2": ceipSecEndPtRemoteAddr2,
       "ceipSecEndPtRemoteProtocol": ceipSecEndPtRemoteProtocol,
       "ceipSecEndPtRemotePort": ceipSecEndPtRemotePort,
       "ceipSecSaTable": ceipSecSaTable,
       "ceipSecSaEntry": ceipSecSaEntry,
       "ceipSecSaProtocol": ceipSecSaProtocol,
       "ceipSecSaIndex": ceipSecSaIndex,
       "ceipSecSaDirection": ceipSecSaDirection,
       "ceipSecSaValue": ceipSecSaValue,
       "ceipSecSaStatus": ceipSecSaStatus,
       "ceipSecTunnelSaTable": ceipSecTunnelSaTable,
       "ceipSecTunnelSaEntry": ceipSecTunnelSaEntry,
       "ceipSecTunSaProtocol": ceipSecTunSaProtocol,
       "ceipSecTunSaIndex": ceipSecTunSaIndex,
       "ceipSecTunSaDirection": ceipSecTunSaDirection,
       "ceipSecTunSaValue": ceipSecTunSaValue,
       "ceipSecTunSaIfIndex": ceipSecTunSaIfIndex,
       "ceipSecTunSaInOctets": ceipSecTunSaInOctets,
       "ceipSecTunSaInDecompOctets": ceipSecTunSaInDecompOctets,
       "ceipSecTunSaInPkts": ceipSecTunSaInPkts,
       "ceipSecTunSaInDropPkts": ceipSecTunSaInDropPkts,
       "ceipSecTunSaInReplayDropPkts": ceipSecTunSaInReplayDropPkts,
       "ceipSecTunSaInAuths": ceipSecTunSaInAuths,
       "ceipSecTunSaInAuthFails": ceipSecTunSaInAuthFails,
       "ceipSecTunSaInDecrypts": ceipSecTunSaInDecrypts,
       "ceipSecTunSaInDecryptFails": ceipSecTunSaInDecryptFails,
       "ceipSecTunSaOutOctets": ceipSecTunSaOutOctets,
       "ceipSecTunSaOutUncompOctets": ceipSecTunSaOutUncompOctets,
       "ceipSecTunSaOutPkts": ceipSecTunSaOutPkts,
       "ceipSecTunSaOutDropPkts": ceipSecTunSaOutDropPkts,
       "ceipSecTunSaOutAuths": ceipSecTunSaOutAuths,
       "ceipSecTunSaOutAuthFails": ceipSecTunSaOutAuthFails,
       "ceipSecTunSaOutEncrypts": ceipSecTunSaOutEncrypts,
       "ceipSecTunSaOutEncryptFails": ceipSecTunSaOutEncryptFails,
       "ceipSecTunSaOutCompressedPkts": ceipSecTunSaOutCompressedPkts,
       "ceipSecTunSaOutCompSkippedPkts": ceipSecTunSaOutCompSkippedPkts,
       "ceipSecTunSaOutCompFailPkts": ceipSecTunSaOutCompFailPkts,
       "ceipSecTunSaOutCompTooSmallPkts": ceipSecTunSaOutCompTooSmallPkts,
       "ceipSecTunSaStatus": ceipSecTunSaStatus,
       "ceipSecIfTunnelTable": ceipSecIfTunnelTable,
       "ceipSecIfTunnelEntry": ceipSecIfTunnelEntry,
       "ceipSecIfTunnelStatus": ceipSecIfTunnelStatus,
       "ceipSecHistory": ceipSecHistory,
       "ceipSecHistGlobal": ceipSecHistGlobal,
       "ceipSecHistGlobalCntl": ceipSecHistGlobalCntl,
       "ceipSecHistTableSize": ceipSecHistTableSize,
       "ceipSecTunnelHistTable": ceipSecTunnelHistTable,
       "ceipSecTunnelHistEntry": ceipSecTunnelHistEntry,
       "ceipSecTunHistIndex": ceipSecTunHistIndex,
       "ceipSecTunHistTermReason": ceipSecTunHistTermReason,
       "ceipSecTunHistActiveIndex": ceipSecTunHistActiveIndex,
       "ceipSecTunHistLocalAddressType": ceipSecTunHistLocalAddressType,
       "ceipSecTunHistLocalAddress": ceipSecTunHistLocalAddress,
       "ceipSecTunHistRemoteAddressType": ceipSecTunHistRemoteAddressType,
       "ceipSecTunHistRemoteAddress": ceipSecTunHistRemoteAddress,
       "ceipSecTunHistControlProtocol": ceipSecTunHistControlProtocol,
       "ceipSecTunHistControlTunnelIndex": ceipSecTunHistControlTunnelIndex,
       "ceipSecTunHistEncapMode": ceipSecTunHistEncapMode,
       "ceipSecTunHistNATTraversalMode": ceipSecTunHistNATTraversalMode,
       "ceipSecTunHistLifeSize": ceipSecTunHistLifeSize,
       "ceipSecTunHistLifeTime": ceipSecTunHistLifeTime,
       "ceipSecTunHistStartTime": ceipSecTunHistStartTime,
       "ceipSecTunHistActiveTime": ceipSecTunHistActiveTime,
       "ceipSecTunHistTotalRefreshes": ceipSecTunHistTotalRefreshes,
       "ceipSecTunHistTotalSas": ceipSecTunHistTotalSas,
       "ceipSecTunHistInSaDHGrp": ceipSecTunHistInSaDHGrp,
       "ceipSecTunHistInSaEncryptAlgo": ceipSecTunHistInSaEncryptAlgo,
       "ceipSecTunHistInSaEncryptKeySize": ceipSecTunHistInSaEncryptKeySize,
       "ceipSecTunHistInSaAhAuthAlgo": ceipSecTunHistInSaAhAuthAlgo,
       "ceipSecTunHistInSaEspAuthAlgo": ceipSecTunHistInSaEspAuthAlgo,
       "ceipSecTunHistInSaDecompAlgo": ceipSecTunHistInSaDecompAlgo,
       "ceipSecTunHistOutSaDHGrp": ceipSecTunHistOutSaDHGrp,
       "ceipSecTunHistOutSaEncryptAlgo": ceipSecTunHistOutSaEncryptAlgo,
       "ceipSecTunHistOutSaEncryptKeySz": ceipSecTunHistOutSaEncryptKeySz,
       "ceipSecTunHistOutSaAhAuthAlgo": ceipSecTunHistOutSaAhAuthAlgo,
       "ceipSecTunHistOutSaEspAuthAlgo": ceipSecTunHistOutSaEspAuthAlgo,
       "ceipSecTunHistOutSaCompAlgo": ceipSecTunHistOutSaCompAlgo,
       "ceipSecTunHistPmtu": ceipSecTunHistPmtu,
       "ceipSecTunHistInOctets": ceipSecTunHistInOctets,
       "ceipSecTunHistInDecompOctets": ceipSecTunHistInDecompOctets,
       "ceipSecTunHistInPkts": ceipSecTunHistInPkts,
       "ceipSecTunHistInDropPkts": ceipSecTunHistInDropPkts,
       "ceipSecTunHistInReplayDropPkts": ceipSecTunHistInReplayDropPkts,
       "ceipSecTunHistInAuths": ceipSecTunHistInAuths,
       "ceipSecTunHistInAuthFails": ceipSecTunHistInAuthFails,
       "ceipSecTunHistInDecrypts": ceipSecTunHistInDecrypts,
       "ceipSecTunHistInDecryptFails": ceipSecTunHistInDecryptFails,
       "ceipSecTunHistOutOctets": ceipSecTunHistOutOctets,
       "ceipSecTunHistOutUncompOctets": ceipSecTunHistOutUncompOctets,
       "ceipSecTunHistOutPkts": ceipSecTunHistOutPkts,
       "ceipSecTunHistOutDropPkts": ceipSecTunHistOutDropPkts,
       "ceipSecTunHistOutAuths": ceipSecTunHistOutAuths,
       "ceipSecTunHistOutAuthFails": ceipSecTunHistOutAuthFails,
       "ceipSecTunHistOutEncrypts": ceipSecTunHistOutEncrypts,
       "ceipSecTunHistOutEncryptFails": ceipSecTunHistOutEncryptFails,
       "ceipSecTunHistOutCompressedPkts": ceipSecTunHistOutCompressedPkts,
       "ceipSecTunHistOutCompSkippedPkts": ceipSecTunHistOutCompSkippedPkts,
       "ceipSecTunHistOutCompFailPkts": ceipSecTunHistOutCompFailPkts,
       "ceipSecTunHistOutCompSmallPkts": ceipSecTunHistOutCompSmallPkts,
       "ceipSecEndPtHistTable": ceipSecEndPtHistTable,
       "ceipSecEndPtHistEntry": ceipSecEndPtHistEntry,
       "ceipSecEndPtHistIndex": ceipSecEndPtHistIndex,
       "ceipSecEndPtHistTunIndex": ceipSecEndPtHistTunIndex,
       "ceipSecEndPtHistActiveIndex": ceipSecEndPtHistActiveIndex,
       "ceipSecEndPtHistLocalName": ceipSecEndPtHistLocalName,
       "ceipSecEndPtHistLocalType": ceipSecEndPtHistLocalType,
       "ceipSecEndPtHistLocalAddrType1": ceipSecEndPtHistLocalAddrType1,
       "ceipSecEndPtHistLocalAddr1": ceipSecEndPtHistLocalAddr1,
       "ceipSecEndPtHistLocalAddrType2": ceipSecEndPtHistLocalAddrType2,
       "ceipSecEndPtHistLocalAddr2": ceipSecEndPtHistLocalAddr2,
       "ceipSecEndPtHistLocalProtocol": ceipSecEndPtHistLocalProtocol,
       "ceipSecEndPtHistLocalPort": ceipSecEndPtHistLocalPort,
       "ceipSecEndPtHistRemoteName": ceipSecEndPtHistRemoteName,
       "ceipSecEndPtHistRemoteType": ceipSecEndPtHistRemoteType,
       "ceipSecEndPtHistRemoteAddrType1": ceipSecEndPtHistRemoteAddrType1,
       "ceipSecEndPtHistRemoteAddr1": ceipSecEndPtHistRemoteAddr1,
       "ceipSecEndPtHistRemoteAddrType2": ceipSecEndPtHistRemoteAddrType2,
       "ceipSecEndPtHistRemoteAddr2": ceipSecEndPtHistRemoteAddr2,
       "ceipSecEndPtHistRemoteProtocol": ceipSecEndPtHistRemoteProtocol,
       "ceipSecEndPtHistRemotePort": ceipSecEndPtHistRemotePort,
       "ceipSecFailures": ceipSecFailures,
       "ceipSecFailGlobal": ceipSecFailGlobal,
       "ceipSecFailGlobalCntl": ceipSecFailGlobalCntl,
       "ceipSecFailTableSize": ceipSecFailTableSize,
       "ceipSecFailTable": ceipSecFailTable,
       "ceipSecFailEntry": ceipSecFailEntry,
       "ceipSecFailIndex": ceipSecFailIndex,
       "ceipSecFailReason": ceipSecFailReason,
       "ceipSecFailTime": ceipSecFailTime,
       "ceipSecFailTunnelIndex": ceipSecFailTunnelIndex,
       "ceipSecFailSaSpi": ceipSecFailSaSpi,
       "ceipSecFailPktSrcAddressType": ceipSecFailPktSrcAddressType,
       "ceipSecFailPktSrcAddress": ceipSecFailPktSrcAddress,
       "ceipSecFailPktDstAddressType": ceipSecFailPktDstAddressType,
       "ceipSecFailPktDstAddress": ceipSecFailPktDstAddress,
       "ceipSecNotificationCntl": ceipSecNotificationCntl,
       "ceipSecNotiCntlIpSecAllNotifs": ceipSecNotiCntlIpSecAllNotifs,
       "ceipSecNotifCntlIpSecTunnelStart": ceipSecNotifCntlIpSecTunnelStart,
       "ceipSecNotifCntlIpSecTunnelStop": ceipSecNotifCntlIpSecTunnelStop,
       "ceipSecNotifCntlIpSecSysFailure": ceipSecNotifCntlIpSecSysFailure,
       "ceipSecNotifCntlIpSecSetUpFail": ceipSecNotifCntlIpSecSetUpFail,
       "ceipSecNotifCntlIpSecBadSa": ceipSecNotifCntlIpSecBadSa,
       "ceipSecNotifCntlCertExpiry": ceipSecNotifCntlCertExpiry,
       "ceipSecNotifCntlCertRenewal": ceipSecNotifCntlCertRenewal,
       "ceipSecCertNotification": ceipSecCertNotification,
       "ceipSecCertSubjectName": ceipSecCertSubjectName,
       "ceipSecCertSerialNumber": ceipSecCertSerialNumber,
       "ceipSecCertIssuerName": ceipSecCertIssuerName,
       "ceipSecCertExpiryTime": ceipSecCertExpiryTime,
       "ceipSecCertRenewalStatus": ceipSecCertRenewalStatus,
       "ceipSecCertExpiryStatus": ceipSecCertExpiryStatus,
       "ciscoEnhancedIpsecFlowMIBConform": ciscoEnhancedIpsecFlowMIBConform,
       "ciscoEnhIPsecFlowMIBCompliances": ciscoEnhIPsecFlowMIBCompliances,
       "ciscoEnhIPsecFlowMIBCompliance": ciscoEnhIPsecFlowMIBCompliance,
       "ciscoEnhIPsecFlowMIBComplianceRev1": ciscoEnhIPsecFlowMIBComplianceRev1,
       "ciscoEnhIPsecFlowMIBComplianceRev2": ciscoEnhIPsecFlowMIBComplianceRev2,
       "ciscoIPsecFlowMIBGroups": ciscoIPsecFlowMIBGroups,
       "ciscoEnhIPsecFlowActivityGroup": ciscoEnhIPsecFlowActivityGroup,
       "ciscoEnhIPsecFlowCoreHistGroup": ciscoEnhIPsecFlowCoreHistGroup,
       "ciscoEnhIPsecFlowHistoryGroup": ciscoEnhIPsecFlowHistoryGroup,
       "ciscoEnhIPsecFlowCoreFailGroup": ciscoEnhIPsecFlowCoreFailGroup,
       "ciscoEnhIPsecFlowFailureGroup": ciscoEnhIPsecFlowFailureGroup,
       "ciscoEnhIPsecFlowNotifCntlGroup": ciscoEnhIPsecFlowNotifCntlGroup,
       "ciscoEnhIPsecFlowNotifGroup": ciscoEnhIPsecFlowNotifGroup,
       "ciscoEnhIPsecFlowTunnelSaGroup": ciscoEnhIPsecFlowTunnelSaGroup,
       "ciscoEnhIPsecFlowNotifCntlGroupSup01": ciscoEnhIPsecFlowNotifCntlGroupSup01,
       "ciscoEnhIPsecFlowNotifGroupSup01": ciscoEnhIPsecFlowNotifGroupSup01,
       "ciscoEnhIPsecFlowCertObjectGroup": ciscoEnhIPsecFlowCertObjectGroup,
       "ciscoEnhIPsecFlowPerformanceThroughputGroup": ciscoEnhIPsecFlowPerformanceThroughputGroup}
)

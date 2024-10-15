# SNMP MIB module (CISCO-IPSEC-SIGNALING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSEC-SIGNALING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:20 2024
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

(CIPsecControlProtocol,
 CIPsecEncryptAlgorithm,
 CIPsecEncryptionKeySize,
 CIPsecIkeAuthMethod,
 CIPsecIkeHashAlgorithm,
 CIPsecPhase1PeerIdentityType,
 CIPsecPhase1TunnelIndex,
 CIPsecTunnelStatus) = mibBuilder.importSymbols(
    "CISCO-IPSEC-TC",
    "CIPsecControlProtocol",
    "CIPsecEncryptAlgorithm",
    "CIPsecEncryptionKeySize",
    "CIPsecIkeAuthMethod",
    "CIPsecIkeHashAlgorithm",
    "CIPsecPhase1PeerIdentityType",
    "CIPsecPhase1TunnelIndex",
    "CIPsecTunnelStatus")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(DisplayString,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIPsecSignalingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438)
)
ciscoIPsecSignalingMIB.setRevisions(
        ("2004-09-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIPsecSigMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIPsecSigMIBNotifs = _CiscoIPsecSigMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 0)
)
_CiscoIPsecSigMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIPsecSigMIBObjects = _CiscoIPsecSigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1)
)
_CisgIpsSgCurrentActivity_ObjectIdentity = ObjectIdentity
cisgIpsSgCurrentActivity = _CisgIpsSgCurrentActivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1)
)
_CisgIpsSgGlobalStatsTable_Object = MibTable
cisgIpsSgGlobalStatsTable = _CisgIpsSgGlobalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cisgIpsSgGlobalStatsTable.setStatus("current")
_CisgIpsSgGlobalStatsEntry_Object = MibTableRow
cisgIpsSgGlobalStatsEntry = _CisgIpsSgGlobalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1)
)
cisgIpsSgGlobalStatsEntry.setIndexNames(
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"),
)
if mibBuilder.loadTexts:
    cisgIpsSgGlobalStatsEntry.setStatus("current")
_CisgIpsSgProtocol_Type = CIPsecControlProtocol
_CisgIpsSgProtocol_Object = MibTableColumn
cisgIpsSgProtocol = _CisgIpsSgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 1),
    _CisgIpsSgProtocol_Type()
)
cisgIpsSgProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisgIpsSgProtocol.setStatus("current")
_CisgIpsSgGlobalActiveTunnels_Type = Gauge32
_CisgIpsSgGlobalActiveTunnels_Object = MibTableColumn
cisgIpsSgGlobalActiveTunnels = _CisgIpsSgGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 2),
    _CisgIpsSgGlobalActiveTunnels_Type()
)
cisgIpsSgGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalActiveTunnels.setStatus("current")
_CisgIpsSgGlobalPreviousTunnels_Type = Counter64
_CisgIpsSgGlobalPreviousTunnels_Object = MibTableColumn
cisgIpsSgGlobalPreviousTunnels = _CisgIpsSgGlobalPreviousTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 3),
    _CisgIpsSgGlobalPreviousTunnels_Type()
)
cisgIpsSgGlobalPreviousTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalPreviousTunnels.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalPreviousTunnels.setUnits("SAs")
_CisgIpsSgGlobalInOctets_Type = Counter64
_CisgIpsSgGlobalInOctets_Object = MibTableColumn
cisgIpsSgGlobalInOctets = _CisgIpsSgGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 4),
    _CisgIpsSgGlobalInOctets_Type()
)
cisgIpsSgGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInOctets.setUnits("Octets")
_CisgIpsSgGlobalInPkts_Type = Counter64
_CisgIpsSgGlobalInPkts_Object = MibTableColumn
cisgIpsSgGlobalInPkts = _CisgIpsSgGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 5),
    _CisgIpsSgGlobalInPkts_Type()
)
cisgIpsSgGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInPkts.setUnits("Packets")
_CisgIpsSgGlobalInDropPkts_Type = Counter64
_CisgIpsSgGlobalInDropPkts_Object = MibTableColumn
cisgIpsSgGlobalInDropPkts = _CisgIpsSgGlobalInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 6),
    _CisgIpsSgGlobalInDropPkts_Type()
)
cisgIpsSgGlobalInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInDropPkts.setUnits("Packets")
_CisgIpsSgGlobalInNotifys_Type = Counter64
_CisgIpsSgGlobalInNotifys_Object = MibTableColumn
cisgIpsSgGlobalInNotifys = _CisgIpsSgGlobalInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 7),
    _CisgIpsSgGlobalInNotifys_Type()
)
cisgIpsSgGlobalInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInNotifys.setUnits("Notification Payloads")
_CisgIpsSgGlobalInP2SaDelReqs_Type = Counter64
_CisgIpsSgGlobalInP2SaDelReqs_Object = MibTableColumn
cisgIpsSgGlobalInP2SaDelReqs = _CisgIpsSgGlobalInP2SaDelReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 8),
    _CisgIpsSgGlobalInP2SaDelReqs_Type()
)
cisgIpsSgGlobalInP2SaDelReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInP2SaDelReqs.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInP2SaDelReqs.setUnits("Notification Payloads")
_CisgIpsSgGlobalOutOctets_Type = Counter64
_CisgIpsSgGlobalOutOctets_Object = MibTableColumn
cisgIpsSgGlobalOutOctets = _CisgIpsSgGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 9),
    _CisgIpsSgGlobalOutOctets_Type()
)
cisgIpsSgGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutOctets.setUnits("Octets")
_CisgIpsSgGlobalOutPkts_Type = Counter64
_CisgIpsSgGlobalOutPkts_Object = MibTableColumn
cisgIpsSgGlobalOutPkts = _CisgIpsSgGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 10),
    _CisgIpsSgGlobalOutPkts_Type()
)
cisgIpsSgGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutPkts.setUnits("Packets")
_CisgIpsSgGlobalOutDropPkts_Type = Counter64
_CisgIpsSgGlobalOutDropPkts_Object = MibTableColumn
cisgIpsSgGlobalOutDropPkts = _CisgIpsSgGlobalOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 11),
    _CisgIpsSgGlobalOutDropPkts_Type()
)
cisgIpsSgGlobalOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutDropPkts.setUnits("Packets")
_CisgIpsSgGlobalOutNotifys_Type = Counter64
_CisgIpsSgGlobalOutNotifys_Object = MibTableColumn
cisgIpsSgGlobalOutNotifys = _CisgIpsSgGlobalOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 12),
    _CisgIpsSgGlobalOutNotifys_Type()
)
cisgIpsSgGlobalOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutNotifys.setUnits("Notification Payloads")
_CisgIpsSgGlobalOutP2SaDelReqs_Type = Counter64
_CisgIpsSgGlobalOutP2SaDelReqs_Object = MibTableColumn
cisgIpsSgGlobalOutP2SaDelReqs = _CisgIpsSgGlobalOutP2SaDelReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 13),
    _CisgIpsSgGlobalOutP2SaDelReqs_Type()
)
cisgIpsSgGlobalOutP2SaDelReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutP2SaDelReqs.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutP2SaDelReqs.setUnits("Notification Payloads")
_CisgIpsSgGlobalInitTunnels_Type = Counter64
_CisgIpsSgGlobalInitTunnels_Object = MibTableColumn
cisgIpsSgGlobalInitTunnels = _CisgIpsSgGlobalInitTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 14),
    _CisgIpsSgGlobalInitTunnels_Type()
)
cisgIpsSgGlobalInitTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInitTunnels.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInitTunnels.setUnits("SAs")
_CisgIpsSgGlobalInitTunnelFails_Type = Counter64
_CisgIpsSgGlobalInitTunnelFails_Object = MibTableColumn
cisgIpsSgGlobalInitTunnelFails = _CisgIpsSgGlobalInitTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 15),
    _CisgIpsSgGlobalInitTunnelFails_Type()
)
cisgIpsSgGlobalInitTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInitTunnelFails.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInitTunnelFails.setUnits("SAs")
_CisgIpsSgGlobalRespTunnels_Type = Counter64
_CisgIpsSgGlobalRespTunnels_Object = MibTableColumn
cisgIpsSgGlobalRespTunnels = _CisgIpsSgGlobalRespTunnels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 16),
    _CisgIpsSgGlobalRespTunnels_Type()
)
cisgIpsSgGlobalRespTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalRespTunnels.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalRespTunnels.setUnits("SAs")
_CisgIpsSgGlobalRespTunnelFails_Type = Counter64
_CisgIpsSgGlobalRespTunnelFails_Object = MibTableColumn
cisgIpsSgGlobalRespTunnelFails = _CisgIpsSgGlobalRespTunnelFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 17),
    _CisgIpsSgGlobalRespTunnelFails_Type()
)
cisgIpsSgGlobalRespTunnelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalRespTunnelFails.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalRespTunnelFails.setUnits("SAs")
_CisgIpsSgGlobalSysCapFails_Type = Counter64
_CisgIpsSgGlobalSysCapFails_Object = MibTableColumn
cisgIpsSgGlobalSysCapFails = _CisgIpsSgGlobalSysCapFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 18),
    _CisgIpsSgGlobalSysCapFails_Type()
)
cisgIpsSgGlobalSysCapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalSysCapFails.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalSysCapFails.setUnits("Failures")
_CisgIpsSgGlobalAuthFails_Type = Counter64
_CisgIpsSgGlobalAuthFails_Object = MibTableColumn
cisgIpsSgGlobalAuthFails = _CisgIpsSgGlobalAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 19),
    _CisgIpsSgGlobalAuthFails_Type()
)
cisgIpsSgGlobalAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalAuthFails.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalAuthFails.setUnits("Failures")
_CisgIpsSgGlobalDecryptFails_Type = Counter64
_CisgIpsSgGlobalDecryptFails_Object = MibTableColumn
cisgIpsSgGlobalDecryptFails = _CisgIpsSgGlobalDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 20),
    _CisgIpsSgGlobalDecryptFails_Type()
)
cisgIpsSgGlobalDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalDecryptFails.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalDecryptFails.setUnits("Failures")
_CisgIpsSgGlobalHashValidFails_Type = Counter64
_CisgIpsSgGlobalHashValidFails_Object = MibTableColumn
cisgIpsSgGlobalHashValidFails = _CisgIpsSgGlobalHashValidFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 21),
    _CisgIpsSgGlobalHashValidFails_Type()
)
cisgIpsSgGlobalHashValidFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalHashValidFails.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalHashValidFails.setUnits("Failures")
_CisgIpsSgGlobalBadTunnelRefs_Type = Counter64
_CisgIpsSgGlobalBadTunnelRefs_Object = MibTableColumn
cisgIpsSgGlobalBadTunnelRefs = _CisgIpsSgGlobalBadTunnelRefs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 22),
    _CisgIpsSgGlobalBadTunnelRefs_Type()
)
cisgIpsSgGlobalBadTunnelRefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalBadTunnelRefs.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalBadTunnelRefs.setUnits("Failures")
_CisgIpsSgGlobalInP1SaDelReqs_Type = Counter64
_CisgIpsSgGlobalInP1SaDelReqs_Object = MibTableColumn
cisgIpsSgGlobalInP1SaDelReqs = _CisgIpsSgGlobalInP1SaDelReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 23),
    _CisgIpsSgGlobalInP1SaDelReqs_Type()
)
cisgIpsSgGlobalInP1SaDelReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInP1SaDelReqs.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalInP1SaDelReqs.setUnits("Notification Payloads")
_CisgIpsSgGlobalOutP1SaDelReqs_Type = Counter64
_CisgIpsSgGlobalOutP1SaDelReqs_Object = MibTableColumn
cisgIpsSgGlobalOutP1SaDelReqs = _CisgIpsSgGlobalOutP1SaDelReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 1, 1, 24),
    _CisgIpsSgGlobalOutP1SaDelReqs_Type()
)
cisgIpsSgGlobalOutP1SaDelReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutP1SaDelReqs.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgGlobalOutP1SaDelReqs.setUnits("Notification Payloads")
_CisgIpsSgTunnelTable_Object = MibTable
cisgIpsSgTunnelTable = _CisgIpsSgTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cisgIpsSgTunnelTable.setStatus("current")
_CisgIpsSgTunnelEntry_Object = MibTableRow
cisgIpsSgTunnelEntry = _CisgIpsSgTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1)
)
cisgIpsSgTunnelEntry.setIndexNames(
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"),
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunIndex"),
)
if mibBuilder.loadTexts:
    cisgIpsSgTunnelEntry.setStatus("current")
_CisgIpsSgTunIndex_Type = CIPsecPhase1TunnelIndex
_CisgIpsSgTunIndex_Object = MibTableColumn
cisgIpsSgTunIndex = _CisgIpsSgTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 1),
    _CisgIpsSgTunIndex_Type()
)
cisgIpsSgTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisgIpsSgTunIndex.setStatus("current")
_CisgIpsSgTunLocalType_Type = CIPsecPhase1PeerIdentityType
_CisgIpsSgTunLocalType_Object = MibTableColumn
cisgIpsSgTunLocalType = _CisgIpsSgTunLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 2),
    _CisgIpsSgTunLocalType_Type()
)
cisgIpsSgTunLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunLocalType.setStatus("current")


class _CisgIpsSgTunLocalValue_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunLocalValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CisgIpsSgTunLocalValue_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunLocalValue_Object = MibTableColumn
cisgIpsSgTunLocalValue = _CisgIpsSgTunLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 3),
    _CisgIpsSgTunLocalValue_Type()
)
cisgIpsSgTunLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunLocalValue.setStatus("current")
_CisgIpsSgTunLocalAddressType_Type = CIPsecPhase1PeerIdentityType
_CisgIpsSgTunLocalAddressType_Object = MibTableColumn
cisgIpsSgTunLocalAddressType = _CisgIpsSgTunLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 4),
    _CisgIpsSgTunLocalAddressType_Type()
)
cisgIpsSgTunLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunLocalAddressType.setStatus("current")


class _CisgIpsSgTunLocalAddress_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunLocalAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CisgIpsSgTunLocalAddress_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunLocalAddress_Object = MibTableColumn
cisgIpsSgTunLocalAddress = _CisgIpsSgTunLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 5),
    _CisgIpsSgTunLocalAddress_Type()
)
cisgIpsSgTunLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunLocalAddress.setStatus("current")


class _CisgIpsSgTunLocalName_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunLocalName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CisgIpsSgTunLocalName_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunLocalName_Object = MibTableColumn
cisgIpsSgTunLocalName = _CisgIpsSgTunLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 6),
    _CisgIpsSgTunLocalName_Type()
)
cisgIpsSgTunLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunLocalName.setStatus("current")
_CisgIpsSgTunRemoteType_Type = CIPsecPhase1PeerIdentityType
_CisgIpsSgTunRemoteType_Object = MibTableColumn
cisgIpsSgTunRemoteType = _CisgIpsSgTunRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 7),
    _CisgIpsSgTunRemoteType_Type()
)
cisgIpsSgTunRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunRemoteType.setStatus("current")


class _CisgIpsSgTunRemoteValue_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunRemoteValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CisgIpsSgTunRemoteValue_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunRemoteValue_Object = MibTableColumn
cisgIpsSgTunRemoteValue = _CisgIpsSgTunRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 8),
    _CisgIpsSgTunRemoteValue_Type()
)
cisgIpsSgTunRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunRemoteValue.setStatus("current")
_CisgIpsSgTunRemoteAddressType_Type = CIPsecPhase1PeerIdentityType
_CisgIpsSgTunRemoteAddressType_Object = MibTableColumn
cisgIpsSgTunRemoteAddressType = _CisgIpsSgTunRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 9),
    _CisgIpsSgTunRemoteAddressType_Type()
)
cisgIpsSgTunRemoteAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunRemoteAddressType.setStatus("current")


class _CisgIpsSgTunRemoteAddress_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunRemoteAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CisgIpsSgTunRemoteAddress_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunRemoteAddress_Object = MibTableColumn
cisgIpsSgTunRemoteAddress = _CisgIpsSgTunRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 10),
    _CisgIpsSgTunRemoteAddress_Type()
)
cisgIpsSgTunRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunRemoteAddress.setStatus("current")


class _CisgIpsSgTunRemoteName_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunRemoteName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CisgIpsSgTunRemoteName_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunRemoteName_Object = MibTableColumn
cisgIpsSgTunRemoteName = _CisgIpsSgTunRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 11),
    _CisgIpsSgTunRemoteName_Type()
)
cisgIpsSgTunRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunRemoteName.setStatus("current")
_CisgIpsSgTunEncryptAlgo_Type = CIPsecEncryptAlgorithm
_CisgIpsSgTunEncryptAlgo_Object = MibTableColumn
cisgIpsSgTunEncryptAlgo = _CisgIpsSgTunEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 12),
    _CisgIpsSgTunEncryptAlgo_Type()
)
cisgIpsSgTunEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunEncryptAlgo.setStatus("current")
_CisgIpsSgTunEncryptKeySize_Type = CIPsecEncryptionKeySize
_CisgIpsSgTunEncryptKeySize_Object = MibTableColumn
cisgIpsSgTunEncryptKeySize = _CisgIpsSgTunEncryptKeySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 13),
    _CisgIpsSgTunEncryptKeySize_Type()
)
cisgIpsSgTunEncryptKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunEncryptKeySize.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunEncryptKeySize.setUnits("Bits")
_CisgIpsSgTunHashAlgo_Type = CIPsecIkeHashAlgorithm
_CisgIpsSgTunHashAlgo_Object = MibTableColumn
cisgIpsSgTunHashAlgo = _CisgIpsSgTunHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 14),
    _CisgIpsSgTunHashAlgo_Type()
)
cisgIpsSgTunHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHashAlgo.setStatus("current")
_CisgIpsSgTunAuthMethod_Type = CIPsecIkeAuthMethod
_CisgIpsSgTunAuthMethod_Object = MibTableColumn
cisgIpsSgTunAuthMethod = _CisgIpsSgTunAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 15),
    _CisgIpsSgTunAuthMethod_Type()
)
cisgIpsSgTunAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunAuthMethod.setStatus("current")


class _CisgIpsSgTunLifeTime_Type(Unsigned32):
    """Custom type cisgIpsSgTunLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CisgIpsSgTunLifeTime_Type.__name__ = "Unsigned32"
_CisgIpsSgTunLifeTime_Object = MibTableColumn
cisgIpsSgTunLifeTime = _CisgIpsSgTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 16),
    _CisgIpsSgTunLifeTime_Type()
)
cisgIpsSgTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunLifeTime.setUnits("seconds")
_CisgIpsSgTunActiveTime_Type = TimeInterval
_CisgIpsSgTunActiveTime_Object = MibTableColumn
cisgIpsSgTunActiveTime = _CisgIpsSgTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 17),
    _CisgIpsSgTunActiveTime_Type()
)
cisgIpsSgTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunActiveTime.setStatus("current")
_CisgIpsSgTunInOctets_Type = Counter32
_CisgIpsSgTunInOctets_Object = MibTableColumn
cisgIpsSgTunInOctets = _CisgIpsSgTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 18),
    _CisgIpsSgTunInOctets_Type()
)
cisgIpsSgTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunInOctets.setUnits("Octets")
_CisgIpsSgTunInPkts_Type = Counter32
_CisgIpsSgTunInPkts_Object = MibTableColumn
cisgIpsSgTunInPkts = _CisgIpsSgTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 19),
    _CisgIpsSgTunInPkts_Type()
)
cisgIpsSgTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunInPkts.setUnits("Packets")
_CisgIpsSgTunInDropPkts_Type = Counter32
_CisgIpsSgTunInDropPkts_Object = MibTableColumn
cisgIpsSgTunInDropPkts = _CisgIpsSgTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 20),
    _CisgIpsSgTunInDropPkts_Type()
)
cisgIpsSgTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunInDropPkts.setUnits("Packets")
_CisgIpsSgTunInNotifys_Type = Counter32
_CisgIpsSgTunInNotifys_Object = MibTableColumn
cisgIpsSgTunInNotifys = _CisgIpsSgTunInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 21),
    _CisgIpsSgTunInNotifys_Type()
)
cisgIpsSgTunInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunInNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunInNotifys.setUnits("Notification Payloads")
_CisgIpsSgTunOutOctets_Type = Counter32
_CisgIpsSgTunOutOctets_Object = MibTableColumn
cisgIpsSgTunOutOctets = _CisgIpsSgTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 22),
    _CisgIpsSgTunOutOctets_Type()
)
cisgIpsSgTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunOutOctets.setUnits("Octets")
_CisgIpsSgTunOutPkts_Type = Counter32
_CisgIpsSgTunOutPkts_Object = MibTableColumn
cisgIpsSgTunOutPkts = _CisgIpsSgTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 23),
    _CisgIpsSgTunOutPkts_Type()
)
cisgIpsSgTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunOutPkts.setUnits("Packets")
_CisgIpsSgTunOutDropPkts_Type = Counter32
_CisgIpsSgTunOutDropPkts_Object = MibTableColumn
cisgIpsSgTunOutDropPkts = _CisgIpsSgTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 24),
    _CisgIpsSgTunOutDropPkts_Type()
)
cisgIpsSgTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunOutDropPkts.setUnits("Packets")
_CisgIpsSgTunOutNotifys_Type = Counter32
_CisgIpsSgTunOutNotifys_Object = MibTableColumn
cisgIpsSgTunOutNotifys = _CisgIpsSgTunOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 25),
    _CisgIpsSgTunOutNotifys_Type()
)
cisgIpsSgTunOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunOutNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunOutNotifys.setUnits("Notification Payloads")
_CisgIpsSgTunOutP2SaDelReqs_Type = Counter32
_CisgIpsSgTunOutP2SaDelReqs_Object = MibTableColumn
cisgIpsSgTunOutP2SaDelReqs = _CisgIpsSgTunOutP2SaDelReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 26),
    _CisgIpsSgTunOutP2SaDelReqs_Type()
)
cisgIpsSgTunOutP2SaDelReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunOutP2SaDelReqs.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunOutP2SaDelReqs.setUnits("Notification Payloads")
_CisgIpsSgTunStatus_Type = CIPsecTunnelStatus
_CisgIpsSgTunStatus_Object = MibTableColumn
cisgIpsSgTunStatus = _CisgIpsSgTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 27),
    _CisgIpsSgTunStatus_Type()
)
cisgIpsSgTunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunStatus.setStatus("current")


class _CisgIpsSgTunAction_Type(Integer32):
    """Custom type cisgIpsSgTunAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("none", 1),
          ("rekey", 3))
    )


_CisgIpsSgTunAction_Type.__name__ = "Integer32"
_CisgIpsSgTunAction_Object = MibTableColumn
cisgIpsSgTunAction = _CisgIpsSgTunAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 1, 2, 1, 28),
    _CisgIpsSgTunAction_Type()
)
cisgIpsSgTunAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisgIpsSgTunAction.setStatus("current")
_CisgIpsSgPeerAssociations_ObjectIdentity = ObjectIdentity
cisgIpsSgPeerAssociations = _CisgIpsSgPeerAssociations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 2)
)
_CisgIpsSgHistory_ObjectIdentity = ObjectIdentity
cisgIpsSgHistory = _CisgIpsSgHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3)
)
_CisgIpsSgHistGlobal_ObjectIdentity = ObjectIdentity
cisgIpsSgHistGlobal = _CisgIpsSgHistGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 1)
)
_CisgIpsSgHistGlobalCntl_ObjectIdentity = ObjectIdentity
cisgIpsSgHistGlobalCntl = _CisgIpsSgHistGlobalCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 1, 1)
)


class _CisgIpsSgHistTableSize_Type(Unsigned32):
    """Custom type cisgIpsSgHistTableSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CisgIpsSgHistTableSize_Type.__name__ = "Unsigned32"
_CisgIpsSgHistTableSize_Object = MibScalar
cisgIpsSgHistTableSize = _CisgIpsSgHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 1, 1, 1),
    _CisgIpsSgHistTableSize_Type()
)
cisgIpsSgHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisgIpsSgHistTableSize.setStatus("current")
_CisgIpsSgTunnelHistTable_Object = MibTable
cisgIpsSgTunnelHistTable = _CisgIpsSgTunnelHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cisgIpsSgTunnelHistTable.setStatus("current")
_CisgIpsSgTunnelHistEntry_Object = MibTableRow
cisgIpsSgTunnelHistEntry = _CisgIpsSgTunnelHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1)
)
cisgIpsSgTunnelHistEntry.setIndexNames(
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"),
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistIndex"),
)
if mibBuilder.loadTexts:
    cisgIpsSgTunnelHistEntry.setStatus("current")
_CisgIpsSgTunHistIndex_Type = Unsigned32
_CisgIpsSgTunHistIndex_Object = MibTableColumn
cisgIpsSgTunHistIndex = _CisgIpsSgTunHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 1),
    _CisgIpsSgTunHistIndex_Type()
)
cisgIpsSgTunHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistIndex.setStatus("current")


class _CisgIpsSgTunHistTermReason_Type(Integer32):
    """Custom type cisgIpsSgTunHistTermReason based on Integer32"""
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
        *(("applicationInitiated", 6),
          ("localFailure", 8),
          ("normal", 2),
          ("operRequest", 3),
          ("other", 1),
          ("peerDelRequest", 4),
          ("peerLost", 5),
          ("userAuthFailure", 7))
    )


_CisgIpsSgTunHistTermReason_Type.__name__ = "Integer32"
_CisgIpsSgTunHistTermReason_Object = MibTableColumn
cisgIpsSgTunHistTermReason = _CisgIpsSgTunHistTermReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 2),
    _CisgIpsSgTunHistTermReason_Type()
)
cisgIpsSgTunHistTermReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistTermReason.setStatus("current")
_CisgIpsSgTunHistActiveIndex_Type = CIPsecPhase1TunnelIndex
_CisgIpsSgTunHistActiveIndex_Object = MibTableColumn
cisgIpsSgTunHistActiveIndex = _CisgIpsSgTunHistActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 3),
    _CisgIpsSgTunHistActiveIndex_Type()
)
cisgIpsSgTunHistActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistActiveIndex.setStatus("current")
_CisgIpsSgTunHistPeerLocalType_Type = CIPsecPhase1PeerIdentityType
_CisgIpsSgTunHistPeerLocalType_Object = MibTableColumn
cisgIpsSgTunHistPeerLocalType = _CisgIpsSgTunHistPeerLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 4),
    _CisgIpsSgTunHistPeerLocalType_Type()
)
cisgIpsSgTunHistPeerLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistPeerLocalType.setStatus("current")


class _CisgIpsSgTunHistPeerLocalValue_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunHistPeerLocalValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CisgIpsSgTunHistPeerLocalValue_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunHistPeerLocalValue_Object = MibTableColumn
cisgIpsSgTunHistPeerLocalValue = _CisgIpsSgTunHistPeerLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 5),
    _CisgIpsSgTunHistPeerLocalValue_Type()
)
cisgIpsSgTunHistPeerLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistPeerLocalValue.setStatus("current")


class _CisgIpsSgTunHistPeerIntIndex_Type(Unsigned32):
    """Custom type cisgIpsSgTunHistPeerIntIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CisgIpsSgTunHistPeerIntIndex_Type.__name__ = "Unsigned32"
_CisgIpsSgTunHistPeerIntIndex_Object = MibTableColumn
cisgIpsSgTunHistPeerIntIndex = _CisgIpsSgTunHistPeerIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 6),
    _CisgIpsSgTunHistPeerIntIndex_Type()
)
cisgIpsSgTunHistPeerIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistPeerIntIndex.setStatus("current")
_CisgIpsSgTunHistPeerRemoteType_Type = CIPsecPhase1PeerIdentityType
_CisgIpsSgTunHistPeerRemoteType_Object = MibTableColumn
cisgIpsSgTunHistPeerRemoteType = _CisgIpsSgTunHistPeerRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 7),
    _CisgIpsSgTunHistPeerRemoteType_Type()
)
cisgIpsSgTunHistPeerRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistPeerRemoteType.setStatus("current")


class _CisgIpsSgTunHistPeerRemoteValue_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunHistPeerRemoteValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CisgIpsSgTunHistPeerRemoteValue_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunHistPeerRemoteValue_Object = MibTableColumn
cisgIpsSgTunHistPeerRemoteValue = _CisgIpsSgTunHistPeerRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 8),
    _CisgIpsSgTunHistPeerRemoteValue_Type()
)
cisgIpsSgTunHistPeerRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistPeerRemoteValue.setStatus("current")
_CisgIpsSgTunHistLocalAddrType_Type = CIPsecPhase1PeerIdentityType
_CisgIpsSgTunHistLocalAddrType_Object = MibTableColumn
cisgIpsSgTunHistLocalAddrType = _CisgIpsSgTunHistLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 9),
    _CisgIpsSgTunHistLocalAddrType_Type()
)
cisgIpsSgTunHistLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistLocalAddrType.setStatus("current")


class _CisgIpsSgTunHistLocalAddr_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunHistLocalAddr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CisgIpsSgTunHistLocalAddr_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunHistLocalAddr_Object = MibTableColumn
cisgIpsSgTunHistLocalAddr = _CisgIpsSgTunHistLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 10),
    _CisgIpsSgTunHistLocalAddr_Type()
)
cisgIpsSgTunHistLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistLocalAddr.setStatus("current")


class _CisgIpsSgTunHistLocalName_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunHistLocalName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CisgIpsSgTunHistLocalName_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunHistLocalName_Object = MibTableColumn
cisgIpsSgTunHistLocalName = _CisgIpsSgTunHistLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 11),
    _CisgIpsSgTunHistLocalName_Type()
)
cisgIpsSgTunHistLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistLocalName.setStatus("current")
_CisgIpsSgTunHistRemoteAddrType_Type = CIPsecPhase1PeerIdentityType
_CisgIpsSgTunHistRemoteAddrType_Object = MibTableColumn
cisgIpsSgTunHistRemoteAddrType = _CisgIpsSgTunHistRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 12),
    _CisgIpsSgTunHistRemoteAddrType_Type()
)
cisgIpsSgTunHistRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistRemoteAddrType.setStatus("current")


class _CisgIpsSgTunHistRemoteAddr_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunHistRemoteAddr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CisgIpsSgTunHistRemoteAddr_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunHistRemoteAddr_Object = MibTableColumn
cisgIpsSgTunHistRemoteAddr = _CisgIpsSgTunHistRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 13),
    _CisgIpsSgTunHistRemoteAddr_Type()
)
cisgIpsSgTunHistRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistRemoteAddr.setStatus("current")


class _CisgIpsSgTunHistRemoteName_Type(SnmpAdminString):
    """Custom type cisgIpsSgTunHistRemoteName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CisgIpsSgTunHistRemoteName_Type.__name__ = "SnmpAdminString"
_CisgIpsSgTunHistRemoteName_Object = MibTableColumn
cisgIpsSgTunHistRemoteName = _CisgIpsSgTunHistRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 14),
    _CisgIpsSgTunHistRemoteName_Type()
)
cisgIpsSgTunHistRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistRemoteName.setStatus("current")
_CisgIpsSgTunHistEncryptAlgo_Type = CIPsecEncryptAlgorithm
_CisgIpsSgTunHistEncryptAlgo_Object = MibTableColumn
cisgIpsSgTunHistEncryptAlgo = _CisgIpsSgTunHistEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 15),
    _CisgIpsSgTunHistEncryptAlgo_Type()
)
cisgIpsSgTunHistEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistEncryptAlgo.setStatus("current")
_CisgIpsSgTunHistEncryptKeySize_Type = CIPsecEncryptionKeySize
_CisgIpsSgTunHistEncryptKeySize_Object = MibTableColumn
cisgIpsSgTunHistEncryptKeySize = _CisgIpsSgTunHistEncryptKeySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 16),
    _CisgIpsSgTunHistEncryptKeySize_Type()
)
cisgIpsSgTunHistEncryptKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistEncryptKeySize.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistEncryptKeySize.setUnits("Bits")
_CisgIpsSgTunHistHashAlgo_Type = CIPsecIkeHashAlgorithm
_CisgIpsSgTunHistHashAlgo_Object = MibTableColumn
cisgIpsSgTunHistHashAlgo = _CisgIpsSgTunHistHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 17),
    _CisgIpsSgTunHistHashAlgo_Type()
)
cisgIpsSgTunHistHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistHashAlgo.setStatus("current")
_CisgIpsSgTunHistAuthMethod_Type = CIPsecIkeAuthMethod
_CisgIpsSgTunHistAuthMethod_Object = MibTableColumn
cisgIpsSgTunHistAuthMethod = _CisgIpsSgTunHistAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 18),
    _CisgIpsSgTunHistAuthMethod_Type()
)
cisgIpsSgTunHistAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistAuthMethod.setStatus("current")


class _CisgIpsSgTunHistLifeTime_Type(Unsigned32):
    """Custom type cisgIpsSgTunHistLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CisgIpsSgTunHistLifeTime_Type.__name__ = "Unsigned32"
_CisgIpsSgTunHistLifeTime_Object = MibTableColumn
cisgIpsSgTunHistLifeTime = _CisgIpsSgTunHistLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 19),
    _CisgIpsSgTunHistLifeTime_Type()
)
cisgIpsSgTunHistLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistLifeTime.setStatus("current")
_CisgIpsSgTunHistStartTime_Type = TimeStamp
_CisgIpsSgTunHistStartTime_Object = MibTableColumn
cisgIpsSgTunHistStartTime = _CisgIpsSgTunHistStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 20),
    _CisgIpsSgTunHistStartTime_Type()
)
cisgIpsSgTunHistStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistStartTime.setStatus("current")
_CisgIpsSgTunHistActiveTime_Type = TimeInterval
_CisgIpsSgTunHistActiveTime_Object = MibTableColumn
cisgIpsSgTunHistActiveTime = _CisgIpsSgTunHistActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 21),
    _CisgIpsSgTunHistActiveTime_Type()
)
cisgIpsSgTunHistActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistActiveTime.setStatus("current")
_CisgIpsSgTunHistInOctets_Type = Counter64
_CisgIpsSgTunHistInOctets_Object = MibTableColumn
cisgIpsSgTunHistInOctets = _CisgIpsSgTunHistInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 22),
    _CisgIpsSgTunHistInOctets_Type()
)
cisgIpsSgTunHistInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistInOctets.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistInOctets.setUnits("Octets")
_CisgIpsSgTunHistInPkts_Type = Counter64
_CisgIpsSgTunHistInPkts_Object = MibTableColumn
cisgIpsSgTunHistInPkts = _CisgIpsSgTunHistInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 23),
    _CisgIpsSgTunHistInPkts_Type()
)
cisgIpsSgTunHistInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistInPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistInPkts.setUnits("Packets")
_CisgIpsSgTunHistInDropPkts_Type = Counter64
_CisgIpsSgTunHistInDropPkts_Object = MibTableColumn
cisgIpsSgTunHistInDropPkts = _CisgIpsSgTunHistInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 24),
    _CisgIpsSgTunHistInDropPkts_Type()
)
cisgIpsSgTunHistInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistInDropPkts.setUnits("Packets")
_CisgIpsSgTunHistInNotifys_Type = Counter64
_CisgIpsSgTunHistInNotifys_Object = MibTableColumn
cisgIpsSgTunHistInNotifys = _CisgIpsSgTunHistInNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 25),
    _CisgIpsSgTunHistInNotifys_Type()
)
cisgIpsSgTunHistInNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistInNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistInNotifys.setUnits("Notification Payloads")
_CisgIpsSgTunHistInP2SaDelReqs_Type = Counter64
_CisgIpsSgTunHistInP2SaDelReqs_Object = MibTableColumn
cisgIpsSgTunHistInP2SaDelReqs = _CisgIpsSgTunHistInP2SaDelReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 26),
    _CisgIpsSgTunHistInP2SaDelReqs_Type()
)
cisgIpsSgTunHistInP2SaDelReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistInP2SaDelReqs.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistInP2SaDelReqs.setUnits("Notification Payloads")
_CisgIpsSgTunHistOutOctets_Type = Counter64
_CisgIpsSgTunHistOutOctets_Object = MibTableColumn
cisgIpsSgTunHistOutOctets = _CisgIpsSgTunHistOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 27),
    _CisgIpsSgTunHistOutOctets_Type()
)
cisgIpsSgTunHistOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistOutOctets.setUnits("Octets")
_CisgIpsSgTunHistOutPkts_Type = Counter64
_CisgIpsSgTunHistOutPkts_Object = MibTableColumn
cisgIpsSgTunHistOutPkts = _CisgIpsSgTunHistOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 28),
    _CisgIpsSgTunHistOutPkts_Type()
)
cisgIpsSgTunHistOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistOutPkts.setUnits("Packets")
_CisgIpsSgTunHistOutDropPkts_Type = Counter64
_CisgIpsSgTunHistOutDropPkts_Object = MibTableColumn
cisgIpsSgTunHistOutDropPkts = _CisgIpsSgTunHistOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 29),
    _CisgIpsSgTunHistOutDropPkts_Type()
)
cisgIpsSgTunHistOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistOutDropPkts.setUnits("Packets")
_CisgIpsSgTunHistOutNotifys_Type = Counter64
_CisgIpsSgTunHistOutNotifys_Object = MibTableColumn
cisgIpsSgTunHistOutNotifys = _CisgIpsSgTunHistOutNotifys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 30),
    _CisgIpsSgTunHistOutNotifys_Type()
)
cisgIpsSgTunHistOutNotifys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistOutNotifys.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistOutNotifys.setUnits("Notification Payloads")
_CisgIpsSgTunHistOutP2SaDelReqs_Type = Counter64
_CisgIpsSgTunHistOutP2SaDelReqs_Object = MibTableColumn
cisgIpsSgTunHistOutP2SaDelReqs = _CisgIpsSgTunHistOutP2SaDelReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 3, 2, 1, 31),
    _CisgIpsSgTunHistOutP2SaDelReqs_Type()
)
cisgIpsSgTunHistOutP2SaDelReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistOutP2SaDelReqs.setStatus("current")
if mibBuilder.loadTexts:
    cisgIpsSgTunHistOutP2SaDelReqs.setUnits("Notification Payloads")
_CisgIpsSgFailures_ObjectIdentity = ObjectIdentity
cisgIpsSgFailures = _CisgIpsSgFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4)
)
_CisgIpsSgFailGlobal_ObjectIdentity = ObjectIdentity
cisgIpsSgFailGlobal = _CisgIpsSgFailGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 1)
)
_CisgIpsSgFailGlobalCntl_ObjectIdentity = ObjectIdentity
cisgIpsSgFailGlobalCntl = _CisgIpsSgFailGlobalCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 1, 1)
)


class _CisgIpsSgFailTableSize_Type(Unsigned32):
    """Custom type cisgIpsSgFailTableSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CisgIpsSgFailTableSize_Type.__name__ = "Unsigned32"
_CisgIpsSgFailTableSize_Object = MibScalar
cisgIpsSgFailTableSize = _CisgIpsSgFailTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 1, 1, 1),
    _CisgIpsSgFailTableSize_Type()
)
cisgIpsSgFailTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisgIpsSgFailTableSize.setStatus("current")
_CisgIpsSgFailTable_Object = MibTable
cisgIpsSgFailTable = _CisgIpsSgFailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cisgIpsSgFailTable.setStatus("current")
_CisgIpsSgFailEntry_Object = MibTableRow
cisgIpsSgFailEntry = _CisgIpsSgFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 2, 1)
)
cisgIpsSgFailEntry.setIndexNames(
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgProtocol"),
    (0, "CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailIndex"),
)
if mibBuilder.loadTexts:
    cisgIpsSgFailEntry.setStatus("current")
_CisgIpsSgFailIndex_Type = Unsigned32
_CisgIpsSgFailIndex_Object = MibTableColumn
cisgIpsSgFailIndex = _CisgIpsSgFailIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 2, 1, 1),
    _CisgIpsSgFailIndex_Type()
)
cisgIpsSgFailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cisgIpsSgFailIndex.setStatus("current")


class _CisgIpsSgFailReason_Type(Integer32):
    """Custom type cisgIpsSgFailReason based on Integer32"""
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
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("authFailure", 5),
          ("crlFailure", 14),
          ("deniedByAdmissionControl", 19),
          ("encryptFailure", 7),
          ("hashValidation", 6),
          ("internalError", 8),
          ("localCertExpired", 13),
          ("localFailure", 4),
          ("nonExistentSa", 16),
          ("operRequest", 18),
          ("other", 1),
          ("peerCertNotValid", 12),
          ("peerCertUnavailable", 11),
          ("peerDelRequest", 2),
          ("peerEncodingError", 15),
          ("peerLost", 3),
          ("proposalFailure", 10),
          ("protocolSpecific", 20),
          ("sysCapExceeded", 9),
          ("userAuthFailure", 17))
    )


_CisgIpsSgFailReason_Type.__name__ = "Integer32"
_CisgIpsSgFailReason_Object = MibTableColumn
cisgIpsSgFailReason = _CisgIpsSgFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 2, 1, 2),
    _CisgIpsSgFailReason_Type()
)
cisgIpsSgFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgFailReason.setStatus("current")
_CisgIpsSgFailTime_Type = TimeStamp
_CisgIpsSgFailTime_Object = MibTableColumn
cisgIpsSgFailTime = _CisgIpsSgFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 2, 1, 3),
    _CisgIpsSgFailTime_Type()
)
cisgIpsSgFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgFailTime.setStatus("current")
_CisgIpsSgFailLocalType_Type = CIPsecPhase1PeerIdentityType
_CisgIpsSgFailLocalType_Object = MibTableColumn
cisgIpsSgFailLocalType = _CisgIpsSgFailLocalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 2, 1, 4),
    _CisgIpsSgFailLocalType_Type()
)
cisgIpsSgFailLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgFailLocalType.setStatus("current")


class _CisgIpsSgFailLocalValue_Type(SnmpAdminString):
    """Custom type cisgIpsSgFailLocalValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CisgIpsSgFailLocalValue_Type.__name__ = "SnmpAdminString"
_CisgIpsSgFailLocalValue_Object = MibTableColumn
cisgIpsSgFailLocalValue = _CisgIpsSgFailLocalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 2, 1, 5),
    _CisgIpsSgFailLocalValue_Type()
)
cisgIpsSgFailLocalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgFailLocalValue.setStatus("current")
_CisgIpsSgFailRemoteType_Type = CIPsecPhase1PeerIdentityType
_CisgIpsSgFailRemoteType_Object = MibTableColumn
cisgIpsSgFailRemoteType = _CisgIpsSgFailRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 2, 1, 6),
    _CisgIpsSgFailRemoteType_Type()
)
cisgIpsSgFailRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgFailRemoteType.setStatus("current")


class _CisgIpsSgFailRemoteValue_Type(SnmpAdminString):
    """Custom type cisgIpsSgFailRemoteValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CisgIpsSgFailRemoteValue_Type.__name__ = "SnmpAdminString"
_CisgIpsSgFailRemoteValue_Object = MibTableColumn
cisgIpsSgFailRemoteValue = _CisgIpsSgFailRemoteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 2, 1, 7),
    _CisgIpsSgFailRemoteValue_Type()
)
cisgIpsSgFailRemoteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgFailRemoteValue.setStatus("current")


class _CisgIpsSgFailLocalAddress_Type(SnmpAdminString):
    """Custom type cisgIpsSgFailLocalAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CisgIpsSgFailLocalAddress_Type.__name__ = "SnmpAdminString"
_CisgIpsSgFailLocalAddress_Object = MibTableColumn
cisgIpsSgFailLocalAddress = _CisgIpsSgFailLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 2, 1, 8),
    _CisgIpsSgFailLocalAddress_Type()
)
cisgIpsSgFailLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgFailLocalAddress.setStatus("current")


class _CisgIpsSgFailRemoteAddress_Type(SnmpAdminString):
    """Custom type cisgIpsSgFailRemoteAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CisgIpsSgFailRemoteAddress_Type.__name__ = "SnmpAdminString"
_CisgIpsSgFailRemoteAddress_Object = MibTableColumn
cisgIpsSgFailRemoteAddress = _CisgIpsSgFailRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 4, 2, 1, 9),
    _CisgIpsSgFailRemoteAddress_Type()
)
cisgIpsSgFailRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cisgIpsSgFailRemoteAddress.setStatus("current")
_CisgIpsSgNotificationCntl_ObjectIdentity = ObjectIdentity
cisgIpsSgNotificationCntl = _CisgIpsSgNotificationCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 5)
)


class _CisgIpsSgNotifCntlAllNotifs_Type(TruthValue):
    """Custom type cisgIpsSgNotifCntlAllNotifs based on TruthValue"""


_CisgIpsSgNotifCntlAllNotifs_Object = MibScalar
cisgIpsSgNotifCntlAllNotifs = _CisgIpsSgNotifCntlAllNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 5, 1),
    _CisgIpsSgNotifCntlAllNotifs_Type()
)
cisgIpsSgNotifCntlAllNotifs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisgIpsSgNotifCntlAllNotifs.setStatus("current")


class _CisgIpsSgNotifCntlTunnelStart_Type(TruthValue):
    """Custom type cisgIpsSgNotifCntlTunnelStart based on TruthValue"""


_CisgIpsSgNotifCntlTunnelStart_Object = MibScalar
cisgIpsSgNotifCntlTunnelStart = _CisgIpsSgNotifCntlTunnelStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 5, 2),
    _CisgIpsSgNotifCntlTunnelStart_Type()
)
cisgIpsSgNotifCntlTunnelStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisgIpsSgNotifCntlTunnelStart.setStatus("current")


class _CisgIpsSgNotifCntlTunnelStop_Type(TruthValue):
    """Custom type cisgIpsSgNotifCntlTunnelStop based on TruthValue"""


_CisgIpsSgNotifCntlTunnelStop_Object = MibScalar
cisgIpsSgNotifCntlTunnelStop = _CisgIpsSgNotifCntlTunnelStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 5, 3),
    _CisgIpsSgNotifCntlTunnelStop_Type()
)
cisgIpsSgNotifCntlTunnelStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisgIpsSgNotifCntlTunnelStop.setStatus("current")


class _CisgIpsSgNotifCntlSysFailure_Type(TruthValue):
    """Custom type cisgIpsSgNotifCntlSysFailure based on TruthValue"""


_CisgIpsSgNotifCntlSysFailure_Object = MibScalar
cisgIpsSgNotifCntlSysFailure = _CisgIpsSgNotifCntlSysFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 5, 4),
    _CisgIpsSgNotifCntlSysFailure_Type()
)
cisgIpsSgNotifCntlSysFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisgIpsSgNotifCntlSysFailure.setStatus("current")


class _CisgIpsSgNotifCntlCertCrlFail_Type(TruthValue):
    """Custom type cisgIpsSgNotifCntlCertCrlFail based on TruthValue"""


_CisgIpsSgNotifCntlCertCrlFail_Object = MibScalar
cisgIpsSgNotifCntlCertCrlFail = _CisgIpsSgNotifCntlCertCrlFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 1, 5, 5),
    _CisgIpsSgNotifCntlCertCrlFail_Type()
)
cisgIpsSgNotifCntlCertCrlFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cisgIpsSgNotifCntlCertCrlFail.setStatus("current")
_CiscoIPsecSigMIBConform_ObjectIdentity = ObjectIdentity
ciscoIPsecSigMIBConform = _CiscoIPsecSigMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 2)
)
_CiscoIpsSgMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpsSgMIBCompliances = _CiscoIpsSgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 2, 1)
)
_CiscoIpsSgMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpsSgMIBGroups = _CiscoIpsSgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 2, 2)
)

# Managed Objects groups

ciscoIpsSgActivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 2, 2, 1)
)
ciscoIpsSgActivityGroup.setObjects(
      *(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalActiveTunnels"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalPreviousTunnels"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalInOctets"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalInPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalInDropPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalInNotifys"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalInP2SaDelReqs"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalOutOctets"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalOutPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalOutDropPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalOutNotifys"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalOutP2SaDelReqs"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalInitTunnels"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalInitTunnelFails"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalRespTunnels"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalRespTunnelFails"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalSysCapFails"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalAuthFails"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalDecryptFails"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalHashValidFails"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalBadTunnelRefs"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalInP1SaDelReqs"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgGlobalOutP1SaDelReqs"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunLocalType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunLocalValue"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunLocalAddressType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunLocalAddress"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunLocalName"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunRemoteType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunRemoteValue"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunRemoteAddressType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunRemoteAddress"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunRemoteName"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunEncryptAlgo"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunEncryptKeySize"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHashAlgo"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunAuthMethod"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunLifeTime"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunActiveTime"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunInOctets"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunInPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunInDropPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunInNotifys"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunOutOctets"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunOutPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunOutDropPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunOutNotifys"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunOutP2SaDelReqs"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunStatus"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunAction"))
)
if mibBuilder.loadTexts:
    ciscoIpsSgActivityGroup.setStatus("current")

ciscoIpsSgCoreHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 2, 2, 2)
)
ciscoIpsSgCoreHistoryGroup.setObjects(
    ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgHistTableSize")
)
if mibBuilder.loadTexts:
    ciscoIpsSgCoreHistoryGroup.setStatus("current")

ciscoIpsSgHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 2, 2, 3)
)
ciscoIpsSgHistoryGroup.setObjects(
      *(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistTermReason"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistActiveIndex"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistPeerLocalType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistPeerLocalValue"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistPeerIntIndex"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistPeerRemoteType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistPeerRemoteValue"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistLocalAddrType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistLocalAddr"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistLocalName"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistRemoteAddrType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistRemoteAddr"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistRemoteName"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistEncryptAlgo"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistEncryptKeySize"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistHashAlgo"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistAuthMethod"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistLifeTime"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistStartTime"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistActiveTime"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistInOctets"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistInPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistInDropPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistInNotifys"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistInP2SaDelReqs"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistOutOctets"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistOutPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistOutDropPkts"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistOutNotifys"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistOutP2SaDelReqs"))
)
if mibBuilder.loadTexts:
    ciscoIpsSgHistoryGroup.setStatus("current")

ciscoIpsSgCoreFailureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 2, 2, 4)
)
ciscoIpsSgCoreFailureGroup.setObjects(
    ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailTableSize")
)
if mibBuilder.loadTexts:
    ciscoIpsSgCoreFailureGroup.setStatus("current")

ciscoIpsSgFailureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 2, 2, 5)
)
ciscoIpsSgFailureGroup.setObjects(
      *(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailReason"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailTime"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailLocalType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailLocalValue"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailRemoteType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailRemoteValue"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailLocalAddress"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailRemoteAddress"))
)
if mibBuilder.loadTexts:
    ciscoIpsSgFailureGroup.setStatus("current")

ciscoIpsSgNotifCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 2, 2, 6)
)
ciscoIpsSgNotifCntlGroup.setObjects(
      *(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgNotifCntlAllNotifs"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgNotifCntlTunnelStart"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgNotifCntlTunnelStop"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgNotifCntlSysFailure"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgNotifCntlCertCrlFail"))
)
if mibBuilder.loadTexts:
    ciscoIpsSgNotifCntlGroup.setStatus("current")


# Notification objects

ciscoIpsSgTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 0, 1)
)
ciscoIpsSgTunnelStart.setObjects(
      *(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunLocalAddressType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunLocalAddress"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunRemoteAddressType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunRemoteAddress"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunLifeTime"))
)
if mibBuilder.loadTexts:
    ciscoIpsSgTunnelStart.setStatus(
        "current"
    )

ciscoIpsSgTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 0, 2)
)
ciscoIpsSgTunnelStop.setObjects(
      *(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistLocalAddrType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistLocalAddr"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistRemoteAddrType"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistRemoteAddr"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistTermReason"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgTunHistActiveTime"))
)
if mibBuilder.loadTexts:
    ciscoIpsSgTunnelStop.setStatus(
        "current"
    )

ciscoIpsSgSysFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 0, 3)
)
ciscoIpsSgSysFailure.setObjects(
      *(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailLocalAddress"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailRemoteAddress"))
)
if mibBuilder.loadTexts:
    ciscoIpsSgSysFailure.setStatus(
        "current"
    )

ciscoIpsSgCertCrlFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 0, 4)
)
ciscoIpsSgCertCrlFailure.setObjects(
      *(("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailLocalAddress"),
        ("CISCO-IPSEC-SIGNALING-MIB", "cisgIpsSgFailRemoteAddress"))
)
if mibBuilder.loadTexts:
    ciscoIpsSgCertCrlFailure.setStatus(
        "current"
    )


# Notifications groups

ciscoIpsSgNotifcationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 2, 2, 7)
)
ciscoIpsSgNotifcationGroup.setObjects(
      *(("CISCO-IPSEC-SIGNALING-MIB", "ciscoIpsSgTunnelStart"),
        ("CISCO-IPSEC-SIGNALING-MIB", "ciscoIpsSgTunnelStop"),
        ("CISCO-IPSEC-SIGNALING-MIB", "ciscoIpsSgSysFailure"),
        ("CISCO-IPSEC-SIGNALING-MIB", "ciscoIpsSgCertCrlFailure"))
)
if mibBuilder.loadTexts:
    ciscoIpsSgNotifcationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIpsSgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 438, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpsSgMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSEC-SIGNALING-MIB",
    **{"ciscoIPsecSignalingMIB": ciscoIPsecSignalingMIB,
       "ciscoIPsecSigMIBNotifs": ciscoIPsecSigMIBNotifs,
       "ciscoIpsSgTunnelStart": ciscoIpsSgTunnelStart,
       "ciscoIpsSgTunnelStop": ciscoIpsSgTunnelStop,
       "ciscoIpsSgSysFailure": ciscoIpsSgSysFailure,
       "ciscoIpsSgCertCrlFailure": ciscoIpsSgCertCrlFailure,
       "ciscoIPsecSigMIBObjects": ciscoIPsecSigMIBObjects,
       "cisgIpsSgCurrentActivity": cisgIpsSgCurrentActivity,
       "cisgIpsSgGlobalStatsTable": cisgIpsSgGlobalStatsTable,
       "cisgIpsSgGlobalStatsEntry": cisgIpsSgGlobalStatsEntry,
       "cisgIpsSgProtocol": cisgIpsSgProtocol,
       "cisgIpsSgGlobalActiveTunnels": cisgIpsSgGlobalActiveTunnels,
       "cisgIpsSgGlobalPreviousTunnels": cisgIpsSgGlobalPreviousTunnels,
       "cisgIpsSgGlobalInOctets": cisgIpsSgGlobalInOctets,
       "cisgIpsSgGlobalInPkts": cisgIpsSgGlobalInPkts,
       "cisgIpsSgGlobalInDropPkts": cisgIpsSgGlobalInDropPkts,
       "cisgIpsSgGlobalInNotifys": cisgIpsSgGlobalInNotifys,
       "cisgIpsSgGlobalInP2SaDelReqs": cisgIpsSgGlobalInP2SaDelReqs,
       "cisgIpsSgGlobalOutOctets": cisgIpsSgGlobalOutOctets,
       "cisgIpsSgGlobalOutPkts": cisgIpsSgGlobalOutPkts,
       "cisgIpsSgGlobalOutDropPkts": cisgIpsSgGlobalOutDropPkts,
       "cisgIpsSgGlobalOutNotifys": cisgIpsSgGlobalOutNotifys,
       "cisgIpsSgGlobalOutP2SaDelReqs": cisgIpsSgGlobalOutP2SaDelReqs,
       "cisgIpsSgGlobalInitTunnels": cisgIpsSgGlobalInitTunnels,
       "cisgIpsSgGlobalInitTunnelFails": cisgIpsSgGlobalInitTunnelFails,
       "cisgIpsSgGlobalRespTunnels": cisgIpsSgGlobalRespTunnels,
       "cisgIpsSgGlobalRespTunnelFails": cisgIpsSgGlobalRespTunnelFails,
       "cisgIpsSgGlobalSysCapFails": cisgIpsSgGlobalSysCapFails,
       "cisgIpsSgGlobalAuthFails": cisgIpsSgGlobalAuthFails,
       "cisgIpsSgGlobalDecryptFails": cisgIpsSgGlobalDecryptFails,
       "cisgIpsSgGlobalHashValidFails": cisgIpsSgGlobalHashValidFails,
       "cisgIpsSgGlobalBadTunnelRefs": cisgIpsSgGlobalBadTunnelRefs,
       "cisgIpsSgGlobalInP1SaDelReqs": cisgIpsSgGlobalInP1SaDelReqs,
       "cisgIpsSgGlobalOutP1SaDelReqs": cisgIpsSgGlobalOutP1SaDelReqs,
       "cisgIpsSgTunnelTable": cisgIpsSgTunnelTable,
       "cisgIpsSgTunnelEntry": cisgIpsSgTunnelEntry,
       "cisgIpsSgTunIndex": cisgIpsSgTunIndex,
       "cisgIpsSgTunLocalType": cisgIpsSgTunLocalType,
       "cisgIpsSgTunLocalValue": cisgIpsSgTunLocalValue,
       "cisgIpsSgTunLocalAddressType": cisgIpsSgTunLocalAddressType,
       "cisgIpsSgTunLocalAddress": cisgIpsSgTunLocalAddress,
       "cisgIpsSgTunLocalName": cisgIpsSgTunLocalName,
       "cisgIpsSgTunRemoteType": cisgIpsSgTunRemoteType,
       "cisgIpsSgTunRemoteValue": cisgIpsSgTunRemoteValue,
       "cisgIpsSgTunRemoteAddressType": cisgIpsSgTunRemoteAddressType,
       "cisgIpsSgTunRemoteAddress": cisgIpsSgTunRemoteAddress,
       "cisgIpsSgTunRemoteName": cisgIpsSgTunRemoteName,
       "cisgIpsSgTunEncryptAlgo": cisgIpsSgTunEncryptAlgo,
       "cisgIpsSgTunEncryptKeySize": cisgIpsSgTunEncryptKeySize,
       "cisgIpsSgTunHashAlgo": cisgIpsSgTunHashAlgo,
       "cisgIpsSgTunAuthMethod": cisgIpsSgTunAuthMethod,
       "cisgIpsSgTunLifeTime": cisgIpsSgTunLifeTime,
       "cisgIpsSgTunActiveTime": cisgIpsSgTunActiveTime,
       "cisgIpsSgTunInOctets": cisgIpsSgTunInOctets,
       "cisgIpsSgTunInPkts": cisgIpsSgTunInPkts,
       "cisgIpsSgTunInDropPkts": cisgIpsSgTunInDropPkts,
       "cisgIpsSgTunInNotifys": cisgIpsSgTunInNotifys,
       "cisgIpsSgTunOutOctets": cisgIpsSgTunOutOctets,
       "cisgIpsSgTunOutPkts": cisgIpsSgTunOutPkts,
       "cisgIpsSgTunOutDropPkts": cisgIpsSgTunOutDropPkts,
       "cisgIpsSgTunOutNotifys": cisgIpsSgTunOutNotifys,
       "cisgIpsSgTunOutP2SaDelReqs": cisgIpsSgTunOutP2SaDelReqs,
       "cisgIpsSgTunStatus": cisgIpsSgTunStatus,
       "cisgIpsSgTunAction": cisgIpsSgTunAction,
       "cisgIpsSgPeerAssociations": cisgIpsSgPeerAssociations,
       "cisgIpsSgHistory": cisgIpsSgHistory,
       "cisgIpsSgHistGlobal": cisgIpsSgHistGlobal,
       "cisgIpsSgHistGlobalCntl": cisgIpsSgHistGlobalCntl,
       "cisgIpsSgHistTableSize": cisgIpsSgHistTableSize,
       "cisgIpsSgTunnelHistTable": cisgIpsSgTunnelHistTable,
       "cisgIpsSgTunnelHistEntry": cisgIpsSgTunnelHistEntry,
       "cisgIpsSgTunHistIndex": cisgIpsSgTunHistIndex,
       "cisgIpsSgTunHistTermReason": cisgIpsSgTunHistTermReason,
       "cisgIpsSgTunHistActiveIndex": cisgIpsSgTunHistActiveIndex,
       "cisgIpsSgTunHistPeerLocalType": cisgIpsSgTunHistPeerLocalType,
       "cisgIpsSgTunHistPeerLocalValue": cisgIpsSgTunHistPeerLocalValue,
       "cisgIpsSgTunHistPeerIntIndex": cisgIpsSgTunHistPeerIntIndex,
       "cisgIpsSgTunHistPeerRemoteType": cisgIpsSgTunHistPeerRemoteType,
       "cisgIpsSgTunHistPeerRemoteValue": cisgIpsSgTunHistPeerRemoteValue,
       "cisgIpsSgTunHistLocalAddrType": cisgIpsSgTunHistLocalAddrType,
       "cisgIpsSgTunHistLocalAddr": cisgIpsSgTunHistLocalAddr,
       "cisgIpsSgTunHistLocalName": cisgIpsSgTunHistLocalName,
       "cisgIpsSgTunHistRemoteAddrType": cisgIpsSgTunHistRemoteAddrType,
       "cisgIpsSgTunHistRemoteAddr": cisgIpsSgTunHistRemoteAddr,
       "cisgIpsSgTunHistRemoteName": cisgIpsSgTunHistRemoteName,
       "cisgIpsSgTunHistEncryptAlgo": cisgIpsSgTunHistEncryptAlgo,
       "cisgIpsSgTunHistEncryptKeySize": cisgIpsSgTunHistEncryptKeySize,
       "cisgIpsSgTunHistHashAlgo": cisgIpsSgTunHistHashAlgo,
       "cisgIpsSgTunHistAuthMethod": cisgIpsSgTunHistAuthMethod,
       "cisgIpsSgTunHistLifeTime": cisgIpsSgTunHistLifeTime,
       "cisgIpsSgTunHistStartTime": cisgIpsSgTunHistStartTime,
       "cisgIpsSgTunHistActiveTime": cisgIpsSgTunHistActiveTime,
       "cisgIpsSgTunHistInOctets": cisgIpsSgTunHistInOctets,
       "cisgIpsSgTunHistInPkts": cisgIpsSgTunHistInPkts,
       "cisgIpsSgTunHistInDropPkts": cisgIpsSgTunHistInDropPkts,
       "cisgIpsSgTunHistInNotifys": cisgIpsSgTunHistInNotifys,
       "cisgIpsSgTunHistInP2SaDelReqs": cisgIpsSgTunHistInP2SaDelReqs,
       "cisgIpsSgTunHistOutOctets": cisgIpsSgTunHistOutOctets,
       "cisgIpsSgTunHistOutPkts": cisgIpsSgTunHistOutPkts,
       "cisgIpsSgTunHistOutDropPkts": cisgIpsSgTunHistOutDropPkts,
       "cisgIpsSgTunHistOutNotifys": cisgIpsSgTunHistOutNotifys,
       "cisgIpsSgTunHistOutP2SaDelReqs": cisgIpsSgTunHistOutP2SaDelReqs,
       "cisgIpsSgFailures": cisgIpsSgFailures,
       "cisgIpsSgFailGlobal": cisgIpsSgFailGlobal,
       "cisgIpsSgFailGlobalCntl": cisgIpsSgFailGlobalCntl,
       "cisgIpsSgFailTableSize": cisgIpsSgFailTableSize,
       "cisgIpsSgFailTable": cisgIpsSgFailTable,
       "cisgIpsSgFailEntry": cisgIpsSgFailEntry,
       "cisgIpsSgFailIndex": cisgIpsSgFailIndex,
       "cisgIpsSgFailReason": cisgIpsSgFailReason,
       "cisgIpsSgFailTime": cisgIpsSgFailTime,
       "cisgIpsSgFailLocalType": cisgIpsSgFailLocalType,
       "cisgIpsSgFailLocalValue": cisgIpsSgFailLocalValue,
       "cisgIpsSgFailRemoteType": cisgIpsSgFailRemoteType,
       "cisgIpsSgFailRemoteValue": cisgIpsSgFailRemoteValue,
       "cisgIpsSgFailLocalAddress": cisgIpsSgFailLocalAddress,
       "cisgIpsSgFailRemoteAddress": cisgIpsSgFailRemoteAddress,
       "cisgIpsSgNotificationCntl": cisgIpsSgNotificationCntl,
       "cisgIpsSgNotifCntlAllNotifs": cisgIpsSgNotifCntlAllNotifs,
       "cisgIpsSgNotifCntlTunnelStart": cisgIpsSgNotifCntlTunnelStart,
       "cisgIpsSgNotifCntlTunnelStop": cisgIpsSgNotifCntlTunnelStop,
       "cisgIpsSgNotifCntlSysFailure": cisgIpsSgNotifCntlSysFailure,
       "cisgIpsSgNotifCntlCertCrlFail": cisgIpsSgNotifCntlCertCrlFail,
       "ciscoIPsecSigMIBConform": ciscoIPsecSigMIBConform,
       "ciscoIpsSgMIBCompliances": ciscoIpsSgMIBCompliances,
       "ciscoIpsSgMIBCompliance": ciscoIpsSgMIBCompliance,
       "ciscoIpsSgMIBGroups": ciscoIpsSgMIBGroups,
       "ciscoIpsSgActivityGroup": ciscoIpsSgActivityGroup,
       "ciscoIpsSgCoreHistoryGroup": ciscoIpsSgCoreHistoryGroup,
       "ciscoIpsSgHistoryGroup": ciscoIpsSgHistoryGroup,
       "ciscoIpsSgCoreFailureGroup": ciscoIpsSgCoreFailureGroup,
       "ciscoIpsSgFailureGroup": ciscoIpsSgFailureGroup,
       "ciscoIpsSgNotifCntlGroup": ciscoIpsSgNotifCntlGroup,
       "ciscoIpsSgNotifcationGroup": ciscoIpsSgNotifcationGroup}
)

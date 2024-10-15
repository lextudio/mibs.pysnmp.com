# SNMP MIB module (CISCO-SUBSCRIBER-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SUBSCRIBER-SESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:59 2024
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

(CbpElementName,) = mibBuilder.importSymbols(
    "CISCO-CBP-TC-MIB",
    "CbpElementName")

(DynamicTemplateName,) = mibBuilder.importSymbols(
    "CISCO-DYNAMIC-TEMPLATE-TC-MIB",
    "DynamicTemplateName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SubSessionIdentities,
 SubSessionIdentity,
 SubscriberAcctSessionId,
 SubscriberCircuitId,
 SubscriberDhcpClass,
 SubscriberDnis,
 SubscriberDomain,
 SubscriberLabel,
 SubscriberLocationName,
 SubscriberMediaType,
 SubscriberNasPort,
 SubscriberPbhk,
 SubscriberProtocolType,
 SubscriberRemoteId,
 SubscriberServiceName,
 SubscriberTunnelName,
 SubscriberUsername,
 SubscriberVRF) = mibBuilder.importSymbols(
    "CISCO-SUBSCRIBER-IDENTITY-TC-MIB",
    "SubSessionIdentities",
    "SubSessionIdentity",
    "SubscriberAcctSessionId",
    "SubscriberCircuitId",
    "SubscriberDhcpClass",
    "SubscriberDnis",
    "SubscriberDomain",
    "SubscriberLabel",
    "SubscriberLocationName",
    "SubscriberMediaType",
    "SubscriberNasPort",
    "SubscriberPbhk",
    "SubscriberProtocolType",
    "SubscriberRemoteId",
    "SubscriberServiceName",
    "SubscriberTunnelName",
    "SubscriberUsername",
    "SubscriberVRF")

(SubSessionRedundancyMode,
 SubSessionState,
 SubSessionType) = mibBuilder.importSymbols(
    "CISCO-SUBSCRIBER-SESSION-TC-MIB",
    "SubSessionRedundancyMode",
    "SubSessionState",
    "SubSessionType")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoSubscriberSessionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 786)
)
ciscoSubscriberSessionMIB.setRevisions(
        ("2012-08-08 00:00",
         "2012-03-12 00:00",
         "2011-09-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SubscriberJobIdentifier(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class SubscriberJobIdentifierOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSubscriberSessionMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSubscriberSessionMIBNotifs = _CiscoSubscriberSessionMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 0)
)
_CiscoSubscriberSessionMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSubscriberSessionMIBObjects = _CiscoSubscriberSessionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1)
)
_CsubSession_ObjectIdentity = ObjectIdentity
csubSession = _CsubSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1)
)
_CsubSessionTable_Object = MibTable
csubSessionTable = _CsubSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1)
)
if mibBuilder.loadTexts:
    csubSessionTable.setStatus("current")
_CsubSessionEntry_Object = MibTableRow
csubSessionEntry = _CsubSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1)
)
csubSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    csubSessionEntry.setStatus("current")
_CsubSessionType_Type = SubSessionType
_CsubSessionType_Object = MibTableColumn
csubSessionType = _CsubSessionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 1),
    _CsubSessionType_Type()
)
csubSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionType.setStatus("current")


class _CsubSessionIpAddrAssignment_Type(Integer32):
    """Custom type csubSessionIpAddrAssignment based on Integer32"""
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
        *(("dhcpv4", 5),
          ("dhcpv6", 6),
          ("localPool", 4),
          ("none", 1),
          ("other", 2),
          ("static", 3),
          ("userProfileIpAddr", 7),
          ("userProfileIpSubnet", 8),
          ("userProfileNamedPool", 9))
    )


_CsubSessionIpAddrAssignment_Type.__name__ = "Integer32"
_CsubSessionIpAddrAssignment_Object = MibTableColumn
csubSessionIpAddrAssignment = _CsubSessionIpAddrAssignment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 2),
    _CsubSessionIpAddrAssignment_Type()
)
csubSessionIpAddrAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionIpAddrAssignment.setStatus("current")
_CsubSessionState_Type = SubSessionState
_CsubSessionState_Object = MibTableColumn
csubSessionState = _CsubSessionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 3),
    _CsubSessionState_Type()
)
csubSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionState.setStatus("current")
_CsubSessionAuthenticated_Type = TruthValue
_CsubSessionAuthenticated_Object = MibTableColumn
csubSessionAuthenticated = _CsubSessionAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 4),
    _CsubSessionAuthenticated_Type()
)
csubSessionAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionAuthenticated.setStatus("current")
_CsubSessionRedundancyMode_Type = SubSessionRedundancyMode
_CsubSessionRedundancyMode_Object = MibTableColumn
csubSessionRedundancyMode = _CsubSessionRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 5),
    _CsubSessionRedundancyMode_Type()
)
csubSessionRedundancyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionRedundancyMode.setStatus("current")
_CsubSessionCreationTime_Type = DateAndTime
_CsubSessionCreationTime_Object = MibTableColumn
csubSessionCreationTime = _CsubSessionCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 6),
    _CsubSessionCreationTime_Type()
)
csubSessionCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionCreationTime.setStatus("current")
_CsubSessionDerivedCfg_Type = DynamicTemplateName
_CsubSessionDerivedCfg_Object = MibTableColumn
csubSessionDerivedCfg = _CsubSessionDerivedCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 7),
    _CsubSessionDerivedCfg_Type()
)
csubSessionDerivedCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionDerivedCfg.setStatus("current")
_CsubSessionAvailableIdentities_Type = SubSessionIdentities
_CsubSessionAvailableIdentities_Object = MibTableColumn
csubSessionAvailableIdentities = _CsubSessionAvailableIdentities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 8),
    _CsubSessionAvailableIdentities_Type()
)
csubSessionAvailableIdentities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionAvailableIdentities.setStatus("current")
_CsubSessionSubscriberLabel_Type = SubscriberLabel
_CsubSessionSubscriberLabel_Object = MibTableColumn
csubSessionSubscriberLabel = _CsubSessionSubscriberLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 9),
    _CsubSessionSubscriberLabel_Type()
)
csubSessionSubscriberLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionSubscriberLabel.setStatus("current")
_CsubSessionMacAddress_Type = MacAddress
_CsubSessionMacAddress_Object = MibTableColumn
csubSessionMacAddress = _CsubSessionMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 10),
    _CsubSessionMacAddress_Type()
)
csubSessionMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionMacAddress.setStatus("current")
_CsubSessionNativeVrf_Type = SubscriberVRF
_CsubSessionNativeVrf_Object = MibTableColumn
csubSessionNativeVrf = _CsubSessionNativeVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 11),
    _CsubSessionNativeVrf_Type()
)
csubSessionNativeVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionNativeVrf.setStatus("current")
_CsubSessionNativeIpAddrType_Type = InetAddressType
_CsubSessionNativeIpAddrType_Object = MibTableColumn
csubSessionNativeIpAddrType = _CsubSessionNativeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 12),
    _CsubSessionNativeIpAddrType_Type()
)
csubSessionNativeIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionNativeIpAddrType.setStatus("current")
_CsubSessionNativeIpAddr_Type = InetAddress
_CsubSessionNativeIpAddr_Object = MibTableColumn
csubSessionNativeIpAddr = _CsubSessionNativeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 13),
    _CsubSessionNativeIpAddr_Type()
)
csubSessionNativeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionNativeIpAddr.setStatus("current")
_CsubSessionNativeIpMask_Type = InetAddress
_CsubSessionNativeIpMask_Object = MibTableColumn
csubSessionNativeIpMask = _CsubSessionNativeIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 14),
    _CsubSessionNativeIpMask_Type()
)
csubSessionNativeIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionNativeIpMask.setStatus("current")
_CsubSessionDomainVrf_Type = SubscriberVRF
_CsubSessionDomainVrf_Object = MibTableColumn
csubSessionDomainVrf = _CsubSessionDomainVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 15),
    _CsubSessionDomainVrf_Type()
)
csubSessionDomainVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionDomainVrf.setStatus("current")
_CsubSessionDomainIpAddrType_Type = InetAddressType
_CsubSessionDomainIpAddrType_Object = MibTableColumn
csubSessionDomainIpAddrType = _CsubSessionDomainIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 16),
    _CsubSessionDomainIpAddrType_Type()
)
csubSessionDomainIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionDomainIpAddrType.setStatus("current")
_CsubSessionDomainIpAddr_Type = InetAddress
_CsubSessionDomainIpAddr_Object = MibTableColumn
csubSessionDomainIpAddr = _CsubSessionDomainIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 17),
    _CsubSessionDomainIpAddr_Type()
)
csubSessionDomainIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionDomainIpAddr.setStatus("current")
_CsubSessionDomainIpMask_Type = InetAddress
_CsubSessionDomainIpMask_Object = MibTableColumn
csubSessionDomainIpMask = _CsubSessionDomainIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 18),
    _CsubSessionDomainIpMask_Type()
)
csubSessionDomainIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionDomainIpMask.setStatus("current")
_CsubSessionPbhk_Type = SubscriberPbhk
_CsubSessionPbhk_Object = MibTableColumn
csubSessionPbhk = _CsubSessionPbhk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 19),
    _CsubSessionPbhk_Type()
)
csubSessionPbhk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionPbhk.setStatus("current")
_CsubSessionRemoteId_Type = SubscriberRemoteId
_CsubSessionRemoteId_Object = MibTableColumn
csubSessionRemoteId = _CsubSessionRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 20),
    _CsubSessionRemoteId_Type()
)
csubSessionRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionRemoteId.setStatus("current")
_CsubSessionCircuitId_Type = SubscriberCircuitId
_CsubSessionCircuitId_Object = MibTableColumn
csubSessionCircuitId = _CsubSessionCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 21),
    _CsubSessionCircuitId_Type()
)
csubSessionCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionCircuitId.setStatus("current")
_CsubSessionNasPort_Type = SubscriberNasPort
_CsubSessionNasPort_Object = MibTableColumn
csubSessionNasPort = _CsubSessionNasPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 22),
    _CsubSessionNasPort_Type()
)
csubSessionNasPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionNasPort.setStatus("current")
_CsubSessionDomain_Type = SubscriberDomain
_CsubSessionDomain_Object = MibTableColumn
csubSessionDomain = _CsubSessionDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 23),
    _CsubSessionDomain_Type()
)
csubSessionDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionDomain.setStatus("current")
_CsubSessionUsername_Type = SubscriberUsername
_CsubSessionUsername_Object = MibTableColumn
csubSessionUsername = _CsubSessionUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 24),
    _CsubSessionUsername_Type()
)
csubSessionUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionUsername.setStatus("current")
_CsubSessionAcctSessionId_Type = SubscriberAcctSessionId
_CsubSessionAcctSessionId_Object = MibTableColumn
csubSessionAcctSessionId = _CsubSessionAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 25),
    _CsubSessionAcctSessionId_Type()
)
csubSessionAcctSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionAcctSessionId.setStatus("current")
_CsubSessionDnis_Type = SubscriberDnis
_CsubSessionDnis_Object = MibTableColumn
csubSessionDnis = _CsubSessionDnis_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 26),
    _CsubSessionDnis_Type()
)
csubSessionDnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionDnis.setStatus("current")
_CsubSessionMedia_Type = SubscriberMediaType
_CsubSessionMedia_Object = MibTableColumn
csubSessionMedia = _CsubSessionMedia_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 27),
    _CsubSessionMedia_Type()
)
csubSessionMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionMedia.setStatus("current")
_CsubSessionMlpNegotiated_Type = TruthValue
_CsubSessionMlpNegotiated_Object = MibTableColumn
csubSessionMlpNegotiated = _CsubSessionMlpNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 28),
    _CsubSessionMlpNegotiated_Type()
)
csubSessionMlpNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionMlpNegotiated.setStatus("current")
_CsubSessionProtocol_Type = SubscriberProtocolType
_CsubSessionProtocol_Object = MibTableColumn
csubSessionProtocol = _CsubSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 29),
    _CsubSessionProtocol_Type()
)
csubSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionProtocol.setStatus("current")
_CsubSessionDhcpClass_Type = SubscriberDhcpClass
_CsubSessionDhcpClass_Object = MibTableColumn
csubSessionDhcpClass = _CsubSessionDhcpClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 30),
    _CsubSessionDhcpClass_Type()
)
csubSessionDhcpClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionDhcpClass.setStatus("current")
_CsubSessionTunnelName_Type = SubscriberTunnelName
_CsubSessionTunnelName_Object = MibTableColumn
csubSessionTunnelName = _CsubSessionTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 31),
    _CsubSessionTunnelName_Type()
)
csubSessionTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionTunnelName.setStatus("current")
_CsubSessionLocationIdentifier_Type = SubscriberLocationName
_CsubSessionLocationIdentifier_Object = MibTableColumn
csubSessionLocationIdentifier = _CsubSessionLocationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 32),
    _CsubSessionLocationIdentifier_Type()
)
csubSessionLocationIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionLocationIdentifier.setStatus("current")
_CsubSessionServiceIdentifier_Type = SubscriberServiceName
_CsubSessionServiceIdentifier_Object = MibTableColumn
csubSessionServiceIdentifier = _CsubSessionServiceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 33),
    _CsubSessionServiceIdentifier_Type()
)
csubSessionServiceIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionServiceIdentifier.setStatus("current")
_CsubSessionLastChanged_Type = DateAndTime
_CsubSessionLastChanged_Object = MibTableColumn
csubSessionLastChanged = _CsubSessionLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 34),
    _CsubSessionLastChanged_Type()
)
csubSessionLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionLastChanged.setStatus("current")
_CsubSessionNativeIpAddrType2_Type = InetAddressType
_CsubSessionNativeIpAddrType2_Object = MibTableColumn
csubSessionNativeIpAddrType2 = _CsubSessionNativeIpAddrType2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 35),
    _CsubSessionNativeIpAddrType2_Type()
)
csubSessionNativeIpAddrType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionNativeIpAddrType2.setStatus("current")
_CsubSessionNativeIpAddr2_Type = InetAddress
_CsubSessionNativeIpAddr2_Object = MibTableColumn
csubSessionNativeIpAddr2 = _CsubSessionNativeIpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 36),
    _CsubSessionNativeIpAddr2_Type()
)
csubSessionNativeIpAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionNativeIpAddr2.setStatus("current")
_CsubSessionNativeIpMask2_Type = InetAddress
_CsubSessionNativeIpMask2_Object = MibTableColumn
csubSessionNativeIpMask2 = _CsubSessionNativeIpMask2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 1, 1, 37),
    _CsubSessionNativeIpMask2_Type()
)
csubSessionNativeIpMask2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionNativeIpMask2.setStatus("current")
_CsubSessionByTypeTable_Object = MibTable
csubSessionByTypeTable = _CsubSessionByTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 2)
)
if mibBuilder.loadTexts:
    csubSessionByTypeTable.setStatus("current")
_CsubSessionByTypeEntry_Object = MibTableRow
csubSessionByTypeEntry = _CsubSessionByTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 2, 1)
)
csubSessionByTypeEntry.setIndexNames(
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionByType"),
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionIfIndex"),
)
if mibBuilder.loadTexts:
    csubSessionByTypeEntry.setStatus("current")
_CsubSessionByType_Type = SubSessionType
_CsubSessionByType_Object = MibTableColumn
csubSessionByType = _CsubSessionByType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 2, 1, 1),
    _CsubSessionByType_Type()
)
csubSessionByType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionByType.setStatus("current")
_CsubSessionIfIndex_Type = InterfaceIndex
_CsubSessionIfIndex_Object = MibTableColumn
csubSessionIfIndex = _CsubSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 1, 2, 1, 2),
    _CsubSessionIfIndex_Type()
)
csubSessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubSessionIfIndex.setStatus("current")
_CsubAggStats_ObjectIdentity = ObjectIdentity
csubAggStats = _CsubAggStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2)
)
_CsubAggStatsTable_Object = MibTable
csubAggStatsTable = _CsubAggStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1)
)
if mibBuilder.loadTexts:
    csubAggStatsTable.setStatus("current")
_CsubAggStatsEntry_Object = MibTableRow
csubAggStatsEntry = _CsubAggStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1)
)
csubAggStatsEntry.setIndexNames(
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsPointType"),
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsPoint"),
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsSessionType"),
)
if mibBuilder.loadTexts:
    csubAggStatsEntry.setStatus("current")


class _CsubAggStatsPointType_Type(Integer32):
    """Custom type csubAggStatsPointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 2),
          ("physical", 1))
    )


_CsubAggStatsPointType_Type.__name__ = "Integer32"
_CsubAggStatsPointType_Object = MibTableColumn
csubAggStatsPointType = _CsubAggStatsPointType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 1),
    _CsubAggStatsPointType_Type()
)
csubAggStatsPointType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csubAggStatsPointType.setStatus("current")


class _CsubAggStatsPoint_Type(Unsigned32):
    """Custom type csubAggStatsPoint based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CsubAggStatsPoint_Type.__name__ = "Unsigned32"
_CsubAggStatsPoint_Object = MibTableColumn
csubAggStatsPoint = _CsubAggStatsPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 2),
    _CsubAggStatsPoint_Type()
)
csubAggStatsPoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csubAggStatsPoint.setStatus("current")
_CsubAggStatsSessionType_Type = SubSessionType
_CsubAggStatsSessionType_Object = MibTableColumn
csubAggStatsSessionType = _CsubAggStatsSessionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 3),
    _CsubAggStatsSessionType_Type()
)
csubAggStatsSessionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csubAggStatsSessionType.setStatus("current")
_CsubAggStatsPendingSessions_Type = Gauge32
_CsubAggStatsPendingSessions_Object = MibTableColumn
csubAggStatsPendingSessions = _CsubAggStatsPendingSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 4),
    _CsubAggStatsPendingSessions_Type()
)
csubAggStatsPendingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsPendingSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsPendingSessions.setUnits("sessions")
_CsubAggStatsUpSessions_Type = Gauge32
_CsubAggStatsUpSessions_Object = MibTableColumn
csubAggStatsUpSessions = _CsubAggStatsUpSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 5),
    _CsubAggStatsUpSessions_Type()
)
csubAggStatsUpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsUpSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsUpSessions.setUnits("sessions")
_CsubAggStatsAuthSessions_Type = Gauge32
_CsubAggStatsAuthSessions_Object = MibTableColumn
csubAggStatsAuthSessions = _CsubAggStatsAuthSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 6),
    _CsubAggStatsAuthSessions_Type()
)
csubAggStatsAuthSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsAuthSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsAuthSessions.setUnits("sessions")
_CsubAggStatsUnAuthSessions_Type = Gauge32
_CsubAggStatsUnAuthSessions_Object = MibTableColumn
csubAggStatsUnAuthSessions = _CsubAggStatsUnAuthSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 7),
    _CsubAggStatsUnAuthSessions_Type()
)
csubAggStatsUnAuthSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsUnAuthSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsUnAuthSessions.setUnits("sessions")
_CsubAggStatsLightWeightSessions_Type = Gauge32
_CsubAggStatsLightWeightSessions_Object = MibTableColumn
csubAggStatsLightWeightSessions = _CsubAggStatsLightWeightSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 8),
    _CsubAggStatsLightWeightSessions_Type()
)
csubAggStatsLightWeightSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsLightWeightSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsLightWeightSessions.setUnits("sessions")
_CsubAggStatsRedSessions_Type = Gauge32
_CsubAggStatsRedSessions_Object = MibTableColumn
csubAggStatsRedSessions = _CsubAggStatsRedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 9),
    _CsubAggStatsRedSessions_Type()
)
csubAggStatsRedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsRedSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsRedSessions.setUnits("sessions")
_CsubAggStatsHighUpSessions_Type = Gauge32
_CsubAggStatsHighUpSessions_Object = MibTableColumn
csubAggStatsHighUpSessions = _CsubAggStatsHighUpSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 10),
    _CsubAggStatsHighUpSessions_Type()
)
csubAggStatsHighUpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsHighUpSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsHighUpSessions.setUnits("sessions")
_CsubAggStatsAvgSessionUptime_Type = Gauge32
_CsubAggStatsAvgSessionUptime_Object = MibTableColumn
csubAggStatsAvgSessionUptime = _CsubAggStatsAvgSessionUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 11),
    _CsubAggStatsAvgSessionUptime_Type()
)
csubAggStatsAvgSessionUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsAvgSessionUptime.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsAvgSessionUptime.setUnits("seconds")
_CsubAggStatsAvgSessionRPM_Type = Gauge32
_CsubAggStatsAvgSessionRPM_Object = MibTableColumn
csubAggStatsAvgSessionRPM = _CsubAggStatsAvgSessionRPM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 12),
    _CsubAggStatsAvgSessionRPM_Type()
)
csubAggStatsAvgSessionRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsAvgSessionRPM.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsAvgSessionRPM.setUnits("sessions per minute")
_CsubAggStatsAvgSessionRPH_Type = Gauge32
_CsubAggStatsAvgSessionRPH_Object = MibTableColumn
csubAggStatsAvgSessionRPH = _CsubAggStatsAvgSessionRPH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 13),
    _CsubAggStatsAvgSessionRPH_Type()
)
csubAggStatsAvgSessionRPH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsAvgSessionRPH.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsAvgSessionRPH.setUnits("sessions per hour")
_CsubAggStatsThrottleEngagements_Type = Counter64
_CsubAggStatsThrottleEngagements_Object = MibTableColumn
csubAggStatsThrottleEngagements = _CsubAggStatsThrottleEngagements_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 14),
    _CsubAggStatsThrottleEngagements_Type()
)
csubAggStatsThrottleEngagements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsThrottleEngagements.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsThrottleEngagements.setUnits("engagements")
_CsubAggStatsTotalCreatedSessions_Type = Counter64
_CsubAggStatsTotalCreatedSessions_Object = MibTableColumn
csubAggStatsTotalCreatedSessions = _CsubAggStatsTotalCreatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 15),
    _CsubAggStatsTotalCreatedSessions_Type()
)
csubAggStatsTotalCreatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsTotalCreatedSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsTotalCreatedSessions.setUnits("sessions")
_CsubAggStatsTotalFailedSessions_Type = Counter64
_CsubAggStatsTotalFailedSessions_Object = MibTableColumn
csubAggStatsTotalFailedSessions = _CsubAggStatsTotalFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 16),
    _CsubAggStatsTotalFailedSessions_Type()
)
csubAggStatsTotalFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsTotalFailedSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsTotalFailedSessions.setUnits("sessions")
_CsubAggStatsTotalUpSessions_Type = Counter64
_CsubAggStatsTotalUpSessions_Object = MibTableColumn
csubAggStatsTotalUpSessions = _CsubAggStatsTotalUpSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 17),
    _CsubAggStatsTotalUpSessions_Type()
)
csubAggStatsTotalUpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsTotalUpSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsTotalUpSessions.setUnits("sessions")
_CsubAggStatsTotalAuthSessions_Type = Counter64
_CsubAggStatsTotalAuthSessions_Object = MibTableColumn
csubAggStatsTotalAuthSessions = _CsubAggStatsTotalAuthSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 18),
    _CsubAggStatsTotalAuthSessions_Type()
)
csubAggStatsTotalAuthSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsTotalAuthSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsTotalAuthSessions.setUnits("sessions")
_CsubAggStatsTotalDiscSessions_Type = Counter64
_CsubAggStatsTotalDiscSessions_Object = MibTableColumn
csubAggStatsTotalDiscSessions = _CsubAggStatsTotalDiscSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 19),
    _CsubAggStatsTotalDiscSessions_Type()
)
csubAggStatsTotalDiscSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsTotalDiscSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsTotalDiscSessions.setUnits("sessions")
_CsubAggStatsTotalLightWeightSessions_Type = Counter64
_CsubAggStatsTotalLightWeightSessions_Object = MibTableColumn
csubAggStatsTotalLightWeightSessions = _CsubAggStatsTotalLightWeightSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 20),
    _CsubAggStatsTotalLightWeightSessions_Type()
)
csubAggStatsTotalLightWeightSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsTotalLightWeightSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsTotalLightWeightSessions.setUnits("sessions")
_CsubAggStatsTotalFlowsUp_Type = Counter64
_CsubAggStatsTotalFlowsUp_Object = MibTableColumn
csubAggStatsTotalFlowsUp = _CsubAggStatsTotalFlowsUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 21),
    _CsubAggStatsTotalFlowsUp_Type()
)
csubAggStatsTotalFlowsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsTotalFlowsUp.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsTotalFlowsUp.setUnits("sessions")
_CsubAggStatsDayCreatedSessions_Type = PerfTotalCount
_CsubAggStatsDayCreatedSessions_Object = MibTableColumn
csubAggStatsDayCreatedSessions = _CsubAggStatsDayCreatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 22),
    _CsubAggStatsDayCreatedSessions_Type()
)
csubAggStatsDayCreatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsDayCreatedSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsDayCreatedSessions.setUnits("sessions")
_CsubAggStatsDayFailedSessions_Type = PerfTotalCount
_CsubAggStatsDayFailedSessions_Object = MibTableColumn
csubAggStatsDayFailedSessions = _CsubAggStatsDayFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 23),
    _CsubAggStatsDayFailedSessions_Type()
)
csubAggStatsDayFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsDayFailedSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsDayFailedSessions.setUnits("sessions")
_CsubAggStatsDayUpSessions_Type = PerfTotalCount
_CsubAggStatsDayUpSessions_Object = MibTableColumn
csubAggStatsDayUpSessions = _CsubAggStatsDayUpSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 24),
    _CsubAggStatsDayUpSessions_Type()
)
csubAggStatsDayUpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsDayUpSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsDayUpSessions.setUnits("sessions")
_CsubAggStatsDayAuthSessions_Type = PerfTotalCount
_CsubAggStatsDayAuthSessions_Object = MibTableColumn
csubAggStatsDayAuthSessions = _CsubAggStatsDayAuthSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 25),
    _CsubAggStatsDayAuthSessions_Type()
)
csubAggStatsDayAuthSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsDayAuthSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsDayAuthSessions.setUnits("sessions")
_CsubAggStatsDayDiscSessions_Type = PerfTotalCount
_CsubAggStatsDayDiscSessions_Object = MibTableColumn
csubAggStatsDayDiscSessions = _CsubAggStatsDayDiscSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 26),
    _CsubAggStatsDayDiscSessions_Type()
)
csubAggStatsDayDiscSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsDayDiscSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsDayDiscSessions.setUnits("sessions")


class _CsubAggStatsCurrTimeElapsed_Type(Gauge32):
    """Custom type csubAggStatsCurrTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_CsubAggStatsCurrTimeElapsed_Type.__name__ = "Gauge32"
_CsubAggStatsCurrTimeElapsed_Object = MibTableColumn
csubAggStatsCurrTimeElapsed = _CsubAggStatsCurrTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 27),
    _CsubAggStatsCurrTimeElapsed_Type()
)
csubAggStatsCurrTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsCurrTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsCurrTimeElapsed.setUnits("seconds")


class _CsubAggStatsCurrValidIntervals_Type(Gauge32):
    """Custom type csubAggStatsCurrValidIntervals based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CsubAggStatsCurrValidIntervals_Type.__name__ = "Gauge32"
_CsubAggStatsCurrValidIntervals_Object = MibTableColumn
csubAggStatsCurrValidIntervals = _CsubAggStatsCurrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 28),
    _CsubAggStatsCurrValidIntervals_Type()
)
csubAggStatsCurrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsCurrValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsCurrValidIntervals.setUnits("intervals")


class _CsubAggStatsCurrInvalidIntervals_Type(Gauge32):
    """Custom type csubAggStatsCurrInvalidIntervals based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CsubAggStatsCurrInvalidIntervals_Type.__name__ = "Gauge32"
_CsubAggStatsCurrInvalidIntervals_Object = MibTableColumn
csubAggStatsCurrInvalidIntervals = _CsubAggStatsCurrInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 29),
    _CsubAggStatsCurrInvalidIntervals_Type()
)
csubAggStatsCurrInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsCurrInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsCurrInvalidIntervals.setUnits("intervals")


class _CsubAggStatsCurrFlowsUp_Type(Gauge32):
    """Custom type csubAggStatsCurrFlowsUp based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CsubAggStatsCurrFlowsUp_Type.__name__ = "Gauge32"
_CsubAggStatsCurrFlowsUp_Object = MibTableColumn
csubAggStatsCurrFlowsUp = _CsubAggStatsCurrFlowsUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 30),
    _CsubAggStatsCurrFlowsUp_Type()
)
csubAggStatsCurrFlowsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsCurrFlowsUp.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsCurrFlowsUp.setUnits("intervals")
_CsubAggStatsCurrCreatedSessions_Type = PerfCurrentCount
_CsubAggStatsCurrCreatedSessions_Object = MibTableColumn
csubAggStatsCurrCreatedSessions = _CsubAggStatsCurrCreatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 31),
    _CsubAggStatsCurrCreatedSessions_Type()
)
csubAggStatsCurrCreatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsCurrCreatedSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsCurrCreatedSessions.setUnits("sessions")
_CsubAggStatsCurrFailedSessions_Type = PerfCurrentCount
_CsubAggStatsCurrFailedSessions_Object = MibTableColumn
csubAggStatsCurrFailedSessions = _CsubAggStatsCurrFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 32),
    _CsubAggStatsCurrFailedSessions_Type()
)
csubAggStatsCurrFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsCurrFailedSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsCurrFailedSessions.setUnits("sessions")
_CsubAggStatsCurrUpSessions_Type = PerfCurrentCount
_CsubAggStatsCurrUpSessions_Object = MibTableColumn
csubAggStatsCurrUpSessions = _CsubAggStatsCurrUpSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 33),
    _CsubAggStatsCurrUpSessions_Type()
)
csubAggStatsCurrUpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsCurrUpSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsCurrUpSessions.setUnits("sessions")
_CsubAggStatsCurrAuthSessions_Type = PerfCurrentCount
_CsubAggStatsCurrAuthSessions_Object = MibTableColumn
csubAggStatsCurrAuthSessions = _CsubAggStatsCurrAuthSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 34),
    _CsubAggStatsCurrAuthSessions_Type()
)
csubAggStatsCurrAuthSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsCurrAuthSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsCurrAuthSessions.setUnits("sessions")
_CsubAggStatsCurrDiscSessions_Type = PerfCurrentCount
_CsubAggStatsCurrDiscSessions_Object = MibTableColumn
csubAggStatsCurrDiscSessions = _CsubAggStatsCurrDiscSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 35),
    _CsubAggStatsCurrDiscSessions_Type()
)
csubAggStatsCurrDiscSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsCurrDiscSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsCurrDiscSessions.setUnits("sessions")
_CsubAggStatsDiscontinuityTime_Type = DateAndTime
_CsubAggStatsDiscontinuityTime_Object = MibTableColumn
csubAggStatsDiscontinuityTime = _CsubAggStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 1, 1, 36),
    _CsubAggStatsDiscontinuityTime_Type()
)
csubAggStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsDiscontinuityTime.setStatus("current")
_CsubAggStatsIntTable_Object = MibTable
csubAggStatsIntTable = _CsubAggStatsIntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 2)
)
if mibBuilder.loadTexts:
    csubAggStatsIntTable.setStatus("current")
_CsubAggStatsIntEntry_Object = MibTableRow
csubAggStatsIntEntry = _CsubAggStatsIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 2, 1)
)
csubAggStatsIntEntry.setIndexNames(
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsPointType"),
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsPoint"),
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsSessionType"),
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsIntNumber"),
)
if mibBuilder.loadTexts:
    csubAggStatsIntEntry.setStatus("current")


class _CsubAggStatsIntNumber_Type(Unsigned32):
    """Custom type csubAggStatsIntNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CsubAggStatsIntNumber_Type.__name__ = "Unsigned32"
_CsubAggStatsIntNumber_Object = MibTableColumn
csubAggStatsIntNumber = _CsubAggStatsIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 2, 1, 1),
    _CsubAggStatsIntNumber_Type()
)
csubAggStatsIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csubAggStatsIntNumber.setStatus("current")
_CsubAggStatsIntValid_Type = TruthValue
_CsubAggStatsIntValid_Object = MibTableColumn
csubAggStatsIntValid = _CsubAggStatsIntValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 2, 1, 2),
    _CsubAggStatsIntValid_Type()
)
csubAggStatsIntValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsIntValid.setStatus("current")
_CsubAggStatsIntCreatedSessions_Type = PerfIntervalCount
_CsubAggStatsIntCreatedSessions_Object = MibTableColumn
csubAggStatsIntCreatedSessions = _CsubAggStatsIntCreatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 2, 1, 3),
    _CsubAggStatsIntCreatedSessions_Type()
)
csubAggStatsIntCreatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsIntCreatedSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsIntCreatedSessions.setUnits("sessions")
_CsubAggStatsIntFailedSessions_Type = PerfIntervalCount
_CsubAggStatsIntFailedSessions_Object = MibTableColumn
csubAggStatsIntFailedSessions = _CsubAggStatsIntFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 2, 1, 4),
    _CsubAggStatsIntFailedSessions_Type()
)
csubAggStatsIntFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsIntFailedSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsIntFailedSessions.setUnits("sessions")
_CsubAggStatsIntUpSessions_Type = PerfIntervalCount
_CsubAggStatsIntUpSessions_Object = MibTableColumn
csubAggStatsIntUpSessions = _CsubAggStatsIntUpSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 2, 1, 5),
    _CsubAggStatsIntUpSessions_Type()
)
csubAggStatsIntUpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsIntUpSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsIntUpSessions.setUnits("sessions")
_CsubAggStatsIntAuthSessions_Type = PerfIntervalCount
_CsubAggStatsIntAuthSessions_Object = MibTableColumn
csubAggStatsIntAuthSessions = _CsubAggStatsIntAuthSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 2, 1, 6),
    _CsubAggStatsIntAuthSessions_Type()
)
csubAggStatsIntAuthSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsIntAuthSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsIntAuthSessions.setUnits("sessions")
_CsubAggStatsIntDiscSessions_Type = PerfIntervalCount
_CsubAggStatsIntDiscSessions_Object = MibTableColumn
csubAggStatsIntDiscSessions = _CsubAggStatsIntDiscSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 2, 1, 7),
    _CsubAggStatsIntDiscSessions_Type()
)
csubAggStatsIntDiscSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubAggStatsIntDiscSessions.setStatus("current")
if mibBuilder.loadTexts:
    csubAggStatsIntDiscSessions.setUnits("sessions")
_CsubAggStatsThreshTable_Object = MibTable
csubAggStatsThreshTable = _CsubAggStatsThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 3)
)
if mibBuilder.loadTexts:
    csubAggStatsThreshTable.setStatus("current")
_CsubAggStatsThreshEntry_Object = MibTableRow
csubAggStatsThreshEntry = _CsubAggStatsThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 3, 1)
)
csubAggStatsThreshEntry.setIndexNames(
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionRisingThresh"),
)
if mibBuilder.loadTexts:
    csubAggStatsThreshEntry.setStatus("current")


class _CsubSessionRisingThresh_Type(Unsigned32):
    """Custom type csubSessionRisingThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CsubSessionRisingThresh_Type.__name__ = "Unsigned32"
_CsubSessionRisingThresh_Object = MibTableColumn
csubSessionRisingThresh = _CsubSessionRisingThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 3, 1, 1),
    _CsubSessionRisingThresh_Type()
)
csubSessionRisingThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csubSessionRisingThresh.setStatus("current")


class _CsubSessionFallingThresh_Type(Unsigned32):
    """Custom type csubSessionFallingThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CsubSessionFallingThresh_Type.__name__ = "Unsigned32"
_CsubSessionFallingThresh_Object = MibTableColumn
csubSessionFallingThresh = _CsubSessionFallingThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 3, 1, 2),
    _CsubSessionFallingThresh_Type()
)
csubSessionFallingThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csubSessionFallingThresh.setStatus("current")


class _CsubSessionDeltaPercentFallingThresh_Type(Unsigned32):
    """Custom type csubSessionDeltaPercentFallingThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CsubSessionDeltaPercentFallingThresh_Type.__name__ = "Unsigned32"
_CsubSessionDeltaPercentFallingThresh_Object = MibTableColumn
csubSessionDeltaPercentFallingThresh = _CsubSessionDeltaPercentFallingThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 3, 1, 3),
    _CsubSessionDeltaPercentFallingThresh_Type()
)
csubSessionDeltaPercentFallingThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csubSessionDeltaPercentFallingThresh.setStatus("current")


class _CsubSessionThreshEvalInterval_Type(Unsigned32):
    """Custom type csubSessionThreshEvalInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_CsubSessionThreshEvalInterval_Type.__name__ = "Unsigned32"
_CsubSessionThreshEvalInterval_Object = MibTableColumn
csubSessionThreshEvalInterval = _CsubSessionThreshEvalInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 2, 3, 1, 4),
    _CsubSessionThreshEvalInterval_Type()
)
csubSessionThreshEvalInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csubSessionThreshEvalInterval.setStatus("current")
_CsubJob_ObjectIdentity = ObjectIdentity
csubJob = _CsubJob_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3)
)


class _CsubJobFinishedNotifyEnable_Type(TruthValue):
    """Custom type csubJobFinishedNotifyEnable based on TruthValue"""


_CsubJobFinishedNotifyEnable_Object = MibScalar
csubJobFinishedNotifyEnable = _CsubJobFinishedNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 1),
    _CsubJobFinishedNotifyEnable_Type()
)
csubJobFinishedNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csubJobFinishedNotifyEnable.setStatus("current")
_CsubJobIndexedAttributes_Type = SubSessionIdentities
_CsubJobIndexedAttributes_Object = MibScalar
csubJobIndexedAttributes = _CsubJobIndexedAttributes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 2),
    _CsubJobIndexedAttributes_Type()
)
csubJobIndexedAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubJobIndexedAttributes.setStatus("current")
_CsubJobIdNext_Type = SubscriberJobIdentifierOrZero
_CsubJobIdNext_Object = MibScalar
csubJobIdNext = _CsubJobIdNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 3),
    _CsubJobIdNext_Type()
)
csubJobIdNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubJobIdNext.setStatus("current")


class _CsubJobMaxNumber_Type(Unsigned32):
    """Custom type csubJobMaxNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CsubJobMaxNumber_Type.__name__ = "Unsigned32"
_CsubJobMaxNumber_Object = MibScalar
csubJobMaxNumber = _CsubJobMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 4),
    _CsubJobMaxNumber_Type()
)
csubJobMaxNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csubJobMaxNumber.setStatus("current")
if mibBuilder.loadTexts:
    csubJobMaxNumber.setUnits("jobs")


class _CsubJobMaxLife_Type(Unsigned32):
    """Custom type csubJobMaxLife based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CsubJobMaxLife_Type.__name__ = "Unsigned32"
_CsubJobMaxLife_Object = MibScalar
csubJobMaxLife = _CsubJobMaxLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 5),
    _CsubJobMaxLife_Type()
)
csubJobMaxLife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csubJobMaxLife.setStatus("current")
if mibBuilder.loadTexts:
    csubJobMaxLife.setUnits("seconds")
_CsubJobCount_Type = Gauge32
_CsubJobCount_Object = MibScalar
csubJobCount = _CsubJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 6),
    _CsubJobCount_Type()
)
csubJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubJobCount.setStatus("current")
if mibBuilder.loadTexts:
    csubJobCount.setUnits("jobs")
_CsubJobTable_Object = MibTable
csubJobTable = _CsubJobTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 7)
)
if mibBuilder.loadTexts:
    csubJobTable.setStatus("current")
_CsubJobEntry_Object = MibTableRow
csubJobEntry = _CsubJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 7, 1)
)
csubJobEntry.setIndexNames(
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubJobId"),
)
if mibBuilder.loadTexts:
    csubJobEntry.setStatus("current")
_CsubJobId_Type = SubscriberJobIdentifier
_CsubJobId_Object = MibTableColumn
csubJobId = _CsubJobId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 7, 1, 1),
    _CsubJobId_Type()
)
csubJobId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csubJobId.setStatus("current")
_CsubJobStatus_Type = RowStatus
_CsubJobStatus_Object = MibTableColumn
csubJobStatus = _CsubJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 7, 1, 2),
    _CsubJobStatus_Type()
)
csubJobStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobStatus.setStatus("current")


class _CsubJobStorage_Type(StorageType):
    """Custom type csubJobStorage based on StorageType"""


_CsubJobStorage_Object = MibTableColumn
csubJobStorage = _CsubJobStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 7, 1, 3),
    _CsubJobStorage_Type()
)
csubJobStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobStorage.setStatus("current")


class _CsubJobType_Type(Integer32):
    """Custom type csubJobType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("noop", 1),
          ("query", 2))
    )


_CsubJobType_Type.__name__ = "Integer32"
_CsubJobType_Object = MibTableColumn
csubJobType = _CsubJobType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 7, 1, 4),
    _CsubJobType_Type()
)
csubJobType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobType.setStatus("current")


class _CsubJobControl_Type(Integer32):
    """Custom type csubJobControl based on Integer32"""
    defaultValue = 1

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
        *(("abort", 3),
          ("noop", 1),
          ("release", 4),
          ("start", 2))
    )


_CsubJobControl_Type.__name__ = "Integer32"
_CsubJobControl_Object = MibTableColumn
csubJobControl = _CsubJobControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 7, 1, 5),
    _CsubJobControl_Type()
)
csubJobControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobControl.setStatus("current")


class _CsubJobState_Type(Integer32):
    """Custom type csubJobState based on Integer32"""
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
        *(("finished", 4),
          ("idle", 1),
          ("inProgress", 3),
          ("pending", 2))
    )


_CsubJobState_Type.__name__ = "Integer32"
_CsubJobState_Object = MibTableColumn
csubJobState = _CsubJobState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 7, 1, 6),
    _CsubJobState_Type()
)
csubJobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubJobState.setStatus("current")
_CsubJobStartedTime_Type = TimeStamp
_CsubJobStartedTime_Object = MibTableColumn
csubJobStartedTime = _CsubJobStartedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 7, 1, 7),
    _CsubJobStartedTime_Type()
)
csubJobStartedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubJobStartedTime.setStatus("current")
_CsubJobFinishedTime_Type = TimeStamp
_CsubJobFinishedTime_Object = MibTableColumn
csubJobFinishedTime = _CsubJobFinishedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 7, 1, 8),
    _CsubJobFinishedTime_Type()
)
csubJobFinishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubJobFinishedTime.setStatus("current")


class _CsubJobFinishedReason_Type(Integer32):
    """Custom type csubJobFinishedReason based on Integer32"""
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
        *(("aborted", 4),
          ("error", 6),
          ("insufficientResources", 5),
          ("invalid", 1),
          ("normal", 3),
          ("other", 2))
    )


_CsubJobFinishedReason_Type.__name__ = "Integer32"
_CsubJobFinishedReason_Object = MibTableColumn
csubJobFinishedReason = _CsubJobFinishedReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 7, 1, 9),
    _CsubJobFinishedReason_Type()
)
csubJobFinishedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubJobFinishedReason.setStatus("current")
_CsubJobMatchParamsTable_Object = MibTable
csubJobMatchParamsTable = _CsubJobMatchParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8)
)
if mibBuilder.loadTexts:
    csubJobMatchParamsTable.setStatus("current")
_CsubJobMatchParamsEntry_Object = MibTableRow
csubJobMatchParamsEntry = _CsubJobMatchParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1)
)
csubJobMatchParamsEntry.setIndexNames(
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubJobId"),
)
if mibBuilder.loadTexts:
    csubJobMatchParamsEntry.setStatus("current")


class _CsubJobMatchIdentities_Type(SubSessionIdentities):
    """Custom type csubJobMatchIdentities based on SubSessionIdentities"""
    defaultBinValue = "0"


_CsubJobMatchIdentities_Object = MibTableColumn
csubJobMatchIdentities = _CsubJobMatchIdentities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 1),
    _CsubJobMatchIdentities_Type()
)
csubJobMatchIdentities.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchIdentities.setStatus("current")


class _CsubJobMatchOtherParams_Type(Bits):
    """Custom type csubJobMatchOtherParams based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("authenticated", 2),
          ("danglingDuration", 0),
          ("redundancyMode", 3),
          ("state", 1))
    )

_CsubJobMatchOtherParams_Type.__name__ = "Bits"
_CsubJobMatchOtherParams_Object = MibTableColumn
csubJobMatchOtherParams = _CsubJobMatchOtherParams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 2),
    _CsubJobMatchOtherParams_Type()
)
csubJobMatchOtherParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchOtherParams.setStatus("current")


class _CsubJobMatchSubscriberLabel_Type(SubscriberLabel):
    """Custom type csubJobMatchSubscriberLabel based on SubscriberLabel"""
    defaultValue = 0


_CsubJobMatchSubscriberLabel_Object = MibTableColumn
csubJobMatchSubscriberLabel = _CsubJobMatchSubscriberLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 3),
    _CsubJobMatchSubscriberLabel_Type()
)
csubJobMatchSubscriberLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchSubscriberLabel.setStatus("current")


class _CsubJobMatchMacAddress_Type(MacAddress):
    """Custom type csubJobMatchMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_CsubJobMatchMacAddress_Object = MibTableColumn
csubJobMatchMacAddress = _CsubJobMatchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 4),
    _CsubJobMatchMacAddress_Type()
)
csubJobMatchMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchMacAddress.setStatus("current")
_CsubJobMatchNativeVrf_Type = SubscriberVRF
_CsubJobMatchNativeVrf_Object = MibTableColumn
csubJobMatchNativeVrf = _CsubJobMatchNativeVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 5),
    _CsubJobMatchNativeVrf_Type()
)
csubJobMatchNativeVrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchNativeVrf.setStatus("current")


class _CsubJobMatchNativeIpAddrType_Type(InetAddressType):
    """Custom type csubJobMatchNativeIpAddrType based on InetAddressType"""


_CsubJobMatchNativeIpAddrType_Object = MibTableColumn
csubJobMatchNativeIpAddrType = _CsubJobMatchNativeIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 6),
    _CsubJobMatchNativeIpAddrType_Type()
)
csubJobMatchNativeIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchNativeIpAddrType.setStatus("current")


class _CsubJobMatchNativeIpAddr_Type(InetAddress):
    """Custom type csubJobMatchNativeIpAddr based on InetAddress"""
    defaultHexValue = "00"


_CsubJobMatchNativeIpAddr_Object = MibTableColumn
csubJobMatchNativeIpAddr = _CsubJobMatchNativeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 7),
    _CsubJobMatchNativeIpAddr_Type()
)
csubJobMatchNativeIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchNativeIpAddr.setStatus("current")


class _CsubJobMatchNativeIpMask_Type(InetAddress):
    """Custom type csubJobMatchNativeIpMask based on InetAddress"""
    defaultHexValue = "00"


_CsubJobMatchNativeIpMask_Object = MibTableColumn
csubJobMatchNativeIpMask = _CsubJobMatchNativeIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 8),
    _CsubJobMatchNativeIpMask_Type()
)
csubJobMatchNativeIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchNativeIpMask.setStatus("current")
_CsubJobMatchDomainVrf_Type = SubscriberVRF
_CsubJobMatchDomainVrf_Object = MibTableColumn
csubJobMatchDomainVrf = _CsubJobMatchDomainVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 9),
    _CsubJobMatchDomainVrf_Type()
)
csubJobMatchDomainVrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchDomainVrf.setStatus("current")


class _CsubJobMatchDomainIpAddrType_Type(InetAddressType):
    """Custom type csubJobMatchDomainIpAddrType based on InetAddressType"""


_CsubJobMatchDomainIpAddrType_Object = MibTableColumn
csubJobMatchDomainIpAddrType = _CsubJobMatchDomainIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 10),
    _CsubJobMatchDomainIpAddrType_Type()
)
csubJobMatchDomainIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchDomainIpAddrType.setStatus("current")


class _CsubJobMatchDomainIpAddr_Type(InetAddress):
    """Custom type csubJobMatchDomainIpAddr based on InetAddress"""
    defaultHexValue = "00"


_CsubJobMatchDomainIpAddr_Object = MibTableColumn
csubJobMatchDomainIpAddr = _CsubJobMatchDomainIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 11),
    _CsubJobMatchDomainIpAddr_Type()
)
csubJobMatchDomainIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchDomainIpAddr.setStatus("current")


class _CsubJobMatchDomainIpMask_Type(InetAddress):
    """Custom type csubJobMatchDomainIpMask based on InetAddress"""
    defaultHexValue = "00"


_CsubJobMatchDomainIpMask_Object = MibTableColumn
csubJobMatchDomainIpMask = _CsubJobMatchDomainIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 12),
    _CsubJobMatchDomainIpMask_Type()
)
csubJobMatchDomainIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchDomainIpMask.setStatus("current")


class _CsubJobMatchPbhk_Type(SubscriberPbhk):
    """Custom type csubJobMatchPbhk based on SubscriberPbhk"""
    defaultHexValue = "000000000000"


_CsubJobMatchPbhk_Object = MibTableColumn
csubJobMatchPbhk = _CsubJobMatchPbhk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 13),
    _CsubJobMatchPbhk_Type()
)
csubJobMatchPbhk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchPbhk.setStatus("current")
_CsubJobMatchRemoteId_Type = SubscriberRemoteId
_CsubJobMatchRemoteId_Object = MibTableColumn
csubJobMatchRemoteId = _CsubJobMatchRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 14),
    _CsubJobMatchRemoteId_Type()
)
csubJobMatchRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchRemoteId.setStatus("current")
_CsubJobMatchCircuitId_Type = SubscriberCircuitId
_CsubJobMatchCircuitId_Object = MibTableColumn
csubJobMatchCircuitId = _CsubJobMatchCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 15),
    _CsubJobMatchCircuitId_Type()
)
csubJobMatchCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchCircuitId.setStatus("current")


class _CsubJobMatchNasPort_Type(SubscriberNasPort):
    """Custom type csubJobMatchNasPort based on SubscriberNasPort"""
    defaultHexValue = "00"


_CsubJobMatchNasPort_Object = MibTableColumn
csubJobMatchNasPort = _CsubJobMatchNasPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 16),
    _CsubJobMatchNasPort_Type()
)
csubJobMatchNasPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchNasPort.setStatus("current")
_CsubJobMatchDomain_Type = SubscriberDomain
_CsubJobMatchDomain_Object = MibTableColumn
csubJobMatchDomain = _CsubJobMatchDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 17),
    _CsubJobMatchDomain_Type()
)
csubJobMatchDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchDomain.setStatus("current")
_CsubJobMatchUsername_Type = SubscriberUsername
_CsubJobMatchUsername_Object = MibTableColumn
csubJobMatchUsername = _CsubJobMatchUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 18),
    _CsubJobMatchUsername_Type()
)
csubJobMatchUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchUsername.setStatus("current")


class _CsubJobMatchAcctSessionId_Type(SubscriberAcctSessionId):
    """Custom type csubJobMatchAcctSessionId based on SubscriberAcctSessionId"""
    defaultValue = 0


_CsubJobMatchAcctSessionId_Object = MibTableColumn
csubJobMatchAcctSessionId = _CsubJobMatchAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 20),
    _CsubJobMatchAcctSessionId_Type()
)
csubJobMatchAcctSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchAcctSessionId.setStatus("current")
_CsubJobMatchDnis_Type = SubscriberDnis
_CsubJobMatchDnis_Object = MibTableColumn
csubJobMatchDnis = _CsubJobMatchDnis_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 21),
    _CsubJobMatchDnis_Type()
)
csubJobMatchDnis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchDnis.setStatus("current")


class _CsubJobMatchMedia_Type(SubscriberMediaType):
    """Custom type csubJobMatchMedia based on SubscriberMediaType"""


_CsubJobMatchMedia_Object = MibTableColumn
csubJobMatchMedia = _CsubJobMatchMedia_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 22),
    _CsubJobMatchMedia_Type()
)
csubJobMatchMedia.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchMedia.setStatus("current")


class _CsubJobMatchMlpNegotiated_Type(TruthValue):
    """Custom type csubJobMatchMlpNegotiated based on TruthValue"""


_CsubJobMatchMlpNegotiated_Object = MibTableColumn
csubJobMatchMlpNegotiated = _CsubJobMatchMlpNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 23),
    _CsubJobMatchMlpNegotiated_Type()
)
csubJobMatchMlpNegotiated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchMlpNegotiated.setStatus("current")


class _CsubJobMatchProtocol_Type(SubscriberProtocolType):
    """Custom type csubJobMatchProtocol based on SubscriberProtocolType"""


_CsubJobMatchProtocol_Object = MibTableColumn
csubJobMatchProtocol = _CsubJobMatchProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 24),
    _CsubJobMatchProtocol_Type()
)
csubJobMatchProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchProtocol.setStatus("current")
_CsubJobMatchServiceName_Type = CbpElementName
_CsubJobMatchServiceName_Object = MibTableColumn
csubJobMatchServiceName = _CsubJobMatchServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 25),
    _CsubJobMatchServiceName_Type()
)
csubJobMatchServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchServiceName.setStatus("current")
_CsubJobMatchDhcpClass_Type = SubscriberDhcpClass
_CsubJobMatchDhcpClass_Object = MibTableColumn
csubJobMatchDhcpClass = _CsubJobMatchDhcpClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 26),
    _CsubJobMatchDhcpClass_Type()
)
csubJobMatchDhcpClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchDhcpClass.setStatus("current")
_CsubJobMatchTunnelName_Type = SubscriberTunnelName
_CsubJobMatchTunnelName_Object = MibTableColumn
csubJobMatchTunnelName = _CsubJobMatchTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 27),
    _CsubJobMatchTunnelName_Type()
)
csubJobMatchTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchTunnelName.setStatus("current")


class _CsubJobMatchDanglingDuration_Type(Unsigned32):
    """Custom type csubJobMatchDanglingDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CsubJobMatchDanglingDuration_Type.__name__ = "Unsigned32"
_CsubJobMatchDanglingDuration_Object = MibTableColumn
csubJobMatchDanglingDuration = _CsubJobMatchDanglingDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 28),
    _CsubJobMatchDanglingDuration_Type()
)
csubJobMatchDanglingDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchDanglingDuration.setStatus("current")


class _CsubJobMatchState_Type(SubSessionState):
    """Custom type csubJobMatchState based on SubSessionState"""


_CsubJobMatchState_Object = MibTableColumn
csubJobMatchState = _CsubJobMatchState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 29),
    _CsubJobMatchState_Type()
)
csubJobMatchState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchState.setStatus("current")


class _CsubJobMatchAuthenticated_Type(TruthValue):
    """Custom type csubJobMatchAuthenticated based on TruthValue"""


_CsubJobMatchAuthenticated_Object = MibTableColumn
csubJobMatchAuthenticated = _CsubJobMatchAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 30),
    _CsubJobMatchAuthenticated_Type()
)
csubJobMatchAuthenticated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchAuthenticated.setStatus("current")


class _CsubJobMatchRedundancyMode_Type(SubSessionRedundancyMode):
    """Custom type csubJobMatchRedundancyMode based on SubSessionRedundancyMode"""


_CsubJobMatchRedundancyMode_Object = MibTableColumn
csubJobMatchRedundancyMode = _CsubJobMatchRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 8, 1, 31),
    _CsubJobMatchRedundancyMode_Type()
)
csubJobMatchRedundancyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobMatchRedundancyMode.setStatus("current")
_CsubJobQueryParamsTable_Object = MibTable
csubJobQueryParamsTable = _CsubJobQueryParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 9)
)
if mibBuilder.loadTexts:
    csubJobQueryParamsTable.setStatus("current")
_CsubJobQueryParamsEntry_Object = MibTableRow
csubJobQueryParamsEntry = _CsubJobQueryParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 9, 1)
)
csubJobQueryParamsEntry.setIndexNames(
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubJobId"),
)
if mibBuilder.loadTexts:
    csubJobQueryParamsEntry.setStatus("current")


class _CsubJobQuerySortKey1_Type(SubSessionIdentity):
    """Custom type csubJobQuerySortKey1 based on SubSessionIdentity"""


_CsubJobQuerySortKey1_Object = MibTableColumn
csubJobQuerySortKey1 = _CsubJobQuerySortKey1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 9, 1, 1),
    _CsubJobQuerySortKey1_Type()
)
csubJobQuerySortKey1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobQuerySortKey1.setStatus("current")


class _CsubJobQuerySortKey2_Type(SubSessionIdentity):
    """Custom type csubJobQuerySortKey2 based on SubSessionIdentity"""


_CsubJobQuerySortKey2_Object = MibTableColumn
csubJobQuerySortKey2 = _CsubJobQuerySortKey2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 9, 1, 2),
    _CsubJobQuerySortKey2_Type()
)
csubJobQuerySortKey2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobQuerySortKey2.setStatus("current")


class _CsubJobQuerySortKey3_Type(SubSessionIdentity):
    """Custom type csubJobQuerySortKey3 based on SubSessionIdentity"""


_CsubJobQuerySortKey3_Object = MibTableColumn
csubJobQuerySortKey3 = _CsubJobQuerySortKey3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 9, 1, 3),
    _CsubJobQuerySortKey3_Type()
)
csubJobQuerySortKey3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csubJobQuerySortKey3.setStatus("current")
_CsubJobQueryResultingReportSize_Type = Gauge32
_CsubJobQueryResultingReportSize_Object = MibTableColumn
csubJobQueryResultingReportSize = _CsubJobQueryResultingReportSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 9, 1, 4),
    _CsubJobQueryResultingReportSize_Type()
)
csubJobQueryResultingReportSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubJobQueryResultingReportSize.setStatus("current")
_CsubJobQueueTable_Object = MibTable
csubJobQueueTable = _CsubJobQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 10)
)
if mibBuilder.loadTexts:
    csubJobQueueTable.setStatus("current")
_CsubJobQueueEntry_Object = MibTableRow
csubJobQueueEntry = _CsubJobQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 10, 1)
)
csubJobQueueEntry.setIndexNames(
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubJobQueueNumber"),
)
if mibBuilder.loadTexts:
    csubJobQueueEntry.setStatus("current")


class _CsubJobQueueNumber_Type(Unsigned32):
    """Custom type csubJobQueueNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CsubJobQueueNumber_Type.__name__ = "Unsigned32"
_CsubJobQueueNumber_Object = MibTableColumn
csubJobQueueNumber = _CsubJobQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 10, 1, 1),
    _CsubJobQueueNumber_Type()
)
csubJobQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csubJobQueueNumber.setStatus("current")
_CsubJobQueueJobId_Type = SubscriberJobIdentifier
_CsubJobQueueJobId_Object = MibTableColumn
csubJobQueueJobId = _CsubJobQueueJobId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 10, 1, 2),
    _CsubJobQueueJobId_Type()
)
csubJobQueueJobId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubJobQueueJobId.setStatus("current")
_CsubJobReportTable_Object = MibTable
csubJobReportTable = _CsubJobReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 11)
)
if mibBuilder.loadTexts:
    csubJobReportTable.setStatus("current")
_CsubJobReportEntry_Object = MibTableRow
csubJobReportEntry = _CsubJobReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 11, 1)
)
csubJobReportEntry.setIndexNames(
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubJobId"),
    (0, "CISCO-SUBSCRIBER-SESSION-MIB", "csubJobReportId"),
)
if mibBuilder.loadTexts:
    csubJobReportEntry.setStatus("current")


class _CsubJobReportId_Type(Unsigned32):
    """Custom type csubJobReportId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CsubJobReportId_Type.__name__ = "Unsigned32"
_CsubJobReportId_Object = MibTableColumn
csubJobReportId = _CsubJobReportId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 11, 1, 1),
    _CsubJobReportId_Type()
)
csubJobReportId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csubJobReportId.setStatus("current")
_CsubJobReportSession_Type = InterfaceIndex
_CsubJobReportSession_Object = MibTableColumn
csubJobReportSession = _CsubJobReportSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 3, 11, 1, 2),
    _CsubJobReportSession_Type()
)
csubJobReportSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csubJobReportSession.setStatus("current")
_CsubAggThresh_ObjectIdentity = ObjectIdentity
csubAggThresh = _CsubAggThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 4)
)
_CsubAggStatsThreshNotifEnable_Type = TruthValue
_CsubAggStatsThreshNotifEnable_Object = MibScalar
csubAggStatsThreshNotifEnable = _CsubAggStatsThreshNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 1, 4, 1),
    _CsubAggStatsThreshNotifEnable_Type()
)
csubAggStatsThreshNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csubAggStatsThreshNotifEnable.setStatus("current")
_CiscoSubscriberSessionMIBConform_ObjectIdentity = ObjectIdentity
ciscoSubscriberSessionMIBConform = _CiscoSubscriberSessionMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2)
)
_CiscoSubscriberSessionMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSubscriberSessionMIBCompliances = _CiscoSubscriberSessionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 1)
)
_CiscoSubscriberSessionMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSubscriberSessionMIBGroups = _CiscoSubscriberSessionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2)
)

# Managed Objects groups

csubSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 1)
)
csubSessionGroup.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionType"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionIpAddrAssignment"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionState"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionAuthenticated"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionRedundancyMode"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionCreationTime"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionDerivedCfg"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionAvailableIdentities"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionSubscriberLabel"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionMacAddress"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionNativeVrf"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionNativeIpAddrType"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionNativeIpAddr"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionNativeIpMask"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionDomainVrf"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionDomainIpAddrType"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionDomainIpAddr"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionDomainIpMask"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionPbhk"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionRemoteId"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionCircuitId"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionNasPort"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionDomain"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionUsername"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionAcctSessionId"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionDnis"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionMedia"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionMlpNegotiated"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionProtocol"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionDhcpClass"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionTunnelName"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionIfIndex"))
)
if mibBuilder.loadTexts:
    csubSessionGroup.setStatus("current")

csubAggStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 2)
)
csubAggStatsGroup.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsPendingSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsUpSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsAuthSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsRedSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsHighUpSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsAvgSessionUptime"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsAvgSessionRPM"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsAvgSessionRPH"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsThrottleEngagements"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsTotalCreatedSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsTotalFailedSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsTotalUpSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsTotalAuthSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsTotalDiscSessions"))
)
if mibBuilder.loadTexts:
    csubAggStatsGroup.setStatus("current")

csubAggStatsCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 3)
)
csubAggStatsCurrGroup.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsCurrTimeElapsed"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsCurrValidIntervals"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsCurrInvalidIntervals"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsCurrCreatedSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsCurrFailedSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsCurrUpSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsCurrAuthSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsCurrDiscSessions"))
)
if mibBuilder.loadTexts:
    csubAggStatsCurrGroup.setStatus("current")

csubAggStatsIntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 4)
)
csubAggStatsIntGroup.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsIntValid"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsIntCreatedSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsIntFailedSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsIntUpSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsIntAuthSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsIntDiscSessions"))
)
if mibBuilder.loadTexts:
    csubAggStatsIntGroup.setStatus("current")

csubAggStatsDayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 5)
)
csubAggStatsDayGroup.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsDayCreatedSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsDayFailedSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsDayUpSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsDayAuthSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsDayDiscSessions"))
)
if mibBuilder.loadTexts:
    csubAggStatsDayGroup.setStatus("current")

csubJobGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 6)
)
csubJobGroup.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobFinishedNotifyEnable"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobIndexedAttributes"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobIdNext"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMaxNumber"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMaxLife"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobCount"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobStatus"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobStorage"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobType"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobControl"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobState"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobStartedTime"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobFinishedTime"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobFinishedReason"))
)
if mibBuilder.loadTexts:
    csubJobGroup.setStatus("current")

csubJobMatchParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 7)
)
csubJobMatchParamsGroup.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchIdentities"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchOtherParams"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchSubscriberLabel"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchMacAddress"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchNativeVrf"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchNativeIpAddrType"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchNativeIpAddr"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchNativeIpMask"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchDomainVrf"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchDomainIpAddrType"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchDomainIpAddr"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchDomainIpMask"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchPbhk"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchRemoteId"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchCircuitId"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchNasPort"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchDomain"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchUsername"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchAcctSessionId"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchDnis"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchMedia"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchMlpNegotiated"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchProtocol"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchServiceName"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchDhcpClass"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchTunnelName"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchDanglingDuration"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchState"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchAuthenticated"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobMatchRedundancyMode"))
)
if mibBuilder.loadTexts:
    csubJobMatchParamsGroup.setStatus("current")

csubJobQueryParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 8)
)
csubJobQueryParamsGroup.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobQuerySortKey1"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobQuerySortKey2"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobQuerySortKey3"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobQueryResultingReportSize"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobReportSession"))
)
if mibBuilder.loadTexts:
    csubJobQueryParamsGroup.setStatus("current")

csubJobQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 9)
)
csubJobQueueGroup.setObjects(
    ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobQueueJobId")
)
if mibBuilder.loadTexts:
    csubJobQueueGroup.setStatus("current")

csubAggStatsThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 11)
)
csubAggStatsThreshGroup.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionRisingThresh"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionFallingThresh"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionDeltaPercentFallingThresh"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionThreshEvalInterval"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsThreshNotifEnable"))
)
if mibBuilder.loadTexts:
    csubAggStatsThreshGroup.setStatus("current")


# Notification objects

csubJobFinishedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 0, 1)
)
csubJobFinishedNotify.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobStartedTime"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobFinishedTime"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobFinishedReason"))
)
if mibBuilder.loadTexts:
    csubJobFinishedNotify.setStatus(
        "current"
    )

csubSessionRisingNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 0, 2)
)
csubSessionRisingNotif.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsUpSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionRisingThresh"))
)
if mibBuilder.loadTexts:
    csubSessionRisingNotif.setStatus(
        "current"
    )

csubSessionFallingNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 0, 3)
)
csubSessionFallingNotif.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsUpSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionFallingThresh"))
)
if mibBuilder.loadTexts:
    csubSessionFallingNotif.setStatus(
        "current"
    )

csubSessionDeltaPercentFallingThreshNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 0, 4)
)
csubSessionDeltaPercentFallingThreshNotif.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubAggStatsUpSessions"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionDeltaPercentFallingThresh"))
)
if mibBuilder.loadTexts:
    csubSessionDeltaPercentFallingThreshNotif.setStatus(
        "current"
    )


# Notifications groups

csubJobNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 10)
)
csubJobNotifGroup.setObjects(
    ("CISCO-SUBSCRIBER-SESSION-MIB", "csubJobFinishedNotify")
)
if mibBuilder.loadTexts:
    csubJobNotifGroup.setStatus(
        "current"
    )

csubAggStatsNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 2, 12)
)
csubAggStatsNotifGroup.setObjects(
      *(("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionRisingNotif"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionFallingNotif"),
        ("CISCO-SUBSCRIBER-SESSION-MIB", "csubSessionDeltaPercentFallingThreshNotif"))
)
if mibBuilder.loadTexts:
    csubAggStatsNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSubscriberSessionR1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSubscriberSessionR1Compliance.setStatus(
        "obsolete"
    )

ciscoSubscriberSessionR2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 786, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSubscriberSessionR2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SUBSCRIBER-SESSION-MIB",
    **{"SubscriberJobIdentifier": SubscriberJobIdentifier,
       "SubscriberJobIdentifierOrZero": SubscriberJobIdentifierOrZero,
       "ciscoSubscriberSessionMIB": ciscoSubscriberSessionMIB,
       "ciscoSubscriberSessionMIBNotifs": ciscoSubscriberSessionMIBNotifs,
       "csubJobFinishedNotify": csubJobFinishedNotify,
       "csubSessionRisingNotif": csubSessionRisingNotif,
       "csubSessionFallingNotif": csubSessionFallingNotif,
       "csubSessionDeltaPercentFallingThreshNotif": csubSessionDeltaPercentFallingThreshNotif,
       "ciscoSubscriberSessionMIBObjects": ciscoSubscriberSessionMIBObjects,
       "csubSession": csubSession,
       "csubSessionTable": csubSessionTable,
       "csubSessionEntry": csubSessionEntry,
       "csubSessionType": csubSessionType,
       "csubSessionIpAddrAssignment": csubSessionIpAddrAssignment,
       "csubSessionState": csubSessionState,
       "csubSessionAuthenticated": csubSessionAuthenticated,
       "csubSessionRedundancyMode": csubSessionRedundancyMode,
       "csubSessionCreationTime": csubSessionCreationTime,
       "csubSessionDerivedCfg": csubSessionDerivedCfg,
       "csubSessionAvailableIdentities": csubSessionAvailableIdentities,
       "csubSessionSubscriberLabel": csubSessionSubscriberLabel,
       "csubSessionMacAddress": csubSessionMacAddress,
       "csubSessionNativeVrf": csubSessionNativeVrf,
       "csubSessionNativeIpAddrType": csubSessionNativeIpAddrType,
       "csubSessionNativeIpAddr": csubSessionNativeIpAddr,
       "csubSessionNativeIpMask": csubSessionNativeIpMask,
       "csubSessionDomainVrf": csubSessionDomainVrf,
       "csubSessionDomainIpAddrType": csubSessionDomainIpAddrType,
       "csubSessionDomainIpAddr": csubSessionDomainIpAddr,
       "csubSessionDomainIpMask": csubSessionDomainIpMask,
       "csubSessionPbhk": csubSessionPbhk,
       "csubSessionRemoteId": csubSessionRemoteId,
       "csubSessionCircuitId": csubSessionCircuitId,
       "csubSessionNasPort": csubSessionNasPort,
       "csubSessionDomain": csubSessionDomain,
       "csubSessionUsername": csubSessionUsername,
       "csubSessionAcctSessionId": csubSessionAcctSessionId,
       "csubSessionDnis": csubSessionDnis,
       "csubSessionMedia": csubSessionMedia,
       "csubSessionMlpNegotiated": csubSessionMlpNegotiated,
       "csubSessionProtocol": csubSessionProtocol,
       "csubSessionDhcpClass": csubSessionDhcpClass,
       "csubSessionTunnelName": csubSessionTunnelName,
       "csubSessionLocationIdentifier": csubSessionLocationIdentifier,
       "csubSessionServiceIdentifier": csubSessionServiceIdentifier,
       "csubSessionLastChanged": csubSessionLastChanged,
       "csubSessionNativeIpAddrType2": csubSessionNativeIpAddrType2,
       "csubSessionNativeIpAddr2": csubSessionNativeIpAddr2,
       "csubSessionNativeIpMask2": csubSessionNativeIpMask2,
       "csubSessionByTypeTable": csubSessionByTypeTable,
       "csubSessionByTypeEntry": csubSessionByTypeEntry,
       "csubSessionByType": csubSessionByType,
       "csubSessionIfIndex": csubSessionIfIndex,
       "csubAggStats": csubAggStats,
       "csubAggStatsTable": csubAggStatsTable,
       "csubAggStatsEntry": csubAggStatsEntry,
       "csubAggStatsPointType": csubAggStatsPointType,
       "csubAggStatsPoint": csubAggStatsPoint,
       "csubAggStatsSessionType": csubAggStatsSessionType,
       "csubAggStatsPendingSessions": csubAggStatsPendingSessions,
       "csubAggStatsUpSessions": csubAggStatsUpSessions,
       "csubAggStatsAuthSessions": csubAggStatsAuthSessions,
       "csubAggStatsUnAuthSessions": csubAggStatsUnAuthSessions,
       "csubAggStatsLightWeightSessions": csubAggStatsLightWeightSessions,
       "csubAggStatsRedSessions": csubAggStatsRedSessions,
       "csubAggStatsHighUpSessions": csubAggStatsHighUpSessions,
       "csubAggStatsAvgSessionUptime": csubAggStatsAvgSessionUptime,
       "csubAggStatsAvgSessionRPM": csubAggStatsAvgSessionRPM,
       "csubAggStatsAvgSessionRPH": csubAggStatsAvgSessionRPH,
       "csubAggStatsThrottleEngagements": csubAggStatsThrottleEngagements,
       "csubAggStatsTotalCreatedSessions": csubAggStatsTotalCreatedSessions,
       "csubAggStatsTotalFailedSessions": csubAggStatsTotalFailedSessions,
       "csubAggStatsTotalUpSessions": csubAggStatsTotalUpSessions,
       "csubAggStatsTotalAuthSessions": csubAggStatsTotalAuthSessions,
       "csubAggStatsTotalDiscSessions": csubAggStatsTotalDiscSessions,
       "csubAggStatsTotalLightWeightSessions": csubAggStatsTotalLightWeightSessions,
       "csubAggStatsTotalFlowsUp": csubAggStatsTotalFlowsUp,
       "csubAggStatsDayCreatedSessions": csubAggStatsDayCreatedSessions,
       "csubAggStatsDayFailedSessions": csubAggStatsDayFailedSessions,
       "csubAggStatsDayUpSessions": csubAggStatsDayUpSessions,
       "csubAggStatsDayAuthSessions": csubAggStatsDayAuthSessions,
       "csubAggStatsDayDiscSessions": csubAggStatsDayDiscSessions,
       "csubAggStatsCurrTimeElapsed": csubAggStatsCurrTimeElapsed,
       "csubAggStatsCurrValidIntervals": csubAggStatsCurrValidIntervals,
       "csubAggStatsCurrInvalidIntervals": csubAggStatsCurrInvalidIntervals,
       "csubAggStatsCurrFlowsUp": csubAggStatsCurrFlowsUp,
       "csubAggStatsCurrCreatedSessions": csubAggStatsCurrCreatedSessions,
       "csubAggStatsCurrFailedSessions": csubAggStatsCurrFailedSessions,
       "csubAggStatsCurrUpSessions": csubAggStatsCurrUpSessions,
       "csubAggStatsCurrAuthSessions": csubAggStatsCurrAuthSessions,
       "csubAggStatsCurrDiscSessions": csubAggStatsCurrDiscSessions,
       "csubAggStatsDiscontinuityTime": csubAggStatsDiscontinuityTime,
       "csubAggStatsIntTable": csubAggStatsIntTable,
       "csubAggStatsIntEntry": csubAggStatsIntEntry,
       "csubAggStatsIntNumber": csubAggStatsIntNumber,
       "csubAggStatsIntValid": csubAggStatsIntValid,
       "csubAggStatsIntCreatedSessions": csubAggStatsIntCreatedSessions,
       "csubAggStatsIntFailedSessions": csubAggStatsIntFailedSessions,
       "csubAggStatsIntUpSessions": csubAggStatsIntUpSessions,
       "csubAggStatsIntAuthSessions": csubAggStatsIntAuthSessions,
       "csubAggStatsIntDiscSessions": csubAggStatsIntDiscSessions,
       "csubAggStatsThreshTable": csubAggStatsThreshTable,
       "csubAggStatsThreshEntry": csubAggStatsThreshEntry,
       "csubSessionRisingThresh": csubSessionRisingThresh,
       "csubSessionFallingThresh": csubSessionFallingThresh,
       "csubSessionDeltaPercentFallingThresh": csubSessionDeltaPercentFallingThresh,
       "csubSessionThreshEvalInterval": csubSessionThreshEvalInterval,
       "csubJob": csubJob,
       "csubJobFinishedNotifyEnable": csubJobFinishedNotifyEnable,
       "csubJobIndexedAttributes": csubJobIndexedAttributes,
       "csubJobIdNext": csubJobIdNext,
       "csubJobMaxNumber": csubJobMaxNumber,
       "csubJobMaxLife": csubJobMaxLife,
       "csubJobCount": csubJobCount,
       "csubJobTable": csubJobTable,
       "csubJobEntry": csubJobEntry,
       "csubJobId": csubJobId,
       "csubJobStatus": csubJobStatus,
       "csubJobStorage": csubJobStorage,
       "csubJobType": csubJobType,
       "csubJobControl": csubJobControl,
       "csubJobState": csubJobState,
       "csubJobStartedTime": csubJobStartedTime,
       "csubJobFinishedTime": csubJobFinishedTime,
       "csubJobFinishedReason": csubJobFinishedReason,
       "csubJobMatchParamsTable": csubJobMatchParamsTable,
       "csubJobMatchParamsEntry": csubJobMatchParamsEntry,
       "csubJobMatchIdentities": csubJobMatchIdentities,
       "csubJobMatchOtherParams": csubJobMatchOtherParams,
       "csubJobMatchSubscriberLabel": csubJobMatchSubscriberLabel,
       "csubJobMatchMacAddress": csubJobMatchMacAddress,
       "csubJobMatchNativeVrf": csubJobMatchNativeVrf,
       "csubJobMatchNativeIpAddrType": csubJobMatchNativeIpAddrType,
       "csubJobMatchNativeIpAddr": csubJobMatchNativeIpAddr,
       "csubJobMatchNativeIpMask": csubJobMatchNativeIpMask,
       "csubJobMatchDomainVrf": csubJobMatchDomainVrf,
       "csubJobMatchDomainIpAddrType": csubJobMatchDomainIpAddrType,
       "csubJobMatchDomainIpAddr": csubJobMatchDomainIpAddr,
       "csubJobMatchDomainIpMask": csubJobMatchDomainIpMask,
       "csubJobMatchPbhk": csubJobMatchPbhk,
       "csubJobMatchRemoteId": csubJobMatchRemoteId,
       "csubJobMatchCircuitId": csubJobMatchCircuitId,
       "csubJobMatchNasPort": csubJobMatchNasPort,
       "csubJobMatchDomain": csubJobMatchDomain,
       "csubJobMatchUsername": csubJobMatchUsername,
       "csubJobMatchAcctSessionId": csubJobMatchAcctSessionId,
       "csubJobMatchDnis": csubJobMatchDnis,
       "csubJobMatchMedia": csubJobMatchMedia,
       "csubJobMatchMlpNegotiated": csubJobMatchMlpNegotiated,
       "csubJobMatchProtocol": csubJobMatchProtocol,
       "csubJobMatchServiceName": csubJobMatchServiceName,
       "csubJobMatchDhcpClass": csubJobMatchDhcpClass,
       "csubJobMatchTunnelName": csubJobMatchTunnelName,
       "csubJobMatchDanglingDuration": csubJobMatchDanglingDuration,
       "csubJobMatchState": csubJobMatchState,
       "csubJobMatchAuthenticated": csubJobMatchAuthenticated,
       "csubJobMatchRedundancyMode": csubJobMatchRedundancyMode,
       "csubJobQueryParamsTable": csubJobQueryParamsTable,
       "csubJobQueryParamsEntry": csubJobQueryParamsEntry,
       "csubJobQuerySortKey1": csubJobQuerySortKey1,
       "csubJobQuerySortKey2": csubJobQuerySortKey2,
       "csubJobQuerySortKey3": csubJobQuerySortKey3,
       "csubJobQueryResultingReportSize": csubJobQueryResultingReportSize,
       "csubJobQueueTable": csubJobQueueTable,
       "csubJobQueueEntry": csubJobQueueEntry,
       "csubJobQueueNumber": csubJobQueueNumber,
       "csubJobQueueJobId": csubJobQueueJobId,
       "csubJobReportTable": csubJobReportTable,
       "csubJobReportEntry": csubJobReportEntry,
       "csubJobReportId": csubJobReportId,
       "csubJobReportSession": csubJobReportSession,
       "csubAggThresh": csubAggThresh,
       "csubAggStatsThreshNotifEnable": csubAggStatsThreshNotifEnable,
       "ciscoSubscriberSessionMIBConform": ciscoSubscriberSessionMIBConform,
       "ciscoSubscriberSessionMIBCompliances": ciscoSubscriberSessionMIBCompliances,
       "ciscoSubscriberSessionR1Compliance": ciscoSubscriberSessionR1Compliance,
       "ciscoSubscriberSessionR2Compliance": ciscoSubscriberSessionR2Compliance,
       "ciscoSubscriberSessionMIBGroups": ciscoSubscriberSessionMIBGroups,
       "csubSessionGroup": csubSessionGroup,
       "csubAggStatsGroup": csubAggStatsGroup,
       "csubAggStatsCurrGroup": csubAggStatsCurrGroup,
       "csubAggStatsIntGroup": csubAggStatsIntGroup,
       "csubAggStatsDayGroup": csubAggStatsDayGroup,
       "csubJobGroup": csubJobGroup,
       "csubJobMatchParamsGroup": csubJobMatchParamsGroup,
       "csubJobQueryParamsGroup": csubJobQueryParamsGroup,
       "csubJobQueueGroup": csubJobQueueGroup,
       "csubJobNotifGroup": csubJobNotifGroup,
       "csubAggStatsThreshGroup": csubAggStatsThreshGroup,
       "csubAggStatsNotifGroup": csubAggStatsNotifGroup}
)

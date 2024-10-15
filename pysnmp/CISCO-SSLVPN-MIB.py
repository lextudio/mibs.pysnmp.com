# SNMP MIB module (CISCO-SSLVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SSLVPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:49 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSslvpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 829)
)
ciscoSslvpnMIB.setRevisions(
        ("2015-11-17 00:00",
         "2015-10-14 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSslvpnMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSslvpnMIBNotifs = _CiscoSslvpnMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 0)
)
_CiscoSslvpnMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSslvpnMIBObjects = _CiscoSslvpnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1)
)
_CsslvpnGlobalStatistics_ObjectIdentity = ObjectIdentity
csslvpnGlobalStatistics = _CsslvpnGlobalStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1)
)
_CsslvpnMaxSessionAllowed_Type = Unsigned32
_CsslvpnMaxSessionAllowed_Object = MibScalar
csslvpnMaxSessionAllowed = _CsslvpnMaxSessionAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 1),
    _CsslvpnMaxSessionAllowed_Type()
)
csslvpnMaxSessionAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnMaxSessionAllowed.setStatus("current")
_CsslvpnActiveSessions_Type = Unsigned32
_CsslvpnActiveSessions_Object = MibScalar
csslvpnActiveSessions = _CsslvpnActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 2),
    _CsslvpnActiveSessions_Type()
)
csslvpnActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnActiveSessions.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnActiveSessions.setUnits("sessions")
_CsslvpnPeakSessions_Type = Unsigned32
_CsslvpnPeakSessions_Object = MibScalar
csslvpnPeakSessions = _CsslvpnPeakSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 3),
    _CsslvpnPeakSessions_Type()
)
csslvpnPeakSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnPeakSessions.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnPeakSessions.setUnits("sessions")
_CsslvpnInControlPackets_Type = Counter64
_CsslvpnInControlPackets_Object = MibScalar
csslvpnInControlPackets = _CsslvpnInControlPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 4),
    _CsslvpnInControlPackets_Type()
)
csslvpnInControlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnInControlPackets.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnInControlPackets.setUnits("packets")
_CsslvpnInDataPackets_Type = Counter64
_CsslvpnInDataPackets_Object = MibScalar
csslvpnInDataPackets = _CsslvpnInDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 5),
    _CsslvpnInDataPackets_Type()
)
csslvpnInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnInDataPackets.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnInDataPackets.setUnits("packets")
_CsslvpnOutControlPackets_Type = Counter64
_CsslvpnOutControlPackets_Object = MibScalar
csslvpnOutControlPackets = _CsslvpnOutControlPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 6),
    _CsslvpnOutControlPackets_Type()
)
csslvpnOutControlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnOutControlPackets.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnOutControlPackets.setUnits("packets")
_CsslvpnOutDataPackets_Type = Counter64
_CsslvpnOutDataPackets_Object = MibScalar
csslvpnOutDataPackets = _CsslvpnOutDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 7),
    _CsslvpnOutDataPackets_Type()
)
csslvpnOutDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnOutDataPackets.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnOutDataPackets.setUnits("packets")
_CsslvpnAuthFailures_Type = Unsigned32
_CsslvpnAuthFailures_Object = MibScalar
csslvpnAuthFailures = _CsslvpnAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 8),
    _CsslvpnAuthFailures_Type()
)
csslvpnAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnAuthFailures.setStatus("current")
_CsslvpnConnectFailures_Type = Unsigned32
_CsslvpnConnectFailures_Object = MibScalar
csslvpnConnectFailures = _CsslvpnConnectFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 9),
    _CsslvpnConnectFailures_Type()
)
csslvpnConnectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnConnectFailures.setStatus("current")
_CsslvpnReconnectFailures_Type = Unsigned32
_CsslvpnReconnectFailures_Object = MibScalar
csslvpnReconnectFailures = _CsslvpnReconnectFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 10),
    _CsslvpnReconnectFailures_Type()
)
csslvpnReconnectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnReconnectFailures.setStatus("current")
_CsslvpnDpdTimeouts_Type = Counter64
_CsslvpnDpdTimeouts_Object = MibScalar
csslvpnDpdTimeouts = _CsslvpnDpdTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 11),
    _CsslvpnDpdTimeouts_Type()
)
csslvpnDpdTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnDpdTimeouts.setStatus("current")
_CsslvpnAuthRequests_Type = Counter64
_CsslvpnAuthRequests_Object = MibScalar
csslvpnAuthRequests = _CsslvpnAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 12),
    _CsslvpnAuthRequests_Type()
)
csslvpnAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnAuthRequests.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnAuthRequests.setUnits("requests")
_CsslvpnAuthResponses_Type = Counter64
_CsslvpnAuthResponses_Object = MibScalar
csslvpnAuthResponses = _CsslvpnAuthResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 13),
    _CsslvpnAuthResponses_Type()
)
csslvpnAuthResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnAuthResponses.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnAuthResponses.setUnits("responses")
_CsslvpnInDpdRequests_Type = Counter64
_CsslvpnInDpdRequests_Object = MibScalar
csslvpnInDpdRequests = _CsslvpnInDpdRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 14),
    _CsslvpnInDpdRequests_Type()
)
csslvpnInDpdRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnInDpdRequests.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnInDpdRequests.setUnits("requests")
_CsslvpnOutDpdRequests_Type = Counter64
_CsslvpnOutDpdRequests_Object = MibScalar
csslvpnOutDpdRequests = _CsslvpnOutDpdRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 15),
    _CsslvpnOutDpdRequests_Type()
)
csslvpnOutDpdRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnOutDpdRequests.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnOutDpdRequests.setUnits("requests")
_CsslvpnInDpdResponses_Type = Counter64
_CsslvpnInDpdResponses_Object = MibScalar
csslvpnInDpdResponses = _CsslvpnInDpdResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 16),
    _CsslvpnInDpdResponses_Type()
)
csslvpnInDpdResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnInDpdResponses.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnInDpdResponses.setUnits("responses")
_CsslvpnOutDpdResponses_Type = Counter64
_CsslvpnOutDpdResponses_Object = MibScalar
csslvpnOutDpdResponses = _CsslvpnOutDpdResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 1, 17),
    _CsslvpnOutDpdResponses_Type()
)
csslvpnOutDpdResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnOutDpdResponses.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnOutDpdResponses.setUnits("responses")
_CsslvpnSession_ObjectIdentity = ObjectIdentity
csslvpnSession = _CsslvpnSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2)
)
_CsslvpnSessionTable_Object = MibTable
csslvpnSessionTable = _CsslvpnSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1)
)
if mibBuilder.loadTexts:
    csslvpnSessionTable.setStatus("current")
_CsslvpnSessionEntry_Object = MibTableRow
csslvpnSessionEntry = _CsslvpnSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1)
)
csslvpnSessionEntry.setIndexNames(
    (0, "CISCO-SSLVPN-MIB", "csslvpnSessionID"),
)
if mibBuilder.loadTexts:
    csslvpnSessionEntry.setStatus("current")


class _CsslvpnSessionID_Type(Unsigned32):
    """Custom type csslvpnSessionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CsslvpnSessionID_Type.__name__ = "Unsigned32"
_CsslvpnSessionID_Object = MibTableColumn
csslvpnSessionID = _CsslvpnSessionID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 1),
    _CsslvpnSessionID_Type()
)
csslvpnSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csslvpnSessionID.setStatus("current")
_CsslvpnSessionUser_Type = SnmpAdminString
_CsslvpnSessionUser_Object = MibTableColumn
csslvpnSessionUser = _CsslvpnSessionUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 2),
    _CsslvpnSessionUser_Type()
)
csslvpnSessionUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionUser.setStatus("current")
_CsslvpnSessionProfile_Type = SnmpAdminString
_CsslvpnSessionProfile_Object = MibTableColumn
csslvpnSessionProfile = _CsslvpnSessionProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 3),
    _CsslvpnSessionProfile_Type()
)
csslvpnSessionProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionProfile.setStatus("current")
_CsslvpnSessionPolicy_Type = SnmpAdminString
_CsslvpnSessionPolicy_Object = MibTableColumn
csslvpnSessionPolicy = _CsslvpnSessionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 4),
    _CsslvpnSessionPolicy_Type()
)
csslvpnSessionPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionPolicy.setStatus("current")
_CsslvpnSessionClientIpAddrType_Type = InetAddressType
_CsslvpnSessionClientIpAddrType_Object = MibTableColumn
csslvpnSessionClientIpAddrType = _CsslvpnSessionClientIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 5),
    _CsslvpnSessionClientIpAddrType_Type()
)
csslvpnSessionClientIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionClientIpAddrType.setStatus("current")
_CsslvpnSessionClientIpAddr_Type = InetAddress
_CsslvpnSessionClientIpAddr_Object = MibTableColumn
csslvpnSessionClientIpAddr = _CsslvpnSessionClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 6),
    _CsslvpnSessionClientIpAddr_Type()
)
csslvpnSessionClientIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionClientIpAddr.setStatus("current")
_CsslvpnSessionTunnelIpAddrType_Type = InetAddressType
_CsslvpnSessionTunnelIpAddrType_Object = MibTableColumn
csslvpnSessionTunnelIpAddrType = _CsslvpnSessionTunnelIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 7),
    _CsslvpnSessionTunnelIpAddrType_Type()
)
csslvpnSessionTunnelIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionTunnelIpAddrType.setStatus("current")
_CsslvpnSessionTunnelIpAddr_Type = InetAddress
_CsslvpnSessionTunnelIpAddr_Object = MibTableColumn
csslvpnSessionTunnelIpAddr = _CsslvpnSessionTunnelIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 8),
    _CsslvpnSessionTunnelIpAddr_Type()
)
csslvpnSessionTunnelIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionTunnelIpAddr.setStatus("current")
_CsslvpnSessionTunnelNetmask_Type = InetAddressPrefixLength
_CsslvpnSessionTunnelNetmask_Object = MibTableColumn
csslvpnSessionTunnelNetmask = _CsslvpnSessionTunnelNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 9),
    _CsslvpnSessionTunnelNetmask_Type()
)
csslvpnSessionTunnelNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionTunnelNetmask.setStatus("current")
_CsslvpnSessionNumConnections_Type = Unsigned32
_CsslvpnSessionNumConnections_Object = MibTableColumn
csslvpnSessionNumConnections = _CsslvpnSessionNumConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 10),
    _CsslvpnSessionNumConnections_Type()
)
csslvpnSessionNumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionNumConnections.setStatus("current")
_CsslvpnSessionRxPackets_Type = Counter64
_CsslvpnSessionRxPackets_Object = MibTableColumn
csslvpnSessionRxPackets = _CsslvpnSessionRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 11),
    _CsslvpnSessionRxPackets_Type()
)
csslvpnSessionRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionRxPackets.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnSessionRxPackets.setUnits("packets")
_CsslvpnSessionTxPackets_Type = Counter64
_CsslvpnSessionTxPackets_Object = MibTableColumn
csslvpnSessionTxPackets = _CsslvpnSessionTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 12),
    _CsslvpnSessionTxPackets_Type()
)
csslvpnSessionTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionTxPackets.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnSessionTxPackets.setUnits("packets")
_CsslvpnSessionRxBytes_Type = Counter64
_CsslvpnSessionRxBytes_Object = MibTableColumn
csslvpnSessionRxBytes = _CsslvpnSessionRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 13),
    _CsslvpnSessionRxBytes_Type()
)
csslvpnSessionRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnSessionRxBytes.setUnits("bytes")
_CsslvpnSessionTxBytes_Type = Counter64
_CsslvpnSessionTxBytes_Object = MibTableColumn
csslvpnSessionTxBytes = _CsslvpnSessionTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 14),
    _CsslvpnSessionTxBytes_Type()
)
csslvpnSessionTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    csslvpnSessionTxBytes.setUnits("bytes")
_CsslvpnSessionLastUsed_Type = DateAndTime
_CsslvpnSessionLastUsed_Object = MibTableColumn
csslvpnSessionLastUsed = _CsslvpnSessionLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 15),
    _CsslvpnSessionLastUsed_Type()
)
csslvpnSessionLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionLastUsed.setStatus("current")
_CsslvpnSessionCreated_Type = DateAndTime
_CsslvpnSessionCreated_Object = MibTableColumn
csslvpnSessionCreated = _CsslvpnSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 2, 1, 1, 16),
    _CsslvpnSessionCreated_Type()
)
csslvpnSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csslvpnSessionCreated.setStatus("current")
_CsslvpnNotificationControl_ObjectIdentity = ObjectIdentity
csslvpnNotificationControl = _CsslvpnNotificationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 3)
)


class _CsslvpnNotificationEnable_Type(Bits):
    """Custom type csslvpnNotificationEnable based on Bits"""
    namedValues = NamedValues(
        *(("sessionLimit", 0),
          ("tunnelDown", 2),
          ("tunnelUp", 1))
    )

_CsslvpnNotificationEnable_Type.__name__ = "Bits"
_CsslvpnNotificationEnable_Object = MibScalar
csslvpnNotificationEnable = _CsslvpnNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 1, 3, 1),
    _CsslvpnNotificationEnable_Type()
)
csslvpnNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csslvpnNotificationEnable.setStatus("current")
_CiscoSslvpnMIBConform_ObjectIdentity = ObjectIdentity
ciscoSslvpnMIBConform = _CiscoSslvpnMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 2)
)
_CiscoSslvpnMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSslvpnMIBCompliances = _CiscoSslvpnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 2, 1)
)
_CiscoSslvpnMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSslvpnMIBGroups = _CiscoSslvpnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 2, 2)
)

# Managed Objects groups

csslvpnGlobalSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 2, 2, 1)
)
csslvpnGlobalSessionGroup.setObjects(
      *(("CISCO-SSLVPN-MIB", "csslvpnMaxSessionAllowed"),
        ("CISCO-SSLVPN-MIB", "csslvpnActiveSessions"),
        ("CISCO-SSLVPN-MIB", "csslvpnPeakSessions"))
)
if mibBuilder.loadTexts:
    csslvpnGlobalSessionGroup.setStatus("current")

csslvpnStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 2, 2, 2)
)
csslvpnStatisticsGroup.setObjects(
      *(("CISCO-SSLVPN-MIB", "csslvpnInControlPackets"),
        ("CISCO-SSLVPN-MIB", "csslvpnInDataPackets"),
        ("CISCO-SSLVPN-MIB", "csslvpnOutControlPackets"),
        ("CISCO-SSLVPN-MIB", "csslvpnOutDataPackets"),
        ("CISCO-SSLVPN-MIB", "csslvpnAuthFailures"),
        ("CISCO-SSLVPN-MIB", "csslvpnConnectFailures"),
        ("CISCO-SSLVPN-MIB", "csslvpnReconnectFailures"),
        ("CISCO-SSLVPN-MIB", "csslvpnDpdTimeouts"),
        ("CISCO-SSLVPN-MIB", "csslvpnAuthRequests"),
        ("CISCO-SSLVPN-MIB", "csslvpnAuthResponses"),
        ("CISCO-SSLVPN-MIB", "csslvpnInDpdRequests"),
        ("CISCO-SSLVPN-MIB", "csslvpnOutDpdRequests"),
        ("CISCO-SSLVPN-MIB", "csslvpnInDpdResponses"),
        ("CISCO-SSLVPN-MIB", "csslvpnOutDpdResponses"))
)
if mibBuilder.loadTexts:
    csslvpnStatisticsGroup.setStatus("current")

csslvpnSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 2, 2, 3)
)
csslvpnSessionGroup.setObjects(
      *(("CISCO-SSLVPN-MIB", "csslvpnSessionUser"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionProfile"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionPolicy"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionClientIpAddrType"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionClientIpAddr"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionTunnelIpAddrType"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionTunnelIpAddr"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionTunnelNetmask"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionNumConnections"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionRxPackets"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionTxPackets"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionRxBytes"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionTxBytes"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionLastUsed"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionCreated"))
)
if mibBuilder.loadTexts:
    csslvpnSessionGroup.setStatus("current")

csslvpnNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 2, 2, 5)
)
csslvpnNotificationControlGroup.setObjects(
    ("CISCO-SSLVPN-MIB", "csslvpnNotificationEnable")
)
if mibBuilder.loadTexts:
    csslvpnNotificationControlGroup.setStatus("current")


# Notification objects

csslvpnSessionLimitNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 0, 1)
)
csslvpnSessionLimitNotif.setObjects(
    ("CISCO-SSLVPN-MIB", "csslvpnMaxSessionAllowed")
)
if mibBuilder.loadTexts:
    csslvpnSessionLimitNotif.setStatus(
        "current"
    )

csslvpnTunnelUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 0, 2)
)
csslvpnTunnelUpNotif.setObjects(
      *(("CISCO-SSLVPN-MIB", "csslvpnSessionUser"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionTunnelIpAddrType"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionTunnelIpAddr"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionTunnelNetmask"))
)
if mibBuilder.loadTexts:
    csslvpnTunnelUpNotif.setStatus(
        "current"
    )

csslvpnTunnelDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 0, 3)
)
csslvpnTunnelDownNotif.setObjects(
      *(("CISCO-SSLVPN-MIB", "csslvpnSessionUser"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionTunnelIpAddrType"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionTunnelIpAddr"),
        ("CISCO-SSLVPN-MIB", "csslvpnSessionTunnelNetmask"))
)
if mibBuilder.loadTexts:
    csslvpnTunnelDownNotif.setStatus(
        "current"
    )


# Notifications groups

csslvpnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 2, 2, 4)
)
csslvpnNotificationGroup.setObjects(
      *(("CISCO-SSLVPN-MIB", "csslvpnSessionLimitNotif"),
        ("CISCO-SSLVPN-MIB", "csslvpnTunnelUpNotif"),
        ("CISCO-SSLVPN-MIB", "csslvpnTunnelDownNotif"))
)
if mibBuilder.loadTexts:
    csslvpnNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSslvpnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 829, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSslvpnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SSLVPN-MIB",
    **{"ciscoSslvpnMIB": ciscoSslvpnMIB,
       "ciscoSslvpnMIBNotifs": ciscoSslvpnMIBNotifs,
       "csslvpnSessionLimitNotif": csslvpnSessionLimitNotif,
       "csslvpnTunnelUpNotif": csslvpnTunnelUpNotif,
       "csslvpnTunnelDownNotif": csslvpnTunnelDownNotif,
       "ciscoSslvpnMIBObjects": ciscoSslvpnMIBObjects,
       "csslvpnGlobalStatistics": csslvpnGlobalStatistics,
       "csslvpnMaxSessionAllowed": csslvpnMaxSessionAllowed,
       "csslvpnActiveSessions": csslvpnActiveSessions,
       "csslvpnPeakSessions": csslvpnPeakSessions,
       "csslvpnInControlPackets": csslvpnInControlPackets,
       "csslvpnInDataPackets": csslvpnInDataPackets,
       "csslvpnOutControlPackets": csslvpnOutControlPackets,
       "csslvpnOutDataPackets": csslvpnOutDataPackets,
       "csslvpnAuthFailures": csslvpnAuthFailures,
       "csslvpnConnectFailures": csslvpnConnectFailures,
       "csslvpnReconnectFailures": csslvpnReconnectFailures,
       "csslvpnDpdTimeouts": csslvpnDpdTimeouts,
       "csslvpnAuthRequests": csslvpnAuthRequests,
       "csslvpnAuthResponses": csslvpnAuthResponses,
       "csslvpnInDpdRequests": csslvpnInDpdRequests,
       "csslvpnOutDpdRequests": csslvpnOutDpdRequests,
       "csslvpnInDpdResponses": csslvpnInDpdResponses,
       "csslvpnOutDpdResponses": csslvpnOutDpdResponses,
       "csslvpnSession": csslvpnSession,
       "csslvpnSessionTable": csslvpnSessionTable,
       "csslvpnSessionEntry": csslvpnSessionEntry,
       "csslvpnSessionID": csslvpnSessionID,
       "csslvpnSessionUser": csslvpnSessionUser,
       "csslvpnSessionProfile": csslvpnSessionProfile,
       "csslvpnSessionPolicy": csslvpnSessionPolicy,
       "csslvpnSessionClientIpAddrType": csslvpnSessionClientIpAddrType,
       "csslvpnSessionClientIpAddr": csslvpnSessionClientIpAddr,
       "csslvpnSessionTunnelIpAddrType": csslvpnSessionTunnelIpAddrType,
       "csslvpnSessionTunnelIpAddr": csslvpnSessionTunnelIpAddr,
       "csslvpnSessionTunnelNetmask": csslvpnSessionTunnelNetmask,
       "csslvpnSessionNumConnections": csslvpnSessionNumConnections,
       "csslvpnSessionRxPackets": csslvpnSessionRxPackets,
       "csslvpnSessionTxPackets": csslvpnSessionTxPackets,
       "csslvpnSessionRxBytes": csslvpnSessionRxBytes,
       "csslvpnSessionTxBytes": csslvpnSessionTxBytes,
       "csslvpnSessionLastUsed": csslvpnSessionLastUsed,
       "csslvpnSessionCreated": csslvpnSessionCreated,
       "csslvpnNotificationControl": csslvpnNotificationControl,
       "csslvpnNotificationEnable": csslvpnNotificationEnable,
       "ciscoSslvpnMIBConform": ciscoSslvpnMIBConform,
       "ciscoSslvpnMIBCompliances": ciscoSslvpnMIBCompliances,
       "ciscoSslvpnMIBCompliance": ciscoSslvpnMIBCompliance,
       "ciscoSslvpnMIBGroups": ciscoSslvpnMIBGroups,
       "csslvpnGlobalSessionGroup": csslvpnGlobalSessionGroup,
       "csslvpnStatisticsGroup": csslvpnStatisticsGroup,
       "csslvpnSessionGroup": csslvpnSessionGroup,
       "csslvpnNotificationGroup": csslvpnNotificationGroup,
       "csslvpnNotificationControlGroup": csslvpnNotificationControlGroup}
)

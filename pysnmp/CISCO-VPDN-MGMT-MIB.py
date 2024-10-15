# SNMP MIB module (CISCO-VPDN-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VPDN-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:34 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoVpdnMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24)
)
ciscoVpdnMgmtMIB.setRevisions(
        ("2006-01-20 00:00",
         "2004-06-08 00:00",
         "2004-04-02 00:00",
         "2002-07-08 00:00",
         "2002-05-17 00:00",
         "2002-04-02 00:00",
         "2000-01-12 00:00",
         "1999-03-24 00:00",
         "1997-07-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TunnelType(Integer32, TextualConvention):
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
        *(("l2f", 1),
          ("l2tp", 2),
          ("pptp", 3))
    )



class EndpointClass(Integer32, TextualConvention):
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
        *(("ipV4Address", 3),
          ("local", 2),
          ("macAddress", 4),
          ("magicNumber", 5),
          ("none", 1),
          ("phone", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVpdnMgmtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVpdnMgmtMIBNotifs = _CiscoVpdnMgmtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 0)
)


class _CvpdnNotifSessionID_Type(Integer32):
    """Custom type cvpdnNotifSessionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvpdnNotifSessionID_Type.__name__ = "Integer32"
_CvpdnNotifSessionID_Object = MibScalar
cvpdnNotifSessionID = _CvpdnNotifSessionID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 0, 1),
    _CvpdnNotifSessionID_Type()
)
cvpdnNotifSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnNotifSessionID.setStatus("current")


class _CvpdnNotifSessionEvent_Type(Integer32):
    """Custom type cvpdnNotifSessionEvent based on Integer32"""
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
        *(("down", 2),
          ("pwDown", 4),
          ("pwUp", 3),
          ("up", 1))
    )


_CvpdnNotifSessionEvent_Type.__name__ = "Integer32"
_CvpdnNotifSessionEvent_Object = MibScalar
cvpdnNotifSessionEvent = _CvpdnNotifSessionEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 0, 2),
    _CvpdnNotifSessionEvent_Type()
)
cvpdnNotifSessionEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnNotifSessionEvent.setStatus("current")
_CiscoVpdnMgmtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVpdnMgmtMIBObjects = _CiscoVpdnMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1)
)
_CvpdnSystemInfo_ObjectIdentity = ObjectIdentity
cvpdnSystemInfo = _CvpdnSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1)
)
_CvpdnTunnelTotal_Type = Gauge32
_CvpdnTunnelTotal_Object = MibScalar
cvpdnTunnelTotal = _CvpdnTunnelTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 1),
    _CvpdnTunnelTotal_Type()
)
cvpdnTunnelTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelTotal.setStatus("obsolete")
if mibBuilder.loadTexts:
    cvpdnTunnelTotal.setUnits("tunnels")
_CvpdnSessionTotal_Type = Gauge32
_CvpdnSessionTotal_Object = MibScalar
cvpdnSessionTotal = _CvpdnSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 2),
    _CvpdnSessionTotal_Type()
)
cvpdnSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionTotal.setStatus("obsolete")
if mibBuilder.loadTexts:
    cvpdnSessionTotal.setUnits("users")
_CvpdnDeniedUsersTotal_Type = Counter32
_CvpdnDeniedUsersTotal_Object = MibScalar
cvpdnDeniedUsersTotal = _CvpdnDeniedUsersTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 3),
    _CvpdnDeniedUsersTotal_Type()
)
cvpdnDeniedUsersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnDeniedUsersTotal.setStatus("obsolete")
if mibBuilder.loadTexts:
    cvpdnDeniedUsersTotal.setUnits("attempts")
_CvpdnSystemTable_Object = MibTable
cvpdnSystemTable = _CvpdnSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cvpdnSystemTable.setStatus("current")
_CvpdnSystemEntry_Object = MibTableRow
cvpdnSystemEntry = _CvpdnSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 4, 1)
)
cvpdnSystemEntry.setIndexNames(
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnSystemTunnelType"),
)
if mibBuilder.loadTexts:
    cvpdnSystemEntry.setStatus("current")
_CvpdnSystemTunnelType_Type = TunnelType
_CvpdnSystemTunnelType_Object = MibTableColumn
cvpdnSystemTunnelType = _CvpdnSystemTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 4, 1, 1),
    _CvpdnSystemTunnelType_Type()
)
cvpdnSystemTunnelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpdnSystemTunnelType.setStatus("current")
_CvpdnSystemTunnelTotal_Type = Gauge32
_CvpdnSystemTunnelTotal_Object = MibTableColumn
cvpdnSystemTunnelTotal = _CvpdnSystemTunnelTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 4, 1, 2),
    _CvpdnSystemTunnelTotal_Type()
)
cvpdnSystemTunnelTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSystemTunnelTotal.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSystemTunnelTotal.setUnits("tunnels")
_CvpdnSystemSessionTotal_Type = Gauge32
_CvpdnSystemSessionTotal_Object = MibTableColumn
cvpdnSystemSessionTotal = _CvpdnSystemSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 4, 1, 3),
    _CvpdnSystemSessionTotal_Type()
)
cvpdnSystemSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSystemSessionTotal.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSystemSessionTotal.setUnits("sessions")
_CvpdnSystemDeniedUsersTotal_Type = Counter32
_CvpdnSystemDeniedUsersTotal_Object = MibTableColumn
cvpdnSystemDeniedUsersTotal = _CvpdnSystemDeniedUsersTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 4, 1, 4),
    _CvpdnSystemDeniedUsersTotal_Type()
)
cvpdnSystemDeniedUsersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSystemDeniedUsersTotal.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSystemDeniedUsersTotal.setUnits("attempts")
_CvpdnSystemInitialConnReq_Type = Counter32
_CvpdnSystemInitialConnReq_Object = MibTableColumn
cvpdnSystemInitialConnReq = _CvpdnSystemInitialConnReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 4, 1, 5),
    _CvpdnSystemInitialConnReq_Type()
)
cvpdnSystemInitialConnReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSystemInitialConnReq.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSystemInitialConnReq.setUnits("attempts")
_CvpdnSystemSuccessConnReq_Type = Counter32
_CvpdnSystemSuccessConnReq_Object = MibTableColumn
cvpdnSystemSuccessConnReq = _CvpdnSystemSuccessConnReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 4, 1, 6),
    _CvpdnSystemSuccessConnReq_Type()
)
cvpdnSystemSuccessConnReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSystemSuccessConnReq.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSystemSuccessConnReq.setUnits("attempts")
_CvpdnSystemFailedConnReq_Type = Counter32
_CvpdnSystemFailedConnReq_Object = MibTableColumn
cvpdnSystemFailedConnReq = _CvpdnSystemFailedConnReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 4, 1, 7),
    _CvpdnSystemFailedConnReq_Type()
)
cvpdnSystemFailedConnReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSystemFailedConnReq.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSystemFailedConnReq.setUnits("attempts")


class _CvpdnSystemNotifSessionEnabled_Type(TruthValue):
    """Custom type cvpdnSystemNotifSessionEnabled based on TruthValue"""


_CvpdnSystemNotifSessionEnabled_Object = MibScalar
cvpdnSystemNotifSessionEnabled = _CvpdnSystemNotifSessionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 5),
    _CvpdnSystemNotifSessionEnabled_Type()
)
cvpdnSystemNotifSessionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSystemNotifSessionEnabled.setStatus("current")


class _CvpdnSystemClearSessions_Type(Integer32):
    """Custom type cvpdnSystemClearSessions based on Integer32"""
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
        *(("all", 2),
          ("l2f", 3),
          ("l2tp", 4),
          ("none", 1),
          ("pptp", 5))
    )


_CvpdnSystemClearSessions_Type.__name__ = "Integer32"
_CvpdnSystemClearSessions_Object = MibScalar
cvpdnSystemClearSessions = _CvpdnSystemClearSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 1, 6),
    _CvpdnSystemClearSessions_Type()
)
cvpdnSystemClearSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvpdnSystemClearSessions.setStatus("current")
_CvpdnTunnelInfo_ObjectIdentity = ObjectIdentity
cvpdnTunnelInfo = _CvpdnTunnelInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2)
)
_CvpdnTunnelTable_Object = MibTable
cvpdnTunnelTable = _CvpdnTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvpdnTunnelTable.setStatus("obsolete")
_CvpdnTunnelEntry_Object = MibTableRow
cvpdnTunnelEntry = _CvpdnTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1)
)
cvpdnTunnelEntry.setIndexNames(
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnTunnelTunnelId"),
)
if mibBuilder.loadTexts:
    cvpdnTunnelEntry.setStatus("obsolete")
_CvpdnTunnelTunnelId_Type = Unsigned32
_CvpdnTunnelTunnelId_Object = MibTableColumn
cvpdnTunnelTunnelId = _CvpdnTunnelTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 1),
    _CvpdnTunnelTunnelId_Type()
)
cvpdnTunnelTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpdnTunnelTunnelId.setStatus("obsolete")
_CvpdnTunnelRemoteTunnelId_Type = Unsigned32
_CvpdnTunnelRemoteTunnelId_Object = MibTableColumn
cvpdnTunnelRemoteTunnelId = _CvpdnTunnelRemoteTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 2),
    _CvpdnTunnelRemoteTunnelId_Type()
)
cvpdnTunnelRemoteTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelRemoteTunnelId.setStatus("obsolete")


class _CvpdnTunnelLocalName_Type(DisplayString):
    """Custom type cvpdnTunnelLocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnTunnelLocalName_Type.__name__ = "DisplayString"
_CvpdnTunnelLocalName_Object = MibTableColumn
cvpdnTunnelLocalName = _CvpdnTunnelLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 3),
    _CvpdnTunnelLocalName_Type()
)
cvpdnTunnelLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelLocalName.setStatus("obsolete")


class _CvpdnTunnelRemoteName_Type(DisplayString):
    """Custom type cvpdnTunnelRemoteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnTunnelRemoteName_Type.__name__ = "DisplayString"
_CvpdnTunnelRemoteName_Object = MibTableColumn
cvpdnTunnelRemoteName = _CvpdnTunnelRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 4),
    _CvpdnTunnelRemoteName_Type()
)
cvpdnTunnelRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelRemoteName.setStatus("obsolete")


class _CvpdnTunnelRemoteEndpointName_Type(DisplayString):
    """Custom type cvpdnTunnelRemoteEndpointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnTunnelRemoteEndpointName_Type.__name__ = "DisplayString"
_CvpdnTunnelRemoteEndpointName_Object = MibTableColumn
cvpdnTunnelRemoteEndpointName = _CvpdnTunnelRemoteEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 5),
    _CvpdnTunnelRemoteEndpointName_Type()
)
cvpdnTunnelRemoteEndpointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelRemoteEndpointName.setStatus("obsolete")
_CvpdnTunnelLocalInitConnection_Type = TruthValue
_CvpdnTunnelLocalInitConnection_Object = MibTableColumn
cvpdnTunnelLocalInitConnection = _CvpdnTunnelLocalInitConnection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 6),
    _CvpdnTunnelLocalInitConnection_Type()
)
cvpdnTunnelLocalInitConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelLocalInitConnection.setStatus("obsolete")


class _CvpdnTunnelOrigCause_Type(Integer32):
    """Custom type cvpdnTunnelOrigCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dnis", 2),
          ("domain", 1),
          ("stack", 3))
    )


_CvpdnTunnelOrigCause_Type.__name__ = "Integer32"
_CvpdnTunnelOrigCause_Object = MibTableColumn
cvpdnTunnelOrigCause = _CvpdnTunnelOrigCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 7),
    _CvpdnTunnelOrigCause_Type()
)
cvpdnTunnelOrigCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelOrigCause.setStatus("obsolete")


class _CvpdnTunnelState_Type(Integer32):
    """Custom type cvpdnTunnelState based on Integer32"""
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
        *(("closing", 4),
          ("open", 3),
          ("opening", 2),
          ("unknown", 1))
    )


_CvpdnTunnelState_Type.__name__ = "Integer32"
_CvpdnTunnelState_Object = MibTableColumn
cvpdnTunnelState = _CvpdnTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 8),
    _CvpdnTunnelState_Type()
)
cvpdnTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelState.setStatus("obsolete")
_CvpdnTunnelActiveSessions_Type = Gauge32
_CvpdnTunnelActiveSessions_Object = MibTableColumn
cvpdnTunnelActiveSessions = _CvpdnTunnelActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 9),
    _CvpdnTunnelActiveSessions_Type()
)
cvpdnTunnelActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelActiveSessions.setStatus("obsolete")
if mibBuilder.loadTexts:
    cvpdnTunnelActiveSessions.setUnits("sessions")
_CvpdnTunnelDeniedUsers_Type = Counter32
_CvpdnTunnelDeniedUsers_Object = MibTableColumn
cvpdnTunnelDeniedUsers = _CvpdnTunnelDeniedUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 10),
    _CvpdnTunnelDeniedUsers_Type()
)
cvpdnTunnelDeniedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelDeniedUsers.setStatus("obsolete")
if mibBuilder.loadTexts:
    cvpdnTunnelDeniedUsers.setUnits("calls")
_CvpdnTunnelSoftshut_Type = TruthValue
_CvpdnTunnelSoftshut_Object = MibTableColumn
cvpdnTunnelSoftshut = _CvpdnTunnelSoftshut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 12),
    _CvpdnTunnelSoftshut_Type()
)
cvpdnTunnelSoftshut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSoftshut.setStatus("obsolete")


class _CvpdnTunnelNetworkServiceType_Type(Integer32):
    """Custom type cvpdnTunnelNetworkServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_CvpdnTunnelNetworkServiceType_Type.__name__ = "Integer32"
_CvpdnTunnelNetworkServiceType_Object = MibTableColumn
cvpdnTunnelNetworkServiceType = _CvpdnTunnelNetworkServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 13),
    _CvpdnTunnelNetworkServiceType_Type()
)
cvpdnTunnelNetworkServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelNetworkServiceType.setStatus("obsolete")
_CvpdnTunnelLocalIpAddress_Type = IpAddress
_CvpdnTunnelLocalIpAddress_Object = MibTableColumn
cvpdnTunnelLocalIpAddress = _CvpdnTunnelLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 14),
    _CvpdnTunnelLocalIpAddress_Type()
)
cvpdnTunnelLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelLocalIpAddress.setStatus("obsolete")
_CvpdnTunnelSourceIpAddress_Type = IpAddress
_CvpdnTunnelSourceIpAddress_Object = MibTableColumn
cvpdnTunnelSourceIpAddress = _CvpdnTunnelSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 15),
    _CvpdnTunnelSourceIpAddress_Type()
)
cvpdnTunnelSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSourceIpAddress.setStatus("obsolete")
_CvpdnTunnelRemoteIpAddress_Type = IpAddress
_CvpdnTunnelRemoteIpAddress_Object = MibTableColumn
cvpdnTunnelRemoteIpAddress = _CvpdnTunnelRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 1, 1, 16),
    _CvpdnTunnelRemoteIpAddress_Type()
)
cvpdnTunnelRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelRemoteIpAddress.setStatus("obsolete")
_CvpdnTunnelAttrTable_Object = MibTable
cvpdnTunnelAttrTable = _CvpdnTunnelAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cvpdnTunnelAttrTable.setStatus("current")
_CvpdnTunnelAttrEntry_Object = MibTableRow
cvpdnTunnelAttrEntry = _CvpdnTunnelAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1)
)
cvpdnTunnelAttrEntry.setIndexNames(
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnSystemTunnelType"),
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrTunnelId"),
)
if mibBuilder.loadTexts:
    cvpdnTunnelAttrEntry.setStatus("current")


class _CvpdnTunnelAttrTunnelId_Type(Integer32):
    """Custom type cvpdnTunnelAttrTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvpdnTunnelAttrTunnelId_Type.__name__ = "Integer32"
_CvpdnTunnelAttrTunnelId_Object = MibTableColumn
cvpdnTunnelAttrTunnelId = _CvpdnTunnelAttrTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 1),
    _CvpdnTunnelAttrTunnelId_Type()
)
cvpdnTunnelAttrTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrTunnelId.setStatus("current")


class _CvpdnTunnelAttrRemoteTunnelId_Type(Integer32):
    """Custom type cvpdnTunnelAttrRemoteTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvpdnTunnelAttrRemoteTunnelId_Type.__name__ = "Integer32"
_CvpdnTunnelAttrRemoteTunnelId_Object = MibTableColumn
cvpdnTunnelAttrRemoteTunnelId = _CvpdnTunnelAttrRemoteTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 2),
    _CvpdnTunnelAttrRemoteTunnelId_Type()
)
cvpdnTunnelAttrRemoteTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrRemoteTunnelId.setStatus("current")


class _CvpdnTunnelAttrLocalName_Type(DisplayString):
    """Custom type cvpdnTunnelAttrLocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnTunnelAttrLocalName_Type.__name__ = "DisplayString"
_CvpdnTunnelAttrLocalName_Object = MibTableColumn
cvpdnTunnelAttrLocalName = _CvpdnTunnelAttrLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 3),
    _CvpdnTunnelAttrLocalName_Type()
)
cvpdnTunnelAttrLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrLocalName.setStatus("current")


class _CvpdnTunnelAttrRemoteName_Type(DisplayString):
    """Custom type cvpdnTunnelAttrRemoteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnTunnelAttrRemoteName_Type.__name__ = "DisplayString"
_CvpdnTunnelAttrRemoteName_Object = MibTableColumn
cvpdnTunnelAttrRemoteName = _CvpdnTunnelAttrRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 4),
    _CvpdnTunnelAttrRemoteName_Type()
)
cvpdnTunnelAttrRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrRemoteName.setStatus("current")


class _CvpdnTunnelAttrRemoteEndpointName_Type(DisplayString):
    """Custom type cvpdnTunnelAttrRemoteEndpointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnTunnelAttrRemoteEndpointName_Type.__name__ = "DisplayString"
_CvpdnTunnelAttrRemoteEndpointName_Object = MibTableColumn
cvpdnTunnelAttrRemoteEndpointName = _CvpdnTunnelAttrRemoteEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 5),
    _CvpdnTunnelAttrRemoteEndpointName_Type()
)
cvpdnTunnelAttrRemoteEndpointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrRemoteEndpointName.setStatus("current")
_CvpdnTunnelAttrLocalInitConnection_Type = TruthValue
_CvpdnTunnelAttrLocalInitConnection_Object = MibTableColumn
cvpdnTunnelAttrLocalInitConnection = _CvpdnTunnelAttrLocalInitConnection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 6),
    _CvpdnTunnelAttrLocalInitConnection_Type()
)
cvpdnTunnelAttrLocalInitConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrLocalInitConnection.setStatus("current")


class _CvpdnTunnelAttrOrigCause_Type(Integer32):
    """Custom type cvpdnTunnelAttrOrigCause based on Integer32"""
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
        *(("dnis", 2),
          ("domain", 1),
          ("stack", 3),
          ("xconnect", 4))
    )


_CvpdnTunnelAttrOrigCause_Type.__name__ = "Integer32"
_CvpdnTunnelAttrOrigCause_Object = MibTableColumn
cvpdnTunnelAttrOrigCause = _CvpdnTunnelAttrOrigCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 7),
    _CvpdnTunnelAttrOrigCause_Type()
)
cvpdnTunnelAttrOrigCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrOrigCause.setStatus("current")


class _CvpdnTunnelAttrState_Type(Integer32):
    """Custom type cvpdnTunnelAttrState based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("l2fCloseWait", 6),
          ("l2fClosing", 5),
          ("l2fOpen", 4),
          ("l2fOpenWait", 3),
          ("l2fOpening", 2),
          ("l2tpEstablished", 9),
          ("l2tpIdle", 7),
          ("l2tpNoSessionLeft", 11),
          ("l2tpShuttingDown", 10),
          ("l2tpWaitCtlReply", 8),
          ("pptpEstablished", 16),
          ("pptpIdle", 12),
          ("pptpTerminal", 18),
          ("pptpWaitConnect", 13),
          ("pptpWaitCtlReply", 15),
          ("pptpWaitCtlRequest", 14),
          ("pptpWaitStopReply", 17),
          ("unknown", 1))
    )


_CvpdnTunnelAttrState_Type.__name__ = "Integer32"
_CvpdnTunnelAttrState_Object = MibTableColumn
cvpdnTunnelAttrState = _CvpdnTunnelAttrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 8),
    _CvpdnTunnelAttrState_Type()
)
cvpdnTunnelAttrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrState.setStatus("current")
_CvpdnTunnelAttrActiveSessions_Type = Gauge32
_CvpdnTunnelAttrActiveSessions_Object = MibTableColumn
cvpdnTunnelAttrActiveSessions = _CvpdnTunnelAttrActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 9),
    _CvpdnTunnelAttrActiveSessions_Type()
)
cvpdnTunnelAttrActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrActiveSessions.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrActiveSessions.setUnits("sessions")
_CvpdnTunnelAttrDeniedUsers_Type = Counter32
_CvpdnTunnelAttrDeniedUsers_Object = MibTableColumn
cvpdnTunnelAttrDeniedUsers = _CvpdnTunnelAttrDeniedUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 10),
    _CvpdnTunnelAttrDeniedUsers_Type()
)
cvpdnTunnelAttrDeniedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrDeniedUsers.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrDeniedUsers.setUnits("calls")
_CvpdnTunnelAttrSoftshut_Type = TruthValue
_CvpdnTunnelAttrSoftshut_Object = MibTableColumn
cvpdnTunnelAttrSoftshut = _CvpdnTunnelAttrSoftshut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 11),
    _CvpdnTunnelAttrSoftshut_Type()
)
cvpdnTunnelAttrSoftshut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrSoftshut.setStatus("current")


class _CvpdnTunnelAttrNetworkServiceType_Type(Integer32):
    """Custom type cvpdnTunnelAttrNetworkServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_CvpdnTunnelAttrNetworkServiceType_Type.__name__ = "Integer32"
_CvpdnTunnelAttrNetworkServiceType_Object = MibTableColumn
cvpdnTunnelAttrNetworkServiceType = _CvpdnTunnelAttrNetworkServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 12),
    _CvpdnTunnelAttrNetworkServiceType_Type()
)
cvpdnTunnelAttrNetworkServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrNetworkServiceType.setStatus("current")
_CvpdnTunnelAttrLocalIpAddress_Type = IpAddress
_CvpdnTunnelAttrLocalIpAddress_Object = MibTableColumn
cvpdnTunnelAttrLocalIpAddress = _CvpdnTunnelAttrLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 13),
    _CvpdnTunnelAttrLocalIpAddress_Type()
)
cvpdnTunnelAttrLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrLocalIpAddress.setStatus("deprecated")
_CvpdnTunnelAttrSourceIpAddress_Type = IpAddress
_CvpdnTunnelAttrSourceIpAddress_Object = MibTableColumn
cvpdnTunnelAttrSourceIpAddress = _CvpdnTunnelAttrSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 14),
    _CvpdnTunnelAttrSourceIpAddress_Type()
)
cvpdnTunnelAttrSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrSourceIpAddress.setStatus("deprecated")
_CvpdnTunnelAttrRemoteIpAddress_Type = IpAddress
_CvpdnTunnelAttrRemoteIpAddress_Object = MibTableColumn
cvpdnTunnelAttrRemoteIpAddress = _CvpdnTunnelAttrRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 15),
    _CvpdnTunnelAttrRemoteIpAddress_Type()
)
cvpdnTunnelAttrRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrRemoteIpAddress.setStatus("deprecated")
_CvpdnTunnelAttrLocalInetAddressType_Type = InetAddressType
_CvpdnTunnelAttrLocalInetAddressType_Object = MibTableColumn
cvpdnTunnelAttrLocalInetAddressType = _CvpdnTunnelAttrLocalInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 16),
    _CvpdnTunnelAttrLocalInetAddressType_Type()
)
cvpdnTunnelAttrLocalInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrLocalInetAddressType.setStatus("current")
_CvpdnTunnelAttrLocalInetAddress_Type = InetAddress
_CvpdnTunnelAttrLocalInetAddress_Object = MibTableColumn
cvpdnTunnelAttrLocalInetAddress = _CvpdnTunnelAttrLocalInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 17),
    _CvpdnTunnelAttrLocalInetAddress_Type()
)
cvpdnTunnelAttrLocalInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrLocalInetAddress.setStatus("current")
_CvpdnTunnelAttrSourceInetAddressType_Type = InetAddressType
_CvpdnTunnelAttrSourceInetAddressType_Object = MibTableColumn
cvpdnTunnelAttrSourceInetAddressType = _CvpdnTunnelAttrSourceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 18),
    _CvpdnTunnelAttrSourceInetAddressType_Type()
)
cvpdnTunnelAttrSourceInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrSourceInetAddressType.setStatus("current")
_CvpdnTunnelAttrSourceInetAddress_Type = InetAddress
_CvpdnTunnelAttrSourceInetAddress_Object = MibTableColumn
cvpdnTunnelAttrSourceInetAddress = _CvpdnTunnelAttrSourceInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 19),
    _CvpdnTunnelAttrSourceInetAddress_Type()
)
cvpdnTunnelAttrSourceInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrSourceInetAddress.setStatus("current")
_CvpdnTunnelAttrRemoteInetAddressType_Type = InetAddressType
_CvpdnTunnelAttrRemoteInetAddressType_Object = MibTableColumn
cvpdnTunnelAttrRemoteInetAddressType = _CvpdnTunnelAttrRemoteInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 20),
    _CvpdnTunnelAttrRemoteInetAddressType_Type()
)
cvpdnTunnelAttrRemoteInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrRemoteInetAddressType.setStatus("current")
_CvpdnTunnelAttrRemoteInetAddress_Type = InetAddress
_CvpdnTunnelAttrRemoteInetAddress_Object = MibTableColumn
cvpdnTunnelAttrRemoteInetAddress = _CvpdnTunnelAttrRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 2, 2, 1, 21),
    _CvpdnTunnelAttrRemoteInetAddress_Type()
)
cvpdnTunnelAttrRemoteInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelAttrRemoteInetAddress.setStatus("current")
_CvpdnTunnelSessionInfo_ObjectIdentity = ObjectIdentity
cvpdnTunnelSessionInfo = _CvpdnTunnelSessionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3)
)
_CvpdnTunnelSessionTable_Object = MibTable
cvpdnTunnelSessionTable = _CvpdnTunnelSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cvpdnTunnelSessionTable.setStatus("obsolete")
_CvpdnTunnelSessionEntry_Object = MibTableRow
cvpdnTunnelSessionEntry = _CvpdnTunnelSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1)
)
cvpdnTunnelSessionEntry.setIndexNames(
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnTunnelTunnelId"),
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionId"),
)
if mibBuilder.loadTexts:
    cvpdnTunnelSessionEntry.setStatus("obsolete")
_CvpdnTunnelSessionId_Type = Unsigned32
_CvpdnTunnelSessionId_Object = MibTableColumn
cvpdnTunnelSessionId = _CvpdnTunnelSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 1),
    _CvpdnTunnelSessionId_Type()
)
cvpdnTunnelSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionId.setStatus("obsolete")


class _CvpdnTunnelSessionUserName_Type(DisplayString):
    """Custom type cvpdnTunnelSessionUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnTunnelSessionUserName_Type.__name__ = "DisplayString"
_CvpdnTunnelSessionUserName_Object = MibTableColumn
cvpdnTunnelSessionUserName = _CvpdnTunnelSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 2),
    _CvpdnTunnelSessionUserName_Type()
)
cvpdnTunnelSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionUserName.setStatus("obsolete")


class _CvpdnTunnelSessionState_Type(Integer32):
    """Custom type cvpdnTunnelSessionState based on Integer32"""
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
        *(("closing", 4),
          ("open", 3),
          ("opening", 2),
          ("unknown", 1),
          ("waitingForTunnel", 5))
    )


_CvpdnTunnelSessionState_Type.__name__ = "Integer32"
_CvpdnTunnelSessionState_Object = MibTableColumn
cvpdnTunnelSessionState = _CvpdnTunnelSessionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 3),
    _CvpdnTunnelSessionState_Type()
)
cvpdnTunnelSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionState.setStatus("obsolete")
_CvpdnTunnelSessionCallDuration_Type = TimeTicks
_CvpdnTunnelSessionCallDuration_Object = MibTableColumn
cvpdnTunnelSessionCallDuration = _CvpdnTunnelSessionCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 4),
    _CvpdnTunnelSessionCallDuration_Type()
)
cvpdnTunnelSessionCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionCallDuration.setStatus("obsolete")
_CvpdnTunnelSessionPacketsOut_Type = Counter32
_CvpdnTunnelSessionPacketsOut_Object = MibTableColumn
cvpdnTunnelSessionPacketsOut = _CvpdnTunnelSessionPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 5),
    _CvpdnTunnelSessionPacketsOut_Type()
)
cvpdnTunnelSessionPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionPacketsOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionPacketsOut.setUnits("packets")
_CvpdnTunnelSessionBytesOut_Type = Counter32
_CvpdnTunnelSessionBytesOut_Object = MibTableColumn
cvpdnTunnelSessionBytesOut = _CvpdnTunnelSessionBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 6),
    _CvpdnTunnelSessionBytesOut_Type()
)
cvpdnTunnelSessionBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionBytesOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionBytesOut.setUnits("bytes")
_CvpdnTunnelSessionPacketsIn_Type = Counter32
_CvpdnTunnelSessionPacketsIn_Object = MibTableColumn
cvpdnTunnelSessionPacketsIn = _CvpdnTunnelSessionPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 7),
    _CvpdnTunnelSessionPacketsIn_Type()
)
cvpdnTunnelSessionPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionPacketsIn.setStatus("obsolete")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionPacketsIn.setUnits("packets")
_CvpdnTunnelSessionBytesIn_Type = Counter32
_CvpdnTunnelSessionBytesIn_Object = MibTableColumn
cvpdnTunnelSessionBytesIn = _CvpdnTunnelSessionBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 8),
    _CvpdnTunnelSessionBytesIn_Type()
)
cvpdnTunnelSessionBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionBytesIn.setStatus("obsolete")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionBytesIn.setUnits("bytes")


class _CvpdnTunnelSessionDeviceType_Type(Integer32):
    """Custom type cvpdnTunnelSessionDeviceType based on Integer32"""
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
        *(("async", 3),
          ("asyncInternalModem", 2),
          ("bchan", 4),
          ("cable", 8),
          ("other", 1),
          ("sync", 5),
          ("virtualAccess", 6),
          ("xdsl", 7))
    )


_CvpdnTunnelSessionDeviceType_Type.__name__ = "Integer32"
_CvpdnTunnelSessionDeviceType_Object = MibTableColumn
cvpdnTunnelSessionDeviceType = _CvpdnTunnelSessionDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 9),
    _CvpdnTunnelSessionDeviceType_Type()
)
cvpdnTunnelSessionDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionDeviceType.setStatus("obsolete")
_CvpdnTunnelSessionDeviceCallerId_Type = DisplayString
_CvpdnTunnelSessionDeviceCallerId_Object = MibTableColumn
cvpdnTunnelSessionDeviceCallerId = _CvpdnTunnelSessionDeviceCallerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 10),
    _CvpdnTunnelSessionDeviceCallerId_Type()
)
cvpdnTunnelSessionDeviceCallerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionDeviceCallerId.setStatus("obsolete")
_CvpdnTunnelSessionDevicePhyId_Type = InterfaceIndexOrZero
_CvpdnTunnelSessionDevicePhyId_Object = MibTableColumn
cvpdnTunnelSessionDevicePhyId = _CvpdnTunnelSessionDevicePhyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 11),
    _CvpdnTunnelSessionDevicePhyId_Type()
)
cvpdnTunnelSessionDevicePhyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionDevicePhyId.setStatus("obsolete")
_CvpdnTunnelSessionMultilink_Type = TruthValue
_CvpdnTunnelSessionMultilink_Object = MibTableColumn
cvpdnTunnelSessionMultilink = _CvpdnTunnelSessionMultilink_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 12),
    _CvpdnTunnelSessionMultilink_Type()
)
cvpdnTunnelSessionMultilink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionMultilink.setStatus("obsolete")
_CvpdnTunnelSessionModemSlotIndex_Type = Unsigned32
_CvpdnTunnelSessionModemSlotIndex_Object = MibTableColumn
cvpdnTunnelSessionModemSlotIndex = _CvpdnTunnelSessionModemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 13),
    _CvpdnTunnelSessionModemSlotIndex_Type()
)
cvpdnTunnelSessionModemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionModemSlotIndex.setStatus("obsolete")
_CvpdnTunnelSessionModemPortIndex_Type = Unsigned32
_CvpdnTunnelSessionModemPortIndex_Object = MibTableColumn
cvpdnTunnelSessionModemPortIndex = _CvpdnTunnelSessionModemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 14),
    _CvpdnTunnelSessionModemPortIndex_Type()
)
cvpdnTunnelSessionModemPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionModemPortIndex.setStatus("obsolete")
_CvpdnTunnelSessionDS1SlotIndex_Type = Unsigned32
_CvpdnTunnelSessionDS1SlotIndex_Object = MibTableColumn
cvpdnTunnelSessionDS1SlotIndex = _CvpdnTunnelSessionDS1SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 15),
    _CvpdnTunnelSessionDS1SlotIndex_Type()
)
cvpdnTunnelSessionDS1SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionDS1SlotIndex.setStatus("obsolete")
_CvpdnTunnelSessionDS1PortIndex_Type = Unsigned32
_CvpdnTunnelSessionDS1PortIndex_Object = MibTableColumn
cvpdnTunnelSessionDS1PortIndex = _CvpdnTunnelSessionDS1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 16),
    _CvpdnTunnelSessionDS1PortIndex_Type()
)
cvpdnTunnelSessionDS1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionDS1PortIndex.setStatus("obsolete")
_CvpdnTunnelSessionDS1ChannelIndex_Type = Unsigned32
_CvpdnTunnelSessionDS1ChannelIndex_Object = MibTableColumn
cvpdnTunnelSessionDS1ChannelIndex = _CvpdnTunnelSessionDS1ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 17),
    _CvpdnTunnelSessionDS1ChannelIndex_Type()
)
cvpdnTunnelSessionDS1ChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionDS1ChannelIndex.setStatus("obsolete")
_CvpdnTunnelSessionModemCallStartTime_Type = TimeStamp
_CvpdnTunnelSessionModemCallStartTime_Object = MibTableColumn
cvpdnTunnelSessionModemCallStartTime = _CvpdnTunnelSessionModemCallStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 18),
    _CvpdnTunnelSessionModemCallStartTime_Type()
)
cvpdnTunnelSessionModemCallStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionModemCallStartTime.setStatus("obsolete")
_CvpdnTunnelSessionModemCallStartIndex_Type = Unsigned32
_CvpdnTunnelSessionModemCallStartIndex_Object = MibTableColumn
cvpdnTunnelSessionModemCallStartIndex = _CvpdnTunnelSessionModemCallStartIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 1, 1, 19),
    _CvpdnTunnelSessionModemCallStartIndex_Type()
)
cvpdnTunnelSessionModemCallStartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTunnelSessionModemCallStartIndex.setStatus("obsolete")
_CvpdnSessionAttrTable_Object = MibTable
cvpdnSessionAttrTable = _CvpdnSessionAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cvpdnSessionAttrTable.setStatus("current")
_CvpdnSessionAttrEntry_Object = MibTableRow
cvpdnSessionAttrEntry = _CvpdnSessionAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1)
)
cvpdnSessionAttrEntry.setIndexNames(
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnSystemTunnelType"),
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrTunnelId"),
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrSessionId"),
)
if mibBuilder.loadTexts:
    cvpdnSessionAttrEntry.setStatus("current")


class _CvpdnSessionAttrSessionId_Type(Integer32):
    """Custom type cvpdnSessionAttrSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvpdnSessionAttrSessionId_Type.__name__ = "Integer32"
_CvpdnSessionAttrSessionId_Object = MibTableColumn
cvpdnSessionAttrSessionId = _CvpdnSessionAttrSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 1),
    _CvpdnSessionAttrSessionId_Type()
)
cvpdnSessionAttrSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpdnSessionAttrSessionId.setStatus("current")


class _CvpdnSessionAttrUserName_Type(DisplayString):
    """Custom type cvpdnSessionAttrUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnSessionAttrUserName_Type.__name__ = "DisplayString"
_CvpdnSessionAttrUserName_Object = MibTableColumn
cvpdnSessionAttrUserName = _CvpdnSessionAttrUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 2),
    _CvpdnSessionAttrUserName_Type()
)
cvpdnSessionAttrUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrUserName.setStatus("current")


class _CvpdnSessionAttrState_Type(Integer32):
    """Custom type cvpdnSessionAttrState based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("l2fCloseWait", 4),
          ("l2fOpen", 3),
          ("l2fOpening", 2),
          ("l2fWaitingForTunnel", 5),
          ("l2tpEstablished", 10),
          ("l2tpIdle", 6),
          ("l2tpShuttingDown", 11),
          ("l2tpWaitConnect", 9),
          ("l2tpWaitReply", 8),
          ("l2tpWaitingTunnel", 7),
          ("pptpPacEstablished", 13),
          ("pptpPnsEstablished", 16),
          ("pptpTerminal", 18),
          ("pptpWaitCallDisc", 17),
          ("pptpWaitOCRP", 15),
          ("pptpWaitTunnel", 14),
          ("pptpWaitVAccess", 12),
          ("unknown", 1))
    )


_CvpdnSessionAttrState_Type.__name__ = "Integer32"
_CvpdnSessionAttrState_Object = MibTableColumn
cvpdnSessionAttrState = _CvpdnSessionAttrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 3),
    _CvpdnSessionAttrState_Type()
)
cvpdnSessionAttrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrState.setStatus("current")
_CvpdnSessionAttrCallDuration_Type = TimeTicks
_CvpdnSessionAttrCallDuration_Object = MibTableColumn
cvpdnSessionAttrCallDuration = _CvpdnSessionAttrCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 4),
    _CvpdnSessionAttrCallDuration_Type()
)
cvpdnSessionAttrCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrCallDuration.setStatus("current")
_CvpdnSessionAttrPacketsOut_Type = Counter32
_CvpdnSessionAttrPacketsOut_Object = MibTableColumn
cvpdnSessionAttrPacketsOut = _CvpdnSessionAttrPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 5),
    _CvpdnSessionAttrPacketsOut_Type()
)
cvpdnSessionAttrPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrPacketsOut.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionAttrPacketsOut.setUnits("packets")
_CvpdnSessionAttrBytesOut_Type = Counter32
_CvpdnSessionAttrBytesOut_Object = MibTableColumn
cvpdnSessionAttrBytesOut = _CvpdnSessionAttrBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 6),
    _CvpdnSessionAttrBytesOut_Type()
)
cvpdnSessionAttrBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionAttrBytesOut.setUnits("bytes")
_CvpdnSessionAttrPacketsIn_Type = Counter32
_CvpdnSessionAttrPacketsIn_Object = MibTableColumn
cvpdnSessionAttrPacketsIn = _CvpdnSessionAttrPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 7),
    _CvpdnSessionAttrPacketsIn_Type()
)
cvpdnSessionAttrPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrPacketsIn.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionAttrPacketsIn.setUnits("packets")
_CvpdnSessionAttrBytesIn_Type = Counter32
_CvpdnSessionAttrBytesIn_Object = MibTableColumn
cvpdnSessionAttrBytesIn = _CvpdnSessionAttrBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 8),
    _CvpdnSessionAttrBytesIn_Type()
)
cvpdnSessionAttrBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionAttrBytesIn.setUnits("bytes")


class _CvpdnSessionAttrDeviceType_Type(Integer32):
    """Custom type cvpdnSessionAttrDeviceType based on Integer32"""
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
        *(("async", 3),
          ("asyncInternalModem", 2),
          ("bchan", 4),
          ("cable", 8),
          ("other", 1),
          ("sync", 5),
          ("virtualAccess", 6),
          ("xdsl", 7))
    )


_CvpdnSessionAttrDeviceType_Type.__name__ = "Integer32"
_CvpdnSessionAttrDeviceType_Object = MibTableColumn
cvpdnSessionAttrDeviceType = _CvpdnSessionAttrDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 9),
    _CvpdnSessionAttrDeviceType_Type()
)
cvpdnSessionAttrDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrDeviceType.setStatus("current")
_CvpdnSessionAttrDeviceCallerId_Type = DisplayString
_CvpdnSessionAttrDeviceCallerId_Object = MibTableColumn
cvpdnSessionAttrDeviceCallerId = _CvpdnSessionAttrDeviceCallerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 10),
    _CvpdnSessionAttrDeviceCallerId_Type()
)
cvpdnSessionAttrDeviceCallerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrDeviceCallerId.setStatus("current")
_CvpdnSessionAttrDevicePhyId_Type = InterfaceIndexOrZero
_CvpdnSessionAttrDevicePhyId_Object = MibTableColumn
cvpdnSessionAttrDevicePhyId = _CvpdnSessionAttrDevicePhyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 11),
    _CvpdnSessionAttrDevicePhyId_Type()
)
cvpdnSessionAttrDevicePhyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrDevicePhyId.setStatus("current")
_CvpdnSessionAttrMultilink_Type = TruthValue
_CvpdnSessionAttrMultilink_Object = MibTableColumn
cvpdnSessionAttrMultilink = _CvpdnSessionAttrMultilink_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 12),
    _CvpdnSessionAttrMultilink_Type()
)
cvpdnSessionAttrMultilink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrMultilink.setStatus("current")
_CvpdnSessionAttrModemSlotIndex_Type = Unsigned32
_CvpdnSessionAttrModemSlotIndex_Object = MibTableColumn
cvpdnSessionAttrModemSlotIndex = _CvpdnSessionAttrModemSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 13),
    _CvpdnSessionAttrModemSlotIndex_Type()
)
cvpdnSessionAttrModemSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrModemSlotIndex.setStatus("current")
_CvpdnSessionAttrModemPortIndex_Type = Unsigned32
_CvpdnSessionAttrModemPortIndex_Object = MibTableColumn
cvpdnSessionAttrModemPortIndex = _CvpdnSessionAttrModemPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 14),
    _CvpdnSessionAttrModemPortIndex_Type()
)
cvpdnSessionAttrModemPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrModemPortIndex.setStatus("current")
_CvpdnSessionAttrDS1SlotIndex_Type = Unsigned32
_CvpdnSessionAttrDS1SlotIndex_Object = MibTableColumn
cvpdnSessionAttrDS1SlotIndex = _CvpdnSessionAttrDS1SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 15),
    _CvpdnSessionAttrDS1SlotIndex_Type()
)
cvpdnSessionAttrDS1SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrDS1SlotIndex.setStatus("current")
_CvpdnSessionAttrDS1PortIndex_Type = Unsigned32
_CvpdnSessionAttrDS1PortIndex_Object = MibTableColumn
cvpdnSessionAttrDS1PortIndex = _CvpdnSessionAttrDS1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 16),
    _CvpdnSessionAttrDS1PortIndex_Type()
)
cvpdnSessionAttrDS1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrDS1PortIndex.setStatus("current")
_CvpdnSessionAttrDS1ChannelIndex_Type = Unsigned32
_CvpdnSessionAttrDS1ChannelIndex_Object = MibTableColumn
cvpdnSessionAttrDS1ChannelIndex = _CvpdnSessionAttrDS1ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 17),
    _CvpdnSessionAttrDS1ChannelIndex_Type()
)
cvpdnSessionAttrDS1ChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrDS1ChannelIndex.setStatus("current")
_CvpdnSessionAttrModemCallStartTime_Type = TimeStamp
_CvpdnSessionAttrModemCallStartTime_Object = MibTableColumn
cvpdnSessionAttrModemCallStartTime = _CvpdnSessionAttrModemCallStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 18),
    _CvpdnSessionAttrModemCallStartTime_Type()
)
cvpdnSessionAttrModemCallStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrModemCallStartTime.setStatus("current")
_CvpdnSessionAttrModemCallStartIndex_Type = Unsigned32
_CvpdnSessionAttrModemCallStartIndex_Object = MibTableColumn
cvpdnSessionAttrModemCallStartIndex = _CvpdnSessionAttrModemCallStartIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 19),
    _CvpdnSessionAttrModemCallStartIndex_Type()
)
cvpdnSessionAttrModemCallStartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrModemCallStartIndex.setStatus("current")
_CvpdnSessionAttrVirtualCircuitID_Type = Unsigned32
_CvpdnSessionAttrVirtualCircuitID_Object = MibTableColumn
cvpdnSessionAttrVirtualCircuitID = _CvpdnSessionAttrVirtualCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 20),
    _CvpdnSessionAttrVirtualCircuitID_Type()
)
cvpdnSessionAttrVirtualCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrVirtualCircuitID.setStatus("current")
_CvpdnSessionAttrSentPktsDropped_Type = Counter32
_CvpdnSessionAttrSentPktsDropped_Object = MibTableColumn
cvpdnSessionAttrSentPktsDropped = _CvpdnSessionAttrSentPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 21),
    _CvpdnSessionAttrSentPktsDropped_Type()
)
cvpdnSessionAttrSentPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrSentPktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionAttrSentPktsDropped.setUnits("packets")
_CvpdnSessionAttrRecvPktsDropped_Type = Counter32
_CvpdnSessionAttrRecvPktsDropped_Object = MibTableColumn
cvpdnSessionAttrRecvPktsDropped = _CvpdnSessionAttrRecvPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 22),
    _CvpdnSessionAttrRecvPktsDropped_Type()
)
cvpdnSessionAttrRecvPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrRecvPktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnSessionAttrRecvPktsDropped.setUnits("packets")


class _CvpdnSessionAttrMultilinkBundle_Type(SnmpAdminString):
    """Custom type cvpdnSessionAttrMultilinkBundle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvpdnSessionAttrMultilinkBundle_Type.__name__ = "SnmpAdminString"
_CvpdnSessionAttrMultilinkBundle_Object = MibTableColumn
cvpdnSessionAttrMultilinkBundle = _CvpdnSessionAttrMultilinkBundle_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 23),
    _CvpdnSessionAttrMultilinkBundle_Type()
)
cvpdnSessionAttrMultilinkBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrMultilinkBundle.setStatus("current")
_CvpdnSessionAttrMultilinkIfIndex_Type = InterfaceIndexOrZero
_CvpdnSessionAttrMultilinkIfIndex_Object = MibTableColumn
cvpdnSessionAttrMultilinkIfIndex = _CvpdnSessionAttrMultilinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 3, 2, 1, 24),
    _CvpdnSessionAttrMultilinkIfIndex_Type()
)
cvpdnSessionAttrMultilinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnSessionAttrMultilinkIfIndex.setStatus("current")
_CvpdnUserToFailHistInfo_ObjectIdentity = ObjectIdentity
cvpdnUserToFailHistInfo = _CvpdnUserToFailHistInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4)
)
_CvpdnUserToFailHistInfoTable_Object = MibTable
cvpdnUserToFailHistInfoTable = _CvpdnUserToFailHistInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cvpdnUserToFailHistInfoTable.setStatus("current")
_CvpdnUserToFailHistInfoEntry_Object = MibTableRow
cvpdnUserToFailHistInfoEntry = _CvpdnUserToFailHistInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1)
)
cvpdnUserToFailHistInfoEntry.setIndexNames(
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistUname"),
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistTunnelId"),
)
if mibBuilder.loadTexts:
    cvpdnUserToFailHistInfoEntry.setStatus("current")


class _CvpdnUnameToFailHistUname_Type(DisplayString):
    """Custom type cvpdnUnameToFailHistUname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnUnameToFailHistUname_Type.__name__ = "DisplayString"
_CvpdnUnameToFailHistUname_Object = MibTableColumn
cvpdnUnameToFailHistUname = _CvpdnUnameToFailHistUname_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 1),
    _CvpdnUnameToFailHistUname_Type()
)
cvpdnUnameToFailHistUname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistUname.setStatus("current")
_CvpdnUnameToFailHistTunnelId_Type = Unsigned32
_CvpdnUnameToFailHistTunnelId_Object = MibTableColumn
cvpdnUnameToFailHistTunnelId = _CvpdnUnameToFailHistTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 2),
    _CvpdnUnameToFailHistTunnelId_Type()
)
cvpdnUnameToFailHistTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistTunnelId.setStatus("current")
_CvpdnUnameToFailHistUserId_Type = Unsigned32
_CvpdnUnameToFailHistUserId_Object = MibTableColumn
cvpdnUnameToFailHistUserId = _CvpdnUnameToFailHistUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 3),
    _CvpdnUnameToFailHistUserId_Type()
)
cvpdnUnameToFailHistUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistUserId.setStatus("current")
_CvpdnUnameToFailHistLocalInitConn_Type = TruthValue
_CvpdnUnameToFailHistLocalInitConn_Object = MibTableColumn
cvpdnUnameToFailHistLocalInitConn = _CvpdnUnameToFailHistLocalInitConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 4),
    _CvpdnUnameToFailHistLocalInitConn_Type()
)
cvpdnUnameToFailHistLocalInitConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistLocalInitConn.setStatus("current")
_CvpdnUnameToFailHistLocalName_Type = DisplayString
_CvpdnUnameToFailHistLocalName_Object = MibTableColumn
cvpdnUnameToFailHistLocalName = _CvpdnUnameToFailHistLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 5),
    _CvpdnUnameToFailHistLocalName_Type()
)
cvpdnUnameToFailHistLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistLocalName.setStatus("current")
_CvpdnUnameToFailHistRemoteName_Type = DisplayString
_CvpdnUnameToFailHistRemoteName_Object = MibTableColumn
cvpdnUnameToFailHistRemoteName = _CvpdnUnameToFailHistRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 6),
    _CvpdnUnameToFailHistRemoteName_Type()
)
cvpdnUnameToFailHistRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistRemoteName.setStatus("current")
_CvpdnUnameToFailHistSourceIp_Type = IpAddress
_CvpdnUnameToFailHistSourceIp_Object = MibTableColumn
cvpdnUnameToFailHistSourceIp = _CvpdnUnameToFailHistSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 7),
    _CvpdnUnameToFailHistSourceIp_Type()
)
cvpdnUnameToFailHistSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistSourceIp.setStatus("deprecated")
_CvpdnUnameToFailHistDestIp_Type = IpAddress
_CvpdnUnameToFailHistDestIp_Object = MibTableColumn
cvpdnUnameToFailHistDestIp = _CvpdnUnameToFailHistDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 8),
    _CvpdnUnameToFailHistDestIp_Type()
)
cvpdnUnameToFailHistDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistDestIp.setStatus("deprecated")
_CvpdnUnameToFailHistCount_Type = Counter32
_CvpdnUnameToFailHistCount_Object = MibTableColumn
cvpdnUnameToFailHistCount = _CvpdnUnameToFailHistCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 9),
    _CvpdnUnameToFailHistCount_Type()
)
cvpdnUnameToFailHistCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistCount.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistCount.setUnits("failures")
_CvpdnUnameToFailHistFailTime_Type = TimeStamp
_CvpdnUnameToFailHistFailTime_Object = MibTableColumn
cvpdnUnameToFailHistFailTime = _CvpdnUnameToFailHistFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 10),
    _CvpdnUnameToFailHistFailTime_Type()
)
cvpdnUnameToFailHistFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistFailTime.setStatus("current")


class _CvpdnUnameToFailHistFailType_Type(DisplayString):
    """Custom type cvpdnUnameToFailHistFailType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnUnameToFailHistFailType_Type.__name__ = "DisplayString"
_CvpdnUnameToFailHistFailType_Object = MibTableColumn
cvpdnUnameToFailHistFailType = _CvpdnUnameToFailHistFailType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 11),
    _CvpdnUnameToFailHistFailType_Type()
)
cvpdnUnameToFailHistFailType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistFailType.setStatus("current")


class _CvpdnUnameToFailHistFailReason_Type(DisplayString):
    """Custom type cvpdnUnameToFailHistFailReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnUnameToFailHistFailReason_Type.__name__ = "DisplayString"
_CvpdnUnameToFailHistFailReason_Object = MibTableColumn
cvpdnUnameToFailHistFailReason = _CvpdnUnameToFailHistFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 12),
    _CvpdnUnameToFailHistFailReason_Type()
)
cvpdnUnameToFailHistFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistFailReason.setStatus("current")
_CvpdnUnameToFailHistSourceInetType_Type = InetAddressType
_CvpdnUnameToFailHistSourceInetType_Object = MibTableColumn
cvpdnUnameToFailHistSourceInetType = _CvpdnUnameToFailHistSourceInetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 13),
    _CvpdnUnameToFailHistSourceInetType_Type()
)
cvpdnUnameToFailHistSourceInetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistSourceInetType.setStatus("current")
_CvpdnUnameToFailHistSourceInetAddr_Type = InetAddress
_CvpdnUnameToFailHistSourceInetAddr_Object = MibTableColumn
cvpdnUnameToFailHistSourceInetAddr = _CvpdnUnameToFailHistSourceInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 14),
    _CvpdnUnameToFailHistSourceInetAddr_Type()
)
cvpdnUnameToFailHistSourceInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistSourceInetAddr.setStatus("current")
_CvpdnUnameToFailHistDestInetType_Type = InetAddressType
_CvpdnUnameToFailHistDestInetType_Object = MibTableColumn
cvpdnUnameToFailHistDestInetType = _CvpdnUnameToFailHistDestInetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 15),
    _CvpdnUnameToFailHistDestInetType_Type()
)
cvpdnUnameToFailHistDestInetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistDestInetType.setStatus("current")
_CvpdnUnameToFailHistDestInetAddr_Type = InetAddress
_CvpdnUnameToFailHistDestInetAddr_Object = MibTableColumn
cvpdnUnameToFailHistDestInetAddr = _CvpdnUnameToFailHistDestInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 4, 1, 1, 16),
    _CvpdnUnameToFailHistDestInetAddr_Type()
)
cvpdnUnameToFailHistDestInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnUnameToFailHistDestInetAddr.setStatus("current")
_CvpdnTemplateInfo_ObjectIdentity = ObjectIdentity
cvpdnTemplateInfo = _CvpdnTemplateInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 5)
)
_CvpdnTemplateTable_Object = MibTable
cvpdnTemplateTable = _CvpdnTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cvpdnTemplateTable.setStatus("current")
_CvpdnTemplateEntry_Object = MibTableRow
cvpdnTemplateEntry = _CvpdnTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 5, 1, 1)
)
cvpdnTemplateEntry.setIndexNames(
    (1, "CISCO-VPDN-MGMT-MIB", "cvpdnTemplateName"),
)
if mibBuilder.loadTexts:
    cvpdnTemplateEntry.setStatus("current")


class _CvpdnTemplateName_Type(SnmpAdminString):
    """Custom type cvpdnTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CvpdnTemplateName_Type.__name__ = "SnmpAdminString"
_CvpdnTemplateName_Object = MibTableColumn
cvpdnTemplateName = _CvpdnTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 5, 1, 1, 1),
    _CvpdnTemplateName_Type()
)
cvpdnTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpdnTemplateName.setStatus("current")
_CvpdnTemplateActiveSessions_Type = Gauge32
_CvpdnTemplateActiveSessions_Object = MibTableColumn
cvpdnTemplateActiveSessions = _CvpdnTemplateActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 5, 1, 1, 2),
    _CvpdnTemplateActiveSessions_Type()
)
cvpdnTemplateActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnTemplateActiveSessions.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnTemplateActiveSessions.setUnits("sessions")
_CvpdnMultilinkInfo_ObjectIdentity = ObjectIdentity
cvpdnMultilinkInfo = _CvpdnMultilinkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6)
)
_CvpdnBundlesWithOneLink_Type = Gauge32
_CvpdnBundlesWithOneLink_Object = MibScalar
cvpdnBundlesWithOneLink = _CvpdnBundlesWithOneLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 1),
    _CvpdnBundlesWithOneLink_Type()
)
cvpdnBundlesWithOneLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnBundlesWithOneLink.setStatus("current")
_CvpdnBundlesWithTwoLinks_Type = Gauge32
_CvpdnBundlesWithTwoLinks_Object = MibScalar
cvpdnBundlesWithTwoLinks = _CvpdnBundlesWithTwoLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 2),
    _CvpdnBundlesWithTwoLinks_Type()
)
cvpdnBundlesWithTwoLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnBundlesWithTwoLinks.setStatus("current")
_CvpdnBundlesWithMoreThanTwoLinks_Type = Gauge32
_CvpdnBundlesWithMoreThanTwoLinks_Object = MibScalar
cvpdnBundlesWithMoreThanTwoLinks = _CvpdnBundlesWithMoreThanTwoLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 3),
    _CvpdnBundlesWithMoreThanTwoLinks_Type()
)
cvpdnBundlesWithMoreThanTwoLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnBundlesWithMoreThanTwoLinks.setStatus("current")
_CvpdnBundleTable_Object = MibTable
cvpdnBundleTable = _CvpdnBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cvpdnBundleTable.setStatus("current")
_CvpdnBundleEntry_Object = MibTableRow
cvpdnBundleEntry = _CvpdnBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 4, 1)
)
cvpdnBundleEntry.setIndexNames(
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnBundleName"),
)
if mibBuilder.loadTexts:
    cvpdnBundleEntry.setStatus("current")


class _CvpdnBundleName_Type(SnmpAdminString):
    """Custom type cvpdnBundleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CvpdnBundleName_Type.__name__ = "SnmpAdminString"
_CvpdnBundleName_Object = MibTableColumn
cvpdnBundleName = _CvpdnBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 4, 1, 1),
    _CvpdnBundleName_Type()
)
cvpdnBundleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpdnBundleName.setStatus("current")
_CvpdnBundleLinkCount_Type = Gauge32
_CvpdnBundleLinkCount_Object = MibTableColumn
cvpdnBundleLinkCount = _CvpdnBundleLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 4, 1, 2),
    _CvpdnBundleLinkCount_Type()
)
cvpdnBundleLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnBundleLinkCount.setStatus("current")
if mibBuilder.loadTexts:
    cvpdnBundleLinkCount.setUnits("links")


class _CvpdnBundleEndpointType_Type(Integer32):
    """Custom type cvpdnBundleEndpointType based on Integer32"""
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
        *(("hostname", 2),
          ("ipV4Address", 5),
          ("ipV6Address", 6),
          ("macAddress", 4),
          ("magicNumber", 8),
          ("none", 1),
          ("phone", 7),
          ("string", 3))
    )


_CvpdnBundleEndpointType_Type.__name__ = "Integer32"
_CvpdnBundleEndpointType_Object = MibTableColumn
cvpdnBundleEndpointType = _CvpdnBundleEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 4, 1, 3),
    _CvpdnBundleEndpointType_Type()
)
cvpdnBundleEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnBundleEndpointType.setStatus("deprecated")


class _CvpdnBundleEndpoint_Type(OctetString):
    """Custom type cvpdnBundleEndpoint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvpdnBundleEndpoint_Type.__name__ = "OctetString"
_CvpdnBundleEndpoint_Object = MibTableColumn
cvpdnBundleEndpoint = _CvpdnBundleEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 4, 1, 4),
    _CvpdnBundleEndpoint_Type()
)
cvpdnBundleEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnBundleEndpoint.setStatus("current")
_CvpdnBundlePeerIpAddrType_Type = InetAddressType
_CvpdnBundlePeerIpAddrType_Object = MibTableColumn
cvpdnBundlePeerIpAddrType = _CvpdnBundlePeerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 4, 1, 5),
    _CvpdnBundlePeerIpAddrType_Type()
)
cvpdnBundlePeerIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnBundlePeerIpAddrType.setStatus("current")
_CvpdnBundlePeerIpAddr_Type = InetAddress
_CvpdnBundlePeerIpAddr_Object = MibTableColumn
cvpdnBundlePeerIpAddr = _CvpdnBundlePeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 4, 1, 6),
    _CvpdnBundlePeerIpAddr_Type()
)
cvpdnBundlePeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnBundlePeerIpAddr.setStatus("current")
_CvpdnBundleEndpointClass_Type = EndpointClass
_CvpdnBundleEndpointClass_Object = MibTableColumn
cvpdnBundleEndpointClass = _CvpdnBundleEndpointClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 4, 1, 7),
    _CvpdnBundleEndpointClass_Type()
)
cvpdnBundleEndpointClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnBundleEndpointClass.setStatus("current")
_CvpdnBundleLastChanged_Type = TimeStamp
_CvpdnBundleLastChanged_Object = MibScalar
cvpdnBundleLastChanged = _CvpdnBundleLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 5),
    _CvpdnBundleLastChanged_Type()
)
cvpdnBundleLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnBundleLastChanged.setStatus("current")
_CvpdnBundleChildTable_Object = MibTable
cvpdnBundleChildTable = _CvpdnBundleChildTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 6)
)
if mibBuilder.loadTexts:
    cvpdnBundleChildTable.setStatus("current")
_CvpdnBundleChildEntry_Object = MibTableRow
cvpdnBundleChildEntry = _CvpdnBundleChildEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 6, 1)
)
cvpdnBundleChildEntry.setIndexNames(
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnBundleName"),
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnBundleChildTunnelType"),
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnBundleChildTunnelId"),
    (0, "CISCO-VPDN-MGMT-MIB", "cvpdnBundleChildSessionId"),
)
if mibBuilder.loadTexts:
    cvpdnBundleChildEntry.setStatus("current")
_CvpdnBundleChildTunnelType_Type = TunnelType
_CvpdnBundleChildTunnelType_Object = MibTableColumn
cvpdnBundleChildTunnelType = _CvpdnBundleChildTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 6, 1, 1),
    _CvpdnBundleChildTunnelType_Type()
)
cvpdnBundleChildTunnelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpdnBundleChildTunnelType.setStatus("current")
_CvpdnBundleChildTunnelId_Type = Unsigned32
_CvpdnBundleChildTunnelId_Object = MibTableColumn
cvpdnBundleChildTunnelId = _CvpdnBundleChildTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 6, 1, 2),
    _CvpdnBundleChildTunnelId_Type()
)
cvpdnBundleChildTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpdnBundleChildTunnelId.setStatus("current")
_CvpdnBundleChildSessionId_Type = Unsigned32
_CvpdnBundleChildSessionId_Object = MibTableColumn
cvpdnBundleChildSessionId = _CvpdnBundleChildSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 1, 6, 6, 1, 3),
    _CvpdnBundleChildSessionId_Type()
)
cvpdnBundleChildSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpdnBundleChildSessionId.setStatus("current")
_CiscoVpdnMgmtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVpdnMgmtMIBConformance = _CiscoVpdnMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3)
)
_CiscoVpdnMgmtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVpdnMgmtMIBCompliances = _CiscoVpdnMgmtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 1)
)
_CiscoVpdnMgmtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVpdnMgmtMIBGroups = _CiscoVpdnMgmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2)
)

# Managed Objects groups

cvpdnSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 1)
)
cvpdnSystemInfoGroup.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelTotal"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionTotal"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnDeniedUsersTotal"))
)
if mibBuilder.loadTexts:
    cvpdnSystemInfoGroup.setStatus("obsolete")

cvpdnTunnelInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 2)
)
cvpdnTunnelInfoGroup.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelRemoteTunnelId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelLocalName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelRemoteName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelRemoteEndpointName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelLocalInitConnection"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelOrigCause"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelState"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelActiveSessions"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelDeniedUsers"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSoftshut"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelNetworkServiceType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelLocalIpAddress"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSourceIpAddress"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelRemoteIpAddress"))
)
if mibBuilder.loadTexts:
    cvpdnTunnelInfoGroup.setStatus("obsolete")

cvpdnTunnelSessionInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 3)
)
cvpdnTunnelSessionInfoGroup.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionUserName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionState"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionCallDuration"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionPacketsOut"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionBytesOut"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionPacketsIn"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionBytesIn"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionDeviceType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionDeviceCallerId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionDevicePhyId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionMultilink"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionModemSlotIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionModemPortIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionDS1SlotIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionDS1PortIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionDS1ChannelIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionModemCallStartTime"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelSessionModemCallStartIndex"))
)
if mibBuilder.loadTexts:
    cvpdnTunnelSessionInfoGroup.setStatus("obsolete")

cvpdnUserToFailHistInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 4)
)
cvpdnUserToFailHistInfoGroup.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistUserId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistLocalInitConn"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistLocalName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistRemoteName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistSourceIp"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistDestIp"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistCount"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistFailTime"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistFailType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistFailReason"))
)
if mibBuilder.loadTexts:
    cvpdnUserToFailHistInfoGroup.setStatus("deprecated")

cvpdnSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 5)
)
cvpdnSystemGroup.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnSystemTunnelTotal"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSystemSessionTotal"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSystemDeniedUsersTotal"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSystemInitialConnReq"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSystemSuccessConnReq"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSystemFailedConnReq"))
)
if mibBuilder.loadTexts:
    cvpdnSystemGroup.setStatus("current")

cvpdnTunnelAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 6)
)
cvpdnTunnelAttrGroup.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrRemoteTunnelId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrLocalName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrRemoteName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrRemoteEndpointName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrLocalInitConnection"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrOrigCause"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrState"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrActiveSessions"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrDeniedUsers"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrSoftshut"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrNetworkServiceType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrLocalIpAddress"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrSourceIpAddress"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrRemoteIpAddress"))
)
if mibBuilder.loadTexts:
    cvpdnTunnelAttrGroup.setStatus("deprecated")

cvpdnSessionAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 7)
)
cvpdnSessionAttrGroup.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrUserName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrState"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrCallDuration"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrPacketsOut"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrBytesOut"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrPacketsIn"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrBytesIn"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDeviceType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDeviceCallerId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDevicePhyId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrMultilink"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrModemSlotIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrModemPortIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDS1SlotIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDS1PortIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDS1ChannelIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrModemCallStartTime"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrModemCallStartIndex"))
)
if mibBuilder.loadTexts:
    cvpdnSessionAttrGroup.setStatus("deprecated")

cvpdnSessionAttrGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 8)
)
cvpdnSessionAttrGroupRev1.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrUserName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrState"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrCallDuration"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrPacketsOut"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrBytesOut"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrPacketsIn"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrBytesIn"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDeviceType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDeviceCallerId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDevicePhyId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrMultilink"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrModemSlotIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrModemPortIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDS1SlotIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDS1PortIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDS1ChannelIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrModemCallStartTime"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrModemCallStartIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrVirtualCircuitID"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrSentPktsDropped"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrRecvPktsDropped"))
)
if mibBuilder.loadTexts:
    cvpdnSessionAttrGroupRev1.setStatus("current")

cvpdnNotifEnabledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 9)
)
cvpdnNotifEnabledGroup.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnSystemNotifSessionEnabled"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnNotifSessionID"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnNotifSessionEvent"))
)
if mibBuilder.loadTexts:
    cvpdnNotifEnabledGroup.setStatus("current")

cvpdnTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 11)
)
cvpdnTemplateGroup.setObjects(
    ("CISCO-VPDN-MGMT-MIB", "cvpdnTemplateActiveSessions")
)
if mibBuilder.loadTexts:
    cvpdnTemplateGroup.setStatus("current")

cvpdnConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 12)
)
cvpdnConfigGroup.setObjects(
    ("CISCO-VPDN-MGMT-MIB", "cvpdnSystemClearSessions")
)
if mibBuilder.loadTexts:
    cvpdnConfigGroup.setStatus("current")

cvpdnMultilinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 13)
)
cvpdnMultilinkGroup.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrMultilinkBundle"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrMultilinkIfIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundlesWithOneLink"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundlesWithTwoLinks"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundlesWithMoreThanTwoLinks"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundleLinkCount"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundleEndpointType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundleEndpoint"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundlePeerIpAddrType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundlePeerIpAddr"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundleLastChanged"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundleChildSessionId"))
)
if mibBuilder.loadTexts:
    cvpdnMultilinkGroup.setStatus("deprecated")

cvpdnMultilinkGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 14)
)
cvpdnMultilinkGroupRev1.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrMultilinkBundle"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrMultilinkIfIndex"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundlesWithOneLink"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundlesWithTwoLinks"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundlesWithMoreThanTwoLinks"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundleLinkCount"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundleEndpoint"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundlePeerIpAddrType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundlePeerIpAddr"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundleLastChanged"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundleChildSessionId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnBundleEndpointClass"))
)
if mibBuilder.loadTexts:
    cvpdnMultilinkGroupRev1.setStatus("current")

cvpdnUserToFailHistInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 15)
)
cvpdnUserToFailHistInfoGroupRev1.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistUserId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistLocalInitConn"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistLocalName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistRemoteName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistCount"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistFailTime"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistFailType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistFailReason"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistSourceInetType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistSourceInetAddr"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistDestInetType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnUnameToFailHistDestInetAddr"))
)
if mibBuilder.loadTexts:
    cvpdnUserToFailHistInfoGroupRev1.setStatus("current")

cvpdnTunnelAttrGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 16)
)
cvpdnTunnelAttrGroupRev1.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrRemoteTunnelId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrLocalName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrRemoteName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrRemoteEndpointName"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrLocalInitConnection"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrOrigCause"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrState"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrActiveSessions"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrDeniedUsers"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrSoftshut"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrNetworkServiceType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrLocalInetAddressType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrLocalInetAddress"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrSourceInetAddressType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrSourceInetAddress"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrRemoteInetAddressType"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnTunnelAttrRemoteInetAddress"))
)
if mibBuilder.loadTexts:
    cvpdnTunnelAttrGroupRev1.setStatus("current")


# Notification objects

cvpdnNotifSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 0, 3)
)
cvpdnNotifSession.setObjects(
      *(("CISCO-VPDN-MGMT-MIB", "cvpdnNotifSessionID"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnNotifSessionEvent"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrDevicePhyId"),
        ("CISCO-VPDN-MGMT-MIB", "cvpdnSessionAttrVirtualCircuitID"))
)
if mibBuilder.loadTexts:
    cvpdnNotifSession.setStatus(
        "current"
    )


# Notifications groups

cvpdnSessionNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 2, 10)
)
cvpdnSessionNotifGroup.setObjects(
    ("CISCO-VPDN-MGMT-MIB", "cvpdnNotifSession")
)
if mibBuilder.loadTexts:
    cvpdnSessionNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoVpdnMgmtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVpdnMgmtMIBCompliance.setStatus(
        "obsolete"
    )

ciscoVpdnMgmtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoVpdnMgmtMIBComplianceRev1.setStatus(
        "obsolete"
    )

ciscoVpdnMgmtMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoVpdnMgmtMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoVpdnMgmtMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoVpdnMgmtMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoVpdnMgmtMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoVpdnMgmtMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoVpdnMgmtMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 24, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoVpdnMgmtMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VPDN-MGMT-MIB",
    **{"TunnelType": TunnelType,
       "EndpointClass": EndpointClass,
       "ciscoVpdnMgmtMIB": ciscoVpdnMgmtMIB,
       "ciscoVpdnMgmtMIBNotifs": ciscoVpdnMgmtMIBNotifs,
       "cvpdnNotifSessionID": cvpdnNotifSessionID,
       "cvpdnNotifSessionEvent": cvpdnNotifSessionEvent,
       "cvpdnNotifSession": cvpdnNotifSession,
       "ciscoVpdnMgmtMIBObjects": ciscoVpdnMgmtMIBObjects,
       "cvpdnSystemInfo": cvpdnSystemInfo,
       "cvpdnTunnelTotal": cvpdnTunnelTotal,
       "cvpdnSessionTotal": cvpdnSessionTotal,
       "cvpdnDeniedUsersTotal": cvpdnDeniedUsersTotal,
       "cvpdnSystemTable": cvpdnSystemTable,
       "cvpdnSystemEntry": cvpdnSystemEntry,
       "cvpdnSystemTunnelType": cvpdnSystemTunnelType,
       "cvpdnSystemTunnelTotal": cvpdnSystemTunnelTotal,
       "cvpdnSystemSessionTotal": cvpdnSystemSessionTotal,
       "cvpdnSystemDeniedUsersTotal": cvpdnSystemDeniedUsersTotal,
       "cvpdnSystemInitialConnReq": cvpdnSystemInitialConnReq,
       "cvpdnSystemSuccessConnReq": cvpdnSystemSuccessConnReq,
       "cvpdnSystemFailedConnReq": cvpdnSystemFailedConnReq,
       "cvpdnSystemNotifSessionEnabled": cvpdnSystemNotifSessionEnabled,
       "cvpdnSystemClearSessions": cvpdnSystemClearSessions,
       "cvpdnTunnelInfo": cvpdnTunnelInfo,
       "cvpdnTunnelTable": cvpdnTunnelTable,
       "cvpdnTunnelEntry": cvpdnTunnelEntry,
       "cvpdnTunnelTunnelId": cvpdnTunnelTunnelId,
       "cvpdnTunnelRemoteTunnelId": cvpdnTunnelRemoteTunnelId,
       "cvpdnTunnelLocalName": cvpdnTunnelLocalName,
       "cvpdnTunnelRemoteName": cvpdnTunnelRemoteName,
       "cvpdnTunnelRemoteEndpointName": cvpdnTunnelRemoteEndpointName,
       "cvpdnTunnelLocalInitConnection": cvpdnTunnelLocalInitConnection,
       "cvpdnTunnelOrigCause": cvpdnTunnelOrigCause,
       "cvpdnTunnelState": cvpdnTunnelState,
       "cvpdnTunnelActiveSessions": cvpdnTunnelActiveSessions,
       "cvpdnTunnelDeniedUsers": cvpdnTunnelDeniedUsers,
       "cvpdnTunnelSoftshut": cvpdnTunnelSoftshut,
       "cvpdnTunnelNetworkServiceType": cvpdnTunnelNetworkServiceType,
       "cvpdnTunnelLocalIpAddress": cvpdnTunnelLocalIpAddress,
       "cvpdnTunnelSourceIpAddress": cvpdnTunnelSourceIpAddress,
       "cvpdnTunnelRemoteIpAddress": cvpdnTunnelRemoteIpAddress,
       "cvpdnTunnelAttrTable": cvpdnTunnelAttrTable,
       "cvpdnTunnelAttrEntry": cvpdnTunnelAttrEntry,
       "cvpdnTunnelAttrTunnelId": cvpdnTunnelAttrTunnelId,
       "cvpdnTunnelAttrRemoteTunnelId": cvpdnTunnelAttrRemoteTunnelId,
       "cvpdnTunnelAttrLocalName": cvpdnTunnelAttrLocalName,
       "cvpdnTunnelAttrRemoteName": cvpdnTunnelAttrRemoteName,
       "cvpdnTunnelAttrRemoteEndpointName": cvpdnTunnelAttrRemoteEndpointName,
       "cvpdnTunnelAttrLocalInitConnection": cvpdnTunnelAttrLocalInitConnection,
       "cvpdnTunnelAttrOrigCause": cvpdnTunnelAttrOrigCause,
       "cvpdnTunnelAttrState": cvpdnTunnelAttrState,
       "cvpdnTunnelAttrActiveSessions": cvpdnTunnelAttrActiveSessions,
       "cvpdnTunnelAttrDeniedUsers": cvpdnTunnelAttrDeniedUsers,
       "cvpdnTunnelAttrSoftshut": cvpdnTunnelAttrSoftshut,
       "cvpdnTunnelAttrNetworkServiceType": cvpdnTunnelAttrNetworkServiceType,
       "cvpdnTunnelAttrLocalIpAddress": cvpdnTunnelAttrLocalIpAddress,
       "cvpdnTunnelAttrSourceIpAddress": cvpdnTunnelAttrSourceIpAddress,
       "cvpdnTunnelAttrRemoteIpAddress": cvpdnTunnelAttrRemoteIpAddress,
       "cvpdnTunnelAttrLocalInetAddressType": cvpdnTunnelAttrLocalInetAddressType,
       "cvpdnTunnelAttrLocalInetAddress": cvpdnTunnelAttrLocalInetAddress,
       "cvpdnTunnelAttrSourceInetAddressType": cvpdnTunnelAttrSourceInetAddressType,
       "cvpdnTunnelAttrSourceInetAddress": cvpdnTunnelAttrSourceInetAddress,
       "cvpdnTunnelAttrRemoteInetAddressType": cvpdnTunnelAttrRemoteInetAddressType,
       "cvpdnTunnelAttrRemoteInetAddress": cvpdnTunnelAttrRemoteInetAddress,
       "cvpdnTunnelSessionInfo": cvpdnTunnelSessionInfo,
       "cvpdnTunnelSessionTable": cvpdnTunnelSessionTable,
       "cvpdnTunnelSessionEntry": cvpdnTunnelSessionEntry,
       "cvpdnTunnelSessionId": cvpdnTunnelSessionId,
       "cvpdnTunnelSessionUserName": cvpdnTunnelSessionUserName,
       "cvpdnTunnelSessionState": cvpdnTunnelSessionState,
       "cvpdnTunnelSessionCallDuration": cvpdnTunnelSessionCallDuration,
       "cvpdnTunnelSessionPacketsOut": cvpdnTunnelSessionPacketsOut,
       "cvpdnTunnelSessionBytesOut": cvpdnTunnelSessionBytesOut,
       "cvpdnTunnelSessionPacketsIn": cvpdnTunnelSessionPacketsIn,
       "cvpdnTunnelSessionBytesIn": cvpdnTunnelSessionBytesIn,
       "cvpdnTunnelSessionDeviceType": cvpdnTunnelSessionDeviceType,
       "cvpdnTunnelSessionDeviceCallerId": cvpdnTunnelSessionDeviceCallerId,
       "cvpdnTunnelSessionDevicePhyId": cvpdnTunnelSessionDevicePhyId,
       "cvpdnTunnelSessionMultilink": cvpdnTunnelSessionMultilink,
       "cvpdnTunnelSessionModemSlotIndex": cvpdnTunnelSessionModemSlotIndex,
       "cvpdnTunnelSessionModemPortIndex": cvpdnTunnelSessionModemPortIndex,
       "cvpdnTunnelSessionDS1SlotIndex": cvpdnTunnelSessionDS1SlotIndex,
       "cvpdnTunnelSessionDS1PortIndex": cvpdnTunnelSessionDS1PortIndex,
       "cvpdnTunnelSessionDS1ChannelIndex": cvpdnTunnelSessionDS1ChannelIndex,
       "cvpdnTunnelSessionModemCallStartTime": cvpdnTunnelSessionModemCallStartTime,
       "cvpdnTunnelSessionModemCallStartIndex": cvpdnTunnelSessionModemCallStartIndex,
       "cvpdnSessionAttrTable": cvpdnSessionAttrTable,
       "cvpdnSessionAttrEntry": cvpdnSessionAttrEntry,
       "cvpdnSessionAttrSessionId": cvpdnSessionAttrSessionId,
       "cvpdnSessionAttrUserName": cvpdnSessionAttrUserName,
       "cvpdnSessionAttrState": cvpdnSessionAttrState,
       "cvpdnSessionAttrCallDuration": cvpdnSessionAttrCallDuration,
       "cvpdnSessionAttrPacketsOut": cvpdnSessionAttrPacketsOut,
       "cvpdnSessionAttrBytesOut": cvpdnSessionAttrBytesOut,
       "cvpdnSessionAttrPacketsIn": cvpdnSessionAttrPacketsIn,
       "cvpdnSessionAttrBytesIn": cvpdnSessionAttrBytesIn,
       "cvpdnSessionAttrDeviceType": cvpdnSessionAttrDeviceType,
       "cvpdnSessionAttrDeviceCallerId": cvpdnSessionAttrDeviceCallerId,
       "cvpdnSessionAttrDevicePhyId": cvpdnSessionAttrDevicePhyId,
       "cvpdnSessionAttrMultilink": cvpdnSessionAttrMultilink,
       "cvpdnSessionAttrModemSlotIndex": cvpdnSessionAttrModemSlotIndex,
       "cvpdnSessionAttrModemPortIndex": cvpdnSessionAttrModemPortIndex,
       "cvpdnSessionAttrDS1SlotIndex": cvpdnSessionAttrDS1SlotIndex,
       "cvpdnSessionAttrDS1PortIndex": cvpdnSessionAttrDS1PortIndex,
       "cvpdnSessionAttrDS1ChannelIndex": cvpdnSessionAttrDS1ChannelIndex,
       "cvpdnSessionAttrModemCallStartTime": cvpdnSessionAttrModemCallStartTime,
       "cvpdnSessionAttrModemCallStartIndex": cvpdnSessionAttrModemCallStartIndex,
       "cvpdnSessionAttrVirtualCircuitID": cvpdnSessionAttrVirtualCircuitID,
       "cvpdnSessionAttrSentPktsDropped": cvpdnSessionAttrSentPktsDropped,
       "cvpdnSessionAttrRecvPktsDropped": cvpdnSessionAttrRecvPktsDropped,
       "cvpdnSessionAttrMultilinkBundle": cvpdnSessionAttrMultilinkBundle,
       "cvpdnSessionAttrMultilinkIfIndex": cvpdnSessionAttrMultilinkIfIndex,
       "cvpdnUserToFailHistInfo": cvpdnUserToFailHistInfo,
       "cvpdnUserToFailHistInfoTable": cvpdnUserToFailHistInfoTable,
       "cvpdnUserToFailHistInfoEntry": cvpdnUserToFailHistInfoEntry,
       "cvpdnUnameToFailHistUname": cvpdnUnameToFailHistUname,
       "cvpdnUnameToFailHistTunnelId": cvpdnUnameToFailHistTunnelId,
       "cvpdnUnameToFailHistUserId": cvpdnUnameToFailHistUserId,
       "cvpdnUnameToFailHistLocalInitConn": cvpdnUnameToFailHistLocalInitConn,
       "cvpdnUnameToFailHistLocalName": cvpdnUnameToFailHistLocalName,
       "cvpdnUnameToFailHistRemoteName": cvpdnUnameToFailHistRemoteName,
       "cvpdnUnameToFailHistSourceIp": cvpdnUnameToFailHistSourceIp,
       "cvpdnUnameToFailHistDestIp": cvpdnUnameToFailHistDestIp,
       "cvpdnUnameToFailHistCount": cvpdnUnameToFailHistCount,
       "cvpdnUnameToFailHistFailTime": cvpdnUnameToFailHistFailTime,
       "cvpdnUnameToFailHistFailType": cvpdnUnameToFailHistFailType,
       "cvpdnUnameToFailHistFailReason": cvpdnUnameToFailHistFailReason,
       "cvpdnUnameToFailHistSourceInetType": cvpdnUnameToFailHistSourceInetType,
       "cvpdnUnameToFailHistSourceInetAddr": cvpdnUnameToFailHistSourceInetAddr,
       "cvpdnUnameToFailHistDestInetType": cvpdnUnameToFailHistDestInetType,
       "cvpdnUnameToFailHistDestInetAddr": cvpdnUnameToFailHistDestInetAddr,
       "cvpdnTemplateInfo": cvpdnTemplateInfo,
       "cvpdnTemplateTable": cvpdnTemplateTable,
       "cvpdnTemplateEntry": cvpdnTemplateEntry,
       "cvpdnTemplateName": cvpdnTemplateName,
       "cvpdnTemplateActiveSessions": cvpdnTemplateActiveSessions,
       "cvpdnMultilinkInfo": cvpdnMultilinkInfo,
       "cvpdnBundlesWithOneLink": cvpdnBundlesWithOneLink,
       "cvpdnBundlesWithTwoLinks": cvpdnBundlesWithTwoLinks,
       "cvpdnBundlesWithMoreThanTwoLinks": cvpdnBundlesWithMoreThanTwoLinks,
       "cvpdnBundleTable": cvpdnBundleTable,
       "cvpdnBundleEntry": cvpdnBundleEntry,
       "cvpdnBundleName": cvpdnBundleName,
       "cvpdnBundleLinkCount": cvpdnBundleLinkCount,
       "cvpdnBundleEndpointType": cvpdnBundleEndpointType,
       "cvpdnBundleEndpoint": cvpdnBundleEndpoint,
       "cvpdnBundlePeerIpAddrType": cvpdnBundlePeerIpAddrType,
       "cvpdnBundlePeerIpAddr": cvpdnBundlePeerIpAddr,
       "cvpdnBundleEndpointClass": cvpdnBundleEndpointClass,
       "cvpdnBundleLastChanged": cvpdnBundleLastChanged,
       "cvpdnBundleChildTable": cvpdnBundleChildTable,
       "cvpdnBundleChildEntry": cvpdnBundleChildEntry,
       "cvpdnBundleChildTunnelType": cvpdnBundleChildTunnelType,
       "cvpdnBundleChildTunnelId": cvpdnBundleChildTunnelId,
       "cvpdnBundleChildSessionId": cvpdnBundleChildSessionId,
       "ciscoVpdnMgmtMIBConformance": ciscoVpdnMgmtMIBConformance,
       "ciscoVpdnMgmtMIBCompliances": ciscoVpdnMgmtMIBCompliances,
       "ciscoVpdnMgmtMIBCompliance": ciscoVpdnMgmtMIBCompliance,
       "ciscoVpdnMgmtMIBComplianceRev1": ciscoVpdnMgmtMIBComplianceRev1,
       "ciscoVpdnMgmtMIBComplianceRev2": ciscoVpdnMgmtMIBComplianceRev2,
       "ciscoVpdnMgmtMIBComplianceRev3": ciscoVpdnMgmtMIBComplianceRev3,
       "ciscoVpdnMgmtMIBComplianceRev4": ciscoVpdnMgmtMIBComplianceRev4,
       "ciscoVpdnMgmtMIBComplianceRev5": ciscoVpdnMgmtMIBComplianceRev5,
       "ciscoVpdnMgmtMIBGroups": ciscoVpdnMgmtMIBGroups,
       "cvpdnSystemInfoGroup": cvpdnSystemInfoGroup,
       "cvpdnTunnelInfoGroup": cvpdnTunnelInfoGroup,
       "cvpdnTunnelSessionInfoGroup": cvpdnTunnelSessionInfoGroup,
       "cvpdnUserToFailHistInfoGroup": cvpdnUserToFailHistInfoGroup,
       "cvpdnSystemGroup": cvpdnSystemGroup,
       "cvpdnTunnelAttrGroup": cvpdnTunnelAttrGroup,
       "cvpdnSessionAttrGroup": cvpdnSessionAttrGroup,
       "cvpdnSessionAttrGroupRev1": cvpdnSessionAttrGroupRev1,
       "cvpdnNotifEnabledGroup": cvpdnNotifEnabledGroup,
       "cvpdnSessionNotifGroup": cvpdnSessionNotifGroup,
       "cvpdnTemplateGroup": cvpdnTemplateGroup,
       "cvpdnConfigGroup": cvpdnConfigGroup,
       "cvpdnMultilinkGroup": cvpdnMultilinkGroup,
       "cvpdnMultilinkGroupRev1": cvpdnMultilinkGroupRev1,
       "cvpdnUserToFailHistInfoGroupRev1": cvpdnUserToFailHistInfoGroupRev1,
       "cvpdnTunnelAttrGroupRev1": cvpdnTunnelAttrGroupRev1}
)

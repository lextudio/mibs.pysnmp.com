# SNMP MIB module (WLSX-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-AUTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:04 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaAuthServerType,
 ArubaAuthenticationMethods,
 ArubaEnableValue,
 ArubaEncryptionMethods,
 ArubaHashAlgorithms) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaAuthServerType",
    "ArubaAuthenticationMethods",
    "ArubaEnableValue",
    "ArubaEncryptionMethods",
    "ArubaHashAlgorithms")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

wlsxAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8)
)
wlsxAuthMIB.setRevisions(
        ("1906-11-27 20:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxAuthenticationServerGroup_ObjectIdentity = ObjectIdentity
wlsxAuthenticationServerGroup = _WlsxAuthenticationServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1)
)
_WlsxAuthenticationServerTable_Object = MibTable
wlsxAuthenticationServerTable = _WlsxAuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxAuthenticationServerTable.setStatus("current")
_WlsxAuthenticationServerEntry_Object = MibTableRow
wlsxAuthenticationServerEntry = _WlsxAuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1)
)
wlsxAuthenticationServerEntry.setIndexNames(
    (0, "WLSX-AUTH-MIB", "authServerName"),
)
if mibBuilder.loadTexts:
    wlsxAuthenticationServerEntry.setStatus("current")


class _AuthServerName_Type(DisplayString):
    """Custom type authServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AuthServerName_Type.__name__ = "DisplayString"
_AuthServerName_Object = MibTableColumn
authServerName = _AuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 1),
    _AuthServerName_Type()
)
authServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    authServerName.setStatus("current")
_AuthServerType_Type = ArubaAuthServerType
_AuthServerType_Object = MibTableColumn
authServerType = _AuthServerType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 2),
    _AuthServerType_Type()
)
authServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authServerType.setStatus("current")


class _AuthServerAddress_Type(DisplayString):
    """Custom type authServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_AuthServerAddress_Type.__name__ = "DisplayString"
_AuthServerAddress_Object = MibTableColumn
authServerAddress = _AuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 3),
    _AuthServerAddress_Type()
)
authServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authServerAddress.setStatus("current")
_AuthServerPort_Type = Integer32
_AuthServerPort_Object = MibTableColumn
authServerPort = _AuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 4),
    _AuthServerPort_Type()
)
authServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authServerPort.setStatus("current")
_AuthServerRetryCount_Type = Integer32
_AuthServerRetryCount_Object = MibTableColumn
authServerRetryCount = _AuthServerRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 5),
    _AuthServerRetryCount_Type()
)
authServerRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authServerRetryCount.setStatus("current")
_AuthServerTimeOutValue_Type = Integer32
_AuthServerTimeOutValue_Object = MibTableColumn
authServerTimeOutValue = _AuthServerTimeOutValue_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 6),
    _AuthServerTimeOutValue_Type()
)
authServerTimeOutValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authServerTimeOutValue.setStatus("current")
_AuthServerState_Type = ArubaEnableValue
_AuthServerState_Object = MibTableColumn
authServerState = _AuthServerState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 7),
    _AuthServerState_Type()
)
authServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authServerState.setStatus("current")
_AuthServerInservice_Type = TruthValue
_AuthServerInservice_Object = MibTableColumn
authServerInservice = _AuthServerInservice_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 8),
    _AuthServerInservice_Type()
)
authServerInservice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authServerInservice.setStatus("current")
_AuthServerUsageCount_Type = Counter32
_AuthServerUsageCount_Object = MibTableColumn
authServerUsageCount = _AuthServerUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 9),
    _AuthServerUsageCount_Type()
)
authServerUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authServerUsageCount.setStatus("current")
_AuthServerSuccessfullAuths_Type = Counter32
_AuthServerSuccessfullAuths_Object = MibTableColumn
authServerSuccessfullAuths = _AuthServerSuccessfullAuths_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 10),
    _AuthServerSuccessfullAuths_Type()
)
authServerSuccessfullAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authServerSuccessfullAuths.setStatus("current")
_AuthServerFailedAuths_Type = Counter32
_AuthServerFailedAuths_Object = MibTableColumn
authServerFailedAuths = _AuthServerFailedAuths_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 11),
    _AuthServerFailedAuths_Type()
)
authServerFailedAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authServerFailedAuths.setStatus("current")
_AuthServerTimeouts_Type = Counter32
_AuthServerTimeouts_Object = MibTableColumn
authServerTimeouts = _AuthServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 12),
    _AuthServerTimeouts_Type()
)
authServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authServerTimeouts.setStatus("current")
_AuthServerAvgResponseTime_Type = Integer32
_AuthServerAvgResponseTime_Object = MibTableColumn
authServerAvgResponseTime = _AuthServerAvgResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 13),
    _AuthServerAvgResponseTime_Type()
)
authServerAvgResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authServerAvgResponseTime.setStatus("current")
_AuthServerOutStandingRequests_Type = Integer32
_AuthServerOutStandingRequests_Object = MibTableColumn
authServerOutStandingRequests = _AuthServerOutStandingRequests_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 14),
    _AuthServerOutStandingRequests_Type()
)
authServerOutStandingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authServerOutStandingRequests.setStatus("current")
_AuthServerUptime_Type = Integer32
_AuthServerUptime_Object = MibTableColumn
authServerUptime = _AuthServerUptime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 1, 1, 15),
    _AuthServerUptime_Type()
)
authServerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authServerUptime.setStatus("current")
_WlsxPortalServerTable_Object = MibTable
wlsxPortalServerTable = _WlsxPortalServerTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxPortalServerTable.setStatus("current")
_WlsxPortalServerEntry_Object = MibTableRow
wlsxPortalServerEntry = _WlsxPortalServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 2, 1)
)
wlsxPortalServerEntry.setIndexNames(
    (0, "WLSX-AUTH-MIB", "portalServerIndex"),
)
if mibBuilder.loadTexts:
    wlsxPortalServerEntry.setStatus("current")


class _PortalServerIndex_Type(DisplayString):
    """Custom type portalServerIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PortalServerIndex_Type.__name__ = "DisplayString"
_PortalServerIndex_Object = MibTableColumn
portalServerIndex = _PortalServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 2, 1, 1),
    _PortalServerIndex_Type()
)
portalServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portalServerIndex.setStatus("current")


class _PortalServerHost_Type(DisplayString):
    """Custom type portalServerHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PortalServerHost_Type.__name__ = "DisplayString"
_PortalServerHost_Object = MibTableColumn
portalServerHost = _PortalServerHost_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 2, 1, 2),
    _PortalServerHost_Type()
)
portalServerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portalServerHost.setStatus("current")
_PortalServerPort_Type = Integer32
_PortalServerPort_Object = MibTableColumn
portalServerPort = _PortalServerPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 2, 1, 3),
    _PortalServerPort_Type()
)
portalServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portalServerPort.setStatus("current")


class _PortalServerPage_Type(DisplayString):
    """Custom type portalServerPage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PortalServerPage_Type.__name__ = "DisplayString"
_PortalServerPage_Object = MibTableColumn
portalServerPage = _PortalServerPage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 2, 1, 4),
    _PortalServerPage_Type()
)
portalServerPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portalServerPage.setStatus("current")
_PortalServerProtocol_Type = DisplayString
_PortalServerProtocol_Object = MibTableColumn
portalServerProtocol = _PortalServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 2, 1, 5),
    _PortalServerProtocol_Type()
)
portalServerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portalServerProtocol.setStatus("current")
_WlsxLdapServerStateTable_Object = MibTable
wlsxLdapServerStateTable = _WlsxLdapServerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 5)
)
if mibBuilder.loadTexts:
    wlsxLdapServerStateTable.setStatus("current")
_WlsxLdapServerStateEntry_Object = MibTableRow
wlsxLdapServerStateEntry = _WlsxLdapServerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 5, 1)
)
wlsxLdapServerStateEntry.setIndexNames(
    (0, "WLSX-AUTH-MIB", "authServerName"),
)
if mibBuilder.loadTexts:
    wlsxLdapServerStateEntry.setStatus("current")
_LdapInitDone_Type = TruthValue
_LdapInitDone_Object = MibTableColumn
ldapInitDone = _LdapInitDone_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 5, 1, 1),
    _LdapInitDone_Type()
)
ldapInitDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapInitDone.setStatus("current")


class _LdapAdminBound_Type(Integer32):
    """Custom type ldapAdminBound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 3),
          ("no", 1),
          ("yes", 2))
    )


_LdapAdminBound_Type.__name__ = "Integer32"
_LdapAdminBound_Object = MibTableColumn
ldapAdminBound = _LdapAdminBound_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 5, 1, 2),
    _LdapAdminBound_Type()
)
ldapAdminBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapAdminBound.setStatus("current")
_LdapReBindCount_Type = Counter32
_LdapReBindCount_Object = MibTableColumn
ldapReBindCount = _LdapReBindCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 1, 5, 1, 3),
    _LdapReBindCount_Type()
)
ldapReBindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapReBindCount.setStatus("current")
_WlsxAuthenticationInfoGroup_ObjectIdentity = ObjectIdentity
wlsxAuthenticationInfoGroup = _WlsxAuthenticationInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 2)
)
_WlsxAuthenticationGroup_ObjectIdentity = ObjectIdentity
wlsxAuthenticationGroup = _WlsxAuthenticationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 8, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-AUTH-MIB",
    **{"wlsxAuthMIB": wlsxAuthMIB,
       "wlsxAuthenticationServerGroup": wlsxAuthenticationServerGroup,
       "wlsxAuthenticationServerTable": wlsxAuthenticationServerTable,
       "wlsxAuthenticationServerEntry": wlsxAuthenticationServerEntry,
       "authServerName": authServerName,
       "authServerType": authServerType,
       "authServerAddress": authServerAddress,
       "authServerPort": authServerPort,
       "authServerRetryCount": authServerRetryCount,
       "authServerTimeOutValue": authServerTimeOutValue,
       "authServerState": authServerState,
       "authServerInservice": authServerInservice,
       "authServerUsageCount": authServerUsageCount,
       "authServerSuccessfullAuths": authServerSuccessfullAuths,
       "authServerFailedAuths": authServerFailedAuths,
       "authServerTimeouts": authServerTimeouts,
       "authServerAvgResponseTime": authServerAvgResponseTime,
       "authServerOutStandingRequests": authServerOutStandingRequests,
       "authServerUptime": authServerUptime,
       "wlsxPortalServerTable": wlsxPortalServerTable,
       "wlsxPortalServerEntry": wlsxPortalServerEntry,
       "portalServerIndex": portalServerIndex,
       "portalServerHost": portalServerHost,
       "portalServerPort": portalServerPort,
       "portalServerPage": portalServerPage,
       "portalServerProtocol": portalServerProtocol,
       "wlsxLdapServerStateTable": wlsxLdapServerStateTable,
       "wlsxLdapServerStateEntry": wlsxLdapServerStateEntry,
       "ldapInitDone": ldapInitDone,
       "ldapAdminBound": ldapAdminBound,
       "ldapReBindCount": ldapReBindCount,
       "wlsxAuthenticationInfoGroup": wlsxAuthenticationInfoGroup,
       "wlsxAuthenticationGroup": wlsxAuthenticationGroup}
)

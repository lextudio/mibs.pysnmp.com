# SNMP MIB module (Unisphere-Data-SSC-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-SSC-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:40 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdName,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdName")


# MODULE-IDENTITY

usdSscClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36)
)
usdSscClientMIB.setRevisions(
        ("2002-01-14 20:15",
         "2001-01-23 21:30",
         "2000-02-17 23:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdSscClientObjects_ObjectIdentity = ObjectIdentity
usdSscClientObjects = _UsdSscClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1)
)
_UsdSscClientCfg_ObjectIdentity = ObjectIdentity
usdSscClientCfg = _UsdSscClientCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1)
)
_UsdSscClientCfgScalars_ObjectIdentity = ObjectIdentity
usdSscClientCfgScalars = _UsdSscClientCfgScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1)
)


class _UsdSscClientServerSwitchoverTimeout_Type(Integer32):
    """Custom type usdSscClientServerSwitchoverTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_UsdSscClientServerSwitchoverTimeout_Type.__name__ = "Integer32"
_UsdSscClientServerSwitchoverTimeout_Object = MibScalar
usdSscClientServerSwitchoverTimeout = _UsdSscClientServerSwitchoverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 1),
    _UsdSscClientServerSwitchoverTimeout_Type()
)
usdSscClientServerSwitchoverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSscClientServerSwitchoverTimeout.setStatus("current")
if mibBuilder.loadTexts:
    usdSscClientServerSwitchoverTimeout.setUnits("seconds")
_UsdSscClientPrimaryAddress_Type = IpAddress
_UsdSscClientPrimaryAddress_Object = MibScalar
usdSscClientPrimaryAddress = _UsdSscClientPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 2),
    _UsdSscClientPrimaryAddress_Type()
)
usdSscClientPrimaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSscClientPrimaryAddress.setStatus("current")


class _UsdSscClientPrimaryPort_Type(Integer32):
    """Custom type usdSscClientPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdSscClientPrimaryPort_Type.__name__ = "Integer32"
_UsdSscClientPrimaryPort_Object = MibScalar
usdSscClientPrimaryPort = _UsdSscClientPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 3),
    _UsdSscClientPrimaryPort_Type()
)
usdSscClientPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSscClientPrimaryPort.setStatus("current")
_UsdSscClientSecondaryAddress_Type = IpAddress
_UsdSscClientSecondaryAddress_Object = MibScalar
usdSscClientSecondaryAddress = _UsdSscClientSecondaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 4),
    _UsdSscClientSecondaryAddress_Type()
)
usdSscClientSecondaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSscClientSecondaryAddress.setStatus("current")


class _UsdSscClientSecondaryPort_Type(Integer32):
    """Custom type usdSscClientSecondaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdSscClientSecondaryPort_Type.__name__ = "Integer32"
_UsdSscClientSecondaryPort_Object = MibScalar
usdSscClientSecondaryPort = _UsdSscClientSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 5),
    _UsdSscClientSecondaryPort_Type()
)
usdSscClientSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSscClientSecondaryPort.setStatus("current")
_UsdSscClientTertiaryAddress_Type = IpAddress
_UsdSscClientTertiaryAddress_Object = MibScalar
usdSscClientTertiaryAddress = _UsdSscClientTertiaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 6),
    _UsdSscClientTertiaryAddress_Type()
)
usdSscClientTertiaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSscClientTertiaryAddress.setStatus("current")


class _UsdSscClientTertiaryPort_Type(Integer32):
    """Custom type usdSscClientTertiaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdSscClientTertiaryPort_Type.__name__ = "Integer32"
_UsdSscClientTertiaryPort_Object = MibScalar
usdSscClientTertiaryPort = _UsdSscClientTertiaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 7),
    _UsdSscClientTertiaryPort_Type()
)
usdSscClientTertiaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSscClientTertiaryPort.setStatus("current")
_UsdSscClientLocalAddress_Type = IpAddress
_UsdSscClientLocalAddress_Object = MibScalar
usdSscClientLocalAddress = _UsdSscClientLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 8),
    _UsdSscClientLocalAddress_Type()
)
usdSscClientLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSscClientLocalAddress.setStatus("current")
_UsdSscClientTransportRouterName_Type = UsdName
_UsdSscClientTransportRouterName_Object = MibScalar
usdSscClientTransportRouterName = _UsdSscClientTransportRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 9),
    _UsdSscClientTransportRouterName_Type()
)
usdSscClientTransportRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSscClientTransportRouterName.setStatus("current")
_UsdSscClientStatus_ObjectIdentity = ObjectIdentity
usdSscClientStatus = _UsdSscClientStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2)
)
_UsdSscClientStatusScalars_ObjectIdentity = ObjectIdentity
usdSscClientStatusScalars = _UsdSscClientStatusScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2, 1)
)


class _UsdSscClientConnectionState_Type(Integer32):
    """Custom type usdSscClientConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 0),
          ("trying", 1))
    )


_UsdSscClientConnectionState_Type.__name__ = "Integer32"
_UsdSscClientConnectionState_Object = MibScalar
usdSscClientConnectionState = _UsdSscClientConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2, 1, 1),
    _UsdSscClientConnectionState_Type()
)
usdSscClientConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientConnectionState.setStatus("current")
_UsdSscClientActiveAddress_Type = IpAddress
_UsdSscClientActiveAddress_Object = MibScalar
usdSscClientActiveAddress = _UsdSscClientActiveAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2, 1, 2),
    _UsdSscClientActiveAddress_Type()
)
usdSscClientActiveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientActiveAddress.setStatus("current")


class _UsdSscClientActivePort_Type(Integer32):
    """Custom type usdSscClientActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdSscClientActivePort_Type.__name__ = "Integer32"
_UsdSscClientActivePort_Object = MibScalar
usdSscClientActivePort = _UsdSscClientActivePort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2, 1, 3),
    _UsdSscClientActivePort_Type()
)
usdSscClientActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientActivePort.setStatus("current")


class _UsdSscClientVersion_Type(DisplayString):
    """Custom type usdSscClientVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UsdSscClientVersion_Type.__name__ = "DisplayString"
_UsdSscClientVersion_Object = MibScalar
usdSscClientVersion = _UsdSscClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2, 1, 4),
    _UsdSscClientVersion_Type()
)
usdSscClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientVersion.setStatus("current")
_UsdSscClientStatistics_ObjectIdentity = ObjectIdentity
usdSscClientStatistics = _UsdSscClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3)
)
_UsdSscClientStatisticsScalars_ObjectIdentity = ObjectIdentity
usdSscClientStatisticsScalars = _UsdSscClientStatisticsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1)
)
_UsdSscClientPolicyCommandsReceived_Type = Counter32
_UsdSscClientPolicyCommandsReceived_Object = MibScalar
usdSscClientPolicyCommandsReceived = _UsdSscClientPolicyCommandsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 1),
    _UsdSscClientPolicyCommandsReceived_Type()
)
usdSscClientPolicyCommandsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientPolicyCommandsReceived.setStatus("current")
_UsdSscClientPolicyCommandsListReceived_Type = Counter32
_UsdSscClientPolicyCommandsListReceived_Object = MibScalar
usdSscClientPolicyCommandsListReceived = _UsdSscClientPolicyCommandsListReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 2),
    _UsdSscClientPolicyCommandsListReceived_Type()
)
usdSscClientPolicyCommandsListReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientPolicyCommandsListReceived.setStatus("current")
_UsdSscClientPolicyCommandsAcctReceived_Type = Counter32
_UsdSscClientPolicyCommandsAcctReceived_Object = MibScalar
usdSscClientPolicyCommandsAcctReceived = _UsdSscClientPolicyCommandsAcctReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 3),
    _UsdSscClientPolicyCommandsAcctReceived_Type()
)
usdSscClientPolicyCommandsAcctReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientPolicyCommandsAcctReceived.setStatus("current")
_UsdSscClientBadPolicyCommandsReceived_Type = Counter32
_UsdSscClientBadPolicyCommandsReceived_Object = MibScalar
usdSscClientBadPolicyCommandsReceived = _UsdSscClientBadPolicyCommandsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 4),
    _UsdSscClientBadPolicyCommandsReceived_Type()
)
usdSscClientBadPolicyCommandsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientBadPolicyCommandsReceived.setStatus("current")
_UsdSscClientErrorPolicyCommandsReceived_Type = Counter32
_UsdSscClientErrorPolicyCommandsReceived_Object = MibScalar
usdSscClientErrorPolicyCommandsReceived = _UsdSscClientErrorPolicyCommandsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 5),
    _UsdSscClientErrorPolicyCommandsReceived_Type()
)
usdSscClientErrorPolicyCommandsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientErrorPolicyCommandsReceived.setStatus("current")
_UsdSscClientPolicyReportsSent_Type = Counter32
_UsdSscClientPolicyReportsSent_Object = MibScalar
usdSscClientPolicyReportsSent = _UsdSscClientPolicyReportsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 6),
    _UsdSscClientPolicyReportsSent_Type()
)
usdSscClientPolicyReportsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientPolicyReportsSent.setStatus("current")
_UsdSscClientConnectionOpenRequests_Type = Counter32
_UsdSscClientConnectionOpenRequests_Object = MibScalar
usdSscClientConnectionOpenRequests = _UsdSscClientConnectionOpenRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 7),
    _UsdSscClientConnectionOpenRequests_Type()
)
usdSscClientConnectionOpenRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientConnectionOpenRequests.setStatus("current")
_UsdSscClientConnectionOpenCompletes_Type = Counter32
_UsdSscClientConnectionOpenCompletes_Object = MibScalar
usdSscClientConnectionOpenCompletes = _UsdSscClientConnectionOpenCompletes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 8),
    _UsdSscClientConnectionOpenCompletes_Type()
)
usdSscClientConnectionOpenCompletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientConnectionOpenCompletes.setStatus("current")
_UsdSscClientConnectionClosedSent_Type = Counter32
_UsdSscClientConnectionClosedSent_Object = MibScalar
usdSscClientConnectionClosedSent = _UsdSscClientConnectionClosedSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 9),
    _UsdSscClientConnectionClosedSent_Type()
)
usdSscClientConnectionClosedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientConnectionClosedSent.setStatus("current")
_UsdSscClientConnectionClosedRemotely_Type = Counter32
_UsdSscClientConnectionClosedRemotely_Object = MibScalar
usdSscClientConnectionClosedRemotely = _UsdSscClientConnectionClosedRemotely_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 10),
    _UsdSscClientConnectionClosedRemotely_Type()
)
usdSscClientConnectionClosedRemotely.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientConnectionClosedRemotely.setStatus("current")
_UsdSscClientCreateInterfacesSent_Type = Counter32
_UsdSscClientCreateInterfacesSent_Object = MibScalar
usdSscClientCreateInterfacesSent = _UsdSscClientCreateInterfacesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 11),
    _UsdSscClientCreateInterfacesSent_Type()
)
usdSscClientCreateInterfacesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientCreateInterfacesSent.setStatus("current")
_UsdSscClientDeleteInterfacesSent_Type = Counter32
_UsdSscClientDeleteInterfacesSent_Object = MibScalar
usdSscClientDeleteInterfacesSent = _UsdSscClientDeleteInterfacesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 12),
    _UsdSscClientDeleteInterfacesSent_Type()
)
usdSscClientDeleteInterfacesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientDeleteInterfacesSent.setStatus("current")
_UsdSscClientActiveIpInterfaces_Type = Counter32
_UsdSscClientActiveIpInterfaces_Object = MibScalar
usdSscClientActiveIpInterfaces = _UsdSscClientActiveIpInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 13),
    _UsdSscClientActiveIpInterfaces_Type()
)
usdSscClientActiveIpInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientActiveIpInterfaces.setStatus("current")
_UsdSscClientIpInterfaceTransitions_Type = Counter32
_UsdSscClientIpInterfaceTransitions_Object = MibScalar
usdSscClientIpInterfaceTransitions = _UsdSscClientIpInterfaceTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 14),
    _UsdSscClientIpInterfaceTransitions_Type()
)
usdSscClientIpInterfaceTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientIpInterfaceTransitions.setStatus("current")
_UsdSscClientSynchronizesReceived_Type = Counter32
_UsdSscClientSynchronizesReceived_Object = MibScalar
usdSscClientSynchronizesReceived = _UsdSscClientSynchronizesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 15),
    _UsdSscClientSynchronizesReceived_Type()
)
usdSscClientSynchronizesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientSynchronizesReceived.setStatus("current")
_UsdSscClientSynchronizeCompletesSent_Type = Counter32
_UsdSscClientSynchronizeCompletesSent_Object = MibScalar
usdSscClientSynchronizeCompletesSent = _UsdSscClientSynchronizeCompletesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 16),
    _UsdSscClientSynchronizeCompletesSent_Type()
)
usdSscClientSynchronizeCompletesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientSynchronizeCompletesSent.setStatus("current")
_UsdSscClientInternalErrors_Type = Counter32
_UsdSscClientInternalErrors_Object = MibScalar
usdSscClientInternalErrors = _UsdSscClientInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 17),
    _UsdSscClientInternalErrors_Type()
)
usdSscClientInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientInternalErrors.setStatus("current")
_UsdSscClientCommunicationErrors_Type = Counter32
_UsdSscClientCommunicationErrors_Object = MibScalar
usdSscClientCommunicationErrors = _UsdSscClientCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 18),
    _UsdSscClientCommunicationErrors_Type()
)
usdSscClientCommunicationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientCommunicationErrors.setStatus("current")
_UsdSscClientTokensSeen_Type = Counter32
_UsdSscClientTokensSeen_Object = MibScalar
usdSscClientTokensSeen = _UsdSscClientTokensSeen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 19),
    _UsdSscClientTokensSeen_Type()
)
usdSscClientTokensSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientTokensSeen.setStatus("current")
_UsdSscClientActiveTokens_Type = Counter32
_UsdSscClientActiveTokens_Object = MibScalar
usdSscClientActiveTokens = _UsdSscClientActiveTokens_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 20),
    _UsdSscClientActiveTokens_Type()
)
usdSscClientActiveTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientActiveTokens.setStatus("current")
_UsdSscClientTokenTransitions_Type = Counter32
_UsdSscClientTokenTransitions_Object = MibScalar
usdSscClientTokenTransitions = _UsdSscClientTokenTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 21),
    _UsdSscClientTokenTransitions_Type()
)
usdSscClientTokenTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientTokenTransitions.setStatus("current")
_UsdSscClientCreateTokensSent_Type = Counter32
_UsdSscClientCreateTokensSent_Object = MibScalar
usdSscClientCreateTokensSent = _UsdSscClientCreateTokensSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 22),
    _UsdSscClientCreateTokensSent_Type()
)
usdSscClientCreateTokensSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientCreateTokensSent.setStatus("current")
_UsdSscClientDeleteTokensSent_Type = Counter32
_UsdSscClientDeleteTokensSent_Object = MibScalar
usdSscClientDeleteTokensSent = _UsdSscClientDeleteTokensSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 23),
    _UsdSscClientDeleteTokensSent_Type()
)
usdSscClientDeleteTokensSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientDeleteTokensSent.setStatus("current")
_UsdSscClientActiveAddresses_Type = Counter32
_UsdSscClientActiveAddresses_Object = MibScalar
usdSscClientActiveAddresses = _UsdSscClientActiveAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 24),
    _UsdSscClientActiveAddresses_Type()
)
usdSscClientActiveAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientActiveAddresses.setStatus("current")
_UsdSscClientAddressTransitions_Type = Counter32
_UsdSscClientAddressTransitions_Object = MibScalar
usdSscClientAddressTransitions = _UsdSscClientAddressTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 25),
    _UsdSscClientAddressTransitions_Type()
)
usdSscClientAddressTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientAddressTransitions.setStatus("current")
_UsdSscClientCreateAddressesSent_Type = Counter32
_UsdSscClientCreateAddressesSent_Object = MibScalar
usdSscClientCreateAddressesSent = _UsdSscClientCreateAddressesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 26),
    _UsdSscClientCreateAddressesSent_Type()
)
usdSscClientCreateAddressesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientCreateAddressesSent.setStatus("current")
_UsdSscClientDeleteAddressesSent_Type = Counter32
_UsdSscClientDeleteAddressesSent_Object = MibScalar
usdSscClientDeleteAddressesSent = _UsdSscClientDeleteAddressesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 27),
    _UsdSscClientDeleteAddressesSent_Type()
)
usdSscClientDeleteAddressesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientDeleteAddressesSent.setStatus("current")
_UsdSscClientAuthenticationSuccesses_Type = Counter32
_UsdSscClientAuthenticationSuccesses_Object = MibScalar
usdSscClientAuthenticationSuccesses = _UsdSscClientAuthenticationSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 28),
    _UsdSscClientAuthenticationSuccesses_Type()
)
usdSscClientAuthenticationSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientAuthenticationSuccesses.setStatus("current")
_UsdSscClientAuthenticationFailures_Type = Counter32
_UsdSscClientAuthenticationFailures_Object = MibScalar
usdSscClientAuthenticationFailures = _UsdSscClientAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 29),
    _UsdSscClientAuthenticationFailures_Type()
)
usdSscClientAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSscClientAuthenticationFailures.setStatus("current")
_UsdSscClientMIBConformance_ObjectIdentity = ObjectIdentity
usdSscClientMIBConformance = _UsdSscClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4)
)
_UsdSscClientMIBCompliances_ObjectIdentity = ObjectIdentity
usdSscClientMIBCompliances = _UsdSscClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 1)
)
_UsdSscClientMIBGroups_ObjectIdentity = ObjectIdentity
usdSscClientMIBGroups = _UsdSscClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 2)
)

# Managed Objects groups

usdSscClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 2, 1)
)
usdSscClientGroup.setObjects(
      *(("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientServerSwitchoverTimeout"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPrimaryAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPrimaryPort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSecondaryAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSecondaryPort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientTertiaryAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientTertiaryPort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActiveAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionState"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActivePort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyCommandsReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyCommandsListReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyCommandsAcctReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientBadPolicyCommandsReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientErrorPolicyCommandsReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyReportsSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionOpenRequests"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionOpenCompletes"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionClosedSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionClosedRemotely"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientCreateInterfacesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientDeleteInterfacesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActiveIpInterfaces"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientIpInterfaceTransitions"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSynchronizesReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSynchronizeCompletesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientInternalErrors"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientCommunicationErrors"))
)
if mibBuilder.loadTexts:
    usdSscClientGroup.setStatus("obsolete")

usdSscClientGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 2, 2)
)
usdSscClientGroup2.setObjects(
      *(("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientServerSwitchoverTimeout"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPrimaryAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPrimaryPort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSecondaryAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSecondaryPort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientTertiaryAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientTertiaryPort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActiveAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionState"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActivePort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyCommandsReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyCommandsListReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyCommandsAcctReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientBadPolicyCommandsReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientErrorPolicyCommandsReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyReportsSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionOpenRequests"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionOpenCompletes"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionClosedSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionClosedRemotely"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientCreateInterfacesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientDeleteInterfacesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActiveIpInterfaces"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientIpInterfaceTransitions"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSynchronizesReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSynchronizeCompletesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientInternalErrors"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientCommunicationErrors"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientTokensSeen"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActiveTokens"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientTokenTransitions"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientCreateTokensSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientDeleteTokensSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActiveAddresses"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientAddressTransitions"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientCreateAddressesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientDeleteAddressesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientAuthenticationSuccesses"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientAuthenticationFailures"))
)
if mibBuilder.loadTexts:
    usdSscClientGroup2.setStatus("obsolete")

usdSscClientGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 2, 3)
)
usdSscClientGroup3.setObjects(
      *(("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientServerSwitchoverTimeout"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPrimaryAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPrimaryPort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSecondaryAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSecondaryPort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientTertiaryAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientTertiaryPort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientLocalAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientTransportRouterName"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActiveAddress"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionState"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActivePort"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientVersion"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyCommandsReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyCommandsListReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyCommandsAcctReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientBadPolicyCommandsReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientErrorPolicyCommandsReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientPolicyReportsSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionOpenRequests"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionOpenCompletes"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionClosedSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientConnectionClosedRemotely"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientCreateInterfacesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientDeleteInterfacesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActiveIpInterfaces"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientIpInterfaceTransitions"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSynchronizesReceived"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientSynchronizeCompletesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientInternalErrors"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientCommunicationErrors"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientTokensSeen"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActiveTokens"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientTokenTransitions"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientCreateTokensSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientDeleteTokensSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientActiveAddresses"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientAddressTransitions"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientCreateAddressesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientDeleteAddressesSent"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientAuthenticationSuccesses"),
        ("Unisphere-Data-SSC-CLIENT-MIB", "usdSscClientAuthenticationFailures"))
)
if mibBuilder.loadTexts:
    usdSscClientGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdSscClientAuthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdSscClientAuthCompliance.setStatus(
        "obsolete"
    )

usdSscClientAuthCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdSscClientAuthCompliance2.setStatus(
        "obsolete"
    )

usdSscClientAuthCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdSscClientAuthCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-SSC-CLIENT-MIB",
    **{"usdSscClientMIB": usdSscClientMIB,
       "usdSscClientObjects": usdSscClientObjects,
       "usdSscClientCfg": usdSscClientCfg,
       "usdSscClientCfgScalars": usdSscClientCfgScalars,
       "usdSscClientServerSwitchoverTimeout": usdSscClientServerSwitchoverTimeout,
       "usdSscClientPrimaryAddress": usdSscClientPrimaryAddress,
       "usdSscClientPrimaryPort": usdSscClientPrimaryPort,
       "usdSscClientSecondaryAddress": usdSscClientSecondaryAddress,
       "usdSscClientSecondaryPort": usdSscClientSecondaryPort,
       "usdSscClientTertiaryAddress": usdSscClientTertiaryAddress,
       "usdSscClientTertiaryPort": usdSscClientTertiaryPort,
       "usdSscClientLocalAddress": usdSscClientLocalAddress,
       "usdSscClientTransportRouterName": usdSscClientTransportRouterName,
       "usdSscClientStatus": usdSscClientStatus,
       "usdSscClientStatusScalars": usdSscClientStatusScalars,
       "usdSscClientConnectionState": usdSscClientConnectionState,
       "usdSscClientActiveAddress": usdSscClientActiveAddress,
       "usdSscClientActivePort": usdSscClientActivePort,
       "usdSscClientVersion": usdSscClientVersion,
       "usdSscClientStatistics": usdSscClientStatistics,
       "usdSscClientStatisticsScalars": usdSscClientStatisticsScalars,
       "usdSscClientPolicyCommandsReceived": usdSscClientPolicyCommandsReceived,
       "usdSscClientPolicyCommandsListReceived": usdSscClientPolicyCommandsListReceived,
       "usdSscClientPolicyCommandsAcctReceived": usdSscClientPolicyCommandsAcctReceived,
       "usdSscClientBadPolicyCommandsReceived": usdSscClientBadPolicyCommandsReceived,
       "usdSscClientErrorPolicyCommandsReceived": usdSscClientErrorPolicyCommandsReceived,
       "usdSscClientPolicyReportsSent": usdSscClientPolicyReportsSent,
       "usdSscClientConnectionOpenRequests": usdSscClientConnectionOpenRequests,
       "usdSscClientConnectionOpenCompletes": usdSscClientConnectionOpenCompletes,
       "usdSscClientConnectionClosedSent": usdSscClientConnectionClosedSent,
       "usdSscClientConnectionClosedRemotely": usdSscClientConnectionClosedRemotely,
       "usdSscClientCreateInterfacesSent": usdSscClientCreateInterfacesSent,
       "usdSscClientDeleteInterfacesSent": usdSscClientDeleteInterfacesSent,
       "usdSscClientActiveIpInterfaces": usdSscClientActiveIpInterfaces,
       "usdSscClientIpInterfaceTransitions": usdSscClientIpInterfaceTransitions,
       "usdSscClientSynchronizesReceived": usdSscClientSynchronizesReceived,
       "usdSscClientSynchronizeCompletesSent": usdSscClientSynchronizeCompletesSent,
       "usdSscClientInternalErrors": usdSscClientInternalErrors,
       "usdSscClientCommunicationErrors": usdSscClientCommunicationErrors,
       "usdSscClientTokensSeen": usdSscClientTokensSeen,
       "usdSscClientActiveTokens": usdSscClientActiveTokens,
       "usdSscClientTokenTransitions": usdSscClientTokenTransitions,
       "usdSscClientCreateTokensSent": usdSscClientCreateTokensSent,
       "usdSscClientDeleteTokensSent": usdSscClientDeleteTokensSent,
       "usdSscClientActiveAddresses": usdSscClientActiveAddresses,
       "usdSscClientAddressTransitions": usdSscClientAddressTransitions,
       "usdSscClientCreateAddressesSent": usdSscClientCreateAddressesSent,
       "usdSscClientDeleteAddressesSent": usdSscClientDeleteAddressesSent,
       "usdSscClientAuthenticationSuccesses": usdSscClientAuthenticationSuccesses,
       "usdSscClientAuthenticationFailures": usdSscClientAuthenticationFailures,
       "usdSscClientMIBConformance": usdSscClientMIBConformance,
       "usdSscClientMIBCompliances": usdSscClientMIBCompliances,
       "usdSscClientAuthCompliance": usdSscClientAuthCompliance,
       "usdSscClientAuthCompliance2": usdSscClientAuthCompliance2,
       "usdSscClientAuthCompliance3": usdSscClientAuthCompliance3,
       "usdSscClientMIBGroups": usdSscClientMIBGroups,
       "usdSscClientGroup": usdSscClientGroup,
       "usdSscClientGroup2": usdSscClientGroup2,
       "usdSscClientGroup3": usdSscClientGroup3}
)

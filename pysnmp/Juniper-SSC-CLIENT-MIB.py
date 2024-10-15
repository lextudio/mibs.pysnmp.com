# SNMP MIB module (Juniper-SSC-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-SSC-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:22 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniName,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniName")

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


# MODULE-IDENTITY

juniSscClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36)
)
juniSscClientMIB.setRevisions(
        ("2003-12-18 16:29",
         "2002-09-16 21:44",
         "2002-01-14 20:15",
         "2001-01-23 21:30",
         "2000-02-17 23:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniSscClientObjects_ObjectIdentity = ObjectIdentity
juniSscClientObjects = _JuniSscClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1)
)
_JuniSscClientCfg_ObjectIdentity = ObjectIdentity
juniSscClientCfg = _JuniSscClientCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1)
)
_JuniSscClientCfgScalars_ObjectIdentity = ObjectIdentity
juniSscClientCfgScalars = _JuniSscClientCfgScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1)
)


class _JuniSscClientServerSwitchoverTimeout_Type(Integer32):
    """Custom type juniSscClientServerSwitchoverTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_JuniSscClientServerSwitchoverTimeout_Type.__name__ = "Integer32"
_JuniSscClientServerSwitchoverTimeout_Object = MibScalar
juniSscClientServerSwitchoverTimeout = _JuniSscClientServerSwitchoverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 1),
    _JuniSscClientServerSwitchoverTimeout_Type()
)
juniSscClientServerSwitchoverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSscClientServerSwitchoverTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniSscClientServerSwitchoverTimeout.setUnits("seconds")
_JuniSscClientPrimaryAddress_Type = IpAddress
_JuniSscClientPrimaryAddress_Object = MibScalar
juniSscClientPrimaryAddress = _JuniSscClientPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 2),
    _JuniSscClientPrimaryAddress_Type()
)
juniSscClientPrimaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSscClientPrimaryAddress.setStatus("current")


class _JuniSscClientPrimaryPort_Type(Integer32):
    """Custom type juniSscClientPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniSscClientPrimaryPort_Type.__name__ = "Integer32"
_JuniSscClientPrimaryPort_Object = MibScalar
juniSscClientPrimaryPort = _JuniSscClientPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 3),
    _JuniSscClientPrimaryPort_Type()
)
juniSscClientPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSscClientPrimaryPort.setStatus("current")
_JuniSscClientSecondaryAddress_Type = IpAddress
_JuniSscClientSecondaryAddress_Object = MibScalar
juniSscClientSecondaryAddress = _JuniSscClientSecondaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 4),
    _JuniSscClientSecondaryAddress_Type()
)
juniSscClientSecondaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSscClientSecondaryAddress.setStatus("current")


class _JuniSscClientSecondaryPort_Type(Integer32):
    """Custom type juniSscClientSecondaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniSscClientSecondaryPort_Type.__name__ = "Integer32"
_JuniSscClientSecondaryPort_Object = MibScalar
juniSscClientSecondaryPort = _JuniSscClientSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 5),
    _JuniSscClientSecondaryPort_Type()
)
juniSscClientSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSscClientSecondaryPort.setStatus("current")
_JuniSscClientTertiaryAddress_Type = IpAddress
_JuniSscClientTertiaryAddress_Object = MibScalar
juniSscClientTertiaryAddress = _JuniSscClientTertiaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 6),
    _JuniSscClientTertiaryAddress_Type()
)
juniSscClientTertiaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSscClientTertiaryAddress.setStatus("current")


class _JuniSscClientTertiaryPort_Type(Integer32):
    """Custom type juniSscClientTertiaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniSscClientTertiaryPort_Type.__name__ = "Integer32"
_JuniSscClientTertiaryPort_Object = MibScalar
juniSscClientTertiaryPort = _JuniSscClientTertiaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 7),
    _JuniSscClientTertiaryPort_Type()
)
juniSscClientTertiaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSscClientTertiaryPort.setStatus("current")
_JuniSscClientLocalAddress_Type = IpAddress
_JuniSscClientLocalAddress_Object = MibScalar
juniSscClientLocalAddress = _JuniSscClientLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 8),
    _JuniSscClientLocalAddress_Type()
)
juniSscClientLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSscClientLocalAddress.setStatus("current")
_JuniSscClientTransportRouterName_Type = JuniName
_JuniSscClientTransportRouterName_Object = MibScalar
juniSscClientTransportRouterName = _JuniSscClientTransportRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 1, 1, 9),
    _JuniSscClientTransportRouterName_Type()
)
juniSscClientTransportRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSscClientTransportRouterName.setStatus("current")
_JuniSscClientStatus_ObjectIdentity = ObjectIdentity
juniSscClientStatus = _JuniSscClientStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2)
)
_JuniSscClientStatusScalars_ObjectIdentity = ObjectIdentity
juniSscClientStatusScalars = _JuniSscClientStatusScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2, 1)
)


class _JuniSscClientConnectionState_Type(Integer32):
    """Custom type juniSscClientConnectionState based on Integer32"""
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


_JuniSscClientConnectionState_Type.__name__ = "Integer32"
_JuniSscClientConnectionState_Object = MibScalar
juniSscClientConnectionState = _JuniSscClientConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2, 1, 1),
    _JuniSscClientConnectionState_Type()
)
juniSscClientConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientConnectionState.setStatus("current")
_JuniSscClientActiveAddress_Type = IpAddress
_JuniSscClientActiveAddress_Object = MibScalar
juniSscClientActiveAddress = _JuniSscClientActiveAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2, 1, 2),
    _JuniSscClientActiveAddress_Type()
)
juniSscClientActiveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientActiveAddress.setStatus("current")


class _JuniSscClientActivePort_Type(Integer32):
    """Custom type juniSscClientActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniSscClientActivePort_Type.__name__ = "Integer32"
_JuniSscClientActivePort_Object = MibScalar
juniSscClientActivePort = _JuniSscClientActivePort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2, 1, 3),
    _JuniSscClientActivePort_Type()
)
juniSscClientActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientActivePort.setStatus("current")


class _JuniSscClientVersion_Type(DisplayString):
    """Custom type juniSscClientVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JuniSscClientVersion_Type.__name__ = "DisplayString"
_JuniSscClientVersion_Object = MibScalar
juniSscClientVersion = _JuniSscClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 2, 1, 4),
    _JuniSscClientVersion_Type()
)
juniSscClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientVersion.setStatus("current")
_JuniSscClientStatistics_ObjectIdentity = ObjectIdentity
juniSscClientStatistics = _JuniSscClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3)
)
_JuniSscClientStatisticsScalars_ObjectIdentity = ObjectIdentity
juniSscClientStatisticsScalars = _JuniSscClientStatisticsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1)
)
_JuniSscClientPolicyCommandsReceived_Type = Counter32
_JuniSscClientPolicyCommandsReceived_Object = MibScalar
juniSscClientPolicyCommandsReceived = _JuniSscClientPolicyCommandsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 1),
    _JuniSscClientPolicyCommandsReceived_Type()
)
juniSscClientPolicyCommandsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientPolicyCommandsReceived.setStatus("current")
_JuniSscClientPolicyCommandsListReceived_Type = Counter32
_JuniSscClientPolicyCommandsListReceived_Object = MibScalar
juniSscClientPolicyCommandsListReceived = _JuniSscClientPolicyCommandsListReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 2),
    _JuniSscClientPolicyCommandsListReceived_Type()
)
juniSscClientPolicyCommandsListReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientPolicyCommandsListReceived.setStatus("current")
_JuniSscClientPolicyCommandsAcctReceived_Type = Counter32
_JuniSscClientPolicyCommandsAcctReceived_Object = MibScalar
juniSscClientPolicyCommandsAcctReceived = _JuniSscClientPolicyCommandsAcctReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 3),
    _JuniSscClientPolicyCommandsAcctReceived_Type()
)
juniSscClientPolicyCommandsAcctReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientPolicyCommandsAcctReceived.setStatus("current")
_JuniSscClientBadPolicyCommandsReceived_Type = Counter32
_JuniSscClientBadPolicyCommandsReceived_Object = MibScalar
juniSscClientBadPolicyCommandsReceived = _JuniSscClientBadPolicyCommandsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 4),
    _JuniSscClientBadPolicyCommandsReceived_Type()
)
juniSscClientBadPolicyCommandsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientBadPolicyCommandsReceived.setStatus("current")
_JuniSscClientErrorPolicyCommandsReceived_Type = Counter32
_JuniSscClientErrorPolicyCommandsReceived_Object = MibScalar
juniSscClientErrorPolicyCommandsReceived = _JuniSscClientErrorPolicyCommandsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 5),
    _JuniSscClientErrorPolicyCommandsReceived_Type()
)
juniSscClientErrorPolicyCommandsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientErrorPolicyCommandsReceived.setStatus("current")
_JuniSscClientPolicyReportsSent_Type = Counter32
_JuniSscClientPolicyReportsSent_Object = MibScalar
juniSscClientPolicyReportsSent = _JuniSscClientPolicyReportsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 6),
    _JuniSscClientPolicyReportsSent_Type()
)
juniSscClientPolicyReportsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientPolicyReportsSent.setStatus("current")
_JuniSscClientConnectionOpenRequests_Type = Counter32
_JuniSscClientConnectionOpenRequests_Object = MibScalar
juniSscClientConnectionOpenRequests = _JuniSscClientConnectionOpenRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 7),
    _JuniSscClientConnectionOpenRequests_Type()
)
juniSscClientConnectionOpenRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientConnectionOpenRequests.setStatus("current")
_JuniSscClientConnectionOpenCompletes_Type = Counter32
_JuniSscClientConnectionOpenCompletes_Object = MibScalar
juniSscClientConnectionOpenCompletes = _JuniSscClientConnectionOpenCompletes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 8),
    _JuniSscClientConnectionOpenCompletes_Type()
)
juniSscClientConnectionOpenCompletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientConnectionOpenCompletes.setStatus("current")
_JuniSscClientConnectionClosedSent_Type = Counter32
_JuniSscClientConnectionClosedSent_Object = MibScalar
juniSscClientConnectionClosedSent = _JuniSscClientConnectionClosedSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 9),
    _JuniSscClientConnectionClosedSent_Type()
)
juniSscClientConnectionClosedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientConnectionClosedSent.setStatus("current")
_JuniSscClientConnectionClosedRemotely_Type = Counter32
_JuniSscClientConnectionClosedRemotely_Object = MibScalar
juniSscClientConnectionClosedRemotely = _JuniSscClientConnectionClosedRemotely_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 10),
    _JuniSscClientConnectionClosedRemotely_Type()
)
juniSscClientConnectionClosedRemotely.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientConnectionClosedRemotely.setStatus("current")
_JuniSscClientCreateInterfacesSent_Type = Counter32
_JuniSscClientCreateInterfacesSent_Object = MibScalar
juniSscClientCreateInterfacesSent = _JuniSscClientCreateInterfacesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 11),
    _JuniSscClientCreateInterfacesSent_Type()
)
juniSscClientCreateInterfacesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientCreateInterfacesSent.setStatus("current")
_JuniSscClientDeleteInterfacesSent_Type = Counter32
_JuniSscClientDeleteInterfacesSent_Object = MibScalar
juniSscClientDeleteInterfacesSent = _JuniSscClientDeleteInterfacesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 12),
    _JuniSscClientDeleteInterfacesSent_Type()
)
juniSscClientDeleteInterfacesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientDeleteInterfacesSent.setStatus("current")
_JuniSscClientActiveIpInterfaces_Type = Counter32
_JuniSscClientActiveIpInterfaces_Object = MibScalar
juniSscClientActiveIpInterfaces = _JuniSscClientActiveIpInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 13),
    _JuniSscClientActiveIpInterfaces_Type()
)
juniSscClientActiveIpInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientActiveIpInterfaces.setStatus("current")
_JuniSscClientIpInterfaceTransitions_Type = Counter32
_JuniSscClientIpInterfaceTransitions_Object = MibScalar
juniSscClientIpInterfaceTransitions = _JuniSscClientIpInterfaceTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 14),
    _JuniSscClientIpInterfaceTransitions_Type()
)
juniSscClientIpInterfaceTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientIpInterfaceTransitions.setStatus("current")
_JuniSscClientSynchronizesReceived_Type = Counter32
_JuniSscClientSynchronizesReceived_Object = MibScalar
juniSscClientSynchronizesReceived = _JuniSscClientSynchronizesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 15),
    _JuniSscClientSynchronizesReceived_Type()
)
juniSscClientSynchronizesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientSynchronizesReceived.setStatus("current")
_JuniSscClientSynchronizeCompletesSent_Type = Counter32
_JuniSscClientSynchronizeCompletesSent_Object = MibScalar
juniSscClientSynchronizeCompletesSent = _JuniSscClientSynchronizeCompletesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 16),
    _JuniSscClientSynchronizeCompletesSent_Type()
)
juniSscClientSynchronizeCompletesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientSynchronizeCompletesSent.setStatus("current")
_JuniSscClientInternalErrors_Type = Counter32
_JuniSscClientInternalErrors_Object = MibScalar
juniSscClientInternalErrors = _JuniSscClientInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 17),
    _JuniSscClientInternalErrors_Type()
)
juniSscClientInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientInternalErrors.setStatus("current")
_JuniSscClientCommunicationErrors_Type = Counter32
_JuniSscClientCommunicationErrors_Object = MibScalar
juniSscClientCommunicationErrors = _JuniSscClientCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 18),
    _JuniSscClientCommunicationErrors_Type()
)
juniSscClientCommunicationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientCommunicationErrors.setStatus("current")
_JuniSscClientTokensSeen_Type = Counter32
_JuniSscClientTokensSeen_Object = MibScalar
juniSscClientTokensSeen = _JuniSscClientTokensSeen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 19),
    _JuniSscClientTokensSeen_Type()
)
juniSscClientTokensSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientTokensSeen.setStatus("obsolete")
_JuniSscClientActiveTokens_Type = Counter32
_JuniSscClientActiveTokens_Object = MibScalar
juniSscClientActiveTokens = _JuniSscClientActiveTokens_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 20),
    _JuniSscClientActiveTokens_Type()
)
juniSscClientActiveTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientActiveTokens.setStatus("obsolete")
_JuniSscClientTokenTransitions_Type = Counter32
_JuniSscClientTokenTransitions_Object = MibScalar
juniSscClientTokenTransitions = _JuniSscClientTokenTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 21),
    _JuniSscClientTokenTransitions_Type()
)
juniSscClientTokenTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientTokenTransitions.setStatus("obsolete")
_JuniSscClientCreateTokensSent_Type = Counter32
_JuniSscClientCreateTokensSent_Object = MibScalar
juniSscClientCreateTokensSent = _JuniSscClientCreateTokensSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 22),
    _JuniSscClientCreateTokensSent_Type()
)
juniSscClientCreateTokensSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientCreateTokensSent.setStatus("obsolete")
_JuniSscClientDeleteTokensSent_Type = Counter32
_JuniSscClientDeleteTokensSent_Object = MibScalar
juniSscClientDeleteTokensSent = _JuniSscClientDeleteTokensSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 23),
    _JuniSscClientDeleteTokensSent_Type()
)
juniSscClientDeleteTokensSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientDeleteTokensSent.setStatus("obsolete")
_JuniSscClientActiveAddresses_Type = Counter32
_JuniSscClientActiveAddresses_Object = MibScalar
juniSscClientActiveAddresses = _JuniSscClientActiveAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 24),
    _JuniSscClientActiveAddresses_Type()
)
juniSscClientActiveAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientActiveAddresses.setStatus("current")
_JuniSscClientAddressTransitions_Type = Counter32
_JuniSscClientAddressTransitions_Object = MibScalar
juniSscClientAddressTransitions = _JuniSscClientAddressTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 25),
    _JuniSscClientAddressTransitions_Type()
)
juniSscClientAddressTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientAddressTransitions.setStatus("current")
_JuniSscClientCreateAddressesSent_Type = Counter32
_JuniSscClientCreateAddressesSent_Object = MibScalar
juniSscClientCreateAddressesSent = _JuniSscClientCreateAddressesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 26),
    _JuniSscClientCreateAddressesSent_Type()
)
juniSscClientCreateAddressesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientCreateAddressesSent.setStatus("current")
_JuniSscClientDeleteAddressesSent_Type = Counter32
_JuniSscClientDeleteAddressesSent_Object = MibScalar
juniSscClientDeleteAddressesSent = _JuniSscClientDeleteAddressesSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 27),
    _JuniSscClientDeleteAddressesSent_Type()
)
juniSscClientDeleteAddressesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientDeleteAddressesSent.setStatus("current")
_JuniSscClientAuthenticationSuccesses_Type = Counter32
_JuniSscClientAuthenticationSuccesses_Object = MibScalar
juniSscClientAuthenticationSuccesses = _JuniSscClientAuthenticationSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 28),
    _JuniSscClientAuthenticationSuccesses_Type()
)
juniSscClientAuthenticationSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientAuthenticationSuccesses.setStatus("obsolete")
_JuniSscClientAuthenticationFailures_Type = Counter32
_JuniSscClientAuthenticationFailures_Object = MibScalar
juniSscClientAuthenticationFailures = _JuniSscClientAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 29),
    _JuniSscClientAuthenticationFailures_Type()
)
juniSscClientAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientAuthenticationFailures.setStatus("obsolete")
_JuniSscClientDiscoversSeen_Type = Counter32
_JuniSscClientDiscoversSeen_Object = MibScalar
juniSscClientDiscoversSeen = _JuniSscClientDiscoversSeen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 30),
    _JuniSscClientDiscoversSeen_Type()
)
juniSscClientDiscoversSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientDiscoversSeen.setStatus("current")
_JuniSscClientActiveDiscovers_Type = Counter32
_JuniSscClientActiveDiscovers_Object = MibScalar
juniSscClientActiveDiscovers = _JuniSscClientActiveDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 31),
    _JuniSscClientActiveDiscovers_Type()
)
juniSscClientActiveDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientActiveDiscovers.setStatus("current")
_JuniSscClientDiscoverTransitions_Type = Counter32
_JuniSscClientDiscoverTransitions_Object = MibScalar
juniSscClientDiscoverTransitions = _JuniSscClientDiscoverTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 32),
    _JuniSscClientDiscoverTransitions_Type()
)
juniSscClientDiscoverTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientDiscoverTransitions.setStatus("current")
_JuniSscClientCreateDiscoversSent_Type = Counter32
_JuniSscClientCreateDiscoversSent_Object = MibScalar
juniSscClientCreateDiscoversSent = _JuniSscClientCreateDiscoversSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 33),
    _JuniSscClientCreateDiscoversSent_Type()
)
juniSscClientCreateDiscoversSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientCreateDiscoversSent.setStatus("current")
_JuniSscClientDeleteDiscoversSent_Type = Counter32
_JuniSscClientDeleteDiscoversSent_Object = MibScalar
juniSscClientDeleteDiscoversSent = _JuniSscClientDeleteDiscoversSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 1, 3, 1, 34),
    _JuniSscClientDeleteDiscoversSent_Type()
)
juniSscClientDeleteDiscoversSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSscClientDeleteDiscoversSent.setStatus("current")
_JuniSscClientMIBConformance_ObjectIdentity = ObjectIdentity
juniSscClientMIBConformance = _JuniSscClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4)
)
_JuniSscClientMIBCompliances_ObjectIdentity = ObjectIdentity
juniSscClientMIBCompliances = _JuniSscClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 1)
)
_JuniSscClientMIBGroups_ObjectIdentity = ObjectIdentity
juniSscClientMIBGroups = _JuniSscClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 2)
)

# Managed Objects groups

juniSscClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 2, 1)
)
juniSscClientGroup.setObjects(
      *(("Juniper-SSC-CLIENT-MIB", "juniSscClientServerSwitchoverTimeout"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPrimaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPrimaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSecondaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSecondaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTertiaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTertiaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionState"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActivePort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsListReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsAcctReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientBadPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientErrorPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyReportsSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionOpenRequests"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionOpenCompletes"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionClosedSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionClosedRemotely"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCreateInterfacesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDeleteInterfacesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveIpInterfaces"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientIpInterfaceTransitions"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSynchronizesReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSynchronizeCompletesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientInternalErrors"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCommunicationErrors"))
)
if mibBuilder.loadTexts:
    juniSscClientGroup.setStatus("obsolete")

juniSscClientGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 2, 2)
)
juniSscClientGroup2.setObjects(
      *(("Juniper-SSC-CLIENT-MIB", "juniSscClientServerSwitchoverTimeout"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPrimaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPrimaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSecondaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSecondaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTertiaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTertiaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionState"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActivePort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsListReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsAcctReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientBadPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientErrorPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyReportsSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionOpenRequests"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionOpenCompletes"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionClosedSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionClosedRemotely"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCreateInterfacesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDeleteInterfacesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveIpInterfaces"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientIpInterfaceTransitions"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSynchronizesReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSynchronizeCompletesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientInternalErrors"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCommunicationErrors"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTokensSeen"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveTokens"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTokenTransitions"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCreateTokensSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDeleteTokensSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveAddresses"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientAddressTransitions"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCreateAddressesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDeleteAddressesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientAuthenticationSuccesses"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientAuthenticationFailures"))
)
if mibBuilder.loadTexts:
    juniSscClientGroup2.setStatus("obsolete")

juniSscClientGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 2, 3)
)
juniSscClientGroup3.setObjects(
      *(("Juniper-SSC-CLIENT-MIB", "juniSscClientServerSwitchoverTimeout"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPrimaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPrimaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSecondaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSecondaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTertiaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTertiaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientLocalAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTransportRouterName"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionState"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActivePort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientVersion"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsListReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsAcctReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientBadPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientErrorPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyReportsSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionOpenRequests"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionOpenCompletes"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionClosedSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionClosedRemotely"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCreateInterfacesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDeleteInterfacesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveIpInterfaces"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientIpInterfaceTransitions"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSynchronizesReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSynchronizeCompletesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientInternalErrors"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCommunicationErrors"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTokensSeen"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveTokens"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTokenTransitions"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCreateTokensSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDeleteTokensSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveAddresses"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientAddressTransitions"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCreateAddressesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDeleteAddressesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientAuthenticationSuccesses"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientAuthenticationFailures"))
)
if mibBuilder.loadTexts:
    juniSscClientGroup3.setStatus("obsolete")

juniSscClientGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 2, 4)
)
juniSscClientGroup4.setObjects(
      *(("Juniper-SSC-CLIENT-MIB", "juniSscClientServerSwitchoverTimeout"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPrimaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPrimaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSecondaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSecondaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTertiaryAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTertiaryPort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientLocalAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientTransportRouterName"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveAddress"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionState"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActivePort"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientVersion"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsListReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyCommandsAcctReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientBadPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientErrorPolicyCommandsReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientPolicyReportsSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionOpenRequests"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionOpenCompletes"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionClosedSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientConnectionClosedRemotely"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCreateInterfacesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDeleteInterfacesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveIpInterfaces"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientIpInterfaceTransitions"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSynchronizesReceived"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientSynchronizeCompletesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientInternalErrors"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCommunicationErrors"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveAddresses"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientAddressTransitions"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCreateAddressesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDeleteAddressesSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDiscoversSeen"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientActiveDiscovers"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDiscoverTransitions"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientCreateDiscoversSent"),
        ("Juniper-SSC-CLIENT-MIB", "juniSscClientDeleteDiscoversSent"))
)
if mibBuilder.loadTexts:
    juniSscClientGroup4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniSscClientAuthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniSscClientAuthCompliance.setStatus(
        "obsolete"
    )

juniSscClientAuthCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniSscClientAuthCompliance2.setStatus(
        "obsolete"
    )

juniSscClientAuthCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniSscClientAuthCompliance3.setStatus(
        "obsolete"
    )

juniSscClientAuthCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniSscClientAuthCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-SSC-CLIENT-MIB",
    **{"juniSscClientMIB": juniSscClientMIB,
       "juniSscClientObjects": juniSscClientObjects,
       "juniSscClientCfg": juniSscClientCfg,
       "juniSscClientCfgScalars": juniSscClientCfgScalars,
       "juniSscClientServerSwitchoverTimeout": juniSscClientServerSwitchoverTimeout,
       "juniSscClientPrimaryAddress": juniSscClientPrimaryAddress,
       "juniSscClientPrimaryPort": juniSscClientPrimaryPort,
       "juniSscClientSecondaryAddress": juniSscClientSecondaryAddress,
       "juniSscClientSecondaryPort": juniSscClientSecondaryPort,
       "juniSscClientTertiaryAddress": juniSscClientTertiaryAddress,
       "juniSscClientTertiaryPort": juniSscClientTertiaryPort,
       "juniSscClientLocalAddress": juniSscClientLocalAddress,
       "juniSscClientTransportRouterName": juniSscClientTransportRouterName,
       "juniSscClientStatus": juniSscClientStatus,
       "juniSscClientStatusScalars": juniSscClientStatusScalars,
       "juniSscClientConnectionState": juniSscClientConnectionState,
       "juniSscClientActiveAddress": juniSscClientActiveAddress,
       "juniSscClientActivePort": juniSscClientActivePort,
       "juniSscClientVersion": juniSscClientVersion,
       "juniSscClientStatistics": juniSscClientStatistics,
       "juniSscClientStatisticsScalars": juniSscClientStatisticsScalars,
       "juniSscClientPolicyCommandsReceived": juniSscClientPolicyCommandsReceived,
       "juniSscClientPolicyCommandsListReceived": juniSscClientPolicyCommandsListReceived,
       "juniSscClientPolicyCommandsAcctReceived": juniSscClientPolicyCommandsAcctReceived,
       "juniSscClientBadPolicyCommandsReceived": juniSscClientBadPolicyCommandsReceived,
       "juniSscClientErrorPolicyCommandsReceived": juniSscClientErrorPolicyCommandsReceived,
       "juniSscClientPolicyReportsSent": juniSscClientPolicyReportsSent,
       "juniSscClientConnectionOpenRequests": juniSscClientConnectionOpenRequests,
       "juniSscClientConnectionOpenCompletes": juniSscClientConnectionOpenCompletes,
       "juniSscClientConnectionClosedSent": juniSscClientConnectionClosedSent,
       "juniSscClientConnectionClosedRemotely": juniSscClientConnectionClosedRemotely,
       "juniSscClientCreateInterfacesSent": juniSscClientCreateInterfacesSent,
       "juniSscClientDeleteInterfacesSent": juniSscClientDeleteInterfacesSent,
       "juniSscClientActiveIpInterfaces": juniSscClientActiveIpInterfaces,
       "juniSscClientIpInterfaceTransitions": juniSscClientIpInterfaceTransitions,
       "juniSscClientSynchronizesReceived": juniSscClientSynchronizesReceived,
       "juniSscClientSynchronizeCompletesSent": juniSscClientSynchronizeCompletesSent,
       "juniSscClientInternalErrors": juniSscClientInternalErrors,
       "juniSscClientCommunicationErrors": juniSscClientCommunicationErrors,
       "juniSscClientTokensSeen": juniSscClientTokensSeen,
       "juniSscClientActiveTokens": juniSscClientActiveTokens,
       "juniSscClientTokenTransitions": juniSscClientTokenTransitions,
       "juniSscClientCreateTokensSent": juniSscClientCreateTokensSent,
       "juniSscClientDeleteTokensSent": juniSscClientDeleteTokensSent,
       "juniSscClientActiveAddresses": juniSscClientActiveAddresses,
       "juniSscClientAddressTransitions": juniSscClientAddressTransitions,
       "juniSscClientCreateAddressesSent": juniSscClientCreateAddressesSent,
       "juniSscClientDeleteAddressesSent": juniSscClientDeleteAddressesSent,
       "juniSscClientAuthenticationSuccesses": juniSscClientAuthenticationSuccesses,
       "juniSscClientAuthenticationFailures": juniSscClientAuthenticationFailures,
       "juniSscClientDiscoversSeen": juniSscClientDiscoversSeen,
       "juniSscClientActiveDiscovers": juniSscClientActiveDiscovers,
       "juniSscClientDiscoverTransitions": juniSscClientDiscoverTransitions,
       "juniSscClientCreateDiscoversSent": juniSscClientCreateDiscoversSent,
       "juniSscClientDeleteDiscoversSent": juniSscClientDeleteDiscoversSent,
       "juniSscClientMIBConformance": juniSscClientMIBConformance,
       "juniSscClientMIBCompliances": juniSscClientMIBCompliances,
       "juniSscClientAuthCompliance": juniSscClientAuthCompliance,
       "juniSscClientAuthCompliance2": juniSscClientAuthCompliance2,
       "juniSscClientAuthCompliance3": juniSscClientAuthCompliance3,
       "juniSscClientAuthCompliance4": juniSscClientAuthCompliance4,
       "juniSscClientMIBGroups": juniSscClientMIBGroups,
       "juniSscClientGroup": juniSscClientGroup,
       "juniSscClientGroup2": juniSscClientGroup2,
       "juniSscClientGroup3": juniSscClientGroup3,
       "juniSscClientGroup4": juniSscClientGroup4}
)

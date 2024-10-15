# SNMP MIB module (CISCO-SSG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SSG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:46 2024
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

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoSsgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260)
)
ciscoSsgMIB.setRevisions(
        ("2005-12-22 00:00",
         "2003-10-17 00:00",
         "2002-03-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSsgMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoSsgMIBNotifications = _CiscoSsgMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 0)
)
_CiscoSsgMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSsgMIBObjects = _CiscoSsgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1)
)
_CssgCfgObjects_ObjectIdentity = ObjectIdentity
cssgCfgObjects = _CssgCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1)
)
_CssgCfgSsgEnabled_Type = TruthValue
_CssgCfgSsgEnabled_Object = MibScalar
cssgCfgSsgEnabled = _CssgCfgSsgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 1),
    _CssgCfgSsgEnabled_Type()
)
cssgCfgSsgEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgSsgEnabled.setStatus("current")


class _CssgCfgAutoDomainMode_Type(Integer32):
    """Custom type cssgCfgAutoDomainMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("basic", 2),
          ("disabled", 1),
          ("extended", 3))
    )


_CssgCfgAutoDomainMode_Type.__name__ = "Integer32"
_CssgCfgAutoDomainMode_Object = MibScalar
cssgCfgAutoDomainMode = _CssgCfgAutoDomainMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 2),
    _CssgCfgAutoDomainMode_Type()
)
cssgCfgAutoDomainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgAutoDomainMode.setStatus("current")
_CssgCfgLocalForwardingEnabled_Type = TruthValue
_CssgCfgLocalForwardingEnabled_Object = MibScalar
cssgCfgLocalForwardingEnabled = _CssgCfgLocalForwardingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 3),
    _CssgCfgLocalForwardingEnabled_Type()
)
cssgCfgLocalForwardingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgLocalForwardingEnabled.setStatus("current")


class _CssgCfgAutoLogOffMode_Type(Integer32):
    """Custom type cssgCfgAutoLogOffMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 3),
          ("disabled", 1),
          ("icmp", 2))
    )


_CssgCfgAutoLogOffMode_Type.__name__ = "Integer32"
_CssgCfgAutoLogOffMode_Object = MibScalar
cssgCfgAutoLogOffMode = _CssgCfgAutoLogOffMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 4),
    _CssgCfgAutoLogOffMode_Type()
)
cssgCfgAutoLogOffMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgAutoLogOffMode.setStatus("current")
_CssgCfgRadiusProxyEnabled_Type = TruthValue
_CssgCfgRadiusProxyEnabled_Object = MibScalar
cssgCfgRadiusProxyEnabled = _CssgCfgRadiusProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 5),
    _CssgCfgRadiusProxyEnabled_Type()
)
cssgCfgRadiusProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgRadiusProxyEnabled.setStatus("current")
_CssgCfgTcpRedirectEnabled_Type = TruthValue
_CssgCfgTcpRedirectEnabled_Object = MibScalar
cssgCfgTcpRedirectEnabled = _CssgCfgTcpRedirectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 6),
    _CssgCfgTcpRedirectEnabled_Type()
)
cssgCfgTcpRedirectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgTcpRedirectEnabled.setStatus("current")
_CssgCfgAutoDomainNatEnabled_Type = TruthValue
_CssgCfgAutoDomainNatEnabled_Object = MibScalar
cssgCfgAutoDomainNatEnabled = _CssgCfgAutoDomainNatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 7),
    _CssgCfgAutoDomainNatEnabled_Type()
)
cssgCfgAutoDomainNatEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgAutoDomainNatEnabled.setStatus("current")
_CssgCfgPortBundleHostKeyEnabled_Type = TruthValue
_CssgCfgPortBundleHostKeyEnabled_Object = MibScalar
cssgCfgPortBundleHostKeyEnabled = _CssgCfgPortBundleHostKeyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 8),
    _CssgCfgPortBundleHostKeyEnabled_Type()
)
cssgCfgPortBundleHostKeyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgPortBundleHostKeyEnabled.setStatus("current")
_CssgCfgTransPassThroughEnabled_Type = TruthValue
_CssgCfgTransPassThroughEnabled_Object = MibScalar
cssgCfgTransPassThroughEnabled = _CssgCfgTransPassThroughEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 9),
    _CssgCfgTransPassThroughEnabled_Type()
)
cssgCfgTransPassThroughEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgTransPassThroughEnabled.setStatus("current")
_CssgCfgAutoLogOffInterval_Type = TimeInterval
_CssgCfgAutoLogOffInterval_Object = MibScalar
cssgCfgAutoLogOffInterval = _CssgCfgAutoLogOffInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 10),
    _CssgCfgAutoLogOffInterval_Type()
)
cssgCfgAutoLogOffInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgAutoLogOffInterval.setStatus("current")


class _CssgCfgAutoLogOffIcmpRetries_Type(Unsigned32):
    """Custom type cssgCfgAutoLogOffIcmpRetries based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CssgCfgAutoLogOffIcmpRetries_Type.__name__ = "Unsigned32"
_CssgCfgAutoLogOffIcmpRetries_Object = MibScalar
cssgCfgAutoLogOffIcmpRetries = _CssgCfgAutoLogOffIcmpRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 11),
    _CssgCfgAutoLogOffIcmpRetries_Type()
)
cssgCfgAutoLogOffIcmpRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgAutoLogOffIcmpRetries.setStatus("current")


class _CssgCfgMaxServicesPerUser_Type(Unsigned32):
    """Custom type cssgCfgMaxServicesPerUser based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CssgCfgMaxServicesPerUser_Type.__name__ = "Unsigned32"
_CssgCfgMaxServicesPerUser_Object = MibScalar
cssgCfgMaxServicesPerUser = _CssgCfgMaxServicesPerUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 12),
    _CssgCfgMaxServicesPerUser_Type()
)
cssgCfgMaxServicesPerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgMaxServicesPerUser.setStatus("current")
_CssgCfgAccountingEnabled_Type = TruthValue
_CssgCfgAccountingEnabled_Object = MibScalar
cssgCfgAccountingEnabled = _CssgCfgAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 13),
    _CssgCfgAccountingEnabled_Type()
)
cssgCfgAccountingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgAccountingEnabled.setStatus("current")
_CssgCfgDefaultNetworkType_Type = InetAddressType
_CssgCfgDefaultNetworkType_Object = MibScalar
cssgCfgDefaultNetworkType = _CssgCfgDefaultNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 14),
    _CssgCfgDefaultNetworkType_Type()
)
cssgCfgDefaultNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgDefaultNetworkType.setStatus("current")
_CssgCfgDefaultNetwork_Type = InetAddress
_CssgCfgDefaultNetwork_Object = MibScalar
cssgCfgDefaultNetwork = _CssgCfgDefaultNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 15),
    _CssgCfgDefaultNetwork_Type()
)
cssgCfgDefaultNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgDefaultNetwork.setStatus("current")
_CssgCfgRadiusAuthenPort_Type = CiscoPort
_CssgCfgRadiusAuthenPort_Object = MibScalar
cssgCfgRadiusAuthenPort = _CssgCfgRadiusAuthenPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 16),
    _CssgCfgRadiusAuthenPort_Type()
)
cssgCfgRadiusAuthenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgRadiusAuthenPort.setStatus("current")
_CssgCfgRadiusAccountingPort_Type = CiscoPort
_CssgCfgRadiusAccountingPort_Object = MibScalar
cssgCfgRadiusAccountingPort = _CssgCfgRadiusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 17),
    _CssgCfgRadiusAccountingPort_Type()
)
cssgCfgRadiusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgRadiusAccountingPort.setStatus("current")
_CssgCfgRadiusFwdAcctPktsEnabled_Type = TruthValue
_CssgCfgRadiusFwdAcctPktsEnabled_Object = MibScalar
cssgCfgRadiusFwdAcctPktsEnabled = _CssgCfgRadiusFwdAcctPktsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 18),
    _CssgCfgRadiusFwdAcctPktsEnabled_Type()
)
cssgCfgRadiusFwdAcctPktsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgRadiusFwdAcctPktsEnabled.setStatus("current")


class _CssgCfgAccountingInterval_Type(Unsigned32):
    """Custom type cssgCfgAccountingInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2147483647),
    )


_CssgCfgAccountingInterval_Type.__name__ = "Unsigned32"
_CssgCfgAccountingInterval_Object = MibScalar
cssgCfgAccountingInterval = _CssgCfgAccountingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 19),
    _CssgCfgAccountingInterval_Type()
)
cssgCfgAccountingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgAccountingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cssgCfgAccountingInterval.setUnits("seconds")
_CssgCfgTCPRedirGrpForUnAuthUsers_Type = DisplayString
_CssgCfgTCPRedirGrpForUnAuthUsers_Object = MibScalar
cssgCfgTCPRedirGrpForUnAuthUsers = _CssgCfgTCPRedirGrpForUnAuthUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 20),
    _CssgCfgTCPRedirGrpForUnAuthUsers_Type()
)
cssgCfgTCPRedirGrpForUnAuthUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgTCPRedirGrpForUnAuthUsers.setStatus("current")
_CssgCfgTCPRedirGrpForUnAuthServ_Type = DisplayString
_CssgCfgTCPRedirGrpForUnAuthServ_Object = MibScalar
cssgCfgTCPRedirGrpForUnAuthServ = _CssgCfgTCPRedirGrpForUnAuthServ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 21),
    _CssgCfgTCPRedirGrpForUnAuthServ_Type()
)
cssgCfgTCPRedirGrpForUnAuthServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgTCPRedirGrpForUnAuthServ.setStatus("current")
_CssgCfgTcpRedirGrpForSMTP_Type = DisplayString
_CssgCfgTcpRedirGrpForSMTP_Object = MibScalar
cssgCfgTcpRedirGrpForSMTP = _CssgCfgTcpRedirGrpForSMTP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 22),
    _CssgCfgTcpRedirGrpForSMTP_Type()
)
cssgCfgTcpRedirGrpForSMTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgTcpRedirGrpForSMTP.setStatus("current")
_CssgCfgTcpRedirGrpForInitialCapt_Type = DisplayString
_CssgCfgTcpRedirGrpForInitialCapt_Object = MibScalar
cssgCfgTcpRedirGrpForInitialCapt = _CssgCfgTcpRedirGrpForInitialCapt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 23),
    _CssgCfgTcpRedirGrpForInitialCapt_Type()
)
cssgCfgTcpRedirGrpForInitialCapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgTcpRedirGrpForInitialCapt.setStatus("current")
_CssgCfgTcpRedirGrpForAdvCapt_Type = DisplayString
_CssgCfgTcpRedirGrpForAdvCapt_Object = MibScalar
cssgCfgTcpRedirGrpForAdvCapt = _CssgCfgTcpRedirGrpForAdvCapt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 24),
    _CssgCfgTcpRedirGrpForAdvCapt_Type()
)
cssgCfgTcpRedirGrpForAdvCapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgTcpRedirGrpForAdvCapt.setStatus("current")


class _CssgCfgRadiusClntRbtNotifEnabled_Type(TruthValue):
    """Custom type cssgCfgRadiusClntRbtNotifEnabled based on TruthValue"""


_CssgCfgRadiusClntRbtNotifEnabled_Object = MibScalar
cssgCfgRadiusClntRbtNotifEnabled = _CssgCfgRadiusClntRbtNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 25),
    _CssgCfgRadiusClntRbtNotifEnabled_Type()
)
cssgCfgRadiusClntRbtNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgRadiusClntRbtNotifEnabled.setStatus("current")


class _CssgCfgAAAServerDownNotifEnabled_Type(TruthValue):
    """Custom type cssgCfgAAAServerDownNotifEnabled based on TruthValue"""


_CssgCfgAAAServerDownNotifEnabled_Object = MibScalar
cssgCfgAAAServerDownNotifEnabled = _CssgCfgAAAServerDownNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 26),
    _CssgCfgAAAServerDownNotifEnabled_Type()
)
cssgCfgAAAServerDownNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgAAAServerDownNotifEnabled.setStatus("current")


class _CssgCfgTalEnabled_Type(TruthValue):
    """Custom type cssgCfgTalEnabled based on TruthValue"""


_CssgCfgTalEnabled_Object = MibScalar
cssgCfgTalEnabled = _CssgCfgTalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 1, 27),
    _CssgCfgTalEnabled_Type()
)
cssgCfgTalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgCfgTalEnabled.setStatus("current")
_CssgStatsObjects_ObjectIdentity = ObjectIdentity
cssgStatsObjects = _CssgStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 2)
)
_CssgStatsLoginAttempts_Type = Counter32
_CssgStatsLoginAttempts_Object = MibScalar
cssgStatsLoginAttempts = _CssgStatsLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 2, 1),
    _CssgStatsLoginAttempts_Type()
)
cssgStatsLoginAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgStatsLoginAttempts.setStatus("current")
_CssgStatsLoginsSuccessful_Type = Counter32
_CssgStatsLoginsSuccessful_Object = MibScalar
cssgStatsLoginsSuccessful = _CssgStatsLoginsSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 2, 2),
    _CssgStatsLoginsSuccessful_Type()
)
cssgStatsLoginsSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgStatsLoginsSuccessful.setStatus("current")
_CssgStatsActiveSessions_Type = Gauge32
_CssgStatsActiveSessions_Object = MibScalar
cssgStatsActiveSessions = _CssgStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 2, 3),
    _CssgStatsActiveSessions_Type()
)
cssgStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgStatsActiveSessions.setStatus("current")
_CssgStatsActiveHosts_Type = Gauge32
_CssgStatsActiveHosts_Object = MibScalar
cssgStatsActiveHosts = _CssgStatsActiveHosts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 2, 4),
    _CssgStatsActiveHosts_Type()
)
cssgStatsActiveHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgStatsActiveHosts.setStatus("current")
_CssgStatsActiveServices_Type = Gauge32
_CssgStatsActiveServices_Object = MibScalar
cssgStatsActiveServices = _CssgStatsActiveServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 2, 5),
    _CssgStatsActiveServices_Type()
)
cssgStatsActiveServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgStatsActiveServices.setStatus("current")
_CssgStatsPODs_Type = Counter32
_CssgStatsPODs_Object = MibScalar
cssgStatsPODs = _CssgStatsPODs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 2, 6),
    _CssgStatsPODs_Type()
)
cssgStatsPODs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgStatsPODs.setStatus("current")
_CssgService_ObjectIdentity = ObjectIdentity
cssgService = _CssgService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3)
)
_CssgServiceTable_Object = MibTable
cssgServiceTable = _CssgServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cssgServiceTable.setStatus("current")
_CssgServiceEntry_Object = MibTableRow
cssgServiceEntry = _CssgServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1)
)
cssgServiceEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgServiceName"),
)
if mibBuilder.loadTexts:
    cssgServiceEntry.setStatus("current")


class _CssgServiceName_Type(DisplayString):
    """Custom type cssgServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CssgServiceName_Type.__name__ = "DisplayString"
_CssgServiceName_Object = MibTableColumn
cssgServiceName = _CssgServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 1),
    _CssgServiceName_Type()
)
cssgServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgServiceName.setStatus("current")


class _CssgServiceMode_Type(Integer32):
    """Custom type cssgServiceMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("concurrent", 2),
          ("sequential", 3),
          ("unknown", 1))
    )


_CssgServiceMode_Type.__name__ = "Integer32"
_CssgServiceMode_Object = MibTableColumn
cssgServiceMode = _CssgServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 2),
    _CssgServiceMode_Type()
)
cssgServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceMode.setStatus("current")


class _CssgServiceType_Type(Integer32):
    """Custom type cssgServiceType based on Integer32"""
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
        *(("passthrough", 2),
          ("proxy", 4),
          ("tunnel", 3),
          ("unknown", 1))
    )


_CssgServiceType_Type.__name__ = "Integer32"
_CssgServiceType_Object = MibTableColumn
cssgServiceType = _CssgServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 3),
    _CssgServiceType_Type()
)
cssgServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceType.setStatus("current")
_CssgServiceIdleTimeout_Type = Unsigned32
_CssgServiceIdleTimeout_Object = MibTableColumn
cssgServiceIdleTimeout = _CssgServiceIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 4),
    _CssgServiceIdleTimeout_Type()
)
cssgServiceIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cssgServiceIdleTimeout.setUnits("seconds")
_CssgServiceSessionTimeout_Type = Unsigned32
_CssgServiceSessionTimeout_Object = MibTableColumn
cssgServiceSessionTimeout = _CssgServiceSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 5),
    _CssgServiceSessionTimeout_Type()
)
cssgServiceSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cssgServiceSessionTimeout.setUnits("seconds")
_CssgServiceActiveSessions_Type = Gauge32
_CssgServiceActiveSessions_Object = MibTableColumn
cssgServiceActiveSessions = _CssgServiceActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 6),
    _CssgServiceActiveSessions_Type()
)
cssgServiceActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceActiveSessions.setStatus("current")
_CssgServiceDNSPrimaryIpType_Type = InetAddressType
_CssgServiceDNSPrimaryIpType_Object = MibTableColumn
cssgServiceDNSPrimaryIpType = _CssgServiceDNSPrimaryIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 7),
    _CssgServiceDNSPrimaryIpType_Type()
)
cssgServiceDNSPrimaryIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceDNSPrimaryIpType.setStatus("current")
_CssgServiceDNSPrimary_Type = InetAddress
_CssgServiceDNSPrimary_Object = MibTableColumn
cssgServiceDNSPrimary = _CssgServiceDNSPrimary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 8),
    _CssgServiceDNSPrimary_Type()
)
cssgServiceDNSPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceDNSPrimary.setStatus("current")
_CssgServiceDNSSecondaryIpType_Type = InetAddressType
_CssgServiceDNSSecondaryIpType_Object = MibTableColumn
cssgServiceDNSSecondaryIpType = _CssgServiceDNSSecondaryIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 9),
    _CssgServiceDNSSecondaryIpType_Type()
)
cssgServiceDNSSecondaryIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceDNSSecondaryIpType.setStatus("current")
_CssgServiceDNSSecondary_Type = InetAddress
_CssgServiceDNSSecondary_Object = MibTableColumn
cssgServiceDNSSecondary = _CssgServiceDNSSecondary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 10),
    _CssgServiceDNSSecondary_Type()
)
cssgServiceDNSSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceDNSSecondary.setStatus("current")
_CssgServiceUpstreamQOSEnabled_Type = TruthValue
_CssgServiceUpstreamQOSEnabled_Object = MibTableColumn
cssgServiceUpstreamQOSEnabled = _CssgServiceUpstreamQOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 11),
    _CssgServiceUpstreamQOSEnabled_Type()
)
cssgServiceUpstreamQOSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceUpstreamQOSEnabled.setStatus("current")
_CssgServiceDownStreamQOSEnabled_Type = TruthValue
_CssgServiceDownStreamQOSEnabled_Object = MibTableColumn
cssgServiceDownStreamQOSEnabled = _CssgServiceDownStreamQOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 12),
    _CssgServiceDownStreamQOSEnabled_Type()
)
cssgServiceDownStreamQOSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceDownStreamQOSEnabled.setStatus("current")
_CssgServiceOpenGarden_Type = TruthValue
_CssgServiceOpenGarden_Object = MibTableColumn
cssgServiceOpenGarden = _CssgServiceOpenGarden_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 13),
    _CssgServiceOpenGarden_Type()
)
cssgServiceOpenGarden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceOpenGarden.setStatus("current")
_CssgServicePrepaid_Type = TruthValue
_CssgServicePrepaid_Object = MibTableColumn
cssgServicePrepaid = _CssgServicePrepaid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 1, 1, 14),
    _CssgServicePrepaid_Type()
)
cssgServicePrepaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServicePrepaid.setStatus("current")
_CssgServiceRouteTable_Object = MibTable
cssgServiceRouteTable = _CssgServiceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cssgServiceRouteTable.setStatus("current")
_CssgServiceRouteEntry_Object = MibTableRow
cssgServiceRouteEntry = _CssgServiceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 2, 1)
)
cssgServiceRouteEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgServiceName"),
    (0, "CISCO-SSG-MIB", "cssgServiceRouteType"),
    (0, "CISCO-SSG-MIB", "cssgServiceRouteAddr"),
    (0, "CISCO-SSG-MIB", "cssgServiceRouteMaskType"),
    (0, "CISCO-SSG-MIB", "cssgServiceRouteMask"),
)
if mibBuilder.loadTexts:
    cssgServiceRouteEntry.setStatus("current")
_CssgServiceRouteType_Type = InetAddressType
_CssgServiceRouteType_Object = MibTableColumn
cssgServiceRouteType = _CssgServiceRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 2, 1, 1),
    _CssgServiceRouteType_Type()
)
cssgServiceRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgServiceRouteType.setStatus("current")
_CssgServiceRouteAddr_Type = InetAddress
_CssgServiceRouteAddr_Object = MibTableColumn
cssgServiceRouteAddr = _CssgServiceRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 2, 1, 2),
    _CssgServiceRouteAddr_Type()
)
cssgServiceRouteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgServiceRouteAddr.setStatus("current")
_CssgServiceRouteMaskType_Type = InetAddressType
_CssgServiceRouteMaskType_Object = MibTableColumn
cssgServiceRouteMaskType = _CssgServiceRouteMaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 2, 1, 3),
    _CssgServiceRouteMaskType_Type()
)
cssgServiceRouteMaskType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgServiceRouteMaskType.setStatus("current")
_CssgServiceRouteMask_Type = InetAddress
_CssgServiceRouteMask_Object = MibTableColumn
cssgServiceRouteMask = _CssgServiceRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 2, 1, 4),
    _CssgServiceRouteMask_Type()
)
cssgServiceRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgServiceRouteMask.setStatus("current")


class _CssgServiceRoutePermission_Type(Integer32):
    """Custom type cssgServiceRoutePermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_CssgServiceRoutePermission_Type.__name__ = "Integer32"
_CssgServiceRoutePermission_Object = MibTableColumn
cssgServiceRoutePermission = _CssgServiceRoutePermission_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 3, 2, 1, 5),
    _CssgServiceRoutePermission_Type()
)
cssgServiceRoutePermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgServiceRoutePermission.setStatus("current")
_CssgExcludedAPN_ObjectIdentity = ObjectIdentity
cssgExcludedAPN = _CssgExcludedAPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 4)
)
_CssgExcludedAPNTable_Object = MibTable
cssgExcludedAPNTable = _CssgExcludedAPNTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cssgExcludedAPNTable.setStatus("current")
_CssgExcludedAPNEntry_Object = MibTableRow
cssgExcludedAPNEntry = _CssgExcludedAPNEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 4, 1, 1)
)
cssgExcludedAPNEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgExcludedAPNName"),
)
if mibBuilder.loadTexts:
    cssgExcludedAPNEntry.setStatus("current")


class _CssgExcludedAPNName_Type(DisplayString):
    """Custom type cssgExcludedAPNName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CssgExcludedAPNName_Type.__name__ = "DisplayString"
_CssgExcludedAPNName_Object = MibTableColumn
cssgExcludedAPNName = _CssgExcludedAPNName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 4, 1, 1, 1),
    _CssgExcludedAPNName_Type()
)
cssgExcludedAPNName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgExcludedAPNName.setStatus("current")
_CssgExcludedAPNRowStatus_Type = RowStatus
_CssgExcludedAPNRowStatus_Object = MibTableColumn
cssgExcludedAPNRowStatus = _CssgExcludedAPNRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 4, 1, 1, 2),
    _CssgExcludedAPNRowStatus_Type()
)
cssgExcludedAPNRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgExcludedAPNRowStatus.setStatus("current")
_CssgExcludedDomain_ObjectIdentity = ObjectIdentity
cssgExcludedDomain = _CssgExcludedDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 5)
)
_CssgExcludedDomainTable_Object = MibTable
cssgExcludedDomainTable = _CssgExcludedDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cssgExcludedDomainTable.setStatus("current")
_CssgExcludedDomainEntry_Object = MibTableRow
cssgExcludedDomainEntry = _CssgExcludedDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 5, 1, 1)
)
cssgExcludedDomainEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgExcludedDomainName"),
)
if mibBuilder.loadTexts:
    cssgExcludedDomainEntry.setStatus("current")


class _CssgExcludedDomainName_Type(DisplayString):
    """Custom type cssgExcludedDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CssgExcludedDomainName_Type.__name__ = "DisplayString"
_CssgExcludedDomainName_Object = MibTableColumn
cssgExcludedDomainName = _CssgExcludedDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 5, 1, 1, 1),
    _CssgExcludedDomainName_Type()
)
cssgExcludedDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgExcludedDomainName.setStatus("current")
_CssgExcludedDomainRowStatus_Type = RowStatus
_CssgExcludedDomainRowStatus_Object = MibTableColumn
cssgExcludedDomainRowStatus = _CssgExcludedDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 5, 1, 1, 2),
    _CssgExcludedDomainRowStatus_Type()
)
cssgExcludedDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgExcludedDomainRowStatus.setStatus("current")
_CssgTcpRedirect_ObjectIdentity = ObjectIdentity
cssgTcpRedirect = _CssgTcpRedirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6)
)
_CssgTcpRedirectGrpTable_Object = MibTable
cssgTcpRedirectGrpTable = _CssgTcpRedirectGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cssgTcpRedirectGrpTable.setStatus("current")
_CssgTcpRedirectGrpEntry_Object = MibTableRow
cssgTcpRedirectGrpEntry = _CssgTcpRedirectGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 1, 1)
)
cssgTcpRedirectGrpEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgTcpRedirectGrpName"),
    (0, "CISCO-SSG-MIB", "cssgTcpRedirectGrpServerAddrType"),
    (0, "CISCO-SSG-MIB", "cssgTcpRedirectGrpServerAddr"),
    (0, "CISCO-SSG-MIB", "cssgTcpRedirectGrpServerPort"),
)
if mibBuilder.loadTexts:
    cssgTcpRedirectGrpEntry.setStatus("current")


class _CssgTcpRedirectGrpName_Type(DisplayString):
    """Custom type cssgTcpRedirectGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CssgTcpRedirectGrpName_Type.__name__ = "DisplayString"
_CssgTcpRedirectGrpName_Object = MibTableColumn
cssgTcpRedirectGrpName = _CssgTcpRedirectGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 1, 1, 1),
    _CssgTcpRedirectGrpName_Type()
)
cssgTcpRedirectGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgTcpRedirectGrpName.setStatus("current")
_CssgTcpRedirectGrpServerAddrType_Type = InetAddressType
_CssgTcpRedirectGrpServerAddrType_Object = MibTableColumn
cssgTcpRedirectGrpServerAddrType = _CssgTcpRedirectGrpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 1, 1, 2),
    _CssgTcpRedirectGrpServerAddrType_Type()
)
cssgTcpRedirectGrpServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgTcpRedirectGrpServerAddrType.setStatus("current")
_CssgTcpRedirectGrpServerAddr_Type = InetAddress
_CssgTcpRedirectGrpServerAddr_Object = MibTableColumn
cssgTcpRedirectGrpServerAddr = _CssgTcpRedirectGrpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 1, 1, 3),
    _CssgTcpRedirectGrpServerAddr_Type()
)
cssgTcpRedirectGrpServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgTcpRedirectGrpServerAddr.setStatus("current")
_CssgTcpRedirectGrpServerPort_Type = CiscoPort
_CssgTcpRedirectGrpServerPort_Object = MibTableColumn
cssgTcpRedirectGrpServerPort = _CssgTcpRedirectGrpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 1, 1, 4),
    _CssgTcpRedirectGrpServerPort_Type()
)
cssgTcpRedirectGrpServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgTcpRedirectGrpServerPort.setStatus("current")
_CssgTcpRedirectGrpRowStatus_Type = RowStatus
_CssgTcpRedirectGrpRowStatus_Object = MibTableColumn
cssgTcpRedirectGrpRowStatus = _CssgTcpRedirectGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 1, 1, 5),
    _CssgTcpRedirectGrpRowStatus_Type()
)
cssgTcpRedirectGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgTcpRedirectGrpRowStatus.setStatus("current")
_CssgNetworkGrpTable_Object = MibTable
cssgNetworkGrpTable = _CssgNetworkGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cssgNetworkGrpTable.setStatus("current")
_CssgNetworkGrpEntry_Object = MibTableRow
cssgNetworkGrpEntry = _CssgNetworkGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 2, 1)
)
cssgNetworkGrpEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgNetworkGrpName"),
    (0, "CISCO-SSG-MIB", "cssgNetworkGrpNetIpType"),
    (0, "CISCO-SSG-MIB", "cssgNetworkGrpNetIpAddr"),
    (0, "CISCO-SSG-MIB", "cssgNetworkGrpNetMaskType"),
    (0, "CISCO-SSG-MIB", "cssgNetworkGrpNetMask"),
)
if mibBuilder.loadTexts:
    cssgNetworkGrpEntry.setStatus("current")


class _CssgNetworkGrpName_Type(DisplayString):
    """Custom type cssgNetworkGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CssgNetworkGrpName_Type.__name__ = "DisplayString"
_CssgNetworkGrpName_Object = MibTableColumn
cssgNetworkGrpName = _CssgNetworkGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 2, 1, 1),
    _CssgNetworkGrpName_Type()
)
cssgNetworkGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgNetworkGrpName.setStatus("current")
_CssgNetworkGrpNetIpType_Type = InetAddressType
_CssgNetworkGrpNetIpType_Object = MibTableColumn
cssgNetworkGrpNetIpType = _CssgNetworkGrpNetIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 2, 1, 2),
    _CssgNetworkGrpNetIpType_Type()
)
cssgNetworkGrpNetIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgNetworkGrpNetIpType.setStatus("current")
_CssgNetworkGrpNetIpAddr_Type = InetAddress
_CssgNetworkGrpNetIpAddr_Object = MibTableColumn
cssgNetworkGrpNetIpAddr = _CssgNetworkGrpNetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 2, 1, 3),
    _CssgNetworkGrpNetIpAddr_Type()
)
cssgNetworkGrpNetIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgNetworkGrpNetIpAddr.setStatus("current")
_CssgNetworkGrpNetMaskType_Type = InetAddressType
_CssgNetworkGrpNetMaskType_Object = MibTableColumn
cssgNetworkGrpNetMaskType = _CssgNetworkGrpNetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 2, 1, 4),
    _CssgNetworkGrpNetMaskType_Type()
)
cssgNetworkGrpNetMaskType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgNetworkGrpNetMaskType.setStatus("current")
_CssgNetworkGrpNetMask_Type = InetAddress
_CssgNetworkGrpNetMask_Object = MibTableColumn
cssgNetworkGrpNetMask = _CssgNetworkGrpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 2, 1, 5),
    _CssgNetworkGrpNetMask_Type()
)
cssgNetworkGrpNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgNetworkGrpNetMask.setStatus("current")
_CssgNetworkGrpNetRowStatus_Type = RowStatus
_CssgNetworkGrpNetRowStatus_Object = MibTableColumn
cssgNetworkGrpNetRowStatus = _CssgNetworkGrpNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 2, 1, 6),
    _CssgNetworkGrpNetRowStatus_Type()
)
cssgNetworkGrpNetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgNetworkGrpNetRowStatus.setStatus("current")
_CssgPortGrpTable_Object = MibTable
cssgPortGrpTable = _CssgPortGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cssgPortGrpTable.setStatus("current")
_CssgPortGrpEntry_Object = MibTableRow
cssgPortGrpEntry = _CssgPortGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 3, 1)
)
cssgPortGrpEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgPortGrpName"),
    (0, "CISCO-SSG-MIB", "cssgPortGrpPortNo"),
)
if mibBuilder.loadTexts:
    cssgPortGrpEntry.setStatus("current")


class _CssgPortGrpName_Type(DisplayString):
    """Custom type cssgPortGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CssgPortGrpName_Type.__name__ = "DisplayString"
_CssgPortGrpName_Object = MibTableColumn
cssgPortGrpName = _CssgPortGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 3, 1, 1),
    _CssgPortGrpName_Type()
)
cssgPortGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgPortGrpName.setStatus("current")
_CssgPortGrpPortNo_Type = CiscoPort
_CssgPortGrpPortNo_Object = MibTableColumn
cssgPortGrpPortNo = _CssgPortGrpPortNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 3, 1, 2),
    _CssgPortGrpPortNo_Type()
)
cssgPortGrpPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgPortGrpPortNo.setStatus("current")
_CssgPortGrpPortRowStatus_Type = RowStatus
_CssgPortGrpPortRowStatus_Object = MibTableColumn
cssgPortGrpPortRowStatus = _CssgPortGrpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 3, 1, 3),
    _CssgPortGrpPortRowStatus_Type()
)
cssgPortGrpPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgPortGrpPortRowStatus.setStatus("current")
_CssgTcpRedirNetworkGrpMapTable_Object = MibTable
cssgTcpRedirNetworkGrpMapTable = _CssgTcpRedirNetworkGrpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cssgTcpRedirNetworkGrpMapTable.setStatus("current")
_CssgTcpRedirNetworkGrpMapEntry_Object = MibTableRow
cssgTcpRedirNetworkGrpMapEntry = _CssgTcpRedirNetworkGrpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 4, 1)
)
cssgTcpRedirNetworkGrpMapEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgTcpRedirectGrpName"),
)
if mibBuilder.loadTexts:
    cssgTcpRedirNetworkGrpMapEntry.setStatus("current")


class _CssgTcpRedirNetworkMapGrpName_Type(DisplayString):
    """Custom type cssgTcpRedirNetworkMapGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CssgTcpRedirNetworkMapGrpName_Type.__name__ = "DisplayString"
_CssgTcpRedirNetworkMapGrpName_Object = MibTableColumn
cssgTcpRedirNetworkMapGrpName = _CssgTcpRedirNetworkMapGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 4, 1, 1),
    _CssgTcpRedirNetworkMapGrpName_Type()
)
cssgTcpRedirNetworkMapGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgTcpRedirNetworkMapGrpName.setStatus("current")
_CssgTcpRedirNetworkGrpMapRowStat_Type = RowStatus
_CssgTcpRedirNetworkGrpMapRowStat_Object = MibTableColumn
cssgTcpRedirNetworkGrpMapRowStat = _CssgTcpRedirNetworkGrpMapRowStat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 4, 1, 2),
    _CssgTcpRedirNetworkGrpMapRowStat_Type()
)
cssgTcpRedirNetworkGrpMapRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgTcpRedirNetworkGrpMapRowStat.setStatus("current")
_CssgTcpRedirPortGrpMapTable_Object = MibTable
cssgTcpRedirPortGrpMapTable = _CssgTcpRedirPortGrpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 5)
)
if mibBuilder.loadTexts:
    cssgTcpRedirPortGrpMapTable.setStatus("current")
_CssgTcpRedirPortGrpMapEntry_Object = MibTableRow
cssgTcpRedirPortGrpMapEntry = _CssgTcpRedirPortGrpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 5, 1)
)
cssgTcpRedirPortGrpMapEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgTcpRedirectGrpName"),
)
if mibBuilder.loadTexts:
    cssgTcpRedirPortGrpMapEntry.setStatus("current")


class _CssgTcpRedirPortMapGrpName_Type(DisplayString):
    """Custom type cssgTcpRedirPortMapGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CssgTcpRedirPortMapGrpName_Type.__name__ = "DisplayString"
_CssgTcpRedirPortMapGrpName_Object = MibTableColumn
cssgTcpRedirPortMapGrpName = _CssgTcpRedirPortMapGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 5, 1, 1),
    _CssgTcpRedirPortMapGrpName_Type()
)
cssgTcpRedirPortMapGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgTcpRedirPortMapGrpName.setStatus("current")
_CssgTcpRedirPortGrpMapRowStat_Type = RowStatus
_CssgTcpRedirPortGrpMapRowStat_Object = MibTableColumn
cssgTcpRedirPortGrpMapRowStat = _CssgTcpRedirPortGrpMapRowStat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 5, 1, 2),
    _CssgTcpRedirPortGrpMapRowStat_Type()
)
cssgTcpRedirPortGrpMapRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgTcpRedirPortGrpMapRowStat.setStatus("current")
_CssgTcpRedirPortNoMapTable_Object = MibTable
cssgTcpRedirPortNoMapTable = _CssgTcpRedirPortNoMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 6)
)
if mibBuilder.loadTexts:
    cssgTcpRedirPortNoMapTable.setStatus("current")
_CssgTcpRedirPortNoMapEntry_Object = MibTableRow
cssgTcpRedirPortNoMapEntry = _CssgTcpRedirPortNoMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 6, 1)
)
cssgTcpRedirPortNoMapEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgTcpRedirectGrpName"),
)
if mibBuilder.loadTexts:
    cssgTcpRedirPortNoMapEntry.setStatus("current")
_CssgTcpRedirPortNo_Type = CiscoPort
_CssgTcpRedirPortNo_Object = MibTableColumn
cssgTcpRedirPortNo = _CssgTcpRedirPortNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 6, 1, 1),
    _CssgTcpRedirPortNo_Type()
)
cssgTcpRedirPortNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgTcpRedirPortNo.setStatus("current")
_CssgTcpRedirPortNoMapRowStat_Type = RowStatus
_CssgTcpRedirPortNoMapRowStat_Object = MibTableColumn
cssgTcpRedirPortNoMapRowStat = _CssgTcpRedirPortNoMapRowStat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 6, 6, 1, 2),
    _CssgTcpRedirPortNoMapRowStat_Type()
)
cssgTcpRedirPortNoMapRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgTcpRedirPortNoMapRowStat.setStatus("current")
_CssgServiceIfBinds_ObjectIdentity = ObjectIdentity
cssgServiceIfBinds = _CssgServiceIfBinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 7)
)
_CssgServiceIfBindTable_Object = MibTable
cssgServiceIfBindTable = _CssgServiceIfBindTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cssgServiceIfBindTable.setStatus("current")
_CssgServiceIfBindEntry_Object = MibTableRow
cssgServiceIfBindEntry = _CssgServiceIfBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 7, 1, 1)
)
cssgServiceIfBindEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgServiceName"),
)
if mibBuilder.loadTexts:
    cssgServiceIfBindEntry.setStatus("current")
_CssgServiceIfIndex_Type = InterfaceIndex
_CssgServiceIfIndex_Object = MibTableColumn
cssgServiceIfIndex = _CssgServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 7, 1, 1, 1),
    _CssgServiceIfIndex_Type()
)
cssgServiceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgServiceIfIndex.setStatus("current")
_CssgServiceIfRowStatus_Type = RowStatus
_CssgServiceIfRowStatus_Object = MibTableColumn
cssgServiceIfRowStatus = _CssgServiceIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 7, 1, 1, 2),
    _CssgServiceIfRowStatus_Type()
)
cssgServiceIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgServiceIfRowStatus.setStatus("current")
_CssgRadiusClients_ObjectIdentity = ObjectIdentity
cssgRadiusClients = _CssgRadiusClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 8)
)
_CssgRadiusClientTable_Object = MibTable
cssgRadiusClientTable = _CssgRadiusClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cssgRadiusClientTable.setStatus("current")
_CssgRadiusClientEntry_Object = MibTableRow
cssgRadiusClientEntry = _CssgRadiusClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 8, 1, 1)
)
cssgRadiusClientEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgRadiusClientAddrType"),
    (0, "CISCO-SSG-MIB", "cssgRadiusClientAddr"),
)
if mibBuilder.loadTexts:
    cssgRadiusClientEntry.setStatus("current")
_CssgRadiusClientAddrType_Type = InetAddressType
_CssgRadiusClientAddrType_Object = MibTableColumn
cssgRadiusClientAddrType = _CssgRadiusClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 8, 1, 1, 1),
    _CssgRadiusClientAddrType_Type()
)
cssgRadiusClientAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgRadiusClientAddrType.setStatus("current")
_CssgRadiusClientAddr_Type = InetAddress
_CssgRadiusClientAddr_Object = MibTableColumn
cssgRadiusClientAddr = _CssgRadiusClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 8, 1, 1, 2),
    _CssgRadiusClientAddr_Type()
)
cssgRadiusClientAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgRadiusClientAddr.setStatus("current")
_CssgRadiusClientRowStatus_Type = RowStatus
_CssgRadiusClientRowStatus_Object = MibTableColumn
cssgRadiusClientRowStatus = _CssgRadiusClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 8, 1, 1, 3),
    _CssgRadiusClientRowStatus_Type()
)
cssgRadiusClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgRadiusClientRowStatus.setStatus("current")
_CssgPortMap_ObjectIdentity = ObjectIdentity
cssgPortMap = _CssgPortMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 9)
)
_CssgPortMapLength_Type = Unsigned32
_CssgPortMapLength_Object = MibScalar
cssgPortMapLength = _CssgPortMapLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 9, 1),
    _CssgPortMapLength_Type()
)
cssgPortMapLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgPortMapLength.setStatus("current")
_CssgPortMapTable_Object = MibTable
cssgPortMapTable = _CssgPortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 9, 2)
)
if mibBuilder.loadTexts:
    cssgPortMapTable.setStatus("current")
_CssgPortMapEntry_Object = MibTableRow
cssgPortMapEntry = _CssgPortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 9, 2, 1)
)
cssgPortMapEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgPortMapSourceIpType"),
    (0, "CISCO-SSG-MIB", "cssgPortMapSourceIp"),
)
if mibBuilder.loadTexts:
    cssgPortMapEntry.setStatus("current")
_CssgPortMapSourceIpType_Type = InetAddressType
_CssgPortMapSourceIpType_Object = MibTableColumn
cssgPortMapSourceIpType = _CssgPortMapSourceIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 9, 2, 1, 1),
    _CssgPortMapSourceIpType_Type()
)
cssgPortMapSourceIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgPortMapSourceIpType.setStatus("current")
_CssgPortMapSourceIp_Type = InetAddress
_CssgPortMapSourceIp_Object = MibTableColumn
cssgPortMapSourceIp = _CssgPortMapSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 9, 2, 1, 2),
    _CssgPortMapSourceIp_Type()
)
cssgPortMapSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgPortMapSourceIp.setStatus("current")
_CssgPortMapPortRangeFrom_Type = CiscoPort
_CssgPortMapPortRangeFrom_Object = MibTableColumn
cssgPortMapPortRangeFrom = _CssgPortMapPortRangeFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 9, 2, 1, 3),
    _CssgPortMapPortRangeFrom_Type()
)
cssgPortMapPortRangeFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgPortMapPortRangeFrom.setStatus("current")
_CssgPortMapPortRangeTo_Type = CiscoPort
_CssgPortMapPortRangeTo_Object = MibTableColumn
cssgPortMapPortRangeTo = _CssgPortMapPortRangeTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 9, 2, 1, 4),
    _CssgPortMapPortRangeTo_Type()
)
cssgPortMapPortRangeTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgPortMapPortRangeTo.setStatus("current")
_CssgPortMapRowStatus_Type = RowStatus
_CssgPortMapRowStatus_Object = MibTableColumn
cssgPortMapRowStatus = _CssgPortMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 9, 2, 1, 5),
    _CssgPortMapRowStatus_Type()
)
cssgPortMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cssgPortMapRowStatus.setStatus("current")
_CssgTal_ObjectIdentity = ObjectIdentity
cssgTal = _CssgTal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10)
)
_CssgTalWaitingForAuthUsers_Type = Gauge32
_CssgTalWaitingForAuthUsers_Object = MibScalar
cssgTalWaitingForAuthUsers = _CssgTalWaitingForAuthUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 1),
    _CssgTalWaitingForAuthUsers_Type()
)
cssgTalWaitingForAuthUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgTalWaitingForAuthUsers.setStatus("current")
_CssgTalUnidentifiedUsers_Type = Gauge32
_CssgTalUnidentifiedUsers_Object = MibScalar
cssgTalUnidentifiedUsers = _CssgTalUnidentifiedUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 2),
    _CssgTalUnidentifiedUsers_Type()
)
cssgTalUnidentifiedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgTalUnidentifiedUsers.setStatus("current")
_CssgTalSuspectUsers_Type = Gauge32
_CssgTalSuspectUsers_Object = MibScalar
cssgTalSuspectUsers = _CssgTalSuspectUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 3),
    _CssgTalSuspectUsers_Type()
)
cssgTalSuspectUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgTalSuspectUsers.setStatus("current")
_CssgTalPassthroughUsers_Type = Gauge32
_CssgTalPassthroughUsers_Object = MibScalar
cssgTalPassthroughUsers = _CssgTalPassthroughUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 4),
    _CssgTalPassthroughUsers_Type()
)
cssgTalPassthroughUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgTalPassthroughUsers.setStatus("current")
_CssgTalMaxAuthRate_Type = Unsigned32
_CssgTalMaxAuthRate_Object = MibScalar
cssgTalMaxAuthRate = _CssgTalMaxAuthRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 5),
    _CssgTalMaxAuthRate_Type()
)
cssgTalMaxAuthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgTalMaxAuthRate.setStatus("current")
_CssgTalMaxAuthRateTimestamp_Type = DateAndTime
_CssgTalMaxAuthRateTimestamp_Object = MibScalar
cssgTalMaxAuthRateTimestamp = _CssgTalMaxAuthRateTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 6),
    _CssgTalMaxAuthRateTimestamp_Type()
)
cssgTalMaxAuthRateTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgTalMaxAuthRateTimestamp.setStatus("current")
_CssgTalMinAuthRate_Type = Unsigned32
_CssgTalMinAuthRate_Object = MibScalar
cssgTalMinAuthRate = _CssgTalMinAuthRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 7),
    _CssgTalMinAuthRate_Type()
)
cssgTalMinAuthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgTalMinAuthRate.setStatus("current")
_CssgTalMinAuthRateTimestamp_Type = DateAndTime
_CssgTalMinAuthRateTimestamp_Object = MibScalar
cssgTalMinAuthRateTimestamp = _CssgTalMinAuthRateTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 8),
    _CssgTalMinAuthRateTimestamp_Type()
)
cssgTalMinAuthRateTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgTalMinAuthRateTimestamp.setStatus("current")
_CssgTalCurrentAuthRate_Type = Unsigned32
_CssgTalCurrentAuthRate_Object = MibScalar
cssgTalCurrentAuthRate = _CssgTalCurrentAuthRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 9),
    _CssgTalCurrentAuthRate_Type()
)
cssgTalCurrentAuthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgTalCurrentAuthRate.setStatus("current")
_CssgTalCurrentAuthRateTimestamp_Type = DateAndTime
_CssgTalCurrentAuthRateTimestamp_Object = MibScalar
cssgTalCurrentAuthRateTimestamp = _CssgTalCurrentAuthRateTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 10),
    _CssgTalCurrentAuthRateTimestamp_Type()
)
cssgTalCurrentAuthRateTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgTalCurrentAuthRateTimestamp.setStatus("current")


class _CssgTalResetAuthRates_Type(Integer32):
    """Custom type cssgTalResetAuthRates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("unknown", 1))
    )


_CssgTalResetAuthRates_Type.__name__ = "Integer32"
_CssgTalResetAuthRates_Object = MibScalar
cssgTalResetAuthRates = _CssgTalResetAuthRates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 11),
    _CssgTalResetAuthRates_Type()
)
cssgTalResetAuthRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgTalResetAuthRates.setStatus("current")
_CssgTalMaxPendingAuthReqs_Type = Unsigned32
_CssgTalMaxPendingAuthReqs_Object = MibScalar
cssgTalMaxPendingAuthReqs = _CssgTalMaxPendingAuthReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 12),
    _CssgTalMaxPendingAuthReqs_Type()
)
cssgTalMaxPendingAuthReqs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgTalMaxPendingAuthReqs.setStatus("current")
_CssgTalMaxAuthReqsRate_Type = Unsigned32
_CssgTalMaxAuthReqsRate_Object = MibScalar
cssgTalMaxAuthReqsRate = _CssgTalMaxAuthReqsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 13),
    _CssgTalMaxAuthReqsRate_Type()
)
cssgTalMaxAuthReqsRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgTalMaxAuthReqsRate.setStatus("current")


class _CssgTalDropPakDuringAuthorization_Type(TruthValue):
    """Custom type cssgTalDropPakDuringAuthorization based on TruthValue"""


_CssgTalDropPakDuringAuthorization_Object = MibScalar
cssgTalDropPakDuringAuthorization = _CssgTalDropPakDuringAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 14),
    _CssgTalDropPakDuringAuthorization_Type()
)
cssgTalDropPakDuringAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgTalDropPakDuringAuthorization.setStatus("current")


class _CssgTalUnidentifiedUserAllowTraff_Type(TruthValue):
    """Custom type cssgTalUnidentifiedUserAllowTraff based on TruthValue"""


_CssgTalUnidentifiedUserAllowTraff_Object = MibScalar
cssgTalUnidentifiedUserAllowTraff = _CssgTalUnidentifiedUserAllowTraff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 15),
    _CssgTalUnidentifiedUserAllowTraff_Type()
)
cssgTalUnidentifiedUserAllowTraff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgTalUnidentifiedUserAllowTraff.setStatus("current")


class _CssgTalMaxSuspectUsers_Type(Unsigned32):
    """Custom type cssgTalMaxSuspectUsers based on Unsigned32"""
    defaultValue = 5000


_CssgTalMaxSuspectUsers_Object = MibScalar
cssgTalMaxSuspectUsers = _CssgTalMaxSuspectUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 16),
    _CssgTalMaxSuspectUsers_Type()
)
cssgTalMaxSuspectUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgTalMaxSuspectUsers.setStatus("current")


class _CssgTalSuspectUserTimeout_Type(Unsigned32):
    """Custom type cssgTalSuspectUserTimeout based on Unsigned32"""
    defaultValue = 60


_CssgTalSuspectUserTimeout_Object = MibScalar
cssgTalSuspectUserTimeout = _CssgTalSuspectUserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 17),
    _CssgTalSuspectUserTimeout_Type()
)
cssgTalSuspectUserTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgTalSuspectUserTimeout.setStatus("current")


class _CssgTalUnidentifiedUserTimeout_Type(Unsigned32):
    """Custom type cssgTalUnidentifiedUserTimeout based on Unsigned32"""
    defaultValue = 10


_CssgTalUnidentifiedUserTimeout_Object = MibScalar
cssgTalUnidentifiedUserTimeout = _CssgTalUnidentifiedUserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 18),
    _CssgTalUnidentifiedUserTimeout_Type()
)
cssgTalUnidentifiedUserTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cssgTalUnidentifiedUserTimeout.setStatus("current")
_CssgTalUserInfoTable_Object = MibTable
cssgTalUserInfoTable = _CssgTalUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 19)
)
if mibBuilder.loadTexts:
    cssgTalUserInfoTable.setStatus("current")
_CssgTalUserInfoEntry_Object = MibTableRow
cssgTalUserInfoEntry = _CssgTalUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 19, 1)
)
cssgTalUserInfoEntry.setIndexNames(
    (0, "CISCO-SSG-MIB", "cssgTalUserIPAddressType"),
    (0, "CISCO-SSG-MIB", "cssgTalUserIPAddress"),
)
if mibBuilder.loadTexts:
    cssgTalUserInfoEntry.setStatus("current")
_CssgTalUserIPAddressType_Type = InetAddressType
_CssgTalUserIPAddressType_Object = MibTableColumn
cssgTalUserIPAddressType = _CssgTalUserIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 19, 1, 1),
    _CssgTalUserIPAddressType_Type()
)
cssgTalUserIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgTalUserIPAddressType.setStatus("current")
_CssgTalUserIPAddress_Type = InetAddress
_CssgTalUserIPAddress_Object = MibTableColumn
cssgTalUserIPAddress = _CssgTalUserIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 19, 1, 2),
    _CssgTalUserIPAddress_Type()
)
cssgTalUserIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cssgTalUserIPAddress.setStatus("current")


class _CssgTalUserState_Type(Integer32):
    """Custom type cssgTalUserState based on Integer32"""
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
        *(("authorizing", 2),
          ("other", 1),
          ("passthrough", 5),
          ("suspect", 4),
          ("unidentified", 3))
    )


_CssgTalUserState_Type.__name__ = "Integer32"
_CssgTalUserState_Object = MibTableColumn
cssgTalUserState = _CssgTalUserState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 1, 10, 19, 1, 3),
    _CssgTalUserState_Type()
)
cssgTalUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cssgTalUserState.setStatus("current")
_CiscoSsgMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSsgMIBConformance = _CiscoSsgMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3)
)
_CiscoSsgMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSsgMIBCompliances = _CiscoSsgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 1)
)
_CiscoSsgMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSsgMIBGroups = _CiscoSsgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2)
)

# Managed Objects groups

ciscoSsgCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2, 1)
)
ciscoSsgCfgGroup.setObjects(
      *(("CISCO-SSG-MIB", "cssgCfgSsgEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAutoDomainMode"),
        ("CISCO-SSG-MIB", "cssgCfgLocalForwardingEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAutoLogOffMode"),
        ("CISCO-SSG-MIB", "cssgCfgRadiusProxyEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgTcpRedirectEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAutoDomainNatEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgPortBundleHostKeyEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgTransPassThroughEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAutoLogOffInterval"),
        ("CISCO-SSG-MIB", "cssgCfgAutoLogOffIcmpRetries"),
        ("CISCO-SSG-MIB", "cssgCfgMaxServicesPerUser"),
        ("CISCO-SSG-MIB", "cssgCfgAccountingEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgDefaultNetworkType"),
        ("CISCO-SSG-MIB", "cssgCfgDefaultNetwork"),
        ("CISCO-SSG-MIB", "cssgCfgRadiusAuthenPort"),
        ("CISCO-SSG-MIB", "cssgCfgRadiusAccountingPort"),
        ("CISCO-SSG-MIB", "cssgCfgRadiusFwdAcctPktsEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAccountingInterval"),
        ("CISCO-SSG-MIB", "cssgCfgTCPRedirGrpForUnAuthUsers"),
        ("CISCO-SSG-MIB", "cssgCfgTCPRedirGrpForUnAuthServ"),
        ("CISCO-SSG-MIB", "cssgCfgTcpRedirGrpForSMTP"),
        ("CISCO-SSG-MIB", "cssgCfgTcpRedirGrpForInitialCapt"),
        ("CISCO-SSG-MIB", "cssgCfgTcpRedirGrpForAdvCapt"),
        ("CISCO-SSG-MIB", "cssgCfgRadiusClntRbtNotifEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAAAServerDownNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoSsgCfgGroup.setStatus("deprecated")

ciscoSsgStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2, 2)
)
ciscoSsgStatsGroup.setObjects(
      *(("CISCO-SSG-MIB", "cssgStatsLoginAttempts"),
        ("CISCO-SSG-MIB", "cssgStatsLoginsSuccessful"),
        ("CISCO-SSG-MIB", "cssgStatsActiveSessions"),
        ("CISCO-SSG-MIB", "cssgStatsActiveHosts"),
        ("CISCO-SSG-MIB", "cssgStatsActiveServices"),
        ("CISCO-SSG-MIB", "cssgStatsPODs"))
)
if mibBuilder.loadTexts:
    ciscoSsgStatsGroup.setStatus("current")

ciscoSsgServicesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2, 3)
)
ciscoSsgServicesGroup.setObjects(
      *(("CISCO-SSG-MIB", "cssgServiceMode"),
        ("CISCO-SSG-MIB", "cssgServiceType"),
        ("CISCO-SSG-MIB", "cssgServiceIdleTimeout"),
        ("CISCO-SSG-MIB", "cssgServiceSessionTimeout"),
        ("CISCO-SSG-MIB", "cssgServiceActiveSessions"),
        ("CISCO-SSG-MIB", "cssgServiceDNSPrimaryIpType"),
        ("CISCO-SSG-MIB", "cssgServiceDNSPrimary"),
        ("CISCO-SSG-MIB", "cssgServiceDNSSecondaryIpType"),
        ("CISCO-SSG-MIB", "cssgServiceDNSSecondary"),
        ("CISCO-SSG-MIB", "cssgServiceUpstreamQOSEnabled"),
        ("CISCO-SSG-MIB", "cssgServiceDownStreamQOSEnabled"),
        ("CISCO-SSG-MIB", "cssgServiceOpenGarden"),
        ("CISCO-SSG-MIB", "cssgServicePrepaid"),
        ("CISCO-SSG-MIB", "cssgServiceRoutePermission"))
)
if mibBuilder.loadTexts:
    ciscoSsgServicesGroup.setStatus("current")

ciscoSsgExclusionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2, 4)
)
ciscoSsgExclusionsGroup.setObjects(
      *(("CISCO-SSG-MIB", "cssgExcludedAPNRowStatus"),
        ("CISCO-SSG-MIB", "cssgExcludedDomainRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSsgExclusionsGroup.setStatus("current")

ciscoSsgTcpRedirectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2, 5)
)
ciscoSsgTcpRedirectGroup.setObjects(
      *(("CISCO-SSG-MIB", "cssgTcpRedirectGrpRowStatus"),
        ("CISCO-SSG-MIB", "cssgNetworkGrpNetRowStatus"),
        ("CISCO-SSG-MIB", "cssgPortGrpPortRowStatus"),
        ("CISCO-SSG-MIB", "cssgTcpRedirNetworkMapGrpName"),
        ("CISCO-SSG-MIB", "cssgTcpRedirNetworkGrpMapRowStat"),
        ("CISCO-SSG-MIB", "cssgTcpRedirPortMapGrpName"),
        ("CISCO-SSG-MIB", "cssgTcpRedirPortGrpMapRowStat"),
        ("CISCO-SSG-MIB", "cssgTcpRedirPortNo"),
        ("CISCO-SSG-MIB", "cssgTcpRedirPortNoMapRowStat"))
)
if mibBuilder.loadTexts:
    ciscoSsgTcpRedirectGroup.setStatus("current")

ciscoSsgServiceInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2, 6)
)
ciscoSsgServiceInterfaceGroup.setObjects(
      *(("CISCO-SSG-MIB", "cssgServiceIfIndex"),
        ("CISCO-SSG-MIB", "cssgServiceIfRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSsgServiceInterfaceGroup.setStatus("current")

ciscoSsgRadiusClientsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2, 7)
)
ciscoSsgRadiusClientsGroup.setObjects(
    ("CISCO-SSG-MIB", "cssgRadiusClientRowStatus")
)
if mibBuilder.loadTexts:
    ciscoSsgRadiusClientsGroup.setStatus("current")

ciscoSsgPortMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2, 8)
)
ciscoSsgPortMapGroup.setObjects(
      *(("CISCO-SSG-MIB", "cssgPortMapLength"),
        ("CISCO-SSG-MIB", "cssgPortMapPortRangeFrom"),
        ("CISCO-SSG-MIB", "cssgPortMapPortRangeTo"),
        ("CISCO-SSG-MIB", "cssgPortMapRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSsgPortMapGroup.setStatus("current")

ciscoSsgCfgGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2, 10)
)
ciscoSsgCfgGroupRev1.setObjects(
      *(("CISCO-SSG-MIB", "cssgCfgSsgEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAutoDomainMode"),
        ("CISCO-SSG-MIB", "cssgCfgLocalForwardingEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAutoLogOffMode"),
        ("CISCO-SSG-MIB", "cssgCfgRadiusProxyEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgTcpRedirectEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAutoDomainNatEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgPortBundleHostKeyEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgTransPassThroughEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAutoLogOffInterval"),
        ("CISCO-SSG-MIB", "cssgCfgAutoLogOffIcmpRetries"),
        ("CISCO-SSG-MIB", "cssgCfgMaxServicesPerUser"),
        ("CISCO-SSG-MIB", "cssgCfgAccountingEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgDefaultNetworkType"),
        ("CISCO-SSG-MIB", "cssgCfgDefaultNetwork"),
        ("CISCO-SSG-MIB", "cssgCfgRadiusAuthenPort"),
        ("CISCO-SSG-MIB", "cssgCfgRadiusAccountingPort"),
        ("CISCO-SSG-MIB", "cssgCfgRadiusFwdAcctPktsEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAccountingInterval"),
        ("CISCO-SSG-MIB", "cssgCfgTCPRedirGrpForUnAuthUsers"),
        ("CISCO-SSG-MIB", "cssgCfgTCPRedirGrpForUnAuthServ"),
        ("CISCO-SSG-MIB", "cssgCfgTcpRedirGrpForSMTP"),
        ("CISCO-SSG-MIB", "cssgCfgTcpRedirGrpForInitialCapt"),
        ("CISCO-SSG-MIB", "cssgCfgTcpRedirGrpForAdvCapt"),
        ("CISCO-SSG-MIB", "cssgCfgRadiusClntRbtNotifEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgAAAServerDownNotifEnabled"),
        ("CISCO-SSG-MIB", "cssgCfgTalEnabled"))
)
if mibBuilder.loadTexts:
    ciscoSsgCfgGroupRev1.setStatus("current")

ciscoSsgTalUserInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2, 11)
)
ciscoSsgTalUserInfoGroup.setObjects(
      *(("CISCO-SSG-MIB", "cssgTalWaitingForAuthUsers"),
        ("CISCO-SSG-MIB", "cssgTalUnidentifiedUsers"),
        ("CISCO-SSG-MIB", "cssgTalSuspectUsers"),
        ("CISCO-SSG-MIB", "cssgTalPassthroughUsers"),
        ("CISCO-SSG-MIB", "cssgTalMaxAuthRate"),
        ("CISCO-SSG-MIB", "cssgTalMaxAuthRateTimestamp"),
        ("CISCO-SSG-MIB", "cssgTalMinAuthRate"),
        ("CISCO-SSG-MIB", "cssgTalMinAuthRateTimestamp"),
        ("CISCO-SSG-MIB", "cssgTalCurrentAuthRate"),
        ("CISCO-SSG-MIB", "cssgTalCurrentAuthRateTimestamp"),
        ("CISCO-SSG-MIB", "cssgTalResetAuthRates"),
        ("CISCO-SSG-MIB", "cssgTalMaxPendingAuthReqs"),
        ("CISCO-SSG-MIB", "cssgTalMaxAuthReqsRate"),
        ("CISCO-SSG-MIB", "cssgTalDropPakDuringAuthorization"),
        ("CISCO-SSG-MIB", "cssgTalUnidentifiedUserAllowTraff"),
        ("CISCO-SSG-MIB", "cssgTalMaxSuspectUsers"),
        ("CISCO-SSG-MIB", "cssgTalSuspectUserTimeout"),
        ("CISCO-SSG-MIB", "cssgTalUnidentifiedUserTimeout"),
        ("CISCO-SSG-MIB", "cssgTalUserState"))
)
if mibBuilder.loadTexts:
    ciscoSsgTalUserInfoGroup.setStatus("current")


# Notification objects

ciscoSsgRadiusClientReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 0, 1)
)
if mibBuilder.loadTexts:
    ciscoSsgRadiusClientReboot.setStatus(
        "current"
    )

ciscoSsgRadiusAAAServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 0, 2)
)
if mibBuilder.loadTexts:
    ciscoSsgRadiusAAAServerDown.setStatus(
        "current"
    )


# Notifications groups

ciscoSsgNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 2, 9)
)
ciscoSsgNotificationGroup.setObjects(
      *(("CISCO-SSG-MIB", "ciscoSsgRadiusClientReboot"),
        ("CISCO-SSG-MIB", "ciscoSsgRadiusAAAServerDown"))
)
if mibBuilder.loadTexts:
    ciscoSsgNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSsgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSsgMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSsgMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 260, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSsgMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SSG-MIB",
    **{"ciscoSsgMIB": ciscoSsgMIB,
       "ciscoSsgMIBNotifications": ciscoSsgMIBNotifications,
       "ciscoSsgRadiusClientReboot": ciscoSsgRadiusClientReboot,
       "ciscoSsgRadiusAAAServerDown": ciscoSsgRadiusAAAServerDown,
       "ciscoSsgMIBObjects": ciscoSsgMIBObjects,
       "cssgCfgObjects": cssgCfgObjects,
       "cssgCfgSsgEnabled": cssgCfgSsgEnabled,
       "cssgCfgAutoDomainMode": cssgCfgAutoDomainMode,
       "cssgCfgLocalForwardingEnabled": cssgCfgLocalForwardingEnabled,
       "cssgCfgAutoLogOffMode": cssgCfgAutoLogOffMode,
       "cssgCfgRadiusProxyEnabled": cssgCfgRadiusProxyEnabled,
       "cssgCfgTcpRedirectEnabled": cssgCfgTcpRedirectEnabled,
       "cssgCfgAutoDomainNatEnabled": cssgCfgAutoDomainNatEnabled,
       "cssgCfgPortBundleHostKeyEnabled": cssgCfgPortBundleHostKeyEnabled,
       "cssgCfgTransPassThroughEnabled": cssgCfgTransPassThroughEnabled,
       "cssgCfgAutoLogOffInterval": cssgCfgAutoLogOffInterval,
       "cssgCfgAutoLogOffIcmpRetries": cssgCfgAutoLogOffIcmpRetries,
       "cssgCfgMaxServicesPerUser": cssgCfgMaxServicesPerUser,
       "cssgCfgAccountingEnabled": cssgCfgAccountingEnabled,
       "cssgCfgDefaultNetworkType": cssgCfgDefaultNetworkType,
       "cssgCfgDefaultNetwork": cssgCfgDefaultNetwork,
       "cssgCfgRadiusAuthenPort": cssgCfgRadiusAuthenPort,
       "cssgCfgRadiusAccountingPort": cssgCfgRadiusAccountingPort,
       "cssgCfgRadiusFwdAcctPktsEnabled": cssgCfgRadiusFwdAcctPktsEnabled,
       "cssgCfgAccountingInterval": cssgCfgAccountingInterval,
       "cssgCfgTCPRedirGrpForUnAuthUsers": cssgCfgTCPRedirGrpForUnAuthUsers,
       "cssgCfgTCPRedirGrpForUnAuthServ": cssgCfgTCPRedirGrpForUnAuthServ,
       "cssgCfgTcpRedirGrpForSMTP": cssgCfgTcpRedirGrpForSMTP,
       "cssgCfgTcpRedirGrpForInitialCapt": cssgCfgTcpRedirGrpForInitialCapt,
       "cssgCfgTcpRedirGrpForAdvCapt": cssgCfgTcpRedirGrpForAdvCapt,
       "cssgCfgRadiusClntRbtNotifEnabled": cssgCfgRadiusClntRbtNotifEnabled,
       "cssgCfgAAAServerDownNotifEnabled": cssgCfgAAAServerDownNotifEnabled,
       "cssgCfgTalEnabled": cssgCfgTalEnabled,
       "cssgStatsObjects": cssgStatsObjects,
       "cssgStatsLoginAttempts": cssgStatsLoginAttempts,
       "cssgStatsLoginsSuccessful": cssgStatsLoginsSuccessful,
       "cssgStatsActiveSessions": cssgStatsActiveSessions,
       "cssgStatsActiveHosts": cssgStatsActiveHosts,
       "cssgStatsActiveServices": cssgStatsActiveServices,
       "cssgStatsPODs": cssgStatsPODs,
       "cssgService": cssgService,
       "cssgServiceTable": cssgServiceTable,
       "cssgServiceEntry": cssgServiceEntry,
       "cssgServiceName": cssgServiceName,
       "cssgServiceMode": cssgServiceMode,
       "cssgServiceType": cssgServiceType,
       "cssgServiceIdleTimeout": cssgServiceIdleTimeout,
       "cssgServiceSessionTimeout": cssgServiceSessionTimeout,
       "cssgServiceActiveSessions": cssgServiceActiveSessions,
       "cssgServiceDNSPrimaryIpType": cssgServiceDNSPrimaryIpType,
       "cssgServiceDNSPrimary": cssgServiceDNSPrimary,
       "cssgServiceDNSSecondaryIpType": cssgServiceDNSSecondaryIpType,
       "cssgServiceDNSSecondary": cssgServiceDNSSecondary,
       "cssgServiceUpstreamQOSEnabled": cssgServiceUpstreamQOSEnabled,
       "cssgServiceDownStreamQOSEnabled": cssgServiceDownStreamQOSEnabled,
       "cssgServiceOpenGarden": cssgServiceOpenGarden,
       "cssgServicePrepaid": cssgServicePrepaid,
       "cssgServiceRouteTable": cssgServiceRouteTable,
       "cssgServiceRouteEntry": cssgServiceRouteEntry,
       "cssgServiceRouteType": cssgServiceRouteType,
       "cssgServiceRouteAddr": cssgServiceRouteAddr,
       "cssgServiceRouteMaskType": cssgServiceRouteMaskType,
       "cssgServiceRouteMask": cssgServiceRouteMask,
       "cssgServiceRoutePermission": cssgServiceRoutePermission,
       "cssgExcludedAPN": cssgExcludedAPN,
       "cssgExcludedAPNTable": cssgExcludedAPNTable,
       "cssgExcludedAPNEntry": cssgExcludedAPNEntry,
       "cssgExcludedAPNName": cssgExcludedAPNName,
       "cssgExcludedAPNRowStatus": cssgExcludedAPNRowStatus,
       "cssgExcludedDomain": cssgExcludedDomain,
       "cssgExcludedDomainTable": cssgExcludedDomainTable,
       "cssgExcludedDomainEntry": cssgExcludedDomainEntry,
       "cssgExcludedDomainName": cssgExcludedDomainName,
       "cssgExcludedDomainRowStatus": cssgExcludedDomainRowStatus,
       "cssgTcpRedirect": cssgTcpRedirect,
       "cssgTcpRedirectGrpTable": cssgTcpRedirectGrpTable,
       "cssgTcpRedirectGrpEntry": cssgTcpRedirectGrpEntry,
       "cssgTcpRedirectGrpName": cssgTcpRedirectGrpName,
       "cssgTcpRedirectGrpServerAddrType": cssgTcpRedirectGrpServerAddrType,
       "cssgTcpRedirectGrpServerAddr": cssgTcpRedirectGrpServerAddr,
       "cssgTcpRedirectGrpServerPort": cssgTcpRedirectGrpServerPort,
       "cssgTcpRedirectGrpRowStatus": cssgTcpRedirectGrpRowStatus,
       "cssgNetworkGrpTable": cssgNetworkGrpTable,
       "cssgNetworkGrpEntry": cssgNetworkGrpEntry,
       "cssgNetworkGrpName": cssgNetworkGrpName,
       "cssgNetworkGrpNetIpType": cssgNetworkGrpNetIpType,
       "cssgNetworkGrpNetIpAddr": cssgNetworkGrpNetIpAddr,
       "cssgNetworkGrpNetMaskType": cssgNetworkGrpNetMaskType,
       "cssgNetworkGrpNetMask": cssgNetworkGrpNetMask,
       "cssgNetworkGrpNetRowStatus": cssgNetworkGrpNetRowStatus,
       "cssgPortGrpTable": cssgPortGrpTable,
       "cssgPortGrpEntry": cssgPortGrpEntry,
       "cssgPortGrpName": cssgPortGrpName,
       "cssgPortGrpPortNo": cssgPortGrpPortNo,
       "cssgPortGrpPortRowStatus": cssgPortGrpPortRowStatus,
       "cssgTcpRedirNetworkGrpMapTable": cssgTcpRedirNetworkGrpMapTable,
       "cssgTcpRedirNetworkGrpMapEntry": cssgTcpRedirNetworkGrpMapEntry,
       "cssgTcpRedirNetworkMapGrpName": cssgTcpRedirNetworkMapGrpName,
       "cssgTcpRedirNetworkGrpMapRowStat": cssgTcpRedirNetworkGrpMapRowStat,
       "cssgTcpRedirPortGrpMapTable": cssgTcpRedirPortGrpMapTable,
       "cssgTcpRedirPortGrpMapEntry": cssgTcpRedirPortGrpMapEntry,
       "cssgTcpRedirPortMapGrpName": cssgTcpRedirPortMapGrpName,
       "cssgTcpRedirPortGrpMapRowStat": cssgTcpRedirPortGrpMapRowStat,
       "cssgTcpRedirPortNoMapTable": cssgTcpRedirPortNoMapTable,
       "cssgTcpRedirPortNoMapEntry": cssgTcpRedirPortNoMapEntry,
       "cssgTcpRedirPortNo": cssgTcpRedirPortNo,
       "cssgTcpRedirPortNoMapRowStat": cssgTcpRedirPortNoMapRowStat,
       "cssgServiceIfBinds": cssgServiceIfBinds,
       "cssgServiceIfBindTable": cssgServiceIfBindTable,
       "cssgServiceIfBindEntry": cssgServiceIfBindEntry,
       "cssgServiceIfIndex": cssgServiceIfIndex,
       "cssgServiceIfRowStatus": cssgServiceIfRowStatus,
       "cssgRadiusClients": cssgRadiusClients,
       "cssgRadiusClientTable": cssgRadiusClientTable,
       "cssgRadiusClientEntry": cssgRadiusClientEntry,
       "cssgRadiusClientAddrType": cssgRadiusClientAddrType,
       "cssgRadiusClientAddr": cssgRadiusClientAddr,
       "cssgRadiusClientRowStatus": cssgRadiusClientRowStatus,
       "cssgPortMap": cssgPortMap,
       "cssgPortMapLength": cssgPortMapLength,
       "cssgPortMapTable": cssgPortMapTable,
       "cssgPortMapEntry": cssgPortMapEntry,
       "cssgPortMapSourceIpType": cssgPortMapSourceIpType,
       "cssgPortMapSourceIp": cssgPortMapSourceIp,
       "cssgPortMapPortRangeFrom": cssgPortMapPortRangeFrom,
       "cssgPortMapPortRangeTo": cssgPortMapPortRangeTo,
       "cssgPortMapRowStatus": cssgPortMapRowStatus,
       "cssgTal": cssgTal,
       "cssgTalWaitingForAuthUsers": cssgTalWaitingForAuthUsers,
       "cssgTalUnidentifiedUsers": cssgTalUnidentifiedUsers,
       "cssgTalSuspectUsers": cssgTalSuspectUsers,
       "cssgTalPassthroughUsers": cssgTalPassthroughUsers,
       "cssgTalMaxAuthRate": cssgTalMaxAuthRate,
       "cssgTalMaxAuthRateTimestamp": cssgTalMaxAuthRateTimestamp,
       "cssgTalMinAuthRate": cssgTalMinAuthRate,
       "cssgTalMinAuthRateTimestamp": cssgTalMinAuthRateTimestamp,
       "cssgTalCurrentAuthRate": cssgTalCurrentAuthRate,
       "cssgTalCurrentAuthRateTimestamp": cssgTalCurrentAuthRateTimestamp,
       "cssgTalResetAuthRates": cssgTalResetAuthRates,
       "cssgTalMaxPendingAuthReqs": cssgTalMaxPendingAuthReqs,
       "cssgTalMaxAuthReqsRate": cssgTalMaxAuthReqsRate,
       "cssgTalDropPakDuringAuthorization": cssgTalDropPakDuringAuthorization,
       "cssgTalUnidentifiedUserAllowTraff": cssgTalUnidentifiedUserAllowTraff,
       "cssgTalMaxSuspectUsers": cssgTalMaxSuspectUsers,
       "cssgTalSuspectUserTimeout": cssgTalSuspectUserTimeout,
       "cssgTalUnidentifiedUserTimeout": cssgTalUnidentifiedUserTimeout,
       "cssgTalUserInfoTable": cssgTalUserInfoTable,
       "cssgTalUserInfoEntry": cssgTalUserInfoEntry,
       "cssgTalUserIPAddressType": cssgTalUserIPAddressType,
       "cssgTalUserIPAddress": cssgTalUserIPAddress,
       "cssgTalUserState": cssgTalUserState,
       "ciscoSsgMIBConformance": ciscoSsgMIBConformance,
       "ciscoSsgMIBCompliances": ciscoSsgMIBCompliances,
       "ciscoSsgMIBCompliance": ciscoSsgMIBCompliance,
       "ciscoSsgMIBComplianceRev1": ciscoSsgMIBComplianceRev1,
       "ciscoSsgMIBGroups": ciscoSsgMIBGroups,
       "ciscoSsgCfgGroup": ciscoSsgCfgGroup,
       "ciscoSsgStatsGroup": ciscoSsgStatsGroup,
       "ciscoSsgServicesGroup": ciscoSsgServicesGroup,
       "ciscoSsgExclusionsGroup": ciscoSsgExclusionsGroup,
       "ciscoSsgTcpRedirectGroup": ciscoSsgTcpRedirectGroup,
       "ciscoSsgServiceInterfaceGroup": ciscoSsgServiceInterfaceGroup,
       "ciscoSsgRadiusClientsGroup": ciscoSsgRadiusClientsGroup,
       "ciscoSsgPortMapGroup": ciscoSsgPortMapGroup,
       "ciscoSsgNotificationGroup": ciscoSsgNotificationGroup,
       "ciscoSsgCfgGroupRev1": ciscoSsgCfgGroupRev1,
       "ciscoSsgTalUserInfoGroup": ciscoSsgTalUserInfoGroup}
)

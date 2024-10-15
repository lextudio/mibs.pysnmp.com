# SNMP MIB module (KENYA-NMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/KENYA-NMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:40 2024
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(vlbProducts,) = mibBuilder.importSymbols(
    "VOLUBILL-ROOT-MIB",
    "vlbProducts")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bay_ObjectIdentity = ObjectIdentity
bay = _Bay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1)
)


class _BayConsolidatedStatus_Type(Integer32):
    """Custom type bayConsolidatedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUnmanaged", 0),
          ("green", 1),
          ("orange", 3),
          ("red", 4),
          ("yellow", 2))
    )


_BayConsolidatedStatus_Type.__name__ = "Integer32"
_BayConsolidatedStatus_Object = MibScalar
bayConsolidatedStatus = _BayConsolidatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 1),
    _BayConsolidatedStatus_Type()
)
bayConsolidatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayConsolidatedStatus.setStatus("mandatory")
_BayHardwares_ObjectIdentity = ObjectIdentity
bayHardwares = _BayHardwares_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 2)
)
_BayHwCount_Type = Integer32
_BayHwCount_Object = MibScalar
bayHwCount = _BayHwCount_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 2, 1),
    _BayHwCount_Type()
)
bayHwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayHwCount.setStatus("mandatory")
_BayHwTable_Object = MibTable
bayHwTable = _BayHwTable_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    bayHwTable.setStatus("current")
_BayHwEntry_Object = MibTableRow
bayHwEntry = _BayHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 2, 2, 1)
)
bayHwEntry.setIndexNames(
    (0, "KENYA-NMS-MIB", "bayHwIndex"),
)
if mibBuilder.loadTexts:
    bayHwEntry.setStatus("current")


class _BayHwIndex_Type(Integer32):
    """Custom type bayHwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BayHwIndex_Type.__name__ = "Integer32"
_BayHwIndex_Object = MibTableColumn
bayHwIndex = _BayHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 2, 2, 1, 1),
    _BayHwIndex_Type()
)
bayHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayHwIndex.setStatus("current")


class _BayHwName_Type(OctetString):
    """Custom type bayHwName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BayHwName_Type.__name__ = "OctetString"
_BayHwName_Object = MibTableColumn
bayHwName = _BayHwName_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 2, 2, 1, 2),
    _BayHwName_Type()
)
bayHwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayHwName.setStatus("current")
_BayHwAddress_Type = IpAddress
_BayHwAddress_Object = MibTableColumn
bayHwAddress = _BayHwAddress_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 2, 2, 1, 3),
    _BayHwAddress_Type()
)
bayHwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayHwAddress.setStatus("current")
_BayApplications_ObjectIdentity = ObjectIdentity
bayApplications = _BayApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3)
)
_BayProxy_ObjectIdentity = ObjectIdentity
bayProxy = _BayProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 1)
)


class _BayProxyGlobalStatus_Type(Integer32):
    """Custom type bayProxyGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUnmanaged", 0),
          ("green", 1),
          ("orange", 3),
          ("red", 4),
          ("yellow", 2))
    )


_BayProxyGlobalStatus_Type.__name__ = "Integer32"
_BayProxyGlobalStatus_Object = MibScalar
bayProxyGlobalStatus = _BayProxyGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 1, 1),
    _BayProxyGlobalStatus_Type()
)
bayProxyGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayProxyGlobalStatus.setStatus("mandatory")


class _ProxyHTTPGroupStatus_Type(Integer32):
    """Custom type proxyHTTPGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUnmanaged", 0),
          ("green", 1),
          ("orange", 3),
          ("red", 4),
          ("yellow", 2))
    )


_ProxyHTTPGroupStatus_Type.__name__ = "Integer32"
_ProxyHTTPGroupStatus_Object = MibScalar
proxyHTTPGroupStatus = _ProxyHTTPGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 1, 2),
    _ProxyHTTPGroupStatus_Type()
)
proxyHTTPGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyHTTPGroupStatus.setStatus("mandatory")


class _ProxySSNGroupStatus_Type(Integer32):
    """Custom type proxySSNGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUnmanaged", 0),
          ("green", 1),
          ("orange", 3),
          ("red", 4),
          ("yellow", 2))
    )


_ProxySSNGroupStatus_Type.__name__ = "Integer32"
_ProxySSNGroupStatus_Object = MibScalar
proxySSNGroupStatus = _ProxySSNGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 1, 3),
    _ProxySSNGroupStatus_Type()
)
proxySSNGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxySSNGroupStatus.setStatus("mandatory")


class _ProxyMMSGroupStatus_Type(Integer32):
    """Custom type proxyMMSGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUnmanaged", 0),
          ("green", 1),
          ("orange", 3),
          ("red", 4),
          ("yellow", 2))
    )


_ProxyMMSGroupStatus_Type.__name__ = "Integer32"
_ProxyMMSGroupStatus_Object = MibScalar
proxyMMSGroupStatus = _ProxyMMSGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 1, 4),
    _ProxyMMSGroupStatus_Type()
)
proxyMMSGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyMMSGroupStatus.setStatus("mandatory")


class _ProxyMAILGroupStatus_Type(Integer32):
    """Custom type proxyMAILGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUnmanaged", 0),
          ("green", 1),
          ("orange", 3),
          ("red", 4),
          ("yellow", 2))
    )


_ProxyMAILGroupStatus_Type.__name__ = "Integer32"
_ProxyMAILGroupStatus_Object = MibScalar
proxyMAILGroupStatus = _ProxyMAILGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 1, 5),
    _ProxyMAILGroupStatus_Type()
)
proxyMAILGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyMAILGroupStatus.setStatus("mandatory")
_BayBilling_ObjectIdentity = ObjectIdentity
bayBilling = _BayBilling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 2)
)


class _BayBillingGlobalStatus_Type(Integer32):
    """Custom type bayBillingGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUnmanaged", 0),
          ("green", 1),
          ("orange", 3),
          ("red", 4),
          ("yellow", 2))
    )


_BayBillingGlobalStatus_Type.__name__ = "Integer32"
_BayBillingGlobalStatus_Object = MibScalar
bayBillingGlobalStatus = _BayBillingGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 2, 1),
    _BayBillingGlobalStatus_Type()
)
bayBillingGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayBillingGlobalStatus.setStatus("mandatory")
_BaySwitching_ObjectIdentity = ObjectIdentity
baySwitching = _BaySwitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 3)
)


class _BayL7SwitchingGlobalStatus_Type(Integer32):
    """Custom type bayL7SwitchingGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUnmanaged", 0),
          ("green", 1),
          ("orange", 3),
          ("red", 4),
          ("yellow", 2))
    )


_BayL7SwitchingGlobalStatus_Type.__name__ = "Integer32"
_BayL7SwitchingGlobalStatus_Object = MibScalar
bayL7SwitchingGlobalStatus = _BayL7SwitchingGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 3, 1),
    _BayL7SwitchingGlobalStatus_Type()
)
bayL7SwitchingGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayL7SwitchingGlobalStatus.setStatus("mandatory")


class _BayL2SwitchingGlobalStatus_Type(Integer32):
    """Custom type bayL2SwitchingGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUnmanaged", 0),
          ("green", 1),
          ("orange", 3),
          ("red", 4),
          ("yellow", 2))
    )


_BayL2SwitchingGlobalStatus_Type.__name__ = "Integer32"
_BayL2SwitchingGlobalStatus_Object = MibScalar
bayL2SwitchingGlobalStatus = _BayL2SwitchingGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 3, 2),
    _BayL2SwitchingGlobalStatus_Type()
)
bayL2SwitchingGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayL2SwitchingGlobalStatus.setStatus("mandatory")
_BayLms_ObjectIdentity = ObjectIdentity
bayLms = _BayLms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 4)
)


class _BayLmsGlobalStatus_Type(Integer32):
    """Custom type bayLmsGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUnmanaged", 0),
          ("green", 1),
          ("orange", 3),
          ("red", 4),
          ("yellow", 2))
    )


_BayLmsGlobalStatus_Type.__name__ = "Integer32"
_BayLmsGlobalStatus_Object = MibScalar
bayLmsGlobalStatus = _BayLmsGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 4, 1),
    _BayLmsGlobalStatus_Type()
)
bayLmsGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayLmsGlobalStatus.setStatus("mandatory")
_BayScstats_ObjectIdentity = ObjectIdentity
bayScstats = _BayScstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5)
)
_BscInAgentReportRequests_Type = Integer32
_BscInAgentReportRequests_Object = MibScalar
bscInAgentReportRequests = _BscInAgentReportRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 1),
    _BscInAgentReportRequests_Type()
)
bscInAgentReportRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInAgentReportRequests.setStatus("mandatory")
_BscOutUpdateSessionReplies_Type = Integer32
_BscOutUpdateSessionReplies_Object = MibScalar
bscOutUpdateSessionReplies = _BscOutUpdateSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 2),
    _BscOutUpdateSessionReplies_Type()
)
bscOutUpdateSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutUpdateSessionReplies.setStatus("mandatory")
_BscOutReplies_Type = Integer32
_BscOutReplies_Object = MibScalar
bscOutReplies = _BscOutReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 3),
    _BscOutReplies_Type()
)
bscOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutReplies.setStatus("mandatory")
_BscCurrentServicesPendingSessions_Type = Integer32
_BscCurrentServicesPendingSessions_Object = MibScalar
bscCurrentServicesPendingSessions = _BscCurrentServicesPendingSessions_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 4),
    _BscCurrentServicesPendingSessions_Type()
)
bscCurrentServicesPendingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCurrentServicesPendingSessions.setStatus("mandatory")
_BscUdrs_Type = Integer32
_BscUdrs_Object = MibScalar
bscUdrs = _BscUdrs_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 5),
    _BscUdrs_Type()
)
bscUdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscUdrs.setStatus("mandatory")
_BscInReportUsageReplies_Type = Integer32
_BscInReportUsageReplies_Object = MibScalar
bscInReportUsageReplies = _BscInReportUsageReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 6),
    _BscInReportUsageReplies_Type()
)
bscInReportUsageReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInReportUsageReplies.setStatus("mandatory")
_BscClosedSessions_Type = Integer32
_BscClosedSessions_Object = MibScalar
bscClosedSessions = _BscClosedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 7),
    _BscClosedSessions_Type()
)
bscClosedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscClosedSessions.setStatus("mandatory")
_BscOldServicesPendingSessions_Type = Integer32
_BscOldServicesPendingSessions_Object = MibScalar
bscOldServicesPendingSessions = _BscOldServicesPendingSessions_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 8),
    _BscOldServicesPendingSessions_Type()
)
bscOldServicesPendingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOldServicesPendingSessions.setStatus("mandatory")
_BscInRequests_Type = Integer32
_BscInRequests_Object = MibScalar
bscInRequests = _BscInRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 9),
    _BscInRequests_Type()
)
bscInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInRequests.setStatus("mandatory")
_BscOutAgentReportReplies_Type = Integer32
_BscOutAgentReportReplies_Object = MibScalar
bscOutAgentReportReplies = _BscOutAgentReportReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 10),
    _BscOutAgentReportReplies_Type()
)
bscOutAgentReportReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutAgentReportReplies.setStatus("mandatory")
_BscInCloseSessionReplies_Type = Integer32
_BscInCloseSessionReplies_Object = MibScalar
bscInCloseSessionReplies = _BscInCloseSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 11),
    _BscInCloseSessionReplies_Type()
)
bscInCloseSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInCloseSessionReplies.setStatus("mandatory")
_BscInCloseSessionRequests_Type = Integer32
_BscInCloseSessionRequests_Object = MibScalar
bscInCloseSessionRequests = _BscInCloseSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 12),
    _BscInCloseSessionRequests_Type()
)
bscInCloseSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInCloseSessionRequests.setStatus("mandatory")
_BscOutCloseSessionReplies_Type = Integer32
_BscOutCloseSessionReplies_Object = MibScalar
bscOutCloseSessionReplies = _BscOutCloseSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 13),
    _BscOutCloseSessionReplies_Type()
)
bscOutCloseSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutCloseSessionReplies.setStatus("mandatory")
_BscUdrFiles_Type = Integer32
_BscUdrFiles_Object = MibScalar
bscUdrFiles = _BscUdrFiles_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 14),
    _BscUdrFiles_Type()
)
bscUdrFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscUdrFiles.setStatus("mandatory")
_BscOutListSessionReplies_Type = Integer32
_BscOutListSessionReplies_Object = MibScalar
bscOutListSessionReplies = _BscOutListSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 15),
    _BscOutListSessionReplies_Type()
)
bscOutListSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutListSessionReplies.setStatus("mandatory")
_BscOutRequests_Type = Integer32
_BscOutRequests_Object = MibScalar
bscOutRequests = _BscOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 16),
    _BscOutRequests_Type()
)
bscOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutRequests.setStatus("mandatory")
_BscOutUpdateSessionRequests_Type = Integer32
_BscOutUpdateSessionRequests_Object = MibScalar
bscOutUpdateSessionRequests = _BscOutUpdateSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 17),
    _BscOutUpdateSessionRequests_Type()
)
bscOutUpdateSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutUpdateSessionRequests.setStatus("mandatory")
_BscInUpdateSessionReplies_Type = Integer32
_BscInUpdateSessionReplies_Object = MibScalar
bscInUpdateSessionReplies = _BscInUpdateSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 18),
    _BscInUpdateSessionReplies_Type()
)
bscInUpdateSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInUpdateSessionReplies.setStatus("mandatory")
_BscInAgentReportReplies_Type = Integer32
_BscInAgentReportReplies_Object = MibScalar
bscInAgentReportReplies = _BscInAgentReportReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 19),
    _BscInAgentReportReplies_Type()
)
bscInAgentReportReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInAgentReportReplies.setStatus("mandatory")
_BscOutAgentReportRequests_Type = Integer32
_BscOutAgentReportRequests_Object = MibScalar
bscOutAgentReportRequests = _BscOutAgentReportRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 20),
    _BscOutAgentReportRequests_Type()
)
bscOutAgentReportRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutAgentReportRequests.setStatus("mandatory")
_BscInUpdateSessionRequests_Type = Integer32
_BscInUpdateSessionRequests_Object = MibScalar
bscInUpdateSessionRequests = _BscInUpdateSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 21),
    _BscInUpdateSessionRequests_Type()
)
bscInUpdateSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInUpdateSessionRequests.setStatus("mandatory")
_BscInReplies_Type = Integer32
_BscInReplies_Object = MibScalar
bscInReplies = _BscInReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 22),
    _BscInReplies_Type()
)
bscInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInReplies.setStatus("mandatory")
_BscOutCreateSessionRequests_Type = Integer32
_BscOutCreateSessionRequests_Object = MibScalar
bscOutCreateSessionRequests = _BscOutCreateSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 23),
    _BscOutCreateSessionRequests_Type()
)
bscOutCreateSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutCreateSessionRequests.setStatus("mandatory")
_BscInReportUsageRequests_Type = Integer32
_BscInReportUsageRequests_Object = MibScalar
bscInReportUsageRequests = _BscInReportUsageRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 24),
    _BscInReportUsageRequests_Type()
)
bscInReportUsageRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInReportUsageRequests.setStatus("mandatory")
_BscInListSessionRequests_Type = Integer32
_BscInListSessionRequests_Object = MibScalar
bscInListSessionRequests = _BscInListSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 25),
    _BscInListSessionRequests_Type()
)
bscInListSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInListSessionRequests.setStatus("mandatory")
_BscOutReportUsageRequests_Type = Integer32
_BscOutReportUsageRequests_Object = MibScalar
bscOutReportUsageRequests = _BscOutReportUsageRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 26),
    _BscOutReportUsageRequests_Type()
)
bscOutReportUsageRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutReportUsageRequests.setStatus("mandatory")
_BscInListSessionReplies_Type = Integer32
_BscInListSessionReplies_Object = MibScalar
bscInListSessionReplies = _BscInListSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 27),
    _BscInListSessionReplies_Type()
)
bscInListSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInListSessionReplies.setStatus("mandatory")
_BscInCreateSessionRequests_Type = Integer32
_BscInCreateSessionRequests_Object = MibScalar
bscInCreateSessionRequests = _BscInCreateSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 28),
    _BscInCreateSessionRequests_Type()
)
bscInCreateSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInCreateSessionRequests.setStatus("mandatory")
_BscOutCloseSessionRequests_Type = Integer32
_BscOutCloseSessionRequests_Object = MibScalar
bscOutCloseSessionRequests = _BscOutCloseSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 29),
    _BscOutCloseSessionRequests_Type()
)
bscOutCloseSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutCloseSessionRequests.setStatus("mandatory")
_BscOutListSessionRequests_Type = Integer32
_BscOutListSessionRequests_Object = MibScalar
bscOutListSessionRequests = _BscOutListSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 30),
    _BscOutListSessionRequests_Type()
)
bscOutListSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutListSessionRequests.setStatus("mandatory")
_BscInCreateSessionReplies_Type = Integer32
_BscInCreateSessionReplies_Object = MibScalar
bscInCreateSessionReplies = _BscInCreateSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 31),
    _BscInCreateSessionReplies_Type()
)
bscInCreateSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInCreateSessionReplies.setStatus("mandatory")
_BscCreatedSessions_Type = Integer32
_BscCreatedSessions_Object = MibScalar
bscCreatedSessions = _BscCreatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 32),
    _BscCreatedSessions_Type()
)
bscCreatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCreatedSessions.setStatus("mandatory")
_BscOutReportUsageReplies_Type = Integer32
_BscOutReportUsageReplies_Object = MibScalar
bscOutReportUsageReplies = _BscOutReportUsageReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 33),
    _BscOutReportUsageReplies_Type()
)
bscOutReportUsageReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutReportUsageReplies.setStatus("mandatory")
_BscOutCreateSessionReplies_Type = Integer32
_BscOutCreateSessionReplies_Object = MibScalar
bscOutCreateSessionReplies = _BscOutCreateSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 34),
    _BscOutCreateSessionReplies_Type()
)
bscOutCreateSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutCreateSessionReplies.setStatus("mandatory")
_BscSessionsPerSecond_Type = Integer32
_BscSessionsPerSecond_Object = MibScalar
bscSessionsPerSecond = _BscSessionsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 35),
    _BscSessionsPerSecond_Type()
)
bscSessionsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscSessionsPerSecond.setStatus("mandatory")
_BscRejectedSessions_Type = Integer32
_BscRejectedSessions_Object = MibScalar
bscRejectedSessions = _BscRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 36),
    _BscRejectedSessions_Type()
)
bscRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscRejectedSessions.setStatus("mandatory")
_BscInContinueSessionRequest_Type = Integer32
_BscInContinueSessionRequest_Object = MibScalar
bscInContinueSessionRequest = _BscInContinueSessionRequest_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 37),
    _BscInContinueSessionRequest_Type()
)
bscInContinueSessionRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInContinueSessionRequest.setStatus("mandatory")
_BscOutContinueSessionRequest_Type = Integer32
_BscOutContinueSessionRequest_Object = MibScalar
bscOutContinueSessionRequest = _BscOutContinueSessionRequest_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 38),
    _BscOutContinueSessionRequest_Type()
)
bscOutContinueSessionRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutContinueSessionRequest.setStatus("mandatory")
_BscInContinueSessionReplies_Type = Integer32
_BscInContinueSessionReplies_Object = MibScalar
bscInContinueSessionReplies = _BscInContinueSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 39),
    _BscInContinueSessionReplies_Type()
)
bscInContinueSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscInContinueSessionReplies.setStatus("mandatory")
_BscOutContinueSessionReplies_Type = Integer32
_BscOutContinueSessionReplies_Object = MibScalar
bscOutContinueSessionReplies = _BscOutContinueSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 40),
    _BscOutContinueSessionReplies_Type()
)
bscOutContinueSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscOutContinueSessionReplies.setStatus("mandatory")
_BscAuthRequests_Type = Integer32
_BscAuthRequests_Object = MibScalar
bscAuthRequests = _BscAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 41),
    _BscAuthRequests_Type()
)
bscAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscAuthRequests.setStatus("mandatory")
_BscAuthNonRepliedRequestsPercent_Type = Integer32
_BscAuthNonRepliedRequestsPercent_Object = MibScalar
bscAuthNonRepliedRequestsPercent = _BscAuthNonRepliedRequestsPercent_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 42),
    _BscAuthNonRepliedRequestsPercent_Type()
)
bscAuthNonRepliedRequestsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscAuthNonRepliedRequestsPercent.setStatus("mandatory")
_BscAuthReplies_Type = Integer32
_BscAuthReplies_Object = MibScalar
bscAuthReplies = _BscAuthReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 43),
    _BscAuthReplies_Type()
)
bscAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscAuthReplies.setStatus("mandatory")
_BscAcctReplies_Type = Integer32
_BscAcctReplies_Object = MibScalar
bscAcctReplies = _BscAcctReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 44),
    _BscAcctReplies_Type()
)
bscAcctReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscAcctReplies.setStatus("mandatory")
_BscAcctRequests_Type = Integer32
_BscAcctRequests_Object = MibScalar
bscAcctRequests = _BscAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 45),
    _BscAcctRequests_Type()
)
bscAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscAcctRequests.setStatus("mandatory")
_BscAcctRepliedRequestsPercent_Type = Integer32
_BscAcctRepliedRequestsPercent_Object = MibScalar
bscAcctRepliedRequestsPercent = _BscAcctRepliedRequestsPercent_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 3, 5, 46),
    _BscAcctRepliedRequestsPercent_Type()
)
bscAcctRepliedRequestsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscAcctRepliedRequestsPercent.setStatus("mandatory")
_BayTraps_ObjectIdentity = ObjectIdentity
bayTraps = _BayTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 4)
)


class _BayExternalTrapTarget_Type(OctetString):
    """Custom type bayExternalTrapTarget based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BayExternalTrapTarget_Type.__name__ = "OctetString"
_BayExternalTrapTarget_Object = MibScalar
bayExternalTrapTarget = _BayExternalTrapTarget_Object(
    (1, 3, 6, 1, 4, 1, 9905, 1, 1, 4, 1),
    _BayExternalTrapTarget_Type()
)
bayExternalTrapTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bayExternalTrapTarget.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KENYA-NMS-MIB",
    **{"bay": bay,
       "bayConsolidatedStatus": bayConsolidatedStatus,
       "bayHardwares": bayHardwares,
       "bayHwCount": bayHwCount,
       "bayHwTable": bayHwTable,
       "bayHwEntry": bayHwEntry,
       "bayHwIndex": bayHwIndex,
       "bayHwName": bayHwName,
       "bayHwAddress": bayHwAddress,
       "bayApplications": bayApplications,
       "bayProxy": bayProxy,
       "bayProxyGlobalStatus": bayProxyGlobalStatus,
       "proxyHTTPGroupStatus": proxyHTTPGroupStatus,
       "proxySSNGroupStatus": proxySSNGroupStatus,
       "proxyMMSGroupStatus": proxyMMSGroupStatus,
       "proxyMAILGroupStatus": proxyMAILGroupStatus,
       "bayBilling": bayBilling,
       "bayBillingGlobalStatus": bayBillingGlobalStatus,
       "baySwitching": baySwitching,
       "bayL7SwitchingGlobalStatus": bayL7SwitchingGlobalStatus,
       "bayL2SwitchingGlobalStatus": bayL2SwitchingGlobalStatus,
       "bayLms": bayLms,
       "bayLmsGlobalStatus": bayLmsGlobalStatus,
       "bayScstats": bayScstats,
       "bscInAgentReportRequests": bscInAgentReportRequests,
       "bscOutUpdateSessionReplies": bscOutUpdateSessionReplies,
       "bscOutReplies": bscOutReplies,
       "bscCurrentServicesPendingSessions": bscCurrentServicesPendingSessions,
       "bscUdrs": bscUdrs,
       "bscInReportUsageReplies": bscInReportUsageReplies,
       "bscClosedSessions": bscClosedSessions,
       "bscOldServicesPendingSessions": bscOldServicesPendingSessions,
       "bscInRequests": bscInRequests,
       "bscOutAgentReportReplies": bscOutAgentReportReplies,
       "bscInCloseSessionReplies": bscInCloseSessionReplies,
       "bscInCloseSessionRequests": bscInCloseSessionRequests,
       "bscOutCloseSessionReplies": bscOutCloseSessionReplies,
       "bscUdrFiles": bscUdrFiles,
       "bscOutListSessionReplies": bscOutListSessionReplies,
       "bscOutRequests": bscOutRequests,
       "bscOutUpdateSessionRequests": bscOutUpdateSessionRequests,
       "bscInUpdateSessionReplies": bscInUpdateSessionReplies,
       "bscInAgentReportReplies": bscInAgentReportReplies,
       "bscOutAgentReportRequests": bscOutAgentReportRequests,
       "bscInUpdateSessionRequests": bscInUpdateSessionRequests,
       "bscInReplies": bscInReplies,
       "bscOutCreateSessionRequests": bscOutCreateSessionRequests,
       "bscInReportUsageRequests": bscInReportUsageRequests,
       "bscInListSessionRequests": bscInListSessionRequests,
       "bscOutReportUsageRequests": bscOutReportUsageRequests,
       "bscInListSessionReplies": bscInListSessionReplies,
       "bscInCreateSessionRequests": bscInCreateSessionRequests,
       "bscOutCloseSessionRequests": bscOutCloseSessionRequests,
       "bscOutListSessionRequests": bscOutListSessionRequests,
       "bscInCreateSessionReplies": bscInCreateSessionReplies,
       "bscCreatedSessions": bscCreatedSessions,
       "bscOutReportUsageReplies": bscOutReportUsageReplies,
       "bscOutCreateSessionReplies": bscOutCreateSessionReplies,
       "bscSessionsPerSecond": bscSessionsPerSecond,
       "bscRejectedSessions": bscRejectedSessions,
       "bscInContinueSessionRequest": bscInContinueSessionRequest,
       "bscOutContinueSessionRequest": bscOutContinueSessionRequest,
       "bscInContinueSessionReplies": bscInContinueSessionReplies,
       "bscOutContinueSessionReplies": bscOutContinueSessionReplies,
       "bscAuthRequests": bscAuthRequests,
       "bscAuthNonRepliedRequestsPercent": bscAuthNonRepliedRequestsPercent,
       "bscAuthReplies": bscAuthReplies,
       "bscAcctReplies": bscAcctReplies,
       "bscAcctRequests": bscAcctRequests,
       "bscAcctRepliedRequestsPercent": bscAcctRepliedRequestsPercent,
       "bayTraps": bayTraps,
       "bayExternalTrapTarget": bayExternalTrapTarget}
)

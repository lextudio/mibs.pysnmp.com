# SNMP MIB module (KENYA-COMPONENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/KENYA-COMPONENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:39 2024
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

(vlbComponents,) = mibBuilder.importSymbols(
    "VOLUBILL-ROOT-MIB",
    "vlbComponents")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BayServer_ObjectIdentity = ObjectIdentity
bayServer = _BayServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1)
)
_IsLms_Type = Integer32
_IsLms_Object = MibScalar
isLms = _IsLms_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 1),
    _IsLms_Type()
)
isLms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isLms.setStatus("mandatory")
_IsProxy_Type = Integer32
_IsProxy_Object = MibScalar
isProxy = _IsProxy_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 2),
    _IsProxy_Type()
)
isProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isProxy.setStatus("mandatory")
_IsBilling_Type = Integer32
_IsBilling_Object = MibScalar
isBilling = _IsBilling_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 3),
    _IsBilling_Type()
)
isBilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isBilling.setStatus("mandatory")
_LmsUnit_ObjectIdentity = ObjectIdentity
lmsUnit = _LmsUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 4)
)


class _LmsUnitGlobalStatus_Type(Integer32):
    """Custom type lmsUnitGlobalStatus based on Integer32"""
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
        *(("green", 1),
          ("orange", 3),
          ("red", 4),
          ("unmanaged", 0),
          ("yellow", 2))
    )


_LmsUnitGlobalStatus_Type.__name__ = "Integer32"
_LmsUnitGlobalStatus_Object = MibScalar
lmsUnitGlobalStatus = _LmsUnitGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 4, 1),
    _LmsUnitGlobalStatus_Type()
)
lmsUnitGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmsUnitGlobalStatus.setStatus("mandatory")


class _LmsUnitActivation_Type(Integer32):
    """Custom type lmsUnitActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setonly", 2),
          ("start", 1),
          ("stop", 0))
    )


_LmsUnitActivation_Type.__name__ = "Integer32"
_LmsUnitActivation_Object = MibScalar
lmsUnitActivation = _LmsUnitActivation_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 4, 2),
    _LmsUnitActivation_Type()
)
lmsUnitActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmsUnitActivation.setStatus("mandatory")
_ProxyUnit_ObjectIdentity = ObjectIdentity
proxyUnit = _ProxyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 5)
)


class _ProxyUnitGlobalStatus_Type(Integer32):
    """Custom type proxyUnitGlobalStatus based on Integer32"""
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
        *(("green", 1),
          ("orange", 3),
          ("red", 4),
          ("unmanaged", 0),
          ("yellow", 2))
    )


_ProxyUnitGlobalStatus_Type.__name__ = "Integer32"
_ProxyUnitGlobalStatus_Object = MibScalar
proxyUnitGlobalStatus = _ProxyUnitGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 5, 1),
    _ProxyUnitGlobalStatus_Type()
)
proxyUnitGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyUnitGlobalStatus.setStatus("mandatory")


class _ProxyUnitActivation_Type(Integer32):
    """Custom type proxyUnitActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setonly", 2),
          ("start", 1),
          ("stop", 0))
    )


_ProxyUnitActivation_Type.__name__ = "Integer32"
_ProxyUnitActivation_Object = MibScalar
proxyUnitActivation = _ProxyUnitActivation_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 5, 2),
    _ProxyUnitActivation_Type()
)
proxyUnitActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyUnitActivation.setStatus("mandatory")
_ProxyUnitScagentCpuUse_Type = OctetString
_ProxyUnitScagentCpuUse_Object = MibScalar
proxyUnitScagentCpuUse = _ProxyUnitScagentCpuUse_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 5, 3),
    _ProxyUnitScagentCpuUse_Type()
)
proxyUnitScagentCpuUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyUnitScagentCpuUse.setStatus("mandatory")
_ProxyUnitScagentMemoryUse_Type = Integer32
_ProxyUnitScagentMemoryUse_Object = MibScalar
proxyUnitScagentMemoryUse = _ProxyUnitScagentMemoryUse_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 5, 4),
    _ProxyUnitScagentMemoryUse_Type()
)
proxyUnitScagentMemoryUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyUnitScagentMemoryUse.setStatus("mandatory")
_ProxyUnitHttpdCpuUse_Type = OctetString
_ProxyUnitHttpdCpuUse_Object = MibScalar
proxyUnitHttpdCpuUse = _ProxyUnitHttpdCpuUse_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 5, 5),
    _ProxyUnitHttpdCpuUse_Type()
)
proxyUnitHttpdCpuUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyUnitHttpdCpuUse.setStatus("mandatory")
_ProxyUnitHttpdMemoryUse_Type = Integer32
_ProxyUnitHttpdMemoryUse_Object = MibScalar
proxyUnitHttpdMemoryUse = _ProxyUnitHttpdMemoryUse_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 5, 6),
    _ProxyUnitHttpdMemoryUse_Type()
)
proxyUnitHttpdMemoryUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyUnitHttpdMemoryUse.setStatus("mandatory")
_BillingUnit_ObjectIdentity = ObjectIdentity
billingUnit = _BillingUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6)
)


class _BillingUnitGlobalStatus_Type(Integer32):
    """Custom type billingUnitGlobalStatus based on Integer32"""
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
        *(("green", 1),
          ("orange", 3),
          ("red", 4),
          ("unmanaged", 0),
          ("yellow", 2))
    )


_BillingUnitGlobalStatus_Type.__name__ = "Integer32"
_BillingUnitGlobalStatus_Object = MibScalar
billingUnitGlobalStatus = _BillingUnitGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 1),
    _BillingUnitGlobalStatus_Type()
)
billingUnitGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    billingUnitGlobalStatus.setStatus("mandatory")


class _BillingUnitActivation_Type(Integer32):
    """Custom type billingUnitActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setonly", 2),
          ("start", 1),
          ("stop", 0))
    )


_BillingUnitActivation_Type.__name__ = "Integer32"
_BillingUnitActivation_Object = MibScalar
billingUnitActivation = _BillingUnitActivation_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 2),
    _BillingUnitActivation_Type()
)
billingUnitActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billingUnitActivation.setStatus("mandatory")
_BuScstats_ObjectIdentity = ObjectIdentity
buScstats = _BuScstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3)
)
_BuScInAgentReportRequests_Type = Integer32
_BuScInAgentReportRequests_Object = MibScalar
buScInAgentReportRequests = _BuScInAgentReportRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 1),
    _BuScInAgentReportRequests_Type()
)
buScInAgentReportRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInAgentReportRequests.setStatus("mandatory")
_BuScOutUpdateSessionReplies_Type = Integer32
_BuScOutUpdateSessionReplies_Object = MibScalar
buScOutUpdateSessionReplies = _BuScOutUpdateSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 2),
    _BuScOutUpdateSessionReplies_Type()
)
buScOutUpdateSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutUpdateSessionReplies.setStatus("mandatory")
_BuScOutReplies_Type = Integer32
_BuScOutReplies_Object = MibScalar
buScOutReplies = _BuScOutReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 3),
    _BuScOutReplies_Type()
)
buScOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutReplies.setStatus("mandatory")
_BuScCurrentServicesPendingSessions_Type = Integer32
_BuScCurrentServicesPendingSessions_Object = MibScalar
buScCurrentServicesPendingSessions = _BuScCurrentServicesPendingSessions_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 4),
    _BuScCurrentServicesPendingSessions_Type()
)
buScCurrentServicesPendingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScCurrentServicesPendingSessions.setStatus("mandatory")
_BuScUdrs_Type = Integer32
_BuScUdrs_Object = MibScalar
buScUdrs = _BuScUdrs_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 5),
    _BuScUdrs_Type()
)
buScUdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScUdrs.setStatus("mandatory")
_BuScInReportUsageReplies_Type = Integer32
_BuScInReportUsageReplies_Object = MibScalar
buScInReportUsageReplies = _BuScInReportUsageReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 6),
    _BuScInReportUsageReplies_Type()
)
buScInReportUsageReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInReportUsageReplies.setStatus("mandatory")
_BuScClosedSessions_Type = Integer32
_BuScClosedSessions_Object = MibScalar
buScClosedSessions = _BuScClosedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 7),
    _BuScClosedSessions_Type()
)
buScClosedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScClosedSessions.setStatus("mandatory")
_BuScOldServicesPendingSessions_Type = Integer32
_BuScOldServicesPendingSessions_Object = MibScalar
buScOldServicesPendingSessions = _BuScOldServicesPendingSessions_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 8),
    _BuScOldServicesPendingSessions_Type()
)
buScOldServicesPendingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOldServicesPendingSessions.setStatus("mandatory")
_BuScInRequests_Type = Integer32
_BuScInRequests_Object = MibScalar
buScInRequests = _BuScInRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 9),
    _BuScInRequests_Type()
)
buScInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInRequests.setStatus("mandatory")
_BuScOutAgentReportReplies_Type = Integer32
_BuScOutAgentReportReplies_Object = MibScalar
buScOutAgentReportReplies = _BuScOutAgentReportReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 10),
    _BuScOutAgentReportReplies_Type()
)
buScOutAgentReportReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutAgentReportReplies.setStatus("mandatory")
_BuScInCloseSessionReplies_Type = Integer32
_BuScInCloseSessionReplies_Object = MibScalar
buScInCloseSessionReplies = _BuScInCloseSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 11),
    _BuScInCloseSessionReplies_Type()
)
buScInCloseSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInCloseSessionReplies.setStatus("mandatory")
_BuScInCloseSessionRequests_Type = Integer32
_BuScInCloseSessionRequests_Object = MibScalar
buScInCloseSessionRequests = _BuScInCloseSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 12),
    _BuScInCloseSessionRequests_Type()
)
buScInCloseSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInCloseSessionRequests.setStatus("mandatory")
_BuScOutCloseSessionReplies_Type = Integer32
_BuScOutCloseSessionReplies_Object = MibScalar
buScOutCloseSessionReplies = _BuScOutCloseSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 13),
    _BuScOutCloseSessionReplies_Type()
)
buScOutCloseSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutCloseSessionReplies.setStatus("mandatory")
_BuScUdrFiles_Type = Integer32
_BuScUdrFiles_Object = MibScalar
buScUdrFiles = _BuScUdrFiles_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 14),
    _BuScUdrFiles_Type()
)
buScUdrFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScUdrFiles.setStatus("mandatory")
_BuScOutListSessionReplies_Type = Integer32
_BuScOutListSessionReplies_Object = MibScalar
buScOutListSessionReplies = _BuScOutListSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 15),
    _BuScOutListSessionReplies_Type()
)
buScOutListSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutListSessionReplies.setStatus("mandatory")
_BuScOutRequests_Type = Integer32
_BuScOutRequests_Object = MibScalar
buScOutRequests = _BuScOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 16),
    _BuScOutRequests_Type()
)
buScOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutRequests.setStatus("mandatory")
_BuScOutUpdateSessionRequests_Type = Integer32
_BuScOutUpdateSessionRequests_Object = MibScalar
buScOutUpdateSessionRequests = _BuScOutUpdateSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 17),
    _BuScOutUpdateSessionRequests_Type()
)
buScOutUpdateSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutUpdateSessionRequests.setStatus("mandatory")
_BuScInUpdateSessionReplies_Type = Integer32
_BuScInUpdateSessionReplies_Object = MibScalar
buScInUpdateSessionReplies = _BuScInUpdateSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 18),
    _BuScInUpdateSessionReplies_Type()
)
buScInUpdateSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInUpdateSessionReplies.setStatus("mandatory")
_BuScInAgentReportReplies_Type = Integer32
_BuScInAgentReportReplies_Object = MibScalar
buScInAgentReportReplies = _BuScInAgentReportReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 19),
    _BuScInAgentReportReplies_Type()
)
buScInAgentReportReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInAgentReportReplies.setStatus("mandatory")
_BuScOutAgentReportRequests_Type = Integer32
_BuScOutAgentReportRequests_Object = MibScalar
buScOutAgentReportRequests = _BuScOutAgentReportRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 20),
    _BuScOutAgentReportRequests_Type()
)
buScOutAgentReportRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutAgentReportRequests.setStatus("mandatory")
_BuScInUpdateSessionRequests_Type = Integer32
_BuScInUpdateSessionRequests_Object = MibScalar
buScInUpdateSessionRequests = _BuScInUpdateSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 21),
    _BuScInUpdateSessionRequests_Type()
)
buScInUpdateSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInUpdateSessionRequests.setStatus("mandatory")
_BuScInReplies_Type = Integer32
_BuScInReplies_Object = MibScalar
buScInReplies = _BuScInReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 22),
    _BuScInReplies_Type()
)
buScInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInReplies.setStatus("mandatory")
_BuScOutCreateSessionRequests_Type = Integer32
_BuScOutCreateSessionRequests_Object = MibScalar
buScOutCreateSessionRequests = _BuScOutCreateSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 23),
    _BuScOutCreateSessionRequests_Type()
)
buScOutCreateSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutCreateSessionRequests.setStatus("mandatory")
_BuInReportUsageRequests_Type = Integer32
_BuInReportUsageRequests_Object = MibScalar
buInReportUsageRequests = _BuInReportUsageRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 24),
    _BuInReportUsageRequests_Type()
)
buInReportUsageRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buInReportUsageRequests.setStatus("mandatory")
_BuInListSessionRequests_Type = Integer32
_BuInListSessionRequests_Object = MibScalar
buInListSessionRequests = _BuInListSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 25),
    _BuInListSessionRequests_Type()
)
buInListSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buInListSessionRequests.setStatus("mandatory")
_BuScOutReportUsageRequests_Type = Integer32
_BuScOutReportUsageRequests_Object = MibScalar
buScOutReportUsageRequests = _BuScOutReportUsageRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 26),
    _BuScOutReportUsageRequests_Type()
)
buScOutReportUsageRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutReportUsageRequests.setStatus("mandatory")
_BuScInListSessionReplies_Type = Integer32
_BuScInListSessionReplies_Object = MibScalar
buScInListSessionReplies = _BuScInListSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 27),
    _BuScInListSessionReplies_Type()
)
buScInListSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInListSessionReplies.setStatus("mandatory")
_BuScInCreateSessionRequests_Type = Integer32
_BuScInCreateSessionRequests_Object = MibScalar
buScInCreateSessionRequests = _BuScInCreateSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 28),
    _BuScInCreateSessionRequests_Type()
)
buScInCreateSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInCreateSessionRequests.setStatus("mandatory")
_BuScOutCloseSessionRequests_Type = Integer32
_BuScOutCloseSessionRequests_Object = MibScalar
buScOutCloseSessionRequests = _BuScOutCloseSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 29),
    _BuScOutCloseSessionRequests_Type()
)
buScOutCloseSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutCloseSessionRequests.setStatus("mandatory")
_BuScOutListSessionRequests_Type = Integer32
_BuScOutListSessionRequests_Object = MibScalar
buScOutListSessionRequests = _BuScOutListSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 30),
    _BuScOutListSessionRequests_Type()
)
buScOutListSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutListSessionRequests.setStatus("mandatory")
_BuScInCreateSessionReplies_Type = Integer32
_BuScInCreateSessionReplies_Object = MibScalar
buScInCreateSessionReplies = _BuScInCreateSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 31),
    _BuScInCreateSessionReplies_Type()
)
buScInCreateSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInCreateSessionReplies.setStatus("mandatory")
_BuScCreatedSessions_Type = Integer32
_BuScCreatedSessions_Object = MibScalar
buScCreatedSessions = _BuScCreatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 32),
    _BuScCreatedSessions_Type()
)
buScCreatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScCreatedSessions.setStatus("mandatory")
_BuScOutReportUsageReplies_Type = Integer32
_BuScOutReportUsageReplies_Object = MibScalar
buScOutReportUsageReplies = _BuScOutReportUsageReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 33),
    _BuScOutReportUsageReplies_Type()
)
buScOutReportUsageReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutReportUsageReplies.setStatus("mandatory")
_BuScOutCreateSessionReplies_Type = Integer32
_BuScOutCreateSessionReplies_Object = MibScalar
buScOutCreateSessionReplies = _BuScOutCreateSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 34),
    _BuScOutCreateSessionReplies_Type()
)
buScOutCreateSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutCreateSessionReplies.setStatus("mandatory")
_BuScSessionsPerSecond_Type = Integer32
_BuScSessionsPerSecond_Object = MibScalar
buScSessionsPerSecond = _BuScSessionsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 35),
    _BuScSessionsPerSecond_Type()
)
buScSessionsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScSessionsPerSecond.setStatus("mandatory")
_BuScRejectedSessions_Type = Integer32
_BuScRejectedSessions_Object = MibScalar
buScRejectedSessions = _BuScRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 36),
    _BuScRejectedSessions_Type()
)
buScRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScRejectedSessions.setStatus("mandatory")
_BuScInContinueSessionRequest_Type = Integer32
_BuScInContinueSessionRequest_Object = MibScalar
buScInContinueSessionRequest = _BuScInContinueSessionRequest_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 37),
    _BuScInContinueSessionRequest_Type()
)
buScInContinueSessionRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInContinueSessionRequest.setStatus("mandatory")
_BuScOutContinueSessionRequest_Type = Integer32
_BuScOutContinueSessionRequest_Object = MibScalar
buScOutContinueSessionRequest = _BuScOutContinueSessionRequest_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 38),
    _BuScOutContinueSessionRequest_Type()
)
buScOutContinueSessionRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutContinueSessionRequest.setStatus("mandatory")
_BuScInContinueSessionReplies_Type = Integer32
_BuScInContinueSessionReplies_Object = MibScalar
buScInContinueSessionReplies = _BuScInContinueSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 39),
    _BuScInContinueSessionReplies_Type()
)
buScInContinueSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScInContinueSessionReplies.setStatus("mandatory")
_BuScOutContinueSessionReplies_Type = Integer32
_BuScOutContinueSessionReplies_Object = MibScalar
buScOutContinueSessionReplies = _BuScOutContinueSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 40),
    _BuScOutContinueSessionReplies_Type()
)
buScOutContinueSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScOutContinueSessionReplies.setStatus("mandatory")
_BuScAuthRequests_Type = Integer32
_BuScAuthRequests_Object = MibScalar
buScAuthRequests = _BuScAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 41),
    _BuScAuthRequests_Type()
)
buScAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScAuthRequests.setStatus("mandatory")
_BuScAuthNonRepliedRequestsPercent_Type = Integer32
_BuScAuthNonRepliedRequestsPercent_Object = MibScalar
buScAuthNonRepliedRequestsPercent = _BuScAuthNonRepliedRequestsPercent_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 42),
    _BuScAuthNonRepliedRequestsPercent_Type()
)
buScAuthNonRepliedRequestsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScAuthNonRepliedRequestsPercent.setStatus("mandatory")
_BuScAuthReplies_Type = Integer32
_BuScAuthReplies_Object = MibScalar
buScAuthReplies = _BuScAuthReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 43),
    _BuScAuthReplies_Type()
)
buScAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScAuthReplies.setStatus("mandatory")
_BuScAcctReplies_Type = Integer32
_BuScAcctReplies_Object = MibScalar
buScAcctReplies = _BuScAcctReplies_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 44),
    _BuScAcctReplies_Type()
)
buScAcctReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScAcctReplies.setStatus("mandatory")
_BuScAcctRequests_Type = Integer32
_BuScAcctRequests_Object = MibScalar
buScAcctRequests = _BuScAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 45),
    _BuScAcctRequests_Type()
)
buScAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScAcctRequests.setStatus("mandatory")
_BuScAcctNonRepliedRequestsPercent_Type = Integer32
_BuScAcctNonRepliedRequestsPercent_Object = MibScalar
buScAcctNonRepliedRequestsPercent = _BuScAcctNonRepliedRequestsPercent_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 46),
    _BuScAcctNonRepliedRequestsPercent_Type()
)
buScAcctNonRepliedRequestsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScAcctNonRepliedRequestsPercent.setStatus("mandatory")
_BuScReplicatedSessions_Type = Integer32
_BuScReplicatedSessions_Object = MibScalar
buScReplicatedSessions = _BuScReplicatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 47),
    _BuScReplicatedSessions_Type()
)
buScReplicatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScReplicatedSessions.setStatus("mandatory")
_BuScActivityCount_Type = Integer32
_BuScActivityCount_Object = MibScalar
buScActivityCount = _BuScActivityCount_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 3, 48),
    _BuScActivityCount_Type()
)
buScActivityCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buScActivityCount.setStatus("mandatory")
_BillingUnitScagentCpuUse_Type = OctetString
_BillingUnitScagentCpuUse_Object = MibScalar
billingUnitScagentCpuUse = _BillingUnitScagentCpuUse_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 4),
    _BillingUnitScagentCpuUse_Type()
)
billingUnitScagentCpuUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    billingUnitScagentCpuUse.setStatus("mandatory")
_BillingUnitScagentMemoryUse_Type = Integer32
_BillingUnitScagentMemoryUse_Object = MibScalar
billingUnitScagentMemoryUse = _BillingUnitScagentMemoryUse_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 6, 5),
    _BillingUnitScagentMemoryUse_Type()
)
billingUnitScagentMemoryUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    billingUnitScagentMemoryUse.setStatus("mandatory")
_UpdateServerConfig_Type = Integer32
_UpdateServerConfig_Object = MibScalar
updateServerConfig = _UpdateServerConfig_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 7),
    _UpdateServerConfig_Type()
)
updateServerConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    updateServerConfig.setStatus("mandatory")
_ConfigServerItf_Type = OctetString
_ConfigServerItf_Object = MibScalar
configServerItf = _ConfigServerItf_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 8),
    _ConfigServerItf_Type()
)
configServerItf.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    configServerItf.setStatus("mandatory")
_RestartDataCollector_Type = Integer32
_RestartDataCollector_Object = MibScalar
restartDataCollector = _RestartDataCollector_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 9),
    _RestartDataCollector_Type()
)
restartDataCollector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartDataCollector.setStatus("mandatory")
_ServerConnCount_Type = Integer32
_ServerConnCount_Object = MibScalar
serverConnCount = _ServerConnCount_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 10),
    _ServerConnCount_Type()
)
serverConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnCount.setStatus("mandatory")
_ServerConnTable_Object = MibTable
serverConnTable = _ServerConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 11)
)
if mibBuilder.loadTexts:
    serverConnTable.setStatus("current")
_ServerConnEntry_Object = MibTableRow
serverConnEntry = _ServerConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 11, 1)
)
serverConnEntry.setIndexNames(
    (0, "KENYA-COMPONENT-MIB", "bayServerIndex"),
)
if mibBuilder.loadTexts:
    serverConnEntry.setStatus("current")


class _ServerConnIndex_Type(Integer32):
    """Custom type serverConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ServerConnIndex_Type.__name__ = "Integer32"
_ServerConnIndex_Object = MibTableColumn
serverConnIndex = _ServerConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 11, 1, 1),
    _ServerConnIndex_Type()
)
serverConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnIndex.setStatus("current")
_ServerConnStartAddress_Type = IpAddress
_ServerConnStartAddress_Object = MibTableColumn
serverConnStartAddress = _ServerConnStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 11, 1, 2),
    _ServerConnStartAddress_Type()
)
serverConnStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnStartAddress.setStatus("current")
_ServerConnEndAddress_Type = IpAddress
_ServerConnEndAddress_Object = MibTableColumn
serverConnEndAddress = _ServerConnEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 11, 1, 3),
    _ServerConnEndAddress_Type()
)
serverConnEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnEndAddress.setStatus("current")


class _ServerConnStatus_Type(Integer32):
    """Custom type serverConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failure", 0),
          ("ok", 1))
    )


_ServerConnStatus_Type.__name__ = "Integer32"
_ServerConnStatus_Object = MibTableColumn
serverConnStatus = _ServerConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 1, 11, 1, 4),
    _ServerConnStatus_Type()
)
serverConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverConnStatus.setStatus("mandatory")
_NmSoftwares_ObjectIdentity = ObjectIdentity
nmSoftwares = _NmSoftwares_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2)
)
_ScSoftwares_ObjectIdentity = ObjectIdentity
scSoftwares = _ScSoftwares_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 3)
)
_PxSoftwares_ObjectIdentity = ObjectIdentity
pxSoftwares = _PxSoftwares_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KENYA-COMPONENT-MIB",
    **{"bayServer": bayServer,
       "isLms": isLms,
       "isProxy": isProxy,
       "isBilling": isBilling,
       "lmsUnit": lmsUnit,
       "lmsUnitGlobalStatus": lmsUnitGlobalStatus,
       "lmsUnitActivation": lmsUnitActivation,
       "proxyUnit": proxyUnit,
       "proxyUnitGlobalStatus": proxyUnitGlobalStatus,
       "proxyUnitActivation": proxyUnitActivation,
       "proxyUnitScagentCpuUse": proxyUnitScagentCpuUse,
       "proxyUnitScagentMemoryUse": proxyUnitScagentMemoryUse,
       "proxyUnitHttpdCpuUse": proxyUnitHttpdCpuUse,
       "proxyUnitHttpdMemoryUse": proxyUnitHttpdMemoryUse,
       "billingUnit": billingUnit,
       "billingUnitGlobalStatus": billingUnitGlobalStatus,
       "billingUnitActivation": billingUnitActivation,
       "buScstats": buScstats,
       "buScInAgentReportRequests": buScInAgentReportRequests,
       "buScOutUpdateSessionReplies": buScOutUpdateSessionReplies,
       "buScOutReplies": buScOutReplies,
       "buScCurrentServicesPendingSessions": buScCurrentServicesPendingSessions,
       "buScUdrs": buScUdrs,
       "buScInReportUsageReplies": buScInReportUsageReplies,
       "buScClosedSessions": buScClosedSessions,
       "buScOldServicesPendingSessions": buScOldServicesPendingSessions,
       "buScInRequests": buScInRequests,
       "buScOutAgentReportReplies": buScOutAgentReportReplies,
       "buScInCloseSessionReplies": buScInCloseSessionReplies,
       "buScInCloseSessionRequests": buScInCloseSessionRequests,
       "buScOutCloseSessionReplies": buScOutCloseSessionReplies,
       "buScUdrFiles": buScUdrFiles,
       "buScOutListSessionReplies": buScOutListSessionReplies,
       "buScOutRequests": buScOutRequests,
       "buScOutUpdateSessionRequests": buScOutUpdateSessionRequests,
       "buScInUpdateSessionReplies": buScInUpdateSessionReplies,
       "buScInAgentReportReplies": buScInAgentReportReplies,
       "buScOutAgentReportRequests": buScOutAgentReportRequests,
       "buScInUpdateSessionRequests": buScInUpdateSessionRequests,
       "buScInReplies": buScInReplies,
       "buScOutCreateSessionRequests": buScOutCreateSessionRequests,
       "buInReportUsageRequests": buInReportUsageRequests,
       "buInListSessionRequests": buInListSessionRequests,
       "buScOutReportUsageRequests": buScOutReportUsageRequests,
       "buScInListSessionReplies": buScInListSessionReplies,
       "buScInCreateSessionRequests": buScInCreateSessionRequests,
       "buScOutCloseSessionRequests": buScOutCloseSessionRequests,
       "buScOutListSessionRequests": buScOutListSessionRequests,
       "buScInCreateSessionReplies": buScInCreateSessionReplies,
       "buScCreatedSessions": buScCreatedSessions,
       "buScOutReportUsageReplies": buScOutReportUsageReplies,
       "buScOutCreateSessionReplies": buScOutCreateSessionReplies,
       "buScSessionsPerSecond": buScSessionsPerSecond,
       "buScRejectedSessions": buScRejectedSessions,
       "buScInContinueSessionRequest": buScInContinueSessionRequest,
       "buScOutContinueSessionRequest": buScOutContinueSessionRequest,
       "buScInContinueSessionReplies": buScInContinueSessionReplies,
       "buScOutContinueSessionReplies": buScOutContinueSessionReplies,
       "buScAuthRequests": buScAuthRequests,
       "buScAuthNonRepliedRequestsPercent": buScAuthNonRepliedRequestsPercent,
       "buScAuthReplies": buScAuthReplies,
       "buScAcctReplies": buScAcctReplies,
       "buScAcctRequests": buScAcctRequests,
       "buScAcctNonRepliedRequestsPercent": buScAcctNonRepliedRequestsPercent,
       "buScReplicatedSessions": buScReplicatedSessions,
       "buScActivityCount": buScActivityCount,
       "billingUnitScagentCpuUse": billingUnitScagentCpuUse,
       "billingUnitScagentMemoryUse": billingUnitScagentMemoryUse,
       "updateServerConfig": updateServerConfig,
       "configServerItf": configServerItf,
       "restartDataCollector": restartDataCollector,
       "serverConnCount": serverConnCount,
       "serverConnTable": serverConnTable,
       "serverConnEntry": serverConnEntry,
       "serverConnIndex": serverConnIndex,
       "serverConnStartAddress": serverConnStartAddress,
       "serverConnEndAddress": serverConnEndAddress,
       "serverConnStatus": serverConnStatus,
       "nmSoftwares": nmSoftwares,
       "scSoftwares": scSoftwares,
       "pxSoftwares": pxSoftwares}
)

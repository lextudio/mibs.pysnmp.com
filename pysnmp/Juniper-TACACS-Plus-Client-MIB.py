# SNMP MIB module (Juniper-TACACS-Plus-Client-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-TACACS-Plus-Client-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:27 2024
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

juniTacacsPlusClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60)
)
juniTacacsPlusClientMIB.setRevisions(
        ("2004-03-02 17:31",
         "2002-09-16 21:44",
         "2002-07-12 13:49")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniKeyString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_JuniTacacsPlusClientObjects_ObjectIdentity = ObjectIdentity
juniTacacsPlusClientObjects = _JuniTacacsPlusClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1)
)
_JuniTacacsPlusClientCommonConfig_ObjectIdentity = ObjectIdentity
juniTacacsPlusClientCommonConfig = _JuniTacacsPlusClientCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 1)
)


class _JuniTacacsPlusClientDirectedRequest_Type(Integer32):
    """Custom type juniTacacsPlusClientDirectedRequest based on Integer32"""
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
        *(("disabled", 2),
          ("notRestrictedAndNotTruncated", 3),
          ("notRestrictedAndTruncated", 1),
          ("restrictedAndNotTruncated", 5),
          ("restrictedAndTruncated", 4))
    )


_JuniTacacsPlusClientDirectedRequest_Type.__name__ = "Integer32"
_JuniTacacsPlusClientDirectedRequest_Object = MibScalar
juniTacacsPlusClientDirectedRequest = _JuniTacacsPlusClientDirectedRequest_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 1, 1),
    _JuniTacacsPlusClientDirectedRequest_Type()
)
juniTacacsPlusClientDirectedRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniTacacsPlusClientDirectedRequest.setStatus("current")


class _JuniTacacsPlusClientTimeout_Type(Integer32):
    """Custom type juniTacacsPlusClientTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniTacacsPlusClientTimeout_Type.__name__ = "Integer32"
_JuniTacacsPlusClientTimeout_Object = MibScalar
juniTacacsPlusClientTimeout = _JuniTacacsPlusClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 1, 2),
    _JuniTacacsPlusClientTimeout_Type()
)
juniTacacsPlusClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniTacacsPlusClientTimeout.setStatus("current")
_JuniTacacsPlusClientKey_Type = JuniKeyString
_JuniTacacsPlusClientKey_Object = MibScalar
juniTacacsPlusClientKey = _JuniTacacsPlusClientKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 1, 3),
    _JuniTacacsPlusClientKey_Type()
)
juniTacacsPlusClientKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniTacacsPlusClientKey.setStatus("current")
_JuniTacacsPlusClientSourceIp_Type = IpAddress
_JuniTacacsPlusClientSourceIp_Object = MibScalar
juniTacacsPlusClientSourceIp = _JuniTacacsPlusClientSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 1, 4),
    _JuniTacacsPlusClientSourceIp_Type()
)
juniTacacsPlusClientSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniTacacsPlusClientSourceIp.setStatus("current")
_JuniTacacsPlusClientHostConfig_ObjectIdentity = ObjectIdentity
juniTacacsPlusClientHostConfig = _JuniTacacsPlusClientHostConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2)
)
_JuniTacacsPlusClientHostConfigTable_Object = MibTable
juniTacacsPlusClientHostConfigTable = _JuniTacacsPlusClientHostConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostConfigTable.setStatus("current")
_JuniTacacsPlusClientHostConfigEntry_Object = MibTableRow
juniTacacsPlusClientHostConfigEntry = _JuniTacacsPlusClientHostConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1)
)
juniTacacsPlusClientHostConfigEntry.setIndexNames(
    (0, "Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAddr"),
)
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostConfigEntry.setStatus("current")
_JuniTacacsPlusClientHostAddr_Type = IpAddress
_JuniTacacsPlusClientHostAddr_Object = MibTableColumn
juniTacacsPlusClientHostAddr = _JuniTacacsPlusClientHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 1),
    _JuniTacacsPlusClientHostAddr_Type()
)
juniTacacsPlusClientHostAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAddr.setStatus("current")


class _JuniTacacsPlusClientHostPort_Type(Integer32):
    """Custom type juniTacacsPlusClientHostPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniTacacsPlusClientHostPort_Type.__name__ = "Integer32"
_JuniTacacsPlusClientHostPort_Object = MibTableColumn
juniTacacsPlusClientHostPort = _JuniTacacsPlusClientHostPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 2),
    _JuniTacacsPlusClientHostPort_Type()
)
juniTacacsPlusClientHostPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostPort.setStatus("current")


class _JuniTacacsPlusClientHostPrimary_Type(TruthValue):
    """Custom type juniTacacsPlusClientHostPrimary based on TruthValue"""


_JuniTacacsPlusClientHostPrimary_Object = MibTableColumn
juniTacacsPlusClientHostPrimary = _JuniTacacsPlusClientHostPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 3),
    _JuniTacacsPlusClientHostPrimary_Type()
)
juniTacacsPlusClientHostPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostPrimary.setStatus("current")


class _JuniTacacsPlusClientHostSingleConnection_Type(TruthValue):
    """Custom type juniTacacsPlusClientHostSingleConnection based on TruthValue"""


_JuniTacacsPlusClientHostSingleConnection_Object = MibTableColumn
juniTacacsPlusClientHostSingleConnection = _JuniTacacsPlusClientHostSingleConnection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 4),
    _JuniTacacsPlusClientHostSingleConnection_Type()
)
juniTacacsPlusClientHostSingleConnection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostSingleConnection.setStatus("current")


class _JuniTacacsPlusClientHostTimeout_Type(Integer32):
    """Custom type juniTacacsPlusClientHostTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniTacacsPlusClientHostTimeout_Type.__name__ = "Integer32"
_JuniTacacsPlusClientHostTimeout_Object = MibTableColumn
juniTacacsPlusClientHostTimeout = _JuniTacacsPlusClientHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 5),
    _JuniTacacsPlusClientHostTimeout_Type()
)
juniTacacsPlusClientHostTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostTimeout.setStatus("current")
_JuniTacacsPlusClientHostKey_Type = JuniKeyString
_JuniTacacsPlusClientHostKey_Object = MibTableColumn
juniTacacsPlusClientHostKey = _JuniTacacsPlusClientHostKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 6),
    _JuniTacacsPlusClientHostKey_Type()
)
juniTacacsPlusClientHostKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostKey.setStatus("current")
_JuniTacacsPlusClientHostStatus_Type = RowStatus
_JuniTacacsPlusClientHostStatus_Object = MibTableColumn
juniTacacsPlusClientHostStatus = _JuniTacacsPlusClientHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 7),
    _JuniTacacsPlusClientHostStatus_Type()
)
juniTacacsPlusClientHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostStatus.setStatus("current")
_JuniTacacsPlusClientHostOrder_Type = Integer32
_JuniTacacsPlusClientHostOrder_Object = MibTableColumn
juniTacacsPlusClientHostOrder = _JuniTacacsPlusClientHostOrder_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 8),
    _JuniTacacsPlusClientHostOrder_Type()
)
juniTacacsPlusClientHostOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostOrder.setStatus("current")
_JuniTacacsPlusClientHostStats_ObjectIdentity = ObjectIdentity
juniTacacsPlusClientHostStats = _JuniTacacsPlusClientHostStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3)
)
_JuniTacacsPlusClientHostStatsTable_Object = MibTable
juniTacacsPlusClientHostStatsTable = _JuniTacacsPlusClientHostStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1)
)
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostStatsTable.setStatus("current")
_JuniTacacsPlusClientHostStatsEntry_Object = MibTableRow
juniTacacsPlusClientHostStatsEntry = _JuniTacacsPlusClientHostStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostStatsEntry.setStatus("current")
_JuniTacacsPlusClientHostAuthRequests_Type = Counter32
_JuniTacacsPlusClientHostAuthRequests_Object = MibTableColumn
juniTacacsPlusClientHostAuthRequests = _JuniTacacsPlusClientHostAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 1),
    _JuniTacacsPlusClientHostAuthRequests_Type()
)
juniTacacsPlusClientHostAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAuthRequests.setStatus("current")
_JuniTacacsPlusClientHostAuthReplies_Type = Counter32
_JuniTacacsPlusClientHostAuthReplies_Object = MibTableColumn
juniTacacsPlusClientHostAuthReplies = _JuniTacacsPlusClientHostAuthReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 2),
    _JuniTacacsPlusClientHostAuthReplies_Type()
)
juniTacacsPlusClientHostAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAuthReplies.setStatus("current")
_JuniTacacsPlusClientHostAuthPending_Type = Counter32
_JuniTacacsPlusClientHostAuthPending_Object = MibTableColumn
juniTacacsPlusClientHostAuthPending = _JuniTacacsPlusClientHostAuthPending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 3),
    _JuniTacacsPlusClientHostAuthPending_Type()
)
juniTacacsPlusClientHostAuthPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAuthPending.setStatus("current")
_JuniTacacsPlusClientHostAuthTimeouts_Type = Counter32
_JuniTacacsPlusClientHostAuthTimeouts_Object = MibTableColumn
juniTacacsPlusClientHostAuthTimeouts = _JuniTacacsPlusClientHostAuthTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 4),
    _JuniTacacsPlusClientHostAuthTimeouts_Type()
)
juniTacacsPlusClientHostAuthTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAuthTimeouts.setStatus("current")
_JuniTacacsPlusClientHostAuthorRequests_Type = Counter32
_JuniTacacsPlusClientHostAuthorRequests_Object = MibTableColumn
juniTacacsPlusClientHostAuthorRequests = _JuniTacacsPlusClientHostAuthorRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 5),
    _JuniTacacsPlusClientHostAuthorRequests_Type()
)
juniTacacsPlusClientHostAuthorRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAuthorRequests.setStatus("current")
_JuniTacacsPlusClientHostAuthorReplies_Type = Counter32
_JuniTacacsPlusClientHostAuthorReplies_Object = MibTableColumn
juniTacacsPlusClientHostAuthorReplies = _JuniTacacsPlusClientHostAuthorReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 6),
    _JuniTacacsPlusClientHostAuthorReplies_Type()
)
juniTacacsPlusClientHostAuthorReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAuthorReplies.setStatus("current")
_JuniTacacsPlusClientHostAuthorPending_Type = Counter32
_JuniTacacsPlusClientHostAuthorPending_Object = MibTableColumn
juniTacacsPlusClientHostAuthorPending = _JuniTacacsPlusClientHostAuthorPending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 7),
    _JuniTacacsPlusClientHostAuthorPending_Type()
)
juniTacacsPlusClientHostAuthorPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAuthorPending.setStatus("current")
_JuniTacacsPlusClientHostAuthorTimeouts_Type = Counter32
_JuniTacacsPlusClientHostAuthorTimeouts_Object = MibTableColumn
juniTacacsPlusClientHostAuthorTimeouts = _JuniTacacsPlusClientHostAuthorTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 8),
    _JuniTacacsPlusClientHostAuthorTimeouts_Type()
)
juniTacacsPlusClientHostAuthorTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAuthorTimeouts.setStatus("current")
_JuniTacacsPlusClientHostAcctRequests_Type = Counter32
_JuniTacacsPlusClientHostAcctRequests_Object = MibTableColumn
juniTacacsPlusClientHostAcctRequests = _JuniTacacsPlusClientHostAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 9),
    _JuniTacacsPlusClientHostAcctRequests_Type()
)
juniTacacsPlusClientHostAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAcctRequests.setStatus("current")
_JuniTacacsPlusClientHostAcctReplies_Type = Counter32
_JuniTacacsPlusClientHostAcctReplies_Object = MibTableColumn
juniTacacsPlusClientHostAcctReplies = _JuniTacacsPlusClientHostAcctReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 10),
    _JuniTacacsPlusClientHostAcctReplies_Type()
)
juniTacacsPlusClientHostAcctReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAcctReplies.setStatus("current")
_JuniTacacsPlusClientHostAcctPending_Type = Counter32
_JuniTacacsPlusClientHostAcctPending_Object = MibTableColumn
juniTacacsPlusClientHostAcctPending = _JuniTacacsPlusClientHostAcctPending_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 11),
    _JuniTacacsPlusClientHostAcctPending_Type()
)
juniTacacsPlusClientHostAcctPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAcctPending.setStatus("current")
_JuniTacacsPlusClientHostAcctTimeouts_Type = Counter32
_JuniTacacsPlusClientHostAcctTimeouts_Object = MibTableColumn
juniTacacsPlusClientHostAcctTimeouts = _JuniTacacsPlusClientHostAcctTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 12),
    _JuniTacacsPlusClientHostAcctTimeouts_Type()
)
juniTacacsPlusClientHostAcctTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostAcctTimeouts.setStatus("current")
_JuniTacacsPlusClientHostDiscontinuityTime_Type = TimeStamp
_JuniTacacsPlusClientHostDiscontinuityTime_Object = MibTableColumn
juniTacacsPlusClientHostDiscontinuityTime = _JuniTacacsPlusClientHostDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 13),
    _JuniTacacsPlusClientHostDiscontinuityTime_Type()
)
juniTacacsPlusClientHostDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostDiscontinuityTime.setStatus("current")
_JuniTacacsPlusClientConformance_ObjectIdentity = ObjectIdentity
juniTacacsPlusClientConformance = _JuniTacacsPlusClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2)
)
_JuniTacacsPlusClientCompliances_ObjectIdentity = ObjectIdentity
juniTacacsPlusClientCompliances = _JuniTacacsPlusClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 1)
)
_JuniTacacsPlusClientGroups_ObjectIdentity = ObjectIdentity
juniTacacsPlusClientGroups = _JuniTacacsPlusClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 2)
)
juniTacacsPlusClientHostConfigEntry.registerAugmentions(
    ("Juniper-TACACS-Plus-Client-MIB",
     "juniTacacsPlusClientHostStatsEntry")
)
juniTacacsPlusClientHostStatsEntry.setIndexNames(*juniTacacsPlusClientHostConfigEntry.getIndexNames())

# Managed Objects groups

juniTacacsPlusClientCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 2, 1)
)
juniTacacsPlusClientCommonGroup.setObjects(
      *(("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientDirectedRequest"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientTimeout"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientKey"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientSourceIp"))
)
if mibBuilder.loadTexts:
    juniTacacsPlusClientCommonGroup.setStatus("current")

juniTacacsPlusClientHostConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 2, 2)
)
juniTacacsPlusClientHostConfigGroup.setObjects(
      *(("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostPort"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostPrimary"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostSingleConnection"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostTimeout"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostKey"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostStatus"))
)
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostConfigGroup.setStatus("obsolete")

juniTacacsPlusClientHostStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 2, 3)
)
juniTacacsPlusClientHostStatsGroup.setObjects(
      *(("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthRequests"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthReplies"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthPending"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthTimeouts"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthorRequests"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthorReplies"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthorPending"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthorTimeouts"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAcctRequests"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAcctReplies"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAcctPending"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAcctTimeouts"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostStatsGroup.setStatus("current")

juniTacacsPlusClientHostConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 2, 4)
)
juniTacacsPlusClientHostConfigGroup2.setObjects(
      *(("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostPort"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostPrimary"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostSingleConnection"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostTimeout"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostKey"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostStatus"),
        ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostOrder"))
)
if mibBuilder.loadTexts:
    juniTacacsPlusClientHostConfigGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniTacacsPlusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniTacacsPlusCompliance.setStatus(
        "obsolete"
    )

juniTacacsPlusCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniTacacsPlusCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-TACACS-Plus-Client-MIB",
    **{"JuniKeyString": JuniKeyString,
       "juniTacacsPlusClientMIB": juniTacacsPlusClientMIB,
       "juniTacacsPlusClientObjects": juniTacacsPlusClientObjects,
       "juniTacacsPlusClientCommonConfig": juniTacacsPlusClientCommonConfig,
       "juniTacacsPlusClientDirectedRequest": juniTacacsPlusClientDirectedRequest,
       "juniTacacsPlusClientTimeout": juniTacacsPlusClientTimeout,
       "juniTacacsPlusClientKey": juniTacacsPlusClientKey,
       "juniTacacsPlusClientSourceIp": juniTacacsPlusClientSourceIp,
       "juniTacacsPlusClientHostConfig": juniTacacsPlusClientHostConfig,
       "juniTacacsPlusClientHostConfigTable": juniTacacsPlusClientHostConfigTable,
       "juniTacacsPlusClientHostConfigEntry": juniTacacsPlusClientHostConfigEntry,
       "juniTacacsPlusClientHostAddr": juniTacacsPlusClientHostAddr,
       "juniTacacsPlusClientHostPort": juniTacacsPlusClientHostPort,
       "juniTacacsPlusClientHostPrimary": juniTacacsPlusClientHostPrimary,
       "juniTacacsPlusClientHostSingleConnection": juniTacacsPlusClientHostSingleConnection,
       "juniTacacsPlusClientHostTimeout": juniTacacsPlusClientHostTimeout,
       "juniTacacsPlusClientHostKey": juniTacacsPlusClientHostKey,
       "juniTacacsPlusClientHostStatus": juniTacacsPlusClientHostStatus,
       "juniTacacsPlusClientHostOrder": juniTacacsPlusClientHostOrder,
       "juniTacacsPlusClientHostStats": juniTacacsPlusClientHostStats,
       "juniTacacsPlusClientHostStatsTable": juniTacacsPlusClientHostStatsTable,
       "juniTacacsPlusClientHostStatsEntry": juniTacacsPlusClientHostStatsEntry,
       "juniTacacsPlusClientHostAuthRequests": juniTacacsPlusClientHostAuthRequests,
       "juniTacacsPlusClientHostAuthReplies": juniTacacsPlusClientHostAuthReplies,
       "juniTacacsPlusClientHostAuthPending": juniTacacsPlusClientHostAuthPending,
       "juniTacacsPlusClientHostAuthTimeouts": juniTacacsPlusClientHostAuthTimeouts,
       "juniTacacsPlusClientHostAuthorRequests": juniTacacsPlusClientHostAuthorRequests,
       "juniTacacsPlusClientHostAuthorReplies": juniTacacsPlusClientHostAuthorReplies,
       "juniTacacsPlusClientHostAuthorPending": juniTacacsPlusClientHostAuthorPending,
       "juniTacacsPlusClientHostAuthorTimeouts": juniTacacsPlusClientHostAuthorTimeouts,
       "juniTacacsPlusClientHostAcctRequests": juniTacacsPlusClientHostAcctRequests,
       "juniTacacsPlusClientHostAcctReplies": juniTacacsPlusClientHostAcctReplies,
       "juniTacacsPlusClientHostAcctPending": juniTacacsPlusClientHostAcctPending,
       "juniTacacsPlusClientHostAcctTimeouts": juniTacacsPlusClientHostAcctTimeouts,
       "juniTacacsPlusClientHostDiscontinuityTime": juniTacacsPlusClientHostDiscontinuityTime,
       "juniTacacsPlusClientConformance": juniTacacsPlusClientConformance,
       "juniTacacsPlusClientCompliances": juniTacacsPlusClientCompliances,
       "juniTacacsPlusCompliance": juniTacacsPlusCompliance,
       "juniTacacsPlusCompliance2": juniTacacsPlusCompliance2,
       "juniTacacsPlusClientGroups": juniTacacsPlusClientGroups,
       "juniTacacsPlusClientCommonGroup": juniTacacsPlusClientCommonGroup,
       "juniTacacsPlusClientHostConfigGroup": juniTacacsPlusClientHostConfigGroup,
       "juniTacacsPlusClientHostStatsGroup": juniTacacsPlusClientHostStatsGroup,
       "juniTacacsPlusClientHostConfigGroup2": juniTacacsPlusClientHostConfigGroup2}
)

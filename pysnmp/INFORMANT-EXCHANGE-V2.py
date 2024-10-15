# SNMP MIB module (INFORMANT-EXCHANGE-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-EXCHANGE-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:12 2024
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

(InstanceName,
 informant) = mibBuilder.importSymbols(
    "WTCS",
    "InstanceName",
    "informant")


# MODULE-IDENTITY

exchangeV2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15)
)
exchangeV2.setRevisions(
        ("2008-04-08 00:09",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ex2ADRMSPrelicensingAgent_ObjectIdentity = ObjectIdentity
ex2ADRMSPrelicensingAgent = _Ex2ADRMSPrelicensingAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 1)
)
if mibBuilder.loadTexts:
    ex2ADRMSPrelicensingAgent.setStatus("current")
_Ex2apaAvgProcessTimeLicenseRqst_Type = Gauge32
_Ex2apaAvgProcessTimeLicenseRqst_Object = MibScalar
ex2apaAvgProcessTimeLicenseRqst = _Ex2apaAvgProcessTimeLicenseRqst_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 1, 1),
    _Ex2apaAvgProcessTimeLicenseRqst_Type()
)
ex2apaAvgProcessTimeLicenseRqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2apaAvgProcessTimeLicenseRqst.setStatus("current")
_Ex2apaMessageProcessSuccessfully_Type = Gauge32
_Ex2apaMessageProcessSuccessfully_Object = MibScalar
ex2apaMessageProcessSuccessfully = _Ex2apaMessageProcessSuccessfully_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 1, 2),
    _Ex2apaMessageProcessSuccessfully_Type()
)
ex2apaMessageProcessSuccessfully.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2apaMessageProcessSuccessfully.setStatus("current")
_Ex2apaPermanentFailLicenseRqsts_Type = Gauge32
_Ex2apaPermanentFailLicenseRqsts_Object = MibScalar
ex2apaPermanentFailLicenseRqsts = _Ex2apaPermanentFailLicenseRqsts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 1, 3),
    _Ex2apaPermanentFailLicenseRqsts_Type()
)
ex2apaPermanentFailLicenseRqsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2apaPermanentFailLicenseRqsts.setStatus("current")
_Ex2apaSuccessfulLicenseRequests_Type = Gauge32
_Ex2apaSuccessfulLicenseRequests_Object = MibScalar
ex2apaSuccessfulLicenseRequests = _Ex2apaSuccessfulLicenseRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 1, 4),
    _Ex2apaSuccessfulLicenseRequests_Type()
)
ex2apaSuccessfulLicenseRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2apaSuccessfulLicenseRequests.setStatus("current")
_Ex2apaTotalLicenseRequests_Type = Gauge32
_Ex2apaTotalLicenseRequests_Object = MibScalar
ex2apaTotalLicenseRequests = _Ex2apaTotalLicenseRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 1, 5),
    _Ex2apaTotalLicenseRequests_Type()
)
ex2apaTotalLicenseRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2apaTotalLicenseRequests.setStatus("current")
_Ex2apaTotalLicenseRqstsProcTime_Type = Gauge32
_Ex2apaTotalLicenseRqstsProcTime_Object = MibScalar
ex2apaTotalLicenseRqstsProcTime = _Ex2apaTotalLicenseRqstsProcTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 1, 6),
    _Ex2apaTotalLicenseRqstsProcTime_Type()
)
ex2apaTotalLicenseRqstsProcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2apaTotalLicenseRqstsProcTime.setStatus("current")
_Ex2apaTotalLicenseRequestsPerSec_Type = Gauge32
_Ex2apaTotalLicenseRequestsPerSec_Object = MibScalar
ex2apaTotalLicenseRequestsPerSec = _Ex2apaTotalLicenseRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 1, 7),
    _Ex2apaTotalLicenseRequestsPerSec_Type()
)
ex2apaTotalLicenseRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2apaTotalLicenseRequestsPerSec.setStatus("current")
_Ex2apaTotalMessages_Type = Gauge32
_Ex2apaTotalMessages_Object = MibScalar
ex2apaTotalMessages = _Ex2apaTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 1, 8),
    _Ex2apaTotalMessages_Type()
)
ex2apaTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2apaTotalMessages.setStatus("current")
_Ex2apaTotalRecipients_Type = Gauge32
_Ex2apaTotalRecipients_Object = MibScalar
ex2apaTotalRecipients = _Ex2apaTotalRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 1, 9),
    _Ex2apaTotalRecipients_Type()
)
ex2apaTotalRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2apaTotalRecipients.setStatus("current")
_Ex2ADAccessCachesTable_Object = MibTable
ex2ADAccessCachesTable = _Ex2ADAccessCachesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2)
)
if mibBuilder.loadTexts:
    ex2ADAccessCachesTable.setStatus("current")
_Ex2ADAccessCachesEntry_Object = MibTableRow
ex2ADAccessCachesEntry = _Ex2ADAccessCachesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1)
)
ex2ADAccessCachesEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2aacInstance"),
)
if mibBuilder.loadTexts:
    ex2ADAccessCachesEntry.setStatus("current")
_Ex2aacInstance_Type = InstanceName
_Ex2aacInstance_Object = MibTableColumn
ex2aacInstance = _Ex2aacInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 1),
    _Ex2aacInstance_Type()
)
ex2aacInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacInstance.setStatus("current")
_Ex2aacCacheExpireTotalConfigData_Type = Gauge32
_Ex2aacCacheExpireTotalConfigData_Object = MibTableColumn
ex2aacCacheExpireTotalConfigData = _Ex2aacCacheExpireTotalConfigData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 2),
    _Ex2aacCacheExpireTotalConfigData_Type()
)
ex2aacCacheExpireTotalConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheExpireTotalConfigData.setStatus("current")
_Ex2aacCacheExpiriesTotalUserData_Type = Gauge32
_Ex2aacCacheExpiriesTotalUserData_Object = MibTableColumn
ex2aacCacheExpiriesTotalUserData = _Ex2aacCacheExpiriesTotalUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 3),
    _Ex2aacCacheExpiriesTotalUserData_Type()
)
ex2aacCacheExpiriesTotalUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheExpiriesTotalUserData.setStatus("current")
_Ex2aacCacheExpiriesSecConfigData_Type = Gauge32
_Ex2aacCacheExpiriesSecConfigData_Object = MibTableColumn
ex2aacCacheExpiriesSecConfigData = _Ex2aacCacheExpiriesSecConfigData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 4),
    _Ex2aacCacheExpiriesSecConfigData_Type()
)
ex2aacCacheExpiriesSecConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheExpiriesSecConfigData.setStatus("current")
_Ex2aacCacheExpirePerSecUserData_Type = Gauge32
_Ex2aacCacheExpirePerSecUserData_Object = MibTableColumn
ex2aacCacheExpirePerSecUserData = _Ex2aacCacheExpirePerSecUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 5),
    _Ex2aacCacheExpirePerSecUserData_Type()
)
ex2aacCacheExpirePerSecUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheExpirePerSecUserData.setStatus("current")
_Ex2aacCacheHitsTotal_Type = Gauge32
_Ex2aacCacheHitsTotal_Object = MibTableColumn
ex2aacCacheHitsTotal = _Ex2aacCacheHitsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 6),
    _Ex2aacCacheHitsTotal_Type()
)
ex2aacCacheHitsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheHitsTotal.setStatus("current")
_Ex2aacCacheHitsPerSec_Type = Gauge32
_Ex2aacCacheHitsPerSec_Object = MibTableColumn
ex2aacCacheHitsPerSec = _Ex2aacCacheHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 7),
    _Ex2aacCacheHitsPerSec_Type()
)
ex2aacCacheHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheHitsPerSec.setStatus("current")
_Ex2aacCacheInsertTotalConfigData_Type = Gauge32
_Ex2aacCacheInsertTotalConfigData_Object = MibTableColumn
ex2aacCacheInsertTotalConfigData = _Ex2aacCacheInsertTotalConfigData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 8),
    _Ex2aacCacheInsertTotalConfigData_Type()
)
ex2aacCacheInsertTotalConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheInsertTotalConfigData.setStatus("current")
_Ex2aacCacheInsertsTotalUserData_Type = Gauge32
_Ex2aacCacheInsertsTotalUserData_Object = MibTableColumn
ex2aacCacheInsertsTotalUserData = _Ex2aacCacheInsertsTotalUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 9),
    _Ex2aacCacheInsertsTotalUserData_Type()
)
ex2aacCacheInsertsTotalUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheInsertsTotalUserData.setStatus("current")
_Ex2aacCacheInsertSecConfigurData_Type = Gauge32
_Ex2aacCacheInsertSecConfigurData_Object = MibTableColumn
ex2aacCacheInsertSecConfigurData = _Ex2aacCacheInsertSecConfigurData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 10),
    _Ex2aacCacheInsertSecConfigurData_Type()
)
ex2aacCacheInsertSecConfigurData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheInsertSecConfigurData.setStatus("current")
_Ex2aacCacheInsertsPerSecUserData_Type = Gauge32
_Ex2aacCacheInsertsPerSecUserData_Object = MibTableColumn
ex2aacCacheInsertsPerSecUserData = _Ex2aacCacheInsertsPerSecUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 11),
    _Ex2aacCacheInsertsPerSecUserData_Type()
)
ex2aacCacheInsertsPerSecUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheInsertsPerSecUserData.setStatus("current")
_Ex2aacCacheMissesTotal_Type = Gauge32
_Ex2aacCacheMissesTotal_Object = MibTableColumn
ex2aacCacheMissesTotal = _Ex2aacCacheMissesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 12),
    _Ex2aacCacheMissesTotal_Type()
)
ex2aacCacheMissesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheMissesTotal.setStatus("current")
_Ex2aacCacheMissesPerSec_Type = Gauge32
_Ex2aacCacheMissesPerSec_Object = MibTableColumn
ex2aacCacheMissesPerSec = _Ex2aacCacheMissesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 13),
    _Ex2aacCacheMissesPerSec_Type()
)
ex2aacCacheMissesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacCacheMissesPerSec.setStatus("current")
_Ex2aacDNEntriesConfigurationData_Type = Gauge32
_Ex2aacDNEntriesConfigurationData_Object = MibTableColumn
ex2aacDNEntriesConfigurationData = _Ex2aacDNEntriesConfigurationData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 14),
    _Ex2aacDNEntriesConfigurationData_Type()
)
ex2aacDNEntriesConfigurationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacDNEntriesConfigurationData.setStatus("current")
_Ex2aacDNEntriesUserData_Type = Gauge32
_Ex2aacDNEntriesUserData_Object = MibTableColumn
ex2aacDNEntriesUserData = _Ex2aacDNEntriesUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 15),
    _Ex2aacDNEntriesUserData_Type()
)
ex2aacDNEntriesUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacDNEntriesUserData.setStatus("current")
_Ex2aacDNEntriesMemoryConfigData_Type = Gauge32
_Ex2aacDNEntriesMemoryConfigData_Object = MibTableColumn
ex2aacDNEntriesMemoryConfigData = _Ex2aacDNEntriesMemoryConfigData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 16),
    _Ex2aacDNEntriesMemoryConfigData_Type()
)
ex2aacDNEntriesMemoryConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacDNEntriesMemoryConfigData.setStatus("current")
_Ex2aacDNEntriesMemoryUserData_Type = Gauge32
_Ex2aacDNEntriesMemoryUserData_Object = MibTableColumn
ex2aacDNEntriesMemoryUserData = _Ex2aacDNEntriesMemoryUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 17),
    _Ex2aacDNEntriesMemoryUserData_Type()
)
ex2aacDNEntriesMemoryUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacDNEntriesMemoryUserData.setStatus("current")
_Ex2aacLDAPSearchesTotal_Type = Gauge32
_Ex2aacLDAPSearchesTotal_Object = MibTableColumn
ex2aacLDAPSearchesTotal = _Ex2aacLDAPSearchesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 18),
    _Ex2aacLDAPSearchesTotal_Type()
)
ex2aacLDAPSearchesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacLDAPSearchesTotal.setStatus("current")
_Ex2aacLDAPSearchesPerSec_Type = Gauge32
_Ex2aacLDAPSearchesPerSec_Object = MibTableColumn
ex2aacLDAPSearchesPerSec = _Ex2aacLDAPSearchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 19),
    _Ex2aacLDAPSearchesPerSec_Type()
)
ex2aacLDAPSearchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacLDAPSearchesPerSec.setStatus("current")
_Ex2aacNotFndDNEntriesConfigData_Type = Gauge32
_Ex2aacNotFndDNEntriesConfigData_Object = MibTableColumn
ex2aacNotFndDNEntriesConfigData = _Ex2aacNotFndDNEntriesConfigData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 20),
    _Ex2aacNotFndDNEntriesConfigData_Type()
)
ex2aacNotFndDNEntriesConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacNotFndDNEntriesConfigData.setStatus("current")
_Ex2aacNotFoundDNEntriesUserData_Type = Gauge32
_Ex2aacNotFoundDNEntriesUserData_Object = MibTableColumn
ex2aacNotFoundDNEntriesUserData = _Ex2aacNotFoundDNEntriesUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 21),
    _Ex2aacNotFoundDNEntriesUserData_Type()
)
ex2aacNotFoundDNEntriesUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacNotFoundDNEntriesUserData.setStatus("current")
_Ex2aacNotFndDNEntryMemConfigData_Type = Gauge32
_Ex2aacNotFndDNEntryMemConfigData_Object = MibTableColumn
ex2aacNotFndDNEntryMemConfigData = _Ex2aacNotFndDNEntryMemConfigData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 22),
    _Ex2aacNotFndDNEntryMemConfigData_Type()
)
ex2aacNotFndDNEntryMemConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacNotFndDNEntryMemConfigData.setStatus("current")
_Ex2aacNotFndDNEntriesMemUserData_Type = Gauge32
_Ex2aacNotFndDNEntriesMemUserData_Object = MibTableColumn
ex2aacNotFndDNEntriesMemUserData = _Ex2aacNotFndDNEntriesMemUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 23),
    _Ex2aacNotFndDNEntriesMemUserData_Type()
)
ex2aacNotFndDNEntriesMemUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacNotFndDNEntriesMemUserData.setStatus("current")
_Ex2aacNotFndGUIDEntryConfigData_Type = Gauge32
_Ex2aacNotFndGUIDEntryConfigData_Object = MibTableColumn
ex2aacNotFndGUIDEntryConfigData = _Ex2aacNotFndGUIDEntryConfigData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 24),
    _Ex2aacNotFndGUIDEntryConfigData_Type()
)
ex2aacNotFndGUIDEntryConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacNotFndGUIDEntryConfigData.setStatus("current")
_Ex2aacNotFndGUIDEntriesUserData_Type = Gauge32
_Ex2aacNotFndGUIDEntriesUserData_Object = MibTableColumn
ex2aacNotFndGUIDEntriesUserData = _Ex2aacNotFndGUIDEntriesUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 25),
    _Ex2aacNotFndGUIDEntriesUserData_Type()
)
ex2aacNotFndGUIDEntriesUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacNotFndGUIDEntriesUserData.setStatus("current")
_Ex2aacNotFndGUIDEntryMemConfigDa_Type = Gauge32
_Ex2aacNotFndGUIDEntryMemConfigDa_Object = MibTableColumn
ex2aacNotFndGUIDEntryMemConfigDa = _Ex2aacNotFndGUIDEntryMemConfigDa_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 26),
    _Ex2aacNotFndGUIDEntryMemConfigDa_Type()
)
ex2aacNotFndGUIDEntryMemConfigDa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacNotFndGUIDEntryMemConfigDa.setStatus("current")
_Ex2aacNotFndGUIDEntryMemUserData_Type = Gauge32
_Ex2aacNotFndGUIDEntryMemUserData_Object = MibTableColumn
ex2aacNotFndGUIDEntryMemUserData = _Ex2aacNotFndGUIDEntryMemUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 27),
    _Ex2aacNotFndGUIDEntryMemUserData_Type()
)
ex2aacNotFndGUIDEntryMemUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacNotFndGUIDEntryMemUserData.setStatus("current")
_Ex2aacOutstandingAsyncNotifies_Type = Gauge32
_Ex2aacOutstandingAsyncNotifies_Object = MibTableColumn
ex2aacOutstandingAsyncNotifies = _Ex2aacOutstandingAsyncNotifies_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 28),
    _Ex2aacOutstandingAsyncNotifies_Type()
)
ex2aacOutstandingAsyncNotifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacOutstandingAsyncNotifies.setStatus("current")
_Ex2aacOutstandingAsyncReads_Type = Gauge32
_Ex2aacOutstandingAsyncReads_Object = MibTableColumn
ex2aacOutstandingAsyncReads = _Ex2aacOutstandingAsyncReads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 29),
    _Ex2aacOutstandingAsyncReads_Type()
)
ex2aacOutstandingAsyncReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacOutstandingAsyncReads.setStatus("current")
_Ex2aacOutstandingAsyncSearches_Type = Gauge32
_Ex2aacOutstandingAsyncSearches_Object = MibTableColumn
ex2aacOutstandingAsyncSearches = _Ex2aacOutstandingAsyncSearches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 30),
    _Ex2aacOutstandingAsyncSearches_Type()
)
ex2aacOutstandingAsyncSearches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacOutstandingAsyncSearches.setStatus("current")
_Ex2aacSearchEntriesConfigData_Type = Gauge32
_Ex2aacSearchEntriesConfigData_Object = MibTableColumn
ex2aacSearchEntriesConfigData = _Ex2aacSearchEntriesConfigData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 31),
    _Ex2aacSearchEntriesConfigData_Type()
)
ex2aacSearchEntriesConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacSearchEntriesConfigData.setStatus("current")
_Ex2aacSearchEntriesUserData_Type = Gauge32
_Ex2aacSearchEntriesUserData_Object = MibTableColumn
ex2aacSearchEntriesUserData = _Ex2aacSearchEntriesUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 32),
    _Ex2aacSearchEntriesUserData_Type()
)
ex2aacSearchEntriesUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacSearchEntriesUserData.setStatus("current")
_Ex2aacSearchEntriesMemConfigData_Type = Gauge32
_Ex2aacSearchEntriesMemConfigData_Object = MibTableColumn
ex2aacSearchEntriesMemConfigData = _Ex2aacSearchEntriesMemConfigData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 33),
    _Ex2aacSearchEntriesMemConfigData_Type()
)
ex2aacSearchEntriesMemConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacSearchEntriesMemConfigData.setStatus("current")
_Ex2aacSearchEntryMemoryUserData_Type = Gauge32
_Ex2aacSearchEntryMemoryUserData_Object = MibTableColumn
ex2aacSearchEntryMemoryUserData = _Ex2aacSearchEntryMemoryUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 34),
    _Ex2aacSearchEntryMemoryUserData_Type()
)
ex2aacSearchEntryMemoryUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacSearchEntryMemoryUserData.setStatus("current")
_Ex2aacTotalEntriesConfigData_Type = Gauge32
_Ex2aacTotalEntriesConfigData_Object = MibTableColumn
ex2aacTotalEntriesConfigData = _Ex2aacTotalEntriesConfigData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 35),
    _Ex2aacTotalEntriesConfigData_Type()
)
ex2aacTotalEntriesConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacTotalEntriesConfigData.setStatus("current")
_Ex2aacTotalEntriesUserData_Type = Gauge32
_Ex2aacTotalEntriesUserData_Object = MibTableColumn
ex2aacTotalEntriesUserData = _Ex2aacTotalEntriesUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 36),
    _Ex2aacTotalEntriesUserData_Type()
)
ex2aacTotalEntriesUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacTotalEntriesUserData.setStatus("current")
_Ex2aacTotalEntriesMemConfigData_Type = Gauge32
_Ex2aacTotalEntriesMemConfigData_Object = MibTableColumn
ex2aacTotalEntriesMemConfigData = _Ex2aacTotalEntriesMemConfigData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 37),
    _Ex2aacTotalEntriesMemConfigData_Type()
)
ex2aacTotalEntriesMemConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacTotalEntriesMemConfigData.setStatus("current")
_Ex2aacTotalEntriesMemoryUserData_Type = Gauge32
_Ex2aacTotalEntriesMemoryUserData_Object = MibTableColumn
ex2aacTotalEntriesMemoryUserData = _Ex2aacTotalEntriesMemoryUserData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 2, 1, 38),
    _Ex2aacTotalEntriesMemoryUserData_Type()
)
ex2aacTotalEntriesMemoryUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aacTotalEntriesMemoryUserData.setStatus("current")
_Ex2ADAccessDomainControllerTable_Object = MibTable
ex2ADAccessDomainControllerTable = _Ex2ADAccessDomainControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3)
)
if mibBuilder.loadTexts:
    ex2ADAccessDomainControllerTable.setStatus("current")
_Ex2ADAccessDomainControllerEntry_Object = MibTableRow
ex2ADAccessDomainControllerEntry = _Ex2ADAccessDomainControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1)
)
ex2ADAccessDomainControllerEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2aadcInstance"),
)
if mibBuilder.loadTexts:
    ex2ADAccessDomainControllerEntry.setStatus("current")
_Ex2aadcInstance_Type = InstanceName
_Ex2aadcInstance_Object = MibTableColumn
ex2aadcInstance = _Ex2aadcInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 1),
    _Ex2aadcInstance_Type()
)
ex2aadcInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcInstance.setStatus("current")
_Ex2aadcBindFailuresPerMinute_Type = Gauge32
_Ex2aadcBindFailuresPerMinute_Object = MibTableColumn
ex2aadcBindFailuresPerMinute = _Ex2aadcBindFailuresPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 2),
    _Ex2aadcBindFailuresPerMinute_Type()
)
ex2aadcBindFailuresPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcBindFailuresPerMinute.setStatus("current")
_Ex2aadcCriticalDataFlag_Type = Gauge32
_Ex2aadcCriticalDataFlag_Object = MibTableColumn
ex2aadcCriticalDataFlag = _Ex2aadcCriticalDataFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 3),
    _Ex2aadcCriticalDataFlag_Type()
)
ex2aadcCriticalDataFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcCriticalDataFlag.setStatus("current")
_Ex2aadcDsGetDcNameElapsedTime_Type = Gauge32
_Ex2aadcDsGetDcNameElapsedTime_Object = MibTableColumn
ex2aadcDsGetDcNameElapsedTime = _Ex2aadcDsGetDcNameElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 4),
    _Ex2aadcDsGetDcNameElapsedTime_Type()
)
ex2aadcDsGetDcNameElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcDsGetDcNameElapsedTime.setStatus("current")
_Ex2aadcGCCapableFlag_Type = Gauge32
_Ex2aadcGCCapableFlag_Object = MibTableColumn
ex2aadcGCCapableFlag = _Ex2aadcGCCapableFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 5),
    _Ex2aadcGCCapableFlag_Type()
)
ex2aadcGCCapableFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcGCCapableFlag.setStatus("current")
_Ex2aadcIsSynchronizedFlag_Type = Gauge32
_Ex2aadcIsSynchronizedFlag_Object = MibTableColumn
ex2aadcIsSynchronizedFlag = _Ex2aadcIsSynchronizedFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 6),
    _Ex2aadcIsSynchronizedFlag_Type()
)
ex2aadcIsSynchronizedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcIsSynchronizedFlag.setStatus("current")
_Ex2aadcKerberosTicketLifetime_Type = Gauge32
_Ex2aadcKerberosTicketLifetime_Object = MibTableColumn
ex2aadcKerberosTicketLifetime = _Ex2aadcKerberosTicketLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 7),
    _Ex2aadcKerberosTicketLifetime_Type()
)
ex2aadcKerberosTicketLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcKerberosTicketLifetime.setStatus("current")
_Ex2aadcLDAPDisconnectsPerMinute_Type = Gauge32
_Ex2aadcLDAPDisconnectsPerMinute_Object = MibTableColumn
ex2aadcLDAPDisconnectsPerMinute = _Ex2aadcLDAPDisconnectsPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 8),
    _Ex2aadcLDAPDisconnectsPerMinute_Type()
)
ex2aadcLDAPDisconnectsPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLDAPDisconnectsPerMinute.setStatus("current")
_Ex2aadcLDAPFatalErrorsPerMinute_Type = Gauge32
_Ex2aadcLDAPFatalErrorsPerMinute_Object = MibTableColumn
ex2aadcLDAPFatalErrorsPerMinute = _Ex2aadcLDAPFatalErrorsPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 9),
    _Ex2aadcLDAPFatalErrorsPerMinute_Type()
)
ex2aadcLDAPFatalErrorsPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLDAPFatalErrorsPerMinute.setStatus("current")
_Ex2aadcLDAPPagesPerSec_Type = Gauge32
_Ex2aadcLDAPPagesPerSec_Object = MibTableColumn
ex2aadcLDAPPagesPerSec = _Ex2aadcLDAPPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 10),
    _Ex2aadcLDAPPagesPerSec_Type()
)
ex2aadcLDAPPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLDAPPagesPerSec.setStatus("current")
_Ex2aadcLDAPReadTime_Type = Gauge32
_Ex2aadcLDAPReadTime_Object = MibTableColumn
ex2aadcLDAPReadTime = _Ex2aadcLDAPReadTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 11),
    _Ex2aadcLDAPReadTime_Type()
)
ex2aadcLDAPReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLDAPReadTime.setStatus("current")
_Ex2aadcLDAPReadCallsPerSec_Type = Gauge32
_Ex2aadcLDAPReadCallsPerSec_Object = MibTableColumn
ex2aadcLDAPReadCallsPerSec = _Ex2aadcLDAPReadCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 12),
    _Ex2aadcLDAPReadCallsPerSec_Type()
)
ex2aadcLDAPReadCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLDAPReadCallsPerSec.setStatus("current")
_Ex2aadcLDAPSearchTime_Type = Gauge32
_Ex2aadcLDAPSearchTime_Object = MibTableColumn
ex2aadcLDAPSearchTime = _Ex2aadcLDAPSearchTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 13),
    _Ex2aadcLDAPSearchTime_Type()
)
ex2aadcLDAPSearchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLDAPSearchTime.setStatus("current")
_Ex2aadcLDAPSearchCallsPerSec_Type = Gauge32
_Ex2aadcLDAPSearchCallsPerSec_Object = MibTableColumn
ex2aadcLDAPSearchCallsPerSec = _Ex2aadcLDAPSearchCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 14),
    _Ex2aadcLDAPSearchCallsPerSec_Type()
)
ex2aadcLDAPSearchCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLDAPSearchCallsPerSec.setStatus("current")
_Ex2aadcLDAPSearchTimedOutPerMin_Type = Gauge32
_Ex2aadcLDAPSearchTimedOutPerMin_Object = MibTableColumn
ex2aadcLDAPSearchTimedOutPerMin = _Ex2aadcLDAPSearchTimedOutPerMin_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 15),
    _Ex2aadcLDAPSearchTimedOutPerMin_Type()
)
ex2aadcLDAPSearchTimedOutPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLDAPSearchTimedOutPerMin.setStatus("current")
_Ex2aadcLDAPVLVRequestsPerSec_Type = Gauge32
_Ex2aadcLDAPVLVRequestsPerSec_Object = MibTableColumn
ex2aadcLDAPVLVRequestsPerSec = _Ex2aadcLDAPVLVRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 16),
    _Ex2aadcLDAPVLVRequestsPerSec_Type()
)
ex2aadcLDAPVLVRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLDAPVLVRequestsPerSec.setStatus("current")
_Ex2aadcLDAPConnectionLifetime_Type = Gauge32
_Ex2aadcLDAPConnectionLifetime_Object = MibTableColumn
ex2aadcLDAPConnectionLifetime = _Ex2aadcLDAPConnectionLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 17),
    _Ex2aadcLDAPConnectionLifetime_Type()
)
ex2aadcLDAPConnectionLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLDAPConnectionLifetime.setStatus("current")
_Ex2aadcLocalSiteFlag_Type = Gauge32
_Ex2aadcLocalSiteFlag_Object = MibTableColumn
ex2aadcLocalSiteFlag = _Ex2aadcLocalSiteFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 18),
    _Ex2aadcLocalSiteFlag_Type()
)
ex2aadcLocalSiteFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLocalSiteFlag.setStatus("current")
_Ex2aadcLongRunningLDAPOperPerMin_Type = Gauge32
_Ex2aadcLongRunningLDAPOperPerMin_Object = MibTableColumn
ex2aadcLongRunningLDAPOperPerMin = _Ex2aadcLongRunningLDAPOperPerMin_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 19),
    _Ex2aadcLongRunningLDAPOperPerMin_Type()
)
ex2aadcLongRunningLDAPOperPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcLongRunningLDAPOperPerMin.setStatus("current")
_Ex2aadcNetlogonFlag_Type = Gauge32
_Ex2aadcNetlogonFlag_Object = MibTableColumn
ex2aadcNetlogonFlag = _Ex2aadcNetlogonFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 20),
    _Ex2aadcNetlogonFlag_Type()
)
ex2aadcNetlogonFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcNetlogonFlag.setStatus("current")
_Ex2aadcNumberOfOutstandRequests_Type = Gauge32
_Ex2aadcNumberOfOutstandRequests_Object = MibTableColumn
ex2aadcNumberOfOutstandRequests = _Ex2aadcNumberOfOutstandRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 21),
    _Ex2aadcNumberOfOutstandRequests_Type()
)
ex2aadcNumberOfOutstandRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcNumberOfOutstandRequests.setStatus("current")
_Ex2aadcOSVersionFlag_Type = Gauge32
_Ex2aadcOSVersionFlag_Object = MibTableColumn
ex2aadcOSVersionFlag = _Ex2aadcOSVersionFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 22),
    _Ex2aadcOSVersionFlag_Type()
)
ex2aadcOSVersionFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcOSVersionFlag.setStatus("current")
_Ex2aadcPDCFlag_Type = Gauge32
_Ex2aadcPDCFlag_Object = MibTableColumn
ex2aadcPDCFlag = _Ex2aadcPDCFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 23),
    _Ex2aadcPDCFlag_Type()
)
ex2aadcPDCFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcPDCFlag.setStatus("current")
_Ex2aadcReachabilityBitmask_Type = Gauge32
_Ex2aadcReachabilityBitmask_Object = MibTableColumn
ex2aadcReachabilityBitmask = _Ex2aadcReachabilityBitmask_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 24),
    _Ex2aadcReachabilityBitmask_Type()
)
ex2aadcReachabilityBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcReachabilityBitmask.setStatus("current")
_Ex2aadcSACLRightFlag_Type = Gauge32
_Ex2aadcSACLRightFlag_Object = MibTableColumn
ex2aadcSACLRightFlag = _Ex2aadcSACLRightFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 25),
    _Ex2aadcSACLRightFlag_Type()
)
ex2aadcSACLRightFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcSACLRightFlag.setStatus("current")
_Ex2aadcUserSearchesFailPerMinute_Type = Gauge32
_Ex2aadcUserSearchesFailPerMinute_Object = MibTableColumn
ex2aadcUserSearchesFailPerMinute = _Ex2aadcUserSearchesFailPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 26),
    _Ex2aadcUserSearchesFailPerMinute_Type()
)
ex2aadcUserSearchesFailPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcUserSearchesFailPerMinute.setStatus("current")
_Ex2aadcGethostbynameElapsedTime_Type = Gauge32
_Ex2aadcGethostbynameElapsedTime_Object = MibTableColumn
ex2aadcGethostbynameElapsedTime = _Ex2aadcGethostbynameElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 3, 1, 27),
    _Ex2aadcGethostbynameElapsedTime_Type()
)
ex2aadcGethostbynameElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aadcGethostbynameElapsedTime.setStatus("current")
_Ex2ADAccessGlobalCounters_ObjectIdentity = ObjectIdentity
ex2ADAccessGlobalCounters = _Ex2ADAccessGlobalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 4)
)
if mibBuilder.loadTexts:
    ex2ADAccessGlobalCounters.setStatus("current")
_Ex2aagcDNSQueryDurationTime_Type = Gauge32
_Ex2aagcDNSQueryDurationTime_Object = MibScalar
ex2aagcDNSQueryDurationTime = _Ex2aagcDNSQueryDurationTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 4, 1),
    _Ex2aagcDNSQueryDurationTime_Type()
)
ex2aagcDNSQueryDurationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aagcDNSQueryDurationTime.setStatus("current")
_Ex2aagcInSiteDomainControllers_Type = Gauge32
_Ex2aagcInSiteDomainControllers_Object = MibScalar
ex2aagcInSiteDomainControllers = _Ex2aagcInSiteDomainControllers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 4, 2),
    _Ex2aagcInSiteDomainControllers_Type()
)
ex2aagcInSiteDomainControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aagcInSiteDomainControllers.setStatus("current")
_Ex2aagcInSiteGlobalCatalogs_Type = Gauge32
_Ex2aagcInSiteGlobalCatalogs_Object = MibScalar
ex2aagcInSiteGlobalCatalogs = _Ex2aagcInSiteGlobalCatalogs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 4, 3),
    _Ex2aagcInSiteGlobalCatalogs_Type()
)
ex2aagcInSiteGlobalCatalogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aagcInSiteGlobalCatalogs.setStatus("current")
_Ex2aagcOutOfSiteDomainController_Type = Gauge32
_Ex2aagcOutOfSiteDomainController_Object = MibScalar
ex2aagcOutOfSiteDomainController = _Ex2aagcOutOfSiteDomainController_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 4, 4),
    _Ex2aagcOutOfSiteDomainController_Type()
)
ex2aagcOutOfSiteDomainController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aagcOutOfSiteDomainController.setStatus("current")
_Ex2aagcOutOfSiteGlobalCatalogs_Type = Gauge32
_Ex2aagcOutOfSiteGlobalCatalogs_Object = MibScalar
ex2aagcOutOfSiteGlobalCatalogs = _Ex2aagcOutOfSiteGlobalCatalogs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 4, 5),
    _Ex2aagcOutOfSiteGlobalCatalogs_Type()
)
ex2aagcOutOfSiteGlobalCatalogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aagcOutOfSiteGlobalCatalogs.setStatus("current")
_Ex2aagcTopologyDiscoveryDuraTime_Type = Gauge32
_Ex2aagcTopologyDiscoveryDuraTime_Object = MibScalar
ex2aagcTopologyDiscoveryDuraTime = _Ex2aagcTopologyDiscoveryDuraTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 4, 6),
    _Ex2aagcTopologyDiscoveryDuraTime_Type()
)
ex2aagcTopologyDiscoveryDuraTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aagcTopologyDiscoveryDuraTime.setStatus("current")
_Ex2ADAccessProcessesTable_Object = MibTable
ex2ADAccessProcessesTable = _Ex2ADAccessProcessesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5)
)
if mibBuilder.loadTexts:
    ex2ADAccessProcessesTable.setStatus("current")
_Ex2ADAccessProcessesEntry_Object = MibTableRow
ex2ADAccessProcessesEntry = _Ex2ADAccessProcessesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1)
)
ex2ADAccessProcessesEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2aapInstance"),
)
if mibBuilder.loadTexts:
    ex2ADAccessProcessesEntry.setStatus("current")
_Ex2aapInstance_Type = InstanceName
_Ex2aapInstance_Object = MibTableColumn
ex2aapInstance = _Ex2aapInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 1),
    _Ex2aapInstance_Type()
)
ex2aapInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapInstance.setStatus("current")
_Ex2aapCriticlValidFailuresPerMin_Type = Gauge32
_Ex2aapCriticlValidFailuresPerMin_Object = MibTableColumn
ex2aapCriticlValidFailuresPerMin = _Ex2aapCriticlValidFailuresPerMin_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 2),
    _Ex2aapCriticlValidFailuresPerMin_Type()
)
ex2aapCriticlValidFailuresPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapCriticlValidFailuresPerMin.setStatus("current")
_Ex2aapIgnorValidatFailuresPerMin_Type = Gauge32
_Ex2aapIgnorValidatFailuresPerMin_Object = MibTableColumn
ex2aapIgnorValidatFailuresPerMin = _Ex2aapIgnorValidatFailuresPerMin_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 3),
    _Ex2aapIgnorValidatFailuresPerMin_Type()
)
ex2aapIgnorValidatFailuresPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapIgnorValidatFailuresPerMin.setStatus("current")
_Ex2aapLDAPNotFndConfigRdCallSec_Type = Gauge32
_Ex2aapLDAPNotFndConfigRdCallSec_Object = MibTableColumn
ex2aapLDAPNotFndConfigRdCallSec = _Ex2aapLDAPNotFndConfigRdCallSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 4),
    _Ex2aapLDAPNotFndConfigRdCallSec_Type()
)
ex2aapLDAPNotFndConfigRdCallSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPNotFndConfigRdCallSec.setStatus("current")
_Ex2aapLDAPPagesPerSec_Type = Gauge32
_Ex2aapLDAPPagesPerSec_Object = MibTableColumn
ex2aapLDAPPagesPerSec = _Ex2aapLDAPPagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 5),
    _Ex2aapLDAPPagesPerSec_Type()
)
ex2aapLDAPPagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPPagesPerSec.setStatus("current")
_Ex2aapLDAPReadTime_Type = Gauge32
_Ex2aapLDAPReadTime_Object = MibTableColumn
ex2aapLDAPReadTime = _Ex2aapLDAPReadTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 6),
    _Ex2aapLDAPReadTime_Type()
)
ex2aapLDAPReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPReadTime.setStatus("current")
_Ex2aapLDAPReadCallsPerSec_Type = Gauge32
_Ex2aapLDAPReadCallsPerSec_Object = MibTableColumn
ex2aapLDAPReadCallsPerSec = _Ex2aapLDAPReadCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 7),
    _Ex2aapLDAPReadCallsPerSec_Type()
)
ex2aapLDAPReadCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPReadCallsPerSec.setStatus("current")
_Ex2aapLDAPSearchTime_Type = Gauge32
_Ex2aapLDAPSearchTime_Object = MibTableColumn
ex2aapLDAPSearchTime = _Ex2aapLDAPSearchTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 8),
    _Ex2aapLDAPSearchTime_Type()
)
ex2aapLDAPSearchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPSearchTime.setStatus("current")
_Ex2aapLDAPSearchCallsPerSec_Type = Gauge32
_Ex2aapLDAPSearchCallsPerSec_Object = MibTableColumn
ex2aapLDAPSearchCallsPerSec = _Ex2aapLDAPSearchCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 9),
    _Ex2aapLDAPSearchCallsPerSec_Type()
)
ex2aapLDAPSearchCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPSearchCallsPerSec.setStatus("current")
_Ex2aapLDAPTimeoutErrorsPerSec_Type = Gauge32
_Ex2aapLDAPTimeoutErrorsPerSec_Object = MibTableColumn
ex2aapLDAPTimeoutErrorsPerSec = _Ex2aapLDAPTimeoutErrorsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 10),
    _Ex2aapLDAPTimeoutErrorsPerSec_Type()
)
ex2aapLDAPTimeoutErrorsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPTimeoutErrorsPerSec.setStatus("current")
_Ex2aapLDAPVLVRequestsPerSec_Type = Gauge32
_Ex2aapLDAPVLVRequestsPerSec_Object = MibTableColumn
ex2aapLDAPVLVRequestsPerSec = _Ex2aapLDAPVLVRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 11),
    _Ex2aapLDAPVLVRequestsPerSec_Type()
)
ex2aapLDAPVLVRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPVLVRequestsPerSec.setStatus("current")
_Ex2aapLDAPWriteTime_Type = Gauge32
_Ex2aapLDAPWriteTime_Object = MibTableColumn
ex2aapLDAPWriteTime = _Ex2aapLDAPWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 12),
    _Ex2aapLDAPWriteTime_Type()
)
ex2aapLDAPWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPWriteTime.setStatus("current")
_Ex2aapLDAPWriteCallsPerSec_Type = Gauge32
_Ex2aapLDAPWriteCallsPerSec_Object = MibTableColumn
ex2aapLDAPWriteCallsPerSec = _Ex2aapLDAPWriteCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 13),
    _Ex2aapLDAPWriteCallsPerSec_Type()
)
ex2aapLDAPWriteCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPWriteCallsPerSec.setStatus("current")
_Ex2aapLDAPNotificaReportedPerSec_Type = Gauge32
_Ex2aapLDAPNotificaReportedPerSec_Object = MibTableColumn
ex2aapLDAPNotificaReportedPerSec = _Ex2aapLDAPNotificaReportedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 14),
    _Ex2aapLDAPNotificaReportedPerSec_Type()
)
ex2aapLDAPNotificaReportedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPNotificaReportedPerSec.setStatus("current")
_Ex2aapLDAPNotificaReceivedPerSec_Type = Gauge32
_Ex2aapLDAPNotificaReceivedPerSec_Object = MibTableColumn
ex2aapLDAPNotificaReceivedPerSec = _Ex2aapLDAPNotificaReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 15),
    _Ex2aapLDAPNotificaReceivedPerSec_Type()
)
ex2aapLDAPNotificaReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLDAPNotificaReceivedPerSec.setStatus("current")
_Ex2aapLongRunningLDAPOperaPerMin_Type = Gauge32
_Ex2aapLongRunningLDAPOperaPerMin_Object = MibTableColumn
ex2aapLongRunningLDAPOperaPerMin = _Ex2aapLongRunningLDAPOperaPerMin_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 16),
    _Ex2aapLongRunningLDAPOperaPerMin_Type()
)
ex2aapLongRunningLDAPOperaPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapLongRunningLDAPOperaPerMin.setStatus("current")
_Ex2aapNonCriticalValidFailPerMin_Type = Gauge32
_Ex2aapNonCriticalValidFailPerMin_Object = MibTableColumn
ex2aapNonCriticalValidFailPerMin = _Ex2aapNonCriticalValidFailPerMin_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 17),
    _Ex2aapNonCriticalValidFailPerMin_Type()
)
ex2aapNonCriticalValidFailPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapNonCriticalValidFailPerMin.setStatus("current")
_Ex2aapNumberOfOutstandingRequest_Type = Gauge32
_Ex2aapNumberOfOutstandingRequest_Object = MibTableColumn
ex2aapNumberOfOutstandingRequest = _Ex2aapNumberOfOutstandingRequest_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 18),
    _Ex2aapNumberOfOutstandingRequest_Type()
)
ex2aapNumberOfOutstandingRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapNumberOfOutstandingRequest.setStatus("current")
_Ex2aapOpenConnectionToDomainCtrl_Type = Gauge32
_Ex2aapOpenConnectionToDomainCtrl_Object = MibTableColumn
ex2aapOpenConnectionToDomainCtrl = _Ex2aapOpenConnectionToDomainCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 19),
    _Ex2aapOpenConnectionToDomainCtrl_Type()
)
ex2aapOpenConnectionToDomainCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapOpenConnectionToDomainCtrl.setStatus("current")
_Ex2aapOpenConnectionsToGlobalCat_Type = Gauge32
_Ex2aapOpenConnectionsToGlobalCat_Object = MibTableColumn
ex2aapOpenConnectionsToGlobalCat = _Ex2aapOpenConnectionsToGlobalCat_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 20),
    _Ex2aapOpenConnectionsToGlobalCat_Type()
)
ex2aapOpenConnectionsToGlobalCat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapOpenConnectionsToGlobalCat.setStatus("current")
_Ex2aapProcessID_Type = Gauge32
_Ex2aapProcessID_Object = MibTableColumn
ex2aapProcessID = _Ex2aapProcessID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 21),
    _Ex2aapProcessID_Type()
)
ex2aapProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapProcessID.setStatus("current")
_Ex2aapTopologyVersion_Type = Gauge32
_Ex2aapTopologyVersion_Object = MibTableColumn
ex2aapTopologyVersion = _Ex2aapTopologyVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 5, 1, 22),
    _Ex2aapTopologyVersion_Type()
)
ex2aapTopologyVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aapTopologyVersion.setStatus("current")
_Ex2ActiveSync_ObjectIdentity = ObjectIdentity
ex2ActiveSync = _Ex2ActiveSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6)
)
if mibBuilder.loadTexts:
    ex2ActiveSync.setStatus("current")
_Ex2asAveragePingTime_Type = Gauge32
_Ex2asAveragePingTime_Object = MibScalar
ex2asAveragePingTime = _Ex2asAveragePingTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 1),
    _Ex2asAveragePingTime_Type()
)
ex2asAveragePingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asAveragePingTime.setStatus("current")
_Ex2asAverageRequestTime_Type = Gauge32
_Ex2asAverageRequestTime_Object = MibScalar
ex2asAverageRequestTime = _Ex2asAverageRequestTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 2),
    _Ex2asAverageRequestTime_Type()
)
ex2asAverageRequestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asAverageRequestTime.setStatus("current")
_Ex2asBadItemReportGeneratedTotal_Type = Gauge32
_Ex2asBadItemReportGeneratedTotal_Object = MibScalar
ex2asBadItemReportGeneratedTotal = _Ex2asBadItemReportGeneratedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 3),
    _Ex2asBadItemReportGeneratedTotal_Type()
)
ex2asBadItemReportGeneratedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asBadItemReportGeneratedTotal.setStatus("current")
_Ex2asBusyThreads_Type = Gauge32
_Ex2asBusyThreads_Object = MibScalar
ex2asBusyThreads = _Ex2asBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 4),
    _Ex2asBusyThreads_Type()
)
ex2asBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asBusyThreads.setStatus("current")
_Ex2asConflictConcurrentSyncTotal_Type = Gauge32
_Ex2asConflictConcurrentSyncTotal_Object = MibScalar
ex2asConflictConcurrentSyncTotal = _Ex2asConflictConcurrentSyncTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 5),
    _Ex2asConflictConcurrentSyncTotal_Type()
)
ex2asConflictConcurrentSyncTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asConflictConcurrentSyncTotal.setStatus("current")
_Ex2asConflictConcurrentSyncPrSec_Type = Gauge32
_Ex2asConflictConcurrentSyncPrSec_Object = MibScalar
ex2asConflictConcurrentSyncPrSec = _Ex2asConflictConcurrentSyncPrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 6),
    _Ex2asConflictConcurrentSyncPrSec_Type()
)
ex2asConflictConcurrentSyncPrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asConflictConcurrentSyncPrSec.setStatus("current")
_Ex2asCreateCollectionCommandsSec_Type = Gauge32
_Ex2asCreateCollectionCommandsSec_Object = MibScalar
ex2asCreateCollectionCommandsSec = _Ex2asCreateCollectionCommandsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 7),
    _Ex2asCreateCollectionCommandsSec_Type()
)
ex2asCreateCollectionCommandsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asCreateCollectionCommandsSec.setStatus("current")
_Ex2asCreateCollectionTotal_Type = Gauge32
_Ex2asCreateCollectionTotal_Object = MibScalar
ex2asCreateCollectionTotal = _Ex2asCreateCollectionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 8),
    _Ex2asCreateCollectionTotal_Type()
)
ex2asCreateCollectionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asCreateCollectionTotal.setStatus("current")
_Ex2asCurrentRequests_Type = Gauge32
_Ex2asCurrentRequests_Object = MibScalar
ex2asCurrentRequests = _Ex2asCurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 9),
    _Ex2asCurrentRequests_Type()
)
ex2asCurrentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asCurrentRequests.setStatus("current")
_Ex2asDeleteCollectionCommandsSec_Type = Gauge32
_Ex2asDeleteCollectionCommandsSec_Object = MibScalar
ex2asDeleteCollectionCommandsSec = _Ex2asDeleteCollectionCommandsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 10),
    _Ex2asDeleteCollectionCommandsSec_Type()
)
ex2asDeleteCollectionCommandsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asDeleteCollectionCommandsSec.setStatus("current")
_Ex2asDeleteCollectionTotal_Type = Gauge32
_Ex2asDeleteCollectionTotal_Object = MibScalar
ex2asDeleteCollectionTotal = _Ex2asDeleteCollectionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 11),
    _Ex2asDeleteCollectionTotal_Type()
)
ex2asDeleteCollectionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asDeleteCollectionTotal.setStatus("current")
_Ex2asDocuLibraryFetchCommandsSec_Type = Gauge32
_Ex2asDocuLibraryFetchCommandsSec_Object = MibScalar
ex2asDocuLibraryFetchCommandsSec = _Ex2asDocuLibraryFetchCommandsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 12),
    _Ex2asDocuLibraryFetchCommandsSec_Type()
)
ex2asDocuLibraryFetchCommandsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asDocuLibraryFetchCommandsSec.setStatus("current")
_Ex2asDocumentLibraryFetchTotal_Type = Gauge32
_Ex2asDocumentLibraryFetchTotal_Object = MibScalar
ex2asDocumentLibraryFetchTotal = _Ex2asDocumentLibraryFetchTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 13),
    _Ex2asDocumentLibraryFetchTotal_Type()
)
ex2asDocumentLibraryFetchTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asDocumentLibraryFetchTotal.setStatus("current")
_Ex2asDocumentLibrarySearchTotal_Type = Gauge32
_Ex2asDocumentLibrarySearchTotal_Object = MibScalar
ex2asDocumentLibrarySearchTotal = _Ex2asDocumentLibrarySearchTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 14),
    _Ex2asDocumentLibrarySearchTotal_Type()
)
ex2asDocumentLibrarySearchTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asDocumentLibrarySearchTotal.setStatus("current")
_Ex2asDocumentLibrarySearchPerSec_Type = Gauge32
_Ex2asDocumentLibrarySearchPerSec_Object = MibScalar
ex2asDocumentLibrarySearchPerSec = _Ex2asDocumentLibrarySearchPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 15),
    _Ex2asDocumentLibrarySearchPerSec_Type()
)
ex2asDocumentLibrarySearchPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asDocumentLibrarySearchPerSec.setStatus("current")
_Ex2asEmptyFolderContentsTotal_Type = Gauge32
_Ex2asEmptyFolderContentsTotal_Object = MibScalar
ex2asEmptyFolderContentsTotal = _Ex2asEmptyFolderContentsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 16),
    _Ex2asEmptyFolderContentsTotal_Type()
)
ex2asEmptyFolderContentsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asEmptyFolderContentsTotal.setStatus("current")
_Ex2asFailedItemConversionTotal_Type = Gauge32
_Ex2asFailedItemConversionTotal_Object = MibScalar
ex2asFailedItemConversionTotal = _Ex2asFailedItemConversionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 17),
    _Ex2asFailedItemConversionTotal_Type()
)
ex2asFailedItemConversionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asFailedItemConversionTotal.setStatus("current")
_Ex2asFolderCreateCommandsPerSec_Type = Gauge32
_Ex2asFolderCreateCommandsPerSec_Object = MibScalar
ex2asFolderCreateCommandsPerSec = _Ex2asFolderCreateCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 18),
    _Ex2asFolderCreateCommandsPerSec_Type()
)
ex2asFolderCreateCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asFolderCreateCommandsPerSec.setStatus("current")
_Ex2asFolderCreateTotal_Type = Gauge32
_Ex2asFolderCreateTotal_Object = MibScalar
ex2asFolderCreateTotal = _Ex2asFolderCreateTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 19),
    _Ex2asFolderCreateTotal_Type()
)
ex2asFolderCreateTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asFolderCreateTotal.setStatus("current")
_Ex2asFolderDeleteCommandsPerSec_Type = Gauge32
_Ex2asFolderDeleteCommandsPerSec_Object = MibScalar
ex2asFolderDeleteCommandsPerSec = _Ex2asFolderDeleteCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 20),
    _Ex2asFolderDeleteCommandsPerSec_Type()
)
ex2asFolderDeleteCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asFolderDeleteCommandsPerSec.setStatus("current")
_Ex2asFolderDeleteTotal_Type = Gauge32
_Ex2asFolderDeleteTotal_Object = MibScalar
ex2asFolderDeleteTotal = _Ex2asFolderDeleteTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 21),
    _Ex2asFolderDeleteTotal_Type()
)
ex2asFolderDeleteTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asFolderDeleteTotal.setStatus("current")
_Ex2asFolderSyncCommandsPerSec_Type = Gauge32
_Ex2asFolderSyncCommandsPerSec_Object = MibScalar
ex2asFolderSyncCommandsPerSec = _Ex2asFolderSyncCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 22),
    _Ex2asFolderSyncCommandsPerSec_Type()
)
ex2asFolderSyncCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asFolderSyncCommandsPerSec.setStatus("current")
_Ex2asFolderSyncTotal_Type = Gauge32
_Ex2asFolderSyncTotal_Object = MibScalar
ex2asFolderSyncTotal = _Ex2asFolderSyncTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 23),
    _Ex2asFolderSyncTotal_Type()
)
ex2asFolderSyncTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asFolderSyncTotal.setStatus("current")
_Ex2asFolderUpdateCommandsPerSec_Type = Gauge32
_Ex2asFolderUpdateCommandsPerSec_Object = MibScalar
ex2asFolderUpdateCommandsPerSec = _Ex2asFolderUpdateCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 24),
    _Ex2asFolderUpdateCommandsPerSec_Type()
)
ex2asFolderUpdateCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asFolderUpdateCommandsPerSec.setStatus("current")
_Ex2asFolderUpdateTotal_Type = Gauge32
_Ex2asFolderUpdateTotal_Object = MibScalar
ex2asFolderUpdateTotal = _Ex2asFolderUpdateTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 25),
    _Ex2asFolderUpdateTotal_Type()
)
ex2asFolderUpdateTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asFolderUpdateTotal.setStatus("current")
_Ex2asGALSearchTotal_Type = Gauge32
_Ex2asGALSearchTotal_Object = MibScalar
ex2asGALSearchTotal = _Ex2asGALSearchTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 26),
    _Ex2asGALSearchTotal_Type()
)
ex2asGALSearchTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asGALSearchTotal.setStatus("current")
_Ex2asGALSearchesPerSec_Type = Gauge32
_Ex2asGALSearchesPerSec_Object = MibScalar
ex2asGALSearchesPerSec = _Ex2asGALSearchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 27),
    _Ex2asGALSearchesPerSec_Type()
)
ex2asGALSearchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asGALSearchesPerSec.setStatus("current")
_Ex2asGetAttachmentCommandsPerSec_Type = Gauge32
_Ex2asGetAttachmentCommandsPerSec_Object = MibScalar
ex2asGetAttachmentCommandsPerSec = _Ex2asGetAttachmentCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 28),
    _Ex2asGetAttachmentCommandsPerSec_Type()
)
ex2asGetAttachmentCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asGetAttachmentCommandsPerSec.setStatus("current")
_Ex2asGetAttachmentTotal_Type = Gauge32
_Ex2asGetAttachmentTotal_Object = MibScalar
ex2asGetAttachmentTotal = _Ex2asGetAttachmentTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 29),
    _Ex2asGetAttachmentTotal_Type()
)
ex2asGetAttachmentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asGetAttachmentTotal.setStatus("current")
_Ex2asGetHierarchyCommandsPerSec_Type = Gauge32
_Ex2asGetHierarchyCommandsPerSec_Object = MibScalar
ex2asGetHierarchyCommandsPerSec = _Ex2asGetHierarchyCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 30),
    _Ex2asGetHierarchyCommandsPerSec_Type()
)
ex2asGetHierarchyCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asGetHierarchyCommandsPerSec.setStatus("current")
_Ex2asGetHierarchyTotal_Type = Gauge32
_Ex2asGetHierarchyTotal_Object = MibScalar
ex2asGetHierarchyTotal = _Ex2asGetHierarchyTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 31),
    _Ex2asGetHierarchyTotal_Type()
)
ex2asGetHierarchyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asGetHierarchyTotal.setStatus("current")
_Ex2asGetItemEstimatCommandPerSec_Type = Gauge32
_Ex2asGetItemEstimatCommandPerSec_Object = MibScalar
ex2asGetItemEstimatCommandPerSec = _Ex2asGetItemEstimatCommandPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 32),
    _Ex2asGetItemEstimatCommandPerSec_Type()
)
ex2asGetItemEstimatCommandPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asGetItemEstimatCommandPerSec.setStatus("current")
_Ex2asGetItemEstimateTotal_Type = Gauge32
_Ex2asGetItemEstimateTotal_Object = MibScalar
ex2asGetItemEstimateTotal = _Ex2asGetItemEstimateTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 33),
    _Ex2asGetItemEstimateTotal_Type()
)
ex2asGetItemEstimateTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asGetItemEstimateTotal.setStatus("current")
_Ex2asHeartbeatInterval_Type = Gauge32
_Ex2asHeartbeatInterval_Object = MibScalar
ex2asHeartbeatInterval = _Ex2asHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 34),
    _Ex2asHeartbeatInterval_Type()
)
ex2asHeartbeatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asHeartbeatInterval.setStatus("current")
_Ex2asIdleThreads_Type = Gauge32
_Ex2asIdleThreads_Object = MibScalar
ex2asIdleThreads = _Ex2asIdleThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 35),
    _Ex2asIdleThreads_Type()
)
ex2asIdleThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asIdleThreads.setStatus("current")
_Ex2asIncomingProxyRequestsTotal_Type = Gauge32
_Ex2asIncomingProxyRequestsTotal_Object = MibScalar
ex2asIncomingProxyRequestsTotal = _Ex2asIncomingProxyRequestsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 36),
    _Ex2asIncomingProxyRequestsTotal_Type()
)
ex2asIncomingProxyRequestsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asIncomingProxyRequestsTotal.setStatus("current")
_Ex2asItemOperationsCommandPerSec_Type = Gauge32
_Ex2asItemOperationsCommandPerSec_Object = MibScalar
ex2asItemOperationsCommandPerSec = _Ex2asItemOperationsCommandPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 37),
    _Ex2asItemOperationsCommandPerSec_Type()
)
ex2asItemOperationsCommandPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asItemOperationsCommandPerSec.setStatus("current")
_Ex2asItemOperationsTotal_Type = Gauge32
_Ex2asItemOperationsTotal_Object = MibScalar
ex2asItemOperationsTotal = _Ex2asItemOperationsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 38),
    _Ex2asItemOperationsTotal_Type()
)
ex2asItemOperationsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asItemOperationsTotal.setStatus("current")
_Ex2asMailboxAttchFetchCommandSec_Type = Gauge32
_Ex2asMailboxAttchFetchCommandSec_Object = MibScalar
ex2asMailboxAttchFetchCommandSec = _Ex2asMailboxAttchFetchCommandSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 39),
    _Ex2asMailboxAttchFetchCommandSec_Type()
)
ex2asMailboxAttchFetchCommandSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMailboxAttchFetchCommandSec.setStatus("current")
_Ex2asMailboxAttachmentFetchTotal_Type = Gauge32
_Ex2asMailboxAttachmentFetchTotal_Object = MibScalar
ex2asMailboxAttachmentFetchTotal = _Ex2asMailboxAttachmentFetchTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 40),
    _Ex2asMailboxAttachmentFetchTotal_Type()
)
ex2asMailboxAttachmentFetchTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMailboxAttachmentFetchTotal.setStatus("current")
_Ex2asMailboxItemFetchCommandsSec_Type = Gauge32
_Ex2asMailboxItemFetchCommandsSec_Object = MibScalar
ex2asMailboxItemFetchCommandsSec = _Ex2asMailboxItemFetchCommandsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 41),
    _Ex2asMailboxItemFetchCommandsSec_Type()
)
ex2asMailboxItemFetchCommandsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMailboxItemFetchCommandsSec.setStatus("current")
_Ex2asMailboxItemFetchTotal_Type = Gauge32
_Ex2asMailboxItemFetchTotal_Object = MibScalar
ex2asMailboxItemFetchTotal = _Ex2asMailboxItemFetchTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 42),
    _Ex2asMailboxItemFetchTotal_Type()
)
ex2asMailboxItemFetchTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMailboxItemFetchTotal.setStatus("current")
_Ex2asMailboxSearchTotal_Type = Gauge32
_Ex2asMailboxSearchTotal_Object = MibScalar
ex2asMailboxSearchTotal = _Ex2asMailboxSearchTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 43),
    _Ex2asMailboxSearchTotal_Type()
)
ex2asMailboxSearchTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMailboxSearchTotal.setStatus("current")
_Ex2asMailboxSearchesPerSec_Type = Gauge32
_Ex2asMailboxSearchesPerSec_Object = MibScalar
ex2asMailboxSearchesPerSec = _Ex2asMailboxSearchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 44),
    _Ex2asMailboxSearchesPerSec_Type()
)
ex2asMailboxSearchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMailboxSearchesPerSec.setStatus("current")
_Ex2asMeetingResponsCommandPerSec_Type = Gauge32
_Ex2asMeetingResponsCommandPerSec_Object = MibScalar
ex2asMeetingResponsCommandPerSec = _Ex2asMeetingResponsCommandPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 45),
    _Ex2asMeetingResponsCommandPerSec_Type()
)
ex2asMeetingResponsCommandPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMeetingResponsCommandPerSec.setStatus("current")
_Ex2asMeetingResponseTotal_Type = Gauge32
_Ex2asMeetingResponseTotal_Object = MibScalar
ex2asMeetingResponseTotal = _Ex2asMeetingResponseTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 46),
    _Ex2asMeetingResponseTotal_Type()
)
ex2asMeetingResponseTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMeetingResponseTotal.setStatus("current")
_Ex2asMoveCollectionCommandPerSec_Type = Gauge32
_Ex2asMoveCollectionCommandPerSec_Object = MibScalar
ex2asMoveCollectionCommandPerSec = _Ex2asMoveCollectionCommandPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 47),
    _Ex2asMoveCollectionCommandPerSec_Type()
)
ex2asMoveCollectionCommandPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMoveCollectionCommandPerSec.setStatus("current")
_Ex2asMoveCollectionTotal_Type = Gauge32
_Ex2asMoveCollectionTotal_Object = MibScalar
ex2asMoveCollectionTotal = _Ex2asMoveCollectionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 48),
    _Ex2asMoveCollectionTotal_Type()
)
ex2asMoveCollectionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMoveCollectionTotal.setStatus("current")
_Ex2asMoveItemsCommandsPerSec_Type = Gauge32
_Ex2asMoveItemsCommandsPerSec_Object = MibScalar
ex2asMoveItemsCommandsPerSec = _Ex2asMoveItemsCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 49),
    _Ex2asMoveItemsCommandsPerSec_Type()
)
ex2asMoveItemsCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMoveItemsCommandsPerSec.setStatus("current")
_Ex2asMoveItemsTotal_Type = Gauge32
_Ex2asMoveItemsTotal_Object = MibScalar
ex2asMoveItemsTotal = _Ex2asMoveItemsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 50),
    _Ex2asMoveItemsTotal_Type()
)
ex2asMoveItemsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asMoveItemsTotal.setStatus("current")
_Ex2asNumEmptyFoldrContentProcSec_Type = Gauge32
_Ex2asNumEmptyFoldrContentProcSec_Object = MibScalar
ex2asNumEmptyFoldrContentProcSec = _Ex2asNumEmptyFoldrContentProcSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 51),
    _Ex2asNumEmptyFoldrContentProcSec_Type()
)
ex2asNumEmptyFoldrContentProcSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asNumEmptyFoldrContentProcSec.setStatus("current")
_Ex2asOptionsCommandsPerSec_Type = Gauge32
_Ex2asOptionsCommandsPerSec_Object = MibScalar
ex2asOptionsCommandsPerSec = _Ex2asOptionsCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 52),
    _Ex2asOptionsCommandsPerSec_Type()
)
ex2asOptionsCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asOptionsCommandsPerSec.setStatus("current")
_Ex2asOptionsTotal_Type = Gauge32
_Ex2asOptionsTotal_Object = MibScalar
ex2asOptionsTotal = _Ex2asOptionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 53),
    _Ex2asOptionsTotal_Type()
)
ex2asOptionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asOptionsTotal.setStatus("current")
_Ex2asOutgoingProxyRequestsTotal_Type = Gauge32
_Ex2asOutgoingProxyRequestsTotal_Object = MibScalar
ex2asOutgoingProxyRequestsTotal = _Ex2asOutgoingProxyRequestsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 54),
    _Ex2asOutgoingProxyRequestsTotal_Type()
)
ex2asOutgoingProxyRequestsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asOutgoingProxyRequestsTotal.setStatus("current")
_Ex2asPID_Type = Gauge32
_Ex2asPID_Object = MibScalar
ex2asPID = _Ex2asPID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 55),
    _Ex2asPID_Type()
)
ex2asPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asPID.setStatus("current")
_Ex2asPingCommandsDroppedPerSec_Type = Gauge32
_Ex2asPingCommandsDroppedPerSec_Object = MibScalar
ex2asPingCommandsDroppedPerSec = _Ex2asPingCommandsDroppedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 56),
    _Ex2asPingCommandsDroppedPerSec_Type()
)
ex2asPingCommandsDroppedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asPingCommandsDroppedPerSec.setStatus("current")
_Ex2asPingCommandsPending_Type = Gauge32
_Ex2asPingCommandsPending_Object = MibScalar
ex2asPingCommandsPending = _Ex2asPingCommandsPending_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 57),
    _Ex2asPingCommandsPending_Type()
)
ex2asPingCommandsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asPingCommandsPending.setStatus("current")
_Ex2asPingCommandsPerSec_Type = Gauge32
_Ex2asPingCommandsPerSec_Object = MibScalar
ex2asPingCommandsPerSec = _Ex2asPingCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 58),
    _Ex2asPingCommandsPerSec_Type()
)
ex2asPingCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asPingCommandsPerSec.setStatus("current")
_Ex2asPingDroppedTotal_Type = Gauge32
_Ex2asPingDroppedTotal_Object = MibScalar
ex2asPingDroppedTotal = _Ex2asPingDroppedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 59),
    _Ex2asPingDroppedTotal_Type()
)
ex2asPingDroppedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asPingDroppedTotal.setStatus("current")
_Ex2asPingTotal_Type = Gauge32
_Ex2asPingTotal_Object = MibScalar
ex2asPingTotal = _Ex2asPingTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 60),
    _Ex2asPingTotal_Type()
)
ex2asPingTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asPingTotal.setStatus("current")
_Ex2asProvisionCommandsPerSec_Type = Gauge32
_Ex2asProvisionCommandsPerSec_Object = MibScalar
ex2asProvisionCommandsPerSec = _Ex2asProvisionCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 61),
    _Ex2asProvisionCommandsPerSec_Type()
)
ex2asProvisionCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asProvisionCommandsPerSec.setStatus("current")
_Ex2asProvisionTotal_Type = Gauge32
_Ex2asProvisionTotal_Object = MibScalar
ex2asProvisionTotal = _Ex2asProvisionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 62),
    _Ex2asProvisionTotal_Type()
)
ex2asProvisionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asProvisionTotal.setStatus("current")
_Ex2asProxyLogonCommandsSentTotal_Type = Gauge32
_Ex2asProxyLogonCommandsSentTotal_Object = MibScalar
ex2asProxyLogonCommandsSentTotal = _Ex2asProxyLogonCommandsSentTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 63),
    _Ex2asProxyLogonCommandsSentTotal_Type()
)
ex2asProxyLogonCommandsSentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asProxyLogonCommandsSentTotal.setStatus("current")
_Ex2asProxyLogonReceivedTotal_Type = Gauge32
_Ex2asProxyLogonReceivedTotal_Object = MibScalar
ex2asProxyLogonReceivedTotal = _Ex2asProxyLogonReceivedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 64),
    _Ex2asProxyLogonReceivedTotal_Type()
)
ex2asProxyLogonReceivedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asProxyLogonReceivedTotal.setStatus("current")
_Ex2asRecoverySyncCommandsPerSec_Type = Gauge32
_Ex2asRecoverySyncCommandsPerSec_Object = MibScalar
ex2asRecoverySyncCommandsPerSec = _Ex2asRecoverySyncCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 65),
    _Ex2asRecoverySyncCommandsPerSec_Type()
)
ex2asRecoverySyncCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asRecoverySyncCommandsPerSec.setStatus("current")
_Ex2asRecoverySyncTotal_Type = Gauge32
_Ex2asRecoverySyncTotal_Object = MibScalar
ex2asRecoverySyncTotal = _Ex2asRecoverySyncTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 66),
    _Ex2asRecoverySyncTotal_Type()
)
ex2asRecoverySyncTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asRecoverySyncTotal.setStatus("current")
_Ex2asRequestsQueued_Type = Gauge32
_Ex2asRequestsQueued_Object = MibScalar
ex2asRequestsQueued = _Ex2asRequestsQueued_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 67),
    _Ex2asRequestsQueued_Type()
)
ex2asRequestsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asRequestsQueued.setStatus("current")
_Ex2asRequestsTotal_Type = Gauge32
_Ex2asRequestsTotal_Object = MibScalar
ex2asRequestsTotal = _Ex2asRequestsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 68),
    _Ex2asRequestsTotal_Type()
)
ex2asRequestsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asRequestsTotal.setStatus("current")
_Ex2asRequestsPerSec_Type = Gauge32
_Ex2asRequestsPerSec_Object = MibScalar
ex2asRequestsPerSec = _Ex2asRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 69),
    _Ex2asRequestsPerSec_Type()
)
ex2asRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asRequestsPerSec.setStatus("current")
_Ex2asSearchCommandsPerSec_Type = Gauge32
_Ex2asSearchCommandsPerSec_Object = MibScalar
ex2asSearchCommandsPerSec = _Ex2asSearchCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 70),
    _Ex2asSearchCommandsPerSec_Type()
)
ex2asSearchCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSearchCommandsPerSec.setStatus("current")
_Ex2asSearchTotal_Type = Gauge32
_Ex2asSearchTotal_Object = MibScalar
ex2asSearchTotal = _Ex2asSearchTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 71),
    _Ex2asSearchTotal_Type()
)
ex2asSearchTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSearchTotal.setStatus("current")
_Ex2asSendMailCommandsPerSec_Type = Gauge32
_Ex2asSendMailCommandsPerSec_Object = MibScalar
ex2asSendMailCommandsPerSec = _Ex2asSendMailCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 72),
    _Ex2asSendMailCommandsPerSec_Type()
)
ex2asSendMailCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSendMailCommandsPerSec.setStatus("current")
_Ex2asSendMailTotal_Type = Gauge32
_Ex2asSendMailTotal_Object = MibScalar
ex2asSendMailTotal = _Ex2asSendMailTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 73),
    _Ex2asSendMailTotal_Type()
)
ex2asSendMailTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSendMailTotal.setStatus("current")
_Ex2asSettingsCommandsPerSec_Type = Gauge32
_Ex2asSettingsCommandsPerSec_Object = MibScalar
ex2asSettingsCommandsPerSec = _Ex2asSettingsCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 74),
    _Ex2asSettingsCommandsPerSec_Type()
)
ex2asSettingsCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSettingsCommandsPerSec.setStatus("current")
_Ex2asSettingsTotal_Type = Gauge32
_Ex2asSettingsTotal_Object = MibScalar
ex2asSettingsTotal = _Ex2asSettingsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 75),
    _Ex2asSettingsTotal_Type()
)
ex2asSettingsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSettingsTotal.setStatus("current")
_Ex2asSmartForwardCommandsPerSec_Type = Gauge32
_Ex2asSmartForwardCommandsPerSec_Object = MibScalar
ex2asSmartForwardCommandsPerSec = _Ex2asSmartForwardCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 76),
    _Ex2asSmartForwardCommandsPerSec_Type()
)
ex2asSmartForwardCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSmartForwardCommandsPerSec.setStatus("current")
_Ex2asSmartForwardTotal_Type = Gauge32
_Ex2asSmartForwardTotal_Object = MibScalar
ex2asSmartForwardTotal = _Ex2asSmartForwardTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 77),
    _Ex2asSmartForwardTotal_Type()
)
ex2asSmartForwardTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSmartForwardTotal.setStatus("current")
_Ex2asSmartReplyCommandsPerSec_Type = Gauge32
_Ex2asSmartReplyCommandsPerSec_Object = MibScalar
ex2asSmartReplyCommandsPerSec = _Ex2asSmartReplyCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 78),
    _Ex2asSmartReplyCommandsPerSec_Type()
)
ex2asSmartReplyCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSmartReplyCommandsPerSec.setStatus("current")
_Ex2asSmartReplyTotal_Type = Gauge32
_Ex2asSmartReplyTotal_Object = MibScalar
ex2asSmartReplyTotal = _Ex2asSmartReplyTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 79),
    _Ex2asSmartReplyTotal_Type()
)
ex2asSmartReplyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSmartReplyTotal.setStatus("current")
_Ex2asSyncCommandsDroppedPerSec_Type = Gauge32
_Ex2asSyncCommandsDroppedPerSec_Object = MibScalar
ex2asSyncCommandsDroppedPerSec = _Ex2asSyncCommandsDroppedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 80),
    _Ex2asSyncCommandsDroppedPerSec_Type()
)
ex2asSyncCommandsDroppedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSyncCommandsDroppedPerSec.setStatus("current")
_Ex2asSyncCommandsPending_Type = Gauge32
_Ex2asSyncCommandsPending_Object = MibScalar
ex2asSyncCommandsPending = _Ex2asSyncCommandsPending_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 81),
    _Ex2asSyncCommandsPending_Type()
)
ex2asSyncCommandsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSyncCommandsPending.setStatus("current")
_Ex2asSyncCommandsPerSec_Type = Gauge32
_Ex2asSyncCommandsPerSec_Object = MibScalar
ex2asSyncCommandsPerSec = _Ex2asSyncCommandsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 82),
    _Ex2asSyncCommandsPerSec_Type()
)
ex2asSyncCommandsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSyncCommandsPerSec.setStatus("current")
_Ex2asSyncDroppedTotal_Type = Gauge32
_Ex2asSyncDroppedTotal_Object = MibScalar
ex2asSyncDroppedTotal = _Ex2asSyncDroppedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 83),
    _Ex2asSyncDroppedTotal_Type()
)
ex2asSyncDroppedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSyncDroppedTotal.setStatus("current")
_Ex2asSyncStateKBytesLeftCompress_Type = Gauge32
_Ex2asSyncStateKBytesLeftCompress_Object = MibScalar
ex2asSyncStateKBytesLeftCompress = _Ex2asSyncStateKBytesLeftCompress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 84),
    _Ex2asSyncStateKBytesLeftCompress_Type()
)
ex2asSyncStateKBytesLeftCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSyncStateKBytesLeftCompress.setStatus("current")
_Ex2asSyncStateKBytesTotal_Type = Gauge32
_Ex2asSyncStateKBytesTotal_Object = MibScalar
ex2asSyncStateKBytesTotal = _Ex2asSyncStateKBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 85),
    _Ex2asSyncStateKBytesTotal_Type()
)
ex2asSyncStateKBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSyncStateKBytesTotal.setStatus("current")
_Ex2asSyncTotal_Type = Gauge32
_Ex2asSyncTotal_Object = MibScalar
ex2asSyncTotal = _Ex2asSyncTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 86),
    _Ex2asSyncTotal_Type()
)
ex2asSyncTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asSyncTotal.setStatus("current")
_Ex2asWrongCASProxyRequestsTotal_Type = Gauge32
_Ex2asWrongCASProxyRequestsTotal_Object = MibScalar
ex2asWrongCASProxyRequestsTotal = _Ex2asWrongCASProxyRequestsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 6, 87),
    _Ex2asWrongCASProxyRequestsTotal_Type()
)
ex2asWrongCASProxyRequestsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2asWrongCASProxyRequestsTotal.setStatus("current")
_Ex2AssistantsTable_Object = MibTable
ex2AssistantsTable = _Ex2AssistantsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7)
)
if mibBuilder.loadTexts:
    ex2AssistantsTable.setStatus("current")
_Ex2AssistantsEntry_Object = MibTableRow
ex2AssistantsEntry = _Ex2AssistantsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1)
)
ex2AssistantsEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2aInstance"),
)
if mibBuilder.loadTexts:
    ex2AssistantsEntry.setStatus("current")
_Ex2aInstance_Type = InstanceName
_Ex2aInstance_Object = MibTableColumn
ex2aInstance = _Ex2aInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 1),
    _Ex2aInstance_Type()
)
ex2aInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aInstance.setStatus("current")
_Ex2aAvgEventProcessTimeInSeconds_Type = Gauge32
_Ex2aAvgEventProcessTimeInSeconds_Object = MibTableColumn
ex2aAvgEventProcessTimeInSeconds = _Ex2aAvgEventProcessTimeInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 2),
    _Ex2aAvgEventProcessTimeInSeconds_Type()
)
ex2aAvgEventProcessTimeInSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aAvgEventProcessTimeInSeconds.setStatus("current")
_Ex2aAvgEventQueueTimeInSeconds_Type = Gauge32
_Ex2aAvgEventQueueTimeInSeconds_Object = MibTableColumn
ex2aAvgEventQueueTimeInSeconds = _Ex2aAvgEventQueueTimeInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 3),
    _Ex2aAvgEventQueueTimeInSeconds_Type()
)
ex2aAvgEventQueueTimeInSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aAvgEventQueueTimeInSeconds.setStatus("current")
_Ex2aAvgMailboxProcessTimeSeconds_Type = Gauge32
_Ex2aAvgMailboxProcessTimeSeconds_Object = MibTableColumn
ex2aAvgMailboxProcessTimeSeconds = _Ex2aAvgMailboxProcessTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 4),
    _Ex2aAvgMailboxProcessTimeSeconds_Type()
)
ex2aAvgMailboxProcessTimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aAvgMailboxProcessTimeSeconds.setStatus("current")
_Ex2aAvgQueueSizeEventDispatchers_Type = Gauge32
_Ex2aAvgQueueSizeEventDispatchers_Object = MibTableColumn
ex2aAvgQueueSizeEventDispatchers = _Ex2aAvgQueueSizeEventDispatchers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 5),
    _Ex2aAvgQueueSizeEventDispatchers_Type()
)
ex2aAvgQueueSizeEventDispatchers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aAvgQueueSizeEventDispatchers.setStatus("current")
_Ex2aEventsPolled_Type = Gauge32
_Ex2aEventsPolled_Object = MibTableColumn
ex2aEventsPolled = _Ex2aEventsPolled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 6),
    _Ex2aEventsPolled_Type()
)
ex2aEventsPolled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aEventsPolled.setStatus("current")
_Ex2aEventsPolledPerSec_Type = Gauge32
_Ex2aEventsPolledPerSec_Object = MibTableColumn
ex2aEventsPolledPerSec = _Ex2aEventsPolledPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 7),
    _Ex2aEventsPolledPerSec_Type()
)
ex2aEventsPolledPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aEventsPolledPerSec.setStatus("current")
_Ex2aEventsProcessed_Type = Gauge32
_Ex2aEventsProcessed_Object = MibTableColumn
ex2aEventsProcessed = _Ex2aEventsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 8),
    _Ex2aEventsProcessed_Type()
)
ex2aEventsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aEventsProcessed.setStatus("current")
_Ex2aEventsInQueue_Type = Gauge32
_Ex2aEventsInQueue_Object = MibTableColumn
ex2aEventsInQueue = _Ex2aEventsInQueue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 9),
    _Ex2aEventsInQueue_Type()
)
ex2aEventsInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aEventsInQueue.setStatus("current")
_Ex2aHighestEventCounterPolled_Type = Gauge32
_Ex2aHighestEventCounterPolled_Object = MibTableColumn
ex2aHighestEventCounterPolled = _Ex2aHighestEventCounterPolled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 10),
    _Ex2aHighestEventCounterPolled_Type()
)
ex2aHighestEventCounterPolled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aHighestEventCounterPolled.setStatus("current")
_Ex2aMailboxesProcessed_Type = Gauge32
_Ex2aMailboxesProcessed_Object = MibTableColumn
ex2aMailboxesProcessed = _Ex2aMailboxesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 11),
    _Ex2aMailboxesProcessed_Type()
)
ex2aMailboxesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aMailboxesProcessed.setStatus("current")
_Ex2aMailboxesProcessedPerSec_Type = Gauge32
_Ex2aMailboxesProcessedPerSec_Object = MibTableColumn
ex2aMailboxesProcessedPerSec = _Ex2aMailboxesProcessedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 12),
    _Ex2aMailboxesProcessedPerSec_Type()
)
ex2aMailboxesProcessedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aMailboxesProcessedPerSec.setStatus("current")
_Ex2aNumberOfEventDispatchers_Type = Gauge32
_Ex2aNumberOfEventDispatchers_Object = MibTableColumn
ex2aNumberOfEventDispatchers = _Ex2aNumberOfEventDispatchers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 13),
    _Ex2aNumberOfEventDispatchers_Type()
)
ex2aNumberOfEventDispatchers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aNumberOfEventDispatchers.setStatus("current")
_Ex2aNumberOfFailEventDispatchers_Type = Gauge32
_Ex2aNumberOfFailEventDispatchers_Object = MibTableColumn
ex2aNumberOfFailEventDispatchers = _Ex2aNumberOfFailEventDispatchers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 14),
    _Ex2aNumberOfFailEventDispatchers_Type()
)
ex2aNumberOfFailEventDispatchers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aNumberOfFailEventDispatchers.setStatus("current")
_Ex2aNumberOfHandledExceptions_Type = Gauge32
_Ex2aNumberOfHandledExceptions_Object = MibTableColumn
ex2aNumberOfHandledExceptions = _Ex2aNumberOfHandledExceptions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 15),
    _Ex2aNumberOfHandledExceptions_Type()
)
ex2aNumberOfHandledExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aNumberOfHandledExceptions.setStatus("current")
_Ex2aNumberOfThreadsUsed_Type = Gauge32
_Ex2aNumberOfThreadsUsed_Object = MibTableColumn
ex2aNumberOfThreadsUsed = _Ex2aNumberOfThreadsUsed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 16),
    _Ex2aNumberOfThreadsUsed_Type()
)
ex2aNumberOfThreadsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aNumberOfThreadsUsed.setStatus("current")
_Ex2aNumberEventsProcessPerSecond_Type = Gauge32
_Ex2aNumberEventsProcessPerSecond_Object = MibTableColumn
ex2aNumberEventsProcessPerSecond = _Ex2aNumberEventsProcessPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 17),
    _Ex2aNumberEventsProcessPerSecond_Type()
)
ex2aNumberEventsProcessPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aNumberEventsProcessPerSecond.setStatus("current")
_Ex2aPercentageFailEventDispatchr_Type = Gauge32
_Ex2aPercentageFailEventDispatchr_Object = MibTableColumn
ex2aPercentageFailEventDispatchr = _Ex2aPercentageFailEventDispatchr_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 18),
    _Ex2aPercentageFailEventDispatchr_Type()
)
ex2aPercentageFailEventDispatchr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aPercentageFailEventDispatchr.setStatus("current")
_Ex2aPercentageOfInterestingEvent_Type = Gauge32
_Ex2aPercentageOfInterestingEvent_Object = MibTableColumn
ex2aPercentageOfInterestingEvent = _Ex2aPercentageOfInterestingEvent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 19),
    _Ex2aPercentageOfInterestingEvent_Type()
)
ex2aPercentageOfInterestingEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aPercentageOfInterestingEvent.setStatus("current")
_Ex2aPollingDelay_Type = Gauge32
_Ex2aPollingDelay_Object = MibTableColumn
ex2aPollingDelay = _Ex2aPollingDelay_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 7, 1, 20),
    _Ex2aPollingDelay_Type()
)
ex2aPollingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aPollingDelay.setStatus("current")
_Ex2AvailabilityService_ObjectIdentity = ObjectIdentity
ex2AvailabilityService = _Ex2AvailabilityService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8)
)
if mibBuilder.loadTexts:
    ex2AvailabilityService.setStatus("current")
_Ex2aserAvailabilityRequestsSec_Type = Gauge32
_Ex2aserAvailabilityRequestsSec_Object = MibScalar
ex2aserAvailabilityRequestsSec = _Ex2aserAvailabilityRequestsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 1),
    _Ex2aserAvailabilityRequestsSec_Type()
)
ex2aserAvailabilityRequestsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserAvailabilityRequestsSec.setStatus("current")
_Ex2aserAvgNumMailboxProcessReqst_Type = Gauge32
_Ex2aserAvgNumMailboxProcessReqst_Object = MibScalar
ex2aserAvgNumMailboxProcessReqst = _Ex2aserAvgNumMailboxProcessReqst_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 2),
    _Ex2aserAvgNumMailboxProcessReqst_Type()
)
ex2aserAvgNumMailboxProcessReqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserAvgNumMailboxProcessReqst.setStatus("current")
_Ex2aserAvgTimProCrsFrstFreBsyReq_Type = Gauge32
_Ex2aserAvgTimProCrsFrstFreBsyReq_Object = MibScalar
ex2aserAvgTimProCrsFrstFreBsyReq = _Ex2aserAvgTimProCrsFrstFreBsyReq_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 3),
    _Ex2aserAvgTimProCrsFrstFreBsyReq_Type()
)
ex2aserAvgTimProCrsFrstFreBsyReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserAvgTimProCrsFrstFreBsyReq.setStatus("current")
_Ex2aserAvgTimProCrsSiteFreBsyReq_Type = Gauge32
_Ex2aserAvgTimProCrsSiteFreBsyReq_Object = MibScalar
ex2aserAvgTimProCrsSiteFreBsyReq = _Ex2aserAvgTimProCrsSiteFreBsyReq_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 4),
    _Ex2aserAvgTimProCrsSiteFreBsyReq_Type()
)
ex2aserAvgTimProCrsSiteFreBsyReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserAvgTimProCrsSiteFreBsyReq.setStatus("current")
_Ex2aserAvgTimeProcessFreeBusyReq_Type = Gauge32
_Ex2aserAvgTimeProcessFreeBusyReq_Object = MibScalar
ex2aserAvgTimeProcessFreeBusyReq = _Ex2aserAvgTimeProcessFreeBusyReq_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 5),
    _Ex2aserAvgTimeProcessFreeBusyReq_Type()
)
ex2aserAvgTimeProcessFreeBusyReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserAvgTimeProcessFreeBusyReq.setStatus("current")
_Ex2aserAvgTimeProcessMtgSuggRequ_Type = Gauge32
_Ex2aserAvgTimeProcessMtgSuggRequ_Object = MibScalar
ex2aserAvgTimeProcessMtgSuggRequ = _Ex2aserAvgTimeProcessMtgSuggRequ_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 6),
    _Ex2aserAvgTimeProcessMtgSuggRequ_Type()
)
ex2aserAvgTimeProcessMtgSuggRequ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserAvgTimeProcessMtgSuggRequ.setStatus("current")
_Ex2aserCrsFrstCalendarFailureSec_Type = Gauge32
_Ex2aserCrsFrstCalendarFailureSec_Object = MibScalar
ex2aserCrsFrstCalendarFailureSec = _Ex2aserCrsFrstCalendarFailureSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 7),
    _Ex2aserCrsFrstCalendarFailureSec_Type()
)
ex2aserCrsFrstCalendarFailureSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserCrsFrstCalendarFailureSec.setStatus("current")
_Ex2aserCrsFrstCalendarQueriesSec_Type = Gauge32
_Ex2aserCrsFrstCalendarQueriesSec_Object = MibScalar
ex2aserCrsFrstCalendarQueriesSec = _Ex2aserCrsFrstCalendarQueriesSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 8),
    _Ex2aserCrsFrstCalendarQueriesSec_Type()
)
ex2aserCrsFrstCalendarQueriesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserCrsFrstCalendarQueriesSec.setStatus("current")
_Ex2aserCrsSiteCalendarFailureSec_Type = Gauge32
_Ex2aserCrsSiteCalendarFailureSec_Object = MibScalar
ex2aserCrsSiteCalendarFailureSec = _Ex2aserCrsSiteCalendarFailureSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 9),
    _Ex2aserCrsSiteCalendarFailureSec_Type()
)
ex2aserCrsSiteCalendarFailureSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserCrsSiteCalendarFailureSec.setStatus("current")
_Ex2aserCrsSiteCalendarQueriesSec_Type = Gauge32
_Ex2aserCrsSiteCalendarQueriesSec_Object = MibScalar
ex2aserCrsSiteCalendarQueriesSec = _Ex2aserCrsSiteCalendarQueriesSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 10),
    _Ex2aserCrsSiteCalendarQueriesSec_Type()
)
ex2aserCrsSiteCalendarQueriesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserCrsSiteCalendarQueriesSec.setStatus("current")
_Ex2aserForeignConnectorQuerySec_Type = Gauge32
_Ex2aserForeignConnectorQuerySec_Object = MibScalar
ex2aserForeignConnectorQuerySec = _Ex2aserForeignConnectorQuerySec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 11),
    _Ex2aserForeignConnectorQuerySec_Type()
)
ex2aserForeignConnectorQuerySec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserForeignConnectorQuerySec.setStatus("current")
_Ex2aserForeignConnectReqFailRate_Type = Gauge32
_Ex2aserForeignConnectReqFailRate_Object = MibScalar
ex2aserForeignConnectReqFailRate = _Ex2aserForeignConnectReqFailRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 12),
    _Ex2aserForeignConnectReqFailRate_Type()
)
ex2aserForeignConnectReqFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserForeignConnectReqFailRate.setStatus("current")
_Ex2aserIntraSiteCalendarFailSec_Type = Gauge32
_Ex2aserIntraSiteCalendarFailSec_Object = MibScalar
ex2aserIntraSiteCalendarFailSec = _Ex2aserIntraSiteCalendarFailSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 13),
    _Ex2aserIntraSiteCalendarFailSec_Type()
)
ex2aserIntraSiteCalendarFailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserIntraSiteCalendarFailSec.setStatus("current")
_Ex2aserIntraSiteCalendarQuerySec_Type = Gauge32
_Ex2aserIntraSiteCalendarQuerySec_Object = MibScalar
ex2aserIntraSiteCalendarQuerySec = _Ex2aserIntraSiteCalendarQuerySec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 14),
    _Ex2aserIntraSiteCalendarQuerySec_Type()
)
ex2aserIntraSiteCalendarQuerySec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserIntraSiteCalendarQuerySec.setStatus("current")
_Ex2aserPublicFolderQueriesSec_Type = Gauge32
_Ex2aserPublicFolderQueriesSec_Object = MibScalar
ex2aserPublicFolderQueriesSec = _Ex2aserPublicFolderQueriesSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 15),
    _Ex2aserPublicFolderQueriesSec_Type()
)
ex2aserPublicFolderQueriesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserPublicFolderQueriesSec.setStatus("current")
_Ex2aserPublicFolderReqFailSec_Type = Gauge32
_Ex2aserPublicFolderReqFailSec_Object = MibScalar
ex2aserPublicFolderReqFailSec = _Ex2aserPublicFolderReqFailSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 16),
    _Ex2aserPublicFolderReqFailSec_Type()
)
ex2aserPublicFolderReqFailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserPublicFolderReqFailSec.setStatus("current")
_Ex2aserSuggestionsRequestsSec_Type = Gauge32
_Ex2aserSuggestionsRequestsSec_Object = MibScalar
ex2aserSuggestionsRequestsSec = _Ex2aserSuggestionsRequestsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 8, 17),
    _Ex2aserSuggestionsRequestsSec_Type()
)
ex2aserSuggestionsRequestsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2aserSuggestionsRequestsSec.setStatus("current")
_Ex2CalendarAttendant_ObjectIdentity = ObjectIdentity
ex2CalendarAttendant = _Ex2CalendarAttendant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 9)
)
if mibBuilder.loadTexts:
    ex2CalendarAttendant.setStatus("current")
_Ex2caAvgCalendarAttendntProcTime_Type = Gauge32
_Ex2caAvgCalendarAttendntProcTime_Object = MibScalar
ex2caAvgCalendarAttendntProcTime = _Ex2caAvgCalendarAttendntProcTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 9, 1),
    _Ex2caAvgCalendarAttendntProcTime_Type()
)
ex2caAvgCalendarAttendntProcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2caAvgCalendarAttendntProcTime.setStatus("current")
_Ex2caLastCalendarAttendtProcTime_Type = Gauge32
_Ex2caLastCalendarAttendtProcTime_Object = MibScalar
ex2caLastCalendarAttendtProcTime = _Ex2caLastCalendarAttendtProcTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 9, 2),
    _Ex2caLastCalendarAttendtProcTime_Type()
)
ex2caLastCalendarAttendtProcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2caLastCalendarAttendtProcTime.setStatus("current")
_Ex2caLostRaces_Type = Gauge32
_Ex2caLostRaces_Object = MibScalar
ex2caLostRaces = _Ex2caLostRaces_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 9, 3),
    _Ex2caLostRaces_Type()
)
ex2caLostRaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2caLostRaces.setStatus("current")
_Ex2caMeetingCancellations_Type = Gauge32
_Ex2caMeetingCancellations_Object = MibScalar
ex2caMeetingCancellations = _Ex2caMeetingCancellations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 9, 4),
    _Ex2caMeetingCancellations_Type()
)
ex2caMeetingCancellations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2caMeetingCancellations.setStatus("current")
_Ex2caMeetingMessagesDeleted_Type = Gauge32
_Ex2caMeetingMessagesDeleted_Object = MibScalar
ex2caMeetingMessagesDeleted = _Ex2caMeetingMessagesDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 9, 5),
    _Ex2caMeetingMessagesDeleted_Type()
)
ex2caMeetingMessagesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2caMeetingMessagesDeleted.setStatus("current")
_Ex2caMeetingMessagesProcessed_Type = Gauge32
_Ex2caMeetingMessagesProcessed_Object = MibScalar
ex2caMeetingMessagesProcessed = _Ex2caMeetingMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 9, 6),
    _Ex2caMeetingMessagesProcessed_Type()
)
ex2caMeetingMessagesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2caMeetingMessagesProcessed.setStatus("current")
_Ex2caMeetingRequests_Type = Gauge32
_Ex2caMeetingRequests_Object = MibScalar
ex2caMeetingRequests = _Ex2caMeetingRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 9, 7),
    _Ex2caMeetingRequests_Type()
)
ex2caMeetingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2caMeetingRequests.setStatus("current")
_Ex2caMeetingResponses_Type = Gauge32
_Ex2caMeetingResponses_Object = MibScalar
ex2caMeetingResponses = _Ex2caMeetingResponses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 9, 8),
    _Ex2caMeetingResponses_Type()
)
ex2caMeetingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2caMeetingResponses.setStatus("current")
_Ex2caRequestsFailed_Type = Gauge32
_Ex2caRequestsFailed_Object = MibScalar
ex2caRequestsFailed = _Ex2caRequestsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 9, 9),
    _Ex2caRequestsFailed_Type()
)
ex2caRequestsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2caRequestsFailed.setStatus("current")
_Ex2ConnectionFilteringAgent_ObjectIdentity = ObjectIdentity
ex2ConnectionFilteringAgent = _Ex2ConnectionFilteringAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10)
)
if mibBuilder.loadTexts:
    ex2ConnectionFilteringAgent.setStatus("current")
_Ex2cfaConnectionsOnIPAllowList_Type = Gauge32
_Ex2cfaConnectionsOnIPAllowList_Object = MibScalar
ex2cfaConnectionsOnIPAllowList = _Ex2cfaConnectionsOnIPAllowList_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 1),
    _Ex2cfaConnectionsOnIPAllowList_Type()
)
ex2cfaConnectionsOnIPAllowList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaConnectionsOnIPAllowList.setStatus("current")
_Ex2cfaConnOnIPAllowListProviders_Type = Gauge32
_Ex2cfaConnOnIPAllowListProviders_Object = MibScalar
ex2cfaConnOnIPAllowListProviders = _Ex2cfaConnOnIPAllowListProviders_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 2),
    _Ex2cfaConnOnIPAllowListProviders_Type()
)
ex2cfaConnOnIPAllowListProviders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaConnOnIPAllowListProviders.setStatus("current")
_Ex2cfaConnOnIPAllowListProvidSec_Type = Gauge32
_Ex2cfaConnOnIPAllowListProvidSec_Object = MibScalar
ex2cfaConnOnIPAllowListProvidSec = _Ex2cfaConnOnIPAllowListProvidSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 3),
    _Ex2cfaConnOnIPAllowListProvidSec_Type()
)
ex2cfaConnOnIPAllowListProvidSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaConnOnIPAllowListProvidSec.setStatus("current")
_Ex2cfaConnOnIPAllowListSec_Type = Gauge32
_Ex2cfaConnOnIPAllowListSec_Object = MibScalar
ex2cfaConnOnIPAllowListSec = _Ex2cfaConnOnIPAllowListSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 4),
    _Ex2cfaConnOnIPAllowListSec_Type()
)
ex2cfaConnOnIPAllowListSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaConnOnIPAllowListSec.setStatus("current")
_Ex2cfaConnectionsOnIPBlockList_Type = Gauge32
_Ex2cfaConnectionsOnIPBlockList_Object = MibScalar
ex2cfaConnectionsOnIPBlockList = _Ex2cfaConnectionsOnIPBlockList_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 5),
    _Ex2cfaConnectionsOnIPBlockList_Type()
)
ex2cfaConnectionsOnIPBlockList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaConnectionsOnIPBlockList.setStatus("current")
_Ex2cfaConnOnIPBlockListProviders_Type = Gauge32
_Ex2cfaConnOnIPBlockListProviders_Object = MibScalar
ex2cfaConnOnIPBlockListProviders = _Ex2cfaConnOnIPBlockListProviders_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 6),
    _Ex2cfaConnOnIPBlockListProviders_Type()
)
ex2cfaConnOnIPBlockListProviders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaConnOnIPBlockListProviders.setStatus("current")
_Ex2cfaConnOnIPBlockListProvidSec_Type = Gauge32
_Ex2cfaConnOnIPBlockListProvidSec_Object = MibScalar
ex2cfaConnOnIPBlockListProvidSec = _Ex2cfaConnOnIPBlockListProvidSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 7),
    _Ex2cfaConnOnIPBlockListProvidSec_Type()
)
ex2cfaConnOnIPBlockListProvidSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaConnOnIPBlockListProvidSec.setStatus("current")
_Ex2cfaConnOnIPBlockListPerSec_Type = Gauge32
_Ex2cfaConnOnIPBlockListPerSec_Object = MibScalar
ex2cfaConnOnIPBlockListPerSec = _Ex2cfaConnOnIPBlockListPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 8),
    _Ex2cfaConnOnIPBlockListPerSec_Type()
)
ex2cfaConnOnIPBlockListPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaConnOnIPBlockListPerSec.setStatus("current")
_Ex2cfaMsgOrigIPIPAllowList_Type = Gauge32
_Ex2cfaMsgOrigIPIPAllowList_Object = MibScalar
ex2cfaMsgOrigIPIPAllowList = _Ex2cfaMsgOrigIPIPAllowList_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 9),
    _Ex2cfaMsgOrigIPIPAllowList_Type()
)
ex2cfaMsgOrigIPIPAllowList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaMsgOrigIPIPAllowList.setStatus("current")
_Ex2cfaMsgOrigIPIPAllowListPrv_Type = Gauge32
_Ex2cfaMsgOrigIPIPAllowListPrv_Object = MibScalar
ex2cfaMsgOrigIPIPAllowListPrv = _Ex2cfaMsgOrigIPIPAllowListPrv_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 10),
    _Ex2cfaMsgOrigIPIPAllowListPrv_Type()
)
ex2cfaMsgOrigIPIPAllowListPrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaMsgOrigIPIPAllowListPrv.setStatus("current")
_Ex2cfaMsgOrigIPIPAllowListPrvSec_Type = Gauge32
_Ex2cfaMsgOrigIPIPAllowListPrvSec_Object = MibScalar
ex2cfaMsgOrigIPIPAllowListPrvSec = _Ex2cfaMsgOrigIPIPAllowListPrvSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 11),
    _Ex2cfaMsgOrigIPIPAllowListPrvSec_Type()
)
ex2cfaMsgOrigIPIPAllowListPrvSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaMsgOrigIPIPAllowListPrvSec.setStatus("current")
_Ex2cfaMsgOrigIPIPAllowListSec_Type = Gauge32
_Ex2cfaMsgOrigIPIPAllowListSec_Object = MibScalar
ex2cfaMsgOrigIPIPAllowListSec = _Ex2cfaMsgOrigIPIPAllowListSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 12),
    _Ex2cfaMsgOrigIPIPAllowListSec_Type()
)
ex2cfaMsgOrigIPIPAllowListSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaMsgOrigIPIPAllowListSec.setStatus("current")
_Ex2cfaMsgOrigIPIPBlockList_Type = Gauge32
_Ex2cfaMsgOrigIPIPBlockList_Object = MibScalar
ex2cfaMsgOrigIPIPBlockList = _Ex2cfaMsgOrigIPIPBlockList_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 13),
    _Ex2cfaMsgOrigIPIPBlockList_Type()
)
ex2cfaMsgOrigIPIPBlockList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaMsgOrigIPIPBlockList.setStatus("current")
_Ex2cfaMsgOrigIPIPBlockListPrv_Type = Gauge32
_Ex2cfaMsgOrigIPIPBlockListPrv_Object = MibScalar
ex2cfaMsgOrigIPIPBlockListPrv = _Ex2cfaMsgOrigIPIPBlockListPrv_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 14),
    _Ex2cfaMsgOrigIPIPBlockListPrv_Type()
)
ex2cfaMsgOrigIPIPBlockListPrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaMsgOrigIPIPBlockListPrv.setStatus("current")
_Ex2cfaMsgOrigIPIPBlockListPrvSec_Type = Gauge32
_Ex2cfaMsgOrigIPIPBlockListPrvSec_Object = MibScalar
ex2cfaMsgOrigIPIPBlockListPrvSec = _Ex2cfaMsgOrigIPIPBlockListPrvSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 15),
    _Ex2cfaMsgOrigIPIPBlockListPrvSec_Type()
)
ex2cfaMsgOrigIPIPBlockListPrvSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaMsgOrigIPIPBlockListPrvSec.setStatus("current")
_Ex2cfaMsgOrigIPIPBlockListSec_Type = Gauge32
_Ex2cfaMsgOrigIPIPBlockListSec_Object = MibScalar
ex2cfaMsgOrigIPIPBlockListSec = _Ex2cfaMsgOrigIPIPBlockListSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 10, 16),
    _Ex2cfaMsgOrigIPIPBlockListSec_Type()
)
ex2cfaMsgOrigIPIPBlockListSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2cfaMsgOrigIPIPBlockListSec.setStatus("current")
_Ex2ContentFilterAgent_ObjectIdentity = ObjectIdentity
ex2ContentFilterAgent = _Ex2ContentFilterAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11)
)
if mibBuilder.loadTexts:
    ex2ContentFilterAgent.setStatus("current")
_Ex2ctfaBypassRecptDueRecptSafSnd_Type = Gauge32
_Ex2ctfaBypassRecptDueRecptSafSnd_Object = MibScalar
ex2ctfaBypassRecptDueRecptSafSnd = _Ex2ctfaBypassRecptDueRecptSafSnd_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 1),
    _Ex2ctfaBypassRecptDueRecptSafSnd_Type()
)
ex2ctfaBypassRecptDueRecptSafSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaBypassRecptDueRecptSafSnd.setStatus("current")
_Ex2ctfaMessagesDeleted_Type = Gauge32
_Ex2ctfaMessagesDeleted_Object = MibScalar
ex2ctfaMessagesDeleted = _Ex2ctfaMessagesDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 2),
    _Ex2ctfaMessagesDeleted_Type()
)
ex2ctfaMessagesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesDeleted.setStatus("current")
_Ex2ctfaMessagesQuarantined_Type = Gauge32
_Ex2ctfaMessagesQuarantined_Object = MibScalar
ex2ctfaMessagesQuarantined = _Ex2ctfaMessagesQuarantined_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 3),
    _Ex2ctfaMessagesQuarantined_Type()
)
ex2ctfaMessagesQuarantined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesQuarantined.setStatus("current")
_Ex2ctfaMessagesRejected_Type = Gauge32
_Ex2ctfaMessagesRejected_Object = MibScalar
ex2ctfaMessagesRejected = _Ex2ctfaMessagesRejected_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 4),
    _Ex2ctfaMessagesRejected_Type()
)
ex2ctfaMessagesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesRejected.setStatus("current")
_Ex2ctfaMessagesScanned_Type = Gauge32
_Ex2ctfaMessagesScanned_Object = MibScalar
ex2ctfaMessagesScanned = _Ex2ctfaMessagesScanned_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 5),
    _Ex2ctfaMessagesScanned_Type()
)
ex2ctfaMessagesScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesScanned.setStatus("current")
_Ex2ctfaMessagesScannedPerSecond_Type = Gauge32
_Ex2ctfaMessagesScannedPerSecond_Object = MibScalar
ex2ctfaMessagesScannedPerSecond = _Ex2ctfaMessagesScannedPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 6),
    _Ex2ctfaMessagesScannedPerSecond_Type()
)
ex2ctfaMessagesScannedPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesScannedPerSecond.setStatus("current")
_Ex2ctfaMessageThatBypassScanning_Type = Gauge32
_Ex2ctfaMessageThatBypassScanning_Object = MibScalar
ex2ctfaMessageThatBypassScanning = _Ex2ctfaMessageThatBypassScanning_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 7),
    _Ex2ctfaMessageThatBypassScanning_Type()
)
ex2ctfaMessageThatBypassScanning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessageThatBypassScanning.setStatus("current")
_Ex2ctfaMsgBypassScanOrgWideSafe_Type = Gauge32
_Ex2ctfaMsgBypassScanOrgWideSafe_Object = MibScalar
ex2ctfaMsgBypassScanOrgWideSafe = _Ex2ctfaMsgBypassScanOrgWideSafe_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 8),
    _Ex2ctfaMsgBypassScanOrgWideSafe_Type()
)
ex2ctfaMsgBypassScanOrgWideSafe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMsgBypassScanOrgWideSafe.setStatus("current")
_Ex2ctfaMsgIncOtlkEMailPMNotValid_Type = Gauge32
_Ex2ctfaMsgIncOtlkEMailPMNotValid_Object = MibScalar
ex2ctfaMsgIncOtlkEMailPMNotValid = _Ex2ctfaMsgIncOtlkEMailPMNotValid_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 9),
    _Ex2ctfaMsgIncOtlkEMailPMNotValid_Type()
)
ex2ctfaMsgIncOtlkEMailPMNotValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMsgIncOtlkEMailPMNotValid.setStatus("current")
_Ex2ctfaMsgIncOtlkEMailPMValidScs_Type = Gauge32
_Ex2ctfaMsgIncOtlkEMailPMValidScs_Object = MibScalar
ex2ctfaMsgIncOtlkEMailPMValidScs = _Ex2ctfaMsgIncOtlkEMailPMValidScs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 10),
    _Ex2ctfaMsgIncOtlkEMailPMValidScs_Type()
)
ex2ctfaMsgIncOtlkEMailPMValidScs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMsgIncOtlkEMailPMValidScs.setStatus("current")
_Ex2ctfaMessagesWithSCL0_Type = Gauge32
_Ex2ctfaMessagesWithSCL0_Object = MibScalar
ex2ctfaMessagesWithSCL0 = _Ex2ctfaMessagesWithSCL0_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 11),
    _Ex2ctfaMessagesWithSCL0_Type()
)
ex2ctfaMessagesWithSCL0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesWithSCL0.setStatus("current")
_Ex2ctfaMessagesWithSCL1_Type = Gauge32
_Ex2ctfaMessagesWithSCL1_Object = MibScalar
ex2ctfaMessagesWithSCL1 = _Ex2ctfaMessagesWithSCL1_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 12),
    _Ex2ctfaMessagesWithSCL1_Type()
)
ex2ctfaMessagesWithSCL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesWithSCL1.setStatus("current")
_Ex2ctfaMessagesWithSCL2_Type = Gauge32
_Ex2ctfaMessagesWithSCL2_Object = MibScalar
ex2ctfaMessagesWithSCL2 = _Ex2ctfaMessagesWithSCL2_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 13),
    _Ex2ctfaMessagesWithSCL2_Type()
)
ex2ctfaMessagesWithSCL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesWithSCL2.setStatus("current")
_Ex2ctfaMessagesWithSCL3_Type = Gauge32
_Ex2ctfaMessagesWithSCL3_Object = MibScalar
ex2ctfaMessagesWithSCL3 = _Ex2ctfaMessagesWithSCL3_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 14),
    _Ex2ctfaMessagesWithSCL3_Type()
)
ex2ctfaMessagesWithSCL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesWithSCL3.setStatus("current")
_Ex2ctfaMessagesWithSCL4_Type = Gauge32
_Ex2ctfaMessagesWithSCL4_Object = MibScalar
ex2ctfaMessagesWithSCL4 = _Ex2ctfaMessagesWithSCL4_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 15),
    _Ex2ctfaMessagesWithSCL4_Type()
)
ex2ctfaMessagesWithSCL4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesWithSCL4.setStatus("current")
_Ex2ctfaMessagesWithSCL5_Type = Gauge32
_Ex2ctfaMessagesWithSCL5_Object = MibScalar
ex2ctfaMessagesWithSCL5 = _Ex2ctfaMessagesWithSCL5_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 16),
    _Ex2ctfaMessagesWithSCL5_Type()
)
ex2ctfaMessagesWithSCL5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesWithSCL5.setStatus("current")
_Ex2ctfaMessagesWithSCL6_Type = Gauge32
_Ex2ctfaMessagesWithSCL6_Object = MibScalar
ex2ctfaMessagesWithSCL6 = _Ex2ctfaMessagesWithSCL6_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 17),
    _Ex2ctfaMessagesWithSCL6_Type()
)
ex2ctfaMessagesWithSCL6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesWithSCL6.setStatus("current")
_Ex2ctfaMessagesWithSCL7_Type = Gauge32
_Ex2ctfaMessagesWithSCL7_Object = MibScalar
ex2ctfaMessagesWithSCL7 = _Ex2ctfaMessagesWithSCL7_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 18),
    _Ex2ctfaMessagesWithSCL7_Type()
)
ex2ctfaMessagesWithSCL7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesWithSCL7.setStatus("current")
_Ex2ctfaMessagesWithSCL8_Type = Gauge32
_Ex2ctfaMessagesWithSCL8_Object = MibScalar
ex2ctfaMessagesWithSCL8 = _Ex2ctfaMessagesWithSCL8_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 19),
    _Ex2ctfaMessagesWithSCL8_Type()
)
ex2ctfaMessagesWithSCL8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesWithSCL8.setStatus("current")
_Ex2ctfaMessagesWithSCL9_Type = Gauge32
_Ex2ctfaMessagesWithSCL9_Object = MibScalar
ex2ctfaMessagesWithSCL9 = _Ex2ctfaMessagesWithSCL9_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 20),
    _Ex2ctfaMessagesWithSCL9_Type()
)
ex2ctfaMessagesWithSCL9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesWithSCL9.setStatus("current")
_Ex2ctfaMessagesWithSCLUnknown_Type = Gauge32
_Ex2ctfaMessagesWithSCLUnknown_Object = MibScalar
ex2ctfaMessagesWithSCLUnknown = _Ex2ctfaMessagesWithSCLUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 21),
    _Ex2ctfaMessagesWithSCLUnknown_Type()
)
ex2ctfaMessagesWithSCLUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessagesWithSCLUnknown.setStatus("current")
_Ex2ctfaMessageWithPreexistingSCL_Type = Gauge32
_Ex2ctfaMessageWithPreexistingSCL_Object = MibScalar
ex2ctfaMessageWithPreexistingSCL = _Ex2ctfaMessageWithPreexistingSCL_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 11, 22),
    _Ex2ctfaMessageWithPreexistingSCL_Type()
)
ex2ctfaMessageWithPreexistingSCL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ctfaMessageWithPreexistingSCL.setStatus("current")
_Ex2DatabaseTable_Object = MibTable
ex2DatabaseTable = _Ex2DatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12)
)
if mibBuilder.loadTexts:
    ex2DatabaseTable.setStatus("current")
_Ex2DatabaseEntry_Object = MibTableRow
ex2DatabaseEntry = _Ex2DatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1)
)
ex2DatabaseEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2dbInstance"),
)
if mibBuilder.loadTexts:
    ex2DatabaseEntry.setStatus("current")
_Ex2dbInstance_Type = InstanceName
_Ex2dbInstance_Object = MibTableColumn
ex2dbInstance = _Ex2dbInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 1),
    _Ex2dbInstance_Type()
)
ex2dbInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbInstance.setStatus("current")
_Ex2dbDatabaseCachePercentHit_Type = Gauge32
_Ex2dbDatabaseCachePercentHit_Object = MibTableColumn
ex2dbDatabaseCachePercentHit = _Ex2dbDatabaseCachePercentHit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 2),
    _Ex2dbDatabaseCachePercentHit_Type()
)
ex2dbDatabaseCachePercentHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbDatabaseCachePercentHit.setStatus("current")
_Ex2dbDatabaseCacheSize_Type = Gauge32
_Ex2dbDatabaseCacheSize_Object = MibTableColumn
ex2dbDatabaseCacheSize = _Ex2dbDatabaseCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 3),
    _Ex2dbDatabaseCacheSize_Type()
)
ex2dbDatabaseCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbDatabaseCacheSize.setStatus("current")
_Ex2dbDatabaseCacheSizeMB_Type = Gauge32
_Ex2dbDatabaseCacheSizeMB_Object = MibTableColumn
ex2dbDatabaseCacheSizeMB = _Ex2dbDatabaseCacheSizeMB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 4),
    _Ex2dbDatabaseCacheSizeMB_Type()
)
ex2dbDatabaseCacheSizeMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbDatabaseCacheSizeMB.setStatus("current")
_Ex2dbDatabasePageEvictionsPerSec_Type = Gauge32
_Ex2dbDatabasePageEvictionsPerSec_Object = MibTableColumn
ex2dbDatabasePageEvictionsPerSec = _Ex2dbDatabasePageEvictionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 5),
    _Ex2dbDatabasePageEvictionsPerSec_Type()
)
ex2dbDatabasePageEvictionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbDatabasePageEvictionsPerSec.setStatus("current")
_Ex2dbDatabasePgFaultStallPerSec_Type = Gauge32
_Ex2dbDatabasePgFaultStallPerSec_Object = MibTableColumn
ex2dbDatabasePgFaultStallPerSec = _Ex2dbDatabasePgFaultStallPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 6),
    _Ex2dbDatabasePgFaultStallPerSec_Type()
)
ex2dbDatabasePgFaultStallPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbDatabasePgFaultStallPerSec.setStatus("current")
_Ex2dbDatabasePageFaultsPerSec_Type = Gauge32
_Ex2dbDatabasePageFaultsPerSec_Object = MibTableColumn
ex2dbDatabasePageFaultsPerSec = _Ex2dbDatabasePageFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 7),
    _Ex2dbDatabasePageFaultsPerSec_Type()
)
ex2dbDatabasePageFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbDatabasePageFaultsPerSec.setStatus("current")
_Ex2dbIODatabaseReadsAvgLatency_Type = Gauge32
_Ex2dbIODatabaseReadsAvgLatency_Object = MibTableColumn
ex2dbIODatabaseReadsAvgLatency = _Ex2dbIODatabaseReadsAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 8),
    _Ex2dbIODatabaseReadsAvgLatency_Type()
)
ex2dbIODatabaseReadsAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbIODatabaseReadsAvgLatency.setStatus("current")
_Ex2dbIODatabaseReadsPerSec_Type = Gauge32
_Ex2dbIODatabaseReadsPerSec_Object = MibTableColumn
ex2dbIODatabaseReadsPerSec = _Ex2dbIODatabaseReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 9),
    _Ex2dbIODatabaseReadsPerSec_Type()
)
ex2dbIODatabaseReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbIODatabaseReadsPerSec.setStatus("current")
_Ex2dbIODatabaseWriteAvgLatency_Type = Gauge32
_Ex2dbIODatabaseWriteAvgLatency_Object = MibTableColumn
ex2dbIODatabaseWriteAvgLatency = _Ex2dbIODatabaseWriteAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 10),
    _Ex2dbIODatabaseWriteAvgLatency_Type()
)
ex2dbIODatabaseWriteAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbIODatabaseWriteAvgLatency.setStatus("current")
_Ex2dbIODatabaseWritesPerSec_Type = Gauge32
_Ex2dbIODatabaseWritesPerSec_Object = MibTableColumn
ex2dbIODatabaseWritesPerSec = _Ex2dbIODatabaseWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 11),
    _Ex2dbIODatabaseWritesPerSec_Type()
)
ex2dbIODatabaseWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbIODatabaseWritesPerSec.setStatus("current")
_Ex2dbIOLogReadsPerSec_Type = Gauge32
_Ex2dbIOLogReadsPerSec_Object = MibTableColumn
ex2dbIOLogReadsPerSec = _Ex2dbIOLogReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 12),
    _Ex2dbIOLogReadsPerSec_Type()
)
ex2dbIOLogReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbIOLogReadsPerSec.setStatus("current")
_Ex2dbIOLogWritesAverageLatency_Type = Gauge32
_Ex2dbIOLogWritesAverageLatency_Object = MibTableColumn
ex2dbIOLogWritesAverageLatency = _Ex2dbIOLogWritesAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 13),
    _Ex2dbIOLogWritesAverageLatency_Type()
)
ex2dbIOLogWritesAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbIOLogWritesAverageLatency.setStatus("current")
_Ex2dbIOLogWritesPerSec_Type = Gauge32
_Ex2dbIOLogWritesPerSec_Object = MibTableColumn
ex2dbIOLogWritesPerSec = _Ex2dbIOLogWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 14),
    _Ex2dbIOLogWritesPerSec_Type()
)
ex2dbIOLogWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbIOLogWritesPerSec.setStatus("current")
_Ex2dbLogBytesWritePerSec_Type = Gauge32
_Ex2dbLogBytesWritePerSec_Object = MibTableColumn
ex2dbLogBytesWritePerSec = _Ex2dbLogBytesWritePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 15),
    _Ex2dbLogBytesWritePerSec_Type()
)
ex2dbLogBytesWritePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbLogBytesWritePerSec.setStatus("current")
_Ex2dbLogRecordStallsPerSec_Type = Gauge32
_Ex2dbLogRecordStallsPerSec_Object = MibTableColumn
ex2dbLogRecordStallsPerSec = _Ex2dbLogRecordStallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 16),
    _Ex2dbLogRecordStallsPerSec_Type()
)
ex2dbLogRecordStallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbLogRecordStallsPerSec.setStatus("current")
_Ex2dbLogThreadsWaiting_Type = Gauge32
_Ex2dbLogThreadsWaiting_Object = MibTableColumn
ex2dbLogThreadsWaiting = _Ex2dbLogThreadsWaiting_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 17),
    _Ex2dbLogThreadsWaiting_Type()
)
ex2dbLogThreadsWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbLogThreadsWaiting.setStatus("current")
_Ex2dbLogWritesPerSec_Type = Gauge32
_Ex2dbLogWritesPerSec_Object = MibTableColumn
ex2dbLogWritesPerSec = _Ex2dbLogWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 18),
    _Ex2dbLogWritesPerSec_Type()
)
ex2dbLogWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbLogWritesPerSec.setStatus("current")
_Ex2dbPagesConverted_Type = Gauge32
_Ex2dbPagesConverted_Object = MibTableColumn
ex2dbPagesConverted = _Ex2dbPagesConverted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 19),
    _Ex2dbPagesConverted_Type()
)
ex2dbPagesConverted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbPagesConverted.setStatus("current")
_Ex2dbPagesConvertedPerSec_Type = Gauge32
_Ex2dbPagesConvertedPerSec_Object = MibTableColumn
ex2dbPagesConvertedPerSec = _Ex2dbPagesConvertedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 20),
    _Ex2dbPagesConvertedPerSec_Type()
)
ex2dbPagesConvertedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbPagesConvertedPerSec.setStatus("current")
_Ex2dbRecordsConverted_Type = Gauge32
_Ex2dbRecordsConverted_Object = MibTableColumn
ex2dbRecordsConverted = _Ex2dbRecordsConverted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 21),
    _Ex2dbRecordsConverted_Type()
)
ex2dbRecordsConverted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbRecordsConverted.setStatus("current")
_Ex2dbRecordsConvertedPerSec_Type = Gauge32
_Ex2dbRecordsConvertedPerSec_Object = MibTableColumn
ex2dbRecordsConvertedPerSec = _Ex2dbRecordsConvertedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 22),
    _Ex2dbRecordsConvertedPerSec_Type()
)
ex2dbRecordsConvertedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbRecordsConvertedPerSec.setStatus("current")
_Ex2dbSessionsPercentUsed_Type = Gauge32
_Ex2dbSessionsPercentUsed_Object = MibTableColumn
ex2dbSessionsPercentUsed = _Ex2dbSessionsPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 23),
    _Ex2dbSessionsPercentUsed_Type()
)
ex2dbSessionsPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbSessionsPercentUsed.setStatus("current")
_Ex2dbSessionsInUse_Type = Gauge32
_Ex2dbSessionsInUse_Object = MibTableColumn
ex2dbSessionsInUse = _Ex2dbSessionsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 24),
    _Ex2dbSessionsInUse_Type()
)
ex2dbSessionsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbSessionsInUse.setStatus("current")
_Ex2dbTableOpenCachePercentHit_Type = Gauge32
_Ex2dbTableOpenCachePercentHit_Object = MibTableColumn
ex2dbTableOpenCachePercentHit = _Ex2dbTableOpenCachePercentHit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 25),
    _Ex2dbTableOpenCachePercentHit_Type()
)
ex2dbTableOpenCachePercentHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbTableOpenCachePercentHit.setStatus("current")
_Ex2dbTableOpenCacheHitsPerSec_Type = Gauge32
_Ex2dbTableOpenCacheHitsPerSec_Object = MibTableColumn
ex2dbTableOpenCacheHitsPerSec = _Ex2dbTableOpenCacheHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 26),
    _Ex2dbTableOpenCacheHitsPerSec_Type()
)
ex2dbTableOpenCacheHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbTableOpenCacheHitsPerSec.setStatus("current")
_Ex2dbTableOpenCacheMissesPerSec_Type = Gauge32
_Ex2dbTableOpenCacheMissesPerSec_Object = MibTableColumn
ex2dbTableOpenCacheMissesPerSec = _Ex2dbTableOpenCacheMissesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 27),
    _Ex2dbTableOpenCacheMissesPerSec_Type()
)
ex2dbTableOpenCacheMissesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbTableOpenCacheMissesPerSec.setStatus("current")
_Ex2dbTableOpensPerSec_Type = Gauge32
_Ex2dbTableOpensPerSec_Object = MibTableColumn
ex2dbTableOpensPerSec = _Ex2dbTableOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 28),
    _Ex2dbTableOpensPerSec_Type()
)
ex2dbTableOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbTableOpensPerSec.setStatus("current")
_Ex2dbVersionBucketsAllocated_Type = Gauge32
_Ex2dbVersionBucketsAllocated_Object = MibTableColumn
ex2dbVersionBucketsAllocated = _Ex2dbVersionBucketsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 12, 1, 29),
    _Ex2dbVersionBucketsAllocated_Type()
)
ex2dbVersionBucketsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbVersionBucketsAllocated.setStatus("current")
_Ex2DatabaseInstancesTable_Object = MibTable
ex2DatabaseInstancesTable = _Ex2DatabaseInstancesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13)
)
if mibBuilder.loadTexts:
    ex2DatabaseInstancesTable.setStatus("current")
_Ex2DatabaseInstancesEntry_Object = MibTableRow
ex2DatabaseInstancesEntry = _Ex2DatabaseInstancesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1)
)
ex2DatabaseInstancesEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2dbiInstance"),
)
if mibBuilder.loadTexts:
    ex2DatabaseInstancesEntry.setStatus("current")
_Ex2dbiInstance_Type = InstanceName
_Ex2dbiInstance_Object = MibTableColumn
ex2dbiInstance = _Ex2dbiInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 1),
    _Ex2dbiInstance_Type()
)
ex2dbiInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiInstance.setStatus("current")
_Ex2dbiIODatabaseRdAvgLatency_Type = Gauge32
_Ex2dbiIODatabaseRdAvgLatency_Object = MibTableColumn
ex2dbiIODatabaseRdAvgLatency = _Ex2dbiIODatabaseRdAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 2),
    _Ex2dbiIODatabaseRdAvgLatency_Type()
)
ex2dbiIODatabaseRdAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiIODatabaseRdAvgLatency.setStatus("current")
_Ex2dbiIODatabaseReadsPerSec_Type = Gauge32
_Ex2dbiIODatabaseReadsPerSec_Object = MibTableColumn
ex2dbiIODatabaseReadsPerSec = _Ex2dbiIODatabaseReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 3),
    _Ex2dbiIODatabaseReadsPerSec_Type()
)
ex2dbiIODatabaseReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiIODatabaseReadsPerSec.setStatus("current")
_Ex2dbiIODatabsWriteAvgLatency_Type = Gauge32
_Ex2dbiIODatabsWriteAvgLatency_Object = MibTableColumn
ex2dbiIODatabsWriteAvgLatency = _Ex2dbiIODatabsWriteAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 4),
    _Ex2dbiIODatabsWriteAvgLatency_Type()
)
ex2dbiIODatabsWriteAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiIODatabsWriteAvgLatency.setStatus("current")
_Ex2dbiIODatabaseWritesPerSec_Type = Gauge32
_Ex2dbiIODatabaseWritesPerSec_Object = MibTableColumn
ex2dbiIODatabaseWritesPerSec = _Ex2dbiIODatabaseWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 5),
    _Ex2dbiIODatabaseWritesPerSec_Type()
)
ex2dbiIODatabaseWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiIODatabaseWritesPerSec.setStatus("current")
_Ex2dbiIOLogReadsPerSec_Type = Gauge32
_Ex2dbiIOLogReadsPerSec_Object = MibTableColumn
ex2dbiIOLogReadsPerSec = _Ex2dbiIOLogReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 6),
    _Ex2dbiIOLogReadsPerSec_Type()
)
ex2dbiIOLogReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiIOLogReadsPerSec.setStatus("current")
_Ex2dbiIOLogWritesAvgLatency_Type = Gauge32
_Ex2dbiIOLogWritesAvgLatency_Object = MibTableColumn
ex2dbiIOLogWritesAvgLatency = _Ex2dbiIOLogWritesAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 7),
    _Ex2dbiIOLogWritesAvgLatency_Type()
)
ex2dbiIOLogWritesAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiIOLogWritesAvgLatency.setStatus("current")
_Ex2dbiIOLogWritesPerSec_Type = Gauge32
_Ex2dbiIOLogWritesPerSec_Object = MibTableColumn
ex2dbiIOLogWritesPerSec = _Ex2dbiIOLogWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 8),
    _Ex2dbiIOLogWritesPerSec_Type()
)
ex2dbiIOLogWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiIOLogWritesPerSec.setStatus("current")
_Ex2dbiLogBytesWritePerSec_Type = Gauge32
_Ex2dbiLogBytesWritePerSec_Object = MibTableColumn
ex2dbiLogBytesWritePerSec = _Ex2dbiLogBytesWritePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 9),
    _Ex2dbiLogBytesWritePerSec_Type()
)
ex2dbiLogBytesWritePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiLogBytesWritePerSec.setStatus("current")
_Ex2dbiLogFileCurrentGeneration_Type = Gauge32
_Ex2dbiLogFileCurrentGeneration_Object = MibTableColumn
ex2dbiLogFileCurrentGeneration = _Ex2dbiLogFileCurrentGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 10),
    _Ex2dbiLogFileCurrentGeneration_Type()
)
ex2dbiLogFileCurrentGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiLogFileCurrentGeneration.setStatus("current")
_Ex2dbiLogFilesGenerated_Type = Gauge32
_Ex2dbiLogFilesGenerated_Object = MibTableColumn
ex2dbiLogFilesGenerated = _Ex2dbiLogFilesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 11),
    _Ex2dbiLogFilesGenerated_Type()
)
ex2dbiLogFilesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiLogFilesGenerated.setStatus("current")
_Ex2dbiLogFilesGeneratedPremature_Type = Gauge32
_Ex2dbiLogFilesGeneratedPremature_Object = MibTableColumn
ex2dbiLogFilesGeneratedPremature = _Ex2dbiLogFilesGeneratedPremature_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 12),
    _Ex2dbiLogFilesGeneratedPremature_Type()
)
ex2dbiLogFilesGeneratedPremature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiLogFilesGeneratedPremature.setStatus("current")
_Ex2dbiLogGenerationCheckptDepth_Type = Gauge32
_Ex2dbiLogGenerationCheckptDepth_Object = MibTableColumn
ex2dbiLogGenerationCheckptDepth = _Ex2dbiLogGenerationCheckptDepth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 13),
    _Ex2dbiLogGenerationCheckptDepth_Type()
)
ex2dbiLogGenerationCheckptDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiLogGenerationCheckptDepth.setStatus("current")
_Ex2dbiLogGeneratnCheckptDepthMax_Type = Gauge32
_Ex2dbiLogGeneratnCheckptDepthMax_Object = MibTableColumn
ex2dbiLogGeneratnCheckptDepthMax = _Ex2dbiLogGeneratnCheckptDepthMax_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 14),
    _Ex2dbiLogGeneratnCheckptDepthMax_Type()
)
ex2dbiLogGeneratnCheckptDepthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiLogGeneratnCheckptDepthMax.setStatus("current")
_Ex2dbiLogGeneratLossResilient_Type = Gauge32
_Ex2dbiLogGeneratLossResilient_Object = MibTableColumn
ex2dbiLogGeneratLossResilient = _Ex2dbiLogGeneratLossResilient_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 15),
    _Ex2dbiLogGeneratLossResilient_Type()
)
ex2dbiLogGeneratLossResilient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiLogGeneratLossResilient.setStatus("current")
_Ex2dbiLogRecordStallsPerSec_Type = Gauge32
_Ex2dbiLogRecordStallsPerSec_Object = MibTableColumn
ex2dbiLogRecordStallsPerSec = _Ex2dbiLogRecordStallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 16),
    _Ex2dbiLogRecordStallsPerSec_Type()
)
ex2dbiLogRecordStallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiLogRecordStallsPerSec.setStatus("current")
_Ex2dbiLogThreadsWaiting_Type = Gauge32
_Ex2dbiLogThreadsWaiting_Object = MibTableColumn
ex2dbiLogThreadsWaiting = _Ex2dbiLogThreadsWaiting_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 17),
    _Ex2dbiLogThreadsWaiting_Type()
)
ex2dbiLogThreadsWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiLogThreadsWaiting.setStatus("current")
_Ex2dbiLogWritesPerSec_Type = Gauge32
_Ex2dbiLogWritesPerSec_Object = MibTableColumn
ex2dbiLogWritesPerSec = _Ex2dbiLogWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 18),
    _Ex2dbiLogWritesPerSec_Type()
)
ex2dbiLogWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiLogWritesPerSec.setStatus("current")
_Ex2dbiPagesConverted_Type = Gauge32
_Ex2dbiPagesConverted_Object = MibTableColumn
ex2dbiPagesConverted = _Ex2dbiPagesConverted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 19),
    _Ex2dbiPagesConverted_Type()
)
ex2dbiPagesConverted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiPagesConverted.setStatus("current")
_Ex2dbiPagesConvertedPerSec_Type = Gauge32
_Ex2dbiPagesConvertedPerSec_Object = MibTableColumn
ex2dbiPagesConvertedPerSec = _Ex2dbiPagesConvertedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 20),
    _Ex2dbiPagesConvertedPerSec_Type()
)
ex2dbiPagesConvertedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiPagesConvertedPerSec.setStatus("current")
_Ex2dbiRecordsConverted_Type = Gauge32
_Ex2dbiRecordsConverted_Object = MibTableColumn
ex2dbiRecordsConverted = _Ex2dbiRecordsConverted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 21),
    _Ex2dbiRecordsConverted_Type()
)
ex2dbiRecordsConverted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiRecordsConverted.setStatus("current")
_Ex2dbiRecordsConvertedPerSec_Type = Gauge32
_Ex2dbiRecordsConvertedPerSec_Object = MibTableColumn
ex2dbiRecordsConvertedPerSec = _Ex2dbiRecordsConvertedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 22),
    _Ex2dbiRecordsConvertedPerSec_Type()
)
ex2dbiRecordsConvertedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiRecordsConvertedPerSec.setStatus("current")
_Ex2dbiSessionsPercentUsed_Type = Gauge32
_Ex2dbiSessionsPercentUsed_Object = MibTableColumn
ex2dbiSessionsPercentUsed = _Ex2dbiSessionsPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 23),
    _Ex2dbiSessionsPercentUsed_Type()
)
ex2dbiSessionsPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiSessionsPercentUsed.setStatus("current")
_Ex2dbiSessionsInUse_Type = Gauge32
_Ex2dbiSessionsInUse_Object = MibTableColumn
ex2dbiSessionsInUse = _Ex2dbiSessionsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 24),
    _Ex2dbiSessionsInUse_Type()
)
ex2dbiSessionsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiSessionsInUse.setStatus("current")
_Ex2dbiStreamBackupPageReadPerSec_Type = Gauge32
_Ex2dbiStreamBackupPageReadPerSec_Object = MibTableColumn
ex2dbiStreamBackupPageReadPerSec = _Ex2dbiStreamBackupPageReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 25),
    _Ex2dbiStreamBackupPageReadPerSec_Type()
)
ex2dbiStreamBackupPageReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiStreamBackupPageReadPerSec.setStatus("current")
_Ex2dbiTableOpenCachePercentHit_Type = Gauge32
_Ex2dbiTableOpenCachePercentHit_Object = MibTableColumn
ex2dbiTableOpenCachePercentHit = _Ex2dbiTableOpenCachePercentHit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 26),
    _Ex2dbiTableOpenCachePercentHit_Type()
)
ex2dbiTableOpenCachePercentHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiTableOpenCachePercentHit.setStatus("current")
_Ex2dbiTableOpenCacheHitsPerSec_Type = Gauge32
_Ex2dbiTableOpenCacheHitsPerSec_Object = MibTableColumn
ex2dbiTableOpenCacheHitsPerSec = _Ex2dbiTableOpenCacheHitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 27),
    _Ex2dbiTableOpenCacheHitsPerSec_Type()
)
ex2dbiTableOpenCacheHitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiTableOpenCacheHitsPerSec.setStatus("current")
_Ex2dbiTableOpenCacheMissesPerSec_Type = Gauge32
_Ex2dbiTableOpenCacheMissesPerSec_Object = MibTableColumn
ex2dbiTableOpenCacheMissesPerSec = _Ex2dbiTableOpenCacheMissesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 28),
    _Ex2dbiTableOpenCacheMissesPerSec_Type()
)
ex2dbiTableOpenCacheMissesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiTableOpenCacheMissesPerSec.setStatus("current")
_Ex2dbiTableOpensPerSec_Type = Gauge32
_Ex2dbiTableOpensPerSec_Object = MibTableColumn
ex2dbiTableOpensPerSec = _Ex2dbiTableOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 29),
    _Ex2dbiTableOpensPerSec_Type()
)
ex2dbiTableOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiTableOpensPerSec.setStatus("current")
_Ex2dbiVersionBucketsAllocated_Type = Gauge32
_Ex2dbiVersionBucketsAllocated_Object = MibTableColumn
ex2dbiVersionBucketsAllocated = _Ex2dbiVersionBucketsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 13, 1, 30),
    _Ex2dbiVersionBucketsAllocated_Type()
)
ex2dbiVersionBucketsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbiVersionBucketsAllocated.setStatus("current")
_Ex2DatabaseTableClassesTable_Object = MibTable
ex2DatabaseTableClassesTable = _Ex2DatabaseTableClassesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 14)
)
if mibBuilder.loadTexts:
    ex2DatabaseTableClassesTable.setStatus("current")
_Ex2DatabaseTableClassesEntry_Object = MibTableRow
ex2DatabaseTableClassesEntry = _Ex2DatabaseTableClassesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 14, 1)
)
ex2DatabaseTableClassesEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2dbtcInstance"),
)
if mibBuilder.loadTexts:
    ex2DatabaseTableClassesEntry.setStatus("current")
_Ex2dbtcInstance_Type = InstanceName
_Ex2dbtcInstance_Object = MibTableColumn
ex2dbtcInstance = _Ex2dbtcInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 14, 1, 1),
    _Ex2dbtcInstance_Type()
)
ex2dbtcInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbtcInstance.setStatus("current")
_Ex2dbtcDatabaseCacheSizeMB_Type = Gauge32
_Ex2dbtcDatabaseCacheSizeMB_Object = MibTableColumn
ex2dbtcDatabaseCacheSizeMB = _Ex2dbtcDatabaseCacheSizeMB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 14, 1, 2),
    _Ex2dbtcDatabaseCacheSizeMB_Type()
)
ex2dbtcDatabaseCacheSizeMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2dbtcDatabaseCacheSizeMB.setStatus("current")
_Ex2ExtensibilityAgentsTable_Object = MibTable
ex2ExtensibilityAgentsTable = _Ex2ExtensibilityAgentsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 15)
)
if mibBuilder.loadTexts:
    ex2ExtensibilityAgentsTable.setStatus("current")
_Ex2ExtensibilityAgentsEntry_Object = MibTableRow
ex2ExtensibilityAgentsEntry = _Ex2ExtensibilityAgentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 15, 1)
)
ex2ExtensibilityAgentsEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2eaInstance"),
)
if mibBuilder.loadTexts:
    ex2ExtensibilityAgentsEntry.setStatus("current")
_Ex2eaInstance_Type = InstanceName
_Ex2eaInstance_Object = MibTableColumn
ex2eaInstance = _Ex2eaInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 15, 1, 1),
    _Ex2eaInstance_Type()
)
ex2eaInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2eaInstance.setStatus("current")
_Ex2eaAverageAgentProcessTimeSec_Type = Gauge32
_Ex2eaAverageAgentProcessTimeSec_Object = MibTableColumn
ex2eaAverageAgentProcessTimeSec = _Ex2eaAverageAgentProcessTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 15, 1, 2),
    _Ex2eaAverageAgentProcessTimeSec_Type()
)
ex2eaAverageAgentProcessTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2eaAverageAgentProcessTimeSec.setStatus("current")
_Ex2eaTotalAgentInvocations_Type = Gauge32
_Ex2eaTotalAgentInvocations_Object = MibTableColumn
ex2eaTotalAgentInvocations = _Ex2eaTotalAgentInvocations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 15, 1, 3),
    _Ex2eaTotalAgentInvocations_Type()
)
ex2eaTotalAgentInvocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2eaTotalAgentInvocations.setStatus("current")
_Ex2JournalingAgent_ObjectIdentity = ObjectIdentity
ex2JournalingAgent = _Ex2JournalingAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 16)
)
if mibBuilder.loadTexts:
    ex2JournalingAgent.setStatus("current")
_Ex2jaJournalReportsCreatedPerSec_Type = Gauge32
_Ex2jaJournalReportsCreatedPerSec_Object = MibScalar
ex2jaJournalReportsCreatedPerSec = _Ex2jaJournalReportsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 16, 1),
    _Ex2jaJournalReportsCreatedPerSec_Type()
)
ex2jaJournalReportsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2jaJournalReportsCreatedPerSec.setStatus("current")
_Ex2jaJournalReportsCreatedTotal_Type = Gauge32
_Ex2jaJournalReportsCreatedTotal_Object = MibScalar
ex2jaJournalReportsCreatedTotal = _Ex2jaJournalReportsCreatedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 16, 2),
    _Ex2jaJournalReportsCreatedTotal_Type()
)
ex2jaJournalReportsCreatedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2jaJournalReportsCreatedTotal.setStatus("current")
_Ex2jaJournalingProcessingTime_Type = Gauge32
_Ex2jaJournalingProcessingTime_Object = MibScalar
ex2jaJournalingProcessingTime = _Ex2jaJournalingProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 16, 3),
    _Ex2jaJournalingProcessingTime_Type()
)
ex2jaJournalingProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2jaJournalingProcessingTime.setStatus("current")
_Ex2jaJournalProcesTimePerMessage_Type = Gauge32
_Ex2jaJournalProcesTimePerMessage_Object = MibScalar
ex2jaJournalProcesTimePerMessage = _Ex2jaJournalProcesTimePerMessage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 16, 4),
    _Ex2jaJournalProcesTimePerMessage_Type()
)
ex2jaJournalProcesTimePerMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2jaJournalProcesTimePerMessage.setStatus("current")
_Ex2jaMessagesProcessByJournaling_Type = Gauge32
_Ex2jaMessagesProcessByJournaling_Object = MibScalar
ex2jaMessagesProcessByJournaling = _Ex2jaMessagesProcessByJournaling_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 16, 5),
    _Ex2jaMessagesProcessByJournaling_Type()
)
ex2jaMessagesProcessByJournaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2jaMessagesProcessByJournaling.setStatus("current")
_Ex2jaUsersJournaled_Type = Gauge32
_Ex2jaUsersJournaled_Object = MibScalar
ex2jaUsersJournaled = _Ex2jaUsersJournaled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 16, 6),
    _Ex2jaUsersJournaled_Type()
)
ex2jaUsersJournaled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2jaUsersJournaled.setStatus("current")
_Ex2jaUsersJournaledPerSec_Type = Gauge32
_Ex2jaUsersJournaledPerSec_Object = MibScalar
ex2jaUsersJournaledPerSec = _Ex2jaUsersJournaledPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 16, 7),
    _Ex2jaUsersJournaledPerSec_Type()
)
ex2jaUsersJournaledPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2jaUsersJournaledPerSec.setStatus("current")
_Ex2ManagedFolderAssistant_ObjectIdentity = ObjectIdentity
ex2ManagedFolderAssistant = _Ex2ManagedFolderAssistant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 17)
)
if mibBuilder.loadTexts:
    ex2ManagedFolderAssistant.setStatus("current")
_Ex2mfaItemsDeletedButRecoverable_Type = Gauge32
_Ex2mfaItemsDeletedButRecoverable_Object = MibScalar
ex2mfaItemsDeletedButRecoverable = _Ex2mfaItemsDeletedButRecoverable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 17, 1),
    _Ex2mfaItemsDeletedButRecoverable_Type()
)
ex2mfaItemsDeletedButRecoverable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mfaItemsDeletedButRecoverable.setStatus("current")
_Ex2mfaItemsJournaled_Type = Gauge32
_Ex2mfaItemsJournaled_Object = MibScalar
ex2mfaItemsJournaled = _Ex2mfaItemsJournaled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 17, 2),
    _Ex2mfaItemsJournaled_Type()
)
ex2mfaItemsJournaled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mfaItemsJournaled.setStatus("current")
_Ex2mfaItemsMarkPastRetentionDate_Type = Gauge32
_Ex2mfaItemsMarkPastRetentionDate_Object = MibScalar
ex2mfaItemsMarkPastRetentionDate = _Ex2mfaItemsMarkPastRetentionDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 17, 3),
    _Ex2mfaItemsMarkPastRetentionDate_Type()
)
ex2mfaItemsMarkPastRetentionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mfaItemsMarkPastRetentionDate.setStatus("current")
_Ex2mfaItemsMoved_Type = Gauge32
_Ex2mfaItemsMoved_Object = MibScalar
ex2mfaItemsMoved = _Ex2mfaItemsMoved_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 17, 4),
    _Ex2mfaItemsMoved_Type()
)
ex2mfaItemsMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mfaItemsMoved.setStatus("current")
_Ex2mfaItemsPermanentlyDeleted_Type = Gauge32
_Ex2mfaItemsPermanentlyDeleted_Object = MibScalar
ex2mfaItemsPermanentlyDeleted = _Ex2mfaItemsPermanentlyDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 17, 5),
    _Ex2mfaItemsPermanentlyDeleted_Type()
)
ex2mfaItemsPermanentlyDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mfaItemsPermanentlyDeleted.setStatus("current")
_Ex2mfaItemSubjectRetentionPolicy_Type = Gauge32
_Ex2mfaItemSubjectRetentionPolicy_Object = MibScalar
ex2mfaItemSubjectRetentionPolicy = _Ex2mfaItemSubjectRetentionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 17, 6),
    _Ex2mfaItemSubjectRetentionPolicy_Type()
)
ex2mfaItemSubjectRetentionPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mfaItemSubjectRetentionPolicy.setStatus("current")
_Ex2OWA_ObjectIdentity = ObjectIdentity
ex2OWA = _Ex2OWA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18)
)
if mibBuilder.loadTexts:
    ex2OWA.setStatus("current")
_Ex2OWAASQueries_Type = Gauge32
_Ex2OWAASQueries_Object = MibScalar
ex2OWAASQueries = _Ex2OWAASQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 1),
    _Ex2OWAASQueries_Type()
)
ex2OWAASQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAASQueries.setStatus("current")
_Ex2OWAASQueriesFailurePercent_Type = Gauge32
_Ex2OWAASQueriesFailurePercent_Object = MibScalar
ex2OWAASQueriesFailurePercent = _Ex2OWAASQueriesFailurePercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 2),
    _Ex2OWAASQueriesFailurePercent_Type()
)
ex2OWAASQueriesFailurePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAASQueriesFailurePercent.setStatus("current")
_Ex2OWAActiveConversions_Type = Gauge32
_Ex2OWAActiveConversions_Object = MibScalar
ex2OWAActiveConversions = _Ex2OWAActiveConversions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 3),
    _Ex2OWAActiveConversions_Type()
)
ex2OWAActiveConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAActiveConversions.setStatus("current")
_Ex2OWAAttachmentUploadedOWAStart_Type = Gauge32
_Ex2OWAAttachmentUploadedOWAStart_Object = MibScalar
ex2OWAAttachmentUploadedOWAStart = _Ex2OWAAttachmentUploadedOWAStart_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 4),
    _Ex2OWAAttachmentUploadedOWAStart_Type()
)
ex2OWAAttachmentUploadedOWAStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAAttachmentUploadedOWAStart.setStatus("current")
_Ex2OWAAverageCheckSpellingTime_Type = Gauge32
_Ex2OWAAverageCheckSpellingTime_Object = MibScalar
ex2OWAAverageCheckSpellingTime = _Ex2OWAAverageCheckSpellingTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 5),
    _Ex2OWAAverageCheckSpellingTime_Type()
)
ex2OWAAverageCheckSpellingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAAverageCheckSpellingTime.setStatus("current")
_Ex2OWAAverageConversionQueueTime_Type = Gauge32
_Ex2OWAAverageConversionQueueTime_Object = MibScalar
ex2OWAAverageConversionQueueTime = _Ex2OWAAverageConversionQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 6),
    _Ex2OWAAverageConversionQueueTime_Type()
)
ex2OWAAverageConversionQueueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAAverageConversionQueueTime.setStatus("current")
_Ex2OWAAverageConversionTime_Type = Gauge32
_Ex2OWAAverageConversionTime_Object = MibScalar
ex2OWAAverageConversionTime = _Ex2OWAAverageConversionTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 7),
    _Ex2OWAAverageConversionTime_Type()
)
ex2OWAAverageConversionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAAverageConversionTime.setStatus("current")
_Ex2OWAAverageResponseTime_Type = Gauge32
_Ex2OWAAverageResponseTime_Object = MibScalar
ex2OWAAverageResponseTime = _Ex2OWAAverageResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 8),
    _Ex2OWAAverageResponseTime_Type()
)
ex2OWAAverageResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAAverageResponseTime.setStatus("current")
_Ex2OWAAverageSearchTime_Type = Gauge32
_Ex2OWAAverageSearchTime_Object = MibScalar
ex2OWAAverageSearchTime = _Ex2OWAAverageSearchTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 9),
    _Ex2OWAAverageSearchTime_Type()
)
ex2OWAAverageSearchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAAverageSearchTime.setStatus("current")
_Ex2OWACalendarViewRefreshed_Type = Gauge32
_Ex2OWACalendarViewRefreshed_Object = MibScalar
ex2OWACalendarViewRefreshed = _Ex2OWACalendarViewRefreshed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 10),
    _Ex2OWACalendarViewRefreshed_Type()
)
ex2OWACalendarViewRefreshed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWACalendarViewRefreshed.setStatus("current")
_Ex2OWACalendarViewsLoaded_Type = Gauge32
_Ex2OWACalendarViewsLoaded_Object = MibScalar
ex2OWACalendarViewsLoaded = _Ex2OWACalendarViewsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 11),
    _Ex2OWACalendarViewsLoaded_Type()
)
ex2OWACalendarViewsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWACalendarViewsLoaded.setStatus("current")
_Ex2OWAConversionRequestsKBPerSec_Type = Gauge32
_Ex2OWAConversionRequestsKBPerSec_Object = MibScalar
ex2OWAConversionRequestsKBPerSec = _Ex2OWAConversionRequestsKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 12),
    _Ex2OWAConversionRequestsKBPerSec_Type()
)
ex2OWAConversionRequestsKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAConversionRequestsKBPerSec.setStatus("current")
_Ex2OWAConversionResponseKBPerSec_Type = Gauge32
_Ex2OWAConversionResponseKBPerSec_Object = MibScalar
ex2OWAConversionResponseKBPerSec = _Ex2OWAConversionResponseKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 13),
    _Ex2OWAConversionResponseKBPerSec_Type()
)
ex2OWAConversionResponseKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAConversionResponseKBPerSec.setStatus("current")
_Ex2OWAConversions_Type = Gauge32
_Ex2OWAConversions_Object = MibScalar
ex2OWAConversions = _Ex2OWAConversions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 14),
    _Ex2OWAConversions_Type()
)
ex2OWAConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAConversions.setStatus("current")
_Ex2OWAConversionsEndedByTimeOut_Type = Gauge32
_Ex2OWAConversionsEndedByTimeOut_Object = MibScalar
ex2OWAConversionsEndedByTimeOut = _Ex2OWAConversionsEndedByTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 15),
    _Ex2OWAConversionsEndedByTimeOut_Type()
)
ex2OWAConversionsEndedByTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAConversionsEndedByTimeOut.setStatus("current")
_Ex2OWAConversionsEndedWithErrors_Type = Gauge32
_Ex2OWAConversionsEndedWithErrors_Object = MibScalar
ex2OWAConversionsEndedWithErrors = _Ex2OWAConversionsEndedWithErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 16),
    _Ex2OWAConversionsEndedWithErrors_Type()
)
ex2OWAConversionsEndedWithErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAConversionsEndedWithErrors.setStatus("current")
_Ex2OWACurrentProxyUsers_Type = Gauge32
_Ex2OWACurrentProxyUsers_Object = MibScalar
ex2OWACurrentProxyUsers = _Ex2OWACurrentProxyUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 17),
    _Ex2OWACurrentProxyUsers_Type()
)
ex2OWACurrentProxyUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWACurrentProxyUsers.setStatus("current")
_Ex2OWACurrentUniqueUsers_Type = Gauge32
_Ex2OWACurrentUniqueUsers_Object = MibScalar
ex2OWACurrentUniqueUsers = _Ex2OWACurrentUniqueUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 18),
    _Ex2OWACurrentUniqueUsers_Type()
)
ex2OWACurrentUniqueUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWACurrentUniqueUsers.setStatus("current")
_Ex2OWACurrentUniqueUsersLight_Type = Gauge32
_Ex2OWACurrentUniqueUsersLight_Object = MibScalar
ex2OWACurrentUniqueUsersLight = _Ex2OWACurrentUniqueUsersLight_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 19),
    _Ex2OWACurrentUniqueUsersLight_Type()
)
ex2OWACurrentUniqueUsersLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWACurrentUniqueUsersLight.setStatus("current")
_Ex2OWACurrentUniqueUsersPremium_Type = Gauge32
_Ex2OWACurrentUniqueUsersPremium_Object = MibScalar
ex2OWACurrentUniqueUsersPremium = _Ex2OWACurrentUniqueUsersPremium_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 20),
    _Ex2OWACurrentUniqueUsersPremium_Type()
)
ex2OWACurrentUniqueUsersPremium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWACurrentUniqueUsersPremium.setStatus("current")
_Ex2OWACurrentUsers_Type = Gauge32
_Ex2OWACurrentUsers_Object = MibScalar
ex2OWACurrentUsers = _Ex2OWACurrentUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 21),
    _Ex2OWACurrentUsers_Type()
)
ex2OWACurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWACurrentUsers.setStatus("current")
_Ex2OWACurrentUsersLight_Type = Gauge32
_Ex2OWACurrentUsersLight_Object = MibScalar
ex2OWACurrentUsersLight = _Ex2OWACurrentUsersLight_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 22),
    _Ex2OWACurrentUsersLight_Type()
)
ex2OWACurrentUsersLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWACurrentUsersLight.setStatus("current")
_Ex2OWACurrentUsersPremium_Type = Gauge32
_Ex2OWACurrentUsersPremium_Object = MibScalar
ex2OWACurrentUsersPremium = _Ex2OWACurrentUsersPremium_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 23),
    _Ex2OWACurrentUsersPremium_Type()
)
ex2OWACurrentUsersPremium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWACurrentUsersPremium.setStatus("current")
_Ex2OWAFailedRequestsPerSec_Type = Gauge32
_Ex2OWAFailedRequestsPerSec_Object = MibScalar
ex2OWAFailedRequestsPerSec = _Ex2OWAFailedRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 24),
    _Ex2OWAFailedRequestsPerSec_Type()
)
ex2OWAFailedRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAFailedRequestsPerSec.setStatus("current")
_Ex2OWAInvalidCanaryRequests_Type = Gauge32
_Ex2OWAInvalidCanaryRequests_Object = MibScalar
ex2OWAInvalidCanaryRequests = _Ex2OWAInvalidCanaryRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 25),
    _Ex2OWAInvalidCanaryRequests_Type()
)
ex2OWAInvalidCanaryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAInvalidCanaryRequests.setStatus("current")
_Ex2OWAItemsCreatedSinceOWAStart_Type = Gauge32
_Ex2OWAItemsCreatedSinceOWAStart_Object = MibScalar
ex2OWAItemsCreatedSinceOWAStart = _Ex2OWAItemsCreatedSinceOWAStart_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 26),
    _Ex2OWAItemsCreatedSinceOWAStart_Type()
)
ex2OWAItemsCreatedSinceOWAStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAItemsCreatedSinceOWAStart.setStatus("current")
_Ex2OWAItemsDeletedSinceOWAStart_Type = Gauge32
_Ex2OWAItemsDeletedSinceOWAStart_Object = MibScalar
ex2OWAItemsDeletedSinceOWAStart = _Ex2OWAItemsDeletedSinceOWAStart_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 27),
    _Ex2OWAItemsDeletedSinceOWAStart_Type()
)
ex2OWAItemsDeletedSinceOWAStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAItemsDeletedSinceOWAStart.setStatus("current")
_Ex2OWAItemsUpdatedSinceOWAStart_Type = Gauge32
_Ex2OWAItemsUpdatedSinceOWAStart_Object = MibScalar
ex2OWAItemsUpdatedSinceOWAStart = _Ex2OWAItemsUpdatedSinceOWAStart_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 28),
    _Ex2OWAItemsUpdatedSinceOWAStart_Type()
)
ex2OWAItemsUpdatedSinceOWAStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAItemsUpdatedSinceOWAStart.setStatus("current")
_Ex2OWALogonsPerSec_Type = Gauge32
_Ex2OWALogonsPerSec_Object = MibScalar
ex2OWALogonsPerSec = _Ex2OWALogonsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 29),
    _Ex2OWALogonsPerSec_Type()
)
ex2OWALogonsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWALogonsPerSec.setStatus("current")
_Ex2OWALogonsPerSecLight_Type = Gauge32
_Ex2OWALogonsPerSecLight_Object = MibScalar
ex2OWALogonsPerSecLight = _Ex2OWALogonsPerSecLight_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 30),
    _Ex2OWALogonsPerSecLight_Type()
)
ex2OWALogonsPerSecLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWALogonsPerSecLight.setStatus("current")
_Ex2OWALogonsPerSecPremium_Type = Gauge32
_Ex2OWALogonsPerSecPremium_Object = MibScalar
ex2OWALogonsPerSecPremium = _Ex2OWALogonsPerSecPremium_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 31),
    _Ex2OWALogonsPerSecPremium_Type()
)
ex2OWALogonsPerSecPremium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWALogonsPerSecPremium.setStatus("current")
_Ex2OWAMailViewRefreshes_Type = Gauge32
_Ex2OWAMailViewRefreshes_Object = MibScalar
ex2OWAMailViewRefreshes = _Ex2OWAMailViewRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 32),
    _Ex2OWAMailViewRefreshes_Type()
)
ex2OWAMailViewRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAMailViewRefreshes.setStatus("current")
_Ex2OWAMailViewsLoaded_Type = Gauge32
_Ex2OWAMailViewsLoaded_Object = MibScalar
ex2OWAMailViewsLoaded = _Ex2OWAMailViewsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 33),
    _Ex2OWAMailViewsLoaded_Type()
)
ex2OWAMailViewsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAMailViewsLoaded.setStatus("current")
_Ex2OWAMessagesSent_Type = Gauge32
_Ex2OWAMessagesSent_Object = MibScalar
ex2OWAMessagesSent = _Ex2OWAMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 34),
    _Ex2OWAMessagesSent_Type()
)
ex2OWAMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAMessagesSent.setStatus("current")
_Ex2OWANamesChecked_Type = Gauge32
_Ex2OWANamesChecked_Object = MibScalar
ex2OWANamesChecked = _Ex2OWANamesChecked_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 35),
    _Ex2OWANamesChecked_Type()
)
ex2OWANamesChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWANamesChecked.setStatus("current")
_Ex2OWAPID_Type = Gauge32
_Ex2OWAPID_Object = MibScalar
ex2OWAPID = _Ex2OWAPID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 36),
    _Ex2OWAPID_Type()
)
ex2OWAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAPID.setStatus("current")
_Ex2OWAPasswordChanges_Type = Gauge32
_Ex2OWAPasswordChanges_Object = MibScalar
ex2OWAPasswordChanges = _Ex2OWAPasswordChanges_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 37),
    _Ex2OWAPasswordChanges_Type()
)
ex2OWAPasswordChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAPasswordChanges.setStatus("current")
_Ex2OWAPeakUserCount_Type = Gauge32
_Ex2OWAPeakUserCount_Object = MibScalar
ex2OWAPeakUserCount = _Ex2OWAPeakUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 38),
    _Ex2OWAPeakUserCount_Type()
)
ex2OWAPeakUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAPeakUserCount.setStatus("current")
_Ex2OWAPeakUserCountLight_Type = Gauge32
_Ex2OWAPeakUserCountLight_Object = MibScalar
ex2OWAPeakUserCountLight = _Ex2OWAPeakUserCountLight_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 39),
    _Ex2OWAPeakUserCountLight_Type()
)
ex2OWAPeakUserCountLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAPeakUserCountLight.setStatus("current")
_Ex2OWAPeakUserCountPremium_Type = Gauge32
_Ex2OWAPeakUserCountPremium_Object = MibScalar
ex2OWAPeakUserCountPremium = _Ex2OWAPeakUserCountPremium_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 40),
    _Ex2OWAPeakUserCountPremium_Type()
)
ex2OWAPeakUserCountPremium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAPeakUserCountPremium.setStatus("current")
_Ex2OWAProxyRequestBytes_Type = Gauge32
_Ex2OWAProxyRequestBytes_Object = MibScalar
ex2OWAProxyRequestBytes = _Ex2OWAProxyRequestBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 41),
    _Ex2OWAProxyRequestBytes_Type()
)
ex2OWAProxyRequestBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAProxyRequestBytes.setStatus("current")
_Ex2OWAProxyResponseBytes_Type = Gauge32
_Ex2OWAProxyResponseBytes_Object = MibScalar
ex2OWAProxyResponseBytes = _Ex2OWAProxyResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 42),
    _Ex2OWAProxyResponseBytes_Type()
)
ex2OWAProxyResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAProxyResponseBytes.setStatus("current")
_Ex2OWAProxyResponseTimeAverage_Type = Gauge32
_Ex2OWAProxyResponseTimeAverage_Object = MibScalar
ex2OWAProxyResponseTimeAverage = _Ex2OWAProxyResponseTimeAverage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 43),
    _Ex2OWAProxyResponseTimeAverage_Type()
)
ex2OWAProxyResponseTimeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAProxyResponseTimeAverage.setStatus("current")
_Ex2OWAProxyUserRequests_Type = Gauge32
_Ex2OWAProxyUserRequests_Object = MibScalar
ex2OWAProxyUserRequests = _Ex2OWAProxyUserRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 44),
    _Ex2OWAProxyUserRequests_Type()
)
ex2OWAProxyUserRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAProxyUserRequests.setStatus("current")
_Ex2OWAProxyUserRequestsPerSec_Type = Gauge32
_Ex2OWAProxyUserRequestsPerSec_Object = MibScalar
ex2OWAProxyUserRequestsPerSec = _Ex2OWAProxyUserRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 45),
    _Ex2OWAProxyUserRequestsPerSec_Type()
)
ex2OWAProxyUserRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAProxyUserRequestsPerSec.setStatus("current")
_Ex2OWAQueuedConversionRequests_Type = Gauge32
_Ex2OWAQueuedConversionRequests_Object = MibScalar
ex2OWAQueuedConversionRequests = _Ex2OWAQueuedConversionRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 46),
    _Ex2OWAQueuedConversionRequests_Type()
)
ex2OWAQueuedConversionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAQueuedConversionRequests.setStatus("current")
_Ex2OWARejectedConversions_Type = Gauge32
_Ex2OWARejectedConversions_Object = MibScalar
ex2OWARejectedConversions = _Ex2OWARejectedConversions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 47),
    _Ex2OWARejectedConversions_Type()
)
ex2OWARejectedConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWARejectedConversions.setStatus("current")
_Ex2OWARequests_Type = Gauge32
_Ex2OWARequests_Object = MibScalar
ex2OWARequests = _Ex2OWARequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 48),
    _Ex2OWARequests_Type()
)
ex2OWARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWARequests.setStatus("current")
_Ex2OWARequestsFailed_Type = Gauge32
_Ex2OWARequestsFailed_Object = MibScalar
ex2OWARequestsFailed = _Ex2OWARequestsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 49),
    _Ex2OWARequestsFailed_Type()
)
ex2OWARequestsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWARequestsFailed.setStatus("current")
_Ex2OWARequestsPerSec_Type = Gauge32
_Ex2OWARequestsPerSec_Object = MibScalar
ex2OWARequestsPerSec = _Ex2OWARequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 50),
    _Ex2OWARequestsPerSec_Type()
)
ex2OWARequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWARequestsPerSec.setStatus("current")
_Ex2OWASearches_Type = Gauge32
_Ex2OWASearches_Object = MibScalar
ex2OWASearches = _Ex2OWASearches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 51),
    _Ex2OWASearches_Type()
)
ex2OWASearches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWASearches.setStatus("current")
_Ex2OWASearchesExecuted_Type = Gauge32
_Ex2OWASearchesExecuted_Object = MibScalar
ex2OWASearchesExecuted = _Ex2OWASearchesExecuted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 52),
    _Ex2OWASearchesExecuted_Type()
)
ex2OWASearchesExecuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWASearchesExecuted.setStatus("current")
_Ex2OWASearchesTimedOut_Type = Gauge32
_Ex2OWASearchesTimedOut_Object = MibScalar
ex2OWASearchesTimedOut = _Ex2OWASearchesTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 53),
    _Ex2OWASearchesTimedOut_Type()
)
ex2OWASearchesTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWASearchesTimedOut.setStatus("current")
_Ex2OWASessionsEndedByLogoff_Type = Gauge32
_Ex2OWASessionsEndedByLogoff_Object = MibScalar
ex2OWASessionsEndedByLogoff = _Ex2OWASessionsEndedByLogoff_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 54),
    _Ex2OWASessionsEndedByLogoff_Type()
)
ex2OWASessionsEndedByLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWASessionsEndedByLogoff.setStatus("current")
_Ex2OWASessionsEndedByTimeOut_Type = Gauge32
_Ex2OWASessionsEndedByTimeOut_Object = MibScalar
ex2OWASessionsEndedByTimeOut = _Ex2OWASessionsEndedByTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 55),
    _Ex2OWASessionsEndedByTimeOut_Type()
)
ex2OWASessionsEndedByTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWASessionsEndedByTimeOut.setStatus("current")
_Ex2OWASpellingChecks_Type = Gauge32
_Ex2OWASpellingChecks_Object = MibScalar
ex2OWASpellingChecks = _Ex2OWASpellingChecks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 56),
    _Ex2OWASpellingChecks_Type()
)
ex2OWASpellingChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWASpellingChecks.setStatus("current")
_Ex2OWAStoreLogonFailurePercent_Type = Gauge32
_Ex2OWAStoreLogonFailurePercent_Object = MibScalar
ex2OWAStoreLogonFailurePercent = _Ex2OWAStoreLogonFailurePercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 57),
    _Ex2OWAStoreLogonFailurePercent_Type()
)
ex2OWAStoreLogonFailurePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAStoreLogonFailurePercent.setStatus("current")
_Ex2OWASuccessConversnReqKBPerSec_Type = Gauge32
_Ex2OWASuccessConversnReqKBPerSec_Object = MibScalar
ex2OWASuccessConversnReqKBPerSec = _Ex2OWASuccessConversnReqKBPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 58),
    _Ex2OWASuccessConversnReqKBPerSec_Type()
)
ex2OWASuccessConversnReqKBPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWASuccessConversnReqKBPerSec.setStatus("current")
_Ex2OWATotalUniqueUsers_Type = Gauge32
_Ex2OWATotalUniqueUsers_Object = MibScalar
ex2OWATotalUniqueUsers = _Ex2OWATotalUniqueUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 59),
    _Ex2OWATotalUniqueUsers_Type()
)
ex2OWATotalUniqueUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWATotalUniqueUsers.setStatus("current")
_Ex2OWATotalUniqueUsersLight_Type = Gauge32
_Ex2OWATotalUniqueUsersLight_Object = MibScalar
ex2OWATotalUniqueUsersLight = _Ex2OWATotalUniqueUsersLight_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 60),
    _Ex2OWATotalUniqueUsersLight_Type()
)
ex2OWATotalUniqueUsersLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWATotalUniqueUsersLight.setStatus("current")
_Ex2OWATotalUniqueUsersPremium_Type = Gauge32
_Ex2OWATotalUniqueUsersPremium_Object = MibScalar
ex2OWATotalUniqueUsersPremium = _Ex2OWATotalUniqueUsersPremium_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 61),
    _Ex2OWATotalUniqueUsersPremium_Type()
)
ex2OWATotalUniqueUsersPremium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWATotalUniqueUsersPremium.setStatus("current")
_Ex2OWATotalUsers_Type = Gauge32
_Ex2OWATotalUsers_Object = MibScalar
ex2OWATotalUsers = _Ex2OWATotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 62),
    _Ex2OWATotalUsers_Type()
)
ex2OWATotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWATotalUsers.setStatus("current")
_Ex2OWATotalUsersLight_Type = Gauge32
_Ex2OWATotalUsersLight_Object = MibScalar
ex2OWATotalUsersLight = _Ex2OWATotalUsersLight_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 63),
    _Ex2OWATotalUsersLight_Type()
)
ex2OWATotalUsersLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWATotalUsersLight.setStatus("current")
_Ex2OWATotalUsersPremium_Type = Gauge32
_Ex2OWATotalUsersPremium_Object = MibScalar
ex2OWATotalUsersPremium = _Ex2OWATotalUsersPremium_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 64),
    _Ex2OWATotalUsersPremium_Type()
)
ex2OWATotalUsersPremium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWATotalUsersPremium.setStatus("current")
_Ex2OWAUNCRequests_Type = Gauge32
_Ex2OWAUNCRequests_Object = MibScalar
ex2OWAUNCRequests = _Ex2OWAUNCRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 65),
    _Ex2OWAUNCRequests_Type()
)
ex2OWAUNCRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAUNCRequests.setStatus("current")
_Ex2OWAUNCResponseBytes_Type = Gauge32
_Ex2OWAUNCResponseBytes_Object = MibScalar
ex2OWAUNCResponseBytes = _Ex2OWAUNCResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 66),
    _Ex2OWAUNCResponseBytes_Type()
)
ex2OWAUNCResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAUNCResponseBytes.setStatus("current")
_Ex2OWAUNCResponseBytesPerSec_Type = Gauge32
_Ex2OWAUNCResponseBytesPerSec_Object = MibScalar
ex2OWAUNCResponseBytesPerSec = _Ex2OWAUNCResponseBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 67),
    _Ex2OWAUNCResponseBytesPerSec_Type()
)
ex2OWAUNCResponseBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAUNCResponseBytesPerSec.setStatus("current")
_Ex2OWAWSSRequests_Type = Gauge32
_Ex2OWAWSSRequests_Object = MibScalar
ex2OWAWSSRequests = _Ex2OWAWSSRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 68),
    _Ex2OWAWSSRequests_Type()
)
ex2OWAWSSRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAWSSRequests.setStatus("current")
_Ex2OWAWSSResponseBytes_Type = Gauge32
_Ex2OWAWSSResponseBytes_Object = MibScalar
ex2OWAWSSResponseBytes = _Ex2OWAWSSResponseBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 69),
    _Ex2OWAWSSResponseBytes_Type()
)
ex2OWAWSSResponseBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAWSSResponseBytes.setStatus("current")
_Ex2OWAWSSResponseBytesPerSec_Type = Gauge32
_Ex2OWAWSSResponseBytesPerSec_Object = MibScalar
ex2OWAWSSResponseBytesPerSec = _Ex2OWAWSSResponseBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 18, 70),
    _Ex2OWAWSSResponseBytesPerSec_Type()
)
ex2OWAWSSResponseBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2OWAWSSResponseBytesPerSec.setStatus("current")
_Ex2OledbEventsTable_Object = MibTable
ex2OledbEventsTable = _Ex2OledbEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 19)
)
if mibBuilder.loadTexts:
    ex2OledbEventsTable.setStatus("current")
_Ex2OledbEventsEntry_Object = MibTableRow
ex2OledbEventsEntry = _Ex2OledbEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 19, 1)
)
ex2OledbEventsEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2oeInstance"),
)
if mibBuilder.loadTexts:
    ex2OledbEventsEntry.setStatus("current")
_Ex2oeInstance_Type = InstanceName
_Ex2oeInstance_Object = MibTableColumn
ex2oeInstance = _Ex2oeInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 19, 1, 1),
    _Ex2oeInstance_Type()
)
ex2oeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2oeInstance.setStatus("current")
_Ex2oeEventsCompletionRate_Type = Gauge32
_Ex2oeEventsCompletionRate_Object = MibTableColumn
ex2oeEventsCompletionRate = _Ex2oeEventsCompletionRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 19, 1, 2),
    _Ex2oeEventsCompletionRate_Type()
)
ex2oeEventsCompletionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2oeEventsCompletionRate.setStatus("current")
_Ex2oeEventsCompletionTotal_Type = Gauge32
_Ex2oeEventsCompletionTotal_Object = MibTableColumn
ex2oeEventsCompletionTotal = _Ex2oeEventsCompletionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 19, 1, 3),
    _Ex2oeEventsCompletionTotal_Type()
)
ex2oeEventsCompletionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2oeEventsCompletionTotal.setStatus("current")
_Ex2oeEventsSubmissionRate_Type = Gauge32
_Ex2oeEventsSubmissionRate_Object = MibTableColumn
ex2oeEventsSubmissionRate = _Ex2oeEventsSubmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 19, 1, 4),
    _Ex2oeEventsSubmissionRate_Type()
)
ex2oeEventsSubmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2oeEventsSubmissionRate.setStatus("current")
_Ex2oeEventsSubmissionTotal_Type = Gauge32
_Ex2oeEventsSubmissionTotal_Object = MibTableColumn
ex2oeEventsSubmissionTotal = _Ex2oeEventsSubmissionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 19, 1, 5),
    _Ex2oeEventsSubmissionTotal_Type()
)
ex2oeEventsSubmissionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2oeEventsSubmissionTotal.setStatus("current")
_Ex2OledbResourceTable_Object = MibTable
ex2OledbResourceTable = _Ex2OledbResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20)
)
if mibBuilder.loadTexts:
    ex2OledbResourceTable.setStatus("current")
_Ex2OledbResourceEntry_Object = MibTableRow
ex2OledbResourceEntry = _Ex2OledbResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1)
)
ex2OledbResourceEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2orInstance"),
)
if mibBuilder.loadTexts:
    ex2OledbResourceEntry.setStatus("current")
_Ex2orInstance_Type = InstanceName
_Ex2orInstance_Object = MibTableColumn
ex2orInstance = _Ex2orInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 1),
    _Ex2orInstance_Type()
)
ex2orInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orInstance.setStatus("current")
_Ex2orActiveCommands_Type = Gauge32
_Ex2orActiveCommands_Object = MibTableColumn
ex2orActiveCommands = _Ex2orActiveCommands_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 2),
    _Ex2orActiveCommands_Type()
)
ex2orActiveCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orActiveCommands.setStatus("current")
_Ex2orActiveDataSources_Type = Gauge32
_Ex2orActiveDataSources_Object = MibTableColumn
ex2orActiveDataSources = _Ex2orActiveDataSources_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 3),
    _Ex2orActiveDataSources_Type()
)
ex2orActiveDataSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orActiveDataSources.setStatus("current")
_Ex2orActiveRows_Type = Gauge32
_Ex2orActiveRows_Object = MibTableColumn
ex2orActiveRows = _Ex2orActiveRows_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 4),
    _Ex2orActiveRows_Type()
)
ex2orActiveRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orActiveRows.setStatus("current")
_Ex2orActiveRowsets_Type = Gauge32
_Ex2orActiveRowsets_Object = MibTableColumn
ex2orActiveRowsets = _Ex2orActiveRowsets_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 5),
    _Ex2orActiveRowsets_Type()
)
ex2orActiveRowsets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orActiveRowsets.setStatus("current")
_Ex2orActiveSessions_Type = Gauge32
_Ex2orActiveSessions_Object = MibTableColumn
ex2orActiveSessions = _Ex2orActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 6),
    _Ex2orActiveSessions_Type()
)
ex2orActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orActiveSessions.setStatus("current")
_Ex2orActiveStreams_Type = Gauge32
_Ex2orActiveStreams_Object = MibTableColumn
ex2orActiveStreams = _Ex2orActiveStreams_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 7),
    _Ex2orActiveStreams_Type()
)
ex2orActiveStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orActiveStreams.setStatus("current")
_Ex2orResourceBindingsRate_Type = Gauge32
_Ex2orResourceBindingsRate_Object = MibTableColumn
ex2orResourceBindingsRate = _Ex2orResourceBindingsRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 8),
    _Ex2orResourceBindingsRate_Type()
)
ex2orResourceBindingsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orResourceBindingsRate.setStatus("current")
_Ex2orResourceBindingsTotal_Type = Gauge32
_Ex2orResourceBindingsTotal_Object = MibTableColumn
ex2orResourceBindingsTotal = _Ex2orResourceBindingsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 9),
    _Ex2orResourceBindingsTotal_Type()
)
ex2orResourceBindingsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orResourceBindingsTotal.setStatus("current")
_Ex2orRowsetsOpenedRate_Type = Gauge32
_Ex2orRowsetsOpenedRate_Object = MibTableColumn
ex2orRowsetsOpenedRate = _Ex2orRowsetsOpenedRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 10),
    _Ex2orRowsetsOpenedRate_Type()
)
ex2orRowsetsOpenedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orRowsetsOpenedRate.setStatus("current")
_Ex2orRowsetsOpenedTotal_Type = Gauge32
_Ex2orRowsetsOpenedTotal_Object = MibTableColumn
ex2orRowsetsOpenedTotal = _Ex2orRowsetsOpenedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 11),
    _Ex2orRowsetsOpenedTotal_Type()
)
ex2orRowsetsOpenedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orRowsetsOpenedTotal.setStatus("current")
_Ex2orTransactionsAbortedRate_Type = Gauge32
_Ex2orTransactionsAbortedRate_Object = MibTableColumn
ex2orTransactionsAbortedRate = _Ex2orTransactionsAbortedRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 12),
    _Ex2orTransactionsAbortedRate_Type()
)
ex2orTransactionsAbortedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orTransactionsAbortedRate.setStatus("current")
_Ex2orTransactionsAbortedTotal_Type = Gauge32
_Ex2orTransactionsAbortedTotal_Object = MibTableColumn
ex2orTransactionsAbortedTotal = _Ex2orTransactionsAbortedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 13),
    _Ex2orTransactionsAbortedTotal_Type()
)
ex2orTransactionsAbortedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orTransactionsAbortedTotal.setStatus("current")
_Ex2orTransactionsCommittedRate_Type = Gauge32
_Ex2orTransactionsCommittedRate_Object = MibTableColumn
ex2orTransactionsCommittedRate = _Ex2orTransactionsCommittedRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 14),
    _Ex2orTransactionsCommittedRate_Type()
)
ex2orTransactionsCommittedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orTransactionsCommittedRate.setStatus("current")
_Ex2orTransactionsCommittedTotal_Type = Gauge32
_Ex2orTransactionsCommittedTotal_Object = MibTableColumn
ex2orTransactionsCommittedTotal = _Ex2orTransactionsCommittedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 15),
    _Ex2orTransactionsCommittedTotal_Type()
)
ex2orTransactionsCommittedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orTransactionsCommittedTotal.setStatus("current")
_Ex2orTransactionsStartedRate_Type = Gauge32
_Ex2orTransactionsStartedRate_Object = MibTableColumn
ex2orTransactionsStartedRate = _Ex2orTransactionsStartedRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 16),
    _Ex2orTransactionsStartedRate_Type()
)
ex2orTransactionsStartedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orTransactionsStartedRate.setStatus("current")
_Ex2orTransactionsStartedTotal_Type = Gauge32
_Ex2orTransactionsStartedTotal_Object = MibTableColumn
ex2orTransactionsStartedTotal = _Ex2orTransactionsStartedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 20, 1, 17),
    _Ex2orTransactionsStartedTotal_Type()
)
ex2orTransactionsStartedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2orTransactionsStartedTotal.setStatus("current")
_Ex2ProtocolAnalysisAgent_ObjectIdentity = ObjectIdentity
ex2ProtocolAnalysisAgent = _Ex2ProtocolAnalysisAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21)
)
if mibBuilder.loadTexts:
    ex2ProtocolAnalysisAgent.setStatus("current")
_Ex2paaCalculationsAtSRL0_Type = Gauge32
_Ex2paaCalculationsAtSRL0_Object = MibScalar
ex2paaCalculationsAtSRL0 = _Ex2paaCalculationsAtSRL0_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 1),
    _Ex2paaCalculationsAtSRL0_Type()
)
ex2paaCalculationsAtSRL0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaCalculationsAtSRL0.setStatus("current")
_Ex2paaCalculationsAtSRL1_Type = Gauge32
_Ex2paaCalculationsAtSRL1_Object = MibScalar
ex2paaCalculationsAtSRL1 = _Ex2paaCalculationsAtSRL1_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 2),
    _Ex2paaCalculationsAtSRL1_Type()
)
ex2paaCalculationsAtSRL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaCalculationsAtSRL1.setStatus("current")
_Ex2paaCalculationsAtSRL2_Type = Gauge32
_Ex2paaCalculationsAtSRL2_Object = MibScalar
ex2paaCalculationsAtSRL2 = _Ex2paaCalculationsAtSRL2_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 3),
    _Ex2paaCalculationsAtSRL2_Type()
)
ex2paaCalculationsAtSRL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaCalculationsAtSRL2.setStatus("current")
_Ex2paaCalculationsAtSRL3_Type = Gauge32
_Ex2paaCalculationsAtSRL3_Object = MibScalar
ex2paaCalculationsAtSRL3 = _Ex2paaCalculationsAtSRL3_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 4),
    _Ex2paaCalculationsAtSRL3_Type()
)
ex2paaCalculationsAtSRL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaCalculationsAtSRL3.setStatus("current")
_Ex2paaCalculationsAtSRL4_Type = Gauge32
_Ex2paaCalculationsAtSRL4_Object = MibScalar
ex2paaCalculationsAtSRL4 = _Ex2paaCalculationsAtSRL4_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 5),
    _Ex2paaCalculationsAtSRL4_Type()
)
ex2paaCalculationsAtSRL4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaCalculationsAtSRL4.setStatus("current")
_Ex2paaCalculationsAtSRL5_Type = Gauge32
_Ex2paaCalculationsAtSRL5_Object = MibScalar
ex2paaCalculationsAtSRL5 = _Ex2paaCalculationsAtSRL5_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 6),
    _Ex2paaCalculationsAtSRL5_Type()
)
ex2paaCalculationsAtSRL5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaCalculationsAtSRL5.setStatus("current")
_Ex2paaCalculationsAtSRL6_Type = Gauge32
_Ex2paaCalculationsAtSRL6_Object = MibScalar
ex2paaCalculationsAtSRL6 = _Ex2paaCalculationsAtSRL6_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 7),
    _Ex2paaCalculationsAtSRL6_Type()
)
ex2paaCalculationsAtSRL6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaCalculationsAtSRL6.setStatus("current")
_Ex2paaCalculationsAtSRL7_Type = Gauge32
_Ex2paaCalculationsAtSRL7_Object = MibScalar
ex2paaCalculationsAtSRL7 = _Ex2paaCalculationsAtSRL7_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 8),
    _Ex2paaCalculationsAtSRL7_Type()
)
ex2paaCalculationsAtSRL7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaCalculationsAtSRL7.setStatus("current")
_Ex2paaCalculationsAtSRL8_Type = Gauge32
_Ex2paaCalculationsAtSRL8_Object = MibScalar
ex2paaCalculationsAtSRL8 = _Ex2paaCalculationsAtSRL8_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 9),
    _Ex2paaCalculationsAtSRL8_Type()
)
ex2paaCalculationsAtSRL8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaCalculationsAtSRL8.setStatus("current")
_Ex2paaCalculationsAtSRL9_Type = Gauge32
_Ex2paaCalculationsAtSRL9_Object = MibScalar
ex2paaCalculationsAtSRL9 = _Ex2paaCalculationsAtSRL9_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 10),
    _Ex2paaCalculationsAtSRL9_Type()
)
ex2paaCalculationsAtSRL9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaCalculationsAtSRL9.setStatus("current")
_Ex2paaSendersBlockLocalOpenProxy_Type = Gauge32
_Ex2paaSendersBlockLocalOpenProxy_Object = MibScalar
ex2paaSendersBlockLocalOpenProxy = _Ex2paaSendersBlockLocalOpenProxy_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 11),
    _Ex2paaSendersBlockLocalOpenProxy_Type()
)
ex2paaSendersBlockLocalOpenProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaSendersBlockLocalOpenProxy.setStatus("current")
_Ex2paaSendersBlockedOfLocalSRL_Type = Gauge32
_Ex2paaSendersBlockedOfLocalSRL_Object = MibScalar
ex2paaSendersBlockedOfLocalSRL = _Ex2paaSendersBlockedOfLocalSRL_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 12),
    _Ex2paaSendersBlockedOfLocalSRL_Type()
)
ex2paaSendersBlockedOfLocalSRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaSendersBlockedOfLocalSRL.setStatus("current")
_Ex2paaSenderBlockRemoteOpenProxy_Type = Gauge32
_Ex2paaSenderBlockRemoteOpenProxy_Object = MibScalar
ex2paaSenderBlockRemoteOpenProxy = _Ex2paaSenderBlockRemoteOpenProxy_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 13),
    _Ex2paaSenderBlockRemoteOpenProxy_Type()
)
ex2paaSenderBlockRemoteOpenProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaSenderBlockRemoteOpenProxy.setStatus("current")
_Ex2paaSendersBlockedOfRemoteSRL_Type = Gauge32
_Ex2paaSendersBlockedOfRemoteSRL_Object = MibScalar
ex2paaSendersBlockedOfRemoteSRL = _Ex2paaSendersBlockedOfRemoteSRL_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 14),
    _Ex2paaSendersBlockedOfRemoteSRL_Type()
)
ex2paaSendersBlockedOfRemoteSRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaSendersBlockedOfRemoteSRL.setStatus("current")
_Ex2paaSendersBypassLocalSRLCalc_Type = Gauge32
_Ex2paaSendersBypassLocalSRLCalc_Object = MibScalar
ex2paaSendersBypassLocalSRLCalc = _Ex2paaSendersBypassLocalSRLCalc_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 15),
    _Ex2paaSendersBypassLocalSRLCalc_Type()
)
ex2paaSendersBypassLocalSRLCalc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaSendersBypassLocalSRLCalc.setStatus("current")
_Ex2paaSendersProcessed_Type = Gauge32
_Ex2paaSendersProcessed_Object = MibScalar
ex2paaSendersProcessed = _Ex2paaSendersProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 21, 16),
    _Ex2paaSendersProcessed_Type()
)
ex2paaSendersProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2paaSendersProcessed.setStatus("current")
_Ex2ProtocolAnalysisBackgndAgent_ObjectIdentity = ObjectIdentity
ex2ProtocolAnalysisBackgndAgent = _Ex2ProtocolAnalysisBackgndAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 22)
)
if mibBuilder.loadTexts:
    ex2ProtocolAnalysisBackgndAgent.setStatus("current")
_Ex2RecipientCacheTable_Object = MibTable
ex2RecipientCacheTable = _Ex2RecipientCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 23)
)
if mibBuilder.loadTexts:
    ex2RecipientCacheTable.setStatus("current")
_Ex2RecipientCacheEntry_Object = MibTableRow
ex2RecipientCacheEntry = _Ex2RecipientCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 23, 1)
)
ex2RecipientCacheEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2rcInstance"),
)
if mibBuilder.loadTexts:
    ex2RecipientCacheEntry.setStatus("current")
_Ex2rcInstance_Type = InstanceName
_Ex2rcInstance_Object = MibTableColumn
ex2rcInstance = _Ex2rcInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 23, 1, 1),
    _Ex2rcInstance_Type()
)
ex2rcInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rcInstance.setStatus("current")
_Ex2rcAddressLookupsPending_Type = Gauge32
_Ex2rcAddressLookupsPending_Object = MibTableColumn
ex2rcAddressLookupsPending = _Ex2rcAddressLookupsPending_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 23, 1, 2),
    _Ex2rcAddressLookupsPending_Type()
)
ex2rcAddressLookupsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rcAddressLookupsPending.setStatus("current")
_Ex2rcBatchedAddressLookups_Type = Gauge32
_Ex2rcBatchedAddressLookups_Object = MibTableColumn
ex2rcBatchedAddressLookups = _Ex2rcBatchedAddressLookups_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 23, 1, 3),
    _Ex2rcBatchedAddressLookups_Type()
)
ex2rcBatchedAddressLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rcBatchedAddressLookups.setStatus("current")
_Ex2rcExpandGroupRequests_Type = Gauge32
_Ex2rcExpandGroupRequests_Object = MibTableColumn
ex2rcExpandGroupRequests = _Ex2rcExpandGroupRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 23, 1, 4),
    _Ex2rcExpandGroupRequests_Type()
)
ex2rcExpandGroupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rcExpandGroupRequests.setStatus("current")
_Ex2rcIndividualAddressLookups_Type = Gauge32
_Ex2rcIndividualAddressLookups_Object = MibTableColumn
ex2rcIndividualAddressLookups = _Ex2rcIndividualAddressLookups_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 23, 1, 5),
    _Ex2rcIndividualAddressLookups_Type()
)
ex2rcIndividualAddressLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rcIndividualAddressLookups.setStatus("current")
_Ex2RecipientFilterAgent_ObjectIdentity = ObjectIdentity
ex2RecipientFilterAgent = _Ex2RecipientFilterAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 24)
)
if mibBuilder.loadTexts:
    ex2RecipientFilterAgent.setStatus("current")
_Ex2rfaRecipientsRejectBlockList_Type = Gauge32
_Ex2rfaRecipientsRejectBlockList_Object = MibScalar
ex2rfaRecipientsRejectBlockList = _Ex2rfaRecipientsRejectBlockList_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 24, 1),
    _Ex2rfaRecipientsRejectBlockList_Type()
)
ex2rfaRecipientsRejectBlockList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rfaRecipientsRejectBlockList.setStatus("current")
_Ex2rfaRecipientRejectBlockLstSec_Type = Gauge32
_Ex2rfaRecipientRejectBlockLstSec_Object = MibScalar
ex2rfaRecipientRejectBlockLstSec = _Ex2rfaRecipientRejectBlockLstSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 24, 2),
    _Ex2rfaRecipientRejectBlockLstSec_Type()
)
ex2rfaRecipientRejectBlockLstSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rfaRecipientRejectBlockLstSec.setStatus("current")
_Ex2rfaRecpntRejectRecipientValid_Type = Gauge32
_Ex2rfaRecpntRejectRecipientValid_Object = MibScalar
ex2rfaRecpntRejectRecipientValid = _Ex2rfaRecpntRejectRecipientValid_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 24, 3),
    _Ex2rfaRecpntRejectRecipientValid_Type()
)
ex2rfaRecpntRejectRecipientValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rfaRecpntRejectRecipientValid.setStatus("current")
_Ex2rfaRecpntRejectRecpntValidSec_Type = Gauge32
_Ex2rfaRecpntRejectRecpntValidSec_Object = MibScalar
ex2rfaRecpntRejectRecpntValidSec = _Ex2rfaRecpntRejectRecpntValidSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 24, 4),
    _Ex2rfaRecpntRejectRecpntValidSec_Type()
)
ex2rfaRecpntRejectRecpntValidSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rfaRecpntRejectRecpntValidSec.setStatus("current")
_Ex2ReplicaSeederTable_Object = MibTable
ex2ReplicaSeederTable = _Ex2ReplicaSeederTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 25)
)
if mibBuilder.loadTexts:
    ex2ReplicaSeederTable.setStatus("current")
_Ex2ReplicaSeederEntry_Object = MibTableRow
ex2ReplicaSeederEntry = _Ex2ReplicaSeederEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 25, 1)
)
ex2ReplicaSeederEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2rsInstance"),
)
if mibBuilder.loadTexts:
    ex2ReplicaSeederEntry.setStatus("current")
_Ex2rsInstance_Type = InstanceName
_Ex2rsInstance_Object = MibTableColumn
ex2rsInstance = _Ex2rsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 25, 1, 1),
    _Ex2rsInstance_Type()
)
ex2rsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rsInstance.setStatus("current")
_Ex2rsSeedingFinishedPercent_Type = Gauge32
_Ex2rsSeedingFinishedPercent_Object = MibTableColumn
ex2rsSeedingFinishedPercent = _Ex2rsSeedingFinishedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 25, 1, 2),
    _Ex2rsSeedingFinishedPercent_Type()
)
ex2rsSeedingFinishedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rsSeedingFinishedPercent.setStatus("current")
_Ex2ReplicationTable_Object = MibTable
ex2ReplicationTable = _Ex2ReplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26)
)
if mibBuilder.loadTexts:
    ex2ReplicationTable.setStatus("current")
_Ex2ReplicationEntry_Object = MibTableRow
ex2ReplicationEntry = _Ex2ReplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1)
)
ex2ReplicationEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2rInstance"),
)
if mibBuilder.loadTexts:
    ex2ReplicationEntry.setStatus("current")
_Ex2rInstance_Type = InstanceName
_Ex2rInstance_Object = MibTableColumn
ex2rInstance = _Ex2rInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 1),
    _Ex2rInstance_Type()
)
ex2rInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rInstance.setStatus("current")
_Ex2rCopyQueExceedMntThresholdCCR_Type = Gauge32
_Ex2rCopyQueExceedMntThresholdCCR_Object = MibTableColumn
ex2rCopyQueExceedMntThresholdCCR = _Ex2rCopyQueExceedMntThresholdCCR_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 2),
    _Ex2rCopyQueExceedMntThresholdCCR_Type()
)
ex2rCopyQueExceedMntThresholdCCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rCopyQueExceedMntThresholdCCR.setStatus("current")
_Ex2rCopyGenerationNumber_Type = Gauge32
_Ex2rCopyGenerationNumber_Object = MibTableColumn
ex2rCopyGenerationNumber = _Ex2rCopyGenerationNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 3),
    _Ex2rCopyGenerationNumber_Type()
)
ex2rCopyGenerationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rCopyGenerationNumber.setStatus("current")
_Ex2rCopyNotifiyGenerationNumber_Type = Gauge32
_Ex2rCopyNotifiyGenerationNumber_Object = MibTableColumn
ex2rCopyNotifiyGenerationNumber = _Ex2rCopyNotifiyGenerationNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 4),
    _Ex2rCopyNotifiyGenerationNumber_Type()
)
ex2rCopyNotifiyGenerationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rCopyNotifiyGenerationNumber.setStatus("current")
_Ex2rCopyQueueLength_Type = Gauge32
_Ex2rCopyQueueLength_Object = MibTableColumn
ex2rCopyQueueLength = _Ex2rCopyQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 5),
    _Ex2rCopyQueueLength_Type()
)
ex2rCopyQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rCopyQueueLength.setStatus("current")
_Ex2rFailed_Type = Gauge32
_Ex2rFailed_Object = MibTableColumn
ex2rFailed = _Ex2rFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 6),
    _Ex2rFailed_Type()
)
ex2rFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rFailed.setStatus("current")
_Ex2rInitializing_Type = Gauge32
_Ex2rInitializing_Object = MibTableColumn
ex2rInitializing = _Ex2rInitializing_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 7),
    _Ex2rInitializing_Type()
)
ex2rInitializing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rInitializing.setStatus("current")
_Ex2rInspectorGenerationNumber_Type = Gauge32
_Ex2rInspectorGenerationNumber_Object = MibTableColumn
ex2rInspectorGenerationNumber = _Ex2rInspectorGenerationNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 8),
    _Ex2rInspectorGenerationNumber_Type()
)
ex2rInspectorGenerationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rInspectorGenerationNumber.setStatus("current")
_Ex2rReplayBatchSize_Type = Gauge32
_Ex2rReplayBatchSize_Object = MibTableColumn
ex2rReplayBatchSize = _Ex2rReplayBatchSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 9),
    _Ex2rReplayBatchSize_Type()
)
ex2rReplayBatchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rReplayBatchSize.setStatus("current")
_Ex2rReplayGenerationNumber_Type = Gauge32
_Ex2rReplayGenerationNumber_Object = MibTableColumn
ex2rReplayGenerationNumber = _Ex2rReplayGenerationNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 10),
    _Ex2rReplayGenerationNumber_Type()
)
ex2rReplayGenerationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rReplayGenerationNumber.setStatus("current")
_Ex2rReplayGenerationsComplete_Type = Gauge32
_Ex2rReplayGenerationsComplete_Object = MibTableColumn
ex2rReplayGenerationsComplete = _Ex2rReplayGenerationsComplete_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 11),
    _Ex2rReplayGenerationsComplete_Type()
)
ex2rReplayGenerationsComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rReplayGenerationsComplete.setStatus("current")
_Ex2rReplayGenerationsPerMinute_Type = Gauge32
_Ex2rReplayGenerationsPerMinute_Object = MibTableColumn
ex2rReplayGenerationsPerMinute = _Ex2rReplayGenerationsPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 12),
    _Ex2rReplayGenerationsPerMinute_Type()
)
ex2rReplayGenerationsPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rReplayGenerationsPerMinute.setStatus("current")
_Ex2rReplayGenerationsRemaining_Type = Gauge32
_Ex2rReplayGenerationsRemaining_Object = MibTableColumn
ex2rReplayGenerationsRemaining = _Ex2rReplayGenerationsRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 13),
    _Ex2rReplayGenerationsRemaining_Type()
)
ex2rReplayGenerationsRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rReplayGenerationsRemaining.setStatus("current")
_Ex2rReplayNotifyGenerationNumber_Type = Gauge32
_Ex2rReplayNotifyGenerationNumber_Object = MibTableColumn
ex2rReplayNotifyGenerationNumber = _Ex2rReplayNotifyGenerationNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 14),
    _Ex2rReplayNotifyGenerationNumber_Type()
)
ex2rReplayNotifyGenerationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rReplayNotifyGenerationNumber.setStatus("current")
_Ex2rReplayQueueLength_Type = Gauge32
_Ex2rReplayQueueLength_Object = MibTableColumn
ex2rReplayQueueLength = _Ex2rReplayQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 15),
    _Ex2rReplayQueueLength_Type()
)
ex2rReplayQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rReplayQueueLength.setStatus("current")
_Ex2rSuspended_Type = Gauge32
_Ex2rSuspended_Object = MibTableColumn
ex2rSuspended = _Ex2rSuspended_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 16),
    _Ex2rSuspended_Type()
)
ex2rSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rSuspended.setStatus("current")
_Ex2rTruncatedGenerationNumber_Type = Gauge32
_Ex2rTruncatedGenerationNumber_Object = MibTableColumn
ex2rTruncatedGenerationNumber = _Ex2rTruncatedGenerationNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 26, 1, 17),
    _Ex2rTruncatedGenerationNumber_Type()
)
ex2rTruncatedGenerationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rTruncatedGenerationNumber.setStatus("current")
_Ex2ResourceBooking_ObjectIdentity = ObjectIdentity
ex2ResourceBooking = _Ex2ResourceBooking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 27)
)
if mibBuilder.loadTexts:
    ex2ResourceBooking.setStatus("current")
_Ex2rbAccepted_Type = Gauge32
_Ex2rbAccepted_Object = MibScalar
ex2rbAccepted = _Ex2rbAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 27, 1),
    _Ex2rbAccepted_Type()
)
ex2rbAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rbAccepted.setStatus("current")
_Ex2rbAvgResourceBookProcessTime_Type = Gauge32
_Ex2rbAvgResourceBookProcessTime_Object = MibScalar
ex2rbAvgResourceBookProcessTime = _Ex2rbAvgResourceBookProcessTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 27, 2),
    _Ex2rbAvgResourceBookProcessTime_Type()
)
ex2rbAvgResourceBookProcessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rbAvgResourceBookProcessTime.setStatus("current")
_Ex2rbCancelled_Type = Gauge32
_Ex2rbCancelled_Object = MibScalar
ex2rbCancelled = _Ex2rbCancelled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 27, 3),
    _Ex2rbCancelled_Type()
)
ex2rbCancelled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rbCancelled.setStatus("current")
_Ex2rbDeclined_Type = Gauge32
_Ex2rbDeclined_Object = MibScalar
ex2rbDeclined = _Ex2rbDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 27, 4),
    _Ex2rbDeclined_Type()
)
ex2rbDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rbDeclined.setStatus("current")
_Ex2rbEvents_Type = Gauge32
_Ex2rbEvents_Object = MibScalar
ex2rbEvents = _Ex2rbEvents_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 27, 5),
    _Ex2rbEvents_Type()
)
ex2rbEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rbEvents.setStatus("current")
_Ex2rbRequestsFailed_Type = Gauge32
_Ex2rbRequestsFailed_Object = MibScalar
ex2rbRequestsFailed = _Ex2rbRequestsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 27, 6),
    _Ex2rbRequestsFailed_Type()
)
ex2rbRequestsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rbRequestsFailed.setStatus("current")
_Ex2rbRequestsProcessed_Type = Gauge32
_Ex2rbRequestsProcessed_Object = MibScalar
ex2rbRequestsProcessed = _Ex2rbRequestsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 27, 7),
    _Ex2rbRequestsProcessed_Type()
)
ex2rbRequestsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rbRequestsProcessed.setStatus("current")
_Ex2rbRequestsSubmitted_Type = Gauge32
_Ex2rbRequestsSubmitted_Object = MibScalar
ex2rbRequestsSubmitted = _Ex2rbRequestsSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 27, 8),
    _Ex2rbRequestsSubmitted_Type()
)
ex2rbRequestsSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2rbRequestsSubmitted.setStatus("current")
_Ex2SearchIndexer_ObjectIdentity = ObjectIdentity
ex2SearchIndexer = _Ex2SearchIndexer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 28)
)
if mibBuilder.loadTexts:
    ex2SearchIndexer.setStatus("current")
_Ex2sAverageBatchLatency_Type = Gauge32
_Ex2sAverageBatchLatency_Object = MibScalar
ex2sAverageBatchLatency = _Ex2sAverageBatchLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 28, 1),
    _Ex2sAverageBatchLatency_Type()
)
ex2sAverageBatchLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sAverageBatchLatency.setStatus("current")
_Ex2siAverageBatchSize_Type = Gauge32
_Ex2siAverageBatchSize_Object = MibScalar
ex2siAverageBatchSize = _Ex2siAverageBatchSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 28, 2),
    _Ex2siAverageBatchSize_Type()
)
ex2siAverageBatchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siAverageBatchSize.setStatus("current")
_Ex2siNumberDatabasesBeingCrawled_Type = Gauge32
_Ex2siNumberDatabasesBeingCrawled_Object = MibScalar
ex2siNumberDatabasesBeingCrawled = _Ex2siNumberDatabasesBeingCrawled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 28, 3),
    _Ex2siNumberDatabasesBeingCrawled_Type()
)
ex2siNumberDatabasesBeingCrawled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siNumberDatabasesBeingCrawled.setStatus("current")
_Ex2siNumberDatabasesBeingIndexed_Type = Gauge32
_Ex2siNumberDatabasesBeingIndexed_Object = MibScalar
ex2siNumberDatabasesBeingIndexed = _Ex2siNumberDatabasesBeingIndexed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 28, 4),
    _Ex2siNumberDatabasesBeingIndexed_Type()
)
ex2siNumberDatabasesBeingIndexed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siNumberDatabasesBeingIndexed.setStatus("current")
_Ex2siNumberOfDisabledDatabases_Type = Gauge32
_Ex2siNumberOfDisabledDatabases_Object = MibScalar
ex2siNumberOfDisabledDatabases = _Ex2siNumberOfDisabledDatabases_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 28, 5),
    _Ex2siNumberOfDisabledDatabases_Type()
)
ex2siNumberOfDisabledDatabases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siNumberOfDisabledDatabases.setStatus("current")
_Ex2siNumIndexDatabaseUpDateNotif_Type = Gauge32
_Ex2siNumIndexDatabaseUpDateNotif_Object = MibScalar
ex2siNumIndexDatabaseUpDateNotif = _Ex2siNumIndexDatabaseUpDateNotif_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 28, 6),
    _Ex2siNumIndexDatabaseUpDateNotif_Type()
)
ex2siNumIndexDatabaseUpDateNotif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siNumIndexDatabaseUpDateNotif.setStatus("current")
_Ex2SearchIndicesTable_Object = MibTable
ex2SearchIndicesTable = _Ex2SearchIndicesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29)
)
if mibBuilder.loadTexts:
    ex2SearchIndicesTable.setStatus("current")
_Ex2SearchIndicesEntry_Object = MibTableRow
ex2SearchIndicesEntry = _Ex2SearchIndicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1)
)
ex2SearchIndicesEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2sidInstance"),
)
if mibBuilder.loadTexts:
    ex2SearchIndicesEntry.setStatus("current")
_Ex2sidInstance_Type = InstanceName
_Ex2sidInstance_Object = MibTableColumn
ex2sidInstance = _Ex2sidInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 1),
    _Ex2sidInstance_Type()
)
ex2sidInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidInstance.setStatus("current")
_Ex2sidAgeLastNotificationIndexed_Type = Gauge32
_Ex2sidAgeLastNotificationIndexed_Object = MibTableColumn
ex2sidAgeLastNotificationIndexed = _Ex2sidAgeLastNotificationIndexed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 2),
    _Ex2sidAgeLastNotificationIndexed_Type()
)
ex2sidAgeLastNotificationIndexed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidAgeLastNotificationIndexed.setStatus("current")
_Ex2sidAgeLastNotificationProcess_Type = Gauge32
_Ex2sidAgeLastNotificationProcess_Object = MibTableColumn
ex2sidAgeLastNotificationProcess = _Ex2sidAgeLastNotificationProcess_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 3),
    _Ex2sidAgeLastNotificationProcess_Type()
)
ex2sidAgeLastNotificationProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidAgeLastNotificationProcess.setStatus("current")
_Ex2sidAvgLatencyRPCsDuringCrawl_Type = Gauge32
_Ex2sidAvgLatencyRPCsDuringCrawl_Object = MibTableColumn
ex2sidAvgLatencyRPCsDuringCrawl = _Ex2sidAvgLatencyRPCsDuringCrawl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 4),
    _Ex2sidAvgLatencyRPCsDuringCrawl_Type()
)
ex2sidAvgLatencyRPCsDuringCrawl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidAvgLatencyRPCsDuringCrawl.setStatus("current")
_Ex2sidAvgLatencyRPCObtainContent_Type = Gauge32
_Ex2sidAvgLatencyRPCObtainContent_Object = MibTableColumn
ex2sidAvgLatencyRPCObtainContent = _Ex2sidAvgLatencyRPCObtainContent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 5),
    _Ex2sidAvgLatencyRPCObtainContent_Type()
)
ex2sidAvgLatencyRPCObtainContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidAvgLatencyRPCObtainContent.setStatus("current")
_Ex2sidAverageDocumentIndexngTime_Type = Gauge32
_Ex2sidAverageDocumentIndexngTime_Object = MibTableColumn
ex2sidAverageDocumentIndexngTime = _Ex2sidAverageDocumentIndexngTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 6),
    _Ex2sidAverageDocumentIndexngTime_Type()
)
ex2sidAverageDocumentIndexngTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidAverageDocumentIndexngTime.setStatus("current")
_Ex2sidAvgLatencyRPCsToGetNotific_Type = Gauge32
_Ex2sidAvgLatencyRPCsToGetNotific_Object = MibTableColumn
ex2sidAvgLatencyRPCsToGetNotific = _Ex2sidAvgLatencyRPCsToGetNotific_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 7),
    _Ex2sidAvgLatencyRPCsToGetNotific_Type()
)
ex2sidAvgLatencyRPCsToGetNotific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidAvgLatencyRPCsToGetNotific.setStatus("current")
_Ex2sidAvgSizeOfIndexedAttachment_Type = Gauge32
_Ex2sidAvgSizeOfIndexedAttachment_Object = MibTableColumn
ex2sidAvgSizeOfIndexedAttachment = _Ex2sidAvgSizeOfIndexedAttachment_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 8),
    _Ex2sidAvgSizeOfIndexedAttachment_Type()
)
ex2sidAvgSizeOfIndexedAttachment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidAvgSizeOfIndexedAttachment.setStatus("current")
_Ex2sidDocumentIndexingRate_Type = Gauge32
_Ex2sidDocumentIndexingRate_Object = MibTableColumn
ex2sidDocumentIndexingRate = _Ex2sidDocumentIndexingRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 9),
    _Ex2sidDocumentIndexingRate_Type()
)
ex2sidDocumentIndexingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidDocumentIndexingRate.setStatus("current")
_Ex2sidFullCrawlModeStatus_Type = Gauge32
_Ex2sidFullCrawlModeStatus_Object = MibTableColumn
ex2sidFullCrawlModeStatus = _Ex2sidFullCrawlModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 10),
    _Ex2sidFullCrawlModeStatus_Type()
)
ex2sidFullCrawlModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidFullCrawlModeStatus.setStatus("current")
_Ex2sidNumContentConversionsDone_Type = Gauge32
_Ex2sidNumContentConversionsDone_Object = MibTableColumn
ex2sidNumContentConversionsDone = _Ex2sidNumContentConversionsDone_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 11),
    _Ex2sidNumContentConversionsDone_Type()
)
ex2sidNumContentConversionsDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumContentConversionsDone.setStatus("current")
_Ex2sidNumCreateNotifications_Type = Gauge32
_Ex2sidNumCreateNotifications_Object = MibTableColumn
ex2sidNumCreateNotifications = _Ex2sidNumCreateNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 12),
    _Ex2sidNumCreateNotifications_Type()
)
ex2sidNumCreateNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumCreateNotifications.setStatus("current")
_Ex2sidNumCreateNotificationPrSec_Type = Gauge32
_Ex2sidNumCreateNotificationPrSec_Object = MibTableColumn
ex2sidNumCreateNotificationPrSec = _Ex2sidNumCreateNotificationPrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 13),
    _Ex2sidNumCreateNotificationPrSec_Type()
)
ex2sidNumCreateNotificationPrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumCreateNotificationPrSec.setStatus("current")
_Ex2sidNumDeleteNotifications_Type = Gauge32
_Ex2sidNumDeleteNotifications_Object = MibTableColumn
ex2sidNumDeleteNotifications = _Ex2sidNumDeleteNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 14),
    _Ex2sidNumDeleteNotifications_Type()
)
ex2sidNumDeleteNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumDeleteNotifications.setStatus("current")
_Ex2sidNumDeleteNotificationPrSec_Type = Gauge32
_Ex2sidNumDeleteNotificationPrSec_Object = MibTableColumn
ex2sidNumDeleteNotificationPrSec = _Ex2sidNumDeleteNotificationPrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 15),
    _Ex2sidNumDeleteNotificationPrSec_Type()
)
ex2sidNumDeleteNotificationPrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumDeleteNotificationPrSec.setStatus("current")
_Ex2sidNumDocumentsSuccessIndexed_Type = Gauge32
_Ex2sidNumDocumentsSuccessIndexed_Object = MibTableColumn
ex2sidNumDocumentsSuccessIndexed = _Ex2sidNumDocumentsSuccessIndexed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 16),
    _Ex2sidNumDocumentsSuccessIndexed_Type()
)
ex2sidNumDocumentsSuccessIndexed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumDocumentsSuccessIndexed.setStatus("current")
_Ex2sidNumDocumentFailDuringIndex_Type = Gauge32
_Ex2sidNumDocumentFailDuringIndex_Object = MibTableColumn
ex2sidNumDocumentFailDuringIndex = _Ex2sidNumDocumentFailDuringIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 17),
    _Ex2sidNumDocumentFailDuringIndex_Type()
)
ex2sidNumDocumentFailDuringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumDocumentFailDuringIndex.setStatus("current")
_Ex2sidNumberOfFailedRetries_Type = Gauge32
_Ex2sidNumberOfFailedRetries_Object = MibTableColumn
ex2sidNumberOfFailedRetries = _Ex2sidNumberOfFailedRetries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 18),
    _Ex2sidNumberOfFailedRetries_Type()
)
ex2sidNumberOfFailedRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumberOfFailedRetries.setStatus("current")
_Ex2sidNumberOfHTMLMessageBodies_Type = Gauge32
_Ex2sidNumberOfHTMLMessageBodies_Object = MibTableColumn
ex2sidNumberOfHTMLMessageBodies = _Ex2sidNumberOfHTMLMessageBodies_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 19),
    _Ex2sidNumberOfHTMLMessageBodies_Type()
)
ex2sidNumberOfHTMLMessageBodies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumberOfHTMLMessageBodies.setStatus("current")
_Ex2sidNumberOfIndexedAttachments_Type = Gauge32
_Ex2sidNumberOfIndexedAttachments_Object = MibTableColumn
ex2sidNumberOfIndexedAttachments = _Ex2sidNumberOfIndexedAttachments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 20),
    _Ex2sidNumberOfIndexedAttachments_Type()
)
ex2sidNumberOfIndexedAttachments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumberOfIndexedAttachments.setStatus("current")
_Ex2sidNumItemInNotificationQueue_Type = Gauge32
_Ex2sidNumItemInNotificationQueue_Object = MibTableColumn
ex2sidNumItemInNotificationQueue = _Ex2sidNumItemInNotificationQueue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 21),
    _Ex2sidNumItemInNotificationQueue_Type()
)
ex2sidNumItemInNotificationQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumItemInNotificationQueue.setStatus("current")
_Ex2sidNumMailboxesLeftToCrawl_Type = Gauge32
_Ex2sidNumMailboxesLeftToCrawl_Object = MibTableColumn
ex2sidNumMailboxesLeftToCrawl = _Ex2sidNumMailboxesLeftToCrawl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 22),
    _Ex2sidNumMailboxesLeftToCrawl_Type()
)
ex2sidNumMailboxesLeftToCrawl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumMailboxesLeftToCrawl.setStatus("current")
_Ex2sidNumberOfMoveNotifications_Type = Gauge32
_Ex2sidNumberOfMoveNotifications_Object = MibTableColumn
ex2sidNumberOfMoveNotifications = _Ex2sidNumberOfMoveNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 23),
    _Ex2sidNumberOfMoveNotifications_Type()
)
ex2sidNumberOfMoveNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumberOfMoveNotifications.setStatus("current")
_Ex2sidNumMoveNotificationsPerSec_Type = Gauge32
_Ex2sidNumMoveNotificationsPerSec_Object = MibTableColumn
ex2sidNumMoveNotificationsPerSec = _Ex2sidNumMoveNotificationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 24),
    _Ex2sidNumMoveNotificationsPerSec_Type()
)
ex2sidNumMoveNotificationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumMoveNotificationsPerSec.setStatus("current")
_Ex2sidNumberOfOutstandingBatches_Type = Gauge32
_Ex2sidNumberOfOutstandingBatches_Object = MibTableColumn
ex2sidNumberOfOutstandingBatches = _Ex2sidNumberOfOutstandingBatches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 25),
    _Ex2sidNumberOfOutstandingBatches_Type()
)
ex2sidNumberOfOutstandingBatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumberOfOutstandingBatches.setStatus("current")
_Ex2sidNumOutstandingDocuments_Type = Gauge32
_Ex2sidNumOutstandingDocuments_Object = MibTableColumn
ex2sidNumOutstandingDocuments = _Ex2sidNumOutstandingDocuments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 26),
    _Ex2sidNumOutstandingDocuments_Type()
)
ex2sidNumOutstandingDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumOutstandingDocuments.setStatus("current")
_Ex2sidNumPlainTextMessageBodies_Type = Gauge32
_Ex2sidNumPlainTextMessageBodies_Object = MibTableColumn
ex2sidNumPlainTextMessageBodies = _Ex2sidNumPlainTextMessageBodies_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 27),
    _Ex2sidNumPlainTextMessageBodies_Type()
)
ex2sidNumPlainTextMessageBodies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumPlainTextMessageBodies.setStatus("current")
_Ex2sidNumberOfRTFMessageBodies_Type = Gauge32
_Ex2sidNumberOfRTFMessageBodies_Object = MibTableColumn
ex2sidNumberOfRTFMessageBodies = _Ex2sidNumberOfRTFMessageBodies_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 28),
    _Ex2sidNumberOfRTFMessageBodies_Type()
)
ex2sidNumberOfRTFMessageBodies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumberOfRTFMessageBodies.setStatus("current")
_Ex2sidNumRecentMoveMailboxCrawl_Type = Gauge32
_Ex2sidNumRecentMoveMailboxCrawl_Object = MibTableColumn
ex2sidNumRecentMoveMailboxCrawl = _Ex2sidNumRecentMoveMailboxCrawl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 29),
    _Ex2sidNumRecentMoveMailboxCrawl_Type()
)
ex2sidNumRecentMoveMailboxCrawl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumRecentMoveMailboxCrawl.setStatus("current")
_Ex2sidNumberOfRetries_Type = Gauge32
_Ex2sidNumberOfRetries_Object = MibTableColumn
ex2sidNumberOfRetries = _Ex2sidNumberOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 30),
    _Ex2sidNumberOfRetries_Type()
)
ex2sidNumberOfRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumberOfRetries.setStatus("current")
_Ex2sidNumberOfSuccessfulRetries_Type = Gauge32
_Ex2sidNumberOfSuccessfulRetries_Object = MibTableColumn
ex2sidNumberOfSuccessfulRetries = _Ex2sidNumberOfSuccessfulRetries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 31),
    _Ex2sidNumberOfSuccessfulRetries_Type()
)
ex2sidNumberOfSuccessfulRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumberOfSuccessfulRetries.setStatus("current")
_Ex2sidNumUpdateNotifications_Type = Gauge32
_Ex2sidNumUpdateNotifications_Object = MibTableColumn
ex2sidNumUpdateNotifications = _Ex2sidNumUpdateNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 32),
    _Ex2sidNumUpdateNotifications_Type()
)
ex2sidNumUpdateNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumUpdateNotifications.setStatus("current")
_Ex2sidNumUpdateNotificationPrSec_Type = Gauge32
_Ex2sidNumUpdateNotificationPrSec_Object = MibTableColumn
ex2sidNumUpdateNotificationPrSec = _Ex2sidNumUpdateNotificationPrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 33),
    _Ex2sidNumUpdateNotificationPrSec_Type()
)
ex2sidNumUpdateNotificationPrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidNumUpdateNotificationPrSec.setStatus("current")
_Ex2sidPercentageNotificOptimize_Type = Gauge32
_Ex2sidPercentageNotificOptimize_Object = MibTableColumn
ex2sidPercentageNotificOptimize = _Ex2sidPercentageNotificOptimize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 34),
    _Ex2sidPercentageNotificOptimize_Type()
)
ex2sidPercentageNotificOptimize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidPercentageNotificOptimize.setStatus("current")
_Ex2sidRecentAvgLatencyRPCUseObta_Type = Gauge32
_Ex2sidRecentAvgLatencyRPCUseObta_Object = MibTableColumn
ex2sidRecentAvgLatencyRPCUseObta = _Ex2sidRecentAvgLatencyRPCUseObta_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 35),
    _Ex2sidRecentAvgLatencyRPCUseObta_Type()
)
ex2sidRecentAvgLatencyRPCUseObta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidRecentAvgLatencyRPCUseObta.setStatus("current")
_Ex2sidThrottlingDelayValue_Type = Gauge32
_Ex2sidThrottlingDelayValue_Object = MibTableColumn
ex2sidThrottlingDelayValue = _Ex2sidThrottlingDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 29, 1, 36),
    _Ex2sidThrottlingDelayValue_Type()
)
ex2sidThrottlingDelayValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sidThrottlingDelayValue.setStatus("current")
_Ex2SecureMailTransportTable_Object = MibTable
ex2SecureMailTransportTable = _Ex2SecureMailTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 30)
)
if mibBuilder.loadTexts:
    ex2SecureMailTransportTable.setStatus("current")
_Ex2SecureMailTransportEntry_Object = MibTableRow
ex2SecureMailTransportEntry = _Ex2SecureMailTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 30, 1)
)
ex2SecureMailTransportEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2smtInstance"),
)
if mibBuilder.loadTexts:
    ex2SecureMailTransportEntry.setStatus("current")
_Ex2smtInstance_Type = InstanceName
_Ex2smtInstance_Object = MibTableColumn
ex2smtInstance = _Ex2smtInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 30, 1, 1),
    _Ex2smtInstance_Type()
)
ex2smtInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2smtInstance.setStatus("current")
_Ex2smtDomainSecureMessageReceive_Type = Gauge32
_Ex2smtDomainSecureMessageReceive_Object = MibTableColumn
ex2smtDomainSecureMessageReceive = _Ex2smtDomainSecureMessageReceive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 30, 1, 2),
    _Ex2smtDomainSecureMessageReceive_Type()
)
ex2smtDomainSecureMessageReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2smtDomainSecureMessageReceive.setStatus("current")
_Ex2smtDomainSecureMessagesSent_Type = Gauge32
_Ex2smtDomainSecureMessagesSent_Object = MibTableColumn
ex2smtDomainSecureMessagesSent = _Ex2smtDomainSecureMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 30, 1, 3),
    _Ex2smtDomainSecureMessagesSent_Type()
)
ex2smtDomainSecureMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2smtDomainSecureMessagesSent.setStatus("current")
_Ex2smtDomSecureOutbndSessionFail_Type = Gauge32
_Ex2smtDomSecureOutbndSessionFail_Object = MibTableColumn
ex2smtDomSecureOutbndSessionFail = _Ex2smtDomSecureOutbndSessionFail_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 30, 1, 4),
    _Ex2smtDomSecureOutbndSessionFail_Type()
)
ex2smtDomSecureOutbndSessionFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2smtDomSecureOutbndSessionFail.setStatus("current")
_Ex2SenderFilterAgent_ObjectIdentity = ObjectIdentity
ex2SenderFilterAgent = _Ex2SenderFilterAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 31)
)
_Ex2sfaMessagesEvalBySenderFilter_Type = Gauge32
_Ex2sfaMessagesEvalBySenderFilter_Object = MibScalar
ex2sfaMessagesEvalBySenderFilter = _Ex2sfaMessagesEvalBySenderFilter_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 31, 1),
    _Ex2sfaMessagesEvalBySenderFilter_Type()
)
ex2sfaMessagesEvalBySenderFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sfaMessagesEvalBySenderFilter.setStatus("current")
_Ex2sfaMsgEvaluatSendFilterPerSec_Type = Gauge32
_Ex2sfaMsgEvaluatSendFilterPerSec_Object = MibScalar
ex2sfaMsgEvaluatSendFilterPerSec = _Ex2sfaMsgEvaluatSendFilterPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 31, 2),
    _Ex2sfaMsgEvaluatSendFilterPerSec_Type()
)
ex2sfaMsgEvaluatSendFilterPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sfaMsgEvaluatSendFilterPerSec.setStatus("current")
_Ex2sfaMsgFilteredBySenderFilter_Type = Gauge32
_Ex2sfaMsgFilteredBySenderFilter_Object = MibScalar
ex2sfaMsgFilteredBySenderFilter = _Ex2sfaMsgFilteredBySenderFilter_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 31, 3),
    _Ex2sfaMsgFilteredBySenderFilter_Type()
)
ex2sfaMsgFilteredBySenderFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sfaMsgFilteredBySenderFilter.setStatus("current")
_Ex2sfaMsgFilterSenderFilterPrSec_Type = Gauge32
_Ex2sfaMsgFilterSenderFilterPrSec_Object = MibScalar
ex2sfaMsgFilterSenderFilterPrSec = _Ex2sfaMsgFilterSenderFilterPrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 31, 4),
    _Ex2sfaMsgFilterSenderFilterPrSec_Type()
)
ex2sfaMsgFilterSenderFilterPrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sfaMsgFilterSenderFilterPrSec.setStatus("current")
_Ex2SenderIdAgent_ObjectIdentity = ObjectIdentity
ex2SenderIdAgent = _Ex2SenderIdAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32)
)
_Ex2siaDNSQueries_Type = Gauge32
_Ex2siaDNSQueries_Object = MibScalar
ex2siaDNSQueries = _Ex2siaDNSQueries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 1),
    _Ex2siaDNSQueries_Type()
)
ex2siaDNSQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaDNSQueries.setStatus("current")
_Ex2siaDNSQueriesPerSec_Type = Gauge32
_Ex2siaDNSQueriesPerSec_Object = MibScalar
ex2siaDNSQueriesPerSec = _Ex2siaDNSQueriesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 2),
    _Ex2siaDNSQueriesPerSec_Type()
)
ex2siaDNSQueriesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaDNSQueriesPerSec.setStatus("current")
_Ex2siaMsgMissingOriginatingIP_Type = Gauge32
_Ex2siaMsgMissingOriginatingIP_Object = MibScalar
ex2siaMsgMissingOriginatingIP = _Ex2siaMsgMissingOriginatingIP_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 3),
    _Ex2siaMsgMissingOriginatingIP_Type()
)
ex2siaMsgMissingOriginatingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgMissingOriginatingIP.setStatus("current")
_Ex2siaMsgMissngOriginateIPPerSec_Type = Gauge32
_Ex2siaMsgMissngOriginateIPPerSec_Object = MibScalar
ex2siaMsgMissngOriginateIPPerSec = _Ex2siaMsgMissngOriginateIPPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 4),
    _Ex2siaMsgMissngOriginateIPPerSec_Type()
)
ex2siaMsgMissngOriginateIPPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgMissngOriginateIPPerSec.setStatus("current")
_Ex2siaMsgThatBypassedValidation_Type = Gauge32
_Ex2siaMsgThatBypassedValidation_Object = MibScalar
ex2siaMsgThatBypassedValidation = _Ex2siaMsgThatBypassedValidation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 5),
    _Ex2siaMsgThatBypassedValidation_Type()
)
ex2siaMsgThatBypassedValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgThatBypassedValidation.setStatus("current")
_Ex2siaMsgThatBypassValidatePrSec_Type = Gauge32
_Ex2siaMsgThatBypassValidatePrSec_Object = MibScalar
ex2siaMsgThatBypassValidatePrSec = _Ex2siaMsgThatBypassValidatePrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 6),
    _Ex2siaMsgThatBypassValidatePrSec_Type()
)
ex2siaMsgThatBypassValidatePrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgThatBypassValidatePrSec.setStatus("current")
_Ex2siaMessagesValidated_Type = Gauge32
_Ex2siaMessagesValidated_Object = MibScalar
ex2siaMessagesValidated = _Ex2siaMessagesValidated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 7),
    _Ex2siaMessagesValidated_Type()
)
ex2siaMessagesValidated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMessagesValidated.setStatus("current")
_Ex2siaMsgValidFailMalformDomRes_Type = Gauge32
_Ex2siaMsgValidFailMalformDomRes_Object = MibScalar
ex2siaMsgValidFailMalformDomRes = _Ex2siaMsgValidFailMalformDomRes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 8),
    _Ex2siaMsgValidFailMalformDomRes_Type()
)
ex2siaMsgValidFailMalformDomRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidFailMalformDomRes.setStatus("current")
_Ex2siaMsgValidFailNonExistDomRes_Type = Gauge32
_Ex2siaMsgValidFailNonExistDomRes_Object = MibScalar
ex2siaMsgValidFailNonExistDomRes = _Ex2siaMsgValidFailNonExistDomRes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 9),
    _Ex2siaMsgValidFailNonExistDomRes_Type()
)
ex2siaMsgValidFailNonExistDomRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidFailNonExistDomRes.setStatus("current")
_Ex2siaMsgValidFailNotPermittRes_Type = Gauge32
_Ex2siaMsgValidFailNotPermittRes_Object = MibScalar
ex2siaMsgValidFailNotPermittRes = _Ex2siaMsgValidFailNotPermittRes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 10),
    _Ex2siaMsgValidFailNotPermittRes_Type()
)
ex2siaMsgValidFailNotPermittRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidFailNotPermittRes.setStatus("current")
_Ex2siaMsgValidWithANeutralResult_Type = Gauge32
_Ex2siaMsgValidWithANeutralResult_Object = MibScalar
ex2siaMsgValidWithANeutralResult = _Ex2siaMsgValidWithANeutralResult_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 11),
    _Ex2siaMsgValidWithANeutralResult_Type()
)
ex2siaMsgValidWithANeutralResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidWithANeutralResult.setStatus("current")
_Ex2siaMsgValidWithANoneResult_Type = Gauge32
_Ex2siaMsgValidWithANoneResult_Object = MibScalar
ex2siaMsgValidWithANoneResult = _Ex2siaMsgValidWithANoneResult_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 12),
    _Ex2siaMsgValidWithANoneResult_Type()
)
ex2siaMsgValidWithANoneResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidWithANoneResult.setStatus("current")
_Ex2siaMsgValidWithAPassResult_Type = Gauge32
_Ex2siaMsgValidWithAPassResult_Object = MibScalar
ex2siaMsgValidWithAPassResult = _Ex2siaMsgValidWithAPassResult_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 13),
    _Ex2siaMsgValidWithAPassResult_Type()
)
ex2siaMsgValidWithAPassResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidWithAPassResult.setStatus("current")
_Ex2siaMsgValidPermErrorResult_Type = Gauge32
_Ex2siaMsgValidPermErrorResult_Object = MibScalar
ex2siaMsgValidPermErrorResult = _Ex2siaMsgValidPermErrorResult_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 14),
    _Ex2siaMsgValidPermErrorResult_Type()
)
ex2siaMsgValidPermErrorResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidPermErrorResult.setStatus("current")
_Ex2siaMsgValidSoftFailResult_Type = Gauge32
_Ex2siaMsgValidSoftFailResult_Object = MibScalar
ex2siaMsgValidSoftFailResult = _Ex2siaMsgValidSoftFailResult_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 15),
    _Ex2siaMsgValidSoftFailResult_Type()
)
ex2siaMsgValidSoftFailResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidSoftFailResult.setStatus("current")
_Ex2siaMsgValidTempErrorResult_Type = Gauge32
_Ex2siaMsgValidTempErrorResult_Object = MibScalar
ex2siaMsgValidTempErrorResult = _Ex2siaMsgValidTempErrorResult_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 16),
    _Ex2siaMsgValidTempErrorResult_Type()
)
ex2siaMsgValidTempErrorResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidTempErrorResult.setStatus("current")
_Ex2siaMessagesValidatedPerSec_Type = Gauge32
_Ex2siaMessagesValidatedPerSec_Object = MibScalar
ex2siaMessagesValidatedPerSec = _Ex2siaMessagesValidatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 17),
    _Ex2siaMessagesValidatedPerSec_Type()
)
ex2siaMessagesValidatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMessagesValidatedPerSec.setStatus("current")
_Ex2siaMsgValidFailMlfrmDomResSec_Type = Gauge32
_Ex2siaMsgValidFailMlfrmDomResSec_Object = MibScalar
ex2siaMsgValidFailMlfrmDomResSec = _Ex2siaMsgValidFailMlfrmDomResSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 18),
    _Ex2siaMsgValidFailMlfrmDomResSec_Type()
)
ex2siaMsgValidFailMlfrmDomResSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidFailMlfrmDomResSec.setStatus("current")
_Ex2siaMsgValidFailNExstDomResSec_Type = Gauge32
_Ex2siaMsgValidFailNExstDomResSec_Object = MibScalar
ex2siaMsgValidFailNExstDomResSec = _Ex2siaMsgValidFailNExstDomResSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 19),
    _Ex2siaMsgValidFailNExstDomResSec_Type()
)
ex2siaMsgValidFailNExstDomResSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidFailNExstDomResSec.setStatus("current")
_Ex2siaMsgValidFailNotPermitRes_Type = Gauge32
_Ex2siaMsgValidFailNotPermitRes_Object = MibScalar
ex2siaMsgValidFailNotPermitRes = _Ex2siaMsgValidFailNotPermitRes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 20),
    _Ex2siaMsgValidFailNotPermitRes_Type()
)
ex2siaMsgValidFailNotPermitRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidFailNotPermitRes.setStatus("current")
_Ex2siaMsgValidPerSecNeutrlResult_Type = Gauge32
_Ex2siaMsgValidPerSecNeutrlResult_Object = MibScalar
ex2siaMsgValidPerSecNeutrlResult = _Ex2siaMsgValidPerSecNeutrlResult_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 21),
    _Ex2siaMsgValidPerSecNeutrlResult_Type()
)
ex2siaMsgValidPerSecNeutrlResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidPerSecNeutrlResult.setStatus("current")
_Ex2siaMsgValidPerSecNoneResult_Type = Gauge32
_Ex2siaMsgValidPerSecNoneResult_Object = MibScalar
ex2siaMsgValidPerSecNoneResult = _Ex2siaMsgValidPerSecNoneResult_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 22),
    _Ex2siaMsgValidPerSecNoneResult_Type()
)
ex2siaMsgValidPerSecNoneResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidPerSecNoneResult.setStatus("current")
_Ex2siaMsgValidPerSecPassResult_Type = Gauge32
_Ex2siaMsgValidPerSecPassResult_Object = MibScalar
ex2siaMsgValidPerSecPassResult = _Ex2siaMsgValidPerSecPassResult_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 23),
    _Ex2siaMsgValidPerSecPassResult_Type()
)
ex2siaMsgValidPerSecPassResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidPerSecPassResult.setStatus("current")
_Ex2siaMsgValidSecPermErrorResult_Type = Gauge32
_Ex2siaMsgValidSecPermErrorResult_Object = MibScalar
ex2siaMsgValidSecPermErrorResult = _Ex2siaMsgValidSecPermErrorResult_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 24),
    _Ex2siaMsgValidSecPermErrorResult_Type()
)
ex2siaMsgValidSecPermErrorResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidSecPermErrorResult.setStatus("current")
_Ex2siaMsgValidPerSecSoftFailRes_Type = Gauge32
_Ex2siaMsgValidPerSecSoftFailRes_Object = MibScalar
ex2siaMsgValidPerSecSoftFailRes = _Ex2siaMsgValidPerSecSoftFailRes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 25),
    _Ex2siaMsgValidPerSecSoftFailRes_Type()
)
ex2siaMsgValidPerSecSoftFailRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidPerSecSoftFailRes.setStatus("current")
_Ex2siaMsgValidSecTempErrorResult_Type = Gauge32
_Ex2siaMsgValidSecTempErrorResult_Object = MibScalar
ex2siaMsgValidSecTempErrorResult = _Ex2siaMsgValidSecTempErrorResult_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 26),
    _Ex2siaMsgValidSecTempErrorResult_Type()
)
ex2siaMsgValidSecTempErrorResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMsgValidSecTempErrorResult.setStatus("current")
_Ex2siaMessagesWithNoPRAPerSec_Type = Gauge32
_Ex2siaMessagesWithNoPRAPerSec_Object = MibScalar
ex2siaMessagesWithNoPRAPerSec = _Ex2siaMessagesWithNoPRAPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 27),
    _Ex2siaMessagesWithNoPRAPerSec_Type()
)
ex2siaMessagesWithNoPRAPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMessagesWithNoPRAPerSec.setStatus("current")
_Ex2siaMessagesWithNoPRA_Type = Gauge32
_Ex2siaMessagesWithNoPRA_Object = MibScalar
ex2siaMessagesWithNoPRA = _Ex2siaMessagesWithNoPRA_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 32, 28),
    _Ex2siaMessagesWithNoPRA_Type()
)
ex2siaMessagesWithNoPRA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2siaMessagesWithNoPRA.setStatus("current")
_Ex2StoreDriverTable_Object = MibTable
ex2StoreDriverTable = _Ex2StoreDriverTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33)
)
if mibBuilder.loadTexts:
    ex2StoreDriverTable.setStatus("current")
_Ex2StoreDriverEntry_Object = MibTableRow
ex2StoreDriverEntry = _Ex2StoreDriverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1)
)
ex2StoreDriverEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2sdInstance"),
)
if mibBuilder.loadTexts:
    ex2StoreDriverEntry.setStatus("current")
_Ex2sdInstance_Type = InstanceName
_Ex2sdInstance_Object = MibTableColumn
ex2sdInstance = _Ex2sdInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 1),
    _Ex2sdInstance_Type()
)
ex2sdInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInstance.setStatus("current")
_Ex2sdInboundBytesDelivered_Type = Gauge32
_Ex2sdInboundBytesDelivered_Object = MibTableColumn
ex2sdInboundBytesDelivered = _Ex2sdInboundBytesDelivered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 2),
    _Ex2sdInboundBytesDelivered_Type()
)
ex2sdInboundBytesDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundBytesDelivered.setStatus("current")
_Ex2sdInboundDuplicateDeliveries_Type = Gauge32
_Ex2sdInboundDuplicateDeliveries_Object = MibTableColumn
ex2sdInboundDuplicateDeliveries = _Ex2sdInboundDuplicateDeliveries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 3),
    _Ex2sdInboundDuplicateDeliveries_Type()
)
ex2sdInboundDuplicateDeliveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundDuplicateDeliveries.setStatus("current")
_Ex2sdInboundFailedRecipients_Type = Gauge32
_Ex2sdInboundFailedRecipients_Object = MibTableColumn
ex2sdInboundFailedRecipients = _Ex2sdInboundFailedRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 4),
    _Ex2sdInboundFailedRecipients_Type()
)
ex2sdInboundFailedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundFailedRecipients.setStatus("current")
_Ex2sdInboundLocalDeliveryCalls_Type = Gauge32
_Ex2sdInboundLocalDeliveryCalls_Object = MibTableColumn
ex2sdInboundLocalDeliveryCalls = _Ex2sdInboundLocalDeliveryCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 5),
    _Ex2sdInboundLocalDeliveryCalls_Type()
)
ex2sdInboundLocalDeliveryCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundLocalDeliveryCalls.setStatus("current")
_Ex2sdInboundLocalDelivCallSecond_Type = Gauge32
_Ex2sdInboundLocalDelivCallSecond_Object = MibTableColumn
ex2sdInboundLocalDelivCallSecond = _Ex2sdInboundLocalDelivCallSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 6),
    _Ex2sdInboundLocalDelivCallSecond_Type()
)
ex2sdInboundLocalDelivCallSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundLocalDelivCallSecond.setStatus("current")
_Ex2sdInboundMsgDeliveryAttempts_Type = Gauge32
_Ex2sdInboundMsgDeliveryAttempts_Object = MibTableColumn
ex2sdInboundMsgDeliveryAttempts = _Ex2sdInboundMsgDeliveryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 7),
    _Ex2sdInboundMsgDeliveryAttempts_Type()
)
ex2sdInboundMsgDeliveryAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundMsgDeliveryAttempts.setStatus("current")
_Ex2sdInboundMsgDelvrAttmptSecond_Type = Gauge32
_Ex2sdInboundMsgDelvrAttmptSecond_Object = MibTableColumn
ex2sdInboundMsgDelvrAttmptSecond = _Ex2sdInboundMsgDelvrAttmptSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 8),
    _Ex2sdInboundMsgDelvrAttmptSecond_Type()
)
ex2sdInboundMsgDelvrAttmptSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundMsgDelvrAttmptSecond.setStatus("current")
_Ex2sdInboundNumDeliveringThreads_Type = Gauge32
_Ex2sdInboundNumDeliveringThreads_Object = MibTableColumn
ex2sdInboundNumDeliveringThreads = _Ex2sdInboundNumDeliveringThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 9),
    _Ex2sdInboundNumDeliveringThreads_Type()
)
ex2sdInboundNumDeliveringThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundNumDeliveringThreads.setStatus("current")
_Ex2sdInboundRecipientsDelivered_Type = Gauge32
_Ex2sdInboundRecipientsDelivered_Object = MibTableColumn
ex2sdInboundRecipientsDelivered = _Ex2sdInboundRecipientsDelivered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 10),
    _Ex2sdInboundRecipientsDelivered_Type()
)
ex2sdInboundRecipientsDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundRecipientsDelivered.setStatus("current")
_Ex2sdInboundRecipntDeliverSecond_Type = Gauge32
_Ex2sdInboundRecipntDeliverSecond_Object = MibTableColumn
ex2sdInboundRecipntDeliverSecond = _Ex2sdInboundRecipntDeliverSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 11),
    _Ex2sdInboundRecipntDeliverSecond_Type()
)
ex2sdInboundRecipntDeliverSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundRecipntDeliverSecond.setStatus("current")
_Ex2sdInboundReroutedRecipients_Type = Gauge32
_Ex2sdInboundReroutedRecipients_Object = MibTableColumn
ex2sdInboundReroutedRecipients = _Ex2sdInboundReroutedRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 12),
    _Ex2sdInboundReroutedRecipients_Type()
)
ex2sdInboundReroutedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundReroutedRecipients.setStatus("current")
_Ex2sdInboundRetriedRecipients_Type = Gauge32
_Ex2sdInboundRetriedRecipients_Object = MibTableColumn
ex2sdInboundRetriedRecipients = _Ex2sdInboundRetriedRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 13),
    _Ex2sdInboundRetriedRecipients_Type()
)
ex2sdInboundRetriedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundRetriedRecipients.setStatus("current")
_Ex2sdInboundSucceededRecipients_Type = Gauge32
_Ex2sdInboundSucceededRecipients_Object = MibTableColumn
ex2sdInboundSucceededRecipients = _Ex2sdInboundSucceededRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 14),
    _Ex2sdInboundSucceededRecipients_Type()
)
ex2sdInboundSucceededRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundSucceededRecipients.setStatus("current")
_Ex2sdInboundTotalMeetingFailures_Type = Gauge32
_Ex2sdInboundTotalMeetingFailures_Object = MibTableColumn
ex2sdInboundTotalMeetingFailures = _Ex2sdInboundTotalMeetingFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 15),
    _Ex2sdInboundTotalMeetingFailures_Type()
)
ex2sdInboundTotalMeetingFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundTotalMeetingFailures.setStatus("current")
_Ex2sdInboundTotalMeetingMessages_Type = Gauge32
_Ex2sdInboundTotalMeetingMessages_Object = MibTableColumn
ex2sdInboundTotalMeetingMessages = _Ex2sdInboundTotalMeetingMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 16),
    _Ex2sdInboundTotalMeetingMessages_Type()
)
ex2sdInboundTotalMeetingMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdInboundTotalMeetingMessages.setStatus("current")
_Ex2sdOutboundMapiEventWithoutMsg_Type = Gauge32
_Ex2sdOutboundMapiEventWithoutMsg_Object = MibTableColumn
ex2sdOutboundMapiEventWithoutMsg = _Ex2sdOutboundMapiEventWithoutMsg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 17),
    _Ex2sdOutboundMapiEventWithoutMsg_Type()
)
ex2sdOutboundMapiEventWithoutMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdOutboundMapiEventWithoutMsg.setStatus("current")
_Ex2sdOutboundSubmittedMailItems_Type = Gauge32
_Ex2sdOutboundSubmittedMailItems_Object = MibTableColumn
ex2sdOutboundSubmittedMailItems = _Ex2sdOutboundSubmittedMailItems_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 18),
    _Ex2sdOutboundSubmittedMailItems_Type()
)
ex2sdOutboundSubmittedMailItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdOutboundSubmittedMailItems.setStatus("current")
_Ex2sdOutboundSubmtMailItemSecond_Type = Gauge32
_Ex2sdOutboundSubmtMailItemSecond_Object = MibTableColumn
ex2sdOutboundSubmtMailItemSecond = _Ex2sdOutboundSubmtMailItemSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 19),
    _Ex2sdOutboundSubmtMailItemSecond_Type()
)
ex2sdOutboundSubmtMailItemSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdOutboundSubmtMailItemSecond.setStatus("current")
_Ex2sdOutboundTotalRecipients_Type = Gauge32
_Ex2sdOutboundTotalRecipients_Object = MibTableColumn
ex2sdOutboundTotalRecipients = _Ex2sdOutboundTotalRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 33, 1, 20),
    _Ex2sdOutboundTotalRecipients_Type()
)
ex2sdOutboundTotalRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sdOutboundTotalRecipients.setStatus("current")
_Ex2StoreInterfaceTable_Object = MibTable
ex2StoreInterfaceTable = _Ex2StoreInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34)
)
if mibBuilder.loadTexts:
    ex2StoreInterfaceTable.setStatus("current")
_Ex2StoreInterfaceEntry_Object = MibTableRow
ex2StoreInterfaceEntry = _Ex2StoreInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1)
)
ex2StoreInterfaceEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2sifInstance"),
)
if mibBuilder.loadTexts:
    ex2StoreInterfaceEntry.setStatus("current")
_Ex2sifInstance_Type = InstanceName
_Ex2sifInstance_Object = MibTableColumn
ex2sifInstance = _Ex2sifInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 1),
    _Ex2sifInstance_Type()
)
ex2sifInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifInstance.setStatus("current")
_Ex2sifConnCacheActiveConns_Type = Gauge32
_Ex2sifConnCacheActiveConns_Object = MibTableColumn
ex2sifConnCacheActiveConns = _Ex2sifConnCacheActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 2),
    _Ex2sifConnCacheActiveConns_Type()
)
ex2sifConnCacheActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifConnCacheActiveConns.setStatus("current")
_Ex2sifConnCacheIdleConns_Type = Gauge32
_Ex2sifConnCacheIdleConns_Object = MibTableColumn
ex2sifConnCacheIdleConns = _Ex2sifConnCacheIdleConns_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 3),
    _Ex2sifConnCacheIdleConns_Type()
)
ex2sifConnCacheIdleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifConnCacheIdleConns.setStatus("current")
_Ex2sifConnectionCacheNumCaches_Type = Gauge32
_Ex2sifConnectionCacheNumCaches_Object = MibTableColumn
ex2sifConnectionCacheNumCaches = _Ex2sifConnectionCacheNumCaches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 4),
    _Ex2sifConnectionCacheNumCaches_Type()
)
ex2sifConnectionCacheNumCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifConnectionCacheNumCaches.setStatus("current")
_Ex2sifConnCacheOutLimitCreations_Type = Gauge32
_Ex2sifConnCacheOutLimitCreations_Object = MibTableColumn
ex2sifConnCacheOutLimitCreations = _Ex2sifConnCacheOutLimitCreations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 5),
    _Ex2sifConnCacheOutLimitCreations_Type()
)
ex2sifConnCacheOutLimitCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifConnCacheOutLimitCreations.setStatus("current")
_Ex2sifConnCacheTotalCapacity_Type = Gauge32
_Ex2sifConnCacheTotalCapacity_Object = MibTableColumn
ex2sifConnCacheTotalCapacity = _Ex2sifConnCacheTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 6),
    _Ex2sifConnCacheTotalCapacity_Type()
)
ex2sifConnCacheTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifConnCacheTotalCapacity.setStatus("current")
_Ex2sifExRpcConnCreationEvents_Type = Gauge32
_Ex2sifExRpcConnCreationEvents_Object = MibTableColumn
ex2sifExRpcConnCreationEvents = _Ex2sifExRpcConnCreationEvents_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 7),
    _Ex2sifExRpcConnCreationEvents_Type()
)
ex2sifExRpcConnCreationEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifExRpcConnCreationEvents.setStatus("current")
_Ex2sifExRpcConnDisposalEvents_Type = Gauge32
_Ex2sifExRpcConnDisposalEvents_Object = MibTableColumn
ex2sifExRpcConnDisposalEvents = _Ex2sifExRpcConnDisposalEvents_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 8),
    _Ex2sifExRpcConnDisposalEvents_Type()
)
ex2sifExRpcConnDisposalEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifExRpcConnDisposalEvents.setStatus("current")
_Ex2sifExRpcConnectionOutstanding_Type = Gauge32
_Ex2sifExRpcConnectionOutstanding_Object = MibTableColumn
ex2sifExRpcConnectionOutstanding = _Ex2sifExRpcConnectionOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 9),
    _Ex2sifExRpcConnectionOutstanding_Type()
)
ex2sifExRpcConnectionOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifExRpcConnectionOutstanding.setStatus("current")
_Ex2sifROPRequestsComplete_Type = Gauge32
_Ex2sifROPRequestsComplete_Object = MibTableColumn
ex2sifROPRequestsComplete = _Ex2sifROPRequestsComplete_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 10),
    _Ex2sifROPRequestsComplete_Type()
)
ex2sifROPRequestsComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifROPRequestsComplete.setStatus("current")
_Ex2sifROPRequestsOutstanding_Type = Gauge32
_Ex2sifROPRequestsOutstanding_Object = MibTableColumn
ex2sifROPRequestsOutstanding = _Ex2sifROPRequestsOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 11),
    _Ex2sifROPRequestsOutstanding_Type()
)
ex2sifROPRequestsOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifROPRequestsOutstanding.setStatus("current")
_Ex2sifROPRequestsSent_Type = Gauge32
_Ex2sifROPRequestsSent_Object = MibTableColumn
ex2sifROPRequestsSent = _Ex2sifROPRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 12),
    _Ex2sifROPRequestsSent_Type()
)
ex2sifROPRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifROPRequestsSent.setStatus("current")
_Ex2sifRPCBytesReceived_Type = Gauge32
_Ex2sifRPCBytesReceived_Object = MibTableColumn
ex2sifRPCBytesReceived = _Ex2sifRPCBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 13),
    _Ex2sifRPCBytesReceived_Type()
)
ex2sifRPCBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCBytesReceived.setStatus("current")
_Ex2sifRPCBytesReceivedAverage_Type = Gauge32
_Ex2sifRPCBytesReceivedAverage_Object = MibTableColumn
ex2sifRPCBytesReceivedAverage = _Ex2sifRPCBytesReceivedAverage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 14),
    _Ex2sifRPCBytesReceivedAverage_Type()
)
ex2sifRPCBytesReceivedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCBytesReceivedAverage.setStatus("current")
_Ex2sifRPCBytesSent_Type = Gauge32
_Ex2sifRPCBytesSent_Object = MibTableColumn
ex2sifRPCBytesSent = _Ex2sifRPCBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 15),
    _Ex2sifRPCBytesSent_Type()
)
ex2sifRPCBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCBytesSent.setStatus("current")
_Ex2sifRPCBytesSentAverage_Type = Gauge32
_Ex2sifRPCBytesSentAverage_Object = MibTableColumn
ex2sifRPCBytesSentAverage = _Ex2sifRPCBytesSentAverage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 16),
    _Ex2sifRPCBytesSentAverage_Type()
)
ex2sifRPCBytesSentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCBytesSentAverage.setStatus("current")
_Ex2sifRPCLatencyAverageMsec_Type = Gauge32
_Ex2sifRPCLatencyAverageMsec_Object = MibTableColumn
ex2sifRPCLatencyAverageMsec = _Ex2sifRPCLatencyAverageMsec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 17),
    _Ex2sifRPCLatencyAverageMsec_Type()
)
ex2sifRPCLatencyAverageMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCLatencyAverageMsec.setStatus("current")
_Ex2sifRPCLatencyTotalMsec_Type = Gauge32
_Ex2sifRPCLatencyTotalMsec_Object = MibTableColumn
ex2sifRPCLatencyTotalMsec = _Ex2sifRPCLatencyTotalMsec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 18),
    _Ex2sifRPCLatencyTotalMsec_Type()
)
ex2sifRPCLatencyTotalMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCLatencyTotalMsec.setStatus("current")
_Ex2sifRPCRequestsFailed_Type = Gauge32
_Ex2sifRPCRequestsFailed_Object = MibTableColumn
ex2sifRPCRequestsFailed = _Ex2sifRPCRequestsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 19),
    _Ex2sifRPCRequestsFailed_Type()
)
ex2sifRPCRequestsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCRequestsFailed.setStatus("current")
_Ex2sifRPCRequestsFailedPercent_Type = Gauge32
_Ex2sifRPCRequestsFailedPercent_Object = MibTableColumn
ex2sifRPCRequestsFailedPercent = _Ex2sifRPCRequestsFailedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 20),
    _Ex2sifRPCRequestsFailedPercent_Type()
)
ex2sifRPCRequestsFailedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCRequestsFailedPercent.setStatus("current")
_Ex2sifRPCRequestsFailedException_Type = Gauge32
_Ex2sifRPCRequestsFailedException_Object = MibTableColumn
ex2sifRPCRequestsFailedException = _Ex2sifRPCRequestsFailedException_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 21),
    _Ex2sifRPCRequestsFailedException_Type()
)
ex2sifRPCRequestsFailedException.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCRequestsFailedException.setStatus("current")
_Ex2sifRPCRequestsOutstanding_Type = Gauge32
_Ex2sifRPCRequestsOutstanding_Object = MibTableColumn
ex2sifRPCRequestsOutstanding = _Ex2sifRPCRequestsOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 22),
    _Ex2sifRPCRequestsOutstanding_Type()
)
ex2sifRPCRequestsOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCRequestsOutstanding.setStatus("current")
_Ex2sifRPCRequestsSent_Type = Gauge32
_Ex2sifRPCRequestsSent_Object = MibTableColumn
ex2sifRPCRequestsSent = _Ex2sifRPCRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 23),
    _Ex2sifRPCRequestsSent_Type()
)
ex2sifRPCRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCRequestsSent.setStatus("current")
_Ex2sifRPCRequestsSentPerSec_Type = Gauge32
_Ex2sifRPCRequestsSentPerSec_Object = MibTableColumn
ex2sifRPCRequestsSentPerSec = _Ex2sifRPCRequestsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 24),
    _Ex2sifRPCRequestsSentPerSec_Type()
)
ex2sifRPCRequestsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCRequestsSentPerSec.setStatus("current")
_Ex2sifRPCRequestsSucceeded_Type = Gauge32
_Ex2sifRPCRequestsSucceeded_Object = MibTableColumn
ex2sifRPCRequestsSucceeded = _Ex2sifRPCRequestsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 25),
    _Ex2sifRPCRequestsSucceeded_Type()
)
ex2sifRPCRequestsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCRequestsSucceeded.setStatus("current")
_Ex2sifRPCSlowRequests_Type = Gauge32
_Ex2sifRPCSlowRequests_Object = MibTableColumn
ex2sifRPCSlowRequests = _Ex2sifRPCSlowRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 26),
    _Ex2sifRPCSlowRequests_Type()
)
ex2sifRPCSlowRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCSlowRequests.setStatus("current")
_Ex2sifRPCSlowRequestsPercent_Type = Gauge32
_Ex2sifRPCSlowRequestsPercent_Object = MibTableColumn
ex2sifRPCSlowRequestsPercent = _Ex2sifRPCSlowRequestsPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 27),
    _Ex2sifRPCSlowRequestsPercent_Type()
)
ex2sifRPCSlowRequestsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCSlowRequestsPercent.setStatus("current")
_Ex2sifRPCSlowReqLatencyAvgMsec_Type = Gauge32
_Ex2sifRPCSlowReqLatencyAvgMsec_Object = MibTableColumn
ex2sifRPCSlowReqLatencyAvgMsec = _Ex2sifRPCSlowReqLatencyAvgMsec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 28),
    _Ex2sifRPCSlowReqLatencyAvgMsec_Type()
)
ex2sifRPCSlowReqLatencyAvgMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCSlowReqLatencyAvgMsec.setStatus("current")
_Ex2sifRPCSlowReqLatencyTotalMsec_Type = Gauge32
_Ex2sifRPCSlowReqLatencyTotalMsec_Object = MibTableColumn
ex2sifRPCSlowReqLatencyTotalMsec = _Ex2sifRPCSlowReqLatencyTotalMsec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 29),
    _Ex2sifRPCSlowReqLatencyTotalMsec_Type()
)
ex2sifRPCSlowReqLatencyTotalMsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifRPCSlowReqLatencyTotalMsec.setStatus("current")
_Ex2sifUNKFolders_Type = Gauge32
_Ex2sifUNKFolders_Object = MibTableColumn
ex2sifUNKFolders = _Ex2sifUNKFolders_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 30),
    _Ex2sifUNKFolders_Type()
)
ex2sifUNKFolders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifUNKFolders.setStatus("current")
_Ex2sifUNKLogons_Type = Gauge32
_Ex2sifUNKLogons_Object = MibTableColumn
ex2sifUNKLogons = _Ex2sifUNKLogons_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 31),
    _Ex2sifUNKLogons_Type()
)
ex2sifUNKLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifUNKLogons.setStatus("current")
_Ex2sifUNKMessages_Type = Gauge32
_Ex2sifUNKMessages_Object = MibTableColumn
ex2sifUNKMessages = _Ex2sifUNKMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 32),
    _Ex2sifUNKMessages_Type()
)
ex2sifUNKMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifUNKMessages.setStatus("current")
_Ex2sifUNKObjectsTotal_Type = Gauge32
_Ex2sifUNKObjectsTotal_Object = MibTableColumn
ex2sifUNKObjectsTotal = _Ex2sifUNKObjectsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 34, 1, 33),
    _Ex2sifUNKObjectsTotal_Type()
)
ex2sifUNKObjectsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2sifUNKObjectsTotal.setStatus("current")
_Ex2TopologyTable_Object = MibTable
ex2TopologyTable = _Ex2TopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 35)
)
if mibBuilder.loadTexts:
    ex2TopologyTable.setStatus("current")
_Ex2TopologyEntry_Object = MibTableRow
ex2TopologyEntry = _Ex2TopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 35, 1)
)
ex2TopologyEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2tpInstance"),
)
if mibBuilder.loadTexts:
    ex2TopologyEntry.setStatus("current")
_Ex2tpInstance_Type = InstanceName
_Ex2tpInstance_Object = MibTableColumn
ex2tpInstance = _Ex2tpInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 35, 1, 1),
    _Ex2tpInstance_Type()
)
ex2tpInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tpInstance.setStatus("current")
_Ex2tpLatestExchgTopologyDisTime_Type = Gauge32
_Ex2tpLatestExchgTopologyDisTime_Object = MibTableColumn
ex2tpLatestExchgTopologyDisTime = _Ex2tpLatestExchgTopologyDisTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 35, 1, 2),
    _Ex2tpLatestExchgTopologyDisTime_Type()
)
ex2tpLatestExchgTopologyDisTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tpLatestExchgTopologyDisTime.setStatus("current")
_Ex2tpNumExchangeTopologyDiscover_Type = Gauge32
_Ex2tpNumExchangeTopologyDiscover_Object = MibTableColumn
ex2tpNumExchangeTopologyDiscover = _Ex2tpNumExchangeTopologyDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 35, 1, 3),
    _Ex2tpNumExchangeTopologyDiscover_Type()
)
ex2tpNumExchangeTopologyDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tpNumExchangeTopologyDiscover.setStatus("current")
_Ex2tpNumberOfSitelessServers_Type = Gauge32
_Ex2tpNumberOfSitelessServers_Object = MibTableColumn
ex2tpNumberOfSitelessServers = _Ex2tpNumberOfSitelessServers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 35, 1, 4),
    _Ex2tpNumberOfSitelessServers_Type()
)
ex2tpNumberOfSitelessServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tpNumberOfSitelessServers.setStatus("current")
_Ex2TransportRulesTable_Object = MibTable
ex2TransportRulesTable = _Ex2TransportRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 36)
)
if mibBuilder.loadTexts:
    ex2TransportRulesTable.setStatus("current")
_Ex2TransportRulesEntry_Object = MibTableRow
ex2TransportRulesEntry = _Ex2TransportRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 36, 1)
)
ex2TransportRulesEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2trInstance"),
)
if mibBuilder.loadTexts:
    ex2TransportRulesEntry.setStatus("current")
_Ex2trInstance_Type = InstanceName
_Ex2trInstance_Object = MibTableColumn
ex2trInstance = _Ex2trInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 36, 1, 1),
    _Ex2trInstance_Type()
)
ex2trInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2trInstance.setStatus("current")
_Ex2trMessagesEvaluated_Type = Gauge32
_Ex2trMessagesEvaluated_Object = MibTableColumn
ex2trMessagesEvaluated = _Ex2trMessagesEvaluated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 36, 1, 2),
    _Ex2trMessagesEvaluated_Type()
)
ex2trMessagesEvaluated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2trMessagesEvaluated.setStatus("current")
_Ex2trMessagesEvaluatedPerSec_Type = Gauge32
_Ex2trMessagesEvaluatedPerSec_Object = MibTableColumn
ex2trMessagesEvaluatedPerSec = _Ex2trMessagesEvaluatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 36, 1, 3),
    _Ex2trMessagesEvaluatedPerSec_Type()
)
ex2trMessagesEvaluatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2trMessagesEvaluatedPerSec.setStatus("current")
_Ex2trMessagesProcessed_Type = Gauge32
_Ex2trMessagesProcessed_Object = MibTableColumn
ex2trMessagesProcessed = _Ex2trMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 36, 1, 4),
    _Ex2trMessagesProcessed_Type()
)
ex2trMessagesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2trMessagesProcessed.setStatus("current")
_Ex2trMessagesProcessedPerSec_Type = Gauge32
_Ex2trMessagesProcessedPerSec_Object = MibTableColumn
ex2trMessagesProcessedPerSec = _Ex2trMessagesProcessedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 36, 1, 5),
    _Ex2trMessagesProcessedPerSec_Type()
)
ex2trMessagesProcessedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2trMessagesProcessedPerSec.setStatus("current")
_Ex2UpdateAgent_ObjectIdentity = ObjectIdentity
ex2UpdateAgent = _Ex2UpdateAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 37)
)
_Ex2uaTotalSRLParameterUpdates_Type = Gauge32
_Ex2uaTotalSRLParameterUpdates_Object = MibScalar
ex2uaTotalSRLParameterUpdates = _Ex2uaTotalSRLParameterUpdates_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 37, 1),
    _Ex2uaTotalSRLParameterUpdates_Type()
)
ex2uaTotalSRLParameterUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2uaTotalSRLParameterUpdates.setStatus("current")
_Ex2uaTotalUpdates_Type = Gauge32
_Ex2uaTotalUpdates_Object = MibScalar
ex2uaTotalUpdates = _Ex2uaTotalUpdates_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 37, 2),
    _Ex2uaTotalUpdates_Type()
)
ex2uaTotalUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2uaTotalUpdates.setStatus("current")
_Ex2WebMailTable_Object = MibTable
ex2WebMailTable = _Ex2WebMailTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38)
)
if mibBuilder.loadTexts:
    ex2WebMailTable.setStatus("current")
_Ex2WebMailEntry_Object = MibTableRow
ex2WebMailEntry = _Ex2WebMailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1)
)
ex2WebMailEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2wmInstance"),
)
if mibBuilder.loadTexts:
    ex2WebMailEntry.setStatus("current")
_Ex2wmInstance_Type = InstanceName
_Ex2wmInstance_Object = MibTableColumn
ex2wmInstance = _Ex2wmInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 1),
    _Ex2wmInstance_Type()
)
ex2wmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmInstance.setStatus("current")
_Ex2wmApptmtAcceptPerDeclineTotal_Type = Gauge32
_Ex2wmApptmtAcceptPerDeclineTotal_Object = MibTableColumn
ex2wmApptmtAcceptPerDeclineTotal = _Ex2wmApptmtAcceptPerDeclineTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 2),
    _Ex2wmApptmtAcceptPerDeclineTotal_Type()
)
ex2wmApptmtAcceptPerDeclineTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtAcceptPerDeclineTotal.setStatus("current")
_Ex2wmApptmtAcceptPrDeclinePerSec_Type = Gauge32
_Ex2wmApptmtAcceptPrDeclinePerSec_Object = MibTableColumn
ex2wmApptmtAcceptPrDeclinePerSec = _Ex2wmApptmtAcceptPrDeclinePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 3),
    _Ex2wmApptmtAcceptPrDeclinePerSec_Type()
)
ex2wmApptmtAcceptPrDeclinePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtAcceptPrDeclinePerSec.setStatus("current")
_Ex2wmApptmtAttachmentEditsTotal_Type = Gauge32
_Ex2wmApptmtAttachmentEditsTotal_Object = MibTableColumn
ex2wmApptmtAttachmentEditsTotal = _Ex2wmApptmtAttachmentEditsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 4),
    _Ex2wmApptmtAttachmentEditsTotal_Type()
)
ex2wmApptmtAttachmentEditsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtAttachmentEditsTotal.setStatus("current")
_Ex2wmApptmtAttachmentEditsPerSec_Type = Gauge32
_Ex2wmApptmtAttachmentEditsPerSec_Object = MibTableColumn
ex2wmApptmtAttachmentEditsPerSec = _Ex2wmApptmtAttachmentEditsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 5),
    _Ex2wmApptmtAttachmentEditsPerSec_Type()
)
ex2wmApptmtAttachmentEditsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtAttachmentEditsPerSec.setStatus("current")
_Ex2wmApptmtDataRetrievesTotal_Type = Gauge32
_Ex2wmApptmtDataRetrievesTotal_Object = MibTableColumn
ex2wmApptmtDataRetrievesTotal = _Ex2wmApptmtDataRetrievesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 6),
    _Ex2wmApptmtDataRetrievesTotal_Type()
)
ex2wmApptmtDataRetrievesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtDataRetrievesTotal.setStatus("current")
_Ex2wmApptmtDataRetrievesPerSec_Type = Gauge32
_Ex2wmApptmtDataRetrievesPerSec_Object = MibTableColumn
ex2wmApptmtDataRetrievesPerSec = _Ex2wmApptmtDataRetrievesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 7),
    _Ex2wmApptmtDataRetrievesPerSec_Type()
)
ex2wmApptmtDataRetrievesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtDataRetrievesPerSec.setStatus("current")
_Ex2wmApptmtEditRecurrenceTotal_Type = Gauge32
_Ex2wmApptmtEditRecurrenceTotal_Object = MibTableColumn
ex2wmApptmtEditRecurrenceTotal = _Ex2wmApptmtEditRecurrenceTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 8),
    _Ex2wmApptmtEditRecurrenceTotal_Type()
)
ex2wmApptmtEditRecurrenceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtEditRecurrenceTotal.setStatus("current")
_Ex2wmApptmtEditRecurrencePerSec_Type = Gauge32
_Ex2wmApptmtEditRecurrencePerSec_Object = MibTableColumn
ex2wmApptmtEditRecurrencePerSec = _Ex2wmApptmtEditRecurrencePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 9),
    _Ex2wmApptmtEditRecurrencePerSec_Type()
)
ex2wmApptmtEditRecurrencePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtEditRecurrencePerSec.setStatus("current")
_Ex2wmAppointmentOpensTotal_Type = Gauge32
_Ex2wmAppointmentOpensTotal_Object = MibTableColumn
ex2wmAppointmentOpensTotal = _Ex2wmAppointmentOpensTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 10),
    _Ex2wmAppointmentOpensTotal_Type()
)
ex2wmAppointmentOpensTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAppointmentOpensTotal.setStatus("current")
_Ex2wmAppointmentOpensPerSec_Type = Gauge32
_Ex2wmAppointmentOpensPerSec_Object = MibTableColumn
ex2wmAppointmentOpensPerSec = _Ex2wmAppointmentOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 11),
    _Ex2wmAppointmentOpensPerSec_Type()
)
ex2wmAppointmentOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAppointmentOpensPerSec.setStatus("current")
_Ex2wmApptmtResolveFreeBusyTotal_Type = Gauge32
_Ex2wmApptmtResolveFreeBusyTotal_Object = MibTableColumn
ex2wmApptmtResolveFreeBusyTotal = _Ex2wmApptmtResolveFreeBusyTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 12),
    _Ex2wmApptmtResolveFreeBusyTotal_Type()
)
ex2wmApptmtResolveFreeBusyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtResolveFreeBusyTotal.setStatus("current")
_Ex2wmApptmtResolveFreeBusyPerSec_Type = Gauge32
_Ex2wmApptmtResolveFreeBusyPerSec_Object = MibTableColumn
ex2wmApptmtResolveFreeBusyPerSec = _Ex2wmApptmtResolveFreeBusyPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 13),
    _Ex2wmApptmtResolveFreeBusyPerSec_Type()
)
ex2wmApptmtResolveFreeBusyPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtResolveFreeBusyPerSec.setStatus("current")
_Ex2wmApptmtSaveRecurrencesTotal_Type = Gauge32
_Ex2wmApptmtSaveRecurrencesTotal_Object = MibTableColumn
ex2wmApptmtSaveRecurrencesTotal = _Ex2wmApptmtSaveRecurrencesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 14),
    _Ex2wmApptmtSaveRecurrencesTotal_Type()
)
ex2wmApptmtSaveRecurrencesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtSaveRecurrencesTotal.setStatus("current")
_Ex2wmApptmtSaveRecurrencesPerSec_Type = Gauge32
_Ex2wmApptmtSaveRecurrencesPerSec_Object = MibTableColumn
ex2wmApptmtSaveRecurrencesPerSec = _Ex2wmApptmtSaveRecurrencesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 15),
    _Ex2wmApptmtSaveRecurrencesPerSec_Type()
)
ex2wmApptmtSaveRecurrencesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmApptmtSaveRecurrencesPerSec.setStatus("current")
_Ex2wmAppointmentSavesTotal_Type = Gauge32
_Ex2wmAppointmentSavesTotal_Object = MibTableColumn
ex2wmAppointmentSavesTotal = _Ex2wmAppointmentSavesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 16),
    _Ex2wmAppointmentSavesTotal_Type()
)
ex2wmAppointmentSavesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAppointmentSavesTotal.setStatus("current")
_Ex2wmAppointmentSavesPerSec_Type = Gauge32
_Ex2wmAppointmentSavesPerSec_Object = MibTableColumn
ex2wmAppointmentSavesPerSec = _Ex2wmAppointmentSavesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 17),
    _Ex2wmAppointmentSavesPerSec_Type()
)
ex2wmAppointmentSavesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAppointmentSavesPerSec.setStatus("current")
_Ex2wmAppointmentSendsTotal_Type = Gauge32
_Ex2wmAppointmentSendsTotal_Object = MibTableColumn
ex2wmAppointmentSendsTotal = _Ex2wmAppointmentSendsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 18),
    _Ex2wmAppointmentSendsTotal_Type()
)
ex2wmAppointmentSendsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAppointmentSendsTotal.setStatus("current")
_Ex2wmAppointmentSendsPerSec_Type = Gauge32
_Ex2wmAppointmentSendsPerSec_Object = MibTableColumn
ex2wmAppointmentSendsPerSec = _Ex2wmAppointmentSendsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 19),
    _Ex2wmAppointmentSendsPerSec_Type()
)
ex2wmAppointmentSendsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAppointmentSendsPerSec.setStatus("current")
_Ex2wmAppointmentUpdatesTotal_Type = Gauge32
_Ex2wmAppointmentUpdatesTotal_Object = MibTableColumn
ex2wmAppointmentUpdatesTotal = _Ex2wmAppointmentUpdatesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 20),
    _Ex2wmAppointmentUpdatesTotal_Type()
)
ex2wmAppointmentUpdatesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAppointmentUpdatesTotal.setStatus("current")
_Ex2wmAppointmentUpdatesPerSec_Type = Gauge32
_Ex2wmAppointmentUpdatesPerSec_Object = MibTableColumn
ex2wmAppointmentUpdatesPerSec = _Ex2wmAppointmentUpdatesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 21),
    _Ex2wmAppointmentUpdatesPerSec_Type()
)
ex2wmAppointmentUpdatesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAppointmentUpdatesPerSec.setStatus("current")
_Ex2wmAttachmentsDeletedTotal_Type = Gauge32
_Ex2wmAttachmentsDeletedTotal_Object = MibTableColumn
ex2wmAttachmentsDeletedTotal = _Ex2wmAttachmentsDeletedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 22),
    _Ex2wmAttachmentsDeletedTotal_Type()
)
ex2wmAttachmentsDeletedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAttachmentsDeletedTotal.setStatus("current")
_Ex2wmAttachmentsDeletedPerSec_Type = Gauge32
_Ex2wmAttachmentsDeletedPerSec_Object = MibTableColumn
ex2wmAttachmentsDeletedPerSec = _Ex2wmAttachmentsDeletedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 23),
    _Ex2wmAttachmentsDeletedPerSec_Type()
)
ex2wmAttachmentsDeletedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAttachmentsDeletedPerSec.setStatus("current")
_Ex2wmAuthenticationCacheHitTotal_Type = Gauge32
_Ex2wmAuthenticationCacheHitTotal_Object = MibTableColumn
ex2wmAuthenticationCacheHitTotal = _Ex2wmAuthenticationCacheHitTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 24),
    _Ex2wmAuthenticationCacheHitTotal_Type()
)
ex2wmAuthenticationCacheHitTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAuthenticationCacheHitTotal.setStatus("current")
_Ex2wmAuthenticationCacheHitPrSec_Type = Gauge32
_Ex2wmAuthenticationCacheHitPrSec_Object = MibTableColumn
ex2wmAuthenticationCacheHitPrSec = _Ex2wmAuthenticationCacheHitPrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 25),
    _Ex2wmAuthenticationCacheHitPrSec_Type()
)
ex2wmAuthenticationCacheHitPrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAuthenticationCacheHitPrSec.setStatus("current")
_Ex2wmAuthenticationsInCache_Type = Gauge32
_Ex2wmAuthenticationsInCache_Object = MibTableColumn
ex2wmAuthenticationsInCache = _Ex2wmAuthenticationsInCache_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 26),
    _Ex2wmAuthenticationsInCache_Type()
)
ex2wmAuthenticationsInCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAuthenticationsInCache.setStatus("current")
_Ex2wmAuthenticationsTotal_Type = Gauge32
_Ex2wmAuthenticationsTotal_Object = MibTableColumn
ex2wmAuthenticationsTotal = _Ex2wmAuthenticationsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 27),
    _Ex2wmAuthenticationsTotal_Type()
)
ex2wmAuthenticationsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAuthenticationsTotal.setStatus("current")
_Ex2wmAuthenticationsPerSec_Type = Gauge32
_Ex2wmAuthenticationsPerSec_Object = MibTableColumn
ex2wmAuthenticationsPerSec = _Ex2wmAuthenticationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 28),
    _Ex2wmAuthenticationsPerSec_Type()
)
ex2wmAuthenticationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmAuthenticationsPerSec.setStatus("current")
_Ex2wmFolderCreatesTotal_Type = Gauge32
_Ex2wmFolderCreatesTotal_Object = MibTableColumn
ex2wmFolderCreatesTotal = _Ex2wmFolderCreatesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 29),
    _Ex2wmFolderCreatesTotal_Type()
)
ex2wmFolderCreatesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmFolderCreatesTotal.setStatus("current")
_Ex2wmFolderCreatesPerSec_Type = Gauge32
_Ex2wmFolderCreatesPerSec_Object = MibTableColumn
ex2wmFolderCreatesPerSec = _Ex2wmFolderCreatesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 30),
    _Ex2wmFolderCreatesPerSec_Type()
)
ex2wmFolderCreatesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmFolderCreatesPerSec.setStatus("current")
_Ex2wmFolderGetContentsTotal_Type = Gauge32
_Ex2wmFolderGetContentsTotal_Object = MibTableColumn
ex2wmFolderGetContentsTotal = _Ex2wmFolderGetContentsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 31),
    _Ex2wmFolderGetContentsTotal_Type()
)
ex2wmFolderGetContentsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmFolderGetContentsTotal.setStatus("current")
_Ex2wmFolderGetContentsPerSec_Type = Gauge32
_Ex2wmFolderGetContentsPerSec_Object = MibTableColumn
ex2wmFolderGetContentsPerSec = _Ex2wmFolderGetContentsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 32),
    _Ex2wmFolderGetContentsPerSec_Type()
)
ex2wmFolderGetContentsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmFolderGetContentsPerSec.setStatus("current")
_Ex2wmFolderGetViewTotal_Type = Gauge32
_Ex2wmFolderGetViewTotal_Object = MibTableColumn
ex2wmFolderGetViewTotal = _Ex2wmFolderGetViewTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 33),
    _Ex2wmFolderGetViewTotal_Type()
)
ex2wmFolderGetViewTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmFolderGetViewTotal.setStatus("current")
_Ex2wmFolderGetViewPerSec_Type = Gauge32
_Ex2wmFolderGetViewPerSec_Object = MibTableColumn
ex2wmFolderGetViewPerSec = _Ex2wmFolderGetViewPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 34),
    _Ex2wmFolderGetViewPerSec_Type()
)
ex2wmFolderGetViewPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmFolderGetViewPerSec.setStatus("current")
_Ex2wmFolderRenamesTotal_Type = Gauge32
_Ex2wmFolderRenamesTotal_Object = MibTableColumn
ex2wmFolderRenamesTotal = _Ex2wmFolderRenamesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 35),
    _Ex2wmFolderRenamesTotal_Type()
)
ex2wmFolderRenamesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmFolderRenamesTotal.setStatus("current")
_Ex2wmFolderRenamesPerSec_Type = Gauge32
_Ex2wmFolderRenamesPerSec_Object = MibTableColumn
ex2wmFolderRenamesPerSec = _Ex2wmFolderRenamesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 36),
    _Ex2wmFolderRenamesPerSec_Type()
)
ex2wmFolderRenamesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmFolderRenamesPerSec.setStatus("current")
_Ex2wmFormsSentTotal_Type = Gauge32
_Ex2wmFormsSentTotal_Object = MibTableColumn
ex2wmFormsSentTotal = _Ex2wmFormsSentTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 37),
    _Ex2wmFormsSentTotal_Type()
)
ex2wmFormsSentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmFormsSentTotal.setStatus("current")
_Ex2wmFormsSentPerSec_Type = Gauge32
_Ex2wmFormsSentPerSec_Object = MibTableColumn
ex2wmFormsSentPerSec = _Ex2wmFormsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 38),
    _Ex2wmFormsSentPerSec_Type()
)
ex2wmFormsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmFormsSentPerSec.setStatus("current")
_Ex2wmGetAppFrameTotal_Type = Gauge32
_Ex2wmGetAppFrameTotal_Object = MibTableColumn
ex2wmGetAppFrameTotal = _Ex2wmGetAppFrameTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 39),
    _Ex2wmGetAppFrameTotal_Type()
)
ex2wmGetAppFrameTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmGetAppFrameTotal.setStatus("current")
_Ex2wmGetAppFramePerSec_Type = Gauge32
_Ex2wmGetAppFramePerSec_Object = MibTableColumn
ex2wmGetAppFramePerSec = _Ex2wmGetAppFramePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 40),
    _Ex2wmGetAppFramePerSec_Type()
)
ex2wmGetAppFramePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmGetAppFramePerSec.setStatus("current")
_Ex2wmGetNavBarTotal_Type = Gauge32
_Ex2wmGetNavBarTotal_Object = MibTableColumn
ex2wmGetNavBarTotal = _Ex2wmGetNavBarTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 41),
    _Ex2wmGetNavBarTotal_Type()
)
ex2wmGetNavBarTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmGetNavBarTotal.setStatus("current")
_Ex2wmGetNavBarPerSec_Type = Gauge32
_Ex2wmGetNavBarPerSec_Object = MibTableColumn
ex2wmGetNavBarPerSec = _Ex2wmGetNavBarPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 42),
    _Ex2wmGetNavBarPerSec_Type()
)
ex2wmGetNavBarPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmGetNavBarPerSec.setStatus("current")
_Ex2wmMessageAttachmentEditsTotal_Type = Gauge32
_Ex2wmMessageAttachmentEditsTotal_Object = MibTableColumn
ex2wmMessageAttachmentEditsTotal = _Ex2wmMessageAttachmentEditsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 43),
    _Ex2wmMessageAttachmentEditsTotal_Type()
)
ex2wmMessageAttachmentEditsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMessageAttachmentEditsTotal.setStatus("current")
_Ex2wmMessageAttachmentEditPerSec_Type = Gauge32
_Ex2wmMessageAttachmentEditPerSec_Object = MibTableColumn
ex2wmMessageAttachmentEditPerSec = _Ex2wmMessageAttachmentEditPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 44),
    _Ex2wmMessageAttachmentEditPerSec_Type()
)
ex2wmMessageAttachmentEditPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMessageAttachmentEditPerSec.setStatus("current")
_Ex2wmMessageMovesPerCopiesTotal_Type = Gauge32
_Ex2wmMessageMovesPerCopiesTotal_Object = MibTableColumn
ex2wmMessageMovesPerCopiesTotal = _Ex2wmMessageMovesPerCopiesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 45),
    _Ex2wmMessageMovesPerCopiesTotal_Type()
)
ex2wmMessageMovesPerCopiesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMessageMovesPerCopiesTotal.setStatus("current")
_Ex2wmMessageMovesPerCopyPerSec_Type = Gauge32
_Ex2wmMessageMovesPerCopyPerSec_Object = MibTableColumn
ex2wmMessageMovesPerCopyPerSec = _Ex2wmMessageMovesPerCopyPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 46),
    _Ex2wmMessageMovesPerCopyPerSec_Type()
)
ex2wmMessageMovesPerCopyPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMessageMovesPerCopyPerSec.setStatus("current")
_Ex2wmMessageOpensTotal_Type = Gauge32
_Ex2wmMessageOpensTotal_Object = MibTableColumn
ex2wmMessageOpensTotal = _Ex2wmMessageOpensTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 47),
    _Ex2wmMessageOpensTotal_Type()
)
ex2wmMessageOpensTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMessageOpensTotal.setStatus("current")
_Ex2wmMessageOpensPerSec_Type = Gauge32
_Ex2wmMessageOpensPerSec_Object = MibTableColumn
ex2wmMessageOpensPerSec = _Ex2wmMessageOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 48),
    _Ex2wmMessageOpensPerSec_Type()
)
ex2wmMessageOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMessageOpensPerSec.setStatus("current")
_Ex2wmMessageSavesTotal_Type = Gauge32
_Ex2wmMessageSavesTotal_Object = MibTableColumn
ex2wmMessageSavesTotal = _Ex2wmMessageSavesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 49),
    _Ex2wmMessageSavesTotal_Type()
)
ex2wmMessageSavesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMessageSavesTotal.setStatus("current")
_Ex2wmMessageSavesPerSec_Type = Gauge32
_Ex2wmMessageSavesPerSec_Object = MibTableColumn
ex2wmMessageSavesPerSec = _Ex2wmMessageSavesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 50),
    _Ex2wmMessageSavesPerSec_Type()
)
ex2wmMessageSavesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMessageSavesPerSec.setStatus("current")
_Ex2wmMessageSendsTotal_Type = Gauge32
_Ex2wmMessageSendsTotal_Object = MibTableColumn
ex2wmMessageSendsTotal = _Ex2wmMessageSendsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 51),
    _Ex2wmMessageSendsTotal_Type()
)
ex2wmMessageSendsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMessageSendsTotal.setStatus("current")
_Ex2wmMessageSendsPerSec_Type = Gauge32
_Ex2wmMessageSendsPerSec_Object = MibTableColumn
ex2wmMessageSendsPerSec = _Ex2wmMessageSendsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 52),
    _Ex2wmMessageSendsPerSec_Type()
)
ex2wmMessageSendsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMessageSendsPerSec.setStatus("current")
_Ex2wmMsgPerApptmtDeletesTotal_Type = Gauge32
_Ex2wmMsgPerApptmtDeletesTotal_Object = MibTableColumn
ex2wmMsgPerApptmtDeletesTotal = _Ex2wmMsgPerApptmtDeletesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 53),
    _Ex2wmMsgPerApptmtDeletesTotal_Type()
)
ex2wmMsgPerApptmtDeletesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMsgPerApptmtDeletesTotal.setStatus("current")
_Ex2wmMsgPerApptmtDeletesPerSec_Type = Gauge32
_Ex2wmMsgPerApptmtDeletesPerSec_Object = MibTableColumn
ex2wmMsgPerApptmtDeletesPerSec = _Ex2wmMsgPerApptmtDeletesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 54),
    _Ex2wmMsgPerApptmtDeletesPerSec_Type()
)
ex2wmMsgPerApptmtDeletesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMsgPerApptmtDeletesPerSec.setStatus("current")
_Ex2wmMsgPerAppointmentOpensTotal_Type = Gauge32
_Ex2wmMsgPerAppointmentOpensTotal_Object = MibTableColumn
ex2wmMsgPerAppointmentOpensTotal = _Ex2wmMsgPerAppointmentOpensTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 55),
    _Ex2wmMsgPerAppointmentOpensTotal_Type()
)
ex2wmMsgPerAppointmentOpensTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMsgPerAppointmentOpensTotal.setStatus("current")
_Ex2wmMsgPerAppointmentOpenPerSec_Type = Gauge32
_Ex2wmMsgPerAppointmentOpenPerSec_Object = MibTableColumn
ex2wmMsgPerAppointmentOpenPerSec = _Ex2wmMsgPerAppointmentOpenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 56),
    _Ex2wmMsgPerAppointmentOpenPerSec_Type()
)
ex2wmMsgPerAppointmentOpenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMsgPerAppointmentOpenPerSec.setStatus("current")
_Ex2wmMsgPerAppointmentSavesTotal_Type = Gauge32
_Ex2wmMsgPerAppointmentSavesTotal_Object = MibTableColumn
ex2wmMsgPerAppointmentSavesTotal = _Ex2wmMsgPerAppointmentSavesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 57),
    _Ex2wmMsgPerAppointmentSavesTotal_Type()
)
ex2wmMsgPerAppointmentSavesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMsgPerAppointmentSavesTotal.setStatus("current")
_Ex2wmMsgPerAppointmentSavePerSec_Type = Gauge32
_Ex2wmMsgPerAppointmentSavePerSec_Object = MibTableColumn
ex2wmMsgPerAppointmentSavePerSec = _Ex2wmMsgPerAppointmentSavePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 58),
    _Ex2wmMsgPerAppointmentSavePerSec_Type()
)
ex2wmMsgPerAppointmentSavePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmMsgPerAppointmentSavePerSec.setStatus("current")
_Ex2wmNamesCheckedTotal_Type = Gauge32
_Ex2wmNamesCheckedTotal_Object = MibTableColumn
ex2wmNamesCheckedTotal = _Ex2wmNamesCheckedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 59),
    _Ex2wmNamesCheckedTotal_Type()
)
ex2wmNamesCheckedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmNamesCheckedTotal.setStatus("current")
_Ex2wmNamesCheckedPerSec_Type = Gauge32
_Ex2wmNamesCheckedPerSec_Object = MibTableColumn
ex2wmNamesCheckedPerSec = _Ex2wmNamesCheckedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 60),
    _Ex2wmNamesCheckedPerSec_Type()
)
ex2wmNamesCheckedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmNamesCheckedPerSec.setStatus("current")
_Ex2wmNavigationOptionsSavesTotal_Type = Gauge32
_Ex2wmNavigationOptionsSavesTotal_Object = MibTableColumn
ex2wmNavigationOptionsSavesTotal = _Ex2wmNavigationOptionsSavesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 61),
    _Ex2wmNavigationOptionsSavesTotal_Type()
)
ex2wmNavigationOptionsSavesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmNavigationOptionsSavesTotal.setStatus("current")
_Ex2wmNavigationOptionsSavePerSec_Type = Gauge32
_Ex2wmNavigationOptionsSavePerSec_Object = MibTableColumn
ex2wmNavigationOptionsSavePerSec = _Ex2wmNavigationOptionsSavePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 62),
    _Ex2wmNavigationOptionsSavePerSec_Type()
)
ex2wmNavigationOptionsSavePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmNavigationOptionsSavePerSec.setStatus("current")
_Ex2wmNewFolderTemplateDataTotal_Type = Gauge32
_Ex2wmNewFolderTemplateDataTotal_Object = MibTableColumn
ex2wmNewFolderTemplateDataTotal = _Ex2wmNewFolderTemplateDataTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 63),
    _Ex2wmNewFolderTemplateDataTotal_Type()
)
ex2wmNewFolderTemplateDataTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmNewFolderTemplateDataTotal.setStatus("current")
_Ex2wmNewFolderTemplateDataPerSec_Type = Gauge32
_Ex2wmNewFolderTemplateDataPerSec_Object = MibTableColumn
ex2wmNewFolderTemplateDataPerSec = _Ex2wmNewFolderTemplateDataPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 64),
    _Ex2wmNewFolderTemplateDataPerSec_Type()
)
ex2wmNewFolderTemplateDataPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmNewFolderTemplateDataPerSec.setStatus("current")
_Ex2wmNewItemURLTotal_Type = Gauge32
_Ex2wmNewItemURLTotal_Object = MibTableColumn
ex2wmNewItemURLTotal = _Ex2wmNewItemURLTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 65),
    _Ex2wmNewItemURLTotal_Type()
)
ex2wmNewItemURLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmNewItemURLTotal.setStatus("current")
_Ex2wmNewItemURLPerSec_Type = Gauge32
_Ex2wmNewItemURLPerSec_Object = MibTableColumn
ex2wmNewItemURLPerSec = _Ex2wmNewItemURLPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 66),
    _Ex2wmNewItemURLPerSec_Type()
)
ex2wmNewItemURLPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmNewItemURLPerSec.setStatus("current")
_Ex2wmPostsSubmittedTotal_Type = Gauge32
_Ex2wmPostsSubmittedTotal_Object = MibTableColumn
ex2wmPostsSubmittedTotal = _Ex2wmPostsSubmittedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 67),
    _Ex2wmPostsSubmittedTotal_Type()
)
ex2wmPostsSubmittedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmPostsSubmittedTotal.setStatus("current")
_Ex2wmPostsSubmittedPerSec_Type = Gauge32
_Ex2wmPostsSubmittedPerSec_Object = MibTableColumn
ex2wmPostsSubmittedPerSec = _Ex2wmPostsSubmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 68),
    _Ex2wmPostsSubmittedPerSec_Type()
)
ex2wmPostsSubmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmPostsSubmittedPerSec.setStatus("current")
_Ex2wmRecipientsEditedTotal_Type = Gauge32
_Ex2wmRecipientsEditedTotal_Object = MibTableColumn
ex2wmRecipientsEditedTotal = _Ex2wmRecipientsEditedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 69),
    _Ex2wmRecipientsEditedTotal_Type()
)
ex2wmRecipientsEditedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmRecipientsEditedTotal.setStatus("current")
_Ex2wmRecipientsEditedPerSec_Type = Gauge32
_Ex2wmRecipientsEditedPerSec_Object = MibTableColumn
ex2wmRecipientsEditedPerSec = _Ex2wmRecipientsEditedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 70),
    _Ex2wmRecipientsEditedPerSec_Type()
)
ex2wmRecipientsEditedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmRecipientsEditedPerSec.setStatus("current")
_Ex2wmRecipientsSavedTotal_Type = Gauge32
_Ex2wmRecipientsSavedTotal_Object = MibTableColumn
ex2wmRecipientsSavedTotal = _Ex2wmRecipientsSavedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 71),
    _Ex2wmRecipientsSavedTotal_Type()
)
ex2wmRecipientsSavedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmRecipientsSavedTotal.setStatus("current")
_Ex2wmRecipientsSavedPerSec_Type = Gauge32
_Ex2wmRecipientsSavedPerSec_Object = MibTableColumn
ex2wmRecipientsSavedPerSec = _Ex2wmRecipientsSavedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 72),
    _Ex2wmRecipientsSavedPerSec_Type()
)
ex2wmRecipientsSavedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmRecipientsSavedPerSec.setStatus("current")
_Ex2wmViewsOfCalendarsTotal_Type = Gauge32
_Ex2wmViewsOfCalendarsTotal_Object = MibTableColumn
ex2wmViewsOfCalendarsTotal = _Ex2wmViewsOfCalendarsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 73),
    _Ex2wmViewsOfCalendarsTotal_Type()
)
ex2wmViewsOfCalendarsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmViewsOfCalendarsTotal.setStatus("current")
_Ex2wmViewsOfCalendarsPerSec_Type = Gauge32
_Ex2wmViewsOfCalendarsPerSec_Object = MibTableColumn
ex2wmViewsOfCalendarsPerSec = _Ex2wmViewsOfCalendarsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 74),
    _Ex2wmViewsOfCalendarsPerSec_Type()
)
ex2wmViewsOfCalendarsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmViewsOfCalendarsPerSec.setStatus("current")
_Ex2wmViewsOfMailFoldersTotal_Type = Gauge32
_Ex2wmViewsOfMailFoldersTotal_Object = MibTableColumn
ex2wmViewsOfMailFoldersTotal = _Ex2wmViewsOfMailFoldersTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 75),
    _Ex2wmViewsOfMailFoldersTotal_Type()
)
ex2wmViewsOfMailFoldersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmViewsOfMailFoldersTotal.setStatus("current")
_Ex2wmViewsOfMailFoldersPerSec_Type = Gauge32
_Ex2wmViewsOfMailFoldersPerSec_Object = MibTableColumn
ex2wmViewsOfMailFoldersPerSec = _Ex2wmViewsOfMailFoldersPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 38, 1, 76),
    _Ex2wmViewsOfMailFoldersPerSec_Type()
)
ex2wmViewsOfMailFoldersPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2wmViewsOfMailFoldersPerSec.setStatus("current")
_Ex2ALTable_Object = MibTable
ex2ALTable = _Ex2ALTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 39)
)
if mibBuilder.loadTexts:
    ex2ALTable.setStatus("current")
_Ex2ALEntry_Object = MibTableRow
ex2ALEntry = _Ex2ALEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 39, 1)
)
ex2ALEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2ALInstance"),
)
if mibBuilder.loadTexts:
    ex2ALEntry.setStatus("current")
_Ex2ALInstance_Type = InstanceName
_Ex2ALInstance_Object = MibTableColumn
ex2ALInstance = _Ex2ALInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 39, 1, 1),
    _Ex2ALInstance_Type()
)
ex2ALInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ALInstance.setStatus("current")
_Ex2ALActiveRPCThreads_Type = Gauge32
_Ex2ALActiveRPCThreads_Object = MibTableColumn
ex2ALActiveRPCThreads = _Ex2ALActiveRPCThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 39, 1, 2),
    _Ex2ALActiveRPCThreads_Type()
)
ex2ALActiveRPCThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ALActiveRPCThreads.setStatus("current")
_Ex2ALLDAPResults_Type = Gauge32
_Ex2ALLDAPResults_Object = MibTableColumn
ex2ALLDAPResults = _Ex2ALLDAPResults_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 39, 1, 3),
    _Ex2ALLDAPResults_Type()
)
ex2ALLDAPResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ALLDAPResults.setStatus("current")
_Ex2ALLDAPResultsPerSec_Type = Gauge32
_Ex2ALLDAPResultsPerSec_Object = MibTableColumn
ex2ALLDAPResultsPerSec = _Ex2ALLDAPResultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 39, 1, 4),
    _Ex2ALLDAPResultsPerSec_Type()
)
ex2ALLDAPResultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ALLDAPResultsPerSec.setStatus("current")
_Ex2ALLDAPSearchCalls_Type = Gauge32
_Ex2ALLDAPSearchCalls_Object = MibTableColumn
ex2ALLDAPSearchCalls = _Ex2ALLDAPSearchCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 39, 1, 5),
    _Ex2ALLDAPSearchCalls_Type()
)
ex2ALLDAPSearchCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ALLDAPSearchCalls.setStatus("current")
_Ex2ALLDAPSearchCallsPerSec_Type = Gauge32
_Ex2ALLDAPSearchCallsPerSec_Object = MibTableColumn
ex2ALLDAPSearchCallsPerSec = _Ex2ALLDAPSearchCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 39, 1, 6),
    _Ex2ALLDAPSearchCallsPerSec_Type()
)
ex2ALLDAPSearchCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ALLDAPSearchCallsPerSec.setStatus("current")
_Ex2Autodiscover_ObjectIdentity = ObjectIdentity
ex2Autodiscover = _Ex2Autodiscover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 40)
)
_Ex2adErrorResponses_Type = Gauge32
_Ex2adErrorResponses_Object = MibScalar
ex2adErrorResponses = _Ex2adErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 40, 1),
    _Ex2adErrorResponses_Type()
)
ex2adErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2adErrorResponses.setStatus("current")
_Ex2adErrorResponsesPerSec_Type = Gauge32
_Ex2adErrorResponsesPerSec_Object = MibScalar
ex2adErrorResponsesPerSec = _Ex2adErrorResponsesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 40, 2),
    _Ex2adErrorResponsesPerSec_Type()
)
ex2adErrorResponsesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2adErrorResponsesPerSec.setStatus("current")
_Ex2adProcessID_Type = Gauge32
_Ex2adProcessID_Object = MibScalar
ex2adProcessID = _Ex2adProcessID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 40, 3),
    _Ex2adProcessID_Type()
)
ex2adProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2adProcessID.setStatus("current")
_Ex2adRequestsPerSec_Type = Gauge32
_Ex2adRequestsPerSec_Object = MibScalar
ex2adRequestsPerSec = _Ex2adRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 40, 4),
    _Ex2adRequestsPerSec_Type()
)
ex2adRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2adRequestsPerSec.setStatus("current")
_Ex2adTotalRequests_Type = Gauge32
_Ex2adTotalRequests_Object = MibScalar
ex2adTotalRequests = _Ex2adTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 40, 5),
    _Ex2adTotalRequests_Type()
)
ex2adTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2adTotalRequests.setStatus("current")
_Ex2EdgeSyncJobTable_Object = MibTable
ex2EdgeSyncJobTable = _Ex2EdgeSyncJobTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41)
)
if mibBuilder.loadTexts:
    ex2EdgeSyncJobTable.setStatus("current")
_Ex2EdgeSyncJobEntry_Object = MibTableRow
ex2EdgeSyncJobEntry = _Ex2EdgeSyncJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1)
)
ex2EdgeSyncJobEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2esjInstance"),
)
if mibBuilder.loadTexts:
    ex2EdgeSyncJobEntry.setStatus("current")
_Ex2esjInstance_Type = InstanceName
_Ex2esjInstance_Object = MibTableColumn
ex2esjInstance = _Ex2esjInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 1),
    _Ex2esjInstance_Type()
)
ex2esjInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjInstance.setStatus("current")
_Ex2esjEdgeObjectsAddedTotal_Type = Gauge32
_Ex2esjEdgeObjectsAddedTotal_Object = MibTableColumn
ex2esjEdgeObjectsAddedTotal = _Ex2esjEdgeObjectsAddedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 2),
    _Ex2esjEdgeObjectsAddedTotal_Type()
)
ex2esjEdgeObjectsAddedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjEdgeObjectsAddedTotal.setStatus("current")
_Ex2esjEdgeObjectsAddedPerSec_Type = Gauge32
_Ex2esjEdgeObjectsAddedPerSec_Object = MibTableColumn
ex2esjEdgeObjectsAddedPerSec = _Ex2esjEdgeObjectsAddedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 3),
    _Ex2esjEdgeObjectsAddedPerSec_Type()
)
ex2esjEdgeObjectsAddedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjEdgeObjectsAddedPerSec.setStatus("current")
_Ex2esjEdgeObjectsDeletedTotal_Type = Gauge32
_Ex2esjEdgeObjectsDeletedTotal_Object = MibTableColumn
ex2esjEdgeObjectsDeletedTotal = _Ex2esjEdgeObjectsDeletedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 4),
    _Ex2esjEdgeObjectsDeletedTotal_Type()
)
ex2esjEdgeObjectsDeletedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjEdgeObjectsDeletedTotal.setStatus("current")
_Ex2esjEdgeObjectsDeletedPerSec_Type = Gauge32
_Ex2esjEdgeObjectsDeletedPerSec_Object = MibTableColumn
ex2esjEdgeObjectsDeletedPerSec = _Ex2esjEdgeObjectsDeletedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 5),
    _Ex2esjEdgeObjectsDeletedPerSec_Type()
)
ex2esjEdgeObjectsDeletedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjEdgeObjectsDeletedPerSec.setStatus("current")
_Ex2esjEdgeObjectsUpdatedTotal_Type = Gauge32
_Ex2esjEdgeObjectsUpdatedTotal_Object = MibTableColumn
ex2esjEdgeObjectsUpdatedTotal = _Ex2esjEdgeObjectsUpdatedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 6),
    _Ex2esjEdgeObjectsUpdatedTotal_Type()
)
ex2esjEdgeObjectsUpdatedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjEdgeObjectsUpdatedTotal.setStatus("current")
_Ex2esjEdgeObjectsUpdatedPerSec_Type = Gauge32
_Ex2esjEdgeObjectsUpdatedPerSec_Object = MibTableColumn
ex2esjEdgeObjectsUpdatedPerSec = _Ex2esjEdgeObjectsUpdatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 7),
    _Ex2esjEdgeObjectsUpdatedPerSec_Type()
)
ex2esjEdgeObjectsUpdatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjEdgeObjectsUpdatedPerSec.setStatus("current")
_Ex2esjScanJobCompletSuccessTotal_Type = Gauge32
_Ex2esjScanJobCompletSuccessTotal_Object = MibTableColumn
ex2esjScanJobCompletSuccessTotal = _Ex2esjScanJobCompletSuccessTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 8),
    _Ex2esjScanJobCompletSuccessTotal_Type()
)
ex2esjScanJobCompletSuccessTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjScanJobCompletSuccessTotal.setStatus("current")
_Ex2esjScanJobFailNotExtLockTotal_Type = Gauge32
_Ex2esjScanJobFailNotExtLockTotal_Object = MibTableColumn
ex2esjScanJobFailNotExtLockTotal = _Ex2esjScanJobFailNotExtLockTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 9),
    _Ex2esjScanJobFailNotExtLockTotal_Type()
)
ex2esjScanJobFailNotExtLockTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjScanJobFailNotExtLockTotal.setStatus("current")
_Ex2esjScanJobFailDirctErrorTotal_Type = Gauge32
_Ex2esjScanJobFailDirctErrorTotal_Object = MibTableColumn
ex2esjScanJobFailDirctErrorTotal = _Ex2esjScanJobFailDirctErrorTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 10),
    _Ex2esjScanJobFailDirctErrorTotal_Type()
)
ex2esjScanJobFailDirctErrorTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjScanJobFailDirctErrorTotal.setStatus("current")
_Ex2esjScanJobNotStartNotLockTotl_Type = Gauge32
_Ex2esjScanJobNotStartNotLockTotl_Object = MibTableColumn
ex2esjScanJobNotStartNotLockTotl = _Ex2esjScanJobNotStartNotLockTotl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 11),
    _Ex2esjScanJobNotStartNotLockTotl_Type()
)
ex2esjScanJobNotStartNotLockTotl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjScanJobNotStartNotLockTotl.setStatus("current")
_Ex2esjScanJobsStartedTotal_Type = Gauge32
_Ex2esjScanJobsStartedTotal_Object = MibTableColumn
ex2esjScanJobsStartedTotal = _Ex2esjScanJobsStartedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 12),
    _Ex2esjScanJobsStartedTotal_Type()
)
ex2esjScanJobsStartedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjScanJobsStartedTotal.setStatus("current")
_Ex2esjSourceObjectsScannedTotal_Type = Gauge32
_Ex2esjSourceObjectsScannedTotal_Object = MibTableColumn
ex2esjSourceObjectsScannedTotal = _Ex2esjSourceObjectsScannedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 13),
    _Ex2esjSourceObjectsScannedTotal_Type()
)
ex2esjSourceObjectsScannedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjSourceObjectsScannedTotal.setStatus("current")
_Ex2esjSourceObjectsScannedPerSec_Type = Gauge32
_Ex2esjSourceObjectsScannedPerSec_Object = MibTableColumn
ex2esjSourceObjectsScannedPerSec = _Ex2esjSourceObjectsScannedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 14),
    _Ex2esjSourceObjectsScannedPerSec_Type()
)
ex2esjSourceObjectsScannedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjSourceObjectsScannedPerSec.setStatus("current")
_Ex2esjTargetObjectsScannedTotal_Type = Gauge32
_Ex2esjTargetObjectsScannedTotal_Object = MibTableColumn
ex2esjTargetObjectsScannedTotal = _Ex2esjTargetObjectsScannedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 15),
    _Ex2esjTargetObjectsScannedTotal_Type()
)
ex2esjTargetObjectsScannedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjTargetObjectsScannedTotal.setStatus("current")
_Ex2esjTargetObjectsScannedPerSec_Type = Gauge32
_Ex2esjTargetObjectsScannedPerSec_Object = MibTableColumn
ex2esjTargetObjectsScannedPerSec = _Ex2esjTargetObjectsScannedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 41, 1, 16),
    _Ex2esjTargetObjectsScannedPerSec_Type()
)
ex2esjTargetObjectsScannedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2esjTargetObjectsScannedPerSec.setStatus("current")
_Ex2EdgeSyncTopology_ObjectIdentity = ObjectIdentity
ex2EdgeSyncTopology = _Ex2EdgeSyncTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 42)
)
_Ex2estCompletedScansTotal_Type = Gauge32
_Ex2estCompletedScansTotal_Object = MibScalar
ex2estCompletedScansTotal = _Ex2estCompletedScansTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 42, 1),
    _Ex2estCompletedScansTotal_Type()
)
ex2estCompletedScansTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2estCompletedScansTotal.setStatus("current")
_Ex2estEdgeServersLeasedTotal_Type = Gauge32
_Ex2estEdgeServersLeasedTotal_Object = MibScalar
ex2estEdgeServersLeasedTotal = _Ex2estEdgeServersLeasedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 42, 2),
    _Ex2estEdgeServersLeasedTotal_Type()
)
ex2estEdgeServersLeasedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2estEdgeServersLeasedTotal.setStatus("current")
_Ex2estEdgeServersTotal_Type = Gauge32
_Ex2estEdgeServersTotal_Object = MibScalar
ex2estEdgeServersTotal = _Ex2estEdgeServersTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 42, 3),
    _Ex2estEdgeServersTotal_Type()
)
ex2estEdgeServersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2estEdgeServersTotal.setStatus("current")
_Ex2estExchangeServersTotal_Type = Gauge32
_Ex2estExchangeServersTotal_Object = MibScalar
ex2estExchangeServersTotal = _Ex2estExchangeServersTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 42, 4),
    _Ex2estExchangeServersTotal_Type()
)
ex2estExchangeServersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2estExchangeServersTotal.setStatus("current")
_Ex2estHubTransportServersTotal_Type = Gauge32
_Ex2estHubTransportServersTotal_Object = MibScalar
ex2estHubTransportServersTotal = _Ex2estHubTransportServersTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 42, 5),
    _Ex2estHubTransportServersTotal_Type()
)
ex2estHubTransportServersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2estHubTransportServersTotal.setStatus("current")
_Ex2estJobsExecutingTotal_Type = Gauge32
_Ex2estJobsExecutingTotal_Object = MibScalar
ex2estJobsExecutingTotal = _Ex2estJobsExecutingTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 42, 6),
    _Ex2estJobsExecutingTotal_Type()
)
ex2estJobsExecutingTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2estJobsExecutingTotal.setStatus("current")
_Ex2estJobsSuspendingTotal_Type = Gauge32
_Ex2estJobsSuspendingTotal_Object = MibScalar
ex2estJobsSuspendingTotal = _Ex2estJobsSuspendingTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 42, 7),
    _Ex2estJobsSuspendingTotal_Type()
)
ex2estJobsSuspendingTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2estJobsSuspendingTotal.setStatus("current")
_Ex2estJobsWaitingTotal_Type = Gauge32
_Ex2estJobsWaitingTotal_Object = MibScalar
ex2estJobsWaitingTotal = _Ex2estJobsWaitingTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 42, 8),
    _Ex2estJobsWaitingTotal_Type()
)
ex2estJobsWaitingTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2estJobsWaitingTotal.setStatus("current")
_Ex2estSyncNowEdgeNotCompletTotal_Type = Gauge32
_Ex2estSyncNowEdgeNotCompletTotal_Object = MibScalar
ex2estSyncNowEdgeNotCompletTotal = _Ex2estSyncNowEdgeNotCompletTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 42, 9),
    _Ex2estSyncNowEdgeNotCompletTotal_Type()
)
ex2estSyncNowEdgeNotCompletTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2estSyncNowEdgeNotCompletTotal.setStatus("current")
_Ex2estSyncNowStartedTotal_Type = Gauge32
_Ex2estSyncNowStartedTotal_Object = MibScalar
ex2estSyncNowStartedTotal = _Ex2estSyncNowStartedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 42, 10),
    _Ex2estSyncNowStartedTotal_Type()
)
ex2estSyncNowStartedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2estSyncNowStartedTotal.setStatus("current")
_Ex2FDSOABTable_Object = MibTable
ex2FDSOABTable = _Ex2FDSOABTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 43)
)
if mibBuilder.loadTexts:
    ex2FDSOABTable.setStatus("current")
_Ex2FDSOABEntry_Object = MibTableRow
ex2FDSOABEntry = _Ex2FDSOABEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 43, 1)
)
ex2FDSOABEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2FDSOABInstance"),
)
if mibBuilder.loadTexts:
    ex2FDSOABEntry.setStatus("current")
_Ex2FDSOABInstance_Type = InstanceName
_Ex2FDSOABInstance_Object = MibTableColumn
ex2FDSOABInstance = _Ex2FDSOABInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 43, 1, 1),
    _Ex2FDSOABInstance_Type()
)
ex2FDSOABInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDSOABInstance.setStatus("current")
_Ex2FDSOABBytesDownloaded_Type = Gauge32
_Ex2FDSOABBytesDownloaded_Object = MibTableColumn
ex2FDSOABBytesDownloaded = _Ex2FDSOABBytesDownloaded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 43, 1, 2),
    _Ex2FDSOABBytesDownloaded_Type()
)
ex2FDSOABBytesDownloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDSOABBytesDownloaded.setStatus("current")
_Ex2FDSOABDownloadTaskQueued_Type = Gauge32
_Ex2FDSOABDownloadTaskQueued_Object = MibTableColumn
ex2FDSOABDownloadTaskQueued = _Ex2FDSOABDownloadTaskQueued_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 43, 1, 3),
    _Ex2FDSOABDownloadTaskQueued_Type()
)
ex2FDSOABDownloadTaskQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDSOABDownloadTaskQueued.setStatus("current")
_Ex2FDSOABDownloadTasksCompleted_Type = Gauge32
_Ex2FDSOABDownloadTasksCompleted_Object = MibTableColumn
ex2FDSOABDownloadTasksCompleted = _Ex2FDSOABDownloadTasksCompleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 43, 1, 4),
    _Ex2FDSOABDownloadTasksCompleted_Type()
)
ex2FDSOABDownloadTasksCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDSOABDownloadTasksCompleted.setStatus("current")
_Ex2FDSOABTotalBytesToDownload_Type = Gauge32
_Ex2FDSOABTotalBytesToDownload_Object = MibTableColumn
ex2FDSOABTotalBytesToDownload = _Ex2FDSOABTotalBytesToDownload_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 43, 1, 5),
    _Ex2FDSOABTotalBytesToDownload_Type()
)
ex2FDSOABTotalBytesToDownload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDSOABTotalBytesToDownload.setStatus("current")
_Ex2FDSUMTable_Object = MibTable
ex2FDSUMTable = _Ex2FDSUMTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 44)
)
if mibBuilder.loadTexts:
    ex2FDSUMTable.setStatus("current")
_Ex2FDSUMEntry_Object = MibTableRow
ex2FDSUMEntry = _Ex2FDSUMEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 44, 1)
)
ex2FDSUMEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2FDSUMInstance"),
)
if mibBuilder.loadTexts:
    ex2FDSUMEntry.setStatus("current")
_Ex2FDSUMInstance_Type = InstanceName
_Ex2FDSUMInstance_Object = MibTableColumn
ex2FDSUMInstance = _Ex2FDSUMInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 44, 1, 1),
    _Ex2FDSUMInstance_Type()
)
ex2FDSUMInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDSUMInstance.setStatus("current")
_Ex2FDSUMBytesDownloaded_Type = Gauge32
_Ex2FDSUMBytesDownloaded_Object = MibTableColumn
ex2FDSUMBytesDownloaded = _Ex2FDSUMBytesDownloaded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 44, 1, 2),
    _Ex2FDSUMBytesDownloaded_Type()
)
ex2FDSUMBytesDownloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDSUMBytesDownloaded.setStatus("current")
_Ex2FDSUMDownloadTaskQueued_Type = Gauge32
_Ex2FDSUMDownloadTaskQueued_Object = MibTableColumn
ex2FDSUMDownloadTaskQueued = _Ex2FDSUMDownloadTaskQueued_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 44, 1, 3),
    _Ex2FDSUMDownloadTaskQueued_Type()
)
ex2FDSUMDownloadTaskQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDSUMDownloadTaskQueued.setStatus("current")
_Ex2FDSUMDownloadTasksCompleted_Type = Gauge32
_Ex2FDSUMDownloadTasksCompleted_Object = MibTableColumn
ex2FDSUMDownloadTasksCompleted = _Ex2FDSUMDownloadTasksCompleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 44, 1, 4),
    _Ex2FDSUMDownloadTasksCompleted_Type()
)
ex2FDSUMDownloadTasksCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDSUMDownloadTasksCompleted.setStatus("current")
_Ex2FDSUMTotalBytesToDownload_Type = Gauge32
_Ex2FDSUMTotalBytesToDownload_Object = MibTableColumn
ex2FDSUMTotalBytesToDownload = _Ex2FDSUMTotalBytesToDownload_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 44, 1, 5),
    _Ex2FDSUMTotalBytesToDownload_Type()
)
ex2FDSUMTotalBytesToDownload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDSUMTotalBytesToDownload.setStatus("current")
_Ex2InformationStore_ObjectIdentity = ObjectIdentity
ex2InformationStore = _Ex2InformationStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45)
)
_Ex2ISACLUpgradeCompletedUpgrades_Type = Gauge32
_Ex2ISACLUpgradeCompletedUpgrades_Object = MibScalar
ex2ISACLUpgradeCompletedUpgrades = _Ex2ISACLUpgradeCompletedUpgrades_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 1),
    _Ex2ISACLUpgradeCompletedUpgrades_Type()
)
ex2ISACLUpgradeCompletedUpgrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISACLUpgradeCompletedUpgrades.setStatus("current")
_Ex2ISACLUpgradeFailures_Type = Gauge32
_Ex2ISACLUpgradeFailures_Object = MibScalar
ex2ISACLUpgradeFailures = _Ex2ISACLUpgradeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 2),
    _Ex2ISACLUpgradeFailures_Type()
)
ex2ISACLUpgradeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISACLUpgradeFailures.setStatus("current")
_Ex2ISACLUpgrdHitACLUpgrdRtryList_Type = Gauge32
_Ex2ISACLUpgrdHitACLUpgrdRtryList_Object = MibScalar
ex2ISACLUpgrdHitACLUpgrdRtryList = _Ex2ISACLUpgrdHitACLUpgrdRtryList_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 3),
    _Ex2ISACLUpgrdHitACLUpgrdRtryList_Type()
)
ex2ISACLUpgrdHitACLUpgrdRtryList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISACLUpgrdHitACLUpgrdRtryList.setStatus("current")
_Ex2ISACLUpgradePartialUpgrades_Type = Gauge32
_Ex2ISACLUpgradePartialUpgrades_Object = MibScalar
ex2ISACLUpgradePartialUpgrades = _Ex2ISACLUpgradePartialUpgrades_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 4),
    _Ex2ISACLUpgradePartialUpgrades_Type()
)
ex2ISACLUpgradePartialUpgrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISACLUpgradePartialUpgrades.setStatus("current")
_Ex2ISACLUpgradeTimesAttempted_Type = Gauge32
_Ex2ISACLUpgradeTimesAttempted_Object = MibScalar
ex2ISACLUpgradeTimesAttempted = _Ex2ISACLUpgradeTimesAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 5),
    _Ex2ISACLUpgradeTimesAttempted_Type()
)
ex2ISACLUpgradeTimesAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISACLUpgradeTimesAttempted.setStatus("current")
_Ex2ISActiveAnonymousUserCount_Type = Gauge32
_Ex2ISActiveAnonymousUserCount_Object = MibScalar
ex2ISActiveAnonymousUserCount = _Ex2ISActiveAnonymousUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 6),
    _Ex2ISActiveAnonymousUserCount_Type()
)
ex2ISActiveAnonymousUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISActiveAnonymousUserCount.setStatus("current")
_Ex2ISActiveConnectionCount_Type = Gauge32
_Ex2ISActiveConnectionCount_Object = MibScalar
ex2ISActiveConnectionCount = _Ex2ISActiveConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 7),
    _Ex2ISActiveConnectionCount_Type()
)
ex2ISActiveConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISActiveConnectionCount.setStatus("current")
_Ex2ISActiveUserCount_Type = Gauge32
_Ex2ISActiveUserCount_Object = MibScalar
ex2ISActiveUserCount = _Ex2ISActiveUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 8),
    _Ex2ISActiveUserCount_Type()
)
ex2ISActiveUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISActiveUserCount.setStatus("current")
_Ex2ISAdminRPCRequests_Type = Gauge32
_Ex2ISAdminRPCRequests_Object = MibScalar
ex2ISAdminRPCRequests = _Ex2ISAdminRPCRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 9),
    _Ex2ISAdminRPCRequests_Type()
)
ex2ISAdminRPCRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISAdminRPCRequests.setStatus("current")
_Ex2ISAdminRPCRequestsPeak_Type = Gauge32
_Ex2ISAdminRPCRequestsPeak_Object = MibScalar
ex2ISAdminRPCRequestsPeak = _Ex2ISAdminRPCRequestsPeak_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 10),
    _Ex2ISAdminRPCRequestsPeak_Type()
)
ex2ISAdminRPCRequestsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISAdminRPCRequestsPeak.setStatus("current")
_Ex2ISAnonymousUserCount_Type = Gauge32
_Ex2ISAnonymousUserCount_Object = MibScalar
ex2ISAnonymousUserCount = _Ex2ISAnonymousUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 11),
    _Ex2ISAnonymousUserCount_Type()
)
ex2ISAnonymousUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISAnonymousUserCount.setStatus("current")
_Ex2ISApptmtInstanceCreationRate_Type = Gauge32
_Ex2ISApptmtInstanceCreationRate_Object = MibScalar
ex2ISApptmtInstanceCreationRate = _Ex2ISApptmtInstanceCreationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 12),
    _Ex2ISApptmtInstanceCreationRate_Type()
)
ex2ISApptmtInstanceCreationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISApptmtInstanceCreationRate.setStatus("current")
_Ex2ISApptmtInstanceDeletionRate_Type = Gauge32
_Ex2ISApptmtInstanceDeletionRate_Object = MibScalar
ex2ISApptmtInstanceDeletionRate = _Ex2ISApptmtInstanceDeletionRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 13),
    _Ex2ISApptmtInstanceDeletionRate_Type()
)
ex2ISApptmtInstanceDeletionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISApptmtInstanceDeletionRate.setStatus("current")
_Ex2ISAppointmentInstancesCreated_Type = Gauge32
_Ex2ISAppointmentInstancesCreated_Object = MibScalar
ex2ISAppointmentInstancesCreated = _Ex2ISAppointmentInstancesCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 14),
    _Ex2ISAppointmentInstancesCreated_Type()
)
ex2ISAppointmentInstancesCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISAppointmentInstancesCreated.setStatus("current")
_Ex2ISAppointmentInstancesDeleted_Type = Gauge32
_Ex2ISAppointmentInstancesDeleted_Object = MibScalar
ex2ISAppointmentInstancesDeleted = _Ex2ISAppointmentInstancesDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 15),
    _Ex2ISAppointmentInstancesDeleted_Type()
)
ex2ISAppointmentInstancesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISAppointmentInstancesDeleted.setStatus("current")
_Ex2ISAsyncNotificationsCacheSize_Type = Gauge32
_Ex2ISAsyncNotificationsCacheSize_Object = MibScalar
ex2ISAsyncNotificationsCacheSize = _Ex2ISAsyncNotificationsCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 16),
    _Ex2ISAsyncNotificationsCacheSize_Type()
)
ex2ISAsyncNotificationsCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISAsyncNotificationsCacheSize.setStatus("current")
_Ex2ISAsyncNotificatGeneratPerSec_Type = Gauge32
_Ex2ISAsyncNotificatGeneratPerSec_Object = MibScalar
ex2ISAsyncNotificatGeneratPerSec = _Ex2ISAsyncNotificatGeneratPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 17),
    _Ex2ISAsyncNotificatGeneratPerSec_Type()
)
ex2ISAsyncNotificatGeneratPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISAsyncNotificatGeneratPerSec.setStatus("current")
_Ex2ISAsyncRPCRequests_Type = Gauge32
_Ex2ISAsyncRPCRequests_Object = MibScalar
ex2ISAsyncRPCRequests = _Ex2ISAsyncRPCRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 18),
    _Ex2ISAsyncRPCRequests_Type()
)
ex2ISAsyncRPCRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISAsyncRPCRequests.setStatus("current")
_Ex2ISAsyncRPCRequestsPeak_Type = Gauge32
_Ex2ISAsyncRPCRequestsPeak_Object = MibScalar
ex2ISAsyncRPCRequestsPeak = _Ex2ISAsyncRPCRequestsPeak_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 19),
    _Ex2ISAsyncRPCRequestsPeak_Type()
)
ex2ISAsyncRPCRequestsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISAsyncRPCRequestsPeak.setStatus("current")
_Ex2ISBackgroundExpanQueueLength_Type = Gauge32
_Ex2ISBackgroundExpanQueueLength_Object = MibScalar
ex2ISBackgroundExpanQueueLength = _Ex2ISBackgroundExpanQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 20),
    _Ex2ISBackgroundExpanQueueLength_Type()
)
ex2ISBackgroundExpanQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISBackgroundExpanQueueLength.setStatus("current")
_Ex2ISCIQPThreads_Type = Gauge32
_Ex2ISCIQPThreads_Object = MibScalar
ex2ISCIQPThreads = _Ex2ISCIQPThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 21),
    _Ex2ISCIQPThreads_Type()
)
ex2ISCIQPThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCIQPThreads.setStatus("current")
_Ex2ISClientBackgroundRPCsFailed_Type = Gauge32
_Ex2ISClientBackgroundRPCsFailed_Object = MibScalar
ex2ISClientBackgroundRPCsFailed = _Ex2ISClientBackgroundRPCsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 22),
    _Ex2ISClientBackgroundRPCsFailed_Type()
)
ex2ISClientBackgroundRPCsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientBackgroundRPCsFailed.setStatus("current")
_Ex2ISClientBackgroundRPCsFailSec_Type = Gauge32
_Ex2ISClientBackgroundRPCsFailSec_Object = MibScalar
ex2ISClientBackgroundRPCsFailSec = _Ex2ISClientBackgroundRPCsFailSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 23),
    _Ex2ISClientBackgroundRPCsFailSec_Type()
)
ex2ISClientBackgroundRPCsFailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientBackgroundRPCsFailSec.setStatus("current")
_Ex2ISClientBackgroundRPCsSucceed_Type = Gauge32
_Ex2ISClientBackgroundRPCsSucceed_Object = MibScalar
ex2ISClientBackgroundRPCsSucceed = _Ex2ISClientBackgroundRPCsSucceed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 24),
    _Ex2ISClientBackgroundRPCsSucceed_Type()
)
ex2ISClientBackgroundRPCsSucceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientBackgroundRPCsSucceed.setStatus("current")
_Ex2ISClientBgRPCSucceedPerSec_Type = Gauge32
_Ex2ISClientBgRPCSucceedPerSec_Object = MibScalar
ex2ISClientBgRPCSucceedPerSec = _Ex2ISClientBgRPCSucceedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 25),
    _Ex2ISClientBgRPCSucceedPerSec_Type()
)
ex2ISClientBgRPCSucceedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientBgRPCSucceedPerSec.setStatus("current")
_Ex2ISClientForegroundRPCsFailed_Type = Gauge32
_Ex2ISClientForegroundRPCsFailed_Object = MibScalar
ex2ISClientForegroundRPCsFailed = _Ex2ISClientForegroundRPCsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 26),
    _Ex2ISClientForegroundRPCsFailed_Type()
)
ex2ISClientForegroundRPCsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientForegroundRPCsFailed.setStatus("current")
_Ex2ISClientFgRPCsFailedPerSec_Type = Gauge32
_Ex2ISClientFgRPCsFailedPerSec_Object = MibScalar
ex2ISClientFgRPCsFailedPerSec = _Ex2ISClientFgRPCsFailedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 27),
    _Ex2ISClientFgRPCsFailedPerSec_Type()
)
ex2ISClientFgRPCsFailedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientFgRPCsFailedPerSec.setStatus("current")
_Ex2ISClientFgRPCsSucceeded_Type = Gauge32
_Ex2ISClientFgRPCsSucceeded_Object = MibScalar
ex2ISClientFgRPCsSucceeded = _Ex2ISClientFgRPCsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 28),
    _Ex2ISClientFgRPCsSucceeded_Type()
)
ex2ISClientFgRPCsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientFgRPCsSucceeded.setStatus("current")
_Ex2ISClientFgRPCsSucceededPerSec_Type = Gauge32
_Ex2ISClientFgRPCsSucceededPerSec_Object = MibScalar
ex2ISClientFgRPCsSucceededPerSec = _Ex2ISClientFgRPCsSucceededPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 29),
    _Ex2ISClientFgRPCsSucceededPerSec_Type()
)
ex2ISClientFgRPCsSucceededPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientFgRPCsSucceededPerSec.setStatus("current")
_Ex2ISClientLatencyGT10SecRPCs_Type = Gauge32
_Ex2ISClientLatencyGT10SecRPCs_Object = MibScalar
ex2ISClientLatencyGT10SecRPCs = _Ex2ISClientLatencyGT10SecRPCs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 30),
    _Ex2ISClientLatencyGT10SecRPCs_Type()
)
ex2ISClientLatencyGT10SecRPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientLatencyGT10SecRPCs.setStatus("current")
_Ex2ISClientLatencyGT2SecRPCs_Type = Gauge32
_Ex2ISClientLatencyGT2SecRPCs_Object = MibScalar
ex2ISClientLatencyGT2SecRPCs = _Ex2ISClientLatencyGT2SecRPCs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 31),
    _Ex2ISClientLatencyGT2SecRPCs_Type()
)
ex2ISClientLatencyGT2SecRPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientLatencyGT2SecRPCs.setStatus("current")
_Ex2ISClientLatencyGT5SecRPCs_Type = Gauge32
_Ex2ISClientLatencyGT5SecRPCs_Object = MibScalar
ex2ISClientLatencyGT5SecRPCs = _Ex2ISClientLatencyGT5SecRPCs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 32),
    _Ex2ISClientLatencyGT5SecRPCs_Type()
)
ex2ISClientLatencyGT5SecRPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientLatencyGT5SecRPCs.setStatus("current")
_Ex2ISClientRPCsFailed_Type = Gauge32
_Ex2ISClientRPCsFailed_Object = MibScalar
ex2ISClientRPCsFailed = _Ex2ISClientRPCsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 33),
    _Ex2ISClientRPCsFailed_Type()
)
ex2ISClientRPCsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCsFailed.setStatus("current")
_Ex2ISClientRPCsFailedPerSec_Type = Gauge32
_Ex2ISClientRPCsFailedPerSec_Object = MibScalar
ex2ISClientRPCsFailedPerSec = _Ex2ISClientRPCsFailedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 34),
    _Ex2ISClientRPCsFailedPerSec_Type()
)
ex2ISClientRPCsFailedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCsFailedPerSec.setStatus("current")
_Ex2ISClientRPCFailedAccessDenied_Type = Gauge32
_Ex2ISClientRPCFailedAccessDenied_Object = MibScalar
ex2ISClientRPCFailedAccessDenied = _Ex2ISClientRPCFailedAccessDenied_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 35),
    _Ex2ISClientRPCFailedAccessDenied_Type()
)
ex2ISClientRPCFailedAccessDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCFailedAccessDenied.setStatus("current")
_Ex2ISClientRPCFailAccessDenySec_Type = Gauge32
_Ex2ISClientRPCFailAccessDenySec_Object = MibScalar
ex2ISClientRPCFailAccessDenySec = _Ex2ISClientRPCFailAccessDenySec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 36),
    _Ex2ISClientRPCFailAccessDenySec_Type()
)
ex2ISClientRPCFailAccessDenySec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCFailAccessDenySec.setStatus("current")
_Ex2ISClientRPCFailAllOtherErrors_Type = Gauge32
_Ex2ISClientRPCFailAllOtherErrors_Object = MibScalar
ex2ISClientRPCFailAllOtherErrors = _Ex2ISClientRPCFailAllOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 37),
    _Ex2ISClientRPCFailAllOtherErrors_Type()
)
ex2ISClientRPCFailAllOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCFailAllOtherErrors.setStatus("current")
_Ex2ISClientRPCFailOtherErrorSec_Type = Gauge32
_Ex2ISClientRPCFailOtherErrorSec_Object = MibScalar
ex2ISClientRPCFailOtherErrorSec = _Ex2ISClientRPCFailOtherErrorSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 38),
    _Ex2ISClientRPCFailOtherErrorSec_Type()
)
ex2ISClientRPCFailOtherErrorSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCFailOtherErrorSec.setStatus("current")
_Ex2ISClientRPCFailCallCancelled_Type = Gauge32
_Ex2ISClientRPCFailCallCancelled_Object = MibScalar
ex2ISClientRPCFailCallCancelled = _Ex2ISClientRPCFailCallCancelled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 39),
    _Ex2ISClientRPCFailCallCancelled_Type()
)
ex2ISClientRPCFailCallCancelled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCFailCallCancelled.setStatus("current")
_Ex2ISClientRPCFailCallCancelSec_Type = Gauge32
_Ex2ISClientRPCFailCallCancelSec_Object = MibScalar
ex2ISClientRPCFailCallCancelSec = _Ex2ISClientRPCFailCallCancelSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 40),
    _Ex2ISClientRPCFailCallCancelSec_Type()
)
ex2ISClientRPCFailCallCancelSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCFailCallCancelSec.setStatus("current")
_Ex2ISClientRPCsFailedCallFailed_Type = Gauge32
_Ex2ISClientRPCsFailedCallFailed_Object = MibScalar
ex2ISClientRPCsFailedCallFailed = _Ex2ISClientRPCsFailedCallFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 41),
    _Ex2ISClientRPCsFailedCallFailed_Type()
)
ex2ISClientRPCsFailedCallFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCsFailedCallFailed.setStatus("current")
_Ex2ISClientRPCFailCallFailedSec_Type = Gauge32
_Ex2ISClientRPCFailCallFailedSec_Object = MibScalar
ex2ISClientRPCFailCallFailedSec = _Ex2ISClientRPCFailCallFailedSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 42),
    _Ex2ISClientRPCFailCallFailedSec_Type()
)
ex2ISClientRPCFailCallFailedSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCFailCallFailedSec.setStatus("current")
_Ex2ISClientRPCFailServerTooBusy_Type = Gauge32
_Ex2ISClientRPCFailServerTooBusy_Object = MibScalar
ex2ISClientRPCFailServerTooBusy = _Ex2ISClientRPCFailServerTooBusy_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 43),
    _Ex2ISClientRPCFailServerTooBusy_Type()
)
ex2ISClientRPCFailServerTooBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCFailServerTooBusy.setStatus("current")
_Ex2ISClientRPCFailServerToBsySec_Type = Gauge32
_Ex2ISClientRPCFailServerToBsySec_Object = MibScalar
ex2ISClientRPCFailServerToBsySec = _Ex2ISClientRPCFailServerToBsySec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 44),
    _Ex2ISClientRPCFailServerToBsySec_Type()
)
ex2ISClientRPCFailServerToBsySec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCFailServerToBsySec.setStatus("current")
_Ex2ISClientRPCFailServerUnavail_Type = Gauge32
_Ex2ISClientRPCFailServerUnavail_Object = MibScalar
ex2ISClientRPCFailServerUnavail = _Ex2ISClientRPCFailServerUnavail_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 45),
    _Ex2ISClientRPCFailServerUnavail_Type()
)
ex2ISClientRPCFailServerUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCFailServerUnavail.setStatus("current")
_Ex2ISClientRPCFailServUnavailSec_Type = Gauge32
_Ex2ISClientRPCFailServUnavailSec_Object = MibScalar
ex2ISClientRPCFailServUnavailSec = _Ex2ISClientRPCFailServUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 46),
    _Ex2ISClientRPCFailServUnavailSec_Type()
)
ex2ISClientRPCFailServUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCFailServUnavailSec.setStatus("current")
_Ex2ISClientRPCsAttempted_Type = Gauge32
_Ex2ISClientRPCsAttempted_Object = MibScalar
ex2ISClientRPCsAttempted = _Ex2ISClientRPCsAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 47),
    _Ex2ISClientRPCsAttempted_Type()
)
ex2ISClientRPCsAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCsAttempted.setStatus("current")
_Ex2ISClientRPCsAttemptedPerSec_Type = Gauge32
_Ex2ISClientRPCsAttemptedPerSec_Object = MibScalar
ex2ISClientRPCsAttemptedPerSec = _Ex2ISClientRPCsAttemptedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 48),
    _Ex2ISClientRPCsAttemptedPerSec_Type()
)
ex2ISClientRPCsAttemptedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCsAttemptedPerSec.setStatus("current")
_Ex2ISClientRPCsSucceeded_Type = Gauge32
_Ex2ISClientRPCsSucceeded_Object = MibScalar
ex2ISClientRPCsSucceeded = _Ex2ISClientRPCsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 49),
    _Ex2ISClientRPCsSucceeded_Type()
)
ex2ISClientRPCsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCsSucceeded.setStatus("current")
_Ex2ISClientRPCsSucceededPerSec_Type = Gauge32
_Ex2ISClientRPCsSucceededPerSec_Object = MibScalar
ex2ISClientRPCsSucceededPerSec = _Ex2ISClientRPCsSucceededPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 50),
    _Ex2ISClientRPCsSucceededPerSec_Type()
)
ex2ISClientRPCsSucceededPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientRPCsSucceededPerSec.setStatus("current")
_Ex2ISClientTotalReportedLatency_Type = Gauge32
_Ex2ISClientTotalReportedLatency_Object = MibScalar
ex2ISClientTotalReportedLatency = _Ex2ISClientTotalReportedLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 51),
    _Ex2ISClientTotalReportedLatency_Type()
)
ex2ISClientTotalReportedLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISClientTotalReportedLatency.setStatus("current")
_Ex2ISConnectionCount_Type = Gauge32
_Ex2ISConnectionCount_Object = MibScalar
ex2ISConnectionCount = _Ex2ISConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 52),
    _Ex2ISConnectionCount_Type()
)
ex2ISConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISConnectionCount.setStatus("current")
_Ex2ISDLMembershipCacheEntryCount_Type = Gauge32
_Ex2ISDLMembershipCacheEntryCount_Object = MibScalar
ex2ISDLMembershipCacheEntryCount = _Ex2ISDLMembershipCacheEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 53),
    _Ex2ISDLMembershipCacheEntryCount_Type()
)
ex2ISDLMembershipCacheEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISDLMembershipCacheEntryCount.setStatus("current")
_Ex2ISDLMembershipCacheHits_Type = Gauge32
_Ex2ISDLMembershipCacheHits_Object = MibScalar
ex2ISDLMembershipCacheHits = _Ex2ISDLMembershipCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 54),
    _Ex2ISDLMembershipCacheHits_Type()
)
ex2ISDLMembershipCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISDLMembershipCacheHits.setStatus("current")
_Ex2ISDLMembershipCacheMisses_Type = Gauge32
_Ex2ISDLMembershipCacheMisses_Object = MibScalar
ex2ISDLMembershipCacheMisses = _Ex2ISDLMembershipCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 55),
    _Ex2ISDLMembershipCacheMisses_Type()
)
ex2ISDLMembershipCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISDLMembershipCacheMisses.setStatus("current")
_Ex2ISDLMembershipCacheSize_Type = Gauge32
_Ex2ISDLMembershipCacheSize_Object = MibScalar
ex2ISDLMembershipCacheSize = _Ex2ISDLMembershipCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 56),
    _Ex2ISDLMembershipCacheSize_Type()
)
ex2ISDLMembershipCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISDLMembershipCacheSize.setStatus("current")
_Ex2ISExchmemCurrentByteAllocated_Type = Gauge32
_Ex2ISExchmemCurrentByteAllocated_Object = MibScalar
ex2ISExchmemCurrentByteAllocated = _Ex2ISExchmemCurrentByteAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 57),
    _Ex2ISExchmemCurrentByteAllocated_Type()
)
ex2ISExchmemCurrentByteAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISExchmemCurrentByteAllocated.setStatus("current")
_Ex2ISExchmemCurrNumbOfVirtAlloca_Type = Gauge32
_Ex2ISExchmemCurrNumbOfVirtAlloca_Object = MibScalar
ex2ISExchmemCurrNumbOfVirtAlloca = _Ex2ISExchmemCurrNumbOfVirtAlloca_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 58),
    _Ex2ISExchmemCurrNumbOfVirtAlloca_Type()
)
ex2ISExchmemCurrNumbOfVirtAlloca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISExchmemCurrNumbOfVirtAlloca.setStatus("current")
_Ex2ISExchmemCurrVirtByteAllocate_Type = Gauge32
_Ex2ISExchmemCurrVirtByteAllocate_Object = MibScalar
ex2ISExchmemCurrVirtByteAllocate = _Ex2ISExchmemCurrVirtByteAllocate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 59),
    _Ex2ISExchmemCurrVirtByteAllocate_Type()
)
ex2ISExchmemCurrVirtByteAllocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISExchmemCurrVirtByteAllocate.setStatus("current")
_Ex2ISExchmemMaximumByteAllocated_Type = Gauge32
_Ex2ISExchmemMaximumByteAllocated_Object = MibScalar
ex2ISExchmemMaximumByteAllocated = _Ex2ISExchmemMaximumByteAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 60),
    _Ex2ISExchmemMaximumByteAllocated_Type()
)
ex2ISExchmemMaximumByteAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISExchmemMaximumByteAllocated.setStatus("current")
_Ex2ISExchmemMaxVirtualBytAllocat_Type = Gauge32
_Ex2ISExchmemMaxVirtualBytAllocat_Object = MibScalar
ex2ISExchmemMaxVirtualBytAllocat = _Ex2ISExchmemMaxVirtualBytAllocat_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 61),
    _Ex2ISExchmemMaxVirtualBytAllocat_Type()
)
ex2ISExchmemMaxVirtualBytAllocat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISExchmemMaxVirtualBytAllocat.setStatus("current")
_Ex2ISExchmemNumAdditionalHeaps_Type = Gauge32
_Ex2ISExchmemNumAdditionalHeaps_Object = MibScalar
ex2ISExchmemNumAdditionalHeaps = _Ex2ISExchmemNumAdditionalHeaps_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 62),
    _Ex2ISExchmemNumAdditionalHeaps_Type()
)
ex2ISExchmemNumAdditionalHeaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISExchmemNumAdditionalHeaps.setStatus("current")
_Ex2ISExchmemNumberOfHeaps_Type = Gauge32
_Ex2ISExchmemNumberOfHeaps_Object = MibScalar
ex2ISExchmemNumberOfHeaps = _Ex2ISExchmemNumberOfHeaps_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 63),
    _Ex2ISExchmemNumberOfHeaps_Type()
)
ex2ISExchmemNumberOfHeaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISExchmemNumberOfHeaps.setStatus("current")
_Ex2ISExchmemNumHeapsMemErrors_Type = Gauge32
_Ex2ISExchmemNumHeapsMemErrors_Object = MibScalar
ex2ISExchmemNumHeapsMemErrors = _Ex2ISExchmemNumHeapsMemErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 64),
    _Ex2ISExchmemNumHeapsMemErrors_Type()
)
ex2ISExchmemNumHeapsMemErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISExchmemNumHeapsMemErrors.setStatus("current")
_Ex2ISExchmemNumberOfMemoryErrors_Type = Gauge32
_Ex2ISExchmemNumberOfMemoryErrors_Object = MibScalar
ex2ISExchmemNumberOfMemoryErrors = _Ex2ISExchmemNumberOfMemoryErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 65),
    _Ex2ISExchmemNumberOfMemoryErrors_Type()
)
ex2ISExchmemNumberOfMemoryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISExchmemNumberOfMemoryErrors.setStatus("current")
_Ex2ISExchmemTotalNumVirtAllocate_Type = Gauge32
_Ex2ISExchmemTotalNumVirtAllocate_Object = MibScalar
ex2ISExchmemTotalNumVirtAllocate = _Ex2ISExchmemTotalNumVirtAllocate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 66),
    _Ex2ISExchmemTotalNumVirtAllocate_Type()
)
ex2ISExchmemTotalNumVirtAllocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISExchmemTotalNumVirtAllocate.setStatus("current")
_Ex2ISFBPublishCount_Type = Gauge32
_Ex2ISFBPublishCount_Object = MibScalar
ex2ISFBPublishCount = _Ex2ISFBPublishCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 67),
    _Ex2ISFBPublishCount_Type()
)
ex2ISFBPublishCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISFBPublishCount.setStatus("current")
_Ex2ISFBPublishRate_Type = Gauge32
_Ex2ISFBPublishRate_Object = MibScalar
ex2ISFBPublishRate = _Ex2ISFBPublishRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 68),
    _Ex2ISFBPublishRate_Type()
)
ex2ISFBPublishRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISFBPublishRate.setStatus("current")
_Ex2ISMaximumAnonymousUsers_Type = Gauge32
_Ex2ISMaximumAnonymousUsers_Object = MibScalar
ex2ISMaximumAnonymousUsers = _Ex2ISMaximumAnonymousUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 69),
    _Ex2ISMaximumAnonymousUsers_Type()
)
ex2ISMaximumAnonymousUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISMaximumAnonymousUsers.setStatus("current")
_Ex2ISMaximumConnections_Type = Gauge32
_Ex2ISMaximumConnections_Object = MibScalar
ex2ISMaximumConnections = _Ex2ISMaximumConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 70),
    _Ex2ISMaximumConnections_Type()
)
ex2ISMaximumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISMaximumConnections.setStatus("current")
_Ex2ISMaximumUsers_Type = Gauge32
_Ex2ISMaximumUsers_Object = MibScalar
ex2ISMaximumUsers = _Ex2ISMaximumUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 71),
    _Ex2ISMaximumUsers_Type()
)
ex2ISMaximumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISMaximumUsers.setStatus("current")
_Ex2ISOABDifferentialDnldAttempts_Type = Gauge32
_Ex2ISOABDifferentialDnldAttempts_Object = MibScalar
ex2ISOABDifferentialDnldAttempts = _Ex2ISOABDifferentialDnldAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 72),
    _Ex2ISOABDifferentialDnldAttempts_Type()
)
ex2ISOABDifferentialDnldAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISOABDifferentialDnldAttempts.setStatus("current")
_Ex2ISOABDifferentialDnldBytes_Type = Gauge32
_Ex2ISOABDifferentialDnldBytes_Object = MibScalar
ex2ISOABDifferentialDnldBytes = _Ex2ISOABDifferentialDnldBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 73),
    _Ex2ISOABDifferentialDnldBytes_Type()
)
ex2ISOABDifferentialDnldBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISOABDifferentialDnldBytes.setStatus("current")
_Ex2ISOABDifferentialDnldBytesSec_Type = Gauge32
_Ex2ISOABDifferentialDnldBytesSec_Object = MibScalar
ex2ISOABDifferentialDnldBytesSec = _Ex2ISOABDifferentialDnldBytesSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 74),
    _Ex2ISOABDifferentialDnldBytesSec_Type()
)
ex2ISOABDifferentialDnldBytesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISOABDifferentialDnldBytesSec.setStatus("current")
_Ex2ISOABFullDownloadAttempts_Type = Gauge32
_Ex2ISOABFullDownloadAttempts_Object = MibScalar
ex2ISOABFullDownloadAttempts = _Ex2ISOABFullDownloadAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 75),
    _Ex2ISOABFullDownloadAttempts_Type()
)
ex2ISOABFullDownloadAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISOABFullDownloadAttempts.setStatus("current")
_Ex2ISOABFullDnldAttemptsBlocked_Type = Gauge32
_Ex2ISOABFullDnldAttemptsBlocked_Object = MibScalar
ex2ISOABFullDnldAttemptsBlocked = _Ex2ISOABFullDnldAttemptsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 76),
    _Ex2ISOABFullDnldAttemptsBlocked_Type()
)
ex2ISOABFullDnldAttemptsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISOABFullDnldAttemptsBlocked.setStatus("current")
_Ex2ISOABFullDownloadBytes_Type = Gauge32
_Ex2ISOABFullDownloadBytes_Object = MibScalar
ex2ISOABFullDownloadBytes = _Ex2ISOABFullDownloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 77),
    _Ex2ISOABFullDownloadBytes_Type()
)
ex2ISOABFullDownloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISOABFullDownloadBytes.setStatus("current")
_Ex2ISOABFullDownloadBytesPerSec_Type = Gauge32
_Ex2ISOABFullDownloadBytesPerSec_Object = MibScalar
ex2ISOABFullDownloadBytesPerSec = _Ex2ISOABFullDownloadBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 78),
    _Ex2ISOABFullDownloadBytesPerSec_Type()
)
ex2ISOABFullDownloadBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISOABFullDownloadBytesPerSec.setStatus("current")
_Ex2ISPeakAsyncNotificaCacheSize_Type = Gauge32
_Ex2ISPeakAsyncNotificaCacheSize_Object = MibScalar
ex2ISPeakAsyncNotificaCacheSize = _Ex2ISPeakAsyncNotificaCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 79),
    _Ex2ISPeakAsyncNotificaCacheSize_Type()
)
ex2ISPeakAsyncNotificaCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISPeakAsyncNotificaCacheSize.setStatus("current")
_Ex2ISPeakPushNotificatCacheSize_Type = Gauge32
_Ex2ISPeakPushNotificatCacheSize_Object = MibScalar
ex2ISPeakPushNotificatCacheSize = _Ex2ISPeakPushNotificatCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 80),
    _Ex2ISPeakPushNotificatCacheSize_Type()
)
ex2ISPeakPushNotificatCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISPeakPushNotificatCacheSize.setStatus("current")
_Ex2ISPushNotificationsCacheSize_Type = Gauge32
_Ex2ISPushNotificationsCacheSize_Object = MibScalar
ex2ISPushNotificationsCacheSize = _Ex2ISPushNotificationsCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 81),
    _Ex2ISPushNotificationsCacheSize_Type()
)
ex2ISPushNotificationsCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISPushNotificationsCacheSize.setStatus("current")
_Ex2ISPushNotificatGeneratePerSec_Type = Gauge32
_Ex2ISPushNotificatGeneratePerSec_Object = MibScalar
ex2ISPushNotificatGeneratePerSec = _Ex2ISPushNotificatGeneratePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 82),
    _Ex2ISPushNotificatGeneratePerSec_Type()
)
ex2ISPushNotificatGeneratePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISPushNotificatGeneratePerSec.setStatus("current")
_Ex2ISPushNotificationsSkipPerSec_Type = Gauge32
_Ex2ISPushNotificationsSkipPerSec_Object = MibScalar
ex2ISPushNotificationsSkipPerSec = _Ex2ISPushNotificationsSkipPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 83),
    _Ex2ISPushNotificationsSkipPerSec_Type()
)
ex2ISPushNotificationsSkipPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISPushNotificationsSkipPerSec.setStatus("current")
_Ex2ISRPCAveragedLatency_Type = Gauge32
_Ex2ISRPCAveragedLatency_Object = MibScalar
ex2ISRPCAveragedLatency = _Ex2ISRPCAveragedLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 84),
    _Ex2ISRPCAveragedLatency_Type()
)
ex2ISRPCAveragedLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRPCAveragedLatency.setStatus("current")
_Ex2ISRPCClientBackoffPerSec_Type = Gauge32
_Ex2ISRPCClientBackoffPerSec_Object = MibScalar
ex2ISRPCClientBackoffPerSec = _Ex2ISRPCClientBackoffPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 85),
    _Ex2ISRPCClientBackoffPerSec_Type()
)
ex2ISRPCClientBackoffPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRPCClientBackoffPerSec.setStatus("current")
_Ex2ISRPCClientsBytesRead_Type = Gauge32
_Ex2ISRPCClientsBytesRead_Object = MibScalar
ex2ISRPCClientsBytesRead = _Ex2ISRPCClientsBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 86),
    _Ex2ISRPCClientsBytesRead_Type()
)
ex2ISRPCClientsBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRPCClientsBytesRead.setStatus("current")
_Ex2ISRPCClientsBytesWritten_Type = Gauge32
_Ex2ISRPCClientsBytesWritten_Object = MibScalar
ex2ISRPCClientsBytesWritten = _Ex2ISRPCClientsBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 87),
    _Ex2ISRPCClientsBytesWritten_Type()
)
ex2ISRPCClientsBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRPCClientsBytesWritten.setStatus("current")
_Ex2ISRPCClientsUncomprsdByteRead_Type = Gauge32
_Ex2ISRPCClientsUncomprsdByteRead_Object = MibScalar
ex2ISRPCClientsUncomprsdByteRead = _Ex2ISRPCClientsUncomprsdByteRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 88),
    _Ex2ISRPCClientsUncomprsdByteRead_Type()
)
ex2ISRPCClientsUncomprsdByteRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRPCClientsUncomprsdByteRead.setStatus("current")
_Ex2ISRPCClientUncomprsdByteWrite_Type = Gauge32
_Ex2ISRPCClientUncomprsdByteWrite_Object = MibScalar
ex2ISRPCClientUncomprsdByteWrite = _Ex2ISRPCClientUncomprsdByteWrite_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 89),
    _Ex2ISRPCClientUncomprsdByteWrite_Type()
)
ex2ISRPCClientUncomprsdByteWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRPCClientUncomprsdByteWrite.setStatus("current")
_Ex2ISRPCNumOfSlowPackets_Type = Gauge32
_Ex2ISRPCNumOfSlowPackets_Object = MibScalar
ex2ISRPCNumOfSlowPackets = _Ex2ISRPCNumOfSlowPackets_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 90),
    _Ex2ISRPCNumOfSlowPackets_Type()
)
ex2ISRPCNumOfSlowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRPCNumOfSlowPackets.setStatus("current")
_Ex2ISRPCOperationsPerSec_Type = Gauge32
_Ex2ISRPCOperationsPerSec_Object = MibScalar
ex2ISRPCOperationsPerSec = _Ex2ISRPCOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 91),
    _Ex2ISRPCOperationsPerSec_Type()
)
ex2ISRPCOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRPCOperationsPerSec.setStatus("current")
_Ex2ISRPCPacketsPerSec_Type = Gauge32
_Ex2ISRPCPacketsPerSec_Object = MibScalar
ex2ISRPCPacketsPerSec = _Ex2ISRPCPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 92),
    _Ex2ISRPCPacketsPerSec_Type()
)
ex2ISRPCPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRPCPacketsPerSec.setStatus("current")
_Ex2ISRPCRequests_Type = Gauge32
_Ex2ISRPCRequests_Object = MibScalar
ex2ISRPCRequests = _Ex2ISRPCRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 93),
    _Ex2ISRPCRequests_Type()
)
ex2ISRPCRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRPCRequests.setStatus("current")
_Ex2ISRPCRequestsPeak_Type = Gauge32
_Ex2ISRPCRequestsPeak_Object = MibScalar
ex2ISRPCRequestsPeak = _Ex2ISRPCRequestsPeak_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 94),
    _Ex2ISRPCRequestsPeak_Type()
)
ex2ISRPCRequestsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRPCRequestsPeak.setStatus("current")
_Ex2ISReadBytesRPCClientsPerSec_Type = Gauge32
_Ex2ISReadBytesRPCClientsPerSec_Object = MibScalar
ex2ISReadBytesRPCClientsPerSec = _Ex2ISReadBytesRPCClientsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 95),
    _Ex2ISReadBytesRPCClientsPerSec_Type()
)
ex2ISReadBytesRPCClientsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISReadBytesRPCClientsPerSec.setStatus("current")
_Ex2ISRecurringApptmtDeletionRate_Type = Gauge32
_Ex2ISRecurringApptmtDeletionRate_Object = MibScalar
ex2ISRecurringApptmtDeletionRate = _Ex2ISRecurringApptmtDeletionRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 96),
    _Ex2ISRecurringApptmtDeletionRate_Type()
)
ex2ISRecurringApptmtDeletionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRecurringApptmtDeletionRate.setStatus("current")
_Ex2ISRecurApptmtModificationRate_Type = Gauge32
_Ex2ISRecurApptmtModificationRate_Object = MibScalar
ex2ISRecurApptmtModificationRate = _Ex2ISRecurApptmtModificationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 97),
    _Ex2ISRecurApptmtModificationRate_Type()
)
ex2ISRecurApptmtModificationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRecurApptmtModificationRate.setStatus("current")
_Ex2ISRecurringApptmtsCreated_Type = Gauge32
_Ex2ISRecurringApptmtsCreated_Object = MibScalar
ex2ISRecurringApptmtsCreated = _Ex2ISRecurringApptmtsCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 98),
    _Ex2ISRecurringApptmtsCreated_Type()
)
ex2ISRecurringApptmtsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRecurringApptmtsCreated.setStatus("current")
_Ex2ISRecurringApptmtsDeleted_Type = Gauge32
_Ex2ISRecurringApptmtsDeleted_Object = MibScalar
ex2ISRecurringApptmtsDeleted = _Ex2ISRecurringApptmtsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 99),
    _Ex2ISRecurringApptmtsDeleted_Type()
)
ex2ISRecurringApptmtsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRecurringApptmtsDeleted.setStatus("current")
_Ex2ISRecurringApptmtsModified_Type = Gauge32
_Ex2ISRecurringApptmtsModified_Object = MibScalar
ex2ISRecurringApptmtsModified = _Ex2ISRecurringApptmtsModified_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 100),
    _Ex2ISRecurringApptmtsModified_Type()
)
ex2ISRecurringApptmtsModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRecurringApptmtsModified.setStatus("current")
_Ex2ISRecurringApptmtCreationRate_Type = Gauge32
_Ex2ISRecurringApptmtCreationRate_Object = MibScalar
ex2ISRecurringApptmtCreationRate = _Ex2ISRecurringApptmtCreationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 101),
    _Ex2ISRecurringApptmtCreationRate_Type()
)
ex2ISRecurringApptmtCreationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRecurringApptmtCreationRate.setStatus("current")
_Ex2ISRecurringMstrApptmtExpanded_Type = Gauge32
_Ex2ISRecurringMstrApptmtExpanded_Object = MibScalar
ex2ISRecurringMstrApptmtExpanded = _Ex2ISRecurringMstrApptmtExpanded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 102),
    _Ex2ISRecurringMstrApptmtExpanded_Type()
)
ex2ISRecurringMstrApptmtExpanded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRecurringMstrApptmtExpanded.setStatus("current")
_Ex2ISRecurringMasterExpansionRat_Type = Gauge32
_Ex2ISRecurringMasterExpansionRat_Object = MibScalar
ex2ISRecurringMasterExpansionRat = _Ex2ISRecurringMasterExpansionRat_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 103),
    _Ex2ISRecurringMasterExpansionRat_Type()
)
ex2ISRecurringMasterExpansionRat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISRecurringMasterExpansionRat.setStatus("current")
_Ex2ISSingleApptmtCreationRate_Type = Gauge32
_Ex2ISSingleApptmtCreationRate_Object = MibScalar
ex2ISSingleApptmtCreationRate = _Ex2ISSingleApptmtCreationRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 104),
    _Ex2ISSingleApptmtCreationRate_Type()
)
ex2ISSingleApptmtCreationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISSingleApptmtCreationRate.setStatus("current")
_Ex2ISSingleApptmtDeletionRate_Type = Gauge32
_Ex2ISSingleApptmtDeletionRate_Object = MibScalar
ex2ISSingleApptmtDeletionRate = _Ex2ISSingleApptmtDeletionRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 105),
    _Ex2ISSingleApptmtDeletionRate_Type()
)
ex2ISSingleApptmtDeletionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISSingleApptmtDeletionRate.setStatus("current")
_Ex2ISSingleApptmtModificationRat_Type = Gauge32
_Ex2ISSingleApptmtModificationRat_Object = MibScalar
ex2ISSingleApptmtModificationRat = _Ex2ISSingleApptmtModificationRat_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 106),
    _Ex2ISSingleApptmtModificationRat_Type()
)
ex2ISSingleApptmtModificationRat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISSingleApptmtModificationRat.setStatus("current")
_Ex2ISSingleAppointmentsCreated_Type = Gauge32
_Ex2ISSingleAppointmentsCreated_Object = MibScalar
ex2ISSingleAppointmentsCreated = _Ex2ISSingleAppointmentsCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 107),
    _Ex2ISSingleAppointmentsCreated_Type()
)
ex2ISSingleAppointmentsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISSingleAppointmentsCreated.setStatus("current")
_Ex2ISSingleAppointmentsDeleted_Type = Gauge32
_Ex2ISSingleAppointmentsDeleted_Object = MibScalar
ex2ISSingleAppointmentsDeleted = _Ex2ISSingleAppointmentsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 108),
    _Ex2ISSingleAppointmentsDeleted_Type()
)
ex2ISSingleAppointmentsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISSingleAppointmentsDeleted.setStatus("current")
_Ex2ISSingleAppointmentsModified_Type = Gauge32
_Ex2ISSingleAppointmentsModified_Object = MibScalar
ex2ISSingleAppointmentsModified = _Ex2ISSingleAppointmentsModified_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 109),
    _Ex2ISSingleAppointmentsModified_Type()
)
ex2ISSingleAppointmentsModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISSingleAppointmentsModified.setStatus("current")
_Ex2ISSlowQPThreads_Type = Gauge32
_Ex2ISSlowQPThreads_Object = MibScalar
ex2ISSlowQPThreads = _Ex2ISSlowQPThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 110),
    _Ex2ISSlowQPThreads_Type()
)
ex2ISSlowQPThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISSlowQPThreads.setStatus("current")
_Ex2ISSlowSearchThreads_Type = Gauge32
_Ex2ISSlowSearchThreads_Object = MibScalar
ex2ISSlowSearchThreads = _Ex2ISSlowSearchThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 111),
    _Ex2ISSlowSearchThreads_Type()
)
ex2ISSlowSearchThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISSlowSearchThreads.setStatus("current")
_Ex2ISTotalParkedAsyncNotifiCalls_Type = Gauge32
_Ex2ISTotalParkedAsyncNotifiCalls_Object = MibScalar
ex2ISTotalParkedAsyncNotifiCalls = _Ex2ISTotalParkedAsyncNotifiCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 112),
    _Ex2ISTotalParkedAsyncNotifiCalls_Type()
)
ex2ISTotalParkedAsyncNotifiCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISTotalParkedAsyncNotifiCalls.setStatus("current")
_Ex2ISUserCount_Type = Gauge32
_Ex2ISUserCount_Object = MibScalar
ex2ISUserCount = _Ex2ISUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 113),
    _Ex2ISUserCount_Type()
)
ex2ISUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISUserCount.setStatus("current")
_Ex2ISVMLargestBlockSize_Type = Gauge32
_Ex2ISVMLargestBlockSize_Object = MibScalar
ex2ISVMLargestBlockSize = _Ex2ISVMLargestBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 114),
    _Ex2ISVMLargestBlockSize_Type()
)
ex2ISVMLargestBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVMLargestBlockSize.setStatus("current")
_Ex2ISVMTotal16MBFreeBlocks_Type = Gauge32
_Ex2ISVMTotal16MBFreeBlocks_Object = MibScalar
ex2ISVMTotal16MBFreeBlocks = _Ex2ISVMTotal16MBFreeBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 115),
    _Ex2ISVMTotal16MBFreeBlocks_Type()
)
ex2ISVMTotal16MBFreeBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVMTotal16MBFreeBlocks.setStatus("current")
_Ex2ISVMTotalFreeBlocks_Type = Gauge32
_Ex2ISVMTotalFreeBlocks_Object = MibScalar
ex2ISVMTotalFreeBlocks = _Ex2ISVMTotalFreeBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 116),
    _Ex2ISVMTotalFreeBlocks_Type()
)
ex2ISVMTotalFreeBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVMTotalFreeBlocks.setStatus("current")
_Ex2ISVMTotalLargeFreeBlockBytes_Type = Gauge32
_Ex2ISVMTotalLargeFreeBlockBytes_Object = MibScalar
ex2ISVMTotalLargeFreeBlockBytes = _Ex2ISVMTotalLargeFreeBlockBytes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 117),
    _Ex2ISVMTotalLargeFreeBlockBytes_Type()
)
ex2ISVMTotalLargeFreeBlockBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVMTotalLargeFreeBlockBytes.setStatus("current")
_Ex2ISVirusScanBytesScanned_Type = Gauge32
_Ex2ISVirusScanBytesScanned_Object = MibScalar
ex2ISVirusScanBytesScanned = _Ex2ISVirusScanBytesScanned_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 118),
    _Ex2ISVirusScanBytesScanned_Type()
)
ex2ISVirusScanBytesScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanBytesScanned.setStatus("current")
_Ex2ISVirusScanFilesCleaned_Type = Gauge32
_Ex2ISVirusScanFilesCleaned_Object = MibScalar
ex2ISVirusScanFilesCleaned = _Ex2ISVirusScanFilesCleaned_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 119),
    _Ex2ISVirusScanFilesCleaned_Type()
)
ex2ISVirusScanFilesCleaned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanFilesCleaned.setStatus("current")
_Ex2ISVirusScanFilesCleanedPerSec_Type = Gauge32
_Ex2ISVirusScanFilesCleanedPerSec_Object = MibScalar
ex2ISVirusScanFilesCleanedPerSec = _Ex2ISVirusScanFilesCleanedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 120),
    _Ex2ISVirusScanFilesCleanedPerSec_Type()
)
ex2ISVirusScanFilesCleanedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanFilesCleanedPerSec.setStatus("current")
_Ex2ISVirusScanFilesQuarantined_Type = Gauge32
_Ex2ISVirusScanFilesQuarantined_Object = MibScalar
ex2ISVirusScanFilesQuarantined = _Ex2ISVirusScanFilesQuarantined_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 121),
    _Ex2ISVirusScanFilesQuarantined_Type()
)
ex2ISVirusScanFilesQuarantined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanFilesQuarantined.setStatus("current")
_Ex2ISVirusScanFileQuarantinePSec_Type = Gauge32
_Ex2ISVirusScanFileQuarantinePSec_Object = MibScalar
ex2ISVirusScanFileQuarantinePSec = _Ex2ISVirusScanFileQuarantinePSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 122),
    _Ex2ISVirusScanFileQuarantinePSec_Type()
)
ex2ISVirusScanFileQuarantinePSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanFileQuarantinePSec.setStatus("current")
_Ex2ISVirusScanFilesScanned_Type = Gauge32
_Ex2ISVirusScanFilesScanned_Object = MibScalar
ex2ISVirusScanFilesScanned = _Ex2ISVirusScanFilesScanned_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 123),
    _Ex2ISVirusScanFilesScanned_Type()
)
ex2ISVirusScanFilesScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanFilesScanned.setStatus("current")
_Ex2ISVirusScanFilesScannedPerSec_Type = Gauge32
_Ex2ISVirusScanFilesScannedPerSec_Object = MibScalar
ex2ISVirusScanFilesScannedPerSec = _Ex2ISVirusScanFilesScannedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 124),
    _Ex2ISVirusScanFilesScannedPerSec_Type()
)
ex2ISVirusScanFilesScannedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanFilesScannedPerSec.setStatus("current")
_Ex2ISVirusScanFoldersScannedInBg_Type = Gauge32
_Ex2ISVirusScanFoldersScannedInBg_Object = MibScalar
ex2ISVirusScanFoldersScannedInBg = _Ex2ISVirusScanFoldersScannedInBg_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 125),
    _Ex2ISVirusScanFoldersScannedInBg_Type()
)
ex2ISVirusScanFoldersScannedInBg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanFoldersScannedInBg.setStatus("current")
_Ex2ISVirusScanMessagesCleaned_Type = Gauge32
_Ex2ISVirusScanMessagesCleaned_Object = MibScalar
ex2ISVirusScanMessagesCleaned = _Ex2ISVirusScanMessagesCleaned_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 126),
    _Ex2ISVirusScanMessagesCleaned_Type()
)
ex2ISVirusScanMessagesCleaned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanMessagesCleaned.setStatus("current")
_Ex2ISVirusScanMsgsCleanedPerSec_Type = Gauge32
_Ex2ISVirusScanMsgsCleanedPerSec_Object = MibScalar
ex2ISVirusScanMsgsCleanedPerSec = _Ex2ISVirusScanMsgsCleanedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 127),
    _Ex2ISVirusScanMsgsCleanedPerSec_Type()
)
ex2ISVirusScanMsgsCleanedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanMsgsCleanedPerSec.setStatus("current")
_Ex2ISVirusScanMessagesDeleted_Type = Gauge32
_Ex2ISVirusScanMessagesDeleted_Object = MibScalar
ex2ISVirusScanMessagesDeleted = _Ex2ISVirusScanMessagesDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 128),
    _Ex2ISVirusScanMessagesDeleted_Type()
)
ex2ISVirusScanMessagesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanMessagesDeleted.setStatus("current")
_Ex2ISVirusScanMsgsDeletedPerSec_Type = Gauge32
_Ex2ISVirusScanMsgsDeletedPerSec_Object = MibScalar
ex2ISVirusScanMsgsDeletedPerSec = _Ex2ISVirusScanMsgsDeletedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 129),
    _Ex2ISVirusScanMsgsDeletedPerSec_Type()
)
ex2ISVirusScanMsgsDeletedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanMsgsDeletedPerSec.setStatus("current")
_Ex2ISVirusScanMessagesProcessed_Type = Gauge32
_Ex2ISVirusScanMessagesProcessed_Object = MibScalar
ex2ISVirusScanMessagesProcessed = _Ex2ISVirusScanMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 130),
    _Ex2ISVirusScanMessagesProcessed_Type()
)
ex2ISVirusScanMessagesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanMessagesProcessed.setStatus("current")
_Ex2ISVirusScanMsgProcessedPerSec_Type = Gauge32
_Ex2ISVirusScanMsgProcessedPerSec_Object = MibScalar
ex2ISVirusScanMsgProcessedPerSec = _Ex2ISVirusScanMsgProcessedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 131),
    _Ex2ISVirusScanMsgProcessedPerSec_Type()
)
ex2ISVirusScanMsgProcessedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanMsgProcessedPerSec.setStatus("current")
_Ex2ISVirusScanMsgsQuarantined_Type = Gauge32
_Ex2ISVirusScanMsgsQuarantined_Object = MibScalar
ex2ISVirusScanMsgsQuarantined = _Ex2ISVirusScanMsgsQuarantined_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 132),
    _Ex2ISVirusScanMsgsQuarantined_Type()
)
ex2ISVirusScanMsgsQuarantined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanMsgsQuarantined.setStatus("current")
_Ex2ISVirusScanMsgQuarantinPerSec_Type = Gauge32
_Ex2ISVirusScanMsgQuarantinPerSec_Object = MibScalar
ex2ISVirusScanMsgQuarantinPerSec = _Ex2ISVirusScanMsgQuarantinPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 133),
    _Ex2ISVirusScanMsgQuarantinPerSec_Type()
)
ex2ISVirusScanMsgQuarantinPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanMsgQuarantinPerSec.setStatus("current")
_Ex2ISVirusScanMsgsScanBackground_Type = Gauge32
_Ex2ISVirusScanMsgsScanBackground_Object = MibScalar
ex2ISVirusScanMsgsScanBackground = _Ex2ISVirusScanMsgsScanBackground_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 134),
    _Ex2ISVirusScanMsgsScanBackground_Type()
)
ex2ISVirusScanMsgsScanBackground.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanMsgsScanBackground.setStatus("current")
_Ex2ISVirusScanQueueLength_Type = Gauge32
_Ex2ISVirusScanQueueLength_Object = MibScalar
ex2ISVirusScanQueueLength = _Ex2ISVirusScanQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 135),
    _Ex2ISVirusScanQueueLength_Type()
)
ex2ISVirusScanQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISVirusScanQueueLength.setStatus("current")
_Ex2ISWriteBytesRPCClientsPerSec_Type = Gauge32
_Ex2ISWriteBytesRPCClientsPerSec_Object = MibScalar
ex2ISWriteBytesRPCClientsPerSec = _Ex2ISWriteBytesRPCClientsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 45, 136),
    _Ex2ISWriteBytesRPCClientsPerSec_Type()
)
ex2ISWriteBytesRPCClientsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISWriteBytesRPCClientsPerSec.setStatus("current")
_Ex2ISClientTable_Object = MibTable
ex2ISClientTable = _Ex2ISClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46)
)
if mibBuilder.loadTexts:
    ex2ISClientTable.setStatus("current")
_Ex2ISClientEntry_Object = MibTableRow
ex2ISClientEntry = _Ex2ISClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1)
)
ex2ISClientEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2ISCInstance"),
)
if mibBuilder.loadTexts:
    ex2ISClientEntry.setStatus("current")
_Ex2ISCInstance_Type = InstanceName
_Ex2ISCInstance_Object = MibTableColumn
ex2ISCInstance = _Ex2ISCInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 1),
    _Ex2ISCInstance_Type()
)
ex2ISCInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCInstance.setStatus("current")
_Ex2ISCDirAccCacheEntryAddPerSec_Type = Gauge32
_Ex2ISCDirAccCacheEntryAddPerSec_Object = MibTableColumn
ex2ISCDirAccCacheEntryAddPerSec = _Ex2ISCDirAccCacheEntryAddPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 2),
    _Ex2ISCDirAccCacheEntryAddPerSec_Type()
)
ex2ISCDirAccCacheEntryAddPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCDirAccCacheEntryAddPerSec.setStatus("current")
_Ex2ISCDirAccCacheEntryExpiredSec_Type = Gauge32
_Ex2ISCDirAccCacheEntryExpiredSec_Object = MibTableColumn
ex2ISCDirAccCacheEntryExpiredSec = _Ex2ISCDirAccCacheEntryExpiredSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 3),
    _Ex2ISCDirAccCacheEntryExpiredSec_Type()
)
ex2ISCDirAccCacheEntryExpiredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCDirAccCacheEntryExpiredSec.setStatus("current")
_Ex2ISCDirAccCacheHitsPercent_Type = Gauge32
_Ex2ISCDirAccCacheHitsPercent_Object = MibTableColumn
ex2ISCDirAccCacheHitsPercent = _Ex2ISCDirAccCacheHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 4),
    _Ex2ISCDirAccCacheHitsPercent_Type()
)
ex2ISCDirAccCacheHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCDirAccCacheHitsPercent.setStatus("current")
_Ex2ISCDirAccLDAPReadsPerSec_Type = Gauge32
_Ex2ISCDirAccLDAPReadsPerSec_Object = MibTableColumn
ex2ISCDirAccLDAPReadsPerSec = _Ex2ISCDirAccLDAPReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 5),
    _Ex2ISCDirAccLDAPReadsPerSec_Type()
)
ex2ISCDirAccLDAPReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCDirAccLDAPReadsPerSec.setStatus("current")
_Ex2ISCDirAccLDAPSearchesPerSec_Type = Gauge32
_Ex2ISCDirAccLDAPSearchesPerSec_Object = MibTableColumn
ex2ISCDirAccLDAPSearchesPerSec = _Ex2ISCDirAccLDAPSearchesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 6),
    _Ex2ISCDirAccLDAPSearchesPerSec_Type()
)
ex2ISCDirAccLDAPSearchesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCDirAccLDAPSearchesPerSec.setStatus("current")
_Ex2ISCJETLogRecordBytesPerSec_Type = Gauge32
_Ex2ISCJETLogRecordBytesPerSec_Object = MibTableColumn
ex2ISCJETLogRecordBytesPerSec = _Ex2ISCJETLogRecordBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 7),
    _Ex2ISCJETLogRecordBytesPerSec_Type()
)
ex2ISCJETLogRecordBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCJETLogRecordBytesPerSec.setStatus("current")
_Ex2ISCJETLogRecordsPerSec_Type = Gauge32
_Ex2ISCJETLogRecordsPerSec_Object = MibTableColumn
ex2ISCJETLogRecordsPerSec = _Ex2ISCJETLogRecordsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 8),
    _Ex2ISCJETLogRecordsPerSec_Type()
)
ex2ISCJETLogRecordsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCJETLogRecordsPerSec.setStatus("current")
_Ex2ISCJETPagesModifiedPerSec_Type = Gauge32
_Ex2ISCJETPagesModifiedPerSec_Object = MibTableColumn
ex2ISCJETPagesModifiedPerSec = _Ex2ISCJETPagesModifiedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 9),
    _Ex2ISCJETPagesModifiedPerSec_Type()
)
ex2ISCJETPagesModifiedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCJETPagesModifiedPerSec.setStatus("current")
_Ex2ISCJETPagesPrereadPerSec_Type = Gauge32
_Ex2ISCJETPagesPrereadPerSec_Object = MibTableColumn
ex2ISCJETPagesPrereadPerSec = _Ex2ISCJETPagesPrereadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 10),
    _Ex2ISCJETPagesPrereadPerSec_Type()
)
ex2ISCJETPagesPrereadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCJETPagesPrereadPerSec.setStatus("current")
_Ex2ISCJETPagesReadPerSec_Type = Gauge32
_Ex2ISCJETPagesReadPerSec_Object = MibTableColumn
ex2ISCJETPagesReadPerSec = _Ex2ISCJETPagesReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 11),
    _Ex2ISCJETPagesReadPerSec_Type()
)
ex2ISCJETPagesReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCJETPagesReadPerSec.setStatus("current")
_Ex2ISCJETPagesReferencedPerSec_Type = Gauge32
_Ex2ISCJETPagesReferencedPerSec_Object = MibTableColumn
ex2ISCJETPagesReferencedPerSec = _Ex2ISCJETPagesReferencedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 12),
    _Ex2ISCJETPagesReferencedPerSec_Type()
)
ex2ISCJETPagesReferencedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCJETPagesReferencedPerSec.setStatus("current")
_Ex2ISCJETPagesRemodifiedPerSec_Type = Gauge32
_Ex2ISCJETPagesRemodifiedPerSec_Object = MibTableColumn
ex2ISCJETPagesRemodifiedPerSec = _Ex2ISCJETPagesRemodifiedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 13),
    _Ex2ISCJETPagesRemodifiedPerSec_Type()
)
ex2ISCJETPagesRemodifiedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCJETPagesRemodifiedPerSec.setStatus("current")
_Ex2ISCRPCAverageLatency_Type = Gauge32
_Ex2ISCRPCAverageLatency_Object = MibTableColumn
ex2ISCRPCAverageLatency = _Ex2ISCRPCAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 14),
    _Ex2ISCRPCAverageLatency_Type()
)
ex2ISCRPCAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCRPCAverageLatency.setStatus("current")
_Ex2ISCRPCBytesReceivedPerSec_Type = Gauge32
_Ex2ISCRPCBytesReceivedPerSec_Object = MibTableColumn
ex2ISCRPCBytesReceivedPerSec = _Ex2ISCRPCBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 15),
    _Ex2ISCRPCBytesReceivedPerSec_Type()
)
ex2ISCRPCBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCRPCBytesReceivedPerSec.setStatus("current")
_Ex2ISCRPCBytesSentPerSec_Type = Gauge32
_Ex2ISCRPCBytesSentPerSec_Object = MibTableColumn
ex2ISCRPCBytesSentPerSec = _Ex2ISCRPCBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 16),
    _Ex2ISCRPCBytesSentPerSec_Type()
)
ex2ISCRPCBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCRPCBytesSentPerSec.setStatus("current")
_Ex2ISCRPCOperationsPerSec_Type = Gauge32
_Ex2ISCRPCOperationsPerSec_Object = MibTableColumn
ex2ISCRPCOperationsPerSec = _Ex2ISCRPCOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 17),
    _Ex2ISCRPCOperationsPerSec_Type()
)
ex2ISCRPCOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCRPCOperationsPerSec.setStatus("current")
_Ex2ISCRPCPacketsPerSec_Type = Gauge32
_Ex2ISCRPCPacketsPerSec_Object = MibTableColumn
ex2ISCRPCPacketsPerSec = _Ex2ISCRPCPacketsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 46, 1, 18),
    _Ex2ISCRPCPacketsPerSec_Type()
)
ex2ISCRPCPacketsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ISCRPCPacketsPerSec.setStatus("current")
_Ex2ISMailboxTable_Object = MibTable
ex2ISMailboxTable = _Ex2ISMailboxTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47)
)
if mibBuilder.loadTexts:
    ex2ISMailboxTable.setStatus("current")
_Ex2ISMailboxEntry_Object = MibTableRow
ex2ISMailboxEntry = _Ex2ISMailboxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1)
)
ex2ISMailboxEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2mbInstance"),
)
if mibBuilder.loadTexts:
    ex2ISMailboxEntry.setStatus("current")
_Ex2mbInstance_Type = InstanceName
_Ex2mbInstance_Object = MibTableColumn
ex2mbInstance = _Ex2mbInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 1),
    _Ex2mbInstance_Type()
)
ex2mbInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbInstance.setStatus("current")
_Ex2mbActiveClientLogons_Type = Gauge32
_Ex2mbActiveClientLogons_Object = MibTableColumn
ex2mbActiveClientLogons = _Ex2mbActiveClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 2),
    _Ex2mbActiveClientLogons_Type()
)
ex2mbActiveClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbActiveClientLogons.setStatus("current")
_Ex2mbAverageDeliveryTime_Type = Gauge32
_Ex2mbAverageDeliveryTime_Object = MibTableColumn
ex2mbAverageDeliveryTime = _Ex2mbAverageDeliveryTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 3),
    _Ex2mbAverageDeliveryTime_Type()
)
ex2mbAverageDeliveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbAverageDeliveryTime.setStatus("current")
_Ex2mbCategorizationCount_Type = Gauge32
_Ex2mbCategorizationCount_Object = MibTableColumn
ex2mbCategorizationCount = _Ex2mbCategorizationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 4),
    _Ex2mbCategorizationCount_Type()
)
ex2mbCategorizationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbCategorizationCount.setStatus("current")
_Ex2mbClientLogons_Type = Gauge32
_Ex2mbClientLogons_Object = MibTableColumn
ex2mbClientLogons = _Ex2mbClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 5),
    _Ex2mbClientLogons_Type()
)
ex2mbClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbClientLogons.setStatus("current")
_Ex2mbEventHistoryDeletes_Type = Gauge32
_Ex2mbEventHistoryDeletes_Object = MibTableColumn
ex2mbEventHistoryDeletes = _Ex2mbEventHistoryDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 6),
    _Ex2mbEventHistoryDeletes_Type()
)
ex2mbEventHistoryDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistoryDeletes.setStatus("current")
_Ex2mbEventHistoryDeletesPerSec_Type = Gauge32
_Ex2mbEventHistoryDeletesPerSec_Object = MibTableColumn
ex2mbEventHistoryDeletesPerSec = _Ex2mbEventHistoryDeletesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 7),
    _Ex2mbEventHistoryDeletesPerSec_Type()
)
ex2mbEventHistoryDeletesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistoryDeletesPerSec.setStatus("current")
_Ex2mbEventHistEventCacheHitsPerc_Type = Gauge32
_Ex2mbEventHistEventCacheHitsPerc_Object = MibTableColumn
ex2mbEventHistEventCacheHitsPerc = _Ex2mbEventHistEventCacheHitsPerc_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 8),
    _Ex2mbEventHistEventCacheHitsPerc_Type()
)
ex2mbEventHistEventCacheHitsPerc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistEventCacheHitsPerc.setStatus("current")
_Ex2mbEventHistoryEventsCount_Type = Gauge32
_Ex2mbEventHistoryEventsCount_Object = MibTableColumn
ex2mbEventHistoryEventsCount = _Ex2mbEventHistoryEventsCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 9),
    _Ex2mbEventHistoryEventsCount_Type()
)
ex2mbEventHistoryEventsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistoryEventsCount.setStatus("current")
_Ex2mbEventHistEventEmptyConClass_Type = Gauge32
_Ex2mbEventHistEventEmptyConClass_Object = MibTableColumn
ex2mbEventHistEventEmptyConClass = _Ex2mbEventHistEventEmptyConClass_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 10),
    _Ex2mbEventHistEventEmptyConClass_Type()
)
ex2mbEventHistEventEmptyConClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistEventEmptyConClass.setStatus("current")
_Ex2mbEventHistEventEmptyMsgClass_Type = Gauge32
_Ex2mbEventHistEventEmptyMsgClass_Object = MibTableColumn
ex2mbEventHistEventEmptyMsgClass = _Ex2mbEventHistEventEmptyMsgClass_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 11),
    _Ex2mbEventHistEventEmptyMsgClass_Type()
)
ex2mbEventHistEventEmptyMsgClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistEventEmptyMsgClass.setStatus("current")
_Ex2mbEventHistEventsTrunConClass_Type = Gauge32
_Ex2mbEventHistEventsTrunConClass_Object = MibTableColumn
ex2mbEventHistEventsTrunConClass = _Ex2mbEventHistEventsTrunConClass_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 12),
    _Ex2mbEventHistEventsTrunConClass_Type()
)
ex2mbEventHistEventsTrunConClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistEventsTrunConClass.setStatus("current")
_Ex2mbEventHistEventsTrunMsgClass_Type = Gauge32
_Ex2mbEventHistEventsTrunMsgClass_Object = MibTableColumn
ex2mbEventHistEventsTrunMsgClass = _Ex2mbEventHistEventsTrunMsgClass_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 13),
    _Ex2mbEventHistEventsTrunMsgClass_Type()
)
ex2mbEventHistEventsTrunMsgClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistEventsTrunMsgClass.setStatus("current")
_Ex2mbEventHistoryReads_Type = Gauge32
_Ex2mbEventHistoryReads_Object = MibTableColumn
ex2mbEventHistoryReads = _Ex2mbEventHistoryReads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 14),
    _Ex2mbEventHistoryReads_Type()
)
ex2mbEventHistoryReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistoryReads.setStatus("current")
_Ex2mbEventHistoryReadsPerSec_Type = Gauge32
_Ex2mbEventHistoryReadsPerSec_Object = MibTableColumn
ex2mbEventHistoryReadsPerSec = _Ex2mbEventHistoryReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 15),
    _Ex2mbEventHistoryReadsPerSec_Type()
)
ex2mbEventHistoryReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistoryReadsPerSec.setStatus("current")
_Ex2mbEventHistUncommitTransCount_Type = Gauge32
_Ex2mbEventHistUncommitTransCount_Object = MibTableColumn
ex2mbEventHistUncommitTransCount = _Ex2mbEventHistUncommitTransCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 16),
    _Ex2mbEventHistUncommitTransCount_Type()
)
ex2mbEventHistUncommitTransCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistUncommitTransCount.setStatus("current")
_Ex2mbEventHistoryWatermarksCount_Type = Gauge32
_Ex2mbEventHistoryWatermarksCount_Object = MibTableColumn
ex2mbEventHistoryWatermarksCount = _Ex2mbEventHistoryWatermarksCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 17),
    _Ex2mbEventHistoryWatermarksCount_Type()
)
ex2mbEventHistoryWatermarksCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistoryWatermarksCount.setStatus("current")
_Ex2mbEventHistWatermarksDeletes_Type = Gauge32
_Ex2mbEventHistWatermarksDeletes_Object = MibTableColumn
ex2mbEventHistWatermarksDeletes = _Ex2mbEventHistWatermarksDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 18),
    _Ex2mbEventHistWatermarksDeletes_Type()
)
ex2mbEventHistWatermarksDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistWatermarksDeletes.setStatus("current")
_Ex2mbEventHistWatermarkDelPerSec_Type = Gauge32
_Ex2mbEventHistWatermarkDelPerSec_Object = MibTableColumn
ex2mbEventHistWatermarkDelPerSec = _Ex2mbEventHistWatermarkDelPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 19),
    _Ex2mbEventHistWatermarkDelPerSec_Type()
)
ex2mbEventHistWatermarkDelPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistWatermarkDelPerSec.setStatus("current")
_Ex2mbEventHistoryWatermarksReads_Type = Gauge32
_Ex2mbEventHistoryWatermarksReads_Object = MibTableColumn
ex2mbEventHistoryWatermarksReads = _Ex2mbEventHistoryWatermarksReads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 20),
    _Ex2mbEventHistoryWatermarksReads_Type()
)
ex2mbEventHistoryWatermarksReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistoryWatermarksReads.setStatus("current")
_Ex2mbEventHistWatermarkReadPrSec_Type = Gauge32
_Ex2mbEventHistWatermarkReadPrSec_Object = MibTableColumn
ex2mbEventHistWatermarkReadPrSec = _Ex2mbEventHistWatermarkReadPrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 21),
    _Ex2mbEventHistWatermarkReadPrSec_Type()
)
ex2mbEventHistWatermarkReadPrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistWatermarkReadPrSec.setStatus("current")
_Ex2mbEventHistWatermarksWrites_Type = Gauge32
_Ex2mbEventHistWatermarksWrites_Object = MibTableColumn
ex2mbEventHistWatermarksWrites = _Ex2mbEventHistWatermarksWrites_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 22),
    _Ex2mbEventHistWatermarksWrites_Type()
)
ex2mbEventHistWatermarksWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistWatermarksWrites.setStatus("current")
_Ex2mbEventHistWatermarkWritPrSec_Type = Gauge32
_Ex2mbEventHistWatermarkWritPrSec_Object = MibTableColumn
ex2mbEventHistWatermarkWritPrSec = _Ex2mbEventHistWatermarkWritPrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 23),
    _Ex2mbEventHistWatermarkWritPrSec_Type()
)
ex2mbEventHistWatermarkWritPrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistWatermarkWritPrSec.setStatus("current")
_Ex2mbEventHistoryWrites_Type = Gauge32
_Ex2mbEventHistoryWrites_Object = MibTableColumn
ex2mbEventHistoryWrites = _Ex2mbEventHistoryWrites_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 24),
    _Ex2mbEventHistoryWrites_Type()
)
ex2mbEventHistoryWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistoryWrites.setStatus("current")
_Ex2mbEventHistoryWritesPerSec_Type = Gauge32
_Ex2mbEventHistoryWritesPerSec_Object = MibTableColumn
ex2mbEventHistoryWritesPerSec = _Ex2mbEventHistoryWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 25),
    _Ex2mbEventHistoryWritesPerSec_Type()
)
ex2mbEventHistoryWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbEventHistoryWritesPerSec.setStatus("current")
_Ex2mbFolderOpensPerSec_Type = Gauge32
_Ex2mbFolderOpensPerSec_Object = MibTableColumn
ex2mbFolderOpensPerSec = _Ex2mbFolderOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 26),
    _Ex2mbFolderOpensPerSec_Type()
)
ex2mbFolderOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbFolderOpensPerSec.setStatus("current")
_Ex2mbHTTPPerDAVCurrentPendNotif_Type = Gauge32
_Ex2mbHTTPPerDAVCurrentPendNotif_Object = MibTableColumn
ex2mbHTTPPerDAVCurrentPendNotif = _Ex2mbHTTPPerDAVCurrentPendNotif_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 27),
    _Ex2mbHTTPPerDAVCurrentPendNotif_Type()
)
ex2mbHTTPPerDAVCurrentPendNotif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbHTTPPerDAVCurrentPendNotif.setStatus("current")
_Ex2mbHTTPPerDAVCurrentSubscript_Type = Gauge32
_Ex2mbHTTPPerDAVCurrentSubscript_Object = MibTableColumn
ex2mbHTTPPerDAVCurrentSubscript = _Ex2mbHTTPPerDAVCurrentSubscript_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 28),
    _Ex2mbHTTPPerDAVCurrentSubscript_Type()
)
ex2mbHTTPPerDAVCurrentSubscript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbHTTPPerDAVCurrentSubscript.setStatus("current")
_Ex2mbHTTPPerDAVCurrentTransLocks_Type = Gauge32
_Ex2mbHTTPPerDAVCurrentTransLocks_Object = MibTableColumn
ex2mbHTTPPerDAVCurrentTransLocks = _Ex2mbHTTPPerDAVCurrentTransLocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 29),
    _Ex2mbHTTPPerDAVCurrentTransLocks_Type()
)
ex2mbHTTPPerDAVCurrentTransLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbHTTPPerDAVCurrentTransLocks.setStatus("current")
_Ex2mbHTTPPerDAVNotifyRequestPSec_Type = Gauge32
_Ex2mbHTTPPerDAVNotifyRequestPSec_Object = MibTableColumn
ex2mbHTTPPerDAVNotifyRequestPSec = _Ex2mbHTTPPerDAVNotifyRequestPSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 30),
    _Ex2mbHTTPPerDAVNotifyRequestPSec_Type()
)
ex2mbHTTPPerDAVNotifyRequestPSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbHTTPPerDAVNotifyRequestPSec.setStatus("current")
_Ex2mbHTTPPerDAVTotalLocksCreated_Type = Gauge32
_Ex2mbHTTPPerDAVTotalLocksCreated_Object = MibTableColumn
ex2mbHTTPPerDAVTotalLocksCreated = _Ex2mbHTTPPerDAVTotalLocksCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 31),
    _Ex2mbHTTPPerDAVTotalLocksCreated_Type()
)
ex2mbHTTPPerDAVTotalLocksCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbHTTPPerDAVTotalLocksCreated.setStatus("current")
_Ex2mbHTTPPerDAVTotalNotifyRequst_Type = Gauge32
_Ex2mbHTTPPerDAVTotalNotifyRequst_Object = MibTableColumn
ex2mbHTTPPerDAVTotalNotifyRequst = _Ex2mbHTTPPerDAVTotalNotifyRequst_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 32),
    _Ex2mbHTTPPerDAVTotalNotifyRequst_Type()
)
ex2mbHTTPPerDAVTotalNotifyRequst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbHTTPPerDAVTotalNotifyRequst.setStatus("current")
_Ex2mbHTTPPerDAVTotalSubscCreated_Type = Gauge32
_Ex2mbHTTPPerDAVTotalSubscCreated_Object = MibTableColumn
ex2mbHTTPPerDAVTotalSubscCreated = _Ex2mbHTTPPerDAVTotalSubscCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 33),
    _Ex2mbHTTPPerDAVTotalSubscCreated_Type()
)
ex2mbHTTPPerDAVTotalSubscCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbHTTPPerDAVTotalSubscCreated.setStatus("current")
_Ex2mbHTTPPerDAVTotalSubscExpired_Type = Gauge32
_Ex2mbHTTPPerDAVTotalSubscExpired_Object = MibTableColumn
ex2mbHTTPPerDAVTotalSubscExpired = _Ex2mbHTTPPerDAVTotalSubscExpired_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 34),
    _Ex2mbHTTPPerDAVTotalSubscExpired_Type()
)
ex2mbHTTPPerDAVTotalSubscExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbHTTPPerDAVTotalSubscExpired.setStatus("current")
_Ex2mbLocalDeliveries_Type = Gauge32
_Ex2mbLocalDeliveries_Object = MibTableColumn
ex2mbLocalDeliveries = _Ex2mbLocalDeliveries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 35),
    _Ex2mbLocalDeliveries_Type()
)
ex2mbLocalDeliveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbLocalDeliveries.setStatus("current")
_Ex2mbLocalDeliveryRate_Type = Gauge32
_Ex2mbLocalDeliveryRate_Object = MibTableColumn
ex2mbLocalDeliveryRate = _Ex2mbLocalDeliveryRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 36),
    _Ex2mbLocalDeliveryRate_Type()
)
ex2mbLocalDeliveryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbLocalDeliveryRate.setStatus("current")
_Ex2mbLogonOperationsPerSec_Type = Gauge32
_Ex2mbLogonOperationsPerSec_Object = MibTableColumn
ex2mbLogonOperationsPerSec = _Ex2mbLogonOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 37),
    _Ex2mbLogonOperationsPerSec_Type()
)
ex2mbLogonOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbLogonOperationsPerSec.setStatus("current")
_Ex2mbMessageOpensPerSec_Type = Gauge32
_Ex2mbMessageOpensPerSec_Object = MibTableColumn
ex2mbMessageOpensPerSec = _Ex2mbMessageOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 38),
    _Ex2mbMessageOpensPerSec_Type()
)
ex2mbMessageOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbMessageOpensPerSec.setStatus("current")
_Ex2mbMessageRecipientsDelivered_Type = Gauge32
_Ex2mbMessageRecipientsDelivered_Object = MibTableColumn
ex2mbMessageRecipientsDelivered = _Ex2mbMessageRecipientsDelivered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 39),
    _Ex2mbMessageRecipientsDelivered_Type()
)
ex2mbMessageRecipientsDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbMessageRecipientsDelivered.setStatus("current")
_Ex2mbMessageRecipientDelivPerSec_Type = Gauge32
_Ex2mbMessageRecipientDelivPerSec_Object = MibTableColumn
ex2mbMessageRecipientDelivPerSec = _Ex2mbMessageRecipientDelivPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 40),
    _Ex2mbMessageRecipientDelivPerSec_Type()
)
ex2mbMessageRecipientDelivPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbMessageRecipientDelivPerSec.setStatus("current")
_Ex2mbMessagesDelivered_Type = Gauge32
_Ex2mbMessagesDelivered_Object = MibTableColumn
ex2mbMessagesDelivered = _Ex2mbMessagesDelivered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 41),
    _Ex2mbMessagesDelivered_Type()
)
ex2mbMessagesDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbMessagesDelivered.setStatus("current")
_Ex2mbMessagesDeliveredPerSec_Type = Gauge32
_Ex2mbMessagesDeliveredPerSec_Object = MibTableColumn
ex2mbMessagesDeliveredPerSec = _Ex2mbMessagesDeliveredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 42),
    _Ex2mbMessagesDeliveredPerSec_Type()
)
ex2mbMessagesDeliveredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbMessagesDeliveredPerSec.setStatus("current")
_Ex2mbMessagesQueuedForSubmission_Type = Gauge32
_Ex2mbMessagesQueuedForSubmission_Object = MibTableColumn
ex2mbMessagesQueuedForSubmission = _Ex2mbMessagesQueuedForSubmission_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 43),
    _Ex2mbMessagesQueuedForSubmission_Type()
)
ex2mbMessagesQueuedForSubmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbMessagesQueuedForSubmission.setStatus("current")
_Ex2mbMessagesSent_Type = Gauge32
_Ex2mbMessagesSent_Object = MibTableColumn
ex2mbMessagesSent = _Ex2mbMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 44),
    _Ex2mbMessagesSent_Type()
)
ex2mbMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbMessagesSent.setStatus("current")
_Ex2mbMessagesSentPerSec_Type = Gauge32
_Ex2mbMessagesSentPerSec_Object = MibTableColumn
ex2mbMessagesSentPerSec = _Ex2mbMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 45),
    _Ex2mbMessagesSentPerSec_Type()
)
ex2mbMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbMessagesSentPerSec.setStatus("current")
_Ex2mbMessagesSubmitted_Type = Gauge32
_Ex2mbMessagesSubmitted_Object = MibTableColumn
ex2mbMessagesSubmitted = _Ex2mbMessagesSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 46),
    _Ex2mbMessagesSubmitted_Type()
)
ex2mbMessagesSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbMessagesSubmitted.setStatus("current")
_Ex2mbMessagesSubmittedPerSec_Type = Gauge32
_Ex2mbMessagesSubmittedPerSec_Object = MibTableColumn
ex2mbMessagesSubmittedPerSec = _Ex2mbMessagesSubmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 47),
    _Ex2mbMessagesSubmittedPerSec_Type()
)
ex2mbMessagesSubmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbMessagesSubmittedPerSec.setStatus("current")
_Ex2mbPeakClientLogons_Type = Gauge32
_Ex2mbPeakClientLogons_Object = MibTableColumn
ex2mbPeakClientLogons = _Ex2mbPeakClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 48),
    _Ex2mbPeakClientLogons_Type()
)
ex2mbPeakClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbPeakClientLogons.setStatus("current")
_Ex2mbReceiveQueueSize_Type = Gauge32
_Ex2mbReceiveQueueSize_Object = MibTableColumn
ex2mbReceiveQueueSize = _Ex2mbReceiveQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 49),
    _Ex2mbReceiveQueueSize_Type()
)
ex2mbReceiveQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbReceiveQueueSize.setStatus("current")
_Ex2mbReplIDCount_Type = Gauge32
_Ex2mbReplIDCount_Object = MibTableColumn
ex2mbReplIDCount = _Ex2mbReplIDCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 50),
    _Ex2mbReplIDCount_Type()
)
ex2mbReplIDCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbReplIDCount.setStatus("current")
_Ex2mbRestrictedViewCacheHitRate_Type = Gauge32
_Ex2mbRestrictedViewCacheHitRate_Object = MibTableColumn
ex2mbRestrictedViewCacheHitRate = _Ex2mbRestrictedViewCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 51),
    _Ex2mbRestrictedViewCacheHitRate_Type()
)
ex2mbRestrictedViewCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbRestrictedViewCacheHitRate.setStatus("current")
_Ex2mbRestrictedViewCacheMissRate_Type = Gauge32
_Ex2mbRestrictedViewCacheMissRate_Object = MibTableColumn
ex2mbRestrictedViewCacheMissRate = _Ex2mbRestrictedViewCacheMissRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 52),
    _Ex2mbRestrictedViewCacheMissRate_Type()
)
ex2mbRestrictedViewCacheMissRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbRestrictedViewCacheMissRate.setStatus("current")
_Ex2mbSearchTaskRate_Type = Gauge32
_Ex2mbSearchTaskRate_Object = MibTableColumn
ex2mbSearchTaskRate = _Ex2mbSearchTaskRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 53),
    _Ex2mbSearchTaskRate_Type()
)
ex2mbSearchTaskRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbSearchTaskRate.setStatus("current")
_Ex2mbSingleInstanceRatio_Type = Gauge32
_Ex2mbSingleInstanceRatio_Object = MibTableColumn
ex2mbSingleInstanceRatio = _Ex2mbSingleInstanceRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 54),
    _Ex2mbSingleInstanceRatio_Type()
)
ex2mbSingleInstanceRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbSingleInstanceRatio.setStatus("current")
_Ex2mbSlowFindRowRate_Type = Gauge32
_Ex2mbSlowFindRowRate_Object = MibTableColumn
ex2mbSlowFindRowRate = _Ex2mbSlowFindRowRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 55),
    _Ex2mbSlowFindRowRate_Type()
)
ex2mbSlowFindRowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbSlowFindRowRate.setStatus("current")
_Ex2mbTotalCountOfRecoverableItem_Type = Gauge32
_Ex2mbTotalCountOfRecoverableItem_Object = MibTableColumn
ex2mbTotalCountOfRecoverableItem = _Ex2mbTotalCountOfRecoverableItem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 56),
    _Ex2mbTotalCountOfRecoverableItem_Type()
)
ex2mbTotalCountOfRecoverableItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbTotalCountOfRecoverableItem.setStatus("current")
_Ex2mbTotalSizeOfRecoverableItems_Type = Gauge32
_Ex2mbTotalSizeOfRecoverableItems_Object = MibTableColumn
ex2mbTotalSizeOfRecoverableItems = _Ex2mbTotalSizeOfRecoverableItems_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 57),
    _Ex2mbTotalSizeOfRecoverableItems_Type()
)
ex2mbTotalSizeOfRecoverableItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbTotalSizeOfRecoverableItems.setStatus("current")
_Ex2mbVirusScanBackgrndScanThread_Type = Gauge32
_Ex2mbVirusScanBackgrndScanThread_Object = MibTableColumn
ex2mbVirusScanBackgrndScanThread = _Ex2mbVirusScanBackgrndScanThread_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 58),
    _Ex2mbVirusScanBackgrndScanThread_Type()
)
ex2mbVirusScanBackgrndScanThread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbVirusScanBackgrndScanThread.setStatus("current")
_Ex2mbVirusScanBackgrndMsgScanned_Type = Gauge32
_Ex2mbVirusScanBackgrndMsgScanned_Object = MibTableColumn
ex2mbVirusScanBackgrndMsgScanned = _Ex2mbVirusScanBackgrndMsgScanned_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 59),
    _Ex2mbVirusScanBackgrndMsgScanned_Type()
)
ex2mbVirusScanBackgrndMsgScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbVirusScanBackgrndMsgScanned.setStatus("current")
_Ex2mbVirusScanBackgrndMsgSkipped_Type = Gauge32
_Ex2mbVirusScanBackgrndMsgSkipped_Object = MibTableColumn
ex2mbVirusScanBackgrndMsgSkipped = _Ex2mbVirusScanBackgrndMsgSkipped_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 60),
    _Ex2mbVirusScanBackgrndMsgSkipped_Type()
)
ex2mbVirusScanBackgrndMsgSkipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbVirusScanBackgrndMsgSkipped.setStatus("current")
_Ex2mbVirusScanBackgrndMsgUpDate_Type = Gauge32
_Ex2mbVirusScanBackgrndMsgUpDate_Object = MibTableColumn
ex2mbVirusScanBackgrndMsgUpDate = _Ex2mbVirusScanBackgrndMsgUpDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 61),
    _Ex2mbVirusScanBackgrndMsgUpDate_Type()
)
ex2mbVirusScanBackgrndMsgUpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbVirusScanBackgrndMsgUpDate.setStatus("current")
_Ex2mbVirusScanExtRsltsAccepted_Type = Gauge32
_Ex2mbVirusScanExtRsltsAccepted_Object = MibTableColumn
ex2mbVirusScanExtRsltsAccepted = _Ex2mbVirusScanExtRsltsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 62),
    _Ex2mbVirusScanExtRsltsAccepted_Type()
)
ex2mbVirusScanExtRsltsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbVirusScanExtRsltsAccepted.setStatus("current")
_Ex2mbVirusScanExtRsltNotAccepted_Type = Gauge32
_Ex2mbVirusScanExtRsltNotAccepted_Object = MibTableColumn
ex2mbVirusScanExtRsltNotAccepted = _Ex2mbVirusScanExtRsltNotAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 63),
    _Ex2mbVirusScanExtRsltNotAccepted_Type()
)
ex2mbVirusScanExtRsltNotAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbVirusScanExtRsltNotAccepted.setStatus("current")
_Ex2mbVirusScanExtRsltsNotPresent_Type = Gauge32
_Ex2mbVirusScanExtRsltsNotPresent_Object = MibTableColumn
ex2mbVirusScanExtRsltsNotPresent = _Ex2mbVirusScanExtRsltsNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 47, 1, 64),
    _Ex2mbVirusScanExtRsltsNotPresent_Type()
)
ex2mbVirusScanExtRsltsNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2mbVirusScanExtRsltsNotPresent.setStatus("current")
_Ex2ISPublicTable_Object = MibTable
ex2ISPublicTable = _Ex2ISPublicTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48)
)
if mibBuilder.loadTexts:
    ex2ISPublicTable.setStatus("current")
_Ex2ISPublicEntry_Object = MibTableRow
ex2ISPublicEntry = _Ex2ISPublicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1)
)
ex2ISPublicEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2ispInstance"),
)
if mibBuilder.loadTexts:
    ex2ISPublicEntry.setStatus("current")
_Ex2ispInstance_Type = InstanceName
_Ex2ispInstance_Object = MibTableColumn
ex2ispInstance = _Ex2ispInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 1),
    _Ex2ispInstance_Type()
)
ex2ispInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispInstance.setStatus("current")
_Ex2ispActiveClientLogons_Type = Gauge32
_Ex2ispActiveClientLogons_Object = MibTableColumn
ex2ispActiveClientLogons = _Ex2ispActiveClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 2),
    _Ex2ispActiveClientLogons_Type()
)
ex2ispActiveClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispActiveClientLogons.setStatus("current")
_Ex2ispAverageDeliveryTime_Type = Gauge32
_Ex2ispAverageDeliveryTime_Object = MibTableColumn
ex2ispAverageDeliveryTime = _Ex2ispAverageDeliveryTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 3),
    _Ex2ispAverageDeliveryTime_Type()
)
ex2ispAverageDeliveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispAverageDeliveryTime.setStatus("current")
_Ex2ispCategorizationCount_Type = Gauge32
_Ex2ispCategorizationCount_Object = MibTableColumn
ex2ispCategorizationCount = _Ex2ispCategorizationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 4),
    _Ex2ispCategorizationCount_Type()
)
ex2ispCategorizationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispCategorizationCount.setStatus("current")
_Ex2ispClientLogons_Type = Gauge32
_Ex2ispClientLogons_Object = MibTableColumn
ex2ispClientLogons = _Ex2ispClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 5),
    _Ex2ispClientLogons_Type()
)
ex2ispClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispClientLogons.setStatus("current")
_Ex2ispEventHistoryDeletes_Type = Gauge32
_Ex2ispEventHistoryDeletes_Object = MibTableColumn
ex2ispEventHistoryDeletes = _Ex2ispEventHistoryDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 6),
    _Ex2ispEventHistoryDeletes_Type()
)
ex2ispEventHistoryDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistoryDeletes.setStatus("current")
_Ex2ispEventHistoryDeletesPerSec_Type = Gauge32
_Ex2ispEventHistoryDeletesPerSec_Object = MibTableColumn
ex2ispEventHistoryDeletesPerSec = _Ex2ispEventHistoryDeletesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 7),
    _Ex2ispEventHistoryDeletesPerSec_Type()
)
ex2ispEventHistoryDeletesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistoryDeletesPerSec.setStatus("current")
_Ex2ispEventHistEventCacheHitPerc_Type = Gauge32
_Ex2ispEventHistEventCacheHitPerc_Object = MibTableColumn
ex2ispEventHistEventCacheHitPerc = _Ex2ispEventHistEventCacheHitPerc_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 8),
    _Ex2ispEventHistEventCacheHitPerc_Type()
)
ex2ispEventHistEventCacheHitPerc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistEventCacheHitPerc.setStatus("current")
_Ex2ispEventHistoryEventsCount_Type = Gauge32
_Ex2ispEventHistoryEventsCount_Object = MibTableColumn
ex2ispEventHistoryEventsCount = _Ex2ispEventHistoryEventsCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 9),
    _Ex2ispEventHistoryEventsCount_Type()
)
ex2ispEventHistoryEventsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistoryEventsCount.setStatus("current")
_Ex2ispEventHistEvntEmptyCntClass_Type = Gauge32
_Ex2ispEventHistEvntEmptyCntClass_Object = MibTableColumn
ex2ispEventHistEvntEmptyCntClass = _Ex2ispEventHistEvntEmptyCntClass_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 10),
    _Ex2ispEventHistEvntEmptyCntClass_Type()
)
ex2ispEventHistEvntEmptyCntClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistEvntEmptyCntClass.setStatus("current")
_Ex2ispEventHisEventEmptyMsgClass_Type = Gauge32
_Ex2ispEventHisEventEmptyMsgClass_Object = MibTableColumn
ex2ispEventHisEventEmptyMsgClass = _Ex2ispEventHisEventEmptyMsgClass_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 11),
    _Ex2ispEventHisEventEmptyMsgClass_Type()
)
ex2ispEventHisEventEmptyMsgClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHisEventEmptyMsgClass.setStatus("current")
_Ex2ispEventHistEventTrunConClass_Type = Gauge32
_Ex2ispEventHistEventTrunConClass_Object = MibTableColumn
ex2ispEventHistEventTrunConClass = _Ex2ispEventHistEventTrunConClass_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 12),
    _Ex2ispEventHistEventTrunConClass_Type()
)
ex2ispEventHistEventTrunConClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistEventTrunConClass.setStatus("current")
_Ex2ispEventHistEventTrunMsgClass_Type = Gauge32
_Ex2ispEventHistEventTrunMsgClass_Object = MibTableColumn
ex2ispEventHistEventTrunMsgClass = _Ex2ispEventHistEventTrunMsgClass_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 13),
    _Ex2ispEventHistEventTrunMsgClass_Type()
)
ex2ispEventHistEventTrunMsgClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistEventTrunMsgClass.setStatus("current")
_Ex2ispEventHistoryReads_Type = Gauge32
_Ex2ispEventHistoryReads_Object = MibTableColumn
ex2ispEventHistoryReads = _Ex2ispEventHistoryReads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 14),
    _Ex2ispEventHistoryReads_Type()
)
ex2ispEventHistoryReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistoryReads.setStatus("current")
_Ex2ispEventHistoryReadsPerSec_Type = Gauge32
_Ex2ispEventHistoryReadsPerSec_Object = MibTableColumn
ex2ispEventHistoryReadsPerSec = _Ex2ispEventHistoryReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 15),
    _Ex2ispEventHistoryReadsPerSec_Type()
)
ex2ispEventHistoryReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistoryReadsPerSec.setStatus("current")
_Ex2ispEventHistUncommitTranCount_Type = Gauge32
_Ex2ispEventHistUncommitTranCount_Object = MibTableColumn
ex2ispEventHistUncommitTranCount = _Ex2ispEventHistUncommitTranCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 16),
    _Ex2ispEventHistUncommitTranCount_Type()
)
ex2ispEventHistUncommitTranCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistUncommitTranCount.setStatus("current")
_Ex2ispEventHistWatermarksCount_Type = Gauge32
_Ex2ispEventHistWatermarksCount_Object = MibTableColumn
ex2ispEventHistWatermarksCount = _Ex2ispEventHistWatermarksCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 17),
    _Ex2ispEventHistWatermarksCount_Type()
)
ex2ispEventHistWatermarksCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistWatermarksCount.setStatus("current")
_Ex2ispEventHistWatermarksDeletes_Type = Gauge32
_Ex2ispEventHistWatermarksDeletes_Object = MibTableColumn
ex2ispEventHistWatermarksDeletes = _Ex2ispEventHistWatermarksDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 18),
    _Ex2ispEventHistWatermarksDeletes_Type()
)
ex2ispEventHistWatermarksDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistWatermarksDeletes.setStatus("current")
_Ex2ispEventHistWatermarkDelPrSec_Type = Gauge32
_Ex2ispEventHistWatermarkDelPrSec_Object = MibTableColumn
ex2ispEventHistWatermarkDelPrSec = _Ex2ispEventHistWatermarkDelPrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 19),
    _Ex2ispEventHistWatermarkDelPrSec_Type()
)
ex2ispEventHistWatermarkDelPrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistWatermarkDelPrSec.setStatus("current")
_Ex2ispEventHistWatermarksReads_Type = Gauge32
_Ex2ispEventHistWatermarksReads_Object = MibTableColumn
ex2ispEventHistWatermarksReads = _Ex2ispEventHistWatermarksReads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 20),
    _Ex2ispEventHistWatermarksReads_Type()
)
ex2ispEventHistWatermarksReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistWatermarksReads.setStatus("current")
_Ex2ispEventHistWatermarkRdPerSec_Type = Gauge32
_Ex2ispEventHistWatermarkRdPerSec_Object = MibTableColumn
ex2ispEventHistWatermarkRdPerSec = _Ex2ispEventHistWatermarkRdPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 21),
    _Ex2ispEventHistWatermarkRdPerSec_Type()
)
ex2ispEventHistWatermarkRdPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistWatermarkRdPerSec.setStatus("current")
_Ex2ispEventHistWatermarksWrites_Type = Gauge32
_Ex2ispEventHistWatermarksWrites_Object = MibTableColumn
ex2ispEventHistWatermarksWrites = _Ex2ispEventHistWatermarksWrites_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 22),
    _Ex2ispEventHistWatermarksWrites_Type()
)
ex2ispEventHistWatermarksWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistWatermarksWrites.setStatus("current")
_Ex2ispEventHistWatermarkWriteSec_Type = Gauge32
_Ex2ispEventHistWatermarkWriteSec_Object = MibTableColumn
ex2ispEventHistWatermarkWriteSec = _Ex2ispEventHistWatermarkWriteSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 23),
    _Ex2ispEventHistWatermarkWriteSec_Type()
)
ex2ispEventHistWatermarkWriteSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistWatermarkWriteSec.setStatus("current")
_Ex2ispEventHistoryWrites_Type = Gauge32
_Ex2ispEventHistoryWrites_Object = MibTableColumn
ex2ispEventHistoryWrites = _Ex2ispEventHistoryWrites_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 24),
    _Ex2ispEventHistoryWrites_Type()
)
ex2ispEventHistoryWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistoryWrites.setStatus("current")
_Ex2ispEventHistoryWritesPerSec_Type = Gauge32
_Ex2ispEventHistoryWritesPerSec_Object = MibTableColumn
ex2ispEventHistoryWritesPerSec = _Ex2ispEventHistoryWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 25),
    _Ex2ispEventHistoryWritesPerSec_Type()
)
ex2ispEventHistoryWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispEventHistoryWritesPerSec.setStatus("current")
_Ex2ispFolderOpensPerSec_Type = Gauge32
_Ex2ispFolderOpensPerSec_Object = MibTableColumn
ex2ispFolderOpensPerSec = _Ex2ispFolderOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 26),
    _Ex2ispFolderOpensPerSec_Type()
)
ex2ispFolderOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispFolderOpensPerSec.setStatus("current")
_Ex2ispHTTPPerDAVCurrentPendNotif_Type = Gauge32
_Ex2ispHTTPPerDAVCurrentPendNotif_Object = MibTableColumn
ex2ispHTTPPerDAVCurrentPendNotif = _Ex2ispHTTPPerDAVCurrentPendNotif_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 27),
    _Ex2ispHTTPPerDAVCurrentPendNotif_Type()
)
ex2ispHTTPPerDAVCurrentPendNotif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispHTTPPerDAVCurrentPendNotif.setStatus("current")
_Ex2ispHTTPPerDAVCurrentSubscript_Type = Gauge32
_Ex2ispHTTPPerDAVCurrentSubscript_Object = MibTableColumn
ex2ispHTTPPerDAVCurrentSubscript = _Ex2ispHTTPPerDAVCurrentSubscript_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 28),
    _Ex2ispHTTPPerDAVCurrentSubscript_Type()
)
ex2ispHTTPPerDAVCurrentSubscript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispHTTPPerDAVCurrentSubscript.setStatus("current")
_Ex2ispHTTPPerDAVCurrentTransLock_Type = Gauge32
_Ex2ispHTTPPerDAVCurrentTransLock_Object = MibTableColumn
ex2ispHTTPPerDAVCurrentTransLock = _Ex2ispHTTPPerDAVCurrentTransLock_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 29),
    _Ex2ispHTTPPerDAVCurrentTransLock_Type()
)
ex2ispHTTPPerDAVCurrentTransLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispHTTPPerDAVCurrentTransLock.setStatus("current")
_Ex2ispHTTPPerDAVNotifyReqPerSec_Type = Gauge32
_Ex2ispHTTPPerDAVNotifyReqPerSec_Object = MibTableColumn
ex2ispHTTPPerDAVNotifyReqPerSec = _Ex2ispHTTPPerDAVNotifyReqPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 30),
    _Ex2ispHTTPPerDAVNotifyReqPerSec_Type()
)
ex2ispHTTPPerDAVNotifyReqPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispHTTPPerDAVNotifyReqPerSec.setStatus("current")
_Ex2ispHTTPPerDAVTotalLockCreated_Type = Gauge32
_Ex2ispHTTPPerDAVTotalLockCreated_Object = MibTableColumn
ex2ispHTTPPerDAVTotalLockCreated = _Ex2ispHTTPPerDAVTotalLockCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 31),
    _Ex2ispHTTPPerDAVTotalLockCreated_Type()
)
ex2ispHTTPPerDAVTotalLockCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispHTTPPerDAVTotalLockCreated.setStatus("current")
_Ex2ispHTTPPerDAVTotalNotifyReqst_Type = Gauge32
_Ex2ispHTTPPerDAVTotalNotifyReqst_Object = MibTableColumn
ex2ispHTTPPerDAVTotalNotifyReqst = _Ex2ispHTTPPerDAVTotalNotifyReqst_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 32),
    _Ex2ispHTTPPerDAVTotalNotifyReqst_Type()
)
ex2ispHTTPPerDAVTotalNotifyReqst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispHTTPPerDAVTotalNotifyReqst.setStatus("current")
_Ex2ispHTTPPerDAVTotalSubsCreated_Type = Gauge32
_Ex2ispHTTPPerDAVTotalSubsCreated_Object = MibTableColumn
ex2ispHTTPPerDAVTotalSubsCreated = _Ex2ispHTTPPerDAVTotalSubsCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 33),
    _Ex2ispHTTPPerDAVTotalSubsCreated_Type()
)
ex2ispHTTPPerDAVTotalSubsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispHTTPPerDAVTotalSubsCreated.setStatus("current")
_Ex2ispHTTPPerDAVTotalSubsExpired_Type = Gauge32
_Ex2ispHTTPPerDAVTotalSubsExpired_Object = MibTableColumn
ex2ispHTTPPerDAVTotalSubsExpired = _Ex2ispHTTPPerDAVTotalSubsExpired_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 34),
    _Ex2ispHTTPPerDAVTotalSubsExpired_Type()
)
ex2ispHTTPPerDAVTotalSubsExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispHTTPPerDAVTotalSubsExpired.setStatus("current")
_Ex2ispLogonOperationsPerSec_Type = Gauge32
_Ex2ispLogonOperationsPerSec_Object = MibTableColumn
ex2ispLogonOperationsPerSec = _Ex2ispLogonOperationsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 35),
    _Ex2ispLogonOperationsPerSec_Type()
)
ex2ispLogonOperationsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispLogonOperationsPerSec.setStatus("current")
_Ex2ispMessageOpensPerSec_Type = Gauge32
_Ex2ispMessageOpensPerSec_Object = MibTableColumn
ex2ispMessageOpensPerSec = _Ex2ispMessageOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 36),
    _Ex2ispMessageOpensPerSec_Type()
)
ex2ispMessageOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispMessageOpensPerSec.setStatus("current")
_Ex2ispMessageRecipientsDelivered_Type = Gauge32
_Ex2ispMessageRecipientsDelivered_Object = MibTableColumn
ex2ispMessageRecipientsDelivered = _Ex2ispMessageRecipientsDelivered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 37),
    _Ex2ispMessageRecipientsDelivered_Type()
)
ex2ispMessageRecipientsDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispMessageRecipientsDelivered.setStatus("current")
_Ex2ispMsgRecipientsDeliverPerSec_Type = Gauge32
_Ex2ispMsgRecipientsDeliverPerSec_Object = MibTableColumn
ex2ispMsgRecipientsDeliverPerSec = _Ex2ispMsgRecipientsDeliverPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 38),
    _Ex2ispMsgRecipientsDeliverPerSec_Type()
)
ex2ispMsgRecipientsDeliverPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispMsgRecipientsDeliverPerSec.setStatus("current")
_Ex2ispMessagesDelivered_Type = Gauge32
_Ex2ispMessagesDelivered_Object = MibTableColumn
ex2ispMessagesDelivered = _Ex2ispMessagesDelivered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 39),
    _Ex2ispMessagesDelivered_Type()
)
ex2ispMessagesDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispMessagesDelivered.setStatus("current")
_Ex2ispMessagesDeliveredPerSec_Type = Gauge32
_Ex2ispMessagesDeliveredPerSec_Object = MibTableColumn
ex2ispMessagesDeliveredPerSec = _Ex2ispMessagesDeliveredPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 40),
    _Ex2ispMessagesDeliveredPerSec_Type()
)
ex2ispMessagesDeliveredPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispMessagesDeliveredPerSec.setStatus("current")
_Ex2ispMsgsQueuedForSubmission_Type = Gauge32
_Ex2ispMsgsQueuedForSubmission_Object = MibTableColumn
ex2ispMsgsQueuedForSubmission = _Ex2ispMsgsQueuedForSubmission_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 41),
    _Ex2ispMsgsQueuedForSubmission_Type()
)
ex2ispMsgsQueuedForSubmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispMsgsQueuedForSubmission.setStatus("current")
_Ex2ispMessagesSent_Type = Gauge32
_Ex2ispMessagesSent_Object = MibTableColumn
ex2ispMessagesSent = _Ex2ispMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 42),
    _Ex2ispMessagesSent_Type()
)
ex2ispMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispMessagesSent.setStatus("current")
_Ex2ispMessagesSentPerSec_Type = Gauge32
_Ex2ispMessagesSentPerSec_Object = MibTableColumn
ex2ispMessagesSentPerSec = _Ex2ispMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 43),
    _Ex2ispMessagesSentPerSec_Type()
)
ex2ispMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispMessagesSentPerSec.setStatus("current")
_Ex2ispMessagesSubmitted_Type = Gauge32
_Ex2ispMessagesSubmitted_Object = MibTableColumn
ex2ispMessagesSubmitted = _Ex2ispMessagesSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 44),
    _Ex2ispMessagesSubmitted_Type()
)
ex2ispMessagesSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispMessagesSubmitted.setStatus("current")
_Ex2ispMessagesSubmittedPerSec_Type = Gauge32
_Ex2ispMessagesSubmittedPerSec_Object = MibTableColumn
ex2ispMessagesSubmittedPerSec = _Ex2ispMessagesSubmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 45),
    _Ex2ispMessagesSubmittedPerSec_Type()
)
ex2ispMessagesSubmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispMessagesSubmittedPerSec.setStatus("current")
_Ex2ispNumMsgsExpireFrmPublicFold_Type = Gauge32
_Ex2ispNumMsgsExpireFrmPublicFold_Object = MibTableColumn
ex2ispNumMsgsExpireFrmPublicFold = _Ex2ispNumMsgsExpireFrmPublicFold_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 46),
    _Ex2ispNumMsgsExpireFrmPublicFold_Type()
)
ex2ispNumMsgsExpireFrmPublicFold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispNumMsgsExpireFrmPublicFold.setStatus("current")
_Ex2ispPeakClientLogons_Type = Gauge32
_Ex2ispPeakClientLogons_Object = MibTableColumn
ex2ispPeakClientLogons = _Ex2ispPeakClientLogons_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 47),
    _Ex2ispPeakClientLogons_Type()
)
ex2ispPeakClientLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispPeakClientLogons.setStatus("current")
_Ex2ispReceiveQueueSize_Type = Gauge32
_Ex2ispReceiveQueueSize_Object = MibTableColumn
ex2ispReceiveQueueSize = _Ex2ispReceiveQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 48),
    _Ex2ispReceiveQueueSize_Type()
)
ex2ispReceiveQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReceiveQueueSize.setStatus("current")
_Ex2ispReplIDCount_Type = Gauge32
_Ex2ispReplIDCount_Object = MibTableColumn
ex2ispReplIDCount = _Ex2ispReplIDCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 49),
    _Ex2ispReplIDCount_Type()
)
ex2ispReplIDCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplIDCount.setStatus("current")
_Ex2ispReplicBackfillDataMsgsRecv_Type = Gauge32
_Ex2ispReplicBackfillDataMsgsRecv_Object = MibTableColumn
ex2ispReplicBackfillDataMsgsRecv = _Ex2ispReplicBackfillDataMsgsRecv_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 50),
    _Ex2ispReplicBackfillDataMsgsRecv_Type()
)
ex2ispReplicBackfillDataMsgsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicBackfillDataMsgsRecv.setStatus("current")
_Ex2ispReplicBackfillDataMsgsSent_Type = Gauge32
_Ex2ispReplicBackfillDataMsgsSent_Object = MibTableColumn
ex2ispReplicBackfillDataMsgsSent = _Ex2ispReplicBackfillDataMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 51),
    _Ex2ispReplicBackfillDataMsgsSent_Type()
)
ex2ispReplicBackfillDataMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicBackfillDataMsgsSent.setStatus("current")
_Ex2ispReplicBackfillRequestRecvd_Type = Gauge32
_Ex2ispReplicBackfillRequestRecvd_Object = MibTableColumn
ex2ispReplicBackfillRequestRecvd = _Ex2ispReplicBackfillRequestRecvd_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 52),
    _Ex2ispReplicBackfillRequestRecvd_Type()
)
ex2ispReplicBackfillRequestRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicBackfillRequestRecvd.setStatus("current")
_Ex2ispReplicBackfillRequestsSent_Type = Gauge32
_Ex2ispReplicBackfillRequestsSent_Object = MibTableColumn
ex2ispReplicBackfillRequestsSent = _Ex2ispReplicBackfillRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 53),
    _Ex2ispReplicBackfillRequestsSent_Type()
)
ex2ispReplicBackfillRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicBackfillRequestsSent.setStatus("current")
_Ex2ispReplicFolderChangeReceived_Type = Gauge32
_Ex2ispReplicFolderChangeReceived_Object = MibTableColumn
ex2ispReplicFolderChangeReceived = _Ex2ispReplicFolderChangeReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 54),
    _Ex2ispReplicFolderChangeReceived_Type()
)
ex2ispReplicFolderChangeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicFolderChangeReceived.setStatus("current")
_Ex2ispReplicFolderChangesSent_Type = Gauge32
_Ex2ispReplicFolderChangesSent_Object = MibTableColumn
ex2ispReplicFolderChangesSent = _Ex2ispReplicFolderChangesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 55),
    _Ex2ispReplicFolderChangesSent_Type()
)
ex2ispReplicFolderChangesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicFolderChangesSent.setStatus("current")
_Ex2ispReplicFolderDataMsgReceive_Type = Gauge32
_Ex2ispReplicFolderDataMsgReceive_Object = MibTableColumn
ex2ispReplicFolderDataMsgReceive = _Ex2ispReplicFolderDataMsgReceive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 56),
    _Ex2ispReplicFolderDataMsgReceive_Type()
)
ex2ispReplicFolderDataMsgReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicFolderDataMsgReceive.setStatus("current")
_Ex2ispReplicFolderDataMsgsSent_Type = Gauge32
_Ex2ispReplicFolderDataMsgsSent_Object = MibTableColumn
ex2ispReplicFolderDataMsgsSent = _Ex2ispReplicFolderDataMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 57),
    _Ex2ispReplicFolderDataMsgsSent_Type()
)
ex2ispReplicFolderDataMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicFolderDataMsgsSent.setStatus("current")
_Ex2ispReplicFolderTreeMsgReceive_Type = Gauge32
_Ex2ispReplicFolderTreeMsgReceive_Object = MibTableColumn
ex2ispReplicFolderTreeMsgReceive = _Ex2ispReplicFolderTreeMsgReceive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 58),
    _Ex2ispReplicFolderTreeMsgReceive_Type()
)
ex2ispReplicFolderTreeMsgReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicFolderTreeMsgReceive.setStatus("current")
_Ex2ispReplicFolderTreeMsgsSent_Type = Gauge32
_Ex2ispReplicFolderTreeMsgsSent_Object = MibTableColumn
ex2ispReplicFolderTreeMsgsSent = _Ex2ispReplicFolderTreeMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 59),
    _Ex2ispReplicFolderTreeMsgsSent_Type()
)
ex2ispReplicFolderTreeMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicFolderTreeMsgsSent.setStatus("current")
_Ex2ispReplicMessageChangeReceive_Type = Gauge32
_Ex2ispReplicMessageChangeReceive_Object = MibTableColumn
ex2ispReplicMessageChangeReceive = _Ex2ispReplicMessageChangeReceive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 60),
    _Ex2ispReplicMessageChangeReceive_Type()
)
ex2ispReplicMessageChangeReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicMessageChangeReceive.setStatus("current")
_Ex2ispReplicMessageChangesSent_Type = Gauge32
_Ex2ispReplicMessageChangesSent_Object = MibTableColumn
ex2ispReplicMessageChangesSent = _Ex2ispReplicMessageChangesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 61),
    _Ex2ispReplicMessageChangesSent_Type()
)
ex2ispReplicMessageChangesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicMessageChangesSent.setStatus("current")
_Ex2ispReplicMsgsReceived_Type = Gauge32
_Ex2ispReplicMsgsReceived_Object = MibTableColumn
ex2ispReplicMsgsReceived = _Ex2ispReplicMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 62),
    _Ex2ispReplicMsgsReceived_Type()
)
ex2ispReplicMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicMsgsReceived.setStatus("current")
_Ex2ispReplicationMessagesSent_Type = Gauge32
_Ex2ispReplicationMessagesSent_Object = MibTableColumn
ex2ispReplicationMessagesSent = _Ex2ispReplicationMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 63),
    _Ex2ispReplicationMessagesSent_Type()
)
ex2ispReplicationMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicationMessagesSent.setStatus("current")
_Ex2ispReplicReceiveQueueSize_Type = Gauge32
_Ex2ispReplicReceiveQueueSize_Object = MibTableColumn
ex2ispReplicReceiveQueueSize = _Ex2ispReplicReceiveQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 64),
    _Ex2ispReplicReceiveQueueSize_Type()
)
ex2ispReplicReceiveQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicReceiveQueueSize.setStatus("current")
_Ex2ispReplicStatusMsgsReceived_Type = Gauge32
_Ex2ispReplicStatusMsgsReceived_Object = MibTableColumn
ex2ispReplicStatusMsgsReceived = _Ex2ispReplicStatusMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 65),
    _Ex2ispReplicStatusMsgsReceived_Type()
)
ex2ispReplicStatusMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicStatusMsgsReceived.setStatus("current")
_Ex2ispReplicStatusMsgsSent_Type = Gauge32
_Ex2ispReplicStatusMsgsSent_Object = MibTableColumn
ex2ispReplicStatusMsgsSent = _Ex2ispReplicStatusMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 66),
    _Ex2ispReplicStatusMsgsSent_Type()
)
ex2ispReplicStatusMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispReplicStatusMsgsSent.setStatus("current")
_Ex2ispRestrictedViewCacheHitRate_Type = Gauge32
_Ex2ispRestrictedViewCacheHitRate_Object = MibTableColumn
ex2ispRestrictedViewCacheHitRate = _Ex2ispRestrictedViewCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 67),
    _Ex2ispRestrictedViewCacheHitRate_Type()
)
ex2ispRestrictedViewCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispRestrictedViewCacheHitRate.setStatus("current")
_Ex2ispRestricteViewCacheMissRate_Type = Gauge32
_Ex2ispRestricteViewCacheMissRate_Object = MibTableColumn
ex2ispRestricteViewCacheMissRate = _Ex2ispRestricteViewCacheMissRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 68),
    _Ex2ispRestricteViewCacheMissRate_Type()
)
ex2ispRestricteViewCacheMissRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispRestricteViewCacheMissRate.setStatus("current")
_Ex2ispSearchTaskRate_Type = Gauge32
_Ex2ispSearchTaskRate_Object = MibTableColumn
ex2ispSearchTaskRate = _Ex2ispSearchTaskRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 69),
    _Ex2ispSearchTaskRate_Type()
)
ex2ispSearchTaskRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispSearchTaskRate.setStatus("current")
_Ex2ispSingleInstanceRatio_Type = Gauge32
_Ex2ispSingleInstanceRatio_Object = MibTableColumn
ex2ispSingleInstanceRatio = _Ex2ispSingleInstanceRatio_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 70),
    _Ex2ispSingleInstanceRatio_Type()
)
ex2ispSingleInstanceRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispSingleInstanceRatio.setStatus("current")
_Ex2ispSlowFindRowRate_Type = Gauge32
_Ex2ispSlowFindRowRate_Object = MibTableColumn
ex2ispSlowFindRowRate = _Ex2ispSlowFindRowRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 71),
    _Ex2ispSlowFindRowRate_Type()
)
ex2ispSlowFindRowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispSlowFindRowRate.setStatus("current")
_Ex2ispTotalCountRecoverableItems_Type = Gauge32
_Ex2ispTotalCountRecoverableItems_Object = MibTableColumn
ex2ispTotalCountRecoverableItems = _Ex2ispTotalCountRecoverableItems_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 72),
    _Ex2ispTotalCountRecoverableItems_Type()
)
ex2ispTotalCountRecoverableItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispTotalCountRecoverableItems.setStatus("current")
_Ex2ispTotalSizeOfRecoverableItem_Type = Gauge32
_Ex2ispTotalSizeOfRecoverableItem_Object = MibTableColumn
ex2ispTotalSizeOfRecoverableItem = _Ex2ispTotalSizeOfRecoverableItem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 73),
    _Ex2ispTotalSizeOfRecoverableItem_Type()
)
ex2ispTotalSizeOfRecoverableItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispTotalSizeOfRecoverableItem.setStatus("current")
_Ex2ispVirusScanBackgrndScnThread_Type = Gauge32
_Ex2ispVirusScanBackgrndScnThread_Object = MibTableColumn
ex2ispVirusScanBackgrndScnThread = _Ex2ispVirusScanBackgrndScnThread_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 74),
    _Ex2ispVirusScanBackgrndScnThread_Type()
)
ex2ispVirusScanBackgrndScnThread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispVirusScanBackgrndScnThread.setStatus("current")
_Ex2ispVirusScanBackgrndMsgsScan_Type = Gauge32
_Ex2ispVirusScanBackgrndMsgsScan_Object = MibTableColumn
ex2ispVirusScanBackgrndMsgsScan = _Ex2ispVirusScanBackgrndMsgsScan_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 75),
    _Ex2ispVirusScanBackgrndMsgsScan_Type()
)
ex2ispVirusScanBackgrndMsgsScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispVirusScanBackgrndMsgsScan.setStatus("current")
_Ex2ispVirusScanBackgrndMsgSkippd_Type = Gauge32
_Ex2ispVirusScanBackgrndMsgSkippd_Object = MibTableColumn
ex2ispVirusScanBackgrndMsgSkippd = _Ex2ispVirusScanBackgrndMsgSkippd_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 76),
    _Ex2ispVirusScanBackgrndMsgSkippd_Type()
)
ex2ispVirusScanBackgrndMsgSkippd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispVirusScanBackgrndMsgSkippd.setStatus("current")
_Ex2ispVirusScanBackgrndMsgUpDate_Type = Gauge32
_Ex2ispVirusScanBackgrndMsgUpDate_Object = MibTableColumn
ex2ispVirusScanBackgrndMsgUpDate = _Ex2ispVirusScanBackgrndMsgUpDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 77),
    _Ex2ispVirusScanBackgrndMsgUpDate_Type()
)
ex2ispVirusScanBackgrndMsgUpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispVirusScanBackgrndMsgUpDate.setStatus("current")
_Ex2ispVirusScanExtResultAccepted_Type = Gauge32
_Ex2ispVirusScanExtResultAccepted_Object = MibTableColumn
ex2ispVirusScanExtResultAccepted = _Ex2ispVirusScanExtResultAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 78),
    _Ex2ispVirusScanExtResultAccepted_Type()
)
ex2ispVirusScanExtResultAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispVirusScanExtResultAccepted.setStatus("current")
_Ex2ispVirusScanExtResultNotAccpt_Type = Gauge32
_Ex2ispVirusScanExtResultNotAccpt_Object = MibTableColumn
ex2ispVirusScanExtResultNotAccpt = _Ex2ispVirusScanExtResultNotAccpt_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 79),
    _Ex2ispVirusScanExtResultNotAccpt_Type()
)
ex2ispVirusScanExtResultNotAccpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispVirusScanExtResultNotAccpt.setStatus("current")
_Ex2ispVirusScanExtResultsNotPres_Type = Gauge32
_Ex2ispVirusScanExtResultsNotPres_Object = MibTableColumn
ex2ispVirusScanExtResultsNotPres = _Ex2ispVirusScanExtResultsNotPres_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 48, 1, 80),
    _Ex2ispVirusScanExtResultsNotPres_Type()
)
ex2ispVirusScanExtResultsNotPres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2ispVirusScanExtResultsNotPres.setStatus("current")
_Ex2Imap4Table_Object = MibTable
ex2Imap4Table = _Ex2Imap4Table_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49)
)
if mibBuilder.loadTexts:
    ex2Imap4Table.setStatus("current")
_Ex2Imap4Entry_Object = MibTableRow
ex2Imap4Entry = _Ex2Imap4Entry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1)
)
ex2Imap4Entry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2im4Instance"),
)
if mibBuilder.loadTexts:
    ex2Imap4Entry.setStatus("current")
_Ex2im4Instance_Type = InstanceName
_Ex2im4Instance_Object = MibTableColumn
ex2im4Instance = _Ex2im4Instance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 1),
    _Ex2im4Instance_Type()
)
ex2im4Instance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4Instance.setStatus("current")
_Ex2im4ActiveSSLConnections_Type = Gauge32
_Ex2im4ActiveSSLConnections_Object = MibTableColumn
ex2im4ActiveSSLConnections = _Ex2im4ActiveSSLConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 2),
    _Ex2im4ActiveSSLConnections_Type()
)
ex2im4ActiveSSLConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ActiveSSLConnections.setStatus("current")
_Ex2im4AppendFailures_Type = Gauge32
_Ex2im4AppendFailures_Object = MibTableColumn
ex2im4AppendFailures = _Ex2im4AppendFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 3),
    _Ex2im4AppendFailures_Type()
)
ex2im4AppendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4AppendFailures.setStatus("current")
_Ex2im4AppendRate_Type = Gauge32
_Ex2im4AppendRate_Object = MibTableColumn
ex2im4AppendRate = _Ex2im4AppendRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 4),
    _Ex2im4AppendRate_Type()
)
ex2im4AppendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4AppendRate.setStatus("current")
_Ex2im4AppendTotal_Type = Gauge32
_Ex2im4AppendTotal_Object = MibTableColumn
ex2im4AppendTotal = _Ex2im4AppendTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 5),
    _Ex2im4AppendTotal_Type()
)
ex2im4AppendTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4AppendTotal.setStatus("current")
_Ex2im4AuthenticateFailures_Type = Gauge32
_Ex2im4AuthenticateFailures_Object = MibTableColumn
ex2im4AuthenticateFailures = _Ex2im4AuthenticateFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 6),
    _Ex2im4AuthenticateFailures_Type()
)
ex2im4AuthenticateFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4AuthenticateFailures.setStatus("current")
_Ex2im4AuthenticateRate_Type = Gauge32
_Ex2im4AuthenticateRate_Object = MibTableColumn
ex2im4AuthenticateRate = _Ex2im4AuthenticateRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 7),
    _Ex2im4AuthenticateRate_Type()
)
ex2im4AuthenticateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4AuthenticateRate.setStatus("current")
_Ex2im4AuthenticateTotal_Type = Gauge32
_Ex2im4AuthenticateTotal_Object = MibTableColumn
ex2im4AuthenticateTotal = _Ex2im4AuthenticateTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 8),
    _Ex2im4AuthenticateTotal_Type()
)
ex2im4AuthenticateTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4AuthenticateTotal.setStatus("current")
_Ex2im4AvgCommProcessTimeMillisec_Type = Gauge32
_Ex2im4AvgCommProcessTimeMillisec_Object = MibTableColumn
ex2im4AvgCommProcessTimeMillisec = _Ex2im4AvgCommProcessTimeMillisec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 9),
    _Ex2im4AvgCommProcessTimeMillisec_Type()
)
ex2im4AvgCommProcessTimeMillisec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4AvgCommProcessTimeMillisec.setStatus("current")
_Ex2im4CapabilityFailures_Type = Gauge32
_Ex2im4CapabilityFailures_Object = MibTableColumn
ex2im4CapabilityFailures = _Ex2im4CapabilityFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 10),
    _Ex2im4CapabilityFailures_Type()
)
ex2im4CapabilityFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CapabilityFailures.setStatus("current")
_Ex2im4CapabilityRate_Type = Gauge32
_Ex2im4CapabilityRate_Object = MibTableColumn
ex2im4CapabilityRate = _Ex2im4CapabilityRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 11),
    _Ex2im4CapabilityRate_Type()
)
ex2im4CapabilityRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CapabilityRate.setStatus("current")
_Ex2im4CapabilityTotal_Type = Gauge32
_Ex2im4CapabilityTotal_Object = MibTableColumn
ex2im4CapabilityTotal = _Ex2im4CapabilityTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 12),
    _Ex2im4CapabilityTotal_Type()
)
ex2im4CapabilityTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CapabilityTotal.setStatus("current")
_Ex2im4CheckFailures_Type = Gauge32
_Ex2im4CheckFailures_Object = MibTableColumn
ex2im4CheckFailures = _Ex2im4CheckFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 13),
    _Ex2im4CheckFailures_Type()
)
ex2im4CheckFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CheckFailures.setStatus("current")
_Ex2im4CheckRate_Type = Gauge32
_Ex2im4CheckRate_Object = MibTableColumn
ex2im4CheckRate = _Ex2im4CheckRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 14),
    _Ex2im4CheckRate_Type()
)
ex2im4CheckRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CheckRate.setStatus("current")
_Ex2im4CheckTotal_Type = Gauge32
_Ex2im4CheckTotal_Object = MibTableColumn
ex2im4CheckTotal = _Ex2im4CheckTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 15),
    _Ex2im4CheckTotal_Type()
)
ex2im4CheckTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CheckTotal.setStatus("current")
_Ex2im4CloseFailures_Type = Gauge32
_Ex2im4CloseFailures_Object = MibTableColumn
ex2im4CloseFailures = _Ex2im4CloseFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 16),
    _Ex2im4CloseFailures_Type()
)
ex2im4CloseFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CloseFailures.setStatus("current")
_Ex2im4CloseRate_Type = Gauge32
_Ex2im4CloseRate_Object = MibTableColumn
ex2im4CloseRate = _Ex2im4CloseRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 17),
    _Ex2im4CloseRate_Type()
)
ex2im4CloseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CloseRate.setStatus("current")
_Ex2im4CloseTotal_Type = Gauge32
_Ex2im4CloseTotal_Object = MibTableColumn
ex2im4CloseTotal = _Ex2im4CloseTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 18),
    _Ex2im4CloseTotal_Type()
)
ex2im4CloseTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CloseTotal.setStatus("current")
_Ex2im4ConnectionsFailed_Type = Gauge32
_Ex2im4ConnectionsFailed_Object = MibTableColumn
ex2im4ConnectionsFailed = _Ex2im4ConnectionsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 19),
    _Ex2im4ConnectionsFailed_Type()
)
ex2im4ConnectionsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ConnectionsFailed.setStatus("current")
_Ex2im4ConnectionsRejected_Type = Gauge32
_Ex2im4ConnectionsRejected_Object = MibTableColumn
ex2im4ConnectionsRejected = _Ex2im4ConnectionsRejected_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 20),
    _Ex2im4ConnectionsRejected_Type()
)
ex2im4ConnectionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ConnectionsRejected.setStatus("current")
_Ex2im4CopyFailures_Type = Gauge32
_Ex2im4CopyFailures_Object = MibTableColumn
ex2im4CopyFailures = _Ex2im4CopyFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 21),
    _Ex2im4CopyFailures_Type()
)
ex2im4CopyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CopyFailures.setStatus("current")
_Ex2im4CopyRate_Type = Gauge32
_Ex2im4CopyRate_Object = MibTableColumn
ex2im4CopyRate = _Ex2im4CopyRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 22),
    _Ex2im4CopyRate_Type()
)
ex2im4CopyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CopyRate.setStatus("current")
_Ex2im4CopyTotal_Type = Gauge32
_Ex2im4CopyTotal_Object = MibTableColumn
ex2im4CopyTotal = _Ex2im4CopyTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 23),
    _Ex2im4CopyTotal_Type()
)
ex2im4CopyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CopyTotal.setStatus("current")
_Ex2im4CreateFailures_Type = Gauge32
_Ex2im4CreateFailures_Object = MibTableColumn
ex2im4CreateFailures = _Ex2im4CreateFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 24),
    _Ex2im4CreateFailures_Type()
)
ex2im4CreateFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CreateFailures.setStatus("current")
_Ex2im4CreateRate_Type = Gauge32
_Ex2im4CreateRate_Object = MibTableColumn
ex2im4CreateRate = _Ex2im4CreateRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 25),
    _Ex2im4CreateRate_Type()
)
ex2im4CreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CreateRate.setStatus("current")
_Ex2im4CreateTotal_Type = Gauge32
_Ex2im4CreateTotal_Object = MibTableColumn
ex2im4CreateTotal = _Ex2im4CreateTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 26),
    _Ex2im4CreateTotal_Type()
)
ex2im4CreateTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CreateTotal.setStatus("current")
_Ex2im4CurrentConnections_Type = Gauge32
_Ex2im4CurrentConnections_Object = MibTableColumn
ex2im4CurrentConnections = _Ex2im4CurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 27),
    _Ex2im4CurrentConnections_Type()
)
ex2im4CurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4CurrentConnections.setStatus("current")
_Ex2im4DeleteFailures_Type = Gauge32
_Ex2im4DeleteFailures_Object = MibTableColumn
ex2im4DeleteFailures = _Ex2im4DeleteFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 28),
    _Ex2im4DeleteFailures_Type()
)
ex2im4DeleteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4DeleteFailures.setStatus("current")
_Ex2im4DeleteRate_Type = Gauge32
_Ex2im4DeleteRate_Object = MibTableColumn
ex2im4DeleteRate = _Ex2im4DeleteRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 29),
    _Ex2im4DeleteRate_Type()
)
ex2im4DeleteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4DeleteRate.setStatus("current")
_Ex2im4DeleteTotal_Type = Gauge32
_Ex2im4DeleteTotal_Object = MibTableColumn
ex2im4DeleteTotal = _Ex2im4DeleteTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 30),
    _Ex2im4DeleteTotal_Type()
)
ex2im4DeleteTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4DeleteTotal.setStatus("current")
_Ex2im4ExamineFailures_Type = Gauge32
_Ex2im4ExamineFailures_Object = MibTableColumn
ex2im4ExamineFailures = _Ex2im4ExamineFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 31),
    _Ex2im4ExamineFailures_Type()
)
ex2im4ExamineFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ExamineFailures.setStatus("current")
_Ex2im4ExamineRate_Type = Gauge32
_Ex2im4ExamineRate_Object = MibTableColumn
ex2im4ExamineRate = _Ex2im4ExamineRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 32),
    _Ex2im4ExamineRate_Type()
)
ex2im4ExamineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ExamineRate.setStatus("current")
_Ex2im4ExamineTotal_Type = Gauge32
_Ex2im4ExamineTotal_Object = MibTableColumn
ex2im4ExamineTotal = _Ex2im4ExamineTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 33),
    _Ex2im4ExamineTotal_Type()
)
ex2im4ExamineTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ExamineTotal.setStatus("current")
_Ex2im4ExpungeFailures_Type = Gauge32
_Ex2im4ExpungeFailures_Object = MibTableColumn
ex2im4ExpungeFailures = _Ex2im4ExpungeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 34),
    _Ex2im4ExpungeFailures_Type()
)
ex2im4ExpungeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ExpungeFailures.setStatus("current")
_Ex2im4ExpungeRate_Type = Gauge32
_Ex2im4ExpungeRate_Object = MibTableColumn
ex2im4ExpungeRate = _Ex2im4ExpungeRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 35),
    _Ex2im4ExpungeRate_Type()
)
ex2im4ExpungeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ExpungeRate.setStatus("current")
_Ex2im4ExpungeTotal_Type = Gauge32
_Ex2im4ExpungeTotal_Object = MibTableColumn
ex2im4ExpungeTotal = _Ex2im4ExpungeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 36),
    _Ex2im4ExpungeTotal_Type()
)
ex2im4ExpungeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ExpungeTotal.setStatus("current")
_Ex2im4FetchFailures_Type = Gauge32
_Ex2im4FetchFailures_Object = MibTableColumn
ex2im4FetchFailures = _Ex2im4FetchFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 37),
    _Ex2im4FetchFailures_Type()
)
ex2im4FetchFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4FetchFailures.setStatus("current")
_Ex2im4FetchRate_Type = Gauge32
_Ex2im4FetchRate_Object = MibTableColumn
ex2im4FetchRate = _Ex2im4FetchRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 38),
    _Ex2im4FetchRate_Type()
)
ex2im4FetchRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4FetchRate.setStatus("current")
_Ex2im4FetchTotal_Type = Gauge32
_Ex2im4FetchTotal_Object = MibTableColumn
ex2im4FetchTotal = _Ex2im4FetchTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 39),
    _Ex2im4FetchTotal_Type()
)
ex2im4FetchTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4FetchTotal.setStatus("current")
_Ex2im4IdleFailures_Type = Gauge32
_Ex2im4IdleFailures_Object = MibTableColumn
ex2im4IdleFailures = _Ex2im4IdleFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 40),
    _Ex2im4IdleFailures_Type()
)
ex2im4IdleFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4IdleFailures.setStatus("current")
_Ex2im4IdleRate_Type = Gauge32
_Ex2im4IdleRate_Object = MibTableColumn
ex2im4IdleRate = _Ex2im4IdleRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 41),
    _Ex2im4IdleRate_Type()
)
ex2im4IdleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4IdleRate.setStatus("current")
_Ex2im4IdleTotal_Type = Gauge32
_Ex2im4IdleTotal_Object = MibTableColumn
ex2im4IdleTotal = _Ex2im4IdleTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 42),
    _Ex2im4IdleTotal_Type()
)
ex2im4IdleTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4IdleTotal.setStatus("current")
_Ex2im4InvalidCommands_Type = Gauge32
_Ex2im4InvalidCommands_Object = MibTableColumn
ex2im4InvalidCommands = _Ex2im4InvalidCommands_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 43),
    _Ex2im4InvalidCommands_Type()
)
ex2im4InvalidCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4InvalidCommands.setStatus("current")
_Ex2im4InvalidCommandsRate_Type = Gauge32
_Ex2im4InvalidCommandsRate_Object = MibTableColumn
ex2im4InvalidCommandsRate = _Ex2im4InvalidCommandsRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 44),
    _Ex2im4InvalidCommandsRate_Type()
)
ex2im4InvalidCommandsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4InvalidCommandsRate.setStatus("current")
_Ex2im4LSUBFailures_Type = Gauge32
_Ex2im4LSUBFailures_Object = MibTableColumn
ex2im4LSUBFailures = _Ex2im4LSUBFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 45),
    _Ex2im4LSUBFailures_Type()
)
ex2im4LSUBFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4LSUBFailures.setStatus("current")
_Ex2im4LSUBRate_Type = Gauge32
_Ex2im4LSUBRate_Object = MibTableColumn
ex2im4LSUBRate = _Ex2im4LSUBRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 46),
    _Ex2im4LSUBRate_Type()
)
ex2im4LSUBRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4LSUBRate.setStatus("current")
_Ex2im4LSUBTotal_Type = Gauge32
_Ex2im4LSUBTotal_Object = MibTableColumn
ex2im4LSUBTotal = _Ex2im4LSUBTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 47),
    _Ex2im4LSUBTotal_Type()
)
ex2im4LSUBTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4LSUBTotal.setStatus("current")
_Ex2im4ListFailures_Type = Gauge32
_Ex2im4ListFailures_Object = MibTableColumn
ex2im4ListFailures = _Ex2im4ListFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 48),
    _Ex2im4ListFailures_Type()
)
ex2im4ListFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ListFailures.setStatus("current")
_Ex2im4ListRate_Type = Gauge32
_Ex2im4ListRate_Object = MibTableColumn
ex2im4ListRate = _Ex2im4ListRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 49),
    _Ex2im4ListRate_Type()
)
ex2im4ListRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ListRate.setStatus("current")
_Ex2im4ListTotal_Type = Gauge32
_Ex2im4ListTotal_Object = MibTableColumn
ex2im4ListTotal = _Ex2im4ListTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 50),
    _Ex2im4ListTotal_Type()
)
ex2im4ListTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4ListTotal.setStatus("current")
_Ex2im4LoginFailures_Type = Gauge32
_Ex2im4LoginFailures_Object = MibTableColumn
ex2im4LoginFailures = _Ex2im4LoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 51),
    _Ex2im4LoginFailures_Type()
)
ex2im4LoginFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4LoginFailures.setStatus("current")
_Ex2im4LoginRate_Type = Gauge32
_Ex2im4LoginRate_Object = MibTableColumn
ex2im4LoginRate = _Ex2im4LoginRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 52),
    _Ex2im4LoginRate_Type()
)
ex2im4LoginRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4LoginRate.setStatus("current")
_Ex2im4LoginTotal_Type = Gauge32
_Ex2im4LoginTotal_Object = MibTableColumn
ex2im4LoginTotal = _Ex2im4LoginTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 53),
    _Ex2im4LoginTotal_Type()
)
ex2im4LoginTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4LoginTotal.setStatus("current")
_Ex2im4LogoutFailures_Type = Gauge32
_Ex2im4LogoutFailures_Object = MibTableColumn
ex2im4LogoutFailures = _Ex2im4LogoutFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 54),
    _Ex2im4LogoutFailures_Type()
)
ex2im4LogoutFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4LogoutFailures.setStatus("current")
_Ex2im4LogoutRate_Type = Gauge32
_Ex2im4LogoutRate_Object = MibTableColumn
ex2im4LogoutRate = _Ex2im4LogoutRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 55),
    _Ex2im4LogoutRate_Type()
)
ex2im4LogoutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4LogoutRate.setStatus("current")
_Ex2im4LogoutTotal_Type = Gauge32
_Ex2im4LogoutTotal_Object = MibTableColumn
ex2im4LogoutTotal = _Ex2im4LogoutTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 56),
    _Ex2im4LogoutTotal_Type()
)
ex2im4LogoutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4LogoutTotal.setStatus("current")
_Ex2im4NOOPFailures_Type = Gauge32
_Ex2im4NOOPFailures_Object = MibTableColumn
ex2im4NOOPFailures = _Ex2im4NOOPFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 57),
    _Ex2im4NOOPFailures_Type()
)
ex2im4NOOPFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4NOOPFailures.setStatus("current")
_Ex2im4NOOPRate_Type = Gauge32
_Ex2im4NOOPRate_Object = MibTableColumn
ex2im4NOOPRate = _Ex2im4NOOPRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 58),
    _Ex2im4NOOPRate_Type()
)
ex2im4NOOPRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4NOOPRate.setStatus("current")
_Ex2im4NOOPTotal_Type = Gauge32
_Ex2im4NOOPTotal_Object = MibTableColumn
ex2im4NOOPTotal = _Ex2im4NOOPTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 59),
    _Ex2im4NOOPTotal_Type()
)
ex2im4NOOPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4NOOPTotal.setStatus("current")
_Ex2im4NamespaceFailures_Type = Gauge32
_Ex2im4NamespaceFailures_Object = MibTableColumn
ex2im4NamespaceFailures = _Ex2im4NamespaceFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 60),
    _Ex2im4NamespaceFailures_Type()
)
ex2im4NamespaceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4NamespaceFailures.setStatus("current")
_Ex2im4NamespaceRate_Type = Gauge32
_Ex2im4NamespaceRate_Object = MibTableColumn
ex2im4NamespaceRate = _Ex2im4NamespaceRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 61),
    _Ex2im4NamespaceRate_Type()
)
ex2im4NamespaceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4NamespaceRate.setStatus("current")
_Ex2im4NamespaceTotal_Type = Gauge32
_Ex2im4NamespaceTotal_Object = MibTableColumn
ex2im4NamespaceTotal = _Ex2im4NamespaceTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 62),
    _Ex2im4NamespaceTotal_Type()
)
ex2im4NamespaceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4NamespaceTotal.setStatus("current")
_Ex2im4RenameFailures_Type = Gauge32
_Ex2im4RenameFailures_Object = MibTableColumn
ex2im4RenameFailures = _Ex2im4RenameFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 63),
    _Ex2im4RenameFailures_Type()
)
ex2im4RenameFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4RenameFailures.setStatus("current")
_Ex2im4RenameRate_Type = Gauge32
_Ex2im4RenameRate_Object = MibTableColumn
ex2im4RenameRate = _Ex2im4RenameRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 64),
    _Ex2im4RenameRate_Type()
)
ex2im4RenameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4RenameRate.setStatus("current")
_Ex2im4RenameTotal_Type = Gauge32
_Ex2im4RenameTotal_Object = MibTableColumn
ex2im4RenameTotal = _Ex2im4RenameTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 65),
    _Ex2im4RenameTotal_Type()
)
ex2im4RenameTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4RenameTotal.setStatus("current")
_Ex2im4SSLConnections_Type = Gauge32
_Ex2im4SSLConnections_Object = MibTableColumn
ex2im4SSLConnections = _Ex2im4SSLConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 66),
    _Ex2im4SSLConnections_Type()
)
ex2im4SSLConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4SSLConnections.setStatus("current")
_Ex2im4STARTTLSFailures_Type = Gauge32
_Ex2im4STARTTLSFailures_Object = MibTableColumn
ex2im4STARTTLSFailures = _Ex2im4STARTTLSFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 67),
    _Ex2im4STARTTLSFailures_Type()
)
ex2im4STARTTLSFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4STARTTLSFailures.setStatus("current")
_Ex2im4STARTTLSRate_Type = Gauge32
_Ex2im4STARTTLSRate_Object = MibTableColumn
ex2im4STARTTLSRate = _Ex2im4STARTTLSRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 68),
    _Ex2im4STARTTLSRate_Type()
)
ex2im4STARTTLSRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4STARTTLSRate.setStatus("current")
_Ex2im4STARTTLSTotal_Type = Gauge32
_Ex2im4STARTTLSTotal_Object = MibTableColumn
ex2im4STARTTLSTotal = _Ex2im4STARTTLSTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 69),
    _Ex2im4STARTTLSTotal_Type()
)
ex2im4STARTTLSTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4STARTTLSTotal.setStatus("current")
_Ex2im4SearchFailures_Type = Gauge32
_Ex2im4SearchFailures_Object = MibTableColumn
ex2im4SearchFailures = _Ex2im4SearchFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 70),
    _Ex2im4SearchFailures_Type()
)
ex2im4SearchFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4SearchFailures.setStatus("current")
_Ex2im4SearchRate_Type = Gauge32
_Ex2im4SearchRate_Object = MibTableColumn
ex2im4SearchRate = _Ex2im4SearchRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 71),
    _Ex2im4SearchRate_Type()
)
ex2im4SearchRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4SearchRate.setStatus("current")
_Ex2im4SearchTotal_Type = Gauge32
_Ex2im4SearchTotal_Object = MibTableColumn
ex2im4SearchTotal = _Ex2im4SearchTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 72),
    _Ex2im4SearchTotal_Type()
)
ex2im4SearchTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4SearchTotal.setStatus("current")
_Ex2im4SelectFailures_Type = Gauge32
_Ex2im4SelectFailures_Object = MibTableColumn
ex2im4SelectFailures = _Ex2im4SelectFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 73),
    _Ex2im4SelectFailures_Type()
)
ex2im4SelectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4SelectFailures.setStatus("current")
_Ex2im4SelectRate_Type = Gauge32
_Ex2im4SelectRate_Object = MibTableColumn
ex2im4SelectRate = _Ex2im4SelectRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 74),
    _Ex2im4SelectRate_Type()
)
ex2im4SelectRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4SelectRate.setStatus("current")
_Ex2im4SelectTotal_Type = Gauge32
_Ex2im4SelectTotal_Object = MibTableColumn
ex2im4SelectTotal = _Ex2im4SelectTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 75),
    _Ex2im4SelectTotal_Type()
)
ex2im4SelectTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4SelectTotal.setStatus("current")
_Ex2im4StatusFailures_Type = Gauge32
_Ex2im4StatusFailures_Object = MibTableColumn
ex2im4StatusFailures = _Ex2im4StatusFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 76),
    _Ex2im4StatusFailures_Type()
)
ex2im4StatusFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4StatusFailures.setStatus("current")
_Ex2im4StatusRate_Type = Gauge32
_Ex2im4StatusRate_Object = MibTableColumn
ex2im4StatusRate = _Ex2im4StatusRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 77),
    _Ex2im4StatusRate_Type()
)
ex2im4StatusRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4StatusRate.setStatus("current")
_Ex2im4StatusTotal_Type = Gauge32
_Ex2im4StatusTotal_Object = MibTableColumn
ex2im4StatusTotal = _Ex2im4StatusTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 78),
    _Ex2im4StatusTotal_Type()
)
ex2im4StatusTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4StatusTotal.setStatus("current")
_Ex2im4StoreFailures_Type = Gauge32
_Ex2im4StoreFailures_Object = MibTableColumn
ex2im4StoreFailures = _Ex2im4StoreFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 79),
    _Ex2im4StoreFailures_Type()
)
ex2im4StoreFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4StoreFailures.setStatus("current")
_Ex2im4StoreRate_Type = Gauge32
_Ex2im4StoreRate_Object = MibTableColumn
ex2im4StoreRate = _Ex2im4StoreRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 80),
    _Ex2im4StoreRate_Type()
)
ex2im4StoreRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4StoreRate.setStatus("current")
_Ex2im4StoreTotal_Type = Gauge32
_Ex2im4StoreTotal_Object = MibTableColumn
ex2im4StoreTotal = _Ex2im4StoreTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 81),
    _Ex2im4StoreTotal_Type()
)
ex2im4StoreTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4StoreTotal.setStatus("current")
_Ex2im4SubscribeFailures_Type = Gauge32
_Ex2im4SubscribeFailures_Object = MibTableColumn
ex2im4SubscribeFailures = _Ex2im4SubscribeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 82),
    _Ex2im4SubscribeFailures_Type()
)
ex2im4SubscribeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4SubscribeFailures.setStatus("current")
_Ex2im4SubscribeRate_Type = Gauge32
_Ex2im4SubscribeRate_Object = MibTableColumn
ex2im4SubscribeRate = _Ex2im4SubscribeRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 83),
    _Ex2im4SubscribeRate_Type()
)
ex2im4SubscribeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4SubscribeRate.setStatus("current")
_Ex2im4SubscribeTotal_Type = Gauge32
_Ex2im4SubscribeTotal_Object = MibTableColumn
ex2im4SubscribeTotal = _Ex2im4SubscribeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 84),
    _Ex2im4SubscribeTotal_Type()
)
ex2im4SubscribeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4SubscribeTotal.setStatus("current")
_Ex2im4TotalConnections_Type = Gauge32
_Ex2im4TotalConnections_Object = MibTableColumn
ex2im4TotalConnections = _Ex2im4TotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 85),
    _Ex2im4TotalConnections_Type()
)
ex2im4TotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4TotalConnections.setStatus("current")
_Ex2im4UnsubscribeFailures_Type = Gauge32
_Ex2im4UnsubscribeFailures_Object = MibTableColumn
ex2im4UnsubscribeFailures = _Ex2im4UnsubscribeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 86),
    _Ex2im4UnsubscribeFailures_Type()
)
ex2im4UnsubscribeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4UnsubscribeFailures.setStatus("current")
_Ex2im4UnsubscribeRate_Type = Gauge32
_Ex2im4UnsubscribeRate_Object = MibTableColumn
ex2im4UnsubscribeRate = _Ex2im4UnsubscribeRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 87),
    _Ex2im4UnsubscribeRate_Type()
)
ex2im4UnsubscribeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4UnsubscribeRate.setStatus("current")
_Ex2im4UnsubscribeTotal_Type = Gauge32
_Ex2im4UnsubscribeTotal_Object = MibTableColumn
ex2im4UnsubscribeTotal = _Ex2im4UnsubscribeTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 49, 1, 88),
    _Ex2im4UnsubscribeTotal_Type()
)
ex2im4UnsubscribeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2im4UnsubscribeTotal.setStatus("current")
_Ex2MailSubmissionTable_Object = MibTable
ex2MailSubmissionTable = _Ex2MailSubmissionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 50)
)
if mibBuilder.loadTexts:
    ex2MailSubmissionTable.setStatus("current")
_Ex2MailSubmissionEntry_Object = MibTableRow
ex2MailSubmissionEntry = _Ex2MailSubmissionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 50, 1)
)
ex2MailSubmissionEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2msInstance"),
)
if mibBuilder.loadTexts:
    ex2MailSubmissionEntry.setStatus("current")
_Ex2msInstance_Type = InstanceName
_Ex2msInstance_Object = MibTableColumn
ex2msInstance = _Ex2msInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 50, 1, 1),
    _Ex2msInstance_Type()
)
ex2msInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2msInstance.setStatus("current")
_Ex2msFailedSubmissions_Type = Gauge32
_Ex2msFailedSubmissions_Object = MibTableColumn
ex2msFailedSubmissions = _Ex2msFailedSubmissions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 50, 1, 2),
    _Ex2msFailedSubmissions_Type()
)
ex2msFailedSubmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2msFailedSubmissions.setStatus("current")
_Ex2msFailedSubmissionsPerSecond_Type = Gauge32
_Ex2msFailedSubmissionsPerSecond_Object = MibTableColumn
ex2msFailedSubmissionsPerSecond = _Ex2msFailedSubmissionsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 50, 1, 3),
    _Ex2msFailedSubmissionsPerSecond_Type()
)
ex2msFailedSubmissionsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2msFailedSubmissionsPerSecond.setStatus("current")
_Ex2msHubServers_Type = Gauge32
_Ex2msHubServers_Object = MibTableColumn
ex2msHubServers = _Ex2msHubServers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 50, 1, 4),
    _Ex2msHubServers_Type()
)
ex2msHubServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2msHubServers.setStatus("current")
_Ex2msHubServersInRetry_Type = Gauge32
_Ex2msHubServersInRetry_Object = MibTableColumn
ex2msHubServersInRetry = _Ex2msHubServersInRetry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 50, 1, 5),
    _Ex2msHubServersInRetry_Type()
)
ex2msHubServersInRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2msHubServersInRetry.setStatus("current")
_Ex2msSuccessfulSubmissions_Type = Gauge32
_Ex2msSuccessfulSubmissions_Object = MibTableColumn
ex2msSuccessfulSubmissions = _Ex2msSuccessfulSubmissions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 50, 1, 6),
    _Ex2msSuccessfulSubmissions_Type()
)
ex2msSuccessfulSubmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2msSuccessfulSubmissions.setStatus("current")
_Ex2msSuccessfulSubmsPerSecond_Type = Gauge32
_Ex2msSuccessfulSubmsPerSecond_Object = MibTableColumn
ex2msSuccessfulSubmsPerSecond = _Ex2msSuccessfulSubmsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 50, 1, 7),
    _Ex2msSuccessfulSubmsPerSecond_Type()
)
ex2msSuccessfulSubmsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2msSuccessfulSubmsPerSecond.setStatus("current")
_Ex2msTemporarySubmissionFailures_Type = Gauge32
_Ex2msTemporarySubmissionFailures_Object = MibTableColumn
ex2msTemporarySubmissionFailures = _Ex2msTemporarySubmissionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 50, 1, 8),
    _Ex2msTemporarySubmissionFailures_Type()
)
ex2msTemporarySubmissionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2msTemporarySubmissionFailures.setStatus("current")
_Ex2msTemporarySubmFailuresPerSec_Type = Gauge32
_Ex2msTemporarySubmFailuresPerSec_Object = MibTableColumn
ex2msTemporarySubmFailuresPerSec = _Ex2msTemporarySubmFailuresPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 50, 1, 9),
    _Ex2msTemporarySubmFailuresPerSec_Type()
)
ex2msTemporarySubmFailuresPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2msTemporarySubmFailuresPerSec.setStatus("current")
_Ex2Pop3Table_Object = MibTable
ex2Pop3Table = _Ex2Pop3Table_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51)
)
if mibBuilder.loadTexts:
    ex2Pop3Table.setStatus("current")
_Ex2Pop3Entry_Object = MibTableRow
ex2Pop3Entry = _Ex2Pop3Entry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1)
)
ex2Pop3Entry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2p3Instance"),
)
if mibBuilder.loadTexts:
    ex2Pop3Entry.setStatus("current")
_Ex2p3Instance_Type = InstanceName
_Ex2p3Instance_Object = MibTableColumn
ex2p3Instance = _Ex2p3Instance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 1),
    _Ex2p3Instance_Type()
)
ex2p3Instance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3Instance.setStatus("current")
_Ex2p3AUTHFailures_Type = Gauge32
_Ex2p3AUTHFailures_Object = MibTableColumn
ex2p3AUTHFailures = _Ex2p3AUTHFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 2),
    _Ex2p3AUTHFailures_Type()
)
ex2p3AUTHFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3AUTHFailures.setStatus("current")
_Ex2p3AUTHRate_Type = Gauge32
_Ex2p3AUTHRate_Object = MibTableColumn
ex2p3AUTHRate = _Ex2p3AUTHRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 3),
    _Ex2p3AUTHRate_Type()
)
ex2p3AUTHRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3AUTHRate.setStatus("current")
_Ex2p3AUTHTotal_Type = Gauge32
_Ex2p3AUTHTotal_Object = MibTableColumn
ex2p3AUTHTotal = _Ex2p3AUTHTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 4),
    _Ex2p3AUTHTotal_Type()
)
ex2p3AUTHTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3AUTHTotal.setStatus("current")
_Ex2p3ActiveSSLConnections_Type = Gauge32
_Ex2p3ActiveSSLConnections_Object = MibTableColumn
ex2p3ActiveSSLConnections = _Ex2p3ActiveSSLConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 5),
    _Ex2p3ActiveSSLConnections_Type()
)
ex2p3ActiveSSLConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3ActiveSSLConnections.setStatus("current")
_Ex2p3AvgComndProcessTimeMillisec_Type = Gauge32
_Ex2p3AvgComndProcessTimeMillisec_Object = MibTableColumn
ex2p3AvgComndProcessTimeMillisec = _Ex2p3AvgComndProcessTimeMillisec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 6),
    _Ex2p3AvgComndProcessTimeMillisec_Type()
)
ex2p3AvgComndProcessTimeMillisec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3AvgComndProcessTimeMillisec.setStatus("current")
_Ex2p3CAPAFailures_Type = Gauge32
_Ex2p3CAPAFailures_Object = MibTableColumn
ex2p3CAPAFailures = _Ex2p3CAPAFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 7),
    _Ex2p3CAPAFailures_Type()
)
ex2p3CAPAFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3CAPAFailures.setStatus("current")
_Ex2p3CAPARate_Type = Gauge32
_Ex2p3CAPARate_Object = MibTableColumn
ex2p3CAPARate = _Ex2p3CAPARate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 8),
    _Ex2p3CAPARate_Type()
)
ex2p3CAPARate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3CAPARate.setStatus("current")
_Ex2p3CAPATotal_Type = Gauge32
_Ex2p3CAPATotal_Object = MibTableColumn
ex2p3CAPATotal = _Ex2p3CAPATotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 9),
    _Ex2p3CAPATotal_Type()
)
ex2p3CAPATotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3CAPATotal.setStatus("current")
_Ex2p3ConnectionsCurrent_Type = Gauge32
_Ex2p3ConnectionsCurrent_Object = MibTableColumn
ex2p3ConnectionsCurrent = _Ex2p3ConnectionsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 10),
    _Ex2p3ConnectionsCurrent_Type()
)
ex2p3ConnectionsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3ConnectionsCurrent.setStatus("current")
_Ex2p3ConnectionsFailed_Type = Gauge32
_Ex2p3ConnectionsFailed_Object = MibTableColumn
ex2p3ConnectionsFailed = _Ex2p3ConnectionsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 11),
    _Ex2p3ConnectionsFailed_Type()
)
ex2p3ConnectionsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3ConnectionsFailed.setStatus("current")
_Ex2p3ConnectionsRejected_Type = Gauge32
_Ex2p3ConnectionsRejected_Object = MibTableColumn
ex2p3ConnectionsRejected = _Ex2p3ConnectionsRejected_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 12),
    _Ex2p3ConnectionsRejected_Type()
)
ex2p3ConnectionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3ConnectionsRejected.setStatus("current")
_Ex2p3ConnectionsTotal_Type = Gauge32
_Ex2p3ConnectionsTotal_Object = MibTableColumn
ex2p3ConnectionsTotal = _Ex2p3ConnectionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 13),
    _Ex2p3ConnectionsTotal_Type()
)
ex2p3ConnectionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3ConnectionsTotal.setStatus("current")
_Ex2p3DELEFailures_Type = Gauge32
_Ex2p3DELEFailures_Object = MibTableColumn
ex2p3DELEFailures = _Ex2p3DELEFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 14),
    _Ex2p3DELEFailures_Type()
)
ex2p3DELEFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3DELEFailures.setStatus("current")
_Ex2p3DELERate_Type = Gauge32
_Ex2p3DELERate_Object = MibTableColumn
ex2p3DELERate = _Ex2p3DELERate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 15),
    _Ex2p3DELERate_Type()
)
ex2p3DELERate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3DELERate.setStatus("current")
_Ex2p3DELETotal_Type = Gauge32
_Ex2p3DELETotal_Object = MibTableColumn
ex2p3DELETotal = _Ex2p3DELETotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 16),
    _Ex2p3DELETotal_Type()
)
ex2p3DELETotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3DELETotal.setStatus("current")
_Ex2p3InvalidCommands_Type = Gauge32
_Ex2p3InvalidCommands_Object = MibTableColumn
ex2p3InvalidCommands = _Ex2p3InvalidCommands_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 17),
    _Ex2p3InvalidCommands_Type()
)
ex2p3InvalidCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3InvalidCommands.setStatus("current")
_Ex2p3InvalidCommandsRate_Type = Gauge32
_Ex2p3InvalidCommandsRate_Object = MibTableColumn
ex2p3InvalidCommandsRate = _Ex2p3InvalidCommandsRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 18),
    _Ex2p3InvalidCommandsRate_Type()
)
ex2p3InvalidCommandsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3InvalidCommandsRate.setStatus("current")
_Ex2p3LISTFailures_Type = Gauge32
_Ex2p3LISTFailures_Object = MibTableColumn
ex2p3LISTFailures = _Ex2p3LISTFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 19),
    _Ex2p3LISTFailures_Type()
)
ex2p3LISTFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3LISTFailures.setStatus("current")
_Ex2p3LISTRate_Type = Gauge32
_Ex2p3LISTRate_Object = MibTableColumn
ex2p3LISTRate = _Ex2p3LISTRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 20),
    _Ex2p3LISTRate_Type()
)
ex2p3LISTRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3LISTRate.setStatus("current")
_Ex2p3LISTTotal_Type = Gauge32
_Ex2p3LISTTotal_Object = MibTableColumn
ex2p3LISTTotal = _Ex2p3LISTTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 21),
    _Ex2p3LISTTotal_Type()
)
ex2p3LISTTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3LISTTotal.setStatus("current")
_Ex2p3NOOPFailures_Type = Gauge32
_Ex2p3NOOPFailures_Object = MibTableColumn
ex2p3NOOPFailures = _Ex2p3NOOPFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 22),
    _Ex2p3NOOPFailures_Type()
)
ex2p3NOOPFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3NOOPFailures.setStatus("current")
_Ex2p3NOOPRate_Type = Gauge32
_Ex2p3NOOPRate_Object = MibTableColumn
ex2p3NOOPRate = _Ex2p3NOOPRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 23),
    _Ex2p3NOOPRate_Type()
)
ex2p3NOOPRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3NOOPRate.setStatus("current")
_Ex2p3NOOPTotal_Type = Gauge32
_Ex2p3NOOPTotal_Object = MibTableColumn
ex2p3NOOPTotal = _Ex2p3NOOPTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 24),
    _Ex2p3NOOPTotal_Type()
)
ex2p3NOOPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3NOOPTotal.setStatus("current")
_Ex2p3PASSFailures_Type = Gauge32
_Ex2p3PASSFailures_Object = MibTableColumn
ex2p3PASSFailures = _Ex2p3PASSFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 25),
    _Ex2p3PASSFailures_Type()
)
ex2p3PASSFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3PASSFailures.setStatus("current")
_Ex2p3PASSRate_Type = Gauge32
_Ex2p3PASSRate_Object = MibTableColumn
ex2p3PASSRate = _Ex2p3PASSRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 26),
    _Ex2p3PASSRate_Type()
)
ex2p3PASSRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3PASSRate.setStatus("current")
_Ex2p3PASSTotal_Type = Gauge32
_Ex2p3PASSTotal_Object = MibTableColumn
ex2p3PASSTotal = _Ex2p3PASSTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 27),
    _Ex2p3PASSTotal_Type()
)
ex2p3PASSTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3PASSTotal.setStatus("current")
_Ex2p3QUITFailures_Type = Gauge32
_Ex2p3QUITFailures_Object = MibTableColumn
ex2p3QUITFailures = _Ex2p3QUITFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 28),
    _Ex2p3QUITFailures_Type()
)
ex2p3QUITFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3QUITFailures.setStatus("current")
_Ex2p3QUITRate_Type = Gauge32
_Ex2p3QUITRate_Object = MibTableColumn
ex2p3QUITRate = _Ex2p3QUITRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 29),
    _Ex2p3QUITRate_Type()
)
ex2p3QUITRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3QUITRate.setStatus("current")
_Ex2p3QUITTotal_Type = Gauge32
_Ex2p3QUITTotal_Object = MibTableColumn
ex2p3QUITTotal = _Ex2p3QUITTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 30),
    _Ex2p3QUITTotal_Type()
)
ex2p3QUITTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3QUITTotal.setStatus("current")
_Ex2p3RETRFailures_Type = Gauge32
_Ex2p3RETRFailures_Object = MibTableColumn
ex2p3RETRFailures = _Ex2p3RETRFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 31),
    _Ex2p3RETRFailures_Type()
)
ex2p3RETRFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3RETRFailures.setStatus("current")
_Ex2p3RETRRate_Type = Gauge32
_Ex2p3RETRRate_Object = MibTableColumn
ex2p3RETRRate = _Ex2p3RETRRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 32),
    _Ex2p3RETRRate_Type()
)
ex2p3RETRRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3RETRRate.setStatus("current")
_Ex2p3RETRTotal_Type = Gauge32
_Ex2p3RETRTotal_Object = MibTableColumn
ex2p3RETRTotal = _Ex2p3RETRTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 33),
    _Ex2p3RETRTotal_Type()
)
ex2p3RETRTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3RETRTotal.setStatus("current")
_Ex2p3RSETFailures_Type = Gauge32
_Ex2p3RSETFailures_Object = MibTableColumn
ex2p3RSETFailures = _Ex2p3RSETFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 34),
    _Ex2p3RSETFailures_Type()
)
ex2p3RSETFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3RSETFailures.setStatus("current")
_Ex2p3RSETRate_Type = Gauge32
_Ex2p3RSETRate_Object = MibTableColumn
ex2p3RSETRate = _Ex2p3RSETRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 35),
    _Ex2p3RSETRate_Type()
)
ex2p3RSETRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3RSETRate.setStatus("current")
_Ex2p3RSETTotal_Type = Gauge32
_Ex2p3RSETTotal_Object = MibTableColumn
ex2p3RSETTotal = _Ex2p3RSETTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 36),
    _Ex2p3RSETTotal_Type()
)
ex2p3RSETTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3RSETTotal.setStatus("current")
_Ex2p3SSLConnections_Type = Gauge32
_Ex2p3SSLConnections_Object = MibTableColumn
ex2p3SSLConnections = _Ex2p3SSLConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 37),
    _Ex2p3SSLConnections_Type()
)
ex2p3SSLConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3SSLConnections.setStatus("current")
_Ex2p3STATFailures_Type = Gauge32
_Ex2p3STATFailures_Object = MibTableColumn
ex2p3STATFailures = _Ex2p3STATFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 38),
    _Ex2p3STATFailures_Type()
)
ex2p3STATFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3STATFailures.setStatus("current")
_Ex2p3STATRate_Type = Gauge32
_Ex2p3STATRate_Object = MibTableColumn
ex2p3STATRate = _Ex2p3STATRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 39),
    _Ex2p3STATRate_Type()
)
ex2p3STATRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3STATRate.setStatus("current")
_Ex2p3STATTotal_Type = Gauge32
_Ex2p3STATTotal_Object = MibTableColumn
ex2p3STATTotal = _Ex2p3STATTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 40),
    _Ex2p3STATTotal_Type()
)
ex2p3STATTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3STATTotal.setStatus("current")
_Ex2p3STLSFailures_Type = Gauge32
_Ex2p3STLSFailures_Object = MibTableColumn
ex2p3STLSFailures = _Ex2p3STLSFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 41),
    _Ex2p3STLSFailures_Type()
)
ex2p3STLSFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3STLSFailures.setStatus("current")
_Ex2p3STLSRate_Type = Gauge32
_Ex2p3STLSRate_Object = MibTableColumn
ex2p3STLSRate = _Ex2p3STLSRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 42),
    _Ex2p3STLSRate_Type()
)
ex2p3STLSRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3STLSRate.setStatus("current")
_Ex2p3STLSTotal_Type = Gauge32
_Ex2p3STLSTotal_Object = MibTableColumn
ex2p3STLSTotal = _Ex2p3STLSTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 43),
    _Ex2p3STLSTotal_Type()
)
ex2p3STLSTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3STLSTotal.setStatus("current")
_Ex2p3TOPFailures_Type = Gauge32
_Ex2p3TOPFailures_Object = MibTableColumn
ex2p3TOPFailures = _Ex2p3TOPFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 44),
    _Ex2p3TOPFailures_Type()
)
ex2p3TOPFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3TOPFailures.setStatus("current")
_Ex2p3TOPRate_Type = Gauge32
_Ex2p3TOPRate_Object = MibTableColumn
ex2p3TOPRate = _Ex2p3TOPRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 45),
    _Ex2p3TOPRate_Type()
)
ex2p3TOPRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3TOPRate.setStatus("current")
_Ex2p3TOPTotal_Type = Gauge32
_Ex2p3TOPTotal_Object = MibTableColumn
ex2p3TOPTotal = _Ex2p3TOPTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 46),
    _Ex2p3TOPTotal_Type()
)
ex2p3TOPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3TOPTotal.setStatus("current")
_Ex2p3UIDLFailures_Type = Gauge32
_Ex2p3UIDLFailures_Object = MibTableColumn
ex2p3UIDLFailures = _Ex2p3UIDLFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 47),
    _Ex2p3UIDLFailures_Type()
)
ex2p3UIDLFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3UIDLFailures.setStatus("current")
_Ex2p3UIDLRate_Type = Gauge32
_Ex2p3UIDLRate_Object = MibTableColumn
ex2p3UIDLRate = _Ex2p3UIDLRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 48),
    _Ex2p3UIDLRate_Type()
)
ex2p3UIDLRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3UIDLRate.setStatus("current")
_Ex2p3UIDLTotal_Type = Gauge32
_Ex2p3UIDLTotal_Object = MibTableColumn
ex2p3UIDLTotal = _Ex2p3UIDLTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 49),
    _Ex2p3UIDLTotal_Type()
)
ex2p3UIDLTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3UIDLTotal.setStatus("current")
_Ex2p3USERFailures_Type = Gauge32
_Ex2p3USERFailures_Object = MibTableColumn
ex2p3USERFailures = _Ex2p3USERFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 50),
    _Ex2p3USERFailures_Type()
)
ex2p3USERFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3USERFailures.setStatus("current")
_Ex2p3USERRate_Type = Gauge32
_Ex2p3USERRate_Object = MibTableColumn
ex2p3USERRate = _Ex2p3USERRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 51),
    _Ex2p3USERRate_Type()
)
ex2p3USERRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3USERRate.setStatus("current")
_Ex2p3USERTotal_Type = Gauge32
_Ex2p3USERTotal_Object = MibTableColumn
ex2p3USERTotal = _Ex2p3USERTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 51, 1, 52),
    _Ex2p3USERTotal_Type()
)
ex2p3USERTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2p3USERTotal.setStatus("current")
_Ex2SANSPIProxy_ObjectIdentity = ObjectIdentity
ex2SANSPIProxy = _Ex2SANSPIProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52)
)
_Ex2SANSPIPBytesTransmittedPerSec_Type = Gauge32
_Ex2SANSPIPBytesTransmittedPerSec_Object = MibScalar
ex2SANSPIPBytesTransmittedPerSec = _Ex2SANSPIPBytesTransmittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 1),
    _Ex2SANSPIPBytesTransmittedPerSec_Type()
)
ex2SANSPIPBytesTransmittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPBytesTransmittedPerSec.setStatus("current")
_Ex2SANSPIPClientConnectionCount_Type = Gauge32
_Ex2SANSPIPClientConnectionCount_Object = MibScalar
ex2SANSPIPClientConnectionCount = _Ex2SANSPIPClientConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 2),
    _Ex2SANSPIPClientConnectionCount_Type()
)
ex2SANSPIPClientConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPClientConnectionCount.setStatus("current")
_Ex2SANSPIPClientConnectionPerSec_Type = Gauge32
_Ex2SANSPIPClientConnectionPerSec_Object = MibScalar
ex2SANSPIPClientConnectionPerSec = _Ex2SANSPIPClientConnectionPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 3),
    _Ex2SANSPIPClientConnectionPerSec_Type()
)
ex2SANSPIPClientConnectionPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPClientConnectionPerSec.setStatus("current")
_Ex2SANSPIPClientDisconnectPerSec_Type = Gauge32
_Ex2SANSPIPClientDisconnectPerSec_Object = MibScalar
ex2SANSPIPClientDisconnectPerSec = _Ex2SANSPIPClientDisconnectPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 4),
    _Ex2SANSPIPClientDisconnectPerSec_Type()
)
ex2SANSPIPClientDisconnectPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPClientDisconnectPerSec.setStatus("current")
_Ex2SANSPIPClientReferrals_Type = Gauge32
_Ex2SANSPIPClientReferrals_Object = MibScalar
ex2SANSPIPClientReferrals = _Ex2SANSPIPClientReferrals_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 5),
    _Ex2SANSPIPClientReferrals_Type()
)
ex2SANSPIPClientReferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPClientReferrals.setStatus("current")
_Ex2SANSPIPClientReferralsPerSec_Type = Gauge32
_Ex2SANSPIPClientReferralsPerSec_Object = MibScalar
ex2SANSPIPClientReferralsPerSec = _Ex2SANSPIPClientReferralsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 6),
    _Ex2SANSPIPClientReferralsPerSec_Type()
)
ex2SANSPIPClientReferralsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPClientReferralsPerSec.setStatus("current")
_Ex2SANSPIPCumulatClientConnCount_Type = Gauge32
_Ex2SANSPIPCumulatClientConnCount_Object = MibScalar
ex2SANSPIPCumulatClientConnCount = _Ex2SANSPIPCumulatClientConnCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 7),
    _Ex2SANSPIPCumulatClientConnCount_Type()
)
ex2SANSPIPCumulatClientConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPCumulatClientConnCount.setStatus("current")
_Ex2SANSPIPFailedClientConnPerSec_Type = Gauge32
_Ex2SANSPIPFailedClientConnPerSec_Object = MibScalar
ex2SANSPIPFailedClientConnPerSec = _Ex2SANSPIPFailedClientConnPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 8),
    _Ex2SANSPIPFailedClientConnPerSec_Type()
)
ex2SANSPIPFailedClientConnPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPFailedClientConnPerSec.setStatus("current")
_Ex2SANSPIPFailedReadsPerSec_Type = Gauge32
_Ex2SANSPIPFailedReadsPerSec_Object = MibScalar
ex2SANSPIPFailedReadsPerSec = _Ex2SANSPIPFailedReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 9),
    _Ex2SANSPIPFailedReadsPerSec_Type()
)
ex2SANSPIPFailedReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPFailedReadsPerSec.setStatus("current")
_Ex2SANSPIPFailedServerConnPerSec_Type = Gauge32
_Ex2SANSPIPFailedServerConnPerSec_Object = MibScalar
ex2SANSPIPFailedServerConnPerSec = _Ex2SANSPIPFailedServerConnPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 10),
    _Ex2SANSPIPFailedServerConnPerSec_Type()
)
ex2SANSPIPFailedServerConnPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPFailedServerConnPerSec.setStatus("current")
_Ex2SANSPIPFailedWritesPerSec_Type = Gauge32
_Ex2SANSPIPFailedWritesPerSec_Object = MibScalar
ex2SANSPIPFailedWritesPerSec = _Ex2SANSPIPFailedWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 11),
    _Ex2SANSPIPFailedWritesPerSec_Type()
)
ex2SANSPIPFailedWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPFailedWritesPerSec.setStatus("current")
_Ex2SANSPIPPacketsTransmittPerSec_Type = Gauge32
_Ex2SANSPIPPacketsTransmittPerSec_Object = MibScalar
ex2SANSPIPPacketsTransmittPerSec = _Ex2SANSPIPPacketsTransmittPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 12),
    _Ex2SANSPIPPacketsTransmittPerSec_Type()
)
ex2SANSPIPPacketsTransmittPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPPacketsTransmittPerSec.setStatus("current")
_Ex2SANSPIPPeakClientConnections_Type = Gauge32
_Ex2SANSPIPPeakClientConnections_Object = MibScalar
ex2SANSPIPPeakClientConnections = _Ex2SANSPIPPeakClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 13),
    _Ex2SANSPIPPeakClientConnections_Type()
)
ex2SANSPIPPeakClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPPeakClientConnections.setStatus("current")
_Ex2SANSPIPPeakWorkerThreads_Type = Gauge32
_Ex2SANSPIPPeakWorkerThreads_Object = MibScalar
ex2SANSPIPPeakWorkerThreads = _Ex2SANSPIPPeakWorkerThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 14),
    _Ex2SANSPIPPeakWorkerThreads_Type()
)
ex2SANSPIPPeakWorkerThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPPeakWorkerThreads.setStatus("current")
_Ex2SANSPIPTotalFailedClientConns_Type = Gauge32
_Ex2SANSPIPTotalFailedClientConns_Object = MibScalar
ex2SANSPIPTotalFailedClientConns = _Ex2SANSPIPTotalFailedClientConns_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 15),
    _Ex2SANSPIPTotalFailedClientConns_Type()
)
ex2SANSPIPTotalFailedClientConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPTotalFailedClientConns.setStatus("current")
_Ex2SANSPIPTotalFailedReads_Type = Gauge32
_Ex2SANSPIPTotalFailedReads_Object = MibScalar
ex2SANSPIPTotalFailedReads = _Ex2SANSPIPTotalFailedReads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 16),
    _Ex2SANSPIPTotalFailedReads_Type()
)
ex2SANSPIPTotalFailedReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPTotalFailedReads.setStatus("current")
_Ex2SANSPIPTotalFailedServerConns_Type = Gauge32
_Ex2SANSPIPTotalFailedServerConns_Object = MibScalar
ex2SANSPIPTotalFailedServerConns = _Ex2SANSPIPTotalFailedServerConns_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 17),
    _Ex2SANSPIPTotalFailedServerConns_Type()
)
ex2SANSPIPTotalFailedServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPTotalFailedServerConns.setStatus("current")
_Ex2SANSPIPTotalFailedWrites_Type = Gauge32
_Ex2SANSPIPTotalFailedWrites_Object = MibScalar
ex2SANSPIPTotalFailedWrites = _Ex2SANSPIPTotalFailedWrites_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 18),
    _Ex2SANSPIPTotalFailedWrites_Type()
)
ex2SANSPIPTotalFailedWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPTotalFailedWrites.setStatus("current")
_Ex2SANSPIPWorkerThreadsInUse_Type = Gauge32
_Ex2SANSPIPWorkerThreadsInUse_Object = MibScalar
ex2SANSPIPWorkerThreadsInUse = _Ex2SANSPIPWorkerThreadsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 52, 19),
    _Ex2SANSPIPWorkerThreadsInUse_Type()
)
ex2SANSPIPWorkerThreadsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2SANSPIPWorkerThreadsInUse.setStatus("current")
_Ex2TransportBatchPointTable_Object = MibTable
ex2TransportBatchPointTable = _Ex2TransportBatchPointTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53)
)
if mibBuilder.loadTexts:
    ex2TransportBatchPointTable.setStatus("current")
_Ex2TransportBatchPointEntry_Object = MibTableRow
ex2TransportBatchPointEntry = _Ex2TransportBatchPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1)
)
ex2TransportBatchPointEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2tbpInstance"),
)
if mibBuilder.loadTexts:
    ex2TransportBatchPointEntry.setStatus("current")
_Ex2tbpInstance_Type = InstanceName
_Ex2tbpInstance_Object = MibTableColumn
ex2tbpInstance = _Ex2tbpInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 1),
    _Ex2tbpInstance_Type()
)
ex2tbpInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpInstance.setStatus("current")
_Ex2tbpBatchSizeExecutedTotal_Type = Gauge32
_Ex2tbpBatchSizeExecutedTotal_Object = MibTableColumn
ex2tbpBatchSizeExecutedTotal = _Ex2tbpBatchSizeExecutedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 2),
    _Ex2tbpBatchSizeExecutedTotal_Type()
)
ex2tbpBatchSizeExecutedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchSizeExecutedTotal.setStatus("current")
_Ex2tbpBatchSizeExecutedPerSec_Type = Gauge32
_Ex2tbpBatchSizeExecutedPerSec_Object = MibTableColumn
ex2tbpBatchSizeExecutedPerSec = _Ex2tbpBatchSizeExecutedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 3),
    _Ex2tbpBatchSizeExecutedPerSec_Type()
)
ex2tbpBatchSizeExecutedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchSizeExecutedPerSec.setStatus("current")
_Ex2tbpBatchesExecBackgroundTotal_Type = Gauge32
_Ex2tbpBatchesExecBackgroundTotal_Object = MibTableColumn
ex2tbpBatchesExecBackgroundTotal = _Ex2tbpBatchesExecBackgroundTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 4),
    _Ex2tbpBatchesExecBackgroundTotal_Type()
)
ex2tbpBatchesExecBackgroundTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesExecBackgroundTotal.setStatus("current")
_Ex2tbpBatchesExecBackgroundPrSec_Type = Gauge32
_Ex2tbpBatchesExecBackgroundPrSec_Object = MibTableColumn
ex2tbpBatchesExecBackgroundPrSec = _Ex2tbpBatchesExecBackgroundPrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 5),
    _Ex2tbpBatchesExecBackgroundPrSec_Type()
)
ex2tbpBatchesExecBackgroundPrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesExecBackgroundPrSec.setStatus("current")
_Ex2tbpBatchesExecutedNormalTotal_Type = Gauge32
_Ex2tbpBatchesExecutedNormalTotal_Object = MibTableColumn
ex2tbpBatchesExecutedNormalTotal = _Ex2tbpBatchesExecutedNormalTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 6),
    _Ex2tbpBatchesExecutedNormalTotal_Type()
)
ex2tbpBatchesExecutedNormalTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesExecutedNormalTotal.setStatus("current")
_Ex2tbpBatcheExecutedNormalPerSec_Type = Gauge32
_Ex2tbpBatcheExecutedNormalPerSec_Object = MibTableColumn
ex2tbpBatcheExecutedNormalPerSec = _Ex2tbpBatcheExecutedNormalPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 7),
    _Ex2tbpBatcheExecutedNormalPerSec_Type()
)
ex2tbpBatcheExecutedNormalPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatcheExecutedNormalPerSec.setStatus("current")
_Ex2tbpBatchesExecutedTotal_Type = Gauge32
_Ex2tbpBatchesExecutedTotal_Object = MibTableColumn
ex2tbpBatchesExecutedTotal = _Ex2tbpBatchesExecutedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 8),
    _Ex2tbpBatchesExecutedTotal_Type()
)
ex2tbpBatchesExecutedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesExecutedTotal.setStatus("current")
_Ex2tbpBatchesExecutedPerSec_Type = Gauge32
_Ex2tbpBatchesExecutedPerSec_Object = MibTableColumn
ex2tbpBatchesExecutedPerSec = _Ex2tbpBatchesExecutedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 9),
    _Ex2tbpBatchesExecutedPerSec_Type()
)
ex2tbpBatchesExecutedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesExecutedPerSec.setStatus("current")
_Ex2tbpBatchesPendingTotal_Type = Gauge32
_Ex2tbpBatchesPendingTotal_Object = MibTableColumn
ex2tbpBatchesPendingTotal = _Ex2tbpBatchesPendingTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 10),
    _Ex2tbpBatchesPendingTotal_Type()
)
ex2tbpBatchesPendingTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesPendingTotal.setStatus("current")
_Ex2tbpBatchesPendingPerSec_Type = Gauge32
_Ex2tbpBatchesPendingPerSec_Object = MibTableColumn
ex2tbpBatchesPendingPerSec = _Ex2tbpBatchesPendingPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 11),
    _Ex2tbpBatchesPendingPerSec_Type()
)
ex2tbpBatchesPendingPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesPendingPerSec.setStatus("current")
_Ex2tbpBatchesTimedOutTotal_Type = Gauge32
_Ex2tbpBatchesTimedOutTotal_Object = MibTableColumn
ex2tbpBatchesTimedOutTotal = _Ex2tbpBatchesTimedOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 12),
    _Ex2tbpBatchesTimedOutTotal_Type()
)
ex2tbpBatchesTimedOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesTimedOutTotal.setStatus("current")
_Ex2tbpBatchesTimedOutPerSec_Type = Gauge32
_Ex2tbpBatchesTimedOutPerSec_Object = MibTableColumn
ex2tbpBatchesTimedOutPerSec = _Ex2tbpBatchesTimedOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 13),
    _Ex2tbpBatchesTimedOutPerSec_Type()
)
ex2tbpBatchesTimedOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesTimedOutPerSec.setStatus("current")
_Ex2tbpBatchesWaitingCurrent_Type = Gauge32
_Ex2tbpBatchesWaitingCurrent_Object = MibTableColumn
ex2tbpBatchesWaitingCurrent = _Ex2tbpBatchesWaitingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 14),
    _Ex2tbpBatchesWaitingCurrent_Type()
)
ex2tbpBatchesWaitingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesWaitingCurrent.setStatus("current")
_Ex2tbpBatchesWaitingTotal_Type = Gauge32
_Ex2tbpBatchesWaitingTotal_Object = MibTableColumn
ex2tbpBatchesWaitingTotal = _Ex2tbpBatchesWaitingTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 15),
    _Ex2tbpBatchesWaitingTotal_Type()
)
ex2tbpBatchesWaitingTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesWaitingTotal.setStatus("current")
_Ex2tbpBatchesWaitingPerSec_Type = Gauge32
_Ex2tbpBatchesWaitingPerSec_Object = MibTableColumn
ex2tbpBatchesWaitingPerSec = _Ex2tbpBatchesWaitingPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 16),
    _Ex2tbpBatchesWaitingPerSec_Type()
)
ex2tbpBatchesWaitingPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpBatchesWaitingPerSec.setStatus("current")
_Ex2tbpCursorsClosedTotal_Type = Gauge32
_Ex2tbpCursorsClosedTotal_Object = MibTableColumn
ex2tbpCursorsClosedTotal = _Ex2tbpCursorsClosedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 17),
    _Ex2tbpCursorsClosedTotal_Type()
)
ex2tbpCursorsClosedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpCursorsClosedTotal.setStatus("current")
_Ex2tbpCursorsClosedPerSec_Type = Gauge32
_Ex2tbpCursorsClosedPerSec_Object = MibTableColumn
ex2tbpCursorsClosedPerSec = _Ex2tbpCursorsClosedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 18),
    _Ex2tbpCursorsClosedPerSec_Type()
)
ex2tbpCursorsClosedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpCursorsClosedPerSec.setStatus("current")
_Ex2tbpCursorsOpenedTotal_Type = Gauge32
_Ex2tbpCursorsOpenedTotal_Object = MibTableColumn
ex2tbpCursorsOpenedTotal = _Ex2tbpCursorsOpenedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 19),
    _Ex2tbpCursorsOpenedTotal_Type()
)
ex2tbpCursorsOpenedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpCursorsOpenedTotal.setStatus("current")
_Ex2tbpCursorsOpenedPerSec_Type = Gauge32
_Ex2tbpCursorsOpenedPerSec_Object = MibTableColumn
ex2tbpCursorsOpenedPerSec = _Ex2tbpCursorsOpenedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 20),
    _Ex2tbpCursorsOpenedPerSec_Type()
)
ex2tbpCursorsOpenedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpCursorsOpenedPerSec.setStatus("current")
_Ex2tbpDatabaseConnectionsCurrent_Type = Gauge32
_Ex2tbpDatabaseConnectionsCurrent_Object = MibTableColumn
ex2tbpDatabaseConnectionsCurrent = _Ex2tbpDatabaseConnectionsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 21),
    _Ex2tbpDatabaseConnectionsCurrent_Type()
)
ex2tbpDatabaseConnectionsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpDatabaseConnectionsCurrent.setStatus("current")
_Ex2tbpDatabaseConnsRejectedTotal_Type = Gauge32
_Ex2tbpDatabaseConnsRejectedTotal_Object = MibTableColumn
ex2tbpDatabaseConnsRejectedTotal = _Ex2tbpDatabaseConnsRejectedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 22),
    _Ex2tbpDatabaseConnsRejectedTotal_Type()
)
ex2tbpDatabaseConnsRejectedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpDatabaseConnsRejectedTotal.setStatus("current")
_Ex2tbpDatabaseConnsRejectdPerSec_Type = Gauge32
_Ex2tbpDatabaseConnsRejectdPerSec_Object = MibTableColumn
ex2tbpDatabaseConnsRejectdPerSec = _Ex2tbpDatabaseConnsRejectdPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 23),
    _Ex2tbpDatabaseConnsRejectdPerSec_Type()
)
ex2tbpDatabaseConnsRejectdPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpDatabaseConnsRejectdPerSec.setStatus("current")
_Ex2tbpTransactionsAbortedTotal_Type = Gauge32
_Ex2tbpTransactionsAbortedTotal_Object = MibTableColumn
ex2tbpTransactionsAbortedTotal = _Ex2tbpTransactionsAbortedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 24),
    _Ex2tbpTransactionsAbortedTotal_Type()
)
ex2tbpTransactionsAbortedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpTransactionsAbortedTotal.setStatus("current")
_Ex2tbpTransactionsAbortedPerSec_Type = Gauge32
_Ex2tbpTransactionsAbortedPerSec_Object = MibTableColumn
ex2tbpTransactionsAbortedPerSec = _Ex2tbpTransactionsAbortedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 25),
    _Ex2tbpTransactionsAbortedPerSec_Type()
)
ex2tbpTransactionsAbortedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpTransactionsAbortedPerSec.setStatus("current")
_Ex2tbpTransactionsCommittedTotal_Type = Gauge32
_Ex2tbpTransactionsCommittedTotal_Object = MibTableColumn
ex2tbpTransactionsCommittedTotal = _Ex2tbpTransactionsCommittedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 26),
    _Ex2tbpTransactionsCommittedTotal_Type()
)
ex2tbpTransactionsCommittedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpTransactionsCommittedTotal.setStatus("current")
_Ex2tbpTransactionCommittedPerSec_Type = Gauge32
_Ex2tbpTransactionCommittedPerSec_Object = MibTableColumn
ex2tbpTransactionCommittedPerSec = _Ex2tbpTransactionCommittedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 53, 1, 27),
    _Ex2tbpTransactionCommittedPerSec_Type()
)
ex2tbpTransactionCommittedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbpTransactionCommittedPerSec.setStatus("current")
_Ex2TransportDSNTable_Object = MibTable
ex2TransportDSNTable = _Ex2TransportDSNTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 54)
)
if mibBuilder.loadTexts:
    ex2TransportDSNTable.setStatus("current")
_Ex2TransportDSNEntry_Object = MibTableRow
ex2TransportDSNEntry = _Ex2TransportDSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 54, 1)
)
ex2TransportDSNEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2tdsnInstance"),
)
if mibBuilder.loadTexts:
    ex2TransportDSNEntry.setStatus("current")
_Ex2tdsnInstance_Type = InstanceName
_Ex2tdsnInstance_Object = MibTableColumn
ex2tdsnInstance = _Ex2tdsnInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 54, 1, 1),
    _Ex2tdsnInstance_Type()
)
ex2tdsnInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tdsnInstance.setStatus("current")
_Ex2tdsnDelayDSNs_Type = Gauge32
_Ex2tdsnDelayDSNs_Object = MibTableColumn
ex2tdsnDelayDSNs = _Ex2tdsnDelayDSNs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 54, 1, 2),
    _Ex2tdsnDelayDSNs_Type()
)
ex2tdsnDelayDSNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tdsnDelayDSNs.setStatus("current")
_Ex2tdsnDeliveredDSNs_Type = Gauge32
_Ex2tdsnDeliveredDSNs_Object = MibTableColumn
ex2tdsnDeliveredDSNs = _Ex2tdsnDeliveredDSNs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 54, 1, 3),
    _Ex2tdsnDeliveredDSNs_Type()
)
ex2tdsnDeliveredDSNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tdsnDeliveredDSNs.setStatus("current")
_Ex2tdsnExpandedDSNs_Type = Gauge32
_Ex2tdsnExpandedDSNs_Object = MibTableColumn
ex2tdsnExpandedDSNs = _Ex2tdsnExpandedDSNs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 54, 1, 4),
    _Ex2tdsnExpandedDSNs_Type()
)
ex2tdsnExpandedDSNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tdsnExpandedDSNs.setStatus("current")
_Ex2tdsnFailureDSNsTotal_Type = Gauge32
_Ex2tdsnFailureDSNsTotal_Object = MibTableColumn
ex2tdsnFailureDSNsTotal = _Ex2tdsnFailureDSNsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 54, 1, 5),
    _Ex2tdsnFailureDSNsTotal_Type()
)
ex2tdsnFailureDSNsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tdsnFailureDSNsTotal.setStatus("current")
_Ex2tdsnRelayDSNs_Type = Gauge32
_Ex2tdsnRelayDSNs_Object = MibTableColumn
ex2tdsnRelayDSNs = _Ex2tdsnRelayDSNs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 54, 1, 6),
    _Ex2tdsnRelayDSNs_Type()
)
ex2tdsnRelayDSNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tdsnRelayDSNs.setStatus("current")
_Ex2TransportDatabaseTable_Object = MibTable
ex2TransportDatabaseTable = _Ex2TransportDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55)
)
if mibBuilder.loadTexts:
    ex2TransportDatabaseTable.setStatus("current")
_Ex2TransportDatabaseEntry_Object = MibTableRow
ex2TransportDatabaseEntry = _Ex2TransportDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1)
)
ex2TransportDatabaseEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2tbInstance"),
)
if mibBuilder.loadTexts:
    ex2TransportDatabaseEntry.setStatus("current")
_Ex2tbInstance_Type = InstanceName
_Ex2tbInstance_Object = MibTableColumn
ex2tbInstance = _Ex2tbInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 1),
    _Ex2tbInstance_Type()
)
ex2tbInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbInstance.setStatus("current")
_Ex2tbColumCacheLoadTotal_Type = Gauge32
_Ex2tbColumCacheLoadTotal_Object = MibTableColumn
ex2tbColumCacheLoadTotal = _Ex2tbColumCacheLoadTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 2),
    _Ex2tbColumCacheLoadTotal_Type()
)
ex2tbColumCacheLoadTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumCacheLoadTotal.setStatus("current")
_Ex2tbColumCacheLoadPerSec_Type = Gauge32
_Ex2tbColumCacheLoadPerSec_Object = MibTableColumn
ex2tbColumCacheLoadPerSec = _Ex2tbColumCacheLoadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 3),
    _Ex2tbColumCacheLoadPerSec_Type()
)
ex2tbColumCacheLoadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumCacheLoadPerSec.setStatus("current")
_Ex2tbColumCacheSaveTotal_Type = Gauge32
_Ex2tbColumCacheSaveTotal_Object = MibTableColumn
ex2tbColumCacheSaveTotal = _Ex2tbColumCacheSaveTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 4),
    _Ex2tbColumCacheSaveTotal_Type()
)
ex2tbColumCacheSaveTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumCacheSaveTotal.setStatus("current")
_Ex2tbColumCacheSavePerSec_Type = Gauge32
_Ex2tbColumCacheSavePerSec_Object = MibTableColumn
ex2tbColumCacheSavePerSec = _Ex2tbColumCacheSavePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 5),
    _Ex2tbColumCacheSavePerSec_Type()
)
ex2tbColumCacheSavePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumCacheSavePerSec.setStatus("current")
_Ex2tbColumnCacheLoadedBytesTotal_Type = Gauge32
_Ex2tbColumnCacheLoadedBytesTotal_Object = MibTableColumn
ex2tbColumnCacheLoadedBytesTotal = _Ex2tbColumnCacheLoadedBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 6),
    _Ex2tbColumnCacheLoadedBytesTotal_Type()
)
ex2tbColumnCacheLoadedBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumnCacheLoadedBytesTotal.setStatus("current")
_Ex2tbColumnCachLoadedBytesPerSec_Type = Gauge32
_Ex2tbColumnCachLoadedBytesPerSec_Object = MibTableColumn
ex2tbColumnCachLoadedBytesPerSec = _Ex2tbColumnCachLoadedBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 7),
    _Ex2tbColumnCachLoadedBytesPerSec_Type()
)
ex2tbColumnCachLoadedBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumnCachLoadedBytesPerSec.setStatus("current")
_Ex2tbColumnCacheLoadColumnsTotal_Type = Gauge32
_Ex2tbColumnCacheLoadColumnsTotal_Object = MibTableColumn
ex2tbColumnCacheLoadColumnsTotal = _Ex2tbColumnCacheLoadColumnsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 8),
    _Ex2tbColumnCacheLoadColumnsTotal_Type()
)
ex2tbColumnCacheLoadColumnsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumnCacheLoadColumnsTotal.setStatus("current")
_Ex2tbColumnCacheLoadedColumnsSec_Type = Gauge32
_Ex2tbColumnCacheLoadedColumnsSec_Object = MibTableColumn
ex2tbColumnCacheLoadedColumnsSec = _Ex2tbColumnCacheLoadedColumnsSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 9),
    _Ex2tbColumnCacheLoadedColumnsSec_Type()
)
ex2tbColumnCacheLoadedColumnsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumnCacheLoadedColumnsSec.setStatus("current")
_Ex2tbColumnCacheSavedBytesTotal_Type = Gauge32
_Ex2tbColumnCacheSavedBytesTotal_Object = MibTableColumn
ex2tbColumnCacheSavedBytesTotal = _Ex2tbColumnCacheSavedBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 10),
    _Ex2tbColumnCacheSavedBytesTotal_Type()
)
ex2tbColumnCacheSavedBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumnCacheSavedBytesTotal.setStatus("current")
_Ex2tbColumnCacheSavedBytesPerSec_Type = Gauge32
_Ex2tbColumnCacheSavedBytesPerSec_Object = MibTableColumn
ex2tbColumnCacheSavedBytesPerSec = _Ex2tbColumnCacheSavedBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 11),
    _Ex2tbColumnCacheSavedBytesPerSec_Type()
)
ex2tbColumnCacheSavedBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumnCacheSavedBytesPerSec.setStatus("current")
_Ex2tbColumnCacheSavedColumnTotal_Type = Gauge32
_Ex2tbColumnCacheSavedColumnTotal_Object = MibTableColumn
ex2tbColumnCacheSavedColumnTotal = _Ex2tbColumnCacheSavedColumnTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 12),
    _Ex2tbColumnCacheSavedColumnTotal_Type()
)
ex2tbColumnCacheSavedColumnTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumnCacheSavedColumnTotal.setStatus("current")
_Ex2tbColumnCacheSaveColumnPerSec_Type = Gauge32
_Ex2tbColumnCacheSaveColumnPerSec_Object = MibTableColumn
ex2tbColumnCacheSaveColumnPerSec = _Ex2tbColumnCacheSaveColumnPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 13),
    _Ex2tbColumnCacheSaveColumnPerSec_Type()
)
ex2tbColumnCacheSaveColumnPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbColumnCacheSaveColumnPerSec.setStatus("current")
_Ex2tbDataRowClonesTotal_Type = Gauge32
_Ex2tbDataRowClonesTotal_Object = MibTableColumn
ex2tbDataRowClonesTotal = _Ex2tbDataRowClonesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 14),
    _Ex2tbDataRowClonesTotal_Type()
)
ex2tbDataRowClonesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowClonesTotal.setStatus("current")
_Ex2tbDataRowClonesPerSec_Type = Gauge32
_Ex2tbDataRowClonesPerSec_Object = MibTableColumn
ex2tbDataRowClonesPerSec = _Ex2tbDataRowClonesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 15),
    _Ex2tbDataRowClonesPerSec_Type()
)
ex2tbDataRowClonesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowClonesPerSec.setStatus("current")
_Ex2tbDataRowDeletesTotal_Type = Gauge32
_Ex2tbDataRowDeletesTotal_Object = MibTableColumn
ex2tbDataRowDeletesTotal = _Ex2tbDataRowDeletesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 16),
    _Ex2tbDataRowDeletesTotal_Type()
)
ex2tbDataRowDeletesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowDeletesTotal.setStatus("current")
_Ex2tbDataRowDeletesPerSec_Type = Gauge32
_Ex2tbDataRowDeletesPerSec_Object = MibTableColumn
ex2tbDataRowDeletesPerSec = _Ex2tbDataRowDeletesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 17),
    _Ex2tbDataRowDeletesPerSec_Type()
)
ex2tbDataRowDeletesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowDeletesPerSec.setStatus("current")
_Ex2tbDataRowLoadsTotal_Type = Gauge32
_Ex2tbDataRowLoadsTotal_Object = MibTableColumn
ex2tbDataRowLoadsTotal = _Ex2tbDataRowLoadsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 18),
    _Ex2tbDataRowLoadsTotal_Type()
)
ex2tbDataRowLoadsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowLoadsTotal.setStatus("current")
_Ex2tbDataRowLoadsPerSec_Type = Gauge32
_Ex2tbDataRowLoadsPerSec_Object = MibTableColumn
ex2tbDataRowLoadsPerSec = _Ex2tbDataRowLoadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 19),
    _Ex2tbDataRowLoadsPerSec_Type()
)
ex2tbDataRowLoadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowLoadsPerSec.setStatus("current")
_Ex2tbDataRowMinimizeMemoryTotal_Type = Gauge32
_Ex2tbDataRowMinimizeMemoryTotal_Object = MibTableColumn
ex2tbDataRowMinimizeMemoryTotal = _Ex2tbDataRowMinimizeMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 20),
    _Ex2tbDataRowMinimizeMemoryTotal_Type()
)
ex2tbDataRowMinimizeMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowMinimizeMemoryTotal.setStatus("current")
_Ex2tbDataRowMinimizeMemoryPerSec_Type = Gauge32
_Ex2tbDataRowMinimizeMemoryPerSec_Object = MibTableColumn
ex2tbDataRowMinimizeMemoryPerSec = _Ex2tbDataRowMinimizeMemoryPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 21),
    _Ex2tbDataRowMinimizeMemoryPerSec_Type()
)
ex2tbDataRowMinimizeMemoryPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowMinimizeMemoryPerSec.setStatus("current")
_Ex2tbDataRowMovesTotal_Type = Gauge32
_Ex2tbDataRowMovesTotal_Object = MibTableColumn
ex2tbDataRowMovesTotal = _Ex2tbDataRowMovesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 22),
    _Ex2tbDataRowMovesTotal_Type()
)
ex2tbDataRowMovesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowMovesTotal.setStatus("current")
_Ex2tbDataRowMovesPerSec_Type = Gauge32
_Ex2tbDataRowMovesPerSec_Object = MibTableColumn
ex2tbDataRowMovesPerSec = _Ex2tbDataRowMovesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 23),
    _Ex2tbDataRowMovesPerSec_Type()
)
ex2tbDataRowMovesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowMovesPerSec.setStatus("current")
_Ex2tbDataRowNewInsertsTotal_Type = Gauge32
_Ex2tbDataRowNewInsertsTotal_Object = MibTableColumn
ex2tbDataRowNewInsertsTotal = _Ex2tbDataRowNewInsertsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 24),
    _Ex2tbDataRowNewInsertsTotal_Type()
)
ex2tbDataRowNewInsertsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowNewInsertsTotal.setStatus("current")
_Ex2tbDataRowNewInsertsPerSec_Type = Gauge32
_Ex2tbDataRowNewInsertsPerSec_Object = MibTableColumn
ex2tbDataRowNewInsertsPerSec = _Ex2tbDataRowNewInsertsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 25),
    _Ex2tbDataRowNewInsertsPerSec_Type()
)
ex2tbDataRowNewInsertsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowNewInsertsPerSec.setStatus("current")
_Ex2tbDataRowSeeksPrefixTotal_Type = Gauge32
_Ex2tbDataRowSeeksPrefixTotal_Object = MibTableColumn
ex2tbDataRowSeeksPrefixTotal = _Ex2tbDataRowSeeksPrefixTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 26),
    _Ex2tbDataRowSeeksPrefixTotal_Type()
)
ex2tbDataRowSeeksPrefixTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowSeeksPrefixTotal.setStatus("current")
_Ex2tbDataRowSeeksPrefixPerSec_Type = Gauge32
_Ex2tbDataRowSeeksPrefixPerSec_Object = MibTableColumn
ex2tbDataRowSeeksPrefixPerSec = _Ex2tbDataRowSeeksPrefixPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 27),
    _Ex2tbDataRowSeeksPrefixPerSec_Type()
)
ex2tbDataRowSeeksPrefixPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowSeeksPrefixPerSec.setStatus("current")
_Ex2tbDataRowSeeksTotal_Type = Gauge32
_Ex2tbDataRowSeeksTotal_Object = MibTableColumn
ex2tbDataRowSeeksTotal = _Ex2tbDataRowSeeksTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 28),
    _Ex2tbDataRowSeeksTotal_Type()
)
ex2tbDataRowSeeksTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowSeeksTotal.setStatus("current")
_Ex2tbDataRowSeeksPerSec_Type = Gauge32
_Ex2tbDataRowSeeksPerSec_Object = MibTableColumn
ex2tbDataRowSeeksPerSec = _Ex2tbDataRowSeeksPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 29),
    _Ex2tbDataRowSeeksPerSec_Type()
)
ex2tbDataRowSeeksPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowSeeksPerSec.setStatus("current")
_Ex2tbDataRowUpdatesTotal_Type = Gauge32
_Ex2tbDataRowUpdatesTotal_Object = MibTableColumn
ex2tbDataRowUpdatesTotal = _Ex2tbDataRowUpdatesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 30),
    _Ex2tbDataRowUpdatesTotal_Type()
)
ex2tbDataRowUpdatesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowUpdatesTotal.setStatus("current")
_Ex2tbDataRowUpdatesPerSec_Type = Gauge32
_Ex2tbDataRowUpdatesPerSec_Object = MibTableColumn
ex2tbDataRowUpdatesPerSec = _Ex2tbDataRowUpdatesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 31),
    _Ex2tbDataRowUpdatesPerSec_Type()
)
ex2tbDataRowUpdatesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbDataRowUpdatesPerSec.setStatus("current")
_Ex2tbExtendPropertyByteReadTotal_Type = Gauge32
_Ex2tbExtendPropertyByteReadTotal_Object = MibTableColumn
ex2tbExtendPropertyByteReadTotal = _Ex2tbExtendPropertyByteReadTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 32),
    _Ex2tbExtendPropertyByteReadTotal_Type()
)
ex2tbExtendPropertyByteReadTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbExtendPropertyByteReadTotal.setStatus("current")
_Ex2tbExtendPropertyBytReadPerSec_Type = Gauge32
_Ex2tbExtendPropertyBytReadPerSec_Object = MibTableColumn
ex2tbExtendPropertyBytReadPerSec = _Ex2tbExtendPropertyBytReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 33),
    _Ex2tbExtendPropertyBytReadPerSec_Type()
)
ex2tbExtendPropertyBytReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbExtendPropertyBytReadPerSec.setStatus("current")
_Ex2tbExtenePropertyByteWritTotal_Type = Gauge32
_Ex2tbExtenePropertyByteWritTotal_Object = MibTableColumn
ex2tbExtenePropertyByteWritTotal = _Ex2tbExtenePropertyByteWritTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 34),
    _Ex2tbExtenePropertyByteWritTotal_Type()
)
ex2tbExtenePropertyByteWritTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbExtenePropertyByteWritTotal.setStatus("current")
_Ex2tbExtenPropertyByteWritPerSec_Type = Gauge32
_Ex2tbExtenPropertyByteWritPerSec_Object = MibTableColumn
ex2tbExtenPropertyByteWritPerSec = _Ex2tbExtenPropertyByteWritPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 35),
    _Ex2tbExtenPropertyByteWritPerSec_Type()
)
ex2tbExtenPropertyByteWritPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbExtenPropertyByteWritPerSec.setStatus("current")
_Ex2tbExtenedPropertyReadsTotal_Type = Gauge32
_Ex2tbExtenedPropertyReadsTotal_Object = MibTableColumn
ex2tbExtenedPropertyReadsTotal = _Ex2tbExtenedPropertyReadsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 36),
    _Ex2tbExtenedPropertyReadsTotal_Type()
)
ex2tbExtenedPropertyReadsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbExtenedPropertyReadsTotal.setStatus("current")
_Ex2tbExtenedPropertyReadsPerSec_Type = Gauge32
_Ex2tbExtenedPropertyReadsPerSec_Object = MibTableColumn
ex2tbExtenedPropertyReadsPerSec = _Ex2tbExtenedPropertyReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 37),
    _Ex2tbExtenedPropertyReadsPerSec_Type()
)
ex2tbExtenedPropertyReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbExtenedPropertyReadsPerSec.setStatus("current")
_Ex2tbExtenedPropertyWritesTotal_Type = Gauge32
_Ex2tbExtenedPropertyWritesTotal_Object = MibTableColumn
ex2tbExtenedPropertyWritesTotal = _Ex2tbExtenedPropertyWritesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 38),
    _Ex2tbExtenedPropertyWritesTotal_Type()
)
ex2tbExtenedPropertyWritesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbExtenedPropertyWritesTotal.setStatus("current")
_Ex2tbExtenedPropertyWritesPerSec_Type = Gauge32
_Ex2tbExtenedPropertyWritesPerSec_Object = MibTableColumn
ex2tbExtenedPropertyWritesPerSec = _Ex2tbExtenedPropertyWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 39),
    _Ex2tbExtenedPropertyWritesPerSec_Type()
)
ex2tbExtenedPropertyWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbExtenedPropertyWritesPerSec.setStatus("current")
_Ex2tbLazyBytesLoadPerformedTotal_Type = Gauge32
_Ex2tbLazyBytesLoadPerformedTotal_Object = MibTableColumn
ex2tbLazyBytesLoadPerformedTotal = _Ex2tbLazyBytesLoadPerformedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 40),
    _Ex2tbLazyBytesLoadPerformedTotal_Type()
)
ex2tbLazyBytesLoadPerformedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbLazyBytesLoadPerformedTotal.setStatus("current")
_Ex2tbLazyByteLoadPerformedPerSec_Type = Gauge32
_Ex2tbLazyByteLoadPerformedPerSec_Object = MibTableColumn
ex2tbLazyByteLoadPerformedPerSec = _Ex2tbLazyByteLoadPerformedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 41),
    _Ex2tbLazyByteLoadPerformedPerSec_Type()
)
ex2tbLazyByteLoadPerformedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbLazyByteLoadPerformedPerSec.setStatus("current")
_Ex2tbLazyBytesLoadRequestedTotal_Type = Gauge32
_Ex2tbLazyBytesLoadRequestedTotal_Object = MibTableColumn
ex2tbLazyBytesLoadRequestedTotal = _Ex2tbLazyBytesLoadRequestedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 42),
    _Ex2tbLazyBytesLoadRequestedTotal_Type()
)
ex2tbLazyBytesLoadRequestedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbLazyBytesLoadRequestedTotal.setStatus("current")
_Ex2tbLazyByteLoadRequestedPerSec_Type = Gauge32
_Ex2tbLazyByteLoadRequestedPerSec_Object = MibTableColumn
ex2tbLazyByteLoadRequestedPerSec = _Ex2tbLazyByteLoadRequestedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 43),
    _Ex2tbLazyByteLoadRequestedPerSec_Type()
)
ex2tbLazyByteLoadRequestedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbLazyByteLoadRequestedPerSec.setStatus("current")
_Ex2tbMailItemBeginCommitTotal_Type = Gauge32
_Ex2tbMailItemBeginCommitTotal_Object = MibTableColumn
ex2tbMailItemBeginCommitTotal = _Ex2tbMailItemBeginCommitTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 44),
    _Ex2tbMailItemBeginCommitTotal_Type()
)
ex2tbMailItemBeginCommitTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemBeginCommitTotal.setStatus("current")
_Ex2tbMailItemBeginCommitPerSec_Type = Gauge32
_Ex2tbMailItemBeginCommitPerSec_Object = MibTableColumn
ex2tbMailItemBeginCommitPerSec = _Ex2tbMailItemBeginCommitPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 45),
    _Ex2tbMailItemBeginCommitPerSec_Type()
)
ex2tbMailItemBeginCommitPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemBeginCommitPerSec.setStatus("current")
_Ex2tbMailItemCloneCreateTotal_Type = Gauge32
_Ex2tbMailItemCloneCreateTotal_Object = MibTableColumn
ex2tbMailItemCloneCreateTotal = _Ex2tbMailItemCloneCreateTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 46),
    _Ex2tbMailItemCloneCreateTotal_Type()
)
ex2tbMailItemCloneCreateTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemCloneCreateTotal.setStatus("current")
_Ex2tbMailItemCloneCreatePerSec_Type = Gauge32
_Ex2tbMailItemCloneCreatePerSec_Object = MibTableColumn
ex2tbMailItemCloneCreatePerSec = _Ex2tbMailItemCloneCreatePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 47),
    _Ex2tbMailItemCloneCreatePerSec_Type()
)
ex2tbMailItemCloneCreatePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemCloneCreatePerSec.setStatus("current")
_Ex2tbMailItemCommitImmediatTotal_Type = Gauge32
_Ex2tbMailItemCommitImmediatTotal_Object = MibTableColumn
ex2tbMailItemCommitImmediatTotal = _Ex2tbMailItemCommitImmediatTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 48),
    _Ex2tbMailItemCommitImmediatTotal_Type()
)
ex2tbMailItemCommitImmediatTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemCommitImmediatTotal.setStatus("current")
_Ex2tbMailItemCommitImmediaPerSec_Type = Gauge32
_Ex2tbMailItemCommitImmediaPerSec_Object = MibTableColumn
ex2tbMailItemCommitImmediaPerSec = _Ex2tbMailItemCommitImmediaPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 49),
    _Ex2tbMailItemCommitImmediaPerSec_Type()
)
ex2tbMailItemCommitImmediaPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemCommitImmediaPerSec.setStatus("current")
_Ex2tbMailItemCommitLazyTotal_Type = Gauge32
_Ex2tbMailItemCommitLazyTotal_Object = MibTableColumn
ex2tbMailItemCommitLazyTotal = _Ex2tbMailItemCommitLazyTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 50),
    _Ex2tbMailItemCommitLazyTotal_Type()
)
ex2tbMailItemCommitLazyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemCommitLazyTotal.setStatus("current")
_Ex2tbMailItemCommitLazyPerSec_Type = Gauge32
_Ex2tbMailItemCommitLazyPerSec_Object = MibTableColumn
ex2tbMailItemCommitLazyPerSec = _Ex2tbMailItemCommitLazyPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 51),
    _Ex2tbMailItemCommitLazyPerSec_Type()
)
ex2tbMailItemCommitLazyPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemCommitLazyPerSec.setStatus("current")
_Ex2tbMailItemDehydrateTotal_Type = Gauge32
_Ex2tbMailItemDehydrateTotal_Object = MibTableColumn
ex2tbMailItemDehydrateTotal = _Ex2tbMailItemDehydrateTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 52),
    _Ex2tbMailItemDehydrateTotal_Type()
)
ex2tbMailItemDehydrateTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemDehydrateTotal.setStatus("current")
_Ex2tbMailItemDehydratePerSec_Type = Gauge32
_Ex2tbMailItemDehydratePerSec_Object = MibTableColumn
ex2tbMailItemDehydratePerSec = _Ex2tbMailItemDehydratePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 53),
    _Ex2tbMailItemDehydratePerSec_Type()
)
ex2tbMailItemDehydratePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemDehydratePerSec.setStatus("current")
_Ex2tbMailItemDeleteLazyTotal_Type = Gauge32
_Ex2tbMailItemDeleteLazyTotal_Object = MibTableColumn
ex2tbMailItemDeleteLazyTotal = _Ex2tbMailItemDeleteLazyTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 54),
    _Ex2tbMailItemDeleteLazyTotal_Type()
)
ex2tbMailItemDeleteLazyTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemDeleteLazyTotal.setStatus("current")
_Ex2tbMailItemDeleteLazyPerSec_Type = Gauge32
_Ex2tbMailItemDeleteLazyPerSec_Object = MibTableColumn
ex2tbMailItemDeleteLazyPerSec = _Ex2tbMailItemDeleteLazyPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 55),
    _Ex2tbMailItemDeleteLazyPerSec_Type()
)
ex2tbMailItemDeleteLazyPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemDeleteLazyPerSec.setStatus("current")
_Ex2tbMailItemLoadTotal_Type = Gauge32
_Ex2tbMailItemLoadTotal_Object = MibTableColumn
ex2tbMailItemLoadTotal = _Ex2tbMailItemLoadTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 56),
    _Ex2tbMailItemLoadTotal_Type()
)
ex2tbMailItemLoadTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemLoadTotal.setStatus("current")
_Ex2tbMailItemLoadPerSec_Type = Gauge32
_Ex2tbMailItemLoadPerSec_Object = MibTableColumn
ex2tbMailItemLoadPerSec = _Ex2tbMailItemLoadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 57),
    _Ex2tbMailItemLoadPerSec_Type()
)
ex2tbMailItemLoadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemLoadPerSec.setStatus("current")
_Ex2tbMailItemMaterialize_Type = Gauge32
_Ex2tbMailItemMaterialize_Object = MibTableColumn
ex2tbMailItemMaterialize = _Ex2tbMailItemMaterialize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 58),
    _Ex2tbMailItemMaterialize_Type()
)
ex2tbMailItemMaterialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemMaterialize.setStatus("current")
_Ex2tbMailItemMaterializePerSec_Type = Gauge32
_Ex2tbMailItemMaterializePerSec_Object = MibTableColumn
ex2tbMailItemMaterializePerSec = _Ex2tbMailItemMaterializePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 59),
    _Ex2tbMailItemMaterializePerSec_Type()
)
ex2tbMailItemMaterializePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemMaterializePerSec.setStatus("current")
_Ex2tbMailItemNewTotal_Type = Gauge32
_Ex2tbMailItemNewTotal_Object = MibTableColumn
ex2tbMailItemNewTotal = _Ex2tbMailItemNewTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 60),
    _Ex2tbMailItemNewTotal_Type()
)
ex2tbMailItemNewTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemNewTotal.setStatus("current")
_Ex2tbMailItemNewPerSec_Type = Gauge32
_Ex2tbMailItemNewPerSec_Object = MibTableColumn
ex2tbMailItemNewPerSec = _Ex2tbMailItemNewPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 61),
    _Ex2tbMailItemNewPerSec_Type()
)
ex2tbMailItemNewPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemNewPerSec.setStatus("current")
_Ex2tbMailItemWriteMimeToTotal_Type = Gauge32
_Ex2tbMailItemWriteMimeToTotal_Object = MibTableColumn
ex2tbMailItemWriteMimeToTotal = _Ex2tbMailItemWriteMimeToTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 62),
    _Ex2tbMailItemWriteMimeToTotal_Type()
)
ex2tbMailItemWriteMimeToTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemWriteMimeToTotal.setStatus("current")
_Ex2tbMailItemWriteMimeToPerSec_Type = Gauge32
_Ex2tbMailItemWriteMimeToPerSec_Object = MibTableColumn
ex2tbMailItemWriteMimeToPerSec = _Ex2tbMailItemWriteMimeToPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 63),
    _Ex2tbMailItemWriteMimeToPerSec_Type()
)
ex2tbMailItemWriteMimeToPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbMailItemWriteMimeToPerSec.setStatus("current")
_Ex2tbStreamBytesReadTotal_Type = Gauge32
_Ex2tbStreamBytesReadTotal_Object = MibTableColumn
ex2tbStreamBytesReadTotal = _Ex2tbStreamBytesReadTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 64),
    _Ex2tbStreamBytesReadTotal_Type()
)
ex2tbStreamBytesReadTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbStreamBytesReadTotal.setStatus("current")
_Ex2tbStreamBytesReadPerSec_Type = Gauge32
_Ex2tbStreamBytesReadPerSec_Object = MibTableColumn
ex2tbStreamBytesReadPerSec = _Ex2tbStreamBytesReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 65),
    _Ex2tbStreamBytesReadPerSec_Type()
)
ex2tbStreamBytesReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbStreamBytesReadPerSec.setStatus("current")
_Ex2tbStreamBytesWrittenTotal_Type = Gauge32
_Ex2tbStreamBytesWrittenTotal_Object = MibTableColumn
ex2tbStreamBytesWrittenTotal = _Ex2tbStreamBytesWrittenTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 66),
    _Ex2tbStreamBytesWrittenTotal_Type()
)
ex2tbStreamBytesWrittenTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbStreamBytesWrittenTotal.setStatus("current")
_Ex2tbStreamBytesWrittenPerSec_Type = Gauge32
_Ex2tbStreamBytesWrittenPerSec_Object = MibTableColumn
ex2tbStreamBytesWrittenPerSec = _Ex2tbStreamBytesWrittenPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 67),
    _Ex2tbStreamBytesWrittenPerSec_Type()
)
ex2tbStreamBytesWrittenPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbStreamBytesWrittenPerSec.setStatus("current")
_Ex2tbStreamReadTotal_Type = Gauge32
_Ex2tbStreamReadTotal_Object = MibTableColumn
ex2tbStreamReadTotal = _Ex2tbStreamReadTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 68),
    _Ex2tbStreamReadTotal_Type()
)
ex2tbStreamReadTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbStreamReadTotal.setStatus("current")
_Ex2tbStreamReadPerSec_Type = Gauge32
_Ex2tbStreamReadPerSec_Object = MibTableColumn
ex2tbStreamReadPerSec = _Ex2tbStreamReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 69),
    _Ex2tbStreamReadPerSec_Type()
)
ex2tbStreamReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbStreamReadPerSec.setStatus("current")
_Ex2tbStreamSetLengthCount_Type = Gauge32
_Ex2tbStreamSetLengthCount_Object = MibTableColumn
ex2tbStreamSetLengthCount = _Ex2tbStreamSetLengthCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 70),
    _Ex2tbStreamSetLengthCount_Type()
)
ex2tbStreamSetLengthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbStreamSetLengthCount.setStatus("current")
_Ex2tbStreamSetLengthPerSec_Type = Gauge32
_Ex2tbStreamSetLengthPerSec_Object = MibTableColumn
ex2tbStreamSetLengthPerSec = _Ex2tbStreamSetLengthPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 71),
    _Ex2tbStreamSetLengthPerSec_Type()
)
ex2tbStreamSetLengthPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbStreamSetLengthPerSec.setStatus("current")
_Ex2tbStreamWritesTotal_Type = Gauge32
_Ex2tbStreamWritesTotal_Object = MibTableColumn
ex2tbStreamWritesTotal = _Ex2tbStreamWritesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 72),
    _Ex2tbStreamWritesTotal_Type()
)
ex2tbStreamWritesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbStreamWritesTotal.setStatus("current")
_Ex2tbStreamWritesPerSec_Type = Gauge32
_Ex2tbStreamWritesPerSec_Object = MibTableColumn
ex2tbStreamWritesPerSec = _Ex2tbStreamWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 55, 1, 73),
    _Ex2tbStreamWritesPerSec_Type()
)
ex2tbStreamWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tbStreamWritesPerSec.setStatus("current")
_Ex2TransportDumpster_ObjectIdentity = ObjectIdentity
ex2TransportDumpster = _Ex2TransportDumpster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 56)
)
_Ex2tdDumpsterDeletesPerSec_Type = Gauge32
_Ex2tdDumpsterDeletesPerSec_Object = MibScalar
ex2tdDumpsterDeletesPerSec = _Ex2tdDumpsterDeletesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 56, 1),
    _Ex2tdDumpsterDeletesPerSec_Type()
)
ex2tdDumpsterDeletesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tdDumpsterDeletesPerSec.setStatus("current")
_Ex2tdDumpsterInsertsPerSec_Type = Gauge32
_Ex2tdDumpsterInsertsPerSec_Object = MibScalar
ex2tdDumpsterInsertsPerSec = _Ex2tdDumpsterInsertsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 56, 2),
    _Ex2tdDumpsterInsertsPerSec_Type()
)
ex2tdDumpsterInsertsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tdDumpsterInsertsPerSec.setStatus("current")
_Ex2tdDumpsterItemCount_Type = Gauge32
_Ex2tdDumpsterItemCount_Object = MibScalar
ex2tdDumpsterItemCount = _Ex2tdDumpsterItemCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 56, 3),
    _Ex2tdDumpsterItemCount_Type()
)
ex2tdDumpsterItemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tdDumpsterItemCount.setStatus("current")
_Ex2tdDumpsterSize_Type = Gauge32
_Ex2tdDumpsterSize_Object = MibScalar
ex2tdDumpsterSize = _Ex2tdDumpsterSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 56, 4),
    _Ex2tdDumpsterSize_Type()
)
ex2tdDumpsterSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tdDumpsterSize.setStatus("current")
_Ex2tdRedeliveryCount_Type = Gauge32
_Ex2tdRedeliveryCount_Object = MibScalar
ex2tdRedeliveryCount = _Ex2tdRedeliveryCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 56, 5),
    _Ex2tdRedeliveryCount_Type()
)
ex2tdRedeliveryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tdRedeliveryCount.setStatus("current")
_Ex2TransportPickupTable_Object = MibTable
ex2TransportPickupTable = _Ex2TransportPickupTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 57)
)
if mibBuilder.loadTexts:
    ex2TransportPickupTable.setStatus("current")
_Ex2TransportPickupEntry_Object = MibTableRow
ex2TransportPickupEntry = _Ex2TransportPickupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 57, 1)
)
ex2TransportPickupEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2tpInstance"),
)
if mibBuilder.loadTexts:
    ex2TransportPickupEntry.setStatus("current")
_Ex2tpkInstance_Type = InstanceName
_Ex2tpkInstance_Object = MibTableColumn
ex2tpkInstance = _Ex2tpkInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 57, 1, 1),
    _Ex2tpkInstance_Type()
)
ex2tpkInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tpkInstance.setStatus("current")
_Ex2tpkMessagesBadmailed_Type = Gauge32
_Ex2tpkMessagesBadmailed_Object = MibTableColumn
ex2tpkMessagesBadmailed = _Ex2tpkMessagesBadmailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 57, 1, 2),
    _Ex2tpkMessagesBadmailed_Type()
)
ex2tpkMessagesBadmailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tpkMessagesBadmailed.setStatus("current")
_Ex2tpkMessagesNDRed_Type = Gauge32
_Ex2tpkMessagesNDRed_Object = MibTableColumn
ex2tpkMessagesNDRed = _Ex2tpkMessagesNDRed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 57, 1, 3),
    _Ex2tpkMessagesNDRed_Type()
)
ex2tpkMessagesNDRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tpkMessagesNDRed.setStatus("current")
_Ex2tpkMessagesSubmitted_Type = Gauge32
_Ex2tpkMessagesSubmitted_Object = MibTableColumn
ex2tpkMessagesSubmitted = _Ex2tpkMessagesSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 57, 1, 4),
    _Ex2tpkMessagesSubmitted_Type()
)
ex2tpkMessagesSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tpkMessagesSubmitted.setStatus("current")
_Ex2TransportQueuesTable_Object = MibTable
ex2TransportQueuesTable = _Ex2TransportQueuesTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58)
)
if mibBuilder.loadTexts:
    ex2TransportQueuesTable.setStatus("current")
_Ex2TransportQueuesEntry_Object = MibTableRow
ex2TransportQueuesEntry = _Ex2TransportQueuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1)
)
ex2TransportQueuesEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2tqInstance"),
)
if mibBuilder.loadTexts:
    ex2TransportQueuesEntry.setStatus("current")
_Ex2tqInstance_Type = InstanceName
_Ex2tqInstance_Object = MibTableColumn
ex2tqInstance = _Ex2tqInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 1),
    _Ex2tqInstance_Type()
)
ex2tqInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqInstance.setStatus("current")
_Ex2tqActiveMailboxDelivQueLength_Type = Gauge32
_Ex2tqActiveMailboxDelivQueLength_Object = MibTableColumn
ex2tqActiveMailboxDelivQueLength = _Ex2tqActiveMailboxDelivQueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 2),
    _Ex2tqActiveMailboxDelivQueLength_Type()
)
ex2tqActiveMailboxDelivQueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqActiveMailboxDelivQueLength.setStatus("current")
_Ex2tqActiveNonSmtpDelivQueLength_Type = Gauge32
_Ex2tqActiveNonSmtpDelivQueLength_Object = MibTableColumn
ex2tqActiveNonSmtpDelivQueLength = _Ex2tqActiveNonSmtpDelivQueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 3),
    _Ex2tqActiveNonSmtpDelivQueLength_Type()
)
ex2tqActiveNonSmtpDelivQueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqActiveNonSmtpDelivQueLength.setStatus("current")
_Ex2tqActiveRemoteDelivQueLength_Type = Gauge32
_Ex2tqActiveRemoteDelivQueLength_Object = MibTableColumn
ex2tqActiveRemoteDelivQueLength = _Ex2tqActiveRemoteDelivQueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 4),
    _Ex2tqActiveRemoteDelivQueLength_Type()
)
ex2tqActiveRemoteDelivQueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqActiveRemoteDelivQueLength.setStatus("current")
_Ex2tqAggregDelivQueLengthAllQues_Type = Gauge32
_Ex2tqAggregDelivQueLengthAllQues_Object = MibTableColumn
ex2tqAggregDelivQueLengthAllQues = _Ex2tqAggregDelivQueLengthAllQues_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 5),
    _Ex2tqAggregDelivQueLengthAllQues_Type()
)
ex2tqAggregDelivQueLengthAllQues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqAggregDelivQueLengthAllQues.setStatus("current")
_Ex2tqItemCompletedDelivPerSecond_Type = Gauge32
_Ex2tqItemCompletedDelivPerSecond_Object = MibTableColumn
ex2tqItemCompletedDelivPerSecond = _Ex2tqItemCompletedDelivPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 6),
    _Ex2tqItemCompletedDelivPerSecond_Type()
)
ex2tqItemCompletedDelivPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqItemCompletedDelivPerSecond.setStatus("current")
_Ex2tqItemsCompletedDeliveryTotal_Type = Gauge32
_Ex2tqItemsCompletedDeliveryTotal_Object = MibTableColumn
ex2tqItemsCompletedDeliveryTotal = _Ex2tqItemsCompletedDeliveryTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 7),
    _Ex2tqItemsCompletedDeliveryTotal_Type()
)
ex2tqItemsCompletedDeliveryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqItemsCompletedDeliveryTotal.setStatus("current")
_Ex2tqItemsDeletedByAdminTotal_Type = Gauge32
_Ex2tqItemsDeletedByAdminTotal_Object = MibTableColumn
ex2tqItemsDeletedByAdminTotal = _Ex2tqItemsDeletedByAdminTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 8),
    _Ex2tqItemsDeletedByAdminTotal_Type()
)
ex2tqItemsDeletedByAdminTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqItemsDeletedByAdminTotal.setStatus("current")
_Ex2tqItemQuedForDelivExpireTotal_Type = Gauge32
_Ex2tqItemQuedForDelivExpireTotal_Object = MibTableColumn
ex2tqItemQuedForDelivExpireTotal = _Ex2tqItemQuedForDelivExpireTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 9),
    _Ex2tqItemQuedForDelivExpireTotal_Type()
)
ex2tqItemQuedForDelivExpireTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqItemQuedForDelivExpireTotal.setStatus("current")
_Ex2tqItemsQueuedForDeliveryTotal_Type = Gauge32
_Ex2tqItemsQueuedForDeliveryTotal_Object = MibTableColumn
ex2tqItemsQueuedForDeliveryTotal = _Ex2tqItemsQueuedForDeliveryTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 10),
    _Ex2tqItemsQueuedForDeliveryTotal_Type()
)
ex2tqItemsQueuedForDeliveryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqItemsQueuedForDeliveryTotal.setStatus("current")
_Ex2tqItemsQuedForDelivPerSecond_Type = Gauge32
_Ex2tqItemsQuedForDelivPerSecond_Object = MibTableColumn
ex2tqItemsQuedForDelivPerSecond = _Ex2tqItemsQuedForDelivPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 11),
    _Ex2tqItemsQuedForDelivPerSecond_Type()
)
ex2tqItemsQuedForDelivPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqItemsQuedForDelivPerSecond.setStatus("current")
_Ex2tqItemsResubmittedTotal_Type = Gauge32
_Ex2tqItemsResubmittedTotal_Object = MibTableColumn
ex2tqItemsResubmittedTotal = _Ex2tqItemsResubmittedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 12),
    _Ex2tqItemsResubmittedTotal_Type()
)
ex2tqItemsResubmittedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqItemsResubmittedTotal.setStatus("current")
_Ex2tqLargestDeliveryQueueLength_Type = Gauge32
_Ex2tqLargestDeliveryQueueLength_Object = MibTableColumn
ex2tqLargestDeliveryQueueLength = _Ex2tqLargestDeliveryQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 13),
    _Ex2tqLargestDeliveryQueueLength_Type()
)
ex2tqLargestDeliveryQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqLargestDeliveryQueueLength.setStatus("current")
_Ex2tqMsgsCompletedDelivPerSecond_Type = Gauge32
_Ex2tqMsgsCompletedDelivPerSecond_Object = MibTableColumn
ex2tqMsgsCompletedDelivPerSecond = _Ex2tqMsgsCompletedDelivPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 14),
    _Ex2tqMsgsCompletedDelivPerSecond_Type()
)
ex2tqMsgsCompletedDelivPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqMsgsCompletedDelivPerSecond.setStatus("current")
_Ex2tqMsgsCompletedDelivTotal_Type = Gauge32
_Ex2tqMsgsCompletedDelivTotal_Object = MibTableColumn
ex2tqMsgsCompletedDelivTotal = _Ex2tqMsgsCompletedDelivTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 15),
    _Ex2tqMsgsCompletedDelivTotal_Type()
)
ex2tqMsgsCompletedDelivTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqMsgsCompletedDelivTotal.setStatus("current")
_Ex2tqMessagesQueuedForDelivery_Type = Gauge32
_Ex2tqMessagesQueuedForDelivery_Object = MibTableColumn
ex2tqMessagesQueuedForDelivery = _Ex2tqMessagesQueuedForDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 16),
    _Ex2tqMessagesQueuedForDelivery_Type()
)
ex2tqMessagesQueuedForDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqMessagesQueuedForDelivery.setStatus("current")
_Ex2tqMsgsQuedForDelivTotal_Type = Gauge32
_Ex2tqMsgsQuedForDelivTotal_Object = MibTableColumn
ex2tqMsgsQuedForDelivTotal = _Ex2tqMsgsQuedForDelivTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 17),
    _Ex2tqMsgsQuedForDelivTotal_Type()
)
ex2tqMsgsQuedForDelivTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqMsgsQuedForDelivTotal.setStatus("current")
_Ex2tqMsgsQuedForDelivPerSecond_Type = Gauge32
_Ex2tqMsgsQuedForDelivPerSecond_Object = MibTableColumn
ex2tqMsgsQuedForDelivPerSecond = _Ex2tqMsgsQuedForDelivPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 18),
    _Ex2tqMsgsQuedForDelivPerSecond_Type()
)
ex2tqMsgsQuedForDelivPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqMsgsQuedForDelivPerSecond.setStatus("current")
_Ex2tqMessagesSubmittedPerSecond_Type = Gauge32
_Ex2tqMessagesSubmittedPerSecond_Object = MibTableColumn
ex2tqMessagesSubmittedPerSecond = _Ex2tqMessagesSubmittedPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 19),
    _Ex2tqMessagesSubmittedPerSecond_Type()
)
ex2tqMessagesSubmittedPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqMessagesSubmittedPerSecond.setStatus("current")
_Ex2tqMessagesSubmittedTotal_Type = Gauge32
_Ex2tqMessagesSubmittedTotal_Object = MibTableColumn
ex2tqMessagesSubmittedTotal = _Ex2tqMessagesSubmittedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 20),
    _Ex2tqMessagesSubmittedTotal_Type()
)
ex2tqMessagesSubmittedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqMessagesSubmittedTotal.setStatus("current")
_Ex2tqPoisonQueueLength_Type = Gauge32
_Ex2tqPoisonQueueLength_Object = MibTableColumn
ex2tqPoisonQueueLength = _Ex2tqPoisonQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 21),
    _Ex2tqPoisonQueueLength_Type()
)
ex2tqPoisonQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqPoisonQueueLength.setStatus("current")
_Ex2tqRetryMailboxDelivQueLength_Type = Gauge32
_Ex2tqRetryMailboxDelivQueLength_Object = MibTableColumn
ex2tqRetryMailboxDelivQueLength = _Ex2tqRetryMailboxDelivQueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 22),
    _Ex2tqRetryMailboxDelivQueLength_Type()
)
ex2tqRetryMailboxDelivQueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqRetryMailboxDelivQueLength.setStatus("current")
_Ex2tqRetryNonSmtpDelivQueLength_Type = Gauge32
_Ex2tqRetryNonSmtpDelivQueLength_Object = MibTableColumn
ex2tqRetryNonSmtpDelivQueLength = _Ex2tqRetryNonSmtpDelivQueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 23),
    _Ex2tqRetryNonSmtpDelivQueLength_Type()
)
ex2tqRetryNonSmtpDelivQueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqRetryNonSmtpDelivQueLength.setStatus("current")
_Ex2tqRetryRemoteDelivQueLength_Type = Gauge32
_Ex2tqRetryRemoteDelivQueLength_Object = MibTableColumn
ex2tqRetryRemoteDelivQueLength = _Ex2tqRetryRemoteDelivQueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 24),
    _Ex2tqRetryRemoteDelivQueLength_Type()
)
ex2tqRetryRemoteDelivQueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqRetryRemoteDelivQueLength.setStatus("current")
_Ex2tqSubmissQueueItemExpireTotal_Type = Gauge32
_Ex2tqSubmissQueueItemExpireTotal_Object = MibTableColumn
ex2tqSubmissQueueItemExpireTotal = _Ex2tqSubmissQueueItemExpireTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 25),
    _Ex2tqSubmissQueueItemExpireTotal_Type()
)
ex2tqSubmissQueueItemExpireTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqSubmissQueueItemExpireTotal.setStatus("current")
_Ex2tqSubmissionQueueLength_Type = Gauge32
_Ex2tqSubmissionQueueLength_Object = MibTableColumn
ex2tqSubmissionQueueLength = _Ex2tqSubmissionQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 26),
    _Ex2tqSubmissionQueueLength_Type()
)
ex2tqSubmissionQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqSubmissionQueueLength.setStatus("current")
_Ex2tqUnreachableQueueLength_Type = Gauge32
_Ex2tqUnreachableQueueLength_Object = MibTableColumn
ex2tqUnreachableQueueLength = _Ex2tqUnreachableQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 58, 1, 27),
    _Ex2tqUnreachableQueueLength_Type()
)
ex2tqUnreachableQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tqUnreachableQueueLength.setStatus("current")
_Ex2TransportResolverTable_Object = MibTable
ex2TransportResolverTable = _Ex2TransportResolverTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59)
)
if mibBuilder.loadTexts:
    ex2TransportResolverTable.setStatus("current")
_Ex2TransportResolverEntry_Object = MibTableRow
ex2TransportResolverEntry = _Ex2TransportResolverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59, 1)
)
ex2TransportResolverEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2treInstance"),
)
if mibBuilder.loadTexts:
    ex2TransportResolverEntry.setStatus("current")
_Ex2treInstance_Type = InstanceName
_Ex2treInstance_Object = MibTableColumn
ex2treInstance = _Ex2treInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59, 1, 1),
    _Ex2treInstance_Type()
)
ex2treInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2treInstance.setStatus("current")
_Ex2treAmbiguousRecipients_Type = Gauge32
_Ex2treAmbiguousRecipients_Object = MibTableColumn
ex2treAmbiguousRecipients = _Ex2treAmbiguousRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59, 1, 2),
    _Ex2treAmbiguousRecipients_Type()
)
ex2treAmbiguousRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2treAmbiguousRecipients.setStatus("current")
_Ex2treAmbiguousSenders_Type = Gauge32
_Ex2treAmbiguousSenders_Object = MibTableColumn
ex2treAmbiguousSenders = _Ex2treAmbiguousSenders_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59, 1, 3),
    _Ex2treAmbiguousSenders_Type()
)
ex2treAmbiguousSenders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2treAmbiguousSenders.setStatus("current")
_Ex2treFailedRecipients_Type = Gauge32
_Ex2treFailedRecipients_Object = MibTableColumn
ex2treFailedRecipients = _Ex2treFailedRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59, 1, 4),
    _Ex2treFailedRecipients_Type()
)
ex2treFailedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2treFailedRecipients.setStatus("current")
_Ex2treLoopRecipients_Type = Gauge32
_Ex2treLoopRecipients_Object = MibTableColumn
ex2treLoopRecipients = _Ex2treLoopRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59, 1, 5),
    _Ex2treLoopRecipients_Type()
)
ex2treLoopRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2treLoopRecipients.setStatus("current")
_Ex2treMessagesChipped_Type = Gauge32
_Ex2treMessagesChipped_Object = MibTableColumn
ex2treMessagesChipped = _Ex2treMessagesChipped_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59, 1, 6),
    _Ex2treMessagesChipped_Type()
)
ex2treMessagesChipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2treMessagesChipped.setStatus("current")
_Ex2treMessagesCreated_Type = Gauge32
_Ex2treMessagesCreated_Object = MibTableColumn
ex2treMessagesCreated = _Ex2treMessagesCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59, 1, 7),
    _Ex2treMessagesCreated_Type()
)
ex2treMessagesCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2treMessagesCreated.setStatus("current")
_Ex2treMessagesRetried_Type = Gauge32
_Ex2treMessagesRetried_Object = MibTableColumn
ex2treMessagesRetried = _Ex2treMessagesRetried_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59, 1, 8),
    _Ex2treMessagesRetried_Type()
)
ex2treMessagesRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2treMessagesRetried.setStatus("current")
_Ex2treUnresolvedOrgRecipients_Type = Gauge32
_Ex2treUnresolvedOrgRecipients_Object = MibTableColumn
ex2treUnresolvedOrgRecipients = _Ex2treUnresolvedOrgRecipients_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59, 1, 9),
    _Ex2treUnresolvedOrgRecipients_Type()
)
ex2treUnresolvedOrgRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2treUnresolvedOrgRecipients.setStatus("current")
_Ex2treUnresolvedOrgSenders_Type = Gauge32
_Ex2treUnresolvedOrgSenders_Object = MibTableColumn
ex2treUnresolvedOrgSenders = _Ex2treUnresolvedOrgSenders_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 59, 1, 10),
    _Ex2treUnresolvedOrgSenders_Type()
)
ex2treUnresolvedOrgSenders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2treUnresolvedOrgSenders.setStatus("current")
_Ex2TransportRoutingTable_Object = MibTable
ex2TransportRoutingTable = _Ex2TransportRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 60)
)
if mibBuilder.loadTexts:
    ex2TransportRoutingTable.setStatus("current")
_Ex2TransportRoutingEntry_Object = MibTableRow
ex2TransportRoutingEntry = _Ex2TransportRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 60, 1)
)
ex2TransportRoutingEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2troInstance"),
)
if mibBuilder.loadTexts:
    ex2TransportRoutingEntry.setStatus("current")
_Ex2troInstance_Type = InstanceName
_Ex2troInstance_Object = MibTableColumn
ex2troInstance = _Ex2troInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 60, 1, 1),
    _Ex2troInstance_Type()
)
ex2troInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2troInstance.setStatus("current")
_Ex2troRoutingNDRsTotal_Type = Gauge32
_Ex2troRoutingNDRsTotal_Object = MibTableColumn
ex2troRoutingNDRsTotal = _Ex2troRoutingNDRsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 60, 1, 2),
    _Ex2troRoutingNDRsTotal_Type()
)
ex2troRoutingNDRsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2troRoutingNDRsTotal.setStatus("current")
_Ex2troRoutingTableCalculateTotal_Type = Gauge32
_Ex2troRoutingTableCalculateTotal_Object = MibTableColumn
ex2troRoutingTableCalculateTotal = _Ex2troRoutingTableCalculateTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 60, 1, 3),
    _Ex2troRoutingTableCalculateTotal_Type()
)
ex2troRoutingTableCalculateTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2troRoutingTableCalculateTotal.setStatus("current")
_Ex2troRoutingTablesChangedTotal_Type = Gauge32
_Ex2troRoutingTablesChangedTotal_Object = MibTableColumn
ex2troRoutingTablesChangedTotal = _Ex2troRoutingTablesChangedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 60, 1, 4),
    _Ex2troRoutingTablesChangedTotal_Type()
)
ex2troRoutingTablesChangedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2troRoutingTablesChangedTotal.setStatus("current")
_Ex2TransportSmtpReceiveTable_Object = MibTable
ex2TransportSmtpReceiveTable = _Ex2TransportSmtpReceiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61)
)
if mibBuilder.loadTexts:
    ex2TransportSmtpReceiveTable.setStatus("current")
_Ex2TransportSmtpReceiveEntry_Object = MibTableRow
ex2TransportSmtpReceiveEntry = _Ex2TransportSmtpReceiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1)
)
ex2TransportSmtpReceiveEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2tsrInstance"),
)
if mibBuilder.loadTexts:
    ex2TransportSmtpReceiveEntry.setStatus("current")
_Ex2tsrInstance_Type = InstanceName
_Ex2tsrInstance_Object = MibTableColumn
ex2tsrInstance = _Ex2tsrInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 1),
    _Ex2tsrInstance_Type()
)
ex2tsrInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrInstance.setStatus("current")
_Ex2tsrAverageBytesPerConnection_Type = Gauge32
_Ex2tsrAverageBytesPerConnection_Object = MibTableColumn
ex2tsrAverageBytesPerConnection = _Ex2tsrAverageBytesPerConnection_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 2),
    _Ex2tsrAverageBytesPerConnection_Type()
)
ex2tsrAverageBytesPerConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrAverageBytesPerConnection.setStatus("current")
_Ex2tsrAverageBytesPerMessage_Type = Gauge32
_Ex2tsrAverageBytesPerMessage_Object = MibTableColumn
ex2tsrAverageBytesPerMessage = _Ex2tsrAverageBytesPerMessage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 3),
    _Ex2tsrAverageBytesPerMessage_Type()
)
ex2tsrAverageBytesPerMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrAverageBytesPerMessage.setStatus("current")
_Ex2tsrAverageMessagePerConnectin_Type = Gauge32
_Ex2tsrAverageMessagePerConnectin_Object = MibTableColumn
ex2tsrAverageMessagePerConnectin = _Ex2tsrAverageMessagePerConnectin_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 4),
    _Ex2tsrAverageMessagePerConnectin_Type()
)
ex2tsrAverageMessagePerConnectin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrAverageMessagePerConnectin.setStatus("current")
_Ex2tsrAverageRecipientPerMessage_Type = Gauge32
_Ex2tsrAverageRecipientPerMessage_Object = MibTableColumn
ex2tsrAverageRecipientPerMessage = _Ex2tsrAverageRecipientPerMessage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 5),
    _Ex2tsrAverageRecipientPerMessage_Type()
)
ex2tsrAverageRecipientPerMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrAverageRecipientPerMessage.setStatus("current")
_Ex2tsrBytesReceivedTotal_Type = Gauge32
_Ex2tsrBytesReceivedTotal_Object = MibTableColumn
ex2tsrBytesReceivedTotal = _Ex2tsrBytesReceivedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 6),
    _Ex2tsrBytesReceivedTotal_Type()
)
ex2tsrBytesReceivedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrBytesReceivedTotal.setStatus("current")
_Ex2tsrBytesReceivedPerSec_Type = Gauge32
_Ex2tsrBytesReceivedPerSec_Object = MibTableColumn
ex2tsrBytesReceivedPerSec = _Ex2tsrBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 7),
    _Ex2tsrBytesReceivedPerSec_Type()
)
ex2tsrBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrBytesReceivedPerSec.setStatus("current")
_Ex2tsrConnectionsCreatedPerSec_Type = Gauge32
_Ex2tsrConnectionsCreatedPerSec_Object = MibTableColumn
ex2tsrConnectionsCreatedPerSec = _Ex2tsrConnectionsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 8),
    _Ex2tsrConnectionsCreatedPerSec_Type()
)
ex2tsrConnectionsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrConnectionsCreatedPerSec.setStatus("current")
_Ex2tsrConnectionsCurrent_Type = Gauge32
_Ex2tsrConnectionsCurrent_Object = MibTableColumn
ex2tsrConnectionsCurrent = _Ex2tsrConnectionsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 9),
    _Ex2tsrConnectionsCurrent_Type()
)
ex2tsrConnectionsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrConnectionsCurrent.setStatus("current")
_Ex2tsrConnectionsTotal_Type = Gauge32
_Ex2tsrConnectionsTotal_Object = MibTableColumn
ex2tsrConnectionsTotal = _Ex2tsrConnectionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 10),
    _Ex2tsrConnectionsTotal_Type()
)
ex2tsrConnectionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrConnectionsTotal.setStatus("current")
_Ex2tsrDisconnectionsByAgents_Type = Gauge32
_Ex2tsrDisconnectionsByAgents_Object = MibTableColumn
ex2tsrDisconnectionsByAgents = _Ex2tsrDisconnectionsByAgents_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 11),
    _Ex2tsrDisconnectionsByAgents_Type()
)
ex2tsrDisconnectionsByAgents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrDisconnectionsByAgents.setStatus("current")
_Ex2tsrDisconnectByAgentPerSecond_Type = Gauge32
_Ex2tsrDisconnectByAgentPerSecond_Object = MibTableColumn
ex2tsrDisconnectByAgentPerSecond = _Ex2tsrDisconnectByAgentPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 12),
    _Ex2tsrDisconnectByAgentPerSecond_Type()
)
ex2tsrDisconnectByAgentPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrDisconnectByAgentPerSecond.setStatus("current")
_Ex2tsrMessageBytesReceivedTotal_Type = Gauge32
_Ex2tsrMessageBytesReceivedTotal_Object = MibTableColumn
ex2tsrMessageBytesReceivedTotal = _Ex2tsrMessageBytesReceivedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 13),
    _Ex2tsrMessageBytesReceivedTotal_Type()
)
ex2tsrMessageBytesReceivedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrMessageBytesReceivedTotal.setStatus("current")
_Ex2tsrMessageBytesReceivedPerSec_Type = Gauge32
_Ex2tsrMessageBytesReceivedPerSec_Object = MibTableColumn
ex2tsrMessageBytesReceivedPerSec = _Ex2tsrMessageBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 14),
    _Ex2tsrMessageBytesReceivedPerSec_Type()
)
ex2tsrMessageBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrMessageBytesReceivedPerSec.setStatus("current")
_Ex2tsrMessagesReceivedTotal_Type = Gauge32
_Ex2tsrMessagesReceivedTotal_Object = MibTableColumn
ex2tsrMessagesReceivedTotal = _Ex2tsrMessagesReceivedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 15),
    _Ex2tsrMessagesReceivedTotal_Type()
)
ex2tsrMessagesReceivedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrMessagesReceivedTotal.setStatus("current")
_Ex2tsrMessagesReceivedPerSec_Type = Gauge32
_Ex2tsrMessagesReceivedPerSec_Object = MibTableColumn
ex2tsrMessagesReceivedPerSec = _Ex2tsrMessagesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 16),
    _Ex2tsrMessagesReceivedPerSec_Type()
)
ex2tsrMessagesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrMessagesReceivedPerSec.setStatus("current")
_Ex2tsrMessagesRefusedForSize_Type = Gauge32
_Ex2tsrMessagesRefusedForSize_Object = MibTableColumn
ex2tsrMessagesRefusedForSize = _Ex2tsrMessagesRefusedForSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 17),
    _Ex2tsrMessagesRefusedForSize_Type()
)
ex2tsrMessagesRefusedForSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrMessagesRefusedForSize.setStatus("current")
_Ex2tsrRecipientsAcceptedTotal_Type = Gauge32
_Ex2tsrRecipientsAcceptedTotal_Object = MibTableColumn
ex2tsrRecipientsAcceptedTotal = _Ex2tsrRecipientsAcceptedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 18),
    _Ex2tsrRecipientsAcceptedTotal_Type()
)
ex2tsrRecipientsAcceptedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrRecipientsAcceptedTotal.setStatus("current")
_Ex2tsrTarpittingDelaysAnonymous_Type = Gauge32
_Ex2tsrTarpittingDelaysAnonymous_Object = MibTableColumn
ex2tsrTarpittingDelaysAnonymous = _Ex2tsrTarpittingDelaysAnonymous_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 19),
    _Ex2tsrTarpittingDelaysAnonymous_Type()
)
ex2tsrTarpittingDelaysAnonymous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrTarpittingDelaysAnonymous.setStatus("current")
_Ex2tsrTarpittngDelayAuthenticate_Type = Gauge32
_Ex2tsrTarpittngDelayAuthenticate_Object = MibTableColumn
ex2tsrTarpittngDelayAuthenticate = _Ex2tsrTarpittngDelayAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 61, 1, 20),
    _Ex2tsrTarpittngDelayAuthenticate_Type()
)
ex2tsrTarpittngDelayAuthenticate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tsrTarpittngDelayAuthenticate.setStatus("current")
_Ex2TransportSmtpSendTable_Object = MibTable
ex2TransportSmtpSendTable = _Ex2TransportSmtpSendTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62)
)
if mibBuilder.loadTexts:
    ex2TransportSmtpSendTable.setStatus("current")
_Ex2TransportSmtpSendEntry_Object = MibTableRow
ex2TransportSmtpSendEntry = _Ex2TransportSmtpSendEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1)
)
ex2TransportSmtpSendEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2tssInstance"),
)
if mibBuilder.loadTexts:
    ex2TransportSmtpSendEntry.setStatus("current")
_Ex2tssInstance_Type = InstanceName
_Ex2tssInstance_Object = MibTableColumn
ex2tssInstance = _Ex2tssInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 1),
    _Ex2tssInstance_Type()
)
ex2tssInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssInstance.setStatus("current")
_Ex2tssAverageBytesPerConnection_Type = Gauge32
_Ex2tssAverageBytesPerConnection_Object = MibTableColumn
ex2tssAverageBytesPerConnection = _Ex2tssAverageBytesPerConnection_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 2),
    _Ex2tssAverageBytesPerConnection_Type()
)
ex2tssAverageBytesPerConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssAverageBytesPerConnection.setStatus("current")
_Ex2tssAvgMessageBytesPerMessage_Type = Gauge32
_Ex2tssAvgMessageBytesPerMessage_Object = MibTableColumn
ex2tssAvgMessageBytesPerMessage = _Ex2tssAvgMessageBytesPerMessage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 3),
    _Ex2tssAvgMessageBytesPerMessage_Type()
)
ex2tssAvgMessageBytesPerMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssAvgMessageBytesPerMessage.setStatus("current")
_Ex2tssAvgMessagesPerConnection_Type = Gauge32
_Ex2tssAvgMessagesPerConnection_Object = MibTableColumn
ex2tssAvgMessagesPerConnection = _Ex2tssAvgMessagesPerConnection_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 4),
    _Ex2tssAvgMessagesPerConnection_Type()
)
ex2tssAvgMessagesPerConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssAvgMessagesPerConnection.setStatus("current")
_Ex2tssAvgRecipientsPerMessage_Type = Gauge32
_Ex2tssAvgRecipientsPerMessage_Object = MibTableColumn
ex2tssAvgRecipientsPerMessage = _Ex2tssAvgRecipientsPerMessage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 5),
    _Ex2tssAvgRecipientsPerMessage_Type()
)
ex2tssAvgRecipientsPerMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssAvgRecipientsPerMessage.setStatus("current")
_Ex2tssBytesSentTotal_Type = Gauge32
_Ex2tssBytesSentTotal_Object = MibTableColumn
ex2tssBytesSentTotal = _Ex2tssBytesSentTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 6),
    _Ex2tssBytesSentTotal_Type()
)
ex2tssBytesSentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssBytesSentTotal.setStatus("current")
_Ex2tssBytesSentPerSec_Type = Gauge32
_Ex2tssBytesSentPerSec_Object = MibTableColumn
ex2tssBytesSentPerSec = _Ex2tssBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 7),
    _Ex2tssBytesSentPerSec_Type()
)
ex2tssBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssBytesSentPerSec.setStatus("current")
_Ex2tssConnectionsCreatedPerSec_Type = Gauge32
_Ex2tssConnectionsCreatedPerSec_Object = MibTableColumn
ex2tssConnectionsCreatedPerSec = _Ex2tssConnectionsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 8),
    _Ex2tssConnectionsCreatedPerSec_Type()
)
ex2tssConnectionsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssConnectionsCreatedPerSec.setStatus("current")
_Ex2tssConnectionsCurrent_Type = Gauge32
_Ex2tssConnectionsCurrent_Object = MibTableColumn
ex2tssConnectionsCurrent = _Ex2tssConnectionsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 9),
    _Ex2tssConnectionsCurrent_Type()
)
ex2tssConnectionsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssConnectionsCurrent.setStatus("current")
_Ex2tssConnectionsTotal_Type = Gauge32
_Ex2tssConnectionsTotal_Object = MibTableColumn
ex2tssConnectionsTotal = _Ex2tssConnectionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 10),
    _Ex2tssConnectionsTotal_Type()
)
ex2tssConnectionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssConnectionsTotal.setStatus("current")
_Ex2tssMessageBytesSentTotal_Type = Gauge32
_Ex2tssMessageBytesSentTotal_Object = MibTableColumn
ex2tssMessageBytesSentTotal = _Ex2tssMessageBytesSentTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 11),
    _Ex2tssMessageBytesSentTotal_Type()
)
ex2tssMessageBytesSentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssMessageBytesSentTotal.setStatus("current")
_Ex2tssMessageBytesSentPerSec_Type = Gauge32
_Ex2tssMessageBytesSentPerSec_Object = MibTableColumn
ex2tssMessageBytesSentPerSec = _Ex2tssMessageBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 12),
    _Ex2tssMessageBytesSentPerSec_Type()
)
ex2tssMessageBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssMessageBytesSentPerSec.setStatus("current")
_Ex2tssMessagesSentTotal_Type = Gauge32
_Ex2tssMessagesSentTotal_Object = MibTableColumn
ex2tssMessagesSentTotal = _Ex2tssMessagesSentTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 13),
    _Ex2tssMessagesSentTotal_Type()
)
ex2tssMessagesSentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssMessagesSentTotal.setStatus("current")
_Ex2tssMessagesSentPerSec_Type = Gauge32
_Ex2tssMessagesSentPerSec_Object = MibTableColumn
ex2tssMessagesSentPerSec = _Ex2tssMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 14),
    _Ex2tssMessagesSentPerSec_Type()
)
ex2tssMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssMessagesSentPerSec.setStatus("current")
_Ex2tssRecipientsSent_Type = Gauge32
_Ex2tssRecipientsSent_Object = MibTableColumn
ex2tssRecipientsSent = _Ex2tssRecipientsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 62, 1, 15),
    _Ex2tssRecipientsSent_Type()
)
ex2tssRecipientsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2tssRecipientsSent.setStatus("current")
_Ex2UMAutoAttendantTable_Object = MibTable
ex2UMAutoAttendantTable = _Ex2UMAutoAttendantTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63)
)
if mibBuilder.loadTexts:
    ex2UMAutoAttendantTable.setStatus("current")
_Ex2UMAutoAttendantEntry_Object = MibTableRow
ex2UMAutoAttendantEntry = _Ex2UMAutoAttendantEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1)
)
ex2UMAutoAttendantEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2umaaInstance"),
)
if mibBuilder.loadTexts:
    ex2UMAutoAttendantEntry.setStatus("current")
_Ex2umaaInstance_Type = InstanceName
_Ex2umaaInstance_Object = MibTableColumn
ex2umaaInstance = _Ex2umaaInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 1),
    _Ex2umaaInstance_Type()
)
ex2umaaInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaInstance.setStatus("current")
_Ex2umaaPercentSuccessfulCalls_Type = Gauge32
_Ex2umaaPercentSuccessfulCalls_Object = MibTableColumn
ex2umaaPercentSuccessfulCalls = _Ex2umaaPercentSuccessfulCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 2),
    _Ex2umaaPercentSuccessfulCalls_Type()
)
ex2umaaPercentSuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaPercentSuccessfulCalls.setStatus("current")
_Ex2umaaAmbiguousNameTransfers_Type = Gauge32
_Ex2umaaAmbiguousNameTransfers_Object = MibTableColumn
ex2umaaAmbiguousNameTransfers = _Ex2umaaAmbiguousNameTransfers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 3),
    _Ex2umaaAmbiguousNameTransfers_Type()
)
ex2umaaAmbiguousNameTransfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaAmbiguousNameTransfers.setStatus("current")
_Ex2umaaAverageCallTime_Type = Gauge32
_Ex2umaaAverageCallTime_Object = MibTableColumn
ex2umaaAverageCallTime = _Ex2umaaAverageCallTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 4),
    _Ex2umaaAverageCallTime_Type()
)
ex2umaaAverageCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaAverageCallTime.setStatus("current")
_Ex2umaaAverageRecentCallTime_Type = Gauge32
_Ex2umaaAverageRecentCallTime_Object = MibTableColumn
ex2umaaAverageRecentCallTime = _Ex2umaaAverageRecentCallTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 5),
    _Ex2umaaAverageRecentCallTime_Type()
)
ex2umaaAverageRecentCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaAverageRecentCallTime.setStatus("current")
_Ex2umaaBusinessHoursCalls_Type = Gauge32
_Ex2umaaBusinessHoursCalls_Object = MibTableColumn
ex2umaaBusinessHoursCalls = _Ex2umaaBusinessHoursCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 6),
    _Ex2umaaBusinessHoursCalls_Type()
)
ex2umaaBusinessHoursCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaBusinessHoursCalls.setStatus("current")
_Ex2umaaCallsDisconUMIrreExtError_Type = Gauge32
_Ex2umaaCallsDisconUMIrreExtError_Object = MibTableColumn
ex2umaaCallsDisconUMIrreExtError = _Ex2umaaCallsDisconUMIrreExtError_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 7),
    _Ex2umaaCallsDisconUMIrreExtError_Type()
)
ex2umaaCallsDisconUMIrreExtError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaCallsDisconUMIrreExtError.setStatus("current")
_Ex2umaaCallsWithDTMFFallback_Type = Gauge32
_Ex2umaaCallsWithDTMFFallback_Object = MibTableColumn
ex2umaaCallsWithDTMFFallback = _Ex2umaaCallsWithDTMFFallback_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 8),
    _Ex2umaaCallsWithDTMFFallback_Type()
)
ex2umaaCallsWithDTMFFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaCallsWithDTMFFallback.setStatus("current")
_Ex2umaaCallsWithSentMessage_Type = Gauge32
_Ex2umaaCallsWithSentMessage_Object = MibTableColumn
ex2umaaCallsWithSentMessage = _Ex2umaaCallsWithSentMessage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 9),
    _Ex2umaaCallsWithSentMessage_Type()
)
ex2umaaCallsWithSentMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaCallsWithSentMessage.setStatus("current")
_Ex2umaaCallsWithSpeechInput_Type = Gauge32
_Ex2umaaCallsWithSpeechInput_Object = MibTableColumn
ex2umaaCallsWithSpeechInput = _Ex2umaaCallsWithSpeechInput_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 10),
    _Ex2umaaCallsWithSpeechInput_Type()
)
ex2umaaCallsWithSpeechInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaCallsWithSpeechInput.setStatus("current")
_Ex2umaaCallsWithSpokenName_Type = Gauge32
_Ex2umaaCallsWithSpokenName_Object = MibTableColumn
ex2umaaCallsWithSpokenName = _Ex2umaaCallsWithSpokenName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 11),
    _Ex2umaaCallsWithSpokenName_Type()
)
ex2umaaCallsWithSpokenName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaCallsWithSpokenName.setStatus("current")
_Ex2umaaCustomMenuOptions_Type = Gauge32
_Ex2umaaCustomMenuOptions_Object = MibTableColumn
ex2umaaCustomMenuOptions = _Ex2umaaCustomMenuOptions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 12),
    _Ex2umaaCustomMenuOptions_Type()
)
ex2umaaCustomMenuOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaCustomMenuOptions.setStatus("current")
_Ex2umaaDirectoryAccessed_Type = Gauge32
_Ex2umaaDirectoryAccessed_Object = MibTableColumn
ex2umaaDirectoryAccessed = _Ex2umaaDirectoryAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 13),
    _Ex2umaaDirectoryAccessed_Type()
)
ex2umaaDirectoryAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaDirectoryAccessed.setStatus("current")
_Ex2umaaDirAccsdSuccByDialByName_Type = Gauge32
_Ex2umaaDirAccsdSuccByDialByName_Object = MibTableColumn
ex2umaaDirAccsdSuccByDialByName = _Ex2umaaDirAccsdSuccByDialByName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 14),
    _Ex2umaaDirAccsdSuccByDialByName_Type()
)
ex2umaaDirAccsdSuccByDialByName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaDirAccsdSuccByDialByName.setStatus("current")
_Ex2umaaDirAccsdSuccBySpokenName_Type = Gauge32
_Ex2umaaDirAccsdSuccBySpokenName_Object = MibTableColumn
ex2umaaDirAccsdSuccBySpokenName = _Ex2umaaDirAccsdSuccBySpokenName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 15),
    _Ex2umaaDirAccsdSuccBySpokenName_Type()
)
ex2umaaDirAccsdSuccBySpokenName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaDirAccsdSuccBySpokenName.setStatus("current")
_Ex2umaaDirAccsdByDialByName_Type = Gauge32
_Ex2umaaDirAccsdByDialByName_Object = MibTableColumn
ex2umaaDirAccsdByDialByName = _Ex2umaaDirAccsdByDialByName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 16),
    _Ex2umaaDirAccsdByDialByName_Type()
)
ex2umaaDirAccsdByDialByName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaDirAccsdByDialByName.setStatus("current")
_Ex2umaaDirAccsdByExtension_Type = Gauge32
_Ex2umaaDirAccsdByExtension_Object = MibTableColumn
ex2umaaDirAccsdByExtension = _Ex2umaaDirAccsdByExtension_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 17),
    _Ex2umaaDirAccsdByExtension_Type()
)
ex2umaaDirAccsdByExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaDirAccsdByExtension.setStatus("current")
_Ex2umaaDirAccsdBySpokenName_Type = Gauge32
_Ex2umaaDirAccsdBySpokenName_Object = MibTableColumn
ex2umaaDirAccsdBySpokenName = _Ex2umaaDirAccsdBySpokenName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 18),
    _Ex2umaaDirAccsdBySpokenName_Type()
)
ex2umaaDirAccsdBySpokenName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaDirAccsdBySpokenName.setStatus("current")
_Ex2umaaDisallowedTransfers_Type = Gauge32
_Ex2umaaDisallowedTransfers_Object = MibTableColumn
ex2umaaDisallowedTransfers = _Ex2umaaDisallowedTransfers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 19),
    _Ex2umaaDisallowedTransfers_Type()
)
ex2umaaDisallowedTransfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaDisallowedTransfers.setStatus("current")
_Ex2umaaDisconnectedWithoutInput_Type = Gauge32
_Ex2umaaDisconnectedWithoutInput_Object = MibTableColumn
ex2umaaDisconnectedWithoutInput = _Ex2umaaDisconnectedWithoutInput_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 20),
    _Ex2umaaDisconnectedWithoutInput_Type()
)
ex2umaaDisconnectedWithoutInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaDisconnectedWithoutInput.setStatus("current")
_Ex2umaaMenuOption1Used_Type = Gauge32
_Ex2umaaMenuOption1Used_Object = MibTableColumn
ex2umaaMenuOption1Used = _Ex2umaaMenuOption1Used_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 21),
    _Ex2umaaMenuOption1Used_Type()
)
ex2umaaMenuOption1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaMenuOption1Used.setStatus("current")
_Ex2umaaMenuOption2Used_Type = Gauge32
_Ex2umaaMenuOption2Used_Object = MibTableColumn
ex2umaaMenuOption2Used = _Ex2umaaMenuOption2Used_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 22),
    _Ex2umaaMenuOption2Used_Type()
)
ex2umaaMenuOption2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaMenuOption2Used.setStatus("current")
_Ex2umaaMenuOption3Used_Type = Gauge32
_Ex2umaaMenuOption3Used_Object = MibTableColumn
ex2umaaMenuOption3Used = _Ex2umaaMenuOption3Used_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 23),
    _Ex2umaaMenuOption3Used_Type()
)
ex2umaaMenuOption3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaMenuOption3Used.setStatus("current")
_Ex2umaaMenuOption4Used_Type = Gauge32
_Ex2umaaMenuOption4Used_Object = MibTableColumn
ex2umaaMenuOption4Used = _Ex2umaaMenuOption4Used_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 24),
    _Ex2umaaMenuOption4Used_Type()
)
ex2umaaMenuOption4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaMenuOption4Used.setStatus("current")
_Ex2umaaMenuOption5Used_Type = Gauge32
_Ex2umaaMenuOption5Used_Object = MibTableColumn
ex2umaaMenuOption5Used = _Ex2umaaMenuOption5Used_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 25),
    _Ex2umaaMenuOption5Used_Type()
)
ex2umaaMenuOption5Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaMenuOption5Used.setStatus("current")
_Ex2umaaMenuOption6Used_Type = Gauge32
_Ex2umaaMenuOption6Used_Object = MibTableColumn
ex2umaaMenuOption6Used = _Ex2umaaMenuOption6Used_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 26),
    _Ex2umaaMenuOption6Used_Type()
)
ex2umaaMenuOption6Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaMenuOption6Used.setStatus("current")
_Ex2umaaMenuOption7Used_Type = Gauge32
_Ex2umaaMenuOption7Used_Object = MibTableColumn
ex2umaaMenuOption7Used = _Ex2umaaMenuOption7Used_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 27),
    _Ex2umaaMenuOption7Used_Type()
)
ex2umaaMenuOption7Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaMenuOption7Used.setStatus("current")
_Ex2umaaMenuOption8Used_Type = Gauge32
_Ex2umaaMenuOption8Used_Object = MibTableColumn
ex2umaaMenuOption8Used = _Ex2umaaMenuOption8Used_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 28),
    _Ex2umaaMenuOption8Used_Type()
)
ex2umaaMenuOption8Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaMenuOption8Used.setStatus("current")
_Ex2umaaMenuOption9Used_Type = Gauge32
_Ex2umaaMenuOption9Used_Object = MibTableColumn
ex2umaaMenuOption9Used = _Ex2umaaMenuOption9Used_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 29),
    _Ex2umaaMenuOption9Used_Type()
)
ex2umaaMenuOption9Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaMenuOption9Used.setStatus("current")
_Ex2umaaMenuOptionTimedOut_Type = Gauge32
_Ex2umaaMenuOptionTimedOut_Object = MibTableColumn
ex2umaaMenuOptionTimedOut = _Ex2umaaMenuOptionTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 30),
    _Ex2umaaMenuOptionTimedOut_Type()
)
ex2umaaMenuOptionTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaMenuOptionTimedOut.setStatus("current")
_Ex2umaaOperatorTransfers_Type = Gauge32
_Ex2umaaOperatorTransfers_Object = MibTableColumn
ex2umaaOperatorTransfers = _Ex2umaaOperatorTransfers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 31),
    _Ex2umaaOperatorTransfers_Type()
)
ex2umaaOperatorTransfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaOperatorTransfers.setStatus("current")
_Ex2umaaOperTransReqByUser_Type = Gauge32
_Ex2umaaOperTransReqByUser_Object = MibTableColumn
ex2umaaOperTransReqByUser = _Ex2umaaOperTransReqByUser_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 32),
    _Ex2umaaOperTransReqByUser_Type()
)
ex2umaaOperTransReqByUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaOperTransReqByUser.setStatus("current")
_Ex2umaaOperTransReqByUseOpenMenu_Type = Gauge32
_Ex2umaaOperTransReqByUseOpenMenu_Object = MibTableColumn
ex2umaaOperTransReqByUseOpenMenu = _Ex2umaaOperTransReqByUseOpenMenu_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 33),
    _Ex2umaaOperTransReqByUseOpenMenu_Type()
)
ex2umaaOperTransReqByUseOpenMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaOperTransReqByUseOpenMenu.setStatus("current")
_Ex2umaaOutOfHoursCalls_Type = Gauge32
_Ex2umaaOutOfHoursCalls_Object = MibTableColumn
ex2umaaOutOfHoursCalls = _Ex2umaaOutOfHoursCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 34),
    _Ex2umaaOutOfHoursCalls_Type()
)
ex2umaaOutOfHoursCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaOutOfHoursCalls.setStatus("current")
_Ex2umaaSentToAutoAttendant_Type = Gauge32
_Ex2umaaSentToAutoAttendant_Object = MibTableColumn
ex2umaaSentToAutoAttendant = _Ex2umaaSentToAutoAttendant_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 35),
    _Ex2umaaSentToAutoAttendant_Type()
)
ex2umaaSentToAutoAttendant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaSentToAutoAttendant.setStatus("current")
_Ex2umaaTotalCalls_Type = Gauge32
_Ex2umaaTotalCalls_Object = MibTableColumn
ex2umaaTotalCalls = _Ex2umaaTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 36),
    _Ex2umaaTotalCalls_Type()
)
ex2umaaTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaTotalCalls.setStatus("current")
_Ex2umaaTransferredCount_Type = Gauge32
_Ex2umaaTransferredCount_Object = MibTableColumn
ex2umaaTransferredCount = _Ex2umaaTransferredCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 63, 1, 37),
    _Ex2umaaTransferredCount_Type()
)
ex2umaaTransferredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaaTransferredCount.setStatus("current")
_Ex2UMAvailability_ObjectIdentity = ObjectIdentity
ex2UMAvailability = _Ex2UMAvailability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64)
)
_Ex2umaCallAnswerQueuedMessages_Type = Gauge32
_Ex2umaCallAnswerQueuedMessages_Object = MibScalar
ex2umaCallAnswerQueuedMessages = _Ex2umaCallAnswerQueuedMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 1),
    _Ex2umaCallAnswerQueuedMessages_Type()
)
ex2umaCallAnswerQueuedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaCallAnswerQueuedMessages.setStatus("current")
_Ex2umaCalDisconUMIrrecovExtError_Type = Gauge32
_Ex2umaCalDisconUMIrrecovExtError_Object = MibScalar
ex2umaCalDisconUMIrrecovExtError = _Ex2umaCalDisconUMIrrecovExtError_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 2),
    _Ex2umaCalDisconUMIrrecovExtError_Type()
)
ex2umaCalDisconUMIrrecovExtError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaCalDisconUMIrrecovExtError.setStatus("current")
_Ex2umaCalDiscnUMIrrecovExtErrSec_Type = Gauge32
_Ex2umaCalDiscnUMIrrecovExtErrSec_Object = MibScalar
ex2umaCalDiscnUMIrrecovExtErrSec = _Ex2umaCalDiscnUMIrrecovExtErrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 3),
    _Ex2umaCalDiscnUMIrrecovExtErrSec_Type()
)
ex2umaCalDiscnUMIrrecovExtErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaCalDiscnUMIrrecovExtErrSec.setStatus("current")
_Ex2umaCalDiscnIrrecovInternalErr_Type = Gauge32
_Ex2umaCalDiscnIrrecovInternalErr_Object = MibScalar
ex2umaCalDiscnIrrecovInternalErr = _Ex2umaCalDiscnIrrecovInternalErr_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 4),
    _Ex2umaCalDiscnIrrecovInternalErr_Type()
)
ex2umaCalDiscnIrrecovInternalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaCalDiscnIrrecovInternalErr.setStatus("current")
_Ex2umaDirectoryAccessFailures_Type = Gauge32
_Ex2umaDirectoryAccessFailures_Object = MibScalar
ex2umaDirectoryAccessFailures = _Ex2umaDirectoryAccessFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 5),
    _Ex2umaDirectoryAccessFailures_Type()
)
ex2umaDirectoryAccessFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaDirectoryAccessFailures.setStatus("current")
_Ex2umaFailedToRedirectCall_Type = Gauge32
_Ex2umaFailedToRedirectCall_Object = MibScalar
ex2umaFailedToRedirectCall = _Ex2umaFailedToRedirectCall_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 6),
    _Ex2umaFailedToRedirectCall_Type()
)
ex2umaFailedToRedirectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaFailedToRedirectCall.setStatus("current")
_Ex2umaHubTransportAccessComplete_Type = Gauge32
_Ex2umaHubTransportAccessComplete_Object = MibScalar
ex2umaHubTransportAccessComplete = _Ex2umaHubTransportAccessComplete_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 7),
    _Ex2umaHubTransportAccessComplete_Type()
)
ex2umaHubTransportAccessComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaHubTransportAccessComplete.setStatus("current")
_Ex2umaHubTransportAccessFailures_Type = Gauge32
_Ex2umaHubTransportAccessFailures_Object = MibScalar
ex2umaHubTransportAccessFailures = _Ex2umaHubTransportAccessFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 8),
    _Ex2umaHubTransportAccessFailures_Type()
)
ex2umaHubTransportAccessFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaHubTransportAccessFailures.setStatus("current")
_Ex2umaIncompSignalingInformation_Type = Gauge32
_Ex2umaIncompSignalingInformation_Object = MibScalar
ex2umaIncompSignalingInformation = _Ex2umaIncompSignalingInformation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 9),
    _Ex2umaIncompSignalingInformation_Type()
)
ex2umaIncompSignalingInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaIncompSignalingInformation.setStatus("current")
_Ex2umaMailboxServerAccessFailure_Type = Gauge32
_Ex2umaMailboxServerAccessFailure_Object = MibScalar
ex2umaMailboxServerAccessFailure = _Ex2umaMailboxServerAccessFailure_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 10),
    _Ex2umaMailboxServerAccessFailure_Type()
)
ex2umaMailboxServerAccessFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaMailboxServerAccessFailure.setStatus("current")
_Ex2umaMaximumCallsAllowed_Type = Gauge32
_Ex2umaMaximumCallsAllowed_Object = MibScalar
ex2umaMaximumCallsAllowed = _Ex2umaMaximumCallsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 11),
    _Ex2umaMaximumCallsAllowed_Type()
)
ex2umaMaximumCallsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaMaximumCallsAllowed.setStatus("current")
_Ex2umaNameTTSed_Type = Gauge32
_Ex2umaNameTTSed_Object = MibScalar
ex2umaNameTTSed = _Ex2umaNameTTSed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 12),
    _Ex2umaNameTTSed_Type()
)
ex2umaNameTTSed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaNameTTSed.setStatus("current")
_Ex2umaQueuedOCSUserEventNotifica_Type = Gauge32
_Ex2umaQueuedOCSUserEventNotifica_Object = MibScalar
ex2umaQueuedOCSUserEventNotifica = _Ex2umaQueuedOCSUserEventNotifica_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 13),
    _Ex2umaQueuedOCSUserEventNotifica_Type()
)
ex2umaQueuedOCSUserEventNotifica.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaQueuedOCSUserEventNotifica.setStatus("current")
_Ex2umaSpokenNameAccessed_Type = Gauge32
_Ex2umaSpokenNameAccessed_Object = MibScalar
ex2umaSpokenNameAccessed = _Ex2umaSpokenNameAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 14),
    _Ex2umaSpokenNameAccessed_Type()
)
ex2umaSpokenNameAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaSpokenNameAccessed.setStatus("current")
_Ex2umaTotalWorkerProcesCallCount_Type = Gauge32
_Ex2umaTotalWorkerProcesCallCount_Object = MibScalar
ex2umaTotalWorkerProcesCallCount = _Ex2umaTotalWorkerProcesCallCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 15),
    _Ex2umaTotalWorkerProcesCallCount_Type()
)
ex2umaTotalWorkerProcesCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaTotalWorkerProcesCallCount.setStatus("current")
_Ex2umaUnhandledExceptionsPerSec_Type = Gauge32
_Ex2umaUnhandledExceptionsPerSec_Object = MibScalar
ex2umaUnhandledExceptionsPerSec = _Ex2umaUnhandledExceptionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 16),
    _Ex2umaUnhandledExceptionsPerSec_Type()
)
ex2umaUnhandledExceptionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaUnhandledExceptionsPerSec.setStatus("current")
_Ex2umaWorkerProcessRecycled_Type = Gauge32
_Ex2umaWorkerProcessRecycled_Object = MibScalar
ex2umaWorkerProcessRecycled = _Ex2umaWorkerProcessRecycled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 64, 17),
    _Ex2umaWorkerProcessRecycled_Type()
)
ex2umaWorkerProcessRecycled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umaWorkerProcessRecycled.setStatus("current")
_Ex2UMCallAnswer_ObjectIdentity = ObjectIdentity
ex2UMCallAnswer = _Ex2UMCallAnswer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65)
)
_Ex2UMCallAnsAvgGreetingSize_Type = Gauge32
_Ex2UMCallAnsAvgGreetingSize_Object = MibScalar
ex2UMCallAnsAvgGreetingSize = _Ex2UMCallAnsAvgGreetingSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 1),
    _Ex2UMCallAnsAvgGreetingSize_Type()
)
ex2UMCallAnsAvgGreetingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsAvgGreetingSize.setStatus("current")
_Ex2UMCallAnsAvgRecentVoiceMsgSiz_Type = Gauge32
_Ex2UMCallAnsAvgRecentVoiceMsgSiz_Object = MibScalar
ex2UMCallAnsAvgRecentVoiceMsgSiz = _Ex2UMCallAnsAvgRecentVoiceMsgSiz_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 2),
    _Ex2UMCallAnsAvgRecentVoiceMsgSiz_Type()
)
ex2UMCallAnsAvgRecentVoiceMsgSiz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsAvgRecentVoiceMsgSiz.setStatus("current")
_Ex2UMCallAnsAvgVoiceMsgSize_Type = Gauge32
_Ex2UMCallAnsAvgVoiceMsgSize_Object = MibScalar
ex2UMCallAnsAvgVoiceMsgSize = _Ex2UMCallAnsAvgVoiceMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 3),
    _Ex2UMCallAnsAvgVoiceMsgSize_Type()
)
ex2UMCallAnsAvgVoiceMsgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsAvgVoiceMsgSize.setStatus("current")
_Ex2UMCallAnsCallAnsingCalls_Type = Gauge32
_Ex2UMCallAnsCallAnsingCalls_Object = MibScalar
ex2UMCallAnsCallAnsingCalls = _Ex2UMCallAnsCallAnsingCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 4),
    _Ex2UMCallAnsCallAnsingCalls_Type()
)
ex2UMCallAnsCallAnsingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsCallAnsingCalls.setStatus("current")
_Ex2UMCallAnsCallAnsingEscapes_Type = Gauge32
_Ex2UMCallAnsCallAnsingEscapes_Object = MibScalar
ex2UMCallAnsCallAnsingEscapes = _Ex2UMCallAnsCallAnsingEscapes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 5),
    _Ex2UMCallAnsCallAnsingEscapes_Type()
)
ex2UMCallAnsCallAnsingEscapes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsCallAnsingEscapes.setStatus("current")
_Ex2UMCallAnsCallAnsingMissedCall_Type = Gauge32
_Ex2UMCallAnsCallAnsingMissedCall_Object = MibScalar
ex2UMCallAnsCallAnsingMissedCall = _Ex2UMCallAnsCallAnsingMissedCall_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 6),
    _Ex2UMCallAnsCallAnsingMissedCall_Type()
)
ex2UMCallAnsCallAnsingMissedCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsCallAnsingMissedCall.setStatus("current")
_Ex2UMCallAnsCallAnsingVoiceMsgs_Type = Gauge32
_Ex2UMCallAnsCallAnsingVoiceMsgs_Object = MibScalar
ex2UMCallAnsCallAnsingVoiceMsgs = _Ex2UMCallAnsCallAnsingVoiceMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 7),
    _Ex2UMCallAnsCallAnsingVoiceMsgs_Type()
)
ex2UMCallAnsCallAnsingVoiceMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsCallAnsingVoiceMsgs.setStatus("current")
_Ex2UMCallAnsCallAnsVoiceMsgPrSec_Type = Gauge32
_Ex2UMCallAnsCallAnsVoiceMsgPrSec_Object = MibScalar
ex2UMCallAnsCallAnsVoiceMsgPrSec = _Ex2UMCallAnsCallAnsVoiceMsgPrSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 8),
    _Ex2UMCallAnsCallAnsVoiceMsgPrSec_Type()
)
ex2UMCallAnsCallAnsVoiceMsgPrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsCallAnsVoiceMsgPrSec.setStatus("current")
_Ex2UMCallAnsCallFailTransUnavail_Type = Gauge32
_Ex2UMCallAnsCallFailTransUnavail_Object = MibScalar
ex2UMCallAnsCallFailTransUnavail = _Ex2UMCallAnsCallFailTransUnavail_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 9),
    _Ex2UMCallAnsCallFailTransUnavail_Type()
)
ex2UMCallAnsCallFailTransUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsCallFailTransUnavail.setStatus("current")
_Ex2UMCalAnsCalDisCalUMAudioHrgls_Type = Gauge32
_Ex2UMCalAnsCalDisCalUMAudioHrgls_Object = MibScalar
ex2UMCalAnsCalDisCalUMAudioHrgls = _Ex2UMCalAnsCalDisCalUMAudioHrgls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 10),
    _Ex2UMCalAnsCalDisCalUMAudioHrgls_Type()
)
ex2UMCalAnsCalDisCalUMAudioHrgls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCalAnsCalDisCalUMAudioHrgls.setStatus("current")
_Ex2UMCalAnsCalDisUMIrrecExtError_Type = Gauge32
_Ex2UMCalAnsCalDisUMIrrecExtError_Object = MibScalar
ex2UMCalAnsCalDisUMIrrecExtError = _Ex2UMCalAnsCalDisUMIrrecExtError_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 11),
    _Ex2UMCalAnsCalDisUMIrrecExtError_Type()
)
ex2UMCalAnsCalDisUMIrrecExtError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCalAnsCalDisUMIrrecExtError.setStatus("current")
_Ex2UMCallAnsCallWithoutPersGreet_Type = Gauge32
_Ex2UMCallAnsCallWithoutPersGreet_Object = MibScalar
ex2UMCallAnsCallWithoutPersGreet = _Ex2UMCallAnsCallWithoutPersGreet_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 12),
    _Ex2UMCallAnsCallWithoutPersGreet_Type()
)
ex2UMCallAnsCallWithoutPersGreet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsCallWithoutPersGreet.setStatus("current")
_Ex2UMCallAnsDivertExtNotProvis_Type = Gauge32
_Ex2UMCallAnsDivertExtNotProvis_Object = MibScalar
ex2UMCallAnsDivertExtNotProvis = _Ex2UMCallAnsDivertExtNotProvis_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 13),
    _Ex2UMCallAnsDivertExtNotProvis_Type()
)
ex2UMCallAnsDivertExtNotProvis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsDivertExtNotProvis.setStatus("current")
_Ex2UMCallAnsFetchGreetingTimeOut_Type = Gauge32
_Ex2UMCallAnsFetchGreetingTimeOut_Object = MibScalar
ex2UMCallAnsFetchGreetingTimeOut = _Ex2UMCallAnsFetchGreetingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 65, 14),
    _Ex2UMCallAnsFetchGreetingTimeOut_Type()
)
ex2UMCallAnsFetchGreetingTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2UMCallAnsFetchGreetingTimeOut.setStatus("current")
_Ex2UMClientAccessTable_Object = MibTable
ex2UMClientAccessTable = _Ex2UMClientAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 66)
)
if mibBuilder.loadTexts:
    ex2UMClientAccessTable.setStatus("current")
_Ex2UMClientAccessEntry_Object = MibTableRow
ex2UMClientAccessEntry = _Ex2UMClientAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 66, 1)
)
ex2UMClientAccessEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2umcacInstance"),
)
if mibBuilder.loadTexts:
    ex2UMClientAccessEntry.setStatus("current")
_Ex2umcacInstance_Type = InstanceName
_Ex2umcacInstance_Object = MibTableColumn
ex2umcacInstance = _Ex2umcacInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 66, 1, 1),
    _Ex2umcacInstance_Type()
)
ex2umcacInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umcacInstance.setStatus("current")
_Ex2umcacPID_Type = Gauge32
_Ex2umcacPID_Object = MibTableColumn
ex2umcacPID = _Ex2umcacPID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 66, 1, 2),
    _Ex2umcacPID_Type()
)
ex2umcacPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umcacPID.setStatus("current")
_Ex2umcacTotalNumPINResetRequests_Type = Gauge32
_Ex2umcacTotalNumPINResetRequests_Object = MibTableColumn
ex2umcacTotalNumPINResetRequests = _Ex2umcacTotalNumPINResetRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 66, 1, 3),
    _Ex2umcacTotalNumPINResetRequests_Type()
)
ex2umcacTotalNumPINResetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umcacTotalNumPINResetRequests.setStatus("current")
_Ex2umcacTotalNumFailPINResetReq_Type = Gauge32
_Ex2umcacTotalNumFailPINResetReq_Object = MibTableColumn
ex2umcacTotalNumFailPINResetReq = _Ex2umcacTotalNumFailPINResetReq_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 66, 1, 4),
    _Ex2umcacTotalNumFailPINResetReq_Type()
)
ex2umcacTotalNumFailPINResetReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umcacTotalNumFailPINResetReq.setStatus("current")
_Ex2umcacTotalNumFailPlayPhoneReq_Type = Gauge32
_Ex2umcacTotalNumFailPlayPhoneReq_Object = MibTableColumn
ex2umcacTotalNumFailPlayPhoneReq = _Ex2umcacTotalNumFailPlayPhoneReq_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 66, 1, 5),
    _Ex2umcacTotalNumFailPlayPhoneReq_Type()
)
ex2umcacTotalNumFailPlayPhoneReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umcacTotalNumFailPlayPhoneReq.setStatus("current")
_Ex2umcacTotalNumPlayPhoneRequest_Type = Gauge32
_Ex2umcacTotalNumPlayPhoneRequest_Object = MibTableColumn
ex2umcacTotalNumPlayPhoneRequest = _Ex2umcacTotalNumPlayPhoneRequest_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 66, 1, 6),
    _Ex2umcacTotalNumPlayPhoneRequest_Type()
)
ex2umcacTotalNumPlayPhoneRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umcacTotalNumPlayPhoneRequest.setStatus("current")
_Ex2UMFax_ObjectIdentity = ObjectIdentity
ex2UMFax = _Ex2UMFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 67)
)
_Ex2umfAverageFaxMessageSize_Type = Gauge32
_Ex2umfAverageFaxMessageSize_Object = MibScalar
ex2umfAverageFaxMessageSize = _Ex2umfAverageFaxMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 67, 1),
    _Ex2umfAverageFaxMessageSize_Type()
)
ex2umfAverageFaxMessageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umfAverageFaxMessageSize.setStatus("current")
_Ex2umfAverageRecentFaxMessageSiz_Type = Gauge32
_Ex2umfAverageRecentFaxMessageSiz_Object = MibScalar
ex2umfAverageRecentFaxMessageSiz = _Ex2umfAverageRecentFaxMessageSiz_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 67, 2),
    _Ex2umfAverageRecentFaxMessageSiz_Type()
)
ex2umfAverageRecentFaxMessageSiz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umfAverageRecentFaxMessageSiz.setStatus("current")
_Ex2umfFaxCallDurationExceeded_Type = Gauge32
_Ex2umfFaxCallDurationExceeded_Object = MibScalar
ex2umfFaxCallDurationExceeded = _Ex2umfFaxCallDurationExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 67, 3),
    _Ex2umfFaxCallDurationExceeded_Type()
)
ex2umfFaxCallDurationExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umfFaxCallDurationExceeded.setStatus("current")
_Ex2umfFaxCallNonProvisionMailbox_Type = Gauge32
_Ex2umfFaxCallNonProvisionMailbox_Object = MibScalar
ex2umfFaxCallNonProvisionMailbox = _Ex2umfFaxCallNonProvisionMailbox_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 67, 4),
    _Ex2umfFaxCallNonProvisionMailbox_Type()
)
ex2umfFaxCallNonProvisionMailbox.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umfFaxCallNonProvisionMailbox.setStatus("current")
_Ex2umfFaxIncomplete_Type = Gauge32
_Ex2umfFaxIncomplete_Object = MibScalar
ex2umfFaxIncomplete = _Ex2umfFaxIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 67, 5),
    _Ex2umfFaxIncomplete_Type()
)
ex2umfFaxIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umfFaxIncomplete.setStatus("current")
_Ex2umfFaxMessages_Type = Gauge32
_Ex2umfFaxMessages_Object = MibScalar
ex2umfFaxMessages = _Ex2umfFaxMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 67, 6),
    _Ex2umfFaxMessages_Type()
)
ex2umfFaxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umfFaxMessages.setStatus("current")
_Ex2UMGeneral_ObjectIdentity = ObjectIdentity
ex2UMGeneral = _Ex2UMGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68)
)
_Ex2umgAverageCallDuration_Type = Gauge32
_Ex2umgAverageCallDuration_Object = MibScalar
ex2umgAverageCallDuration = _Ex2umgAverageCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 1),
    _Ex2umgAverageCallDuration_Type()
)
ex2umgAverageCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgAverageCallDuration.setStatus("current")
_Ex2umgAverageRecentCallDuration_Type = Gauge32
_Ex2umgAverageRecentCallDuration_Object = MibScalar
ex2umgAverageRecentCallDuration = _Ex2umgAverageRecentCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 2),
    _Ex2umgAverageRecentCallDuration_Type()
)
ex2umgAverageRecentCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgAverageRecentCallDuration.setStatus("current")
_Ex2umgCallDurationExceeded_Type = Gauge32
_Ex2umgCallDurationExceeded_Object = MibScalar
ex2umgCallDurationExceeded = _Ex2umgCallDurationExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 3),
    _Ex2umgCallDurationExceeded_Type()
)
ex2umgCallDurationExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCallDurationExceeded.setStatus("current")
_Ex2umgCallsDisconnectUserFailure_Type = Gauge32
_Ex2umgCallsDisconnectUserFailure_Object = MibScalar
ex2umgCallsDisconnectUserFailure = _Ex2umgCallsDisconnectUserFailure_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 4),
    _Ex2umgCallsDisconnectUserFailure_Type()
)
ex2umgCallsDisconnectUserFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCallsDisconnectUserFailure.setStatus("current")
_Ex2umgCallsRejected_Type = Gauge32
_Ex2umgCallsRejected_Object = MibScalar
ex2umgCallsRejected = _Ex2umgCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 5),
    _Ex2umgCallsRejected_Type()
)
ex2umgCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCallsRejected.setStatus("current")
_Ex2umgCallsRejectedPerSecond_Type = Gauge32
_Ex2umgCallsRejectedPerSecond_Object = MibScalar
ex2umgCallsRejectedPerSecond = _Ex2umgCallsRejectedPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 6),
    _Ex2umgCallsRejectedPerSecond_Type()
)
ex2umgCallsRejectedPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCallsRejectedPerSecond.setStatus("current")
_Ex2umgCurrentAutoAttendantCalls_Type = Gauge32
_Ex2umgCurrentAutoAttendantCalls_Object = MibScalar
ex2umgCurrentAutoAttendantCalls = _Ex2umgCurrentAutoAttendantCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 7),
    _Ex2umgCurrentAutoAttendantCalls_Type()
)
ex2umgCurrentAutoAttendantCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCurrentAutoAttendantCalls.setStatus("current")
_Ex2umgCurrentCASConnections_Type = Gauge32
_Ex2umgCurrentCASConnections_Object = MibScalar
ex2umgCurrentCASConnections = _Ex2umgCurrentCASConnections_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 8),
    _Ex2umgCurrentCASConnections_Type()
)
ex2umgCurrentCASConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCurrentCASConnections.setStatus("current")
_Ex2umgCurrentCalls_Type = Gauge32
_Ex2umgCurrentCalls_Object = MibScalar
ex2umgCurrentCalls = _Ex2umgCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 9),
    _Ex2umgCurrentCalls_Type()
)
ex2umgCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCurrentCalls.setStatus("current")
_Ex2umgCurrentFaxCalls_Type = Gauge32
_Ex2umgCurrentFaxCalls_Object = MibScalar
ex2umgCurrentFaxCalls = _Ex2umgCurrentFaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 10),
    _Ex2umgCurrentFaxCalls_Type()
)
ex2umgCurrentFaxCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCurrentFaxCalls.setStatus("current")
_Ex2umgCurrentPlayOnPhoneCalls_Type = Gauge32
_Ex2umgCurrentPlayOnPhoneCalls_Object = MibScalar
ex2umgCurrentPlayOnPhoneCalls = _Ex2umgCurrentPlayOnPhoneCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 11),
    _Ex2umgCurrentPlayOnPhoneCalls_Type()
)
ex2umgCurrentPlayOnPhoneCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCurrentPlayOnPhoneCalls.setStatus("current")
_Ex2umgCurrentPromptEditingCalls_Type = Gauge32
_Ex2umgCurrentPromptEditingCalls_Object = MibScalar
ex2umgCurrentPromptEditingCalls = _Ex2umgCurrentPromptEditingCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 12),
    _Ex2umgCurrentPromptEditingCalls_Type()
)
ex2umgCurrentPromptEditingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCurrentPromptEditingCalls.setStatus("current")
_Ex2umgCurrentSubscriberAccesCall_Type = Gauge32
_Ex2umgCurrentSubscriberAccesCall_Object = MibScalar
ex2umgCurrentSubscriberAccesCall = _Ex2umgCurrentSubscriberAccesCall_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 13),
    _Ex2umgCurrentSubscriberAccesCall_Type()
)
ex2umgCurrentSubscriberAccesCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCurrentSubscriberAccesCall.setStatus("current")
_Ex2umgCurrUnauthentPilotNumCall_Type = Gauge32
_Ex2umgCurrUnauthentPilotNumCall_Object = MibScalar
ex2umgCurrUnauthentPilotNumCall = _Ex2umgCurrUnauthentPilotNumCall_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 14),
    _Ex2umgCurrUnauthentPilotNumCall_Type()
)
ex2umgCurrUnauthentPilotNumCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCurrUnauthentPilotNumCall.setStatus("current")
_Ex2umgCurrentVoiceCalls_Type = Gauge32
_Ex2umgCurrentVoiceCalls_Object = MibScalar
ex2umgCurrentVoiceCalls = _Ex2umgCurrentVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 15),
    _Ex2umgCurrentVoiceCalls_Type()
)
ex2umgCurrentVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgCurrentVoiceCalls.setStatus("current")
_Ex2umgDelayedCalls_Type = Gauge32
_Ex2umgDelayedCalls_Object = MibScalar
ex2umgDelayedCalls = _Ex2umgDelayedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 16),
    _Ex2umgDelayedCalls_Type()
)
ex2umgDelayedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgDelayedCalls.setStatus("current")
_Ex2umgOCSUserEventNotifications_Type = Gauge32
_Ex2umgOCSUserEventNotifications_Object = MibScalar
ex2umgOCSUserEventNotifications = _Ex2umgOCSUserEventNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 17),
    _Ex2umgOCSUserEventNotifications_Type()
)
ex2umgOCSUserEventNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgOCSUserEventNotifications.setStatus("current")
_Ex2umgTotalCalls_Type = Gauge32
_Ex2umgTotalCalls_Object = MibScalar
ex2umgTotalCalls = _Ex2umgTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 18),
    _Ex2umgTotalCalls_Type()
)
ex2umgTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgTotalCalls.setStatus("current")
_Ex2umgTotalCallsPerSecond_Type = Gauge32
_Ex2umgTotalCallsPerSecond_Object = MibScalar
ex2umgTotalCallsPerSecond = _Ex2umgTotalCallsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 19),
    _Ex2umgTotalCallsPerSecond_Type()
)
ex2umgTotalCallsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgTotalCallsPerSecond.setStatus("current")
_Ex2umgTotalPlayOnPhoneCalls_Type = Gauge32
_Ex2umgTotalPlayOnPhoneCalls_Object = MibScalar
ex2umgTotalPlayOnPhoneCalls = _Ex2umgTotalPlayOnPhoneCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 20),
    _Ex2umgTotalPlayOnPhoneCalls_Type()
)
ex2umgTotalPlayOnPhoneCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgTotalPlayOnPhoneCalls.setStatus("current")
_Ex2umgUserResponseLatency_Type = Gauge32
_Ex2umgUserResponseLatency_Object = MibScalar
ex2umgUserResponseLatency = _Ex2umgUserResponseLatency_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 68, 21),
    _Ex2umgUserResponseLatency_Type()
)
ex2umgUserResponseLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umgUserResponseLatency.setStatus("current")
_Ex2UMPerformance_ObjectIdentity = ObjectIdentity
ex2UMPerformance = _Ex2UMPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 69)
)
_Ex2umpOperationsOverFiveSeconds_Type = Gauge32
_Ex2umpOperationsOverFiveSeconds_Object = MibScalar
ex2umpOperationsOverFiveSeconds = _Ex2umpOperationsOverFiveSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 69, 1),
    _Ex2umpOperationsOverFiveSeconds_Type()
)
ex2umpOperationsOverFiveSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umpOperationsOverFiveSeconds.setStatus("current")
_Ex2umpOperationsOverFourSeconds_Type = Gauge32
_Ex2umpOperationsOverFourSeconds_Object = MibScalar
ex2umpOperationsOverFourSeconds = _Ex2umpOperationsOverFourSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 69, 2),
    _Ex2umpOperationsOverFourSeconds_Type()
)
ex2umpOperationsOverFourSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umpOperationsOverFourSeconds.setStatus("current")
_Ex2umpOperationsOverSixSeconds_Type = Gauge32
_Ex2umpOperationsOverSixSeconds_Object = MibScalar
ex2umpOperationsOverSixSeconds = _Ex2umpOperationsOverSixSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 69, 3),
    _Ex2umpOperationsOverSixSeconds_Type()
)
ex2umpOperationsOverSixSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umpOperationsOverSixSeconds.setStatus("current")
_Ex2umpOperationsOverThreeSeconds_Type = Gauge32
_Ex2umpOperationsOverThreeSeconds_Object = MibScalar
ex2umpOperationsOverThreeSeconds = _Ex2umpOperationsOverThreeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 69, 4),
    _Ex2umpOperationsOverThreeSeconds_Type()
)
ex2umpOperationsOverThreeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umpOperationsOverThreeSeconds.setStatus("current")
_Ex2umpOperationsOverTwoSeconds_Type = Gauge32
_Ex2umpOperationsOverTwoSeconds_Object = MibScalar
ex2umpOperationsOverTwoSeconds = _Ex2umpOperationsOverTwoSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 69, 5),
    _Ex2umpOperationsOverTwoSeconds_Type()
)
ex2umpOperationsOverTwoSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umpOperationsOverTwoSeconds.setStatus("current")
_Ex2umpOperationsUnderTwoSeconds_Type = Gauge32
_Ex2umpOperationsUnderTwoSeconds_Object = MibScalar
ex2umpOperationsUnderTwoSeconds = _Ex2umpOperationsUnderTwoSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 69, 6),
    _Ex2umpOperationsUnderTwoSeconds_Type()
)
ex2umpOperationsUnderTwoSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umpOperationsUnderTwoSeconds.setStatus("current")
_Ex2UMSubscriberAccess_ObjectIdentity = ObjectIdentity
ex2UMSubscriberAccess = _Ex2UMSubscriberAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70)
)
_Ex2umsaAvgRecentSentVoiceMsgSize_Type = Gauge32
_Ex2umsaAvgRecentSentVoiceMsgSize_Object = MibScalar
ex2umsaAvgRecentSentVoiceMsgSize = _Ex2umsaAvgRecentSentVoiceMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 1),
    _Ex2umsaAvgRecentSentVoiceMsgSize_Type()
)
ex2umsaAvgRecentSentVoiceMsgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaAvgRecentSentVoiceMsgSize.setStatus("current")
_Ex2umsaAvgRecentSubscribeCallDur_Type = Gauge32
_Ex2umsaAvgRecentSubscribeCallDur_Object = MibScalar
ex2umsaAvgRecentSubscribeCallDur = _Ex2umsaAvgRecentSubscribeCallDur_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 2),
    _Ex2umsaAvgRecentSubscribeCallDur_Type()
)
ex2umsaAvgRecentSubscribeCallDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaAvgRecentSubscribeCallDur.setStatus("current")
_Ex2umsaAvgSentVoiceMessageSize_Type = Gauge32
_Ex2umsaAvgSentVoiceMessageSize_Object = MibScalar
ex2umsaAvgSentVoiceMessageSize = _Ex2umsaAvgSentVoiceMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 3),
    _Ex2umsaAvgSentVoiceMessageSize_Type()
)
ex2umsaAvgSentVoiceMessageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaAvgSentVoiceMessageSize.setStatus("current")
_Ex2umsaAvgSubscriberCallDuration_Type = Gauge32
_Ex2umsaAvgSubscriberCallDuration_Object = MibScalar
ex2umsaAvgSubscriberCallDuration = _Ex2umsaAvgSubscriberCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 4),
    _Ex2umsaAvgSubscriberCallDuration_Type()
)
ex2umsaAvgSubscriberCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaAvgSubscriberCallDuration.setStatus("current")
_Ex2umsaCalendarAccessed_Type = Gauge32
_Ex2umsaCalendarAccessed_Object = MibScalar
ex2umsaCalendarAccessed = _Ex2umsaCalendarAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 5),
    _Ex2umsaCalendarAccessed_Type()
)
ex2umsaCalendarAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaCalendarAccessed.setStatus("current")
_Ex2umsaCalendarItemDetailRequest_Type = Gauge32
_Ex2umsaCalendarItemDetailRequest_Object = MibScalar
ex2umsaCalendarItemDetailRequest = _Ex2umsaCalendarItemDetailRequest_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 6),
    _Ex2umsaCalendarItemDetailRequest_Type()
)
ex2umsaCalendarItemDetailRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaCalendarItemDetailRequest.setStatus("current")
_Ex2umsaCalendarItemsHeard_Type = Gauge32
_Ex2umsaCalendarItemsHeard_Object = MibScalar
ex2umsaCalendarItemsHeard = _Ex2umsaCalendarItemsHeard_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 7),
    _Ex2umsaCalendarItemsHeard_Type()
)
ex2umsaCalendarItemsHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaCalendarItemsHeard.setStatus("current")
_Ex2umsaCalendarLateAttendance_Type = Gauge32
_Ex2umsaCalendarLateAttendance_Object = MibScalar
ex2umsaCalendarLateAttendance = _Ex2umsaCalendarLateAttendance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 8),
    _Ex2umsaCalendarLateAttendance_Type()
)
ex2umsaCalendarLateAttendance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaCalendarLateAttendance.setStatus("current")
_Ex2umsaCalledMeetingOrganizer_Type = Gauge32
_Ex2umsaCalledMeetingOrganizer_Object = MibScalar
ex2umsaCalledMeetingOrganizer = _Ex2umsaCalledMeetingOrganizer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 9),
    _Ex2umsaCalledMeetingOrganizer_Type()
)
ex2umsaCalledMeetingOrganizer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaCalledMeetingOrganizer.setStatus("current")
_Ex2umsaCalDiscCalDurUMAudioHrgls_Type = Gauge32
_Ex2umsaCalDiscCalDurUMAudioHrgls_Object = MibScalar
ex2umsaCalDiscCalDurUMAudioHrgls = _Ex2umsaCalDiscCalDurUMAudioHrgls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 10),
    _Ex2umsaCalDiscCalDurUMAudioHrgls_Type()
)
ex2umsaCalDiscCalDurUMAudioHrgls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaCalDiscCalDurUMAudioHrgls.setStatus("current")
_Ex2umsaCallDisUMOnIrrecvExtError_Type = Gauge32
_Ex2umsaCallDisUMOnIrrecvExtError_Object = MibScalar
ex2umsaCallDisUMOnIrrecvExtError = _Ex2umsaCallDisUMOnIrrecvExtError_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 11),
    _Ex2umsaCallDisUMOnIrrecvExtError_Type()
)
ex2umsaCallDisUMOnIrrecvExtError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaCallDisUMOnIrrecvExtError.setStatus("current")
_Ex2umsaContactItemsHeard_Type = Gauge32
_Ex2umsaContactItemsHeard_Object = MibScalar
ex2umsaContactItemsHeard = _Ex2umsaContactItemsHeard_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 12),
    _Ex2umsaContactItemsHeard_Type()
)
ex2umsaContactItemsHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaContactItemsHeard.setStatus("current")
_Ex2umsaContactsAccessed_Type = Gauge32
_Ex2umsaContactsAccessed_Object = MibScalar
ex2umsaContactsAccessed = _Ex2umsaContactsAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 13),
    _Ex2umsaContactsAccessed_Type()
)
ex2umsaContactsAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaContactsAccessed.setStatus("current")
_Ex2umsaDirectoryAccessed_Type = Gauge32
_Ex2umsaDirectoryAccessed_Object = MibScalar
ex2umsaDirectoryAccessed = _Ex2umsaDirectoryAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 14),
    _Ex2umsaDirectoryAccessed_Type()
)
ex2umsaDirectoryAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaDirectoryAccessed.setStatus("current")
_Ex2umsaDirAccsdSuccessDialName_Type = Gauge32
_Ex2umsaDirAccsdSuccessDialName_Object = MibScalar
ex2umsaDirAccsdSuccessDialName = _Ex2umsaDirAccsdSuccessDialName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 15),
    _Ex2umsaDirAccsdSuccessDialName_Type()
)
ex2umsaDirAccsdSuccessDialName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaDirAccsdSuccessDialName.setStatus("current")
_Ex2umsaDirAccsdSuccessSpokenName_Type = Gauge32
_Ex2umsaDirAccsdSuccessSpokenName_Object = MibScalar
ex2umsaDirAccsdSuccessSpokenName = _Ex2umsaDirAccsdSuccessSpokenName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 16),
    _Ex2umsaDirAccsdSuccessSpokenName_Type()
)
ex2umsaDirAccsdSuccessSpokenName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaDirAccsdSuccessSpokenName.setStatus("current")
_Ex2umsaDirAccsdByDialByName_Type = Gauge32
_Ex2umsaDirAccsdByDialByName_Object = MibScalar
ex2umsaDirAccsdByDialByName = _Ex2umsaDirAccsdByDialByName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 17),
    _Ex2umsaDirAccsdByDialByName_Type()
)
ex2umsaDirAccsdByDialByName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaDirAccsdByDialByName.setStatus("current")
_Ex2umsaDirAccsdByExtension_Type = Gauge32
_Ex2umsaDirAccsdByExtension_Object = MibScalar
ex2umsaDirAccsdByExtension = _Ex2umsaDirAccsdByExtension_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 18),
    _Ex2umsaDirAccsdByExtension_Type()
)
ex2umsaDirAccsdByExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaDirAccsdByExtension.setStatus("current")
_Ex2umsaDirAccsdBySpokenName_Type = Gauge32
_Ex2umsaDirAccsdBySpokenName_Object = MibScalar
ex2umsaDirAccsdBySpokenName = _Ex2umsaDirAccsdBySpokenName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 19),
    _Ex2umsaDirAccsdBySpokenName_Type()
)
ex2umsaDirAccsdBySpokenName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaDirAccsdBySpokenName.setStatus("current")
_Ex2umsaEmailMessageQueueAccessed_Type = Gauge32
_Ex2umsaEmailMessageQueueAccessed_Object = MibScalar
ex2umsaEmailMessageQueueAccessed = _Ex2umsaEmailMessageQueueAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 20),
    _Ex2umsaEmailMessageQueueAccessed_Type()
)
ex2umsaEmailMessageQueueAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaEmailMessageQueueAccessed.setStatus("current")
_Ex2umsaEmailMessagesDeleted_Type = Gauge32
_Ex2umsaEmailMessagesDeleted_Object = MibScalar
ex2umsaEmailMessagesDeleted = _Ex2umsaEmailMessagesDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 21),
    _Ex2umsaEmailMessagesDeleted_Type()
)
ex2umsaEmailMessagesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaEmailMessagesDeleted.setStatus("current")
_Ex2umsaEmailMessagesHeard_Type = Gauge32
_Ex2umsaEmailMessagesHeard_Object = MibScalar
ex2umsaEmailMessagesHeard = _Ex2umsaEmailMessagesHeard_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 22),
    _Ex2umsaEmailMessagesHeard_Type()
)
ex2umsaEmailMessagesHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaEmailMessagesHeard.setStatus("current")
_Ex2umsaForwardMessagesSent_Type = Gauge32
_Ex2umsaForwardMessagesSent_Object = MibScalar
ex2umsaForwardMessagesSent = _Ex2umsaForwardMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 23),
    _Ex2umsaForwardMessagesSent_Type()
)
ex2umsaForwardMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaForwardMessagesSent.setStatus("current")
_Ex2umsaLaunchedCalls_Type = Gauge32
_Ex2umsaLaunchedCalls_Object = MibScalar
ex2umsaLaunchedCalls = _Ex2umsaLaunchedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 24),
    _Ex2umsaLaunchedCalls_Type()
)
ex2umsaLaunchedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaLaunchedCalls.setStatus("current")
_Ex2umsaMeetingsAccepted_Type = Gauge32
_Ex2umsaMeetingsAccepted_Object = MibScalar
ex2umsaMeetingsAccepted = _Ex2umsaMeetingsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 25),
    _Ex2umsaMeetingsAccepted_Type()
)
ex2umsaMeetingsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaMeetingsAccepted.setStatus("current")
_Ex2umsaMeetingsDeclined_Type = Gauge32
_Ex2umsaMeetingsDeclined_Object = MibScalar
ex2umsaMeetingsDeclined = _Ex2umsaMeetingsDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 26),
    _Ex2umsaMeetingsDeclined_Type()
)
ex2umsaMeetingsDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaMeetingsDeclined.setStatus("current")
_Ex2umsaRepliedToOrganizer_Type = Gauge32
_Ex2umsaRepliedToOrganizer_Object = MibScalar
ex2umsaRepliedToOrganizer = _Ex2umsaRepliedToOrganizer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 27),
    _Ex2umsaRepliedToOrganizer_Type()
)
ex2umsaRepliedToOrganizer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaRepliedToOrganizer.setStatus("current")
_Ex2umsaReplyMessagesSent_Type = Gauge32
_Ex2umsaReplyMessagesSent_Object = MibScalar
ex2umsaReplyMessagesSent = _Ex2umsaReplyMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 28),
    _Ex2umsaReplyMessagesSent_Type()
)
ex2umsaReplyMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaReplyMessagesSent.setStatus("current")
_Ex2umsaSubscriberAuthentFailure_Type = Gauge32
_Ex2umsaSubscriberAuthentFailure_Object = MibScalar
ex2umsaSubscriberAuthentFailure = _Ex2umsaSubscriberAuthentFailure_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 29),
    _Ex2umsaSubscriberAuthentFailure_Type()
)
ex2umsaSubscriberAuthentFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaSubscriberAuthentFailure.setStatus("current")
_Ex2umsaSubscriberLogonFailures_Type = Gauge32
_Ex2umsaSubscriberLogonFailures_Object = MibScalar
ex2umsaSubscriberLogonFailures = _Ex2umsaSubscriberLogonFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 30),
    _Ex2umsaSubscriberLogonFailures_Type()
)
ex2umsaSubscriberLogonFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaSubscriberLogonFailures.setStatus("current")
_Ex2umsaSubscriberLogons_Type = Gauge32
_Ex2umsaSubscriberLogons_Object = MibScalar
ex2umsaSubscriberLogons = _Ex2umsaSubscriberLogons_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 31),
    _Ex2umsaSubscriberLogons_Type()
)
ex2umsaSubscriberLogons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaSubscriberLogons.setStatus("current")
_Ex2umsaVoiceMessageQueueAccessed_Type = Gauge32
_Ex2umsaVoiceMessageQueueAccessed_Object = MibScalar
ex2umsaVoiceMessageQueueAccessed = _Ex2umsaVoiceMessageQueueAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 32),
    _Ex2umsaVoiceMessageQueueAccessed_Type()
)
ex2umsaVoiceMessageQueueAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaVoiceMessageQueueAccessed.setStatus("current")
_Ex2umsaVoiceMessagesDeleted_Type = Gauge32
_Ex2umsaVoiceMessagesDeleted_Object = MibScalar
ex2umsaVoiceMessagesDeleted = _Ex2umsaVoiceMessagesDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 33),
    _Ex2umsaVoiceMessagesDeleted_Type()
)
ex2umsaVoiceMessagesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaVoiceMessagesDeleted.setStatus("current")
_Ex2umsaVoiceMessagesHeard_Type = Gauge32
_Ex2umsaVoiceMessagesHeard_Object = MibScalar
ex2umsaVoiceMessagesHeard = _Ex2umsaVoiceMessagesHeard_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 34),
    _Ex2umsaVoiceMessagesHeard_Type()
)
ex2umsaVoiceMessagesHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaVoiceMessagesHeard.setStatus("current")
_Ex2umsaVoiceMessagesSent_Type = Gauge32
_Ex2umsaVoiceMessagesSent_Object = MibScalar
ex2umsaVoiceMessagesSent = _Ex2umsaVoiceMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 70, 35),
    _Ex2umsaVoiceMessagesSent_Type()
)
ex2umsaVoiceMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2umsaVoiceMessagesSent.setStatus("current")
_Ex2WS_ObjectIdentity = ObjectIdentity
ex2WS = _Ex2WS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71)
)
_Ex2WSActiveSubscriptions_Type = Gauge32
_Ex2WSActiveSubscriptions_Object = MibScalar
ex2WSActiveSubscriptions = _Ex2WSActiveSubscriptions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 1),
    _Ex2WSActiveSubscriptions_Type()
)
ex2WSActiveSubscriptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSActiveSubscriptions.setStatus("current")
_Ex2WSAddDelegateRequests_Type = Gauge32
_Ex2WSAddDelegateRequests_Object = MibScalar
ex2WSAddDelegateRequests = _Ex2WSAddDelegateRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 2),
    _Ex2WSAddDelegateRequests_Type()
)
ex2WSAddDelegateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSAddDelegateRequests.setStatus("current")
_Ex2WSAddDelegateRequestsPerSec_Type = Gauge32
_Ex2WSAddDelegateRequestsPerSec_Object = MibScalar
ex2WSAddDelegateRequestsPerSec = _Ex2WSAddDelegateRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 3),
    _Ex2WSAddDelegateRequestsPerSec_Type()
)
ex2WSAddDelegateRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSAddDelegateRequestsPerSec.setStatus("current")
_Ex2WSConvertIdRequests_Type = Gauge32
_Ex2WSConvertIdRequests_Object = MibScalar
ex2WSConvertIdRequests = _Ex2WSConvertIdRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 4),
    _Ex2WSConvertIdRequests_Type()
)
ex2WSConvertIdRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSConvertIdRequests.setStatus("current")
_Ex2WSConvertIdRequestsPerSec_Type = Gauge32
_Ex2WSConvertIdRequestsPerSec_Object = MibScalar
ex2WSConvertIdRequestsPerSec = _Ex2WSConvertIdRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 5),
    _Ex2WSConvertIdRequestsPerSec_Type()
)
ex2WSConvertIdRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSConvertIdRequestsPerSec.setStatus("current")
_Ex2WSCopyFolderRequests_Type = Gauge32
_Ex2WSCopyFolderRequests_Object = MibScalar
ex2WSCopyFolderRequests = _Ex2WSCopyFolderRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 6),
    _Ex2WSCopyFolderRequests_Type()
)
ex2WSCopyFolderRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCopyFolderRequests.setStatus("current")
_Ex2WSCopyFolderRequestsPerSec_Type = Gauge32
_Ex2WSCopyFolderRequestsPerSec_Object = MibScalar
ex2WSCopyFolderRequestsPerSec = _Ex2WSCopyFolderRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 7),
    _Ex2WSCopyFolderRequestsPerSec_Type()
)
ex2WSCopyFolderRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCopyFolderRequestsPerSec.setStatus("current")
_Ex2WSCopyItemRequests_Type = Gauge32
_Ex2WSCopyItemRequests_Object = MibScalar
ex2WSCopyItemRequests = _Ex2WSCopyItemRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 8),
    _Ex2WSCopyItemRequests_Type()
)
ex2WSCopyItemRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCopyItemRequests.setStatus("current")
_Ex2WSCopyItemRequestsPerSec_Type = Gauge32
_Ex2WSCopyItemRequestsPerSec_Object = MibScalar
ex2WSCopyItemRequestsPerSec = _Ex2WSCopyItemRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 9),
    _Ex2WSCopyItemRequestsPerSec_Type()
)
ex2WSCopyItemRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCopyItemRequestsPerSec.setStatus("current")
_Ex2WSCreateAttachmentRequests_Type = Gauge32
_Ex2WSCreateAttachmentRequests_Object = MibScalar
ex2WSCreateAttachmentRequests = _Ex2WSCreateAttachmentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 10),
    _Ex2WSCreateAttachmentRequests_Type()
)
ex2WSCreateAttachmentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCreateAttachmentRequests.setStatus("current")
_Ex2WSCreateAttachRequestsPerSec_Type = Gauge32
_Ex2WSCreateAttachRequestsPerSec_Object = MibScalar
ex2WSCreateAttachRequestsPerSec = _Ex2WSCreateAttachRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 11),
    _Ex2WSCreateAttachRequestsPerSec_Type()
)
ex2WSCreateAttachRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCreateAttachRequestsPerSec.setStatus("current")
_Ex2WSCreateFolderRequests_Type = Gauge32
_Ex2WSCreateFolderRequests_Object = MibScalar
ex2WSCreateFolderRequests = _Ex2WSCreateFolderRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 12),
    _Ex2WSCreateFolderRequests_Type()
)
ex2WSCreateFolderRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCreateFolderRequests.setStatus("current")
_Ex2WSCreateFolderRequestsPerSec_Type = Gauge32
_Ex2WSCreateFolderRequestsPerSec_Object = MibScalar
ex2WSCreateFolderRequestsPerSec = _Ex2WSCreateFolderRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 13),
    _Ex2WSCreateFolderRequestsPerSec_Type()
)
ex2WSCreateFolderRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCreateFolderRequestsPerSec.setStatus("current")
_Ex2WSCreateItemRequests_Type = Gauge32
_Ex2WSCreateItemRequests_Object = MibScalar
ex2WSCreateItemRequests = _Ex2WSCreateItemRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 14),
    _Ex2WSCreateItemRequests_Type()
)
ex2WSCreateItemRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCreateItemRequests.setStatus("current")
_Ex2WSCreateItemRequestsPerSec_Type = Gauge32
_Ex2WSCreateItemRequestsPerSec_Object = MibScalar
ex2WSCreateItemRequestsPerSec = _Ex2WSCreateItemRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 15),
    _Ex2WSCreateItemRequestsPerSec_Type()
)
ex2WSCreateItemRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCreateItemRequestsPerSec.setStatus("current")
_Ex2WSCreateManagedFolderRequests_Type = Gauge32
_Ex2WSCreateManagedFolderRequests_Object = MibScalar
ex2WSCreateManagedFolderRequests = _Ex2WSCreateManagedFolderRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 16),
    _Ex2WSCreateManagedFolderRequests_Type()
)
ex2WSCreateManagedFolderRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCreateManagedFolderRequests.setStatus("current")
_Ex2WSCreateManageFoldReqstPerSec_Type = Gauge32
_Ex2WSCreateManageFoldReqstPerSec_Object = MibScalar
ex2WSCreateManageFoldReqstPerSec = _Ex2WSCreateManageFoldReqstPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 17),
    _Ex2WSCreateManageFoldReqstPerSec_Type()
)
ex2WSCreateManageFoldReqstPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSCreateManageFoldReqstPerSec.setStatus("current")
_Ex2WSDeleteAttachmentRequests_Type = Gauge32
_Ex2WSDeleteAttachmentRequests_Object = MibScalar
ex2WSDeleteAttachmentRequests = _Ex2WSDeleteAttachmentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 18),
    _Ex2WSDeleteAttachmentRequests_Type()
)
ex2WSDeleteAttachmentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSDeleteAttachmentRequests.setStatus("current")
_Ex2WSDeleteAttachmentReqstPerSec_Type = Gauge32
_Ex2WSDeleteAttachmentReqstPerSec_Object = MibScalar
ex2WSDeleteAttachmentReqstPerSec = _Ex2WSDeleteAttachmentReqstPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 19),
    _Ex2WSDeleteAttachmentReqstPerSec_Type()
)
ex2WSDeleteAttachmentReqstPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSDeleteAttachmentReqstPerSec.setStatus("current")
_Ex2WSDeleteFolderRequests_Type = Gauge32
_Ex2WSDeleteFolderRequests_Object = MibScalar
ex2WSDeleteFolderRequests = _Ex2WSDeleteFolderRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 20),
    _Ex2WSDeleteFolderRequests_Type()
)
ex2WSDeleteFolderRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSDeleteFolderRequests.setStatus("current")
_Ex2WSDeleteFolderRequestsPerSec_Type = Gauge32
_Ex2WSDeleteFolderRequestsPerSec_Object = MibScalar
ex2WSDeleteFolderRequestsPerSec = _Ex2WSDeleteFolderRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 21),
    _Ex2WSDeleteFolderRequestsPerSec_Type()
)
ex2WSDeleteFolderRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSDeleteFolderRequestsPerSec.setStatus("current")
_Ex2WSDeleteItemRequests_Type = Gauge32
_Ex2WSDeleteItemRequests_Object = MibScalar
ex2WSDeleteItemRequests = _Ex2WSDeleteItemRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 22),
    _Ex2WSDeleteItemRequests_Type()
)
ex2WSDeleteItemRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSDeleteItemRequests.setStatus("current")
_Ex2WSDeleteItemRequestsPerSec_Type = Gauge32
_Ex2WSDeleteItemRequestsPerSec_Object = MibScalar
ex2WSDeleteItemRequestsPerSec = _Ex2WSDeleteItemRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 23),
    _Ex2WSDeleteItemRequestsPerSec_Type()
)
ex2WSDeleteItemRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSDeleteItemRequestsPerSec.setStatus("current")
_Ex2WSExpandDLRequests_Type = Gauge32
_Ex2WSExpandDLRequests_Object = MibScalar
ex2WSExpandDLRequests = _Ex2WSExpandDLRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 24),
    _Ex2WSExpandDLRequests_Type()
)
ex2WSExpandDLRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSExpandDLRequests.setStatus("current")
_Ex2WSExpandDLRequestsPerSec_Type = Gauge32
_Ex2WSExpandDLRequestsPerSec_Object = MibScalar
ex2WSExpandDLRequestsPerSec = _Ex2WSExpandDLRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 25),
    _Ex2WSExpandDLRequestsPerSec_Type()
)
ex2WSExpandDLRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSExpandDLRequestsPerSec.setStatus("current")
_Ex2WSFindFolderRequests_Type = Gauge32
_Ex2WSFindFolderRequests_Object = MibScalar
ex2WSFindFolderRequests = _Ex2WSFindFolderRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 26),
    _Ex2WSFindFolderRequests_Type()
)
ex2WSFindFolderRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFindFolderRequests.setStatus("current")
_Ex2WSFindFolderRequestsPerSec_Type = Gauge32
_Ex2WSFindFolderRequestsPerSec_Object = MibScalar
ex2WSFindFolderRequestsPerSec = _Ex2WSFindFolderRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 27),
    _Ex2WSFindFolderRequestsPerSec_Type()
)
ex2WSFindFolderRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFindFolderRequestsPerSec.setStatus("current")
_Ex2WSFindItemRequests_Type = Gauge32
_Ex2WSFindItemRequests_Object = MibScalar
ex2WSFindItemRequests = _Ex2WSFindItemRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 28),
    _Ex2WSFindItemRequests_Type()
)
ex2WSFindItemRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFindItemRequests.setStatus("current")
_Ex2WSFindItemRequestsPerSec_Type = Gauge32
_Ex2WSFindItemRequestsPerSec_Object = MibScalar
ex2WSFindItemRequestsPerSec = _Ex2WSFindItemRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 29),
    _Ex2WSFindItemRequestsPerSec_Type()
)
ex2WSFindItemRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFindItemRequestsPerSec.setStatus("current")
_Ex2WSFoldersCopied_Type = Gauge32
_Ex2WSFoldersCopied_Object = MibScalar
ex2WSFoldersCopied = _Ex2WSFoldersCopied_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 30),
    _Ex2WSFoldersCopied_Type()
)
ex2WSFoldersCopied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersCopied.setStatus("current")
_Ex2WSFoldersCopiedPerSec_Type = Gauge32
_Ex2WSFoldersCopiedPerSec_Object = MibScalar
ex2WSFoldersCopiedPerSec = _Ex2WSFoldersCopiedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 31),
    _Ex2WSFoldersCopiedPerSec_Type()
)
ex2WSFoldersCopiedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersCopiedPerSec.setStatus("current")
_Ex2WSFoldersCreated_Type = Gauge32
_Ex2WSFoldersCreated_Object = MibScalar
ex2WSFoldersCreated = _Ex2WSFoldersCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 32),
    _Ex2WSFoldersCreated_Type()
)
ex2WSFoldersCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersCreated.setStatus("current")
_Ex2WSFoldersCreatedPerSec_Type = Gauge32
_Ex2WSFoldersCreatedPerSec_Object = MibScalar
ex2WSFoldersCreatedPerSec = _Ex2WSFoldersCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 33),
    _Ex2WSFoldersCreatedPerSec_Type()
)
ex2WSFoldersCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersCreatedPerSec.setStatus("current")
_Ex2WSFoldersDeleted_Type = Gauge32
_Ex2WSFoldersDeleted_Object = MibScalar
ex2WSFoldersDeleted = _Ex2WSFoldersDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 34),
    _Ex2WSFoldersDeleted_Type()
)
ex2WSFoldersDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersDeleted.setStatus("current")
_Ex2WSFoldersDeletedPerSec_Type = Gauge32
_Ex2WSFoldersDeletedPerSec_Object = MibScalar
ex2WSFoldersDeletedPerSec = _Ex2WSFoldersDeletedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 35),
    _Ex2WSFoldersDeletedPerSec_Type()
)
ex2WSFoldersDeletedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersDeletedPerSec.setStatus("current")
_Ex2WSFoldersMoved_Type = Gauge32
_Ex2WSFoldersMoved_Object = MibScalar
ex2WSFoldersMoved = _Ex2WSFoldersMoved_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 36),
    _Ex2WSFoldersMoved_Type()
)
ex2WSFoldersMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersMoved.setStatus("current")
_Ex2WSFoldersMovedPerSec_Type = Gauge32
_Ex2WSFoldersMovedPerSec_Object = MibScalar
ex2WSFoldersMovedPerSec = _Ex2WSFoldersMovedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 37),
    _Ex2WSFoldersMovedPerSec_Type()
)
ex2WSFoldersMovedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersMovedPerSec.setStatus("current")
_Ex2WSFoldersRead_Type = Gauge32
_Ex2WSFoldersRead_Object = MibScalar
ex2WSFoldersRead = _Ex2WSFoldersRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 38),
    _Ex2WSFoldersRead_Type()
)
ex2WSFoldersRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersRead.setStatus("current")
_Ex2WSFoldersSentPerSec_Type = Gauge32
_Ex2WSFoldersSentPerSec_Object = MibScalar
ex2WSFoldersSentPerSec = _Ex2WSFoldersSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 39),
    _Ex2WSFoldersSentPerSec_Type()
)
ex2WSFoldersSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersSentPerSec.setStatus("current")
_Ex2WSFoldersSyncedPerSec_Type = Gauge32
_Ex2WSFoldersSyncedPerSec_Object = MibScalar
ex2WSFoldersSyncedPerSec = _Ex2WSFoldersSyncedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 40),
    _Ex2WSFoldersSyncedPerSec_Type()
)
ex2WSFoldersSyncedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersSyncedPerSec.setStatus("current")
_Ex2WSFoldersSynchronized_Type = Gauge32
_Ex2WSFoldersSynchronized_Object = MibScalar
ex2WSFoldersSynchronized = _Ex2WSFoldersSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 41),
    _Ex2WSFoldersSynchronized_Type()
)
ex2WSFoldersSynchronized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersSynchronized.setStatus("current")
_Ex2WSFoldersUpdated_Type = Gauge32
_Ex2WSFoldersUpdated_Object = MibScalar
ex2WSFoldersUpdated = _Ex2WSFoldersUpdated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 42),
    _Ex2WSFoldersUpdated_Type()
)
ex2WSFoldersUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersUpdated.setStatus("current")
_Ex2WSFoldersUpdatedPerSec_Type = Gauge32
_Ex2WSFoldersUpdatedPerSec_Object = MibScalar
ex2WSFoldersUpdatedPerSec = _Ex2WSFoldersUpdatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 43),
    _Ex2WSFoldersUpdatedPerSec_Type()
)
ex2WSFoldersUpdatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSFoldersUpdatedPerSec.setStatus("current")
_Ex2WSGetAttachmentRequests_Type = Gauge32
_Ex2WSGetAttachmentRequests_Object = MibScalar
ex2WSGetAttachmentRequests = _Ex2WSGetAttachmentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 44),
    _Ex2WSGetAttachmentRequests_Type()
)
ex2WSGetAttachmentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSGetAttachmentRequests.setStatus("current")
_Ex2WSGetAttachmentRequestsPerSec_Type = Gauge32
_Ex2WSGetAttachmentRequestsPerSec_Object = MibScalar
ex2WSGetAttachmentRequestsPerSec = _Ex2WSGetAttachmentRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 45),
    _Ex2WSGetAttachmentRequestsPerSec_Type()
)
ex2WSGetAttachmentRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSGetAttachmentRequestsPerSec.setStatus("current")
_Ex2WSGetDelegateRequests_Type = Gauge32
_Ex2WSGetDelegateRequests_Object = MibScalar
ex2WSGetDelegateRequests = _Ex2WSGetDelegateRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 46),
    _Ex2WSGetDelegateRequests_Type()
)
ex2WSGetDelegateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSGetDelegateRequests.setStatus("current")
_Ex2WSGetDelegateRequestsPerSec_Type = Gauge32
_Ex2WSGetDelegateRequestsPerSec_Object = MibScalar
ex2WSGetDelegateRequestsPerSec = _Ex2WSGetDelegateRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 47),
    _Ex2WSGetDelegateRequestsPerSec_Type()
)
ex2WSGetDelegateRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSGetDelegateRequestsPerSec.setStatus("current")
_Ex2WSGetEventsRequests_Type = Gauge32
_Ex2WSGetEventsRequests_Object = MibScalar
ex2WSGetEventsRequests = _Ex2WSGetEventsRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 48),
    _Ex2WSGetEventsRequests_Type()
)
ex2WSGetEventsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSGetEventsRequests.setStatus("current")
_Ex2WSGetEventsRequestsPerSec_Type = Gauge32
_Ex2WSGetEventsRequestsPerSec_Object = MibScalar
ex2WSGetEventsRequestsPerSec = _Ex2WSGetEventsRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 49),
    _Ex2WSGetEventsRequestsPerSec_Type()
)
ex2WSGetEventsRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSGetEventsRequestsPerSec.setStatus("current")
_Ex2WSGetFolderRequests_Type = Gauge32
_Ex2WSGetFolderRequests_Object = MibScalar
ex2WSGetFolderRequests = _Ex2WSGetFolderRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 50),
    _Ex2WSGetFolderRequests_Type()
)
ex2WSGetFolderRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSGetFolderRequests.setStatus("current")
_Ex2WSGetFolderRequestsPerSec_Type = Gauge32
_Ex2WSGetFolderRequestsPerSec_Object = MibScalar
ex2WSGetFolderRequestsPerSec = _Ex2WSGetFolderRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 51),
    _Ex2WSGetFolderRequestsPerSec_Type()
)
ex2WSGetFolderRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSGetFolderRequestsPerSec.setStatus("current")
_Ex2WSGetItemRequests_Type = Gauge32
_Ex2WSGetItemRequests_Object = MibScalar
ex2WSGetItemRequests = _Ex2WSGetItemRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 52),
    _Ex2WSGetItemRequests_Type()
)
ex2WSGetItemRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSGetItemRequests.setStatus("current")
_Ex2WSGetItemRequestsPerSec_Type = Gauge32
_Ex2WSGetItemRequestsPerSec_Object = MibScalar
ex2WSGetItemRequestsPerSec = _Ex2WSGetItemRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 53),
    _Ex2WSGetItemRequestsPerSec_Type()
)
ex2WSGetItemRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSGetItemRequestsPerSec.setStatus("current")
_Ex2WSIdsConvertedPerSec_Type = Gauge32
_Ex2WSIdsConvertedPerSec_Object = MibScalar
ex2WSIdsConvertedPerSec = _Ex2WSIdsConvertedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 54),
    _Ex2WSIdsConvertedPerSec_Type()
)
ex2WSIdsConvertedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSIdsConvertedPerSec.setStatus("current")
_Ex2WSItemsCopied_Type = Gauge32
_Ex2WSItemsCopied_Object = MibScalar
ex2WSItemsCopied = _Ex2WSItemsCopied_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 55),
    _Ex2WSItemsCopied_Type()
)
ex2WSItemsCopied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsCopied.setStatus("current")
_Ex2WSItemsCopiedPerSec_Type = Gauge32
_Ex2WSItemsCopiedPerSec_Object = MibScalar
ex2WSItemsCopiedPerSec = _Ex2WSItemsCopiedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 56),
    _Ex2WSItemsCopiedPerSec_Type()
)
ex2WSItemsCopiedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsCopiedPerSec.setStatus("current")
_Ex2WSItemsCreated_Type = Gauge32
_Ex2WSItemsCreated_Object = MibScalar
ex2WSItemsCreated = _Ex2WSItemsCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 57),
    _Ex2WSItemsCreated_Type()
)
ex2WSItemsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsCreated.setStatus("current")
_Ex2WSItemsCreatedPerSec_Type = Gauge32
_Ex2WSItemsCreatedPerSec_Object = MibScalar
ex2WSItemsCreatedPerSec = _Ex2WSItemsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 58),
    _Ex2WSItemsCreatedPerSec_Type()
)
ex2WSItemsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsCreatedPerSec.setStatus("current")
_Ex2WSItemsDeleted_Type = Gauge32
_Ex2WSItemsDeleted_Object = MibScalar
ex2WSItemsDeleted = _Ex2WSItemsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 59),
    _Ex2WSItemsDeleted_Type()
)
ex2WSItemsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsDeleted.setStatus("current")
_Ex2WSItemsDeletedPerSec_Type = Gauge32
_Ex2WSItemsDeletedPerSec_Object = MibScalar
ex2WSItemsDeletedPerSec = _Ex2WSItemsDeletedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 60),
    _Ex2WSItemsDeletedPerSec_Type()
)
ex2WSItemsDeletedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsDeletedPerSec.setStatus("current")
_Ex2WSItemsMoved_Type = Gauge32
_Ex2WSItemsMoved_Object = MibScalar
ex2WSItemsMoved = _Ex2WSItemsMoved_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 61),
    _Ex2WSItemsMoved_Type()
)
ex2WSItemsMoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsMoved.setStatus("current")
_Ex2WSItemsMovedPerSec_Type = Gauge32
_Ex2WSItemsMovedPerSec_Object = MibScalar
ex2WSItemsMovedPerSec = _Ex2WSItemsMovedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 62),
    _Ex2WSItemsMovedPerSec_Type()
)
ex2WSItemsMovedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsMovedPerSec.setStatus("current")
_Ex2WSItemsRead_Type = Gauge32
_Ex2WSItemsRead_Object = MibScalar
ex2WSItemsRead = _Ex2WSItemsRead_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 63),
    _Ex2WSItemsRead_Type()
)
ex2WSItemsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsRead.setStatus("current")
_Ex2WSItemsReadPerSec_Type = Gauge32
_Ex2WSItemsReadPerSec_Object = MibScalar
ex2WSItemsReadPerSec = _Ex2WSItemsReadPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 64),
    _Ex2WSItemsReadPerSec_Type()
)
ex2WSItemsReadPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsReadPerSec.setStatus("current")
_Ex2WSItemsSent_Type = Gauge32
_Ex2WSItemsSent_Object = MibScalar
ex2WSItemsSent = _Ex2WSItemsSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 65),
    _Ex2WSItemsSent_Type()
)
ex2WSItemsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsSent.setStatus("current")
_Ex2WSItemsSentPerSec_Type = Gauge32
_Ex2WSItemsSentPerSec_Object = MibScalar
ex2WSItemsSentPerSec = _Ex2WSItemsSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 66),
    _Ex2WSItemsSentPerSec_Type()
)
ex2WSItemsSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsSentPerSec.setStatus("current")
_Ex2WSItemsSyncedPerSec_Type = Gauge32
_Ex2WSItemsSyncedPerSec_Object = MibScalar
ex2WSItemsSyncedPerSec = _Ex2WSItemsSyncedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 67),
    _Ex2WSItemsSyncedPerSec_Type()
)
ex2WSItemsSyncedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsSyncedPerSec.setStatus("current")
_Ex2WSItemsSynchronized_Type = Gauge32
_Ex2WSItemsSynchronized_Object = MibScalar
ex2WSItemsSynchronized = _Ex2WSItemsSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 68),
    _Ex2WSItemsSynchronized_Type()
)
ex2WSItemsSynchronized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsSynchronized.setStatus("current")
_Ex2WSItemsUpdated_Type = Gauge32
_Ex2WSItemsUpdated_Object = MibScalar
ex2WSItemsUpdated = _Ex2WSItemsUpdated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 69),
    _Ex2WSItemsUpdated_Type()
)
ex2WSItemsUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsUpdated.setStatus("current")
_Ex2WSItemsUpdatedPerSec_Type = Gauge32
_Ex2WSItemsUpdatedPerSec_Object = MibScalar
ex2WSItemsUpdatedPerSec = _Ex2WSItemsUpdatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 70),
    _Ex2WSItemsUpdatedPerSec_Type()
)
ex2WSItemsUpdatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSItemsUpdatedPerSec.setStatus("current")
_Ex2WSMoveFolderRequests_Type = Gauge32
_Ex2WSMoveFolderRequests_Object = MibScalar
ex2WSMoveFolderRequests = _Ex2WSMoveFolderRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 71),
    _Ex2WSMoveFolderRequests_Type()
)
ex2WSMoveFolderRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSMoveFolderRequests.setStatus("current")
_Ex2WSMoveFolderRequestsPerSec_Type = Gauge32
_Ex2WSMoveFolderRequestsPerSec_Object = MibScalar
ex2WSMoveFolderRequestsPerSec = _Ex2WSMoveFolderRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 72),
    _Ex2WSMoveFolderRequestsPerSec_Type()
)
ex2WSMoveFolderRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSMoveFolderRequestsPerSec.setStatus("current")
_Ex2WSMoveItemRequests_Type = Gauge32
_Ex2WSMoveItemRequests_Object = MibScalar
ex2WSMoveItemRequests = _Ex2WSMoveItemRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 73),
    _Ex2WSMoveItemRequests_Type()
)
ex2WSMoveItemRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSMoveItemRequests.setStatus("current")
_Ex2WSMoveItemRequestsPerSec_Type = Gauge32
_Ex2WSMoveItemRequestsPerSec_Object = MibScalar
ex2WSMoveItemRequestsPerSec = _Ex2WSMoveItemRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 74),
    _Ex2WSMoveItemRequestsPerSec_Type()
)
ex2WSMoveItemRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSMoveItemRequestsPerSec.setStatus("current")
_Ex2WSNumberOfCurrentProxyCalls_Type = Gauge32
_Ex2WSNumberOfCurrentProxyCalls_Object = MibScalar
ex2WSNumberOfCurrentProxyCalls = _Ex2WSNumberOfCurrentProxyCalls_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 75),
    _Ex2WSNumberOfCurrentProxyCalls_Type()
)
ex2WSNumberOfCurrentProxyCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSNumberOfCurrentProxyCalls.setStatus("current")
_Ex2WSNumberOfProxyReqstPerSecond_Type = Gauge32
_Ex2WSNumberOfProxyReqstPerSecond_Object = MibScalar
ex2WSNumberOfProxyReqstPerSecond = _Ex2WSNumberOfProxyReqstPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 76),
    _Ex2WSNumberOfProxyReqstPerSecond_Type()
)
ex2WSNumberOfProxyReqstPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSNumberOfProxyReqstPerSecond.setStatus("current")
_Ex2WSNumbrProxyFailoverPerSecond_Type = Gauge32
_Ex2WSNumbrProxyFailoverPerSecond_Object = MibScalar
ex2WSNumbrProxyFailoverPerSecond = _Ex2WSNumbrProxyFailoverPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 77),
    _Ex2WSNumbrProxyFailoverPerSecond_Type()
)
ex2WSNumbrProxyFailoverPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSNumbrProxyFailoverPerSecond.setStatus("current")
_Ex2WSProcessID_Type = Gauge32
_Ex2WSProcessID_Object = MibScalar
ex2WSProcessID = _Ex2WSProcessID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 78),
    _Ex2WSProcessID_Type()
)
ex2WSProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSProcessID.setStatus("current")
_Ex2WSProxyAverageResponseTime_Type = Gauge32
_Ex2WSProxyAverageResponseTime_Object = MibScalar
ex2WSProxyAverageResponseTime = _Ex2WSProxyAverageResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 79),
    _Ex2WSProxyAverageResponseTime_Type()
)
ex2WSProxyAverageResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSProxyAverageResponseTime.setStatus("current")
_Ex2WSProxyAverageResponseTimNum1_Type = Gauge32
_Ex2WSProxyAverageResponseTimNum1_Object = MibScalar
ex2WSProxyAverageResponseTimNum1 = _Ex2WSProxyAverageResponseTimNum1_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 80),
    _Ex2WSProxyAverageResponseTimNum1_Type()
)
ex2WSProxyAverageResponseTimNum1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSProxyAverageResponseTimNum1.setStatus("current")
_Ex2WSPushNotificationsFailed_Type = Gauge32
_Ex2WSPushNotificationsFailed_Object = MibScalar
ex2WSPushNotificationsFailed = _Ex2WSPushNotificationsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 81),
    _Ex2WSPushNotificationsFailed_Type()
)
ex2WSPushNotificationsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSPushNotificationsFailed.setStatus("current")
_Ex2WSPushNotificationsSucceeded_Type = Gauge32
_Ex2WSPushNotificationsSucceeded_Object = MibScalar
ex2WSPushNotificationsSucceeded = _Ex2WSPushNotificationsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 82),
    _Ex2WSPushNotificationsSucceeded_Type()
)
ex2WSPushNotificationsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSPushNotificationsSucceeded.setStatus("current")
_Ex2WSRemoveDelegateRequests_Type = Gauge32
_Ex2WSRemoveDelegateRequests_Object = MibScalar
ex2WSRemoveDelegateRequests = _Ex2WSRemoveDelegateRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 83),
    _Ex2WSRemoveDelegateRequests_Type()
)
ex2WSRemoveDelegateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSRemoveDelegateRequests.setStatus("current")
_Ex2WSRemoveDelegateRequestPerSec_Type = Gauge32
_Ex2WSRemoveDelegateRequestPerSec_Object = MibScalar
ex2WSRemoveDelegateRequestPerSec = _Ex2WSRemoveDelegateRequestPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 84),
    _Ex2WSRemoveDelegateRequestPerSec_Type()
)
ex2WSRemoveDelegateRequestPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSRemoveDelegateRequestPerSec.setStatus("current")
_Ex2WSRequestsPerSec_Type = Gauge32
_Ex2WSRequestsPerSec_Object = MibScalar
ex2WSRequestsPerSec = _Ex2WSRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 85),
    _Ex2WSRequestsPerSec_Type()
)
ex2WSRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSRequestsPerSec.setStatus("current")
_Ex2WSResolveNamesRequests_Type = Gauge32
_Ex2WSResolveNamesRequests_Object = MibScalar
ex2WSResolveNamesRequests = _Ex2WSResolveNamesRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 86),
    _Ex2WSResolveNamesRequests_Type()
)
ex2WSResolveNamesRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSResolveNamesRequests.setStatus("current")
_Ex2WSResolveNamesRequestsPerSec_Type = Gauge32
_Ex2WSResolveNamesRequestsPerSec_Object = MibScalar
ex2WSResolveNamesRequestsPerSec = _Ex2WSResolveNamesRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 87),
    _Ex2WSResolveNamesRequestsPerSec_Type()
)
ex2WSResolveNamesRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSResolveNamesRequestsPerSec.setStatus("current")
_Ex2WSSendItemRequests_Type = Gauge32
_Ex2WSSendItemRequests_Object = MibScalar
ex2WSSendItemRequests = _Ex2WSSendItemRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 88),
    _Ex2WSSendItemRequests_Type()
)
ex2WSSendItemRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSSendItemRequests.setStatus("current")
_Ex2WSSendItemRequestsPerSec_Type = Gauge32
_Ex2WSSendItemRequestsPerSec_Object = MibScalar
ex2WSSendItemRequestsPerSec = _Ex2WSSendItemRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 89),
    _Ex2WSSendItemRequestsPerSec_Type()
)
ex2WSSendItemRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSSendItemRequestsPerSec.setStatus("current")
_Ex2WSSubscribeRequests_Type = Gauge32
_Ex2WSSubscribeRequests_Object = MibScalar
ex2WSSubscribeRequests = _Ex2WSSubscribeRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 90),
    _Ex2WSSubscribeRequests_Type()
)
ex2WSSubscribeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSSubscribeRequests.setStatus("current")
_Ex2WSSubscribeRequestsPerSec_Type = Gauge32
_Ex2WSSubscribeRequestsPerSec_Object = MibScalar
ex2WSSubscribeRequestsPerSec = _Ex2WSSubscribeRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 91),
    _Ex2WSSubscribeRequestsPerSec_Type()
)
ex2WSSubscribeRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSSubscribeRequestsPerSec.setStatus("current")
_Ex2WSSyncFolderHierarchyRequests_Type = Gauge32
_Ex2WSSyncFolderHierarchyRequests_Object = MibScalar
ex2WSSyncFolderHierarchyRequests = _Ex2WSSyncFolderHierarchyRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 92),
    _Ex2WSSyncFolderHierarchyRequests_Type()
)
ex2WSSyncFolderHierarchyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSSyncFolderHierarchyRequests.setStatus("current")
_Ex2WSSynFoldHierarchyReqstPerSec_Type = Gauge32
_Ex2WSSynFoldHierarchyReqstPerSec_Object = MibScalar
ex2WSSynFoldHierarchyReqstPerSec = _Ex2WSSynFoldHierarchyReqstPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 93),
    _Ex2WSSynFoldHierarchyReqstPerSec_Type()
)
ex2WSSynFoldHierarchyReqstPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSSynFoldHierarchyReqstPerSec.setStatus("current")
_Ex2WSSyncFolderItemsRequests_Type = Gauge32
_Ex2WSSyncFolderItemsRequests_Object = MibScalar
ex2WSSyncFolderItemsRequests = _Ex2WSSyncFolderItemsRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 94),
    _Ex2WSSyncFolderItemsRequests_Type()
)
ex2WSSyncFolderItemsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSSyncFolderItemsRequests.setStatus("current")
_Ex2WSSyncFolderItemsReqstPerSec_Type = Gauge32
_Ex2WSSyncFolderItemsReqstPerSec_Object = MibScalar
ex2WSSyncFolderItemsReqstPerSec = _Ex2WSSyncFolderItemsReqstPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 95),
    _Ex2WSSyncFolderItemsReqstPerSec_Type()
)
ex2WSSyncFolderItemsReqstPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSSyncFolderItemsReqstPerSec.setStatus("current")
_Ex2WSTotalNumberOfIdsConverted_Type = Gauge32
_Ex2WSTotalNumberOfIdsConverted_Object = MibScalar
ex2WSTotalNumberOfIdsConverted = _Ex2WSTotalNumberOfIdsConverted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 96),
    _Ex2WSTotalNumberOfIdsConverted_Type()
)
ex2WSTotalNumberOfIdsConverted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSTotalNumberOfIdsConverted.setStatus("current")
_Ex2WSTotalRequests_Type = Gauge32
_Ex2WSTotalRequests_Object = MibScalar
ex2WSTotalRequests = _Ex2WSTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 97),
    _Ex2WSTotalRequests_Type()
)
ex2WSTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSTotalRequests.setStatus("current")
_Ex2WSTotalNumberOfBytesProxied_Type = Gauge32
_Ex2WSTotalNumberOfBytesProxied_Object = MibScalar
ex2WSTotalNumberOfBytesProxied = _Ex2WSTotalNumberOfBytesProxied_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 98),
    _Ex2WSTotalNumberOfBytesProxied_Type()
)
ex2WSTotalNumberOfBytesProxied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSTotalNumberOfBytesProxied.setStatus("current")
_Ex2WSTotalNumberOfProxiedRequest_Type = Gauge32
_Ex2WSTotalNumberOfProxiedRequest_Object = MibScalar
ex2WSTotalNumberOfProxiedRequest = _Ex2WSTotalNumberOfProxiedRequest_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 99),
    _Ex2WSTotalNumberOfProxiedRequest_Type()
)
ex2WSTotalNumberOfProxiedRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSTotalNumberOfProxiedRequest.setStatus("current")
_Ex2WSTotalNumberOfProxyFailover_Type = Gauge32
_Ex2WSTotalNumberOfProxyFailover_Object = MibScalar
ex2WSTotalNumberOfProxyFailover = _Ex2WSTotalNumberOfProxyFailover_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 100),
    _Ex2WSTotalNumberOfProxyFailover_Type()
)
ex2WSTotalNumberOfProxyFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSTotalNumberOfProxyFailover.setStatus("current")
_Ex2WSTotalNumberProxyResponsByte_Type = Gauge32
_Ex2WSTotalNumberProxyResponsByte_Object = MibScalar
ex2WSTotalNumberProxyResponsByte = _Ex2WSTotalNumberProxyResponsByte_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 101),
    _Ex2WSTotalNumberProxyResponsByte_Type()
)
ex2WSTotalNumberProxyResponsByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSTotalNumberProxyResponsByte.setStatus("current")
_Ex2WSUnsubscribeRequests_Type = Gauge32
_Ex2WSUnsubscribeRequests_Object = MibScalar
ex2WSUnsubscribeRequests = _Ex2WSUnsubscribeRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 102),
    _Ex2WSUnsubscribeRequests_Type()
)
ex2WSUnsubscribeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSUnsubscribeRequests.setStatus("current")
_Ex2WSUnsubscribeRequestsPerSec_Type = Gauge32
_Ex2WSUnsubscribeRequestsPerSec_Object = MibScalar
ex2WSUnsubscribeRequestsPerSec = _Ex2WSUnsubscribeRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 103),
    _Ex2WSUnsubscribeRequestsPerSec_Type()
)
ex2WSUnsubscribeRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSUnsubscribeRequestsPerSec.setStatus("current")
_Ex2WSUpdateDelegateRequests_Type = Gauge32
_Ex2WSUpdateDelegateRequests_Object = MibScalar
ex2WSUpdateDelegateRequests = _Ex2WSUpdateDelegateRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 104),
    _Ex2WSUpdateDelegateRequests_Type()
)
ex2WSUpdateDelegateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSUpdateDelegateRequests.setStatus("current")
_Ex2WSUpdateDelegateRequestPerSec_Type = Gauge32
_Ex2WSUpdateDelegateRequestPerSec_Object = MibScalar
ex2WSUpdateDelegateRequestPerSec = _Ex2WSUpdateDelegateRequestPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 105),
    _Ex2WSUpdateDelegateRequestPerSec_Type()
)
ex2WSUpdateDelegateRequestPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSUpdateDelegateRequestPerSec.setStatus("current")
_Ex2WSUpdateFolderRequests_Type = Gauge32
_Ex2WSUpdateFolderRequests_Object = MibScalar
ex2WSUpdateFolderRequests = _Ex2WSUpdateFolderRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 106),
    _Ex2WSUpdateFolderRequests_Type()
)
ex2WSUpdateFolderRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSUpdateFolderRequests.setStatus("current")
_Ex2WSUpdateFolderRequestsPerSec_Type = Gauge32
_Ex2WSUpdateFolderRequestsPerSec_Object = MibScalar
ex2WSUpdateFolderRequestsPerSec = _Ex2WSUpdateFolderRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 107),
    _Ex2WSUpdateFolderRequestsPerSec_Type()
)
ex2WSUpdateFolderRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSUpdateFolderRequestsPerSec.setStatus("current")
_Ex2WSUpdateItemRequests_Type = Gauge32
_Ex2WSUpdateItemRequests_Object = MibScalar
ex2WSUpdateItemRequests = _Ex2WSUpdateItemRequests_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 108),
    _Ex2WSUpdateItemRequests_Type()
)
ex2WSUpdateItemRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSUpdateItemRequests.setStatus("current")
_Ex2WSUpdateItemRequestsPerSec_Type = Gauge32
_Ex2WSUpdateItemRequestsPerSec_Object = MibScalar
ex2WSUpdateItemRequestsPerSec = _Ex2WSUpdateItemRequestsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 71, 109),
    _Ex2WSUpdateItemRequestsPerSec_Type()
)
ex2WSUpdateItemRequestsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2WSUpdateItemRequestsPerSec.setStatus("current")
_Ex2CatalogsTable_Object = MibTable
ex2CatalogsTable = _Ex2CatalogsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72)
)
if mibBuilder.loadTexts:
    ex2CatalogsTable.setStatus("current")
_Ex2CatalogsEntry_Object = MibTableRow
ex2CatalogsEntry = _Ex2CatalogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1)
)
ex2CatalogsEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2catInstance"),
)
if mibBuilder.loadTexts:
    ex2CatalogsEntry.setStatus("current")
_Ex2catInstance_Type = InstanceName
_Ex2catInstance_Object = MibTableColumn
ex2catInstance = _Ex2catInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 1),
    _Ex2catInstance_Type()
)
ex2catInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catInstance.setStatus("current")
_Ex2catBatchesFPC_Type = Gauge32
_Ex2catBatchesFPC_Object = MibTableColumn
ex2catBatchesFPC = _Ex2catBatchesFPC_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 2),
    _Ex2catBatchesFPC_Type()
)
ex2catBatchesFPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catBatchesFPC.setStatus("current")
_Ex2catBatchesAborted_Type = Gauge32
_Ex2catBatchesAborted_Object = MibTableColumn
ex2catBatchesAborted = _Ex2catBatchesAborted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 3),
    _Ex2catBatchesAborted_Type()
)
ex2catBatchesAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catBatchesAborted.setStatus("current")
_Ex2catBatchesCompletedSuccess_Type = Gauge32
_Ex2catBatchesCompletedSuccess_Object = MibTableColumn
ex2catBatchesCompletedSuccess = _Ex2catBatchesCompletedSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 4),
    _Ex2catBatchesCompletedSuccess_Type()
)
ex2catBatchesCompletedSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catBatchesCompletedSuccess.setStatus("current")
_Ex2catBatchesCompletedWPerErrors_Type = Gauge32
_Ex2catBatchesCompletedWPerErrors_Object = MibTableColumn
ex2catBatchesCompletedWPerErrors = _Ex2catBatchesCompletedWPerErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 5),
    _Ex2catBatchesCompletedWPerErrors_Type()
)
ex2catBatchesCompletedWPerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catBatchesCompletedWPerErrors.setStatus("current")
_Ex2catBatchesCompleteWPerWarning_Type = Gauge32
_Ex2catBatchesCompleteWPerWarning_Object = MibTableColumn
ex2catBatchesCompleteWPerWarning = _Ex2catBatchesCompleteWPerWarning_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 6),
    _Ex2catBatchesCompleteWPerWarning_Type()
)
ex2catBatchesCompleteWPerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catBatchesCompleteWPerWarning.setStatus("current")
_Ex2catBatchesDone_Type = Gauge32
_Ex2catBatchesDone_Object = MibTableColumn
ex2catBatchesDone = _Ex2catBatchesDone_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 7),
    _Ex2catBatchesDone_Type()
)
ex2catBatchesDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catBatchesDone.setStatus("current")
_Ex2catBatchesInProgress_Type = Gauge32
_Ex2catBatchesInProgress_Object = MibTableColumn
ex2catBatchesInProgress = _Ex2catBatchesInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 8),
    _Ex2catBatchesInProgress_Type()
)
ex2catBatchesInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catBatchesInProgress.setStatus("current")
_Ex2catBatchesReceived_Type = Gauge32
_Ex2catBatchesReceived_Object = MibTableColumn
ex2catBatchesReceived = _Ex2catBatchesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 9),
    _Ex2catBatchesReceived_Type()
)
ex2catBatchesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catBatchesReceived.setStatus("current")
_Ex2catPhaseComplete_Type = Gauge32
_Ex2catPhaseComplete_Object = MibTableColumn
ex2catPhaseComplete = _Ex2catPhaseComplete_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 10),
    _Ex2catPhaseComplete_Type()
)
ex2catPhaseComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catPhaseComplete.setStatus("current")
_Ex2catPhaseInHDFD_Type = Gauge32
_Ex2catPhaseInHDFD_Object = MibTableColumn
ex2catPhaseInHDFD = _Ex2catPhaseInHDFD_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 11),
    _Ex2catPhaseInHDFD_Type()
)
ex2catPhaseInHDFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catPhaseInHDFD.setStatus("current")
_Ex2catPhaseInMTFD_Type = Gauge32
_Ex2catPhaseInMTFD_Object = MibTableColumn
ex2catPhaseInMTFD = _Ex2catPhaseInMTFD_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 12),
    _Ex2catPhaseInMTFD_Type()
)
ex2catPhaseInMTFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catPhaseInMTFD.setStatus("current")
_Ex2catPhaseInSTFD_Type = Gauge32
_Ex2catPhaseInSTFD_Object = MibTableColumn
ex2catPhaseInSTFD = _Ex2catPhaseInSTFD_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 13),
    _Ex2catPhaseInSTFD_Type()
)
ex2catPhaseInSTFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catPhaseInSTFD.setStatus("current")
_Ex2catPhaseInPipeline_Type = Gauge32
_Ex2catPhaseInPipeline_Object = MibTableColumn
ex2catPhaseInPipeline = _Ex2catPhaseInPipeline_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 14),
    _Ex2catPhaseInPipeline_Type()
)
ex2catPhaseInPipeline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catPhaseInPipeline.setStatus("current")
_Ex2catPhaseInReadyQueue_Type = Gauge32
_Ex2catPhaseInReadyQueue_Object = MibTableColumn
ex2catPhaseInReadyQueue = _Ex2catPhaseInReadyQueue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 15),
    _Ex2catPhaseInReadyQueue_Type()
)
ex2catPhaseInReadyQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catPhaseInReadyQueue.setStatus("current")
_Ex2catPhaseOnHold_Type = Gauge32
_Ex2catPhaseOnHold_Object = MibTableColumn
ex2catPhaseOnHold = _Ex2catPhaseOnHold_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 16),
    _Ex2catPhaseOnHold_Type()
)
ex2catPhaseOnHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catPhaseOnHold.setStatus("current")
_Ex2catPhasePendingCompletion_Type = Gauge32
_Ex2catPhasePendingCompletion_Object = MibTableColumn
ex2catPhasePendingCompletion = _Ex2catPhasePendingCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 17),
    _Ex2catPhasePendingCompletion_Type()
)
ex2catPhasePendingCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catPhasePendingCompletion.setStatus("current")
_Ex2catPhaseRedundant_Type = Gauge32
_Ex2catPhaseRedundant_Object = MibTableColumn
ex2catPhaseRedundant = _Ex2catPhaseRedundant_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 18),
    _Ex2catPhaseRedundant_Type()
)
ex2catPhaseRedundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catPhaseRedundant.setStatus("current")
_Ex2catRequestAbort_Type = Gauge32
_Ex2catRequestAbort_Object = MibTableColumn
ex2catRequestAbort = _Ex2catRequestAbort_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 19),
    _Ex2catRequestAbort_Type()
)
ex2catRequestAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catRequestAbort.setStatus("current")
_Ex2catRequestAsyncFlush_Type = Gauge32
_Ex2catRequestAsyncFlush_Object = MibTableColumn
ex2catRequestAsyncFlush = _Ex2catRequestAsyncFlush_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 20),
    _Ex2catRequestAsyncFlush_Type()
)
ex2catRequestAsyncFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catRequestAsyncFlush.setStatus("current")
_Ex2catRequestFlushPerDrain_Type = Gauge32
_Ex2catRequestFlushPerDrain_Object = MibTableColumn
ex2catRequestFlushPerDrain = _Ex2catRequestFlushPerDrain_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 21),
    _Ex2catRequestFlushPerDrain_Type()
)
ex2catRequestFlushPerDrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catRequestFlushPerDrain.setStatus("current")
_Ex2catRequestForceMerge_Type = Gauge32
_Ex2catRequestForceMerge_Object = MibTableColumn
ex2catRequestForceMerge = _Ex2catRequestForceMerge_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 22),
    _Ex2catRequestForceMerge_Type()
)
ex2catRequestForceMerge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catRequestForceMerge.setStatus("current")
_Ex2catRequestPause_Type = Gauge32
_Ex2catRequestPause_Object = MibTableColumn
ex2catRequestPause = _Ex2catRequestPause_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 23),
    _Ex2catRequestPause_Type()
)
ex2catRequestPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catRequestPause.setStatus("current")
_Ex2catRequestReset_Type = Gauge32
_Ex2catRequestReset_Object = MibTableColumn
ex2catRequestReset = _Ex2catRequestReset_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 24),
    _Ex2catRequestReset_Type()
)
ex2catRequestReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catRequestReset.setStatus("current")
_Ex2catRequestResume_Type = Gauge32
_Ex2catRequestResume_Object = MibTableColumn
ex2catRequestResume = _Ex2catRequestResume_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 25),
    _Ex2catRequestResume_Type()
)
ex2catRequestResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catRequestResume.setStatus("current")
_Ex2catState_Type = Gauge32
_Ex2catState_Object = MibTableColumn
ex2catState = _Ex2catState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 26),
    _Ex2catState_Type()
)
ex2catState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catState.setStatus("current")
_Ex2catStateCallerComponent_Type = Gauge32
_Ex2catStateCallerComponent_Object = MibTableColumn
ex2catStateCallerComponent = _Ex2catStateCallerComponent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 27),
    _Ex2catStateCallerComponent_Type()
)
ex2catStateCallerComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catStateCallerComponent.setStatus("current")
_Ex2catStateReasonCode_Type = Gauge32
_Ex2catStateReasonCode_Object = MibTableColumn
ex2catStateReasonCode = _Ex2catStateReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 28),
    _Ex2catStateReasonCode_Type()
)
ex2catStateReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catStateReasonCode.setStatus("current")
_Ex2catStateResultCode_Type = Gauge32
_Ex2catStateResultCode_Object = MibTableColumn
ex2catStateResultCode = _Ex2catStateResultCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 29),
    _Ex2catStateResultCode_Type()
)
ex2catStateResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catStateResultCode.setStatus("current")
_Ex2catTransDeletes_Type = Gauge32
_Ex2catTransDeletes_Object = MibTableColumn
ex2catTransDeletes = _Ex2catTransDeletes_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 30),
    _Ex2catTransDeletes_Type()
)
ex2catTransDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catTransDeletes.setStatus("current")
_Ex2catTransDone_Type = Gauge32
_Ex2catTransDone_Object = MibTableColumn
ex2catTransDone = _Ex2catTransDone_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 31),
    _Ex2catTransDone_Type()
)
ex2catTransDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catTransDone.setStatus("current")
_Ex2catTransErrored_Type = Gauge32
_Ex2catTransErrored_Object = MibTableColumn
ex2catTransErrored = _Ex2catTransErrored_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 32),
    _Ex2catTransErrored_Type()
)
ex2catTransErrored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catTransErrored.setStatus("current")
_Ex2catTransInProgress_Type = Gauge32
_Ex2catTransInProgress_Object = MibTableColumn
ex2catTransInProgress = _Ex2catTransInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 33),
    _Ex2catTransInProgress_Type()
)
ex2catTransInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catTransInProgress.setStatus("current")
_Ex2catTransModifies_Type = Gauge32
_Ex2catTransModifies_Object = MibTableColumn
ex2catTransModifies = _Ex2catTransModifies_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 34),
    _Ex2catTransModifies_Type()
)
ex2catTransModifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catTransModifies.setStatus("current")
_Ex2catTransRerouted_Type = Gauge32
_Ex2catTransRerouted_Object = MibTableColumn
ex2catTransRerouted = _Ex2catTransRerouted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 72, 1, 35),
    _Ex2catTransRerouted_Type()
)
ex2catTransRerouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2catTransRerouted.setStatus("current")
_Ex2FDTable_Object = MibTable
ex2FDTable = _Ex2FDTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73)
)
if mibBuilder.loadTexts:
    ex2FDTable.setStatus("current")
_Ex2FDEntry_Object = MibTableRow
ex2FDEntry = _Ex2FDEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1)
)
ex2FDEntry.setIndexNames(
    (0, "INFORMANT-EXCHANGE-V2", "ex2FDInstance"),
)
if mibBuilder.loadTexts:
    ex2FDEntry.setStatus("current")
_Ex2FDInstance_Type = InstanceName
_Ex2FDInstance_Object = MibTableColumn
ex2FDInstance = _Ex2FDInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 1),
    _Ex2FDInstance_Type()
)
ex2FDInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDInstance.setStatus("current")
_Ex2FDBatchesCompleted_Type = Gauge32
_Ex2FDBatchesCompleted_Object = MibTableColumn
ex2FDBatchesCompleted = _Ex2FDBatchesCompleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 2),
    _Ex2FDBatchesCompleted_Type()
)
ex2FDBatchesCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDBatchesCompleted.setStatus("current")
_Ex2FDBatchesInProgress_Type = Gauge32
_Ex2FDBatchesInProgress_Object = MibTableColumn
ex2FDBatchesInProgress = _Ex2FDBatchesInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 3),
    _Ex2FDBatchesInProgress_Type()
)
ex2FDBatchesInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDBatchesInProgress.setStatus("current")
_Ex2FDBatchesReceived_Type = Gauge32
_Ex2FDBatchesReceived_Object = MibTableColumn
ex2FDBatchesReceived = _Ex2FDBatchesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 4),
    _Ex2FDBatchesReceived_Type()
)
ex2FDBatchesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDBatchesReceived.setStatus("current")
_Ex2FDBatchesRejected_Type = Gauge32
_Ex2FDBatchesRejected_Object = MibTableColumn
ex2FDBatchesRejected = _Ex2FDBatchesRejected_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 5),
    _Ex2FDBatchesRejected_Type()
)
ex2FDBatchesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDBatchesRejected.setStatus("current")
_Ex2FDFilters_Type = Gauge32
_Ex2FDFilters_Object = MibTableColumn
ex2FDFilters = _Ex2FDFilters_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 6),
    _Ex2FDFilters_Type()
)
ex2FDFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDFilters.setStatus("current")
_Ex2FDNoiseWordLists_Type = Gauge32
_Ex2FDNoiseWordLists_Object = MibTableColumn
ex2FDNoiseWordLists = _Ex2FDNoiseWordLists_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 7),
    _Ex2FDNoiseWordLists_Type()
)
ex2FDNoiseWordLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDNoiseWordLists.setStatus("current")
_Ex2FDTransErrors_Type = Gauge32
_Ex2FDTransErrors_Object = MibTableColumn
ex2FDTransErrors = _Ex2FDTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 8),
    _Ex2FDTransErrors_Type()
)
ex2FDTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDTransErrors.setStatus("current")
_Ex2FDTransSuccess_Type = Gauge32
_Ex2FDTransSuccess_Object = MibTableColumn
ex2FDTransSuccess = _Ex2FDTransSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 9),
    _Ex2FDTransSuccess_Type()
)
ex2FDTransSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDTransSuccess.setStatus("current")
_Ex2FDTransactionsCompleted_Type = Gauge32
_Ex2FDTransactionsCompleted_Object = MibTableColumn
ex2FDTransactionsCompleted = _Ex2FDTransactionsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 10),
    _Ex2FDTransactionsCompleted_Type()
)
ex2FDTransactionsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDTransactionsCompleted.setStatus("current")
_Ex2FDTransactionsReceived_Type = Gauge32
_Ex2FDTransactionsReceived_Object = MibTableColumn
ex2FDTransactionsReceived = _Ex2FDTransactionsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 11),
    _Ex2FDTransactionsReceived_Type()
)
ex2FDTransactionsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDTransactionsReceived.setStatus("current")
_Ex2FDTransactionsStarted_Type = Gauge32
_Ex2FDTransactionsStarted_Object = MibTableColumn
ex2FDTransactionsStarted = _Ex2FDTransactionsStarted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 12),
    _Ex2FDTransactionsStarted_Type()
)
ex2FDTransactionsStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDTransactionsStarted.setStatus("current")
_Ex2FDWordBreakers_Type = Gauge32
_Ex2FDWordBreakers_Object = MibTableColumn
ex2FDWordBreakers = _Ex2FDWordBreakers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 73, 1, 13),
    _Ex2FDWordBreakers_Type()
)
ex2FDWordBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2FDWordBreakers.setStatus("current")
_Ex2Service_ObjectIdentity = ObjectIdentity
ex2Service = _Ex2Service_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74)
)
_Ex2svcBatchesFPC_Type = Gauge32
_Ex2svcBatchesFPC_Object = MibScalar
ex2svcBatchesFPC = _Ex2svcBatchesFPC_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 1),
    _Ex2svcBatchesFPC_Type()
)
ex2svcBatchesFPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcBatchesFPC.setStatus("current")
_Ex2svcBatchesAborted_Type = Gauge32
_Ex2svcBatchesAborted_Object = MibScalar
ex2svcBatchesAborted = _Ex2svcBatchesAborted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 2),
    _Ex2svcBatchesAborted_Type()
)
ex2svcBatchesAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcBatchesAborted.setStatus("current")
_Ex2svcBatchesCompletedWPerErrors_Type = Gauge32
_Ex2svcBatchesCompletedWPerErrors_Object = MibScalar
ex2svcBatchesCompletedWPerErrors = _Ex2svcBatchesCompletedWPerErrors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 3),
    _Ex2svcBatchesCompletedWPerErrors_Type()
)
ex2svcBatchesCompletedWPerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcBatchesCompletedWPerErrors.setStatus("current")
_Ex2svcBatchesCompleteWPerWarning_Type = Gauge32
_Ex2svcBatchesCompleteWPerWarning_Object = MibScalar
ex2svcBatchesCompleteWPerWarning = _Ex2svcBatchesCompleteWPerWarning_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 4),
    _Ex2svcBatchesCompleteWPerWarning_Type()
)
ex2svcBatchesCompleteWPerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcBatchesCompleteWPerWarning.setStatus("current")
_Ex2svcBatcheCompletelySuccessful_Type = Gauge32
_Ex2svcBatcheCompletelySuccessful_Object = MibScalar
ex2svcBatcheCompletelySuccessful = _Ex2svcBatcheCompletelySuccessful_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 5),
    _Ex2svcBatcheCompletelySuccessful_Type()
)
ex2svcBatcheCompletelySuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcBatcheCompletelySuccessful.setStatus("current")
_Ex2svcBatchesDone_Type = Gauge32
_Ex2svcBatchesDone_Object = MibScalar
ex2svcBatchesDone = _Ex2svcBatchesDone_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 6),
    _Ex2svcBatchesDone_Type()
)
ex2svcBatchesDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcBatchesDone.setStatus("current")
_Ex2svcBatchesInProgress_Type = Gauge32
_Ex2svcBatchesInProgress_Object = MibScalar
ex2svcBatchesInProgress = _Ex2svcBatchesInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 7),
    _Ex2svcBatchesInProgress_Type()
)
ex2svcBatchesInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcBatchesInProgress.setStatus("current")
_Ex2svcBatchesInReadyQueue_Type = Gauge32
_Ex2svcBatchesInReadyQueue_Object = MibScalar
ex2svcBatchesInReadyQueue = _Ex2svcBatchesInReadyQueue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 8),
    _Ex2svcBatchesInReadyQueue_Type()
)
ex2svcBatchesInReadyQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcBatchesInReadyQueue.setStatus("current")
_Ex2svcBatchesReceived_Type = Gauge32
_Ex2svcBatchesReceived_Object = MibScalar
ex2svcBatchesReceived = _Ex2svcBatchesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 9),
    _Ex2svcBatchesReceived_Type()
)
ex2svcBatchesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcBatchesReceived.setStatus("current")
_Ex2svcCBSize_Type = Gauge32
_Ex2svcCBSize_Object = MibScalar
ex2svcCBSize = _Ex2svcCBSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 10),
    _Ex2svcCBSize_Type()
)
ex2svcCBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcCBSize.setStatus("current")
_Ex2svcCBsAcquired_Type = Gauge32
_Ex2svcCBsAcquired_Object = MibScalar
ex2svcCBsAcquired = _Ex2svcCBsAcquired_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 11),
    _Ex2svcCBsAcquired_Type()
)
ex2svcCBsAcquired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcCBsAcquired.setStatus("current")
_Ex2svcCBsDestroyed_Type = Gauge32
_Ex2svcCBsDestroyed_Object = MibScalar
ex2svcCBsDestroyed = _Ex2svcCBsDestroyed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 12),
    _Ex2svcCBsDestroyed_Type()
)
ex2svcCBsDestroyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcCBsDestroyed.setStatus("current")
_Ex2svcCBsGarbageCollected_Type = Gauge32
_Ex2svcCBsGarbageCollected_Object = MibScalar
ex2svcCBsGarbageCollected = _Ex2svcCBsGarbageCollected_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 13),
    _Ex2svcCBsGarbageCollected_Type()
)
ex2svcCBsGarbageCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcCBsGarbageCollected.setStatus("current")
_Ex2svcCBsGiven_Type = Gauge32
_Ex2svcCBsGiven_Object = MibScalar
ex2svcCBsGiven = _Ex2svcCBsGiven_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 14),
    _Ex2svcCBsGiven_Type()
)
ex2svcCBsGiven.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcCBsGiven.setStatus("current")
_Ex2svcCBsInUse_Type = Gauge32
_Ex2svcCBsInUse_Object = MibScalar
ex2svcCBsInUse = _Ex2svcCBsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 15),
    _Ex2svcCBsInUse_Type()
)
ex2svcCBsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcCBsInUse.setStatus("current")
_Ex2svcCBsReleased_Type = Gauge32
_Ex2svcCBsReleased_Object = MibScalar
ex2svcCBsReleased = _Ex2svcCBsReleased_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 16),
    _Ex2svcCBsReleased_Type()
)
ex2svcCBsReleased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcCBsReleased.setStatus("current")
_Ex2svcCBsTotal_Type = Gauge32
_Ex2svcCBsTotal_Object = MibScalar
ex2svcCBsTotal = _Ex2svcCBsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 17),
    _Ex2svcCBsTotal_Type()
)
ex2svcCBsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcCBsTotal.setStatus("current")
_Ex2svcCatalogsMonitored_Type = Gauge32
_Ex2svcCatalogsMonitored_Object = MibScalar
ex2svcCatalogsMonitored = _Ex2svcCatalogsMonitored_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 18),
    _Ex2svcCatalogsMonitored_Type()
)
ex2svcCatalogsMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcCatalogsMonitored.setStatus("current")
_Ex2svcCatalogsMounted_Type = Gauge32
_Ex2svcCatalogsMounted_Object = MibScalar
ex2svcCatalogsMounted = _Ex2svcCatalogsMounted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 19),
    _Ex2svcCatalogsMounted_Type()
)
ex2svcCatalogsMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcCatalogsMounted.setStatus("current")
_Ex2svcFDHDCBEmpty_Type = Gauge32
_Ex2svcFDHDCBEmpty_Object = MibScalar
ex2svcFDHDCBEmpty = _Ex2svcFDHDCBEmpty_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 20),
    _Ex2svcFDHDCBEmpty_Type()
)
ex2svcFDHDCBEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDHDCBEmpty.setStatus("current")
_Ex2svcFDHDActive_Type = Gauge32
_Ex2svcFDHDActive_Object = MibScalar
ex2svcFDHDActive = _Ex2svcFDHDActive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 21),
    _Ex2svcFDHDActive_Type()
)
ex2svcFDHDActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDHDActive.setStatus("current")
_Ex2svcFDHDLaunched_Type = Gauge32
_Ex2svcFDHDLaunched_Object = MibScalar
ex2svcFDHDLaunched = _Ex2svcFDHDLaunched_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 22),
    _Ex2svcFDHDLaunched_Type()
)
ex2svcFDHDLaunched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDHDLaunched.setStatus("current")
_Ex2svcFDHDTerminatedAV_Type = Gauge32
_Ex2svcFDHDTerminatedAV_Object = MibScalar
ex2svcFDHDTerminatedAV = _Ex2svcFDHDTerminatedAV_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 23),
    _Ex2svcFDHDTerminatedAV_Type()
)
ex2svcFDHDTerminatedAV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDHDTerminatedAV.setStatus("current")
_Ex2svcFDHDTerminatedExcessiveMem_Type = Gauge32
_Ex2svcFDHDTerminatedExcessiveMem_Object = MibScalar
ex2svcFDHDTerminatedExcessiveMem = _Ex2svcFDHDTerminatedExcessiveMem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 24),
    _Ex2svcFDHDTerminatedExcessiveMem_Type()
)
ex2svcFDHDTerminatedExcessiveMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDHDTerminatedExcessiveMem.setStatus("current")
_Ex2svcFDHDTerminatedIdle_Type = Gauge32
_Ex2svcFDHDTerminatedIdle_Object = MibScalar
ex2svcFDHDTerminatedIdle = _Ex2svcFDHDTerminatedIdle_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 25),
    _Ex2svcFDHDTerminatedIdle_Type()
)
ex2svcFDHDTerminatedIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDHDTerminatedIdle.setStatus("current")
_Ex2svcFDHDTerminatedOther_Type = Gauge32
_Ex2svcFDHDTerminatedOther_Object = MibScalar
ex2svcFDHDTerminatedOther = _Ex2svcFDHDTerminatedOther_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 26),
    _Ex2svcFDHDTerminatedOther_Type()
)
ex2svcFDHDTerminatedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDHDTerminatedOther.setStatus("current")
_Ex2svcFDHDTerminatedPipe_Type = Gauge32
_Ex2svcFDHDTerminatedPipe_Object = MibScalar
ex2svcFDHDTerminatedPipe = _Ex2svcFDHDTerminatedPipe_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 27),
    _Ex2svcFDHDTerminatedPipe_Type()
)
ex2svcFDHDTerminatedPipe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDHDTerminatedPipe.setStatus("current")
_Ex2svcFDHDTerminatedTimeOut_Type = Gauge32
_Ex2svcFDHDTerminatedTimeOut_Object = MibScalar
ex2svcFDHDTerminatedTimeOut = _Ex2svcFDHDTerminatedTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 28),
    _Ex2svcFDHDTerminatedTimeOut_Type()
)
ex2svcFDHDTerminatedTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDHDTerminatedTimeOut.setStatus("current")
_Ex2svcFDHDUnresponsiveToShutdown_Type = Gauge32
_Ex2svcFDHDUnresponsiveToShutdown_Object = MibScalar
ex2svcFDHDUnresponsiveToShutdown = _Ex2svcFDHDUnresponsiveToShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 29),
    _Ex2svcFDHDUnresponsiveToShutdown_Type()
)
ex2svcFDHDUnresponsiveToShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDHDUnresponsiveToShutdown.setStatus("current")
_Ex2svcFDMTCBEmpty_Type = Gauge32
_Ex2svcFDMTCBEmpty_Object = MibScalar
ex2svcFDMTCBEmpty = _Ex2svcFDMTCBEmpty_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 30),
    _Ex2svcFDMTCBEmpty_Type()
)
ex2svcFDMTCBEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDMTCBEmpty.setStatus("current")
_Ex2svcFDMTActive_Type = Gauge32
_Ex2svcFDMTActive_Object = MibScalar
ex2svcFDMTActive = _Ex2svcFDMTActive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 31),
    _Ex2svcFDMTActive_Type()
)
ex2svcFDMTActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDMTActive.setStatus("current")
_Ex2svcFDMTLaunched_Type = Gauge32
_Ex2svcFDMTLaunched_Object = MibScalar
ex2svcFDMTLaunched = _Ex2svcFDMTLaunched_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 32),
    _Ex2svcFDMTLaunched_Type()
)
ex2svcFDMTLaunched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDMTLaunched.setStatus("current")
_Ex2svcFDMTTerminatedAV_Type = Gauge32
_Ex2svcFDMTTerminatedAV_Object = MibScalar
ex2svcFDMTTerminatedAV = _Ex2svcFDMTTerminatedAV_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 33),
    _Ex2svcFDMTTerminatedAV_Type()
)
ex2svcFDMTTerminatedAV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDMTTerminatedAV.setStatus("current")
_Ex2svcFDMTTerminatedExcessiveMem_Type = Gauge32
_Ex2svcFDMTTerminatedExcessiveMem_Object = MibScalar
ex2svcFDMTTerminatedExcessiveMem = _Ex2svcFDMTTerminatedExcessiveMem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 34),
    _Ex2svcFDMTTerminatedExcessiveMem_Type()
)
ex2svcFDMTTerminatedExcessiveMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDMTTerminatedExcessiveMem.setStatus("current")
_Ex2svcFDMTTerminatedIdle_Type = Gauge32
_Ex2svcFDMTTerminatedIdle_Object = MibScalar
ex2svcFDMTTerminatedIdle = _Ex2svcFDMTTerminatedIdle_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 35),
    _Ex2svcFDMTTerminatedIdle_Type()
)
ex2svcFDMTTerminatedIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDMTTerminatedIdle.setStatus("current")
_Ex2svcFDMTTerminatedOther_Type = Gauge32
_Ex2svcFDMTTerminatedOther_Object = MibScalar
ex2svcFDMTTerminatedOther = _Ex2svcFDMTTerminatedOther_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 36),
    _Ex2svcFDMTTerminatedOther_Type()
)
ex2svcFDMTTerminatedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDMTTerminatedOther.setStatus("current")
_Ex2svcFDMTTerminatedPipe_Type = Gauge32
_Ex2svcFDMTTerminatedPipe_Object = MibScalar
ex2svcFDMTTerminatedPipe = _Ex2svcFDMTTerminatedPipe_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 37),
    _Ex2svcFDMTTerminatedPipe_Type()
)
ex2svcFDMTTerminatedPipe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDMTTerminatedPipe.setStatus("current")
_Ex2svcFDMTTerminatedTimeOut_Type = Gauge32
_Ex2svcFDMTTerminatedTimeOut_Object = MibScalar
ex2svcFDMTTerminatedTimeOut = _Ex2svcFDMTTerminatedTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 38),
    _Ex2svcFDMTTerminatedTimeOut_Type()
)
ex2svcFDMTTerminatedTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDMTTerminatedTimeOut.setStatus("current")
_Ex2svcFDMTUnresponsiveToShutdown_Type = Gauge32
_Ex2svcFDMTUnresponsiveToShutdown_Object = MibScalar
ex2svcFDMTUnresponsiveToShutdown = _Ex2svcFDMTUnresponsiveToShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 39),
    _Ex2svcFDMTUnresponsiveToShutdown_Type()
)
ex2svcFDMTUnresponsiveToShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDMTUnresponsiveToShutdown.setStatus("current")
_Ex2svcFDSTCBEmpty_Type = Gauge32
_Ex2svcFDSTCBEmpty_Object = MibScalar
ex2svcFDSTCBEmpty = _Ex2svcFDSTCBEmpty_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 40),
    _Ex2svcFDSTCBEmpty_Type()
)
ex2svcFDSTCBEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDSTCBEmpty.setStatus("current")
_Ex2svcFDSTActive_Type = Gauge32
_Ex2svcFDSTActive_Object = MibScalar
ex2svcFDSTActive = _Ex2svcFDSTActive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 41),
    _Ex2svcFDSTActive_Type()
)
ex2svcFDSTActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDSTActive.setStatus("current")
_Ex2svcFDSTLaunched_Type = Gauge32
_Ex2svcFDSTLaunched_Object = MibScalar
ex2svcFDSTLaunched = _Ex2svcFDSTLaunched_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 42),
    _Ex2svcFDSTLaunched_Type()
)
ex2svcFDSTLaunched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDSTLaunched.setStatus("current")
_Ex2svcFDSTTerminatedAV_Type = Gauge32
_Ex2svcFDSTTerminatedAV_Object = MibScalar
ex2svcFDSTTerminatedAV = _Ex2svcFDSTTerminatedAV_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 43),
    _Ex2svcFDSTTerminatedAV_Type()
)
ex2svcFDSTTerminatedAV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDSTTerminatedAV.setStatus("current")
_Ex2svcFDSTTerminatedExcessiveMem_Type = Gauge32
_Ex2svcFDSTTerminatedExcessiveMem_Object = MibScalar
ex2svcFDSTTerminatedExcessiveMem = _Ex2svcFDSTTerminatedExcessiveMem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 44),
    _Ex2svcFDSTTerminatedExcessiveMem_Type()
)
ex2svcFDSTTerminatedExcessiveMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDSTTerminatedExcessiveMem.setStatus("current")
_Ex2svcFDSTTerminatedIdle_Type = Gauge32
_Ex2svcFDSTTerminatedIdle_Object = MibScalar
ex2svcFDSTTerminatedIdle = _Ex2svcFDSTTerminatedIdle_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 45),
    _Ex2svcFDSTTerminatedIdle_Type()
)
ex2svcFDSTTerminatedIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDSTTerminatedIdle.setStatus("current")
_Ex2svcFDSTTerminatedOther_Type = Gauge32
_Ex2svcFDSTTerminatedOther_Object = MibScalar
ex2svcFDSTTerminatedOther = _Ex2svcFDSTTerminatedOther_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 46),
    _Ex2svcFDSTTerminatedOther_Type()
)
ex2svcFDSTTerminatedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDSTTerminatedOther.setStatus("current")
_Ex2svcFDSTTerminatedPipe_Type = Gauge32
_Ex2svcFDSTTerminatedPipe_Object = MibScalar
ex2svcFDSTTerminatedPipe = _Ex2svcFDSTTerminatedPipe_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 47),
    _Ex2svcFDSTTerminatedPipe_Type()
)
ex2svcFDSTTerminatedPipe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDSTTerminatedPipe.setStatus("current")
_Ex2svcFDSTTerminatedTimeOut_Type = Gauge32
_Ex2svcFDSTTerminatedTimeOut_Object = MibScalar
ex2svcFDSTTerminatedTimeOut = _Ex2svcFDSTTerminatedTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 48),
    _Ex2svcFDSTTerminatedTimeOut_Type()
)
ex2svcFDSTTerminatedTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDSTTerminatedTimeOut.setStatus("current")
_Ex2svcFDSTUnresponsiveToShutdown_Type = Gauge32
_Ex2svcFDSTUnresponsiveToShutdown_Object = MibScalar
ex2svcFDSTUnresponsiveToShutdown = _Ex2svcFDSTUnresponsiveToShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 49),
    _Ex2svcFDSTUnresponsiveToShutdown_Type()
)
ex2svcFDSTUnresponsiveToShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcFDSTUnresponsiveToShutdown.setStatus("current")
_Ex2svcHeartbeats_Type = Gauge32
_Ex2svcHeartbeats_Object = MibScalar
ex2svcHeartbeats = _Ex2svcHeartbeats_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 50),
    _Ex2svcHeartbeats_Type()
)
ex2svcHeartbeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcHeartbeats.setStatus("current")
_Ex2svcIndexPerfLevel_Type = Gauge32
_Ex2svcIndexPerfLevel_Object = MibScalar
ex2svcIndexPerfLevel = _Ex2svcIndexPerfLevel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 51),
    _Ex2svcIndexPerfLevel_Type()
)
ex2svcIndexPerfLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcIndexPerfLevel.setStatus("current")
_Ex2svcQueryPerfLevel_Type = Gauge32
_Ex2svcQueryPerfLevel_Object = MibScalar
ex2svcQueryPerfLevel = _Ex2svcQueryPerfLevel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 52),
    _Ex2svcQueryPerfLevel_Type()
)
ex2svcQueryPerfLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcQueryPerfLevel.setStatus("current")
_Ex2svcTotalNoiseWordFiles_Type = Gauge32
_Ex2svcTotalNoiseWordFiles_Object = MibScalar
ex2svcTotalNoiseWordFiles = _Ex2svcTotalNoiseWordFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 53),
    _Ex2svcTotalNoiseWordFiles_Type()
)
ex2svcTotalNoiseWordFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcTotalNoiseWordFiles.setStatus("current")
_Ex2svcTotalStemmers_Type = Gauge32
_Ex2svcTotalStemmers_Object = MibScalar
ex2svcTotalStemmers = _Ex2svcTotalStemmers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 54),
    _Ex2svcTotalStemmers_Type()
)
ex2svcTotalStemmers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcTotalStemmers.setStatus("current")
_Ex2svcTotalThesaurus_Type = Gauge32
_Ex2svcTotalThesaurus_Object = MibScalar
ex2svcTotalThesaurus = _Ex2svcTotalThesaurus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 55),
    _Ex2svcTotalThesaurus_Type()
)
ex2svcTotalThesaurus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcTotalThesaurus.setStatus("current")
_Ex2svcTotalWordbreakers_Type = Gauge32
_Ex2svcTotalWordbreakers_Object = MibScalar
ex2svcTotalWordbreakers = _Ex2svcTotalWordbreakers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 15, 74, 56),
    _Ex2svcTotalWordbreakers_Type()
)
ex2svcTotalWordbreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ex2svcTotalWordbreakers.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-EXCHANGE-V2",
    **{"exchangeV2": exchangeV2,
       "ex2ADRMSPrelicensingAgent": ex2ADRMSPrelicensingAgent,
       "ex2apaAvgProcessTimeLicenseRqst": ex2apaAvgProcessTimeLicenseRqst,
       "ex2apaMessageProcessSuccessfully": ex2apaMessageProcessSuccessfully,
       "ex2apaPermanentFailLicenseRqsts": ex2apaPermanentFailLicenseRqsts,
       "ex2apaSuccessfulLicenseRequests": ex2apaSuccessfulLicenseRequests,
       "ex2apaTotalLicenseRequests": ex2apaTotalLicenseRequests,
       "ex2apaTotalLicenseRqstsProcTime": ex2apaTotalLicenseRqstsProcTime,
       "ex2apaTotalLicenseRequestsPerSec": ex2apaTotalLicenseRequestsPerSec,
       "ex2apaTotalMessages": ex2apaTotalMessages,
       "ex2apaTotalRecipients": ex2apaTotalRecipients,
       "ex2ADAccessCachesTable": ex2ADAccessCachesTable,
       "ex2ADAccessCachesEntry": ex2ADAccessCachesEntry,
       "ex2aacInstance": ex2aacInstance,
       "ex2aacCacheExpireTotalConfigData": ex2aacCacheExpireTotalConfigData,
       "ex2aacCacheExpiriesTotalUserData": ex2aacCacheExpiriesTotalUserData,
       "ex2aacCacheExpiriesSecConfigData": ex2aacCacheExpiriesSecConfigData,
       "ex2aacCacheExpirePerSecUserData": ex2aacCacheExpirePerSecUserData,
       "ex2aacCacheHitsTotal": ex2aacCacheHitsTotal,
       "ex2aacCacheHitsPerSec": ex2aacCacheHitsPerSec,
       "ex2aacCacheInsertTotalConfigData": ex2aacCacheInsertTotalConfigData,
       "ex2aacCacheInsertsTotalUserData": ex2aacCacheInsertsTotalUserData,
       "ex2aacCacheInsertSecConfigurData": ex2aacCacheInsertSecConfigurData,
       "ex2aacCacheInsertsPerSecUserData": ex2aacCacheInsertsPerSecUserData,
       "ex2aacCacheMissesTotal": ex2aacCacheMissesTotal,
       "ex2aacCacheMissesPerSec": ex2aacCacheMissesPerSec,
       "ex2aacDNEntriesConfigurationData": ex2aacDNEntriesConfigurationData,
       "ex2aacDNEntriesUserData": ex2aacDNEntriesUserData,
       "ex2aacDNEntriesMemoryConfigData": ex2aacDNEntriesMemoryConfigData,
       "ex2aacDNEntriesMemoryUserData": ex2aacDNEntriesMemoryUserData,
       "ex2aacLDAPSearchesTotal": ex2aacLDAPSearchesTotal,
       "ex2aacLDAPSearchesPerSec": ex2aacLDAPSearchesPerSec,
       "ex2aacNotFndDNEntriesConfigData": ex2aacNotFndDNEntriesConfigData,
       "ex2aacNotFoundDNEntriesUserData": ex2aacNotFoundDNEntriesUserData,
       "ex2aacNotFndDNEntryMemConfigData": ex2aacNotFndDNEntryMemConfigData,
       "ex2aacNotFndDNEntriesMemUserData": ex2aacNotFndDNEntriesMemUserData,
       "ex2aacNotFndGUIDEntryConfigData": ex2aacNotFndGUIDEntryConfigData,
       "ex2aacNotFndGUIDEntriesUserData": ex2aacNotFndGUIDEntriesUserData,
       "ex2aacNotFndGUIDEntryMemConfigDa": ex2aacNotFndGUIDEntryMemConfigDa,
       "ex2aacNotFndGUIDEntryMemUserData": ex2aacNotFndGUIDEntryMemUserData,
       "ex2aacOutstandingAsyncNotifies": ex2aacOutstandingAsyncNotifies,
       "ex2aacOutstandingAsyncReads": ex2aacOutstandingAsyncReads,
       "ex2aacOutstandingAsyncSearches": ex2aacOutstandingAsyncSearches,
       "ex2aacSearchEntriesConfigData": ex2aacSearchEntriesConfigData,
       "ex2aacSearchEntriesUserData": ex2aacSearchEntriesUserData,
       "ex2aacSearchEntriesMemConfigData": ex2aacSearchEntriesMemConfigData,
       "ex2aacSearchEntryMemoryUserData": ex2aacSearchEntryMemoryUserData,
       "ex2aacTotalEntriesConfigData": ex2aacTotalEntriesConfigData,
       "ex2aacTotalEntriesUserData": ex2aacTotalEntriesUserData,
       "ex2aacTotalEntriesMemConfigData": ex2aacTotalEntriesMemConfigData,
       "ex2aacTotalEntriesMemoryUserData": ex2aacTotalEntriesMemoryUserData,
       "ex2ADAccessDomainControllerTable": ex2ADAccessDomainControllerTable,
       "ex2ADAccessDomainControllerEntry": ex2ADAccessDomainControllerEntry,
       "ex2aadcInstance": ex2aadcInstance,
       "ex2aadcBindFailuresPerMinute": ex2aadcBindFailuresPerMinute,
       "ex2aadcCriticalDataFlag": ex2aadcCriticalDataFlag,
       "ex2aadcDsGetDcNameElapsedTime": ex2aadcDsGetDcNameElapsedTime,
       "ex2aadcGCCapableFlag": ex2aadcGCCapableFlag,
       "ex2aadcIsSynchronizedFlag": ex2aadcIsSynchronizedFlag,
       "ex2aadcKerberosTicketLifetime": ex2aadcKerberosTicketLifetime,
       "ex2aadcLDAPDisconnectsPerMinute": ex2aadcLDAPDisconnectsPerMinute,
       "ex2aadcLDAPFatalErrorsPerMinute": ex2aadcLDAPFatalErrorsPerMinute,
       "ex2aadcLDAPPagesPerSec": ex2aadcLDAPPagesPerSec,
       "ex2aadcLDAPReadTime": ex2aadcLDAPReadTime,
       "ex2aadcLDAPReadCallsPerSec": ex2aadcLDAPReadCallsPerSec,
       "ex2aadcLDAPSearchTime": ex2aadcLDAPSearchTime,
       "ex2aadcLDAPSearchCallsPerSec": ex2aadcLDAPSearchCallsPerSec,
       "ex2aadcLDAPSearchTimedOutPerMin": ex2aadcLDAPSearchTimedOutPerMin,
       "ex2aadcLDAPVLVRequestsPerSec": ex2aadcLDAPVLVRequestsPerSec,
       "ex2aadcLDAPConnectionLifetime": ex2aadcLDAPConnectionLifetime,
       "ex2aadcLocalSiteFlag": ex2aadcLocalSiteFlag,
       "ex2aadcLongRunningLDAPOperPerMin": ex2aadcLongRunningLDAPOperPerMin,
       "ex2aadcNetlogonFlag": ex2aadcNetlogonFlag,
       "ex2aadcNumberOfOutstandRequests": ex2aadcNumberOfOutstandRequests,
       "ex2aadcOSVersionFlag": ex2aadcOSVersionFlag,
       "ex2aadcPDCFlag": ex2aadcPDCFlag,
       "ex2aadcReachabilityBitmask": ex2aadcReachabilityBitmask,
       "ex2aadcSACLRightFlag": ex2aadcSACLRightFlag,
       "ex2aadcUserSearchesFailPerMinute": ex2aadcUserSearchesFailPerMinute,
       "ex2aadcGethostbynameElapsedTime": ex2aadcGethostbynameElapsedTime,
       "ex2ADAccessGlobalCounters": ex2ADAccessGlobalCounters,
       "ex2aagcDNSQueryDurationTime": ex2aagcDNSQueryDurationTime,
       "ex2aagcInSiteDomainControllers": ex2aagcInSiteDomainControllers,
       "ex2aagcInSiteGlobalCatalogs": ex2aagcInSiteGlobalCatalogs,
       "ex2aagcOutOfSiteDomainController": ex2aagcOutOfSiteDomainController,
       "ex2aagcOutOfSiteGlobalCatalogs": ex2aagcOutOfSiteGlobalCatalogs,
       "ex2aagcTopologyDiscoveryDuraTime": ex2aagcTopologyDiscoveryDuraTime,
       "ex2ADAccessProcessesTable": ex2ADAccessProcessesTable,
       "ex2ADAccessProcessesEntry": ex2ADAccessProcessesEntry,
       "ex2aapInstance": ex2aapInstance,
       "ex2aapCriticlValidFailuresPerMin": ex2aapCriticlValidFailuresPerMin,
       "ex2aapIgnorValidatFailuresPerMin": ex2aapIgnorValidatFailuresPerMin,
       "ex2aapLDAPNotFndConfigRdCallSec": ex2aapLDAPNotFndConfigRdCallSec,
       "ex2aapLDAPPagesPerSec": ex2aapLDAPPagesPerSec,
       "ex2aapLDAPReadTime": ex2aapLDAPReadTime,
       "ex2aapLDAPReadCallsPerSec": ex2aapLDAPReadCallsPerSec,
       "ex2aapLDAPSearchTime": ex2aapLDAPSearchTime,
       "ex2aapLDAPSearchCallsPerSec": ex2aapLDAPSearchCallsPerSec,
       "ex2aapLDAPTimeoutErrorsPerSec": ex2aapLDAPTimeoutErrorsPerSec,
       "ex2aapLDAPVLVRequestsPerSec": ex2aapLDAPVLVRequestsPerSec,
       "ex2aapLDAPWriteTime": ex2aapLDAPWriteTime,
       "ex2aapLDAPWriteCallsPerSec": ex2aapLDAPWriteCallsPerSec,
       "ex2aapLDAPNotificaReportedPerSec": ex2aapLDAPNotificaReportedPerSec,
       "ex2aapLDAPNotificaReceivedPerSec": ex2aapLDAPNotificaReceivedPerSec,
       "ex2aapLongRunningLDAPOperaPerMin": ex2aapLongRunningLDAPOperaPerMin,
       "ex2aapNonCriticalValidFailPerMin": ex2aapNonCriticalValidFailPerMin,
       "ex2aapNumberOfOutstandingRequest": ex2aapNumberOfOutstandingRequest,
       "ex2aapOpenConnectionToDomainCtrl": ex2aapOpenConnectionToDomainCtrl,
       "ex2aapOpenConnectionsToGlobalCat": ex2aapOpenConnectionsToGlobalCat,
       "ex2aapProcessID": ex2aapProcessID,
       "ex2aapTopologyVersion": ex2aapTopologyVersion,
       "ex2ActiveSync": ex2ActiveSync,
       "ex2asAveragePingTime": ex2asAveragePingTime,
       "ex2asAverageRequestTime": ex2asAverageRequestTime,
       "ex2asBadItemReportGeneratedTotal": ex2asBadItemReportGeneratedTotal,
       "ex2asBusyThreads": ex2asBusyThreads,
       "ex2asConflictConcurrentSyncTotal": ex2asConflictConcurrentSyncTotal,
       "ex2asConflictConcurrentSyncPrSec": ex2asConflictConcurrentSyncPrSec,
       "ex2asCreateCollectionCommandsSec": ex2asCreateCollectionCommandsSec,
       "ex2asCreateCollectionTotal": ex2asCreateCollectionTotal,
       "ex2asCurrentRequests": ex2asCurrentRequests,
       "ex2asDeleteCollectionCommandsSec": ex2asDeleteCollectionCommandsSec,
       "ex2asDeleteCollectionTotal": ex2asDeleteCollectionTotal,
       "ex2asDocuLibraryFetchCommandsSec": ex2asDocuLibraryFetchCommandsSec,
       "ex2asDocumentLibraryFetchTotal": ex2asDocumentLibraryFetchTotal,
       "ex2asDocumentLibrarySearchTotal": ex2asDocumentLibrarySearchTotal,
       "ex2asDocumentLibrarySearchPerSec": ex2asDocumentLibrarySearchPerSec,
       "ex2asEmptyFolderContentsTotal": ex2asEmptyFolderContentsTotal,
       "ex2asFailedItemConversionTotal": ex2asFailedItemConversionTotal,
       "ex2asFolderCreateCommandsPerSec": ex2asFolderCreateCommandsPerSec,
       "ex2asFolderCreateTotal": ex2asFolderCreateTotal,
       "ex2asFolderDeleteCommandsPerSec": ex2asFolderDeleteCommandsPerSec,
       "ex2asFolderDeleteTotal": ex2asFolderDeleteTotal,
       "ex2asFolderSyncCommandsPerSec": ex2asFolderSyncCommandsPerSec,
       "ex2asFolderSyncTotal": ex2asFolderSyncTotal,
       "ex2asFolderUpdateCommandsPerSec": ex2asFolderUpdateCommandsPerSec,
       "ex2asFolderUpdateTotal": ex2asFolderUpdateTotal,
       "ex2asGALSearchTotal": ex2asGALSearchTotal,
       "ex2asGALSearchesPerSec": ex2asGALSearchesPerSec,
       "ex2asGetAttachmentCommandsPerSec": ex2asGetAttachmentCommandsPerSec,
       "ex2asGetAttachmentTotal": ex2asGetAttachmentTotal,
       "ex2asGetHierarchyCommandsPerSec": ex2asGetHierarchyCommandsPerSec,
       "ex2asGetHierarchyTotal": ex2asGetHierarchyTotal,
       "ex2asGetItemEstimatCommandPerSec": ex2asGetItemEstimatCommandPerSec,
       "ex2asGetItemEstimateTotal": ex2asGetItemEstimateTotal,
       "ex2asHeartbeatInterval": ex2asHeartbeatInterval,
       "ex2asIdleThreads": ex2asIdleThreads,
       "ex2asIncomingProxyRequestsTotal": ex2asIncomingProxyRequestsTotal,
       "ex2asItemOperationsCommandPerSec": ex2asItemOperationsCommandPerSec,
       "ex2asItemOperationsTotal": ex2asItemOperationsTotal,
       "ex2asMailboxAttchFetchCommandSec": ex2asMailboxAttchFetchCommandSec,
       "ex2asMailboxAttachmentFetchTotal": ex2asMailboxAttachmentFetchTotal,
       "ex2asMailboxItemFetchCommandsSec": ex2asMailboxItemFetchCommandsSec,
       "ex2asMailboxItemFetchTotal": ex2asMailboxItemFetchTotal,
       "ex2asMailboxSearchTotal": ex2asMailboxSearchTotal,
       "ex2asMailboxSearchesPerSec": ex2asMailboxSearchesPerSec,
       "ex2asMeetingResponsCommandPerSec": ex2asMeetingResponsCommandPerSec,
       "ex2asMeetingResponseTotal": ex2asMeetingResponseTotal,
       "ex2asMoveCollectionCommandPerSec": ex2asMoveCollectionCommandPerSec,
       "ex2asMoveCollectionTotal": ex2asMoveCollectionTotal,
       "ex2asMoveItemsCommandsPerSec": ex2asMoveItemsCommandsPerSec,
       "ex2asMoveItemsTotal": ex2asMoveItemsTotal,
       "ex2asNumEmptyFoldrContentProcSec": ex2asNumEmptyFoldrContentProcSec,
       "ex2asOptionsCommandsPerSec": ex2asOptionsCommandsPerSec,
       "ex2asOptionsTotal": ex2asOptionsTotal,
       "ex2asOutgoingProxyRequestsTotal": ex2asOutgoingProxyRequestsTotal,
       "ex2asPID": ex2asPID,
       "ex2asPingCommandsDroppedPerSec": ex2asPingCommandsDroppedPerSec,
       "ex2asPingCommandsPending": ex2asPingCommandsPending,
       "ex2asPingCommandsPerSec": ex2asPingCommandsPerSec,
       "ex2asPingDroppedTotal": ex2asPingDroppedTotal,
       "ex2asPingTotal": ex2asPingTotal,
       "ex2asProvisionCommandsPerSec": ex2asProvisionCommandsPerSec,
       "ex2asProvisionTotal": ex2asProvisionTotal,
       "ex2asProxyLogonCommandsSentTotal": ex2asProxyLogonCommandsSentTotal,
       "ex2asProxyLogonReceivedTotal": ex2asProxyLogonReceivedTotal,
       "ex2asRecoverySyncCommandsPerSec": ex2asRecoverySyncCommandsPerSec,
       "ex2asRecoverySyncTotal": ex2asRecoverySyncTotal,
       "ex2asRequestsQueued": ex2asRequestsQueued,
       "ex2asRequestsTotal": ex2asRequestsTotal,
       "ex2asRequestsPerSec": ex2asRequestsPerSec,
       "ex2asSearchCommandsPerSec": ex2asSearchCommandsPerSec,
       "ex2asSearchTotal": ex2asSearchTotal,
       "ex2asSendMailCommandsPerSec": ex2asSendMailCommandsPerSec,
       "ex2asSendMailTotal": ex2asSendMailTotal,
       "ex2asSettingsCommandsPerSec": ex2asSettingsCommandsPerSec,
       "ex2asSettingsTotal": ex2asSettingsTotal,
       "ex2asSmartForwardCommandsPerSec": ex2asSmartForwardCommandsPerSec,
       "ex2asSmartForwardTotal": ex2asSmartForwardTotal,
       "ex2asSmartReplyCommandsPerSec": ex2asSmartReplyCommandsPerSec,
       "ex2asSmartReplyTotal": ex2asSmartReplyTotal,
       "ex2asSyncCommandsDroppedPerSec": ex2asSyncCommandsDroppedPerSec,
       "ex2asSyncCommandsPending": ex2asSyncCommandsPending,
       "ex2asSyncCommandsPerSec": ex2asSyncCommandsPerSec,
       "ex2asSyncDroppedTotal": ex2asSyncDroppedTotal,
       "ex2asSyncStateKBytesLeftCompress": ex2asSyncStateKBytesLeftCompress,
       "ex2asSyncStateKBytesTotal": ex2asSyncStateKBytesTotal,
       "ex2asSyncTotal": ex2asSyncTotal,
       "ex2asWrongCASProxyRequestsTotal": ex2asWrongCASProxyRequestsTotal,
       "ex2AssistantsTable": ex2AssistantsTable,
       "ex2AssistantsEntry": ex2AssistantsEntry,
       "ex2aInstance": ex2aInstance,
       "ex2aAvgEventProcessTimeInSeconds": ex2aAvgEventProcessTimeInSeconds,
       "ex2aAvgEventQueueTimeInSeconds": ex2aAvgEventQueueTimeInSeconds,
       "ex2aAvgMailboxProcessTimeSeconds": ex2aAvgMailboxProcessTimeSeconds,
       "ex2aAvgQueueSizeEventDispatchers": ex2aAvgQueueSizeEventDispatchers,
       "ex2aEventsPolled": ex2aEventsPolled,
       "ex2aEventsPolledPerSec": ex2aEventsPolledPerSec,
       "ex2aEventsProcessed": ex2aEventsProcessed,
       "ex2aEventsInQueue": ex2aEventsInQueue,
       "ex2aHighestEventCounterPolled": ex2aHighestEventCounterPolled,
       "ex2aMailboxesProcessed": ex2aMailboxesProcessed,
       "ex2aMailboxesProcessedPerSec": ex2aMailboxesProcessedPerSec,
       "ex2aNumberOfEventDispatchers": ex2aNumberOfEventDispatchers,
       "ex2aNumberOfFailEventDispatchers": ex2aNumberOfFailEventDispatchers,
       "ex2aNumberOfHandledExceptions": ex2aNumberOfHandledExceptions,
       "ex2aNumberOfThreadsUsed": ex2aNumberOfThreadsUsed,
       "ex2aNumberEventsProcessPerSecond": ex2aNumberEventsProcessPerSecond,
       "ex2aPercentageFailEventDispatchr": ex2aPercentageFailEventDispatchr,
       "ex2aPercentageOfInterestingEvent": ex2aPercentageOfInterestingEvent,
       "ex2aPollingDelay": ex2aPollingDelay,
       "ex2AvailabilityService": ex2AvailabilityService,
       "ex2aserAvailabilityRequestsSec": ex2aserAvailabilityRequestsSec,
       "ex2aserAvgNumMailboxProcessReqst": ex2aserAvgNumMailboxProcessReqst,
       "ex2aserAvgTimProCrsFrstFreBsyReq": ex2aserAvgTimProCrsFrstFreBsyReq,
       "ex2aserAvgTimProCrsSiteFreBsyReq": ex2aserAvgTimProCrsSiteFreBsyReq,
       "ex2aserAvgTimeProcessFreeBusyReq": ex2aserAvgTimeProcessFreeBusyReq,
       "ex2aserAvgTimeProcessMtgSuggRequ": ex2aserAvgTimeProcessMtgSuggRequ,
       "ex2aserCrsFrstCalendarFailureSec": ex2aserCrsFrstCalendarFailureSec,
       "ex2aserCrsFrstCalendarQueriesSec": ex2aserCrsFrstCalendarQueriesSec,
       "ex2aserCrsSiteCalendarFailureSec": ex2aserCrsSiteCalendarFailureSec,
       "ex2aserCrsSiteCalendarQueriesSec": ex2aserCrsSiteCalendarQueriesSec,
       "ex2aserForeignConnectorQuerySec": ex2aserForeignConnectorQuerySec,
       "ex2aserForeignConnectReqFailRate": ex2aserForeignConnectReqFailRate,
       "ex2aserIntraSiteCalendarFailSec": ex2aserIntraSiteCalendarFailSec,
       "ex2aserIntraSiteCalendarQuerySec": ex2aserIntraSiteCalendarQuerySec,
       "ex2aserPublicFolderQueriesSec": ex2aserPublicFolderQueriesSec,
       "ex2aserPublicFolderReqFailSec": ex2aserPublicFolderReqFailSec,
       "ex2aserSuggestionsRequestsSec": ex2aserSuggestionsRequestsSec,
       "ex2CalendarAttendant": ex2CalendarAttendant,
       "ex2caAvgCalendarAttendntProcTime": ex2caAvgCalendarAttendntProcTime,
       "ex2caLastCalendarAttendtProcTime": ex2caLastCalendarAttendtProcTime,
       "ex2caLostRaces": ex2caLostRaces,
       "ex2caMeetingCancellations": ex2caMeetingCancellations,
       "ex2caMeetingMessagesDeleted": ex2caMeetingMessagesDeleted,
       "ex2caMeetingMessagesProcessed": ex2caMeetingMessagesProcessed,
       "ex2caMeetingRequests": ex2caMeetingRequests,
       "ex2caMeetingResponses": ex2caMeetingResponses,
       "ex2caRequestsFailed": ex2caRequestsFailed,
       "ex2ConnectionFilteringAgent": ex2ConnectionFilteringAgent,
       "ex2cfaConnectionsOnIPAllowList": ex2cfaConnectionsOnIPAllowList,
       "ex2cfaConnOnIPAllowListProviders": ex2cfaConnOnIPAllowListProviders,
       "ex2cfaConnOnIPAllowListProvidSec": ex2cfaConnOnIPAllowListProvidSec,
       "ex2cfaConnOnIPAllowListSec": ex2cfaConnOnIPAllowListSec,
       "ex2cfaConnectionsOnIPBlockList": ex2cfaConnectionsOnIPBlockList,
       "ex2cfaConnOnIPBlockListProviders": ex2cfaConnOnIPBlockListProviders,
       "ex2cfaConnOnIPBlockListProvidSec": ex2cfaConnOnIPBlockListProvidSec,
       "ex2cfaConnOnIPBlockListPerSec": ex2cfaConnOnIPBlockListPerSec,
       "ex2cfaMsgOrigIPIPAllowList": ex2cfaMsgOrigIPIPAllowList,
       "ex2cfaMsgOrigIPIPAllowListPrv": ex2cfaMsgOrigIPIPAllowListPrv,
       "ex2cfaMsgOrigIPIPAllowListPrvSec": ex2cfaMsgOrigIPIPAllowListPrvSec,
       "ex2cfaMsgOrigIPIPAllowListSec": ex2cfaMsgOrigIPIPAllowListSec,
       "ex2cfaMsgOrigIPIPBlockList": ex2cfaMsgOrigIPIPBlockList,
       "ex2cfaMsgOrigIPIPBlockListPrv": ex2cfaMsgOrigIPIPBlockListPrv,
       "ex2cfaMsgOrigIPIPBlockListPrvSec": ex2cfaMsgOrigIPIPBlockListPrvSec,
       "ex2cfaMsgOrigIPIPBlockListSec": ex2cfaMsgOrigIPIPBlockListSec,
       "ex2ContentFilterAgent": ex2ContentFilterAgent,
       "ex2ctfaBypassRecptDueRecptSafSnd": ex2ctfaBypassRecptDueRecptSafSnd,
       "ex2ctfaMessagesDeleted": ex2ctfaMessagesDeleted,
       "ex2ctfaMessagesQuarantined": ex2ctfaMessagesQuarantined,
       "ex2ctfaMessagesRejected": ex2ctfaMessagesRejected,
       "ex2ctfaMessagesScanned": ex2ctfaMessagesScanned,
       "ex2ctfaMessagesScannedPerSecond": ex2ctfaMessagesScannedPerSecond,
       "ex2ctfaMessageThatBypassScanning": ex2ctfaMessageThatBypassScanning,
       "ex2ctfaMsgBypassScanOrgWideSafe": ex2ctfaMsgBypassScanOrgWideSafe,
       "ex2ctfaMsgIncOtlkEMailPMNotValid": ex2ctfaMsgIncOtlkEMailPMNotValid,
       "ex2ctfaMsgIncOtlkEMailPMValidScs": ex2ctfaMsgIncOtlkEMailPMValidScs,
       "ex2ctfaMessagesWithSCL0": ex2ctfaMessagesWithSCL0,
       "ex2ctfaMessagesWithSCL1": ex2ctfaMessagesWithSCL1,
       "ex2ctfaMessagesWithSCL2": ex2ctfaMessagesWithSCL2,
       "ex2ctfaMessagesWithSCL3": ex2ctfaMessagesWithSCL3,
       "ex2ctfaMessagesWithSCL4": ex2ctfaMessagesWithSCL4,
       "ex2ctfaMessagesWithSCL5": ex2ctfaMessagesWithSCL5,
       "ex2ctfaMessagesWithSCL6": ex2ctfaMessagesWithSCL6,
       "ex2ctfaMessagesWithSCL7": ex2ctfaMessagesWithSCL7,
       "ex2ctfaMessagesWithSCL8": ex2ctfaMessagesWithSCL8,
       "ex2ctfaMessagesWithSCL9": ex2ctfaMessagesWithSCL9,
       "ex2ctfaMessagesWithSCLUnknown": ex2ctfaMessagesWithSCLUnknown,
       "ex2ctfaMessageWithPreexistingSCL": ex2ctfaMessageWithPreexistingSCL,
       "ex2DatabaseTable": ex2DatabaseTable,
       "ex2DatabaseEntry": ex2DatabaseEntry,
       "ex2dbInstance": ex2dbInstance,
       "ex2dbDatabaseCachePercentHit": ex2dbDatabaseCachePercentHit,
       "ex2dbDatabaseCacheSize": ex2dbDatabaseCacheSize,
       "ex2dbDatabaseCacheSizeMB": ex2dbDatabaseCacheSizeMB,
       "ex2dbDatabasePageEvictionsPerSec": ex2dbDatabasePageEvictionsPerSec,
       "ex2dbDatabasePgFaultStallPerSec": ex2dbDatabasePgFaultStallPerSec,
       "ex2dbDatabasePageFaultsPerSec": ex2dbDatabasePageFaultsPerSec,
       "ex2dbIODatabaseReadsAvgLatency": ex2dbIODatabaseReadsAvgLatency,
       "ex2dbIODatabaseReadsPerSec": ex2dbIODatabaseReadsPerSec,
       "ex2dbIODatabaseWriteAvgLatency": ex2dbIODatabaseWriteAvgLatency,
       "ex2dbIODatabaseWritesPerSec": ex2dbIODatabaseWritesPerSec,
       "ex2dbIOLogReadsPerSec": ex2dbIOLogReadsPerSec,
       "ex2dbIOLogWritesAverageLatency": ex2dbIOLogWritesAverageLatency,
       "ex2dbIOLogWritesPerSec": ex2dbIOLogWritesPerSec,
       "ex2dbLogBytesWritePerSec": ex2dbLogBytesWritePerSec,
       "ex2dbLogRecordStallsPerSec": ex2dbLogRecordStallsPerSec,
       "ex2dbLogThreadsWaiting": ex2dbLogThreadsWaiting,
       "ex2dbLogWritesPerSec": ex2dbLogWritesPerSec,
       "ex2dbPagesConverted": ex2dbPagesConverted,
       "ex2dbPagesConvertedPerSec": ex2dbPagesConvertedPerSec,
       "ex2dbRecordsConverted": ex2dbRecordsConverted,
       "ex2dbRecordsConvertedPerSec": ex2dbRecordsConvertedPerSec,
       "ex2dbSessionsPercentUsed": ex2dbSessionsPercentUsed,
       "ex2dbSessionsInUse": ex2dbSessionsInUse,
       "ex2dbTableOpenCachePercentHit": ex2dbTableOpenCachePercentHit,
       "ex2dbTableOpenCacheHitsPerSec": ex2dbTableOpenCacheHitsPerSec,
       "ex2dbTableOpenCacheMissesPerSec": ex2dbTableOpenCacheMissesPerSec,
       "ex2dbTableOpensPerSec": ex2dbTableOpensPerSec,
       "ex2dbVersionBucketsAllocated": ex2dbVersionBucketsAllocated,
       "ex2DatabaseInstancesTable": ex2DatabaseInstancesTable,
       "ex2DatabaseInstancesEntry": ex2DatabaseInstancesEntry,
       "ex2dbiInstance": ex2dbiInstance,
       "ex2dbiIODatabaseRdAvgLatency": ex2dbiIODatabaseRdAvgLatency,
       "ex2dbiIODatabaseReadsPerSec": ex2dbiIODatabaseReadsPerSec,
       "ex2dbiIODatabsWriteAvgLatency": ex2dbiIODatabsWriteAvgLatency,
       "ex2dbiIODatabaseWritesPerSec": ex2dbiIODatabaseWritesPerSec,
       "ex2dbiIOLogReadsPerSec": ex2dbiIOLogReadsPerSec,
       "ex2dbiIOLogWritesAvgLatency": ex2dbiIOLogWritesAvgLatency,
       "ex2dbiIOLogWritesPerSec": ex2dbiIOLogWritesPerSec,
       "ex2dbiLogBytesWritePerSec": ex2dbiLogBytesWritePerSec,
       "ex2dbiLogFileCurrentGeneration": ex2dbiLogFileCurrentGeneration,
       "ex2dbiLogFilesGenerated": ex2dbiLogFilesGenerated,
       "ex2dbiLogFilesGeneratedPremature": ex2dbiLogFilesGeneratedPremature,
       "ex2dbiLogGenerationCheckptDepth": ex2dbiLogGenerationCheckptDepth,
       "ex2dbiLogGeneratnCheckptDepthMax": ex2dbiLogGeneratnCheckptDepthMax,
       "ex2dbiLogGeneratLossResilient": ex2dbiLogGeneratLossResilient,
       "ex2dbiLogRecordStallsPerSec": ex2dbiLogRecordStallsPerSec,
       "ex2dbiLogThreadsWaiting": ex2dbiLogThreadsWaiting,
       "ex2dbiLogWritesPerSec": ex2dbiLogWritesPerSec,
       "ex2dbiPagesConverted": ex2dbiPagesConverted,
       "ex2dbiPagesConvertedPerSec": ex2dbiPagesConvertedPerSec,
       "ex2dbiRecordsConverted": ex2dbiRecordsConverted,
       "ex2dbiRecordsConvertedPerSec": ex2dbiRecordsConvertedPerSec,
       "ex2dbiSessionsPercentUsed": ex2dbiSessionsPercentUsed,
       "ex2dbiSessionsInUse": ex2dbiSessionsInUse,
       "ex2dbiStreamBackupPageReadPerSec": ex2dbiStreamBackupPageReadPerSec,
       "ex2dbiTableOpenCachePercentHit": ex2dbiTableOpenCachePercentHit,
       "ex2dbiTableOpenCacheHitsPerSec": ex2dbiTableOpenCacheHitsPerSec,
       "ex2dbiTableOpenCacheMissesPerSec": ex2dbiTableOpenCacheMissesPerSec,
       "ex2dbiTableOpensPerSec": ex2dbiTableOpensPerSec,
       "ex2dbiVersionBucketsAllocated": ex2dbiVersionBucketsAllocated,
       "ex2DatabaseTableClassesTable": ex2DatabaseTableClassesTable,
       "ex2DatabaseTableClassesEntry": ex2DatabaseTableClassesEntry,
       "ex2dbtcInstance": ex2dbtcInstance,
       "ex2dbtcDatabaseCacheSizeMB": ex2dbtcDatabaseCacheSizeMB,
       "ex2ExtensibilityAgentsTable": ex2ExtensibilityAgentsTable,
       "ex2ExtensibilityAgentsEntry": ex2ExtensibilityAgentsEntry,
       "ex2eaInstance": ex2eaInstance,
       "ex2eaAverageAgentProcessTimeSec": ex2eaAverageAgentProcessTimeSec,
       "ex2eaTotalAgentInvocations": ex2eaTotalAgentInvocations,
       "ex2JournalingAgent": ex2JournalingAgent,
       "ex2jaJournalReportsCreatedPerSec": ex2jaJournalReportsCreatedPerSec,
       "ex2jaJournalReportsCreatedTotal": ex2jaJournalReportsCreatedTotal,
       "ex2jaJournalingProcessingTime": ex2jaJournalingProcessingTime,
       "ex2jaJournalProcesTimePerMessage": ex2jaJournalProcesTimePerMessage,
       "ex2jaMessagesProcessByJournaling": ex2jaMessagesProcessByJournaling,
       "ex2jaUsersJournaled": ex2jaUsersJournaled,
       "ex2jaUsersJournaledPerSec": ex2jaUsersJournaledPerSec,
       "ex2ManagedFolderAssistant": ex2ManagedFolderAssistant,
       "ex2mfaItemsDeletedButRecoverable": ex2mfaItemsDeletedButRecoverable,
       "ex2mfaItemsJournaled": ex2mfaItemsJournaled,
       "ex2mfaItemsMarkPastRetentionDate": ex2mfaItemsMarkPastRetentionDate,
       "ex2mfaItemsMoved": ex2mfaItemsMoved,
       "ex2mfaItemsPermanentlyDeleted": ex2mfaItemsPermanentlyDeleted,
       "ex2mfaItemSubjectRetentionPolicy": ex2mfaItemSubjectRetentionPolicy,
       "ex2OWA": ex2OWA,
       "ex2OWAASQueries": ex2OWAASQueries,
       "ex2OWAASQueriesFailurePercent": ex2OWAASQueriesFailurePercent,
       "ex2OWAActiveConversions": ex2OWAActiveConversions,
       "ex2OWAAttachmentUploadedOWAStart": ex2OWAAttachmentUploadedOWAStart,
       "ex2OWAAverageCheckSpellingTime": ex2OWAAverageCheckSpellingTime,
       "ex2OWAAverageConversionQueueTime": ex2OWAAverageConversionQueueTime,
       "ex2OWAAverageConversionTime": ex2OWAAverageConversionTime,
       "ex2OWAAverageResponseTime": ex2OWAAverageResponseTime,
       "ex2OWAAverageSearchTime": ex2OWAAverageSearchTime,
       "ex2OWACalendarViewRefreshed": ex2OWACalendarViewRefreshed,
       "ex2OWACalendarViewsLoaded": ex2OWACalendarViewsLoaded,
       "ex2OWAConversionRequestsKBPerSec": ex2OWAConversionRequestsKBPerSec,
       "ex2OWAConversionResponseKBPerSec": ex2OWAConversionResponseKBPerSec,
       "ex2OWAConversions": ex2OWAConversions,
       "ex2OWAConversionsEndedByTimeOut": ex2OWAConversionsEndedByTimeOut,
       "ex2OWAConversionsEndedWithErrors": ex2OWAConversionsEndedWithErrors,
       "ex2OWACurrentProxyUsers": ex2OWACurrentProxyUsers,
       "ex2OWACurrentUniqueUsers": ex2OWACurrentUniqueUsers,
       "ex2OWACurrentUniqueUsersLight": ex2OWACurrentUniqueUsersLight,
       "ex2OWACurrentUniqueUsersPremium": ex2OWACurrentUniqueUsersPremium,
       "ex2OWACurrentUsers": ex2OWACurrentUsers,
       "ex2OWACurrentUsersLight": ex2OWACurrentUsersLight,
       "ex2OWACurrentUsersPremium": ex2OWACurrentUsersPremium,
       "ex2OWAFailedRequestsPerSec": ex2OWAFailedRequestsPerSec,
       "ex2OWAInvalidCanaryRequests": ex2OWAInvalidCanaryRequests,
       "ex2OWAItemsCreatedSinceOWAStart": ex2OWAItemsCreatedSinceOWAStart,
       "ex2OWAItemsDeletedSinceOWAStart": ex2OWAItemsDeletedSinceOWAStart,
       "ex2OWAItemsUpdatedSinceOWAStart": ex2OWAItemsUpdatedSinceOWAStart,
       "ex2OWALogonsPerSec": ex2OWALogonsPerSec,
       "ex2OWALogonsPerSecLight": ex2OWALogonsPerSecLight,
       "ex2OWALogonsPerSecPremium": ex2OWALogonsPerSecPremium,
       "ex2OWAMailViewRefreshes": ex2OWAMailViewRefreshes,
       "ex2OWAMailViewsLoaded": ex2OWAMailViewsLoaded,
       "ex2OWAMessagesSent": ex2OWAMessagesSent,
       "ex2OWANamesChecked": ex2OWANamesChecked,
       "ex2OWAPID": ex2OWAPID,
       "ex2OWAPasswordChanges": ex2OWAPasswordChanges,
       "ex2OWAPeakUserCount": ex2OWAPeakUserCount,
       "ex2OWAPeakUserCountLight": ex2OWAPeakUserCountLight,
       "ex2OWAPeakUserCountPremium": ex2OWAPeakUserCountPremium,
       "ex2OWAProxyRequestBytes": ex2OWAProxyRequestBytes,
       "ex2OWAProxyResponseBytes": ex2OWAProxyResponseBytes,
       "ex2OWAProxyResponseTimeAverage": ex2OWAProxyResponseTimeAverage,
       "ex2OWAProxyUserRequests": ex2OWAProxyUserRequests,
       "ex2OWAProxyUserRequestsPerSec": ex2OWAProxyUserRequestsPerSec,
       "ex2OWAQueuedConversionRequests": ex2OWAQueuedConversionRequests,
       "ex2OWARejectedConversions": ex2OWARejectedConversions,
       "ex2OWARequests": ex2OWARequests,
       "ex2OWARequestsFailed": ex2OWARequestsFailed,
       "ex2OWARequestsPerSec": ex2OWARequestsPerSec,
       "ex2OWASearches": ex2OWASearches,
       "ex2OWASearchesExecuted": ex2OWASearchesExecuted,
       "ex2OWASearchesTimedOut": ex2OWASearchesTimedOut,
       "ex2OWASessionsEndedByLogoff": ex2OWASessionsEndedByLogoff,
       "ex2OWASessionsEndedByTimeOut": ex2OWASessionsEndedByTimeOut,
       "ex2OWASpellingChecks": ex2OWASpellingChecks,
       "ex2OWAStoreLogonFailurePercent": ex2OWAStoreLogonFailurePercent,
       "ex2OWASuccessConversnReqKBPerSec": ex2OWASuccessConversnReqKBPerSec,
       "ex2OWATotalUniqueUsers": ex2OWATotalUniqueUsers,
       "ex2OWATotalUniqueUsersLight": ex2OWATotalUniqueUsersLight,
       "ex2OWATotalUniqueUsersPremium": ex2OWATotalUniqueUsersPremium,
       "ex2OWATotalUsers": ex2OWATotalUsers,
       "ex2OWATotalUsersLight": ex2OWATotalUsersLight,
       "ex2OWATotalUsersPremium": ex2OWATotalUsersPremium,
       "ex2OWAUNCRequests": ex2OWAUNCRequests,
       "ex2OWAUNCResponseBytes": ex2OWAUNCResponseBytes,
       "ex2OWAUNCResponseBytesPerSec": ex2OWAUNCResponseBytesPerSec,
       "ex2OWAWSSRequests": ex2OWAWSSRequests,
       "ex2OWAWSSResponseBytes": ex2OWAWSSResponseBytes,
       "ex2OWAWSSResponseBytesPerSec": ex2OWAWSSResponseBytesPerSec,
       "ex2OledbEventsTable": ex2OledbEventsTable,
       "ex2OledbEventsEntry": ex2OledbEventsEntry,
       "ex2oeInstance": ex2oeInstance,
       "ex2oeEventsCompletionRate": ex2oeEventsCompletionRate,
       "ex2oeEventsCompletionTotal": ex2oeEventsCompletionTotal,
       "ex2oeEventsSubmissionRate": ex2oeEventsSubmissionRate,
       "ex2oeEventsSubmissionTotal": ex2oeEventsSubmissionTotal,
       "ex2OledbResourceTable": ex2OledbResourceTable,
       "ex2OledbResourceEntry": ex2OledbResourceEntry,
       "ex2orInstance": ex2orInstance,
       "ex2orActiveCommands": ex2orActiveCommands,
       "ex2orActiveDataSources": ex2orActiveDataSources,
       "ex2orActiveRows": ex2orActiveRows,
       "ex2orActiveRowsets": ex2orActiveRowsets,
       "ex2orActiveSessions": ex2orActiveSessions,
       "ex2orActiveStreams": ex2orActiveStreams,
       "ex2orResourceBindingsRate": ex2orResourceBindingsRate,
       "ex2orResourceBindingsTotal": ex2orResourceBindingsTotal,
       "ex2orRowsetsOpenedRate": ex2orRowsetsOpenedRate,
       "ex2orRowsetsOpenedTotal": ex2orRowsetsOpenedTotal,
       "ex2orTransactionsAbortedRate": ex2orTransactionsAbortedRate,
       "ex2orTransactionsAbortedTotal": ex2orTransactionsAbortedTotal,
       "ex2orTransactionsCommittedRate": ex2orTransactionsCommittedRate,
       "ex2orTransactionsCommittedTotal": ex2orTransactionsCommittedTotal,
       "ex2orTransactionsStartedRate": ex2orTransactionsStartedRate,
       "ex2orTransactionsStartedTotal": ex2orTransactionsStartedTotal,
       "ex2ProtocolAnalysisAgent": ex2ProtocolAnalysisAgent,
       "ex2paaCalculationsAtSRL0": ex2paaCalculationsAtSRL0,
       "ex2paaCalculationsAtSRL1": ex2paaCalculationsAtSRL1,
       "ex2paaCalculationsAtSRL2": ex2paaCalculationsAtSRL2,
       "ex2paaCalculationsAtSRL3": ex2paaCalculationsAtSRL3,
       "ex2paaCalculationsAtSRL4": ex2paaCalculationsAtSRL4,
       "ex2paaCalculationsAtSRL5": ex2paaCalculationsAtSRL5,
       "ex2paaCalculationsAtSRL6": ex2paaCalculationsAtSRL6,
       "ex2paaCalculationsAtSRL7": ex2paaCalculationsAtSRL7,
       "ex2paaCalculationsAtSRL8": ex2paaCalculationsAtSRL8,
       "ex2paaCalculationsAtSRL9": ex2paaCalculationsAtSRL9,
       "ex2paaSendersBlockLocalOpenProxy": ex2paaSendersBlockLocalOpenProxy,
       "ex2paaSendersBlockedOfLocalSRL": ex2paaSendersBlockedOfLocalSRL,
       "ex2paaSenderBlockRemoteOpenProxy": ex2paaSenderBlockRemoteOpenProxy,
       "ex2paaSendersBlockedOfRemoteSRL": ex2paaSendersBlockedOfRemoteSRL,
       "ex2paaSendersBypassLocalSRLCalc": ex2paaSendersBypassLocalSRLCalc,
       "ex2paaSendersProcessed": ex2paaSendersProcessed,
       "ex2ProtocolAnalysisBackgndAgent": ex2ProtocolAnalysisBackgndAgent,
       "ex2RecipientCacheTable": ex2RecipientCacheTable,
       "ex2RecipientCacheEntry": ex2RecipientCacheEntry,
       "ex2rcInstance": ex2rcInstance,
       "ex2rcAddressLookupsPending": ex2rcAddressLookupsPending,
       "ex2rcBatchedAddressLookups": ex2rcBatchedAddressLookups,
       "ex2rcExpandGroupRequests": ex2rcExpandGroupRequests,
       "ex2rcIndividualAddressLookups": ex2rcIndividualAddressLookups,
       "ex2RecipientFilterAgent": ex2RecipientFilterAgent,
       "ex2rfaRecipientsRejectBlockList": ex2rfaRecipientsRejectBlockList,
       "ex2rfaRecipientRejectBlockLstSec": ex2rfaRecipientRejectBlockLstSec,
       "ex2rfaRecpntRejectRecipientValid": ex2rfaRecpntRejectRecipientValid,
       "ex2rfaRecpntRejectRecpntValidSec": ex2rfaRecpntRejectRecpntValidSec,
       "ex2ReplicaSeederTable": ex2ReplicaSeederTable,
       "ex2ReplicaSeederEntry": ex2ReplicaSeederEntry,
       "ex2rsInstance": ex2rsInstance,
       "ex2rsSeedingFinishedPercent": ex2rsSeedingFinishedPercent,
       "ex2ReplicationTable": ex2ReplicationTable,
       "ex2ReplicationEntry": ex2ReplicationEntry,
       "ex2rInstance": ex2rInstance,
       "ex2rCopyQueExceedMntThresholdCCR": ex2rCopyQueExceedMntThresholdCCR,
       "ex2rCopyGenerationNumber": ex2rCopyGenerationNumber,
       "ex2rCopyNotifiyGenerationNumber": ex2rCopyNotifiyGenerationNumber,
       "ex2rCopyQueueLength": ex2rCopyQueueLength,
       "ex2rFailed": ex2rFailed,
       "ex2rInitializing": ex2rInitializing,
       "ex2rInspectorGenerationNumber": ex2rInspectorGenerationNumber,
       "ex2rReplayBatchSize": ex2rReplayBatchSize,
       "ex2rReplayGenerationNumber": ex2rReplayGenerationNumber,
       "ex2rReplayGenerationsComplete": ex2rReplayGenerationsComplete,
       "ex2rReplayGenerationsPerMinute": ex2rReplayGenerationsPerMinute,
       "ex2rReplayGenerationsRemaining": ex2rReplayGenerationsRemaining,
       "ex2rReplayNotifyGenerationNumber": ex2rReplayNotifyGenerationNumber,
       "ex2rReplayQueueLength": ex2rReplayQueueLength,
       "ex2rSuspended": ex2rSuspended,
       "ex2rTruncatedGenerationNumber": ex2rTruncatedGenerationNumber,
       "ex2ResourceBooking": ex2ResourceBooking,
       "ex2rbAccepted": ex2rbAccepted,
       "ex2rbAvgResourceBookProcessTime": ex2rbAvgResourceBookProcessTime,
       "ex2rbCancelled": ex2rbCancelled,
       "ex2rbDeclined": ex2rbDeclined,
       "ex2rbEvents": ex2rbEvents,
       "ex2rbRequestsFailed": ex2rbRequestsFailed,
       "ex2rbRequestsProcessed": ex2rbRequestsProcessed,
       "ex2rbRequestsSubmitted": ex2rbRequestsSubmitted,
       "ex2SearchIndexer": ex2SearchIndexer,
       "ex2sAverageBatchLatency": ex2sAverageBatchLatency,
       "ex2siAverageBatchSize": ex2siAverageBatchSize,
       "ex2siNumberDatabasesBeingCrawled": ex2siNumberDatabasesBeingCrawled,
       "ex2siNumberDatabasesBeingIndexed": ex2siNumberDatabasesBeingIndexed,
       "ex2siNumberOfDisabledDatabases": ex2siNumberOfDisabledDatabases,
       "ex2siNumIndexDatabaseUpDateNotif": ex2siNumIndexDatabaseUpDateNotif,
       "ex2SearchIndicesTable": ex2SearchIndicesTable,
       "ex2SearchIndicesEntry": ex2SearchIndicesEntry,
       "ex2sidInstance": ex2sidInstance,
       "ex2sidAgeLastNotificationIndexed": ex2sidAgeLastNotificationIndexed,
       "ex2sidAgeLastNotificationProcess": ex2sidAgeLastNotificationProcess,
       "ex2sidAvgLatencyRPCsDuringCrawl": ex2sidAvgLatencyRPCsDuringCrawl,
       "ex2sidAvgLatencyRPCObtainContent": ex2sidAvgLatencyRPCObtainContent,
       "ex2sidAverageDocumentIndexngTime": ex2sidAverageDocumentIndexngTime,
       "ex2sidAvgLatencyRPCsToGetNotific": ex2sidAvgLatencyRPCsToGetNotific,
       "ex2sidAvgSizeOfIndexedAttachment": ex2sidAvgSizeOfIndexedAttachment,
       "ex2sidDocumentIndexingRate": ex2sidDocumentIndexingRate,
       "ex2sidFullCrawlModeStatus": ex2sidFullCrawlModeStatus,
       "ex2sidNumContentConversionsDone": ex2sidNumContentConversionsDone,
       "ex2sidNumCreateNotifications": ex2sidNumCreateNotifications,
       "ex2sidNumCreateNotificationPrSec": ex2sidNumCreateNotificationPrSec,
       "ex2sidNumDeleteNotifications": ex2sidNumDeleteNotifications,
       "ex2sidNumDeleteNotificationPrSec": ex2sidNumDeleteNotificationPrSec,
       "ex2sidNumDocumentsSuccessIndexed": ex2sidNumDocumentsSuccessIndexed,
       "ex2sidNumDocumentFailDuringIndex": ex2sidNumDocumentFailDuringIndex,
       "ex2sidNumberOfFailedRetries": ex2sidNumberOfFailedRetries,
       "ex2sidNumberOfHTMLMessageBodies": ex2sidNumberOfHTMLMessageBodies,
       "ex2sidNumberOfIndexedAttachments": ex2sidNumberOfIndexedAttachments,
       "ex2sidNumItemInNotificationQueue": ex2sidNumItemInNotificationQueue,
       "ex2sidNumMailboxesLeftToCrawl": ex2sidNumMailboxesLeftToCrawl,
       "ex2sidNumberOfMoveNotifications": ex2sidNumberOfMoveNotifications,
       "ex2sidNumMoveNotificationsPerSec": ex2sidNumMoveNotificationsPerSec,
       "ex2sidNumberOfOutstandingBatches": ex2sidNumberOfOutstandingBatches,
       "ex2sidNumOutstandingDocuments": ex2sidNumOutstandingDocuments,
       "ex2sidNumPlainTextMessageBodies": ex2sidNumPlainTextMessageBodies,
       "ex2sidNumberOfRTFMessageBodies": ex2sidNumberOfRTFMessageBodies,
       "ex2sidNumRecentMoveMailboxCrawl": ex2sidNumRecentMoveMailboxCrawl,
       "ex2sidNumberOfRetries": ex2sidNumberOfRetries,
       "ex2sidNumberOfSuccessfulRetries": ex2sidNumberOfSuccessfulRetries,
       "ex2sidNumUpdateNotifications": ex2sidNumUpdateNotifications,
       "ex2sidNumUpdateNotificationPrSec": ex2sidNumUpdateNotificationPrSec,
       "ex2sidPercentageNotificOptimize": ex2sidPercentageNotificOptimize,
       "ex2sidRecentAvgLatencyRPCUseObta": ex2sidRecentAvgLatencyRPCUseObta,
       "ex2sidThrottlingDelayValue": ex2sidThrottlingDelayValue,
       "ex2SecureMailTransportTable": ex2SecureMailTransportTable,
       "ex2SecureMailTransportEntry": ex2SecureMailTransportEntry,
       "ex2smtInstance": ex2smtInstance,
       "ex2smtDomainSecureMessageReceive": ex2smtDomainSecureMessageReceive,
       "ex2smtDomainSecureMessagesSent": ex2smtDomainSecureMessagesSent,
       "ex2smtDomSecureOutbndSessionFail": ex2smtDomSecureOutbndSessionFail,
       "ex2SenderFilterAgent": ex2SenderFilterAgent,
       "ex2sfaMessagesEvalBySenderFilter": ex2sfaMessagesEvalBySenderFilter,
       "ex2sfaMsgEvaluatSendFilterPerSec": ex2sfaMsgEvaluatSendFilterPerSec,
       "ex2sfaMsgFilteredBySenderFilter": ex2sfaMsgFilteredBySenderFilter,
       "ex2sfaMsgFilterSenderFilterPrSec": ex2sfaMsgFilterSenderFilterPrSec,
       "ex2SenderIdAgent": ex2SenderIdAgent,
       "ex2siaDNSQueries": ex2siaDNSQueries,
       "ex2siaDNSQueriesPerSec": ex2siaDNSQueriesPerSec,
       "ex2siaMsgMissingOriginatingIP": ex2siaMsgMissingOriginatingIP,
       "ex2siaMsgMissngOriginateIPPerSec": ex2siaMsgMissngOriginateIPPerSec,
       "ex2siaMsgThatBypassedValidation": ex2siaMsgThatBypassedValidation,
       "ex2siaMsgThatBypassValidatePrSec": ex2siaMsgThatBypassValidatePrSec,
       "ex2siaMessagesValidated": ex2siaMessagesValidated,
       "ex2siaMsgValidFailMalformDomRes": ex2siaMsgValidFailMalformDomRes,
       "ex2siaMsgValidFailNonExistDomRes": ex2siaMsgValidFailNonExistDomRes,
       "ex2siaMsgValidFailNotPermittRes": ex2siaMsgValidFailNotPermittRes,
       "ex2siaMsgValidWithANeutralResult": ex2siaMsgValidWithANeutralResult,
       "ex2siaMsgValidWithANoneResult": ex2siaMsgValidWithANoneResult,
       "ex2siaMsgValidWithAPassResult": ex2siaMsgValidWithAPassResult,
       "ex2siaMsgValidPermErrorResult": ex2siaMsgValidPermErrorResult,
       "ex2siaMsgValidSoftFailResult": ex2siaMsgValidSoftFailResult,
       "ex2siaMsgValidTempErrorResult": ex2siaMsgValidTempErrorResult,
       "ex2siaMessagesValidatedPerSec": ex2siaMessagesValidatedPerSec,
       "ex2siaMsgValidFailMlfrmDomResSec": ex2siaMsgValidFailMlfrmDomResSec,
       "ex2siaMsgValidFailNExstDomResSec": ex2siaMsgValidFailNExstDomResSec,
       "ex2siaMsgValidFailNotPermitRes": ex2siaMsgValidFailNotPermitRes,
       "ex2siaMsgValidPerSecNeutrlResult": ex2siaMsgValidPerSecNeutrlResult,
       "ex2siaMsgValidPerSecNoneResult": ex2siaMsgValidPerSecNoneResult,
       "ex2siaMsgValidPerSecPassResult": ex2siaMsgValidPerSecPassResult,
       "ex2siaMsgValidSecPermErrorResult": ex2siaMsgValidSecPermErrorResult,
       "ex2siaMsgValidPerSecSoftFailRes": ex2siaMsgValidPerSecSoftFailRes,
       "ex2siaMsgValidSecTempErrorResult": ex2siaMsgValidSecTempErrorResult,
       "ex2siaMessagesWithNoPRAPerSec": ex2siaMessagesWithNoPRAPerSec,
       "ex2siaMessagesWithNoPRA": ex2siaMessagesWithNoPRA,
       "ex2StoreDriverTable": ex2StoreDriverTable,
       "ex2StoreDriverEntry": ex2StoreDriverEntry,
       "ex2sdInstance": ex2sdInstance,
       "ex2sdInboundBytesDelivered": ex2sdInboundBytesDelivered,
       "ex2sdInboundDuplicateDeliveries": ex2sdInboundDuplicateDeliveries,
       "ex2sdInboundFailedRecipients": ex2sdInboundFailedRecipients,
       "ex2sdInboundLocalDeliveryCalls": ex2sdInboundLocalDeliveryCalls,
       "ex2sdInboundLocalDelivCallSecond": ex2sdInboundLocalDelivCallSecond,
       "ex2sdInboundMsgDeliveryAttempts": ex2sdInboundMsgDeliveryAttempts,
       "ex2sdInboundMsgDelvrAttmptSecond": ex2sdInboundMsgDelvrAttmptSecond,
       "ex2sdInboundNumDeliveringThreads": ex2sdInboundNumDeliveringThreads,
       "ex2sdInboundRecipientsDelivered": ex2sdInboundRecipientsDelivered,
       "ex2sdInboundRecipntDeliverSecond": ex2sdInboundRecipntDeliverSecond,
       "ex2sdInboundReroutedRecipients": ex2sdInboundReroutedRecipients,
       "ex2sdInboundRetriedRecipients": ex2sdInboundRetriedRecipients,
       "ex2sdInboundSucceededRecipients": ex2sdInboundSucceededRecipients,
       "ex2sdInboundTotalMeetingFailures": ex2sdInboundTotalMeetingFailures,
       "ex2sdInboundTotalMeetingMessages": ex2sdInboundTotalMeetingMessages,
       "ex2sdOutboundMapiEventWithoutMsg": ex2sdOutboundMapiEventWithoutMsg,
       "ex2sdOutboundSubmittedMailItems": ex2sdOutboundSubmittedMailItems,
       "ex2sdOutboundSubmtMailItemSecond": ex2sdOutboundSubmtMailItemSecond,
       "ex2sdOutboundTotalRecipients": ex2sdOutboundTotalRecipients,
       "ex2StoreInterfaceTable": ex2StoreInterfaceTable,
       "ex2StoreInterfaceEntry": ex2StoreInterfaceEntry,
       "ex2sifInstance": ex2sifInstance,
       "ex2sifConnCacheActiveConns": ex2sifConnCacheActiveConns,
       "ex2sifConnCacheIdleConns": ex2sifConnCacheIdleConns,
       "ex2sifConnectionCacheNumCaches": ex2sifConnectionCacheNumCaches,
       "ex2sifConnCacheOutLimitCreations": ex2sifConnCacheOutLimitCreations,
       "ex2sifConnCacheTotalCapacity": ex2sifConnCacheTotalCapacity,
       "ex2sifExRpcConnCreationEvents": ex2sifExRpcConnCreationEvents,
       "ex2sifExRpcConnDisposalEvents": ex2sifExRpcConnDisposalEvents,
       "ex2sifExRpcConnectionOutstanding": ex2sifExRpcConnectionOutstanding,
       "ex2sifROPRequestsComplete": ex2sifROPRequestsComplete,
       "ex2sifROPRequestsOutstanding": ex2sifROPRequestsOutstanding,
       "ex2sifROPRequestsSent": ex2sifROPRequestsSent,
       "ex2sifRPCBytesReceived": ex2sifRPCBytesReceived,
       "ex2sifRPCBytesReceivedAverage": ex2sifRPCBytesReceivedAverage,
       "ex2sifRPCBytesSent": ex2sifRPCBytesSent,
       "ex2sifRPCBytesSentAverage": ex2sifRPCBytesSentAverage,
       "ex2sifRPCLatencyAverageMsec": ex2sifRPCLatencyAverageMsec,
       "ex2sifRPCLatencyTotalMsec": ex2sifRPCLatencyTotalMsec,
       "ex2sifRPCRequestsFailed": ex2sifRPCRequestsFailed,
       "ex2sifRPCRequestsFailedPercent": ex2sifRPCRequestsFailedPercent,
       "ex2sifRPCRequestsFailedException": ex2sifRPCRequestsFailedException,
       "ex2sifRPCRequestsOutstanding": ex2sifRPCRequestsOutstanding,
       "ex2sifRPCRequestsSent": ex2sifRPCRequestsSent,
       "ex2sifRPCRequestsSentPerSec": ex2sifRPCRequestsSentPerSec,
       "ex2sifRPCRequestsSucceeded": ex2sifRPCRequestsSucceeded,
       "ex2sifRPCSlowRequests": ex2sifRPCSlowRequests,
       "ex2sifRPCSlowRequestsPercent": ex2sifRPCSlowRequestsPercent,
       "ex2sifRPCSlowReqLatencyAvgMsec": ex2sifRPCSlowReqLatencyAvgMsec,
       "ex2sifRPCSlowReqLatencyTotalMsec": ex2sifRPCSlowReqLatencyTotalMsec,
       "ex2sifUNKFolders": ex2sifUNKFolders,
       "ex2sifUNKLogons": ex2sifUNKLogons,
       "ex2sifUNKMessages": ex2sifUNKMessages,
       "ex2sifUNKObjectsTotal": ex2sifUNKObjectsTotal,
       "ex2TopologyTable": ex2TopologyTable,
       "ex2TopologyEntry": ex2TopologyEntry,
       "ex2tpInstance": ex2tpInstance,
       "ex2tpLatestExchgTopologyDisTime": ex2tpLatestExchgTopologyDisTime,
       "ex2tpNumExchangeTopologyDiscover": ex2tpNumExchangeTopologyDiscover,
       "ex2tpNumberOfSitelessServers": ex2tpNumberOfSitelessServers,
       "ex2TransportRulesTable": ex2TransportRulesTable,
       "ex2TransportRulesEntry": ex2TransportRulesEntry,
       "ex2trInstance": ex2trInstance,
       "ex2trMessagesEvaluated": ex2trMessagesEvaluated,
       "ex2trMessagesEvaluatedPerSec": ex2trMessagesEvaluatedPerSec,
       "ex2trMessagesProcessed": ex2trMessagesProcessed,
       "ex2trMessagesProcessedPerSec": ex2trMessagesProcessedPerSec,
       "ex2UpdateAgent": ex2UpdateAgent,
       "ex2uaTotalSRLParameterUpdates": ex2uaTotalSRLParameterUpdates,
       "ex2uaTotalUpdates": ex2uaTotalUpdates,
       "ex2WebMailTable": ex2WebMailTable,
       "ex2WebMailEntry": ex2WebMailEntry,
       "ex2wmInstance": ex2wmInstance,
       "ex2wmApptmtAcceptPerDeclineTotal": ex2wmApptmtAcceptPerDeclineTotal,
       "ex2wmApptmtAcceptPrDeclinePerSec": ex2wmApptmtAcceptPrDeclinePerSec,
       "ex2wmApptmtAttachmentEditsTotal": ex2wmApptmtAttachmentEditsTotal,
       "ex2wmApptmtAttachmentEditsPerSec": ex2wmApptmtAttachmentEditsPerSec,
       "ex2wmApptmtDataRetrievesTotal": ex2wmApptmtDataRetrievesTotal,
       "ex2wmApptmtDataRetrievesPerSec": ex2wmApptmtDataRetrievesPerSec,
       "ex2wmApptmtEditRecurrenceTotal": ex2wmApptmtEditRecurrenceTotal,
       "ex2wmApptmtEditRecurrencePerSec": ex2wmApptmtEditRecurrencePerSec,
       "ex2wmAppointmentOpensTotal": ex2wmAppointmentOpensTotal,
       "ex2wmAppointmentOpensPerSec": ex2wmAppointmentOpensPerSec,
       "ex2wmApptmtResolveFreeBusyTotal": ex2wmApptmtResolveFreeBusyTotal,
       "ex2wmApptmtResolveFreeBusyPerSec": ex2wmApptmtResolveFreeBusyPerSec,
       "ex2wmApptmtSaveRecurrencesTotal": ex2wmApptmtSaveRecurrencesTotal,
       "ex2wmApptmtSaveRecurrencesPerSec": ex2wmApptmtSaveRecurrencesPerSec,
       "ex2wmAppointmentSavesTotal": ex2wmAppointmentSavesTotal,
       "ex2wmAppointmentSavesPerSec": ex2wmAppointmentSavesPerSec,
       "ex2wmAppointmentSendsTotal": ex2wmAppointmentSendsTotal,
       "ex2wmAppointmentSendsPerSec": ex2wmAppointmentSendsPerSec,
       "ex2wmAppointmentUpdatesTotal": ex2wmAppointmentUpdatesTotal,
       "ex2wmAppointmentUpdatesPerSec": ex2wmAppointmentUpdatesPerSec,
       "ex2wmAttachmentsDeletedTotal": ex2wmAttachmentsDeletedTotal,
       "ex2wmAttachmentsDeletedPerSec": ex2wmAttachmentsDeletedPerSec,
       "ex2wmAuthenticationCacheHitTotal": ex2wmAuthenticationCacheHitTotal,
       "ex2wmAuthenticationCacheHitPrSec": ex2wmAuthenticationCacheHitPrSec,
       "ex2wmAuthenticationsInCache": ex2wmAuthenticationsInCache,
       "ex2wmAuthenticationsTotal": ex2wmAuthenticationsTotal,
       "ex2wmAuthenticationsPerSec": ex2wmAuthenticationsPerSec,
       "ex2wmFolderCreatesTotal": ex2wmFolderCreatesTotal,
       "ex2wmFolderCreatesPerSec": ex2wmFolderCreatesPerSec,
       "ex2wmFolderGetContentsTotal": ex2wmFolderGetContentsTotal,
       "ex2wmFolderGetContentsPerSec": ex2wmFolderGetContentsPerSec,
       "ex2wmFolderGetViewTotal": ex2wmFolderGetViewTotal,
       "ex2wmFolderGetViewPerSec": ex2wmFolderGetViewPerSec,
       "ex2wmFolderRenamesTotal": ex2wmFolderRenamesTotal,
       "ex2wmFolderRenamesPerSec": ex2wmFolderRenamesPerSec,
       "ex2wmFormsSentTotal": ex2wmFormsSentTotal,
       "ex2wmFormsSentPerSec": ex2wmFormsSentPerSec,
       "ex2wmGetAppFrameTotal": ex2wmGetAppFrameTotal,
       "ex2wmGetAppFramePerSec": ex2wmGetAppFramePerSec,
       "ex2wmGetNavBarTotal": ex2wmGetNavBarTotal,
       "ex2wmGetNavBarPerSec": ex2wmGetNavBarPerSec,
       "ex2wmMessageAttachmentEditsTotal": ex2wmMessageAttachmentEditsTotal,
       "ex2wmMessageAttachmentEditPerSec": ex2wmMessageAttachmentEditPerSec,
       "ex2wmMessageMovesPerCopiesTotal": ex2wmMessageMovesPerCopiesTotal,
       "ex2wmMessageMovesPerCopyPerSec": ex2wmMessageMovesPerCopyPerSec,
       "ex2wmMessageOpensTotal": ex2wmMessageOpensTotal,
       "ex2wmMessageOpensPerSec": ex2wmMessageOpensPerSec,
       "ex2wmMessageSavesTotal": ex2wmMessageSavesTotal,
       "ex2wmMessageSavesPerSec": ex2wmMessageSavesPerSec,
       "ex2wmMessageSendsTotal": ex2wmMessageSendsTotal,
       "ex2wmMessageSendsPerSec": ex2wmMessageSendsPerSec,
       "ex2wmMsgPerApptmtDeletesTotal": ex2wmMsgPerApptmtDeletesTotal,
       "ex2wmMsgPerApptmtDeletesPerSec": ex2wmMsgPerApptmtDeletesPerSec,
       "ex2wmMsgPerAppointmentOpensTotal": ex2wmMsgPerAppointmentOpensTotal,
       "ex2wmMsgPerAppointmentOpenPerSec": ex2wmMsgPerAppointmentOpenPerSec,
       "ex2wmMsgPerAppointmentSavesTotal": ex2wmMsgPerAppointmentSavesTotal,
       "ex2wmMsgPerAppointmentSavePerSec": ex2wmMsgPerAppointmentSavePerSec,
       "ex2wmNamesCheckedTotal": ex2wmNamesCheckedTotal,
       "ex2wmNamesCheckedPerSec": ex2wmNamesCheckedPerSec,
       "ex2wmNavigationOptionsSavesTotal": ex2wmNavigationOptionsSavesTotal,
       "ex2wmNavigationOptionsSavePerSec": ex2wmNavigationOptionsSavePerSec,
       "ex2wmNewFolderTemplateDataTotal": ex2wmNewFolderTemplateDataTotal,
       "ex2wmNewFolderTemplateDataPerSec": ex2wmNewFolderTemplateDataPerSec,
       "ex2wmNewItemURLTotal": ex2wmNewItemURLTotal,
       "ex2wmNewItemURLPerSec": ex2wmNewItemURLPerSec,
       "ex2wmPostsSubmittedTotal": ex2wmPostsSubmittedTotal,
       "ex2wmPostsSubmittedPerSec": ex2wmPostsSubmittedPerSec,
       "ex2wmRecipientsEditedTotal": ex2wmRecipientsEditedTotal,
       "ex2wmRecipientsEditedPerSec": ex2wmRecipientsEditedPerSec,
       "ex2wmRecipientsSavedTotal": ex2wmRecipientsSavedTotal,
       "ex2wmRecipientsSavedPerSec": ex2wmRecipientsSavedPerSec,
       "ex2wmViewsOfCalendarsTotal": ex2wmViewsOfCalendarsTotal,
       "ex2wmViewsOfCalendarsPerSec": ex2wmViewsOfCalendarsPerSec,
       "ex2wmViewsOfMailFoldersTotal": ex2wmViewsOfMailFoldersTotal,
       "ex2wmViewsOfMailFoldersPerSec": ex2wmViewsOfMailFoldersPerSec,
       "ex2ALTable": ex2ALTable,
       "ex2ALEntry": ex2ALEntry,
       "ex2ALInstance": ex2ALInstance,
       "ex2ALActiveRPCThreads": ex2ALActiveRPCThreads,
       "ex2ALLDAPResults": ex2ALLDAPResults,
       "ex2ALLDAPResultsPerSec": ex2ALLDAPResultsPerSec,
       "ex2ALLDAPSearchCalls": ex2ALLDAPSearchCalls,
       "ex2ALLDAPSearchCallsPerSec": ex2ALLDAPSearchCallsPerSec,
       "ex2Autodiscover": ex2Autodiscover,
       "ex2adErrorResponses": ex2adErrorResponses,
       "ex2adErrorResponsesPerSec": ex2adErrorResponsesPerSec,
       "ex2adProcessID": ex2adProcessID,
       "ex2adRequestsPerSec": ex2adRequestsPerSec,
       "ex2adTotalRequests": ex2adTotalRequests,
       "ex2EdgeSyncJobTable": ex2EdgeSyncJobTable,
       "ex2EdgeSyncJobEntry": ex2EdgeSyncJobEntry,
       "ex2esjInstance": ex2esjInstance,
       "ex2esjEdgeObjectsAddedTotal": ex2esjEdgeObjectsAddedTotal,
       "ex2esjEdgeObjectsAddedPerSec": ex2esjEdgeObjectsAddedPerSec,
       "ex2esjEdgeObjectsDeletedTotal": ex2esjEdgeObjectsDeletedTotal,
       "ex2esjEdgeObjectsDeletedPerSec": ex2esjEdgeObjectsDeletedPerSec,
       "ex2esjEdgeObjectsUpdatedTotal": ex2esjEdgeObjectsUpdatedTotal,
       "ex2esjEdgeObjectsUpdatedPerSec": ex2esjEdgeObjectsUpdatedPerSec,
       "ex2esjScanJobCompletSuccessTotal": ex2esjScanJobCompletSuccessTotal,
       "ex2esjScanJobFailNotExtLockTotal": ex2esjScanJobFailNotExtLockTotal,
       "ex2esjScanJobFailDirctErrorTotal": ex2esjScanJobFailDirctErrorTotal,
       "ex2esjScanJobNotStartNotLockTotl": ex2esjScanJobNotStartNotLockTotl,
       "ex2esjScanJobsStartedTotal": ex2esjScanJobsStartedTotal,
       "ex2esjSourceObjectsScannedTotal": ex2esjSourceObjectsScannedTotal,
       "ex2esjSourceObjectsScannedPerSec": ex2esjSourceObjectsScannedPerSec,
       "ex2esjTargetObjectsScannedTotal": ex2esjTargetObjectsScannedTotal,
       "ex2esjTargetObjectsScannedPerSec": ex2esjTargetObjectsScannedPerSec,
       "ex2EdgeSyncTopology": ex2EdgeSyncTopology,
       "ex2estCompletedScansTotal": ex2estCompletedScansTotal,
       "ex2estEdgeServersLeasedTotal": ex2estEdgeServersLeasedTotal,
       "ex2estEdgeServersTotal": ex2estEdgeServersTotal,
       "ex2estExchangeServersTotal": ex2estExchangeServersTotal,
       "ex2estHubTransportServersTotal": ex2estHubTransportServersTotal,
       "ex2estJobsExecutingTotal": ex2estJobsExecutingTotal,
       "ex2estJobsSuspendingTotal": ex2estJobsSuspendingTotal,
       "ex2estJobsWaitingTotal": ex2estJobsWaitingTotal,
       "ex2estSyncNowEdgeNotCompletTotal": ex2estSyncNowEdgeNotCompletTotal,
       "ex2estSyncNowStartedTotal": ex2estSyncNowStartedTotal,
       "ex2FDSOABTable": ex2FDSOABTable,
       "ex2FDSOABEntry": ex2FDSOABEntry,
       "ex2FDSOABInstance": ex2FDSOABInstance,
       "ex2FDSOABBytesDownloaded": ex2FDSOABBytesDownloaded,
       "ex2FDSOABDownloadTaskQueued": ex2FDSOABDownloadTaskQueued,
       "ex2FDSOABDownloadTasksCompleted": ex2FDSOABDownloadTasksCompleted,
       "ex2FDSOABTotalBytesToDownload": ex2FDSOABTotalBytesToDownload,
       "ex2FDSUMTable": ex2FDSUMTable,
       "ex2FDSUMEntry": ex2FDSUMEntry,
       "ex2FDSUMInstance": ex2FDSUMInstance,
       "ex2FDSUMBytesDownloaded": ex2FDSUMBytesDownloaded,
       "ex2FDSUMDownloadTaskQueued": ex2FDSUMDownloadTaskQueued,
       "ex2FDSUMDownloadTasksCompleted": ex2FDSUMDownloadTasksCompleted,
       "ex2FDSUMTotalBytesToDownload": ex2FDSUMTotalBytesToDownload,
       "ex2InformationStore": ex2InformationStore,
       "ex2ISACLUpgradeCompletedUpgrades": ex2ISACLUpgradeCompletedUpgrades,
       "ex2ISACLUpgradeFailures": ex2ISACLUpgradeFailures,
       "ex2ISACLUpgrdHitACLUpgrdRtryList": ex2ISACLUpgrdHitACLUpgrdRtryList,
       "ex2ISACLUpgradePartialUpgrades": ex2ISACLUpgradePartialUpgrades,
       "ex2ISACLUpgradeTimesAttempted": ex2ISACLUpgradeTimesAttempted,
       "ex2ISActiveAnonymousUserCount": ex2ISActiveAnonymousUserCount,
       "ex2ISActiveConnectionCount": ex2ISActiveConnectionCount,
       "ex2ISActiveUserCount": ex2ISActiveUserCount,
       "ex2ISAdminRPCRequests": ex2ISAdminRPCRequests,
       "ex2ISAdminRPCRequestsPeak": ex2ISAdminRPCRequestsPeak,
       "ex2ISAnonymousUserCount": ex2ISAnonymousUserCount,
       "ex2ISApptmtInstanceCreationRate": ex2ISApptmtInstanceCreationRate,
       "ex2ISApptmtInstanceDeletionRate": ex2ISApptmtInstanceDeletionRate,
       "ex2ISAppointmentInstancesCreated": ex2ISAppointmentInstancesCreated,
       "ex2ISAppointmentInstancesDeleted": ex2ISAppointmentInstancesDeleted,
       "ex2ISAsyncNotificationsCacheSize": ex2ISAsyncNotificationsCacheSize,
       "ex2ISAsyncNotificatGeneratPerSec": ex2ISAsyncNotificatGeneratPerSec,
       "ex2ISAsyncRPCRequests": ex2ISAsyncRPCRequests,
       "ex2ISAsyncRPCRequestsPeak": ex2ISAsyncRPCRequestsPeak,
       "ex2ISBackgroundExpanQueueLength": ex2ISBackgroundExpanQueueLength,
       "ex2ISCIQPThreads": ex2ISCIQPThreads,
       "ex2ISClientBackgroundRPCsFailed": ex2ISClientBackgroundRPCsFailed,
       "ex2ISClientBackgroundRPCsFailSec": ex2ISClientBackgroundRPCsFailSec,
       "ex2ISClientBackgroundRPCsSucceed": ex2ISClientBackgroundRPCsSucceed,
       "ex2ISClientBgRPCSucceedPerSec": ex2ISClientBgRPCSucceedPerSec,
       "ex2ISClientForegroundRPCsFailed": ex2ISClientForegroundRPCsFailed,
       "ex2ISClientFgRPCsFailedPerSec": ex2ISClientFgRPCsFailedPerSec,
       "ex2ISClientFgRPCsSucceeded": ex2ISClientFgRPCsSucceeded,
       "ex2ISClientFgRPCsSucceededPerSec": ex2ISClientFgRPCsSucceededPerSec,
       "ex2ISClientLatencyGT10SecRPCs": ex2ISClientLatencyGT10SecRPCs,
       "ex2ISClientLatencyGT2SecRPCs": ex2ISClientLatencyGT2SecRPCs,
       "ex2ISClientLatencyGT5SecRPCs": ex2ISClientLatencyGT5SecRPCs,
       "ex2ISClientRPCsFailed": ex2ISClientRPCsFailed,
       "ex2ISClientRPCsFailedPerSec": ex2ISClientRPCsFailedPerSec,
       "ex2ISClientRPCFailedAccessDenied": ex2ISClientRPCFailedAccessDenied,
       "ex2ISClientRPCFailAccessDenySec": ex2ISClientRPCFailAccessDenySec,
       "ex2ISClientRPCFailAllOtherErrors": ex2ISClientRPCFailAllOtherErrors,
       "ex2ISClientRPCFailOtherErrorSec": ex2ISClientRPCFailOtherErrorSec,
       "ex2ISClientRPCFailCallCancelled": ex2ISClientRPCFailCallCancelled,
       "ex2ISClientRPCFailCallCancelSec": ex2ISClientRPCFailCallCancelSec,
       "ex2ISClientRPCsFailedCallFailed": ex2ISClientRPCsFailedCallFailed,
       "ex2ISClientRPCFailCallFailedSec": ex2ISClientRPCFailCallFailedSec,
       "ex2ISClientRPCFailServerTooBusy": ex2ISClientRPCFailServerTooBusy,
       "ex2ISClientRPCFailServerToBsySec": ex2ISClientRPCFailServerToBsySec,
       "ex2ISClientRPCFailServerUnavail": ex2ISClientRPCFailServerUnavail,
       "ex2ISClientRPCFailServUnavailSec": ex2ISClientRPCFailServUnavailSec,
       "ex2ISClientRPCsAttempted": ex2ISClientRPCsAttempted,
       "ex2ISClientRPCsAttemptedPerSec": ex2ISClientRPCsAttemptedPerSec,
       "ex2ISClientRPCsSucceeded": ex2ISClientRPCsSucceeded,
       "ex2ISClientRPCsSucceededPerSec": ex2ISClientRPCsSucceededPerSec,
       "ex2ISClientTotalReportedLatency": ex2ISClientTotalReportedLatency,
       "ex2ISConnectionCount": ex2ISConnectionCount,
       "ex2ISDLMembershipCacheEntryCount": ex2ISDLMembershipCacheEntryCount,
       "ex2ISDLMembershipCacheHits": ex2ISDLMembershipCacheHits,
       "ex2ISDLMembershipCacheMisses": ex2ISDLMembershipCacheMisses,
       "ex2ISDLMembershipCacheSize": ex2ISDLMembershipCacheSize,
       "ex2ISExchmemCurrentByteAllocated": ex2ISExchmemCurrentByteAllocated,
       "ex2ISExchmemCurrNumbOfVirtAlloca": ex2ISExchmemCurrNumbOfVirtAlloca,
       "ex2ISExchmemCurrVirtByteAllocate": ex2ISExchmemCurrVirtByteAllocate,
       "ex2ISExchmemMaximumByteAllocated": ex2ISExchmemMaximumByteAllocated,
       "ex2ISExchmemMaxVirtualBytAllocat": ex2ISExchmemMaxVirtualBytAllocat,
       "ex2ISExchmemNumAdditionalHeaps": ex2ISExchmemNumAdditionalHeaps,
       "ex2ISExchmemNumberOfHeaps": ex2ISExchmemNumberOfHeaps,
       "ex2ISExchmemNumHeapsMemErrors": ex2ISExchmemNumHeapsMemErrors,
       "ex2ISExchmemNumberOfMemoryErrors": ex2ISExchmemNumberOfMemoryErrors,
       "ex2ISExchmemTotalNumVirtAllocate": ex2ISExchmemTotalNumVirtAllocate,
       "ex2ISFBPublishCount": ex2ISFBPublishCount,
       "ex2ISFBPublishRate": ex2ISFBPublishRate,
       "ex2ISMaximumAnonymousUsers": ex2ISMaximumAnonymousUsers,
       "ex2ISMaximumConnections": ex2ISMaximumConnections,
       "ex2ISMaximumUsers": ex2ISMaximumUsers,
       "ex2ISOABDifferentialDnldAttempts": ex2ISOABDifferentialDnldAttempts,
       "ex2ISOABDifferentialDnldBytes": ex2ISOABDifferentialDnldBytes,
       "ex2ISOABDifferentialDnldBytesSec": ex2ISOABDifferentialDnldBytesSec,
       "ex2ISOABFullDownloadAttempts": ex2ISOABFullDownloadAttempts,
       "ex2ISOABFullDnldAttemptsBlocked": ex2ISOABFullDnldAttemptsBlocked,
       "ex2ISOABFullDownloadBytes": ex2ISOABFullDownloadBytes,
       "ex2ISOABFullDownloadBytesPerSec": ex2ISOABFullDownloadBytesPerSec,
       "ex2ISPeakAsyncNotificaCacheSize": ex2ISPeakAsyncNotificaCacheSize,
       "ex2ISPeakPushNotificatCacheSize": ex2ISPeakPushNotificatCacheSize,
       "ex2ISPushNotificationsCacheSize": ex2ISPushNotificationsCacheSize,
       "ex2ISPushNotificatGeneratePerSec": ex2ISPushNotificatGeneratePerSec,
       "ex2ISPushNotificationsSkipPerSec": ex2ISPushNotificationsSkipPerSec,
       "ex2ISRPCAveragedLatency": ex2ISRPCAveragedLatency,
       "ex2ISRPCClientBackoffPerSec": ex2ISRPCClientBackoffPerSec,
       "ex2ISRPCClientsBytesRead": ex2ISRPCClientsBytesRead,
       "ex2ISRPCClientsBytesWritten": ex2ISRPCClientsBytesWritten,
       "ex2ISRPCClientsUncomprsdByteRead": ex2ISRPCClientsUncomprsdByteRead,
       "ex2ISRPCClientUncomprsdByteWrite": ex2ISRPCClientUncomprsdByteWrite,
       "ex2ISRPCNumOfSlowPackets": ex2ISRPCNumOfSlowPackets,
       "ex2ISRPCOperationsPerSec": ex2ISRPCOperationsPerSec,
       "ex2ISRPCPacketsPerSec": ex2ISRPCPacketsPerSec,
       "ex2ISRPCRequests": ex2ISRPCRequests,
       "ex2ISRPCRequestsPeak": ex2ISRPCRequestsPeak,
       "ex2ISReadBytesRPCClientsPerSec": ex2ISReadBytesRPCClientsPerSec,
       "ex2ISRecurringApptmtDeletionRate": ex2ISRecurringApptmtDeletionRate,
       "ex2ISRecurApptmtModificationRate": ex2ISRecurApptmtModificationRate,
       "ex2ISRecurringApptmtsCreated": ex2ISRecurringApptmtsCreated,
       "ex2ISRecurringApptmtsDeleted": ex2ISRecurringApptmtsDeleted,
       "ex2ISRecurringApptmtsModified": ex2ISRecurringApptmtsModified,
       "ex2ISRecurringApptmtCreationRate": ex2ISRecurringApptmtCreationRate,
       "ex2ISRecurringMstrApptmtExpanded": ex2ISRecurringMstrApptmtExpanded,
       "ex2ISRecurringMasterExpansionRat": ex2ISRecurringMasterExpansionRat,
       "ex2ISSingleApptmtCreationRate": ex2ISSingleApptmtCreationRate,
       "ex2ISSingleApptmtDeletionRate": ex2ISSingleApptmtDeletionRate,
       "ex2ISSingleApptmtModificationRat": ex2ISSingleApptmtModificationRat,
       "ex2ISSingleAppointmentsCreated": ex2ISSingleAppointmentsCreated,
       "ex2ISSingleAppointmentsDeleted": ex2ISSingleAppointmentsDeleted,
       "ex2ISSingleAppointmentsModified": ex2ISSingleAppointmentsModified,
       "ex2ISSlowQPThreads": ex2ISSlowQPThreads,
       "ex2ISSlowSearchThreads": ex2ISSlowSearchThreads,
       "ex2ISTotalParkedAsyncNotifiCalls": ex2ISTotalParkedAsyncNotifiCalls,
       "ex2ISUserCount": ex2ISUserCount,
       "ex2ISVMLargestBlockSize": ex2ISVMLargestBlockSize,
       "ex2ISVMTotal16MBFreeBlocks": ex2ISVMTotal16MBFreeBlocks,
       "ex2ISVMTotalFreeBlocks": ex2ISVMTotalFreeBlocks,
       "ex2ISVMTotalLargeFreeBlockBytes": ex2ISVMTotalLargeFreeBlockBytes,
       "ex2ISVirusScanBytesScanned": ex2ISVirusScanBytesScanned,
       "ex2ISVirusScanFilesCleaned": ex2ISVirusScanFilesCleaned,
       "ex2ISVirusScanFilesCleanedPerSec": ex2ISVirusScanFilesCleanedPerSec,
       "ex2ISVirusScanFilesQuarantined": ex2ISVirusScanFilesQuarantined,
       "ex2ISVirusScanFileQuarantinePSec": ex2ISVirusScanFileQuarantinePSec,
       "ex2ISVirusScanFilesScanned": ex2ISVirusScanFilesScanned,
       "ex2ISVirusScanFilesScannedPerSec": ex2ISVirusScanFilesScannedPerSec,
       "ex2ISVirusScanFoldersScannedInBg": ex2ISVirusScanFoldersScannedInBg,
       "ex2ISVirusScanMessagesCleaned": ex2ISVirusScanMessagesCleaned,
       "ex2ISVirusScanMsgsCleanedPerSec": ex2ISVirusScanMsgsCleanedPerSec,
       "ex2ISVirusScanMessagesDeleted": ex2ISVirusScanMessagesDeleted,
       "ex2ISVirusScanMsgsDeletedPerSec": ex2ISVirusScanMsgsDeletedPerSec,
       "ex2ISVirusScanMessagesProcessed": ex2ISVirusScanMessagesProcessed,
       "ex2ISVirusScanMsgProcessedPerSec": ex2ISVirusScanMsgProcessedPerSec,
       "ex2ISVirusScanMsgsQuarantined": ex2ISVirusScanMsgsQuarantined,
       "ex2ISVirusScanMsgQuarantinPerSec": ex2ISVirusScanMsgQuarantinPerSec,
       "ex2ISVirusScanMsgsScanBackground": ex2ISVirusScanMsgsScanBackground,
       "ex2ISVirusScanQueueLength": ex2ISVirusScanQueueLength,
       "ex2ISWriteBytesRPCClientsPerSec": ex2ISWriteBytesRPCClientsPerSec,
       "ex2ISClientTable": ex2ISClientTable,
       "ex2ISClientEntry": ex2ISClientEntry,
       "ex2ISCInstance": ex2ISCInstance,
       "ex2ISCDirAccCacheEntryAddPerSec": ex2ISCDirAccCacheEntryAddPerSec,
       "ex2ISCDirAccCacheEntryExpiredSec": ex2ISCDirAccCacheEntryExpiredSec,
       "ex2ISCDirAccCacheHitsPercent": ex2ISCDirAccCacheHitsPercent,
       "ex2ISCDirAccLDAPReadsPerSec": ex2ISCDirAccLDAPReadsPerSec,
       "ex2ISCDirAccLDAPSearchesPerSec": ex2ISCDirAccLDAPSearchesPerSec,
       "ex2ISCJETLogRecordBytesPerSec": ex2ISCJETLogRecordBytesPerSec,
       "ex2ISCJETLogRecordsPerSec": ex2ISCJETLogRecordsPerSec,
       "ex2ISCJETPagesModifiedPerSec": ex2ISCJETPagesModifiedPerSec,
       "ex2ISCJETPagesPrereadPerSec": ex2ISCJETPagesPrereadPerSec,
       "ex2ISCJETPagesReadPerSec": ex2ISCJETPagesReadPerSec,
       "ex2ISCJETPagesReferencedPerSec": ex2ISCJETPagesReferencedPerSec,
       "ex2ISCJETPagesRemodifiedPerSec": ex2ISCJETPagesRemodifiedPerSec,
       "ex2ISCRPCAverageLatency": ex2ISCRPCAverageLatency,
       "ex2ISCRPCBytesReceivedPerSec": ex2ISCRPCBytesReceivedPerSec,
       "ex2ISCRPCBytesSentPerSec": ex2ISCRPCBytesSentPerSec,
       "ex2ISCRPCOperationsPerSec": ex2ISCRPCOperationsPerSec,
       "ex2ISCRPCPacketsPerSec": ex2ISCRPCPacketsPerSec,
       "ex2ISMailboxTable": ex2ISMailboxTable,
       "ex2ISMailboxEntry": ex2ISMailboxEntry,
       "ex2mbInstance": ex2mbInstance,
       "ex2mbActiveClientLogons": ex2mbActiveClientLogons,
       "ex2mbAverageDeliveryTime": ex2mbAverageDeliveryTime,
       "ex2mbCategorizationCount": ex2mbCategorizationCount,
       "ex2mbClientLogons": ex2mbClientLogons,
       "ex2mbEventHistoryDeletes": ex2mbEventHistoryDeletes,
       "ex2mbEventHistoryDeletesPerSec": ex2mbEventHistoryDeletesPerSec,
       "ex2mbEventHistEventCacheHitsPerc": ex2mbEventHistEventCacheHitsPerc,
       "ex2mbEventHistoryEventsCount": ex2mbEventHistoryEventsCount,
       "ex2mbEventHistEventEmptyConClass": ex2mbEventHistEventEmptyConClass,
       "ex2mbEventHistEventEmptyMsgClass": ex2mbEventHistEventEmptyMsgClass,
       "ex2mbEventHistEventsTrunConClass": ex2mbEventHistEventsTrunConClass,
       "ex2mbEventHistEventsTrunMsgClass": ex2mbEventHistEventsTrunMsgClass,
       "ex2mbEventHistoryReads": ex2mbEventHistoryReads,
       "ex2mbEventHistoryReadsPerSec": ex2mbEventHistoryReadsPerSec,
       "ex2mbEventHistUncommitTransCount": ex2mbEventHistUncommitTransCount,
       "ex2mbEventHistoryWatermarksCount": ex2mbEventHistoryWatermarksCount,
       "ex2mbEventHistWatermarksDeletes": ex2mbEventHistWatermarksDeletes,
       "ex2mbEventHistWatermarkDelPerSec": ex2mbEventHistWatermarkDelPerSec,
       "ex2mbEventHistoryWatermarksReads": ex2mbEventHistoryWatermarksReads,
       "ex2mbEventHistWatermarkReadPrSec": ex2mbEventHistWatermarkReadPrSec,
       "ex2mbEventHistWatermarksWrites": ex2mbEventHistWatermarksWrites,
       "ex2mbEventHistWatermarkWritPrSec": ex2mbEventHistWatermarkWritPrSec,
       "ex2mbEventHistoryWrites": ex2mbEventHistoryWrites,
       "ex2mbEventHistoryWritesPerSec": ex2mbEventHistoryWritesPerSec,
       "ex2mbFolderOpensPerSec": ex2mbFolderOpensPerSec,
       "ex2mbHTTPPerDAVCurrentPendNotif": ex2mbHTTPPerDAVCurrentPendNotif,
       "ex2mbHTTPPerDAVCurrentSubscript": ex2mbHTTPPerDAVCurrentSubscript,
       "ex2mbHTTPPerDAVCurrentTransLocks": ex2mbHTTPPerDAVCurrentTransLocks,
       "ex2mbHTTPPerDAVNotifyRequestPSec": ex2mbHTTPPerDAVNotifyRequestPSec,
       "ex2mbHTTPPerDAVTotalLocksCreated": ex2mbHTTPPerDAVTotalLocksCreated,
       "ex2mbHTTPPerDAVTotalNotifyRequst": ex2mbHTTPPerDAVTotalNotifyRequst,
       "ex2mbHTTPPerDAVTotalSubscCreated": ex2mbHTTPPerDAVTotalSubscCreated,
       "ex2mbHTTPPerDAVTotalSubscExpired": ex2mbHTTPPerDAVTotalSubscExpired,
       "ex2mbLocalDeliveries": ex2mbLocalDeliveries,
       "ex2mbLocalDeliveryRate": ex2mbLocalDeliveryRate,
       "ex2mbLogonOperationsPerSec": ex2mbLogonOperationsPerSec,
       "ex2mbMessageOpensPerSec": ex2mbMessageOpensPerSec,
       "ex2mbMessageRecipientsDelivered": ex2mbMessageRecipientsDelivered,
       "ex2mbMessageRecipientDelivPerSec": ex2mbMessageRecipientDelivPerSec,
       "ex2mbMessagesDelivered": ex2mbMessagesDelivered,
       "ex2mbMessagesDeliveredPerSec": ex2mbMessagesDeliveredPerSec,
       "ex2mbMessagesQueuedForSubmission": ex2mbMessagesQueuedForSubmission,
       "ex2mbMessagesSent": ex2mbMessagesSent,
       "ex2mbMessagesSentPerSec": ex2mbMessagesSentPerSec,
       "ex2mbMessagesSubmitted": ex2mbMessagesSubmitted,
       "ex2mbMessagesSubmittedPerSec": ex2mbMessagesSubmittedPerSec,
       "ex2mbPeakClientLogons": ex2mbPeakClientLogons,
       "ex2mbReceiveQueueSize": ex2mbReceiveQueueSize,
       "ex2mbReplIDCount": ex2mbReplIDCount,
       "ex2mbRestrictedViewCacheHitRate": ex2mbRestrictedViewCacheHitRate,
       "ex2mbRestrictedViewCacheMissRate": ex2mbRestrictedViewCacheMissRate,
       "ex2mbSearchTaskRate": ex2mbSearchTaskRate,
       "ex2mbSingleInstanceRatio": ex2mbSingleInstanceRatio,
       "ex2mbSlowFindRowRate": ex2mbSlowFindRowRate,
       "ex2mbTotalCountOfRecoverableItem": ex2mbTotalCountOfRecoverableItem,
       "ex2mbTotalSizeOfRecoverableItems": ex2mbTotalSizeOfRecoverableItems,
       "ex2mbVirusScanBackgrndScanThread": ex2mbVirusScanBackgrndScanThread,
       "ex2mbVirusScanBackgrndMsgScanned": ex2mbVirusScanBackgrndMsgScanned,
       "ex2mbVirusScanBackgrndMsgSkipped": ex2mbVirusScanBackgrndMsgSkipped,
       "ex2mbVirusScanBackgrndMsgUpDate": ex2mbVirusScanBackgrndMsgUpDate,
       "ex2mbVirusScanExtRsltsAccepted": ex2mbVirusScanExtRsltsAccepted,
       "ex2mbVirusScanExtRsltNotAccepted": ex2mbVirusScanExtRsltNotAccepted,
       "ex2mbVirusScanExtRsltsNotPresent": ex2mbVirusScanExtRsltsNotPresent,
       "ex2ISPublicTable": ex2ISPublicTable,
       "ex2ISPublicEntry": ex2ISPublicEntry,
       "ex2ispInstance": ex2ispInstance,
       "ex2ispActiveClientLogons": ex2ispActiveClientLogons,
       "ex2ispAverageDeliveryTime": ex2ispAverageDeliveryTime,
       "ex2ispCategorizationCount": ex2ispCategorizationCount,
       "ex2ispClientLogons": ex2ispClientLogons,
       "ex2ispEventHistoryDeletes": ex2ispEventHistoryDeletes,
       "ex2ispEventHistoryDeletesPerSec": ex2ispEventHistoryDeletesPerSec,
       "ex2ispEventHistEventCacheHitPerc": ex2ispEventHistEventCacheHitPerc,
       "ex2ispEventHistoryEventsCount": ex2ispEventHistoryEventsCount,
       "ex2ispEventHistEvntEmptyCntClass": ex2ispEventHistEvntEmptyCntClass,
       "ex2ispEventHisEventEmptyMsgClass": ex2ispEventHisEventEmptyMsgClass,
       "ex2ispEventHistEventTrunConClass": ex2ispEventHistEventTrunConClass,
       "ex2ispEventHistEventTrunMsgClass": ex2ispEventHistEventTrunMsgClass,
       "ex2ispEventHistoryReads": ex2ispEventHistoryReads,
       "ex2ispEventHistoryReadsPerSec": ex2ispEventHistoryReadsPerSec,
       "ex2ispEventHistUncommitTranCount": ex2ispEventHistUncommitTranCount,
       "ex2ispEventHistWatermarksCount": ex2ispEventHistWatermarksCount,
       "ex2ispEventHistWatermarksDeletes": ex2ispEventHistWatermarksDeletes,
       "ex2ispEventHistWatermarkDelPrSec": ex2ispEventHistWatermarkDelPrSec,
       "ex2ispEventHistWatermarksReads": ex2ispEventHistWatermarksReads,
       "ex2ispEventHistWatermarkRdPerSec": ex2ispEventHistWatermarkRdPerSec,
       "ex2ispEventHistWatermarksWrites": ex2ispEventHistWatermarksWrites,
       "ex2ispEventHistWatermarkWriteSec": ex2ispEventHistWatermarkWriteSec,
       "ex2ispEventHistoryWrites": ex2ispEventHistoryWrites,
       "ex2ispEventHistoryWritesPerSec": ex2ispEventHistoryWritesPerSec,
       "ex2ispFolderOpensPerSec": ex2ispFolderOpensPerSec,
       "ex2ispHTTPPerDAVCurrentPendNotif": ex2ispHTTPPerDAVCurrentPendNotif,
       "ex2ispHTTPPerDAVCurrentSubscript": ex2ispHTTPPerDAVCurrentSubscript,
       "ex2ispHTTPPerDAVCurrentTransLock": ex2ispHTTPPerDAVCurrentTransLock,
       "ex2ispHTTPPerDAVNotifyReqPerSec": ex2ispHTTPPerDAVNotifyReqPerSec,
       "ex2ispHTTPPerDAVTotalLockCreated": ex2ispHTTPPerDAVTotalLockCreated,
       "ex2ispHTTPPerDAVTotalNotifyReqst": ex2ispHTTPPerDAVTotalNotifyReqst,
       "ex2ispHTTPPerDAVTotalSubsCreated": ex2ispHTTPPerDAVTotalSubsCreated,
       "ex2ispHTTPPerDAVTotalSubsExpired": ex2ispHTTPPerDAVTotalSubsExpired,
       "ex2ispLogonOperationsPerSec": ex2ispLogonOperationsPerSec,
       "ex2ispMessageOpensPerSec": ex2ispMessageOpensPerSec,
       "ex2ispMessageRecipientsDelivered": ex2ispMessageRecipientsDelivered,
       "ex2ispMsgRecipientsDeliverPerSec": ex2ispMsgRecipientsDeliverPerSec,
       "ex2ispMessagesDelivered": ex2ispMessagesDelivered,
       "ex2ispMessagesDeliveredPerSec": ex2ispMessagesDeliveredPerSec,
       "ex2ispMsgsQueuedForSubmission": ex2ispMsgsQueuedForSubmission,
       "ex2ispMessagesSent": ex2ispMessagesSent,
       "ex2ispMessagesSentPerSec": ex2ispMessagesSentPerSec,
       "ex2ispMessagesSubmitted": ex2ispMessagesSubmitted,
       "ex2ispMessagesSubmittedPerSec": ex2ispMessagesSubmittedPerSec,
       "ex2ispNumMsgsExpireFrmPublicFold": ex2ispNumMsgsExpireFrmPublicFold,
       "ex2ispPeakClientLogons": ex2ispPeakClientLogons,
       "ex2ispReceiveQueueSize": ex2ispReceiveQueueSize,
       "ex2ispReplIDCount": ex2ispReplIDCount,
       "ex2ispReplicBackfillDataMsgsRecv": ex2ispReplicBackfillDataMsgsRecv,
       "ex2ispReplicBackfillDataMsgsSent": ex2ispReplicBackfillDataMsgsSent,
       "ex2ispReplicBackfillRequestRecvd": ex2ispReplicBackfillRequestRecvd,
       "ex2ispReplicBackfillRequestsSent": ex2ispReplicBackfillRequestsSent,
       "ex2ispReplicFolderChangeReceived": ex2ispReplicFolderChangeReceived,
       "ex2ispReplicFolderChangesSent": ex2ispReplicFolderChangesSent,
       "ex2ispReplicFolderDataMsgReceive": ex2ispReplicFolderDataMsgReceive,
       "ex2ispReplicFolderDataMsgsSent": ex2ispReplicFolderDataMsgsSent,
       "ex2ispReplicFolderTreeMsgReceive": ex2ispReplicFolderTreeMsgReceive,
       "ex2ispReplicFolderTreeMsgsSent": ex2ispReplicFolderTreeMsgsSent,
       "ex2ispReplicMessageChangeReceive": ex2ispReplicMessageChangeReceive,
       "ex2ispReplicMessageChangesSent": ex2ispReplicMessageChangesSent,
       "ex2ispReplicMsgsReceived": ex2ispReplicMsgsReceived,
       "ex2ispReplicationMessagesSent": ex2ispReplicationMessagesSent,
       "ex2ispReplicReceiveQueueSize": ex2ispReplicReceiveQueueSize,
       "ex2ispReplicStatusMsgsReceived": ex2ispReplicStatusMsgsReceived,
       "ex2ispReplicStatusMsgsSent": ex2ispReplicStatusMsgsSent,
       "ex2ispRestrictedViewCacheHitRate": ex2ispRestrictedViewCacheHitRate,
       "ex2ispRestricteViewCacheMissRate": ex2ispRestricteViewCacheMissRate,
       "ex2ispSearchTaskRate": ex2ispSearchTaskRate,
       "ex2ispSingleInstanceRatio": ex2ispSingleInstanceRatio,
       "ex2ispSlowFindRowRate": ex2ispSlowFindRowRate,
       "ex2ispTotalCountRecoverableItems": ex2ispTotalCountRecoverableItems,
       "ex2ispTotalSizeOfRecoverableItem": ex2ispTotalSizeOfRecoverableItem,
       "ex2ispVirusScanBackgrndScnThread": ex2ispVirusScanBackgrndScnThread,
       "ex2ispVirusScanBackgrndMsgsScan": ex2ispVirusScanBackgrndMsgsScan,
       "ex2ispVirusScanBackgrndMsgSkippd": ex2ispVirusScanBackgrndMsgSkippd,
       "ex2ispVirusScanBackgrndMsgUpDate": ex2ispVirusScanBackgrndMsgUpDate,
       "ex2ispVirusScanExtResultAccepted": ex2ispVirusScanExtResultAccepted,
       "ex2ispVirusScanExtResultNotAccpt": ex2ispVirusScanExtResultNotAccpt,
       "ex2ispVirusScanExtResultsNotPres": ex2ispVirusScanExtResultsNotPres,
       "ex2Imap4Table": ex2Imap4Table,
       "ex2Imap4Entry": ex2Imap4Entry,
       "ex2im4Instance": ex2im4Instance,
       "ex2im4ActiveSSLConnections": ex2im4ActiveSSLConnections,
       "ex2im4AppendFailures": ex2im4AppendFailures,
       "ex2im4AppendRate": ex2im4AppendRate,
       "ex2im4AppendTotal": ex2im4AppendTotal,
       "ex2im4AuthenticateFailures": ex2im4AuthenticateFailures,
       "ex2im4AuthenticateRate": ex2im4AuthenticateRate,
       "ex2im4AuthenticateTotal": ex2im4AuthenticateTotal,
       "ex2im4AvgCommProcessTimeMillisec": ex2im4AvgCommProcessTimeMillisec,
       "ex2im4CapabilityFailures": ex2im4CapabilityFailures,
       "ex2im4CapabilityRate": ex2im4CapabilityRate,
       "ex2im4CapabilityTotal": ex2im4CapabilityTotal,
       "ex2im4CheckFailures": ex2im4CheckFailures,
       "ex2im4CheckRate": ex2im4CheckRate,
       "ex2im4CheckTotal": ex2im4CheckTotal,
       "ex2im4CloseFailures": ex2im4CloseFailures,
       "ex2im4CloseRate": ex2im4CloseRate,
       "ex2im4CloseTotal": ex2im4CloseTotal,
       "ex2im4ConnectionsFailed": ex2im4ConnectionsFailed,
       "ex2im4ConnectionsRejected": ex2im4ConnectionsRejected,
       "ex2im4CopyFailures": ex2im4CopyFailures,
       "ex2im4CopyRate": ex2im4CopyRate,
       "ex2im4CopyTotal": ex2im4CopyTotal,
       "ex2im4CreateFailures": ex2im4CreateFailures,
       "ex2im4CreateRate": ex2im4CreateRate,
       "ex2im4CreateTotal": ex2im4CreateTotal,
       "ex2im4CurrentConnections": ex2im4CurrentConnections,
       "ex2im4DeleteFailures": ex2im4DeleteFailures,
       "ex2im4DeleteRate": ex2im4DeleteRate,
       "ex2im4DeleteTotal": ex2im4DeleteTotal,
       "ex2im4ExamineFailures": ex2im4ExamineFailures,
       "ex2im4ExamineRate": ex2im4ExamineRate,
       "ex2im4ExamineTotal": ex2im4ExamineTotal,
       "ex2im4ExpungeFailures": ex2im4ExpungeFailures,
       "ex2im4ExpungeRate": ex2im4ExpungeRate,
       "ex2im4ExpungeTotal": ex2im4ExpungeTotal,
       "ex2im4FetchFailures": ex2im4FetchFailures,
       "ex2im4FetchRate": ex2im4FetchRate,
       "ex2im4FetchTotal": ex2im4FetchTotal,
       "ex2im4IdleFailures": ex2im4IdleFailures,
       "ex2im4IdleRate": ex2im4IdleRate,
       "ex2im4IdleTotal": ex2im4IdleTotal,
       "ex2im4InvalidCommands": ex2im4InvalidCommands,
       "ex2im4InvalidCommandsRate": ex2im4InvalidCommandsRate,
       "ex2im4LSUBFailures": ex2im4LSUBFailures,
       "ex2im4LSUBRate": ex2im4LSUBRate,
       "ex2im4LSUBTotal": ex2im4LSUBTotal,
       "ex2im4ListFailures": ex2im4ListFailures,
       "ex2im4ListRate": ex2im4ListRate,
       "ex2im4ListTotal": ex2im4ListTotal,
       "ex2im4LoginFailures": ex2im4LoginFailures,
       "ex2im4LoginRate": ex2im4LoginRate,
       "ex2im4LoginTotal": ex2im4LoginTotal,
       "ex2im4LogoutFailures": ex2im4LogoutFailures,
       "ex2im4LogoutRate": ex2im4LogoutRate,
       "ex2im4LogoutTotal": ex2im4LogoutTotal,
       "ex2im4NOOPFailures": ex2im4NOOPFailures,
       "ex2im4NOOPRate": ex2im4NOOPRate,
       "ex2im4NOOPTotal": ex2im4NOOPTotal,
       "ex2im4NamespaceFailures": ex2im4NamespaceFailures,
       "ex2im4NamespaceRate": ex2im4NamespaceRate,
       "ex2im4NamespaceTotal": ex2im4NamespaceTotal,
       "ex2im4RenameFailures": ex2im4RenameFailures,
       "ex2im4RenameRate": ex2im4RenameRate,
       "ex2im4RenameTotal": ex2im4RenameTotal,
       "ex2im4SSLConnections": ex2im4SSLConnections,
       "ex2im4STARTTLSFailures": ex2im4STARTTLSFailures,
       "ex2im4STARTTLSRate": ex2im4STARTTLSRate,
       "ex2im4STARTTLSTotal": ex2im4STARTTLSTotal,
       "ex2im4SearchFailures": ex2im4SearchFailures,
       "ex2im4SearchRate": ex2im4SearchRate,
       "ex2im4SearchTotal": ex2im4SearchTotal,
       "ex2im4SelectFailures": ex2im4SelectFailures,
       "ex2im4SelectRate": ex2im4SelectRate,
       "ex2im4SelectTotal": ex2im4SelectTotal,
       "ex2im4StatusFailures": ex2im4StatusFailures,
       "ex2im4StatusRate": ex2im4StatusRate,
       "ex2im4StatusTotal": ex2im4StatusTotal,
       "ex2im4StoreFailures": ex2im4StoreFailures,
       "ex2im4StoreRate": ex2im4StoreRate,
       "ex2im4StoreTotal": ex2im4StoreTotal,
       "ex2im4SubscribeFailures": ex2im4SubscribeFailures,
       "ex2im4SubscribeRate": ex2im4SubscribeRate,
       "ex2im4SubscribeTotal": ex2im4SubscribeTotal,
       "ex2im4TotalConnections": ex2im4TotalConnections,
       "ex2im4UnsubscribeFailures": ex2im4UnsubscribeFailures,
       "ex2im4UnsubscribeRate": ex2im4UnsubscribeRate,
       "ex2im4UnsubscribeTotal": ex2im4UnsubscribeTotal,
       "ex2MailSubmissionTable": ex2MailSubmissionTable,
       "ex2MailSubmissionEntry": ex2MailSubmissionEntry,
       "ex2msInstance": ex2msInstance,
       "ex2msFailedSubmissions": ex2msFailedSubmissions,
       "ex2msFailedSubmissionsPerSecond": ex2msFailedSubmissionsPerSecond,
       "ex2msHubServers": ex2msHubServers,
       "ex2msHubServersInRetry": ex2msHubServersInRetry,
       "ex2msSuccessfulSubmissions": ex2msSuccessfulSubmissions,
       "ex2msSuccessfulSubmsPerSecond": ex2msSuccessfulSubmsPerSecond,
       "ex2msTemporarySubmissionFailures": ex2msTemporarySubmissionFailures,
       "ex2msTemporarySubmFailuresPerSec": ex2msTemporarySubmFailuresPerSec,
       "ex2Pop3Table": ex2Pop3Table,
       "ex2Pop3Entry": ex2Pop3Entry,
       "ex2p3Instance": ex2p3Instance,
       "ex2p3AUTHFailures": ex2p3AUTHFailures,
       "ex2p3AUTHRate": ex2p3AUTHRate,
       "ex2p3AUTHTotal": ex2p3AUTHTotal,
       "ex2p3ActiveSSLConnections": ex2p3ActiveSSLConnections,
       "ex2p3AvgComndProcessTimeMillisec": ex2p3AvgComndProcessTimeMillisec,
       "ex2p3CAPAFailures": ex2p3CAPAFailures,
       "ex2p3CAPARate": ex2p3CAPARate,
       "ex2p3CAPATotal": ex2p3CAPATotal,
       "ex2p3ConnectionsCurrent": ex2p3ConnectionsCurrent,
       "ex2p3ConnectionsFailed": ex2p3ConnectionsFailed,
       "ex2p3ConnectionsRejected": ex2p3ConnectionsRejected,
       "ex2p3ConnectionsTotal": ex2p3ConnectionsTotal,
       "ex2p3DELEFailures": ex2p3DELEFailures,
       "ex2p3DELERate": ex2p3DELERate,
       "ex2p3DELETotal": ex2p3DELETotal,
       "ex2p3InvalidCommands": ex2p3InvalidCommands,
       "ex2p3InvalidCommandsRate": ex2p3InvalidCommandsRate,
       "ex2p3LISTFailures": ex2p3LISTFailures,
       "ex2p3LISTRate": ex2p3LISTRate,
       "ex2p3LISTTotal": ex2p3LISTTotal,
       "ex2p3NOOPFailures": ex2p3NOOPFailures,
       "ex2p3NOOPRate": ex2p3NOOPRate,
       "ex2p3NOOPTotal": ex2p3NOOPTotal,
       "ex2p3PASSFailures": ex2p3PASSFailures,
       "ex2p3PASSRate": ex2p3PASSRate,
       "ex2p3PASSTotal": ex2p3PASSTotal,
       "ex2p3QUITFailures": ex2p3QUITFailures,
       "ex2p3QUITRate": ex2p3QUITRate,
       "ex2p3QUITTotal": ex2p3QUITTotal,
       "ex2p3RETRFailures": ex2p3RETRFailures,
       "ex2p3RETRRate": ex2p3RETRRate,
       "ex2p3RETRTotal": ex2p3RETRTotal,
       "ex2p3RSETFailures": ex2p3RSETFailures,
       "ex2p3RSETRate": ex2p3RSETRate,
       "ex2p3RSETTotal": ex2p3RSETTotal,
       "ex2p3SSLConnections": ex2p3SSLConnections,
       "ex2p3STATFailures": ex2p3STATFailures,
       "ex2p3STATRate": ex2p3STATRate,
       "ex2p3STATTotal": ex2p3STATTotal,
       "ex2p3STLSFailures": ex2p3STLSFailures,
       "ex2p3STLSRate": ex2p3STLSRate,
       "ex2p3STLSTotal": ex2p3STLSTotal,
       "ex2p3TOPFailures": ex2p3TOPFailures,
       "ex2p3TOPRate": ex2p3TOPRate,
       "ex2p3TOPTotal": ex2p3TOPTotal,
       "ex2p3UIDLFailures": ex2p3UIDLFailures,
       "ex2p3UIDLRate": ex2p3UIDLRate,
       "ex2p3UIDLTotal": ex2p3UIDLTotal,
       "ex2p3USERFailures": ex2p3USERFailures,
       "ex2p3USERRate": ex2p3USERRate,
       "ex2p3USERTotal": ex2p3USERTotal,
       "ex2SANSPIProxy": ex2SANSPIProxy,
       "ex2SANSPIPBytesTransmittedPerSec": ex2SANSPIPBytesTransmittedPerSec,
       "ex2SANSPIPClientConnectionCount": ex2SANSPIPClientConnectionCount,
       "ex2SANSPIPClientConnectionPerSec": ex2SANSPIPClientConnectionPerSec,
       "ex2SANSPIPClientDisconnectPerSec": ex2SANSPIPClientDisconnectPerSec,
       "ex2SANSPIPClientReferrals": ex2SANSPIPClientReferrals,
       "ex2SANSPIPClientReferralsPerSec": ex2SANSPIPClientReferralsPerSec,
       "ex2SANSPIPCumulatClientConnCount": ex2SANSPIPCumulatClientConnCount,
       "ex2SANSPIPFailedClientConnPerSec": ex2SANSPIPFailedClientConnPerSec,
       "ex2SANSPIPFailedReadsPerSec": ex2SANSPIPFailedReadsPerSec,
       "ex2SANSPIPFailedServerConnPerSec": ex2SANSPIPFailedServerConnPerSec,
       "ex2SANSPIPFailedWritesPerSec": ex2SANSPIPFailedWritesPerSec,
       "ex2SANSPIPPacketsTransmittPerSec": ex2SANSPIPPacketsTransmittPerSec,
       "ex2SANSPIPPeakClientConnections": ex2SANSPIPPeakClientConnections,
       "ex2SANSPIPPeakWorkerThreads": ex2SANSPIPPeakWorkerThreads,
       "ex2SANSPIPTotalFailedClientConns": ex2SANSPIPTotalFailedClientConns,
       "ex2SANSPIPTotalFailedReads": ex2SANSPIPTotalFailedReads,
       "ex2SANSPIPTotalFailedServerConns": ex2SANSPIPTotalFailedServerConns,
       "ex2SANSPIPTotalFailedWrites": ex2SANSPIPTotalFailedWrites,
       "ex2SANSPIPWorkerThreadsInUse": ex2SANSPIPWorkerThreadsInUse,
       "ex2TransportBatchPointTable": ex2TransportBatchPointTable,
       "ex2TransportBatchPointEntry": ex2TransportBatchPointEntry,
       "ex2tbpInstance": ex2tbpInstance,
       "ex2tbpBatchSizeExecutedTotal": ex2tbpBatchSizeExecutedTotal,
       "ex2tbpBatchSizeExecutedPerSec": ex2tbpBatchSizeExecutedPerSec,
       "ex2tbpBatchesExecBackgroundTotal": ex2tbpBatchesExecBackgroundTotal,
       "ex2tbpBatchesExecBackgroundPrSec": ex2tbpBatchesExecBackgroundPrSec,
       "ex2tbpBatchesExecutedNormalTotal": ex2tbpBatchesExecutedNormalTotal,
       "ex2tbpBatcheExecutedNormalPerSec": ex2tbpBatcheExecutedNormalPerSec,
       "ex2tbpBatchesExecutedTotal": ex2tbpBatchesExecutedTotal,
       "ex2tbpBatchesExecutedPerSec": ex2tbpBatchesExecutedPerSec,
       "ex2tbpBatchesPendingTotal": ex2tbpBatchesPendingTotal,
       "ex2tbpBatchesPendingPerSec": ex2tbpBatchesPendingPerSec,
       "ex2tbpBatchesTimedOutTotal": ex2tbpBatchesTimedOutTotal,
       "ex2tbpBatchesTimedOutPerSec": ex2tbpBatchesTimedOutPerSec,
       "ex2tbpBatchesWaitingCurrent": ex2tbpBatchesWaitingCurrent,
       "ex2tbpBatchesWaitingTotal": ex2tbpBatchesWaitingTotal,
       "ex2tbpBatchesWaitingPerSec": ex2tbpBatchesWaitingPerSec,
       "ex2tbpCursorsClosedTotal": ex2tbpCursorsClosedTotal,
       "ex2tbpCursorsClosedPerSec": ex2tbpCursorsClosedPerSec,
       "ex2tbpCursorsOpenedTotal": ex2tbpCursorsOpenedTotal,
       "ex2tbpCursorsOpenedPerSec": ex2tbpCursorsOpenedPerSec,
       "ex2tbpDatabaseConnectionsCurrent": ex2tbpDatabaseConnectionsCurrent,
       "ex2tbpDatabaseConnsRejectedTotal": ex2tbpDatabaseConnsRejectedTotal,
       "ex2tbpDatabaseConnsRejectdPerSec": ex2tbpDatabaseConnsRejectdPerSec,
       "ex2tbpTransactionsAbortedTotal": ex2tbpTransactionsAbortedTotal,
       "ex2tbpTransactionsAbortedPerSec": ex2tbpTransactionsAbortedPerSec,
       "ex2tbpTransactionsCommittedTotal": ex2tbpTransactionsCommittedTotal,
       "ex2tbpTransactionCommittedPerSec": ex2tbpTransactionCommittedPerSec,
       "ex2TransportDSNTable": ex2TransportDSNTable,
       "ex2TransportDSNEntry": ex2TransportDSNEntry,
       "ex2tdsnInstance": ex2tdsnInstance,
       "ex2tdsnDelayDSNs": ex2tdsnDelayDSNs,
       "ex2tdsnDeliveredDSNs": ex2tdsnDeliveredDSNs,
       "ex2tdsnExpandedDSNs": ex2tdsnExpandedDSNs,
       "ex2tdsnFailureDSNsTotal": ex2tdsnFailureDSNsTotal,
       "ex2tdsnRelayDSNs": ex2tdsnRelayDSNs,
       "ex2TransportDatabaseTable": ex2TransportDatabaseTable,
       "ex2TransportDatabaseEntry": ex2TransportDatabaseEntry,
       "ex2tbInstance": ex2tbInstance,
       "ex2tbColumCacheLoadTotal": ex2tbColumCacheLoadTotal,
       "ex2tbColumCacheLoadPerSec": ex2tbColumCacheLoadPerSec,
       "ex2tbColumCacheSaveTotal": ex2tbColumCacheSaveTotal,
       "ex2tbColumCacheSavePerSec": ex2tbColumCacheSavePerSec,
       "ex2tbColumnCacheLoadedBytesTotal": ex2tbColumnCacheLoadedBytesTotal,
       "ex2tbColumnCachLoadedBytesPerSec": ex2tbColumnCachLoadedBytesPerSec,
       "ex2tbColumnCacheLoadColumnsTotal": ex2tbColumnCacheLoadColumnsTotal,
       "ex2tbColumnCacheLoadedColumnsSec": ex2tbColumnCacheLoadedColumnsSec,
       "ex2tbColumnCacheSavedBytesTotal": ex2tbColumnCacheSavedBytesTotal,
       "ex2tbColumnCacheSavedBytesPerSec": ex2tbColumnCacheSavedBytesPerSec,
       "ex2tbColumnCacheSavedColumnTotal": ex2tbColumnCacheSavedColumnTotal,
       "ex2tbColumnCacheSaveColumnPerSec": ex2tbColumnCacheSaveColumnPerSec,
       "ex2tbDataRowClonesTotal": ex2tbDataRowClonesTotal,
       "ex2tbDataRowClonesPerSec": ex2tbDataRowClonesPerSec,
       "ex2tbDataRowDeletesTotal": ex2tbDataRowDeletesTotal,
       "ex2tbDataRowDeletesPerSec": ex2tbDataRowDeletesPerSec,
       "ex2tbDataRowLoadsTotal": ex2tbDataRowLoadsTotal,
       "ex2tbDataRowLoadsPerSec": ex2tbDataRowLoadsPerSec,
       "ex2tbDataRowMinimizeMemoryTotal": ex2tbDataRowMinimizeMemoryTotal,
       "ex2tbDataRowMinimizeMemoryPerSec": ex2tbDataRowMinimizeMemoryPerSec,
       "ex2tbDataRowMovesTotal": ex2tbDataRowMovesTotal,
       "ex2tbDataRowMovesPerSec": ex2tbDataRowMovesPerSec,
       "ex2tbDataRowNewInsertsTotal": ex2tbDataRowNewInsertsTotal,
       "ex2tbDataRowNewInsertsPerSec": ex2tbDataRowNewInsertsPerSec,
       "ex2tbDataRowSeeksPrefixTotal": ex2tbDataRowSeeksPrefixTotal,
       "ex2tbDataRowSeeksPrefixPerSec": ex2tbDataRowSeeksPrefixPerSec,
       "ex2tbDataRowSeeksTotal": ex2tbDataRowSeeksTotal,
       "ex2tbDataRowSeeksPerSec": ex2tbDataRowSeeksPerSec,
       "ex2tbDataRowUpdatesTotal": ex2tbDataRowUpdatesTotal,
       "ex2tbDataRowUpdatesPerSec": ex2tbDataRowUpdatesPerSec,
       "ex2tbExtendPropertyByteReadTotal": ex2tbExtendPropertyByteReadTotal,
       "ex2tbExtendPropertyBytReadPerSec": ex2tbExtendPropertyBytReadPerSec,
       "ex2tbExtenePropertyByteWritTotal": ex2tbExtenePropertyByteWritTotal,
       "ex2tbExtenPropertyByteWritPerSec": ex2tbExtenPropertyByteWritPerSec,
       "ex2tbExtenedPropertyReadsTotal": ex2tbExtenedPropertyReadsTotal,
       "ex2tbExtenedPropertyReadsPerSec": ex2tbExtenedPropertyReadsPerSec,
       "ex2tbExtenedPropertyWritesTotal": ex2tbExtenedPropertyWritesTotal,
       "ex2tbExtenedPropertyWritesPerSec": ex2tbExtenedPropertyWritesPerSec,
       "ex2tbLazyBytesLoadPerformedTotal": ex2tbLazyBytesLoadPerformedTotal,
       "ex2tbLazyByteLoadPerformedPerSec": ex2tbLazyByteLoadPerformedPerSec,
       "ex2tbLazyBytesLoadRequestedTotal": ex2tbLazyBytesLoadRequestedTotal,
       "ex2tbLazyByteLoadRequestedPerSec": ex2tbLazyByteLoadRequestedPerSec,
       "ex2tbMailItemBeginCommitTotal": ex2tbMailItemBeginCommitTotal,
       "ex2tbMailItemBeginCommitPerSec": ex2tbMailItemBeginCommitPerSec,
       "ex2tbMailItemCloneCreateTotal": ex2tbMailItemCloneCreateTotal,
       "ex2tbMailItemCloneCreatePerSec": ex2tbMailItemCloneCreatePerSec,
       "ex2tbMailItemCommitImmediatTotal": ex2tbMailItemCommitImmediatTotal,
       "ex2tbMailItemCommitImmediaPerSec": ex2tbMailItemCommitImmediaPerSec,
       "ex2tbMailItemCommitLazyTotal": ex2tbMailItemCommitLazyTotal,
       "ex2tbMailItemCommitLazyPerSec": ex2tbMailItemCommitLazyPerSec,
       "ex2tbMailItemDehydrateTotal": ex2tbMailItemDehydrateTotal,
       "ex2tbMailItemDehydratePerSec": ex2tbMailItemDehydratePerSec,
       "ex2tbMailItemDeleteLazyTotal": ex2tbMailItemDeleteLazyTotal,
       "ex2tbMailItemDeleteLazyPerSec": ex2tbMailItemDeleteLazyPerSec,
       "ex2tbMailItemLoadTotal": ex2tbMailItemLoadTotal,
       "ex2tbMailItemLoadPerSec": ex2tbMailItemLoadPerSec,
       "ex2tbMailItemMaterialize": ex2tbMailItemMaterialize,
       "ex2tbMailItemMaterializePerSec": ex2tbMailItemMaterializePerSec,
       "ex2tbMailItemNewTotal": ex2tbMailItemNewTotal,
       "ex2tbMailItemNewPerSec": ex2tbMailItemNewPerSec,
       "ex2tbMailItemWriteMimeToTotal": ex2tbMailItemWriteMimeToTotal,
       "ex2tbMailItemWriteMimeToPerSec": ex2tbMailItemWriteMimeToPerSec,
       "ex2tbStreamBytesReadTotal": ex2tbStreamBytesReadTotal,
       "ex2tbStreamBytesReadPerSec": ex2tbStreamBytesReadPerSec,
       "ex2tbStreamBytesWrittenTotal": ex2tbStreamBytesWrittenTotal,
       "ex2tbStreamBytesWrittenPerSec": ex2tbStreamBytesWrittenPerSec,
       "ex2tbStreamReadTotal": ex2tbStreamReadTotal,
       "ex2tbStreamReadPerSec": ex2tbStreamReadPerSec,
       "ex2tbStreamSetLengthCount": ex2tbStreamSetLengthCount,
       "ex2tbStreamSetLengthPerSec": ex2tbStreamSetLengthPerSec,
       "ex2tbStreamWritesTotal": ex2tbStreamWritesTotal,
       "ex2tbStreamWritesPerSec": ex2tbStreamWritesPerSec,
       "ex2TransportDumpster": ex2TransportDumpster,
       "ex2tdDumpsterDeletesPerSec": ex2tdDumpsterDeletesPerSec,
       "ex2tdDumpsterInsertsPerSec": ex2tdDumpsterInsertsPerSec,
       "ex2tdDumpsterItemCount": ex2tdDumpsterItemCount,
       "ex2tdDumpsterSize": ex2tdDumpsterSize,
       "ex2tdRedeliveryCount": ex2tdRedeliveryCount,
       "ex2TransportPickupTable": ex2TransportPickupTable,
       "ex2TransportPickupEntry": ex2TransportPickupEntry,
       "ex2tpkInstance": ex2tpkInstance,
       "ex2tpkMessagesBadmailed": ex2tpkMessagesBadmailed,
       "ex2tpkMessagesNDRed": ex2tpkMessagesNDRed,
       "ex2tpkMessagesSubmitted": ex2tpkMessagesSubmitted,
       "ex2TransportQueuesTable": ex2TransportQueuesTable,
       "ex2TransportQueuesEntry": ex2TransportQueuesEntry,
       "ex2tqInstance": ex2tqInstance,
       "ex2tqActiveMailboxDelivQueLength": ex2tqActiveMailboxDelivQueLength,
       "ex2tqActiveNonSmtpDelivQueLength": ex2tqActiveNonSmtpDelivQueLength,
       "ex2tqActiveRemoteDelivQueLength": ex2tqActiveRemoteDelivQueLength,
       "ex2tqAggregDelivQueLengthAllQues": ex2tqAggregDelivQueLengthAllQues,
       "ex2tqItemCompletedDelivPerSecond": ex2tqItemCompletedDelivPerSecond,
       "ex2tqItemsCompletedDeliveryTotal": ex2tqItemsCompletedDeliveryTotal,
       "ex2tqItemsDeletedByAdminTotal": ex2tqItemsDeletedByAdminTotal,
       "ex2tqItemQuedForDelivExpireTotal": ex2tqItemQuedForDelivExpireTotal,
       "ex2tqItemsQueuedForDeliveryTotal": ex2tqItemsQueuedForDeliveryTotal,
       "ex2tqItemsQuedForDelivPerSecond": ex2tqItemsQuedForDelivPerSecond,
       "ex2tqItemsResubmittedTotal": ex2tqItemsResubmittedTotal,
       "ex2tqLargestDeliveryQueueLength": ex2tqLargestDeliveryQueueLength,
       "ex2tqMsgsCompletedDelivPerSecond": ex2tqMsgsCompletedDelivPerSecond,
       "ex2tqMsgsCompletedDelivTotal": ex2tqMsgsCompletedDelivTotal,
       "ex2tqMessagesQueuedForDelivery": ex2tqMessagesQueuedForDelivery,
       "ex2tqMsgsQuedForDelivTotal": ex2tqMsgsQuedForDelivTotal,
       "ex2tqMsgsQuedForDelivPerSecond": ex2tqMsgsQuedForDelivPerSecond,
       "ex2tqMessagesSubmittedPerSecond": ex2tqMessagesSubmittedPerSecond,
       "ex2tqMessagesSubmittedTotal": ex2tqMessagesSubmittedTotal,
       "ex2tqPoisonQueueLength": ex2tqPoisonQueueLength,
       "ex2tqRetryMailboxDelivQueLength": ex2tqRetryMailboxDelivQueLength,
       "ex2tqRetryNonSmtpDelivQueLength": ex2tqRetryNonSmtpDelivQueLength,
       "ex2tqRetryRemoteDelivQueLength": ex2tqRetryRemoteDelivQueLength,
       "ex2tqSubmissQueueItemExpireTotal": ex2tqSubmissQueueItemExpireTotal,
       "ex2tqSubmissionQueueLength": ex2tqSubmissionQueueLength,
       "ex2tqUnreachableQueueLength": ex2tqUnreachableQueueLength,
       "ex2TransportResolverTable": ex2TransportResolverTable,
       "ex2TransportResolverEntry": ex2TransportResolverEntry,
       "ex2treInstance": ex2treInstance,
       "ex2treAmbiguousRecipients": ex2treAmbiguousRecipients,
       "ex2treAmbiguousSenders": ex2treAmbiguousSenders,
       "ex2treFailedRecipients": ex2treFailedRecipients,
       "ex2treLoopRecipients": ex2treLoopRecipients,
       "ex2treMessagesChipped": ex2treMessagesChipped,
       "ex2treMessagesCreated": ex2treMessagesCreated,
       "ex2treMessagesRetried": ex2treMessagesRetried,
       "ex2treUnresolvedOrgRecipients": ex2treUnresolvedOrgRecipients,
       "ex2treUnresolvedOrgSenders": ex2treUnresolvedOrgSenders,
       "ex2TransportRoutingTable": ex2TransportRoutingTable,
       "ex2TransportRoutingEntry": ex2TransportRoutingEntry,
       "ex2troInstance": ex2troInstance,
       "ex2troRoutingNDRsTotal": ex2troRoutingNDRsTotal,
       "ex2troRoutingTableCalculateTotal": ex2troRoutingTableCalculateTotal,
       "ex2troRoutingTablesChangedTotal": ex2troRoutingTablesChangedTotal,
       "ex2TransportSmtpReceiveTable": ex2TransportSmtpReceiveTable,
       "ex2TransportSmtpReceiveEntry": ex2TransportSmtpReceiveEntry,
       "ex2tsrInstance": ex2tsrInstance,
       "ex2tsrAverageBytesPerConnection": ex2tsrAverageBytesPerConnection,
       "ex2tsrAverageBytesPerMessage": ex2tsrAverageBytesPerMessage,
       "ex2tsrAverageMessagePerConnectin": ex2tsrAverageMessagePerConnectin,
       "ex2tsrAverageRecipientPerMessage": ex2tsrAverageRecipientPerMessage,
       "ex2tsrBytesReceivedTotal": ex2tsrBytesReceivedTotal,
       "ex2tsrBytesReceivedPerSec": ex2tsrBytesReceivedPerSec,
       "ex2tsrConnectionsCreatedPerSec": ex2tsrConnectionsCreatedPerSec,
       "ex2tsrConnectionsCurrent": ex2tsrConnectionsCurrent,
       "ex2tsrConnectionsTotal": ex2tsrConnectionsTotal,
       "ex2tsrDisconnectionsByAgents": ex2tsrDisconnectionsByAgents,
       "ex2tsrDisconnectByAgentPerSecond": ex2tsrDisconnectByAgentPerSecond,
       "ex2tsrMessageBytesReceivedTotal": ex2tsrMessageBytesReceivedTotal,
       "ex2tsrMessageBytesReceivedPerSec": ex2tsrMessageBytesReceivedPerSec,
       "ex2tsrMessagesReceivedTotal": ex2tsrMessagesReceivedTotal,
       "ex2tsrMessagesReceivedPerSec": ex2tsrMessagesReceivedPerSec,
       "ex2tsrMessagesRefusedForSize": ex2tsrMessagesRefusedForSize,
       "ex2tsrRecipientsAcceptedTotal": ex2tsrRecipientsAcceptedTotal,
       "ex2tsrTarpittingDelaysAnonymous": ex2tsrTarpittingDelaysAnonymous,
       "ex2tsrTarpittngDelayAuthenticate": ex2tsrTarpittngDelayAuthenticate,
       "ex2TransportSmtpSendTable": ex2TransportSmtpSendTable,
       "ex2TransportSmtpSendEntry": ex2TransportSmtpSendEntry,
       "ex2tssInstance": ex2tssInstance,
       "ex2tssAverageBytesPerConnection": ex2tssAverageBytesPerConnection,
       "ex2tssAvgMessageBytesPerMessage": ex2tssAvgMessageBytesPerMessage,
       "ex2tssAvgMessagesPerConnection": ex2tssAvgMessagesPerConnection,
       "ex2tssAvgRecipientsPerMessage": ex2tssAvgRecipientsPerMessage,
       "ex2tssBytesSentTotal": ex2tssBytesSentTotal,
       "ex2tssBytesSentPerSec": ex2tssBytesSentPerSec,
       "ex2tssConnectionsCreatedPerSec": ex2tssConnectionsCreatedPerSec,
       "ex2tssConnectionsCurrent": ex2tssConnectionsCurrent,
       "ex2tssConnectionsTotal": ex2tssConnectionsTotal,
       "ex2tssMessageBytesSentTotal": ex2tssMessageBytesSentTotal,
       "ex2tssMessageBytesSentPerSec": ex2tssMessageBytesSentPerSec,
       "ex2tssMessagesSentTotal": ex2tssMessagesSentTotal,
       "ex2tssMessagesSentPerSec": ex2tssMessagesSentPerSec,
       "ex2tssRecipientsSent": ex2tssRecipientsSent,
       "ex2UMAutoAttendantTable": ex2UMAutoAttendantTable,
       "ex2UMAutoAttendantEntry": ex2UMAutoAttendantEntry,
       "ex2umaaInstance": ex2umaaInstance,
       "ex2umaaPercentSuccessfulCalls": ex2umaaPercentSuccessfulCalls,
       "ex2umaaAmbiguousNameTransfers": ex2umaaAmbiguousNameTransfers,
       "ex2umaaAverageCallTime": ex2umaaAverageCallTime,
       "ex2umaaAverageRecentCallTime": ex2umaaAverageRecentCallTime,
       "ex2umaaBusinessHoursCalls": ex2umaaBusinessHoursCalls,
       "ex2umaaCallsDisconUMIrreExtError": ex2umaaCallsDisconUMIrreExtError,
       "ex2umaaCallsWithDTMFFallback": ex2umaaCallsWithDTMFFallback,
       "ex2umaaCallsWithSentMessage": ex2umaaCallsWithSentMessage,
       "ex2umaaCallsWithSpeechInput": ex2umaaCallsWithSpeechInput,
       "ex2umaaCallsWithSpokenName": ex2umaaCallsWithSpokenName,
       "ex2umaaCustomMenuOptions": ex2umaaCustomMenuOptions,
       "ex2umaaDirectoryAccessed": ex2umaaDirectoryAccessed,
       "ex2umaaDirAccsdSuccByDialByName": ex2umaaDirAccsdSuccByDialByName,
       "ex2umaaDirAccsdSuccBySpokenName": ex2umaaDirAccsdSuccBySpokenName,
       "ex2umaaDirAccsdByDialByName": ex2umaaDirAccsdByDialByName,
       "ex2umaaDirAccsdByExtension": ex2umaaDirAccsdByExtension,
       "ex2umaaDirAccsdBySpokenName": ex2umaaDirAccsdBySpokenName,
       "ex2umaaDisallowedTransfers": ex2umaaDisallowedTransfers,
       "ex2umaaDisconnectedWithoutInput": ex2umaaDisconnectedWithoutInput,
       "ex2umaaMenuOption1Used": ex2umaaMenuOption1Used,
       "ex2umaaMenuOption2Used": ex2umaaMenuOption2Used,
       "ex2umaaMenuOption3Used": ex2umaaMenuOption3Used,
       "ex2umaaMenuOption4Used": ex2umaaMenuOption4Used,
       "ex2umaaMenuOption5Used": ex2umaaMenuOption5Used,
       "ex2umaaMenuOption6Used": ex2umaaMenuOption6Used,
       "ex2umaaMenuOption7Used": ex2umaaMenuOption7Used,
       "ex2umaaMenuOption8Used": ex2umaaMenuOption8Used,
       "ex2umaaMenuOption9Used": ex2umaaMenuOption9Used,
       "ex2umaaMenuOptionTimedOut": ex2umaaMenuOptionTimedOut,
       "ex2umaaOperatorTransfers": ex2umaaOperatorTransfers,
       "ex2umaaOperTransReqByUser": ex2umaaOperTransReqByUser,
       "ex2umaaOperTransReqByUseOpenMenu": ex2umaaOperTransReqByUseOpenMenu,
       "ex2umaaOutOfHoursCalls": ex2umaaOutOfHoursCalls,
       "ex2umaaSentToAutoAttendant": ex2umaaSentToAutoAttendant,
       "ex2umaaTotalCalls": ex2umaaTotalCalls,
       "ex2umaaTransferredCount": ex2umaaTransferredCount,
       "ex2UMAvailability": ex2UMAvailability,
       "ex2umaCallAnswerQueuedMessages": ex2umaCallAnswerQueuedMessages,
       "ex2umaCalDisconUMIrrecovExtError": ex2umaCalDisconUMIrrecovExtError,
       "ex2umaCalDiscnUMIrrecovExtErrSec": ex2umaCalDiscnUMIrrecovExtErrSec,
       "ex2umaCalDiscnIrrecovInternalErr": ex2umaCalDiscnIrrecovInternalErr,
       "ex2umaDirectoryAccessFailures": ex2umaDirectoryAccessFailures,
       "ex2umaFailedToRedirectCall": ex2umaFailedToRedirectCall,
       "ex2umaHubTransportAccessComplete": ex2umaHubTransportAccessComplete,
       "ex2umaHubTransportAccessFailures": ex2umaHubTransportAccessFailures,
       "ex2umaIncompSignalingInformation": ex2umaIncompSignalingInformation,
       "ex2umaMailboxServerAccessFailure": ex2umaMailboxServerAccessFailure,
       "ex2umaMaximumCallsAllowed": ex2umaMaximumCallsAllowed,
       "ex2umaNameTTSed": ex2umaNameTTSed,
       "ex2umaQueuedOCSUserEventNotifica": ex2umaQueuedOCSUserEventNotifica,
       "ex2umaSpokenNameAccessed": ex2umaSpokenNameAccessed,
       "ex2umaTotalWorkerProcesCallCount": ex2umaTotalWorkerProcesCallCount,
       "ex2umaUnhandledExceptionsPerSec": ex2umaUnhandledExceptionsPerSec,
       "ex2umaWorkerProcessRecycled": ex2umaWorkerProcessRecycled,
       "ex2UMCallAnswer": ex2UMCallAnswer,
       "ex2UMCallAnsAvgGreetingSize": ex2UMCallAnsAvgGreetingSize,
       "ex2UMCallAnsAvgRecentVoiceMsgSiz": ex2UMCallAnsAvgRecentVoiceMsgSiz,
       "ex2UMCallAnsAvgVoiceMsgSize": ex2UMCallAnsAvgVoiceMsgSize,
       "ex2UMCallAnsCallAnsingCalls": ex2UMCallAnsCallAnsingCalls,
       "ex2UMCallAnsCallAnsingEscapes": ex2UMCallAnsCallAnsingEscapes,
       "ex2UMCallAnsCallAnsingMissedCall": ex2UMCallAnsCallAnsingMissedCall,
       "ex2UMCallAnsCallAnsingVoiceMsgs": ex2UMCallAnsCallAnsingVoiceMsgs,
       "ex2UMCallAnsCallAnsVoiceMsgPrSec": ex2UMCallAnsCallAnsVoiceMsgPrSec,
       "ex2UMCallAnsCallFailTransUnavail": ex2UMCallAnsCallFailTransUnavail,
       "ex2UMCalAnsCalDisCalUMAudioHrgls": ex2UMCalAnsCalDisCalUMAudioHrgls,
       "ex2UMCalAnsCalDisUMIrrecExtError": ex2UMCalAnsCalDisUMIrrecExtError,
       "ex2UMCallAnsCallWithoutPersGreet": ex2UMCallAnsCallWithoutPersGreet,
       "ex2UMCallAnsDivertExtNotProvis": ex2UMCallAnsDivertExtNotProvis,
       "ex2UMCallAnsFetchGreetingTimeOut": ex2UMCallAnsFetchGreetingTimeOut,
       "ex2UMClientAccessTable": ex2UMClientAccessTable,
       "ex2UMClientAccessEntry": ex2UMClientAccessEntry,
       "ex2umcacInstance": ex2umcacInstance,
       "ex2umcacPID": ex2umcacPID,
       "ex2umcacTotalNumPINResetRequests": ex2umcacTotalNumPINResetRequests,
       "ex2umcacTotalNumFailPINResetReq": ex2umcacTotalNumFailPINResetReq,
       "ex2umcacTotalNumFailPlayPhoneReq": ex2umcacTotalNumFailPlayPhoneReq,
       "ex2umcacTotalNumPlayPhoneRequest": ex2umcacTotalNumPlayPhoneRequest,
       "ex2UMFax": ex2UMFax,
       "ex2umfAverageFaxMessageSize": ex2umfAverageFaxMessageSize,
       "ex2umfAverageRecentFaxMessageSiz": ex2umfAverageRecentFaxMessageSiz,
       "ex2umfFaxCallDurationExceeded": ex2umfFaxCallDurationExceeded,
       "ex2umfFaxCallNonProvisionMailbox": ex2umfFaxCallNonProvisionMailbox,
       "ex2umfFaxIncomplete": ex2umfFaxIncomplete,
       "ex2umfFaxMessages": ex2umfFaxMessages,
       "ex2UMGeneral": ex2UMGeneral,
       "ex2umgAverageCallDuration": ex2umgAverageCallDuration,
       "ex2umgAverageRecentCallDuration": ex2umgAverageRecentCallDuration,
       "ex2umgCallDurationExceeded": ex2umgCallDurationExceeded,
       "ex2umgCallsDisconnectUserFailure": ex2umgCallsDisconnectUserFailure,
       "ex2umgCallsRejected": ex2umgCallsRejected,
       "ex2umgCallsRejectedPerSecond": ex2umgCallsRejectedPerSecond,
       "ex2umgCurrentAutoAttendantCalls": ex2umgCurrentAutoAttendantCalls,
       "ex2umgCurrentCASConnections": ex2umgCurrentCASConnections,
       "ex2umgCurrentCalls": ex2umgCurrentCalls,
       "ex2umgCurrentFaxCalls": ex2umgCurrentFaxCalls,
       "ex2umgCurrentPlayOnPhoneCalls": ex2umgCurrentPlayOnPhoneCalls,
       "ex2umgCurrentPromptEditingCalls": ex2umgCurrentPromptEditingCalls,
       "ex2umgCurrentSubscriberAccesCall": ex2umgCurrentSubscriberAccesCall,
       "ex2umgCurrUnauthentPilotNumCall": ex2umgCurrUnauthentPilotNumCall,
       "ex2umgCurrentVoiceCalls": ex2umgCurrentVoiceCalls,
       "ex2umgDelayedCalls": ex2umgDelayedCalls,
       "ex2umgOCSUserEventNotifications": ex2umgOCSUserEventNotifications,
       "ex2umgTotalCalls": ex2umgTotalCalls,
       "ex2umgTotalCallsPerSecond": ex2umgTotalCallsPerSecond,
       "ex2umgTotalPlayOnPhoneCalls": ex2umgTotalPlayOnPhoneCalls,
       "ex2umgUserResponseLatency": ex2umgUserResponseLatency,
       "ex2UMPerformance": ex2UMPerformance,
       "ex2umpOperationsOverFiveSeconds": ex2umpOperationsOverFiveSeconds,
       "ex2umpOperationsOverFourSeconds": ex2umpOperationsOverFourSeconds,
       "ex2umpOperationsOverSixSeconds": ex2umpOperationsOverSixSeconds,
       "ex2umpOperationsOverThreeSeconds": ex2umpOperationsOverThreeSeconds,
       "ex2umpOperationsOverTwoSeconds": ex2umpOperationsOverTwoSeconds,
       "ex2umpOperationsUnderTwoSeconds": ex2umpOperationsUnderTwoSeconds,
       "ex2UMSubscriberAccess": ex2UMSubscriberAccess,
       "ex2umsaAvgRecentSentVoiceMsgSize": ex2umsaAvgRecentSentVoiceMsgSize,
       "ex2umsaAvgRecentSubscribeCallDur": ex2umsaAvgRecentSubscribeCallDur,
       "ex2umsaAvgSentVoiceMessageSize": ex2umsaAvgSentVoiceMessageSize,
       "ex2umsaAvgSubscriberCallDuration": ex2umsaAvgSubscriberCallDuration,
       "ex2umsaCalendarAccessed": ex2umsaCalendarAccessed,
       "ex2umsaCalendarItemDetailRequest": ex2umsaCalendarItemDetailRequest,
       "ex2umsaCalendarItemsHeard": ex2umsaCalendarItemsHeard,
       "ex2umsaCalendarLateAttendance": ex2umsaCalendarLateAttendance,
       "ex2umsaCalledMeetingOrganizer": ex2umsaCalledMeetingOrganizer,
       "ex2umsaCalDiscCalDurUMAudioHrgls": ex2umsaCalDiscCalDurUMAudioHrgls,
       "ex2umsaCallDisUMOnIrrecvExtError": ex2umsaCallDisUMOnIrrecvExtError,
       "ex2umsaContactItemsHeard": ex2umsaContactItemsHeard,
       "ex2umsaContactsAccessed": ex2umsaContactsAccessed,
       "ex2umsaDirectoryAccessed": ex2umsaDirectoryAccessed,
       "ex2umsaDirAccsdSuccessDialName": ex2umsaDirAccsdSuccessDialName,
       "ex2umsaDirAccsdSuccessSpokenName": ex2umsaDirAccsdSuccessSpokenName,
       "ex2umsaDirAccsdByDialByName": ex2umsaDirAccsdByDialByName,
       "ex2umsaDirAccsdByExtension": ex2umsaDirAccsdByExtension,
       "ex2umsaDirAccsdBySpokenName": ex2umsaDirAccsdBySpokenName,
       "ex2umsaEmailMessageQueueAccessed": ex2umsaEmailMessageQueueAccessed,
       "ex2umsaEmailMessagesDeleted": ex2umsaEmailMessagesDeleted,
       "ex2umsaEmailMessagesHeard": ex2umsaEmailMessagesHeard,
       "ex2umsaForwardMessagesSent": ex2umsaForwardMessagesSent,
       "ex2umsaLaunchedCalls": ex2umsaLaunchedCalls,
       "ex2umsaMeetingsAccepted": ex2umsaMeetingsAccepted,
       "ex2umsaMeetingsDeclined": ex2umsaMeetingsDeclined,
       "ex2umsaRepliedToOrganizer": ex2umsaRepliedToOrganizer,
       "ex2umsaReplyMessagesSent": ex2umsaReplyMessagesSent,
       "ex2umsaSubscriberAuthentFailure": ex2umsaSubscriberAuthentFailure,
       "ex2umsaSubscriberLogonFailures": ex2umsaSubscriberLogonFailures,
       "ex2umsaSubscriberLogons": ex2umsaSubscriberLogons,
       "ex2umsaVoiceMessageQueueAccessed": ex2umsaVoiceMessageQueueAccessed,
       "ex2umsaVoiceMessagesDeleted": ex2umsaVoiceMessagesDeleted,
       "ex2umsaVoiceMessagesHeard": ex2umsaVoiceMessagesHeard,
       "ex2umsaVoiceMessagesSent": ex2umsaVoiceMessagesSent,
       "ex2WS": ex2WS,
       "ex2WSActiveSubscriptions": ex2WSActiveSubscriptions,
       "ex2WSAddDelegateRequests": ex2WSAddDelegateRequests,
       "ex2WSAddDelegateRequestsPerSec": ex2WSAddDelegateRequestsPerSec,
       "ex2WSConvertIdRequests": ex2WSConvertIdRequests,
       "ex2WSConvertIdRequestsPerSec": ex2WSConvertIdRequestsPerSec,
       "ex2WSCopyFolderRequests": ex2WSCopyFolderRequests,
       "ex2WSCopyFolderRequestsPerSec": ex2WSCopyFolderRequestsPerSec,
       "ex2WSCopyItemRequests": ex2WSCopyItemRequests,
       "ex2WSCopyItemRequestsPerSec": ex2WSCopyItemRequestsPerSec,
       "ex2WSCreateAttachmentRequests": ex2WSCreateAttachmentRequests,
       "ex2WSCreateAttachRequestsPerSec": ex2WSCreateAttachRequestsPerSec,
       "ex2WSCreateFolderRequests": ex2WSCreateFolderRequests,
       "ex2WSCreateFolderRequestsPerSec": ex2WSCreateFolderRequestsPerSec,
       "ex2WSCreateItemRequests": ex2WSCreateItemRequests,
       "ex2WSCreateItemRequestsPerSec": ex2WSCreateItemRequestsPerSec,
       "ex2WSCreateManagedFolderRequests": ex2WSCreateManagedFolderRequests,
       "ex2WSCreateManageFoldReqstPerSec": ex2WSCreateManageFoldReqstPerSec,
       "ex2WSDeleteAttachmentRequests": ex2WSDeleteAttachmentRequests,
       "ex2WSDeleteAttachmentReqstPerSec": ex2WSDeleteAttachmentReqstPerSec,
       "ex2WSDeleteFolderRequests": ex2WSDeleteFolderRequests,
       "ex2WSDeleteFolderRequestsPerSec": ex2WSDeleteFolderRequestsPerSec,
       "ex2WSDeleteItemRequests": ex2WSDeleteItemRequests,
       "ex2WSDeleteItemRequestsPerSec": ex2WSDeleteItemRequestsPerSec,
       "ex2WSExpandDLRequests": ex2WSExpandDLRequests,
       "ex2WSExpandDLRequestsPerSec": ex2WSExpandDLRequestsPerSec,
       "ex2WSFindFolderRequests": ex2WSFindFolderRequests,
       "ex2WSFindFolderRequestsPerSec": ex2WSFindFolderRequestsPerSec,
       "ex2WSFindItemRequests": ex2WSFindItemRequests,
       "ex2WSFindItemRequestsPerSec": ex2WSFindItemRequestsPerSec,
       "ex2WSFoldersCopied": ex2WSFoldersCopied,
       "ex2WSFoldersCopiedPerSec": ex2WSFoldersCopiedPerSec,
       "ex2WSFoldersCreated": ex2WSFoldersCreated,
       "ex2WSFoldersCreatedPerSec": ex2WSFoldersCreatedPerSec,
       "ex2WSFoldersDeleted": ex2WSFoldersDeleted,
       "ex2WSFoldersDeletedPerSec": ex2WSFoldersDeletedPerSec,
       "ex2WSFoldersMoved": ex2WSFoldersMoved,
       "ex2WSFoldersMovedPerSec": ex2WSFoldersMovedPerSec,
       "ex2WSFoldersRead": ex2WSFoldersRead,
       "ex2WSFoldersSentPerSec": ex2WSFoldersSentPerSec,
       "ex2WSFoldersSyncedPerSec": ex2WSFoldersSyncedPerSec,
       "ex2WSFoldersSynchronized": ex2WSFoldersSynchronized,
       "ex2WSFoldersUpdated": ex2WSFoldersUpdated,
       "ex2WSFoldersUpdatedPerSec": ex2WSFoldersUpdatedPerSec,
       "ex2WSGetAttachmentRequests": ex2WSGetAttachmentRequests,
       "ex2WSGetAttachmentRequestsPerSec": ex2WSGetAttachmentRequestsPerSec,
       "ex2WSGetDelegateRequests": ex2WSGetDelegateRequests,
       "ex2WSGetDelegateRequestsPerSec": ex2WSGetDelegateRequestsPerSec,
       "ex2WSGetEventsRequests": ex2WSGetEventsRequests,
       "ex2WSGetEventsRequestsPerSec": ex2WSGetEventsRequestsPerSec,
       "ex2WSGetFolderRequests": ex2WSGetFolderRequests,
       "ex2WSGetFolderRequestsPerSec": ex2WSGetFolderRequestsPerSec,
       "ex2WSGetItemRequests": ex2WSGetItemRequests,
       "ex2WSGetItemRequestsPerSec": ex2WSGetItemRequestsPerSec,
       "ex2WSIdsConvertedPerSec": ex2WSIdsConvertedPerSec,
       "ex2WSItemsCopied": ex2WSItemsCopied,
       "ex2WSItemsCopiedPerSec": ex2WSItemsCopiedPerSec,
       "ex2WSItemsCreated": ex2WSItemsCreated,
       "ex2WSItemsCreatedPerSec": ex2WSItemsCreatedPerSec,
       "ex2WSItemsDeleted": ex2WSItemsDeleted,
       "ex2WSItemsDeletedPerSec": ex2WSItemsDeletedPerSec,
       "ex2WSItemsMoved": ex2WSItemsMoved,
       "ex2WSItemsMovedPerSec": ex2WSItemsMovedPerSec,
       "ex2WSItemsRead": ex2WSItemsRead,
       "ex2WSItemsReadPerSec": ex2WSItemsReadPerSec,
       "ex2WSItemsSent": ex2WSItemsSent,
       "ex2WSItemsSentPerSec": ex2WSItemsSentPerSec,
       "ex2WSItemsSyncedPerSec": ex2WSItemsSyncedPerSec,
       "ex2WSItemsSynchronized": ex2WSItemsSynchronized,
       "ex2WSItemsUpdated": ex2WSItemsUpdated,
       "ex2WSItemsUpdatedPerSec": ex2WSItemsUpdatedPerSec,
       "ex2WSMoveFolderRequests": ex2WSMoveFolderRequests,
       "ex2WSMoveFolderRequestsPerSec": ex2WSMoveFolderRequestsPerSec,
       "ex2WSMoveItemRequests": ex2WSMoveItemRequests,
       "ex2WSMoveItemRequestsPerSec": ex2WSMoveItemRequestsPerSec,
       "ex2WSNumberOfCurrentProxyCalls": ex2WSNumberOfCurrentProxyCalls,
       "ex2WSNumberOfProxyReqstPerSecond": ex2WSNumberOfProxyReqstPerSecond,
       "ex2WSNumbrProxyFailoverPerSecond": ex2WSNumbrProxyFailoverPerSecond,
       "ex2WSProcessID": ex2WSProcessID,
       "ex2WSProxyAverageResponseTime": ex2WSProxyAverageResponseTime,
       "ex2WSProxyAverageResponseTimNum1": ex2WSProxyAverageResponseTimNum1,
       "ex2WSPushNotificationsFailed": ex2WSPushNotificationsFailed,
       "ex2WSPushNotificationsSucceeded": ex2WSPushNotificationsSucceeded,
       "ex2WSRemoveDelegateRequests": ex2WSRemoveDelegateRequests,
       "ex2WSRemoveDelegateRequestPerSec": ex2WSRemoveDelegateRequestPerSec,
       "ex2WSRequestsPerSec": ex2WSRequestsPerSec,
       "ex2WSResolveNamesRequests": ex2WSResolveNamesRequests,
       "ex2WSResolveNamesRequestsPerSec": ex2WSResolveNamesRequestsPerSec,
       "ex2WSSendItemRequests": ex2WSSendItemRequests,
       "ex2WSSendItemRequestsPerSec": ex2WSSendItemRequestsPerSec,
       "ex2WSSubscribeRequests": ex2WSSubscribeRequests,
       "ex2WSSubscribeRequestsPerSec": ex2WSSubscribeRequestsPerSec,
       "ex2WSSyncFolderHierarchyRequests": ex2WSSyncFolderHierarchyRequests,
       "ex2WSSynFoldHierarchyReqstPerSec": ex2WSSynFoldHierarchyReqstPerSec,
       "ex2WSSyncFolderItemsRequests": ex2WSSyncFolderItemsRequests,
       "ex2WSSyncFolderItemsReqstPerSec": ex2WSSyncFolderItemsReqstPerSec,
       "ex2WSTotalNumberOfIdsConverted": ex2WSTotalNumberOfIdsConverted,
       "ex2WSTotalRequests": ex2WSTotalRequests,
       "ex2WSTotalNumberOfBytesProxied": ex2WSTotalNumberOfBytesProxied,
       "ex2WSTotalNumberOfProxiedRequest": ex2WSTotalNumberOfProxiedRequest,
       "ex2WSTotalNumberOfProxyFailover": ex2WSTotalNumberOfProxyFailover,
       "ex2WSTotalNumberProxyResponsByte": ex2WSTotalNumberProxyResponsByte,
       "ex2WSUnsubscribeRequests": ex2WSUnsubscribeRequests,
       "ex2WSUnsubscribeRequestsPerSec": ex2WSUnsubscribeRequestsPerSec,
       "ex2WSUpdateDelegateRequests": ex2WSUpdateDelegateRequests,
       "ex2WSUpdateDelegateRequestPerSec": ex2WSUpdateDelegateRequestPerSec,
       "ex2WSUpdateFolderRequests": ex2WSUpdateFolderRequests,
       "ex2WSUpdateFolderRequestsPerSec": ex2WSUpdateFolderRequestsPerSec,
       "ex2WSUpdateItemRequests": ex2WSUpdateItemRequests,
       "ex2WSUpdateItemRequestsPerSec": ex2WSUpdateItemRequestsPerSec,
       "ex2CatalogsTable": ex2CatalogsTable,
       "ex2CatalogsEntry": ex2CatalogsEntry,
       "ex2catInstance": ex2catInstance,
       "ex2catBatchesFPC": ex2catBatchesFPC,
       "ex2catBatchesAborted": ex2catBatchesAborted,
       "ex2catBatchesCompletedSuccess": ex2catBatchesCompletedSuccess,
       "ex2catBatchesCompletedWPerErrors": ex2catBatchesCompletedWPerErrors,
       "ex2catBatchesCompleteWPerWarning": ex2catBatchesCompleteWPerWarning,
       "ex2catBatchesDone": ex2catBatchesDone,
       "ex2catBatchesInProgress": ex2catBatchesInProgress,
       "ex2catBatchesReceived": ex2catBatchesReceived,
       "ex2catPhaseComplete": ex2catPhaseComplete,
       "ex2catPhaseInHDFD": ex2catPhaseInHDFD,
       "ex2catPhaseInMTFD": ex2catPhaseInMTFD,
       "ex2catPhaseInSTFD": ex2catPhaseInSTFD,
       "ex2catPhaseInPipeline": ex2catPhaseInPipeline,
       "ex2catPhaseInReadyQueue": ex2catPhaseInReadyQueue,
       "ex2catPhaseOnHold": ex2catPhaseOnHold,
       "ex2catPhasePendingCompletion": ex2catPhasePendingCompletion,
       "ex2catPhaseRedundant": ex2catPhaseRedundant,
       "ex2catRequestAbort": ex2catRequestAbort,
       "ex2catRequestAsyncFlush": ex2catRequestAsyncFlush,
       "ex2catRequestFlushPerDrain": ex2catRequestFlushPerDrain,
       "ex2catRequestForceMerge": ex2catRequestForceMerge,
       "ex2catRequestPause": ex2catRequestPause,
       "ex2catRequestReset": ex2catRequestReset,
       "ex2catRequestResume": ex2catRequestResume,
       "ex2catState": ex2catState,
       "ex2catStateCallerComponent": ex2catStateCallerComponent,
       "ex2catStateReasonCode": ex2catStateReasonCode,
       "ex2catStateResultCode": ex2catStateResultCode,
       "ex2catTransDeletes": ex2catTransDeletes,
       "ex2catTransDone": ex2catTransDone,
       "ex2catTransErrored": ex2catTransErrored,
       "ex2catTransInProgress": ex2catTransInProgress,
       "ex2catTransModifies": ex2catTransModifies,
       "ex2catTransRerouted": ex2catTransRerouted,
       "ex2FDTable": ex2FDTable,
       "ex2FDEntry": ex2FDEntry,
       "ex2FDInstance": ex2FDInstance,
       "ex2FDBatchesCompleted": ex2FDBatchesCompleted,
       "ex2FDBatchesInProgress": ex2FDBatchesInProgress,
       "ex2FDBatchesReceived": ex2FDBatchesReceived,
       "ex2FDBatchesRejected": ex2FDBatchesRejected,
       "ex2FDFilters": ex2FDFilters,
       "ex2FDNoiseWordLists": ex2FDNoiseWordLists,
       "ex2FDTransErrors": ex2FDTransErrors,
       "ex2FDTransSuccess": ex2FDTransSuccess,
       "ex2FDTransactionsCompleted": ex2FDTransactionsCompleted,
       "ex2FDTransactionsReceived": ex2FDTransactionsReceived,
       "ex2FDTransactionsStarted": ex2FDTransactionsStarted,
       "ex2FDWordBreakers": ex2FDWordBreakers,
       "ex2Service": ex2Service,
       "ex2svcBatchesFPC": ex2svcBatchesFPC,
       "ex2svcBatchesAborted": ex2svcBatchesAborted,
       "ex2svcBatchesCompletedWPerErrors": ex2svcBatchesCompletedWPerErrors,
       "ex2svcBatchesCompleteWPerWarning": ex2svcBatchesCompleteWPerWarning,
       "ex2svcBatcheCompletelySuccessful": ex2svcBatcheCompletelySuccessful,
       "ex2svcBatchesDone": ex2svcBatchesDone,
       "ex2svcBatchesInProgress": ex2svcBatchesInProgress,
       "ex2svcBatchesInReadyQueue": ex2svcBatchesInReadyQueue,
       "ex2svcBatchesReceived": ex2svcBatchesReceived,
       "ex2svcCBSize": ex2svcCBSize,
       "ex2svcCBsAcquired": ex2svcCBsAcquired,
       "ex2svcCBsDestroyed": ex2svcCBsDestroyed,
       "ex2svcCBsGarbageCollected": ex2svcCBsGarbageCollected,
       "ex2svcCBsGiven": ex2svcCBsGiven,
       "ex2svcCBsInUse": ex2svcCBsInUse,
       "ex2svcCBsReleased": ex2svcCBsReleased,
       "ex2svcCBsTotal": ex2svcCBsTotal,
       "ex2svcCatalogsMonitored": ex2svcCatalogsMonitored,
       "ex2svcCatalogsMounted": ex2svcCatalogsMounted,
       "ex2svcFDHDCBEmpty": ex2svcFDHDCBEmpty,
       "ex2svcFDHDActive": ex2svcFDHDActive,
       "ex2svcFDHDLaunched": ex2svcFDHDLaunched,
       "ex2svcFDHDTerminatedAV": ex2svcFDHDTerminatedAV,
       "ex2svcFDHDTerminatedExcessiveMem": ex2svcFDHDTerminatedExcessiveMem,
       "ex2svcFDHDTerminatedIdle": ex2svcFDHDTerminatedIdle,
       "ex2svcFDHDTerminatedOther": ex2svcFDHDTerminatedOther,
       "ex2svcFDHDTerminatedPipe": ex2svcFDHDTerminatedPipe,
       "ex2svcFDHDTerminatedTimeOut": ex2svcFDHDTerminatedTimeOut,
       "ex2svcFDHDUnresponsiveToShutdown": ex2svcFDHDUnresponsiveToShutdown,
       "ex2svcFDMTCBEmpty": ex2svcFDMTCBEmpty,
       "ex2svcFDMTActive": ex2svcFDMTActive,
       "ex2svcFDMTLaunched": ex2svcFDMTLaunched,
       "ex2svcFDMTTerminatedAV": ex2svcFDMTTerminatedAV,
       "ex2svcFDMTTerminatedExcessiveMem": ex2svcFDMTTerminatedExcessiveMem,
       "ex2svcFDMTTerminatedIdle": ex2svcFDMTTerminatedIdle,
       "ex2svcFDMTTerminatedOther": ex2svcFDMTTerminatedOther,
       "ex2svcFDMTTerminatedPipe": ex2svcFDMTTerminatedPipe,
       "ex2svcFDMTTerminatedTimeOut": ex2svcFDMTTerminatedTimeOut,
       "ex2svcFDMTUnresponsiveToShutdown": ex2svcFDMTUnresponsiveToShutdown,
       "ex2svcFDSTCBEmpty": ex2svcFDSTCBEmpty,
       "ex2svcFDSTActive": ex2svcFDSTActive,
       "ex2svcFDSTLaunched": ex2svcFDSTLaunched,
       "ex2svcFDSTTerminatedAV": ex2svcFDSTTerminatedAV,
       "ex2svcFDSTTerminatedExcessiveMem": ex2svcFDSTTerminatedExcessiveMem,
       "ex2svcFDSTTerminatedIdle": ex2svcFDSTTerminatedIdle,
       "ex2svcFDSTTerminatedOther": ex2svcFDSTTerminatedOther,
       "ex2svcFDSTTerminatedPipe": ex2svcFDSTTerminatedPipe,
       "ex2svcFDSTTerminatedTimeOut": ex2svcFDSTTerminatedTimeOut,
       "ex2svcFDSTUnresponsiveToShutdown": ex2svcFDSTUnresponsiveToShutdown,
       "ex2svcHeartbeats": ex2svcHeartbeats,
       "ex2svcIndexPerfLevel": ex2svcIndexPerfLevel,
       "ex2svcQueryPerfLevel": ex2svcQueryPerfLevel,
       "ex2svcTotalNoiseWordFiles": ex2svcTotalNoiseWordFiles,
       "ex2svcTotalStemmers": ex2svcTotalStemmers,
       "ex2svcTotalThesaurus": ex2svcTotalThesaurus,
       "ex2svcTotalWordbreakers": ex2svcTotalWordbreakers}
)

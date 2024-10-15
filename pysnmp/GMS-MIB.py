# SNMP MIB module (GMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:47 2024
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

(applIndex,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex")

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
 enterprises,
 iso,
 mib_2,
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
    "enterprises",
    "iso",
    "mib-2",
    "snmpModules")

(DisplayString,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

gordano = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24534)
)
gordano.setRevisions(
        ("1916-11-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GmsApplTable_Object = MibTable
gmsApplTable = _GmsApplTable_Object(
    (1, 3, 6, 1, 4, 1, 24534, 1)
)
if mibBuilder.loadTexts:
    gmsApplTable.setStatus("current")
_GmsApplEntry_Object = MibTableRow
gmsApplEntry = _GmsApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 24534, 1, 1)
)
gmsApplEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    gmsApplEntry.setStatus("current")
_ApplHandleCount_Type = Integer32
_ApplHandleCount_Object = MibTableColumn
applHandleCount = _ApplHandleCount_Object(
    (1, 3, 6, 1, 4, 1, 24534, 1, 1, 1),
    _ApplHandleCount_Type()
)
applHandleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applHandleCount.setStatus("current")
_ApplPercentCPU_Type = Integer32
_ApplPercentCPU_Object = MibTableColumn
applPercentCPU = _ApplPercentCPU_Object(
    (1, 3, 6, 1, 4, 1, 24534, 1, 1, 2),
    _ApplPercentCPU_Type()
)
applPercentCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPercentCPU.setStatus("current")
_ApplRssKB_Type = Integer32
_ApplRssKB_Object = MibTableColumn
applRssKB = _ApplRssKB_Object(
    (1, 3, 6, 1, 4, 1, 24534, 1, 1, 3),
    _ApplRssKB_Type()
)
applRssKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applRssKB.setStatus("current")
_GmsAV_ObjectIdentity = ObjectIdentity
gmsAV = _GmsAV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24534, 2)
)
_AvEngineVersion_Type = DisplayString
_AvEngineVersion_Object = MibScalar
avEngineVersion = _AvEngineVersion_Object(
    (1, 3, 6, 1, 4, 1, 24534, 2, 1),
    _AvEngineVersion_Type()
)
avEngineVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEngineVersion.setStatus("current")
_AvLastUpdate_Type = DisplayString
_AvLastUpdate_Object = MibScalar
avLastUpdate = _AvLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 24534, 2, 2),
    _AvLastUpdate_Type()
)
avLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avLastUpdate.setStatus("current")
_AvMessagesScanned_Type = Counter64
_AvMessagesScanned_Object = MibScalar
avMessagesScanned = _AvMessagesScanned_Object(
    (1, 3, 6, 1, 4, 1, 24534, 2, 3),
    _AvMessagesScanned_Type()
)
avMessagesScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avMessagesScanned.setStatus("current")
_AvMessagesScannedLow_Type = Counter32
_AvMessagesScannedLow_Object = MibScalar
avMessagesScannedLow = _AvMessagesScannedLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 2, 4),
    _AvMessagesScannedLow_Type()
)
avMessagesScannedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avMessagesScannedLow.setStatus("current")
_AvVirusesFound_Type = Counter64
_AvVirusesFound_Object = MibScalar
avVirusesFound = _AvVirusesFound_Object(
    (1, 3, 6, 1, 4, 1, 24534, 2, 5),
    _AvVirusesFound_Type()
)
avVirusesFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avVirusesFound.setStatus("current")
_AvVirusesFoundLow_Type = Counter32
_AvVirusesFoundLow_Object = MibScalar
avVirusesFoundLow = _AvVirusesFoundLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 2, 6),
    _AvVirusesFoundLow_Type()
)
avVirusesFoundLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avVirusesFoundLow.setStatus("current")
_GmsAS_ObjectIdentity = ObjectIdentity
gmsAS = _GmsAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24534, 3)
)
_AsLastUpdate_Type = DisplayString
_AsLastUpdate_Object = MibScalar
asLastUpdate = _AsLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 24534, 3, 1),
    _AsLastUpdate_Type()
)
asLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLastUpdate.setStatus("current")
_AsMessagesChecked_Type = Counter64
_AsMessagesChecked_Object = MibScalar
asMessagesChecked = _AsMessagesChecked_Object(
    (1, 3, 6, 1, 4, 1, 24534, 3, 2),
    _AsMessagesChecked_Type()
)
asMessagesChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMessagesChecked.setStatus("current")
_AsMessagesCheckedLow_Type = Counter32
_AsMessagesCheckedLow_Object = MibScalar
asMessagesCheckedLow = _AsMessagesCheckedLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 3, 3),
    _AsMessagesCheckedLow_Type()
)
asMessagesCheckedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMessagesCheckedLow.setStatus("current")
_AsMessagesRejected_Type = Counter64
_AsMessagesRejected_Object = MibScalar
asMessagesRejected = _AsMessagesRejected_Object(
    (1, 3, 6, 1, 4, 1, 24534, 3, 4),
    _AsMessagesRejected_Type()
)
asMessagesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMessagesRejected.setStatus("current")
_AsMessagesRejectedLow_Type = Counter32
_AsMessagesRejectedLow_Object = MibScalar
asMessagesRejectedLow = _AsMessagesRejectedLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 3, 5),
    _AsMessagesRejectedLow_Type()
)
asMessagesRejectedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMessagesRejectedLow.setStatus("current")
_GmsSMTP_ObjectIdentity = ObjectIdentity
gmsSMTP = _GmsSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24534, 4)
)
_SmtpThreadsTotal_Type = Integer32
_SmtpThreadsTotal_Object = MibScalar
smtpThreadsTotal = _SmtpThreadsTotal_Object(
    (1, 3, 6, 1, 4, 1, 24534, 4, 1),
    _SmtpThreadsTotal_Type()
)
smtpThreadsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpThreadsTotal.setStatus("current")
_SmtpThreadsActive_Type = Integer32
_SmtpThreadsActive_Object = MibScalar
smtpThreadsActive = _SmtpThreadsActive_Object(
    (1, 3, 6, 1, 4, 1, 24534, 4, 2),
    _SmtpThreadsActive_Type()
)
smtpThreadsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpThreadsActive.setStatus("current")
_SmtpSessions_Type = Integer32
_SmtpSessions_Object = MibScalar
smtpSessions = _SmtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 4, 3),
    _SmtpSessions_Type()
)
smtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpSessions.setStatus("current")
_SmtpSSLSessions_Type = Integer32
_SmtpSSLSessions_Object = MibScalar
smtpSSLSessions = _SmtpSSLSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 4, 4),
    _SmtpSSLSessions_Type()
)
smtpSSLSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpSSLSessions.setStatus("current")
_SmtpOutOfThreads_Type = Integer32
_SmtpOutOfThreads_Object = MibScalar
smtpOutOfThreads = _SmtpOutOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 24534, 4, 5),
    _SmtpOutOfThreads_Type()
)
smtpOutOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpOutOfThreads.setStatus("current")
_SmtpSuccessfulAuthentications_Type = Counter64
_SmtpSuccessfulAuthentications_Object = MibScalar
smtpSuccessfulAuthentications = _SmtpSuccessfulAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 24534, 4, 6),
    _SmtpSuccessfulAuthentications_Type()
)
smtpSuccessfulAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpSuccessfulAuthentications.setStatus("current")
_SmtpSuccessfulAuthenticationsLow_Type = Counter32
_SmtpSuccessfulAuthenticationsLow_Object = MibScalar
smtpSuccessfulAuthenticationsLow = _SmtpSuccessfulAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 4, 7),
    _SmtpSuccessfulAuthenticationsLow_Type()
)
smtpSuccessfulAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpSuccessfulAuthenticationsLow.setStatus("current")
_SmtpFailedAuthentications_Type = Counter64
_SmtpFailedAuthentications_Object = MibScalar
smtpFailedAuthentications = _SmtpFailedAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 24534, 4, 8),
    _SmtpFailedAuthentications_Type()
)
smtpFailedAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpFailedAuthentications.setStatus("current")
_SmtpFailedAuthenticationsLow_Type = Counter32
_SmtpFailedAuthenticationsLow_Object = MibScalar
smtpFailedAuthenticationsLow = _SmtpFailedAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 4, 9),
    _SmtpFailedAuthenticationsLow_Type()
)
smtpFailedAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpFailedAuthenticationsLow.setStatus("current")
_GmsPOST_ObjectIdentity = ObjectIdentity
gmsPOST = _GmsPOST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24534, 5)
)
_PostThreadsTotal_Type = Integer32
_PostThreadsTotal_Object = MibScalar
postThreadsTotal = _PostThreadsTotal_Object(
    (1, 3, 6, 1, 4, 1, 24534, 5, 1),
    _PostThreadsTotal_Type()
)
postThreadsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postThreadsTotal.setStatus("current")
_PostThreadsActive_Type = Integer32
_PostThreadsActive_Object = MibScalar
postThreadsActive = _PostThreadsActive_Object(
    (1, 3, 6, 1, 4, 1, 24534, 5, 2),
    _PostThreadsActive_Type()
)
postThreadsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postThreadsActive.setStatus("current")
_PostSessions_Type = Integer32
_PostSessions_Object = MibScalar
postSessions = _PostSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 5, 3),
    _PostSessions_Type()
)
postSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postSessions.setStatus("current")
_PostSSLSessions_Type = Integer32
_PostSSLSessions_Object = MibScalar
postSSLSessions = _PostSSLSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 5, 4),
    _PostSSLSessions_Type()
)
postSSLSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postSSLSessions.setStatus("current")
_PostSuccessfulAuthentications_Type = Counter64
_PostSuccessfulAuthentications_Object = MibScalar
postSuccessfulAuthentications = _PostSuccessfulAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 24534, 5, 5),
    _PostSuccessfulAuthentications_Type()
)
postSuccessfulAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postSuccessfulAuthentications.setStatus("current")
_PostSuccessfulAuthenticationsLow_Type = Counter32
_PostSuccessfulAuthenticationsLow_Object = MibScalar
postSuccessfulAuthenticationsLow = _PostSuccessfulAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 5, 6),
    _PostSuccessfulAuthenticationsLow_Type()
)
postSuccessfulAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postSuccessfulAuthenticationsLow.setStatus("current")
_PostFailedAuthentications_Type = Counter64
_PostFailedAuthentications_Object = MibScalar
postFailedAuthentications = _PostFailedAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 24534, 5, 7),
    _PostFailedAuthentications_Type()
)
postFailedAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postFailedAuthentications.setStatus("current")
_PostFailedAuthenticationsLow_Type = Counter32
_PostFailedAuthenticationsLow_Object = MibScalar
postFailedAuthenticationsLow = _PostFailedAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 5, 8),
    _PostFailedAuthenticationsLow_Type()
)
postFailedAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postFailedAuthenticationsLow.setStatus("current")
_PostQueues_Type = Gauge32
_PostQueues_Object = MibScalar
postQueues = _PostQueues_Object(
    (1, 3, 6, 1, 4, 1, 24534, 5, 9),
    _PostQueues_Type()
)
postQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postQueues.setStatus("current")
_GmsPOP_ObjectIdentity = ObjectIdentity
gmsPOP = _GmsPOP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24534, 6)
)
_PopThreadsTotal_Type = Integer32
_PopThreadsTotal_Object = MibScalar
popThreadsTotal = _PopThreadsTotal_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 1),
    _PopThreadsTotal_Type()
)
popThreadsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popThreadsTotal.setStatus("current")
_PopThreadsActive_Type = Integer32
_PopThreadsActive_Object = MibScalar
popThreadsActive = _PopThreadsActive_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 2),
    _PopThreadsActive_Type()
)
popThreadsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popThreadsActive.setStatus("current")
_PopSessions_Type = Integer32
_PopSessions_Object = MibScalar
popSessions = _PopSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 3),
    _PopSessions_Type()
)
popSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popSessions.setStatus("current")
_PopSSLSessions_Type = Integer32
_PopSSLSessions_Object = MibScalar
popSSLSessions = _PopSSLSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 4),
    _PopSSLSessions_Type()
)
popSSLSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popSSLSessions.setStatus("current")
_PopLoggedOnUsers_Type = Integer32
_PopLoggedOnUsers_Object = MibScalar
popLoggedOnUsers = _PopLoggedOnUsers_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 5),
    _PopLoggedOnUsers_Type()
)
popLoggedOnUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popLoggedOnUsers.setStatus("current")
_PopOutOfThreads_Type = Integer32
_PopOutOfThreads_Object = MibScalar
popOutOfThreads = _PopOutOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 6),
    _PopOutOfThreads_Type()
)
popOutOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popOutOfThreads.setStatus("current")
_PopSuccessfulAuthentications_Type = Counter64
_PopSuccessfulAuthentications_Object = MibScalar
popSuccessfulAuthentications = _PopSuccessfulAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 7),
    _PopSuccessfulAuthentications_Type()
)
popSuccessfulAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popSuccessfulAuthentications.setStatus("current")
_PopSuccessfulAuthenticationsLow_Type = Counter32
_PopSuccessfulAuthenticationsLow_Object = MibScalar
popSuccessfulAuthenticationsLow = _PopSuccessfulAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 8),
    _PopSuccessfulAuthenticationsLow_Type()
)
popSuccessfulAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popSuccessfulAuthenticationsLow.setStatus("current")
_PopFailedAuthentications_Type = Counter64
_PopFailedAuthentications_Object = MibScalar
popFailedAuthentications = _PopFailedAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 9),
    _PopFailedAuthentications_Type()
)
popFailedAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popFailedAuthentications.setStatus("current")
_PopFailedAuthenticationsLow_Type = Counter32
_PopFailedAuthenticationsLow_Object = MibScalar
popFailedAuthenticationsLow = _PopFailedAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 10),
    _PopFailedAuthenticationsLow_Type()
)
popFailedAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popFailedAuthenticationsLow.setStatus("current")
_PopRetrievedVolume_Type = Counter64
_PopRetrievedVolume_Object = MibScalar
popRetrievedVolume = _PopRetrievedVolume_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 11),
    _PopRetrievedVolume_Type()
)
popRetrievedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popRetrievedVolume.setStatus("current")
_PopRetrievedVolumeLow_Type = Counter32
_PopRetrievedVolumeLow_Object = MibScalar
popRetrievedVolumeLow = _PopRetrievedVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 12),
    _PopRetrievedVolumeLow_Type()
)
popRetrievedVolumeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popRetrievedVolumeLow.setStatus("current")
_PopToppedVolume_Type = Counter64
_PopToppedVolume_Object = MibScalar
popToppedVolume = _PopToppedVolume_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 13),
    _PopToppedVolume_Type()
)
popToppedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popToppedVolume.setStatus("current")
_PopToppedVolumeLow_Type = Counter32
_PopToppedVolumeLow_Object = MibScalar
popToppedVolumeLow = _PopToppedVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 14),
    _PopToppedVolumeLow_Type()
)
popToppedVolumeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popToppedVolumeLow.setStatus("current")
_PopXmitVolume_Type = Counter64
_PopXmitVolume_Object = MibScalar
popXmitVolume = _PopXmitVolume_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 15),
    _PopXmitVolume_Type()
)
popXmitVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popXmitVolume.setStatus("current")
_PopXmitVolumeLow_Type = Counter32
_PopXmitVolumeLow_Object = MibScalar
popXmitVolumeLow = _PopXmitVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 16),
    _PopXmitVolumeLow_Type()
)
popXmitVolumeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popXmitVolumeLow.setStatus("current")
_PopDeletedMessages_Type = Counter64
_PopDeletedMessages_Object = MibScalar
popDeletedMessages = _PopDeletedMessages_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 17),
    _PopDeletedMessages_Type()
)
popDeletedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popDeletedMessages.setStatus("current")
_PopDeletedMessagesLow_Type = Counter32
_PopDeletedMessagesLow_Object = MibScalar
popDeletedMessagesLow = _PopDeletedMessagesLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 18),
    _PopDeletedMessagesLow_Type()
)
popDeletedMessagesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popDeletedMessagesLow.setStatus("current")
_PopRetrievedMessages_Type = Counter64
_PopRetrievedMessages_Object = MibScalar
popRetrievedMessages = _PopRetrievedMessages_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 19),
    _PopRetrievedMessages_Type()
)
popRetrievedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popRetrievedMessages.setStatus("current")
_PopRetrievedMessagesLow_Type = Counter32
_PopRetrievedMessagesLow_Object = MibScalar
popRetrievedMessagesLow = _PopRetrievedMessagesLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 20),
    _PopRetrievedMessagesLow_Type()
)
popRetrievedMessagesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popRetrievedMessagesLow.setStatus("current")
_PopToppedMessages_Type = Counter64
_PopToppedMessages_Object = MibScalar
popToppedMessages = _PopToppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 21),
    _PopToppedMessages_Type()
)
popToppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popToppedMessages.setStatus("current")
_PopToppedMessagesLow_Type = Counter32
_PopToppedMessagesLow_Object = MibScalar
popToppedMessagesLow = _PopToppedMessagesLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 22),
    _PopToppedMessagesLow_Type()
)
popToppedMessagesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popToppedMessagesLow.setStatus("current")
_PopXmitedMessages_Type = Counter64
_PopXmitedMessages_Object = MibScalar
popXmitedMessages = _PopXmitedMessages_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 23),
    _PopXmitedMessages_Type()
)
popXmitedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popXmitedMessages.setStatus("current")
_PopXmitedMessagesLow_Type = Counter32
_PopXmitedMessagesLow_Object = MibScalar
popXmitedMessagesLow = _PopXmitedMessagesLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 24),
    _PopXmitedMessagesLow_Type()
)
popXmitedMessagesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popXmitedMessagesLow.setStatus("current")
_PopLastInboundActivity_Type = TimeInterval
_PopLastInboundActivity_Object = MibScalar
popLastInboundActivity = _PopLastInboundActivity_Object(
    (1, 3, 6, 1, 4, 1, 24534, 6, 25),
    _PopLastInboundActivity_Type()
)
popLastInboundActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popLastInboundActivity.setStatus("current")
_GmsIMAP_ObjectIdentity = ObjectIdentity
gmsIMAP = _GmsIMAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24534, 7)
)
_ImapThreadsTotal_Type = Integer32
_ImapThreadsTotal_Object = MibScalar
imapThreadsTotal = _ImapThreadsTotal_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 1),
    _ImapThreadsTotal_Type()
)
imapThreadsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapThreadsTotal.setStatus("current")
_ImapThreadsActive_Type = Integer32
_ImapThreadsActive_Object = MibScalar
imapThreadsActive = _ImapThreadsActive_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 2),
    _ImapThreadsActive_Type()
)
imapThreadsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapThreadsActive.setStatus("current")
_ImapSessions_Type = Integer32
_ImapSessions_Object = MibScalar
imapSessions = _ImapSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 3),
    _ImapSessions_Type()
)
imapSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapSessions.setStatus("current")
_ImapSSLSessions_Type = Integer32
_ImapSSLSessions_Object = MibScalar
imapSSLSessions = _ImapSSLSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 4),
    _ImapSSLSessions_Type()
)
imapSSLSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapSSLSessions.setStatus("current")
_ImapIdleSessions_Type = Integer32
_ImapIdleSessions_Object = MibScalar
imapIdleSessions = _ImapIdleSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 5),
    _ImapIdleSessions_Type()
)
imapIdleSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapIdleSessions.setStatus("current")
_ImapLoggedOnUsers_Type = Integer32
_ImapLoggedOnUsers_Object = MibScalar
imapLoggedOnUsers = _ImapLoggedOnUsers_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 6),
    _ImapLoggedOnUsers_Type()
)
imapLoggedOnUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapLoggedOnUsers.setStatus("current")
_ImapOutOfThreads_Type = Integer32
_ImapOutOfThreads_Object = MibScalar
imapOutOfThreads = _ImapOutOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 7),
    _ImapOutOfThreads_Type()
)
imapOutOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapOutOfThreads.setStatus("current")
_ImapSuccessfulAuthentications_Type = Counter64
_ImapSuccessfulAuthentications_Object = MibScalar
imapSuccessfulAuthentications = _ImapSuccessfulAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 8),
    _ImapSuccessfulAuthentications_Type()
)
imapSuccessfulAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapSuccessfulAuthentications.setStatus("current")
_ImapSuccessfulAuthenticationsLow_Type = Counter32
_ImapSuccessfulAuthenticationsLow_Object = MibScalar
imapSuccessfulAuthenticationsLow = _ImapSuccessfulAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 9),
    _ImapSuccessfulAuthenticationsLow_Type()
)
imapSuccessfulAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapSuccessfulAuthenticationsLow.setStatus("current")
_ImapFailedAuthentications_Type = Counter64
_ImapFailedAuthentications_Object = MibScalar
imapFailedAuthentications = _ImapFailedAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 10),
    _ImapFailedAuthentications_Type()
)
imapFailedAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapFailedAuthentications.setStatus("current")
_ImapFailedAuthenticationsLow_Type = Counter32
_ImapFailedAuthenticationsLow_Object = MibScalar
imapFailedAuthenticationsLow = _ImapFailedAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 11),
    _ImapFailedAuthenticationsLow_Type()
)
imapFailedAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapFailedAuthenticationsLow.setStatus("current")
_ImapDeletedMessages_Type = Counter64
_ImapDeletedMessages_Object = MibScalar
imapDeletedMessages = _ImapDeletedMessages_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 12),
    _ImapDeletedMessages_Type()
)
imapDeletedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapDeletedMessages.setStatus("current")
_ImapDeletedMessagesLow_Type = Counter32
_ImapDeletedMessagesLow_Object = MibScalar
imapDeletedMessagesLow = _ImapDeletedMessagesLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 13),
    _ImapDeletedMessagesLow_Type()
)
imapDeletedMessagesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapDeletedMessagesLow.setStatus("current")
_ImapStoredMessages_Type = Counter64
_ImapStoredMessages_Object = MibScalar
imapStoredMessages = _ImapStoredMessages_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 14),
    _ImapStoredMessages_Type()
)
imapStoredMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapStoredMessages.setStatus("current")
_ImapStoredMessagesLow_Type = Counter32
_ImapStoredMessagesLow_Object = MibScalar
imapStoredMessagesLow = _ImapStoredMessagesLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 15),
    _ImapStoredMessagesLow_Type()
)
imapStoredMessagesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapStoredMessagesLow.setStatus("current")
_ImapAppendedMessages_Type = Counter64
_ImapAppendedMessages_Object = MibScalar
imapAppendedMessages = _ImapAppendedMessages_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 16),
    _ImapAppendedMessages_Type()
)
imapAppendedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapAppendedMessages.setStatus("current")
_ImapAppendedMessagesLow_Type = Counter32
_ImapAppendedMessagesLow_Object = MibScalar
imapAppendedMessagesLow = _ImapAppendedMessagesLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 17),
    _ImapAppendedMessagesLow_Type()
)
imapAppendedMessagesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapAppendedMessagesLow.setStatus("current")
_ImapAppendedVolume_Type = Counter64
_ImapAppendedVolume_Object = MibScalar
imapAppendedVolume = _ImapAppendedVolume_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 18),
    _ImapAppendedVolume_Type()
)
imapAppendedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapAppendedVolume.setStatus("current")
_ImapAppendedVolumeLow_Type = Counter32
_ImapAppendedVolumeLow_Object = MibScalar
imapAppendedVolumeLow = _ImapAppendedVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 19),
    _ImapAppendedVolumeLow_Type()
)
imapAppendedVolumeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapAppendedVolumeLow.setStatus("current")
_ImapFetchedMessages_Type = Counter64
_ImapFetchedMessages_Object = MibScalar
imapFetchedMessages = _ImapFetchedMessages_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 20),
    _ImapFetchedMessages_Type()
)
imapFetchedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapFetchedMessages.setStatus("current")
_ImapFetchedMessagesLow_Type = Counter32
_ImapFetchedMessagesLow_Object = MibScalar
imapFetchedMessagesLow = _ImapFetchedMessagesLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 21),
    _ImapFetchedMessagesLow_Type()
)
imapFetchedMessagesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapFetchedMessagesLow.setStatus("current")
_ImapFetchedVolume_Type = Counter64
_ImapFetchedVolume_Object = MibScalar
imapFetchedVolume = _ImapFetchedVolume_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 22),
    _ImapFetchedVolume_Type()
)
imapFetchedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapFetchedVolume.setStatus("current")
_ImapFetchedVolumeLow_Type = Counter32
_ImapFetchedVolumeLow_Object = MibScalar
imapFetchedVolumeLow = _ImapFetchedVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 23),
    _ImapFetchedVolumeLow_Type()
)
imapFetchedVolumeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapFetchedVolumeLow.setStatus("current")
_ImapCopiedMessages_Type = Counter64
_ImapCopiedMessages_Object = MibScalar
imapCopiedMessages = _ImapCopiedMessages_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 24),
    _ImapCopiedMessages_Type()
)
imapCopiedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapCopiedMessages.setStatus("current")
_ImapCopiedMessagesLow_Type = Counter32
_ImapCopiedMessagesLow_Object = MibScalar
imapCopiedMessagesLow = _ImapCopiedMessagesLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 25),
    _ImapCopiedMessagesLow_Type()
)
imapCopiedMessagesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapCopiedMessagesLow.setStatus("current")
_ImapSearchedMessages_Type = Counter64
_ImapSearchedMessages_Object = MibScalar
imapSearchedMessages = _ImapSearchedMessages_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 26),
    _ImapSearchedMessages_Type()
)
imapSearchedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapSearchedMessages.setStatus("current")
_ImapSearchedMessagesLow_Type = Counter32
_ImapSearchedMessagesLow_Object = MibScalar
imapSearchedMessagesLow = _ImapSearchedMessagesLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 27),
    _ImapSearchedMessagesLow_Type()
)
imapSearchedMessagesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapSearchedMessagesLow.setStatus("current")
_ImapLastInboundActivity_Type = TimeInterval
_ImapLastInboundActivity_Object = MibScalar
imapLastInboundActivity = _ImapLastInboundActivity_Object(
    (1, 3, 6, 1, 4, 1, 24534, 7, 28),
    _ImapLastInboundActivity_Type()
)
imapLastInboundActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imapLastInboundActivity.setStatus("current")
_GmsWWW_ObjectIdentity = ObjectIdentity
gmsWWW = _GmsWWW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24534, 8)
)
_WwwThreadsTotal_Type = Integer32
_WwwThreadsTotal_Object = MibScalar
wwwThreadsTotal = _WwwThreadsTotal_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 1),
    _WwwThreadsTotal_Type()
)
wwwThreadsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwThreadsTotal.setStatus("current")
_WwwThreadsActive_Type = Integer32
_WwwThreadsActive_Object = MibScalar
wwwThreadsActive = _WwwThreadsActive_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 2),
    _WwwThreadsActive_Type()
)
wwwThreadsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwThreadsActive.setStatus("current")
_WwwSessions_Type = Integer32
_WwwSessions_Object = MibScalar
wwwSessions = _WwwSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 3),
    _WwwSessions_Type()
)
wwwSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSessions.setStatus("current")
_WwwProxySessions_Type = Integer32
_WwwProxySessions_Object = MibScalar
wwwProxySessions = _WwwProxySessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 4),
    _WwwProxySessions_Type()
)
wwwProxySessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwProxySessions.setStatus("current")
_WwwScriptSessions_Type = Integer32
_WwwScriptSessions_Object = MibScalar
wwwScriptSessions = _WwwScriptSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 5),
    _WwwScriptSessions_Type()
)
wwwScriptSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwScriptSessions.setStatus("current")
_WwwConnections_Type = Integer32
_WwwConnections_Object = MibScalar
wwwConnections = _WwwConnections_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 6),
    _WwwConnections_Type()
)
wwwConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwConnections.setStatus("current")
_WwwSSLConnections_Type = Integer32
_WwwSSLConnections_Object = MibScalar
wwwSSLConnections = _WwwSSLConnections_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 7),
    _WwwSSLConnections_Type()
)
wwwSSLConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSSLConnections.setStatus("current")
_WwwProxyConnections_Type = Integer32
_WwwProxyConnections_Object = MibScalar
wwwProxyConnections = _WwwProxyConnections_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 8),
    _WwwProxyConnections_Type()
)
wwwProxyConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwProxyConnections.setStatus("current")
_WwwProxySSLConnections_Type = Integer32
_WwwProxySSLConnections_Object = MibScalar
wwwProxySSLConnections = _WwwProxySSLConnections_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 9),
    _WwwProxySSLConnections_Type()
)
wwwProxySSLConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwProxySSLConnections.setStatus("current")
_WwwScriptConnections_Type = Integer32
_WwwScriptConnections_Object = MibScalar
wwwScriptConnections = _WwwScriptConnections_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 10),
    _WwwScriptConnections_Type()
)
wwwScriptConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwScriptConnections.setStatus("current")
_WwwLoggedOnUsers_Type = Integer32
_WwwLoggedOnUsers_Object = MibScalar
wwwLoggedOnUsers = _WwwLoggedOnUsers_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 11),
    _WwwLoggedOnUsers_Type()
)
wwwLoggedOnUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwLoggedOnUsers.setStatus("current")
_WwwOutOfThreads_Type = Integer32
_WwwOutOfThreads_Object = MibScalar
wwwOutOfThreads = _WwwOutOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 12),
    _WwwOutOfThreads_Type()
)
wwwOutOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwOutOfThreads.setStatus("current")
_WwwOutOfSessions_Type = Integer32
_WwwOutOfSessions_Object = MibScalar
wwwOutOfSessions = _WwwOutOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 13),
    _WwwOutOfSessions_Type()
)
wwwOutOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwOutOfSessions.setStatus("current")
_WwwOutOfProxySessions_Type = Integer32
_WwwOutOfProxySessions_Object = MibScalar
wwwOutOfProxySessions = _WwwOutOfProxySessions_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 14),
    _WwwOutOfProxySessions_Type()
)
wwwOutOfProxySessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwOutOfProxySessions.setStatus("current")
_WwwSessionTimeouts_Type = Counter64
_WwwSessionTimeouts_Object = MibScalar
wwwSessionTimeouts = _WwwSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 15),
    _WwwSessionTimeouts_Type()
)
wwwSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSessionTimeouts.setStatus("current")
_WwwSessionTimeoutsLow_Type = Counter32
_WwwSessionTimeoutsLow_Object = MibScalar
wwwSessionTimeoutsLow = _WwwSessionTimeoutsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 16),
    _WwwSessionTimeoutsLow_Type()
)
wwwSessionTimeoutsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSessionTimeoutsLow.setStatus("current")
_WwwProxySessionTimeouts_Type = Counter64
_WwwProxySessionTimeouts_Object = MibScalar
wwwProxySessionTimeouts = _WwwProxySessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 17),
    _WwwProxySessionTimeouts_Type()
)
wwwProxySessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwProxySessionTimeouts.setStatus("current")
_WwwProxySessionTimeoutsLow_Type = Counter32
_WwwProxySessionTimeoutsLow_Object = MibScalar
wwwProxySessionTimeoutsLow = _WwwProxySessionTimeoutsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 18),
    _WwwProxySessionTimeoutsLow_Type()
)
wwwProxySessionTimeoutsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwProxySessionTimeoutsLow.setStatus("current")
_WwwScriptSessionTimeouts_Type = Counter64
_WwwScriptSessionTimeouts_Object = MibScalar
wwwScriptSessionTimeouts = _WwwScriptSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 19),
    _WwwScriptSessionTimeouts_Type()
)
wwwScriptSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwScriptSessionTimeouts.setStatus("current")
_WwwScriptSessionTimeoutsLow_Type = Counter32
_WwwScriptSessionTimeoutsLow_Object = MibScalar
wwwScriptSessionTimeoutsLow = _WwwScriptSessionTimeoutsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 20),
    _WwwScriptSessionTimeoutsLow_Type()
)
wwwScriptSessionTimeoutsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwScriptSessionTimeoutsLow.setStatus("current")
_WwwSuccessfulAuthentications_Type = Counter64
_WwwSuccessfulAuthentications_Object = MibScalar
wwwSuccessfulAuthentications = _WwwSuccessfulAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 21),
    _WwwSuccessfulAuthentications_Type()
)
wwwSuccessfulAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulAuthentications.setStatus("current")
_WwwSuccessfulAuthenticationsLow_Type = Counter32
_WwwSuccessfulAuthenticationsLow_Object = MibScalar
wwwSuccessfulAuthenticationsLow = _WwwSuccessfulAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 22),
    _WwwSuccessfulAuthenticationsLow_Type()
)
wwwSuccessfulAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulAuthenticationsLow.setStatus("current")
_WwwFailedAuthentications_Type = Counter64
_WwwFailedAuthentications_Object = MibScalar
wwwFailedAuthentications = _WwwFailedAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 23),
    _WwwFailedAuthentications_Type()
)
wwwFailedAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedAuthentications.setStatus("current")
_WwwFailedAuthenticationsLow_Type = Counter32
_WwwFailedAuthenticationsLow_Object = MibScalar
wwwFailedAuthenticationsLow = _WwwFailedAuthenticationsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 24),
    _WwwFailedAuthenticationsLow_Type()
)
wwwFailedAuthenticationsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedAuthenticationsLow.setStatus("current")
_WwwReceivedVolume_Type = Counter64
_WwwReceivedVolume_Object = MibScalar
wwwReceivedVolume = _WwwReceivedVolume_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 25),
    _WwwReceivedVolume_Type()
)
wwwReceivedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwReceivedVolume.setStatus("current")
_WwwReceivedVolumeLow_Type = Counter32
_WwwReceivedVolumeLow_Object = MibScalar
wwwReceivedVolumeLow = _WwwReceivedVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 26),
    _WwwReceivedVolumeLow_Type()
)
wwwReceivedVolumeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwReceivedVolumeLow.setStatus("current")
_WwwTransmittedVolume_Type = Counter64
_WwwTransmittedVolume_Object = MibScalar
wwwTransmittedVolume = _WwwTransmittedVolume_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 27),
    _WwwTransmittedVolume_Type()
)
wwwTransmittedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwTransmittedVolume.setStatus("current")
_WwwTransmittedVolumeLow_Type = Counter32
_WwwTransmittedVolumeLow_Object = MibScalar
wwwTransmittedVolumeLow = _WwwTransmittedVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 28),
    _WwwTransmittedVolumeLow_Type()
)
wwwTransmittedVolumeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwTransmittedVolumeLow.setStatus("current")
_WwwProxyReceivedVolume_Type = Counter64
_WwwProxyReceivedVolume_Object = MibScalar
wwwProxyReceivedVolume = _WwwProxyReceivedVolume_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 29),
    _WwwProxyReceivedVolume_Type()
)
wwwProxyReceivedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwProxyReceivedVolume.setStatus("current")
_WwwProxyReceivedVolumeLow_Type = Counter32
_WwwProxyReceivedVolumeLow_Object = MibScalar
wwwProxyReceivedVolumeLow = _WwwProxyReceivedVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 30),
    _WwwProxyReceivedVolumeLow_Type()
)
wwwProxyReceivedVolumeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwProxyReceivedVolumeLow.setStatus("current")
_WwwProxyTransmittedVolume_Type = Counter64
_WwwProxyTransmittedVolume_Object = MibScalar
wwwProxyTransmittedVolume = _WwwProxyTransmittedVolume_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 31),
    _WwwProxyTransmittedVolume_Type()
)
wwwProxyTransmittedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwProxyTransmittedVolume.setStatus("current")
_WwwProxyTransmittedVolumeLow_Type = Counter32
_WwwProxyTransmittedVolumeLow_Object = MibScalar
wwwProxyTransmittedVolumeLow = _WwwProxyTransmittedVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 32),
    _WwwProxyTransmittedVolumeLow_Type()
)
wwwProxyTransmittedVolumeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwProxyTransmittedVolumeLow.setStatus("current")
_WwwReverseProxyReceivedVolume_Type = Counter64
_WwwReverseProxyReceivedVolume_Object = MibScalar
wwwReverseProxyReceivedVolume = _WwwReverseProxyReceivedVolume_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 33),
    _WwwReverseProxyReceivedVolume_Type()
)
wwwReverseProxyReceivedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwReverseProxyReceivedVolume.setStatus("current")
_WwwReverseProxyReceivedVolumeLow_Type = Counter32
_WwwReverseProxyReceivedVolumeLow_Object = MibScalar
wwwReverseProxyReceivedVolumeLow = _WwwReverseProxyReceivedVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 34),
    _WwwReverseProxyReceivedVolumeLow_Type()
)
wwwReverseProxyReceivedVolumeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwReverseProxyReceivedVolumeLow.setStatus("current")
_WwwReverseProxyTransmittedVolume_Type = Counter64
_WwwReverseProxyTransmittedVolume_Object = MibScalar
wwwReverseProxyTransmittedVolume = _WwwReverseProxyTransmittedVolume_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 35),
    _WwwReverseProxyTransmittedVolume_Type()
)
wwwReverseProxyTransmittedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwReverseProxyTransmittedVolume.setStatus("current")
_WwwReverseProxyTransmittedVolumeLow_Type = Counter32
_WwwReverseProxyTransmittedVolumeLow_Object = MibScalar
wwwReverseProxyTransmittedVolumeLow = _WwwReverseProxyTransmittedVolumeLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 36),
    _WwwReverseProxyTransmittedVolumeLow_Type()
)
wwwReverseProxyTransmittedVolumeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwReverseProxyTransmittedVolumeLow.setStatus("current")
_WwwSuccessfulRequests_Type = Counter64
_WwwSuccessfulRequests_Object = MibScalar
wwwSuccessfulRequests = _WwwSuccessfulRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 37),
    _WwwSuccessfulRequests_Type()
)
wwwSuccessfulRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulRequests.setStatus("current")
_WwwSuccessfulRequestsLow_Type = Counter32
_WwwSuccessfulRequestsLow_Object = MibScalar
wwwSuccessfulRequestsLow = _WwwSuccessfulRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 38),
    _WwwSuccessfulRequestsLow_Type()
)
wwwSuccessfulRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulRequestsLow.setStatus("current")
_WwwFailedRequests_Type = Counter64
_WwwFailedRequests_Object = MibScalar
wwwFailedRequests = _WwwFailedRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 39),
    _WwwFailedRequests_Type()
)
wwwFailedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedRequests.setStatus("current")
_WwwFailedRequestsLow_Type = Counter32
_WwwFailedRequestsLow_Object = MibScalar
wwwFailedRequestsLow = _WwwFailedRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 40),
    _WwwFailedRequestsLow_Type()
)
wwwFailedRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedRequestsLow.setStatus("current")
_WwwSuccessfulAdminRequests_Type = Counter64
_WwwSuccessfulAdminRequests_Object = MibScalar
wwwSuccessfulAdminRequests = _WwwSuccessfulAdminRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 41),
    _WwwSuccessfulAdminRequests_Type()
)
wwwSuccessfulAdminRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulAdminRequests.setStatus("current")
_WwwSuccessfulAdminRequestsLow_Type = Counter32
_WwwSuccessfulAdminRequestsLow_Object = MibScalar
wwwSuccessfulAdminRequestsLow = _WwwSuccessfulAdminRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 42),
    _WwwSuccessfulAdminRequestsLow_Type()
)
wwwSuccessfulAdminRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulAdminRequestsLow.setStatus("current")
_WwwFailedAdminRequests_Type = Counter64
_WwwFailedAdminRequests_Object = MibScalar
wwwFailedAdminRequests = _WwwFailedAdminRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 43),
    _WwwFailedAdminRequests_Type()
)
wwwFailedAdminRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedAdminRequests.setStatus("current")
_WwwFailedAdminRequestsLow_Type = Counter32
_WwwFailedAdminRequestsLow_Object = MibScalar
wwwFailedAdminRequestsLow = _WwwFailedAdminRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 44),
    _WwwFailedAdminRequestsLow_Type()
)
wwwFailedAdminRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedAdminRequestsLow.setStatus("current")
_WwwSuccessfulWebmailRequests_Type = Counter64
_WwwSuccessfulWebmailRequests_Object = MibScalar
wwwSuccessfulWebmailRequests = _WwwSuccessfulWebmailRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 45),
    _WwwSuccessfulWebmailRequests_Type()
)
wwwSuccessfulWebmailRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulWebmailRequests.setStatus("current")
_WwwSuccessfulWebmailRequestsLow_Type = Counter32
_WwwSuccessfulWebmailRequestsLow_Object = MibScalar
wwwSuccessfulWebmailRequestsLow = _WwwSuccessfulWebmailRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 46),
    _WwwSuccessfulWebmailRequestsLow_Type()
)
wwwSuccessfulWebmailRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulWebmailRequestsLow.setStatus("current")
_WwwFailedWebmailRequests_Type = Counter64
_WwwFailedWebmailRequests_Object = MibScalar
wwwFailedWebmailRequests = _WwwFailedWebmailRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 47),
    _WwwFailedWebmailRequests_Type()
)
wwwFailedWebmailRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedWebmailRequests.setStatus("current")
_WwwFailedWebmailRequestsLow_Type = Counter32
_WwwFailedWebmailRequestsLow_Object = MibScalar
wwwFailedWebmailRequestsLow = _WwwFailedWebmailRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 48),
    _WwwFailedWebmailRequestsLow_Type()
)
wwwFailedWebmailRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedWebmailRequestsLow.setStatus("current")
_WwwSuccessfulUserRequests_Type = Counter64
_WwwSuccessfulUserRequests_Object = MibScalar
wwwSuccessfulUserRequests = _WwwSuccessfulUserRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 49),
    _WwwSuccessfulUserRequests_Type()
)
wwwSuccessfulUserRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulUserRequests.setStatus("current")
_WwwSuccessfulUserRequestsLow_Type = Counter32
_WwwSuccessfulUserRequestsLow_Object = MibScalar
wwwSuccessfulUserRequestsLow = _WwwSuccessfulUserRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 50),
    _WwwSuccessfulUserRequestsLow_Type()
)
wwwSuccessfulUserRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulUserRequestsLow.setStatus("current")
_WwwFailedUserRequests_Type = Counter64
_WwwFailedUserRequests_Object = MibScalar
wwwFailedUserRequests = _WwwFailedUserRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 51),
    _WwwFailedUserRequests_Type()
)
wwwFailedUserRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedUserRequests.setStatus("current")
_WwwFailedUserRequestsLow_Type = Counter32
_WwwFailedUserRequestsLow_Object = MibScalar
wwwFailedUserRequestsLow = _WwwFailedUserRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 52),
    _WwwFailedUserRequestsLow_Type()
)
wwwFailedUserRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedUserRequestsLow.setStatus("current")
_WwwSuccessfulProxyRequests_Type = Counter64
_WwwSuccessfulProxyRequests_Object = MibScalar
wwwSuccessfulProxyRequests = _WwwSuccessfulProxyRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 53),
    _WwwSuccessfulProxyRequests_Type()
)
wwwSuccessfulProxyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulProxyRequests.setStatus("current")
_WwwSuccessfulProxyRequestsLow_Type = Counter32
_WwwSuccessfulProxyRequestsLow_Object = MibScalar
wwwSuccessfulProxyRequestsLow = _WwwSuccessfulProxyRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 54),
    _WwwSuccessfulProxyRequestsLow_Type()
)
wwwSuccessfulProxyRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulProxyRequestsLow.setStatus("current")
_WwwFailedProxyRequests_Type = Counter64
_WwwFailedProxyRequests_Object = MibScalar
wwwFailedProxyRequests = _WwwFailedProxyRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 55),
    _WwwFailedProxyRequests_Type()
)
wwwFailedProxyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedProxyRequests.setStatus("current")
_WwwFailedProxyRequestsLow_Type = Counter32
_WwwFailedProxyRequestsLow_Object = MibScalar
wwwFailedProxyRequestsLow = _WwwFailedProxyRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 56),
    _WwwFailedProxyRequestsLow_Type()
)
wwwFailedProxyRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedProxyRequestsLow.setStatus("current")
_WwwSuccessfulReverseProxyRequests_Type = Counter64
_WwwSuccessfulReverseProxyRequests_Object = MibScalar
wwwSuccessfulReverseProxyRequests = _WwwSuccessfulReverseProxyRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 57),
    _WwwSuccessfulReverseProxyRequests_Type()
)
wwwSuccessfulReverseProxyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulReverseProxyRequests.setStatus("current")
_WwwSuccessfulReverseProxyRequestsLow_Type = Counter32
_WwwSuccessfulReverseProxyRequestsLow_Object = MibScalar
wwwSuccessfulReverseProxyRequestsLow = _WwwSuccessfulReverseProxyRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 58),
    _WwwSuccessfulReverseProxyRequestsLow_Type()
)
wwwSuccessfulReverseProxyRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulReverseProxyRequestsLow.setStatus("current")
_WwwFailedReverseProxyRequests_Type = Counter64
_WwwFailedReverseProxyRequests_Object = MibScalar
wwwFailedReverseProxyRequests = _WwwFailedReverseProxyRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 59),
    _WwwFailedReverseProxyRequests_Type()
)
wwwFailedReverseProxyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedReverseProxyRequests.setStatus("current")
_WwwFailedReverseProxyRequestsLow_Type = Counter32
_WwwFailedReverseProxyRequestsLow_Object = MibScalar
wwwFailedReverseProxyRequestsLow = _WwwFailedReverseProxyRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 60),
    _WwwFailedReverseProxyRequestsLow_Type()
)
wwwFailedReverseProxyRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedReverseProxyRequestsLow.setStatus("current")
_WwwSuccessfulScriptRequests_Type = Counter64
_WwwSuccessfulScriptRequests_Object = MibScalar
wwwSuccessfulScriptRequests = _WwwSuccessfulScriptRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 61),
    _WwwSuccessfulScriptRequests_Type()
)
wwwSuccessfulScriptRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulScriptRequests.setStatus("current")
_WwwSuccessfulScriptRequestsLow_Type = Counter32
_WwwSuccessfulScriptRequestsLow_Object = MibScalar
wwwSuccessfulScriptRequestsLow = _WwwSuccessfulScriptRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 62),
    _WwwSuccessfulScriptRequestsLow_Type()
)
wwwSuccessfulScriptRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulScriptRequestsLow.setStatus("current")
_WwwFailedScriptRequests_Type = Counter64
_WwwFailedScriptRequests_Object = MibScalar
wwwFailedScriptRequests = _WwwFailedScriptRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 63),
    _WwwFailedScriptRequests_Type()
)
wwwFailedScriptRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedScriptRequests.setStatus("current")
_WwwFailedScriptRequestsLow_Type = Counter32
_WwwFailedScriptRequestsLow_Object = MibScalar
wwwFailedScriptRequestsLow = _WwwFailedScriptRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 64),
    _WwwFailedScriptRequestsLow_Type()
)
wwwFailedScriptRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedScriptRequestsLow.setStatus("current")
_WwwSuccessfulTimedRequests_Type = Counter64
_WwwSuccessfulTimedRequests_Object = MibScalar
wwwSuccessfulTimedRequests = _WwwSuccessfulTimedRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 65),
    _WwwSuccessfulTimedRequests_Type()
)
wwwSuccessfulTimedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulTimedRequests.setStatus("current")
_WwwSuccessfulTimedRequestsLow_Type = Counter32
_WwwSuccessfulTimedRequestsLow_Object = MibScalar
wwwSuccessfulTimedRequestsLow = _WwwSuccessfulTimedRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 66),
    _WwwSuccessfulTimedRequestsLow_Type()
)
wwwSuccessfulTimedRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSuccessfulTimedRequestsLow.setStatus("current")
_WwwFailedTimedRequests_Type = Counter64
_WwwFailedTimedRequests_Object = MibScalar
wwwFailedTimedRequests = _WwwFailedTimedRequests_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 67),
    _WwwFailedTimedRequests_Type()
)
wwwFailedTimedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedTimedRequests.setStatus("current")
_WwwFailedTimedRequestsLow_Type = Counter32
_WwwFailedTimedRequestsLow_Object = MibScalar
wwwFailedTimedRequestsLow = _WwwFailedTimedRequestsLow_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 68),
    _WwwFailedTimedRequestsLow_Type()
)
wwwFailedTimedRequestsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwFailedTimedRequestsLow.setStatus("current")
_WwwMMLErrors_Type = Integer32
_WwwMMLErrors_Object = MibScalar
wwwMMLErrors = _WwwMMLErrors_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 69),
    _WwwMMLErrors_Type()
)
wwwMMLErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwMMLErrors.setStatus("current")
_WwwMessagesRead_Type = Integer32
_WwwMessagesRead_Object = MibScalar
wwwMessagesRead = _WwwMessagesRead_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 70),
    _WwwMessagesRead_Type()
)
wwwMessagesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwMessagesRead.setStatus("current")
_WwwMessagesSent_Type = Integer32
_WwwMessagesSent_Object = MibScalar
wwwMessagesSent = _WwwMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 71),
    _WwwMessagesSent_Type()
)
wwwMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwMessagesSent.setStatus("current")
_WwwLastInboundActivity_Type = TimeInterval
_WwwLastInboundActivity_Object = MibScalar
wwwLastInboundActivity = _WwwLastInboundActivity_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 72),
    _WwwLastInboundActivity_Type()
)
wwwLastInboundActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwLastInboundActivity.setStatus("current")
_WwwLastOutboundActivity_Type = TimeInterval
_WwwLastOutboundActivity_Object = MibScalar
wwwLastOutboundActivity = _WwwLastOutboundActivity_Object(
    (1, 3, 6, 1, 4, 1, 24534, 8, 73),
    _WwwLastOutboundActivity_Type()
)
wwwLastOutboundActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwLastOutboundActivity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GMS-MIB",
    **{"gordano": gordano,
       "gmsApplTable": gmsApplTable,
       "gmsApplEntry": gmsApplEntry,
       "applHandleCount": applHandleCount,
       "applPercentCPU": applPercentCPU,
       "applRssKB": applRssKB,
       "gmsAV": gmsAV,
       "avEngineVersion": avEngineVersion,
       "avLastUpdate": avLastUpdate,
       "avMessagesScanned": avMessagesScanned,
       "avMessagesScannedLow": avMessagesScannedLow,
       "avVirusesFound": avVirusesFound,
       "avVirusesFoundLow": avVirusesFoundLow,
       "gmsAS": gmsAS,
       "asLastUpdate": asLastUpdate,
       "asMessagesChecked": asMessagesChecked,
       "asMessagesCheckedLow": asMessagesCheckedLow,
       "asMessagesRejected": asMessagesRejected,
       "asMessagesRejectedLow": asMessagesRejectedLow,
       "gmsSMTP": gmsSMTP,
       "smtpThreadsTotal": smtpThreadsTotal,
       "smtpThreadsActive": smtpThreadsActive,
       "smtpSessions": smtpSessions,
       "smtpSSLSessions": smtpSSLSessions,
       "smtpOutOfThreads": smtpOutOfThreads,
       "smtpSuccessfulAuthentications": smtpSuccessfulAuthentications,
       "smtpSuccessfulAuthenticationsLow": smtpSuccessfulAuthenticationsLow,
       "smtpFailedAuthentications": smtpFailedAuthentications,
       "smtpFailedAuthenticationsLow": smtpFailedAuthenticationsLow,
       "gmsPOST": gmsPOST,
       "postThreadsTotal": postThreadsTotal,
       "postThreadsActive": postThreadsActive,
       "postSessions": postSessions,
       "postSSLSessions": postSSLSessions,
       "postSuccessfulAuthentications": postSuccessfulAuthentications,
       "postSuccessfulAuthenticationsLow": postSuccessfulAuthenticationsLow,
       "postFailedAuthentications": postFailedAuthentications,
       "postFailedAuthenticationsLow": postFailedAuthenticationsLow,
       "postQueues": postQueues,
       "gmsPOP": gmsPOP,
       "popThreadsTotal": popThreadsTotal,
       "popThreadsActive": popThreadsActive,
       "popSessions": popSessions,
       "popSSLSessions": popSSLSessions,
       "popLoggedOnUsers": popLoggedOnUsers,
       "popOutOfThreads": popOutOfThreads,
       "popSuccessfulAuthentications": popSuccessfulAuthentications,
       "popSuccessfulAuthenticationsLow": popSuccessfulAuthenticationsLow,
       "popFailedAuthentications": popFailedAuthentications,
       "popFailedAuthenticationsLow": popFailedAuthenticationsLow,
       "popRetrievedVolume": popRetrievedVolume,
       "popRetrievedVolumeLow": popRetrievedVolumeLow,
       "popToppedVolume": popToppedVolume,
       "popToppedVolumeLow": popToppedVolumeLow,
       "popXmitVolume": popXmitVolume,
       "popXmitVolumeLow": popXmitVolumeLow,
       "popDeletedMessages": popDeletedMessages,
       "popDeletedMessagesLow": popDeletedMessagesLow,
       "popRetrievedMessages": popRetrievedMessages,
       "popRetrievedMessagesLow": popRetrievedMessagesLow,
       "popToppedMessages": popToppedMessages,
       "popToppedMessagesLow": popToppedMessagesLow,
       "popXmitedMessages": popXmitedMessages,
       "popXmitedMessagesLow": popXmitedMessagesLow,
       "popLastInboundActivity": popLastInboundActivity,
       "gmsIMAP": gmsIMAP,
       "imapThreadsTotal": imapThreadsTotal,
       "imapThreadsActive": imapThreadsActive,
       "imapSessions": imapSessions,
       "imapSSLSessions": imapSSLSessions,
       "imapIdleSessions": imapIdleSessions,
       "imapLoggedOnUsers": imapLoggedOnUsers,
       "imapOutOfThreads": imapOutOfThreads,
       "imapSuccessfulAuthentications": imapSuccessfulAuthentications,
       "imapSuccessfulAuthenticationsLow": imapSuccessfulAuthenticationsLow,
       "imapFailedAuthentications": imapFailedAuthentications,
       "imapFailedAuthenticationsLow": imapFailedAuthenticationsLow,
       "imapDeletedMessages": imapDeletedMessages,
       "imapDeletedMessagesLow": imapDeletedMessagesLow,
       "imapStoredMessages": imapStoredMessages,
       "imapStoredMessagesLow": imapStoredMessagesLow,
       "imapAppendedMessages": imapAppendedMessages,
       "imapAppendedMessagesLow": imapAppendedMessagesLow,
       "imapAppendedVolume": imapAppendedVolume,
       "imapAppendedVolumeLow": imapAppendedVolumeLow,
       "imapFetchedMessages": imapFetchedMessages,
       "imapFetchedMessagesLow": imapFetchedMessagesLow,
       "imapFetchedVolume": imapFetchedVolume,
       "imapFetchedVolumeLow": imapFetchedVolumeLow,
       "imapCopiedMessages": imapCopiedMessages,
       "imapCopiedMessagesLow": imapCopiedMessagesLow,
       "imapSearchedMessages": imapSearchedMessages,
       "imapSearchedMessagesLow": imapSearchedMessagesLow,
       "imapLastInboundActivity": imapLastInboundActivity,
       "gmsWWW": gmsWWW,
       "wwwThreadsTotal": wwwThreadsTotal,
       "wwwThreadsActive": wwwThreadsActive,
       "wwwSessions": wwwSessions,
       "wwwProxySessions": wwwProxySessions,
       "wwwScriptSessions": wwwScriptSessions,
       "wwwConnections": wwwConnections,
       "wwwSSLConnections": wwwSSLConnections,
       "wwwProxyConnections": wwwProxyConnections,
       "wwwProxySSLConnections": wwwProxySSLConnections,
       "wwwScriptConnections": wwwScriptConnections,
       "wwwLoggedOnUsers": wwwLoggedOnUsers,
       "wwwOutOfThreads": wwwOutOfThreads,
       "wwwOutOfSessions": wwwOutOfSessions,
       "wwwOutOfProxySessions": wwwOutOfProxySessions,
       "wwwSessionTimeouts": wwwSessionTimeouts,
       "wwwSessionTimeoutsLow": wwwSessionTimeoutsLow,
       "wwwProxySessionTimeouts": wwwProxySessionTimeouts,
       "wwwProxySessionTimeoutsLow": wwwProxySessionTimeoutsLow,
       "wwwScriptSessionTimeouts": wwwScriptSessionTimeouts,
       "wwwScriptSessionTimeoutsLow": wwwScriptSessionTimeoutsLow,
       "wwwSuccessfulAuthentications": wwwSuccessfulAuthentications,
       "wwwSuccessfulAuthenticationsLow": wwwSuccessfulAuthenticationsLow,
       "wwwFailedAuthentications": wwwFailedAuthentications,
       "wwwFailedAuthenticationsLow": wwwFailedAuthenticationsLow,
       "wwwReceivedVolume": wwwReceivedVolume,
       "wwwReceivedVolumeLow": wwwReceivedVolumeLow,
       "wwwTransmittedVolume": wwwTransmittedVolume,
       "wwwTransmittedVolumeLow": wwwTransmittedVolumeLow,
       "wwwProxyReceivedVolume": wwwProxyReceivedVolume,
       "wwwProxyReceivedVolumeLow": wwwProxyReceivedVolumeLow,
       "wwwProxyTransmittedVolume": wwwProxyTransmittedVolume,
       "wwwProxyTransmittedVolumeLow": wwwProxyTransmittedVolumeLow,
       "wwwReverseProxyReceivedVolume": wwwReverseProxyReceivedVolume,
       "wwwReverseProxyReceivedVolumeLow": wwwReverseProxyReceivedVolumeLow,
       "wwwReverseProxyTransmittedVolume": wwwReverseProxyTransmittedVolume,
       "wwwReverseProxyTransmittedVolumeLow": wwwReverseProxyTransmittedVolumeLow,
       "wwwSuccessfulRequests": wwwSuccessfulRequests,
       "wwwSuccessfulRequestsLow": wwwSuccessfulRequestsLow,
       "wwwFailedRequests": wwwFailedRequests,
       "wwwFailedRequestsLow": wwwFailedRequestsLow,
       "wwwSuccessfulAdminRequests": wwwSuccessfulAdminRequests,
       "wwwSuccessfulAdminRequestsLow": wwwSuccessfulAdminRequestsLow,
       "wwwFailedAdminRequests": wwwFailedAdminRequests,
       "wwwFailedAdminRequestsLow": wwwFailedAdminRequestsLow,
       "wwwSuccessfulWebmailRequests": wwwSuccessfulWebmailRequests,
       "wwwSuccessfulWebmailRequestsLow": wwwSuccessfulWebmailRequestsLow,
       "wwwFailedWebmailRequests": wwwFailedWebmailRequests,
       "wwwFailedWebmailRequestsLow": wwwFailedWebmailRequestsLow,
       "wwwSuccessfulUserRequests": wwwSuccessfulUserRequests,
       "wwwSuccessfulUserRequestsLow": wwwSuccessfulUserRequestsLow,
       "wwwFailedUserRequests": wwwFailedUserRequests,
       "wwwFailedUserRequestsLow": wwwFailedUserRequestsLow,
       "wwwSuccessfulProxyRequests": wwwSuccessfulProxyRequests,
       "wwwSuccessfulProxyRequestsLow": wwwSuccessfulProxyRequestsLow,
       "wwwFailedProxyRequests": wwwFailedProxyRequests,
       "wwwFailedProxyRequestsLow": wwwFailedProxyRequestsLow,
       "wwwSuccessfulReverseProxyRequests": wwwSuccessfulReverseProxyRequests,
       "wwwSuccessfulReverseProxyRequestsLow": wwwSuccessfulReverseProxyRequestsLow,
       "wwwFailedReverseProxyRequests": wwwFailedReverseProxyRequests,
       "wwwFailedReverseProxyRequestsLow": wwwFailedReverseProxyRequestsLow,
       "wwwSuccessfulScriptRequests": wwwSuccessfulScriptRequests,
       "wwwSuccessfulScriptRequestsLow": wwwSuccessfulScriptRequestsLow,
       "wwwFailedScriptRequests": wwwFailedScriptRequests,
       "wwwFailedScriptRequestsLow": wwwFailedScriptRequestsLow,
       "wwwSuccessfulTimedRequests": wwwSuccessfulTimedRequests,
       "wwwSuccessfulTimedRequestsLow": wwwSuccessfulTimedRequestsLow,
       "wwwFailedTimedRequests": wwwFailedTimedRequests,
       "wwwFailedTimedRequestsLow": wwwFailedTimedRequestsLow,
       "wwwMMLErrors": wwwMMLErrors,
       "wwwMessagesRead": wwwMessagesRead,
       "wwwMessagesSent": wwwMessagesSent,
       "wwwLastInboundActivity": wwwLastInboundActivity,
       "wwwLastOutboundActivity": wwwLastOutboundActivity}
)

# SNMP MIB module (Fore-Callrecord-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Callrecord-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:50 2024
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

(EntryStatus,
 software) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "EntryStatus",
    "software")

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


# MODULE-IDENTITY

crGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1)
)


# Types definitions



class CrXfrTrapStatus(Integer32):
    """Custom type CrXfrTrapStatus based on Integer32"""
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
        *(("crXfrAccessViolation", 3),
          ("crXfrDiskFullorAllocationExceeded", 4),
          ("crXfrNoError", 1),
          ("crXfrNoResponseFromServer", 2),
          ("crXfrOtherError", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CrXfrGroup_ObjectIdentity = ObjectIdentity
crXfrGroup = _CrXfrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1)
)
_CrXfrTable_Object = MibTable
crXfrTable = _CrXfrTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    crXfrTable.setStatus("current")
_CrXfrEntry_Object = MibTableRow
crXfrEntry = _CrXfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1)
)
crXfrEntry.setIndexNames(
    (0, "Fore-Callrecord-MIB", "crXfrIndex"),
)
if mibBuilder.loadTexts:
    crXfrEntry.setStatus("current")


class _CrXfrIndex_Type(Integer32):
    """Custom type crXfrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("callrecord", 1),
          ("performance", 2))
    )


_CrXfrIndex_Type.__name__ = "Integer32"
_CrXfrIndex_Object = MibTableColumn
crXfrIndex = _CrXfrIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 1),
    _CrXfrIndex_Type()
)
crXfrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crXfrIndex.setStatus("current")
_CrXfrPrimaryUrl_Type = DisplayString
_CrXfrPrimaryUrl_Object = MibTableColumn
crXfrPrimaryUrl = _CrXfrPrimaryUrl_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 2),
    _CrXfrPrimaryUrl_Type()
)
crXfrPrimaryUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crXfrPrimaryUrl.setStatus("current")
_CrXfrSecondaryUrl_Type = DisplayString
_CrXfrSecondaryUrl_Object = MibTableColumn
crXfrSecondaryUrl = _CrXfrSecondaryUrl_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 3),
    _CrXfrSecondaryUrl_Type()
)
crXfrSecondaryUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crXfrSecondaryUrl.setStatus("current")


class _CrXfrRecordingInterval_Type(Integer32):
    """Custom type crXfrRecordingInterval based on Integer32"""
    defaultValue = 5


_CrXfrRecordingInterval_Object = MibTableColumn
crXfrRecordingInterval = _CrXfrRecordingInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 4),
    _CrXfrRecordingInterval_Type()
)
crXfrRecordingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crXfrRecordingInterval.setStatus("current")
_CrXfrUserId_Type = DisplayString
_CrXfrUserId_Object = MibTableColumn
crXfrUserId = _CrXfrUserId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 5),
    _CrXfrUserId_Type()
)
crXfrUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crXfrUserId.setStatus("obsolete")
_CrXfrPassword_Type = DisplayString
_CrXfrPassword_Object = MibTableColumn
crXfrPassword = _CrXfrPassword_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 6),
    _CrXfrPassword_Type()
)
crXfrPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crXfrPassword.setStatus("obsolete")


class _CrXfrTransferStatus_Type(Integer32):
    """Custom type crXfrTransferStatus based on Integer32"""
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
        *(("bothFailed", 5),
          ("primaryInProgress", 1),
          ("primarySucceeded", 3),
          ("secondaryInProgress", 2),
          ("secondarySucceeded", 4))
    )


_CrXfrTransferStatus_Type.__name__ = "Integer32"
_CrXfrTransferStatus_Object = MibTableColumn
crXfrTransferStatus = _CrXfrTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 7),
    _CrXfrTransferStatus_Type()
)
crXfrTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crXfrTransferStatus.setStatus("current")
_CrXfrStatusText_Type = DisplayString
_CrXfrStatusText_Object = MibTableColumn
crXfrStatusText = _CrXfrStatusText_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 8),
    _CrXfrStatusText_Type()
)
crXfrStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crXfrStatusText.setStatus("current")
_CrXfrPrimaryTrapStatus_Type = CrXfrTrapStatus
_CrXfrPrimaryTrapStatus_Object = MibTableColumn
crXfrPrimaryTrapStatus = _CrXfrPrimaryTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 9),
    _CrXfrPrimaryTrapStatus_Type()
)
crXfrPrimaryTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crXfrPrimaryTrapStatus.setStatus("current")
_CrXfrSecondaryTrapStatus_Type = CrXfrTrapStatus
_CrXfrSecondaryTrapStatus_Object = MibTableColumn
crXfrSecondaryTrapStatus = _CrXfrSecondaryTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 10),
    _CrXfrSecondaryTrapStatus_Type()
)
crXfrSecondaryTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crXfrSecondaryTrapStatus.setStatus("current")
_CrXfrPrimaryXfrFailed_Type = Counter32
_CrXfrPrimaryXfrFailed_Object = MibTableColumn
crXfrPrimaryXfrFailed = _CrXfrPrimaryXfrFailed_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 11),
    _CrXfrPrimaryXfrFailed_Type()
)
crXfrPrimaryXfrFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crXfrPrimaryXfrFailed.setStatus("current")
_CrXfrSecondaryXfrFailed_Type = Counter32
_CrXfrSecondaryXfrFailed_Object = MibTableColumn
crXfrSecondaryXfrFailed = _CrXfrSecondaryXfrFailed_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 12),
    _CrXfrSecondaryXfrFailed_Type()
)
crXfrSecondaryXfrFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crXfrSecondaryXfrFailed.setStatus("current")
_CrXfrEntryStatus_Type = EntryStatus
_CrXfrEntryStatus_Object = MibTableColumn
crXfrEntryStatus = _CrXfrEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 13),
    _CrXfrEntryStatus_Type()
)
crXfrEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crXfrEntryStatus.setStatus("current")
_CrXfrPrimaryUserId_Type = DisplayString
_CrXfrPrimaryUserId_Object = MibTableColumn
crXfrPrimaryUserId = _CrXfrPrimaryUserId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 14),
    _CrXfrPrimaryUserId_Type()
)
crXfrPrimaryUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crXfrPrimaryUserId.setStatus("current")
_CrXfrPrimaryPassword_Type = DisplayString
_CrXfrPrimaryPassword_Object = MibTableColumn
crXfrPrimaryPassword = _CrXfrPrimaryPassword_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 15),
    _CrXfrPrimaryPassword_Type()
)
crXfrPrimaryPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crXfrPrimaryPassword.setStatus("current")
_CrXfrSecondaryUserId_Type = DisplayString
_CrXfrSecondaryUserId_Object = MibTableColumn
crXfrSecondaryUserId = _CrXfrSecondaryUserId_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 16),
    _CrXfrSecondaryUserId_Type()
)
crXfrSecondaryUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crXfrSecondaryUserId.setStatus("current")
_CrXfrSecondaryPassword_Type = DisplayString
_CrXfrSecondaryPassword_Object = MibTableColumn
crXfrSecondaryPassword = _CrXfrSecondaryPassword_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 1, 1, 1, 17),
    _CrXfrSecondaryPassword_Type()
)
crXfrSecondaryPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crXfrSecondaryPassword.setStatus("current")
_CrConfGroup_ObjectIdentity = ObjectIdentity
crConfGroup = _CrConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2)
)


class _CrAdminStatus_Type(Integer32):
    """Custom type crAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CrAdminStatus_Type.__name__ = "Integer32"
_CrAdminStatus_Object = MibScalar
crAdminStatus = _CrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2, 1),
    _CrAdminStatus_Type()
)
crAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crAdminStatus.setStatus("current")
_CrMemoryAllocated_Type = Integer32
_CrMemoryAllocated_Object = MibScalar
crMemoryAllocated = _CrMemoryAllocated_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2, 2),
    _CrMemoryAllocated_Type()
)
crMemoryAllocated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crMemoryAllocated.setStatus("obsolete")


class _CrMemOflowAction_Type(Integer32):
    """Custom type crMemOflowAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontRecordCall", 2),
          ("rejectCall", 1))
    )


_CrMemOflowAction_Type.__name__ = "Integer32"
_CrMemOflowAction_Object = MibScalar
crMemOflowAction = _CrMemOflowAction_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2, 3),
    _CrMemOflowAction_Type()
)
crMemOflowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crMemOflowAction.setStatus("current")
_CrAdminMinRecords_Type = Integer32
_CrAdminMinRecords_Object = MibScalar
crAdminMinRecords = _CrAdminMinRecords_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2, 4),
    _CrAdminMinRecords_Type()
)
crAdminMinRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crAdminMinRecords.setStatus("current")
_CrAdminMaxRecords_Type = Integer32
_CrAdminMaxRecords_Object = MibScalar
crAdminMaxRecords = _CrAdminMaxRecords_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2, 5),
    _CrAdminMaxRecords_Type()
)
crAdminMaxRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crAdminMaxRecords.setStatus("current")
_CrOperRecords_Type = Integer32
_CrOperRecords_Object = MibScalar
crOperRecords = _CrOperRecords_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2, 6),
    _CrOperRecords_Type()
)
crOperRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crOperRecords.setStatus("current")
_CrAdminMinDTBs_Type = Integer32
_CrAdminMinDTBs_Object = MibScalar
crAdminMinDTBs = _CrAdminMinDTBs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2, 7),
    _CrAdminMinDTBs_Type()
)
crAdminMinDTBs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crAdminMinDTBs.setStatus("current")
_CrAdminMaxDTBs_Type = Integer32
_CrAdminMaxDTBs_Object = MibScalar
crAdminMaxDTBs = _CrAdminMaxDTBs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2, 8),
    _CrAdminMaxDTBs_Type()
)
crAdminMaxDTBs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crAdminMaxDTBs.setStatus("current")
_CrOperDTBs_Type = Integer32
_CrOperDTBs_Object = MibScalar
crOperDTBs = _CrOperDTBs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2, 9),
    _CrOperDTBs_Type()
)
crOperDTBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crOperDTBs.setStatus("current")


class _CrOperStatus_Type(Integer32):
    """Custom type crOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("shutting-down", 3))
    )


_CrOperStatus_Type.__name__ = "Integer32"
_CrOperStatus_Object = MibScalar
crOperStatus = _CrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2, 10),
    _CrOperStatus_Type()
)
crOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crOperStatus.setStatus("current")
_CrCounterCollectionInterval_Type = Integer32
_CrCounterCollectionInterval_Object = MibScalar
crCounterCollectionInterval = _CrCounterCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 2, 11),
    _CrCounterCollectionInterval_Type()
)
crCounterCollectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crCounterCollectionInterval.setStatus("current")
_CrStatsGroup_ObjectIdentity = ObjectIdentity
crStatsGroup = _CrStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 3)
)
_CrCallsRejected_Type = Counter32
_CrCallsRejected_Object = MibScalar
crCallsRejected = _CrCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 3, 1),
    _CrCallsRejected_Type()
)
crCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crCallsRejected.setStatus("current")
_CrCallsNotRecorded_Type = Counter32
_CrCallsNotRecorded_Object = MibScalar
crCallsNotRecorded = _CrCallsNotRecorded_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 3, 2),
    _CrCallsNotRecorded_Type()
)
crCallsNotRecorded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crCallsNotRecorded.setStatus("current")
_CrCallsOpened_Type = Counter32
_CrCallsOpened_Object = MibScalar
crCallsOpened = _CrCallsOpened_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 3, 3),
    _CrCallsOpened_Type()
)
crCallsOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crCallsOpened.setStatus("current")
_CrIntervalsSkipped_Type = Counter32
_CrIntervalsSkipped_Object = MibScalar
crIntervalsSkipped = _CrIntervalsSkipped_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 3, 4),
    _CrIntervalsSkipped_Type()
)
crIntervalsSkipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crIntervalsSkipped.setStatus("current")
_CrTermCallsLost_Type = Counter32
_CrTermCallsLost_Object = MibScalar
crTermCallsLost = _CrTermCallsLost_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 3, 5),
    _CrTermCallsLost_Type()
)
crTermCallsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crTermCallsLost.setStatus("current")
_CrUpTime_Type = TimeTicks
_CrUpTime_Object = MibScalar
crUpTime = _CrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 3, 6),
    _CrUpTime_Type()
)
crUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crUpTime.setStatus("current")
_CrCurrentCallsRecorded_Type = Counter32
_CrCurrentCallsRecorded_Object = MibScalar
crCurrentCallsRecorded = _CrCurrentCallsRecorded_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 3, 7),
    _CrCurrentCallsRecorded_Type()
)
crCurrentCallsRecorded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crCurrentCallsRecorded.setStatus("current")
_PerfConfGroup_ObjectIdentity = ObjectIdentity
perfConfGroup = _PerfConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 4)
)


class _PerfAdminStatus_Type(Integer32):
    """Custom type perfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PerfAdminStatus_Type.__name__ = "Integer32"
_PerfAdminStatus_Object = MibScalar
perfAdminStatus = _PerfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 4, 1),
    _PerfAdminStatus_Type()
)
perfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfAdminStatus.setStatus("current")
_CrFilterGroup_ObjectIdentity = ObjectIdentity
crFilterGroup = _CrFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5)
)
_CrFilterTable_Object = MibTable
crFilterTable = _CrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    crFilterTable.setStatus("current")
_CrFilterEntry_Object = MibTableRow
crFilterEntry = _CrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1)
)
crFilterEntry.setIndexNames(
    (0, "Fore-Callrecord-MIB", "crFilterPort"),
    (0, "Fore-Callrecord-MIB", "crFilterVpi"),
    (0, "Fore-Callrecord-MIB", "crFilterVci"),
)
if mibBuilder.loadTexts:
    crFilterEntry.setStatus("current")
_CrFilterPort_Type = Integer32
_CrFilterPort_Object = MibTableColumn
crFilterPort = _CrFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1, 1),
    _CrFilterPort_Type()
)
crFilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crFilterPort.setStatus("current")
_CrFilterVpi_Type = Integer32
_CrFilterVpi_Object = MibTableColumn
crFilterVpi = _CrFilterVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1, 2),
    _CrFilterVpi_Type()
)
crFilterVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crFilterVpi.setStatus("current")
_CrFilterVci_Type = Integer32
_CrFilterVci_Object = MibTableColumn
crFilterVci = _CrFilterVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1, 3),
    _CrFilterVci_Type()
)
crFilterVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crFilterVci.setStatus("current")


class _CrFilterPVCSupport_Type(Integer32):
    """Custom type crFilterPVCSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unspecified", 3))
    )


_CrFilterPVCSupport_Type.__name__ = "Integer32"
_CrFilterPVCSupport_Object = MibTableColumn
crFilterPVCSupport = _CrFilterPVCSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1, 4),
    _CrFilterPVCSupport_Type()
)
crFilterPVCSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crFilterPVCSupport.setStatus("current")


class _CrFilterPVPSupport_Type(Integer32):
    """Custom type crFilterPVPSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unspecified", 3))
    )


_CrFilterPVPSupport_Type.__name__ = "Integer32"
_CrFilterPVPSupport_Object = MibTableColumn
crFilterPVPSupport = _CrFilterPVPSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1, 5),
    _CrFilterPVPSupport_Type()
)
crFilterPVPSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crFilterPVPSupport.setStatus("current")


class _CrFilterSVCSupport_Type(Integer32):
    """Custom type crFilterSVCSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unspecified", 3))
    )


_CrFilterSVCSupport_Type.__name__ = "Integer32"
_CrFilterSVCSupport_Object = MibTableColumn
crFilterSVCSupport = _CrFilterSVCSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1, 6),
    _CrFilterSVCSupport_Type()
)
crFilterSVCSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crFilterSVCSupport.setStatus("current")


class _CrFilterSVPSupport_Type(Integer32):
    """Custom type crFilterSVPSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unspecified", 3))
    )


_CrFilterSVPSupport_Type.__name__ = "Integer32"
_CrFilterSVPSupport_Object = MibTableColumn
crFilterSVPSupport = _CrFilterSVPSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1, 7),
    _CrFilterSVPSupport_Type()
)
crFilterSVPSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crFilterSVPSupport.setStatus("current")


class _CrFilterSPVCSupport_Type(Integer32):
    """Custom type crFilterSPVCSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unspecified", 3))
    )


_CrFilterSPVCSupport_Type.__name__ = "Integer32"
_CrFilterSPVCSupport_Object = MibTableColumn
crFilterSPVCSupport = _CrFilterSPVCSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1, 8),
    _CrFilterSPVCSupport_Type()
)
crFilterSPVCSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crFilterSPVCSupport.setStatus("current")


class _CrFilterSPVPSupport_Type(Integer32):
    """Custom type crFilterSPVPSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unspecified", 3))
    )


_CrFilterSPVPSupport_Type.__name__ = "Integer32"
_CrFilterSPVPSupport_Object = MibTableColumn
crFilterSPVPSupport = _CrFilterSPVPSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1, 9),
    _CrFilterSPVPSupport_Type()
)
crFilterSPVPSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crFilterSPVPSupport.setStatus("current")


class _CrFilterFailedCallSupport_Type(Integer32):
    """Custom type crFilterFailedCallSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unspecified", 3))
    )


_CrFilterFailedCallSupport_Type.__name__ = "Integer32"
_CrFilterFailedCallSupport_Object = MibTableColumn
crFilterFailedCallSupport = _CrFilterFailedCallSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1, 10),
    _CrFilterFailedCallSupport_Type()
)
crFilterFailedCallSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crFilterFailedCallSupport.setStatus("current")
_CrFilterEntryStatus_Type = EntryStatus
_CrFilterEntryStatus_Object = MibTableColumn
crFilterEntryStatus = _CrFilterEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 3, 1, 5, 1, 1, 11),
    _CrFilterEntryStatus_Type()
)
crFilterEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crFilterEntryStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Callrecord-MIB",
    **{"CrXfrTrapStatus": CrXfrTrapStatus,
       "crGroup": crGroup,
       "crXfrGroup": crXfrGroup,
       "crXfrTable": crXfrTable,
       "crXfrEntry": crXfrEntry,
       "crXfrIndex": crXfrIndex,
       "crXfrPrimaryUrl": crXfrPrimaryUrl,
       "crXfrSecondaryUrl": crXfrSecondaryUrl,
       "crXfrRecordingInterval": crXfrRecordingInterval,
       "crXfrUserId": crXfrUserId,
       "crXfrPassword": crXfrPassword,
       "crXfrTransferStatus": crXfrTransferStatus,
       "crXfrStatusText": crXfrStatusText,
       "crXfrPrimaryTrapStatus": crXfrPrimaryTrapStatus,
       "crXfrSecondaryTrapStatus": crXfrSecondaryTrapStatus,
       "crXfrPrimaryXfrFailed": crXfrPrimaryXfrFailed,
       "crXfrSecondaryXfrFailed": crXfrSecondaryXfrFailed,
       "crXfrEntryStatus": crXfrEntryStatus,
       "crXfrPrimaryUserId": crXfrPrimaryUserId,
       "crXfrPrimaryPassword": crXfrPrimaryPassword,
       "crXfrSecondaryUserId": crXfrSecondaryUserId,
       "crXfrSecondaryPassword": crXfrSecondaryPassword,
       "crConfGroup": crConfGroup,
       "crAdminStatus": crAdminStatus,
       "crMemoryAllocated": crMemoryAllocated,
       "crMemOflowAction": crMemOflowAction,
       "crAdminMinRecords": crAdminMinRecords,
       "crAdminMaxRecords": crAdminMaxRecords,
       "crOperRecords": crOperRecords,
       "crAdminMinDTBs": crAdminMinDTBs,
       "crAdminMaxDTBs": crAdminMaxDTBs,
       "crOperDTBs": crOperDTBs,
       "crOperStatus": crOperStatus,
       "crCounterCollectionInterval": crCounterCollectionInterval,
       "crStatsGroup": crStatsGroup,
       "crCallsRejected": crCallsRejected,
       "crCallsNotRecorded": crCallsNotRecorded,
       "crCallsOpened": crCallsOpened,
       "crIntervalsSkipped": crIntervalsSkipped,
       "crTermCallsLost": crTermCallsLost,
       "crUpTime": crUpTime,
       "crCurrentCallsRecorded": crCurrentCallsRecorded,
       "perfConfGroup": perfConfGroup,
       "perfAdminStatus": perfAdminStatus,
       "crFilterGroup": crFilterGroup,
       "crFilterTable": crFilterTable,
       "crFilterEntry": crFilterEntry,
       "crFilterPort": crFilterPort,
       "crFilterVpi": crFilterVpi,
       "crFilterVci": crFilterVci,
       "crFilterPVCSupport": crFilterPVCSupport,
       "crFilterPVPSupport": crFilterPVPSupport,
       "crFilterSVCSupport": crFilterSVCSupport,
       "crFilterSVPSupport": crFilterSVPSupport,
       "crFilterSPVCSupport": crFilterSPVCSupport,
       "crFilterSPVPSupport": crFilterSPVPSupport,
       "crFilterFailedCallSupport": crFilterFailedCallSupport,
       "crFilterEntryStatus": crFilterEntryStatus}
)

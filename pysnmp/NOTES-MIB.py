# SNMP MIB module (NOTES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOTES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:00 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lotus_ObjectIdentity = ObjectIdentity
lotus = _Lotus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334)
)
_Notes_ObjectIdentity = ObjectIdentity
notes = _Notes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72)
)
_LnInfo_ObjectIdentity = ObjectIdentity
lnInfo = _LnInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1)
)
_LnStats_ObjectIdentity = ObjectIdentity
lnStats = _LnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1)
)
_LnAllStatsTable_Object = MibTable
lnAllStatsTable = _LnAllStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lnAllStatsTable.setStatus("mandatory")
_LnAllStatsEntry_Object = MibTableRow
lnAllStatsEntry = _LnAllStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 1, 1)
)
lnAllStatsEntry.setIndexNames(
    (0, "NOTES-MIB", "lnStatisticIndex"),
)
if mibBuilder.loadTexts:
    lnAllStatsEntry.setStatus("mandatory")


class _LnStatisticIndex_Type(Integer32):
    """Custom type lnStatisticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnStatisticIndex_Type.__name__ = "Integer32"
_LnStatisticIndex_Object = MibTableColumn
lnStatisticIndex = _LnStatisticIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 1, 1, 1),
    _LnStatisticIndex_Type()
)
lnStatisticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnStatisticIndex.setStatus("mandatory")
_LnStatisticString_Type = DisplayString
_LnStatisticString_Object = MibTableColumn
lnStatisticString = _LnStatisticString_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 1, 1, 2),
    _LnStatisticString_Type()
)
lnStatisticString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnStatisticString.setStatus("mandatory")


class _LnStatsStartTime_Type(Integer32):
    """Custom type lnStatsStartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnStatsStartTime_Type.__name__ = "Integer32"
_LnStatsStartTime_Object = MibScalar
lnStatsStartTime = _LnStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 2),
    _LnStatsStartTime_Type()
)
lnStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnStatsStartTime.setStatus("mandatory")


class _LnStatsCurrentTime_Type(Integer32):
    """Custom type lnStatsCurrentTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnStatsCurrentTime_Type.__name__ = "Integer32"
_LnStatsCurrentTime_Object = MibScalar
lnStatsCurrentTime = _LnStatsCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 3),
    _LnStatsCurrentTime_Type()
)
lnStatsCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnStatsCurrentTime.setStatus("mandatory")
_LnMail_ObjectIdentity = ObjectIdentity
lnMail = _LnMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4)
)


class _LnDeadMail_Type(Integer32):
    """Custom type lnDeadMail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDeadMail_Type.__name__ = "Integer32"
_LnDeadMail_Object = MibScalar
lnDeadMail = _LnDeadMail_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 1),
    _LnDeadMail_Type()
)
lnDeadMail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDeadMail.setStatus("optional")


class _LnDeliveredMail_Type(Integer32):
    """Custom type lnDeliveredMail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDeliveredMail_Type.__name__ = "Integer32"
_LnDeliveredMail_Object = MibScalar
lnDeliveredMail = _LnDeliveredMail_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 2),
    _LnDeliveredMail_Type()
)
lnDeliveredMail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDeliveredMail.setStatus("optional")


class _LnTotalMailFailures_Type(Integer32):
    """Custom type lnTotalMailFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnTotalMailFailures_Type.__name__ = "Integer32"
_LnTotalMailFailures_Object = MibScalar
lnTotalMailFailures = _LnTotalMailFailures_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 3),
    _LnTotalMailFailures_Type()
)
lnTotalMailFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTotalMailFailures.setStatus("optional")


class _LnTotalRoutedMail_Type(Integer32):
    """Custom type lnTotalRoutedMail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnTotalRoutedMail_Type.__name__ = "Integer32"
_LnTotalRoutedMail_Object = MibScalar
lnTotalRoutedMail = _LnTotalRoutedMail_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 4),
    _LnTotalRoutedMail_Type()
)
lnTotalRoutedMail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTotalRoutedMail.setStatus("optional")


class _LnTransferredMail_Type(Integer32):
    """Custom type lnTransferredMail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnTransferredMail_Type.__name__ = "Integer32"
_LnTransferredMail_Object = MibScalar
lnTransferredMail = _LnTransferredMail_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 5),
    _LnTransferredMail_Type()
)
lnTransferredMail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTransferredMail.setStatus("optional")


class _LnWaitingMail_Type(Integer32):
    """Custom type lnWaitingMail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnWaitingMail_Type.__name__ = "Integer32"
_LnWaitingMail_Object = MibScalar
lnWaitingMail = _LnWaitingMail_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 6),
    _LnWaitingMail_Type()
)
lnWaitingMail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWaitingMail.setStatus("optional")


class _LnNumWaitingRecipients_Type(Integer32):
    """Custom type lnNumWaitingRecipients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNumWaitingRecipients_Type.__name__ = "Integer32"
_LnNumWaitingRecipients_Object = MibScalar
lnNumWaitingRecipients = _LnNumWaitingRecipients_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 7),
    _LnNumWaitingRecipients_Type()
)
lnNumWaitingRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNumWaitingRecipients.setStatus("optional")
_LnMailDomain_Type = DisplayString
_LnMailDomain_Object = MibScalar
lnMailDomain = _LnMailDomain_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 8),
    _LnMailDomain_Type()
)
lnMailDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMailDomain.setStatus("optional")


class _LnAverageMailDeliverTime_Type(Integer32):
    """Custom type lnAverageMailDeliverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnAverageMailDeliverTime_Type.__name__ = "Integer32"
_LnAverageMailDeliverTime_Object = MibScalar
lnAverageMailDeliverTime = _LnAverageMailDeliverTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 9),
    _LnAverageMailDeliverTime_Type()
)
lnAverageMailDeliverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnAverageMailDeliverTime.setStatus("optional")


class _LnAverageMailServerHops_Type(Integer32):
    """Custom type lnAverageMailServerHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnAverageMailServerHops_Type.__name__ = "Integer32"
_LnAverageMailServerHops_Object = MibScalar
lnAverageMailServerHops = _LnAverageMailServerHops_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 10),
    _LnAverageMailServerHops_Type()
)
lnAverageMailServerHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnAverageMailServerHops.setStatus("optional")


class _LnAverageMailSizeDelivered_Type(Integer32):
    """Custom type lnAverageMailSizeDelivered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnAverageMailSizeDelivered_Type.__name__ = "Integer32"
_LnAverageMailSizeDelivered_Object = MibScalar
lnAverageMailSizeDelivered = _LnAverageMailSizeDelivered_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 11),
    _LnAverageMailSizeDelivered_Type()
)
lnAverageMailSizeDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnAverageMailSizeDelivered.setStatus("optional")


class _LnMaximumMailDeliverTime_Type(Integer32):
    """Custom type lnMaximumMailDeliverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMaximumMailDeliverTime_Type.__name__ = "Integer32"
_LnMaximumMailDeliverTime_Object = MibScalar
lnMaximumMailDeliverTime = _LnMaximumMailDeliverTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 12),
    _LnMaximumMailDeliverTime_Type()
)
lnMaximumMailDeliverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMaximumMailDeliverTime.setStatus("optional")


class _LnMaximumMailServerHops_Type(Integer32):
    """Custom type lnMaximumMailServerHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMaximumMailServerHops_Type.__name__ = "Integer32"
_LnMaximumMailServerHops_Object = MibScalar
lnMaximumMailServerHops = _LnMaximumMailServerHops_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 13),
    _LnMaximumMailServerHops_Type()
)
lnMaximumMailServerHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMaximumMailServerHops.setStatus("optional")


class _LnMaximumMailSizeDelivered_Type(Integer32):
    """Custom type lnMaximumMailSizeDelivered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMaximumMailSizeDelivered_Type.__name__ = "Integer32"
_LnMaximumMailSizeDelivered_Object = MibScalar
lnMaximumMailSizeDelivered = _LnMaximumMailSizeDelivered_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 14),
    _LnMaximumMailSizeDelivered_Type()
)
lnMaximumMailSizeDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMaximumMailSizeDelivered.setStatus("optional")


class _LnMinimumMailDeliverTime_Type(Integer32):
    """Custom type lnMinimumMailDeliverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMinimumMailDeliverTime_Type.__name__ = "Integer32"
_LnMinimumMailDeliverTime_Object = MibScalar
lnMinimumMailDeliverTime = _LnMinimumMailDeliverTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 15),
    _LnMinimumMailDeliverTime_Type()
)
lnMinimumMailDeliverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMinimumMailDeliverTime.setStatus("optional")


class _LnMinimumMailServerHops_Type(Integer32):
    """Custom type lnMinimumMailServerHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMinimumMailServerHops_Type.__name__ = "Integer32"
_LnMinimumMailServerHops_Object = MibScalar
lnMinimumMailServerHops = _LnMinimumMailServerHops_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 16),
    _LnMinimumMailServerHops_Type()
)
lnMinimumMailServerHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMinimumMailServerHops.setStatus("optional")


class _LnMinimumMailSizeDelivered_Type(Integer32):
    """Custom type lnMinimumMailSizeDelivered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMinimumMailSizeDelivered_Type.__name__ = "Integer32"
_LnMinimumMailSizeDelivered_Object = MibScalar
lnMinimumMailSizeDelivered = _LnMinimumMailSizeDelivered_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 17),
    _LnMinimumMailSizeDelivered_Type()
)
lnMinimumMailSizeDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMinimumMailSizeDelivered.setStatus("optional")


class _LnTotalKBTransferred_Type(Integer32):
    """Custom type lnTotalKBTransferred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnTotalKBTransferred_Type.__name__ = "Integer32"
_LnTotalKBTransferred_Object = MibScalar
lnTotalKBTransferred = _LnTotalKBTransferred_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 18),
    _LnTotalKBTransferred_Type()
)
lnTotalKBTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTotalKBTransferred.setStatus("optional")


class _LnMailTransferFailures_Type(Integer32):
    """Custom type lnMailTransferFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMailTransferFailures_Type.__name__ = "Integer32"
_LnMailTransferFailures_Object = MibScalar
lnMailTransferFailures = _LnMailTransferFailures_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 4, 19),
    _LnMailTransferFailures_Type()
)
lnMailTransferFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMailTransferFailures.setStatus("optional")
_LnReplica_ObjectIdentity = ObjectIdentity
lnReplica = _LnReplica_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5)
)


class _LnRepDocsAdded_Type(Integer32):
    """Custom type lnRepDocsAdded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepDocsAdded_Type.__name__ = "Integer32"
_LnRepDocsAdded_Object = MibScalar
lnRepDocsAdded = _LnRepDocsAdded_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 1),
    _LnRepDocsAdded_Type()
)
lnRepDocsAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepDocsAdded.setStatus("optional")


class _LnRepDocsDeleted_Type(Integer32):
    """Custom type lnRepDocsDeleted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepDocsDeleted_Type.__name__ = "Integer32"
_LnRepDocsDeleted_Object = MibScalar
lnRepDocsDeleted = _LnRepDocsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 2),
    _LnRepDocsDeleted_Type()
)
lnRepDocsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepDocsDeleted.setStatus("optional")


class _LnRepDocsUpdated_Type(Integer32):
    """Custom type lnRepDocsUpdated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepDocsUpdated_Type.__name__ = "Integer32"
_LnRepDocsUpdated_Object = MibScalar
lnRepDocsUpdated = _LnRepDocsUpdated_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 3),
    _LnRepDocsUpdated_Type()
)
lnRepDocsUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepDocsUpdated.setStatus("optional")


class _LnRepFailed_Type(Integer32):
    """Custom type lnRepFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepFailed_Type.__name__ = "Integer32"
_LnRepFailed_Object = MibScalar
lnRepFailed = _LnRepFailed_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 4),
    _LnRepFailed_Type()
)
lnRepFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepFailed.setStatus("optional")


class _LnRepSuccessful_Type(Integer32):
    """Custom type lnRepSuccessful based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepSuccessful_Type.__name__ = "Integer32"
_LnRepSuccessful_Object = MibScalar
lnRepSuccessful = _LnRepSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 5),
    _LnRepSuccessful_Type()
)
lnRepSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepSuccessful.setStatus("optional")
_LnReplicaCluster_ObjectIdentity = ObjectIdentity
lnReplicaCluster = _LnReplicaCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6)
)


class _LnRepClusterDocsAdded_Type(Integer32):
    """Custom type lnRepClusterDocsAdded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterDocsAdded_Type.__name__ = "Integer32"
_LnRepClusterDocsAdded_Object = MibScalar
lnRepClusterDocsAdded = _LnRepClusterDocsAdded_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 1),
    _LnRepClusterDocsAdded_Type()
)
lnRepClusterDocsAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterDocsAdded.setStatus("optional")


class _LnRepClusterDocsDeleted_Type(Integer32):
    """Custom type lnRepClusterDocsDeleted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterDocsDeleted_Type.__name__ = "Integer32"
_LnRepClusterDocsDeleted_Object = MibScalar
lnRepClusterDocsDeleted = _LnRepClusterDocsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 2),
    _LnRepClusterDocsDeleted_Type()
)
lnRepClusterDocsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterDocsDeleted.setStatus("optional")


class _LnRepClusterDocsUpdated_Type(Integer32):
    """Custom type lnRepClusterDocsUpdated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterDocsUpdated_Type.__name__ = "Integer32"
_LnRepClusterDocsUpdated_Object = MibScalar
lnRepClusterDocsUpdated = _LnRepClusterDocsUpdated_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 3),
    _LnRepClusterDocsUpdated_Type()
)
lnRepClusterDocsUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterDocsUpdated.setStatus("optional")


class _LnRepClusterFailed_Type(Integer32):
    """Custom type lnRepClusterFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterFailed_Type.__name__ = "Integer32"
_LnRepClusterFailed_Object = MibScalar
lnRepClusterFailed = _LnRepClusterFailed_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 4),
    _LnRepClusterFailed_Type()
)
lnRepClusterFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterFailed.setStatus("optional")


class _LnRepClusterFilesLocal_Type(Integer32):
    """Custom type lnRepClusterFilesLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterFilesLocal_Type.__name__ = "Integer32"
_LnRepClusterFilesLocal_Object = MibScalar
lnRepClusterFilesLocal = _LnRepClusterFilesLocal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 5),
    _LnRepClusterFilesLocal_Type()
)
lnRepClusterFilesLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterFilesLocal.setStatus("optional")


class _LnRepClusterFilesRemote_Type(Integer32):
    """Custom type lnRepClusterFilesRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterFilesRemote_Type.__name__ = "Integer32"
_LnRepClusterFilesRemote_Object = MibScalar
lnRepClusterFilesRemote = _LnRepClusterFilesRemote_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 6),
    _LnRepClusterFilesRemote_Type()
)
lnRepClusterFilesRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterFilesRemote.setStatus("optional")


class _LnRepClusterRetrySkipped_Type(Integer32):
    """Custom type lnRepClusterRetrySkipped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterRetrySkipped_Type.__name__ = "Integer32"
_LnRepClusterRetrySkipped_Object = MibScalar
lnRepClusterRetrySkipped = _LnRepClusterRetrySkipped_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 7),
    _LnRepClusterRetrySkipped_Type()
)
lnRepClusterRetrySkipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterRetrySkipped.setStatus("optional")


class _LnRepClusterRetryWaiting_Type(Integer32):
    """Custom type lnRepClusterRetryWaiting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterRetryWaiting_Type.__name__ = "Integer32"
_LnRepClusterRetryWaiting_Object = MibScalar
lnRepClusterRetryWaiting = _LnRepClusterRetryWaiting_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 8),
    _LnRepClusterRetryWaiting_Type()
)
lnRepClusterRetryWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterRetryWaiting.setStatus("optional")


class _LnRepClusterSecondsOnQueue_Type(Integer32):
    """Custom type lnRepClusterSecondsOnQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterSecondsOnQueue_Type.__name__ = "Integer32"
_LnRepClusterSecondsOnQueue_Object = MibScalar
lnRepClusterSecondsOnQueue = _LnRepClusterSecondsOnQueue_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 9),
    _LnRepClusterSecondsOnQueue_Type()
)
lnRepClusterSecondsOnQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterSecondsOnQueue.setStatus("optional")


class _LnRepClusterSecondsOnQueueAvg_Type(Integer32):
    """Custom type lnRepClusterSecondsOnQueueAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterSecondsOnQueueAvg_Type.__name__ = "Integer32"
_LnRepClusterSecondsOnQueueAvg_Object = MibScalar
lnRepClusterSecondsOnQueueAvg = _LnRepClusterSecondsOnQueueAvg_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 10),
    _LnRepClusterSecondsOnQueueAvg_Type()
)
lnRepClusterSecondsOnQueueAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterSecondsOnQueueAvg.setStatus("optional")


class _LnRepClusterSecondsOnQueueMax_Type(Integer32):
    """Custom type lnRepClusterSecondsOnQueueMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterSecondsOnQueueMax_Type.__name__ = "Integer32"
_LnRepClusterSecondsOnQueueMax_Object = MibScalar
lnRepClusterSecondsOnQueueMax = _LnRepClusterSecondsOnQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 11),
    _LnRepClusterSecondsOnQueueMax_Type()
)
lnRepClusterSecondsOnQueueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterSecondsOnQueueMax.setStatus("optional")


class _LnRepClusterServers_Type(Integer32):
    """Custom type lnRepClusterServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterServers_Type.__name__ = "Integer32"
_LnRepClusterServers_Object = MibScalar
lnRepClusterServers = _LnRepClusterServers_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 12),
    _LnRepClusterServers_Type()
)
lnRepClusterServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterServers.setStatus("optional")


class _LnRepClusterSessionBytesIn_Type(Integer32):
    """Custom type lnRepClusterSessionBytesIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterSessionBytesIn_Type.__name__ = "Integer32"
_LnRepClusterSessionBytesIn_Object = MibScalar
lnRepClusterSessionBytesIn = _LnRepClusterSessionBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 13),
    _LnRepClusterSessionBytesIn_Type()
)
lnRepClusterSessionBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterSessionBytesIn.setStatus("optional")


class _LnRepClusterSessionBytesOut_Type(Integer32):
    """Custom type lnRepClusterSessionBytesOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterSessionBytesOut_Type.__name__ = "Integer32"
_LnRepClusterSessionBytesOut_Object = MibScalar
lnRepClusterSessionBytesOut = _LnRepClusterSessionBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 14),
    _LnRepClusterSessionBytesOut_Type()
)
lnRepClusterSessionBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterSessionBytesOut.setStatus("optional")


class _LnRepClusterSuccessful_Type(Integer32):
    """Custom type lnRepClusterSuccessful based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterSuccessful_Type.__name__ = "Integer32"
_LnRepClusterSuccessful_Object = MibScalar
lnRepClusterSuccessful = _LnRepClusterSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 15),
    _LnRepClusterSuccessful_Type()
)
lnRepClusterSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterSuccessful.setStatus("optional")


class _LnRepClusterWorkQueueDepth_Type(Integer32):
    """Custom type lnRepClusterWorkQueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterWorkQueueDepth_Type.__name__ = "Integer32"
_LnRepClusterWorkQueueDepth_Object = MibScalar
lnRepClusterWorkQueueDepth = _LnRepClusterWorkQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 16),
    _LnRepClusterWorkQueueDepth_Type()
)
lnRepClusterWorkQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterWorkQueueDepth.setStatus("optional")


class _LnRepClusterWorkQueueDepthAvg_Type(Integer32):
    """Custom type lnRepClusterWorkQueueDepthAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterWorkQueueDepthAvg_Type.__name__ = "Integer32"
_LnRepClusterWorkQueueDepthAvg_Object = MibScalar
lnRepClusterWorkQueueDepthAvg = _LnRepClusterWorkQueueDepthAvg_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 17),
    _LnRepClusterWorkQueueDepthAvg_Type()
)
lnRepClusterWorkQueueDepthAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterWorkQueueDepthAvg.setStatus("optional")


class _LnRepClusterWorkQueueDepthMax_Type(Integer32):
    """Custom type lnRepClusterWorkQueueDepthMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnRepClusterWorkQueueDepthMax_Type.__name__ = "Integer32"
_LnRepClusterWorkQueueDepthMax_Object = MibScalar
lnRepClusterWorkQueueDepthMax = _LnRepClusterWorkQueueDepthMax_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 5, 6, 18),
    _LnRepClusterWorkQueueDepthMax_Type()
)
lnRepClusterWorkQueueDepthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRepClusterWorkQueueDepthMax.setStatus("optional")
_LnServer_ObjectIdentity = ObjectIdentity
lnServer = _LnServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6)
)
_LnServerTask_ObjectIdentity = ObjectIdentity
lnServerTask = _LnServerTask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 1)
)


class _LnTaskCount_Type(Integer32):
    """Custom type lnTaskCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnTaskCount_Type.__name__ = "Integer32"
_LnTaskCount_Object = MibScalar
lnTaskCount = _LnTaskCount_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 1, 1),
    _LnTaskCount_Type()
)
lnTaskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTaskCount.setStatus("mandatory")
_LnTaskTable_Object = MibTable
lnTaskTable = _LnTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    lnTaskTable.setStatus("mandatory")
_LnTaskEntry_Object = MibTableRow
lnTaskEntry = _LnTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 1, 2, 1)
)
lnTaskEntry.setIndexNames(
    (0, "NOTES-MIB", "lnTaskIndex"),
)
if mibBuilder.loadTexts:
    lnTaskEntry.setStatus("mandatory")


class _LnTaskIndex_Type(Integer32):
    """Custom type lnTaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnTaskIndex_Type.__name__ = "Integer32"
_LnTaskIndex_Object = MibTableColumn
lnTaskIndex = _LnTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 1, 2, 1, 1),
    _LnTaskIndex_Type()
)
lnTaskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTaskIndex.setStatus("mandatory")


class _LnTaskType_Type(Integer32):
    """Custom type lnTaskType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("adminprocess", 14),
          ("agentmanager", 23),
          ("billing", 19),
          ("calendarconnector", 11),
          ("cataloger", 24),
          ("ccmailmta", 34),
          ("chronos", 16),
          ("clusteradmin", 22),
          ("clusterdbdirmgr", 21),
          ("clusterreplicator", 20),
          ("collector", 17),
          ("databasecompactor", 25),
          ("databasefixup", 31),
          ("databaseserver", 1),
          ("designer", 26),
          ("event", 2),
          ("eventinterceptor", 7),
          ("httpwebserver", 15),
          ("imap4server", 40),
          ("imapserver", 39),
          ("indexer", 5),
          ("innews", 32),
          ("inotes", 18),
          ("ldapserver", 37),
          ("nntpserver", 38),
          ("objectstoremgr", 27),
          ("pop3server", 28),
          ("querysethandler", 8),
          ("reflectoragent", 9),
          ("replicator", 4),
          ("reporter", 3),
          ("router", 6),
          ("schedulemanager", 12),
          ("smtpmta", 35),
          ("statistics", 29),
          ("stats", 30),
          ("unknownaddin", 13),
          ("webpublisher", 33),
          ("webretriever", 10),
          ("x400mta", 36))
    )


_LnTaskType_Type.__name__ = "Integer32"
_LnTaskType_Object = MibTableColumn
lnTaskType = _LnTaskType_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 1, 2, 1, 2),
    _LnTaskType_Type()
)
lnTaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTaskType.setStatus("mandatory")
_LnTaskData_Type = DisplayString
_LnTaskData_Object = MibTableColumn
lnTaskData = _LnTaskData_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 1, 2, 1, 3),
    _LnTaskData_Type()
)
lnTaskData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTaskData.setStatus("mandatory")
_LnTaskName_Type = DisplayString
_LnTaskName_Object = MibTableColumn
lnTaskName = _LnTaskName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 1, 2, 1, 4),
    _LnTaskName_Type()
)
lnTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTaskName.setStatus("mandatory")
_LnReplicatorStatus_Type = DisplayString
_LnReplicatorStatus_Object = MibScalar
lnReplicatorStatus = _LnReplicatorStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 1, 3),
    _LnReplicatorStatus_Type()
)
lnReplicatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnReplicatorStatus.setStatus("mandatory")
_LnRouterStatus_Type = DisplayString
_LnRouterStatus_Object = MibScalar
lnRouterStatus = _LnRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 1, 4),
    _LnRouterStatus_Type()
)
lnRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnRouterStatus.setStatus("mandatory")
_LnEventStatus_Type = DisplayString
_LnEventStatus_Object = MibScalar
lnEventStatus = _LnEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 1, 5),
    _LnEventStatus_Type()
)
lnEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnEventStatus.setStatus("mandatory")
_LnServerInfo_ObjectIdentity = ObjectIdentity
lnServerInfo = _LnServerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2)
)
_LnServerName_Type = DisplayString
_LnServerName_Object = MibScalar
lnServerName = _LnServerName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 1),
    _LnServerName_Type()
)
lnServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerName.setStatus("mandatory")
_LnServerTitle_Type = DisplayString
_LnServerTitle_Object = MibScalar
lnServerTitle = _LnServerTitle_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 2),
    _LnServerTitle_Type()
)
lnServerTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerTitle.setStatus("optional")
_LnServerAdministrators_Type = DisplayString
_LnServerAdministrators_Object = MibScalar
lnServerAdministrators = _LnServerAdministrators_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 3),
    _LnServerAdministrators_Type()
)
lnServerAdministrators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerAdministrators.setStatus("mandatory")
_LnServerNotesVersion_Type = DisplayString
_LnServerNotesVersion_Object = MibScalar
lnServerNotesVersion = _LnServerNotesVersion_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 4),
    _LnServerNotesVersion_Type()
)
lnServerNotesVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerNotesVersion.setStatus("mandatory")
_LnServerSystemVersion_Type = DisplayString
_LnServerSystemVersion_Object = MibScalar
lnServerSystemVersion = _LnServerSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 5),
    _LnServerSystemVersion_Type()
)
lnServerSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerSystemVersion.setStatus("mandatory")


class _LnServerBootID_Type(Integer32):
    """Custom type lnServerBootID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerBootID_Type.__name__ = "Integer32"
_LnServerBootID_Object = MibScalar
lnServerBootID = _LnServerBootID_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 6),
    _LnServerBootID_Type()
)
lnServerBootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerBootID.setStatus("mandatory")
_LnServerDataPath_Type = DisplayString
_LnServerDataPath_Object = MibScalar
lnServerDataPath = _LnServerDataPath_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 7),
    _LnServerDataPath_Type()
)
lnServerDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerDataPath.setStatus("optional")
_LnServerSwapPath_Type = DisplayString
_LnServerSwapPath_Object = MibScalar
lnServerSwapPath = _LnServerSwapPath_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 8),
    _LnServerSwapPath_Type()
)
lnServerSwapPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerSwapPath.setStatus("optional")


class _LnServerRS232Ports_Type(Integer32):
    """Custom type lnServerRS232Ports based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerRS232Ports_Type.__name__ = "Integer32"
_LnServerRS232Ports_Object = MibScalar
lnServerRS232Ports = _LnServerRS232Ports_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 9),
    _LnServerRS232Ports_Type()
)
lnServerRS232Ports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerRS232Ports.setStatus("optional")


class _LnServerCoprocessor_Type(Integer32):
    """Custom type lnServerCoprocessor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LnServerCoprocessor_Type.__name__ = "Integer32"
_LnServerCoprocessor_Object = MibScalar
lnServerCoprocessor = _LnServerCoprocessor_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 10),
    _LnServerCoprocessor_Type()
)
lnServerCoprocessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerCoprocessor.setStatus("optional")


class _LnServerOS_Type(Integer32):
    """Custom type lnServerOS based on Integer32"""
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
        *(("netware", 2),
          ("os2", 1),
          ("unix", 4),
          ("windowsnt", 3))
    )


_LnServerOS_Type.__name__ = "Integer32"
_LnServerOS_Object = MibScalar
lnServerOS = _LnServerOS_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 11),
    _LnServerOS_Type()
)
lnServerOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerOS.setStatus("mandatory")


class _LnServerCPUCount_Type(Integer32):
    """Custom type lnServerCPUCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerCPUCount_Type.__name__ = "Integer32"
_LnServerCPUCount_Object = MibScalar
lnServerCPUCount = _LnServerCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 12),
    _LnServerCPUCount_Type()
)
lnServerCPUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerCPUCount.setStatus("mandatory")
_LnServerCPUType_Type = DisplayString
_LnServerCPUType_Object = MibScalar
lnServerCPUType = _LnServerCPUType_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 13),
    _LnServerCPUType_Type()
)
lnServerCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerCPUType.setStatus("optional")
_LnServerUsersTable_Object = MibTable
lnServerUsersTable = _LnServerUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 14)
)
if mibBuilder.loadTexts:
    lnServerUsersTable.setStatus("optional")
_LnServerUsersEntry_Object = MibTableRow
lnServerUsersEntry = _LnServerUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 14, 1)
)
lnServerUsersEntry.setIndexNames(
    (0, "NOTES-MIB", "lnServerUsersIndex"),
)
if mibBuilder.loadTexts:
    lnServerUsersEntry.setStatus("mandatory")


class _LnServerUsersIndex_Type(Integer32):
    """Custom type lnServerUsersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnServerUsersIndex_Type.__name__ = "Integer32"
_LnServerUsersIndex_Object = MibTableColumn
lnServerUsersIndex = _LnServerUsersIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 14, 1, 1),
    _LnServerUsersIndex_Type()
)
lnServerUsersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerUsersIndex.setStatus("mandatory")
_LnServerUserName_Type = DisplayString
_LnServerUserName_Object = MibTableColumn
lnServerUserName = _LnServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 14, 1, 2),
    _LnServerUserName_Type()
)
lnServerUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerUserName.setStatus("mandatory")
_LnServerUserSessionID_Type = DisplayString
_LnServerUserSessionID_Object = MibTableColumn
lnServerUserSessionID = _LnServerUserSessionID_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 14, 1, 3),
    _LnServerUserSessionID_Type()
)
lnServerUserSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerUserSessionID.setStatus("mandatory")


class _LnServerUserAccessedDBs_Type(Integer32):
    """Custom type lnServerUserAccessedDBs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerUserAccessedDBs_Type.__name__ = "Integer32"
_LnServerUserAccessedDBs_Object = MibTableColumn
lnServerUserAccessedDBs = _LnServerUserAccessedDBs_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 14, 1, 4),
    _LnServerUserAccessedDBs_Type()
)
lnServerUserAccessedDBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerUserAccessedDBs.setStatus("mandatory")
_LnServerPorts_Type = DisplayString
_LnServerPorts_Object = MibScalar
lnServerPorts = _LnServerPorts_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 15),
    _LnServerPorts_Type()
)
lnServerPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerPorts.setStatus("optional")
_LnServerPoweredBy_Type = DisplayString
_LnServerPoweredBy_Object = MibScalar
lnServerPoweredBy = _LnServerPoweredBy_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 2, 16),
    _LnServerPoweredBy_Type()
)
lnServerPoweredBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerPoweredBy.setStatus("optional")
_LnServerStats_ObjectIdentity = ObjectIdentity
lnServerStats = _LnServerStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3)
)


class _LnServerDroppedSessions_Type(Integer32):
    """Custom type lnServerDroppedSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerDroppedSessions_Type.__name__ = "Integer32"
_LnServerDroppedSessions_Object = MibScalar
lnServerDroppedSessions = _LnServerDroppedSessions_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 1),
    _LnServerDroppedSessions_Type()
)
lnServerDroppedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerDroppedSessions.setStatus("optional")


class _LnServerTransPerMin_Type(Integer32):
    """Custom type lnServerTransPerMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerTransPerMin_Type.__name__ = "Integer32"
_LnServerTransPerMin_Object = MibScalar
lnServerTransPerMin = _LnServerTransPerMin_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 2),
    _LnServerTransPerMin_Type()
)
lnServerTransPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerTransPerMin.setStatus("optional")


class _LnServerTransPerMinPeak_Type(Integer32):
    """Custom type lnServerTransPerMinPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerTransPerMinPeak_Type.__name__ = "Integer32"
_LnServerTransPerMinPeak_Object = MibScalar
lnServerTransPerMinPeak = _LnServerTransPerMinPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 3),
    _LnServerTransPerMinPeak_Type()
)
lnServerTransPerMinPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerTransPerMinPeak.setStatus("optional")


class _LnServerTransPerMinPeakTime_Type(Integer32):
    """Custom type lnServerTransPerMinPeakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerTransPerMinPeakTime_Type.__name__ = "Integer32"
_LnServerTransPerMinPeakTime_Object = MibScalar
lnServerTransPerMinPeakTime = _LnServerTransPerMinPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 4),
    _LnServerTransPerMinPeakTime_Type()
)
lnServerTransPerMinPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerTransPerMinPeakTime.setStatus("optional")


class _LnServerTransTotal_Type(Integer32):
    """Custom type lnServerTransTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerTransTotal_Type.__name__ = "Integer32"
_LnServerTransTotal_Object = MibScalar
lnServerTransTotal = _LnServerTransTotal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 5),
    _LnServerTransTotal_Type()
)
lnServerTransTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerTransTotal.setStatus("optional")


class _LnServerUsers_Type(Integer32):
    """Custom type lnServerUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerUsers_Type.__name__ = "Integer32"
_LnServerUsers_Object = MibScalar
lnServerUsers = _LnServerUsers_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 6),
    _LnServerUsers_Type()
)
lnServerUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerUsers.setStatus("optional")


class _LnServerUsers1MinPeak_Type(Integer32):
    """Custom type lnServerUsers1MinPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerUsers1MinPeak_Type.__name__ = "Integer32"
_LnServerUsers1MinPeak_Object = MibScalar
lnServerUsers1MinPeak = _LnServerUsers1MinPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 7),
    _LnServerUsers1MinPeak_Type()
)
lnServerUsers1MinPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerUsers1MinPeak.setStatus("optional")


class _LnServerUsers1MinPeakTime_Type(Integer32):
    """Custom type lnServerUsers1MinPeakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnServerUsers1MinPeakTime_Type.__name__ = "Integer32"
_LnServerUsers1MinPeakTime_Object = MibScalar
lnServerUsers1MinPeakTime = _LnServerUsers1MinPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 8),
    _LnServerUsers1MinPeakTime_Type()
)
lnServerUsers1MinPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerUsers1MinPeakTime.setStatus("optional")


class _LnServerUsers5MinPeak_Type(Integer32):
    """Custom type lnServerUsers5MinPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerUsers5MinPeak_Type.__name__ = "Integer32"
_LnServerUsers5MinPeak_Object = MibScalar
lnServerUsers5MinPeak = _LnServerUsers5MinPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 9),
    _LnServerUsers5MinPeak_Type()
)
lnServerUsers5MinPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerUsers5MinPeak.setStatus("optional")


class _LnServerUsers5MinPeakTime_Type(Integer32):
    """Custom type lnServerUsers5MinPeakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnServerUsers5MinPeakTime_Type.__name__ = "Integer32"
_LnServerUsers5MinPeakTime_Object = MibScalar
lnServerUsers5MinPeakTime = _LnServerUsers5MinPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 10),
    _LnServerUsers5MinPeakTime_Type()
)
lnServerUsers5MinPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerUsers5MinPeakTime.setStatus("optional")


class _LnServerUsersPeak_Type(Integer32):
    """Custom type lnServerUsersPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerUsersPeak_Type.__name__ = "Integer32"
_LnServerUsersPeak_Object = MibScalar
lnServerUsersPeak = _LnServerUsersPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 11),
    _LnServerUsersPeak_Type()
)
lnServerUsersPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerUsersPeak.setStatus("optional")


class _LnServerUsersPeakTime_Type(Integer32):
    """Custom type lnServerUsersPeakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnServerUsersPeakTime_Type.__name__ = "Integer32"
_LnServerUsersPeakTime_Object = MibScalar
lnServerUsersPeakTime = _LnServerUsersPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 12),
    _LnServerUsersPeakTime_Type()
)
lnServerUsersPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerUsersPeakTime.setStatus("optional")


class _LnServerOpenReqMaxUsers_Type(Integer32):
    """Custom type lnServerOpenReqMaxUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerOpenReqMaxUsers_Type.__name__ = "Integer32"
_LnServerOpenReqMaxUsers_Object = MibScalar
lnServerOpenReqMaxUsers = _LnServerOpenReqMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 13),
    _LnServerOpenReqMaxUsers_Type()
)
lnServerOpenReqMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerOpenReqMaxUsers.setStatus("optional")


class _LnServerOpenReqPreV4Client_Type(Integer32):
    """Custom type lnServerOpenReqPreV4Client based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerOpenReqPreV4Client_Type.__name__ = "Integer32"
_LnServerOpenReqPreV4Client_Object = MibScalar
lnServerOpenReqPreV4Client = _LnServerOpenReqPreV4Client_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 14),
    _LnServerOpenReqPreV4Client_Type()
)
lnServerOpenReqPreV4Client.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerOpenReqPreV4Client.setStatus("optional")


class _LnServerOpenReqRestricted_Type(Integer32):
    """Custom type lnServerOpenReqRestricted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerOpenReqRestricted_Type.__name__ = "Integer32"
_LnServerOpenReqRestricted_Object = MibScalar
lnServerOpenReqRestricted = _LnServerOpenReqRestricted_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 15),
    _LnServerOpenReqRestricted_Type()
)
lnServerOpenReqRestricted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerOpenReqRestricted.setStatus("optional")


class _LnServerOpenReqV4Client_Type(Integer32):
    """Custom type lnServerOpenReqV4Client based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerOpenReqV4Client_Type.__name__ = "Integer32"
_LnServerOpenReqV4Client_Object = MibScalar
lnServerOpenReqV4Client = _LnServerOpenReqV4Client_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 16),
    _LnServerOpenReqV4Client_Type()
)
lnServerOpenReqV4Client.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerOpenReqV4Client.setStatus("optional")


class _LnServerBusyTimeQueryReceivedCount_Type(Integer32):
    """Custom type lnServerBusyTimeQueryReceivedCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerBusyTimeQueryReceivedCount_Type.__name__ = "Integer32"
_LnServerBusyTimeQueryReceivedCount_Object = MibScalar
lnServerBusyTimeQueryReceivedCount = _LnServerBusyTimeQueryReceivedCount_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 17),
    _LnServerBusyTimeQueryReceivedCount_Type()
)
lnServerBusyTimeQueryReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerBusyTimeQueryReceivedCount.setStatus("optional")


class _LnServerBusyTimeQueryRetObjSched_Type(Integer32):
    """Custom type lnServerBusyTimeQueryRetObjSched based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnServerBusyTimeQueryRetObjSched_Type.__name__ = "Integer32"
_LnServerBusyTimeQueryRetObjSched_Object = MibScalar
lnServerBusyTimeQueryRetObjSched = _LnServerBusyTimeQueryRetObjSched_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 3, 18),
    _LnServerBusyTimeQueryRetObjSched_Type()
)
lnServerBusyTimeQueryRetObjSched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerBusyTimeQueryRetObjSched.setStatus("optional")
_LnCluster_ObjectIdentity = ObjectIdentity
lnCluster = _LnCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4)
)
_LnClusterName_Type = DisplayString
_LnClusterName_Object = MibScalar
lnClusterName = _LnClusterName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 1),
    _LnClusterName_Type()
)
lnClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterName.setStatus("optional")


class _LnClusterAvailIndex_Type(Integer32):
    """Custom type lnClusterAvailIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LnClusterAvailIndex_Type.__name__ = "Integer32"
_LnClusterAvailIndex_Object = MibScalar
lnClusterAvailIndex = _LnClusterAvailIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 2),
    _LnClusterAvailIndex_Type()
)
lnClusterAvailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterAvailIndex.setStatus("optional")


class _LnClusterAvailThreshold_Type(Integer32):
    """Custom type lnClusterAvailThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterAvailThreshold_Type.__name__ = "Integer32"
_LnClusterAvailThreshold_Object = MibScalar
lnClusterAvailThreshold = _LnClusterAvailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 3),
    _LnClusterAvailThreshold_Type()
)
lnClusterAvailThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterAvailThreshold.setStatus("optional")
_LnClusterPortName_Type = DisplayString
_LnClusterPortName_Object = MibScalar
lnClusterPortName = _LnClusterPortName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 4),
    _LnClusterPortName_Type()
)
lnClusterPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterPortName.setStatus("optional")


class _LnClusterProbeCount_Type(Integer32):
    """Custom type lnClusterProbeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterProbeCount_Type.__name__ = "Integer32"
_LnClusterProbeCount_Object = MibScalar
lnClusterProbeCount = _LnClusterProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 5),
    _LnClusterProbeCount_Type()
)
lnClusterProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterProbeCount.setStatus("optional")


class _LnClusterProbeTimeout_Type(Integer32):
    """Custom type lnClusterProbeTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterProbeTimeout_Type.__name__ = "Integer32"
_LnClusterProbeTimeout_Object = MibScalar
lnClusterProbeTimeout = _LnClusterProbeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 6),
    _LnClusterProbeTimeout_Type()
)
lnClusterProbeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterProbeTimeout.setStatus("optional")
_LnClusterTable_Object = MibTable
lnClusterTable = _LnClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 7)
)
if mibBuilder.loadTexts:
    lnClusterTable.setStatus("optional")
_LnClusterEntry_Object = MibTableRow
lnClusterEntry = _LnClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 7, 1)
)
lnClusterEntry.setIndexNames(
    (0, "NOTES-MIB", "lnClusterTableIndex"),
)
if mibBuilder.loadTexts:
    lnClusterEntry.setStatus("optional")


class _LnClusterTableIndex_Type(Integer32):
    """Custom type lnClusterTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnClusterTableIndex_Type.__name__ = "Integer32"
_LnClusterTableIndex_Object = MibTableColumn
lnClusterTableIndex = _LnClusterTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 7, 1, 1),
    _LnClusterTableIndex_Type()
)
lnClusterTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterTableIndex.setStatus("optional")
_LnClusterMemberName_Type = DisplayString
_LnClusterMemberName_Object = MibTableColumn
lnClusterMemberName = _LnClusterMemberName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 7, 1, 2),
    _LnClusterMemberName_Type()
)
lnClusterMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterMemberName.setStatus("optional")
_LnClusterMemberIndex_Type = DisplayString
_LnClusterMemberIndex_Object = MibTableColumn
lnClusterMemberIndex = _LnClusterMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 7, 1, 3),
    _LnClusterMemberIndex_Type()
)
lnClusterMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterMemberIndex.setStatus("optional")
_LnOpenRedirects_ObjectIdentity = ObjectIdentity
lnOpenRedirects = _LnOpenRedirects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 8)
)


class _LnClusterFailoverByPathSucc_Type(Integer32):
    """Custom type lnClusterFailoverByPathSucc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterFailoverByPathSucc_Type.__name__ = "Integer32"
_LnClusterFailoverByPathSucc_Object = MibScalar
lnClusterFailoverByPathSucc = _LnClusterFailoverByPathSucc_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 8, 1),
    _LnClusterFailoverByPathSucc_Type()
)
lnClusterFailoverByPathSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterFailoverByPathSucc.setStatus("optional")


class _LnClusterFailoverByPathUnsucc_Type(Integer32):
    """Custom type lnClusterFailoverByPathUnsucc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterFailoverByPathUnsucc_Type.__name__ = "Integer32"
_LnClusterFailoverByPathUnsucc_Object = MibScalar
lnClusterFailoverByPathUnsucc = _LnClusterFailoverByPathUnsucc_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 8, 2),
    _LnClusterFailoverByPathUnsucc_Type()
)
lnClusterFailoverByPathUnsucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterFailoverByPathUnsucc.setStatus("optional")


class _LnClusterFailoverSucc_Type(Integer32):
    """Custom type lnClusterFailoverSucc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterFailoverSucc_Type.__name__ = "Integer32"
_LnClusterFailoverSucc_Object = MibScalar
lnClusterFailoverSucc = _LnClusterFailoverSucc_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 8, 3),
    _LnClusterFailoverSucc_Type()
)
lnClusterFailoverSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterFailoverSucc.setStatus("optional")


class _LnClusterFailoverUnsucc_Type(Integer32):
    """Custom type lnClusterFailoverUnsucc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterFailoverUnsucc_Type.__name__ = "Integer32"
_LnClusterFailoverUnsucc_Object = MibScalar
lnClusterFailoverUnsucc = _LnClusterFailoverUnsucc_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 8, 4),
    _LnClusterFailoverUnsucc_Type()
)
lnClusterFailoverUnsucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterFailoverUnsucc.setStatus("optional")


class _LnClusterLoadBalByPathSucc_Type(Integer32):
    """Custom type lnClusterLoadBalByPathSucc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterLoadBalByPathSucc_Type.__name__ = "Integer32"
_LnClusterLoadBalByPathSucc_Object = MibScalar
lnClusterLoadBalByPathSucc = _LnClusterLoadBalByPathSucc_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 8, 5),
    _LnClusterLoadBalByPathSucc_Type()
)
lnClusterLoadBalByPathSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterLoadBalByPathSucc.setStatus("optional")


class _LnClusterLoadBalByPathUnsucc_Type(Integer32):
    """Custom type lnClusterLoadBalByPathUnsucc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterLoadBalByPathUnsucc_Type.__name__ = "Integer32"
_LnClusterLoadBalByPathUnsucc_Object = MibScalar
lnClusterLoadBalByPathUnsucc = _LnClusterLoadBalByPathUnsucc_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 8, 6),
    _LnClusterLoadBalByPathUnsucc_Type()
)
lnClusterLoadBalByPathUnsucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterLoadBalByPathUnsucc.setStatus("optional")


class _LnClusterLoadBalSucc_Type(Integer32):
    """Custom type lnClusterLoadBalSucc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterLoadBalSucc_Type.__name__ = "Integer32"
_LnClusterLoadBalSucc_Object = MibScalar
lnClusterLoadBalSucc = _LnClusterLoadBalSucc_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 8, 7),
    _LnClusterLoadBalSucc_Type()
)
lnClusterLoadBalSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterLoadBalSucc.setStatus("optional")


class _LnClusterLoadBalUnsucc_Type(Integer32):
    """Custom type lnClusterLoadBalUnsucc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterLoadBalUnsucc_Type.__name__ = "Integer32"
_LnClusterLoadBalUnsucc_Object = MibScalar
lnClusterLoadBalUnsucc = _LnClusterLoadBalUnsucc_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 8, 8),
    _LnClusterLoadBalUnsucc_Type()
)
lnClusterLoadBalUnsucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterLoadBalUnsucc.setStatus("optional")
_LnOpenRequest_ObjectIdentity = ObjectIdentity
lnOpenRequest = _LnOpenRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 9)
)


class _LnClusterOpenReqClustBusy_Type(Integer32):
    """Custom type lnClusterOpenReqClustBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterOpenReqClustBusy_Type.__name__ = "Integer32"
_LnClusterOpenReqClustBusy_Object = MibScalar
lnClusterOpenReqClustBusy = _LnClusterOpenReqClustBusy_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 9, 1),
    _LnClusterOpenReqClustBusy_Type()
)
lnClusterOpenReqClustBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterOpenReqClustBusy.setStatus("optional")


class _LnClusterOpenReqDBOutofServ_Type(Integer32):
    """Custom type lnClusterOpenReqDBOutofServ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterOpenReqDBOutofServ_Type.__name__ = "Integer32"
_LnClusterOpenReqDBOutofServ_Object = MibScalar
lnClusterOpenReqDBOutofServ = _LnClusterOpenReqDBOutofServ_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 9, 2),
    _LnClusterOpenReqDBOutofServ_Type()
)
lnClusterOpenReqDBOutofServ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterOpenReqDBOutofServ.setStatus("optional")


class _LnClusterOpenReqLoadBalanced_Type(Integer32):
    """Custom type lnClusterOpenReqLoadBalanced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterOpenReqLoadBalanced_Type.__name__ = "Integer32"
_LnClusterOpenReqLoadBalanced_Object = MibScalar
lnClusterOpenReqLoadBalanced = _LnClusterOpenReqLoadBalanced_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 9, 3),
    _LnClusterOpenReqLoadBalanced_Type()
)
lnClusterOpenReqLoadBalanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterOpenReqLoadBalanced.setStatus("optional")
_LnClusterTrans_ObjectIdentity = ObjectIdentity
lnClusterTrans = _LnClusterTrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 10)
)


class _LnClusterTransIntAvgTime_Type(Integer32):
    """Custom type lnClusterTransIntAvgTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterTransIntAvgTime_Type.__name__ = "Integer32"
_LnClusterTransIntAvgTime_Object = MibScalar
lnClusterTransIntAvgTime = _LnClusterTransIntAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 10, 1),
    _LnClusterTransIntAvgTime_Type()
)
lnClusterTransIntAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterTransIntAvgTime.setStatus("optional")


class _LnClusterTransIntInSec_Type(Integer32):
    """Custom type lnClusterTransIntInSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterTransIntInSec_Type.__name__ = "Integer32"
_LnClusterTransIntInSec_Object = MibScalar
lnClusterTransIntInSec = _LnClusterTransIntInSec_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 10, 2),
    _LnClusterTransIntInSec_Type()
)
lnClusterTransIntInSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterTransIntInSec.setStatus("optional")


class _LnClusterTransIntUsedInAvg_Type(Integer32):
    """Custom type lnClusterTransIntUsedInAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterTransIntUsedInAvg_Type.__name__ = "Integer32"
_LnClusterTransIntUsedInAvg_Object = MibScalar
lnClusterTransIntUsedInAvg = _LnClusterTransIntUsedInAvg_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 10, 3),
    _LnClusterTransIntUsedInAvg_Type()
)
lnClusterTransIntUsedInAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterTransIntUsedInAvg.setStatus("optional")


class _LnClusterTransLastIntAvgTime_Type(Integer32):
    """Custom type lnClusterTransLastIntAvgTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterTransLastIntAvgTime_Type.__name__ = "Integer32"
_LnClusterTransLastIntAvgTime_Object = MibScalar
lnClusterTransLastIntAvgTime = _LnClusterTransLastIntAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 10, 4),
    _LnClusterTransLastIntAvgTime_Type()
)
lnClusterTransLastIntAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterTransLastIntAvgTime.setStatus("optional")


class _LnClusterTransNormValue_Type(Integer32):
    """Custom type lnClusterTransNormValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterTransNormValue_Type.__name__ = "Integer32"
_LnClusterTransNormValue_Object = MibScalar
lnClusterTransNormValue = _LnClusterTransNormValue_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 10, 5),
    _LnClusterTransNormValue_Type()
)
lnClusterTransNormValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterTransNormValue.setStatus("optional")


class _LnClusterProbeError_Type(Integer32):
    """Custom type lnClusterProbeError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnClusterProbeError_Type.__name__ = "Integer32"
_LnClusterProbeError_Object = MibScalar
lnClusterProbeError = _LnClusterProbeError_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 6, 4, 11),
    _LnClusterProbeError_Type()
)
lnClusterProbeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnClusterProbeError.setStatus("optional")
_LnComm_ObjectIdentity = ObjectIdentity
lnComm = _LnComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7)
)


class _LnNumClosedOldSessions_Type(Integer32):
    """Custom type lnNumClosedOldSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNumClosedOldSessions_Type.__name__ = "Integer32"
_LnNumClosedOldSessions_Object = MibScalar
lnNumClosedOldSessions = _LnNumClosedOldSessions_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 1),
    _LnNumClosedOldSessions_Type()
)
lnNumClosedOldSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNumClosedOldSessions.setStatus("optional")
_LnNetbiosTable_Object = MibTable
lnNetbiosTable = _LnNetbiosTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    lnNetbiosTable.setStatus("mandatory")
_LnNetbiosEntry_Object = MibTableRow
lnNetbiosEntry = _LnNetbiosEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1)
)
lnNetbiosEntry.setIndexNames(
    (0, "NOTES-MIB", "lnNBIndex"),
)
if mibBuilder.loadTexts:
    lnNetbiosEntry.setStatus("mandatory")


class _LnNBIndex_Type(Integer32):
    """Custom type lnNBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnNBIndex_Type.__name__ = "Integer32"
_LnNBIndex_Object = MibTableColumn
lnNBIndex = _LnNBIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 1),
    _LnNBIndex_Type()
)
lnNBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBIndex.setStatus("mandatory")
_LnNBPort_Type = DisplayString
_LnNBPort_Object = MibTableColumn
lnNBPort = _LnNBPort_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 2),
    _LnNBPort_Type()
)
lnNBPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBPort.setStatus("mandatory")


class _LnNBUnitNumber_Type(Integer32):
    """Custom type lnNBUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBUnitNumber_Type.__name__ = "Integer32"
_LnNBUnitNumber_Object = MibTableColumn
lnNBUnitNumber = _LnNBUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 3),
    _LnNBUnitNumber_Type()
)
lnNBUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBUnitNumber.setStatus("mandatory")


class _LnNBMajVersion_Type(Integer32):
    """Custom type lnNBMajVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBMajVersion_Type.__name__ = "Integer32"
_LnNBMajVersion_Object = MibTableColumn
lnNBMajVersion = _LnNBMajVersion_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 4),
    _LnNBMajVersion_Type()
)
lnNBMajVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBMajVersion.setStatus("mandatory")


class _LnNMMinVersion_Type(Integer32):
    """Custom type lnNMMinVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNMMinVersion_Type.__name__ = "Integer32"
_LnNMMinVersion_Object = MibTableColumn
lnNMMinVersion = _LnNMMinVersion_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 5),
    _LnNMMinVersion_Type()
)
lnNMMinVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNMMinVersion.setStatus("mandatory")


class _LnNBReportPeriod_Type(Integer32):
    """Custom type lnNBReportPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBReportPeriod_Type.__name__ = "Integer32"
_LnNBReportPeriod_Object = MibTableColumn
lnNBReportPeriod = _LnNBReportPeriod_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 6),
    _LnNBReportPeriod_Type()
)
lnNBReportPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBReportPeriod.setStatus("mandatory")


class _LnNBInUseSessions_Type(Integer32):
    """Custom type lnNBInUseSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBInUseSessions_Type.__name__ = "Integer32"
_LnNBInUseSessions_Object = MibTableColumn
lnNBInUseSessions = _LnNBInUseSessions_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 7),
    _LnNBInUseSessions_Type()
)
lnNBInUseSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBInUseSessions.setStatus("mandatory")


class _LnNBMaxSessions_Type(Integer32):
    """Custom type lnNBMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBMaxSessions_Type.__name__ = "Integer32"
_LnNBMaxSessions_Object = MibTableColumn
lnNBMaxSessions = _LnNBMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 8),
    _LnNBMaxSessions_Type()
)
lnNBMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBMaxSessions.setStatus("mandatory")


class _LnNBAvailCmdBlocks_Type(Integer32):
    """Custom type lnNBAvailCmdBlocks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBAvailCmdBlocks_Type.__name__ = "Integer32"
_LnNBAvailCmdBlocks_Object = MibTableColumn
lnNBAvailCmdBlocks = _LnNBAvailCmdBlocks_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 9),
    _LnNBAvailCmdBlocks_Type()
)
lnNBAvailCmdBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBAvailCmdBlocks.setStatus("mandatory")


class _LnNBTotalCmdBlocks_Type(Integer32):
    """Custom type lnNBTotalCmdBlocks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBTotalCmdBlocks_Type.__name__ = "Integer32"
_LnNBTotalCmdBlocks_Object = MibTableColumn
lnNBTotalCmdBlocks = _LnNBTotalCmdBlocks_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 10),
    _LnNBTotalCmdBlocks_Type()
)
lnNBTotalCmdBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBTotalCmdBlocks.setStatus("mandatory")


class _LnNBPacketSize_Type(Integer32):
    """Custom type lnNBPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBPacketSize_Type.__name__ = "Integer32"
_LnNBPacketSize_Object = MibTableColumn
lnNBPacketSize = _LnNBPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 11),
    _LnNBPacketSize_Type()
)
lnNBPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBPacketSize.setStatus("mandatory")


class _LnNBReceivedPackets_Type(Integer32):
    """Custom type lnNBReceivedPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBReceivedPackets_Type.__name__ = "Integer32"
_LnNBReceivedPackets_Object = MibTableColumn
lnNBReceivedPackets = _LnNBReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 12),
    _LnNBReceivedPackets_Type()
)
lnNBReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBReceivedPackets.setStatus("mandatory")


class _LnNBSentPackets_Type(Integer32):
    """Custom type lnNBSentPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBSentPackets_Type.__name__ = "Integer32"
_LnNBSentPackets_Object = MibTableColumn
lnNBSentPackets = _LnNBSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 13),
    _LnNBSentPackets_Type()
)
lnNBSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBSentPackets.setStatus("mandatory")


class _LnNBAbortedTransmissions_Type(Integer32):
    """Custom type lnNBAbortedTransmissions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBAbortedTransmissions_Type.__name__ = "Integer32"
_LnNBAbortedTransmissions_Object = MibTableColumn
lnNBAbortedTransmissions = _LnNBAbortedTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 14),
    _LnNBAbortedTransmissions_Type()
)
lnNBAbortedTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBAbortedTransmissions.setStatus("mandatory")


class _LnNBRetriedTransmissions_Type(Integer32):
    """Custom type lnNBRetriedTransmissions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBRetriedTransmissions_Type.__name__ = "Integer32"
_LnNBRetriedTransmissions_Object = MibTableColumn
lnNBRetriedTransmissions = _LnNBRetriedTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 15),
    _LnNBRetriedTransmissions_Type()
)
lnNBRetriedTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBRetriedTransmissions.setStatus("mandatory")


class _LnNBAlignmentErrors_Type(Integer32):
    """Custom type lnNBAlignmentErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBAlignmentErrors_Type.__name__ = "Integer32"
_LnNBAlignmentErrors_Object = MibTableColumn
lnNBAlignmentErrors = _LnNBAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 16),
    _LnNBAlignmentErrors_Type()
)
lnNBAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBAlignmentErrors.setStatus("mandatory")


class _LnNBCollisionErrors_Type(Integer32):
    """Custom type lnNBCollisionErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBCollisionErrors_Type.__name__ = "Integer32"
_LnNBCollisionErrors_Object = MibTableColumn
lnNBCollisionErrors = _LnNBCollisionErrors_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 17),
    _LnNBCollisionErrors_Type()
)
lnNBCollisionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBCollisionErrors.setStatus("mandatory")


class _LnNBCRCErrors_Type(Integer32):
    """Custom type lnNBCRCErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNBCRCErrors_Type.__name__ = "Integer32"
_LnNBCRCErrors_Object = MibTableColumn
lnNBCRCErrors = _LnNBCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 2, 1, 18),
    _LnNBCRCErrors_Type()
)
lnNBCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNBCRCErrors.setStatus("mandatory")
_LnXPCTable_Object = MibTable
lnXPCTable = _LnXPCTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    lnXPCTable.setStatus("mandatory")
_LnXPCEntry_Object = MibTableRow
lnXPCEntry = _LnXPCEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1)
)
lnXPCEntry.setIndexNames(
    (0, "NOTES-MIB", "lnXPCIndex"),
)
if mibBuilder.loadTexts:
    lnXPCEntry.setStatus("mandatory")


class _LnXPCIndex_Type(Integer32):
    """Custom type lnXPCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnXPCIndex_Type.__name__ = "Integer32"
_LnXPCIndex_Object = MibTableColumn
lnXPCIndex = _LnXPCIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 1),
    _LnXPCIndex_Type()
)
lnXPCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCIndex.setStatus("mandatory")
_LnXPCPort_Type = DisplayString
_LnXPCPort_Object = MibTableColumn
lnXPCPort = _LnXPCPort_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 2),
    _LnXPCPort_Type()
)
lnXPCPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCPort.setStatus("mandatory")
_LnXPCStatus_Type = DisplayString
_LnXPCStatus_Object = MibTableColumn
lnXPCStatus = _LnXPCStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 3),
    _LnXPCStatus_Type()
)
lnXPCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCStatus.setStatus("mandatory")


class _LnXPCCarrierSpeed_Type(Integer32):
    """Custom type lnXPCCarrierSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnXPCCarrierSpeed_Type.__name__ = "Integer32"
_LnXPCCarrierSpeed_Object = MibTableColumn
lnXPCCarrierSpeed = _LnXPCCarrierSpeed_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 4),
    _LnXPCCarrierSpeed_Type()
)
lnXPCCarrierSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCCarrierSpeed.setStatus("mandatory")


class _LnXPCPortSpeed_Type(Integer32):
    """Custom type lnXPCPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnXPCPortSpeed_Type.__name__ = "Integer32"
_LnXPCPortSpeed_Object = MibTableColumn
lnXPCPortSpeed = _LnXPCPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 5),
    _LnXPCPortSpeed_Type()
)
lnXPCPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCPortSpeed.setStatus("mandatory")


class _LnXPCActiveSessions_Type(Integer32):
    """Custom type lnXPCActiveSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnXPCActiveSessions_Type.__name__ = "Integer32"
_LnXPCActiveSessions_Object = MibTableColumn
lnXPCActiveSessions = _LnXPCActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 6),
    _LnXPCActiveSessions_Type()
)
lnXPCActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCActiveSessions.setStatus("mandatory")


class _LnXPCKiloBytesReceived_Type(Integer32):
    """Custom type lnXPCKiloBytesReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnXPCKiloBytesReceived_Type.__name__ = "Integer32"
_LnXPCKiloBytesReceived_Object = MibTableColumn
lnXPCKiloBytesReceived = _LnXPCKiloBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 7),
    _LnXPCKiloBytesReceived_Type()
)
lnXPCKiloBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCKiloBytesReceived.setStatus("mandatory")


class _LnXPCKiloBytesSent_Type(Integer32):
    """Custom type lnXPCKiloBytesSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnXPCKiloBytesSent_Type.__name__ = "Integer32"
_LnXPCKiloBytesSent_Object = MibTableColumn
lnXPCKiloBytesSent = _LnXPCKiloBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 8),
    _LnXPCKiloBytesSent_Type()
)
lnXPCKiloBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCKiloBytesSent.setStatus("mandatory")


class _LnXPCMsgsReceived_Type(Integer32):
    """Custom type lnXPCMsgsReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnXPCMsgsReceived_Type.__name__ = "Integer32"
_LnXPCMsgsReceived_Object = MibTableColumn
lnXPCMsgsReceived = _LnXPCMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 9),
    _LnXPCMsgsReceived_Type()
)
lnXPCMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCMsgsReceived.setStatus("mandatory")


class _LnXPCMsgsSent_Type(Integer32):
    """Custom type lnXPCMsgsSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnXPCMsgsSent_Type.__name__ = "Integer32"
_LnXPCMsgsSent_Object = MibTableColumn
lnXPCMsgsSent = _LnXPCMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 10),
    _LnXPCMsgsSent_Type()
)
lnXPCMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCMsgsSent.setStatus("mandatory")


class _LnXPCCRCErrors_Type(Integer32):
    """Custom type lnXPCCRCErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnXPCCRCErrors_Type.__name__ = "Integer32"
_LnXPCCRCErrors_Object = MibTableColumn
lnXPCCRCErrors = _LnXPCCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 11),
    _LnXPCCRCErrors_Type()
)
lnXPCCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCCRCErrors.setStatus("mandatory")


class _LnXPCPortErrors_Type(Integer32):
    """Custom type lnXPCPortErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnXPCPortErrors_Type.__name__ = "Integer32"
_LnXPCPortErrors_Object = MibTableColumn
lnXPCPortErrors = _LnXPCPortErrors_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 12),
    _LnXPCPortErrors_Type()
)
lnXPCPortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCPortErrors.setStatus("mandatory")


class _LnXPCRetransmissions_Type(Integer32):
    """Custom type lnXPCRetransmissions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnXPCRetransmissions_Type.__name__ = "Integer32"
_LnXPCRetransmissions_Object = MibTableColumn
lnXPCRetransmissions = _LnXPCRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 3, 1, 13),
    _LnXPCRetransmissions_Type()
)
lnXPCRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnXPCRetransmissions.setStatus("mandatory")


class _LnAppleTalkStatsLogged_Type(Integer32):
    """Custom type lnAppleTalkStatsLogged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnAppleTalkStatsLogged_Type.__name__ = "Integer32"
_LnAppleTalkStatsLogged_Object = MibScalar
lnAppleTalkStatsLogged = _LnAppleTalkStatsLogged_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 4),
    _LnAppleTalkStatsLogged_Type()
)
lnAppleTalkStatsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnAppleTalkStatsLogged.setStatus("optional")


class _LnNetWareSPXIIStatsLogged_Type(Integer32):
    """Custom type lnNetWareSPXIIStatsLogged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnNetWareSPXIIStatsLogged_Type.__name__ = "Integer32"
_LnNetWareSPXIIStatsLogged_Object = MibScalar
lnNetWareSPXIIStatsLogged = _LnNetWareSPXIIStatsLogged_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 5),
    _LnNetWareSPXIIStatsLogged_Type()
)
lnNetWareSPXIIStatsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetWareSPXIIStatsLogged.setStatus("optional")
_LnNetPortTable_Object = MibTable
lnNetPortTable = _LnNetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6)
)
if mibBuilder.loadTexts:
    lnNetPortTable.setStatus("mandatory")
_LnNetPortEntry_Object = MibTableRow
lnNetPortEntry = _LnNetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1)
)
lnNetPortEntry.setIndexNames(
    (0, "NOTES-MIB", "lnNetPortIndex"),
)
if mibBuilder.loadTexts:
    lnNetPortEntry.setStatus("mandatory")


class _LnNetPortIndex_Type(Integer32):
    """Custom type lnNetPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnNetPortIndex_Type.__name__ = "Integer32"
_LnNetPortIndex_Object = MibTableColumn
lnNetPortIndex = _LnNetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 1),
    _LnNetPortIndex_Type()
)
lnNetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortIndex.setStatus("mandatory")
_LnNetPortName_Type = DisplayString
_LnNetPortName_Object = MibTableColumn
lnNetPortName = _LnNetPortName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 2),
    _LnNetPortName_Type()
)
lnNetPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortName.setStatus("mandatory")


class _LnNetPortKBytesRec_Type(Integer32):
    """Custom type lnNetPortKBytesRec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnNetPortKBytesRec_Type.__name__ = "Integer32"
_LnNetPortKBytesRec_Object = MibTableColumn
lnNetPortKBytesRec = _LnNetPortKBytesRec_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 3),
    _LnNetPortKBytesRec_Type()
)
lnNetPortKBytesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortKBytesRec.setStatus("mandatory")


class _LnNetPortKBytesSent_Type(Integer32):
    """Custom type lnNetPortKBytesSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnNetPortKBytesSent_Type.__name__ = "Integer32"
_LnNetPortKBytesSent_Object = MibTableColumn
lnNetPortKBytesSent = _LnNetPortKBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 4),
    _LnNetPortKBytesSent_Type()
)
lnNetPortKBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortKBytesSent.setStatus("mandatory")


class _LnNetPortSessEstIn_Type(Integer32):
    """Custom type lnNetPortSessEstIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnNetPortSessEstIn_Type.__name__ = "Integer32"
_LnNetPortSessEstIn_Object = MibTableColumn
lnNetPortSessEstIn = _LnNetPortSessEstIn_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 5),
    _LnNetPortSessEstIn_Type()
)
lnNetPortSessEstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortSessEstIn.setStatus("mandatory")


class _LnNetPortSessEstOut_Type(Integer32):
    """Custom type lnNetPortSessEstOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnNetPortSessEstOut_Type.__name__ = "Integer32"
_LnNetPortSessEstOut_Object = MibTableColumn
lnNetPortSessEstOut = _LnNetPortSessEstOut_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 6),
    _LnNetPortSessEstOut_Type()
)
lnNetPortSessEstOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortSessEstOut.setStatus("mandatory")


class _LnNetPortSessLimit_Type(Integer32):
    """Custom type lnNetPortSessLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnNetPortSessLimit_Type.__name__ = "Integer32"
_LnNetPortSessLimit_Object = MibTableColumn
lnNetPortSessLimit = _LnNetPortSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 7),
    _LnNetPortSessLimit_Type()
)
lnNetPortSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortSessLimit.setStatus("mandatory")


class _LnNetPortSessLimitMax_Type(Integer32):
    """Custom type lnNetPortSessLimitMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnNetPortSessLimitMax_Type.__name__ = "Integer32"
_LnNetPortSessLimitMax_Object = MibTableColumn
lnNetPortSessLimitMax = _LnNetPortSessLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 8),
    _LnNetPortSessLimitMax_Type()
)
lnNetPortSessLimitMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortSessLimitMax.setStatus("mandatory")


class _LnNetPortSessLimitMin_Type(Integer32):
    """Custom type lnNetPortSessLimitMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnNetPortSessLimitMin_Type.__name__ = "Integer32"
_LnNetPortSessLimitMin_Object = MibTableColumn
lnNetPortSessLimitMin = _LnNetPortSessLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 9),
    _LnNetPortSessLimitMin_Type()
)
lnNetPortSessLimitMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortSessLimitMin.setStatus("mandatory")


class _LnNetPortSessPeak_Type(Integer32):
    """Custom type lnNetPortSessPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnNetPortSessPeak_Type.__name__ = "Integer32"
_LnNetPortSessPeak_Object = MibTableColumn
lnNetPortSessPeak = _LnNetPortSessPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 10),
    _LnNetPortSessPeak_Type()
)
lnNetPortSessPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortSessPeak.setStatus("mandatory")


class _LnNetPortSessRecycled_Type(Integer32):
    """Custom type lnNetPortSessRecycled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnNetPortSessRecycled_Type.__name__ = "Integer32"
_LnNetPortSessRecycled_Object = MibTableColumn
lnNetPortSessRecycled = _LnNetPortSessRecycled_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 11),
    _LnNetPortSessRecycled_Type()
)
lnNetPortSessRecycled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortSessRecycled.setStatus("mandatory")


class _LnNetPortSessRecycling_Type(Integer32):
    """Custom type lnNetPortSessRecycling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnNetPortSessRecycling_Type.__name__ = "Integer32"
_LnNetPortSessRecycling_Object = MibTableColumn
lnNetPortSessRecycling = _LnNetPortSessRecycling_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 12),
    _LnNetPortSessRecycling_Type()
)
lnNetPortSessRecycling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNetPortSessRecycling.setStatus("mandatory")


class _LnSNARemoteLU_Type(Integer32):
    """Custom type lnSNARemoteLU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNARemoteLU_Type.__name__ = "Integer32"
_LnSNARemoteLU_Object = MibTableColumn
lnSNARemoteLU = _LnSNARemoteLU_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 13),
    _LnSNARemoteLU_Type()
)
lnSNARemoteLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNARemoteLU.setStatus("optional")


class _LnSNALocalLU_Type(Integer32):
    """Custom type lnSNALocalLU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNALocalLU_Type.__name__ = "Integer32"
_LnSNALocalLU_Object = MibTableColumn
lnSNALocalLU = _LnSNALocalLU_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 14),
    _LnSNALocalLU_Type()
)
lnSNALocalLU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNALocalLU.setStatus("optional")


class _LnSNALNCVersion_Type(Integer32):
    """Custom type lnSNALNCVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNALNCVersion_Type.__name__ = "Integer32"
_LnSNALNCVersion_Object = MibTableColumn
lnSNALNCVersion = _LnSNALNCVersion_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 15),
    _LnSNALNCVersion_Type()
)
lnSNALNCVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNALNCVersion.setStatus("optional")


class _LnSNAVersion_Type(Integer32):
    """Custom type lnSNAVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNAVersion_Type.__name__ = "Integer32"
_LnSNAVersion_Object = MibTableColumn
lnSNAVersion = _LnSNAVersion_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 16),
    _LnSNAVersion_Type()
)
lnSNAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNAVersion.setStatus("optional")


class _LnSNAMaxSessions_Type(Integer32):
    """Custom type lnSNAMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNAMaxSessions_Type.__name__ = "Integer32"
_LnSNAMaxSessions_Object = MibTableColumn
lnSNAMaxSessions = _LnSNAMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 17),
    _LnSNAMaxSessions_Type()
)
lnSNAMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNAMaxSessions.setStatus("optional")


class _LnSNAActiveSessions_Type(Integer32):
    """Custom type lnSNAActiveSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNAActiveSessions_Type.__name__ = "Integer32"
_LnSNAActiveSessions_Object = MibTableColumn
lnSNAActiveSessions = _LnSNAActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 18),
    _LnSNAActiveSessions_Type()
)
lnSNAActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNAActiveSessions.setStatus("optional")


class _LnSNATPType_Type(Integer32):
    """Custom type lnSNATPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNATPType_Type.__name__ = "Integer32"
_LnSNATPType_Object = MibTableColumn
lnSNATPType = _LnSNATPType_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 19),
    _LnSNATPType_Type()
)
lnSNATPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNATPType.setStatus("optional")


class _LnSNATPState_Type(Integer32):
    """Custom type lnSNATPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNATPState_Type.__name__ = "Integer32"
_LnSNATPState_Object = MibTableColumn
lnSNATPState = _LnSNATPState_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 20),
    _LnSNATPState_Type()
)
lnSNATPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNATPState.setStatus("optional")


class _LnSNAConversationId_Type(Integer32):
    """Custom type lnSNAConversationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNAConversationId_Type.__name__ = "Integer32"
_LnSNAConversationId_Object = MibTableColumn
lnSNAConversationId = _LnSNAConversationId_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 21),
    _LnSNAConversationId_Type()
)
lnSNAConversationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNAConversationId.setStatus("optional")


class _LnSNAMaxSendRUSize_Type(Integer32):
    """Custom type lnSNAMaxSendRUSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNAMaxSendRUSize_Type.__name__ = "Integer32"
_LnSNAMaxSendRUSize_Object = MibTableColumn
lnSNAMaxSendRUSize = _LnSNAMaxSendRUSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 22),
    _LnSNAMaxSendRUSize_Type()
)
lnSNAMaxSendRUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNAMaxSendRUSize.setStatus("optional")


class _LnSNAMaxRcvRUSize_Type(Integer32):
    """Custom type lnSNAMaxRcvRUSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNAMaxRcvRUSize_Type.__name__ = "Integer32"
_LnSNAMaxRcvRUSize_Object = MibTableColumn
lnSNAMaxRcvRUSize = _LnSNAMaxRcvRUSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 23),
    _LnSNAMaxRcvRUSize_Type()
)
lnSNAMaxRcvRUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNAMaxRcvRUSize.setStatus("optional")


class _LnSNASendPacingSize_Type(Integer32):
    """Custom type lnSNASendPacingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNASendPacingSize_Type.__name__ = "Integer32"
_LnSNASendPacingSize_Object = MibTableColumn
lnSNASendPacingSize = _LnSNASendPacingSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 24),
    _LnSNASendPacingSize_Type()
)
lnSNASendPacingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNASendPacingSize.setStatus("optional")


class _LnSNARcvPacingSize_Type(Integer32):
    """Custom type lnSNARcvPacingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNARcvPacingSize_Type.__name__ = "Integer32"
_LnSNARcvPacingSize_Object = MibTableColumn
lnSNARcvPacingSize = _LnSNARcvPacingSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 25),
    _LnSNARcvPacingSize_Type()
)
lnSNARcvPacingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNARcvPacingSize.setStatus("optional")


class _LnSNAPacingType_Type(Integer32):
    """Custom type lnSNAPacingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnSNAPacingType_Type.__name__ = "Integer32"
_LnSNAPacingType_Object = MibTableColumn
lnSNAPacingType = _LnSNAPacingType_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 26),
    _LnSNAPacingType_Type()
)
lnSNAPacingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnSNAPacingType.setStatus("optional")


class _LnX25LocalResets_Type(Integer32):
    """Custom type lnX25LocalResets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25LocalResets_Type.__name__ = "Integer32"
_LnX25LocalResets_Object = MibTableColumn
lnX25LocalResets = _LnX25LocalResets_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 27),
    _LnX25LocalResets_Type()
)
lnX25LocalResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25LocalResets.setStatus("optional")


class _LnX25RemoteResets_Type(Integer32):
    """Custom type lnX25RemoteResets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25RemoteResets_Type.__name__ = "Integer32"
_LnX25RemoteResets_Object = MibTableColumn
lnX25RemoteResets = _LnX25RemoteResets_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 28),
    _LnX25RemoteResets_Type()
)
lnX25RemoteResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25RemoteResets.setStatus("optional")


class _LnX25WindowSize_Type(Integer32):
    """Custom type lnX25WindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25WindowSize_Type.__name__ = "Integer32"
_LnX25WindowSize_Object = MibTableColumn
lnX25WindowSize = _LnX25WindowSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 29),
    _LnX25WindowSize_Type()
)
lnX25WindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25WindowSize.setStatus("optional")


class _LnX25FrameSize_Type(Integer32):
    """Custom type lnX25FrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25FrameSize_Type.__name__ = "Integer32"
_LnX25FrameSize_Object = MibTableColumn
lnX25FrameSize = _LnX25FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 30),
    _LnX25FrameSize_Type()
)
lnX25FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25FrameSize.setStatus("optional")


class _LnX25PktSize_Type(Integer32):
    """Custom type lnX25PktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25PktSize_Type.__name__ = "Integer32"
_LnX25PktSize_Object = MibTableColumn
lnX25PktSize = _LnX25PktSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 31),
    _LnX25PktSize_Type()
)
lnX25PktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25PktSize.setStatus("optional")


class _LnX25UnderRuns_Type(Integer32):
    """Custom type lnX25UnderRuns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25UnderRuns_Type.__name__ = "Integer32"
_LnX25UnderRuns_Object = MibTableColumn
lnX25UnderRuns = _LnX25UnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 32),
    _LnX25UnderRuns_Type()
)
lnX25UnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25UnderRuns.setStatus("optional")


class _LnX25OverRuns_Type(Integer32):
    """Custom type lnX25OverRuns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25OverRuns_Type.__name__ = "Integer32"
_LnX25OverRuns_Object = MibTableColumn
lnX25OverRuns = _LnX25OverRuns_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 33),
    _LnX25OverRuns_Type()
)
lnX25OverRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25OverRuns.setStatus("optional")


class _LnX25REJTran_Type(Integer32):
    """Custom type lnX25REJTran based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25REJTran_Type.__name__ = "Integer32"
_LnX25REJTran_Object = MibTableColumn
lnX25REJTran = _LnX25REJTran_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 34),
    _LnX25REJTran_Type()
)
lnX25REJTran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25REJTran.setStatus("optional")


class _LnX25REJRcv_Type(Integer32):
    """Custom type lnX25REJRcv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25REJRcv_Type.__name__ = "Integer32"
_LnX25REJRcv_Object = MibTableColumn
lnX25REJRcv = _LnX25REJRcv_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 35),
    _LnX25REJRcv_Type()
)
lnX25REJRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25REJRcv.setStatus("optional")


class _LnX25VCCfg_Type(Integer32):
    """Custom type lnX25VCCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25VCCfg_Type.__name__ = "Integer32"
_LnX25VCCfg_Object = MibTableColumn
lnX25VCCfg = _LnX25VCCfg_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 36),
    _LnX25VCCfg_Type()
)
lnX25VCCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25VCCfg.setStatus("optional")


class _LnX25VCInUse_Type(Integer32):
    """Custom type lnX25VCInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25VCInUse_Type.__name__ = "Integer32"
_LnX25VCInUse_Object = MibTableColumn
lnX25VCInUse = _LnX25VCInUse_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 37),
    _LnX25VCInUse_Type()
)
lnX25VCInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25VCInUse.setStatus("optional")


class _LnX25CRCErrors_Type(Integer32):
    """Custom type lnX25CRCErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25CRCErrors_Type.__name__ = "Integer32"
_LnX25CRCErrors_Object = MibTableColumn
lnX25CRCErrors = _LnX25CRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 38),
    _LnX25CRCErrors_Type()
)
lnX25CRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25CRCErrors.setStatus("optional")


class _LnX25LocalDTEAddress_Type(Integer32):
    """Custom type lnX25LocalDTEAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LnX25LocalDTEAddress_Type.__name__ = "Integer32"
_LnX25LocalDTEAddress_Object = MibTableColumn
lnX25LocalDTEAddress = _LnX25LocalDTEAddress_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 7, 6, 1, 39),
    _LnX25LocalDTEAddress_Type()
)
lnX25LocalDTEAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnX25LocalDTEAddress.setStatus("optional")
_LnDisk_ObjectIdentity = ObjectIdentity
lnDisk = _LnDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 8)
)


class _LnDiskFixed_Type(Integer32):
    """Custom type lnDiskFixed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDiskFixed_Type.__name__ = "Integer32"
_LnDiskFixed_Object = MibScalar
lnDiskFixed = _LnDiskFixed_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 8, 1),
    _LnDiskFixed_Type()
)
lnDiskFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDiskFixed.setStatus("mandatory")


class _LnDiskFreeSwap_Type(Integer32):
    """Custom type lnDiskFreeSwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDiskFreeSwap_Type.__name__ = "Integer32"
_LnDiskFreeSwap_Object = MibScalar
lnDiskFreeSwap = _LnDiskFreeSwap_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 8, 2),
    _LnDiskFreeSwap_Type()
)
lnDiskFreeSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDiskFreeSwap.setStatus("optional")
_LnDriveTable_Object = MibTable
lnDriveTable = _LnDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    lnDriveTable.setStatus("mandatory")
_LnDriveEntry_Object = MibTableRow
lnDriveEntry = _LnDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 8, 3, 1)
)
lnDriveEntry.setIndexNames(
    (0, "NOTES-MIB", "lnDriveIndex"),
)
if mibBuilder.loadTexts:
    lnDriveEntry.setStatus("mandatory")


class _LnDriveIndex_Type(Integer32):
    """Custom type lnDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnDriveIndex_Type.__name__ = "Integer32"
_LnDriveIndex_Object = MibTableColumn
lnDriveIndex = _LnDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 8, 3, 1, 1),
    _LnDriveIndex_Type()
)
lnDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDriveIndex.setStatus("mandatory")
_LnDriveLetter_Type = DisplayString
_LnDriveLetter_Object = MibTableColumn
lnDriveLetter = _LnDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 8, 3, 1, 2),
    _LnDriveLetter_Type()
)
lnDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDriveLetter.setStatus("mandatory")


class _LnDriveSize_Type(Integer32):
    """Custom type lnDriveSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDriveSize_Type.__name__ = "Integer32"
_LnDriveSize_Object = MibTableColumn
lnDriveSize = _LnDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 8, 3, 1, 3),
    _LnDriveSize_Type()
)
lnDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDriveSize.setStatus("mandatory")


class _LnDriveFree_Type(Integer32):
    """Custom type lnDriveFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDriveFree_Type.__name__ = "Integer32"
_LnDriveFree_Object = MibTableColumn
lnDriveFree = _LnDriveFree_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 8, 3, 1, 4),
    _LnDriveFree_Type()
)
lnDriveFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDriveFree.setStatus("mandatory")


class _LnDiskRemote_Type(Integer32):
    """Custom type lnDiskRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDiskRemote_Type.__name__ = "Integer32"
_LnDiskRemote_Object = MibScalar
lnDiskRemote = _LnDiskRemote_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 8, 4),
    _LnDiskRemote_Type()
)
lnDiskRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDiskRemote.setStatus("optional")
_LnMem_ObjectIdentity = ObjectIdentity
lnMem = _LnMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 9)
)


class _LnMemAllocTotal_Type(Integer32):
    """Custom type lnMemAllocTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMemAllocTotal_Type.__name__ = "Integer32"
_LnMemAllocTotal_Object = MibScalar
lnMemAllocTotal = _LnMemAllocTotal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 9, 1),
    _LnMemAllocTotal_Type()
)
lnMemAllocTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMemAllocTotal.setStatus("mandatory")


class _LnMemAllocProcess_Type(Integer32):
    """Custom type lnMemAllocProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMemAllocProcess_Type.__name__ = "Integer32"
_LnMemAllocProcess_Object = MibScalar
lnMemAllocProcess = _LnMemAllocProcess_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 9, 2),
    _LnMemAllocProcess_Type()
)
lnMemAllocProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMemAllocProcess.setStatus("mandatory")


class _LnMemAllocShared_Type(Integer32):
    """Custom type lnMemAllocShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMemAllocShared_Type.__name__ = "Integer32"
_LnMemAllocShared_Object = MibScalar
lnMemAllocShared = _LnMemAllocShared_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 9, 3),
    _LnMemAllocShared_Type()
)
lnMemAllocShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMemAllocShared.setStatus("mandatory")
_LnMemAvailability_Type = DisplayString
_LnMemAvailability_Object = MibScalar
lnMemAvailability = _LnMemAvailability_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 9, 4),
    _LnMemAvailability_Type()
)
lnMemAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMemAvailability.setStatus("mandatory")


class _LnMemFree_Type(Integer32):
    """Custom type lnMemFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMemFree_Type.__name__ = "Integer32"
_LnMemFree_Object = MibScalar
lnMemFree = _LnMemFree_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 9, 5),
    _LnMemFree_Type()
)
lnMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMemFree.setStatus("mandatory")


class _LnMemSwapSize_Type(Integer32):
    """Custom type lnMemSwapSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMemSwapSize_Type.__name__ = "Integer32"
_LnMemSwapSize_Object = MibScalar
lnMemSwapSize = _LnMemSwapSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 9, 6),
    _LnMemSwapSize_Type()
)
lnMemSwapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMemSwapSize.setStatus("optional")


class _LnMemPhysicalRAM_Type(Integer32):
    """Custom type lnMemPhysicalRAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMemPhysicalRAM_Type.__name__ = "Integer32"
_LnMemPhysicalRAM_Object = MibScalar
lnMemPhysicalRAM = _LnMemPhysicalRAM_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 9, 7),
    _LnMemPhysicalRAM_Type()
)
lnMemPhysicalRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMemPhysicalRAM.setStatus("optional")
_LnDatabase_ObjectIdentity = ObjectIdentity
lnDatabase = _LnDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10)
)


class _LnDBBufferControlPoolSize_Type(Integer32):
    """Custom type lnDBBufferControlPoolSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBBufferControlPoolSize_Type.__name__ = "Integer32"
_LnDBBufferControlPoolSize_Object = MibScalar
lnDBBufferControlPoolSize = _LnDBBufferControlPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 1),
    _LnDBBufferControlPoolSize_Type()
)
lnDBBufferControlPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBBufferControlPoolSize.setStatus("optional")


class _LnDBBufferControlPoolUsed_Type(Integer32):
    """Custom type lnDBBufferControlPoolUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBBufferControlPoolUsed_Type.__name__ = "Integer32"
_LnDBBufferControlPoolUsed_Object = MibScalar
lnDBBufferControlPoolUsed = _LnDBBufferControlPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 2),
    _LnDBBufferControlPoolUsed_Type()
)
lnDBBufferControlPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBBufferControlPoolUsed.setStatus("optional")


class _LnDBBufferPoolAllocated_Type(Integer32):
    """Custom type lnDBBufferPoolAllocated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBBufferPoolAllocated_Type.__name__ = "Integer32"
_LnDBBufferPoolAllocated_Object = MibScalar
lnDBBufferPoolAllocated = _LnDBBufferPoolAllocated_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 3),
    _LnDBBufferPoolAllocated_Type()
)
lnDBBufferPoolAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBBufferPoolAllocated.setStatus("optional")


class _LnDBBufferPoolMaximum_Type(Integer32):
    """Custom type lnDBBufferPoolMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBBufferPoolMaximum_Type.__name__ = "Integer32"
_LnDBBufferPoolMaximum_Object = MibScalar
lnDBBufferPoolMaximum = _LnDBBufferPoolMaximum_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 4),
    _LnDBBufferPoolMaximum_Type()
)
lnDBBufferPoolMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBBufferPoolMaximum.setStatus("optional")


class _LnDBBufferPoolUsed_Type(Integer32):
    """Custom type lnDBBufferPoolUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBBufferPoolUsed_Type.__name__ = "Integer32"
_LnDBBufferPoolUsed_Object = MibScalar
lnDBBufferPoolUsed = _LnDBBufferPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 5),
    _LnDBBufferPoolUsed_Type()
)
lnDBBufferPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBBufferPoolUsed.setStatus("optional")


class _LnDBNSFPoolSize_Type(Integer32):
    """Custom type lnDBNSFPoolSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBNSFPoolSize_Type.__name__ = "Integer32"
_LnDBNSFPoolSize_Object = MibScalar
lnDBNSFPoolSize = _LnDBNSFPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 6),
    _LnDBNSFPoolSize_Type()
)
lnDBNSFPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBNSFPoolSize.setStatus("optional")


class _LnDBNSFPoolUsed_Type(Integer32):
    """Custom type lnDBNSFPoolUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBNSFPoolUsed_Type.__name__ = "Integer32"
_LnDBNSFPoolUsed_Object = MibScalar
lnDBNSFPoolUsed = _LnDBNSFPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 7),
    _LnDBNSFPoolUsed_Type()
)
lnDBNSFPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBNSFPoolUsed.setStatus("optional")


class _LnDBBufferPoolPercentReadsInBuffer_Type(Integer32):
    """Custom type lnDBBufferPoolPercentReadsInBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBBufferPoolPercentReadsInBuffer_Type.__name__ = "Integer32"
_LnDBBufferPoolPercentReadsInBuffer_Object = MibScalar
lnDBBufferPoolPercentReadsInBuffer = _LnDBBufferPoolPercentReadsInBuffer_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 8),
    _LnDBBufferPoolPercentReadsInBuffer_Type()
)
lnDBBufferPoolPercentReadsInBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBBufferPoolPercentReadsInBuffer.setStatus("optional")


class _LnDBBufferPoolReads_Type(Integer32):
    """Custom type lnDBBufferPoolReads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBBufferPoolReads_Type.__name__ = "Integer32"
_LnDBBufferPoolReads_Object = MibScalar
lnDBBufferPoolReads = _LnDBBufferPoolReads_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 9),
    _LnDBBufferPoolReads_Type()
)
lnDBBufferPoolReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBBufferPoolReads.setStatus("optional")


class _LnDBBufferPoolWrites_Type(Integer32):
    """Custom type lnDBBufferPoolWrites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBBufferPoolWrites_Type.__name__ = "Integer32"
_LnDBBufferPoolWrites_Object = MibScalar
lnDBBufferPoolWrites = _LnDBBufferPoolWrites_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 10),
    _LnDBBufferPoolWrites_Type()
)
lnDBBufferPoolWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBBufferPoolWrites.setStatus("optional")


class _LnDBNIFPoolSize_Type(Integer32):
    """Custom type lnDBNIFPoolSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBNIFPoolSize_Type.__name__ = "Integer32"
_LnDBNIFPoolSize_Object = MibScalar
lnDBNIFPoolSize = _LnDBNIFPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 11),
    _LnDBNIFPoolSize_Type()
)
lnDBNIFPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBNIFPoolSize.setStatus("optional")


class _LnDBNIFPoolUsed_Type(Integer32):
    """Custom type lnDBNIFPoolUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBNIFPoolUsed_Type.__name__ = "Integer32"
_LnDBNIFPoolUsed_Object = MibScalar
lnDBNIFPoolUsed = _LnDBNIFPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 12),
    _LnDBNIFPoolUsed_Type()
)
lnDBNIFPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBNIFPoolUsed.setStatus("optional")


class _LnDBNIFPoolPeak_Type(Integer32):
    """Custom type lnDBNIFPoolPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBNIFPoolPeak_Type.__name__ = "Integer32"
_LnDBNIFPoolPeak_Object = MibScalar
lnDBNIFPoolPeak = _LnDBNIFPoolPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 13),
    _LnDBNIFPoolPeak_Type()
)
lnDBNIFPoolPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBNIFPoolPeak.setStatus("optional")


class _LnDBNSFPoolPeak_Type(Integer32):
    """Custom type lnDBNSFPoolPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBNSFPoolPeak_Type.__name__ = "Integer32"
_LnDBNSFPoolPeak_Object = MibScalar
lnDBNSFPoolPeak = _LnDBNSFPoolPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 14),
    _LnDBNSFPoolPeak_Type()
)
lnDBNSFPoolPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBNSFPoolPeak.setStatus("optional")


class _LnDBCacheCurrentEntries_Type(Integer32):
    """Custom type lnDBCacheCurrentEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBCacheCurrentEntries_Type.__name__ = "Integer32"
_LnDBCacheCurrentEntries_Object = MibScalar
lnDBCacheCurrentEntries = _LnDBCacheCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 15),
    _LnDBCacheCurrentEntries_Type()
)
lnDBCacheCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBCacheCurrentEntries.setStatus("optional")


class _LnDBCacheHighWaterMark_Type(Integer32):
    """Custom type lnDBCacheHighWaterMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBCacheHighWaterMark_Type.__name__ = "Integer32"
_LnDBCacheHighWaterMark_Object = MibScalar
lnDBCacheHighWaterMark = _LnDBCacheHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 16),
    _LnDBCacheHighWaterMark_Type()
)
lnDBCacheHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBCacheHighWaterMark.setStatus("optional")


class _LnDBCacheHits_Type(Integer32):
    """Custom type lnDBCacheHits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBCacheHits_Type.__name__ = "Integer32"
_LnDBCacheHits_Object = MibScalar
lnDBCacheHits = _LnDBCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 17),
    _LnDBCacheHits_Type()
)
lnDBCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBCacheHits.setStatus("optional")


class _LnDBCacheInitialDbOpens_Type(Integer32):
    """Custom type lnDBCacheInitialDbOpens based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBCacheInitialDbOpens_Type.__name__ = "Integer32"
_LnDBCacheInitialDbOpens_Object = MibScalar
lnDBCacheInitialDbOpens = _LnDBCacheInitialDbOpens_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 18),
    _LnDBCacheInitialDbOpens_Type()
)
lnDBCacheInitialDbOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBCacheInitialDbOpens.setStatus("optional")


class _LnDBCacheLookups_Type(Integer32):
    """Custom type lnDBCacheLookups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBCacheLookups_Type.__name__ = "Integer32"
_LnDBCacheLookups_Object = MibScalar
lnDBCacheLookups = _LnDBCacheLookups_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 19),
    _LnDBCacheLookups_Type()
)
lnDBCacheLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBCacheLookups.setStatus("optional")


class _LnDBCacheMaxEntries_Type(Integer32):
    """Custom type lnDBCacheMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBCacheMaxEntries_Type.__name__ = "Integer32"
_LnDBCacheMaxEntries_Object = MibScalar
lnDBCacheMaxEntries = _LnDBCacheMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 20),
    _LnDBCacheMaxEntries_Type()
)
lnDBCacheMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBCacheMaxEntries.setStatus("optional")


class _LnDBCacheOvercrowdingRejections_Type(Integer32):
    """Custom type lnDBCacheOvercrowdingRejections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBCacheOvercrowdingRejections_Type.__name__ = "Integer32"
_LnDBCacheOvercrowdingRejections_Object = MibScalar
lnDBCacheOvercrowdingRejections = _LnDBCacheOvercrowdingRejections_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 21),
    _LnDBCacheOvercrowdingRejections_Type()
)
lnDBCacheOvercrowdingRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBCacheOvercrowdingRejections.setStatus("optional")


class _LnDBBufferControlPoolPeak_Type(Integer32):
    """Custom type lnDBBufferControlPoolPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDBBufferControlPoolPeak_Type.__name__ = "Integer32"
_LnDBBufferControlPoolPeak_Object = MibScalar
lnDBBufferControlPoolPeak = _LnDBBufferControlPoolPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 10, 22),
    _LnDBBufferControlPoolPeak_Type()
)
lnDBBufferControlPoolPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDBBufferControlPoolPeak.setStatus("optional")
_LnAgentMgr_ObjectIdentity = ObjectIdentity
lnAgentMgr = _LnAgentMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 11)
)


class _LnDailyAccessDenials_Type(Integer32):
    """Custom type lnDailyAccessDenials based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDailyAccessDenials_Type.__name__ = "Integer32"
_LnDailyAccessDenials_Object = MibScalar
lnDailyAccessDenials = _LnDailyAccessDenials_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 11, 1),
    _LnDailyAccessDenials_Type()
)
lnDailyAccessDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDailyAccessDenials.setStatus("optional")


class _LnDailyScheduledRuns_Type(Integer32):
    """Custom type lnDailyScheduledRuns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDailyScheduledRuns_Type.__name__ = "Integer32"
_LnDailyScheduledRuns_Object = MibScalar
lnDailyScheduledRuns = _LnDailyScheduledRuns_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 11, 2),
    _LnDailyScheduledRuns_Type()
)
lnDailyScheduledRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDailyScheduledRuns.setStatus("optional")


class _LnDailyTriggeredRuns_Type(Integer32):
    """Custom type lnDailyTriggeredRuns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDailyTriggeredRuns_Type.__name__ = "Integer32"
_LnDailyTriggeredRuns_Object = MibScalar
lnDailyTriggeredRuns = _LnDailyTriggeredRuns_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 11, 3),
    _LnDailyTriggeredRuns_Type()
)
lnDailyTriggeredRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDailyTriggeredRuns.setStatus("optional")


class _LnDailyUnsuccessfulRuns_Type(Integer32):
    """Custom type lnDailyUnsuccessfulRuns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnDailyUnsuccessfulRuns_Type.__name__ = "Integer32"
_LnDailyUnsuccessfulRuns_Object = MibScalar
lnDailyUnsuccessfulRuns = _LnDailyUnsuccessfulRuns_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 11, 4),
    _LnDailyUnsuccessfulRuns_Type()
)
lnDailyUnsuccessfulRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDailyUnsuccessfulRuns.setStatus("optional")
_LnDailyUsedRunTime_Type = DisplayString
_LnDailyUsedRunTime_Object = MibScalar
lnDailyUsedRunTime = _LnDailyUsedRunTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 11, 5),
    _LnDailyUsedRunTime_Type()
)
lnDailyUsedRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDailyUsedRunTime.setStatus("optional")


class _LnHourlyAccessDenials_Type(Integer32):
    """Custom type lnHourlyAccessDenials based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnHourlyAccessDenials_Type.__name__ = "Integer32"
_LnHourlyAccessDenials_Object = MibScalar
lnHourlyAccessDenials = _LnHourlyAccessDenials_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 11, 6),
    _LnHourlyAccessDenials_Type()
)
lnHourlyAccessDenials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnHourlyAccessDenials.setStatus("optional")


class _LnHourlyScheduledRuns_Type(Integer32):
    """Custom type lnHourlyScheduledRuns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnHourlyScheduledRuns_Type.__name__ = "Integer32"
_LnHourlyScheduledRuns_Object = MibScalar
lnHourlyScheduledRuns = _LnHourlyScheduledRuns_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 11, 7),
    _LnHourlyScheduledRuns_Type()
)
lnHourlyScheduledRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnHourlyScheduledRuns.setStatus("optional")


class _LnHourlyTriggeredRuns_Type(Integer32):
    """Custom type lnHourlyTriggeredRuns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnHourlyTriggeredRuns_Type.__name__ = "Integer32"
_LnHourlyTriggeredRuns_Object = MibScalar
lnHourlyTriggeredRuns = _LnHourlyTriggeredRuns_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 11, 8),
    _LnHourlyTriggeredRuns_Type()
)
lnHourlyTriggeredRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnHourlyTriggeredRuns.setStatus("optional")


class _LnHourlyUnsuccessfulRuns_Type(Integer32):
    """Custom type lnHourlyUnsuccessfulRuns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnHourlyUnsuccessfulRuns_Type.__name__ = "Integer32"
_LnHourlyUnsuccessfulRuns_Object = MibScalar
lnHourlyUnsuccessfulRuns = _LnHourlyUnsuccessfulRuns_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 11, 9),
    _LnHourlyUnsuccessfulRuns_Type()
)
lnHourlyUnsuccessfulRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnHourlyUnsuccessfulRuns.setStatus("optional")
_LnHourlyUsedRunTime_Type = DisplayString
_LnHourlyUsedRunTime_Object = MibScalar
lnHourlyUsedRunTime = _LnHourlyUsedRunTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 11, 10),
    _LnHourlyUsedRunTime_Type()
)
lnHourlyUsedRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnHourlyUsedRunTime.setStatus("optional")
_LnMTA_ObjectIdentity = ObjectIdentity
lnMTA = _LnMTA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12)
)
_LnMTATable_Object = MibTable
lnMTATable = _LnMTATable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    lnMTATable.setStatus("mandatory")
_LnMTAEntry_Object = MibTableRow
lnMTAEntry = _LnMTAEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12, 1, 1)
)
lnMTAEntry.setIndexNames(
    (0, "NOTES-MIB", "lnMTAIndex"),
)
if mibBuilder.loadTexts:
    lnMTAEntry.setStatus("mandatory")


class _LnMTAIndex_Type(Integer32):
    """Custom type lnMTAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnMTAIndex_Type.__name__ = "Integer32"
_LnMTAIndex_Object = MibTableColumn
lnMTAIndex = _LnMTAIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12, 1, 1, 1),
    _LnMTAIndex_Type()
)
lnMTAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMTAIndex.setStatus("mandatory")
_LnMTAName_Type = DisplayString
_LnMTAName_Object = MibTableColumn
lnMTAName = _LnMTAName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12, 1, 1, 2),
    _LnMTAName_Type()
)
lnMTAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMTAName.setStatus("mandatory")


class _LnMTADeadMsgs_Type(Integer32):
    """Custom type lnMTADeadMsgs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMTADeadMsgs_Type.__name__ = "Integer32"
_LnMTADeadMsgs_Object = MibTableColumn
lnMTADeadMsgs = _LnMTADeadMsgs_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12, 1, 1, 3),
    _LnMTADeadMsgs_Type()
)
lnMTADeadMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMTADeadMsgs.setStatus("optional")


class _LnMTAWaitingRecp_Type(Integer32):
    """Custom type lnMTAWaitingRecp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMTAWaitingRecp_Type.__name__ = "Integer32"
_LnMTAWaitingRecp_Object = MibTableColumn
lnMTAWaitingRecp = _LnMTAWaitingRecp_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12, 1, 1, 4),
    _LnMTAWaitingRecp_Type()
)
lnMTAWaitingRecp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMTAWaitingRecp.setStatus("optional")


class _LnMTAWaitingMsgs_Type(Integer32):
    """Custom type lnMTAWaitingMsgs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMTAWaitingMsgs_Type.__name__ = "Integer32"
_LnMTAWaitingMsgs_Object = MibTableColumn
lnMTAWaitingMsgs = _LnMTAWaitingMsgs_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12, 1, 1, 5),
    _LnMTAWaitingMsgs_Type()
)
lnMTAWaitingMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMTAWaitingMsgs.setStatus("optional")


class _LnMTATransferFailures_Type(Integer32):
    """Custom type lnMTATransferFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMTATransferFailures_Type.__name__ = "Integer32"
_LnMTATransferFailures_Object = MibTableColumn
lnMTATransferFailures = _LnMTATransferFailures_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12, 1, 1, 6),
    _LnMTATransferFailures_Type()
)
lnMTATransferFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMTATransferFailures.setStatus("optional")


class _LnMTATotalKBTransferred_Type(Integer32):
    """Custom type lnMTATotalKBTransferred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMTATotalKBTransferred_Type.__name__ = "Integer32"
_LnMTATotalKBTransferred_Object = MibTableColumn
lnMTATotalKBTransferred = _LnMTATotalKBTransferred_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12, 1, 1, 7),
    _LnMTATotalKBTransferred_Type()
)
lnMTATotalKBTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMTATotalKBTransferred.setStatus("optional")


class _LnMTATransferredMsgs_Type(Integer32):
    """Custom type lnMTATransferredMsgs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMTATransferredMsgs_Type.__name__ = "Integer32"
_LnMTATransferredMsgs_Object = MibTableColumn
lnMTATransferredMsgs = _LnMTATransferredMsgs_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12, 1, 1, 8),
    _LnMTATransferredMsgs_Type()
)
lnMTATransferredMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMTATransferredMsgs.setStatus("optional")


class _LnMTATotalRouted_Type(Integer32):
    """Custom type lnMTATotalRouted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnMTATotalRouted_Type.__name__ = "Integer32"
_LnMTATotalRouted_Object = MibTableColumn
lnMTATotalRouted = _LnMTATotalRouted_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 12, 1, 1, 9),
    _LnMTATotalRouted_Type()
)
lnMTATotalRouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMTATotalRouted.setStatus("optional")
_LnWeb_ObjectIdentity = ObjectIdentity
lnWeb = _LnWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13)
)


class _LnWebAccessFtp_Type(Integer32):
    """Custom type lnWebAccessFtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebAccessFtp_Type.__name__ = "Integer32"
_LnWebAccessFtp_Object = MibScalar
lnWebAccessFtp = _LnWebAccessFtp_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 1),
    _LnWebAccessFtp_Type()
)
lnWebAccessFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebAccessFtp.setStatus("optional")


class _LnWebAccessGopher_Type(Integer32):
    """Custom type lnWebAccessGopher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebAccessGopher_Type.__name__ = "Integer32"
_LnWebAccessGopher_Object = MibScalar
lnWebAccessGopher = _LnWebAccessGopher_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 2),
    _LnWebAccessGopher_Type()
)
lnWebAccessGopher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebAccessGopher.setStatus("optional")


class _LnWebAccessHttp_Type(Integer32):
    """Custom type lnWebAccessHttp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebAccessHttp_Type.__name__ = "Integer32"
_LnWebAccessHttp_Object = MibScalar
lnWebAccessHttp = _LnWebAccessHttp_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 3),
    _LnWebAccessHttp_Type()
)
lnWebAccessHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebAccessHttp.setStatus("optional")


class _LnWebKBytesReceived_Type(Integer32):
    """Custom type lnWebKBytesReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebKBytesReceived_Type.__name__ = "Integer32"
_LnWebKBytesReceived_Object = MibScalar
lnWebKBytesReceived = _LnWebKBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 4),
    _LnWebKBytesReceived_Type()
)
lnWebKBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebKBytesReceived.setStatus("optional")


class _LnWebKBytesSent_Type(Integer32):
    """Custom type lnWebKBytesSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebKBytesSent_Type.__name__ = "Integer32"
_LnWebKBytesSent_Object = MibScalar
lnWebKBytesSent = _LnWebKBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 5),
    _LnWebKBytesSent_Type()
)
lnWebKBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebKBytesSent.setStatus("optional")


class _LnWebImageCacheHits_Type(Integer32):
    """Custom type lnWebImageCacheHits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebImageCacheHits_Type.__name__ = "Integer32"
_LnWebImageCacheHits_Object = MibScalar
lnWebImageCacheHits = _LnWebImageCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 6),
    _LnWebImageCacheHits_Type()
)
lnWebImageCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebImageCacheHits.setStatus("optional")


class _LnWebImageCacheMisses_Type(Integer32):
    """Custom type lnWebImageCacheMisses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebImageCacheMisses_Type.__name__ = "Integer32"
_LnWebImageCacheMisses_Object = MibScalar
lnWebImageCacheMisses = _LnWebImageCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 7),
    _LnWebImageCacheMisses_Type()
)
lnWebImageCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebImageCacheMisses.setStatus("optional")
_LnWebLogMessages_Type = DisplayString
_LnWebLogMessages_Object = MibScalar
lnWebLogMessages = _LnWebLogMessages_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 8),
    _LnWebLogMessages_Type()
)
lnWebLogMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebLogMessages.setStatus("optional")


class _LnWebActiveProcesses_Type(Integer32):
    """Custom type lnWebActiveProcesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebActiveProcesses_Type.__name__ = "Integer32"
_LnWebActiveProcesses_Object = MibScalar
lnWebActiveProcesses = _LnWebActiveProcesses_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 9),
    _LnWebActiveProcesses_Type()
)
lnWebActiveProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebActiveProcesses.setStatus("optional")


class _LnWebBusyProcesses_Type(Integer32):
    """Custom type lnWebBusyProcesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebBusyProcesses_Type.__name__ = "Integer32"
_LnWebBusyProcesses_Object = MibScalar
lnWebBusyProcesses = _LnWebBusyProcesses_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 10),
    _LnWebBusyProcesses_Type()
)
lnWebBusyProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebBusyProcesses.setStatus("optional")


class _LnWebIdleProcesses_Type(Integer32):
    """Custom type lnWebIdleProcesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebIdleProcesses_Type.__name__ = "Integer32"
_LnWebIdleProcesses_Object = MibScalar
lnWebIdleProcesses = _LnWebIdleProcesses_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 11),
    _LnWebIdleProcesses_Type()
)
lnWebIdleProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebIdleProcesses.setStatus("optional")


class _LnWebMaxProcesses_Type(Integer32):
    """Custom type lnWebMaxProcesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebMaxProcesses_Type.__name__ = "Integer32"
_LnWebMaxProcesses_Object = MibScalar
lnWebMaxProcesses = _LnWebMaxProcesses_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 12),
    _LnWebMaxProcesses_Type()
)
lnWebMaxProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebMaxProcesses.setStatus("optional")
_LnWebProcessState_Type = DisplayString
_LnWebProcessState_Object = MibScalar
lnWebProcessState = _LnWebProcessState_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 13),
    _LnWebProcessState_Type()
)
lnWebProcessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcessState.setStatus("optional")
_LnWebTimeCurrent_Type = DisplayString
_LnWebTimeCurrent_Object = MibScalar
lnWebTimeCurrent = _LnWebTimeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 14),
    _LnWebTimeCurrent_Type()
)
lnWebTimeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebTimeCurrent.setStatus("optional")
_LnWebTimeDuration_Type = DisplayString
_LnWebTimeDuration_Object = MibScalar
lnWebTimeDuration = _LnWebTimeDuration_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 15),
    _LnWebTimeDuration_Type()
)
lnWebTimeDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebTimeDuration.setStatus("optional")
_LnWebTimeStart_Type = DisplayString
_LnWebTimeStart_Object = MibScalar
lnWebTimeStart = _LnWebTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 16),
    _LnWebTimeStart_Type()
)
lnWebTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebTimeStart.setStatus("optional")


class _LnWebUrlFail_Type(Integer32):
    """Custom type lnWebUrlFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebUrlFail_Type.__name__ = "Integer32"
_LnWebUrlFail_Object = MibScalar
lnWebUrlFail = _LnWebUrlFail_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 17),
    _LnWebUrlFail_Type()
)
lnWebUrlFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebUrlFail.setStatus("optional")


class _LnWebUrlRequested_Type(Integer32):
    """Custom type lnWebUrlRequested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebUrlRequested_Type.__name__ = "Integer32"
_LnWebUrlRequested_Object = MibScalar
lnWebUrlRequested = _LnWebUrlRequested_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 18),
    _LnWebUrlRequested_Type()
)
lnWebUrlRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebUrlRequested.setStatus("optional")


class _LnWebUrlSucceeded_Type(Integer32):
    """Custom type lnWebUrlSucceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebUrlSucceeded_Type.__name__ = "Integer32"
_LnWebUrlSucceeded_Object = MibScalar
lnWebUrlSucceeded = _LnWebUrlSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 19),
    _LnWebUrlSucceeded_Type()
)
lnWebUrlSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebUrlSucceeded.setStatus("optional")
_LnWebRetrieverVersion_Type = DisplayString
_LnWebRetrieverVersion_Object = MibScalar
lnWebRetrieverVersion = _LnWebRetrieverVersion_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 20),
    _LnWebRetrieverVersion_Type()
)
lnWebRetrieverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebRetrieverVersion.setStatus("optional")


class _LnWebVpoolMaxBuf_Type(Integer32):
    """Custom type lnWebVpoolMaxBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebVpoolMaxBuf_Type.__name__ = "Integer32"
_LnWebVpoolMaxBuf_Object = MibScalar
lnWebVpoolMaxBuf = _LnWebVpoolMaxBuf_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 21),
    _LnWebVpoolMaxBuf_Type()
)
lnWebVpoolMaxBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebVpoolMaxBuf.setStatus("optional")


class _LnWebVpoolMaxElement_Type(Integer32):
    """Custom type lnWebVpoolMaxElement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebVpoolMaxElement_Type.__name__ = "Integer32"
_LnWebVpoolMaxElement_Object = MibScalar
lnWebVpoolMaxElement = _LnWebVpoolMaxElement_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 22),
    _LnWebVpoolMaxElement_Type()
)
lnWebVpoolMaxElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebVpoolMaxElement.setStatus("optional")


class _LnWebVpoolMaxMarker_Type(Integer32):
    """Custom type lnWebVpoolMaxMarker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebVpoolMaxMarker_Type.__name__ = "Integer32"
_LnWebVpoolMaxMarker_Object = MibScalar
lnWebVpoolMaxMarker = _LnWebVpoolMaxMarker_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 23),
    _LnWebVpoolMaxMarker_Type()
)
lnWebVpoolMaxMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebVpoolMaxMarker.setStatus("optional")


class _LnWebVpoolMaxText_Type(Integer32):
    """Custom type lnWebVpoolMaxText based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebVpoolMaxText_Type.__name__ = "Integer32"
_LnWebVpoolMaxText_Object = MibScalar
lnWebVpoolMaxText = _LnWebVpoolMaxText_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 24),
    _LnWebVpoolMaxText_Type()
)
lnWebVpoolMaxText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebVpoolMaxText.setStatus("optional")


class _LnWebVpoolMaxUrl_Type(Integer32):
    """Custom type lnWebVpoolMaxUrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebVpoolMaxUrl_Type.__name__ = "Integer32"
_LnWebVpoolMaxUrl_Object = MibScalar
lnWebVpoolMaxUrl = _LnWebVpoolMaxUrl_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 25),
    _LnWebVpoolMaxUrl_Type()
)
lnWebVpoolMaxUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebVpoolMaxUrl.setStatus("optional")
_LnWebProcessTable_Object = MibTable
lnWebProcessTable = _LnWebProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26)
)
if mibBuilder.loadTexts:
    lnWebProcessTable.setStatus("optional")
_LnWebProcEntry_Object = MibTableRow
lnWebProcEntry = _LnWebProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1)
)
lnWebProcEntry.setIndexNames(
    (0, "NOTES-MIB", "lnWebProcIndex"),
)
if mibBuilder.loadTexts:
    lnWebProcEntry.setStatus("optional")


class _LnWebProcIndex_Type(Integer32):
    """Custom type lnWebProcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcIndex_Type.__name__ = "Integer32"
_LnWebProcIndex_Object = MibTableColumn
lnWebProcIndex = _LnWebProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 1),
    _LnWebProcIndex_Type()
)
lnWebProcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcIndex.setStatus("mandatory")
_LnWebProcNumber_Type = DisplayString
_LnWebProcNumber_Object = MibTableColumn
lnWebProcNumber = _LnWebProcNumber_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 2),
    _LnWebProcNumber_Type()
)
lnWebProcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcNumber.setStatus("mandatory")


class _LnWebProcAccFtp_Type(Integer32):
    """Custom type lnWebProcAccFtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcAccFtp_Type.__name__ = "Integer32"
_LnWebProcAccFtp_Object = MibTableColumn
lnWebProcAccFtp = _LnWebProcAccFtp_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 3),
    _LnWebProcAccFtp_Type()
)
lnWebProcAccFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcAccFtp.setStatus("mandatory")


class _LnWebProcAccGopher_Type(Integer32):
    """Custom type lnWebProcAccGopher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcAccGopher_Type.__name__ = "Integer32"
_LnWebProcAccGopher_Object = MibTableColumn
lnWebProcAccGopher = _LnWebProcAccGopher_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 4),
    _LnWebProcAccGopher_Type()
)
lnWebProcAccGopher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcAccGopher.setStatus("mandatory")


class _LnWebProcAccHttp_Type(Integer32):
    """Custom type lnWebProcAccHttp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcAccHttp_Type.__name__ = "Integer32"
_LnWebProcAccHttp_Object = MibTableColumn
lnWebProcAccHttp = _LnWebProcAccHttp_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 5),
    _LnWebProcAccHttp_Type()
)
lnWebProcAccHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcAccHttp.setStatus("mandatory")


class _LnWebProcKBytesRec_Type(Integer32):
    """Custom type lnWebProcKBytesRec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcKBytesRec_Type.__name__ = "Integer32"
_LnWebProcKBytesRec_Object = MibTableColumn
lnWebProcKBytesRec = _LnWebProcKBytesRec_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 6),
    _LnWebProcKBytesRec_Type()
)
lnWebProcKBytesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcKBytesRec.setStatus("mandatory")


class _LnWebProcKBytesSent_Type(Integer32):
    """Custom type lnWebProcKBytesSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcKBytesSent_Type.__name__ = "Integer32"
_LnWebProcKBytesSent_Object = MibTableColumn
lnWebProcKBytesSent = _LnWebProcKBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 7),
    _LnWebProcKBytesSent_Type()
)
lnWebProcKBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcKBytesSent.setStatus("mandatory")


class _LnWebProcCacheHits_Type(Integer32):
    """Custom type lnWebProcCacheHits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcCacheHits_Type.__name__ = "Integer32"
_LnWebProcCacheHits_Object = MibTableColumn
lnWebProcCacheHits = _LnWebProcCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 8),
    _LnWebProcCacheHits_Type()
)
lnWebProcCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcCacheHits.setStatus("mandatory")


class _LnWebProcCacheMisses_Type(Integer32):
    """Custom type lnWebProcCacheMisses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcCacheMisses_Type.__name__ = "Integer32"
_LnWebProcCacheMisses_Object = MibTableColumn
lnWebProcCacheMisses = _LnWebProcCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 9),
    _LnWebProcCacheMisses_Type()
)
lnWebProcCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcCacheMisses.setStatus("mandatory")


class _LnWebProcPid_Type(Integer32):
    """Custom type lnWebProcPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcPid_Type.__name__ = "Integer32"
_LnWebProcPid_Object = MibTableColumn
lnWebProcPid = _LnWebProcPid_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 10),
    _LnWebProcPid_Type()
)
lnWebProcPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcPid.setStatus("mandatory")


class _LnWebProcUrlFail_Type(Integer32):
    """Custom type lnWebProcUrlFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcUrlFail_Type.__name__ = "Integer32"
_LnWebProcUrlFail_Object = MibTableColumn
lnWebProcUrlFail = _LnWebProcUrlFail_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 11),
    _LnWebProcUrlFail_Type()
)
lnWebProcUrlFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcUrlFail.setStatus("mandatory")


class _LnWebProcUrlReq_Type(Integer32):
    """Custom type lnWebProcUrlReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcUrlReq_Type.__name__ = "Integer32"
_LnWebProcUrlReq_Object = MibTableColumn
lnWebProcUrlReq = _LnWebProcUrlReq_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 12),
    _LnWebProcUrlReq_Type()
)
lnWebProcUrlReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcUrlReq.setStatus("mandatory")


class _LnWebProcUrlSucc_Type(Integer32):
    """Custom type lnWebProcUrlSucc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcUrlSucc_Type.__name__ = "Integer32"
_LnWebProcUrlSucc_Object = MibTableColumn
lnWebProcUrlSucc = _LnWebProcUrlSucc_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 13),
    _LnWebProcUrlSucc_Type()
)
lnWebProcUrlSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcUrlSucc.setStatus("mandatory")


class _LnWebProcVpoolCurBuf_Type(Integer32):
    """Custom type lnWebProcVpoolCurBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcVpoolCurBuf_Type.__name__ = "Integer32"
_LnWebProcVpoolCurBuf_Object = MibTableColumn
lnWebProcVpoolCurBuf = _LnWebProcVpoolCurBuf_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 14),
    _LnWebProcVpoolCurBuf_Type()
)
lnWebProcVpoolCurBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcVpoolCurBuf.setStatus("mandatory")


class _LnWebProcVpoolCurElement_Type(Integer32):
    """Custom type lnWebProcVpoolCurElement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcVpoolCurElement_Type.__name__ = "Integer32"
_LnWebProcVpoolCurElement_Object = MibTableColumn
lnWebProcVpoolCurElement = _LnWebProcVpoolCurElement_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 15),
    _LnWebProcVpoolCurElement_Type()
)
lnWebProcVpoolCurElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcVpoolCurElement.setStatus("mandatory")


class _LnWebProcVpoolCurMarker_Type(Integer32):
    """Custom type lnWebProcVpoolCurMarker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcVpoolCurMarker_Type.__name__ = "Integer32"
_LnWebProcVpoolCurMarker_Object = MibTableColumn
lnWebProcVpoolCurMarker = _LnWebProcVpoolCurMarker_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 16),
    _LnWebProcVpoolCurMarker_Type()
)
lnWebProcVpoolCurMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcVpoolCurMarker.setStatus("mandatory")


class _LnWebProcVpoolCurText_Type(Integer32):
    """Custom type lnWebProcVpoolCurText based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcVpoolCurText_Type.__name__ = "Integer32"
_LnWebProcVpoolCurText_Object = MibTableColumn
lnWebProcVpoolCurText = _LnWebProcVpoolCurText_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 17),
    _LnWebProcVpoolCurText_Type()
)
lnWebProcVpoolCurText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcVpoolCurText.setStatus("mandatory")


class _LnWebProcVpoolCurUrl_Type(Integer32):
    """Custom type lnWebProcVpoolCurUrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcVpoolCurUrl_Type.__name__ = "Integer32"
_LnWebProcVpoolCurUrl_Object = MibTableColumn
lnWebProcVpoolCurUrl = _LnWebProcVpoolCurUrl_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 18),
    _LnWebProcVpoolCurUrl_Type()
)
lnWebProcVpoolCurUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcVpoolCurUrl.setStatus("mandatory")


class _LnWebProcVpoolMaxBuf_Type(Integer32):
    """Custom type lnWebProcVpoolMaxBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcVpoolMaxBuf_Type.__name__ = "Integer32"
_LnWebProcVpoolMaxBuf_Object = MibTableColumn
lnWebProcVpoolMaxBuf = _LnWebProcVpoolMaxBuf_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 19),
    _LnWebProcVpoolMaxBuf_Type()
)
lnWebProcVpoolMaxBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcVpoolMaxBuf.setStatus("mandatory")


class _LnWebProcVpoolMaxElement_Type(Integer32):
    """Custom type lnWebProcVpoolMaxElement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcVpoolMaxElement_Type.__name__ = "Integer32"
_LnWebProcVpoolMaxElement_Object = MibTableColumn
lnWebProcVpoolMaxElement = _LnWebProcVpoolMaxElement_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 20),
    _LnWebProcVpoolMaxElement_Type()
)
lnWebProcVpoolMaxElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcVpoolMaxElement.setStatus("mandatory")


class _LnWebProcVpoolMaxMarker_Type(Integer32):
    """Custom type lnWebProcVpoolMaxMarker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcVpoolMaxMarker_Type.__name__ = "Integer32"
_LnWebProcVpoolMaxMarker_Object = MibTableColumn
lnWebProcVpoolMaxMarker = _LnWebProcVpoolMaxMarker_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 21),
    _LnWebProcVpoolMaxMarker_Type()
)
lnWebProcVpoolMaxMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcVpoolMaxMarker.setStatus("mandatory")


class _LnWebProcVpoolMaxText_Type(Integer32):
    """Custom type lnWebProcVpoolMaxText based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcVpoolMaxText_Type.__name__ = "Integer32"
_LnWebProcVpoolMaxText_Object = MibTableColumn
lnWebProcVpoolMaxText = _LnWebProcVpoolMaxText_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 22),
    _LnWebProcVpoolMaxText_Type()
)
lnWebProcVpoolMaxText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcVpoolMaxText.setStatus("mandatory")


class _LnWebProcVpoolMaxUrl_Type(Integer32):
    """Custom type lnWebProcVpoolMaxUrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496795),
    )


_LnWebProcVpoolMaxUrl_Type.__name__ = "Integer32"
_LnWebProcVpoolMaxUrl_Object = MibTableColumn
lnWebProcVpoolMaxUrl = _LnWebProcVpoolMaxUrl_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 13, 26, 1, 23),
    _LnWebProcVpoolMaxUrl_Type()
)
lnWebProcVpoolMaxUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnWebProcVpoolMaxUrl.setStatus("mandatory")
_LnObject_ObjectIdentity = ObjectIdentity
lnObject = _LnObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14)
)
_LnObjectFileName_Type = DisplayString
_LnObjectFileName_Object = MibScalar
lnObjectFileName = _LnObjectFileName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 1),
    _LnObjectFileName_Type()
)
lnObjectFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectFileName.setStatus("optional")
_LnObjectTable_Object = MibTable
lnObjectTable = _LnObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    lnObjectTable.setStatus("optional")
_LnObjectEntry_Object = MibTableRow
lnObjectEntry = _LnObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1)
)
if mibBuilder.loadTexts:
    lnObjectEntry.setStatus("mandatory")


class _LnObjectIndex_Type(Integer32):
    """Custom type lnObjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectIndex_Type.__name__ = "Integer32"
_LnObjectIndex_Object = MibTableColumn
lnObjectIndex = _LnObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 1),
    _LnObjectIndex_Type()
)
lnObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectIndex.setStatus("optional")
_LnObjectName_Type = DisplayString
_LnObjectName_Object = MibTableColumn
lnObjectName = _LnObjectName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 2),
    _LnObjectName_Type()
)
lnObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectName.setStatus("optional")


class _LnObjectSharedBy01_Type(Integer32):
    """Custom type lnObjectSharedBy01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy01_Type.__name__ = "Integer32"
_LnObjectSharedBy01_Object = MibTableColumn
lnObjectSharedBy01 = _LnObjectSharedBy01_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 3),
    _LnObjectSharedBy01_Type()
)
lnObjectSharedBy01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy01.setStatus("optional")


class _LnObjectSharedBy02_Type(Integer32):
    """Custom type lnObjectSharedBy02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy02_Type.__name__ = "Integer32"
_LnObjectSharedBy02_Object = MibTableColumn
lnObjectSharedBy02 = _LnObjectSharedBy02_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 4),
    _LnObjectSharedBy02_Type()
)
lnObjectSharedBy02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy02.setStatus("optional")


class _LnObjectSharedBy03_Type(Integer32):
    """Custom type lnObjectSharedBy03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy03_Type.__name__ = "Integer32"
_LnObjectSharedBy03_Object = MibTableColumn
lnObjectSharedBy03 = _LnObjectSharedBy03_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 5),
    _LnObjectSharedBy03_Type()
)
lnObjectSharedBy03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy03.setStatus("optional")


class _LnObjectSharedBy04_Type(Integer32):
    """Custom type lnObjectSharedBy04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy04_Type.__name__ = "Integer32"
_LnObjectSharedBy04_Object = MibTableColumn
lnObjectSharedBy04 = _LnObjectSharedBy04_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 6),
    _LnObjectSharedBy04_Type()
)
lnObjectSharedBy04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy04.setStatus("optional")


class _LnObjectSharedBy05_Type(Integer32):
    """Custom type lnObjectSharedBy05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy05_Type.__name__ = "Integer32"
_LnObjectSharedBy05_Object = MibTableColumn
lnObjectSharedBy05 = _LnObjectSharedBy05_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 7),
    _LnObjectSharedBy05_Type()
)
lnObjectSharedBy05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy05.setStatus("optional")


class _LnObjectSharedBy06_Type(Integer32):
    """Custom type lnObjectSharedBy06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy06_Type.__name__ = "Integer32"
_LnObjectSharedBy06_Object = MibTableColumn
lnObjectSharedBy06 = _LnObjectSharedBy06_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 8),
    _LnObjectSharedBy06_Type()
)
lnObjectSharedBy06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy06.setStatus("optional")


class _LnObjectSharedBy07_Type(Integer32):
    """Custom type lnObjectSharedBy07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy07_Type.__name__ = "Integer32"
_LnObjectSharedBy07_Object = MibTableColumn
lnObjectSharedBy07 = _LnObjectSharedBy07_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 9),
    _LnObjectSharedBy07_Type()
)
lnObjectSharedBy07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy07.setStatus("optional")


class _LnObjectSharedBy08_Type(Integer32):
    """Custom type lnObjectSharedBy08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy08_Type.__name__ = "Integer32"
_LnObjectSharedBy08_Object = MibTableColumn
lnObjectSharedBy08 = _LnObjectSharedBy08_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 10),
    _LnObjectSharedBy08_Type()
)
lnObjectSharedBy08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy08.setStatus("optional")


class _LnObjectSharedBy09_Type(Integer32):
    """Custom type lnObjectSharedBy09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy09_Type.__name__ = "Integer32"
_LnObjectSharedBy09_Object = MibTableColumn
lnObjectSharedBy09 = _LnObjectSharedBy09_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 11),
    _LnObjectSharedBy09_Type()
)
lnObjectSharedBy09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy09.setStatus("optional")


class _LnObjectSharedBy10_Type(Integer32):
    """Custom type lnObjectSharedBy10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy10_Type.__name__ = "Integer32"
_LnObjectSharedBy10_Object = MibTableColumn
lnObjectSharedBy10 = _LnObjectSharedBy10_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 12),
    _LnObjectSharedBy10_Type()
)
lnObjectSharedBy10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy10.setStatus("optional")


class _LnObjectSharedBy11_Type(Integer32):
    """Custom type lnObjectSharedBy11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy11_Type.__name__ = "Integer32"
_LnObjectSharedBy11_Object = MibTableColumn
lnObjectSharedBy11 = _LnObjectSharedBy11_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 13),
    _LnObjectSharedBy11_Type()
)
lnObjectSharedBy11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy11.setStatus("optional")


class _LnObjectSharedBy12_Type(Integer32):
    """Custom type lnObjectSharedBy12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy12_Type.__name__ = "Integer32"
_LnObjectSharedBy12_Object = MibTableColumn
lnObjectSharedBy12 = _LnObjectSharedBy12_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 14),
    _LnObjectSharedBy12_Type()
)
lnObjectSharedBy12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy12.setStatus("optional")


class _LnObjectSharedBy13_Type(Integer32):
    """Custom type lnObjectSharedBy13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy13_Type.__name__ = "Integer32"
_LnObjectSharedBy13_Object = MibTableColumn
lnObjectSharedBy13 = _LnObjectSharedBy13_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 15),
    _LnObjectSharedBy13_Type()
)
lnObjectSharedBy13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy13.setStatus("optional")


class _LnObjectSharedBy14_Type(Integer32):
    """Custom type lnObjectSharedBy14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy14_Type.__name__ = "Integer32"
_LnObjectSharedBy14_Object = MibTableColumn
lnObjectSharedBy14 = _LnObjectSharedBy14_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 16),
    _LnObjectSharedBy14_Type()
)
lnObjectSharedBy14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy14.setStatus("optional")


class _LnObjectSharedBy15_Type(Integer32):
    """Custom type lnObjectSharedBy15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy15_Type.__name__ = "Integer32"
_LnObjectSharedBy15_Object = MibTableColumn
lnObjectSharedBy15 = _LnObjectSharedBy15_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 17),
    _LnObjectSharedBy15_Type()
)
lnObjectSharedBy15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy15.setStatus("optional")


class _LnObjectSharedBy16_Type(Integer32):
    """Custom type lnObjectSharedBy16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy16_Type.__name__ = "Integer32"
_LnObjectSharedBy16_Object = MibTableColumn
lnObjectSharedBy16 = _LnObjectSharedBy16_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 18),
    _LnObjectSharedBy16_Type()
)
lnObjectSharedBy16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy16.setStatus("optional")


class _LnObjectSharedBy17_Type(Integer32):
    """Custom type lnObjectSharedBy17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy17_Type.__name__ = "Integer32"
_LnObjectSharedBy17_Object = MibTableColumn
lnObjectSharedBy17 = _LnObjectSharedBy17_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 19),
    _LnObjectSharedBy17_Type()
)
lnObjectSharedBy17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy17.setStatus("optional")


class _LnObjectSharedBy18_Type(Integer32):
    """Custom type lnObjectSharedBy18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy18_Type.__name__ = "Integer32"
_LnObjectSharedBy18_Object = MibTableColumn
lnObjectSharedBy18 = _LnObjectSharedBy18_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 20),
    _LnObjectSharedBy18_Type()
)
lnObjectSharedBy18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy18.setStatus("optional")


class _LnObjectSharedBy19_Type(Integer32):
    """Custom type lnObjectSharedBy19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy19_Type.__name__ = "Integer32"
_LnObjectSharedBy19_Object = MibTableColumn
lnObjectSharedBy19 = _LnObjectSharedBy19_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 21),
    _LnObjectSharedBy19_Type()
)
lnObjectSharedBy19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy19.setStatus("optional")


class _LnObjectSharedBy20_Type(Integer32):
    """Custom type lnObjectSharedBy20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedBy20_Type.__name__ = "Integer32"
_LnObjectSharedBy20_Object = MibTableColumn
lnObjectSharedBy20 = _LnObjectSharedBy20_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 22),
    _LnObjectSharedBy20_Type()
)
lnObjectSharedBy20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedBy20.setStatus("optional")


class _LnObjectSharedByGreater_Type(Integer32):
    """Custom type lnObjectSharedByGreater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedByGreater_Type.__name__ = "Integer32"
_LnObjectSharedByGreater_Object = MibTableColumn
lnObjectSharedByGreater = _LnObjectSharedByGreater_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 23),
    _LnObjectSharedByGreater_Type()
)
lnObjectSharedByGreater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedByGreater.setStatus("optional")


class _LnObjectSharedByTotal_Type(Integer32):
    """Custom type lnObjectSharedByTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnObjectSharedByTotal_Type.__name__ = "Integer32"
_LnObjectSharedByTotal_Object = MibTableColumn
lnObjectSharedByTotal = _LnObjectSharedByTotal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 14, 2, 1, 24),
    _LnObjectSharedByTotal_Type()
)
lnObjectSharedByTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnObjectSharedByTotal.setStatus("optional")
_LnDomino_ObjectIdentity = ObjectIdentity
lnDomino = _LnDomino_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15)
)
_LnDominoInfo_ObjectIdentity = ObjectIdentity
lnDominoInfo = _LnDominoInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1)
)
_LnDominoBuildName_Type = DisplayString
_LnDominoBuildName_Object = MibScalar
lnDominoBuildName = _LnDominoBuildName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 1),
    _LnDominoBuildName_Type()
)
lnDominoBuildName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoBuildName.setStatus("optional")
_LnDominoBuildNumber_Type = DisplayString
_LnDominoBuildNumber_Object = MibScalar
lnDominoBuildNumber = _LnDominoBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 2),
    _LnDominoBuildNumber_Type()
)
lnDominoBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoBuildNumber.setStatus("optional")
_LnDominoBuildPlatform_Type = DisplayString
_LnDominoBuildPlatform_Object = MibScalar
lnDominoBuildPlatform = _LnDominoBuildPlatform_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 3),
    _LnDominoBuildPlatform_Type()
)
lnDominoBuildPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoBuildPlatform.setStatus("optional")
_LnDominoBuildVersion_Type = DisplayString
_LnDominoBuildVersion_Object = MibScalar
lnDominoBuildVersion = _LnDominoBuildVersion_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 4),
    _LnDominoBuildVersion_Type()
)
lnDominoBuildVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoBuildVersion.setStatus("optional")


class _LnDominoThreadsActivePeak_Type(Integer32):
    """Custom type lnDominoThreadsActivePeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoThreadsActivePeak_Type.__name__ = "Integer32"
_LnDominoThreadsActivePeak_Object = MibScalar
lnDominoThreadsActivePeak = _LnDominoThreadsActivePeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 5),
    _LnDominoThreadsActivePeak_Type()
)
lnDominoThreadsActivePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoThreadsActivePeak.setStatus("optional")


class _LnDominoThreadsTotal_Type(Integer32):
    """Custom type lnDominoThreadsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoThreadsTotal_Type.__name__ = "Integer32"
_LnDominoThreadsTotal_Object = MibScalar
lnDominoThreadsTotal = _LnDominoThreadsTotal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 6),
    _LnDominoThreadsTotal_Type()
)
lnDominoThreadsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoThreadsTotal.setStatus("optional")


class _LnDominoThreadsPeakTotal_Type(Integer32):
    """Custom type lnDominoThreadsPeakTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoThreadsPeakTotal_Type.__name__ = "Integer32"
_LnDominoThreadsPeakTotal_Object = MibScalar
lnDominoThreadsPeakTotal = _LnDominoThreadsPeakTotal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 7),
    _LnDominoThreadsPeakTotal_Type()
)
lnDominoThreadsPeakTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoThreadsPeakTotal.setStatus("optional")


class _LnDominoThreadsPeakTime_Type(Integer32):
    """Custom type lnDominoThreadsPeakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoThreadsPeakTime_Type.__name__ = "Integer32"
_LnDominoThreadsPeakTime_Object = MibScalar
lnDominoThreadsPeakTime = _LnDominoThreadsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 8),
    _LnDominoThreadsPeakTime_Type()
)
lnDominoThreadsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoThreadsPeakTime.setStatus("optional")


class _LnDominoStartTime_Type(Integer32):
    """Custom type lnDominoStartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoStartTime_Type.__name__ = "Integer32"
_LnDominoStartTime_Object = MibScalar
lnDominoStartTime = _LnDominoStartTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 9),
    _LnDominoStartTime_Type()
)
lnDominoStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoStartTime.setStatus("optional")


class _LnDominoReqPerMinTotal_Type(Integer32):
    """Custom type lnDominoReqPerMinTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPerMinTotal_Type.__name__ = "Integer32"
_LnDominoReqPerMinTotal_Object = MibScalar
lnDominoReqPerMinTotal = _LnDominoReqPerMinTotal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 10),
    _LnDominoReqPerMinTotal_Type()
)
lnDominoReqPerMinTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPerMinTotal.setStatus("optional")


class _LnDominoReqPerMinPeak_Type(Integer32):
    """Custom type lnDominoReqPerMinPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPerMinPeak_Type.__name__ = "Integer32"
_LnDominoReqPerMinPeak_Object = MibScalar
lnDominoReqPerMinPeak = _LnDominoReqPerMinPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 11),
    _LnDominoReqPerMinPeak_Type()
)
lnDominoReqPerMinPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPerMinPeak.setStatus("optional")


class _LnDominoReqPerMinPeakTime_Type(Integer32):
    """Custom type lnDominoReqPerMinPeakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPerMinPeakTime_Type.__name__ = "Integer32"
_LnDominoReqPerMinPeakTime_Object = MibScalar
lnDominoReqPerMinPeakTime = _LnDominoReqPerMinPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 12),
    _LnDominoReqPerMinPeakTime_Type()
)
lnDominoReqPerMinPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPerMinPeakTime.setStatus("optional")


class _LnDominoReqPer5MinsTotal_Type(Integer32):
    """Custom type lnDominoReqPer5MinsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPer5MinsTotal_Type.__name__ = "Integer32"
_LnDominoReqPer5MinsTotal_Object = MibScalar
lnDominoReqPer5MinsTotal = _LnDominoReqPer5MinsTotal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 13),
    _LnDominoReqPer5MinsTotal_Type()
)
lnDominoReqPer5MinsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPer5MinsTotal.setStatus("optional")


class _LnDominoReqPer5MinsPeak_Type(Integer32):
    """Custom type lnDominoReqPer5MinsPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPer5MinsPeak_Type.__name__ = "Integer32"
_LnDominoReqPer5MinsPeak_Object = MibScalar
lnDominoReqPer5MinsPeak = _LnDominoReqPer5MinsPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 14),
    _LnDominoReqPer5MinsPeak_Type()
)
lnDominoReqPer5MinsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPer5MinsPeak.setStatus("optional")


class _LnDominoReqPer5MinsPeakTime_Type(Integer32):
    """Custom type lnDominoReqPer5MinsPeakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPer5MinsPeakTime_Type.__name__ = "Integer32"
_LnDominoReqPer5MinsPeakTime_Object = MibScalar
lnDominoReqPer5MinsPeakTime = _LnDominoReqPer5MinsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 15),
    _LnDominoReqPer5MinsPeakTime_Type()
)
lnDominoReqPer5MinsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPer5MinsPeakTime.setStatus("optional")


class _LnDominoReqPerHourTotal_Type(Integer32):
    """Custom type lnDominoReqPerHourTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPerHourTotal_Type.__name__ = "Integer32"
_LnDominoReqPerHourTotal_Object = MibScalar
lnDominoReqPerHourTotal = _LnDominoReqPerHourTotal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 16),
    _LnDominoReqPerHourTotal_Type()
)
lnDominoReqPerHourTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPerHourTotal.setStatus("optional")


class _LnDominoReqPerHourPeak_Type(Integer32):
    """Custom type lnDominoReqPerHourPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPerHourPeak_Type.__name__ = "Integer32"
_LnDominoReqPerHourPeak_Object = MibScalar
lnDominoReqPerHourPeak = _LnDominoReqPerHourPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 17),
    _LnDominoReqPerHourPeak_Type()
)
lnDominoReqPerHourPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPerHourPeak.setStatus("optional")


class _LnDominoReqPerHourPeakTime_Type(Integer32):
    """Custom type lnDominoReqPerHourPeakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPerHourPeakTime_Type.__name__ = "Integer32"
_LnDominoReqPerHourPeakTime_Object = MibScalar
lnDominoReqPerHourPeakTime = _LnDominoReqPerHourPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 18),
    _LnDominoReqPerHourPeakTime_Type()
)
lnDominoReqPerHourPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPerHourPeakTime.setStatus("optional")


class _LnDominoReqPerDayTotal_Type(Integer32):
    """Custom type lnDominoReqPerDayTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPerDayTotal_Type.__name__ = "Integer32"
_LnDominoReqPerDayTotal_Object = MibScalar
lnDominoReqPerDayTotal = _LnDominoReqPerDayTotal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 19),
    _LnDominoReqPerDayTotal_Type()
)
lnDominoReqPerDayTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPerDayTotal.setStatus("optional")


class _LnDominoReqPerDayPeak_Type(Integer32):
    """Custom type lnDominoReqPerDayPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPerDayPeak_Type.__name__ = "Integer32"
_LnDominoReqPerDayPeak_Object = MibScalar
lnDominoReqPerDayPeak = _LnDominoReqPerDayPeak_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 20),
    _LnDominoReqPerDayPeak_Type()
)
lnDominoReqPerDayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPerDayPeak.setStatus("optional")


class _LnDominoReqPerDayPeakTime_Type(Integer32):
    """Custom type lnDominoReqPerDayPeakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoReqPerDayPeakTime_Type.__name__ = "Integer32"
_LnDominoReqPerDayPeakTime_Object = MibScalar
lnDominoReqPerDayPeakTime = _LnDominoReqPerDayPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 21),
    _LnDominoReqPerDayPeakTime_Type()
)
lnDominoReqPerDayPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoReqPerDayPeakTime.setStatus("optional")


class _LnDominoRequestsTotal_Type(Integer32):
    """Custom type lnDominoRequestsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoRequestsTotal_Type.__name__ = "Integer32"
_LnDominoRequestsTotal_Object = MibScalar
lnDominoRequestsTotal = _LnDominoRequestsTotal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 22),
    _LnDominoRequestsTotal_Type()
)
lnDominoRequestsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoRequestsTotal.setStatus("optional")


class _LnDominoCacheCommandDisplaceRate_Type(Integer32):
    """Custom type lnDominoCacheCommandDisplaceRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCacheCommandDisplaceRate_Type.__name__ = "Integer32"
_LnDominoCacheCommandDisplaceRate_Object = MibScalar
lnDominoCacheCommandDisplaceRate = _LnDominoCacheCommandDisplaceRate_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 23),
    _LnDominoCacheCommandDisplaceRate_Type()
)
lnDominoCacheCommandDisplaceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCacheCommandDisplaceRate.setStatus("optional")


class _LnDominoCacheCommandHitRate_Type(Integer32):
    """Custom type lnDominoCacheCommandHitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCacheCommandHitRate_Type.__name__ = "Integer32"
_LnDominoCacheCommandHitRate_Object = MibScalar
lnDominoCacheCommandHitRate = _LnDominoCacheCommandHitRate_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 24),
    _LnDominoCacheCommandHitRate_Type()
)
lnDominoCacheCommandHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCacheCommandHitRate.setStatus("optional")


class _LnDominoCacheDatabaseDisplaceRate_Type(Integer32):
    """Custom type lnDominoCacheDatabaseDisplaceRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCacheDatabaseDisplaceRate_Type.__name__ = "Integer32"
_LnDominoCacheDatabaseDisplaceRate_Object = MibScalar
lnDominoCacheDatabaseDisplaceRate = _LnDominoCacheDatabaseDisplaceRate_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 25),
    _LnDominoCacheDatabaseDisplaceRate_Type()
)
lnDominoCacheDatabaseDisplaceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCacheDatabaseDisplaceRate.setStatus("optional")


class _LnDominoCacheDatabaseHitRate_Type(Integer32):
    """Custom type lnDominoCacheDatabaseHitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCacheDatabaseHitRate_Type.__name__ = "Integer32"
_LnDominoCacheDatabaseHitRate_Object = MibScalar
lnDominoCacheDatabaseHitRate = _LnDominoCacheDatabaseHitRate_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 1, 26),
    _LnDominoCacheDatabaseHitRate_Type()
)
lnDominoCacheDatabaseHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCacheDatabaseHitRate.setStatus("optional")
_LnDominoCmdInfo_ObjectIdentity = ObjectIdentity
lnDominoCmdInfo = _LnDominoCmdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2)
)


class _LnDominoCmdInfoEditDocument_Type(Integer32):
    """Custom type lnDominoCmdInfoEditDocument based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoEditDocument_Type.__name__ = "Integer32"
_LnDominoCmdInfoEditDocument_Object = MibScalar
lnDominoCmdInfoEditDocument = _LnDominoCmdInfoEditDocument_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 1),
    _LnDominoCmdInfoEditDocument_Type()
)
lnDominoCmdInfoEditDocument.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoEditDocument.setStatus("optional")


class _LnDominoCmdInfoOpenServer_Type(Integer32):
    """Custom type lnDominoCmdInfoOpenServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoOpenServer_Type.__name__ = "Integer32"
_LnDominoCmdInfoOpenServer_Object = MibScalar
lnDominoCmdInfoOpenServer = _LnDominoCmdInfoOpenServer_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 2),
    _LnDominoCmdInfoOpenServer_Type()
)
lnDominoCmdInfoOpenServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoOpenServer.setStatus("optional")


class _LnDominoCmdInfoOpenDatabase_Type(Integer32):
    """Custom type lnDominoCmdInfoOpenDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoOpenDatabase_Type.__name__ = "Integer32"
_LnDominoCmdInfoOpenDatabase_Object = MibScalar
lnDominoCmdInfoOpenDatabase = _LnDominoCmdInfoOpenDatabase_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 3),
    _LnDominoCmdInfoOpenDatabase_Type()
)
lnDominoCmdInfoOpenDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoOpenDatabase.setStatus("optional")


class _LnDominoCmdInfoOpenView_Type(Integer32):
    """Custom type lnDominoCmdInfoOpenView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoOpenView_Type.__name__ = "Integer32"
_LnDominoCmdInfoOpenView_Object = MibScalar
lnDominoCmdInfoOpenView = _LnDominoCmdInfoOpenView_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 4),
    _LnDominoCmdInfoOpenView_Type()
)
lnDominoCmdInfoOpenView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoOpenView.setStatus("optional")


class _LnDominoCmdInfoOpenDocument_Type(Integer32):
    """Custom type lnDominoCmdInfoOpenDocument based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoOpenDocument_Type.__name__ = "Integer32"
_LnDominoCmdInfoOpenDocument_Object = MibScalar
lnDominoCmdInfoOpenDocument = _LnDominoCmdInfoOpenDocument_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 5),
    _LnDominoCmdInfoOpenDocument_Type()
)
lnDominoCmdInfoOpenDocument.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoOpenDocument.setStatus("optional")


class _LnDominoCmdInfoOpenElement_Type(Integer32):
    """Custom type lnDominoCmdInfoOpenElement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoOpenElement_Type.__name__ = "Integer32"
_LnDominoCmdInfoOpenElement_Object = MibScalar
lnDominoCmdInfoOpenElement = _LnDominoCmdInfoOpenElement_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 6),
    _LnDominoCmdInfoOpenElement_Type()
)
lnDominoCmdInfoOpenElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoOpenElement.setStatus("optional")


class _LnDominoCmdInfoOpenIcon_Type(Integer32):
    """Custom type lnDominoCmdInfoOpenIcon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoOpenIcon_Type.__name__ = "Integer32"
_LnDominoCmdInfoOpenIcon_Object = MibScalar
lnDominoCmdInfoOpenIcon = _LnDominoCmdInfoOpenIcon_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 7),
    _LnDominoCmdInfoOpenIcon_Type()
)
lnDominoCmdInfoOpenIcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoOpenIcon.setStatus("optional")


class _LnDominoCmdInfoOpenForm_Type(Integer32):
    """Custom type lnDominoCmdInfoOpenForm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoOpenForm_Type.__name__ = "Integer32"
_LnDominoCmdInfoOpenForm_Object = MibScalar
lnDominoCmdInfoOpenForm = _LnDominoCmdInfoOpenForm_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 8),
    _LnDominoCmdInfoOpenForm_Type()
)
lnDominoCmdInfoOpenForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoOpenForm.setStatus("optional")


class _LnDominoCmdInfoOpenAgent_Type(Integer32):
    """Custom type lnDominoCmdInfoOpenAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoOpenAgent_Type.__name__ = "Integer32"
_LnDominoCmdInfoOpenAgent_Object = MibScalar
lnDominoCmdInfoOpenAgent = _LnDominoCmdInfoOpenAgent_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 9),
    _LnDominoCmdInfoOpenAgent_Type()
)
lnDominoCmdInfoOpenAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoOpenAgent.setStatus("optional")


class _LnDominoCmdInfoOpenNavigator_Type(Integer32):
    """Custom type lnDominoCmdInfoOpenNavigator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoOpenNavigator_Type.__name__ = "Integer32"
_LnDominoCmdInfoOpenNavigator_Object = MibScalar
lnDominoCmdInfoOpenNavigator = _LnDominoCmdInfoOpenNavigator_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 10),
    _LnDominoCmdInfoOpenNavigator_Type()
)
lnDominoCmdInfoOpenNavigator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoOpenNavigator.setStatus("optional")


class _LnDominoCmdInfoOpenAbout_Type(Integer32):
    """Custom type lnDominoCmdInfoOpenAbout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoOpenAbout_Type.__name__ = "Integer32"
_LnDominoCmdInfoOpenAbout_Object = MibScalar
lnDominoCmdInfoOpenAbout = _LnDominoCmdInfoOpenAbout_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 11),
    _LnDominoCmdInfoOpenAbout_Type()
)
lnDominoCmdInfoOpenAbout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoOpenAbout.setStatus("optional")


class _LnDominoCmdInfoOpenHelp_Type(Integer32):
    """Custom type lnDominoCmdInfoOpenHelp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoOpenHelp_Type.__name__ = "Integer32"
_LnDominoCmdInfoOpenHelp_Object = MibScalar
lnDominoCmdInfoOpenHelp = _LnDominoCmdInfoOpenHelp_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 12),
    _LnDominoCmdInfoOpenHelp_Type()
)
lnDominoCmdInfoOpenHelp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoOpenHelp.setStatus("optional")


class _LnDominoCmdInfoCreateDocument_Type(Integer32):
    """Custom type lnDominoCmdInfoCreateDocument based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoCreateDocument_Type.__name__ = "Integer32"
_LnDominoCmdInfoCreateDocument_Object = MibScalar
lnDominoCmdInfoCreateDocument = _LnDominoCmdInfoCreateDocument_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 13),
    _LnDominoCmdInfoCreateDocument_Type()
)
lnDominoCmdInfoCreateDocument.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoCreateDocument.setStatus("optional")


class _LnDominoCmdInfoSaveDocument_Type(Integer32):
    """Custom type lnDominoCmdInfoSaveDocument based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoSaveDocument_Type.__name__ = "Integer32"
_LnDominoCmdInfoSaveDocument_Object = MibScalar
lnDominoCmdInfoSaveDocument = _LnDominoCmdInfoSaveDocument_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 14),
    _LnDominoCmdInfoSaveDocument_Type()
)
lnDominoCmdInfoSaveDocument.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoSaveDocument.setStatus("optional")


class _LnDominoCmdInfoDeleteDocument_Type(Integer32):
    """Custom type lnDominoCmdInfoDeleteDocument based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoDeleteDocument_Type.__name__ = "Integer32"
_LnDominoCmdInfoDeleteDocument_Object = MibScalar
lnDominoCmdInfoDeleteDocument = _LnDominoCmdInfoDeleteDocument_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 15),
    _LnDominoCmdInfoDeleteDocument_Type()
)
lnDominoCmdInfoDeleteDocument.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoDeleteDocument.setStatus("optional")


class _LnDominoCmdInfoSearchSite_Type(Integer32):
    """Custom type lnDominoCmdInfoSearchSite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoSearchSite_Type.__name__ = "Integer32"
_LnDominoCmdInfoSearchSite_Object = MibScalar
lnDominoCmdInfoSearchSite = _LnDominoCmdInfoSearchSite_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 16),
    _LnDominoCmdInfoSearchSite_Type()
)
lnDominoCmdInfoSearchSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoSearchSite.setStatus("optional")


class _LnDominoCmdInfoSearchView_Type(Integer32):
    """Custom type lnDominoCmdInfoSearchView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoSearchView_Type.__name__ = "Integer32"
_LnDominoCmdInfoSearchView_Object = MibScalar
lnDominoCmdInfoSearchView = _LnDominoCmdInfoSearchView_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 17),
    _LnDominoCmdInfoSearchView_Type()
)
lnDominoCmdInfoSearchView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoSearchView.setStatus("optional")


class _LnDominoCmdInfoUnknown_Type(Integer32):
    """Custom type lnDominoCmdInfoUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoUnknown_Type.__name__ = "Integer32"
_LnDominoCmdInfoUnknown_Object = MibScalar
lnDominoCmdInfoUnknown = _LnDominoCmdInfoUnknown_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 18),
    _LnDominoCmdInfoUnknown_Type()
)
lnDominoCmdInfoUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoUnknown.setStatus("optional")


class _LnDominoCmdInfoLogin_Type(Integer32):
    """Custom type lnDominoCmdInfoLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoLogin_Type.__name__ = "Integer32"
_LnDominoCmdInfoLogin_Object = MibScalar
lnDominoCmdInfoLogin = _LnDominoCmdInfoLogin_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 19),
    _LnDominoCmdInfoLogin_Type()
)
lnDominoCmdInfoLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoLogin.setStatus("optional")


class _LnDominoCmdInfoNavigate_Type(Integer32):
    """Custom type lnDominoCmdInfoNavigate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoNavigate_Type.__name__ = "Integer32"
_LnDominoCmdInfoNavigate_Object = MibScalar
lnDominoCmdInfoNavigate = _LnDominoCmdInfoNavigate_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 20),
    _LnDominoCmdInfoNavigate_Type()
)
lnDominoCmdInfoNavigate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoNavigate.setStatus("optional")


class _LnDominoCmdInfoReadForm_Type(Integer32):
    """Custom type lnDominoCmdInfoReadForm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoReadForm_Type.__name__ = "Integer32"
_LnDominoCmdInfoReadForm_Object = MibScalar
lnDominoCmdInfoReadForm = _LnDominoCmdInfoReadForm_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 21),
    _LnDominoCmdInfoReadForm_Type()
)
lnDominoCmdInfoReadForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoReadForm.setStatus("optional")


class _LnDominoCmdInfoTotal_Type(Integer32):
    """Custom type lnDominoCmdInfoTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCmdInfoTotal_Type.__name__ = "Integer32"
_LnDominoCmdInfoTotal_Object = MibScalar
lnDominoCmdInfoTotal = _LnDominoCmdInfoTotal_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 2, 22),
    _LnDominoCmdInfoTotal_Type()
)
lnDominoCmdInfoTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCmdInfoTotal.setStatus("optional")
_LnDominoConfig_ObjectIdentity = ObjectIdentity
lnDominoConfig = _LnDominoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3)
)


class _LnDominoCfgPortNumber_Type(Integer32):
    """Custom type lnDominoCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCfgPortNumber_Type.__name__ = "Integer32"
_LnDominoCfgPortNumber_Object = MibScalar
lnDominoCfgPortNumber = _LnDominoCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 1),
    _LnDominoCfgPortNumber_Type()
)
lnDominoCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgPortNumber.setStatus("optional")


class _LnDominoCfgPortStatus_Type(Integer32):
    """Custom type lnDominoCfgPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LnDominoCfgPortStatus_Type.__name__ = "Integer32"
_LnDominoCfgPortStatus_Object = MibScalar
lnDominoCfgPortStatus = _LnDominoCfgPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 2),
    _LnDominoCfgPortStatus_Type()
)
lnDominoCfgPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgPortStatus.setStatus("optional")
_LnDominoCfgHostName_Type = DisplayString
_LnDominoCfgHostName_Object = MibScalar
lnDominoCfgHostName = _LnDominoCfgHostName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 3),
    _LnDominoCfgHostName_Type()
)
lnDominoCfgHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgHostName.setStatus("optional")


class _LnDominoCfgDNSLookup_Type(Integer32):
    """Custom type lnDominoCfgDNSLookup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LnDominoCfgDNSLookup_Type.__name__ = "Integer32"
_LnDominoCfgDNSLookup_Object = MibScalar
lnDominoCfgDNSLookup = _LnDominoCfgDNSLookup_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 4),
    _LnDominoCfgDNSLookup_Type()
)
lnDominoCfgDNSLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgDNSLookup.setStatus("optional")
_LnDominoCfgHomeURL_Type = DisplayString
_LnDominoCfgHomeURL_Object = MibScalar
lnDominoCfgHomeURL = _LnDominoCfgHomeURL_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 5),
    _LnDominoCfgHomeURL_Type()
)
lnDominoCfgHomeURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgHomeURL.setStatus("optional")
_LnDominoCfgWelcomePage_Type = DisplayString
_LnDominoCfgWelcomePage_Object = MibScalar
lnDominoCfgWelcomePage = _LnDominoCfgWelcomePage_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 6),
    _LnDominoCfgWelcomePage_Type()
)
lnDominoCfgWelcomePage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgWelcomePage.setStatus("optional")


class _LnDominoCfgActiveThreadsMax_Type(Integer32):
    """Custom type lnDominoCfgActiveThreadsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCfgActiveThreadsMax_Type.__name__ = "Integer32"
_LnDominoCfgActiveThreadsMax_Object = MibScalar
lnDominoCfgActiveThreadsMax = _LnDominoCfgActiveThreadsMax_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 7),
    _LnDominoCfgActiveThreadsMax_Type()
)
lnDominoCfgActiveThreadsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgActiveThreadsMax.setStatus("optional")


class _LnDominoCfgActiveThreadsMin_Type(Integer32):
    """Custom type lnDominoCfgActiveThreadsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCfgActiveThreadsMin_Type.__name__ = "Integer32"
_LnDominoCfgActiveThreadsMin_Object = MibScalar
lnDominoCfgActiveThreadsMin = _LnDominoCfgActiveThreadsMin_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 8),
    _LnDominoCfgActiveThreadsMin_Type()
)
lnDominoCfgActiveThreadsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgActiveThreadsMin.setStatus("optional")


class _LnDominoCfgSSLPortNumber_Type(Integer32):
    """Custom type lnDominoCfgSSLPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCfgSSLPortNumber_Type.__name__ = "Integer32"
_LnDominoCfgSSLPortNumber_Object = MibScalar
lnDominoCfgSSLPortNumber = _LnDominoCfgSSLPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 9),
    _LnDominoCfgSSLPortNumber_Type()
)
lnDominoCfgSSLPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgSSLPortNumber.setStatus("optional")


class _LnDominoCfgSSLStatus_Type(Integer32):
    """Custom type lnDominoCfgSSLStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LnDominoCfgSSLStatus_Type.__name__ = "Integer32"
_LnDominoCfgSSLStatus_Object = MibScalar
lnDominoCfgSSLStatus = _LnDominoCfgSSLStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 10),
    _LnDominoCfgSSLStatus_Type()
)
lnDominoCfgSSLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgSSLStatus.setStatus("optional")
_LnDominoCfgSSLKeyFile_Type = DisplayString
_LnDominoCfgSSLKeyFile_Object = MibScalar
lnDominoCfgSSLKeyFile = _LnDominoCfgSSLKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 11),
    _LnDominoCfgSSLKeyFile_Type()
)
lnDominoCfgSSLKeyFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgSSLKeyFile.setStatus("optional")
_LnDominoCfgCacheDirectory_Type = DisplayString
_LnDominoCfgCacheDirectory_Object = MibScalar
lnDominoCfgCacheDirectory = _LnDominoCfgCacheDirectory_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 12),
    _LnDominoCfgCacheDirectory_Type()
)
lnDominoCfgCacheDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgCacheDirectory.setStatus("optional")


class _LnDominoCfgCacheSizeMax_Type(Integer32):
    """Custom type lnDominoCfgCacheSizeMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCfgCacheSizeMax_Type.__name__ = "Integer32"
_LnDominoCfgCacheSizeMax_Object = MibScalar
lnDominoCfgCacheSizeMax = _LnDominoCfgCacheSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 13),
    _LnDominoCfgCacheSizeMax_Type()
)
lnDominoCfgCacheSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgCacheSizeMax.setStatus("optional")


class _LnDominoCfgCacheDelete_Type(Integer32):
    """Custom type lnDominoCfgCacheDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LnDominoCfgCacheDelete_Type.__name__ = "Integer32"
_LnDominoCfgCacheDelete_Object = MibScalar
lnDominoCfgCacheDelete = _LnDominoCfgCacheDelete_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 14),
    _LnDominoCfgCacheDelete_Type()
)
lnDominoCfgCacheDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgCacheDelete.setStatus("optional")


class _LnDominoCfgGarbageCollectionStatus_Type(Integer32):
    """Custom type lnDominoCfgGarbageCollectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LnDominoCfgGarbageCollectionStatus_Type.__name__ = "Integer32"
_LnDominoCfgGarbageCollectionStatus_Object = MibScalar
lnDominoCfgGarbageCollectionStatus = _LnDominoCfgGarbageCollectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 15),
    _LnDominoCfgGarbageCollectionStatus_Type()
)
lnDominoCfgGarbageCollectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgGarbageCollectionStatus.setStatus("optional")


class _LnDominoCfgGarbageCollectionInterval_Type(Integer32):
    """Custom type lnDominoCfgGarbageCollectionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCfgGarbageCollectionInterval_Type.__name__ = "Integer32"
_LnDominoCfgGarbageCollectionInterval_Object = MibScalar
lnDominoCfgGarbageCollectionInterval = _LnDominoCfgGarbageCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 16),
    _LnDominoCfgGarbageCollectionInterval_Type()
)
lnDominoCfgGarbageCollectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgGarbageCollectionInterval.setStatus("optional")
_LnDominoCfgImageFormat_Type = DisplayString
_LnDominoCfgImageFormat_Object = MibScalar
lnDominoCfgImageFormat = _LnDominoCfgImageFormat_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 17),
    _LnDominoCfgImageFormat_Type()
)
lnDominoCfgImageFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgImageFormat.setStatus("optional")


class _LnDominoCfgImageInterlaced_Type(Integer32):
    """Custom type lnDominoCfgImageInterlaced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LnDominoCfgImageInterlaced_Type.__name__ = "Integer32"
_LnDominoCfgImageInterlaced_Object = MibScalar
lnDominoCfgImageInterlaced = _LnDominoCfgImageInterlaced_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 18),
    _LnDominoCfgImageInterlaced_Type()
)
lnDominoCfgImageInterlaced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgImageInterlaced.setStatus("optional")


class _LnDominoCfgViewLines_Type(Integer32):
    """Custom type lnDominoCfgViewLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCfgViewLines_Type.__name__ = "Integer32"
_LnDominoCfgViewLines_Object = MibScalar
lnDominoCfgViewLines = _LnDominoCfgViewLines_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 19),
    _LnDominoCfgViewLines_Type()
)
lnDominoCfgViewLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgViewLines.setStatus("optional")
_LnDominoCfgDirectoryHTML_Type = DisplayString
_LnDominoCfgDirectoryHTML_Object = MibScalar
lnDominoCfgDirectoryHTML = _LnDominoCfgDirectoryHTML_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 20),
    _LnDominoCfgDirectoryHTML_Type()
)
lnDominoCfgDirectoryHTML.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgDirectoryHTML.setStatus("optional")
_LnDominoCfgDirectoryURLPathCGI_Type = DisplayString
_LnDominoCfgDirectoryURLPathCGI_Object = MibScalar
lnDominoCfgDirectoryURLPathCGI = _LnDominoCfgDirectoryURLPathCGI_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 21),
    _LnDominoCfgDirectoryURLPathCGI_Type()
)
lnDominoCfgDirectoryURLPathCGI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgDirectoryURLPathCGI.setStatus("optional")
_LnDominoCfgDirectoryCGI_Type = DisplayString
_LnDominoCfgDirectoryCGI_Object = MibScalar
lnDominoCfgDirectoryCGI = _LnDominoCfgDirectoryCGI_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 22),
    _LnDominoCfgDirectoryCGI_Type()
)
lnDominoCfgDirectoryCGI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgDirectoryCGI.setStatus("optional")
_LnDominoCfgDirectoryURLPathIcons_Type = DisplayString
_LnDominoCfgDirectoryURLPathIcons_Object = MibScalar
lnDominoCfgDirectoryURLPathIcons = _LnDominoCfgDirectoryURLPathIcons_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 23),
    _LnDominoCfgDirectoryURLPathIcons_Type()
)
lnDominoCfgDirectoryURLPathIcons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgDirectoryURLPathIcons.setStatus("optional")
_LnDominoCfgDirectoryIcons_Type = DisplayString
_LnDominoCfgDirectoryIcons_Object = MibScalar
lnDominoCfgDirectoryIcons = _LnDominoCfgDirectoryIcons_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 24),
    _LnDominoCfgDirectoryIcons_Type()
)
lnDominoCfgDirectoryIcons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgDirectoryIcons.setStatus("optional")
_LnDominoCfgLogAccess_Type = DisplayString
_LnDominoCfgLogAccess_Object = MibScalar
lnDominoCfgLogAccess = _LnDominoCfgLogAccess_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 25),
    _LnDominoCfgLogAccess_Type()
)
lnDominoCfgLogAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgLogAccess.setStatus("optional")
_LnDominoCfgLogError_Type = DisplayString
_LnDominoCfgLogError_Object = MibScalar
lnDominoCfgLogError = _LnDominoCfgLogError_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 26),
    _LnDominoCfgLogError_Type()
)
lnDominoCfgLogError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgLogError.setStatus("optional")
_LnDominoCfgLogTimeStamp_Type = DisplayString
_LnDominoCfgLogTimeStamp_Object = MibScalar
lnDominoCfgLogTimeStamp = _LnDominoCfgLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 27),
    _LnDominoCfgLogTimeStamp_Type()
)
lnDominoCfgLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgLogTimeStamp.setStatus("optional")
_LnDominoCfgLogFilter_Type = DisplayString
_LnDominoCfgLogFilter_Object = MibScalar
lnDominoCfgLogFilter = _LnDominoCfgLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 28),
    _LnDominoCfgLogFilter_Type()
)
lnDominoCfgLogFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgLogFilter.setStatus("optional")


class _LnDominoCfgTimeoutIdleThread_Type(Integer32):
    """Custom type lnDominoCfgTimeoutIdleThread based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCfgTimeoutIdleThread_Type.__name__ = "Integer32"
_LnDominoCfgTimeoutIdleThread_Object = MibScalar
lnDominoCfgTimeoutIdleThread = _LnDominoCfgTimeoutIdleThread_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 29),
    _LnDominoCfgTimeoutIdleThread_Type()
)
lnDominoCfgTimeoutIdleThread.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgTimeoutIdleThread.setStatus("optional")


class _LnDominoCfgTimeoutInput_Type(Integer32):
    """Custom type lnDominoCfgTimeoutInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCfgTimeoutInput_Type.__name__ = "Integer32"
_LnDominoCfgTimeoutInput_Object = MibScalar
lnDominoCfgTimeoutInput = _LnDominoCfgTimeoutInput_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 30),
    _LnDominoCfgTimeoutInput_Type()
)
lnDominoCfgTimeoutInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgTimeoutInput.setStatus("optional")


class _LnDominoCfgTimeoutOutput_Type(Integer32):
    """Custom type lnDominoCfgTimeoutOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCfgTimeoutOutput_Type.__name__ = "Integer32"
_LnDominoCfgTimeoutOutput_Object = MibScalar
lnDominoCfgTimeoutOutput = _LnDominoCfgTimeoutOutput_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 31),
    _LnDominoCfgTimeoutOutput_Type()
)
lnDominoCfgTimeoutOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgTimeoutOutput.setStatus("optional")


class _LnDominoCfgTimeoutCGI_Type(Integer32):
    """Custom type lnDominoCfgTimeoutCGI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnDominoCfgTimeoutCGI_Type.__name__ = "Integer32"
_LnDominoCfgTimeoutCGI_Object = MibScalar
lnDominoCfgTimeoutCGI = _LnDominoCfgTimeoutCGI_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 15, 3, 32),
    _LnDominoCfgTimeoutCGI_Type()
)
lnDominoCfgTimeoutCGI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnDominoCfgTimeoutCGI.setStatus("optional")
_LnCalendar_ObjectIdentity = ObjectIdentity
lnCalendar = _LnCalendar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 16)
)


class _LnCalTotalAllApptsResources_Type(Integer32):
    """Custom type lnCalTotalAllApptsResources based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnCalTotalAllApptsResources_Type.__name__ = "Integer32"
_LnCalTotalAllApptsResources_Object = MibScalar
lnCalTotalAllApptsResources = _LnCalTotalAllApptsResources_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 16, 1),
    _LnCalTotalAllApptsResources_Type()
)
lnCalTotalAllApptsResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnCalTotalAllApptsResources.setStatus("optional")


class _LnCalTotalAllUsersResources_Type(Integer32):
    """Custom type lnCalTotalAllUsersResources based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnCalTotalAllUsersResources_Type.__name__ = "Integer32"
_LnCalTotalAllUsersResources_Object = MibScalar
lnCalTotalAllUsersResources = _LnCalTotalAllUsersResources_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 16, 2),
    _LnCalTotalAllUsersResources_Type()
)
lnCalTotalAllUsersResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnCalTotalAllUsersResources.setStatus("optional")


class _LnCalTotalAppointments_Type(Integer32):
    """Custom type lnCalTotalAppointments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnCalTotalAppointments_Type.__name__ = "Integer32"
_LnCalTotalAppointments_Object = MibScalar
lnCalTotalAppointments = _LnCalTotalAppointments_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 16, 3),
    _LnCalTotalAppointments_Type()
)
lnCalTotalAppointments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnCalTotalAppointments.setStatus("optional")


class _LnCalTotalReservations_Type(Integer32):
    """Custom type lnCalTotalReservations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnCalTotalReservations_Type.__name__ = "Integer32"
_LnCalTotalReservations_Object = MibScalar
lnCalTotalReservations = _LnCalTotalReservations_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 16, 4),
    _LnCalTotalReservations_Type()
)
lnCalTotalReservations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnCalTotalReservations.setStatus("optional")


class _LnCalTotalResources_Type(Integer32):
    """Custom type lnCalTotalResources based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnCalTotalResources_Type.__name__ = "Integer32"
_LnCalTotalResources_Object = MibScalar
lnCalTotalResources = _LnCalTotalResources_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 16, 5),
    _LnCalTotalResources_Type()
)
lnCalTotalResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnCalTotalResources.setStatus("optional")


class _LnCalTotalUsers_Type(Integer32):
    """Custom type lnCalTotalUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496795),
    )


_LnCalTotalUsers_Type.__name__ = "Integer32"
_LnCalTotalUsers_Object = MibScalar
lnCalTotalUsers = _LnCalTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 16, 6),
    _LnCalTotalUsers_Type()
)
lnCalTotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnCalTotalUsers.setStatus("optional")
_LnCollector_ObjectIdentity = ObjectIdentity
lnCollector = _LnCollector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 17)
)


class _LnCollectorTimeCollected_Type(Integer32):
    """Custom type lnCollectorTimeCollected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnCollectorTimeCollected_Type.__name__ = "Integer32"
_LnCollectorTimeCollected_Object = MibScalar
lnCollectorTimeCollected = _LnCollectorTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 17, 1),
    _LnCollectorTimeCollected_Type()
)
lnCollectorTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnCollectorTimeCollected.setStatus("mandatory")
_LnCollectorTimeElapsed_Type = DisplayString
_LnCollectorTimeElapsed_Object = MibScalar
lnCollectorTimeElapsed = _LnCollectorTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 1, 17, 2),
    _LnCollectorTimeElapsed_Type()
)
lnCollectorTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnCollectorTimeElapsed.setStatus("mandatory")
_LnMIBVersion_Type = DisplayString
_LnMIBVersion_Object = MibScalar
lnMIBVersion = _LnMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 3),
    _LnMIBVersion_Type()
)
lnMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMIBVersion.setStatus("mandatory")
_LnQSBuildNumber_Type = DisplayString
_LnQSBuildNumber_Object = MibScalar
lnQSBuildNumber = _LnQSBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 1, 5),
    _LnQSBuildNumber_Type()
)
lnQSBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnQSBuildNumber.setStatus("mandatory")
_LnControl_ObjectIdentity = ObjectIdentity
lnControl = _LnControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 2)
)


class _LnNotesServerSetState_Type(Integer32):
    """Custom type lnNotesServerSetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_LnNotesServerSetState_Type.__name__ = "Integer32"
_LnNotesServerSetState_Object = MibScalar
lnNotesServerSetState = _LnNotesServerSetState_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 1),
    _LnNotesServerSetState_Type()
)
lnNotesServerSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnNotesServerSetState.setStatus("mandatory")


class _LnNotesServerState_Type(Integer32):
    """Custom type lnNotesServerState based on Integer32"""
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
        *(("crashed", 4),
          ("down", 2),
          ("not-responding", 3),
          ("unknown", 5),
          ("up", 1))
    )


_LnNotesServerState_Type.__name__ = "Integer32"
_LnNotesServerState_Object = MibScalar
lnNotesServerState = _LnNotesServerState_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 2),
    _LnNotesServerState_Type()
)
lnNotesServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnNotesServerState.setStatus("mandatory")


class _LnLastTrapSeq_Type(Integer32):
    """Custom type lnLastTrapSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnLastTrapSeq_Type.__name__ = "Integer32"
_LnLastTrapSeq_Object = MibScalar
lnLastTrapSeq = _LnLastTrapSeq_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 3),
    _LnLastTrapSeq_Type()
)
lnLastTrapSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnLastTrapSeq.setStatus("mandatory")
_LnRecentTrapsTable_Object = MibTable
lnRecentTrapsTable = _LnRecentTrapsTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 4)
)
if mibBuilder.loadTexts:
    lnRecentTrapsTable.setStatus("mandatory")
_LnRecentTrapsEntry_Object = MibTableRow
lnRecentTrapsEntry = _LnRecentTrapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 4, 1)
)
lnRecentTrapsEntry.setIndexNames(
    (0, "NOTES-MIB", "lnTrapSeq"),
)
if mibBuilder.loadTexts:
    lnRecentTrapsEntry.setStatus("mandatory")


class _LnTrapSeq_Type(Integer32):
    """Custom type lnTrapSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnTrapSeq_Type.__name__ = "Integer32"
_LnTrapSeq_Object = MibTableColumn
lnTrapSeq = _LnTrapSeq_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 4, 1, 1),
    _LnTrapSeq_Type()
)
lnTrapSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTrapSeq.setStatus("mandatory")
_LnTrapInfo_Type = DisplayString
_LnTrapInfo_Object = MibTableColumn
lnTrapInfo = _LnTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 4, 1, 2),
    _LnTrapInfo_Type()
)
lnTrapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTrapInfo.setStatus("mandatory")


class _LnRemoteReboot_Type(Integer32):
    """Custom type lnRemoteReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LnRemoteReboot_Type.__name__ = "Integer32"
_LnRemoteReboot_Object = MibScalar
lnRemoteReboot = _LnRemoteReboot_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 5),
    _LnRemoteReboot_Type()
)
lnRemoteReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnRemoteReboot.setStatus("mandatory")
_LnServerTbl_Object = MibTable
lnServerTbl = _LnServerTbl_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 6)
)
if mibBuilder.loadTexts:
    lnServerTbl.setStatus("optional")
_LnServerTblEntry_Object = MibTableRow
lnServerTblEntry = _LnServerTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 6, 1)
)
lnServerTblEntry.setIndexNames(
    (0, "NOTES-MIB", "lnServerTblIndex"),
)
if mibBuilder.loadTexts:
    lnServerTblEntry.setStatus("optional")


class _LnServerTblIndex_Type(Integer32):
    """Custom type lnServerTblIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnServerTblIndex_Type.__name__ = "Integer32"
_LnServerTblIndex_Object = MibTableColumn
lnServerTblIndex = _LnServerTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 6, 1, 1),
    _LnServerTblIndex_Type()
)
lnServerTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerTblIndex.setStatus("optional")
_LnServerTblName_Type = DisplayString
_LnServerTblName_Object = MibTableColumn
lnServerTblName = _LnServerTblName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 6, 1, 2),
    _LnServerTblName_Type()
)
lnServerTblName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerTblName.setStatus("optional")


class _LnServerTblNotesPartition_Type(Integer32):
    """Custom type lnServerTblNotesPartition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnServerTblNotesPartition_Type.__name__ = "Integer32"
_LnServerTblNotesPartition_Object = MibTableColumn
lnServerTblNotesPartition = _LnServerTblNotesPartition_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 6, 1, 3),
    _LnServerTblNotesPartition_Type()
)
lnServerTblNotesPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerTblNotesPartition.setStatus("optional")
_LnServerTblDataDir_Type = DisplayString
_LnServerTblDataDir_Object = MibTableColumn
lnServerTblDataDir = _LnServerTblDataDir_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 6, 1, 4),
    _LnServerTblDataDir_Type()
)
lnServerTblDataDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerTblDataDir.setStatus("optional")


class _LnServerTblDataDirValid_Type(Integer32):
    """Custom type lnServerTblDataDirValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LnServerTblDataDirValid_Type.__name__ = "Integer32"
_LnServerTblDataDirValid_Object = MibTableColumn
lnServerTblDataDirValid = _LnServerTblDataDirValid_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 6, 1, 5),
    _LnServerTblDataDirValid_Type()
)
lnServerTblDataDirValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerTblDataDirValid.setStatus("optional")


class _LnServerTblState_Type(Integer32):
    """Custom type lnServerTblState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_LnServerTblState_Type.__name__ = "Integer32"
_LnServerTblState_Object = MibTableColumn
lnServerTblState = _LnServerTblState_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 6, 1, 6),
    _LnServerTblState_Type()
)
lnServerTblState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerTblState.setStatus("optional")


class _LnServerIdentifiedItself_Type(Integer32):
    """Custom type lnServerIdentifiedItself based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LnServerIdentifiedItself_Type.__name__ = "Integer32"
_LnServerIdentifiedItself_Object = MibTableColumn
lnServerIdentifiedItself = _LnServerIdentifiedItself_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 6, 1, 7),
    _LnServerIdentifiedItself_Type()
)
lnServerIdentifiedItself.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnServerIdentifiedItself.setStatus("optional")


class _LnServerTblSetState_Type(Integer32):
    """Custom type lnServerTblSetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_LnServerTblSetState_Type.__name__ = "Integer32"
_LnServerTblSetState_Object = MibTableColumn
lnServerTblSetState = _LnServerTblSetState_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 6, 1, 8),
    _LnServerTblSetState_Type()
)
lnServerTblSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lnServerTblSetState.setStatus("optional")


class _LnTotalPartitions_Type(Integer32):
    """Custom type lnTotalPartitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnTotalPartitions_Type.__name__ = "Integer32"
_LnTotalPartitions_Object = MibScalar
lnTotalPartitions = _LnTotalPartitions_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 7),
    _LnTotalPartitions_Type()
)
lnTotalPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnTotalPartitions.setStatus("mandatory")
_LnMPAIniFileLocation_Type = DisplayString
_LnMPAIniFileLocation_Object = MibScalar
lnMPAIniFileLocation = _LnMPAIniFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 2, 8),
    _LnMPAIniFileLocation_Type()
)
lnMPAIniFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMPAIniFileLocation.setStatus("mandatory")
_LnInterceptor_ObjectIdentity = ObjectIdentity
lnInterceptor = _LnInterceptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 3)
)
_LnEvtServer_Type = DisplayString
_LnEvtServer_Object = MibScalar
lnEvtServer = _LnEvtServer_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 3, 1),
    _LnEvtServer_Type()
)
lnEvtServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnEvtServer.setStatus("mandatory")


class _LnEvtType_Type(Integer32):
    """Custom type lnEvtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 8),
          ("communications", 1),
          ("mail", 3),
          ("miscellaneous", 6),
          ("replication", 4),
          ("resource", 5),
          ("security", 2),
          ("server", 7),
          ("unknown", 0))
    )


_LnEvtType_Type.__name__ = "Integer32"
_LnEvtType_Object = MibScalar
lnEvtType = _LnEvtType_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 3, 2),
    _LnEvtType_Type()
)
lnEvtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnEvtType.setStatus("mandatory")


class _LnEvtSeverity_Type(Integer32):
    """Custom type lnEvtSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("fatal", 1),
          ("normal", 5),
          ("unknown", 0),
          ("warning1", 3),
          ("warning2", 4))
    )


_LnEvtSeverity_Type.__name__ = "Integer32"
_LnEvtSeverity_Object = MibScalar
lnEvtSeverity = _LnEvtSeverity_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 3, 3),
    _LnEvtSeverity_Type()
)
lnEvtSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnEvtSeverity.setStatus("mandatory")


class _LnEvtWhen_Type(Integer32):
    """Custom type lnEvtWhen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnEvtWhen_Type.__name__ = "Integer32"
_LnEvtWhen_Object = MibScalar
lnEvtWhen = _LnEvtWhen_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 3, 4),
    _LnEvtWhen_Type()
)
lnEvtWhen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnEvtWhen.setStatus("mandatory")
_LnEvtData_Type = DisplayString
_LnEvtData_Object = MibScalar
lnEvtData = _LnEvtData_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 3, 5),
    _LnEvtData_Type()
)
lnEvtData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnEvtData.setStatus("mandatory")


class _LnEvtSeq_Type(Integer32):
    """Custom type lnEvtSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LnEvtSeq_Type.__name__ = "Integer32"
_LnEvtSeq_Object = MibScalar
lnEvtSeq = _LnEvtSeq_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 3, 6),
    _LnEvtSeq_Type()
)
lnEvtSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnEvtSeq.setStatus("mandatory")
_LnUnix_ObjectIdentity = ObjectIdentity
lnUnix = _LnUnix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 4)
)
_LnAlarm_ObjectIdentity = ObjectIdentity
lnAlarm = _LnAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1)
)


class _LnAlarmServerHandle_Type(Integer32):
    """Custom type lnAlarmServerHandle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnAlarmServerHandle_Type.__name__ = "Integer32"
_LnAlarmServerHandle_Object = MibScalar
lnAlarmServerHandle = _LnAlarmServerHandle_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 1),
    _LnAlarmServerHandle_Type()
)
lnAlarmServerHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmServerHandle.setStatus("optional")


class _LnAlarmTargetHandle_Type(Integer32):
    """Custom type lnAlarmTargetHandle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnAlarmTargetHandle_Type.__name__ = "Integer32"
_LnAlarmTargetHandle_Object = MibScalar
lnAlarmTargetHandle = _LnAlarmTargetHandle_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 2),
    _LnAlarmTargetHandle_Type()
)
lnAlarmTargetHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmTargetHandle.setStatus("optional")


class _LnAlarmDate_Type(Integer32):
    """Custom type lnAlarmDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnAlarmDate_Type.__name__ = "Integer32"
_LnAlarmDate_Object = MibScalar
lnAlarmDate = _LnAlarmDate_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 3),
    _LnAlarmDate_Type()
)
lnAlarmDate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmDate.setStatus("optional")


class _LnAlarmTime_Type(Integer32):
    """Custom type lnAlarmTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnAlarmTime_Type.__name__ = "Integer32"
_LnAlarmTime_Object = MibScalar
lnAlarmTime = _LnAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 4),
    _LnAlarmTime_Type()
)
lnAlarmTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmTime.setStatus("optional")


class _LnAlarmSeverity_Type(Integer32):
    """Custom type lnAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("critical", 9),
          ("disabled", 2),
          ("informational", 1),
          ("major", 8),
          ("marginal", 5),
          ("minor", 7),
          ("normal", 0),
          ("unknown", 4),
          ("unmanaged", 3),
          ("warning", 6))
    )


_LnAlarmSeverity_Type.__name__ = "Integer32"
_LnAlarmSeverity_Object = MibScalar
lnAlarmSeverity = _LnAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 5),
    _LnAlarmSeverity_Type()
)
lnAlarmSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmSeverity.setStatus("optional")


class _LnAlarmIntArg_Type(Integer32):
    """Custom type lnAlarmIntArg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LnAlarmIntArg_Type.__name__ = "Integer32"
_LnAlarmIntArg_Object = MibScalar
lnAlarmIntArg = _LnAlarmIntArg_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 6),
    _LnAlarmIntArg_Type()
)
lnAlarmIntArg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmIntArg.setStatus("optional")


class _LnAlarmLongArg_Type(Integer32):
    """Custom type lnAlarmLongArg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnAlarmLongArg_Type.__name__ = "Integer32"
_LnAlarmLongArg_Object = MibScalar
lnAlarmLongArg = _LnAlarmLongArg_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 7),
    _LnAlarmLongArg_Type()
)
lnAlarmLongArg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmLongArg.setStatus("optional")
_LnAlarmDoubleArg_Type = OctetString
_LnAlarmDoubleArg_Object = MibScalar
lnAlarmDoubleArg = _LnAlarmDoubleArg_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 8),
    _LnAlarmDoubleArg_Type()
)
lnAlarmDoubleArg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmDoubleArg.setStatus("optional")
_LnAlarmTextArg1_Type = OctetString
_LnAlarmTextArg1_Object = MibScalar
lnAlarmTextArg1 = _LnAlarmTextArg1_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 9),
    _LnAlarmTextArg1_Type()
)
lnAlarmTextArg1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmTextArg1.setStatus("optional")
_LnAlarmTextArg2_Type = OctetString
_LnAlarmTextArg2_Object = MibScalar
lnAlarmTextArg2 = _LnAlarmTextArg2_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 10),
    _LnAlarmTextArg2_Type()
)
lnAlarmTextArg2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmTextArg2.setStatus("optional")
_LnAlarmSeverityStr_Type = DisplayString
_LnAlarmSeverityStr_Object = MibScalar
lnAlarmSeverityStr = _LnAlarmSeverityStr_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 11),
    _LnAlarmSeverityStr_Type()
)
lnAlarmSeverityStr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmSeverityStr.setStatus("optional")
_LnAlarmTypeStr_Type = DisplayString
_LnAlarmTypeStr_Object = MibScalar
lnAlarmTypeStr = _LnAlarmTypeStr_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 12),
    _LnAlarmTypeStr_Type()
)
lnAlarmTypeStr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmTypeStr.setStatus("optional")
_LnAlarmMessage_Type = DisplayString
_LnAlarmMessage_Object = MibScalar
lnAlarmMessage = _LnAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 13),
    _LnAlarmMessage_Type()
)
lnAlarmMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmMessage.setStatus("optional")
_LnAlarmMessageExt_Type = DisplayString
_LnAlarmMessageExt_Object = MibScalar
lnAlarmMessageExt = _LnAlarmMessageExt_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 14),
    _LnAlarmMessageExt_Type()
)
lnAlarmMessageExt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmMessageExt.setStatus("optional")
_LnAlarmServerName_Type = DisplayString
_LnAlarmServerName_Object = MibScalar
lnAlarmServerName = _LnAlarmServerName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 1, 15),
    _LnAlarmServerName_Type()
)
lnAlarmServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnAlarmServerName.setStatus("optional")
_LnSignal_ObjectIdentity = ObjectIdentity
lnSignal = _LnSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 2)
)


class _LnSignalServerId_Type(Integer32):
    """Custom type lnSignalServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnSignalServerId_Type.__name__ = "Integer32"
_LnSignalServerId_Object = MibScalar
lnSignalServerId = _LnSignalServerId_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 2, 1),
    _LnSignalServerId_Type()
)
lnSignalServerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnSignalServerId.setStatus("optional")


class _LnSignalOldServerType_Type(Integer32):
    """Custom type lnSignalOldServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnSignalOldServerType_Type.__name__ = "Integer32"
_LnSignalOldServerType_Object = MibScalar
lnSignalOldServerType = _LnSignalOldServerType_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 2, 2),
    _LnSignalOldServerType_Type()
)
lnSignalOldServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnSignalOldServerType.setStatus("optional")


class _LnSignalNewServerType_Type(Integer32):
    """Custom type lnSignalNewServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnSignalNewServerType_Type.__name__ = "Integer32"
_LnSignalNewServerType_Object = MibScalar
lnSignalNewServerType = _LnSignalNewServerType_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 2, 3),
    _LnSignalNewServerType_Type()
)
lnSignalNewServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnSignalNewServerType.setStatus("optional")


class _LnSignalWhatHasChanged_Type(Integer32):
    """Custom type lnSignalWhatHasChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LnSignalWhatHasChanged_Type.__name__ = "Integer32"
_LnSignalWhatHasChanged_Object = MibScalar
lnSignalWhatHasChanged = _LnSignalWhatHasChanged_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 2, 4),
    _LnSignalWhatHasChanged_Type()
)
lnSignalWhatHasChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnSignalWhatHasChanged.setStatus("optional")
_LnSignalServerName_Type = DisplayString
_LnSignalServerName_Object = MibScalar
lnSignalServerName = _LnSignalServerName_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 4, 2, 5),
    _LnSignalServerName_Type()
)
lnSignalServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lnSignalServerName.setStatus("optional")
_MapInfo_ObjectIdentity = ObjectIdentity
mapInfo = _MapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 72, 100)
)
_LnMainProxyAgentVersion_Type = DisplayString
_LnMainProxyAgentVersion_Object = MibScalar
lnMainProxyAgentVersion = _LnMainProxyAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 334, 72, 100, 1),
    _LnMainProxyAgentVersion_Type()
)
lnMainProxyAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnMainProxyAgentVersion.setStatus("mandatory")
_NotesPump_ObjectIdentity = ObjectIdentity
notesPump = _NotesPump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 73)
)

# Managed Objects groups


# Notification objects

lnUnknownEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 0)
)
lnUnknownEventTrap.setObjects(
      *(("NOTES-MIB", "lnEvtServer"),
        ("NOTES-MIB", "lnEvtType"),
        ("NOTES-MIB", "lnEvtSeverity"),
        ("NOTES-MIB", "lnEvtWhen"),
        ("NOTES-MIB", "lnEvtData"),
        ("NOTES-MIB", "lnEvtSeq"))
)
if mibBuilder.loadTexts:
    lnUnknownEventTrap.setStatus(
        ""
    )

lnFatalEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 1)
)
lnFatalEventTrap.setObjects(
      *(("NOTES-MIB", "lnEvtServer"),
        ("NOTES-MIB", "lnEvtType"),
        ("NOTES-MIB", "lnEvtSeverity"),
        ("NOTES-MIB", "lnEvtWhen"),
        ("NOTES-MIB", "lnEvtData"),
        ("NOTES-MIB", "lnEvtSeq"))
)
if mibBuilder.loadTexts:
    lnFatalEventTrap.setStatus(
        ""
    )

lnFailureEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 2)
)
lnFailureEventTrap.setObjects(
      *(("NOTES-MIB", "lnEvtServer"),
        ("NOTES-MIB", "lnEvtType"),
        ("NOTES-MIB", "lnEvtSeverity"),
        ("NOTES-MIB", "lnEvtWhen"),
        ("NOTES-MIB", "lnEvtData"),
        ("NOTES-MIB", "lnEvtSeq"))
)
if mibBuilder.loadTexts:
    lnFailureEventTrap.setStatus(
        ""
    )

lnWarning1EventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 3)
)
lnWarning1EventTrap.setObjects(
      *(("NOTES-MIB", "lnEvtServer"),
        ("NOTES-MIB", "lnEvtType"),
        ("NOTES-MIB", "lnEvtSeverity"),
        ("NOTES-MIB", "lnEvtWhen"),
        ("NOTES-MIB", "lnEvtData"),
        ("NOTES-MIB", "lnEvtSeq"))
)
if mibBuilder.loadTexts:
    lnWarning1EventTrap.setStatus(
        ""
    )

lnWarning2EventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 4)
)
lnWarning2EventTrap.setObjects(
      *(("NOTES-MIB", "lnEvtServer"),
        ("NOTES-MIB", "lnEvtType"),
        ("NOTES-MIB", "lnEvtSeverity"),
        ("NOTES-MIB", "lnEvtWhen"),
        ("NOTES-MIB", "lnEvtData"),
        ("NOTES-MIB", "lnEvtSeq"))
)
if mibBuilder.loadTexts:
    lnWarning2EventTrap.setStatus(
        ""
    )

lnNormalEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 5)
)
lnNormalEventTrap.setObjects(
      *(("NOTES-MIB", "lnEvtServer"),
        ("NOTES-MIB", "lnEvtType"),
        ("NOTES-MIB", "lnEvtSeverity"),
        ("NOTES-MIB", "lnEvtWhen"),
        ("NOTES-MIB", "lnEvtData"),
        ("NOTES-MIB", "lnEvtSeq"))
)
if mibBuilder.loadTexts:
    lnNormalEventTrap.setStatus(
        ""
    )

lnServerUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 11)
)
lnServerUpTrap.setObjects(
    ("NOTES-MIB", "lnEvtServer")
)
if mibBuilder.loadTexts:
    lnServerUpTrap.setStatus(
        ""
    )

lnServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 12)
)
lnServerDownTrap.setObjects(
    ("NOTES-MIB", "lnEvtServer")
)
if mibBuilder.loadTexts:
    lnServerDownTrap.setStatus(
        ""
    )

lnServerPulseFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 13)
)
lnServerPulseFailedTrap.setObjects(
    ("NOTES-MIB", "lnEvtServer")
)
if mibBuilder.loadTexts:
    lnServerPulseFailedTrap.setStatus(
        ""
    )

lnServerPulseRestoredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 14)
)
lnServerPulseRestoredTrap.setObjects(
    ("NOTES-MIB", "lnEvtServer")
)
if mibBuilder.loadTexts:
    lnServerPulseRestoredTrap.setStatus(
        ""
    )

lnSystemRebootingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 15)
)
if mibBuilder.loadTexts:
    lnSystemRebootingTrap.setStatus(
        ""
    )

lnServerNotRespondingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 16)
)
lnServerNotRespondingTrap.setObjects(
    ("NOTES-MIB", "lnEvtServer")
)
if mibBuilder.loadTexts:
    lnServerNotRespondingTrap.setStatus(
        ""
    )

lnServerNowRespondingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 17)
)
lnServerNowRespondingTrap.setObjects(
    ("NOTES-MIB", "lnEvtServer")
)
if mibBuilder.loadTexts:
    lnServerNowRespondingTrap.setStatus(
        ""
    )

lnAlarmStatisticThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 30)
)
lnAlarmStatisticThreshold.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmStatisticThreshold.setStatus(
        ""
    )

lnAlarmServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 31)
)
lnAlarmServerStatusChange.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmServerStatusChange.setStatus(
        ""
    )

lnAlarmPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 32)
)
lnAlarmPortStatusChange.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmPortStatusChange.setStatus(
        ""
    )

lnAlarmTaskStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 33)
)
lnAlarmTaskStatusChange.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmTaskStatusChange.setStatus(
        ""
    )

lnAlarmNVStatClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 34)
)
lnAlarmNVStatClear.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmNVStatClear.setStatus(
        ""
    )

lnAlarmAutoDiscovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 35)
)
lnAlarmAutoDiscovery.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmAutoDiscovery.setStatus(
        ""
    )

lnAlarmServerNotesEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 36)
)
lnAlarmServerNotesEvent.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmServerNotesEvent.setStatus(
        ""
    )

lnAlarmServerCfgChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 37)
)
lnAlarmServerCfgChangeEvent.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmServerCfgChangeEvent.setStatus(
        ""
    )

lnAlarmMailProbeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 38)
)
lnAlarmMailProbeEvent.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmMailProbeEvent.setStatus(
        ""
    )

lnAlarmServerSNMPEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 39)
)
lnAlarmServerSNMPEvent.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmServerSNMPEvent.setStatus(
        ""
    )

lnAlarmNSFRemoteConsoleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 40)
)
lnAlarmNSFRemoteConsoleEvent.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmNSFRemoteConsoleEvent.setStatus(
        ""
    )

lnAlarmMailBoxEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 41)
)
lnAlarmMailBoxEvent.setObjects(
      *(("NOTES-MIB", "lnAlarmServerHandle"),
        ("NOTES-MIB", "lnAlarmTargetHandle"),
        ("NOTES-MIB", "lnAlarmDate"),
        ("NOTES-MIB", "lnAlarmTime"),
        ("NOTES-MIB", "lnAlarmSeverity"),
        ("NOTES-MIB", "lnAlarmIntArg"),
        ("NOTES-MIB", "lnAlarmLongArg"),
        ("NOTES-MIB", "lnAlarmDoubleArg"),
        ("NOTES-MIB", "lnAlarmTextArg1"),
        ("NOTES-MIB", "lnAlarmTextArg2"))
)
if mibBuilder.loadTexts:
    lnAlarmMailBoxEvent.setStatus(
        ""
    )

lnAlarmClearAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 50)
)
if mibBuilder.loadTexts:
    lnAlarmClearAll.setStatus(
        ""
    )

lnAlarmClearServers = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 51)
)
lnAlarmClearServers.setObjects(
    ("NOTES-MIB", "lnAlarmServerHandle")
)
if mibBuilder.loadTexts:
    lnAlarmClearServers.setStatus(
        ""
    )

lnSignalAutodiscoveryStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 52)
)
if mibBuilder.loadTexts:
    lnSignalAutodiscoveryStart.setStatus(
        ""
    )

lnSignalAutodiscoveryFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 53)
)
if mibBuilder.loadTexts:
    lnSignalAutodiscoveryFinished.setStatus(
        ""
    )

lnSignalServerConfigChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 54)
)
lnSignalServerConfigChg.setObjects(
      *(("NOTES-MIB", "lnSignalServerId"),
        ("NOTES-MIB", "lnSignalOldServerType"),
        ("NOTES-MIB", "lnSignalNewServerType"),
        ("NOTES-MIB", "lnSignalWhatHasChanged"))
)
if mibBuilder.loadTexts:
    lnSignalServerConfigChg.setStatus(
        ""
    )

lnTrapRequestMostSevereStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 55)
)
lnTrapRequestMostSevereStatus.setObjects(
    ("NOTES-MIB", "lnAlarmServerHandle")
)
if mibBuilder.loadTexts:
    lnTrapRequestMostSevereStatus.setStatus(
        ""
    )

lnTrapDisplayAlarmClearServers = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 60)
)
lnTrapDisplayAlarmClearServers.setObjects(
      *(("NOTES-MIB", "lnSignalServerId"),
        ("NOTES-MIB", "lnSignalServerName"))
)
if mibBuilder.loadTexts:
    lnTrapDisplayAlarmClearServers.setStatus(
        ""
    )

lnTrapDisplayClearedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 70)
)
lnTrapDisplayClearedAlarm.setObjects(
      *(("NOTES-MIB", "lnAlarmSeverityStr"),
        ("NOTES-MIB", "lnAlarmTypeStr"),
        ("NOTES-MIB", "lnAlarmMessage"),
        ("NOTES-MIB", "lnAlarmMessageExt"))
)
if mibBuilder.loadTexts:
    lnTrapDisplayClearedAlarm.setStatus(
        ""
    )

lnTrapDisplayIndeterminateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 71)
)
lnTrapDisplayIndeterminateAlarm.setObjects(
      *(("NOTES-MIB", "lnAlarmSeverityStr"),
        ("NOTES-MIB", "lnAlarmTypeStr"),
        ("NOTES-MIB", "lnAlarmMessage"),
        ("NOTES-MIB", "lnAlarmMessageExt"))
)
if mibBuilder.loadTexts:
    lnTrapDisplayIndeterminateAlarm.setStatus(
        ""
    )

lnTrapDisplayWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 72)
)
lnTrapDisplayWarningAlarm.setObjects(
      *(("NOTES-MIB", "lnAlarmSeverityStr"),
        ("NOTES-MIB", "lnAlarmTypeStr"),
        ("NOTES-MIB", "lnAlarmMessage"),
        ("NOTES-MIB", "lnAlarmMessageExt"))
)
if mibBuilder.loadTexts:
    lnTrapDisplayWarningAlarm.setStatus(
        ""
    )

lnTrapDisplayMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 73)
)
lnTrapDisplayMinorAlarm.setObjects(
      *(("NOTES-MIB", "lnAlarmSeverityStr"),
        ("NOTES-MIB", "lnAlarmTypeStr"),
        ("NOTES-MIB", "lnAlarmMessage"),
        ("NOTES-MIB", "lnAlarmMessageExt"))
)
if mibBuilder.loadTexts:
    lnTrapDisplayMinorAlarm.setStatus(
        ""
    )

lnTrapDisplayCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 74)
)
lnTrapDisplayCriticalAlarm.setObjects(
      *(("NOTES-MIB", "lnAlarmSeverityStr"),
        ("NOTES-MIB", "lnAlarmTypeStr"),
        ("NOTES-MIB", "lnAlarmMessage"),
        ("NOTES-MIB", "lnAlarmMessageExt"))
)
if mibBuilder.loadTexts:
    lnTrapDisplayCriticalAlarm.setStatus(
        ""
    )

lnTrapDisplayMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 72, 0, 75)
)
lnTrapDisplayMajorAlarm.setObjects(
      *(("NOTES-MIB", "lnAlarmSeverityStr"),
        ("NOTES-MIB", "lnAlarmTypeStr"),
        ("NOTES-MIB", "lnAlarmMessage"),
        ("NOTES-MIB", "lnAlarmMessageExt"))
)
if mibBuilder.loadTexts:
    lnTrapDisplayMajorAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOTES-MIB",
    **{"lotus": lotus,
       "notes": notes,
       "lnUnknownEventTrap": lnUnknownEventTrap,
       "lnFatalEventTrap": lnFatalEventTrap,
       "lnFailureEventTrap": lnFailureEventTrap,
       "lnWarning1EventTrap": lnWarning1EventTrap,
       "lnWarning2EventTrap": lnWarning2EventTrap,
       "lnNormalEventTrap": lnNormalEventTrap,
       "lnServerUpTrap": lnServerUpTrap,
       "lnServerDownTrap": lnServerDownTrap,
       "lnServerPulseFailedTrap": lnServerPulseFailedTrap,
       "lnServerPulseRestoredTrap": lnServerPulseRestoredTrap,
       "lnSystemRebootingTrap": lnSystemRebootingTrap,
       "lnServerNotRespondingTrap": lnServerNotRespondingTrap,
       "lnServerNowRespondingTrap": lnServerNowRespondingTrap,
       "lnAlarmStatisticThreshold": lnAlarmStatisticThreshold,
       "lnAlarmServerStatusChange": lnAlarmServerStatusChange,
       "lnAlarmPortStatusChange": lnAlarmPortStatusChange,
       "lnAlarmTaskStatusChange": lnAlarmTaskStatusChange,
       "lnAlarmNVStatClear": lnAlarmNVStatClear,
       "lnAlarmAutoDiscovery": lnAlarmAutoDiscovery,
       "lnAlarmServerNotesEvent": lnAlarmServerNotesEvent,
       "lnAlarmServerCfgChangeEvent": lnAlarmServerCfgChangeEvent,
       "lnAlarmMailProbeEvent": lnAlarmMailProbeEvent,
       "lnAlarmServerSNMPEvent": lnAlarmServerSNMPEvent,
       "lnAlarmNSFRemoteConsoleEvent": lnAlarmNSFRemoteConsoleEvent,
       "lnAlarmMailBoxEvent": lnAlarmMailBoxEvent,
       "lnAlarmClearAll": lnAlarmClearAll,
       "lnAlarmClearServers": lnAlarmClearServers,
       "lnSignalAutodiscoveryStart": lnSignalAutodiscoveryStart,
       "lnSignalAutodiscoveryFinished": lnSignalAutodiscoveryFinished,
       "lnSignalServerConfigChg": lnSignalServerConfigChg,
       "lnTrapRequestMostSevereStatus": lnTrapRequestMostSevereStatus,
       "lnTrapDisplayAlarmClearServers": lnTrapDisplayAlarmClearServers,
       "lnTrapDisplayClearedAlarm": lnTrapDisplayClearedAlarm,
       "lnTrapDisplayIndeterminateAlarm": lnTrapDisplayIndeterminateAlarm,
       "lnTrapDisplayWarningAlarm": lnTrapDisplayWarningAlarm,
       "lnTrapDisplayMinorAlarm": lnTrapDisplayMinorAlarm,
       "lnTrapDisplayCriticalAlarm": lnTrapDisplayCriticalAlarm,
       "lnTrapDisplayMajorAlarm": lnTrapDisplayMajorAlarm,
       "lnInfo": lnInfo,
       "lnStats": lnStats,
       "lnAllStatsTable": lnAllStatsTable,
       "lnAllStatsEntry": lnAllStatsEntry,
       "lnStatisticIndex": lnStatisticIndex,
       "lnStatisticString": lnStatisticString,
       "lnStatsStartTime": lnStatsStartTime,
       "lnStatsCurrentTime": lnStatsCurrentTime,
       "lnMail": lnMail,
       "lnDeadMail": lnDeadMail,
       "lnDeliveredMail": lnDeliveredMail,
       "lnTotalMailFailures": lnTotalMailFailures,
       "lnTotalRoutedMail": lnTotalRoutedMail,
       "lnTransferredMail": lnTransferredMail,
       "lnWaitingMail": lnWaitingMail,
       "lnNumWaitingRecipients": lnNumWaitingRecipients,
       "lnMailDomain": lnMailDomain,
       "lnAverageMailDeliverTime": lnAverageMailDeliverTime,
       "lnAverageMailServerHops": lnAverageMailServerHops,
       "lnAverageMailSizeDelivered": lnAverageMailSizeDelivered,
       "lnMaximumMailDeliverTime": lnMaximumMailDeliverTime,
       "lnMaximumMailServerHops": lnMaximumMailServerHops,
       "lnMaximumMailSizeDelivered": lnMaximumMailSizeDelivered,
       "lnMinimumMailDeliverTime": lnMinimumMailDeliverTime,
       "lnMinimumMailServerHops": lnMinimumMailServerHops,
       "lnMinimumMailSizeDelivered": lnMinimumMailSizeDelivered,
       "lnTotalKBTransferred": lnTotalKBTransferred,
       "lnMailTransferFailures": lnMailTransferFailures,
       "lnReplica": lnReplica,
       "lnRepDocsAdded": lnRepDocsAdded,
       "lnRepDocsDeleted": lnRepDocsDeleted,
       "lnRepDocsUpdated": lnRepDocsUpdated,
       "lnRepFailed": lnRepFailed,
       "lnRepSuccessful": lnRepSuccessful,
       "lnReplicaCluster": lnReplicaCluster,
       "lnRepClusterDocsAdded": lnRepClusterDocsAdded,
       "lnRepClusterDocsDeleted": lnRepClusterDocsDeleted,
       "lnRepClusterDocsUpdated": lnRepClusterDocsUpdated,
       "lnRepClusterFailed": lnRepClusterFailed,
       "lnRepClusterFilesLocal": lnRepClusterFilesLocal,
       "lnRepClusterFilesRemote": lnRepClusterFilesRemote,
       "lnRepClusterRetrySkipped": lnRepClusterRetrySkipped,
       "lnRepClusterRetryWaiting": lnRepClusterRetryWaiting,
       "lnRepClusterSecondsOnQueue": lnRepClusterSecondsOnQueue,
       "lnRepClusterSecondsOnQueueAvg": lnRepClusterSecondsOnQueueAvg,
       "lnRepClusterSecondsOnQueueMax": lnRepClusterSecondsOnQueueMax,
       "lnRepClusterServers": lnRepClusterServers,
       "lnRepClusterSessionBytesIn": lnRepClusterSessionBytesIn,
       "lnRepClusterSessionBytesOut": lnRepClusterSessionBytesOut,
       "lnRepClusterSuccessful": lnRepClusterSuccessful,
       "lnRepClusterWorkQueueDepth": lnRepClusterWorkQueueDepth,
       "lnRepClusterWorkQueueDepthAvg": lnRepClusterWorkQueueDepthAvg,
       "lnRepClusterWorkQueueDepthMax": lnRepClusterWorkQueueDepthMax,
       "lnServer": lnServer,
       "lnServerTask": lnServerTask,
       "lnTaskCount": lnTaskCount,
       "lnTaskTable": lnTaskTable,
       "lnTaskEntry": lnTaskEntry,
       "lnTaskIndex": lnTaskIndex,
       "lnTaskType": lnTaskType,
       "lnTaskData": lnTaskData,
       "lnTaskName": lnTaskName,
       "lnReplicatorStatus": lnReplicatorStatus,
       "lnRouterStatus": lnRouterStatus,
       "lnEventStatus": lnEventStatus,
       "lnServerInfo": lnServerInfo,
       "lnServerName": lnServerName,
       "lnServerTitle": lnServerTitle,
       "lnServerAdministrators": lnServerAdministrators,
       "lnServerNotesVersion": lnServerNotesVersion,
       "lnServerSystemVersion": lnServerSystemVersion,
       "lnServerBootID": lnServerBootID,
       "lnServerDataPath": lnServerDataPath,
       "lnServerSwapPath": lnServerSwapPath,
       "lnServerRS232Ports": lnServerRS232Ports,
       "lnServerCoprocessor": lnServerCoprocessor,
       "lnServerOS": lnServerOS,
       "lnServerCPUCount": lnServerCPUCount,
       "lnServerCPUType": lnServerCPUType,
       "lnServerUsersTable": lnServerUsersTable,
       "lnServerUsersEntry": lnServerUsersEntry,
       "lnServerUsersIndex": lnServerUsersIndex,
       "lnServerUserName": lnServerUserName,
       "lnServerUserSessionID": lnServerUserSessionID,
       "lnServerUserAccessedDBs": lnServerUserAccessedDBs,
       "lnServerPorts": lnServerPorts,
       "lnServerPoweredBy": lnServerPoweredBy,
       "lnServerStats": lnServerStats,
       "lnServerDroppedSessions": lnServerDroppedSessions,
       "lnServerTransPerMin": lnServerTransPerMin,
       "lnServerTransPerMinPeak": lnServerTransPerMinPeak,
       "lnServerTransPerMinPeakTime": lnServerTransPerMinPeakTime,
       "lnServerTransTotal": lnServerTransTotal,
       "lnServerUsers": lnServerUsers,
       "lnServerUsers1MinPeak": lnServerUsers1MinPeak,
       "lnServerUsers1MinPeakTime": lnServerUsers1MinPeakTime,
       "lnServerUsers5MinPeak": lnServerUsers5MinPeak,
       "lnServerUsers5MinPeakTime": lnServerUsers5MinPeakTime,
       "lnServerUsersPeak": lnServerUsersPeak,
       "lnServerUsersPeakTime": lnServerUsersPeakTime,
       "lnServerOpenReqMaxUsers": lnServerOpenReqMaxUsers,
       "lnServerOpenReqPreV4Client": lnServerOpenReqPreV4Client,
       "lnServerOpenReqRestricted": lnServerOpenReqRestricted,
       "lnServerOpenReqV4Client": lnServerOpenReqV4Client,
       "lnServerBusyTimeQueryReceivedCount": lnServerBusyTimeQueryReceivedCount,
       "lnServerBusyTimeQueryRetObjSched": lnServerBusyTimeQueryRetObjSched,
       "lnCluster": lnCluster,
       "lnClusterName": lnClusterName,
       "lnClusterAvailIndex": lnClusterAvailIndex,
       "lnClusterAvailThreshold": lnClusterAvailThreshold,
       "lnClusterPortName": lnClusterPortName,
       "lnClusterProbeCount": lnClusterProbeCount,
       "lnClusterProbeTimeout": lnClusterProbeTimeout,
       "lnClusterTable": lnClusterTable,
       "lnClusterEntry": lnClusterEntry,
       "lnClusterTableIndex": lnClusterTableIndex,
       "lnClusterMemberName": lnClusterMemberName,
       "lnClusterMemberIndex": lnClusterMemberIndex,
       "lnOpenRedirects": lnOpenRedirects,
       "lnClusterFailoverByPathSucc": lnClusterFailoverByPathSucc,
       "lnClusterFailoverByPathUnsucc": lnClusterFailoverByPathUnsucc,
       "lnClusterFailoverSucc": lnClusterFailoverSucc,
       "lnClusterFailoverUnsucc": lnClusterFailoverUnsucc,
       "lnClusterLoadBalByPathSucc": lnClusterLoadBalByPathSucc,
       "lnClusterLoadBalByPathUnsucc": lnClusterLoadBalByPathUnsucc,
       "lnClusterLoadBalSucc": lnClusterLoadBalSucc,
       "lnClusterLoadBalUnsucc": lnClusterLoadBalUnsucc,
       "lnOpenRequest": lnOpenRequest,
       "lnClusterOpenReqClustBusy": lnClusterOpenReqClustBusy,
       "lnClusterOpenReqDBOutofServ": lnClusterOpenReqDBOutofServ,
       "lnClusterOpenReqLoadBalanced": lnClusterOpenReqLoadBalanced,
       "lnClusterTrans": lnClusterTrans,
       "lnClusterTransIntAvgTime": lnClusterTransIntAvgTime,
       "lnClusterTransIntInSec": lnClusterTransIntInSec,
       "lnClusterTransIntUsedInAvg": lnClusterTransIntUsedInAvg,
       "lnClusterTransLastIntAvgTime": lnClusterTransLastIntAvgTime,
       "lnClusterTransNormValue": lnClusterTransNormValue,
       "lnClusterProbeError": lnClusterProbeError,
       "lnComm": lnComm,
       "lnNumClosedOldSessions": lnNumClosedOldSessions,
       "lnNetbiosTable": lnNetbiosTable,
       "lnNetbiosEntry": lnNetbiosEntry,
       "lnNBIndex": lnNBIndex,
       "lnNBPort": lnNBPort,
       "lnNBUnitNumber": lnNBUnitNumber,
       "lnNBMajVersion": lnNBMajVersion,
       "lnNMMinVersion": lnNMMinVersion,
       "lnNBReportPeriod": lnNBReportPeriod,
       "lnNBInUseSessions": lnNBInUseSessions,
       "lnNBMaxSessions": lnNBMaxSessions,
       "lnNBAvailCmdBlocks": lnNBAvailCmdBlocks,
       "lnNBTotalCmdBlocks": lnNBTotalCmdBlocks,
       "lnNBPacketSize": lnNBPacketSize,
       "lnNBReceivedPackets": lnNBReceivedPackets,
       "lnNBSentPackets": lnNBSentPackets,
       "lnNBAbortedTransmissions": lnNBAbortedTransmissions,
       "lnNBRetriedTransmissions": lnNBRetriedTransmissions,
       "lnNBAlignmentErrors": lnNBAlignmentErrors,
       "lnNBCollisionErrors": lnNBCollisionErrors,
       "lnNBCRCErrors": lnNBCRCErrors,
       "lnXPCTable": lnXPCTable,
       "lnXPCEntry": lnXPCEntry,
       "lnXPCIndex": lnXPCIndex,
       "lnXPCPort": lnXPCPort,
       "lnXPCStatus": lnXPCStatus,
       "lnXPCCarrierSpeed": lnXPCCarrierSpeed,
       "lnXPCPortSpeed": lnXPCPortSpeed,
       "lnXPCActiveSessions": lnXPCActiveSessions,
       "lnXPCKiloBytesReceived": lnXPCKiloBytesReceived,
       "lnXPCKiloBytesSent": lnXPCKiloBytesSent,
       "lnXPCMsgsReceived": lnXPCMsgsReceived,
       "lnXPCMsgsSent": lnXPCMsgsSent,
       "lnXPCCRCErrors": lnXPCCRCErrors,
       "lnXPCPortErrors": lnXPCPortErrors,
       "lnXPCRetransmissions": lnXPCRetransmissions,
       "lnAppleTalkStatsLogged": lnAppleTalkStatsLogged,
       "lnNetWareSPXIIStatsLogged": lnNetWareSPXIIStatsLogged,
       "lnNetPortTable": lnNetPortTable,
       "lnNetPortEntry": lnNetPortEntry,
       "lnNetPortIndex": lnNetPortIndex,
       "lnNetPortName": lnNetPortName,
       "lnNetPortKBytesRec": lnNetPortKBytesRec,
       "lnNetPortKBytesSent": lnNetPortKBytesSent,
       "lnNetPortSessEstIn": lnNetPortSessEstIn,
       "lnNetPortSessEstOut": lnNetPortSessEstOut,
       "lnNetPortSessLimit": lnNetPortSessLimit,
       "lnNetPortSessLimitMax": lnNetPortSessLimitMax,
       "lnNetPortSessLimitMin": lnNetPortSessLimitMin,
       "lnNetPortSessPeak": lnNetPortSessPeak,
       "lnNetPortSessRecycled": lnNetPortSessRecycled,
       "lnNetPortSessRecycling": lnNetPortSessRecycling,
       "lnSNARemoteLU": lnSNARemoteLU,
       "lnSNALocalLU": lnSNALocalLU,
       "lnSNALNCVersion": lnSNALNCVersion,
       "lnSNAVersion": lnSNAVersion,
       "lnSNAMaxSessions": lnSNAMaxSessions,
       "lnSNAActiveSessions": lnSNAActiveSessions,
       "lnSNATPType": lnSNATPType,
       "lnSNATPState": lnSNATPState,
       "lnSNAConversationId": lnSNAConversationId,
       "lnSNAMaxSendRUSize": lnSNAMaxSendRUSize,
       "lnSNAMaxRcvRUSize": lnSNAMaxRcvRUSize,
       "lnSNASendPacingSize": lnSNASendPacingSize,
       "lnSNARcvPacingSize": lnSNARcvPacingSize,
       "lnSNAPacingType": lnSNAPacingType,
       "lnX25LocalResets": lnX25LocalResets,
       "lnX25RemoteResets": lnX25RemoteResets,
       "lnX25WindowSize": lnX25WindowSize,
       "lnX25FrameSize": lnX25FrameSize,
       "lnX25PktSize": lnX25PktSize,
       "lnX25UnderRuns": lnX25UnderRuns,
       "lnX25OverRuns": lnX25OverRuns,
       "lnX25REJTran": lnX25REJTran,
       "lnX25REJRcv": lnX25REJRcv,
       "lnX25VCCfg": lnX25VCCfg,
       "lnX25VCInUse": lnX25VCInUse,
       "lnX25CRCErrors": lnX25CRCErrors,
       "lnX25LocalDTEAddress": lnX25LocalDTEAddress,
       "lnDisk": lnDisk,
       "lnDiskFixed": lnDiskFixed,
       "lnDiskFreeSwap": lnDiskFreeSwap,
       "lnDriveTable": lnDriveTable,
       "lnDriveEntry": lnDriveEntry,
       "lnDriveIndex": lnDriveIndex,
       "lnDriveLetter": lnDriveLetter,
       "lnDriveSize": lnDriveSize,
       "lnDriveFree": lnDriveFree,
       "lnDiskRemote": lnDiskRemote,
       "lnMem": lnMem,
       "lnMemAllocTotal": lnMemAllocTotal,
       "lnMemAllocProcess": lnMemAllocProcess,
       "lnMemAllocShared": lnMemAllocShared,
       "lnMemAvailability": lnMemAvailability,
       "lnMemFree": lnMemFree,
       "lnMemSwapSize": lnMemSwapSize,
       "lnMemPhysicalRAM": lnMemPhysicalRAM,
       "lnDatabase": lnDatabase,
       "lnDBBufferControlPoolSize": lnDBBufferControlPoolSize,
       "lnDBBufferControlPoolUsed": lnDBBufferControlPoolUsed,
       "lnDBBufferPoolAllocated": lnDBBufferPoolAllocated,
       "lnDBBufferPoolMaximum": lnDBBufferPoolMaximum,
       "lnDBBufferPoolUsed": lnDBBufferPoolUsed,
       "lnDBNSFPoolSize": lnDBNSFPoolSize,
       "lnDBNSFPoolUsed": lnDBNSFPoolUsed,
       "lnDBBufferPoolPercentReadsInBuffer": lnDBBufferPoolPercentReadsInBuffer,
       "lnDBBufferPoolReads": lnDBBufferPoolReads,
       "lnDBBufferPoolWrites": lnDBBufferPoolWrites,
       "lnDBNIFPoolSize": lnDBNIFPoolSize,
       "lnDBNIFPoolUsed": lnDBNIFPoolUsed,
       "lnDBNIFPoolPeak": lnDBNIFPoolPeak,
       "lnDBNSFPoolPeak": lnDBNSFPoolPeak,
       "lnDBCacheCurrentEntries": lnDBCacheCurrentEntries,
       "lnDBCacheHighWaterMark": lnDBCacheHighWaterMark,
       "lnDBCacheHits": lnDBCacheHits,
       "lnDBCacheInitialDbOpens": lnDBCacheInitialDbOpens,
       "lnDBCacheLookups": lnDBCacheLookups,
       "lnDBCacheMaxEntries": lnDBCacheMaxEntries,
       "lnDBCacheOvercrowdingRejections": lnDBCacheOvercrowdingRejections,
       "lnDBBufferControlPoolPeak": lnDBBufferControlPoolPeak,
       "lnAgentMgr": lnAgentMgr,
       "lnDailyAccessDenials": lnDailyAccessDenials,
       "lnDailyScheduledRuns": lnDailyScheduledRuns,
       "lnDailyTriggeredRuns": lnDailyTriggeredRuns,
       "lnDailyUnsuccessfulRuns": lnDailyUnsuccessfulRuns,
       "lnDailyUsedRunTime": lnDailyUsedRunTime,
       "lnHourlyAccessDenials": lnHourlyAccessDenials,
       "lnHourlyScheduledRuns": lnHourlyScheduledRuns,
       "lnHourlyTriggeredRuns": lnHourlyTriggeredRuns,
       "lnHourlyUnsuccessfulRuns": lnHourlyUnsuccessfulRuns,
       "lnHourlyUsedRunTime": lnHourlyUsedRunTime,
       "lnMTA": lnMTA,
       "lnMTATable": lnMTATable,
       "lnMTAEntry": lnMTAEntry,
       "lnMTAIndex": lnMTAIndex,
       "lnMTAName": lnMTAName,
       "lnMTADeadMsgs": lnMTADeadMsgs,
       "lnMTAWaitingRecp": lnMTAWaitingRecp,
       "lnMTAWaitingMsgs": lnMTAWaitingMsgs,
       "lnMTATransferFailures": lnMTATransferFailures,
       "lnMTATotalKBTransferred": lnMTATotalKBTransferred,
       "lnMTATransferredMsgs": lnMTATransferredMsgs,
       "lnMTATotalRouted": lnMTATotalRouted,
       "lnWeb": lnWeb,
       "lnWebAccessFtp": lnWebAccessFtp,
       "lnWebAccessGopher": lnWebAccessGopher,
       "lnWebAccessHttp": lnWebAccessHttp,
       "lnWebKBytesReceived": lnWebKBytesReceived,
       "lnWebKBytesSent": lnWebKBytesSent,
       "lnWebImageCacheHits": lnWebImageCacheHits,
       "lnWebImageCacheMisses": lnWebImageCacheMisses,
       "lnWebLogMessages": lnWebLogMessages,
       "lnWebActiveProcesses": lnWebActiveProcesses,
       "lnWebBusyProcesses": lnWebBusyProcesses,
       "lnWebIdleProcesses": lnWebIdleProcesses,
       "lnWebMaxProcesses": lnWebMaxProcesses,
       "lnWebProcessState": lnWebProcessState,
       "lnWebTimeCurrent": lnWebTimeCurrent,
       "lnWebTimeDuration": lnWebTimeDuration,
       "lnWebTimeStart": lnWebTimeStart,
       "lnWebUrlFail": lnWebUrlFail,
       "lnWebUrlRequested": lnWebUrlRequested,
       "lnWebUrlSucceeded": lnWebUrlSucceeded,
       "lnWebRetrieverVersion": lnWebRetrieverVersion,
       "lnWebVpoolMaxBuf": lnWebVpoolMaxBuf,
       "lnWebVpoolMaxElement": lnWebVpoolMaxElement,
       "lnWebVpoolMaxMarker": lnWebVpoolMaxMarker,
       "lnWebVpoolMaxText": lnWebVpoolMaxText,
       "lnWebVpoolMaxUrl": lnWebVpoolMaxUrl,
       "lnWebProcessTable": lnWebProcessTable,
       "lnWebProcEntry": lnWebProcEntry,
       "lnWebProcIndex": lnWebProcIndex,
       "lnWebProcNumber": lnWebProcNumber,
       "lnWebProcAccFtp": lnWebProcAccFtp,
       "lnWebProcAccGopher": lnWebProcAccGopher,
       "lnWebProcAccHttp": lnWebProcAccHttp,
       "lnWebProcKBytesRec": lnWebProcKBytesRec,
       "lnWebProcKBytesSent": lnWebProcKBytesSent,
       "lnWebProcCacheHits": lnWebProcCacheHits,
       "lnWebProcCacheMisses": lnWebProcCacheMisses,
       "lnWebProcPid": lnWebProcPid,
       "lnWebProcUrlFail": lnWebProcUrlFail,
       "lnWebProcUrlReq": lnWebProcUrlReq,
       "lnWebProcUrlSucc": lnWebProcUrlSucc,
       "lnWebProcVpoolCurBuf": lnWebProcVpoolCurBuf,
       "lnWebProcVpoolCurElement": lnWebProcVpoolCurElement,
       "lnWebProcVpoolCurMarker": lnWebProcVpoolCurMarker,
       "lnWebProcVpoolCurText": lnWebProcVpoolCurText,
       "lnWebProcVpoolCurUrl": lnWebProcVpoolCurUrl,
       "lnWebProcVpoolMaxBuf": lnWebProcVpoolMaxBuf,
       "lnWebProcVpoolMaxElement": lnWebProcVpoolMaxElement,
       "lnWebProcVpoolMaxMarker": lnWebProcVpoolMaxMarker,
       "lnWebProcVpoolMaxText": lnWebProcVpoolMaxText,
       "lnWebProcVpoolMaxUrl": lnWebProcVpoolMaxUrl,
       "lnObject": lnObject,
       "lnObjectFileName": lnObjectFileName,
       "lnObjectTable": lnObjectTable,
       "lnObjectEntry": lnObjectEntry,
       "lnObjectIndex": lnObjectIndex,
       "lnObjectName": lnObjectName,
       "lnObjectSharedBy01": lnObjectSharedBy01,
       "lnObjectSharedBy02": lnObjectSharedBy02,
       "lnObjectSharedBy03": lnObjectSharedBy03,
       "lnObjectSharedBy04": lnObjectSharedBy04,
       "lnObjectSharedBy05": lnObjectSharedBy05,
       "lnObjectSharedBy06": lnObjectSharedBy06,
       "lnObjectSharedBy07": lnObjectSharedBy07,
       "lnObjectSharedBy08": lnObjectSharedBy08,
       "lnObjectSharedBy09": lnObjectSharedBy09,
       "lnObjectSharedBy10": lnObjectSharedBy10,
       "lnObjectSharedBy11": lnObjectSharedBy11,
       "lnObjectSharedBy12": lnObjectSharedBy12,
       "lnObjectSharedBy13": lnObjectSharedBy13,
       "lnObjectSharedBy14": lnObjectSharedBy14,
       "lnObjectSharedBy15": lnObjectSharedBy15,
       "lnObjectSharedBy16": lnObjectSharedBy16,
       "lnObjectSharedBy17": lnObjectSharedBy17,
       "lnObjectSharedBy18": lnObjectSharedBy18,
       "lnObjectSharedBy19": lnObjectSharedBy19,
       "lnObjectSharedBy20": lnObjectSharedBy20,
       "lnObjectSharedByGreater": lnObjectSharedByGreater,
       "lnObjectSharedByTotal": lnObjectSharedByTotal,
       "lnDomino": lnDomino,
       "lnDominoInfo": lnDominoInfo,
       "lnDominoBuildName": lnDominoBuildName,
       "lnDominoBuildNumber": lnDominoBuildNumber,
       "lnDominoBuildPlatform": lnDominoBuildPlatform,
       "lnDominoBuildVersion": lnDominoBuildVersion,
       "lnDominoThreadsActivePeak": lnDominoThreadsActivePeak,
       "lnDominoThreadsTotal": lnDominoThreadsTotal,
       "lnDominoThreadsPeakTotal": lnDominoThreadsPeakTotal,
       "lnDominoThreadsPeakTime": lnDominoThreadsPeakTime,
       "lnDominoStartTime": lnDominoStartTime,
       "lnDominoReqPerMinTotal": lnDominoReqPerMinTotal,
       "lnDominoReqPerMinPeak": lnDominoReqPerMinPeak,
       "lnDominoReqPerMinPeakTime": lnDominoReqPerMinPeakTime,
       "lnDominoReqPer5MinsTotal": lnDominoReqPer5MinsTotal,
       "lnDominoReqPer5MinsPeak": lnDominoReqPer5MinsPeak,
       "lnDominoReqPer5MinsPeakTime": lnDominoReqPer5MinsPeakTime,
       "lnDominoReqPerHourTotal": lnDominoReqPerHourTotal,
       "lnDominoReqPerHourPeak": lnDominoReqPerHourPeak,
       "lnDominoReqPerHourPeakTime": lnDominoReqPerHourPeakTime,
       "lnDominoReqPerDayTotal": lnDominoReqPerDayTotal,
       "lnDominoReqPerDayPeak": lnDominoReqPerDayPeak,
       "lnDominoReqPerDayPeakTime": lnDominoReqPerDayPeakTime,
       "lnDominoRequestsTotal": lnDominoRequestsTotal,
       "lnDominoCacheCommandDisplaceRate": lnDominoCacheCommandDisplaceRate,
       "lnDominoCacheCommandHitRate": lnDominoCacheCommandHitRate,
       "lnDominoCacheDatabaseDisplaceRate": lnDominoCacheDatabaseDisplaceRate,
       "lnDominoCacheDatabaseHitRate": lnDominoCacheDatabaseHitRate,
       "lnDominoCmdInfo": lnDominoCmdInfo,
       "lnDominoCmdInfoEditDocument": lnDominoCmdInfoEditDocument,
       "lnDominoCmdInfoOpenServer": lnDominoCmdInfoOpenServer,
       "lnDominoCmdInfoOpenDatabase": lnDominoCmdInfoOpenDatabase,
       "lnDominoCmdInfoOpenView": lnDominoCmdInfoOpenView,
       "lnDominoCmdInfoOpenDocument": lnDominoCmdInfoOpenDocument,
       "lnDominoCmdInfoOpenElement": lnDominoCmdInfoOpenElement,
       "lnDominoCmdInfoOpenIcon": lnDominoCmdInfoOpenIcon,
       "lnDominoCmdInfoOpenForm": lnDominoCmdInfoOpenForm,
       "lnDominoCmdInfoOpenAgent": lnDominoCmdInfoOpenAgent,
       "lnDominoCmdInfoOpenNavigator": lnDominoCmdInfoOpenNavigator,
       "lnDominoCmdInfoOpenAbout": lnDominoCmdInfoOpenAbout,
       "lnDominoCmdInfoOpenHelp": lnDominoCmdInfoOpenHelp,
       "lnDominoCmdInfoCreateDocument": lnDominoCmdInfoCreateDocument,
       "lnDominoCmdInfoSaveDocument": lnDominoCmdInfoSaveDocument,
       "lnDominoCmdInfoDeleteDocument": lnDominoCmdInfoDeleteDocument,
       "lnDominoCmdInfoSearchSite": lnDominoCmdInfoSearchSite,
       "lnDominoCmdInfoSearchView": lnDominoCmdInfoSearchView,
       "lnDominoCmdInfoUnknown": lnDominoCmdInfoUnknown,
       "lnDominoCmdInfoLogin": lnDominoCmdInfoLogin,
       "lnDominoCmdInfoNavigate": lnDominoCmdInfoNavigate,
       "lnDominoCmdInfoReadForm": lnDominoCmdInfoReadForm,
       "lnDominoCmdInfoTotal": lnDominoCmdInfoTotal,
       "lnDominoConfig": lnDominoConfig,
       "lnDominoCfgPortNumber": lnDominoCfgPortNumber,
       "lnDominoCfgPortStatus": lnDominoCfgPortStatus,
       "lnDominoCfgHostName": lnDominoCfgHostName,
       "lnDominoCfgDNSLookup": lnDominoCfgDNSLookup,
       "lnDominoCfgHomeURL": lnDominoCfgHomeURL,
       "lnDominoCfgWelcomePage": lnDominoCfgWelcomePage,
       "lnDominoCfgActiveThreadsMax": lnDominoCfgActiveThreadsMax,
       "lnDominoCfgActiveThreadsMin": lnDominoCfgActiveThreadsMin,
       "lnDominoCfgSSLPortNumber": lnDominoCfgSSLPortNumber,
       "lnDominoCfgSSLStatus": lnDominoCfgSSLStatus,
       "lnDominoCfgSSLKeyFile": lnDominoCfgSSLKeyFile,
       "lnDominoCfgCacheDirectory": lnDominoCfgCacheDirectory,
       "lnDominoCfgCacheSizeMax": lnDominoCfgCacheSizeMax,
       "lnDominoCfgCacheDelete": lnDominoCfgCacheDelete,
       "lnDominoCfgGarbageCollectionStatus": lnDominoCfgGarbageCollectionStatus,
       "lnDominoCfgGarbageCollectionInterval": lnDominoCfgGarbageCollectionInterval,
       "lnDominoCfgImageFormat": lnDominoCfgImageFormat,
       "lnDominoCfgImageInterlaced": lnDominoCfgImageInterlaced,
       "lnDominoCfgViewLines": lnDominoCfgViewLines,
       "lnDominoCfgDirectoryHTML": lnDominoCfgDirectoryHTML,
       "lnDominoCfgDirectoryURLPathCGI": lnDominoCfgDirectoryURLPathCGI,
       "lnDominoCfgDirectoryCGI": lnDominoCfgDirectoryCGI,
       "lnDominoCfgDirectoryURLPathIcons": lnDominoCfgDirectoryURLPathIcons,
       "lnDominoCfgDirectoryIcons": lnDominoCfgDirectoryIcons,
       "lnDominoCfgLogAccess": lnDominoCfgLogAccess,
       "lnDominoCfgLogError": lnDominoCfgLogError,
       "lnDominoCfgLogTimeStamp": lnDominoCfgLogTimeStamp,
       "lnDominoCfgLogFilter": lnDominoCfgLogFilter,
       "lnDominoCfgTimeoutIdleThread": lnDominoCfgTimeoutIdleThread,
       "lnDominoCfgTimeoutInput": lnDominoCfgTimeoutInput,
       "lnDominoCfgTimeoutOutput": lnDominoCfgTimeoutOutput,
       "lnDominoCfgTimeoutCGI": lnDominoCfgTimeoutCGI,
       "lnCalendar": lnCalendar,
       "lnCalTotalAllApptsResources": lnCalTotalAllApptsResources,
       "lnCalTotalAllUsersResources": lnCalTotalAllUsersResources,
       "lnCalTotalAppointments": lnCalTotalAppointments,
       "lnCalTotalReservations": lnCalTotalReservations,
       "lnCalTotalResources": lnCalTotalResources,
       "lnCalTotalUsers": lnCalTotalUsers,
       "lnCollector": lnCollector,
       "lnCollectorTimeCollected": lnCollectorTimeCollected,
       "lnCollectorTimeElapsed": lnCollectorTimeElapsed,
       "lnMIBVersion": lnMIBVersion,
       "lnQSBuildNumber": lnQSBuildNumber,
       "lnControl": lnControl,
       "lnNotesServerSetState": lnNotesServerSetState,
       "lnNotesServerState": lnNotesServerState,
       "lnLastTrapSeq": lnLastTrapSeq,
       "lnRecentTrapsTable": lnRecentTrapsTable,
       "lnRecentTrapsEntry": lnRecentTrapsEntry,
       "lnTrapSeq": lnTrapSeq,
       "lnTrapInfo": lnTrapInfo,
       "lnRemoteReboot": lnRemoteReboot,
       "lnServerTbl": lnServerTbl,
       "lnServerTblEntry": lnServerTblEntry,
       "lnServerTblIndex": lnServerTblIndex,
       "lnServerTblName": lnServerTblName,
       "lnServerTblNotesPartition": lnServerTblNotesPartition,
       "lnServerTblDataDir": lnServerTblDataDir,
       "lnServerTblDataDirValid": lnServerTblDataDirValid,
       "lnServerTblState": lnServerTblState,
       "lnServerIdentifiedItself": lnServerIdentifiedItself,
       "lnServerTblSetState": lnServerTblSetState,
       "lnTotalPartitions": lnTotalPartitions,
       "lnMPAIniFileLocation": lnMPAIniFileLocation,
       "lnInterceptor": lnInterceptor,
       "lnEvtServer": lnEvtServer,
       "lnEvtType": lnEvtType,
       "lnEvtSeverity": lnEvtSeverity,
       "lnEvtWhen": lnEvtWhen,
       "lnEvtData": lnEvtData,
       "lnEvtSeq": lnEvtSeq,
       "lnUnix": lnUnix,
       "lnAlarm": lnAlarm,
       "lnAlarmServerHandle": lnAlarmServerHandle,
       "lnAlarmTargetHandle": lnAlarmTargetHandle,
       "lnAlarmDate": lnAlarmDate,
       "lnAlarmTime": lnAlarmTime,
       "lnAlarmSeverity": lnAlarmSeverity,
       "lnAlarmIntArg": lnAlarmIntArg,
       "lnAlarmLongArg": lnAlarmLongArg,
       "lnAlarmDoubleArg": lnAlarmDoubleArg,
       "lnAlarmTextArg1": lnAlarmTextArg1,
       "lnAlarmTextArg2": lnAlarmTextArg2,
       "lnAlarmSeverityStr": lnAlarmSeverityStr,
       "lnAlarmTypeStr": lnAlarmTypeStr,
       "lnAlarmMessage": lnAlarmMessage,
       "lnAlarmMessageExt": lnAlarmMessageExt,
       "lnAlarmServerName": lnAlarmServerName,
       "lnSignal": lnSignal,
       "lnSignalServerId": lnSignalServerId,
       "lnSignalOldServerType": lnSignalOldServerType,
       "lnSignalNewServerType": lnSignalNewServerType,
       "lnSignalWhatHasChanged": lnSignalWhatHasChanged,
       "lnSignalServerName": lnSignalServerName,
       "mapInfo": mapInfo,
       "lnMainProxyAgentVersion": lnMainProxyAgentVersion,
       "notesPump": notesPump}
)

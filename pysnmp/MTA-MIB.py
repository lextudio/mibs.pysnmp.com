# SNMP MIB module (MTA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MTA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:16 2024
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

(URLString,
 applIndex) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "URLString",
    "applIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

mta = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 28)
)
mta.setRevisions(
        ("2000-03-03 00:00",
         "1999-05-12 00:00",
         "1997-08-17 00:00",
         "1993-11-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MtaTable_Object = MibTable
mtaTable = _MtaTable_Object(
    (1, 3, 6, 1, 2, 1, 28, 1)
)
if mibBuilder.loadTexts:
    mtaTable.setStatus("current")
_MtaEntry_Object = MibTableRow
mtaEntry = _MtaEntry_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1)
)
mtaEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    mtaEntry.setStatus("current")
_MtaReceivedMessages_Type = Counter32
_MtaReceivedMessages_Object = MibTableColumn
mtaReceivedMessages = _MtaReceivedMessages_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 1),
    _MtaReceivedMessages_Type()
)
mtaReceivedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaReceivedMessages.setStatus("current")
_MtaStoredMessages_Type = Gauge32
_MtaStoredMessages_Object = MibTableColumn
mtaStoredMessages = _MtaStoredMessages_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 2),
    _MtaStoredMessages_Type()
)
mtaStoredMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaStoredMessages.setStatus("current")
_MtaTransmittedMessages_Type = Counter32
_MtaTransmittedMessages_Object = MibTableColumn
mtaTransmittedMessages = _MtaTransmittedMessages_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 3),
    _MtaTransmittedMessages_Type()
)
mtaTransmittedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTransmittedMessages.setStatus("current")
_MtaReceivedVolume_Type = Counter32
_MtaReceivedVolume_Object = MibTableColumn
mtaReceivedVolume = _MtaReceivedVolume_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 4),
    _MtaReceivedVolume_Type()
)
mtaReceivedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaReceivedVolume.setStatus("current")
if mibBuilder.loadTexts:
    mtaReceivedVolume.setUnits("K-octets")
_MtaStoredVolume_Type = Gauge32
_MtaStoredVolume_Object = MibTableColumn
mtaStoredVolume = _MtaStoredVolume_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 5),
    _MtaStoredVolume_Type()
)
mtaStoredVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaStoredVolume.setStatus("current")
if mibBuilder.loadTexts:
    mtaStoredVolume.setUnits("K-octets")
_MtaTransmittedVolume_Type = Counter32
_MtaTransmittedVolume_Object = MibTableColumn
mtaTransmittedVolume = _MtaTransmittedVolume_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 6),
    _MtaTransmittedVolume_Type()
)
mtaTransmittedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTransmittedVolume.setStatus("current")
if mibBuilder.loadTexts:
    mtaTransmittedVolume.setUnits("K-octets")
_MtaReceivedRecipients_Type = Counter32
_MtaReceivedRecipients_Object = MibTableColumn
mtaReceivedRecipients = _MtaReceivedRecipients_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 7),
    _MtaReceivedRecipients_Type()
)
mtaReceivedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaReceivedRecipients.setStatus("current")
_MtaStoredRecipients_Type = Gauge32
_MtaStoredRecipients_Object = MibTableColumn
mtaStoredRecipients = _MtaStoredRecipients_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 8),
    _MtaStoredRecipients_Type()
)
mtaStoredRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaStoredRecipients.setStatus("current")
_MtaTransmittedRecipients_Type = Counter32
_MtaTransmittedRecipients_Object = MibTableColumn
mtaTransmittedRecipients = _MtaTransmittedRecipients_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 9),
    _MtaTransmittedRecipients_Type()
)
mtaTransmittedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTransmittedRecipients.setStatus("current")
_MtaSuccessfulConvertedMessages_Type = Counter32
_MtaSuccessfulConvertedMessages_Object = MibTableColumn
mtaSuccessfulConvertedMessages = _MtaSuccessfulConvertedMessages_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 10),
    _MtaSuccessfulConvertedMessages_Type()
)
mtaSuccessfulConvertedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaSuccessfulConvertedMessages.setStatus("current")
_MtaFailedConvertedMessages_Type = Counter32
_MtaFailedConvertedMessages_Object = MibTableColumn
mtaFailedConvertedMessages = _MtaFailedConvertedMessages_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 11),
    _MtaFailedConvertedMessages_Type()
)
mtaFailedConvertedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaFailedConvertedMessages.setStatus("current")
_MtaLoopsDetected_Type = Counter32
_MtaLoopsDetected_Object = MibTableColumn
mtaLoopsDetected = _MtaLoopsDetected_Object(
    (1, 3, 6, 1, 2, 1, 28, 1, 1, 12),
    _MtaLoopsDetected_Type()
)
mtaLoopsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaLoopsDetected.setStatus("current")
_MtaGroupTable_Object = MibTable
mtaGroupTable = _MtaGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 28, 2)
)
if mibBuilder.loadTexts:
    mtaGroupTable.setStatus("current")
_MtaGroupEntry_Object = MibTableRow
mtaGroupEntry = _MtaGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1)
)
mtaGroupEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "MTA-MIB", "mtaGroupIndex"),
)
if mibBuilder.loadTexts:
    mtaGroupEntry.setStatus("current")


class _MtaGroupIndex_Type(Integer32):
    """Custom type mtaGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MtaGroupIndex_Type.__name__ = "Integer32"
_MtaGroupIndex_Object = MibTableColumn
mtaGroupIndex = _MtaGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 1),
    _MtaGroupIndex_Type()
)
mtaGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtaGroupIndex.setStatus("current")
_MtaGroupReceivedMessages_Type = Counter32
_MtaGroupReceivedMessages_Object = MibTableColumn
mtaGroupReceivedMessages = _MtaGroupReceivedMessages_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 2),
    _MtaGroupReceivedMessages_Type()
)
mtaGroupReceivedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupReceivedMessages.setStatus("current")
_MtaGroupRejectedMessages_Type = Counter32
_MtaGroupRejectedMessages_Object = MibTableColumn
mtaGroupRejectedMessages = _MtaGroupRejectedMessages_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 3),
    _MtaGroupRejectedMessages_Type()
)
mtaGroupRejectedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupRejectedMessages.setStatus("current")
_MtaGroupStoredMessages_Type = Gauge32
_MtaGroupStoredMessages_Object = MibTableColumn
mtaGroupStoredMessages = _MtaGroupStoredMessages_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 4),
    _MtaGroupStoredMessages_Type()
)
mtaGroupStoredMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupStoredMessages.setStatus("current")
_MtaGroupTransmittedMessages_Type = Counter32
_MtaGroupTransmittedMessages_Object = MibTableColumn
mtaGroupTransmittedMessages = _MtaGroupTransmittedMessages_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 5),
    _MtaGroupTransmittedMessages_Type()
)
mtaGroupTransmittedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupTransmittedMessages.setStatus("current")
_MtaGroupReceivedVolume_Type = Counter32
_MtaGroupReceivedVolume_Object = MibTableColumn
mtaGroupReceivedVolume = _MtaGroupReceivedVolume_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 6),
    _MtaGroupReceivedVolume_Type()
)
mtaGroupReceivedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupReceivedVolume.setStatus("current")
if mibBuilder.loadTexts:
    mtaGroupReceivedVolume.setUnits("K-octets")
_MtaGroupStoredVolume_Type = Gauge32
_MtaGroupStoredVolume_Object = MibTableColumn
mtaGroupStoredVolume = _MtaGroupStoredVolume_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 7),
    _MtaGroupStoredVolume_Type()
)
mtaGroupStoredVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupStoredVolume.setStatus("current")
if mibBuilder.loadTexts:
    mtaGroupStoredVolume.setUnits("K-octets")
_MtaGroupTransmittedVolume_Type = Counter32
_MtaGroupTransmittedVolume_Object = MibTableColumn
mtaGroupTransmittedVolume = _MtaGroupTransmittedVolume_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 8),
    _MtaGroupTransmittedVolume_Type()
)
mtaGroupTransmittedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupTransmittedVolume.setStatus("current")
if mibBuilder.loadTexts:
    mtaGroupTransmittedVolume.setUnits("K-octets")
_MtaGroupReceivedRecipients_Type = Counter32
_MtaGroupReceivedRecipients_Object = MibTableColumn
mtaGroupReceivedRecipients = _MtaGroupReceivedRecipients_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 9),
    _MtaGroupReceivedRecipients_Type()
)
mtaGroupReceivedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupReceivedRecipients.setStatus("current")
_MtaGroupStoredRecipients_Type = Gauge32
_MtaGroupStoredRecipients_Object = MibTableColumn
mtaGroupStoredRecipients = _MtaGroupStoredRecipients_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 10),
    _MtaGroupStoredRecipients_Type()
)
mtaGroupStoredRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupStoredRecipients.setStatus("current")
_MtaGroupTransmittedRecipients_Type = Counter32
_MtaGroupTransmittedRecipients_Object = MibTableColumn
mtaGroupTransmittedRecipients = _MtaGroupTransmittedRecipients_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 11),
    _MtaGroupTransmittedRecipients_Type()
)
mtaGroupTransmittedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupTransmittedRecipients.setStatus("current")
_MtaGroupOldestMessageStored_Type = TimeInterval
_MtaGroupOldestMessageStored_Object = MibTableColumn
mtaGroupOldestMessageStored = _MtaGroupOldestMessageStored_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 12),
    _MtaGroupOldestMessageStored_Type()
)
mtaGroupOldestMessageStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupOldestMessageStored.setStatus("current")
_MtaGroupInboundAssociations_Type = Gauge32
_MtaGroupInboundAssociations_Object = MibTableColumn
mtaGroupInboundAssociations = _MtaGroupInboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 13),
    _MtaGroupInboundAssociations_Type()
)
mtaGroupInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupInboundAssociations.setStatus("current")
_MtaGroupOutboundAssociations_Type = Gauge32
_MtaGroupOutboundAssociations_Object = MibTableColumn
mtaGroupOutboundAssociations = _MtaGroupOutboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 14),
    _MtaGroupOutboundAssociations_Type()
)
mtaGroupOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupOutboundAssociations.setStatus("current")
_MtaGroupAccumulatedInboundAssociations_Type = Counter32
_MtaGroupAccumulatedInboundAssociations_Object = MibTableColumn
mtaGroupAccumulatedInboundAssociations = _MtaGroupAccumulatedInboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 15),
    _MtaGroupAccumulatedInboundAssociations_Type()
)
mtaGroupAccumulatedInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupAccumulatedInboundAssociations.setStatus("current")
_MtaGroupAccumulatedOutboundAssociations_Type = Counter32
_MtaGroupAccumulatedOutboundAssociations_Object = MibTableColumn
mtaGroupAccumulatedOutboundAssociations = _MtaGroupAccumulatedOutboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 16),
    _MtaGroupAccumulatedOutboundAssociations_Type()
)
mtaGroupAccumulatedOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupAccumulatedOutboundAssociations.setStatus("current")
_MtaGroupLastInboundActivity_Type = TimeInterval
_MtaGroupLastInboundActivity_Object = MibTableColumn
mtaGroupLastInboundActivity = _MtaGroupLastInboundActivity_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 17),
    _MtaGroupLastInboundActivity_Type()
)
mtaGroupLastInboundActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupLastInboundActivity.setStatus("current")
_MtaGroupLastOutboundActivity_Type = TimeInterval
_MtaGroupLastOutboundActivity_Object = MibTableColumn
mtaGroupLastOutboundActivity = _MtaGroupLastOutboundActivity_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 18),
    _MtaGroupLastOutboundActivity_Type()
)
mtaGroupLastOutboundActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupLastOutboundActivity.setStatus("current")
_MtaGroupRejectedInboundAssociations_Type = Counter32
_MtaGroupRejectedInboundAssociations_Object = MibTableColumn
mtaGroupRejectedInboundAssociations = _MtaGroupRejectedInboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 19),
    _MtaGroupRejectedInboundAssociations_Type()
)
mtaGroupRejectedInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupRejectedInboundAssociations.setStatus("current")
_MtaGroupFailedOutboundAssociations_Type = Counter32
_MtaGroupFailedOutboundAssociations_Object = MibTableColumn
mtaGroupFailedOutboundAssociations = _MtaGroupFailedOutboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 20),
    _MtaGroupFailedOutboundAssociations_Type()
)
mtaGroupFailedOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupFailedOutboundAssociations.setStatus("current")
_MtaGroupInboundRejectionReason_Type = SnmpAdminString
_MtaGroupInboundRejectionReason_Object = MibTableColumn
mtaGroupInboundRejectionReason = _MtaGroupInboundRejectionReason_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 21),
    _MtaGroupInboundRejectionReason_Type()
)
mtaGroupInboundRejectionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupInboundRejectionReason.setStatus("current")
_MtaGroupOutboundConnectFailureReason_Type = SnmpAdminString
_MtaGroupOutboundConnectFailureReason_Object = MibTableColumn
mtaGroupOutboundConnectFailureReason = _MtaGroupOutboundConnectFailureReason_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 22),
    _MtaGroupOutboundConnectFailureReason_Type()
)
mtaGroupOutboundConnectFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupOutboundConnectFailureReason.setStatus("current")
_MtaGroupScheduledRetry_Type = TimeInterval
_MtaGroupScheduledRetry_Object = MibTableColumn
mtaGroupScheduledRetry = _MtaGroupScheduledRetry_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 23),
    _MtaGroupScheduledRetry_Type()
)
mtaGroupScheduledRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupScheduledRetry.setStatus("current")
_MtaGroupMailProtocol_Type = ObjectIdentifier
_MtaGroupMailProtocol_Object = MibTableColumn
mtaGroupMailProtocol = _MtaGroupMailProtocol_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 24),
    _MtaGroupMailProtocol_Type()
)
mtaGroupMailProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupMailProtocol.setStatus("current")
_MtaGroupName_Type = SnmpAdminString
_MtaGroupName_Object = MibTableColumn
mtaGroupName = _MtaGroupName_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 25),
    _MtaGroupName_Type()
)
mtaGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupName.setStatus("current")
_MtaGroupSuccessfulConvertedMessages_Type = Counter32
_MtaGroupSuccessfulConvertedMessages_Object = MibTableColumn
mtaGroupSuccessfulConvertedMessages = _MtaGroupSuccessfulConvertedMessages_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 26),
    _MtaGroupSuccessfulConvertedMessages_Type()
)
mtaGroupSuccessfulConvertedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupSuccessfulConvertedMessages.setStatus("current")
_MtaGroupFailedConvertedMessages_Type = Counter32
_MtaGroupFailedConvertedMessages_Object = MibTableColumn
mtaGroupFailedConvertedMessages = _MtaGroupFailedConvertedMessages_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 27),
    _MtaGroupFailedConvertedMessages_Type()
)
mtaGroupFailedConvertedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupFailedConvertedMessages.setStatus("current")
_MtaGroupDescription_Type = SnmpAdminString
_MtaGroupDescription_Object = MibTableColumn
mtaGroupDescription = _MtaGroupDescription_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 28),
    _MtaGroupDescription_Type()
)
mtaGroupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupDescription.setStatus("current")
_MtaGroupURL_Type = URLString
_MtaGroupURL_Object = MibTableColumn
mtaGroupURL = _MtaGroupURL_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 29),
    _MtaGroupURL_Type()
)
mtaGroupURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupURL.setStatus("current")
_MtaGroupCreationTime_Type = TimeInterval
_MtaGroupCreationTime_Object = MibTableColumn
mtaGroupCreationTime = _MtaGroupCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 30),
    _MtaGroupCreationTime_Type()
)
mtaGroupCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupCreationTime.setStatus("current")


class _MtaGroupHierarchy_Type(Integer32):
    """Custom type mtaGroupHierarchy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_MtaGroupHierarchy_Type.__name__ = "Integer32"
_MtaGroupHierarchy_Object = MibTableColumn
mtaGroupHierarchy = _MtaGroupHierarchy_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 31),
    _MtaGroupHierarchy_Type()
)
mtaGroupHierarchy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupHierarchy.setStatus("current")
_MtaGroupOldestMessageId_Type = SnmpAdminString
_MtaGroupOldestMessageId_Object = MibTableColumn
mtaGroupOldestMessageId = _MtaGroupOldestMessageId_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 32),
    _MtaGroupOldestMessageId_Type()
)
mtaGroupOldestMessageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupOldestMessageId.setStatus("current")
_MtaGroupLoopsDetected_Type = Counter32
_MtaGroupLoopsDetected_Object = MibTableColumn
mtaGroupLoopsDetected = _MtaGroupLoopsDetected_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 33),
    _MtaGroupLoopsDetected_Type()
)
mtaGroupLoopsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupLoopsDetected.setStatus("current")
_MtaGroupLastOutboundAssociationAttempt_Type = TimeInterval
_MtaGroupLastOutboundAssociationAttempt_Object = MibTableColumn
mtaGroupLastOutboundAssociationAttempt = _MtaGroupLastOutboundAssociationAttempt_Object(
    (1, 3, 6, 1, 2, 1, 28, 2, 1, 34),
    _MtaGroupLastOutboundAssociationAttempt_Type()
)
mtaGroupLastOutboundAssociationAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupLastOutboundAssociationAttempt.setStatus("current")
_MtaGroupAssociationTable_Object = MibTable
mtaGroupAssociationTable = _MtaGroupAssociationTable_Object(
    (1, 3, 6, 1, 2, 1, 28, 3)
)
if mibBuilder.loadTexts:
    mtaGroupAssociationTable.setStatus("current")
_MtaGroupAssociationEntry_Object = MibTableRow
mtaGroupAssociationEntry = _MtaGroupAssociationEntry_Object(
    (1, 3, 6, 1, 2, 1, 28, 3, 1)
)
mtaGroupAssociationEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "MTA-MIB", "mtaGroupIndex"),
    (0, "MTA-MIB", "mtaGroupAssociationIndex"),
)
if mibBuilder.loadTexts:
    mtaGroupAssociationEntry.setStatus("current")


class _MtaGroupAssociationIndex_Type(Integer32):
    """Custom type mtaGroupAssociationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MtaGroupAssociationIndex_Type.__name__ = "Integer32"
_MtaGroupAssociationIndex_Object = MibTableColumn
mtaGroupAssociationIndex = _MtaGroupAssociationIndex_Object(
    (1, 3, 6, 1, 2, 1, 28, 3, 1, 1),
    _MtaGroupAssociationIndex_Type()
)
mtaGroupAssociationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupAssociationIndex.setStatus("current")
_MtaConformance_ObjectIdentity = ObjectIdentity
mtaConformance = _MtaConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 28, 4)
)
_MtaGroups_ObjectIdentity = ObjectIdentity
mtaGroups = _MtaGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 28, 4, 1)
)
_MtaCompliances_ObjectIdentity = ObjectIdentity
mtaCompliances = _MtaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 28, 4, 2)
)
_MtaGroupErrorTable_Object = MibTable
mtaGroupErrorTable = _MtaGroupErrorTable_Object(
    (1, 3, 6, 1, 2, 1, 28, 5)
)
if mibBuilder.loadTexts:
    mtaGroupErrorTable.setStatus("current")
_MtaGroupErrorEntry_Object = MibTableRow
mtaGroupErrorEntry = _MtaGroupErrorEntry_Object(
    (1, 3, 6, 1, 2, 1, 28, 5, 1)
)
mtaGroupErrorEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "MTA-MIB", "mtaGroupIndex"),
    (0, "MTA-MIB", "mtaStatusCode"),
)
if mibBuilder.loadTexts:
    mtaGroupErrorEntry.setStatus("current")
_MtaGroupInboundErrorCount_Type = Counter32
_MtaGroupInboundErrorCount_Object = MibTableColumn
mtaGroupInboundErrorCount = _MtaGroupInboundErrorCount_Object(
    (1, 3, 6, 1, 2, 1, 28, 5, 1, 1),
    _MtaGroupInboundErrorCount_Type()
)
mtaGroupInboundErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupInboundErrorCount.setStatus("current")
_MtaGroupInternalErrorCount_Type = Counter32
_MtaGroupInternalErrorCount_Object = MibTableColumn
mtaGroupInternalErrorCount = _MtaGroupInternalErrorCount_Object(
    (1, 3, 6, 1, 2, 1, 28, 5, 1, 2),
    _MtaGroupInternalErrorCount_Type()
)
mtaGroupInternalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupInternalErrorCount.setStatus("current")
_MtaGroupOutboundErrorCount_Type = Counter32
_MtaGroupOutboundErrorCount_Object = MibTableColumn
mtaGroupOutboundErrorCount = _MtaGroupOutboundErrorCount_Object(
    (1, 3, 6, 1, 2, 1, 28, 5, 1, 3),
    _MtaGroupOutboundErrorCount_Type()
)
mtaGroupOutboundErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupOutboundErrorCount.setStatus("current")


class _MtaStatusCode_Type(Integer32):
    """Custom type mtaStatusCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000000, 5999999),
    )


_MtaStatusCode_Type.__name__ = "Integer32"
_MtaStatusCode_Object = MibTableColumn
mtaStatusCode = _MtaStatusCode_Object(
    (1, 3, 6, 1, 2, 1, 28, 5, 1, 4),
    _MtaStatusCode_Type()
)
mtaStatusCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtaStatusCode.setStatus("current")

# Managed Objects groups

mtaRFC2249Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 28, 4, 1, 4)
)
mtaRFC2249Group.setObjects(
      *(("MTA-MIB", "mtaReceivedMessages"),
        ("MTA-MIB", "mtaStoredMessages"),
        ("MTA-MIB", "mtaTransmittedMessages"),
        ("MTA-MIB", "mtaReceivedVolume"),
        ("MTA-MIB", "mtaStoredVolume"),
        ("MTA-MIB", "mtaTransmittedVolume"),
        ("MTA-MIB", "mtaReceivedRecipients"),
        ("MTA-MIB", "mtaStoredRecipients"),
        ("MTA-MIB", "mtaTransmittedRecipients"),
        ("MTA-MIB", "mtaSuccessfulConvertedMessages"),
        ("MTA-MIB", "mtaFailedConvertedMessages"),
        ("MTA-MIB", "mtaGroupReceivedMessages"),
        ("MTA-MIB", "mtaGroupRejectedMessages"),
        ("MTA-MIB", "mtaGroupStoredMessages"),
        ("MTA-MIB", "mtaGroupTransmittedMessages"),
        ("MTA-MIB", "mtaGroupReceivedVolume"),
        ("MTA-MIB", "mtaGroupStoredVolume"),
        ("MTA-MIB", "mtaGroupTransmittedVolume"),
        ("MTA-MIB", "mtaGroupReceivedRecipients"),
        ("MTA-MIB", "mtaGroupStoredRecipients"),
        ("MTA-MIB", "mtaGroupTransmittedRecipients"),
        ("MTA-MIB", "mtaGroupOldestMessageStored"),
        ("MTA-MIB", "mtaGroupInboundAssociations"),
        ("MTA-MIB", "mtaGroupOutboundAssociations"),
        ("MTA-MIB", "mtaLoopsDetected"),
        ("MTA-MIB", "mtaGroupAccumulatedInboundAssociations"),
        ("MTA-MIB", "mtaGroupAccumulatedOutboundAssociations"),
        ("MTA-MIB", "mtaGroupLastInboundActivity"),
        ("MTA-MIB", "mtaGroupLastOutboundActivity"),
        ("MTA-MIB", "mtaGroupLastOutboundAssociationAttempt"),
        ("MTA-MIB", "mtaGroupRejectedInboundAssociations"),
        ("MTA-MIB", "mtaGroupFailedOutboundAssociations"),
        ("MTA-MIB", "mtaGroupInboundRejectionReason"),
        ("MTA-MIB", "mtaGroupOutboundConnectFailureReason"),
        ("MTA-MIB", "mtaGroupScheduledRetry"),
        ("MTA-MIB", "mtaGroupMailProtocol"),
        ("MTA-MIB", "mtaGroupName"),
        ("MTA-MIB", "mtaGroupSuccessfulConvertedMessages"),
        ("MTA-MIB", "mtaGroupFailedConvertedMessages"),
        ("MTA-MIB", "mtaGroupDescription"),
        ("MTA-MIB", "mtaGroupURL"),
        ("MTA-MIB", "mtaGroupCreationTime"),
        ("MTA-MIB", "mtaGroupHierarchy"),
        ("MTA-MIB", "mtaGroupOldestMessageId"),
        ("MTA-MIB", "mtaGroupLoopsDetected"))
)
if mibBuilder.loadTexts:
    mtaRFC2249Group.setStatus("current")

mtaRFC2249AssocGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 28, 4, 1, 5)
)
mtaRFC2249AssocGroup.setObjects(
    ("MTA-MIB", "mtaGroupAssociationIndex")
)
if mibBuilder.loadTexts:
    mtaRFC2249AssocGroup.setStatus("current")

mtaRFC2249ErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 28, 4, 1, 6)
)
mtaRFC2249ErrorGroup.setObjects(
      *(("MTA-MIB", "mtaGroupInboundErrorCount"),
        ("MTA-MIB", "mtaGroupInternalErrorCount"),
        ("MTA-MIB", "mtaGroupOutboundErrorCount"))
)
if mibBuilder.loadTexts:
    mtaRFC2249ErrorGroup.setStatus("current")

mtaRFC2789Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 28, 4, 1, 7)
)
mtaRFC2789Group.setObjects(
      *(("MTA-MIB", "mtaReceivedMessages"),
        ("MTA-MIB", "mtaStoredMessages"),
        ("MTA-MIB", "mtaTransmittedMessages"),
        ("MTA-MIB", "mtaReceivedVolume"),
        ("MTA-MIB", "mtaStoredVolume"),
        ("MTA-MIB", "mtaTransmittedVolume"),
        ("MTA-MIB", "mtaReceivedRecipients"),
        ("MTA-MIB", "mtaStoredRecipients"),
        ("MTA-MIB", "mtaTransmittedRecipients"),
        ("MTA-MIB", "mtaSuccessfulConvertedMessages"),
        ("MTA-MIB", "mtaFailedConvertedMessages"),
        ("MTA-MIB", "mtaGroupReceivedMessages"),
        ("MTA-MIB", "mtaGroupRejectedMessages"),
        ("MTA-MIB", "mtaGroupStoredMessages"),
        ("MTA-MIB", "mtaGroupTransmittedMessages"),
        ("MTA-MIB", "mtaGroupReceivedVolume"),
        ("MTA-MIB", "mtaGroupStoredVolume"),
        ("MTA-MIB", "mtaGroupTransmittedVolume"),
        ("MTA-MIB", "mtaGroupReceivedRecipients"),
        ("MTA-MIB", "mtaGroupStoredRecipients"),
        ("MTA-MIB", "mtaGroupTransmittedRecipients"),
        ("MTA-MIB", "mtaGroupOldestMessageStored"),
        ("MTA-MIB", "mtaGroupInboundAssociations"),
        ("MTA-MIB", "mtaGroupOutboundAssociations"),
        ("MTA-MIB", "mtaLoopsDetected"),
        ("MTA-MIB", "mtaGroupAccumulatedInboundAssociations"),
        ("MTA-MIB", "mtaGroupAccumulatedOutboundAssociations"),
        ("MTA-MIB", "mtaGroupLastInboundActivity"),
        ("MTA-MIB", "mtaGroupLastOutboundActivity"),
        ("MTA-MIB", "mtaGroupLastOutboundAssociationAttempt"),
        ("MTA-MIB", "mtaGroupRejectedInboundAssociations"),
        ("MTA-MIB", "mtaGroupFailedOutboundAssociations"),
        ("MTA-MIB", "mtaGroupInboundRejectionReason"),
        ("MTA-MIB", "mtaGroupOutboundConnectFailureReason"),
        ("MTA-MIB", "mtaGroupScheduledRetry"),
        ("MTA-MIB", "mtaGroupMailProtocol"),
        ("MTA-MIB", "mtaGroupName"),
        ("MTA-MIB", "mtaGroupSuccessfulConvertedMessages"),
        ("MTA-MIB", "mtaGroupFailedConvertedMessages"),
        ("MTA-MIB", "mtaGroupDescription"),
        ("MTA-MIB", "mtaGroupURL"),
        ("MTA-MIB", "mtaGroupCreationTime"),
        ("MTA-MIB", "mtaGroupHierarchy"),
        ("MTA-MIB", "mtaGroupOldestMessageId"),
        ("MTA-MIB", "mtaGroupLoopsDetected"))
)
if mibBuilder.loadTexts:
    mtaRFC2789Group.setStatus("current")

mtaRFC2789AssocGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 28, 4, 1, 8)
)
mtaRFC2789AssocGroup.setObjects(
    ("MTA-MIB", "mtaGroupAssociationIndex")
)
if mibBuilder.loadTexts:
    mtaRFC2789AssocGroup.setStatus("current")

mtaRFC2789ErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 28, 4, 1, 9)
)
mtaRFC2789ErrorGroup.setObjects(
      *(("MTA-MIB", "mtaGroupInboundErrorCount"),
        ("MTA-MIB", "mtaGroupInternalErrorCount"),
        ("MTA-MIB", "mtaGroupOutboundErrorCount"))
)
if mibBuilder.loadTexts:
    mtaRFC2789ErrorGroup.setStatus("current")

mtaRFC1566Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 28, 4, 1, 10)
)
mtaRFC1566Group.setObjects(
      *(("MTA-MIB", "mtaReceivedMessages"),
        ("MTA-MIB", "mtaStoredMessages"),
        ("MTA-MIB", "mtaTransmittedMessages"),
        ("MTA-MIB", "mtaReceivedVolume"),
        ("MTA-MIB", "mtaStoredVolume"),
        ("MTA-MIB", "mtaTransmittedVolume"),
        ("MTA-MIB", "mtaReceivedRecipients"),
        ("MTA-MIB", "mtaStoredRecipients"),
        ("MTA-MIB", "mtaTransmittedRecipients"),
        ("MTA-MIB", "mtaGroupReceivedMessages"),
        ("MTA-MIB", "mtaGroupRejectedMessages"),
        ("MTA-MIB", "mtaGroupStoredMessages"),
        ("MTA-MIB", "mtaGroupTransmittedMessages"),
        ("MTA-MIB", "mtaGroupReceivedVolume"),
        ("MTA-MIB", "mtaGroupStoredVolume"),
        ("MTA-MIB", "mtaGroupTransmittedVolume"),
        ("MTA-MIB", "mtaGroupReceivedRecipients"),
        ("MTA-MIB", "mtaGroupStoredRecipients"),
        ("MTA-MIB", "mtaGroupTransmittedRecipients"),
        ("MTA-MIB", "mtaGroupOldestMessageStored"),
        ("MTA-MIB", "mtaGroupInboundAssociations"),
        ("MTA-MIB", "mtaGroupOutboundAssociations"),
        ("MTA-MIB", "mtaGroupAccumulatedInboundAssociations"),
        ("MTA-MIB", "mtaGroupAccumulatedOutboundAssociations"),
        ("MTA-MIB", "mtaGroupLastInboundActivity"),
        ("MTA-MIB", "mtaGroupLastOutboundActivity"),
        ("MTA-MIB", "mtaGroupRejectedInboundAssociations"),
        ("MTA-MIB", "mtaGroupFailedOutboundAssociations"),
        ("MTA-MIB", "mtaGroupInboundRejectionReason"),
        ("MTA-MIB", "mtaGroupOutboundConnectFailureReason"),
        ("MTA-MIB", "mtaGroupScheduledRetry"),
        ("MTA-MIB", "mtaGroupMailProtocol"),
        ("MTA-MIB", "mtaGroupName"))
)
if mibBuilder.loadTexts:
    mtaRFC1566Group.setStatus("current")

mtaRFC1566AssocGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 28, 4, 1, 11)
)
mtaRFC1566AssocGroup.setObjects(
    ("MTA-MIB", "mtaGroupAssociationIndex")
)
if mibBuilder.loadTexts:
    mtaRFC1566AssocGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mtaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 28, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mtaCompliance.setStatus(
        "current"
    )

mtaAssocCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 28, 4, 2, 2)
)
if mibBuilder.loadTexts:
    mtaAssocCompliance.setStatus(
        "current"
    )

mtaRFC2249Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 28, 4, 2, 5)
)
if mibBuilder.loadTexts:
    mtaRFC2249Compliance.setStatus(
        "current"
    )

mtaRFC2249AssocCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 28, 4, 2, 6)
)
if mibBuilder.loadTexts:
    mtaRFC2249AssocCompliance.setStatus(
        "current"
    )

mtaRFC2249ErrorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 28, 4, 2, 7)
)
if mibBuilder.loadTexts:
    mtaRFC2249ErrorCompliance.setStatus(
        "current"
    )

mtaRFC2249FullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 28, 4, 2, 8)
)
if mibBuilder.loadTexts:
    mtaRFC2249FullCompliance.setStatus(
        "current"
    )

mtaRFC2789Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 28, 4, 2, 9)
)
if mibBuilder.loadTexts:
    mtaRFC2789Compliance.setStatus(
        "current"
    )

mtaRFC2789AssocCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 28, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mtaRFC2789AssocCompliance.setStatus(
        "current"
    )

mtaRFC2789ErrorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 28, 4, 2, 11)
)
if mibBuilder.loadTexts:
    mtaRFC2789ErrorCompliance.setStatus(
        "current"
    )

mtaRFC2789FullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 28, 4, 2, 12)
)
if mibBuilder.loadTexts:
    mtaRFC2789FullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MTA-MIB",
    **{"mta": mta,
       "mtaTable": mtaTable,
       "mtaEntry": mtaEntry,
       "mtaReceivedMessages": mtaReceivedMessages,
       "mtaStoredMessages": mtaStoredMessages,
       "mtaTransmittedMessages": mtaTransmittedMessages,
       "mtaReceivedVolume": mtaReceivedVolume,
       "mtaStoredVolume": mtaStoredVolume,
       "mtaTransmittedVolume": mtaTransmittedVolume,
       "mtaReceivedRecipients": mtaReceivedRecipients,
       "mtaStoredRecipients": mtaStoredRecipients,
       "mtaTransmittedRecipients": mtaTransmittedRecipients,
       "mtaSuccessfulConvertedMessages": mtaSuccessfulConvertedMessages,
       "mtaFailedConvertedMessages": mtaFailedConvertedMessages,
       "mtaLoopsDetected": mtaLoopsDetected,
       "mtaGroupTable": mtaGroupTable,
       "mtaGroupEntry": mtaGroupEntry,
       "mtaGroupIndex": mtaGroupIndex,
       "mtaGroupReceivedMessages": mtaGroupReceivedMessages,
       "mtaGroupRejectedMessages": mtaGroupRejectedMessages,
       "mtaGroupStoredMessages": mtaGroupStoredMessages,
       "mtaGroupTransmittedMessages": mtaGroupTransmittedMessages,
       "mtaGroupReceivedVolume": mtaGroupReceivedVolume,
       "mtaGroupStoredVolume": mtaGroupStoredVolume,
       "mtaGroupTransmittedVolume": mtaGroupTransmittedVolume,
       "mtaGroupReceivedRecipients": mtaGroupReceivedRecipients,
       "mtaGroupStoredRecipients": mtaGroupStoredRecipients,
       "mtaGroupTransmittedRecipients": mtaGroupTransmittedRecipients,
       "mtaGroupOldestMessageStored": mtaGroupOldestMessageStored,
       "mtaGroupInboundAssociations": mtaGroupInboundAssociations,
       "mtaGroupOutboundAssociations": mtaGroupOutboundAssociations,
       "mtaGroupAccumulatedInboundAssociations": mtaGroupAccumulatedInboundAssociations,
       "mtaGroupAccumulatedOutboundAssociations": mtaGroupAccumulatedOutboundAssociations,
       "mtaGroupLastInboundActivity": mtaGroupLastInboundActivity,
       "mtaGroupLastOutboundActivity": mtaGroupLastOutboundActivity,
       "mtaGroupRejectedInboundAssociations": mtaGroupRejectedInboundAssociations,
       "mtaGroupFailedOutboundAssociations": mtaGroupFailedOutboundAssociations,
       "mtaGroupInboundRejectionReason": mtaGroupInboundRejectionReason,
       "mtaGroupOutboundConnectFailureReason": mtaGroupOutboundConnectFailureReason,
       "mtaGroupScheduledRetry": mtaGroupScheduledRetry,
       "mtaGroupMailProtocol": mtaGroupMailProtocol,
       "mtaGroupName": mtaGroupName,
       "mtaGroupSuccessfulConvertedMessages": mtaGroupSuccessfulConvertedMessages,
       "mtaGroupFailedConvertedMessages": mtaGroupFailedConvertedMessages,
       "mtaGroupDescription": mtaGroupDescription,
       "mtaGroupURL": mtaGroupURL,
       "mtaGroupCreationTime": mtaGroupCreationTime,
       "mtaGroupHierarchy": mtaGroupHierarchy,
       "mtaGroupOldestMessageId": mtaGroupOldestMessageId,
       "mtaGroupLoopsDetected": mtaGroupLoopsDetected,
       "mtaGroupLastOutboundAssociationAttempt": mtaGroupLastOutboundAssociationAttempt,
       "mtaGroupAssociationTable": mtaGroupAssociationTable,
       "mtaGroupAssociationEntry": mtaGroupAssociationEntry,
       "mtaGroupAssociationIndex": mtaGroupAssociationIndex,
       "mtaConformance": mtaConformance,
       "mtaGroups": mtaGroups,
       "mtaRFC2249Group": mtaRFC2249Group,
       "mtaRFC2249AssocGroup": mtaRFC2249AssocGroup,
       "mtaRFC2249ErrorGroup": mtaRFC2249ErrorGroup,
       "mtaRFC2789Group": mtaRFC2789Group,
       "mtaRFC2789AssocGroup": mtaRFC2789AssocGroup,
       "mtaRFC2789ErrorGroup": mtaRFC2789ErrorGroup,
       "mtaRFC1566Group": mtaRFC1566Group,
       "mtaRFC1566AssocGroup": mtaRFC1566AssocGroup,
       "mtaCompliances": mtaCompliances,
       "mtaCompliance": mtaCompliance,
       "mtaAssocCompliance": mtaAssocCompliance,
       "mtaRFC2249Compliance": mtaRFC2249Compliance,
       "mtaRFC2249AssocCompliance": mtaRFC2249AssocCompliance,
       "mtaRFC2249ErrorCompliance": mtaRFC2249ErrorCompliance,
       "mtaRFC2249FullCompliance": mtaRFC2249FullCompliance,
       "mtaRFC2789Compliance": mtaRFC2789Compliance,
       "mtaRFC2789AssocCompliance": mtaRFC2789AssocCompliance,
       "mtaRFC2789ErrorCompliance": mtaRFC2789ErrorCompliance,
       "mtaRFC2789FullCompliance": mtaRFC2789FullCompliance,
       "mtaGroupErrorTable": mtaGroupErrorTable,
       "mtaGroupErrorEntry": mtaGroupErrorEntry,
       "mtaGroupInboundErrorCount": mtaGroupInboundErrorCount,
       "mtaGroupInternalErrorCount": mtaGroupInternalErrorCount,
       "mtaGroupOutboundErrorCount": mtaGroupOutboundErrorCount,
       "mtaStatusCode": mtaStatusCode}
)

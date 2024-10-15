# SNMP MIB module (EXTENDED-MADMAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTENDED-MADMAN-MIB
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

(mtaGroupInboundRejectionReason,
 mtaGroupIndex,
 mtaGroupName,
 mtaGroupOutboundConnectFailureReason) = mibBuilder.importSymbols(
    "MTA-MIB",
    "mtaGroupInboundRejectionReason",
    "mtaGroupIndex",
    "mtaGroupName",
    "mtaGroupOutboundConnectFailureReason")

(applIndex,
 applLastChange,
 applName,
 applOperStatus) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex",
    "applLastChange",
    "applName",
    "applOperStatus")

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



class TimeInterval(Integer32):
    """Custom type TimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lotus_ObjectIdentity = ObjectIdentity
lotus = _Lotus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334)
)
_Notes_ObjectIdentity = ObjectIdentity
notes = _Notes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 1)
)
_Lcs_ObjectIdentity = ObjectIdentity
lcs = _Lcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 2)
)
_Softswitch_ObjectIdentity = ObjectIdentity
softswitch = _Softswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3)
)
_Common_mibs_ObjectIdentity = ObjectIdentity
common_mibs = _Common_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 1)
)
_ExtendedMADMAN_ObjectIdentity = ObjectIdentity
extendedMADMAN = _ExtendedMADMAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1)
)
_ExtendedApplTable_Object = MibTable
extendedApplTable = _ExtendedApplTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    extendedApplTable.setStatus("mandatory")
_ExtendedApplEntry_Object = MibTableRow
extendedApplEntry = _ExtendedApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 1, 1)
)
extendedApplEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    extendedApplEntry.setStatus("mandatory")
_ApplDescr_Type = DisplayString
_ApplDescr_Object = MibTableColumn
applDescr = _ApplDescr_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 1, 1, 1),
    _ApplDescr_Type()
)
applDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applDescr.setStatus("mandatory")
_ApplContact_Type = DisplayString
_ApplContact_Object = MibTableColumn
applContact = _ApplContact_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 1, 1, 2),
    _ApplContact_Type()
)
applContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applContact.setStatus("mandatory")


class _ApplDesiredOperStatus_Type(Integer32):
    """Custom type applDesiredOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("halted", 3),
          ("up", 1))
    )


_ApplDesiredOperStatus_Type.__name__ = "Integer32"
_ApplDesiredOperStatus_Object = MibTableColumn
applDesiredOperStatus = _ApplDesiredOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 1, 1, 3),
    _ApplDesiredOperStatus_Type()
)
applDesiredOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applDesiredOperStatus.setStatus("mandatory")
_ExtendedMtaTable_Object = MibTable
extendedMtaTable = _ExtendedMtaTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    extendedMtaTable.setStatus("mandatory")
_ExtendedMtaEntry_Object = MibTableRow
extendedMtaEntry = _ExtendedMtaEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 2, 1)
)
extendedMtaEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    extendedMtaEntry.setStatus("mandatory")
_MtaFailedMessages_Type = Counter32
_MtaFailedMessages_Object = MibTableColumn
mtaFailedMessages = _MtaFailedMessages_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 2, 1, 1),
    _MtaFailedMessages_Type()
)
mtaFailedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaFailedMessages.setStatus("mandatory")
_MtaFailedVolume_Type = Counter32
_MtaFailedVolume_Object = MibTableColumn
mtaFailedVolume = _MtaFailedVolume_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 2, 1, 2),
    _MtaFailedVolume_Type()
)
mtaFailedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaFailedVolume.setStatus("mandatory")
_MtaFailedRecipients_Type = Counter32
_MtaFailedRecipients_Object = MibTableColumn
mtaFailedRecipients = _MtaFailedRecipients_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 2, 1, 3),
    _MtaFailedRecipients_Type()
)
mtaFailedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaFailedRecipients.setStatus("mandatory")
_MtaLastMessageFailureReason_Type = DisplayString
_MtaLastMessageFailureReason_Object = MibTableColumn
mtaLastMessageFailureReason = _MtaLastMessageFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 2, 1, 4),
    _MtaLastMessageFailureReason_Type()
)
mtaLastMessageFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaLastMessageFailureReason.setStatus("mandatory")
_MtaLargestMessageStored_Type = Gauge32
_MtaLargestMessageStored_Object = MibTableColumn
mtaLargestMessageStored = _MtaLargestMessageStored_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 2, 1, 5),
    _MtaLargestMessageStored_Type()
)
mtaLargestMessageStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaLargestMessageStored.setStatus("mandatory")
_MtaOldestMessageStored_Type = TimeTicks
_MtaOldestMessageStored_Object = MibTableColumn
mtaOldestMessageStored = _MtaOldestMessageStored_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 2, 1, 6),
    _MtaOldestMessageStored_Type()
)
mtaOldestMessageStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaOldestMessageStored.setStatus("mandatory")


class _MtaInputInhibited_Type(Integer32):
    """Custom type mtaInputInhibited based on Integer32"""
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


_MtaInputInhibited_Type.__name__ = "Integer32"
_MtaInputInhibited_Object = MibTableColumn
mtaInputInhibited = _MtaInputInhibited_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 2, 1, 7),
    _MtaInputInhibited_Type()
)
mtaInputInhibited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtaInputInhibited.setStatus("mandatory")


class _MtaType_Type(Integer32):
    """Custom type mtaType based on Integer32"""
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
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("ccMail", 6),
          ("cmc", 8),
          ("fax", 13),
          ("mapi", 9),
          ("notes", 7),
          ("other", 20),
          ("profs", 12),
          ("smtp", 5),
          ("smtp-mime", 4),
          ("snads", 11),
          ("snapi", 10),
          ("unknown", 21),
          ("x400-84", 3),
          ("x400-88", 2),
          ("x400-92", 1))
    )


_MtaType_Type.__name__ = "Integer32"
_MtaType_Object = MibTableColumn
mtaType = _MtaType_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 2, 1, 8),
    _MtaType_Type()
)
mtaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaType.setStatus("mandatory")
_ExtendedMtaGroupTable_Object = MibTable
extendedMtaGroupTable = _ExtendedMtaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    extendedMtaGroupTable.setStatus("mandatory")
_ExtendedMtaGroupEntry_Object = MibTableRow
extendedMtaGroupEntry = _ExtendedMtaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1)
)
extendedMtaGroupEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "MTA-MIB", "mtaGroupIndex"),
)
if mibBuilder.loadTexts:
    extendedMtaGroupEntry.setStatus("mandatory")
_MtaGroupIdOfOldestMessage_Type = DisplayString
_MtaGroupIdOfOldestMessage_Object = MibTableColumn
mtaGroupIdOfOldestMessage = _MtaGroupIdOfOldestMessage_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 1),
    _MtaGroupIdOfOldestMessage_Type()
)
mtaGroupIdOfOldestMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupIdOfOldestMessage.setStatus("mandatory")
_MtaGroupLastOutboundAssociationAttempt_Type = TimeTicks
_MtaGroupLastOutboundAssociationAttempt_Object = MibTableColumn
mtaGroupLastOutboundAssociationAttempt = _MtaGroupLastOutboundAssociationAttempt_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 2),
    _MtaGroupLastOutboundAssociationAttempt_Type()
)
mtaGroupLastOutboundAssociationAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupLastOutboundAssociationAttempt.setStatus("mandatory")
_MtaGroupMaxInboundAssociations_Type = Gauge32
_MtaGroupMaxInboundAssociations_Object = MibTableColumn
mtaGroupMaxInboundAssociations = _MtaGroupMaxInboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 3),
    _MtaGroupMaxInboundAssociations_Type()
)
mtaGroupMaxInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupMaxInboundAssociations.setStatus("mandatory")
_MtaGroupMaxOutboundAssociations_Type = Gauge32
_MtaGroupMaxOutboundAssociations_Object = MibTableColumn
mtaGroupMaxOutboundAssociations = _MtaGroupMaxOutboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 4),
    _MtaGroupMaxOutboundAssociations_Type()
)
mtaGroupMaxOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupMaxOutboundAssociations.setStatus("mandatory")


class _MtaGroupCurrentState_Type(Integer32):
    """Custom type mtaGroupCurrentState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("configurable", 3),
          ("initializing", 2),
          ("input-disabled", 4),
          ("output-disabled", 5),
          ("running", 6),
          ("stopped", 1),
          ("stopping", 7),
          ("unknown", 8))
    )


_MtaGroupCurrentState_Type.__name__ = "Integer32"
_MtaGroupCurrentState_Object = MibTableColumn
mtaGroupCurrentState = _MtaGroupCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 5),
    _MtaGroupCurrentState_Type()
)
mtaGroupCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupCurrentState.setStatus("mandatory")
_MtaGroupLastChange_Type = TimeTicks
_MtaGroupLastChange_Object = MibTableColumn
mtaGroupLastChange = _MtaGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 6),
    _MtaGroupLastChange_Type()
)
mtaGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupLastChange.setStatus("mandatory")
_MtaGroupLargestMessageStored_Type = Integer32
_MtaGroupLargestMessageStored_Object = MibTableColumn
mtaGroupLargestMessageStored = _MtaGroupLargestMessageStored_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 7),
    _MtaGroupLargestMessageStored_Type()
)
mtaGroupLargestMessageStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupLargestMessageStored.setStatus("mandatory")
_MtaGroupInboundRejectSecurityViolations_Type = Counter32
_MtaGroupInboundRejectSecurityViolations_Object = MibTableColumn
mtaGroupInboundRejectSecurityViolations = _MtaGroupInboundRejectSecurityViolations_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 8),
    _MtaGroupInboundRejectSecurityViolations_Type()
)
mtaGroupInboundRejectSecurityViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupInboundRejectSecurityViolations.setStatus("mandatory")
_MtaGroupOutboundFailSecurityViolations_Type = Counter32
_MtaGroupOutboundFailSecurityViolations_Object = MibTableColumn
mtaGroupOutboundFailSecurityViolations = _MtaGroupOutboundFailSecurityViolations_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 9),
    _MtaGroupOutboundFailSecurityViolations_Type()
)
mtaGroupOutboundFailSecurityViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupOutboundFailSecurityViolations.setStatus("mandatory")
_MtaGroupInboundRejectResourceFailures_Type = Counter32
_MtaGroupInboundRejectResourceFailures_Object = MibTableColumn
mtaGroupInboundRejectResourceFailures = _MtaGroupInboundRejectResourceFailures_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 10),
    _MtaGroupInboundRejectResourceFailures_Type()
)
mtaGroupInboundRejectResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupInboundRejectResourceFailures.setStatus("mandatory")
_MtaGroupOutboundFailResourceFailures_Type = Counter32
_MtaGroupOutboundFailResourceFailures_Object = MibTableColumn
mtaGroupOutboundFailResourceFailures = _MtaGroupOutboundFailResourceFailures_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 11),
    _MtaGroupOutboundFailResourceFailures_Type()
)
mtaGroupOutboundFailResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupOutboundFailResourceFailures.setStatus("mandatory")
_MtaGroupFailedVolume_Type = Counter32
_MtaGroupFailedVolume_Object = MibTableColumn
mtaGroupFailedVolume = _MtaGroupFailedVolume_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 12),
    _MtaGroupFailedVolume_Type()
)
mtaGroupFailedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupFailedVolume.setStatus("mandatory")
_MtaGroupFailedRecipients_Type = Counter32
_MtaGroupFailedRecipients_Object = MibTableColumn
mtaGroupFailedRecipients = _MtaGroupFailedRecipients_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 1, 1, 3, 1, 13),
    _MtaGroupFailedRecipients_Type()
)
mtaGroupFailedRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaGroupFailedRecipients.setStatus("mandatory")
_Lms_ObjectIdentity = ObjectIdentity
lms = _Lms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTENDED-MADMAN-MIB",
    **{"TimeInterval": TimeInterval,
       "lotus": lotus,
       "notes": notes,
       "lcs": lcs,
       "softswitch": softswitch,
       "common-mibs": common_mibs,
       "extendedMADMAN": extendedMADMAN,
       "extendedApplTable": extendedApplTable,
       "extendedApplEntry": extendedApplEntry,
       "applDescr": applDescr,
       "applContact": applContact,
       "applDesiredOperStatus": applDesiredOperStatus,
       "extendedMtaTable": extendedMtaTable,
       "extendedMtaEntry": extendedMtaEntry,
       "mtaFailedMessages": mtaFailedMessages,
       "mtaFailedVolume": mtaFailedVolume,
       "mtaFailedRecipients": mtaFailedRecipients,
       "mtaLastMessageFailureReason": mtaLastMessageFailureReason,
       "mtaLargestMessageStored": mtaLargestMessageStored,
       "mtaOldestMessageStored": mtaOldestMessageStored,
       "mtaInputInhibited": mtaInputInhibited,
       "mtaType": mtaType,
       "extendedMtaGroupTable": extendedMtaGroupTable,
       "extendedMtaGroupEntry": extendedMtaGroupEntry,
       "mtaGroupIdOfOldestMessage": mtaGroupIdOfOldestMessage,
       "mtaGroupLastOutboundAssociationAttempt": mtaGroupLastOutboundAssociationAttempt,
       "mtaGroupMaxInboundAssociations": mtaGroupMaxInboundAssociations,
       "mtaGroupMaxOutboundAssociations": mtaGroupMaxOutboundAssociations,
       "mtaGroupCurrentState": mtaGroupCurrentState,
       "mtaGroupLastChange": mtaGroupLastChange,
       "mtaGroupLargestMessageStored": mtaGroupLargestMessageStored,
       "mtaGroupInboundRejectSecurityViolations": mtaGroupInboundRejectSecurityViolations,
       "mtaGroupOutboundFailSecurityViolations": mtaGroupOutboundFailSecurityViolations,
       "mtaGroupInboundRejectResourceFailures": mtaGroupInboundRejectResourceFailures,
       "mtaGroupOutboundFailResourceFailures": mtaGroupOutboundFailResourceFailures,
       "mtaGroupFailedVolume": mtaGroupFailedVolume,
       "mtaGroupFailedRecipients": mtaGroupFailedRecipients,
       "lms": lms}
)

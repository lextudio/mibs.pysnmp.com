# SNMP MIB module (MESSAGE-TRACKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MESSAGE-TRACKING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:18 2024
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
 experimental,
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
    "experimental",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

mta_message_track = ModuleIdentity(
    (1, 3, 6, 1, 3, 73, 2, 1)
)


# Types definitions



class NameForm(Integer32):
    """Custom type NameForm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freeForm", 1),
          ("smtp", 3),
          ("x400", 2))
    )





class DispositionStatus(Integer32):
    """Custom type DispositionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("delivered", 3),
          ("dlist-expanded", 6),
          ("in-queue", 7),
          ("non-delivered", 4),
          ("redirected", 5),
          ("transferred", 2),
          ("unknown", 1))
    )





class MsgType(Integer32):
    """Custom type MsgType based on Integer32"""
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
        *(("any", 1),
          ("data", 2),
          ("probe", 4),
          ("status", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MsgTracking_ObjectIdentity = ObjectIdentity
msgTracking = _MsgTracking_ObjectIdentity(
    (1, 3, 6, 1, 3, 73, 2)
)
_MtaInformationTable_Object = MibTable
mtaInformationTable = _MtaInformationTable_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mtaInformationTable.setStatus("current")
_MtaInformationEntry_Object = MibTableRow
mtaInformationEntry = _MtaInformationEntry_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 1, 1)
)
mtaInformationEntry.setIndexNames(
    (0, "MESSAGE-TRACKING-MIB", "mtaIndex"),
)
if mibBuilder.loadTexts:
    mtaInformationEntry.setStatus("current")


class _MtaIndex_Type(Integer32):
    """Custom type mtaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MtaIndex_Type.__name__ = "Integer32"
_MtaIndex_Object = MibTableColumn
mtaIndex = _MtaIndex_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 1, 1, 1),
    _MtaIndex_Type()
)
mtaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaIndex.setStatus("current")
_MtaName_Type = DisplayString
_MtaName_Object = MibTableColumn
mtaName = _MtaName_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 1, 1, 2),
    _MtaName_Type()
)
mtaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaName.setStatus("current")
_MtaMessagingType_Type = DisplayString
_MtaMessagingType_Object = MibTableColumn
mtaMessagingType = _MtaMessagingType_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 1, 1, 3),
    _MtaMessagingType_Type()
)
mtaMessagingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaMessagingType.setStatus("current")
_MtaStartTimeforRecordedInformation_Type = DateAndTime
_MtaStartTimeforRecordedInformation_Object = MibScalar
mtaStartTimeforRecordedInformation = _MtaStartTimeforRecordedInformation_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 1, 1, 4),
    _MtaStartTimeforRecordedInformation_Type()
)
mtaStartTimeforRecordedInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaStartTimeforRecordedInformation.setStatus("current")
_MtaAlternativeAgent_Type = DisplayString
_MtaAlternativeAgent_Object = MibScalar
mtaAlternativeAgent = _MtaAlternativeAgent_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 1, 1, 5),
    _MtaAlternativeAgent_Type()
)
mtaAlternativeAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAlternativeAgent.setStatus("current")
_MsgTrackNextRequestIndex_Type = Counter32
_MsgTrackNextRequestIndex_Object = MibScalar
msgTrackNextRequestIndex = _MsgTrackNextRequestIndex_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 2),
    _MsgTrackNextRequestIndex_Type()
)
msgTrackNextRequestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgTrackNextRequestIndex.setStatus("current")
_MsgTrackRequestTable_Object = MibTable
msgTrackRequestTable = _MsgTrackRequestTable_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3)
)
if mibBuilder.loadTexts:
    msgTrackRequestTable.setStatus("current")
_MsgTrackRequestEntry_Object = MibTableRow
msgTrackRequestEntry = _MsgTrackRequestEntry_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1)
)
msgTrackRequestEntry.setIndexNames(
    (0, "MESSAGE-TRACKING-MIB", "reqEntryIndex"),
)
if mibBuilder.loadTexts:
    msgTrackRequestEntry.setStatus("current")


class _ReqEntryIndex_Type(Integer32):
    """Custom type reqEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ReqEntryIndex_Type.__name__ = "Integer32"
_ReqEntryIndex_Object = MibTableColumn
reqEntryIndex = _ReqEntryIndex_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 1),
    _ReqEntryIndex_Type()
)
reqEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqEntryIndex.setStatus("current")


class _ReqRowStatus_Type(Integer32):
    """Custom type reqRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_ReqRowStatus_Type.__name__ = "Integer32"
_ReqRowStatus_Object = MibTableColumn
reqRowStatus = _ReqRowStatus_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 2),
    _ReqRowStatus_Type()
)
reqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqRowStatus.setStatus("current")


class _ReqResponseStatus_Type(Integer32):
    """Custom type reqResponseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("failedError", 5),
          ("failedInvalidQuery", 4),
          ("failedNoMatches", 3),
          ("inProgress", 2),
          ("success", 7),
          ("successUnderqualified", 6),
          ("unknown", 1))
    )


_ReqResponseStatus_Type.__name__ = "Integer32"
_ReqResponseStatus_Object = MibTableColumn
reqResponseStatus = _ReqResponseStatus_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 3),
    _ReqResponseStatus_Type()
)
reqResponseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqResponseStatus.setStatus("current")


class _ReqMaxResponses_Type(Integer32):
    """Custom type reqMaxResponses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ReqMaxResponses_Type.__name__ = "Integer32"
_ReqMaxResponses_Object = MibTableColumn
reqMaxResponses = _ReqMaxResponses_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 4),
    _ReqMaxResponses_Type()
)
reqMaxResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqMaxResponses.setStatus("current")
_ReqUniqueMsgId_Type = DisplayString
_ReqUniqueMsgId_Object = MibTableColumn
reqUniqueMsgId = _ReqUniqueMsgId_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 5),
    _ReqUniqueMsgId_Type()
)
reqUniqueMsgId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqUniqueMsgId.setStatus("current")
_ReqInboundMsgId_Type = DisplayString
_ReqInboundMsgId_Object = MibTableColumn
reqInboundMsgId = _ReqInboundMsgId_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 6),
    _ReqInboundMsgId_Type()
)
reqInboundMsgId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqInboundMsgId.setStatus("current")
_ReqOutboundMsgId_Type = DisplayString
_ReqOutboundMsgId_Object = MibTableColumn
reqOutboundMsgId = _ReqOutboundMsgId_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 7),
    _ReqOutboundMsgId_Type()
)
reqOutboundMsgId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqOutboundMsgId.setStatus("current")
_ReqInboundOriginator_Type = DisplayString
_ReqInboundOriginator_Object = MibTableColumn
reqInboundOriginator = _ReqInboundOriginator_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 8),
    _ReqInboundOriginator_Type()
)
reqInboundOriginator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqInboundOriginator.setStatus("current")
_ReqOutboundOriginator_Type = DisplayString
_ReqOutboundOriginator_Object = MibTableColumn
reqOutboundOriginator = _ReqOutboundOriginator_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 9),
    _ReqOutboundOriginator_Type()
)
reqOutboundOriginator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqOutboundOriginator.setStatus("current")
_ReqOriginatorNameForm_Type = NameForm
_ReqOriginatorNameForm_Object = MibTableColumn
reqOriginatorNameForm = _ReqOriginatorNameForm_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 10),
    _ReqOriginatorNameForm_Type()
)
reqOriginatorNameForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqOriginatorNameForm.setStatus("current")
_ReqInboundRecipient_Type = DisplayString
_ReqInboundRecipient_Object = MibTableColumn
reqInboundRecipient = _ReqInboundRecipient_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 11),
    _ReqInboundRecipient_Type()
)
reqInboundRecipient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqInboundRecipient.setStatus("current")
_ReqOutboundRecipient_Type = DisplayString
_ReqOutboundRecipient_Object = MibTableColumn
reqOutboundRecipient = _ReqOutboundRecipient_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 12),
    _ReqOutboundRecipient_Type()
)
reqOutboundRecipient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqOutboundRecipient.setStatus("current")
_ReqRecipientNameForm_Type = NameForm
_ReqRecipientNameForm_Object = MibTableColumn
reqRecipientNameForm = _ReqRecipientNameForm_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 13),
    _ReqRecipientNameForm_Type()
)
reqRecipientNameForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqRecipientNameForm.setStatus("current")
_ReqSubject_Type = DisplayString
_ReqSubject_Object = MibTableColumn
reqSubject = _ReqSubject_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 14),
    _ReqSubject_Type()
)
reqSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqSubject.setStatus("current")


class _ReqMinMsgSize_Type(Integer32):
    """Custom type reqMinMsgSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ReqMinMsgSize_Type.__name__ = "Integer32"
_ReqMinMsgSize_Object = MibTableColumn
reqMinMsgSize = _ReqMinMsgSize_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 15),
    _ReqMinMsgSize_Type()
)
reqMinMsgSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqMinMsgSize.setStatus("current")


class _ReqMaxMsgSize_Type(Integer32):
    """Custom type reqMaxMsgSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ReqMaxMsgSize_Type.__name__ = "Integer32"
_ReqMaxMsgSize_Object = MibTableColumn
reqMaxMsgSize = _ReqMaxMsgSize_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 16),
    _ReqMaxMsgSize_Type()
)
reqMaxMsgSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqMaxMsgSize.setStatus("current")
_ReqEarliestArrivalTime_Type = DateAndTime
_ReqEarliestArrivalTime_Object = MibTableColumn
reqEarliestArrivalTime = _ReqEarliestArrivalTime_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 17),
    _ReqEarliestArrivalTime_Type()
)
reqEarliestArrivalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqEarliestArrivalTime.setStatus("current")
_ReqLatestArrivalTime_Type = DateAndTime
_ReqLatestArrivalTime_Object = MibTableColumn
reqLatestArrivalTime = _ReqLatestArrivalTime_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 18),
    _ReqLatestArrivalTime_Type()
)
reqLatestArrivalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqLatestArrivalTime.setStatus("current")
_ReqDispositionStatus_Type = DispositionStatus
_ReqDispositionStatus_Object = MibTableColumn
reqDispositionStatus = _ReqDispositionStatus_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 19),
    _ReqDispositionStatus_Type()
)
reqDispositionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqDispositionStatus.setStatus("current")
_ReqMsgType_Type = MsgType
_ReqMsgType_Object = MibTableColumn
reqMsgType = _ReqMsgType_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 20),
    _ReqMsgType_Type()
)
reqMsgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqMsgType.setStatus("current")


class _ReqCollapseRecipients_Type(Integer32):
    """Custom type reqCollapseRecipients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ReqCollapseRecipients_Type.__name__ = "Integer32"
_ReqCollapseRecipients_Object = MibTableColumn
reqCollapseRecipients = _ReqCollapseRecipients_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 21),
    _ReqCollapseRecipients_Type()
)
reqCollapseRecipients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reqCollapseRecipients.setStatus("current")
_ReqFailureReason_Type = DisplayString
_ReqFailureReason_Object = MibTableColumn
reqFailureReason = _ReqFailureReason_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 3, 1, 22),
    _ReqFailureReason_Type()
)
reqFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reqFailureReason.setStatus("current")
_MsgTrackResponseTable_Object = MibTable
msgTrackResponseTable = _MsgTrackResponseTable_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4)
)
if mibBuilder.loadTexts:
    msgTrackResponseTable.setStatus("current")
_MsgTrackResponseEntry_Object = MibTableRow
msgTrackResponseEntry = _MsgTrackResponseEntry_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1)
)
msgTrackResponseEntry.setIndexNames(
    (0, "MESSAGE-TRACKING-MIB", "respEntryIndex"),
    (0, "MESSAGE-TRACKING-MIB", "respMsgIndex"),
)
if mibBuilder.loadTexts:
    msgTrackResponseEntry.setStatus("current")


class _RespEntryIndex_Type(Integer32):
    """Custom type respEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RespEntryIndex_Type.__name__ = "Integer32"
_RespEntryIndex_Object = MibTableColumn
respEntryIndex = _RespEntryIndex_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 1),
    _RespEntryIndex_Type()
)
respEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respEntryIndex.setStatus("current")


class _RespMsgIndex_Type(Integer32):
    """Custom type respMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RespMsgIndex_Type.__name__ = "Integer32"
_RespMsgIndex_Object = MibTableColumn
respMsgIndex = _RespMsgIndex_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 2),
    _RespMsgIndex_Type()
)
respMsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respMsgIndex.setStatus("current")
_RespDispositionStatus_Type = DispositionStatus
_RespDispositionStatus_Object = MibTableColumn
respDispositionStatus = _RespDispositionStatus_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 3),
    _RespDispositionStatus_Type()
)
respDispositionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respDispositionStatus.setStatus("current")
_RspDispositionTime_Type = DateAndTime
_RspDispositionTime_Object = MibScalar
rspDispositionTime = _RspDispositionTime_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 4),
    _RspDispositionTime_Type()
)
rspDispositionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rspDispositionTime.setStatus("current")
_RespNextHopMta_Type = DisplayString
_RespNextHopMta_Object = MibTableColumn
respNextHopMta = _RespNextHopMta_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 5),
    _RespNextHopMta_Type()
)
respNextHopMta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respNextHopMta.setStatus("current")
_RespPrevHopMta_Type = DisplayString
_RespPrevHopMta_Object = MibTableColumn
respPrevHopMta = _RespPrevHopMta_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 6),
    _RespPrevHopMta_Type()
)
respPrevHopMta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respPrevHopMta.setStatus("current")
_RespNonDeliveryReason_Type = DisplayString
_RespNonDeliveryReason_Object = MibTableColumn
respNonDeliveryReason = _RespNonDeliveryReason_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 7),
    _RespNonDeliveryReason_Type()
)
respNonDeliveryReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respNonDeliveryReason.setStatus("current")
_RespMsgArrivalTime_Type = DateAndTime
_RespMsgArrivalTime_Object = MibTableColumn
respMsgArrivalTime = _RespMsgArrivalTime_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 8),
    _RespMsgArrivalTime_Type()
)
respMsgArrivalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respMsgArrivalTime.setStatus("current")


class _RespMsgSize_Type(Integer32):
    """Custom type respMsgSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RespMsgSize_Type.__name__ = "Integer32"
_RespMsgSize_Object = MibTableColumn
respMsgSize = _RespMsgSize_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 9),
    _RespMsgSize_Type()
)
respMsgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respMsgSize.setStatus("current")
_RespMsgPriority_Type = DisplayString
_RespMsgPriority_Object = MibTableColumn
respMsgPriority = _RespMsgPriority_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 10),
    _RespMsgPriority_Type()
)
respMsgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respMsgPriority.setStatus("current")
_RespUniqueMsgId_Type = DisplayString
_RespUniqueMsgId_Object = MibTableColumn
respUniqueMsgId = _RespUniqueMsgId_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 11),
    _RespUniqueMsgId_Type()
)
respUniqueMsgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respUniqueMsgId.setStatus("current")
_RespInboundMsgId_Type = DisplayString
_RespInboundMsgId_Object = MibTableColumn
respInboundMsgId = _RespInboundMsgId_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 12),
    _RespInboundMsgId_Type()
)
respInboundMsgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respInboundMsgId.setStatus("current")
_RespOutboundMsgId_Type = DisplayString
_RespOutboundMsgId_Object = MibTableColumn
respOutboundMsgId = _RespOutboundMsgId_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 13),
    _RespOutboundMsgId_Type()
)
respOutboundMsgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respOutboundMsgId.setStatus("current")
_RespInboundOriginator_Type = DisplayString
_RespInboundOriginator_Object = MibTableColumn
respInboundOriginator = _RespInboundOriginator_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 14),
    _RespInboundOriginator_Type()
)
respInboundOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respInboundOriginator.setStatus("current")
_RespOutboundOriginator_Type = DisplayString
_RespOutboundOriginator_Object = MibTableColumn
respOutboundOriginator = _RespOutboundOriginator_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 15),
    _RespOutboundOriginator_Type()
)
respOutboundOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respOutboundOriginator.setStatus("current")
_RespInboundRecipient_Type = DisplayString
_RespInboundRecipient_Object = MibTableColumn
respInboundRecipient = _RespInboundRecipient_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 16),
    _RespInboundRecipient_Type()
)
respInboundRecipient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respInboundRecipient.setStatus("current")
_RespOutboundRecipient_Type = DisplayString
_RespOutboundRecipient_Object = MibTableColumn
respOutboundRecipient = _RespOutboundRecipient_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 17),
    _RespOutboundRecipient_Type()
)
respOutboundRecipient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respOutboundRecipient.setStatus("current")
_RespSupplementalInformation_Type = DisplayString
_RespSupplementalInformation_Object = MibTableColumn
respSupplementalInformation = _RespSupplementalInformation_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 18),
    _RespSupplementalInformation_Type()
)
respSupplementalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respSupplementalInformation.setStatus("current")
_RespSubject_Type = DisplayString
_RespSubject_Object = MibTableColumn
respSubject = _RespSubject_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 19),
    _RespSubject_Type()
)
respSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respSubject.setStatus("current")
_RespMsgType_Type = MsgType
_RespMsgType_Object = MibTableColumn
respMsgType = _RespMsgType_Object(
    (1, 3, 6, 1, 3, 73, 2, 1, 4, 1, 20),
    _RespMsgType_Type()
)
respMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respMsgType.setStatus("current")
_MessageTrackingConformance_ObjectIdentity = ObjectIdentity
messageTrackingConformance = _MessageTrackingConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 73, 2, 1, 5)
)
_MessageTrackingGroups_ObjectIdentity = ObjectIdentity
messageTrackingGroups = _MessageTrackingGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 73, 2, 1, 5, 1)
)
_MessageTrackingCompliances_ObjectIdentity = ObjectIdentity
messageTrackingCompliances = _MessageTrackingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 73, 2, 1, 5, 2)
)

# Managed Objects groups

msgIdGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 73, 2, 1, 5, 1, 1)
)
msgIdGroup.setObjects(
      *(("MESSAGE-TRACKING-MIB", "msgTrackNextRequestIndex"),
        ("MESSAGE-TRACKING-MIB", "reqRowStatus"),
        ("MESSAGE-TRACKING-MIB", "reqResponseStatus"),
        ("MESSAGE-TRACKING-MIB", "reqMaxResponses"),
        ("MESSAGE-TRACKING-MIB", "reqUniqueMsgId"),
        ("MESSAGE-TRACKING-MIB", "reqFailureReason"),
        ("MESSAGE-TRACKING-MIB", "respDispositionStatus"),
        ("MESSAGE-TRACKING-MIB", "respDispositionTime"),
        ("MESSAGE-TRACKING-MIB", "respNonDeliveryReason"),
        ("MESSAGE-TRACKING-MIB", "respMsgArrivalTime"),
        ("MESSAGE-TRACKING-MIB", "respUniqueMsgId"),
        ("MESSAGE-TRACKING-MIB", "respInboundOriginator"),
        ("MESSAGE-TRACKING-MIB", "respInboundRecipient"))
)
if mibBuilder.loadTexts:
    msgIdGroup.setStatus("current")

basicGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 73, 2, 1, 5, 1, 2)
)
basicGroup.setObjects(
      *(("MESSAGE-TRACKING-MIB", "reqInboundOriginator"),
        ("MESSAGE-TRACKING-MIB", "reqInboundRecipient"),
        ("MESSAGE-TRACKING-MIB", "reqOriginatorNameForm"),
        ("MESSAGE-TRACKING-MIB", "reqRecipientNameForm"),
        ("MESSAGE-TRACKING-MIB", "reqEarliestArrivalTime"),
        ("MESSAGE-TRACKING-MIB", "reqLatestArrivalTime"))
)
if mibBuilder.loadTexts:
    basicGroup.setStatus("current")

enhancedGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 73, 2, 1, 5, 1, 3)
)
enhancedGroup.setObjects(
      *(("MESSAGE-TRACKING-MIB", "reqSubject"),
        ("MESSAGE-TRACKING-MIB", "reqMinMsgSize"),
        ("MESSAGE-TRACKING-MIB", "reqMaxMsgSize"),
        ("MESSAGE-TRACKING-MIB", "reqDispositionStatus"),
        ("MESSAGE-TRACKING-MIB", "reqMsgType"),
        ("MESSAGE-TRACKING-MIB", "reqCollapseRecipients"),
        ("MESSAGE-TRACKING-MIB", "respMsgSize"),
        ("MESSAGE-TRACKING-MIB", "respMsgPriority"),
        ("MESSAGE-TRACKING-MIB", "respSupplementalInformation"),
        ("MESSAGE-TRACKING-MIB", "respSubject"),
        ("MESSAGE-TRACKING-MIB", "respMsgType"))
)
if mibBuilder.loadTexts:
    enhancedGroup.setStatus("current")

gatewayGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 73, 2, 1, 5, 1, 4)
)
gatewayGroup.setObjects(
      *(("MESSAGE-TRACKING-MIB", "reqInboundMsgId"),
        ("MESSAGE-TRACKING-MIB", "reqOutboundMsgId"),
        ("MESSAGE-TRACKING-MIB", "reqOutboundOriginator"),
        ("MESSAGE-TRACKING-MIB", "reqOutboundRecipient"),
        ("MESSAGE-TRACKING-MIB", "respNextHopMta"),
        ("MESSAGE-TRACKING-MIB", "respPrevHopMta"),
        ("MESSAGE-TRACKING-MIB", "respInboundMsgId"),
        ("MESSAGE-TRACKING-MIB", "respOutboundMsgId"),
        ("MESSAGE-TRACKING-MIB", "respOutboundOriginator"),
        ("MESSAGE-TRACKING-MIB", "respOutboundRecipient"))
)
if mibBuilder.loadTexts:
    gatewayGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

limitedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 73, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    limitedCompliance.setStatus(
        "current"
    )

basicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 73, 2, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )

enhancedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 73, 2, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    enhancedCompliance.setStatus(
        "current"
    )

gatewayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 73, 2, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    gatewayCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MESSAGE-TRACKING-MIB",
    **{"NameForm": NameForm,
       "DispositionStatus": DispositionStatus,
       "MsgType": MsgType,
       "msgTracking": msgTracking,
       "mta-message-track": mta_message_track,
       "mtaInformationTable": mtaInformationTable,
       "mtaInformationEntry": mtaInformationEntry,
       "mtaIndex": mtaIndex,
       "mtaName": mtaName,
       "mtaMessagingType": mtaMessagingType,
       "mtaStartTimeforRecordedInformation": mtaStartTimeforRecordedInformation,
       "mtaAlternativeAgent": mtaAlternativeAgent,
       "msgTrackNextRequestIndex": msgTrackNextRequestIndex,
       "msgTrackRequestTable": msgTrackRequestTable,
       "msgTrackRequestEntry": msgTrackRequestEntry,
       "reqEntryIndex": reqEntryIndex,
       "reqRowStatus": reqRowStatus,
       "reqResponseStatus": reqResponseStatus,
       "reqMaxResponses": reqMaxResponses,
       "reqUniqueMsgId": reqUniqueMsgId,
       "reqInboundMsgId": reqInboundMsgId,
       "reqOutboundMsgId": reqOutboundMsgId,
       "reqInboundOriginator": reqInboundOriginator,
       "reqOutboundOriginator": reqOutboundOriginator,
       "reqOriginatorNameForm": reqOriginatorNameForm,
       "reqInboundRecipient": reqInboundRecipient,
       "reqOutboundRecipient": reqOutboundRecipient,
       "reqRecipientNameForm": reqRecipientNameForm,
       "reqSubject": reqSubject,
       "reqMinMsgSize": reqMinMsgSize,
       "reqMaxMsgSize": reqMaxMsgSize,
       "reqEarliestArrivalTime": reqEarliestArrivalTime,
       "reqLatestArrivalTime": reqLatestArrivalTime,
       "reqDispositionStatus": reqDispositionStatus,
       "reqMsgType": reqMsgType,
       "reqCollapseRecipients": reqCollapseRecipients,
       "reqFailureReason": reqFailureReason,
       "msgTrackResponseTable": msgTrackResponseTable,
       "msgTrackResponseEntry": msgTrackResponseEntry,
       "respEntryIndex": respEntryIndex,
       "respMsgIndex": respMsgIndex,
       "respDispositionStatus": respDispositionStatus,
       "rspDispositionTime": rspDispositionTime,
       "respNextHopMta": respNextHopMta,
       "respPrevHopMta": respPrevHopMta,
       "respNonDeliveryReason": respNonDeliveryReason,
       "respMsgArrivalTime": respMsgArrivalTime,
       "respMsgSize": respMsgSize,
       "respMsgPriority": respMsgPriority,
       "respUniqueMsgId": respUniqueMsgId,
       "respInboundMsgId": respInboundMsgId,
       "respOutboundMsgId": respOutboundMsgId,
       "respInboundOriginator": respInboundOriginator,
       "respOutboundOriginator": respOutboundOriginator,
       "respInboundRecipient": respInboundRecipient,
       "respOutboundRecipient": respOutboundRecipient,
       "respSupplementalInformation": respSupplementalInformation,
       "respSubject": respSubject,
       "respMsgType": respMsgType,
       "messageTrackingConformance": messageTrackingConformance,
       "messageTrackingGroups": messageTrackingGroups,
       "msgIdGroup": msgIdGroup,
       "basicGroup": basicGroup,
       "enhancedGroup": enhancedGroup,
       "gatewayGroup": gatewayGroup,
       "messageTrackingCompliances": messageTrackingCompliances,
       "limitedCompliance": limitedCompliance,
       "basicCompliance": basicCompliance,
       "enhancedCompliance": enhancedCompliance,
       "gatewayCompliance": gatewayCompliance}
)

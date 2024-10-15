# SNMP MIB module (ASCEND-CALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-CALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:54 2024
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

(callStatusGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "callStatusGroup")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CallStatusMaximumEntries_Type = Integer32
_CallStatusMaximumEntries_Object = MibScalar
callStatusMaximumEntries = _CallStatusMaximumEntries_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 1),
    _CallStatusMaximumEntries_Type()
)
callStatusMaximumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusMaximumEntries.setStatus("mandatory")
_CallStatusTable_Object = MibTable
callStatusTable = _CallStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2)
)
if mibBuilder.loadTexts:
    callStatusTable.setStatus("mandatory")
_CallStatusEntry_Object = MibTableRow
callStatusEntry = _CallStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1)
)
callStatusEntry.setIndexNames(
    (0, "ASCEND-CALL-MIB", "callStatusIndex"),
)
if mibBuilder.loadTexts:
    callStatusEntry.setStatus("mandatory")
_CallStatusIndex_Type = Integer32
_CallStatusIndex_Object = MibTableColumn
callStatusIndex = _CallStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 1),
    _CallStatusIndex_Type()
)
callStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusIndex.setStatus("mandatory")


class _CallStatusValidFlag_Type(Integer32):
    """Custom type callStatusValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CallStatusValidFlag_Type.__name__ = "Integer32"
_CallStatusValidFlag_Object = MibTableColumn
callStatusValidFlag = _CallStatusValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 2),
    _CallStatusValidFlag_Type()
)
callStatusValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusValidFlag.setStatus("mandatory")
_CallStatusStartingTimeStamp_Type = Integer32
_CallStatusStartingTimeStamp_Object = MibTableColumn
callStatusStartingTimeStamp = _CallStatusStartingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 3),
    _CallStatusStartingTimeStamp_Type()
)
callStatusStartingTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusStartingTimeStamp.setStatus("mandatory")
_CallStatusCallReferenceNum_Type = Integer32
_CallStatusCallReferenceNum_Object = MibTableColumn
callStatusCallReferenceNum = _CallStatusCallReferenceNum_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 4),
    _CallStatusCallReferenceNum_Type()
)
callStatusCallReferenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusCallReferenceNum.setStatus("mandatory")
_CallStatusDataRate_Type = Integer32
_CallStatusDataRate_Object = MibTableColumn
callStatusDataRate = _CallStatusDataRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 5),
    _CallStatusDataRate_Type()
)
callStatusDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusDataRate.setStatus("mandatory")
_CallStatusSlotNumber_Type = Integer32
_CallStatusSlotNumber_Object = MibTableColumn
callStatusSlotNumber = _CallStatusSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 6),
    _CallStatusSlotNumber_Type()
)
callStatusSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusSlotNumber.setStatus("mandatory")
_CallStatusSlotLineNumber_Type = Integer32
_CallStatusSlotLineNumber_Object = MibTableColumn
callStatusSlotLineNumber = _CallStatusSlotLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 7),
    _CallStatusSlotLineNumber_Type()
)
callStatusSlotLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusSlotLineNumber.setStatus("mandatory")
_CallStatusSlotChannelNumber_Type = Integer32
_CallStatusSlotChannelNumber_Object = MibTableColumn
callStatusSlotChannelNumber = _CallStatusSlotChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 8),
    _CallStatusSlotChannelNumber_Type()
)
callStatusSlotChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusSlotChannelNumber.setStatus("mandatory")
_CallStatusModemSlotNumber_Type = Integer32
_CallStatusModemSlotNumber_Object = MibTableColumn
callStatusModemSlotNumber = _CallStatusModemSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 9),
    _CallStatusModemSlotNumber_Type()
)
callStatusModemSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusModemSlotNumber.setStatus("mandatory")
_CallStatusModemOnSlot_Type = Integer32
_CallStatusModemOnSlot_Object = MibTableColumn
callStatusModemOnSlot = _CallStatusModemOnSlot_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 10),
    _CallStatusModemOnSlot_Type()
)
callStatusModemOnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusModemOnSlot.setStatus("mandatory")
_CallStatusIfIndex_Type = Integer32
_CallStatusIfIndex_Object = MibTableColumn
callStatusIfIndex = _CallStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 11),
    _CallStatusIfIndex_Type()
)
callStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusIfIndex.setStatus("mandatory")
_CallSessionIndex_Type = Integer32
_CallSessionIndex_Object = MibTableColumn
callSessionIndex = _CallSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 12),
    _CallSessionIndex_Type()
)
callSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSessionIndex.setStatus("mandatory")


class _CallStatusType_Type(Integer32):
    """Custom type callStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("callIncoming", 2),
          ("callOutgoing", 1))
    )


_CallStatusType_Type.__name__ = "Integer32"
_CallStatusType_Object = MibTableColumn
callStatusType = _CallStatusType_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 13),
    _CallStatusType_Type()
)
callStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusType.setStatus("mandatory")
_CallStatusXmitRate_Type = Integer32
_CallStatusXmitRate_Object = MibTableColumn
callStatusXmitRate = _CallStatusXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 14),
    _CallStatusXmitRate_Type()
)
callStatusXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusXmitRate.setStatus("mandatory")


class _CallStatusPortType_Type(Integer32):
    """Custom type callStatusPortType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("callPortAsync", 2),
          ("callPortISDNAsyncV110", 6),
          ("callPortISDNAsyncV120", 5),
          ("callPortISDNAsyncV32", 8),
          ("callPortISDNAsyncVDSP", 9),
          ("callPortISDNSync", 4),
          ("callPortSync", 3),
          ("callPortUnknown", 1),
          ("callPortVirtual", 7))
    )


_CallStatusPortType_Type.__name__ = "Integer32"
_CallStatusPortType_Object = MibTableColumn
callStatusPortType = _CallStatusPortType_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 15),
    _CallStatusPortType_Type()
)
callStatusPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusPortType.setStatus("mandatory")
_CallStatusCalledParyID_Type = DisplayString
_CallStatusCalledParyID_Object = MibTableColumn
callStatusCalledParyID = _CallStatusCalledParyID_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 16),
    _CallStatusCalledParyID_Type()
)
callStatusCalledParyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusCalledParyID.setStatus("mandatory")
_CallStatusCallingPartyID_Type = DisplayString
_CallStatusCallingPartyID_Object = MibTableColumn
callStatusCallingPartyID = _CallStatusCallingPartyID_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 17),
    _CallStatusCallingPartyID_Type()
)
callStatusCallingPartyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusCallingPartyID.setStatus("mandatory")
_CallStatusMultiLinkID_Type = Integer32
_CallStatusMultiLinkID_Object = MibTableColumn
callStatusMultiLinkID = _CallStatusMultiLinkID_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 2, 1, 18),
    _CallStatusMultiLinkID_Type()
)
callStatusMultiLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callStatusMultiLinkID.setStatus("mandatory")
_CallStatusHighWaterMark_Type = Integer32
_CallStatusHighWaterMark_Object = MibScalar
callStatusHighWaterMark = _CallStatusHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 3),
    _CallStatusHighWaterMark_Type()
)
callStatusHighWaterMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callStatusHighWaterMark.setStatus("mandatory")
_CallCurrentAnalogOutgoing_Type = Integer32
_CallCurrentAnalogOutgoing_Object = MibScalar
callCurrentAnalogOutgoing = _CallCurrentAnalogOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 4),
    _CallCurrentAnalogOutgoing_Type()
)
callCurrentAnalogOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callCurrentAnalogOutgoing.setStatus("mandatory")
_CallCurrentAnalogIncoming_Type = Integer32
_CallCurrentAnalogIncoming_Object = MibScalar
callCurrentAnalogIncoming = _CallCurrentAnalogIncoming_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 5),
    _CallCurrentAnalogIncoming_Type()
)
callCurrentAnalogIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callCurrentAnalogIncoming.setStatus("mandatory")
_CallCurrentDigitalOutgoing_Type = Integer32
_CallCurrentDigitalOutgoing_Object = MibScalar
callCurrentDigitalOutgoing = _CallCurrentDigitalOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 6),
    _CallCurrentDigitalOutgoing_Type()
)
callCurrentDigitalOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callCurrentDigitalOutgoing.setStatus("mandatory")
_CallCurrentDigitalIncoming_Type = Integer32
_CallCurrentDigitalIncoming_Object = MibScalar
callCurrentDigitalIncoming = _CallCurrentDigitalIncoming_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 7),
    _CallCurrentDigitalIncoming_Type()
)
callCurrentDigitalIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callCurrentDigitalIncoming.setStatus("mandatory")
_CallCurrentFROutgoing_Type = Integer32
_CallCurrentFROutgoing_Object = MibScalar
callCurrentFROutgoing = _CallCurrentFROutgoing_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 8),
    _CallCurrentFROutgoing_Type()
)
callCurrentFROutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callCurrentFROutgoing.setStatus("mandatory")
_CallCurrentFRIncoming_Type = Integer32
_CallCurrentFRIncoming_Object = MibScalar
callCurrentFRIncoming = _CallCurrentFRIncoming_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 9),
    _CallCurrentFRIncoming_Type()
)
callCurrentFRIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callCurrentFRIncoming.setStatus("mandatory")
_CallTotalAnalogOutgoing_Type = Integer32
_CallTotalAnalogOutgoing_Object = MibScalar
callTotalAnalogOutgoing = _CallTotalAnalogOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 10),
    _CallTotalAnalogOutgoing_Type()
)
callTotalAnalogOutgoing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callTotalAnalogOutgoing.setStatus("mandatory")
_CallTotalAnalogIncoming_Type = Integer32
_CallTotalAnalogIncoming_Object = MibScalar
callTotalAnalogIncoming = _CallTotalAnalogIncoming_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 11),
    _CallTotalAnalogIncoming_Type()
)
callTotalAnalogIncoming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callTotalAnalogIncoming.setStatus("mandatory")
_CallTotalDigitalOutgoing_Type = Integer32
_CallTotalDigitalOutgoing_Object = MibScalar
callTotalDigitalOutgoing = _CallTotalDigitalOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 12),
    _CallTotalDigitalOutgoing_Type()
)
callTotalDigitalOutgoing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callTotalDigitalOutgoing.setStatus("mandatory")
_CallTotalDigitalIncoming_Type = Integer32
_CallTotalDigitalIncoming_Object = MibScalar
callTotalDigitalIncoming = _CallTotalDigitalIncoming_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 13),
    _CallTotalDigitalIncoming_Type()
)
callTotalDigitalIncoming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callTotalDigitalIncoming.setStatus("mandatory")
_CallTotalFROutgoing_Type = Integer32
_CallTotalFROutgoing_Object = MibScalar
callTotalFROutgoing = _CallTotalFROutgoing_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 14),
    _CallTotalFROutgoing_Type()
)
callTotalFROutgoing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callTotalFROutgoing.setStatus("mandatory")
_CallTotalFRIncoming_Type = Integer32
_CallTotalFRIncoming_Object = MibScalar
callTotalFRIncoming = _CallTotalFRIncoming_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 15),
    _CallTotalFRIncoming_Type()
)
callTotalFRIncoming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callTotalFRIncoming.setStatus("mandatory")
_CallActiveTable_Object = MibTable
callActiveTable = _CallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16)
)
if mibBuilder.loadTexts:
    callActiveTable.setStatus("mandatory")
_CallActiveEntry_Object = MibTableRow
callActiveEntry = _CallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1)
)
callActiveEntry.setIndexNames(
    (0, "ASCEND-CALL-MIB", "callActiveCallReferenceNum"),
)
if mibBuilder.loadTexts:
    callActiveEntry.setStatus("mandatory")
_CallActiveCallReferenceNum_Type = Integer32
_CallActiveCallReferenceNum_Object = MibTableColumn
callActiveCallReferenceNum = _CallActiveCallReferenceNum_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 1),
    _CallActiveCallReferenceNum_Type()
)
callActiveCallReferenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallReferenceNum.setStatus("mandatory")
_CallActiveIndex_Type = Integer32
_CallActiveIndex_Object = MibTableColumn
callActiveIndex = _CallActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 2),
    _CallActiveIndex_Type()
)
callActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveIndex.setStatus("mandatory")


class _CallActiveValidFlag_Type(Integer32):
    """Custom type callActiveValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CallActiveValidFlag_Type.__name__ = "Integer32"
_CallActiveValidFlag_Object = MibTableColumn
callActiveValidFlag = _CallActiveValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 3),
    _CallActiveValidFlag_Type()
)
callActiveValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveValidFlag.setStatus("mandatory")
_CallActiveStartingTimeStamp_Type = Integer32
_CallActiveStartingTimeStamp_Object = MibTableColumn
callActiveStartingTimeStamp = _CallActiveStartingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 4),
    _CallActiveStartingTimeStamp_Type()
)
callActiveStartingTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveStartingTimeStamp.setStatus("mandatory")
_CallActiveDataRate_Type = Integer32
_CallActiveDataRate_Object = MibTableColumn
callActiveDataRate = _CallActiveDataRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 5),
    _CallActiveDataRate_Type()
)
callActiveDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveDataRate.setStatus("mandatory")
_CallActiveSlotNumber_Type = Integer32
_CallActiveSlotNumber_Object = MibTableColumn
callActiveSlotNumber = _CallActiveSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 6),
    _CallActiveSlotNumber_Type()
)
callActiveSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveSlotNumber.setStatus("mandatory")
_CallActiveSlotLineNumber_Type = Integer32
_CallActiveSlotLineNumber_Object = MibTableColumn
callActiveSlotLineNumber = _CallActiveSlotLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 7),
    _CallActiveSlotLineNumber_Type()
)
callActiveSlotLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveSlotLineNumber.setStatus("mandatory")
_CallActiveSlotChannelNumber_Type = Integer32
_CallActiveSlotChannelNumber_Object = MibTableColumn
callActiveSlotChannelNumber = _CallActiveSlotChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 8),
    _CallActiveSlotChannelNumber_Type()
)
callActiveSlotChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveSlotChannelNumber.setStatus("mandatory")
_CallActiveModemSlotNumber_Type = Integer32
_CallActiveModemSlotNumber_Object = MibTableColumn
callActiveModemSlotNumber = _CallActiveModemSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 9),
    _CallActiveModemSlotNumber_Type()
)
callActiveModemSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveModemSlotNumber.setStatus("mandatory")
_CallActiveModemOnSlot_Type = Integer32
_CallActiveModemOnSlot_Object = MibTableColumn
callActiveModemOnSlot = _CallActiveModemOnSlot_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 10),
    _CallActiveModemOnSlot_Type()
)
callActiveModemOnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveModemOnSlot.setStatus("mandatory")
_CallActiveIfIndex_Type = Integer32
_CallActiveIfIndex_Object = MibTableColumn
callActiveIfIndex = _CallActiveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 11),
    _CallActiveIfIndex_Type()
)
callActiveIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveIfIndex.setStatus("mandatory")
_CallActiveSessionIndex_Type = Integer32
_CallActiveSessionIndex_Object = MibTableColumn
callActiveSessionIndex = _CallActiveSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 12),
    _CallActiveSessionIndex_Type()
)
callActiveSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveSessionIndex.setStatus("mandatory")


class _CallActiveType_Type(Integer32):
    """Custom type callActiveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("callIncoming", 2),
          ("callOutgoing", 1))
    )


_CallActiveType_Type.__name__ = "Integer32"
_CallActiveType_Object = MibTableColumn
callActiveType = _CallActiveType_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 13),
    _CallActiveType_Type()
)
callActiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveType.setStatus("mandatory")
_CallActiveXmitRate_Type = Integer32
_CallActiveXmitRate_Object = MibTableColumn
callActiveXmitRate = _CallActiveXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 14),
    _CallActiveXmitRate_Type()
)
callActiveXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveXmitRate.setStatus("mandatory")


class _CallActivePortType_Type(Integer32):
    """Custom type callActivePortType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("callPortAsync", 2),
          ("callPortISDNAsyncV110", 6),
          ("callPortISDNAsyncV120", 5),
          ("callPortISDNAsyncV32", 8),
          ("callPortISDNAsyncVDSP", 9),
          ("callPortISDNSync", 4),
          ("callPortSync", 3),
          ("callPortUnknown", 1),
          ("callPortVirtual", 7))
    )


_CallActivePortType_Type.__name__ = "Integer32"
_CallActivePortType_Object = MibTableColumn
callActivePortType = _CallActivePortType_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 15),
    _CallActivePortType_Type()
)
callActivePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActivePortType.setStatus("mandatory")
_CallActiveCalledParyID_Type = DisplayString
_CallActiveCalledParyID_Object = MibTableColumn
callActiveCalledParyID = _CallActiveCalledParyID_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 16),
    _CallActiveCalledParyID_Type()
)
callActiveCalledParyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCalledParyID.setStatus("mandatory")
_CallActiveCallingPartyID_Type = DisplayString
_CallActiveCallingPartyID_Object = MibTableColumn
callActiveCallingPartyID = _CallActiveCallingPartyID_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 17),
    _CallActiveCallingPartyID_Type()
)
callActiveCallingPartyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallingPartyID.setStatus("mandatory")
_CallActiveMultiLinkID_Type = Integer32
_CallActiveMultiLinkID_Object = MibTableColumn
callActiveMultiLinkID = _CallActiveMultiLinkID_Object(
    (1, 3, 6, 1, 4, 1, 529, 11, 16, 1, 18),
    _CallActiveMultiLinkID_Type()
)
callActiveMultiLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveMultiLinkID.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-CALL-MIB",
    **{"callStatusMaximumEntries": callStatusMaximumEntries,
       "callStatusTable": callStatusTable,
       "callStatusEntry": callStatusEntry,
       "callStatusIndex": callStatusIndex,
       "callStatusValidFlag": callStatusValidFlag,
       "callStatusStartingTimeStamp": callStatusStartingTimeStamp,
       "callStatusCallReferenceNum": callStatusCallReferenceNum,
       "callStatusDataRate": callStatusDataRate,
       "callStatusSlotNumber": callStatusSlotNumber,
       "callStatusSlotLineNumber": callStatusSlotLineNumber,
       "callStatusSlotChannelNumber": callStatusSlotChannelNumber,
       "callStatusModemSlotNumber": callStatusModemSlotNumber,
       "callStatusModemOnSlot": callStatusModemOnSlot,
       "callStatusIfIndex": callStatusIfIndex,
       "callSessionIndex": callSessionIndex,
       "callStatusType": callStatusType,
       "callStatusXmitRate": callStatusXmitRate,
       "callStatusPortType": callStatusPortType,
       "callStatusCalledParyID": callStatusCalledParyID,
       "callStatusCallingPartyID": callStatusCallingPartyID,
       "callStatusMultiLinkID": callStatusMultiLinkID,
       "callStatusHighWaterMark": callStatusHighWaterMark,
       "callCurrentAnalogOutgoing": callCurrentAnalogOutgoing,
       "callCurrentAnalogIncoming": callCurrentAnalogIncoming,
       "callCurrentDigitalOutgoing": callCurrentDigitalOutgoing,
       "callCurrentDigitalIncoming": callCurrentDigitalIncoming,
       "callCurrentFROutgoing": callCurrentFROutgoing,
       "callCurrentFRIncoming": callCurrentFRIncoming,
       "callTotalAnalogOutgoing": callTotalAnalogOutgoing,
       "callTotalAnalogIncoming": callTotalAnalogIncoming,
       "callTotalDigitalOutgoing": callTotalDigitalOutgoing,
       "callTotalDigitalIncoming": callTotalDigitalIncoming,
       "callTotalFROutgoing": callTotalFROutgoing,
       "callTotalFRIncoming": callTotalFRIncoming,
       "callActiveTable": callActiveTable,
       "callActiveEntry": callActiveEntry,
       "callActiveCallReferenceNum": callActiveCallReferenceNum,
       "callActiveIndex": callActiveIndex,
       "callActiveValidFlag": callActiveValidFlag,
       "callActiveStartingTimeStamp": callActiveStartingTimeStamp,
       "callActiveDataRate": callActiveDataRate,
       "callActiveSlotNumber": callActiveSlotNumber,
       "callActiveSlotLineNumber": callActiveSlotLineNumber,
       "callActiveSlotChannelNumber": callActiveSlotChannelNumber,
       "callActiveModemSlotNumber": callActiveModemSlotNumber,
       "callActiveModemOnSlot": callActiveModemOnSlot,
       "callActiveIfIndex": callActiveIfIndex,
       "callActiveSessionIndex": callActiveSessionIndex,
       "callActiveType": callActiveType,
       "callActiveXmitRate": callActiveXmitRate,
       "callActivePortType": callActivePortType,
       "callActiveCalledParyID": callActiveCalledParyID,
       "callActiveCallingPartyID": callActiveCallingPartyID,
       "callActiveMultiLinkID": callActiveMultiLinkID}
)

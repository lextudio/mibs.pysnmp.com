# SNMP MIB module (BCS-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BCS-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:21 2024
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

(bcs,) = mibBuilder.importSymbols(
    "BCS-IDENT-MIB",
    "bcs")

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

bcsTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigChangeState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applied", 2),
          ("saved", 3),
          ("staged", 1))
    )



class ConfigChangeAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("waitingReboot", 3),
          ("waitingRetune", 1),
          ("waitingSave", 2))
    )



# MIB Managed Objects in the order of their OIDs

_BcsTrapElements_ObjectIdentity = ObjectIdentity
bcsTrapElements = _BcsTrapElements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1)
)


class _TrapIdentifier_Type(Integer32):
    """Custom type trapIdentifier based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapIdentifier_Type.__name__ = "Integer32"
_TrapIdentifier_Object = MibScalar
trapIdentifier = _TrapIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 1),
    _TrapIdentifier_Type()
)
trapIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIdentifier.setStatus("current")


class _TrapSequenceId_Type(Integer32):
    """Custom type trapSequenceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapSequenceId_Type.__name__ = "Integer32"
_TrapSequenceId_Object = MibScalar
trapSequenceId = _TrapSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 2),
    _TrapSequenceId_Type()
)
trapSequenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSequenceId.setStatus("current")
_TrapNetworkElemModelNumber_Type = DisplayString
_TrapNetworkElemModelNumber_Object = MibScalar
trapNetworkElemModelNumber = _TrapNetworkElemModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 3),
    _TrapNetworkElemModelNumber_Type()
)
trapNetworkElemModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemModelNumber.setStatus("current")
_TrapNetworkElemSerialNum_Type = DisplayString
_TrapNetworkElemSerialNum_Object = MibScalar
trapNetworkElemSerialNum = _TrapNetworkElemSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 4),
    _TrapNetworkElemSerialNum_Type()
)
trapNetworkElemSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemSerialNum.setStatus("current")


class _TrapPerceivedSeverity_Type(Integer32):
    """Custom type trapPerceivedSeverity based on Integer32"""
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
        *(("cleared", 1),
          ("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_TrapPerceivedSeverity_Type.__name__ = "Integer32"
_TrapPerceivedSeverity_Object = MibScalar
trapPerceivedSeverity = _TrapPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 5),
    _TrapPerceivedSeverity_Type()
)
trapPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPerceivedSeverity.setStatus("current")


class _TrapNetworkElemOperState_Type(Integer32):
    """Custom type trapNetworkElemOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TrapNetworkElemOperState_Type.__name__ = "Integer32"
_TrapNetworkElemOperState_Object = MibScalar
trapNetworkElemOperState = _TrapNetworkElemOperState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 6),
    _TrapNetworkElemOperState_Type()
)
trapNetworkElemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemOperState.setStatus("current")


class _TrapNetworkElemAlarmStatus_Type(Integer32):
    """Custom type trapNetworkElemAlarmStatus based on Integer32"""
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
        *(("critical", 6),
          ("idle", 1),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_TrapNetworkElemAlarmStatus_Type.__name__ = "Integer32"
_TrapNetworkElemAlarmStatus_Object = MibScalar
trapNetworkElemAlarmStatus = _TrapNetworkElemAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 7),
    _TrapNetworkElemAlarmStatus_Type()
)
trapNetworkElemAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemAlarmStatus.setStatus("current")


class _TrapNetworkElemAdminState_Type(Integer32):
    """Custom type trapNetworkElemAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("shuttingDown", 3),
          ("unlocked", 2))
    )


_TrapNetworkElemAdminState_Type.__name__ = "Integer32"
_TrapNetworkElemAdminState_Object = MibScalar
trapNetworkElemAdminState = _TrapNetworkElemAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 8),
    _TrapNetworkElemAdminState_Type()
)
trapNetworkElemAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemAdminState.setStatus("current")


class _TrapNetworkElemAvailStatus_Type(Integer32):
    """Custom type trapNetworkElemAvailStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("available", 10),
          ("degraded", 7),
          ("dependency", 6),
          ("failed", 2),
          ("inTest", 1),
          ("logFull", 9),
          ("notInstalled", 8),
          ("offDuty", 5),
          ("offLine", 4),
          ("powerOff", 3))
    )


_TrapNetworkElemAvailStatus_Type.__name__ = "Integer32"
_TrapNetworkElemAvailStatus_Object = MibScalar
trapNetworkElemAvailStatus = _TrapNetworkElemAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 9),
    _TrapNetworkElemAvailStatus_Type()
)
trapNetworkElemAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemAvailStatus.setStatus("current")
_TrapText_Type = DisplayString
_TrapText_Object = MibScalar
trapText = _TrapText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 10),
    _TrapText_Type()
)
trapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapText.setStatus("current")
_TrapNETrapLastTrapTimeStamp_Type = TimeTicks
_TrapNETrapLastTrapTimeStamp_Object = MibScalar
trapNETrapLastTrapTimeStamp = _TrapNETrapLastTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 11),
    _TrapNETrapLastTrapTimeStamp_Type()
)
trapNETrapLastTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNETrapLastTrapTimeStamp.setStatus("current")
_TrapChangedObjectId_Type = ObjectIdentifier
_TrapChangedObjectId_Object = MibScalar
trapChangedObjectId = _TrapChangedObjectId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 12),
    _TrapChangedObjectId_Type()
)
trapChangedObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChangedObjectId.setStatus("current")


class _TrapAdditionalInfoInteger1_Type(Integer32):
    """Custom type trapAdditionalInfoInteger1 based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapAdditionalInfoInteger1_Type.__name__ = "Integer32"
_TrapAdditionalInfoInteger1_Object = MibScalar
trapAdditionalInfoInteger1 = _TrapAdditionalInfoInteger1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 13),
    _TrapAdditionalInfoInteger1_Type()
)
trapAdditionalInfoInteger1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAdditionalInfoInteger1.setStatus("current")


class _TrapAdditionalInfoInteger2_Type(Integer32):
    """Custom type trapAdditionalInfoInteger2 based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapAdditionalInfoInteger2_Type.__name__ = "Integer32"
_TrapAdditionalInfoInteger2_Object = MibScalar
trapAdditionalInfoInteger2 = _TrapAdditionalInfoInteger2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 14),
    _TrapAdditionalInfoInteger2_Type()
)
trapAdditionalInfoInteger2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAdditionalInfoInteger2.setStatus("current")


class _TrapAdditionalInfoInteger3_Type(Integer32):
    """Custom type trapAdditionalInfoInteger3 based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapAdditionalInfoInteger3_Type.__name__ = "Integer32"
_TrapAdditionalInfoInteger3_Object = MibScalar
trapAdditionalInfoInteger3 = _TrapAdditionalInfoInteger3_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 15),
    _TrapAdditionalInfoInteger3_Type()
)
trapAdditionalInfoInteger3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAdditionalInfoInteger3.setStatus("current")
_TrapChangedValueDisplayString_Type = DisplayString
_TrapChangedValueDisplayString_Object = MibScalar
trapChangedValueDisplayString = _TrapChangedValueDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 16),
    _TrapChangedValueDisplayString_Type()
)
trapChangedValueDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChangedValueDisplayString.setStatus("current")
_TrapChangedValueOID_Type = DisplayString
_TrapChangedValueOID_Object = MibScalar
trapChangedValueOID = _TrapChangedValueOID_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 17),
    _TrapChangedValueOID_Type()
)
trapChangedValueOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChangedValueOID.setStatus("current")
_TrapChangedValueIpAddress_Type = IpAddress
_TrapChangedValueIpAddress_Object = MibScalar
trapChangedValueIpAddress = _TrapChangedValueIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 18),
    _TrapChangedValueIpAddress_Type()
)
trapChangedValueIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChangedValueIpAddress.setStatus("current")


class _TrapChangedValueInteger_Type(Integer32):
    """Custom type trapChangedValueInteger based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapChangedValueInteger_Type.__name__ = "Integer32"
_TrapChangedValueInteger_Object = MibScalar
trapChangedValueInteger = _TrapChangedValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 19),
    _TrapChangedValueInteger_Type()
)
trapChangedValueInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChangedValueInteger.setStatus("current")
_BcsTrapControl_ObjectIdentity = ObjectIdentity
bcsTrapControl = _BcsTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2)
)


class _NumberOfTrapReceivers_Type(Integer32):
    """Custom type numberOfTrapReceivers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NumberOfTrapReceivers_Type.__name__ = "Integer32"
_NumberOfTrapReceivers_Object = MibScalar
numberOfTrapReceivers = _NumberOfTrapReceivers_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 1),
    _NumberOfTrapReceivers_Type()
)
numberOfTrapReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfTrapReceivers.setStatus("current")
_TrapReceiversTable_Object = MibTable
trapReceiversTable = _TrapReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2)
)
if mibBuilder.loadTexts:
    trapReceiversTable.setStatus("current")
_TrapReceiversEntry_Object = MibTableRow
trapReceiversEntry = _TrapReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1)
)
trapReceiversEntry.setIndexNames(
    (0, "BCS-TRAPS-MIB", "trapReceiversTableIndex"),
)
if mibBuilder.loadTexts:
    trapReceiversEntry.setStatus("current")


class _TrapReceiversTableIndex_Type(Integer32):
    """Custom type trapReceiversTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TrapReceiversTableIndex_Type.__name__ = "Integer32"
_TrapReceiversTableIndex_Object = MibTableColumn
trapReceiversTableIndex = _TrapReceiversTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 1),
    _TrapReceiversTableIndex_Type()
)
trapReceiversTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapReceiversTableIndex.setStatus("current")
_TrapReceiverAddr_Type = IpAddress
_TrapReceiverAddr_Object = MibTableColumn
trapReceiverAddr = _TrapReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 2),
    _TrapReceiverAddr_Type()
)
trapReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverAddr.setStatus("current")
_TrapReceiverCommunityString_Type = DisplayString
_TrapReceiverCommunityString_Object = MibTableColumn
trapReceiverCommunityString = _TrapReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 3),
    _TrapReceiverCommunityString_Type()
)
trapReceiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverCommunityString.setStatus("current")


class _TrapToBeSendQueueSize_Type(Integer32):
    """Custom type trapToBeSendQueueSize based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000),
    )


_TrapToBeSendQueueSize_Type.__name__ = "Integer32"
_TrapToBeSendQueueSize_Object = MibTableColumn
trapToBeSendQueueSize = _TrapToBeSendQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 4),
    _TrapToBeSendQueueSize_Type()
)
trapToBeSendQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapToBeSendQueueSize.setStatus("current")


class _TrapSentQueueSize_Type(Integer32):
    """Custom type trapSentQueueSize based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 300),
    )


_TrapSentQueueSize_Type.__name__ = "Integer32"
_TrapSentQueueSize_Object = MibTableColumn
trapSentQueueSize = _TrapSentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 5),
    _TrapSentQueueSize_Type()
)
trapSentQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSentQueueSize.setStatus("current")


class _TrapThrottlingRate_Type(Integer32):
    """Custom type trapThrottlingRate based on Integer32"""
    defaultValue = 1


_TrapThrottlingRate_Object = MibTableColumn
trapThrottlingRate = _TrapThrottlingRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 6),
    _TrapThrottlingRate_Type()
)
trapThrottlingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapThrottlingRate.setStatus("current")


class _TrapLastSent_Type(Integer32):
    """Custom type trapLastSent based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapLastSent_Type.__name__ = "Integer32"
_TrapLastSent_Object = MibTableColumn
trapLastSent = _TrapLastSent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 7),
    _TrapLastSent_Type()
)
trapLastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLastSent.setStatus("current")


class _TrapReceiversEntryOperState_Type(Integer32):
    """Custom type trapReceiversEntryOperState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TrapReceiversEntryOperState_Type.__name__ = "Integer32"
_TrapReceiversEntryOperState_Object = MibTableColumn
trapReceiversEntryOperState = _TrapReceiversEntryOperState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 8),
    _TrapReceiversEntryOperState_Type()
)
trapReceiversEntryOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiversEntryOperState.setStatus("current")


class _TrapResendRequest_Type(Integer32):
    """Custom type trapResendRequest based on Integer32"""
    defaultValue = 2147483647


_TrapResendRequest_Object = MibTableColumn
trapResendRequest = _TrapResendRequest_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 9),
    _TrapResendRequest_Type()
)
trapResendRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapResendRequest.setStatus("current")


class _NumberOfDiscriminators_Type(Integer32):
    """Custom type numberOfDiscriminators based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NumberOfDiscriminators_Type.__name__ = "Integer32"
_NumberOfDiscriminators_Object = MibScalar
numberOfDiscriminators = _NumberOfDiscriminators_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 3),
    _NumberOfDiscriminators_Type()
)
numberOfDiscriminators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfDiscriminators.setStatus("current")
_TrapDiscrimTable_Object = MibTable
trapDiscrimTable = _TrapDiscrimTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4)
)
if mibBuilder.loadTexts:
    trapDiscrimTable.setStatus("current")
_TrapDiscrimEntry_Object = MibTableRow
trapDiscrimEntry = _TrapDiscrimEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1)
)
trapDiscrimEntry.setIndexNames(
    (0, "BCS-TRAPS-MIB", "trapDiscrimTableIndex"),
)
if mibBuilder.loadTexts:
    trapDiscrimEntry.setStatus("current")


class _TrapDiscrimTableIndex_Type(Integer32):
    """Custom type trapDiscrimTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TrapDiscrimTableIndex_Type.__name__ = "Integer32"
_TrapDiscrimTableIndex_Object = MibTableColumn
trapDiscrimTableIndex = _TrapDiscrimTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 1),
    _TrapDiscrimTableIndex_Type()
)
trapDiscrimTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDiscrimTableIndex.setStatus("current")
_TrapDiscrimReceiverAddr_Type = IpAddress
_TrapDiscrimReceiverAddr_Object = MibTableColumn
trapDiscrimReceiverAddr = _TrapDiscrimReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 2),
    _TrapDiscrimReceiverAddr_Type()
)
trapDiscrimReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimReceiverAddr.setStatus("current")


class _TrapDiscrimAvailabilityStatus_Type(Integer32):
    """Custom type trapDiscrimAvailabilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10)
        )
    )
    namedValues = NamedValues(
        *(("available", 10),
          ("offDuty", 5))
    )


_TrapDiscrimAvailabilityStatus_Type.__name__ = "Integer32"
_TrapDiscrimAvailabilityStatus_Object = MibTableColumn
trapDiscrimAvailabilityStatus = _TrapDiscrimAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 3),
    _TrapDiscrimAvailabilityStatus_Type()
)
trapDiscrimAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDiscrimAvailabilityStatus.setStatus("current")


class _TrapDiscrimWeeklyMask_Type(DisplayString):
    """Custom type trapDiscrimWeeklyMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_TrapDiscrimWeeklyMask_Type.__name__ = "DisplayString"
_TrapDiscrimWeeklyMask_Object = MibTableColumn
trapDiscrimWeeklyMask = _TrapDiscrimWeeklyMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 4),
    _TrapDiscrimWeeklyMask_Type()
)
trapDiscrimWeeklyMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimWeeklyMask.setStatus("current")


class _TrapDiscrimDailyStartTime_Type(Integer32):
    """Custom type trapDiscrimDailyStartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_TrapDiscrimDailyStartTime_Type.__name__ = "Integer32"
_TrapDiscrimDailyStartTime_Object = MibTableColumn
trapDiscrimDailyStartTime = _TrapDiscrimDailyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 5),
    _TrapDiscrimDailyStartTime_Type()
)
trapDiscrimDailyStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimDailyStartTime.setStatus("current")


class _TrapDiscrimDailyStopTime_Type(Integer32):
    """Custom type trapDiscrimDailyStopTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_TrapDiscrimDailyStopTime_Type.__name__ = "Integer32"
_TrapDiscrimDailyStopTime_Object = MibTableColumn
trapDiscrimDailyStopTime = _TrapDiscrimDailyStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 6),
    _TrapDiscrimDailyStopTime_Type()
)
trapDiscrimDailyStopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimDailyStopTime.setStatus("current")


class _TrapSeverityDiscrim_Type(Integer32):
    """Custom type trapSeverityDiscrim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_TrapSeverityDiscrim_Type.__name__ = "Integer32"
_TrapSeverityDiscrim_Object = MibTableColumn
trapSeverityDiscrim = _TrapSeverityDiscrim_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 7),
    _TrapSeverityDiscrim_Type()
)
trapSeverityDiscrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSeverityDiscrim.setStatus("current")


class _TrapDiscrimOperationalState_Type(Integer32):
    """Custom type trapDiscrimOperationalState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TrapDiscrimOperationalState_Type.__name__ = "Integer32"
_TrapDiscrimOperationalState_Object = MibTableColumn
trapDiscrimOperationalState = _TrapDiscrimOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 8),
    _TrapDiscrimOperationalState_Type()
)
trapDiscrimOperationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimOperationalState.setStatus("current")


class _TrapDiscrimConfigChangeCntl_Type(Integer32):
    """Custom type trapDiscrimConfigChangeCntl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_TrapDiscrimConfigChangeCntl_Type.__name__ = "Integer32"
_TrapDiscrimConfigChangeCntl_Object = MibTableColumn
trapDiscrimConfigChangeCntl = _TrapDiscrimConfigChangeCntl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 9),
    _TrapDiscrimConfigChangeCntl_Type()
)
trapDiscrimConfigChangeCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimConfigChangeCntl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCS-TRAPS-MIB",
    **{"ConfigChangeState": ConfigChangeState,
       "ConfigChangeAction": ConfigChangeAction,
       "bcsTraps": bcsTraps,
       "bcsTrapElements": bcsTrapElements,
       "trapIdentifier": trapIdentifier,
       "trapSequenceId": trapSequenceId,
       "trapNetworkElemModelNumber": trapNetworkElemModelNumber,
       "trapNetworkElemSerialNum": trapNetworkElemSerialNum,
       "trapPerceivedSeverity": trapPerceivedSeverity,
       "trapNetworkElemOperState": trapNetworkElemOperState,
       "trapNetworkElemAlarmStatus": trapNetworkElemAlarmStatus,
       "trapNetworkElemAdminState": trapNetworkElemAdminState,
       "trapNetworkElemAvailStatus": trapNetworkElemAvailStatus,
       "trapText": trapText,
       "trapNETrapLastTrapTimeStamp": trapNETrapLastTrapTimeStamp,
       "trapChangedObjectId": trapChangedObjectId,
       "trapAdditionalInfoInteger1": trapAdditionalInfoInteger1,
       "trapAdditionalInfoInteger2": trapAdditionalInfoInteger2,
       "trapAdditionalInfoInteger3": trapAdditionalInfoInteger3,
       "trapChangedValueDisplayString": trapChangedValueDisplayString,
       "trapChangedValueOID": trapChangedValueOID,
       "trapChangedValueIpAddress": trapChangedValueIpAddress,
       "trapChangedValueInteger": trapChangedValueInteger,
       "bcsTrapControl": bcsTrapControl,
       "numberOfTrapReceivers": numberOfTrapReceivers,
       "trapReceiversTable": trapReceiversTable,
       "trapReceiversEntry": trapReceiversEntry,
       "trapReceiversTableIndex": trapReceiversTableIndex,
       "trapReceiverAddr": trapReceiverAddr,
       "trapReceiverCommunityString": trapReceiverCommunityString,
       "trapToBeSendQueueSize": trapToBeSendQueueSize,
       "trapSentQueueSize": trapSentQueueSize,
       "trapThrottlingRate": trapThrottlingRate,
       "trapLastSent": trapLastSent,
       "trapReceiversEntryOperState": trapReceiversEntryOperState,
       "trapResendRequest": trapResendRequest,
       "numberOfDiscriminators": numberOfDiscriminators,
       "trapDiscrimTable": trapDiscrimTable,
       "trapDiscrimEntry": trapDiscrimEntry,
       "trapDiscrimTableIndex": trapDiscrimTableIndex,
       "trapDiscrimReceiverAddr": trapDiscrimReceiverAddr,
       "trapDiscrimAvailabilityStatus": trapDiscrimAvailabilityStatus,
       "trapDiscrimWeeklyMask": trapDiscrimWeeklyMask,
       "trapDiscrimDailyStartTime": trapDiscrimDailyStartTime,
       "trapDiscrimDailyStopTime": trapDiscrimDailyStopTime,
       "trapSeverityDiscrim": trapSeverityDiscrim,
       "trapDiscrimOperationalState": trapDiscrimOperationalState,
       "trapDiscrimConfigChangeCntl": trapDiscrimConfigChangeCntl}
)

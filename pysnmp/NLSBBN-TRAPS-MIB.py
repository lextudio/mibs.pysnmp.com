# SNMP MIB module (NLSBBN-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NLSBBN-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:30 2024
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

(bbnTraps,
 gi,
 nlsbbn) = mibBuilder.importSymbols(
    "NLS-BBNIDENT-MIB",
    "bbnTraps",
    "gi",
    "nlsbbn")

(EntryStatus,) = mibBuilder.importSymbols(
    "RFC1271-MIB",
    "EntryStatus")

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

_BbnTrapElements_ObjectIdentity = ObjectIdentity
bbnTrapElements = _BbnTrapElements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1)
)


class _TrapIdentifier_Type(Integer32):
    """Custom type trapIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapIdentifier_Type.__name__ = "Integer32"
_TrapIdentifier_Object = MibScalar
trapIdentifier = _TrapIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 1),
    _TrapIdentifier_Type()
)
trapIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIdentifier.setStatus("mandatory")


class _TrapNetworkElemModelNumber_Type(DisplayString):
    """Custom type trapNetworkElemModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TrapNetworkElemModelNumber_Type.__name__ = "DisplayString"
_TrapNetworkElemModelNumber_Object = MibScalar
trapNetworkElemModelNumber = _TrapNetworkElemModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 2),
    _TrapNetworkElemModelNumber_Type()
)
trapNetworkElemModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemModelNumber.setStatus("mandatory")


class _TrapNetworkElemSerialNum_Type(DisplayString):
    """Custom type trapNetworkElemSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TrapNetworkElemSerialNum_Type.__name__ = "DisplayString"
_TrapNetworkElemSerialNum_Object = MibScalar
trapNetworkElemSerialNum = _TrapNetworkElemSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 3),
    _TrapNetworkElemSerialNum_Type()
)
trapNetworkElemSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemSerialNum.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 4),
    _TrapPerceivedSeverity_Type()
)
trapPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPerceivedSeverity.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 5),
    _TrapNetworkElemOperState_Type()
)
trapNetworkElemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemOperState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 6),
    _TrapNetworkElemAlarmStatus_Type()
)
trapNetworkElemAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemAlarmStatus.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 7),
    _TrapNetworkElemAdminState_Type()
)
trapNetworkElemAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemAdminState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 8),
    _TrapNetworkElemAvailStatus_Type()
)
trapNetworkElemAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNetworkElemAvailStatus.setStatus("mandatory")
_TrapText_Type = DisplayString
_TrapText_Object = MibScalar
trapText = _TrapText_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 9),
    _TrapText_Type()
)
trapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapText.setStatus("mandatory")
_TrapNETrapLastTrapTimeStamp_Type = TimeTicks
_TrapNETrapLastTrapTimeStamp_Object = MibScalar
trapNETrapLastTrapTimeStamp = _TrapNETrapLastTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 10),
    _TrapNETrapLastTrapTimeStamp_Type()
)
trapNETrapLastTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNETrapLastTrapTimeStamp.setStatus("mandatory")


class _TrapChangedObjectId_Type(ObjectIdentifier):
    """Custom type trapChangedObjectId based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 1166)


_TrapChangedObjectId_Object = MibScalar
trapChangedObjectId = _TrapChangedObjectId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 11),
    _TrapChangedObjectId_Type()
)
trapChangedObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChangedObjectId.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 12),
    _TrapAdditionalInfoInteger1_Type()
)
trapAdditionalInfoInteger1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAdditionalInfoInteger1.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 13),
    _TrapAdditionalInfoInteger2_Type()
)
trapAdditionalInfoInteger2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAdditionalInfoInteger2.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 14),
    _TrapAdditionalInfoInteger3_Type()
)
trapAdditionalInfoInteger3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAdditionalInfoInteger3.setStatus("mandatory")
_TrapChangedValueDisplayString_Type = DisplayString
_TrapChangedValueDisplayString_Object = MibScalar
trapChangedValueDisplayString = _TrapChangedValueDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 15),
    _TrapChangedValueDisplayString_Type()
)
trapChangedValueDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChangedValueDisplayString.setStatus("mandatory")


class _TrapChangedValueOID_Type(ObjectIdentifier):
    """Custom type trapChangedValueOID based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 1166)


_TrapChangedValueOID_Object = MibScalar
trapChangedValueOID = _TrapChangedValueOID_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 16),
    _TrapChangedValueOID_Type()
)
trapChangedValueOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChangedValueOID.setStatus("mandatory")


class _TrapChangedValueIpAddress_Type(IpAddress):
    """Custom type trapChangedValueIpAddress based on IpAddress"""
    defaultValue = 0


_TrapChangedValueIpAddress_Object = MibScalar
trapChangedValueIpAddress = _TrapChangedValueIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 17),
    _TrapChangedValueIpAddress_Type()
)
trapChangedValueIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChangedValueIpAddress.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 18),
    _TrapChangedValueInteger_Type()
)
trapChangedValueInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChangedValueInteger.setStatus("mandatory")
_BbnTrapControl_ObjectIdentity = ObjectIdentity
bbnTrapControl = _BbnTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2)
)
_NumberOfTrapReceivers_Type = Integer32
_NumberOfTrapReceivers_Object = MibScalar
numberOfTrapReceivers = _NumberOfTrapReceivers_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 1),
    _NumberOfTrapReceivers_Type()
)
numberOfTrapReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfTrapReceivers.setStatus("mandatory")
_TrapReceiversTable_Object = MibTable
trapReceiversTable = _TrapReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2)
)
if mibBuilder.loadTexts:
    trapReceiversTable.setStatus("mandatory")
_TrapReceiversTableEntry_Object = MibTableRow
trapReceiversTableEntry = _TrapReceiversTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1)
)
trapReceiversTableEntry.setIndexNames(
    (0, "NLSBBN-TRAPS-MIB", "trapReceiversTableIndex"),
)
if mibBuilder.loadTexts:
    trapReceiversTableEntry.setStatus("mandatory")


class _TrapReceiversTableIndex_Type(Integer32):
    """Custom type trapReceiversTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TrapReceiversTableIndex_Type.__name__ = "Integer32"
_TrapReceiversTableIndex_Object = MibTableColumn
trapReceiversTableIndex = _TrapReceiversTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 1),
    _TrapReceiversTableIndex_Type()
)
trapReceiversTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapReceiversTableIndex.setStatus("mandatory")


class _TrapReceiverAddr_Type(IpAddress):
    """Custom type trapReceiverAddr based on IpAddress"""
    defaultValue = 0


_TrapReceiverAddr_Object = MibTableColumn
trapReceiverAddr = _TrapReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 2),
    _TrapReceiverAddr_Type()
)
trapReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverAddr.setStatus("mandatory")
_TrapReceiverCommunityString_Type = DisplayString
_TrapReceiverCommunityString_Object = MibTableColumn
trapReceiverCommunityString = _TrapReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 3),
    _TrapReceiverCommunityString_Type()
)
trapReceiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverCommunityString.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 4),
    _TrapToBeSendQueueSize_Type()
)
trapToBeSendQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapToBeSendQueueSize.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 5),
    _TrapSentQueueSize_Type()
)
trapSentQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSentQueueSize.setStatus("mandatory")


class _TrapThrottlingRate_Type(Integer32):
    """Custom type trapThrottlingRate based on Integer32"""
    defaultValue = 1


_TrapThrottlingRate_Object = MibTableColumn
trapThrottlingRate = _TrapThrottlingRate_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 6),
    _TrapThrottlingRate_Type()
)
trapThrottlingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapThrottlingRate.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 7),
    _TrapLastSent_Type()
)
trapLastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLastSent.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 8),
    _TrapReceiversEntryOperState_Type()
)
trapReceiversEntryOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiversEntryOperState.setStatus("mandatory")
_TrapResendRequest_Type = Integer32
_TrapResendRequest_Object = MibTableColumn
trapResendRequest = _TrapResendRequest_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 9),
    _TrapResendRequest_Type()
)
trapResendRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapResendRequest.setStatus("mandatory")
_NumberOfDiscriminators_Type = Integer32
_NumberOfDiscriminators_Object = MibScalar
numberOfDiscriminators = _NumberOfDiscriminators_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 3),
    _NumberOfDiscriminators_Type()
)
numberOfDiscriminators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfDiscriminators.setStatus("mandatory")
_TrapDiscrimTable_Object = MibTable
trapDiscrimTable = _TrapDiscrimTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4)
)
if mibBuilder.loadTexts:
    trapDiscrimTable.setStatus("mandatory")
_TrapDiscrimTableEntry_Object = MibTableRow
trapDiscrimTableEntry = _TrapDiscrimTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1)
)
trapDiscrimTableEntry.setIndexNames(
    (0, "NLSBBN-TRAPS-MIB", "trapDiscrimTableIndex"),
)
if mibBuilder.loadTexts:
    trapDiscrimTableEntry.setStatus("mandatory")


class _TrapDiscrimTableIndex_Type(Integer32):
    """Custom type trapDiscrimTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TrapDiscrimTableIndex_Type.__name__ = "Integer32"
_TrapDiscrimTableIndex_Object = MibTableColumn
trapDiscrimTableIndex = _TrapDiscrimTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 1),
    _TrapDiscrimTableIndex_Type()
)
trapDiscrimTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDiscrimTableIndex.setStatus("mandatory")


class _TrapDiscrimReceiverAddr_Type(IpAddress):
    """Custom type trapDiscrimReceiverAddr based on IpAddress"""
    defaultValue = 0


_TrapDiscrimReceiverAddr_Object = MibTableColumn
trapDiscrimReceiverAddr = _TrapDiscrimReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 2),
    _TrapDiscrimReceiverAddr_Type()
)
trapDiscrimReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimReceiverAddr.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 3),
    _TrapDiscrimAvailabilityStatus_Type()
)
trapDiscrimAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDiscrimAvailabilityStatus.setStatus("mandatory")


class _TrapDiscrimWeeklyMask_Type(DisplayString):
    """Custom type trapDiscrimWeeklyMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_TrapDiscrimWeeklyMask_Type.__name__ = "DisplayString"
_TrapDiscrimWeeklyMask_Object = MibTableColumn
trapDiscrimWeeklyMask = _TrapDiscrimWeeklyMask_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 4),
    _TrapDiscrimWeeklyMask_Type()
)
trapDiscrimWeeklyMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimWeeklyMask.setStatus("mandatory")


class _TrapDiscrimDailyStartTime_Type(Integer32):
    """Custom type trapDiscrimDailyStartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_TrapDiscrimDailyStartTime_Type.__name__ = "Integer32"
_TrapDiscrimDailyStartTime_Object = MibTableColumn
trapDiscrimDailyStartTime = _TrapDiscrimDailyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 5),
    _TrapDiscrimDailyStartTime_Type()
)
trapDiscrimDailyStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimDailyStartTime.setStatus("mandatory")


class _TrapDiscrimDailyStopTime_Type(Integer32):
    """Custom type trapDiscrimDailyStopTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_TrapDiscrimDailyStopTime_Type.__name__ = "Integer32"
_TrapDiscrimDailyStopTime_Object = MibTableColumn
trapDiscrimDailyStopTime = _TrapDiscrimDailyStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 6),
    _TrapDiscrimDailyStopTime_Type()
)
trapDiscrimDailyStopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimDailyStopTime.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 7),
    _TrapSeverityDiscrim_Type()
)
trapSeverityDiscrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSeverityDiscrim.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 8),
    _TrapDiscrimOperationalState_Type()
)
trapDiscrimOperationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimOperationalState.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 9),
    _TrapDiscrimConfigChangeCntl_Type()
)
trapDiscrimConfigChangeCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDiscrimConfigChangeCntl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NLSBBN-TRAPS-MIB",
    **{"bbnTrapElements": bbnTrapElements,
       "trapIdentifier": trapIdentifier,
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
       "bbnTrapControl": bbnTrapControl,
       "numberOfTrapReceivers": numberOfTrapReceivers,
       "trapReceiversTable": trapReceiversTable,
       "trapReceiversTableEntry": trapReceiversTableEntry,
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
       "trapDiscrimTableEntry": trapDiscrimTableEntry,
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

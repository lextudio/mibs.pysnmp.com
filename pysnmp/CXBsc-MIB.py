# SNMP MIB module (CXBsc-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXBsc-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:09 2024
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

(Alias,
 SapIndex,
 cxBsc) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxBsc")

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



class BscCuIndex(Integer32):
    """Custom type BscCuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )





class BscDevIndex(Integer32):
    """Custom type BscDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )





class BscRowStatus(Integer32):
    """Custom type BscRowStatus based on Integer32"""
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





class BscAckMode(Integer32):
    """Custom type BscAckMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 1),
          ("local", 2))
    )





class BscOperationalMode(Integer32):
    """Custom type BscOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )





class BscBlockSize(Integer32):
    """Custom type BscBlockSize based on Integer32"""
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
        *(("block128", 1),
          ("block1k", 4),
          ("block256", 2),
          ("block2k", 5),
          ("block3000", 6),
          ("block512", 3),
          ("block5k", 7))
    )





class BscStatusSense(Integer32):
    """Custom type BscStatusSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isSet", 2),
          ("notSet", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BscSapTable_Object = MibTable
bscSapTable = _BscSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10)
)
if mibBuilder.loadTexts:
    bscSapTable.setStatus("mandatory")
_BscSapEntry_Object = MibTableRow
bscSapEntry = _BscSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1)
)
bscSapEntry.setIndexNames(
    (0, "CXBsc-MIB", "bscSapNumber"),
)
if mibBuilder.loadTexts:
    bscSapEntry.setStatus("mandatory")
_BscSapNumber_Type = SapIndex
_BscSapNumber_Object = MibTableColumn
bscSapNumber = _BscSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 1),
    _BscSapNumber_Type()
)
bscSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscSapNumber.setStatus("mandatory")
_BscSapRowStatus_Type = BscRowStatus
_BscSapRowStatus_Object = MibTableColumn
bscSapRowStatus = _BscSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 2),
    _BscSapRowStatus_Type()
)
bscSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscSapRowStatus.setStatus("mandatory")


class _BscSapType_Type(Integer32):
    """Custom type bscSapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 1),
          ("upper", 2))
    )


_BscSapType_Type.__name__ = "Integer32"
_BscSapType_Object = MibTableColumn
bscSapType = _BscSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 3),
    _BscSapType_Type()
)
bscSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscSapType.setStatus("mandatory")


class _BscSapInterfaceType_Type(Integer32):
    """Custom type bscSapInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hostInterfaceUnit", 2),
          ("terminalInterfaceUnit", 1))
    )


_BscSapInterfaceType_Type.__name__ = "Integer32"
_BscSapInterfaceType_Object = MibTableColumn
bscSapInterfaceType = _BscSapInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 4),
    _BscSapInterfaceType_Type()
)
bscSapInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscSapInterfaceType.setStatus("mandatory")
_BscSapAlias_Type = Alias
_BscSapAlias_Object = MibTableColumn
bscSapAlias = _BscSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 5),
    _BscSapAlias_Type()
)
bscSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscSapAlias.setStatus("mandatory")
_BscSapCompanionAlias_Type = Alias
_BscSapCompanionAlias_Object = MibTableColumn
bscSapCompanionAlias = _BscSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 6),
    _BscSapCompanionAlias_Type()
)
bscSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscSapCompanionAlias.setStatus("mandatory")


class _BscSapSnalcRef_Type(Integer32):
    """Custom type bscSapSnalcRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_BscSapSnalcRef_Type.__name__ = "Integer32"
_BscSapSnalcRef_Object = MibTableColumn
bscSapSnalcRef = _BscSapSnalcRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 7),
    _BscSapSnalcRef_Type()
)
bscSapSnalcRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscSapSnalcRef.setStatus("mandatory")


class _BscPollIntAfterAckTimer_Type(TimeTicks):
    """Custom type bscPollIntAfterAckTimer based on TimeTicks"""
    defaultValue = 0


_BscPollIntAfterAckTimer_Object = MibTableColumn
bscPollIntAfterAckTimer = _BscPollIntAfterAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 8),
    _BscPollIntAfterAckTimer_Type()
)
bscPollIntAfterAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscPollIntAfterAckTimer.setStatus("mandatory")


class _BscSapControl_Type(Integer32):
    """Custom type bscSapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_BscSapControl_Type.__name__ = "Integer32"
_BscSapControl_Object = MibTableColumn
bscSapControl = _BscSapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 20),
    _BscSapControl_Type()
)
bscSapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bscSapControl.setStatus("mandatory")
_BscSapOperationalMode_Type = BscOperationalMode
_BscSapOperationalMode_Object = MibTableColumn
bscSapOperationalMode = _BscSapOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 30),
    _BscSapOperationalMode_Type()
)
bscSapOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscSapOperationalMode.setStatus("mandatory")


class _BscSapLinkStatus_Type(Integer32):
    """Custom type bscSapLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_BscSapLinkStatus_Type.__name__ = "Integer32"
_BscSapLinkStatus_Object = MibTableColumn
bscSapLinkStatus = _BscSapLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 31),
    _BscSapLinkStatus_Type()
)
bscSapLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscSapLinkStatus.setStatus("mandatory")
_BscSapLinkChange_Type = Counter32
_BscSapLinkChange_Object = MibTableColumn
bscSapLinkChange = _BscSapLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 40),
    _BscSapLinkChange_Type()
)
bscSapLinkChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscSapLinkChange.setStatus("mandatory")
_BscSapOverrun_Type = Counter32
_BscSapOverrun_Object = MibTableColumn
bscSapOverrun = _BscSapOverrun_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 41),
    _BscSapOverrun_Type()
)
bscSapOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscSapOverrun.setStatus("mandatory")
_BscSapParityError_Type = Counter32
_BscSapParityError_Object = MibTableColumn
bscSapParityError = _BscSapParityError_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 42),
    _BscSapParityError_Type()
)
bscSapParityError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscSapParityError.setStatus("mandatory")
_BscSapCrcError_Type = Counter32
_BscSapCrcError_Object = MibTableColumn
bscSapCrcError = _BscSapCrcError_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 43),
    _BscSapCrcError_Type()
)
bscSapCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscSapCrcError.setStatus("mandatory")
_BscSapBlockReject_Type = Counter32
_BscSapBlockReject_Object = MibTableColumn
bscSapBlockReject = _BscSapBlockReject_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 10, 1, 44),
    _BscSapBlockReject_Type()
)
bscSapBlockReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscSapBlockReject.setStatus("mandatory")
_BscCuTable_Object = MibTable
bscCuTable = _BscCuTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11)
)
if mibBuilder.loadTexts:
    bscCuTable.setStatus("mandatory")
_BscCuEntry_Object = MibTableRow
bscCuEntry = _BscCuEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1)
)
bscCuEntry.setIndexNames(
    (0, "CXBsc-MIB", "bscCuSapNumber"),
    (0, "CXBsc-MIB", "bscCuNumber"),
)
if mibBuilder.loadTexts:
    bscCuEntry.setStatus("mandatory")
_BscCuSapNumber_Type = SapIndex
_BscCuSapNumber_Object = MibTableColumn
bscCuSapNumber = _BscCuSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 1),
    _BscCuSapNumber_Type()
)
bscCuSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCuSapNumber.setStatus("mandatory")
_BscCuNumber_Type = BscCuIndex
_BscCuNumber_Object = MibTableColumn
bscCuNumber = _BscCuNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 2),
    _BscCuNumber_Type()
)
bscCuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCuNumber.setStatus("mandatory")
_BscCuRowStatus_Type = BscRowStatus
_BscCuRowStatus_Object = MibTableColumn
bscCuRowStatus = _BscCuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 3),
    _BscCuRowStatus_Type()
)
bscCuRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscCuRowStatus.setStatus("mandatory")


class _BscCuHwdType_Type(Integer32):
    """Custom type bscCuHwdType based on Integer32"""
    defaultValue = 3

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
        *(("cu3271", 1),
          ("cu3274", 2),
          ("cu3275", 3),
          ("cu3276", 4),
          ("cuMES", 5))
    )


_BscCuHwdType_Type.__name__ = "Integer32"
_BscCuHwdType_Object = MibTableColumn
bscCuHwdType = _BscCuHwdType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 4),
    _BscCuHwdType_Type()
)
bscCuHwdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscCuHwdType.setStatus("mandatory")


class _BscCuMaxBlockLength_Type(BscBlockSize):
    """Custom type bscCuMaxBlockLength based on BscBlockSize"""


_BscCuMaxBlockLength_Object = MibTableColumn
bscCuMaxBlockLength = _BscCuMaxBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 5),
    _BscCuMaxBlockLength_Type()
)
bscCuMaxBlockLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscCuMaxBlockLength.setStatus("mandatory")


class _BscCuPollTimeout_Type(Integer32):
    """Custom type bscCuPollTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_BscCuPollTimeout_Type.__name__ = "Integer32"
_BscCuPollTimeout_Object = MibTableColumn
bscCuPollTimeout = _BscCuPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 6),
    _BscCuPollTimeout_Type()
)
bscCuPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscCuPollTimeout.setStatus("mandatory")


class _BscCuDelayTimer_Type(Integer32):
    """Custom type bscCuDelayTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_BscCuDelayTimer_Type.__name__ = "Integer32"
_BscCuDelayTimer_Object = MibTableColumn
bscCuDelayTimer = _BscCuDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 7),
    _BscCuDelayTimer_Type()
)
bscCuDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscCuDelayTimer.setStatus("mandatory")


class _BscCuRetryCounter_Type(Integer32):
    """Custom type bscCuRetryCounter based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_BscCuRetryCounter_Type.__name__ = "Integer32"
_BscCuRetryCounter_Object = MibTableColumn
bscCuRetryCounter = _BscCuRetryCounter_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 8),
    _BscCuRetryCounter_Type()
)
bscCuRetryCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscCuRetryCounter.setStatus("mandatory")


class _BscCuETBAck_Type(BscAckMode):
    """Custom type bscCuETBAck based on BscAckMode"""


_BscCuETBAck_Object = MibTableColumn
bscCuETBAck = _BscCuETBAck_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 9),
    _BscCuETBAck_Type()
)
bscCuETBAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscCuETBAck.setStatus("mandatory")


class _BscCuETXAck_Type(BscAckMode):
    """Custom type bscCuETXAck based on BscAckMode"""


_BscCuETXAck_Object = MibTableColumn
bscCuETXAck = _BscCuETXAck_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 10),
    _BscCuETXAck_Type()
)
bscCuETXAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscCuETXAck.setStatus("mandatory")


class _BscCuControl_Type(Integer32):
    """Custom type bscCuControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_BscCuControl_Type.__name__ = "Integer32"
_BscCuControl_Object = MibTableColumn
bscCuControl = _BscCuControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 20),
    _BscCuControl_Type()
)
bscCuControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bscCuControl.setStatus("mandatory")
_BscCuOperationalMode_Type = BscOperationalMode
_BscCuOperationalMode_Object = MibTableColumn
bscCuOperationalMode = _BscCuOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 30),
    _BscCuOperationalMode_Type()
)
bscCuOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCuOperationalMode.setStatus("mandatory")


class _BscCuConnectionStatus_Type(Integer32):
    """Custom type bscCuConnectionStatus based on Integer32"""
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
        *(("nonExistantX25Connection", 1),
          ("snalcConnectionConfirmationSent", 3),
          ("snalcConnectionRequested", 2),
          ("x25ConnectionEstablished", 4))
    )


_BscCuConnectionStatus_Type.__name__ = "Integer32"
_BscCuConnectionStatus_Object = MibTableColumn
bscCuConnectionStatus = _BscCuConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 31),
    _BscCuConnectionStatus_Type()
)
bscCuConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCuConnectionStatus.setStatus("mandatory")
_BscCuConnectRequest_Type = Counter32
_BscCuConnectRequest_Object = MibTableColumn
bscCuConnectRequest = _BscCuConnectRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 45),
    _BscCuConnectRequest_Type()
)
bscCuConnectRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCuConnectRequest.setStatus("mandatory")
_BscCuDisconnectRequest_Type = Counter32
_BscCuDisconnectRequest_Object = MibTableColumn
bscCuDisconnectRequest = _BscCuDisconnectRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 46),
    _BscCuDisconnectRequest_Type()
)
bscCuDisconnectRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCuDisconnectRequest.setStatus("mandatory")
_BscCuDisconnectIndication_Type = Counter32
_BscCuDisconnectIndication_Object = MibTableColumn
bscCuDisconnectIndication = _BscCuDisconnectIndication_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 47),
    _BscCuDisconnectIndication_Type()
)
bscCuDisconnectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCuDisconnectIndication.setStatus("mandatory")
_BscCuEndToEndConnectCnf_Type = Counter32
_BscCuEndToEndConnectCnf_Object = MibTableColumn
bscCuEndToEndConnectCnf = _BscCuEndToEndConnectCnf_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 48),
    _BscCuEndToEndConnectCnf_Type()
)
bscCuEndToEndConnectCnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCuEndToEndConnectCnf.setStatus("mandatory")
_BscCuSnalcRxRnr_Type = Counter32
_BscCuSnalcRxRnr_Object = MibTableColumn
bscCuSnalcRxRnr = _BscCuSnalcRxRnr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 49),
    _BscCuSnalcRxRnr_Type()
)
bscCuSnalcRxRnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCuSnalcRxRnr.setStatus("mandatory")
_BscCuSnalcRxRr_Type = Counter32
_BscCuSnalcRxRr_Object = MibTableColumn
bscCuSnalcRxRr = _BscCuSnalcRxRr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 11, 1, 50),
    _BscCuSnalcRxRr_Type()
)
bscCuSnalcRxRr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCuSnalcRxRr.setStatus("mandatory")
_BscDevTable_Object = MibTable
bscDevTable = _BscDevTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12)
)
if mibBuilder.loadTexts:
    bscDevTable.setStatus("mandatory")
_BscDevEntry_Object = MibTableRow
bscDevEntry = _BscDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1)
)
bscDevEntry.setIndexNames(
    (0, "CXBsc-MIB", "bscDevSapNumber"),
    (0, "CXBsc-MIB", "bscDevCuNumber"),
    (0, "CXBsc-MIB", "bscDevNumber"),
)
if mibBuilder.loadTexts:
    bscDevEntry.setStatus("mandatory")
_BscDevSapNumber_Type = SapIndex
_BscDevSapNumber_Object = MibTableColumn
bscDevSapNumber = _BscDevSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 1),
    _BscDevSapNumber_Type()
)
bscDevSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSapNumber.setStatus("mandatory")
_BscDevCuNumber_Type = BscCuIndex
_BscDevCuNumber_Object = MibTableColumn
bscDevCuNumber = _BscDevCuNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 2),
    _BscDevCuNumber_Type()
)
bscDevCuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevCuNumber.setStatus("mandatory")
_BscDevNumber_Type = BscDevIndex
_BscDevNumber_Object = MibTableColumn
bscDevNumber = _BscDevNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 3),
    _BscDevNumber_Type()
)
bscDevNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevNumber.setStatus("mandatory")
_BscDevRowStatus_Type = BscRowStatus
_BscDevRowStatus_Object = MibTableColumn
bscDevRowStatus = _BscDevRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 4),
    _BscDevRowStatus_Type()
)
bscDevRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscDevRowStatus.setStatus("mandatory")


class _BscDevType_Type(Integer32):
    """Custom type bscDevType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("display", 1),
          ("printer", 2))
    )


_BscDevType_Type.__name__ = "Integer32"
_BscDevType_Object = MibTableColumn
bscDevType = _BscDevType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 5),
    _BscDevType_Type()
)
bscDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bscDevType.setStatus("mandatory")


class _BscDevControl_Type(Integer32):
    """Custom type bscDevControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_BscDevControl_Type.__name__ = "Integer32"
_BscDevControl_Object = MibTableColumn
bscDevControl = _BscDevControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 20),
    _BscDevControl_Type()
)
bscDevControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bscDevControl.setStatus("mandatory")
_BscDevOperationalMode_Type = BscOperationalMode
_BscDevOperationalMode_Object = MibTableColumn
bscDevOperationalMode = _BscDevOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 30),
    _BscDevOperationalMode_Type()
)
bscDevOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevOperationalMode.setStatus("mandatory")


class _BscDevConnectionStatus_Type(Integer32):
    """Custom type bscDevConnectionStatus based on Integer32"""
    defaultValue = 1

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
        *(("circuitEnableReceived", 3),
          ("circuitEnableSent", 4),
          ("circuitRequestSent", 2),
          ("dataMode", 5),
          ("nonExistantLogicalConnection", 1))
    )


_BscDevConnectionStatus_Type.__name__ = "Integer32"
_BscDevConnectionStatus_Object = MibTableColumn
bscDevConnectionStatus = _BscDevConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 31),
    _BscDevConnectionStatus_Type()
)
bscDevConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevConnectionStatus.setStatus("mandatory")


class _BscDevState_Type(Integer32):
    """Custom type bscDevState based on Integer32"""
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("hiuDeviceStateReserved-1", 12),
          ("hiuDeviceStateReserved-2", 13),
          ("hiuDeviceStateReserved-3", 14),
          ("hiuReadWaitForResponse", 6),
          ("hiuReceiveCommandMode", 5),
          ("hiuSendEotOnAcknowledgment", 4),
          ("hiuSendNextMessageOnAcknowledgment", 3),
          ("hiuSendNextOnNak", 11),
          ("hiuSendNextTransparent", 8),
          ("hiuWaitForCuReadEtx", 7),
          ("hiuWaitForNextPoll", 1),
          ("hiuWaitingForRviResponse", 9),
          ("hiuWaitingForStatusSenseAcknowledgment", 2),
          ("hiuWaitingForWackResponse", 10),
          ("tiuDataPending", 22),
          ("tiuEndTestRequest", 29),
          ("tiuParityCursorCheckDetected", 24),
          ("tiuReadWaitForResponse", 25),
          ("tiuReceivingCommand", 23),
          ("tiuSendEotOnAcknowledgment", 21),
          ("tiuSendEotOnTransparentAcknowledgment", 20),
          ("tiuSendNextAfterNak", 27),
          ("tiuSendNextMessageOnAcknowledgment", 19),
          ("tiuSentSelectivePoll", 17),
          ("tiuSentSpecificPoll", 16),
          ("tiuStatusSenseReceived", 18),
          ("tiuTerminatePolling", 28),
          ("tiuWaitForNextPoll", 15),
          ("tiuWaitingForSnalcData", 26))
    )


_BscDevState_Type.__name__ = "Integer32"
_BscDevState_Object = MibTableColumn
bscDevState = _BscDevState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 32),
    _BscDevState_Type()
)
bscDevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevState.setStatus("mandatory")


class _BscDevSSDeviceBusy_Type(BscStatusSense):
    """Custom type bscDevSSDeviceBusy based on BscStatusSense"""


_BscDevSSDeviceBusy_Object = MibTableColumn
bscDevSSDeviceBusy = _BscDevSSDeviceBusy_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 33),
    _BscDevSSDeviceBusy_Type()
)
bscDevSSDeviceBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSSDeviceBusy.setStatus("mandatory")


class _BscDevSSUnitSpecify_Type(BscStatusSense):
    """Custom type bscDevSSUnitSpecify based on BscStatusSense"""


_BscDevSSUnitSpecify_Object = MibTableColumn
bscDevSSUnitSpecify = _BscDevSSUnitSpecify_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 34),
    _BscDevSSUnitSpecify_Type()
)
bscDevSSUnitSpecify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSSUnitSpecify.setStatus("mandatory")


class _BscDevSSDeviceEnd_Type(BscStatusSense):
    """Custom type bscDevSSDeviceEnd based on BscStatusSense"""


_BscDevSSDeviceEnd_Object = MibTableColumn
bscDevSSDeviceEnd = _BscDevSSDeviceEnd_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 35),
    _BscDevSSDeviceEnd_Type()
)
bscDevSSDeviceEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSSDeviceEnd.setStatus("mandatory")


class _BscDevSSTransmissionCheck_Type(BscStatusSense):
    """Custom type bscDevSSTransmissionCheck based on BscStatusSense"""


_BscDevSSTransmissionCheck_Object = MibTableColumn
bscDevSSTransmissionCheck = _BscDevSSTransmissionCheck_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 36),
    _BscDevSSTransmissionCheck_Type()
)
bscDevSSTransmissionCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSSTransmissionCheck.setStatus("mandatory")


class _BscDevSSCommandReject_Type(BscStatusSense):
    """Custom type bscDevSSCommandReject based on BscStatusSense"""


_BscDevSSCommandReject_Object = MibTableColumn
bscDevSSCommandReject = _BscDevSSCommandReject_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 37),
    _BscDevSSCommandReject_Type()
)
bscDevSSCommandReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSSCommandReject.setStatus("mandatory")


class _BscDevSSInterventionRequired_Type(BscStatusSense):
    """Custom type bscDevSSInterventionRequired based on BscStatusSense"""


_BscDevSSInterventionRequired_Object = MibTableColumn
bscDevSSInterventionRequired = _BscDevSSInterventionRequired_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 38),
    _BscDevSSInterventionRequired_Type()
)
bscDevSSInterventionRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSSInterventionRequired.setStatus("mandatory")


class _BscDevSSEquipmentCheck_Type(BscStatusSense):
    """Custom type bscDevSSEquipmentCheck based on BscStatusSense"""


_BscDevSSEquipmentCheck_Object = MibTableColumn
bscDevSSEquipmentCheck = _BscDevSSEquipmentCheck_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 39),
    _BscDevSSEquipmentCheck_Type()
)
bscDevSSEquipmentCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSSEquipmentCheck.setStatus("mandatory")


class _BscDevSSDataCheck_Type(BscStatusSense):
    """Custom type bscDevSSDataCheck based on BscStatusSense"""


_BscDevSSDataCheck_Object = MibTableColumn
bscDevSSDataCheck = _BscDevSSDataCheck_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 40),
    _BscDevSSDataCheck_Type()
)
bscDevSSDataCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSSDataCheck.setStatus("mandatory")


class _BscDevSSControlCheck_Type(BscStatusSense):
    """Custom type bscDevSSControlCheck based on BscStatusSense"""


_BscDevSSControlCheck_Object = MibTableColumn
bscDevSSControlCheck = _BscDevSSControlCheck_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 41),
    _BscDevSSControlCheck_Type()
)
bscDevSSControlCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSSControlCheck.setStatus("mandatory")


class _BscDevSSOperationCheck_Type(BscStatusSense):
    """Custom type bscDevSSOperationCheck based on BscStatusSense"""


_BscDevSSOperationCheck_Object = MibTableColumn
bscDevSSOperationCheck = _BscDevSSOperationCheck_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 42),
    _BscDevSSOperationCheck_Type()
)
bscDevSSOperationCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSSOperationCheck.setStatus("mandatory")
_BscDevGeneralPoll_Type = Counter32
_BscDevGeneralPoll_Object = MibTableColumn
bscDevGeneralPoll = _BscDevGeneralPoll_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 60),
    _BscDevGeneralPoll_Type()
)
bscDevGeneralPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevGeneralPoll.setStatus("mandatory")
_BscDevSpecificPoll_Type = Counter32
_BscDevSpecificPoll_Object = MibTableColumn
bscDevSpecificPoll = _BscDevSpecificPoll_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 61),
    _BscDevSpecificPoll_Type()
)
bscDevSpecificPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevSpecificPoll.setStatus("mandatory")
_BscDevDeviceSelection_Type = Counter32
_BscDevDeviceSelection_Object = MibTableColumn
bscDevDeviceSelection = _BscDevDeviceSelection_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 62),
    _BscDevDeviceSelection_Type()
)
bscDevDeviceSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevDeviceSelection.setStatus("mandatory")
_BscDevTestRequest_Type = Counter32
_BscDevTestRequest_Object = MibTableColumn
bscDevTestRequest = _BscDevTestRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 63),
    _BscDevTestRequest_Type()
)
bscDevTestRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevTestRequest.setStatus("mandatory")
_BscDevHostWrite_Type = Counter32
_BscDevHostWrite_Object = MibTableColumn
bscDevHostWrite = _BscDevHostWrite_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 64),
    _BscDevHostWrite_Type()
)
bscDevHostWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevHostWrite.setStatus("mandatory")
_BscDevHostRead_Type = Counter32
_BscDevHostRead_Object = MibTableColumn
bscDevHostRead = _BscDevHostRead_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 65),
    _BscDevHostRead_Type()
)
bscDevHostRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevHostRead.setStatus("mandatory")
_BscDevHostControl_Type = Counter32
_BscDevHostControl_Object = MibTableColumn
bscDevHostControl = _BscDevHostControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 66),
    _BscDevHostControl_Type()
)
bscDevHostControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevHostControl.setStatus("mandatory")
_BscDevCuShortRead_Type = Counter32
_BscDevCuShortRead_Object = MibTableColumn
bscDevCuShortRead = _BscDevCuShortRead_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 67),
    _BscDevCuShortRead_Type()
)
bscDevCuShortRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevCuShortRead.setStatus("mandatory")
_BscDevTxBlocks_Type = Counter32
_BscDevTxBlocks_Object = MibTableColumn
bscDevTxBlocks = _BscDevTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 68),
    _BscDevTxBlocks_Type()
)
bscDevTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevTxBlocks.setStatus("mandatory")
_BscDevRxBlocks_Type = Counter32
_BscDevRxBlocks_Object = MibTableColumn
bscDevRxBlocks = _BscDevRxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 69),
    _BscDevRxBlocks_Type()
)
bscDevRxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevRxBlocks.setStatus("mandatory")
_BscDevStatusSense_Type = Counter32
_BscDevStatusSense_Object = MibTableColumn
bscDevStatusSense = _BscDevStatusSense_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 70),
    _BscDevStatusSense_Type()
)
bscDevStatusSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevStatusSense.setStatus("mandatory")
_BscDevError_Type = Counter32
_BscDevError_Object = MibTableColumn
bscDevError = _BscDevError_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 71),
    _BscDevError_Type()
)
bscDevError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevError.setStatus("mandatory")
_BscDevErrTimeout_Type = Counter32
_BscDevErrTimeout_Object = MibTableColumn
bscDevErrTimeout = _BscDevErrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 72),
    _BscDevErrTimeout_Type()
)
bscDevErrTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevErrTimeout.setStatus("mandatory")
_BscDevCircuitEnable_Type = Counter32
_BscDevCircuitEnable_Object = MibTableColumn
bscDevCircuitEnable = _BscDevCircuitEnable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 73),
    _BscDevCircuitEnable_Type()
)
bscDevCircuitEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevCircuitEnable.setStatus("mandatory")
_BscDevCircuitDisconnect_Type = Counter32
_BscDevCircuitDisconnect_Object = MibTableColumn
bscDevCircuitDisconnect = _BscDevCircuitDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 74),
    _BscDevCircuitDisconnect_Type()
)
bscDevCircuitDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevCircuitDisconnect.setStatus("mandatory")
_BscDevCircuitRequest_Type = Counter32
_BscDevCircuitRequest_Object = MibTableColumn
bscDevCircuitRequest = _BscDevCircuitRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 75),
    _BscDevCircuitRequest_Type()
)
bscDevCircuitRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevCircuitRequest.setStatus("mandatory")
_BscDevTxCommands_Type = Counter32
_BscDevTxCommands_Object = MibTableColumn
bscDevTxCommands = _BscDevTxCommands_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 76),
    _BscDevTxCommands_Type()
)
bscDevTxCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevTxCommands.setStatus("mandatory")
_BscDevRxCommands_Type = Counter32
_BscDevRxCommands_Object = MibTableColumn
bscDevRxCommands = _BscDevRxCommands_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 77),
    _BscDevRxCommands_Type()
)
bscDevRxCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevRxCommands.setStatus("mandatory")
_BscDevCommandsQueued_Type = Counter32
_BscDevCommandsQueued_Object = MibTableColumn
bscDevCommandsQueued = _BscDevCommandsQueued_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 78),
    _BscDevCommandsQueued_Type()
)
bscDevCommandsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevCommandsQueued.setStatus("mandatory")
_BscDevBlocksQueued_Type = Counter32
_BscDevBlocksQueued_Object = MibTableColumn
bscDevBlocksQueued = _BscDevBlocksQueued_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 79),
    _BscDevBlocksQueued_Type()
)
bscDevBlocksQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevBlocksQueued.setStatus("mandatory")
_BscDevTxRvi_Type = Counter32
_BscDevTxRvi_Object = MibTableColumn
bscDevTxRvi = _BscDevTxRvi_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 80),
    _BscDevTxRvi_Type()
)
bscDevTxRvi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevTxRvi.setStatus("mandatory")
_BscDevRxRvi_Type = Counter32
_BscDevRxRvi_Object = MibTableColumn
bscDevRxRvi = _BscDevRxRvi_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 81),
    _BscDevRxRvi_Type()
)
bscDevRxRvi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevRxRvi.setStatus("mandatory")
_BscDevTxTtd_Type = Counter32
_BscDevTxTtd_Object = MibTableColumn
bscDevTxTtd = _BscDevTxTtd_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 82),
    _BscDevTxTtd_Type()
)
bscDevTxTtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevTxTtd.setStatus("mandatory")
_BscDevRxTtd_Type = Counter32
_BscDevRxTtd_Object = MibTableColumn
bscDevRxTtd = _BscDevRxTtd_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 83),
    _BscDevRxTtd_Type()
)
bscDevRxTtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevRxTtd.setStatus("mandatory")
_BscDevTxWack_Type = Counter32
_BscDevTxWack_Object = MibTableColumn
bscDevTxWack = _BscDevTxWack_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 84),
    _BscDevTxWack_Type()
)
bscDevTxWack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevTxWack.setStatus("mandatory")
_BscDevRxWack_Type = Counter32
_BscDevRxWack_Object = MibTableColumn
bscDevRxWack = _BscDevRxWack_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 56, 12, 1, 85),
    _BscDevRxWack_Type()
)
bscDevRxWack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscDevRxWack.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXBsc-MIB",
    **{"BscCuIndex": BscCuIndex,
       "BscDevIndex": BscDevIndex,
       "BscRowStatus": BscRowStatus,
       "BscAckMode": BscAckMode,
       "BscOperationalMode": BscOperationalMode,
       "BscBlockSize": BscBlockSize,
       "BscStatusSense": BscStatusSense,
       "bscSapTable": bscSapTable,
       "bscSapEntry": bscSapEntry,
       "bscSapNumber": bscSapNumber,
       "bscSapRowStatus": bscSapRowStatus,
       "bscSapType": bscSapType,
       "bscSapInterfaceType": bscSapInterfaceType,
       "bscSapAlias": bscSapAlias,
       "bscSapCompanionAlias": bscSapCompanionAlias,
       "bscSapSnalcRef": bscSapSnalcRef,
       "bscPollIntAfterAckTimer": bscPollIntAfterAckTimer,
       "bscSapControl": bscSapControl,
       "bscSapOperationalMode": bscSapOperationalMode,
       "bscSapLinkStatus": bscSapLinkStatus,
       "bscSapLinkChange": bscSapLinkChange,
       "bscSapOverrun": bscSapOverrun,
       "bscSapParityError": bscSapParityError,
       "bscSapCrcError": bscSapCrcError,
       "bscSapBlockReject": bscSapBlockReject,
       "bscCuTable": bscCuTable,
       "bscCuEntry": bscCuEntry,
       "bscCuSapNumber": bscCuSapNumber,
       "bscCuNumber": bscCuNumber,
       "bscCuRowStatus": bscCuRowStatus,
       "bscCuHwdType": bscCuHwdType,
       "bscCuMaxBlockLength": bscCuMaxBlockLength,
       "bscCuPollTimeout": bscCuPollTimeout,
       "bscCuDelayTimer": bscCuDelayTimer,
       "bscCuRetryCounter": bscCuRetryCounter,
       "bscCuETBAck": bscCuETBAck,
       "bscCuETXAck": bscCuETXAck,
       "bscCuControl": bscCuControl,
       "bscCuOperationalMode": bscCuOperationalMode,
       "bscCuConnectionStatus": bscCuConnectionStatus,
       "bscCuConnectRequest": bscCuConnectRequest,
       "bscCuDisconnectRequest": bscCuDisconnectRequest,
       "bscCuDisconnectIndication": bscCuDisconnectIndication,
       "bscCuEndToEndConnectCnf": bscCuEndToEndConnectCnf,
       "bscCuSnalcRxRnr": bscCuSnalcRxRnr,
       "bscCuSnalcRxRr": bscCuSnalcRxRr,
       "bscDevTable": bscDevTable,
       "bscDevEntry": bscDevEntry,
       "bscDevSapNumber": bscDevSapNumber,
       "bscDevCuNumber": bscDevCuNumber,
       "bscDevNumber": bscDevNumber,
       "bscDevRowStatus": bscDevRowStatus,
       "bscDevType": bscDevType,
       "bscDevControl": bscDevControl,
       "bscDevOperationalMode": bscDevOperationalMode,
       "bscDevConnectionStatus": bscDevConnectionStatus,
       "bscDevState": bscDevState,
       "bscDevSSDeviceBusy": bscDevSSDeviceBusy,
       "bscDevSSUnitSpecify": bscDevSSUnitSpecify,
       "bscDevSSDeviceEnd": bscDevSSDeviceEnd,
       "bscDevSSTransmissionCheck": bscDevSSTransmissionCheck,
       "bscDevSSCommandReject": bscDevSSCommandReject,
       "bscDevSSInterventionRequired": bscDevSSInterventionRequired,
       "bscDevSSEquipmentCheck": bscDevSSEquipmentCheck,
       "bscDevSSDataCheck": bscDevSSDataCheck,
       "bscDevSSControlCheck": bscDevSSControlCheck,
       "bscDevSSOperationCheck": bscDevSSOperationCheck,
       "bscDevGeneralPoll": bscDevGeneralPoll,
       "bscDevSpecificPoll": bscDevSpecificPoll,
       "bscDevDeviceSelection": bscDevDeviceSelection,
       "bscDevTestRequest": bscDevTestRequest,
       "bscDevHostWrite": bscDevHostWrite,
       "bscDevHostRead": bscDevHostRead,
       "bscDevHostControl": bscDevHostControl,
       "bscDevCuShortRead": bscDevCuShortRead,
       "bscDevTxBlocks": bscDevTxBlocks,
       "bscDevRxBlocks": bscDevRxBlocks,
       "bscDevStatusSense": bscDevStatusSense,
       "bscDevError": bscDevError,
       "bscDevErrTimeout": bscDevErrTimeout,
       "bscDevCircuitEnable": bscDevCircuitEnable,
       "bscDevCircuitDisconnect": bscDevCircuitDisconnect,
       "bscDevCircuitRequest": bscDevCircuitRequest,
       "bscDevTxCommands": bscDevTxCommands,
       "bscDevRxCommands": bscDevRxCommands,
       "bscDevCommandsQueued": bscDevCommandsQueued,
       "bscDevBlocksQueued": bscDevBlocksQueued,
       "bscDevTxRvi": bscDevTxRvi,
       "bscDevRxRvi": bscDevRxRvi,
       "bscDevTxTtd": bscDevTxTtd,
       "bscDevRxTtd": bscDevRxTtd,
       "bscDevTxWack": bscDevTxWack,
       "bscDevRxWack": bscDevRxWack}
)

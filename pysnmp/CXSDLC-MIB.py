# SNMP MIB module (CXSDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXSDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:49 2024
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
 cxSDLC) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxSDLC")

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



class CuAddress(Integer32):
    """Custom type CuAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SdlcSapTable_Object = MibTable
sdlcSapTable = _SdlcSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1)
)
if mibBuilder.loadTexts:
    sdlcSapTable.setStatus("mandatory")
_SdlcSapEntry_Object = MibTableRow
sdlcSapEntry = _SdlcSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1)
)
sdlcSapEntry.setIndexNames(
    (0, "CXSDLC-MIB", "sdlcSapNumber"),
)
if mibBuilder.loadTexts:
    sdlcSapEntry.setStatus("mandatory")
_SdlcSapNumber_Type = SapIndex
_SdlcSapNumber_Object = MibTableColumn
sdlcSapNumber = _SdlcSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 1),
    _SdlcSapNumber_Type()
)
sdlcSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcSapNumber.setStatus("mandatory")


class _SdlcSapRowStatus_Type(Integer32):
    """Custom type sdlcSapRowStatus based on Integer32"""
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


_SdlcSapRowStatus_Type.__name__ = "Integer32"
_SdlcSapRowStatus_Object = MibTableColumn
sdlcSapRowStatus = _SdlcSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 2),
    _SdlcSapRowStatus_Type()
)
sdlcSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcSapRowStatus.setStatus("mandatory")


class _SdlcSapType_Type(Integer32):
    """Custom type sdlcSapType based on Integer32"""
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


_SdlcSapType_Type.__name__ = "Integer32"
_SdlcSapType_Object = MibTableColumn
sdlcSapType = _SdlcSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 3),
    _SdlcSapType_Type()
)
sdlcSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcSapType.setStatus("mandatory")


class _SdlcSapCuType_Type(Integer32):
    """Custom type sdlcSapCuType based on Integer32"""
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


_SdlcSapCuType_Type.__name__ = "Integer32"
_SdlcSapCuType_Object = MibTableColumn
sdlcSapCuType = _SdlcSapCuType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 4),
    _SdlcSapCuType_Type()
)
sdlcSapCuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcSapCuType.setStatus("mandatory")
_SdlcSapAlias_Type = Alias
_SdlcSapAlias_Object = MibTableColumn
sdlcSapAlias = _SdlcSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 5),
    _SdlcSapAlias_Type()
)
sdlcSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcSapAlias.setStatus("mandatory")
_SdlcSapCompanionAlias_Type = Alias
_SdlcSapCompanionAlias_Object = MibTableColumn
sdlcSapCompanionAlias = _SdlcSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 6),
    _SdlcSapCompanionAlias_Type()
)
sdlcSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcSapCompanionAlias.setStatus("mandatory")


class _SdlcSapSnalcRef_Type(Integer32):
    """Custom type sdlcSapSnalcRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SdlcSapSnalcRef_Type.__name__ = "Integer32"
_SdlcSapSnalcRef_Object = MibTableColumn
sdlcSapSnalcRef = _SdlcSapSnalcRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 7),
    _SdlcSapSnalcRef_Type()
)
sdlcSapSnalcRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcSapSnalcRef.setStatus("mandatory")


class _SdlcSapDuplex_Type(Integer32):
    """Custom type sdlcSapDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 1),
          ("halfduplex", 2))
    )


_SdlcSapDuplex_Type.__name__ = "Integer32"
_SdlcSapDuplex_Object = MibTableColumn
sdlcSapDuplex = _SdlcSapDuplex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 8),
    _SdlcSapDuplex_Type()
)
sdlcSapDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcSapDuplex.setStatus("mandatory")


class _SdlcSapRaiseDtrOnConnectReq_Type(Integer32):
    """Custom type sdlcSapRaiseDtrOnConnectReq based on Integer32"""
    defaultValue = 1

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


_SdlcSapRaiseDtrOnConnectReq_Type.__name__ = "Integer32"
_SdlcSapRaiseDtrOnConnectReq_Object = MibTableColumn
sdlcSapRaiseDtrOnConnectReq = _SdlcSapRaiseDtrOnConnectReq_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 9),
    _SdlcSapRaiseDtrOnConnectReq_Type()
)
sdlcSapRaiseDtrOnConnectReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcSapRaiseDtrOnConnectReq.setStatus("mandatory")


class _SdlcPollIntAfterAckTimer_Type(TimeTicks):
    """Custom type sdlcPollIntAfterAckTimer based on TimeTicks"""
    defaultValue = 0


_SdlcPollIntAfterAckTimer_Object = MibTableColumn
sdlcPollIntAfterAckTimer = _SdlcPollIntAfterAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 10),
    _SdlcPollIntAfterAckTimer_Type()
)
sdlcPollIntAfterAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcPollIntAfterAckTimer.setStatus("mandatory")


class _SdlcSapLineType_Type(Integer32):
    """Custom type sdlcSapLineType based on Integer32"""
    defaultValue = 2

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
        *(("negotiable", 2),
          ("standard", 1),
          ("switched", 3),
          ("switched-negotiable", 4))
    )


_SdlcSapLineType_Type.__name__ = "Integer32"
_SdlcSapLineType_Object = MibTableColumn
sdlcSapLineType = _SdlcSapLineType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 11),
    _SdlcSapLineType_Type()
)
sdlcSapLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcSapLineType.setStatus("mandatory")


class _SdlcSapControl_Type(Integer32):
    """Custom type sdlcSapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_SdlcSapControl_Type.__name__ = "Integer32"
_SdlcSapControl_Object = MibTableColumn
sdlcSapControl = _SdlcSapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 20),
    _SdlcSapControl_Type()
)
sdlcSapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sdlcSapControl.setStatus("mandatory")


class _SdlcSapOperationalMode_Type(Integer32):
    """Custom type sdlcSapOperationalMode based on Integer32"""
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


_SdlcSapOperationalMode_Type.__name__ = "Integer32"
_SdlcSapOperationalMode_Object = MibTableColumn
sdlcSapOperationalMode = _SdlcSapOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 30),
    _SdlcSapOperationalMode_Type()
)
sdlcSapOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcSapOperationalMode.setStatus("mandatory")


class _SdlcSapLinkStatus_Type(Integer32):
    """Custom type sdlcSapLinkStatus based on Integer32"""
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


_SdlcSapLinkStatus_Type.__name__ = "Integer32"
_SdlcSapLinkStatus_Object = MibTableColumn
sdlcSapLinkStatus = _SdlcSapLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 31),
    _SdlcSapLinkStatus_Type()
)
sdlcSapLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcSapLinkStatus.setStatus("mandatory")
_SdlcSapLinkChange_Type = Counter32
_SdlcSapLinkChange_Object = MibTableColumn
sdlcSapLinkChange = _SdlcSapLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 40),
    _SdlcSapLinkChange_Type()
)
sdlcSapLinkChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcSapLinkChange.setStatus("mandatory")
_SdlcSapTxDataFrames_Type = Counter32
_SdlcSapTxDataFrames_Object = MibTableColumn
sdlcSapTxDataFrames = _SdlcSapTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 41),
    _SdlcSapTxDataFrames_Type()
)
sdlcSapTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcSapTxDataFrames.setStatus("mandatory")
_SdlcSapRxDataFrames_Type = Counter32
_SdlcSapRxDataFrames_Object = MibTableColumn
sdlcSapRxDataFrames = _SdlcSapRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 42),
    _SdlcSapRxDataFrames_Type()
)
sdlcSapRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcSapRxDataFrames.setStatus("mandatory")
_SdlcSapConnectRequest_Type = Counter32
_SdlcSapConnectRequest_Object = MibTableColumn
sdlcSapConnectRequest = _SdlcSapConnectRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 43),
    _SdlcSapConnectRequest_Type()
)
sdlcSapConnectRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcSapConnectRequest.setStatus("mandatory")
_SdlcSapDisconnectRequest_Type = Counter32
_SdlcSapDisconnectRequest_Object = MibTableColumn
sdlcSapDisconnectRequest = _SdlcSapDisconnectRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 44),
    _SdlcSapDisconnectRequest_Type()
)
sdlcSapDisconnectRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcSapDisconnectRequest.setStatus("mandatory")
_SdlcSapDisconnectIndication_Type = Counter32
_SdlcSapDisconnectIndication_Object = MibTableColumn
sdlcSapDisconnectIndication = _SdlcSapDisconnectIndication_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 1, 1, 45),
    _SdlcSapDisconnectIndication_Type()
)
sdlcSapDisconnectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcSapDisconnectIndication.setStatus("mandatory")
_SdlcCuTable_Object = MibTable
sdlcCuTable = _SdlcCuTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2)
)
if mibBuilder.loadTexts:
    sdlcCuTable.setStatus("mandatory")
_SdlcCuEntry_Object = MibTableRow
sdlcCuEntry = _SdlcCuEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1)
)
sdlcCuEntry.setIndexNames(
    (0, "CXSDLC-MIB", "sdlcCuSap"),
    (0, "CXSDLC-MIB", "sdlcCuId"),
)
if mibBuilder.loadTexts:
    sdlcCuEntry.setStatus("mandatory")
_SdlcCuSap_Type = SapIndex
_SdlcCuSap_Object = MibTableColumn
sdlcCuSap = _SdlcCuSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 1),
    _SdlcCuSap_Type()
)
sdlcCuSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuSap.setStatus("mandatory")
_SdlcCuId_Type = CuAddress
_SdlcCuId_Object = MibTableColumn
sdlcCuId = _SdlcCuId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 2),
    _SdlcCuId_Type()
)
sdlcCuId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcCuId.setStatus("mandatory")


class _SdlcCuRowStatus_Type(Integer32):
    """Custom type sdlcCuRowStatus based on Integer32"""
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


_SdlcCuRowStatus_Type.__name__ = "Integer32"
_SdlcCuRowStatus_Object = MibTableColumn
sdlcCuRowStatus = _SdlcCuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 3),
    _SdlcCuRowStatus_Type()
)
sdlcCuRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcCuRowStatus.setStatus("mandatory")


class _SdlcCuMaxFrameLength_Type(Integer32):
    """Custom type sdlcCuMaxFrameLength based on Integer32"""
    defaultValue = 521

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_SdlcCuMaxFrameLength_Type.__name__ = "Integer32"
_SdlcCuMaxFrameLength_Object = MibTableColumn
sdlcCuMaxFrameLength = _SdlcCuMaxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 4),
    _SdlcCuMaxFrameLength_Type()
)
sdlcCuMaxFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcCuMaxFrameLength.setStatus("mandatory")


class _SdlcCuTransmitWindow_Type(Integer32):
    """Custom type sdlcCuTransmitWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_SdlcCuTransmitWindow_Type.__name__ = "Integer32"
_SdlcCuTransmitWindow_Object = MibTableColumn
sdlcCuTransmitWindow = _SdlcCuTransmitWindow_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 5),
    _SdlcCuTransmitWindow_Type()
)
sdlcCuTransmitWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcCuTransmitWindow.setStatus("mandatory")


class _SdlcCuPollRetry_Type(Integer32):
    """Custom type sdlcCuPollRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SdlcCuPollRetry_Type.__name__ = "Integer32"
_SdlcCuPollRetry_Object = MibTableColumn
sdlcCuPollRetry = _SdlcCuPollRetry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 6),
    _SdlcCuPollRetry_Type()
)
sdlcCuPollRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcCuPollRetry.setStatus("mandatory")


class _SdlcCuMaxRetry_Type(Integer32):
    """Custom type sdlcCuMaxRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SdlcCuMaxRetry_Type.__name__ = "Integer32"
_SdlcCuMaxRetry_Object = MibTableColumn
sdlcCuMaxRetry = _SdlcCuMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 7),
    _SdlcCuMaxRetry_Type()
)
sdlcCuMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcCuMaxRetry.setStatus("mandatory")


class _SdlcCuWaitForNextSnrmOrXid_Type(Integer32):
    """Custom type sdlcCuWaitForNextSnrmOrXid based on Integer32"""
    defaultValue = 1

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


_SdlcCuWaitForNextSnrmOrXid_Type.__name__ = "Integer32"
_SdlcCuWaitForNextSnrmOrXid_Object = MibTableColumn
sdlcCuWaitForNextSnrmOrXid = _SdlcCuWaitForNextSnrmOrXid_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 8),
    _SdlcCuWaitForNextSnrmOrXid_Type()
)
sdlcCuWaitForNextSnrmOrXid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcCuWaitForNextSnrmOrXid.setStatus("mandatory")


class _SdlcCuSendDisconnect_Type(Integer32):
    """Custom type sdlcCuSendDisconnect based on Integer32"""
    defaultValue = 2

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


_SdlcCuSendDisconnect_Type.__name__ = "Integer32"
_SdlcCuSendDisconnect_Object = MibTableColumn
sdlcCuSendDisconnect = _SdlcCuSendDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 9),
    _SdlcCuSendDisconnect_Type()
)
sdlcCuSendDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcCuSendDisconnect.setStatus("mandatory")


class _SdlcCuPollAckTimer_Type(TimeTicks):
    """Custom type sdlcCuPollAckTimer based on TimeTicks"""
    defaultValue = 20


_SdlcCuPollAckTimer_Object = MibTableColumn
sdlcCuPollAckTimer = _SdlcCuPollAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 10),
    _SdlcCuPollAckTimer_Type()
)
sdlcCuPollAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcCuPollAckTimer.setStatus("mandatory")


class _SdlcCuSlowPollTimer_Type(TimeTicks):
    """Custom type sdlcCuSlowPollTimer based on TimeTicks"""
    defaultValue = 10


_SdlcCuSlowPollTimer_Object = MibTableColumn
sdlcCuSlowPollTimer = _SdlcCuSlowPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 11),
    _SdlcCuSlowPollTimer_Type()
)
sdlcCuSlowPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcCuSlowPollTimer.setStatus("mandatory")


class _SdlcCuWaitForUaFromSnalcTimer_Type(TimeTicks):
    """Custom type sdlcCuWaitForUaFromSnalcTimer based on TimeTicks"""
    defaultValue = 0


_SdlcCuWaitForUaFromSnalcTimer_Object = MibTableColumn
sdlcCuWaitForUaFromSnalcTimer = _SdlcCuWaitForUaFromSnalcTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 13),
    _SdlcCuWaitForUaFromSnalcTimer_Type()
)
sdlcCuWaitForUaFromSnalcTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcCuWaitForUaFromSnalcTimer.setStatus("mandatory")


class _SdlcCuControl_Type(Integer32):
    """Custom type sdlcCuControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_SdlcCuControl_Type.__name__ = "Integer32"
_SdlcCuControl_Object = MibTableColumn
sdlcCuControl = _SdlcCuControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 30),
    _SdlcCuControl_Type()
)
sdlcCuControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sdlcCuControl.setStatus("mandatory")


class _SdlcCuState_Type(Integer32):
    """Custom type sdlcCuState based on Integer32"""
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
        *(("discSent", 8),
          ("normalDiscMode", 1),
          ("normalResponseMode", 4),
          ("receivedDisc", 6),
          ("receivedSnrm", 3),
          ("remoteDiscReceived", 9),
          ("snrmSent", 7),
          ("waitForDisc", 5),
          ("waitForSnrm", 2),
          ("xidExchange", 10))
    )


_SdlcCuState_Type.__name__ = "Integer32"
_SdlcCuState_Object = MibTableColumn
sdlcCuState = _SdlcCuState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 40),
    _SdlcCuState_Type()
)
sdlcCuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuState.setStatus("mandatory")


class _SdlcCuOperationalMode_Type(Integer32):
    """Custom type sdlcCuOperationalMode based on Integer32"""
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


_SdlcCuOperationalMode_Type.__name__ = "Integer32"
_SdlcCuOperationalMode_Object = MibTableColumn
sdlcCuOperationalMode = _SdlcCuOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 41),
    _SdlcCuOperationalMode_Type()
)
sdlcCuOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuOperationalMode.setStatus("mandatory")


class _SdlcCuDiscReasonCode_Type(Integer32):
    """Custom type sdlcCuDiscReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SdlcCuDiscReasonCode_Type.__name__ = "Integer32"
_SdlcCuDiscReasonCode_Object = MibTableColumn
sdlcCuDiscReasonCode = _SdlcCuDiscReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 42),
    _SdlcCuDiscReasonCode_Type()
)
sdlcCuDiscReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuDiscReasonCode.setStatus("mandatory")


class _SdlcCuSnalcDiscReasonCode_Type(Integer32):
    """Custom type sdlcCuSnalcDiscReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SdlcCuSnalcDiscReasonCode_Type.__name__ = "Integer32"
_SdlcCuSnalcDiscReasonCode_Object = MibTableColumn
sdlcCuSnalcDiscReasonCode = _SdlcCuSnalcDiscReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 43),
    _SdlcCuSnalcDiscReasonCode_Type()
)
sdlcCuSnalcDiscReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuSnalcDiscReasonCode.setStatus("mandatory")


class _SdlcCuConnectionStatus_Type(Integer32):
    """Custom type sdlcCuConnectionStatus based on Integer32"""
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


_SdlcCuConnectionStatus_Type.__name__ = "Integer32"
_SdlcCuConnectionStatus_Object = MibTableColumn
sdlcCuConnectionStatus = _SdlcCuConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 44),
    _SdlcCuConnectionStatus_Type()
)
sdlcCuConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuConnectionStatus.setStatus("mandatory")
_SdlcCuFramesInTransmitQueue_Type = Counter32
_SdlcCuFramesInTransmitQueue_Object = MibTableColumn
sdlcCuFramesInTransmitQueue = _SdlcCuFramesInTransmitQueue_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 50),
    _SdlcCuFramesInTransmitQueue_Type()
)
sdlcCuFramesInTransmitQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuFramesInTransmitQueue.setStatus("mandatory")
_SdlcCuTxFrames_Type = Counter32
_SdlcCuTxFrames_Object = MibTableColumn
sdlcCuTxFrames = _SdlcCuTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 51),
    _SdlcCuTxFrames_Type()
)
sdlcCuTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuTxFrames.setStatus("mandatory")
_SdlcCuRxFrames_Type = Counter32
_SdlcCuRxFrames_Object = MibTableColumn
sdlcCuRxFrames = _SdlcCuRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 52),
    _SdlcCuRxFrames_Type()
)
sdlcCuRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuRxFrames.setStatus("mandatory")
_SdlcCuTimeOuts_Type = Counter32
_SdlcCuTimeOuts_Object = MibTableColumn
sdlcCuTimeOuts = _SdlcCuTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 55),
    _SdlcCuTimeOuts_Type()
)
sdlcCuTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuTimeOuts.setStatus("mandatory")
_SdlcCuSnrmCount_Type = Counter32
_SdlcCuSnrmCount_Object = MibTableColumn
sdlcCuSnrmCount = _SdlcCuSnrmCount_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 56),
    _SdlcCuSnrmCount_Type()
)
sdlcCuSnrmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuSnrmCount.setStatus("mandatory")
_SdlcCuXidCommand_Type = Counter32
_SdlcCuXidCommand_Object = MibTableColumn
sdlcCuXidCommand = _SdlcCuXidCommand_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 57),
    _SdlcCuXidCommand_Type()
)
sdlcCuXidCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuXidCommand.setStatus("mandatory")
_SdlcCuXidResponse_Type = Counter32
_SdlcCuXidResponse_Object = MibTableColumn
sdlcCuXidResponse = _SdlcCuXidResponse_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 58),
    _SdlcCuXidResponse_Type()
)
sdlcCuXidResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuXidResponse.setStatus("mandatory")
_SdlcCuUnnumberedAcks_Type = Counter32
_SdlcCuUnnumberedAcks_Object = MibTableColumn
sdlcCuUnnumberedAcks = _SdlcCuUnnumberedAcks_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 59),
    _SdlcCuUnnumberedAcks_Type()
)
sdlcCuUnnumberedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuUnnumberedAcks.setStatus("mandatory")
_SdlcCuRetransmission_Type = Counter32
_SdlcCuRetransmission_Object = MibTableColumn
sdlcCuRetransmission = _SdlcCuRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 60),
    _SdlcCuRetransmission_Type()
)
sdlcCuRetransmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuRetransmission.setStatus("mandatory")
_SdlcCuDisconnectCount_Type = Counter32
_SdlcCuDisconnectCount_Object = MibTableColumn
sdlcCuDisconnectCount = _SdlcCuDisconnectCount_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 61),
    _SdlcCuDisconnectCount_Type()
)
sdlcCuDisconnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuDisconnectCount.setStatus("mandatory")
_SdlcCuDisconnectModeCount_Type = Counter32
_SdlcCuDisconnectModeCount_Object = MibTableColumn
sdlcCuDisconnectModeCount = _SdlcCuDisconnectModeCount_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 62),
    _SdlcCuDisconnectModeCount_Type()
)
sdlcCuDisconnectModeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuDisconnectModeCount.setStatus("mandatory")
_SdlcCuTransmittedRNR_Type = Counter32
_SdlcCuTransmittedRNR_Object = MibTableColumn
sdlcCuTransmittedRNR = _SdlcCuTransmittedRNR_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 63),
    _SdlcCuTransmittedRNR_Type()
)
sdlcCuTransmittedRNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuTransmittedRNR.setStatus("mandatory")
_SdlcCuReceivedRNR_Type = Counter32
_SdlcCuReceivedRNR_Object = MibTableColumn
sdlcCuReceivedRNR = _SdlcCuReceivedRNR_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 64),
    _SdlcCuReceivedRNR_Type()
)
sdlcCuReceivedRNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuReceivedRNR.setStatus("mandatory")
_SdlcCuFrameRejects_Type = Counter32
_SdlcCuFrameRejects_Object = MibTableColumn
sdlcCuFrameRejects = _SdlcCuFrameRejects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 65),
    _SdlcCuFrameRejects_Type()
)
sdlcCuFrameRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuFrameRejects.setStatus("mandatory")
_SdlcCuRemoteDisc_Type = Counter32
_SdlcCuRemoteDisc_Object = MibTableColumn
sdlcCuRemoteDisc = _SdlcCuRemoteDisc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 66),
    _SdlcCuRemoteDisc_Type()
)
sdlcCuRemoteDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuRemoteDisc.setStatus("mandatory")
_SdlcCuConnectionRequest_Type = Counter32
_SdlcCuConnectionRequest_Object = MibTableColumn
sdlcCuConnectionRequest = _SdlcCuConnectionRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 67),
    _SdlcCuConnectionRequest_Type()
)
sdlcCuConnectionRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuConnectionRequest.setStatus("mandatory")
_SdlcCuDisconnectionRequest_Type = Counter32
_SdlcCuDisconnectionRequest_Object = MibTableColumn
sdlcCuDisconnectionRequest = _SdlcCuDisconnectionRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 68),
    _SdlcCuDisconnectionRequest_Type()
)
sdlcCuDisconnectionRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuDisconnectionRequest.setStatus("mandatory")
_SdlcCuDisconnectionIndication_Type = Counter32
_SdlcCuDisconnectionIndication_Object = MibTableColumn
sdlcCuDisconnectionIndication = _SdlcCuDisconnectionIndication_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 37, 2, 1, 69),
    _SdlcCuDisconnectionIndication_Type()
)
sdlcCuDisconnectionIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCuDisconnectionIndication.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXSDLC-MIB",
    **{"CuAddress": CuAddress,
       "sdlcSapTable": sdlcSapTable,
       "sdlcSapEntry": sdlcSapEntry,
       "sdlcSapNumber": sdlcSapNumber,
       "sdlcSapRowStatus": sdlcSapRowStatus,
       "sdlcSapType": sdlcSapType,
       "sdlcSapCuType": sdlcSapCuType,
       "sdlcSapAlias": sdlcSapAlias,
       "sdlcSapCompanionAlias": sdlcSapCompanionAlias,
       "sdlcSapSnalcRef": sdlcSapSnalcRef,
       "sdlcSapDuplex": sdlcSapDuplex,
       "sdlcSapRaiseDtrOnConnectReq": sdlcSapRaiseDtrOnConnectReq,
       "sdlcPollIntAfterAckTimer": sdlcPollIntAfterAckTimer,
       "sdlcSapLineType": sdlcSapLineType,
       "sdlcSapControl": sdlcSapControl,
       "sdlcSapOperationalMode": sdlcSapOperationalMode,
       "sdlcSapLinkStatus": sdlcSapLinkStatus,
       "sdlcSapLinkChange": sdlcSapLinkChange,
       "sdlcSapTxDataFrames": sdlcSapTxDataFrames,
       "sdlcSapRxDataFrames": sdlcSapRxDataFrames,
       "sdlcSapConnectRequest": sdlcSapConnectRequest,
       "sdlcSapDisconnectRequest": sdlcSapDisconnectRequest,
       "sdlcSapDisconnectIndication": sdlcSapDisconnectIndication,
       "sdlcCuTable": sdlcCuTable,
       "sdlcCuEntry": sdlcCuEntry,
       "sdlcCuSap": sdlcCuSap,
       "sdlcCuId": sdlcCuId,
       "sdlcCuRowStatus": sdlcCuRowStatus,
       "sdlcCuMaxFrameLength": sdlcCuMaxFrameLength,
       "sdlcCuTransmitWindow": sdlcCuTransmitWindow,
       "sdlcCuPollRetry": sdlcCuPollRetry,
       "sdlcCuMaxRetry": sdlcCuMaxRetry,
       "sdlcCuWaitForNextSnrmOrXid": sdlcCuWaitForNextSnrmOrXid,
       "sdlcCuSendDisconnect": sdlcCuSendDisconnect,
       "sdlcCuPollAckTimer": sdlcCuPollAckTimer,
       "sdlcCuSlowPollTimer": sdlcCuSlowPollTimer,
       "sdlcCuWaitForUaFromSnalcTimer": sdlcCuWaitForUaFromSnalcTimer,
       "sdlcCuControl": sdlcCuControl,
       "sdlcCuState": sdlcCuState,
       "sdlcCuOperationalMode": sdlcCuOperationalMode,
       "sdlcCuDiscReasonCode": sdlcCuDiscReasonCode,
       "sdlcCuSnalcDiscReasonCode": sdlcCuSnalcDiscReasonCode,
       "sdlcCuConnectionStatus": sdlcCuConnectionStatus,
       "sdlcCuFramesInTransmitQueue": sdlcCuFramesInTransmitQueue,
       "sdlcCuTxFrames": sdlcCuTxFrames,
       "sdlcCuRxFrames": sdlcCuRxFrames,
       "sdlcCuTimeOuts": sdlcCuTimeOuts,
       "sdlcCuSnrmCount": sdlcCuSnrmCount,
       "sdlcCuXidCommand": sdlcCuXidCommand,
       "sdlcCuXidResponse": sdlcCuXidResponse,
       "sdlcCuUnnumberedAcks": sdlcCuUnnumberedAcks,
       "sdlcCuRetransmission": sdlcCuRetransmission,
       "sdlcCuDisconnectCount": sdlcCuDisconnectCount,
       "sdlcCuDisconnectModeCount": sdlcCuDisconnectModeCount,
       "sdlcCuTransmittedRNR": sdlcCuTransmittedRNR,
       "sdlcCuReceivedRNR": sdlcCuReceivedRNR,
       "sdlcCuFrameRejects": sdlcCuFrameRejects,
       "sdlcCuRemoteDisc": sdlcCuRemoteDisc,
       "sdlcCuConnectionRequest": sdlcCuConnectionRequest,
       "sdlcCuDisconnectionRequest": sdlcCuDisconnectionRequest,
       "sdlcCuDisconnectionIndication": sdlcCuDisconnectionIndication}
)

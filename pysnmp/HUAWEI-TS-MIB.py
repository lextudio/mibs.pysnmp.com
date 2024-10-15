# SNMP MIB module (HUAWEI-TS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-TS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:17 2024
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

(huawei,
 mlsr) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "huawei",
    "mlsr")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TerminalServer_ObjectIdentity = ObjectIdentity
terminalServer = _TerminalServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1)
)
_TsAppTable_Object = MibTable
tsAppTable = _TsAppTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1)
)
if mibBuilder.loadTexts:
    tsAppTable.setStatus("mandatory")
_TsAppEntry_Object = MibTableRow
tsAppEntry = _TsAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1)
)
tsAppEntry.setIndexNames(
    (0, "HUAWEI-TS-MIB", "tsAppID"),
)
if mibBuilder.loadTexts:
    tsAppEntry.setStatus("mandatory")


class _TsAppID_Type(Integer32):
    """Custom type tsAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 515),
    )


_TsAppID_Type.__name__ = "Integer32"
_TsAppID_Object = MibTableColumn
tsAppID = _TsAppID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 1),
    _TsAppID_Type()
)
tsAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAppID.setStatus("mandatory")


class _TsAppIPAddress_Type(IpAddress):
    """Custom type tsAppIPAddress based on IpAddress"""
    defaultValue = 0


_TsAppIPAddress_Object = MibTableColumn
tsAppIPAddress = _TsAppIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 2),
    _TsAppIPAddress_Type()
)
tsAppIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsAppIPAddress.setStatus("mandatory")


class _TsAppPort_Type(Integer32):
    """Custom type tsAppPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1025, 65535),
    )


_TsAppPort_Type.__name__ = "Integer32"
_TsAppPort_Object = MibTableColumn
tsAppPort = _TsAppPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 3),
    _TsAppPort_Type()
)
tsAppPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsAppPort.setStatus("mandatory")


class _TsAppType_Type(Integer32):
    """Custom type tsAppType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("special", 2))
    )


_TsAppType_Type.__name__ = "Integer32"
_TsAppType_Object = MibTableColumn
tsAppType = _TsAppType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 4),
    _TsAppType_Type()
)
tsAppType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsAppType.setStatus("mandatory")


class _TsAppName_Type(DisplayString):
    """Custom type tsAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_TsAppName_Type.__name__ = "DisplayString"
_TsAppName_Object = MibTableColumn
tsAppName = _TsAppName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 5),
    _TsAppName_Type()
)
tsAppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsAppName.setStatus("mandatory")


class _TsAppSourceIP_Type(IpAddress):
    """Custom type tsAppSourceIP based on IpAddress"""
    defaultValue = 0


_TsAppSourceIP_Object = MibTableColumn
tsAppSourceIP = _TsAppSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 6),
    _TsAppSourceIP_Type()
)
tsAppSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsAppSourceIP.setStatus("mandatory")


class _TsAppLocalPort_Type(Integer32):
    """Custom type tsAppLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
        ValueRangeConstraint(0, 0),
    )


_TsAppLocalPort_Type.__name__ = "Integer32"
_TsAppLocalPort_Object = MibTableColumn
tsAppLocalPort = _TsAppLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 7),
    _TsAppLocalPort_Type()
)
tsAppLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAppLocalPort.setStatus("mandatory")


class _TsAppTtyServerState_Type(Integer32):
    """Custom type tsAppTtyServerState based on Integer32"""
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
        *(("kept", 2),
          ("linked", 4),
          ("linking", 3),
          ("noset", 1),
          ("overcast", 6),
          ("removed", 5))
    )


_TsAppTtyServerState_Type.__name__ = "Integer32"
_TsAppTtyServerState_Object = MibTableColumn
tsAppTtyServerState = _TsAppTtyServerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 8),
    _TsAppTtyServerState_Type()
)
tsAppTtyServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAppTtyServerState.setStatus("mandatory")
_TsAppSocketRecvBufSize_Type = Integer32
_TsAppSocketRecvBufSize_Object = MibTableColumn
tsAppSocketRecvBufSize = _TsAppSocketRecvBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 9),
    _TsAppSocketRecvBufSize_Type()
)
tsAppSocketRecvBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAppSocketRecvBufSize.setStatus("mandatory")
_TsAppSocketSendBufSize_Type = Integer32
_TsAppSocketSendBufSize_Object = MibTableColumn
tsAppSocketSendBufSize = _TsAppSocketSendBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 10),
    _TsAppSocketSendBufSize_Type()
)
tsAppSocketSendBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAppSocketSendBufSize.setStatus("mandatory")
_TsAppSockRecvByte_Type = Integer32
_TsAppSockRecvByte_Object = MibTableColumn
tsAppSockRecvByte = _TsAppSockRecvByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 11),
    _TsAppSockRecvByte_Type()
)
tsAppSockRecvByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAppSockRecvByte.setStatus("mandatory")
_TsAppSockSendByte_Type = Integer32
_TsAppSockSendByte_Object = MibTableColumn
tsAppSockSendByte = _TsAppSockSendByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 12),
    _TsAppSockSendByte_Type()
)
tsAppSockSendByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAppSockSendByte.setStatus("mandatory")
_TsAppLastRecvTime_Type = DisplayString
_TsAppLastRecvTime_Object = MibTableColumn
tsAppLastRecvTime = _TsAppLastRecvTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 13),
    _TsAppLastRecvTime_Type()
)
tsAppLastRecvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAppLastRecvTime.setStatus("mandatory")
_TsAppLastSendTime_Type = DisplayString
_TsAppLastSendTime_Object = MibTableColumn
tsAppLastSendTime = _TsAppLastSendTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 14),
    _TsAppLastSendTime_Type()
)
tsAppLastSendTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAppLastSendTime.setStatus("mandatory")


class _TsAppClearStatistic_Type(Integer32):
    """Custom type tsAppClearStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TsAppClearStatistic_Type.__name__ = "Integer32"
_TsAppClearStatistic_Object = MibTableColumn
tsAppClearStatistic = _TsAppClearStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 15),
    _TsAppClearStatistic_Type()
)
tsAppClearStatistic.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tsAppClearStatistic.setStatus("mandatory")


class _TsAppUnixIndex_Type(Integer32):
    """Custom type tsAppUnixIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_TsAppUnixIndex_Type.__name__ = "Integer32"
_TsAppUnixIndex_Object = MibTableColumn
tsAppUnixIndex = _TsAppUnixIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 16),
    _TsAppUnixIndex_Type()
)
tsAppUnixIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAppUnixIndex.setStatus("mandatory")
_TsAppStatus_Type = EntryStatus
_TsAppStatus_Object = MibTableColumn
tsAppStatus = _TsAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 1, 1, 17),
    _TsAppStatus_Type()
)
tsAppStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsAppStatus.setStatus("mandatory")
_TsAsyModeTtyTable_Object = MibTable
tsAsyModeTtyTable = _TsAsyModeTtyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 2)
)
if mibBuilder.loadTexts:
    tsAsyModeTtyTable.setStatus("mandatory")
_TsAsyModeTtyEntry_Object = MibTableRow
tsAsyModeTtyEntry = _TsAsyModeTtyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 2, 1)
)
tsAsyModeTtyEntry.setIndexNames(
    (0, "HUAWEI-TS-MIB", "tsAsyModeTtyID"),
    (0, "HUAWEI-TS-MIB", "tsAsyModeTtyVtyID"),
)
if mibBuilder.loadTexts:
    tsAsyModeTtyEntry.setStatus("mandatory")


class _TsAsyModeTtyID_Type(Integer32):
    """Custom type tsAsyModeTtyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TsAsyModeTtyID_Type.__name__ = "Integer32"
_TsAsyModeTtyID_Object = MibTableColumn
tsAsyModeTtyID = _TsAsyModeTtyID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 2, 1, 1),
    _TsAsyModeTtyID_Type()
)
tsAsyModeTtyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAsyModeTtyID.setStatus("mandatory")


class _TsAsyModeTtyVtyID_Type(Integer32):
    """Custom type tsAsyModeTtyVtyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TsAsyModeTtyVtyID_Type.__name__ = "Integer32"
_TsAsyModeTtyVtyID_Object = MibTableColumn
tsAsyModeTtyVtyID = _TsAsyModeTtyVtyID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 2, 1, 2),
    _TsAsyModeTtyVtyID_Type()
)
tsAsyModeTtyVtyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAsyModeTtyVtyID.setStatus("mandatory")
_TsAsyModeTtyIFIndex_Type = Integer32
_TsAsyModeTtyIFIndex_Object = MibTableColumn
tsAsyModeTtyIFIndex = _TsAsyModeTtyIFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 2, 1, 3),
    _TsAsyModeTtyIFIndex_Type()
)
tsAsyModeTtyIFIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsAsyModeTtyIFIndex.setStatus("mandatory")


class _TsAsyModeTtyAppID_Type(Integer32):
    """Custom type tsAsyModeTtyAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 515),
    )


_TsAsyModeTtyAppID_Type.__name__ = "Integer32"
_TsAsyModeTtyAppID_Object = MibTableColumn
tsAsyModeTtyAppID = _TsAsyModeTtyAppID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 2, 1, 4),
    _TsAsyModeTtyAppID_Type()
)
tsAsyModeTtyAppID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsAsyModeTtyAppID.setStatus("mandatory")


class _TsAsyModeTtyDisconnect_Type(Integer32):
    """Custom type tsAsyModeTtyDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disconnect", 1)
    )


_TsAsyModeTtyDisconnect_Type.__name__ = "Integer32"
_TsAsyModeTtyDisconnect_Object = MibTableColumn
tsAsyModeTtyDisconnect = _TsAsyModeTtyDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 2, 1, 5),
    _TsAsyModeTtyDisconnect_Type()
)
tsAsyModeTtyDisconnect.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tsAsyModeTtyDisconnect.setStatus("mandatory")


class _TsAsyModeTtyVtyState_Type(Integer32):
    """Custom type tsAsyModeTtyVtyState based on Integer32"""
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
        *(("down", 1),
          ("menu", 5),
          ("ok", 4),
          ("up", 2),
          ("waitaaa", 3))
    )


_TsAsyModeTtyVtyState_Type.__name__ = "Integer32"
_TsAsyModeTtyVtyState_Object = MibTableColumn
tsAsyModeTtyVtyState = _TsAsyModeTtyVtyState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 2, 1, 6),
    _TsAsyModeTtyVtyState_Type()
)
tsAsyModeTtyVtyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAsyModeTtyVtyState.setStatus("mandatory")


class _TsAsyModeTtyFlowCtrlState_Type(Integer32):
    """Custom type tsAsyModeTtyFlowCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_TsAsyModeTtyFlowCtrlState_Type.__name__ = "Integer32"
_TsAsyModeTtyFlowCtrlState_Object = MibTableColumn
tsAsyModeTtyFlowCtrlState = _TsAsyModeTtyFlowCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 2, 1, 7),
    _TsAsyModeTtyFlowCtrlState_Type()
)
tsAsyModeTtyFlowCtrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsAsyModeTtyFlowCtrlState.setStatus("mandatory")
_TsAsyModeTtyStatus_Type = EntryStatus
_TsAsyModeTtyStatus_Object = MibTableColumn
tsAsyModeTtyStatus = _TsAsyModeTtyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 2, 1, 8),
    _TsAsyModeTtyStatus_Type()
)
tsAsyModeTtyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsAsyModeTtyStatus.setStatus("mandatory")
_TsTtyTable_Object = MibTable
tsTtyTable = _TsTtyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3)
)
if mibBuilder.loadTexts:
    tsTtyTable.setStatus("mandatory")
_TsTtyEntry_Object = MibTableRow
tsTtyEntry = _TsTtyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1)
)
tsTtyEntry.setIndexNames(
    (0, "HUAWEI-TS-MIB", "tsTtyID"),
)
if mibBuilder.loadTexts:
    tsTtyEntry.setStatus("mandatory")


class _TsTtyID_Type(Integer32):
    """Custom type tsTtyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TsTtyID_Type.__name__ = "Integer32"
_TsTtyID_Object = MibTableColumn
tsTtyID = _TsTtyID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 1),
    _TsTtyID_Type()
)
tsTtyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyID.setStatus("mandatory")


class _TsTtyBufferSize_Type(Integer32):
    """Custom type tsTtyBufferSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 204800),
    )


_TsTtyBufferSize_Type.__name__ = "Integer32"
_TsTtyBufferSize_Object = MibTableColumn
tsTtyBufferSize = _TsTtyBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 2),
    _TsTtyBufferSize_Type()
)
tsTtyBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyBufferSize.setStatus("mandatory")


class _TsTtyAutoLink_Type(Integer32):
    """Custom type tsTtyAutoLink based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 3600),
    )


_TsTtyAutoLink_Type.__name__ = "Integer32"
_TsTtyAutoLink_Object = MibTableColumn
tsTtyAutoLink = _TsTtyAutoLink_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 3),
    _TsTtyAutoLink_Type()
)
tsTtyAutoLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyAutoLink.setStatus("mandatory")


class _TsTtyCloseLink_Type(Integer32):
    """Custom type tsTtyCloseLink based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 3600),
    )


_TsTtyCloseLink_Type.__name__ = "Integer32"
_TsTtyCloseLink_Object = MibTableColumn
tsTtyCloseLink = _TsTtyCloseLink_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 4),
    _TsTtyCloseLink_Type()
)
tsTtyCloseLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyCloseLink.setStatus("mandatory")


class _TsTtyConnPrint_Type(Integer32):
    """Custom type tsTtyConnPrint based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chinese", 2),
          ("english", 1),
          ("none", 3))
    )


_TsTtyConnPrint_Type.__name__ = "Integer32"
_TsTtyConnPrint_Object = MibTableColumn
tsTtyConnPrint = _TsTtyConnPrint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 5),
    _TsTtyConnPrint_Type()
)
tsTtyConnPrint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyConnPrint.setStatus("mandatory")


class _TsTtyDelay_Type(Integer32):
    """Custom type tsTtyDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_TsTtyDelay_Type.__name__ = "Integer32"
_TsTtyDelay_Object = MibTableColumn
tsTtyDelay = _TsTtyDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 6),
    _TsTtyDelay_Type()
)
tsTtyDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyDelay.setStatus("mandatory")


class _TsTtyLogoPrint_Type(Integer32):
    """Custom type tsTtyLogoPrint based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsTtyLogoPrint_Type.__name__ = "Integer32"
_TsTtyLogoPrint_Object = MibTableColumn
tsTtyLogoPrint = _TsTtyLogoPrint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 7),
    _TsTtyLogoPrint_Type()
)
tsTtyLogoPrint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyLogoPrint.setStatus("mandatory")


class _TsTtyMenuKey1_Type(Integer32):
    """Custom type tsTtyMenuKey1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyMenuKey1_Type.__name__ = "Integer32"
_TsTtyMenuKey1_Object = MibTableColumn
tsTtyMenuKey1 = _TsTtyMenuKey1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 8),
    _TsTtyMenuKey1_Type()
)
tsTtyMenuKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyMenuKey1.setStatus("mandatory")


class _TsTtyMenuKey2_Type(Integer32):
    """Custom type tsTtyMenuKey2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyMenuKey2_Type.__name__ = "Integer32"
_TsTtyMenuKey2_Object = MibTableColumn
tsTtyMenuKey2 = _TsTtyMenuKey2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 9),
    _TsTtyMenuKey2_Type()
)
tsTtyMenuKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyMenuKey2.setStatus("mandatory")


class _TsTtyMenuKey3_Type(Integer32):
    """Custom type tsTtyMenuKey3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyMenuKey3_Type.__name__ = "Integer32"
_TsTtyMenuKey3_Object = MibTableColumn
tsTtyMenuKey3 = _TsTtyMenuKey3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 10),
    _TsTtyMenuKey3_Type()
)
tsTtyMenuKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyMenuKey3.setStatus("mandatory")


class _TsTtyReadBlock_Type(Integer32):
    """Custom type tsTtyReadBlock based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSet", 2),
          ("set", 1))
    )


_TsTtyReadBlock_Type.__name__ = "Integer32"
_TsTtyReadBlock_Object = MibTableColumn
tsTtyReadBlock = _TsTtyReadBlock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 11),
    _TsTtyReadBlock_Type()
)
tsTtyReadBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyReadBlock.setStatus("mandatory")


class _TsTtyRedrawkey1_Type(Integer32):
    """Custom type tsTtyRedrawkey1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyRedrawkey1_Type.__name__ = "Integer32"
_TsTtyRedrawkey1_Object = MibTableColumn
tsTtyRedrawkey1 = _TsTtyRedrawkey1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 12),
    _TsTtyRedrawkey1_Type()
)
tsTtyRedrawkey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyRedrawkey1.setStatus("mandatory")


class _TsTtyRedrawkey2_Type(Integer32):
    """Custom type tsTtyRedrawkey2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyRedrawkey2_Type.__name__ = "Integer32"
_TsTtyRedrawkey2_Object = MibTableColumn
tsTtyRedrawkey2 = _TsTtyRedrawkey2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 13),
    _TsTtyRedrawkey2_Type()
)
tsTtyRedrawkey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyRedrawkey2.setStatus("mandatory")


class _TsTtyRedrawkey3_Type(Integer32):
    """Custom type tsTtyRedrawkey3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyRedrawkey3_Type.__name__ = "Integer32"
_TsTtyRedrawkey3_Object = MibTableColumn
tsTtyRedrawkey3 = _TsTtyRedrawkey3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 14),
    _TsTtyRedrawkey3_Type()
)
tsTtyRedrawkey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyRedrawkey3.setStatus("mandatory")


class _TsTtyResetKey1_Type(Integer32):
    """Custom type tsTtyResetKey1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyResetKey1_Type.__name__ = "Integer32"
_TsTtyResetKey1_Object = MibTableColumn
tsTtyResetKey1 = _TsTtyResetKey1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 15),
    _TsTtyResetKey1_Type()
)
tsTtyResetKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyResetKey1.setStatus("mandatory")


class _TsTtyResetKey2_Type(Integer32):
    """Custom type tsTtyResetKey2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyResetKey2_Type.__name__ = "Integer32"
_TsTtyResetKey2_Object = MibTableColumn
tsTtyResetKey2 = _TsTtyResetKey2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 16),
    _TsTtyResetKey2_Type()
)
tsTtyResetKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyResetKey2.setStatus("mandatory")


class _TsTtyResetKey3_Type(Integer32):
    """Custom type tsTtyResetKey3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyResetKey3_Type.__name__ = "Integer32"
_TsTtyResetKey3_Object = MibTableColumn
tsTtyResetKey3 = _TsTtyResetKey3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 17),
    _TsTtyResetKey3_Type()
)
tsTtyResetKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyResetKey3.setStatus("mandatory")


class _TsTtyTcpNoDelay_Type(Integer32):
    """Custom type tsTtyTcpNoDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsTtyTcpNoDelay_Type.__name__ = "Integer32"
_TsTtyTcpNoDelay_Object = MibTableColumn
tsTtyTcpNoDelay = _TsTtyTcpNoDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 18),
    _TsTtyTcpNoDelay_Type()
)
tsTtyTcpNoDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyTcpNoDelay.setStatus("mandatory")


class _TsTtyTcpRecvBufferSize_Type(Integer32):
    """Custom type tsTtyTcpRecvBufferSize based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_TsTtyTcpRecvBufferSize_Type.__name__ = "Integer32"
_TsTtyTcpRecvBufferSize_Object = MibTableColumn
tsTtyTcpRecvBufferSize = _TsTtyTcpRecvBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 19),
    _TsTtyTcpRecvBufferSize_Type()
)
tsTtyTcpRecvBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyTcpRecvBufferSize.setStatus("mandatory")


class _TsTtyTcpSendBufferSize_Type(Integer32):
    """Custom type tsTtyTcpSendBufferSize based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16384),
    )


_TsTtyTcpSendBufferSize_Type.__name__ = "Integer32"
_TsTtyTcpSendBufferSize_Object = MibTableColumn
tsTtyTcpSendBufferSize = _TsTtyTcpSendBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 20),
    _TsTtyTcpSendBufferSize_Type()
)
tsTtyTcpSendBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyTcpSendBufferSize.setStatus("mandatory")


class _TsTtyTestKey1_Type(Integer32):
    """Custom type tsTtyTestKey1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyTestKey1_Type.__name__ = "Integer32"
_TsTtyTestKey1_Object = MibTableColumn
tsTtyTestKey1 = _TsTtyTestKey1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 21),
    _TsTtyTestKey1_Type()
)
tsTtyTestKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyTestKey1.setStatus("mandatory")


class _TsTtyTestKey2_Type(Integer32):
    """Custom type tsTtyTestKey2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyTestKey2_Type.__name__ = "Integer32"
_TsTtyTestKey2_Object = MibTableColumn
tsTtyTestKey2 = _TsTtyTestKey2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 22),
    _TsTtyTestKey2_Type()
)
tsTtyTestKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyTestKey2.setStatus("mandatory")


class _TsTtyTestKey3_Type(Integer32):
    """Custom type tsTtyTestKey3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TsTtyTestKey3_Type.__name__ = "Integer32"
_TsTtyTestKey3_Object = MibTableColumn
tsTtyTestKey3 = _TsTtyTestKey3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 23),
    _TsTtyTestKey3_Type()
)
tsTtyTestKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsTtyTestKey3.setStatus("mandatory")


class _TsTtyBufferRate_Type(Integer32):
    """Custom type tsTtyBufferRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsTtyBufferRate_Type.__name__ = "Integer32"
_TsTtyBufferRate_Object = MibTableColumn
tsTtyBufferRate = _TsTtyBufferRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 24),
    _TsTtyBufferRate_Type()
)
tsTtyBufferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyBufferRate.setStatus("mandatory")
_TsTtyRecvBytes_Type = Integer32
_TsTtyRecvBytes_Object = MibTableColumn
tsTtyRecvBytes = _TsTtyRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 25),
    _TsTtyRecvBytes_Type()
)
tsTtyRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyRecvBytes.setStatus("mandatory")
_TsTtySendBytes_Type = Integer32
_TsTtySendBytes_Object = MibTableColumn
tsTtySendBytes = _TsTtySendBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 26),
    _TsTtySendBytes_Type()
)
tsTtySendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtySendBytes.setStatus("mandatory")
_TsTtyLastRecvTime_Type = DisplayString
_TsTtyLastRecvTime_Object = MibTableColumn
tsTtyLastRecvTime = _TsTtyLastRecvTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 27),
    _TsTtyLastRecvTime_Type()
)
tsTtyLastRecvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyLastRecvTime.setStatus("mandatory")
_TsTtyLastSendTime_Type = DisplayString
_TsTtyLastSendTime_Object = MibTableColumn
tsTtyLastSendTime = _TsTtyLastSendTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 28),
    _TsTtyLastSendTime_Type()
)
tsTtyLastSendTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyLastSendTime.setStatus("mandatory")
_TsTtyCurrentVtyID_Type = Integer32
_TsTtyCurrentVtyID_Object = MibTableColumn
tsTtyCurrentVtyID = _TsTtyCurrentVtyID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 29),
    _TsTtyCurrentVtyID_Type()
)
tsTtyCurrentVtyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyCurrentVtyID.setStatus("mandatory")
_TsTtyCurrentVtyRecv_Type = Integer32
_TsTtyCurrentVtyRecv_Object = MibTableColumn
tsTtyCurrentVtyRecv = _TsTtyCurrentVtyRecv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 30),
    _TsTtyCurrentVtyRecv_Type()
)
tsTtyCurrentVtyRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyCurrentVtyRecv.setStatus("mandatory")
_TsTtyCurrentVtySend_Type = Integer32
_TsTtyCurrentVtySend_Object = MibTableColumn
tsTtyCurrentVtySend = _TsTtyCurrentVtySend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 31),
    _TsTtyCurrentVtySend_Type()
)
tsTtyCurrentVtySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyCurrentVtySend.setStatus("mandatory")
_TsTtyCurrentAppID_Type = Integer32
_TsTtyCurrentAppID_Object = MibTableColumn
tsTtyCurrentAppID = _TsTtyCurrentAppID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 32),
    _TsTtyCurrentAppID_Type()
)
tsTtyCurrentAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyCurrentAppID.setStatus("mandatory")
_TsTtyCurrentAppRecv_Type = Integer32
_TsTtyCurrentAppRecv_Object = MibTableColumn
tsTtyCurrentAppRecv = _TsTtyCurrentAppRecv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 33),
    _TsTtyCurrentAppRecv_Type()
)
tsTtyCurrentAppRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyCurrentAppRecv.setStatus("mandatory")
_TsTtyCurrentAppSend_Type = Integer32
_TsTtyCurrentAppSend_Object = MibTableColumn
tsTtyCurrentAppSend = _TsTtyCurrentAppSend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 34),
    _TsTtyCurrentAppSend_Type()
)
tsTtyCurrentAppSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyCurrentAppSend.setStatus("mandatory")


class _TsTtyClearStatistic_Type(Integer32):
    """Custom type tsTtyClearStatistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TsTtyClearStatistic_Type.__name__ = "Integer32"
_TsTtyClearStatistic_Object = MibTableColumn
tsTtyClearStatistic = _TsTtyClearStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 35),
    _TsTtyClearStatistic_Type()
)
tsTtyClearStatistic.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tsTtyClearStatistic.setStatus("mandatory")


class _TsDebugTtyAll_Type(Integer32):
    """Custom type tsDebugTtyAll based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsDebugTtyAll_Type.__name__ = "Integer32"
_TsDebugTtyAll_Object = MibTableColumn
tsDebugTtyAll = _TsDebugTtyAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 36),
    _TsDebugTtyAll_Type()
)
tsDebugTtyAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsDebugTtyAll.setStatus("mandatory")


class _TsDebugTtyBrief_Type(Integer32):
    """Custom type tsDebugTtyBrief based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsDebugTtyBrief_Type.__name__ = "Integer32"
_TsDebugTtyBrief_Object = MibTableColumn
tsDebugTtyBrief = _TsDebugTtyBrief_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 37),
    _TsDebugTtyBrief_Type()
)
tsDebugTtyBrief.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsDebugTtyBrief.setStatus("mandatory")


class _TsDebugTtySock_Type(Integer32):
    """Custom type tsDebugTtySock based on Integer32"""
    defaultValue = 4

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
        *(("all", 1),
          ("none", 4),
          ("recv", 2),
          ("send", 3))
    )


_TsDebugTtySock_Type.__name__ = "Integer32"
_TsDebugTtySock_Object = MibTableColumn
tsDebugTtySock = _TsDebugTtySock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 38),
    _TsDebugTtySock_Type()
)
tsDebugTtySock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsDebugTtySock.setStatus("mandatory")


class _TsDebugTtyTimeStamp_Type(Integer32):
    """Custom type tsDebugTtyTimeStamp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsDebugTtyTimeStamp_Type.__name__ = "Integer32"
_TsDebugTtyTimeStamp_Object = MibTableColumn
tsDebugTtyTimeStamp = _TsDebugTtyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 39),
    _TsDebugTtyTimeStamp_Type()
)
tsDebugTtyTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsDebugTtyTimeStamp.setStatus("mandatory")


class _TsDebugTtyTty_Type(Integer32):
    """Custom type tsDebugTtyTty based on Integer32"""
    defaultValue = 4

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
        *(("all", 1),
          ("none", 4),
          ("recv", 2),
          ("send", 3))
    )


_TsDebugTtyTty_Type.__name__ = "Integer32"
_TsDebugTtyTty_Object = MibTableColumn
tsDebugTtyTty = _TsDebugTtyTty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 3, 1, 40),
    _TsDebugTtyTty_Type()
)
tsDebugTtyTty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsDebugTtyTty.setStatus("mandatory")
_TsTtyManageTable_Object = MibTable
tsTtyManageTable = _TsTtyManageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 4)
)
if mibBuilder.loadTexts:
    tsTtyManageTable.setStatus("mandatory")
_TsTtyManageEntry_Object = MibTableRow
tsTtyManageEntry = _TsTtyManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 4, 1)
)
tsTtyManageEntry.setIndexNames(
    (0, "HUAWEI-TS-MIB", "tsTtyManageUnixIndex"),
)
if mibBuilder.loadTexts:
    tsTtyManageEntry.setStatus("mandatory")


class _TsTtyManageUnixIndex_Type(Integer32):
    """Custom type tsTtyManageUnixIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_TsTtyManageUnixIndex_Type.__name__ = "Integer32"
_TsTtyManageUnixIndex_Object = MibTableColumn
tsTtyManageUnixIndex = _TsTtyManageUnixIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 4, 1, 1),
    _TsTtyManageUnixIndex_Type()
)
tsTtyManageUnixIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyManageUnixIndex.setStatus("mandatory")
_TsTtyManageUnixSockid_Type = Integer32
_TsTtyManageUnixSockid_Object = MibTableColumn
tsTtyManageUnixSockid = _TsTtyManageUnixSockid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 4, 1, 2),
    _TsTtyManageUnixSockid_Type()
)
tsTtyManageUnixSockid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyManageUnixSockid.setStatus("mandatory")
_TsTtyManageLocalIP_Type = IpAddress
_TsTtyManageLocalIP_Object = MibTableColumn
tsTtyManageLocalIP = _TsTtyManageLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 4, 1, 3),
    _TsTtyManageLocalIP_Type()
)
tsTtyManageLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyManageLocalIP.setStatus("mandatory")
_TsTtyManageItemNum_Type = Integer32
_TsTtyManageItemNum_Object = MibTableColumn
tsTtyManageItemNum = _TsTtyManageItemNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 4, 1, 4),
    _TsTtyManageItemNum_Type()
)
tsTtyManageItemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTtyManageItemNum.setStatus("mandatory")


class _TsEnable_Type(Integer32):
    """Custom type tsEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsEnable_Type.__name__ = "Integer32"
_TsEnable_Object = MibScalar
tsEnable = _TsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 5),
    _TsEnable_Type()
)
tsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsEnable.setStatus("mandatory")


class _TsEnableTrap_Type(Integer32):
    """Custom type tsEnableTrap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsEnableTrap_Type.__name__ = "Integer32"
_TsEnableTrap_Object = MibScalar
tsEnableTrap = _TsEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 6),
    _TsEnableTrap_Type()
)
tsEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsEnableTrap.setStatus("mandatory")


class _TsClearTtyAll_Type(Integer32):
    """Custom type tsClearTtyAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TsClearTtyAll_Type.__name__ = "Integer32"
_TsClearTtyAll_Object = MibScalar
tsClearTtyAll = _TsClearTtyAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 7),
    _TsClearTtyAll_Type()
)
tsClearTtyAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tsClearTtyAll.setStatus("mandatory")


class _TsLoginTty_Type(Integer32):
    """Custom type tsLoginTty based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsLoginTty_Type.__name__ = "Integer32"
_TsLoginTty_Object = MibScalar
tsLoginTty = _TsLoginTty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 8),
    _TsLoginTty_Type()
)
tsLoginTty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsLoginTty.setStatus("obsolete")
_TsDebugTtyGroup_ObjectIdentity = ObjectIdentity
tsDebugTtyGroup = _TsDebugTtyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 9)
)


class _TsDebugTtyError_Type(Integer32):
    """Custom type tsDebugTtyError based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsDebugTtyError_Type.__name__ = "Integer32"
_TsDebugTtyError_Object = MibScalar
tsDebugTtyError = _TsDebugTtyError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 9, 1),
    _TsDebugTtyError_Type()
)
tsDebugTtyError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsDebugTtyError.setStatus("mandatory")


class _TsDebugTtyManage_Type(Integer32):
    """Custom type tsDebugTtyManage based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsDebugTtyManage_Type.__name__ = "Integer32"
_TsDebugTtyManage_Object = MibScalar
tsDebugTtyManage = _TsDebugTtyManage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 9, 2),
    _TsDebugTtyManage_Type()
)
tsDebugTtyManage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsDebugTtyManage.setStatus("mandatory")
_TsTrap_ObjectIdentity = ObjectIdentity
tsTrap = _TsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 10)
)

# Managed Objects groups


# Notification objects

tsAppStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 10, 1)
)
tsAppStatusTrap.setObjects(
      *(("HUAWEI-TS-MIB", "tsAppID"),
        ("HUAWEI-TS-MIB", "tsAppTtyServerState"))
)
if mibBuilder.loadTexts:
    tsAppStatusTrap.setStatus(
        "current"
    )

tsTtyStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 10, 2)
)
tsTtyStatusTrap.setObjects(
      *(("HUAWEI-TS-MIB", "tsAsyModeTtyID"),
        ("HUAWEI-TS-MIB", "tsAsyModeTtyVtyID"),
        ("HUAWEI-TS-MIB", "tsAsyModeTtyVtyState"))
)
if mibBuilder.loadTexts:
    tsTtyStatusTrap.setStatus(
        "current"
    )

tsExceptionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 10, 3)
)
if mibBuilder.loadTexts:
    tsExceptionTrap.setStatus(
        "current"
    )

tsClearSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 10, 4)
)
if mibBuilder.loadTexts:
    tsClearSuccessTrap.setStatus(
        "current"
    )

tsDisconnectSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 1, 10, 5)
)
if mibBuilder.loadTexts:
    tsDisconnectSuccessTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-TS-MIB",
    **{"EntryStatus": EntryStatus,
       "terminalServer": terminalServer,
       "tsAppTable": tsAppTable,
       "tsAppEntry": tsAppEntry,
       "tsAppID": tsAppID,
       "tsAppIPAddress": tsAppIPAddress,
       "tsAppPort": tsAppPort,
       "tsAppType": tsAppType,
       "tsAppName": tsAppName,
       "tsAppSourceIP": tsAppSourceIP,
       "tsAppLocalPort": tsAppLocalPort,
       "tsAppTtyServerState": tsAppTtyServerState,
       "tsAppSocketRecvBufSize": tsAppSocketRecvBufSize,
       "tsAppSocketSendBufSize": tsAppSocketSendBufSize,
       "tsAppSockRecvByte": tsAppSockRecvByte,
       "tsAppSockSendByte": tsAppSockSendByte,
       "tsAppLastRecvTime": tsAppLastRecvTime,
       "tsAppLastSendTime": tsAppLastSendTime,
       "tsAppClearStatistic": tsAppClearStatistic,
       "tsAppUnixIndex": tsAppUnixIndex,
       "tsAppStatus": tsAppStatus,
       "tsAsyModeTtyTable": tsAsyModeTtyTable,
       "tsAsyModeTtyEntry": tsAsyModeTtyEntry,
       "tsAsyModeTtyID": tsAsyModeTtyID,
       "tsAsyModeTtyVtyID": tsAsyModeTtyVtyID,
       "tsAsyModeTtyIFIndex": tsAsyModeTtyIFIndex,
       "tsAsyModeTtyAppID": tsAsyModeTtyAppID,
       "tsAsyModeTtyDisconnect": tsAsyModeTtyDisconnect,
       "tsAsyModeTtyVtyState": tsAsyModeTtyVtyState,
       "tsAsyModeTtyFlowCtrlState": tsAsyModeTtyFlowCtrlState,
       "tsAsyModeTtyStatus": tsAsyModeTtyStatus,
       "tsTtyTable": tsTtyTable,
       "tsTtyEntry": tsTtyEntry,
       "tsTtyID": tsTtyID,
       "tsTtyBufferSize": tsTtyBufferSize,
       "tsTtyAutoLink": tsTtyAutoLink,
       "tsTtyCloseLink": tsTtyCloseLink,
       "tsTtyConnPrint": tsTtyConnPrint,
       "tsTtyDelay": tsTtyDelay,
       "tsTtyLogoPrint": tsTtyLogoPrint,
       "tsTtyMenuKey1": tsTtyMenuKey1,
       "tsTtyMenuKey2": tsTtyMenuKey2,
       "tsTtyMenuKey3": tsTtyMenuKey3,
       "tsTtyReadBlock": tsTtyReadBlock,
       "tsTtyRedrawkey1": tsTtyRedrawkey1,
       "tsTtyRedrawkey2": tsTtyRedrawkey2,
       "tsTtyRedrawkey3": tsTtyRedrawkey3,
       "tsTtyResetKey1": tsTtyResetKey1,
       "tsTtyResetKey2": tsTtyResetKey2,
       "tsTtyResetKey3": tsTtyResetKey3,
       "tsTtyTcpNoDelay": tsTtyTcpNoDelay,
       "tsTtyTcpRecvBufferSize": tsTtyTcpRecvBufferSize,
       "tsTtyTcpSendBufferSize": tsTtyTcpSendBufferSize,
       "tsTtyTestKey1": tsTtyTestKey1,
       "tsTtyTestKey2": tsTtyTestKey2,
       "tsTtyTestKey3": tsTtyTestKey3,
       "tsTtyBufferRate": tsTtyBufferRate,
       "tsTtyRecvBytes": tsTtyRecvBytes,
       "tsTtySendBytes": tsTtySendBytes,
       "tsTtyLastRecvTime": tsTtyLastRecvTime,
       "tsTtyLastSendTime": tsTtyLastSendTime,
       "tsTtyCurrentVtyID": tsTtyCurrentVtyID,
       "tsTtyCurrentVtyRecv": tsTtyCurrentVtyRecv,
       "tsTtyCurrentVtySend": tsTtyCurrentVtySend,
       "tsTtyCurrentAppID": tsTtyCurrentAppID,
       "tsTtyCurrentAppRecv": tsTtyCurrentAppRecv,
       "tsTtyCurrentAppSend": tsTtyCurrentAppSend,
       "tsTtyClearStatistic": tsTtyClearStatistic,
       "tsDebugTtyAll": tsDebugTtyAll,
       "tsDebugTtyBrief": tsDebugTtyBrief,
       "tsDebugTtySock": tsDebugTtySock,
       "tsDebugTtyTimeStamp": tsDebugTtyTimeStamp,
       "tsDebugTtyTty": tsDebugTtyTty,
       "tsTtyManageTable": tsTtyManageTable,
       "tsTtyManageEntry": tsTtyManageEntry,
       "tsTtyManageUnixIndex": tsTtyManageUnixIndex,
       "tsTtyManageUnixSockid": tsTtyManageUnixSockid,
       "tsTtyManageLocalIP": tsTtyManageLocalIP,
       "tsTtyManageItemNum": tsTtyManageItemNum,
       "tsEnable": tsEnable,
       "tsEnableTrap": tsEnableTrap,
       "tsClearTtyAll": tsClearTtyAll,
       "tsLoginTty": tsLoginTty,
       "tsDebugTtyGroup": tsDebugTtyGroup,
       "tsDebugTtyError": tsDebugTtyError,
       "tsDebugTtyManage": tsDebugTtyManage,
       "tsTrap": tsTrap,
       "tsAppStatusTrap": tsAppStatusTrap,
       "tsTtyStatusTrap": tsTtyStatusTrap,
       "tsExceptionTrap": tsExceptionTrap,
       "tsClearSuccessTrap": tsClearSuccessTrap,
       "tsDisconnectSuccessTrap": tsDisconnectSuccessTrap}
)

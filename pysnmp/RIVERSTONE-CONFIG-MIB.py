# SNMP MIB module (RIVERSTONE-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:43 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

(RSChangeSessionType,
 RSConfigErrorCode,
 RSFileTransferProtocol,
 RSTransferStatus) = mibBuilder.importSymbols(
    "RIVERSTONE-TC-MIB",
    "RSChangeSessionType",
    "RSConfigErrorCode",
    "RSFileTransferProtocol",
    "RSTransferStatus")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20)
)
rsConfigMIB.setRevisions(
        ("2003-05-06 00:00",
         "2002-11-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsCfgObjects_ObjectIdentity = ObjectIdentity
rsCfgObjects = _RsCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1)
)
_RsCfgNextTransferId_Type = Unsigned32
_RsCfgNextTransferId_Object = MibScalar
rsCfgNextTransferId = _RsCfgNextTransferId_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 1),
    _RsCfgNextTransferId_Type()
)
rsCfgNextTransferId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgNextTransferId.setStatus("current")
_RsCfgTransferTable_Object = MibTable
rsCfgTransferTable = _RsCfgTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2)
)
if mibBuilder.loadTexts:
    rsCfgTransferTable.setStatus("current")
_RsCfgTransferEntry_Object = MibTableRow
rsCfgTransferEntry = _RsCfgTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1)
)
rsCfgTransferEntry.setIndexNames(
    (0, "RIVERSTONE-CONFIG-MIB", "rsCfgTransferId"),
)
if mibBuilder.loadTexts:
    rsCfgTransferEntry.setStatus("current")
_RsCfgTransferId_Type = Unsigned32
_RsCfgTransferId_Object = MibTableColumn
rsCfgTransferId = _RsCfgTransferId_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 1),
    _RsCfgTransferId_Type()
)
rsCfgTransferId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsCfgTransferId.setStatus("current")


class _RsCfgTransferOp_Type(Integer32):
    """Custom type rsCfgTransferOp based on Integer32"""
    defaultValue = 1

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("copyActiveToFlash", 8),
          ("copyActiveToStartup", 6),
          ("copyFlashToActive", 10),
          ("copyFlashToStartup", 11),
          ("copyStartupToActive", 7),
          ("copyStartupToFlash", 9),
          ("noop", 1),
          ("receiveActiveConfigFromHost", 3),
          ("receiveBootlogFromHost", 12),
          ("receiveStartupConfigFromHost", 5),
          ("sendActiveConfigToHost", 2),
          ("sendStartupConfigToHost", 4))
    )


_RsCfgTransferOp_Type.__name__ = "Integer32"
_RsCfgTransferOp_Object = MibTableColumn
rsCfgTransferOp = _RsCfgTransferOp_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 2),
    _RsCfgTransferOp_Type()
)
rsCfgTransferOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsCfgTransferOp.setStatus("current")


class _RsCfgHostAddressType_Type(InetAddressType):
    """Custom type rsCfgHostAddressType based on InetAddressType"""


_RsCfgHostAddressType_Object = MibTableColumn
rsCfgHostAddressType = _RsCfgHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 3),
    _RsCfgHostAddressType_Type()
)
rsCfgHostAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsCfgHostAddressType.setStatus("current")


class _RsCfgHostAddress_Type(InetAddress):
    """Custom type rsCfgHostAddress based on InetAddress"""
    defaultHexValue = ""


_RsCfgHostAddress_Object = MibTableColumn
rsCfgHostAddress = _RsCfgHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 4),
    _RsCfgHostAddress_Type()
)
rsCfgHostAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsCfgHostAddress.setStatus("current")
_RsCfgFileName_Type = DisplayString
_RsCfgFileName_Object = MibTableColumn
rsCfgFileName = _RsCfgFileName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 5),
    _RsCfgFileName_Type()
)
rsCfgFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsCfgFileName.setStatus("current")
_RsCfgFileTransferProtocol_Type = RSFileTransferProtocol
_RsCfgFileTransferProtocol_Object = MibTableColumn
rsCfgFileTransferProtocol = _RsCfgFileTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 6),
    _RsCfgFileTransferProtocol_Type()
)
rsCfgFileTransferProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsCfgFileTransferProtocol.setStatus("current")
_RsCfgActivateTransfer_Type = TruthValue
_RsCfgActivateTransfer_Object = MibTableColumn
rsCfgActivateTransfer = _RsCfgActivateTransfer_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 7),
    _RsCfgActivateTransfer_Type()
)
rsCfgActivateTransfer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsCfgActivateTransfer.setStatus("current")
_RsCfgTransferStatus_Type = RSTransferStatus
_RsCfgTransferStatus_Object = MibTableColumn
rsCfgTransferStatus = _RsCfgTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 8),
    _RsCfgTransferStatus_Type()
)
rsCfgTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgTransferStatus.setStatus("current")
_RsCfgTransferStartTime_Type = TimeTicks
_RsCfgTransferStartTime_Object = MibTableColumn
rsCfgTransferStartTime = _RsCfgTransferStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 9),
    _RsCfgTransferStartTime_Type()
)
rsCfgTransferStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgTransferStartTime.setStatus("current")
_RsCfgTransferEndTime_Type = TimeTicks
_RsCfgTransferEndTime_Object = MibTableColumn
rsCfgTransferEndTime = _RsCfgTransferEndTime_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 10),
    _RsCfgTransferEndTime_Type()
)
rsCfgTransferEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgTransferEndTime.setStatus("current")
_RsCfgTransferError_Type = RSConfigErrorCode
_RsCfgTransferError_Object = MibTableColumn
rsCfgTransferError = _RsCfgTransferError_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 11),
    _RsCfgTransferError_Type()
)
rsCfgTransferError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgTransferError.setStatus("current")
_RsCfgTransferErrorReason_Type = DisplayString
_RsCfgTransferErrorReason_Object = MibTableColumn
rsCfgTransferErrorReason = _RsCfgTransferErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 12),
    _RsCfgTransferErrorReason_Type()
)
rsCfgTransferErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgTransferErrorReason.setStatus("current")
_RsCfgTransferRowStatus_Type = RowStatus
_RsCfgTransferRowStatus_Object = MibTableColumn
rsCfgTransferRowStatus = _RsCfgTransferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 2, 1, 13),
    _RsCfgTransferRowStatus_Type()
)
rsCfgTransferRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsCfgTransferRowStatus.setStatus("current")
_RsCfgMaxEntriesInTransferTable_Type = Unsigned32
_RsCfgMaxEntriesInTransferTable_Object = MibScalar
rsCfgMaxEntriesInTransferTable = _RsCfgMaxEntriesInTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 3),
    _RsCfgMaxEntriesInTransferTable_Type()
)
rsCfgMaxEntriesInTransferTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCfgMaxEntriesInTransferTable.setStatus("current")
_RsCfgMaxSimultaneousTransfers_Type = Unsigned32
_RsCfgMaxSimultaneousTransfers_Object = MibScalar
rsCfgMaxSimultaneousTransfers = _RsCfgMaxSimultaneousTransfers_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 4),
    _RsCfgMaxSimultaneousTransfers_Type()
)
rsCfgMaxSimultaneousTransfers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCfgMaxSimultaneousTransfers.setStatus("current")


class _RsCfgIsStartupActiveAlike_Type(Integer32):
    """Custom type rsCfgIsStartupActiveAlike based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alike", 1),
          ("alikeExceptVolatile", 2),
          ("different", 3))
    )


_RsCfgIsStartupActiveAlike_Type.__name__ = "Integer32"
_RsCfgIsStartupActiveAlike_Object = MibScalar
rsCfgIsStartupActiveAlike = _RsCfgIsStartupActiveAlike_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 5),
    _RsCfgIsStartupActiveAlike_Type()
)
rsCfgIsStartupActiveAlike.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgIsStartupActiveAlike.setStatus("current")
_RsCfgActiveLastChange_Type = DateAndTime
_RsCfgActiveLastChange_Object = MibScalar
rsCfgActiveLastChange = _RsCfgActiveLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 6),
    _RsCfgActiveLastChange_Type()
)
rsCfgActiveLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveLastChange.setStatus("current")
_RsCfgStartupLastChange_Type = DateAndTime
_RsCfgStartupLastChange_Object = MibScalar
rsCfgStartupLastChange = _RsCfgStartupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 1, 7),
    _RsCfgStartupLastChange_Type()
)
rsCfgStartupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgStartupLastChange.setStatus("current")
_RsCfgChangeLogs_ObjectIdentity = ObjectIdentity
rsCfgChangeLogs = _RsCfgChangeLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2)
)
_RsCfgActiveChangeSessionTable_Object = MibTable
rsCfgActiveChangeSessionTable = _RsCfgActiveChangeSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    rsCfgActiveChangeSessionTable.setStatus("current")
_RsCfgActiveChangeSessionEntry_Object = MibTableRow
rsCfgActiveChangeSessionEntry = _RsCfgActiveChangeSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 1, 1)
)
rsCfgActiveChangeSessionEntry.setIndexNames(
    (0, "RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionId"),
)
if mibBuilder.loadTexts:
    rsCfgActiveChangeSessionEntry.setStatus("current")
_RsCfgActiveChangeSessionId_Type = Unsigned32
_RsCfgActiveChangeSessionId_Object = MibTableColumn
rsCfgActiveChangeSessionId = _RsCfgActiveChangeSessionId_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 1, 1, 1),
    _RsCfgActiveChangeSessionId_Type()
)
rsCfgActiveChangeSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsCfgActiveChangeSessionId.setStatus("current")
_RsCfgActiveChangeSessionType_Type = RSChangeSessionType
_RsCfgActiveChangeSessionType_Object = MibTableColumn
rsCfgActiveChangeSessionType = _RsCfgActiveChangeSessionType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 1, 1, 2),
    _RsCfgActiveChangeSessionType_Type()
)
rsCfgActiveChangeSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveChangeSessionType.setStatus("current")
_RsCfgActiveChangeSessionUser_Type = DisplayString
_RsCfgActiveChangeSessionUser_Object = MibTableColumn
rsCfgActiveChangeSessionUser = _RsCfgActiveChangeSessionUser_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 1, 1, 3),
    _RsCfgActiveChangeSessionUser_Type()
)
rsCfgActiveChangeSessionUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveChangeSessionUser.setStatus("current")
_RsCfgActiveChangeSessionHostType_Type = InetAddressType
_RsCfgActiveChangeSessionHostType_Object = MibTableColumn
rsCfgActiveChangeSessionHostType = _RsCfgActiveChangeSessionHostType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 1, 1, 4),
    _RsCfgActiveChangeSessionHostType_Type()
)
rsCfgActiveChangeSessionHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveChangeSessionHostType.setStatus("current")
_RsCfgActiveChangeSessionHostAddress_Type = InetAddress
_RsCfgActiveChangeSessionHostAddress_Object = MibTableColumn
rsCfgActiveChangeSessionHostAddress = _RsCfgActiveChangeSessionHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 1, 1, 5),
    _RsCfgActiveChangeSessionHostAddress_Type()
)
rsCfgActiveChangeSessionHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveChangeSessionHostAddress.setStatus("current")
_RsCfgActiveChangeSessionTime_Type = DateAndTime
_RsCfgActiveChangeSessionTime_Object = MibTableColumn
rsCfgActiveChangeSessionTime = _RsCfgActiveChangeSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 1, 1, 6),
    _RsCfgActiveChangeSessionTime_Type()
)
rsCfgActiveChangeSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveChangeSessionTime.setStatus("current")
_RsCfgActiveChangeAddedLines_Type = Unsigned32
_RsCfgActiveChangeAddedLines_Object = MibTableColumn
rsCfgActiveChangeAddedLines = _RsCfgActiveChangeAddedLines_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 1, 1, 7),
    _RsCfgActiveChangeAddedLines_Type()
)
rsCfgActiveChangeAddedLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveChangeAddedLines.setStatus("current")
_RsCfgActiveChangeDeletedLines_Type = Unsigned32
_RsCfgActiveChangeDeletedLines_Object = MibTableColumn
rsCfgActiveChangeDeletedLines = _RsCfgActiveChangeDeletedLines_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 1, 1, 8),
    _RsCfgActiveChangeDeletedLines_Type()
)
rsCfgActiveChangeDeletedLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveChangeDeletedLines.setStatus("current")
_RsCfgActiveChangePresentInChangeTable_Type = TruthValue
_RsCfgActiveChangePresentInChangeTable_Object = MibTableColumn
rsCfgActiveChangePresentInChangeTable = _RsCfgActiveChangePresentInChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 1, 1, 9),
    _RsCfgActiveChangePresentInChangeTable_Type()
)
rsCfgActiveChangePresentInChangeTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveChangePresentInChangeTable.setStatus("current")
_RsCfgActiveChangeTable_Object = MibTable
rsCfgActiveChangeTable = _RsCfgActiveChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 2)
)
if mibBuilder.loadTexts:
    rsCfgActiveChangeTable.setStatus("current")
_RsCfgActiveChangeEntry_Object = MibTableRow
rsCfgActiveChangeEntry = _RsCfgActiveChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 2, 1)
)
rsCfgActiveChangeEntry.setIndexNames(
    (0, "RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionId"),
    (0, "RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeId"),
)
if mibBuilder.loadTexts:
    rsCfgActiveChangeEntry.setStatus("current")
_RsCfgActiveChangeId_Type = Unsigned32
_RsCfgActiveChangeId_Object = MibTableColumn
rsCfgActiveChangeId = _RsCfgActiveChangeId_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 2, 1, 1),
    _RsCfgActiveChangeId_Type()
)
rsCfgActiveChangeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsCfgActiveChangeId.setStatus("current")


class _RsCfgActiveChangeAction_Type(Integer32):
    """Custom type rsCfgActiveChangeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_RsCfgActiveChangeAction_Type.__name__ = "Integer32"
_RsCfgActiveChangeAction_Object = MibTableColumn
rsCfgActiveChangeAction = _RsCfgActiveChangeAction_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 2, 1, 2),
    _RsCfgActiveChangeAction_Type()
)
rsCfgActiveChangeAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveChangeAction.setStatus("current")
_RsCfgActiveChangeLine_Type = DisplayString
_RsCfgActiveChangeLine_Object = MibTableColumn
rsCfgActiveChangeLine = _RsCfgActiveChangeLine_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 2, 1, 3),
    _RsCfgActiveChangeLine_Type()
)
rsCfgActiveChangeLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveChangeLine.setStatus("current")
_RsCfgEnableChangeLog_Type = TruthValue
_RsCfgEnableChangeLog_Object = MibScalar
rsCfgEnableChangeLog = _RsCfgEnableChangeLog_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 3),
    _RsCfgEnableChangeLog_Type()
)
rsCfgEnableChangeLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCfgEnableChangeLog.setStatus("current")
_RsCfgResetChangeLog_Type = TruthValue
_RsCfgResetChangeLog_Object = MibScalar
rsCfgResetChangeLog = _RsCfgResetChangeLog_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 4),
    _RsCfgResetChangeLog_Type()
)
rsCfgResetChangeLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCfgResetChangeLog.setStatus("current")
_RsCfgMaxActiveChangeLines_Type = Unsigned32
_RsCfgMaxActiveChangeLines_Object = MibScalar
rsCfgMaxActiveChangeLines = _RsCfgMaxActiveChangeLines_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 5),
    _RsCfgMaxActiveChangeLines_Type()
)
rsCfgMaxActiveChangeLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCfgMaxActiveChangeLines.setStatus("current")
_RsCfgMaxActiveChangeLinesPerSession_Type = Unsigned32
_RsCfgMaxActiveChangeLinesPerSession_Object = MibScalar
rsCfgMaxActiveChangeLinesPerSession = _RsCfgMaxActiveChangeLinesPerSession_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 6),
    _RsCfgMaxActiveChangeLinesPerSession_Type()
)
rsCfgMaxActiveChangeLinesPerSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCfgMaxActiveChangeLinesPerSession.setStatus("current")
_RsCfgMaxActiveChangeSessions_Type = Unsigned32
_RsCfgMaxActiveChangeSessions_Object = MibScalar
rsCfgMaxActiveChangeSessions = _RsCfgMaxActiveChangeSessions_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 7),
    _RsCfgMaxActiveChangeSessions_Type()
)
rsCfgMaxActiveChangeSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCfgMaxActiveChangeSessions.setStatus("current")
_RsCfgNumberOfActiveChanges_Type = Unsigned32
_RsCfgNumberOfActiveChanges_Object = MibScalar
rsCfgNumberOfActiveChanges = _RsCfgNumberOfActiveChanges_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 8),
    _RsCfgNumberOfActiveChanges_Type()
)
rsCfgNumberOfActiveChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgNumberOfActiveChanges.setStatus("current")
_RsCfgNumberOfStartupChanges_Type = Unsigned32
_RsCfgNumberOfStartupChanges_Object = MibScalar
rsCfgNumberOfStartupChanges = _RsCfgNumberOfStartupChanges_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 2, 9),
    _RsCfgNumberOfStartupChanges_Type()
)
rsCfgNumberOfStartupChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgNumberOfStartupChanges.setStatus("current")
_RsCfgNotification_ObjectIdentity = ObjectIdentity
rsCfgNotification = _RsCfgNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 3)
)
_RsCfgNotificationControl_ObjectIdentity = ObjectIdentity
rsCfgNotificationControl = _RsCfgNotificationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 3, 1)
)
_RsCfgEnableNotifications_Type = TruthValue
_RsCfgEnableNotifications_Object = MibScalar
rsCfgEnableNotifications = _RsCfgEnableNotifications_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 3, 1, 1),
    _RsCfgEnableNotifications_Type()
)
rsCfgEnableNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsCfgEnableNotifications.setStatus("current")
_RsCfgNotifications_ObjectIdentity = ObjectIdentity
rsCfgNotifications = _RsCfgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 3, 2)
)
_RsCfgNotifyPrefix_ObjectIdentity = ObjectIdentity
rsCfgNotifyPrefix = _RsCfgNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 3, 2, 0)
)
_RsCfgBootDetails_ObjectIdentity = ObjectIdentity
rsCfgBootDetails = _RsCfgBootDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 4)
)
_RsCfgActiveImageVersion_Type = DisplayString
_RsCfgActiveImageVersion_Object = MibScalar
rsCfgActiveImageVersion = _RsCfgActiveImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 4, 1),
    _RsCfgActiveImageVersion_Type()
)
rsCfgActiveImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveImageVersion.setStatus("current")
_RsCfgActiveImageBootLocation_Type = DisplayString
_RsCfgActiveImageBootLocation_Object = MibScalar
rsCfgActiveImageBootLocation = _RsCfgActiveImageBootLocation_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 4, 2),
    _RsCfgActiveImageBootLocation_Type()
)
rsCfgActiveImageBootLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCfgActiveImageBootLocation.setStatus("current")
_RsConfigConformance_ObjectIdentity = ObjectIdentity
rsConfigConformance = _RsConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 5)
)
_RsConfigCompliances_ObjectIdentity = ObjectIdentity
rsConfigCompliances = _RsConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 5, 1)
)
_RsConfigGroups_ObjectIdentity = ObjectIdentity
rsConfigGroups = _RsConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 5, 2)
)

# Managed Objects groups

rsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 5, 2, 1)
)
rsConfigGroup.setObjects(
      *(("RIVERSTONE-CONFIG-MIB", "rsCfgNextTransferId"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgTransferOp"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgHostAddressType"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgHostAddress"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgFileName"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgFileTransferProtocol"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActivateTransfer"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgTransferStatus"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgTransferStartTime"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgTransferEndTime"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgTransferError"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgTransferErrorReason"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgTransferRowStatus"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgMaxEntriesInTransferTable"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgMaxSimultaneousTransfers"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgIsStartupActiveAlike"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveLastChange"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgStartupLastChange"))
)
if mibBuilder.loadTexts:
    rsConfigGroup.setStatus("current")

rsChangeLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 5, 2, 2)
)
rsChangeLogGroup.setObjects(
      *(("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionType"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionUser"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionHostType"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionHostAddress"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionTime"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeAddedLines"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeDeletedLines"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangePresentInChangeTable"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeAction"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeLine"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgEnableChangeLog"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgResetChangeLog"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgMaxActiveChangeLines"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgMaxActiveChangeLinesPerSession"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgMaxActiveChangeSessions"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgNumberOfActiveChanges"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgNumberOfStartupChanges"))
)
if mibBuilder.loadTexts:
    rsChangeLogGroup.setStatus("current")

rsConfigNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 5, 2, 4)
)
rsConfigNotificationControlGroup.setObjects(
    ("RIVERSTONE-CONFIG-MIB", "rsCfgEnableNotifications")
)
if mibBuilder.loadTexts:
    rsConfigNotificationControlGroup.setStatus("current")

rsBootInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 5, 2, 5)
)
rsBootInfoGroup.setObjects(
      *(("RIVERSTONE-CONFIG-MIB", "rsCfgActiveImageVersion"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveImageBootLocation"))
)
if mibBuilder.loadTexts:
    rsBootInfoGroup.setStatus("current")


# Notification objects

rsCfgActiveConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 3, 2, 0, 1)
)
rsCfgActiveConfigChange.setObjects(
      *(("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionType"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionUser"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionHostType"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionHostAddress"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgActiveChangeSessionTime"))
)
if mibBuilder.loadTexts:
    rsCfgActiveConfigChange.setStatus(
        "current"
    )

rsCfgStartupConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 3, 2, 0, 2)
)
rsCfgStartupConfigChange.setObjects(
    ("RIVERSTONE-CONFIG-MIB", "rsCfgStartupLastChange")
)
if mibBuilder.loadTexts:
    rsCfgStartupConfigChange.setStatus(
        "current"
    )


# Notifications groups

rsConfigNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 5, 2, 3)
)
rsConfigNotificationGroup.setObjects(
      *(("RIVERSTONE-CONFIG-MIB", "rsCfgActiveConfigChange"),
        ("RIVERSTONE-CONFIG-MIB", "rsCfgStartupConfigChange"))
)
if mibBuilder.loadTexts:
    rsConfigNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rsConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 20, 5, 1, 1)
)
if mibBuilder.loadTexts:
    rsConfigCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-CONFIG-MIB",
    **{"rsConfigMIB": rsConfigMIB,
       "rsCfgObjects": rsCfgObjects,
       "rsCfgNextTransferId": rsCfgNextTransferId,
       "rsCfgTransferTable": rsCfgTransferTable,
       "rsCfgTransferEntry": rsCfgTransferEntry,
       "rsCfgTransferId": rsCfgTransferId,
       "rsCfgTransferOp": rsCfgTransferOp,
       "rsCfgHostAddressType": rsCfgHostAddressType,
       "rsCfgHostAddress": rsCfgHostAddress,
       "rsCfgFileName": rsCfgFileName,
       "rsCfgFileTransferProtocol": rsCfgFileTransferProtocol,
       "rsCfgActivateTransfer": rsCfgActivateTransfer,
       "rsCfgTransferStatus": rsCfgTransferStatus,
       "rsCfgTransferStartTime": rsCfgTransferStartTime,
       "rsCfgTransferEndTime": rsCfgTransferEndTime,
       "rsCfgTransferError": rsCfgTransferError,
       "rsCfgTransferErrorReason": rsCfgTransferErrorReason,
       "rsCfgTransferRowStatus": rsCfgTransferRowStatus,
       "rsCfgMaxEntriesInTransferTable": rsCfgMaxEntriesInTransferTable,
       "rsCfgMaxSimultaneousTransfers": rsCfgMaxSimultaneousTransfers,
       "rsCfgIsStartupActiveAlike": rsCfgIsStartupActiveAlike,
       "rsCfgActiveLastChange": rsCfgActiveLastChange,
       "rsCfgStartupLastChange": rsCfgStartupLastChange,
       "rsCfgChangeLogs": rsCfgChangeLogs,
       "rsCfgActiveChangeSessionTable": rsCfgActiveChangeSessionTable,
       "rsCfgActiveChangeSessionEntry": rsCfgActiveChangeSessionEntry,
       "rsCfgActiveChangeSessionId": rsCfgActiveChangeSessionId,
       "rsCfgActiveChangeSessionType": rsCfgActiveChangeSessionType,
       "rsCfgActiveChangeSessionUser": rsCfgActiveChangeSessionUser,
       "rsCfgActiveChangeSessionHostType": rsCfgActiveChangeSessionHostType,
       "rsCfgActiveChangeSessionHostAddress": rsCfgActiveChangeSessionHostAddress,
       "rsCfgActiveChangeSessionTime": rsCfgActiveChangeSessionTime,
       "rsCfgActiveChangeAddedLines": rsCfgActiveChangeAddedLines,
       "rsCfgActiveChangeDeletedLines": rsCfgActiveChangeDeletedLines,
       "rsCfgActiveChangePresentInChangeTable": rsCfgActiveChangePresentInChangeTable,
       "rsCfgActiveChangeTable": rsCfgActiveChangeTable,
       "rsCfgActiveChangeEntry": rsCfgActiveChangeEntry,
       "rsCfgActiveChangeId": rsCfgActiveChangeId,
       "rsCfgActiveChangeAction": rsCfgActiveChangeAction,
       "rsCfgActiveChangeLine": rsCfgActiveChangeLine,
       "rsCfgEnableChangeLog": rsCfgEnableChangeLog,
       "rsCfgResetChangeLog": rsCfgResetChangeLog,
       "rsCfgMaxActiveChangeLines": rsCfgMaxActiveChangeLines,
       "rsCfgMaxActiveChangeLinesPerSession": rsCfgMaxActiveChangeLinesPerSession,
       "rsCfgMaxActiveChangeSessions": rsCfgMaxActiveChangeSessions,
       "rsCfgNumberOfActiveChanges": rsCfgNumberOfActiveChanges,
       "rsCfgNumberOfStartupChanges": rsCfgNumberOfStartupChanges,
       "rsCfgNotification": rsCfgNotification,
       "rsCfgNotificationControl": rsCfgNotificationControl,
       "rsCfgEnableNotifications": rsCfgEnableNotifications,
       "rsCfgNotifications": rsCfgNotifications,
       "rsCfgNotifyPrefix": rsCfgNotifyPrefix,
       "rsCfgActiveConfigChange": rsCfgActiveConfigChange,
       "rsCfgStartupConfigChange": rsCfgStartupConfigChange,
       "rsCfgBootDetails": rsCfgBootDetails,
       "rsCfgActiveImageVersion": rsCfgActiveImageVersion,
       "rsCfgActiveImageBootLocation": rsCfgActiveImageBootLocation,
       "rsConfigConformance": rsConfigConformance,
       "rsConfigCompliances": rsConfigCompliances,
       "rsConfigCompliance": rsConfigCompliance,
       "rsConfigGroups": rsConfigGroups,
       "rsConfigGroup": rsConfigGroup,
       "rsChangeLogGroup": rsChangeLogGroup,
       "rsConfigNotificationGroup": rsConfigNotificationGroup,
       "rsConfigNotificationControlGroup": rsConfigNotificationControlGroup,
       "rsBootInfoGroup": rsBootInfoGroup}
)

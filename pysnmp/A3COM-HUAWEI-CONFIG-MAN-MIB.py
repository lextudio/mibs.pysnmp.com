# SNMP MIB module (A3COM-HUAWEI-CONFIG-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-CONFIG-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:25 2024
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

(huaweiUtility,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "huaweiUtility")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10)
)
h3cConfig.setRevisions(
        ("2011-11-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigOperationType(Integer32, TextualConvention):
    status = "current"
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
        *(("net2Running", 4),
          ("net2Startup", 5),
          ("running2Net", 3),
          ("running2Startup", 1),
          ("startup2Net", 6),
          ("startup2Running", 2))
    )



class ConfigOperationStateType(Integer32, TextualConvention):
    status = "current"
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("opAuthFail", 17),
          ("opCopyToSlaveFailure", 22),
          ("opDeviceBusy", 8),
          ("opDeviceError", 10),
          ("opDeviceFull", 12),
          ("opDeviceNotProgrammable", 11),
          ("opDeviceOpenError", 9),
          ("opFileChecksumError", 15),
          ("opFileOpenError", 13),
          ("opFileTransferError", 14),
          ("opInProgress", 1),
          ("opInvalidConfigFile", 20),
          ("opInvalidDestName", 6),
          ("opInvalidOperation", 3),
          ("opInvalidProtocol", 4),
          ("opInvalidServerAddress", 7),
          ("opInvalidSourceName", 5),
          ("opNoMemory", 16),
          ("opSlaveFull", 21),
          ("opSuccess", 2),
          ("opTimeOut", 18),
          ("opUnknownFailure", 19))
    )



# MIB Managed Objects in the order of their OIDs

_H3cConfigManObjects_ObjectIdentity = ObjectIdentity
h3cConfigManObjects = _H3cConfigManObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1)
)
_H3cCfgLog_ObjectIdentity = ObjectIdentity
h3cCfgLog = _H3cCfgLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1)
)
_H3cCfgRunModifiedLast_Type = TimeTicks
_H3cCfgRunModifiedLast_Object = MibScalar
h3cCfgRunModifiedLast = _H3cCfgRunModifiedLast_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 1),
    _H3cCfgRunModifiedLast_Type()
)
h3cCfgRunModifiedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgRunModifiedLast.setStatus("current")
_H3cCfgRunSavedLast_Type = TimeTicks
_H3cCfgRunSavedLast_Object = MibScalar
h3cCfgRunSavedLast = _H3cCfgRunSavedLast_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 2),
    _H3cCfgRunSavedLast_Type()
)
h3cCfgRunSavedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgRunSavedLast.setStatus("current")
_H3cCfgStartModifiedLast_Type = TimeTicks
_H3cCfgStartModifiedLast_Object = MibScalar
h3cCfgStartModifiedLast = _H3cCfgStartModifiedLast_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 3),
    _H3cCfgStartModifiedLast_Type()
)
h3cCfgStartModifiedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgStartModifiedLast.setStatus("current")


class _H3cCfgLogLimitedEntries_Type(Integer32):
    """Custom type h3cCfgLogLimitedEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cCfgLogLimitedEntries_Type.__name__ = "Integer32"
_H3cCfgLogLimitedEntries_Object = MibScalar
h3cCfgLogLimitedEntries = _H3cCfgLogLimitedEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 4),
    _H3cCfgLogLimitedEntries_Type()
)
h3cCfgLogLimitedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogLimitedEntries.setStatus("current")
_H3cCfgLogDeletedEntries_Type = Counter32
_H3cCfgLogDeletedEntries_Object = MibScalar
h3cCfgLogDeletedEntries = _H3cCfgLogDeletedEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 5),
    _H3cCfgLogDeletedEntries_Type()
)
h3cCfgLogDeletedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogDeletedEntries.setStatus("current")


class _H3cCfgLogWantBackup_Type(TruthValue):
    """Custom type h3cCfgLogWantBackup based on TruthValue"""


_H3cCfgLogWantBackup_Object = MibScalar
h3cCfgLogWantBackup = _H3cCfgLogWantBackup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 6),
    _H3cCfgLogWantBackup_Type()
)
h3cCfgLogWantBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCfgLogWantBackup.setStatus("current")
_H3cCfgLogTable_Object = MibTable
h3cCfgLogTable = _H3cCfgLogTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7)
)
if mibBuilder.loadTexts:
    h3cCfgLogTable.setStatus("current")
_H3cCfgLogEntry_Object = MibTableRow
h3cCfgLogEntry = _H3cCfgLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1)
)
h3cCfgLogEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogIndex"),
)
if mibBuilder.loadTexts:
    h3cCfgLogEntry.setStatus("current")


class _H3cCfgLogIndex_Type(Integer32):
    """Custom type h3cCfgLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cCfgLogIndex_Type.__name__ = "Integer32"
_H3cCfgLogIndex_Object = MibTableColumn
h3cCfgLogIndex = _H3cCfgLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 1),
    _H3cCfgLogIndex_Type()
)
h3cCfgLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCfgLogIndex.setStatus("current")
_H3cCfgLogTime_Type = TimeTicks
_H3cCfgLogTime_Object = MibTableColumn
h3cCfgLogTime = _H3cCfgLogTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 2),
    _H3cCfgLogTime_Type()
)
h3cCfgLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogTime.setStatus("current")


class _H3cCfgLogSrcCmd_Type(Integer32):
    """Custom type h3cCfgLogSrcCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cmdLine", 1),
          ("other", 3),
          ("snmp", 2))
    )


_H3cCfgLogSrcCmd_Type.__name__ = "Integer32"
_H3cCfgLogSrcCmd_Object = MibTableColumn
h3cCfgLogSrcCmd = _H3cCfgLogSrcCmd_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 3),
    _H3cCfgLogSrcCmd_Type()
)
h3cCfgLogSrcCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogSrcCmd.setStatus("current")


class _H3cCfgLogSrcData_Type(Integer32):
    """Custom type h3cCfgLogSrcData based on Integer32"""
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
        *(("commandSource", 3),
          ("erase", 1),
          ("hotPlugging", 7),
          ("local", 5),
          ("netFtp", 6),
          ("runningData", 2),
          ("startupData", 4))
    )


_H3cCfgLogSrcData_Type.__name__ = "Integer32"
_H3cCfgLogSrcData_Object = MibTableColumn
h3cCfgLogSrcData = _H3cCfgLogSrcData_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 4),
    _H3cCfgLogSrcData_Type()
)
h3cCfgLogSrcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogSrcData.setStatus("current")


class _H3cCfgLogDesData_Type(Integer32):
    """Custom type h3cCfgLogDesData based on Integer32"""
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
        *(("commandSource", 3),
          ("hotPlugging", 7),
          ("local", 5),
          ("netFtp", 6),
          ("runningData", 2),
          ("startupData", 4),
          ("unknown", 1))
    )


_H3cCfgLogDesData_Type.__name__ = "Integer32"
_H3cCfgLogDesData_Object = MibTableColumn
h3cCfgLogDesData = _H3cCfgLogDesData_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 5),
    _H3cCfgLogDesData_Type()
)
h3cCfgLogDesData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogDesData.setStatus("current")


class _H3cCfgLogTerminalType_Type(Integer32):
    """Custom type h3cCfgLogTerminalType based on Integer32"""
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
        *(("auxiliary", 6),
          ("console", 3),
          ("notApplicable", 1),
          ("terminal", 4),
          ("unknown", 2),
          ("virtual", 5))
    )


_H3cCfgLogTerminalType_Type.__name__ = "Integer32"
_H3cCfgLogTerminalType_Object = MibTableColumn
h3cCfgLogTerminalType = _H3cCfgLogTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 6),
    _H3cCfgLogTerminalType_Type()
)
h3cCfgLogTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogTerminalType.setStatus("current")


class _H3cCfgLogTerminalUser_Type(DisplayString):
    """Custom type h3cCfgLogTerminalUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cCfgLogTerminalUser_Type.__name__ = "DisplayString"
_H3cCfgLogTerminalUser_Object = MibTableColumn
h3cCfgLogTerminalUser = _H3cCfgLogTerminalUser_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 7),
    _H3cCfgLogTerminalUser_Type()
)
h3cCfgLogTerminalUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogTerminalUser.setStatus("current")
_H3cCfgLogTerminalNum_Type = Integer32
_H3cCfgLogTerminalNum_Object = MibTableColumn
h3cCfgLogTerminalNum = _H3cCfgLogTerminalNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 8),
    _H3cCfgLogTerminalNum_Type()
)
h3cCfgLogTerminalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogTerminalNum.setStatus("current")


class _H3cCfgLogTerminalLocation_Type(DisplayString):
    """Custom type h3cCfgLogTerminalLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cCfgLogTerminalLocation_Type.__name__ = "DisplayString"
_H3cCfgLogTerminalLocation_Object = MibTableColumn
h3cCfgLogTerminalLocation = _H3cCfgLogTerminalLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 9),
    _H3cCfgLogTerminalLocation_Type()
)
h3cCfgLogTerminalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogTerminalLocation.setStatus("current")
_H3cCfgLogCmdSrcAddress_Type = IpAddress
_H3cCfgLogCmdSrcAddress_Object = MibTableColumn
h3cCfgLogCmdSrcAddress = _H3cCfgLogCmdSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 10),
    _H3cCfgLogCmdSrcAddress_Type()
)
h3cCfgLogCmdSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogCmdSrcAddress.setStatus("deprecated")


class _H3cCfgLogVirHost_Type(DisplayString):
    """Custom type h3cCfgLogVirHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cCfgLogVirHost_Type.__name__ = "DisplayString"
_H3cCfgLogVirHost_Object = MibTableColumn
h3cCfgLogVirHost = _H3cCfgLogVirHost_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 11),
    _H3cCfgLogVirHost_Type()
)
h3cCfgLogVirHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogVirHost.setStatus("current")


class _H3cCfgLogUserName_Type(DisplayString):
    """Custom type h3cCfgLogUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cCfgLogUserName_Type.__name__ = "DisplayString"
_H3cCfgLogUserName_Object = MibTableColumn
h3cCfgLogUserName = _H3cCfgLogUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 12),
    _H3cCfgLogUserName_Type()
)
h3cCfgLogUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogUserName.setStatus("current")
_H3cCfgLogServerAddress_Type = IpAddress
_H3cCfgLogServerAddress_Object = MibTableColumn
h3cCfgLogServerAddress = _H3cCfgLogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 13),
    _H3cCfgLogServerAddress_Type()
)
h3cCfgLogServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogServerAddress.setStatus("deprecated")


class _H3cCfgLogFile_Type(DisplayString):
    """Custom type h3cCfgLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cCfgLogFile_Type.__name__ = "DisplayString"
_H3cCfgLogFile_Object = MibTableColumn
h3cCfgLogFile = _H3cCfgLogFile_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 14),
    _H3cCfgLogFile_Type()
)
h3cCfgLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogFile.setStatus("current")
_H3cCfgLogCmdSrcAddrType_Type = InetAddressType
_H3cCfgLogCmdSrcAddrType_Object = MibTableColumn
h3cCfgLogCmdSrcAddrType = _H3cCfgLogCmdSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 15),
    _H3cCfgLogCmdSrcAddrType_Type()
)
h3cCfgLogCmdSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogCmdSrcAddrType.setStatus("current")
_H3cCfgLogCmdSrcAddrRev_Type = InetAddress
_H3cCfgLogCmdSrcAddrRev_Object = MibTableColumn
h3cCfgLogCmdSrcAddrRev = _H3cCfgLogCmdSrcAddrRev_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 16),
    _H3cCfgLogCmdSrcAddrRev_Type()
)
h3cCfgLogCmdSrcAddrRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogCmdSrcAddrRev.setStatus("current")
_H3cCfgLogCmdSrcAddrVPNName_Type = DisplayString
_H3cCfgLogCmdSrcAddrVPNName_Object = MibTableColumn
h3cCfgLogCmdSrcAddrVPNName = _H3cCfgLogCmdSrcAddrVPNName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 17),
    _H3cCfgLogCmdSrcAddrVPNName_Type()
)
h3cCfgLogCmdSrcAddrVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogCmdSrcAddrVPNName.setStatus("current")
_H3cCfgLogServerAddrType_Type = InetAddressType
_H3cCfgLogServerAddrType_Object = MibTableColumn
h3cCfgLogServerAddrType = _H3cCfgLogServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 18),
    _H3cCfgLogServerAddrType_Type()
)
h3cCfgLogServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogServerAddrType.setStatus("current")
_H3cCfgLogServerAddrRev_Type = InetAddress
_H3cCfgLogServerAddrRev_Object = MibTableColumn
h3cCfgLogServerAddrRev = _H3cCfgLogServerAddrRev_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 19),
    _H3cCfgLogServerAddrRev_Type()
)
h3cCfgLogServerAddrRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogServerAddrRev.setStatus("current")
_H3cCfgLogServerAddrVPNName_Type = DisplayString
_H3cCfgLogServerAddrVPNName_Object = MibTableColumn
h3cCfgLogServerAddrVPNName = _H3cCfgLogServerAddrVPNName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 7, 1, 20),
    _H3cCfgLogServerAddrVPNName_Type()
)
h3cCfgLogServerAddrVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgLogServerAddrVPNName.setStatus("current")
_H3cCfgFirstTrapTime_Type = TimeTicks
_H3cCfgFirstTrapTime_Object = MibScalar
h3cCfgFirstTrapTime = _H3cCfgFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 1, 8),
    _H3cCfgFirstTrapTime_Type()
)
h3cCfgFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cCfgFirstTrapTime.setStatus("current")
_H3cCfgOperate_ObjectIdentity = ObjectIdentity
h3cCfgOperate = _H3cCfgOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2)
)


class _H3cCfgOperateGlobalEntryLimit_Type(Integer32):
    """Custom type h3cCfgOperateGlobalEntryLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_H3cCfgOperateGlobalEntryLimit_Type.__name__ = "Integer32"
_H3cCfgOperateGlobalEntryLimit_Object = MibScalar
h3cCfgOperateGlobalEntryLimit = _H3cCfgOperateGlobalEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 1),
    _H3cCfgOperateGlobalEntryLimit_Type()
)
h3cCfgOperateGlobalEntryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgOperateGlobalEntryLimit.setStatus("current")


class _H3cCfgOperateEntryAgeOutTime_Type(Integer32):
    """Custom type h3cCfgOperateEntryAgeOutTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_H3cCfgOperateEntryAgeOutTime_Type.__name__ = "Integer32"
_H3cCfgOperateEntryAgeOutTime_Object = MibScalar
h3cCfgOperateEntryAgeOutTime = _H3cCfgOperateEntryAgeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 2),
    _H3cCfgOperateEntryAgeOutTime_Type()
)
h3cCfgOperateEntryAgeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCfgOperateEntryAgeOutTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cCfgOperateEntryAgeOutTime.setUnits("minute")


class _H3cCfgOperateResultGlobalEntryLimit_Type(Integer32):
    """Custom type h3cCfgOperateResultGlobalEntryLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_H3cCfgOperateResultGlobalEntryLimit_Type.__name__ = "Integer32"
_H3cCfgOperateResultGlobalEntryLimit_Object = MibScalar
h3cCfgOperateResultGlobalEntryLimit = _H3cCfgOperateResultGlobalEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 3),
    _H3cCfgOperateResultGlobalEntryLimit_Type()
)
h3cCfgOperateResultGlobalEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCfgOperateResultGlobalEntryLimit.setStatus("current")
_H3cCfgOperateTable_Object = MibTable
h3cCfgOperateTable = _H3cCfgOperateTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4)
)
if mibBuilder.loadTexts:
    h3cCfgOperateTable.setStatus("current")
_H3cCfgOperateEntry_Object = MibTableRow
h3cCfgOperateEntry = _H3cCfgOperateEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1)
)
h3cCfgOperateEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateIndex"),
)
if mibBuilder.loadTexts:
    h3cCfgOperateEntry.setStatus("current")


class _H3cCfgOperateIndex_Type(Integer32):
    """Custom type h3cCfgOperateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cCfgOperateIndex_Type.__name__ = "Integer32"
_H3cCfgOperateIndex_Object = MibTableColumn
h3cCfgOperateIndex = _H3cCfgOperateIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 1),
    _H3cCfgOperateIndex_Type()
)
h3cCfgOperateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCfgOperateIndex.setStatus("current")
_H3cCfgOperateType_Type = ConfigOperationType
_H3cCfgOperateType_Object = MibTableColumn
h3cCfgOperateType = _H3cCfgOperateType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 2),
    _H3cCfgOperateType_Type()
)
h3cCfgOperateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateType.setStatus("current")


class _H3cCfgOperateProtocol_Type(Integer32):
    """Custom type h3cCfgOperateProtocol based on Integer32"""
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
        *(("clusterftp", 3),
          ("clustertftp", 4),
          ("ftp", 1),
          ("tftp", 2))
    )


_H3cCfgOperateProtocol_Type.__name__ = "Integer32"
_H3cCfgOperateProtocol_Object = MibTableColumn
h3cCfgOperateProtocol = _H3cCfgOperateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 3),
    _H3cCfgOperateProtocol_Type()
)
h3cCfgOperateProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateProtocol.setStatus("current")


class _H3cCfgOperateFileName_Type(DisplayString):
    """Custom type h3cCfgOperateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_H3cCfgOperateFileName_Type.__name__ = "DisplayString"
_H3cCfgOperateFileName_Object = MibTableColumn
h3cCfgOperateFileName = _H3cCfgOperateFileName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 4),
    _H3cCfgOperateFileName_Type()
)
h3cCfgOperateFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateFileName.setStatus("current")
_H3cCfgOperateServerAddress_Type = IpAddress
_H3cCfgOperateServerAddress_Object = MibTableColumn
h3cCfgOperateServerAddress = _H3cCfgOperateServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 5),
    _H3cCfgOperateServerAddress_Type()
)
h3cCfgOperateServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateServerAddress.setStatus("deprecated")


class _H3cCfgOperateUserName_Type(DisplayString):
    """Custom type h3cCfgOperateUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_H3cCfgOperateUserName_Type.__name__ = "DisplayString"
_H3cCfgOperateUserName_Object = MibTableColumn
h3cCfgOperateUserName = _H3cCfgOperateUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 6),
    _H3cCfgOperateUserName_Type()
)
h3cCfgOperateUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateUserName.setStatus("current")


class _H3cCfgOperateUserPassword_Type(DisplayString):
    """Custom type h3cCfgOperateUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_H3cCfgOperateUserPassword_Type.__name__ = "DisplayString"
_H3cCfgOperateUserPassword_Object = MibTableColumn
h3cCfgOperateUserPassword = _H3cCfgOperateUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 7),
    _H3cCfgOperateUserPassword_Type()
)
h3cCfgOperateUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateUserPassword.setStatus("current")


class _H3cCfgOperateEndNotificationSwitch_Type(TruthValue):
    """Custom type h3cCfgOperateEndNotificationSwitch based on TruthValue"""


_H3cCfgOperateEndNotificationSwitch_Object = MibTableColumn
h3cCfgOperateEndNotificationSwitch = _H3cCfgOperateEndNotificationSwitch_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 8),
    _H3cCfgOperateEndNotificationSwitch_Type()
)
h3cCfgOperateEndNotificationSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateEndNotificationSwitch.setStatus("current")
_H3cCfgOperateRowStatus_Type = RowStatus
_H3cCfgOperateRowStatus_Object = MibTableColumn
h3cCfgOperateRowStatus = _H3cCfgOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 9),
    _H3cCfgOperateRowStatus_Type()
)
h3cCfgOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateRowStatus.setStatus("current")


class _H3cCfgOperateServerPort_Type(Integer32):
    """Custom type h3cCfgOperateServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cCfgOperateServerPort_Type.__name__ = "Integer32"
_H3cCfgOperateServerPort_Object = MibTableColumn
h3cCfgOperateServerPort = _H3cCfgOperateServerPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 10),
    _H3cCfgOperateServerPort_Type()
)
h3cCfgOperateServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateServerPort.setStatus("current")
_H3cCfgOperateSrvAddrType_Type = InetAddressType
_H3cCfgOperateSrvAddrType_Object = MibTableColumn
h3cCfgOperateSrvAddrType = _H3cCfgOperateSrvAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 11),
    _H3cCfgOperateSrvAddrType_Type()
)
h3cCfgOperateSrvAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateSrvAddrType.setStatus("current")
_H3cCfgOperateSrvAddrRev_Type = InetAddress
_H3cCfgOperateSrvAddrRev_Object = MibTableColumn
h3cCfgOperateSrvAddrRev = _H3cCfgOperateSrvAddrRev_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 12),
    _H3cCfgOperateSrvAddrRev_Type()
)
h3cCfgOperateSrvAddrRev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateSrvAddrRev.setStatus("current")
_H3cCfgOperateSrvVPNName_Type = DisplayString
_H3cCfgOperateSrvVPNName_Object = MibTableColumn
h3cCfgOperateSrvVPNName = _H3cCfgOperateSrvVPNName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 4, 1, 13),
    _H3cCfgOperateSrvVPNName_Type()
)
h3cCfgOperateSrvVPNName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cCfgOperateSrvVPNName.setStatus("current")
_H3cCfgOperateResultTable_Object = MibTable
h3cCfgOperateResultTable = _H3cCfgOperateResultTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5)
)
if mibBuilder.loadTexts:
    h3cCfgOperateResultTable.setStatus("current")
_H3cCfgOperateResultEntry_Object = MibTableRow
h3cCfgOperateResultEntry = _H3cCfgOperateResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1)
)
h3cCfgOperateResultEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateResultIndex"),
)
if mibBuilder.loadTexts:
    h3cCfgOperateResultEntry.setStatus("current")


class _H3cCfgOperateResultIndex_Type(Integer32):
    """Custom type h3cCfgOperateResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cCfgOperateResultIndex_Type.__name__ = "Integer32"
_H3cCfgOperateResultIndex_Object = MibTableColumn
h3cCfgOperateResultIndex = _H3cCfgOperateResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 1),
    _H3cCfgOperateResultIndex_Type()
)
h3cCfgOperateResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCfgOperateResultIndex.setStatus("current")


class _H3cCfgOperateResultOptIndex_Type(Integer32):
    """Custom type h3cCfgOperateResultOptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cCfgOperateResultOptIndex_Type.__name__ = "Integer32"
_H3cCfgOperateResultOptIndex_Object = MibTableColumn
h3cCfgOperateResultOptIndex = _H3cCfgOperateResultOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 2),
    _H3cCfgOperateResultOptIndex_Type()
)
h3cCfgOperateResultOptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgOperateResultOptIndex.setStatus("current")
_H3cCfgOperateResultOpType_Type = ConfigOperationType
_H3cCfgOperateResultOpType_Object = MibTableColumn
h3cCfgOperateResultOpType = _H3cCfgOperateResultOpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 3),
    _H3cCfgOperateResultOpType_Type()
)
h3cCfgOperateResultOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgOperateResultOpType.setStatus("current")
_H3cCfgOperateState_Type = ConfigOperationStateType
_H3cCfgOperateState_Object = MibTableColumn
h3cCfgOperateState = _H3cCfgOperateState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 4),
    _H3cCfgOperateState_Type()
)
h3cCfgOperateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgOperateState.setStatus("current")
_H3cCfgOperateTime_Type = TimeTicks
_H3cCfgOperateTime_Object = MibTableColumn
h3cCfgOperateTime = _H3cCfgOperateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 5),
    _H3cCfgOperateTime_Type()
)
h3cCfgOperateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgOperateTime.setStatus("current")
_H3cCfgOperateEndTime_Type = TimeTicks
_H3cCfgOperateEndTime_Object = MibTableColumn
h3cCfgOperateEndTime = _H3cCfgOperateEndTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 6),
    _H3cCfgOperateEndTime_Type()
)
h3cCfgOperateEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgOperateEndTime.setStatus("current")
_H3cCfgOperFailReason_Type = DisplayString
_H3cCfgOperFailReason_Object = MibTableColumn
h3cCfgOperFailReason = _H3cCfgOperFailReason_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 5, 1, 7),
    _H3cCfgOperFailReason_Type()
)
h3cCfgOperFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgOperFailReason.setStatus("current")
_H3cCfgExecuteOperate_ObjectIdentity = ObjectIdentity
h3cCfgExecuteOperate = _H3cCfgExecuteOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6)
)


class _H3cCfgExecuteOperateResultEntryLimit_Type(Integer32):
    """Custom type h3cCfgExecuteOperateResultEntryLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_H3cCfgExecuteOperateResultEntryLimit_Type.__name__ = "Integer32"
_H3cCfgExecuteOperateResultEntryLimit_Object = MibScalar
h3cCfgExecuteOperateResultEntryLimit = _H3cCfgExecuteOperateResultEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 1),
    _H3cCfgExecuteOperateResultEntryLimit_Type()
)
h3cCfgExecuteOperateResultEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCfgExecuteOperateResultEntryLimit.setStatus("current")
_H3cCfgExecuteResultTable_Object = MibTable
h3cCfgExecuteResultTable = _H3cCfgExecuteResultTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    h3cCfgExecuteResultTable.setStatus("current")
_H3cCfgExecuteResultEntry_Object = MibTableRow
h3cCfgExecuteResultEntry = _H3cCfgExecuteResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1)
)
h3cCfgExecuteResultEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgExecuteResultIndex"),
)
if mibBuilder.loadTexts:
    h3cCfgExecuteResultEntry.setStatus("current")


class _H3cCfgExecuteResultIndex_Type(Integer32):
    """Custom type h3cCfgExecuteResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cCfgExecuteResultIndex_Type.__name__ = "Integer32"
_H3cCfgExecuteResultIndex_Object = MibTableColumn
h3cCfgExecuteResultIndex = _H3cCfgExecuteResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 1),
    _H3cCfgExecuteResultIndex_Type()
)
h3cCfgExecuteResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cCfgExecuteResultIndex.setStatus("current")


class _H3cCfgExecuteResultOptIndex_Type(Integer32):
    """Custom type h3cCfgExecuteResultOptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cCfgExecuteResultOptIndex_Type.__name__ = "Integer32"
_H3cCfgExecuteResultOptIndex_Object = MibTableColumn
h3cCfgExecuteResultOptIndex = _H3cCfgExecuteResultOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 2),
    _H3cCfgExecuteResultOptIndex_Type()
)
h3cCfgExecuteResultOptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgExecuteResultOptIndex.setStatus("current")
_H3cCfgExecuteResultOpType_Type = ConfigOperationType
_H3cCfgExecuteResultOpType_Object = MibTableColumn
h3cCfgExecuteResultOpType = _H3cCfgExecuteResultOpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 3),
    _H3cCfgExecuteResultOpType_Type()
)
h3cCfgExecuteResultOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgExecuteResultOpType.setStatus("current")
_H3cCfgExecuteState_Type = ConfigOperationStateType
_H3cCfgExecuteState_Object = MibTableColumn
h3cCfgExecuteState = _H3cCfgExecuteState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 4),
    _H3cCfgExecuteState_Type()
)
h3cCfgExecuteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgExecuteState.setStatus("current")
_H3cCfgExecuteTime_Type = TimeTicks
_H3cCfgExecuteTime_Object = MibTableColumn
h3cCfgExecuteTime = _H3cCfgExecuteTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 5),
    _H3cCfgExecuteTime_Type()
)
h3cCfgExecuteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgExecuteTime.setStatus("current")
_H3cCfgExecuteEndTime_Type = TimeTicks
_H3cCfgExecuteEndTime_Object = MibTableColumn
h3cCfgExecuteEndTime = _H3cCfgExecuteEndTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 6, 2, 1, 6),
    _H3cCfgExecuteEndTime_Type()
)
h3cCfgExecuteEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfgExecuteEndTime.setStatus("current")


class _H3cCfgReset_Type(Integer32):
    """Custom type h3cCfgReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_H3cCfgReset_Type.__name__ = "Integer32"
_H3cCfgReset_Object = MibScalar
h3cCfgReset = _H3cCfgReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 1, 2, 7),
    _H3cCfgReset_Type()
)
h3cCfgReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cCfgReset.setStatus("current")
_H3cConfigManNotifications_ObjectIdentity = ObjectIdentity
h3cConfigManNotifications = _H3cConfigManNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 2)
)
_H3cConfigManConformance_ObjectIdentity = ObjectIdentity
h3cConfigManConformance = _H3cConfigManConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3)
)
_H3cConfigManCompliances_ObjectIdentity = ObjectIdentity
h3cConfigManCompliances = _H3cConfigManCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 1)
)
_H3cConfigManGroups_ObjectIdentity = ObjectIdentity
h3cConfigManGroups = _H3cConfigManGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 2)
)

# Managed Objects groups

h3cCfgManLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 2, 1)
)
h3cCfgManLogGroup.setObjects(
      *(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgRunModifiedLast"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgRunSavedLast"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgStartModifiedLast"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogLimitedEntries"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogDeletedEntries"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogTime"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogSrcCmd"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogTerminalType"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogTerminalNum"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogTerminalUser"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogTerminalLocation"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogCmdSrcAddress"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogVirHost"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogServerAddress"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogFile"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogUserName"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogWantBackup"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogSrcData"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogDesData"))
)
if mibBuilder.loadTexts:
    h3cCfgManLogGroup.setStatus("current")

h3cCfgOperateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 2, 2)
)
h3cCfgOperateGroup.setObjects(
      *(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateGlobalEntryLimit"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateEntryAgeOutTime"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateType"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateProtocol"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateFileName"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateServerAddress"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateUserName"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateUserPassword"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateTime"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateEndNotificationSwitch"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateResultGlobalEntryLimit"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateState"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateRowStatus"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateResultOptIndex"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateResultOpType"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateEndTime"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperFailReason"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateServerPort"))
)
if mibBuilder.loadTexts:
    h3cCfgOperateGroup.setStatus("current")


# Notification objects

h3cCfgManEventlog = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 2, 1)
)
h3cCfgManEventlog.setObjects(
      *(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogSrcCmd"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogSrcData"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgLogDesData"))
)
if mibBuilder.loadTexts:
    h3cCfgManEventlog.setStatus(
        "current"
    )

h3cCfgOperateCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 2, 2)
)
h3cCfgOperateCompletion.setObjects(
      *(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateType"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateTime"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateState"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateEndTime"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperFailReason"))
)
if mibBuilder.loadTexts:
    h3cCfgOperateCompletion.setStatus(
        "current"
    )

h3cCfgInvalidConfigFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 2, 3)
)
h3cCfgInvalidConfigFile.setObjects(
      *(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateType"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateFileName"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cCfgInvalidConfigFile.setStatus(
        "current"
    )


# Notifications groups

h3cCfgManNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 2, 3)
)
h3cCfgManNotificationGroup.setObjects(
      *(("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgManEventlog"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgOperateCompletion"),
        ("A3COM-HUAWEI-CONFIG-MAN-MIB", "h3cCfgInvalidConfigFile"))
)
if mibBuilder.loadTexts:
    h3cCfgManNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cConfigManCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cConfigManCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-CONFIG-MAN-MIB",
    **{"ConfigOperationType": ConfigOperationType,
       "ConfigOperationStateType": ConfigOperationStateType,
       "h3cConfig": h3cConfig,
       "h3cConfigManObjects": h3cConfigManObjects,
       "h3cCfgLog": h3cCfgLog,
       "h3cCfgRunModifiedLast": h3cCfgRunModifiedLast,
       "h3cCfgRunSavedLast": h3cCfgRunSavedLast,
       "h3cCfgStartModifiedLast": h3cCfgStartModifiedLast,
       "h3cCfgLogLimitedEntries": h3cCfgLogLimitedEntries,
       "h3cCfgLogDeletedEntries": h3cCfgLogDeletedEntries,
       "h3cCfgLogWantBackup": h3cCfgLogWantBackup,
       "h3cCfgLogTable": h3cCfgLogTable,
       "h3cCfgLogEntry": h3cCfgLogEntry,
       "h3cCfgLogIndex": h3cCfgLogIndex,
       "h3cCfgLogTime": h3cCfgLogTime,
       "h3cCfgLogSrcCmd": h3cCfgLogSrcCmd,
       "h3cCfgLogSrcData": h3cCfgLogSrcData,
       "h3cCfgLogDesData": h3cCfgLogDesData,
       "h3cCfgLogTerminalType": h3cCfgLogTerminalType,
       "h3cCfgLogTerminalUser": h3cCfgLogTerminalUser,
       "h3cCfgLogTerminalNum": h3cCfgLogTerminalNum,
       "h3cCfgLogTerminalLocation": h3cCfgLogTerminalLocation,
       "h3cCfgLogCmdSrcAddress": h3cCfgLogCmdSrcAddress,
       "h3cCfgLogVirHost": h3cCfgLogVirHost,
       "h3cCfgLogUserName": h3cCfgLogUserName,
       "h3cCfgLogServerAddress": h3cCfgLogServerAddress,
       "h3cCfgLogFile": h3cCfgLogFile,
       "h3cCfgLogCmdSrcAddrType": h3cCfgLogCmdSrcAddrType,
       "h3cCfgLogCmdSrcAddrRev": h3cCfgLogCmdSrcAddrRev,
       "h3cCfgLogCmdSrcAddrVPNName": h3cCfgLogCmdSrcAddrVPNName,
       "h3cCfgLogServerAddrType": h3cCfgLogServerAddrType,
       "h3cCfgLogServerAddrRev": h3cCfgLogServerAddrRev,
       "h3cCfgLogServerAddrVPNName": h3cCfgLogServerAddrVPNName,
       "h3cCfgFirstTrapTime": h3cCfgFirstTrapTime,
       "h3cCfgOperate": h3cCfgOperate,
       "h3cCfgOperateGlobalEntryLimit": h3cCfgOperateGlobalEntryLimit,
       "h3cCfgOperateEntryAgeOutTime": h3cCfgOperateEntryAgeOutTime,
       "h3cCfgOperateResultGlobalEntryLimit": h3cCfgOperateResultGlobalEntryLimit,
       "h3cCfgOperateTable": h3cCfgOperateTable,
       "h3cCfgOperateEntry": h3cCfgOperateEntry,
       "h3cCfgOperateIndex": h3cCfgOperateIndex,
       "h3cCfgOperateType": h3cCfgOperateType,
       "h3cCfgOperateProtocol": h3cCfgOperateProtocol,
       "h3cCfgOperateFileName": h3cCfgOperateFileName,
       "h3cCfgOperateServerAddress": h3cCfgOperateServerAddress,
       "h3cCfgOperateUserName": h3cCfgOperateUserName,
       "h3cCfgOperateUserPassword": h3cCfgOperateUserPassword,
       "h3cCfgOperateEndNotificationSwitch": h3cCfgOperateEndNotificationSwitch,
       "h3cCfgOperateRowStatus": h3cCfgOperateRowStatus,
       "h3cCfgOperateServerPort": h3cCfgOperateServerPort,
       "h3cCfgOperateSrvAddrType": h3cCfgOperateSrvAddrType,
       "h3cCfgOperateSrvAddrRev": h3cCfgOperateSrvAddrRev,
       "h3cCfgOperateSrvVPNName": h3cCfgOperateSrvVPNName,
       "h3cCfgOperateResultTable": h3cCfgOperateResultTable,
       "h3cCfgOperateResultEntry": h3cCfgOperateResultEntry,
       "h3cCfgOperateResultIndex": h3cCfgOperateResultIndex,
       "h3cCfgOperateResultOptIndex": h3cCfgOperateResultOptIndex,
       "h3cCfgOperateResultOpType": h3cCfgOperateResultOpType,
       "h3cCfgOperateState": h3cCfgOperateState,
       "h3cCfgOperateTime": h3cCfgOperateTime,
       "h3cCfgOperateEndTime": h3cCfgOperateEndTime,
       "h3cCfgOperFailReason": h3cCfgOperFailReason,
       "h3cCfgExecuteOperate": h3cCfgExecuteOperate,
       "h3cCfgExecuteOperateResultEntryLimit": h3cCfgExecuteOperateResultEntryLimit,
       "h3cCfgExecuteResultTable": h3cCfgExecuteResultTable,
       "h3cCfgExecuteResultEntry": h3cCfgExecuteResultEntry,
       "h3cCfgExecuteResultIndex": h3cCfgExecuteResultIndex,
       "h3cCfgExecuteResultOptIndex": h3cCfgExecuteResultOptIndex,
       "h3cCfgExecuteResultOpType": h3cCfgExecuteResultOpType,
       "h3cCfgExecuteState": h3cCfgExecuteState,
       "h3cCfgExecuteTime": h3cCfgExecuteTime,
       "h3cCfgExecuteEndTime": h3cCfgExecuteEndTime,
       "h3cCfgReset": h3cCfgReset,
       "h3cConfigManNotifications": h3cConfigManNotifications,
       "h3cCfgManEventlog": h3cCfgManEventlog,
       "h3cCfgOperateCompletion": h3cCfgOperateCompletion,
       "h3cCfgInvalidConfigFile": h3cCfgInvalidConfigFile,
       "h3cConfigManConformance": h3cConfigManConformance,
       "h3cConfigManCompliances": h3cConfigManCompliances,
       "h3cConfigManCompliance": h3cConfigManCompliance,
       "h3cConfigManGroups": h3cConfigManGroups,
       "h3cCfgManLogGroup": h3cCfgManLogGroup,
       "h3cCfgOperateGroup": h3cCfgOperateGroup,
       "h3cCfgManNotificationGroup": h3cCfgManNotificationGroup}
)

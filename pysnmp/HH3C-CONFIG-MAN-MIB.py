# SNMP MIB module (HH3C-CONFIG-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-CONFIG-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:36 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4)
)
hh3cConfig.setRevisions(
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

_Hh3cConfigManObjects_ObjectIdentity = ObjectIdentity
hh3cConfigManObjects = _Hh3cConfigManObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1)
)
_Hh3cCfgLog_ObjectIdentity = ObjectIdentity
hh3cCfgLog = _Hh3cCfgLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1)
)
_Hh3cCfgRunModifiedLast_Type = TimeTicks
_Hh3cCfgRunModifiedLast_Object = MibScalar
hh3cCfgRunModifiedLast = _Hh3cCfgRunModifiedLast_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 1),
    _Hh3cCfgRunModifiedLast_Type()
)
hh3cCfgRunModifiedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgRunModifiedLast.setStatus("current")
_Hh3cCfgRunSavedLast_Type = TimeTicks
_Hh3cCfgRunSavedLast_Object = MibScalar
hh3cCfgRunSavedLast = _Hh3cCfgRunSavedLast_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 2),
    _Hh3cCfgRunSavedLast_Type()
)
hh3cCfgRunSavedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgRunSavedLast.setStatus("current")
_Hh3cCfgStartModifiedLast_Type = TimeTicks
_Hh3cCfgStartModifiedLast_Object = MibScalar
hh3cCfgStartModifiedLast = _Hh3cCfgStartModifiedLast_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 3),
    _Hh3cCfgStartModifiedLast_Type()
)
hh3cCfgStartModifiedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgStartModifiedLast.setStatus("current")


class _Hh3cCfgLogLimitedEntries_Type(Integer32):
    """Custom type hh3cCfgLogLimitedEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cCfgLogLimitedEntries_Type.__name__ = "Integer32"
_Hh3cCfgLogLimitedEntries_Object = MibScalar
hh3cCfgLogLimitedEntries = _Hh3cCfgLogLimitedEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 4),
    _Hh3cCfgLogLimitedEntries_Type()
)
hh3cCfgLogLimitedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogLimitedEntries.setStatus("current")
_Hh3cCfgLogDeletedEntries_Type = Counter32
_Hh3cCfgLogDeletedEntries_Object = MibScalar
hh3cCfgLogDeletedEntries = _Hh3cCfgLogDeletedEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 5),
    _Hh3cCfgLogDeletedEntries_Type()
)
hh3cCfgLogDeletedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogDeletedEntries.setStatus("current")


class _Hh3cCfgLogWantBackup_Type(TruthValue):
    """Custom type hh3cCfgLogWantBackup based on TruthValue"""


_Hh3cCfgLogWantBackup_Object = MibScalar
hh3cCfgLogWantBackup = _Hh3cCfgLogWantBackup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 6),
    _Hh3cCfgLogWantBackup_Type()
)
hh3cCfgLogWantBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCfgLogWantBackup.setStatus("current")
_Hh3cCfgLogTable_Object = MibTable
hh3cCfgLogTable = _Hh3cCfgLogTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cCfgLogTable.setStatus("current")
_Hh3cCfgLogEntry_Object = MibTableRow
hh3cCfgLogEntry = _Hh3cCfgLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1)
)
hh3cCfgLogEntry.setIndexNames(
    (0, "HH3C-CONFIG-MAN-MIB", "hh3cCfgLogIndex"),
)
if mibBuilder.loadTexts:
    hh3cCfgLogEntry.setStatus("current")


class _Hh3cCfgLogIndex_Type(Integer32):
    """Custom type hh3cCfgLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cCfgLogIndex_Type.__name__ = "Integer32"
_Hh3cCfgLogIndex_Object = MibTableColumn
hh3cCfgLogIndex = _Hh3cCfgLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 1),
    _Hh3cCfgLogIndex_Type()
)
hh3cCfgLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCfgLogIndex.setStatus("current")
_Hh3cCfgLogTime_Type = TimeTicks
_Hh3cCfgLogTime_Object = MibTableColumn
hh3cCfgLogTime = _Hh3cCfgLogTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 2),
    _Hh3cCfgLogTime_Type()
)
hh3cCfgLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogTime.setStatus("current")


class _Hh3cCfgLogSrcCmd_Type(Integer32):
    """Custom type hh3cCfgLogSrcCmd based on Integer32"""
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


_Hh3cCfgLogSrcCmd_Type.__name__ = "Integer32"
_Hh3cCfgLogSrcCmd_Object = MibTableColumn
hh3cCfgLogSrcCmd = _Hh3cCfgLogSrcCmd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 3),
    _Hh3cCfgLogSrcCmd_Type()
)
hh3cCfgLogSrcCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogSrcCmd.setStatus("current")


class _Hh3cCfgLogSrcData_Type(Integer32):
    """Custom type hh3cCfgLogSrcData based on Integer32"""
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


_Hh3cCfgLogSrcData_Type.__name__ = "Integer32"
_Hh3cCfgLogSrcData_Object = MibTableColumn
hh3cCfgLogSrcData = _Hh3cCfgLogSrcData_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 4),
    _Hh3cCfgLogSrcData_Type()
)
hh3cCfgLogSrcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogSrcData.setStatus("current")


class _Hh3cCfgLogDesData_Type(Integer32):
    """Custom type hh3cCfgLogDesData based on Integer32"""
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


_Hh3cCfgLogDesData_Type.__name__ = "Integer32"
_Hh3cCfgLogDesData_Object = MibTableColumn
hh3cCfgLogDesData = _Hh3cCfgLogDesData_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 5),
    _Hh3cCfgLogDesData_Type()
)
hh3cCfgLogDesData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogDesData.setStatus("current")


class _Hh3cCfgLogTerminalType_Type(Integer32):
    """Custom type hh3cCfgLogTerminalType based on Integer32"""
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


_Hh3cCfgLogTerminalType_Type.__name__ = "Integer32"
_Hh3cCfgLogTerminalType_Object = MibTableColumn
hh3cCfgLogTerminalType = _Hh3cCfgLogTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 6),
    _Hh3cCfgLogTerminalType_Type()
)
hh3cCfgLogTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogTerminalType.setStatus("current")


class _Hh3cCfgLogTerminalUser_Type(DisplayString):
    """Custom type hh3cCfgLogTerminalUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cCfgLogTerminalUser_Type.__name__ = "DisplayString"
_Hh3cCfgLogTerminalUser_Object = MibTableColumn
hh3cCfgLogTerminalUser = _Hh3cCfgLogTerminalUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 7),
    _Hh3cCfgLogTerminalUser_Type()
)
hh3cCfgLogTerminalUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogTerminalUser.setStatus("current")
_Hh3cCfgLogTerminalNum_Type = Integer32
_Hh3cCfgLogTerminalNum_Object = MibTableColumn
hh3cCfgLogTerminalNum = _Hh3cCfgLogTerminalNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 8),
    _Hh3cCfgLogTerminalNum_Type()
)
hh3cCfgLogTerminalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogTerminalNum.setStatus("current")


class _Hh3cCfgLogTerminalLocation_Type(DisplayString):
    """Custom type hh3cCfgLogTerminalLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cCfgLogTerminalLocation_Type.__name__ = "DisplayString"
_Hh3cCfgLogTerminalLocation_Object = MibTableColumn
hh3cCfgLogTerminalLocation = _Hh3cCfgLogTerminalLocation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 9),
    _Hh3cCfgLogTerminalLocation_Type()
)
hh3cCfgLogTerminalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogTerminalLocation.setStatus("current")
_Hh3cCfgLogCmdSrcAddress_Type = IpAddress
_Hh3cCfgLogCmdSrcAddress_Object = MibTableColumn
hh3cCfgLogCmdSrcAddress = _Hh3cCfgLogCmdSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 10),
    _Hh3cCfgLogCmdSrcAddress_Type()
)
hh3cCfgLogCmdSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogCmdSrcAddress.setStatus("deprecated")


class _Hh3cCfgLogVirHost_Type(DisplayString):
    """Custom type hh3cCfgLogVirHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cCfgLogVirHost_Type.__name__ = "DisplayString"
_Hh3cCfgLogVirHost_Object = MibTableColumn
hh3cCfgLogVirHost = _Hh3cCfgLogVirHost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 11),
    _Hh3cCfgLogVirHost_Type()
)
hh3cCfgLogVirHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogVirHost.setStatus("current")


class _Hh3cCfgLogUserName_Type(DisplayString):
    """Custom type hh3cCfgLogUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cCfgLogUserName_Type.__name__ = "DisplayString"
_Hh3cCfgLogUserName_Object = MibTableColumn
hh3cCfgLogUserName = _Hh3cCfgLogUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 12),
    _Hh3cCfgLogUserName_Type()
)
hh3cCfgLogUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogUserName.setStatus("current")
_Hh3cCfgLogServerAddress_Type = IpAddress
_Hh3cCfgLogServerAddress_Object = MibTableColumn
hh3cCfgLogServerAddress = _Hh3cCfgLogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 13),
    _Hh3cCfgLogServerAddress_Type()
)
hh3cCfgLogServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogServerAddress.setStatus("deprecated")


class _Hh3cCfgLogFile_Type(DisplayString):
    """Custom type hh3cCfgLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cCfgLogFile_Type.__name__ = "DisplayString"
_Hh3cCfgLogFile_Object = MibTableColumn
hh3cCfgLogFile = _Hh3cCfgLogFile_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 14),
    _Hh3cCfgLogFile_Type()
)
hh3cCfgLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogFile.setStatus("current")
_Hh3cCfgLogCmdSrcAddrType_Type = InetAddressType
_Hh3cCfgLogCmdSrcAddrType_Object = MibTableColumn
hh3cCfgLogCmdSrcAddrType = _Hh3cCfgLogCmdSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 15),
    _Hh3cCfgLogCmdSrcAddrType_Type()
)
hh3cCfgLogCmdSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogCmdSrcAddrType.setStatus("current")
_Hh3cCfgLogCmdSrcAddrRev_Type = InetAddress
_Hh3cCfgLogCmdSrcAddrRev_Object = MibTableColumn
hh3cCfgLogCmdSrcAddrRev = _Hh3cCfgLogCmdSrcAddrRev_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 16),
    _Hh3cCfgLogCmdSrcAddrRev_Type()
)
hh3cCfgLogCmdSrcAddrRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogCmdSrcAddrRev.setStatus("current")
_Hh3cCfgLogCmdSrcAddrVPNName_Type = DisplayString
_Hh3cCfgLogCmdSrcAddrVPNName_Object = MibTableColumn
hh3cCfgLogCmdSrcAddrVPNName = _Hh3cCfgLogCmdSrcAddrVPNName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 17),
    _Hh3cCfgLogCmdSrcAddrVPNName_Type()
)
hh3cCfgLogCmdSrcAddrVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogCmdSrcAddrVPNName.setStatus("current")
_Hh3cCfgLogServerAddrType_Type = InetAddressType
_Hh3cCfgLogServerAddrType_Object = MibTableColumn
hh3cCfgLogServerAddrType = _Hh3cCfgLogServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 18),
    _Hh3cCfgLogServerAddrType_Type()
)
hh3cCfgLogServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogServerAddrType.setStatus("current")
_Hh3cCfgLogServerAddrRev_Type = InetAddress
_Hh3cCfgLogServerAddrRev_Object = MibTableColumn
hh3cCfgLogServerAddrRev = _Hh3cCfgLogServerAddrRev_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 19),
    _Hh3cCfgLogServerAddrRev_Type()
)
hh3cCfgLogServerAddrRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogServerAddrRev.setStatus("current")
_Hh3cCfgLogServerAddrVPNName_Type = DisplayString
_Hh3cCfgLogServerAddrVPNName_Object = MibTableColumn
hh3cCfgLogServerAddrVPNName = _Hh3cCfgLogServerAddrVPNName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 7, 1, 20),
    _Hh3cCfgLogServerAddrVPNName_Type()
)
hh3cCfgLogServerAddrVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgLogServerAddrVPNName.setStatus("current")
_Hh3cCfgFirstTrapTime_Type = TimeTicks
_Hh3cCfgFirstTrapTime_Object = MibScalar
hh3cCfgFirstTrapTime = _Hh3cCfgFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 1, 8),
    _Hh3cCfgFirstTrapTime_Type()
)
hh3cCfgFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCfgFirstTrapTime.setStatus("current")
_Hh3cCfgOperate_ObjectIdentity = ObjectIdentity
hh3cCfgOperate = _Hh3cCfgOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2)
)


class _Hh3cCfgOperateGlobalEntryLimit_Type(Integer32):
    """Custom type hh3cCfgOperateGlobalEntryLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hh3cCfgOperateGlobalEntryLimit_Type.__name__ = "Integer32"
_Hh3cCfgOperateGlobalEntryLimit_Object = MibScalar
hh3cCfgOperateGlobalEntryLimit = _Hh3cCfgOperateGlobalEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 1),
    _Hh3cCfgOperateGlobalEntryLimit_Type()
)
hh3cCfgOperateGlobalEntryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgOperateGlobalEntryLimit.setStatus("current")


class _Hh3cCfgOperateEntryAgeOutTime_Type(Integer32):
    """Custom type hh3cCfgOperateEntryAgeOutTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Hh3cCfgOperateEntryAgeOutTime_Type.__name__ = "Integer32"
_Hh3cCfgOperateEntryAgeOutTime_Object = MibScalar
hh3cCfgOperateEntryAgeOutTime = _Hh3cCfgOperateEntryAgeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 2),
    _Hh3cCfgOperateEntryAgeOutTime_Type()
)
hh3cCfgOperateEntryAgeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCfgOperateEntryAgeOutTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCfgOperateEntryAgeOutTime.setUnits("minute")


class _Hh3cCfgOperateResultGlobalEntryLimit_Type(Integer32):
    """Custom type hh3cCfgOperateResultGlobalEntryLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Hh3cCfgOperateResultGlobalEntryLimit_Type.__name__ = "Integer32"
_Hh3cCfgOperateResultGlobalEntryLimit_Object = MibScalar
hh3cCfgOperateResultGlobalEntryLimit = _Hh3cCfgOperateResultGlobalEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 3),
    _Hh3cCfgOperateResultGlobalEntryLimit_Type()
)
hh3cCfgOperateResultGlobalEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCfgOperateResultGlobalEntryLimit.setStatus("current")
_Hh3cCfgOperateTable_Object = MibTable
hh3cCfgOperateTable = _Hh3cCfgOperateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cCfgOperateTable.setStatus("current")
_Hh3cCfgOperateEntry_Object = MibTableRow
hh3cCfgOperateEntry = _Hh3cCfgOperateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1)
)
hh3cCfgOperateEntry.setIndexNames(
    (0, "HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateIndex"),
)
if mibBuilder.loadTexts:
    hh3cCfgOperateEntry.setStatus("current")


class _Hh3cCfgOperateIndex_Type(Integer32):
    """Custom type hh3cCfgOperateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cCfgOperateIndex_Type.__name__ = "Integer32"
_Hh3cCfgOperateIndex_Object = MibTableColumn
hh3cCfgOperateIndex = _Hh3cCfgOperateIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 1),
    _Hh3cCfgOperateIndex_Type()
)
hh3cCfgOperateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCfgOperateIndex.setStatus("current")
_Hh3cCfgOperateType_Type = ConfigOperationType
_Hh3cCfgOperateType_Object = MibTableColumn
hh3cCfgOperateType = _Hh3cCfgOperateType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 2),
    _Hh3cCfgOperateType_Type()
)
hh3cCfgOperateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateType.setStatus("current")


class _Hh3cCfgOperateProtocol_Type(Integer32):
    """Custom type hh3cCfgOperateProtocol based on Integer32"""
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


_Hh3cCfgOperateProtocol_Type.__name__ = "Integer32"
_Hh3cCfgOperateProtocol_Object = MibTableColumn
hh3cCfgOperateProtocol = _Hh3cCfgOperateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 3),
    _Hh3cCfgOperateProtocol_Type()
)
hh3cCfgOperateProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateProtocol.setStatus("current")


class _Hh3cCfgOperateFileName_Type(DisplayString):
    """Custom type hh3cCfgOperateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cCfgOperateFileName_Type.__name__ = "DisplayString"
_Hh3cCfgOperateFileName_Object = MibTableColumn
hh3cCfgOperateFileName = _Hh3cCfgOperateFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 4),
    _Hh3cCfgOperateFileName_Type()
)
hh3cCfgOperateFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateFileName.setStatus("current")
_Hh3cCfgOperateServerAddress_Type = IpAddress
_Hh3cCfgOperateServerAddress_Object = MibTableColumn
hh3cCfgOperateServerAddress = _Hh3cCfgOperateServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 5),
    _Hh3cCfgOperateServerAddress_Type()
)
hh3cCfgOperateServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateServerAddress.setStatus("deprecated")


class _Hh3cCfgOperateUserName_Type(DisplayString):
    """Custom type hh3cCfgOperateUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Hh3cCfgOperateUserName_Type.__name__ = "DisplayString"
_Hh3cCfgOperateUserName_Object = MibTableColumn
hh3cCfgOperateUserName = _Hh3cCfgOperateUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 6),
    _Hh3cCfgOperateUserName_Type()
)
hh3cCfgOperateUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateUserName.setStatus("current")


class _Hh3cCfgOperateUserPassword_Type(DisplayString):
    """Custom type hh3cCfgOperateUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Hh3cCfgOperateUserPassword_Type.__name__ = "DisplayString"
_Hh3cCfgOperateUserPassword_Object = MibTableColumn
hh3cCfgOperateUserPassword = _Hh3cCfgOperateUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 7),
    _Hh3cCfgOperateUserPassword_Type()
)
hh3cCfgOperateUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateUserPassword.setStatus("current")


class _Hh3cCfgOperateEndNotificationSwitch_Type(TruthValue):
    """Custom type hh3cCfgOperateEndNotificationSwitch based on TruthValue"""


_Hh3cCfgOperateEndNotificationSwitch_Object = MibTableColumn
hh3cCfgOperateEndNotificationSwitch = _Hh3cCfgOperateEndNotificationSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 8),
    _Hh3cCfgOperateEndNotificationSwitch_Type()
)
hh3cCfgOperateEndNotificationSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateEndNotificationSwitch.setStatus("current")
_Hh3cCfgOperateRowStatus_Type = RowStatus
_Hh3cCfgOperateRowStatus_Object = MibTableColumn
hh3cCfgOperateRowStatus = _Hh3cCfgOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 9),
    _Hh3cCfgOperateRowStatus_Type()
)
hh3cCfgOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateRowStatus.setStatus("current")


class _Hh3cCfgOperateServerPort_Type(Integer32):
    """Custom type hh3cCfgOperateServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cCfgOperateServerPort_Type.__name__ = "Integer32"
_Hh3cCfgOperateServerPort_Object = MibTableColumn
hh3cCfgOperateServerPort = _Hh3cCfgOperateServerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 10),
    _Hh3cCfgOperateServerPort_Type()
)
hh3cCfgOperateServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateServerPort.setStatus("current")
_Hh3cCfgOperateSrvAddrType_Type = InetAddressType
_Hh3cCfgOperateSrvAddrType_Object = MibTableColumn
hh3cCfgOperateSrvAddrType = _Hh3cCfgOperateSrvAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 11),
    _Hh3cCfgOperateSrvAddrType_Type()
)
hh3cCfgOperateSrvAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateSrvAddrType.setStatus("current")
_Hh3cCfgOperateSrvAddrRev_Type = InetAddress
_Hh3cCfgOperateSrvAddrRev_Object = MibTableColumn
hh3cCfgOperateSrvAddrRev = _Hh3cCfgOperateSrvAddrRev_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 12),
    _Hh3cCfgOperateSrvAddrRev_Type()
)
hh3cCfgOperateSrvAddrRev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateSrvAddrRev.setStatus("current")
_Hh3cCfgOperateSrvVPNName_Type = DisplayString
_Hh3cCfgOperateSrvVPNName_Object = MibTableColumn
hh3cCfgOperateSrvVPNName = _Hh3cCfgOperateSrvVPNName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 4, 1, 13),
    _Hh3cCfgOperateSrvVPNName_Type()
)
hh3cCfgOperateSrvVPNName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCfgOperateSrvVPNName.setStatus("current")
_Hh3cCfgOperateResultTable_Object = MibTable
hh3cCfgOperateResultTable = _Hh3cCfgOperateResultTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cCfgOperateResultTable.setStatus("current")
_Hh3cCfgOperateResultEntry_Object = MibTableRow
hh3cCfgOperateResultEntry = _Hh3cCfgOperateResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1)
)
hh3cCfgOperateResultEntry.setIndexNames(
    (0, "HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateResultIndex"),
)
if mibBuilder.loadTexts:
    hh3cCfgOperateResultEntry.setStatus("current")


class _Hh3cCfgOperateResultIndex_Type(Integer32):
    """Custom type hh3cCfgOperateResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cCfgOperateResultIndex_Type.__name__ = "Integer32"
_Hh3cCfgOperateResultIndex_Object = MibTableColumn
hh3cCfgOperateResultIndex = _Hh3cCfgOperateResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 1),
    _Hh3cCfgOperateResultIndex_Type()
)
hh3cCfgOperateResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCfgOperateResultIndex.setStatus("current")


class _Hh3cCfgOperateResultOptIndex_Type(Integer32):
    """Custom type hh3cCfgOperateResultOptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cCfgOperateResultOptIndex_Type.__name__ = "Integer32"
_Hh3cCfgOperateResultOptIndex_Object = MibTableColumn
hh3cCfgOperateResultOptIndex = _Hh3cCfgOperateResultOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 2),
    _Hh3cCfgOperateResultOptIndex_Type()
)
hh3cCfgOperateResultOptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgOperateResultOptIndex.setStatus("current")
_Hh3cCfgOperateResultOpType_Type = ConfigOperationType
_Hh3cCfgOperateResultOpType_Object = MibTableColumn
hh3cCfgOperateResultOpType = _Hh3cCfgOperateResultOpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 3),
    _Hh3cCfgOperateResultOpType_Type()
)
hh3cCfgOperateResultOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgOperateResultOpType.setStatus("current")
_Hh3cCfgOperateState_Type = ConfigOperationStateType
_Hh3cCfgOperateState_Object = MibTableColumn
hh3cCfgOperateState = _Hh3cCfgOperateState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 4),
    _Hh3cCfgOperateState_Type()
)
hh3cCfgOperateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgOperateState.setStatus("current")
_Hh3cCfgOperateTime_Type = TimeTicks
_Hh3cCfgOperateTime_Object = MibTableColumn
hh3cCfgOperateTime = _Hh3cCfgOperateTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 5),
    _Hh3cCfgOperateTime_Type()
)
hh3cCfgOperateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgOperateTime.setStatus("current")
_Hh3cCfgOperateEndTime_Type = TimeTicks
_Hh3cCfgOperateEndTime_Object = MibTableColumn
hh3cCfgOperateEndTime = _Hh3cCfgOperateEndTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 6),
    _Hh3cCfgOperateEndTime_Type()
)
hh3cCfgOperateEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgOperateEndTime.setStatus("current")
_Hh3cCfgOperFailReason_Type = DisplayString
_Hh3cCfgOperFailReason_Object = MibTableColumn
hh3cCfgOperFailReason = _Hh3cCfgOperFailReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 5, 1, 7),
    _Hh3cCfgOperFailReason_Type()
)
hh3cCfgOperFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgOperFailReason.setStatus("current")
_Hh3cCfgExecuteOperate_ObjectIdentity = ObjectIdentity
hh3cCfgExecuteOperate = _Hh3cCfgExecuteOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6)
)


class _Hh3cCfgExecuteOperateResultEntryLimit_Type(Integer32):
    """Custom type hh3cCfgExecuteOperateResultEntryLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_Hh3cCfgExecuteOperateResultEntryLimit_Type.__name__ = "Integer32"
_Hh3cCfgExecuteOperateResultEntryLimit_Object = MibScalar
hh3cCfgExecuteOperateResultEntryLimit = _Hh3cCfgExecuteOperateResultEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 1),
    _Hh3cCfgExecuteOperateResultEntryLimit_Type()
)
hh3cCfgExecuteOperateResultEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCfgExecuteOperateResultEntryLimit.setStatus("current")
_Hh3cCfgExecuteResultTable_Object = MibTable
hh3cCfgExecuteResultTable = _Hh3cCfgExecuteResultTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    hh3cCfgExecuteResultTable.setStatus("current")
_Hh3cCfgExecuteResultEntry_Object = MibTableRow
hh3cCfgExecuteResultEntry = _Hh3cCfgExecuteResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1)
)
hh3cCfgExecuteResultEntry.setIndexNames(
    (0, "HH3C-CONFIG-MAN-MIB", "hh3cCfgExecuteResultIndex"),
)
if mibBuilder.loadTexts:
    hh3cCfgExecuteResultEntry.setStatus("current")


class _Hh3cCfgExecuteResultIndex_Type(Integer32):
    """Custom type hh3cCfgExecuteResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cCfgExecuteResultIndex_Type.__name__ = "Integer32"
_Hh3cCfgExecuteResultIndex_Object = MibTableColumn
hh3cCfgExecuteResultIndex = _Hh3cCfgExecuteResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 1),
    _Hh3cCfgExecuteResultIndex_Type()
)
hh3cCfgExecuteResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCfgExecuteResultIndex.setStatus("current")


class _Hh3cCfgExecuteResultOptIndex_Type(Integer32):
    """Custom type hh3cCfgExecuteResultOptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cCfgExecuteResultOptIndex_Type.__name__ = "Integer32"
_Hh3cCfgExecuteResultOptIndex_Object = MibTableColumn
hh3cCfgExecuteResultOptIndex = _Hh3cCfgExecuteResultOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 2),
    _Hh3cCfgExecuteResultOptIndex_Type()
)
hh3cCfgExecuteResultOptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgExecuteResultOptIndex.setStatus("current")
_Hh3cCfgExecuteResultOpType_Type = ConfigOperationType
_Hh3cCfgExecuteResultOpType_Object = MibTableColumn
hh3cCfgExecuteResultOpType = _Hh3cCfgExecuteResultOpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 3),
    _Hh3cCfgExecuteResultOpType_Type()
)
hh3cCfgExecuteResultOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgExecuteResultOpType.setStatus("current")
_Hh3cCfgExecuteState_Type = ConfigOperationStateType
_Hh3cCfgExecuteState_Object = MibTableColumn
hh3cCfgExecuteState = _Hh3cCfgExecuteState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 4),
    _Hh3cCfgExecuteState_Type()
)
hh3cCfgExecuteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgExecuteState.setStatus("current")
_Hh3cCfgExecuteTime_Type = TimeTicks
_Hh3cCfgExecuteTime_Object = MibTableColumn
hh3cCfgExecuteTime = _Hh3cCfgExecuteTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 5),
    _Hh3cCfgExecuteTime_Type()
)
hh3cCfgExecuteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgExecuteTime.setStatus("current")
_Hh3cCfgExecuteEndTime_Type = TimeTicks
_Hh3cCfgExecuteEndTime_Object = MibTableColumn
hh3cCfgExecuteEndTime = _Hh3cCfgExecuteEndTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 6, 2, 1, 6),
    _Hh3cCfgExecuteEndTime_Type()
)
hh3cCfgExecuteEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfgExecuteEndTime.setStatus("current")


class _Hh3cCfgReset_Type(Integer32):
    """Custom type hh3cCfgReset based on Integer32"""
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


_Hh3cCfgReset_Type.__name__ = "Integer32"
_Hh3cCfgReset_Object = MibScalar
hh3cCfgReset = _Hh3cCfgReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 7),
    _Hh3cCfgReset_Type()
)
hh3cCfgReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCfgReset.setStatus("current")


class _Hh3cCfgReset2_Type(Integer32):
    """Custom type hh3cCfgReset2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1))
    )


_Hh3cCfgReset2_Type.__name__ = "Integer32"
_Hh3cCfgReset2_Object = MibScalar
hh3cCfgReset2 = _Hh3cCfgReset2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 1, 2, 8),
    _Hh3cCfgReset2_Type()
)
hh3cCfgReset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCfgReset2.setStatus("current")
_Hh3cConfigManNotifications_ObjectIdentity = ObjectIdentity
hh3cConfigManNotifications = _Hh3cConfigManNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 2)
)
_Hh3cConfigManConformance_ObjectIdentity = ObjectIdentity
hh3cConfigManConformance = _Hh3cConfigManConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 3)
)
_Hh3cConfigManCompliances_ObjectIdentity = ObjectIdentity
hh3cConfigManCompliances = _Hh3cConfigManCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 1)
)
_Hh3cConfigManGroups_ObjectIdentity = ObjectIdentity
hh3cConfigManGroups = _Hh3cConfigManGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 2)
)

# Managed Objects groups

hh3cCfgManLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 2, 1)
)
hh3cCfgManLogGroup.setObjects(
      *(("HH3C-CONFIG-MAN-MIB", "hh3cCfgRunModifiedLast"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgRunSavedLast"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgStartModifiedLast"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogLimitedEntries"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogDeletedEntries"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogTime"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogSrcCmd"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogTerminalType"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogTerminalNum"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogTerminalUser"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogTerminalLocation"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogCmdSrcAddress"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogVirHost"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogServerAddress"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogFile"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogUserName"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogWantBackup"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogSrcData"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogDesData"))
)
if mibBuilder.loadTexts:
    hh3cCfgManLogGroup.setStatus("current")

hh3cCfgOperateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 2, 2)
)
hh3cCfgOperateGroup.setObjects(
      *(("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateGlobalEntryLimit"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateEntryAgeOutTime"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateType"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateProtocol"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateFileName"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateServerAddress"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateUserName"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateUserPassword"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateTime"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateEndNotificationSwitch"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateResultGlobalEntryLimit"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateState"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateRowStatus"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateResultOptIndex"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateResultOpType"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateEndTime"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperFailReason"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateServerPort"))
)
if mibBuilder.loadTexts:
    hh3cCfgOperateGroup.setStatus("current")


# Notification objects

hh3cCfgManEventlog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 2, 1)
)
hh3cCfgManEventlog.setObjects(
      *(("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogSrcCmd"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogSrcData"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgLogDesData"))
)
if mibBuilder.loadTexts:
    hh3cCfgManEventlog.setStatus(
        "current"
    )

hh3cCfgOperateCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 2, 2)
)
hh3cCfgOperateCompletion.setObjects(
      *(("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateType"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateTime"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateState"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateEndTime"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperFailReason"))
)
if mibBuilder.loadTexts:
    hh3cCfgOperateCompletion.setStatus(
        "current"
    )

hh3cCfgInvalidConfigFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 2, 3)
)
hh3cCfgInvalidConfigFile.setObjects(
      *(("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateType"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateFileName"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cCfgInvalidConfigFile.setStatus(
        "current"
    )


# Notifications groups

hh3cCfgManNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 2, 3)
)
hh3cCfgManNotificationGroup.setObjects(
      *(("HH3C-CONFIG-MAN-MIB", "hh3cCfgManEventlog"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgOperateCompletion"),
        ("HH3C-CONFIG-MAN-MIB", "hh3cCfgInvalidConfigFile"))
)
if mibBuilder.loadTexts:
    hh3cCfgManNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cConfigManCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cConfigManCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-CONFIG-MAN-MIB",
    **{"ConfigOperationType": ConfigOperationType,
       "ConfigOperationStateType": ConfigOperationStateType,
       "hh3cConfig": hh3cConfig,
       "hh3cConfigManObjects": hh3cConfigManObjects,
       "hh3cCfgLog": hh3cCfgLog,
       "hh3cCfgRunModifiedLast": hh3cCfgRunModifiedLast,
       "hh3cCfgRunSavedLast": hh3cCfgRunSavedLast,
       "hh3cCfgStartModifiedLast": hh3cCfgStartModifiedLast,
       "hh3cCfgLogLimitedEntries": hh3cCfgLogLimitedEntries,
       "hh3cCfgLogDeletedEntries": hh3cCfgLogDeletedEntries,
       "hh3cCfgLogWantBackup": hh3cCfgLogWantBackup,
       "hh3cCfgLogTable": hh3cCfgLogTable,
       "hh3cCfgLogEntry": hh3cCfgLogEntry,
       "hh3cCfgLogIndex": hh3cCfgLogIndex,
       "hh3cCfgLogTime": hh3cCfgLogTime,
       "hh3cCfgLogSrcCmd": hh3cCfgLogSrcCmd,
       "hh3cCfgLogSrcData": hh3cCfgLogSrcData,
       "hh3cCfgLogDesData": hh3cCfgLogDesData,
       "hh3cCfgLogTerminalType": hh3cCfgLogTerminalType,
       "hh3cCfgLogTerminalUser": hh3cCfgLogTerminalUser,
       "hh3cCfgLogTerminalNum": hh3cCfgLogTerminalNum,
       "hh3cCfgLogTerminalLocation": hh3cCfgLogTerminalLocation,
       "hh3cCfgLogCmdSrcAddress": hh3cCfgLogCmdSrcAddress,
       "hh3cCfgLogVirHost": hh3cCfgLogVirHost,
       "hh3cCfgLogUserName": hh3cCfgLogUserName,
       "hh3cCfgLogServerAddress": hh3cCfgLogServerAddress,
       "hh3cCfgLogFile": hh3cCfgLogFile,
       "hh3cCfgLogCmdSrcAddrType": hh3cCfgLogCmdSrcAddrType,
       "hh3cCfgLogCmdSrcAddrRev": hh3cCfgLogCmdSrcAddrRev,
       "hh3cCfgLogCmdSrcAddrVPNName": hh3cCfgLogCmdSrcAddrVPNName,
       "hh3cCfgLogServerAddrType": hh3cCfgLogServerAddrType,
       "hh3cCfgLogServerAddrRev": hh3cCfgLogServerAddrRev,
       "hh3cCfgLogServerAddrVPNName": hh3cCfgLogServerAddrVPNName,
       "hh3cCfgFirstTrapTime": hh3cCfgFirstTrapTime,
       "hh3cCfgOperate": hh3cCfgOperate,
       "hh3cCfgOperateGlobalEntryLimit": hh3cCfgOperateGlobalEntryLimit,
       "hh3cCfgOperateEntryAgeOutTime": hh3cCfgOperateEntryAgeOutTime,
       "hh3cCfgOperateResultGlobalEntryLimit": hh3cCfgOperateResultGlobalEntryLimit,
       "hh3cCfgOperateTable": hh3cCfgOperateTable,
       "hh3cCfgOperateEntry": hh3cCfgOperateEntry,
       "hh3cCfgOperateIndex": hh3cCfgOperateIndex,
       "hh3cCfgOperateType": hh3cCfgOperateType,
       "hh3cCfgOperateProtocol": hh3cCfgOperateProtocol,
       "hh3cCfgOperateFileName": hh3cCfgOperateFileName,
       "hh3cCfgOperateServerAddress": hh3cCfgOperateServerAddress,
       "hh3cCfgOperateUserName": hh3cCfgOperateUserName,
       "hh3cCfgOperateUserPassword": hh3cCfgOperateUserPassword,
       "hh3cCfgOperateEndNotificationSwitch": hh3cCfgOperateEndNotificationSwitch,
       "hh3cCfgOperateRowStatus": hh3cCfgOperateRowStatus,
       "hh3cCfgOperateServerPort": hh3cCfgOperateServerPort,
       "hh3cCfgOperateSrvAddrType": hh3cCfgOperateSrvAddrType,
       "hh3cCfgOperateSrvAddrRev": hh3cCfgOperateSrvAddrRev,
       "hh3cCfgOperateSrvVPNName": hh3cCfgOperateSrvVPNName,
       "hh3cCfgOperateResultTable": hh3cCfgOperateResultTable,
       "hh3cCfgOperateResultEntry": hh3cCfgOperateResultEntry,
       "hh3cCfgOperateResultIndex": hh3cCfgOperateResultIndex,
       "hh3cCfgOperateResultOptIndex": hh3cCfgOperateResultOptIndex,
       "hh3cCfgOperateResultOpType": hh3cCfgOperateResultOpType,
       "hh3cCfgOperateState": hh3cCfgOperateState,
       "hh3cCfgOperateTime": hh3cCfgOperateTime,
       "hh3cCfgOperateEndTime": hh3cCfgOperateEndTime,
       "hh3cCfgOperFailReason": hh3cCfgOperFailReason,
       "hh3cCfgExecuteOperate": hh3cCfgExecuteOperate,
       "hh3cCfgExecuteOperateResultEntryLimit": hh3cCfgExecuteOperateResultEntryLimit,
       "hh3cCfgExecuteResultTable": hh3cCfgExecuteResultTable,
       "hh3cCfgExecuteResultEntry": hh3cCfgExecuteResultEntry,
       "hh3cCfgExecuteResultIndex": hh3cCfgExecuteResultIndex,
       "hh3cCfgExecuteResultOptIndex": hh3cCfgExecuteResultOptIndex,
       "hh3cCfgExecuteResultOpType": hh3cCfgExecuteResultOpType,
       "hh3cCfgExecuteState": hh3cCfgExecuteState,
       "hh3cCfgExecuteTime": hh3cCfgExecuteTime,
       "hh3cCfgExecuteEndTime": hh3cCfgExecuteEndTime,
       "hh3cCfgReset": hh3cCfgReset,
       "hh3cCfgReset2": hh3cCfgReset2,
       "hh3cConfigManNotifications": hh3cConfigManNotifications,
       "hh3cCfgManEventlog": hh3cCfgManEventlog,
       "hh3cCfgOperateCompletion": hh3cCfgOperateCompletion,
       "hh3cCfgInvalidConfigFile": hh3cCfgInvalidConfigFile,
       "hh3cConfigManConformance": hh3cConfigManConformance,
       "hh3cConfigManCompliances": hh3cConfigManCompliances,
       "hh3cConfigManCompliance": hh3cConfigManCompliance,
       "hh3cConfigManGroups": hh3cConfigManGroups,
       "hh3cCfgManLogGroup": hh3cCfgManLogGroup,
       "hh3cCfgOperateGroup": hh3cCfgOperateGroup,
       "hh3cCfgManNotificationGroup": hh3cCfgManNotificationGroup}
)

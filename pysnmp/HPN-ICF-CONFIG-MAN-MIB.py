# SNMP MIB module (HPN-ICF-CONFIG-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-CONFIG-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:36 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4)
)
hpnicfConfig.setRevisions(
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

_HpnicfConfigManObjects_ObjectIdentity = ObjectIdentity
hpnicfConfigManObjects = _HpnicfConfigManObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1)
)
_HpnicfCfgLog_ObjectIdentity = ObjectIdentity
hpnicfCfgLog = _HpnicfCfgLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1)
)
_HpnicfCfgRunModifiedLast_Type = TimeTicks
_HpnicfCfgRunModifiedLast_Object = MibScalar
hpnicfCfgRunModifiedLast = _HpnicfCfgRunModifiedLast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 1),
    _HpnicfCfgRunModifiedLast_Type()
)
hpnicfCfgRunModifiedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgRunModifiedLast.setStatus("current")
_HpnicfCfgRunSavedLast_Type = TimeTicks
_HpnicfCfgRunSavedLast_Object = MibScalar
hpnicfCfgRunSavedLast = _HpnicfCfgRunSavedLast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 2),
    _HpnicfCfgRunSavedLast_Type()
)
hpnicfCfgRunSavedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgRunSavedLast.setStatus("current")
_HpnicfCfgStartModifiedLast_Type = TimeTicks
_HpnicfCfgStartModifiedLast_Object = MibScalar
hpnicfCfgStartModifiedLast = _HpnicfCfgStartModifiedLast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 3),
    _HpnicfCfgStartModifiedLast_Type()
)
hpnicfCfgStartModifiedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgStartModifiedLast.setStatus("current")


class _HpnicfCfgLogLimitedEntries_Type(Integer32):
    """Custom type hpnicfCfgLogLimitedEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfCfgLogLimitedEntries_Type.__name__ = "Integer32"
_HpnicfCfgLogLimitedEntries_Object = MibScalar
hpnicfCfgLogLimitedEntries = _HpnicfCfgLogLimitedEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 4),
    _HpnicfCfgLogLimitedEntries_Type()
)
hpnicfCfgLogLimitedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogLimitedEntries.setStatus("current")
_HpnicfCfgLogDeletedEntries_Type = Counter32
_HpnicfCfgLogDeletedEntries_Object = MibScalar
hpnicfCfgLogDeletedEntries = _HpnicfCfgLogDeletedEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 5),
    _HpnicfCfgLogDeletedEntries_Type()
)
hpnicfCfgLogDeletedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogDeletedEntries.setStatus("current")


class _HpnicfCfgLogWantBackup_Type(TruthValue):
    """Custom type hpnicfCfgLogWantBackup based on TruthValue"""


_HpnicfCfgLogWantBackup_Object = MibScalar
hpnicfCfgLogWantBackup = _HpnicfCfgLogWantBackup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 6),
    _HpnicfCfgLogWantBackup_Type()
)
hpnicfCfgLogWantBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCfgLogWantBackup.setStatus("current")
_HpnicfCfgLogTable_Object = MibTable
hpnicfCfgLogTable = _HpnicfCfgLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfCfgLogTable.setStatus("current")
_HpnicfCfgLogEntry_Object = MibTableRow
hpnicfCfgLogEntry = _HpnicfCfgLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1)
)
hpnicfCfgLogEntry.setIndexNames(
    (0, "HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCfgLogEntry.setStatus("current")


class _HpnicfCfgLogIndex_Type(Integer32):
    """Custom type hpnicfCfgLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfCfgLogIndex_Type.__name__ = "Integer32"
_HpnicfCfgLogIndex_Object = MibTableColumn
hpnicfCfgLogIndex = _HpnicfCfgLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 1),
    _HpnicfCfgLogIndex_Type()
)
hpnicfCfgLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCfgLogIndex.setStatus("current")
_HpnicfCfgLogTime_Type = TimeTicks
_HpnicfCfgLogTime_Object = MibTableColumn
hpnicfCfgLogTime = _HpnicfCfgLogTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 2),
    _HpnicfCfgLogTime_Type()
)
hpnicfCfgLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogTime.setStatus("current")


class _HpnicfCfgLogSrcCmd_Type(Integer32):
    """Custom type hpnicfCfgLogSrcCmd based on Integer32"""
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


_HpnicfCfgLogSrcCmd_Type.__name__ = "Integer32"
_HpnicfCfgLogSrcCmd_Object = MibTableColumn
hpnicfCfgLogSrcCmd = _HpnicfCfgLogSrcCmd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 3),
    _HpnicfCfgLogSrcCmd_Type()
)
hpnicfCfgLogSrcCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogSrcCmd.setStatus("current")


class _HpnicfCfgLogSrcData_Type(Integer32):
    """Custom type hpnicfCfgLogSrcData based on Integer32"""
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


_HpnicfCfgLogSrcData_Type.__name__ = "Integer32"
_HpnicfCfgLogSrcData_Object = MibTableColumn
hpnicfCfgLogSrcData = _HpnicfCfgLogSrcData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 4),
    _HpnicfCfgLogSrcData_Type()
)
hpnicfCfgLogSrcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogSrcData.setStatus("current")


class _HpnicfCfgLogDesData_Type(Integer32):
    """Custom type hpnicfCfgLogDesData based on Integer32"""
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


_HpnicfCfgLogDesData_Type.__name__ = "Integer32"
_HpnicfCfgLogDesData_Object = MibTableColumn
hpnicfCfgLogDesData = _HpnicfCfgLogDesData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 5),
    _HpnicfCfgLogDesData_Type()
)
hpnicfCfgLogDesData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogDesData.setStatus("current")


class _HpnicfCfgLogTerminalType_Type(Integer32):
    """Custom type hpnicfCfgLogTerminalType based on Integer32"""
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


_HpnicfCfgLogTerminalType_Type.__name__ = "Integer32"
_HpnicfCfgLogTerminalType_Object = MibTableColumn
hpnicfCfgLogTerminalType = _HpnicfCfgLogTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 6),
    _HpnicfCfgLogTerminalType_Type()
)
hpnicfCfgLogTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogTerminalType.setStatus("current")


class _HpnicfCfgLogTerminalUser_Type(DisplayString):
    """Custom type hpnicfCfgLogTerminalUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfCfgLogTerminalUser_Type.__name__ = "DisplayString"
_HpnicfCfgLogTerminalUser_Object = MibTableColumn
hpnicfCfgLogTerminalUser = _HpnicfCfgLogTerminalUser_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 7),
    _HpnicfCfgLogTerminalUser_Type()
)
hpnicfCfgLogTerminalUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogTerminalUser.setStatus("current")
_HpnicfCfgLogTerminalNum_Type = Integer32
_HpnicfCfgLogTerminalNum_Object = MibTableColumn
hpnicfCfgLogTerminalNum = _HpnicfCfgLogTerminalNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 8),
    _HpnicfCfgLogTerminalNum_Type()
)
hpnicfCfgLogTerminalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogTerminalNum.setStatus("current")


class _HpnicfCfgLogTerminalLocation_Type(DisplayString):
    """Custom type hpnicfCfgLogTerminalLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfCfgLogTerminalLocation_Type.__name__ = "DisplayString"
_HpnicfCfgLogTerminalLocation_Object = MibTableColumn
hpnicfCfgLogTerminalLocation = _HpnicfCfgLogTerminalLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 9),
    _HpnicfCfgLogTerminalLocation_Type()
)
hpnicfCfgLogTerminalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogTerminalLocation.setStatus("current")
_HpnicfCfgLogCmdSrcAddress_Type = IpAddress
_HpnicfCfgLogCmdSrcAddress_Object = MibTableColumn
hpnicfCfgLogCmdSrcAddress = _HpnicfCfgLogCmdSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 10),
    _HpnicfCfgLogCmdSrcAddress_Type()
)
hpnicfCfgLogCmdSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogCmdSrcAddress.setStatus("deprecated")


class _HpnicfCfgLogVirHost_Type(DisplayString):
    """Custom type hpnicfCfgLogVirHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfCfgLogVirHost_Type.__name__ = "DisplayString"
_HpnicfCfgLogVirHost_Object = MibTableColumn
hpnicfCfgLogVirHost = _HpnicfCfgLogVirHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 11),
    _HpnicfCfgLogVirHost_Type()
)
hpnicfCfgLogVirHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogVirHost.setStatus("current")


class _HpnicfCfgLogUserName_Type(DisplayString):
    """Custom type hpnicfCfgLogUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfCfgLogUserName_Type.__name__ = "DisplayString"
_HpnicfCfgLogUserName_Object = MibTableColumn
hpnicfCfgLogUserName = _HpnicfCfgLogUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 12),
    _HpnicfCfgLogUserName_Type()
)
hpnicfCfgLogUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogUserName.setStatus("current")
_HpnicfCfgLogServerAddress_Type = IpAddress
_HpnicfCfgLogServerAddress_Object = MibTableColumn
hpnicfCfgLogServerAddress = _HpnicfCfgLogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 13),
    _HpnicfCfgLogServerAddress_Type()
)
hpnicfCfgLogServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogServerAddress.setStatus("deprecated")


class _HpnicfCfgLogFile_Type(DisplayString):
    """Custom type hpnicfCfgLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfCfgLogFile_Type.__name__ = "DisplayString"
_HpnicfCfgLogFile_Object = MibTableColumn
hpnicfCfgLogFile = _HpnicfCfgLogFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 14),
    _HpnicfCfgLogFile_Type()
)
hpnicfCfgLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogFile.setStatus("current")
_HpnicfCfgLogCmdSrcAddrType_Type = InetAddressType
_HpnicfCfgLogCmdSrcAddrType_Object = MibTableColumn
hpnicfCfgLogCmdSrcAddrType = _HpnicfCfgLogCmdSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 15),
    _HpnicfCfgLogCmdSrcAddrType_Type()
)
hpnicfCfgLogCmdSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogCmdSrcAddrType.setStatus("current")
_HpnicfCfgLogCmdSrcAddrRev_Type = InetAddress
_HpnicfCfgLogCmdSrcAddrRev_Object = MibTableColumn
hpnicfCfgLogCmdSrcAddrRev = _HpnicfCfgLogCmdSrcAddrRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 16),
    _HpnicfCfgLogCmdSrcAddrRev_Type()
)
hpnicfCfgLogCmdSrcAddrRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogCmdSrcAddrRev.setStatus("current")
_HpnicfCfgLogCmdSrcAddrVPNName_Type = DisplayString
_HpnicfCfgLogCmdSrcAddrVPNName_Object = MibTableColumn
hpnicfCfgLogCmdSrcAddrVPNName = _HpnicfCfgLogCmdSrcAddrVPNName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 17),
    _HpnicfCfgLogCmdSrcAddrVPNName_Type()
)
hpnicfCfgLogCmdSrcAddrVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogCmdSrcAddrVPNName.setStatus("current")
_HpnicfCfgLogServerAddrType_Type = InetAddressType
_HpnicfCfgLogServerAddrType_Object = MibTableColumn
hpnicfCfgLogServerAddrType = _HpnicfCfgLogServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 18),
    _HpnicfCfgLogServerAddrType_Type()
)
hpnicfCfgLogServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogServerAddrType.setStatus("current")
_HpnicfCfgLogServerAddrRev_Type = InetAddress
_HpnicfCfgLogServerAddrRev_Object = MibTableColumn
hpnicfCfgLogServerAddrRev = _HpnicfCfgLogServerAddrRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 19),
    _HpnicfCfgLogServerAddrRev_Type()
)
hpnicfCfgLogServerAddrRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogServerAddrRev.setStatus("current")
_HpnicfCfgLogServerAddrVPNName_Type = DisplayString
_HpnicfCfgLogServerAddrVPNName_Object = MibTableColumn
hpnicfCfgLogServerAddrVPNName = _HpnicfCfgLogServerAddrVPNName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 7, 1, 20),
    _HpnicfCfgLogServerAddrVPNName_Type()
)
hpnicfCfgLogServerAddrVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgLogServerAddrVPNName.setStatus("current")
_HpnicfCfgFirstTrapTime_Type = TimeTicks
_HpnicfCfgFirstTrapTime_Object = MibScalar
hpnicfCfgFirstTrapTime = _HpnicfCfgFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 1, 8),
    _HpnicfCfgFirstTrapTime_Type()
)
hpnicfCfgFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfCfgFirstTrapTime.setStatus("current")
_HpnicfCfgOperate_ObjectIdentity = ObjectIdentity
hpnicfCfgOperate = _HpnicfCfgOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2)
)


class _HpnicfCfgOperateGlobalEntryLimit_Type(Integer32):
    """Custom type hpnicfCfgOperateGlobalEntryLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpnicfCfgOperateGlobalEntryLimit_Type.__name__ = "Integer32"
_HpnicfCfgOperateGlobalEntryLimit_Object = MibScalar
hpnicfCfgOperateGlobalEntryLimit = _HpnicfCfgOperateGlobalEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 1),
    _HpnicfCfgOperateGlobalEntryLimit_Type()
)
hpnicfCfgOperateGlobalEntryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgOperateGlobalEntryLimit.setStatus("current")


class _HpnicfCfgOperateEntryAgeOutTime_Type(Integer32):
    """Custom type hpnicfCfgOperateEntryAgeOutTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HpnicfCfgOperateEntryAgeOutTime_Type.__name__ = "Integer32"
_HpnicfCfgOperateEntryAgeOutTime_Object = MibScalar
hpnicfCfgOperateEntryAgeOutTime = _HpnicfCfgOperateEntryAgeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 2),
    _HpnicfCfgOperateEntryAgeOutTime_Type()
)
hpnicfCfgOperateEntryAgeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCfgOperateEntryAgeOutTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfCfgOperateEntryAgeOutTime.setUnits("minute")


class _HpnicfCfgOperateResultGlobalEntryLimit_Type(Integer32):
    """Custom type hpnicfCfgOperateResultGlobalEntryLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_HpnicfCfgOperateResultGlobalEntryLimit_Type.__name__ = "Integer32"
_HpnicfCfgOperateResultGlobalEntryLimit_Object = MibScalar
hpnicfCfgOperateResultGlobalEntryLimit = _HpnicfCfgOperateResultGlobalEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 3),
    _HpnicfCfgOperateResultGlobalEntryLimit_Type()
)
hpnicfCfgOperateResultGlobalEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCfgOperateResultGlobalEntryLimit.setStatus("current")
_HpnicfCfgOperateTable_Object = MibTable
hpnicfCfgOperateTable = _HpnicfCfgOperateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfCfgOperateTable.setStatus("current")
_HpnicfCfgOperateEntry_Object = MibTableRow
hpnicfCfgOperateEntry = _HpnicfCfgOperateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1)
)
hpnicfCfgOperateEntry.setIndexNames(
    (0, "HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCfgOperateEntry.setStatus("current")


class _HpnicfCfgOperateIndex_Type(Integer32):
    """Custom type hpnicfCfgOperateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfCfgOperateIndex_Type.__name__ = "Integer32"
_HpnicfCfgOperateIndex_Object = MibTableColumn
hpnicfCfgOperateIndex = _HpnicfCfgOperateIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 1),
    _HpnicfCfgOperateIndex_Type()
)
hpnicfCfgOperateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCfgOperateIndex.setStatus("current")
_HpnicfCfgOperateType_Type = ConfigOperationType
_HpnicfCfgOperateType_Object = MibTableColumn
hpnicfCfgOperateType = _HpnicfCfgOperateType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 2),
    _HpnicfCfgOperateType_Type()
)
hpnicfCfgOperateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateType.setStatus("current")


class _HpnicfCfgOperateProtocol_Type(Integer32):
    """Custom type hpnicfCfgOperateProtocol based on Integer32"""
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


_HpnicfCfgOperateProtocol_Type.__name__ = "Integer32"
_HpnicfCfgOperateProtocol_Object = MibTableColumn
hpnicfCfgOperateProtocol = _HpnicfCfgOperateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 3),
    _HpnicfCfgOperateProtocol_Type()
)
hpnicfCfgOperateProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateProtocol.setStatus("current")


class _HpnicfCfgOperateFileName_Type(DisplayString):
    """Custom type hpnicfCfgOperateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfCfgOperateFileName_Type.__name__ = "DisplayString"
_HpnicfCfgOperateFileName_Object = MibTableColumn
hpnicfCfgOperateFileName = _HpnicfCfgOperateFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 4),
    _HpnicfCfgOperateFileName_Type()
)
hpnicfCfgOperateFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateFileName.setStatus("current")
_HpnicfCfgOperateServerAddress_Type = IpAddress
_HpnicfCfgOperateServerAddress_Object = MibTableColumn
hpnicfCfgOperateServerAddress = _HpnicfCfgOperateServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 5),
    _HpnicfCfgOperateServerAddress_Type()
)
hpnicfCfgOperateServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateServerAddress.setStatus("deprecated")


class _HpnicfCfgOperateUserName_Type(DisplayString):
    """Custom type hpnicfCfgOperateUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HpnicfCfgOperateUserName_Type.__name__ = "DisplayString"
_HpnicfCfgOperateUserName_Object = MibTableColumn
hpnicfCfgOperateUserName = _HpnicfCfgOperateUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 6),
    _HpnicfCfgOperateUserName_Type()
)
hpnicfCfgOperateUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateUserName.setStatus("current")


class _HpnicfCfgOperateUserPassword_Type(DisplayString):
    """Custom type hpnicfCfgOperateUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HpnicfCfgOperateUserPassword_Type.__name__ = "DisplayString"
_HpnicfCfgOperateUserPassword_Object = MibTableColumn
hpnicfCfgOperateUserPassword = _HpnicfCfgOperateUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 7),
    _HpnicfCfgOperateUserPassword_Type()
)
hpnicfCfgOperateUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateUserPassword.setStatus("current")


class _HpnicfCfgOperateEndNotificationSwitch_Type(TruthValue):
    """Custom type hpnicfCfgOperateEndNotificationSwitch based on TruthValue"""


_HpnicfCfgOperateEndNotificationSwitch_Object = MibTableColumn
hpnicfCfgOperateEndNotificationSwitch = _HpnicfCfgOperateEndNotificationSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 8),
    _HpnicfCfgOperateEndNotificationSwitch_Type()
)
hpnicfCfgOperateEndNotificationSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateEndNotificationSwitch.setStatus("current")
_HpnicfCfgOperateRowStatus_Type = RowStatus
_HpnicfCfgOperateRowStatus_Object = MibTableColumn
hpnicfCfgOperateRowStatus = _HpnicfCfgOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 9),
    _HpnicfCfgOperateRowStatus_Type()
)
hpnicfCfgOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateRowStatus.setStatus("current")


class _HpnicfCfgOperateServerPort_Type(Integer32):
    """Custom type hpnicfCfgOperateServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfCfgOperateServerPort_Type.__name__ = "Integer32"
_HpnicfCfgOperateServerPort_Object = MibTableColumn
hpnicfCfgOperateServerPort = _HpnicfCfgOperateServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 10),
    _HpnicfCfgOperateServerPort_Type()
)
hpnicfCfgOperateServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateServerPort.setStatus("current")
_HpnicfCfgOperateSrvAddrType_Type = InetAddressType
_HpnicfCfgOperateSrvAddrType_Object = MibTableColumn
hpnicfCfgOperateSrvAddrType = _HpnicfCfgOperateSrvAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 11),
    _HpnicfCfgOperateSrvAddrType_Type()
)
hpnicfCfgOperateSrvAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateSrvAddrType.setStatus("current")
_HpnicfCfgOperateSrvAddrRev_Type = InetAddress
_HpnicfCfgOperateSrvAddrRev_Object = MibTableColumn
hpnicfCfgOperateSrvAddrRev = _HpnicfCfgOperateSrvAddrRev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 12),
    _HpnicfCfgOperateSrvAddrRev_Type()
)
hpnicfCfgOperateSrvAddrRev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateSrvAddrRev.setStatus("current")
_HpnicfCfgOperateSrvVPNName_Type = DisplayString
_HpnicfCfgOperateSrvVPNName_Object = MibTableColumn
hpnicfCfgOperateSrvVPNName = _HpnicfCfgOperateSrvVPNName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 4, 1, 13),
    _HpnicfCfgOperateSrvVPNName_Type()
)
hpnicfCfgOperateSrvVPNName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfCfgOperateSrvVPNName.setStatus("current")
_HpnicfCfgOperateResultTable_Object = MibTable
hpnicfCfgOperateResultTable = _HpnicfCfgOperateResultTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfCfgOperateResultTable.setStatus("current")
_HpnicfCfgOperateResultEntry_Object = MibTableRow
hpnicfCfgOperateResultEntry = _HpnicfCfgOperateResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 5, 1)
)
hpnicfCfgOperateResultEntry.setIndexNames(
    (0, "HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateResultIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCfgOperateResultEntry.setStatus("current")


class _HpnicfCfgOperateResultIndex_Type(Integer32):
    """Custom type hpnicfCfgOperateResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfCfgOperateResultIndex_Type.__name__ = "Integer32"
_HpnicfCfgOperateResultIndex_Object = MibTableColumn
hpnicfCfgOperateResultIndex = _HpnicfCfgOperateResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 5, 1, 1),
    _HpnicfCfgOperateResultIndex_Type()
)
hpnicfCfgOperateResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCfgOperateResultIndex.setStatus("current")


class _HpnicfCfgOperateResultOptIndex_Type(Integer32):
    """Custom type hpnicfCfgOperateResultOptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfCfgOperateResultOptIndex_Type.__name__ = "Integer32"
_HpnicfCfgOperateResultOptIndex_Object = MibTableColumn
hpnicfCfgOperateResultOptIndex = _HpnicfCfgOperateResultOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 5, 1, 2),
    _HpnicfCfgOperateResultOptIndex_Type()
)
hpnicfCfgOperateResultOptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgOperateResultOptIndex.setStatus("current")
_HpnicfCfgOperateResultOpType_Type = ConfigOperationType
_HpnicfCfgOperateResultOpType_Object = MibTableColumn
hpnicfCfgOperateResultOpType = _HpnicfCfgOperateResultOpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 5, 1, 3),
    _HpnicfCfgOperateResultOpType_Type()
)
hpnicfCfgOperateResultOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgOperateResultOpType.setStatus("current")
_HpnicfCfgOperateState_Type = ConfigOperationStateType
_HpnicfCfgOperateState_Object = MibTableColumn
hpnicfCfgOperateState = _HpnicfCfgOperateState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 5, 1, 4),
    _HpnicfCfgOperateState_Type()
)
hpnicfCfgOperateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgOperateState.setStatus("current")
_HpnicfCfgOperateTime_Type = TimeTicks
_HpnicfCfgOperateTime_Object = MibTableColumn
hpnicfCfgOperateTime = _HpnicfCfgOperateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 5, 1, 5),
    _HpnicfCfgOperateTime_Type()
)
hpnicfCfgOperateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgOperateTime.setStatus("current")
_HpnicfCfgOperateEndTime_Type = TimeTicks
_HpnicfCfgOperateEndTime_Object = MibTableColumn
hpnicfCfgOperateEndTime = _HpnicfCfgOperateEndTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 5, 1, 6),
    _HpnicfCfgOperateEndTime_Type()
)
hpnicfCfgOperateEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgOperateEndTime.setStatus("current")
_HpnicfCfgOperFailReason_Type = DisplayString
_HpnicfCfgOperFailReason_Object = MibTableColumn
hpnicfCfgOperFailReason = _HpnicfCfgOperFailReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 5, 1, 7),
    _HpnicfCfgOperFailReason_Type()
)
hpnicfCfgOperFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgOperFailReason.setStatus("current")
_HpnicfCfgExecuteOperate_ObjectIdentity = ObjectIdentity
hpnicfCfgExecuteOperate = _HpnicfCfgExecuteOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 6)
)


class _HpnicfCfgExecuteOperateResultEntryLimit_Type(Integer32):
    """Custom type hpnicfCfgExecuteOperateResultEntryLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_HpnicfCfgExecuteOperateResultEntryLimit_Type.__name__ = "Integer32"
_HpnicfCfgExecuteOperateResultEntryLimit_Object = MibScalar
hpnicfCfgExecuteOperateResultEntryLimit = _HpnicfCfgExecuteOperateResultEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 6, 1),
    _HpnicfCfgExecuteOperateResultEntryLimit_Type()
)
hpnicfCfgExecuteOperateResultEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCfgExecuteOperateResultEntryLimit.setStatus("current")
_HpnicfCfgExecuteResultTable_Object = MibTable
hpnicfCfgExecuteResultTable = _HpnicfCfgExecuteResultTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    hpnicfCfgExecuteResultTable.setStatus("current")
_HpnicfCfgExecuteResultEntry_Object = MibTableRow
hpnicfCfgExecuteResultEntry = _HpnicfCfgExecuteResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 6, 2, 1)
)
hpnicfCfgExecuteResultEntry.setIndexNames(
    (0, "HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgExecuteResultIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCfgExecuteResultEntry.setStatus("current")


class _HpnicfCfgExecuteResultIndex_Type(Integer32):
    """Custom type hpnicfCfgExecuteResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfCfgExecuteResultIndex_Type.__name__ = "Integer32"
_HpnicfCfgExecuteResultIndex_Object = MibTableColumn
hpnicfCfgExecuteResultIndex = _HpnicfCfgExecuteResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 6, 2, 1, 1),
    _HpnicfCfgExecuteResultIndex_Type()
)
hpnicfCfgExecuteResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCfgExecuteResultIndex.setStatus("current")


class _HpnicfCfgExecuteResultOptIndex_Type(Integer32):
    """Custom type hpnicfCfgExecuteResultOptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfCfgExecuteResultOptIndex_Type.__name__ = "Integer32"
_HpnicfCfgExecuteResultOptIndex_Object = MibTableColumn
hpnicfCfgExecuteResultOptIndex = _HpnicfCfgExecuteResultOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 6, 2, 1, 2),
    _HpnicfCfgExecuteResultOptIndex_Type()
)
hpnicfCfgExecuteResultOptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgExecuteResultOptIndex.setStatus("current")
_HpnicfCfgExecuteResultOpType_Type = ConfigOperationType
_HpnicfCfgExecuteResultOpType_Object = MibTableColumn
hpnicfCfgExecuteResultOpType = _HpnicfCfgExecuteResultOpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 6, 2, 1, 3),
    _HpnicfCfgExecuteResultOpType_Type()
)
hpnicfCfgExecuteResultOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgExecuteResultOpType.setStatus("current")
_HpnicfCfgExecuteState_Type = ConfigOperationStateType
_HpnicfCfgExecuteState_Object = MibTableColumn
hpnicfCfgExecuteState = _HpnicfCfgExecuteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 6, 2, 1, 4),
    _HpnicfCfgExecuteState_Type()
)
hpnicfCfgExecuteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgExecuteState.setStatus("current")
_HpnicfCfgExecuteTime_Type = TimeTicks
_HpnicfCfgExecuteTime_Object = MibTableColumn
hpnicfCfgExecuteTime = _HpnicfCfgExecuteTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 6, 2, 1, 5),
    _HpnicfCfgExecuteTime_Type()
)
hpnicfCfgExecuteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgExecuteTime.setStatus("current")
_HpnicfCfgExecuteEndTime_Type = TimeTicks
_HpnicfCfgExecuteEndTime_Object = MibTableColumn
hpnicfCfgExecuteEndTime = _HpnicfCfgExecuteEndTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 6, 2, 1, 6),
    _HpnicfCfgExecuteEndTime_Type()
)
hpnicfCfgExecuteEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfgExecuteEndTime.setStatus("current")


class _HpnicfCfgReset_Type(Integer32):
    """Custom type hpnicfCfgReset based on Integer32"""
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


_HpnicfCfgReset_Type.__name__ = "Integer32"
_HpnicfCfgReset_Object = MibScalar
hpnicfCfgReset = _HpnicfCfgReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 7),
    _HpnicfCfgReset_Type()
)
hpnicfCfgReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCfgReset.setStatus("current")


class _HpnicfCfgReset2_Type(Integer32):
    """Custom type hpnicfCfgReset2 based on Integer32"""
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


_HpnicfCfgReset2_Type.__name__ = "Integer32"
_HpnicfCfgReset2_Object = MibScalar
hpnicfCfgReset2 = _HpnicfCfgReset2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 1, 2, 8),
    _HpnicfCfgReset2_Type()
)
hpnicfCfgReset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCfgReset2.setStatus("current")
_HpnicfConfigManNotifications_ObjectIdentity = ObjectIdentity
hpnicfConfigManNotifications = _HpnicfConfigManNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 2)
)
_HpnicfConfigManConformance_ObjectIdentity = ObjectIdentity
hpnicfConfigManConformance = _HpnicfConfigManConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 3)
)
_HpnicfConfigManCompliances_ObjectIdentity = ObjectIdentity
hpnicfConfigManCompliances = _HpnicfConfigManCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 3, 1)
)
_HpnicfConfigManGroups_ObjectIdentity = ObjectIdentity
hpnicfConfigManGroups = _HpnicfConfigManGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 3, 2)
)

# Managed Objects groups

hpnicfCfgManLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 3, 2, 1)
)
hpnicfCfgManLogGroup.setObjects(
      *(("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgRunModifiedLast"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgRunSavedLast"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgStartModifiedLast"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogLimitedEntries"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogDeletedEntries"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogTime"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogSrcCmd"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogTerminalType"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogTerminalNum"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogTerminalUser"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogTerminalLocation"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogCmdSrcAddress"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogVirHost"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogServerAddress"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogFile"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogUserName"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogWantBackup"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogSrcData"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogDesData"))
)
if mibBuilder.loadTexts:
    hpnicfCfgManLogGroup.setStatus("current")

hpnicfCfgOperateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 3, 2, 2)
)
hpnicfCfgOperateGroup.setObjects(
      *(("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateGlobalEntryLimit"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateEntryAgeOutTime"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateType"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateProtocol"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateFileName"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateServerAddress"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateUserName"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateUserPassword"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateTime"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateEndNotificationSwitch"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateResultGlobalEntryLimit"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateState"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateRowStatus"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateResultOptIndex"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateResultOpType"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateEndTime"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperFailReason"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateServerPort"))
)
if mibBuilder.loadTexts:
    hpnicfCfgOperateGroup.setStatus("current")


# Notification objects

hpnicfCfgManEventlog = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 2, 1)
)
hpnicfCfgManEventlog.setObjects(
      *(("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogSrcCmd"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogSrcData"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgLogDesData"))
)
if mibBuilder.loadTexts:
    hpnicfCfgManEventlog.setStatus(
        "current"
    )

hpnicfCfgOperateCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 2, 2)
)
hpnicfCfgOperateCompletion.setObjects(
      *(("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateType"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateTime"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateState"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateEndTime"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperFailReason"))
)
if mibBuilder.loadTexts:
    hpnicfCfgOperateCompletion.setStatus(
        "current"
    )

hpnicfCfgInvalidConfigFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 2, 3)
)
hpnicfCfgInvalidConfigFile.setObjects(
      *(("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateType"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateFileName"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfCfgInvalidConfigFile.setStatus(
        "current"
    )


# Notifications groups

hpnicfCfgManNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 3, 2, 3)
)
hpnicfCfgManNotificationGroup.setObjects(
      *(("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgManEventlog"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgOperateCompletion"),
        ("HPN-ICF-CONFIG-MAN-MIB", "hpnicfCfgInvalidConfigFile"))
)
if mibBuilder.loadTexts:
    hpnicfCfgManNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfConfigManCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfConfigManCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-CONFIG-MAN-MIB",
    **{"ConfigOperationType": ConfigOperationType,
       "ConfigOperationStateType": ConfigOperationStateType,
       "hpnicfConfig": hpnicfConfig,
       "hpnicfConfigManObjects": hpnicfConfigManObjects,
       "hpnicfCfgLog": hpnicfCfgLog,
       "hpnicfCfgRunModifiedLast": hpnicfCfgRunModifiedLast,
       "hpnicfCfgRunSavedLast": hpnicfCfgRunSavedLast,
       "hpnicfCfgStartModifiedLast": hpnicfCfgStartModifiedLast,
       "hpnicfCfgLogLimitedEntries": hpnicfCfgLogLimitedEntries,
       "hpnicfCfgLogDeletedEntries": hpnicfCfgLogDeletedEntries,
       "hpnicfCfgLogWantBackup": hpnicfCfgLogWantBackup,
       "hpnicfCfgLogTable": hpnicfCfgLogTable,
       "hpnicfCfgLogEntry": hpnicfCfgLogEntry,
       "hpnicfCfgLogIndex": hpnicfCfgLogIndex,
       "hpnicfCfgLogTime": hpnicfCfgLogTime,
       "hpnicfCfgLogSrcCmd": hpnicfCfgLogSrcCmd,
       "hpnicfCfgLogSrcData": hpnicfCfgLogSrcData,
       "hpnicfCfgLogDesData": hpnicfCfgLogDesData,
       "hpnicfCfgLogTerminalType": hpnicfCfgLogTerminalType,
       "hpnicfCfgLogTerminalUser": hpnicfCfgLogTerminalUser,
       "hpnicfCfgLogTerminalNum": hpnicfCfgLogTerminalNum,
       "hpnicfCfgLogTerminalLocation": hpnicfCfgLogTerminalLocation,
       "hpnicfCfgLogCmdSrcAddress": hpnicfCfgLogCmdSrcAddress,
       "hpnicfCfgLogVirHost": hpnicfCfgLogVirHost,
       "hpnicfCfgLogUserName": hpnicfCfgLogUserName,
       "hpnicfCfgLogServerAddress": hpnicfCfgLogServerAddress,
       "hpnicfCfgLogFile": hpnicfCfgLogFile,
       "hpnicfCfgLogCmdSrcAddrType": hpnicfCfgLogCmdSrcAddrType,
       "hpnicfCfgLogCmdSrcAddrRev": hpnicfCfgLogCmdSrcAddrRev,
       "hpnicfCfgLogCmdSrcAddrVPNName": hpnicfCfgLogCmdSrcAddrVPNName,
       "hpnicfCfgLogServerAddrType": hpnicfCfgLogServerAddrType,
       "hpnicfCfgLogServerAddrRev": hpnicfCfgLogServerAddrRev,
       "hpnicfCfgLogServerAddrVPNName": hpnicfCfgLogServerAddrVPNName,
       "hpnicfCfgFirstTrapTime": hpnicfCfgFirstTrapTime,
       "hpnicfCfgOperate": hpnicfCfgOperate,
       "hpnicfCfgOperateGlobalEntryLimit": hpnicfCfgOperateGlobalEntryLimit,
       "hpnicfCfgOperateEntryAgeOutTime": hpnicfCfgOperateEntryAgeOutTime,
       "hpnicfCfgOperateResultGlobalEntryLimit": hpnicfCfgOperateResultGlobalEntryLimit,
       "hpnicfCfgOperateTable": hpnicfCfgOperateTable,
       "hpnicfCfgOperateEntry": hpnicfCfgOperateEntry,
       "hpnicfCfgOperateIndex": hpnicfCfgOperateIndex,
       "hpnicfCfgOperateType": hpnicfCfgOperateType,
       "hpnicfCfgOperateProtocol": hpnicfCfgOperateProtocol,
       "hpnicfCfgOperateFileName": hpnicfCfgOperateFileName,
       "hpnicfCfgOperateServerAddress": hpnicfCfgOperateServerAddress,
       "hpnicfCfgOperateUserName": hpnicfCfgOperateUserName,
       "hpnicfCfgOperateUserPassword": hpnicfCfgOperateUserPassword,
       "hpnicfCfgOperateEndNotificationSwitch": hpnicfCfgOperateEndNotificationSwitch,
       "hpnicfCfgOperateRowStatus": hpnicfCfgOperateRowStatus,
       "hpnicfCfgOperateServerPort": hpnicfCfgOperateServerPort,
       "hpnicfCfgOperateSrvAddrType": hpnicfCfgOperateSrvAddrType,
       "hpnicfCfgOperateSrvAddrRev": hpnicfCfgOperateSrvAddrRev,
       "hpnicfCfgOperateSrvVPNName": hpnicfCfgOperateSrvVPNName,
       "hpnicfCfgOperateResultTable": hpnicfCfgOperateResultTable,
       "hpnicfCfgOperateResultEntry": hpnicfCfgOperateResultEntry,
       "hpnicfCfgOperateResultIndex": hpnicfCfgOperateResultIndex,
       "hpnicfCfgOperateResultOptIndex": hpnicfCfgOperateResultOptIndex,
       "hpnicfCfgOperateResultOpType": hpnicfCfgOperateResultOpType,
       "hpnicfCfgOperateState": hpnicfCfgOperateState,
       "hpnicfCfgOperateTime": hpnicfCfgOperateTime,
       "hpnicfCfgOperateEndTime": hpnicfCfgOperateEndTime,
       "hpnicfCfgOperFailReason": hpnicfCfgOperFailReason,
       "hpnicfCfgExecuteOperate": hpnicfCfgExecuteOperate,
       "hpnicfCfgExecuteOperateResultEntryLimit": hpnicfCfgExecuteOperateResultEntryLimit,
       "hpnicfCfgExecuteResultTable": hpnicfCfgExecuteResultTable,
       "hpnicfCfgExecuteResultEntry": hpnicfCfgExecuteResultEntry,
       "hpnicfCfgExecuteResultIndex": hpnicfCfgExecuteResultIndex,
       "hpnicfCfgExecuteResultOptIndex": hpnicfCfgExecuteResultOptIndex,
       "hpnicfCfgExecuteResultOpType": hpnicfCfgExecuteResultOpType,
       "hpnicfCfgExecuteState": hpnicfCfgExecuteState,
       "hpnicfCfgExecuteTime": hpnicfCfgExecuteTime,
       "hpnicfCfgExecuteEndTime": hpnicfCfgExecuteEndTime,
       "hpnicfCfgReset": hpnicfCfgReset,
       "hpnicfCfgReset2": hpnicfCfgReset2,
       "hpnicfConfigManNotifications": hpnicfConfigManNotifications,
       "hpnicfCfgManEventlog": hpnicfCfgManEventlog,
       "hpnicfCfgOperateCompletion": hpnicfCfgOperateCompletion,
       "hpnicfCfgInvalidConfigFile": hpnicfCfgInvalidConfigFile,
       "hpnicfConfigManConformance": hpnicfConfigManConformance,
       "hpnicfConfigManCompliances": hpnicfConfigManCompliances,
       "hpnicfConfigManCompliance": hpnicfConfigManCompliance,
       "hpnicfConfigManGroups": hpnicfConfigManGroups,
       "hpnicfCfgManLogGroup": hpnicfCfgManLogGroup,
       "hpnicfCfgOperateGroup": hpnicfCfgOperateGroup,
       "hpnicfCfgManNotificationGroup": hpnicfCfgManNotificationGroup}
)

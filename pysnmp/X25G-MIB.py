# SNMP MIB module (X25G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/X25G-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:38 2024
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
 enterprises,
 experimental,
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
    "enterprises",
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_X25g_ObjectIdentity = ObjectIdentity
x25g = _X25g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 11)
)
_X25gwId_ObjectIdentity = ObjectIdentity
x25gwId = _X25gwId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1)
)
_X25gwIdTable_Object = MibTable
x25gwIdTable = _X25gwIdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    x25gwIdTable.setStatus("mandatory")
_X25gwIdEntry_Object = MibTableRow
x25gwIdEntry = _X25gwIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1, 1)
)
x25gwIdEntry.setIndexNames(
    (0, "X25G-MIB", "x25gwIdIndex"),
)
if mibBuilder.loadTexts:
    x25gwIdEntry.setStatus("mandatory")
_X25gwIdIndex_Type = Integer32
_X25gwIdIndex_Object = MibTableColumn
x25gwIdIndex = _X25gwIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1, 1, 1),
    _X25gwIdIndex_Type()
)
x25gwIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwIdIndex.setStatus("mandatory")
_X25gwIdHardwareSerNum_Type = DisplayString
_X25gwIdHardwareSerNum_Object = MibTableColumn
x25gwIdHardwareSerNum = _X25gwIdHardwareSerNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1, 1, 2),
    _X25gwIdHardwareSerNum_Type()
)
x25gwIdHardwareSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwIdHardwareSerNum.setStatus("mandatory")
_X25gwIdHardwareRev_Type = DisplayString
_X25gwIdHardwareRev_Object = MibTableColumn
x25gwIdHardwareRev = _X25gwIdHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1, 1, 3),
    _X25gwIdHardwareRev_Type()
)
x25gwIdHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwIdHardwareRev.setStatus("mandatory")
_X25gwIdSoftwareRev_Type = DisplayString
_X25gwIdSoftwareRev_Object = MibTableColumn
x25gwIdSoftwareRev = _X25gwIdSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1, 1, 4),
    _X25gwIdSoftwareRev_Type()
)
x25gwIdSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwIdSoftwareRev.setStatus("mandatory")


class _X25gwIdCpuType_Type(Integer32):
    """Custom type x25gwIdCpuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("i80386", 1),
          ("i80486", 2))
    )


_X25gwIdCpuType_Type.__name__ = "Integer32"
_X25gwIdCpuType_Object = MibTableColumn
x25gwIdCpuType = _X25gwIdCpuType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1, 1, 5),
    _X25gwIdCpuType_Type()
)
x25gwIdCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwIdCpuType.setStatus("mandatory")
_X25gwIdRamInstalled_Type = Integer32
_X25gwIdRamInstalled_Object = MibTableColumn
x25gwIdRamInstalled = _X25gwIdRamInstalled_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1, 1, 6),
    _X25gwIdRamInstalled_Type()
)
x25gwIdRamInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwIdRamInstalled.setStatus("mandatory")
_X25gwIdFlashInstalled_Type = Integer32
_X25gwIdFlashInstalled_Object = MibTableColumn
x25gwIdFlashInstalled = _X25gwIdFlashInstalled_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1, 1, 7),
    _X25gwIdFlashInstalled_Type()
)
x25gwIdFlashInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwIdFlashInstalled.setStatus("mandatory")


class _X25gwIdOperCfgSts_Type(Integer32):
    """Custom type x25gwIdOperCfgSts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminChanged", 2),
          ("adminNvram", 3),
          ("operNvram", 1))
    )


_X25gwIdOperCfgSts_Type.__name__ = "Integer32"
_X25gwIdOperCfgSts_Object = MibTableColumn
x25gwIdOperCfgSts = _X25gwIdOperCfgSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1, 1, 8),
    _X25gwIdOperCfgSts_Type()
)
x25gwIdOperCfgSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwIdOperCfgSts.setStatus("mandatory")
_X25gwIdSelfTestResult_Type = Integer32
_X25gwIdSelfTestResult_Object = MibTableColumn
x25gwIdSelfTestResult = _X25gwIdSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1, 1, 9),
    _X25gwIdSelfTestResult_Type()
)
x25gwIdSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwIdSelfTestResult.setStatus("mandatory")


class _X25gwIdMgmtConnect_Type(Integer32):
    """Custom type x25gwIdMgmtConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_X25gwIdMgmtConnect_Type.__name__ = "Integer32"
_X25gwIdMgmtConnect_Object = MibTableColumn
x25gwIdMgmtConnect = _X25gwIdMgmtConnect_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 1, 1, 1, 10),
    _X25gwIdMgmtConnect_Type()
)
x25gwIdMgmtConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwIdMgmtConnect.setStatus("mandatory")
_X25gwCmd_ObjectIdentity = ObjectIdentity
x25gwCmd = _X25gwCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 2)
)
_X25gwCmdTable_Object = MibTable
x25gwCmdTable = _X25gwCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    x25gwCmdTable.setStatus("mandatory")
_X25gwCmdEntry_Object = MibTableRow
x25gwCmdEntry = _X25gwCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 2, 1, 1)
)
x25gwCmdEntry.setIndexNames(
    (0, "X25G-MIB", "x25gwCmdIndex"),
)
if mibBuilder.loadTexts:
    x25gwCmdEntry.setStatus("mandatory")
_X25gwCmdIndex_Type = Integer32
_X25gwCmdIndex_Object = MibTableColumn
x25gwCmdIndex = _X25gwCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 2, 1, 1, 1),
    _X25gwCmdIndex_Type()
)
x25gwCmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwCmdIndex.setStatus("mandatory")


class _X25gwCmdMgtStationId_Type(OctetString):
    """Custom type x25gwCmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_X25gwCmdMgtStationId_Type.__name__ = "OctetString"
_X25gwCmdMgtStationId_Object = MibTableColumn
x25gwCmdMgtStationId = _X25gwCmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 2, 1, 1, 2),
    _X25gwCmdMgtStationId_Type()
)
x25gwCmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25gwCmdMgtStationId.setStatus("mandatory")
_X25gwCmdReqId_Type = Integer32
_X25gwCmdReqId_Object = MibTableColumn
x25gwCmdReqId = _X25gwCmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 2, 1, 1, 3),
    _X25gwCmdReqId_Type()
)
x25gwCmdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwCmdReqId.setStatus("mandatory")


class _X25gwCmdFunction_Type(Integer32):
    """Custom type x25gwCmdFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disruptSelfTest", 6),
          ("downloadCfgFile", 8),
          ("noCommand", 1),
          ("nonDisruptSelfTest", 5),
          ("restoreFromDefault", 4),
          ("saveToNVRAM", 2),
          ("softwareReset", 7),
          ("uploadCfgFile", 9))
    )


_X25gwCmdFunction_Type.__name__ = "Integer32"
_X25gwCmdFunction_Object = MibTableColumn
x25gwCmdFunction = _X25gwCmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 2, 1, 1, 4),
    _X25gwCmdFunction_Type()
)
x25gwCmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25gwCmdFunction.setStatus("mandatory")
_X25gwCmdForce_Type = Integer32
_X25gwCmdForce_Object = MibTableColumn
x25gwCmdForce = _X25gwCmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 2, 1, 1, 5),
    _X25gwCmdForce_Type()
)
x25gwCmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25gwCmdForce.setStatus("mandatory")
_X25gwCmdParam_Type = OctetString
_X25gwCmdParam_Object = MibTableColumn
x25gwCmdParam = _X25gwCmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 2, 1, 1, 6),
    _X25gwCmdParam_Type()
)
x25gwCmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25gwCmdParam.setStatus("mandatory")


class _X25gwCmdResult_Type(Integer32):
    """Custom type x25gwCmdResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_X25gwCmdResult_Type.__name__ = "Integer32"
_X25gwCmdResult_Object = MibTableColumn
x25gwCmdResult = _X25gwCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 2, 1, 1, 7),
    _X25gwCmdResult_Type()
)
x25gwCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwCmdResult.setStatus("mandatory")


class _X25gwCmdCode_Type(Integer32):
    """Custom type x25gwCmdCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8,
              12,
              20,
              22,
              46,
              58,
              61,
              62,
              63,
              64,
              65,
              66,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              84,
              85,
              86,
              87,
              88,
              93)
        )
    )
    namedValues = NamedValues(
        *(("badFlashRomID", 61),
          ("badFlashVoltage", 62),
          ("badProgramVoltage", 68),
          ("bulkTransferInProcess", 93),
          ("cardIdMismatch", 84),
          ("cardIdUnknown", 85),
          ("deviceDisabled", 22),
          ("eraseExecutionError", 65),
          ("eraseSequenceError", 64),
          ("fileTooBig", 46),
          ("flashEraseError", 63),
          ("flashEraseTimeout", 87),
          ("invalidCodeError", 71),
          ("invalidFileHeader", 88),
          ("invalidRomId", 75),
          ("noError", 1),
          ("noResponse", 12),
          ("pendingSoftwareDownload", 73),
          ("programCodeError", 70),
          ("programmingDataError", 69),
          ("ramCrcBad", 74),
          ("receiveBufferOverflow", 66),
          ("romCrcBad", 72),
          ("slotEmpty", 8),
          ("tftpTimeout", 86),
          ("unable", 2),
          ("unrecognizedCommand", 6),
          ("unsupportedCommand", 20),
          ("userInterfaceActive", 58))
    )


_X25gwCmdCode_Type.__name__ = "Integer32"
_X25gwCmdCode_Object = MibTableColumn
x25gwCmdCode = _X25gwCmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 2, 1, 1, 8),
    _X25gwCmdCode_Type()
)
x25gwCmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwCmdCode.setStatus("mandatory")
_X25gwCfg_ObjectIdentity = ObjectIdentity
x25gwCfg = _X25gwCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 3)
)
_X25gwCfgTable_Object = MibTable
x25gwCfgTable = _X25gwCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    x25gwCfgTable.setStatus("mandatory")
_X25gwCfgEntry_Object = MibTableRow
x25gwCfgEntry = _X25gwCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 3, 1, 1)
)
x25gwCfgEntry.setIndexNames(
    (0, "X25G-MIB", "x25gwCfgIndex"),
)
if mibBuilder.loadTexts:
    x25gwCfgEntry.setStatus("mandatory")
_X25gwCfgIndex_Type = Integer32
_X25gwCfgIndex_Object = MibTableColumn
x25gwCfgIndex = _X25gwCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 3, 1, 1, 1),
    _X25gwCfgIndex_Type()
)
x25gwCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwCfgIndex.setStatus("mandatory")


class _X25gwCfgUiPort_Type(Integer32):
    """Custom type x25gwCfgUiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("padAccess", 2))
    )


_X25gwCfgUiPort_Type.__name__ = "Integer32"
_X25gwCfgUiPort_Object = MibTableColumn
x25gwCfgUiPort = _X25gwCfgUiPort_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 3, 1, 1, 2),
    _X25gwCfgUiPort_Type()
)
x25gwCfgUiPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwCfgUiPort.setStatus("mandatory")


class _X25gwCfgLocModemConn_Type(Integer32):
    """Custom type x25gwCfgLocModemConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dial", 2),
          ("direct", 1))
    )


_X25gwCfgLocModemConn_Type.__name__ = "Integer32"
_X25gwCfgLocModemConn_Object = MibTableColumn
x25gwCfgLocModemConn = _X25gwCfgLocModemConn_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 3, 1, 1, 3),
    _X25gwCfgLocModemConn_Type()
)
x25gwCfgLocModemConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25gwCfgLocModemConn.setStatus("mandatory")


class _X25gwCfgRoutingType_Type(Integer32):
    """Custom type x25gwCfgRoutingType based on Integer32"""
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
        *(("both", 4),
          ("callUserData", 3),
          ("managmentOnly", 5),
          ("none", 1),
          ("subAddr", 2))
    )


_X25gwCfgRoutingType_Type.__name__ = "Integer32"
_X25gwCfgRoutingType_Object = MibTableColumn
x25gwCfgRoutingType = _X25gwCfgRoutingType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 3, 1, 1, 4),
    _X25gwCfgRoutingType_Type()
)
x25gwCfgRoutingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25gwCfgRoutingType.setStatus("mandatory")


class _X25gwCfgCudRoutStr_Type(DisplayString):
    """Custom type x25gwCfgCudRoutStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_X25gwCfgCudRoutStr_Type.__name__ = "DisplayString"
_X25gwCfgCudRoutStr_Object = MibTableColumn
x25gwCfgCudRoutStr = _X25gwCfgCudRoutStr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 3, 1, 1, 5),
    _X25gwCfgCudRoutStr_Type()
)
x25gwCfgCudRoutStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25gwCfgCudRoutStr.setStatus("mandatory")


class _X25gwCfgX121SubAddr_Type(Integer32):
    """Custom type x25gwCfgX121SubAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_X25gwCfgX121SubAddr_Type.__name__ = "Integer32"
_X25gwCfgX121SubAddr_Object = MibTableColumn
x25gwCfgX121SubAddr = _X25gwCfgX121SubAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 3, 1, 1, 6),
    _X25gwCfgX121SubAddr_Type()
)
x25gwCfgX121SubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25gwCfgX121SubAddr.setStatus("mandatory")


class _X25gwCfgSysDate_Type(DisplayString):
    """Custom type x25gwCfgSysDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 8),
    )


_X25gwCfgSysDate_Type.__name__ = "DisplayString"
_X25gwCfgSysDate_Object = MibTableColumn
x25gwCfgSysDate = _X25gwCfgSysDate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 3, 1, 1, 7),
    _X25gwCfgSysDate_Type()
)
x25gwCfgSysDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25gwCfgSysDate.setStatus("mandatory")


class _X25gwCfgSysTime_Type(DisplayString):
    """Custom type x25gwCfgSysTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 8),
    )


_X25gwCfgSysTime_Type.__name__ = "DisplayString"
_X25gwCfgSysTime_Object = MibTableColumn
x25gwCfgSysTime = _X25gwCfgSysTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 3, 1, 1, 8),
    _X25gwCfgSysTime_Type()
)
x25gwCfgSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25gwCfgSysTime.setStatus("mandatory")
_X25gwTrapEna_ObjectIdentity = ObjectIdentity
x25gwTrapEna = _X25gwTrapEna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 4)
)
_X25gwTrapEnaTable_Object = MibTable
x25gwTrapEnaTable = _X25gwTrapEnaTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 4, 1)
)
if mibBuilder.loadTexts:
    x25gwTrapEnaTable.setStatus("mandatory")
_X25gwTrapEnaEntry_Object = MibTableRow
x25gwTrapEnaEntry = _X25gwTrapEnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 4, 1, 1)
)
x25gwTrapEnaEntry.setIndexNames(
    (0, "X25G-MIB", "x25gwTrapEnaIndex"),
)
if mibBuilder.loadTexts:
    x25gwTrapEnaEntry.setStatus("mandatory")
_X25gwTrapEnaIndex_Type = Integer32
_X25gwTrapEnaIndex_Object = MibTableColumn
x25gwTrapEnaIndex = _X25gwTrapEnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 4, 1, 1, 1),
    _X25gwTrapEnaIndex_Type()
)
x25gwTrapEnaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25gwTrapEnaIndex.setStatus("mandatory")


class _X25gwTrapEnaUiReset_Type(Integer32):
    """Custom type x25gwTrapEnaUiReset based on Integer32"""
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


_X25gwTrapEnaUiReset_Type.__name__ = "Integer32"
_X25gwTrapEnaUiReset_Object = MibTableColumn
x25gwTrapEnaUiReset = _X25gwTrapEnaUiReset_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 11, 4, 1, 1, 2),
    _X25gwTrapEnaUiReset_Type()
)
x25gwTrapEnaUiReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25gwTrapEnaUiReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "X25G-MIB",
    **{"usr": usr,
       "nas": nas,
       "x25g": x25g,
       "x25gwId": x25gwId,
       "x25gwIdTable": x25gwIdTable,
       "x25gwIdEntry": x25gwIdEntry,
       "x25gwIdIndex": x25gwIdIndex,
       "x25gwIdHardwareSerNum": x25gwIdHardwareSerNum,
       "x25gwIdHardwareRev": x25gwIdHardwareRev,
       "x25gwIdSoftwareRev": x25gwIdSoftwareRev,
       "x25gwIdCpuType": x25gwIdCpuType,
       "x25gwIdRamInstalled": x25gwIdRamInstalled,
       "x25gwIdFlashInstalled": x25gwIdFlashInstalled,
       "x25gwIdOperCfgSts": x25gwIdOperCfgSts,
       "x25gwIdSelfTestResult": x25gwIdSelfTestResult,
       "x25gwIdMgmtConnect": x25gwIdMgmtConnect,
       "x25gwCmd": x25gwCmd,
       "x25gwCmdTable": x25gwCmdTable,
       "x25gwCmdEntry": x25gwCmdEntry,
       "x25gwCmdIndex": x25gwCmdIndex,
       "x25gwCmdMgtStationId": x25gwCmdMgtStationId,
       "x25gwCmdReqId": x25gwCmdReqId,
       "x25gwCmdFunction": x25gwCmdFunction,
       "x25gwCmdForce": x25gwCmdForce,
       "x25gwCmdParam": x25gwCmdParam,
       "x25gwCmdResult": x25gwCmdResult,
       "x25gwCmdCode": x25gwCmdCode,
       "x25gwCfg": x25gwCfg,
       "x25gwCfgTable": x25gwCfgTable,
       "x25gwCfgEntry": x25gwCfgEntry,
       "x25gwCfgIndex": x25gwCfgIndex,
       "x25gwCfgUiPort": x25gwCfgUiPort,
       "x25gwCfgLocModemConn": x25gwCfgLocModemConn,
       "x25gwCfgRoutingType": x25gwCfgRoutingType,
       "x25gwCfgCudRoutStr": x25gwCfgCudRoutStr,
       "x25gwCfgX121SubAddr": x25gwCfgX121SubAddr,
       "x25gwCfgSysDate": x25gwCfgSysDate,
       "x25gwCfgSysTime": x25gwCfgSysTime,
       "x25gwTrapEna": x25gwTrapEna,
       "x25gwTrapEnaTable": x25gwTrapEnaTable,
       "x25gwTrapEnaEntry": x25gwTrapEnaEntry,
       "x25gwTrapEnaIndex": x25gwTrapEnaIndex,
       "x25gwTrapEnaUiReset": x25gwTrapEnaUiReset}
)

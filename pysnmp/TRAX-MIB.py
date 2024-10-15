# SNMP MIB module (TRAX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:42 2024
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
_Trax_ObjectIdentity = ObjectIdentity
trax = _Trax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 31)
)
_TraxId_ObjectIdentity = ObjectIdentity
traxId = _TraxId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1)
)
_TraxIdTable_Object = MibTable
traxIdTable = _TraxIdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1, 1)
)
if mibBuilder.loadTexts:
    traxIdTable.setStatus("mandatory")
_TraxIdEntry_Object = MibTableRow
traxIdEntry = _TraxIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1, 1, 1)
)
traxIdEntry.setIndexNames(
    (0, "TRAX-MIB", "traxIdIndex"),
)
if mibBuilder.loadTexts:
    traxIdEntry.setStatus("mandatory")
_TraxIdIndex_Type = Integer32
_TraxIdIndex_Object = MibTableColumn
traxIdIndex = _TraxIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1, 1, 1, 1),
    _TraxIdIndex_Type()
)
traxIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxIdIndex.setStatus("mandatory")
_TraxIdHardwareSerNum_Type = DisplayString
_TraxIdHardwareSerNum_Object = MibTableColumn
traxIdHardwareSerNum = _TraxIdHardwareSerNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1, 1, 1, 2),
    _TraxIdHardwareSerNum_Type()
)
traxIdHardwareSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxIdHardwareSerNum.setStatus("mandatory")
_TraxIdHardwareRev_Type = DisplayString
_TraxIdHardwareRev_Object = MibTableColumn
traxIdHardwareRev = _TraxIdHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1, 1, 1, 3),
    _TraxIdHardwareRev_Type()
)
traxIdHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxIdHardwareRev.setStatus("mandatory")
_TraxIdSoftwareRev_Type = DisplayString
_TraxIdSoftwareRev_Object = MibTableColumn
traxIdSoftwareRev = _TraxIdSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1, 1, 1, 4),
    _TraxIdSoftwareRev_Type()
)
traxIdSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxIdSoftwareRev.setStatus("mandatory")


class _TraxIdCpuType_Type(Integer32):
    """Custom type traxIdCpuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("i80386", 1),
          ("i80486", 2),
          ("powerPC603", 3))
    )


_TraxIdCpuType_Type.__name__ = "Integer32"
_TraxIdCpuType_Object = MibTableColumn
traxIdCpuType = _TraxIdCpuType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1, 1, 1, 5),
    _TraxIdCpuType_Type()
)
traxIdCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxIdCpuType.setStatus("mandatory")
_TraxIdRamInstalled_Type = Integer32
_TraxIdRamInstalled_Object = MibTableColumn
traxIdRamInstalled = _TraxIdRamInstalled_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1, 1, 1, 6),
    _TraxIdRamInstalled_Type()
)
traxIdRamInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxIdRamInstalled.setStatus("mandatory")
_TraxIdFlashInstalled_Type = Integer32
_TraxIdFlashInstalled_Object = MibTableColumn
traxIdFlashInstalled = _TraxIdFlashInstalled_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1, 1, 1, 7),
    _TraxIdFlashInstalled_Type()
)
traxIdFlashInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxIdFlashInstalled.setStatus("mandatory")
_TraxIdSelfTestResult_Type = Integer32
_TraxIdSelfTestResult_Object = MibTableColumn
traxIdSelfTestResult = _TraxIdSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1, 1, 1, 9),
    _TraxIdSelfTestResult_Type()
)
traxIdSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxIdSelfTestResult.setStatus("mandatory")


class _TraxIdMgmtConnect_Type(Integer32):
    """Custom type traxIdMgmtConnect based on Integer32"""
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


_TraxIdMgmtConnect_Type.__name__ = "Integer32"
_TraxIdMgmtConnect_Object = MibTableColumn
traxIdMgmtConnect = _TraxIdMgmtConnect_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 1, 1, 1, 10),
    _TraxIdMgmtConnect_Type()
)
traxIdMgmtConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxIdMgmtConnect.setStatus("mandatory")
_TraxCmd_ObjectIdentity = ObjectIdentity
traxCmd = _TraxCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 2)
)
_TraxCmdTable_Object = MibTable
traxCmdTable = _TraxCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 2, 1)
)
if mibBuilder.loadTexts:
    traxCmdTable.setStatus("mandatory")
_TraxCmdEntry_Object = MibTableRow
traxCmdEntry = _TraxCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 2, 1, 1)
)
traxCmdEntry.setIndexNames(
    (0, "TRAX-MIB", "traxCmdIndex"),
)
if mibBuilder.loadTexts:
    traxCmdEntry.setStatus("mandatory")
_TraxCmdIndex_Type = Integer32
_TraxCmdIndex_Object = MibTableColumn
traxCmdIndex = _TraxCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 2, 1, 1, 1),
    _TraxCmdIndex_Type()
)
traxCmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxCmdIndex.setStatus("mandatory")


class _TraxCmdMgtStationId_Type(OctetString):
    """Custom type traxCmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TraxCmdMgtStationId_Type.__name__ = "OctetString"
_TraxCmdMgtStationId_Object = MibTableColumn
traxCmdMgtStationId = _TraxCmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 2, 1, 1, 2),
    _TraxCmdMgtStationId_Type()
)
traxCmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCmdMgtStationId.setStatus("mandatory")
_TraxCmdReqId_Type = Integer32
_TraxCmdReqId_Object = MibTableColumn
traxCmdReqId = _TraxCmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 2, 1, 1, 3),
    _TraxCmdReqId_Type()
)
traxCmdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxCmdReqId.setStatus("mandatory")


class _TraxCmdFunction_Type(Integer32):
    """Custom type traxCmdFunction based on Integer32"""
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
        *(("disruptSelfTest", 6),
          ("downloadCfgFile", 8),
          ("noCommand", 1),
          ("nonDisruptSelfTest", 5),
          ("resetStsCounters", 10),
          ("restoreFromDefault", 4),
          ("restoreFromNVRAM", 3),
          ("saveToNVRAM", 2),
          ("softwareReset", 7),
          ("uploadCfgFile", 9))
    )


_TraxCmdFunction_Type.__name__ = "Integer32"
_TraxCmdFunction_Object = MibTableColumn
traxCmdFunction = _TraxCmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 2, 1, 1, 4),
    _TraxCmdFunction_Type()
)
traxCmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCmdFunction.setStatus("mandatory")
_TraxCmdForce_Type = Integer32
_TraxCmdForce_Object = MibTableColumn
traxCmdForce = _TraxCmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 2, 1, 1, 5),
    _TraxCmdForce_Type()
)
traxCmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCmdForce.setStatus("mandatory")
_TraxCmdParam_Type = OctetString
_TraxCmdParam_Object = MibTableColumn
traxCmdParam = _TraxCmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 2, 1, 1, 6),
    _TraxCmdParam_Type()
)
traxCmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCmdParam.setStatus("mandatory")


class _TraxCmdResult_Type(Integer32):
    """Custom type traxCmdResult based on Integer32"""
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


_TraxCmdResult_Type.__name__ = "Integer32"
_TraxCmdResult_Object = MibTableColumn
traxCmdResult = _TraxCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 2, 1, 1, 7),
    _TraxCmdResult_Type()
)
traxCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxCmdResult.setStatus("mandatory")


class _TraxCmdCode_Type(Integer32):
    """Custom type traxCmdCode based on Integer32"""
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


_TraxCmdCode_Type.__name__ = "Integer32"
_TraxCmdCode_Object = MibTableColumn
traxCmdCode = _TraxCmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 2, 1, 1, 8),
    _TraxCmdCode_Type()
)
traxCmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxCmdCode.setStatus("mandatory")
_TraxCfg_ObjectIdentity = ObjectIdentity
traxCfg = _TraxCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3)
)
_TraxCfgTable_Object = MibTable
traxCfgTable = _TraxCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1)
)
if mibBuilder.loadTexts:
    traxCfgTable.setStatus("mandatory")
_TraxCfgEntry_Object = MibTableRow
traxCfgEntry = _TraxCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1)
)
traxCfgEntry.setIndexNames(
    (0, "TRAX-MIB", "traxCfgIndex"),
)
if mibBuilder.loadTexts:
    traxCfgEntry.setStatus("mandatory")
_TraxCfgIndex_Type = Integer32
_TraxCfgIndex_Object = MibTableColumn
traxCfgIndex = _TraxCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 1),
    _TraxCfgIndex_Type()
)
traxCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxCfgIndex.setStatus("mandatory")
_TraxCfgCardIPAddress_Type = IpAddress
_TraxCfgCardIPAddress_Object = MibTableColumn
traxCfgCardIPAddress = _TraxCfgCardIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 2),
    _TraxCfgCardIPAddress_Type()
)
traxCfgCardIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgCardIPAddress.setStatus("mandatory")
_TraxCfgIPMask_Type = IpAddress
_TraxCfgIPMask_Object = MibTableColumn
traxCfgIPMask = _TraxCfgIPMask_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 3),
    _TraxCfgIPMask_Type()
)
traxCfgIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgIPMask.setStatus("mandatory")
_TraxCfgGatewayIpAddr_Type = IpAddress
_TraxCfgGatewayIpAddr_Object = MibTableColumn
traxCfgGatewayIpAddr = _TraxCfgGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 4),
    _TraxCfgGatewayIpAddr_Type()
)
traxCfgGatewayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgGatewayIpAddr.setStatus("mandatory")
_TraxCfgHostIPAddr_Type = IpAddress
_TraxCfgHostIPAddr_Object = MibTableColumn
traxCfgHostIPAddr = _TraxCfgHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 5),
    _TraxCfgHostIPAddr_Type()
)
traxCfgHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgHostIPAddr.setStatus("mandatory")


class _TraxCfgX25Addr_Type(DisplayString):
    """Custom type traxCfgX25Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TraxCfgX25Addr_Type.__name__ = "DisplayString"
_TraxCfgX25Addr_Object = MibTableColumn
traxCfgX25Addr = _TraxCfgX25Addr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 6),
    _TraxCfgX25Addr_Type()
)
traxCfgX25Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgX25Addr.setStatus("mandatory")
_TraxCfgNicTrapDestination_Type = IpAddress
_TraxCfgNicTrapDestination_Object = MibTableColumn
traxCfgNicTrapDestination = _TraxCfgNicTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 7),
    _TraxCfgNicTrapDestination_Type()
)
traxCfgNicTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgNicTrapDestination.setStatus("mandatory")
_TraxCfgReadMemAddr_Type = Integer32
_TraxCfgReadMemAddr_Object = MibTableColumn
traxCfgReadMemAddr = _TraxCfgReadMemAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 8),
    _TraxCfgReadMemAddr_Type()
)
traxCfgReadMemAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgReadMemAddr.setStatus("mandatory")


class _TraxCfgReadMemData_Type(OctetString):
    """Custom type traxCfgReadMemData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TraxCfgReadMemData_Type.__name__ = "OctetString"
_TraxCfgReadMemData_Object = MibTableColumn
traxCfgReadMemData = _TraxCfgReadMemData_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 9),
    _TraxCfgReadMemData_Type()
)
traxCfgReadMemData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgReadMemData.setStatus("mandatory")
_TraxCfgReadMemLength_Type = Integer32
_TraxCfgReadMemLength_Object = MibTableColumn
traxCfgReadMemLength = _TraxCfgReadMemLength_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 10),
    _TraxCfgReadMemLength_Type()
)
traxCfgReadMemLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgReadMemLength.setStatus("mandatory")
_TraxCfgWriteMemAddr_Type = Integer32
_TraxCfgWriteMemAddr_Object = MibTableColumn
traxCfgWriteMemAddr = _TraxCfgWriteMemAddr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 11),
    _TraxCfgWriteMemAddr_Type()
)
traxCfgWriteMemAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgWriteMemAddr.setStatus("mandatory")
_TraxCfgWriteMemLen_Type = Integer32
_TraxCfgWriteMemLen_Object = MibTableColumn
traxCfgWriteMemLen = _TraxCfgWriteMemLen_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 12),
    _TraxCfgWriteMemLen_Type()
)
traxCfgWriteMemLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgWriteMemLen.setStatus("mandatory")


class _TraxCfgWriteMemData_Type(OctetString):
    """Custom type traxCfgWriteMemData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TraxCfgWriteMemData_Type.__name__ = "OctetString"
_TraxCfgWriteMemData_Object = MibTableColumn
traxCfgWriteMemData = _TraxCfgWriteMemData_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 13),
    _TraxCfgWriteMemData_Type()
)
traxCfgWriteMemData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgWriteMemData.setStatus("mandatory")
_TraxFailureReason_Type = Integer32
_TraxFailureReason_Object = MibTableColumn
traxFailureReason = _TraxFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 14),
    _TraxFailureReason_Type()
)
traxFailureReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traxFailureReason.setStatus("mandatory")


class _TraxDNIFailureReason_Type(OctetString):
    """Custom type traxDNIFailureReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TraxDNIFailureReason_Type.__name__ = "OctetString"
_TraxDNIFailureReason_Object = MibTableColumn
traxDNIFailureReason = _TraxDNIFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 15),
    _TraxDNIFailureReason_Type()
)
traxDNIFailureReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traxDNIFailureReason.setStatus("mandatory")


class _TraxCfgX25AddrPort1_Type(DisplayString):
    """Custom type traxCfgX25AddrPort1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TraxCfgX25AddrPort1_Type.__name__ = "DisplayString"
_TraxCfgX25AddrPort1_Object = MibTableColumn
traxCfgX25AddrPort1 = _TraxCfgX25AddrPort1_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 3, 1, 1, 16),
    _TraxCfgX25AddrPort1_Type()
)
traxCfgX25AddrPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxCfgX25AddrPort1.setStatus("mandatory")
_TraxTrapEna_ObjectIdentity = ObjectIdentity
traxTrapEna = _TraxTrapEna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4)
)
_TraxTrapEnaTable_Object = MibTable
traxTrapEnaTable = _TraxTrapEnaTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1)
)
if mibBuilder.loadTexts:
    traxTrapEnaTable.setStatus("mandatory")
_TraxTrapEnaEntry_Object = MibTableRow
traxTrapEnaEntry = _TraxTrapEnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1)
)
traxTrapEnaEntry.setIndexNames(
    (0, "TRAX-MIB", "traxTrapEnaIndex"),
)
if mibBuilder.loadTexts:
    traxTrapEnaEntry.setStatus("mandatory")
_TraxTrapEnaIndex_Type = Integer32
_TraxTrapEnaIndex_Object = MibTableColumn
traxTrapEnaIndex = _TraxTrapEnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 1),
    _TraxTrapEnaIndex_Type()
)
traxTrapEnaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxTrapEnaIndex.setStatus("mandatory")


class _TraxTrapEnaNicMissing_Type(Integer32):
    """Custom type traxTrapEnaNicMissing based on Integer32"""
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


_TraxTrapEnaNicMissing_Type.__name__ = "Integer32"
_TraxTrapEnaNicMissing_Object = MibTableColumn
traxTrapEnaNicMissing = _TraxTrapEnaNicMissing_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 2),
    _TraxTrapEnaNicMissing_Type()
)
traxTrapEnaNicMissing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapEnaNicMissing.setStatus("mandatory")


class _TraxTrapEnaX25FrameLevelUp_Type(Integer32):
    """Custom type traxTrapEnaX25FrameLevelUp based on Integer32"""
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


_TraxTrapEnaX25FrameLevelUp_Type.__name__ = "Integer32"
_TraxTrapEnaX25FrameLevelUp_Object = MibTableColumn
traxTrapEnaX25FrameLevelUp = _TraxTrapEnaX25FrameLevelUp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 3),
    _TraxTrapEnaX25FrameLevelUp_Type()
)
traxTrapEnaX25FrameLevelUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapEnaX25FrameLevelUp.setStatus("mandatory")


class _TraxTrapEnaX25FrameLevelDown_Type(Integer32):
    """Custom type traxTrapEnaX25FrameLevelDown based on Integer32"""
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


_TraxTrapEnaX25FrameLevelDown_Type.__name__ = "Integer32"
_TraxTrapEnaX25FrameLevelDown_Object = MibTableColumn
traxTrapEnaX25FrameLevelDown = _TraxTrapEnaX25FrameLevelDown_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 4),
    _TraxTrapEnaX25FrameLevelDown_Type()
)
traxTrapEnaX25FrameLevelDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapEnaX25FrameLevelDown.setStatus("mandatory")


class _TraxTrapEnaX25PacketLevelUp_Type(Integer32):
    """Custom type traxTrapEnaX25PacketLevelUp based on Integer32"""
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


_TraxTrapEnaX25PacketLevelUp_Type.__name__ = "Integer32"
_TraxTrapEnaX25PacketLevelUp_Object = MibTableColumn
traxTrapEnaX25PacketLevelUp = _TraxTrapEnaX25PacketLevelUp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 5),
    _TraxTrapEnaX25PacketLevelUp_Type()
)
traxTrapEnaX25PacketLevelUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapEnaX25PacketLevelUp.setStatus("mandatory")


class _TraxTrapEnaX25PacketLevelDn_Type(Integer32):
    """Custom type traxTrapEnaX25PacketLevelDn based on Integer32"""
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


_TraxTrapEnaX25PacketLevelDn_Type.__name__ = "Integer32"
_TraxTrapEnaX25PacketLevelDn_Object = MibTableColumn
traxTrapEnaX25PacketLevelDn = _TraxTrapEnaX25PacketLevelDn_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 6),
    _TraxTrapEnaX25PacketLevelDn_Type()
)
traxTrapEnaX25PacketLevelDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapEnaX25PacketLevelDn.setStatus("mandatory")


class _TraxTrapEnaX25LostCalls_Type(Integer32):
    """Custom type traxTrapEnaX25LostCalls based on Integer32"""
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


_TraxTrapEnaX25LostCalls_Type.__name__ = "Integer32"
_TraxTrapEnaX25LostCalls_Object = MibTableColumn
traxTrapEnaX25LostCalls = _TraxTrapEnaX25LostCalls_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 7),
    _TraxTrapEnaX25LostCalls_Type()
)
traxTrapEnaX25LostCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapEnaX25LostCalls.setStatus("mandatory")


class _TraxTrapEnaX25LinkUp_Type(Integer32):
    """Custom type traxTrapEnaX25LinkUp based on Integer32"""
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


_TraxTrapEnaX25LinkUp_Type.__name__ = "Integer32"
_TraxTrapEnaX25LinkUp_Object = MibTableColumn
traxTrapEnaX25LinkUp = _TraxTrapEnaX25LinkUp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 8),
    _TraxTrapEnaX25LinkUp_Type()
)
traxTrapEnaX25LinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapEnaX25LinkUp.setStatus("mandatory")


class _TraxTrapEnaX25LinkDn_Type(Integer32):
    """Custom type traxTrapEnaX25LinkDn based on Integer32"""
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


_TraxTrapEnaX25LinkDn_Type.__name__ = "Integer32"
_TraxTrapEnaX25LinkDn_Object = MibTableColumn
traxTrapEnaX25LinkDn = _TraxTrapEnaX25LinkDn_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 9),
    _TraxTrapEnaX25LinkDn_Type()
)
traxTrapEnaX25LinkDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapEnaX25LinkDn.setStatus("mandatory")


class _TraxTrapEnaDnisLookUp_Type(Integer32):
    """Custom type traxTrapEnaDnisLookUp based on Integer32"""
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


_TraxTrapEnaDnisLookUp_Type.__name__ = "Integer32"
_TraxTrapEnaDnisLookUp_Object = MibTableColumn
traxTrapEnaDnisLookUp = _TraxTrapEnaDnisLookUp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 10),
    _TraxTrapEnaDnisLookUp_Type()
)
traxTrapEnaDnisLookUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapEnaDnisLookUp.setStatus("mandatory")


class _TraxTrapEnaSvcSetUp_Type(Integer32):
    """Custom type traxTrapEnaSvcSetUp based on Integer32"""
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


_TraxTrapEnaSvcSetUp_Type.__name__ = "Integer32"
_TraxTrapEnaSvcSetUp_Object = MibTableColumn
traxTrapEnaSvcSetUp = _TraxTrapEnaSvcSetUp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 11),
    _TraxTrapEnaSvcSetUp_Type()
)
traxTrapEnaSvcSetUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapEnaSvcSetUp.setStatus("mandatory")


class _TraxTrapEnaSvcAlarm_Type(Integer32):
    """Custom type traxTrapEnaSvcAlarm based on Integer32"""
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


_TraxTrapEnaSvcAlarm_Type.__name__ = "Integer32"
_TraxTrapEnaSvcAlarm_Object = MibTableColumn
traxTrapEnaSvcAlarm = _TraxTrapEnaSvcAlarm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 12),
    _TraxTrapEnaSvcAlarm_Type()
)
traxTrapEnaSvcAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapEnaSvcAlarm.setStatus("mandatory")


class _TraxTrapDupTrans_Type(Integer32):
    """Custom type traxTrapDupTrans based on Integer32"""
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


_TraxTrapDupTrans_Type.__name__ = "Integer32"
_TraxTrapDupTrans_Object = MibTableColumn
traxTrapDupTrans = _TraxTrapDupTrans_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 4, 1, 1, 13),
    _TraxTrapDupTrans_Type()
)
traxTrapDupTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traxTrapDupTrans.setStatus("mandatory")
_TraxVisaSts_ObjectIdentity = ObjectIdentity
traxVisaSts = _TraxVisaSts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5)
)
_TraxVisaStsTable_Object = MibTable
traxVisaStsTable = _TraxVisaStsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1)
)
if mibBuilder.loadTexts:
    traxVisaStsTable.setStatus("mandatory")
_TraxVisaStsEntry_Object = MibTableRow
traxVisaStsEntry = _TraxVisaStsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1)
)
traxVisaStsEntry.setIndexNames(
    (0, "TRAX-MIB", "traxVisaStsIndex"),
)
if mibBuilder.loadTexts:
    traxVisaStsEntry.setStatus("mandatory")
_TraxVisaStsIndex_Type = Integer32
_TraxVisaStsIndex_Object = MibTableColumn
traxVisaStsIndex = _TraxVisaStsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 1),
    _TraxVisaStsIndex_Type()
)
traxVisaStsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaStsIndex.setStatus("mandatory")
_TraxVisaCallCount_Type = Counter32
_TraxVisaCallCount_Object = MibTableColumn
traxVisaCallCount = _TraxVisaCallCount_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 2),
    _TraxVisaCallCount_Type()
)
traxVisaCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaCallCount.setStatus("mandatory")
_TraxVisaTransactionCount_Type = Counter32
_TraxVisaTransactionCount_Object = MibTableColumn
traxVisaTransactionCount = _TraxVisaTransactionCount_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 3),
    _TraxVisaTransactionCount_Type()
)
traxVisaTransactionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaTransactionCount.setStatus("mandatory")
_TraxVisaRetransCount_Type = Counter32
_TraxVisaRetransCount_Object = MibTableColumn
traxVisaRetransCount = _TraxVisaRetransCount_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 4),
    _TraxVisaRetransCount_Type()
)
traxVisaRetransCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaRetransCount.setStatus("mandatory")
_TraxVisaDuplicateTransCount_Type = Counter32
_TraxVisaDuplicateTransCount_Object = MibTableColumn
traxVisaDuplicateTransCount = _TraxVisaDuplicateTransCount_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 5),
    _TraxVisaDuplicateTransCount_Type()
)
traxVisaDuplicateTransCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDuplicateTransCount.setStatus("mandatory")
_TraxVisaDiscNormal_Type = Counter32
_TraxVisaDiscNormal_Object = MibTableColumn
traxVisaDiscNormal = _TraxVisaDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 6),
    _TraxVisaDiscNormal_Type()
)
traxVisaDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscNormal.setStatus("mandatory")
_TraxVisaDiscPosRequest_Type = Counter32
_TraxVisaDiscPosRequest_Object = MibTableColumn
traxVisaDiscPosRequest = _TraxVisaDiscPosRequest_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 7),
    _TraxVisaDiscPosRequest_Type()
)
traxVisaDiscPosRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscPosRequest.setStatus("mandatory")
_TraxVisaDiscHostRequest_Type = Counter32
_TraxVisaDiscHostRequest_Object = MibTableColumn
traxVisaDiscHostRequest = _TraxVisaDiscHostRequest_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 8),
    _TraxVisaDiscHostRequest_Type()
)
traxVisaDiscHostRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscHostRequest.setStatus("mandatory")
_TraxVisaDiscMaxEnqs_Type = Counter32
_TraxVisaDiscMaxEnqs_Object = MibTableColumn
traxVisaDiscMaxEnqs = _TraxVisaDiscMaxEnqs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 9),
    _TraxVisaDiscMaxEnqs_Type()
)
traxVisaDiscMaxEnqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscMaxEnqs.setStatus("mandatory")
_TraxVisaDiscMaxRetranToPos_Type = Counter32
_TraxVisaDiscMaxRetranToPos_Object = MibTableColumn
traxVisaDiscMaxRetranToPos = _TraxVisaDiscMaxRetranToPos_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 10),
    _TraxVisaDiscMaxRetranToPos_Type()
)
traxVisaDiscMaxRetranToPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscMaxRetranToPos.setStatus("mandatory")
_TraxVisaDiscMaxRetranToHost_Type = Counter32
_TraxVisaDiscMaxRetranToHost_Object = MibTableColumn
traxVisaDiscMaxRetranToHost = _TraxVisaDiscMaxRetranToHost_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 11),
    _TraxVisaDiscMaxRetranToHost_Type()
)
traxVisaDiscMaxRetranToHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscMaxRetranToHost.setStatus("mandatory")
_TraxVisaDiscMaxBadFrames_Type = Counter32
_TraxVisaDiscMaxBadFrames_Object = MibTableColumn
traxVisaDiscMaxBadFrames = _TraxVisaDiscMaxBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 12),
    _TraxVisaDiscMaxBadFrames_Type()
)
traxVisaDiscMaxBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscMaxBadFrames.setStatus("mandatory")
_TraxVisaDiscPosWriteTimeouts_Type = Counter32
_TraxVisaDiscPosWriteTimeouts_Object = MibTableColumn
traxVisaDiscPosWriteTimeouts = _TraxVisaDiscPosWriteTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 13),
    _TraxVisaDiscPosWriteTimeouts_Type()
)
traxVisaDiscPosWriteTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscPosWriteTimeouts.setStatus("mandatory")
_TraxVisaDiscHostWriteTimeouts_Type = Counter32
_TraxVisaDiscHostWriteTimeouts_Object = MibTableColumn
traxVisaDiscHostWriteTimeouts = _TraxVisaDiscHostWriteTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 14),
    _TraxVisaDiscHostWriteTimeouts_Type()
)
traxVisaDiscHostWriteTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscHostWriteTimeouts.setStatus("mandatory")
_TraxVisaDiscSynDelayTooLong_Type = Counter32
_TraxVisaDiscSynDelayTooLong_Object = MibTableColumn
traxVisaDiscSynDelayTooLong = _TraxVisaDiscSynDelayTooLong_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 15),
    _TraxVisaDiscSynDelayTooLong_Type()
)
traxVisaDiscSynDelayTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscSynDelayTooLong.setStatus("mandatory")
_TraxVisaDiscBadCurrentState_Type = Counter32
_TraxVisaDiscBadCurrentState_Object = MibTableColumn
traxVisaDiscBadCurrentState = _TraxVisaDiscBadCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 16),
    _TraxVisaDiscBadCurrentState_Type()
)
traxVisaDiscBadCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscBadCurrentState.setStatus("mandatory")
_TraxVisaDiscUnexpectedEvent_Type = Counter32
_TraxVisaDiscUnexpectedEvent_Object = MibTableColumn
traxVisaDiscUnexpectedEvent = _TraxVisaDiscUnexpectedEvent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 17),
    _TraxVisaDiscUnexpectedEvent_Type()
)
traxVisaDiscUnexpectedEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscUnexpectedEvent.setStatus("mandatory")
_TraxVisaDiscNdcLogonFailures_Type = Counter32
_TraxVisaDiscNdcLogonFailures_Object = MibTableColumn
traxVisaDiscNdcLogonFailures = _TraxVisaDiscNdcLogonFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 18),
    _TraxVisaDiscNdcLogonFailures_Type()
)
traxVisaDiscNdcLogonFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscNdcLogonFailures.setStatus("mandatory")
_TraxVisaDiscPosRcvTimeouts_Type = Counter32
_TraxVisaDiscPosRcvTimeouts_Object = MibTableColumn
traxVisaDiscPosRcvTimeouts = _TraxVisaDiscPosRcvTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 19),
    _TraxVisaDiscPosRcvTimeouts_Type()
)
traxVisaDiscPosRcvTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscPosRcvTimeouts.setStatus("mandatory")
_TraxVisaDiscPosFrameTooBig_Type = Counter32
_TraxVisaDiscPosFrameTooBig_Object = MibTableColumn
traxVisaDiscPosFrameTooBig = _TraxVisaDiscPosFrameTooBig_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 20),
    _TraxVisaDiscPosFrameTooBig_Type()
)
traxVisaDiscPosFrameTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscPosFrameTooBig.setStatus("mandatory")
_TraxVisaDiscHostFrameTooBig_Type = Counter32
_TraxVisaDiscHostFrameTooBig_Object = MibTableColumn
traxVisaDiscHostFrameTooBig = _TraxVisaDiscHostFrameTooBig_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 21),
    _TraxVisaDiscHostFrameTooBig_Type()
)
traxVisaDiscHostFrameTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscHostFrameTooBig.setStatus("mandatory")
_TraxVisaDiscHostRespTimeouts_Type = Counter32
_TraxVisaDiscHostRespTimeouts_Object = MibTableColumn
traxVisaDiscHostRespTimeouts = _TraxVisaDiscHostRespTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 22),
    _TraxVisaDiscHostRespTimeouts_Type()
)
traxVisaDiscHostRespTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscHostRespTimeouts.setStatus("mandatory")
_TraxVisaDiscNumBadMsg_Type = Counter32
_TraxVisaDiscNumBadMsg_Object = MibTableColumn
traxVisaDiscNumBadMsg = _TraxVisaDiscNumBadMsg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 23),
    _TraxVisaDiscNumBadMsg_Type()
)
traxVisaDiscNumBadMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscNumBadMsg.setStatus("mandatory")
_TraxVisaDiscNumSystem_Type = Counter32
_TraxVisaDiscNumSystem_Object = MibTableColumn
traxVisaDiscNumSystem = _TraxVisaDiscNumSystem_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 5, 1, 1, 24),
    _TraxVisaDiscNumSystem_Type()
)
traxVisaDiscNumSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxVisaDiscNumSystem.setStatus("mandatory")
_TraxSyncSts_ObjectIdentity = ObjectIdentity
traxSyncSts = _TraxSyncSts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6)
)
_TraxSyncStsTable_Object = MibTable
traxSyncStsTable = _TraxSyncStsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1)
)
if mibBuilder.loadTexts:
    traxSyncStsTable.setStatus("mandatory")
_TraxSyncStsEntry_Object = MibTableRow
traxSyncStsEntry = _TraxSyncStsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1)
)
traxSyncStsEntry.setIndexNames(
    (0, "TRAX-MIB", "traxSyncStsIndex"),
)
if mibBuilder.loadTexts:
    traxSyncStsEntry.setStatus("mandatory")
_TraxSyncStsIndex_Type = Integer32
_TraxSyncStsIndex_Object = MibTableColumn
traxSyncStsIndex = _TraxSyncStsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 1),
    _TraxSyncStsIndex_Type()
)
traxSyncStsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncStsIndex.setStatus("mandatory")
_TraxSyncCallCount_Type = Counter32
_TraxSyncCallCount_Object = MibTableColumn
traxSyncCallCount = _TraxSyncCallCount_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 2),
    _TraxSyncCallCount_Type()
)
traxSyncCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncCallCount.setStatus("mandatory")
_TraxSyncTransactionCount_Type = Counter32
_TraxSyncTransactionCount_Object = MibTableColumn
traxSyncTransactionCount = _TraxSyncTransactionCount_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 3),
    _TraxSyncTransactionCount_Type()
)
traxSyncTransactionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncTransactionCount.setStatus("mandatory")
_TraxSyncDiscNormal_Type = Counter32
_TraxSyncDiscNormal_Object = MibTableColumn
traxSyncDiscNormal = _TraxSyncDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 4),
    _TraxSyncDiscNormal_Type()
)
traxSyncDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscNormal.setStatus("mandatory")
_TraxSyncDiscMaxRetrans_Type = Counter32
_TraxSyncDiscMaxRetrans_Object = MibTableColumn
traxSyncDiscMaxRetrans = _TraxSyncDiscMaxRetrans_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 5),
    _TraxSyncDiscMaxRetrans_Type()
)
traxSyncDiscMaxRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscMaxRetrans.setStatus("mandatory")
_TraxSyncDiscMaxSnrms_Type = Counter32
_TraxSyncDiscMaxSnrms_Object = MibTableColumn
traxSyncDiscMaxSnrms = _TraxSyncDiscMaxSnrms_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 6),
    _TraxSyncDiscMaxSnrms_Type()
)
traxSyncDiscMaxSnrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscMaxSnrms.setStatus("mandatory")
_TraxSyncDiscHostFrameTooBig_Type = Counter32
_TraxSyncDiscHostFrameTooBig_Object = MibTableColumn
traxSyncDiscHostFrameTooBig = _TraxSyncDiscHostFrameTooBig_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 7),
    _TraxSyncDiscHostFrameTooBig_Type()
)
traxSyncDiscHostFrameTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscHostFrameTooBig.setStatus("mandatory")
_TraxSyncDiscPosFrameTooSmall_Type = Counter32
_TraxSyncDiscPosFrameTooSmall_Object = MibTableColumn
traxSyncDiscPosFrameTooSmall = _TraxSyncDiscPosFrameTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 8),
    _TraxSyncDiscPosFrameTooSmall_Type()
)
traxSyncDiscPosFrameTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscPosFrameTooSmall.setStatus("mandatory")
_TraxSyncDiscPosFrameTooBig_Type = Counter32
_TraxSyncDiscPosFrameTooBig_Object = MibTableColumn
traxSyncDiscPosFrameTooBig = _TraxSyncDiscPosFrameTooBig_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 9),
    _TraxSyncDiscPosFrameTooBig_Type()
)
traxSyncDiscPosFrameTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscPosFrameTooBig.setStatus("mandatory")
_TraxSyncDiscHostFlowOffTimeOuts_Type = Counter32
_TraxSyncDiscHostFlowOffTimeOuts_Object = MibTableColumn
traxSyncDiscHostFlowOffTimeOuts = _TraxSyncDiscHostFlowOffTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 10),
    _TraxSyncDiscHostFlowOffTimeOuts_Type()
)
traxSyncDiscHostFlowOffTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscHostFlowOffTimeOuts.setStatus("mandatory")
_TraxSyncDiscPosFlowoffTimeOuts_Type = Counter32
_TraxSyncDiscPosFlowoffTimeOuts_Object = MibTableColumn
traxSyncDiscPosFlowoffTimeOuts = _TraxSyncDiscPosFlowoffTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 11),
    _TraxSyncDiscPosFlowoffTimeOuts_Type()
)
traxSyncDiscPosFlowoffTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscPosFlowoffTimeOuts.setStatus("mandatory")
_TraxSyncDiscInactivityTimeouts_Type = Counter32
_TraxSyncDiscInactivityTimeouts_Object = MibTableColumn
traxSyncDiscInactivityTimeouts = _TraxSyncDiscInactivityTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 12),
    _TraxSyncDiscInactivityTimeouts_Type()
)
traxSyncDiscInactivityTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscInactivityTimeouts.setStatus("mandatory")
_TraxSyncDiscNoBuffers_Type = Counter32
_TraxSyncDiscNoBuffers_Object = MibTableColumn
traxSyncDiscNoBuffers = _TraxSyncDiscNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 13),
    _TraxSyncDiscNoBuffers_Type()
)
traxSyncDiscNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscNoBuffers.setStatus("mandatory")
_TraxSyncDiscInvalidEvent_Type = Counter32
_TraxSyncDiscInvalidEvent_Object = MibTableColumn
traxSyncDiscInvalidEvent = _TraxSyncDiscInvalidEvent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 14),
    _TraxSyncDiscInvalidEvent_Type()
)
traxSyncDiscInvalidEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscInvalidEvent.setStatus("mandatory")
_TraxSyncDiscInvalidState_Type = Counter32
_TraxSyncDiscInvalidState_Object = MibTableColumn
traxSyncDiscInvalidState = _TraxSyncDiscInvalidState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 6, 1, 1, 15),
    _TraxSyncDiscInvalidState_Type()
)
traxSyncDiscInvalidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxSyncDiscInvalidState.setStatus("mandatory")
_TraxX25wSts_ObjectIdentity = ObjectIdentity
traxX25wSts = _TraxX25wSts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7)
)
_Traxx25wanStats_ObjectIdentity = ObjectIdentity
traxx25wanStats = _Traxx25wanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1)
)
_Traxx25wanStatsTable_Object = MibTable
traxx25wanStatsTable = _Traxx25wanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1)
)
if mibBuilder.loadTexts:
    traxx25wanStatsTable.setStatus("mandatory")
_Traxx25wanStatsEntry_Object = MibTableRow
traxx25wanStatsEntry = _Traxx25wanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1)
)
traxx25wanStatsEntry.setIndexNames(
    (0, "TRAX-MIB", "traxx25wanStatsIndex"),
)
if mibBuilder.loadTexts:
    traxx25wanStatsEntry.setStatus("mandatory")
_Traxx25wanStatsIndex_Type = Integer32
_Traxx25wanStatsIndex_Object = MibTableColumn
traxx25wanStatsIndex = _Traxx25wanStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 1),
    _Traxx25wanStatsIndex_Type()
)
traxx25wanStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsIndex.setStatus("mandatory")
_Traxx25wanStatsGoodFramesTxs_Type = Counter32
_Traxx25wanStatsGoodFramesTxs_Object = MibTableColumn
traxx25wanStatsGoodFramesTxs = _Traxx25wanStatsGoodFramesTxs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 2),
    _Traxx25wanStatsGoodFramesTxs_Type()
)
traxx25wanStatsGoodFramesTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsGoodFramesTxs.setStatus("mandatory")
_Traxx25wanStatsGoodFramesRxs_Type = Counter32
_Traxx25wanStatsGoodFramesRxs_Object = MibTableColumn
traxx25wanStatsGoodFramesRxs = _Traxx25wanStatsGoodFramesRxs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 3),
    _Traxx25wanStatsGoodFramesRxs_Type()
)
traxx25wanStatsGoodFramesRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsGoodFramesRxs.setStatus("mandatory")
_Traxx25wanStatsTxUnderruns_Type = Counter32
_Traxx25wanStatsTxUnderruns_Object = MibTableColumn
traxx25wanStatsTxUnderruns = _Traxx25wanStatsTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 4),
    _Traxx25wanStatsTxUnderruns_Type()
)
traxx25wanStatsTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsTxUnderruns.setStatus("mandatory")
_Traxx25wanStatsRxOverruns_Type = Counter32
_Traxx25wanStatsRxOverruns_Object = MibTableColumn
traxx25wanStatsRxOverruns = _Traxx25wanStatsRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 5),
    _Traxx25wanStatsRxOverruns_Type()
)
traxx25wanStatsRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsRxOverruns.setStatus("mandatory")
_Traxx25wanStatsRxCrcErrs_Type = Counter32
_Traxx25wanStatsRxCrcErrs_Object = MibTableColumn
traxx25wanStatsRxCrcErrs = _Traxx25wanStatsRxCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 6),
    _Traxx25wanStatsRxCrcErrs_Type()
)
traxx25wanStatsRxCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsRxCrcErrs.setStatus("mandatory")
_Traxx25wanStatsRxFrameNoBufs_Type = Counter32
_Traxx25wanStatsRxFrameNoBufs_Object = MibTableColumn
traxx25wanStatsRxFrameNoBufs = _Traxx25wanStatsRxFrameNoBufs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 7),
    _Traxx25wanStatsRxFrameNoBufs_Type()
)
traxx25wanStatsRxFrameNoBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsRxFrameNoBufs.setStatus("mandatory")
_Traxx25wanStatsUnrecoveredRxs_Type = Counter32
_Traxx25wanStatsUnrecoveredRxs_Object = MibTableColumn
traxx25wanStatsUnrecoveredRxs = _Traxx25wanStatsUnrecoveredRxs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 8),
    _Traxx25wanStatsUnrecoveredRxs_Type()
)
traxx25wanStatsUnrecoveredRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsUnrecoveredRxs.setStatus("mandatory")
_Traxx25wanStatsRxOverflows_Type = Counter32
_Traxx25wanStatsRxOverflows_Object = MibTableColumn
traxx25wanStatsRxOverflows = _Traxx25wanStatsRxOverflows_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 9),
    _Traxx25wanStatsRxOverflows_Type()
)
traxx25wanStatsRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsRxOverflows.setStatus("mandatory")
_Traxx25wanStatsRxAborts_Type = Counter32
_Traxx25wanStatsRxAborts_Object = MibTableColumn
traxx25wanStatsRxAborts = _Traxx25wanStatsRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 10),
    _Traxx25wanStatsRxAborts_Type()
)
traxx25wanStatsRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsRxAborts.setStatus("mandatory")
_Traxx25wanStatsRxTooLongs_Type = Counter32
_Traxx25wanStatsRxTooLongs_Object = MibTableColumn
traxx25wanStatsRxTooLongs = _Traxx25wanStatsRxTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 11),
    _Traxx25wanStatsRxTooLongs_Type()
)
traxx25wanStatsRxTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsRxTooLongs.setStatus("mandatory")
_Traxx25wanStatsTxTooShorts_Type = Counter32
_Traxx25wanStatsTxTooShorts_Object = MibTableColumn
traxx25wanStatsTxTooShorts = _Traxx25wanStatsTxTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 12),
    _Traxx25wanStatsTxTooShorts_Type()
)
traxx25wanStatsTxTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsTxTooShorts.setStatus("mandatory")
_Traxx25wanStatsRxTooShorts_Type = Counter32
_Traxx25wanStatsRxTooShorts_Object = MibTableColumn
traxx25wanStatsRxTooShorts = _Traxx25wanStatsRxTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 13),
    _Traxx25wanStatsRxTooShorts_Type()
)
traxx25wanStatsRxTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsRxTooShorts.setStatus("mandatory")
_Traxx25wanStatsTxBadPackets_Type = Counter32
_Traxx25wanStatsTxBadPackets_Object = MibTableColumn
traxx25wanStatsTxBadPackets = _Traxx25wanStatsTxBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 14),
    _Traxx25wanStatsTxBadPackets_Type()
)
traxx25wanStatsTxBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsTxBadPackets.setStatus("mandatory")
_Traxx25wanStatsTxRingQFulls_Type = Counter32
_Traxx25wanStatsTxRingQFulls_Object = MibTableColumn
traxx25wanStatsTxRingQFulls = _Traxx25wanStatsTxRingQFulls_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 15),
    _Traxx25wanStatsTxRingQFulls_Type()
)
traxx25wanStatsTxRingQFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsTxRingQFulls.setStatus("mandatory")


class _Traxx25wanStatsDSR_Type(Integer32):
    """Custom type traxx25wanStatsDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Traxx25wanStatsDSR_Type.__name__ = "Integer32"
_Traxx25wanStatsDSR_Object = MibTableColumn
traxx25wanStatsDSR = _Traxx25wanStatsDSR_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 17),
    _Traxx25wanStatsDSR_Type()
)
traxx25wanStatsDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsDSR.setStatus("mandatory")


class _Traxx25wanStatsCTS_Type(Integer32):
    """Custom type traxx25wanStatsCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Traxx25wanStatsCTS_Type.__name__ = "Integer32"
_Traxx25wanStatsCTS_Object = MibTableColumn
traxx25wanStatsCTS = _Traxx25wanStatsCTS_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 18),
    _Traxx25wanStatsCTS_Type()
)
traxx25wanStatsCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsCTS.setStatus("mandatory")


class _Traxx25wanStatsDCD_Type(Integer32):
    """Custom type traxx25wanStatsDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Traxx25wanStatsDCD_Type.__name__ = "Integer32"
_Traxx25wanStatsDCD_Object = MibTableColumn
traxx25wanStatsDCD = _Traxx25wanStatsDCD_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 7, 1, 1, 1, 19),
    _Traxx25wanStatsDCD_Type()
)
traxx25wanStatsDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxx25wanStatsDCD.setStatus("mandatory")
_TraxUX25Sts_ObjectIdentity = ObjectIdentity
traxUX25Sts = _TraxUX25Sts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8)
)
_TraxUx25StatTable_Object = MibTable
traxUx25StatTable = _TraxUx25StatTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1)
)
if mibBuilder.loadTexts:
    traxUx25StatTable.setStatus("mandatory")
_TraxUx25StatEntry_Object = MibTableRow
traxUx25StatEntry = _TraxUx25StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1)
)
traxUx25StatEntry.setIndexNames(
    (0, "TRAX-MIB", "traxUx25StatIndex"),
)
if mibBuilder.loadTexts:
    traxUx25StatEntry.setStatus("mandatory")
_TraxUx25StatIndex_Type = Integer32
_TraxUx25StatIndex_Object = MibTableColumn
traxUx25StatIndex = _TraxUx25StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 1),
    _TraxUx25StatIndex_Type()
)
traxUx25StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatIndex.setStatus("mandatory")
_TraxUx25StatCallsRcvd_Type = Integer32
_TraxUx25StatCallsRcvd_Object = MibTableColumn
traxUx25StatCallsRcvd = _TraxUx25StatCallsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 2),
    _TraxUx25StatCallsRcvd_Type()
)
traxUx25StatCallsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatCallsRcvd.setStatus("mandatory")
_TraxUx25StatCallsSent_Type = Integer32
_TraxUx25StatCallsSent_Object = MibTableColumn
traxUx25StatCallsSent = _TraxUx25StatCallsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 3),
    _TraxUx25StatCallsSent_Type()
)
traxUx25StatCallsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatCallsSent.setStatus("mandatory")
_TraxUx25StatCallsRcvdEstab_Type = Integer32
_TraxUx25StatCallsRcvdEstab_Object = MibTableColumn
traxUx25StatCallsRcvdEstab = _TraxUx25StatCallsRcvdEstab_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 4),
    _TraxUx25StatCallsRcvdEstab_Type()
)
traxUx25StatCallsRcvdEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatCallsRcvdEstab.setStatus("mandatory")
_TraxUx25StatCallsSentEstab_Type = Integer32
_TraxUx25StatCallsSentEstab_Object = MibTableColumn
traxUx25StatCallsSentEstab = _TraxUx25StatCallsSentEstab_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 5),
    _TraxUx25StatCallsSentEstab_Type()
)
traxUx25StatCallsSentEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatCallsSentEstab.setStatus("mandatory")
_TraxUx25StatDataPktsRcvd_Type = Integer32
_TraxUx25StatDataPktsRcvd_Object = MibTableColumn
traxUx25StatDataPktsRcvd = _TraxUx25StatDataPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 6),
    _TraxUx25StatDataPktsRcvd_Type()
)
traxUx25StatDataPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatDataPktsRcvd.setStatus("mandatory")
_TraxUx25StatDataPktsSent_Type = Integer32
_TraxUx25StatDataPktsSent_Object = MibTableColumn
traxUx25StatDataPktsSent = _TraxUx25StatDataPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 7),
    _TraxUx25StatDataPktsSent_Type()
)
traxUx25StatDataPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatDataPktsSent.setStatus("mandatory")
_TraxUx25StatRestartsRcvd_Type = Integer32
_TraxUx25StatRestartsRcvd_Object = MibTableColumn
traxUx25StatRestartsRcvd = _TraxUx25StatRestartsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 8),
    _TraxUx25StatRestartsRcvd_Type()
)
traxUx25StatRestartsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatRestartsRcvd.setStatus("mandatory")
_TraxUx25StatRestartsSent_Type = Integer32
_TraxUx25StatRestartsSent_Object = MibTableColumn
traxUx25StatRestartsSent = _TraxUx25StatRestartsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 9),
    _TraxUx25StatRestartsSent_Type()
)
traxUx25StatRestartsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatRestartsSent.setStatus("mandatory")
_TraxUx25StatRcvrNotRdyRcvd_Type = Integer32
_TraxUx25StatRcvrNotRdyRcvd_Object = MibTableColumn
traxUx25StatRcvrNotRdyRcvd = _TraxUx25StatRcvrNotRdyRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 10),
    _TraxUx25StatRcvrNotRdyRcvd_Type()
)
traxUx25StatRcvrNotRdyRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatRcvrNotRdyRcvd.setStatus("mandatory")
_TraxUx25StatRcvrNotRdySent_Type = Integer32
_TraxUx25StatRcvrNotRdySent_Object = MibTableColumn
traxUx25StatRcvrNotRdySent = _TraxUx25StatRcvrNotRdySent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 11),
    _TraxUx25StatRcvrNotRdySent_Type()
)
traxUx25StatRcvrNotRdySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatRcvrNotRdySent.setStatus("mandatory")
_TraxUx25StatRcvrRdyRcvd_Type = Integer32
_TraxUx25StatRcvrRdyRcvd_Object = MibTableColumn
traxUx25StatRcvrRdyRcvd = _TraxUx25StatRcvrRdyRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 12),
    _TraxUx25StatRcvrRdyRcvd_Type()
)
traxUx25StatRcvrRdyRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatRcvrRdyRcvd.setStatus("mandatory")
_TraxUx25StatRcvrRdySent_Type = Integer32
_TraxUx25StatRcvrRdySent_Object = MibTableColumn
traxUx25StatRcvrRdySent = _TraxUx25StatRcvrRdySent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 13),
    _TraxUx25StatRcvrRdySent_Type()
)
traxUx25StatRcvrRdySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatRcvrRdySent.setStatus("mandatory")
_TraxUx25StatResetsRcvd_Type = Integer32
_TraxUx25StatResetsRcvd_Object = MibTableColumn
traxUx25StatResetsRcvd = _TraxUx25StatResetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 14),
    _TraxUx25StatResetsRcvd_Type()
)
traxUx25StatResetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatResetsRcvd.setStatus("mandatory")
_TraxUx25StatResetsSent_Type = Integer32
_TraxUx25StatResetsSent_Object = MibTableColumn
traxUx25StatResetsSent = _TraxUx25StatResetsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 15),
    _TraxUx25StatResetsSent_Type()
)
traxUx25StatResetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatResetsSent.setStatus("mandatory")
_TraxUx25StatDiagPktsRcvd_Type = Integer32
_TraxUx25StatDiagPktsRcvd_Object = MibTableColumn
traxUx25StatDiagPktsRcvd = _TraxUx25StatDiagPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 16),
    _TraxUx25StatDiagPktsRcvd_Type()
)
traxUx25StatDiagPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatDiagPktsRcvd.setStatus("mandatory")
_TraxUx25StatDiagPktsSent_Type = Integer32
_TraxUx25StatDiagPktsSent_Object = MibTableColumn
traxUx25StatDiagPktsSent = _TraxUx25StatDiagPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 17),
    _TraxUx25StatDiagPktsSent_Type()
)
traxUx25StatDiagPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatDiagPktsSent.setStatus("mandatory")
_TraxUx25StatIntrptPktsRcvd_Type = Integer32
_TraxUx25StatIntrptPktsRcvd_Object = MibTableColumn
traxUx25StatIntrptPktsRcvd = _TraxUx25StatIntrptPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 18),
    _TraxUx25StatIntrptPktsRcvd_Type()
)
traxUx25StatIntrptPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatIntrptPktsRcvd.setStatus("mandatory")
_TraxUx25StatIntrptPktsSent_Type = Integer32
_TraxUx25StatIntrptPktsSent_Object = MibTableColumn
traxUx25StatIntrptPktsSent = _TraxUx25StatIntrptPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 19),
    _TraxUx25StatIntrptPktsSent_Type()
)
traxUx25StatIntrptPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatIntrptPktsSent.setStatus("mandatory")
_TraxUx25StatRejPktsRcvd_Type = Integer32
_TraxUx25StatRejPktsRcvd_Object = MibTableColumn
traxUx25StatRejPktsRcvd = _TraxUx25StatRejPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 20),
    _TraxUx25StatRejPktsRcvd_Type()
)
traxUx25StatRejPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatRejPktsRcvd.setStatus("mandatory")
_TraxUx25StatRejPktsSent_Type = Integer32
_TraxUx25StatRejPktsSent_Object = MibTableColumn
traxUx25StatRejPktsSent = _TraxUx25StatRejPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 21),
    _TraxUx25StatRejPktsSent_Type()
)
traxUx25StatRejPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatRejPktsSent.setStatus("mandatory")
_TraxUx25StatClrPktRcvd_Type = Integer32
_TraxUx25StatClrPktRcvd_Object = MibTableColumn
traxUx25StatClrPktRcvd = _TraxUx25StatClrPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 22),
    _TraxUx25StatClrPktRcvd_Type()
)
traxUx25StatClrPktRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatClrPktRcvd.setStatus("mandatory")
_TraxUx25StatClrPktSent_Type = Integer32
_TraxUx25StatClrPktSent_Object = MibTableColumn
traxUx25StatClrPktSent = _TraxUx25StatClrPktSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 23),
    _TraxUx25StatClrPktSent_Type()
)
traxUx25StatClrPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatClrPktSent.setStatus("mandatory")
_TraxUx25StatPVCsInDatTrnsfrState_Type = Integer32
_TraxUx25StatPVCsInDatTrnsfrState_Object = MibTableColumn
traxUx25StatPVCsInDatTrnsfrState = _TraxUx25StatPVCsInDatTrnsfrState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 24),
    _TraxUx25StatPVCsInDatTrnsfrState_Type()
)
traxUx25StatPVCsInDatTrnsfrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatPVCsInDatTrnsfrState.setStatus("mandatory")
_TraxUx25StatSVCsInDatTrnsfrState_Type = Integer32
_TraxUx25StatSVCsInDatTrnsfrState_Object = MibTableColumn
traxUx25StatSVCsInDatTrnsfrState = _TraxUx25StatSVCsInDatTrnsfrState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 8, 1, 1, 25),
    _TraxUx25StatSVCsInDatTrnsfrState_Type()
)
traxUx25StatSVCsInDatTrnsfrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxUx25StatSVCsInDatTrnsfrState.setStatus("mandatory")
_TraxULPBSts_ObjectIdentity = ObjectIdentity
traxULPBSts = _TraxULPBSts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9)
)
_TraxulpbStatTable_Object = MibTable
traxulpbStatTable = _TraxulpbStatTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1)
)
if mibBuilder.loadTexts:
    traxulpbStatTable.setStatus("mandatory")
_TraxulpbStatEntry_Object = MibTableRow
traxulpbStatEntry = _TraxulpbStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1)
)
traxulpbStatEntry.setIndexNames(
    (0, "TRAX-MIB", "traxulpbStatIndex"),
)
if mibBuilder.loadTexts:
    traxulpbStatEntry.setStatus("mandatory")
_TraxulpbStatIndex_Type = Integer32
_TraxulpbStatIndex_Object = MibTableColumn
traxulpbStatIndex = _TraxulpbStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 1),
    _TraxulpbStatIndex_Type()
)
traxulpbStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatIndex.setStatus("mandatory")
_TraxulpbStatRRRcvd_Type = Integer32
_TraxulpbStatRRRcvd_Object = MibTableColumn
traxulpbStatRRRcvd = _TraxulpbStatRRRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 2),
    _TraxulpbStatRRRcvd_Type()
)
traxulpbStatRRRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatRRRcvd.setStatus("mandatory")
_TraxulpbStatRRTrnsmt_Type = Integer32
_TraxulpbStatRRTrnsmt_Object = MibTableColumn
traxulpbStatRRTrnsmt = _TraxulpbStatRRTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 3),
    _TraxulpbStatRRTrnsmt_Type()
)
traxulpbStatRRTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatRRTrnsmt.setStatus("mandatory")
_TraxulpbStatRNRCmdsRcvd_Type = Integer32
_TraxulpbStatRNRCmdsRcvd_Object = MibTableColumn
traxulpbStatRNRCmdsRcvd = _TraxulpbStatRNRCmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 4),
    _TraxulpbStatRNRCmdsRcvd_Type()
)
traxulpbStatRNRCmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatRNRCmdsRcvd.setStatus("mandatory")
_TraxulpbStatRNRCmdsTrnsmt_Type = Integer32
_TraxulpbStatRNRCmdsTrnsmt_Object = MibTableColumn
traxulpbStatRNRCmdsTrnsmt = _TraxulpbStatRNRCmdsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 5),
    _TraxulpbStatRNRCmdsTrnsmt_Type()
)
traxulpbStatRNRCmdsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatRNRCmdsTrnsmt.setStatus("mandatory")
_TraxulpbStatREJCmdsRcvd_Type = Integer32
_TraxulpbStatREJCmdsRcvd_Object = MibTableColumn
traxulpbStatREJCmdsRcvd = _TraxulpbStatREJCmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 6),
    _TraxulpbStatREJCmdsRcvd_Type()
)
traxulpbStatREJCmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatREJCmdsRcvd.setStatus("mandatory")
_TraxulpbStatREJCmdsTrnsmt_Type = Integer32
_TraxulpbStatREJCmdsTrnsmt_Object = MibTableColumn
traxulpbStatREJCmdsTrnsmt = _TraxulpbStatREJCmdsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 7),
    _TraxulpbStatREJCmdsTrnsmt_Type()
)
traxulpbStatREJCmdsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatREJCmdsTrnsmt.setStatus("mandatory")
_TraxulpbStatREJRspsRcvd_Type = Integer32
_TraxulpbStatREJRspsRcvd_Object = MibTableColumn
traxulpbStatREJRspsRcvd = _TraxulpbStatREJRspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 8),
    _TraxulpbStatREJRspsRcvd_Type()
)
traxulpbStatREJRspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatREJRspsRcvd.setStatus("mandatory")
_TraxulpbStatREJRspsTrnsmt_Type = Integer32
_TraxulpbStatREJRspsTrnsmt_Object = MibTableColumn
traxulpbStatREJRspsTrnsmt = _TraxulpbStatREJRspsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 9),
    _TraxulpbStatREJRspsTrnsmt_Type()
)
traxulpbStatREJRspsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatREJRspsTrnsmt.setStatus("mandatory")
_TraxulpbStatSABMCmdsRcvd_Type = Integer32
_TraxulpbStatSABMCmdsRcvd_Object = MibTableColumn
traxulpbStatSABMCmdsRcvd = _TraxulpbStatSABMCmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 10),
    _TraxulpbStatSABMCmdsRcvd_Type()
)
traxulpbStatSABMCmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatSABMCmdsRcvd.setStatus("mandatory")
_TraxulpbStatSABMCmdsTrnsmt_Type = Integer32
_TraxulpbStatSABMCmdsTrnsmt_Object = MibTableColumn
traxulpbStatSABMCmdsTrnsmt = _TraxulpbStatSABMCmdsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 11),
    _TraxulpbStatSABMCmdsTrnsmt_Type()
)
traxulpbStatSABMCmdsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatSABMCmdsTrnsmt.setStatus("mandatory")
_TraxulpbStatSABMECmdsRcvd_Type = Integer32
_TraxulpbStatSABMECmdsRcvd_Object = MibTableColumn
traxulpbStatSABMECmdsRcvd = _TraxulpbStatSABMECmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 12),
    _TraxulpbStatSABMECmdsRcvd_Type()
)
traxulpbStatSABMECmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatSABMECmdsRcvd.setStatus("mandatory")
_TraxulpbStatSABMECmdsTransmit_Type = Integer32
_TraxulpbStatSABMECmdsTransmit_Object = MibTableColumn
traxulpbStatSABMECmdsTransmit = _TraxulpbStatSABMECmdsTransmit_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 13),
    _TraxulpbStatSABMECmdsTransmit_Type()
)
traxulpbStatSABMECmdsTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatSABMECmdsTransmit.setStatus("mandatory")
_TraxulpbStatDISCCmdsRcvd_Type = Integer32
_TraxulpbStatDISCCmdsRcvd_Object = MibTableColumn
traxulpbStatDISCCmdsRcvd = _TraxulpbStatDISCCmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 14),
    _TraxulpbStatDISCCmdsRcvd_Type()
)
traxulpbStatDISCCmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatDISCCmdsRcvd.setStatus("mandatory")
_TraxulpbStatDISCCmdsTrnsmt_Type = Integer32
_TraxulpbStatDISCCmdsTrnsmt_Object = MibTableColumn
traxulpbStatDISCCmdsTrnsmt = _TraxulpbStatDISCCmdsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 15),
    _TraxulpbStatDISCCmdsTrnsmt_Type()
)
traxulpbStatDISCCmdsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatDISCCmdsTrnsmt.setStatus("mandatory")
_TraxulpbStatDMRspsRcvd_Type = Integer32
_TraxulpbStatDMRspsRcvd_Object = MibTableColumn
traxulpbStatDMRspsRcvd = _TraxulpbStatDMRspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 16),
    _TraxulpbStatDMRspsRcvd_Type()
)
traxulpbStatDMRspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatDMRspsRcvd.setStatus("mandatory")
_TraxulpbStatDMRspsTrnsmt_Type = Integer32
_TraxulpbStatDMRspsTrnsmt_Object = MibTableColumn
traxulpbStatDMRspsTrnsmt = _TraxulpbStatDMRspsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 17),
    _TraxulpbStatDMRspsTrnsmt_Type()
)
traxulpbStatDMRspsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatDMRspsTrnsmt.setStatus("mandatory")
_TraxulpbStatUARspsRcvd_Type = Integer32
_TraxulpbStatUARspsRcvd_Object = MibTableColumn
traxulpbStatUARspsRcvd = _TraxulpbStatUARspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 18),
    _TraxulpbStatUARspsRcvd_Type()
)
traxulpbStatUARspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatUARspsRcvd.setStatus("mandatory")
_TraxulpbStatUARspsTrnsmt_Type = Integer32
_TraxulpbStatUARspsTrnsmt_Object = MibTableColumn
traxulpbStatUARspsTrnsmt = _TraxulpbStatUARspsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 19),
    _TraxulpbStatUARspsTrnsmt_Type()
)
traxulpbStatUARspsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatUARspsTrnsmt.setStatus("mandatory")
_TraxulpbStatFRMRRspsRcvd_Type = Integer32
_TraxulpbStatFRMRRspsRcvd_Object = MibTableColumn
traxulpbStatFRMRRspsRcvd = _TraxulpbStatFRMRRspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 20),
    _TraxulpbStatFRMRRspsRcvd_Type()
)
traxulpbStatFRMRRspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatFRMRRspsRcvd.setStatus("mandatory")
_TraxulpbStatFRMRRspsTrnsmt_Type = Integer32
_TraxulpbStatFRMRRspsTrnsmt_Object = MibTableColumn
traxulpbStatFRMRRspsTrnsmt = _TraxulpbStatFRMRRspsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 21),
    _TraxulpbStatFRMRRspsTrnsmt_Type()
)
traxulpbStatFRMRRspsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatFRMRRspsTrnsmt.setStatus("mandatory")
_TraxulpbStatIFrameCmdsRcvd_Type = Integer32
_TraxulpbStatIFrameCmdsRcvd_Object = MibTableColumn
traxulpbStatIFrameCmdsRcvd = _TraxulpbStatIFrameCmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 22),
    _TraxulpbStatIFrameCmdsRcvd_Type()
)
traxulpbStatIFrameCmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatIFrameCmdsRcvd.setStatus("mandatory")
_TraxulpbStatIFrameCmdsTrnsmt_Type = Integer32
_TraxulpbStatIFrameCmdsTrnsmt_Object = MibTableColumn
traxulpbStatIFrameCmdsTrnsmt = _TraxulpbStatIFrameCmdsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 31, 9, 1, 1, 23),
    _TraxulpbStatIFrameCmdsTrnsmt_Type()
)
traxulpbStatIFrameCmdsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traxulpbStatIFrameCmdsTrnsmt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAX-MIB",
    **{"usr": usr,
       "nas": nas,
       "trax": trax,
       "traxId": traxId,
       "traxIdTable": traxIdTable,
       "traxIdEntry": traxIdEntry,
       "traxIdIndex": traxIdIndex,
       "traxIdHardwareSerNum": traxIdHardwareSerNum,
       "traxIdHardwareRev": traxIdHardwareRev,
       "traxIdSoftwareRev": traxIdSoftwareRev,
       "traxIdCpuType": traxIdCpuType,
       "traxIdRamInstalled": traxIdRamInstalled,
       "traxIdFlashInstalled": traxIdFlashInstalled,
       "traxIdSelfTestResult": traxIdSelfTestResult,
       "traxIdMgmtConnect": traxIdMgmtConnect,
       "traxCmd": traxCmd,
       "traxCmdTable": traxCmdTable,
       "traxCmdEntry": traxCmdEntry,
       "traxCmdIndex": traxCmdIndex,
       "traxCmdMgtStationId": traxCmdMgtStationId,
       "traxCmdReqId": traxCmdReqId,
       "traxCmdFunction": traxCmdFunction,
       "traxCmdForce": traxCmdForce,
       "traxCmdParam": traxCmdParam,
       "traxCmdResult": traxCmdResult,
       "traxCmdCode": traxCmdCode,
       "traxCfg": traxCfg,
       "traxCfgTable": traxCfgTable,
       "traxCfgEntry": traxCfgEntry,
       "traxCfgIndex": traxCfgIndex,
       "traxCfgCardIPAddress": traxCfgCardIPAddress,
       "traxCfgIPMask": traxCfgIPMask,
       "traxCfgGatewayIpAddr": traxCfgGatewayIpAddr,
       "traxCfgHostIPAddr": traxCfgHostIPAddr,
       "traxCfgX25Addr": traxCfgX25Addr,
       "traxCfgNicTrapDestination": traxCfgNicTrapDestination,
       "traxCfgReadMemAddr": traxCfgReadMemAddr,
       "traxCfgReadMemData": traxCfgReadMemData,
       "traxCfgReadMemLength": traxCfgReadMemLength,
       "traxCfgWriteMemAddr": traxCfgWriteMemAddr,
       "traxCfgWriteMemLen": traxCfgWriteMemLen,
       "traxCfgWriteMemData": traxCfgWriteMemData,
       "traxFailureReason": traxFailureReason,
       "traxDNIFailureReason": traxDNIFailureReason,
       "traxCfgX25AddrPort1": traxCfgX25AddrPort1,
       "traxTrapEna": traxTrapEna,
       "traxTrapEnaTable": traxTrapEnaTable,
       "traxTrapEnaEntry": traxTrapEnaEntry,
       "traxTrapEnaIndex": traxTrapEnaIndex,
       "traxTrapEnaNicMissing": traxTrapEnaNicMissing,
       "traxTrapEnaX25FrameLevelUp": traxTrapEnaX25FrameLevelUp,
       "traxTrapEnaX25FrameLevelDown": traxTrapEnaX25FrameLevelDown,
       "traxTrapEnaX25PacketLevelUp": traxTrapEnaX25PacketLevelUp,
       "traxTrapEnaX25PacketLevelDn": traxTrapEnaX25PacketLevelDn,
       "traxTrapEnaX25LostCalls": traxTrapEnaX25LostCalls,
       "traxTrapEnaX25LinkUp": traxTrapEnaX25LinkUp,
       "traxTrapEnaX25LinkDn": traxTrapEnaX25LinkDn,
       "traxTrapEnaDnisLookUp": traxTrapEnaDnisLookUp,
       "traxTrapEnaSvcSetUp": traxTrapEnaSvcSetUp,
       "traxTrapEnaSvcAlarm": traxTrapEnaSvcAlarm,
       "traxTrapDupTrans": traxTrapDupTrans,
       "traxVisaSts": traxVisaSts,
       "traxVisaStsTable": traxVisaStsTable,
       "traxVisaStsEntry": traxVisaStsEntry,
       "traxVisaStsIndex": traxVisaStsIndex,
       "traxVisaCallCount": traxVisaCallCount,
       "traxVisaTransactionCount": traxVisaTransactionCount,
       "traxVisaRetransCount": traxVisaRetransCount,
       "traxVisaDuplicateTransCount": traxVisaDuplicateTransCount,
       "traxVisaDiscNormal": traxVisaDiscNormal,
       "traxVisaDiscPosRequest": traxVisaDiscPosRequest,
       "traxVisaDiscHostRequest": traxVisaDiscHostRequest,
       "traxVisaDiscMaxEnqs": traxVisaDiscMaxEnqs,
       "traxVisaDiscMaxRetranToPos": traxVisaDiscMaxRetranToPos,
       "traxVisaDiscMaxRetranToHost": traxVisaDiscMaxRetranToHost,
       "traxVisaDiscMaxBadFrames": traxVisaDiscMaxBadFrames,
       "traxVisaDiscPosWriteTimeouts": traxVisaDiscPosWriteTimeouts,
       "traxVisaDiscHostWriteTimeouts": traxVisaDiscHostWriteTimeouts,
       "traxVisaDiscSynDelayTooLong": traxVisaDiscSynDelayTooLong,
       "traxVisaDiscBadCurrentState": traxVisaDiscBadCurrentState,
       "traxVisaDiscUnexpectedEvent": traxVisaDiscUnexpectedEvent,
       "traxVisaDiscNdcLogonFailures": traxVisaDiscNdcLogonFailures,
       "traxVisaDiscPosRcvTimeouts": traxVisaDiscPosRcvTimeouts,
       "traxVisaDiscPosFrameTooBig": traxVisaDiscPosFrameTooBig,
       "traxVisaDiscHostFrameTooBig": traxVisaDiscHostFrameTooBig,
       "traxVisaDiscHostRespTimeouts": traxVisaDiscHostRespTimeouts,
       "traxVisaDiscNumBadMsg": traxVisaDiscNumBadMsg,
       "traxVisaDiscNumSystem": traxVisaDiscNumSystem,
       "traxSyncSts": traxSyncSts,
       "traxSyncStsTable": traxSyncStsTable,
       "traxSyncStsEntry": traxSyncStsEntry,
       "traxSyncStsIndex": traxSyncStsIndex,
       "traxSyncCallCount": traxSyncCallCount,
       "traxSyncTransactionCount": traxSyncTransactionCount,
       "traxSyncDiscNormal": traxSyncDiscNormal,
       "traxSyncDiscMaxRetrans": traxSyncDiscMaxRetrans,
       "traxSyncDiscMaxSnrms": traxSyncDiscMaxSnrms,
       "traxSyncDiscHostFrameTooBig": traxSyncDiscHostFrameTooBig,
       "traxSyncDiscPosFrameTooSmall": traxSyncDiscPosFrameTooSmall,
       "traxSyncDiscPosFrameTooBig": traxSyncDiscPosFrameTooBig,
       "traxSyncDiscHostFlowOffTimeOuts": traxSyncDiscHostFlowOffTimeOuts,
       "traxSyncDiscPosFlowoffTimeOuts": traxSyncDiscPosFlowoffTimeOuts,
       "traxSyncDiscInactivityTimeouts": traxSyncDiscInactivityTimeouts,
       "traxSyncDiscNoBuffers": traxSyncDiscNoBuffers,
       "traxSyncDiscInvalidEvent": traxSyncDiscInvalidEvent,
       "traxSyncDiscInvalidState": traxSyncDiscInvalidState,
       "traxX25wSts": traxX25wSts,
       "traxx25wanStats": traxx25wanStats,
       "traxx25wanStatsTable": traxx25wanStatsTable,
       "traxx25wanStatsEntry": traxx25wanStatsEntry,
       "traxx25wanStatsIndex": traxx25wanStatsIndex,
       "traxx25wanStatsGoodFramesTxs": traxx25wanStatsGoodFramesTxs,
       "traxx25wanStatsGoodFramesRxs": traxx25wanStatsGoodFramesRxs,
       "traxx25wanStatsTxUnderruns": traxx25wanStatsTxUnderruns,
       "traxx25wanStatsRxOverruns": traxx25wanStatsRxOverruns,
       "traxx25wanStatsRxCrcErrs": traxx25wanStatsRxCrcErrs,
       "traxx25wanStatsRxFrameNoBufs": traxx25wanStatsRxFrameNoBufs,
       "traxx25wanStatsUnrecoveredRxs": traxx25wanStatsUnrecoveredRxs,
       "traxx25wanStatsRxOverflows": traxx25wanStatsRxOverflows,
       "traxx25wanStatsRxAborts": traxx25wanStatsRxAborts,
       "traxx25wanStatsRxTooLongs": traxx25wanStatsRxTooLongs,
       "traxx25wanStatsTxTooShorts": traxx25wanStatsTxTooShorts,
       "traxx25wanStatsRxTooShorts": traxx25wanStatsRxTooShorts,
       "traxx25wanStatsTxBadPackets": traxx25wanStatsTxBadPackets,
       "traxx25wanStatsTxRingQFulls": traxx25wanStatsTxRingQFulls,
       "traxx25wanStatsDSR": traxx25wanStatsDSR,
       "traxx25wanStatsCTS": traxx25wanStatsCTS,
       "traxx25wanStatsDCD": traxx25wanStatsDCD,
       "traxUX25Sts": traxUX25Sts,
       "traxUx25StatTable": traxUx25StatTable,
       "traxUx25StatEntry": traxUx25StatEntry,
       "traxUx25StatIndex": traxUx25StatIndex,
       "traxUx25StatCallsRcvd": traxUx25StatCallsRcvd,
       "traxUx25StatCallsSent": traxUx25StatCallsSent,
       "traxUx25StatCallsRcvdEstab": traxUx25StatCallsRcvdEstab,
       "traxUx25StatCallsSentEstab": traxUx25StatCallsSentEstab,
       "traxUx25StatDataPktsRcvd": traxUx25StatDataPktsRcvd,
       "traxUx25StatDataPktsSent": traxUx25StatDataPktsSent,
       "traxUx25StatRestartsRcvd": traxUx25StatRestartsRcvd,
       "traxUx25StatRestartsSent": traxUx25StatRestartsSent,
       "traxUx25StatRcvrNotRdyRcvd": traxUx25StatRcvrNotRdyRcvd,
       "traxUx25StatRcvrNotRdySent": traxUx25StatRcvrNotRdySent,
       "traxUx25StatRcvrRdyRcvd": traxUx25StatRcvrRdyRcvd,
       "traxUx25StatRcvrRdySent": traxUx25StatRcvrRdySent,
       "traxUx25StatResetsRcvd": traxUx25StatResetsRcvd,
       "traxUx25StatResetsSent": traxUx25StatResetsSent,
       "traxUx25StatDiagPktsRcvd": traxUx25StatDiagPktsRcvd,
       "traxUx25StatDiagPktsSent": traxUx25StatDiagPktsSent,
       "traxUx25StatIntrptPktsRcvd": traxUx25StatIntrptPktsRcvd,
       "traxUx25StatIntrptPktsSent": traxUx25StatIntrptPktsSent,
       "traxUx25StatRejPktsRcvd": traxUx25StatRejPktsRcvd,
       "traxUx25StatRejPktsSent": traxUx25StatRejPktsSent,
       "traxUx25StatClrPktRcvd": traxUx25StatClrPktRcvd,
       "traxUx25StatClrPktSent": traxUx25StatClrPktSent,
       "traxUx25StatPVCsInDatTrnsfrState": traxUx25StatPVCsInDatTrnsfrState,
       "traxUx25StatSVCsInDatTrnsfrState": traxUx25StatSVCsInDatTrnsfrState,
       "traxULPBSts": traxULPBSts,
       "traxulpbStatTable": traxulpbStatTable,
       "traxulpbStatEntry": traxulpbStatEntry,
       "traxulpbStatIndex": traxulpbStatIndex,
       "traxulpbStatRRRcvd": traxulpbStatRRRcvd,
       "traxulpbStatRRTrnsmt": traxulpbStatRRTrnsmt,
       "traxulpbStatRNRCmdsRcvd": traxulpbStatRNRCmdsRcvd,
       "traxulpbStatRNRCmdsTrnsmt": traxulpbStatRNRCmdsTrnsmt,
       "traxulpbStatREJCmdsRcvd": traxulpbStatREJCmdsRcvd,
       "traxulpbStatREJCmdsTrnsmt": traxulpbStatREJCmdsTrnsmt,
       "traxulpbStatREJRspsRcvd": traxulpbStatREJRspsRcvd,
       "traxulpbStatREJRspsTrnsmt": traxulpbStatREJRspsTrnsmt,
       "traxulpbStatSABMCmdsRcvd": traxulpbStatSABMCmdsRcvd,
       "traxulpbStatSABMCmdsTrnsmt": traxulpbStatSABMCmdsTrnsmt,
       "traxulpbStatSABMECmdsRcvd": traxulpbStatSABMECmdsRcvd,
       "traxulpbStatSABMECmdsTransmit": traxulpbStatSABMECmdsTransmit,
       "traxulpbStatDISCCmdsRcvd": traxulpbStatDISCCmdsRcvd,
       "traxulpbStatDISCCmdsTrnsmt": traxulpbStatDISCCmdsTrnsmt,
       "traxulpbStatDMRspsRcvd": traxulpbStatDMRspsRcvd,
       "traxulpbStatDMRspsTrnsmt": traxulpbStatDMRspsTrnsmt,
       "traxulpbStatUARspsRcvd": traxulpbStatUARspsRcvd,
       "traxulpbStatUARspsTrnsmt": traxulpbStatUARspsTrnsmt,
       "traxulpbStatFRMRRspsRcvd": traxulpbStatFRMRRspsRcvd,
       "traxulpbStatFRMRRspsTrnsmt": traxulpbStatFRMRRspsTrnsmt,
       "traxulpbStatIFrameCmdsRcvd": traxulpbStatIFrameCmdsRcvd,
       "traxulpbStatIFrameCmdsTrnsmt": traxulpbStatIFrameCmdsTrnsmt}
)

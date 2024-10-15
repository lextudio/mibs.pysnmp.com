# SNMP MIB module (A3COM-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:39 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rivet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8)
)
rivet.setRevisions(
        ("2004-04-27 07:55",
         "2004-09-01 00:00",
         "2004-10-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Wlan_mib_ObjectIdentity = ObjectIdentity
wlan_mib = _Wlan_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35)
)
_EnterpriseApSys_ObjectIdentity = ObjectIdentity
enterpriseApSys = _EnterpriseApSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 1)
)


class _SwHardwareVer_Type(DisplayString):
    """Custom type swHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwHardwareVer_Type.__name__ = "DisplayString"
_SwHardwareVer_Object = MibScalar
swHardwareVer = _SwHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 1, 1),
    _SwHardwareVer_Type()
)
swHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHardwareVer.setStatus("current")


class _SwBootRomVer_Type(DisplayString):
    """Custom type swBootRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwBootRomVer_Type.__name__ = "DisplayString"
_SwBootRomVer_Object = MibScalar
swBootRomVer = _SwBootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 1, 2),
    _SwBootRomVer_Type()
)
swBootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootRomVer.setStatus("current")


class _SwOpCodeVer_Type(DisplayString):
    """Custom type swOpCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwOpCodeVer_Type.__name__ = "DisplayString"
_SwOpCodeVer_Object = MibScalar
swOpCodeVer = _SwOpCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 1, 3),
    _SwOpCodeVer_Type()
)
swOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOpCodeVer.setStatus("current")


class _SwSerialNumber_Type(DisplayString):
    """Custom type swSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwSerialNumber_Type.__name__ = "DisplayString"
_SwSerialNumber_Object = MibScalar
swSerialNumber = _SwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 1, 4),
    _SwSerialNumber_Type()
)
swSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSerialNumber.setStatus("current")
_EnterpriseApLineMgnt_ObjectIdentity = ObjectIdentity
enterpriseApLineMgnt = _EnterpriseApLineMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 2)
)
_LineTable_Object = MibTable
lineTable = _LineTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 2, 1)
)
if mibBuilder.loadTexts:
    lineTable.setStatus("current")
_LineEntry_Object = MibTableRow
lineEntry = _LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 2, 1, 1)
)
lineEntry.setIndexNames(
    (0, "A3COM-PRIVATE-MIB", "lineIndex"),
)
if mibBuilder.loadTexts:
    lineEntry.setStatus("current")
_LineIndex_Type = Integer32
_LineIndex_Object = MibTableColumn
lineIndex = _LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 2, 1, 1, 1),
    _LineIndex_Type()
)
lineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lineIndex.setStatus("current")
_LineDataBits_Type = Integer32
_LineDataBits_Object = MibTableColumn
lineDataBits = _LineDataBits_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 2, 1, 1, 2),
    _LineDataBits_Type()
)
lineDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDataBits.setStatus("current")


class _LineParity_Type(Integer32):
    """Custom type lineParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 99),
          ("odd", 1))
    )


_LineParity_Type.__name__ = "Integer32"
_LineParity_Object = MibTableColumn
lineParity = _LineParity_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 2, 1, 1, 3),
    _LineParity_Type()
)
lineParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineParity.setStatus("current")
_LineSpeed_Type = Integer32
_LineSpeed_Object = MibTableColumn
lineSpeed = _LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 2, 1, 1, 4),
    _LineSpeed_Type()
)
lineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineSpeed.setStatus("current")
_LineStopBits_Type = Integer32
_LineStopBits_Object = MibTableColumn
lineStopBits = _LineStopBits_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 2, 1, 1, 5),
    _LineStopBits_Type()
)
lineStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineStopBits.setStatus("current")
_EnterpriseApPortMgnt_ObjectIdentity = ObjectIdentity
enterpriseApPortMgnt = _EnterpriseApPortMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3, 1, 1)
)
portEntry.setIndexNames(
    (0, "A3COM-PRIVATE-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3, 1, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("hundredBaseFX", 3),
          ("hundredBaseTX", 2),
          ("other", 1),
          ("thousandBaseGBIC", 7),
          ("thousandBaseLX", 5),
          ("thousandBaseMiniGBIC", 8),
          ("thousandBaseSX", 4),
          ("thousandBaseT", 6))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3, 1, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortSpeedDpxCfg_Type(Integer32):
    """Custom type portSpeedDpxCfg based on Integer32"""
    defaultValue = 2

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
        *(("fullDuplex10", 3),
          ("fullDuplex100", 5),
          ("fullDuplex1000", 7),
          ("halfDuplex10", 2),
          ("halfDuplex100", 4),
          ("halfDuplex1000", 6),
          ("reserved", 1))
    )


_PortSpeedDpxCfg_Type.__name__ = "Integer32"
_PortSpeedDpxCfg_Object = MibTableColumn
portSpeedDpxCfg = _PortSpeedDpxCfg_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3, 1, 1, 4),
    _PortSpeedDpxCfg_Type()
)
portSpeedDpxCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeedDpxCfg.setStatus("current")


class _PortFlowCtrlCfg_Type(Integer32):
    """Custom type portFlowCtrlCfg based on Integer32"""
    defaultValue = 1

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
        *(("backPressure", 3),
          ("disabled", 2),
          ("dot3xFlowControl", 4),
          ("enabled", 1))
    )


_PortFlowCtrlCfg_Type.__name__ = "Integer32"
_PortFlowCtrlCfg_Object = MibTableColumn
portFlowCtrlCfg = _PortFlowCtrlCfg_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3, 1, 1, 5),
    _PortFlowCtrlCfg_Type()
)
portFlowCtrlCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlCfg.setStatus("current")


class _PortCapabilities_Type(Integer32):
    """Custom type portCapabilities based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("portCap1000full", 5),
          ("portCap1000half", 4),
          ("portCap100full", 3),
          ("portCap100half", 2),
          ("portCap10full", 1),
          ("portCap10half", 99),
          ("portCapFlowCtrl", 15),
          ("portCapSym", 14),
          ("reserved10", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("reserved9", 9))
    )


_PortCapabilities_Type.__name__ = "Integer32"
_PortCapabilities_Object = MibTableColumn
portCapabilities = _PortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3, 1, 1, 6),
    _PortCapabilities_Type()
)
portCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCapabilities.setStatus("current")


class _PortAutonegotiation_Type(Integer32):
    """Custom type portAutonegotiation based on Integer32"""
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


_PortAutonegotiation_Type.__name__ = "Integer32"
_PortAutonegotiation_Object = MibTableColumn
portAutonegotiation = _PortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3, 1, 1, 7),
    _PortAutonegotiation_Type()
)
portAutonegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAutonegotiation.setStatus("current")


class _PortSpeedDpxStatus_Type(Integer32):
    """Custom type portSpeedDpxStatus based on Integer32"""
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
        *(("error", 1),
          ("fullDuplex10", 3),
          ("fullDuplex100", 5),
          ("fullDuplex1000", 7),
          ("halfDuplex10", 2),
          ("halfDuplex100", 4),
          ("halfDuplex1000", 6))
    )


_PortSpeedDpxStatus_Type.__name__ = "Integer32"
_PortSpeedDpxStatus_Object = MibTableColumn
portSpeedDpxStatus = _PortSpeedDpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3, 1, 1, 8),
    _PortSpeedDpxStatus_Type()
)
portSpeedDpxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeedDpxStatus.setStatus("current")


class _PortFlowCtrlStatus_Type(Integer32):
    """Custom type portFlowCtrlStatus based on Integer32"""
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
        *(("backPressure", 2),
          ("dot3xFlowControl", 3),
          ("error", 1),
          ("none", 4))
    )


_PortFlowCtrlStatus_Type.__name__ = "Integer32"
_PortFlowCtrlStatus_Object = MibTableColumn
portFlowCtrlStatus = _PortFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 3, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("current")
_EnterpriseApFileTransferMgt_ObjectIdentity = ObjectIdentity
enterpriseApFileTransferMgt = _EnterpriseApFileTransferMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 4)
)


class _TransferType_Type(Integer32):
    """Custom type transferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("tftp", 2))
    )


_TransferType_Type.__name__ = "Integer32"
_TransferType_Object = MibScalar
transferType = _TransferType_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 4, 1),
    _TransferType_Type()
)
transferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferType.setStatus("current")


class _FileType_Type(Integer32):
    """Custom type fileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("application", 1),
          ("config", 2))
    )


_FileType_Type.__name__ = "Integer32"
_FileType_Object = MibScalar
fileType = _FileType_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 4, 2),
    _FileType_Type()
)
fileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileType.setStatus("current")


class _SrcFile_Type(DisplayString):
    """Custom type srcFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SrcFile_Type.__name__ = "DisplayString"
_SrcFile_Object = MibScalar
srcFile = _SrcFile_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 4, 3),
    _SrcFile_Type()
)
srcFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcFile.setStatus("current")


class _DestFile_Type(DisplayString):
    """Custom type destFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DestFile_Type.__name__ = "DisplayString"
_DestFile_Object = MibScalar
destFile = _DestFile_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 4, 4),
    _DestFile_Type()
)
destFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destFile.setStatus("current")
_FileServer_Type = IpAddress
_FileServer_Object = MibScalar
fileServer = _FileServer_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 4, 5),
    _FileServer_Type()
)
fileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServer.setStatus("current")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 4, 6),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _Password_Type(DisplayString):
    """Custom type password based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Password_Type.__name__ = "DisplayString"
_Password_Object = MibScalar
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 4, 7),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("current")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11,
              12,
              13,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("failureGeneric", 3),
          ("flashFtypeError", 13),
          ("flashMallocError", 11),
          ("flashOpenError", 10),
          ("flashReadError", 12),
          ("protocolError", 30),
          ("running", 1),
          ("socketWriteError", 20),
          ("success", 2))
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 4, 8),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")


class _TransferStart_Type(Integer32):
    """Custom type transferStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2))
    )


_TransferStart_Type.__name__ = "Integer32"
_TransferStart_Object = MibScalar
transferStart = _TransferStart_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 4, 9),
    _TransferStart_Type()
)
transferStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferStart.setStatus("current")
_EnterpriseApResetMgt_ObjectIdentity = ObjectIdentity
enterpriseApResetMgt = _EnterpriseApResetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 5)
)


class _RestartOpCodeFile_Type(DisplayString):
    """Custom type restartOpCodeFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RestartOpCodeFile_Type.__name__ = "DisplayString"
_RestartOpCodeFile_Object = MibScalar
restartOpCodeFile = _RestartOpCodeFile_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 5, 1),
    _RestartOpCodeFile_Type()
)
restartOpCodeFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartOpCodeFile.setStatus("current")


class _RestartControl_Type(Integer32):
    """Custom type restartControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldBoot", 3),
          ("running", 1),
          ("warmBoot", 2))
    )


_RestartControl_Type.__name__ = "Integer32"
_RestartControl_Object = MibScalar
restartControl = _RestartControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 5, 2),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("current")
_EnterpriseApIpMgt_ObjectIdentity = ObjectIdentity
enterpriseApIpMgt = _EnterpriseApIpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 6)
)
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibScalar
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 6, 1),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("current")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibScalar
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 6, 2),
    _NetConfigSubnetMask_Type()
)
netConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigSubnetMask.setStatus("current")
_NetConfigDefaultGateway_Type = IpAddress
_NetConfigDefaultGateway_Object = MibScalar
netConfigDefaultGateway = _NetConfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 6, 3),
    _NetConfigDefaultGateway_Type()
)
netConfigDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigDefaultGateway.setStatus("current")


class _NetConfigHttpState_Type(Integer32):
    """Custom type netConfigHttpState based on Integer32"""
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


_NetConfigHttpState_Type.__name__ = "Integer32"
_NetConfigHttpState_Object = MibScalar
netConfigHttpState = _NetConfigHttpState_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 6, 4),
    _NetConfigHttpState_Type()
)
netConfigHttpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigHttpState.setStatus("current")


class _NetConfigHttpPort_Type(Integer32):
    """Custom type netConfigHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_NetConfigHttpPort_Type.__name__ = "Integer32"
_NetConfigHttpPort_Object = MibScalar
netConfigHttpPort = _NetConfigHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 6, 5),
    _NetConfigHttpPort_Type()
)
netConfigHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigHttpPort.setStatus("current")


class _NetConfigHttpsState_Type(Integer32):
    """Custom type netConfigHttpsState based on Integer32"""
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


_NetConfigHttpsState_Type.__name__ = "Integer32"
_NetConfigHttpsState_Object = MibScalar
netConfigHttpsState = _NetConfigHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 6, 6),
    _NetConfigHttpsState_Type()
)
netConfigHttpsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigHttpsState.setStatus("current")


class _NetConfigHttpsPort_Type(Integer32):
    """Custom type netConfigHttpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_NetConfigHttpsPort_Type.__name__ = "Integer32"
_NetConfigHttpsPort_Object = MibScalar
netConfigHttpsPort = _NetConfigHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 6, 7),
    _NetConfigHttpsPort_Type()
)
netConfigHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigHttpsPort.setStatus("current")


class _NetConfigDHCPState_Type(Integer32):
    """Custom type netConfigDHCPState based on Integer32"""
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


_NetConfigDHCPState_Type.__name__ = "Integer32"
_NetConfigDHCPState_Object = MibScalar
netConfigDHCPState = _NetConfigDHCPState_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 6, 8),
    _NetConfigDHCPState_Type()
)
netConfigDHCPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigDHCPState.setStatus("current")
_EnterpriseAPdot11_ObjectIdentity = ObjectIdentity
enterpriseAPdot11 = _EnterpriseAPdot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7)
)
_Dot11AuthenticationEntry_ObjectIdentity = ObjectIdentity
dot11AuthenticationEntry = _Dot11AuthenticationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 5)
)


class _Dot118021xState_Type(Integer32):
    """Custom type dot118021xState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("required", 2),
          ("supported", 1))
    )


_Dot118021xState_Type.__name__ = "Integer32"
_Dot118021xState_Object = MibScalar
dot118021xState = _Dot118021xState_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 5, 1),
    _Dot118021xState_Type()
)
dot118021xState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xState.setStatus("current")


class _Dot118021xBroadcastKeyRefreshRate_Type(Integer32):
    """Custom type dot118021xBroadcastKeyRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Dot118021xBroadcastKeyRefreshRate_Type.__name__ = "Integer32"
_Dot118021xBroadcastKeyRefreshRate_Object = MibScalar
dot118021xBroadcastKeyRefreshRate = _Dot118021xBroadcastKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 5, 2),
    _Dot118021xBroadcastKeyRefreshRate_Type()
)
dot118021xBroadcastKeyRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xBroadcastKeyRefreshRate.setStatus("current")


class _Dot118021xSessionKeyRefreshRate_Type(Integer32):
    """Custom type dot118021xSessionKeyRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Dot118021xSessionKeyRefreshRate_Type.__name__ = "Integer32"
_Dot118021xSessionKeyRefreshRate_Object = MibScalar
dot118021xSessionKeyRefreshRate = _Dot118021xSessionKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 5, 3),
    _Dot118021xSessionKeyRefreshRate_Type()
)
dot118021xSessionKeyRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xSessionKeyRefreshRate.setStatus("current")


class _Dot118021xReauthenticationTimeout_Type(Integer32):
    """Custom type dot118021xReauthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Dot118021xReauthenticationTimeout_Type.__name__ = "Integer32"
_Dot118021xReauthenticationTimeout_Object = MibScalar
dot118021xReauthenticationTimeout = _Dot118021xReauthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 5, 4),
    _Dot118021xReauthenticationTimeout_Type()
)
dot118021xReauthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xReauthenticationTimeout.setStatus("current")


class _Dot11MACAuthenticationType_Type(Integer32):
    """Custom type dot11MACAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("local", 1),
          ("radius", 2))
    )


_Dot11MACAuthenticationType_Type.__name__ = "Integer32"
_Dot11MACAuthenticationType_Object = MibScalar
dot11MACAuthenticationType = _Dot11MACAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 5, 5),
    _Dot11MACAuthenticationType_Type()
)
dot11MACAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MACAuthenticationType.setStatus("current")
_Dot11AuthenticationServerTable_Object = MibTable
dot11AuthenticationServerTable = _Dot11AuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 6)
)
if mibBuilder.loadTexts:
    dot11AuthenticationServerTable.setStatus("current")
_Dot11AuthenticationServerEntry_Object = MibTableRow
dot11AuthenticationServerEntry = _Dot11AuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 6, 1)
)
dot11AuthenticationServerEntry.setIndexNames(
    (0, "A3COM-PRIVATE-MIB", "dot11AuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    dot11AuthenticationServerEntry.setStatus("current")
_Dot11AuthenticationServerIndex_Type = Integer32
_Dot11AuthenticationServerIndex_Object = MibTableColumn
dot11AuthenticationServerIndex = _Dot11AuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 6, 1, 1),
    _Dot11AuthenticationServerIndex_Type()
)
dot11AuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11AuthenticationServerIndex.setStatus("current")
_Dot11AuthenticationServer_Type = IpAddress
_Dot11AuthenticationServer_Object = MibTableColumn
dot11AuthenticationServer = _Dot11AuthenticationServer_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 6, 1, 2),
    _Dot11AuthenticationServer_Type()
)
dot11AuthenticationServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationServer.setStatus("current")


class _Dot11AuthenticationPort_Type(Integer32):
    """Custom type dot11AuthenticationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Dot11AuthenticationPort_Type.__name__ = "Integer32"
_Dot11AuthenticationPort_Object = MibTableColumn
dot11AuthenticationPort = _Dot11AuthenticationPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 6, 1, 3),
    _Dot11AuthenticationPort_Type()
)
dot11AuthenticationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationPort.setStatus("current")


class _Dot11AuthenticationKey_Type(DisplayString):
    """Custom type dot11AuthenticationKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Dot11AuthenticationKey_Type.__name__ = "DisplayString"
_Dot11AuthenticationKey_Object = MibTableColumn
dot11AuthenticationKey = _Dot11AuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 6, 1, 4),
    _Dot11AuthenticationKey_Type()
)
dot11AuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationKey.setStatus("current")


class _Dot11AuthenticationRetransmit_Type(Integer32):
    """Custom type dot11AuthenticationRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Dot11AuthenticationRetransmit_Type.__name__ = "Integer32"
_Dot11AuthenticationRetransmit_Object = MibTableColumn
dot11AuthenticationRetransmit = _Dot11AuthenticationRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 6, 1, 5),
    _Dot11AuthenticationRetransmit_Type()
)
dot11AuthenticationRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationRetransmit.setStatus("current")


class _Dot11AuthenticationTimeout_Type(Integer32):
    """Custom type dot11AuthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Dot11AuthenticationTimeout_Type.__name__ = "Integer32"
_Dot11AuthenticationTimeout_Object = MibTableColumn
dot11AuthenticationTimeout = _Dot11AuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 6, 1, 6),
    _Dot11AuthenticationTimeout_Type()
)
dot11AuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationTimeout.setStatus("current")


class _Dot11AuthenticationAcctPort_Type(Integer32):
    """Custom type dot11AuthenticationAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Dot11AuthenticationAcctPort_Type.__name__ = "Integer32"
_Dot11AuthenticationAcctPort_Object = MibTableColumn
dot11AuthenticationAcctPort = _Dot11AuthenticationAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 6, 1, 7),
    _Dot11AuthenticationAcctPort_Type()
)
dot11AuthenticationAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationAcctPort.setStatus("current")


class _Dot11AuthenticationInterimUpdate_Type(Integer32):
    """Custom type dot11AuthenticationInterimUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_Dot11AuthenticationInterimUpdate_Type.__name__ = "Integer32"
_Dot11AuthenticationInterimUpdate_Object = MibTableColumn
dot11AuthenticationInterimUpdate = _Dot11AuthenticationInterimUpdate_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 6, 1, 8),
    _Dot11AuthenticationInterimUpdate_Type()
)
dot11AuthenticationInterimUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationInterimUpdate.setStatus("current")
_Dot11Filter_ObjectIdentity = ObjectIdentity
dot11Filter = _Dot11Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 7)
)


class _Dot11FilterDefault_Type(Integer32):
    """Custom type dot11FilterDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_Dot11FilterDefault_Type.__name__ = "Integer32"
_Dot11FilterDefault_Object = MibScalar
dot11FilterDefault = _Dot11FilterDefault_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 7, 1),
    _Dot11FilterDefault_Type()
)
dot11FilterDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FilterDefault.setStatus("current")
_Dot11FilterTable_Object = MibTable
dot11FilterTable = _Dot11FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 7, 2)
)
if mibBuilder.loadTexts:
    dot11FilterTable.setStatus("current")
_Dot11FilterEntry_Object = MibTableRow
dot11FilterEntry = _Dot11FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 7, 2, 1)
)
dot11FilterEntry.setIndexNames(
    (0, "A3COM-PRIVATE-MIB", "dot11FilterAddress"),
)
if mibBuilder.loadTexts:
    dot11FilterEntry.setStatus("current")
_Dot11FilterAddress_Type = MacAddress
_Dot11FilterAddress_Object = MibTableColumn
dot11FilterAddress = _Dot11FilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 7, 2, 1, 1),
    _Dot11FilterAddress_Type()
)
dot11FilterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11FilterAddress.setStatus("current")


class _Dot11FilterStatus_Type(Integer32):
    """Custom type dot11FilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 30),
          ("delete", 32),
          ("denied", 31))
    )


_Dot11FilterStatus_Type.__name__ = "Integer32"
_Dot11FilterStatus_Object = MibTableColumn
dot11FilterStatus = _Dot11FilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 7, 2, 1, 2),
    _Dot11FilterStatus_Type()
)
dot11FilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FilterStatus.setStatus("current")
_Dot11AuthenticationSupplicantTable_Object = MibTable
dot11AuthenticationSupplicantTable = _Dot11AuthenticationSupplicantTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 8)
)
if mibBuilder.loadTexts:
    dot11AuthenticationSupplicantTable.setStatus("current")
_Dot11AuthenticationSupplicantEntry_Object = MibTableRow
dot11AuthenticationSupplicantEntry = _Dot11AuthenticationSupplicantEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 8, 1)
)
dot11AuthenticationSupplicantEntry.setIndexNames(
    (0, "A3COM-PRIVATE-MIB", "dot118021xSuppIndex"),
)
if mibBuilder.loadTexts:
    dot11AuthenticationSupplicantEntry.setStatus("current")
_Dot118021xSuppIndex_Type = Integer32
_Dot118021xSuppIndex_Object = MibTableColumn
dot118021xSuppIndex = _Dot118021xSuppIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 8, 1, 1),
    _Dot118021xSuppIndex_Type()
)
dot118021xSuppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot118021xSuppIndex.setStatus("current")


class _Dot118021xSuppState_Type(Integer32):
    """Custom type dot118021xSuppState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Dot118021xSuppState_Type.__name__ = "Integer32"
_Dot118021xSuppState_Object = MibTableColumn
dot118021xSuppState = _Dot118021xSuppState_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 8, 1, 2),
    _Dot118021xSuppState_Type()
)
dot118021xSuppState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xSuppState.setStatus("current")


class _Dot118021xSuppUser_Type(DisplayString):
    """Custom type dot118021xSuppUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Dot118021xSuppUser_Type.__name__ = "DisplayString"
_Dot118021xSuppUser_Object = MibTableColumn
dot118021xSuppUser = _Dot118021xSuppUser_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 8, 1, 3),
    _Dot118021xSuppUser_Type()
)
dot118021xSuppUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xSuppUser.setStatus("current")


class _Dot118021xSuppPasswd_Type(DisplayString):
    """Custom type dot118021xSuppPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Dot118021xSuppPasswd_Type.__name__ = "DisplayString"
_Dot118021xSuppPasswd_Object = MibTableColumn
dot118021xSuppPasswd = _Dot118021xSuppPasswd_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 7, 8, 1, 4),
    _Dot118021xSuppPasswd_Type()
)
dot118021xSuppPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xSuppPasswd.setStatus("current")
_EnterpriseApAdmin_ObjectIdentity = ObjectIdentity
enterpriseApAdmin = _EnterpriseApAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 8)
)


class _EnterpriseApAdminUser_Type(DisplayString):
    """Custom type enterpriseApAdminUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 16),
    )


_EnterpriseApAdminUser_Type.__name__ = "DisplayString"
_EnterpriseApAdminUser_Object = MibScalar
enterpriseApAdminUser = _EnterpriseApAdminUser_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 8, 1),
    _EnterpriseApAdminUser_Type()
)
enterpriseApAdminUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApAdminUser.setStatus("current")


class _EnterpriseApAdminPassword_Type(DisplayString):
    """Custom type enterpriseApAdminPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 16),
    )


_EnterpriseApAdminPassword_Type.__name__ = "DisplayString"
_EnterpriseApAdminPassword_Object = MibScalar
enterpriseApAdminPassword = _EnterpriseApAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 8, 2),
    _EnterpriseApAdminPassword_Type()
)
enterpriseApAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApAdminPassword.setStatus("current")
_EnterpriseApSecurity_ObjectIdentity = ObjectIdentity
enterpriseApSecurity = _EnterpriseApSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9)
)
_EnterpriseApSecurityTable_Object = MibTable
enterpriseApSecurityTable = _EnterpriseApSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1)
)
if mibBuilder.loadTexts:
    enterpriseApSecurityTable.setStatus("current")
_EnterpriseApSecurityEntry_Object = MibTableRow
enterpriseApSecurityEntry = _EnterpriseApSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1, 1)
)
enterpriseApSecurityEntry.setIndexNames(
    (0, "A3COM-PRIVATE-MIB", "enterpriseApSecurityIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApSecurityEntry.setStatus("current")
_EnterpriseApSecurityIndex_Type = Integer32
_EnterpriseApSecurityIndex_Object = MibTableColumn
enterpriseApSecurityIndex = _EnterpriseApSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1, 1, 1),
    _EnterpriseApSecurityIndex_Type()
)
enterpriseApSecurityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApSecurityIndex.setStatus("current")


class _EnterpriseApSecurityAuthType_Type(Integer32):
    """Custom type enterpriseApSecurityAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("shared", 1))
    )


_EnterpriseApSecurityAuthType_Type.__name__ = "Integer32"
_EnterpriseApSecurityAuthType_Object = MibTableColumn
enterpriseApSecurityAuthType = _EnterpriseApSecurityAuthType_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1, 1, 2),
    _EnterpriseApSecurityAuthType_Type()
)
enterpriseApSecurityAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityAuthType.setStatus("current")


class _EnterpriseApSecuritySharedKeyLen_Type(Integer32):
    """Custom type enterpriseApSecuritySharedKeyLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("oneHundredFiftyTwo", 3),
          ("oneHundredTwentyEight", 2),
          ("sixtyFour", 1))
    )


_EnterpriseApSecuritySharedKeyLen_Type.__name__ = "Integer32"
_EnterpriseApSecuritySharedKeyLen_Object = MibTableColumn
enterpriseApSecuritySharedKeyLen = _EnterpriseApSecuritySharedKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1, 1, 3),
    _EnterpriseApSecuritySharedKeyLen_Type()
)
enterpriseApSecuritySharedKeyLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSecuritySharedKeyLen.setStatus("current")


class _EnterpriseApSecurityWPAMode_Type(Integer32):
    """Custom type enterpriseApSecurityWPAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("required", 1),
          ("supported", 0))
    )


_EnterpriseApSecurityWPAMode_Type.__name__ = "Integer32"
_EnterpriseApSecurityWPAMode_Object = MibTableColumn
enterpriseApSecurityWPAMode = _EnterpriseApSecurityWPAMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1, 1, 4),
    _EnterpriseApSecurityWPAMode_Type()
)
enterpriseApSecurityWPAMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWPAMode.setStatus("current")


class _EnterpriseApSecurityWPAKeyType_Type(Integer32):
    """Custom type enterpriseApSecurityWPAKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 0),
          ("presharedkey", 1))
    )


_EnterpriseApSecurityWPAKeyType_Type.__name__ = "Integer32"
_EnterpriseApSecurityWPAKeyType_Object = MibTableColumn
enterpriseApSecurityWPAKeyType = _EnterpriseApSecurityWPAKeyType_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1, 1, 5),
    _EnterpriseApSecurityWPAKeyType_Type()
)
enterpriseApSecurityWPAKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWPAKeyType.setStatus("current")


class _EnterpriseApSecurityWPACipher_Type(Integer32):
    """Custom type enterpriseApSecurityWPACipher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("tkip", 1),
          ("wep", 0))
    )


_EnterpriseApSecurityWPACipher_Type.__name__ = "Integer32"
_EnterpriseApSecurityWPACipher_Object = MibTableColumn
enterpriseApSecurityWPACipher = _EnterpriseApSecurityWPACipher_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1, 1, 6),
    _EnterpriseApSecurityWPACipher_Type()
)
enterpriseApSecurityWPACipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWPACipher.setStatus("current")


class _EnterpriseApSecurityWPAPSKType_Type(Integer32):
    """Custom type enterpriseApSecurityWPAPSKType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alphanumeric", 1),
          ("hex", 0))
    )


_EnterpriseApSecurityWPAPSKType_Type.__name__ = "Integer32"
_EnterpriseApSecurityWPAPSKType_Object = MibTableColumn
enterpriseApSecurityWPAPSKType = _EnterpriseApSecurityWPAPSKType_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1, 1, 7),
    _EnterpriseApSecurityWPAPSKType_Type()
)
enterpriseApSecurityWPAPSKType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWPAPSKType.setStatus("current")


class _EnterpriseApSecurityWPAPSK_Type(DisplayString):
    """Custom type enterpriseApSecurityWPAPSK based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EnterpriseApSecurityWPAPSK_Type.__name__ = "DisplayString"
_EnterpriseApSecurityWPAPSK_Object = MibTableColumn
enterpriseApSecurityWPAPSK = _EnterpriseApSecurityWPAPSK_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1, 1, 8),
    _EnterpriseApSecurityWPAPSK_Type()
)
enterpriseApSecurityWPAPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWPAPSK.setStatus("current")


class _EnterpriseApSecurityWEPKeyType_Type(Integer32):
    """Custom type enterpriseApSecurityWEPKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alphanumeric", 1),
          ("hexadecimal", 0))
    )


_EnterpriseApSecurityWEPKeyType_Type.__name__ = "Integer32"
_EnterpriseApSecurityWEPKeyType_Object = MibTableColumn
enterpriseApSecurityWEPKeyType = _EnterpriseApSecurityWEPKeyType_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1, 1, 9),
    _EnterpriseApSecurityWEPKeyType_Type()
)
enterpriseApSecurityWEPKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWEPKeyType.setStatus("current")
_EnterpriseApSecurityWEPEnabled_Type = TruthValue
_EnterpriseApSecurityWEPEnabled_Object = MibTableColumn
enterpriseApSecurityWEPEnabled = _EnterpriseApSecurityWEPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 9, 1, 1, 10),
    _EnterpriseApSecurityWEPEnabled_Type()
)
enterpriseApSecurityWEPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWEPEnabled.setStatus("current")
_EnterpriseApRadio_ObjectIdentity = ObjectIdentity
enterpriseApRadio = _EnterpriseApRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10)
)
_EnterpriseApRadioTable_Object = MibTable
enterpriseApRadioTable = _EnterpriseApRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1)
)
if mibBuilder.loadTexts:
    enterpriseApRadioTable.setStatus("current")
_EnterpriseApRadioEntry_Object = MibTableRow
enterpriseApRadioEntry = _EnterpriseApRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1)
)
enterpriseApRadioEntry.setIndexNames(
    (0, "A3COM-PRIVATE-MIB", "enterpriseApRadioIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApRadioEntry.setStatus("current")
_EnterpriseApRadioIndex_Type = Integer32
_EnterpriseApRadioIndex_Object = MibTableColumn
enterpriseApRadioIndex = _EnterpriseApRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1, 1),
    _EnterpriseApRadioIndex_Type()
)
enterpriseApRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApRadioIndex.setStatus("current")


class _EnterpriseApRadioAutoChannel_Type(Integer32):
    """Custom type enterpriseApRadioAutoChannel based on Integer32"""
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


_EnterpriseApRadioAutoChannel_Type.__name__ = "Integer32"
_EnterpriseApRadioAutoChannel_Object = MibTableColumn
enterpriseApRadioAutoChannel = _EnterpriseApRadioAutoChannel_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1, 2),
    _EnterpriseApRadioAutoChannel_Type()
)
enterpriseApRadioAutoChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioAutoChannel.setStatus("current")


class _EnterpriseApRadioTransmitPower_Type(Integer32):
    """Custom type enterpriseApRadioTransmitPower based on Integer32"""
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
        *(("eighth", 5),
          ("full", 1),
          ("half", 2),
          ("middle", 3),
          ("min", 6),
          ("quarter", 4))
    )


_EnterpriseApRadioTransmitPower_Type.__name__ = "Integer32"
_EnterpriseApRadioTransmitPower_Object = MibTableColumn
enterpriseApRadioTransmitPower = _EnterpriseApRadioTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1, 3),
    _EnterpriseApRadioTransmitPower_Type()
)
enterpriseApRadioTransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioTransmitPower.setStatus("current")


class _EnterpriseApRadioTurboMode_Type(Integer32):
    """Custom type enterpriseApRadioTurboMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("invalid", 3))
    )


_EnterpriseApRadioTurboMode_Type.__name__ = "Integer32"
_EnterpriseApRadioTurboMode_Object = MibTableColumn
enterpriseApRadioTurboMode = _EnterpriseApRadioTurboMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1, 4),
    _EnterpriseApRadioTurboMode_Type()
)
enterpriseApRadioTurboMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioTurboMode.setStatus("current")


class _EnterpriseApRadioDataRate_Type(Integer32):
    """Custom type enterpriseApRadioDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              9,
              11,
              12,
              18,
              24,
              36,
              48,
              54,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 255),
          ("eighteenMbps", 18),
          ("elevenMbps", 11),
          ("fiftyFourMbps", 54),
          ("fiveAndHalfMbps", 5),
          ("fourtyEightMbps", 48),
          ("nineMbps", 9),
          ("oneMbps", 1),
          ("sixMbps", 6),
          ("thirtySixMbps", 36),
          ("twelveMbps", 12),
          ("twentyFourMbps", 24),
          ("twoMbps", 2))
    )


_EnterpriseApRadioDataRate_Type.__name__ = "Integer32"
_EnterpriseApRadioDataRate_Object = MibTableColumn
enterpriseApRadioDataRate = _EnterpriseApRadioDataRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1, 5),
    _EnterpriseApRadioDataRate_Type()
)
enterpriseApRadioDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioDataRate.setStatus("current")


class _EnterpriseApRadioGMode_Type(Integer32):
    """Custom type enterpriseApRadioGMode based on Integer32"""
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
        *(("bOnly", 1),
          ("bg", 3),
          ("gOnly", 2),
          ("invalid", 4))
    )


_EnterpriseApRadioGMode_Type.__name__ = "Integer32"
_EnterpriseApRadioGMode_Object = MibTableColumn
enterpriseApRadioGMode = _EnterpriseApRadioGMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1, 6),
    _EnterpriseApRadioGMode_Type()
)
enterpriseApRadioGMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioGMode.setStatus("current")


class _EnterpriseApRadioAntennaMode_Type(Integer32):
    """Custom type enterpriseApRadioAntennaMode based on Integer32"""
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
        *(("both", 1),
          ("invalid", 4),
          ("left", 2),
          ("right", 3))
    )


_EnterpriseApRadioAntennaMode_Type.__name__ = "Integer32"
_EnterpriseApRadioAntennaMode_Object = MibTableColumn
enterpriseApRadioAntennaMode = _EnterpriseApRadioAntennaMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1, 7),
    _EnterpriseApRadioAntennaMode_Type()
)
enterpriseApRadioAntennaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioAntennaMode.setStatus("current")


class _RogueApState_Type(Integer32):
    """Custom type rogueApState based on Integer32"""
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


_RogueApState_Type.__name__ = "Integer32"
_RogueApState_Object = MibTableColumn
rogueApState = _RogueApState_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1, 8),
    _RogueApState_Type()
)
rogueApState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueApState.setStatus("current")


class _RogueApInterval_Type(Integer32):
    """Custom type rogueApInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 10080),
    )


_RogueApInterval_Type.__name__ = "Integer32"
_RogueApInterval_Object = MibTableColumn
rogueApInterval = _RogueApInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1, 9),
    _RogueApInterval_Type()
)
rogueApInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueApInterval.setStatus("current")


class _RogueApDuration_Type(Integer32):
    """Custom type rogueApDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_RogueApDuration_Type.__name__ = "Integer32"
_RogueApDuration_Object = MibTableColumn
rogueApDuration = _RogueApDuration_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1, 10),
    _RogueApDuration_Type()
)
rogueApDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueApDuration.setStatus("current")


class _RogueApScanNow_Type(Integer32):
    """Custom type rogueApScanNow based on Integer32"""
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


_RogueApScanNow_Type.__name__ = "Integer32"
_RogueApScanNow_Object = MibTableColumn
rogueApScanNow = _RogueApScanNow_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 1, 1, 11),
    _RogueApScanNow_Type()
)
rogueApScanNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueApScanNow.setStatus("current")
_EnterpriseApVapRadioTable_Object = MibTable
enterpriseApVapRadioTable = _EnterpriseApVapRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 2)
)
if mibBuilder.loadTexts:
    enterpriseApVapRadioTable.setStatus("current")
_EnterpriseApVapRadioEntry_Object = MibTableRow
enterpriseApVapRadioEntry = _EnterpriseApVapRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 2, 1)
)
enterpriseApVapRadioEntry.setIndexNames(
    (0, "A3COM-PRIVATE-MIB", "enterpriseApVapRadioIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApVapRadioEntry.setStatus("current")
_EnterpriseApVapRadioIndex_Type = Integer32
_EnterpriseApVapRadioIndex_Object = MibTableColumn
enterpriseApVapRadioIndex = _EnterpriseApVapRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 2, 1, 1),
    _EnterpriseApVapRadioIndex_Type()
)
enterpriseApVapRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApVapRadioIndex.setStatus("current")


class _EnterpriseApVapRadioState_Type(Integer32):
    """Custom type enterpriseApVapRadioState based on Integer32"""
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


_EnterpriseApVapRadioState_Type.__name__ = "Integer32"
_EnterpriseApVapRadioState_Object = MibTableColumn
enterpriseApVapRadioState = _EnterpriseApVapRadioState_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 2, 1, 2),
    _EnterpriseApVapRadioState_Type()
)
enterpriseApVapRadioState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVapRadioState.setStatus("current")


class _EnterpriseApVapRadioClosedSystem_Type(Integer32):
    """Custom type enterpriseApVapRadioClosedSystem based on Integer32"""
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


_EnterpriseApVapRadioClosedSystem_Type.__name__ = "Integer32"
_EnterpriseApVapRadioClosedSystem_Object = MibTableColumn
enterpriseApVapRadioClosedSystem = _EnterpriseApVapRadioClosedSystem_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 2, 1, 3),
    _EnterpriseApVapRadioClosedSystem_Type()
)
enterpriseApVapRadioClosedSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVapRadioClosedSystem.setStatus("current")


class _EnterpriseApVapRadioMaxAssoc_Type(Integer32):
    """Custom type enterpriseApVapRadioMaxAssoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EnterpriseApVapRadioMaxAssoc_Type.__name__ = "Integer32"
_EnterpriseApVapRadioMaxAssoc_Object = MibTableColumn
enterpriseApVapRadioMaxAssoc = _EnterpriseApVapRadioMaxAssoc_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 2, 1, 4),
    _EnterpriseApVapRadioMaxAssoc_Type()
)
enterpriseApVapRadioMaxAssoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVapRadioMaxAssoc.setStatus("current")


class _EnterpriseApVapRadioTransmitKey_Type(Integer32):
    """Custom type enterpriseApVapRadioTransmitKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnterpriseApVapRadioTransmitKey_Type.__name__ = "Integer32"
_EnterpriseApVapRadioTransmitKey_Object = MibTableColumn
enterpriseApVapRadioTransmitKey = _EnterpriseApVapRadioTransmitKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 2, 1, 5),
    _EnterpriseApVapRadioTransmitKey_Type()
)
enterpriseApVapRadioTransmitKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVapRadioTransmitKey.setStatus("current")


class _EnterpriseApVapRadioDescription_Type(DisplayString):
    """Custom type enterpriseApVapRadioDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnterpriseApVapRadioDescription_Type.__name__ = "DisplayString"
_EnterpriseApVapRadioDescription_Object = MibTableColumn
enterpriseApVapRadioDescription = _EnterpriseApVapRadioDescription_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 2, 1, 6),
    _EnterpriseApVapRadioDescription_Type()
)
enterpriseApVapRadioDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVapRadioDescription.setStatus("current")
_RadioWdsTable_Object = MibTable
radioWdsTable = _RadioWdsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 3)
)
if mibBuilder.loadTexts:
    radioWdsTable.setStatus("current")
_RadioWdsEntry_Object = MibTableRow
radioWdsEntry = _RadioWdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 3, 1)
)
radioWdsEntry.setIndexNames(
    (0, "A3COM-PRIVATE-MIB", "enterpriseApRadioIndex"),
)
if mibBuilder.loadTexts:
    radioWdsEntry.setStatus("current")


class _WdsApRole_Type(Integer32):
    """Custom type wdsApRole based on Integer32"""
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
        *(("roleAp", 1),
          ("roleBridge", 4),
          ("roleBridgeMaster", 2),
          ("roleRepeater", 3))
    )


_WdsApRole_Type.__name__ = "Integer32"
_WdsApRole_Object = MibTableColumn
wdsApRole = _WdsApRole_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 3, 1, 1),
    _WdsApRole_Type()
)
wdsApRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsApRole.setStatus("current")
_RadioWdsPeerTable_Object = MibTable
radioWdsPeerTable = _RadioWdsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 4)
)
if mibBuilder.loadTexts:
    radioWdsPeerTable.setStatus("current")
_RadioWdsPeerEntry_Object = MibTableRow
radioWdsPeerEntry = _RadioWdsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 4, 1)
)
radioWdsPeerEntry.setIndexNames(
    (0, "A3COM-PRIVATE-MIB", "enterpriseApRadioIndex"),
    (0, "A3COM-PRIVATE-MIB", "wdsPeerIndex"),
)
if mibBuilder.loadTexts:
    radioWdsPeerEntry.setStatus("current")
_WdsPeerIndex_Type = Integer32
_WdsPeerIndex_Object = MibTableColumn
wdsPeerIndex = _WdsPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 4, 1, 1),
    _WdsPeerIndex_Type()
)
wdsPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wdsPeerIndex.setStatus("current")


class _WdsPeerBssid_Type(DisplayString):
    """Custom type wdsPeerBssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_WdsPeerBssid_Type.__name__ = "DisplayString"
_WdsPeerBssid_Object = MibTableColumn
wdsPeerBssid = _WdsPeerBssid_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 10, 4, 1, 2),
    _WdsPeerBssid_Type()
)
wdsPeerBssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsPeerBssid.setStatus("current")
_EnterpriseApWebRedirection_ObjectIdentity = ObjectIdentity
enterpriseApWebRedirection = _EnterpriseApWebRedirection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 11)
)


class _WebRedirectionEnabled_Type(Integer32):
    """Custom type webRedirectionEnabled based on Integer32"""
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


_WebRedirectionEnabled_Type.__name__ = "Integer32"
_WebRedirectionEnabled_Object = MibScalar
webRedirectionEnabled = _WebRedirectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 11, 1),
    _WebRedirectionEnabled_Type()
)
webRedirectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webRedirectionEnabled.setStatus("current")
_EnterpriseApProxyArp_ObjectIdentity = ObjectIdentity
enterpriseApProxyArp = _EnterpriseApProxyArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 12)
)


class _ProxyArpEnabled_Type(Integer32):
    """Custom type proxyArpEnabled based on Integer32"""
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


_ProxyArpEnabled_Type.__name__ = "Integer32"
_ProxyArpEnabled_Object = MibScalar
proxyArpEnabled = _ProxyArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 12, 1),
    _ProxyArpEnabled_Type()
)
proxyArpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyArpEnabled.setStatus("current")
_EnterpriseApRogueAp_ObjectIdentity = ObjectIdentity
enterpriseApRogueAp = _EnterpriseApRogueAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 13)
)
_RogueApDetectionTable_Object = MibTable
rogueApDetectionTable = _RogueApDetectionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 13, 1)
)
if mibBuilder.loadTexts:
    rogueApDetectionTable.setStatus("current")
_RogueApEntry_Object = MibTableRow
rogueApEntry = _RogueApEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 13, 1, 1)
)
rogueApEntry.setIndexNames(
    (0, "A3COM-PRIVATE-MIB", "rogueApIndex"),
)
if mibBuilder.loadTexts:
    rogueApEntry.setStatus("current")


class _RogueApIndex_Type(Integer32):
    """Custom type rogueApIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_RogueApIndex_Type.__name__ = "Integer32"
_RogueApIndex_Object = MibTableColumn
rogueApIndex = _RogueApIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 13, 1, 1, 1),
    _RogueApIndex_Type()
)
rogueApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rogueApIndex.setStatus("current")


class _RogueApBssid_Type(DisplayString):
    """Custom type rogueApBssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RogueApBssid_Type.__name__ = "DisplayString"
_RogueApBssid_Object = MibTableColumn
rogueApBssid = _RogueApBssid_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 13, 1, 1, 2),
    _RogueApBssid_Type()
)
rogueApBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueApBssid.setStatus("current")


class _RogueApSsid_Type(DisplayString):
    """Custom type rogueApSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RogueApSsid_Type.__name__ = "DisplayString"
_RogueApSsid_Object = MibTableColumn
rogueApSsid = _RogueApSsid_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 13, 1, 1, 3),
    _RogueApSsid_Type()
)
rogueApSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueApSsid.setStatus("current")
_RogueApPortNumber_Type = Integer32
_RogueApPortNumber_Object = MibTableColumn
rogueApPortNumber = _RogueApPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 13, 1, 1, 4),
    _RogueApPortNumber_Type()
)
rogueApPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueApPortNumber.setStatus("current")
_RogueApChannelNumber_Type = Integer32
_RogueApChannelNumber_Object = MibTableColumn
rogueApChannelNumber = _RogueApChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 13, 1, 1, 5),
    _RogueApChannelNumber_Type()
)
rogueApChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueApChannelNumber.setStatus("current")
_RogueApRSSIValue_Type = Integer32
_RogueApRSSIValue_Object = MibTableColumn
rogueApRSSIValue = _RogueApRSSIValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 13, 1, 1, 6),
    _RogueApRSSIValue_Type()
)
rogueApRSSIValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rogueApRSSIValue.setStatus("current")
_ApNotificationTrapTree_ObjectIdentity = ObjectIdentity
apNotificationTrapTree = _ApNotificationTrapTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100)
)
_ApNotificationObjects_ObjectIdentity = ObjectIdentity
apNotificationObjects = _ApNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 1)
)
_ApNotificationDot11MacAddr_Type = MacAddress
_ApNotificationDot11MacAddr_Object = MibScalar
apNotificationDot11MacAddr = _ApNotificationDot11MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 1, 1),
    _ApNotificationDot11MacAddr_Type()
)
apNotificationDot11MacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apNotificationDot11MacAddr.setStatus("current")
_ApNotificationDot11Station_Type = MacAddress
_ApNotificationDot11Station_Object = MibScalar
apNotificationDot11Station = _ApNotificationDot11Station_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 1, 2),
    _ApNotificationDot11Station_Type()
)
apNotificationDot11Station.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apNotificationDot11Station.setStatus("current")


class _ApNotificationDot11RequestType_Type(Integer32):
    """Custom type apNotificationDot11RequestType based on Integer32"""
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
        *(("association", 2),
          ("authentication", 4),
          ("reAssociation", 3),
          ("unknown", 1))
    )


_ApNotificationDot11RequestType_Type.__name__ = "Integer32"
_ApNotificationDot11RequestType_Object = MibScalar
apNotificationDot11RequestType = _ApNotificationDot11RequestType_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 1, 3),
    _ApNotificationDot11RequestType_Type()
)
apNotificationDot11RequestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apNotificationDot11RequestType.setStatus("current")


class _ApNotificationDot11ReasonCode_Type(Integer32):
    """Custom type apNotificationDot11ReasonCode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("challengeTextMismatch", 9),
          ("internalError", 3),
          ("invalidFrameLngth", 6),
          ("invalidModeOrState", 1),
          ("outOfSequenceFrame", 4),
          ("unAuthenticatedStation", 2),
          ("unsupportedAlgorithm", 5),
          ("wepNotAllowed", 8),
          ("wepRequiredOnAP", 7))
    )


_ApNotificationDot11ReasonCode_Type.__name__ = "Integer32"
_ApNotificationDot11ReasonCode_Object = MibScalar
apNotificationDot11ReasonCode = _ApNotificationDot11ReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 1, 4),
    _ApNotificationDot11ReasonCode_Type()
)
apNotificationDot11ReasonCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apNotificationDot11ReasonCode.setStatus("current")
_ApNotificationDot11IpAddress_Type = IpAddress
_ApNotificationDot11IpAddress_Object = MibScalar
apNotificationDot11IpAddress = _ApNotificationDot11IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 1, 5),
    _ApNotificationDot11IpAddress_Type()
)
apNotificationDot11IpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apNotificationDot11IpAddress.setStatus("current")
_ApNotificationDot11AuthenticatorMacAddr_Type = MacAddress
_ApNotificationDot11AuthenticatorMacAddr_Object = MibScalar
apNotificationDot11AuthenticatorMacAddr = _ApNotificationDot11AuthenticatorMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 1, 6),
    _ApNotificationDot11AuthenticatorMacAddr_Type()
)
apNotificationDot11AuthenticatorMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apNotificationDot11AuthenticatorMacAddr.setStatus("current")
_ApNotificationTrapObjects_ObjectIdentity = ObjectIdentity
apNotificationTrapObjects = _ApNotificationTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2)
)

# Managed Objects groups


# Notification objects

sysSystemUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 1)
)
if mibBuilder.loadTexts:
    sysSystemUp.setStatus(
        "current"
    )

sysSystemDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 2)
)
if mibBuilder.loadTexts:
    sysSystemDown.setStatus(
        "current"
    )

sysRadiusServerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 3)
)
if mibBuilder.loadTexts:
    sysRadiusServerChanged.setStatus(
        "current"
    )

dot11StationAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 4)
)
dot11StationAssociation.setObjects(
    ("A3COM-PRIVATE-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot11StationAssociation.setStatus(
        "current"
    )

dot11StationReAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 5)
)
dot11StationReAssociation.setObjects(
    ("A3COM-PRIVATE-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot11StationReAssociation.setStatus(
        "current"
    )

dot11StationAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 6)
)
dot11StationAuthentication.setObjects(
    ("A3COM-PRIVATE-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot11StationAuthentication.setStatus(
        "current"
    )

dot11StationRequestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 7)
)
dot11StationRequestFail.setObjects(
      *(("A3COM-PRIVATE-MIB", "apNotificationDot11Station"),
        ("A3COM-PRIVATE-MIB", "apNotificationDot11RequestType"),
        ("A3COM-PRIVATE-MIB", "apNotificationDot11ReasonCode"))
)
if mibBuilder.loadTexts:
    dot11StationRequestFail.setStatus(
        "current"
    )

dot11InterfaceAGFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 8)
)
if mibBuilder.loadTexts:
    dot11InterfaceAGFail.setStatus(
        "current"
    )

dot1xMacAddrAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 9)
)
dot1xMacAddrAuthSuccess.setObjects(
    ("A3COM-PRIVATE-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot1xMacAddrAuthSuccess.setStatus(
        "current"
    )

dot1xMacAddrAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 10)
)
dot1xMacAddrAuthFail.setObjects(
    ("A3COM-PRIVATE-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot1xMacAddrAuthFail.setStatus(
        "current"
    )

dot1xAuthNotInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 11)
)
dot1xAuthNotInitiated.setObjects(
    ("A3COM-PRIVATE-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot1xAuthNotInitiated.setStatus(
        "current"
    )

dot1xAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 12)
)
dot1xAuthSuccess.setObjects(
    ("A3COM-PRIVATE-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot1xAuthSuccess.setStatus(
        "current"
    )

dot1xAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 13)
)
dot1xAuthFail.setObjects(
    ("A3COM-PRIVATE-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    dot1xAuthFail.setStatus(
        "current"
    )

localMacAddrAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 14)
)
localMacAddrAuthSuccess.setObjects(
    ("A3COM-PRIVATE-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    localMacAddrAuthSuccess.setStatus(
        "current"
    )

localMacAddrAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 15)
)
localMacAddrAuthFail.setObjects(
    ("A3COM-PRIVATE-MIB", "apNotificationDot11Station")
)
if mibBuilder.loadTexts:
    localMacAddrAuthFail.setStatus(
        "current"
    )

pppLogonFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 16)
)
if mibBuilder.loadTexts:
    pppLogonFail.setStatus(
        "current"
    )

iappStationRoamedFrom = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 17)
)
iappStationRoamedFrom.setObjects(
      *(("A3COM-PRIVATE-MIB", "apNotificationDot11Station"),
        ("A3COM-PRIVATE-MIB", "apNotificationDot11IpAddress"))
)
if mibBuilder.loadTexts:
    iappStationRoamedFrom.setStatus(
        "current"
    )

iappStationRoamedTo = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 18)
)
iappStationRoamedTo.setObjects(
      *(("A3COM-PRIVATE-MIB", "apNotificationDot11Station"),
        ("A3COM-PRIVATE-MIB", "apNotificationDot11IpAddress"))
)
if mibBuilder.loadTexts:
    iappStationRoamedTo.setStatus(
        "current"
    )

iappContextDataSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 19)
)
iappContextDataSent.setObjects(
      *(("A3COM-PRIVATE-MIB", "apNotificationDot11Station"),
        ("A3COM-PRIVATE-MIB", "apNotificationDot11IpAddress"))
)
if mibBuilder.loadTexts:
    iappContextDataSent.setStatus(
        "current"
    )

sntpServerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 35, 8, 100, 2, 20)
)
if mibBuilder.loadTexts:
    sntpServerFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-PRIVATE-MIB",
    **{"a3Com": a3Com,
       "wlan-mib": wlan_mib,
       "rivet": rivet,
       "enterpriseApSys": enterpriseApSys,
       "swHardwareVer": swHardwareVer,
       "swBootRomVer": swBootRomVer,
       "swOpCodeVer": swOpCodeVer,
       "swSerialNumber": swSerialNumber,
       "enterpriseApLineMgnt": enterpriseApLineMgnt,
       "lineTable": lineTable,
       "lineEntry": lineEntry,
       "lineIndex": lineIndex,
       "lineDataBits": lineDataBits,
       "lineParity": lineParity,
       "lineSpeed": lineSpeed,
       "lineStopBits": lineStopBits,
       "enterpriseApPortMgnt": enterpriseApPortMgnt,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portName": portName,
       "portType": portType,
       "portSpeedDpxCfg": portSpeedDpxCfg,
       "portFlowCtrlCfg": portFlowCtrlCfg,
       "portCapabilities": portCapabilities,
       "portAutonegotiation": portAutonegotiation,
       "portSpeedDpxStatus": portSpeedDpxStatus,
       "portFlowCtrlStatus": portFlowCtrlStatus,
       "enterpriseApFileTransferMgt": enterpriseApFileTransferMgt,
       "transferType": transferType,
       "fileType": fileType,
       "srcFile": srcFile,
       "destFile": destFile,
       "fileServer": fileServer,
       "userName": userName,
       "password": password,
       "status": status,
       "transferStart": transferStart,
       "enterpriseApResetMgt": enterpriseApResetMgt,
       "restartOpCodeFile": restartOpCodeFile,
       "restartControl": restartControl,
       "enterpriseApIpMgt": enterpriseApIpMgt,
       "netConfigIPAddress": netConfigIPAddress,
       "netConfigSubnetMask": netConfigSubnetMask,
       "netConfigDefaultGateway": netConfigDefaultGateway,
       "netConfigHttpState": netConfigHttpState,
       "netConfigHttpPort": netConfigHttpPort,
       "netConfigHttpsState": netConfigHttpsState,
       "netConfigHttpsPort": netConfigHttpsPort,
       "netConfigDHCPState": netConfigDHCPState,
       "enterpriseAPdot11": enterpriseAPdot11,
       "dot11AuthenticationEntry": dot11AuthenticationEntry,
       "dot118021xState": dot118021xState,
       "dot118021xBroadcastKeyRefreshRate": dot118021xBroadcastKeyRefreshRate,
       "dot118021xSessionKeyRefreshRate": dot118021xSessionKeyRefreshRate,
       "dot118021xReauthenticationTimeout": dot118021xReauthenticationTimeout,
       "dot11MACAuthenticationType": dot11MACAuthenticationType,
       "dot11AuthenticationServerTable": dot11AuthenticationServerTable,
       "dot11AuthenticationServerEntry": dot11AuthenticationServerEntry,
       "dot11AuthenticationServerIndex": dot11AuthenticationServerIndex,
       "dot11AuthenticationServer": dot11AuthenticationServer,
       "dot11AuthenticationPort": dot11AuthenticationPort,
       "dot11AuthenticationKey": dot11AuthenticationKey,
       "dot11AuthenticationRetransmit": dot11AuthenticationRetransmit,
       "dot11AuthenticationTimeout": dot11AuthenticationTimeout,
       "dot11AuthenticationAcctPort": dot11AuthenticationAcctPort,
       "dot11AuthenticationInterimUpdate": dot11AuthenticationInterimUpdate,
       "dot11Filter": dot11Filter,
       "dot11FilterDefault": dot11FilterDefault,
       "dot11FilterTable": dot11FilterTable,
       "dot11FilterEntry": dot11FilterEntry,
       "dot11FilterAddress": dot11FilterAddress,
       "dot11FilterStatus": dot11FilterStatus,
       "dot11AuthenticationSupplicantTable": dot11AuthenticationSupplicantTable,
       "dot11AuthenticationSupplicantEntry": dot11AuthenticationSupplicantEntry,
       "dot118021xSuppIndex": dot118021xSuppIndex,
       "dot118021xSuppState": dot118021xSuppState,
       "dot118021xSuppUser": dot118021xSuppUser,
       "dot118021xSuppPasswd": dot118021xSuppPasswd,
       "enterpriseApAdmin": enterpriseApAdmin,
       "enterpriseApAdminUser": enterpriseApAdminUser,
       "enterpriseApAdminPassword": enterpriseApAdminPassword,
       "enterpriseApSecurity": enterpriseApSecurity,
       "enterpriseApSecurityTable": enterpriseApSecurityTable,
       "enterpriseApSecurityEntry": enterpriseApSecurityEntry,
       "enterpriseApSecurityIndex": enterpriseApSecurityIndex,
       "enterpriseApSecurityAuthType": enterpriseApSecurityAuthType,
       "enterpriseApSecuritySharedKeyLen": enterpriseApSecuritySharedKeyLen,
       "enterpriseApSecurityWPAMode": enterpriseApSecurityWPAMode,
       "enterpriseApSecurityWPAKeyType": enterpriseApSecurityWPAKeyType,
       "enterpriseApSecurityWPACipher": enterpriseApSecurityWPACipher,
       "enterpriseApSecurityWPAPSKType": enterpriseApSecurityWPAPSKType,
       "enterpriseApSecurityWPAPSK": enterpriseApSecurityWPAPSK,
       "enterpriseApSecurityWEPKeyType": enterpriseApSecurityWEPKeyType,
       "enterpriseApSecurityWEPEnabled": enterpriseApSecurityWEPEnabled,
       "enterpriseApRadio": enterpriseApRadio,
       "enterpriseApRadioTable": enterpriseApRadioTable,
       "enterpriseApRadioEntry": enterpriseApRadioEntry,
       "enterpriseApRadioIndex": enterpriseApRadioIndex,
       "enterpriseApRadioAutoChannel": enterpriseApRadioAutoChannel,
       "enterpriseApRadioTransmitPower": enterpriseApRadioTransmitPower,
       "enterpriseApRadioTurboMode": enterpriseApRadioTurboMode,
       "enterpriseApRadioDataRate": enterpriseApRadioDataRate,
       "enterpriseApRadioGMode": enterpriseApRadioGMode,
       "enterpriseApRadioAntennaMode": enterpriseApRadioAntennaMode,
       "rogueApState": rogueApState,
       "rogueApInterval": rogueApInterval,
       "rogueApDuration": rogueApDuration,
       "rogueApScanNow": rogueApScanNow,
       "enterpriseApVapRadioTable": enterpriseApVapRadioTable,
       "enterpriseApVapRadioEntry": enterpriseApVapRadioEntry,
       "enterpriseApVapRadioIndex": enterpriseApVapRadioIndex,
       "enterpriseApVapRadioState": enterpriseApVapRadioState,
       "enterpriseApVapRadioClosedSystem": enterpriseApVapRadioClosedSystem,
       "enterpriseApVapRadioMaxAssoc": enterpriseApVapRadioMaxAssoc,
       "enterpriseApVapRadioTransmitKey": enterpriseApVapRadioTransmitKey,
       "enterpriseApVapRadioDescription": enterpriseApVapRadioDescription,
       "radioWdsTable": radioWdsTable,
       "radioWdsEntry": radioWdsEntry,
       "wdsApRole": wdsApRole,
       "radioWdsPeerTable": radioWdsPeerTable,
       "radioWdsPeerEntry": radioWdsPeerEntry,
       "wdsPeerIndex": wdsPeerIndex,
       "wdsPeerBssid": wdsPeerBssid,
       "enterpriseApWebRedirection": enterpriseApWebRedirection,
       "webRedirectionEnabled": webRedirectionEnabled,
       "enterpriseApProxyArp": enterpriseApProxyArp,
       "proxyArpEnabled": proxyArpEnabled,
       "enterpriseApRogueAp": enterpriseApRogueAp,
       "rogueApDetectionTable": rogueApDetectionTable,
       "rogueApEntry": rogueApEntry,
       "rogueApIndex": rogueApIndex,
       "rogueApBssid": rogueApBssid,
       "rogueApSsid": rogueApSsid,
       "rogueApPortNumber": rogueApPortNumber,
       "rogueApChannelNumber": rogueApChannelNumber,
       "rogueApRSSIValue": rogueApRSSIValue,
       "apNotificationTrapTree": apNotificationTrapTree,
       "apNotificationObjects": apNotificationObjects,
       "apNotificationDot11MacAddr": apNotificationDot11MacAddr,
       "apNotificationDot11Station": apNotificationDot11Station,
       "apNotificationDot11RequestType": apNotificationDot11RequestType,
       "apNotificationDot11ReasonCode": apNotificationDot11ReasonCode,
       "apNotificationDot11IpAddress": apNotificationDot11IpAddress,
       "apNotificationDot11AuthenticatorMacAddr": apNotificationDot11AuthenticatorMacAddr,
       "apNotificationTrapObjects": apNotificationTrapObjects,
       "sysSystemUp": sysSystemUp,
       "sysSystemDown": sysSystemDown,
       "sysRadiusServerChanged": sysRadiusServerChanged,
       "dot11StationAssociation": dot11StationAssociation,
       "dot11StationReAssociation": dot11StationReAssociation,
       "dot11StationAuthentication": dot11StationAuthentication,
       "dot11StationRequestFail": dot11StationRequestFail,
       "dot11InterfaceAGFail": dot11InterfaceAGFail,
       "dot1xMacAddrAuthSuccess": dot1xMacAddrAuthSuccess,
       "dot1xMacAddrAuthFail": dot1xMacAddrAuthFail,
       "dot1xAuthNotInitiated": dot1xAuthNotInitiated,
       "dot1xAuthSuccess": dot1xAuthSuccess,
       "dot1xAuthFail": dot1xAuthFail,
       "localMacAddrAuthSuccess": localMacAddrAuthSuccess,
       "localMacAddrAuthFail": localMacAddrAuthFail,
       "pppLogonFail": pppLogonFail,
       "iappStationRoamedFrom": iappStationRoamedFrom,
       "iappStationRoamedTo": iappStationRoamedTo,
       "iappContextDataSent": iappContextDataSent,
       "sntpServerFail": sntpServerFail}
)

# SNMP MIB module (HP-PROCURVE-420-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-PROCURVE-420-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:39 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class Guage32(Counter32):
    """Custom type Guage32 based on Counter32"""




class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""




class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HP_ObjectIdentity = ObjectIdentity
hP = _HP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Enterprise_ObjectIdentity = ObjectIdentity
enterprise = _Enterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_AccessPoint_ObjectIdentity = ObjectIdentity
accessPoint = _AccessPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7)
)
_ProCurve_ObjectIdentity = ObjectIdentity
proCurve = _ProCurve_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11)
)
_HPProCuve420_ObjectIdentity = ObjectIdentity
hPProCuve420 = _HPProCuve420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37)
)
_EnterpriseApSys_ObjectIdentity = ObjectIdentity
enterpriseApSys = _EnterpriseApSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 1)
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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 1, 1),
    _SwHardwareVer_Type()
)
swHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHardwareVer.setStatus("mandatory")


class _SwBootRomVer_Type(DisplayString):
    """Custom type swBootRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwBootRomVer_Type.__name__ = "DisplayString"
_SwBootRomVer_Object = MibScalar
swBootRomVer = _SwBootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 1, 2),
    _SwBootRomVer_Type()
)
swBootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootRomVer.setStatus("mandatory")


class _SwOpCodeVer_Type(DisplayString):
    """Custom type swOpCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwOpCodeVer_Type.__name__ = "DisplayString"
_SwOpCodeVer_Object = MibScalar
swOpCodeVer = _SwOpCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 1, 3),
    _SwOpCodeVer_Type()
)
swOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOpCodeVer.setStatus("mandatory")


class _SwCountryCode_Type(DisplayString):
    """Custom type swCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwCountryCode_Type.__name__ = "DisplayString"
_SwCountryCode_Object = MibScalar
swCountryCode = _SwCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 1, 4),
    _SwCountryCode_Type()
)
swCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCountryCode.setStatus("mandatory")
_EnterpriseApLineMgnt_ObjectIdentity = ObjectIdentity
enterpriseApLineMgnt = _EnterpriseApLineMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2)
)
_LineTable_Object = MibTable
lineTable = _LineTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1)
)
if mibBuilder.loadTexts:
    lineTable.setStatus("mandatory")
_LineEntry_Object = MibTableRow
lineEntry = _LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1)
)
lineEntry.setIndexNames(
    (0, "HP-PROCURVE-420-PRIVATE-MIB", "lineIndex"),
)
if mibBuilder.loadTexts:
    lineEntry.setStatus("mandatory")
_LineIndex_Type = Integer32
_LineIndex_Object = MibTableColumn
lineIndex = _LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1, 1),
    _LineIndex_Type()
)
lineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lineIndex.setStatus("mandatory")
_LineDataBits_Type = Integer32
_LineDataBits_Object = MibTableColumn
lineDataBits = _LineDataBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1, 2),
    _LineDataBits_Type()
)
lineDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDataBits.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1, 3),
    _LineParity_Type()
)
lineParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineParity.setStatus("mandatory")
_LineSpeed_Type = Integer32
_LineSpeed_Object = MibTableColumn
lineSpeed = _LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1, 4),
    _LineSpeed_Type()
)
lineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineSpeed.setStatus("mandatory")
_LineStopBits_Type = Integer32
_LineStopBits_Object = MibTableColumn
lineStopBits = _LineStopBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1, 5),
    _LineStopBits_Type()
)
lineStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineStopBits.setStatus("mandatory")
_EnterpriseApPortMgnt_ObjectIdentity = ObjectIdentity
enterpriseApPortMgnt = _EnterpriseApPortMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1)
)
portEntry.setIndexNames(
    (0, "HP-PROCURVE-420-PRIVATE-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("mandatory")


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
        *(("auto", 1),
          ("fullDuplex10", 3),
          ("fullDuplex100", 5),
          ("fullDuplex1000", 7),
          ("halfDuplex10", 2),
          ("halfDuplex100", 4),
          ("halfDuplex1000", 6))
    )


_PortSpeedDpxCfg_Type.__name__ = "Integer32"
_PortSpeedDpxCfg_Object = MibTableColumn
portSpeedDpxCfg = _PortSpeedDpxCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 4),
    _PortSpeedDpxCfg_Type()
)
portSpeedDpxCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeedDpxCfg.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 5),
    _PortFlowCtrlCfg_Type()
)
portFlowCtrlCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlCfg.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 6),
    _PortCapabilities_Type()
)
portCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCapabilities.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 7),
    _PortAutonegotiation_Type()
)
portAutonegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAutonegotiation.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 8),
    _PortSpeedDpxStatus_Type()
)
portSpeedDpxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeedDpxStatus.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("mandatory")
_EnterpriseApFileTransferMgt_ObjectIdentity = ObjectIdentity
enterpriseApFileTransferMgt = _EnterpriseApFileTransferMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4)
)


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
        *(("go", 1),
          ("nogo", 2))
    )


_TransferStart_Type.__name__ = "Integer32"
_TransferStart_Object = MibScalar
transferStart = _TransferStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 1),
    _TransferStart_Type()
)
transferStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferStart.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 2),
    _TransferType_Type()
)
transferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferType.setStatus("mandatory")


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
        *(("config", 2),
          ("opcode", 1))
    )


_FileType_Type.__name__ = "Integer32"
_FileType_Object = MibScalar
fileType = _FileType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 3),
    _FileType_Type()
)
fileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileType.setStatus("mandatory")


class _SrcFile_Type(DisplayString):
    """Custom type srcFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SrcFile_Type.__name__ = "DisplayString"
_SrcFile_Object = MibScalar
srcFile = _SrcFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 4),
    _SrcFile_Type()
)
srcFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcFile.setStatus("mandatory")


class _DestFile_Type(DisplayString):
    """Custom type destFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DestFile_Type.__name__ = "DisplayString"
_DestFile_Object = MibScalar
destFile = _DestFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 5),
    _DestFile_Type()
)
destFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destFile.setStatus("mandatory")
_FileServer_Type = IpAddress
_FileServer_Object = MibScalar
fileServer = _FileServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 6),
    _FileServer_Type()
)
fileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServer.setStatus("mandatory")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 7),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("mandatory")


class _Password_Type(DisplayString):
    """Custom type password based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Password_Type.__name__ = "DisplayString"
_Password_Object = MibScalar
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 8),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("mandatory")
_EnterpriseApResetMgt_ObjectIdentity = ObjectIdentity
enterpriseApResetMgt = _EnterpriseApResetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 5)
)


class _RestartOpCodeFile_Type(DisplayString):
    """Custom type restartOpCodeFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RestartOpCodeFile_Type.__name__ = "DisplayString"
_RestartOpCodeFile_Object = MibScalar
restartOpCodeFile = _RestartOpCodeFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 5, 1),
    _RestartOpCodeFile_Type()
)
restartOpCodeFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartOpCodeFile.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 5, 2),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("mandatory")
_EnterpriseApIpMgt_ObjectIdentity = ObjectIdentity
enterpriseApIpMgt = _EnterpriseApIpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6)
)
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibScalar
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6, 1),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("mandatory")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibScalar
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6, 2),
    _NetConfigSubnetMask_Type()
)
netConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigSubnetMask.setStatus("mandatory")
_NetDefaultGateway_Type = IpAddress
_NetDefaultGateway_Object = MibScalar
netDefaultGateway = _NetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6, 3),
    _NetDefaultGateway_Type()
)
netDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDefaultGateway.setStatus("mandatory")


class _IpHttpState_Type(Integer32):
    """Custom type ipHttpState based on Integer32"""
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


_IpHttpState_Type.__name__ = "Integer32"
_IpHttpState_Object = MibScalar
ipHttpState = _IpHttpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6, 4),
    _IpHttpState_Type()
)
ipHttpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpState.setStatus("mandatory")
_IpHttpPort_Type = Integer32
_IpHttpPort_Object = MibScalar
ipHttpPort = _IpHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6, 5),
    _IpHttpPort_Type()
)
ipHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpPort.setStatus("mandatory")
_EnterpriseAPdot11_ObjectIdentity = ObjectIdentity
enterpriseAPdot11 = _EnterpriseAPdot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7)
)
_Hpdot11StationConfigTable_Object = MibTable
hpdot11StationConfigTable = _Hpdot11StationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1)
)
if mibBuilder.loadTexts:
    hpdot11StationConfigTable.setStatus("mandatory")
_Hpdot11StationConfigEntry_Object = MibTableRow
hpdot11StationConfigEntry = _Hpdot11StationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1)
)
hpdot11StationConfigEntry.setIndexNames(
    (0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11portIndex"),
)
if mibBuilder.loadTexts:
    hpdot11StationConfigEntry.setStatus("mandatory")
_Hpdot11portIndex_Type = Integer32
_Hpdot11portIndex_Object = MibTableColumn
hpdot11portIndex = _Hpdot11portIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 1),
    _Hpdot11portIndex_Type()
)
hpdot11portIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpdot11portIndex.setStatus("mandatory")


class _Hpdot11DesiredSSID_Type(OctetString):
    """Custom type hpdot11DesiredSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hpdot11DesiredSSID_Type.__name__ = "OctetString"
_Hpdot11DesiredSSID_Object = MibTableColumn
hpdot11DesiredSSID = _Hpdot11DesiredSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 2),
    _Hpdot11DesiredSSID_Type()
)
hpdot11DesiredSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11DesiredSSID.setStatus("mandatory")


class _Hpdot11BeaconPeriod_Type(Integer32):
    """Custom type hpdot11BeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_Hpdot11BeaconPeriod_Type.__name__ = "Integer32"
_Hpdot11BeaconPeriod_Object = MibTableColumn
hpdot11BeaconPeriod = _Hpdot11BeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 3),
    _Hpdot11BeaconPeriod_Type()
)
hpdot11BeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11BeaconPeriod.setStatus("mandatory")


class _Hpdot11DTIMPeriod_Type(Integer32):
    """Custom type hpdot11DTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hpdot11DTIMPeriod_Type.__name__ = "Integer32"
_Hpdot11DTIMPeriod_Object = MibTableColumn
hpdot11DTIMPeriod = _Hpdot11DTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 4),
    _Hpdot11DTIMPeriod_Type()
)
hpdot11DTIMPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11DTIMPeriod.setStatus("mandatory")


class _Hpdot11OperationalRateSet_Type(Integer32):
    """Custom type hpdot11OperationalRateSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 108),
    )


_Hpdot11OperationalRateSet_Type.__name__ = "Integer32"
_Hpdot11OperationalRateSet_Object = MibTableColumn
hpdot11OperationalRateSet = _Hpdot11OperationalRateSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 5),
    _Hpdot11OperationalRateSet_Type()
)
hpdot11OperationalRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11OperationalRateSet.setStatus("mandatory")


class _Hpdot11AuthenticationAlgorithm_Type(Integer32):
    """Custom type hpdot11AuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2))
    )


_Hpdot11AuthenticationAlgorithm_Type.__name__ = "Integer32"
_Hpdot11AuthenticationAlgorithm_Object = MibTableColumn
hpdot11AuthenticationAlgorithm = _Hpdot11AuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 6),
    _Hpdot11AuthenticationAlgorithm_Type()
)
hpdot11AuthenticationAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11AuthenticationAlgorithm.setStatus("mandatory")
_Hpdot11PrivacyTable_Object = MibTable
hpdot11PrivacyTable = _Hpdot11PrivacyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2)
)
if mibBuilder.loadTexts:
    hpdot11PrivacyTable.setStatus("mandatory")
_Hpdot11PrivacyEntry_Object = MibTableRow
hpdot11PrivacyEntry = _Hpdot11PrivacyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2, 1)
)
hpdot11PrivacyEntry.setIndexNames(
    (0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11PrivacyportIndex"),
)
if mibBuilder.loadTexts:
    hpdot11PrivacyEntry.setStatus("mandatory")
_Hpdot11PrivacyportIndex_Type = Integer32
_Hpdot11PrivacyportIndex_Object = MibTableColumn
hpdot11PrivacyportIndex = _Hpdot11PrivacyportIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2, 1, 1),
    _Hpdot11PrivacyportIndex_Type()
)
hpdot11PrivacyportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpdot11PrivacyportIndex.setStatus("mandatory")


class _Hpdot11PrivacyInvoked_Type(Integer32):
    """Custom type hpdot11PrivacyInvoked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Hpdot11PrivacyInvoked_Type.__name__ = "Integer32"
_Hpdot11PrivacyInvoked_Object = MibTableColumn
hpdot11PrivacyInvoked = _Hpdot11PrivacyInvoked_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2, 1, 2),
    _Hpdot11PrivacyInvoked_Type()
)
hpdot11PrivacyInvoked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11PrivacyInvoked.setStatus("mandatory")


class _Hpdot11WEPDefaultKeyID_Type(Integer32):
    """Custom type hpdot11WEPDefaultKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Hpdot11WEPDefaultKeyID_Type.__name__ = "Integer32"
_Hpdot11WEPDefaultKeyID_Object = MibTableColumn
hpdot11WEPDefaultKeyID = _Hpdot11WEPDefaultKeyID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2, 1, 3),
    _Hpdot11WEPDefaultKeyID_Type()
)
hpdot11WEPDefaultKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11WEPDefaultKeyID.setStatus("mandatory")


class _Hpdot11WEPKeyMappingLength_Type(Integer32):
    """Custom type hpdot11WEPKeyMappingLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483647),
    )


_Hpdot11WEPKeyMappingLength_Type.__name__ = "Integer32"
_Hpdot11WEPKeyMappingLength_Object = MibTableColumn
hpdot11WEPKeyMappingLength = _Hpdot11WEPKeyMappingLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2, 1, 4),
    _Hpdot11WEPKeyMappingLength_Type()
)
hpdot11WEPKeyMappingLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11WEPKeyMappingLength.setStatus("mandatory")
_Hpdot11mac_ObjectIdentity = ObjectIdentity
hpdot11mac = _Hpdot11mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3)
)
_Hpdot11OperationTable_Object = MibTable
hpdot11OperationTable = _Hpdot11OperationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3, 1)
)
if mibBuilder.loadTexts:
    hpdot11OperationTable.setStatus("mandatory")
_Hpdot11OperationEntry_Object = MibTableRow
hpdot11OperationEntry = _Hpdot11OperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3, 1, 1)
)
hpdot11OperationEntry.setIndexNames(
    (0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11OperationIndex"),
)
if mibBuilder.loadTexts:
    hpdot11OperationEntry.setStatus("mandatory")
_Hpdot11OperationIndex_Type = Integer32
_Hpdot11OperationIndex_Object = MibTableColumn
hpdot11OperationIndex = _Hpdot11OperationIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3, 1, 1, 1),
    _Hpdot11OperationIndex_Type()
)
hpdot11OperationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpdot11OperationIndex.setStatus("mandatory")


class _Hpdot11RTSThreshold_Type(Integer32):
    """Custom type hpdot11RTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_Hpdot11RTSThreshold_Type.__name__ = "Integer32"
_Hpdot11RTSThreshold_Object = MibTableColumn
hpdot11RTSThreshold = _Hpdot11RTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3, 1, 1, 2),
    _Hpdot11RTSThreshold_Type()
)
hpdot11RTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11RTSThreshold.setStatus("mandatory")


class _Hpdot11FragmentationThreshold_Type(Integer32):
    """Custom type hpdot11FragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_Hpdot11FragmentationThreshold_Type.__name__ = "Integer32"
_Hpdot11FragmentationThreshold_Object = MibTableColumn
hpdot11FragmentationThreshold = _Hpdot11FragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3, 1, 1, 3),
    _Hpdot11FragmentationThreshold_Type()
)
hpdot11FragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11FragmentationThreshold.setStatus("mandatory")
_Hpdot11phy_ObjectIdentity = ObjectIdentity
hpdot11phy = _Hpdot11phy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4)
)
_Hpdot11PhyOperationTable_Object = MibTable
hpdot11PhyOperationTable = _Hpdot11PhyOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1)
)
if mibBuilder.loadTexts:
    hpdot11PhyOperationTable.setStatus("mandatory")
_Hpdot11PhyOperationEntry_Object = MibTableRow
hpdot11PhyOperationEntry = _Hpdot11PhyOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1, 1)
)
hpdot11PhyOperationEntry.setIndexNames(
    (0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11Index"),
)
if mibBuilder.loadTexts:
    hpdot11PhyOperationEntry.setStatus("mandatory")
_Hpdot11Index_Type = Integer32
_Hpdot11Index_Object = MibTableColumn
hpdot11Index = _Hpdot11Index_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1, 1, 1),
    _Hpdot11Index_Type()
)
hpdot11Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpdot11Index.setStatus("mandatory")
_Hpdot11CurrentChannel_Type = Integer32
_Hpdot11CurrentChannel_Object = MibTableColumn
hpdot11CurrentChannel = _Hpdot11CurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1, 1, 2),
    _Hpdot11CurrentChannel_Type()
)
hpdot11CurrentChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11CurrentChannel.setStatus("mandatory")


class _Hpdot11TurboModeEnabled_Type(Integer32):
    """Custom type hpdot11TurboModeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("none", 99),
          ("off", 2),
          ("on", 1))
    )


_Hpdot11TurboModeEnabled_Type.__name__ = "Integer32"
_Hpdot11TurboModeEnabled_Object = MibTableColumn
hpdot11TurboModeEnabled = _Hpdot11TurboModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1, 1, 3),
    _Hpdot11TurboModeEnabled_Type()
)
hpdot11TurboModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpdot11TurboModeEnabled.setStatus("mandatory")


class _Hpdot11PreambleLength_Type(Integer32):
    """Custom type hpdot11PreambleLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_Hpdot11PreambleLength_Type.__name__ = "Integer32"
_Hpdot11PreambleLength_Object = MibTableColumn
hpdot11PreambleLength = _Hpdot11PreambleLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1, 1, 4),
    _Hpdot11PreambleLength_Type()
)
hpdot11PreambleLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11PreambleLength.setStatus("mandatory")
_Hpdot11AuthenticationEntry_ObjectIdentity = ObjectIdentity
hpdot11AuthenticationEntry = _Hpdot11AuthenticationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 5)
)
_Hpdot118021xSupport_Type = TruthValue
_Hpdot118021xSupport_Object = MibScalar
hpdot118021xSupport = _Hpdot118021xSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 5, 1),
    _Hpdot118021xSupport_Type()
)
hpdot118021xSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot118021xSupport.setStatus("mandatory")
_Hpdot118021xRequired_Type = TruthValue
_Hpdot118021xRequired_Object = MibScalar
hpdot118021xRequired = _Hpdot118021xRequired_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 5, 2),
    _Hpdot118021xRequired_Type()
)
hpdot118021xRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot118021xRequired.setStatus("mandatory")
_Hpdot11AuthenticationServerTable_Object = MibTable
hpdot11AuthenticationServerTable = _Hpdot11AuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6)
)
if mibBuilder.loadTexts:
    hpdot11AuthenticationServerTable.setStatus("mandatory")
_Hpdot11AuthenticationServerEntry_Object = MibTableRow
hpdot11AuthenticationServerEntry = _Hpdot11AuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1)
)
hpdot11AuthenticationServerEntry.setIndexNames(
    (0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11serverIndex"),
)
if mibBuilder.loadTexts:
    hpdot11AuthenticationServerEntry.setStatus("mandatory")
_Hpdot11serverIndex_Type = Integer32
_Hpdot11serverIndex_Object = MibTableColumn
hpdot11serverIndex = _Hpdot11serverIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 1),
    _Hpdot11serverIndex_Type()
)
hpdot11serverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpdot11serverIndex.setStatus("mandatory")
_Hpdot11AuthenticationServer_Type = IpAddress
_Hpdot11AuthenticationServer_Object = MibTableColumn
hpdot11AuthenticationServer = _Hpdot11AuthenticationServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 2),
    _Hpdot11AuthenticationServer_Type()
)
hpdot11AuthenticationServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11AuthenticationServer.setStatus("mandatory")


class _Hpdot11AuthenticationPort_Type(Integer32):
    """Custom type hpdot11AuthenticationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Hpdot11AuthenticationPort_Type.__name__ = "Integer32"
_Hpdot11AuthenticationPort_Object = MibTableColumn
hpdot11AuthenticationPort = _Hpdot11AuthenticationPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 3),
    _Hpdot11AuthenticationPort_Type()
)
hpdot11AuthenticationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11AuthenticationPort.setStatus("mandatory")


class _Hpdot11AuthenticationKey_Type(DisplayString):
    """Custom type hpdot11AuthenticationKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Hpdot11AuthenticationKey_Type.__name__ = "DisplayString"
_Hpdot11AuthenticationKey_Object = MibTableColumn
hpdot11AuthenticationKey = _Hpdot11AuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 4),
    _Hpdot11AuthenticationKey_Type()
)
hpdot11AuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11AuthenticationKey.setStatus("mandatory")


class _Hpdot11AuthenticationRetransmit_Type(Integer32):
    """Custom type hpdot11AuthenticationRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Hpdot11AuthenticationRetransmit_Type.__name__ = "Integer32"
_Hpdot11AuthenticationRetransmit_Object = MibTableColumn
hpdot11AuthenticationRetransmit = _Hpdot11AuthenticationRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 5),
    _Hpdot11AuthenticationRetransmit_Type()
)
hpdot11AuthenticationRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11AuthenticationRetransmit.setStatus("mandatory")


class _Hpdot11AuthenticationTimeout_Type(Integer32):
    """Custom type hpdot11AuthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Hpdot11AuthenticationTimeout_Type.__name__ = "Integer32"
_Hpdot11AuthenticationTimeout_Object = MibTableColumn
hpdot11AuthenticationTimeout = _Hpdot11AuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 6),
    _Hpdot11AuthenticationTimeout_Type()
)
hpdot11AuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11AuthenticationTimeout.setStatus("mandatory")
_Hpdot11FilterTable_Object = MibTable
hpdot11FilterTable = _Hpdot11FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 7)
)
if mibBuilder.loadTexts:
    hpdot11FilterTable.setStatus("mandatory")
_Hpdot11FilterEntry_Object = MibTableRow
hpdot11FilterEntry = _Hpdot11FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 7, 1)
)
hpdot11FilterEntry.setIndexNames(
    (0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11FilterIndex"),
)
if mibBuilder.loadTexts:
    hpdot11FilterEntry.setStatus("mandatory")
_Hpdot11FilterIndex_Type = Integer32
_Hpdot11FilterIndex_Object = MibTableColumn
hpdot11FilterIndex = _Hpdot11FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 7, 1, 1),
    _Hpdot11FilterIndex_Type()
)
hpdot11FilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpdot11FilterIndex.setStatus("mandatory")
_Hpdot11FilterAddress_Type = PhysAddress
_Hpdot11FilterAddress_Object = MibTableColumn
hpdot11FilterAddress = _Hpdot11FilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 7, 1, 2),
    _Hpdot11FilterAddress_Type()
)
hpdot11FilterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11FilterAddress.setStatus("mandatory")


class _Hpdot11FilterStatus_Type(Integer32):
    """Custom type hpdot11FilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 30),
          ("denied", 31))
    )


_Hpdot11FilterStatus_Type.__name__ = "Integer32"
_Hpdot11FilterStatus_Object = MibTableColumn
hpdot11FilterStatus = _Hpdot11FilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 7, 1, 3),
    _Hpdot11FilterStatus_Type()
)
hpdot11FilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11FilterStatus.setStatus("mandatory")
_Hpdot11smt_ObjectIdentity = ObjectIdentity
hpdot11smt = _Hpdot11smt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8)
)
_Hpdot11WEPDefaultKeys11g_ObjectIdentity = ObjectIdentity
hpdot11WEPDefaultKeys11g = _Hpdot11WEPDefaultKeys11g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1)
)
_Hpdot11WEPDefaultKeys11gTable_Object = MibTable
hpdot11WEPDefaultKeys11gTable = _Hpdot11WEPDefaultKeys11gTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hpdot11WEPDefaultKeys11gTable.setStatus("mandatory")
_Hpdot11WEPDefaultKeys11gEntry_Object = MibTableRow
hpdot11WEPDefaultKeys11gEntry = _Hpdot11WEPDefaultKeys11gEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1, 1, 1)
)
hpdot11WEPDefaultKeys11gEntry.setIndexNames(
    (0, "HP-PROCURVE-420-PRIVATE-MIB", "dot11WEPDefaultKey11gLength"),
)
if mibBuilder.loadTexts:
    hpdot11WEPDefaultKeys11gEntry.setStatus("mandatory")


class _Hpdot11WEPDefaultKey11gLength_Type(Integer32):
    """Custom type hpdot11WEPDefaultKey11gLength based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              128,
              152)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredFiftyTwo", 152),
          ("oneHundredTwentyEight", 128),
          ("sixtyFour", 64))
    )


_Hpdot11WEPDefaultKey11gLength_Type.__name__ = "Integer32"
_Hpdot11WEPDefaultKey11gLength_Object = MibTableColumn
hpdot11WEPDefaultKey11gLength = _Hpdot11WEPDefaultKey11gLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1, 1, 1, 1),
    _Hpdot11WEPDefaultKey11gLength_Type()
)
hpdot11WEPDefaultKey11gLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11WEPDefaultKey11gLength.setStatus("mandatory")


class _Hpdot11WEPDefaultKey11gIndex_Type(Integer32):
    """Custom type hpdot11WEPDefaultKey11gIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hpdot11WEPDefaultKey11gIndex_Type.__name__ = "Integer32"
_Hpdot11WEPDefaultKey11gIndex_Object = MibTableColumn
hpdot11WEPDefaultKey11gIndex = _Hpdot11WEPDefaultKey11gIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1, 1, 1, 2),
    _Hpdot11WEPDefaultKey11gIndex_Type()
)
hpdot11WEPDefaultKey11gIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpdot11WEPDefaultKey11gIndex.setStatus("mandatory")


class _Hpdot11WEPDefaultKey11gValue_Type(OctetString):
    """Custom type hpdot11WEPDefaultKey11gValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hpdot11WEPDefaultKey11gValue_Type.__name__ = "OctetString"
_Hpdot11WEPDefaultKey11gValue_Object = MibTableColumn
hpdot11WEPDefaultKey11gValue = _Hpdot11WEPDefaultKey11gValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1, 1, 1, 3),
    _Hpdot11WEPDefaultKey11gValue_Type()
)
hpdot11WEPDefaultKey11gValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpdot11WEPDefaultKey11gValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-PROCURVE-420-PRIVATE-MIB",
    **{"PhysAddress": PhysAddress,
       "Guage32": Guage32,
       "MacAddress": MacAddress,
       "DisplayString": DisplayString,
       "TruthValue": TruthValue,
       "hP": hP,
       "wireless": wireless,
       "enterprise": enterprise,
       "accessPoint": accessPoint,
       "proCurve": proCurve,
       "hPProCuve420": hPProCuve420,
       "enterpriseApSys": enterpriseApSys,
       "swHardwareVer": swHardwareVer,
       "swBootRomVer": swBootRomVer,
       "swOpCodeVer": swOpCodeVer,
       "swCountryCode": swCountryCode,
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
       "transferStart": transferStart,
       "transferType": transferType,
       "fileType": fileType,
       "srcFile": srcFile,
       "destFile": destFile,
       "fileServer": fileServer,
       "userName": userName,
       "password": password,
       "enterpriseApResetMgt": enterpriseApResetMgt,
       "restartOpCodeFile": restartOpCodeFile,
       "restartControl": restartControl,
       "enterpriseApIpMgt": enterpriseApIpMgt,
       "netConfigIPAddress": netConfigIPAddress,
       "netConfigSubnetMask": netConfigSubnetMask,
       "netDefaultGateway": netDefaultGateway,
       "ipHttpState": ipHttpState,
       "ipHttpPort": ipHttpPort,
       "enterpriseAPdot11": enterpriseAPdot11,
       "hpdot11StationConfigTable": hpdot11StationConfigTable,
       "hpdot11StationConfigEntry": hpdot11StationConfigEntry,
       "hpdot11portIndex": hpdot11portIndex,
       "hpdot11DesiredSSID": hpdot11DesiredSSID,
       "hpdot11BeaconPeriod": hpdot11BeaconPeriod,
       "hpdot11DTIMPeriod": hpdot11DTIMPeriod,
       "hpdot11OperationalRateSet": hpdot11OperationalRateSet,
       "hpdot11AuthenticationAlgorithm": hpdot11AuthenticationAlgorithm,
       "hpdot11PrivacyTable": hpdot11PrivacyTable,
       "hpdot11PrivacyEntry": hpdot11PrivacyEntry,
       "hpdot11PrivacyportIndex": hpdot11PrivacyportIndex,
       "hpdot11PrivacyInvoked": hpdot11PrivacyInvoked,
       "hpdot11WEPDefaultKeyID": hpdot11WEPDefaultKeyID,
       "hpdot11WEPKeyMappingLength": hpdot11WEPKeyMappingLength,
       "hpdot11mac": hpdot11mac,
       "hpdot11OperationTable": hpdot11OperationTable,
       "hpdot11OperationEntry": hpdot11OperationEntry,
       "hpdot11OperationIndex": hpdot11OperationIndex,
       "hpdot11RTSThreshold": hpdot11RTSThreshold,
       "hpdot11FragmentationThreshold": hpdot11FragmentationThreshold,
       "hpdot11phy": hpdot11phy,
       "hpdot11PhyOperationTable": hpdot11PhyOperationTable,
       "hpdot11PhyOperationEntry": hpdot11PhyOperationEntry,
       "hpdot11Index": hpdot11Index,
       "hpdot11CurrentChannel": hpdot11CurrentChannel,
       "hpdot11TurboModeEnabled": hpdot11TurboModeEnabled,
       "hpdot11PreambleLength": hpdot11PreambleLength,
       "hpdot11AuthenticationEntry": hpdot11AuthenticationEntry,
       "hpdot118021xSupport": hpdot118021xSupport,
       "hpdot118021xRequired": hpdot118021xRequired,
       "hpdot11AuthenticationServerTable": hpdot11AuthenticationServerTable,
       "hpdot11AuthenticationServerEntry": hpdot11AuthenticationServerEntry,
       "hpdot11serverIndex": hpdot11serverIndex,
       "hpdot11AuthenticationServer": hpdot11AuthenticationServer,
       "hpdot11AuthenticationPort": hpdot11AuthenticationPort,
       "hpdot11AuthenticationKey": hpdot11AuthenticationKey,
       "hpdot11AuthenticationRetransmit": hpdot11AuthenticationRetransmit,
       "hpdot11AuthenticationTimeout": hpdot11AuthenticationTimeout,
       "hpdot11FilterTable": hpdot11FilterTable,
       "hpdot11FilterEntry": hpdot11FilterEntry,
       "hpdot11FilterIndex": hpdot11FilterIndex,
       "hpdot11FilterAddress": hpdot11FilterAddress,
       "hpdot11FilterStatus": hpdot11FilterStatus,
       "hpdot11smt": hpdot11smt,
       "hpdot11WEPDefaultKeys11g": hpdot11WEPDefaultKeys11g,
       "hpdot11WEPDefaultKeys11gTable": hpdot11WEPDefaultKeys11gTable,
       "hpdot11WEPDefaultKeys11gEntry": hpdot11WEPDefaultKeys11gEntry,
       "hpdot11WEPDefaultKey11gLength": hpdot11WEPDefaultKey11gLength,
       "hpdot11WEPDefaultKey11gIndex": hpdot11WEPDefaultKey11gIndex,
       "hpdot11WEPDefaultKey11gValue": hpdot11WEPDefaultKey11gValue}
)

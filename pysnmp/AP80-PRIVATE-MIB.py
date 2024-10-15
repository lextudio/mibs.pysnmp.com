# SNMP MIB module (AP80-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AP80-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:08 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





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

_Aruba_ObjectIdentity = ObjectIdentity
aruba = _Aruba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823)
)
_ArubaEnterpriseMibModules_ObjectIdentity = ObjectIdentity
arubaEnterpriseMibModules = _ArubaEnterpriseMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2)
)
_ArubaAp_ObjectIdentity = ObjectIdentity
arubaAp = _ArubaAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3)
)
_WlsrOutDoorApMibModules_ObjectIdentity = ObjectIdentity
wlsrOutDoorApMibModules = _WlsrOutDoorApMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2)
)
_EnterpriseApSys_ObjectIdentity = ObjectIdentity
enterpriseApSys = _EnterpriseApSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1, 4),
    _SwSerialNumber_Type()
)
swSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSerialNumber.setStatus("current")
_SysNotificationTree_ObjectIdentity = ObjectIdentity
sysNotificationTree = _SysNotificationTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1, 5)
)
_SysNotificationObjects_ObjectIdentity = ObjectIdentity
sysNotificationObjects = _SysNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1, 5, 1)
)
_SysNotifications_ObjectIdentity = ObjectIdentity
sysNotifications = _SysNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1, 5, 2)
)
_EnterpriseApLineMgnt_ObjectIdentity = ObjectIdentity
enterpriseApLineMgnt = _EnterpriseApLineMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 2)
)
_LineTable_Object = MibTable
lineTable = _LineTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lineTable.setStatus("current")
_LineEntry_Object = MibTableRow
lineEntry = _LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 2, 1, 1)
)
lineEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "lineIndex"),
)
if mibBuilder.loadTexts:
    lineEntry.setStatus("current")
_LineIndex_Type = Integer32
_LineIndex_Object = MibTableColumn
lineIndex = _LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 2, 1, 1, 1),
    _LineIndex_Type()
)
lineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lineIndex.setStatus("current")
_LineDataBits_Type = Integer32
_LineDataBits_Object = MibTableColumn
lineDataBits = _LineDataBits_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 2, 1, 1, 3),
    _LineParity_Type()
)
lineParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineParity.setStatus("current")
_LineSpeed_Type = Integer32
_LineSpeed_Object = MibTableColumn
lineSpeed = _LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 2, 1, 1, 4),
    _LineSpeed_Type()
)
lineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineSpeed.setStatus("current")
_LineStopBits_Type = Integer32
_LineStopBits_Object = MibTableColumn
lineStopBits = _LineStopBits_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 2, 1, 1, 5),
    _LineStopBits_Type()
)
lineStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineStopBits.setStatus("current")
_EnterpriseApPortMgnt_ObjectIdentity = ObjectIdentity
enterpriseApPortMgnt = _EnterpriseApPortMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3, 1, 1)
)
portEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 3, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("current")
_EnterpriseApFileTransferMgt_ObjectIdentity = ObjectIdentity
enterpriseApFileTransferMgt = _EnterpriseApFileTransferMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 4)
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 4, 1),
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("application", 1),
          ("bootcode", 3),
          ("config", 2))
    )


_FileType_Type.__name__ = "Integer32"
_FileType_Object = MibScalar
fileType = _FileType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 4, 3),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 4, 4),
    _DestFile_Type()
)
destFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destFile.setStatus("current")
_FileServer_Type = IpAddress
_FileServer_Object = MibScalar
fileServer = _FileServer_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 4, 5),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 4, 6),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 4, 7),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 4, 8),
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
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("nothing", 0),
          ("upload", 2))
    )


_TransferStart_Type.__name__ = "Integer32"
_TransferStart_Object = MibScalar
transferStart = _TransferStart_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 4, 9),
    _TransferStart_Type()
)
transferStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferStart.setStatus("current")
_EnterpriseApResetMgt_ObjectIdentity = ObjectIdentity
enterpriseApResetMgt = _EnterpriseApResetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 5)
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 5, 2),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("current")
_EnterpriseApIpMgt_ObjectIdentity = ObjectIdentity
enterpriseApIpMgt = _EnterpriseApIpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 6)
)
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibScalar
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 6, 1),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("current")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibScalar
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 6, 2),
    _NetConfigSubnetMask_Type()
)
netConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigSubnetMask.setStatus("current")
_NetConfigDefaultGateway_Type = IpAddress
_NetConfigDefaultGateway_Object = MibScalar
netConfigDefaultGateway = _NetConfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 6, 3),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 6, 4),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 6, 5),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 6, 6),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 6, 7),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 6, 8),
    _NetConfigDHCPState_Type()
)
netConfigDHCPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netConfigDHCPState.setStatus("current")
_EnterpriseAPdot11_ObjectIdentity = ObjectIdentity
enterpriseAPdot11 = _EnterpriseAPdot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7)
)
_Dot11AuthenticationEntry_ObjectIdentity = ObjectIdentity
dot11AuthenticationEntry = _Dot11AuthenticationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 1)
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 1, 1),
    _Dot118021xState_Type()
)
dot118021xState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xState.setStatus("obsolete")


class _Dot118021xBroadcastKeyRefreshRate_Type(Integer32):
    """Custom type dot118021xBroadcastKeyRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Dot118021xBroadcastKeyRefreshRate_Type.__name__ = "Integer32"
_Dot118021xBroadcastKeyRefreshRate_Object = MibScalar
dot118021xBroadcastKeyRefreshRate = _Dot118021xBroadcastKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 1, 2),
    _Dot118021xBroadcastKeyRefreshRate_Type()
)
dot118021xBroadcastKeyRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xBroadcastKeyRefreshRate.setStatus("obsolete")


class _Dot118021xSessionKeyRefreshRate_Type(Integer32):
    """Custom type dot118021xSessionKeyRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Dot118021xSessionKeyRefreshRate_Type.__name__ = "Integer32"
_Dot118021xSessionKeyRefreshRate_Object = MibScalar
dot118021xSessionKeyRefreshRate = _Dot118021xSessionKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 1, 3),
    _Dot118021xSessionKeyRefreshRate_Type()
)
dot118021xSessionKeyRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xSessionKeyRefreshRate.setStatus("obsolete")


class _Dot118021xReauthenticationTimeout_Type(Integer32):
    """Custom type dot118021xReauthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Dot118021xReauthenticationTimeout_Type.__name__ = "Integer32"
_Dot118021xReauthenticationTimeout_Object = MibScalar
dot118021xReauthenticationTimeout = _Dot118021xReauthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 1, 4),
    _Dot118021xReauthenticationTimeout_Type()
)
dot118021xReauthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xReauthenticationTimeout.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 1, 5),
    _Dot11MACAuthenticationType_Type()
)
dot11MACAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MACAuthenticationType.setStatus("obsolete")
_Dot11AuthenticationServerTable_Object = MibTable
dot11AuthenticationServerTable = _Dot11AuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    dot11AuthenticationServerTable.setStatus("current")
_Dot11AuthenticationServerEntry_Object = MibTableRow
dot11AuthenticationServerEntry = _Dot11AuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2, 1)
)
dot11AuthenticationServerEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "dot11AuthenticationServerIndex"),
)
if mibBuilder.loadTexts:
    dot11AuthenticationServerEntry.setStatus("current")
_Dot11AuthenticationServerIndex_Type = Integer32
_Dot11AuthenticationServerIndex_Object = MibTableColumn
dot11AuthenticationServerIndex = _Dot11AuthenticationServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2, 1, 1),
    _Dot11AuthenticationServerIndex_Type()
)
dot11AuthenticationServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11AuthenticationServerIndex.setStatus("current")
_Dot11AuthenticationServer_Type = IpAddress
_Dot11AuthenticationServer_Object = MibTableColumn
dot11AuthenticationServer = _Dot11AuthenticationServer_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2, 1, 6),
    _Dot11AuthenticationTimeout_Type()
)
dot11AuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationTimeout.setStatus("current")


class _Dot11AuthenticationAcctPort_Type(Integer32):
    """Custom type dot11AuthenticationAcctPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_Dot11AuthenticationAcctPort_Type.__name__ = "Integer32"
_Dot11AuthenticationAcctPort_Object = MibTableColumn
dot11AuthenticationAcctPort = _Dot11AuthenticationAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2, 1, 7),
    _Dot11AuthenticationAcctPort_Type()
)
dot11AuthenticationAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationAcctPort.setStatus("current")


class _Dot11AuthenticationAcctInterimUpdate_Type(Integer32):
    """Custom type dot11AuthenticationAcctInterimUpdate based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_Dot11AuthenticationAcctInterimUpdate_Type.__name__ = "Integer32"
_Dot11AuthenticationAcctInterimUpdate_Object = MibTableColumn
dot11AuthenticationAcctInterimUpdate = _Dot11AuthenticationAcctInterimUpdate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2, 1, 8),
    _Dot11AuthenticationAcctInterimUpdate_Type()
)
dot11AuthenticationAcctInterimUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationAcctInterimUpdate.setStatus("current")


class _Dot11AuthenticationMACAddressFormat_Type(Integer32):
    """Custom type dot11AuthenticationMACAddressFormat based on Integer32"""
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
        *(("multi-colon", 4),
          ("multi-dash", 3),
          ("no-delimiter", 1),
          ("single-dash", 2))
    )


_Dot11AuthenticationMACAddressFormat_Type.__name__ = "Integer32"
_Dot11AuthenticationMACAddressFormat_Object = MibTableColumn
dot11AuthenticationMACAddressFormat = _Dot11AuthenticationMACAddressFormat_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2, 1, 9),
    _Dot11AuthenticationMACAddressFormat_Type()
)
dot11AuthenticationMACAddressFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationMACAddressFormat.setStatus("current")


class _Dot11AuthenticationVLANIDFormat_Type(Integer32):
    """Custom type dot11AuthenticationVLANIDFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 1))
    )


_Dot11AuthenticationVLANIDFormat_Type.__name__ = "Integer32"
_Dot11AuthenticationVLANIDFormat_Object = MibTableColumn
dot11AuthenticationVLANIDFormat = _Dot11AuthenticationVLANIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 2, 1, 10),
    _Dot11AuthenticationVLANIDFormat_Type()
)
dot11AuthenticationVLANIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AuthenticationVLANIDFormat.setStatus("current")
_Dot11MACAuthenticationFilter_ObjectIdentity = ObjectIdentity
dot11MACAuthenticationFilter = _Dot11MACAuthenticationFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 3)
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 3, 1),
    _Dot11FilterDefault_Type()
)
dot11FilterDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FilterDefault.setStatus("current")
_Dot11FilterTable_Object = MibTable
dot11FilterTable = _Dot11FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 3, 2)
)
if mibBuilder.loadTexts:
    dot11FilterTable.setStatus("current")
_Dot11FilterEntry_Object = MibTableRow
dot11FilterEntry = _Dot11FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 3, 2, 1)
)
dot11FilterEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "dot11FilterAddress"),
)
if mibBuilder.loadTexts:
    dot11FilterEntry.setStatus("current")
_Dot11FilterAddress_Type = MacAddress
_Dot11FilterAddress_Object = MibTableColumn
dot11FilterAddress = _Dot11FilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 3, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 3, 2, 1, 2),
    _Dot11FilterStatus_Type()
)
dot11FilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FilterStatus.setStatus("current")
_Dot11NotificationTree_ObjectIdentity = ObjectIdentity
dot11NotificationTree = _Dot11NotificationTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4)
)
_Dot11NotificationObjects_ObjectIdentity = ObjectIdentity
dot11NotificationObjects = _Dot11NotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 1)
)
_Dot11MacAddr_Type = MacAddress
_Dot11MacAddr_Object = MibScalar
dot11MacAddr = _Dot11MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 1, 1),
    _Dot11MacAddr_Type()
)
dot11MacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11MacAddr.setStatus("current")
_Dot11Station_Type = MacAddress
_Dot11Station_Object = MibScalar
dot11Station = _Dot11Station_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 1, 2),
    _Dot11Station_Type()
)
dot11Station.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11Station.setStatus("current")


class _Dot11RequestType_Type(Integer32):
    """Custom type dot11RequestType based on Integer32"""
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


_Dot11RequestType_Type.__name__ = "Integer32"
_Dot11RequestType_Object = MibScalar
dot11RequestType = _Dot11RequestType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 1, 3),
    _Dot11RequestType_Type()
)
dot11RequestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11RequestType.setStatus("current")


class _Dot11ReasonCode_Type(Integer32):
    """Custom type dot11ReasonCode based on Integer32"""
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


_Dot11ReasonCode_Type.__name__ = "Integer32"
_Dot11ReasonCode_Object = MibScalar
dot11ReasonCode = _Dot11ReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 1, 4),
    _Dot11ReasonCode_Type()
)
dot11ReasonCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11ReasonCode.setStatus("current")
_Dot11ApIpAddress_Type = IpAddress
_Dot11ApIpAddress_Object = MibScalar
dot11ApIpAddress = _Dot11ApIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 1, 5),
    _Dot11ApIpAddress_Type()
)
dot11ApIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11ApIpAddress.setStatus("current")
_Dot1xAuthenticatorMacAddr_Type = MacAddress
_Dot1xAuthenticatorMacAddr_Object = MibScalar
dot1xAuthenticatorMacAddr = _Dot1xAuthenticatorMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 1, 6),
    _Dot1xAuthenticatorMacAddr_Type()
)
dot1xAuthenticatorMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1xAuthenticatorMacAddr.setStatus("current")
_Dot11Notifications_ObjectIdentity = ObjectIdentity
dot11Notifications = _Dot11Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2)
)
_Dot11AuthenticationSupplicantTable_Object = MibTable
dot11AuthenticationSupplicantTable = _Dot11AuthenticationSupplicantTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 5)
)
if mibBuilder.loadTexts:
    dot11AuthenticationSupplicantTable.setStatus("current")
_Dot11AuthenticationSupplicantEntry_Object = MibTableRow
dot11AuthenticationSupplicantEntry = _Dot11AuthenticationSupplicantEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 5, 1)
)
dot11AuthenticationSupplicantEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "dot11AuthenticationSuppIndex"),
)
if mibBuilder.loadTexts:
    dot11AuthenticationSupplicantEntry.setStatus("current")
_Dot118021xSuppIndex_Type = Integer32
_Dot118021xSuppIndex_Object = MibTableColumn
dot118021xSuppIndex = _Dot118021xSuppIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 5, 1, 4),
    _Dot118021xSuppPasswd_Type()
)
dot118021xSuppPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot118021xSuppPasswd.setStatus("current")
_Dot11VapAuthenticationTable_Object = MibTable
dot11VapAuthenticationTable = _Dot11VapAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 6)
)
if mibBuilder.loadTexts:
    dot11VapAuthenticationTable.setStatus("current")
_Dot11VapAuthenticationEntry_Object = MibTableRow
dot11VapAuthenticationEntry = _Dot11VapAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 6, 1)
)
dot11VapAuthenticationEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "dot11Vap8021xIndex"),
)
if mibBuilder.loadTexts:
    dot11VapAuthenticationEntry.setStatus("current")
_Dot11Vap8021xIndex_Type = Integer32
_Dot11Vap8021xIndex_Object = MibTableColumn
dot11Vap8021xIndex = _Dot11Vap8021xIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 6, 1, 1),
    _Dot11Vap8021xIndex_Type()
)
dot11Vap8021xIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot11Vap8021xIndex.setStatus("current")


class _Dot11Vap8021xState_Type(Integer32):
    """Custom type dot11Vap8021xState based on Integer32"""
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


_Dot11Vap8021xState_Type.__name__ = "Integer32"
_Dot11Vap8021xState_Object = MibTableColumn
dot11Vap8021xState = _Dot11Vap8021xState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 6, 1, 2),
    _Dot11Vap8021xState_Type()
)
dot11Vap8021xState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Vap8021xState.setStatus("current")


class _Dot11Vap8021xBroadcastKeyRefreshRate_Type(Integer32):
    """Custom type dot11Vap8021xBroadcastKeyRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Dot11Vap8021xBroadcastKeyRefreshRate_Type.__name__ = "Integer32"
_Dot11Vap8021xBroadcastKeyRefreshRate_Object = MibTableColumn
dot11Vap8021xBroadcastKeyRefreshRate = _Dot11Vap8021xBroadcastKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 6, 1, 3),
    _Dot11Vap8021xBroadcastKeyRefreshRate_Type()
)
dot11Vap8021xBroadcastKeyRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Vap8021xBroadcastKeyRefreshRate.setStatus("current")


class _Dot11Vap8021xSessionKeyRefreshRate_Type(Integer32):
    """Custom type dot11Vap8021xSessionKeyRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Dot11Vap8021xSessionKeyRefreshRate_Type.__name__ = "Integer32"
_Dot11Vap8021xSessionKeyRefreshRate_Object = MibTableColumn
dot11Vap8021xSessionKeyRefreshRate = _Dot11Vap8021xSessionKeyRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 6, 1, 4),
    _Dot11Vap8021xSessionKeyRefreshRate_Type()
)
dot11Vap8021xSessionKeyRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Vap8021xSessionKeyRefreshRate.setStatus("current")


class _Dot11Vap8021xReauthenticationTimeout_Type(Integer32):
    """Custom type dot11Vap8021xReauthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Dot11Vap8021xReauthenticationTimeout_Type.__name__ = "Integer32"
_Dot11Vap8021xReauthenticationTimeout_Object = MibTableColumn
dot11Vap8021xReauthenticationTimeout = _Dot11Vap8021xReauthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 6, 1, 5),
    _Dot11Vap8021xReauthenticationTimeout_Type()
)
dot11Vap8021xReauthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Vap8021xReauthenticationTimeout.setStatus("current")


class _Dot11VapAuthMACAuthenticationType_Type(Integer32):
    """Custom type dot11VapAuthMACAuthenticationType based on Integer32"""
    defaultValue = 0

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
          ("remote", 2))
    )


_Dot11VapAuthMACAuthenticationType_Type.__name__ = "Integer32"
_Dot11VapAuthMACAuthenticationType_Object = MibTableColumn
dot11VapAuthMACAuthenticationType = _Dot11VapAuthMACAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 6, 1, 6),
    _Dot11VapAuthMACAuthenticationType_Type()
)
dot11VapAuthMACAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11VapAuthMACAuthenticationType.setStatus("current")


class _Dot11VapAuthMACAuthenticationTimeout_Type(Integer32):
    """Custom type dot11VapAuthMACAuthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Dot11VapAuthMACAuthenticationTimeout_Type.__name__ = "Integer32"
_Dot11VapAuthMACAuthenticationTimeout_Object = MibTableColumn
dot11VapAuthMACAuthenticationTimeout = _Dot11VapAuthMACAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 6, 1, 7),
    _Dot11VapAuthMACAuthenticationTimeout_Type()
)
dot11VapAuthMACAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11VapAuthMACAuthenticationTimeout.setStatus("current")
_EnterpriseApAdmin_ObjectIdentity = ObjectIdentity
enterpriseApAdmin = _EnterpriseApAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 8)
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 8, 1),
    _EnterpriseApAdminUser_Type()
)
enterpriseApAdminUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApAdminUser.setStatus("current")


class _EnterpriseApAdminPassword_Type(DisplayString):
    """Custom type enterpriseApAdminPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EnterpriseApAdminPassword_Type.__name__ = "DisplayString"
_EnterpriseApAdminPassword_Object = MibScalar
enterpriseApAdminPassword = _EnterpriseApAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 8, 2),
    _EnterpriseApAdminPassword_Type()
)
enterpriseApAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApAdminPassword.setStatus("current")
_EnterpriseApVLAN_ObjectIdentity = ObjectIdentity
enterpriseApVLAN = _EnterpriseApVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 9)
)
_EnterpriseApVLANNativeId_Type = Integer32
_EnterpriseApVLANNativeId_Object = MibScalar
enterpriseApVLANNativeId = _EnterpriseApVLANNativeId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 9, 1),
    _EnterpriseApVLANNativeId_Type()
)
enterpriseApVLANNativeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVLANNativeId.setStatus("current")


class _EnterpriseApVLANState_Type(Integer32):
    """Custom type enterpriseApVLANState based on Integer32"""
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


_EnterpriseApVLANState_Type.__name__ = "Integer32"
_EnterpriseApVLANState_Object = MibScalar
enterpriseApVLANState = _EnterpriseApVLANState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 9, 2),
    _EnterpriseApVLANState_Type()
)
enterpriseApVLANState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApVLANState.setStatus("current")
_EnterpriseApNativeVlanTable_Object = MibTable
enterpriseApNativeVlanTable = _EnterpriseApNativeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 9, 3)
)
if mibBuilder.loadTexts:
    enterpriseApNativeVlanTable.setStatus("mandatory")
_EnterpriseApNativeVlanEntry_Object = MibTableRow
enterpriseApNativeVlanEntry = _EnterpriseApNativeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 9, 3, 1)
)
enterpriseApNativeVlanEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "nativeVlanIfIndex"),
    (0, "AP80-PRIVATE-MIB", "nativeVlanSsidNumber"),
)
if mibBuilder.loadTexts:
    enterpriseApNativeVlanEntry.setStatus("mandatory")
_NativeVlanIfIndex_Type = Integer32
_NativeVlanIfIndex_Object = MibTableColumn
nativeVlanIfIndex = _NativeVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 9, 3, 1, 1),
    _NativeVlanIfIndex_Type()
)
nativeVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nativeVlanIfIndex.setStatus("mandatory")
_NativeVlanSsidNumber_Type = Integer32
_NativeVlanSsidNumber_Object = MibTableColumn
nativeVlanSsidNumber = _NativeVlanSsidNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 9, 3, 1, 2),
    _NativeVlanSsidNumber_Type()
)
nativeVlanSsidNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nativeVlanSsidNumber.setStatus("mandatory")
_NativeVlanVlanId_Type = Integer32
_NativeVlanVlanId_Object = MibTableColumn
nativeVlanVlanId = _NativeVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 9, 3, 1, 3),
    _NativeVlanVlanId_Type()
)
nativeVlanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nativeVlanVlanId.setStatus("mandatory")
_EnterpriseApFilterControl_ObjectIdentity = ObjectIdentity
enterpriseApFilterControl = _EnterpriseApFilterControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10)
)


class _EnterpriseApFilterControlInterClientSTAsCommun_Type(Integer32):
    """Custom type enterpriseApFilterControlInterClientSTAsCommun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("PreventInterAndIntraVAPClient", 3),
          ("PreventIntraVAPClient", 2),
          ("disabled", 1))
    )


_EnterpriseApFilterControlInterClientSTAsCommun_Type.__name__ = "Integer32"
_EnterpriseApFilterControlInterClientSTAsCommun_Object = MibScalar
enterpriseApFilterControlInterClientSTAsCommun = _EnterpriseApFilterControlInterClientSTAsCommun_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 1),
    _EnterpriseApFilterControlInterClientSTAsCommun_Type()
)
enterpriseApFilterControlInterClientSTAsCommun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApFilterControlInterClientSTAsCommun.setStatus("current")


class _EnterpriseApFilterControlAPManage_Type(Integer32):
    """Custom type enterpriseApFilterControlAPManage based on Integer32"""
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


_EnterpriseApFilterControlAPManage_Type.__name__ = "Integer32"
_EnterpriseApFilterControlAPManage_Object = MibScalar
enterpriseApFilterControlAPManage = _EnterpriseApFilterControlAPManage_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 2),
    _EnterpriseApFilterControlAPManage_Type()
)
enterpriseApFilterControlAPManage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApFilterControlAPManage.setStatus("current")


class _EnterpriseApFilterControlEthernet_Type(Integer32):
    """Custom type enterpriseApFilterControlEthernet based on Integer32"""
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


_EnterpriseApFilterControlEthernet_Type.__name__ = "Integer32"
_EnterpriseApFilterControlEthernet_Object = MibScalar
enterpriseApFilterControlEthernet = _EnterpriseApFilterControlEthernet_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 3),
    _EnterpriseApFilterControlEthernet_Type()
)
enterpriseApFilterControlEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApFilterControlEthernet.setStatus("current")
_EnterpriseApFilterProtocolTable_Object = MibTable
enterpriseApFilterProtocolTable = _EnterpriseApFilterProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 4)
)
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolTable.setStatus("current")
_EnterpriseApFilterProtocolEntry_Object = MibTableRow
enterpriseApFilterProtocolEntry = _EnterpriseApFilterProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 4, 1)
)
enterpriseApFilterProtocolEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApFilterProtocolIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolEntry.setStatus("current")
_EnterpriseApFilterProtocolIndex_Type = Integer32
_EnterpriseApFilterProtocolIndex_Object = MibTableColumn
enterpriseApFilterProtocolIndex = _EnterpriseApFilterProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 4, 1, 1),
    _EnterpriseApFilterProtocolIndex_Type()
)
enterpriseApFilterProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolIndex.setStatus("current")
_EnterpriseApFilterProtocolName_Type = DisplayString
_EnterpriseApFilterProtocolName_Object = MibTableColumn
enterpriseApFilterProtocolName = _EnterpriseApFilterProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 4, 1, 2),
    _EnterpriseApFilterProtocolName_Type()
)
enterpriseApFilterProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolName.setStatus("current")
_EnterpriseApFilterProtocolISODesignator_Type = DisplayString
_EnterpriseApFilterProtocolISODesignator_Object = MibTableColumn
enterpriseApFilterProtocolISODesignator = _EnterpriseApFilterProtocolISODesignator_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 4, 1, 3),
    _EnterpriseApFilterProtocolISODesignator_Type()
)
enterpriseApFilterProtocolISODesignator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolISODesignator.setStatus("current")


class _EnterpriseApFilterProtocolState_Type(Integer32):
    """Custom type enterpriseApFilterProtocolState based on Integer32"""
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


_EnterpriseApFilterProtocolState_Type.__name__ = "Integer32"
_EnterpriseApFilterProtocolState_Object = MibTableColumn
enterpriseApFilterProtocolState = _EnterpriseApFilterProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 4, 1, 4),
    _EnterpriseApFilterProtocolState_Type()
)
enterpriseApFilterProtocolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApFilterProtocolState.setStatus("current")
_EnterpriseApFilterUplinkPortMACAddrFilter_ObjectIdentity = ObjectIdentity
enterpriseApFilterUplinkPortMACAddrFilter = _EnterpriseApFilterUplinkPortMACAddrFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 5)
)


class _UplinkPortMACAddrFilterStatus_Type(Integer32):
    """Custom type uplinkPortMACAddrFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enable", 1))
    )


_UplinkPortMACAddrFilterStatus_Type.__name__ = "Integer32"
_UplinkPortMACAddrFilterStatus_Object = MibScalar
uplinkPortMACAddrFilterStatus = _UplinkPortMACAddrFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 5, 1),
    _UplinkPortMACAddrFilterStatus_Type()
)
uplinkPortMACAddrFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uplinkPortMACAddrFilterStatus.setStatus("current")
_UplinkPortMACAddrFilterAddMac_Type = MacAddress
_UplinkPortMACAddrFilterAddMac_Object = MibScalar
uplinkPortMACAddrFilterAddMac = _UplinkPortMACAddrFilterAddMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 5, 2),
    _UplinkPortMACAddrFilterAddMac_Type()
)
uplinkPortMACAddrFilterAddMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uplinkPortMACAddrFilterAddMac.setStatus("current")
_UplinkPortMACAddrFilteringTable_Object = MibTable
uplinkPortMACAddrFilteringTable = _UplinkPortMACAddrFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 5, 3)
)
if mibBuilder.loadTexts:
    uplinkPortMACAddrFilteringTable.setStatus("current")
_UplinkPortMACAddrFilteringEntry_Object = MibTableRow
uplinkPortMACAddrFilteringEntry = _UplinkPortMACAddrFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 5, 3, 1)
)
uplinkPortMACAddrFilteringEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "uplinkPortMacAddrIndex"),
)
if mibBuilder.loadTexts:
    uplinkPortMACAddrFilteringEntry.setStatus("current")
_UplinkPortMacAddrIndex_Type = Integer32
_UplinkPortMacAddrIndex_Object = MibTableColumn
uplinkPortMacAddrIndex = _UplinkPortMacAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 5, 3, 1, 1),
    _UplinkPortMacAddrIndex_Type()
)
uplinkPortMacAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplinkPortMacAddrIndex.setStatus("current")
_UplinkPortMACAddr_Type = MacAddress
_UplinkPortMACAddr_Object = MibTableColumn
uplinkPortMACAddr = _UplinkPortMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 5, 3, 1, 2),
    _UplinkPortMACAddr_Type()
)
uplinkPortMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplinkPortMACAddr.setStatus("current")


class _DeleteMacAddr_Type(Integer32):
    """Custom type deleteMacAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Delete", 1),
          ("Nothing", 2))
    )


_DeleteMacAddr_Type.__name__ = "Integer32"
_DeleteMacAddr_Object = MibTableColumn
deleteMacAddr = _DeleteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 10, 5, 3, 1, 3),
    _DeleteMacAddr_Type()
)
deleteMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deleteMacAddr.setStatus("current")
_EnterpriseApSNTP_ObjectIdentity = ObjectIdentity
enterpriseApSNTP = _EnterpriseApSNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11)
)


class _EnterpriseApSNTPState_Type(Integer32):
    """Custom type enterpriseApSNTPState based on Integer32"""
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


_EnterpriseApSNTPState_Type.__name__ = "Integer32"
_EnterpriseApSNTPState_Object = MibScalar
enterpriseApSNTPState = _EnterpriseApSNTPState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 1),
    _EnterpriseApSNTPState_Type()
)
enterpriseApSNTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNTPState.setStatus("current")
_EnterpriseApSNTPPrimaryServer_Type = IpAddress
_EnterpriseApSNTPPrimaryServer_Object = MibScalar
enterpriseApSNTPPrimaryServer = _EnterpriseApSNTPPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 2),
    _EnterpriseApSNTPPrimaryServer_Type()
)
enterpriseApSNTPPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNTPPrimaryServer.setStatus("current")
_EnterpriseApSNTPSecondaryServer_Type = IpAddress
_EnterpriseApSNTPSecondaryServer_Object = MibScalar
enterpriseApSNTPSecondaryServer = _EnterpriseApSNTPSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 3),
    _EnterpriseApSNTPSecondaryServer_Type()
)
enterpriseApSNTPSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNTPSecondaryServer.setStatus("current")


class _EnterpriseApSNTPTimezone_Type(Integer32):
    """Custom type enterpriseApSNTPTimezone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53)
        )
    )
    namedValues = NamedValues(
        *(("abuDhabi", 39),
          ("alaska", 3),
          ("almaty", 42),
          ("amsterdam", 24),
          ("arizona", 5),
          ("athens", 30),
          ("atlantic", 13),
          ("azores", 20),
          ("baghdad", 36),
          ("bangkok", 43),
          ("beijing", 44),
          ("bogota", 10),
          ("brasilia", 17),
          ("bratislava", 26),
          ("brisbane", 47),
          ("bucharest", 31),
          ("buenos", 18),
          ("cairo", 32),
          ("canberra", 48),
          ("caracas", 14),
          ("casablanca", 21),
          ("central", 7),
          ("eastern", 11),
          ("enewetakKwajalein", 0),
          ("fiji", 52),
          ("greenwichMeanTimeDublin", 22),
          ("greenwichMeanTimeLisbon", 23),
          ("guam", 49),
          ("harare", 33),
          ("hawaii", 2),
          ("helsinki", 34),
          ("hobart", 50),
          ("indiana", 12),
          ("islamabad", 41),
          ("israel", 35),
          ("magadan", 51),
          ("mexicoCity", 8),
          ("midAtlantic", 19),
          ("midwayIsland", 1),
          ("moscow", 37),
          ("mountain", 6),
          ("newfoundland", 16),
          ("pacific", 4),
          ("paris", 28),
          ("prague", 27),
          ("santiago", 15),
          ("saskatchewan", 9),
          ("sofija", 29),
          ("stockhoim", 25),
          ("taipei", 45),
          ("tehran", 38),
          ("tokyo", 46),
          ("vogograd", 40),
          ("wellington", 53))
    )


_EnterpriseApSNTPTimezone_Type.__name__ = "Integer32"
_EnterpriseApSNTPTimezone_Object = MibScalar
enterpriseApSNTPTimezone = _EnterpriseApSNTPTimezone_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 4),
    _EnterpriseApSNTPTimezone_Type()
)
enterpriseApSNTPTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNTPTimezone.setStatus("current")


class _EnterpriseApSNTPDST_Type(Integer32):
    """Custom type enterpriseApSNTPDST based on Integer32"""
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


_EnterpriseApSNTPDST_Type.__name__ = "Integer32"
_EnterpriseApSNTPDST_Object = MibScalar
enterpriseApSNTPDST = _EnterpriseApSNTPDST_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 5),
    _EnterpriseApSNTPDST_Type()
)
enterpriseApSNTPDST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNTPDST.setStatus("current")


class _EnterpriseApSNTPDSTStartMonth_Type(Integer32):
    """Custom type enterpriseApSNTPDSTStartMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EnterpriseApSNTPDSTStartMonth_Type.__name__ = "Integer32"
_EnterpriseApSNTPDSTStartMonth_Object = MibScalar
enterpriseApSNTPDSTStartMonth = _EnterpriseApSNTPDSTStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 6),
    _EnterpriseApSNTPDSTStartMonth_Type()
)
enterpriseApSNTPDSTStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNTPDSTStartMonth.setStatus("current")


class _EnterpriseApSNTPDSTStartDay_Type(Integer32):
    """Custom type enterpriseApSNTPDSTStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_EnterpriseApSNTPDSTStartDay_Type.__name__ = "Integer32"
_EnterpriseApSNTPDSTStartDay_Object = MibScalar
enterpriseApSNTPDSTStartDay = _EnterpriseApSNTPDSTStartDay_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 7),
    _EnterpriseApSNTPDSTStartDay_Type()
)
enterpriseApSNTPDSTStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNTPDSTStartDay.setStatus("current")


class _EnterpriseApSNTPDSTEndMonth_Type(Integer32):
    """Custom type enterpriseApSNTPDSTEndMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EnterpriseApSNTPDSTEndMonth_Type.__name__ = "Integer32"
_EnterpriseApSNTPDSTEndMonth_Object = MibScalar
enterpriseApSNTPDSTEndMonth = _EnterpriseApSNTPDSTEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 8),
    _EnterpriseApSNTPDSTEndMonth_Type()
)
enterpriseApSNTPDSTEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNTPDSTEndMonth.setStatus("current")


class _EnterpriseApSNTPDSTEndDay_Type(Integer32):
    """Custom type enterpriseApSNTPDSTEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_EnterpriseApSNTPDSTEndDay_Type.__name__ = "Integer32"
_EnterpriseApSNTPDSTEndDay_Object = MibScalar
enterpriseApSNTPDSTEndDay = _EnterpriseApSNTPDSTEndDay_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 9),
    _EnterpriseApSNTPDSTEndDay_Type()
)
enterpriseApSNTPDSTEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNTPDSTEndDay.setStatus("current")
_SntpNotificationTree_ObjectIdentity = ObjectIdentity
sntpNotificationTree = _SntpNotificationTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 10)
)
_SntpNotificationObjects_ObjectIdentity = ObjectIdentity
sntpNotificationObjects = _SntpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 10, 1)
)
_SntpNotifications_ObjectIdentity = ObjectIdentity
sntpNotifications = _SntpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 10, 2)
)
_EnterpriseApDNS_ObjectIdentity = ObjectIdentity
enterpriseApDNS = _EnterpriseApDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 12)
)
_EnterpriseApDNSPrimaryServer_Type = IpAddress
_EnterpriseApDNSPrimaryServer_Object = MibScalar
enterpriseApDNSPrimaryServer = _EnterpriseApDNSPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 12, 1),
    _EnterpriseApDNSPrimaryServer_Type()
)
enterpriseApDNSPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApDNSPrimaryServer.setStatus("current")
_EnterpriseApDNSSecondaryServer_Type = IpAddress
_EnterpriseApDNSSecondaryServer_Object = MibScalar
enterpriseApDNSSecondaryServer = _EnterpriseApDNSSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 12, 2),
    _EnterpriseApDNSSecondaryServer_Type()
)
enterpriseApDNSSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApDNSSecondaryServer.setStatus("current")
_EnterpriseApSyslog_ObjectIdentity = ObjectIdentity
enterpriseApSyslog = _EnterpriseApSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 13)
)


class _EnterpriseApSyslogState_Type(Integer32):
    """Custom type enterpriseApSyslogState based on Integer32"""
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


_EnterpriseApSyslogState_Type.__name__ = "Integer32"
_EnterpriseApSyslogState_Object = MibScalar
enterpriseApSyslogState = _EnterpriseApSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 13, 1),
    _EnterpriseApSyslogState_Type()
)
enterpriseApSyslogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSyslogState.setStatus("current")


class _EnterpriseApSyslogConsoleState_Type(Integer32):
    """Custom type enterpriseApSyslogConsoleState based on Integer32"""
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


_EnterpriseApSyslogConsoleState_Type.__name__ = "Integer32"
_EnterpriseApSyslogConsoleState_Object = MibScalar
enterpriseApSyslogConsoleState = _EnterpriseApSyslogConsoleState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 13, 2),
    _EnterpriseApSyslogConsoleState_Type()
)
enterpriseApSyslogConsoleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSyslogConsoleState.setStatus("current")


class _EnterpriseApSyslogLevel_Type(Integer32):
    """Custom type enterpriseApSyslogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_EnterpriseApSyslogLevel_Type.__name__ = "Integer32"
_EnterpriseApSyslogLevel_Object = MibScalar
enterpriseApSyslogLevel = _EnterpriseApSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 13, 3),
    _EnterpriseApSyslogLevel_Type()
)
enterpriseApSyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSyslogLevel.setStatus("current")
_EnterpriseApSyslogServerTable_Object = MibTable
enterpriseApSyslogServerTable = _EnterpriseApSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 13, 4)
)
if mibBuilder.loadTexts:
    enterpriseApSyslogServerTable.setStatus("current")
_EnterpriseApSyslogServerEntry_Object = MibTableRow
enterpriseApSyslogServerEntry = _EnterpriseApSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 13, 4, 1)
)
enterpriseApSyslogServerEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApSyslogServerEntry.setStatus("current")
_EnterpriseApSyslogServerIndex_Type = Integer32
_EnterpriseApSyslogServerIndex_Object = MibTableColumn
enterpriseApSyslogServerIndex = _EnterpriseApSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 13, 4, 1, 1),
    _EnterpriseApSyslogServerIndex_Type()
)
enterpriseApSyslogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApSyslogServerIndex.setStatus("current")


class _EnterpriseApSyslogServerState_Type(Integer32):
    """Custom type enterpriseApSyslogServerState based on Integer32"""
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


_EnterpriseApSyslogServerState_Type.__name__ = "Integer32"
_EnterpriseApSyslogServerState_Object = MibTableColumn
enterpriseApSyslogServerState = _EnterpriseApSyslogServerState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 13, 4, 1, 2),
    _EnterpriseApSyslogServerState_Type()
)
enterpriseApSyslogServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSyslogServerState.setStatus("current")
_EnterpriseApSyslogServerIPAddress_Type = IpAddress
_EnterpriseApSyslogServerIPAddress_Object = MibTableColumn
enterpriseApSyslogServerIPAddress = _EnterpriseApSyslogServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 13, 4, 1, 3),
    _EnterpriseApSyslogServerIPAddress_Type()
)
enterpriseApSyslogServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSyslogServerIPAddress.setStatus("current")


class _EnterpriseApSyslogServerPort_Type(Integer32):
    """Custom type enterpriseApSyslogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_EnterpriseApSyslogServerPort_Type.__name__ = "Integer32"
_EnterpriseApSyslogServerPort_Object = MibTableColumn
enterpriseApSyslogServerPort = _EnterpriseApSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 13, 4, 1, 4),
    _EnterpriseApSyslogServerPort_Type()
)
enterpriseApSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSyslogServerPort.setStatus("current")
_EnterpriseApSecurity_ObjectIdentity = ObjectIdentity
enterpriseApSecurity = _EnterpriseApSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14)
)
_EnterpriseApSecurityTable_Object = MibTable
enterpriseApSecurityTable = _EnterpriseApSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1)
)
if mibBuilder.loadTexts:
    enterpriseApSecurityTable.setStatus("current")
_EnterpriseApSecurityEntry_Object = MibTableRow
enterpriseApSecurityEntry = _EnterpriseApSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1)
)
enterpriseApSecurityEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApSecurityIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApSecurityEntry.setStatus("current")
_EnterpriseApSecurityIndex_Type = Integer32
_EnterpriseApSecurityIndex_Object = MibTableColumn
enterpriseApSecurityIndex = _EnterpriseApSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 1),
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
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 0),
          ("sharedkey", 1),
          ("wpa", 2),
          ("wpa2", 6),
          ("wpa2psk", 7),
          ("wpapsk", 3),
          ("wpawpa2mixed", 4),
          ("wpawpa2pskmixed", 5))
    )


_EnterpriseApSecurityAuthType_Type.__name__ = "Integer32"
_EnterpriseApSecurityAuthType_Object = MibTableColumn
enterpriseApSecurityAuthType = _EnterpriseApSecurityAuthType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 6),
    _EnterpriseApSecurityWPACipher_Type()
)
enterpriseApSecurityWPACipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWPACipher.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 7),
    _EnterpriseApSecurityWPAPSKType_Type()
)
enterpriseApSecurityWPAPSKType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWPAPSKType.setStatus("current")


class _EnterpriseApSecurityWPAPSK_Type(DisplayString):
    """Custom type enterpriseApSecurityWPAPSK based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnterpriseApSecurityWPAPSK_Type.__name__ = "DisplayString"
_EnterpriseApSecurityWPAPSK_Object = MibTableColumn
enterpriseApSecurityWPAPSK = _EnterpriseApSecurityWPAPSK_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 9),
    _EnterpriseApSecurityWEPKeyType_Type()
)
enterpriseApSecurityWEPKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWEPKeyType.setStatus("current")
_EnterpriseApSecurityWEPEnabled_Type = TruthValue
_EnterpriseApSecurityWEPEnabled_Object = MibTableColumn
enterpriseApSecurityWEPEnabled = _EnterpriseApSecurityWEPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 10),
    _EnterpriseApSecurityWEPEnabled_Type()
)
enterpriseApSecurityWEPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWEPEnabled.setStatus("current")


class _EnterpriseApSecurityWPACipherSuite_Type(Integer32):
    """Custom type enterpriseApSecurityWPACipherSuite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes-ccmp", 0),
          ("tkip", 1),
          ("wep", 2))
    )


_EnterpriseApSecurityWPACipherSuite_Type.__name__ = "Integer32"
_EnterpriseApSecurityWPACipherSuite_Object = MibTableColumn
enterpriseApSecurityWPACipherSuite = _EnterpriseApSecurityWPACipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 11),
    _EnterpriseApSecurityWPACipherSuite_Type()
)
enterpriseApSecurityWPACipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWPACipherSuite.setStatus("current")


class _EnterpriseApSecurityWPAPreAuthentication_Type(Integer32):
    """Custom type enterpriseApSecurityWPAPreAuthentication based on Integer32"""
    defaultValue = 2

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


_EnterpriseApSecurityWPAPreAuthentication_Type.__name__ = "Integer32"
_EnterpriseApSecurityWPAPreAuthentication_Object = MibTableColumn
enterpriseApSecurityWPAPreAuthentication = _EnterpriseApSecurityWPAPreAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 12),
    _EnterpriseApSecurityWPAPreAuthentication_Type()
)
enterpriseApSecurityWPAPreAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWPAPreAuthentication.setStatus("current")


class _EnterpriseApSecurityWPAPmksaLifetime_Type(Integer32):
    """Custom type enterpriseApSecurityWPAPmksaLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_EnterpriseApSecurityWPAPmksaLifetime_Type.__name__ = "Integer32"
_EnterpriseApSecurityWPAPmksaLifetime_Object = MibTableColumn
enterpriseApSecurityWPAPmksaLifetime = _EnterpriseApSecurityWPAPmksaLifetime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 1, 1, 13),
    _EnterpriseApSecurityWPAPmksaLifetime_Type()
)
enterpriseApSecurityWPAPmksaLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSecurityWPAPmksaLifetime.setStatus("current")
_EnterpriseApSsh_ObjectIdentity = ObjectIdentity
enterpriseApSsh = _EnterpriseApSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 2)
)
_EnterpriseApSshServerEnabled_Type = TruthValue
_EnterpriseApSshServerEnabled_Object = MibScalar
enterpriseApSshServerEnabled = _EnterpriseApSshServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 2, 1),
    _EnterpriseApSshServerEnabled_Type()
)
enterpriseApSshServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSshServerEnabled.setStatus("mandatory")


class _EnterpriseApSshServerPort_Type(Integer32):
    """Custom type enterpriseApSshServerPort based on Integer32"""
    defaultValue = 22


_EnterpriseApSshServerPort_Object = MibScalar
enterpriseApSshServerPort = _EnterpriseApSshServerPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 2, 2),
    _EnterpriseApSshServerPort_Type()
)
enterpriseApSshServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSshServerPort.setStatus("mandatory")
_EnterpriseApSshTelnetServerEnabled_Type = TruthValue
_EnterpriseApSshTelnetServerEnabled_Object = MibScalar
enterpriseApSshTelnetServerEnabled = _EnterpriseApSshTelnetServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 14, 2, 3),
    _EnterpriseApSshTelnetServerEnabled_Type()
)
enterpriseApSshTelnetServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSshTelnetServerEnabled.setStatus("mandatory")
_EnterpriseApRadio_ObjectIdentity = ObjectIdentity
enterpriseApRadio = _EnterpriseApRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15)
)
_EnterpriseApRadioTable_Object = MibTable
enterpriseApRadioTable = _EnterpriseApRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1)
)
if mibBuilder.loadTexts:
    enterpriseApRadioTable.setStatus("current")
_EnterpriseApRadioEntry_Object = MibTableRow
enterpriseApRadioEntry = _EnterpriseApRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1)
)
enterpriseApRadioEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApRadioIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApRadioEntry.setStatus("current")
_EnterpriseApRadioIndex_Type = Integer32
_EnterpriseApRadioIndex_Object = MibTableColumn
enterpriseApRadioIndex = _EnterpriseApRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 1),
    _EnterpriseApRadioIndex_Type()
)
enterpriseApRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApRadioIndex.setStatus("current")


class _EnterpriseApRadioState_Type(Integer32):
    """Custom type enterpriseApRadioState based on Integer32"""
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


_EnterpriseApRadioState_Type.__name__ = "Integer32"
_EnterpriseApRadioState_Object = MibTableColumn
enterpriseApRadioState = _EnterpriseApRadioState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 2),
    _EnterpriseApRadioState_Type()
)
enterpriseApRadioState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioState.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 3),
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
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eighth", 1),
          ("full", 4),
          ("half", 3),
          ("min", 0),
          ("quarter", 2))
    )


_EnterpriseApRadioTransmitPower_Type.__name__ = "Integer32"
_EnterpriseApRadioTransmitPower_Object = MibTableColumn
enterpriseApRadioTransmitPower = _EnterpriseApRadioTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 4),
    _EnterpriseApRadioTransmitPower_Type()
)
enterpriseApRadioTransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioTransmitPower.setStatus("current")


class _EnterpriseApRadioClosedSystem_Type(Integer32):
    """Custom type enterpriseApRadioClosedSystem based on Integer32"""
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


_EnterpriseApRadioClosedSystem_Type.__name__ = "Integer32"
_EnterpriseApRadioClosedSystem_Object = MibTableColumn
enterpriseApRadioClosedSystem = _EnterpriseApRadioClosedSystem_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 5),
    _EnterpriseApRadioClosedSystem_Type()
)
enterpriseApRadioClosedSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioClosedSystem.setStatus("obsolete")


class _EnterpriseApRadioMaxAssoc_Type(Integer32):
    """Custom type enterpriseApRadioMaxAssoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EnterpriseApRadioMaxAssoc_Type.__name__ = "Integer32"
_EnterpriseApRadioMaxAssoc_Object = MibTableColumn
enterpriseApRadioMaxAssoc = _EnterpriseApRadioMaxAssoc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 6),
    _EnterpriseApRadioMaxAssoc_Type()
)
enterpriseApRadioMaxAssoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioMaxAssoc.setStatus("obsolete")


class _EnterpriseApRadioTransmitKey_Type(Integer32):
    """Custom type enterpriseApRadioTransmitKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnterpriseApRadioTransmitKey_Type.__name__ = "Integer32"
_EnterpriseApRadioTransmitKey_Object = MibTableColumn
enterpriseApRadioTransmitKey = _EnterpriseApRadioTransmitKey_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 7),
    _EnterpriseApRadioTransmitKey_Type()
)
enterpriseApRadioTransmitKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioTransmitKey.setStatus("obsolete")


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
        *(("disabled", 1),
          ("dynamic-turbo", 3),
          ("static-turbo", 2))
    )


_EnterpriseApRadioTurboMode_Type.__name__ = "Integer32"
_EnterpriseApRadioTurboMode_Object = MibTableColumn
enterpriseApRadioTurboMode = _EnterpriseApRadioTurboMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 8),
    _EnterpriseApRadioTurboMode_Type()
)
enterpriseApRadioTurboMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioTurboMode.setStatus("current")


class _EnterpriseApRadioDescription_Type(DisplayString):
    """Custom type enterpriseApRadioDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnterpriseApRadioDescription_Type.__name__ = "DisplayString"
_EnterpriseApRadioDescription_Object = MibTableColumn
enterpriseApRadioDescription = _EnterpriseApRadioDescription_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 9),
    _EnterpriseApRadioDescription_Type()
)
enterpriseApRadioDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioDescription.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 10),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("bOnly", 1),
          ("bg", 3),
          ("gOnly", 2))
    )


_EnterpriseApRadioGMode_Type.__name__ = "Integer32"
_EnterpriseApRadioGMode_Object = MibTableColumn
enterpriseApRadioGMode = _EnterpriseApRadioGMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 11),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("fixed", 1))
    )


_EnterpriseApRadioAntennaMode_Type.__name__ = "Integer32"
_EnterpriseApRadioAntennaMode_Object = MibTableColumn
enterpriseApRadioAntennaMode = _EnterpriseApRadioAntennaMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 12),
    _EnterpriseApRadioAntennaMode_Type()
)
enterpriseApRadioAntennaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioAntennaMode.setStatus("mandatory")
_EnterpriseApRadioAntennaId_Type = DisplayString
_EnterpriseApRadioAntennaId_Object = MibTableColumn
enterpriseApRadioAntennaId = _EnterpriseApRadioAntennaId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 13),
    _EnterpriseApRadioAntennaId_Type()
)
enterpriseApRadioAntennaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApRadioAntennaId.setStatus("current")


class _EnterpriseApRadioAntennaControlMethod_Type(Integer32):
    """Custom type enterpriseApRadioAntennaControlMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("Diversity", 1),
          ("Left", 2),
          ("Right", 3))
    )


_EnterpriseApRadioAntennaControlMethod_Type.__name__ = "Integer32"
_EnterpriseApRadioAntennaControlMethod_Object = MibTableColumn
enterpriseApRadioAntennaControlMethod = _EnterpriseApRadioAntennaControlMethod_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 14),
    _EnterpriseApRadioAntennaControlMethod_Type()
)
enterpriseApRadioAntennaControlMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioAntennaControlMethod.setStatus("current")


class _EnterpriseApRadioAntennaLocation_Type(Integer32):
    """Custom type enterpriseApRadioAntennaLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Indoor", 1),
          ("Outdoor", 2))
    )


_EnterpriseApRadioAntennaLocation_Type.__name__ = "Integer32"
_EnterpriseApRadioAntennaLocation_Object = MibTableColumn
enterpriseApRadioAntennaLocation = _EnterpriseApRadioAntennaLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 15),
    _EnterpriseApRadioAntennaLocation_Type()
)
enterpriseApRadioAntennaLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioAntennaLocation.setStatus("current")


class _EnterpriseApRadioRogueApDetection_Type(Integer32):
    """Custom type enterpriseApRadioRogueApDetection based on Integer32"""
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


_EnterpriseApRadioRogueApDetection_Type.__name__ = "Integer32"
_EnterpriseApRadioRogueApDetection_Object = MibTableColumn
enterpriseApRadioRogueApDetection = _EnterpriseApRadioRogueApDetection_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 16),
    _EnterpriseApRadioRogueApDetection_Type()
)
enterpriseApRadioRogueApDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioRogueApDetection.setStatus("current")


class _EnterpriseApRadioRogueApScanInterval_Type(Integer32):
    """Custom type enterpriseApRadioRogueApScanInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_EnterpriseApRadioRogueApScanInterval_Type.__name__ = "Integer32"
_EnterpriseApRadioRogueApScanInterval_Object = MibTableColumn
enterpriseApRadioRogueApScanInterval = _EnterpriseApRadioRogueApScanInterval_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 17),
    _EnterpriseApRadioRogueApScanInterval_Type()
)
enterpriseApRadioRogueApScanInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioRogueApScanInterval.setStatus("current")


class _EnterpriseApRadioRogueApScanDuration_Type(Integer32):
    """Custom type enterpriseApRadioRogueApScanDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_EnterpriseApRadioRogueApScanDuration_Type.__name__ = "Integer32"
_EnterpriseApRadioRogueApScanDuration_Object = MibTableColumn
enterpriseApRadioRogueApScanDuration = _EnterpriseApRadioRogueApScanDuration_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 18),
    _EnterpriseApRadioRogueApScanDuration_Type()
)
enterpriseApRadioRogueApScanDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioRogueApScanDuration.setStatus("current")


class _EnterpriseApRadioRogueApScanNow_Type(Integer32):
    """Custom type enterpriseApRadioRogueApScanNow based on Integer32"""
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


_EnterpriseApRadioRogueApScanNow_Type.__name__ = "Integer32"
_EnterpriseApRadioRogueApScanNow_Object = MibTableColumn
enterpriseApRadioRogueApScanNow = _EnterpriseApRadioRogueApScanNow_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 19),
    _EnterpriseApRadioRogueApScanNow_Type()
)
enterpriseApRadioRogueApScanNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioRogueApScanNow.setStatus("current")


class _EnterpriseApRadioMICMode_Type(Integer32):
    """Custom type enterpriseApRadioMICMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("software", 1))
    )


_EnterpriseApRadioMICMode_Type.__name__ = "Integer32"
_EnterpriseApRadioMICMode_Object = MibTableColumn
enterpriseApRadioMICMode = _EnterpriseApRadioMICMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 21),
    _EnterpriseApRadioMICMode_Type()
)
enterpriseApRadioMICMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioMICMode.setStatus("current")


class _EnterpriseApRadioSuperMode_Type(Integer32):
    """Custom type enterpriseApRadioSuperMode based on Integer32"""
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


_EnterpriseApRadioSuperMode_Type.__name__ = "Integer32"
_EnterpriseApRadioSuperMode_Object = MibTableColumn
enterpriseApRadioSuperMode = _EnterpriseApRadioSuperMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 22),
    _EnterpriseApRadioSuperMode_Type()
)
enterpriseApRadioSuperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioSuperMode.setStatus("current")


class _EnterpriseApRadioBeaconInterval_Type(Integer32):
    """Custom type enterpriseApRadioBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_EnterpriseApRadioBeaconInterval_Type.__name__ = "Integer32"
_EnterpriseApRadioBeaconInterval_Object = MibTableColumn
enterpriseApRadioBeaconInterval = _EnterpriseApRadioBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 23),
    _EnterpriseApRadioBeaconInterval_Type()
)
enterpriseApRadioBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioBeaconInterval.setStatus("current")
_EnterpriseApRadioDataBeaconRate_Type = Integer32
_EnterpriseApRadioDataBeaconRate_Object = MibTableColumn
enterpriseApRadioDataBeaconRate = _EnterpriseApRadioDataBeaconRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 24),
    _EnterpriseApRadioDataBeaconRate_Type()
)
enterpriseApRadioDataBeaconRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioDataBeaconRate.setStatus("current")
_EnterpriseApRadioChannel_Type = Integer32
_EnterpriseApRadioChannel_Object = MibTableColumn
enterpriseApRadioChannel = _EnterpriseApRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 25),
    _EnterpriseApRadioChannel_Type()
)
enterpriseApRadioChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioChannel.setStatus("current")


class _EnterpriseApRadioFragmentLength_Type(Integer32):
    """Custom type enterpriseApRadioFragmentLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_EnterpriseApRadioFragmentLength_Type.__name__ = "Integer32"
_EnterpriseApRadioFragmentLength_Object = MibTableColumn
enterpriseApRadioFragmentLength = _EnterpriseApRadioFragmentLength_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 26),
    _EnterpriseApRadioFragmentLength_Type()
)
enterpriseApRadioFragmentLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioFragmentLength.setStatus("current")


class _EnterpriseApRadioRTSThreshold_Type(Integer32):
    """Custom type enterpriseApRadioRTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_EnterpriseApRadioRTSThreshold_Type.__name__ = "Integer32"
_EnterpriseApRadioRTSThreshold_Object = MibTableColumn
enterpriseApRadioRTSThreshold = _EnterpriseApRadioRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 27),
    _EnterpriseApRadioRTSThreshold_Type()
)
enterpriseApRadioRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioRTSThreshold.setStatus("current")


class _EnterpriseApRadioAntennaGainReduction_Type(Integer32):
    """Custom type enterpriseApRadioAntennaGainReduction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_EnterpriseApRadioAntennaGainReduction_Type.__name__ = "Integer32"
_EnterpriseApRadioAntennaGainReduction_Object = MibTableColumn
enterpriseApRadioAntennaGainReduction = _EnterpriseApRadioAntennaGainReduction_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 15, 1, 1, 28),
    _EnterpriseApRadioAntennaGainReduction_Type()
)
enterpriseApRadioAntennaGainReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApRadioAntennaGainReduction.setStatus("current")
_EnterpriseApSNMP_ObjectIdentity = ObjectIdentity
enterpriseApSNMP = _EnterpriseApSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16)
)


class _EnterpriseApSNMPCommunityReadOnly_Type(DisplayString):
    """Custom type enterpriseApSNMPCommunityReadOnly based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnterpriseApSNMPCommunityReadOnly_Type.__name__ = "DisplayString"
_EnterpriseApSNMPCommunityReadOnly_Object = MibScalar
enterpriseApSNMPCommunityReadOnly = _EnterpriseApSNMPCommunityReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 1),
    _EnterpriseApSNMPCommunityReadOnly_Type()
)
enterpriseApSNMPCommunityReadOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNMPCommunityReadOnly.setStatus("current")


class _EnterpriseApSNMPCommunityReadWrite_Type(DisplayString):
    """Custom type enterpriseApSNMPCommunityReadWrite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnterpriseApSNMPCommunityReadWrite_Type.__name__ = "DisplayString"
_EnterpriseApSNMPCommunityReadWrite_Object = MibScalar
enterpriseApSNMPCommunityReadWrite = _EnterpriseApSNMPCommunityReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 2),
    _EnterpriseApSNMPCommunityReadWrite_Type()
)
enterpriseApSNMPCommunityReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNMPCommunityReadWrite.setStatus("current")
_EnterpriseApSNMPTrapDestinationTable_Object = MibTable
enterpriseApSNMPTrapDestinationTable = _EnterpriseApSNMPTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 3)
)
if mibBuilder.loadTexts:
    enterpriseApSNMPTrapDestinationTable.setStatus("current")
_EnterpriseApSNMPTrapDestinationEntry_Object = MibTableRow
enterpriseApSNMPTrapDestinationEntry = _EnterpriseApSNMPTrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 3, 1)
)
enterpriseApSNMPTrapDestinationEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApSNMPTrapDestinationIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApSNMPTrapDestinationEntry.setStatus("current")


class _EnterpriseApSNMPTrapDestinationIndex_Type(Integer32):
    """Custom type enterpriseApSNMPTrapDestinationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnterpriseApSNMPTrapDestinationIndex_Type.__name__ = "Integer32"
_EnterpriseApSNMPTrapDestinationIndex_Object = MibTableColumn
enterpriseApSNMPTrapDestinationIndex = _EnterpriseApSNMPTrapDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 3, 1, 1),
    _EnterpriseApSNMPTrapDestinationIndex_Type()
)
enterpriseApSNMPTrapDestinationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApSNMPTrapDestinationIndex.setStatus("current")


class _EnterpriseApSNMPTrapDestinationCommunity_Type(DisplayString):
    """Custom type enterpriseApSNMPTrapDestinationCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EnterpriseApSNMPTrapDestinationCommunity_Type.__name__ = "DisplayString"
_EnterpriseApSNMPTrapDestinationCommunity_Object = MibTableColumn
enterpriseApSNMPTrapDestinationCommunity = _EnterpriseApSNMPTrapDestinationCommunity_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 3, 1, 2),
    _EnterpriseApSNMPTrapDestinationCommunity_Type()
)
enterpriseApSNMPTrapDestinationCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNMPTrapDestinationCommunity.setStatus("current")
_EnterpriseApSNMPTrapDestinationIP_Type = IpAddress
_EnterpriseApSNMPTrapDestinationIP_Object = MibTableColumn
enterpriseApSNMPTrapDestinationIP = _EnterpriseApSNMPTrapDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 3, 1, 3),
    _EnterpriseApSNMPTrapDestinationIP_Type()
)
enterpriseApSNMPTrapDestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNMPTrapDestinationIP.setStatus("current")


class _EnterpriseApSNMPTrapDestinationState_Type(Integer32):
    """Custom type enterpriseApSNMPTrapDestinationState based on Integer32"""
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


_EnterpriseApSNMPTrapDestinationState_Type.__name__ = "Integer32"
_EnterpriseApSNMPTrapDestinationState_Object = MibTableColumn
enterpriseApSNMPTrapDestinationState = _EnterpriseApSNMPTrapDestinationState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 3, 1, 4),
    _EnterpriseApSNMPTrapDestinationState_Type()
)
enterpriseApSNMPTrapDestinationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSNMPTrapDestinationState.setStatus("current")
_EnterpriseApSNMPTrapFilters_ObjectIdentity = ObjectIdentity
enterpriseApSNMPTrapFilters = _EnterpriseApSNMPTrapFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4)
)


class _SysSystemUpTrapEnabled_Type(Integer32):
    """Custom type sysSystemUpTrapEnabled based on Integer32"""
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


_SysSystemUpTrapEnabled_Type.__name__ = "Integer32"
_SysSystemUpTrapEnabled_Object = MibScalar
sysSystemUpTrapEnabled = _SysSystemUpTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 1),
    _SysSystemUpTrapEnabled_Type()
)
sysSystemUpTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSystemUpTrapEnabled.setStatus("current")


class _SysSystemDownTrapEnabled_Type(Integer32):
    """Custom type sysSystemDownTrapEnabled based on Integer32"""
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


_SysSystemDownTrapEnabled_Type.__name__ = "Integer32"
_SysSystemDownTrapEnabled_Object = MibScalar
sysSystemDownTrapEnabled = _SysSystemDownTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 2),
    _SysSystemDownTrapEnabled_Type()
)
sysSystemDownTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSystemDownTrapEnabled.setStatus("current")


class _SysRadiusServerChangedTrapEnabled_Type(Integer32):
    """Custom type sysRadiusServerChangedTrapEnabled based on Integer32"""
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


_SysRadiusServerChangedTrapEnabled_Type.__name__ = "Integer32"
_SysRadiusServerChangedTrapEnabled_Object = MibScalar
sysRadiusServerChangedTrapEnabled = _SysRadiusServerChangedTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 3),
    _SysRadiusServerChangedTrapEnabled_Type()
)
sysRadiusServerChangedTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRadiusServerChangedTrapEnabled.setStatus("current")


class _SysConfigFileVersionChangedTrapEnabled_Type(Integer32):
    """Custom type sysConfigFileVersionChangedTrapEnabled based on Integer32"""
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


_SysConfigFileVersionChangedTrapEnabled_Type.__name__ = "Integer32"
_SysConfigFileVersionChangedTrapEnabled_Object = MibScalar
sysConfigFileVersionChangedTrapEnabled = _SysConfigFileVersionChangedTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 4),
    _SysConfigFileVersionChangedTrapEnabled_Type()
)
sysConfigFileVersionChangedTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigFileVersionChangedTrapEnabled.setStatus("current")


class _Dot11StationAssociationTrapEnabled_Type(Integer32):
    """Custom type dot11StationAssociationTrapEnabled based on Integer32"""
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


_Dot11StationAssociationTrapEnabled_Type.__name__ = "Integer32"
_Dot11StationAssociationTrapEnabled_Object = MibScalar
dot11StationAssociationTrapEnabled = _Dot11StationAssociationTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 5),
    _Dot11StationAssociationTrapEnabled_Type()
)
dot11StationAssociationTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11StationAssociationTrapEnabled.setStatus("current")


class _Dot11StationReAssociationTrapEnabled_Type(Integer32):
    """Custom type dot11StationReAssociationTrapEnabled based on Integer32"""
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


_Dot11StationReAssociationTrapEnabled_Type.__name__ = "Integer32"
_Dot11StationReAssociationTrapEnabled_Object = MibScalar
dot11StationReAssociationTrapEnabled = _Dot11StationReAssociationTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 6),
    _Dot11StationReAssociationTrapEnabled_Type()
)
dot11StationReAssociationTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11StationReAssociationTrapEnabled.setStatus("current")


class _Dot11StationAuthenticationTrapEnabled_Type(Integer32):
    """Custom type dot11StationAuthenticationTrapEnabled based on Integer32"""
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


_Dot11StationAuthenticationTrapEnabled_Type.__name__ = "Integer32"
_Dot11StationAuthenticationTrapEnabled_Object = MibScalar
dot11StationAuthenticationTrapEnabled = _Dot11StationAuthenticationTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 7),
    _Dot11StationAuthenticationTrapEnabled_Type()
)
dot11StationAuthenticationTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11StationAuthenticationTrapEnabled.setStatus("current")


class _Dot11StationRequestFailTrapEnabled_Type(Integer32):
    """Custom type dot11StationRequestFailTrapEnabled based on Integer32"""
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


_Dot11StationRequestFailTrapEnabled_Type.__name__ = "Integer32"
_Dot11StationRequestFailTrapEnabled_Object = MibScalar
dot11StationRequestFailTrapEnabled = _Dot11StationRequestFailTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 8),
    _Dot11StationRequestFailTrapEnabled_Type()
)
dot11StationRequestFailTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11StationRequestFailTrapEnabled.setStatus("current")


class _Dot11InterfaceBFailTrapEnabled_Type(Integer32):
    """Custom type dot11InterfaceBFailTrapEnabled based on Integer32"""
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


_Dot11InterfaceBFailTrapEnabled_Type.__name__ = "Integer32"
_Dot11InterfaceBFailTrapEnabled_Object = MibScalar
dot11InterfaceBFailTrapEnabled = _Dot11InterfaceBFailTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 9),
    _Dot11InterfaceBFailTrapEnabled_Type()
)
dot11InterfaceBFailTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11InterfaceBFailTrapEnabled.setStatus("current")


class _Dot11InterfaceAGFailTrapEnabled_Type(Integer32):
    """Custom type dot11InterfaceAGFailTrapEnabled based on Integer32"""
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


_Dot11InterfaceAGFailTrapEnabled_Type.__name__ = "Integer32"
_Dot11InterfaceAGFailTrapEnabled_Object = MibScalar
dot11InterfaceAGFailTrapEnabled = _Dot11InterfaceAGFailTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 10),
    _Dot11InterfaceAGFailTrapEnabled_Type()
)
dot11InterfaceAGFailTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11InterfaceAGFailTrapEnabled.setStatus("current")


class _Dot1xMacAddrAuthSuccessTrapEnabled_Type(Integer32):
    """Custom type dot1xMacAddrAuthSuccessTrapEnabled based on Integer32"""
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


_Dot1xMacAddrAuthSuccessTrapEnabled_Type.__name__ = "Integer32"
_Dot1xMacAddrAuthSuccessTrapEnabled_Object = MibScalar
dot1xMacAddrAuthSuccessTrapEnabled = _Dot1xMacAddrAuthSuccessTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 11),
    _Dot1xMacAddrAuthSuccessTrapEnabled_Type()
)
dot1xMacAddrAuthSuccessTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xMacAddrAuthSuccessTrapEnabled.setStatus("current")


class _Dot1xMacAddrAuthFailTrapEnabled_Type(Integer32):
    """Custom type dot1xMacAddrAuthFailTrapEnabled based on Integer32"""
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


_Dot1xMacAddrAuthFailTrapEnabled_Type.__name__ = "Integer32"
_Dot1xMacAddrAuthFailTrapEnabled_Object = MibScalar
dot1xMacAddrAuthFailTrapEnabled = _Dot1xMacAddrAuthFailTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 12),
    _Dot1xMacAddrAuthFailTrapEnabled_Type()
)
dot1xMacAddrAuthFailTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xMacAddrAuthFailTrapEnabled.setStatus("current")


class _Dot1xAuthNotInitiatedTrapEnabled_Type(Integer32):
    """Custom type dot1xAuthNotInitiatedTrapEnabled based on Integer32"""
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


_Dot1xAuthNotInitiatedTrapEnabled_Type.__name__ = "Integer32"
_Dot1xAuthNotInitiatedTrapEnabled_Object = MibScalar
dot1xAuthNotInitiatedTrapEnabled = _Dot1xAuthNotInitiatedTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 13),
    _Dot1xAuthNotInitiatedTrapEnabled_Type()
)
dot1xAuthNotInitiatedTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthNotInitiatedTrapEnabled.setStatus("current")


class _Dot1xAuthSuccessTrapEnabled_Type(Integer32):
    """Custom type dot1xAuthSuccessTrapEnabled based on Integer32"""
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


_Dot1xAuthSuccessTrapEnabled_Type.__name__ = "Integer32"
_Dot1xAuthSuccessTrapEnabled_Object = MibScalar
dot1xAuthSuccessTrapEnabled = _Dot1xAuthSuccessTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 14),
    _Dot1xAuthSuccessTrapEnabled_Type()
)
dot1xAuthSuccessTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthSuccessTrapEnabled.setStatus("current")


class _Dot1xAuthFailTrapEnabled_Type(Integer32):
    """Custom type dot1xAuthFailTrapEnabled based on Integer32"""
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


_Dot1xAuthFailTrapEnabled_Type.__name__ = "Integer32"
_Dot1xAuthFailTrapEnabled_Object = MibScalar
dot1xAuthFailTrapEnabled = _Dot1xAuthFailTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 15),
    _Dot1xAuthFailTrapEnabled_Type()
)
dot1xAuthFailTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthFailTrapEnabled.setStatus("current")


class _LocalMacAddrAuthSuccessTrapEnabled_Type(Integer32):
    """Custom type localMacAddrAuthSuccessTrapEnabled based on Integer32"""
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


_LocalMacAddrAuthSuccessTrapEnabled_Type.__name__ = "Integer32"
_LocalMacAddrAuthSuccessTrapEnabled_Object = MibScalar
localMacAddrAuthSuccessTrapEnabled = _LocalMacAddrAuthSuccessTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 16),
    _LocalMacAddrAuthSuccessTrapEnabled_Type()
)
localMacAddrAuthSuccessTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localMacAddrAuthSuccessTrapEnabled.setStatus("current")


class _LocalMacAddrAuthFailTrapEnabled_Type(Integer32):
    """Custom type localMacAddrAuthFailTrapEnabled based on Integer32"""
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


_LocalMacAddrAuthFailTrapEnabled_Type.__name__ = "Integer32"
_LocalMacAddrAuthFailTrapEnabled_Object = MibScalar
localMacAddrAuthFailTrapEnabled = _LocalMacAddrAuthFailTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 17),
    _LocalMacAddrAuthFailTrapEnabled_Type()
)
localMacAddrAuthFailTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localMacAddrAuthFailTrapEnabled.setStatus("current")


class _PppLogonFailTrapEnabled_Type(Integer32):
    """Custom type pppLogonFailTrapEnabled based on Integer32"""
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


_PppLogonFailTrapEnabled_Type.__name__ = "Integer32"
_PppLogonFailTrapEnabled_Object = MibScalar
pppLogonFailTrapEnabled = _PppLogonFailTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 18),
    _PppLogonFailTrapEnabled_Type()
)
pppLogonFailTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLogonFailTrapEnabled.setStatus("current")


class _IappStationRoamedFromTrapEnabled_Type(Integer32):
    """Custom type iappStationRoamedFromTrapEnabled based on Integer32"""
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


_IappStationRoamedFromTrapEnabled_Type.__name__ = "Integer32"
_IappStationRoamedFromTrapEnabled_Object = MibScalar
iappStationRoamedFromTrapEnabled = _IappStationRoamedFromTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 19),
    _IappStationRoamedFromTrapEnabled_Type()
)
iappStationRoamedFromTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iappStationRoamedFromTrapEnabled.setStatus("current")


class _IappStationRoamedToTrapEnabled_Type(Integer32):
    """Custom type iappStationRoamedToTrapEnabled based on Integer32"""
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


_IappStationRoamedToTrapEnabled_Type.__name__ = "Integer32"
_IappStationRoamedToTrapEnabled_Object = MibScalar
iappStationRoamedToTrapEnabled = _IappStationRoamedToTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 20),
    _IappStationRoamedToTrapEnabled_Type()
)
iappStationRoamedToTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iappStationRoamedToTrapEnabled.setStatus("current")


class _IappContextDataSentTrapEnabled_Type(Integer32):
    """Custom type iappContextDataSentTrapEnabled based on Integer32"""
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


_IappContextDataSentTrapEnabled_Type.__name__ = "Integer32"
_IappContextDataSentTrapEnabled_Object = MibScalar
iappContextDataSentTrapEnabled = _IappContextDataSentTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 21),
    _IappContextDataSentTrapEnabled_Type()
)
iappContextDataSentTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iappContextDataSentTrapEnabled.setStatus("current")


class _SntpServerFailTrapEnabled_Type(Integer32):
    """Custom type sntpServerFailTrapEnabled based on Integer32"""
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


_SntpServerFailTrapEnabled_Type.__name__ = "Integer32"
_SntpServerFailTrapEnabled_Object = MibScalar
sntpServerFailTrapEnabled = _SntpServerFailTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 22),
    _SntpServerFailTrapEnabled_Type()
)
sntpServerFailTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerFailTrapEnabled.setStatus("current")


class _Dot1xSuppAuthenticatedTrapEnabled_Type(Integer32):
    """Custom type dot1xSuppAuthenticatedTrapEnabled based on Integer32"""
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


_Dot1xSuppAuthenticatedTrapEnabled_Type.__name__ = "Integer32"
_Dot1xSuppAuthenticatedTrapEnabled_Object = MibScalar
dot1xSuppAuthenticatedTrapEnabled = _Dot1xSuppAuthenticatedTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 23),
    _Dot1xSuppAuthenticatedTrapEnabled_Type()
)
dot1xSuppAuthenticatedTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xSuppAuthenticatedTrapEnabled.setStatus("current")


class _Dot11FailedTransmitsTrapEnabled_Type(Integer32):
    """Custom type dot11FailedTransmitsTrapEnabled based on Integer32"""
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


_Dot11FailedTransmitsTrapEnabled_Type.__name__ = "Integer32"
_Dot11FailedTransmitsTrapEnabled_Object = MibScalar
dot11FailedTransmitsTrapEnabled = _Dot11FailedTransmitsTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 24),
    _Dot11FailedTransmitsTrapEnabled_Type()
)
dot11FailedTransmitsTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FailedTransmitsTrapEnabled.setStatus("current")


class _Dot11AckFailuresTrapEnabled_Type(Integer32):
    """Custom type dot11AckFailuresTrapEnabled based on Integer32"""
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


_Dot11AckFailuresTrapEnabled_Type.__name__ = "Integer32"
_Dot11AckFailuresTrapEnabled_Object = MibScalar
dot11AckFailuresTrapEnabled = _Dot11AckFailuresTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 25),
    _Dot11AckFailuresTrapEnabled_Type()
)
dot11AckFailuresTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AckFailuresTrapEnabled.setStatus("current")


class _Dot11FcsErrorsTrapEnabled_Type(Integer32):
    """Custom type dot11FcsErrorsTrapEnabled based on Integer32"""
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


_Dot11FcsErrorsTrapEnabled_Type.__name__ = "Integer32"
_Dot11FcsErrorsTrapEnabled_Object = MibScalar
dot11FcsErrorsTrapEnabled = _Dot11FcsErrorsTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 26),
    _Dot11FcsErrorsTrapEnabled_Type()
)
dot11FcsErrorsTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FcsErrorsTrapEnabled.setStatus("current")


class _RogueAPDetectedTrapEnabled_Type(Integer32):
    """Custom type rogueAPDetectedTrapEnabled based on Integer32"""
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


_RogueAPDetectedTrapEnabled_Type.__name__ = "Integer32"
_RogueAPDetectedTrapEnabled_Object = MibScalar
rogueAPDetectedTrapEnabled = _RogueAPDetectedTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 27),
    _RogueAPDetectedTrapEnabled_Type()
)
rogueAPDetectedTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rogueAPDetectedTrapEnabled.setStatus("current")


class _PossibleRogueAPDetectedTrapEnabled_Type(Integer32):
    """Custom type possibleRogueAPDetectedTrapEnabled based on Integer32"""
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


_PossibleRogueAPDetectedTrapEnabled_Type.__name__ = "Integer32"
_PossibleRogueAPDetectedTrapEnabled_Object = MibScalar
possibleRogueAPDetectedTrapEnabled = _PossibleRogueAPDetectedTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 16, 4, 28),
    _PossibleRogueAPDetectedTrapEnabled_Type()
)
possibleRogueAPDetectedTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    possibleRogueAPDetectedTrapEnabled.setStatus("current")
_EnterpriseApSession_ObjectIdentity = ObjectIdentity
enterpriseApSession = _EnterpriseApSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17)
)
_EnterpriseApSessionTable_Object = MibTable
enterpriseApSessionTable = _EnterpriseApSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1)
)
if mibBuilder.loadTexts:
    enterpriseApSessionTable.setStatus("current")
_EnterpriseApSessionEntry_Object = MibTableRow
enterpriseApSessionEntry = _EnterpriseApSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1)
)
enterpriseApSessionEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApSessionIfIndex"),
    (0, "AP80-PRIVATE-MIB", "enterpriseApSessionStationAddres"),
)
if mibBuilder.loadTexts:
    enterpriseApSessionEntry.setStatus("current")
_EnterpriseApSessionIfIndex_Type = Integer32
_EnterpriseApSessionIfIndex_Object = MibTableColumn
enterpriseApSessionIfIndex = _EnterpriseApSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 1),
    _EnterpriseApSessionIfIndex_Type()
)
enterpriseApSessionIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApSessionIfIndex.setStatus("current")
_EnterpriseApSessionStationAddres_Type = MacAddress
_EnterpriseApSessionStationAddres_Object = MibTableColumn
enterpriseApSessionStationAddres = _EnterpriseApSessionStationAddres_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 2),
    _EnterpriseApSessionStationAddres_Type()
)
enterpriseApSessionStationAddres.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApSessionStationAddres.setStatus("current")
_EnterpriseApSessionAuthenticated_Type = TruthValue
_EnterpriseApSessionAuthenticated_Object = MibTableColumn
enterpriseApSessionAuthenticated = _EnterpriseApSessionAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 3),
    _EnterpriseApSessionAuthenticated_Type()
)
enterpriseApSessionAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionAuthenticated.setStatus("current")
_EnterpriseApSessionAssociated_Type = TruthValue
_EnterpriseApSessionAssociated_Object = MibTableColumn
enterpriseApSessionAssociated = _EnterpriseApSessionAssociated_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 4),
    _EnterpriseApSessionAssociated_Type()
)
enterpriseApSessionAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionAssociated.setStatus("current")
_EnterpriseApSessionIsForwarding_Type = TruthValue
_EnterpriseApSessionIsForwarding_Object = MibTableColumn
enterpriseApSessionIsForwarding = _EnterpriseApSessionIsForwarding_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 5),
    _EnterpriseApSessionIsForwarding_Type()
)
enterpriseApSessionIsForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionIsForwarding.setStatus("current")


class _EnterpriseApSessionKeyType_Type(Integer32):
    """Custom type enterpriseApSessionKeyType based on Integer32"""
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
        *(("dynamicWep", 3),
          ("none", 1),
          ("staticWep", 2),
          ("wpaAes", 6),
          ("wpaTkip", 5),
          ("wpaWep", 4))
    )


_EnterpriseApSessionKeyType_Type.__name__ = "Integer32"
_EnterpriseApSessionKeyType_Object = MibTableColumn
enterpriseApSessionKeyType = _EnterpriseApSessionKeyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 6),
    _EnterpriseApSessionKeyType_Type()
)
enterpriseApSessionKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionKeyType.setStatus("current")
_EnterpriseApSessionAssociationId_Type = Integer32
_EnterpriseApSessionAssociationId_Object = MibTableColumn
enterpriseApSessionAssociationId = _EnterpriseApSessionAssociationId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 7),
    _EnterpriseApSessionAssociationId_Type()
)
enterpriseApSessionAssociationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionAssociationId.setStatus("current")
_EnterpriseApSessionLastAuthenticatedTime_Type = TimeTicks
_EnterpriseApSessionLastAuthenticatedTime_Object = MibTableColumn
enterpriseApSessionLastAuthenticatedTime = _EnterpriseApSessionLastAuthenticatedTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 8),
    _EnterpriseApSessionLastAuthenticatedTime_Type()
)
enterpriseApSessionLastAuthenticatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionLastAuthenticatedTime.setStatus("current")
_EnterpriseApSessionAssociatedTime_Type = TimeTicks
_EnterpriseApSessionAssociatedTime_Object = MibTableColumn
enterpriseApSessionAssociatedTime = _EnterpriseApSessionAssociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 9),
    _EnterpriseApSessionAssociatedTime_Type()
)
enterpriseApSessionAssociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionAssociatedTime.setStatus("current")
_EnterpriseApSessionLastAssociatedTime_Type = TimeTicks
_EnterpriseApSessionLastAssociatedTime_Object = MibTableColumn
enterpriseApSessionLastAssociatedTime = _EnterpriseApSessionLastAssociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 10),
    _EnterpriseApSessionLastAssociatedTime_Type()
)
enterpriseApSessionLastAssociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionLastAssociatedTime.setStatus("current")
_EnterpriseApSessionLastDisassociatedTime_Type = TimeTicks
_EnterpriseApSessionLastDisassociatedTime_Object = MibTableColumn
enterpriseApSessionLastDisassociatedTime = _EnterpriseApSessionLastDisassociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 11),
    _EnterpriseApSessionLastDisassociatedTime_Type()
)
enterpriseApSessionLastDisassociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionLastDisassociatedTime.setStatus("current")
_EnterpriseApSessionTxPacketCount_Type = Counter32
_EnterpriseApSessionTxPacketCount_Object = MibTableColumn
enterpriseApSessionTxPacketCount = _EnterpriseApSessionTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 12),
    _EnterpriseApSessionTxPacketCount_Type()
)
enterpriseApSessionTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionTxPacketCount.setStatus("current")
_EnterpriseApSessionRxPacketCount_Type = Counter32
_EnterpriseApSessionRxPacketCount_Object = MibTableColumn
enterpriseApSessionRxPacketCount = _EnterpriseApSessionRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 13),
    _EnterpriseApSessionRxPacketCount_Type()
)
enterpriseApSessionRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionRxPacketCount.setStatus("current")
_EnterpriseApSessionTxByteCount_Type = Counter32
_EnterpriseApSessionTxByteCount_Object = MibTableColumn
enterpriseApSessionTxByteCount = _EnterpriseApSessionTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 14),
    _EnterpriseApSessionTxByteCount_Type()
)
enterpriseApSessionTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionTxByteCount.setStatus("current")
_EnterpriseApSessionRxByteCount_Type = Counter32
_EnterpriseApSessionRxByteCount_Object = MibTableColumn
enterpriseApSessionRxByteCount = _EnterpriseApSessionRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 17, 1, 1, 15),
    _EnterpriseApSessionRxByteCount_Type()
)
enterpriseApSessionRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApSessionRxByteCount.setStatus("current")
_EnterpriseAPVapRadio_ObjectIdentity = ObjectIdentity
enterpriseAPVapRadio = _EnterpriseAPVapRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20)
)
_EnterpriseAPVapRadioTable_Object = MibTable
enterpriseAPVapRadioTable = _EnterpriseAPVapRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20, 1)
)
if mibBuilder.loadTexts:
    enterpriseAPVapRadioTable.setStatus("current")
_EnterpriseAPVapRadioEntry_Object = MibTableRow
enterpriseAPVapRadioEntry = _EnterpriseAPVapRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20, 1, 1)
)
enterpriseAPVapRadioEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseAPVapRadioIndex"),
)
if mibBuilder.loadTexts:
    enterpriseAPVapRadioEntry.setStatus("current")
_EnterpriseAPVapRadioIndex_Type = Integer32
_EnterpriseAPVapRadioIndex_Object = MibTableColumn
enterpriseAPVapRadioIndex = _EnterpriseAPVapRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20, 1, 1, 1),
    _EnterpriseAPVapRadioIndex_Type()
)
enterpriseAPVapRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseAPVapRadioIndex.setStatus("current")


class _EnterpriseAPVapRadioState_Type(Integer32):
    """Custom type enterpriseAPVapRadioState based on Integer32"""
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


_EnterpriseAPVapRadioState_Type.__name__ = "Integer32"
_EnterpriseAPVapRadioState_Object = MibTableColumn
enterpriseAPVapRadioState = _EnterpriseAPVapRadioState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20, 1, 1, 2),
    _EnterpriseAPVapRadioState_Type()
)
enterpriseAPVapRadioState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseAPVapRadioState.setStatus("current")


class _EnterpriseAPVapRadioClosedSystem_Type(Integer32):
    """Custom type enterpriseAPVapRadioClosedSystem based on Integer32"""
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


_EnterpriseAPVapRadioClosedSystem_Type.__name__ = "Integer32"
_EnterpriseAPVapRadioClosedSystem_Object = MibTableColumn
enterpriseAPVapRadioClosedSystem = _EnterpriseAPVapRadioClosedSystem_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20, 1, 1, 3),
    _EnterpriseAPVapRadioClosedSystem_Type()
)
enterpriseAPVapRadioClosedSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseAPVapRadioClosedSystem.setStatus("current")


class _EnterpriseAPVapRadioMaxAssoc_Type(Integer32):
    """Custom type enterpriseAPVapRadioMaxAssoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EnterpriseAPVapRadioMaxAssoc_Type.__name__ = "Integer32"
_EnterpriseAPVapRadioMaxAssoc_Object = MibTableColumn
enterpriseAPVapRadioMaxAssoc = _EnterpriseAPVapRadioMaxAssoc_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20, 1, 1, 4),
    _EnterpriseAPVapRadioMaxAssoc_Type()
)
enterpriseAPVapRadioMaxAssoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseAPVapRadioMaxAssoc.setStatus("current")


class _EnterpriseAPVapRadioTransmitKey_Type(Integer32):
    """Custom type enterpriseAPVapRadioTransmitKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnterpriseAPVapRadioTransmitKey_Type.__name__ = "Integer32"
_EnterpriseAPVapRadioTransmitKey_Object = MibTableColumn
enterpriseAPVapRadioTransmitKey = _EnterpriseAPVapRadioTransmitKey_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20, 1, 1, 5),
    _EnterpriseAPVapRadioTransmitKey_Type()
)
enterpriseAPVapRadioTransmitKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseAPVapRadioTransmitKey.setStatus("current")


class _EnterpriseAPVapRadioDescription_Type(DisplayString):
    """Custom type enterpriseAPVapRadioDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EnterpriseAPVapRadioDescription_Type.__name__ = "DisplayString"
_EnterpriseAPVapRadioDescription_Object = MibTableColumn
enterpriseAPVapRadioDescription = _EnterpriseAPVapRadioDescription_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20, 1, 1, 6),
    _EnterpriseAPVapRadioDescription_Type()
)
enterpriseAPVapRadioDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseAPVapRadioDescription.setStatus("current")


class _EnterpriseAPVapRadioAuthTimeoutInterval_Type(Integer32):
    """Custom type enterpriseAPVapRadioAuthTimeoutInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_EnterpriseAPVapRadioAuthTimeoutInterval_Type.__name__ = "Integer32"
_EnterpriseAPVapRadioAuthTimeoutInterval_Object = MibTableColumn
enterpriseAPVapRadioAuthTimeoutInterval = _EnterpriseAPVapRadioAuthTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20, 1, 1, 8),
    _EnterpriseAPVapRadioAuthTimeoutInterval_Type()
)
enterpriseAPVapRadioAuthTimeoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseAPVapRadioAuthTimeoutInterval.setStatus("current")


class _EnterpriseAPVapRadioAssocTimeoutInterval_Type(Integer32):
    """Custom type enterpriseAPVapRadioAssocTimeoutInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_EnterpriseAPVapRadioAssocTimeoutInterval_Type.__name__ = "Integer32"
_EnterpriseAPVapRadioAssocTimeoutInterval_Object = MibTableColumn
enterpriseAPVapRadioAssocTimeoutInterval = _EnterpriseAPVapRadioAssocTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20, 1, 1, 9),
    _EnterpriseAPVapRadioAssocTimeoutInterval_Type()
)
enterpriseAPVapRadioAssocTimeoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseAPVapRadioAssocTimeoutInterval.setStatus("current")


class _EnterpriseAPVapRadioWPA2PMKSALifeTime_Type(Integer32):
    """Custom type enterpriseAPVapRadioWPA2PMKSALifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_EnterpriseAPVapRadioWPA2PMKSALifeTime_Type.__name__ = "Integer32"
_EnterpriseAPVapRadioWPA2PMKSALifeTime_Object = MibTableColumn
enterpriseAPVapRadioWPA2PMKSALifeTime = _EnterpriseAPVapRadioWPA2PMKSALifeTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 20, 1, 1, 10),
    _EnterpriseAPVapRadioWPA2PMKSALifeTime_Type()
)
enterpriseAPVapRadioWPA2PMKSALifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseAPVapRadioWPA2PMKSALifeTime.setStatus("current")
_EnterpriseApRadioWds_ObjectIdentity = ObjectIdentity
enterpriseApRadioWds = _EnterpriseApRadioWds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 22)
)
_EnterpriseApRadioWdsTable_Object = MibTable
enterpriseApRadioWdsTable = _EnterpriseApRadioWdsTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 22, 1)
)
if mibBuilder.loadTexts:
    enterpriseApRadioWdsTable.setStatus("current")
_EnterpriseApRadioWdsEntry_Object = MibTableRow
enterpriseApRadioWdsEntry = _EnterpriseApRadioWdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 22, 1, 1)
)
enterpriseApRadioWdsEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApRadioIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApRadioWdsEntry.setStatus("current")


class _WdsApRole_Type(Integer32):
    """Custom type wdsApRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("roleAp", 1),
          ("roleBridge", 4),
          ("roleBridgeMaster", 2))
    )


_WdsApRole_Type.__name__ = "Integer32"
_WdsApRole_Object = MibTableColumn
wdsApRole = _WdsApRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 22, 1, 1, 1),
    _WdsApRole_Type()
)
wdsApRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsApRole.setStatus("current")


class _WdsChannelAutoSync_Type(Integer32):
    """Custom type wdsChannelAutoSync based on Integer32"""
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


_WdsChannelAutoSync_Type.__name__ = "Integer32"
_WdsChannelAutoSync_Object = MibTableColumn
wdsChannelAutoSync = _WdsChannelAutoSync_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 22, 1, 1, 3),
    _WdsChannelAutoSync_Type()
)
wdsChannelAutoSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsChannelAutoSync.setStatus("current")


class _WdsMasterSlaveMode_Type(Integer32):
    """Custom type wdsMasterSlaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_WdsMasterSlaveMode_Type.__name__ = "Integer32"
_WdsMasterSlaveMode_Object = MibTableColumn
wdsMasterSlaveMode = _WdsMasterSlaveMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 22, 1, 1, 4),
    _WdsMasterSlaveMode_Type()
)
wdsMasterSlaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsMasterSlaveMode.setStatus("current")
_EnterpriseApRadioWdsPeerTable_Object = MibTable
enterpriseApRadioWdsPeerTable = _EnterpriseApRadioWdsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 22, 2)
)
if mibBuilder.loadTexts:
    enterpriseApRadioWdsPeerTable.setStatus("current")
_EnterpriseApRadioWdsPeerEntry_Object = MibTableRow
enterpriseApRadioWdsPeerEntry = _EnterpriseApRadioWdsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 22, 2, 1)
)
enterpriseApRadioWdsPeerEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApRadioIndex"),
    (0, "AP80-PRIVATE-MIB", "wdsPeerIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApRadioWdsPeerEntry.setStatus("current")
_WdsPeerIndex_Type = Integer32
_WdsPeerIndex_Object = MibTableColumn
wdsPeerIndex = _WdsPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 22, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 22, 2, 1, 2),
    _WdsPeerBssid_Type()
)
wdsPeerBssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsPeerBssid.setStatus("current")
_EnterpriseApWMM_ObjectIdentity = ObjectIdentity
enterpriseApWMM = _EnterpriseApWMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24)
)
_EnterpriseApWMMTable_Object = MibTable
enterpriseApWMMTable = _EnterpriseApWMMTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 1)
)
if mibBuilder.loadTexts:
    enterpriseApWMMTable.setStatus("current")
_EnterpriseApWMMEntry_Object = MibTableRow
enterpriseApWMMEntry = _EnterpriseApWMMEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 1, 1)
)
enterpriseApWMMEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApWMMModeIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApWMMEntry.setStatus("current")
_EnterpriseApWMMModeIndex_Type = Integer32
_EnterpriseApWMMModeIndex_Object = MibTableColumn
enterpriseApWMMModeIndex = _EnterpriseApWMMModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 1, 1, 1),
    _EnterpriseApWMMModeIndex_Type()
)
enterpriseApWMMModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApWMMModeIndex.setStatus("current")


class _EnterpriseApWMMMode_Type(Integer32):
    """Custom type enterpriseApWMMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("required", 3),
          ("support", 2))
    )


_EnterpriseApWMMMode_Type.__name__ = "Integer32"
_EnterpriseApWMMMode_Object = MibTableColumn
enterpriseApWMMMode = _EnterpriseApWMMMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 1, 1, 2),
    _EnterpriseApWMMMode_Type()
)
enterpriseApWMMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMMode.setStatus("current")
_EnterpriseApWMMAckPolicyTable_Object = MibTable
enterpriseApWMMAckPolicyTable = _EnterpriseApWMMAckPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 2)
)
if mibBuilder.loadTexts:
    enterpriseApWMMAckPolicyTable.setStatus("current")
_EnterpriseApWMMAckPolicyEntry_Object = MibTableRow
enterpriseApWMMAckPolicyEntry = _EnterpriseApWMMAckPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 2, 1)
)
enterpriseApWMMAckPolicyEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApWMMAckPolicyIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApWMMAckPolicyEntry.setStatus("current")
_EnterpriseApWMMAckPolicyIndex_Type = Integer32
_EnterpriseApWMMAckPolicyIndex_Object = MibTableColumn
enterpriseApWMMAckPolicyIndex = _EnterpriseApWMMAckPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 2, 1, 1),
    _EnterpriseApWMMAckPolicyIndex_Type()
)
enterpriseApWMMAckPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApWMMAckPolicyIndex.setStatus("current")


class _EnterpriseApWMMACKPolicy_Type(Integer32):
    """Custom type enterpriseApWMMACKPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("NoAcknowledge", 2),
          ("acknowledge", 1))
    )


_EnterpriseApWMMACKPolicy_Type.__name__ = "Integer32"
_EnterpriseApWMMACKPolicy_Object = MibTableColumn
enterpriseApWMMACKPolicy = _EnterpriseApWMMACKPolicy_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 2, 1, 2),
    _EnterpriseApWMMACKPolicy_Type()
)
enterpriseApWMMACKPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMACKPolicy.setStatus("current")
_EnterpriseApWMMBSSParamTable_Object = MibTable
enterpriseApWMMBSSParamTable = _EnterpriseApWMMBSSParamTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 3)
)
if mibBuilder.loadTexts:
    enterpriseApWMMBSSParamTable.setStatus("current")
_EnterpriseApWMMBSSParamEntry_Object = MibTableRow
enterpriseApWMMBSSParamEntry = _EnterpriseApWMMBSSParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 3, 1)
)
enterpriseApWMMBSSParamEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApWMMBSSParamIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApWMMBSSParamEntry.setStatus("current")
_EnterpriseApWMMBSSParamIndex_Type = Integer32
_EnterpriseApWMMBSSParamIndex_Object = MibTableColumn
enterpriseApWMMBSSParamIndex = _EnterpriseApWMMBSSParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 3, 1, 1),
    _EnterpriseApWMMBSSParamIndex_Type()
)
enterpriseApWMMBSSParamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApWMMBSSParamIndex.setStatus("current")


class _EnterpriseApWMMBSSParamLogCwMin_Type(Integer32):
    """Custom type enterpriseApWMMBSSParamLogCwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_EnterpriseApWMMBSSParamLogCwMin_Type.__name__ = "Integer32"
_EnterpriseApWMMBSSParamLogCwMin_Object = MibTableColumn
enterpriseApWMMBSSParamLogCwMin = _EnterpriseApWMMBSSParamLogCwMin_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 3, 1, 2),
    _EnterpriseApWMMBSSParamLogCwMin_Type()
)
enterpriseApWMMBSSParamLogCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMBSSParamLogCwMin.setStatus("current")


class _EnterpriseApWMMBSSParamLogCwMax_Type(Integer32):
    """Custom type enterpriseApWMMBSSParamLogCwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_EnterpriseApWMMBSSParamLogCwMax_Type.__name__ = "Integer32"
_EnterpriseApWMMBSSParamLogCwMax_Object = MibTableColumn
enterpriseApWMMBSSParamLogCwMax = _EnterpriseApWMMBSSParamLogCwMax_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 3, 1, 3),
    _EnterpriseApWMMBSSParamLogCwMax_Type()
)
enterpriseApWMMBSSParamLogCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMBSSParamLogCwMax.setStatus("current")


class _EnterpriseApWMMBSSParamAIFSN_Type(Integer32):
    """Custom type enterpriseApWMMBSSParamAIFSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_EnterpriseApWMMBSSParamAIFSN_Type.__name__ = "Integer32"
_EnterpriseApWMMBSSParamAIFSN_Object = MibTableColumn
enterpriseApWMMBSSParamAIFSN = _EnterpriseApWMMBSSParamAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 3, 1, 4),
    _EnterpriseApWMMBSSParamAIFSN_Type()
)
enterpriseApWMMBSSParamAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMBSSParamAIFSN.setStatus("current")


class _EnterpriseApWMMBSSParamTXOPLimit_Type(Integer32):
    """Custom type enterpriseApWMMBSSParamTXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EnterpriseApWMMBSSParamTXOPLimit_Type.__name__ = "Integer32"
_EnterpriseApWMMBSSParamTXOPLimit_Object = MibTableColumn
enterpriseApWMMBSSParamTXOPLimit = _EnterpriseApWMMBSSParamTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 3, 1, 5),
    _EnterpriseApWMMBSSParamTXOPLimit_Type()
)
enterpriseApWMMBSSParamTXOPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMBSSParamTXOPLimit.setStatus("current")


class _EnterpriseApWMMBSSParamAdmissionCtrl_Type(Integer32):
    """Custom type enterpriseApWMMBSSParamAdmissionCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("ebabled", 1))
    )


_EnterpriseApWMMBSSParamAdmissionCtrl_Type.__name__ = "Integer32"
_EnterpriseApWMMBSSParamAdmissionCtrl_Object = MibTableColumn
enterpriseApWMMBSSParamAdmissionCtrl = _EnterpriseApWMMBSSParamAdmissionCtrl_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 3, 1, 6),
    _EnterpriseApWMMBSSParamAdmissionCtrl_Type()
)
enterpriseApWMMBSSParamAdmissionCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMBSSParamAdmissionCtrl.setStatus("current")
_EnterpriseApWMMAPParamTable_Object = MibTable
enterpriseApWMMAPParamTable = _EnterpriseApWMMAPParamTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 4)
)
if mibBuilder.loadTexts:
    enterpriseApWMMAPParamTable.setStatus("current")
_EnterpriseApWMMAPParamEntry_Object = MibTableRow
enterpriseApWMMAPParamEntry = _EnterpriseApWMMAPParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 4, 1)
)
enterpriseApWMMAPParamEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApWMMAPParamIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApWMMAPParamEntry.setStatus("current")
_EnterpriseApWMMAPParamIndex_Type = Integer32
_EnterpriseApWMMAPParamIndex_Object = MibTableColumn
enterpriseApWMMAPParamIndex = _EnterpriseApWMMAPParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 4, 1, 1),
    _EnterpriseApWMMAPParamIndex_Type()
)
enterpriseApWMMAPParamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterpriseApWMMAPParamIndex.setStatus("current")


class _EnterpriseApWMMAPParamLogCwMin_Type(Integer32):
    """Custom type enterpriseApWMMAPParamLogCwMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_EnterpriseApWMMAPParamLogCwMin_Type.__name__ = "Integer32"
_EnterpriseApWMMAPParamLogCwMin_Object = MibTableColumn
enterpriseApWMMAPParamLogCwMin = _EnterpriseApWMMAPParamLogCwMin_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 4, 1, 2),
    _EnterpriseApWMMAPParamLogCwMin_Type()
)
enterpriseApWMMAPParamLogCwMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMAPParamLogCwMin.setStatus("current")


class _EnterpriseApWMMAPParamLogCwMax_Type(Integer32):
    """Custom type enterpriseApWMMAPParamLogCwMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_EnterpriseApWMMAPParamLogCwMax_Type.__name__ = "Integer32"
_EnterpriseApWMMAPParamLogCwMax_Object = MibTableColumn
enterpriseApWMMAPParamLogCwMax = _EnterpriseApWMMAPParamLogCwMax_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 4, 1, 3),
    _EnterpriseApWMMAPParamLogCwMax_Type()
)
enterpriseApWMMAPParamLogCwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMAPParamLogCwMax.setStatus("current")


class _EnterpriseApWMMAPParamAIFSN_Type(Integer32):
    """Custom type enterpriseApWMMAPParamAIFSN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_EnterpriseApWMMAPParamAIFSN_Type.__name__ = "Integer32"
_EnterpriseApWMMAPParamAIFSN_Object = MibTableColumn
enterpriseApWMMAPParamAIFSN = _EnterpriseApWMMAPParamAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 4, 1, 4),
    _EnterpriseApWMMAPParamAIFSN_Type()
)
enterpriseApWMMAPParamAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMAPParamAIFSN.setStatus("current")


class _EnterpriseApWMMAPParamTXOPLimit_Type(Integer32):
    """Custom type enterpriseApWMMAPParamTXOPLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EnterpriseApWMMAPParamTXOPLimit_Type.__name__ = "Integer32"
_EnterpriseApWMMAPParamTXOPLimit_Object = MibTableColumn
enterpriseApWMMAPParamTXOPLimit = _EnterpriseApWMMAPParamTXOPLimit_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 4, 1, 5),
    _EnterpriseApWMMAPParamTXOPLimit_Type()
)
enterpriseApWMMAPParamTXOPLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMAPParamTXOPLimit.setStatus("current")


class _EnterpriseApWMMAPParamAdmissionCtrl_Type(Integer32):
    """Custom type enterpriseApWMMAPParamAdmissionCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("ebabled", 1))
    )


_EnterpriseApWMMAPParamAdmissionCtrl_Type.__name__ = "Integer32"
_EnterpriseApWMMAPParamAdmissionCtrl_Object = MibTableColumn
enterpriseApWMMAPParamAdmissionCtrl = _EnterpriseApWMMAPParamAdmissionCtrl_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 24, 4, 1, 6),
    _EnterpriseApWMMAPParamAdmissionCtrl_Type()
)
enterpriseApWMMAPParamAdmissionCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApWMMAPParamAdmissionCtrl.setStatus("current")
_EnterpriseApSTP_ObjectIdentity = ObjectIdentity
enterpriseApSTP = _EnterpriseApSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25)
)


class _EnterpriseApSTPBridgeStatus_Type(Integer32):
    """Custom type enterpriseApSTPBridgeStatus based on Integer32"""
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


_EnterpriseApSTPBridgeStatus_Type.__name__ = "Integer32"
_EnterpriseApSTPBridgeStatus_Object = MibScalar
enterpriseApSTPBridgeStatus = _EnterpriseApSTPBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 1),
    _EnterpriseApSTPBridgeStatus_Type()
)
enterpriseApSTPBridgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSTPBridgeStatus.setStatus("current")


class _EnterpriseApSTPBridgePriority_Type(Integer32):
    """Custom type enterpriseApSTPBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EnterpriseApSTPBridgePriority_Type.__name__ = "Integer32"
_EnterpriseApSTPBridgePriority_Object = MibScalar
enterpriseApSTPBridgePriority = _EnterpriseApSTPBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 2),
    _EnterpriseApSTPBridgePriority_Type()
)
enterpriseApSTPBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSTPBridgePriority.setStatus("current")


class _EnterpriseApSTPBridgeMaxAge_Type(Integer32):
    """Custom type enterpriseApSTPBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_EnterpriseApSTPBridgeMaxAge_Type.__name__ = "Integer32"
_EnterpriseApSTPBridgeMaxAge_Object = MibScalar
enterpriseApSTPBridgeMaxAge = _EnterpriseApSTPBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 3),
    _EnterpriseApSTPBridgeMaxAge_Type()
)
enterpriseApSTPBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSTPBridgeMaxAge.setStatus("current")


class _EnterpriseApSTPHelloTime_Type(Integer32):
    """Custom type enterpriseApSTPHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EnterpriseApSTPHelloTime_Type.__name__ = "Integer32"
_EnterpriseApSTPHelloTime_Object = MibScalar
enterpriseApSTPHelloTime = _EnterpriseApSTPHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 4),
    _EnterpriseApSTPHelloTime_Type()
)
enterpriseApSTPHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSTPHelloTime.setStatus("current")


class _EnterpriseApSTPBridgeForwardingDelay_Type(Integer32):
    """Custom type enterpriseApSTPBridgeForwardingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_EnterpriseApSTPBridgeForwardingDelay_Type.__name__ = "Integer32"
_EnterpriseApSTPBridgeForwardingDelay_Object = MibScalar
enterpriseApSTPBridgeForwardingDelay = _EnterpriseApSTPBridgeForwardingDelay_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 5),
    _EnterpriseApSTPBridgeForwardingDelay_Type()
)
enterpriseApSTPBridgeForwardingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSTPBridgeForwardingDelay.setStatus("current")
_EnterpriseApSTPRadioInterface_ObjectIdentity = ObjectIdentity
enterpriseApSTPRadioInterface = _EnterpriseApSTPRadioInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 6)
)
_EnterpriseApSTPNodeTable_Object = MibTable
enterpriseApSTPNodeTable = _EnterpriseApSTPNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 6, 1)
)
if mibBuilder.loadTexts:
    enterpriseApSTPNodeTable.setStatus("current")
_EnterpriseApSTPNodeEntry_Object = MibTableRow
enterpriseApSTPNodeEntry = _EnterpriseApSTPNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 6, 1, 1)
)
enterpriseApSTPNodeEntry.setIndexNames(
    (0, "AP80-PRIVATE-MIB", "enterpriseApSTPNodeIndex"),
)
if mibBuilder.loadTexts:
    enterpriseApSTPNodeEntry.setStatus("current")
_EnterpriseApSTPNodeIndex_Type = Integer32
_EnterpriseApSTPNodeIndex_Object = MibTableColumn
enterpriseApSTPNodeIndex = _EnterpriseApSTPNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 6, 1, 1, 1),
    _EnterpriseApSTPNodeIndex_Type()
)
enterpriseApSTPNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enterpriseApSTPNodeIndex.setStatus("current")


class _EnterpriseApSTPNodeLinkPathCost_Type(Integer32):
    """Custom type enterpriseApSTPNodeLinkPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EnterpriseApSTPNodeLinkPathCost_Type.__name__ = "Integer32"
_EnterpriseApSTPNodeLinkPathCost_Object = MibTableColumn
enterpriseApSTPNodeLinkPathCost = _EnterpriseApSTPNodeLinkPathCost_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 6, 1, 1, 2),
    _EnterpriseApSTPNodeLinkPathCost_Type()
)
enterpriseApSTPNodeLinkPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSTPNodeLinkPathCost.setStatus("current")


class _EnterpriseApSTPNodeLinkPortPriority_Type(Integer32):
    """Custom type enterpriseApSTPNodeLinkPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnterpriseApSTPNodeLinkPortPriority_Type.__name__ = "Integer32"
_EnterpriseApSTPNodeLinkPortPriority_Object = MibTableColumn
enterpriseApSTPNodeLinkPortPriority = _EnterpriseApSTPNodeLinkPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 6, 1, 1, 3),
    _EnterpriseApSTPNodeLinkPortPriority_Type()
)
enterpriseApSTPNodeLinkPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSTPNodeLinkPortPriority.setStatus("current")
_EnterpriseApSTPEthernetInterface_ObjectIdentity = ObjectIdentity
enterpriseApSTPEthernetInterface = _EnterpriseApSTPEthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 7)
)


class _EnterpriseApSTPEthernetLinkPathCost_Type(Integer32):
    """Custom type enterpriseApSTPEthernetLinkPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EnterpriseApSTPEthernetLinkPathCost_Type.__name__ = "Integer32"
_EnterpriseApSTPEthernetLinkPathCost_Object = MibScalar
enterpriseApSTPEthernetLinkPathCost = _EnterpriseApSTPEthernetLinkPathCost_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 7, 1),
    _EnterpriseApSTPEthernetLinkPathCost_Type()
)
enterpriseApSTPEthernetLinkPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSTPEthernetLinkPathCost.setStatus("current")


class _EnterpriseApSTPEthernetLinkPortPriority_Type(Integer32):
    """Custom type enterpriseApSTPEthernetLinkPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnterpriseApSTPEthernetLinkPortPriority_Type.__name__ = "Integer32"
_EnterpriseApSTPEthernetLinkPortPriority_Object = MibScalar
enterpriseApSTPEthernetLinkPortPriority = _EnterpriseApSTPEthernetLinkPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 25, 7, 2),
    _EnterpriseApSTPEthernetLinkPortPriority_Type()
)
enterpriseApSTPEthernetLinkPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterpriseApSTPEthernetLinkPortPriority.setStatus("current")

# Managed Objects groups


# Notification objects

sysSystemUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    sysSystemUp.setStatus(
        "current"
    )

sysSystemDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    sysSystemDown.setStatus(
        "current"
    )

sysRadiusServerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    sysRadiusServerChanged.setStatus(
        "current"
    )

sysConfigFileVersionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    sysConfigFileVersionChanged.setStatus(
        "current"
    )

dot11StationAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 1)
)
dot11StationAssociation.setObjects(
    ("AP80-PRIVATE-MIB", "dot11Station")
)
if mibBuilder.loadTexts:
    dot11StationAssociation.setStatus(
        "current"
    )

dot11StationReAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 2)
)
dot11StationReAssociation.setObjects(
    ("AP80-PRIVATE-MIB", "dot11Station")
)
if mibBuilder.loadTexts:
    dot11StationReAssociation.setStatus(
        "current"
    )

dot11StationAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 3)
)
dot11StationAuthentication.setObjects(
    ("AP80-PRIVATE-MIB", "dot11Station")
)
if mibBuilder.loadTexts:
    dot11StationAuthentication.setStatus(
        "current"
    )

dot11StationRequestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 4)
)
dot11StationRequestFail.setObjects(
      *(("AP80-PRIVATE-MIB", "dot11Station"),
        ("AP80-PRIVATE-MIB", "dot11RequestType"),
        ("AP80-PRIVATE-MIB", "dot11ReasonCode"))
)
if mibBuilder.loadTexts:
    dot11StationRequestFail.setStatus(
        "current"
    )

dot11InterfaceBFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 5)
)
if mibBuilder.loadTexts:
    dot11InterfaceBFail.setStatus(
        "current"
    )

dot11InterfaceAGFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 6)
)
if mibBuilder.loadTexts:
    dot11InterfaceAGFail.setStatus(
        "current"
    )

dot1xMacAddrAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 7)
)
dot1xMacAddrAuthSuccess.setObjects(
    ("AP80-PRIVATE-MIB", "dot11Station")
)
if mibBuilder.loadTexts:
    dot1xMacAddrAuthSuccess.setStatus(
        "current"
    )

dot1xMacAddrAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 8)
)
dot1xMacAddrAuthFail.setObjects(
    ("AP80-PRIVATE-MIB", "dot11Station")
)
if mibBuilder.loadTexts:
    dot1xMacAddrAuthFail.setStatus(
        "current"
    )

dot1xAuthNotInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 9)
)
dot1xAuthNotInitiated.setObjects(
    ("AP80-PRIVATE-MIB", "dot11Station")
)
if mibBuilder.loadTexts:
    dot1xAuthNotInitiated.setStatus(
        "current"
    )

dot1xAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 10)
)
dot1xAuthSuccess.setObjects(
    ("AP80-PRIVATE-MIB", "dot11Station")
)
if mibBuilder.loadTexts:
    dot1xAuthSuccess.setStatus(
        "current"
    )

dot1xAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 11)
)
dot1xAuthFail.setObjects(
    ("AP80-PRIVATE-MIB", "dot11Station")
)
if mibBuilder.loadTexts:
    dot1xAuthFail.setStatus(
        "current"
    )

localMacAddrAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 12)
)
localMacAddrAuthSuccess.setObjects(
    ("AP80-PRIVATE-MIB", "dot11Station")
)
if mibBuilder.loadTexts:
    localMacAddrAuthSuccess.setStatus(
        "current"
    )

localMacAddrAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 13)
)
localMacAddrAuthFail.setObjects(
    ("AP80-PRIVATE-MIB", "dot11Station")
)
if mibBuilder.loadTexts:
    localMacAddrAuthFail.setStatus(
        "current"
    )

pppLogonFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 14)
)
if mibBuilder.loadTexts:
    pppLogonFail.setStatus(
        "current"
    )

iappStationRoamedFrom = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 15)
)
iappStationRoamedFrom.setObjects(
      *(("AP80-PRIVATE-MIB", "dot11Station"),
        ("AP80-PRIVATE-MIB", "dot11ApIpAddress"))
)
if mibBuilder.loadTexts:
    iappStationRoamedFrom.setStatus(
        "current"
    )

iappStationRoamedTo = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 16)
)
iappStationRoamedTo.setObjects(
      *(("AP80-PRIVATE-MIB", "dot11Station"),
        ("AP80-PRIVATE-MIB", "dot11ApIpAddress"))
)
if mibBuilder.loadTexts:
    iappStationRoamedTo.setStatus(
        "current"
    )

iappContextDataSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 17)
)
iappContextDataSent.setObjects(
      *(("AP80-PRIVATE-MIB", "dot11Station"),
        ("AP80-PRIVATE-MIB", "dot11ApIpAddress"))
)
if mibBuilder.loadTexts:
    iappContextDataSent.setStatus(
        "current"
    )

dot1xSupplicantAuthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 7, 4, 2, 18)
)
dot1xSupplicantAuthenticated.setObjects(
    ("AP80-PRIVATE-MIB", "dot11AuthenticatorMacAddr")
)
if mibBuilder.loadTexts:
    dot1xSupplicantAuthenticated.setStatus(
        "current"
    )

sntpServerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 2, 11, 10, 2, 1)
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
    "AP80-PRIVATE-MIB",
    **{"MacAddress": MacAddress,
       "DisplayString": DisplayString,
       "TruthValue": TruthValue,
       "aruba": aruba,
       "arubaEnterpriseMibModules": arubaEnterpriseMibModules,
       "arubaAp": arubaAp,
       "wlsrOutDoorApMibModules": wlsrOutDoorApMibModules,
       "enterpriseApSys": enterpriseApSys,
       "swHardwareVer": swHardwareVer,
       "swBootRomVer": swBootRomVer,
       "swOpCodeVer": swOpCodeVer,
       "swSerialNumber": swSerialNumber,
       "sysNotificationTree": sysNotificationTree,
       "sysNotificationObjects": sysNotificationObjects,
       "sysNotifications": sysNotifications,
       "sysSystemUp": sysSystemUp,
       "sysSystemDown": sysSystemDown,
       "sysRadiusServerChanged": sysRadiusServerChanged,
       "sysConfigFileVersionChanged": sysConfigFileVersionChanged,
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
       "dot11AuthenticationAcctInterimUpdate": dot11AuthenticationAcctInterimUpdate,
       "dot11AuthenticationMACAddressFormat": dot11AuthenticationMACAddressFormat,
       "dot11AuthenticationVLANIDFormat": dot11AuthenticationVLANIDFormat,
       "dot11MACAuthenticationFilter": dot11MACAuthenticationFilter,
       "dot11FilterDefault": dot11FilterDefault,
       "dot11FilterTable": dot11FilterTable,
       "dot11FilterEntry": dot11FilterEntry,
       "dot11FilterAddress": dot11FilterAddress,
       "dot11FilterStatus": dot11FilterStatus,
       "dot11NotificationTree": dot11NotificationTree,
       "dot11NotificationObjects": dot11NotificationObjects,
       "dot11MacAddr": dot11MacAddr,
       "dot11Station": dot11Station,
       "dot11RequestType": dot11RequestType,
       "dot11ReasonCode": dot11ReasonCode,
       "dot11ApIpAddress": dot11ApIpAddress,
       "dot1xAuthenticatorMacAddr": dot1xAuthenticatorMacAddr,
       "dot11Notifications": dot11Notifications,
       "dot11StationAssociation": dot11StationAssociation,
       "dot11StationReAssociation": dot11StationReAssociation,
       "dot11StationAuthentication": dot11StationAuthentication,
       "dot11StationRequestFail": dot11StationRequestFail,
       "dot11InterfaceBFail": dot11InterfaceBFail,
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
       "dot1xSupplicantAuthenticated": dot1xSupplicantAuthenticated,
       "dot11AuthenticationSupplicantTable": dot11AuthenticationSupplicantTable,
       "dot11AuthenticationSupplicantEntry": dot11AuthenticationSupplicantEntry,
       "dot118021xSuppIndex": dot118021xSuppIndex,
       "dot118021xSuppState": dot118021xSuppState,
       "dot118021xSuppUser": dot118021xSuppUser,
       "dot118021xSuppPasswd": dot118021xSuppPasswd,
       "dot11VapAuthenticationTable": dot11VapAuthenticationTable,
       "dot11VapAuthenticationEntry": dot11VapAuthenticationEntry,
       "dot11Vap8021xIndex": dot11Vap8021xIndex,
       "dot11Vap8021xState": dot11Vap8021xState,
       "dot11Vap8021xBroadcastKeyRefreshRate": dot11Vap8021xBroadcastKeyRefreshRate,
       "dot11Vap8021xSessionKeyRefreshRate": dot11Vap8021xSessionKeyRefreshRate,
       "dot11Vap8021xReauthenticationTimeout": dot11Vap8021xReauthenticationTimeout,
       "dot11VapAuthMACAuthenticationType": dot11VapAuthMACAuthenticationType,
       "dot11VapAuthMACAuthenticationTimeout": dot11VapAuthMACAuthenticationTimeout,
       "enterpriseApAdmin": enterpriseApAdmin,
       "enterpriseApAdminUser": enterpriseApAdminUser,
       "enterpriseApAdminPassword": enterpriseApAdminPassword,
       "enterpriseApVLAN": enterpriseApVLAN,
       "enterpriseApVLANNativeId": enterpriseApVLANNativeId,
       "enterpriseApVLANState": enterpriseApVLANState,
       "enterpriseApNativeVlanTable": enterpriseApNativeVlanTable,
       "enterpriseApNativeVlanEntry": enterpriseApNativeVlanEntry,
       "nativeVlanIfIndex": nativeVlanIfIndex,
       "nativeVlanSsidNumber": nativeVlanSsidNumber,
       "nativeVlanVlanId": nativeVlanVlanId,
       "enterpriseApFilterControl": enterpriseApFilterControl,
       "enterpriseApFilterControlInterClientSTAsCommun": enterpriseApFilterControlInterClientSTAsCommun,
       "enterpriseApFilterControlAPManage": enterpriseApFilterControlAPManage,
       "enterpriseApFilterControlEthernet": enterpriseApFilterControlEthernet,
       "enterpriseApFilterProtocolTable": enterpriseApFilterProtocolTable,
       "enterpriseApFilterProtocolEntry": enterpriseApFilterProtocolEntry,
       "enterpriseApFilterProtocolIndex": enterpriseApFilterProtocolIndex,
       "enterpriseApFilterProtocolName": enterpriseApFilterProtocolName,
       "enterpriseApFilterProtocolISODesignator": enterpriseApFilterProtocolISODesignator,
       "enterpriseApFilterProtocolState": enterpriseApFilterProtocolState,
       "enterpriseApFilterUplinkPortMACAddrFilter": enterpriseApFilterUplinkPortMACAddrFilter,
       "uplinkPortMACAddrFilterStatus": uplinkPortMACAddrFilterStatus,
       "uplinkPortMACAddrFilterAddMac": uplinkPortMACAddrFilterAddMac,
       "uplinkPortMACAddrFilteringTable": uplinkPortMACAddrFilteringTable,
       "uplinkPortMACAddrFilteringEntry": uplinkPortMACAddrFilteringEntry,
       "uplinkPortMacAddrIndex": uplinkPortMacAddrIndex,
       "uplinkPortMACAddr": uplinkPortMACAddr,
       "deleteMacAddr": deleteMacAddr,
       "enterpriseApSNTP": enterpriseApSNTP,
       "enterpriseApSNTPState": enterpriseApSNTPState,
       "enterpriseApSNTPPrimaryServer": enterpriseApSNTPPrimaryServer,
       "enterpriseApSNTPSecondaryServer": enterpriseApSNTPSecondaryServer,
       "enterpriseApSNTPTimezone": enterpriseApSNTPTimezone,
       "enterpriseApSNTPDST": enterpriseApSNTPDST,
       "enterpriseApSNTPDSTStartMonth": enterpriseApSNTPDSTStartMonth,
       "enterpriseApSNTPDSTStartDay": enterpriseApSNTPDSTStartDay,
       "enterpriseApSNTPDSTEndMonth": enterpriseApSNTPDSTEndMonth,
       "enterpriseApSNTPDSTEndDay": enterpriseApSNTPDSTEndDay,
       "sntpNotificationTree": sntpNotificationTree,
       "sntpNotificationObjects": sntpNotificationObjects,
       "sntpNotifications": sntpNotifications,
       "sntpServerFail": sntpServerFail,
       "enterpriseApDNS": enterpriseApDNS,
       "enterpriseApDNSPrimaryServer": enterpriseApDNSPrimaryServer,
       "enterpriseApDNSSecondaryServer": enterpriseApDNSSecondaryServer,
       "enterpriseApSyslog": enterpriseApSyslog,
       "enterpriseApSyslogState": enterpriseApSyslogState,
       "enterpriseApSyslogConsoleState": enterpriseApSyslogConsoleState,
       "enterpriseApSyslogLevel": enterpriseApSyslogLevel,
       "enterpriseApSyslogServerTable": enterpriseApSyslogServerTable,
       "enterpriseApSyslogServerEntry": enterpriseApSyslogServerEntry,
       "enterpriseApSyslogServerIndex": enterpriseApSyslogServerIndex,
       "enterpriseApSyslogServerState": enterpriseApSyslogServerState,
       "enterpriseApSyslogServerIPAddress": enterpriseApSyslogServerIPAddress,
       "enterpriseApSyslogServerPort": enterpriseApSyslogServerPort,
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
       "enterpriseApSecurityWPACipherSuite": enterpriseApSecurityWPACipherSuite,
       "enterpriseApSecurityWPAPreAuthentication": enterpriseApSecurityWPAPreAuthentication,
       "enterpriseApSecurityWPAPmksaLifetime": enterpriseApSecurityWPAPmksaLifetime,
       "enterpriseApSsh": enterpriseApSsh,
       "enterpriseApSshServerEnabled": enterpriseApSshServerEnabled,
       "enterpriseApSshServerPort": enterpriseApSshServerPort,
       "enterpriseApSshTelnetServerEnabled": enterpriseApSshTelnetServerEnabled,
       "enterpriseApRadio": enterpriseApRadio,
       "enterpriseApRadioTable": enterpriseApRadioTable,
       "enterpriseApRadioEntry": enterpriseApRadioEntry,
       "enterpriseApRadioIndex": enterpriseApRadioIndex,
       "enterpriseApRadioState": enterpriseApRadioState,
       "enterpriseApRadioAutoChannel": enterpriseApRadioAutoChannel,
       "enterpriseApRadioTransmitPower": enterpriseApRadioTransmitPower,
       "enterpriseApRadioClosedSystem": enterpriseApRadioClosedSystem,
       "enterpriseApRadioMaxAssoc": enterpriseApRadioMaxAssoc,
       "enterpriseApRadioTransmitKey": enterpriseApRadioTransmitKey,
       "enterpriseApRadioTurboMode": enterpriseApRadioTurboMode,
       "enterpriseApRadioDescription": enterpriseApRadioDescription,
       "enterpriseApRadioDataRate": enterpriseApRadioDataRate,
       "enterpriseApRadioGMode": enterpriseApRadioGMode,
       "enterpriseApRadioAntennaMode": enterpriseApRadioAntennaMode,
       "enterpriseApRadioAntennaId": enterpriseApRadioAntennaId,
       "enterpriseApRadioAntennaControlMethod": enterpriseApRadioAntennaControlMethod,
       "enterpriseApRadioAntennaLocation": enterpriseApRadioAntennaLocation,
       "enterpriseApRadioRogueApDetection": enterpriseApRadioRogueApDetection,
       "enterpriseApRadioRogueApScanInterval": enterpriseApRadioRogueApScanInterval,
       "enterpriseApRadioRogueApScanDuration": enterpriseApRadioRogueApScanDuration,
       "enterpriseApRadioRogueApScanNow": enterpriseApRadioRogueApScanNow,
       "enterpriseApRadioMICMode": enterpriseApRadioMICMode,
       "enterpriseApRadioSuperMode": enterpriseApRadioSuperMode,
       "enterpriseApRadioBeaconInterval": enterpriseApRadioBeaconInterval,
       "enterpriseApRadioDataBeaconRate": enterpriseApRadioDataBeaconRate,
       "enterpriseApRadioChannel": enterpriseApRadioChannel,
       "enterpriseApRadioFragmentLength": enterpriseApRadioFragmentLength,
       "enterpriseApRadioRTSThreshold": enterpriseApRadioRTSThreshold,
       "enterpriseApRadioAntennaGainReduction": enterpriseApRadioAntennaGainReduction,
       "enterpriseApSNMP": enterpriseApSNMP,
       "enterpriseApSNMPCommunityReadOnly": enterpriseApSNMPCommunityReadOnly,
       "enterpriseApSNMPCommunityReadWrite": enterpriseApSNMPCommunityReadWrite,
       "enterpriseApSNMPTrapDestinationTable": enterpriseApSNMPTrapDestinationTable,
       "enterpriseApSNMPTrapDestinationEntry": enterpriseApSNMPTrapDestinationEntry,
       "enterpriseApSNMPTrapDestinationIndex": enterpriseApSNMPTrapDestinationIndex,
       "enterpriseApSNMPTrapDestinationCommunity": enterpriseApSNMPTrapDestinationCommunity,
       "enterpriseApSNMPTrapDestinationIP": enterpriseApSNMPTrapDestinationIP,
       "enterpriseApSNMPTrapDestinationState": enterpriseApSNMPTrapDestinationState,
       "enterpriseApSNMPTrapFilters": enterpriseApSNMPTrapFilters,
       "sysSystemUpTrapEnabled": sysSystemUpTrapEnabled,
       "sysSystemDownTrapEnabled": sysSystemDownTrapEnabled,
       "sysRadiusServerChangedTrapEnabled": sysRadiusServerChangedTrapEnabled,
       "sysConfigFileVersionChangedTrapEnabled": sysConfigFileVersionChangedTrapEnabled,
       "dot11StationAssociationTrapEnabled": dot11StationAssociationTrapEnabled,
       "dot11StationReAssociationTrapEnabled": dot11StationReAssociationTrapEnabled,
       "dot11StationAuthenticationTrapEnabled": dot11StationAuthenticationTrapEnabled,
       "dot11StationRequestFailTrapEnabled": dot11StationRequestFailTrapEnabled,
       "dot11InterfaceBFailTrapEnabled": dot11InterfaceBFailTrapEnabled,
       "dot11InterfaceAGFailTrapEnabled": dot11InterfaceAGFailTrapEnabled,
       "dot1xMacAddrAuthSuccessTrapEnabled": dot1xMacAddrAuthSuccessTrapEnabled,
       "dot1xMacAddrAuthFailTrapEnabled": dot1xMacAddrAuthFailTrapEnabled,
       "dot1xAuthNotInitiatedTrapEnabled": dot1xAuthNotInitiatedTrapEnabled,
       "dot1xAuthSuccessTrapEnabled": dot1xAuthSuccessTrapEnabled,
       "dot1xAuthFailTrapEnabled": dot1xAuthFailTrapEnabled,
       "localMacAddrAuthSuccessTrapEnabled": localMacAddrAuthSuccessTrapEnabled,
       "localMacAddrAuthFailTrapEnabled": localMacAddrAuthFailTrapEnabled,
       "pppLogonFailTrapEnabled": pppLogonFailTrapEnabled,
       "iappStationRoamedFromTrapEnabled": iappStationRoamedFromTrapEnabled,
       "iappStationRoamedToTrapEnabled": iappStationRoamedToTrapEnabled,
       "iappContextDataSentTrapEnabled": iappContextDataSentTrapEnabled,
       "sntpServerFailTrapEnabled": sntpServerFailTrapEnabled,
       "dot1xSuppAuthenticatedTrapEnabled": dot1xSuppAuthenticatedTrapEnabled,
       "dot11FailedTransmitsTrapEnabled": dot11FailedTransmitsTrapEnabled,
       "dot11AckFailuresTrapEnabled": dot11AckFailuresTrapEnabled,
       "dot11FcsErrorsTrapEnabled": dot11FcsErrorsTrapEnabled,
       "rogueAPDetectedTrapEnabled": rogueAPDetectedTrapEnabled,
       "possibleRogueAPDetectedTrapEnabled": possibleRogueAPDetectedTrapEnabled,
       "enterpriseApSession": enterpriseApSession,
       "enterpriseApSessionTable": enterpriseApSessionTable,
       "enterpriseApSessionEntry": enterpriseApSessionEntry,
       "enterpriseApSessionIfIndex": enterpriseApSessionIfIndex,
       "enterpriseApSessionStationAddres": enterpriseApSessionStationAddres,
       "enterpriseApSessionAuthenticated": enterpriseApSessionAuthenticated,
       "enterpriseApSessionAssociated": enterpriseApSessionAssociated,
       "enterpriseApSessionIsForwarding": enterpriseApSessionIsForwarding,
       "enterpriseApSessionKeyType": enterpriseApSessionKeyType,
       "enterpriseApSessionAssociationId": enterpriseApSessionAssociationId,
       "enterpriseApSessionLastAuthenticatedTime": enterpriseApSessionLastAuthenticatedTime,
       "enterpriseApSessionAssociatedTime": enterpriseApSessionAssociatedTime,
       "enterpriseApSessionLastAssociatedTime": enterpriseApSessionLastAssociatedTime,
       "enterpriseApSessionLastDisassociatedTime": enterpriseApSessionLastDisassociatedTime,
       "enterpriseApSessionTxPacketCount": enterpriseApSessionTxPacketCount,
       "enterpriseApSessionRxPacketCount": enterpriseApSessionRxPacketCount,
       "enterpriseApSessionTxByteCount": enterpriseApSessionTxByteCount,
       "enterpriseApSessionRxByteCount": enterpriseApSessionRxByteCount,
       "enterpriseAPVapRadio": enterpriseAPVapRadio,
       "enterpriseAPVapRadioTable": enterpriseAPVapRadioTable,
       "enterpriseAPVapRadioEntry": enterpriseAPVapRadioEntry,
       "enterpriseAPVapRadioIndex": enterpriseAPVapRadioIndex,
       "enterpriseAPVapRadioState": enterpriseAPVapRadioState,
       "enterpriseAPVapRadioClosedSystem": enterpriseAPVapRadioClosedSystem,
       "enterpriseAPVapRadioMaxAssoc": enterpriseAPVapRadioMaxAssoc,
       "enterpriseAPVapRadioTransmitKey": enterpriseAPVapRadioTransmitKey,
       "enterpriseAPVapRadioDescription": enterpriseAPVapRadioDescription,
       "enterpriseAPVapRadioAuthTimeoutInterval": enterpriseAPVapRadioAuthTimeoutInterval,
       "enterpriseAPVapRadioAssocTimeoutInterval": enterpriseAPVapRadioAssocTimeoutInterval,
       "enterpriseAPVapRadioWPA2PMKSALifeTime": enterpriseAPVapRadioWPA2PMKSALifeTime,
       "enterpriseApRadioWds": enterpriseApRadioWds,
       "enterpriseApRadioWdsTable": enterpriseApRadioWdsTable,
       "enterpriseApRadioWdsEntry": enterpriseApRadioWdsEntry,
       "wdsApRole": wdsApRole,
       "wdsChannelAutoSync": wdsChannelAutoSync,
       "wdsMasterSlaveMode": wdsMasterSlaveMode,
       "enterpriseApRadioWdsPeerTable": enterpriseApRadioWdsPeerTable,
       "enterpriseApRadioWdsPeerEntry": enterpriseApRadioWdsPeerEntry,
       "wdsPeerIndex": wdsPeerIndex,
       "wdsPeerBssid": wdsPeerBssid,
       "enterpriseApWMM": enterpriseApWMM,
       "enterpriseApWMMTable": enterpriseApWMMTable,
       "enterpriseApWMMEntry": enterpriseApWMMEntry,
       "enterpriseApWMMModeIndex": enterpriseApWMMModeIndex,
       "enterpriseApWMMMode": enterpriseApWMMMode,
       "enterpriseApWMMAckPolicyTable": enterpriseApWMMAckPolicyTable,
       "enterpriseApWMMAckPolicyEntry": enterpriseApWMMAckPolicyEntry,
       "enterpriseApWMMAckPolicyIndex": enterpriseApWMMAckPolicyIndex,
       "enterpriseApWMMACKPolicy": enterpriseApWMMACKPolicy,
       "enterpriseApWMMBSSParamTable": enterpriseApWMMBSSParamTable,
       "enterpriseApWMMBSSParamEntry": enterpriseApWMMBSSParamEntry,
       "enterpriseApWMMBSSParamIndex": enterpriseApWMMBSSParamIndex,
       "enterpriseApWMMBSSParamLogCwMin": enterpriseApWMMBSSParamLogCwMin,
       "enterpriseApWMMBSSParamLogCwMax": enterpriseApWMMBSSParamLogCwMax,
       "enterpriseApWMMBSSParamAIFSN": enterpriseApWMMBSSParamAIFSN,
       "enterpriseApWMMBSSParamTXOPLimit": enterpriseApWMMBSSParamTXOPLimit,
       "enterpriseApWMMBSSParamAdmissionCtrl": enterpriseApWMMBSSParamAdmissionCtrl,
       "enterpriseApWMMAPParamTable": enterpriseApWMMAPParamTable,
       "enterpriseApWMMAPParamEntry": enterpriseApWMMAPParamEntry,
       "enterpriseApWMMAPParamIndex": enterpriseApWMMAPParamIndex,
       "enterpriseApWMMAPParamLogCwMin": enterpriseApWMMAPParamLogCwMin,
       "enterpriseApWMMAPParamLogCwMax": enterpriseApWMMAPParamLogCwMax,
       "enterpriseApWMMAPParamAIFSN": enterpriseApWMMAPParamAIFSN,
       "enterpriseApWMMAPParamTXOPLimit": enterpriseApWMMAPParamTXOPLimit,
       "enterpriseApWMMAPParamAdmissionCtrl": enterpriseApWMMAPParamAdmissionCtrl,
       "enterpriseApSTP": enterpriseApSTP,
       "enterpriseApSTPBridgeStatus": enterpriseApSTPBridgeStatus,
       "enterpriseApSTPBridgePriority": enterpriseApSTPBridgePriority,
       "enterpriseApSTPBridgeMaxAge": enterpriseApSTPBridgeMaxAge,
       "enterpriseApSTPHelloTime": enterpriseApSTPHelloTime,
       "enterpriseApSTPBridgeForwardingDelay": enterpriseApSTPBridgeForwardingDelay,
       "enterpriseApSTPRadioInterface": enterpriseApSTPRadioInterface,
       "enterpriseApSTPNodeTable": enterpriseApSTPNodeTable,
       "enterpriseApSTPNodeEntry": enterpriseApSTPNodeEntry,
       "enterpriseApSTPNodeIndex": enterpriseApSTPNodeIndex,
       "enterpriseApSTPNodeLinkPathCost": enterpriseApSTPNodeLinkPathCost,
       "enterpriseApSTPNodeLinkPortPriority": enterpriseApSTPNodeLinkPortPriority,
       "enterpriseApSTPEthernetInterface": enterpriseApSTPEthernetInterface,
       "enterpriseApSTPEthernetLinkPathCost": enterpriseApSTPEthernetLinkPathCost,
       "enterpriseApSTPEthernetLinkPortPriority": enterpriseApSTPEthernetLinkPortPriority}
)

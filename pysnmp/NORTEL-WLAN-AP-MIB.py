# SNMP MIB module (NORTEL-WLAN-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NORTEL-WLAN-AP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:58 2024
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

(InterfaceIndex,
 ifIndex,
 ifPhysAddress) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "ifPhysAddress")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wlan2200,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "wlan2200")


# MODULE-IDENTITY

nortelWlanApMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1)
)
nortelWlanApMib.setRevisions(
        ("2003-07-16 00:00",
         "2003-09-11 00:00",
         "2004-04-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NtWlanApDataRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )



class NtWlanApWEPKey(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_NtWlanApSys_ObjectIdentity = ObjectIdentity
ntWlanApSys = _NtWlanApSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 1)
)


class _NtWlanSwHardwareVer_Type(DisplayString):
    """Custom type ntWlanSwHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtWlanSwHardwareVer_Type.__name__ = "DisplayString"
_NtWlanSwHardwareVer_Object = MibScalar
ntWlanSwHardwareVer = _NtWlanSwHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 1, 1),
    _NtWlanSwHardwareVer_Type()
)
ntWlanSwHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanSwHardwareVer.setStatus("current")


class _NtWlanSwBootRomVer_Type(DisplayString):
    """Custom type ntWlanSwBootRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtWlanSwBootRomVer_Type.__name__ = "DisplayString"
_NtWlanSwBootRomVer_Object = MibScalar
ntWlanSwBootRomVer = _NtWlanSwBootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 1, 2),
    _NtWlanSwBootRomVer_Type()
)
ntWlanSwBootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanSwBootRomVer.setStatus("current")


class _NtWlanSwOpCodeVer_Type(DisplayString):
    """Custom type ntWlanSwOpCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtWlanSwOpCodeVer_Type.__name__ = "DisplayString"
_NtWlanSwOpCodeVer_Object = MibScalar
ntWlanSwOpCodeVer = _NtWlanSwOpCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 1, 3),
    _NtWlanSwOpCodeVer_Type()
)
ntWlanSwOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanSwOpCodeVer.setStatus("current")


class _NtWlanSwCountryCode_Type(DisplayString):
    """Custom type ntWlanSwCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NtWlanSwCountryCode_Type.__name__ = "DisplayString"
_NtWlanSwCountryCode_Object = MibScalar
ntWlanSwCountryCode = _NtWlanSwCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 1, 4),
    _NtWlanSwCountryCode_Type()
)
ntWlanSwCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanSwCountryCode.setStatus("current")


class _NtWlanSwNNDataFileVer_Type(DisplayString):
    """Custom type ntWlanSwNNDataFileVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtWlanSwNNDataFileVer_Type.__name__ = "DisplayString"
_NtWlanSwNNDataFileVer_Object = MibScalar
ntWlanSwNNDataFileVer = _NtWlanSwNNDataFileVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 1, 5),
    _NtWlanSwNNDataFileVer_Type()
)
ntWlanSwNNDataFileVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanSwNNDataFileVer.setStatus("current")
_NtWlanApLineMgnt_ObjectIdentity = ObjectIdentity
ntWlanApLineMgnt = _NtWlanApLineMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 2)
)
_NtWlanLineTable_Object = MibTable
ntWlanLineTable = _NtWlanLineTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ntWlanLineTable.setStatus("current")
_NtWlanLineEntry_Object = MibTableRow
ntWlanLineEntry = _NtWlanLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 2, 1, 1)
)
ntWlanLineEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanLineIndex"),
)
if mibBuilder.loadTexts:
    ntWlanLineEntry.setStatus("current")


class _NtWlanLineIndex_Type(Integer32):
    """Custom type ntWlanLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtWlanLineIndex_Type.__name__ = "Integer32"
_NtWlanLineIndex_Object = MibTableColumn
ntWlanLineIndex = _NtWlanLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 2, 1, 1, 1),
    _NtWlanLineIndex_Type()
)
ntWlanLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanLineIndex.setStatus("current")
_NtWlanLineDataBits_Type = Integer32
_NtWlanLineDataBits_Object = MibTableColumn
ntWlanLineDataBits = _NtWlanLineDataBits_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 2, 1, 1, 2),
    _NtWlanLineDataBits_Type()
)
ntWlanLineDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanLineDataBits.setStatus("current")


class _NtWlanLineParity_Type(Integer32):
    """Custom type ntWlanLineParity based on Integer32"""
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


_NtWlanLineParity_Type.__name__ = "Integer32"
_NtWlanLineParity_Object = MibTableColumn
ntWlanLineParity = _NtWlanLineParity_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 2, 1, 1, 3),
    _NtWlanLineParity_Type()
)
ntWlanLineParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanLineParity.setStatus("current")
_NtWlanLineSpeed_Type = Integer32
_NtWlanLineSpeed_Object = MibTableColumn
ntWlanLineSpeed = _NtWlanLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 2, 1, 1, 4),
    _NtWlanLineSpeed_Type()
)
ntWlanLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanLineSpeed.setStatus("current")
_NtWlanLineStopBits_Type = Integer32
_NtWlanLineStopBits_Object = MibTableColumn
ntWlanLineStopBits = _NtWlanLineStopBits_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 2, 1, 1, 5),
    _NtWlanLineStopBits_Type()
)
ntWlanLineStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanLineStopBits.setStatus("current")
_NtWlanApPortMgnt_ObjectIdentity = ObjectIdentity
ntWlanApPortMgnt = _NtWlanApPortMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3)
)
_NtWlanPortTable_Object = MibTable
ntWlanPortTable = _NtWlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ntWlanPortTable.setStatus("current")
_NtWlanPortEntry_Object = MibTableRow
ntWlanPortEntry = _NtWlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3, 1, 1)
)
ntWlanPortEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanPortIndex"),
)
if mibBuilder.loadTexts:
    ntWlanPortEntry.setStatus("current")
_NtWlanPortIndex_Type = InterfaceIndex
_NtWlanPortIndex_Object = MibTableColumn
ntWlanPortIndex = _NtWlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3, 1, 1, 1),
    _NtWlanPortIndex_Type()
)
ntWlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanPortIndex.setStatus("current")


class _NtWlanPortName_Type(DisplayString):
    """Custom type ntWlanPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NtWlanPortName_Type.__name__ = "DisplayString"
_NtWlanPortName_Object = MibTableColumn
ntWlanPortName = _NtWlanPortName_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3, 1, 1, 2),
    _NtWlanPortName_Type()
)
ntWlanPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanPortName.setStatus("current")


class _NtWlanPortType_Type(Integer32):
    """Custom type ntWlanPortType based on Integer32"""
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


_NtWlanPortType_Type.__name__ = "Integer32"
_NtWlanPortType_Object = MibTableColumn
ntWlanPortType = _NtWlanPortType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3, 1, 1, 3),
    _NtWlanPortType_Type()
)
ntWlanPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanPortType.setStatus("current")


class _NtWlanPortSpeedDpxCfg_Type(Integer32):
    """Custom type ntWlanPortSpeedDpxCfg based on Integer32"""
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


_NtWlanPortSpeedDpxCfg_Type.__name__ = "Integer32"
_NtWlanPortSpeedDpxCfg_Object = MibTableColumn
ntWlanPortSpeedDpxCfg = _NtWlanPortSpeedDpxCfg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3, 1, 1, 4),
    _NtWlanPortSpeedDpxCfg_Type()
)
ntWlanPortSpeedDpxCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanPortSpeedDpxCfg.setStatus("current")


class _NtWlanPortFlowCtrlCfg_Type(Integer32):
    """Custom type ntWlanPortFlowCtrlCfg based on Integer32"""
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


_NtWlanPortFlowCtrlCfg_Type.__name__ = "Integer32"
_NtWlanPortFlowCtrlCfg_Object = MibTableColumn
ntWlanPortFlowCtrlCfg = _NtWlanPortFlowCtrlCfg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3, 1, 1, 5),
    _NtWlanPortFlowCtrlCfg_Type()
)
ntWlanPortFlowCtrlCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanPortFlowCtrlCfg.setStatus("current")


class _NtWlanPortCapabilities_Type(Integer32):
    """Custom type ntWlanPortCapabilities based on Integer32"""
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


_NtWlanPortCapabilities_Type.__name__ = "Integer32"
_NtWlanPortCapabilities_Object = MibTableColumn
ntWlanPortCapabilities = _NtWlanPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3, 1, 1, 6),
    _NtWlanPortCapabilities_Type()
)
ntWlanPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanPortCapabilities.setStatus("current")


class _NtWlanPortAutonegotiation_Type(Integer32):
    """Custom type ntWlanPortAutonegotiation based on Integer32"""
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


_NtWlanPortAutonegotiation_Type.__name__ = "Integer32"
_NtWlanPortAutonegotiation_Object = MibTableColumn
ntWlanPortAutonegotiation = _NtWlanPortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3, 1, 1, 7),
    _NtWlanPortAutonegotiation_Type()
)
ntWlanPortAutonegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanPortAutonegotiation.setStatus("current")


class _NtWlanPortSpeedDpxStatus_Type(Integer32):
    """Custom type ntWlanPortSpeedDpxStatus based on Integer32"""
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


_NtWlanPortSpeedDpxStatus_Type.__name__ = "Integer32"
_NtWlanPortSpeedDpxStatus_Object = MibTableColumn
ntWlanPortSpeedDpxStatus = _NtWlanPortSpeedDpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3, 1, 1, 8),
    _NtWlanPortSpeedDpxStatus_Type()
)
ntWlanPortSpeedDpxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanPortSpeedDpxStatus.setStatus("current")


class _NtWlanPortFlowCtrlStatus_Type(Integer32):
    """Custom type ntWlanPortFlowCtrlStatus based on Integer32"""
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


_NtWlanPortFlowCtrlStatus_Type.__name__ = "Integer32"
_NtWlanPortFlowCtrlStatus_Object = MibTableColumn
ntWlanPortFlowCtrlStatus = _NtWlanPortFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 3, 1, 1, 9),
    _NtWlanPortFlowCtrlStatus_Type()
)
ntWlanPortFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanPortFlowCtrlStatus.setStatus("current")
_NtWlanApFileTransferMgt_ObjectIdentity = ObjectIdentity
ntWlanApFileTransferMgt = _NtWlanApFileTransferMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 4)
)


class _NtWlanTransferStart_Type(Integer32):
    """Custom type ntWlanTransferStart based on Integer32"""
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


_NtWlanTransferStart_Type.__name__ = "Integer32"
_NtWlanTransferStart_Object = MibScalar
ntWlanTransferStart = _NtWlanTransferStart_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 4, 1),
    _NtWlanTransferStart_Type()
)
ntWlanTransferStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanTransferStart.setStatus("current")


class _NtWlanTransferType_Type(Integer32):
    """Custom type ntWlanTransferType based on Integer32"""
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
        *(("ftpDownload", 1),
          ("ftpUpload", 3),
          ("tftpDownload", 2),
          ("tftpUpload", 4))
    )


_NtWlanTransferType_Type.__name__ = "Integer32"
_NtWlanTransferType_Object = MibScalar
ntWlanTransferType = _NtWlanTransferType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 4, 2),
    _NtWlanTransferType_Type()
)
ntWlanTransferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanTransferType.setStatus("current")


class _NtWlanFileType_Type(Integer32):
    """Custom type ntWlanFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("firmware", 1),
          ("nortelConfig", 3))
    )


_NtWlanFileType_Type.__name__ = "Integer32"
_NtWlanFileType_Object = MibScalar
ntWlanFileType = _NtWlanFileType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 4, 3),
    _NtWlanFileType_Type()
)
ntWlanFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanFileType.setStatus("current")


class _NtWlanSrcFile_Type(DisplayString):
    """Custom type ntWlanSrcFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NtWlanSrcFile_Type.__name__ = "DisplayString"
_NtWlanSrcFile_Object = MibScalar
ntWlanSrcFile = _NtWlanSrcFile_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 4, 4),
    _NtWlanSrcFile_Type()
)
ntWlanSrcFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanSrcFile.setStatus("current")


class _NtWlanDestFile_Type(DisplayString):
    """Custom type ntWlanDestFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NtWlanDestFile_Type.__name__ = "DisplayString"
_NtWlanDestFile_Object = MibScalar
ntWlanDestFile = _NtWlanDestFile_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 4, 5),
    _NtWlanDestFile_Type()
)
ntWlanDestFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDestFile.setStatus("current")
_NtWlanFileServer_Type = IpAddress
_NtWlanFileServer_Object = MibScalar
ntWlanFileServer = _NtWlanFileServer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 4, 6),
    _NtWlanFileServer_Type()
)
ntWlanFileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanFileServer.setStatus("current")


class _NtWlanUserName_Type(DisplayString):
    """Custom type ntWlanUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NtWlanUserName_Type.__name__ = "DisplayString"
_NtWlanUserName_Object = MibScalar
ntWlanUserName = _NtWlanUserName_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 4, 7),
    _NtWlanUserName_Type()
)
ntWlanUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanUserName.setStatus("current")


class _NtWlanPassword_Type(DisplayString):
    """Custom type ntWlanPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NtWlanPassword_Type.__name__ = "DisplayString"
_NtWlanPassword_Object = MibScalar
ntWlanPassword = _NtWlanPassword_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 4, 8),
    _NtWlanPassword_Type()
)
ntWlanPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanPassword.setStatus("current")


class _NtWlanFileTransferStatus_Type(Integer32):
    """Custom type ntWlanFileTransferStatus based on Integer32"""
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
        *(("fail", 4),
          ("fileNotFound", 9),
          ("inProgress", 2),
          ("invalidDestination", 6),
          ("invalidSource", 5),
          ("none", 1),
          ("outOfMemory", 7),
          ("outOfSpace", 8),
          ("success", 3))
    )


_NtWlanFileTransferStatus_Type.__name__ = "Integer32"
_NtWlanFileTransferStatus_Object = MibScalar
ntWlanFileTransferStatus = _NtWlanFileTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 4, 9),
    _NtWlanFileTransferStatus_Type()
)
ntWlanFileTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanFileTransferStatus.setStatus("current")
_NtWlanApResetMgt_ObjectIdentity = ObjectIdentity
ntWlanApResetMgt = _NtWlanApResetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 5)
)


class _NtWlanRestartOpCodeFile_Type(DisplayString):
    """Custom type ntWlanRestartOpCodeFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NtWlanRestartOpCodeFile_Type.__name__ = "DisplayString"
_NtWlanRestartOpCodeFile_Object = MibScalar
ntWlanRestartOpCodeFile = _NtWlanRestartOpCodeFile_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 5, 1),
    _NtWlanRestartOpCodeFile_Type()
)
ntWlanRestartOpCodeFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanRestartOpCodeFile.setStatus("current")


class _NtWlanRestartControl_Type(Integer32):
    """Custom type ntWlanRestartControl based on Integer32"""
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


_NtWlanRestartControl_Type.__name__ = "Integer32"
_NtWlanRestartControl_Object = MibScalar
ntWlanRestartControl = _NtWlanRestartControl_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 5, 2),
    _NtWlanRestartControl_Type()
)
ntWlanRestartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanRestartControl.setStatus("current")
_NtWlanApIpMgt_ObjectIdentity = ObjectIdentity
ntWlanApIpMgt = _NtWlanApIpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 6)
)
_NtWlanNetConfigIPAddress_Type = IpAddress
_NtWlanNetConfigIPAddress_Object = MibScalar
ntWlanNetConfigIPAddress = _NtWlanNetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 6, 1),
    _NtWlanNetConfigIPAddress_Type()
)
ntWlanNetConfigIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanNetConfigIPAddress.setStatus("current")
_NtWlanNetConfigSubnetMask_Type = IpAddress
_NtWlanNetConfigSubnetMask_Object = MibScalar
ntWlanNetConfigSubnetMask = _NtWlanNetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 6, 2),
    _NtWlanNetConfigSubnetMask_Type()
)
ntWlanNetConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanNetConfigSubnetMask.setStatus("current")
_NtWlanNetDefaultGateway_Type = IpAddress
_NtWlanNetDefaultGateway_Object = MibScalar
ntWlanNetDefaultGateway = _NtWlanNetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 6, 3),
    _NtWlanNetDefaultGateway_Type()
)
ntWlanNetDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanNetDefaultGateway.setStatus("current")


class _NtWlanIpHttpState_Type(Integer32):
    """Custom type ntWlanIpHttpState based on Integer32"""
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


_NtWlanIpHttpState_Type.__name__ = "Integer32"
_NtWlanIpHttpState_Object = MibScalar
ntWlanIpHttpState = _NtWlanIpHttpState_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 6, 4),
    _NtWlanIpHttpState_Type()
)
ntWlanIpHttpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanIpHttpState.setStatus("current")


class _NtWlanIpHttpPort_Type(Integer32):
    """Custom type ntWlanIpHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtWlanIpHttpPort_Type.__name__ = "Integer32"
_NtWlanIpHttpPort_Object = MibScalar
ntWlanIpHttpPort = _NtWlanIpHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 6, 5),
    _NtWlanIpHttpPort_Type()
)
ntWlanIpHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanIpHttpPort.setStatus("current")
_NtWlanApDot11_ObjectIdentity = ObjectIdentity
ntWlanApDot11 = _NtWlanApDot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7)
)
_NtWlanDot11Phy_ObjectIdentity = ObjectIdentity
ntWlanDot11Phy = _NtWlanDot11Phy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 4)
)
_NtWlanDot11PhyOperationTable_Object = MibTable
ntWlanDot11PhyOperationTable = _NtWlanDot11PhyOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 4, 1)
)
if mibBuilder.loadTexts:
    ntWlanDot11PhyOperationTable.setStatus("current")
_NtWlanDot11PhyOperationEntry_Object = MibTableRow
ntWlanDot11PhyOperationEntry = _NtWlanDot11PhyOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 4, 1, 1)
)
ntWlanDot11PhyOperationEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanDot11Index"),
)
if mibBuilder.loadTexts:
    ntWlanDot11PhyOperationEntry.setStatus("current")


class _NtWlanDot11Index_Type(Integer32):
    """Custom type ntWlanDot11Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtWlanDot11Index_Type.__name__ = "Integer32"
_NtWlanDot11Index_Object = MibTableColumn
ntWlanDot11Index = _NtWlanDot11Index_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 4, 1, 1, 1),
    _NtWlanDot11Index_Type()
)
ntWlanDot11Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanDot11Index.setStatus("current")


class _NtWlanDot11TurboModeEnabled_Type(Integer32):
    """Custom type ntWlanDot11TurboModeEnabled based on Integer32"""
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


_NtWlanDot11TurboModeEnabled_Type.__name__ = "Integer32"
_NtWlanDot11TurboModeEnabled_Object = MibTableColumn
ntWlanDot11TurboModeEnabled = _NtWlanDot11TurboModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 4, 1, 1, 3),
    _NtWlanDot11TurboModeEnabled_Type()
)
ntWlanDot11TurboModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanDot11TurboModeEnabled.setStatus("current")


class _NtWlanDot11PreambleLength_Type(Integer32):
    """Custom type ntWlanDot11PreambleLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1),
          ("twelveSymbols", 99))
    )


_NtWlanDot11PreambleLength_Type.__name__ = "Integer32"
_NtWlanDot11PreambleLength_Object = MibTableColumn
ntWlanDot11PreambleLength = _NtWlanDot11PreambleLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 4, 1, 1, 4),
    _NtWlanDot11PreambleLength_Type()
)
ntWlanDot11PreambleLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11PreambleLength.setStatus("current")
_NtWlanDot11dWorldModeEnabled_Type = TruthValue
_NtWlanDot11dWorldModeEnabled_Object = MibTableColumn
ntWlanDot11dWorldModeEnabled = _NtWlanDot11dWorldModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 4, 1, 1, 5),
    _NtWlanDot11dWorldModeEnabled_Type()
)
ntWlanDot11dWorldModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11dWorldModeEnabled.setStatus("current")
_NtWlanDot11ClosedSystem_Type = TruthValue
_NtWlanDot11ClosedSystem_Object = MibTableColumn
ntWlanDot11ClosedSystem = _NtWlanDot11ClosedSystem_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 4, 1, 1, 6),
    _NtWlanDot11ClosedSystem_Type()
)
ntWlanDot11ClosedSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11ClosedSystem.setStatus("current")
_NtWlanDot11AuthenticationEntry_ObjectIdentity = ObjectIdentity
ntWlanDot11AuthenticationEntry = _NtWlanDot11AuthenticationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 5)
)
_NtWlanDot118021xSupport_Type = TruthValue
_NtWlanDot118021xSupport_Object = MibScalar
ntWlanDot118021xSupport = _NtWlanDot118021xSupport_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 5, 1),
    _NtWlanDot118021xSupport_Type()
)
ntWlanDot118021xSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot118021xSupport.setStatus("current")
_NtWlanDot118021xRequired_Type = TruthValue
_NtWlanDot118021xRequired_Object = MibScalar
ntWlanDot118021xRequired = _NtWlanDot118021xRequired_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 5, 2),
    _NtWlanDot118021xRequired_Type()
)
ntWlanDot118021xRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot118021xRequired.setStatus("current")


class _NtWlanDot118021xBcastKeyRefresh_Type(Integer32):
    """Custom type ntWlanDot118021xBcastKeyRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_NtWlanDot118021xBcastKeyRefresh_Type.__name__ = "Integer32"
_NtWlanDot118021xBcastKeyRefresh_Object = MibScalar
ntWlanDot118021xBcastKeyRefresh = _NtWlanDot118021xBcastKeyRefresh_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 5, 3),
    _NtWlanDot118021xBcastKeyRefresh_Type()
)
ntWlanDot118021xBcastKeyRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot118021xBcastKeyRefresh.setStatus("current")
if mibBuilder.loadTexts:
    ntWlanDot118021xBcastKeyRefresh.setUnits("Minutes")


class _NtWlanDot118021xSessKeyRefresh_Type(Integer32):
    """Custom type ntWlanDot118021xSessKeyRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_NtWlanDot118021xSessKeyRefresh_Type.__name__ = "Integer32"
_NtWlanDot118021xSessKeyRefresh_Object = MibScalar
ntWlanDot118021xSessKeyRefresh = _NtWlanDot118021xSessKeyRefresh_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 5, 4),
    _NtWlanDot118021xSessKeyRefresh_Type()
)
ntWlanDot118021xSessKeyRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot118021xSessKeyRefresh.setStatus("current")
if mibBuilder.loadTexts:
    ntWlanDot118021xSessKeyRefresh.setUnits("Minutes")


class _NtWlanDot118021xReAuthRefresh_Type(Integer32):
    """Custom type ntWlanDot118021xReAuthRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtWlanDot118021xReAuthRefresh_Type.__name__ = "Integer32"
_NtWlanDot118021xReAuthRefresh_Object = MibScalar
ntWlanDot118021xReAuthRefresh = _NtWlanDot118021xReAuthRefresh_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 5, 5),
    _NtWlanDot118021xReAuthRefresh_Type()
)
ntWlanDot118021xReAuthRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot118021xReAuthRefresh.setStatus("current")
if mibBuilder.loadTexts:
    ntWlanDot118021xReAuthRefresh.setUnits("Seconds")
_NtWlanDot11AuthenticationServerTable_Object = MibTable
ntWlanDot11AuthenticationServerTable = _NtWlanDot11AuthenticationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6)
)
if mibBuilder.loadTexts:
    ntWlanDot11AuthenticationServerTable.setStatus("current")
_NtWlanDot11AuthenticationServerEntry_Object = MibTableRow
ntWlanDot11AuthenticationServerEntry = _NtWlanDot11AuthenticationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1)
)
ntWlanDot11AuthenticationServerEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanDot11ServerIndex"),
)
if mibBuilder.loadTexts:
    ntWlanDot11AuthenticationServerEntry.setStatus("current")


class _NtWlanDot11ServerIndex_Type(Integer32):
    """Custom type ntWlanDot11ServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtWlanDot11ServerIndex_Type.__name__ = "Integer32"
_NtWlanDot11ServerIndex_Object = MibTableColumn
ntWlanDot11ServerIndex = _NtWlanDot11ServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1, 1),
    _NtWlanDot11ServerIndex_Type()
)
ntWlanDot11ServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanDot11ServerIndex.setStatus("current")
_NtWlanDot11AuthenticationServer_Type = IpAddress
_NtWlanDot11AuthenticationServer_Object = MibTableColumn
ntWlanDot11AuthenticationServer = _NtWlanDot11AuthenticationServer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1, 2),
    _NtWlanDot11AuthenticationServer_Type()
)
ntWlanDot11AuthenticationServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11AuthenticationServer.setStatus("current")


class _NtWlanDot11AuthenticationPort_Type(Integer32):
    """Custom type ntWlanDot11AuthenticationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_NtWlanDot11AuthenticationPort_Type.__name__ = "Integer32"
_NtWlanDot11AuthenticationPort_Object = MibTableColumn
ntWlanDot11AuthenticationPort = _NtWlanDot11AuthenticationPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1, 3),
    _NtWlanDot11AuthenticationPort_Type()
)
ntWlanDot11AuthenticationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11AuthenticationPort.setStatus("current")


class _NtWlanDot11AuthenticationKey_Type(DisplayString):
    """Custom type ntWlanDot11AuthenticationKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtWlanDot11AuthenticationKey_Type.__name__ = "DisplayString"
_NtWlanDot11AuthenticationKey_Object = MibTableColumn
ntWlanDot11AuthenticationKey = _NtWlanDot11AuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1, 4),
    _NtWlanDot11AuthenticationKey_Type()
)
ntWlanDot11AuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11AuthenticationKey.setStatus("current")


class _NtWlanDot11AuthenticationRetransmit_Type(Integer32):
    """Custom type ntWlanDot11AuthenticationRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_NtWlanDot11AuthenticationRetransmit_Type.__name__ = "Integer32"
_NtWlanDot11AuthenticationRetransmit_Object = MibTableColumn
ntWlanDot11AuthenticationRetransmit = _NtWlanDot11AuthenticationRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1, 5),
    _NtWlanDot11AuthenticationRetransmit_Type()
)
ntWlanDot11AuthenticationRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11AuthenticationRetransmit.setStatus("current")


class _NtWlanDot11AuthenticationTimeout_Type(Integer32):
    """Custom type ntWlanDot11AuthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_NtWlanDot11AuthenticationTimeout_Type.__name__ = "Integer32"
_NtWlanDot11AuthenticationTimeout_Object = MibTableColumn
ntWlanDot11AuthenticationTimeout = _NtWlanDot11AuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1, 6),
    _NtWlanDot11AuthenticationTimeout_Type()
)
ntWlanDot11AuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11AuthenticationTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ntWlanDot11AuthenticationTimeout.setUnits("Seconds")
_NtWlanDot11SecondaryAuthServer_Type = IpAddress
_NtWlanDot11SecondaryAuthServer_Object = MibTableColumn
ntWlanDot11SecondaryAuthServer = _NtWlanDot11SecondaryAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1, 7),
    _NtWlanDot11SecondaryAuthServer_Type()
)
ntWlanDot11SecondaryAuthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11SecondaryAuthServer.setStatus("current")


class _NtWlanDot11SecondaryAuthPort_Type(Integer32):
    """Custom type ntWlanDot11SecondaryAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_NtWlanDot11SecondaryAuthPort_Type.__name__ = "Integer32"
_NtWlanDot11SecondaryAuthPort_Object = MibTableColumn
ntWlanDot11SecondaryAuthPort = _NtWlanDot11SecondaryAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1, 8),
    _NtWlanDot11SecondaryAuthPort_Type()
)
ntWlanDot11SecondaryAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11SecondaryAuthPort.setStatus("current")


class _NtWlanDot11SecondaryAuthKey_Type(DisplayString):
    """Custom type ntWlanDot11SecondaryAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtWlanDot11SecondaryAuthKey_Type.__name__ = "DisplayString"
_NtWlanDot11SecondaryAuthKey_Object = MibTableColumn
ntWlanDot11SecondaryAuthKey = _NtWlanDot11SecondaryAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1, 9),
    _NtWlanDot11SecondaryAuthKey_Type()
)
ntWlanDot11SecondaryAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11SecondaryAuthKey.setStatus("current")


class _NtWlanDot11SecondaryAuthRetransmit_Type(Integer32):
    """Custom type ntWlanDot11SecondaryAuthRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_NtWlanDot11SecondaryAuthRetransmit_Type.__name__ = "Integer32"
_NtWlanDot11SecondaryAuthRetransmit_Object = MibTableColumn
ntWlanDot11SecondaryAuthRetransmit = _NtWlanDot11SecondaryAuthRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1, 10),
    _NtWlanDot11SecondaryAuthRetransmit_Type()
)
ntWlanDot11SecondaryAuthRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11SecondaryAuthRetransmit.setStatus("current")


class _NtWlanDot11SecondaryAuthTimeout_Type(Integer32):
    """Custom type ntWlanDot11SecondaryAuthTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_NtWlanDot11SecondaryAuthTimeout_Type.__name__ = "Integer32"
_NtWlanDot11SecondaryAuthTimeout_Object = MibTableColumn
ntWlanDot11SecondaryAuthTimeout = _NtWlanDot11SecondaryAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 6, 1, 11),
    _NtWlanDot11SecondaryAuthTimeout_Type()
)
ntWlanDot11SecondaryAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11SecondaryAuthTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ntWlanDot11SecondaryAuthTimeout.setUnits("Seconds")
_NtWlanDot11FilterTable_Object = MibTable
ntWlanDot11FilterTable = _NtWlanDot11FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 7)
)
if mibBuilder.loadTexts:
    ntWlanDot11FilterTable.setStatus("current")
_NtWlanDot11FilterEntry_Object = MibTableRow
ntWlanDot11FilterEntry = _NtWlanDot11FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 7, 1)
)
ntWlanDot11FilterEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanDot11FilterIndex"),
)
if mibBuilder.loadTexts:
    ntWlanDot11FilterEntry.setStatus("current")


class _NtWlanDot11FilterIndex_Type(Integer32):
    """Custom type ntWlanDot11FilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtWlanDot11FilterIndex_Type.__name__ = "Integer32"
_NtWlanDot11FilterIndex_Object = MibTableColumn
ntWlanDot11FilterIndex = _NtWlanDot11FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 7, 1, 1),
    _NtWlanDot11FilterIndex_Type()
)
ntWlanDot11FilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanDot11FilterIndex.setStatus("current")
_NtWlanDot11FilterAddress_Type = PhysAddress
_NtWlanDot11FilterAddress_Object = MibTableColumn
ntWlanDot11FilterAddress = _NtWlanDot11FilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 7, 1, 2),
    _NtWlanDot11FilterAddress_Type()
)
ntWlanDot11FilterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11FilterAddress.setStatus("current")


class _NtWlanDot11FilterStatus_Type(Integer32):
    """Custom type ntWlanDot11FilterStatus based on Integer32"""
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


_NtWlanDot11FilterStatus_Type.__name__ = "Integer32"
_NtWlanDot11FilterStatus_Object = MibTableColumn
ntWlanDot11FilterStatus = _NtWlanDot11FilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 7, 1, 3),
    _NtWlanDot11FilterStatus_Type()
)
ntWlanDot11FilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanDot11FilterStatus.setStatus("current")
_NtWlanDot11TrapTable_Object = MibTable
ntWlanDot11TrapTable = _NtWlanDot11TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 9)
)
if mibBuilder.loadTexts:
    ntWlanDot11TrapTable.setStatus("current")
_NtWlanDot11TrapEntry_Object = MibTableRow
ntWlanDot11TrapEntry = _NtWlanDot11TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 9, 1)
)
ntWlanDot11TrapEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanDot11InterfaceIndex"),
)
if mibBuilder.loadTexts:
    ntWlanDot11TrapEntry.setStatus("current")


class _NtWlanDot11InterfaceIndex_Type(Integer32):
    """Custom type ntWlanDot11InterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtWlanDot11InterfaceIndex_Type.__name__ = "Integer32"
_NtWlanDot11InterfaceIndex_Object = MibTableColumn
ntWlanDot11InterfaceIndex = _NtWlanDot11InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 9, 1, 1),
    _NtWlanDot11InterfaceIndex_Type()
)
ntWlanDot11InterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanDot11InterfaceIndex.setStatus("current")
_NtWlanDot11AssociationStationAddress_Type = PhysAddress
_NtWlanDot11AssociationStationAddress_Object = MibTableColumn
ntWlanDot11AssociationStationAddress = _NtWlanDot11AssociationStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 9, 1, 2),
    _NtWlanDot11AssociationStationAddress_Type()
)
ntWlanDot11AssociationStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanDot11AssociationStationAddress.setStatus("current")
_NtWlanDot11DisassociationStationAddress_Type = PhysAddress
_NtWlanDot11DisassociationStationAddress_Object = MibTableColumn
ntWlanDot11DisassociationStationAddress = _NtWlanDot11DisassociationStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 9, 1, 3),
    _NtWlanDot11DisassociationStationAddress_Type()
)
ntWlanDot11DisassociationStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanDot11DisassociationStationAddress.setStatus("current")


class _NtWlanDot11AssociationMU_Type(Integer32):
    """Custom type ntWlanDot11AssociationMU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtWlanDot11AssociationMU_Type.__name__ = "Integer32"
_NtWlanDot11AssociationMU_Object = MibTableColumn
ntWlanDot11AssociationMU = _NtWlanDot11AssociationMU_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 7, 9, 1, 4),
    _NtWlanDot11AssociationMU_Type()
)
ntWlanDot11AssociationMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanDot11AssociationMU.setStatus("current")
_NtWlanApTraps_ObjectIdentity = ObjectIdentity
ntWlanApTraps = _NtWlanApTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 8)
)
_NtWlanApTraps0_ObjectIdentity = ObjectIdentity
ntWlanApTraps0 = _NtWlanApTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 8, 0)
)
_NtWlanApMuAssocTrapEnabled_Type = TruthValue
_NtWlanApMuAssocTrapEnabled_Object = MibScalar
ntWlanApMuAssocTrapEnabled = _NtWlanApMuAssocTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 8, 1),
    _NtWlanApMuAssocTrapEnabled_Type()
)
ntWlanApMuAssocTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApMuAssocTrapEnabled.setStatus("current")
_NtWlanApMuDisAssocTrapEnabled_Type = TruthValue
_NtWlanApMuDisAssocTrapEnabled_Object = MibScalar
ntWlanApMuDisAssocTrapEnabled = _NtWlanApMuDisAssocTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 8, 2),
    _NtWlanApMuDisAssocTrapEnabled_Type()
)
ntWlanApMuDisAssocTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApMuDisAssocTrapEnabled.setStatus("current")
_NtWlanApLID_ObjectIdentity = ObjectIdentity
ntWlanApLID = _NtWlanApLID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 9)
)
_NtWlanApLIDCheckEtherLinkEnabled_Type = TruthValue
_NtWlanApLIDCheckEtherLinkEnabled_Object = MibScalar
ntWlanApLIDCheckEtherLinkEnabled = _NtWlanApLIDCheckEtherLinkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 9, 1),
    _NtWlanApLIDCheckEtherLinkEnabled_Type()
)
ntWlanApLIDCheckEtherLinkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApLIDCheckEtherLinkEnabled.setStatus("current")
_NtWlanApLIDCheckIPLinkEnabled_Type = TruthValue
_NtWlanApLIDCheckIPLinkEnabled_Object = MibScalar
ntWlanApLIDCheckIPLinkEnabled = _NtWlanApLIDCheckIPLinkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 9, 2),
    _NtWlanApLIDCheckIPLinkEnabled_Type()
)
ntWlanApLIDCheckIPLinkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApLIDCheckIPLinkEnabled.setStatus("current")
_NtWlanApLIDCheckIpLinkAddress_Type = IpAddress
_NtWlanApLIDCheckIpLinkAddress_Object = MibScalar
ntWlanApLIDCheckIpLinkAddress = _NtWlanApLIDCheckIpLinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 9, 3),
    _NtWlanApLIDCheckIpLinkAddress_Type()
)
ntWlanApLIDCheckIpLinkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApLIDCheckIpLinkAddress.setStatus("current")
_NtWlanApRateSupport_ObjectIdentity = ObjectIdentity
ntWlanApRateSupport = _NtWlanApRateSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 10)
)
_NtWlanApRateSupportTable_Object = MibTable
ntWlanApRateSupportTable = _NtWlanApRateSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ntWlanApRateSupportTable.setStatus("current")
_NtWlanApRateSupportEntry_Object = MibTableRow
ntWlanApRateSupportEntry = _NtWlanApRateSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 10, 1, 1)
)
ntWlanApRateSupportEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanApRateSupportIfIndex"),
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanApRateSupportSpeed"),
)
if mibBuilder.loadTexts:
    ntWlanApRateSupportEntry.setStatus("current")
_NtWlanApRateSupportIfIndex_Type = InterfaceIndex
_NtWlanApRateSupportIfIndex_Object = MibTableColumn
ntWlanApRateSupportIfIndex = _NtWlanApRateSupportIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 10, 1, 1, 1),
    _NtWlanApRateSupportIfIndex_Type()
)
ntWlanApRateSupportIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanApRateSupportIfIndex.setStatus("current")
_NtWlanApRateSupportSpeed_Type = NtWlanApDataRate
_NtWlanApRateSupportSpeed_Object = MibTableColumn
ntWlanApRateSupportSpeed = _NtWlanApRateSupportSpeed_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 10, 1, 1, 2),
    _NtWlanApRateSupportSpeed_Type()
)
ntWlanApRateSupportSpeed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanApRateSupportSpeed.setStatus("current")


class _NtWlanApRateSupportLevel_Type(Integer32):
    """Custom type ntWlanApRateSupportLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("supported", 1),
          ("supportedBasic", 2))
    )


_NtWlanApRateSupportLevel_Type.__name__ = "Integer32"
_NtWlanApRateSupportLevel_Object = MibTableColumn
ntWlanApRateSupportLevel = _NtWlanApRateSupportLevel_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 10, 1, 1, 3),
    _NtWlanApRateSupportLevel_Type()
)
ntWlanApRateSupportLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApRateSupportLevel.setStatus("current")
_NtWlanApSecurity_ObjectIdentity = ObjectIdentity
ntWlanApSecurity = _NtWlanApSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11)
)
_NtWlanApSecurityTable_Object = MibTable
ntWlanApSecurityTable = _NtWlanApSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1)
)
if mibBuilder.loadTexts:
    ntWlanApSecurityTable.setStatus("current")
_NtWlanApSecurityEntry_Object = MibTableRow
ntWlanApSecurityEntry = _NtWlanApSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1)
)
ntWlanApSecurityEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanApSecurityIfIndex"),
)
if mibBuilder.loadTexts:
    ntWlanApSecurityEntry.setStatus("current")
_NtWlanApSecurityIfIndex_Type = InterfaceIndex
_NtWlanApSecurityIfIndex_Object = MibTableColumn
ntWlanApSecurityIfIndex = _NtWlanApSecurityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 1),
    _NtWlanApSecurityIfIndex_Type()
)
ntWlanApSecurityIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanApSecurityIfIndex.setStatus("current")
_NtWlanApSecurityEnabled_Type = TruthValue
_NtWlanApSecurityEnabled_Object = MibTableColumn
ntWlanApSecurityEnabled = _NtWlanApSecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 2),
    _NtWlanApSecurityEnabled_Type()
)
ntWlanApSecurityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityEnabled.setStatus("current")


class _NtWlanApSecurityWEPAuthType_Type(Integer32):
    """Custom type ntWlanApSecurityWEPAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 0),
          ("sharedKey", 1))
    )


_NtWlanApSecurityWEPAuthType_Type.__name__ = "Integer32"
_NtWlanApSecurityWEPAuthType_Object = MibTableColumn
ntWlanApSecurityWEPAuthType = _NtWlanApSecurityWEPAuthType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 3),
    _NtWlanApSecurityWEPAuthType_Type()
)
ntWlanApSecurityWEPAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityWEPAuthType.setStatus("current")


class _NtWlanApSecurityWEPKeyLength_Type(Integer32):
    """Custom type ntWlanApSecurityWEPKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wepKey128", 1),
          ("wepKey152", 2),
          ("wepKey64", 0))
    )


_NtWlanApSecurityWEPKeyLength_Type.__name__ = "Integer32"
_NtWlanApSecurityWEPKeyLength_Object = MibTableColumn
ntWlanApSecurityWEPKeyLength = _NtWlanApSecurityWEPKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 4),
    _NtWlanApSecurityWEPKeyLength_Type()
)
ntWlanApSecurityWEPKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityWEPKeyLength.setStatus("current")


class _NtWlanApSecurityWEPActiveKey_Type(Integer32):
    """Custom type ntWlanApSecurityWEPActiveKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NtWlanApSecurityWEPActiveKey_Type.__name__ = "Integer32"
_NtWlanApSecurityWEPActiveKey_Object = MibTableColumn
ntWlanApSecurityWEPActiveKey = _NtWlanApSecurityWEPActiveKey_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 5),
    _NtWlanApSecurityWEPActiveKey_Type()
)
ntWlanApSecurityWEPActiveKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityWEPActiveKey.setStatus("current")
_NtWlanApSecurityWEPKey1_Type = NtWlanApWEPKey
_NtWlanApSecurityWEPKey1_Object = MibTableColumn
ntWlanApSecurityWEPKey1 = _NtWlanApSecurityWEPKey1_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 6),
    _NtWlanApSecurityWEPKey1_Type()
)
ntWlanApSecurityWEPKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityWEPKey1.setStatus("current")
_NtWlanApSecurityWEPKey2_Type = NtWlanApWEPKey
_NtWlanApSecurityWEPKey2_Object = MibTableColumn
ntWlanApSecurityWEPKey2 = _NtWlanApSecurityWEPKey2_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 7),
    _NtWlanApSecurityWEPKey2_Type()
)
ntWlanApSecurityWEPKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityWEPKey2.setStatus("current")
_NtWlanApSecurityWEPKey3_Type = NtWlanApWEPKey
_NtWlanApSecurityWEPKey3_Object = MibTableColumn
ntWlanApSecurityWEPKey3 = _NtWlanApSecurityWEPKey3_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 8),
    _NtWlanApSecurityWEPKey3_Type()
)
ntWlanApSecurityWEPKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityWEPKey3.setStatus("current")
_NtWlanApSecurityWEPKey4_Type = NtWlanApWEPKey
_NtWlanApSecurityWEPKey4_Object = MibTableColumn
ntWlanApSecurityWEPKey4 = _NtWlanApSecurityWEPKey4_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 9),
    _NtWlanApSecurityWEPKey4_Type()
)
ntWlanApSecurityWEPKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityWEPKey4.setStatus("current")


class _NtWlanApSecurityWPASupport_Type(Integer32):
    """Custom type ntWlanApSecurityWPASupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("required", 2),
          ("supported", 1),
          ("wepOnly", 3))
    )


_NtWlanApSecurityWPASupport_Type.__name__ = "Integer32"
_NtWlanApSecurityWPASupport_Object = MibTableColumn
ntWlanApSecurityWPASupport = _NtWlanApSecurityWPASupport_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 10),
    _NtWlanApSecurityWPASupport_Type()
)
ntWlanApSecurityWPASupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityWPASupport.setStatus("current")


class _NtWlanApSecurityWPAMode_Type(Integer32):
    """Custom type ntWlanApSecurityWPAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("preSharedKey", 1))
    )


_NtWlanApSecurityWPAMode_Type.__name__ = "Integer32"
_NtWlanApSecurityWPAMode_Object = MibTableColumn
ntWlanApSecurityWPAMode = _NtWlanApSecurityWPAMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 11),
    _NtWlanApSecurityWPAMode_Type()
)
ntWlanApSecurityWPAMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityWPAMode.setStatus("current")


class _NtWlanApSecurityWPAPreSharedKey_Type(OctetString):
    """Custom type ntWlanApSecurityWPAPreSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )


_NtWlanApSecurityWPAPreSharedKey_Type.__name__ = "OctetString"
_NtWlanApSecurityWPAPreSharedKey_Object = MibTableColumn
ntWlanApSecurityWPAPreSharedKey = _NtWlanApSecurityWPAPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 12),
    _NtWlanApSecurityWPAPreSharedKey_Type()
)
ntWlanApSecurityWPAPreSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityWPAPreSharedKey.setStatus("current")


class _NtWlanApSecurityWPAMcastCypherMode_Type(Integer32):
    """Custom type ntWlanApSecurityWPAMcastCypherMode based on Integer32"""
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


_NtWlanApSecurityWPAMcastCypherMode_Type.__name__ = "Integer32"
_NtWlanApSecurityWPAMcastCypherMode_Object = MibTableColumn
ntWlanApSecurityWPAMcastCypherMode = _NtWlanApSecurityWPAMcastCypherMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 11, 1, 1, 13),
    _NtWlanApSecurityWPAMcastCypherMode_Type()
)
ntWlanApSecurityWPAMcastCypherMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApSecurityWPAMcastCypherMode.setStatus("current")
_NtWlanApQoS_ObjectIdentity = ObjectIdentity
ntWlanApQoS = _NtWlanApQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12)
)


class _NtWlanApQoSMode_Type(Integer32):
    """Custom type ntWlanApQoSMode based on Integer32"""
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
        *(("directPriorityMap", 4),
          ("etherDst", 2),
          ("etherSrc", 1),
          ("ethertype", 3),
          ("off", 0))
    )


_NtWlanApQoSMode_Type.__name__ = "Integer32"
_NtWlanApQoSMode_Object = MibScalar
ntWlanApQoSMode = _NtWlanApQoSMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12, 1),
    _NtWlanApQoSMode_Type()
)
ntWlanApQoSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApQoSMode.setStatus("current")
_NtWlanApQoSEtherTypeToQueueTable_Object = MibTable
ntWlanApQoSEtherTypeToQueueTable = _NtWlanApQoSEtherTypeToQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12, 2)
)
if mibBuilder.loadTexts:
    ntWlanApQoSEtherTypeToQueueTable.setStatus("current")
_NtWlanApQoSEtherTypeToQueueEntry_Object = MibTableRow
ntWlanApQoSEtherTypeToQueueEntry = _NtWlanApQoSEtherTypeToQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12, 2, 1)
)
ntWlanApQoSEtherTypeToQueueEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanApQoSEtherTypeToQueueIndex"),
)
if mibBuilder.loadTexts:
    ntWlanApQoSEtherTypeToQueueEntry.setStatus("current")


class _NtWlanApQoSEtherTypeToQueueIndex_Type(Integer32):
    """Custom type ntWlanApQoSEtherTypeToQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtWlanApQoSEtherTypeToQueueIndex_Type.__name__ = "Integer32"
_NtWlanApQoSEtherTypeToQueueIndex_Object = MibTableColumn
ntWlanApQoSEtherTypeToQueueIndex = _NtWlanApQoSEtherTypeToQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12, 2, 1, 1),
    _NtWlanApQoSEtherTypeToQueueIndex_Type()
)
ntWlanApQoSEtherTypeToQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanApQoSEtherTypeToQueueIndex.setStatus("current")


class _NtWlanApQoSEtherTypeToQueueNumber_Type(Integer32):
    """Custom type ntWlanApQoSEtherTypeToQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NtWlanApQoSEtherTypeToQueueNumber_Type.__name__ = "Integer32"
_NtWlanApQoSEtherTypeToQueueNumber_Object = MibTableColumn
ntWlanApQoSEtherTypeToQueueNumber = _NtWlanApQoSEtherTypeToQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12, 2, 1, 2),
    _NtWlanApQoSEtherTypeToQueueNumber_Type()
)
ntWlanApQoSEtherTypeToQueueNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApQoSEtherTypeToQueueNumber.setStatus("current")
_NtWlanApQoSEtherTypeToQueueRowStatus_Type = RowStatus
_NtWlanApQoSEtherTypeToQueueRowStatus_Object = MibTableColumn
ntWlanApQoSEtherTypeToQueueRowStatus = _NtWlanApQoSEtherTypeToQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12, 2, 1, 3),
    _NtWlanApQoSEtherTypeToQueueRowStatus_Type()
)
ntWlanApQoSEtherTypeToQueueRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApQoSEtherTypeToQueueRowStatus.setStatus("current")
_NtWlanApQoSMACToQueueTable_Object = MibTable
ntWlanApQoSMACToQueueTable = _NtWlanApQoSMACToQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12, 3)
)
if mibBuilder.loadTexts:
    ntWlanApQoSMACToQueueTable.setStatus("current")
_NtWlanApQoSMACToQueueEntry_Object = MibTableRow
ntWlanApQoSMACToQueueEntry = _NtWlanApQoSMACToQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12, 3, 1)
)
ntWlanApQoSMACToQueueEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanApQoSMACToQueueAddress"),
)
if mibBuilder.loadTexts:
    ntWlanApQoSMACToQueueEntry.setStatus("current")
_NtWlanApQoSMACToQueueAddress_Type = MacAddress
_NtWlanApQoSMACToQueueAddress_Object = MibTableColumn
ntWlanApQoSMACToQueueAddress = _NtWlanApQoSMACToQueueAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12, 3, 1, 1),
    _NtWlanApQoSMACToQueueAddress_Type()
)
ntWlanApQoSMACToQueueAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanApQoSMACToQueueAddress.setStatus("current")


class _NtWlanApQoSMACToQueueNumber_Type(Integer32):
    """Custom type ntWlanApQoSMACToQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NtWlanApQoSMACToQueueNumber_Type.__name__ = "Integer32"
_NtWlanApQoSMACToQueueNumber_Object = MibTableColumn
ntWlanApQoSMACToQueueNumber = _NtWlanApQoSMACToQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12, 3, 1, 2),
    _NtWlanApQoSMACToQueueNumber_Type()
)
ntWlanApQoSMACToQueueNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApQoSMACToQueueNumber.setStatus("current")
_NtWlanApQoSMACToQueueRowStatus_Type = RowStatus
_NtWlanApQoSMACToQueueRowStatus_Object = MibTableColumn
ntWlanApQoSMACToQueueRowStatus = _NtWlanApQoSMACToQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 12, 3, 1, 3),
    _NtWlanApQoSMACToQueueRowStatus_Type()
)
ntWlanApQoSMACToQueueRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApQoSMACToQueueRowStatus.setStatus("current")
_NtWlanApVlan_ObjectIdentity = ObjectIdentity
ntWlanApVlan = _NtWlanApVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 13)
)
_NtWlanApVlanEnabled_Type = TruthValue
_NtWlanApVlanEnabled_Object = MibScalar
ntWlanApVlanEnabled = _NtWlanApVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 13, 1),
    _NtWlanApVlanEnabled_Type()
)
ntWlanApVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApVlanEnabled.setStatus("current")
_NtWlanApVlanTable_Object = MibTable
ntWlanApVlanTable = _NtWlanApVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 13, 2)
)
if mibBuilder.loadTexts:
    ntWlanApVlanTable.setStatus("current")
_NtWlanApVlanEntry_Object = MibTableRow
ntWlanApVlanEntry = _NtWlanApVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 13, 2, 1)
)
ntWlanApVlanEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanApVlanIfIndex"),
)
if mibBuilder.loadTexts:
    ntWlanApVlanEntry.setStatus("current")
_NtWlanApVlanIfIndex_Type = InterfaceIndex
_NtWlanApVlanIfIndex_Object = MibTableColumn
ntWlanApVlanIfIndex = _NtWlanApVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 13, 2, 1, 1),
    _NtWlanApVlanIfIndex_Type()
)
ntWlanApVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanApVlanIfIndex.setStatus("current")


class _NtWlanApVlanDefaultVid_Type(Integer32):
    """Custom type ntWlanApVlanDefaultVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_NtWlanApVlanDefaultVid_Type.__name__ = "Integer32"
_NtWlanApVlanDefaultVid_Object = MibTableColumn
ntWlanApVlanDefaultVid = _NtWlanApVlanDefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 13, 2, 1, 2),
    _NtWlanApVlanDefaultVid_Type()
)
ntWlanApVlanDefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApVlanDefaultVid.setStatus("current")
_NtWlanApVlanMUMACToVidTable_Object = MibTable
ntWlanApVlanMUMACToVidTable = _NtWlanApVlanMUMACToVidTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 13, 3)
)
if mibBuilder.loadTexts:
    ntWlanApVlanMUMACToVidTable.setStatus("current")
_NtWlanApVlanMUMACToVidEntry_Object = MibTableRow
ntWlanApVlanMUMACToVidEntry = _NtWlanApVlanMUMACToVidEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 13, 3, 1)
)
ntWlanApVlanMUMACToVidEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanApVlanMUMACToVidAddress"),
)
if mibBuilder.loadTexts:
    ntWlanApVlanMUMACToVidEntry.setStatus("current")
_NtWlanApVlanMUMACToVidAddress_Type = MacAddress
_NtWlanApVlanMUMACToVidAddress_Object = MibTableColumn
ntWlanApVlanMUMACToVidAddress = _NtWlanApVlanMUMACToVidAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 13, 3, 1, 1),
    _NtWlanApVlanMUMACToVidAddress_Type()
)
ntWlanApVlanMUMACToVidAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanApVlanMUMACToVidAddress.setStatus("current")


class _NtWlanApVlanMUMACToVidNumber_Type(Integer32):
    """Custom type ntWlanApVlanMUMACToVidNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NtWlanApVlanMUMACToVidNumber_Type.__name__ = "Integer32"
_NtWlanApVlanMUMACToVidNumber_Object = MibTableColumn
ntWlanApVlanMUMACToVidNumber = _NtWlanApVlanMUMACToVidNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 13, 3, 1, 2),
    _NtWlanApVlanMUMACToVidNumber_Type()
)
ntWlanApVlanMUMACToVidNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntWlanApVlanMUMACToVidNumber.setStatus("current")
_NtWlanApStats_ObjectIdentity = ObjectIdentity
ntWlanApStats = _NtWlanApStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 14)
)
_NtWlanApMUStatsTable_Object = MibTable
ntWlanApMUStatsTable = _NtWlanApMUStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 14, 1)
)
if mibBuilder.loadTexts:
    ntWlanApMUStatsTable.setStatus("current")
_NtWlanApMUStatsEntry_Object = MibTableRow
ntWlanApMUStatsEntry = _NtWlanApMUStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 14, 1, 1)
)
ntWlanApMUStatsEntry.setIndexNames(
    (0, "NORTEL-WLAN-AP-MIB", "ntWlanApMUStatsMUAddress"),
)
if mibBuilder.loadTexts:
    ntWlanApMUStatsEntry.setStatus("current")
_NtWlanApMUStatsMUAddress_Type = MacAddress
_NtWlanApMUStatsMUAddress_Object = MibTableColumn
ntWlanApMUStatsMUAddress = _NtWlanApMUStatsMUAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 14, 1, 1, 1),
    _NtWlanApMUStatsMUAddress_Type()
)
ntWlanApMUStatsMUAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntWlanApMUStatsMUAddress.setStatus("current")
_NtWlanApMUStatsPacketsIn_Type = Counter32
_NtWlanApMUStatsPacketsIn_Object = MibTableColumn
ntWlanApMUStatsPacketsIn = _NtWlanApMUStatsPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 14, 1, 1, 2),
    _NtWlanApMUStatsPacketsIn_Type()
)
ntWlanApMUStatsPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanApMUStatsPacketsIn.setStatus("current")
_NtWlanApMUStatsPacketsOut_Type = Counter32
_NtWlanApMUStatsPacketsOut_Object = MibTableColumn
ntWlanApMUStatsPacketsOut = _NtWlanApMUStatsPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 14, 1, 1, 3),
    _NtWlanApMUStatsPacketsOut_Type()
)
ntWlanApMUStatsPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanApMUStatsPacketsOut.setStatus("current")
_NtWlanApMUStatsOctetsIn_Type = Counter32
_NtWlanApMUStatsOctetsIn_Object = MibTableColumn
ntWlanApMUStatsOctetsIn = _NtWlanApMUStatsOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 14, 1, 1, 4),
    _NtWlanApMUStatsOctetsIn_Type()
)
ntWlanApMUStatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanApMUStatsOctetsIn.setStatus("current")
_NtWlanApMUStatsOctetsOut_Type = Counter32
_NtWlanApMUStatsOctetsOut_Object = MibTableColumn
ntWlanApMUStatsOctetsOut = _NtWlanApMUStatsOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 14, 1, 1, 5),
    _NtWlanApMUStatsOctetsOut_Type()
)
ntWlanApMUStatsOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntWlanApMUStatsOctetsOut.setStatus("current")

# Managed Objects groups


# Notification objects

ntWlanApDot1xAuthenticationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 8, 0, 101)
)
ntWlanApDot1xAuthenticationFail.setObjects(
      *(("IF-MIB", "ifPhysAddress"),
        ("NORTEL-WLAN-AP-MIB", "ntWlanDot11AssociationStationAddress"))
)
if mibBuilder.loadTexts:
    ntWlanApDot1xAuthenticationFail.setStatus(
        "current"
    )

ntWlanApMuAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 8, 0, 111)
)
ntWlanApMuAssocTrap.setObjects(
      *(("IF-MIB", "ifPhysAddress"),
        ("NORTEL-WLAN-AP-MIB", "ntWlanDot11AssociationStationAddress"),
        ("NORTEL-WLAN-AP-MIB", "ntWlanDot11AssociationMU"))
)
if mibBuilder.loadTexts:
    ntWlanApMuAssocTrap.setStatus(
        "current"
    )

ntWlanApMuDisAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 8, 0, 112)
)
ntWlanApMuDisAssocTrap.setObjects(
      *(("IF-MIB", "ifPhysAddress"),
        ("NORTEL-WLAN-AP-MIB", "ntWlanDot11DisassociationStationAddress"),
        ("NORTEL-WLAN-AP-MIB", "ntWlanDot11AssociationMU"))
)
if mibBuilder.loadTexts:
    ntWlanApMuDisAssocTrap.setStatus(
        "current"
    )

ntWlanApMuWEPAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 8, 0, 113)
)
ntWlanApMuWEPAuthFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("NORTEL-WLAN-AP-MIB", "ntWlanDot11AssociationStationAddress"))
)
if mibBuilder.loadTexts:
    ntWlanApMuWEPAuthFail.setStatus(
        "current"
    )

ntWlanApMuWPAAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 11, 1, 8, 0, 114)
)
ntWlanApMuWPAAuthFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("NORTEL-WLAN-AP-MIB", "ntWlanDot11AssociationStationAddress"))
)
if mibBuilder.loadTexts:
    ntWlanApMuWPAAuthFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-WLAN-AP-MIB",
    **{"NtWlanApDataRate": NtWlanApDataRate,
       "NtWlanApWEPKey": NtWlanApWEPKey,
       "nortelWlanApMib": nortelWlanApMib,
       "ntWlanApSys": ntWlanApSys,
       "ntWlanSwHardwareVer": ntWlanSwHardwareVer,
       "ntWlanSwBootRomVer": ntWlanSwBootRomVer,
       "ntWlanSwOpCodeVer": ntWlanSwOpCodeVer,
       "ntWlanSwCountryCode": ntWlanSwCountryCode,
       "ntWlanSwNNDataFileVer": ntWlanSwNNDataFileVer,
       "ntWlanApLineMgnt": ntWlanApLineMgnt,
       "ntWlanLineTable": ntWlanLineTable,
       "ntWlanLineEntry": ntWlanLineEntry,
       "ntWlanLineIndex": ntWlanLineIndex,
       "ntWlanLineDataBits": ntWlanLineDataBits,
       "ntWlanLineParity": ntWlanLineParity,
       "ntWlanLineSpeed": ntWlanLineSpeed,
       "ntWlanLineStopBits": ntWlanLineStopBits,
       "ntWlanApPortMgnt": ntWlanApPortMgnt,
       "ntWlanPortTable": ntWlanPortTable,
       "ntWlanPortEntry": ntWlanPortEntry,
       "ntWlanPortIndex": ntWlanPortIndex,
       "ntWlanPortName": ntWlanPortName,
       "ntWlanPortType": ntWlanPortType,
       "ntWlanPortSpeedDpxCfg": ntWlanPortSpeedDpxCfg,
       "ntWlanPortFlowCtrlCfg": ntWlanPortFlowCtrlCfg,
       "ntWlanPortCapabilities": ntWlanPortCapabilities,
       "ntWlanPortAutonegotiation": ntWlanPortAutonegotiation,
       "ntWlanPortSpeedDpxStatus": ntWlanPortSpeedDpxStatus,
       "ntWlanPortFlowCtrlStatus": ntWlanPortFlowCtrlStatus,
       "ntWlanApFileTransferMgt": ntWlanApFileTransferMgt,
       "ntWlanTransferStart": ntWlanTransferStart,
       "ntWlanTransferType": ntWlanTransferType,
       "ntWlanFileType": ntWlanFileType,
       "ntWlanSrcFile": ntWlanSrcFile,
       "ntWlanDestFile": ntWlanDestFile,
       "ntWlanFileServer": ntWlanFileServer,
       "ntWlanUserName": ntWlanUserName,
       "ntWlanPassword": ntWlanPassword,
       "ntWlanFileTransferStatus": ntWlanFileTransferStatus,
       "ntWlanApResetMgt": ntWlanApResetMgt,
       "ntWlanRestartOpCodeFile": ntWlanRestartOpCodeFile,
       "ntWlanRestartControl": ntWlanRestartControl,
       "ntWlanApIpMgt": ntWlanApIpMgt,
       "ntWlanNetConfigIPAddress": ntWlanNetConfigIPAddress,
       "ntWlanNetConfigSubnetMask": ntWlanNetConfigSubnetMask,
       "ntWlanNetDefaultGateway": ntWlanNetDefaultGateway,
       "ntWlanIpHttpState": ntWlanIpHttpState,
       "ntWlanIpHttpPort": ntWlanIpHttpPort,
       "ntWlanApDot11": ntWlanApDot11,
       "ntWlanDot11Phy": ntWlanDot11Phy,
       "ntWlanDot11PhyOperationTable": ntWlanDot11PhyOperationTable,
       "ntWlanDot11PhyOperationEntry": ntWlanDot11PhyOperationEntry,
       "ntWlanDot11Index": ntWlanDot11Index,
       "ntWlanDot11TurboModeEnabled": ntWlanDot11TurboModeEnabled,
       "ntWlanDot11PreambleLength": ntWlanDot11PreambleLength,
       "ntWlanDot11dWorldModeEnabled": ntWlanDot11dWorldModeEnabled,
       "ntWlanDot11ClosedSystem": ntWlanDot11ClosedSystem,
       "ntWlanDot11AuthenticationEntry": ntWlanDot11AuthenticationEntry,
       "ntWlanDot118021xSupport": ntWlanDot118021xSupport,
       "ntWlanDot118021xRequired": ntWlanDot118021xRequired,
       "ntWlanDot118021xBcastKeyRefresh": ntWlanDot118021xBcastKeyRefresh,
       "ntWlanDot118021xSessKeyRefresh": ntWlanDot118021xSessKeyRefresh,
       "ntWlanDot118021xReAuthRefresh": ntWlanDot118021xReAuthRefresh,
       "ntWlanDot11AuthenticationServerTable": ntWlanDot11AuthenticationServerTable,
       "ntWlanDot11AuthenticationServerEntry": ntWlanDot11AuthenticationServerEntry,
       "ntWlanDot11ServerIndex": ntWlanDot11ServerIndex,
       "ntWlanDot11AuthenticationServer": ntWlanDot11AuthenticationServer,
       "ntWlanDot11AuthenticationPort": ntWlanDot11AuthenticationPort,
       "ntWlanDot11AuthenticationKey": ntWlanDot11AuthenticationKey,
       "ntWlanDot11AuthenticationRetransmit": ntWlanDot11AuthenticationRetransmit,
       "ntWlanDot11AuthenticationTimeout": ntWlanDot11AuthenticationTimeout,
       "ntWlanDot11SecondaryAuthServer": ntWlanDot11SecondaryAuthServer,
       "ntWlanDot11SecondaryAuthPort": ntWlanDot11SecondaryAuthPort,
       "ntWlanDot11SecondaryAuthKey": ntWlanDot11SecondaryAuthKey,
       "ntWlanDot11SecondaryAuthRetransmit": ntWlanDot11SecondaryAuthRetransmit,
       "ntWlanDot11SecondaryAuthTimeout": ntWlanDot11SecondaryAuthTimeout,
       "ntWlanDot11FilterTable": ntWlanDot11FilterTable,
       "ntWlanDot11FilterEntry": ntWlanDot11FilterEntry,
       "ntWlanDot11FilterIndex": ntWlanDot11FilterIndex,
       "ntWlanDot11FilterAddress": ntWlanDot11FilterAddress,
       "ntWlanDot11FilterStatus": ntWlanDot11FilterStatus,
       "ntWlanDot11TrapTable": ntWlanDot11TrapTable,
       "ntWlanDot11TrapEntry": ntWlanDot11TrapEntry,
       "ntWlanDot11InterfaceIndex": ntWlanDot11InterfaceIndex,
       "ntWlanDot11AssociationStationAddress": ntWlanDot11AssociationStationAddress,
       "ntWlanDot11DisassociationStationAddress": ntWlanDot11DisassociationStationAddress,
       "ntWlanDot11AssociationMU": ntWlanDot11AssociationMU,
       "ntWlanApTraps": ntWlanApTraps,
       "ntWlanApTraps0": ntWlanApTraps0,
       "ntWlanApDot1xAuthenticationFail": ntWlanApDot1xAuthenticationFail,
       "ntWlanApMuAssocTrap": ntWlanApMuAssocTrap,
       "ntWlanApMuDisAssocTrap": ntWlanApMuDisAssocTrap,
       "ntWlanApMuWEPAuthFail": ntWlanApMuWEPAuthFail,
       "ntWlanApMuWPAAuthFail": ntWlanApMuWPAAuthFail,
       "ntWlanApMuAssocTrapEnabled": ntWlanApMuAssocTrapEnabled,
       "ntWlanApMuDisAssocTrapEnabled": ntWlanApMuDisAssocTrapEnabled,
       "ntWlanApLID": ntWlanApLID,
       "ntWlanApLIDCheckEtherLinkEnabled": ntWlanApLIDCheckEtherLinkEnabled,
       "ntWlanApLIDCheckIPLinkEnabled": ntWlanApLIDCheckIPLinkEnabled,
       "ntWlanApLIDCheckIpLinkAddress": ntWlanApLIDCheckIpLinkAddress,
       "ntWlanApRateSupport": ntWlanApRateSupport,
       "ntWlanApRateSupportTable": ntWlanApRateSupportTable,
       "ntWlanApRateSupportEntry": ntWlanApRateSupportEntry,
       "ntWlanApRateSupportIfIndex": ntWlanApRateSupportIfIndex,
       "ntWlanApRateSupportSpeed": ntWlanApRateSupportSpeed,
       "ntWlanApRateSupportLevel": ntWlanApRateSupportLevel,
       "ntWlanApSecurity": ntWlanApSecurity,
       "ntWlanApSecurityTable": ntWlanApSecurityTable,
       "ntWlanApSecurityEntry": ntWlanApSecurityEntry,
       "ntWlanApSecurityIfIndex": ntWlanApSecurityIfIndex,
       "ntWlanApSecurityEnabled": ntWlanApSecurityEnabled,
       "ntWlanApSecurityWEPAuthType": ntWlanApSecurityWEPAuthType,
       "ntWlanApSecurityWEPKeyLength": ntWlanApSecurityWEPKeyLength,
       "ntWlanApSecurityWEPActiveKey": ntWlanApSecurityWEPActiveKey,
       "ntWlanApSecurityWEPKey1": ntWlanApSecurityWEPKey1,
       "ntWlanApSecurityWEPKey2": ntWlanApSecurityWEPKey2,
       "ntWlanApSecurityWEPKey3": ntWlanApSecurityWEPKey3,
       "ntWlanApSecurityWEPKey4": ntWlanApSecurityWEPKey4,
       "ntWlanApSecurityWPASupport": ntWlanApSecurityWPASupport,
       "ntWlanApSecurityWPAMode": ntWlanApSecurityWPAMode,
       "ntWlanApSecurityWPAPreSharedKey": ntWlanApSecurityWPAPreSharedKey,
       "ntWlanApSecurityWPAMcastCypherMode": ntWlanApSecurityWPAMcastCypherMode,
       "ntWlanApQoS": ntWlanApQoS,
       "ntWlanApQoSMode": ntWlanApQoSMode,
       "ntWlanApQoSEtherTypeToQueueTable": ntWlanApQoSEtherTypeToQueueTable,
       "ntWlanApQoSEtherTypeToQueueEntry": ntWlanApQoSEtherTypeToQueueEntry,
       "ntWlanApQoSEtherTypeToQueueIndex": ntWlanApQoSEtherTypeToQueueIndex,
       "ntWlanApQoSEtherTypeToQueueNumber": ntWlanApQoSEtherTypeToQueueNumber,
       "ntWlanApQoSEtherTypeToQueueRowStatus": ntWlanApQoSEtherTypeToQueueRowStatus,
       "ntWlanApQoSMACToQueueTable": ntWlanApQoSMACToQueueTable,
       "ntWlanApQoSMACToQueueEntry": ntWlanApQoSMACToQueueEntry,
       "ntWlanApQoSMACToQueueAddress": ntWlanApQoSMACToQueueAddress,
       "ntWlanApQoSMACToQueueNumber": ntWlanApQoSMACToQueueNumber,
       "ntWlanApQoSMACToQueueRowStatus": ntWlanApQoSMACToQueueRowStatus,
       "ntWlanApVlan": ntWlanApVlan,
       "ntWlanApVlanEnabled": ntWlanApVlanEnabled,
       "ntWlanApVlanTable": ntWlanApVlanTable,
       "ntWlanApVlanEntry": ntWlanApVlanEntry,
       "ntWlanApVlanIfIndex": ntWlanApVlanIfIndex,
       "ntWlanApVlanDefaultVid": ntWlanApVlanDefaultVid,
       "ntWlanApVlanMUMACToVidTable": ntWlanApVlanMUMACToVidTable,
       "ntWlanApVlanMUMACToVidEntry": ntWlanApVlanMUMACToVidEntry,
       "ntWlanApVlanMUMACToVidAddress": ntWlanApVlanMUMACToVidAddress,
       "ntWlanApVlanMUMACToVidNumber": ntWlanApVlanMUMACToVidNumber,
       "ntWlanApStats": ntWlanApStats,
       "ntWlanApMUStatsTable": ntWlanApMUStatsTable,
       "ntWlanApMUStatsEntry": ntWlanApMUStatsEntry,
       "ntWlanApMUStatsMUAddress": ntWlanApMUStatsMUAddress,
       "ntWlanApMUStatsPacketsIn": ntWlanApMUStatsPacketsIn,
       "ntWlanApMUStatsPacketsOut": ntWlanApMUStatsPacketsOut,
       "ntWlanApMUStatsOctetsIn": ntWlanApMUStatsOctetsIn,
       "ntWlanApMUStatsOctetsOut": ntWlanApMUStatsOctetsOut}
)

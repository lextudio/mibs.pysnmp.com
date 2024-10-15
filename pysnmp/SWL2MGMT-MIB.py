# SNMP MIB module (SWL2MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWL2MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:24 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

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

(privateMgmt,) = mibBuilder.importSymbols(
    "SWPRIMGMT-MIB",
    "privateMgmt")


# MODULE-IDENTITY

swL2MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )





class VlanIndex(Unsigned32):
    """Custom type VlanIndex based on Unsigned32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwL2DevMgmt_ObjectIdentity = ObjectIdentity
swL2DevMgmt = _SwL2DevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1)
)
_SwL2DevInfo_ObjectIdentity = ObjectIdentity
swL2DevInfo = _SwL2DevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 1)
)
_SwDevInfoSystemUpTime_Type = TimeTicks
_SwDevInfoSystemUpTime_Object = MibScalar
swDevInfoSystemUpTime = _SwDevInfoSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 1, 1),
    _SwDevInfoSystemUpTime_Type()
)
swDevInfoSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoSystemUpTime.setStatus("current")


class _SwDevInfoTotalNumOfPort_Type(Integer32):
    """Custom type swDevInfoTotalNumOfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwDevInfoTotalNumOfPort_Type.__name__ = "Integer32"
_SwDevInfoTotalNumOfPort_Object = MibScalar
swDevInfoTotalNumOfPort = _SwDevInfoTotalNumOfPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 1, 2),
    _SwDevInfoTotalNumOfPort_Type()
)
swDevInfoTotalNumOfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoTotalNumOfPort.setStatus("current")


class _SwDevInfoNumOfPortInUse_Type(Integer32):
    """Custom type swDevInfoNumOfPortInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwDevInfoNumOfPortInUse_Type.__name__ = "Integer32"
_SwDevInfoNumOfPortInUse_Object = MibScalar
swDevInfoNumOfPortInUse = _SwDevInfoNumOfPortInUse_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 1, 3),
    _SwDevInfoNumOfPortInUse_Type()
)
swDevInfoNumOfPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoNumOfPortInUse.setStatus("current")


class _SwDevInfoConsoleInUse_Type(Integer32):
    """Custom type swDevInfoConsoleInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in-use", 2),
          ("not-in-use", 3),
          ("other", 1))
    )


_SwDevInfoConsoleInUse_Type.__name__ = "Integer32"
_SwDevInfoConsoleInUse_Object = MibScalar
swDevInfoConsoleInUse = _SwDevInfoConsoleInUse_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 1, 4),
    _SwDevInfoConsoleInUse_Type()
)
swDevInfoConsoleInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoConsoleInUse.setStatus("current")


class _SwDevInfoFrontPanelLedStatus_Type(OctetString):
    """Custom type swDevInfoFrontPanelLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 324),
    )


_SwDevInfoFrontPanelLedStatus_Type.__name__ = "OctetString"
_SwDevInfoFrontPanelLedStatus_Object = MibScalar
swDevInfoFrontPanelLedStatus = _SwDevInfoFrontPanelLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 1, 5),
    _SwDevInfoFrontPanelLedStatus_Type()
)
swDevInfoFrontPanelLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoFrontPanelLedStatus.setStatus("current")


class _SwL2DevCtrlUpDownloadState_Type(Integer32):
    """Custom type swL2DevCtrlUpDownloadState based on Integer32"""
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
        *(("complete", 7),
          ("disk-full", 6),
          ("file-not-found", 5),
          ("in-process", 2),
          ("invalid-file", 3),
          ("other", 1),
          ("tftp-establish-fail", 9),
          ("time-out", 8),
          ("violation", 4))
    )


_SwL2DevCtrlUpDownloadState_Type.__name__ = "Integer32"
_SwL2DevCtrlUpDownloadState_Object = MibScalar
swL2DevCtrlUpDownloadState = _SwL2DevCtrlUpDownloadState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 1, 6),
    _SwL2DevCtrlUpDownloadState_Type()
)
swL2DevCtrlUpDownloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DevCtrlUpDownloadState.setStatus("current")


class _SwDevInfoSaveCfg_Type(Integer32):
    """Custom type swDevInfoSaveCfg based on Integer32"""
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
        *(("failed", 4),
          ("other", 1),
          ("proceeding", 2),
          ("ready", 3))
    )


_SwDevInfoSaveCfg_Type.__name__ = "Integer32"
_SwDevInfoSaveCfg_Object = MibScalar
swDevInfoSaveCfg = _SwDevInfoSaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 1, 7),
    _SwDevInfoSaveCfg_Type()
)
swDevInfoSaveCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoSaveCfg.setStatus("current")
_SwL2DevCtrl_ObjectIdentity = ObjectIdentity
swL2DevCtrl = _SwL2DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 2)
)


class _SwL2DevCtrlStpState_Type(Integer32):
    """Custom type swL2DevCtrlStpState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevCtrlStpState_Type.__name__ = "Integer32"
_SwL2DevCtrlStpState_Object = MibScalar
swL2DevCtrlStpState = _SwL2DevCtrlStpState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 2, 1),
    _SwL2DevCtrlStpState_Type()
)
swL2DevCtrlStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlStpState.setStatus("current")


class _SwL2DevCtrlIGMPSnooping_Type(Integer32):
    """Custom type swL2DevCtrlIGMPSnooping based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevCtrlIGMPSnooping_Type.__name__ = "Integer32"
_SwL2DevCtrlIGMPSnooping_Object = MibScalar
swL2DevCtrlIGMPSnooping = _SwL2DevCtrlIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 2, 2),
    _SwL2DevCtrlIGMPSnooping_Type()
)
swL2DevCtrlIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIGMPSnooping.setStatus("current")


class _SwL2DevCtrlRmonState_Type(Integer32):
    """Custom type swL2DevCtrlRmonState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevCtrlRmonState_Type.__name__ = "Integer32"
_SwL2DevCtrlRmonState_Object = MibScalar
swL2DevCtrlRmonState = _SwL2DevCtrlRmonState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 2, 3),
    _SwL2DevCtrlRmonState_Type()
)
swL2DevCtrlRmonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlRmonState.setStatus("current")


class _SwL2DevCtrlUpDownloadImageFileName_Type(DisplayString):
    """Custom type swL2DevCtrlUpDownloadImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwL2DevCtrlUpDownloadImageFileName_Type.__name__ = "DisplayString"
_SwL2DevCtrlUpDownloadImageFileName_Object = MibScalar
swL2DevCtrlUpDownloadImageFileName = _SwL2DevCtrlUpDownloadImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 2, 4),
    _SwL2DevCtrlUpDownloadImageFileName_Type()
)
swL2DevCtrlUpDownloadImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlUpDownloadImageFileName.setStatus("current")
_SwL2DevCtrlUpDownloadImageSourceAddr_Type = IpAddress
_SwL2DevCtrlUpDownloadImageSourceAddr_Object = MibScalar
swL2DevCtrlUpDownloadImageSourceAddr = _SwL2DevCtrlUpDownloadImageSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 2, 5),
    _SwL2DevCtrlUpDownloadImageSourceAddr_Type()
)
swL2DevCtrlUpDownloadImageSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlUpDownloadImageSourceAddr.setStatus("current")


class _SwL2DevCtrlUpDownloadImage_Type(Integer32):
    """Custom type swL2DevCtrlUpDownloadImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 3),
          ("other", 1),
          ("upload", 2))
    )


_SwL2DevCtrlUpDownloadImage_Type.__name__ = "Integer32"
_SwL2DevCtrlUpDownloadImage_Object = MibScalar
swL2DevCtrlUpDownloadImage = _SwL2DevCtrlUpDownloadImage_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 2, 6),
    _SwL2DevCtrlUpDownloadImage_Type()
)
swL2DevCtrlUpDownloadImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlUpDownloadImage.setStatus("current")


class _SwL2DevCtrlSaveCfg_Type(Integer32):
    """Custom type swL2DevCtrlSaveCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("normal", 1))
    )


_SwL2DevCtrlSaveCfg_Type.__name__ = "Integer32"
_SwL2DevCtrlSaveCfg_Object = MibScalar
swL2DevCtrlSaveCfg = _SwL2DevCtrlSaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 2, 7),
    _SwL2DevCtrlSaveCfg_Type()
)
swL2DevCtrlSaveCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlSaveCfg.setStatus("current")


class _SwL2DevCtrlCleanAllStatisticCounter_Type(Integer32):
    """Custom type swL2DevCtrlCleanAllStatisticCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("normal", 1))
    )


_SwL2DevCtrlCleanAllStatisticCounter_Type.__name__ = "Integer32"
_SwL2DevCtrlCleanAllStatisticCounter_Object = MibScalar
swL2DevCtrlCleanAllStatisticCounter = _SwL2DevCtrlCleanAllStatisticCounter_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 2, 8),
    _SwL2DevCtrlCleanAllStatisticCounter_Type()
)
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCleanAllStatisticCounter.setStatus("current")


class _SwL2DevCtrlStpForwardBPDU_Type(Integer32):
    """Custom type swL2DevCtrlStpForwardBPDU based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevCtrlStpForwardBPDU_Type.__name__ = "Integer32"
_SwL2DevCtrlStpForwardBPDU_Object = MibScalar
swL2DevCtrlStpForwardBPDU = _SwL2DevCtrlStpForwardBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 2, 9),
    _SwL2DevCtrlStpForwardBPDU_Type()
)
swL2DevCtrlStpForwardBPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlStpForwardBPDU.setStatus("current")
_SwL2DevAlarm_ObjectIdentity = ObjectIdentity
swL2DevAlarm = _SwL2DevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 3)
)


class _SwL2DevAlarmNewRoot_Type(Integer32):
    """Custom type swL2DevAlarmNewRoot based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevAlarmNewRoot_Type.__name__ = "Integer32"
_SwL2DevAlarmNewRoot_Object = MibScalar
swL2DevAlarmNewRoot = _SwL2DevAlarmNewRoot_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 3, 1),
    _SwL2DevAlarmNewRoot_Type()
)
swL2DevAlarmNewRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmNewRoot.setStatus("current")


class _SwL2DevAlarmTopologyChange_Type(Integer32):
    """Custom type swL2DevAlarmTopologyChange based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevAlarmTopologyChange_Type.__name__ = "Integer32"
_SwL2DevAlarmTopologyChange_Object = MibScalar
swL2DevAlarmTopologyChange = _SwL2DevAlarmTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 3, 2),
    _SwL2DevAlarmTopologyChange_Type()
)
swL2DevAlarmTopologyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmTopologyChange.setStatus("current")


class _SwL2DevAlarmLinkChange_Type(Integer32):
    """Custom type swL2DevAlarmLinkChange based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevAlarmLinkChange_Type.__name__ = "Integer32"
_SwL2DevAlarmLinkChange_Object = MibScalar
swL2DevAlarmLinkChange = _SwL2DevAlarmLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 1, 3, 3),
    _SwL2DevAlarmLinkChange_Type()
)
swL2DevAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmLinkChange.setStatus("current")
_SwL2UnitMgmt_ObjectIdentity = ObjectIdentity
swL2UnitMgmt = _SwL2UnitMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 2)
)
_SwL2UnitCtrl_ObjectIdentity = ObjectIdentity
swL2UnitCtrl = _SwL2UnitCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 2, 1)
)
_SwL2ModuleMgmt_ObjectIdentity = ObjectIdentity
swL2ModuleMgmt = _SwL2ModuleMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 3)
)
_SwL2PortMgmt_ObjectIdentity = ObjectIdentity
swL2PortMgmt = _SwL2PortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4)
)
_SwL2PortInfoTable_Object = MibTable
swL2PortInfoTable = _SwL2PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    swL2PortInfoTable.setStatus("current")
_SwL2PortInfoEntry_Object = MibTableRow
swL2PortInfoEntry = _SwL2PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 1, 1)
)
swL2PortInfoEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2PortInfoPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortInfoEntry.setStatus("current")


class _SwL2PortInfoPortIndex_Type(Integer32):
    """Custom type swL2PortInfoPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortInfoPortIndex_Type.__name__ = "Integer32"
_SwL2PortInfoPortIndex_Object = MibTableColumn
swL2PortInfoPortIndex = _SwL2PortInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 1, 1, 1),
    _SwL2PortInfoPortIndex_Type()
)
swL2PortInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoPortIndex.setStatus("current")


class _SwL2PortInfoUnitIndex_Type(Integer32):
    """Custom type swL2PortInfoUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortInfoUnitIndex_Type.__name__ = "Integer32"
_SwL2PortInfoUnitIndex_Object = MibTableColumn
swL2PortInfoUnitIndex = _SwL2PortInfoUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 1, 1, 2),
    _SwL2PortInfoUnitIndex_Type()
)
swL2PortInfoUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoUnitIndex.setStatus("current")


class _SwL2PortInfoType_Type(Integer32):
    """Custom type swL2PortInfoType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("portType-1000Base-GBIC-COPPER", 13),
          ("portType-1000Base-GBIC-CWDM", 10),
          ("portType-1000Base-GBIC-LX", 9),
          ("portType-1000Base-GBIC-OTHER", 14),
          ("portType-1000Base-GBIC-SX", 8),
          ("portType-1000Base-GBIC-XD", 11),
          ("portType-1000Base-GBIC-ZX", 12),
          ("portType-1000Base-LX", 7),
          ("portType-1000Base-SX", 6),
          ("portType-1000Base-T", 5),
          ("portType-100Base-FL", 4),
          ("portType-100Base-FX", 3),
          ("portType-100Base-TX", 2))
    )


_SwL2PortInfoType_Type.__name__ = "Integer32"
_SwL2PortInfoType_Object = MibTableColumn
swL2PortInfoType = _SwL2PortInfoType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 1, 1, 3),
    _SwL2PortInfoType_Type()
)
swL2PortInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoType.setStatus("current")


class _SwL2PortInfoLinkStatus_Type(Integer32):
    """Custom type swL2PortInfoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-fail", 3),
          ("link-pass", 2),
          ("other", 1))
    )


_SwL2PortInfoLinkStatus_Type.__name__ = "Integer32"
_SwL2PortInfoLinkStatus_Object = MibTableColumn
swL2PortInfoLinkStatus = _SwL2PortInfoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 1, 1, 4),
    _SwL2PortInfoLinkStatus_Type()
)
swL2PortInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoLinkStatus.setStatus("current")


class _SwL2PortInfoNwayStatus_Type(Integer32):
    """Custom type swL2PortInfoNwayStatus based on Integer32"""
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
        *(("auto", 2),
          ("full-100Mbps", 6),
          ("full-10Mbps", 4),
          ("full-1Gigabps", 8),
          ("half-100Mbps", 5),
          ("half-10Mbps", 3),
          ("half-1Gigabps", 7),
          ("other", 1))
    )


_SwL2PortInfoNwayStatus_Type.__name__ = "Integer32"
_SwL2PortInfoNwayStatus_Object = MibTableColumn
swL2PortInfoNwayStatus = _SwL2PortInfoNwayStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 1, 1, 5),
    _SwL2PortInfoNwayStatus_Type()
)
swL2PortInfoNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoNwayStatus.setStatus("current")
_SwL2PortCtrlTable_Object = MibTable
swL2PortCtrlTable = _SwL2PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    swL2PortCtrlTable.setStatus("current")
_SwL2PortCtrlEntry_Object = MibTableRow
swL2PortCtrlEntry = _SwL2PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 2, 1)
)
swL2PortCtrlEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2PortCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortCtrlEntry.setStatus("current")


class _SwL2PortCtrlPortIndex_Type(Integer32):
    """Custom type swL2PortCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortCtrlPortIndex_Type.__name__ = "Integer32"
_SwL2PortCtrlPortIndex_Object = MibTableColumn
swL2PortCtrlPortIndex = _SwL2PortCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 2, 1, 1),
    _SwL2PortCtrlPortIndex_Type()
)
swL2PortCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlPortIndex.setStatus("current")


class _SwL2PortCtrlUnitIndex_Type(Integer32):
    """Custom type swL2PortCtrlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortCtrlUnitIndex_Type.__name__ = "Integer32"
_SwL2PortCtrlUnitIndex_Object = MibTableColumn
swL2PortCtrlUnitIndex = _SwL2PortCtrlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 2, 1, 2),
    _SwL2PortCtrlUnitIndex_Type()
)
swL2PortCtrlUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlUnitIndex.setStatus("current")


class _SwL2PortCtrlAdminState_Type(Integer32):
    """Custom type swL2PortCtrlAdminState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2PortCtrlAdminState_Type.__name__ = "Integer32"
_SwL2PortCtrlAdminState_Object = MibTableColumn
swL2PortCtrlAdminState = _SwL2PortCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 2, 1, 3),
    _SwL2PortCtrlAdminState_Type()
)
swL2PortCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAdminState.setStatus("current")


class _SwL2PortCtrlNwayState_Type(Integer32):
    """Custom type swL2PortCtrlNwayState based on Integer32"""
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
        *(("nway-disabled-100Mbps-Full", 6),
          ("nway-disabled-100Mbps-Half", 5),
          ("nway-disabled-10Mbps-Full", 4),
          ("nway-disabled-10Mbps-Half", 3),
          ("nway-disabled-1Gigabps-Full", 7),
          ("nway-enabled", 2),
          ("other", 1))
    )


_SwL2PortCtrlNwayState_Type.__name__ = "Integer32"
_SwL2PortCtrlNwayState_Object = MibTableColumn
swL2PortCtrlNwayState = _SwL2PortCtrlNwayState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 2, 1, 4),
    _SwL2PortCtrlNwayState_Type()
)
swL2PortCtrlNwayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlNwayState.setStatus("current")


class _SwL2PortCtrlFlowCtrlState_Type(Integer32):
    """Custom type swL2PortCtrlFlowCtrlState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2PortCtrlFlowCtrlState_Type.__name__ = "Integer32"
_SwL2PortCtrlFlowCtrlState_Object = MibTableColumn
swL2PortCtrlFlowCtrlState = _SwL2PortCtrlFlowCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 2, 1, 5),
    _SwL2PortCtrlFlowCtrlState_Type()
)
swL2PortCtrlFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlFlowCtrlState.setStatus("current")


class _SwL2PortCtrlAddressLearningState_Type(Integer32):
    """Custom type swL2PortCtrlAddressLearningState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2PortCtrlAddressLearningState_Type.__name__ = "Integer32"
_SwL2PortCtrlAddressLearningState_Object = MibTableColumn
swL2PortCtrlAddressLearningState = _SwL2PortCtrlAddressLearningState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 2, 1, 6),
    _SwL2PortCtrlAddressLearningState_Type()
)
swL2PortCtrlAddressLearningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAddressLearningState.setStatus("current")
_SwL2PortUtilTable_Object = MibTable
swL2PortUtilTable = _SwL2PortUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    swL2PortUtilTable.setStatus("current")
_SwL2PortUtilEntry_Object = MibTableRow
swL2PortUtilEntry = _SwL2PortUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 3, 1)
)
swL2PortUtilEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2PortUtilPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortUtilEntry.setStatus("current")


class _SwL2PortUtilPortIndex_Type(Integer32):
    """Custom type swL2PortUtilPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortUtilPortIndex_Type.__name__ = "Integer32"
_SwL2PortUtilPortIndex_Object = MibTableColumn
swL2PortUtilPortIndex = _SwL2PortUtilPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 3, 1, 1),
    _SwL2PortUtilPortIndex_Type()
)
swL2PortUtilPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortUtilPortIndex.setStatus("current")
_SwL2PortUtilTxSec_Type = Gauge32
_SwL2PortUtilTxSec_Object = MibTableColumn
swL2PortUtilTxSec = _SwL2PortUtilTxSec_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 3, 1, 2),
    _SwL2PortUtilTxSec_Type()
)
swL2PortUtilTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortUtilTxSec.setStatus("current")
_SwL2PortUtilRxSec_Type = Gauge32
_SwL2PortUtilRxSec_Object = MibTableColumn
swL2PortUtilRxSec = _SwL2PortUtilRxSec_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 3, 1, 3),
    _SwL2PortUtilRxSec_Type()
)
swL2PortUtilRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortUtilRxSec.setStatus("current")


class _SwL2PortUtilUtilization_Type(Integer32):
    """Custom type swL2PortUtilUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwL2PortUtilUtilization_Type.__name__ = "Integer32"
_SwL2PortUtilUtilization_Object = MibTableColumn
swL2PortUtilUtilization = _SwL2PortUtilUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 4, 3, 1, 4),
    _SwL2PortUtilUtilization_Type()
)
swL2PortUtilUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortUtilUtilization.setStatus("current")
_SwL2FilterMgmt_ObjectIdentity = ObjectIdentity
swL2FilterMgmt = _SwL2FilterMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 6)
)
_SwL2FilterAddrConfig_ObjectIdentity = ObjectIdentity
swL2FilterAddrConfig = _SwL2FilterAddrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 6, 1)
)


class _SwL2FilterAddrMaxSupportedEntries_Type(Integer32):
    """Custom type swL2FilterAddrMaxSupportedEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2FilterAddrMaxSupportedEntries_Type.__name__ = "Integer32"
_SwL2FilterAddrMaxSupportedEntries_Object = MibScalar
swL2FilterAddrMaxSupportedEntries = _SwL2FilterAddrMaxSupportedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 6, 1, 1),
    _SwL2FilterAddrMaxSupportedEntries_Type()
)
swL2FilterAddrMaxSupportedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2FilterAddrMaxSupportedEntries.setStatus("current")


class _SwL2FilterAddrCurrentTotalEntries_Type(Integer32):
    """Custom type swL2FilterAddrCurrentTotalEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2FilterAddrCurrentTotalEntries_Type.__name__ = "Integer32"
_SwL2FilterAddrCurrentTotalEntries_Object = MibScalar
swL2FilterAddrCurrentTotalEntries = _SwL2FilterAddrCurrentTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 6, 1, 2),
    _SwL2FilterAddrCurrentTotalEntries_Type()
)
swL2FilterAddrCurrentTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2FilterAddrCurrentTotalEntries.setStatus("current")
_SwL2FilterAddrCtrlTable_Object = MibTable
swL2FilterAddrCtrlTable = _SwL2FilterAddrCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 6, 1, 3)
)
if mibBuilder.loadTexts:
    swL2FilterAddrCtrlTable.setStatus("current")
_SwL2FilterAddrCtrlEntry_Object = MibTableRow
swL2FilterAddrCtrlEntry = _SwL2FilterAddrCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 6, 1, 3, 1)
)
swL2FilterAddrCtrlEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2FilterAddrMacIndex"),
)
if mibBuilder.loadTexts:
    swL2FilterAddrCtrlEntry.setStatus("current")
_SwL2FilterAddrMacIndex_Type = MacAddress
_SwL2FilterAddrMacIndex_Object = MibTableColumn
swL2FilterAddrMacIndex = _SwL2FilterAddrMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 6, 1, 3, 1, 1),
    _SwL2FilterAddrMacIndex_Type()
)
swL2FilterAddrMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2FilterAddrMacIndex.setStatus("current")


class _SwL2FilterAddrState_Type(Integer32):
    """Custom type swL2FilterAddrState based on Integer32"""
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
        *(("dst-addr", 2),
          ("dst-src-addr", 4),
          ("invalid", 5),
          ("other", 1),
          ("src-addr", 3))
    )


_SwL2FilterAddrState_Type.__name__ = "Integer32"
_SwL2FilterAddrState_Object = MibTableColumn
swL2FilterAddrState = _SwL2FilterAddrState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 6, 1, 3, 1, 2),
    _SwL2FilterAddrState_Type()
)
swL2FilterAddrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2FilterAddrState.setStatus("current")
_SwL2VlanMgmt_ObjectIdentity = ObjectIdentity
swL2VlanMgmt = _SwL2VlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7)
)
_SwL2StaticVlanTable_Object = MibTable
swL2StaticVlanTable = _SwL2StaticVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    swL2StaticVlanTable.setStatus("current")
_SwL2StaticVlanEntry_Object = MibTableRow
swL2StaticVlanEntry = _SwL2StaticVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1)
)
swL2StaticVlanEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2StaticVlanIndex"),
)
if mibBuilder.loadTexts:
    swL2StaticVlanEntry.setStatus("current")


class _SwL2StaticVlanIndex_Type(Integer32):
    """Custom type swL2StaticVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2StaticVlanIndex_Type.__name__ = "Integer32"
_SwL2StaticVlanIndex_Object = MibTableColumn
swL2StaticVlanIndex = _SwL2StaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 1),
    _SwL2StaticVlanIndex_Type()
)
swL2StaticVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StaticVlanIndex.setStatus("current")


class _SwL2StaticVlanName_Type(DisplayString):
    """Custom type swL2StaticVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwL2StaticVlanName_Type.__name__ = "DisplayString"
_SwL2StaticVlanName_Object = MibTableColumn
swL2StaticVlanName = _SwL2StaticVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 2),
    _SwL2StaticVlanName_Type()
)
swL2StaticVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanName.setStatus("current")


class _SwL2StaticVlanType_Type(Integer32):
    """Custom type swL2StaticVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byIpSubnet", 2),
          ("byProtocolId", 3),
          ("byport", 1))
    )


_SwL2StaticVlanType_Type.__name__ = "Integer32"
_SwL2StaticVlanType_Object = MibTableColumn
swL2StaticVlanType = _SwL2StaticVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 3),
    _SwL2StaticVlanType_Type()
)
swL2StaticVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanType.setStatus("current")


class _SwL2StaticVlanProtocolId_Type(Integer32):
    """Custom type swL2StaticVlanProtocolId based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("apltkEther2Snap", 7),
          ("arpEther2", 17),
          ("decEther2", 8),
          ("decOtherEther2", 9),
          ("ipEther2", 1),
          ("ipv6Ether2", 15),
          ("ipx802dot2", 4),
          ("ipx802dot3", 3),
          ("ipxEther2", 6),
          ("ipxSnap", 5),
          ("netBios", 12),
          ("none", 0),
          ("rarpEther2", 2),
          ("sna802dot2", 10),
          ("snaEther2", 11),
          ("userDefined", 16),
          ("vinesEther2", 14),
          ("xnsEther2", 13))
    )


_SwL2StaticVlanProtocolId_Type.__name__ = "Integer32"
_SwL2StaticVlanProtocolId_Object = MibTableColumn
swL2StaticVlanProtocolId = _SwL2StaticVlanProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 4),
    _SwL2StaticVlanProtocolId_Type()
)
swL2StaticVlanProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanProtocolId.setStatus("current")
_SwL2StaticVlanIpSubnetAddr_Type = IpAddress
_SwL2StaticVlanIpSubnetAddr_Object = MibTableColumn
swL2StaticVlanIpSubnetAddr = _SwL2StaticVlanIpSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 5),
    _SwL2StaticVlanIpSubnetAddr_Type()
)
swL2StaticVlanIpSubnetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanIpSubnetAddr.setStatus("current")
_SwL2StaticVlanIpSubnetMask_Type = IpAddress
_SwL2StaticVlanIpSubnetMask_Object = MibTableColumn
swL2StaticVlanIpSubnetMask = _SwL2StaticVlanIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 6),
    _SwL2StaticVlanIpSubnetMask_Type()
)
swL2StaticVlanIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanIpSubnetMask.setStatus("current")


class _SwL2StaticVlanUserDefinedPid_Type(OctetString):
    """Custom type swL2StaticVlanUserDefinedPid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_SwL2StaticVlanUserDefinedPid_Type.__name__ = "OctetString"
_SwL2StaticVlanUserDefinedPid_Object = MibTableColumn
swL2StaticVlanUserDefinedPid = _SwL2StaticVlanUserDefinedPid_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 7),
    _SwL2StaticVlanUserDefinedPid_Type()
)
swL2StaticVlanUserDefinedPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanUserDefinedPid.setStatus("current")


class _SwL2StaticVlanEncap_Type(Integer32):
    """Custom type swL2StaticVlanEncap based on Integer32"""
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
        *(("all", 1),
          ("ethernet2", 2),
          ("llc", 3),
          ("snap", 4),
          ("un-used", 5))
    )


_SwL2StaticVlanEncap_Type.__name__ = "Integer32"
_SwL2StaticVlanEncap_Object = MibTableColumn
swL2StaticVlanEncap = _SwL2StaticVlanEncap_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 8),
    _SwL2StaticVlanEncap_Type()
)
swL2StaticVlanEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanEncap.setStatus("current")


class _SwL2StaticVlanUserPriority_Type(Integer32):
    """Custom type swL2StaticVlanUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(7, 7),
    )


_SwL2StaticVlanUserPriority_Type.__name__ = "Integer32"
_SwL2StaticVlanUserPriority_Object = MibTableColumn
swL2StaticVlanUserPriority = _SwL2StaticVlanUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 9),
    _SwL2StaticVlanUserPriority_Type()
)
swL2StaticVlanUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanUserPriority.setStatus("current")
_SwL2StaticVlanEgressPorts_Type = PortList
_SwL2StaticVlanEgressPorts_Object = MibTableColumn
swL2StaticVlanEgressPorts = _SwL2StaticVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 10),
    _SwL2StaticVlanEgressPorts_Type()
)
swL2StaticVlanEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanEgressPorts.setStatus("current")
_SwL2StaticVlanUntaggedPorts_Type = PortList
_SwL2StaticVlanUntaggedPorts_Object = MibTableColumn
swL2StaticVlanUntaggedPorts = _SwL2StaticVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 11),
    _SwL2StaticVlanUntaggedPorts_Type()
)
swL2StaticVlanUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanUntaggedPorts.setStatus("current")
_SwL2StaticVlanStatus_Type = RowStatus
_SwL2StaticVlanStatus_Object = MibTableColumn
swL2StaticVlanStatus = _SwL2StaticVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 12),
    _SwL2StaticVlanStatus_Type()
)
swL2StaticVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanStatus.setStatus("current")


class _SwL2StaticVlanIpSubnetArpClassId_Type(Integer32):
    """Custom type swL2StaticVlanIpSubnetArpClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SwL2StaticVlanIpSubnetArpClassId_Type.__name__ = "Integer32"
_SwL2StaticVlanIpSubnetArpClassId_Object = MibTableColumn
swL2StaticVlanIpSubnetArpClassId = _SwL2StaticVlanIpSubnetArpClassId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 1, 1, 13),
    _SwL2StaticVlanIpSubnetArpClassId_Type()
)
swL2StaticVlanIpSubnetArpClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StaticVlanIpSubnetArpClassId.setStatus("current")
_SwL2VlanPortTable_Object = MibTable
swL2VlanPortTable = _SwL2VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    swL2VlanPortTable.setStatus("current")
_SwL2VlanPortEntry_Object = MibTableRow
swL2VlanPortEntry = _SwL2VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 2, 1)
)
swL2VlanPortEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2VlanPortIndex"),
)
if mibBuilder.loadTexts:
    swL2VlanPortEntry.setStatus("current")
_SwL2VlanPortIndex_Type = Integer32
_SwL2VlanPortIndex_Object = MibTableColumn
swL2VlanPortIndex = _SwL2VlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 2, 1, 1),
    _SwL2VlanPortIndex_Type()
)
swL2VlanPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanPortIndex.setStatus("current")
_SwL2VlanPortPvid_Type = Integer32
_SwL2VlanPortPvid_Object = MibTableColumn
swL2VlanPortPvid = _SwL2VlanPortPvid_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 2, 1, 2),
    _SwL2VlanPortPvid_Type()
)
swL2VlanPortPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanPortPvid.setStatus("current")


class _SwL2VlanPortIngressChecking_Type(Integer32):
    """Custom type swL2VlanPortIngressChecking based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2VlanPortIngressChecking_Type.__name__ = "Integer32"
_SwL2VlanPortIngressChecking_Object = MibTableColumn
swL2VlanPortIngressChecking = _SwL2VlanPortIngressChecking_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 7, 2, 1, 3),
    _SwL2VlanPortIngressChecking_Type()
)
swL2VlanPortIngressChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2VlanPortIngressChecking.setStatus("current")
_SwL2TrunkMgmt_ObjectIdentity = ObjectIdentity
swL2TrunkMgmt = _SwL2TrunkMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8)
)


class _SwL2TrunkMaxSupportedEntries_Type(Integer32):
    """Custom type swL2TrunkMaxSupportedEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrunkMaxSupportedEntries_Type.__name__ = "Integer32"
_SwL2TrunkMaxSupportedEntries_Object = MibScalar
swL2TrunkMaxSupportedEntries = _SwL2TrunkMaxSupportedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 1),
    _SwL2TrunkMaxSupportedEntries_Type()
)
swL2TrunkMaxSupportedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkMaxSupportedEntries.setStatus("current")


class _SwL2TrunkCurrentNumEntries_Type(Integer32):
    """Custom type swL2TrunkCurrentNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrunkCurrentNumEntries_Type.__name__ = "Integer32"
_SwL2TrunkCurrentNumEntries_Object = MibScalar
swL2TrunkCurrentNumEntries = _SwL2TrunkCurrentNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 2),
    _SwL2TrunkCurrentNumEntries_Type()
)
swL2TrunkCurrentNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkCurrentNumEntries.setStatus("current")
_SwL2TrunkCtrlTable_Object = MibTable
swL2TrunkCtrlTable = _SwL2TrunkCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    swL2TrunkCtrlTable.setStatus("current")
_SwL2TrunkCtrlEntry_Object = MibTableRow
swL2TrunkCtrlEntry = _SwL2TrunkCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 3, 1)
)
swL2TrunkCtrlEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2TrunkIndex"),
)
if mibBuilder.loadTexts:
    swL2TrunkCtrlEntry.setStatus("current")


class _SwL2TrunkIndex_Type(Integer32):
    """Custom type swL2TrunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrunkIndex_Type.__name__ = "Integer32"
_SwL2TrunkIndex_Object = MibTableColumn
swL2TrunkIndex = _SwL2TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 3, 1, 1),
    _SwL2TrunkIndex_Type()
)
swL2TrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkIndex.setStatus("current")


class _SwL2TrunkName_Type(DisplayString):
    """Custom type swL2TrunkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwL2TrunkName_Type.__name__ = "DisplayString"
_SwL2TrunkName_Object = MibTableColumn
swL2TrunkName = _SwL2TrunkName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 3, 1, 2),
    _SwL2TrunkName_Type()
)
swL2TrunkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkName.setStatus("current")


class _SwL2TrunkMasterPort_Type(Integer32):
    """Custom type swL2TrunkMasterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2TrunkMasterPort_Type.__name__ = "Integer32"
_SwL2TrunkMasterPort_Object = MibTableColumn
swL2TrunkMasterPort = _SwL2TrunkMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 3, 1, 3),
    _SwL2TrunkMasterPort_Type()
)
swL2TrunkMasterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkMasterPort.setStatus("current")
_SwL2TrunkMember_Type = PortList
_SwL2TrunkMember_Object = MibTableColumn
swL2TrunkMember = _SwL2TrunkMember_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 3, 1, 4),
    _SwL2TrunkMember_Type()
)
swL2TrunkMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkMember.setStatus("current")


class _SwL2TrunkFloodingPort_Type(Integer32):
    """Custom type swL2TrunkFloodingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2TrunkFloodingPort_Type.__name__ = "Integer32"
_SwL2TrunkFloodingPort_Object = MibTableColumn
swL2TrunkFloodingPort = _SwL2TrunkFloodingPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 3, 1, 5),
    _SwL2TrunkFloodingPort_Type()
)
swL2TrunkFloodingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkFloodingPort.setStatus("current")


class _SwL2TrunkState_Type(Integer32):
    """Custom type swL2TrunkState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid", 4),
          ("other", 1))
    )


_SwL2TrunkState_Type.__name__ = "Integer32"
_SwL2TrunkState_Object = MibTableColumn
swL2TrunkState = _SwL2TrunkState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 3, 1, 6),
    _SwL2TrunkState_Type()
)
swL2TrunkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkState.setStatus("current")


class _SwL2TrunkBPDU8600InterState_Type(Integer32):
    """Custom type swL2TrunkBPDU8600InterState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2TrunkBPDU8600InterState_Type.__name__ = "Integer32"
_SwL2TrunkBPDU8600InterState_Object = MibTableColumn
swL2TrunkBPDU8600InterState = _SwL2TrunkBPDU8600InterState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 3, 1, 7),
    _SwL2TrunkBPDU8600InterState_Type()
)
swL2TrunkBPDU8600InterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkBPDU8600InterState.setStatus("current")


class _SwL2TrunkAlgorithm_Type(Integer32):
    """Custom type swL2TrunkAlgorithm based on Integer32"""
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
        *(("ip-destination", 6),
          ("ip-source", 5),
          ("ip-source-dest", 7),
          ("mac-destination", 3),
          ("mac-source", 2),
          ("mac-source-dest", 4),
          ("other", 1))
    )


_SwL2TrunkAlgorithm_Type.__name__ = "Integer32"
_SwL2TrunkAlgorithm_Object = MibScalar
swL2TrunkAlgorithm = _SwL2TrunkAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 8, 4),
    _SwL2TrunkAlgorithm_Type()
)
swL2TrunkAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkAlgorithm.setStatus("current")
_SwL2MirrorMgmt_ObjectIdentity = ObjectIdentity
swL2MirrorMgmt = _SwL2MirrorMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 9)
)


class _SwL2MirrorLogicTargetPort_Type(Integer32):
    """Custom type swL2MirrorLogicTargetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2MirrorLogicTargetPort_Type.__name__ = "Integer32"
_SwL2MirrorLogicTargetPort_Object = MibScalar
swL2MirrorLogicTargetPort = _SwL2MirrorLogicTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 9, 1),
    _SwL2MirrorLogicTargetPort_Type()
)
swL2MirrorLogicTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorLogicTargetPort.setStatus("current")
_SwL2MirrorPortSourceIngress_Type = PortList
_SwL2MirrorPortSourceIngress_Object = MibScalar
swL2MirrorPortSourceIngress = _SwL2MirrorPortSourceIngress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 9, 2),
    _SwL2MirrorPortSourceIngress_Type()
)
swL2MirrorPortSourceIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortSourceIngress.setStatus("current")
_SwL2MirrorPortSourceEgress_Type = PortList
_SwL2MirrorPortSourceEgress_Object = MibScalar
swL2MirrorPortSourceEgress = _SwL2MirrorPortSourceEgress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 9, 3),
    _SwL2MirrorPortSourceEgress_Type()
)
swL2MirrorPortSourceEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortSourceEgress.setStatus("current")


class _SwL2MirrorPortState_Type(Integer32):
    """Custom type swL2MirrorPortState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2MirrorPortState_Type.__name__ = "Integer32"
_SwL2MirrorPortState_Object = MibScalar
swL2MirrorPortState = _SwL2MirrorPortState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 9, 4),
    _SwL2MirrorPortState_Type()
)
swL2MirrorPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortState.setStatus("current")
_SwL2IGMPMgmt_ObjectIdentity = ObjectIdentity
swL2IGMPMgmt = _SwL2IGMPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10)
)


class _SwL2IGMPMaxSupportedVlans_Type(Integer32):
    """Custom type swL2IGMPMaxSupportedVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPMaxSupportedVlans_Type.__name__ = "Integer32"
_SwL2IGMPMaxSupportedVlans_Object = MibScalar
swL2IGMPMaxSupportedVlans = _SwL2IGMPMaxSupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 1),
    _SwL2IGMPMaxSupportedVlans_Type()
)
swL2IGMPMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMaxSupportedVlans.setStatus("current")


class _SwL2IGMPMaxIpGroupNumPerVlan_Type(Integer32):
    """Custom type swL2IGMPMaxIpGroupNumPerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPMaxIpGroupNumPerVlan_Type.__name__ = "Integer32"
_SwL2IGMPMaxIpGroupNumPerVlan_Object = MibScalar
swL2IGMPMaxIpGroupNumPerVlan = _SwL2IGMPMaxIpGroupNumPerVlan_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 2),
    _SwL2IGMPMaxIpGroupNumPerVlan_Type()
)
swL2IGMPMaxIpGroupNumPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMaxIpGroupNumPerVlan.setStatus("current")
_SwL2IGMPCtrlTable_Object = MibTable
swL2IGMPCtrlTable = _SwL2IGMPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3)
)
if mibBuilder.loadTexts:
    swL2IGMPCtrlTable.setStatus("current")
_SwL2IGMPCtrlEntry_Object = MibTableRow
swL2IGMPCtrlEntry = _SwL2IGMPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1)
)
swL2IGMPCtrlEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2IGMPCtrlVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPCtrlEntry.setStatus("current")


class _SwL2IGMPCtrlVid_Type(Integer32):
    """Custom type swL2IGMPCtrlVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPCtrlVid_Type.__name__ = "Integer32"
_SwL2IGMPCtrlVid_Object = MibTableColumn
swL2IGMPCtrlVid = _SwL2IGMPCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1, 1),
    _SwL2IGMPCtrlVid_Type()
)
swL2IGMPCtrlVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPCtrlVid.setStatus("current")


class _SwL2IGMPQueryInterval_Type(Integer32):
    """Custom type swL2IGMPQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2IGMPQueryInterval_Type.__name__ = "Integer32"
_SwL2IGMPQueryInterval_Object = MibTableColumn
swL2IGMPQueryInterval = _SwL2IGMPQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1, 2),
    _SwL2IGMPQueryInterval_Type()
)
swL2IGMPQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPQueryInterval.setStatus("current")


class _SwL2IGMPMaxResponseTime_Type(Integer32):
    """Custom type swL2IGMPMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_SwL2IGMPMaxResponseTime_Type.__name__ = "Integer32"
_SwL2IGMPMaxResponseTime_Object = MibTableColumn
swL2IGMPMaxResponseTime = _SwL2IGMPMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1, 3),
    _SwL2IGMPMaxResponseTime_Type()
)
swL2IGMPMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMaxResponseTime.setStatus("current")


class _SwL2IGMPRobustness_Type(Integer32):
    """Custom type swL2IGMPRobustness based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2IGMPRobustness_Type.__name__ = "Integer32"
_SwL2IGMPRobustness_Object = MibTableColumn
swL2IGMPRobustness = _SwL2IGMPRobustness_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1, 4),
    _SwL2IGMPRobustness_Type()
)
swL2IGMPRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRobustness.setStatus("current")


class _SwL2IGMPLastMemberQueryInterval_Type(Integer32):
    """Custom type swL2IGMPLastMemberQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2IGMPLastMemberQueryInterval_Type.__name__ = "Integer32"
_SwL2IGMPLastMemberQueryInterval_Object = MibTableColumn
swL2IGMPLastMemberQueryInterval = _SwL2IGMPLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1, 5),
    _SwL2IGMPLastMemberQueryInterval_Type()
)
swL2IGMPLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPLastMemberQueryInterval.setStatus("current")


class _SwL2IGMPHostTimeout_Type(Integer32):
    """Custom type swL2IGMPHostTimeout based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16711450),
    )


_SwL2IGMPHostTimeout_Type.__name__ = "Integer32"
_SwL2IGMPHostTimeout_Object = MibTableColumn
swL2IGMPHostTimeout = _SwL2IGMPHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1, 6),
    _SwL2IGMPHostTimeout_Type()
)
swL2IGMPHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPHostTimeout.setStatus("current")


class _SwL2IGMPRouteTimeout_Type(Integer32):
    """Custom type swL2IGMPRouteTimeout based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16711450),
    )


_SwL2IGMPRouteTimeout_Type.__name__ = "Integer32"
_SwL2IGMPRouteTimeout_Object = MibTableColumn
swL2IGMPRouteTimeout = _SwL2IGMPRouteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1, 7),
    _SwL2IGMPRouteTimeout_Type()
)
swL2IGMPRouteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouteTimeout.setStatus("current")


class _SwL2IGMPLeaveTimer_Type(Integer32):
    """Custom type swL2IGMPLeaveTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16711450),
    )


_SwL2IGMPLeaveTimer_Type.__name__ = "Integer32"
_SwL2IGMPLeaveTimer_Object = MibTableColumn
swL2IGMPLeaveTimer = _SwL2IGMPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1, 8),
    _SwL2IGMPLeaveTimer_Type()
)
swL2IGMPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPLeaveTimer.setStatus("current")


class _SwL2IGMPQueryState_Type(Integer32):
    """Custom type swL2IGMPQueryState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2IGMPQueryState_Type.__name__ = "Integer32"
_SwL2IGMPQueryState_Object = MibTableColumn
swL2IGMPQueryState = _SwL2IGMPQueryState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1, 9),
    _SwL2IGMPQueryState_Type()
)
swL2IGMPQueryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPQueryState.setStatus("current")


class _SwL2IGMPCurrentState_Type(Integer32):
    """Custom type swL2IGMPCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("non-querier", 3),
          ("other", 1),
          ("querier", 2))
    )


_SwL2IGMPCurrentState_Type.__name__ = "Integer32"
_SwL2IGMPCurrentState_Object = MibTableColumn
swL2IGMPCurrentState = _SwL2IGMPCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1, 10),
    _SwL2IGMPCurrentState_Type()
)
swL2IGMPCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPCurrentState.setStatus("current")


class _SwL2IGMPCtrlState_Type(Integer32):
    """Custom type swL2IGMPCtrlState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2IGMPCtrlState_Type.__name__ = "Integer32"
_SwL2IGMPCtrlState_Object = MibTableColumn
swL2IGMPCtrlState = _SwL2IGMPCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 3, 1, 11),
    _SwL2IGMPCtrlState_Type()
)
swL2IGMPCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPCtrlState.setStatus("current")
_SwL2IGMPQueryInfoTable_Object = MibTable
swL2IGMPQueryInfoTable = _SwL2IGMPQueryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 4)
)
if mibBuilder.loadTexts:
    swL2IGMPQueryInfoTable.setStatus("current")
_SwL2IGMPQueryInfoEntry_Object = MibTableRow
swL2IGMPQueryInfoEntry = _SwL2IGMPQueryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 4, 1)
)
swL2IGMPQueryInfoEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2IGMPInfoVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPQueryInfoEntry.setStatus("current")


class _SwL2IGMPInfoVid_Type(Integer32):
    """Custom type swL2IGMPInfoVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPInfoVid_Type.__name__ = "Integer32"
_SwL2IGMPInfoVid_Object = MibTableColumn
swL2IGMPInfoVid = _SwL2IGMPInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 4, 1, 1),
    _SwL2IGMPInfoVid_Type()
)
swL2IGMPInfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoVid.setStatus("current")


class _SwL2IGMPInfoQueryCount_Type(Integer32):
    """Custom type swL2IGMPInfoQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPInfoQueryCount_Type.__name__ = "Integer32"
_SwL2IGMPInfoQueryCount_Object = MibTableColumn
swL2IGMPInfoQueryCount = _SwL2IGMPInfoQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 4, 1, 2),
    _SwL2IGMPInfoQueryCount_Type()
)
swL2IGMPInfoQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoQueryCount.setStatus("current")


class _SwL2IGMPInfoTxQueryCount_Type(Integer32):
    """Custom type swL2IGMPInfoTxQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPInfoTxQueryCount_Type.__name__ = "Integer32"
_SwL2IGMPInfoTxQueryCount_Object = MibTableColumn
swL2IGMPInfoTxQueryCount = _SwL2IGMPInfoTxQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 4, 1, 3),
    _SwL2IGMPInfoTxQueryCount_Type()
)
swL2IGMPInfoTxQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoTxQueryCount.setStatus("current")
_SwL2IGMPGroupTable_Object = MibTable
swL2IGMPGroupTable = _SwL2IGMPGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 5)
)
if mibBuilder.loadTexts:
    swL2IGMPGroupTable.setStatus("current")
_SwL2IGMPGroupEntry_Object = MibTableRow
swL2IGMPGroupEntry = _SwL2IGMPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 5, 1)
)
swL2IGMPGroupEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2IGMPVid"),
    (0, "SWL2MGMT-MIB", "swL2IGMPGroupIpAddr"),
)
if mibBuilder.loadTexts:
    swL2IGMPGroupEntry.setStatus("current")


class _SwL2IGMPVid_Type(Integer32):
    """Custom type swL2IGMPVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPVid_Type.__name__ = "Integer32"
_SwL2IGMPVid_Object = MibTableColumn
swL2IGMPVid = _SwL2IGMPVid_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 5, 1, 1),
    _SwL2IGMPVid_Type()
)
swL2IGMPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVid.setStatus("current")
_SwL2IGMPGroupIpAddr_Type = IpAddress
_SwL2IGMPGroupIpAddr_Object = MibTableColumn
swL2IGMPGroupIpAddr = _SwL2IGMPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 5, 1, 2),
    _SwL2IGMPGroupIpAddr_Type()
)
swL2IGMPGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPGroupIpAddr.setStatus("current")
_SwL2IGMPMacAddr_Type = MacAddress
_SwL2IGMPMacAddr_Object = MibTableColumn
swL2IGMPMacAddr = _SwL2IGMPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 5, 1, 3),
    _SwL2IGMPMacAddr_Type()
)
swL2IGMPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMacAddr.setStatus("current")
_SwL2IGMPPortMap_Type = PortList
_SwL2IGMPPortMap_Object = MibTableColumn
swL2IGMPPortMap = _SwL2IGMPPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 5, 1, 4),
    _SwL2IGMPPortMap_Type()
)
swL2IGMPPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortMap.setStatus("current")


class _SwL2IGMPIpGroupReportCount_Type(Integer32):
    """Custom type swL2IGMPIpGroupReportCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPIpGroupReportCount_Type.__name__ = "Integer32"
_SwL2IGMPIpGroupReportCount_Object = MibTableColumn
swL2IGMPIpGroupReportCount = _SwL2IGMPIpGroupReportCount_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 5, 1, 5),
    _SwL2IGMPIpGroupReportCount_Type()
)
swL2IGMPIpGroupReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPIpGroupReportCount.setStatus("current")
_SwL2IGMPForwardTable_Object = MibTable
swL2IGMPForwardTable = _SwL2IGMPForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 6)
)
if mibBuilder.loadTexts:
    swL2IGMPForwardTable.setStatus("current")
_SwL2IGMPForwardEntry_Object = MibTableRow
swL2IGMPForwardEntry = _SwL2IGMPForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 6, 1)
)
swL2IGMPForwardEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2IGMPForwardVid"),
    (0, "SWL2MGMT-MIB", "swL2IGMPForwardGroupIpAddr"),
)
if mibBuilder.loadTexts:
    swL2IGMPForwardEntry.setStatus("current")


class _SwL2IGMPForwardVid_Type(Integer32):
    """Custom type swL2IGMPForwardVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPForwardVid_Type.__name__ = "Integer32"
_SwL2IGMPForwardVid_Object = MibTableColumn
swL2IGMPForwardVid = _SwL2IGMPForwardVid_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 6, 1, 1),
    _SwL2IGMPForwardVid_Type()
)
swL2IGMPForwardVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPForwardVid.setStatus("current")
_SwL2IGMPForwardGroupIpAddr_Type = IpAddress
_SwL2IGMPForwardGroupIpAddr_Object = MibTableColumn
swL2IGMPForwardGroupIpAddr = _SwL2IGMPForwardGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 6, 1, 2),
    _SwL2IGMPForwardGroupIpAddr_Type()
)
swL2IGMPForwardGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPForwardGroupIpAddr.setStatus("current")
_SwL2IGMPForwardPortMap_Type = PortList
_SwL2IGMPForwardPortMap_Object = MibTableColumn
swL2IGMPForwardPortMap = _SwL2IGMPForwardPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 6, 1, 3),
    _SwL2IGMPForwardPortMap_Type()
)
swL2IGMPForwardPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPForwardPortMap.setStatus("current")
_SwL2IGMPRPTable_Object = MibTable
swL2IGMPRPTable = _SwL2IGMPRPTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 7)
)
if mibBuilder.loadTexts:
    swL2IGMPRPTable.setStatus("current")
_SwL2IGMPRPEntry_Object = MibTableRow
swL2IGMPRPEntry = _SwL2IGMPRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 7, 1)
)
swL2IGMPRPEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2IGMPRPVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPRPEntry.setStatus("current")


class _SwL2IGMPRPVid_Type(Integer32):
    """Custom type swL2IGMPRPVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPRPVid_Type.__name__ = "Integer32"
_SwL2IGMPRPVid_Object = MibTableColumn
swL2IGMPRPVid = _SwL2IGMPRPVid_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 7, 1, 1),
    _SwL2IGMPRPVid_Type()
)
swL2IGMPRPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRPVid.setStatus("current")
_SwL2IGMPRPStaticRouterPort_Type = PortList
_SwL2IGMPRPStaticRouterPort_Object = MibTableColumn
swL2IGMPRPStaticRouterPort = _SwL2IGMPRPStaticRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 7, 1, 2),
    _SwL2IGMPRPStaticRouterPort_Type()
)
swL2IGMPRPStaticRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRPStaticRouterPort.setStatus("current")
_SwL2IGMPRPDynamicRouterPort_Type = PortList
_SwL2IGMPRPDynamicRouterPort_Object = MibTableColumn
swL2IGMPRPDynamicRouterPort = _SwL2IGMPRPDynamicRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 7, 1, 3),
    _SwL2IGMPRPDynamicRouterPort_Type()
)
swL2IGMPRPDynamicRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRPDynamicRouterPort.setStatus("current")


class _SwL2IGMPMulticastRouterOnly_Type(Integer32):
    """Custom type swL2IGMPMulticastRouterOnly based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2IGMPMulticastRouterOnly_Type.__name__ = "Integer32"
_SwL2IGMPMulticastRouterOnly_Object = MibScalar
swL2IGMPMulticastRouterOnly = _SwL2IGMPMulticastRouterOnly_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 8),
    _SwL2IGMPMulticastRouterOnly_Type()
)
swL2IGMPMulticastRouterOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastRouterOnly.setStatus("current")
_SwL2IGMPGroupPortTable_Object = MibTable
swL2IGMPGroupPortTable = _SwL2IGMPGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 9)
)
if mibBuilder.loadTexts:
    swL2IGMPGroupPortTable.setStatus("current")
_SwL2IGMPGroupPortEntry_Object = MibTableRow
swL2IGMPGroupPortEntry = _SwL2IGMPGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 9, 1)
)
swL2IGMPGroupPortEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2IGMPVid"),
    (0, "SWL2MGMT-MIB", "swL2IGMPGroupIpAddr"),
    (0, "SWL2MGMT-MIB", "swL2IGMPPortMember"),
)
if mibBuilder.loadTexts:
    swL2IGMPGroupPortEntry.setStatus("current")


class _SwL2IGMPPortMember_Type(Integer32):
    """Custom type swL2IGMPPortMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPPortMember_Type.__name__ = "Integer32"
_SwL2IGMPPortMember_Object = MibTableColumn
swL2IGMPPortMember = _SwL2IGMPPortMember_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 9, 1, 1),
    _SwL2IGMPPortMember_Type()
)
swL2IGMPPortMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortMember.setStatus("current")


class _SwL2IGMPPortAgingTime_Type(Integer32):
    """Custom type swL2IGMPPortAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16711450),
    )


_SwL2IGMPPortAgingTime_Type.__name__ = "Integer32"
_SwL2IGMPPortAgingTime_Object = MibTableColumn
swL2IGMPPortAgingTime = _SwL2IGMPPortAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 9, 1, 2),
    _SwL2IGMPPortAgingTime_Type()
)
swL2IGMPPortAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortAgingTime.setStatus("current")


class _SwL2IGMPMulticastFilter_Type(Integer32):
    """Custom type swL2IGMPMulticastFilter based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2IGMPMulticastFilter_Type.__name__ = "Integer32"
_SwL2IGMPMulticastFilter_Object = MibScalar
swL2IGMPMulticastFilter = _SwL2IGMPMulticastFilter_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 10, 10),
    _SwL2IGMPMulticastFilter_Type()
)
swL2IGMPMulticastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastFilter.setStatus("current")
_SwL2TrafficMgmt_ObjectIdentity = ObjectIdentity
swL2TrafficMgmt = _SwL2TrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 12)
)
_SwL2TrafficCtrlTable_Object = MibTable
swL2TrafficCtrlTable = _SwL2TrafficCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    swL2TrafficCtrlTable.setStatus("current")
_SwL2TrafficCtrlEntry_Object = MibTableRow
swL2TrafficCtrlEntry = _SwL2TrafficCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 12, 1, 1)
)
swL2TrafficCtrlEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2TrafficCtrlGroupIndex"),
)
if mibBuilder.loadTexts:
    swL2TrafficCtrlEntry.setStatus("current")


class _SwL2TrafficCtrlGroupIndex_Type(Integer32):
    """Custom type swL2TrafficCtrlGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrafficCtrlGroupIndex_Type.__name__ = "Integer32"
_SwL2TrafficCtrlGroupIndex_Object = MibTableColumn
swL2TrafficCtrlGroupIndex = _SwL2TrafficCtrlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 12, 1, 1, 1),
    _SwL2TrafficCtrlGroupIndex_Type()
)
swL2TrafficCtrlGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficCtrlGroupIndex.setStatus("current")


class _SwL2TrafficCtrlUnitIndex_Type(Integer32):
    """Custom type swL2TrafficCtrlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrafficCtrlUnitIndex_Type.__name__ = "Integer32"
_SwL2TrafficCtrlUnitIndex_Object = MibTableColumn
swL2TrafficCtrlUnitIndex = _SwL2TrafficCtrlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 12, 1, 1, 2),
    _SwL2TrafficCtrlUnitIndex_Type()
)
swL2TrafficCtrlUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficCtrlUnitIndex.setStatus("current")


class _SwL2TrafficCtrlBMStormthreshold_Type(Integer32):
    """Custom type swL2TrafficCtrlBMStormthreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL2TrafficCtrlBMStormthreshold_Type.__name__ = "Integer32"
_SwL2TrafficCtrlBMStormthreshold_Object = MibTableColumn
swL2TrafficCtrlBMStormthreshold = _SwL2TrafficCtrlBMStormthreshold_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 12, 1, 1, 3),
    _SwL2TrafficCtrlBMStormthreshold_Type()
)
swL2TrafficCtrlBMStormthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlBMStormthreshold.setStatus("current")


class _SwL2TrafficCtrlBcastStormCtrl_Type(Integer32):
    """Custom type swL2TrafficCtrlBcastStormCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2TrafficCtrlBcastStormCtrl_Type.__name__ = "Integer32"
_SwL2TrafficCtrlBcastStormCtrl_Object = MibTableColumn
swL2TrafficCtrlBcastStormCtrl = _SwL2TrafficCtrlBcastStormCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 12, 1, 1, 4),
    _SwL2TrafficCtrlBcastStormCtrl_Type()
)
swL2TrafficCtrlBcastStormCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlBcastStormCtrl.setStatus("current")


class _SwL2TrafficCtrlMcastStormCtrl_Type(Integer32):
    """Custom type swL2TrafficCtrlMcastStormCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2TrafficCtrlMcastStormCtrl_Type.__name__ = "Integer32"
_SwL2TrafficCtrlMcastStormCtrl_Object = MibTableColumn
swL2TrafficCtrlMcastStormCtrl = _SwL2TrafficCtrlMcastStormCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 12, 1, 1, 5),
    _SwL2TrafficCtrlMcastStormCtrl_Type()
)
swL2TrafficCtrlMcastStormCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlMcastStormCtrl.setStatus("current")


class _SwL2TrafficCtrlDlfStormCtrl_Type(Integer32):
    """Custom type swL2TrafficCtrlDlfStormCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2TrafficCtrlDlfStormCtrl_Type.__name__ = "Integer32"
_SwL2TrafficCtrlDlfStormCtrl_Object = MibTableColumn
swL2TrafficCtrlDlfStormCtrl = _SwL2TrafficCtrlDlfStormCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 12, 1, 1, 6),
    _SwL2TrafficCtrlDlfStormCtrl_Type()
)
swL2TrafficCtrlDlfStormCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlDlfStormCtrl.setStatus("current")
_SwL2QosMgmt_ObjectIdentity = ObjectIdentity
swL2QosMgmt = _SwL2QosMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13)
)
_SwL2QosSchedulingTable_Object = MibTable
swL2QosSchedulingTable = _SwL2QosSchedulingTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    swL2QosSchedulingTable.setStatus("current")
_SwL2QosSchedulingEntry_Object = MibTableRow
swL2QosSchedulingEntry = _SwL2QosSchedulingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 1, 1)
)
swL2QosSchedulingEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2QosSchedulingClassId"),
)
if mibBuilder.loadTexts:
    swL2QosSchedulingEntry.setStatus("current")


class _SwL2QosSchedulingClassId_Type(Integer32):
    """Custom type swL2QosSchedulingClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2QosSchedulingClassId_Type.__name__ = "Integer32"
_SwL2QosSchedulingClassId_Object = MibTableColumn
swL2QosSchedulingClassId = _SwL2QosSchedulingClassId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 1, 1, 1),
    _SwL2QosSchedulingClassId_Type()
)
swL2QosSchedulingClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QosSchedulingClassId.setStatus("current")


class _SwL2QosSchedulingMaxPkts_Type(Integer32):
    """Custom type swL2QosSchedulingMaxPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL2QosSchedulingMaxPkts_Type.__name__ = "Integer32"
_SwL2QosSchedulingMaxPkts_Object = MibTableColumn
swL2QosSchedulingMaxPkts = _SwL2QosSchedulingMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 1, 1, 2),
    _SwL2QosSchedulingMaxPkts_Type()
)
swL2QosSchedulingMaxPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QosSchedulingMaxPkts.setStatus("current")


class _SwL2QosSchedulingMaxLatency_Type(Integer32):
    """Custom type swL2QosSchedulingMaxLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL2QosSchedulingMaxLatency_Type.__name__ = "Integer32"
_SwL2QosSchedulingMaxLatency_Object = MibTableColumn
swL2QosSchedulingMaxLatency = _SwL2QosSchedulingMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 1, 1, 3),
    _SwL2QosSchedulingMaxLatency_Type()
)
swL2QosSchedulingMaxLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QosSchedulingMaxLatency.setStatus("current")
_SwL2QosPriorityTable_Object = MibTable
swL2QosPriorityTable = _SwL2QosPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    swL2QosPriorityTable.setStatus("current")
_SwL2QosPriorityEntry_Object = MibTableRow
swL2QosPriorityEntry = _SwL2QosPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 2, 1)
)
swL2QosPriorityEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2QosPriorityType"),
    (0, "SWL2MGMT-MIB", "swL2QosPriorityValue"),
)
if mibBuilder.loadTexts:
    swL2QosPriorityEntry.setStatus("current")


class _SwL2QosPriorityType_Type(Integer32):
    """Custom type swL2QosPriorityType based on Integer32"""
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
        *(("other", 1),
          ("type-8021p", 3),
          ("type-dscp", 2),
          ("type-ip", 6),
          ("type-mac", 7),
          ("type-tcp", 4),
          ("type-udp", 5))
    )


_SwL2QosPriorityType_Type.__name__ = "Integer32"
_SwL2QosPriorityType_Object = MibTableColumn
swL2QosPriorityType = _SwL2QosPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 2, 1, 1),
    _SwL2QosPriorityType_Type()
)
swL2QosPriorityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QosPriorityType.setStatus("current")


class _SwL2QosPriorityValue_Type(OctetString):
    """Custom type swL2QosPriorityValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(6, 6),
    )


_SwL2QosPriorityValue_Type.__name__ = "OctetString"
_SwL2QosPriorityValue_Object = MibTableColumn
swL2QosPriorityValue = _SwL2QosPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 2, 1, 2),
    _SwL2QosPriorityValue_Type()
)
swL2QosPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QosPriorityValue.setStatus("current")


class _SwL2QosPriorityPriority_Type(Integer32):
    """Custom type swL2QosPriorityPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2QosPriorityPriority_Type.__name__ = "Integer32"
_SwL2QosPriorityPriority_Object = MibTableColumn
swL2QosPriorityPriority = _SwL2QosPriorityPriority_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 2, 1, 3),
    _SwL2QosPriorityPriority_Type()
)
swL2QosPriorityPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QosPriorityPriority.setStatus("current")


class _SwL2QosPriorityPriorityState_Type(Integer32):
    """Custom type swL2QosPriorityPriorityState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2QosPriorityPriorityState_Type.__name__ = "Integer32"
_SwL2QosPriorityPriorityState_Object = MibTableColumn
swL2QosPriorityPriorityState = _SwL2QosPriorityPriorityState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 2, 1, 4),
    _SwL2QosPriorityPriorityState_Type()
)
swL2QosPriorityPriorityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QosPriorityPriorityState.setStatus("current")


class _SwL2QosPriorityReplaceDscp_Type(Integer32):
    """Custom type swL2QosPriorityReplaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwL2QosPriorityReplaceDscp_Type.__name__ = "Integer32"
_SwL2QosPriorityReplaceDscp_Object = MibTableColumn
swL2QosPriorityReplaceDscp = _SwL2QosPriorityReplaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 2, 1, 5),
    _SwL2QosPriorityReplaceDscp_Type()
)
swL2QosPriorityReplaceDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QosPriorityReplaceDscp.setStatus("current")


class _SwL2QosPriorityReplaceDscpState_Type(Integer32):
    """Custom type swL2QosPriorityReplaceDscpState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2QosPriorityReplaceDscpState_Type.__name__ = "Integer32"
_SwL2QosPriorityReplaceDscpState_Object = MibTableColumn
swL2QosPriorityReplaceDscpState = _SwL2QosPriorityReplaceDscpState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 2, 1, 6),
    _SwL2QosPriorityReplaceDscpState_Type()
)
swL2QosPriorityReplaceDscpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QosPriorityReplaceDscpState.setStatus("current")


class _SwL2QosPriorityReplacePriority_Type(Integer32):
    """Custom type swL2QosPriorityReplacePriority based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2QosPriorityReplacePriority_Type.__name__ = "Integer32"
_SwL2QosPriorityReplacePriority_Object = MibTableColumn
swL2QosPriorityReplacePriority = _SwL2QosPriorityReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 2, 1, 7),
    _SwL2QosPriorityReplacePriority_Type()
)
swL2QosPriorityReplacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QosPriorityReplacePriority.setStatus("current")


class _SwL2QosPriorityState_Type(Integer32):
    """Custom type swL2QosPriorityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL2QosPriorityState_Type.__name__ = "Integer32"
_SwL2QosPriorityState_Object = MibTableColumn
swL2QosPriorityState = _SwL2QosPriorityState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 13, 2, 1, 8),
    _SwL2QosPriorityState_Type()
)
swL2QosPriorityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QosPriorityState.setStatus("current")
_SwL2MgmtMIBTraps_ObjectIdentity = ObjectIdentity
swL2MgmtMIBTraps = _SwL2MgmtMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 14)
)
_SwL2StormCtrlMgmt_ObjectIdentity = ObjectIdentity
swL2StormCtrlMgmt = _SwL2StormCtrlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15)
)
_SwL2StormCtrlTable_Object = MibTable
swL2StormCtrlTable = _SwL2StormCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    swL2StormCtrlTable.setStatus("current")
_SwL2StormCtrlEntry_Object = MibTableRow
swL2StormCtrlEntry = _SwL2StormCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 1, 1)
)
swL2StormCtrlEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2StormCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swL2StormCtrlEntry.setStatus("current")


class _SwL2StormCtrlPortIndex_Type(Integer32):
    """Custom type swL2StormCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2StormCtrlPortIndex_Type.__name__ = "Integer32"
_SwL2StormCtrlPortIndex_Object = MibTableColumn
swL2StormCtrlPortIndex = _SwL2StormCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 1, 1, 1),
    _SwL2StormCtrlPortIndex_Type()
)
swL2StormCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StormCtrlPortIndex.setStatus("current")


class _SwL2StormCtrlBcastStormCtrl_Type(Integer32):
    """Custom type swL2StormCtrlBcastStormCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2StormCtrlBcastStormCtrl_Type.__name__ = "Integer32"
_SwL2StormCtrlBcastStormCtrl_Object = MibTableColumn
swL2StormCtrlBcastStormCtrl = _SwL2StormCtrlBcastStormCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 1, 1, 2),
    _SwL2StormCtrlBcastStormCtrl_Type()
)
swL2StormCtrlBcastStormCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StormCtrlBcastStormCtrl.setStatus("current")


class _SwL2StormCtrlMcastStormCtrl_Type(Integer32):
    """Custom type swL2StormCtrlMcastStormCtrl based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2StormCtrlMcastStormCtrl_Type.__name__ = "Integer32"
_SwL2StormCtrlMcastStormCtrl_Object = MibTableColumn
swL2StormCtrlMcastStormCtrl = _SwL2StormCtrlMcastStormCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 1, 1, 3),
    _SwL2StormCtrlMcastStormCtrl_Type()
)
swL2StormCtrlMcastStormCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StormCtrlMcastStormCtrl.setStatus("current")


class _SwL2StormCtrlBMStormThreshold_Type(Integer32):
    """Custom type swL2StormCtrlBMStormThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwL2StormCtrlBMStormThreshold_Type.__name__ = "Integer32"
_SwL2StormCtrlBMStormThreshold_Object = MibTableColumn
swL2StormCtrlBMStormThreshold = _SwL2StormCtrlBMStormThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 1, 1, 4),
    _SwL2StormCtrlBMStormThreshold_Type()
)
swL2StormCtrlBMStormThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StormCtrlBMStormThreshold.setStatus("current")


class _SwL2StormCtrlDlfState_Type(Integer32):
    """Custom type swL2StormCtrlDlfState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2StormCtrlDlfState_Type.__name__ = "Integer32"
_SwL2StormCtrlDlfState_Object = MibScalar
swL2StormCtrlDlfState = _SwL2StormCtrlDlfState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 2),
    _SwL2StormCtrlDlfState_Type()
)
swL2StormCtrlDlfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StormCtrlDlfState.setStatus("current")


class _SwL2StormCtrlDlfThreshold_Type(Integer32):
    """Custom type swL2StormCtrlDlfThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 148810),
    )


_SwL2StormCtrlDlfThreshold_Type.__name__ = "Integer32"
_SwL2StormCtrlDlfThreshold_Object = MibScalar
swL2StormCtrlDlfThreshold = _SwL2StormCtrlDlfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 3),
    _SwL2StormCtrlDlfThreshold_Type()
)
swL2StormCtrlDlfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StormCtrlDlfThreshold.setStatus("current")
_SwL2CpuRateLimitTable_Object = MibTable
swL2CpuRateLimitTable = _SwL2CpuRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 4)
)
if mibBuilder.loadTexts:
    swL2CpuRateLimitTable.setStatus("current")
_SwL2CpuRateLimitEntry_Object = MibTableRow
swL2CpuRateLimitEntry = _SwL2CpuRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 4, 1)
)
swL2CpuRateLimitEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2CpuRateLimitPortIndex"),
)
if mibBuilder.loadTexts:
    swL2CpuRateLimitEntry.setStatus("current")


class _SwL2CpuRateLimitPortIndex_Type(Integer32):
    """Custom type swL2CpuRateLimitPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2CpuRateLimitPortIndex_Type.__name__ = "Integer32"
_SwL2CpuRateLimitPortIndex_Object = MibTableColumn
swL2CpuRateLimitPortIndex = _SwL2CpuRateLimitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 4, 1, 1),
    _SwL2CpuRateLimitPortIndex_Type()
)
swL2CpuRateLimitPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CpuRateLimitPortIndex.setStatus("current")


class _SwL2CpuRateLimitState_Type(Integer32):
    """Custom type swL2CpuRateLimitState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2CpuRateLimitState_Type.__name__ = "Integer32"
_SwL2CpuRateLimitState_Object = MibTableColumn
swL2CpuRateLimitState = _SwL2CpuRateLimitState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 4, 1, 2),
    _SwL2CpuRateLimitState_Type()
)
swL2CpuRateLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CpuRateLimitState.setStatus("current")


class _SwL2CpuRateLimitBcastThreshold_Type(Integer32):
    """Custom type swL2CpuRateLimitBcastThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1700),
    )


_SwL2CpuRateLimitBcastThreshold_Type.__name__ = "Integer32"
_SwL2CpuRateLimitBcastThreshold_Object = MibTableColumn
swL2CpuRateLimitBcastThreshold = _SwL2CpuRateLimitBcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 4, 1, 3),
    _SwL2CpuRateLimitBcastThreshold_Type()
)
swL2CpuRateLimitBcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CpuRateLimitBcastThreshold.setStatus("current")


class _SwL2CpuRateLimitMcastThreshold_Type(Integer32):
    """Custom type swL2CpuRateLimitMcastThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_SwL2CpuRateLimitMcastThreshold_Type.__name__ = "Integer32"
_SwL2CpuRateLimitMcastThreshold_Object = MibTableColumn
swL2CpuRateLimitMcastThreshold = _SwL2CpuRateLimitMcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 4, 1, 4),
    _SwL2CpuRateLimitMcastThreshold_Type()
)
swL2CpuRateLimitMcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CpuRateLimitMcastThreshold.setStatus("current")


class _SwL2CpuUtilization_Type(Integer32):
    """Custom type swL2CpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwL2CpuUtilization_Type.__name__ = "Integer32"
_SwL2CpuUtilization_Object = MibScalar
swL2CpuUtilization = _SwL2CpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 15, 5),
    _SwL2CpuUtilization_Type()
)
swL2CpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CpuUtilization.setStatus("current")
_SwL2ACLQosMgmt_ObjectIdentity = ObjectIdentity
swL2ACLQosMgmt = _SwL2ACLQosMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16)
)


class _SwL2ACLQosTemplate1Mode_Type(Integer32):
    """Custom type swL2ACLQosTemplate1Mode based on Integer32"""
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
        *(("l4-switch", 4),
          ("other", 1),
          ("qos", 3),
          ("security", 2))
    )


_SwL2ACLQosTemplate1Mode_Type.__name__ = "Integer32"
_SwL2ACLQosTemplate1Mode_Object = MibScalar
swL2ACLQosTemplate1Mode = _SwL2ACLQosTemplate1Mode_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 1),
    _SwL2ACLQosTemplate1Mode_Type()
)
swL2ACLQosTemplate1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplate1Mode.setStatus("current")


class _SwL2ACLQosTemplate2Mode_Type(Integer32):
    """Custom type swL2ACLQosTemplate2Mode based on Integer32"""
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
        *(("l4-switch", 4),
          ("other", 1),
          ("qos", 3),
          ("security", 2))
    )


_SwL2ACLQosTemplate2Mode_Type.__name__ = "Integer32"
_SwL2ACLQosTemplate2Mode_Object = MibScalar
swL2ACLQosTemplate2Mode = _SwL2ACLQosTemplate2Mode_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 2),
    _SwL2ACLQosTemplate2Mode_Type()
)
swL2ACLQosTemplate2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplate2Mode.setStatus("current")
_SwL2ACLQosFlowClassifierTable_Object = MibTable
swL2ACLQosFlowClassifierTable = _SwL2ACLQosFlowClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3)
)
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierTable.setStatus("current")
_SwL2ACLQosFlowClassifierEntry_Object = MibTableRow
swL2ACLQosFlowClassifierEntry = _SwL2ACLQosFlowClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1)
)
swL2ACLQosFlowClassifierEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2ACLQosFlowClassifierTemplateId"),
)
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierEntry.setStatus("current")


class _SwL2ACLQosFlowClassifierTemplateId_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierTemplateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosFlowClassifierTemplateId_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierTemplateId_Object = MibTableColumn
swL2ACLQosFlowClassifierTemplateId = _SwL2ACLQosFlowClassifierTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 1),
    _SwL2ACLQosFlowClassifierTemplateId_Type()
)
swL2ACLQosFlowClassifierTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierTemplateId.setStatus("current")


class _SwL2ACLQosFlowClassifierCurrentMode_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierCurrentMode based on Integer32"""
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
        *(("l4-switch", 4),
          ("other", 1),
          ("qos", 3),
          ("security", 2))
    )


_SwL2ACLQosFlowClassifierCurrentMode_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierCurrentMode_Object = MibTableColumn
swL2ACLQosFlowClassifierCurrentMode = _SwL2ACLQosFlowClassifierCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 2),
    _SwL2ACLQosFlowClassifierCurrentMode_Type()
)
swL2ACLQosFlowClassifierCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierCurrentMode.setStatus("current")
_SwL2ACLQosFlowClassifierSecuritySrcMask_Type = IpAddress
_SwL2ACLQosFlowClassifierSecuritySrcMask_Object = MibTableColumn
swL2ACLQosFlowClassifierSecuritySrcMask = _SwL2ACLQosFlowClassifierSecuritySrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 3),
    _SwL2ACLQosFlowClassifierSecuritySrcMask_Type()
)
swL2ACLQosFlowClassifierSecuritySrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierSecuritySrcMask.setStatus("current")


class _SwL2ACLQosFlowClassifierQosFlavor_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierQosFlavor based on Integer32"""
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
        *(("flavor-8021p", 1),
          ("flavor-dscp", 2),
          ("flavor-ip", 3),
          ("flavor-tcp", 4),
          ("flavor-udp", 5),
          ("flavor-un-used", 6))
    )


_SwL2ACLQosFlowClassifierQosFlavor_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierQosFlavor_Object = MibTableColumn
swL2ACLQosFlowClassifierQosFlavor = _SwL2ACLQosFlowClassifierQosFlavor_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 4),
    _SwL2ACLQosFlowClassifierQosFlavor_Type()
)
swL2ACLQosFlowClassifierQosFlavor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierQosFlavor.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchTCPDstIp_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchTCPDstIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchTCPDstIp_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchTCPDstIp_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchTCPDstIp = _SwL2ACLQosFlowClassifierL4SwitchTCPDstIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 5),
    _SwL2ACLQosFlowClassifierL4SwitchTCPDstIp_Type()
)
swL2ACLQosFlowClassifierL4SwitchTCPDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchTCPDstIp.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchTCPSrcIp_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchTCPSrcIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchTCPSrcIp_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchTCPSrcIp_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchTCPSrcIp = _SwL2ACLQosFlowClassifierL4SwitchTCPSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 6),
    _SwL2ACLQosFlowClassifierL4SwitchTCPSrcIp_Type()
)
swL2ACLQosFlowClassifierL4SwitchTCPSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchTCPSrcIp.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchTCPTos_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchTCPTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchTCPTos_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchTCPTos_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchTCPTos = _SwL2ACLQosFlowClassifierL4SwitchTCPTos_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 7),
    _SwL2ACLQosFlowClassifierL4SwitchTCPTos_Type()
)
swL2ACLQosFlowClassifierL4SwitchTCPTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchTCPTos.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchTCPDstPort_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchTCPDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchTCPDstPort_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchTCPDstPort_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchTCPDstPort = _SwL2ACLQosFlowClassifierL4SwitchTCPDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 8),
    _SwL2ACLQosFlowClassifierL4SwitchTCPDstPort_Type()
)
swL2ACLQosFlowClassifierL4SwitchTCPDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchTCPDstPort.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchTCPSrcPort_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchTCPSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchTCPSrcPort_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchTCPSrcPort_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchTCPSrcPort = _SwL2ACLQosFlowClassifierL4SwitchTCPSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 9),
    _SwL2ACLQosFlowClassifierL4SwitchTCPSrcPort_Type()
)
swL2ACLQosFlowClassifierL4SwitchTCPSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchTCPSrcPort.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchTCPFlags_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchTCPFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchTCPFlags_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchTCPFlags_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchTCPFlags = _SwL2ACLQosFlowClassifierL4SwitchTCPFlags_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 10),
    _SwL2ACLQosFlowClassifierL4SwitchTCPFlags_Type()
)
swL2ACLQosFlowClassifierL4SwitchTCPFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchTCPFlags.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchUDPDstIp_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchUDPDstIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchUDPDstIp_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchUDPDstIp_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchUDPDstIp = _SwL2ACLQosFlowClassifierL4SwitchUDPDstIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 11),
    _SwL2ACLQosFlowClassifierL4SwitchUDPDstIp_Type()
)
swL2ACLQosFlowClassifierL4SwitchUDPDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchUDPDstIp.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchUDPSrcIp_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchUDPSrcIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchUDPSrcIp_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchUDPSrcIp_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchUDPSrcIp = _SwL2ACLQosFlowClassifierL4SwitchUDPSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 12),
    _SwL2ACLQosFlowClassifierL4SwitchUDPSrcIp_Type()
)
swL2ACLQosFlowClassifierL4SwitchUDPSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchUDPSrcIp.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchUDPTos_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchUDPTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchUDPTos_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchUDPTos_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchUDPTos = _SwL2ACLQosFlowClassifierL4SwitchUDPTos_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 13),
    _SwL2ACLQosFlowClassifierL4SwitchUDPTos_Type()
)
swL2ACLQosFlowClassifierL4SwitchUDPTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchUDPTos.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchUDPDstPort_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchUDPDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchUDPDstPort_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchUDPDstPort_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchUDPDstPort = _SwL2ACLQosFlowClassifierL4SwitchUDPDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 14),
    _SwL2ACLQosFlowClassifierL4SwitchUDPDstPort_Type()
)
swL2ACLQosFlowClassifierL4SwitchUDPDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchUDPDstPort.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchUDPSrcPort_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchUDPSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchUDPSrcPort_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchUDPSrcPort_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchUDPSrcPort = _SwL2ACLQosFlowClassifierL4SwitchUDPSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 15),
    _SwL2ACLQosFlowClassifierL4SwitchUDPSrcPort_Type()
)
swL2ACLQosFlowClassifierL4SwitchUDPSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchUDPSrcPort.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchOtherDstIp_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchOtherDstIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchOtherDstIp_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchOtherDstIp_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchOtherDstIp = _SwL2ACLQosFlowClassifierL4SwitchOtherDstIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 16),
    _SwL2ACLQosFlowClassifierL4SwitchOtherDstIp_Type()
)
swL2ACLQosFlowClassifierL4SwitchOtherDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchOtherDstIp.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchOtherSrcIp_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchOtherSrcIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchOtherSrcIp_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchOtherSrcIp_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchOtherSrcIp = _SwL2ACLQosFlowClassifierL4SwitchOtherSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 17),
    _SwL2ACLQosFlowClassifierL4SwitchOtherSrcIp_Type()
)
swL2ACLQosFlowClassifierL4SwitchOtherSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchOtherSrcIp.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchOtherTos_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchOtherTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchOtherTos_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchOtherTos_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchOtherTos = _SwL2ACLQosFlowClassifierL4SwitchOtherTos_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 18),
    _SwL2ACLQosFlowClassifierL4SwitchOtherTos_Type()
)
swL2ACLQosFlowClassifierL4SwitchOtherTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchOtherTos.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchOtherL4Protocol_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchOtherL4Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchOtherL4Protocol_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchOtherL4Protocol_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchOtherL4Protocol = _SwL2ACLQosFlowClassifierL4SwitchOtherL4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 19),
    _SwL2ACLQosFlowClassifierL4SwitchOtherL4Protocol_Type()
)
swL2ACLQosFlowClassifierL4SwitchOtherL4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchOtherL4Protocol.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchOtherICMPMessage_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchOtherICMPMessage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchOtherICMPMessage_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchOtherICMPMessage_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchOtherICMPMessage = _SwL2ACLQosFlowClassifierL4SwitchOtherICMPMessage_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 20),
    _SwL2ACLQosFlowClassifierL4SwitchOtherICMPMessage_Type()
)
swL2ACLQosFlowClassifierL4SwitchOtherICMPMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchOtherICMPMessage.setStatus("current")


class _SwL2ACLQosFlowClassifierL4SwitchOtherIGMPType_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierL4SwitchOtherIGMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("un-used", 3))
    )


_SwL2ACLQosFlowClassifierL4SwitchOtherIGMPType_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierL4SwitchOtherIGMPType_Object = MibTableColumn
swL2ACLQosFlowClassifierL4SwitchOtherIGMPType = _SwL2ACLQosFlowClassifierL4SwitchOtherIGMPType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 21),
    _SwL2ACLQosFlowClassifierL4SwitchOtherIGMPType_Type()
)
swL2ACLQosFlowClassifierL4SwitchOtherIGMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierL4SwitchOtherIGMPType.setStatus("current")


class _SwL2ACLQosFlowClassifierActiveRuleNumber_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierActiveRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosFlowClassifierActiveRuleNumber_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierActiveRuleNumber_Object = MibTableColumn
swL2ACLQosFlowClassifierActiveRuleNumber = _SwL2ACLQosFlowClassifierActiveRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 22),
    _SwL2ACLQosFlowClassifierActiveRuleNumber_Type()
)
swL2ACLQosFlowClassifierActiveRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierActiveRuleNumber.setStatus("current")
_SwL2ACLQosFlowClassifierSecurityDstMask_Type = IpAddress
_SwL2ACLQosFlowClassifierSecurityDstMask_Object = MibTableColumn
swL2ACLQosFlowClassifierSecurityDstMask = _SwL2ACLQosFlowClassifierSecurityDstMask_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 3, 1, 23),
    _SwL2ACLQosFlowClassifierSecurityDstMask_Type()
)
swL2ACLQosFlowClassifierSecurityDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierSecurityDstMask.setStatus("current")
_SwL2ACLQosFlowClassifierVlanTable_Object = MibTable
swL2ACLQosFlowClassifierVlanTable = _SwL2ACLQosFlowClassifierVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 4)
)
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierVlanTable.setStatus("current")
_SwL2ACLQosFlowClassifierVlanEntry_Object = MibTableRow
swL2ACLQosFlowClassifierVlanEntry = _SwL2ACLQosFlowClassifierVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 4, 1)
)
swL2ACLQosFlowClassifierVlanEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2ACLQosFlowClassifierVlanTemplateId"),
    (0, "SWL2MGMT-MIB", "swL2ACLQosFlowClassifierVlanVlanName"),
)
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierVlanEntry.setStatus("current")


class _SwL2ACLQosFlowClassifierVlanTemplateId_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierVlanTemplateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosFlowClassifierVlanTemplateId_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierVlanTemplateId_Object = MibTableColumn
swL2ACLQosFlowClassifierVlanTemplateId = _SwL2ACLQosFlowClassifierVlanTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 4, 1, 1),
    _SwL2ACLQosFlowClassifierVlanTemplateId_Type()
)
swL2ACLQosFlowClassifierVlanTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierVlanTemplateId.setStatus("current")


class _SwL2ACLQosFlowClassifierVlanVlanName_Type(DisplayString):
    """Custom type swL2ACLQosFlowClassifierVlanVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2ACLQosFlowClassifierVlanVlanName_Type.__name__ = "DisplayString"
_SwL2ACLQosFlowClassifierVlanVlanName_Object = MibTableColumn
swL2ACLQosFlowClassifierVlanVlanName = _SwL2ACLQosFlowClassifierVlanVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 4, 1, 2),
    _SwL2ACLQosFlowClassifierVlanVlanName_Type()
)
swL2ACLQosFlowClassifierVlanVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierVlanVlanName.setStatus("current")


class _SwL2ACLQosFlowClassifierVlanState_Type(Integer32):
    """Custom type swL2ACLQosFlowClassifierVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attached", 2),
          ("detached", 3),
          ("other", 1))
    )


_SwL2ACLQosFlowClassifierVlanState_Type.__name__ = "Integer32"
_SwL2ACLQosFlowClassifierVlanState_Object = MibTableColumn
swL2ACLQosFlowClassifierVlanState = _SwL2ACLQosFlowClassifierVlanState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 4, 1, 3),
    _SwL2ACLQosFlowClassifierVlanState_Type()
)
swL2ACLQosFlowClassifierVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFlowClassifierVlanState.setStatus("current")
_SwL2ACLQosTemplateRuleTable_Object = MibTable
swL2ACLQosTemplateRuleTable = _SwL2ACLQosTemplateRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5)
)
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleTable.setStatus("current")
_SwL2ACLQosTemplateRuleEntry_Object = MibTableRow
swL2ACLQosTemplateRuleEntry = _SwL2ACLQosTemplateRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1)
)
swL2ACLQosTemplateRuleEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2ACLQosTemplateRuleTemplateId"),
    (0, "SWL2MGMT-MIB", "swL2ACLQosTemplateRuleIndex"),
)
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleEntry.setStatus("current")


class _SwL2ACLQosTemplateRuleTemplateId_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleTemplateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosTemplateRuleTemplateId_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleTemplateId_Object = MibTableColumn
swL2ACLQosTemplateRuleTemplateId = _SwL2ACLQosTemplateRuleTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 1),
    _SwL2ACLQosTemplateRuleTemplateId_Type()
)
swL2ACLQosTemplateRuleTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleTemplateId.setStatus("current")


class _SwL2ACLQosTemplateRuleIndex_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosTemplateRuleIndex_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleIndex_Object = MibTableColumn
swL2ACLQosTemplateRuleIndex = _SwL2ACLQosTemplateRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 2),
    _SwL2ACLQosTemplateRuleIndex_Type()
)
swL2ACLQosTemplateRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleIndex.setStatus("current")


class _SwL2ACLQosTemplateRuleMode_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleMode based on Integer32"""
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
        *(("l4-switch", 4),
          ("other", 1),
          ("qos", 3),
          ("security", 2))
    )


_SwL2ACLQosTemplateRuleMode_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleMode_Object = MibTableColumn
swL2ACLQosTemplateRuleMode = _SwL2ACLQosTemplateRuleMode_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 3),
    _SwL2ACLQosTemplateRuleMode_Type()
)
swL2ACLQosTemplateRuleMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleMode.setStatus("current")
_SwL2ACLQosTemplateRuleSecuritySrcIp_Type = IpAddress
_SwL2ACLQosTemplateRuleSecuritySrcIp_Object = MibTableColumn
swL2ACLQosTemplateRuleSecuritySrcIp = _SwL2ACLQosTemplateRuleSecuritySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 4),
    _SwL2ACLQosTemplateRuleSecuritySrcIp_Type()
)
swL2ACLQosTemplateRuleSecuritySrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleSecuritySrcIp.setStatus("current")


class _SwL2ACLQosTemplateRuleQosFlavor_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleQosFlavor based on Integer32"""
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
        *(("flavor-8021p", 1),
          ("flavor-dscp", 2),
          ("flavor-ip", 3),
          ("flavor-tcp", 4),
          ("flavor-udp", 5),
          ("flavor-un-used", 6))
    )


_SwL2ACLQosTemplateRuleQosFlavor_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleQosFlavor_Object = MibTableColumn
swL2ACLQosTemplateRuleQosFlavor = _SwL2ACLQosTemplateRuleQosFlavor_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 5),
    _SwL2ACLQosTemplateRuleQosFlavor_Type()
)
swL2ACLQosTemplateRuleQosFlavor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleQosFlavor.setStatus("current")


class _SwL2ACLQosTemplateRuleQosValue_Type(OctetString):
    """Custom type swL2ACLQosTemplateRuleQosValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(4, 4),
    )


_SwL2ACLQosTemplateRuleQosValue_Type.__name__ = "OctetString"
_SwL2ACLQosTemplateRuleQosValue_Object = MibTableColumn
swL2ACLQosTemplateRuleQosValue = _SwL2ACLQosTemplateRuleQosValue_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 6),
    _SwL2ACLQosTemplateRuleQosValue_Type()
)
swL2ACLQosTemplateRuleQosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleQosValue.setStatus("current")


class _SwL2ACLQosTemplateRuleQosPriority_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleQosPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2ACLQosTemplateRuleQosPriority_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleQosPriority_Object = MibTableColumn
swL2ACLQosTemplateRuleQosPriority = _SwL2ACLQosTemplateRuleQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 7),
    _SwL2ACLQosTemplateRuleQosPriority_Type()
)
swL2ACLQosTemplateRuleQosPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleQosPriority.setStatus("current")


class _SwL2ACLQosTemplateRuleQosDscp_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleQosDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwL2ACLQosTemplateRuleQosDscp_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleQosDscp_Object = MibTableColumn
swL2ACLQosTemplateRuleQosDscp = _SwL2ACLQosTemplateRuleQosDscp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 8),
    _SwL2ACLQosTemplateRuleQosDscp_Type()
)
swL2ACLQosTemplateRuleQosDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleQosDscp.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionType_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionType based on Integer32"""
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
        *(("other", 3),
          ("tcp", 1),
          ("udp", 2),
          ("un-used", 4))
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionType_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchSessionType_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionType = _SwL2ACLQosTemplateRuleL4SwitchSessionType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 9),
    _SwL2ACLQosTemplateRuleL4SwitchSessionType_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionType.setStatus("current")
_SwL2ACLQosTemplateRuleL4SwitchSessionTCPDstIp_Type = IpAddress
_SwL2ACLQosTemplateRuleL4SwitchSessionTCPDstIp_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionTCPDstIp = _SwL2ACLQosTemplateRuleL4SwitchSessionTCPDstIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 10),
    _SwL2ACLQosTemplateRuleL4SwitchSessionTCPDstIp_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionTCPDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionTCPDstIp.setStatus("current")
_SwL2ACLQosTemplateRuleL4SwitchSessionTCPSrcIp_Type = IpAddress
_SwL2ACLQosTemplateRuleL4SwitchSessionTCPSrcIp_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionTCPSrcIp = _SwL2ACLQosTemplateRuleL4SwitchSessionTCPSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 11),
    _SwL2ACLQosTemplateRuleL4SwitchSessionTCPSrcIp_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionTCPSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionTCPSrcIp.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionTCPTos_Type(OctetString):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionTCPTos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionTCPTos_Type.__name__ = "OctetString"
_SwL2ACLQosTemplateRuleL4SwitchSessionTCPTos_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionTCPTos = _SwL2ACLQosTemplateRuleL4SwitchSessionTCPTos_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 12),
    _SwL2ACLQosTemplateRuleL4SwitchSessionTCPTos_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionTCPTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionTCPTos.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionTCPDstPort_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionTCPDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionTCPDstPort_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchSessionTCPDstPort_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionTCPDstPort = _SwL2ACLQosTemplateRuleL4SwitchSessionTCPDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 13),
    _SwL2ACLQosTemplateRuleL4SwitchSessionTCPDstPort_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionTCPDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionTCPDstPort.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionTCPSrcPort_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionTCPSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionTCPSrcPort_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchSessionTCPSrcPort_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionTCPSrcPort = _SwL2ACLQosTemplateRuleL4SwitchSessionTCPSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 14),
    _SwL2ACLQosTemplateRuleL4SwitchSessionTCPSrcPort_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionTCPSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionTCPSrcPort.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionTCPFlags_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionTCPFlags based on Integer32"""
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
        *(("ack", 5),
          ("fin", 1),
          ("psh", 4),
          ("rst", 3),
          ("syn", 2),
          ("un-used", 7),
          ("urg", 6))
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionTCPFlags_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchSessionTCPFlags_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionTCPFlags = _SwL2ACLQosTemplateRuleL4SwitchSessionTCPFlags_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 15),
    _SwL2ACLQosTemplateRuleL4SwitchSessionTCPFlags_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionTCPFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionTCPFlags.setStatus("deprecated")
_SwL2ACLQosTemplateRuleL4SwitchSessionUDPDstIp_Type = IpAddress
_SwL2ACLQosTemplateRuleL4SwitchSessionUDPDstIp_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionUDPDstIp = _SwL2ACLQosTemplateRuleL4SwitchSessionUDPDstIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 16),
    _SwL2ACLQosTemplateRuleL4SwitchSessionUDPDstIp_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionUDPDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionUDPDstIp.setStatus("current")
_SwL2ACLQosTemplateRuleL4SwitchSessionUDPSrcIp_Type = IpAddress
_SwL2ACLQosTemplateRuleL4SwitchSessionUDPSrcIp_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionUDPSrcIp = _SwL2ACLQosTemplateRuleL4SwitchSessionUDPSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 17),
    _SwL2ACLQosTemplateRuleL4SwitchSessionUDPSrcIp_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionUDPSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionUDPSrcIp.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionUDPTos_Type(OctetString):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionUDPTos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionUDPTos_Type.__name__ = "OctetString"
_SwL2ACLQosTemplateRuleL4SwitchSessionUDPTos_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionUDPTos = _SwL2ACLQosTemplateRuleL4SwitchSessionUDPTos_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 18),
    _SwL2ACLQosTemplateRuleL4SwitchSessionUDPTos_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionUDPTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionUDPTos.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionUDPDstPort_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionUDPDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionUDPDstPort_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchSessionUDPDstPort_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionUDPDstPort = _SwL2ACLQosTemplateRuleL4SwitchSessionUDPDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 19),
    _SwL2ACLQosTemplateRuleL4SwitchSessionUDPDstPort_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionUDPDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionUDPDstPort.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionUDPSrcPort_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionUDPSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionUDPSrcPort_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchSessionUDPSrcPort_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionUDPSrcPort = _SwL2ACLQosTemplateRuleL4SwitchSessionUDPSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 20),
    _SwL2ACLQosTemplateRuleL4SwitchSessionUDPSrcPort_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionUDPSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionUDPSrcPort.setStatus("current")
_SwL2ACLQosTemplateRuleL4SwitchSessionOtherDstIp_Type = IpAddress
_SwL2ACLQosTemplateRuleL4SwitchSessionOtherDstIp_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionOtherDstIp = _SwL2ACLQosTemplateRuleL4SwitchSessionOtherDstIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 21),
    _SwL2ACLQosTemplateRuleL4SwitchSessionOtherDstIp_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionOtherDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionOtherDstIp.setStatus("current")
_SwL2ACLQosTemplateRuleL4SwitchSessionOtherSrcIp_Type = IpAddress
_SwL2ACLQosTemplateRuleL4SwitchSessionOtherSrcIp_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionOtherSrcIp = _SwL2ACLQosTemplateRuleL4SwitchSessionOtherSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 22),
    _SwL2ACLQosTemplateRuleL4SwitchSessionOtherSrcIp_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionOtherSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionOtherSrcIp.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionOtherTos_Type(OctetString):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionOtherTos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionOtherTos_Type.__name__ = "OctetString"
_SwL2ACLQosTemplateRuleL4SwitchSessionOtherTos_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionOtherTos = _SwL2ACLQosTemplateRuleL4SwitchSessionOtherTos_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 23),
    _SwL2ACLQosTemplateRuleL4SwitchSessionOtherTos_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionOtherTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionOtherTos.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionOtherL4Protocol_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionOtherL4Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("igmp", 2),
          ("un-used", 3))
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionOtherL4Protocol_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchSessionOtherL4Protocol_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionOtherL4Protocol = _SwL2ACLQosTemplateRuleL4SwitchSessionOtherL4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 24),
    _SwL2ACLQosTemplateRuleL4SwitchSessionOtherL4Protocol_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionOtherL4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionOtherL4Protocol.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionOtherICMPType_Type(OctetString):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionOtherICMPType_Type.__name__ = "OctetString"
_SwL2ACLQosTemplateRuleL4SwitchSessionOtherICMPType_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPType = _SwL2ACLQosTemplateRuleL4SwitchSessionOtherICMPType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 25),
    _SwL2ACLQosTemplateRuleL4SwitchSessionOtherICMPType_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPType.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionOtherICMPCode_Type(OctetString):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionOtherICMPCode_Type.__name__ = "OctetString"
_SwL2ACLQosTemplateRuleL4SwitchSessionOtherICMPCode_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPCode = _SwL2ACLQosTemplateRuleL4SwitchSessionOtherICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 26),
    _SwL2ACLQosTemplateRuleL4SwitchSessionOtherICMPCode_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPCode.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionOtherIGMPType_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionOtherIGMPType based on Integer32"""
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
        *(("query", 1),
          ("response-version-1", 2),
          ("response-version-2", 3),
          ("response-version-all", 4),
          ("un-used", 5))
    )


_SwL2ACLQosTemplateRuleL4SwitchSessionOtherIGMPType_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchSessionOtherIGMPType_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionOtherIGMPType = _SwL2ACLQosTemplateRuleL4SwitchSessionOtherIGMPType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 27),
    _SwL2ACLQosTemplateRuleL4SwitchSessionOtherIGMPType_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionOtherIGMPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionOtherIGMPType.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchActionType_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchActionType based on Integer32"""
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
        *(("drop", 1),
          ("forward", 2),
          ("redirect", 3),
          ("un-used", 4))
    )


_SwL2ACLQosTemplateRuleL4SwitchActionType_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchActionType_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchActionType = _SwL2ACLQosTemplateRuleL4SwitchActionType_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 28),
    _SwL2ACLQosTemplateRuleL4SwitchActionType_Type()
)
swL2ACLQosTemplateRuleL4SwitchActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchActionType.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchActionForwardPriorityState_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchActionForwardPriorityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("other", 1),
          ("true", 2))
    )


_SwL2ACLQosTemplateRuleL4SwitchActionForwardPriorityState_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchActionForwardPriorityState_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchActionForwardPriorityState = _SwL2ACLQosTemplateRuleL4SwitchActionForwardPriorityState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 29),
    _SwL2ACLQosTemplateRuleL4SwitchActionForwardPriorityState_Type()
)
swL2ACLQosTemplateRuleL4SwitchActionForwardPriorityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchActionForwardPriorityState.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchActionForwardPriority_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchActionForwardPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2ACLQosTemplateRuleL4SwitchActionForwardPriority_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchActionForwardPriority_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchActionForwardPriority = _SwL2ACLQosTemplateRuleL4SwitchActionForwardPriority_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 30),
    _SwL2ACLQosTemplateRuleL4SwitchActionForwardPriority_Type()
)
swL2ACLQosTemplateRuleL4SwitchActionForwardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchActionForwardPriority.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchActionForwardDscp_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchActionForwardDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwL2ACLQosTemplateRuleL4SwitchActionForwardDscp_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchActionForwardDscp_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchActionForwardDscp = _SwL2ACLQosTemplateRuleL4SwitchActionForwardDscp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 31),
    _SwL2ACLQosTemplateRuleL4SwitchActionForwardDscp_Type()
)
swL2ACLQosTemplateRuleL4SwitchActionForwardDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchActionForwardDscp.setStatus("current")
_SwL2ACLQosTemplateRuleL4SwitchActionRedirectIp_Type = IpAddress
_SwL2ACLQosTemplateRuleL4SwitchActionRedirectIp_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchActionRedirectIp = _SwL2ACLQosTemplateRuleL4SwitchActionRedirectIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 32),
    _SwL2ACLQosTemplateRuleL4SwitchActionRedirectIp_Type()
)
swL2ACLQosTemplateRuleL4SwitchActionRedirectIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchActionRedirectIp.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchActionRedirectDropUnreachable_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleL4SwitchActionRedirectDropUnreachable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("other", 1),
          ("true", 2))
    )


_SwL2ACLQosTemplateRuleL4SwitchActionRedirectDropUnreachable_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleL4SwitchActionRedirectDropUnreachable_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchActionRedirectDropUnreachable = _SwL2ACLQosTemplateRuleL4SwitchActionRedirectDropUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 33),
    _SwL2ACLQosTemplateRuleL4SwitchActionRedirectDropUnreachable_Type()
)
swL2ACLQosTemplateRuleL4SwitchActionRedirectDropUnreachable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchActionRedirectDropUnreachable.setStatus("current")


class _SwL2ACLQosTemplateRuleState_Type(Integer32):
    """Custom type swL2ACLQosTemplateRuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL2ACLQosTemplateRuleState_Type.__name__ = "Integer32"
_SwL2ACLQosTemplateRuleState_Object = MibTableColumn
swL2ACLQosTemplateRuleState = _SwL2ACLQosTemplateRuleState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 34),
    _SwL2ACLQosTemplateRuleState_Type()
)
swL2ACLQosTemplateRuleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleState.setStatus("current")


class _SwL2ACLQosTemplateRuleL4SwitchSessionTCPFlagsAll_Type(Bits):
    """Custom type swL2ACLQosTemplateRuleL4SwitchSessionTCPFlagsAll based on Bits"""
    namedValues = NamedValues(
        *(("ack", 4),
          ("fin", 0),
          ("psh", 3),
          ("rst", 2),
          ("syn", 1),
          ("urg", 5))
    )

_SwL2ACLQosTemplateRuleL4SwitchSessionTCPFlagsAll_Type.__name__ = "Bits"
_SwL2ACLQosTemplateRuleL4SwitchSessionTCPFlagsAll_Object = MibTableColumn
swL2ACLQosTemplateRuleL4SwitchSessionTCPFlagsAll = _SwL2ACLQosTemplateRuleL4SwitchSessionTCPFlagsAll_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 35),
    _SwL2ACLQosTemplateRuleL4SwitchSessionTCPFlagsAll_Type()
)
swL2ACLQosTemplateRuleL4SwitchSessionTCPFlagsAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleL4SwitchSessionTCPFlagsAll.setStatus("current")
_SwL2ACLQosTemplateRuleSecurityDstIp_Type = IpAddress
_SwL2ACLQosTemplateRuleSecurityDstIp_Object = MibTableColumn
swL2ACLQosTemplateRuleSecurityDstIp = _SwL2ACLQosTemplateRuleSecurityDstIp_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 5, 1, 36),
    _SwL2ACLQosTemplateRuleSecurityDstIp_Type()
)
swL2ACLQosTemplateRuleSecurityDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosTemplateRuleSecurityDstIp.setStatus("current")
_SwL2ACLQosDestinationIpFilterTable_Object = MibTable
swL2ACLQosDestinationIpFilterTable = _SwL2ACLQosDestinationIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 6)
)
if mibBuilder.loadTexts:
    swL2ACLQosDestinationIpFilterTable.setStatus("current")
_SwL2ACLQosDestinationIpFilterEntry_Object = MibTableRow
swL2ACLQosDestinationIpFilterEntry = _SwL2ACLQosDestinationIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 6, 1)
)
swL2ACLQosDestinationIpFilterEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2ACLQosDestinationIpFilterIpAddr"),
)
if mibBuilder.loadTexts:
    swL2ACLQosDestinationIpFilterEntry.setStatus("current")


class _SwL2ACLQosDestinationIpFilterIndex_Type(Integer32):
    """Custom type swL2ACLQosDestinationIpFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosDestinationIpFilterIndex_Type.__name__ = "Integer32"
_SwL2ACLQosDestinationIpFilterIndex_Object = MibTableColumn
swL2ACLQosDestinationIpFilterIndex = _SwL2ACLQosDestinationIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 6, 1, 1),
    _SwL2ACLQosDestinationIpFilterIndex_Type()
)
swL2ACLQosDestinationIpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosDestinationIpFilterIndex.setStatus("obsolete")
_SwL2ACLQosDestinationIpFilterIpAddr_Type = IpAddress
_SwL2ACLQosDestinationIpFilterIpAddr_Object = MibTableColumn
swL2ACLQosDestinationIpFilterIpAddr = _SwL2ACLQosDestinationIpFilterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 6, 1, 2),
    _SwL2ACLQosDestinationIpFilterIpAddr_Type()
)
swL2ACLQosDestinationIpFilterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosDestinationIpFilterIpAddr.setStatus("current")


class _SwL2ACLQosDestinationIpFilterState_Type(Integer32):
    """Custom type swL2ACLQosDestinationIpFilterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL2ACLQosDestinationIpFilterState_Type.__name__ = "Integer32"
_SwL2ACLQosDestinationIpFilterState_Object = MibTableColumn
swL2ACLQosDestinationIpFilterState = _SwL2ACLQosDestinationIpFilterState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 6, 1, 3),
    _SwL2ACLQosDestinationIpFilterState_Type()
)
swL2ACLQosDestinationIpFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosDestinationIpFilterState.setStatus("current")
_SwL2ACLQosFDBFilterTable_Object = MibTable
swL2ACLQosFDBFilterTable = _SwL2ACLQosFDBFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 7)
)
if mibBuilder.loadTexts:
    swL2ACLQosFDBFilterTable.setStatus("current")
_SwL2ACLQosFDBFilterEntry_Object = MibTableRow
swL2ACLQosFDBFilterEntry = _SwL2ACLQosFDBFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 7, 1)
)
swL2ACLQosFDBFilterEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2ACLQosFDBFilterVlanName"),
    (0, "SWL2MGMT-MIB", "swL2ACLQosFDBFilterMacAddress"),
)
if mibBuilder.loadTexts:
    swL2ACLQosFDBFilterEntry.setStatus("current")


class _SwL2ACLQosFDBFilterIndex_Type(Integer32):
    """Custom type swL2ACLQosFDBFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosFDBFilterIndex_Type.__name__ = "Integer32"
_SwL2ACLQosFDBFilterIndex_Object = MibTableColumn
swL2ACLQosFDBFilterIndex = _SwL2ACLQosFDBFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 7, 1, 1),
    _SwL2ACLQosFDBFilterIndex_Type()
)
swL2ACLQosFDBFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosFDBFilterIndex.setStatus("obsolete")


class _SwL2ACLQosFDBFilterVlanName_Type(DisplayString):
    """Custom type swL2ACLQosFDBFilterVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2ACLQosFDBFilterVlanName_Type.__name__ = "DisplayString"
_SwL2ACLQosFDBFilterVlanName_Object = MibTableColumn
swL2ACLQosFDBFilterVlanName = _SwL2ACLQosFDBFilterVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 7, 1, 2),
    _SwL2ACLQosFDBFilterVlanName_Type()
)
swL2ACLQosFDBFilterVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosFDBFilterVlanName.setStatus("current")
_SwL2ACLQosFDBFilterMacAddress_Type = MacAddress
_SwL2ACLQosFDBFilterMacAddress_Object = MibTableColumn
swL2ACLQosFDBFilterMacAddress = _SwL2ACLQosFDBFilterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 7, 1, 3),
    _SwL2ACLQosFDBFilterMacAddress_Type()
)
swL2ACLQosFDBFilterMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosFDBFilterMacAddress.setStatus("current")


class _SwL2ACLQosFDBFilterState_Type(Integer32):
    """Custom type swL2ACLQosFDBFilterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL2ACLQosFDBFilterState_Type.__name__ = "Integer32"
_SwL2ACLQosFDBFilterState_Object = MibTableColumn
swL2ACLQosFDBFilterState = _SwL2ACLQosFDBFilterState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 7, 1, 4),
    _SwL2ACLQosFDBFilterState_Type()
)
swL2ACLQosFDBFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosFDBFilterState.setStatus("current")


class _SwL2ACLQosIpFragmentFilterDropPkts_Type(Integer32):
    """Custom type swL2ACLQosIpFragmentFilterDropPkts based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2ACLQosIpFragmentFilterDropPkts_Type.__name__ = "Integer32"
_SwL2ACLQosIpFragmentFilterDropPkts_Object = MibScalar
swL2ACLQosIpFragmentFilterDropPkts = _SwL2ACLQosIpFragmentFilterDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 8),
    _SwL2ACLQosIpFragmentFilterDropPkts_Type()
)
swL2ACLQosIpFragmentFilterDropPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosIpFragmentFilterDropPkts.setStatus("current")
_SwL2ACLQosSchedulingTable_Object = MibTable
swL2ACLQosSchedulingTable = _SwL2ACLQosSchedulingTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 9)
)
if mibBuilder.loadTexts:
    swL2ACLQosSchedulingTable.setStatus("current")
_SwL2ACLQosSchedulingEntry_Object = MibTableRow
swL2ACLQosSchedulingEntry = _SwL2ACLQosSchedulingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 9, 1)
)
swL2ACLQosSchedulingEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2ACLQosSchedulingPortIndex"),
    (0, "SWL2MGMT-MIB", "swL2ACLQosSchedulingClassId"),
)
if mibBuilder.loadTexts:
    swL2ACLQosSchedulingEntry.setStatus("current")


class _SwL2ACLQosSchedulingPortIndex_Type(Integer32):
    """Custom type swL2ACLQosSchedulingPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosSchedulingPortIndex_Type.__name__ = "Integer32"
_SwL2ACLQosSchedulingPortIndex_Object = MibTableColumn
swL2ACLQosSchedulingPortIndex = _SwL2ACLQosSchedulingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 9, 1, 1),
    _SwL2ACLQosSchedulingPortIndex_Type()
)
swL2ACLQosSchedulingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosSchedulingPortIndex.setStatus("current")


class _SwL2ACLQosSchedulingClassId_Type(Integer32):
    """Custom type swL2ACLQosSchedulingClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2ACLQosSchedulingClassId_Type.__name__ = "Integer32"
_SwL2ACLQosSchedulingClassId_Object = MibTableColumn
swL2ACLQosSchedulingClassId = _SwL2ACLQosSchedulingClassId_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 9, 1, 2),
    _SwL2ACLQosSchedulingClassId_Type()
)
swL2ACLQosSchedulingClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosSchedulingClassId.setStatus("current")


class _SwL2ACLQosSchedulingWRRValue_Type(Integer32):
    """Custom type swL2ACLQosSchedulingWRRValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL2ACLQosSchedulingWRRValue_Type.__name__ = "Integer32"
_SwL2ACLQosSchedulingWRRValue_Object = MibTableColumn
swL2ACLQosSchedulingWRRValue = _SwL2ACLQosSchedulingWRRValue_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 9, 1, 3),
    _SwL2ACLQosSchedulingWRRValue_Type()
)
swL2ACLQosSchedulingWRRValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosSchedulingWRRValue.setStatus("current")
_SwL2ACLQosMacPriorityTable_Object = MibTable
swL2ACLQosMacPriorityTable = _SwL2ACLQosMacPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 10)
)
if mibBuilder.loadTexts:
    swL2ACLQosMacPriorityTable.setStatus("current")
_SwL2ACLQosMacPriorityEntry_Object = MibTableRow
swL2ACLQosMacPriorityEntry = _SwL2ACLQosMacPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 10, 1)
)
swL2ACLQosMacPriorityEntry.setIndexNames(
    (0, "SWL2MGMT-MIB", "swL2ACLQosMacPriorityVlanName"),
    (0, "SWL2MGMT-MIB", "swL2ACLQosMacPriorityDstMacAddress"),
)
if mibBuilder.loadTexts:
    swL2ACLQosMacPriorityEntry.setStatus("current")


class _SwL2ACLQosMacPriorityIndex_Type(Integer32):
    """Custom type swL2ACLQosMacPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2ACLQosMacPriorityIndex_Type.__name__ = "Integer32"
_SwL2ACLQosMacPriorityIndex_Object = MibTableColumn
swL2ACLQosMacPriorityIndex = _SwL2ACLQosMacPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 10, 1, 1),
    _SwL2ACLQosMacPriorityIndex_Type()
)
swL2ACLQosMacPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosMacPriorityIndex.setStatus("obsolete")


class _SwL2ACLQosMacPriorityVlanName_Type(DisplayString):
    """Custom type swL2ACLQosMacPriorityVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2ACLQosMacPriorityVlanName_Type.__name__ = "DisplayString"
_SwL2ACLQosMacPriorityVlanName_Object = MibTableColumn
swL2ACLQosMacPriorityVlanName = _SwL2ACLQosMacPriorityVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 10, 1, 2),
    _SwL2ACLQosMacPriorityVlanName_Type()
)
swL2ACLQosMacPriorityVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosMacPriorityVlanName.setStatus("current")
_SwL2ACLQosMacPriorityDstMacAddress_Type = MacAddress
_SwL2ACLQosMacPriorityDstMacAddress_Object = MibTableColumn
swL2ACLQosMacPriorityDstMacAddress = _SwL2ACLQosMacPriorityDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 10, 1, 3),
    _SwL2ACLQosMacPriorityDstMacAddress_Type()
)
swL2ACLQosMacPriorityDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2ACLQosMacPriorityDstMacAddress.setStatus("current")


class _SwL2ACLQosMacPriorityPriorityValue_Type(Integer32):
    """Custom type swL2ACLQosMacPriorityPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2ACLQosMacPriorityPriorityValue_Type.__name__ = "Integer32"
_SwL2ACLQosMacPriorityPriorityValue_Object = MibTableColumn
swL2ACLQosMacPriorityPriorityValue = _SwL2ACLQosMacPriorityPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 10, 1, 4),
    _SwL2ACLQosMacPriorityPriorityValue_Type()
)
swL2ACLQosMacPriorityPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosMacPriorityPriorityValue.setStatus("current")


class _SwL2ACLQosMacPriorityState_Type(Integer32):
    """Custom type swL2ACLQosMacPriorityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL2ACLQosMacPriorityState_Type.__name__ = "Integer32"
_SwL2ACLQosMacPriorityState_Object = MibTableColumn
swL2ACLQosMacPriorityState = _SwL2ACLQosMacPriorityState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 16, 10, 1, 5),
    _SwL2ACLQosMacPriorityState_Type()
)
swL2ACLQosMacPriorityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2ACLQosMacPriorityState.setStatus("current")
_SwL2MgmtPortMgmt_ObjectIdentity = ObjectIdentity
swL2MgmtPortMgmt = _SwL2MgmtPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 17)
)


class _SwL2MgmtPortCurrentLinkStatus_Type(Integer32):
    """Custom type swL2MgmtPortCurrentLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-fail", 3),
          ("link-pass", 2),
          ("other", 1))
    )


_SwL2MgmtPortCurrentLinkStatus_Type.__name__ = "Integer32"
_SwL2MgmtPortCurrentLinkStatus_Object = MibScalar
swL2MgmtPortCurrentLinkStatus = _SwL2MgmtPortCurrentLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 17, 1),
    _SwL2MgmtPortCurrentLinkStatus_Type()
)
swL2MgmtPortCurrentLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2MgmtPortCurrentLinkStatus.setStatus("current")


class _SwL2MgmtPortCurrentNwayStatus_Type(Integer32):
    """Custom type swL2MgmtPortCurrentNwayStatus based on Integer32"""
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
        *(("full-100Mbps", 5),
          ("full-10Mbps", 3),
          ("half-100Mbps", 4),
          ("half-10Mbps", 2),
          ("other", 1))
    )


_SwL2MgmtPortCurrentNwayStatus_Type.__name__ = "Integer32"
_SwL2MgmtPortCurrentNwayStatus_Object = MibScalar
swL2MgmtPortCurrentNwayStatus = _SwL2MgmtPortCurrentNwayStatus_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 17, 2),
    _SwL2MgmtPortCurrentNwayStatus_Type()
)
swL2MgmtPortCurrentNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2MgmtPortCurrentNwayStatus.setStatus("current")


class _SwL2MgmtPortAdminState_Type(Integer32):
    """Custom type swL2MgmtPortAdminState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2MgmtPortAdminState_Type.__name__ = "Integer32"
_SwL2MgmtPortAdminState_Object = MibScalar
swL2MgmtPortAdminState = _SwL2MgmtPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 17, 3),
    _SwL2MgmtPortAdminState_Type()
)
swL2MgmtPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MgmtPortAdminState.setStatus("current")


class _SwL2MgmtPortNwayState_Type(Integer32):
    """Custom type swL2MgmtPortNwayState based on Integer32"""
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
        *(("nway-disabled-100Mbps-Full", 6),
          ("nway-disabled-100Mbps-Half", 5),
          ("nway-disabled-10Mbps-Full", 4),
          ("nway-disabled-10Mbps-Half", 3),
          ("nway-enabled", 2),
          ("other", 1))
    )


_SwL2MgmtPortNwayState_Type.__name__ = "Integer32"
_SwL2MgmtPortNwayState_Object = MibScalar
swL2MgmtPortNwayState = _SwL2MgmtPortNwayState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 17, 4),
    _SwL2MgmtPortNwayState_Type()
)
swL2MgmtPortNwayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MgmtPortNwayState.setStatus("current")


class _SwL2MgmtPortFlowCtrlState_Type(Integer32):
    """Custom type swL2MgmtPortFlowCtrlState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2MgmtPortFlowCtrlState_Type.__name__ = "Integer32"
_SwL2MgmtPortFlowCtrlState_Object = MibScalar
swL2MgmtPortFlowCtrlState = _SwL2MgmtPortFlowCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 17, 5),
    _SwL2MgmtPortFlowCtrlState_Type()
)
swL2MgmtPortFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MgmtPortFlowCtrlState.setStatus("current")


class _SwL2MgmtPortLinkUpDownTrapEnable_Type(Integer32):
    """Custom type swL2MgmtPortLinkUpDownTrapEnable based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwL2MgmtPortLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_SwL2MgmtPortLinkUpDownTrapEnable_Object = MibScalar
swL2MgmtPortLinkUpDownTrapEnable = _SwL2MgmtPortLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 17, 6),
    _SwL2MgmtPortLinkUpDownTrapEnable_Type()
)
swL2MgmtPortLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MgmtPortLinkUpDownTrapEnable.setStatus("current")

# Managed Objects groups


# Notification objects

managementPortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    managementPortLinkUp.setStatus(
        ""
    )

managementPortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    managementPortLinkDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWL2MGMT-MIB",
    **{"PortList": PortList,
       "VlanIndex": VlanIndex,
       "swL2MgmtMIB": swL2MgmtMIB,
       "managementPortLinkUp": managementPortLinkUp,
       "managementPortLinkDown": managementPortLinkDown,
       "swL2DevMgmt": swL2DevMgmt,
       "swL2DevInfo": swL2DevInfo,
       "swDevInfoSystemUpTime": swDevInfoSystemUpTime,
       "swDevInfoTotalNumOfPort": swDevInfoTotalNumOfPort,
       "swDevInfoNumOfPortInUse": swDevInfoNumOfPortInUse,
       "swDevInfoConsoleInUse": swDevInfoConsoleInUse,
       "swDevInfoFrontPanelLedStatus": swDevInfoFrontPanelLedStatus,
       "swL2DevCtrlUpDownloadState": swL2DevCtrlUpDownloadState,
       "swDevInfoSaveCfg": swDevInfoSaveCfg,
       "swL2DevCtrl": swL2DevCtrl,
       "swL2DevCtrlStpState": swL2DevCtrlStpState,
       "swL2DevCtrlIGMPSnooping": swL2DevCtrlIGMPSnooping,
       "swL2DevCtrlRmonState": swL2DevCtrlRmonState,
       "swL2DevCtrlUpDownloadImageFileName": swL2DevCtrlUpDownloadImageFileName,
       "swL2DevCtrlUpDownloadImageSourceAddr": swL2DevCtrlUpDownloadImageSourceAddr,
       "swL2DevCtrlUpDownloadImage": swL2DevCtrlUpDownloadImage,
       "swL2DevCtrlSaveCfg": swL2DevCtrlSaveCfg,
       "swL2DevCtrlCleanAllStatisticCounter": swL2DevCtrlCleanAllStatisticCounter,
       "swL2DevCtrlStpForwardBPDU": swL2DevCtrlStpForwardBPDU,
       "swL2DevAlarm": swL2DevAlarm,
       "swL2DevAlarmNewRoot": swL2DevAlarmNewRoot,
       "swL2DevAlarmTopologyChange": swL2DevAlarmTopologyChange,
       "swL2DevAlarmLinkChange": swL2DevAlarmLinkChange,
       "swL2UnitMgmt": swL2UnitMgmt,
       "swL2UnitCtrl": swL2UnitCtrl,
       "swL2ModuleMgmt": swL2ModuleMgmt,
       "swL2PortMgmt": swL2PortMgmt,
       "swL2PortInfoTable": swL2PortInfoTable,
       "swL2PortInfoEntry": swL2PortInfoEntry,
       "swL2PortInfoPortIndex": swL2PortInfoPortIndex,
       "swL2PortInfoUnitIndex": swL2PortInfoUnitIndex,
       "swL2PortInfoType": swL2PortInfoType,
       "swL2PortInfoLinkStatus": swL2PortInfoLinkStatus,
       "swL2PortInfoNwayStatus": swL2PortInfoNwayStatus,
       "swL2PortCtrlTable": swL2PortCtrlTable,
       "swL2PortCtrlEntry": swL2PortCtrlEntry,
       "swL2PortCtrlPortIndex": swL2PortCtrlPortIndex,
       "swL2PortCtrlUnitIndex": swL2PortCtrlUnitIndex,
       "swL2PortCtrlAdminState": swL2PortCtrlAdminState,
       "swL2PortCtrlNwayState": swL2PortCtrlNwayState,
       "swL2PortCtrlFlowCtrlState": swL2PortCtrlFlowCtrlState,
       "swL2PortCtrlAddressLearningState": swL2PortCtrlAddressLearningState,
       "swL2PortUtilTable": swL2PortUtilTable,
       "swL2PortUtilEntry": swL2PortUtilEntry,
       "swL2PortUtilPortIndex": swL2PortUtilPortIndex,
       "swL2PortUtilTxSec": swL2PortUtilTxSec,
       "swL2PortUtilRxSec": swL2PortUtilRxSec,
       "swL2PortUtilUtilization": swL2PortUtilUtilization,
       "swL2FilterMgmt": swL2FilterMgmt,
       "swL2FilterAddrConfig": swL2FilterAddrConfig,
       "swL2FilterAddrMaxSupportedEntries": swL2FilterAddrMaxSupportedEntries,
       "swL2FilterAddrCurrentTotalEntries": swL2FilterAddrCurrentTotalEntries,
       "swL2FilterAddrCtrlTable": swL2FilterAddrCtrlTable,
       "swL2FilterAddrCtrlEntry": swL2FilterAddrCtrlEntry,
       "swL2FilterAddrMacIndex": swL2FilterAddrMacIndex,
       "swL2FilterAddrState": swL2FilterAddrState,
       "swL2VlanMgmt": swL2VlanMgmt,
       "swL2StaticVlanTable": swL2StaticVlanTable,
       "swL2StaticVlanEntry": swL2StaticVlanEntry,
       "swL2StaticVlanIndex": swL2StaticVlanIndex,
       "swL2StaticVlanName": swL2StaticVlanName,
       "swL2StaticVlanType": swL2StaticVlanType,
       "swL2StaticVlanProtocolId": swL2StaticVlanProtocolId,
       "swL2StaticVlanIpSubnetAddr": swL2StaticVlanIpSubnetAddr,
       "swL2StaticVlanIpSubnetMask": swL2StaticVlanIpSubnetMask,
       "swL2StaticVlanUserDefinedPid": swL2StaticVlanUserDefinedPid,
       "swL2StaticVlanEncap": swL2StaticVlanEncap,
       "swL2StaticVlanUserPriority": swL2StaticVlanUserPriority,
       "swL2StaticVlanEgressPorts": swL2StaticVlanEgressPorts,
       "swL2StaticVlanUntaggedPorts": swL2StaticVlanUntaggedPorts,
       "swL2StaticVlanStatus": swL2StaticVlanStatus,
       "swL2StaticVlanIpSubnetArpClassId": swL2StaticVlanIpSubnetArpClassId,
       "swL2VlanPortTable": swL2VlanPortTable,
       "swL2VlanPortEntry": swL2VlanPortEntry,
       "swL2VlanPortIndex": swL2VlanPortIndex,
       "swL2VlanPortPvid": swL2VlanPortPvid,
       "swL2VlanPortIngressChecking": swL2VlanPortIngressChecking,
       "swL2TrunkMgmt": swL2TrunkMgmt,
       "swL2TrunkMaxSupportedEntries": swL2TrunkMaxSupportedEntries,
       "swL2TrunkCurrentNumEntries": swL2TrunkCurrentNumEntries,
       "swL2TrunkCtrlTable": swL2TrunkCtrlTable,
       "swL2TrunkCtrlEntry": swL2TrunkCtrlEntry,
       "swL2TrunkIndex": swL2TrunkIndex,
       "swL2TrunkName": swL2TrunkName,
       "swL2TrunkMasterPort": swL2TrunkMasterPort,
       "swL2TrunkMember": swL2TrunkMember,
       "swL2TrunkFloodingPort": swL2TrunkFloodingPort,
       "swL2TrunkState": swL2TrunkState,
       "swL2TrunkBPDU8600InterState": swL2TrunkBPDU8600InterState,
       "swL2TrunkAlgorithm": swL2TrunkAlgorithm,
       "swL2MirrorMgmt": swL2MirrorMgmt,
       "swL2MirrorLogicTargetPort": swL2MirrorLogicTargetPort,
       "swL2MirrorPortSourceIngress": swL2MirrorPortSourceIngress,
       "swL2MirrorPortSourceEgress": swL2MirrorPortSourceEgress,
       "swL2MirrorPortState": swL2MirrorPortState,
       "swL2IGMPMgmt": swL2IGMPMgmt,
       "swL2IGMPMaxSupportedVlans": swL2IGMPMaxSupportedVlans,
       "swL2IGMPMaxIpGroupNumPerVlan": swL2IGMPMaxIpGroupNumPerVlan,
       "swL2IGMPCtrlTable": swL2IGMPCtrlTable,
       "swL2IGMPCtrlEntry": swL2IGMPCtrlEntry,
       "swL2IGMPCtrlVid": swL2IGMPCtrlVid,
       "swL2IGMPQueryInterval": swL2IGMPQueryInterval,
       "swL2IGMPMaxResponseTime": swL2IGMPMaxResponseTime,
       "swL2IGMPRobustness": swL2IGMPRobustness,
       "swL2IGMPLastMemberQueryInterval": swL2IGMPLastMemberQueryInterval,
       "swL2IGMPHostTimeout": swL2IGMPHostTimeout,
       "swL2IGMPRouteTimeout": swL2IGMPRouteTimeout,
       "swL2IGMPLeaveTimer": swL2IGMPLeaveTimer,
       "swL2IGMPQueryState": swL2IGMPQueryState,
       "swL2IGMPCurrentState": swL2IGMPCurrentState,
       "swL2IGMPCtrlState": swL2IGMPCtrlState,
       "swL2IGMPQueryInfoTable": swL2IGMPQueryInfoTable,
       "swL2IGMPQueryInfoEntry": swL2IGMPQueryInfoEntry,
       "swL2IGMPInfoVid": swL2IGMPInfoVid,
       "swL2IGMPInfoQueryCount": swL2IGMPInfoQueryCount,
       "swL2IGMPInfoTxQueryCount": swL2IGMPInfoTxQueryCount,
       "swL2IGMPGroupTable": swL2IGMPGroupTable,
       "swL2IGMPGroupEntry": swL2IGMPGroupEntry,
       "swL2IGMPVid": swL2IGMPVid,
       "swL2IGMPGroupIpAddr": swL2IGMPGroupIpAddr,
       "swL2IGMPMacAddr": swL2IGMPMacAddr,
       "swL2IGMPPortMap": swL2IGMPPortMap,
       "swL2IGMPIpGroupReportCount": swL2IGMPIpGroupReportCount,
       "swL2IGMPForwardTable": swL2IGMPForwardTable,
       "swL2IGMPForwardEntry": swL2IGMPForwardEntry,
       "swL2IGMPForwardVid": swL2IGMPForwardVid,
       "swL2IGMPForwardGroupIpAddr": swL2IGMPForwardGroupIpAddr,
       "swL2IGMPForwardPortMap": swL2IGMPForwardPortMap,
       "swL2IGMPRPTable": swL2IGMPRPTable,
       "swL2IGMPRPEntry": swL2IGMPRPEntry,
       "swL2IGMPRPVid": swL2IGMPRPVid,
       "swL2IGMPRPStaticRouterPort": swL2IGMPRPStaticRouterPort,
       "swL2IGMPRPDynamicRouterPort": swL2IGMPRPDynamicRouterPort,
       "swL2IGMPMulticastRouterOnly": swL2IGMPMulticastRouterOnly,
       "swL2IGMPGroupPortTable": swL2IGMPGroupPortTable,
       "swL2IGMPGroupPortEntry": swL2IGMPGroupPortEntry,
       "swL2IGMPPortMember": swL2IGMPPortMember,
       "swL2IGMPPortAgingTime": swL2IGMPPortAgingTime,
       "swL2IGMPMulticastFilter": swL2IGMPMulticastFilter,
       "swL2TrafficMgmt": swL2TrafficMgmt,
       "swL2TrafficCtrlTable": swL2TrafficCtrlTable,
       "swL2TrafficCtrlEntry": swL2TrafficCtrlEntry,
       "swL2TrafficCtrlGroupIndex": swL2TrafficCtrlGroupIndex,
       "swL2TrafficCtrlUnitIndex": swL2TrafficCtrlUnitIndex,
       "swL2TrafficCtrlBMStormthreshold": swL2TrafficCtrlBMStormthreshold,
       "swL2TrafficCtrlBcastStormCtrl": swL2TrafficCtrlBcastStormCtrl,
       "swL2TrafficCtrlMcastStormCtrl": swL2TrafficCtrlMcastStormCtrl,
       "swL2TrafficCtrlDlfStormCtrl": swL2TrafficCtrlDlfStormCtrl,
       "swL2QosMgmt": swL2QosMgmt,
       "swL2QosSchedulingTable": swL2QosSchedulingTable,
       "swL2QosSchedulingEntry": swL2QosSchedulingEntry,
       "swL2QosSchedulingClassId": swL2QosSchedulingClassId,
       "swL2QosSchedulingMaxPkts": swL2QosSchedulingMaxPkts,
       "swL2QosSchedulingMaxLatency": swL2QosSchedulingMaxLatency,
       "swL2QosPriorityTable": swL2QosPriorityTable,
       "swL2QosPriorityEntry": swL2QosPriorityEntry,
       "swL2QosPriorityType": swL2QosPriorityType,
       "swL2QosPriorityValue": swL2QosPriorityValue,
       "swL2QosPriorityPriority": swL2QosPriorityPriority,
       "swL2QosPriorityPriorityState": swL2QosPriorityPriorityState,
       "swL2QosPriorityReplaceDscp": swL2QosPriorityReplaceDscp,
       "swL2QosPriorityReplaceDscpState": swL2QosPriorityReplaceDscpState,
       "swL2QosPriorityReplacePriority": swL2QosPriorityReplacePriority,
       "swL2QosPriorityState": swL2QosPriorityState,
       "swL2MgmtMIBTraps": swL2MgmtMIBTraps,
       "swL2StormCtrlMgmt": swL2StormCtrlMgmt,
       "swL2StormCtrlTable": swL2StormCtrlTable,
       "swL2StormCtrlEntry": swL2StormCtrlEntry,
       "swL2StormCtrlPortIndex": swL2StormCtrlPortIndex,
       "swL2StormCtrlBcastStormCtrl": swL2StormCtrlBcastStormCtrl,
       "swL2StormCtrlMcastStormCtrl": swL2StormCtrlMcastStormCtrl,
       "swL2StormCtrlBMStormThreshold": swL2StormCtrlBMStormThreshold,
       "swL2StormCtrlDlfState": swL2StormCtrlDlfState,
       "swL2StormCtrlDlfThreshold": swL2StormCtrlDlfThreshold,
       "swL2CpuRateLimitTable": swL2CpuRateLimitTable,
       "swL2CpuRateLimitEntry": swL2CpuRateLimitEntry,
       "swL2CpuRateLimitPortIndex": swL2CpuRateLimitPortIndex,
       "swL2CpuRateLimitState": swL2CpuRateLimitState,
       "swL2CpuRateLimitBcastThreshold": swL2CpuRateLimitBcastThreshold,
       "swL2CpuRateLimitMcastThreshold": swL2CpuRateLimitMcastThreshold,
       "swL2CpuUtilization": swL2CpuUtilization,
       "swL2ACLQosMgmt": swL2ACLQosMgmt,
       "swL2ACLQosTemplate1Mode": swL2ACLQosTemplate1Mode,
       "swL2ACLQosTemplate2Mode": swL2ACLQosTemplate2Mode,
       "swL2ACLQosFlowClassifierTable": swL2ACLQosFlowClassifierTable,
       "swL2ACLQosFlowClassifierEntry": swL2ACLQosFlowClassifierEntry,
       "swL2ACLQosFlowClassifierTemplateId": swL2ACLQosFlowClassifierTemplateId,
       "swL2ACLQosFlowClassifierCurrentMode": swL2ACLQosFlowClassifierCurrentMode,
       "swL2ACLQosFlowClassifierSecuritySrcMask": swL2ACLQosFlowClassifierSecuritySrcMask,
       "swL2ACLQosFlowClassifierQosFlavor": swL2ACLQosFlowClassifierQosFlavor,
       "swL2ACLQosFlowClassifierL4SwitchTCPDstIp": swL2ACLQosFlowClassifierL4SwitchTCPDstIp,
       "swL2ACLQosFlowClassifierL4SwitchTCPSrcIp": swL2ACLQosFlowClassifierL4SwitchTCPSrcIp,
       "swL2ACLQosFlowClassifierL4SwitchTCPTos": swL2ACLQosFlowClassifierL4SwitchTCPTos,
       "swL2ACLQosFlowClassifierL4SwitchTCPDstPort": swL2ACLQosFlowClassifierL4SwitchTCPDstPort,
       "swL2ACLQosFlowClassifierL4SwitchTCPSrcPort": swL2ACLQosFlowClassifierL4SwitchTCPSrcPort,
       "swL2ACLQosFlowClassifierL4SwitchTCPFlags": swL2ACLQosFlowClassifierL4SwitchTCPFlags,
       "swL2ACLQosFlowClassifierL4SwitchUDPDstIp": swL2ACLQosFlowClassifierL4SwitchUDPDstIp,
       "swL2ACLQosFlowClassifierL4SwitchUDPSrcIp": swL2ACLQosFlowClassifierL4SwitchUDPSrcIp,
       "swL2ACLQosFlowClassifierL4SwitchUDPTos": swL2ACLQosFlowClassifierL4SwitchUDPTos,
       "swL2ACLQosFlowClassifierL4SwitchUDPDstPort": swL2ACLQosFlowClassifierL4SwitchUDPDstPort,
       "swL2ACLQosFlowClassifierL4SwitchUDPSrcPort": swL2ACLQosFlowClassifierL4SwitchUDPSrcPort,
       "swL2ACLQosFlowClassifierL4SwitchOtherDstIp": swL2ACLQosFlowClassifierL4SwitchOtherDstIp,
       "swL2ACLQosFlowClassifierL4SwitchOtherSrcIp": swL2ACLQosFlowClassifierL4SwitchOtherSrcIp,
       "swL2ACLQosFlowClassifierL4SwitchOtherTos": swL2ACLQosFlowClassifierL4SwitchOtherTos,
       "swL2ACLQosFlowClassifierL4SwitchOtherL4Protocol": swL2ACLQosFlowClassifierL4SwitchOtherL4Protocol,
       "swL2ACLQosFlowClassifierL4SwitchOtherICMPMessage": swL2ACLQosFlowClassifierL4SwitchOtherICMPMessage,
       "swL2ACLQosFlowClassifierL4SwitchOtherIGMPType": swL2ACLQosFlowClassifierL4SwitchOtherIGMPType,
       "swL2ACLQosFlowClassifierActiveRuleNumber": swL2ACLQosFlowClassifierActiveRuleNumber,
       "swL2ACLQosFlowClassifierSecurityDstMask": swL2ACLQosFlowClassifierSecurityDstMask,
       "swL2ACLQosFlowClassifierVlanTable": swL2ACLQosFlowClassifierVlanTable,
       "swL2ACLQosFlowClassifierVlanEntry": swL2ACLQosFlowClassifierVlanEntry,
       "swL2ACLQosFlowClassifierVlanTemplateId": swL2ACLQosFlowClassifierVlanTemplateId,
       "swL2ACLQosFlowClassifierVlanVlanName": swL2ACLQosFlowClassifierVlanVlanName,
       "swL2ACLQosFlowClassifierVlanState": swL2ACLQosFlowClassifierVlanState,
       "swL2ACLQosTemplateRuleTable": swL2ACLQosTemplateRuleTable,
       "swL2ACLQosTemplateRuleEntry": swL2ACLQosTemplateRuleEntry,
       "swL2ACLQosTemplateRuleTemplateId": swL2ACLQosTemplateRuleTemplateId,
       "swL2ACLQosTemplateRuleIndex": swL2ACLQosTemplateRuleIndex,
       "swL2ACLQosTemplateRuleMode": swL2ACLQosTemplateRuleMode,
       "swL2ACLQosTemplateRuleSecuritySrcIp": swL2ACLQosTemplateRuleSecuritySrcIp,
       "swL2ACLQosTemplateRuleQosFlavor": swL2ACLQosTemplateRuleQosFlavor,
       "swL2ACLQosTemplateRuleQosValue": swL2ACLQosTemplateRuleQosValue,
       "swL2ACLQosTemplateRuleQosPriority": swL2ACLQosTemplateRuleQosPriority,
       "swL2ACLQosTemplateRuleQosDscp": swL2ACLQosTemplateRuleQosDscp,
       "swL2ACLQosTemplateRuleL4SwitchSessionType": swL2ACLQosTemplateRuleL4SwitchSessionType,
       "swL2ACLQosTemplateRuleL4SwitchSessionTCPDstIp": swL2ACLQosTemplateRuleL4SwitchSessionTCPDstIp,
       "swL2ACLQosTemplateRuleL4SwitchSessionTCPSrcIp": swL2ACLQosTemplateRuleL4SwitchSessionTCPSrcIp,
       "swL2ACLQosTemplateRuleL4SwitchSessionTCPTos": swL2ACLQosTemplateRuleL4SwitchSessionTCPTos,
       "swL2ACLQosTemplateRuleL4SwitchSessionTCPDstPort": swL2ACLQosTemplateRuleL4SwitchSessionTCPDstPort,
       "swL2ACLQosTemplateRuleL4SwitchSessionTCPSrcPort": swL2ACLQosTemplateRuleL4SwitchSessionTCPSrcPort,
       "swL2ACLQosTemplateRuleL4SwitchSessionTCPFlags": swL2ACLQosTemplateRuleL4SwitchSessionTCPFlags,
       "swL2ACLQosTemplateRuleL4SwitchSessionUDPDstIp": swL2ACLQosTemplateRuleL4SwitchSessionUDPDstIp,
       "swL2ACLQosTemplateRuleL4SwitchSessionUDPSrcIp": swL2ACLQosTemplateRuleL4SwitchSessionUDPSrcIp,
       "swL2ACLQosTemplateRuleL4SwitchSessionUDPTos": swL2ACLQosTemplateRuleL4SwitchSessionUDPTos,
       "swL2ACLQosTemplateRuleL4SwitchSessionUDPDstPort": swL2ACLQosTemplateRuleL4SwitchSessionUDPDstPort,
       "swL2ACLQosTemplateRuleL4SwitchSessionUDPSrcPort": swL2ACLQosTemplateRuleL4SwitchSessionUDPSrcPort,
       "swL2ACLQosTemplateRuleL4SwitchSessionOtherDstIp": swL2ACLQosTemplateRuleL4SwitchSessionOtherDstIp,
       "swL2ACLQosTemplateRuleL4SwitchSessionOtherSrcIp": swL2ACLQosTemplateRuleL4SwitchSessionOtherSrcIp,
       "swL2ACLQosTemplateRuleL4SwitchSessionOtherTos": swL2ACLQosTemplateRuleL4SwitchSessionOtherTos,
       "swL2ACLQosTemplateRuleL4SwitchSessionOtherL4Protocol": swL2ACLQosTemplateRuleL4SwitchSessionOtherL4Protocol,
       "swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPType": swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPType,
       "swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPCode": swL2ACLQosTemplateRuleL4SwitchSessionOtherICMPCode,
       "swL2ACLQosTemplateRuleL4SwitchSessionOtherIGMPType": swL2ACLQosTemplateRuleL4SwitchSessionOtherIGMPType,
       "swL2ACLQosTemplateRuleL4SwitchActionType": swL2ACLQosTemplateRuleL4SwitchActionType,
       "swL2ACLQosTemplateRuleL4SwitchActionForwardPriorityState": swL2ACLQosTemplateRuleL4SwitchActionForwardPriorityState,
       "swL2ACLQosTemplateRuleL4SwitchActionForwardPriority": swL2ACLQosTemplateRuleL4SwitchActionForwardPriority,
       "swL2ACLQosTemplateRuleL4SwitchActionForwardDscp": swL2ACLQosTemplateRuleL4SwitchActionForwardDscp,
       "swL2ACLQosTemplateRuleL4SwitchActionRedirectIp": swL2ACLQosTemplateRuleL4SwitchActionRedirectIp,
       "swL2ACLQosTemplateRuleL4SwitchActionRedirectDropUnreachable": swL2ACLQosTemplateRuleL4SwitchActionRedirectDropUnreachable,
       "swL2ACLQosTemplateRuleState": swL2ACLQosTemplateRuleState,
       "swL2ACLQosTemplateRuleL4SwitchSessionTCPFlagsAll": swL2ACLQosTemplateRuleL4SwitchSessionTCPFlagsAll,
       "swL2ACLQosTemplateRuleSecurityDstIp": swL2ACLQosTemplateRuleSecurityDstIp,
       "swL2ACLQosDestinationIpFilterTable": swL2ACLQosDestinationIpFilterTable,
       "swL2ACLQosDestinationIpFilterEntry": swL2ACLQosDestinationIpFilterEntry,
       "swL2ACLQosDestinationIpFilterIndex": swL2ACLQosDestinationIpFilterIndex,
       "swL2ACLQosDestinationIpFilterIpAddr": swL2ACLQosDestinationIpFilterIpAddr,
       "swL2ACLQosDestinationIpFilterState": swL2ACLQosDestinationIpFilterState,
       "swL2ACLQosFDBFilterTable": swL2ACLQosFDBFilterTable,
       "swL2ACLQosFDBFilterEntry": swL2ACLQosFDBFilterEntry,
       "swL2ACLQosFDBFilterIndex": swL2ACLQosFDBFilterIndex,
       "swL2ACLQosFDBFilterVlanName": swL2ACLQosFDBFilterVlanName,
       "swL2ACLQosFDBFilterMacAddress": swL2ACLQosFDBFilterMacAddress,
       "swL2ACLQosFDBFilterState": swL2ACLQosFDBFilterState,
       "swL2ACLQosIpFragmentFilterDropPkts": swL2ACLQosIpFragmentFilterDropPkts,
       "swL2ACLQosSchedulingTable": swL2ACLQosSchedulingTable,
       "swL2ACLQosSchedulingEntry": swL2ACLQosSchedulingEntry,
       "swL2ACLQosSchedulingPortIndex": swL2ACLQosSchedulingPortIndex,
       "swL2ACLQosSchedulingClassId": swL2ACLQosSchedulingClassId,
       "swL2ACLQosSchedulingWRRValue": swL2ACLQosSchedulingWRRValue,
       "swL2ACLQosMacPriorityTable": swL2ACLQosMacPriorityTable,
       "swL2ACLQosMacPriorityEntry": swL2ACLQosMacPriorityEntry,
       "swL2ACLQosMacPriorityIndex": swL2ACLQosMacPriorityIndex,
       "swL2ACLQosMacPriorityVlanName": swL2ACLQosMacPriorityVlanName,
       "swL2ACLQosMacPriorityDstMacAddress": swL2ACLQosMacPriorityDstMacAddress,
       "swL2ACLQosMacPriorityPriorityValue": swL2ACLQosMacPriorityPriorityValue,
       "swL2ACLQosMacPriorityState": swL2ACLQosMacPriorityState,
       "swL2MgmtPortMgmt": swL2MgmtPortMgmt,
       "swL2MgmtPortCurrentLinkStatus": swL2MgmtPortCurrentLinkStatus,
       "swL2MgmtPortCurrentNwayStatus": swL2MgmtPortCurrentNwayStatus,
       "swL2MgmtPortAdminState": swL2MgmtPortAdminState,
       "swL2MgmtPortNwayState": swL2MgmtPortNwayState,
       "swL2MgmtPortFlowCtrlState": swL2MgmtPortFlowCtrlState,
       "swL2MgmtPortLinkUpDownTrapEnable": swL2MgmtPortLinkUpDownTrapEnable}
)

# SNMP MIB module (DGS3427-L2MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS3427-L2MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:45 2024
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

(AgentNotifyLevel,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "AgentNotifyLevel")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(dgs3427,) = mibBuilder.importSymbols(
    "SW34XXPRIMGMT-MIB",
    "dgs3427")


# MODULE-IDENTITY

swL2MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )





class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



class IANAifMauAutoNegCapBits(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_SwL2DevMgmt_ObjectIdentity = ObjectIdentity
swL2DevMgmt = _SwL2DevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1)
)
_SwL2DevInfo_ObjectIdentity = ObjectIdentity
swL2DevInfo = _SwL2DevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1)
)


class _SwDevInfoTotalNumOfPort_Type(Integer32):
    """Custom type swDevInfoTotalNumOfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwDevInfoTotalNumOfPort_Type.__name__ = "Integer32"
_SwDevInfoTotalNumOfPort_Object = MibScalar
swDevInfoTotalNumOfPort = _SwDevInfoTotalNumOfPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 2),
    _SwDevInfoNumOfPortInUse_Type()
)
swDevInfoNumOfPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoNumOfPortInUse.setStatus("current")
_SwDevModuleInfoTable_Object = MibTable
swDevModuleInfoTable = _SwDevModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    swDevModuleInfoTable.setStatus("current")
_SwDevModuleInfoEntry_Object = MibTableRow
swDevModuleInfoEntry = _SwDevModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 3, 1)
)
swDevModuleInfoEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swDevModuleInfoUnitID"),
    (0, "DGS3427-L2MGMT-MIB", "swDevModuleInfoModuleID"),
)
if mibBuilder.loadTexts:
    swDevModuleInfoEntry.setStatus("current")


class _SwDevModuleInfoUnitID_Type(Integer32):
    """Custom type swDevModuleInfoUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SwDevModuleInfoUnitID_Type.__name__ = "Integer32"
_SwDevModuleInfoUnitID_Object = MibTableColumn
swDevModuleInfoUnitID = _SwDevModuleInfoUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 3, 1, 1),
    _SwDevModuleInfoUnitID_Type()
)
swDevModuleInfoUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevModuleInfoUnitID.setStatus("current")


class _SwDevModuleInfoModuleID_Type(Integer32):
    """Custom type swDevModuleInfoModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SwDevModuleInfoModuleID_Type.__name__ = "Integer32"
_SwDevModuleInfoModuleID_Object = MibTableColumn
swDevModuleInfoModuleID = _SwDevModuleInfoModuleID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 3, 1, 2),
    _SwDevModuleInfoModuleID_Type()
)
swDevModuleInfoModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevModuleInfoModuleID.setStatus("current")


class _SwDevModuleInfoModuleName_Type(DisplayString):
    """Custom type swDevModuleInfoModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwDevModuleInfoModuleName_Type.__name__ = "DisplayString"
_SwDevModuleInfoModuleName_Object = MibTableColumn
swDevModuleInfoModuleName = _SwDevModuleInfoModuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 3, 1, 3),
    _SwDevModuleInfoModuleName_Type()
)
swDevModuleInfoModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevModuleInfoModuleName.setStatus("current")


class _SwDevModuleInfoReversion_Type(DisplayString):
    """Custom type swDevModuleInfoReversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SwDevModuleInfoReversion_Type.__name__ = "DisplayString"
_SwDevModuleInfoReversion_Object = MibTableColumn
swDevModuleInfoReversion = _SwDevModuleInfoReversion_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 3, 1, 4),
    _SwDevModuleInfoReversion_Type()
)
swDevModuleInfoReversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevModuleInfoReversion.setStatus("current")


class _SwDevModuleInfoSerial_Type(DisplayString):
    """Custom type swDevModuleInfoSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwDevModuleInfoSerial_Type.__name__ = "DisplayString"
_SwDevModuleInfoSerial_Object = MibTableColumn
swDevModuleInfoSerial = _SwDevModuleInfoSerial_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 3, 1, 5),
    _SwDevModuleInfoSerial_Type()
)
swDevModuleInfoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevModuleInfoSerial.setStatus("current")


class _SwDevModuleInfoDescription_Type(DisplayString):
    """Custom type swDevModuleInfoDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwDevModuleInfoDescription_Type.__name__ = "DisplayString"
_SwDevModuleInfoDescription_Object = MibTableColumn
swDevModuleInfoDescription = _SwDevModuleInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 3, 1, 6),
    _SwDevModuleInfoDescription_Type()
)
swDevModuleInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevModuleInfoDescription.setStatus("current")


class _SwDevInfoBootPromVersion_Type(DisplayString):
    """Custom type swDevInfoBootPromVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwDevInfoBootPromVersion_Type.__name__ = "DisplayString"
_SwDevInfoBootPromVersion_Object = MibScalar
swDevInfoBootPromVersion = _SwDevInfoBootPromVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 4),
    _SwDevInfoBootPromVersion_Type()
)
swDevInfoBootPromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoBootPromVersion.setStatus("current")


class _SwDevInfoFirmwareVersion_Type(DisplayString):
    """Custom type swDevInfoFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwDevInfoFirmwareVersion_Type.__name__ = "DisplayString"
_SwDevInfoFirmwareVersion_Object = MibScalar
swDevInfoFirmwareVersion = _SwDevInfoFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 5),
    _SwDevInfoFirmwareVersion_Type()
)
swDevInfoFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoFirmwareVersion.setStatus("current")


class _SwDevInfoFrontPanelLedStatus_Type(OctetString):
    """Custom type swDevInfoFrontPanelLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwDevInfoFrontPanelLedStatus_Type.__name__ = "OctetString"
_SwDevInfoFrontPanelLedStatus_Object = MibScalar
swDevInfoFrontPanelLedStatus = _SwDevInfoFrontPanelLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 1, 6),
    _SwDevInfoFrontPanelLedStatus_Type()
)
swDevInfoFrontPanelLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoFrontPanelLedStatus.setStatus("current")
_SwL2DevCtrl_ObjectIdentity = ObjectIdentity
swL2DevCtrl = _SwL2DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 2),
    _SwL2DevCtrlIGMPSnooping_Type()
)
swL2DevCtrlIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIGMPSnooping.setStatus("current")


class _SwL2DevCtrlIGMPSnoopingMcstRTOnly_Type(Integer32):
    """Custom type swL2DevCtrlIGMPSnoopingMcstRTOnly based on Integer32"""
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


_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Type.__name__ = "Integer32"
_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Object = MibScalar
swL2DevCtrlIGMPSnoopingMcstRTOnly = _SwL2DevCtrlIGMPSnoopingMcstRTOnly_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 3),
    _SwL2DevCtrlIGMPSnoopingMcstRTOnly_Type()
)
swL2DevCtrlIGMPSnoopingMcstRTOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIGMPSnoopingMcstRTOnly.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 4),
    _SwL2DevCtrlRmonState_Type()
)
swL2DevCtrlRmonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlRmonState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 5),
    _SwL2DevCtrlCleanAllStatisticCounter_Type()
)
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCleanAllStatisticCounter.setStatus("current")
_SwL2DevCtrlVlanIdOfFDBTbl_Type = VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object = MibScalar
swL2DevCtrlVlanIdOfFDBTbl = _SwL2DevCtrlVlanIdOfFDBTbl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 6),
    _SwL2DevCtrlVlanIdOfFDBTbl_Type()
)
swL2DevCtrlVlanIdOfFDBTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlVlanIdOfFDBTbl.setStatus("current")
_SwL2DevCtrlManagementVlanId_Type = VlanId
_SwL2DevCtrlManagementVlanId_Object = MibScalar
swL2DevCtrlManagementVlanId = _SwL2DevCtrlManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 7),
    _SwL2DevCtrlManagementVlanId_Type()
)
swL2DevCtrlManagementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlManagementVlanId.setStatus("current")


class _SwL2MACNotifyState_Type(Integer32):
    """Custom type swL2MACNotifyState based on Integer32"""
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


_SwL2MACNotifyState_Type.__name__ = "Integer32"
_SwL2MACNotifyState_Object = MibScalar
swL2MACNotifyState = _SwL2MACNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 8),
    _SwL2MACNotifyState_Type()
)
swL2MACNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MACNotifyState.setStatus("current")


class _SwL2MACNotifyHistorySize_Type(Integer32):
    """Custom type swL2MACNotifyHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_SwL2MACNotifyHistorySize_Type.__name__ = "Integer32"
_SwL2MACNotifyHistorySize_Object = MibScalar
swL2MACNotifyHistorySize = _SwL2MACNotifyHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 9),
    _SwL2MACNotifyHistorySize_Type()
)
swL2MACNotifyHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MACNotifyHistorySize.setStatus("current")


class _SwL2MACNotifyInterval_Type(Integer32):
    """Custom type swL2MACNotifyInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SwL2MACNotifyInterval_Type.__name__ = "Integer32"
_SwL2MACNotifyInterval_Object = MibScalar
swL2MACNotifyInterval = _SwL2MACNotifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 10),
    _SwL2MACNotifyInterval_Type()
)
swL2MACNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MACNotifyInterval.setStatus("current")
_SwL2DevCtrlWeb_ObjectIdentity = ObjectIdentity
swL2DevCtrlWeb = _SwL2DevCtrlWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 13)
)


class _SwL2DevCtrlWebState_Type(Integer32):
    """Custom type swL2DevCtrlWebState based on Integer32"""
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


_SwL2DevCtrlWebState_Type.__name__ = "Integer32"
_SwL2DevCtrlWebState_Object = MibScalar
swL2DevCtrlWebState = _SwL2DevCtrlWebState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 13, 1),
    _SwL2DevCtrlWebState_Type()
)
swL2DevCtrlWebState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlWebState.setStatus("current")


class _SwL2DevCtrlWebTcpPort_Type(Integer32):
    """Custom type swL2DevCtrlWebTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2DevCtrlWebTcpPort_Type.__name__ = "Integer32"
_SwL2DevCtrlWebTcpPort_Object = MibScalar
swL2DevCtrlWebTcpPort = _SwL2DevCtrlWebTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 13, 2),
    _SwL2DevCtrlWebTcpPort_Type()
)
swL2DevCtrlWebTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlWebTcpPort.setStatus("current")
_SwL2DevCtrlTelnet_ObjectIdentity = ObjectIdentity
swL2DevCtrlTelnet = _SwL2DevCtrlTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 14)
)


class _SwL2DevCtrlTelnetState_Type(Integer32):
    """Custom type swL2DevCtrlTelnetState based on Integer32"""
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


_SwL2DevCtrlTelnetState_Type.__name__ = "Integer32"
_SwL2DevCtrlTelnetState_Object = MibScalar
swL2DevCtrlTelnetState = _SwL2DevCtrlTelnetState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 14, 1),
    _SwL2DevCtrlTelnetState_Type()
)
swL2DevCtrlTelnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlTelnetState.setStatus("current")


class _SwL2DevCtrlTelnetTcpPort_Type(Integer32):
    """Custom type swL2DevCtrlTelnetTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2DevCtrlTelnetTcpPort_Type.__name__ = "Integer32"
_SwL2DevCtrlTelnetTcpPort_Object = MibScalar
swL2DevCtrlTelnetTcpPort = _SwL2DevCtrlTelnetTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 14, 2),
    _SwL2DevCtrlTelnetTcpPort_Type()
)
swL2DevCtrlTelnetTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlTelnetTcpPort.setStatus("current")


class _SwL2DevCtrlIpAutoconfig_Type(Integer32):
    """Custom type swL2DevCtrlIpAutoconfig based on Integer32"""
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


_SwL2DevCtrlIpAutoconfig_Type.__name__ = "Integer32"
_SwL2DevCtrlIpAutoconfig_Object = MibScalar
swL2DevCtrlIpAutoconfig = _SwL2DevCtrlIpAutoconfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 15),
    _SwL2DevCtrlIpAutoconfig_Type()
)
swL2DevCtrlIpAutoconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIpAutoconfig.setStatus("current")


class _SwL2DevCtrlClipagingState_Type(Integer32):
    """Custom type swL2DevCtrlClipagingState based on Integer32"""
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


_SwL2DevCtrlClipagingState_Type.__name__ = "Integer32"
_SwL2DevCtrlClipagingState_Object = MibScalar
swL2DevCtrlClipagingState = _SwL2DevCtrlClipagingState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 17),
    _SwL2DevCtrlClipagingState_Type()
)
swL2DevCtrlClipagingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlClipagingState.setStatus("current")


class _SwL2DevCtrlLLDPState_Type(Integer32):
    """Custom type swL2DevCtrlLLDPState based on Integer32"""
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


_SwL2DevCtrlLLDPState_Type.__name__ = "Integer32"
_SwL2DevCtrlLLDPState_Object = MibScalar
swL2DevCtrlLLDPState = _SwL2DevCtrlLLDPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 18),
    _SwL2DevCtrlLLDPState_Type()
)
swL2DevCtrlLLDPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlLLDPState.setStatus("current")


class _SwL2DevCtrlLLDPForwardMessageState_Type(Integer32):
    """Custom type swL2DevCtrlLLDPForwardMessageState based on Integer32"""
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


_SwL2DevCtrlLLDPForwardMessageState_Type.__name__ = "Integer32"
_SwL2DevCtrlLLDPForwardMessageState_Object = MibScalar
swL2DevCtrlLLDPForwardMessageState = _SwL2DevCtrlLLDPForwardMessageState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 2, 19),
    _SwL2DevCtrlLLDPForwardMessageState_Type()
)
swL2DevCtrlLLDPForwardMessageState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlLLDPForwardMessageState.setStatus("current")
_SwL2DevAlarm_ObjectIdentity = ObjectIdentity
swL2DevAlarm = _SwL2DevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 3)
)


class _SwL2DevAlarmNewRoot_Type(Integer32):
    """Custom type swL2DevAlarmNewRoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_SwL2DevAlarmNewRoot_Type.__name__ = "Integer32"
_SwL2DevAlarmNewRoot_Object = MibScalar
swL2DevAlarmNewRoot = _SwL2DevAlarmNewRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 3, 1),
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
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_SwL2DevAlarmTopologyChange_Type.__name__ = "Integer32"
_SwL2DevAlarmTopologyChange_Object = MibScalar
swL2DevAlarmTopologyChange = _SwL2DevAlarmTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 3, 2),
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
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_SwL2DevAlarmLinkChange_Type.__name__ = "Integer32"
_SwL2DevAlarmLinkChange_Object = MibScalar
swL2DevAlarmLinkChange = _SwL2DevAlarmLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 1, 3, 3),
    _SwL2DevAlarmLinkChange_Type()
)
swL2DevAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmLinkChange.setStatus("current")
_SwL2MultiFilter_ObjectIdentity = ObjectIdentity
swL2MultiFilter = _SwL2MultiFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 2)
)
_SwL2MultiFilterTable_Object = MibTable
swL2MultiFilterTable = _SwL2MultiFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swL2MultiFilterTable.setStatus("current")
_SwL2MultiFilterEntry_Object = MibTableRow
swL2MultiFilterEntry = _SwL2MultiFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 2, 1, 1)
)
swL2MultiFilterEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2MultiFilterVid"),
)
if mibBuilder.loadTexts:
    swL2MultiFilterEntry.setStatus("current")


class _SwL2MultiFilterVid_Type(Integer32):
    """Custom type swL2MultiFilterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2MultiFilterVid_Type.__name__ = "Integer32"
_SwL2MultiFilterVid_Object = MibTableColumn
swL2MultiFilterVid = _SwL2MultiFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 2, 1, 1, 1),
    _SwL2MultiFilterVid_Type()
)
swL2MultiFilterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2MultiFilterVid.setStatus("current")


class _SwL2MultiFilterMode_Type(Integer32):
    """Custom type swL2MultiFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter-unregistered-groups", 3),
          ("forward-all-groups", 1),
          ("forward-unregistered-groups", 2))
    )


_SwL2MultiFilterMode_Type.__name__ = "Integer32"
_SwL2MultiFilterMode_Object = MibTableColumn
swL2MultiFilterMode = _SwL2MultiFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 2, 1, 1, 2),
    _SwL2MultiFilterMode_Type()
)
swL2MultiFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MultiFilterMode.setStatus("current")
_SwL2PortMgmt_ObjectIdentity = ObjectIdentity
swL2PortMgmt = _SwL2PortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3)
)
_SwL2PortInfoTable_Object = MibTable
swL2PortInfoTable = _SwL2PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    swL2PortInfoTable.setStatus("current")
_SwL2PortInfoEntry_Object = MibTableRow
swL2PortInfoEntry = _SwL2PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 1, 1)
)
swL2PortInfoEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2PortInfoPortIndex"),
    (0, "DGS3427-L2MGMT-MIB", "swL2PortInfoMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 1, 1, 1),
    _SwL2PortInfoPortIndex_Type()
)
swL2PortInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoPortIndex.setStatus("current")


class _SwL2PortInfoMediumType_Type(Integer32):
    """Custom type swL2PortInfoMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_SwL2PortInfoMediumType_Type.__name__ = "Integer32"
_SwL2PortInfoMediumType_Object = MibTableColumn
swL2PortInfoMediumType = _SwL2PortInfoMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 1, 1, 2),
    _SwL2PortInfoMediumType_Type()
)
swL2PortInfoMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoMediumType.setStatus("current")


class _SwL2PortInfoUnitID_Type(Integer32):
    """Custom type swL2PortInfoUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortInfoUnitID_Type.__name__ = "Integer32"
_SwL2PortInfoUnitID_Object = MibTableColumn
swL2PortInfoUnitID = _SwL2PortInfoUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 1, 1, 3),
    _SwL2PortInfoUnitID_Type()
)
swL2PortInfoUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoUnitID.setStatus("current")


class _SwL2PortInfoType_Type(Integer32):
    """Custom type swL2PortInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("portType-1000Base-T", 4),
          ("portType-1000Base-X", 5),
          ("portType-100Base-T", 2),
          ("portType-100Base-X", 3),
          ("portType-10GBase-CX4", 7),
          ("portType-10GBase-R", 6),
          ("portType-SIO", 8),
          ("portType-module-empty", 9),
          ("portType-none", 0),
          ("portType-user-last", 10))
    )


_SwL2PortInfoType_Type.__name__ = "Integer32"
_SwL2PortInfoType_Object = MibTableColumn
swL2PortInfoType = _SwL2PortInfoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 1, 1, 5),
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("empty", 17),
          ("err-disabled", 18),
          ("full-100Mbps-8023x", 5),
          ("full-100Mbps-none", 6),
          ("full-10Gigabps-8023x", 13),
          ("full-10Gigabps-none", 14),
          ("full-10Mbps-8023x", 1),
          ("full-10Mbps-none", 2),
          ("full-1Gigabps-8023x", 9),
          ("full-1Gigabps-none", 10),
          ("half-100Mbps-backp", 7),
          ("half-100Mbps-none", 8),
          ("half-10Gigabps-8023x", 15),
          ("half-10Gigabps-none", 16),
          ("half-10Mbps-backp", 3),
          ("half-10Mbps-none", 4),
          ("half-1Gigabps-backp", 11),
          ("half-1Gigabps-none", 12),
          ("link-down", 0))
    )


_SwL2PortInfoNwayStatus_Type.__name__ = "Integer32"
_SwL2PortInfoNwayStatus_Object = MibTableColumn
swL2PortInfoNwayStatus = _SwL2PortInfoNwayStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 1, 1, 6),
    _SwL2PortInfoNwayStatus_Type()
)
swL2PortInfoNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoNwayStatus.setStatus("current")


class _SwL2PortInfoErrDisReason_Type(Integer32):
    """Custom type swL2PortInfoErrDisReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("err-none", 1),
          ("lbd-control", 3),
          ("storm-control", 2))
    )


_SwL2PortInfoErrDisReason_Type.__name__ = "Integer32"
_SwL2PortInfoErrDisReason_Object = MibTableColumn
swL2PortInfoErrDisReason = _SwL2PortInfoErrDisReason_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 1, 1, 7),
    _SwL2PortInfoErrDisReason_Type()
)
swL2PortInfoErrDisReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoErrDisReason.setStatus("current")
_SwL2PortCtrlTable_Object = MibTable
swL2PortCtrlTable = _SwL2PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    swL2PortCtrlTable.setStatus("current")
_SwL2PortCtrlEntry_Object = MibTableRow
swL2PortCtrlEntry = _SwL2PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2, 1)
)
swL2PortCtrlEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2PortCtrlPortIndex"),
    (0, "DGS3427-L2MGMT-MIB", "swL2PortCtrlMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2, 1, 1),
    _SwL2PortCtrlPortIndex_Type()
)
swL2PortCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlPortIndex.setStatus("current")


class _SwL2PortCtrlMediumType_Type(Integer32):
    """Custom type swL2PortCtrlMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_SwL2PortCtrlMediumType_Type.__name__ = "Integer32"
_SwL2PortCtrlMediumType_Object = MibTableColumn
swL2PortCtrlMediumType = _SwL2PortCtrlMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2, 1, 2),
    _SwL2PortCtrlMediumType_Type()
)
swL2PortCtrlMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlMediumType.setStatus("current")


class _SwL2PortCtrlUnitIndex_Type(Integer32):
    """Custom type swL2PortCtrlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortCtrlUnitIndex_Type.__name__ = "Integer32"
_SwL2PortCtrlUnitIndex_Object = MibTableColumn
swL2PortCtrlUnitIndex = _SwL2PortCtrlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2, 1, 4),
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("nway-disabled-100Mbps-Full", 6),
          ("nway-disabled-100Mbps-Half", 5),
          ("nway-disabled-10Mbps-Full", 4),
          ("nway-disabled-10Mbps-Half", 3),
          ("nway-disabled-1Gigabps-Full", 8),
          ("nway-disabled-1Gigabps-Full-master", 9),
          ("nway-disabled-1Gigabps-Full-slave", 10),
          ("nway-enabled", 2),
          ("other", 1))
    )


_SwL2PortCtrlNwayState_Type.__name__ = "Integer32"
_SwL2PortCtrlNwayState_Object = MibTableColumn
swL2PortCtrlNwayState = _SwL2PortCtrlNwayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2, 1, 6),
    _SwL2PortCtrlFlowCtrlState_Type()
)
swL2PortCtrlFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlFlowCtrlState.setStatus("current")


class _SwL2PortCtrlLockState_Type(Integer32):
    """Custom type swL2PortCtrlLockState based on Integer32"""
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


_SwL2PortCtrlLockState_Type.__name__ = "Integer32"
_SwL2PortCtrlLockState_Object = MibTableColumn
swL2PortCtrlLockState = _SwL2PortCtrlLockState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2, 1, 7),
    _SwL2PortCtrlLockState_Type()
)
swL2PortCtrlLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlLockState.setStatus("current")


class _SwL2PortCtrlMACNotifyState_Type(Integer32):
    """Custom type swL2PortCtrlMACNotifyState based on Integer32"""
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


_SwL2PortCtrlMACNotifyState_Type.__name__ = "Integer32"
_SwL2PortCtrlMACNotifyState_Object = MibTableColumn
swL2PortCtrlMACNotifyState = _SwL2PortCtrlMACNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2, 1, 8),
    _SwL2PortCtrlMACNotifyState_Type()
)
swL2PortCtrlMACNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlMACNotifyState.setStatus("current")


class _SwL2PortCtrlAutoNegRestart_Type(Integer32):
    """Custom type swL2PortCtrlAutoNegRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norestart", 2),
          ("restart", 1))
    )


_SwL2PortCtrlAutoNegRestart_Type.__name__ = "Integer32"
_SwL2PortCtrlAutoNegRestart_Object = MibTableColumn
swL2PortCtrlAutoNegRestart = _SwL2PortCtrlAutoNegRestart_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2, 1, 11),
    _SwL2PortCtrlAutoNegRestart_Type()
)
swL2PortCtrlAutoNegRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAutoNegRestart.setStatus("current")
_SwL2PortCtrlAutoNegCapAdvertisedBits_Type = IANAifMauAutoNegCapBits
_SwL2PortCtrlAutoNegCapAdvertisedBits_Object = MibTableColumn
swL2PortCtrlAutoNegCapAdvertisedBits = _SwL2PortCtrlAutoNegCapAdvertisedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 2, 1, 12),
    _SwL2PortCtrlAutoNegCapAdvertisedBits_Type()
)
swL2PortCtrlAutoNegCapAdvertisedBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAutoNegCapAdvertisedBits.setStatus("current")


class _SwL2PortCtrlJumboFrame_Type(Integer32):
    """Custom type swL2PortCtrlJumboFrame based on Integer32"""
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


_SwL2PortCtrlJumboFrame_Type.__name__ = "Integer32"
_SwL2PortCtrlJumboFrame_Object = MibScalar
swL2PortCtrlJumboFrame = _SwL2PortCtrlJumboFrame_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 3),
    _SwL2PortCtrlJumboFrame_Type()
)
swL2PortCtrlJumboFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlJumboFrame.setStatus("current")
_SwL2PortCtrlJumboFrameMaxSize_Type = Integer32
_SwL2PortCtrlJumboFrameMaxSize_Object = MibScalar
swL2PortCtrlJumboFrameMaxSize = _SwL2PortCtrlJumboFrameMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 4),
    _SwL2PortCtrlJumboFrameMaxSize_Type()
)
swL2PortCtrlJumboFrameMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlJumboFrameMaxSize.setStatus("current")
_SwL2PortCounterCtrlTable_Object = MibTable
swL2PortCounterCtrlTable = _SwL2PortCounterCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 6)
)
if mibBuilder.loadTexts:
    swL2PortCounterCtrlTable.setStatus("current")
_SwL2PortCounterCtrlEntry_Object = MibTableRow
swL2PortCounterCtrlEntry = _SwL2PortCounterCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 6, 1)
)
swL2PortCounterCtrlEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2PortCounterCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortCounterCtrlEntry.setStatus("current")


class _SwL2PortCounterCtrlPortIndex_Type(Integer32):
    """Custom type swL2PortCounterCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortCounterCtrlPortIndex_Type.__name__ = "Integer32"
_SwL2PortCounterCtrlPortIndex_Object = MibTableColumn
swL2PortCounterCtrlPortIndex = _SwL2PortCounterCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 6, 1, 1),
    _SwL2PortCounterCtrlPortIndex_Type()
)
swL2PortCounterCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCounterCtrlPortIndex.setStatus("current")


class _SwL2PortCounterClearCtrl_Type(Integer32):
    """Custom type swL2PortCounterClearCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwL2PortCounterClearCtrl_Type.__name__ = "Integer32"
_SwL2PortCounterClearCtrl_Object = MibTableColumn
swL2PortCounterClearCtrl = _SwL2PortCounterClearCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 6, 1, 2),
    _SwL2PortCounterClearCtrl_Type()
)
swL2PortCounterClearCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCounterClearCtrl.setStatus("current")
_SwL2PortAutoNegInfoTable_Object = MibTable
swL2PortAutoNegInfoTable = _SwL2PortAutoNegInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoTable.setStatus("current")
_SwL2PortAutoNegInfoEntry_Object = MibTableRow
swL2PortAutoNegInfoEntry = _SwL2PortAutoNegInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 8, 1)
)
swL2PortAutoNegInfoEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2PortAutoNegInfoPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoEntry.setStatus("current")


class _SwL2PortAutoNegInfoPortIndex_Type(Integer32):
    """Custom type swL2PortAutoNegInfoPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortAutoNegInfoPortIndex_Type.__name__ = "Integer32"
_SwL2PortAutoNegInfoPortIndex_Object = MibTableColumn
swL2PortAutoNegInfoPortIndex = _SwL2PortAutoNegInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 8, 1, 1),
    _SwL2PortAutoNegInfoPortIndex_Type()
)
swL2PortAutoNegInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoPortIndex.setStatus("current")


class _SwL2PortAutoNegInfoAdminStatus_Type(Integer32):
    """Custom type swL2PortAutoNegInfoAdminStatus based on Integer32"""
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


_SwL2PortAutoNegInfoAdminStatus_Type.__name__ = "Integer32"
_SwL2PortAutoNegInfoAdminStatus_Object = MibTableColumn
swL2PortAutoNegInfoAdminStatus = _SwL2PortAutoNegInfoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 8, 1, 2),
    _SwL2PortAutoNegInfoAdminStatus_Type()
)
swL2PortAutoNegInfoAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoAdminStatus.setStatus("current")
_SwL2PortAutoNegInfoCapabilityBits_Type = IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapabilityBits_Object = MibTableColumn
swL2PortAutoNegInfoCapabilityBits = _SwL2PortAutoNegInfoCapabilityBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 8, 1, 3),
    _SwL2PortAutoNegInfoCapabilityBits_Type()
)
swL2PortAutoNegInfoCapabilityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoCapabilityBits.setStatus("current")
_SwL2PortAutoNegInfoCapAdvertisedBits_Type = IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapAdvertisedBits_Object = MibTableColumn
swL2PortAutoNegInfoCapAdvertisedBits = _SwL2PortAutoNegInfoCapAdvertisedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 8, 1, 4),
    _SwL2PortAutoNegInfoCapAdvertisedBits_Type()
)
swL2PortAutoNegInfoCapAdvertisedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoCapAdvertisedBits.setStatus("current")
_SwL2PortAutoNegInfoCapReceivedBits_Type = IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapReceivedBits_Object = MibTableColumn
swL2PortAutoNegInfoCapReceivedBits = _SwL2PortAutoNegInfoCapReceivedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 8, 1, 5),
    _SwL2PortAutoNegInfoCapReceivedBits_Type()
)
swL2PortAutoNegInfoCapReceivedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoCapReceivedBits.setStatus("current")
_SwL2PortDropCounterTable_Object = MibTable
swL2PortDropCounterTable = _SwL2PortDropCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 9)
)
if mibBuilder.loadTexts:
    swL2PortDropCounterTable.setStatus("current")
_SwL2PortDropCounterEntry_Object = MibTableRow
swL2PortDropCounterEntry = _SwL2PortDropCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 9, 1)
)
swL2PortDropCounterEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2PortDropCounterPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortDropCounterEntry.setStatus("current")


class _SwL2PortDropCounterPortIndex_Type(Integer32):
    """Custom type swL2PortDropCounterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortDropCounterPortIndex_Type.__name__ = "Integer32"
_SwL2PortDropCounterPortIndex_Object = MibTableColumn
swL2PortDropCounterPortIndex = _SwL2PortDropCounterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 9, 1, 1),
    _SwL2PortDropCounterPortIndex_Type()
)
swL2PortDropCounterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortDropCounterPortIndex.setStatus("current")
_SwL2PortBufferFullDrops_Type = Counter32
_SwL2PortBufferFullDrops_Object = MibTableColumn
swL2PortBufferFullDrops = _SwL2PortBufferFullDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 9, 1, 2),
    _SwL2PortBufferFullDrops_Type()
)
swL2PortBufferFullDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortBufferFullDrops.setStatus("current")
_SwL2PortACLDrops_Type = Counter32
_SwL2PortACLDrops_Object = MibTableColumn
swL2PortACLDrops = _SwL2PortACLDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 9, 1, 3),
    _SwL2PortACLDrops_Type()
)
swL2PortACLDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortACLDrops.setStatus("current")
_SwL2PortMulticastDrops_Type = Counter32
_SwL2PortMulticastDrops_Object = MibTableColumn
swL2PortMulticastDrops = _SwL2PortMulticastDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 9, 1, 4),
    _SwL2PortMulticastDrops_Type()
)
swL2PortMulticastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortMulticastDrops.setStatus("current")
_SwL2PortVLANIngressDrops_Type = Counter32
_SwL2PortVLANIngressDrops_Object = MibTableColumn
swL2PortVLANIngressDrops = _SwL2PortVLANIngressDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 3, 9, 1, 5),
    _SwL2PortVLANIngressDrops_Type()
)
swL2PortVLANIngressDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortVLANIngressDrops.setStatus("current")
_SwL2QOSMgmt_ObjectIdentity = ObjectIdentity
swL2QOSMgmt = _SwL2QOSMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6)
)
_SwL2QOSBandwidthControlTable_Object = MibTable
swL2QOSBandwidthControlTable = _SwL2QOSBandwidthControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    swL2QOSBandwidthControlTable.setStatus("current")
_SwL2QOSBandwidthControlEntry_Object = MibTableRow
swL2QOSBandwidthControlEntry = _SwL2QOSBandwidthControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 1, 1)
)
swL2QOSBandwidthControlEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2QOSBandwidthPortIndex"),
)
if mibBuilder.loadTexts:
    swL2QOSBandwidthControlEntry.setStatus("current")


class _SwL2QOSBandwidthPortIndex_Type(Integer32):
    """Custom type swL2QOSBandwidthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_SwL2QOSBandwidthPortIndex_Type.__name__ = "Integer32"
_SwL2QOSBandwidthPortIndex_Object = MibTableColumn
swL2QOSBandwidthPortIndex = _SwL2QOSBandwidthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 1, 1, 1),
    _SwL2QOSBandwidthPortIndex_Type()
)
swL2QOSBandwidthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthPortIndex.setStatus("current")


class _SwL2QOSBandwidthRxRate_Type(Integer32):
    """Custom type swL2QOSBandwidthRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 10000000),
    )


_SwL2QOSBandwidthRxRate_Type.__name__ = "Integer32"
_SwL2QOSBandwidthRxRate_Object = MibTableColumn
swL2QOSBandwidthRxRate = _SwL2QOSBandwidthRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 1, 1, 2),
    _SwL2QOSBandwidthRxRate_Type()
)
swL2QOSBandwidthRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRxRate.setStatus("current")


class _SwL2QOSBandwidthTxRate_Type(Integer32):
    """Custom type swL2QOSBandwidthTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 10000000),
    )


_SwL2QOSBandwidthTxRate_Type.__name__ = "Integer32"
_SwL2QOSBandwidthTxRate_Object = MibTableColumn
swL2QOSBandwidthTxRate = _SwL2QOSBandwidthTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 1, 1, 3),
    _SwL2QOSBandwidthTxRate_Type()
)
swL2QOSBandwidthTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSBandwidthTxRate.setStatus("current")
_SwL2QOSBandwidthRadiusRxRate_Type = Integer32
_SwL2QOSBandwidthRadiusRxRate_Object = MibTableColumn
swL2QOSBandwidthRadiusRxRate = _SwL2QOSBandwidthRadiusRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 1, 1, 4),
    _SwL2QOSBandwidthRadiusRxRate_Type()
)
swL2QOSBandwidthRadiusRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRadiusRxRate.setStatus("current")
_SwL2QOSBandwidthRadiusTxRate_Type = Integer32
_SwL2QOSBandwidthRadiusTxRate_Object = MibTableColumn
swL2QOSBandwidthRadiusTxRate = _SwL2QOSBandwidthRadiusTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 1, 1, 5),
    _SwL2QOSBandwidthRadiusTxRate_Type()
)
swL2QOSBandwidthRadiusTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRadiusTxRate.setStatus("current")
_SwL2QOSSchedulingTable_Object = MibTable
swL2QOSSchedulingTable = _SwL2QOSSchedulingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    swL2QOSSchedulingTable.setStatus("current")
_SwL2QOSSchedulingEntry_Object = MibTableRow
swL2QOSSchedulingEntry = _SwL2QOSSchedulingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 2, 1)
)
swL2QOSSchedulingEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2QOSSchedulingClassIndex"),
)
if mibBuilder.loadTexts:
    swL2QOSSchedulingEntry.setStatus("current")


class _SwL2QOSSchedulingClassIndex_Type(Integer32):
    """Custom type swL2QOSSchedulingClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2QOSSchedulingClassIndex_Type.__name__ = "Integer32"
_SwL2QOSSchedulingClassIndex_Object = MibTableColumn
swL2QOSSchedulingClassIndex = _SwL2QOSSchedulingClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 2, 1, 1),
    _SwL2QOSSchedulingClassIndex_Type()
)
swL2QOSSchedulingClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSSchedulingClassIndex.setStatus("current")


class _SwL2QOSSchedulingMaxPkts_Type(Integer32):
    """Custom type swL2QOSSchedulingMaxPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SwL2QOSSchedulingMaxPkts_Type.__name__ = "Integer32"
_SwL2QOSSchedulingMaxPkts_Object = MibTableColumn
swL2QOSSchedulingMaxPkts = _SwL2QOSSchedulingMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 2, 1, 2),
    _SwL2QOSSchedulingMaxPkts_Type()
)
swL2QOSSchedulingMaxPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSSchedulingMaxPkts.setStatus("current")


class _SwL2QOSSchedulingMechanism_Type(Integer32):
    """Custom type swL2QOSSchedulingMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("roundrobin", 2),
          ("strict", 1),
          ("weightfair", 3))
    )


_SwL2QOSSchedulingMechanism_Type.__name__ = "Integer32"
_SwL2QOSSchedulingMechanism_Object = MibTableColumn
swL2QOSSchedulingMechanism = _SwL2QOSSchedulingMechanism_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 2, 1, 3),
    _SwL2QOSSchedulingMechanism_Type()
)
swL2QOSSchedulingMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSSchedulingMechanism.setStatus("current")
_SwL2QOS8021pUserPriorityTable_Object = MibTable
swL2QOS8021pUserPriorityTable = _SwL2QOS8021pUserPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 3)
)
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityTable.setStatus("current")
_SwL2QOS8021pUserPriorityEntry_Object = MibTableRow
swL2QOS8021pUserPriorityEntry = _SwL2QOS8021pUserPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 3, 1)
)
swL2QOS8021pUserPriorityEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2QOS8021pUserPriorityIndex"),
)
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityEntry.setStatus("current")


class _SwL2QOS8021pUserPriorityIndex_Type(Integer32):
    """Custom type swL2QOS8021pUserPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2QOS8021pUserPriorityIndex_Type.__name__ = "Integer32"
_SwL2QOS8021pUserPriorityIndex_Object = MibTableColumn
swL2QOS8021pUserPriorityIndex = _SwL2QOS8021pUserPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 3, 1, 1),
    _SwL2QOS8021pUserPriorityIndex_Type()
)
swL2QOS8021pUserPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityIndex.setStatus("current")


class _SwL2QOS8021pUserPriorityClass_Type(Integer32):
    """Custom type swL2QOS8021pUserPriorityClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_SwL2QOS8021pUserPriorityClass_Type.__name__ = "Integer32"
_SwL2QOS8021pUserPriorityClass_Object = MibTableColumn
swL2QOS8021pUserPriorityClass = _SwL2QOS8021pUserPriorityClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 3, 1, 2),
    _SwL2QOS8021pUserPriorityClass_Type()
)
swL2QOS8021pUserPriorityClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityClass.setStatus("current")
_SwL2QOS8021pDefaultPriorityTable_Object = MibTable
swL2QOS8021pDefaultPriorityTable = _SwL2QOS8021pDefaultPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 4)
)
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityTable.setStatus("current")
_SwL2QOS8021pDefaultPriorityEntry_Object = MibTableRow
swL2QOS8021pDefaultPriorityEntry = _SwL2QOS8021pDefaultPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 4, 1)
)
swL2QOS8021pDefaultPriorityEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2QOS8021pDefaultPriorityIndex"),
)
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityEntry.setStatus("current")


class _SwL2QOS8021pDefaultPriorityIndex_Type(Integer32):
    """Custom type swL2QOS8021pDefaultPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_SwL2QOS8021pDefaultPriorityIndex_Type.__name__ = "Integer32"
_SwL2QOS8021pDefaultPriorityIndex_Object = MibTableColumn
swL2QOS8021pDefaultPriorityIndex = _SwL2QOS8021pDefaultPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 4, 1, 1),
    _SwL2QOS8021pDefaultPriorityIndex_Type()
)
swL2QOS8021pDefaultPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityIndex.setStatus("current")


class _SwL2QOS8021pDefaultPriority_Type(Integer32):
    """Custom type swL2QOS8021pDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2QOS8021pDefaultPriority_Type.__name__ = "Integer32"
_SwL2QOS8021pDefaultPriority_Object = MibTableColumn
swL2QOS8021pDefaultPriority = _SwL2QOS8021pDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 4, 1, 2),
    _SwL2QOS8021pDefaultPriority_Type()
)
swL2QOS8021pDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriority.setStatus("current")
_SwL2QOS8021pRadiusPriority_Type = Integer32
_SwL2QOS8021pRadiusPriority_Object = MibTableColumn
swL2QOS8021pRadiusPriority = _SwL2QOS8021pRadiusPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 4, 1, 3),
    _SwL2QOS8021pRadiusPriority_Type()
)
swL2QOS8021pRadiusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOS8021pRadiusPriority.setStatus("current")


class _SwL2QOSSchedulingMechanismCtrl_Type(Integer32):
    """Custom type swL2QOSSchedulingMechanismCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("roundrobin", 2),
          ("strict", 1),
          ("weightfair", 3))
    )


_SwL2QOSSchedulingMechanismCtrl_Type.__name__ = "Integer32"
_SwL2QOSSchedulingMechanismCtrl_Object = MibScalar
swL2QOSSchedulingMechanismCtrl = _SwL2QOSSchedulingMechanismCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 5),
    _SwL2QOSSchedulingMechanismCtrl_Type()
)
swL2QOSSchedulingMechanismCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSSchedulingMechanismCtrl.setStatus("current")


class _SwL2QOSHolPreventionCtrl_Type(Integer32):
    """Custom type swL2QOSHolPreventionCtrl based on Integer32"""
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


_SwL2QOSHolPreventionCtrl_Type.__name__ = "Integer32"
_SwL2QOSHolPreventionCtrl_Object = MibScalar
swL2QOSHolPreventionCtrl = _SwL2QOSHolPreventionCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 6, 6),
    _SwL2QOSHolPreventionCtrl_Type()
)
swL2QOSHolPreventionCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSHolPreventionCtrl.setStatus("current")
_SwL2PortSecurityMgmt_ObjectIdentity = ObjectIdentity
swL2PortSecurityMgmt = _SwL2PortSecurityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7)
)
_SwL2PortSecurityControlTable_Object = MibTable
swL2PortSecurityControlTable = _SwL2PortSecurityControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    swL2PortSecurityControlTable.setStatus("current")
_SwL2PortSecurityControlEntry_Object = MibTableRow
swL2PortSecurityControlEntry = _SwL2PortSecurityControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7, 1, 1)
)
swL2PortSecurityControlEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2PortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortSecurityControlEntry.setStatus("current")


class _SwL2PortSecurityPortIndex_Type(Integer32):
    """Custom type swL2PortSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_SwL2PortSecurityPortIndex_Type.__name__ = "Integer32"
_SwL2PortSecurityPortIndex_Object = MibTableColumn
swL2PortSecurityPortIndex = _SwL2PortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7, 1, 1, 1),
    _SwL2PortSecurityPortIndex_Type()
)
swL2PortSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSecurityPortIndex.setStatus("current")


class _SwL2PortSecurityMaxLernAddr_Type(Integer32):
    """Custom type swL2PortSecurityMaxLernAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SwL2PortSecurityMaxLernAddr_Type.__name__ = "Integer32"
_SwL2PortSecurityMaxLernAddr_Object = MibTableColumn
swL2PortSecurityMaxLernAddr = _SwL2PortSecurityMaxLernAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7, 1, 1, 2),
    _SwL2PortSecurityMaxLernAddr_Type()
)
swL2PortSecurityMaxLernAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityMaxLernAddr.setStatus("current")


class _SwL2PortSecurityMode_Type(Integer32):
    """Custom type swL2PortSecurityMode based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 3),
          ("other", 1),
          ("permanent", 2))
    )


_SwL2PortSecurityMode_Type.__name__ = "Integer32"
_SwL2PortSecurityMode_Object = MibTableColumn
swL2PortSecurityMode = _SwL2PortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7, 1, 1, 3),
    _SwL2PortSecurityMode_Type()
)
swL2PortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityMode.setStatus("current")


class _SwL2PortSecurityAdmState_Type(Integer32):
    """Custom type swL2PortSecurityAdmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_SwL2PortSecurityAdmState_Type.__name__ = "Integer32"
_SwL2PortSecurityAdmState_Object = MibTableColumn
swL2PortSecurityAdmState = _SwL2PortSecurityAdmState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7, 1, 1, 4),
    _SwL2PortSecurityAdmState_Type()
)
swL2PortSecurityAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityAdmState.setStatus("current")
_SwL2PortSecurityDelCtrl_ObjectIdentity = ObjectIdentity
swL2PortSecurityDelCtrl = _SwL2PortSecurityDelCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7, 2)
)


class _SwL2PortSecurityDelVlanName_Type(DisplayString):
    """Custom type swL2PortSecurityDelVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2PortSecurityDelVlanName_Type.__name__ = "DisplayString"
_SwL2PortSecurityDelVlanName_Object = MibScalar
swL2PortSecurityDelVlanName = _SwL2PortSecurityDelVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7, 2, 1),
    _SwL2PortSecurityDelVlanName_Type()
)
swL2PortSecurityDelVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityDelVlanName.setStatus("current")


class _SwL2PortSecurityDelPort_Type(Integer32):
    """Custom type swL2PortSecurityDelPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 768),
    )


_SwL2PortSecurityDelPort_Type.__name__ = "Integer32"
_SwL2PortSecurityDelPort_Object = MibScalar
swL2PortSecurityDelPort = _SwL2PortSecurityDelPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7, 2, 2),
    _SwL2PortSecurityDelPort_Type()
)
swL2PortSecurityDelPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityDelPort.setStatus("current")
_SwL2PortSecurityDelMacAddress_Type = MacAddress
_SwL2PortSecurityDelMacAddress_Object = MibScalar
swL2PortSecurityDelMacAddress = _SwL2PortSecurityDelMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7, 2, 3),
    _SwL2PortSecurityDelMacAddress_Type()
)
swL2PortSecurityDelMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityDelMacAddress.setStatus("current")


class _SwL2PortSecurityDelActivity_Type(Integer32):
    """Custom type swL2PortSecurityDelActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SwL2PortSecurityDelActivity_Type.__name__ = "Integer32"
_SwL2PortSecurityDelActivity_Object = MibScalar
swL2PortSecurityDelActivity = _SwL2PortSecurityDelActivity_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 7, 2, 4),
    _SwL2PortSecurityDelActivity_Type()
)
swL2PortSecurityDelActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityDelActivity.setStatus("current")
_SwL2TrunkMgmt_ObjectIdentity = ObjectIdentity
swL2TrunkMgmt = _SwL2TrunkMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 2),
    _SwL2TrunkCurrentNumEntries_Type()
)
swL2TrunkCurrentNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkCurrentNumEntries.setStatus("current")
_SwL2TrunkCtrlTable_Object = MibTable
swL2TrunkCtrlTable = _SwL2TrunkCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 3)
)
if mibBuilder.loadTexts:
    swL2TrunkCtrlTable.setStatus("current")
_SwL2TrunkCtrlEntry_Object = MibTableRow
swL2TrunkCtrlEntry = _SwL2TrunkCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 3, 1)
)
swL2TrunkCtrlEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2TrunkIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 3, 1, 2),
    _SwL2TrunkName_Type()
)
swL2TrunkName.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 3, 1, 3),
    _SwL2TrunkMasterPort_Type()
)
swL2TrunkMasterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkMasterPort.setStatus("current")
_SwL2TrunkMember_Type = PortList
_SwL2TrunkMember_Object = MibTableColumn
swL2TrunkMember = _SwL2TrunkMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 3, 1, 4),
    _SwL2TrunkMember_Type()
)
swL2TrunkMember.setMaxAccess("read-create")
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 3, 1, 5),
    _SwL2TrunkFloodingPort_Type()
)
swL2TrunkFloodingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkFloodingPort.setStatus("current")


class _SwL2TrunkType_Type(Integer32):
    """Custom type swL2TrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 3),
          ("other", 1),
          ("static", 2))
    )


_SwL2TrunkType_Type.__name__ = "Integer32"
_SwL2TrunkType_Object = MibTableColumn
swL2TrunkType = _SwL2TrunkType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 3, 1, 6),
    _SwL2TrunkType_Type()
)
swL2TrunkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkType.setStatus("current")
_SwL2TrunkState_Type = RowStatus
_SwL2TrunkState_Object = MibTableColumn
swL2TrunkState = _SwL2TrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 3, 1, 7),
    _SwL2TrunkState_Type()
)
swL2TrunkState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkState.setStatus("current")
_SwL2TrunkActivePorts_Type = PortList
_SwL2TrunkActivePorts_Object = MibTableColumn
swL2TrunkActivePorts = _SwL2TrunkActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 3, 1, 8),
    _SwL2TrunkActivePorts_Type()
)
swL2TrunkActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkActivePorts.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 4),
    _SwL2TrunkAlgorithm_Type()
)
swL2TrunkAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkAlgorithm.setStatus("current")
_SwL2TrunkLACPPortTable_Object = MibTable
swL2TrunkLACPPortTable = _SwL2TrunkLACPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 5)
)
if mibBuilder.loadTexts:
    swL2TrunkLACPPortTable.setStatus("current")
_SwL2TrunkLACPPortEntry_Object = MibTableRow
swL2TrunkLACPPortEntry = _SwL2TrunkLACPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 5, 1)
)
swL2TrunkLACPPortEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2TrunkLACPPortIndex"),
)
if mibBuilder.loadTexts:
    swL2TrunkLACPPortEntry.setStatus("current")


class _SwL2TrunkLACPPortIndex_Type(Integer32):
    """Custom type swL2TrunkLACPPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrunkLACPPortIndex_Type.__name__ = "Integer32"
_SwL2TrunkLACPPortIndex_Object = MibTableColumn
swL2TrunkLACPPortIndex = _SwL2TrunkLACPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 5, 1, 1),
    _SwL2TrunkLACPPortIndex_Type()
)
swL2TrunkLACPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkLACPPortIndex.setStatus("current")


class _SwL2TrunkLACPPortState_Type(Integer32):
    """Custom type swL2TrunkLACPPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_SwL2TrunkLACPPortState_Type.__name__ = "Integer32"
_SwL2TrunkLACPPortState_Object = MibTableColumn
swL2TrunkLACPPortState = _SwL2TrunkLACPPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 9, 5, 1, 2),
    _SwL2TrunkLACPPortState_Type()
)
swL2TrunkLACPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkLACPPortState.setStatus("current")
_SwL2MirrorMgmt_ObjectIdentity = ObjectIdentity
swL2MirrorMgmt = _SwL2MirrorMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 10)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 10, 1),
    _SwL2MirrorLogicTargetPort_Type()
)
swL2MirrorLogicTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorLogicTargetPort.setStatus("current")
_SwL2MirrorPortSourceIngress_Type = PortList
_SwL2MirrorPortSourceIngress_Object = MibScalar
swL2MirrorPortSourceIngress = _SwL2MirrorPortSourceIngress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 10, 2),
    _SwL2MirrorPortSourceIngress_Type()
)
swL2MirrorPortSourceIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortSourceIngress.setStatus("current")
_SwL2MirrorPortSourceEgress_Type = PortList
_SwL2MirrorPortSourceEgress_Object = MibScalar
swL2MirrorPortSourceEgress = _SwL2MirrorPortSourceEgress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 10, 4),
    _SwL2MirrorPortState_Type()
)
swL2MirrorPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortState.setStatus("current")
_SwL2IGMPMgmt_ObjectIdentity = ObjectIdentity
swL2IGMPMgmt = _SwL2IGMPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 2),
    _SwL2IGMPMaxIpGroupNumPerVlan_Type()
)
swL2IGMPMaxIpGroupNumPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMaxIpGroupNumPerVlan.setStatus("current")
_SwL2IGMPCtrlTable_Object = MibTable
swL2IGMPCtrlTable = _SwL2IGMPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3)
)
if mibBuilder.loadTexts:
    swL2IGMPCtrlTable.setStatus("current")
_SwL2IGMPCtrlEntry_Object = MibTableRow
swL2IGMPCtrlEntry = _SwL2IGMPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1)
)
swL2IGMPCtrlEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2IGMPCtrlVid"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 4),
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
        ValueRangeConstraint(1, 25),
    )


_SwL2IGMPLastMemberQueryInterval_Type.__name__ = "Integer32"
_SwL2IGMPLastMemberQueryInterval_Object = MibTableColumn
swL2IGMPLastMemberQueryInterval = _SwL2IGMPLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 10),
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
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SwL2IGMPCtrlState_Type.__name__ = "Integer32"
_SwL2IGMPCtrlState_Object = MibTableColumn
swL2IGMPCtrlState = _SwL2IGMPCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 11),
    _SwL2IGMPCtrlState_Type()
)
swL2IGMPCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPCtrlState.setStatus("current")


class _SwL2IGMPFastLeaveState_Type(Integer32):
    """Custom type swL2IGMPFastLeaveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SwL2IGMPFastLeaveState_Type.__name__ = "Integer32"
_SwL2IGMPFastLeaveState_Object = MibTableColumn
swL2IGMPFastLeaveState = _SwL2IGMPFastLeaveState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 12),
    _SwL2IGMPFastLeaveState_Type()
)
swL2IGMPFastLeaveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPFastLeaveState.setStatus("current")


class _SwL2IGMPQueryVersion_Type(Integer32):
    """Custom type swL2IGMPQueryVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SwL2IGMPQueryVersion_Type.__name__ = "Integer32"
_SwL2IGMPQueryVersion_Object = MibTableColumn
swL2IGMPQueryVersion = _SwL2IGMPQueryVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 13),
    _SwL2IGMPQueryVersion_Type()
)
swL2IGMPQueryVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPQueryVersion.setStatus("current")


class _SwL2IGMPReportSuppression_Type(Integer32):
    """Custom type swL2IGMPReportSuppression based on Integer32"""
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


_SwL2IGMPReportSuppression_Type.__name__ = "Integer32"
_SwL2IGMPReportSuppression_Object = MibTableColumn
swL2IGMPReportSuppression = _SwL2IGMPReportSuppression_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 3, 1, 15),
    _SwL2IGMPReportSuppression_Type()
)
swL2IGMPReportSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPReportSuppression.setStatus("current")
_SwL2IGMPQueryInfoTable_Object = MibTable
swL2IGMPQueryInfoTable = _SwL2IGMPQueryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 4)
)
if mibBuilder.loadTexts:
    swL2IGMPQueryInfoTable.setStatus("current")
_SwL2IGMPQueryInfoEntry_Object = MibTableRow
swL2IGMPQueryInfoEntry = _SwL2IGMPQueryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 4, 1)
)
swL2IGMPQueryInfoEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2IGMPInfoVid"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 4, 1, 3),
    _SwL2IGMPInfoTxQueryCount_Type()
)
swL2IGMPInfoTxQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoTxQueryCount.setStatus("current")
_SwL2IGMPInfoTable_Object = MibTable
swL2IGMPInfoTable = _SwL2IGMPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 5)
)
if mibBuilder.loadTexts:
    swL2IGMPInfoTable.setStatus("current")
_SwL2IGMPInfoEntry_Object = MibTableRow
swL2IGMPInfoEntry = _SwL2IGMPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 5, 1)
)
swL2IGMPInfoEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2IGMPVid"),
    (0, "DGS3427-L2MGMT-MIB", "swL2IGMPGroupIpAddr"),
)
if mibBuilder.loadTexts:
    swL2IGMPInfoEntry.setStatus("current")


class _SwL2IGMPVid_Type(Integer32):
    """Custom type swL2IGMPVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPVid_Type.__name__ = "Integer32"
_SwL2IGMPVid_Object = MibTableColumn
swL2IGMPVid = _SwL2IGMPVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 5, 1, 1),
    _SwL2IGMPVid_Type()
)
swL2IGMPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVid.setStatus("current")
_SwL2IGMPGroupIpAddr_Type = IpAddress
_SwL2IGMPGroupIpAddr_Object = MibTableColumn
swL2IGMPGroupIpAddr = _SwL2IGMPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 5, 1, 2),
    _SwL2IGMPGroupIpAddr_Type()
)
swL2IGMPGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPGroupIpAddr.setStatus("current")
_SwL2IGMPMacAddr_Type = MacAddress
_SwL2IGMPMacAddr_Object = MibTableColumn
swL2IGMPMacAddr = _SwL2IGMPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 5, 1, 3),
    _SwL2IGMPMacAddr_Type()
)
swL2IGMPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMacAddr.setStatus("current")
_SwL2IGMPPortMap_Type = PortList
_SwL2IGMPPortMap_Object = MibTableColumn
swL2IGMPPortMap = _SwL2IGMPPortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 5, 1, 5),
    _SwL2IGMPIpGroupReportCount_Type()
)
swL2IGMPIpGroupReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPIpGroupReportCount.setStatus("current")
_SwL2IGMPRouterPortsTable_Object = MibTable
swL2IGMPRouterPortsTable = _SwL2IGMPRouterPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 6)
)
if mibBuilder.loadTexts:
    swL2IGMPRouterPortsTable.setStatus("current")
_SwL2IGMPRouterPortsEntry_Object = MibTableRow
swL2IGMPRouterPortsEntry = _SwL2IGMPRouterPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 6, 1)
)
swL2IGMPRouterPortsEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2IGMPRouterPortsVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPRouterPortsEntry.setStatus("current")


class _SwL2IGMPRouterPortsVid_Type(Integer32):
    """Custom type swL2IGMPRouterPortsVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPRouterPortsVid_Type.__name__ = "Integer32"
_SwL2IGMPRouterPortsVid_Object = MibTableColumn
swL2IGMPRouterPortsVid = _SwL2IGMPRouterPortsVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 6, 1, 1),
    _SwL2IGMPRouterPortsVid_Type()
)
swL2IGMPRouterPortsVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortsVid.setStatus("current")
_SwL2IGMPRouterStaticPortList_Type = PortList
_SwL2IGMPRouterStaticPortList_Object = MibTableColumn
swL2IGMPRouterStaticPortList = _SwL2IGMPRouterStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 6, 1, 2),
    _SwL2IGMPRouterStaticPortList_Type()
)
swL2IGMPRouterStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouterStaticPortList.setStatus("current")
_SwL2IGMPRouterDynamicPortList_Type = PortList
_SwL2IGMPRouterDynamicPortList_Object = MibTableColumn
swL2IGMPRouterDynamicPortList = _SwL2IGMPRouterDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 6, 1, 3),
    _SwL2IGMPRouterDynamicPortList_Type()
)
swL2IGMPRouterDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterDynamicPortList.setStatus("current")
_SwL2IGMPRouterForbiddenPortList_Type = PortList
_SwL2IGMPRouterForbiddenPortList_Object = MibTableColumn
swL2IGMPRouterForbiddenPortList = _SwL2IGMPRouterForbiddenPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 6, 1, 4),
    _SwL2IGMPRouterForbiddenPortList_Type()
)
swL2IGMPRouterForbiddenPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouterForbiddenPortList.setStatus("current")
_SwL2IGMPMulticastVlanTable_Object = MibTable
swL2IGMPMulticastVlanTable = _SwL2IGMPMulticastVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 7)
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanTable.setStatus("current")
_SwL2IGMPMulticastVlanEntry_Object = MibTableRow
swL2IGMPMulticastVlanEntry = _SwL2IGMPMulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 7, 1)
)
swL2IGMPMulticastVlanEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2IGMPMulticastVlanid"),
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanEntry.setStatus("current")


class _SwL2IGMPMulticastVlanid_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_SwL2IGMPMulticastVlanid_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanid_Object = MibTableColumn
swL2IGMPMulticastVlanid = _SwL2IGMPMulticastVlanid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 7, 1, 1),
    _SwL2IGMPMulticastVlanid_Type()
)
swL2IGMPMulticastVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanid.setStatus("current")


class _SwL2IGMPMulticastVlanName_Type(DisplayString):
    """Custom type swL2IGMPMulticastVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2IGMPMulticastVlanName_Type.__name__ = "DisplayString"
_SwL2IGMPMulticastVlanName_Object = MibTableColumn
swL2IGMPMulticastVlanName = _SwL2IGMPMulticastVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 7, 1, 2),
    _SwL2IGMPMulticastVlanName_Type()
)
swL2IGMPMulticastVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanName.setStatus("current")
_SwL2IGMPMulticastVlanSourcePort_Type = PortList
_SwL2IGMPMulticastVlanSourcePort_Object = MibTableColumn
swL2IGMPMulticastVlanSourcePort = _SwL2IGMPMulticastVlanSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 7, 1, 3),
    _SwL2IGMPMulticastVlanSourcePort_Type()
)
swL2IGMPMulticastVlanSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanSourcePort.setStatus("current")
_SwL2IGMPMulticastVlanMemberPort_Type = PortList
_SwL2IGMPMulticastVlanMemberPort_Object = MibTableColumn
swL2IGMPMulticastVlanMemberPort = _SwL2IGMPMulticastVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 7, 1, 4),
    _SwL2IGMPMulticastVlanMemberPort_Type()
)
swL2IGMPMulticastVlanMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanMemberPort.setStatus("current")
_SwL2IGMPMulticastVlanTagMemberPort_Type = PortList
_SwL2IGMPMulticastVlanTagMemberPort_Object = MibTableColumn
swL2IGMPMulticastVlanTagMemberPort = _SwL2IGMPMulticastVlanTagMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 7, 1, 5),
    _SwL2IGMPMulticastVlanTagMemberPort_Type()
)
swL2IGMPMulticastVlanTagMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanTagMemberPort.setStatus("current")


class _SwL2IGMPMulticastVlanState_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanState based on Integer32"""
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


_SwL2IGMPMulticastVlanState_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanState_Object = MibTableColumn
swL2IGMPMulticastVlanState = _SwL2IGMPMulticastVlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 7, 1, 6),
    _SwL2IGMPMulticastVlanState_Type()
)
swL2IGMPMulticastVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanState.setStatus("current")
_SwL2IGMPMulticastVlanReplaceSourceIp_Type = IpAddress
_SwL2IGMPMulticastVlanReplaceSourceIp_Object = MibTableColumn
swL2IGMPMulticastVlanReplaceSourceIp = _SwL2IGMPMulticastVlanReplaceSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 7, 1, 7),
    _SwL2IGMPMulticastVlanReplaceSourceIp_Type()
)
swL2IGMPMulticastVlanReplaceSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanReplaceSourceIp.setStatus("current")
_SwL2IGMPMulticastVlanRowStatus_Type = RowStatus
_SwL2IGMPMulticastVlanRowStatus_Object = MibTableColumn
swL2IGMPMulticastVlanRowStatus = _SwL2IGMPMulticastVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 7, 1, 8),
    _SwL2IGMPMulticastVlanRowStatus_Type()
)
swL2IGMPMulticastVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanRowStatus.setStatus("current")


class _SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanRemoveAllMcastAddrListAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Object = MibTableColumn
swL2IGMPMulticastVlanRemoveAllMcastAddrListAction = _SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 7, 1, 9),
    _SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type()
)
swL2IGMPMulticastVlanRemoveAllMcastAddrListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanRemoveAllMcastAddrListAction.setStatus("current")
_SwL2IGMPMulticastVlanGroupTable_Object = MibTable
swL2IGMPMulticastVlanGroupTable = _SwL2IGMPMulticastVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 8)
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupTable.setStatus("current")
_SwL2IGMPMulticastVlanGroupEntry_Object = MibTableRow
swL2IGMPMulticastVlanGroupEntry = _SwL2IGMPMulticastVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 8, 1)
)
swL2IGMPMulticastVlanGroupEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2IGMPMulticastVlanGroupVid"),
    (0, "DGS3427-L2MGMT-MIB", "swL2IGMPMulticastVlanGroupFromIp"),
    (0, "DGS3427-L2MGMT-MIB", "swL2IGMPMulticastVlanGroupToIp"),
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupEntry.setStatus("current")


class _SwL2IGMPMulticastVlanGroupVid_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPMulticastVlanGroupVid_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanGroupVid_Object = MibTableColumn
swL2IGMPMulticastVlanGroupVid = _SwL2IGMPMulticastVlanGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 8, 1, 1),
    _SwL2IGMPMulticastVlanGroupVid_Type()
)
swL2IGMPMulticastVlanGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupVid.setStatus("current")
_SwL2IGMPMulticastVlanGroupFromIp_Type = IpAddress
_SwL2IGMPMulticastVlanGroupFromIp_Object = MibTableColumn
swL2IGMPMulticastVlanGroupFromIp = _SwL2IGMPMulticastVlanGroupFromIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 8, 1, 2),
    _SwL2IGMPMulticastVlanGroupFromIp_Type()
)
swL2IGMPMulticastVlanGroupFromIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupFromIp.setStatus("current")
_SwL2IGMPMulticastVlanGroupToIp_Type = IpAddress
_SwL2IGMPMulticastVlanGroupToIp_Object = MibTableColumn
swL2IGMPMulticastVlanGroupToIp = _SwL2IGMPMulticastVlanGroupToIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 8, 1, 3),
    _SwL2IGMPMulticastVlanGroupToIp_Type()
)
swL2IGMPMulticastVlanGroupToIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupToIp.setStatus("current")
_SwL2IGMPMulticastVlanGroupStatus_Type = RowStatus
_SwL2IGMPMulticastVlanGroupStatus_Object = MibTableColumn
swL2IGMPMulticastVlanGroupStatus = _SwL2IGMPMulticastVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 8, 1, 4),
    _SwL2IGMPMulticastVlanGroupStatus_Type()
)
swL2IGMPMulticastVlanGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupStatus.setStatus("current")
_SwIGMPSnoopingGroupTable_Object = MibTable
swIGMPSnoopingGroupTable = _SwIGMPSnoopingGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 11)
)
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupTable.setStatus("current")
_SwIGMPSnoopingGroupEntry_Object = MibTableRow
swIGMPSnoopingGroupEntry = _SwIGMPSnoopingGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 11, 1)
)
swIGMPSnoopingGroupEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swIGMPSnoopingGroupVid"),
    (0, "DGS3427-L2MGMT-MIB", "swIGMPSnoopingGroupGroupAddr"),
    (0, "DGS3427-L2MGMT-MIB", "swIGMPSnoopingGroupSourceAddr"),
)
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupEntry.setStatus("current")


class _SwIGMPSnoopingGroupVid_Type(Integer32):
    """Custom type swIGMPSnoopingGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwIGMPSnoopingGroupVid_Type.__name__ = "Integer32"
_SwIGMPSnoopingGroupVid_Object = MibTableColumn
swIGMPSnoopingGroupVid = _SwIGMPSnoopingGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 11, 1, 1),
    _SwIGMPSnoopingGroupVid_Type()
)
swIGMPSnoopingGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupVid.setStatus("current")
_SwIGMPSnoopingGroupGroupAddr_Type = IpAddress
_SwIGMPSnoopingGroupGroupAddr_Object = MibTableColumn
swIGMPSnoopingGroupGroupAddr = _SwIGMPSnoopingGroupGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 11, 1, 2),
    _SwIGMPSnoopingGroupGroupAddr_Type()
)
swIGMPSnoopingGroupGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupGroupAddr.setStatus("current")
_SwIGMPSnoopingGroupSourceAddr_Type = IpAddress
_SwIGMPSnoopingGroupSourceAddr_Object = MibTableColumn
swIGMPSnoopingGroupSourceAddr = _SwIGMPSnoopingGroupSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 11, 1, 3),
    _SwIGMPSnoopingGroupSourceAddr_Type()
)
swIGMPSnoopingGroupSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupSourceAddr.setStatus("current")
_SwIGMPSnoopingGroupIncludePortMap_Type = PortList
_SwIGMPSnoopingGroupIncludePortMap_Object = MibTableColumn
swIGMPSnoopingGroupIncludePortMap = _SwIGMPSnoopingGroupIncludePortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 11, 1, 4),
    _SwIGMPSnoopingGroupIncludePortMap_Type()
)
swIGMPSnoopingGroupIncludePortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupIncludePortMap.setStatus("current")
_SwIGMPSnoopingGroupExcludePortMap_Type = PortList
_SwIGMPSnoopingGroupExcludePortMap_Object = MibTableColumn
swIGMPSnoopingGroupExcludePortMap = _SwIGMPSnoopingGroupExcludePortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 11, 1, 5),
    _SwIGMPSnoopingGroupExcludePortMap_Type()
)
swIGMPSnoopingGroupExcludePortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupExcludePortMap.setStatus("current")
_SwL2IGMPSnoopingStaticGroupTable_Object = MibTable
swL2IGMPSnoopingStaticGroupTable = _SwL2IGMPSnoopingStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 16)
)
if mibBuilder.loadTexts:
    swL2IGMPSnoopingStaticGroupTable.setStatus("current")
_SwL2IGMPSnoopingStaticGroupEntry_Object = MibTableRow
swL2IGMPSnoopingStaticGroupEntry = _SwL2IGMPSnoopingStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 16, 1)
)
swL2IGMPSnoopingStaticGroupEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2IGMPSnoopingStaticGroupVID"),
    (0, "DGS3427-L2MGMT-MIB", "swL2IGMPSnoopingStaticGroupIPaddress"),
)
if mibBuilder.loadTexts:
    swL2IGMPSnoopingStaticGroupEntry.setStatus("current")


class _SwL2IGMPSnoopingStaticGroupVID_Type(Integer32):
    """Custom type swL2IGMPSnoopingStaticGroupVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2IGMPSnoopingStaticGroupVID_Type.__name__ = "Integer32"
_SwL2IGMPSnoopingStaticGroupVID_Object = MibTableColumn
swL2IGMPSnoopingStaticGroupVID = _SwL2IGMPSnoopingStaticGroupVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 16, 1, 1),
    _SwL2IGMPSnoopingStaticGroupVID_Type()
)
swL2IGMPSnoopingStaticGroupVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingStaticGroupVID.setStatus("current")
_SwL2IGMPSnoopingStaticGroupIPaddress_Type = IpAddress
_SwL2IGMPSnoopingStaticGroupIPaddress_Object = MibTableColumn
swL2IGMPSnoopingStaticGroupIPaddress = _SwL2IGMPSnoopingStaticGroupIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 16, 1, 2),
    _SwL2IGMPSnoopingStaticGroupIPaddress_Type()
)
swL2IGMPSnoopingStaticGroupIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingStaticGroupIPaddress.setStatus("current")
_SwL2IGMPSnoopingStaticGroupMemberPortList_Type = PortList
_SwL2IGMPSnoopingStaticGroupMemberPortList_Object = MibTableColumn
swL2IGMPSnoopingStaticGroupMemberPortList = _SwL2IGMPSnoopingStaticGroupMemberPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 16, 1, 3),
    _SwL2IGMPSnoopingStaticGroupMemberPortList_Type()
)
swL2IGMPSnoopingStaticGroupMemberPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingStaticGroupMemberPortList.setStatus("current")
_SwL2IGMPSnoopingStaticGroupRowStatus_Type = RowStatus
_SwL2IGMPSnoopingStaticGroupRowStatus_Object = MibTableColumn
swL2IGMPSnoopingStaticGroupRowStatus = _SwL2IGMPSnoopingStaticGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 11, 16, 1, 4),
    _SwL2IGMPSnoopingStaticGroupRowStatus_Type()
)
swL2IGMPSnoopingStaticGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingStaticGroupRowStatus.setStatus("current")
_SwL2TrafficSegMgmt_ObjectIdentity = ObjectIdentity
swL2TrafficSegMgmt = _SwL2TrafficSegMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 14)
)
_SwL2TrafficSegTable_Object = MibTable
swL2TrafficSegTable = _SwL2TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 14, 1)
)
if mibBuilder.loadTexts:
    swL2TrafficSegTable.setStatus("current")
_SwL2TrafficSegEntry_Object = MibTableRow
swL2TrafficSegEntry = _SwL2TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 14, 1, 1)
)
swL2TrafficSegEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2TrafficSegPort"),
)
if mibBuilder.loadTexts:
    swL2TrafficSegEntry.setStatus("current")


class _SwL2TrafficSegPort_Type(Integer32):
    """Custom type swL2TrafficSegPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrafficSegPort_Type.__name__ = "Integer32"
_SwL2TrafficSegPort_Object = MibTableColumn
swL2TrafficSegPort = _SwL2TrafficSegPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 14, 1, 1, 1),
    _SwL2TrafficSegPort_Type()
)
swL2TrafficSegPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficSegPort.setStatus("current")
_SwL2TrafficSegForwardPorts_Type = PortList
_SwL2TrafficSegForwardPorts_Object = MibTableColumn
swL2TrafficSegForwardPorts = _SwL2TrafficSegForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 14, 1, 1, 2),
    _SwL2TrafficSegForwardPorts_Type()
)
swL2TrafficSegForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficSegForwardPorts.setStatus("current")
_SwL2IpLimitedMulticastMgmt_ObjectIdentity = ObjectIdentity
swL2IpLimitedMulticastMgmt = _SwL2IpLimitedMulticastMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 15)
)
_SwL2IpLimitedMulticastTable_Object = MibTable
swL2IpLimitedMulticastTable = _SwL2IpLimitedMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 15, 1)
)
if mibBuilder.loadTexts:
    swL2IpLimitedMulticastTable.setStatus("current")
_SwL2IpLimitedMulticastEntry_Object = MibTableRow
swL2IpLimitedMulticastEntry = _SwL2IpLimitedMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 15, 1, 1)
)
swL2IpLimitedMulticastEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2IpLimitedMulticastPortIndex"),
)
if mibBuilder.loadTexts:
    swL2IpLimitedMulticastEntry.setStatus("current")


class _SwL2IpLimitedMulticastPortIndex_Type(Integer32):
    """Custom type swL2IpLimitedMulticastPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IpLimitedMulticastPortIndex_Type.__name__ = "Integer32"
_SwL2IpLimitedMulticastPortIndex_Object = MibTableColumn
swL2IpLimitedMulticastPortIndex = _SwL2IpLimitedMulticastPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 15, 1, 1, 1),
    _SwL2IpLimitedMulticastPortIndex_Type()
)
swL2IpLimitedMulticastPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IpLimitedMulticastPortIndex.setStatus("current")
_SwL2IpLimitedMulticastHead_Type = IpAddress
_SwL2IpLimitedMulticastHead_Object = MibTableColumn
swL2IpLimitedMulticastHead = _SwL2IpLimitedMulticastHead_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 15, 1, 1, 2),
    _SwL2IpLimitedMulticastHead_Type()
)
swL2IpLimitedMulticastHead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IpLimitedMulticastHead.setStatus("current")
_SwL2IpLimitedMulticastTail_Type = IpAddress
_SwL2IpLimitedMulticastTail_Object = MibTableColumn
swL2IpLimitedMulticastTail = _SwL2IpLimitedMulticastTail_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 15, 1, 1, 3),
    _SwL2IpLimitedMulticastTail_Type()
)
swL2IpLimitedMulticastTail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IpLimitedMulticastTail.setStatus("current")


class _SwL2IpLimitedMulticastAccess_Type(Integer32):
    """Custom type swL2IpLimitedMulticastAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("none", 0),
          ("permit", 1))
    )


_SwL2IpLimitedMulticastAccess_Type.__name__ = "Integer32"
_SwL2IpLimitedMulticastAccess_Object = MibTableColumn
swL2IpLimitedMulticastAccess = _SwL2IpLimitedMulticastAccess_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 15, 1, 1, 4),
    _SwL2IpLimitedMulticastAccess_Type()
)
swL2IpLimitedMulticastAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IpLimitedMulticastAccess.setStatus("current")


class _SwL2IpLimitedMulticastState_Type(Integer32):
    """Custom type swL2IpLimitedMulticastState based on Integer32"""
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


_SwL2IpLimitedMulticastState_Type.__name__ = "Integer32"
_SwL2IpLimitedMulticastState_Object = MibTableColumn
swL2IpLimitedMulticastState = _SwL2IpLimitedMulticastState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 15, 1, 1, 5),
    _SwL2IpLimitedMulticastState_Type()
)
swL2IpLimitedMulticastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IpLimitedMulticastState.setStatus("current")


class _SwL2IpLimitedMulticastDelState_Type(Integer32):
    """Custom type swL2IpLimitedMulticastDelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SwL2IpLimitedMulticastDelState_Type.__name__ = "Integer32"
_SwL2IpLimitedMulticastDelState_Object = MibTableColumn
swL2IpLimitedMulticastDelState = _SwL2IpLimitedMulticastDelState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 15, 1, 1, 6),
    _SwL2IpLimitedMulticastDelState_Type()
)
swL2IpLimitedMulticastDelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IpLimitedMulticastDelState.setStatus("current")
_SwL2MgmtMIBTraps_ObjectIdentity = ObjectIdentity
swL2MgmtMIBTraps = _SwL2MgmtMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16)
)
_SwL2Notify_ObjectIdentity = ObjectIdentity
swL2Notify = _SwL2Notify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1)
)
_SwL2NotifyPrefix_ObjectIdentity = ObjectIdentity
swL2NotifyPrefix = _SwL2NotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1, 2)
)
_SwL2NotifFirmware_ObjectIdentity = ObjectIdentity
swL2NotifFirmware = _SwL2NotifFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1, 2, 0)
)
_SwL2LoopDetectedNotify_ObjectIdentity = ObjectIdentity
swL2LoopDetectedNotify = _SwL2LoopDetectedNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1, 2, 0, 0)
)
_Swl2NotificationBidings_ObjectIdentity = ObjectIdentity
swl2NotificationBidings = _Swl2NotificationBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1, 2, 1)
)


class _SwL2macNotifyInfo_Type(OctetString):
    """Custom type swL2macNotifyInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SwL2macNotifyInfo_Type.__name__ = "OctetString"
_SwL2macNotifyInfo_Object = MibScalar
swL2macNotifyInfo = _SwL2macNotifyInfo_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1, 2, 1, 1),
    _SwL2macNotifyInfo_Type()
)
swL2macNotifyInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2macNotifyInfo.setStatus("current")
_SwL2VlanLoopDetectVID_Type = Integer32
_SwL2VlanLoopDetectVID_Object = MibScalar
swL2VlanLoopDetectVID = _SwL2VlanLoopDetectVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1, 2, 1, 3),
    _SwL2VlanLoopDetectVID_Type()
)
swL2VlanLoopDetectVID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swL2VlanLoopDetectVID.setStatus("current")
_SwL2VlanMgmt_ObjectIdentity = ObjectIdentity
swL2VlanMgmt = _SwL2VlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17)
)
_SwL2VlanTable_Object = MibTable
swL2VlanTable = _SwL2VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1)
)
if mibBuilder.loadTexts:
    swL2VlanTable.setStatus("current")
_SwL2VlanEntry_Object = MibTableRow
swL2VlanEntry = _SwL2VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1)
)
swL2VlanEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2VlanIndex"),
)
if mibBuilder.loadTexts:
    swL2VlanEntry.setStatus("current")
_SwL2VlanIndex_Type = VlanId
_SwL2VlanIndex_Object = MibTableColumn
swL2VlanIndex = _SwL2VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1, 1),
    _SwL2VlanIndex_Type()
)
swL2VlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2VlanIndex.setStatus("current")


class _SwL2VlanName_Type(DisplayString):
    """Custom type swL2VlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2VlanName_Type.__name__ = "DisplayString"
_SwL2VlanName_Object = MibTableColumn
swL2VlanName = _SwL2VlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1, 2),
    _SwL2VlanName_Type()
)
swL2VlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanName.setStatus("current")


class _SwL2VlanType_Type(Integer32):
    """Custom type swL2VlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("double-vlan", 5),
          ("dynamic-vlan", 2),
          ("invalid-vlan-type", 0),
          ("port-base-vlan", 3),
          ("protocolvlan", 4),
          ("static-1q-vlan", 1))
    )


_SwL2VlanType_Type.__name__ = "Integer32"
_SwL2VlanType_Object = MibTableColumn
swL2VlanType = _SwL2VlanType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1, 3),
    _SwL2VlanType_Type()
)
swL2VlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanType.setStatus("current")
_SwL2VlanMemberPorts_Type = PortList
_SwL2VlanMemberPorts_Object = MibTableColumn
swL2VlanMemberPorts = _SwL2VlanMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1, 4),
    _SwL2VlanMemberPorts_Type()
)
swL2VlanMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanMemberPorts.setStatus("current")
_SwL2VlanStaticPorts_Type = PortList
_SwL2VlanStaticPorts_Object = MibTableColumn
swL2VlanStaticPorts = _SwL2VlanStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1, 5),
    _SwL2VlanStaticPorts_Type()
)
swL2VlanStaticPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanStaticPorts.setStatus("current")
_SwL2VlanStaticTaggedPorts_Type = PortList
_SwL2VlanStaticTaggedPorts_Object = MibTableColumn
swL2VlanStaticTaggedPorts = _SwL2VlanStaticTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1, 6),
    _SwL2VlanStaticTaggedPorts_Type()
)
swL2VlanStaticTaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanStaticTaggedPorts.setStatus("current")
_SwL2VlanStaticUntaggedPorts_Type = PortList
_SwL2VlanStaticUntaggedPorts_Object = MibTableColumn
swL2VlanStaticUntaggedPorts = _SwL2VlanStaticUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1, 7),
    _SwL2VlanStaticUntaggedPorts_Type()
)
swL2VlanStaticUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanStaticUntaggedPorts.setStatus("current")
_SwL2VlanForbiddenPorts_Type = PortList
_SwL2VlanForbiddenPorts_Object = MibTableColumn
swL2VlanForbiddenPorts = _SwL2VlanForbiddenPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1, 8),
    _SwL2VlanForbiddenPorts_Type()
)
swL2VlanForbiddenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanForbiddenPorts.setStatus("current")
_SwL2VlanCurrentTaggedPorts_Type = PortList
_SwL2VlanCurrentTaggedPorts_Object = MibTableColumn
swL2VlanCurrentTaggedPorts = _SwL2VlanCurrentTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1, 9),
    _SwL2VlanCurrentTaggedPorts_Type()
)
swL2VlanCurrentTaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanCurrentTaggedPorts.setStatus("current")
_SwL2VlanCurrentUntaggedPorts_Type = PortList
_SwL2VlanCurrentUntaggedPorts_Object = MibTableColumn
swL2VlanCurrentUntaggedPorts = _SwL2VlanCurrentUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1, 10),
    _SwL2VlanCurrentUntaggedPorts_Type()
)
swL2VlanCurrentUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanCurrentUntaggedPorts.setStatus("current")


class _SwL2VlanAdvertisementState_Type(Integer32):
    """Custom type swL2VlanAdvertisementState based on Integer32"""
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


_SwL2VlanAdvertisementState_Type.__name__ = "Integer32"
_SwL2VlanAdvertisementState_Object = MibTableColumn
swL2VlanAdvertisementState = _SwL2VlanAdvertisementState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 1, 1, 11),
    _SwL2VlanAdvertisementState_Type()
)
swL2VlanAdvertisementState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2VlanAdvertisementState.setStatus("current")


class _SwL2PVIDAutoAssignmentState_Type(Integer32):
    """Custom type swL2PVIDAutoAssignmentState based on Integer32"""
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


_SwL2PVIDAutoAssignmentState_Type.__name__ = "Integer32"
_SwL2PVIDAutoAssignmentState_Object = MibScalar
swL2PVIDAutoAssignmentState = _SwL2PVIDAutoAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 17, 2),
    _SwL2PVIDAutoAssignmentState_Type()
)
swL2PVIDAutoAssignmentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PVIDAutoAssignmentState.setStatus("current")
_SwL2LoopDetectMgmt_ObjectIdentity = ObjectIdentity
swL2LoopDetectMgmt = _SwL2LoopDetectMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18)
)
_SwL2LoopDetectCtrl_ObjectIdentity = ObjectIdentity
swL2LoopDetectCtrl = _SwL2LoopDetectCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 1)
)


class _SwL2LoopDetectAdminState_Type(Integer32):
    """Custom type swL2LoopDetectAdminState based on Integer32"""
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


_SwL2LoopDetectAdminState_Type.__name__ = "Integer32"
_SwL2LoopDetectAdminState_Object = MibScalar
swL2LoopDetectAdminState = _SwL2LoopDetectAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 1, 1),
    _SwL2LoopDetectAdminState_Type()
)
swL2LoopDetectAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectAdminState.setStatus("current")


class _SwL2LoopDetectInterval_Type(Integer32):
    """Custom type swL2LoopDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SwL2LoopDetectInterval_Type.__name__ = "Integer32"
_SwL2LoopDetectInterval_Object = MibScalar
swL2LoopDetectInterval = _SwL2LoopDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 1, 2),
    _SwL2LoopDetectInterval_Type()
)
swL2LoopDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectInterval.setStatus("current")


class _SwL2LoopDetectRecoverTime_Type(Integer32):
    """Custom type swL2LoopDetectRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SwL2LoopDetectRecoverTime_Type.__name__ = "Integer32"
_SwL2LoopDetectRecoverTime_Object = MibScalar
swL2LoopDetectRecoverTime = _SwL2LoopDetectRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 1, 3),
    _SwL2LoopDetectRecoverTime_Type()
)
swL2LoopDetectRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectRecoverTime.setStatus("current")


class _SwL2LoopDetectMode_Type(Integer32):
    """Custom type swL2LoopDetectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-based", 2),
          ("vlan-based", 1))
    )


_SwL2LoopDetectMode_Type.__name__ = "Integer32"
_SwL2LoopDetectMode_Object = MibScalar
swL2LoopDetectMode = _SwL2LoopDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 1, 4),
    _SwL2LoopDetectMode_Type()
)
swL2LoopDetectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectMode.setStatus("current")


class _SwL2LoopDetectTrapMode_Type(Integer32):
    """Custom type swL2LoopDetectTrapMode based on Integer32"""
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
        *(("both", 4),
          ("loop_cleared", 3),
          ("loop_detected", 2),
          ("none", 1))
    )


_SwL2LoopDetectTrapMode_Type.__name__ = "Integer32"
_SwL2LoopDetectTrapMode_Object = MibScalar
swL2LoopDetectTrapMode = _SwL2LoopDetectTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 1, 5),
    _SwL2LoopDetectTrapMode_Type()
)
swL2LoopDetectTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectTrapMode.setStatus("current")
_SwL2LoopDetectPortMgmt_ObjectIdentity = ObjectIdentity
swL2LoopDetectPortMgmt = _SwL2LoopDetectPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 2)
)
_SwL2LoopDetectPortTable_Object = MibTable
swL2LoopDetectPortTable = _SwL2LoopDetectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    swL2LoopDetectPortTable.setStatus("current")
_SwL2LoopDetectPortEntry_Object = MibTableRow
swL2LoopDetectPortEntry = _SwL2LoopDetectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 2, 1, 1)
)
swL2LoopDetectPortEntry.setIndexNames(
    (0, "DGS3427-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
)
if mibBuilder.loadTexts:
    swL2LoopDetectPortEntry.setStatus("current")


class _SwL2LoopDetectPortIndex_Type(Integer32):
    """Custom type swL2LoopDetectPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2LoopDetectPortIndex_Type.__name__ = "Integer32"
_SwL2LoopDetectPortIndex_Object = MibTableColumn
swL2LoopDetectPortIndex = _SwL2LoopDetectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 2, 1, 1, 1),
    _SwL2LoopDetectPortIndex_Type()
)
swL2LoopDetectPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LoopDetectPortIndex.setStatus("current")


class _SwL2LoopDetectPortState_Type(Integer32):
    """Custom type swL2LoopDetectPortState based on Integer32"""
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


_SwL2LoopDetectPortState_Type.__name__ = "Integer32"
_SwL2LoopDetectPortState_Object = MibTableColumn
swL2LoopDetectPortState = _SwL2LoopDetectPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 2, 1, 1, 2),
    _SwL2LoopDetectPortState_Type()
)
swL2LoopDetectPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectPortState.setStatus("current")
_SwL2LoopDetectPortLoopVLAN_Type = DisplayString
_SwL2LoopDetectPortLoopVLAN_Object = MibTableColumn
swL2LoopDetectPortLoopVLAN = _SwL2LoopDetectPortLoopVLAN_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 2, 1, 1, 3),
    _SwL2LoopDetectPortLoopVLAN_Type()
)
swL2LoopDetectPortLoopVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LoopDetectPortLoopVLAN.setStatus("current")


class _SwL2LoopDetectPortLoopStatus_Type(Integer32):
    """Custom type swL2LoopDetectPortLoopStatus based on Integer32"""
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
        *(("error", 3),
          ("loop", 2),
          ("none", 4),
          ("normal", 1))
    )


_SwL2LoopDetectPortLoopStatus_Type.__name__ = "Integer32"
_SwL2LoopDetectPortLoopStatus_Object = MibTableColumn
swL2LoopDetectPortLoopStatus = _SwL2LoopDetectPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 18, 2, 1, 1, 4),
    _SwL2LoopDetectPortLoopStatus_Type()
)
swL2LoopDetectPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LoopDetectPortLoopStatus.setStatus("current")

# Managed Objects groups


# Notification objects

swL2PortLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1, 2, 0, 0, 3)
)
swL2PortLoopOccurred.setObjects(
    ("DGS3427-L2MGMT-MIB", "swL2LoopDetectPortIndex")
)
if mibBuilder.loadTexts:
    swL2PortLoopOccurred.setStatus(
        "current"
    )

swL2PortLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1, 2, 0, 0, 4)
)
swL2PortLoopRestart.setObjects(
    ("DGS3427-L2MGMT-MIB", "swL2LoopDetectPortIndex")
)
if mibBuilder.loadTexts:
    swL2PortLoopRestart.setStatus(
        "current"
    )

swL2VlanLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1, 2, 0, 0, 5)
)
swL2VlanLoopOccurred.setObjects(
      *(("DGS3427-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
        ("DGS3427-L2MGMT-MIB", "swL2VlanLoopDetectVID"))
)
if mibBuilder.loadTexts:
    swL2VlanLoopOccurred.setStatus(
        "current"
    )

swL2VlanLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1, 2, 0, 0, 6)
)
swL2VlanLoopRestart.setObjects(
      *(("DGS3427-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
        ("DGS3427-L2MGMT-MIB", "swL2VlanLoopDetectVID"))
)
if mibBuilder.loadTexts:
    swL2VlanLoopRestart.setStatus(
        "current"
    )

swL2macNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2, 2, 16, 1, 2, 0, 1)
)
swL2macNotification.setObjects(
    ("DGS3427-L2MGMT-MIB", "swL2macNotifyInfo")
)
if mibBuilder.loadTexts:
    swL2macNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS3427-L2MGMT-MIB",
    **{"MacAddress": MacAddress,
       "VlanId": VlanId,
       "PortList": PortList,
       "IANAifMauAutoNegCapBits": IANAifMauAutoNegCapBits,
       "swL2MgmtMIB": swL2MgmtMIB,
       "swL2DevMgmt": swL2DevMgmt,
       "swL2DevInfo": swL2DevInfo,
       "swDevInfoTotalNumOfPort": swDevInfoTotalNumOfPort,
       "swDevInfoNumOfPortInUse": swDevInfoNumOfPortInUse,
       "swDevModuleInfoTable": swDevModuleInfoTable,
       "swDevModuleInfoEntry": swDevModuleInfoEntry,
       "swDevModuleInfoUnitID": swDevModuleInfoUnitID,
       "swDevModuleInfoModuleID": swDevModuleInfoModuleID,
       "swDevModuleInfoModuleName": swDevModuleInfoModuleName,
       "swDevModuleInfoReversion": swDevModuleInfoReversion,
       "swDevModuleInfoSerial": swDevModuleInfoSerial,
       "swDevModuleInfoDescription": swDevModuleInfoDescription,
       "swDevInfoBootPromVersion": swDevInfoBootPromVersion,
       "swDevInfoFirmwareVersion": swDevInfoFirmwareVersion,
       "swDevInfoFrontPanelLedStatus": swDevInfoFrontPanelLedStatus,
       "swL2DevCtrl": swL2DevCtrl,
       "swL2DevCtrlStpState": swL2DevCtrlStpState,
       "swL2DevCtrlIGMPSnooping": swL2DevCtrlIGMPSnooping,
       "swL2DevCtrlIGMPSnoopingMcstRTOnly": swL2DevCtrlIGMPSnoopingMcstRTOnly,
       "swL2DevCtrlRmonState": swL2DevCtrlRmonState,
       "swL2DevCtrlCleanAllStatisticCounter": swL2DevCtrlCleanAllStatisticCounter,
       "swL2DevCtrlVlanIdOfFDBTbl": swL2DevCtrlVlanIdOfFDBTbl,
       "swL2DevCtrlManagementVlanId": swL2DevCtrlManagementVlanId,
       "swL2MACNotifyState": swL2MACNotifyState,
       "swL2MACNotifyHistorySize": swL2MACNotifyHistorySize,
       "swL2MACNotifyInterval": swL2MACNotifyInterval,
       "swL2DevCtrlWeb": swL2DevCtrlWeb,
       "swL2DevCtrlWebState": swL2DevCtrlWebState,
       "swL2DevCtrlWebTcpPort": swL2DevCtrlWebTcpPort,
       "swL2DevCtrlTelnet": swL2DevCtrlTelnet,
       "swL2DevCtrlTelnetState": swL2DevCtrlTelnetState,
       "swL2DevCtrlTelnetTcpPort": swL2DevCtrlTelnetTcpPort,
       "swL2DevCtrlIpAutoconfig": swL2DevCtrlIpAutoconfig,
       "swL2DevCtrlClipagingState": swL2DevCtrlClipagingState,
       "swL2DevCtrlLLDPState": swL2DevCtrlLLDPState,
       "swL2DevCtrlLLDPForwardMessageState": swL2DevCtrlLLDPForwardMessageState,
       "swL2DevAlarm": swL2DevAlarm,
       "swL2DevAlarmNewRoot": swL2DevAlarmNewRoot,
       "swL2DevAlarmTopologyChange": swL2DevAlarmTopologyChange,
       "swL2DevAlarmLinkChange": swL2DevAlarmLinkChange,
       "swL2MultiFilter": swL2MultiFilter,
       "swL2MultiFilterTable": swL2MultiFilterTable,
       "swL2MultiFilterEntry": swL2MultiFilterEntry,
       "swL2MultiFilterVid": swL2MultiFilterVid,
       "swL2MultiFilterMode": swL2MultiFilterMode,
       "swL2PortMgmt": swL2PortMgmt,
       "swL2PortInfoTable": swL2PortInfoTable,
       "swL2PortInfoEntry": swL2PortInfoEntry,
       "swL2PortInfoPortIndex": swL2PortInfoPortIndex,
       "swL2PortInfoMediumType": swL2PortInfoMediumType,
       "swL2PortInfoUnitID": swL2PortInfoUnitID,
       "swL2PortInfoType": swL2PortInfoType,
       "swL2PortInfoLinkStatus": swL2PortInfoLinkStatus,
       "swL2PortInfoNwayStatus": swL2PortInfoNwayStatus,
       "swL2PortInfoErrDisReason": swL2PortInfoErrDisReason,
       "swL2PortCtrlTable": swL2PortCtrlTable,
       "swL2PortCtrlEntry": swL2PortCtrlEntry,
       "swL2PortCtrlPortIndex": swL2PortCtrlPortIndex,
       "swL2PortCtrlMediumType": swL2PortCtrlMediumType,
       "swL2PortCtrlUnitIndex": swL2PortCtrlUnitIndex,
       "swL2PortCtrlAdminState": swL2PortCtrlAdminState,
       "swL2PortCtrlNwayState": swL2PortCtrlNwayState,
       "swL2PortCtrlFlowCtrlState": swL2PortCtrlFlowCtrlState,
       "swL2PortCtrlLockState": swL2PortCtrlLockState,
       "swL2PortCtrlMACNotifyState": swL2PortCtrlMACNotifyState,
       "swL2PortCtrlAutoNegRestart": swL2PortCtrlAutoNegRestart,
       "swL2PortCtrlAutoNegCapAdvertisedBits": swL2PortCtrlAutoNegCapAdvertisedBits,
       "swL2PortCtrlJumboFrame": swL2PortCtrlJumboFrame,
       "swL2PortCtrlJumboFrameMaxSize": swL2PortCtrlJumboFrameMaxSize,
       "swL2PortCounterCtrlTable": swL2PortCounterCtrlTable,
       "swL2PortCounterCtrlEntry": swL2PortCounterCtrlEntry,
       "swL2PortCounterCtrlPortIndex": swL2PortCounterCtrlPortIndex,
       "swL2PortCounterClearCtrl": swL2PortCounterClearCtrl,
       "swL2PortAutoNegInfoTable": swL2PortAutoNegInfoTable,
       "swL2PortAutoNegInfoEntry": swL2PortAutoNegInfoEntry,
       "swL2PortAutoNegInfoPortIndex": swL2PortAutoNegInfoPortIndex,
       "swL2PortAutoNegInfoAdminStatus": swL2PortAutoNegInfoAdminStatus,
       "swL2PortAutoNegInfoCapabilityBits": swL2PortAutoNegInfoCapabilityBits,
       "swL2PortAutoNegInfoCapAdvertisedBits": swL2PortAutoNegInfoCapAdvertisedBits,
       "swL2PortAutoNegInfoCapReceivedBits": swL2PortAutoNegInfoCapReceivedBits,
       "swL2PortDropCounterTable": swL2PortDropCounterTable,
       "swL2PortDropCounterEntry": swL2PortDropCounterEntry,
       "swL2PortDropCounterPortIndex": swL2PortDropCounterPortIndex,
       "swL2PortBufferFullDrops": swL2PortBufferFullDrops,
       "swL2PortACLDrops": swL2PortACLDrops,
       "swL2PortMulticastDrops": swL2PortMulticastDrops,
       "swL2PortVLANIngressDrops": swL2PortVLANIngressDrops,
       "swL2QOSMgmt": swL2QOSMgmt,
       "swL2QOSBandwidthControlTable": swL2QOSBandwidthControlTable,
       "swL2QOSBandwidthControlEntry": swL2QOSBandwidthControlEntry,
       "swL2QOSBandwidthPortIndex": swL2QOSBandwidthPortIndex,
       "swL2QOSBandwidthRxRate": swL2QOSBandwidthRxRate,
       "swL2QOSBandwidthTxRate": swL2QOSBandwidthTxRate,
       "swL2QOSBandwidthRadiusRxRate": swL2QOSBandwidthRadiusRxRate,
       "swL2QOSBandwidthRadiusTxRate": swL2QOSBandwidthRadiusTxRate,
       "swL2QOSSchedulingTable": swL2QOSSchedulingTable,
       "swL2QOSSchedulingEntry": swL2QOSSchedulingEntry,
       "swL2QOSSchedulingClassIndex": swL2QOSSchedulingClassIndex,
       "swL2QOSSchedulingMaxPkts": swL2QOSSchedulingMaxPkts,
       "swL2QOSSchedulingMechanism": swL2QOSSchedulingMechanism,
       "swL2QOS8021pUserPriorityTable": swL2QOS8021pUserPriorityTable,
       "swL2QOS8021pUserPriorityEntry": swL2QOS8021pUserPriorityEntry,
       "swL2QOS8021pUserPriorityIndex": swL2QOS8021pUserPriorityIndex,
       "swL2QOS8021pUserPriorityClass": swL2QOS8021pUserPriorityClass,
       "swL2QOS8021pDefaultPriorityTable": swL2QOS8021pDefaultPriorityTable,
       "swL2QOS8021pDefaultPriorityEntry": swL2QOS8021pDefaultPriorityEntry,
       "swL2QOS8021pDefaultPriorityIndex": swL2QOS8021pDefaultPriorityIndex,
       "swL2QOS8021pDefaultPriority": swL2QOS8021pDefaultPriority,
       "swL2QOS8021pRadiusPriority": swL2QOS8021pRadiusPriority,
       "swL2QOSSchedulingMechanismCtrl": swL2QOSSchedulingMechanismCtrl,
       "swL2QOSHolPreventionCtrl": swL2QOSHolPreventionCtrl,
       "swL2PortSecurityMgmt": swL2PortSecurityMgmt,
       "swL2PortSecurityControlTable": swL2PortSecurityControlTable,
       "swL2PortSecurityControlEntry": swL2PortSecurityControlEntry,
       "swL2PortSecurityPortIndex": swL2PortSecurityPortIndex,
       "swL2PortSecurityMaxLernAddr": swL2PortSecurityMaxLernAddr,
       "swL2PortSecurityMode": swL2PortSecurityMode,
       "swL2PortSecurityAdmState": swL2PortSecurityAdmState,
       "swL2PortSecurityDelCtrl": swL2PortSecurityDelCtrl,
       "swL2PortSecurityDelVlanName": swL2PortSecurityDelVlanName,
       "swL2PortSecurityDelPort": swL2PortSecurityDelPort,
       "swL2PortSecurityDelMacAddress": swL2PortSecurityDelMacAddress,
       "swL2PortSecurityDelActivity": swL2PortSecurityDelActivity,
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
       "swL2TrunkType": swL2TrunkType,
       "swL2TrunkState": swL2TrunkState,
       "swL2TrunkActivePorts": swL2TrunkActivePorts,
       "swL2TrunkAlgorithm": swL2TrunkAlgorithm,
       "swL2TrunkLACPPortTable": swL2TrunkLACPPortTable,
       "swL2TrunkLACPPortEntry": swL2TrunkLACPPortEntry,
       "swL2TrunkLACPPortIndex": swL2TrunkLACPPortIndex,
       "swL2TrunkLACPPortState": swL2TrunkLACPPortState,
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
       "swL2IGMPFastLeaveState": swL2IGMPFastLeaveState,
       "swL2IGMPQueryVersion": swL2IGMPQueryVersion,
       "swL2IGMPReportSuppression": swL2IGMPReportSuppression,
       "swL2IGMPQueryInfoTable": swL2IGMPQueryInfoTable,
       "swL2IGMPQueryInfoEntry": swL2IGMPQueryInfoEntry,
       "swL2IGMPInfoVid": swL2IGMPInfoVid,
       "swL2IGMPInfoQueryCount": swL2IGMPInfoQueryCount,
       "swL2IGMPInfoTxQueryCount": swL2IGMPInfoTxQueryCount,
       "swL2IGMPInfoTable": swL2IGMPInfoTable,
       "swL2IGMPInfoEntry": swL2IGMPInfoEntry,
       "swL2IGMPVid": swL2IGMPVid,
       "swL2IGMPGroupIpAddr": swL2IGMPGroupIpAddr,
       "swL2IGMPMacAddr": swL2IGMPMacAddr,
       "swL2IGMPPortMap": swL2IGMPPortMap,
       "swL2IGMPIpGroupReportCount": swL2IGMPIpGroupReportCount,
       "swL2IGMPRouterPortsTable": swL2IGMPRouterPortsTable,
       "swL2IGMPRouterPortsEntry": swL2IGMPRouterPortsEntry,
       "swL2IGMPRouterPortsVid": swL2IGMPRouterPortsVid,
       "swL2IGMPRouterStaticPortList": swL2IGMPRouterStaticPortList,
       "swL2IGMPRouterDynamicPortList": swL2IGMPRouterDynamicPortList,
       "swL2IGMPRouterForbiddenPortList": swL2IGMPRouterForbiddenPortList,
       "swL2IGMPMulticastVlanTable": swL2IGMPMulticastVlanTable,
       "swL2IGMPMulticastVlanEntry": swL2IGMPMulticastVlanEntry,
       "swL2IGMPMulticastVlanid": swL2IGMPMulticastVlanid,
       "swL2IGMPMulticastVlanName": swL2IGMPMulticastVlanName,
       "swL2IGMPMulticastVlanSourcePort": swL2IGMPMulticastVlanSourcePort,
       "swL2IGMPMulticastVlanMemberPort": swL2IGMPMulticastVlanMemberPort,
       "swL2IGMPMulticastVlanTagMemberPort": swL2IGMPMulticastVlanTagMemberPort,
       "swL2IGMPMulticastVlanState": swL2IGMPMulticastVlanState,
       "swL2IGMPMulticastVlanReplaceSourceIp": swL2IGMPMulticastVlanReplaceSourceIp,
       "swL2IGMPMulticastVlanRowStatus": swL2IGMPMulticastVlanRowStatus,
       "swL2IGMPMulticastVlanRemoveAllMcastAddrListAction": swL2IGMPMulticastVlanRemoveAllMcastAddrListAction,
       "swL2IGMPMulticastVlanGroupTable": swL2IGMPMulticastVlanGroupTable,
       "swL2IGMPMulticastVlanGroupEntry": swL2IGMPMulticastVlanGroupEntry,
       "swL2IGMPMulticastVlanGroupVid": swL2IGMPMulticastVlanGroupVid,
       "swL2IGMPMulticastVlanGroupFromIp": swL2IGMPMulticastVlanGroupFromIp,
       "swL2IGMPMulticastVlanGroupToIp": swL2IGMPMulticastVlanGroupToIp,
       "swL2IGMPMulticastVlanGroupStatus": swL2IGMPMulticastVlanGroupStatus,
       "swIGMPSnoopingGroupTable": swIGMPSnoopingGroupTable,
       "swIGMPSnoopingGroupEntry": swIGMPSnoopingGroupEntry,
       "swIGMPSnoopingGroupVid": swIGMPSnoopingGroupVid,
       "swIGMPSnoopingGroupGroupAddr": swIGMPSnoopingGroupGroupAddr,
       "swIGMPSnoopingGroupSourceAddr": swIGMPSnoopingGroupSourceAddr,
       "swIGMPSnoopingGroupIncludePortMap": swIGMPSnoopingGroupIncludePortMap,
       "swIGMPSnoopingGroupExcludePortMap": swIGMPSnoopingGroupExcludePortMap,
       "swL2IGMPSnoopingStaticGroupTable": swL2IGMPSnoopingStaticGroupTable,
       "swL2IGMPSnoopingStaticGroupEntry": swL2IGMPSnoopingStaticGroupEntry,
       "swL2IGMPSnoopingStaticGroupVID": swL2IGMPSnoopingStaticGroupVID,
       "swL2IGMPSnoopingStaticGroupIPaddress": swL2IGMPSnoopingStaticGroupIPaddress,
       "swL2IGMPSnoopingStaticGroupMemberPortList": swL2IGMPSnoopingStaticGroupMemberPortList,
       "swL2IGMPSnoopingStaticGroupRowStatus": swL2IGMPSnoopingStaticGroupRowStatus,
       "swL2TrafficSegMgmt": swL2TrafficSegMgmt,
       "swL2TrafficSegTable": swL2TrafficSegTable,
       "swL2TrafficSegEntry": swL2TrafficSegEntry,
       "swL2TrafficSegPort": swL2TrafficSegPort,
       "swL2TrafficSegForwardPorts": swL2TrafficSegForwardPorts,
       "swL2IpLimitedMulticastMgmt": swL2IpLimitedMulticastMgmt,
       "swL2IpLimitedMulticastTable": swL2IpLimitedMulticastTable,
       "swL2IpLimitedMulticastEntry": swL2IpLimitedMulticastEntry,
       "swL2IpLimitedMulticastPortIndex": swL2IpLimitedMulticastPortIndex,
       "swL2IpLimitedMulticastHead": swL2IpLimitedMulticastHead,
       "swL2IpLimitedMulticastTail": swL2IpLimitedMulticastTail,
       "swL2IpLimitedMulticastAccess": swL2IpLimitedMulticastAccess,
       "swL2IpLimitedMulticastState": swL2IpLimitedMulticastState,
       "swL2IpLimitedMulticastDelState": swL2IpLimitedMulticastDelState,
       "swL2MgmtMIBTraps": swL2MgmtMIBTraps,
       "swL2Notify": swL2Notify,
       "swL2NotifyPrefix": swL2NotifyPrefix,
       "swL2NotifFirmware": swL2NotifFirmware,
       "swL2LoopDetectedNotify": swL2LoopDetectedNotify,
       "swL2PortLoopOccurred": swL2PortLoopOccurred,
       "swL2PortLoopRestart": swL2PortLoopRestart,
       "swL2VlanLoopOccurred": swL2VlanLoopOccurred,
       "swL2VlanLoopRestart": swL2VlanLoopRestart,
       "swL2macNotification": swL2macNotification,
       "swl2NotificationBidings": swl2NotificationBidings,
       "swL2macNotifyInfo": swL2macNotifyInfo,
       "swL2VlanLoopDetectVID": swL2VlanLoopDetectVID,
       "swL2VlanMgmt": swL2VlanMgmt,
       "swL2VlanTable": swL2VlanTable,
       "swL2VlanEntry": swL2VlanEntry,
       "swL2VlanIndex": swL2VlanIndex,
       "swL2VlanName": swL2VlanName,
       "swL2VlanType": swL2VlanType,
       "swL2VlanMemberPorts": swL2VlanMemberPorts,
       "swL2VlanStaticPorts": swL2VlanStaticPorts,
       "swL2VlanStaticTaggedPorts": swL2VlanStaticTaggedPorts,
       "swL2VlanStaticUntaggedPorts": swL2VlanStaticUntaggedPorts,
       "swL2VlanForbiddenPorts": swL2VlanForbiddenPorts,
       "swL2VlanCurrentTaggedPorts": swL2VlanCurrentTaggedPorts,
       "swL2VlanCurrentUntaggedPorts": swL2VlanCurrentUntaggedPorts,
       "swL2VlanAdvertisementState": swL2VlanAdvertisementState,
       "swL2PVIDAutoAssignmentState": swL2PVIDAutoAssignmentState,
       "swL2LoopDetectMgmt": swL2LoopDetectMgmt,
       "swL2LoopDetectCtrl": swL2LoopDetectCtrl,
       "swL2LoopDetectAdminState": swL2LoopDetectAdminState,
       "swL2LoopDetectInterval": swL2LoopDetectInterval,
       "swL2LoopDetectRecoverTime": swL2LoopDetectRecoverTime,
       "swL2LoopDetectMode": swL2LoopDetectMode,
       "swL2LoopDetectTrapMode": swL2LoopDetectTrapMode,
       "swL2LoopDetectPortMgmt": swL2LoopDetectPortMgmt,
       "swL2LoopDetectPortTable": swL2LoopDetectPortTable,
       "swL2LoopDetectPortEntry": swL2LoopDetectPortEntry,
       "swL2LoopDetectPortIndex": swL2LoopDetectPortIndex,
       "swL2LoopDetectPortState": swL2LoopDetectPortState,
       "swL2LoopDetectPortLoopVLAN": swL2LoopDetectPortLoopVLAN,
       "swL2LoopDetectPortLoopStatus": swL2LoopDetectPortLoopStatus}
)

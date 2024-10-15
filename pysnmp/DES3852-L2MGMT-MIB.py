# SNMP MIB module (DES3852-L2MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DES3852-L2MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:25:56 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")

(des3852,) = mibBuilder.importSymbols(
    "SW3800PRIMGMT-MIB",
    "des3852")


# MODULE-IDENTITY

swL2MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2)
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




class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwL2DevMgmt_ObjectIdentity = ObjectIdentity
swL2DevMgmt = _SwL2DevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1)
)
_SwL2DevInfo_ObjectIdentity = ObjectIdentity
swL2DevInfo = _SwL2DevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1)
)
_SwDevInfoSystemUpTime_Type = TimeTicks
_SwDevInfoSystemUpTime_Object = MibScalar
swDevInfoSystemUpTime = _SwDevInfoSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1, 4),
    _SwDevInfoConsoleInUse_Type()
)
swDevInfoConsoleInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoConsoleInUse.setStatus("current")
_SwDevInfoModuleType_Type = OctetString
_SwDevInfoModuleType_Object = MibScalar
swDevInfoModuleType = _SwDevInfoModuleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1, 5),
    _SwDevInfoModuleType_Type()
)
swDevInfoModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoModuleType.setStatus("current")


class _SwDevInfoFrontPanelLedMode_Type(Integer32):
    """Custom type swDevInfoFrontPanelLedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("poeStatusMode", 2),
          ("portStatusMode", 1))
    )


_SwDevInfoFrontPanelLedMode_Type.__name__ = "Integer32"
_SwDevInfoFrontPanelLedMode_Object = MibScalar
swDevInfoFrontPanelLedMode = _SwDevInfoFrontPanelLedMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1, 6),
    _SwDevInfoFrontPanelLedMode_Type()
)
swDevInfoFrontPanelLedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoFrontPanelLedMode.setStatus("current")
_SwDevInfoPowerTable_Object = MibTable
swDevInfoPowerTable = _SwDevInfoPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    swDevInfoPowerTable.setStatus("current")
_SwDevInfoPowerEntry_Object = MibTableRow
swDevInfoPowerEntry = _SwDevInfoPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1, 8, 1)
)
swDevInfoPowerEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swDevInfoPowerUnitIndex"),
    (0, "DES3852-L2MGMT-MIB", "swDevInfoPowerID"),
)
if mibBuilder.loadTexts:
    swDevInfoPowerEntry.setStatus("current")


class _SwDevInfoPowerUnitIndex_Type(Integer32):
    """Custom type swDevInfoPowerUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwDevInfoPowerUnitIndex_Type.__name__ = "Integer32"
_SwDevInfoPowerUnitIndex_Object = MibTableColumn
swDevInfoPowerUnitIndex = _SwDevInfoPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1, 8, 1, 1),
    _SwDevInfoPowerUnitIndex_Type()
)
swDevInfoPowerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoPowerUnitIndex.setStatus("current")


class _SwDevInfoPowerID_Type(Integer32):
    """Custom type swDevInfoPowerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwDevInfoPowerID_Type.__name__ = "Integer32"
_SwDevInfoPowerID_Object = MibTableColumn
swDevInfoPowerID = _SwDevInfoPowerID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1, 8, 1, 2),
    _SwDevInfoPowerID_Type()
)
swDevInfoPowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoPowerID.setStatus("current")


class _SwDevInfoPowerStatus_Type(Integer32):
    """Custom type swDevInfoPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connect", 5),
          ("disconnect", 6),
          ("fail", 4),
          ("lowVoltage", 1),
          ("other", 0),
          ("overCurrent", 2),
          ("working", 3))
    )


_SwDevInfoPowerStatus_Type.__name__ = "Integer32"
_SwDevInfoPowerStatus_Object = MibTableColumn
swDevInfoPowerStatus = _SwDevInfoPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 1, 8, 1, 3),
    _SwDevInfoPowerStatus_Type()
)
swDevInfoPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoPowerStatus.setStatus("current")
_SwL2DevCtrl_ObjectIdentity = ObjectIdentity
swL2DevCtrl = _SwL2DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2, 4),
    _SwL2DevCtrlCleanAllStatisticCounter_Type()
)
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCleanAllStatisticCounter.setStatus("current")
_SwL2DevCtrlVlanIdOfFDBTbl_Type = VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object = MibScalar
swL2DevCtrlVlanIdOfFDBTbl = _SwL2DevCtrlVlanIdOfFDBTbl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2, 5),
    _SwL2DevCtrlVlanIdOfFDBTbl_Type()
)
swL2DevCtrlVlanIdOfFDBTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlVlanIdOfFDBTbl.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2, 8),
    _SwL2MACNotifyInterval_Type()
)
swL2MACNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MACNotifyInterval.setStatus("current")
_SwL2DevCtrlTelnet_ObjectIdentity = ObjectIdentity
swL2DevCtrlTelnet = _SwL2DevCtrlTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2, 10)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2, 10, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 2, 10, 2),
    _SwL2DevCtrlTelnetTcpPort_Type()
)
swL2DevCtrlTelnetTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlTelnetTcpPort.setStatus("current")
_SwL2DevAlarm_ObjectIdentity = ObjectIdentity
swL2DevAlarm = _SwL2DevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 1, 3, 3),
    _SwL2DevAlarmLinkChange_Type()
)
swL2DevAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmLinkChange.setStatus("current")
_SwL2VlanMgmt_ObjectIdentity = ObjectIdentity
swL2VlanMgmt = _SwL2VlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 3)
)
_SwL2VlanAdvertisementTable_Object = MibTable
swL2VlanAdvertisementTable = _SwL2VlanAdvertisementTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    swL2VlanAdvertisementTable.setStatus("current")
_SwL2VlanAdvertisementEntry_Object = MibTableRow
swL2VlanAdvertisementEntry = _SwL2VlanAdvertisementEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 3, 1, 1)
)
swL2VlanAdvertisementEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2VlanIndex"),
)
if mibBuilder.loadTexts:
    swL2VlanAdvertisementEntry.setStatus("current")


class _SwL2VlanIndex_Type(Integer32):
    """Custom type swL2VlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2VlanIndex_Type.__name__ = "Integer32"
_SwL2VlanIndex_Object = MibTableColumn
swL2VlanIndex = _SwL2VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 3, 1, 1, 1),
    _SwL2VlanIndex_Type()
)
swL2VlanIndex.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 3, 1, 1, 2),
    _SwL2VlanName_Type()
)
swL2VlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanName.setStatus("current")


class _SwL2VlanAdvertiseState_Type(Integer32):
    """Custom type swL2VlanAdvertiseState based on Integer32"""
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


_SwL2VlanAdvertiseState_Type.__name__ = "Integer32"
_SwL2VlanAdvertiseState_Object = MibTableColumn
swL2VlanAdvertiseState = _SwL2VlanAdvertiseState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 3, 1, 1, 3),
    _SwL2VlanAdvertiseState_Type()
)
swL2VlanAdvertiseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2VlanAdvertiseState.setStatus("current")
_SwL2PortMgmt_ObjectIdentity = ObjectIdentity
swL2PortMgmt = _SwL2PortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4)
)
_SwL2PortInfoTable_Object = MibTable
swL2PortInfoTable = _SwL2PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    swL2PortInfoTable.setStatus("obsolete")
_SwL2PortInfoEntry_Object = MibTableRow
swL2PortInfoEntry = _SwL2PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 1, 1)
)
swL2PortInfoEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2PortInfoPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortInfoEntry.setStatus("obsolete")


class _SwL2PortInfoPortIndex_Type(Integer32):
    """Custom type swL2PortInfoPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortInfoPortIndex_Type.__name__ = "Integer32"
_SwL2PortInfoPortIndex_Object = MibTableColumn
swL2PortInfoPortIndex = _SwL2PortInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 1, 1, 1),
    _SwL2PortInfoPortIndex_Type()
)
swL2PortInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoPortIndex.setStatus("obsolete")


class _SwL2PortInfoUnitIndex_Type(Integer32):
    """Custom type swL2PortInfoUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortInfoUnitIndex_Type.__name__ = "Integer32"
_SwL2PortInfoUnitIndex_Object = MibTableColumn
swL2PortInfoUnitIndex = _SwL2PortInfoUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 1, 1, 2),
    _SwL2PortInfoUnitIndex_Type()
)
swL2PortInfoUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoUnitIndex.setStatus("obsolete")


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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 7),
          ("portType-1000Base-LX", 6),
          ("portType-1000Base-SX", 5),
          ("portType-1000Base-TX", 4),
          ("portType-100Base-FL", 3),
          ("portType-100Base-FX", 2),
          ("portType-100Base-TX", 1))
    )


_SwL2PortInfoType_Type.__name__ = "Integer32"
_SwL2PortInfoType_Object = MibTableColumn
swL2PortInfoType = _SwL2PortInfoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 1, 1, 3),
    _SwL2PortInfoType_Type()
)
swL2PortInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoType.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 1, 1, 4),
    _SwL2PortInfoLinkStatus_Type()
)
swL2PortInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoLinkStatus.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 1, 1, 5),
    _SwL2PortInfoNwayStatus_Type()
)
swL2PortInfoNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoNwayStatus.setStatus("obsolete")


class _SwL2PortInfoModuleType_Type(Integer32):
    """Custom type swL2PortInfoModuleType based on Integer32"""
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
        *(("moduleType-1000T", 2),
          ("moduleType-BaseModule", 3),
          ("moduleType-COMBO", 1),
          ("none", 0))
    )


_SwL2PortInfoModuleType_Type.__name__ = "Integer32"
_SwL2PortInfoModuleType_Object = MibTableColumn
swL2PortInfoModuleType = _SwL2PortInfoModuleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 1, 1, 6),
    _SwL2PortInfoModuleType_Type()
)
swL2PortInfoModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoModuleType.setStatus("obsolete")


class _SwL2PortInfoErrorDisabled_Type(Integer32):
    """Custom type swL2PortInfoErrorDisabled based on Integer32"""
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
        *(("lbd", 2),
          ("none", 0),
          ("storm", 1),
          ("unknow", 3))
    )


_SwL2PortInfoErrorDisabled_Type.__name__ = "Integer32"
_SwL2PortInfoErrorDisabled_Object = MibTableColumn
swL2PortInfoErrorDisabled = _SwL2PortInfoErrorDisabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 1, 1, 7),
    _SwL2PortInfoErrorDisabled_Type()
)
swL2PortInfoErrorDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoErrorDisabled.setStatus("obsolete")
_SwL2PortCtrlTable_Object = MibTable
swL2PortCtrlTable = _SwL2PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 2)
)
if mibBuilder.loadTexts:
    swL2PortCtrlTable.setStatus("obsolete")
_SwL2PortCtrlEntry_Object = MibTableRow
swL2PortCtrlEntry = _SwL2PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 2, 1)
)
swL2PortCtrlEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2PortCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortCtrlEntry.setStatus("obsolete")


class _SwL2PortCtrlPortIndex_Type(Integer32):
    """Custom type swL2PortCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortCtrlPortIndex_Type.__name__ = "Integer32"
_SwL2PortCtrlPortIndex_Object = MibTableColumn
swL2PortCtrlPortIndex = _SwL2PortCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 2, 1, 1),
    _SwL2PortCtrlPortIndex_Type()
)
swL2PortCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlPortIndex.setStatus("obsolete")


class _SwL2PortCtrlUnitIndex_Type(Integer32):
    """Custom type swL2PortCtrlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortCtrlUnitIndex_Type.__name__ = "Integer32"
_SwL2PortCtrlUnitIndex_Object = MibTableColumn
swL2PortCtrlUnitIndex = _SwL2PortCtrlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 2, 1, 2),
    _SwL2PortCtrlUnitIndex_Type()
)
swL2PortCtrlUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlUnitIndex.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 2, 1, 3),
    _SwL2PortCtrlAdminState_Type()
)
swL2PortCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAdminState.setStatus("obsolete")


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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("nway-disabled-100Mbps-Full", 6),
          ("nway-disabled-100Mbps-Half", 5),
          ("nway-disabled-10Mbps-Full", 4),
          ("nway-disabled-10Mbps-Half", 3),
          ("nway-disabled-1Gigabps-Full", 8),
          ("nway-disabled-1Gigabps-Half", 7),
          ("nway-enabled", 2),
          ("other", 1))
    )


_SwL2PortCtrlNwayState_Type.__name__ = "Integer32"
_SwL2PortCtrlNwayState_Object = MibTableColumn
swL2PortCtrlNwayState = _SwL2PortCtrlNwayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 2, 1, 4),
    _SwL2PortCtrlNwayState_Type()
)
swL2PortCtrlNwayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlNwayState.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 2, 1, 5),
    _SwL2PortCtrlFlowCtrlState_Type()
)
swL2PortCtrlFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlFlowCtrlState.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 2, 1, 6),
    _SwL2PortCtrlLockState_Type()
)
swL2PortCtrlLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlLockState.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 2, 1, 7),
    _SwL2PortCtrlMACNotifyState_Type()
)
swL2PortCtrlMACNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlMACNotifyState.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 3),
    _SwL2PortCtrlJumboFrame_Type()
)
swL2PortCtrlJumboFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlJumboFrame.setStatus("current")
_SwL2PortInformationTable_Object = MibTable
swL2PortInformationTable = _SwL2PortInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 4)
)
if mibBuilder.loadTexts:
    swL2PortInformationTable.setStatus("current")
_SwL2PortInformationEntry_Object = MibTableRow
swL2PortInformationEntry = _SwL2PortInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 4, 1)
)
swL2PortInformationEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2PortInformationPortIndex"),
    (0, "DES3852-L2MGMT-MIB", "swL2PortInformationMediumType"),
)
if mibBuilder.loadTexts:
    swL2PortInformationEntry.setStatus("current")


class _SwL2PortInformationPortIndex_Type(Integer32):
    """Custom type swL2PortInformationPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortInformationPortIndex_Type.__name__ = "Integer32"
_SwL2PortInformationPortIndex_Object = MibTableColumn
swL2PortInformationPortIndex = _SwL2PortInformationPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 4, 1, 1),
    _SwL2PortInformationPortIndex_Type()
)
swL2PortInformationPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInformationPortIndex.setStatus("current")


class _SwL2PortInformationMediumType_Type(Integer32):
    """Custom type swL2PortInformationMediumType based on Integer32"""
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


_SwL2PortInformationMediumType_Type.__name__ = "Integer32"
_SwL2PortInformationMediumType_Object = MibTableColumn
swL2PortInformationMediumType = _SwL2PortInformationMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 4, 1, 2),
    _SwL2PortInformationMediumType_Type()
)
swL2PortInformationMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInformationMediumType.setStatus("current")


class _SwL2PortInformationUnitID_Type(Integer32):
    """Custom type swL2PortInformationUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortInformationUnitID_Type.__name__ = "Integer32"
_SwL2PortInformationUnitID_Object = MibTableColumn
swL2PortInformationUnitID = _SwL2PortInformationUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 4, 1, 3),
    _SwL2PortInformationUnitID_Type()
)
swL2PortInformationUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInformationUnitID.setStatus("current")


class _SwL2PortInformationType_Type(Integer32):
    """Custom type swL2PortInformationType based on Integer32"""
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
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("portType-1000Base-1394", 10),
          ("portType-1000Base-LX", 6),
          ("portType-1000Base-LX-GBIC", 8),
          ("portType-1000Base-LX-MGBIC", 14),
          ("portType-1000Base-SX", 5),
          ("portType-1000Base-SX-GBIC", 7),
          ("portType-1000Base-SX-MGBIC", 13),
          ("portType-1000Base-TX", 4),
          ("portType-1000Base-TX-GBIC", 9),
          ("portType-1000Base-TX-GBIC-COMBO", 11),
          ("portType-1000Base-TX-MGBIC", 15),
          ("portType-1000Base-none-GBIC", 12),
          ("portType-1000Base-none-MGBIC", 16),
          ("portType-100Base-FL", 3),
          ("portType-100Base-FX", 2),
          ("portType-100Base-TX", 1),
          ("portType-10G", 18),
          ("portType-10G-xenpak-1310nm", 19),
          ("portType-10G-xenpak-850nm", 20),
          ("portType-10G-xenpak-empty", 21),
          ("portType-10G-xfp-1310nm", 22),
          ("portType-10G-xfp-850nm", 23),
          ("portType-10G-xfp-empty", 24),
          ("portType-SIO", 17),
          ("portType-none", 25))
    )


_SwL2PortInformationType_Type.__name__ = "Integer32"
_SwL2PortInformationType_Object = MibTableColumn
swL2PortInformationType = _SwL2PortInformationType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 4, 1, 4),
    _SwL2PortInformationType_Type()
)
swL2PortInformationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInformationType.setStatus("current")


class _SwL2PortInformationLinkStatus_Type(Integer32):
    """Custom type swL2PortInformationLinkStatus based on Integer32"""
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


_SwL2PortInformationLinkStatus_Type.__name__ = "Integer32"
_SwL2PortInformationLinkStatus_Object = MibTableColumn
swL2PortInformationLinkStatus = _SwL2PortInformationLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 4, 1, 5),
    _SwL2PortInformationLinkStatus_Type()
)
swL2PortInformationLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInformationLinkStatus.setStatus("current")


class _SwL2PortInformationNwayStatus_Type(Integer32):
    """Custom type swL2PortInformationNwayStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("full-100Mbps", 6),
          ("full-10Gigabps", 9),
          ("full-10Mbps", 4),
          ("full-1Gigabps", 8),
          ("half-100Mbps", 5),
          ("half-10Mbps", 3),
          ("half-1Gigabps", 7),
          ("link-down", 2),
          ("other", 0))
    )


_SwL2PortInformationNwayStatus_Type.__name__ = "Integer32"
_SwL2PortInformationNwayStatus_Object = MibTableColumn
swL2PortInformationNwayStatus = _SwL2PortInformationNwayStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 4, 1, 6),
    _SwL2PortInformationNwayStatus_Type()
)
swL2PortInformationNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInformationNwayStatus.setStatus("current")


class _SwL2PortInformationModuleType_Type(Integer32):
    """Custom type swL2PortInformationModuleType based on Integer32"""
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
              26)
        )
    )
    namedValues = NamedValues(
        *(("moduleType-1000T", 3),
          ("moduleType-1394", 2),
          ("moduleType-1P-100FL", 23),
          ("moduleType-1P-100FX", 21),
          ("moduleType-1P-GBIC", 15),
          ("moduleType-1P-GBIC-1P-STACK", 18),
          ("moduleType-1P-GBIC-1P-TX", 17),
          ("moduleType-1P-MTRJ-LX", 13),
          ("moduleType-1P-MTRJ-SX", 11),
          ("moduleType-1P-SC-LX", 7),
          ("moduleType-1P-SC-SX", 5),
          ("moduleType-1P-TX", 9),
          ("moduleType-2P-100FL", 24),
          ("moduleType-2P-100FX", 20),
          ("moduleType-2P-100FX-NEW", 22),
          ("moduleType-2P-100TX", 25),
          ("moduleType-2P-GBIC", 16),
          ("moduleType-2P-MTRJ-LX", 14),
          ("moduleType-2P-MTRJ-SX", 12),
          ("moduleType-2P-SC-LX", 8),
          ("moduleType-2P-SC-SX", 6),
          ("moduleType-2P-STACK", 19),
          ("moduleType-2P-TX", 10),
          ("moduleType-BaseModule-24PORT", 26),
          ("moduleType-COMBO", 1),
          ("moduleType-MGBIC", 4),
          ("none", 0))
    )


_SwL2PortInformationModuleType_Type.__name__ = "Integer32"
_SwL2PortInformationModuleType_Object = MibTableColumn
swL2PortInformationModuleType = _SwL2PortInformationModuleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 4, 1, 7),
    _SwL2PortInformationModuleType_Type()
)
swL2PortInformationModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInformationModuleType.setStatus("current")


class _SwL2PortInformationErrorDisabled_Type(Integer32):
    """Custom type swL2PortInformationErrorDisabled based on Integer32"""
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
        *(("lbd", 2),
          ("none", 0),
          ("storm", 1),
          ("unknow", 3))
    )


_SwL2PortInformationErrorDisabled_Type.__name__ = "Integer32"
_SwL2PortInformationErrorDisabled_Object = MibTableColumn
swL2PortInformationErrorDisabled = _SwL2PortInformationErrorDisabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 4, 1, 8),
    _SwL2PortInformationErrorDisabled_Type()
)
swL2PortInformationErrorDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInformationErrorDisabled.setStatus("current")
_SwL2PortControlTable_Object = MibTable
swL2PortControlTable = _SwL2PortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 5)
)
if mibBuilder.loadTexts:
    swL2PortControlTable.setStatus("current")
_SwL2PortControlEntry_Object = MibTableRow
swL2PortControlEntry = _SwL2PortControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 5, 1)
)
swL2PortControlEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2PortControlPortIndex"),
    (0, "DES3852-L2MGMT-MIB", "swL2PortControlMediumType"),
)
if mibBuilder.loadTexts:
    swL2PortControlEntry.setStatus("current")


class _SwL2PortControlPortIndex_Type(Integer32):
    """Custom type swL2PortControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortControlPortIndex_Type.__name__ = "Integer32"
_SwL2PortControlPortIndex_Object = MibTableColumn
swL2PortControlPortIndex = _SwL2PortControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 5, 1, 1),
    _SwL2PortControlPortIndex_Type()
)
swL2PortControlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortControlPortIndex.setStatus("current")


class _SwL2PortControlMediumType_Type(Integer32):
    """Custom type swL2PortControlMediumType based on Integer32"""
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


_SwL2PortControlMediumType_Type.__name__ = "Integer32"
_SwL2PortControlMediumType_Object = MibTableColumn
swL2PortControlMediumType = _SwL2PortControlMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 5, 1, 2),
    _SwL2PortControlMediumType_Type()
)
swL2PortControlMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortControlMediumType.setStatus("current")


class _SwL2PortControlUnitIndex_Type(Integer32):
    """Custom type swL2PortControlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortControlUnitIndex_Type.__name__ = "Integer32"
_SwL2PortControlUnitIndex_Object = MibTableColumn
swL2PortControlUnitIndex = _SwL2PortControlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 5, 1, 3),
    _SwL2PortControlUnitIndex_Type()
)
swL2PortControlUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortControlUnitIndex.setStatus("current")


class _SwL2PortControlAdminState_Type(Integer32):
    """Custom type swL2PortControlAdminState based on Integer32"""
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


_SwL2PortControlAdminState_Type.__name__ = "Integer32"
_SwL2PortControlAdminState_Object = MibTableColumn
swL2PortControlAdminState = _SwL2PortControlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 5, 1, 4),
    _SwL2PortControlAdminState_Type()
)
swL2PortControlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortControlAdminState.setStatus("current")


class _SwL2PortControlNwayState_Type(Integer32):
    """Custom type swL2PortControlNwayState based on Integer32"""
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
        *(("nway-disabled-100Mbps-Full", 6),
          ("nway-disabled-100Mbps-Half", 5),
          ("nway-disabled-10Mbps-Full", 4),
          ("nway-disabled-10Mbps-Half", 3),
          ("nway-disabled-1Gigabps-Full", 8),
          ("nway-disabled-1Gigabps-Full-master", 9),
          ("nway-disabled-1Gigabps-Full-slave", 10),
          ("nway-disabled-1Gigabps-Half", 7),
          ("nway-enabled", 2),
          ("other", 1))
    )


_SwL2PortControlNwayState_Type.__name__ = "Integer32"
_SwL2PortControlNwayState_Object = MibTableColumn
swL2PortControlNwayState = _SwL2PortControlNwayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 5, 1, 5),
    _SwL2PortControlNwayState_Type()
)
swL2PortControlNwayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortControlNwayState.setStatus("current")


class _SwL2PortControlFlowCtrlState_Type(Integer32):
    """Custom type swL2PortControlFlowCtrlState based on Integer32"""
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


_SwL2PortControlFlowCtrlState_Type.__name__ = "Integer32"
_SwL2PortControlFlowCtrlState_Object = MibTableColumn
swL2PortControlFlowCtrlState = _SwL2PortControlFlowCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 5, 1, 6),
    _SwL2PortControlFlowCtrlState_Type()
)
swL2PortControlFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortControlFlowCtrlState.setStatus("current")


class _SwL2PortControlLearningState_Type(Integer32):
    """Custom type swL2PortControlLearningState based on Integer32"""
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


_SwL2PortControlLearningState_Type.__name__ = "Integer32"
_SwL2PortControlLearningState_Object = MibTableColumn
swL2PortControlLearningState = _SwL2PortControlLearningState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 5, 1, 7),
    _SwL2PortControlLearningState_Type()
)
swL2PortControlLearningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortControlLearningState.setStatus("current")


class _SwL2PortControlMACNotifyState_Type(Integer32):
    """Custom type swL2PortControlMACNotifyState based on Integer32"""
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


_SwL2PortControlMACNotifyState_Type.__name__ = "Integer32"
_SwL2PortControlMACNotifyState_Object = MibTableColumn
swL2PortControlMACNotifyState = _SwL2PortControlMACNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 5, 1, 8),
    _SwL2PortControlMACNotifyState_Type()
)
swL2PortControlMACNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortControlMACNotifyState.setStatus("current")


class _SwL2PortControlMulticastfilter_Type(Integer32):
    """Custom type swL2PortControlMulticastfilter based on Integer32"""
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
        *(("filter-unregistered-groups", 3),
          ("forward-all-groups", 1),
          ("forward-unregistered-groups", 2),
          ("other", 0))
    )


_SwL2PortControlMulticastfilter_Type.__name__ = "Integer32"
_SwL2PortControlMulticastfilter_Object = MibTableColumn
swL2PortControlMulticastfilter = _SwL2PortControlMulticastfilter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 4, 5, 1, 9),
    _SwL2PortControlMulticastfilter_Type()
)
swL2PortControlMulticastfilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortControlMulticastfilter.setStatus("current")
_SwL2QOSMgmt_ObjectIdentity = ObjectIdentity
swL2QOSMgmt = _SwL2QOSMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6)
)
_SwL2QOSBandwidthControlTable_Object = MibTable
swL2QOSBandwidthControlTable = _SwL2QOSBandwidthControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 1)
)
if mibBuilder.loadTexts:
    swL2QOSBandwidthControlTable.setStatus("current")
_SwL2QOSBandwidthControlEntry_Object = MibTableRow
swL2QOSBandwidthControlEntry = _SwL2QOSBandwidthControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 1, 1)
)
swL2QOSBandwidthControlEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2QOSBandwidthPortIndex"),
)
if mibBuilder.loadTexts:
    swL2QOSBandwidthControlEntry.setStatus("current")


class _SwL2QOSBandwidthPortIndex_Type(Integer32):
    """Custom type swL2QOSBandwidthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 650),
    )


_SwL2QOSBandwidthPortIndex_Type.__name__ = "Integer32"
_SwL2QOSBandwidthPortIndex_Object = MibTableColumn
swL2QOSBandwidthPortIndex = _SwL2QOSBandwidthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 1, 1, 1),
    _SwL2QOSBandwidthPortIndex_Type()
)
swL2QOSBandwidthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthPortIndex.setStatus("current")


class _SwL2QOSBandwidthRxRate_Type(Integer32):
    """Custom type swL2QOSBandwidthRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SwL2QOSBandwidthRxRate_Type.__name__ = "Integer32"
_SwL2QOSBandwidthRxRate_Object = MibTableColumn
swL2QOSBandwidthRxRate = _SwL2QOSBandwidthRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 1, 1, 2),
    _SwL2QOSBandwidthRxRate_Type()
)
swL2QOSBandwidthRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRxRate.setStatus("current")


class _SwL2QOSBandwidthTxRate_Type(Integer32):
    """Custom type swL2QOSBandwidthTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SwL2QOSBandwidthTxRate_Type.__name__ = "Integer32"
_SwL2QOSBandwidthTxRate_Object = MibTableColumn
swL2QOSBandwidthTxRate = _SwL2QOSBandwidthTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 1, 1, 3),
    _SwL2QOSBandwidthTxRate_Type()
)
swL2QOSBandwidthTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSBandwidthTxRate.setStatus("current")
_SwL2QOSBandwidthRadiusRxRate_Type = Integer32
_SwL2QOSBandwidthRadiusRxRate_Object = MibTableColumn
swL2QOSBandwidthRadiusRxRate = _SwL2QOSBandwidthRadiusRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 1, 1, 4),
    _SwL2QOSBandwidthRadiusRxRate_Type()
)
swL2QOSBandwidthRadiusRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRadiusRxRate.setStatus("current")
_SwL2QOSBandwidthRadiusTxRate_Type = Integer32
_SwL2QOSBandwidthRadiusTxRate_Object = MibTableColumn
swL2QOSBandwidthRadiusTxRate = _SwL2QOSBandwidthRadiusTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 1, 1, 5),
    _SwL2QOSBandwidthRadiusTxRate_Type()
)
swL2QOSBandwidthRadiusTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRadiusTxRate.setStatus("current")
_SwL2QOSSchedulingTable_Object = MibTable
swL2QOSSchedulingTable = _SwL2QOSSchedulingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 2)
)
if mibBuilder.loadTexts:
    swL2QOSSchedulingTable.setStatus("current")
_SwL2QOSSchedulingEntry_Object = MibTableRow
swL2QOSSchedulingEntry = _SwL2QOSSchedulingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 2, 1)
)
swL2QOSSchedulingEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2QOSSchedulingClassIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 2, 1, 2),
    _SwL2QOSSchedulingMaxPkts_Type()
)
swL2QOSSchedulingMaxPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSSchedulingMaxPkts.setStatus("current")
_SwL2QOS8021pUserPriorityTable_Object = MibTable
swL2QOS8021pUserPriorityTable = _SwL2QOS8021pUserPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 3)
)
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityTable.setStatus("current")
_SwL2QOS8021pUserPriorityEntry_Object = MibTableRow
swL2QOS8021pUserPriorityEntry = _SwL2QOS8021pUserPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 3, 1)
)
swL2QOS8021pUserPriorityEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2QOS8021pUserPriorityIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 3, 1, 1),
    _SwL2QOS8021pUserPriorityIndex_Type()
)
swL2QOS8021pUserPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityIndex.setStatus("current")


class _SwL2QOS8021pUserPriorityClass_Type(Integer32):
    """Custom type swL2QOS8021pUserPriorityClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2QOS8021pUserPriorityClass_Type.__name__ = "Integer32"
_SwL2QOS8021pUserPriorityClass_Object = MibTableColumn
swL2QOS8021pUserPriorityClass = _SwL2QOS8021pUserPriorityClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 3, 1, 2),
    _SwL2QOS8021pUserPriorityClass_Type()
)
swL2QOS8021pUserPriorityClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityClass.setStatus("current")
_SwL2QOS8021pDefaultPriorityTable_Object = MibTable
swL2QOS8021pDefaultPriorityTable = _SwL2QOS8021pDefaultPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 4)
)
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityTable.setStatus("current")
_SwL2QOS8021pDefaultPriorityEntry_Object = MibTableRow
swL2QOS8021pDefaultPriorityEntry = _SwL2QOS8021pDefaultPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 4, 1)
)
swL2QOS8021pDefaultPriorityEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2QOS8021pDefaultPriorityIndex"),
)
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityEntry.setStatus("current")


class _SwL2QOS8021pDefaultPriorityIndex_Type(Integer32):
    """Custom type swL2QOS8021pDefaultPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 650),
    )


_SwL2QOS8021pDefaultPriorityIndex_Type.__name__ = "Integer32"
_SwL2QOS8021pDefaultPriorityIndex_Object = MibTableColumn
swL2QOS8021pDefaultPriorityIndex = _SwL2QOS8021pDefaultPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 4, 1, 2),
    _SwL2QOS8021pDefaultPriority_Type()
)
swL2QOS8021pDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriority.setStatus("current")
_SwL2QOS8021pRadiusPriority_Type = Integer32
_SwL2QOS8021pRadiusPriority_Object = MibTableColumn
swL2QOS8021pRadiusPriority = _SwL2QOS8021pRadiusPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 6, 4, 1, 3),
    _SwL2QOS8021pRadiusPriority_Type()
)
swL2QOS8021pRadiusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOS8021pRadiusPriority.setStatus("current")
_SwL2TrunkMgmt_ObjectIdentity = ObjectIdentity
swL2TrunkMgmt = _SwL2TrunkMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 2),
    _SwL2TrunkCurrentNumEntries_Type()
)
swL2TrunkCurrentNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkCurrentNumEntries.setStatus("current")
_SwL2TrunkCtrlTable_Object = MibTable
swL2TrunkCtrlTable = _SwL2TrunkCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 3)
)
if mibBuilder.loadTexts:
    swL2TrunkCtrlTable.setStatus("current")
_SwL2TrunkCtrlEntry_Object = MibTableRow
swL2TrunkCtrlEntry = _SwL2TrunkCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 3, 1)
)
swL2TrunkCtrlEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2TrunkIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 3, 1, 3),
    _SwL2TrunkMasterPort_Type()
)
swL2TrunkMasterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkMasterPort.setStatus("current")
_SwL2TrunkMember_Type = PortList
_SwL2TrunkMember_Object = MibTableColumn
swL2TrunkMember = _SwL2TrunkMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 3, 1, 6),
    _SwL2TrunkType_Type()
)
swL2TrunkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkType.setStatus("current")
_SwL2TrunkState_Type = RowStatus
_SwL2TrunkState_Object = MibTableColumn
swL2TrunkState = _SwL2TrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 3, 1, 7),
    _SwL2TrunkState_Type()
)
swL2TrunkState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 8, 4),
    _SwL2TrunkAlgorithm_Type()
)
swL2TrunkAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkAlgorithm.setStatus("current")
_SwL2MirrorMgmt_ObjectIdentity = ObjectIdentity
swL2MirrorMgmt = _SwL2MirrorMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 9, 1),
    _SwL2MirrorLogicTargetPort_Type()
)
swL2MirrorLogicTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorLogicTargetPort.setStatus("current")
_SwL2MirrorPortSourceIngress_Type = PortList
_SwL2MirrorPortSourceIngress_Object = MibScalar
swL2MirrorPortSourceIngress = _SwL2MirrorPortSourceIngress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 9, 2),
    _SwL2MirrorPortSourceIngress_Type()
)
swL2MirrorPortSourceIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortSourceIngress.setStatus("current")
_SwL2MirrorPortSourceEgress_Type = PortList
_SwL2MirrorPortSourceEgress_Object = MibScalar
swL2MirrorPortSourceEgress = _SwL2MirrorPortSourceEgress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 9, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 9, 4),
    _SwL2MirrorPortState_Type()
)
swL2MirrorPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortState.setStatus("current")
_SwL2IGMPMgmt_ObjectIdentity = ObjectIdentity
swL2IGMPMgmt = _SwL2IGMPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 1),
    _SwL2IGMPMaxSupportedVlans_Type()
)
swL2IGMPMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMaxSupportedVlans.setStatus("current")
_SwL2IGMPCtrlTable_Object = MibTable
swL2IGMPCtrlTable = _SwL2IGMPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3)
)
if mibBuilder.loadTexts:
    swL2IGMPCtrlTable.setStatus("current")
_SwL2IGMPCtrlEntry_Object = MibTableRow
swL2IGMPCtrlEntry = _SwL2IGMPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1)
)
swL2IGMPCtrlEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2IGMPCtrlVid"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 7),
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
        ValueRangeConstraint(0, 16711450),
    )


_SwL2IGMPLeaveTimer_Type.__name__ = "Integer32"
_SwL2IGMPLeaveTimer_Object = MibTableColumn
swL2IGMPLeaveTimer = _SwL2IGMPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 3, 1, 12),
    _SwL2IGMPFastLeaveState_Type()
)
swL2IGMPFastLeaveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPFastLeaveState.setStatus("current")
_SwL2IGMPQueryInfoTable_Object = MibTable
swL2IGMPQueryInfoTable = _SwL2IGMPQueryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 4)
)
if mibBuilder.loadTexts:
    swL2IGMPQueryInfoTable.setStatus("current")
_SwL2IGMPQueryInfoEntry_Object = MibTableRow
swL2IGMPQueryInfoEntry = _SwL2IGMPQueryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 4, 1)
)
swL2IGMPQueryInfoEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2IGMPInfoVid"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 4, 1, 3),
    _SwL2IGMPInfoTxQueryCount_Type()
)
swL2IGMPInfoTxQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoTxQueryCount.setStatus("current")
_SwL2IGMPInfoTable_Object = MibTable
swL2IGMPInfoTable = _SwL2IGMPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 5)
)
if mibBuilder.loadTexts:
    swL2IGMPInfoTable.setStatus("current")
_SwL2IGMPInfoEntry_Object = MibTableRow
swL2IGMPInfoEntry = _SwL2IGMPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 5, 1)
)
swL2IGMPInfoEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2IGMPVid"),
    (0, "DES3852-L2MGMT-MIB", "swL2IGMPGroupIpAddr"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 5, 1, 1),
    _SwL2IGMPVid_Type()
)
swL2IGMPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVid.setStatus("current")
_SwL2IGMPGroupIpAddr_Type = IpAddress
_SwL2IGMPGroupIpAddr_Object = MibTableColumn
swL2IGMPGroupIpAddr = _SwL2IGMPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 5, 1, 2),
    _SwL2IGMPGroupIpAddr_Type()
)
swL2IGMPGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPGroupIpAddr.setStatus("current")
_SwL2IGMPMacAddr_Type = MacAddress
_SwL2IGMPMacAddr_Object = MibTableColumn
swL2IGMPMacAddr = _SwL2IGMPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 5, 1, 3),
    _SwL2IGMPMacAddr_Type()
)
swL2IGMPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMacAddr.setStatus("current")
_SwL2IGMPPortMap_Type = PortList
_SwL2IGMPPortMap_Object = MibTableColumn
swL2IGMPPortMap = _SwL2IGMPPortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 5, 1, 5),
    _SwL2IGMPIpGroupReportCount_Type()
)
swL2IGMPIpGroupReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPIpGroupReportCount.setStatus("current")
_SwL2IGMPMulticastVlanTable_Object = MibTable
swL2IGMPMulticastVlanTable = _SwL2IGMPMulticastVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 6)
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanTable.setStatus("current")
_SwL2IGMPMulticastVlanEntry_Object = MibTableRow
swL2IGMPMulticastVlanEntry = _SwL2IGMPMulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 6, 1)
)
swL2IGMPMulticastVlanEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2IGMPMulticastVlanid"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 6, 1, 1),
    _SwL2IGMPMulticastVlanid_Type()
)
swL2IGMPMulticastVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanid.setStatus("current")


class _SwL2IGMPMulticastVlanName_Type(SnmpAdminString):
    """Custom type swL2IGMPMulticastVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2IGMPMulticastVlanName_Type.__name__ = "SnmpAdminString"
_SwL2IGMPMulticastVlanName_Object = MibTableColumn
swL2IGMPMulticastVlanName = _SwL2IGMPMulticastVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 6, 1, 2),
    _SwL2IGMPMulticastVlanName_Type()
)
swL2IGMPMulticastVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanName.setStatus("current")
_SwL2IGMPMulticastVlanSourcePort_Type = PortList
_SwL2IGMPMulticastVlanSourcePort_Object = MibTableColumn
swL2IGMPMulticastVlanSourcePort = _SwL2IGMPMulticastVlanSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 6, 1, 3),
    _SwL2IGMPMulticastVlanSourcePort_Type()
)
swL2IGMPMulticastVlanSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanSourcePort.setStatus("current")
_SwL2IGMPMulticastVlanMemberPort_Type = PortList
_SwL2IGMPMulticastVlanMemberPort_Object = MibTableColumn
swL2IGMPMulticastVlanMemberPort = _SwL2IGMPMulticastVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 6, 1, 4),
    _SwL2IGMPMulticastVlanMemberPort_Type()
)
swL2IGMPMulticastVlanMemberPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanMemberPort.setStatus("current")
_SwL2IGMPMulticastVlanRowStatus_Type = RowStatus
_SwL2IGMPMulticastVlanRowStatus_Object = MibTableColumn
swL2IGMPMulticastVlanRowStatus = _SwL2IGMPMulticastVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 6, 1, 5),
    _SwL2IGMPMulticastVlanRowStatus_Type()
)
swL2IGMPMulticastVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanRowStatus.setStatus("current")
_SwL2IGMPRouterPortTable_Object = MibTable
swL2IGMPRouterPortTable = _SwL2IGMPRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 7)
)
if mibBuilder.loadTexts:
    swL2IGMPRouterPortTable.setStatus("current")
_SwL2IGMPRouterPortEntry_Object = MibTableRow
swL2IGMPRouterPortEntry = _SwL2IGMPRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 7, 1)
)
swL2IGMPRouterPortEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2IGMPRouterPortVlanid"),
)
if mibBuilder.loadTexts:
    swL2IGMPRouterPortEntry.setStatus("current")


class _SwL2IGMPRouterPortVlanid_Type(Integer32):
    """Custom type swL2IGMPRouterPortVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2IGMPRouterPortVlanid_Type.__name__ = "Integer32"
_SwL2IGMPRouterPortVlanid_Object = MibTableColumn
swL2IGMPRouterPortVlanid = _SwL2IGMPRouterPortVlanid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 7, 1, 1),
    _SwL2IGMPRouterPortVlanid_Type()
)
swL2IGMPRouterPortVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortVlanid.setStatus("current")


class _SwL2IGMPRouterPortVlanName_Type(SnmpAdminString):
    """Custom type swL2IGMPRouterPortVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2IGMPRouterPortVlanName_Type.__name__ = "SnmpAdminString"
_SwL2IGMPRouterPortVlanName_Object = MibTableColumn
swL2IGMPRouterPortVlanName = _SwL2IGMPRouterPortVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 7, 1, 2),
    _SwL2IGMPRouterPortVlanName_Type()
)
swL2IGMPRouterPortVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortVlanName.setStatus("current")
_SwL2IGMPRouterPortStaticPortList_Type = PortList
_SwL2IGMPRouterPortStaticPortList_Object = MibTableColumn
swL2IGMPRouterPortStaticPortList = _SwL2IGMPRouterPortStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 7, 1, 3),
    _SwL2IGMPRouterPortStaticPortList_Type()
)
swL2IGMPRouterPortStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortStaticPortList.setStatus("current")
_SwL2IGMPRouterPortDynamicPortList_Type = PortList
_SwL2IGMPRouterPortDynamicPortList_Object = MibTableColumn
swL2IGMPRouterPortDynamicPortList = _SwL2IGMPRouterPortDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 7, 1, 4),
    _SwL2IGMPRouterPortDynamicPortList_Type()
)
swL2IGMPRouterPortDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortDynamicPortList.setStatus("current")
_SwL2IGMPRouterPortForbiddenPortList_Type = PortList
_SwL2IGMPRouterPortForbiddenPortList_Object = MibTableColumn
swL2IGMPRouterPortForbiddenPortList = _SwL2IGMPRouterPortForbiddenPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 10, 7, 1, 5),
    _SwL2IGMPRouterPortForbiddenPortList_Type()
)
swL2IGMPRouterPortForbiddenPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortForbiddenPortList.setStatus("current")
_SwL2TrafficSegMgmt_ObjectIdentity = ObjectIdentity
swL2TrafficSegMgmt = _SwL2TrafficSegMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 13)
)
_SwL2TrafficSegTable_Object = MibTable
swL2TrafficSegTable = _SwL2TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 13, 1)
)
if mibBuilder.loadTexts:
    swL2TrafficSegTable.setStatus("current")
_SwL2TrafficSegEntry_Object = MibTableRow
swL2TrafficSegEntry = _SwL2TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 13, 1, 1)
)
swL2TrafficSegEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2TrafficSegPort"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 13, 1, 1, 1),
    _SwL2TrafficSegPort_Type()
)
swL2TrafficSegPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficSegPort.setStatus("current")
_SwL2TrafficSegForwardPorts_Type = PortList
_SwL2TrafficSegForwardPorts_Object = MibTableColumn
swL2TrafficSegForwardPorts = _SwL2TrafficSegForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 13, 1, 1, 2),
    _SwL2TrafficSegForwardPorts_Type()
)
swL2TrafficSegForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficSegForwardPorts.setStatus("current")
_SwL2BroadcastSegCtrl_ObjectIdentity = ObjectIdentity
swL2BroadcastSegCtrl = _SwL2BroadcastSegCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 13, 2)
)
_SwL2BroadcastSegFilterPorts_Type = PortList
_SwL2BroadcastSegFilterPorts_Object = MibScalar
swL2BroadcastSegFilterPorts = _SwL2BroadcastSegFilterPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 13, 2, 1),
    _SwL2BroadcastSegFilterPorts_Type()
)
swL2BroadcastSegFilterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2BroadcastSegFilterPorts.setStatus("current")
_SwL2BroadcastSegARPForwardPorts_Type = PortList
_SwL2BroadcastSegARPForwardPorts_Object = MibScalar
swL2BroadcastSegARPForwardPorts = _SwL2BroadcastSegARPForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 13, 2, 2),
    _SwL2BroadcastSegARPForwardPorts_Type()
)
swL2BroadcastSegARPForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2BroadcastSegARPForwardPorts.setStatus("current")
_SwL2PortSecurityMgmt_ObjectIdentity = ObjectIdentity
swL2PortSecurityMgmt = _SwL2PortSecurityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 14)
)
_SwL2PortSecurityControlTable_Object = MibTable
swL2PortSecurityControlTable = _SwL2PortSecurityControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 14, 1)
)
if mibBuilder.loadTexts:
    swL2PortSecurityControlTable.setStatus("current")
_SwL2PortSecurityControlEntry_Object = MibTableRow
swL2PortSecurityControlEntry = _SwL2PortSecurityControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 14, 1, 1)
)
swL2PortSecurityControlEntry.setIndexNames(
    (0, "DES3852-L2MGMT-MIB", "swL2PortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortSecurityControlEntry.setStatus("current")


class _SwL2PortSecurityPortIndex_Type(Integer32):
    """Custom type swL2PortSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2PortSecurityPortIndex_Type.__name__ = "Integer32"
_SwL2PortSecurityPortIndex_Object = MibTableColumn
swL2PortSecurityPortIndex = _SwL2PortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 14, 1, 1, 1),
    _SwL2PortSecurityPortIndex_Type()
)
swL2PortSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSecurityPortIndex.setStatus("current")


class _SwL2PortSecurityMaxLernAddr_Type(Integer32):
    """Custom type swL2PortSecurityMaxLernAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortSecurityMaxLernAddr_Type.__name__ = "Integer32"
_SwL2PortSecurityMaxLernAddr_Object = MibTableColumn
swL2PortSecurityMaxLernAddr = _SwL2PortSecurityMaxLernAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 14, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 14, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 14, 1, 1, 4),
    _SwL2PortSecurityAdmState_Type()
)
swL2PortSecurityAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityAdmState.setStatus("current")


class _SwL2PortSecurityTrapLogState_Type(Integer32):
    """Custom type swL2PortSecurityTrapLogState based on Integer32"""
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


_SwL2PortSecurityTrapLogState_Type.__name__ = "Integer32"
_SwL2PortSecurityTrapLogState_Object = MibScalar
swL2PortSecurityTrapLogState = _SwL2PortSecurityTrapLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 14, 2),
    _SwL2PortSecurityTrapLogState_Type()
)
swL2PortSecurityTrapLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityTrapLogState.setStatus("current")
_SwL2MgmtMIBTraps_ObjectIdentity = ObjectIdentity
swL2MgmtMIBTraps = _SwL2MgmtMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15)
)
_SwL2MgmtMIBTrapPrefix_ObjectIdentity = ObjectIdentity
swL2MgmtMIBTrapPrefix = _SwL2MgmtMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15, 0)
)
_Swl2NotificationBidings_ObjectIdentity = ObjectIdentity
swl2NotificationBidings = _Swl2NotificationBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15, 1, 1),
    _SwL2macNotifyInfo_Type()
)
swL2macNotifyInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2macNotifyInfo.setStatus("current")
_Swl2NotifyPortSecurity_ObjectIdentity = ObjectIdentity
swl2NotifyPortSecurity = _Swl2NotifyPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15, 2)
)
_SwL2PortSecurityViolationMac_Type = MacAddress
_SwL2PortSecurityViolationMac_Object = MibScalar
swL2PortSecurityViolationMac = _SwL2PortSecurityViolationMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15, 2, 1),
    _SwL2PortSecurityViolationMac_Type()
)
swL2PortSecurityViolationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swL2PortSecurityViolationMac.setStatus("current")

# Managed Objects groups


# Notification objects

swL2macNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15, 0, 3)
)
swL2macNotification.setObjects(
    ("DES3852-L2MGMT-MIB", "swL2macNotifyInfo")
)
if mibBuilder.loadTexts:
    swL2macNotification.setStatus(
        "current"
    )

swL2porttypechgNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15, 0, 4)
)
swL2porttypechgNotification.setObjects(
      *(("DES3852-L2MGMT-MIB", "swL2PortInfoPortIndex"),
        ("DES3852-L2MGMT-MIB", "swL2PortInfoType"))
)
if mibBuilder.loadTexts:
    swL2porttypechgNotification.setStatus(
        "current"
    )

swPowerStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15, 0, 5)
)
swPowerStatusChg.setObjects(
      *(("DES3852-L2MGMT-MIB", "swDevInfoPowerUnitIndex"),
        ("DES3852-L2MGMT-MIB", "swDevInfoPowerID"),
        ("DES3852-L2MGMT-MIB", "swDevInfoPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerStatusChg.setStatus(
        "current"
    )

swPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15, 0, 6)
)
swPowerFailure.setObjects(
      *(("DES3852-L2MGMT-MIB", "swDevInfoPowerUnitIndex"),
        ("DES3852-L2MGMT-MIB", "swDevInfoPowerID"),
        ("DES3852-L2MGMT-MIB", "swDevInfoPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerFailure.setStatus(
        "current"
    )

swPowerRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15, 0, 7)
)
swPowerRecover.setObjects(
      *(("DES3852-L2MGMT-MIB", "swDevInfoPowerUnitIndex"),
        ("DES3852-L2MGMT-MIB", "swDevInfoPowerID"),
        ("DES3852-L2MGMT-MIB", "swDevInfoPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerRecover.setStatus(
        "current"
    )

swL2PortSecurityViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4, 2, 15, 2, 2)
)
swL2PortSecurityViolationTrap.setObjects(
      *(("DES3852-L2MGMT-MIB", "swL2PortSecurityPortIndex"),
        ("DES3852-L2MGMT-MIB", "swL2PortSecurityViolationMac"))
)
if mibBuilder.loadTexts:
    swL2PortSecurityViolationTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES3852-L2MGMT-MIB",
    **{"PortList": PortList,
       "VlanIndex": VlanIndex,
       "VlanId": VlanId,
       "swL2MgmtMIB": swL2MgmtMIB,
       "swL2DevMgmt": swL2DevMgmt,
       "swL2DevInfo": swL2DevInfo,
       "swDevInfoSystemUpTime": swDevInfoSystemUpTime,
       "swDevInfoTotalNumOfPort": swDevInfoTotalNumOfPort,
       "swDevInfoNumOfPortInUse": swDevInfoNumOfPortInUse,
       "swDevInfoConsoleInUse": swDevInfoConsoleInUse,
       "swDevInfoModuleType": swDevInfoModuleType,
       "swDevInfoFrontPanelLedMode": swDevInfoFrontPanelLedMode,
       "swDevInfoPowerTable": swDevInfoPowerTable,
       "swDevInfoPowerEntry": swDevInfoPowerEntry,
       "swDevInfoPowerUnitIndex": swDevInfoPowerUnitIndex,
       "swDevInfoPowerID": swDevInfoPowerID,
       "swDevInfoPowerStatus": swDevInfoPowerStatus,
       "swL2DevCtrl": swL2DevCtrl,
       "swL2DevCtrlStpState": swL2DevCtrlStpState,
       "swL2DevCtrlIGMPSnooping": swL2DevCtrlIGMPSnooping,
       "swL2DevCtrlRmonState": swL2DevCtrlRmonState,
       "swL2DevCtrlCleanAllStatisticCounter": swL2DevCtrlCleanAllStatisticCounter,
       "swL2DevCtrlVlanIdOfFDBTbl": swL2DevCtrlVlanIdOfFDBTbl,
       "swL2MACNotifyState": swL2MACNotifyState,
       "swL2MACNotifyHistorySize": swL2MACNotifyHistorySize,
       "swL2MACNotifyInterval": swL2MACNotifyInterval,
       "swL2DevCtrlTelnet": swL2DevCtrlTelnet,
       "swL2DevCtrlTelnetState": swL2DevCtrlTelnetState,
       "swL2DevCtrlTelnetTcpPort": swL2DevCtrlTelnetTcpPort,
       "swL2DevAlarm": swL2DevAlarm,
       "swL2DevAlarmNewRoot": swL2DevAlarmNewRoot,
       "swL2DevAlarmTopologyChange": swL2DevAlarmTopologyChange,
       "swL2DevAlarmLinkChange": swL2DevAlarmLinkChange,
       "swL2VlanMgmt": swL2VlanMgmt,
       "swL2VlanAdvertisementTable": swL2VlanAdvertisementTable,
       "swL2VlanAdvertisementEntry": swL2VlanAdvertisementEntry,
       "swL2VlanIndex": swL2VlanIndex,
       "swL2VlanName": swL2VlanName,
       "swL2VlanAdvertiseState": swL2VlanAdvertiseState,
       "swL2PortMgmt": swL2PortMgmt,
       "swL2PortInfoTable": swL2PortInfoTable,
       "swL2PortInfoEntry": swL2PortInfoEntry,
       "swL2PortInfoPortIndex": swL2PortInfoPortIndex,
       "swL2PortInfoUnitIndex": swL2PortInfoUnitIndex,
       "swL2PortInfoType": swL2PortInfoType,
       "swL2PortInfoLinkStatus": swL2PortInfoLinkStatus,
       "swL2PortInfoNwayStatus": swL2PortInfoNwayStatus,
       "swL2PortInfoModuleType": swL2PortInfoModuleType,
       "swL2PortInfoErrorDisabled": swL2PortInfoErrorDisabled,
       "swL2PortCtrlTable": swL2PortCtrlTable,
       "swL2PortCtrlEntry": swL2PortCtrlEntry,
       "swL2PortCtrlPortIndex": swL2PortCtrlPortIndex,
       "swL2PortCtrlUnitIndex": swL2PortCtrlUnitIndex,
       "swL2PortCtrlAdminState": swL2PortCtrlAdminState,
       "swL2PortCtrlNwayState": swL2PortCtrlNwayState,
       "swL2PortCtrlFlowCtrlState": swL2PortCtrlFlowCtrlState,
       "swL2PortCtrlLockState": swL2PortCtrlLockState,
       "swL2PortCtrlMACNotifyState": swL2PortCtrlMACNotifyState,
       "swL2PortCtrlJumboFrame": swL2PortCtrlJumboFrame,
       "swL2PortInformationTable": swL2PortInformationTable,
       "swL2PortInformationEntry": swL2PortInformationEntry,
       "swL2PortInformationPortIndex": swL2PortInformationPortIndex,
       "swL2PortInformationMediumType": swL2PortInformationMediumType,
       "swL2PortInformationUnitID": swL2PortInformationUnitID,
       "swL2PortInformationType": swL2PortInformationType,
       "swL2PortInformationLinkStatus": swL2PortInformationLinkStatus,
       "swL2PortInformationNwayStatus": swL2PortInformationNwayStatus,
       "swL2PortInformationModuleType": swL2PortInformationModuleType,
       "swL2PortInformationErrorDisabled": swL2PortInformationErrorDisabled,
       "swL2PortControlTable": swL2PortControlTable,
       "swL2PortControlEntry": swL2PortControlEntry,
       "swL2PortControlPortIndex": swL2PortControlPortIndex,
       "swL2PortControlMediumType": swL2PortControlMediumType,
       "swL2PortControlUnitIndex": swL2PortControlUnitIndex,
       "swL2PortControlAdminState": swL2PortControlAdminState,
       "swL2PortControlNwayState": swL2PortControlNwayState,
       "swL2PortControlFlowCtrlState": swL2PortControlFlowCtrlState,
       "swL2PortControlLearningState": swL2PortControlLearningState,
       "swL2PortControlMACNotifyState": swL2PortControlMACNotifyState,
       "swL2PortControlMulticastfilter": swL2PortControlMulticastfilter,
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
       "swL2QOS8021pUserPriorityTable": swL2QOS8021pUserPriorityTable,
       "swL2QOS8021pUserPriorityEntry": swL2QOS8021pUserPriorityEntry,
       "swL2QOS8021pUserPriorityIndex": swL2QOS8021pUserPriorityIndex,
       "swL2QOS8021pUserPriorityClass": swL2QOS8021pUserPriorityClass,
       "swL2QOS8021pDefaultPriorityTable": swL2QOS8021pDefaultPriorityTable,
       "swL2QOS8021pDefaultPriorityEntry": swL2QOS8021pDefaultPriorityEntry,
       "swL2QOS8021pDefaultPriorityIndex": swL2QOS8021pDefaultPriorityIndex,
       "swL2QOS8021pDefaultPriority": swL2QOS8021pDefaultPriority,
       "swL2QOS8021pRadiusPriority": swL2QOS8021pRadiusPriority,
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
       "swL2TrunkAlgorithm": swL2TrunkAlgorithm,
       "swL2MirrorMgmt": swL2MirrorMgmt,
       "swL2MirrorLogicTargetPort": swL2MirrorLogicTargetPort,
       "swL2MirrorPortSourceIngress": swL2MirrorPortSourceIngress,
       "swL2MirrorPortSourceEgress": swL2MirrorPortSourceEgress,
       "swL2MirrorPortState": swL2MirrorPortState,
       "swL2IGMPMgmt": swL2IGMPMgmt,
       "swL2IGMPMaxSupportedVlans": swL2IGMPMaxSupportedVlans,
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
       "swL2IGMPMulticastVlanTable": swL2IGMPMulticastVlanTable,
       "swL2IGMPMulticastVlanEntry": swL2IGMPMulticastVlanEntry,
       "swL2IGMPMulticastVlanid": swL2IGMPMulticastVlanid,
       "swL2IGMPMulticastVlanName": swL2IGMPMulticastVlanName,
       "swL2IGMPMulticastVlanSourcePort": swL2IGMPMulticastVlanSourcePort,
       "swL2IGMPMulticastVlanMemberPort": swL2IGMPMulticastVlanMemberPort,
       "swL2IGMPMulticastVlanRowStatus": swL2IGMPMulticastVlanRowStatus,
       "swL2IGMPRouterPortTable": swL2IGMPRouterPortTable,
       "swL2IGMPRouterPortEntry": swL2IGMPRouterPortEntry,
       "swL2IGMPRouterPortVlanid": swL2IGMPRouterPortVlanid,
       "swL2IGMPRouterPortVlanName": swL2IGMPRouterPortVlanName,
       "swL2IGMPRouterPortStaticPortList": swL2IGMPRouterPortStaticPortList,
       "swL2IGMPRouterPortDynamicPortList": swL2IGMPRouterPortDynamicPortList,
       "swL2IGMPRouterPortForbiddenPortList": swL2IGMPRouterPortForbiddenPortList,
       "swL2TrafficSegMgmt": swL2TrafficSegMgmt,
       "swL2TrafficSegTable": swL2TrafficSegTable,
       "swL2TrafficSegEntry": swL2TrafficSegEntry,
       "swL2TrafficSegPort": swL2TrafficSegPort,
       "swL2TrafficSegForwardPorts": swL2TrafficSegForwardPorts,
       "swL2BroadcastSegCtrl": swL2BroadcastSegCtrl,
       "swL2BroadcastSegFilterPorts": swL2BroadcastSegFilterPorts,
       "swL2BroadcastSegARPForwardPorts": swL2BroadcastSegARPForwardPorts,
       "swL2PortSecurityMgmt": swL2PortSecurityMgmt,
       "swL2PortSecurityControlTable": swL2PortSecurityControlTable,
       "swL2PortSecurityControlEntry": swL2PortSecurityControlEntry,
       "swL2PortSecurityPortIndex": swL2PortSecurityPortIndex,
       "swL2PortSecurityMaxLernAddr": swL2PortSecurityMaxLernAddr,
       "swL2PortSecurityMode": swL2PortSecurityMode,
       "swL2PortSecurityAdmState": swL2PortSecurityAdmState,
       "swL2PortSecurityTrapLogState": swL2PortSecurityTrapLogState,
       "swL2MgmtMIBTraps": swL2MgmtMIBTraps,
       "swL2MgmtMIBTrapPrefix": swL2MgmtMIBTrapPrefix,
       "swL2macNotification": swL2macNotification,
       "swL2porttypechgNotification": swL2porttypechgNotification,
       "swPowerStatusChg": swPowerStatusChg,
       "swPowerFailure": swPowerFailure,
       "swPowerRecover": swPowerRecover,
       "swl2NotificationBidings": swl2NotificationBidings,
       "swL2macNotifyInfo": swL2macNotifyInfo,
       "swl2NotifyPortSecurity": swl2NotifyPortSecurity,
       "swL2PortSecurityViolationMac": swL2PortSecurityViolationMac,
       "swL2PortSecurityViolationTrap": swL2PortSecurityViolationTrap}
)

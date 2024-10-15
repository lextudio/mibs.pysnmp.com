# SNMP MIB module (DES3200-52P-L2MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DES3200-52P-L2MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:25:22 2024
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

(swPortSecPortIndex,) = mibBuilder.importSymbols(
    "PORT-SECURITY-MIB",
    "swPortSecPortIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(des3200_52p_cx,) = mibBuilder.importSymbols(
    "SWPRIMGMT-DES3200-MIB",
    "des3200-52p-cx")


# MODULE-IDENTITY

swL2MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1)
)
_SwL2DevInfo_ObjectIdentity = ObjectIdentity
swL2DevInfo = _SwL2DevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 1, 2),
    _SwDevInfoNumOfPortInUse_Type()
)
swDevInfoNumOfPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoNumOfPortInUse.setStatus("current")
_SwDevModuleInfoTable_Object = MibTable
swDevModuleInfoTable = _SwDevModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    swDevModuleInfoTable.setStatus("current")
_SwDevModuleInfoEntry_Object = MibTableRow
swDevModuleInfoEntry = _SwDevModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 1, 3, 1)
)
swDevModuleInfoEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swDevModuleInfoUnitID"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 1, 3, 1, 1),
    _SwDevModuleInfoUnitID_Type()
)
swDevModuleInfoUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevModuleInfoUnitID.setStatus("current")


class _SwDevModuleInfoModuleName_Type(DisplayString):
    """Custom type swDevModuleInfoModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwDevModuleInfoModuleName_Type.__name__ = "DisplayString"
_SwDevModuleInfoModuleName_Object = MibTableColumn
swDevModuleInfoModuleName = _SwDevModuleInfoModuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 1, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 1, 3, 1, 4),
    _SwDevModuleInfoReversion_Type()
)
swDevModuleInfoReversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevModuleInfoReversion.setStatus("current")


class _SwDevModuleInfoSerial_Type(DisplayString):
    """Custom type swDevModuleInfoSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SwDevModuleInfoSerial_Type.__name__ = "DisplayString"
_SwDevModuleInfoSerial_Object = MibTableColumn
swDevModuleInfoSerial = _SwDevModuleInfoSerial_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 1, 3, 1, 6),
    _SwDevModuleInfoDescription_Type()
)
swDevModuleInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevModuleInfoDescription.setStatus("current")


class _SwDevInfoFrontPanelLedStatus_Type(OctetString):
    """Custom type swDevInfoFrontPanelLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwDevInfoFrontPanelLedStatus_Type.__name__ = "OctetString"
_SwDevInfoFrontPanelLedStatus_Object = MibScalar
swDevInfoFrontPanelLedStatus = _SwDevInfoFrontPanelLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 1, 4),
    _SwDevInfoFrontPanelLedStatus_Type()
)
swDevInfoFrontPanelLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoFrontPanelLedStatus.setStatus("current")
_SwL2DevCtrl_ObjectIdentity = ObjectIdentity
swL2DevCtrl = _SwL2DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 2),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Type.__name__ = "Integer32"
_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Object = MibScalar
swL2DevCtrlIGMPSnoopingMcstRTOnly = _SwL2DevCtrlIGMPSnoopingMcstRTOnly_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 4),
    _SwL2DevCtrlRmonState_Type()
)
swL2DevCtrlRmonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlRmonState.setStatus("current")


class _SwL2DevCtrlSnmpTrapState_Type(Integer32):
    """Custom type swL2DevCtrlSnmpTrapState based on Integer32"""
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


_SwL2DevCtrlSnmpTrapState_Type.__name__ = "Integer32"
_SwL2DevCtrlSnmpTrapState_Object = MibScalar
swL2DevCtrlSnmpTrapState = _SwL2DevCtrlSnmpTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 5),
    _SwL2DevCtrlSnmpTrapState_Type()
)
swL2DevCtrlSnmpTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlSnmpTrapState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 6),
    _SwL2DevCtrlCleanAllStatisticCounter_Type()
)
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCleanAllStatisticCounter.setStatus("current")
_SwL2DevCtrlVlanIdOfFDBTbl_Type = VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object = MibScalar
swL2DevCtrlVlanIdOfFDBTbl = _SwL2DevCtrlVlanIdOfFDBTbl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 10),
    _SwL2MACNotifyInterval_Type()
)
swL2MACNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MACNotifyInterval.setStatus("current")


class _SwL2DevCtrlAsymVlanState_Type(Integer32):
    """Custom type swL2DevCtrlAsymVlanState based on Integer32"""
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


_SwL2DevCtrlAsymVlanState_Type.__name__ = "Integer32"
_SwL2DevCtrlAsymVlanState_Object = MibScalar
swL2DevCtrlAsymVlanState = _SwL2DevCtrlAsymVlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 13),
    _SwL2DevCtrlAsymVlanState_Type()
)
swL2DevCtrlAsymVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlAsymVlanState.setStatus("current")
_SwL2DevCtrlTelnet_ObjectIdentity = ObjectIdentity
swL2DevCtrlTelnet = _SwL2DevCtrlTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 14)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 14, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 14, 2),
    _SwL2DevCtrlTelnetTcpPort_Type()
)
swL2DevCtrlTelnetTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlTelnetTcpPort.setStatus("current")
_SwL2DevCtrlManagementVlanId_Type = VlanId
_SwL2DevCtrlManagementVlanId_Object = MibScalar
swL2DevCtrlManagementVlanId = _SwL2DevCtrlManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 16),
    _SwL2DevCtrlManagementVlanId_Type()
)
swL2DevCtrlManagementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlManagementVlanId.setStatus("current")
_SwL2DevCtrlWeb_ObjectIdentity = ObjectIdentity
swL2DevCtrlWeb = _SwL2DevCtrlWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 17)
)


class _SwL2DevCtrlWebState_Type(Integer32):
    """Custom type swL2DevCtrlWebState based on Integer32"""
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


_SwL2DevCtrlWebState_Type.__name__ = "Integer32"
_SwL2DevCtrlWebState_Object = MibScalar
swL2DevCtrlWebState = _SwL2DevCtrlWebState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 17, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 17, 2),
    _SwL2DevCtrlWebTcpPort_Type()
)
swL2DevCtrlWebTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlWebTcpPort.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 19),
    _SwL2DevCtrlLLDPForwardMessageState_Type()
)
swL2DevCtrlLLDPForwardMessageState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlLLDPForwardMessageState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 20),
    _SwL2DevCtrlIpAutoconfig_Type()
)
swL2DevCtrlIpAutoconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIpAutoconfig.setStatus("current")
_SwL2DevCtrlCFM_ObjectIdentity = ObjectIdentity
swL2DevCtrlCFM = _SwL2DevCtrlCFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 21)
)


class _SwL2DevCtrlCFMState_Type(Integer32):
    """Custom type swL2DevCtrlCFMState based on Integer32"""
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


_SwL2DevCtrlCFMState_Type.__name__ = "Integer32"
_SwL2DevCtrlCFMState_Object = MibScalar
swL2DevCtrlCFMState = _SwL2DevCtrlCFMState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 21, 1),
    _SwL2DevCtrlCFMState_Type()
)
swL2DevCtrlCFMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMState.setStatus("current")
_SwL2DevCtrlCFMPortTable_Object = MibTable
swL2DevCtrlCFMPortTable = _SwL2DevCtrlCFMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 21, 2)
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortTable.setStatus("current")
_SwL2DevCtrlCFMPortEntry_Object = MibTableRow
swL2DevCtrlCFMPortEntry = _SwL2DevCtrlCFMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 21, 2, 1)
)
swL2DevCtrlCFMPortEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2DevCtrlCFMPortIndex"),
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortEntry.setStatus("current")
_SwL2DevCtrlCFMPortIndex_Type = Integer32
_SwL2DevCtrlCFMPortIndex_Object = MibTableColumn
swL2DevCtrlCFMPortIndex = _SwL2DevCtrlCFMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 21, 2, 1, 1),
    _SwL2DevCtrlCFMPortIndex_Type()
)
swL2DevCtrlCFMPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortIndex.setStatus("current")


class _SwL2DevCtrlCFMPortState_Type(Integer32):
    """Custom type swL2DevCtrlCFMPortState based on Integer32"""
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


_SwL2DevCtrlCFMPortState_Type.__name__ = "Integer32"
_SwL2DevCtrlCFMPortState_Object = MibTableColumn
swL2DevCtrlCFMPortState = _SwL2DevCtrlCFMPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 21, 2, 1, 2),
    _SwL2DevCtrlCFMPortState_Type()
)
swL2DevCtrlCFMPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortState.setStatus("current")


class _SwL2DevCtrlVLANTrunkState_Type(Integer32):
    """Custom type swL2DevCtrlVLANTrunkState based on Integer32"""
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


_SwL2DevCtrlVLANTrunkState_Type.__name__ = "Integer32"
_SwL2DevCtrlVLANTrunkState_Object = MibScalar
swL2DevCtrlVLANTrunkState = _SwL2DevCtrlVLANTrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 2, 22),
    _SwL2DevCtrlVLANTrunkState_Type()
)
swL2DevCtrlVLANTrunkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlVLANTrunkState.setStatus("current")
_SwL2DevAlarm_ObjectIdentity = ObjectIdentity
swL2DevAlarm = _SwL2DevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 1, 3, 3),
    _SwL2DevAlarmLinkChange_Type()
)
swL2DevAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmLinkChange.setStatus("current")
_SwL2VLANMgmt_ObjectIdentity = ObjectIdentity
swL2VLANMgmt = _SwL2VLANMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2)
)
_SwL2VlanStaticTable_Object = MibTable
swL2VlanStaticTable = _SwL2VlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swL2VlanStaticTable.setStatus("current")
_SwL2VlanStaticEntry_Object = MibTableRow
swL2VlanStaticEntry = _SwL2VlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 1, 1)
)
swL2VlanStaticEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2VlanIndex"),
)
if mibBuilder.loadTexts:
    swL2VlanStaticEntry.setStatus("current")
_SwL2VlanIndex_Type = VlanId
_SwL2VlanIndex_Object = MibTableColumn
swL2VlanIndex = _SwL2VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 1, 1, 1),
    _SwL2VlanIndex_Type()
)
swL2VlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2VlanIndex.setStatus("current")


class _SwL2VLANAdvertisement_Type(Integer32):
    """Custom type swL2VLANAdvertisement based on Integer32"""
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


_SwL2VLANAdvertisement_Type.__name__ = "Integer32"
_SwL2VLANAdvertisement_Object = MibTableColumn
swL2VLANAdvertisement = _SwL2VLANAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 1, 1, 2),
    _SwL2VLANAdvertisement_Type()
)
swL2VLANAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2VLANAdvertisement.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 2),
    _SwL2PVIDAutoAssignmentState_Type()
)
swL2PVIDAutoAssignmentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PVIDAutoAssignmentState.setStatus("current")
_SwL2VlanPortInfoTable_Object = MibTable
swL2VlanPortInfoTable = _SwL2VlanPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    swL2VlanPortInfoTable.setStatus("current")
_SwL2VlanPortInfoEntry_Object = MibTableRow
swL2VlanPortInfoEntry = _SwL2VlanPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 3, 1)
)
swL2VlanPortInfoEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2VlanPortInfoPortIndex"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2VlanPortInfoVid"),
)
if mibBuilder.loadTexts:
    swL2VlanPortInfoEntry.setStatus("current")


class _SwL2VlanPortInfoPortIndex_Type(Integer32):
    """Custom type swL2VlanPortInfoPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2VlanPortInfoPortIndex_Type.__name__ = "Integer32"
_SwL2VlanPortInfoPortIndex_Object = MibTableColumn
swL2VlanPortInfoPortIndex = _SwL2VlanPortInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 3, 1, 1),
    _SwL2VlanPortInfoPortIndex_Type()
)
swL2VlanPortInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanPortInfoPortIndex.setStatus("current")
_SwL2VlanPortInfoVid_Type = VlanId
_SwL2VlanPortInfoVid_Object = MibTableColumn
swL2VlanPortInfoVid = _SwL2VlanPortInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 3, 1, 2),
    _SwL2VlanPortInfoVid_Type()
)
swL2VlanPortInfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanPortInfoVid.setStatus("current")


class _SwL2VlanPortInfoPortRole_Type(Integer32):
    """Custom type swL2VlanPortInfoPortRole based on Integer32"""
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
        *(("dynamic", 4),
          ("forbidden", 5),
          ("other", 1),
          ("tagged", 3),
          ("untagged", 2))
    )


_SwL2VlanPortInfoPortRole_Type.__name__ = "Integer32"
_SwL2VlanPortInfoPortRole_Object = MibTableColumn
swL2VlanPortInfoPortRole = _SwL2VlanPortInfoPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 3, 1, 3),
    _SwL2VlanPortInfoPortRole_Type()
)
swL2VlanPortInfoPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanPortInfoPortRole.setStatus("current")
_SwL2SubnetVLANTable_Object = MibTable
swL2SubnetVLANTable = _SwL2SubnetVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    swL2SubnetVLANTable.setStatus("current")
_SwL2SubnetVLANEntry_Object = MibTableRow
swL2SubnetVLANEntry = _SwL2SubnetVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 4, 1)
)
swL2SubnetVLANEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2SubnetVLANIPAddress"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2SubnetVLANIPMask"),
)
if mibBuilder.loadTexts:
    swL2SubnetVLANEntry.setStatus("current")
_SwL2SubnetVLANIPAddress_Type = IpAddress
_SwL2SubnetVLANIPAddress_Object = MibTableColumn
swL2SubnetVLANIPAddress = _SwL2SubnetVLANIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 4, 1, 1),
    _SwL2SubnetVLANIPAddress_Type()
)
swL2SubnetVLANIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2SubnetVLANIPAddress.setStatus("current")
_SwL2SubnetVLANIPMask_Type = IpAddress
_SwL2SubnetVLANIPMask_Object = MibTableColumn
swL2SubnetVLANIPMask = _SwL2SubnetVLANIPMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 4, 1, 2),
    _SwL2SubnetVLANIPMask_Type()
)
swL2SubnetVLANIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2SubnetVLANIPMask.setStatus("current")
_SwL2SubnetVLANID_Type = VlanId
_SwL2SubnetVLANID_Object = MibTableColumn
swL2SubnetVLANID = _SwL2SubnetVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 4, 1, 3),
    _SwL2SubnetVLANID_Type()
)
swL2SubnetVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2SubnetVLANID.setStatus("current")


class _SwL2SubnetVLANPriority_Type(Integer32):
    """Custom type swL2SubnetVLANPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2SubnetVLANPriority_Type.__name__ = "Integer32"
_SwL2SubnetVLANPriority_Object = MibTableColumn
swL2SubnetVLANPriority = _SwL2SubnetVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 4, 1, 4),
    _SwL2SubnetVLANPriority_Type()
)
swL2SubnetVLANPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2SubnetVLANPriority.setStatus("current")
_SwL2SubnetVLANRowStatus_Type = RowStatus
_SwL2SubnetVLANRowStatus_Object = MibTableColumn
swL2SubnetVLANRowStatus = _SwL2SubnetVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 4, 1, 5),
    _SwL2SubnetVLANRowStatus_Type()
)
swL2SubnetVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2SubnetVLANRowStatus.setStatus("current")
_SwL2VlanPrecedenceTable_Object = MibTable
swL2VlanPrecedenceTable = _SwL2VlanPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    swL2VlanPrecedenceTable.setStatus("current")
_SwL2VlanPrecedenceEntry_Object = MibTableRow
swL2VlanPrecedenceEntry = _SwL2VlanPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 5, 1)
)
swL2VlanPrecedenceEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2VlanPrecedencePortIndex"),
)
if mibBuilder.loadTexts:
    swL2VlanPrecedenceEntry.setStatus("current")


class _SwL2VlanPrecedencePortIndex_Type(Integer32):
    """Custom type swL2VlanPrecedencePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2VlanPrecedencePortIndex_Type.__name__ = "Integer32"
_SwL2VlanPrecedencePortIndex_Object = MibTableColumn
swL2VlanPrecedencePortIndex = _SwL2VlanPrecedencePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 5, 1, 1),
    _SwL2VlanPrecedencePortIndex_Type()
)
swL2VlanPrecedencePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanPrecedencePortIndex.setStatus("current")


class _SwL2VlanPrecedenceClassification_Type(Integer32):
    """Custom type swL2VlanPrecedenceClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac-based", 1),
          ("subnet-based", 2))
    )


_SwL2VlanPrecedenceClassification_Type.__name__ = "Integer32"
_SwL2VlanPrecedenceClassification_Object = MibTableColumn
swL2VlanPrecedenceClassification = _SwL2VlanPrecedenceClassification_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 5, 1, 2),
    _SwL2VlanPrecedenceClassification_Type()
)
swL2VlanPrecedenceClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2VlanPrecedenceClassification.setStatus("current")


class _SwL2NniGvrpBpduAddress_Type(Integer32):
    """Custom type swL2NniGvrpBpduAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1ad", 2),
          ("dot1d", 1))
    )


_SwL2NniGvrpBpduAddress_Type.__name__ = "Integer32"
_SwL2NniGvrpBpduAddress_Object = MibScalar
swL2NniGvrpBpduAddress = _SwL2NniGvrpBpduAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 2, 6),
    _SwL2NniGvrpBpduAddress_Type()
)
swL2NniGvrpBpduAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2NniGvrpBpduAddress.setStatus("current")
_SwL2PortMgmt_ObjectIdentity = ObjectIdentity
swL2PortMgmt = _SwL2PortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3)
)
_SwL2PortInfoTable_Object = MibTable
swL2PortInfoTable = _SwL2PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    swL2PortInfoTable.setStatus("current")
_SwL2PortInfoEntry_Object = MibTableRow
swL2PortInfoEntry = _SwL2PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 1, 1)
)
swL2PortInfoEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortInfoPortIndex"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortInfoMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 1, 1, 3),
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


_SwL2PortInfoType_Type.__name__ = "Integer32"
_SwL2PortInfoType_Object = MibTableColumn
swL2PortInfoType = _SwL2PortInfoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 1, 1, 5),
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


_SwL2PortInfoNwayStatus_Type.__name__ = "Integer32"
_SwL2PortInfoNwayStatus_Object = MibTableColumn
swL2PortInfoNwayStatus = _SwL2PortInfoNwayStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 1, 1, 6),
    _SwL2PortInfoNwayStatus_Type()
)
swL2PortInfoNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoNwayStatus.setStatus("current")


class _SwL2PortInfoModuleType_Type(Integer32):
    """Custom type swL2PortInfoModuleType based on Integer32"""
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


_SwL2PortInfoModuleType_Type.__name__ = "Integer32"
_SwL2PortInfoModuleType_Object = MibTableColumn
swL2PortInfoModuleType = _SwL2PortInfoModuleType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 1, 1, 7),
    _SwL2PortInfoModuleType_Type()
)
swL2PortInfoModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoModuleType.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 1, 1, 8),
    _SwL2PortInfoErrorDisabled_Type()
)
swL2PortInfoErrorDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoErrorDisabled.setStatus("current")
_SwL2PortCtrlTable_Object = MibTable
swL2PortCtrlTable = _SwL2PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    swL2PortCtrlTable.setStatus("current")
_SwL2PortCtrlEntry_Object = MibTableRow
swL2PortCtrlEntry = _SwL2PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1)
)
swL2PortCtrlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortCtrlPortIndex"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortCtrlMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1, 4),
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


_SwL2PortCtrlNwayState_Type.__name__ = "Integer32"
_SwL2PortCtrlNwayState_Object = MibTableColumn
swL2PortCtrlNwayState = _SwL2PortCtrlNwayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1, 6),
    _SwL2PortCtrlFlowCtrlState_Type()
)
swL2PortCtrlFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlFlowCtrlState.setStatus("current")


class _SwL2PortCtrlLearningState_Type(Integer32):
    """Custom type swL2PortCtrlLearningState based on Integer32"""
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


_SwL2PortCtrlLearningState_Type.__name__ = "Integer32"
_SwL2PortCtrlLearningState_Object = MibTableColumn
swL2PortCtrlLearningState = _SwL2PortCtrlLearningState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1, 7),
    _SwL2PortCtrlLearningState_Type()
)
swL2PortCtrlLearningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlLearningState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1, 8),
    _SwL2PortCtrlMACNotifyState_Type()
)
swL2PortCtrlMACNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlMACNotifyState.setStatus("current")


class _SwL2PortCtrlMDIXState_Type(Integer32):
    """Custom type swL2PortCtrlMDIXState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("cross", 3),
          ("normal", 2))
    )


_SwL2PortCtrlMDIXState_Type.__name__ = "Integer32"
_SwL2PortCtrlMDIXState_Object = MibTableColumn
swL2PortCtrlMDIXState = _SwL2PortCtrlMDIXState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1, 10),
    _SwL2PortCtrlMDIXState_Type()
)
swL2PortCtrlMDIXState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlMDIXState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1, 11),
    _SwL2PortCtrlAutoNegRestart_Type()
)
swL2PortCtrlAutoNegRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAutoNegRestart.setStatus("current")
_SwL2PortCtrlAutoNegCapAdvertisedBits_Type = IANAifMauAutoNegCapBits
_SwL2PortCtrlAutoNegCapAdvertisedBits_Object = MibTableColumn
swL2PortCtrlAutoNegCapAdvertisedBits = _SwL2PortCtrlAutoNegCapAdvertisedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 2, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 3),
    _SwL2PortCtrlJumboFrame_Type()
)
swL2PortCtrlJumboFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlJumboFrame.setStatus("current")
_SwL2PortCtrlJumboFrameMaxSize_Type = Integer32
_SwL2PortCtrlJumboFrameMaxSize_Object = MibScalar
swL2PortCtrlJumboFrameMaxSize = _SwL2PortCtrlJumboFrameMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 4),
    _SwL2PortCtrlJumboFrameMaxSize_Type()
)
swL2PortCtrlJumboFrameMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlJumboFrameMaxSize.setStatus("current")
_SwL2PortCableDiagnosisTable_Object = MibTable
swL2PortCableDiagnosisTable = _SwL2PortCableDiagnosisTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisTable.setStatus("current")
_SwL2PortCableDiagnosisEntry_Object = MibTableRow
swL2PortCableDiagnosisEntry = _SwL2PortCableDiagnosisEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 5, 1)
)
swL2PortCableDiagnosisEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortCableDiagnosisPortIndex"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortCableDiagnosisPairIndex"),
)
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisEntry.setStatus("current")


class _SwL2PortCableDiagnosisPortIndex_Type(Integer32):
    """Custom type swL2PortCableDiagnosisPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortCableDiagnosisPortIndex_Type.__name__ = "Integer32"
_SwL2PortCableDiagnosisPortIndex_Object = MibTableColumn
swL2PortCableDiagnosisPortIndex = _SwL2PortCableDiagnosisPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 5, 1, 1),
    _SwL2PortCableDiagnosisPortIndex_Type()
)
swL2PortCableDiagnosisPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisPortIndex.setStatus("current")


class _SwL2PortCableDiagnosisPairIndex_Type(Integer32):
    """Custom type swL2PortCableDiagnosisPairIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SwL2PortCableDiagnosisPairIndex_Type.__name__ = "Integer32"
_SwL2PortCableDiagnosisPairIndex_Object = MibTableColumn
swL2PortCableDiagnosisPairIndex = _SwL2PortCableDiagnosisPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 5, 1, 2),
    _SwL2PortCableDiagnosisPairIndex_Type()
)
swL2PortCableDiagnosisPairIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisPairIndex.setStatus("current")


class _SwL2PortCableDiagnosisCableStatus_Type(Integer32):
    """Custom type swL2PortCableDiagnosisCableStatus based on Integer32"""
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
        *(("not-support", 4),
          ("ok", 0),
          ("open", 1),
          ("open-short", 3),
          ("short", 2),
          ("unknown", 5))
    )


_SwL2PortCableDiagnosisCableStatus_Type.__name__ = "Integer32"
_SwL2PortCableDiagnosisCableStatus_Object = MibTableColumn
swL2PortCableDiagnosisCableStatus = _SwL2PortCableDiagnosisCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 5, 1, 3),
    _SwL2PortCableDiagnosisCableStatus_Type()
)
swL2PortCableDiagnosisCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisCableStatus.setStatus("current")


class _SwL2PortCableDiagnosisPairStatus_Type(Integer32):
    """Custom type swL2PortCableDiagnosisPairStatus based on Integer32"""
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
        *(("fail", 3),
          ("not-supported", 4),
          ("ok", 0),
          ("open", 1),
          ("short", 2),
          ("unknown", 5))
    )


_SwL2PortCableDiagnosisPairStatus_Type.__name__ = "Integer32"
_SwL2PortCableDiagnosisPairStatus_Object = MibTableColumn
swL2PortCableDiagnosisPairStatus = _SwL2PortCableDiagnosisPairStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 5, 1, 4),
    _SwL2PortCableDiagnosisPairStatus_Type()
)
swL2PortCableDiagnosisPairStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisPairStatus.setStatus("current")
_SwL2PortCableDiagnosisPairLength_Type = Integer32
_SwL2PortCableDiagnosisPairLength_Object = MibTableColumn
swL2PortCableDiagnosisPairLength = _SwL2PortCableDiagnosisPairLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 5, 1, 5),
    _SwL2PortCableDiagnosisPairLength_Type()
)
swL2PortCableDiagnosisPairLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisPairLength.setStatus("current")
_SwL2PortCableDiagnosisPairLengthInaccuracy_Type = Integer32
_SwL2PortCableDiagnosisPairLengthInaccuracy_Object = MibTableColumn
swL2PortCableDiagnosisPairLengthInaccuracy = _SwL2PortCableDiagnosisPairLengthInaccuracy_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 5, 1, 6),
    _SwL2PortCableDiagnosisPairLengthInaccuracy_Type()
)
swL2PortCableDiagnosisPairLengthInaccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisPairLengthInaccuracy.setStatus("current")
_SwL2PortCounterCtrlTable_Object = MibTable
swL2PortCounterCtrlTable = _SwL2PortCounterCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    swL2PortCounterCtrlTable.setStatus("current")
_SwL2PortCounterCtrlEntry_Object = MibTableRow
swL2PortCounterCtrlEntry = _SwL2PortCounterCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 6, 1)
)
swL2PortCounterCtrlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortCounterCtrlPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 6, 1, 2),
    _SwL2PortCounterClearCtrl_Type()
)
swL2PortCounterClearCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCounterClearCtrl.setStatus("current")
_SwL2PortErrTable_Object = MibTable
swL2PortErrTable = _SwL2PortErrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 7)
)
if mibBuilder.loadTexts:
    swL2PortErrTable.setStatus("current")
_SwL2PortErrEntry_Object = MibTableRow
swL2PortErrEntry = _SwL2PortErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 7, 1)
)
swL2PortErrEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortErrPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortErrEntry.setStatus("current")


class _SwL2PortErrPortIndex_Type(Integer32):
    """Custom type swL2PortErrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortErrPortIndex_Type.__name__ = "Integer32"
_SwL2PortErrPortIndex_Object = MibTableColumn
swL2PortErrPortIndex = _SwL2PortErrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 7, 1, 1),
    _SwL2PortErrPortIndex_Type()
)
swL2PortErrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortIndex.setStatus("current")


class _SwL2PortErrPortState_Type(Integer32):
    """Custom type swL2PortErrPortState based on Integer32"""
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


_SwL2PortErrPortState_Type.__name__ = "Integer32"
_SwL2PortErrPortState_Object = MibTableColumn
swL2PortErrPortState = _SwL2PortErrPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 7, 1, 2),
    _SwL2PortErrPortState_Type()
)
swL2PortErrPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortState.setStatus("current")


class _SwL2PortErrPortConnStatus_Type(Integer32):
    """Custom type swL2PortErrPortConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("err-disabled", 2),
          ("other", 1))
    )


_SwL2PortErrPortConnStatus_Type.__name__ = "Integer32"
_SwL2PortErrPortConnStatus_Object = MibTableColumn
swL2PortErrPortConnStatus = _SwL2PortErrPortConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 7, 1, 3),
    _SwL2PortErrPortConnStatus_Type()
)
swL2PortErrPortConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortConnStatus.setStatus("current")


class _SwL2PortErrPortReason_Type(Integer32):
    """Custom type swL2PortErrPortReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("storm-control", 2),
          ("stp-lbd", 1))
    )


_SwL2PortErrPortReason_Type.__name__ = "Integer32"
_SwL2PortErrPortReason_Object = MibTableColumn
swL2PortErrPortReason = _SwL2PortErrPortReason_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 7, 1, 4),
    _SwL2PortErrPortReason_Type()
)
swL2PortErrPortReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortReason.setStatus("current")
_SwL2PortAutoNegInfoTable_Object = MibTable
swL2PortAutoNegInfoTable = _SwL2PortAutoNegInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 8)
)
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoTable.setStatus("current")
_SwL2PortAutoNegInfoEntry_Object = MibTableRow
swL2PortAutoNegInfoEntry = _SwL2PortAutoNegInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 8, 1)
)
swL2PortAutoNegInfoEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortAutoNegInfoPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 8, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 8, 1, 2),
    _SwL2PortAutoNegInfoAdminStatus_Type()
)
swL2PortAutoNegInfoAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoAdminStatus.setStatus("current")
_SwL2PortAutoNegInfoCapabilityBits_Type = IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapabilityBits_Object = MibTableColumn
swL2PortAutoNegInfoCapabilityBits = _SwL2PortAutoNegInfoCapabilityBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 8, 1, 3),
    _SwL2PortAutoNegInfoCapabilityBits_Type()
)
swL2PortAutoNegInfoCapabilityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoCapabilityBits.setStatus("current")
_SwL2PortAutoNegInfoCapAdvertisedBits_Type = IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapAdvertisedBits_Object = MibTableColumn
swL2PortAutoNegInfoCapAdvertisedBits = _SwL2PortAutoNegInfoCapAdvertisedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 8, 1, 4),
    _SwL2PortAutoNegInfoCapAdvertisedBits_Type()
)
swL2PortAutoNegInfoCapAdvertisedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoCapAdvertisedBits.setStatus("current")
_SwL2PortAutoNegInfoCapReceivedBits_Type = IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapReceivedBits_Object = MibTableColumn
swL2PortAutoNegInfoCapReceivedBits = _SwL2PortAutoNegInfoCapReceivedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 8, 1, 5),
    _SwL2PortAutoNegInfoCapReceivedBits_Type()
)
swL2PortAutoNegInfoCapReceivedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoCapReceivedBits.setStatus("current")
_SwL2PortDropCounterTable_Object = MibTable
swL2PortDropCounterTable = _SwL2PortDropCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 9)
)
if mibBuilder.loadTexts:
    swL2PortDropCounterTable.setStatus("current")
_SwL2PortDropCounterEntry_Object = MibTableRow
swL2PortDropCounterEntry = _SwL2PortDropCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 9, 1)
)
swL2PortDropCounterEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortDropCounterPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 9, 1, 1),
    _SwL2PortDropCounterPortIndex_Type()
)
swL2PortDropCounterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortDropCounterPortIndex.setStatus("current")
_SwL2PortBufferFullDrops_Type = Counter32
_SwL2PortBufferFullDrops_Object = MibTableColumn
swL2PortBufferFullDrops = _SwL2PortBufferFullDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 9, 1, 2),
    _SwL2PortBufferFullDrops_Type()
)
swL2PortBufferFullDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortBufferFullDrops.setStatus("current")
_SwL2PortACLDrops_Type = Counter32
_SwL2PortACLDrops_Object = MibTableColumn
swL2PortACLDrops = _SwL2PortACLDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 9, 1, 3),
    _SwL2PortACLDrops_Type()
)
swL2PortACLDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortACLDrops.setStatus("current")
_SwL2PortMulticastDrops_Type = Counter32
_SwL2PortMulticastDrops_Object = MibTableColumn
swL2PortMulticastDrops = _SwL2PortMulticastDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 9, 1, 4),
    _SwL2PortMulticastDrops_Type()
)
swL2PortMulticastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortMulticastDrops.setStatus("current")
_SwL2PortVLANIngressDrops_Type = Counter32
_SwL2PortVLANIngressDrops_Object = MibTableColumn
swL2PortVLANIngressDrops = _SwL2PortVLANIngressDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 9, 1, 5),
    _SwL2PortVLANIngressDrops_Type()
)
swL2PortVLANIngressDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortVLANIngressDrops.setStatus("current")
_SwL2PortJumboFrameCtrlTable_Object = MibTable
swL2PortJumboFrameCtrlTable = _SwL2PortJumboFrameCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 10)
)
if mibBuilder.loadTexts:
    swL2PortJumboFrameCtrlTable.setStatus("current")
_SwL2PortJumboFrameCtrlEntry_Object = MibTableRow
swL2PortJumboFrameCtrlEntry = _SwL2PortJumboFrameCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 10, 1)
)
swL2PortJumboFrameCtrlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortJumboFrameCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortJumboFrameCtrlEntry.setStatus("current")
_SwL2PortJumboFrameCtrlPortIndex_Type = Integer32
_SwL2PortJumboFrameCtrlPortIndex_Object = MibTableColumn
swL2PortJumboFrameCtrlPortIndex = _SwL2PortJumboFrameCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 10, 1, 1),
    _SwL2PortJumboFrameCtrlPortIndex_Type()
)
swL2PortJumboFrameCtrlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2PortJumboFrameCtrlPortIndex.setStatus("current")


class _SwL2PortJumboFrameCtrlState_Type(Integer32):
    """Custom type swL2PortJumboFrameCtrlState based on Integer32"""
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


_SwL2PortJumboFrameCtrlState_Type.__name__ = "Integer32"
_SwL2PortJumboFrameCtrlState_Object = MibTableColumn
swL2PortJumboFrameCtrlState = _SwL2PortJumboFrameCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 3, 10, 1, 2),
    _SwL2PortJumboFrameCtrlState_Type()
)
swL2PortJumboFrameCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortJumboFrameCtrlState.setStatus("current")
_SwL2DiffServMgmt_ObjectIdentity = ObjectIdentity
swL2DiffServMgmt = _SwL2DiffServMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4)
)
_SwL2DiffServTypeCtrlTable_Object = MibTable
swL2DiffServTypeCtrlTable = _SwL2DiffServTypeCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    swL2DiffServTypeCtrlTable.setStatus("current")
_SwL2DiffServTypeCtrlEntry_Object = MibTableRow
swL2DiffServTypeCtrlEntry = _SwL2DiffServTypeCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 1, 1)
)
swL2DiffServTypeCtrlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2DiffServTypeCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swL2DiffServTypeCtrlEntry.setStatus("current")


class _SwL2DiffServTypeCtrlPortIndex_Type(Integer32):
    """Custom type swL2DiffServTypeCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2DiffServTypeCtrlPortIndex_Type.__name__ = "Integer32"
_SwL2DiffServTypeCtrlPortIndex_Object = MibTableColumn
swL2DiffServTypeCtrlPortIndex = _SwL2DiffServTypeCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 1, 1, 1),
    _SwL2DiffServTypeCtrlPortIndex_Type()
)
swL2DiffServTypeCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DiffServTypeCtrlPortIndex.setStatus("current")


class _SwL2DiffServTypeCtrlDiffServType_Type(Integer32):
    """Custom type swL2DiffServTypeCtrlDiffServType based on Integer32"""
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
          ("dscp", 2),
          ("tos", 3))
    )


_SwL2DiffServTypeCtrlDiffServType_Type.__name__ = "Integer32"
_SwL2DiffServTypeCtrlDiffServType_Object = MibTableColumn
swL2DiffServTypeCtrlDiffServType = _SwL2DiffServTypeCtrlDiffServType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 1, 1, 2),
    _SwL2DiffServTypeCtrlDiffServType_Type()
)
swL2DiffServTypeCtrlDiffServType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DiffServTypeCtrlDiffServType.setStatus("current")
_SwL2DiffServDSCPCtrlTable_Object = MibTable
swL2DiffServDSCPCtrlTable = _SwL2DiffServDSCPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    swL2DiffServDSCPCtrlTable.setStatus("current")
_SwL2DiffServDSCPCtrlEntry_Object = MibTableRow
swL2DiffServDSCPCtrlEntry = _SwL2DiffServDSCPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 2, 1)
)
swL2DiffServDSCPCtrlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2DiffServDSCPCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swL2DiffServDSCPCtrlEntry.setStatus("current")


class _SwL2DiffServDSCPCtrlPortIndex_Type(Integer32):
    """Custom type swL2DiffServDSCPCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2DiffServDSCPCtrlPortIndex_Type.__name__ = "Integer32"
_SwL2DiffServDSCPCtrlPortIndex_Object = MibTableColumn
swL2DiffServDSCPCtrlPortIndex = _SwL2DiffServDSCPCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 2, 1, 1),
    _SwL2DiffServDSCPCtrlPortIndex_Type()
)
swL2DiffServDSCPCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DiffServDSCPCtrlPortIndex.setStatus("current")


class _SwL2DiffServDSCPCtrlMode_Type(Integer32):
    """Custom type swL2DiffServDSCPCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp-Change-If-Zero", 2),
          ("dscp-Force-Overwrite", 1))
    )


_SwL2DiffServDSCPCtrlMode_Type.__name__ = "Integer32"
_SwL2DiffServDSCPCtrlMode_Object = MibTableColumn
swL2DiffServDSCPCtrlMode = _SwL2DiffServDSCPCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 2, 1, 2),
    _SwL2DiffServDSCPCtrlMode_Type()
)
swL2DiffServDSCPCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DiffServDSCPCtrlMode.setStatus("current")


class _SwL2DiffServDSCPCtrlValue_Type(Integer32):
    """Custom type swL2DiffServDSCPCtrlValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwL2DiffServDSCPCtrlValue_Type.__name__ = "Integer32"
_SwL2DiffServDSCPCtrlValue_Object = MibTableColumn
swL2DiffServDSCPCtrlValue = _SwL2DiffServDSCPCtrlValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 2, 1, 3),
    _SwL2DiffServDSCPCtrlValue_Type()
)
swL2DiffServDSCPCtrlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DiffServDSCPCtrlValue.setStatus("current")
_SwL2DiffServTOSCtrlTable_Object = MibTable
swL2DiffServTOSCtrlTable = _SwL2DiffServTOSCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    swL2DiffServTOSCtrlTable.setStatus("current")
_SwL2DiffServTOSCtrlEntry_Object = MibTableRow
swL2DiffServTOSCtrlEntry = _SwL2DiffServTOSCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 3, 1)
)
swL2DiffServTOSCtrlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2DiffServTOSCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swL2DiffServTOSCtrlEntry.setStatus("current")


class _SwL2DiffServTOSCtrlPortIndex_Type(Integer32):
    """Custom type swL2DiffServTOSCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2DiffServTOSCtrlPortIndex_Type.__name__ = "Integer32"
_SwL2DiffServTOSCtrlPortIndex_Object = MibTableColumn
swL2DiffServTOSCtrlPortIndex = _SwL2DiffServTOSCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 3, 1, 1),
    _SwL2DiffServTOSCtrlPortIndex_Type()
)
swL2DiffServTOSCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DiffServTOSCtrlPortIndex.setStatus("current")


class _SwL2DiffServTOSCtrlMode_Type(Integer32):
    """Custom type swL2DiffServTOSCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tos-802dot1p-Overwrite-TOS", 3),
          ("tos-Force-Overwrite", 1),
          ("tos-TOS-Overwrite-802dot1p", 2))
    )


_SwL2DiffServTOSCtrlMode_Type.__name__ = "Integer32"
_SwL2DiffServTOSCtrlMode_Object = MibTableColumn
swL2DiffServTOSCtrlMode = _SwL2DiffServTOSCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 3, 1, 2),
    _SwL2DiffServTOSCtrlMode_Type()
)
swL2DiffServTOSCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DiffServTOSCtrlMode.setStatus("current")


class _SwL2DiffServTOSCtrlValue_Type(Integer32):
    """Custom type swL2DiffServTOSCtrlValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2DiffServTOSCtrlValue_Type.__name__ = "Integer32"
_SwL2DiffServTOSCtrlValue_Object = MibTableColumn
swL2DiffServTOSCtrlValue = _SwL2DiffServTOSCtrlValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 4, 3, 1, 3),
    _SwL2DiffServTOSCtrlValue_Type()
)
swL2DiffServTOSCtrlValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DiffServTOSCtrlValue.setStatus("current")
_SwL2LimitedMulticastMgmt_ObjectIdentity = ObjectIdentity
swL2LimitedMulticastMgmt = _SwL2LimitedMulticastMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5)
)
_SwL2MulticastFilterProfileTable_Object = MibTable
swL2MulticastFilterProfileTable = _SwL2MulticastFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    swL2MulticastFilterProfileTable.setStatus("current")
_SwL2MulticastFilterProfileEntry_Object = MibTableRow
swL2MulticastFilterProfileEntry = _SwL2MulticastFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 1, 1)
)
swL2MulticastFilterProfileEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2MulticastFilterProfileIndex"),
)
if mibBuilder.loadTexts:
    swL2MulticastFilterProfileEntry.setStatus("current")


class _SwL2MulticastFilterProfileIndex_Type(Integer32):
    """Custom type swL2MulticastFilterProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SwL2MulticastFilterProfileIndex_Type.__name__ = "Integer32"
_SwL2MulticastFilterProfileIndex_Object = MibTableColumn
swL2MulticastFilterProfileIndex = _SwL2MulticastFilterProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 1, 1, 1),
    _SwL2MulticastFilterProfileIndex_Type()
)
swL2MulticastFilterProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2MulticastFilterProfileIndex.setStatus("current")


class _SwL2MulticastFilterProfileName_Type(DisplayString):
    """Custom type swL2MulticastFilterProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwL2MulticastFilterProfileName_Type.__name__ = "DisplayString"
_SwL2MulticastFilterProfileName_Object = MibTableColumn
swL2MulticastFilterProfileName = _SwL2MulticastFilterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 1, 1, 2),
    _SwL2MulticastFilterProfileName_Type()
)
swL2MulticastFilterProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MulticastFilterProfileName.setStatus("current")
_SwL2MulticastFilterStatus_Type = RowStatus
_SwL2MulticastFilterStatus_Object = MibTableColumn
swL2MulticastFilterStatus = _SwL2MulticastFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 1, 1, 3),
    _SwL2MulticastFilterStatus_Type()
)
swL2MulticastFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MulticastFilterStatus.setStatus("current")
_SwL2MulticastFilterProfileAddressTable_Object = MibTable
swL2MulticastFilterProfileAddressTable = _SwL2MulticastFilterProfileAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    swL2MulticastFilterProfileAddressTable.setStatus("current")
_SwL2MulticastFilterProfileAddressEntry_Object = MibTableRow
swL2MulticastFilterProfileAddressEntry = _SwL2MulticastFilterProfileAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 2, 1)
)
swL2MulticastFilterProfileAddressEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2MulticastFilterProfileIdIndex"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2MulticastFilterFromIp"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2MulticastFilterToIp"),
)
if mibBuilder.loadTexts:
    swL2MulticastFilterProfileAddressEntry.setStatus("current")


class _SwL2MulticastFilterProfileIdIndex_Type(Integer32):
    """Custom type swL2MulticastFilterProfileIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SwL2MulticastFilterProfileIdIndex_Type.__name__ = "Integer32"
_SwL2MulticastFilterProfileIdIndex_Object = MibTableColumn
swL2MulticastFilterProfileIdIndex = _SwL2MulticastFilterProfileIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 2, 1, 1),
    _SwL2MulticastFilterProfileIdIndex_Type()
)
swL2MulticastFilterProfileIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2MulticastFilterProfileIdIndex.setStatus("current")
_SwL2MulticastFilterFromIp_Type = IpAddress
_SwL2MulticastFilterFromIp_Object = MibTableColumn
swL2MulticastFilterFromIp = _SwL2MulticastFilterFromIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 2, 1, 2),
    _SwL2MulticastFilterFromIp_Type()
)
swL2MulticastFilterFromIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2MulticastFilterFromIp.setStatus("current")
_SwL2MulticastFilterToIp_Type = IpAddress
_SwL2MulticastFilterToIp_Object = MibTableColumn
swL2MulticastFilterToIp = _SwL2MulticastFilterToIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 2, 1, 3),
    _SwL2MulticastFilterToIp_Type()
)
swL2MulticastFilterToIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2MulticastFilterToIp.setStatus("current")
_SwL2MulticastFilterAddressState_Type = RowStatus
_SwL2MulticastFilterAddressState_Object = MibTableColumn
swL2MulticastFilterAddressState = _SwL2MulticastFilterAddressState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 2, 1, 4),
    _SwL2MulticastFilterAddressState_Type()
)
swL2MulticastFilterAddressState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MulticastFilterAddressState.setStatus("current")
_SwL2LimitedMulticastFilterPortTable_Object = MibTable
swL2LimitedMulticastFilterPortTable = _SwL2LimitedMulticastFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterPortTable.setStatus("current")
_SwL2LimitedMulticastFilterPortEntry_Object = MibTableRow
swL2LimitedMulticastFilterPortEntry = _SwL2LimitedMulticastFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 3, 1)
)
swL2LimitedMulticastFilterPortEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2LimitedMulticastFilterPortIndex"),
)
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterPortEntry.setStatus("current")
_SwL2LimitedMulticastFilterPortIndex_Type = Integer32
_SwL2LimitedMulticastFilterPortIndex_Object = MibTableColumn
swL2LimitedMulticastFilterPortIndex = _SwL2LimitedMulticastFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 3, 1, 1),
    _SwL2LimitedMulticastFilterPortIndex_Type()
)
swL2LimitedMulticastFilterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterPortIndex.setStatus("current")


class _SwL2LimitedMulticastFilterPortAccess_Type(Integer32):
    """Custom type swL2LimitedMulticastFilterPortAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_SwL2LimitedMulticastFilterPortAccess_Type.__name__ = "Integer32"
_SwL2LimitedMulticastFilterPortAccess_Object = MibTableColumn
swL2LimitedMulticastFilterPortAccess = _SwL2LimitedMulticastFilterPortAccess_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 3, 1, 2),
    _SwL2LimitedMulticastFilterPortAccess_Type()
)
swL2LimitedMulticastFilterPortAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterPortAccess.setStatus("current")
_SwL2LimitedMulticastFilterPortProfileID_Type = DisplayString
_SwL2LimitedMulticastFilterPortProfileID_Object = MibTableColumn
swL2LimitedMulticastFilterPortProfileID = _SwL2LimitedMulticastFilterPortProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 3, 1, 3),
    _SwL2LimitedMulticastFilterPortProfileID_Type()
)
swL2LimitedMulticastFilterPortProfileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterPortProfileID.setStatus("current")


class _SwL2LimitedMulticastFilterPortProfileStatus_Type(Integer32):
    """Custom type swL2LimitedMulticastFilterPortProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("other", 1))
    )


_SwL2LimitedMulticastFilterPortProfileStatus_Type.__name__ = "Integer32"
_SwL2LimitedMulticastFilterPortProfileStatus_Object = MibTableColumn
swL2LimitedMulticastFilterPortProfileStatus = _SwL2LimitedMulticastFilterPortProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 3, 1, 4),
    _SwL2LimitedMulticastFilterPortProfileStatus_Type()
)
swL2LimitedMulticastFilterPortProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterPortProfileStatus.setStatus("current")
_SwL2MulticastFilterPortMaxGroupTable_Object = MibTable
swL2MulticastFilterPortMaxGroupTable = _SwL2MulticastFilterPortMaxGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    swL2MulticastFilterPortMaxGroupTable.setStatus("current")
_SwL2MulticastFilterPortMaxGroupEntry_Object = MibTableRow
swL2MulticastFilterPortMaxGroupEntry = _SwL2MulticastFilterPortMaxGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 4, 1)
)
swL2MulticastFilterPortMaxGroupEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2MulticastFilterPortMaxGroupPortIndex"),
)
if mibBuilder.loadTexts:
    swL2MulticastFilterPortMaxGroupEntry.setStatus("current")
_SwL2MulticastFilterPortMaxGroupPortIndex_Type = Integer32
_SwL2MulticastFilterPortMaxGroupPortIndex_Object = MibTableColumn
swL2MulticastFilterPortMaxGroupPortIndex = _SwL2MulticastFilterPortMaxGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 4, 1, 1),
    _SwL2MulticastFilterPortMaxGroupPortIndex_Type()
)
swL2MulticastFilterPortMaxGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2MulticastFilterPortMaxGroupPortIndex.setStatus("current")


class _SwL2MulticastFilterPortMaxGroup_Type(Integer32):
    """Custom type swL2MulticastFilterPortMaxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SwL2MulticastFilterPortMaxGroup_Type.__name__ = "Integer32"
_SwL2MulticastFilterPortMaxGroup_Object = MibTableColumn
swL2MulticastFilterPortMaxGroup = _SwL2MulticastFilterPortMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 4, 1, 2),
    _SwL2MulticastFilterPortMaxGroup_Type()
)
swL2MulticastFilterPortMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MulticastFilterPortMaxGroup.setStatus("current")
_SwL2LimitedMulticastFilterVIDTable_Object = MibTable
swL2LimitedMulticastFilterVIDTable = _SwL2LimitedMulticastFilterVIDTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterVIDTable.setStatus("current")
_SwL2LimitedMulticastFilterVIDEntry_Object = MibTableRow
swL2LimitedMulticastFilterVIDEntry = _SwL2LimitedMulticastFilterVIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 5, 1)
)
swL2LimitedMulticastFilterVIDEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2LimitedMulticastFilterVIDIndex"),
)
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterVIDEntry.setStatus("current")
_SwL2LimitedMulticastFilterVIDIndex_Type = Integer32
_SwL2LimitedMulticastFilterVIDIndex_Object = MibTableColumn
swL2LimitedMulticastFilterVIDIndex = _SwL2LimitedMulticastFilterVIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 5, 1, 1),
    _SwL2LimitedMulticastFilterVIDIndex_Type()
)
swL2LimitedMulticastFilterVIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterVIDIndex.setStatus("current")


class _SwL2LimitedMulticastFilterVIDAccess_Type(Integer32):
    """Custom type swL2LimitedMulticastFilterVIDAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_SwL2LimitedMulticastFilterVIDAccess_Type.__name__ = "Integer32"
_SwL2LimitedMulticastFilterVIDAccess_Object = MibTableColumn
swL2LimitedMulticastFilterVIDAccess = _SwL2LimitedMulticastFilterVIDAccess_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 5, 1, 2),
    _SwL2LimitedMulticastFilterVIDAccess_Type()
)
swL2LimitedMulticastFilterVIDAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterVIDAccess.setStatus("current")
_SwL2LimitedMulticastFilterVIDProfileID_Type = DisplayString
_SwL2LimitedMulticastFilterVIDProfileID_Object = MibTableColumn
swL2LimitedMulticastFilterVIDProfileID = _SwL2LimitedMulticastFilterVIDProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 5, 1, 3),
    _SwL2LimitedMulticastFilterVIDProfileID_Type()
)
swL2LimitedMulticastFilterVIDProfileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterVIDProfileID.setStatus("current")


class _SwL2LimitedMulticastFilterVIDProfileStatus_Type(Integer32):
    """Custom type swL2LimitedMulticastFilterVIDProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("other", 1))
    )


_SwL2LimitedMulticastFilterVIDProfileStatus_Type.__name__ = "Integer32"
_SwL2LimitedMulticastFilterVIDProfileStatus_Object = MibTableColumn
swL2LimitedMulticastFilterVIDProfileStatus = _SwL2LimitedMulticastFilterVIDProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 5, 1, 4),
    _SwL2LimitedMulticastFilterVIDProfileStatus_Type()
)
swL2LimitedMulticastFilterVIDProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2LimitedMulticastFilterVIDProfileStatus.setStatus("current")
_SwL2MulticastFilterVIDMaxGroupTable_Object = MibTable
swL2MulticastFilterVIDMaxGroupTable = _SwL2MulticastFilterVIDMaxGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 6)
)
if mibBuilder.loadTexts:
    swL2MulticastFilterVIDMaxGroupTable.setStatus("current")
_SwL2MulticastFilterVIDMaxGroupEntry_Object = MibTableRow
swL2MulticastFilterVIDMaxGroupEntry = _SwL2MulticastFilterVIDMaxGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 6, 1)
)
swL2MulticastFilterVIDMaxGroupEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2MulticastFilterVIDMaxGroupVIDIndex"),
)
if mibBuilder.loadTexts:
    swL2MulticastFilterVIDMaxGroupEntry.setStatus("current")
_SwL2MulticastFilterVIDMaxGroupVIDIndex_Type = Integer32
_SwL2MulticastFilterVIDMaxGroupVIDIndex_Object = MibTableColumn
swL2MulticastFilterVIDMaxGroupVIDIndex = _SwL2MulticastFilterVIDMaxGroupVIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 6, 1, 1),
    _SwL2MulticastFilterVIDMaxGroupVIDIndex_Type()
)
swL2MulticastFilterVIDMaxGroupVIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2MulticastFilterVIDMaxGroupVIDIndex.setStatus("current")


class _SwL2MulticastFilterVIDMaxGroup_Type(Integer32):
    """Custom type swL2MulticastFilterVIDMaxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SwL2MulticastFilterVIDMaxGroup_Type.__name__ = "Integer32"
_SwL2MulticastFilterVIDMaxGroup_Object = MibTableColumn
swL2MulticastFilterVIDMaxGroup = _SwL2MulticastFilterVIDMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 5, 6, 1, 2),
    _SwL2MulticastFilterVIDMaxGroup_Type()
)
swL2MulticastFilterVIDMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MulticastFilterVIDMaxGroup.setStatus("current")
_SwL2QOSMgmt_ObjectIdentity = ObjectIdentity
swL2QOSMgmt = _SwL2QOSMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6)
)
_SwL2QOSBandwidthControlTable_Object = MibTable
swL2QOSBandwidthControlTable = _SwL2QOSBandwidthControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    swL2QOSBandwidthControlTable.setStatus("current")
_SwL2QOSBandwidthControlEntry_Object = MibTableRow
swL2QOSBandwidthControlEntry = _SwL2QOSBandwidthControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 1, 1)
)
swL2QOSBandwidthControlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2QOSBandwidthPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 1, 1, 1),
    _SwL2QOSBandwidthPortIndex_Type()
)
swL2QOSBandwidthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthPortIndex.setStatus("current")


class _SwL2QOSBandwidthRxRate_Type(Integer32):
    """Custom type swL2QOSBandwidthRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SwL2QOSBandwidthRxRate_Type.__name__ = "Integer32"
_SwL2QOSBandwidthRxRate_Object = MibTableColumn
swL2QOSBandwidthRxRate = _SwL2QOSBandwidthRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 1, 1, 2),
    _SwL2QOSBandwidthRxRate_Type()
)
swL2QOSBandwidthRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRxRate.setStatus("current")


class _SwL2QOSBandwidthTxRate_Type(Integer32):
    """Custom type swL2QOSBandwidthTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SwL2QOSBandwidthTxRate_Type.__name__ = "Integer32"
_SwL2QOSBandwidthTxRate_Object = MibTableColumn
swL2QOSBandwidthTxRate = _SwL2QOSBandwidthTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 1, 1, 3),
    _SwL2QOSBandwidthTxRate_Type()
)
swL2QOSBandwidthTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSBandwidthTxRate.setStatus("current")
_SwL2QOSBandwidthRadiusRxRate_Type = Integer32
_SwL2QOSBandwidthRadiusRxRate_Object = MibTableColumn
swL2QOSBandwidthRadiusRxRate = _SwL2QOSBandwidthRadiusRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 1, 1, 4),
    _SwL2QOSBandwidthRadiusRxRate_Type()
)
swL2QOSBandwidthRadiusRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRadiusRxRate.setStatus("current")
_SwL2QOSBandwidthRadiusTxRate_Type = Integer32
_SwL2QOSBandwidthRadiusTxRate_Object = MibTableColumn
swL2QOSBandwidthRadiusTxRate = _SwL2QOSBandwidthRadiusTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 1, 1, 5),
    _SwL2QOSBandwidthRadiusTxRate_Type()
)
swL2QOSBandwidthRadiusTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRadiusTxRate.setStatus("current")
_SwL2QOSSchedulingTable_Object = MibTable
swL2QOSSchedulingTable = _SwL2QOSSchedulingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    swL2QOSSchedulingTable.setStatus("current")
_SwL2QOSSchedulingEntry_Object = MibTableRow
swL2QOSSchedulingEntry = _SwL2QOSSchedulingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 2, 1)
)
swL2QOSSchedulingEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2QOSSchedulingClassIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 2, 1, 3),
    _SwL2QOSSchedulingMechanism_Type()
)
swL2QOSSchedulingMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSSchedulingMechanism.setStatus("current")


class _SwL2QOSSchedulingMaxLatency_Type(Integer32):
    """Custom type swL2QOSSchedulingMaxLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL2QOSSchedulingMaxLatency_Type.__name__ = "Integer32"
_SwL2QOSSchedulingMaxLatency_Object = MibTableColumn
swL2QOSSchedulingMaxLatency = _SwL2QOSSchedulingMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 2, 1, 4),
    _SwL2QOSSchedulingMaxLatency_Type()
)
swL2QOSSchedulingMaxLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSSchedulingMaxLatency.setStatus("current")
_SwL2QOS8021pUserPriorityTable_Object = MibTable
swL2QOS8021pUserPriorityTable = _SwL2QOS8021pUserPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityTable.setStatus("current")
_SwL2QOS8021pUserPriorityEntry_Object = MibTableRow
swL2QOS8021pUserPriorityEntry = _SwL2QOS8021pUserPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 3, 1)
)
swL2QOS8021pUserPriorityEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2QOS8021pUserPriorityIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 3, 1, 2),
    _SwL2QOS8021pUserPriorityClass_Type()
)
swL2QOS8021pUserPriorityClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityClass.setStatus("current")
_SwL2QOS8021pDefaultPriorityTable_Object = MibTable
swL2QOS8021pDefaultPriorityTable = _SwL2QOS8021pDefaultPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityTable.setStatus("current")
_SwL2QOS8021pDefaultPriorityEntry_Object = MibTableRow
swL2QOS8021pDefaultPriorityEntry = _SwL2QOS8021pDefaultPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 4, 1)
)
swL2QOS8021pDefaultPriorityEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2QOS8021pDefaultPriorityIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 4, 1, 2),
    _SwL2QOS8021pDefaultPriority_Type()
)
swL2QOS8021pDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriority.setStatus("current")
_SwL2QOS8021pRadiusPriority_Type = Integer32
_SwL2QOS8021pRadiusPriority_Object = MibTableColumn
swL2QOS8021pRadiusPriority = _SwL2QOS8021pRadiusPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 6, 6),
    _SwL2QOSHolPreventionCtrl_Type()
)
swL2QOSHolPreventionCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSHolPreventionCtrl.setStatus("current")
_SwL2PortSecurityMgmt_ObjectIdentity = ObjectIdentity
swL2PortSecurityMgmt = _SwL2PortSecurityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7)
)
_SwL2PortSecurityControlTable_Object = MibTable
swL2PortSecurityControlTable = _SwL2PortSecurityControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    swL2PortSecurityControlTable.setStatus("current")
_SwL2PortSecurityControlEntry_Object = MibTableRow
swL2PortSecurityControlEntry = _SwL2PortSecurityControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 1, 1)
)
swL2PortSecurityControlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2PortSecurityPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 1, 1, 4),
    _SwL2PortSecurityAdmState_Type()
)
swL2PortSecurityAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityAdmState.setStatus("current")


class _SwL2PortSecurityEntryClearCtrl_Type(Integer32):
    """Custom type swL2PortSecurityEntryClearCtrl based on Integer32"""
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


_SwL2PortSecurityEntryClearCtrl_Type.__name__ = "Integer32"
_SwL2PortSecurityEntryClearCtrl_Object = MibTableColumn
swL2PortSecurityEntryClearCtrl = _SwL2PortSecurityEntryClearCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 1, 1, 5),
    _SwL2PortSecurityEntryClearCtrl_Type()
)
swL2PortSecurityEntryClearCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityEntryClearCtrl.setStatus("current")
_SwL2PortSecurityDelCtrl_ObjectIdentity = ObjectIdentity
swL2PortSecurityDelCtrl = _SwL2PortSecurityDelCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 2, 1),
    _SwL2PortSecurityDelVlanName_Type()
)
swL2PortSecurityDelVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityDelVlanName.setStatus("current")


class _SwL2PortSecurityDelPort_Type(Integer32):
    """Custom type swL2PortSecurityDelPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 768),
    )


_SwL2PortSecurityDelPort_Type.__name__ = "Integer32"
_SwL2PortSecurityDelPort_Object = MibScalar
swL2PortSecurityDelPort = _SwL2PortSecurityDelPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 2, 2),
    _SwL2PortSecurityDelPort_Type()
)
swL2PortSecurityDelPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityDelPort.setStatus("current")
_SwL2PortSecurityDelMacAddress_Type = MacAddress
_SwL2PortSecurityDelMacAddress_Object = MibScalar
swL2PortSecurityDelMacAddress = _SwL2PortSecurityDelMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 2, 4),
    _SwL2PortSecurityDelActivity_Type()
)
swL2PortSecurityDelActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityDelActivity.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 7, 3),
    _SwL2PortSecurityTrapLogState_Type()
)
swL2PortSecurityTrapLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityTrapLogState.setStatus("current")
_SwL2DhcpRelayMgmt_ObjectIdentity = ObjectIdentity
swL2DhcpRelayMgmt = _SwL2DhcpRelayMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8)
)


class _SwL2DhcpRelayState_Type(Integer32):
    """Custom type swL2DhcpRelayState based on Integer32"""
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


_SwL2DhcpRelayState_Type.__name__ = "Integer32"
_SwL2DhcpRelayState_Object = MibScalar
swL2DhcpRelayState = _SwL2DhcpRelayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8, 1),
    _SwL2DhcpRelayState_Type()
)
swL2DhcpRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayState.setStatus("current")


class _SwL2DhcpRelayHopCount_Type(Integer32):
    """Custom type swL2DhcpRelayHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SwL2DhcpRelayHopCount_Type.__name__ = "Integer32"
_SwL2DhcpRelayHopCount_Object = MibScalar
swL2DhcpRelayHopCount = _SwL2DhcpRelayHopCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8, 2),
    _SwL2DhcpRelayHopCount_Type()
)
swL2DhcpRelayHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayHopCount.setStatus("current")


class _SwL2DhcpRelayTimeThreshold_Type(Integer32):
    """Custom type swL2DhcpRelayTimeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2DhcpRelayTimeThreshold_Type.__name__ = "Integer32"
_SwL2DhcpRelayTimeThreshold_Object = MibScalar
swL2DhcpRelayTimeThreshold = _SwL2DhcpRelayTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8, 3),
    _SwL2DhcpRelayTimeThreshold_Type()
)
swL2DhcpRelayTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayTimeThreshold.setStatus("current")


class _SwL2DhcpRelayOption82State_Type(Integer32):
    """Custom type swL2DhcpRelayOption82State based on Integer32"""
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


_SwL2DhcpRelayOption82State_Type.__name__ = "Integer32"
_SwL2DhcpRelayOption82State_Object = MibScalar
swL2DhcpRelayOption82State = _SwL2DhcpRelayOption82State_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8, 4),
    _SwL2DhcpRelayOption82State_Type()
)
swL2DhcpRelayOption82State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayOption82State.setStatus("current")


class _SwL2DhcpRelayOption82Check_Type(Integer32):
    """Custom type swL2DhcpRelayOption82Check based on Integer32"""
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


_SwL2DhcpRelayOption82Check_Type.__name__ = "Integer32"
_SwL2DhcpRelayOption82Check_Object = MibScalar
swL2DhcpRelayOption82Check = _SwL2DhcpRelayOption82Check_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8, 5),
    _SwL2DhcpRelayOption82Check_Type()
)
swL2DhcpRelayOption82Check.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayOption82Check.setStatus("current")


class _SwL2DhcpRelayOption82Policy_Type(Integer32):
    """Custom type swL2DhcpRelayOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("keep", 3),
          ("replace", 1))
    )


_SwL2DhcpRelayOption82Policy_Type.__name__ = "Integer32"
_SwL2DhcpRelayOption82Policy_Object = MibScalar
swL2DhcpRelayOption82Policy = _SwL2DhcpRelayOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8, 6),
    _SwL2DhcpRelayOption82Policy_Type()
)
swL2DhcpRelayOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayOption82Policy.setStatus("current")
_SwL2DhcpRelayCtrlTable_Object = MibTable
swL2DhcpRelayCtrlTable = _SwL2DhcpRelayCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8, 7)
)
if mibBuilder.loadTexts:
    swL2DhcpRelayCtrlTable.setStatus("current")
_SwL2DhcpRelayCtrlEntry_Object = MibTableRow
swL2DhcpRelayCtrlEntry = _SwL2DhcpRelayCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8, 7, 1)
)
swL2DhcpRelayCtrlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2DhcpRelayCtrlInterfaceName"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2DhcpRelayCtrlServer"),
)
if mibBuilder.loadTexts:
    swL2DhcpRelayCtrlEntry.setStatus("current")


class _SwL2DhcpRelayCtrlInterfaceName_Type(DisplayString):
    """Custom type swL2DhcpRelayCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL2DhcpRelayCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL2DhcpRelayCtrlInterfaceName_Object = MibTableColumn
swL2DhcpRelayCtrlInterfaceName = _SwL2DhcpRelayCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8, 7, 1, 1),
    _SwL2DhcpRelayCtrlInterfaceName_Type()
)
swL2DhcpRelayCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DhcpRelayCtrlInterfaceName.setStatus("current")
_SwL2DhcpRelayCtrlServer_Type = IpAddress
_SwL2DhcpRelayCtrlServer_Object = MibTableColumn
swL2DhcpRelayCtrlServer = _SwL2DhcpRelayCtrlServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8, 7, 1, 2),
    _SwL2DhcpRelayCtrlServer_Type()
)
swL2DhcpRelayCtrlServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DhcpRelayCtrlServer.setStatus("current")


class _SwL2DhcpRelayCtrlState_Type(Integer32):
    """Custom type swL2DhcpRelayCtrlState based on Integer32"""
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


_SwL2DhcpRelayCtrlState_Type.__name__ = "Integer32"
_SwL2DhcpRelayCtrlState_Object = MibTableColumn
swL2DhcpRelayCtrlState = _SwL2DhcpRelayCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 8, 7, 1, 3),
    _SwL2DhcpRelayCtrlState_Type()
)
swL2DhcpRelayCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayCtrlState.setStatus("current")
_SwL2TrunkMgmt_ObjectIdentity = ObjectIdentity
swL2TrunkMgmt = _SwL2TrunkMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 2),
    _SwL2TrunkCurrentNumEntries_Type()
)
swL2TrunkCurrentNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkCurrentNumEntries.setStatus("current")
_SwL2TrunkCtrlTable_Object = MibTable
swL2TrunkCtrlTable = _SwL2TrunkCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 3)
)
if mibBuilder.loadTexts:
    swL2TrunkCtrlTable.setStatus("current")
_SwL2TrunkCtrlEntry_Object = MibTableRow
swL2TrunkCtrlEntry = _SwL2TrunkCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 3, 1)
)
swL2TrunkCtrlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2TrunkIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 3, 1, 3),
    _SwL2TrunkMasterPort_Type()
)
swL2TrunkMasterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkMasterPort.setStatus("current")
_SwL2TrunkMember_Type = PortList
_SwL2TrunkMember_Object = MibTableColumn
swL2TrunkMember = _SwL2TrunkMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 3, 1, 6),
    _SwL2TrunkType_Type()
)
swL2TrunkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkType.setStatus("current")
_SwL2TrunkState_Type = RowStatus
_SwL2TrunkState_Object = MibTableColumn
swL2TrunkState = _SwL2TrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 3, 1, 7),
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ip-destination", 6),
          ("ip-source", 5),
          ("ip-source-dest", 7),
          ("l4-destination-port", 9),
          ("l4-source-dest-port", 10),
          ("l4-source-port", 8),
          ("mac-destination", 3),
          ("mac-source", 2),
          ("mac-source-dest", 4),
          ("other", 1))
    )


_SwL2TrunkAlgorithm_Type.__name__ = "Integer32"
_SwL2TrunkAlgorithm_Object = MibScalar
swL2TrunkAlgorithm = _SwL2TrunkAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 4),
    _SwL2TrunkAlgorithm_Type()
)
swL2TrunkAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkAlgorithm.setStatus("current")
_SwL2TrunkLACPPortTable_Object = MibTable
swL2TrunkLACPPortTable = _SwL2TrunkLACPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 5)
)
if mibBuilder.loadTexts:
    swL2TrunkLACPPortTable.setStatus("current")
_SwL2TrunkLACPPortEntry_Object = MibTableRow
swL2TrunkLACPPortEntry = _SwL2TrunkLACPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 5, 1)
)
swL2TrunkLACPPortEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2TrunkLACPPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 5, 1, 2),
    _SwL2TrunkLACPPortState_Type()
)
swL2TrunkLACPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkLACPPortState.setStatus("current")
_SwL2TrunkVLANTable_Object = MibTable
swL2TrunkVLANTable = _SwL2TrunkVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 6)
)
if mibBuilder.loadTexts:
    swL2TrunkVLANTable.setStatus("current")
_SwL2TrunkVLANEntry_Object = MibTableRow
swL2TrunkVLANEntry = _SwL2TrunkVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 6, 1)
)
swL2TrunkVLANEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2TrunkVLANPort"),
)
if mibBuilder.loadTexts:
    swL2TrunkVLANEntry.setStatus("current")


class _SwL2TrunkVLANPort_Type(Integer32):
    """Custom type swL2TrunkVLANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrunkVLANPort_Type.__name__ = "Integer32"
_SwL2TrunkVLANPort_Object = MibTableColumn
swL2TrunkVLANPort = _SwL2TrunkVLANPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 6, 1, 1),
    _SwL2TrunkVLANPort_Type()
)
swL2TrunkVLANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkVLANPort.setStatus("current")


class _SwL2TrunkVLANState_Type(Integer32):
    """Custom type swL2TrunkVLANState based on Integer32"""
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


_SwL2TrunkVLANState_Type.__name__ = "Integer32"
_SwL2TrunkVLANState_Object = MibTableColumn
swL2TrunkVLANState = _SwL2TrunkVLANState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 9, 6, 1, 2),
    _SwL2TrunkVLANState_Type()
)
swL2TrunkVLANState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkVLANState.setStatus("current")
_SwL2MirrorMgmt_ObjectIdentity = ObjectIdentity
swL2MirrorMgmt = _SwL2MirrorMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 1),
    _SwL2MirrorLogicTargetPort_Type()
)
swL2MirrorLogicTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorLogicTargetPort.setStatus("current")
_SwL2MirrorPortSourceIngress_Type = PortList
_SwL2MirrorPortSourceIngress_Object = MibScalar
swL2MirrorPortSourceIngress = _SwL2MirrorPortSourceIngress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 2),
    _SwL2MirrorPortSourceIngress_Type()
)
swL2MirrorPortSourceIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortSourceIngress.setStatus("current")
_SwL2MirrorPortSourceEgress_Type = PortList
_SwL2MirrorPortSourceEgress_Object = MibScalar
swL2MirrorPortSourceEgress = _SwL2MirrorPortSourceEgress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 4),
    _SwL2MirrorPortState_Type()
)
swL2MirrorPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortState.setStatus("current")
_SwL2MirrorGroupTable_Object = MibTable
swL2MirrorGroupTable = _SwL2MirrorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 5)
)
if mibBuilder.loadTexts:
    swL2MirrorGroupTable.setStatus("current")
_SwL2MirrorGroupEntry_Object = MibTableRow
swL2MirrorGroupEntry = _SwL2MirrorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 5, 1)
)
swL2MirrorGroupEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2MirrorGroupID"),
)
if mibBuilder.loadTexts:
    swL2MirrorGroupEntry.setStatus("current")
_SwL2MirrorGroupID_Type = Integer32
_SwL2MirrorGroupID_Object = MibTableColumn
swL2MirrorGroupID = _SwL2MirrorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 5, 1, 1),
    _SwL2MirrorGroupID_Type()
)
swL2MirrorGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2MirrorGroupID.setStatus("current")
_SwL2MirrorGroupRowStatus_Type = RowStatus
_SwL2MirrorGroupRowStatus_Object = MibTableColumn
swL2MirrorGroupRowStatus = _SwL2MirrorGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 5, 1, 2),
    _SwL2MirrorGroupRowStatus_Type()
)
swL2MirrorGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupRowStatus.setStatus("current")


class _SwL2MirrorGroupState_Type(Integer32):
    """Custom type swL2MirrorGroupState based on Integer32"""
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


_SwL2MirrorGroupState_Type.__name__ = "Integer32"
_SwL2MirrorGroupState_Object = MibTableColumn
swL2MirrorGroupState = _SwL2MirrorGroupState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 5, 1, 3),
    _SwL2MirrorGroupState_Type()
)
swL2MirrorGroupState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupState.setStatus("current")


class _SwL2MirrorGroupTargetPort_Type(Integer32):
    """Custom type swL2MirrorGroupTargetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2MirrorGroupTargetPort_Type.__name__ = "Integer32"
_SwL2MirrorGroupTargetPort_Object = MibTableColumn
swL2MirrorGroupTargetPort = _SwL2MirrorGroupTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 5, 1, 4),
    _SwL2MirrorGroupTargetPort_Type()
)
swL2MirrorGroupTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupTargetPort.setStatus("current")
_SwL2MirrorGroupSourceIngress_Type = PortList
_SwL2MirrorGroupSourceIngress_Object = MibTableColumn
swL2MirrorGroupSourceIngress = _SwL2MirrorGroupSourceIngress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 5, 1, 5),
    _SwL2MirrorGroupSourceIngress_Type()
)
swL2MirrorGroupSourceIngress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupSourceIngress.setStatus("current")
_SwL2MirrorGroupSourceEngress_Type = PortList
_SwL2MirrorGroupSourceEngress_Object = MibTableColumn
swL2MirrorGroupSourceEngress = _SwL2MirrorGroupSourceEngress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 10, 5, 1, 6),
    _SwL2MirrorGroupSourceEngress_Type()
)
swL2MirrorGroupSourceEngress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupSourceEngress.setStatus("current")
_SwL2IGMPMgmt_ObjectIdentity = ObjectIdentity
swL2IGMPMgmt = _SwL2IGMPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 2),
    _SwL2IGMPMaxIpGroupNumPerVlan_Type()
)
swL2IGMPMaxIpGroupNumPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMaxIpGroupNumPerVlan.setStatus("current")


class _SwL2IGMPSnoopingMulticastVlanState_Type(Integer32):
    """Custom type swL2IGMPSnoopingMulticastVlanState based on Integer32"""
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


_SwL2IGMPSnoopingMulticastVlanState_Type.__name__ = "Integer32"
_SwL2IGMPSnoopingMulticastVlanState_Object = MibScalar
swL2IGMPSnoopingMulticastVlanState = _SwL2IGMPSnoopingMulticastVlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 3),
    _SwL2IGMPSnoopingMulticastVlanState_Type()
)
swL2IGMPSnoopingMulticastVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingMulticastVlanState.setStatus("current")
_SwL2IGMPCtrlTable_Object = MibTable
swL2IGMPCtrlTable = _SwL2IGMPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    swL2IGMPCtrlTable.setStatus("current")
_SwL2IGMPCtrlEntry_Object = MibTableRow
swL2IGMPCtrlEntry = _SwL2IGMPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1)
)
swL2IGMPCtrlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPCtrlVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPCtrlEntry.setStatus("current")


class _SwL2IGMPCtrlVid_Type(Integer32):
    """Custom type swL2IGMPCtrlVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2IGMPCtrlVid_Type.__name__ = "Integer32"
_SwL2IGMPCtrlVid_Object = MibTableColumn
swL2IGMPCtrlVid = _SwL2IGMPCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 6),
    _SwL2IGMPHostTimeout_Type()
)
swL2IGMPHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPHostTimeout.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 7),
    _SwL2IGMPRouteTimeout_Type()
)
swL2IGMPRouteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouteTimeout.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 8),
    _SwL2IGMPLeaveTimer_Type()
)
swL2IGMPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPLeaveTimer.setStatus("obsolete")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 13),
    _SwL2IGMPQueryVersion_Type()
)
swL2IGMPQueryVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPQueryVersion.setStatus("current")


class _SwL2IGMPRateLimit_Type(Integer32):
    """Custom type swL2IGMPRateLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SwL2IGMPRateLimit_Type.__name__ = "Integer32"
_SwL2IGMPRateLimit_Object = MibTableColumn
swL2IGMPRateLimit = _SwL2IGMPRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 14),
    _SwL2IGMPRateLimit_Type()
)
swL2IGMPRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRateLimit.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 4, 1, 15),
    _SwL2IGMPReportSuppression_Type()
)
swL2IGMPReportSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPReportSuppression.setStatus("current")
_SwL2IGMPQueryInfoTable_Object = MibTable
swL2IGMPQueryInfoTable = _SwL2IGMPQueryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 5)
)
if mibBuilder.loadTexts:
    swL2IGMPQueryInfoTable.setStatus("current")
_SwL2IGMPQueryInfoEntry_Object = MibTableRow
swL2IGMPQueryInfoEntry = _SwL2IGMPQueryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 5, 1)
)
swL2IGMPQueryInfoEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPInfoVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPQueryInfoEntry.setStatus("current")


class _SwL2IGMPInfoVid_Type(Integer32):
    """Custom type swL2IGMPInfoVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2IGMPInfoVid_Type.__name__ = "Integer32"
_SwL2IGMPInfoVid_Object = MibTableColumn
swL2IGMPInfoVid = _SwL2IGMPInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 5, 1, 2),
    _SwL2IGMPInfoQueryCount_Type()
)
swL2IGMPInfoQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoQueryCount.setStatus("obsolete")


class _SwL2IGMPInfoTxQueryCount_Type(Integer32):
    """Custom type swL2IGMPInfoTxQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPInfoTxQueryCount_Type.__name__ = "Integer32"
_SwL2IGMPInfoTxQueryCount_Object = MibTableColumn
swL2IGMPInfoTxQueryCount = _SwL2IGMPInfoTxQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 5, 1, 3),
    _SwL2IGMPInfoTxQueryCount_Type()
)
swL2IGMPInfoTxQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoTxQueryCount.setStatus("obsolete")
_SwL2IGMPQueryIPAddress_Type = IpAddress
_SwL2IGMPQueryIPAddress_Object = MibTableColumn
swL2IGMPQueryIPAddress = _SwL2IGMPQueryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 5, 1, 4),
    _SwL2IGMPQueryIPAddress_Type()
)
swL2IGMPQueryIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPQueryIPAddress.setStatus("current")


class _SwL2IGMPQueryExpiryTime_Type(Integer32):
    """Custom type swL2IGMPQueryExpiryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPQueryExpiryTime_Type.__name__ = "Integer32"
_SwL2IGMPQueryExpiryTime_Object = MibTableColumn
swL2IGMPQueryExpiryTime = _SwL2IGMPQueryExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 5, 1, 5),
    _SwL2IGMPQueryExpiryTime_Type()
)
swL2IGMPQueryExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPQueryExpiryTime.setStatus("current")
_SwL2IGMPInfoTable_Object = MibTable
swL2IGMPInfoTable = _SwL2IGMPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 6)
)
if mibBuilder.loadTexts:
    swL2IGMPInfoTable.setStatus("obsolete")
_SwL2IGMPInfoEntry_Object = MibTableRow
swL2IGMPInfoEntry = _SwL2IGMPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 6, 1)
)
swL2IGMPInfoEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPVid"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPGroupIpAddr"),
)
if mibBuilder.loadTexts:
    swL2IGMPInfoEntry.setStatus("obsolete")


class _SwL2IGMPVid_Type(Integer32):
    """Custom type swL2IGMPVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2IGMPVid_Type.__name__ = "Integer32"
_SwL2IGMPVid_Object = MibTableColumn
swL2IGMPVid = _SwL2IGMPVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 6, 1, 1),
    _SwL2IGMPVid_Type()
)
swL2IGMPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVid.setStatus("obsolete")
_SwL2IGMPGroupIpAddr_Type = IpAddress
_SwL2IGMPGroupIpAddr_Object = MibTableColumn
swL2IGMPGroupIpAddr = _SwL2IGMPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 6, 1, 2),
    _SwL2IGMPGroupIpAddr_Type()
)
swL2IGMPGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPGroupIpAddr.setStatus("obsolete")
_SwL2IGMPMacAddr_Type = MacAddress
_SwL2IGMPMacAddr_Object = MibTableColumn
swL2IGMPMacAddr = _SwL2IGMPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 6, 1, 3),
    _SwL2IGMPMacAddr_Type()
)
swL2IGMPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMacAddr.setStatus("obsolete")
_SwL2IGMPPortMap_Type = PortList
_SwL2IGMPPortMap_Object = MibTableColumn
swL2IGMPPortMap = _SwL2IGMPPortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 6, 1, 4),
    _SwL2IGMPPortMap_Type()
)
swL2IGMPPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortMap.setStatus("obsolete")


class _SwL2IGMPIpGroupReportCount_Type(Integer32):
    """Custom type swL2IGMPIpGroupReportCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPIpGroupReportCount_Type.__name__ = "Integer32"
_SwL2IGMPIpGroupReportCount_Object = MibTableColumn
swL2IGMPIpGroupReportCount = _SwL2IGMPIpGroupReportCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 6, 1, 5),
    _SwL2IGMPIpGroupReportCount_Type()
)
swL2IGMPIpGroupReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPIpGroupReportCount.setStatus("obsolete")
_SwL2IGMPVersion_Type = Integer32
_SwL2IGMPVersion_Object = MibTableColumn
swL2IGMPVersion = _SwL2IGMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 6, 1, 6),
    _SwL2IGMPVersion_Type()
)
swL2IGMPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVersion.setStatus("obsolete")


class _SwL2IGMPGroupMode_Type(Integer32):
    """Custom type swL2IGMPGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_SwL2IGMPGroupMode_Type.__name__ = "Integer32"
_SwL2IGMPGroupMode_Object = MibTableColumn
swL2IGMPGroupMode = _SwL2IGMPGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 6, 1, 7),
    _SwL2IGMPGroupMode_Type()
)
swL2IGMPGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPGroupMode.setStatus("obsolete")
_SwL2IGMPRouterPortTable_Object = MibTable
swL2IGMPRouterPortTable = _SwL2IGMPRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 7)
)
if mibBuilder.loadTexts:
    swL2IGMPRouterPortTable.setStatus("current")
_SwL2IGMPRouterPortEntry_Object = MibTableRow
swL2IGMPRouterPortEntry = _SwL2IGMPRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 7, 1)
)
swL2IGMPRouterPortEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPRouterPortVlanid"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 7, 1, 1),
    _SwL2IGMPRouterPortVlanid_Type()
)
swL2IGMPRouterPortVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortVlanid.setStatus("current")


class _SwL2IGMPRouterPortVlanName_Type(DisplayString):
    """Custom type swL2IGMPRouterPortVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2IGMPRouterPortVlanName_Type.__name__ = "DisplayString"
_SwL2IGMPRouterPortVlanName_Object = MibTableColumn
swL2IGMPRouterPortVlanName = _SwL2IGMPRouterPortVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 7, 1, 2),
    _SwL2IGMPRouterPortVlanName_Type()
)
swL2IGMPRouterPortVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortVlanName.setStatus("current")
_SwL2IGMPRouterPortStaticPortList_Type = PortList
_SwL2IGMPRouterPortStaticPortList_Object = MibTableColumn
swL2IGMPRouterPortStaticPortList = _SwL2IGMPRouterPortStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 7, 1, 3),
    _SwL2IGMPRouterPortStaticPortList_Type()
)
swL2IGMPRouterPortStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortStaticPortList.setStatus("current")
_SwL2IGMPRouterPortDynamicPortList_Type = PortList
_SwL2IGMPRouterPortDynamicPortList_Object = MibTableColumn
swL2IGMPRouterPortDynamicPortList = _SwL2IGMPRouterPortDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 7, 1, 4),
    _SwL2IGMPRouterPortDynamicPortList_Type()
)
swL2IGMPRouterPortDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortDynamicPortList.setStatus("current")
_SwL2IGMPRouterPortForbiddenPortList_Type = PortList
_SwL2IGMPRouterPortForbiddenPortList_Object = MibTableColumn
swL2IGMPRouterPortForbiddenPortList = _SwL2IGMPRouterPortForbiddenPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 7, 1, 5),
    _SwL2IGMPRouterPortForbiddenPortList_Type()
)
swL2IGMPRouterPortForbiddenPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortForbiddenPortList.setStatus("current")
_SwL2IGMPMulticastVlanTable_Object = MibTable
swL2IGMPMulticastVlanTable = _SwL2IGMPMulticastVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8)
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanTable.setStatus("current")
_SwL2IGMPMulticastVlanEntry_Object = MibTableRow
swL2IGMPMulticastVlanEntry = _SwL2IGMPMulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1)
)
swL2IGMPMulticastVlanEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPMulticastVlanid"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 2),
    _SwL2IGMPMulticastVlanName_Type()
)
swL2IGMPMulticastVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanName.setStatus("current")
_SwL2IGMPMulticastVlanSourcePort_Type = PortList
_SwL2IGMPMulticastVlanSourcePort_Object = MibTableColumn
swL2IGMPMulticastVlanSourcePort = _SwL2IGMPMulticastVlanSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 3),
    _SwL2IGMPMulticastVlanSourcePort_Type()
)
swL2IGMPMulticastVlanSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanSourcePort.setStatus("current")
_SwL2IGMPMulticastVlanMemberPort_Type = PortList
_SwL2IGMPMulticastVlanMemberPort_Object = MibTableColumn
swL2IGMPMulticastVlanMemberPort = _SwL2IGMPMulticastVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 4),
    _SwL2IGMPMulticastVlanMemberPort_Type()
)
swL2IGMPMulticastVlanMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanMemberPort.setStatus("current")
_SwL2IGMPMulticastVlanTagMemberPort_Type = PortList
_SwL2IGMPMulticastVlanTagMemberPort_Object = MibTableColumn
swL2IGMPMulticastVlanTagMemberPort = _SwL2IGMPMulticastVlanTagMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 6),
    _SwL2IGMPMulticastVlanState_Type()
)
swL2IGMPMulticastVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanState.setStatus("current")
_SwL2IGMPMulticastVlanReplaceSourceIp_Type = IpAddress
_SwL2IGMPMulticastVlanReplaceSourceIp_Object = MibTableColumn
swL2IGMPMulticastVlanReplaceSourceIp = _SwL2IGMPMulticastVlanReplaceSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 7),
    _SwL2IGMPMulticastVlanReplaceSourceIp_Type()
)
swL2IGMPMulticastVlanReplaceSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanReplaceSourceIp.setStatus("current")
_SwL2IGMPMulticastVlanRowStatus_Type = RowStatus
_SwL2IGMPMulticastVlanRowStatus_Object = MibTableColumn
swL2IGMPMulticastVlanRowStatus = _SwL2IGMPMulticastVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 9),
    _SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type()
)
swL2IGMPMulticastVlanRemoveAllMcastAddrListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanRemoveAllMcastAddrListAction.setStatus("current")
_SwL2IGMPMulticastVlanUntagSourcePort_Type = PortList
_SwL2IGMPMulticastVlanUntagSourcePort_Object = MibTableColumn
swL2IGMPMulticastVlanUntagSourcePort = _SwL2IGMPMulticastVlanUntagSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 10),
    _SwL2IGMPMulticastVlanUntagSourcePort_Type()
)
swL2IGMPMulticastVlanUntagSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanUntagSourcePort.setStatus("current")


class _SwL2IGMPMulticastVlanRemapPriority_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanRemapPriority based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SwL2IGMPMulticastVlanRemapPriority_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanRemapPriority_Object = MibTableColumn
swL2IGMPMulticastVlanRemapPriority = _SwL2IGMPMulticastVlanRemapPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 11),
    _SwL2IGMPMulticastVlanRemapPriority_Type()
)
swL2IGMPMulticastVlanRemapPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanRemapPriority.setStatus("current")


class _SwL2IGMPMulticastVlanReplacePriority_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanReplacePriority based on Integer32"""
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


_SwL2IGMPMulticastVlanReplacePriority_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanReplacePriority_Object = MibTableColumn
swL2IGMPMulticastVlanReplacePriority = _SwL2IGMPMulticastVlanReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 8, 1, 12),
    _SwL2IGMPMulticastVlanReplacePriority_Type()
)
swL2IGMPMulticastVlanReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanReplacePriority.setStatus("current")
_SwL2IGMPMulticastVlanGroupTable_Object = MibTable
swL2IGMPMulticastVlanGroupTable = _SwL2IGMPMulticastVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 9)
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupTable.setStatus("current")
_SwL2IGMPMulticastVlanGroupEntry_Object = MibTableRow
swL2IGMPMulticastVlanGroupEntry = _SwL2IGMPMulticastVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 9, 1)
)
swL2IGMPMulticastVlanGroupEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPMulticastVlanGroupVid"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPMulticastVlanGroupFromIp"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPMulticastVlanGroupToIp"),
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupEntry.setStatus("current")


class _SwL2IGMPMulticastVlanGroupVid_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2IGMPMulticastVlanGroupVid_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanGroupVid_Object = MibTableColumn
swL2IGMPMulticastVlanGroupVid = _SwL2IGMPMulticastVlanGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 9, 1, 1),
    _SwL2IGMPMulticastVlanGroupVid_Type()
)
swL2IGMPMulticastVlanGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupVid.setStatus("current")
_SwL2IGMPMulticastVlanGroupFromIp_Type = IpAddress
_SwL2IGMPMulticastVlanGroupFromIp_Object = MibTableColumn
swL2IGMPMulticastVlanGroupFromIp = _SwL2IGMPMulticastVlanGroupFromIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 9, 1, 2),
    _SwL2IGMPMulticastVlanGroupFromIp_Type()
)
swL2IGMPMulticastVlanGroupFromIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupFromIp.setStatus("current")
_SwL2IGMPMulticastVlanGroupToIp_Type = IpAddress
_SwL2IGMPMulticastVlanGroupToIp_Object = MibTableColumn
swL2IGMPMulticastVlanGroupToIp = _SwL2IGMPMulticastVlanGroupToIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 9, 1, 3),
    _SwL2IGMPMulticastVlanGroupToIp_Type()
)
swL2IGMPMulticastVlanGroupToIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupToIp.setStatus("current")
_SwL2IGMPMulticastVlanGroupStatus_Type = RowStatus
_SwL2IGMPMulticastVlanGroupStatus_Object = MibTableColumn
swL2IGMPMulticastVlanGroupStatus = _SwL2IGMPMulticastVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 9, 1, 4),
    _SwL2IGMPMulticastVlanGroupStatus_Type()
)
swL2IGMPMulticastVlanGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupStatus.setStatus("current")
_SwL2IGMPv3Table_Object = MibTable
swL2IGMPv3Table = _SwL2IGMPv3Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 10)
)
if mibBuilder.loadTexts:
    swL2IGMPv3Table.setStatus("current")
_SwL2IGMPv3Entry_Object = MibTableRow
swL2IGMPv3Entry = _SwL2IGMPv3Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 10, 1)
)
swL2IGMPv3Entry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPVid"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPGroupIpAddr"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPv3SourceIPAddr"),
)
if mibBuilder.loadTexts:
    swL2IGMPv3Entry.setStatus("current")
_SwL2IGMPv3SourceIPAddr_Type = IpAddress
_SwL2IGMPv3SourceIPAddr_Object = MibTableColumn
swL2IGMPv3SourceIPAddr = _SwL2IGMPv3SourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 10, 1, 1),
    _SwL2IGMPv3SourceIPAddr_Type()
)
swL2IGMPv3SourceIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPv3SourceIPAddr.setStatus("current")


class _SwL2IGMPv3Forwarding_Type(Integer32):
    """Custom type swL2IGMPv3Forwarding based on Integer32"""
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


_SwL2IGMPv3Forwarding_Type.__name__ = "Integer32"
_SwL2IGMPv3Forwarding_Object = MibTableColumn
swL2IGMPv3Forwarding = _SwL2IGMPv3Forwarding_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 10, 1, 2),
    _SwL2IGMPv3Forwarding_Type()
)
swL2IGMPv3Forwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPv3Forwarding.setStatus("current")
_SwL2IGMPv3ExpireTimer_Type = Integer32
_SwL2IGMPv3ExpireTimer_Object = MibTableColumn
swL2IGMPv3ExpireTimer = _SwL2IGMPv3ExpireTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 10, 1, 3),
    _SwL2IGMPv3ExpireTimer_Type()
)
swL2IGMPv3ExpireTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPv3ExpireTimer.setStatus("current")
_SwIGMPSnoopingGroupTable_Object = MibTable
swIGMPSnoopingGroupTable = _SwIGMPSnoopingGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11)
)
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupTable.setStatus("current")
_SwIGMPSnoopingGroupEntry_Object = MibTableRow
swIGMPSnoopingGroupEntry = _SwIGMPSnoopingGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11, 1)
)
swIGMPSnoopingGroupEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swIGMPSnoopingGroupVid"),
    (0, "DES3200-52P-L2MGMT-MIB", "swIGMPSnoopingGroupGroupAddr"),
    (0, "DES3200-52P-L2MGMT-MIB", "swIGMPSnoopingGroupSourceAddr"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11, 1, 1),
    _SwIGMPSnoopingGroupVid_Type()
)
swIGMPSnoopingGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupVid.setStatus("current")
_SwIGMPSnoopingGroupGroupAddr_Type = IpAddress
_SwIGMPSnoopingGroupGroupAddr_Object = MibTableColumn
swIGMPSnoopingGroupGroupAddr = _SwIGMPSnoopingGroupGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11, 1, 2),
    _SwIGMPSnoopingGroupGroupAddr_Type()
)
swIGMPSnoopingGroupGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupGroupAddr.setStatus("current")
_SwIGMPSnoopingGroupSourceAddr_Type = IpAddress
_SwIGMPSnoopingGroupSourceAddr_Object = MibTableColumn
swIGMPSnoopingGroupSourceAddr = _SwIGMPSnoopingGroupSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11, 1, 3),
    _SwIGMPSnoopingGroupSourceAddr_Type()
)
swIGMPSnoopingGroupSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupSourceAddr.setStatus("current")
_SwIGMPSnoopingGroupIncludePortMap_Type = PortList
_SwIGMPSnoopingGroupIncludePortMap_Object = MibTableColumn
swIGMPSnoopingGroupIncludePortMap = _SwIGMPSnoopingGroupIncludePortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11, 1, 4),
    _SwIGMPSnoopingGroupIncludePortMap_Type()
)
swIGMPSnoopingGroupIncludePortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupIncludePortMap.setStatus("current")
_SwIGMPSnoopingGroupExcludePortMap_Type = PortList
_SwIGMPSnoopingGroupExcludePortMap_Object = MibTableColumn
swIGMPSnoopingGroupExcludePortMap = _SwIGMPSnoopingGroupExcludePortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11, 1, 5),
    _SwIGMPSnoopingGroupExcludePortMap_Type()
)
swIGMPSnoopingGroupExcludePortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupExcludePortMap.setStatus("current")
_SwIGMPSnoopingGroupReportCount_Type = Integer32
_SwIGMPSnoopingGroupReportCount_Object = MibTableColumn
swIGMPSnoopingGroupReportCount = _SwIGMPSnoopingGroupReportCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11, 1, 6),
    _SwIGMPSnoopingGroupReportCount_Type()
)
swIGMPSnoopingGroupReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupReportCount.setStatus("current")
_SwIGMPSnoopingGroupUpTime_Type = TimeTicks
_SwIGMPSnoopingGroupUpTime_Object = MibTableColumn
swIGMPSnoopingGroupUpTime = _SwIGMPSnoopingGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11, 1, 7),
    _SwIGMPSnoopingGroupUpTime_Type()
)
swIGMPSnoopingGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupUpTime.setStatus("current")
_SwIGMPSnoopingGroupExpiryTime_Type = TimeTicks
_SwIGMPSnoopingGroupExpiryTime_Object = MibTableColumn
swIGMPSnoopingGroupExpiryTime = _SwIGMPSnoopingGroupExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11, 1, 8),
    _SwIGMPSnoopingGroupExpiryTime_Type()
)
swIGMPSnoopingGroupExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupExpiryTime.setStatus("current")
_SwIGMPSnoopingGroupRouterPorts_Type = PortList
_SwIGMPSnoopingGroupRouterPorts_Object = MibTableColumn
swIGMPSnoopingGroupRouterPorts = _SwIGMPSnoopingGroupRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11, 1, 9),
    _SwIGMPSnoopingGroupRouterPorts_Type()
)
swIGMPSnoopingGroupRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupRouterPorts.setStatus("current")
_SwIGMPSnoopingGroupStaticMemberPorts_Type = PortList
_SwIGMPSnoopingGroupStaticMemberPorts_Object = MibTableColumn
swIGMPSnoopingGroupStaticMemberPorts = _SwIGMPSnoopingGroupStaticMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 11, 1, 10),
    _SwIGMPSnoopingGroupStaticMemberPorts_Type()
)
swIGMPSnoopingGroupStaticMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupStaticMemberPorts.setStatus("current")
_SwL2IGMPDynIpMultMgmt_ObjectIdentity = ObjectIdentity
swL2IGMPDynIpMultMgmt = _SwL2IGMPDynIpMultMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 12)
)
_SwL2IGMPDynIPMultMaxEntry_Type = Integer32
_SwL2IGMPDynIPMultMaxEntry_Object = MibScalar
swL2IGMPDynIPMultMaxEntry = _SwL2IGMPDynIPMultMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 12, 1),
    _SwL2IGMPDynIPMultMaxEntry_Type()
)
swL2IGMPDynIPMultMaxEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPDynIPMultMaxEntry.setStatus("current")
_SwL2IGMPSnoopingClearDynIpMult_ObjectIdentity = ObjectIdentity
swL2IGMPSnoopingClearDynIpMult = _SwL2IGMPSnoopingClearDynIpMult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 12, 2)
)
_SwL2IGMPSnoopingClearDynIpMultVID_Type = VlanId
_SwL2IGMPSnoopingClearDynIpMultVID_Object = MibScalar
swL2IGMPSnoopingClearDynIpMultVID = _SwL2IGMPSnoopingClearDynIpMultVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 12, 2, 1),
    _SwL2IGMPSnoopingClearDynIpMultVID_Type()
)
swL2IGMPSnoopingClearDynIpMultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingClearDynIpMultVID.setStatus("current")
_SwL2IGMPSnoopingClearDynIpMultIP_Type = IpAddress
_SwL2IGMPSnoopingClearDynIpMultIP_Object = MibScalar
swL2IGMPSnoopingClearDynIpMultIP = _SwL2IGMPSnoopingClearDynIpMultIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 12, 2, 2),
    _SwL2IGMPSnoopingClearDynIpMultIP_Type()
)
swL2IGMPSnoopingClearDynIpMultIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingClearDynIpMultIP.setStatus("current")


class _SwL2IGMPSnoopingClearDynIpMultAction_Type(Integer32):
    """Custom type swL2IGMPSnoopingClearDynIpMultAction based on Integer32"""
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
        *(("all", 1),
          ("group", 3),
          ("other", 4),
          ("vlan", 2))
    )


_SwL2IGMPSnoopingClearDynIpMultAction_Type.__name__ = "Integer32"
_SwL2IGMPSnoopingClearDynIpMultAction_Object = MibScalar
swL2IGMPSnoopingClearDynIpMultAction = _SwL2IGMPSnoopingClearDynIpMultAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 12, 2, 3),
    _SwL2IGMPSnoopingClearDynIpMultAction_Type()
)
swL2IGMPSnoopingClearDynIpMultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingClearDynIpMultAction.setStatus("current")
_SwL2IGMPDynIPMultCtrlTable_Object = MibTable
swL2IGMPDynIPMultCtrlTable = _SwL2IGMPDynIPMultCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 12, 3)
)
if mibBuilder.loadTexts:
    swL2IGMPDynIPMultCtrlTable.setStatus("current")
_SwL2IGMPDynIPMultCtrlEntry_Object = MibTableRow
swL2IGMPDynIPMultCtrlEntry = _SwL2IGMPDynIPMultCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 12, 3, 1)
)
swL2IGMPDynIPMultCtrlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPCtrlVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPDynIPMultCtrlEntry.setStatus("current")


class _SwL2IGMPDynIPMultVlanState_Type(Integer32):
    """Custom type swL2IGMPDynIPMultVlanState based on Integer32"""
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


_SwL2IGMPDynIPMultVlanState_Type.__name__ = "Integer32"
_SwL2IGMPDynIPMultVlanState_Object = MibTableColumn
swL2IGMPDynIPMultVlanState = _SwL2IGMPDynIPMultVlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 12, 3, 1, 1),
    _SwL2IGMPDynIPMultVlanState_Type()
)
swL2IGMPDynIPMultVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPDynIPMultVlanState.setStatus("current")


class _SwL2IGMPDynIPMultVlanAge_Type(Integer32):
    """Custom type swL2IGMPDynIPMultVlanAge based on Integer32"""
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


_SwL2IGMPDynIPMultVlanAge_Type.__name__ = "Integer32"
_SwL2IGMPDynIPMultVlanAge_Object = MibTableColumn
swL2IGMPDynIPMultVlanAge = _SwL2IGMPDynIPMultVlanAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 12, 3, 1, 2),
    _SwL2IGMPDynIPMultVlanAge_Type()
)
swL2IGMPDynIPMultVlanAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPDynIPMultVlanAge.setStatus("current")


class _SwL2IGMPDynIPMultGroupExpiryTime_Type(Integer32):
    """Custom type swL2IGMPDynIPMultGroupExpiryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPDynIPMultGroupExpiryTime_Type.__name__ = "Integer32"
_SwL2IGMPDynIPMultGroupExpiryTime_Object = MibTableColumn
swL2IGMPDynIPMultGroupExpiryTime = _SwL2IGMPDynIPMultGroupExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 12, 3, 1, 3),
    _SwL2IGMPDynIPMultGroupExpiryTime_Type()
)
swL2IGMPDynIPMultGroupExpiryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPDynIPMultGroupExpiryTime.setStatus("current")
_SwL2IGMPAccessAuthTable_Object = MibTable
swL2IGMPAccessAuthTable = _SwL2IGMPAccessAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 13)
)
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthTable.setStatus("current")
_SwL2IGMPAccessAuthEntry_Object = MibTableRow
swL2IGMPAccessAuthEntry = _SwL2IGMPAccessAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 13, 1)
)
swL2IGMPAccessAuthEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPAccessAuthPort"),
)
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthEntry.setStatus("current")
_SwL2IGMPAccessAuthPort_Type = Integer32
_SwL2IGMPAccessAuthPort_Object = MibTableColumn
swL2IGMPAccessAuthPort = _SwL2IGMPAccessAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 13, 1, 1),
    _SwL2IGMPAccessAuthPort_Type()
)
swL2IGMPAccessAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthPort.setStatus("current")


class _SwL2IGMPAccessAuthState_Type(Integer32):
    """Custom type swL2IGMPAccessAuthState based on Integer32"""
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


_SwL2IGMPAccessAuthState_Type.__name__ = "Integer32"
_SwL2IGMPAccessAuthState_Object = MibTableColumn
swL2IGMPAccessAuthState = _SwL2IGMPAccessAuthState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 13, 1, 2),
    _SwL2IGMPAccessAuthState_Type()
)
swL2IGMPAccessAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthState.setStatus("current")
_SwL2IGMPCountrInfoMgmt_ObjectIdentity = ObjectIdentity
swL2IGMPCountrInfoMgmt = _SwL2IGMPCountrInfoMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14)
)


class _SwL2IGMPSnoopingClearStatisticsCounter_Type(Integer32):
    """Custom type swL2IGMPSnoopingClearStatisticsCounter based on Integer32"""
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


_SwL2IGMPSnoopingClearStatisticsCounter_Type.__name__ = "Integer32"
_SwL2IGMPSnoopingClearStatisticsCounter_Object = MibScalar
swL2IGMPSnoopingClearStatisticsCounter = _SwL2IGMPSnoopingClearStatisticsCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 1),
    _SwL2IGMPSnoopingClearStatisticsCounter_Type()
)
swL2IGMPSnoopingClearStatisticsCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingClearStatisticsCounter.setStatus("current")
_SwL2IGMPVlanCounterInfoTable_Object = MibTable
swL2IGMPVlanCounterInfoTable = _SwL2IGMPVlanCounterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2)
)
if mibBuilder.loadTexts:
    swL2IGMPVlanCounterInfoTable.setStatus("current")
_SwL2IGMPVlanCounterInfoEntry_Object = MibTableRow
swL2IGMPVlanCounterInfoEntry = _SwL2IGMPVlanCounterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1)
)
swL2IGMPVlanCounterInfoEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPVlanCounterInfoVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPVlanCounterInfoEntry.setStatus("current")


class _SwL2IGMPVlanCounterInfoVid_Type(Integer32):
    """Custom type swL2IGMPVlanCounterInfoVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2IGMPVlanCounterInfoVid_Type.__name__ = "Integer32"
_SwL2IGMPVlanCounterInfoVid_Object = MibTableColumn
swL2IGMPVlanCounterInfoVid = _SwL2IGMPVlanCounterInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 1),
    _SwL2IGMPVlanCounterInfoVid_Type()
)
swL2IGMPVlanCounterInfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanCounterInfoVid.setStatus("current")


class _SwL2IGMPVlanCounterGroupNumber_Type(Integer32):
    """Custom type swL2IGMPVlanCounterGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPVlanCounterGroupNumber_Type.__name__ = "Integer32"
_SwL2IGMPVlanCounterGroupNumber_Object = MibTableColumn
swL2IGMPVlanCounterGroupNumber = _SwL2IGMPVlanCounterGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 2),
    _SwL2IGMPVlanCounterGroupNumber_Type()
)
swL2IGMPVlanCounterGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanCounterGroupNumber.setStatus("current")
_SwL2IGMPVlanQueryCountV1_Type = Counter32
_SwL2IGMPVlanQueryCountV1_Object = MibTableColumn
swL2IGMPVlanQueryCountV1 = _SwL2IGMPVlanQueryCountV1_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 3),
    _SwL2IGMPVlanQueryCountV1_Type()
)
swL2IGMPVlanQueryCountV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanQueryCountV1.setStatus("current")
_SwL2IGMPVlanQueryCountV2_Type = Counter32
_SwL2IGMPVlanQueryCountV2_Object = MibTableColumn
swL2IGMPVlanQueryCountV2 = _SwL2IGMPVlanQueryCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 4),
    _SwL2IGMPVlanQueryCountV2_Type()
)
swL2IGMPVlanQueryCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanQueryCountV2.setStatus("current")
_SwL2IGMPVlanQueryCountV3_Type = Counter32
_SwL2IGMPVlanQueryCountV3_Object = MibTableColumn
swL2IGMPVlanQueryCountV3 = _SwL2IGMPVlanQueryCountV3_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 5),
    _SwL2IGMPVlanQueryCountV3_Type()
)
swL2IGMPVlanQueryCountV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanQueryCountV3.setStatus("current")
_SwL2IGMPVlanDropQueryCount_Type = Counter32
_SwL2IGMPVlanDropQueryCount_Object = MibTableColumn
swL2IGMPVlanDropQueryCount = _SwL2IGMPVlanDropQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 6),
    _SwL2IGMPVlanDropQueryCount_Type()
)
swL2IGMPVlanDropQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanDropQueryCount.setStatus("current")
_SwL2IGMPVlanReportCountV1_Type = Counter32
_SwL2IGMPVlanReportCountV1_Object = MibTableColumn
swL2IGMPVlanReportCountV1 = _SwL2IGMPVlanReportCountV1_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 7),
    _SwL2IGMPVlanReportCountV1_Type()
)
swL2IGMPVlanReportCountV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanReportCountV1.setStatus("current")
_SwL2IGMPVlanReportCountV2_Type = Counter32
_SwL2IGMPVlanReportCountV2_Object = MibTableColumn
swL2IGMPVlanReportCountV2 = _SwL2IGMPVlanReportCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 8),
    _SwL2IGMPVlanReportCountV2_Type()
)
swL2IGMPVlanReportCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanReportCountV2.setStatus("current")
_SwL2IGMPVlanReportCountV3_Type = Counter32
_SwL2IGMPVlanReportCountV3_Object = MibTableColumn
swL2IGMPVlanReportCountV3 = _SwL2IGMPVlanReportCountV3_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 9),
    _SwL2IGMPVlanReportCountV3_Type()
)
swL2IGMPVlanReportCountV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanReportCountV3.setStatus("current")
_SwL2IGMPVlanLeaveCountV2_Type = Counter32
_SwL2IGMPVlanLeaveCountV2_Object = MibTableColumn
swL2IGMPVlanLeaveCountV2 = _SwL2IGMPVlanLeaveCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 10),
    _SwL2IGMPVlanLeaveCountV2_Type()
)
swL2IGMPVlanLeaveCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanLeaveCountV2.setStatus("current")
_SwL2IGMPVlanDropedReportAndLeaveCount_Type = Counter32
_SwL2IGMPVlanDropedReportAndLeaveCount_Object = MibTableColumn
swL2IGMPVlanDropedReportAndLeaveCount = _SwL2IGMPVlanDropedReportAndLeaveCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 11),
    _SwL2IGMPVlanDropedReportAndLeaveCount_Type()
)
swL2IGMPVlanDropedReportAndLeaveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanDropedReportAndLeaveCount.setStatus("current")
_SwL2IGMPVlanDroppedByMaxGroupLimitation_Type = Counter32
_SwL2IGMPVlanDroppedByMaxGroupLimitation_Object = MibTableColumn
swL2IGMPVlanDroppedByMaxGroupLimitation = _SwL2IGMPVlanDroppedByMaxGroupLimitation_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 12),
    _SwL2IGMPVlanDroppedByMaxGroupLimitation_Type()
)
swL2IGMPVlanDroppedByMaxGroupLimitation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanDroppedByMaxGroupLimitation.setStatus("current")
_SwL2IGMPVlanDroppedByGroupFilter_Type = Counter32
_SwL2IGMPVlanDroppedByGroupFilter_Object = MibTableColumn
swL2IGMPVlanDroppedByGroupFilter = _SwL2IGMPVlanDroppedByGroupFilter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 13),
    _SwL2IGMPVlanDroppedByGroupFilter_Type()
)
swL2IGMPVlanDroppedByGroupFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanDroppedByGroupFilter.setStatus("current")
_SwL2IGMPVlanTxQueryCountV1_Type = Counter32
_SwL2IGMPVlanTxQueryCountV1_Object = MibTableColumn
swL2IGMPVlanTxQueryCountV1 = _SwL2IGMPVlanTxQueryCountV1_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 14),
    _SwL2IGMPVlanTxQueryCountV1_Type()
)
swL2IGMPVlanTxQueryCountV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanTxQueryCountV1.setStatus("current")
_SwL2IGMPVlanTxQueryCountV2_Type = Counter32
_SwL2IGMPVlanTxQueryCountV2_Object = MibTableColumn
swL2IGMPVlanTxQueryCountV2 = _SwL2IGMPVlanTxQueryCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 15),
    _SwL2IGMPVlanTxQueryCountV2_Type()
)
swL2IGMPVlanTxQueryCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanTxQueryCountV2.setStatus("current")
_SwL2IGMPVlanTxQueryCountV3_Type = Counter32
_SwL2IGMPVlanTxQueryCountV3_Object = MibTableColumn
swL2IGMPVlanTxQueryCountV3 = _SwL2IGMPVlanTxQueryCountV3_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 16),
    _SwL2IGMPVlanTxQueryCountV3_Type()
)
swL2IGMPVlanTxQueryCountV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanTxQueryCountV3.setStatus("current")
_SwL2IGMPVlanTxReportCountV1_Type = Counter32
_SwL2IGMPVlanTxReportCountV1_Object = MibTableColumn
swL2IGMPVlanTxReportCountV1 = _SwL2IGMPVlanTxReportCountV1_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 17),
    _SwL2IGMPVlanTxReportCountV1_Type()
)
swL2IGMPVlanTxReportCountV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanTxReportCountV1.setStatus("current")
_SwL2IGMPVlanTxReportCountV2_Type = Counter32
_SwL2IGMPVlanTxReportCountV2_Object = MibTableColumn
swL2IGMPVlanTxReportCountV2 = _SwL2IGMPVlanTxReportCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 18),
    _SwL2IGMPVlanTxReportCountV2_Type()
)
swL2IGMPVlanTxReportCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanTxReportCountV2.setStatus("current")
_SwL2IGMPVlanTxReportCountV3_Type = Counter32
_SwL2IGMPVlanTxReportCountV3_Object = MibTableColumn
swL2IGMPVlanTxReportCountV3 = _SwL2IGMPVlanTxReportCountV3_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 19),
    _SwL2IGMPVlanTxReportCountV3_Type()
)
swL2IGMPVlanTxReportCountV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanTxReportCountV3.setStatus("current")
_SwL2IGMPVlanTxLeaveCountV2_Type = Counter32
_SwL2IGMPVlanTxLeaveCountV2_Object = MibTableColumn
swL2IGMPVlanTxLeaveCountV2 = _SwL2IGMPVlanTxLeaveCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 2, 1, 20),
    _SwL2IGMPVlanTxLeaveCountV2_Type()
)
swL2IGMPVlanTxLeaveCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVlanTxLeaveCountV2.setStatus("current")
_SwL2IGMPPortCounterInfoTable_Object = MibTable
swL2IGMPPortCounterInfoTable = _SwL2IGMPPortCounterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3)
)
if mibBuilder.loadTexts:
    swL2IGMPPortCounterInfoTable.setStatus("current")
_SwL2IGMPPortCounterInfoEntry_Object = MibTableRow
swL2IGMPPortCounterInfoEntry = _SwL2IGMPPortCounterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1)
)
swL2IGMPPortCounterInfoEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPPortCounterInfoIndex"),
)
if mibBuilder.loadTexts:
    swL2IGMPPortCounterInfoEntry.setStatus("current")


class _SwL2IGMPPortCounterInfoIndex_Type(Integer32):
    """Custom type swL2IGMPPortCounterInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPPortCounterInfoIndex_Type.__name__ = "Integer32"
_SwL2IGMPPortCounterInfoIndex_Object = MibTableColumn
swL2IGMPPortCounterInfoIndex = _SwL2IGMPPortCounterInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 1),
    _SwL2IGMPPortCounterInfoIndex_Type()
)
swL2IGMPPortCounterInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortCounterInfoIndex.setStatus("current")


class _SwL2IGMPPortCounterGroupNumber_Type(Integer32):
    """Custom type swL2IGMPPortCounterGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPPortCounterGroupNumber_Type.__name__ = "Integer32"
_SwL2IGMPPortCounterGroupNumber_Object = MibTableColumn
swL2IGMPPortCounterGroupNumber = _SwL2IGMPPortCounterGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 2),
    _SwL2IGMPPortCounterGroupNumber_Type()
)
swL2IGMPPortCounterGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortCounterGroupNumber.setStatus("current")
_SwL2IGMPPortQueryCountV1_Type = Counter32
_SwL2IGMPPortQueryCountV1_Object = MibTableColumn
swL2IGMPPortQueryCountV1 = _SwL2IGMPPortQueryCountV1_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 3),
    _SwL2IGMPPortQueryCountV1_Type()
)
swL2IGMPPortQueryCountV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortQueryCountV1.setStatus("current")
_SwL2IGMPPortQueryCountV2_Type = Counter32
_SwL2IGMPPortQueryCountV2_Object = MibTableColumn
swL2IGMPPortQueryCountV2 = _SwL2IGMPPortQueryCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 4),
    _SwL2IGMPPortQueryCountV2_Type()
)
swL2IGMPPortQueryCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortQueryCountV2.setStatus("current")
_SwL2IGMPPortQueryCountV3_Type = Counter32
_SwL2IGMPPortQueryCountV3_Object = MibTableColumn
swL2IGMPPortQueryCountV3 = _SwL2IGMPPortQueryCountV3_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 5),
    _SwL2IGMPPortQueryCountV3_Type()
)
swL2IGMPPortQueryCountV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortQueryCountV3.setStatus("current")
_SwL2IGMPPortDropQueryCount_Type = Counter32
_SwL2IGMPPortDropQueryCount_Object = MibTableColumn
swL2IGMPPortDropQueryCount = _SwL2IGMPPortDropQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 6),
    _SwL2IGMPPortDropQueryCount_Type()
)
swL2IGMPPortDropQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortDropQueryCount.setStatus("current")
_SwL2IGMPPortReportCountV1_Type = Counter32
_SwL2IGMPPortReportCountV1_Object = MibTableColumn
swL2IGMPPortReportCountV1 = _SwL2IGMPPortReportCountV1_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 7),
    _SwL2IGMPPortReportCountV1_Type()
)
swL2IGMPPortReportCountV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortReportCountV1.setStatus("current")
_SwL2IGMPPortReportCountV2_Type = Counter32
_SwL2IGMPPortReportCountV2_Object = MibTableColumn
swL2IGMPPortReportCountV2 = _SwL2IGMPPortReportCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 8),
    _SwL2IGMPPortReportCountV2_Type()
)
swL2IGMPPortReportCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortReportCountV2.setStatus("current")
_SwL2IGMPPortReportCountV3_Type = Counter32
_SwL2IGMPPortReportCountV3_Object = MibTableColumn
swL2IGMPPortReportCountV3 = _SwL2IGMPPortReportCountV3_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 9),
    _SwL2IGMPPortReportCountV3_Type()
)
swL2IGMPPortReportCountV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortReportCountV3.setStatus("current")
_SwL2IGMPPortLeaveCountV2_Type = Counter32
_SwL2IGMPPortLeaveCountV2_Object = MibTableColumn
swL2IGMPPortLeaveCountV2 = _SwL2IGMPPortLeaveCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 10),
    _SwL2IGMPPortLeaveCountV2_Type()
)
swL2IGMPPortLeaveCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortLeaveCountV2.setStatus("current")
_SwL2IGMPPortDropedReportAndLeaveCount_Type = Counter32
_SwL2IGMPPortDropedReportAndLeaveCount_Object = MibTableColumn
swL2IGMPPortDropedReportAndLeaveCount = _SwL2IGMPPortDropedReportAndLeaveCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 11),
    _SwL2IGMPPortDropedReportAndLeaveCount_Type()
)
swL2IGMPPortDropedReportAndLeaveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortDropedReportAndLeaveCount.setStatus("current")
_SwL2IGMPPortDroppedByMaxGroupLimitation_Type = Counter32
_SwL2IGMPPortDroppedByMaxGroupLimitation_Object = MibTableColumn
swL2IGMPPortDroppedByMaxGroupLimitation = _SwL2IGMPPortDroppedByMaxGroupLimitation_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 12),
    _SwL2IGMPPortDroppedByMaxGroupLimitation_Type()
)
swL2IGMPPortDroppedByMaxGroupLimitation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortDroppedByMaxGroupLimitation.setStatus("current")
_SwL2IGMPPortDroppedByGroupFilter_Type = Counter32
_SwL2IGMPPortDroppedByGroupFilter_Object = MibTableColumn
swL2IGMPPortDroppedByGroupFilter = _SwL2IGMPPortDroppedByGroupFilter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 13),
    _SwL2IGMPPortDroppedByGroupFilter_Type()
)
swL2IGMPPortDroppedByGroupFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortDroppedByGroupFilter.setStatus("current")
_SwL2IGMPPortTxQueryCountV1_Type = Counter32
_SwL2IGMPPortTxQueryCountV1_Object = MibTableColumn
swL2IGMPPortTxQueryCountV1 = _SwL2IGMPPortTxQueryCountV1_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 14),
    _SwL2IGMPPortTxQueryCountV1_Type()
)
swL2IGMPPortTxQueryCountV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortTxQueryCountV1.setStatus("current")
_SwL2IGMPPortTxQueryCountV2_Type = Counter32
_SwL2IGMPPortTxQueryCountV2_Object = MibTableColumn
swL2IGMPPortTxQueryCountV2 = _SwL2IGMPPortTxQueryCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 15),
    _SwL2IGMPPortTxQueryCountV2_Type()
)
swL2IGMPPortTxQueryCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortTxQueryCountV2.setStatus("current")
_SwL2IGMPPortTxQueryCountV3_Type = Counter32
_SwL2IGMPPortTxQueryCountV3_Object = MibTableColumn
swL2IGMPPortTxQueryCountV3 = _SwL2IGMPPortTxQueryCountV3_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 16),
    _SwL2IGMPPortTxQueryCountV3_Type()
)
swL2IGMPPortTxQueryCountV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortTxQueryCountV3.setStatus("current")
_SwL2IGMPPortTxReportCountV1_Type = Counter32
_SwL2IGMPPortTxReportCountV1_Object = MibTableColumn
swL2IGMPPortTxReportCountV1 = _SwL2IGMPPortTxReportCountV1_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 17),
    _SwL2IGMPPortTxReportCountV1_Type()
)
swL2IGMPPortTxReportCountV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortTxReportCountV1.setStatus("current")
_SwL2IGMPPortTxReportCountV2_Type = Counter32
_SwL2IGMPPortTxReportCountV2_Object = MibTableColumn
swL2IGMPPortTxReportCountV2 = _SwL2IGMPPortTxReportCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 18),
    _SwL2IGMPPortTxReportCountV2_Type()
)
swL2IGMPPortTxReportCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortTxReportCountV2.setStatus("current")
_SwL2IGMPPortTxReportCountV3_Type = Counter32
_SwL2IGMPPortTxReportCountV3_Object = MibTableColumn
swL2IGMPPortTxReportCountV3 = _SwL2IGMPPortTxReportCountV3_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 19),
    _SwL2IGMPPortTxReportCountV3_Type()
)
swL2IGMPPortTxReportCountV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortTxReportCountV3.setStatus("current")
_SwL2IGMPPortTxLeaveCountV2_Type = Counter32
_SwL2IGMPPortTxLeaveCountV2_Object = MibTableColumn
swL2IGMPPortTxLeaveCountV2 = _SwL2IGMPPortTxLeaveCountV2_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 14, 3, 1, 20),
    _SwL2IGMPPortTxLeaveCountV2_Type()
)
swL2IGMPPortTxLeaveCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortTxLeaveCountV2.setStatus("current")
_SwL2IGMPRouterIPAddressTable_Object = MibTable
swL2IGMPRouterIPAddressTable = _SwL2IGMPRouterIPAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 15)
)
if mibBuilder.loadTexts:
    swL2IGMPRouterIPAddressTable.setStatus("current")
_SwL2IGMPRouterIPAddressEntry_Object = MibTableRow
swL2IGMPRouterIPAddressEntry = _SwL2IGMPRouterIPAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 15, 1)
)
swL2IGMPRouterIPAddressEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPRouterIPAddressVid"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPRouterIPAddress"),
)
if mibBuilder.loadTexts:
    swL2IGMPRouterIPAddressEntry.setStatus("current")


class _SwL2IGMPRouterIPAddressVid_Type(Integer32):
    """Custom type swL2IGMPRouterIPAddressVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2IGMPRouterIPAddressVid_Type.__name__ = "Integer32"
_SwL2IGMPRouterIPAddressVid_Object = MibTableColumn
swL2IGMPRouterIPAddressVid = _SwL2IGMPRouterIPAddressVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 15, 1, 1),
    _SwL2IGMPRouterIPAddressVid_Type()
)
swL2IGMPRouterIPAddressVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterIPAddressVid.setStatus("current")
_SwL2IGMPRouterIPAddress_Type = IpAddress
_SwL2IGMPRouterIPAddress_Object = MibTableColumn
swL2IGMPRouterIPAddress = _SwL2IGMPRouterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 15, 1, 2),
    _SwL2IGMPRouterIPAddress_Type()
)
swL2IGMPRouterIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterIPAddress.setStatus("current")
_SwL2IGMPSnoopingStaticGroupTable_Object = MibTable
swL2IGMPSnoopingStaticGroupTable = _SwL2IGMPSnoopingStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 16)
)
if mibBuilder.loadTexts:
    swL2IGMPSnoopingStaticGroupTable.setStatus("current")
_SwL2IGMPSnoopingStaticGroupEntry_Object = MibTableRow
swL2IGMPSnoopingStaticGroupEntry = _SwL2IGMPSnoopingStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 16, 1)
)
swL2IGMPSnoopingStaticGroupEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPSnoopingStaticGroupVID"),
    (0, "DES3200-52P-L2MGMT-MIB", "swL2IGMPSnoopingStaticGroupIPaddress"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 16, 1, 1),
    _SwL2IGMPSnoopingStaticGroupVID_Type()
)
swL2IGMPSnoopingStaticGroupVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingStaticGroupVID.setStatus("current")
_SwL2IGMPSnoopingStaticGroupIPaddress_Type = IpAddress
_SwL2IGMPSnoopingStaticGroupIPaddress_Object = MibTableColumn
swL2IGMPSnoopingStaticGroupIPaddress = _SwL2IGMPSnoopingStaticGroupIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 16, 1, 2),
    _SwL2IGMPSnoopingStaticGroupIPaddress_Type()
)
swL2IGMPSnoopingStaticGroupIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingStaticGroupIPaddress.setStatus("current")
_SwL2IGMPSnoopingStaticGroupMemberPortList_Type = PortList
_SwL2IGMPSnoopingStaticGroupMemberPortList_Object = MibTableColumn
swL2IGMPSnoopingStaticGroupMemberPortList = _SwL2IGMPSnoopingStaticGroupMemberPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 16, 1, 3),
    _SwL2IGMPSnoopingStaticGroupMemberPortList_Type()
)
swL2IGMPSnoopingStaticGroupMemberPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingStaticGroupMemberPortList.setStatus("current")
_SwL2IGMPSnoopingStaticGroupRowStatus_Type = RowStatus
_SwL2IGMPSnoopingStaticGroupRowStatus_Object = MibTableColumn
swL2IGMPSnoopingStaticGroupRowStatus = _SwL2IGMPSnoopingStaticGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 11, 16, 1, 4),
    _SwL2IGMPSnoopingStaticGroupRowStatus_Type()
)
swL2IGMPSnoopingStaticGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingStaticGroupRowStatus.setStatus("current")
_SwL2TrafficMgmt_ObjectIdentity = ObjectIdentity
swL2TrafficMgmt = _SwL2TrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 13)
)
_SwL2TrafficCtrlTable_Object = MibTable
swL2TrafficCtrlTable = _SwL2TrafficCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    swL2TrafficCtrlTable.setStatus("current")
_SwL2TrafficCtrlEntry_Object = MibTableRow
swL2TrafficCtrlEntry = _SwL2TrafficCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 13, 1, 1)
)
swL2TrafficCtrlEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2TrafficCtrlGroupIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 13, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 13, 1, 1, 2),
    _SwL2TrafficCtrlUnitIndex_Type()
)
swL2TrafficCtrlUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficCtrlUnitIndex.setStatus("current")


class _SwL2TrafficCtrlBMStromthreshold_Type(Integer32):
    """Custom type swL2TrafficCtrlBMStromthreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwL2TrafficCtrlBMStromthreshold_Type.__name__ = "Integer32"
_SwL2TrafficCtrlBMStromthreshold_Object = MibTableColumn
swL2TrafficCtrlBMStromthreshold = _SwL2TrafficCtrlBMStromthreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 13, 1, 1, 3),
    _SwL2TrafficCtrlBMStromthreshold_Type()
)
swL2TrafficCtrlBMStromthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlBMStromthreshold.setStatus("current")


class _SwL2TrafficCtrlBcastStromCtrl_Type(Integer32):
    """Custom type swL2TrafficCtrlBcastStromCtrl based on Integer32"""
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


_SwL2TrafficCtrlBcastStromCtrl_Type.__name__ = "Integer32"
_SwL2TrafficCtrlBcastStromCtrl_Object = MibTableColumn
swL2TrafficCtrlBcastStromCtrl = _SwL2TrafficCtrlBcastStromCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 13, 1, 1, 4),
    _SwL2TrafficCtrlBcastStromCtrl_Type()
)
swL2TrafficCtrlBcastStromCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlBcastStromCtrl.setStatus("current")


class _SwL2TrafficCtrlMcastStromCtrl_Type(Integer32):
    """Custom type swL2TrafficCtrlMcastStromCtrl based on Integer32"""
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


_SwL2TrafficCtrlMcastStromCtrl_Type.__name__ = "Integer32"
_SwL2TrafficCtrlMcastStromCtrl_Object = MibTableColumn
swL2TrafficCtrlMcastStromCtrl = _SwL2TrafficCtrlMcastStromCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 13, 1, 1, 5),
    _SwL2TrafficCtrlMcastStromCtrl_Type()
)
swL2TrafficCtrlMcastStromCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlMcastStromCtrl.setStatus("current")


class _SwL2TrafficCtrlDlfStromCtrl_Type(Integer32):
    """Custom type swL2TrafficCtrlDlfStromCtrl based on Integer32"""
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


_SwL2TrafficCtrlDlfStromCtrl_Type.__name__ = "Integer32"
_SwL2TrafficCtrlDlfStromCtrl_Object = MibTableColumn
swL2TrafficCtrlDlfStromCtrl = _SwL2TrafficCtrlDlfStromCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 13, 1, 1, 6),
    _SwL2TrafficCtrlDlfStromCtrl_Type()
)
swL2TrafficCtrlDlfStromCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlDlfStromCtrl.setStatus("current")
_SwL2TrafficSegMgmt_ObjectIdentity = ObjectIdentity
swL2TrafficSegMgmt = _SwL2TrafficSegMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 14)
)
_SwL2TrafficSegTable_Object = MibTable
swL2TrafficSegTable = _SwL2TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 14, 1)
)
if mibBuilder.loadTexts:
    swL2TrafficSegTable.setStatus("current")
_SwL2TrafficSegEntry_Object = MibTableRow
swL2TrafficSegEntry = _SwL2TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 14, 1, 1)
)
swL2TrafficSegEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2TrafficSegPort"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 14, 1, 1, 1),
    _SwL2TrafficSegPort_Type()
)
swL2TrafficSegPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficSegPort.setStatus("current")
_SwL2TrafficSegForwardPorts_Type = PortList
_SwL2TrafficSegForwardPorts_Object = MibTableColumn
swL2TrafficSegForwardPorts = _SwL2TrafficSegForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 14, 1, 1, 2),
    _SwL2TrafficSegForwardPorts_Type()
)
swL2TrafficSegForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficSegForwardPorts.setStatus("current")
_SwL2StpMgmt_ObjectIdentity = ObjectIdentity
swL2StpMgmt = _SwL2StpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15)
)


class _SwL2StpForwardBPDU_Type(Integer32):
    """Custom type swL2StpForwardBPDU based on Integer32"""
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


_SwL2StpForwardBPDU_Type.__name__ = "Integer32"
_SwL2StpForwardBPDU_Object = MibScalar
swL2StpForwardBPDU = _SwL2StpForwardBPDU_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 1),
    _SwL2StpForwardBPDU_Type()
)
swL2StpForwardBPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpForwardBPDU.setStatus("current")


class _SwL2StpLbd_Type(Integer32):
    """Custom type swL2StpLbd based on Integer32"""
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


_SwL2StpLbd_Type.__name__ = "Integer32"
_SwL2StpLbd_Object = MibScalar
swL2StpLbd = _SwL2StpLbd_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 2),
    _SwL2StpLbd_Type()
)
swL2StpLbd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpLbd.setStatus("current")


class _SwL2StpLbdRecoverTime_Type(Integer32):
    """Custom type swL2StpLbdRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SwL2StpLbdRecoverTime_Type.__name__ = "Integer32"
_SwL2StpLbdRecoverTime_Object = MibScalar
swL2StpLbdRecoverTime = _SwL2StpLbdRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 3),
    _SwL2StpLbdRecoverTime_Type()
)
swL2StpLbdRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpLbdRecoverTime.setStatus("current")
_SwL2StpPortTable_Object = MibTable
swL2StpPortTable = _SwL2StpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4)
)
if mibBuilder.loadTexts:
    swL2StpPortTable.setStatus("current")
_SwL2StpPortEntry_Object = MibTableRow
swL2StpPortEntry = _SwL2StpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1)
)
swL2StpPortEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2StpPort"),
)
if mibBuilder.loadTexts:
    swL2StpPortEntry.setStatus("current")


class _SwL2StpPort_Type(Integer32):
    """Custom type swL2StpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2StpPort_Type.__name__ = "Integer32"
_SwL2StpPort_Object = MibTableColumn
swL2StpPort = _SwL2StpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 1),
    _SwL2StpPort_Type()
)
swL2StpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPort.setStatus("current")


class _SwL2StpPortLbd_Type(Integer32):
    """Custom type swL2StpPortLbd based on Integer32"""
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


_SwL2StpPortLbd_Type.__name__ = "Integer32"
_SwL2StpPortLbd_Object = MibTableColumn
swL2StpPortLbd = _SwL2StpPortLbd_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 2),
    _SwL2StpPortLbd_Type()
)
swL2StpPortLbd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortLbd.setStatus("current")


class _SwL2StpPortStatus_Type(Integer32):
    """Custom type swL2StpPortStatus based on Integer32"""
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
        *(("broken", 6),
          ("disabled", 2),
          ("discarding", 3),
          ("err-disabled", 8),
          ("forwarding", 5),
          ("learning", 4),
          ("no-stp-enabled", 7),
          ("other", 1))
    )


_SwL2StpPortStatus_Type.__name__ = "Integer32"
_SwL2StpPortStatus_Object = MibTableColumn
swL2StpPortStatus = _SwL2StpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 3),
    _SwL2StpPortStatus_Type()
)
swL2StpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPortStatus.setStatus("current")


class _SwL2StpPortRole_Type(Integer32):
    """Custom type swL2StpPortRole based on Integer32"""
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
        *(("alternate", 2),
          ("backup", 3),
          ("designated", 5),
          ("disabled", 1),
          ("loopback", 7),
          ("nonStp", 6),
          ("root", 4))
    )


_SwL2StpPortRole_Type.__name__ = "Integer32"
_SwL2StpPortRole_Object = MibTableColumn
swL2StpPortRole = _SwL2StpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 4),
    _SwL2StpPortRole_Type()
)
swL2StpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPortRole.setStatus("current")


class _SwL2StpPortFBPDU_Type(Integer32):
    """Custom type swL2StpPortFBPDU based on Integer32"""
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


_SwL2StpPortFBPDU_Type.__name__ = "Integer32"
_SwL2StpPortFBPDU_Object = MibTableColumn
swL2StpPortFBPDU = _SwL2StpPortFBPDU_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 5),
    _SwL2StpPortFBPDU_Type()
)
swL2StpPortFBPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortFBPDU.setStatus("current")


class _SwL2StpPortLinkState_Type(Integer32):
    """Custom type swL2StpPortLinkState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("full-1000Mbps-8023x", 13),
          ("full-1000Mbps-backp", 11),
          ("full-1000Mbps-none", 12),
          ("full-100Mbps-8023x", 9),
          ("full-100Mbps-none", 8),
          ("full-10Mbps-8023x", 5),
          ("full-10Mbps-none", 4),
          ("half-1000Mbps-none", 10),
          ("half-100Mbps-backp", 7),
          ("half-100Mbps-none", 6),
          ("half-10Mbps-backp", 3),
          ("half-10Mbps-none", 2),
          ("link-down", 1))
    )


_SwL2StpPortLinkState_Type.__name__ = "Integer32"
_SwL2StpPortLinkState_Object = MibTableColumn
swL2StpPortLinkState = _SwL2StpPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 6),
    _SwL2StpPortLinkState_Type()
)
swL2StpPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPortLinkState.setStatus("current")
_SwL2StpPortProtocolMigration_Type = TruthValue
_SwL2StpPortProtocolMigration_Object = MibTableColumn
swL2StpPortProtocolMigration = _SwL2StpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 7),
    _SwL2StpPortProtocolMigration_Type()
)
swL2StpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortProtocolMigration.setStatus("current")
_SwL2StpPortAdminEdgePort_Type = TruthValue
_SwL2StpPortAdminEdgePort_Object = MibTableColumn
swL2StpPortAdminEdgePort = _SwL2StpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 8),
    _SwL2StpPortAdminEdgePort_Type()
)
swL2StpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortAdminEdgePort.setStatus("current")
_SwL2StpPortOperEdgePort_Type = TruthValue
_SwL2StpPortOperEdgePort_Object = MibTableColumn
swL2StpPortOperEdgePort = _SwL2StpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 9),
    _SwL2StpPortOperEdgePort_Type()
)
swL2StpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPortOperEdgePort.setStatus("current")


class _SwL2StpPortAdminPointToPoint_Type(Integer32):
    """Custom type swL2StpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_SwL2StpPortAdminPointToPoint_Type.__name__ = "Integer32"
_SwL2StpPortAdminPointToPoint_Object = MibTableColumn
swL2StpPortAdminPointToPoint = _SwL2StpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 10),
    _SwL2StpPortAdminPointToPoint_Type()
)
swL2StpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortAdminPointToPoint.setStatus("current")
_SwL2StpPortOperPointToPoint_Type = TruthValue
_SwL2StpPortOperPointToPoint_Object = MibTableColumn
swL2StpPortOperPointToPoint = _SwL2StpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 11),
    _SwL2StpPortOperPointToPoint_Type()
)
swL2StpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPortOperPointToPoint.setStatus("current")


class _SwL2StpPortAdminPathCost_Type(Unsigned32):
    """Custom type swL2StpPortAdminPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_SwL2StpPortAdminPathCost_Type.__name__ = "Unsigned32"
_SwL2StpPortAdminPathCost_Object = MibTableColumn
swL2StpPortAdminPathCost = _SwL2StpPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 12),
    _SwL2StpPortAdminPathCost_Type()
)
swL2StpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortAdminPathCost.setStatus("current")


class _SwL2StpPortPriority_Type(Integer32):
    """Custom type swL2StpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SwL2StpPortPriority_Type.__name__ = "Integer32"
_SwL2StpPortPriority_Object = MibTableColumn
swL2StpPortPriority = _SwL2StpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 13),
    _SwL2StpPortPriority_Type()
)
swL2StpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortPriority.setStatus("current")


class _SwL2STPPortState_Type(Integer32):
    """Custom type swL2STPPortState based on Integer32"""
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


_SwL2STPPortState_Type.__name__ = "Integer32"
_SwL2STPPortState_Object = MibTableColumn
swL2STPPortState = _SwL2STPPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 15, 4, 1, 14),
    _SwL2STPPortState_Type()
)
swL2STPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2STPPortState.setStatus("current")
_SwL2MulticastFilterMode_ObjectIdentity = ObjectIdentity
swL2MulticastFilterMode = _SwL2MulticastFilterMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 17)
)
_SwL2MulticastFilterModeVlanTable_Object = MibTable
swL2MulticastFilterModeVlanTable = _SwL2MulticastFilterModeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    swL2MulticastFilterModeVlanTable.setStatus("current")
_SwL2MulticastFilterModeVlanEntry_Object = MibTableRow
swL2MulticastFilterModeVlanEntry = _SwL2MulticastFilterModeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 17, 1, 1)
)
swL2MulticastFilterModeVlanEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2MulticastFilterVid"),
)
if mibBuilder.loadTexts:
    swL2MulticastFilterModeVlanEntry.setStatus("current")


class _SwL2MulticastFilterVid_Type(Integer32):
    """Custom type swL2MulticastFilterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2MulticastFilterVid_Type.__name__ = "Integer32"
_SwL2MulticastFilterVid_Object = MibTableColumn
swL2MulticastFilterVid = _SwL2MulticastFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 17, 1, 1, 1),
    _SwL2MulticastFilterVid_Type()
)
swL2MulticastFilterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2MulticastFilterVid.setStatus("current")


class _SwL2MulticastFilterVlanMode_Type(Integer32):
    """Custom type swL2MulticastFilterVlanMode based on Integer32"""
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


_SwL2MulticastFilterVlanMode_Type.__name__ = "Integer32"
_SwL2MulticastFilterVlanMode_Object = MibTableColumn
swL2MulticastFilterVlanMode = _SwL2MulticastFilterVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 17, 1, 1, 2),
    _SwL2MulticastFilterVlanMode_Type()
)
swL2MulticastFilterVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MulticastFilterVlanMode.setStatus("current")
_SwL2MulticastFilterModePortTable_Object = MibTable
swL2MulticastFilterModePortTable = _SwL2MulticastFilterModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 17, 2)
)
if mibBuilder.loadTexts:
    swL2MulticastFilterModePortTable.setStatus("current")
_SwL2MulticastFilterModePortEntry_Object = MibTableRow
swL2MulticastFilterModePortEntry = _SwL2MulticastFilterModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 17, 2, 1)
)
swL2MulticastFilterModePortEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2MulticastFilterPortIndex"),
)
if mibBuilder.loadTexts:
    swL2MulticastFilterModePortEntry.setStatus("current")


class _SwL2MulticastFilterPortIndex_Type(Integer32):
    """Custom type swL2MulticastFilterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2MulticastFilterPortIndex_Type.__name__ = "Integer32"
_SwL2MulticastFilterPortIndex_Object = MibTableColumn
swL2MulticastFilterPortIndex = _SwL2MulticastFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 17, 2, 1, 1),
    _SwL2MulticastFilterPortIndex_Type()
)
swL2MulticastFilterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2MulticastFilterPortIndex.setStatus("current")


class _SwL2MulticastFilterPortMode_Type(Integer32):
    """Custom type swL2MulticastFilterPortMode based on Integer32"""
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


_SwL2MulticastFilterPortMode_Type.__name__ = "Integer32"
_SwL2MulticastFilterPortMode_Object = MibTableColumn
swL2MulticastFilterPortMode = _SwL2MulticastFilterPortMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 17, 2, 1, 2),
    _SwL2MulticastFilterPortMode_Type()
)
swL2MulticastFilterPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MulticastFilterPortMode.setStatus("current")
_SwL2LoopDetectMgmt_ObjectIdentity = ObjectIdentity
swL2LoopDetectMgmt = _SwL2LoopDetectMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18)
)
_SwL2LoopDetectCtrl_ObjectIdentity = ObjectIdentity
swL2LoopDetectCtrl = _SwL2LoopDetectCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 1, 5),
    _SwL2LoopDetectTrapMode_Type()
)
swL2LoopDetectTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectTrapMode.setStatus("current")
_SwL2LoopDetectPortMgmt_ObjectIdentity = ObjectIdentity
swL2LoopDetectPortMgmt = _SwL2LoopDetectPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 2)
)
_SwL2LoopDetectPortTable_Object = MibTable
swL2LoopDetectPortTable = _SwL2LoopDetectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    swL2LoopDetectPortTable.setStatus("current")
_SwL2LoopDetectPortEntry_Object = MibTableRow
swL2LoopDetectPortEntry = _SwL2LoopDetectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 2, 1, 1)
)
swL2LoopDetectPortEntry.setIndexNames(
    (0, "DES3200-52P-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 2, 1, 1, 2),
    _SwL2LoopDetectPortState_Type()
)
swL2LoopDetectPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectPortState.setStatus("current")
_SwL2LoopDetectPortLoopVLAN_Type = DisplayString
_SwL2LoopDetectPortLoopVLAN_Object = MibTableColumn
swL2LoopDetectPortLoopVLAN = _SwL2LoopDetectPortLoopVLAN_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 18, 2, 1, 1, 4),
    _SwL2LoopDetectPortLoopStatus_Type()
)
swL2LoopDetectPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LoopDetectPortLoopStatus.setStatus("current")
_SwL2MgmtMIBTraps_ObjectIdentity = ObjectIdentity
swL2MgmtMIBTraps = _SwL2MgmtMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100)
)
_SwL2Notify_ObjectIdentity = ObjectIdentity
swL2Notify = _SwL2Notify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1)
)
_SwL2NotifyMgmt_ObjectIdentity = ObjectIdentity
swL2NotifyMgmt = _SwL2NotifyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 1)
)
_SwL2macNotificationSeverity_Type = AgentNotifyLevel
_SwL2macNotificationSeverity_Object = MibScalar
swL2macNotificationSeverity = _SwL2macNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 1, 1),
    _SwL2macNotificationSeverity_Type()
)
swL2macNotificationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2macNotificationSeverity.setStatus("current")
_SwL2PortSecurityViolationSeverity_Type = AgentNotifyLevel
_SwL2PortSecurityViolationSeverity_Object = MibScalar
swL2PortSecurityViolationSeverity = _SwL2PortSecurityViolationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 1, 2),
    _SwL2PortSecurityViolationSeverity_Type()
)
swL2PortSecurityViolationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityViolationSeverity.setStatus("current")
_SwL2NotifyPrefix_ObjectIdentity = ObjectIdentity
swL2NotifyPrefix = _SwL2NotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2)
)
_SwL2NotifFirmware_ObjectIdentity = ObjectIdentity
swL2NotifFirmware = _SwL2NotifFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2, 0)
)
_Swl2NotificationBidings_ObjectIdentity = ObjectIdentity
swl2NotificationBidings = _Swl2NotificationBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2, 1, 1),
    _SwL2macNotifyInfo_Type()
)
swL2macNotifyInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2macNotifyInfo.setStatus("current")
_SwL2PortSecurityViolationMac_Type = MacAddress
_SwL2PortSecurityViolationMac_Object = MibScalar
swL2PortSecurityViolationMac = _SwL2PortSecurityViolationMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2, 1, 2),
    _SwL2PortSecurityViolationMac_Type()
)
swL2PortSecurityViolationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swL2PortSecurityViolationMac.setStatus("current")
_SwL2VlanLoopDetectVID_Type = Integer32
_SwL2VlanLoopDetectVID_Object = MibScalar
swL2VlanLoopDetectVID = _SwL2VlanLoopDetectVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2, 1, 3),
    _SwL2VlanLoopDetectVID_Type()
)
swL2VlanLoopDetectVID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swL2VlanLoopDetectVID.setStatus("current")

# Managed Objects groups


# Notification objects

swL2macNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2, 0, 1)
)
swL2macNotification.setObjects(
    ("DES3200-52P-L2MGMT-MIB", "swL2macNotifyInfo")
)
if mibBuilder.loadTexts:
    swL2macNotification.setStatus(
        "current"
    )

swL2PortSecurityViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2, 0, 2)
)
swL2PortSecurityViolationTrap.setObjects(
      *(("PORT-SECURITY-MIB", "swPortSecPortIndex"),
        ("DES3200-52P-L2MGMT-MIB", "swL2PortSecurityViolationMac"))
)
if mibBuilder.loadTexts:
    swL2PortSecurityViolationTrap.setStatus(
        "current"
    )

swL2PortLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2, 0, 3)
)
swL2PortLoopOccurred.setObjects(
    ("DES3200-52P-L2MGMT-MIB", "swL2LoopDetectPortIndex")
)
if mibBuilder.loadTexts:
    swL2PortLoopOccurred.setStatus(
        "current"
    )

swL2PortLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2, 0, 4)
)
swL2PortLoopRestart.setObjects(
    ("DES3200-52P-L2MGMT-MIB", "swL2LoopDetectPortIndex")
)
if mibBuilder.loadTexts:
    swL2PortLoopRestart.setStatus(
        "current"
    )

swL2VlanLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2, 0, 5)
)
swL2VlanLoopOccurred.setObjects(
      *(("DES3200-52P-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
        ("DES3200-52P-L2MGMT-MIB", "swL2VlanLoopDetectVID"))
)
if mibBuilder.loadTexts:
    swL2VlanLoopOccurred.setStatus(
        "current"
    )

swL2VlanLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 10, 1, 2, 100, 1, 2, 0, 6)
)
swL2VlanLoopRestart.setObjects(
      *(("DES3200-52P-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
        ("DES3200-52P-L2MGMT-MIB", "swL2VlanLoopDetectVID"))
)
if mibBuilder.loadTexts:
    swL2VlanLoopRestart.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES3200-52P-L2MGMT-MIB",
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
       "swDevModuleInfoModuleName": swDevModuleInfoModuleName,
       "swDevModuleInfoReversion": swDevModuleInfoReversion,
       "swDevModuleInfoSerial": swDevModuleInfoSerial,
       "swDevModuleInfoDescription": swDevModuleInfoDescription,
       "swDevInfoFrontPanelLedStatus": swDevInfoFrontPanelLedStatus,
       "swL2DevCtrl": swL2DevCtrl,
       "swL2DevCtrlStpState": swL2DevCtrlStpState,
       "swL2DevCtrlIGMPSnooping": swL2DevCtrlIGMPSnooping,
       "swL2DevCtrlIGMPSnoopingMcstRTOnly": swL2DevCtrlIGMPSnoopingMcstRTOnly,
       "swL2DevCtrlRmonState": swL2DevCtrlRmonState,
       "swL2DevCtrlSnmpTrapState": swL2DevCtrlSnmpTrapState,
       "swL2DevCtrlCleanAllStatisticCounter": swL2DevCtrlCleanAllStatisticCounter,
       "swL2DevCtrlVlanIdOfFDBTbl": swL2DevCtrlVlanIdOfFDBTbl,
       "swL2MACNotifyState": swL2MACNotifyState,
       "swL2MACNotifyHistorySize": swL2MACNotifyHistorySize,
       "swL2MACNotifyInterval": swL2MACNotifyInterval,
       "swL2DevCtrlAsymVlanState": swL2DevCtrlAsymVlanState,
       "swL2DevCtrlTelnet": swL2DevCtrlTelnet,
       "swL2DevCtrlTelnetState": swL2DevCtrlTelnetState,
       "swL2DevCtrlTelnetTcpPort": swL2DevCtrlTelnetTcpPort,
       "swL2DevCtrlManagementVlanId": swL2DevCtrlManagementVlanId,
       "swL2DevCtrlWeb": swL2DevCtrlWeb,
       "swL2DevCtrlWebState": swL2DevCtrlWebState,
       "swL2DevCtrlWebTcpPort": swL2DevCtrlWebTcpPort,
       "swL2DevCtrlLLDPState": swL2DevCtrlLLDPState,
       "swL2DevCtrlLLDPForwardMessageState": swL2DevCtrlLLDPForwardMessageState,
       "swL2DevCtrlIpAutoconfig": swL2DevCtrlIpAutoconfig,
       "swL2DevCtrlCFM": swL2DevCtrlCFM,
       "swL2DevCtrlCFMState": swL2DevCtrlCFMState,
       "swL2DevCtrlCFMPortTable": swL2DevCtrlCFMPortTable,
       "swL2DevCtrlCFMPortEntry": swL2DevCtrlCFMPortEntry,
       "swL2DevCtrlCFMPortIndex": swL2DevCtrlCFMPortIndex,
       "swL2DevCtrlCFMPortState": swL2DevCtrlCFMPortState,
       "swL2DevCtrlVLANTrunkState": swL2DevCtrlVLANTrunkState,
       "swL2DevAlarm": swL2DevAlarm,
       "swL2DevAlarmNewRoot": swL2DevAlarmNewRoot,
       "swL2DevAlarmTopologyChange": swL2DevAlarmTopologyChange,
       "swL2DevAlarmLinkChange": swL2DevAlarmLinkChange,
       "swL2VLANMgmt": swL2VLANMgmt,
       "swL2VlanStaticTable": swL2VlanStaticTable,
       "swL2VlanStaticEntry": swL2VlanStaticEntry,
       "swL2VlanIndex": swL2VlanIndex,
       "swL2VLANAdvertisement": swL2VLANAdvertisement,
       "swL2PVIDAutoAssignmentState": swL2PVIDAutoAssignmentState,
       "swL2VlanPortInfoTable": swL2VlanPortInfoTable,
       "swL2VlanPortInfoEntry": swL2VlanPortInfoEntry,
       "swL2VlanPortInfoPortIndex": swL2VlanPortInfoPortIndex,
       "swL2VlanPortInfoVid": swL2VlanPortInfoVid,
       "swL2VlanPortInfoPortRole": swL2VlanPortInfoPortRole,
       "swL2SubnetVLANTable": swL2SubnetVLANTable,
       "swL2SubnetVLANEntry": swL2SubnetVLANEntry,
       "swL2SubnetVLANIPAddress": swL2SubnetVLANIPAddress,
       "swL2SubnetVLANIPMask": swL2SubnetVLANIPMask,
       "swL2SubnetVLANID": swL2SubnetVLANID,
       "swL2SubnetVLANPriority": swL2SubnetVLANPriority,
       "swL2SubnetVLANRowStatus": swL2SubnetVLANRowStatus,
       "swL2VlanPrecedenceTable": swL2VlanPrecedenceTable,
       "swL2VlanPrecedenceEntry": swL2VlanPrecedenceEntry,
       "swL2VlanPrecedencePortIndex": swL2VlanPrecedencePortIndex,
       "swL2VlanPrecedenceClassification": swL2VlanPrecedenceClassification,
       "swL2NniGvrpBpduAddress": swL2NniGvrpBpduAddress,
       "swL2PortMgmt": swL2PortMgmt,
       "swL2PortInfoTable": swL2PortInfoTable,
       "swL2PortInfoEntry": swL2PortInfoEntry,
       "swL2PortInfoPortIndex": swL2PortInfoPortIndex,
       "swL2PortInfoMediumType": swL2PortInfoMediumType,
       "swL2PortInfoUnitID": swL2PortInfoUnitID,
       "swL2PortInfoType": swL2PortInfoType,
       "swL2PortInfoLinkStatus": swL2PortInfoLinkStatus,
       "swL2PortInfoNwayStatus": swL2PortInfoNwayStatus,
       "swL2PortInfoModuleType": swL2PortInfoModuleType,
       "swL2PortInfoErrorDisabled": swL2PortInfoErrorDisabled,
       "swL2PortCtrlTable": swL2PortCtrlTable,
       "swL2PortCtrlEntry": swL2PortCtrlEntry,
       "swL2PortCtrlPortIndex": swL2PortCtrlPortIndex,
       "swL2PortCtrlMediumType": swL2PortCtrlMediumType,
       "swL2PortCtrlUnitIndex": swL2PortCtrlUnitIndex,
       "swL2PortCtrlAdminState": swL2PortCtrlAdminState,
       "swL2PortCtrlNwayState": swL2PortCtrlNwayState,
       "swL2PortCtrlFlowCtrlState": swL2PortCtrlFlowCtrlState,
       "swL2PortCtrlLearningState": swL2PortCtrlLearningState,
       "swL2PortCtrlMACNotifyState": swL2PortCtrlMACNotifyState,
       "swL2PortCtrlMDIXState": swL2PortCtrlMDIXState,
       "swL2PortCtrlAutoNegRestart": swL2PortCtrlAutoNegRestart,
       "swL2PortCtrlAutoNegCapAdvertisedBits": swL2PortCtrlAutoNegCapAdvertisedBits,
       "swL2PortCtrlJumboFrame": swL2PortCtrlJumboFrame,
       "swL2PortCtrlJumboFrameMaxSize": swL2PortCtrlJumboFrameMaxSize,
       "swL2PortCableDiagnosisTable": swL2PortCableDiagnosisTable,
       "swL2PortCableDiagnosisEntry": swL2PortCableDiagnosisEntry,
       "swL2PortCableDiagnosisPortIndex": swL2PortCableDiagnosisPortIndex,
       "swL2PortCableDiagnosisPairIndex": swL2PortCableDiagnosisPairIndex,
       "swL2PortCableDiagnosisCableStatus": swL2PortCableDiagnosisCableStatus,
       "swL2PortCableDiagnosisPairStatus": swL2PortCableDiagnosisPairStatus,
       "swL2PortCableDiagnosisPairLength": swL2PortCableDiagnosisPairLength,
       "swL2PortCableDiagnosisPairLengthInaccuracy": swL2PortCableDiagnosisPairLengthInaccuracy,
       "swL2PortCounterCtrlTable": swL2PortCounterCtrlTable,
       "swL2PortCounterCtrlEntry": swL2PortCounterCtrlEntry,
       "swL2PortCounterCtrlPortIndex": swL2PortCounterCtrlPortIndex,
       "swL2PortCounterClearCtrl": swL2PortCounterClearCtrl,
       "swL2PortErrTable": swL2PortErrTable,
       "swL2PortErrEntry": swL2PortErrEntry,
       "swL2PortErrPortIndex": swL2PortErrPortIndex,
       "swL2PortErrPortState": swL2PortErrPortState,
       "swL2PortErrPortConnStatus": swL2PortErrPortConnStatus,
       "swL2PortErrPortReason": swL2PortErrPortReason,
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
       "swL2PortJumboFrameCtrlTable": swL2PortJumboFrameCtrlTable,
       "swL2PortJumboFrameCtrlEntry": swL2PortJumboFrameCtrlEntry,
       "swL2PortJumboFrameCtrlPortIndex": swL2PortJumboFrameCtrlPortIndex,
       "swL2PortJumboFrameCtrlState": swL2PortJumboFrameCtrlState,
       "swL2DiffServMgmt": swL2DiffServMgmt,
       "swL2DiffServTypeCtrlTable": swL2DiffServTypeCtrlTable,
       "swL2DiffServTypeCtrlEntry": swL2DiffServTypeCtrlEntry,
       "swL2DiffServTypeCtrlPortIndex": swL2DiffServTypeCtrlPortIndex,
       "swL2DiffServTypeCtrlDiffServType": swL2DiffServTypeCtrlDiffServType,
       "swL2DiffServDSCPCtrlTable": swL2DiffServDSCPCtrlTable,
       "swL2DiffServDSCPCtrlEntry": swL2DiffServDSCPCtrlEntry,
       "swL2DiffServDSCPCtrlPortIndex": swL2DiffServDSCPCtrlPortIndex,
       "swL2DiffServDSCPCtrlMode": swL2DiffServDSCPCtrlMode,
       "swL2DiffServDSCPCtrlValue": swL2DiffServDSCPCtrlValue,
       "swL2DiffServTOSCtrlTable": swL2DiffServTOSCtrlTable,
       "swL2DiffServTOSCtrlEntry": swL2DiffServTOSCtrlEntry,
       "swL2DiffServTOSCtrlPortIndex": swL2DiffServTOSCtrlPortIndex,
       "swL2DiffServTOSCtrlMode": swL2DiffServTOSCtrlMode,
       "swL2DiffServTOSCtrlValue": swL2DiffServTOSCtrlValue,
       "swL2LimitedMulticastMgmt": swL2LimitedMulticastMgmt,
       "swL2MulticastFilterProfileTable": swL2MulticastFilterProfileTable,
       "swL2MulticastFilterProfileEntry": swL2MulticastFilterProfileEntry,
       "swL2MulticastFilterProfileIndex": swL2MulticastFilterProfileIndex,
       "swL2MulticastFilterProfileName": swL2MulticastFilterProfileName,
       "swL2MulticastFilterStatus": swL2MulticastFilterStatus,
       "swL2MulticastFilterProfileAddressTable": swL2MulticastFilterProfileAddressTable,
       "swL2MulticastFilterProfileAddressEntry": swL2MulticastFilterProfileAddressEntry,
       "swL2MulticastFilterProfileIdIndex": swL2MulticastFilterProfileIdIndex,
       "swL2MulticastFilterFromIp": swL2MulticastFilterFromIp,
       "swL2MulticastFilterToIp": swL2MulticastFilterToIp,
       "swL2MulticastFilterAddressState": swL2MulticastFilterAddressState,
       "swL2LimitedMulticastFilterPortTable": swL2LimitedMulticastFilterPortTable,
       "swL2LimitedMulticastFilterPortEntry": swL2LimitedMulticastFilterPortEntry,
       "swL2LimitedMulticastFilterPortIndex": swL2LimitedMulticastFilterPortIndex,
       "swL2LimitedMulticastFilterPortAccess": swL2LimitedMulticastFilterPortAccess,
       "swL2LimitedMulticastFilterPortProfileID": swL2LimitedMulticastFilterPortProfileID,
       "swL2LimitedMulticastFilterPortProfileStatus": swL2LimitedMulticastFilterPortProfileStatus,
       "swL2MulticastFilterPortMaxGroupTable": swL2MulticastFilterPortMaxGroupTable,
       "swL2MulticastFilterPortMaxGroupEntry": swL2MulticastFilterPortMaxGroupEntry,
       "swL2MulticastFilterPortMaxGroupPortIndex": swL2MulticastFilterPortMaxGroupPortIndex,
       "swL2MulticastFilterPortMaxGroup": swL2MulticastFilterPortMaxGroup,
       "swL2LimitedMulticastFilterVIDTable": swL2LimitedMulticastFilterVIDTable,
       "swL2LimitedMulticastFilterVIDEntry": swL2LimitedMulticastFilterVIDEntry,
       "swL2LimitedMulticastFilterVIDIndex": swL2LimitedMulticastFilterVIDIndex,
       "swL2LimitedMulticastFilterVIDAccess": swL2LimitedMulticastFilterVIDAccess,
       "swL2LimitedMulticastFilterVIDProfileID": swL2LimitedMulticastFilterVIDProfileID,
       "swL2LimitedMulticastFilterVIDProfileStatus": swL2LimitedMulticastFilterVIDProfileStatus,
       "swL2MulticastFilterVIDMaxGroupTable": swL2MulticastFilterVIDMaxGroupTable,
       "swL2MulticastFilterVIDMaxGroupEntry": swL2MulticastFilterVIDMaxGroupEntry,
       "swL2MulticastFilterVIDMaxGroupVIDIndex": swL2MulticastFilterVIDMaxGroupVIDIndex,
       "swL2MulticastFilterVIDMaxGroup": swL2MulticastFilterVIDMaxGroup,
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
       "swL2QOSSchedulingMaxLatency": swL2QOSSchedulingMaxLatency,
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
       "swL2PortSecurityEntryClearCtrl": swL2PortSecurityEntryClearCtrl,
       "swL2PortSecurityDelCtrl": swL2PortSecurityDelCtrl,
       "swL2PortSecurityDelVlanName": swL2PortSecurityDelVlanName,
       "swL2PortSecurityDelPort": swL2PortSecurityDelPort,
       "swL2PortSecurityDelMacAddress": swL2PortSecurityDelMacAddress,
       "swL2PortSecurityDelActivity": swL2PortSecurityDelActivity,
       "swL2PortSecurityTrapLogState": swL2PortSecurityTrapLogState,
       "swL2DhcpRelayMgmt": swL2DhcpRelayMgmt,
       "swL2DhcpRelayState": swL2DhcpRelayState,
       "swL2DhcpRelayHopCount": swL2DhcpRelayHopCount,
       "swL2DhcpRelayTimeThreshold": swL2DhcpRelayTimeThreshold,
       "swL2DhcpRelayOption82State": swL2DhcpRelayOption82State,
       "swL2DhcpRelayOption82Check": swL2DhcpRelayOption82Check,
       "swL2DhcpRelayOption82Policy": swL2DhcpRelayOption82Policy,
       "swL2DhcpRelayCtrlTable": swL2DhcpRelayCtrlTable,
       "swL2DhcpRelayCtrlEntry": swL2DhcpRelayCtrlEntry,
       "swL2DhcpRelayCtrlInterfaceName": swL2DhcpRelayCtrlInterfaceName,
       "swL2DhcpRelayCtrlServer": swL2DhcpRelayCtrlServer,
       "swL2DhcpRelayCtrlState": swL2DhcpRelayCtrlState,
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
       "swL2TrunkLACPPortTable": swL2TrunkLACPPortTable,
       "swL2TrunkLACPPortEntry": swL2TrunkLACPPortEntry,
       "swL2TrunkLACPPortIndex": swL2TrunkLACPPortIndex,
       "swL2TrunkLACPPortState": swL2TrunkLACPPortState,
       "swL2TrunkVLANTable": swL2TrunkVLANTable,
       "swL2TrunkVLANEntry": swL2TrunkVLANEntry,
       "swL2TrunkVLANPort": swL2TrunkVLANPort,
       "swL2TrunkVLANState": swL2TrunkVLANState,
       "swL2MirrorMgmt": swL2MirrorMgmt,
       "swL2MirrorLogicTargetPort": swL2MirrorLogicTargetPort,
       "swL2MirrorPortSourceIngress": swL2MirrorPortSourceIngress,
       "swL2MirrorPortSourceEgress": swL2MirrorPortSourceEgress,
       "swL2MirrorPortState": swL2MirrorPortState,
       "swL2MirrorGroupTable": swL2MirrorGroupTable,
       "swL2MirrorGroupEntry": swL2MirrorGroupEntry,
       "swL2MirrorGroupID": swL2MirrorGroupID,
       "swL2MirrorGroupRowStatus": swL2MirrorGroupRowStatus,
       "swL2MirrorGroupState": swL2MirrorGroupState,
       "swL2MirrorGroupTargetPort": swL2MirrorGroupTargetPort,
       "swL2MirrorGroupSourceIngress": swL2MirrorGroupSourceIngress,
       "swL2MirrorGroupSourceEngress": swL2MirrorGroupSourceEngress,
       "swL2IGMPMgmt": swL2IGMPMgmt,
       "swL2IGMPMaxSupportedVlans": swL2IGMPMaxSupportedVlans,
       "swL2IGMPMaxIpGroupNumPerVlan": swL2IGMPMaxIpGroupNumPerVlan,
       "swL2IGMPSnoopingMulticastVlanState": swL2IGMPSnoopingMulticastVlanState,
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
       "swL2IGMPRateLimit": swL2IGMPRateLimit,
       "swL2IGMPReportSuppression": swL2IGMPReportSuppression,
       "swL2IGMPQueryInfoTable": swL2IGMPQueryInfoTable,
       "swL2IGMPQueryInfoEntry": swL2IGMPQueryInfoEntry,
       "swL2IGMPInfoVid": swL2IGMPInfoVid,
       "swL2IGMPInfoQueryCount": swL2IGMPInfoQueryCount,
       "swL2IGMPInfoTxQueryCount": swL2IGMPInfoTxQueryCount,
       "swL2IGMPQueryIPAddress": swL2IGMPQueryIPAddress,
       "swL2IGMPQueryExpiryTime": swL2IGMPQueryExpiryTime,
       "swL2IGMPInfoTable": swL2IGMPInfoTable,
       "swL2IGMPInfoEntry": swL2IGMPInfoEntry,
       "swL2IGMPVid": swL2IGMPVid,
       "swL2IGMPGroupIpAddr": swL2IGMPGroupIpAddr,
       "swL2IGMPMacAddr": swL2IGMPMacAddr,
       "swL2IGMPPortMap": swL2IGMPPortMap,
       "swL2IGMPIpGroupReportCount": swL2IGMPIpGroupReportCount,
       "swL2IGMPVersion": swL2IGMPVersion,
       "swL2IGMPGroupMode": swL2IGMPGroupMode,
       "swL2IGMPRouterPortTable": swL2IGMPRouterPortTable,
       "swL2IGMPRouterPortEntry": swL2IGMPRouterPortEntry,
       "swL2IGMPRouterPortVlanid": swL2IGMPRouterPortVlanid,
       "swL2IGMPRouterPortVlanName": swL2IGMPRouterPortVlanName,
       "swL2IGMPRouterPortStaticPortList": swL2IGMPRouterPortStaticPortList,
       "swL2IGMPRouterPortDynamicPortList": swL2IGMPRouterPortDynamicPortList,
       "swL2IGMPRouterPortForbiddenPortList": swL2IGMPRouterPortForbiddenPortList,
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
       "swL2IGMPMulticastVlanUntagSourcePort": swL2IGMPMulticastVlanUntagSourcePort,
       "swL2IGMPMulticastVlanRemapPriority": swL2IGMPMulticastVlanRemapPriority,
       "swL2IGMPMulticastVlanReplacePriority": swL2IGMPMulticastVlanReplacePriority,
       "swL2IGMPMulticastVlanGroupTable": swL2IGMPMulticastVlanGroupTable,
       "swL2IGMPMulticastVlanGroupEntry": swL2IGMPMulticastVlanGroupEntry,
       "swL2IGMPMulticastVlanGroupVid": swL2IGMPMulticastVlanGroupVid,
       "swL2IGMPMulticastVlanGroupFromIp": swL2IGMPMulticastVlanGroupFromIp,
       "swL2IGMPMulticastVlanGroupToIp": swL2IGMPMulticastVlanGroupToIp,
       "swL2IGMPMulticastVlanGroupStatus": swL2IGMPMulticastVlanGroupStatus,
       "swL2IGMPv3Table": swL2IGMPv3Table,
       "swL2IGMPv3Entry": swL2IGMPv3Entry,
       "swL2IGMPv3SourceIPAddr": swL2IGMPv3SourceIPAddr,
       "swL2IGMPv3Forwarding": swL2IGMPv3Forwarding,
       "swL2IGMPv3ExpireTimer": swL2IGMPv3ExpireTimer,
       "swIGMPSnoopingGroupTable": swIGMPSnoopingGroupTable,
       "swIGMPSnoopingGroupEntry": swIGMPSnoopingGroupEntry,
       "swIGMPSnoopingGroupVid": swIGMPSnoopingGroupVid,
       "swIGMPSnoopingGroupGroupAddr": swIGMPSnoopingGroupGroupAddr,
       "swIGMPSnoopingGroupSourceAddr": swIGMPSnoopingGroupSourceAddr,
       "swIGMPSnoopingGroupIncludePortMap": swIGMPSnoopingGroupIncludePortMap,
       "swIGMPSnoopingGroupExcludePortMap": swIGMPSnoopingGroupExcludePortMap,
       "swIGMPSnoopingGroupReportCount": swIGMPSnoopingGroupReportCount,
       "swIGMPSnoopingGroupUpTime": swIGMPSnoopingGroupUpTime,
       "swIGMPSnoopingGroupExpiryTime": swIGMPSnoopingGroupExpiryTime,
       "swIGMPSnoopingGroupRouterPorts": swIGMPSnoopingGroupRouterPorts,
       "swIGMPSnoopingGroupStaticMemberPorts": swIGMPSnoopingGroupStaticMemberPorts,
       "swL2IGMPDynIpMultMgmt": swL2IGMPDynIpMultMgmt,
       "swL2IGMPDynIPMultMaxEntry": swL2IGMPDynIPMultMaxEntry,
       "swL2IGMPSnoopingClearDynIpMult": swL2IGMPSnoopingClearDynIpMult,
       "swL2IGMPSnoopingClearDynIpMultVID": swL2IGMPSnoopingClearDynIpMultVID,
       "swL2IGMPSnoopingClearDynIpMultIP": swL2IGMPSnoopingClearDynIpMultIP,
       "swL2IGMPSnoopingClearDynIpMultAction": swL2IGMPSnoopingClearDynIpMultAction,
       "swL2IGMPDynIPMultCtrlTable": swL2IGMPDynIPMultCtrlTable,
       "swL2IGMPDynIPMultCtrlEntry": swL2IGMPDynIPMultCtrlEntry,
       "swL2IGMPDynIPMultVlanState": swL2IGMPDynIPMultVlanState,
       "swL2IGMPDynIPMultVlanAge": swL2IGMPDynIPMultVlanAge,
       "swL2IGMPDynIPMultGroupExpiryTime": swL2IGMPDynIPMultGroupExpiryTime,
       "swL2IGMPAccessAuthTable": swL2IGMPAccessAuthTable,
       "swL2IGMPAccessAuthEntry": swL2IGMPAccessAuthEntry,
       "swL2IGMPAccessAuthPort": swL2IGMPAccessAuthPort,
       "swL2IGMPAccessAuthState": swL2IGMPAccessAuthState,
       "swL2IGMPCountrInfoMgmt": swL2IGMPCountrInfoMgmt,
       "swL2IGMPSnoopingClearStatisticsCounter": swL2IGMPSnoopingClearStatisticsCounter,
       "swL2IGMPVlanCounterInfoTable": swL2IGMPVlanCounterInfoTable,
       "swL2IGMPVlanCounterInfoEntry": swL2IGMPVlanCounterInfoEntry,
       "swL2IGMPVlanCounterInfoVid": swL2IGMPVlanCounterInfoVid,
       "swL2IGMPVlanCounterGroupNumber": swL2IGMPVlanCounterGroupNumber,
       "swL2IGMPVlanQueryCountV1": swL2IGMPVlanQueryCountV1,
       "swL2IGMPVlanQueryCountV2": swL2IGMPVlanQueryCountV2,
       "swL2IGMPVlanQueryCountV3": swL2IGMPVlanQueryCountV3,
       "swL2IGMPVlanDropQueryCount": swL2IGMPVlanDropQueryCount,
       "swL2IGMPVlanReportCountV1": swL2IGMPVlanReportCountV1,
       "swL2IGMPVlanReportCountV2": swL2IGMPVlanReportCountV2,
       "swL2IGMPVlanReportCountV3": swL2IGMPVlanReportCountV3,
       "swL2IGMPVlanLeaveCountV2": swL2IGMPVlanLeaveCountV2,
       "swL2IGMPVlanDropedReportAndLeaveCount": swL2IGMPVlanDropedReportAndLeaveCount,
       "swL2IGMPVlanDroppedByMaxGroupLimitation": swL2IGMPVlanDroppedByMaxGroupLimitation,
       "swL2IGMPVlanDroppedByGroupFilter": swL2IGMPVlanDroppedByGroupFilter,
       "swL2IGMPVlanTxQueryCountV1": swL2IGMPVlanTxQueryCountV1,
       "swL2IGMPVlanTxQueryCountV2": swL2IGMPVlanTxQueryCountV2,
       "swL2IGMPVlanTxQueryCountV3": swL2IGMPVlanTxQueryCountV3,
       "swL2IGMPVlanTxReportCountV1": swL2IGMPVlanTxReportCountV1,
       "swL2IGMPVlanTxReportCountV2": swL2IGMPVlanTxReportCountV2,
       "swL2IGMPVlanTxReportCountV3": swL2IGMPVlanTxReportCountV3,
       "swL2IGMPVlanTxLeaveCountV2": swL2IGMPVlanTxLeaveCountV2,
       "swL2IGMPPortCounterInfoTable": swL2IGMPPortCounterInfoTable,
       "swL2IGMPPortCounterInfoEntry": swL2IGMPPortCounterInfoEntry,
       "swL2IGMPPortCounterInfoIndex": swL2IGMPPortCounterInfoIndex,
       "swL2IGMPPortCounterGroupNumber": swL2IGMPPortCounterGroupNumber,
       "swL2IGMPPortQueryCountV1": swL2IGMPPortQueryCountV1,
       "swL2IGMPPortQueryCountV2": swL2IGMPPortQueryCountV2,
       "swL2IGMPPortQueryCountV3": swL2IGMPPortQueryCountV3,
       "swL2IGMPPortDropQueryCount": swL2IGMPPortDropQueryCount,
       "swL2IGMPPortReportCountV1": swL2IGMPPortReportCountV1,
       "swL2IGMPPortReportCountV2": swL2IGMPPortReportCountV2,
       "swL2IGMPPortReportCountV3": swL2IGMPPortReportCountV3,
       "swL2IGMPPortLeaveCountV2": swL2IGMPPortLeaveCountV2,
       "swL2IGMPPortDropedReportAndLeaveCount": swL2IGMPPortDropedReportAndLeaveCount,
       "swL2IGMPPortDroppedByMaxGroupLimitation": swL2IGMPPortDroppedByMaxGroupLimitation,
       "swL2IGMPPortDroppedByGroupFilter": swL2IGMPPortDroppedByGroupFilter,
       "swL2IGMPPortTxQueryCountV1": swL2IGMPPortTxQueryCountV1,
       "swL2IGMPPortTxQueryCountV2": swL2IGMPPortTxQueryCountV2,
       "swL2IGMPPortTxQueryCountV3": swL2IGMPPortTxQueryCountV3,
       "swL2IGMPPortTxReportCountV1": swL2IGMPPortTxReportCountV1,
       "swL2IGMPPortTxReportCountV2": swL2IGMPPortTxReportCountV2,
       "swL2IGMPPortTxReportCountV3": swL2IGMPPortTxReportCountV3,
       "swL2IGMPPortTxLeaveCountV2": swL2IGMPPortTxLeaveCountV2,
       "swL2IGMPRouterIPAddressTable": swL2IGMPRouterIPAddressTable,
       "swL2IGMPRouterIPAddressEntry": swL2IGMPRouterIPAddressEntry,
       "swL2IGMPRouterIPAddressVid": swL2IGMPRouterIPAddressVid,
       "swL2IGMPRouterIPAddress": swL2IGMPRouterIPAddress,
       "swL2IGMPSnoopingStaticGroupTable": swL2IGMPSnoopingStaticGroupTable,
       "swL2IGMPSnoopingStaticGroupEntry": swL2IGMPSnoopingStaticGroupEntry,
       "swL2IGMPSnoopingStaticGroupVID": swL2IGMPSnoopingStaticGroupVID,
       "swL2IGMPSnoopingStaticGroupIPaddress": swL2IGMPSnoopingStaticGroupIPaddress,
       "swL2IGMPSnoopingStaticGroupMemberPortList": swL2IGMPSnoopingStaticGroupMemberPortList,
       "swL2IGMPSnoopingStaticGroupRowStatus": swL2IGMPSnoopingStaticGroupRowStatus,
       "swL2TrafficMgmt": swL2TrafficMgmt,
       "swL2TrafficCtrlTable": swL2TrafficCtrlTable,
       "swL2TrafficCtrlEntry": swL2TrafficCtrlEntry,
       "swL2TrafficCtrlGroupIndex": swL2TrafficCtrlGroupIndex,
       "swL2TrafficCtrlUnitIndex": swL2TrafficCtrlUnitIndex,
       "swL2TrafficCtrlBMStromthreshold": swL2TrafficCtrlBMStromthreshold,
       "swL2TrafficCtrlBcastStromCtrl": swL2TrafficCtrlBcastStromCtrl,
       "swL2TrafficCtrlMcastStromCtrl": swL2TrafficCtrlMcastStromCtrl,
       "swL2TrafficCtrlDlfStromCtrl": swL2TrafficCtrlDlfStromCtrl,
       "swL2TrafficSegMgmt": swL2TrafficSegMgmt,
       "swL2TrafficSegTable": swL2TrafficSegTable,
       "swL2TrafficSegEntry": swL2TrafficSegEntry,
       "swL2TrafficSegPort": swL2TrafficSegPort,
       "swL2TrafficSegForwardPorts": swL2TrafficSegForwardPorts,
       "swL2StpMgmt": swL2StpMgmt,
       "swL2StpForwardBPDU": swL2StpForwardBPDU,
       "swL2StpLbd": swL2StpLbd,
       "swL2StpLbdRecoverTime": swL2StpLbdRecoverTime,
       "swL2StpPortTable": swL2StpPortTable,
       "swL2StpPortEntry": swL2StpPortEntry,
       "swL2StpPort": swL2StpPort,
       "swL2StpPortLbd": swL2StpPortLbd,
       "swL2StpPortStatus": swL2StpPortStatus,
       "swL2StpPortRole": swL2StpPortRole,
       "swL2StpPortFBPDU": swL2StpPortFBPDU,
       "swL2StpPortLinkState": swL2StpPortLinkState,
       "swL2StpPortProtocolMigration": swL2StpPortProtocolMigration,
       "swL2StpPortAdminEdgePort": swL2StpPortAdminEdgePort,
       "swL2StpPortOperEdgePort": swL2StpPortOperEdgePort,
       "swL2StpPortAdminPointToPoint": swL2StpPortAdminPointToPoint,
       "swL2StpPortOperPointToPoint": swL2StpPortOperPointToPoint,
       "swL2StpPortAdminPathCost": swL2StpPortAdminPathCost,
       "swL2StpPortPriority": swL2StpPortPriority,
       "swL2STPPortState": swL2STPPortState,
       "swL2MulticastFilterMode": swL2MulticastFilterMode,
       "swL2MulticastFilterModeVlanTable": swL2MulticastFilterModeVlanTable,
       "swL2MulticastFilterModeVlanEntry": swL2MulticastFilterModeVlanEntry,
       "swL2MulticastFilterVid": swL2MulticastFilterVid,
       "swL2MulticastFilterVlanMode": swL2MulticastFilterVlanMode,
       "swL2MulticastFilterModePortTable": swL2MulticastFilterModePortTable,
       "swL2MulticastFilterModePortEntry": swL2MulticastFilterModePortEntry,
       "swL2MulticastFilterPortIndex": swL2MulticastFilterPortIndex,
       "swL2MulticastFilterPortMode": swL2MulticastFilterPortMode,
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
       "swL2LoopDetectPortLoopStatus": swL2LoopDetectPortLoopStatus,
       "swL2MgmtMIBTraps": swL2MgmtMIBTraps,
       "swL2Notify": swL2Notify,
       "swL2NotifyMgmt": swL2NotifyMgmt,
       "swL2macNotificationSeverity": swL2macNotificationSeverity,
       "swL2PortSecurityViolationSeverity": swL2PortSecurityViolationSeverity,
       "swL2NotifyPrefix": swL2NotifyPrefix,
       "swL2NotifFirmware": swL2NotifFirmware,
       "swL2macNotification": swL2macNotification,
       "swL2PortSecurityViolationTrap": swL2PortSecurityViolationTrap,
       "swL2PortLoopOccurred": swL2PortLoopOccurred,
       "swL2PortLoopRestart": swL2PortLoopRestart,
       "swL2VlanLoopOccurred": swL2VlanLoopOccurred,
       "swL2VlanLoopRestart": swL2VlanLoopRestart,
       "swl2NotificationBidings": swl2NotificationBidings,
       "swL2macNotifyInfo": swL2macNotifyInfo,
       "swL2PortSecurityViolationMac": swL2PortSecurityViolationMac,
       "swL2VlanLoopDetectVID": swL2VlanLoopDetectVID}
)

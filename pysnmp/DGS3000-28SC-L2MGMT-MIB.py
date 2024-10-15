# SNMP MIB module (DGS3000-28SC-L2MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS3000-28SC-L2MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:18 2024
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

(dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepIdentifier")

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

(dlink_Dgs3000Proj_DGS3000_28SCax,) = mibBuilder.importSymbols(
    "SWDGS3000PRIMGMT-MIB",
    "dlink-Dgs3000Proj-DGS3000-28SCax")


# MODULE-IDENTITY

swL2MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1)
)
_SwL2DevInfo_ObjectIdentity = ObjectIdentity
swL2DevInfo = _SwL2DevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 1, 2),
    _SwDevInfoNumOfPortInUse_Type()
)
swDevInfoNumOfPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoNumOfPortInUse.setStatus("current")
_SwDevModuleInfoTable_Object = MibTable
swDevModuleInfoTable = _SwDevModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    swDevModuleInfoTable.setStatus("current")
_SwDevModuleInfoEntry_Object = MibTableRow
swDevModuleInfoEntry = _SwDevModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 1, 3, 1)
)
swDevModuleInfoEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swDevModuleInfoUnitID"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 1, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 1, 3, 1, 6),
    _SwDevModuleInfoDescription_Type()
)
swDevModuleInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevModuleInfoDescription.setStatus("current")
_SwL2DevCtrl_ObjectIdentity = ObjectIdentity
swL2DevCtrl = _SwL2DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 6),
    _SwL2DevCtrlCleanAllStatisticCounter_Type()
)
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCleanAllStatisticCounter.setStatus("current")
_SwL2DevCtrlVlanIdOfFDBTbl_Type = VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object = MibScalar
swL2DevCtrlVlanIdOfFDBTbl = _SwL2DevCtrlVlanIdOfFDBTbl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 13),
    _SwL2DevCtrlAsymVlanState_Type()
)
swL2DevCtrlAsymVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlAsymVlanState.setStatus("current")
_SwL2DevCtrlTelnet_ObjectIdentity = ObjectIdentity
swL2DevCtrlTelnet = _SwL2DevCtrlTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 14)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 14, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 14, 2),
    _SwL2DevCtrlTelnetTcpPort_Type()
)
swL2DevCtrlTelnetTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlTelnetTcpPort.setStatus("current")
_SwL2DevCtrlManagementVlanId_Type = VlanId
_SwL2DevCtrlManagementVlanId_Object = MibScalar
swL2DevCtrlManagementVlanId = _SwL2DevCtrlManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 16),
    _SwL2DevCtrlManagementVlanId_Type()
)
swL2DevCtrlManagementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlManagementVlanId.setStatus("current")
_SwL2DevCtrlWeb_ObjectIdentity = ObjectIdentity
swL2DevCtrlWeb = _SwL2DevCtrlWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 17)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 17, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 17, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 20),
    _SwL2DevCtrlIpAutoconfig_Type()
)
swL2DevCtrlIpAutoconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIpAutoconfig.setStatus("current")
_SwL2DevCtrlCFM_ObjectIdentity = ObjectIdentity
swL2DevCtrlCFM = _SwL2DevCtrlCFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21, 1),
    _SwL2DevCtrlCFMState_Type()
)
swL2DevCtrlCFMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMState.setStatus("current")
_SwL2DevCtrlCFMPortTable_Object = MibTable
swL2DevCtrlCFMPortTable = _SwL2DevCtrlCFMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21, 2)
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortTable.setStatus("current")
_SwL2DevCtrlCFMPortEntry_Object = MibTableRow
swL2DevCtrlCFMPortEntry = _SwL2DevCtrlCFMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21, 2, 1)
)
swL2DevCtrlCFMPortEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2DevCtrlCFMPortIndex"),
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortEntry.setStatus("current")
_SwL2DevCtrlCFMPortIndex_Type = Integer32
_SwL2DevCtrlCFMPortIndex_Object = MibTableColumn
swL2DevCtrlCFMPortIndex = _SwL2DevCtrlCFMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21, 2, 1, 2),
    _SwL2DevCtrlCFMPortState_Type()
)
swL2DevCtrlCFMPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortState.setStatus("current")
_SwL2DevCtrlCFMMaTable_Object = MibTable
swL2DevCtrlCFMMaTable = _SwL2DevCtrlCFMMaTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21, 3)
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMMaTable.setStatus("current")
_SwL2DevCtrlCFMMaEntry_Object = MibTableRow
swL2DevCtrlCFMMaEntry = _SwL2DevCtrlCFMMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21, 3, 1)
)
swL2DevCtrlCFMMaEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMMaEntry.setStatus("current")


class _SwL2DevCtrlCFMMaMode_Type(Integer32):
    """Custom type swL2DevCtrlCFMMaMode based on Integer32"""
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


_SwL2DevCtrlCFMMaMode_Type.__name__ = "Integer32"
_SwL2DevCtrlCFMMaMode_Object = MibTableColumn
swL2DevCtrlCFMMaMode = _SwL2DevCtrlCFMMaMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21, 3, 1, 1),
    _SwL2DevCtrlCFMMaMode_Type()
)
swL2DevCtrlCFMMaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMMaMode.setStatus("current")
_SwL2DevCtrlCFMMepTable_Object = MibTable
swL2DevCtrlCFMMepTable = _SwL2DevCtrlCFMMepTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21, 4)
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMMepTable.setStatus("current")
_SwL2DevCtrlCFMMepEntry_Object = MibTableRow
swL2DevCtrlCFMMepEntry = _SwL2DevCtrlCFMMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21, 4, 1)
)
swL2DevCtrlCFMMepEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMMepEntry.setStatus("current")


class _SwL2DevCtrlCFMMepMode_Type(Integer32):
    """Custom type swL2DevCtrlCFMMepMode based on Integer32"""
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


_SwL2DevCtrlCFMMepMode_Type.__name__ = "Integer32"
_SwL2DevCtrlCFMMepMode_Object = MibTableColumn
swL2DevCtrlCFMMepMode = _SwL2DevCtrlCFMMepMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 21, 4, 1, 1),
    _SwL2DevCtrlCFMMepMode_Type()
)
swL2DevCtrlCFMMepMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMMepMode.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 22),
    _SwL2DevCtrlVLANTrunkState_Type()
)
swL2DevCtrlVLANTrunkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlVLANTrunkState.setStatus("current")


class _SwL2DevCtrlIpAutoconfigTimeout_Type(Integer32):
    """Custom type swL2DevCtrlIpAutoconfigTimeout based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2DevCtrlIpAutoconfigTimeout_Type.__name__ = "Integer32"
_SwL2DevCtrlIpAutoconfigTimeout_Object = MibScalar
swL2DevCtrlIpAutoconfigTimeout = _SwL2DevCtrlIpAutoconfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 2, 23),
    _SwL2DevCtrlIpAutoconfigTimeout_Type()
)
swL2DevCtrlIpAutoconfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIpAutoconfigTimeout.setStatus("current")
if mibBuilder.loadTexts:
    swL2DevCtrlIpAutoconfigTimeout.setUnits("seconds")
_SwL2DevAlarm_ObjectIdentity = ObjectIdentity
swL2DevAlarm = _SwL2DevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 1, 3, 3),
    _SwL2DevAlarmLinkChange_Type()
)
swL2DevAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmLinkChange.setStatus("current")
_SwL2VLANMgmt_ObjectIdentity = ObjectIdentity
swL2VLANMgmt = _SwL2VLANMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2)
)
_SwL2VlanStaticTable_Object = MibTable
swL2VlanStaticTable = _SwL2VlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swL2VlanStaticTable.setStatus("current")
_SwL2VlanStaticEntry_Object = MibTableRow
swL2VlanStaticEntry = _SwL2VlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 1, 1)
)
swL2VlanStaticEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2VlanIndex"),
)
if mibBuilder.loadTexts:
    swL2VlanStaticEntry.setStatus("current")
_SwL2VlanIndex_Type = VlanId
_SwL2VlanIndex_Object = MibTableColumn
swL2VlanIndex = _SwL2VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 2),
    _SwL2PVIDAutoAssignmentState_Type()
)
swL2PVIDAutoAssignmentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PVIDAutoAssignmentState.setStatus("current")
_SwL2VlanPortInfoTable_Object = MibTable
swL2VlanPortInfoTable = _SwL2VlanPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    swL2VlanPortInfoTable.setStatus("current")
_SwL2VlanPortInfoEntry_Object = MibTableRow
swL2VlanPortInfoEntry = _SwL2VlanPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 3, 1)
)
swL2VlanPortInfoEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2VlanPortInfoPortIndex"),
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2VlanPortInfoVid"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 3, 1, 1),
    _SwL2VlanPortInfoPortIndex_Type()
)
swL2VlanPortInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanPortInfoPortIndex.setStatus("current")
_SwL2VlanPortInfoVid_Type = VlanId
_SwL2VlanPortInfoVid_Object = MibTableColumn
swL2VlanPortInfoVid = _SwL2VlanPortInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 3, 1, 3),
    _SwL2VlanPortInfoPortRole_Type()
)
swL2VlanPortInfoPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanPortInfoPortRole.setStatus("current")
_SwL2SubnetVLANTable_Object = MibTable
swL2SubnetVLANTable = _SwL2SubnetVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    swL2SubnetVLANTable.setStatus("current")
_SwL2SubnetVLANEntry_Object = MibTableRow
swL2SubnetVLANEntry = _SwL2SubnetVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 4, 1)
)
swL2SubnetVLANEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2SubnetVLANIPAddress"),
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2SubnetVLANIPMask"),
)
if mibBuilder.loadTexts:
    swL2SubnetVLANEntry.setStatus("current")
_SwL2SubnetVLANIPAddress_Type = IpAddress
_SwL2SubnetVLANIPAddress_Object = MibTableColumn
swL2SubnetVLANIPAddress = _SwL2SubnetVLANIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 4, 1, 1),
    _SwL2SubnetVLANIPAddress_Type()
)
swL2SubnetVLANIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2SubnetVLANIPAddress.setStatus("current")
_SwL2SubnetVLANIPMask_Type = IpAddress
_SwL2SubnetVLANIPMask_Object = MibTableColumn
swL2SubnetVLANIPMask = _SwL2SubnetVLANIPMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 4, 1, 2),
    _SwL2SubnetVLANIPMask_Type()
)
swL2SubnetVLANIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2SubnetVLANIPMask.setStatus("current")
_SwL2SubnetVLANID_Type = VlanId
_SwL2SubnetVLANID_Object = MibTableColumn
swL2SubnetVLANID = _SwL2SubnetVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 4, 1, 4),
    _SwL2SubnetVLANPriority_Type()
)
swL2SubnetVLANPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2SubnetVLANPriority.setStatus("current")
_SwL2SubnetVLANRowStatus_Type = RowStatus
_SwL2SubnetVLANRowStatus_Object = MibTableColumn
swL2SubnetVLANRowStatus = _SwL2SubnetVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 4, 1, 5),
    _SwL2SubnetVLANRowStatus_Type()
)
swL2SubnetVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2SubnetVLANRowStatus.setStatus("current")
_SwL2VlanPrecedenceTable_Object = MibTable
swL2VlanPrecedenceTable = _SwL2VlanPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    swL2VlanPrecedenceTable.setStatus("current")
_SwL2VlanPrecedenceEntry_Object = MibTableRow
swL2VlanPrecedenceEntry = _SwL2VlanPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 5, 1)
)
swL2VlanPrecedenceEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2VlanPrecedencePortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 2, 6),
    _SwL2NniGvrpBpduAddress_Type()
)
swL2NniGvrpBpduAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2NniGvrpBpduAddress.setStatus("current")
_SwL2PortMgmt_ObjectIdentity = ObjectIdentity
swL2PortMgmt = _SwL2PortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3)
)
_SwL2PortInfoTable_Object = MibTable
swL2PortInfoTable = _SwL2PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    swL2PortInfoTable.setStatus("current")
_SwL2PortInfoEntry_Object = MibTableRow
swL2PortInfoEntry = _SwL2PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 1, 1)
)
swL2PortInfoEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortInfoPortIndex"),
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortInfoMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 1, 1, 7),
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
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bpdu-protection", 6),
          ("ctp-lbd", 4),
          ("ddm", 5),
          ("ip-mac-port-binding", 9),
          ("mac-temperature", 10),
          ("none", 0),
          ("oam-unidirectional-link", 11),
          ("port-security", 8),
          ("power-saving", 7),
          ("storm-control", 1),
          ("stp-lbd", 2),
          ("unknow", 3))
    )


_SwL2PortInfoErrorDisabled_Type.__name__ = "Integer32"
_SwL2PortInfoErrorDisabled_Object = MibTableColumn
swL2PortInfoErrorDisabled = _SwL2PortInfoErrorDisabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 1, 1, 8),
    _SwL2PortInfoErrorDisabled_Type()
)
swL2PortInfoErrorDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoErrorDisabled.setStatus("current")
_SwL2PortCtrlTable_Object = MibTable
swL2PortCtrlTable = _SwL2PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    swL2PortCtrlTable.setStatus("current")
_SwL2PortCtrlEntry_Object = MibTableRow
swL2PortCtrlEntry = _SwL2PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1)
)
swL2PortCtrlEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortCtrlPortIndex"),
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortCtrlMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1, 11),
    _SwL2PortCtrlAutoNegRestart_Type()
)
swL2PortCtrlAutoNegRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAutoNegRestart.setStatus("current")
_SwL2PortCtrlAutoNegCapAdvertisedBits_Type = IANAifMauAutoNegCapBits
_SwL2PortCtrlAutoNegCapAdvertisedBits_Object = MibTableColumn
swL2PortCtrlAutoNegCapAdvertisedBits = _SwL2PortCtrlAutoNegCapAdvertisedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 2, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 3),
    _SwL2PortCtrlJumboFrame_Type()
)
swL2PortCtrlJumboFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlJumboFrame.setStatus("current")
_SwL2PortCtrlJumboFrameMaxSize_Type = Integer32
_SwL2PortCtrlJumboFrameMaxSize_Object = MibScalar
swL2PortCtrlJumboFrameMaxSize = _SwL2PortCtrlJumboFrameMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 4),
    _SwL2PortCtrlJumboFrameMaxSize_Type()
)
swL2PortCtrlJumboFrameMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlJumboFrameMaxSize.setStatus("current")
_SwL2PortCableDiagnosisTable_Object = MibTable
swL2PortCableDiagnosisTable = _SwL2PortCableDiagnosisTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisTable.setStatus("current")
_SwL2PortCableDiagnosisEntry_Object = MibTableRow
swL2PortCableDiagnosisEntry = _SwL2PortCableDiagnosisEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 5, 1)
)
swL2PortCableDiagnosisEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortCableDiagnosisPortIndex"),
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortCableDiagnosisPairIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 5, 1, 4),
    _SwL2PortCableDiagnosisPairStatus_Type()
)
swL2PortCableDiagnosisPairStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisPairStatus.setStatus("current")
_SwL2PortCableDiagnosisPairLength_Type = Integer32
_SwL2PortCableDiagnosisPairLength_Object = MibTableColumn
swL2PortCableDiagnosisPairLength = _SwL2PortCableDiagnosisPairLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 5, 1, 5),
    _SwL2PortCableDiagnosisPairLength_Type()
)
swL2PortCableDiagnosisPairLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisPairLength.setStatus("current")
_SwL2PortCableDiagnosisPairLengthInaccuracy_Type = Integer32
_SwL2PortCableDiagnosisPairLengthInaccuracy_Object = MibTableColumn
swL2PortCableDiagnosisPairLengthInaccuracy = _SwL2PortCableDiagnosisPairLengthInaccuracy_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 5, 1, 6),
    _SwL2PortCableDiagnosisPairLengthInaccuracy_Type()
)
swL2PortCableDiagnosisPairLengthInaccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCableDiagnosisPairLengthInaccuracy.setStatus("current")
_SwL2PortCounterCtrlTable_Object = MibTable
swL2PortCounterCtrlTable = _SwL2PortCounterCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    swL2PortCounterCtrlTable.setStatus("current")
_SwL2PortCounterCtrlEntry_Object = MibTableRow
swL2PortCounterCtrlEntry = _SwL2PortCounterCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 6, 1)
)
swL2PortCounterCtrlEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortCounterCtrlPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 6, 1, 2),
    _SwL2PortCounterClearCtrl_Type()
)
swL2PortCounterClearCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCounterClearCtrl.setStatus("current")
_SwL2PortErrTable_Object = MibTable
swL2PortErrTable = _SwL2PortErrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 7)
)
if mibBuilder.loadTexts:
    swL2PortErrTable.setStatus("current")
_SwL2PortErrEntry_Object = MibTableRow
swL2PortErrEntry = _SwL2PortErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 7, 1)
)
swL2PortErrEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortErrPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 7, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 7, 1, 3),
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
            *(0,
              1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bpdu-protection", 6),
          ("ctp-lbd", 4),
          ("ddm", 5),
          ("ip-mac-port-binding", 9),
          ("mac-temperature", 10),
          ("none", 0),
          ("oam-unidirectional-link", 11),
          ("port-security", 8),
          ("power-saving", 7),
          ("storm-control", 2),
          ("stp-lbd", 1))
    )


_SwL2PortErrPortReason_Type.__name__ = "Integer32"
_SwL2PortErrPortReason_Object = MibTableColumn
swL2PortErrPortReason = _SwL2PortErrPortReason_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 7, 1, 4),
    _SwL2PortErrPortReason_Type()
)
swL2PortErrPortReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortReason.setStatus("current")
_SwL2PortAutoNegInfoTable_Object = MibTable
swL2PortAutoNegInfoTable = _SwL2PortAutoNegInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 8)
)
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoTable.setStatus("current")
_SwL2PortAutoNegInfoEntry_Object = MibTableRow
swL2PortAutoNegInfoEntry = _SwL2PortAutoNegInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 8, 1)
)
swL2PortAutoNegInfoEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortAutoNegInfoPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 8, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 8, 1, 2),
    _SwL2PortAutoNegInfoAdminStatus_Type()
)
swL2PortAutoNegInfoAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoAdminStatus.setStatus("current")
_SwL2PortAutoNegInfoCapabilityBits_Type = IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapabilityBits_Object = MibTableColumn
swL2PortAutoNegInfoCapabilityBits = _SwL2PortAutoNegInfoCapabilityBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 8, 1, 3),
    _SwL2PortAutoNegInfoCapabilityBits_Type()
)
swL2PortAutoNegInfoCapabilityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoCapabilityBits.setStatus("current")
_SwL2PortAutoNegInfoCapAdvertisedBits_Type = IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapAdvertisedBits_Object = MibTableColumn
swL2PortAutoNegInfoCapAdvertisedBits = _SwL2PortAutoNegInfoCapAdvertisedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 8, 1, 4),
    _SwL2PortAutoNegInfoCapAdvertisedBits_Type()
)
swL2PortAutoNegInfoCapAdvertisedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoCapAdvertisedBits.setStatus("current")
_SwL2PortAutoNegInfoCapReceivedBits_Type = IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapReceivedBits_Object = MibTableColumn
swL2PortAutoNegInfoCapReceivedBits = _SwL2PortAutoNegInfoCapReceivedBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 8, 1, 5),
    _SwL2PortAutoNegInfoCapReceivedBits_Type()
)
swL2PortAutoNegInfoCapReceivedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortAutoNegInfoCapReceivedBits.setStatus("current")
_SwL2PortDropCounterTable_Object = MibTable
swL2PortDropCounterTable = _SwL2PortDropCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9)
)
if mibBuilder.loadTexts:
    swL2PortDropCounterTable.setStatus("current")
_SwL2PortDropCounterEntry_Object = MibTableRow
swL2PortDropCounterEntry = _SwL2PortDropCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1)
)
swL2PortDropCounterEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortDropCounterPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1, 1),
    _SwL2PortDropCounterPortIndex_Type()
)
swL2PortDropCounterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortDropCounterPortIndex.setStatus("current")
_SwL2PortBufferFullDrops_Type = Counter32
_SwL2PortBufferFullDrops_Object = MibTableColumn
swL2PortBufferFullDrops = _SwL2PortBufferFullDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1, 2),
    _SwL2PortBufferFullDrops_Type()
)
swL2PortBufferFullDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortBufferFullDrops.setStatus("current")
_SwL2PortACLDrops_Type = Counter32
_SwL2PortACLDrops_Object = MibTableColumn
swL2PortACLDrops = _SwL2PortACLDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1, 3),
    _SwL2PortACLDrops_Type()
)
swL2PortACLDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortACLDrops.setStatus("current")
_SwL2PortMulticastDrops_Type = Counter32
_SwL2PortMulticastDrops_Object = MibTableColumn
swL2PortMulticastDrops = _SwL2PortMulticastDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1, 4),
    _SwL2PortMulticastDrops_Type()
)
swL2PortMulticastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortMulticastDrops.setStatus("current")
_SwL2PortVLANIngressDrops_Type = Counter32
_SwL2PortVLANIngressDrops_Object = MibTableColumn
swL2PortVLANIngressDrops = _SwL2PortVLANIngressDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1, 5),
    _SwL2PortVLANIngressDrops_Type()
)
swL2PortVLANIngressDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortVLANIngressDrops.setStatus("current")
_SwL2PortIngressBandwidthControlDrops_Type = Counter32
_SwL2PortIngressBandwidthControlDrops_Object = MibTableColumn
swL2PortIngressBandwidthControlDrops = _SwL2PortIngressBandwidthControlDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1, 6),
    _SwL2PortIngressBandwidthControlDrops_Type()
)
swL2PortIngressBandwidthControlDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortIngressBandwidthControlDrops.setStatus("current")
_SwL2PortInvalidIPv6Drops_Type = Counter32
_SwL2PortInvalidIPv6Drops_Object = MibTableColumn
swL2PortInvalidIPv6Drops = _SwL2PortInvalidIPv6Drops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1, 7),
    _SwL2PortInvalidIPv6Drops_Type()
)
swL2PortInvalidIPv6Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInvalidIPv6Drops.setStatus("current")
_SwL2PortSTPDrops_Type = Counter32
_SwL2PortSTPDrops_Object = MibTableColumn
swL2PortSTPDrops = _SwL2PortSTPDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1, 8),
    _SwL2PortSTPDrops_Type()
)
swL2PortSTPDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSTPDrops.setStatus("current")
_SwL2PortStormAndFDBDiscard_Type = Counter32
_SwL2PortStormAndFDBDiscard_Object = MibTableColumn
swL2PortStormAndFDBDiscard = _SwL2PortStormAndFDBDiscard_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1, 9),
    _SwL2PortStormAndFDBDiscard_Type()
)
swL2PortStormAndFDBDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortStormAndFDBDiscard.setStatus("current")
_SwL2PortMTUDrops_Type = Counter32
_SwL2PortMTUDrops_Object = MibTableColumn
swL2PortMTUDrops = _SwL2PortMTUDrops_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1, 10),
    _SwL2PortMTUDrops_Type()
)
swL2PortMTUDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortMTUDrops.setStatus("current")
_SwL2PortInvalidDestinationPort_Type = Counter32
_SwL2PortInvalidDestinationPort_Object = MibTableColumn
swL2PortInvalidDestinationPort = _SwL2PortInvalidDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 9, 1, 11),
    _SwL2PortInvalidDestinationPort_Type()
)
swL2PortInvalidDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInvalidDestinationPort.setStatus("current")
_SwL2PortJumboFrameCtrlTable_Object = MibTable
swL2PortJumboFrameCtrlTable = _SwL2PortJumboFrameCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 10)
)
if mibBuilder.loadTexts:
    swL2PortJumboFrameCtrlTable.setStatus("current")
_SwL2PortJumboFrameCtrlEntry_Object = MibTableRow
swL2PortJumboFrameCtrlEntry = _SwL2PortJumboFrameCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 10, 1)
)
swL2PortJumboFrameCtrlEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortJumboFrameCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortJumboFrameCtrlEntry.setStatus("current")
_SwL2PortJumboFrameCtrlPortIndex_Type = Integer32
_SwL2PortJumboFrameCtrlPortIndex_Object = MibTableColumn
swL2PortJumboFrameCtrlPortIndex = _SwL2PortJumboFrameCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 10, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 10, 1, 2),
    _SwL2PortJumboFrameCtrlState_Type()
)
swL2PortJumboFrameCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortJumboFrameCtrlState.setStatus("current")
_SwL2PortSfpInfoTable_Object = MibTable
swL2PortSfpInfoTable = _SwL2PortSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11)
)
if mibBuilder.loadTexts:
    swL2PortSfpInfoTable.setStatus("current")
_SwL2PortSfpInfoEntry_Object = MibTableRow
swL2PortSfpInfoEntry = _SwL2PortSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1)
)
swL2PortSfpInfoEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortSfpInfoPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortSfpInfoEntry.setStatus("current")


class _SwL2PortSfpInfoPortIndex_Type(Integer32):
    """Custom type swL2PortSfpInfoPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortSfpInfoPortIndex_Type.__name__ = "Integer32"
_SwL2PortSfpInfoPortIndex_Object = MibTableColumn
swL2PortSfpInfoPortIndex = _SwL2PortSfpInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1, 1),
    _SwL2PortSfpInfoPortIndex_Type()
)
swL2PortSfpInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSfpInfoPortIndex.setStatus("current")


class _SwL2PortSfpInfoConnectType_Type(DisplayString):
    """Custom type swL2PortSfpInfoConnectType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SwL2PortSfpInfoConnectType_Type.__name__ = "DisplayString"
_SwL2PortSfpInfoConnectType_Object = MibTableColumn
swL2PortSfpInfoConnectType = _SwL2PortSfpInfoConnectType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1, 2),
    _SwL2PortSfpInfoConnectType_Type()
)
swL2PortSfpInfoConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSfpInfoConnectType.setStatus("current")


class _SwL2PortSfpInfoVendorName_Type(DisplayString):
    """Custom type swL2PortSfpInfoVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SwL2PortSfpInfoVendorName_Type.__name__ = "DisplayString"
_SwL2PortSfpInfoVendorName_Object = MibTableColumn
swL2PortSfpInfoVendorName = _SwL2PortSfpInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1, 3),
    _SwL2PortSfpInfoVendorName_Type()
)
swL2PortSfpInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSfpInfoVendorName.setStatus("current")


class _SwL2PortSfpInfoVendorPN_Type(DisplayString):
    """Custom type swL2PortSfpInfoVendorPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SwL2PortSfpInfoVendorPN_Type.__name__ = "DisplayString"
_SwL2PortSfpInfoVendorPN_Object = MibTableColumn
swL2PortSfpInfoVendorPN = _SwL2PortSfpInfoVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1, 4),
    _SwL2PortSfpInfoVendorPN_Type()
)
swL2PortSfpInfoVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSfpInfoVendorPN.setStatus("current")


class _SwL2PortSfpInfoVendorSN_Type(DisplayString):
    """Custom type swL2PortSfpInfoVendorSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SwL2PortSfpInfoVendorSN_Type.__name__ = "DisplayString"
_SwL2PortSfpInfoVendorSN_Object = MibTableColumn
swL2PortSfpInfoVendorSN = _SwL2PortSfpInfoVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1, 5),
    _SwL2PortSfpInfoVendorSN_Type()
)
swL2PortSfpInfoVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSfpInfoVendorSN.setStatus("current")


class _SwL2PortSfpInfoVendorOUI_Type(DisplayString):
    """Custom type swL2PortSfpInfoVendorOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_SwL2PortSfpInfoVendorOUI_Type.__name__ = "DisplayString"
_SwL2PortSfpInfoVendorOUI_Object = MibTableColumn
swL2PortSfpInfoVendorOUI = _SwL2PortSfpInfoVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1, 6),
    _SwL2PortSfpInfoVendorOUI_Type()
)
swL2PortSfpInfoVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSfpInfoVendorOUI.setStatus("current")


class _SwL2PortSfpInfoVendorRev_Type(DisplayString):
    """Custom type swL2PortSfpInfoVendorRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_SwL2PortSfpInfoVendorRev_Type.__name__ = "DisplayString"
_SwL2PortSfpInfoVendorRev_Object = MibTableColumn
swL2PortSfpInfoVendorRev = _SwL2PortSfpInfoVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1, 7),
    _SwL2PortSfpInfoVendorRev_Type()
)
swL2PortSfpInfoVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSfpInfoVendorRev.setStatus("current")


class _SwL2PortSfpInfoDateCode_Type(DisplayString):
    """Custom type swL2PortSfpInfoDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SwL2PortSfpInfoDateCode_Type.__name__ = "DisplayString"
_SwL2PortSfpInfoDateCode_Object = MibTableColumn
swL2PortSfpInfoDateCode = _SwL2PortSfpInfoDateCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1, 8),
    _SwL2PortSfpInfoDateCode_Type()
)
swL2PortSfpInfoDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSfpInfoDateCode.setStatus("current")


class _SwL2PortSfpInfoFiberType_Type(DisplayString):
    """Custom type swL2PortSfpInfoFiberType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_SwL2PortSfpInfoFiberType_Type.__name__ = "DisplayString"
_SwL2PortSfpInfoFiberType_Object = MibTableColumn
swL2PortSfpInfoFiberType = _SwL2PortSfpInfoFiberType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1, 9),
    _SwL2PortSfpInfoFiberType_Type()
)
swL2PortSfpInfoFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSfpInfoFiberType.setStatus("current")


class _SwL2PortSfpInfoBaudRate_Type(Integer32):
    """Custom type swL2PortSfpInfoBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortSfpInfoBaudRate_Type.__name__ = "Integer32"
_SwL2PortSfpInfoBaudRate_Object = MibTableColumn
swL2PortSfpInfoBaudRate = _SwL2PortSfpInfoBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1, 10),
    _SwL2PortSfpInfoBaudRate_Type()
)
swL2PortSfpInfoBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSfpInfoBaudRate.setStatus("current")


class _SwL2PortSfpInfoWavelength_Type(Integer32):
    """Custom type swL2PortSfpInfoWavelength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortSfpInfoWavelength_Type.__name__ = "Integer32"
_SwL2PortSfpInfoWavelength_Object = MibTableColumn
swL2PortSfpInfoWavelength = _SwL2PortSfpInfoWavelength_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 11, 1, 11),
    _SwL2PortSfpInfoWavelength_Type()
)
swL2PortSfpInfoWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSfpInfoWavelength.setStatus("current")
_SwL2PortLinkTimeTable_Object = MibTable
swL2PortLinkTimeTable = _SwL2PortLinkTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 14)
)
if mibBuilder.loadTexts:
    swL2PortLinkTimeTable.setStatus("current")
_SwL2PortLinkTimeEntry_Object = MibTableRow
swL2PortLinkTimeEntry = _SwL2PortLinkTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 14, 1)
)
swL2PortLinkTimeEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2PortLinkTimeIfIndex"),
)
if mibBuilder.loadTexts:
    swL2PortLinkTimeEntry.setStatus("current")


class _SwL2PortLinkTimeIfIndex_Type(Integer32):
    """Custom type swL2PortLinkTimeIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PortLinkTimeIfIndex_Type.__name__ = "Integer32"
_SwL2PortLinkTimeIfIndex_Object = MibTableColumn
swL2PortLinkTimeIfIndex = _SwL2PortLinkTimeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 14, 1, 1),
    _SwL2PortLinkTimeIfIndex_Type()
)
swL2PortLinkTimeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortLinkTimeIfIndex.setStatus("current")
_SwL2PortLinkTimer_Type = TimeTicks
_SwL2PortLinkTimer_Object = MibTableColumn
swL2PortLinkTimer = _SwL2PortLinkTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 3, 14, 1, 2),
    _SwL2PortLinkTimer_Type()
)
swL2PortLinkTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortLinkTimer.setStatus("current")
_SwL2TrunkMgmt_ObjectIdentity = ObjectIdentity
swL2TrunkMgmt = _SwL2TrunkMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 2),
    _SwL2TrunkCurrentNumEntries_Type()
)
swL2TrunkCurrentNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkCurrentNumEntries.setStatus("current")
_SwL2TrunkCtrlTable_Object = MibTable
swL2TrunkCtrlTable = _SwL2TrunkCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 3)
)
if mibBuilder.loadTexts:
    swL2TrunkCtrlTable.setStatus("current")
_SwL2TrunkCtrlEntry_Object = MibTableRow
swL2TrunkCtrlEntry = _SwL2TrunkCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 3, 1)
)
swL2TrunkCtrlEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2TrunkIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 3, 1, 3),
    _SwL2TrunkMasterPort_Type()
)
swL2TrunkMasterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkMasterPort.setStatus("current")
_SwL2TrunkMember_Type = PortList
_SwL2TrunkMember_Object = MibTableColumn
swL2TrunkMember = _SwL2TrunkMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 3, 1, 6),
    _SwL2TrunkType_Type()
)
swL2TrunkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkType.setStatus("current")
_SwL2TrunkState_Type = RowStatus
_SwL2TrunkState_Object = MibTableColumn
swL2TrunkState = _SwL2TrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 4),
    _SwL2TrunkAlgorithm_Type()
)
swL2TrunkAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkAlgorithm.setStatus("current")
_SwL2TrunkLACPPortTable_Object = MibTable
swL2TrunkLACPPortTable = _SwL2TrunkLACPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 5)
)
if mibBuilder.loadTexts:
    swL2TrunkLACPPortTable.setStatus("current")
_SwL2TrunkLACPPortEntry_Object = MibTableRow
swL2TrunkLACPPortEntry = _SwL2TrunkLACPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 5, 1)
)
swL2TrunkLACPPortEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2TrunkLACPPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 5, 1, 2),
    _SwL2TrunkLACPPortState_Type()
)
swL2TrunkLACPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkLACPPortState.setStatus("current")
_SwL2TrunkVLANTable_Object = MibTable
swL2TrunkVLANTable = _SwL2TrunkVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 6)
)
if mibBuilder.loadTexts:
    swL2TrunkVLANTable.setStatus("current")
_SwL2TrunkVLANEntry_Object = MibTableRow
swL2TrunkVLANEntry = _SwL2TrunkVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 6, 1)
)
swL2TrunkVLANEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2TrunkVLANPort"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 9, 6, 1, 2),
    _SwL2TrunkVLANState_Type()
)
swL2TrunkVLANState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkVLANState.setStatus("current")
_SwL2MirrorMgmt_ObjectIdentity = ObjectIdentity
swL2MirrorMgmt = _SwL2MirrorMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 1),
    _SwL2MirrorLogicTargetPort_Type()
)
swL2MirrorLogicTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorLogicTargetPort.setStatus("current")
_SwL2MirrorPortSourceIngress_Type = PortList
_SwL2MirrorPortSourceIngress_Object = MibScalar
swL2MirrorPortSourceIngress = _SwL2MirrorPortSourceIngress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 2),
    _SwL2MirrorPortSourceIngress_Type()
)
swL2MirrorPortSourceIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortSourceIngress.setStatus("current")
_SwL2MirrorPortSourceEgress_Type = PortList
_SwL2MirrorPortSourceEgress_Object = MibScalar
swL2MirrorPortSourceEgress = _SwL2MirrorPortSourceEgress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 4),
    _SwL2MirrorPortState_Type()
)
swL2MirrorPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortState.setStatus("current")
_SwL2MirrorGroupTable_Object = MibTable
swL2MirrorGroupTable = _SwL2MirrorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 5)
)
if mibBuilder.loadTexts:
    swL2MirrorGroupTable.setStatus("current")
_SwL2MirrorGroupEntry_Object = MibTableRow
swL2MirrorGroupEntry = _SwL2MirrorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 5, 1)
)
swL2MirrorGroupEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2MirrorGroupID"),
)
if mibBuilder.loadTexts:
    swL2MirrorGroupEntry.setStatus("current")
_SwL2MirrorGroupID_Type = Integer32
_SwL2MirrorGroupID_Object = MibTableColumn
swL2MirrorGroupID = _SwL2MirrorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 5, 1, 1),
    _SwL2MirrorGroupID_Type()
)
swL2MirrorGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2MirrorGroupID.setStatus("current")
_SwL2MirrorGroupRowStatus_Type = RowStatus
_SwL2MirrorGroupRowStatus_Object = MibTableColumn
swL2MirrorGroupRowStatus = _SwL2MirrorGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 5, 1, 2),
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2MirrorGroupState_Type.__name__ = "Integer32"
_SwL2MirrorGroupState_Object = MibTableColumn
swL2MirrorGroupState = _SwL2MirrorGroupState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 5, 1, 4),
    _SwL2MirrorGroupTargetPort_Type()
)
swL2MirrorGroupTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupTargetPort.setStatus("current")
_SwL2MirrorGroupSourceIngress_Type = PortList
_SwL2MirrorGroupSourceIngress_Object = MibTableColumn
swL2MirrorGroupSourceIngress = _SwL2MirrorGroupSourceIngress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 5, 1, 5),
    _SwL2MirrorGroupSourceIngress_Type()
)
swL2MirrorGroupSourceIngress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupSourceIngress.setStatus("current")
_SwL2MirrorGroupSourceEgress_Type = PortList
_SwL2MirrorGroupSourceEgress_Object = MibTableColumn
swL2MirrorGroupSourceEgress = _SwL2MirrorGroupSourceEgress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 10, 5, 1, 6),
    _SwL2MirrorGroupSourceEgress_Type()
)
swL2MirrorGroupSourceEgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupSourceEgress.setStatus("current")
_SwL2IGMPMgmt_ObjectIdentity = ObjectIdentity
swL2IGMPMgmt = _SwL2IGMPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 11)
)
_SwL2IGMPAccessAuthTable_Object = MibTable
swL2IGMPAccessAuthTable = _SwL2IGMPAccessAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 11, 13)
)
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthTable.setStatus("current")
_SwL2IGMPAccessAuthEntry_Object = MibTableRow
swL2IGMPAccessAuthEntry = _SwL2IGMPAccessAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 11, 13, 1)
)
swL2IGMPAccessAuthEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2IGMPAccessAuthPort"),
)
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthEntry.setStatus("current")
_SwL2IGMPAccessAuthPort_Type = Integer32
_SwL2IGMPAccessAuthPort_Object = MibTableColumn
swL2IGMPAccessAuthPort = _SwL2IGMPAccessAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 11, 13, 1, 1),
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
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("accounting_only", 4),
          ("auth_only", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_SwL2IGMPAccessAuthState_Type.__name__ = "Integer32"
_SwL2IGMPAccessAuthState_Object = MibTableColumn
swL2IGMPAccessAuthState = _SwL2IGMPAccessAuthState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 11, 13, 1, 2),
    _SwL2IGMPAccessAuthState_Type()
)
swL2IGMPAccessAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthState.setStatus("current")
_SwL2TrafficMgmt_ObjectIdentity = ObjectIdentity
swL2TrafficMgmt = _SwL2TrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 13)
)
_SwL2TrafficCtrlTable_Object = MibTable
swL2TrafficCtrlTable = _SwL2TrafficCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    swL2TrafficCtrlTable.setStatus("current")
_SwL2TrafficCtrlEntry_Object = MibTableRow
swL2TrafficCtrlEntry = _SwL2TrafficCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 13, 1, 1)
)
swL2TrafficCtrlEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2TrafficCtrlGroupIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 13, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 13, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 13, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 13, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 13, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 13, 1, 1, 6),
    _SwL2TrafficCtrlDlfStromCtrl_Type()
)
swL2TrafficCtrlDlfStromCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlDlfStromCtrl.setStatus("current")
_SwL2TrafficSegMgmt_ObjectIdentity = ObjectIdentity
swL2TrafficSegMgmt = _SwL2TrafficSegMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 14)
)
_SwL2TrafficSegTable_Object = MibTable
swL2TrafficSegTable = _SwL2TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 14, 1)
)
if mibBuilder.loadTexts:
    swL2TrafficSegTable.setStatus("current")
_SwL2TrafficSegEntry_Object = MibTableRow
swL2TrafficSegEntry = _SwL2TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 14, 1, 1)
)
swL2TrafficSegEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2TrafficSegPort"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 14, 1, 1, 1),
    _SwL2TrafficSegPort_Type()
)
swL2TrafficSegPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficSegPort.setStatus("current")
_SwL2TrafficSegForwardPorts_Type = PortList
_SwL2TrafficSegForwardPorts_Object = MibTableColumn
swL2TrafficSegForwardPorts = _SwL2TrafficSegForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 14, 1, 1, 2),
    _SwL2TrafficSegForwardPorts_Type()
)
swL2TrafficSegForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficSegForwardPorts.setStatus("current")
_SwL2MulticastFilterMode_ObjectIdentity = ObjectIdentity
swL2MulticastFilterMode = _SwL2MulticastFilterMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 17)
)
_SwL2MulticastFilterModeVlanTable_Object = MibTable
swL2MulticastFilterModeVlanTable = _SwL2MulticastFilterModeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    swL2MulticastFilterModeVlanTable.setStatus("current")
_SwL2MulticastFilterModeVlanEntry_Object = MibTableRow
swL2MulticastFilterModeVlanEntry = _SwL2MulticastFilterModeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 17, 1, 1)
)
swL2MulticastFilterModeVlanEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2MulticastFilterVid"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 17, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 17, 1, 1, 2),
    _SwL2MulticastFilterVlanMode_Type()
)
swL2MulticastFilterVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MulticastFilterVlanMode.setStatus("current")
_SwL2MulticastFilterModePortTable_Object = MibTable
swL2MulticastFilterModePortTable = _SwL2MulticastFilterModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 17, 2)
)
if mibBuilder.loadTexts:
    swL2MulticastFilterModePortTable.setStatus("current")
_SwL2MulticastFilterModePortEntry_Object = MibTableRow
swL2MulticastFilterModePortEntry = _SwL2MulticastFilterModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 17, 2, 1)
)
swL2MulticastFilterModePortEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2MulticastFilterPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 17, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 17, 2, 1, 2),
    _SwL2MulticastFilterPortMode_Type()
)
swL2MulticastFilterPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MulticastFilterPortMode.setStatus("current")
_SwL2LoopDetectMgmt_ObjectIdentity = ObjectIdentity
swL2LoopDetectMgmt = _SwL2LoopDetectMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18)
)
_SwL2LoopDetectCtrl_ObjectIdentity = ObjectIdentity
swL2LoopDetectCtrl = _SwL2LoopDetectCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 1, 5),
    _SwL2LoopDetectTrapMode_Type()
)
swL2LoopDetectTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectTrapMode.setStatus("current")
_SwL2LoopDetectPortMgmt_ObjectIdentity = ObjectIdentity
swL2LoopDetectPortMgmt = _SwL2LoopDetectPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 2)
)
_SwL2LoopDetectPortTable_Object = MibTable
swL2LoopDetectPortTable = _SwL2LoopDetectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    swL2LoopDetectPortTable.setStatus("current")
_SwL2LoopDetectPortEntry_Object = MibTableRow
swL2LoopDetectPortEntry = _SwL2LoopDetectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 2, 1, 1)
)
swL2LoopDetectPortEntry.setIndexNames(
    (0, "DGS3000-28SC-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 2, 1, 1, 2),
    _SwL2LoopDetectPortState_Type()
)
swL2LoopDetectPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectPortState.setStatus("current")
_SwL2LoopDetectPortLoopVLAN_Type = DisplayString
_SwL2LoopDetectPortLoopVLAN_Object = MibTableColumn
swL2LoopDetectPortLoopVLAN = _SwL2LoopDetectPortLoopVLAN_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 18, 2, 1, 1, 4),
    _SwL2LoopDetectPortLoopStatus_Type()
)
swL2LoopDetectPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LoopDetectPortLoopStatus.setStatus("current")
_SwL2MgmtMIBTraps_ObjectIdentity = ObjectIdentity
swL2MgmtMIBTraps = _SwL2MgmtMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100)
)
_SwL2Notify_ObjectIdentity = ObjectIdentity
swL2Notify = _SwL2Notify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1)
)
_SwL2NotifyMgmt_ObjectIdentity = ObjectIdentity
swL2NotifyMgmt = _SwL2NotifyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 1)
)
_SwL2macNotificationSeverity_Type = AgentNotifyLevel
_SwL2macNotificationSeverity_Object = MibScalar
swL2macNotificationSeverity = _SwL2macNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 1, 1),
    _SwL2macNotificationSeverity_Type()
)
swL2macNotificationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2macNotificationSeverity.setStatus("current")
_SwL2PortSecurityViolationSeverity_Type = AgentNotifyLevel
_SwL2PortSecurityViolationSeverity_Object = MibScalar
swL2PortSecurityViolationSeverity = _SwL2PortSecurityViolationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 1, 2),
    _SwL2PortSecurityViolationSeverity_Type()
)
swL2PortSecurityViolationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityViolationSeverity.setStatus("current")
_SwL2NotifyPrefix_ObjectIdentity = ObjectIdentity
swL2NotifyPrefix = _SwL2NotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2)
)
_SwL2NotifFirmware_ObjectIdentity = ObjectIdentity
swL2NotifFirmware = _SwL2NotifFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2, 0)
)
_Swl2NotificationBidings_ObjectIdentity = ObjectIdentity
swl2NotificationBidings = _Swl2NotificationBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2, 1, 1),
    _SwL2macNotifyInfo_Type()
)
swL2macNotifyInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2macNotifyInfo.setStatus("current")
_SwL2PortSecurityViolationMac_Type = MacAddress
_SwL2PortSecurityViolationMac_Object = MibScalar
swL2PortSecurityViolationMac = _SwL2PortSecurityViolationMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2, 1, 2),
    _SwL2PortSecurityViolationMac_Type()
)
swL2PortSecurityViolationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swL2PortSecurityViolationMac.setStatus("current")
_SwL2VlanLoopDetectVID_Type = Integer32
_SwL2VlanLoopDetectVID_Object = MibScalar
swL2VlanLoopDetectVID = _SwL2VlanLoopDetectVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2, 1, 3),
    _SwL2VlanLoopDetectVID_Type()
)
swL2VlanLoopDetectVID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swL2VlanLoopDetectVID.setStatus("current")

# Managed Objects groups


# Notification objects

swL2macNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2, 0, 1)
)
swL2macNotification.setObjects(
    ("DGS3000-28SC-L2MGMT-MIB", "swL2macNotifyInfo")
)
if mibBuilder.loadTexts:
    swL2macNotification.setStatus(
        "current"
    )

swL2PortSecurityViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2, 0, 2)
)
swL2PortSecurityViolationTrap.setObjects(
      *(("PORT-SECURITY-MIB", "swPortSecPortIndex"),
        ("DGS3000-28SC-L2MGMT-MIB", "swL2PortSecurityViolationMac"))
)
if mibBuilder.loadTexts:
    swL2PortSecurityViolationTrap.setStatus(
        "current"
    )

swL2PortLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2, 0, 3)
)
swL2PortLoopOccurred.setObjects(
    ("DGS3000-28SC-L2MGMT-MIB", "swL2LoopDetectPortIndex")
)
if mibBuilder.loadTexts:
    swL2PortLoopOccurred.setStatus(
        "current"
    )

swL2PortLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2, 0, 4)
)
swL2PortLoopRestart.setObjects(
    ("DGS3000-28SC-L2MGMT-MIB", "swL2LoopDetectPortIndex")
)
if mibBuilder.loadTexts:
    swL2PortLoopRestart.setStatus(
        "current"
    )

swL2VlanLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2, 0, 5)
)
swL2VlanLoopOccurred.setObjects(
      *(("DGS3000-28SC-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
        ("DGS3000-28SC-L2MGMT-MIB", "swL2VlanLoopDetectVID"))
)
if mibBuilder.loadTexts:
    swL2VlanLoopOccurred.setStatus(
        "current"
    )

swL2VlanLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 2, 100, 1, 2, 0, 6)
)
swL2VlanLoopRestart.setObjects(
      *(("DGS3000-28SC-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
        ("DGS3000-28SC-L2MGMT-MIB", "swL2VlanLoopDetectVID"))
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
    "DGS3000-28SC-L2MGMT-MIB",
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
       "swL2DevCtrlCFMMaTable": swL2DevCtrlCFMMaTable,
       "swL2DevCtrlCFMMaEntry": swL2DevCtrlCFMMaEntry,
       "swL2DevCtrlCFMMaMode": swL2DevCtrlCFMMaMode,
       "swL2DevCtrlCFMMepTable": swL2DevCtrlCFMMepTable,
       "swL2DevCtrlCFMMepEntry": swL2DevCtrlCFMMepEntry,
       "swL2DevCtrlCFMMepMode": swL2DevCtrlCFMMepMode,
       "swL2DevCtrlVLANTrunkState": swL2DevCtrlVLANTrunkState,
       "swL2DevCtrlIpAutoconfigTimeout": swL2DevCtrlIpAutoconfigTimeout,
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
       "swL2PortIngressBandwidthControlDrops": swL2PortIngressBandwidthControlDrops,
       "swL2PortInvalidIPv6Drops": swL2PortInvalidIPv6Drops,
       "swL2PortSTPDrops": swL2PortSTPDrops,
       "swL2PortStormAndFDBDiscard": swL2PortStormAndFDBDiscard,
       "swL2PortMTUDrops": swL2PortMTUDrops,
       "swL2PortInvalidDestinationPort": swL2PortInvalidDestinationPort,
       "swL2PortJumboFrameCtrlTable": swL2PortJumboFrameCtrlTable,
       "swL2PortJumboFrameCtrlEntry": swL2PortJumboFrameCtrlEntry,
       "swL2PortJumboFrameCtrlPortIndex": swL2PortJumboFrameCtrlPortIndex,
       "swL2PortJumboFrameCtrlState": swL2PortJumboFrameCtrlState,
       "swL2PortSfpInfoTable": swL2PortSfpInfoTable,
       "swL2PortSfpInfoEntry": swL2PortSfpInfoEntry,
       "swL2PortSfpInfoPortIndex": swL2PortSfpInfoPortIndex,
       "swL2PortSfpInfoConnectType": swL2PortSfpInfoConnectType,
       "swL2PortSfpInfoVendorName": swL2PortSfpInfoVendorName,
       "swL2PortSfpInfoVendorPN": swL2PortSfpInfoVendorPN,
       "swL2PortSfpInfoVendorSN": swL2PortSfpInfoVendorSN,
       "swL2PortSfpInfoVendorOUI": swL2PortSfpInfoVendorOUI,
       "swL2PortSfpInfoVendorRev": swL2PortSfpInfoVendorRev,
       "swL2PortSfpInfoDateCode": swL2PortSfpInfoDateCode,
       "swL2PortSfpInfoFiberType": swL2PortSfpInfoFiberType,
       "swL2PortSfpInfoBaudRate": swL2PortSfpInfoBaudRate,
       "swL2PortSfpInfoWavelength": swL2PortSfpInfoWavelength,
       "swL2PortLinkTimeTable": swL2PortLinkTimeTable,
       "swL2PortLinkTimeEntry": swL2PortLinkTimeEntry,
       "swL2PortLinkTimeIfIndex": swL2PortLinkTimeIfIndex,
       "swL2PortLinkTimer": swL2PortLinkTimer,
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
       "swL2MirrorGroupSourceEgress": swL2MirrorGroupSourceEgress,
       "swL2IGMPMgmt": swL2IGMPMgmt,
       "swL2IGMPAccessAuthTable": swL2IGMPAccessAuthTable,
       "swL2IGMPAccessAuthEntry": swL2IGMPAccessAuthEntry,
       "swL2IGMPAccessAuthPort": swL2IGMPAccessAuthPort,
       "swL2IGMPAccessAuthState": swL2IGMPAccessAuthState,
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

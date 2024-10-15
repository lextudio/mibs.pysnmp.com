# SNMP MIB module (DGS-3620-28SC-DC-L2MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS-3620-28SC-DC-L2MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:27:32 2024
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

(dlink_Dgs3620Proj_Dgs3620_28SC_DC,) = mibBuilder.importSymbols(
    "SWDGS3620PRIMGMT-MIB",
    "dlink-Dgs3620Proj-Dgs3620-28SC-DC")


# MODULE-IDENTITY

swL2MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1)
)
_SwL2DevInfo_ObjectIdentity = ObjectIdentity
swL2DevInfo = _SwL2DevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 1, 2),
    _SwDevInfoNumOfPortInUse_Type()
)
swDevInfoNumOfPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoNumOfPortInUse.setStatus("current")
_SwL2DevCtrl_ObjectIdentity = ObjectIdentity
swL2DevCtrl = _SwL2DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2)
)


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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 6),
    _SwL2DevCtrlCleanAllStatisticCounter_Type()
)
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCleanAllStatisticCounter.setStatus("current")
_SwL2DevCtrlVlanIdOfFDBTbl_Type = VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object = MibScalar
swL2DevCtrlVlanIdOfFDBTbl = _SwL2DevCtrlVlanIdOfFDBTbl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 13),
    _SwL2DevCtrlAsymVlanState_Type()
)
swL2DevCtrlAsymVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlAsymVlanState.setStatus("current")
_SwL2DevCtrlTelnet_ObjectIdentity = ObjectIdentity
swL2DevCtrlTelnet = _SwL2DevCtrlTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 14)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 14, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 14, 2),
    _SwL2DevCtrlTelnetTcpPort_Type()
)
swL2DevCtrlTelnetTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlTelnetTcpPort.setStatus("current")
_SwL2DevCtrlManagementVlanId_Type = VlanId
_SwL2DevCtrlManagementVlanId_Object = MibScalar
swL2DevCtrlManagementVlanId = _SwL2DevCtrlManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 16),
    _SwL2DevCtrlManagementVlanId_Type()
)
swL2DevCtrlManagementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlManagementVlanId.setStatus("current")
_SwL2DevCtrlWeb_ObjectIdentity = ObjectIdentity
swL2DevCtrlWeb = _SwL2DevCtrlWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 17)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 17, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 17, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 20),
    _SwL2DevCtrlIpAutoconfig_Type()
)
swL2DevCtrlIpAutoconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIpAutoconfig.setStatus("current")
_SwL2DevCtrlCFM_ObjectIdentity = ObjectIdentity
swL2DevCtrlCFM = _SwL2DevCtrlCFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21, 1),
    _SwL2DevCtrlCFMState_Type()
)
swL2DevCtrlCFMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMState.setStatus("current")
_SwL2DevCtrlCFMPortTable_Object = MibTable
swL2DevCtrlCFMPortTable = _SwL2DevCtrlCFMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21, 2)
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortTable.setStatus("current")
_SwL2DevCtrlCFMPortEntry_Object = MibTableRow
swL2DevCtrlCFMPortEntry = _SwL2DevCtrlCFMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21, 2, 1)
)
swL2DevCtrlCFMPortEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2DevCtrlCFMPortIndex"),
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortEntry.setStatus("current")
_SwL2DevCtrlCFMPortIndex_Type = Integer32
_SwL2DevCtrlCFMPortIndex_Object = MibTableColumn
swL2DevCtrlCFMPortIndex = _SwL2DevCtrlCFMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21, 2, 1, 2),
    _SwL2DevCtrlCFMPortState_Type()
)
swL2DevCtrlCFMPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortState.setStatus("current")
_SwL2DevCtrlCFMMaTable_Object = MibTable
swL2DevCtrlCFMMaTable = _SwL2DevCtrlCFMMaTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21, 3)
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMMaTable.setStatus("current")
_SwL2DevCtrlCFMMaEntry_Object = MibTableRow
swL2DevCtrlCFMMaEntry = _SwL2DevCtrlCFMMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21, 3, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21, 3, 1, 1),
    _SwL2DevCtrlCFMMaMode_Type()
)
swL2DevCtrlCFMMaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMMaMode.setStatus("current")
_SwL2DevCtrlCFMMepTable_Object = MibTable
swL2DevCtrlCFMMepTable = _SwL2DevCtrlCFMMepTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21, 4)
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMMepTable.setStatus("current")
_SwL2DevCtrlCFMMepEntry_Object = MibTableRow
swL2DevCtrlCFMMepEntry = _SwL2DevCtrlCFMMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21, 4, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 21, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 2, 22),
    _SwL2DevCtrlVLANTrunkState_Type()
)
swL2DevCtrlVLANTrunkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlVLANTrunkState.setStatus("current")
_SwL2DevAlarm_ObjectIdentity = ObjectIdentity
swL2DevAlarm = _SwL2DevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 1, 3, 3),
    _SwL2DevAlarmLinkChange_Type()
)
swL2DevAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmLinkChange.setStatus("current")
_SwL2VLANMgmt_ObjectIdentity = ObjectIdentity
swL2VLANMgmt = _SwL2VLANMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2)
)
_SwL2VlanStaticTable_Object = MibTable
swL2VlanStaticTable = _SwL2VlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swL2VlanStaticTable.setStatus("current")
_SwL2VlanStaticEntry_Object = MibTableRow
swL2VlanStaticEntry = _SwL2VlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2, 1, 1)
)
swL2VlanStaticEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2VlanIndex"),
)
if mibBuilder.loadTexts:
    swL2VlanStaticEntry.setStatus("current")
_SwL2VlanIndex_Type = VlanId
_SwL2VlanIndex_Object = MibTableColumn
swL2VlanIndex = _SwL2VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2, 2),
    _SwL2PVIDAutoAssignmentState_Type()
)
swL2PVIDAutoAssignmentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PVIDAutoAssignmentState.setStatus("current")
_SwL2VlanPortInfoTable_Object = MibTable
swL2VlanPortInfoTable = _SwL2VlanPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2, 3)
)
if mibBuilder.loadTexts:
    swL2VlanPortInfoTable.setStatus("current")
_SwL2VlanPortInfoEntry_Object = MibTableRow
swL2VlanPortInfoEntry = _SwL2VlanPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2, 3, 1)
)
swL2VlanPortInfoEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2VlanPortInfoPortIndex"),
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2VlanPortInfoVid"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2, 3, 1, 1),
    _SwL2VlanPortInfoPortIndex_Type()
)
swL2VlanPortInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanPortInfoPortIndex.setStatus("current")
_SwL2VlanPortInfoVid_Type = VlanId
_SwL2VlanPortInfoVid_Object = MibTableColumn
swL2VlanPortInfoVid = _SwL2VlanPortInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2, 3, 1, 3),
    _SwL2VlanPortInfoPortRole_Type()
)
swL2VlanPortInfoPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanPortInfoPortRole.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 2, 6),
    _SwL2NniGvrpBpduAddress_Type()
)
swL2NniGvrpBpduAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2NniGvrpBpduAddress.setStatus("current")
_SwL2PortMgmt_ObjectIdentity = ObjectIdentity
swL2PortMgmt = _SwL2PortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3)
)
_SwL2PortInfoTable_Object = MibTable
swL2PortInfoTable = _SwL2PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 1)
)
if mibBuilder.loadTexts:
    swL2PortInfoTable.setStatus("current")
_SwL2PortInfoEntry_Object = MibTableRow
swL2PortInfoEntry = _SwL2PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 1, 1)
)
swL2PortInfoEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2PortInfoPortIndex"),
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2PortInfoMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 1, 1, 6),
    _SwL2PortInfoNwayStatus_Type()
)
swL2PortInfoNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoNwayStatus.setStatus("current")


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
              6)
        )
    )
    namedValues = NamedValues(
        *(("bpdu-protection", 5),
          ("ctp-lbd", 3),
          ("ddm", 4),
          ("none", 0),
          ("storm", 1),
          ("stp-lbd", 2),
          ("unknow", 6))
    )


_SwL2PortInfoErrorDisabled_Type.__name__ = "Integer32"
_SwL2PortInfoErrorDisabled_Object = MibTableColumn
swL2PortInfoErrorDisabled = _SwL2PortInfoErrorDisabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 1, 1, 8),
    _SwL2PortInfoErrorDisabled_Type()
)
swL2PortInfoErrorDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoErrorDisabled.setStatus("current")
_SwL2PortCtrlTable_Object = MibTable
swL2PortCtrlTable = _SwL2PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 2)
)
if mibBuilder.loadTexts:
    swL2PortCtrlTable.setStatus("current")
_SwL2PortCtrlEntry_Object = MibTableRow
swL2PortCtrlEntry = _SwL2PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 2, 1)
)
swL2PortCtrlEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2PortCtrlPortIndex"),
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2PortCtrlMediumType"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 2, 1, 10),
    _SwL2PortCtrlMDIXState_Type()
)
swL2PortCtrlMDIXState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlMDIXState.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 3),
    _SwL2PortCtrlJumboFrame_Type()
)
swL2PortCtrlJumboFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlJumboFrame.setStatus("current")
_SwL2PortCtrlJumboFrameMaxSize_Type = Integer32
_SwL2PortCtrlJumboFrameMaxSize_Object = MibScalar
swL2PortCtrlJumboFrameMaxSize = _SwL2PortCtrlJumboFrameMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 4),
    _SwL2PortCtrlJumboFrameMaxSize_Type()
)
swL2PortCtrlJumboFrameMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlJumboFrameMaxSize.setStatus("current")
_SwL2PortCounterCtrlTable_Object = MibTable
swL2PortCounterCtrlTable = _SwL2PortCounterCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 6)
)
if mibBuilder.loadTexts:
    swL2PortCounterCtrlTable.setStatus("current")
_SwL2PortCounterCtrlEntry_Object = MibTableRow
swL2PortCounterCtrlEntry = _SwL2PortCounterCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 6, 1)
)
swL2PortCounterCtrlEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2PortCounterCtrlPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 6, 1, 2),
    _SwL2PortCounterClearCtrl_Type()
)
swL2PortCounterClearCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCounterClearCtrl.setStatus("current")
_SwL2PortJumboFrameCtrlTable_Object = MibTable
swL2PortJumboFrameCtrlTable = _SwL2PortJumboFrameCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 10)
)
if mibBuilder.loadTexts:
    swL2PortJumboFrameCtrlTable.setStatus("current")
_SwL2PortJumboFrameCtrlEntry_Object = MibTableRow
swL2PortJumboFrameCtrlEntry = _SwL2PortJumboFrameCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 10, 1)
)
swL2PortJumboFrameCtrlEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2PortJumboFrameCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortJumboFrameCtrlEntry.setStatus("current")


class _SwL2PortJumboFrameCtrlPortIndex_Type(Integer32):
    """Custom type swL2PortJumboFrameCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2PortJumboFrameCtrlPortIndex_Type.__name__ = "Integer32"
_SwL2PortJumboFrameCtrlPortIndex_Object = MibTableColumn
swL2PortJumboFrameCtrlPortIndex = _SwL2PortJumboFrameCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 10, 1, 1),
    _SwL2PortJumboFrameCtrlPortIndex_Type()
)
swL2PortJumboFrameCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortJumboFrameCtrlPortIndex.setStatus("current")


class _SwL2PortJumboFrameCtrlPortState_Type(Integer32):
    """Custom type swL2PortJumboFrameCtrlPortState based on Integer32"""
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


_SwL2PortJumboFrameCtrlPortState_Type.__name__ = "Integer32"
_SwL2PortJumboFrameCtrlPortState_Object = MibTableColumn
swL2PortJumboFrameCtrlPortState = _SwL2PortJumboFrameCtrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 3, 10, 1, 2),
    _SwL2PortJumboFrameCtrlPortState_Type()
)
swL2PortJumboFrameCtrlPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortJumboFrameCtrlPortState.setStatus("current")
_SwL2TrunkMgmt_ObjectIdentity = ObjectIdentity
swL2TrunkMgmt = _SwL2TrunkMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 2),
    _SwL2TrunkCurrentNumEntries_Type()
)
swL2TrunkCurrentNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkCurrentNumEntries.setStatus("current")
_SwL2TrunkCtrlTable_Object = MibTable
swL2TrunkCtrlTable = _SwL2TrunkCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 3)
)
if mibBuilder.loadTexts:
    swL2TrunkCtrlTable.setStatus("current")
_SwL2TrunkCtrlEntry_Object = MibTableRow
swL2TrunkCtrlEntry = _SwL2TrunkCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 3, 1)
)
swL2TrunkCtrlEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2TrunkIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 3, 1, 1),
    _SwL2TrunkIndex_Type()
)
swL2TrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkIndex.setStatus("current")


class _SwL2TrunkMasterPort_Type(Integer32):
    """Custom type swL2TrunkMasterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2TrunkMasterPort_Type.__name__ = "Integer32"
_SwL2TrunkMasterPort_Object = MibTableColumn
swL2TrunkMasterPort = _SwL2TrunkMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 3, 1, 3),
    _SwL2TrunkMasterPort_Type()
)
swL2TrunkMasterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkMasterPort.setStatus("current")
_SwL2TrunkMember_Type = PortList
_SwL2TrunkMember_Object = MibTableColumn
swL2TrunkMember = _SwL2TrunkMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 3, 1, 6),
    _SwL2TrunkType_Type()
)
swL2TrunkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2TrunkType.setStatus("current")
_SwL2TrunkState_Type = RowStatus
_SwL2TrunkState_Object = MibTableColumn
swL2TrunkState = _SwL2TrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 4),
    _SwL2TrunkAlgorithm_Type()
)
swL2TrunkAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkAlgorithm.setStatus("current")
_SwL2TrunkLACPPortTable_Object = MibTable
swL2TrunkLACPPortTable = _SwL2TrunkLACPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 5)
)
if mibBuilder.loadTexts:
    swL2TrunkLACPPortTable.setStatus("current")
_SwL2TrunkLACPPortEntry_Object = MibTableRow
swL2TrunkLACPPortEntry = _SwL2TrunkLACPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 5, 1)
)
swL2TrunkLACPPortEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2TrunkLACPPortIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 5, 1, 2),
    _SwL2TrunkLACPPortState_Type()
)
swL2TrunkLACPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkLACPPortState.setStatus("current")
_SwL2TrunkVLANTable_Object = MibTable
swL2TrunkVLANTable = _SwL2TrunkVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 6)
)
if mibBuilder.loadTexts:
    swL2TrunkVLANTable.setStatus("current")
_SwL2TrunkVLANEntry_Object = MibTableRow
swL2TrunkVLANEntry = _SwL2TrunkVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 6, 1)
)
swL2TrunkVLANEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2TrunkVLANPort"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 9, 6, 1, 2),
    _SwL2TrunkVLANState_Type()
)
swL2TrunkVLANState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkVLANState.setStatus("current")
_SwL2MirrorMgmt_ObjectIdentity = ObjectIdentity
swL2MirrorMgmt = _SwL2MirrorMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 1),
    _SwL2MirrorLogicTargetPort_Type()
)
swL2MirrorLogicTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorLogicTargetPort.setStatus("current")
_SwL2MirrorPortSourceIngress_Type = PortList
_SwL2MirrorPortSourceIngress_Object = MibScalar
swL2MirrorPortSourceIngress = _SwL2MirrorPortSourceIngress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 2),
    _SwL2MirrorPortSourceIngress_Type()
)
swL2MirrorPortSourceIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortSourceIngress.setStatus("current")
_SwL2MirrorPortSourceEgress_Type = PortList
_SwL2MirrorPortSourceEgress_Object = MibScalar
swL2MirrorPortSourceEgress = _SwL2MirrorPortSourceEgress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 4),
    _SwL2MirrorPortState_Type()
)
swL2MirrorPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MirrorPortState.setStatus("current")
_SwL2MirrorGroupTable_Object = MibTable
swL2MirrorGroupTable = _SwL2MirrorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 5)
)
if mibBuilder.loadTexts:
    swL2MirrorGroupTable.setStatus("current")
_SwL2MirrorGroupEntry_Object = MibTableRow
swL2MirrorGroupEntry = _SwL2MirrorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 5, 1)
)
swL2MirrorGroupEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2MirrorGroupID"),
)
if mibBuilder.loadTexts:
    swL2MirrorGroupEntry.setStatus("current")
_SwL2MirrorGroupID_Type = Integer32
_SwL2MirrorGroupID_Object = MibTableColumn
swL2MirrorGroupID = _SwL2MirrorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 5, 1, 1),
    _SwL2MirrorGroupID_Type()
)
swL2MirrorGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2MirrorGroupID.setStatus("current")
_SwL2MirrorGroupRowStatus_Type = RowStatus
_SwL2MirrorGroupRowStatus_Object = MibTableColumn
swL2MirrorGroupRowStatus = _SwL2MirrorGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 5, 1, 3),
    _SwL2MirrorGroupState_Type()
)
swL2MirrorGroupState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupState.setStatus("current")


class _SwL2MirrorGroupLogicTargetPort_Type(Integer32):
    """Custom type swL2MirrorGroupLogicTargetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2MirrorGroupLogicTargetPort_Type.__name__ = "Integer32"
_SwL2MirrorGroupLogicTargetPort_Object = MibTableColumn
swL2MirrorGroupLogicTargetPort = _SwL2MirrorGroupLogicTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 5, 1, 4),
    _SwL2MirrorGroupLogicTargetPort_Type()
)
swL2MirrorGroupLogicTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupLogicTargetPort.setStatus("current")
_SwL2MirrorGroupPortSourceIngress_Type = PortList
_SwL2MirrorGroupPortSourceIngress_Object = MibTableColumn
swL2MirrorGroupPortSourceIngress = _SwL2MirrorGroupPortSourceIngress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 5, 1, 5),
    _SwL2MirrorGroupPortSourceIngress_Type()
)
swL2MirrorGroupPortSourceIngress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupPortSourceIngress.setStatus("current")
_SwL2MirrorGroupPortSourceEngress_Type = PortList
_SwL2MirrorGroupPortSourceEngress_Object = MibTableColumn
swL2MirrorGroupPortSourceEngress = _SwL2MirrorGroupPortSourceEngress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 10, 5, 1, 6),
    _SwL2MirrorGroupPortSourceEngress_Type()
)
swL2MirrorGroupPortSourceEngress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2MirrorGroupPortSourceEngress.setStatus("current")
_SwL2TrafficSegMgmt_ObjectIdentity = ObjectIdentity
swL2TrafficSegMgmt = _SwL2TrafficSegMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 14)
)
_SwL2TrafficSegTable_Object = MibTable
swL2TrafficSegTable = _SwL2TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 14, 1)
)
if mibBuilder.loadTexts:
    swL2TrafficSegTable.setStatus("current")
_SwL2TrafficSegEntry_Object = MibTableRow
swL2TrafficSegEntry = _SwL2TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 14, 1, 1)
)
swL2TrafficSegEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2TrafficSegPort"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 14, 1, 1, 1),
    _SwL2TrafficSegPort_Type()
)
swL2TrafficSegPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficSegPort.setStatus("current")
_SwL2TrafficSegForwardPorts_Type = PortList
_SwL2TrafficSegForwardPorts_Object = MibTableColumn
swL2TrafficSegForwardPorts = _SwL2TrafficSegForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 14, 1, 1, 2),
    _SwL2TrafficSegForwardPorts_Type()
)
swL2TrafficSegForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficSegForwardPorts.setStatus("current")
_SwL2MulticastFilterMode_ObjectIdentity = ObjectIdentity
swL2MulticastFilterMode = _SwL2MulticastFilterMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 17)
)
_SwL2MulticastFilterModeVlanTable_Object = MibTable
swL2MulticastFilterModeVlanTable = _SwL2MulticastFilterModeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 17, 1)
)
if mibBuilder.loadTexts:
    swL2MulticastFilterModeVlanTable.setStatus("current")
_SwL2MulticastFilterModeVlanEntry_Object = MibTableRow
swL2MulticastFilterModeVlanEntry = _SwL2MulticastFilterModeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 17, 1, 1)
)
swL2MulticastFilterModeVlanEntry.setIndexNames(
    (0, "DGS-3620-28SC-DC-L2MGMT-MIB", "swL2MulticastFilterVid"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 17, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 17, 1, 1, 2),
    _SwL2MulticastFilterVlanMode_Type()
)
swL2MulticastFilterVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MulticastFilterVlanMode.setStatus("current")
_SwL2MgmtMIBTraps_ObjectIdentity = ObjectIdentity
swL2MgmtMIBTraps = _SwL2MgmtMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100)
)
_SwL2Notify_ObjectIdentity = ObjectIdentity
swL2Notify = _SwL2Notify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100, 1)
)
_SwL2NotifyMgmt_ObjectIdentity = ObjectIdentity
swL2NotifyMgmt = _SwL2NotifyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100, 1, 1)
)
_SwL2macNotificationSeverity_Type = AgentNotifyLevel
_SwL2macNotificationSeverity_Object = MibScalar
swL2macNotificationSeverity = _SwL2macNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100, 1, 1, 1),
    _SwL2macNotificationSeverity_Type()
)
swL2macNotificationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2macNotificationSeverity.setStatus("current")
_SwL2PortSecurityViolationSeverity_Type = AgentNotifyLevel
_SwL2PortSecurityViolationSeverity_Object = MibScalar
swL2PortSecurityViolationSeverity = _SwL2PortSecurityViolationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100, 1, 1, 2),
    _SwL2PortSecurityViolationSeverity_Type()
)
swL2PortSecurityViolationSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityViolationSeverity.setStatus("current")
_SwL2NotifyPrefix_ObjectIdentity = ObjectIdentity
swL2NotifyPrefix = _SwL2NotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100, 1, 2)
)
_SwL2NotifFirmware_ObjectIdentity = ObjectIdentity
swL2NotifFirmware = _SwL2NotifFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100, 1, 2, 0)
)
_Swl2NotificationBidings_ObjectIdentity = ObjectIdentity
swl2NotificationBidings = _Swl2NotificationBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100, 1, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100, 1, 2, 1, 1),
    _SwL2macNotifyInfo_Type()
)
swL2macNotifyInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2macNotifyInfo.setStatus("current")
_SwL2PortSecurityViolationMac_Type = MacAddress
_SwL2PortSecurityViolationMac_Object = MibScalar
swL2PortSecurityViolationMac = _SwL2PortSecurityViolationMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100, 1, 2, 1, 2),
    _SwL2PortSecurityViolationMac_Type()
)
swL2PortSecurityViolationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swL2PortSecurityViolationMac.setStatus("current")

# Managed Objects groups


# Notification objects

swL2macNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100, 1, 2, 0, 1)
)
swL2macNotification.setObjects(
    ("DGS-3620-28SC-DC-L2MGMT-MIB", "swL2macNotifyInfo")
)
if mibBuilder.loadTexts:
    swL2macNotification.setStatus(
        "current"
    )

swL2PortSecurityViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9, 2, 100, 1, 2, 0, 2)
)
swL2PortSecurityViolationTrap.setObjects(
      *(("PORT-SECURITY-MIB", "swPortSecPortIndex"),
        ("DGS-3620-28SC-DC-L2MGMT-MIB", "swL2PortSecurityViolationMac"))
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
    "DGS-3620-28SC-DC-L2MGMT-MIB",
    **{"MacAddress": MacAddress,
       "VlanId": VlanId,
       "PortList": PortList,
       "IANAifMauAutoNegCapBits": IANAifMauAutoNegCapBits,
       "swL2MgmtMIB": swL2MgmtMIB,
       "swL2DevMgmt": swL2DevMgmt,
       "swL2DevInfo": swL2DevInfo,
       "swDevInfoTotalNumOfPort": swDevInfoTotalNumOfPort,
       "swDevInfoNumOfPortInUse": swDevInfoNumOfPortInUse,
       "swL2DevCtrl": swL2DevCtrl,
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
       "swL2PortCtrlJumboFrame": swL2PortCtrlJumboFrame,
       "swL2PortCtrlJumboFrameMaxSize": swL2PortCtrlJumboFrameMaxSize,
       "swL2PortCounterCtrlTable": swL2PortCounterCtrlTable,
       "swL2PortCounterCtrlEntry": swL2PortCounterCtrlEntry,
       "swL2PortCounterCtrlPortIndex": swL2PortCounterCtrlPortIndex,
       "swL2PortCounterClearCtrl": swL2PortCounterClearCtrl,
       "swL2PortJumboFrameCtrlTable": swL2PortJumboFrameCtrlTable,
       "swL2PortJumboFrameCtrlEntry": swL2PortJumboFrameCtrlEntry,
       "swL2PortJumboFrameCtrlPortIndex": swL2PortJumboFrameCtrlPortIndex,
       "swL2PortJumboFrameCtrlPortState": swL2PortJumboFrameCtrlPortState,
       "swL2TrunkMgmt": swL2TrunkMgmt,
       "swL2TrunkMaxSupportedEntries": swL2TrunkMaxSupportedEntries,
       "swL2TrunkCurrentNumEntries": swL2TrunkCurrentNumEntries,
       "swL2TrunkCtrlTable": swL2TrunkCtrlTable,
       "swL2TrunkCtrlEntry": swL2TrunkCtrlEntry,
       "swL2TrunkIndex": swL2TrunkIndex,
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
       "swL2MirrorGroupLogicTargetPort": swL2MirrorGroupLogicTargetPort,
       "swL2MirrorGroupPortSourceIngress": swL2MirrorGroupPortSourceIngress,
       "swL2MirrorGroupPortSourceEngress": swL2MirrorGroupPortSourceEngress,
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
       "swL2MgmtMIBTraps": swL2MgmtMIBTraps,
       "swL2Notify": swL2Notify,
       "swL2NotifyMgmt": swL2NotifyMgmt,
       "swL2macNotificationSeverity": swL2macNotificationSeverity,
       "swL2PortSecurityViolationSeverity": swL2PortSecurityViolationSeverity,
       "swL2NotifyPrefix": swL2NotifyPrefix,
       "swL2NotifFirmware": swL2NotifFirmware,
       "swL2macNotification": swL2macNotification,
       "swL2PortSecurityViolationTrap": swL2PortSecurityViolationTrap,
       "swl2NotificationBidings": swl2NotificationBidings,
       "swL2macNotifyInfo": swL2macNotifyInfo,
       "swL2PortSecurityViolationMac": swL2PortSecurityViolationMac}
)
